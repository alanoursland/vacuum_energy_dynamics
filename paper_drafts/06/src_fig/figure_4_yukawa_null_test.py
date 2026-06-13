from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).resolve().parents[1] / "md" / "figure_4_yukawa_null_test.png"
W, H = 1600, 930


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

d.text((70, 48), "Phenomenological split: bound the scalaron or forbid it", font=title, fill="#172033")
d.text((72, 108), "Short-range experiments are bounds if a is allowed, and null tests if frame indifference is exact.", font=body, fill="#536173")

left = (110, 230, 735, 720)
right = (865, 230, 1490, 720)
for box, h, fill, color in [
    (left, "If R^2 is allowed", "#e0f2fe", "#075985"),
    (right, "If frame indifference is exact", "#dcfce7", "#065f46"),
]:
    d.rounded_rectangle(box, radius=8, fill="#ffffff", outline="#94a3b8", width=2)
    d.rectangle((box[0], box[1], box[2], box[1] + 90), fill=fill)
    d.text((box[0] + 35, box[1] + 28), h, font=head, fill=color)

left_lines = [
    "V(r) = -Gm/r [1 + alpha exp(-r/ell)]",
    "alpha = 1/3",
    "ell = sqrt(6a)",
    "Lee 2020 curve: alpha = 1/3 crossing",
    "ell < 54.05 um",
]
right_lines = [
    "a = 0",
    "no scalaron",
    "no gravitational-strength Yukawa",
    "any confirmed signal forces",
    "a scope revision of the principle",
]

for box, lines, color in [(left, left_lines, "#075985"), (right, right_lines, "#065f46")]:
    yy = box[1] + 130
    for line in lines:
        d.ellipse((box[0] + 40, yy + 8, box[0] + 52, yy + 20), fill=color)
        d.text((box[0] + 70, yy), line, font=body, fill="#334155")
        yy += 55

d.line((735, 475, 865, 475), fill="#64748b", width=4)
d.text((760, 435), "selection", font=body, fill="#64748b")
d.polygon([(865, 475), (842, 462), (842, 488)], fill="#64748b")

footer = (250, 800, 1350, 865)
d.rounded_rectangle(footer, radius=8, fill="#fff7ed", outline="#fdba74", width=2)
d.text((290, 820), "Data do not select a = 0; the principle does. Data test whether the principle survives.", font=body, fill="#7c2d12")

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT)
print(OUT)
