from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "md" / "figure_3_radiative_bootstrap.png"


def load_fonts():
    try:
        return (
            ImageFont.truetype("arial.ttf", 30),
            ImageFont.truetype("arial.ttf", 22),
            ImageFont.truetype("arial.ttf", 18),
        )
    except OSError:
        f = ImageFont.load_default()
        return f, f, f


def rounded(draw, xy, fill, outline, width=2, radius=18):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def arrow(draw, start, end, color, width=3):
    draw.line([start, end], fill=color, width=width)
    x1, y1 = start
    x2, y2 = end
    angle = math.atan2(y2 - y1, x2 - x1)
    size = 12
    points = [
        (x2, y2),
        (x2 - size * math.cos(angle - math.pi / 6), y2 - size * math.sin(angle - math.pi / 6)),
        (x2 - size * math.cos(angle + math.pi / 6), y2 - size * math.sin(angle + math.pi / 6)),
    ]
    draw.polygon(points, fill=color)


def center_text(draw, box, text, font, fill, spacing=5):
    lines = text.split("\n")
    boxes = [draw.textbbox((0, 0), line, font=font) for line in lines]
    widths = [b[2] - b[0] for b in boxes]
    heights = [b[3] - b[1] for b in boxes]
    total_height = sum(heights) + spacing * (len(lines) - 1)
    x0, y0, x1, y1 = box
    y = y0 + (y1 - y0 - total_height) / 2
    for line, width, height in zip(lines, widths, heights):
        draw.text((x0 + (x1 - x0 - width) / 2, y), line, font=font, fill=fill)
        y += height + spacing


def main():
    title_font, head_font, body_font = load_fonts()

    bg = (252, 252, 249)
    ink = (30, 36, 42)
    blue = (44, 92, 150)
    green = (52, 125, 82)
    red = (172, 67, 67)
    gold = (170, 124, 38)
    lightblue = (226, 237, 249)
    lightgreen = (227, 242, 232)
    lightred = (249, 229, 226)
    lightgold = (248, 240, 220)

    image = Image.new("RGB", (1400, 820), bg)
    draw = ImageDraw.Draw(image)
    draw.text((48, 34), "Figure 3. Radiative Normalization Bootstrap", font=title_font, fill=ink)

    steps = [
        (90, 180, 350, 310, "Linear wave\nK_T Box h = J", lightblue, blue),
        (440, 180, 700, 310, "Amplitude\nh ~ J / K_T", lightblue, blue),
        (790, 180, 1050, 310, "Flux and work\nscale as J^2 / K_T", lightgold, gold),
        (965, 500, 1250, 630, "Linear balance\ndoes not fix K_T", lightred, red),
        (565, 500, 845, 630, "Self-coupling\nof wave energy", lightgreen, green),
        (165, 500, 445, 630, "K_T = c^4 / 16 pi G\nquadrupole fixed", lightgreen, green),
    ]

    for x0, y0, x1, y1, text, fill, outline in steps:
        rounded(draw, (x0, y0, x1, y1), fill, outline)
        center_text(draw, (x0, y0, x1, y1), text, head_font, ink)

    arrow(draw, (350, 245), (440, 245), blue)
    arrow(draw, (700, 245), (790, 245), blue)
    arrow(draw, (980, 310), (1090, 500), gold)
    arrow(draw, (965, 565), (845, 565), green)
    arrow(draw, (565, 565), (445, 565), green)

    draw.text(
        (330, 705),
        "Linear work-flux balance cannot choose the coefficient; second-order self-coupling fixes it.",
        font=body_font,
        fill=ink,
    )

    image.save(OUT)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
