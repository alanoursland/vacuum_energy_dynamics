from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).resolve().parents[1] / "md" / "figure_1_selection_logic.png"
W, H = 1700, 950


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

d.text((70, 48), "Selection logic: nonzero R^2 conflicts with static frame indifference", font=title, fill="#172033")
d.text((72, 108), "The argument eliminates the scalaron by principle, not by fitting a short-range bound.", font=body, fill="#536173")

steps = [
    ("a != 0", "healthy R^2 scalaron\nell = sqrt(6a)", "#dbeafe"),
    ("Mandatory hair", "sourced static bodies\nleak exterior R(r)", "#dcfce7"),
    ("Anisotropy", "D^t_t - D^r_r = -R''\nand AB != 1", "#fef3c7"),
    ("Principle", "static vacuum has\nno preferred t-r frame", "#fee2e2"),
    ("Selection", "a = 0\nEH + Lambda remains", "#e5e7eb"),
]

x, y = 100, 270
box_w, box_h, gap = 260, 220, 70
for i, (h, b, fill) in enumerate(steps):
    x0 = x + i * (box_w + gap)
    d.rounded_rectangle((x0, y, x0 + box_w, y + box_h), radius=8, fill=fill, outline="#94a3b8", width=2)
    d.text((x0 + 24, y + 28), h, font=head, fill="#172033")
    yy = y + 80
    for line in b.split("\n"):
        d.text((x0 + 24, yy), line, font=body, fill="#334155")
        yy += 30
    if i < len(steps) - 1:
        ax = x0 + box_w + 10
        ay = y + box_h // 2
        bx = x0 + box_w + gap - 10
        d.line((ax, ay, bx, ay), fill="#64748b", width=4)
        d.polygon([(bx, ay), (bx - 20, ay - 12), (bx - 20, ay + 12)], fill="#64748b")

note = (250, 660, 1450, 805)
d.rounded_rectangle(note, radius=8, fill="#ffffff", outline="#0f766e", width=3)
d.text((290, 690), "Conditional theorem", font=head, fill="#065f46")
d.text((290, 735), "If exact static frame indifference is imposed, the healthy local R^2 scalar is forbidden.", font=body, fill="#064e3b")

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT)
print(OUT)
