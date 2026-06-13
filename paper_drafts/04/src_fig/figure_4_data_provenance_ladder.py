from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).resolve().parents[1] / "md" / "figure_4_data_provenance_ladder.png"
W, H = 1550, 1000


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

d.text((70, 48), "Data provenance grades for empirical gates", font=title, fill="#172033")
d.text((72, 108), "Numbers used to kill or support a claim need source status, not just plausibility.", font=body, fill="#536173")

levels = [
    ("AUTHOR_PROVIDED", "official table, supplement, or author communication", "#dcfce7"),
    ("VECTOR_EXTRACTED", "PDF path extraction with calibration and anchor validation", "#dbeafe"),
    ("ABSTRACT_VERIFIED", "text-stated value checked against source", "#e0f2fe"),
    ("TEXT_STATED", "explicitly stated in paper or caption", "#fef3c7"),
    ("FROM_MEMORY", "forbidden for empirical confrontation", "#fee2e2"),
]

x0, y0 = 260, 215
for i, (name, desc, fill) in enumerate(levels):
    w = 1030 - i * 50
    x = x0 + i * 48
    y = y0 + i * 120
    d.rounded_rectangle((x, y, x + w, y + 78), radius=8, fill=fill, outline="#94a3b8", width=2)
    d.text((x + 28, y + 18), name, font=head, fill="#172033")
    d.text((x + 390, y + 23), desc, font=body, fill="#334155")

gate = (230, 850, 1320, 925)
d.rounded_rectangle(gate, radius=8, fill="#ffffff", outline="#ef4444", width=3)
d.text((270, 873), "Gate norm:", font=head, fill="#991b1b")
d.text((425, 880), "no provenance grade, no empirical kill claim.", font=body, fill="#991b1b")

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT)
print(OUT)
