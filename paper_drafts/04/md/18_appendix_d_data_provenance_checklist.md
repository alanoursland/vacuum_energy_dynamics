# Appendix D. Data Provenance Checklist

For every empirical number used in a gate, record:

- source paper or dataset;
- exact location in source;
- provenance grade;
- extraction or verification method;
- independent anchor if extracted;
- uncertainty or tolerance;
- access date;
- script path if machine-extracted;
- whether author-provided data supersede the value;
- whether the value is used for fitting or only as a kill condition.

Forbidden:

```text
FROM_MEMORY values in empirical confrontations.
Unvalidated plot read-offs as physics-grade data.
Silent replacement of extracted data with later official data.
```
