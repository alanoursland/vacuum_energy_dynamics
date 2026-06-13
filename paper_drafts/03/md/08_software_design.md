# 8. Software Design

A reusable tool should separate PDF mechanics from scientific validation. The
single-figure Lee extraction script proves the method, but a paper-quality
software release should expose a small set of composable operations:

- inspect a PDF page for images, drawings, colors, bounding boxes, and path
  counts;
- select candidate paths by geometry and style;
- identify frames and tick marks;
- fit linear or logarithmic axis calibrations;
- transform path coordinates into data coordinates;
- validate transformed data against anchors;
- export CSV plus provenance metadata.

The command-line interface should support an inspection mode before extraction.
For example:

```text
pdfvec inspect source.pdf --page 4
pdfvec dump-paths source.pdf --page 4 --bbox plot
pdfvec extract config.yaml
pdfvec validate extraction.json
```

The Python API should be configuration-driven enough to reproduce an
extraction without manual state:

```text
page -> drawings -> candidates -> calibration -> curve -> validation -> export
```

Tests should cover coordinate transforms and refusal behavior. The most
important tests are not visual. They are numerical:

- affine calibration from two ticks;
- log calibration from decade ticks;
- minor-tick residual checks;
- PDF y-axis inversion;
- interpolation of a crossing on a log-log curve;
- refusal when an anchor misses tolerance.

If the target venue is JOSS, the software release needs documentation,
examples, continuous integration, a DOI archive, and a clear statement of
scope. If the target is an arXiv methods note, a smaller but fully
reproducible script release may be sufficient.
