# 3. Method

The extraction protocol is:

1. Load the PDF page and extract drawing paths.
2. Identify candidate plot objects by bounding box, color, fill/stroke type,
   line width, z-order, and geometry.
3. Identify the plot frame and tick marks.
4. Calibrate the PDF coordinate system to the plotted data coordinate system.
5. Transform candidate curve vertices into data coordinates.
6. Validate the transformed curve against an external anchor value.
7. Export data only if the validation check passes.

The method is deliberately stricter than a visual digitization workflow. A
human can often decide that a traced curve "looks right." For reusable data,
that is not enough. The extracted curve must reproduce a number that appears
outside the figure itself: for example, a crossing stated in the abstract, a
limit quoted in the text, or a tabulated point in the paper.

The extraction object should record:

- source paper and figure;
- PDF file identity;
- page number;
- path identifier or selection rule;
- coordinate transform;
- calibration ticks;
- anchor value;
- validation tolerance;
- software version;
- exported data columns.

The validation rule is a gate, not a diagnostic afterthought. A path can have
the right color and shape while still being the wrong object, a clipped
fragment, a legend sample, or a post-processed outline. If the external anchor
does not agree within the declared tolerance, the extraction should be marked
failed and the CSV should not be treated as scientific data.

The tolerance depends on the use case. In the Lee et al. case study below, a
`2%` relative tolerance is used as a conservative refusal threshold. The
observed anchor deviation is much smaller, `0.03%`.
