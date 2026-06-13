# 2. Static Frame Indifference

Consider a static spherically symmetric exterior written in areal-radius gauge:

```text
ds^2 = -A(r)c^2 dt^2 + B(r) dr^2 + r^2 dOmega^2 .
```

Areal radius fixes the radial coordinate by the area of the symmetry spheres.
After this choice, the condition

```text
A(r) B(r) = 1
```

is not a disposable coordinate convention. It is a restriction on the static
vacuum response.

We interpret this condition as the metric shadow of static frame indifference:
a strictly static vacuum exterior should carry no energy current and no
intrinsic preferred frame in the temporal-radial plane. In such an exterior,
temporal and radial distortions are compensated rather than independently
distorted.

The principle is satisfied by the Schwarzschild family:

```text
A(r) = 1 - 2GM/(c^2 r),
B(r) = A(r)^(-1).
```

It is also satisfied by Schwarzschild-de Sitter in the corresponding static
patch:

```text
A(r) = 1 - 2GM/(c^2 r) - Lambda r^2/3,
B(r) = A(r)^(-1).
```

The principle is stronger than ordinary spherical symmetry and staticity. A
static spherical metric can have `AB != 1`. The selection claim of this paper
is that healthy local `R^2` scalar hair necessarily produces such a metric,
and is therefore forbidden if static frame indifference is imposed exactly.
