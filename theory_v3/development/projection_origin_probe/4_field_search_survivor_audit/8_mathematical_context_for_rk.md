# Field Search Survivor Audit 8: Mathematical Context for r_k

## Purpose

This report records the mathematical context around:

```text
r_k = (2k - 1)/(2k + 3)
```

and the row family:

```text
psi_k(x) = x^(2k) - r_k x^(2k-2).
```

It separates accurate external analogies from overstrong interpretations.

## Validated Checks

- beta ratio r_(k,m): passed
- Pearson equation for auxiliary Gegenbauer weight a^2: passed
- L as Pearson divergence operator: passed
- primitive identity for observed ratio: passed

## Accuracy Assessment

### Not A Classical Orthogonal Polynomial Sequence

In the variable:

```text
y = x^2,
```

the rows become:

```text
psi_k(y) = y^k - r_k y^(k-1).
```

This is a two-term row family spanning a codimension-one moment kernel. It is
not a classical Jacobi/Gegenbauer/orthogonal polynomial sequence. Classical
orthogonal polynomial families live in the Jacobi/Laguerre/Hermite framework
and have their own recurrence/differential-equation structure; this family is
better understood as a recombined basis adapted to a constraint.

The useful analogy is spectral Galerkin basis recombination: linear
combinations of known simple basis functions are chosen so each basis element
automatically satisfies a constraint. Here the constraint is a moment/contact
condition rather than a standard Dirichlet or Neumann boundary condition.

### Pearson/Gegenbauer Operator Context

The operator:

```text
L[f] = (1-x^2)f' - 6xf
```

has a precise classical fingerprint. Let:

```text
sigma = 1-x^2
rho = (1-x^2)^2.
```

Then:

```text
(sigma rho)' / rho = -6x.
```

Therefore:

```text
L[f] = (1/rho) d/dx [sigma rho f].
```

This is the Pearson/divergence operator for the auxiliary Gegenbauer weight
`rho=a^2`, corresponding to Gegenbauer parameter `lambda=5/2`.

Important distinction:

```text
rho = a^2  is the auxiliary Pearson weight;
w   = a^4  is the projection/energy weight.
```

They are related in the construction, but they are not the same object.

### Transform u=a^3f

The transform:

```text
u = a^3 f
```

is a classical-looking dependent-variable conjugation:

```text
L[f] = u'/a^2
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

It is fair to call this Liouville-type or Sturm-Liouville-normal-form
behavior. It is more precise to describe it as an exact gauge/conjugation
transform in this problem, because no independent-variable change is being
used here.

### Moment Kernel And Fredholm Language

The identity:

```text
span{psi_1,...,psi_N}
  =
ker[S -> integral_0^1 aS dx]
```

is exact on finite even-polynomial coefficient spaces.

This is Fredholm-like only after an additional zero-flux/contact condition is
imposed. For the base mixed-boundary problem:

```text
-u'' = F
u'(0)=0
u(1)=0,
```

there is no Fredholm solvability obstruction for arbitrary `F`. The condition:

```text
integral_0^1 F dx = 0
```

instead enforces:

```text
u'(1)=0,
```

which is the zero-boundary-flux/contact admissibility condition used by the
projection chain.

So the safest language is:

```text
moment-kernel compatibility condition
endpoint-contact admissibility condition
Fredholm-like if promoted to an overdetermined/zero-flux boundary problem
```

not:

```text
ordinary existence condition for the base Green problem.
```

### Beta Function Origin

The general ratio is:

```text
r_(k,m) = (2k - 1)/(2k + 2m - 1).
```

It is exactly the beta-moment ratio:

```text
B(k+1/2,m) / B(k-1/2,m)
  =
  (k-1/2)/(k+m-1/2)
  =
  (2k-1)/(2k+2m-1).
```

The observed case:

```text
r_k = (2k - 1)/(2k + 3)
```

is the `m=2` case.

Important distinction:

```text
This beta ratio uses the auxiliary/contact weight a^(m-1).
It is not the same-weight moment ratio for the projection weight a^4.
```

For example, the direct same-weight ratio under `a^4` would be:

```text
B(k+1/2,5) / B(k-1/2,5)
  =
  (2k-1)/(2k+9),
```

not `(2k-1)/(2k+3)`.

So the accurate history is:

```text
Group 88 discovered r_k through the archived moment-hierarchy identity.
The primitive/beta identity later explained the same survivor ratio as the
m=2 auxiliary endpoint-contact case.
The ratio is not the ordinary same-weight projection ratio for w=a^4.
```

## Best Description

The best concise description is:

```text
psi_k is a beta-moment-kernel row basis adapted to the endpoint-contact
admissibility condition produced by the Pearson/Gegenbauer divergence operator
L[f]=(1/rho)d/dx[sigma rho f], with rho=(1-x^2)^2.
```

Less compressed:

```text
It is not a named classical OPS.
It is a designer Galerkin/moment row basis.
Its ratio is a beta-function moment ratio.
Its operator is a Pearson/Gegenbauer divergence operator.
Its transformed equation is a Liouville-type conjugation to -u''=aS.
Its admissibility condition is a moment-kernel / endpoint-flux condition.
```

## Reference Pointers

Useful external neighborhoods:

```text
DLMF Chapter 18: classical Jacobi/Gegenbauer orthogonal polynomials.
  https://dlmf.nist.gov/18
  https://dlmf.nist.gov/18.3
  https://dlmf.nist.gov/18.8

Shen/Galerkin basis recombination: basis functions chosen to satisfy boundary constraints.
  https://shenfun.readthedocs.io/en/latest/introduction.html

Sturm-Liouville/Liouville transforms: normal-form transformations of second-order operators.
Fredholm alternative: compatibility conditions from adjoint nullspaces, when the boundary problem has such a solvability obstruction.
```
