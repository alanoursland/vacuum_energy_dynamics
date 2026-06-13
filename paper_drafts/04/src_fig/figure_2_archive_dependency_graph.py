from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).resolve().parents[1] / "md" / "figure_2_archive_dependency_graph.png"
W, H = 1700, 1050


def font(size, bold=False):
    name = "arialbd.ttf" if bold else "arial.ttf"
    try:
        return ImageFont.truetype(name, size)
    except OSError:
        return ImageFont.load_default()


img = Image.new("RGB", (W, H), "#fbfaf7")
d = ImageDraw.Draw(img)
title = font(42, True)
head = font(24, True)
body = font(18)

d.text((70, 48), "Archive dependency graph pattern", font=title, fill="#172033")
d.text((72, 108), "Trial groups declare upstream dependencies so conclusions cannot silently mutate.", font=body, fill="#536173")

groups = [
    ("000", "charter", 110, 250),
    ("005", "adoptions", 110, 470),
    ("002", "static bootstrap", 430, 250),
    ("006", "radiative positivity", 430, 470),
    ("008", "radiative bootstrap", 760, 360),
    ("009", "boundary gate", 1090, 250),
    ("010", "curvature health", 1090, 470),
    ("012", "vector closure", 1410, 360),
]

def box(item):
    code, label, x, y = item
    return (x, y, x + 230, y + 110)

for item in groups:
    b = box(item)
    d.rounded_rectangle(b, radius=8, fill="#ffffff", outline="#94a3b8", width=2)
    d.text((b[0] + 18, b[1] + 18), item[0], font=head, fill="#1f2937")
    d.text((b[0] + 18, b[1] + 58), item[1], font=body, fill="#334155")

edges = [
    (0, 2), (1, 2), (0, 3), (2, 4), (3, 4),
    (4, 5), (4, 6), (5, 7), (6, 7),
]

for a, bidx in edges:
    ba, bb = box(groups[a]), box(groups[bidx])
    x1, y1 = ba[2], (ba[1] + ba[3]) / 2
    x2, y2 = bb[0], (bb[1] + bb[3]) / 2
    d.line((x1, y1, x2, y2), fill="#64748b", width=3)
    d.ellipse((x2 - 5, y2 - 5, x2 + 5, y2 + 5), fill="#64748b")

legend = (220, 790, 1480, 930)
d.rounded_rectangle(legend, radius=8, fill="#eef2ff", outline="#a5b4fc", width=2)
d.text((260, 820), "Reproducibility floor", font=head, fill="#312e81")
d.text((260, 865), "Each node is a runnable or inspectable artifact; each edge is an explicit dependency.", font=body, fill="#312e81")
d.text((260, 895), "This is not formal proof, but it prevents quiet coefficient and assumption drift.", font=body, fill="#312e81")

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT)
print(OUT)
