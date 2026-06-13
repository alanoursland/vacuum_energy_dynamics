from pathlib import Path
import math

from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).resolve().parents[1] / "md" / "figure_3_lee2020_case_study.png"
W, H = 1600, 1050


def font(size, bold=False):
    name = "arialbd.ttf" if bold else "arial.ttf"
    try:
        return ImageFont.truetype(name, size)
    except OSError:
        return ImageFont.load_default()


def log_interp(x, x0, x1, p0, p1):
    t = (math.log10(x) - math.log10(x0)) / (math.log10(x1) - math.log10(x0))
    return p0 + t * (p1 - p0)


img = Image.new("RGB", (W, H), "#f8fafc")
d = ImageDraw.Draw(img)
title = font(42, True)
label = font(25, True)
small = font(19)

d.text((70, 45), "Lee 2020 case study: anchor-validated curve readout", font=title, fill="#172033")
d.text((72, 104), "Schematic log-log rendering of the extracted vector path and two crossings used by the program.", font=small, fill="#526071")

plot = (160, 190, 1430, 870)
left, top, right, bottom = plot
d.rectangle(plot, fill="#ffffff", outline="#334155", width=3)

x_min, x_max = 1e-5, 1e-3
y_min, y_max = 1e-3, 1e3


def xp(lam):
    return log_interp(lam, x_min, x_max, left, right)


def yp(alpha):
    return log_interp(alpha, y_min, y_max, bottom, top)


for decade in [-5, -4, -3]:
    x = xp(10 ** decade)
    d.line((x, top, x, bottom), fill="#d9e0ea", width=2)
    d.line((x, bottom, x, bottom + 14), fill="#334155", width=3)
    d.text((x - 35, bottom + 25), f"1e{decade} m", font=small, fill="#334155")
    for k in range(2, 10):
        val = k * 10 ** decade
        if x_min <= val <= x_max:
            xm = xp(val)
            d.line((xm, bottom, xm, bottom + 8), fill="#64748b", width=1)

for decade in [-3, -2, -1, 0, 1, 2, 3]:
    y = yp(10 ** decade)
    d.line((left, y, right, y), fill="#d9e0ea", width=2)
    d.line((left - 14, y, left, y), fill="#334155", width=3)
    d.text((70, y - 12), f"1e{decade}", font=small, fill="#334155")

d.text((650, 940), "lambda", font=label, fill="#1f2937")
d.text((28, 490), "alpha", font=label, fill="#1f2937")

# Smooth illustrative curve constrained to pass through the two recorded crossings.
cross_a1 = 38.61e-6
cross_a13 = 54.05e-6
points = [
    (1.2e-5, 6.0e2),
    (1.8e-5, 8.0e1),
    (2.6e-5, 8.0),
    (cross_a1, 1.0),
    (cross_a13, 1.0 / 3.0),
    (8.5e-5, 7.0e-2),
    (1.5e-4, 2.0e-2),
    (3.0e-4, 8.0e-3),
]
path = [(xp(l), yp(a)) for l, a in points]
fill_poly = path + [(right, bottom), (path[0][0], bottom)]
d.polygon(fill_poly, fill="#bbf7d0")
d.line(path, fill="#047857", width=7, joint="curve")
for x, y in path:
    d.ellipse((x - 6, y - 6, x + 6, y + 6), fill="#064e3b")

for alpha, lam, color, txt in [
    (1.0, cross_a1, "#dc2626", "anchor: alpha = 1 at 38.61 um"),
    (1.0 / 3.0, cross_a13, "#2563eb", "readout: alpha = 1/3 at 54.05 um"),
]:
    x, y = xp(lam), yp(alpha)
    d.line((left, y, right, y), fill=color, width=2)
    d.line((x, top, x, bottom), fill=color, width=2)
    d.ellipse((x - 10, y - 10, x + 10, y + 10), fill=color)
    d.text((x + 18, y - 34), txt, font=small, fill=color)

note = (875, 220, 1395, 340)
d.rounded_rectangle(note, radius=8, fill="#fff7ed", outline="#fdba74", width=2)
d.text((900, 244), "Validation result", font=label, fill="#7c2d12")
d.text((900, 286), "38.61 um vs text anchor 38.6 um", font=small, fill="#7c2d12")
d.text((900, 315), "relative deviation: 0.03%", font=small, fill="#7c2d12")

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT)
print(OUT)
