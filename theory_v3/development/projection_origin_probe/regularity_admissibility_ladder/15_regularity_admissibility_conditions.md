# Synthesis Proof 15: Regularity and Admissibility Conditions

## Purpose

This report turns the regularity issue for:

```text
f = u/a^3
```

into explicit conditions on the transformed forcing:

```text
-u'' = F
u'(0)=0
u(1)=0.
```

For the energy transform, `F=aS`.

## Validated Checks

- Green solution satisfies ODE and base boundary conditions: passed
- endpoint derivative identities through fourth derivative: passed
- u/a^3 boundedness threshold is order >=3 at x=1: passed
- bounded f admissibility conditions derived: passed
- positive source-family fails moment cancellation but satisfies F(1)=0: passed
- example signed forcing satisfies bounded-f admissibility: passed

## Endpoint Derivative Identities

For the Green solution with `u'(0)=0`, `u(1)=0`:

```text
u'(1)  = - integral_0^1 F dx
u''(1) = -F(1)
u'''(1) = -F'(1)
u''''(1) = -F''(1)
```

These identities were verified for a generic degree-7 polynomial forcing.

## Boundedness of `f = u/a^3`

Since:

```text
a = 1 - x^2 = (1-x)(1+x),
```

and `1+x` is nonzero at `x=1`, boundedness of:

```text
f = u/a^3
```

requires `u` to vanish to order at least 3 at `x=1`.

With `u(1)=0` already imposed, this means:

```text
u'(1)=0
u''(1)=0.
```

Using the derivative identities, boundedness of `f` requires:

```text
integral_0^1 F dx = 0
F(1) = 0.
```

For the original source variable, `F=aS`, this becomes:

```text
integral_0^1 aS dx = 0
(aS)(1) = 0.
```

The second condition is automatic for regular `S` because `a(1)=0`. The first
condition is a genuine global cancellation condition.

## Model Boundedness Table

```text
u=(1-x)^0: order=0, bounded u/a^3? False, quotient=-1/((x - 1)**3*(x + 1)**3)
u=(1-x)^1: order=1, bounded u/a^3? False, quotient=1/((x - 1)**2*(x + 1)**3)
u=(1-x)^2: order=2, bounded u/a^3? False, quotient=-1/((x - 1)*(x + 1)**3)
u=(1-x)^3: order=3, bounded u/a^3? True, quotient=(x + 1)**(-3)
u=(1-x)^4: order=4, bounded u/a^3? True, quotient=-(x - 1)/(x + 1)**3
u=(1-x)^5: order=5, bounded u/a^3? True, quotient=(x - 1)**2/(x + 1)**3
u=(1-x)^6: order=6, bounded u/a^3? True, quotient=-(x - 1)**3/(x + 1)**3
```

## Positive Source-Family Obstruction

For:

```text
S_(p,q) = x^(2q)a^p
F_(p,q) = aS_(p,q) = x^(2q)a^(p+1),
```

the endpoint condition `F(1)=0` holds, but the global cancellation condition
fails:

```text
integral_0^1 F_(p,q) dx > 0.
```

Exact checked moments:

```text
P=0, Q=0: int F=2/3, F(1)=0
P=0, Q=1: int F=2/15, F(1)=0
P=0, Q=2: int F=2/35, F(1)=0
P=0, Q=3: int F=2/63, F(1)=0
P=0, Q=4: int F=2/99, F(1)=0
P=0, Q=5: int F=2/143, F(1)=0
P=1, Q=0: int F=8/15, F(1)=0
P=1, Q=1: int F=8/105, F(1)=0
P=1, Q=2: int F=8/315, F(1)=0
P=1, Q=3: int F=8/693, F(1)=0
P=1, Q=4: int F=8/1287, F(1)=0
P=1, Q=5: int F=8/2145, F(1)=0
P=2, Q=0: int F=16/35, F(1)=0
P=2, Q=1: int F=16/315, F(1)=0
P=2, Q=2: int F=16/1155, F(1)=0
P=2, Q=3: int F=16/3003, F(1)=0
P=2, Q=4: int F=16/6435, F(1)=0
P=2, Q=5: int F=16/12155, F(1)=0
P=3, Q=0: int F=128/315, F(1)=0
P=3, Q=1: int F=128/3465, F(1)=0
P=3, Q=2: int F=128/15015, F(1)=0
P=3, Q=3: int F=128/45045, F(1)=0
P=3, Q=4: int F=128/109395, F(1)=0
P=3, Q=5: int F=128/230945, F(1)=0
P=4, Q=0: int F=256/693, F(1)=0
P=4, Q=1: int F=256/9009, F(1)=0
P=4, Q=2: int F=256/45045, F(1)=0
P=4, Q=3: int F=256/153153, F(1)=0
P=4, Q=4: int F=256/415701, F(1)=0
P=4, Q=5: int F=256/969969, F(1)=0
P=5, Q=0: int F=1024/3003, F(1)=0
P=5, Q=1: int F=1024/45045, F(1)=0
P=5, Q=2: int F=1024/255255, F(1)=0
P=5, Q=3: int F=1024/969969, F(1)=0
P=5, Q=4: int F=1024/2909907, F(1)=0
P=5, Q=5: int F=1024/7436429, F(1)=0
```

Thus positive source-family probes produce singular `f` under the simple
Green-domain problem.

## Signed Admissible Example

A minimal signed forcing can satisfy the cancellation:

```text
F = (1-x^2)(x^2 - 1/5).
```

It obeys:

```text
integral_0^1 F dx = 0
F(1) = 0.
```

The corresponding Green solution vanishes to order at least 3 at `x=1`, and
`f=u/a^3` is bounded there.

For this example:

```text
u(x) = (x - 1)**3*(x + 1)**3/30
f(x) = -1/30
lim_(x->1-) f(x) = -1/30
```

## Interpretation

The transformed variational problem converts regularity of `f` into explicit
admissibility conditions on `F=aS`.

The first nontrivial condition is:

```text
integral_0^1 aS dx = 0.
```

This is a concrete global cancellation requirement, not just a local boundary
condition.
