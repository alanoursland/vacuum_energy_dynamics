# Synthesis Proof 17: Regularity Ladder and Source Classes

## Purpose

This report extends the first admissibility condition into a regularity
ladder for:

```text
f = u/a^3
```

where:

```text
-u'' = F = aS
u'(0)=0
u(1)=0.
```

## Validated Checks

- endpoint derivative identities through n=7: passed
- F=aS endpoint derivative formulas through m=6: passed
- regularity ladder conditions assembled: passed
- balanced C^R source bases verified for R=0..4 q=1..5: passed

## Endpoint Derivative Ladder

For the Green solution:

```text
u'(1) = - integral_0^1 F dx
```

and, for `n >= 2`:

```text
u^(n)(1) = -F^(n-2)(1).
```

This was checked through `n=7` for a generic polynomial forcing.

## Translating `F = aS`

For `F=aS`, the endpoint derivatives are:

```text
m=0: (aS)^(0)(1) = 0
m=1: (aS)^(1)(1) = -2*S(1)
m=2: (aS)^(2)(1) = -2*S(1) - 4*Subs(Derivative(S(x), x), x, 1)
m=3: (aS)^(3)(1) = -6*Subs(Derivative(S(x), x), x, 1) - 6*Subs(Derivative(S(x), (x, 2)), x, 1)
m=4: (aS)^(4)(1) = -12*Subs(Derivative(S(x), (x, 2)), x, 1) - 8*Subs(Derivative(S(x), (x, 3)), x, 1)
m=5: (aS)^(5)(1) = -20*Subs(Derivative(S(x), (x, 3)), x, 1) - 10*Subs(Derivative(S(x), (x, 4)), x, 1)
m=6: (aS)^(6)(1) = -30*Subs(Derivative(S(x), (x, 4)), x, 1) - 12*Subs(Derivative(S(x), (x, 5)), x, 1)
```

Since `a(1)=0`, the condition `F(1)=0` is automatic for regular `S`. Higher
endpoint conditions force vanishing derivatives of `S` at `x=1`.

## Regularity Conditions

For `f=u/a^3` to be `C^R` at `x=1`, `u` must vanish to order at least `R+3`.
With `u(1)=0` already imposed, the first conditions are:

```text
C^0 f condition: integral_0^1 aS dx = 0
C^1 f condition: integral_0^1 aS dx = 0; S(1) = 0
C^2 f condition: integral_0^1 aS dx = 0; S(1) = 0; S^(1)(1) = 0
C^3 f condition: integral_0^1 aS dx = 0; S(1) = 0; S^(1)(1) = 0; S^(2)(1) = 0
C^4 f condition: integral_0^1 aS dx = 0; S(1) = 0; S^(1)(1) = 0; S^(2)(1) = 0; S^(3)(1) = 0
C^5 f condition: integral_0^1 aS dx = 0; S(1) = 0; S^(1)(1) = 0; S^(2)(1) = 0; S^(3)(1) = 0; S^(4)(1) = 0
```

Thus boundedness requires only:

```text
integral_0^1 aS dx = 0.
```

`C^1` regularity additionally requires:

```text
S(1)=0.
```

`C^2` regularity additionally requires:

```text
S(1)=0
S'(1)=0.
```

and so on.

## Balanced Source Classes

A source basis satisfying the `C^R` ladder through order `R` is:

```text
B_(R,q)(x) = a^R [x^(2q) - c_(R,q)]
```

where:

```text
c_(R,q) =
  integral_0^1 x^(2q)a^(R+1) dx
  /
  integral_0^1 a^(R+1) dx.
```

This ensures:

```text
integral_0^1 a B_(R,q) dx = 0
```

and gives `S` the endpoint vanishing needed for `C^R` regularity.

Exact checked basis rows:

```text
R=0, q=1: c=1/5, B=(5*x**2 - 1)/5, order_1(u)=3
R=0, q=2: c=3/35, B=(35*x**4 - 3)/35, order_1(u)=3
R=0, q=3: c=1/21, B=(21*x**6 - 1)/21, order_1(u)=3
R=0, q=4: c=1/33, B=(33*x**8 - 1)/33, order_1(u)=3
R=0, q=5: c=3/143, B=(143*x**10 - 3)/143, order_1(u)=3
R=1, q=1: c=1/7, B=-(x - 1)*(x + 1)*(7*x**2 - 1)/7, order_1(u)=4
R=1, q=2: c=1/21, B=-(x - 1)*(x + 1)*(21*x**4 - 1)/21, order_1(u)=4
R=1, q=3: c=5/231, B=-(x - 1)*(x + 1)*(231*x**6 - 5)/231, order_1(u)=4
R=1, q=4: c=5/429, B=-(x - 1)*(x + 1)*(429*x**8 - 5)/429, order_1(u)=4
R=1, q=5: c=1/143, B=-(x - 1)*(x + 1)*(143*x**10 - 1)/143, order_1(u)=4
R=2, q=1: c=1/9, B=(x - 1)**2*(x + 1)**2*(3*x - 1)*(3*x + 1)/9, order_1(u)=5
R=2, q=2: c=1/33, B=(x - 1)**2*(x + 1)**2*(33*x**4 - 1)/33, order_1(u)=5
R=2, q=3: c=5/429, B=(x - 1)**2*(x + 1)**2*(429*x**6 - 5)/429, order_1(u)=5
R=2, q=4: c=7/1287, B=(x - 1)**2*(x + 1)**2*(1287*x**8 - 7)/1287, order_1(u)=5
R=2, q=5: c=7/2431, B=(x - 1)**2*(x + 1)**2*(2431*x**10 - 7)/2431, order_1(u)=5
R=3, q=1: c=1/11, B=-(x - 1)**3*(x + 1)**3*(11*x**2 - 1)/11, order_1(u)=6
R=3, q=2: c=3/143, B=-(x - 1)**3*(x + 1)**3*(143*x**4 - 3)/143, order_1(u)=6
R=3, q=3: c=1/143, B=-(x - 1)**3*(x + 1)**3*(143*x**6 - 1)/143, order_1(u)=6
R=3, q=4: c=7/2431, B=-(x - 1)**3*(x + 1)**3*(2431*x**8 - 7)/2431, order_1(u)=6
R=3, q=5: c=63/46189, B=-(x - 1)**3*(x + 1)**3*(46189*x**10 - 63)/46189, order_1(u)=6
R=4, q=1: c=1/13, B=(x - 1)**4*(x + 1)**4*(13*x**2 - 1)/13, order_1(u)=7
R=4, q=2: c=1/65, B=(x - 1)**4*(x + 1)**4*(65*x**4 - 1)/65, order_1(u)=7
R=4, q=3: c=1/221, B=(x - 1)**4*(x + 1)**4*(221*x**6 - 1)/221, order_1(u)=7
R=4, q=4: c=7/4199, B=(x - 1)**4*(x + 1)**4*(4199*x**8 - 7)/4199, order_1(u)=7
R=4, q=5: c=3/4199, B=(x - 1)**4*(x + 1)**4*(4199*x**10 - 3)/4199, order_1(u)=7
```

## Interpretation

The admissibility condition is not a single accident. It extends into a ladder:

```text
C^0 f:
  integral aS = 0

C^1 f:
  integral aS = 0 and S(1)=0

C^2 f:
  integral aS = 0 and S(1)=S'(1)=0

C^R f:
  integral aS = 0 and S vanishes to order R at x=1.
```

The balanced bases `B_(R,q)` provide explicit source classes satisfying these
conditions.
