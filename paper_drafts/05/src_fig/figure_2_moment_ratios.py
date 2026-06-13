from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).resolve().parents[1] / "md" / "figure_2_moment_ratios.png"
W, H = 1800, 1050
BG = (248, 249, 246)
INK = (33, 39, 44)
GRID = (220, 224, 222)
MUTED = (92, 99, 105)
COLORS = [(34, 96, 148), (46, 125, 92), (178, 124, 39), (161, 65, 63)]


def font(size, bold=False):
    name = "arialbd.ttf" if bold else "arial.ttf"
    try:
        return ImageFont.truetype(name, size)
    except OSError:
        return ImageFont.load_default()


def ratio(R, k):
    return (2 * k - 1) / (2 * k + 2 * R + 3)


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)
title = font(54, True)
body = font(28)
small = font(22)

d.text((90, 70), "Adjacent beta-moment ratios", fill=INK, font=title)
d.text((90, 140), "r_(R,k) = B(k+1/2,R+2) / B(k-1/2,R+2)", fill=MUTED, font=body)

left, top, right, bottom = 180, 250, 1550, 850
d.rectangle((left, top, right, bottom), fill=(255, 255, 255), outline=(210, 214, 212), width=3)

for i in range(6):
    y = bottom - i * (bottom - top) / 5
    d.line((left, y, right, y), fill=GRID, width=2)
    val = i / 5
    d.text((105, y - 14), f"{val:.1f}", fill=MUTED, font=small)

for k in range(1, 11):
    x = left + (k - 1) * (right - left) / 9
    d.line((x, top, x, bottom), fill=(235, 237, 235), width=1)
    d.text((x - 9, bottom + 22), str(k), fill=MUTED, font=small)

d.text((845, 910), "k", fill=INK, font=body)
d.text((45, 535), "ratio", fill=INK, font=body)

for R, color in enumerate(COLORS):
    pts = []
    for k in range(1, 11):
        x = left + (k - 1) * (right - left) / 9
        y = bottom - ratio(R, k) * (bottom - top)
        pts.append((x, y))
    d.line(pts, fill=color, width=5)
    for x, y in pts:
        d.ellipse((x - 7, y - 7, x + 7, y + 7), fill=color)
    d.text((1585, 285 + R * 55), f"R = {R}", fill=color, font=body)

d.text((180, 960), "Higher endpoint contact lowers each finite-k survivor ratio.", fill=MUTED, font=small)

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT)
print(OUT)

