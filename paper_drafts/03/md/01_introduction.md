# 1. Introduction

Physics papers frequently publish results as figures without publishing the
underlying numerical tables. This is especially common for exclusion curves,
confidence contours, response functions, and compilation plots. The practical
consequence is familiar: later work needs a number from a plot, and the only
available route is to digitize the figure.

Pixel digitization is useful and often unavoidable. It is also limited by
rasterization resolution, antialiasing, line width, manual point selection,
axis-label reading, and the ambiguity introduced when several curves overlap.
Those limitations are not intrinsic to the published figure. Many modern
physics PDFs preserve figures as vector graphics. In such files, plotted lines,
filled regions, tick marks, and frames are encoded as geometric paths in PDF
coordinates. The data are not merely visible in the image; in many cases, the
author-generated plotting coordinates are still present in the document.

This paper develops a conservative workflow for recovering numerical data from
vector PDF figures. The workflow has four ingredients. First, extract the PDF
drawing paths. Second, identify the path that carries the plotted curve or
region boundary. Third, calibrate the plot axes from vector tick geometry.
Fourth, validate the recovered data against an external anchor value stated in
the text of the source paper. If the anchor check fails, the tool should refuse
to emit the extraction as physics-grade data.

The method is not a substitute for author-provided tables. Machine-readable
tables and official supplemental data remain the preferred source. Vector
extraction is best understood as a more reproducible and higher-precision form
of digitization for cases where the figure is the only public data product.

The main contributions are:

- a path-level extraction protocol for vector PDF figures;
- an axis-calibration method based on tick geometry, including log axes;
- a validation-or-refuse rule for scientific reuse;
- a worked short-range gravity case study;
- software design requirements for a reusable extraction package.

Figure 1 illustrates the basic observation: a plotted curve in a PDF can be
viewed as pixels, but it may also be available as a sequence of vector path
coordinates. Figure 2 summarizes the extraction pipeline.
