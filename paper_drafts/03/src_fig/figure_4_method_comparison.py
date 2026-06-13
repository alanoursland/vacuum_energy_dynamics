from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).resolve().parents[1] / "md" / "figure_4_method_comparison.png"
W, H = 1600, 900


def font(size, bold=False):
    name = "arialbd.ttf" if bold else "arial.ttf"
    try:
        return ImageFont.truetype(name, size)
    except OSError:
        return ImageFont.load_default()


def wrap(draw, text, width, fnt):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        test = f"{cur} {word}".strip()
        if draw.textbbox((0, 0), test, font=fnt)[2] <= width:
            cur = test
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


img = Image.new("RGB", (W, H), "#f8fafc")
d = ImageDraw.Draw(img)
title = font(42, True)
head = font(28, True)
body = font(21)
small = font(18)

d.text((70, 48), "Pixel digitization and vector extraction fail differently", font=title, fill="#172033")
d.text((72, 108), "The paper's claim is conditional: vector extraction is strong only when path identity and anchors validate.", font=body, fill="#536173")

cards = [
    ("Pixel digitization", "#dbeafe", "#1d4ed8", [
        "Starts from rendered pixels.",
        "Errors come from resolution, antialiasing, line width, and manual clicks.",
        "Works even when the PDF contains only an image.",
    ]),
    ("Vector extraction", "#dcfce7", "#047857", [
        "Starts from PDF drawing paths.",
        "Errors come from path selection, clipping, and post-processing.",
        "Can recover plotted geometry at author-coordinate precision.",
    ]),
    ("Validation gate", "#fee2e2", "#b91c1c", [
        "Uses an external text-stated anchor.",
        "Catches wrong paths and wrong coordinate transforms.",
        "Refuses output when the anchor misses tolerance.",
    ]),
]

for i, (name, fill, accent, lines) in enumerate(cards):
    x0 = 80 + i * 505
    y0 = 205
    x1 = x0 + 435
    y1 = 705
    d.rounded_rectangle((x0, y0, x1, y1), radius=8, fill="#ffffff", outline="#cbd5e1", width=2)
    d.rectangle((x0, y0, x1, y0 + 86), fill=fill)
    d.text((x0 + 28, y0 + 26), name, font=head, fill=accent)
    yy = y0 + 125
    for item in lines:
        d.ellipse((x0 + 30, yy + 9, x0 + 42, yy + 21), fill=accent)
        for line in wrap(d, item, 340, body):
            d.text((x0 + 58, yy), line, font=body, fill="#334155")
            yy += 29
        yy += 28

d.line((520, 455, 585, 455), fill="#64748b", width=4)
d.polygon([(585, 455), (563, 442), (563, 468)], fill="#64748b")
d.line((1025, 455, 1090, 455), fill="#64748b", width=4)
d.polygon([(1090, 455), (1068, 442), (1068, 468)], fill="#64748b")

footer = (140, 760, 1460, 830)
d.rounded_rectangle(footer, radius=8, fill="#eef2ff", outline="#a5b4fc", width=2)
d.text((180, 782), "Recommended norm:", font=head, fill="#312e81")
d.text((500, 789), "emit provenance-graded data only after path extraction, calibration, and anchor validation all pass.", font=body, fill="#312e81")
d.text((75, 850), "Figure is schematic; quantitative pixel-comparison results should be added after the rasterization study.", font=small, fill="#64748b")

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT)
print(OUT)
