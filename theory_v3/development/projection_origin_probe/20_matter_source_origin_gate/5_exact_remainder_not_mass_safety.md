# Matter Source Origin Gate 5: Exact Remainder Is Not Mass Safety

## Purpose

This proof records an archive lesson that matters for source origin:

```text
flat exactness is not the same as physical source neutrality.
```

An exact derivative can have zero total integral while still having nonzero
local value and nonzero weighted/geometric moments.

## Validated Checks

- rho=dJ/dy with endpoint-vanishing J has zero flat integral: passed
- flat exactness does not imply local inertness: passed
- flat exactness does not imply weighted neutrality: passed
- flat exactness does not imply geometric-window neutrality: passed

## Setup

Use the reduced exactness witness:

```text
Xi = (1-y^2)^3
window = (1-y^2)^2
J = window * Xi'
rho = J'.
```

Because `J` vanishes at both endpoints:

```text
integral_-1^1 rho dy = J(1)-J(-1) = 0.
```

SymPy verifies the flat charge vanishes.

## Failure Of Local Inertness

At the origin:

```text
rho(0) = -6.
```

So exactness does not mean pointwise silence.

## Failure Of Weighted Neutrality

Weighted witnesses are nonzero:

```text
integral_-1^1 y^2 rho dy = 1024/1155
integral_-1^1 (1-y^2) rho dy = -1024/1155
```

## Gate Interpretation

An exact residual can be algebraically useful without being a safe matter
source or a safe neutral correction. To promote such an object, the theory
must prove the relevant weighted, boundary, and far-zone neutrality conditions,
not just flat exactness.
