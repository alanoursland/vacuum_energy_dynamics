from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).resolve().parents[1] / "md" / "figure_1_vector_pdf_anatomy.png"
W, H = 1600, 950


def font(size, bold=False):
    name = "arialbd.ttf" if bold else "arial.ttf"
    try:
        return ImageFont.truetype(name, size)
    except OSError:
        return ImageFont.load_default()


def text_center(draw, xy, text, fnt, fill):
    box = draw.textbbox((0, 0), text, font=fnt)
    x = xy[0] - (box[2] - box[0]) / 2
    y = xy[1] - (box[3] - box[1]) / 2
    draw.text((x, y), text, font=fnt, fill=fill)


img = Image.new("RGB", (W, H), "#f7f8fb")
d = ImageDraw.Draw(img)

title = font(44, True)
label = font(27, True)
body = font(24)
small = font(20)
mono = font(20)

d.text((70, 42), "A vector PDF figure contains paths, not only pixels", font=title, fill="#18212f")
d.text((72, 104), "The same plotted curve can be viewed as an image or as recoverable drawing geometry.", font=body, fill="#4b5565")

left = (80, 185, 750, 850)
right = (850, 185, 1520, 850)
for box, head in [(left, "reader view"), (right, "PDF drawing objects")]:
    d.rounded_rectangle(box, radius=8, fill="#ffffff", outline="#c7d0dd", width=2)
    d.text((box[0] + 30, box[1] + 25), head, font=label, fill="#1f2a3a")

# Left: plot-like raster view.
px = (155, 290, 680, 745)
d.rectangle(px, fill="#fbfcff", outline="#475569", width=3)
for i in range(6):
    x = px[0] + 70 + i * 80
    d.line((x, px[3], x, px[3] + 12), fill="#475569", width=3)
for i in range(7):
    y = px[3] - 55 - i * 55
    d.line((px[0] - 12, y, px[0], y), fill="#475569", width=3)
for i in range(6):
    x = px[0] + 70 + i * 80
    d.line((x, px[1], x, px[3]), fill="#e7ebf1", width=1)
for i in range(7):
    y = px[3] - 55 - i * 55
    d.line((px[0], y, px[2], y), fill="#e7ebf1", width=1)

curve = [(190, 665), (240, 635), (300, 600), (355, 552), (420, 495), (482, 420), (555, 360), (640, 315)]
fill_poly = curve + [(680, 745), (190, 745)]
d.polygon(fill_poly, fill="#9ad897")
d.line(curve, fill="#087f5b", width=9, joint="curve")
d.line(curve, fill="#063f31", width=3, joint="curve")
d.text((275, 775), "visible pixels after rendering", font=small, fill="#5b6575")

# Right: PDF object anatomy.
rx = (925, 290, 1450, 745)
d.rectangle(rx, fill="#fbfcff", outline="#475569", width=3)
for i in range(6):
    x = rx[0] + 70 + i * 80
    d.line((x, rx[3], x, rx[3] + 12), fill="#7c8798", width=2)
for i in range(7):
    y = rx[3] - 55 - i * 55
    d.line((rx[0] - 12, y, rx[0], y), fill="#7c8798", width=2)

path_curve = [(960, 665), (1010, 635), (1070, 600), (1125, 552), (1190, 495), (1252, 420), (1325, 360), (1410, 315)]
for p in path_curve:
    d.ellipse((p[0] - 7, p[1] - 7, p[0] + 7, p[1] + 7), fill="#0f766e")
d.line(path_curve, fill="#0f766e", width=4)
d.line(path_curve + [(1450, 745), (960, 745), path_curve[0]], fill="#22c55e", width=3)

objects = [
    ("frame path", "#475569", (950, 770)),
    ("tick paths", "#7c8798", (950, 802)),
    ("fill polygon", "#22c55e", (1160, 770)),
    ("curve vertices", "#0f766e", (1160, 802)),
]
for name, color, pos in objects:
    d.rectangle((pos[0], pos[1] + 5, pos[0] + 24, pos[1] + 21), fill=color)
    d.text((pos[0] + 36, pos[1]), name, font=small, fill="#364152")

code_box = (1095, 242, 1408, 280)
d.rounded_rectangle(code_box, radius=6, fill="#eef6ff", outline="#a9bfd8", width=1)
text_center(d, ((code_box[0] + code_box[2]) / 2, 261), "page.get_drawings()", font(21, True), "#22415f")

d.line((760, 515, 840, 515), fill="#64748b", width=4)
d.polygon([(840, 515), (815, 500), (815, 530)], fill="#64748b")
text_center(d, (800, 475), "inspect", small, "#64748b")

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT)
print(OUT)
