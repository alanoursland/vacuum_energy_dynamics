# Paper 3 TODO

## Core method

- Generalize `src_exp/dataexp/tools/extract_lee2020_fig5.py` into a small
  reusable module or package.
- Add a configuration format that records source PDF, page, selected path,
  calibration ticks, anchors, tolerances, and output schema.
- Implement explicit refusal states rather than only raising ad hoc errors.
- Add tests for affine calibration, log calibration, y-axis inversion,
  crossing interpolation, and anchor-gate failure.

## Case studies

- Keep Lee 2020 as the primary validated case.
- Add at least two more successful case studies from different plotting
  toolchains.
- Add at least one refusal case and document why it fails.
- Add a pixel-digitization comparison on the Lee 2020 figure at several
  rasterization resolutions.

## Figures

- Replace schematic Figure 1 with an actual source-figure crop plus path
  overlay if publication permissions and source quality allow.
- Build Figure 3 from the real extracted CSV once the data artifact is checked
  into the intended release location.
- Add a final comparison table or figure once pixel-digitization results exist.
- Check all figure labels at journal column widths.

## Writing

- Complete literature search on vector figure extraction, chart reverse
  engineering, and document-analysis methods.
- Tighten novelty claim after the literature search.
- Add final references and BibTeX.
- Decide target venue: JOSS requires a package-quality software release; arXiv
  plus Zenodo can accept a smaller methods note.
- Add citation/provenance language reviewed against venue norms.

## Release

- Archive software and extracted data with a DOI.
- Include source scripts for all figures.
- Include extraction logs and validation outputs.
- Ensure the final paper never claims extracted paths are raw author data.
