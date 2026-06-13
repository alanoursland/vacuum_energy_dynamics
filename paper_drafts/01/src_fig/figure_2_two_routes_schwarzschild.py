from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).resolve().parents[1] / "md" / "figure_2_two_routes_schwarzschild.png"
W, H = 1700, 1000


def font(size, bold=False):
    name = "arialbd.ttf" if bold else "arial.ttf"
    try:
        return ImageFont.truetype(name, size)
    except OSError:
        return ImageFont.load_default()


def center(draw, box, text, fnt, fill):
    bb = draw.textbbox((0, 0), text, font=fnt)
    x = (box[0] + box[2] - (bb[2] - bb[0])) / 2
    y = (box[1] + box[3] - (bb[3] - bb[1])) / 2
    draw.text((x, y), text, font=fnt, fill=fill)


img = Image.new("RGB", (W, H), "#fbfaf7")
d = ImageDraw.Draw(img)
title = font(43, True)
head = font(27, True)
body = font(21)
eq = font(24, True)

d.text((70, 48), "Two independent routes meet at the same exterior", font=title, fill="#172033")
d.text((72, 108), "The static metric is derived once by bookkeeping and once by field-theory closure.", font=body, fill="#536173")

left_col = [(110, 230, 640, 330), (110, 405, 640, 505), (110, 580, 640, 680)]
right_col = [(1060, 230, 1590, 330), (1060, 405, 1590, 505), (1060, 580, 1590, 680)]
fills = ["#dbeafe", "#dcfce7", "#fef3c7"]

left_text = [
    ("Areal-flux law", "Delta_areal A = (8 pi G / c^2) rho"),
    ("P7-prime shadow", "A B = 1"),
    ("P9 variable selection", "u_field = -c^4 (s')^2 / 8 pi G"),
]
right_text = [
    ("Metric perturbation", "g_ab = eta_ab + h_ab"),
    ("Gauge spin-2 closure", "N G_ab[g] = T_ab"),
    ("Static normalization", "N = c^4 / 8 pi G"),
]

for boxes, texts in [(left_col, left_text), (right_col, right_text)]:
    for i, (box, (h, b)) in enumerate(zip(boxes, texts)):
        d.rounded_rectangle(box, radius=8, fill=fills[i], outline="#94a3b8", width=2)
        d.text((box[0] + 25, box[1] + 18), h, font=head, fill="#172033")
        d.text((box[0] + 25, box[1] + 58), b, font=body, fill="#334155")

for boxes in [left_col, right_col]:
    for a, b in zip(boxes, boxes[1:]):
        x = (a[0] + a[2]) / 2
        d.line((x, a[3] + 12, x, b[1] - 12), fill="#64748b", width=4)
        d.polygon([(x, b[1] - 12), (x - 12, b[1] - 32), (x + 12, b[1] - 32)], fill="#64748b")

meet = (530, 775, 1170, 900)
d.rounded_rectangle(meet, radius=8, fill="#ffffff", outline="#0f766e", width=3)
center(d, (meet[0], meet[1] + 8, meet[2], meet[1] + 60), "Same exterior", head, "#065f46")
center(d, (meet[0], meet[1] + 55, meet[2], meet[1] + 105), "A = 1 - 2GM/(c^2 r),    B = A^(-1)", eq, "#064e3b")

d.line((375, 680 + 14, 690, 775 - 14), fill="#64748b", width=4)
d.polygon([(690, 775 - 14), (665, 765 - 24), (672, 790 - 5)], fill="#64748b")
d.line((1325, 680 + 14, 1010, 775 - 14), fill="#64748b", width=4)
d.polygon([(1010, 775 - 14), (1035, 765 - 24), (1028, 790 - 5)], fill="#64748b")

d.text((175, 185), "Bookkeeping route", font=head, fill="#1d4ed8")
d.text((1160, 185), "Closure route", font=head, fill="#7c3aed")

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT)
print(OUT)
