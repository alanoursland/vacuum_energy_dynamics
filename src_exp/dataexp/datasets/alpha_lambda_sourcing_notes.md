# Sourcing Notes: alpha(lambda) Exclusion Curves (Short-Range Gravity)

**Date:** 2026-06-12
**Status:** Lee 2020 curve EXTRACTED (vector-path method, anchor-validated).
Tan 2020 pending. No hand digitization was needed.

## Why we need the curves

The abstract-verified anchors (single numbers like "|alpha| = 1 excluded
for lambda >= 38.6 um") are points. The program needs other crossings of
the same curves -- above all the **alpha = 1/3 crossing** (the scalaron
coupling fixed by Gate G20), which also calibrates the P7' null test and
refines the UFFT squeeze. Those crossings exist only on the published
exclusion *plots*.

## Search trail (what exists where)

1. **Eot-Wash group page** -- https://www.npl.washington.edu/eotwash/inverse-square-law
   Checked 2026-06-12: NO downloadable limit-curve data. Links only to
   old arXiv papers (hep-ph/0011014, hep-ph/0611184). Group contact via
   the People page would be the route for official tables.
2. **APS journal page (Lee 2020)** -- https://link.aps.org/doi/10.1103/PhysRevLett.124.101101
   Paywalled; no public supplemental data file found from search.
3. **Public compilations (GitHub/Zenodo)** -- searched "fifth force
   Yukawa exclusion limits data compilation"; no centralized digitized
   repository surfaced. (If one appears, prefer it and cite it.)
4. **arXiv PDFs** -- the winning route, see below.
   - Lee 2020: arXiv:2002.11761 -> https://arxiv.org/pdf/2002.11761
   - Tan 2020 (PRL 124, 051301, HUST): locate via
     https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.124.051301
     (find the arXiv id from the paper page or arXiv search:
     "Improvement for Testing the Gravitational Inverse-Square Law at
     the Submillimeter Range" Tan).

## The vector-extraction method (no digitization needed)

Physics figures are usually **vector art**: the curves live inside the
PDF as path coordinates written by the authors' plotting software.
Checked with PyMuPDF: Lee 2020 page 4 has 7295 drawing groups and ZERO
raster images -- Figure 5 is fully vector.

Recipe (implemented in `dataexp/tools/extract_lee2020_fig5.py`):

1. `page.get_drawings()` -> all stroke/fill paths with colors & widths.
2. Identify the plot frame and **tick marks** (short segments on the
   axes). Log-decade ticks are exactly evenly spaced; minor ticks at
   2,3,...,9 confirm the log calibration to ~0.01 pdf-units.
   - Lee Fig 5 (bottom): x decades 421.22/483.21/545.20 pdf-units =
     1e-5/1e-4/1e-3 m; y decades evenly from 434.72 (1e6) to 585.48 (1e-3).
3. Identify the curve. Lee 2020 paints the *newly excluded* region as a
   green (0,1,0) fill, with the previously-excluded region painted over
   it in yellow -- so the green polygon's lower-left vertex chain IS the
   95% limit curve (47 vertices, author precision).
4. Invert the log-log axis transform -> (lambda_m, alpha) CSV.
5. **Anchor validation (mandatory, data-gate protocol):** the extracted
   curve must reproduce the abstract-verified point. Result: alpha = 1
   crossing at 38.61 um vs abstract 38.6 um -- 0.03% deviation. PASS.

Provenance grade for the CSV: `VECTOR_EXTRACTED_FROM_ARXIV_PDF`
(author-coordinate precision; strictly better than manual digitization,
which remains the fallback if a figure turns out to be raster).

## Results of record (Lee 2020, 95% CL)

| coupling | excluded for |
|---|---|
| \|alpha\| = 1 | lambda >= **38.61 um** (validates against abstract 38.6) |
| alpha = +1/3 (scalaron, G20) | lambda >= **54.05 um** |

Program consequences:
- The G20 scalaron cap (had E3 not killed the route): ell* < 54.0 um.
- The **P7' null test** margin is now precise: VED-with-P7' predicts no
  Yukawa; the strongest current probe at gravitational strength reaches
  54 um at alpha = 1/3.
- The UFFT squeeze (29.9 um < a_disc < 38.6 um) can now be re-read with
  the full curve instead of the single |alpha| = 1 anchor.

## Reproduce / extend

```bash
cd src_exp
PYTHONPATH=. python dataexp/tools/extract_lee2020_fig5.py
# downloads the arXiv PDF if absent, writes
# .data/alpha_lambda/lee2020_alpha_lambda_95cl.csv, validates the anchor,
# prints the alpha = 1 and alpha = 1/3 crossings.
```

To extend to Tan 2020 (or any other curve):
1. Download the arXiv PDF into `.data/alpha_lambda/`.
2. `page.get_images()` -- if empty, it's vector: proceed; if raster,
   fall back to manual digitization (instructions in
   `short_range_gravity.py`).
3. Find the exclusion figure page; dump drawings; locate frame + ticks;
   calibrate; identify the limit curve (fills are easiest; otherwise
   cluster strokes by color/width and pick the family that passes
   through the abstract anchor).
4. ALWAYS validate against the paper's abstract-verified anchor before
   trusting the CSV; reject on > 2% deviation.

## Open items

- Tan 2020 (PRL 124, 051301): **no arXiv preprint exists** (searched
  2026-06-12: only paywalled APS/PubMed/ResearchGate versions). Options:
  (a) email the HUST authors for the curve table, (b) obtain the
  published PDF via institutional access and run the same vector
  recipe (anchor: |alpha| = 1 at 48 um), (c) leave Lee 2020 as the
  binding curve -- it is the stronger limit at the 38-55 um window the
  program cares about.
- Wire the generated CSV into `short_range_gravity.py` as a proper
  Dataset (replacing the ManualFile placeholder for Lee 2020), with the
  anchor validation as the dataset's integrity check.
- If official machine-readable tables ever surface (Eot-Wash contact,
  APS supplemental), supersede the extraction and record the swap.
