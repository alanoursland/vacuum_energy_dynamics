from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).resolve().parents[1] / "md" / "figure_3_status_separation.png"
W, H = 1600, 950


def font(size, bold=False):
    name = "arialbd.ttf" if bold else "arial.ttf"
    try:
        return ImageFont.truetype(name, size)
    except OSError:
        return ImageFont.load_default()


img = Image.new("RGB", (W, H), "#f8fafc")
d = ImageDraw.Draw(img)
title = font(42, True)
head = font(27, True)
body = font(21)

d.text((70, 48), "Keep status modes separate", font=title, fill="#172033")
d.text((72, 108), "A disciplined archive does not let probes, postulates, theorems, and failures blur together.", font=body, fill="#536173")

cols = [
    ("Probe", "early formalization; not owner-confirmed", "#e0f2fe", "#075985"),
    ("Adoption", "human-owned postulate with fences", "#fef3c7", "#92400e"),
    ("Theorem", "derived result with dependencies", "#dcfce7", "#065f46"),
    ("Killed", "failed a predeclared gate", "#fee2e2", "#991b1b"),
]

for i, (name, desc, fill, color) in enumerate(cols):
    x = 95 + i * 375
    box = (x, 230, x + 310, 690)
    d.rounded_rectangle(box, radius=8, fill="#ffffff", outline="#cbd5e1", width=2)
    d.rectangle((box[0], box[1], box[2], box[1] + 90), fill=fill)
    d.text((box[0] + 28, box[1] + 29), name, font=head, fill=color)
    words = desc.split()
    yy = box[1] + 125
    line = ""
    for word in words:
        test = f"{line} {word}".strip()
        if d.textbbox((0, 0), test, font=body)[2] < 250:
            line = test
        else:
            d.text((box[0] + 28, yy), line, font=body, fill="#334155")
            yy += 30
            line = word
    if line:
        d.text((box[0] + 28, yy), line, font=body, fill="#334155")
    if i < len(cols) - 1:
        d.line((box[2] + 18, 460, box[2] + 55, 460), fill="#64748b", width=4)
        d.polygon([(box[2] + 55, 460), (box[2] + 35, 448), (box[2] + 35, 472)], fill="#64748b")

rules = (235, 760, 1365, 865)
d.rounded_rectangle(rules, radius=8, fill="#ffffff", outline="#94a3b8", width=2)
d.text((270, 790), "Rule:", font=head, fill="#172033")
d.text((355, 797), "success downstream does not convert an adoption into a theorem; a killed probe is not necessarily a killed intuition.", font=body, fill="#334155")

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT)
print(OUT)
