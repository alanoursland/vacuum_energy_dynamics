# Einstein-Hilbert Origin Test 113: Projection Ladder to Boundary Flux Bridge

## Purpose

This report records the exact algebraic bridge from the original projection
ratio to the boundary-flux field interpretation.

## Validated Checks

- original ratio is R=0 ladder row: passed
- R=0 corresponds to primitive power m=2: passed
- L transform: passed
- Lstar L transform: passed
- weighted source equation becomes negative second derivative: passed
- zero-flux compatibility condition: passed

## Ratio Placement

The original row ratio is:

```text
r_k = (2k - 1)/(2k + 3).
```

The regularity ladder ratio is:

```text
r_(R,k) = (2k - 1)/(2k + 2R + 3).
```

SymPy verifies:

```text
R = 0 -> r_(R,k) = r_k.
```

The primitive-power relation:

```text
m = R + 2
```

therefore places the original ratio at:

```text
R = 0, m = 2.
```

## Operator Transform

With:

```text
a = 1 - x^2
u = a^3 f
L[f] = a f' - 6x f,
```

SymPy verifies:

```text
L[f] = u'/a^2.
```

Using the weighted adjoint:

```text
L*_w[g] = -a g' + 4xg,
```

SymPy verifies:

```text
L*_w L[f] = -u''/a.
```

Thus:

```text
L*_w L[f] = S
```

is equivalent to:

```text
-u'' = aS.
```

## Boundary-Flux Reading

Integrating:

```text
-u'' = aS
```

over `[0,1]` gives:

```text
integral_0^1 aS dx = -u'(1) + u'(0).
```

So the earlier admissibility condition:

```text
integral_0^1 aS dx = 0
```

is exactly the zero-boundary-flux compatibility case. Nonzero value of the same
functional is a boundary-flux defect.

## Interpretation

The original ratio is not merely a row coefficient. It is the `R=0` boundedness
member of the regularity ladder. Under the energy transform `u=a^3 f`, the same
condition becomes the compatibility condition for a one-dimensional Dirichlet
energy equation. The scalar bridge then interprets the compatibility defect as
boundary flux, and the geometric lift identifies that flux with weak-field
mass.
