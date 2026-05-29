# Vacuum Action Origin 8: Local Additivity to Gradient Strain

## Purpose

This report validates how local additive energy can contain neighboring-cell
coupling without becoming action-at-a-distance.

The gate is:

```text
local nearest-neighbor edge costs
  -> discrete Laplacian variation
  -> continuum gradient strain.
```

## Validated Checks

- interior variation q1: passed
- interior variation q2: passed
- variation q1 is negative discrete Laplacian times Kh: passed
- continuum gradient density leading term: passed
- edge density Taylor series through h^2: passed
- edge strain invariant under uniform shift: passed

## Discrete Edge Energy

Use:

```text
E = K/(2h) sum_i (q_(i+1)-q_i)^2.
```

SymPy verifies that the interior variation is:

```text
partial E / partial q_i
  = K/h (2q_i - q_(i-1) - q_(i+1))
  = -K h Delta_discrete q_i.
```

## Continuum Limit

With:

```text
q(x+h)-q(x)
  = h q' + h^2 q''/2 + h^3 q'''/6 + ...
```

the edge energy per length satisfies:

```text
lim_{h->0} [K/(2h)(q(x+h)-q(x))^2]/h
  = K(q')^2/2.
```

## Interpretation

Strict cell-local potential energy gives algebraic equations. Local additive
edge strain gives differential equations. This is the action-origin bridge from
finite-cell vacuum response to continuum gradient energy.
