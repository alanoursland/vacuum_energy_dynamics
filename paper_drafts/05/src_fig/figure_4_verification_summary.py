from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).resolve().parents[1] / "md" / "figure_4_verification_summary.png"
W, H = 1800, 1050
BG = (248, 249, 246)
INK = (33, 39, 44)
MUTED = (92, 99, 105)
BLUE = (34, 96, 148)
GREEN = (46, 125, 92)
GOLD = (178, 124, 39)


def font(size, bold=False):
    name = "arialbd.ttf" if bold else "arial.ttf"
    try:
        return ImageFont.truetype(name, size)
    except OSError:
        return ImageFont.load_default()


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)
title = font(54, True)
label = font(34, True)
body = font(28)
small = font(23)

d.text((90, 70), "Verification role", fill=INK, font=title)
d.text((90, 140), "Symbolic checks support the proof; they do not replace it.", fill=MUTED, font=body)

items = [
    ("Scalar ladder", ["Beta ratio simplifies", "to r_(R,k)"], BLUE),
    ("Basis checks", ["Both families span", "the admissible space"], GREEN),
    ("Determinants", ["Exact nonzero values", "over tested R,N grid"], GOLD),
]

y = 285
for i, (head, lines, color) in enumerate(items):
    x = 140 + i * 535
    d.rounded_rectangle((x, y, x + 435, y + 310), radius=18, fill=(255, 255, 255), outline=color, width=5)
    d.ellipse((x + 40, y + 42, x + 100, y + 102), fill=color)
    d.text((x + 125, y + 48), head, fill=color, font=label)
    for j, line in enumerate(lines):
        d.text((x + 45, y + 135 + j * 40), line, fill=INK, font=body)
    d.text((x + 45, y + 220), "exact arithmetic", fill=MUTED, font=small)

d.rounded_rectangle((210, 745, 1590, 875), radius=16, fill=(255, 255, 255), outline=(212, 216, 214), width=3)
d.text((260, 775), "Load-bearing proof:", fill=INK, font=label)
d.text((630, 780), "positive pairing + two bases of one finite space", fill=MUTED, font=body)
d.text((260, 825), "Final release should package scripts with commands and expected outputs.", fill=MUTED, font=small)

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT)
print(OUT)
