# Appendix A. PDF Coordinates and Drawing Paths

PDF page coordinates are not data coordinates. A plotted object may be subject
to page transforms, figure transforms, clipping, and the plotting library's own
axis transform before it is written to the content stream. The extraction
workflow treats the PDF coordinates as an intermediate coordinate system.

For line segments, a path item supplies endpoints in PDF units. For Bezier
segments, the path supplies control points. The correct handling depends on the
scientific question:

- if the plotted object is a polyline, endpoints are direct samples of the
  plotted path;
- if the plotted object is a Bezier curve, the visible curve should be sampled
  from the Bezier geometry;
- if the plotted object is an outline, the centerline is not directly present.

A robust inspection step should record each path's:

- path type;
- fill and stroke colors;
- stroke width;
- bounding box;
- number of segments;
- clipping relationship if available;
- page order.

This metadata is often enough to separate axis ticks, frames, filled regions,
legend samples, and plotted curves before any data transform is applied.
