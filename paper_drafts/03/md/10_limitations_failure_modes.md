# 10. Limitations and Failure Modes

The method should refuse or downgrade extractions in several common cases.

Raster-only PDFs contain no useful vector path data for the plot. They should
be handled by conventional digitization.

Curves may be converted to outlines. In that case, the visible stroke becomes
a filled shape with two boundaries rather than a centerline. Recovering a curve
from an outline requires additional assumptions about stroke geometry.

Clipping masks can hide parts of a path. A path may extend beyond the plotted
frame, or a visible curve may be made of several clipped fragments. The export
should reflect only the validated visible boundary.

Bezier paths may encode smooth curves through control points rather than
sampled data points. The plotted curve can still be recovered, but the control
points should not be mistaken for the authors' original sample grid.

Multi-curve plots can contain many paths with similar styles. Legends,
annotations, and inset plots add additional candidates. A selection rule must
be auditable and should be supported by validation.

Axis labels can be ambiguous or absent. Tick geometry can identify spacing, but
the numerical decade assignment still needs semantic information from labels,
caption, or surrounding text.

Finally, the plotted object may not be the scientific quantity desired by a
later analysis. A published exclusion boundary may include smoothing,
interpolation, envelope-taking, or stylistic simplification. Vector extraction
recovers the plotted boundary, not necessarily the underlying statistical
construction.
