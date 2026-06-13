# 2. What Is Inside a Vector PDF Figure

A PDF page may contain raster images, text objects, and vector drawing
commands. Vector figures produced by plotting software commonly encode curves
as paths made of line segments or Bezier segments, with stroke color, fill
color, line width, clipping regions, and transformation matrices attached.
Libraries such as PyMuPDF expose these objects through APIs such as
`page.get_drawings()`.

This is different from extracting a screenshot. In a raster image, a curve is a
set of colored pixels. In a vector figure, the curve may be a path whose
coordinates were generated directly by the plotting program. The PDF coordinate
system is not the physical data coordinate system, but the relationship between
them is often recoverable from the plotted frame and tick marks.

Several common plotting conventions make vector extraction useful:

- line plots often appear as stroked paths;
- confidence regions and exclusion regions often appear as filled polygons;
- filled polygons frequently contain the limiting curve as one boundary of the
  polygon;
- major and minor tick marks are short vector segments with regular geometry;
- log-axis decades appear with equal spacing in PDF coordinates after the
  plotting transform.

Post-processing can complicate the situation. A figure may have been edited in
Illustrator, Inkscape, or journal production software. Curves may be converted
to outlines, clipped, merged, simplified, or recolored. The method therefore
does not assume that every PDF drawing path is meaningful data. It treats vector
paths as candidate evidence that must be calibrated and externally validated.

The key practical distinction is whether the figure page is vector-rich or
raster-only. Raster-only figures should be handled by ordinary digitization
methods. Vector-rich figures can be inspected path by path.
