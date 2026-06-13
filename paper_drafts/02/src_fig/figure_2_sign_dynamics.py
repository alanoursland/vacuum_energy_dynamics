from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "md" / "figure_2_sign_dynamics.png"


def load_fonts():
    try:
        return (
            ImageFont.truetype("arial.ttf", 30),
            ImageFont.truetype("arial.ttf", 22),
        )
    except OSError:
        f = ImageFont.load_default()
        return f, f


def rounded(draw, xy, fill, outline, width=2, radius=14):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


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
    title_font, head_font = load_fonts()

    bg = (252, 252, 249)
    ink = (30, 36, 42)
    blue = (44, 92, 150)
    green = (52, 125, 82)
    red = (172, 67, 67)
    gold = (170, 124, 38)
    gray = (108, 116, 125)
    lightblue = (226, 237, 249)
    lightgreen = (227, 242, 232)
    lightred = (249, 229, 226)
    lightgold = (248, 240, 220)

    image = Image.new("RGB", (1200, 820), bg)
    draw = ImageDraw.Draw(image)
    draw.text((48, 34), "Figure 2. Sign Is Not Enough: Sign Plus Dynamics Matters", font=title_font, fill=ink)

    x0, y0, x1, y1 = 130, 140, 1130, 760
    draw.rectangle((x0, y0, x1, y1), outline=gray, width=3)
    draw.line((x0, 450, x1, 450), fill=gray, width=3)
    draw.line((630, y0, 630, y1), fill=gray, width=3)

    draw.text((330, 100), "Negative energy", font=head_font, fill=red)
    draw.text((805, 100), "Positive energy", font=head_font, fill=green)
    draw.text((20, 270), "Propagating", font=head_font, fill=ink)
    draw.text((35, 585), "Constraint", font=head_font, fill=ink)

    cells = [
        ((160, 180, 600, 420), "FORBIDDEN GHOST\nH unbounded below\nvacuum decay", lightred, red),
        ((660, 180, 1100, 420), "GRAVITATIONAL WAVES\nTT modes\npositive flux", lightgreen, green),
        ((160, 490, 600, 730), "STATIC GRAVITY\nnegative but elliptic\nsource-slaved", lightgold, gold),
        ((660, 490, 1100, 730), "NONDANGEROUS\nnot central here\nbounded constraint", lightblue, blue),
    ]

    for box, text, fill, outline in cells:
        rounded(draw, box, fill, outline)
        center_text(draw, box, text, head_font, ink)

    image.save(OUT)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
