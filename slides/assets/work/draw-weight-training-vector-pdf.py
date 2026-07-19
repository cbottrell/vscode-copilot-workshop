from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch
from math import cos, hypot, radians, sin


OUT = "/Users/cbottrell/Documents/Codex/2026-07-19/mak/outputs/llm-weight-training-schematic-vector.pdf"
W, H = 1800, 900
PAGE_W, PAGE_H = 18 * inch, 9 * inch
SX, SY = PAGE_W / W, PAGE_H / H

BG = "#ffffff"
NAVY = "#253746"
GREEN = "#28724f"
BLUE_GREY = "#7a99ac"
PALE = "#f0f4f6"
PALEST = "#f7f9fa"
LIME = "#d0df00"
PALE_LIME = "#f3f6d5"
PALE_GREEN = "#e7f0eb"
GREY = "#abb8c3"
GREY_TEXT = "#808491"
LINE = "#ccd5df"

pdfmetrics.registerFont(TTFont("Arial", "/System/Library/Fonts/Supplemental/Arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", "/System/Library/Fonts/Supplemental/Arial Bold.ttf"))
pdfmetrics.registerFont(TTFont("Georgia-Bold", "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"))

c = canvas.Canvas(OUT, pagesize=(PAGE_W, PAGE_H), pageCompression=1)
c.setTitle("How Training Adjusts Model Parameters")
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


def multiline_mid(x, y, rows, size, face="Arial", colour=NAVY, align="center", spacing=None):
    spacing = spacing or size * 1.18
    top = y - (len(rows) - 1) * spacing / 2
    for idx, row in enumerate(rows):
        text_mid(x, top + idx * spacing, row, size, face, colour, align)


def arrow(x1, y1, x2, y2, width=30, head=34, border=4):
    shaft_half = width / 2
    head_half = width * 0.84
    head_base = x2 - head
    outer = [
        (x1, y1 - shaft_half),
        (head_base, y1 - shaft_half),
        (head_base, y1 - head_half),
        (x2, y1),
        (head_base, y1 + head_half),
        (head_base, y1 + shaft_half),
        (x1, y1 + shaft_half),
    ]
    inner_shaft_half = shaft_half - border
    inner_head_half = head_half - border * 1.2
    inner_head_base = head_base + border * 0.7
    inner = [
        (x1 + border, y1 - inner_shaft_half),
        (inner_head_base, y1 - inner_shaft_half),
        (inner_head_base, y1 - inner_head_half),
        (x2 - border * 1.25, y1),
        (inner_head_base, y1 + inner_head_half),
        (inner_head_base, y1 + inner_shaft_half),
        (x1 + border, y1 + inner_shaft_half),
    ]
    poly(outer, NAVY)
    poly(inner, LIME)


def small_arrow(x1, y1, x2, y2, colour=GREEN, width=3, head=10):
    """Draw an arrow that works at any angle."""
    dx, dy = x2 - x1, y2 - y1
    length = hypot(dx, dy)
    if not length:
        return
    ux, uy = dx / length, dy / length
    px, py = -uy, ux
    shaft_x = x2 - ux * head * 0.68
    shaft_y = y2 - uy * head * 0.68
    base_x = x2 - ux * head
    base_y = y2 - uy * head
    line((x1, y1, shaft_x, shaft_y), colour, width)
    poly(
        [
            (x2, y2),
            (base_x + px * head * 0.66, base_y + py * head * 0.66),
            (base_x - px * head * 0.66, base_y - py * head * 0.66),
        ],
        colour,
    )


def section_heading(x, y, step, title):
    rounded_rect((x, y, x + 34, y + 34), 8, GREEN)
    text_mid(x + 17, y + 17, step, 15, "Arial-Bold", BG, "center")
    text_mid(x + 47, y + 17, title, 22, "Arial-Bold", NAVY)


def token_box(x, y, label, width):
    rounded_rect((x, y, x + width, y + 60), 8, PALE, BLUE_GREY, 1)
    text_mid(x + width / 2, y + 30, label, 18, "Arial", NAVY, "center")


def probability_row(x, y, label, probability, bar_colour):
    text_mid(x, y, label, 15, "Arial-Bold", NAVY)
    rounded_rect((x + 65, y - 11, x + 65 + 120 * probability, y + 11), 4, bar_colour)
    text_mid(x + 195, y, f"{probability:.2f}", 15, "Arial-Bold", GREEN, "right")


def dial(cx, cy, radius, value, accent=GREEN, show_value=True):
    ellipse((cx - radius, cy - radius, cx + radius, cy + radius), fill=BG, outline=NAVY, width=1.5)
    for degree in (225, 180, 135, 90, 45, 0, -45):
        angle = radians(degree)
        x1 = cx + radius * 0.72 * cos(angle)
        y1 = cy - radius * 0.72 * sin(angle)
        x2 = cx + radius * 0.90 * cos(angle)
        y2 = cy - radius * 0.90 * sin(angle)
        line((x1, y1, x2, y2), BLUE_GREY, 1)
    needle_angle = radians(225 - (max(-1, min(1, value)) + 1) * 135)
    needle_x = cx + radius * 0.68 * cos(needle_angle)
    needle_y = cy - radius * 0.68 * sin(needle_angle)
    line((cx, cy, needle_x, needle_y), accent, 2.5)
    ellipse((cx - 3, cy - 3, cx + 3, cy + 3), fill=accent)
    if show_value:
        text_top(cx, cy + radius + 5, f"{value:+.2f}", 11, "Arial-Bold", accent, "center")


# Background and title
rounded_rect((0, 0, W, H), 0, BG)
text_top(900, 58, "HOW TRAINING ADJUSTS MODEL PARAMETERS", 32, "Georgia-Bold", NAVY, "center")
text_top(
    900,
    100,
    "Known next tokens provide the error signal used to tune billions of numerical weights",
    18,
    "Arial",
    GREY_TEXT,
    "center",
)

# Main panels
rounded_rect((42, 178, 540, 718), 18, PALEST, BLUE_GREY, 1)
rounded_rect((660, 178, 1180, 718), 18, PALE, BLUE_GREY, 1)
rounded_rect((1300, 178, 1758, 718), 18, PALEST, BLUE_GREY, 1)

# Panel 1 - known example
section_heading(72, 208, "1", "KNOWN TRAINING EXAMPLE")
text_top(72, 258, "The dataset supplies both the context and the answer.", 15, "Arial", GREY_TEXT)

token_specs = [("James", 82), ("ate", 58), ("a", 40), ("whole", 78)]
token_x = 75
for label, width in token_specs:
    token_box(token_x, 322, label, width)
    token_x += width + 10

line((84, 410, 486, 410), BLUE_GREY, 1)
text_top(291, 424, "CONTEXT", 13, "Arial-Bold", BLUE_GREY, "center")

rounded_rect((194, 445, 388, 503), 10, PALE_LIME, GREEN, 2)
text_top(291, 456, "KNOWN TARGET", 12, "Arial-Bold", GREEN, "center")
text_mid(291, 488, "pizza", 22, "Arial-Bold", NAVY, "center")

rounded_rect((74, 552, 508, 672), 12, BG, LINE, 1)
text_top(94, 574, "Why the answer matters", 17, "Arial-Bold", NAVY)
text_top(94, 606, "The correct next token lets training measure", 15, "Arial", GREY_TEXT)
text_top(94, 631, "how far the model's prediction was from the target.", 15, "Arial", GREY_TEXT)

# Arrow 1
multiline_mid(600, 361, ["FORWARD", "PASS"], 14, "Arial-Bold", GREY_TEXT)
arrow(555, 430, 646, 430)

# Panel 2 - parameters and prediction
section_heading(690, 208, "2", "WEIGHTS CREATE A PREDICTION")
text_top(690, 258, "Parameters are adjustable numbers in weight matrices and bias vectors.", 15, "Arial", GREY_TEXT)

layers = [
    [(718, 340), (718, 410), (718, 480)],
    [(810, 320), (810, 380), (810, 440), (810, 500)],
    [(900, 350), (900, 420), (900, 490)],
]
for layer_idx in range(len(layers) - 1):
    for x1, y1 in layers[layer_idx]:
        for x2, y2 in layers[layer_idx + 1]:
            line((x1, y1, x2, y2), GREEN, 1.1)
for layer in layers:
    for cx, cy in layer:
        ellipse((cx - 12, cy - 12, cx + 12, cy + 12), fill=GREEN, outline=GREEN, width=1)

# Selected weights shown as adjustable dials
for x, y, value in ((757, 347, 0.42), (756, 432, -0.18), (849, 466, 0.07)):
    dial(x, y, 15, value, GREEN, False)
    text_top(x, y + 18, f"{value:+.2f}", 10, "Arial-Bold", NAVY, "center")

text_top(958, 310, "MODEL PREDICTION", 13, "Arial-Bold", BLUE_GREY)
probability_row(958, 352, "pizza", 0.31, GREEN)
probability_row(958, 397, "cake", 0.28, LIME)
probability_row(958, 442, "loaf", 0.12, GREY)
probability_row(958, 487, "pie", 0.08, GREY)

rounded_rect((690, 550, 1148, 683), 12, BG, LINE, 1)
text_top(712, 566, "A tiny sample of parameter dials", 16, "Arial-Bold", NAVY)
text_top(1126, 568, "motion enlarged for clarity", 12, "Arial", GREY_TEXT, "right")
text_top(838, 594, "weight matrix W", 12, "Arial-Bold", BLUE_GREY, "center")
text_top(1090, 594, "bias b", 12, "Arial-Bold", BLUE_GREY, "center")
line((1002, 595, 1002, 670), LINE, 1)
for dial_x, value in zip((735, 805, 875, 945), (0.42, -0.18, 0.07, 0.63)):
    dial(dial_x, 635, 18, value, GREEN, True)
for dial_x, value in zip((1060, 1120), (0.03, -0.11)):
    dial(dial_x, 635, 18, value, NAVY, True)

# Arrow 2
multiline_mid(1240, 354, ["COMPARE WITH", "KNOWN TARGET"], 14, "Arial-Bold", GREY_TEXT)
arrow(1195, 430, 1286, 430)

# Panel 3 - loss and update
section_heading(1330, 208, "3", "COMPARE AND UPDATE")
text_top(1330, 258, "Backpropagation finds how each weight contributed to the error.", 15, "Arial", GREY_TEXT)

rounded_rect((1330, 305, 1515, 365), 10, PALE_GREEN, GREEN, 1)
text_top(1348, 318, "KNOWN TARGET", 12, "Arial-Bold", GREEN)
text_mid(1495, 344, "pizza = 1.00", 17, "Arial-Bold", NAVY, "right")
rounded_rect((1530, 305, 1728, 365), 10, PALE, BLUE_GREY, 1)
text_top(1548, 318, "MODEL OUTPUT", 12, "Arial-Bold", BLUE_GREY)
text_mid(1708, 344, "pizza = 0.31", 17, "Arial-Bold", NAVY, "right")

loss_box = (1350, 416, 1710, 482)
small_arrow(1424, 382, 1518, loss_box[1], GREEN, 3, 10)
small_arrow(1629, 382, 1542, loss_box[1], GREEN, 3, 10)
rounded_rect(loss_box, 12, PALE_LIME, GREEN, 2)
text_mid(1530, 449, "CROSS-ENTROPY LOSS = 1.17", 18, "Arial-Bold", NAVY, "center")

rounded_rect((1330, 500, 1728, 548), 10, NAVY)
text_mid(
    1529,
    524,
    "new weight = old weight - learning rate x gradient",
    14,
    "Arial-Bold",
    BG,
    "center",
)

text_top(1330, 570, "SMALL PARAMETER UPDATES", 13, "Arial-Bold", BLUE_GREY)
updates = [
    ("w1", 0.42, 0.45, 1.00),
    ("w2", -0.18, -0.16, 0.34),
    ("w3", 0.07, 0.05, -0.45),
]
for row_idx, (name, before, after, exaggerated_after) in enumerate(updates):
    yy = 610 + row_idx * 34
    text_mid(1340, yy, name, 14, "Arial-Bold", NAVY)
    dial(1395, yy, 13, before, BLUE_GREY, False)
    text_mid(1420, yy, f"{before:+.2f}", 12, "Arial", GREY_TEXT)
    small_arrow(1475, yy, 1522, yy, GREEN, 2, 8)
    dial(1548, yy, 13, exaggerated_after, GREEN, False)
    text_mid(1573, yy, f"{after:+.2f}", 12, "Arial-Bold", GREEN)

rounded_rect((1642, 575, 1728, 687), 10, PALE_GREEN, GREEN, 1)
text_top(1685, 590, "NEXT PASS", 11, "Arial-Bold", GREEN, "center")
text_mid(1685, 630, "pizza", 17, "Arial-Bold", NAVY, "center")
text_mid(1685, 660, "0.31 -> 0.62", 13, "Arial-Bold", GREEN, "center")

# Repetition band
rounded_rect((222, 760, 1578, 835), 18, PALE_LIME, GREEN, 1.5)
ellipse((250, 779, 288, 817), fill=GREEN)
text_mid(269, 798, "R", 18, "Arial-Bold", BG, "center")
text_top(312, 778, "REPEAT ACROSS MANY BATCHES", 17, "Arial-Bold", GREEN)
text_top(
    312,
    807,
    "Millions or billions of small updates gradually encode statistical patterns in the model's weights.",
    15,
    "Arial",
    NAVY,
)

c.showPage()
c.save()
