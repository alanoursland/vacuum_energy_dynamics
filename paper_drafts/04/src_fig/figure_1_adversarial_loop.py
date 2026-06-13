from pathlib import Path
import math

from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).resolve().parents[1] / "md" / "figure_1_adversarial_loop.png"
W, H = 1600, 1000


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

d.text((70, 48), "Adversarial AI-assisted theory-development loop", font=title, fill="#172033")
d.text((72, 108), "The model generates and attacks candidates inside a workflow that can kill them.", font=body, fill="#536173")

center = (800, 520)
radius = 300
nodes = [
    ("Charter", "question + kill conditions", "#dbeafe"),
    ("Candidate", "formalized probe", "#e0f2fe"),
    ("Script", "derive from scratch", "#dcfce7"),
    ("Gate", "PASS / KILLED / NOT_READY", "#fef3c7"),
    ("Record", "lab report + provenance", "#ede9fe"),
    ("Handoff", "theorem, adoption, or kill", "#fee2e2"),
]

positions = []
for i, node in enumerate(nodes):
    angle = -math.pi / 2 + i * 2 * math.pi / len(nodes)
    x = center[0] + radius * math.cos(angle)
    y = center[1] + radius * math.sin(angle)
    positions.append((x, y))

for i, (x, y) in enumerate(positions):
    nx, ny = positions[(i + 1) % len(positions)]
    d.line((x, y, nx, ny), fill="#64748b", width=4)
    dx, dy = nx - x, ny - y
    length = (dx * dx + dy * dy) ** 0.5
    ux, uy = dx / length, dy / length
    px, py = nx - ux * 80, ny - uy * 80
    d.polygon([(px, py), (px - uy * 12 - ux * 22, py + ux * 12 - uy * 22), (px + uy * 12 - ux * 22, py - ux * 12 - uy * 22)], fill="#64748b")

for (x, y), (name, desc, fill) in zip(positions, nodes):
    box = (x - 150, y - 70, x + 150, y + 70)
    d.rounded_rectangle(box, radius=8, fill=fill, outline="#94a3b8", width=2)
    d.text((box[0] + 24, box[1] + 22), name, font=head, fill="#172033")
    d.text((box[0] + 24, box[1] + 62), desc, font=body, fill="#334155")

core = (610, 435, 990, 605)
d.rounded_rectangle(core, radius=8, fill="#ffffff", outline="#0f766e", width=3)
d.text((655, 468), "Adversarial placement", font=head, fill="#065f46")
d.text((655, 512), "AI proposes, formalizes,", font=body, fill="#064e3b")
d.text((655, 542), "derives, and attacks.", font=body, fill="#064e3b")
d.text((655, 572), "The archive decides.", font=body, fill="#064e3b")

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT)
print(OUT)
