# Appendix A. Static Bootstrap Details

The static exterior proof uses three ingredients.

First, the areal-flux law:

```text
Delta_areal A = (8 pi G / c^2) rho .
```

Second, P7-prime's static exterior condition:

```text
AB = 1 .
```

Third, P9's count-once self-coupling. With

```text
s = (1/2) ln(A/B),
```

the exponential identity is

```text
Delta_areal(e^s) = e^s [Delta_areal s + (s')^2] .
```

The field-energy density

```text
u_field = -c^4 (s')^2 / (8 pi G)
```

is exactly the energy needed for the nonlinear term to be counted at the
universal coupling. Solving the exterior equation with asymptotic flatness and
the Newton normalization gives

```text
A = 1 - 2GM/(c^2 r),
B = 1/A .
```

This appendix should eventually include the full family-selector calculation
from the verification scripts.
