from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch


OUT = "/Users/cbottrell/Documents/Codex/2026-07-19/mak/outputs/llm-pretraining-schematic-vector.pdf"
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
CHARCOAL = "#425563"

pdfmetrics.registerFont(TTFont("Arial", "/System/Library/Fonts/Supplemental/Arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", "/System/Library/Fonts/Supplemental/Arial Bold.ttf"))
pdfmetrics.registerFont(TTFont("Georgia-Bold", "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"))

c = canvas.Canvas(OUT, pagesize=(PAGE_W, PAGE_H), pageCompression=1)
c.setTitle("LLM Pretraining: From Raw Text to a Base Model")
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


def multiline_mid(x, y, value, size, face="Arial", colour=NAVY, align="left", spacing=None):
    lines = value.split("\n")
    spacing = spacing or size * 1.02
    top = y - (len(lines) - 1) * spacing / 2
    for idx, row in enumerate(lines):
        text_mid(x, top + idx * spacing, row.strip(), size, face, colour, align)


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


def books_icon(x, y):
    for idx, (colour, width) in enumerate(zip((LIME, GREEN, NAVY), (49, 42, 54))):
        yy = y + idx * 13
        rounded_rect((x, yy, x + width, yy + 10), 2, colour)
        line((x + 7, yy + 2, x + 7, yy + 8), BG, 1)


def website_icon(x, y):
    rounded_rect((x, y, x + 52, y + 40), 5, BG, GREEN, 2)
    line((x, y + 11, x + 52, y + 11), GREEN, 2)
    for dot_x in (x + 7, x + 13, x + 19):
        ellipse((dot_x - 2, y + 5, dot_x + 2, y + 9), fill=GREEN)
    ellipse((x + 18, y + 17, x + 37, y + 35), outline=GREEN, width=1)
    line((x + 18, y + 26, x + 37, y + 26), GREEN, 1)
    line((x + 27.5, y + 17, x + 27.5, y + 35), GREEN, 1)


def paper_icon(x, y):
    poly([(x, y), (x + 40, y), (x + 52, y + 12), (x + 52, y + 47), (x, y + 47)], BG, GREEN, 1)
    line((x + 40, y, x + 40, y + 12, x + 52, y + 12), GREEN, 1)
    line((x + 9, y + 18, x + 42, y + 18), GREEN, 2)
    line((x + 9, y + 26, x + 42, y + 26), GREY, 1)
    line((x + 9, y + 33, x + 37, y + 33), GREY, 1)
    line((x + 9, y + 40, x + 30, y + 40), GREY, 1)


def code_icon(x, y):
    rounded_rect((x, y, x + 54, y + 42), 5, NAVY)
    text_mid(x + 27, y + 21, "</>", 20, "Arial-Bold", BG, "center")


def news_icon(x, y):
    rounded_rect((x, y, x + 53, y + 43), 3, BG, NAVY, 1)
    rounded_rect((x + 6, y + 7, x + 24, y + 24), 2, PALE, GREEN, 1)
    line((x + 29, y + 8, x + 47, y + 8), NAVY, 2)
    line((x + 29, y + 15, x + 47, y + 15), GREY, 1)
    line((x + 29, y + 22, x + 44, y + 22), GREY, 1)
    line((x + 6, y + 31, x + 47, y + 31), GREY, 1)
    line((x + 6, y + 37, x + 39, y + 37), GREY, 1)


def encyclopedia_icon(x, y):
    poly([(x + 3, y + 5), (x + 25, y), (x + 25, y + 41), (x + 3, y + 46)], PALE, GREEN, 1)
    poly([(x + 27, y), (x + 49, y + 5), (x + 49, y + 46), (x + 27, y + 41)], PALE, GREEN, 1)
    line((x + 26, y + 2, x + 26, y + 41), GREEN, 2)


def corpus_tile(x, y, label, fill, icon_fn):
    rounded_rect((x, y, x + 216, y + 100), 11, fill, LINE, 1)
    multiline_mid(x + 80, y + 50, label, 24, "Arial", NAVY, "left", 25)
    icon_fn(x + 13, y + 28)


def gpu_rack(x, y, w=74, h=270):
    rounded_rect((x, y, x + w, y + h), 8, NAVY, NAVY, 1)
    rounded_rect((x + 7, y + 8, x + w - 7, y + h - 8), 4, CHARCOAL)
    for row in range(11):
        yy = y + 14 + row * 22
        rounded_rect((x + 12, yy, x + w - 12, yy + 18), 3, GREEN, BLUE_GREY, 1)
        ellipse((x + 18, yy + 6, x + 24, yy + 12), fill=LIME)
        line((x + 30, yy + 6, x + w - 18, yy + 6), PALE, 1)
        line((x + 30, yy + 12, x + w - 24, yy + 12), PALE, 1)


def file_card_icon(x, y, size, accent, icon_kind):
    rounded_rect((x, y, x + size, y + size), 7, accent)
    if icon_kind == "parameters":
        left_nodes = [(x + 10, y + 10), (x + 10, y + 19), (x + 10, y + 28)]
        right_nodes = [(x + 28, y + 11), (x + 28, y + 20), (x + 28, y + 29)]
        for x1, y1 in left_nodes:
            for x2, y2 in right_nodes:
                line((x1, y1, x2, y2), BG, 1)
        for cx, cy in left_nodes + right_nodes:
            ellipse((cx - 2.5, cy - 2.5, cx + 2.5, cy + 2.5), fill=BG)
    else:
        for yy, knob_x in ((11, 24), (19, 15), (27, 27)):
            line((x + 8, y + yy, x + 30, y + yy), BG, 1)
            ellipse((x + knob_x - 3, y + yy - 3, x + knob_x + 3, y + yy + 3), fill=accent, outline=BG, width=1)


def file_card(x, y, title, filename, details, accent, icon_kind):
    w, h = 390, 245
    rounded_rect((x + 8, y + 8, x + w + 8, y + h + 8), 14, PALE, LINE, 1)
    rounded_rect((x, y, x + w, y + h), 14, BG, LINE, 1)
    fold = 42
    poly([(x + w - fold, y), (x + w, y + fold), (x + w - fold, y + fold)], PALE, accent, 1)
    line((x + w - fold, y, x + w - fold, y + fold, x + w, y + fold), accent, 1)
    file_card_icon(x + 22, y + 21, 38, accent, icon_kind)
    text_top(x + 76, y + 28, title, 20, "Arial-Bold")
    text_top(x + 76, y + 53, filename, 14, "Arial", GREY_TEXT)
    for idx, detail in enumerate(details):
        text_top(x + 22, y + 91 + idx * 25, detail, 17 if idx == 0 else 15, "Arial", NAVY if idx == 0 else GREY_TEXT)


# Background and title
rounded_rect((0, 0, W, H), 0, BG)
text_top(900, 72, "LLM PRETRAINING: FROM RAW TEXT TO A BASE MODEL", 32, "Georgia-Bold", NAVY, "center")
text_top(900, 112, "Learning to predict the next token across massive amounts of text", 18, "Arial", GREY_TEXT, "center")

# Corpus panel
rounded_rect((42, 196, 558, 724), 18, PALEST, BLUE_GREY, 1)
text_top(300, 232, "ENORMOUS TEXT CORPUS", 25, "Arial-Bold", NAVY, "center")
text_top(300, 265, "Diverse sources converted into training tokens", 16, "Arial", GREY_TEXT, "center")
corpus_tile(72, 291, "Books", PALE, books_icon)
corpus_tile(310, 291, "Websites", PALE_GREEN, website_icon)
corpus_tile(72, 414, "Scientific\nPapers", PALE, paper_icon)
corpus_tile(310, 414, "Code", PALE_LIME, code_icon)
corpus_tile(72, 537, "News\nArticles", PALE_LIME, news_icon)
corpus_tile(310, 537, "Reference\nWorks", PALE, encyclopedia_icon)
rounded_rect((141, 662, 459, 700), 19, PALE, BLUE_GREY, 1)
text_mid(300, 681, "MASSIVE SEQUENCE OF TOKENS", 15, "Arial", GREEN, "center")

# Corpus to compute
multiline_mid(631, 344, "TOKENISE,\nSHUFFLE &\nSTREAM\nBATCHES", 14, "Arial", GREY_TEXT, "center", 15)
arrow(576, 435, 687, 435)

# Supercomputer panel
rounded_rect((704, 196, 1226, 724), 18, PALE, BLUE_GREY, 1)
text_top(965, 232, "SUPERCOMPUTER", 25, "Arial-Bold", NAVY, "center")
rounded_rect((805, 265, 1125, 310), 20, PALE_LIME, GREEN, 1)
text_mid(965, 290, "~6,000 HIGH-PERFORMANCE GPUs", 16, "Arial", GREEN, "center")
for rack_x in (739, 830, 921, 1012, 1103):
    gpu_rack(rack_x, 320)
rounded_rect((777, 630, 1153, 700), 12, BG, LINE, 1)
text_mid(965, 654, "Next-token predictions", 20, "Arial", GREEN, "center")
text_mid(965, 681, "+ gradient-based parameter updates", 20, "Arial", GREEN, "center")

# Compute to files
multiline_mid(1302, 344, "TRAINING\nWRITES\nLEARNED\nSTATE", 14, "Arial", GREY_TEXT, "center", 15)
arrow(1243, 435, 1362, 435)

# Output files
file_card(
    1380,
    196,
    "PARAMETERS",
    "checkpoint weights (often sharded)",
    [
        ">100 billion learned parameters",
        "~200+ GB at FP16/BF16",
        "~50-100 GB when quantised to 4-8 bit",
        "Weights and biases encoding learned patterns",
    ],
    GREEN,
    "parameters",
)
file_card(
    1380,
    460,
    "MODEL CONFIG",
    "model_config.json",
    [
        "Architecture and hyperparameters",
        "Layers | width | attention | context length",
        "Typically ~1-10 kB",
        "Usually tens of JSON lines - not code",
    ],
    NAVY,
    "config",
)

c.showPage()
c.save()
