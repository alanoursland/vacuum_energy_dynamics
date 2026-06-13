from pathlib import Path
import math

from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).resolve().parents[1] / "md" / "figure_2_scalaron_hair_profile.png"
W, H = 1600, 1000


def font(size, bold=False):
    name = "arialbd.ttf" if bold else "arial.ttf"
    try:
        return ImageFont.truetype(name, size)
    except OSError:
        return ImageFont.load_default()


img = Image.new("RGB", (W, H), "#fbfaf7")
d = ImageDraw.Draw(img)
title = font(42, True)
head = font(25, True)
body = font(20)
small = font(17)

d.text((70, 48), "Exterior scalaron hair creates an AB != 1 layer", font=title, fill="#172033")
d.text((72, 108), "Schematic profile: the scalar curvature tail decays over ell = sqrt(6a).", font=body, fill="#536173")

plot = (155, 210, 1450, 780)
left, top, right, bottom = plot
d.rectangle(plot, fill="#ffffff", outline="#334155", width=3)

R_surface = 0.9
ell = 1.0
xmax = 5.0

def xp(x):
    return left + (x / xmax) * (right - left)

def yp(y):
    return bottom - y * (bottom - top) / 1.15

for i in range(6):
    x = i
    px = xp(x)
    d.line((px, top, px, bottom), fill="#e2e8f0", width=1)
    d.text((px - 8, bottom + 18), str(i), font=small, fill="#334155")
for j in range(6):
    y = j / 5
    py = yp(y)
    d.line((left, py, right, py), fill="#e2e8f0", width=1)

d.rectangle((left, top, xp(R_surface), bottom), fill="#e7f0ff")
d.text((left + 70, top + 35), "source", font=head, fill="#1d4ed8")
d.line((xp(R_surface), top, xp(R_surface), bottom), fill="#1d4ed8", width=3)
d.text((xp(R_surface) - 18, bottom + 48), "R_b", font=small, fill="#1d4ed8")

points = []
ab_points = []
for i in range(350):
    x = R_surface + (xmax - R_surface) * i / 349
    R = math.exp(-(x - R_surface) / ell) * R_surface / x
    ab = 0.55 * math.exp(-(x - R_surface) / ell) * (1 + 0.4 / x)
    points.append((xp(x), yp(R)))
    ab_points.append((xp(x), yp(ab)))

d.line(points, fill="#047857", width=5)
d.line(ab_points, fill="#dc2626", width=4)
d.text((xp(1.25), yp(0.92)), "R_ext ~ C exp(-r/ell)/r", font=body, fill="#047857")
d.text((xp(1.7), yp(0.42)), "AB - 1 != 0 in hair region", font=body, fill="#dc2626")

for n in [1, 2, 3]:
    x = R_surface + n * ell
    d.line((xp(x), top, xp(x), bottom), fill="#94a3b8", width=1)
    d.text((xp(x) - 22, top + 10), f"{n} ell", font=small, fill="#64748b")

d.text((690, 850), "radius from source center", font=head, fill="#172033")
d.text((35, 470), "profile", font=head, fill="#172033")

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT)
print(OUT)
