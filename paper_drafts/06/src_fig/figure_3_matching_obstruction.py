from pathlib import Path
import math

from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).resolve().parents[1] / "md" / "figure_3_matching_obstruction.png"
W, H = 1600, 980


def font(size, bold=False):
    name = "arialbd.ttf" if bold else "arial.ttf"
    try:
        return ImageFont.truetype(name, size)
    except OSError:
        return ImageFont.load_default()


img = Image.new("RGB", (W, H), "#f8fafc")
d = ImageDraw.Draw(img)
title = font(42, True)
head = font(25, True)
body = font(20)
small = font(17)

d.text((70, 48), "Hairless matching reduces to an impossible root condition", font=title, fill="#172033")
d.text((72, 108), "The witness equation x cosh x = sinh x has no positive solution.", font=body, fill="#536173")

plot = (145, 210, 990, 780)
left, top, right, bottom = plot
d.rectangle(plot, fill="#ffffff", outline="#334155", width=3)

xmax, ymax = 4.0, 18.0

def xp(x):
    return left + x / xmax * (right - left)

def yp(y):
    return bottom - y / ymax * (bottom - top)

for i in range(5):
    px = xp(i)
    d.line((px, top, px, bottom), fill="#e2e8f0", width=1)
    d.text((px - 6, bottom + 18), str(i), font=small, fill="#334155")
for j in range(7):
    y = j * 3
    py = yp(y)
    d.line((left, py, right, py), fill="#e2e8f0", width=1)
    d.text((left - 34, py - 9), str(y), font=small, fill="#334155")

points = []
for i in range(350):
    x = xmax * i / 349
    h = x * math.cosh(x) - math.sinh(x)
    points.append((xp(x), yp(min(h, ymax))))
d.line(points, fill="#7c3aed", width=5)
d.line((left, yp(0), right, yp(0)), fill="#475569", width=2)
d.text((390, 820), "x", font=head, fill="#172033")
d.text((50, 465), "h(x)", font=head, fill="#172033")

panel = (1080, 250, 1490, 705)
d.rounded_rectangle(panel, radius=8, fill="#ffffff", outline="#94a3b8", width=2)
d.text((1115, 285), "Proof", font=head, fill="#172033")
lines = [
    "h(x) = x cosh x - sinh x",
    "h(0) = 0",
    "h'(x) = x sinh x",
    "h'(x) > 0 for x > 0",
    "therefore h(x) > 0 for x > 0",
    "so hairless matching fails",
]
yy = 340
for line in lines:
    d.text((1115, yy), line, font=body, fill="#334155")
    yy += 55

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT)
print(OUT)
