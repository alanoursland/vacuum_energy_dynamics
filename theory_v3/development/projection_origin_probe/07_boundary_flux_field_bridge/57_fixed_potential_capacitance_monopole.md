# Boundary Flux Field Bridge 57: Fixed-Potential Monopole Capacitance

## Purpose

This report validates the two-sphere monopole capacitance approximation for
fixed boundary potentials.

It is not the exact two-sphere capacitance solution. It keeps the monopole
terms only.

## Validated Checks

- monopole capacitance Q1: passed
- monopole capacitance Q2: passed
- Q1 isolated limit: passed
- Q2 isolated limit: passed
- Q1 first environmental correction: passed
- Q2 first environmental correction: passed
- fixed-potential stored energy expression: passed

## Monopole Equations

The fixed-potential approximation is:

```text
U1 = Q1/(4*pi*R1) + Q2/(4*pi*d)
U2 = Q2/(4*pi*R2) + Q1/(4*pi*d).
```

Solving gives:

```text
Q1 = 4*pi*R1*d*(U1*d - R2*U2)/(d^2 - R1*R2)
Q2 = 4*pi*R2*d*(U2*d - R1*U1)/(d^2 - R1*R2).
```

## Isolated Limit

As `d -> infinity`:

```text
Q1 -> 4*pi*R1*U1
Q2 -> 4*pi*R2*U2.
```

## Environmental Charge Shift

At large separation:

```text
Q1 = 4*pi*R1*U1 - 4*pi*R1*R2*U2/d + ...
Q2 = 4*pi*R2*U2 - 4*pi*R1*R2*U1/d + ...
```

Thus fixed-potential boundaries do not preserve fixed source strength. The
charge/flux changes with environment.

## Interpretation

This reinforces the earlier boundary-condition split:

```text
fixed flux      -> conserved mass-like source strength
fixed potential -> environment-dependent response strength
```
