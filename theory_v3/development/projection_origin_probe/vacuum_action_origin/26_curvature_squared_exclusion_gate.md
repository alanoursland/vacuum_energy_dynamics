# Vacuum Action Origin 26: Curvature-Squared Exclusion Gate

## Purpose

This report validates why generic curvature-squared candidates fail the
second-order vacuum-action gate.

## Validated Checks

- conformal R squared fourth-derivative coefficient: passed
- conformal R squared variation contains fourth derivative: passed
- R squared trace operator degree: passed
- Ricci squared TT operator degree: passed
- EH linear operator degree: passed
- curvature squared is two derivative orders higher: passed

## Conformal R Squared Test

In a four-dimensional one-coordinate conformal sector:

```text
R = -6 exp(-2s)[s'' + (s')^2]
sqrt(g) = exp(4s).
```

Therefore:

```text
sqrt(g) R^2 = 36[s'' + (s')^2]^2.
```

SymPy verifies that its Euler-Lagrange equation contains `s''''` with
coefficient:

```text
72.
```

## Momentum-Order Test

Linear curvature carries two derivatives:

```text
R_linear ~ k^2 h.
```

Curvature-squared variation adds two more:

```text
R^2 operator      ~ k^4 h
Ricci^2 operator  ~ k^4 h.
```

The EH linear operator is:

```text
EH operator ~ k^2 h.
```

## Interpretation

If the vacuum-action origin gates require local second-order metric equations,
generic `R^2` and `R_ab R^ab` terms are excluded. This is the action-origin
version of the Lovelock derivative-order gate.
