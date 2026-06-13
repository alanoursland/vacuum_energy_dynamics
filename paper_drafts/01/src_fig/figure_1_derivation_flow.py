from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).resolve().parents[1] / "md" / "figure_1_derivation_flow.png"
W, H = 1800, 1050


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
title = font(44, True)
head = font(25, True)
body = font(20)
small = font(18)

d.text((70, 48), "Derivation flow: postulates to Einstein response", font=title, fill="#172033")
d.text((72, 108), "The route fixes sectors and kills freedoms before stating the final field equation.", font=body, fill="#536173")

steps = [
    ("Postulates", "P1-P6, P7-prime, P9 define vacuum substance, exchange, frame indifference, and count-once source bookkeeping.", "#dbeafe"),
    ("Static bootstrap", "Areal flux + P7-prime + P9 give Schwarzschild exterior and negative static field energy.", "#dcfce7"),
    ("Sector stability", "Negative sector is constraint; TT radiation is positive; source-free static vacuum is unique.", "#fef3c7"),
    ("Spin-2 closure", "Gauge tensor kinematics plus self-coupling fix Einstein response and radiative normalization.", "#ede9fe"),
    ("4-derivative gate", "Ghost gate leaves R^2; P7-prime kills scalaron hair; a = 0.", "#fee2e2"),
    ("Result", "G_ab + Lambda g_ab = (8 pi G / c^4) T_ab.", "#e5e7eb"),
]

x0, y0 = 90, 230
box_w, box_h = 250, 360
gap = 40
for i, (name, desc, fill) in enumerate(steps):
    x = x0 + i * (box_w + gap)
    d.rounded_rectangle((x, y0, x + box_w, y0 + box_h), radius=8, fill="#ffffff", outline="#cbd5e1", width=2)
    d.rectangle((x, y0, x + box_w, y0 + 78), fill=fill)
    d.text((x + 22, y0 + 24), name, font=head, fill="#1f2937")
    yy = y0 + 112
    for line in wrap(d, desc, box_w - 42, body):
        d.text((x + 22, yy), line, font=body, fill="#334155")
        yy += 28
    if i < len(steps) - 1:
        ax = x + box_w + 8
        ay = y0 + box_h // 2
        bx = x + box_w + gap - 8
        d.line((ax, ay, bx, ay), fill="#64748b", width=4)
        d.polygon([(bx, ay), (bx - 20, ay - 12), (bx - 20, ay + 12)], fill="#64748b")

ledger = (160, 705, 1640, 920)
d.rounded_rectangle(ledger, radius=8, fill="#ffffff", outline="#94a3b8", width=2)
d.text((195, 735), "Audit rules", font=head, fill="#172033")
rules = [
    "Newton's G is the only empirical normalization.",
    "Classical tests enter after derivation as kill conditions.",
    "Covariant closure uses standard spin-2 uniqueness until the in-house proof is written.",
]
yy = 786
for rule in rules:
    d.ellipse((205, yy + 8, 217, yy + 20), fill="#475569")
    d.text((235, yy), rule, font=body, fill="#334155")
    yy += 42

d.text((70, 985), "Figure is schematic; theorem labels and script paths should be added in the final version.", font=small, fill="#64748b")

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT)
print(OUT)
