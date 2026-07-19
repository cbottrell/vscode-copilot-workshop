from PIL import Image, ImageDraw, ImageFont
from math import cos, pi, sin


BASE = "/Users/cbottrell/Documents/Codex/2026-07-19/mak/outputs/llm-weight-training-schematic.png"
OUT = "/Users/cbottrell/Documents/Codex/2026-07-19/mak/outputs/llm-weight-training-schematic-animated.gif"

BG = "#ffffff"
NAVY = "#253746"
GREEN = "#28724f"
BLUE_GREY = "#7a99ac"
PALE = "#f0f4f6"
PALEST = "#f7f9fa"
PALE_LIME = "#f3f6d5"
LIME = "#d0df00"
GREY = "#abb8c3"
GREY_TEXT = "#808491"
LINE = "#ccd5df"

REGULAR = "/System/Library/Fonts/Supplemental/Arial.ttf"
BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"


def font(size, bold=False):
    return ImageFont.truetype(BOLD if bold else REGULAR, size)


F11B = font(11, True)
F12 = font(12)
F12B = font(12, True)
F13B = font(13, True)
F14 = font(14)
F14B = font(14, True)
F15B = font(15, True)
F16B = font(16, True)
F18B = font(18, True)


def ease(value):
    return value * value * (3 - 2 * value)


def lerp(start, end, amount):
    return start + (end - start) * amount


def draw_dial(draw, cx, cy, radius, needle_value, accent=GREEN, show_value=True, display_value=None):
    draw.ellipse((cx - radius, cy - radius, cx + radius, cy + radius), fill=BG, outline=NAVY, width=2)
    for degree in (225, 180, 135, 90, 45, 0, -45):
        angle = degree * pi / 180
        x1 = cx + radius * 0.72 * cos(angle)
        y1 = cy - radius * 0.72 * sin(angle)
        x2 = cx + radius * 0.90 * cos(angle)
        y2 = cy - radius * 0.90 * sin(angle)
        draw.line((x1, y1, x2, y2), fill=BLUE_GREY, width=1)
    needle_angle = (225 - (max(-1, min(1, needle_value)) + 1) * 135) * pi / 180
    needle_x = cx + radius * 0.68 * cos(needle_angle)
    needle_y = cy - radius * 0.68 * sin(needle_angle)
    draw.line((cx, cy, needle_x, needle_y), fill=accent, width=3)
    draw.ellipse((cx - 3, cy - 3, cx + 3, cy + 3), fill=accent)
    if show_value:
        label_value = needle_value if display_value is None else display_value
        draw.text((cx, cy + radius + 8), f"{label_value:+.2f}", font=F11B, fill=accent, anchor="ma")


def prediction_row(draw, y, label, probability, bar_colour):
    draw.text((958, y), label, font=F15B, fill=NAVY, anchor="lm")
    draw.rounded_rectangle((1023, y - 11, 1023 + 120 * probability, y + 11), radius=4, fill=bar_colour)
    draw.text((1153, y), f"{probability:.2f}", font=F15B, fill=GREEN, anchor="rm")


base = Image.open(BASE).convert("RGB")
initial_values = [0.42, -0.18, 0.07, 0.63, 0.03, -0.11]
final_values = [0.45, -0.16, 0.05, 0.62, 0.04, -0.10]
DIAL_MOTION_EXAGGERATION = 26
LOSS_BOX = (1350, 416, 1710, 482)

timeline = [0.0] * 6 + [ease(i / 17) for i in range(18)] + [1.0] * 12
frames = []

for progress in timeline:
    frame = base.copy()
    draw = ImageDraw.Draw(frame)

    values = [lerp(a, b, progress) for a, b in zip(initial_values, final_values)]
    needle_values = [
        max(-1, min(1, initial + (current - initial) * DIAL_MOTION_EXAGGERATION))
        for initial, current in zip(initial_values, values)
    ]
    pizza = lerp(0.31, 0.62, progress)
    cake = lerp(0.28, 0.19, progress)
    loaf = lerp(0.12, 0.09, progress)
    pie = lerp(0.08, 0.05, progress)
    loss = lerp(1.17, 0.48, progress)

    # Refresh the model prediction area.
    draw.rectangle((946, 296, 1160, 516), fill=PALE)
    draw.text((958, 310), "MODEL PREDICTION", font=F13B, fill=BLUE_GREY, anchor="la")
    prediction_row(draw, 352, "pizza", pizza, GREEN)
    prediction_row(draw, 397, "cake", cake, LIME)
    prediction_row(draw, 442, "loaf", loaf, GREY)
    prediction_row(draw, 487, "pie", pie, GREY)

    # Refresh the magnified parameter dial bank.
    draw.rounded_rectangle((690, 550, 1148, 683), radius=12, fill=BG, outline=LINE, width=1)
    draw.text((712, 566), "A tiny sample of parameter dials", font=F16B, fill=NAVY, anchor="la")
    draw.text((1126, 568), "motion enlarged for clarity", font=F12, fill=GREY_TEXT, anchor="ra")
    draw.text((838, 594), "weight matrix W", font=F12B, fill=BLUE_GREY, anchor="ma")
    draw.text((1090, 594), "bias b", font=F12B, fill=BLUE_GREY, anchor="ma")
    draw.line((1002, 595, 1002, 670), fill=LINE, width=1)
    for dial_x, needle_value, value in zip((735, 805, 875, 945), needle_values[:4], values[:4]):
        draw_dial(draw, dial_x, 635, 18, needle_value, GREEN, True, value)
    for dial_x, needle_value, value in zip((1060, 1120), needle_values[4:], values[4:]):
        draw_dial(draw, dial_x, 635, 18, needle_value, NAVY, True, value)

    # Rotate the three enlarged dials embedded in the network.
    for (dial_x, dial_y), needle_value in zip(((757, 347), (756, 432), (849, 466)), needle_values[:3]):
        draw_dial(draw, dial_x, dial_y, 15, needle_value, GREEN, False)

    # Update the loss card as the correct-token probability improves.
    draw.rounded_rectangle(LOSS_BOX, radius=12, fill=PALE_LIME, outline=GREEN, width=2)
    draw.text((1530, 449), f"CROSS-ENTROPY LOSS = {loss:.2f}", font=F18B, fill=NAVY, anchor="mm")

    frames.append(frame)

palette_frame = frames[0].convert("P", palette=Image.Palette.ADAPTIVE, colors=192)
gif_frames = [palette_frame]
for frame in frames[1:]:
    gif_frames.append(frame.quantize(palette=palette_frame, dither=Image.Dither.NONE))

gif_frames[0].save(
    OUT,
    save_all=True,
    append_images=gif_frames[1:],
    duration=90,
    loop=0,
    disposal=2,
    optimize=True,
)
