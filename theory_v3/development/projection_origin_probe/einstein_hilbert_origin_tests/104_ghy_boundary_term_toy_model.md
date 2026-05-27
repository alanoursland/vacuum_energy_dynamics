# Einstein-Hilbert Origin Test 104: GHY Boundary Term Toy Model

## Purpose

This report validates a one-dimensional toy model for the role played by a
Gibbons-Hawking-York-like boundary term.

## Validated Checks

- second-derivative action converts to first-derivative strain action: passed
- second-derivative variation has eta-prime boundary term: passed
- boundary-corrected variation removes eta-prime boundary term: passed
- added boundary term supplies missing variation: passed

## Toy Split

The second-derivative density:

```text
-q q''
```

becomes a first-derivative strain density after adding a boundary divergence:

```text
-q q'' + d(q q')/dx = (q')^2.
```

## Variation

The second-derivative action variation contains a boundary term involving
`eta'`:

```text
delta(-q q'')
  =
  -2q'' eta
  + d(q' eta - q eta')/dx.
```

The boundary-corrected first-derivative action has:

```text
delta((q')^2)
  =
  -2q'' eta
  + d(2q' eta)/dx.
```

The `eta'` boundary variation has been removed.

## Interpretation

This toy model mirrors the Einstein-Hilbert/GHY issue: curvature actions contain
second derivatives, and a boundary term is needed for a well-posed fixed-metric
variation.
