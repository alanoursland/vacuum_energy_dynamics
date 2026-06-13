from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).resolve().parents[1] / "md" / "figure_3_cross_gram.png"
W, H = 1800, 1050
BG = (248, 249, 246)
INK = (33, 39, 44)
MUTED = (92, 99, 105)
BLUE = (34, 96, 148)
GREEN = (46, 125, 92)
GOLD = (178, 124, 39)


def font(size, bold=False):
    name = "arialbd.ttf" if bold else "arial.ttf"
    try:
        return ImageFont.truetype(name, size)
    except OSError:
        return ImageFont.load_default()


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)
title = font(54, True)
label = font(34, True)
body = font(28)
small = font(23)

d.text((90, 70), "Cross-Gram interpretation", fill=INK, font=title)
d.text((90, 140), "Invertibility comes from nondegenerate pairing between two bases.", fill=MUTED, font=body)

boxes = {
    "rows": (115, 330, 545, 570),
    "matrix": (685, 300, 1115, 600),
    "cols": (1255, 330, 1685, 570),
}

d.rounded_rectangle(boxes["rows"], radius=18, fill=(255, 255, 255), outline=BLUE, width=5)
d.rounded_rectangle(boxes["matrix"], radius=18, fill=(255, 255, 255), outline=GOLD, width=5)
d.rounded_rectangle(boxes["cols"], radius=18, fill=(255, 255, 255), outline=GREEN, width=5)

d.text((160, 365), "Row basis", fill=BLUE, font=label)
d.text((160, 425), "chi_(R,1), ..., chi_(R,N)", fill=INK, font=body)
d.text((160, 475), "admissibility kernel", fill=MUTED, font=small)

d.text((755, 355), "A_kq = <chi_k, B_q>", fill=GOLD, font=label)
d.text((760, 430), "cross-Gram matrix", fill=INK, font=body)
d.text((760, 480), "not a self-Gram matrix", fill=MUTED, font=small)

d.text((1300, 365), "Balanced basis", fill=GREEN, font=label)
d.text((1300, 425), "B_(R,1), ..., B_(R,N)", fill=INK, font=body)
d.text((1300, 475), "same finite space", fill=MUTED, font=small)

def arrow(x1, y1, x2, y2, color):
    d.line((x1, y1, x2, y2), fill=color, width=6)
    if x2 > x1:
        d.polygon([(x2, y2), (x2 - 22, y2 - 14), (x2 - 22, y2 + 14)], fill=color)
    else:
        d.polygon([(x2, y2), (x2 + 22, y2 - 14), (x2 + 22, y2 + 14)], fill=color)

arrow(545, 450, 685, 450, BLUE)
arrow(1255, 450, 1115, 450, GREEN)

d.rounded_rectangle((265, 735, 1535, 860), radius=16, fill=(255, 255, 255), outline=(212, 216, 214), width=3)
d.text((310, 765), "A = G_U T", fill=INK, font=label)
d.text((555, 770), "positive self-Gram times invertible basis change", fill=MUTED, font=body)
d.text((310, 815), "determinant positivity is not the required property", fill=MUTED, font=small)

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT)
print(OUT)

