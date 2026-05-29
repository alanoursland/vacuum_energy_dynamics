# Quadratic Response Selector 18: Parallelogram Closure Obstruction

## Purpose

This proof gives a simple operational witness for nonmetric response: a
parallelogram built from two interval probes fails the metric closure identity.

## Computation

For

```text
Q(x,y)=x^2+y^2+eps(x^2+y^2)^2,
```

SymPy evaluates the orthogonal parallelogram residual:

```text
Q(A,B)+Q(A,-B)-2Q(A,0)-2Q(0,B) = 4*A**2*B**2*eps
```

## Interpretation

The residual vanishes in the metric branch and is nonzero for quartic response.
This makes parallelogram closure a direct diagnostic for whether directional
interval probes are metric-quadratic.
