from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).resolve().parents[1] / "md" / "figure_3_four_derivative_elimination.png"
W, H = 1700, 980


def font(size, bold=False):
    name = "arialbd.ttf" if bold else "arial.ttf"
    try:
        return ImageFont.truetype(name, size)
    except OSError:
        return ImageFont.load_default()


img = Image.new("RGB", (W, H), "#f8fafc")
d = ImageDraw.Draw(img)
title = font(42, True)
head = font(26, True)
body = font(21)

d.text((70, 48), "Four-derivative freedom is eliminated by two gates", font=title, fill="#172033")
d.text((72, 108), "Ghost stability narrows the space; P7-prime removes the scalaron survivor.", font=body, fill="#536173")

nodes = [
    ((95, 245, 445, 385), "Quadratic curvature", "Weyl^2, R_ab R^ab, R^2, GB", "#e0f2fe"),
    ((565, 160, 985, 300), "Spin-2 ghost gate", "TT terms create negative-residue massive spin-2 poles", "#fee2e2"),
    ((565, 410, 955, 550), "Healthy survivor", "a R^2, scalaron range ell* = sqrt(6a)", "#dcfce7"),
    ((1075, 410, 1465, 550), "P7-prime contradiction", "mandatory static hair violates AB = 1", "#fef3c7"),
    ((1075, 690, 1465, 810), "Result", "a = 0; only Einstein-Hilbert + Lambda remains", "#e5e7eb"),
]

for box, h, b, fill in nodes:
    d.rounded_rectangle(box, radius=8, fill=fill, outline="#94a3b8", width=2)
    d.text((box[0] + 24, box[1] + 25), h, font=head, fill="#172033")
    d.text((box[0] + 24, box[1] + 72), b, font=body, fill="#334155")

def arrow(a, b):
    d.line((a[0], a[1], b[0], b[1]), fill="#64748b", width=4)
    vx, vy = b[0] - a[0], b[1] - a[1]
    if abs(vx) > abs(vy):
        sign = 1 if vx > 0 else -1
        d.polygon([(b[0], b[1]), (b[0] - sign * 22, b[1] - 12), (b[0] - sign * 22, b[1] + 12)], fill="#64748b")
    else:
        sign = 1 if vy > 0 else -1
        d.polygon([(b[0], b[1]), (b[0] - 12, b[1] - sign * 22), (b[0] + 12, b[1] - sign * 22)], fill="#64748b")

arrow((445, 315), (565, 230))
arrow((445, 315), (565, 480))
arrow((955, 480), (1075, 480))
arrow((1270, 550), (1270, 690))

d.text((1050, 210), "killed", font=head, fill="#b91c1c")
d.line((990, 230, 1038, 230), fill="#b91c1c", width=4)
d.polygon([(1038, 230), (1018, 218), (1018, 242)], fill="#b91c1c")

note = (180, 720, 880, 850)
d.rounded_rectangle(note, radius=8, fill="#ffffff", outline="#cbd5e1", width=2)
d.text((210, 748), "Empirical face", font=head, fill="#172033")
d.text((210, 792), "The theory predicts no gravitational-strength Yukawa signal from this sector.", font=body, fill="#334155")

OUT.parent.mkdir(parents=True, exist_ok=True)
img.save(OUT)
print(OUT)
