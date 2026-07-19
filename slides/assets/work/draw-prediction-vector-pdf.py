from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch


OUT = "/Users/cbottrell/Documents/Codex/2026-07-19/mak/outputs/llm-next-token-schematic-vector.pdf"
W, H = 1600, 900
PAGE_W, PAGE_H = 16 * inch, 9 * inch
SX, SY = PAGE_W / W, PAGE_H / H

BG = "#ffffff"
NAVY = "#253746"
GREEN = "#28724f"
BLUE_GREY = "#7a99ac"
PALE = "#f0f4f6"
LIME = "#d0df00"
GREY = "#abb8c3"
GREY_TEXT = "#808491"
LINE = "#ccd5df"

pdfmetrics.registerFont(TTFont("Arial", "/System/Library/Fonts/Supplemental/Arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", "/System/Library/Fonts/Supplemental/Arial Bold.ttf"))

c = canvas.Canvas(OUT, pagesize=(PAGE_W, PAGE_H), pageCompression=1)
c.setTitle("LLM Next-Token Prediction Schematic")
c.setAuthor("Codex")


def X(x):
    return x * SX


def Y(y):
    return PAGE_H - y * SY


def set_fill(colour):
    c.setFillColor(HexColor(colour))


def set_stroke(colour):
    c.setStrokeColor(HexColor(colour))


def rounded_rect(coords, radius, fill, outline=None, width=1):
    x1, y1, x2, y2 = coords
    set_fill(fill)
    if outline:
        set_stroke(outline)
        c.setLineWidth(width * SX)
    c.roundRect(
        X(x1),
        Y(y2),
        X(x2 - x1),
        SY * (y2 - y1),
        radius * SX,
        stroke=1 if outline else 0,
        fill=1,
    )


def line(points, colour, width=1):
    path = c.beginPath()
    path.moveTo(X(points[0]), Y(points[1]))
    for idx in range(2, len(points), 2):
        path.lineTo(X(points[idx]), Y(points[idx + 1]))
    set_stroke(colour)
    c.setLineWidth(width * SX)
    c.setLineCap(1)
    c.setLineJoin(1)
    c.drawPath(path, stroke=1, fill=0)


def poly(points, fill, outline=None, width=1):
    path = c.beginPath()
    path.moveTo(X(points[0][0]), Y(points[0][1]))
    for x, y in points[1:]:
        path.lineTo(X(x), Y(y))
    path.close()
    set_fill(fill)
    if outline:
        set_stroke(outline)
        c.setLineWidth(width * SX)
    c.drawPath(path, stroke=1 if outline else 0, fill=1)


def ellipse(coords, fill=None, outline=None, width=1):
    x1, y1, x2, y2 = coords
    if fill:
        set_fill(fill)
    if outline:
        set_stroke(outline)
        c.setLineWidth(width * SX)
    c.ellipse(
        X(x1),
        Y(y2),
        X(x2),
        Y(y1),
        stroke=1 if outline else 0,
        fill=1 if fill else 0,
    )


def text_top(x, y, value, size, face="Arial", colour=NAVY, align="left"):
    c.setFont(face, size * SX)
    set_fill(colour)
    baseline = Y(y + size * 0.9)
    if align == "center":
        c.drawCentredString(X(x), baseline, value)
    elif align == "right":
        c.drawRightString(X(x), baseline, value)
    else:
        c.drawString(X(x), baseline, value)


def text_mid(x, y, value, size, face="Arial", colour=NAVY, align="left"):
    c.setFont(face, size * SX)
    set_fill(colour)
    baseline = Y(y + size * 0.32)
    if align == "center":
        c.drawCentredString(X(x), baseline, value)
    elif align == "right":
        c.drawRightString(X(x), baseline, value)
    else:
        c.drawString(X(x), baseline, value)


def arrow(x1, y1, x2, y2, colour=GREEN, width=4, head=13):
    line((x1, y1, x2 - head * 0.65, y2), colour, width)
    poly(
        [
            (x2, y2),
            (x2 - head, y2 - head * 0.72),
            (x2 - head, y2 + head * 0.72),
        ],
        colour,
    )


def down_arrow(x, y1, y2):
    line((x, y1, x, y2 - 6), GREEN, 1)
    poly([(x, y2), (x - 4, y2 - 7), (x + 4, y2 - 7)], GREEN)


# Background
rounded_rect((0, 0, W, H), 0, BG)

# Prompt tokens
text_top(346, 329, "INPUT PROMPT (CONTEXT SO FAR)", 18, "Arial-Bold", NAVY, "center")

tokens = ["I", "saw", "James", "in", "the", "Forrest", "Hall", "kitchen", "eating", "a", "whole"]
x = 28
centers = []
for index, token in enumerate(tokens, start=1):
    text_width = pdfmetrics.stringWidth(token, "Arial", 17 * SX) / SX
    token_width = max(30, text_width + 18)
    rounded_rect((x, 370, x + token_width, 434), 7, PALE, BLUE_GREY, 1)
    cx = x + token_width / 2
    centers.append(cx)
    text_mid(cx, 402, token, 17, "Arial", NAVY, "center")
    down_arrow(cx, 435, 476)
    text_mid(cx, 522, str(index), 16, "Arial", GREEN, "center")
    x += token_width + 7

text_top(6, 486, "Token", 10, "Arial", GREEN)
text_top(6, 500, "position", 10, "Arial", GREEN)

left_x = 28
right_x = x - 7
mid_x = (left_x + right_x) / 2
line((left_x, 558, left_x, 567), GREEN, 1)
line((left_x, 567, left_x + 9, 575), GREEN, 1)
line((left_x + 9, 575, mid_x - 12, 575), GREEN, 1)
line((mid_x - 12, 575, mid_x, 587), GREEN, 1)
line((mid_x, 587, mid_x + 12, 575), GREEN, 1)
line((mid_x + 12, 575, right_x - 9, 575), GREEN, 1)
line((right_x - 9, 575, right_x, 567), GREEN, 1)
line((right_x, 567, right_x, 558), GREEN, 1)
text_top(mid_x, 622, "Each word (token) is fed to the model in order", 18, "Arial", GREEN, "center")
text_top(mid_x, 652, "and forms the context for the next prediction.", 18, "Arial", GREEN, "center")

arrow(693, 402, 726, 402, GREEN, 5, 15)

# LLM panel
text_top(885, 182, "LLM", 31, "Arial-Bold", GREEN, "center")
rounded_rect((738, 215, 1043, 725), 18, PALE, BLUE_GREY, 1)

layers = [
    [(785, 310), (785, 375), (785, 440), (785, 505)],
    [(860, 285), (860, 375), (860, 440), (860, 530)],
    [(935, 285), (935, 375), (935, 440), (935, 530)],
    [(986, 340), (986, 415), (986, 490)],
]
for layer_index in range(len(layers) - 1):
    for x1, y1 in layers[layer_index]:
        for x2, y2 in layers[layer_index + 1]:
            line((x1, y1, x2, y2), GREEN, 1)

for layer_index, layer_nodes in enumerate(layers):
    for cx, cy in layer_nodes:
        radius = 13 if layer_index == 3 else 14
        fill = PALE if layer_index == 3 else GREEN
        ellipse((cx - radius, cy - radius, cx + radius, cy + radius), fill=fill, outline=GREEN, width=1)

for y in (338, 413, 488):
    text_mid(1004, y, "...", 20, "Arial-Bold", GREEN)

for idx, row in enumerate(
    ["The model uses patterns", "learned from vast amounts", "of text to predict the", "next token."]
):
    text_top(890, 592 + idx * 30, row, 18, "Arial-Bold", NAVY, "center")

arrow(1056, 402, 1089, 402, GREEN, 5, 15)

# Output table
text_top(1310, 157, "PREDICTED NEXT TOKEN (OUTPUT)", 20, "Arial-Bold", NAVY, "center")
text_top(1111, 199, "Candidate next token", 15, "Arial", NAVY)
text_top(1492, 199, "Likelihood", 15, "Arial", NAVY, "right")
rounded_rect((1098, 224, 1514, 746), 12, BG, LINE, 1)

rows = [
    ("pizza", "0.46", 173, GREEN, GREEN),
    ("cake", "0.23", 88, LIME, GREEN),
    ("loaf", "0.10", 52, LIME, GREEN),
    ("pie", "0.06", 42, GREY, GREY_TEXT),
    ("lasagne", "0.04", 29, GREY, GREY_TEXT),
    ("chicken", "0.03", 23, GREY, GREY_TEXT),
    ("buffet", "0.02", 16, GREY, GREY_TEXT),
    ("fridge", "0.01", 10, GREY, GREY_TEXT),
    ("experiment", "<0.01", 6, GREY, GREY_TEXT),
]
row_tops = [226, 277, 328, 389, 440, 491, 552, 603, 654]
for idx, ((candidate, likelihood, bar_width, bar_colour, likelihood_colour), top) in enumerate(zip(rows, row_tops)):
    cy = top + 31
    text_mid(1115, cy, candidate, 18, "Arial-Bold", NAVY)
    rounded_rect((1228, top + 15, 1228 + bar_width, top + 39), 4, bar_colour)
    text_mid(1495, cy, likelihood, 18, "Arial-Bold", likelihood_colour, "right")
    if idx < len(rows) - 1:
        line((1112, top + 52, 1497, top + 52), LINE, 1)

for dash_y in (390, 553):
    for dash_x in range(1098, 1514, 16):
        line((dash_x, dash_y, min(dash_x + 8, 1514), dash_y), GREY_TEXT, 1)

axis_y = 758
line((1121, axis_y, 1483, axis_y), NAVY, 1)
for tx, label in ((1121, "0"), (1212, "0.25"), (1302, "0.50"), (1393, "0.75"), (1483, "1.00")):
    line((tx, axis_y, tx, axis_y + 13), NAVY, 1)
    text_mid(tx, 787, label, 14, "Arial", NAVY, "center")

text_mid(1080, 830, "More likely", 16, "Arial", GREEN)
arrow(1191, 830, 1395, 830, NAVY, 1, 8)
text_mid(1420, 830, "Less likely", 16, "Arial", NAVY)

c.showPage()
c.save()
