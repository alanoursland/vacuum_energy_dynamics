# Paper 3: Author-Precision Data Recovery from Vector Figures

**Working title:** *The Data Is Already in the PDF: Recovering
Numerical Results from Vector Graphics in Published Figures*

**Venue:** Journal of Open Source Software (if we generalize the tool
into a small package) or arXiv physics.data-an + a Zenodo software
release with DOI. Could also suit a short communication in Computing in
Science & Engineering. This is the most broadly useful and least
controversial paper on the list.

**Audience:** anyone who has ever hand-digitized a published plot —
i.e., half of phenomenology.

## The claim

Most physics figures of the last two decades are vector art: the curves
exist inside the published PDF as path coordinates written by the
authors' own plotting software. With (1) path extraction
(`PyMuPDF.get_drawings()`), (2) axis calibration from tick-mark geometry
(log-decade ticks are exactly evenly spaced — calibration to ~10⁻² of a
pdf-unit without reading a single label), and (3) mandatory validation
against a text-stated anchor value, one recovers the authors' numbers at
plotting precision — strictly better than pixel digitization
(WebPlotDigitizer et al.), with a built-in integrity check.

**Demonstrated case study:** the 95% CL Yukawa exclusion curve from
Lee et al., PRL 124, 101101 (2020), recovered as 47 author-precision
vertices from the green fill polygon of Fig. 5; the |α| = 1 crossing
reproduces the abstract's 38.6 μm to 0.03%; a new physics-grade number
(the α = 1/3 crossing at 54.05 μm) is read off a curve never published
as a table.

## What makes it publishable

- The pixel-digitization tools are ubiquitous; we have not found a
  published treatment of *path-level* extraction with tick-geometry
  calibration and anchor validation as a method. (Novelty check
  required: search "PDF vector figure data extraction" literature
  carefully; some plot-reverse-engineering work exists in the document-
  analysis community — position against it.)
- The painter's-algorithm observation (fill polygons of "newly excluded"
  regions carry limit curves directly) is a nice trick worth recording.
- Validation-or-refuse design (the tool refuses to emit data if the
  anchor check fails) is the right norm for provenance-graded reuse.

## What exists vs. what's missing

- EXISTS: working tool (`src_exp/dataexp/tools/extract_lee2020_fig5.py`),
  the method writeup (`alpha_lambda_sourcing_notes.md`), one validated
  case study.
- MISSING for JOSS: generalize from a single-figure script to a small
  package (calibrate-from-ticks + curve-pick + validate API); 2–3 more
  case studies across plotting toolchains (matplotlib, Origin, ROOT —
  each draws paths differently); tests; docs. For the arXiv+Zenodo
  route, one more case study and a cleanup would suffice.

## Risks

- Legal/ethical framing: extracting data from published figures for
  analysis is standard practice (same status as digitization); cite the
  norms, recommend citing the source paper as the data's origin, and
  note the author-request route as the gold standard.

**Effort estimate:** arXiv+Zenodo version: 1–2 sessions. JOSS version:
3–4 (packaging dominates). High value-per-effort; also the best
"calling card" paper — useful to people who will never read paper 1.
