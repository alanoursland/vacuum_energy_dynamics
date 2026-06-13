from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).resolve().parents[1] / "md" / "figure_1_regular_ladder.png"
W, H = 1800, 1050
BG = (248, 249, 246)
INK = (33, 39, 44)
MUTED = (93, 101, 107)
BLUE = (34, 96, 148)
GREEN = (46, 125, 92)
GOLD = (178, 124, 39)
RED = (161, 65, 63)


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
body = font(30)
small = font(24)

d.text((90, 70), "Endpoint-contact ladder", fill=INK, font=title)
d.text(
    (90, 140),
    "The primitive power m = R + 2 shifts the adjacent beta-moment ratio.",
    fill=MUTED,
    font=body,
)

levels = [
    ("R = 0", "m = 2", "r_(0,k) = (2k - 1)/(2k + 3)", BLUE),
    ("R = 1", "m = 3", "r_(1,k) = (2k - 1)/(2k + 5)", GREEN),
    ("R = 2", "m = 4", "r_(2,k) = (2k - 1)/(2k + 7)", GOLD),
    ("R = 3", "m = 5", "r_(3,k) = (2k - 1)/(2k + 9)", RED),
]

x0, x1 = 170, 1620
y0 = 290
gap = 160

for i, (r, m, formula, color) in enumerate(levels):
    y = y0 + i * gap
    d.rounded_rectangle((x0, y, x1, y + 96), radius=18, fill=(255, 255, 255), outline=(215, 219, 217), width=3)
    d.rectangle((x0, y, x0 + 22, y + 96), fill=color)
    d.text((x0 + 55, y + 23), r, fill=color, font=label)
    d.text((x0 + 270, y + 23), m, fill=INK, font=label)
    d.text((x0 + 560, y + 25), formula, fill=INK, font=body)
    if i < len(levels) - 1:
        cx = 890
        d.line((cx, y + 104, cx, y + gap - 12), fill=(150, 155, 155), width=4)
        d.polygon([(cx, y + gap - 12), (cx - 12, y + gap - 36), (cx + 12, y + gap - 36)], fill=(150, 155, 155))

d.text((170, 945), "R labels endpoint contact order, not ordinary differentiability.", fill=MUTED, font=small)

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT)
print(OUT)

