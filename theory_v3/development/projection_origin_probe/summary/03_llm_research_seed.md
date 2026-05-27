# Compact LLM Research Seed

You are continuing a mathematical research thread. Treat this as a distilled formal packet, not as a full proof corpus. Use the source breadcrumbs only to locate the original files if needed.

## Problem

A weighted projection hierarchy survived earlier filtering. The task is to continue the math without overinterpreting it physically.

Core objects:

```text
a = 1 - x^2
w = a^4
phi_j(x)=x^(2j)
A[k,j]=2 integral_0^1 psi_k(x) phi_j(x) a^4 dx
```

with:

```text
psi_k(x)
=
x^(2k)-((2k-1)/(2k+3))x^(2k-2).
```

The current best formal label is:

```text
regularity-adapted weighted projection/admissibility hierarchy
```

not field equation or source law.

## Established spine

### 1. `psi_k` has an IBP primitive

```text
G_k(x)=x^(2k-1)a^2
```

and:

```text
G_k'(x)=-(2k+3)a psi_k(x).
```

So:

```text
psi_k(x)
=
-1/((2k+3)a) d/dx[x^(2k-1)a^2].
```

This derives the ratio:

```text
(2k-1)/(2k+3).
```

Same-weight `a^4` orthogonality would instead give:

```text
(2k-1)/(2k+9),
```

so `psi_k` is not the direct same-weight orthogonal row.

### 2. Projection rows pull back through `L`

For regular endpoint behavior:

```text
<psi_k,f>_w
=
1/(2k+3)<x^(2k-1),L[f]>_w
```

where:

```text
L[f]=af'-6xf=a^(-2)d(a^3f)/dx.
```

Boundary term:

```text
[f x^(2k-1)a^5]_0^1.
```

### 3. Weighted adjoint

Under `w=a^4`:

```text
L_w^*[g]=-ag'+4xg
```

and:

```text
<Lf,g>_w=[a^5fg]_0^1+<f,L_w^*g>_w.
```

Second-order candidate:

```text
L_w^*L[f]
=
-a^2f''+12xaf'+(6-30x^2)f.
```

Reverse composition:

```text
LL_w^*[g]
=
-a^2g''+12xag'+(4-28x^2)g.
```

### 4. Primitive-power family

For:

```text
G_(k,m)=x^(2k-1)a^m
```

one obtains:

```text
psi_(k,m)
=
x^(2k)-((2k-1)/(2k+2m-1))x^(2k-2)
```

and:

```text
L_m[f]=af'-2(5-m)xf.
```

The observed hierarchy is `m=2`.

Family adjoint relation:

```text
L_m^*=-L_(5-m).
```

Boundary cleanliness is family-wide and does not select `m=2`.

### 5. `u=a^3f` transform

Candidate energy:

```text
E[f]=1/2<Lf,Lf>_w-<S,f>_w.
```

Set:

```text
u=a^3f.
```

Then:

```text
L[f]=a^(-2)u'
(L[f])^2w=(u')^2
Sfw=aSu.
```

So:

```text
E[u]=1/2 integral_0^1 (u')^2 dx - integral_0^1 aS u dx
```

with Euler-Lagrange equation:

```text
-u''=aS.
```

This is an algebraic simplification, not a physical derivation of `E`.

### 6. Green domain and regularity

For:

```text
-u''=F
u'(0)=0
u(1)=0
```

Green kernel:

```text
G(x,y)=1-max(x,y).
```

For the energy transform:

```text
F=aS.
```

Endpoint identities:

```text
u'(1)=-integral_0^1 F dx
u''(1)=-F(1)
u'''(1)=-F'(1)
u''''(1)=-F''(1)
```

Regularity of:

```text
f=u/a^3
```

at `x=1` gives:

```text
R=0 bounded/non-contact level:
  integral_0^1 aS dx = 0

R=1 contact level:
  integral_0^1 aS dx = 0
  S(1)=0

R contact level:
  integral_0^1 aS dx = 0
  S vanishes to order R at x=1.
```

The first admissibility condition is:

```text
C0[S]=integral_0^1 aS dx=0.
```

Positive monomial source probes fail it. Signed balanced sources can pass it.

### 7. Balanced sources

First-level balanced basis:

```text
B_q(x)=x^(2q)-c_q
c_q=3/((2q+1)(2q+3)).
```

Then:

```text
integral_0^1 aB_q dx=0.
```

Regularity-level `R` balanced basis:

```text
B_(R,q)(x)=a^R[x^(2q)-c_(R,q)]
```

with:

```text
c_(R,q)
=
integral x^(2q)a^(R+1)dx / integral a^(R+1)dx.
```

In `y=x^2`:

```text
B_(R,q)(y)=(1-y)^R(y^q-c_(R,q))
c_(R,q)=B(q+1/2,R+2)/B(1/2,R+2)
       =(1/2)_q/(R+5/2)_q.
```

Projection signatures:

```text
P_R[k,q]=integral_0^1 psi_k B_(R,q)a^4 dx
```

have full finite-rank evidence and factor as raw projection composed with the balancing transform.

### 8. `y=x^2` kernel bridge

In `y`:

```text
psi_k(y)=y^k-((2k-1)/(2k+3))y^(k-1).
```

The span of `psi_1,...,psi_N` has codimension one in polynomials of degree `<=N`.

Missing coefficient vector:

```text
m_j=3/((2j+1)(2j+3)).
```

The first admissibility functional has coefficients proportional to:

```text
integral_0^1 a x^(2j)dx
=
2/((2j+1)(2j+3)).
```

Thus:

```text
span{psi_1,...,psi_N}
=
ker[S -> integral_0^1 aS dx]
```

on finite even-polynomial coefficient spaces.

This is the strongest bridge result.

### 9. Generalized regularity rows

For endpoint-contact level `R`, define:

```text
C_R[P]=integral_0^1 P(y)(1-y)^(R+1)y^(-1/2)dy.
```

The adapted row family is:

```text
chi_(R,k)(y)
=
y^k-((2k-1)/(2k+2R+3))y^(k-1).
```

Then:

```text
span{chi_(R,1),...,chi_(R,N)}=ker C_R
```

on degree `<=N`.

Proof mechanism:

```text
C_R[y^k]/C_R[y^(k-1)]
=
(2k-1)/(2k+2R+3).
```

Original rows:

```text
psi_k=chi_(0,k).
```

Primitive power relates to regularity by:

```text
m=R+2.
```

Thus observed `m=2` corresponds to `R=0`, the bounded/non-contact admissibility problem for `f=u/a^3`.

## Guardrails

Do not claim:

```text
A is the stiffness matrix K=<Lphi_i,Lphi_j>_w.
```

It is not. `A=2<psi_k,phi_j>_w` is a once-integrated projection/pullback matrix.

Do not claim the rows are direct Gegenbauer/Jacobi polynomials. The Jacobi setting is contextual.

Do not claim compactified radial measure derives `w=a^4`. For `r=x/a^c`, radial measure gives `a^(-cn-1)` for positive `c,n`.

Do not claim physical meanings for `x`, `f`, `S`, `w`, `E`, or the boundary domain without deriving them.

## Best current theorem-sized next tasks

### Task A: General cross-Gram invertibility

Try to prove invertibility of:

```text
G_R[k,q]
=
1/2 integral_0^1
chi_(R,k)(y)(y^q-c_(R,q))(1-y)^(R+4)y^(-1/2)dy
```

for all finite `N`, or identify the precise obstruction.

Known structure:

```text
chi_(R,k) span ker C_R
balanced rows y^q-c_(R,q) span ker C_R
inner product weight is positive on (0,1)
```

Need check whether the cross-weight `(1-y)^(R+4)y^(-1/2)` preserves the needed nondegeneracy between the two kernel bases.

### Task B: Operator-domain regularity theorem

Formalize:

```text
-u''=aS, u'(0)=0, u(1)=0, f=u/a^3.
```

Prove exact conditions for `f in C^R` at `x=1`.

### Task C: Determine whether the energy/domain can be externally derived

This is not algebraic cleanup. It needs a concrete object:

```text
physical/geometric meaning of x
measure deriving w=a^4
variational principle deriving E[f]
boundary/domain derivation
source-pairing derivation
reason R=0 boundedness is selected
```

Without one of these, stop at formal/admissibility status.

