# Extract the Lee 2020 95%-CL Yukawa exclusion curve alpha(lambda) directly
# from the vector paths inside the arXiv PDF figure -- no hand digitization.
#
# Source: arXiv:2002.11761 (Lee et al., PRL 124, 101101 (2020)), Figure 5
# (bottom panel), page 4 of the PDF. The figure is pure vector art (zero
# raster images on that page), so the curve exists in the PDF content
# stream as literal path coordinates laid down by the authors' plotting
# software. This tool recovers them and inverts the axis transform.
#
# Method
# ------
# 1. The newly-excluded region is the (0,1,0) green fill polygon; the
#    previously-excluded region is painted OVER it in yellow (painter's
#    algorithm), so the green polygon's lower-left vertex chain IS the
#    Lee 2020 95% upper-limit curve.
# 2. Axis calibration from tick geometry (log-log):
#      x major ticks (len 5.43) at 421.22 / 483.21 / 545.20 pdf-units,
#        exactly evenly spaced => decades; figure labels => 1e-5/1e-4/1e-3 m.
#        Minor ticks confirm: x(3e-6 family) matches log10 spacing to 0.01 unit.
#      y major ticks evenly spaced (delta = 150.76/9) from 434.72 (top)
#        to 585.48 (bottom) => 1e6 down to 1e-3.
# 3. Validation anchor (data-gate protocol): the abstract's
#    VERIFIED_FROM_ABSTRACT statement "|alpha| = 1 excluded for
#    lambda >= 38.6 um" predicts the curve crosses y(alpha=1) = 535.23
#    at x = 457.6. The extracted chain crosses at x = 457.59 (0.03%).
#
# Output: .data/alpha_lambda/lee2020_alpha_lambda_95cl.csv
#    columns: lambda_m, alpha_95cl
#    provenance: VECTOR_EXTRACTED_FROM_ARXIV_PDF (author-coordinate
#    precision; superior to manual digitization)
#
# Run from src_exp:  PYTHONPATH=. python dataexp/tools/extract_lee2020_fig5.py
# Requires: pymupdf;  the PDF at .data/alpha_lambda/lee2020_arxiv.pdf
# (download: https://arxiv.org/pdf/2002.11761)

import csv
import math
import sys
import urllib.request
from pathlib import Path

import fitz  # pymupdf

DATA_DIR = Path(__file__).resolve().parents[1] / ".data" / "alpha_lambda"
PDF_PATH = DATA_DIR / "lee2020_arxiv.pdf"
OUT_PATH = DATA_DIR / "lee2020_alpha_lambda_95cl.csv"
ARXIV_URL = "https://arxiv.org/pdf/2002.11761"

PAGE_INDEX = 3  # page 4 (0-based)

# calibration (pdf coords; see header derivation)
X_DECADE_TICKS = [421.22, 483.21, 545.20]   # = 1e-5, 1e-4, 1e-3 m
X_PER_DECADE = (X_DECADE_TICKS[2] - X_DECADE_TICKS[0]) / 2.0
Y_TOP, Y_BOTTOM = 434.72, 585.48            # = 1e6, 1e-3
Y_PER_DECADE = (Y_BOTTOM - Y_TOP) / 9.0

# protocol sanity anchor (VERIFIED_FROM_ABSTRACT, Lee 2020)
ANCHOR_ALPHA = 1.0
ANCHOR_LAMBDA_M = 38.6e-6
ANCHOR_TOL_REL = 0.02   # 2% tolerance on the lambda crossing


def x_to_lambda(x: float) -> float:
    return 10 ** (-3.0 - (X_DECADE_TICKS[2] - x) / X_PER_DECADE)


def y_to_alpha(y: float) -> float:
    return 10 ** (-3.0 + (Y_BOTTOM - y) / Y_PER_DECADE)


def ensure_pdf() -> None:
    if PDF_PATH.exists():
        return
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    print(f"[INFO] downloading {ARXIV_URL} -> {PDF_PATH}")
    urllib.request.urlretrieve(ARXIV_URL, PDF_PATH)


def extract_green_chain() -> list:
    doc = fitz.open(PDF_PATH)
    page = doc[PAGE_INDEX]
    for dr in page.get_drawings():
        if dr["type"] == "f" and dr.get("fill") == (0.0, 1.0, 0.0):
            verts = []
            for item in dr["items"]:
                if item[0] == "l":
                    if not verts:
                        verts.append((item[1].x, item[1].y))
                    verts.append((item[2].x, item[2].y))
            return verts
    raise RuntimeError("green fill polygon not found on page 4")


def main() -> None:
    ensure_pdf()
    verts = extract_green_chain()
    # the chain runs bottom-right -> top-left along the limit curve; the
    # final vertex is the top-frame exit (alpha = 1e6 cutoff): keep it,
    # flagged by the frame ordinate.
    rows = []
    for (x, y) in verts:
        rows.append((x_to_lambda(x), y_to_alpha(y)))
    rows.sort(key=lambda t: t[0])

    # protocol validation: |alpha| = 1 crossing
    crossing = None
    for (l1, a1), (l2, a2) in zip(rows, rows[1:]):
        if (a1 - ANCHOR_ALPHA) * (a2 - ANCHOR_ALPHA) <= 0 and a1 != a2:
            t = (math.log10(ANCHOR_ALPHA) - math.log10(a1)) / (math.log10(a2) - math.log10(a1))
            crossing = 10 ** (math.log10(l1) + t * (math.log10(l2) - math.log10(l1)))
            break
    if crossing is None:
        sys.exit("[FAIL] curve never crosses alpha = 1: extraction wrong")
    rel = abs(crossing - ANCHOR_LAMBDA_M) / ANCHOR_LAMBDA_M
    print(f"[CHECK] alpha=1 crossing: {crossing*1e6:.2f} um (abstract anchor {ANCHOR_LAMBDA_M*1e6:.1f} um, "
          f"rel. dev. {rel*100:.2f}%)")
    if rel > ANCHOR_TOL_REL:
        sys.exit("[FAIL] anchor validation outside tolerance; do not use the CSV")

    with open(OUT_PATH, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["lambda_m", "alpha_95cl"])
        w.writerow([f"# source: arXiv:2002.11761 Fig 5 (bottom), vector-path extraction", ""])
        for lam, al in rows:
            w.writerow([f"{lam:.6e}", f"{al:.6e}"])
    print(f"[OK] wrote {len(rows)} points -> {OUT_PATH}")

    # convenience readouts for the program
    def crossing_at(alpha_target: float):
        for (l1, a1), (l2, a2) in zip(rows, rows[1:]):
            if (a1 - alpha_target) * (a2 - alpha_target) <= 0 and a1 != a2:
                t = (math.log10(alpha_target) - math.log10(a1)) / (math.log10(a2) - math.log10(a1))
                return 10 ** (math.log10(l1) + t * (math.log10(l2) - math.log10(l1)))
        return None

    for tgt, label in [(1.0, "|alpha| = 1"), (1.0 / 3.0, "alpha = 1/3 (scalaron, G20)")]:
        cx = crossing_at(tgt)
        if cx:
            print(f"[RESULT] {label}: excluded for lambda >= {cx*1e6:.2f} um")
        else:
            print(f"[RESULT] {label}: no crossing inside figure range")


if __name__ == "__main__":
    main()
