# 9. Provenance, Ethics, and Citation

Data recovered from a published figure remain data from the original
publication. The source paper must be cited as the origin of the scientific
result. The extraction software and derived CSV should also be cited when they
are used, but they do not replace the original citation.

Author-provided data are the gold standard. If official tables or supplemental
files are available, they should be preferred over extraction. If the extracted
curve matters to a high-stakes conclusion, the authors should be contacted for
the original data when practical.

The extracted data product should carry provenance metadata:

- source paper and figure;
- PDF source and access date;
- page number;
- path-selection method;
- axis calibration;
- validation anchor;
- validation tolerance and result;
- software version;
- known limitations.

The paper should avoid implying that vector extraction recovers raw
experimental data. It recovers plotted data from a published visual object.
That is useful, but it is downstream of the original analysis, plotting
choices, smoothing, clipping, and publication workflow.

The recommended provenance label for successful path-level extraction is
`VECTOR_EXTRACTED_FROM_ARXIV_PDF` or an equivalent explicit grade. Failed or
unvalidated attempts should not be quietly downgraded into ordinary CSV files.
They should remain logs or diagnostic artifacts.
