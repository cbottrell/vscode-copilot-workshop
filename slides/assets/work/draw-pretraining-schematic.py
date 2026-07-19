from PIL import Image, ImageDraw, ImageFont


SCALE = 4
W, H = 1800, 900


def s(value):
    return int(round(value * SCALE))


def box(coords):
    return tuple(s(v) for v in coords)


BG = "#ffffff"
NAVY = "#253746"
PURPLE = "#28724f"
PURPLE_MID = "#7a99ac"
PURPLE_LIGHT = "#f0f4f6"
PURPLE_PALE = "#f7f9fa"
GREEN = "#28724f"
LIME = "#d0df00"
GREEN_LIGHT = "#f3f6d5"
BLUE_LIGHT = "#f0f4f6"
TEAL_LIGHT = "#e7f0eb"
GOLD_LIGHT = "#f3f6d5"
GREY = "#abb8c3"
GREY_TEXT = "#808491"
LINE = "#ccd5df"

image = Image.new("RGB", (s(W), s(H)), BG)
draw = ImageDraw.Draw(image)

REGULAR = "/System/Library/Fonts/Supplemental/Arial.ttf"
BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
SERIF_BOLD = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"


def font(size, bold=False):
    return ImageFont.truetype(BOLD if bold else REGULAR, s(size))


F13 = font(13)
F14 = font(14)
F15 = font(15)
F16 = font(16)
F17 = font(17)
F18 = font(18)
F18B = font(18, True)
F20B = font(20, True)
F22B = font(22, True)
F25B = font(25, True)
F32B = font(32, True)
F32DISPLAY = ImageFont.truetype(SERIF_BOLD, s(32))


def text_xy(x, y, text, face, fill=NAVY, anchor="la"):
    draw.text((s(x), s(y)), text, font=face, fill=fill, anchor=anchor)


def centered_lines(x, y, lines, face, spacing=25, fill=NAVY):
    for index, line_text in enumerate(lines):
        text_xy(x, y + index * spacing, line_text, face, fill=fill, anchor="ma")


def rounded_rect(coords, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box(coords), radius=s(radius), fill=fill, outline=outline, width=s(width))


def line(coords, fill, width=1, joint="curve"):
    draw.line(box(coords), fill=fill, width=s(width), joint=joint)


def arrow(x1, y1, x2, y2, color=LIME, width=30, head=34, border=4):
    shaft_half = width / 2
    head_half = width * 0.84
    head_base = x2 - head
    outer = [
        (s(x1), s(y1 - shaft_half)),
        (s(head_base), s(y1 - shaft_half)),
        (s(head_base), s(y1 - head_half)),
        (s(x2), s(y1)),
        (s(head_base), s(y1 + head_half)),
        (s(head_base), s(y1 + shaft_half)),
        (s(x1), s(y1 + shaft_half)),
    ]
    inner_shaft_half = shaft_half - border
    inner_head_half = head_half - border * 1.2
    inner_head_base = head_base + border * 0.7
    inner = [
        (s(x1 + border), s(y1 - inner_shaft_half)),
        (s(inner_head_base), s(y1 - inner_shaft_half)),
        (s(inner_head_base), s(y1 - inner_head_half)),
        (s(x2 - border * 1.25), s(y1)),
        (s(inner_head_base), s(y1 + inner_head_half)),
        (s(inner_head_base), s(y1 + inner_shaft_half)),
        (s(x1 + border), s(y1 + inner_shaft_half)),
    ]
    draw.polygon(outer, fill=NAVY)
    draw.polygon(inner, fill=color)


def corpus_tile(x, y, w, h, label, fill):
    rounded_rect((x, y, x + w, y + h), 11, fill, LINE, 1)
    label_size = 24
    label_font = font(label_size)
    text_xy(x + 80, y + h / 2, label, label_font, anchor="lm")


def books_icon(x, y):
    colors = [LIME, GREEN, NAVY]
    widths = [49, 42, 54]
    for idx, (color, width) in enumerate(zip(colors, widths)):
        yy = y + idx * 13
        rounded_rect((x, yy, x + width, yy + 10), 2, color)
        line((x + 7, yy + 2, x + 7, yy + 8), BG, 1)


def website_icon(x, y):
    rounded_rect((x, y, x + 52, y + 40), 5, BG, PURPLE, 2)
    line((x, y + 11, x + 52, y + 11), PURPLE, 2)
    for dot_x in (x + 7, x + 13, x + 19):
        draw.ellipse(box((dot_x - 2, y + 5, dot_x + 2, y + 9)), fill=PURPLE)
    draw.ellipse(box((x + 18, y + 17, x + 37, y + 35)), outline=PURPLE, width=s(1))
    line((x + 18, y + 26, x + 37, y + 26), PURPLE, 1)
    line((x + 27.5, y + 17, x + 27.5, y + 35), PURPLE, 1)


def paper_icon(x, y):
    draw.polygon(
        [
            (s(x), s(y)),
            (s(x + 40), s(y)),
            (s(x + 52), s(y + 12)),
            (s(x + 52), s(y + 47)),
            (s(x), s(y + 47)),
        ],
        fill=BG,
        outline=PURPLE,
    )
    line((x + 40, y, x + 40, y + 12, x + 52, y + 12), PURPLE, 1)
    line((x + 9, y + 18, x + 42, y + 18), PURPLE, 2)
    line((x + 9, y + 26, x + 42, y + 26), GREY, 1)
    line((x + 9, y + 33, x + 37, y + 33), GREY, 1)
    line((x + 9, y + 40, x + 30, y + 40), GREY, 1)


def code_icon(x, y):
    rounded_rect((x, y, x + 54, y + 42), 5, NAVY)
    text_xy(x + 27, y + 21, "</>", F20B, fill=BG, anchor="mm")


def news_icon(x, y):
    rounded_rect((x, y, x + 53, y + 43), 3, BG, NAVY, 1)
    rounded_rect((x + 6, y + 7, x + 24, y + 24), 2, PURPLE_LIGHT, PURPLE, 1)
    line((x + 29, y + 8, x + 47, y + 8), NAVY, 2)
    line((x + 29, y + 15, x + 47, y + 15), GREY, 1)
    line((x + 29, y + 22, x + 44, y + 22), GREY, 1)
    line((x + 6, y + 31, x + 47, y + 31), GREY, 1)
    line((x + 6, y + 37, x + 39, y + 37), GREY, 1)


def encyclopedia_icon(x, y):
    draw.polygon(
        [(s(x + 3), s(y + 5)), (s(x + 25), s(y)), (s(x + 25), s(y + 41)), (s(x + 3), s(y + 46))],
        fill=PURPLE_LIGHT,
        outline=PURPLE,
    )
    draw.polygon(
        [(s(x + 27), s(y)), (s(x + 49), s(y + 5)), (s(x + 49), s(y + 46)), (s(x + 27), s(y + 41))],
        fill=PURPLE_LIGHT,
        outline=PURPLE,
    )
    line((x + 26, y + 2, x + 26, y + 41), PURPLE, 2)


def gpu_rack(x, y, w=74, h=270):
    rounded_rect((x, y, x + w, y + h), 8, NAVY, NAVY, 1)
    rounded_rect((x + 7, y + 8, x + w - 7, y + h - 8), 4, "#425563")
    slot_height = 18
    for row in range(11):
        yy = y + 14 + row * 22
        rounded_rect((x + 12, yy, x + w - 12, yy + slot_height), 3, PURPLE, PURPLE_MID, 1)
        draw.ellipse(box((x + 18, yy + 6, x + 24, yy + 12)), fill=LIME)
        line((x + 30, yy + 6, x + w - 18, yy + 6), PURPLE_LIGHT, 1)
        line((x + 30, yy + 12, x + w - 24, yy + 12), PURPLE_LIGHT, 1)


def chip_badge(x, y, w, h):
    rounded_rect((x, y, x + w, y + h), 12, PURPLE, PURPLE, 1)
    for px in range(int(x + 18), int(x + w - 10), 18):
        line((px, y - 6, px, y), PURPLE, 2)
        line((px, y + h, px, y + h + 6), PURPLE, 2)
    for py in range(int(y + 15), int(y + h - 7), 18):
        line((x - 6, py, x, py), PURPLE, 2)
        line((x + w, py, x + w + 6, py), PURPLE, 2)
    # text_xy(x + w / 2, y + 24, "LLM", F25B, fill=BG, anchor="mm")
    # text_xy(x + w / 2, y + 50, "PRETRAINING", F14, fill=BG, anchor="mm")


def file_card_icon(x, y, size, accent, icon_kind):
    rounded_rect((x, y, x + size, y + size), 7, accent)
    if icon_kind == "parameters":
        left_nodes = [(x + 10, y + 10), (x + 10, y + 19), (x + 10, y + 28)]
        right_nodes = [(x + 28, y + 11), (x + 28, y + 20), (x + 28, y + 29)]
        for x1, y1 in left_nodes:
            for x2, y2 in right_nodes:
                line((x1, y1, x2, y2), BG, 1)
        for cx, cy in left_nodes + right_nodes:
            draw.ellipse(box((cx - 2.5, cy - 2.5, cx + 2.5, cy + 2.5)), fill=BG)
    else:
        slider_rows = [(11, 24), (19, 15), (27, 27)]
        for yy, knob_x in slider_rows:
            line((x + 8, y + yy, x + 30, y + yy), BG, 1)
            draw.ellipse(
                box((x + knob_x - 3, y + yy - 3, x + knob_x + 3, y + yy + 3)),
                fill=accent,
                outline=BG,
                width=s(1),
            )


def file_card(x, y, w, h, title, filename, detail_lines, accent, icon_kind):
    rounded_rect((x + 8, y + 8, x + w + 8, y + h + 8), 14, PURPLE_LIGHT, LINE, 1)
    rounded_rect((x, y, x + w, y + h), 14, BG, LINE, 1)
    fold = 42
    draw.polygon(
        [
            (s(x + w - fold), s(y)),
            (s(x + w), s(y + fold)),
            (s(x + w - fold), s(y + fold)),
        ],
        fill=PURPLE_LIGHT,
        outline=accent,
    )
    line((x + w - fold, y, x + w - fold, y + fold, x + w, y + fold), accent, 1)
    file_card_icon(x + 22, y + 21, 38, accent, icon_kind)
    text_xy(x + 76, y + 28, title, F20B, anchor="la")
    text_xy(x + 76, y + 53, filename, F14, fill=GREY_TEXT, anchor="la")
    for idx, detail in enumerate(detail_lines):
        text_xy(x + 22, y + 91 + idx * 25, detail, F17 if idx == 0 else F15, fill=NAVY if idx == 0 else GREY_TEXT, anchor="la")


# Header
text_xy(W / 2, 72, "LLM PRETRAINING: FROM RAW TEXT TO A BASE MODEL", F32DISPLAY, anchor="ma")
text_xy(W / 2, 112, "Learning to predict the next token across massive amounts of text", F18, fill=GREY_TEXT, anchor="ma")

# Left: corpus
#text_xy(300, 176, "1  TRAINING DATA", F20B, fill=PURPLE, anchor="ma")
rounded_rect((42, 196, 558, 724), 18, PURPLE_PALE, PURPLE_MID, 1)
text_xy(300, 232, "ENORMOUS TEXT CORPUS", F25B, anchor="ma")
text_xy(300, 265, "Diverse sources converted into training tokens", F16, fill=GREY_TEXT, anchor="ma")

tiles = [
    (72, 291, "Books", BLUE_LIGHT, books_icon),
    (310, 291, "Websites", TEAL_LIGHT, website_icon),
    (72, 414, "Scientific\nPapers", PURPLE_LIGHT, paper_icon),
    (310, 414, "Code", GREEN_LIGHT, code_icon),
    (72, 537, "News \nArticles", GOLD_LIGHT, news_icon),
    (310, 537, "Reference\nWorks", BLUE_LIGHT, encyclopedia_icon),
]
for tx, ty, label, fill, icon_func in tiles:
    corpus_tile(tx, ty, 216, 100, label, fill)
    icon_func(tx + 13, ty + 28)

rounded_rect((141, 662, 459, 700), 19, PURPLE_LIGHT, PURPLE_MID, 1)
text_xy(300, 681, "MASSIVE SEQUENCE OF TOKENS", F15, fill=PURPLE, anchor="mm")

# First transfer arrow
text_xy(631, 344, "TOKENISE,\nSHUFFLE &\nSTREAM\nBATCHES", F14, fill=GREY_TEXT, anchor="ma")
arrow(576, 435, 687, 435)

# Middle: compute 
rounded_rect((704, 196, 1226, 724), 18, PURPLE_LIGHT, PURPLE_MID, 1)
text_xy(965, 232, "SUPERCOMPUTER", F25B, anchor="ma")
rounded_rect((805, 265, 1125, 310), 20, GREEN_LIGHT, GREEN, 1)
text_xy(965, 290, "~6,000 HIGH-PERFORMANCE GPUs", F16, fill=GREEN, anchor="mm")

for rack_x in (739, 830, 921, 1012, 1103):
    gpu_rack(rack_x, 320)

# chip_badge(853, 429, 224, 78)

rounded_rect((777, 630, 1153, 700), 12, BG, LINE, 1)
centered_lines(
    965,
    641,
    ["Next-token predictions", "+ gradient-based parameter updates"],
    font(20), fill=PURPLE,
    spacing=27,
)

# Second transfer arrow
text_xy(1302, 344, "TRAINING\nWRITES\nLEARNED\nSTATE", F14, fill=GREY_TEXT, anchor="ma")
arrow(1243, 435, 1362, 435)

# Right: files
#text_xy(1580, 176, "3  TRAINING OUTPUTS", F20B, fill=PURPLE, anchor="ma")

file_card(
    1380,
    196,
    390,
    245,
    "PARAMETERS",
    "checkpoint weights (often sharded)",
    [
        ">100 billion learned parameters",
        "≈200+ GB at FP16/BF16",
        "≈50–100 GB when quantised to 4–8 bit",
        "Weights and biases encoding learned patterns",
    ],
    PURPLE,
    "parameters",
)

file_card(
    1380,
    460,
    390,
    245,
    "MODEL CONFIG",
    "model_config.json",
    [
        "Architecture and hyperparameters",
        "Layers · width · attention · context length",
        "Typically ≈1–10 kB",
        "Usually tens of JSON lines—not code",
    ],
    NAVY,
    "config",
)

image.save(
    "/Users/cbottrell/Documents/Codex/2026-07-19/mak/outputs/llm-pretraining-schematic-4x.png",
    optimize=True,
    compress_level=6,
    dpi=(300, 300),
)

image = image.resize((W, H), Image.Resampling.LANCZOS)
image.save(
    "/Users/cbottrell/Documents/Codex/2026-07-19/mak/outputs/llm-pretraining-schematic.png",
    optimize=True,
    compress_level=6,
)
