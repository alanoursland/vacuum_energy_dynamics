from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).resolve().parents[1] / "md" / "figure_4_gr_vs_ved_scope.png"
W, H = 1600, 950


def font(size, bold=False):
    name = "arialbd.ttf" if bold else "arial.ttf"
    try:
        return ImageFont.truetype(name, size)
    except OSError:
        return ImageFont.load_default()


img = Image.new("RGB", (W, H), "#fbfaf7")
d = ImageDraw.Draw(img)
title = font(42, True)
head = font(27, True)
body = font(21)

d.text((70, 48), "Same closed gravitational equations, different open program", font=title, fill="#172033")
d.text((72, 108), "Paper 1 should be explicit about what is GR-equivalent and what remains VED-specific.", font=body, fill="#536173")

shared = (510, 185, 1090, 390)
d.rounded_rectangle(shared, radius=8, fill="#e0f2fe", outline="#0284c7", width=3)
d.text((555, 225), "Closed gravitational sector", font=head, fill="#075985")
d.text((555, 278), "G_ab + Lambda g_ab = (8 pi G / c^4) T_ab", font=body, fill="#0c4a6e")
d.text((555, 322), "Weak field, radiation, vector sector match GR", font=body, fill="#0c4a6e")

gr = (90, 500, 730, 820)
ved = (870, 500, 1510, 820)
for box, h, fill, color in [
    (gr, "GR reading", "#f1f5f9", "#334155"),
    (ved, "VED surplus", "#ecfdf5", "#065f46"),
]:
    d.rounded_rectangle(box, radius=8, fill=fill, outline="#94a3b8", width=2)
    d.text((box[0] + 35, box[1] + 35), h, font=head, fill=color)

gr_items = [
    "metric geometry is primitive",
    "Lambda may be a constant",
    "field energy is nonlocal/pseudotensorial",
    "dark sector sits in T_ab or beyond GR",
]
ved_items = [
    "metric is vacuum substance configuration",
    "static field energy has local density",
    "Lambda is assigned to vacuum-sector origin",
    "substance frame exists but is quarantined",
]

for items, box, color in [(gr_items, gr, "#334155"), (ved_items, ved, "#065f46")]:
    yy = box[1] + 105
    for item in items:
        d.ellipse((box[0] + 40, yy + 8, box[0] + 52, yy + 20), fill=color)
        d.text((box[0] + 70, yy), item, font=body, fill=color)
        yy += 48

d.line((800, 390, 410, 500), fill="#64748b", width=4)
d.polygon([(410, 500), (433, 482), (438, 508)], fill="#64748b")
d.line((800, 390, 1190, 500), fill="#64748b", width=4)
d.polygon([(1190, 500), (1167, 482), (1162, 508)], fill="#64748b")

footer = (270, 860, 1330, 910)
d.rounded_rectangle(footer, radius=8, fill="#fff7ed", outline="#fdba74", width=2)
d.text((310, 873), "Do not sell a gravitational deviation here; sell a derivation and a disciplined open vacuum-sector program.", font=body, fill="#7c2d12")

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT)
print(OUT)
