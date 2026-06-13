# 7. Comparison With Pixel Digitization

Pixel digitization and vector extraction solve related but distinct problems.
Pixel digitization starts from an image. Vector extraction starts from the PDF
drawing instructions, when those instructions exist.

| method | input | dominant error source | validation mode |
|---|---|---|---|
| pixel digitization | rasterized figure | resolution, antialiasing, manual clicks, line width | visual agreement plus optional anchors |
| vector extraction | PDF paths | path selection, clipping, post-processing, coordinate calibration | mandatory anchor validation |
| author table | machine-readable data | transcription/versioning if any | source provenance |

Vector extraction can be more precise than pixel digitization because it avoids
the rasterization step. It does not follow that vector extraction is always
more reliable. A vector path may be a legend sample, a clipping boundary, a
filled outline, a smoothed approximation, or an edited object. Pixel
digitization at least forces the user to digitize the visual object that a
reader sees. Vector extraction must prove that the selected path corresponds to
the scientific curve.

The fair comparison is therefore not "vector is always better." The fair claim
is:

```text
When a plotted curve is present as an identifiable vector path, and when an
independent anchor validates the coordinate transform and path identity, vector
extraction can recover the plotted curve at plotting precision and with better
reproducibility than manual pixel digitization.
```

In the Lee et al. case, the anchor check provides a concrete precision test.
The method recovers the text-stated `38.6 um` crossing as `38.61 um`. A pixel
digitization comparison should be added in the final paper by rasterizing the
same figure at several resolutions and repeating the crossing estimate.
