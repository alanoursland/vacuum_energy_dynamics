# Appendix D. Reproducibility Checklist

For each extraction included in the final paper, record:

- source paper citation;
- source PDF URL or DOI landing page;
- PDF checksum if distribution permits;
- access date;
- page number;
- figure panel;
- whether the page contains raster images;
- number of drawing paths on the page;
- selected path identifier or selection rule;
- path style and bounding box;
- tick positions used for calibration;
- axis type for each axis;
- calibration residuals;
- external validation anchor;
- tolerance;
- validation result;
- output file path;
- software commit or release version.

For refused extractions, record:

- attempted source;
- reason for refusal;
- whether the problem was rasterization, ambiguous path identity, failed
  calibration, failed anchor validation, or semantic ambiguity.

The final artifact should include scripts that regenerate every figure in the
paper and every extracted CSV used in a numerical claim.
