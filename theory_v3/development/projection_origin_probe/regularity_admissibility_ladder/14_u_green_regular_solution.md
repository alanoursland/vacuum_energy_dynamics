# Synthesis Proof 14: Green Solution in the `u` Variable

## Purpose

This report solves the transformed energy equation:

```text
-u'' = aS
```

with boundary conditions:

```text
u'(0) = 0
u(1) = 0.
```

These are natural first tests: even/Neumann behavior at `x=0`, and the
minimal Dirichlet condition at the boundary `x=1`.

## Validated Checks

- Green kernel boundary and jump conditions: passed
- source-family Green solutions P,Q=0..4: passed
- endpoint derivative formulas: passed
- positive forcing moment grid P,Q=0..8: passed

## Green Kernel

For:

```text
-u'' = F
u'(0)=0
u(1)=0,
```

the Green kernel is:

```text
G(x,y) = 1 - max(x,y).
```

Equivalently,

```text
G(x,y) =
  1 - y,  x <= y
  1 - x,  x >= y.
```

Thus:

```text
u(x) = integral_0^1 G(x,y) F(y) dy
```

with:

```text
F = aS.
```

For polynomial source families this can be written without `max` as:

```text
u(x)
  = integral_x^1 (1-t)F(t)dt
    + (1-x) integral_0^x F(t)dt.
```

## Source-Family Test

For:

```text
S_(p,q) = x^(2q)(1-x^2)^p
F_(p,q) = aS_(p,q) = x^(2q)(1-x^2)^(p+1),
```

SymPy verifies the exact polynomial solutions for `P,Q=0..4`.

```text
P=0, Q=0: u(x) = (x - 1)*(x + 1)*(x**2 - 5)/12
P=0, Q=1: u(x) = (x - 1)*(x + 1)*(2*x**4 - 3*x**2 - 3)/60
P=0, Q=2: u(x) = (x - 1)*(x + 1)*(15*x**6 - 13*x**4 - 13*x**2 - 13)/840
P=0, Q=3: u(x) = (x - 1)*(x + 1)*(28*x**8 - 17*x**6 - 17*x**4 - 17*x**2 - 17)/2520
P=0, Q=4: u(x) = (x - 1)*(x + 1)*(15*x**10 - 7*x**8 - 7*x**6 - 7*x**4 - 7*x**2 - 7)/1980
P=1, Q=0: u(x) = -(x - 1)*(x + 1)*(x**4 - 4*x**2 + 11)/30
P=1, Q=1: u(x) = -(x - 1)*(x + 1)*(15*x**6 - 41*x**4 + 29*x**2 + 29)/840
P=1, Q=2: u(x) = -(x - 1)*(x + 1)*(14*x**8 - 31*x**6 + 11*x**4 + 11*x**2 + 11)/1260
P=1, Q=3: u(x) = -(x - 1)*(x + 1)*(210*x**10 - 406*x**8 + 89*x**6 + 89*x**4 + 89*x**2 + 89)/27720
P=1, Q=4: u(x) = -(x - 1)*(x + 1)*(495*x**12 - 870*x**10 + 131*x**8 + 131*x**6 + 131*x**4 + 131*x**2 + 131)/90090
P=2, Q=0: u(x) = (x - 1)*(x + 1)*(5*x**6 - 23*x**4 + 47*x**2 - 93)/280
P=2, Q=1: u(x) = (x - 1)*(x + 1)*(28*x**8 - 107*x**6 + 145*x**4 - 65*x**2 - 65)/2520
P=2, Q=2: u(x) = (x - 1)*(x + 1)*(70*x**10 - 238*x**8 + 257*x**6 - 51*x**4 - 51*x**2 - 51)/9240
P=2, Q=3: u(x) = (x - 1)*(x + 1)*(660*x**12 - 2070*x**10 + 1934*x**8 - 211*x**6 - 211*x**4 - 211*x**2 - 211)/120120
P=2, Q=4: u(x) = (x - 1)*(x + 1)*(3003*x**14 - 8877*x**12 + 7503*x**10 - 505*x**8 - 505*x**6 - 505*x**4 - 505*x**2 - 505)/720720
P=3, Q=0: u(x) = -(x - 1)*(x + 1)*(7*x**8 - 38*x**6 + 88*x**4 - 122*x**2 + 193)/630
P=3, Q=1: u(x) = -(x - 1)*(x + 1)*(105*x**10 - 511*x**8 + 974*x**6 - 874*x**4 + 281*x**2 + 281)/13860
P=3, Q=2: u(x) = -(x - 1)*(x + 1)*(165*x**12 - 745*x**10 + 1257*x**8 - 888*x**6 + 113*x**4 + 113*x**2 + 113)/30030
P=3, Q=3: u(x) = -(x - 1)*(x + 1)*(3003*x**14 - 12837*x**12 + 19923*x**10 - 12109*x**8 + 761*x**6 + 761*x**4 + 761*x**2 + 761)/720720
P=3, Q=4: u(x) = -(x - 1)*(x + 1)*(10010*x**16 - 41041*x**14 + 59939*x**12 - 32881*x**10 + 1153*x**8 + 1153*x**6 + 1153*x**4 + 1153*x**2 + 1153)/3063060
P=4, Q=0: u(x) = (x - 1)*(x + 1)*(21*x**10 - 133*x**8 + 362*x**6 - 562*x**4 + 593*x**2 - 793)/2772
P=4, Q=1: u(x) = (x - 1)*(x + 1)*(198*x**12 - 1167*x**10 + 2837*x**8 - 3598*x**6 + 2408*x**4 - 595*x**2 - 595)/36036
P=4, Q=2: u(x) = (x - 1)*(x + 1)*(3003*x**14 - 16797*x**12 + 37803*x**10 - 42277*x**8 + 22073*x**6 - 1951*x**4 - 1951*x**2 - 1951)/720720
P=4, Q=3: u(x) = (x - 1)*(x + 1)*(8008*x**16 - 43043*x**14 + 91597*x**12 - 94043*x**10 + 42093*x**8 - 1665*x**6 - 1665*x**4 - 1665*x**2 - 1665)/2450448
P=4, Q=4: u(x) = (x - 1)*(x + 1)*(306306*x**18 - 1595594*x**16 + 3254251*x**14 - 3141149*x**12 + 1267801*x**10 - 25491*x**8 - 25491*x**6 - 25491*x**4 - 25491*x**2 - 25491)/116396280
```

## Boundary Boundedness for `f = u/a^3`

Boundedness of:

```text
f = u/a^3
```

at `x=1` requires `u` to vanish to at least third order in `1-x`, equivalently
high-order vanishing in `1-x`. The minimal boundary condition `u(1)=0` is not
enough.

For the nonnegative source-family tests, the first obstruction appears at:

```text
u'(1) = - integral_0^1 F(t)dt.
```

Since `F=x^(2q)(1-x^2)^(p+1)` has positive integral for the tested family,
`u'(1)` is nonzero and negative. Therefore the resulting `f=u/a^3` is singular
at `x=1` for these positive source probes under this simple boundary problem.

```text
P=0, Q=0: u'(1)=-2/3, u''(1)=0, u'''(1)=2, u''''(1)=2, regular f? False
P=0, Q=1: u'(1)=-2/15, u''(1)=0, u'''(1)=2, u''''(1)=10, regular f? False
P=0, Q=2: u'(1)=-2/35, u''(1)=0, u'''(1)=2, u''''(1)=18, regular f? False
P=0, Q=3: u'(1)=-2/63, u''(1)=0, u'''(1)=2, u''''(1)=26, regular f? False
P=0, Q=4: u'(1)=-2/99, u''(1)=0, u'''(1)=2, u''''(1)=34, regular f? False
P=1, Q=0: u'(1)=-8/15, u''(1)=0, u'''(1)=0, u''''(1)=-8, regular f? False
P=1, Q=1: u'(1)=-8/105, u''(1)=0, u'''(1)=0, u''''(1)=-8, regular f? False
P=1, Q=2: u'(1)=-8/315, u''(1)=0, u'''(1)=0, u''''(1)=-8, regular f? False
P=1, Q=3: u'(1)=-8/693, u''(1)=0, u'''(1)=0, u''''(1)=-8, regular f? False
P=1, Q=4: u'(1)=-8/1287, u''(1)=0, u'''(1)=0, u''''(1)=-8, regular f? False
P=2, Q=0: u'(1)=-16/35, u''(1)=0, u'''(1)=0, u''''(1)=0, regular f? False
P=2, Q=1: u'(1)=-16/315, u''(1)=0, u'''(1)=0, u''''(1)=0, regular f? False
P=2, Q=2: u'(1)=-16/1155, u''(1)=0, u'''(1)=0, u''''(1)=0, regular f? False
P=2, Q=3: u'(1)=-16/3003, u''(1)=0, u'''(1)=0, u''''(1)=0, regular f? False
P=2, Q=4: u'(1)=-16/6435, u''(1)=0, u'''(1)=0, u''''(1)=0, regular f? False
P=3, Q=0: u'(1)=-128/315, u''(1)=0, u'''(1)=0, u''''(1)=0, regular f? False
P=3, Q=1: u'(1)=-128/3465, u''(1)=0, u'''(1)=0, u''''(1)=0, regular f? False
P=3, Q=2: u'(1)=-128/15015, u''(1)=0, u'''(1)=0, u''''(1)=0, regular f? False
P=3, Q=3: u'(1)=-128/45045, u''(1)=0, u'''(1)=0, u''''(1)=0, regular f? False
P=3, Q=4: u'(1)=-128/109395, u''(1)=0, u'''(1)=0, u''''(1)=0, regular f? False
P=4, Q=0: u'(1)=-256/693, u''(1)=0, u'''(1)=0, u''''(1)=0, regular f? False
P=4, Q=1: u'(1)=-256/9009, u''(1)=0, u'''(1)=0, u''''(1)=0, regular f? False
P=4, Q=2: u'(1)=-256/45045, u''(1)=0, u'''(1)=0, u''''(1)=0, regular f? False
P=4, Q=3: u'(1)=-256/153153, u''(1)=0, u'''(1)=0, u''''(1)=0, regular f? False
P=4, Q=4: u'(1)=-256/415701, u''(1)=0, u'''(1)=0, u''''(1)=0, regular f? False
```

## Interpretation

The transformed equation is explicitly solvable, but boundedness of `f` is much
stronger than the simple Dirichlet condition `u(1)=0`.

This suggests a concrete admissibility direction:

```text
bounded/contact-controlled f requires moment/endpoint cancellations in F=aS.
```

For positive source-family probes, those cancellations do not occur.
