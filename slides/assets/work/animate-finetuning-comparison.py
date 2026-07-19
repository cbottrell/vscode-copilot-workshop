from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


WIDTH, HEIGHT = 1920, 900
OUT_DIR = Path("/Users/cbottrell/Documents/Codex/2026-07-19/mak/outputs")
GIF_OUT = OUT_DIR / "fine-tuning-base-vs-assistant.gif"
PNG_OUT = OUT_DIR / "fine-tuning-base-vs-assistant.png"

WHITE = "#ffffff"
NAVY = "#253746"
GREEN = "#28724f"
LIME = "#d0df00"
BLUE_GREY = "#7a99ac"
PALE = "#f0f4f6"
PALEST = "#f7f9fa"
PALE_GREEN = "#e7f0eb"
GREY = "#abb8c3"
GREY_TEXT = "#6f7884"
LINE = "#ccd5df"
WARM = "#b85c3c"
PALE_WARM = "#f8ece6"

REGULAR = "/System/Library/Fonts/Supplemental/Arial.ttf"
BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
TITLE = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"


def font(size, bold=False, title=False):
    face = TITLE if title else (BOLD if bold else REGULAR)
    return ImageFont.truetype(face, size)


F_TITLE = font(48, title=True)
F_SUBTITLE = font(23)
F_PANEL = font(39, bold=True)
F_CHIP = font(16, bold=True)
F_DESC = font(19)
F_LABEL = font(28, bold=True)
F_PROMPT = font(30)
F_RESPONSE = font(28)
F_STATUS = font(19, bold=True)
F_STATUS_DETAIL = font(17)

PROMPT = "Briefly explain what quantum tunnelling is."

BASE_RESPONSE = (
    "Quantum tunnelling happens when a particle briefly borrows energy from the vacuum, "
    "allowing it to punch through a solid barrier before paying the energy back on the other side. "
    "This temporary energy loan is what makes tunnelling possible."
)

ASSISTANT_RESPONSE = (
    "Quantum tunnelling is a quantum effect where a particle can sometimes be found beyond a barrier "
    "it could not cross classically. Its wave-like state extends through the barrier, giving it a small "
    "probability of appearing on the other side."
)

LEFT = (50, 155, 942, 860)
RIGHT = (978, 155, 1870, 860)


def rounded_panel(draw, box, outline, accent):
    draw.rounded_rectangle(box, radius=32, fill=WHITE, outline=outline, width=3)
    x1, y1, x2, _ = box
    draw.rounded_rectangle((x1, y1, x2, y1 + 14), radius=7, fill=accent)


def wrap_words(draw, text, text_font, max_width):
    lines = []
    current = []
    for word in text.split():
        candidate = " ".join(current + [word])
        if current and draw.textlength(candidate, font=text_font) > max_width:
            lines.append(current)
            current = [word]
        else:
            current.append(word)
    if current:
        lines.append(current)
    return lines


def draw_partial_text(draw, lines, visible_words, x, y, text_font, fill, line_height=42, caret=False):
    remaining = visible_words
    cursor_x, cursor_y = x, y
    for line_index, words in enumerate(lines):
        shown = words[: max(0, min(len(words), remaining))]
        if shown:
            value = " ".join(shown)
            line_y = y + line_index * line_height
            draw.text((x, line_y), value, font=text_font, fill=fill, anchor="la")
            cursor_x = x + draw.textlength(value, font=text_font) + 5
            cursor_y = line_y
        remaining -= len(words)
        if remaining <= 0:
            break
    if caret and visible_words > 0:
        draw.line((cursor_x, cursor_y + 4, cursor_x, cursor_y + 34), fill=GREEN, width=3)


def draw_chip(draw, x, y, label, fill, text_colour, outline=None):
    chip_width = int(draw.textlength(label, font=F_CHIP)) + 34
    draw.rounded_rectangle((x, y, x + chip_width, y + 34), radius=17, fill=fill, outline=outline, width=2)
    draw.text((x + chip_width / 2, y + 17), label, font=F_CHIP, fill=text_colour, anchor="mm")


def draw_status(draw, box, positive):
    x1, y1, x2, y2 = box
    colour = GREEN if positive else WARM
    fill = PALE_GREEN if positive else PALE_WARM
    draw.rounded_rectangle(box, radius=18, fill=fill, outline=colour, width=2)
    icon_x = x1 + 35
    icon_y = (y1 + y2) / 2
    draw.ellipse((icon_x - 14, icon_y - 14, icon_x + 14, icon_y + 14), outline=colour, width=3)
    if positive:
        draw.line((icon_x - 7, icon_y, icon_x - 1, icon_y + 7, icon_x + 9, icon_y - 8), fill=colour, width=3)
        heading = "HELPFUL ANSWER"
        detail = "Simple, accurate and instruction-following"
    else:
        draw.line((icon_x - 7, icon_y - 7, icon_x + 7, icon_y + 7), fill=colour, width=3)
        draw.line((icon_x + 7, icon_y - 7, icon_x - 7, icon_y + 7), fill=colour, width=3)
        heading = "HALLUCINATION"
        detail = "Plausible wording, incorrect mechanism"
    draw.text((x1 + 65, y1 + 19), heading, font=F_STATUS, fill=colour, anchor="la")
    draw.text((x1 + 65, y1 + 48), detail, font=F_STATUS_DETAIL, fill=NAVY, anchor="la")


def draw_loading_dots(draw, x, y, phase, colour):
    for index in range(3):
        cx = x + index * 42
        active = index == phase % 3
        draw.ellipse(
            (cx - 12, y - 12, cx + 12, y + 12),
            fill=colour if active else WHITE,
            outline=colour,
            width=3,
        )


def base_canvas():
    image = Image.new("RGB", (WIDTH, HEIGHT), WHITE)
    draw = ImageDraw.Draw(image)
    draw.text((WIDTH / 2, 47), "FINE-TUNING CHANGES MODEL BEHAVIOUR", font=F_TITLE, fill=NAVY, anchor="ma")
    draw.text(
        (WIDTH / 2, 108),
        "The same prompt reveals the effect of human-written question-and-answer training",
        font=F_SUBTITLE,
        fill=GREY_TEXT,
        anchor="ma",
    )

    rounded_panel(draw, LEFT, BLUE_GREY, NAVY)
    rounded_panel(draw, RIGHT, GREEN, LIME)

    draw.text((90, 194), "BASE LLM", font=F_PANEL, fill=NAVY, anchor="la")
    draw_chip(draw, 90, 247, "PRETRAINED ONLY", PALE, NAVY, BLUE_GREY)
    draw.text(
        (90, 296),
        "Learns text patterns, but is not yet trained to act as a helpful assistant",
        font=F_DESC,
        fill=GREY_TEXT,
        anchor="la",
    )

    draw.text((1018, 194), "ASSISTANT LLM", font=F_PANEL, fill=GREEN, anchor="la")
    draw_chip(draw, 1018, 247, "Q&A FINE-TUNED", PALE_GREEN, GREEN, GREEN)
    draw.text(
        (1018, 296),
        "Fine-tuned on human-written prompts and high-quality helpful answers",
        font=F_DESC,
        fill=GREY_TEXT,
        anchor="la",
    )

    for panel_x in (90, 1018):
        draw.text((panel_x, 355), "Prompt:", font=F_LABEL, fill=NAVY, anchor="la")
        draw.text((panel_x, 402), PROMPT, font=F_PROMPT, fill=NAVY, anchor="la")
        draw.line((panel_x, 459, panel_x + 812, 459), fill=LINE, width=2)
        draw.text((panel_x, 498), "Response:", font=F_LABEL, fill=NAVY, anchor="la")
    return image


probe = Image.new("RGB", (WIDTH, HEIGHT), WHITE)
probe_draw = ImageDraw.Draw(probe)
left_lines = wrap_words(probe_draw, BASE_RESPONSE, F_RESPONSE, 804)
right_lines = wrap_words(probe_draw, ASSISTANT_RESPONSE, F_RESPONSE, 804)
left_word_count = sum(len(line) for line in left_lines)
right_word_count = sum(len(line) for line in right_lines)
typing_steps = max(left_word_count, right_word_count)

frames = []
durations = []

# Brief thinking phase, echoing the three-dot animation in the supplied reference.
for phase in range(9):
    frame = base_canvas()
    draw = ImageDraw.Draw(frame)
    draw_loading_dots(draw, 108, 572, phase, BLUE_GREY)
    draw_loading_dots(draw, 1036, 572, phase, GREEN)
    frames.append(frame)
    durations.append(120)

# Reveal both responses word by word so the contrast develops in parallel.
for step in range(1, typing_steps + 1):
    frame = base_canvas()
    draw = ImageDraw.Draw(frame)
    draw_partial_text(
        draw,
        left_lines,
        min(step, left_word_count),
        90,
        556,
        F_RESPONSE,
        NAVY,
        caret=step < left_word_count,
    )
    draw_partial_text(
        draw,
        right_lines,
        min(step, right_word_count),
        1018,
        556,
        F_RESPONSE,
        NAVY,
        caret=step < right_word_count,
    )
    frames.append(frame)
    durations.append(115)

# Hold the finished comparison long enough to discuss it on the slide.
final_frame = base_canvas()
final_draw = ImageDraw.Draw(final_frame)
draw_partial_text(final_draw, left_lines, left_word_count, 90, 556, F_RESPONSE, NAVY)
draw_partial_text(final_draw, right_lines, right_word_count, 1018, 556, F_RESPONSE, NAVY)
draw_status(final_draw, (90, 746, 902, 828), positive=False)
draw_status(final_draw, (1018, 746, 1830, 828), positive=True)
PNG_OUT.parent.mkdir(parents=True, exist_ok=True)
final_frame.save(PNG_OUT)
frames.append(final_frame)
durations.append(2600)

palette = final_frame.convert("P", palette=Image.Palette.ADAPTIVE, colors=192)
gif_frames = [frame.quantize(palette=palette, dither=Image.Dither.NONE) for frame in frames]
gif_frames[0].save(
    GIF_OUT,
    save_all=True,
    append_images=gif_frames[1:],
    duration=durations,
    loop=0,
    disposal=2,
    optimize=True,
)

print(f"Created {GIF_OUT} with {len(frames)} source frames")
print(f"Created {PNG_OUT}")
