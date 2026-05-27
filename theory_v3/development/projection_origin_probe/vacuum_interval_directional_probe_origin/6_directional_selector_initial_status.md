# Vacuum Interval Directional Probe Origin 6: Initial Status

## Purpose

This report summarizes the first selector-level proof batch for directional
interval data.

## Proofs Completed

Proof `1` validates polarization:

```text
(Q(u+v)-Q(u)-Q(v))/2 = u^T H v.
```

Proof `2` validates finite reconstruction in 3D:

```text
Q(e_i), Q(e_i+e_j) recover all h_ij.
```

Proof `3` validates the trace limitation:

```text
dim(trace-blind symmetric sector in 3D) = 5.
```

Proof `4` validates null-cone scale ambiguity:

```text
Q = 0 and cQ = 0 have the same null set.
```

Proof `5` validates boundary induced metric projection:

```text
h = E^T G E.
```

## Current Result

The directional interval selector is mathematically viable:

```text
local interval comparisons
  -> quadratic form Q(v)
  -> symmetric bilinear tensor by polarization
  -> induced boundary metric from tangent probes.
```

This supplies exactly the type of data the scalar projection ladder lacks.

## Remaining Gap

This batch proves the algebraic selector, not its physical origin.

The next proofs should ask whether the vacuum ontology supplies:

```text
1. enough independent local direction probes;
2. an interval scale, not just null-cone order;
3. tangent-vs-normal boundary splitting;
4. transformation behavior under local frame changes;
5. a source/action coupling that uses h_ab rather than only tr(h).
```

If those close, this folder can hand back to the action-origin chain with a
candidate origin for tensor boundary data.
