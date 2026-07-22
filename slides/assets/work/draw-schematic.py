from PIL import Image, ImageDraw, ImageFont


SCALE = 2
W, H = 1600, 900


def s(value):
    return int(round(value * SCALE))


def box(coords):
    return tuple(s(v) for v in coords)


BG = "#ffffff"
NAVY = "#253746"
PURPLE = "#28724f"
PURPLE_MID = "#7a99ac"
PURPLE_LIGHT = "#f0f4f6"
GREEN = "#28724f"
LIME = "#d0df00"
GREY = "#abb8c3"
GREY_TEXT = "#808491"
LINE = "#ccd5df"

image = Image.new("RGB", (s(W), s(H)), BG)
draw = ImageDraw.Draw(image)

REGULAR = "/System/Library/Fonts/Supplemental/Arial.ttf"
BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"


def font(size, bold=False):
    return ImageFont.truetype(BOLD if bold else REGULAR, s(size))


F12 = font(12)
F14 = font(14)
F15 = font(15)
F16 = font(16)
F17 = font(17)
F18 = font(18)
F18B = font(18, True)
F20B = font(20, True)
F22B = font(22, True)
F31B = font(31, True)


def text_xy(x, y, text, face, fill=NAVY, anchor="la"):
    draw.text((s(x), s(y)), text, font=face, fill=fill, anchor=anchor)


def centered_lines(x, y, lines, face, spacing=28, fill=NAVY):
    for index, line in enumerate(lines):
        text_xy(x, y + index * spacing, line, face, fill=fill, anchor="ma")


def rounded_rect(coords, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box(coords), radius=s(radius), fill=fill, outline=outline, width=s(width))


def line(coords, fill, width=1, joint="curve"):
    draw.line(box(coords), fill=fill, width=s(width), joint=joint)


def arrow(x1, y1, x2, y2, color=PURPLE, width=4, head=13):
    line((x1, y1, x2 - head * 0.65, y2), color, width)
    draw.polygon(
        [
            (s(x2), s(y2)),
            (s(x2 - head), s(y2 - head * 0.72)),
            (s(x2 - head), s(y2 + head * 0.72)),
        ],
        fill=color,
    )


def down_arrow(x, y1, y2):
    line((x, y1, x, y2 - 6), PURPLE, 1)
    draw.polygon(
        [(s(x), s(y2)), (s(x - 4), s(y2 - 7)), (s(x + 4), s(y2 - 7))],
        fill=PURPLE,
    )


text_xy(346, 329, "INPUT PROMPT (CONTEXT SO FAR)", F18B, anchor="ma")

tokens = ["I", "saw", "James", "in", "the", "Forrest", "Hall", "kitchen", "eating", "a", "whole"]
x = 28
centers = []
for index, token in enumerate(tokens, start=1):
    measured = draw.textbbox((0, 0), token, font=F17)
    token_width = max(s(30), measured[2] - measured[0] + s(18)) / SCALE
    rounded_rect((x, 370, x + token_width, 434), 7, PURPLE_LIGHT, PURPLE_MID, 1)
    cx = x + token_width / 2
    centers.append(cx)
    text_xy(cx, 402, token, F17, anchor="mm")
    down_arrow(cx, 435, 476)
    text_xy(cx, 511, str(index), F16, fill=PURPLE, anchor="mm")
    x += token_width + 7

text_xy(6, 494, "Token", F12, fill=PURPLE, anchor="la")
text_xy(6, 513, "position", F12, fill=PURPLE, anchor="la")

left_x = 28
right_x = x - 7
mid_x = (left_x + right_x) / 2
line((left_x, 558, left_x, 567), PURPLE, 1)
line((left_x, 567, left_x + 9, 575), PURPLE, 1)
line((left_x + 9, 575, mid_x - 12, 575), PURPLE, 1)
line((mid_x - 12, 575, mid_x, 587), PURPLE, 1)
line((mid_x, 587, mid_x + 12, 575), PURPLE, 1)
line((mid_x + 12, 575, right_x - 9, 575), PURPLE, 1)
line((right_x - 9, 575, right_x, 567), PURPLE, 1)
line((right_x, 567, right_x, 558), PURPLE, 1)

centered_lines(
    mid_x,
    622,
    [
        "Each word (token) is fed to the model in order",
        "and forms the context for the next prediction.",
    ],
    F18,
    spacing=30,
    fill=PURPLE,
)

arrow(693, 402, 726, 402, width=5, head=15)

text_xy(885, 182, "LLM", F31B, fill=PURPLE, anchor="ma")
rounded_rect((738, 215, 1043, 725), 18, PURPLE_LIGHT, PURPLE_MID, 1)

layers = [
    [(785, 310), (785, 375), (785, 440), (785, 505)],
    [(860, 285), (860, 375), (860, 440), (860, 530)],
    [(935, 285), (935, 375), (935, 440), (935, 530)],
    [(986, 340), (986, 415), (986, 490)],
]
for layer_index in range(len(layers) - 1):
    for x1, y1 in layers[layer_index]:
        for x2, y2 in layers[layer_index + 1]:
            line((x1, y1, x2, y2), PURPLE, 1)

for layer_index, layer_nodes in enumerate(layers):
    for cx, cy in layer_nodes:
        r = 13 if layer_index == 3 else 14
        fill = PURPLE_LIGHT if layer_index == 3 else PURPLE
        draw.ellipse(box((cx - r, cy - r, cx + r, cy + r)), fill=fill, outline=PURPLE, width=s(1))

for y in (338, 413, 488):
    text_xy(1004, y, "...", F20B, fill=PURPLE, anchor="lm")

centered_lines(
    890,
    592,
    [
        "The model uses patterns",
        "learned from vast amounts",
        "of text to predict the",
        "next token.",
    ],
    F18B,
    spacing=30,
)

arrow(1056, 402, 1089, 402, width=5, head=15)

text_xy(1310, 157, "PREDICTED NEXT TOKEN (OUTPUT)", F20B, anchor="ma")
text_xy(1111, 199, "Candidate next token", F15, anchor="la")
text_xy(1492, 199, "Likelihood", F15, anchor="ra")
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
for idx, ((candidate, likelihood, bar_width, bar_color, likelihood_color), top) in enumerate(zip(rows, row_tops)):
    cy = top + 31
    text_xy(1115, cy, candidate, F18B, anchor="lm")
    rounded_rect((1228, top + 15, 1228 + bar_width, top + 39), 4, bar_color)
    text_xy(1495, cy, likelihood, F18B, fill=likelihood_color, anchor="rm")
    if idx < len(rows) - 1:
        line((1112, top + 52, 1497, top + 52), LINE, 1)

for y in (390, 553):
    for x1 in range(1098, 1514, 16):
        line((x1, y, min(x1 + 8, 1514), y), GREY_TEXT, 1)

axis_y = 758
line((1121, axis_y, 1483, axis_y), NAVY, 1)
axis_ticks = [(1121, "0"), (1212, "0.25"), (1302, "0.50"), (1393, "0.75"), (1483, "1.00")]
for tx, label in axis_ticks:
    line((tx, axis_y, tx, axis_y + 13), NAVY, 1)
    text_xy(tx, 787, label, F14, anchor="mm")

text_xy(1080, 830, "Less likely", F16, fill=NAVY, anchor="lm")
arrow(1191, 830, 1395, 830, color=NAVY, width=1, head=8)
text_xy(1420, 830, "More likely", F16, fill=GREEN, anchor="lm")

image = image.resize((W, H), Image.Resampling.LANCZOS)
image.save("/Users/cbottrell/Documents/Codex/2026-07-19/mak/outputs/llm-next-token-schematic.png", quality=96)
