from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).resolve().parents[1] / "md" / "figure_2_extraction_pipeline.png"
W, H = 1850, 950


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


img = Image.new("RGB", (W, H), "#fbfaf7")
d = ImageDraw.Draw(img)
title = font(44, True)
label = font(25, True)
body = font(21)
small = font(18)

d.text((70, 48), "Validation-gated vector extraction pipeline", font=title, fill="#19212c")
d.text((72, 108), "The workflow emits data only after path identity and coordinate calibration pass an external anchor check.", font=body, fill="#4a5567")

steps = [
    ("1", "Load PDF page", "Record source, page, and drawing inventory."),
    ("2", "Extract paths", "Use vector drawing objects, not a rendered screenshot."),
    ("3", "Select candidates", "Filter by color, bbox, fill/stroke type, z-order, and geometry."),
    ("4", "Calibrate axes", "Fit linear or log maps from frame and tick geometry."),
    ("5", "Transform curve", "Convert PDF vertices into data coordinates."),
    ("6", "Validate anchor", "Compare against a text-stated number from the source paper."),
    ("7", "Export or refuse", "Write CSV plus provenance, or record the failure reason."),
]

positions = [
    (80, 225),
    (455, 225),
    (830, 225),
    (1205, 225),
    (1205, 545),
    (830, 545),
    (455, 545),
]
box_w, box_h = 305, 220
colors = ["#dbeafe", "#e0f2fe", "#dcfce7", "#fef3c7", "#ede9fe", "#fee2e2", "#e5e7eb"]

for i, step in enumerate(steps):
    x, y = positions[i]
    d.rounded_rectangle((x, y, x + box_w, y + box_h), radius=8, fill=colors[i], outline="#9aa7b8", width=2)
    d.ellipse((x + 24, y + 24, x + 68, y + 68), fill="#1f2937")
    num_box = d.textbbox((0, 0), step[0], font=label)
    d.text((x + 46 - (num_box[2] - num_box[0]) / 2, y + 46 - (num_box[3] - num_box[1]) / 2), step[0], font=label, fill="#ffffff")
    d.text((x + 84, y + 30), step[1], font=label, fill="#1f2937")
    yy = y + 94
    for line in wrap(d, step[2], box_w - 50, body):
        d.text((x + 26, yy), line, font=body, fill="#405064")
        yy += 29

for idx, (a, b) in enumerate(zip(positions, positions[1:])):
    if a[1] == b[1] and b[0] > a[0]:
        ax, ay = a[0] + box_w, a[1] + box_h // 2
        bx, by = b[0], b[1] + box_h // 2
        d.line((ax + 8, ay, bx - 8, by), fill="#64748b", width=4)
        d.polygon([(bx - 8, by), (bx - 28, by - 12), (bx - 28, by + 12)], fill="#64748b")
    elif a[1] == b[1] and b[0] < a[0]:
        ax, ay = a[0], a[1] + box_h // 2
        bx, by = b[0] + box_w, b[1] + box_h // 2
        d.line((ax - 8, ay, bx + 8, by), fill="#64748b", width=4)
        d.polygon([(bx + 8, by), (bx + 28, by - 12), (bx + 28, by + 12)], fill="#64748b")
    else:
        x = a[0] + box_w // 2
        y1 = a[1] + box_h
        y2 = b[1]
        d.line((x, y1 + 8, x, y2 - 8), fill="#64748b", width=4)
        d.polygon([(x, y2 - 8), (x - 12, y2 - 28), (x + 12, y2 - 28)], fill="#64748b")

gate = (1010, 810, 1765, 885)
d.rounded_rectangle(gate, radius=8, fill="#ffffff", outline="#ef4444", width=3)
d.text((1138, 842), "Rule: no validated anchor, no physics-grade CSV", font=label, fill="#991b1b")
d.text((86, 842), "Output bundle: data table + source PDF identity + path rule + calibration + validation log", font=small, fill="#4a5567")

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT)
print(OUT)
