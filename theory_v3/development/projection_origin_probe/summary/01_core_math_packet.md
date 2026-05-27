# Core Math Packet

This file keeps the mathematical spine of the projection-origin probe and regularity/admissibility ladder. It omits most discussion prose.

## 1. Notation and central projection object

Sources:

```text
overview.md
1_psi_k_ibp_origin.md
2_operator_L_origin_tests.md
regularity_admissibility_ladder/34_ladder_conclusion_report.md
```

Let:

```text
a = 1 - x^2
w = a^4 = (1 - x^2)^4
phi_j(x) = x^(2j)
```

The central projection matrix is:

```text
A[k,j] = 2 integral_0^1 psi_k(x) phi_j(x) a^4 dx.
```

The original row functions are:

```text
psi_k(x)
  = x^(2k) - ((2k - 1)/(2k + 3)) x^(2k - 2)
  = x^(2k - 2)(x^2 - r_k)
```

with:

```text
r_k = (2k - 1)/(2k + 3).
```

The sign-change point is:

```text
x_k = sqrt((2k - 1)/(2k + 3)).
```

This sign change blocks a naive positive-Gram/Hessian reading.

## 2. IBP origin of `psi_k`

Sources:

```text
1_psi_k_ibp_origin.md
conclusion.md
regularity_admissibility_ladder/5_synthesis_operator_energy.md
```

Define the boundary-vanishing primitive:

```text
G_k(x) = x^(2k - 1)a^2.
```

Core identity:

```text
d/dx [x^(2k - 1)a^2]
  = -(2k + 3)a psi_k(x).
```

Equivalently:

```text
psi_k(x)
  =
  -1 / ((2k + 3)a)
  d/dx [x^(2k - 1)a^2].
```

This derives the ratio:

```text
(2k - 1)/(2k + 3)
```

from differentiating the primitive.

Auxiliary moment identity:

```text
integral_0^1 x^(2k)a dx
/
integral_0^1 x^(2k - 2)a dx
=
(2k - 1)/(2k + 3).
```

But under the actual projection weight:

```text
integral_0^1 x^(2k)a^4 dx
/
integral_0^1 x^(2k - 2)a^4 dx
=
(2k - 1)/(2k + 9).
```

Therefore `psi_k` is not the direct same-weight orthogonal row for `w=a^4`.

## 3. Pullback operator `L`

Sources:

```text
1_psi_k_ibp_origin.md
2_operator_L_origin_tests.md
regularity_admissibility_ladder/5_synthesis_operator_energy.md
```

Start with:

```text
I_k[f] = integral_0^1 psi_k(x) f(x) a^4 dx.
```

Using the primitive identity and integrating by parts:

```text
I_k[f]
=
1/(2k + 3)
integral_0^1 x^(2k - 1) a^4 L[f](x) dx
```

provided the endpoint term vanishes. In inner-product notation:

```text
<psi_k, f>_w
=
1/(2k + 3) <x^(2k - 1), L[f]>_w.
```

The pullback operator is:

```text
L[f] = a f' - 6xf.
```

It has divergence form:

```text
L[f] = a^(-2) d/dx[a^3 f].
```

The IBP boundary term is:

```text
[f x^(2k - 1)a^5]_0^1.
```

For `k>=1` and regular `f`, this vanishes at both endpoints.

## 4. General primitive-power family

Sources:

```text
3_primitive_power_family_test.md
4_m2_selector_tests.md
regularity_admissibility_ladder/7_synthesis_family_ladder_selectors.md
regularity_admissibility_ladder/31_primitive_m_regular_ladder_connection.md
```

Define:

```text
G_(k,m)(x) = x^(2k - 1)a^m.
```

Then:

```text
G'_(k,m)
=
-(2k + 2m - 1)a^(m - 1) psi_(k,m)(x),
```

where:

```text
psi_(k,m)(x)
=
x^(2k) - ((2k - 1)/(2k + 2m - 1))x^(2k - 2).
```

The observed rows correspond to:

```text
m = 2.
```

The general pullback operator is:

```text
L_m[f] = a f' - 2(5 - m)xf.
```

For `m=2`:

```text
L_2[f] = a f' - 6xf = L[f].
```

For the regular flux-power range:

```text
1 <= m <= 5,
```

the same IBP form validates directly. The boundary term remains:

```text
[f x^(2k - 1)a^5]_0^1,
```

which is independent of `m`. Therefore boundary cleanliness alone does not select `m=2`.

## 5. Exponent ladder and selector status

Sources:

```text
2_operator_L_origin_tests.md
3_primitive_power_family_test.md
4_m2_selector_tests.md
regularity_admissibility_ladder/7_synthesis_family_ladder_selectors.md
regularity_admissibility_ladder/34_ladder_conclusion_report.md
```

For general `m`, the exponent roles are:

```text
primitive factor:       a^m
operator flux factor:   a^(5 - m)
projection weight:      a^4
IBP boundary factor:    a^5
```

For `m=2`:

```text
primitive factor:       a^2
operator flux factor:   a^3
projection weight:      a^4
IBP boundary factor:    a^5
```

So the observed case gives the adjacent ladder:

```text
a^2 -> a^3 -> a^4 -> a^5.
```

This is internally suggestive. It is not by itself an external derivation.

For generalized weight `w=a^beta`, the analogous roles are:

```text
primitive:   a^m
flux:        a^(beta + 1 - m)
weight:      a^beta
boundary:    a^(beta + 1)
```

The strict adjacent ordered ladder selects:

```text
beta = 4
m = 2.
```

This is a structural selector conditional on accepting the ordered ladder principle.

## 6. Weighted adjoint and second-order compositions

Sources:

```text
2_operator_L_origin_tests.md
4_m2_selector_tests.md
regularity_admissibility_ladder/5_synthesis_operator_energy.md
regularity_admissibility_ladder/10_boundary_domain_classifier.md
```

For:

```text
L_alpha[f] = a f' - 2(alpha + 1)x f
```

under weight:

```text
w_beta = a^beta,
```

the weighted adjoint satisfies:

```text
<L_alpha f, g>_beta
=
[a^(beta + 1)fg]_0^1
+
<f, L^*_(alpha,beta) g>_beta
```

with:

```text
L^*_(alpha,beta)[g]
=
-a g' + 2(beta - alpha)xg.
```

For the observed case:

```text
alpha = 2
beta = 4
```

so:

```text
L^*_w[g] = -a g' + 4xg.
```

and:

```text
<Lf,g>_w
=
[a^5 f g]_0^1
+
<f,L^*_w g>_w.
```

For the primitive-power family under `w=a^4`:

```text
L_m^*[g] = -a g' + 2m xg
```

and:

```text
L_m^* = -L_(5-m).
```

Thus the family pairs:

```text
m=1 <-> m=4
m=2 <-> m=3
m=3 <-> m=2
m=4 <-> m=1
```

The fixed skew-adjoint point is:

```text
m = 5/2,
```

not an integer primitive power.

The observed second-order compositions are:

```text
L^*_w L[f]
=
-a^2 f''
+
12xa f'
+
(6 - 30x^2)f
```

and:

```text
L L^*_w[g]
=
-a^2 g''
+
12xa g'
+
(4 - 28x^2)g.
```

Their zeroth-order residue is:

```text
(6 - 30x^2) - (4 - 28x^2) = 2a.
```

## 7. Candidate energy and the `u=a^3 f` transform

Sources:

```text
regularity_admissibility_ladder/13_energy_minimization_u_transform.md
regularity_admissibility_ladder/14_u_green_regular_solution.md
regularity_admissibility_ladder/15_regularity_admissibility_conditions.md
regularity_admissibility_ladder/34_ladder_conclusion_report.md
```

Consider the candidate energy:

```text
E[f] = 1/2 <L[f],L[f]>_w - <S,f>_w.
```

Define:

```text
u = a^3 f
f = u/a^3.
```

Then:

```text
L[f] = a^(-2)u'
```

and:

```text
(L[f])^2 w = (u')^2.
```

The source coupling becomes:

```text
S f w = S(u/a^3)a^4 = aS u.
```

Thus:

```text
E[u]
=
1/2 integral_0^1 (u')^2 dx
-
integral_0^1 aS u dx.
```

The Euler-Lagrange equation is:

```text
-u'' = aS.
```

The equivalence with the original second-order equation is:

```text
L^*_w L[f] = S
```

which becomes:

```text
-u'' = aS
```

after the transform.

The source-free zero-energy equation:

```text
L[f] = 0
```

implies:

```text
a^3 f = constant
f = constant/a^3.
```

Regularity at `x=1` forces the constant to vanish unless a baseline/domain shift is supplied.

## 8. Green kernel and regularity conditions

Sources:

```text
regularity_admissibility_ladder/14_u_green_regular_solution.md
regularity_admissibility_ladder/15_regularity_admissibility_conditions.md
regularity_admissibility_ladder/17_regularity_ladder_source_classes.md
regularity_admissibility_ladder/34_ladder_conclusion_report.md
```

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

Thus:

```text
u(x) = integral_0^1 G(x,y)F(y)dy.
```

Equivalent no-max form:

```text
u(x)
=
integral_x^1 (1-t)F(t)dt
+
(1-x) integral_0^x F(t)dt.
```

For the transformed energy:

```text
F = aS.
```

Endpoint derivative identities:

```text
u'(1) = - integral_0^1 F dx
u''(1) = -F(1)
u'''(1) = -F'(1)
u''''(1) = -F''(1)
```

Regularity of:

```text
f = u/a^3
```

at `x=1` requires `u` to vanish to high enough order. With `u(1)=0` already imposed:

```text
R=0 bounded/non-contact level:
  integral_0^1 aS dx = 0

R=1 contact level:
  integral_0^1 aS dx = 0
  S(1) = 0

R=2 contact level:
  integral_0^1 aS dx = 0
  S(1) = 0
  S'(1) = 0

R contact level:
  integral_0^1 aS dx = 0
  S vanishes to order R at x=1.
```

The first nontrivial admissibility condition is:

```text
C0[S] = integral_0^1 aS dx = 0.
```

Positive source probes:

```text
S_(p,q)=x^(2q)a^p
```

fail this cancellation because:

```text
integral_0^1 aS_(p,q) dx > 0.
```

Signed sources can satisfy it.

## 9. Balanced signed source bases

Sources:

```text
regularity_admissibility_ladder/16_regular_source_basis.md
regularity_admissibility_ladder/17_regularity_ladder_source_classes.md
regularity_admissibility_ladder/19_balanced_projection_signatures.md
regularity_admissibility_ladder/20_balanced_signature_factorization.md
regularity_admissibility_ladder/22_psi_adapted_balanced_basis.md
regularity_admissibility_ladder/23_y_variable_pairing_structure.md
```

For the first admissibility condition, define:

```text
B_q(x) = x^(2q) - c_q
```

where:

```text
c_q
=
integral_0^1 x^(2q)a dx
/
integral_0^1 a dx
=
3 / ((2q+1)(2q+3)).
```

Then:

```text
integral_0^1 a B_q dx = 0.
```

For endpoint-contact level `R`, define:

```text
B_(R,q)(x) = a^R[x^(2q) - c_(R,q)]
```

where:

```text
c_(R,q)
=
integral_0^1 x^(2q)a^(R+1) dx
/
integral_0^1 a^(R+1) dx.
```

In the `y=x^2` variable:

```text
B_(R,q)(y) = (1-y)^R(y^q - c_(R,q))
```

with beta/Pochhammer form:

```text
c_(R,q)
=
B(q+1/2,R+2) / B(1/2,R+2)
=
(1/2)_q / (R+5/2)_q.
```

The `psi_k` projection signatures on these bases are:

```text
P_R[k,q] = integral_0^1 psi_k B_(R,q) a^4 dx.
```

A closed moment form is:

```text
P_R[k,q]
=
M(2k+2q,R+4)
-
r_k M(2k+2q-2,R+4)
-
c_(R,q)[M(2k,R+4)-r_k M(2k-2,R+4)]
```

where:

```text
M(n,p) = integral_0^1 x^n a^p dx.
```

The signature matrix factors as:

```text
P_R = M_R T_R,
```

where `M_R` is the raw monomial projection matrix under shifted weight and `T_R` is the balancing transform.

Finite adapted bases can be built by:

```text
D = B P^(-1).
```

Then:

```text
integral_0^1 psi_k D_l a^4 dx = delta_(k,l).
```

Thus finite `psi` projections can be used as coordinates on balanced admissible source spaces.

## 10. `y=x^2` row structure and kernel bridge

Sources:

```text
regularity_admissibility_ladder/23_y_variable_pairing_structure.md
regularity_admissibility_ladder/24_span_complement_tests.md
regularity_admissibility_ladder/26_psi_missing_direction_closed_form.md
regularity_admissibility_ladder/27_first_admissibility_kernel_bridge.md
regularity_admissibility_ladder/28_higher_regular_kernel_bridge.md
regularity_admissibility_ladder/30_generalized_admissibility_rows.md
regularity_admissibility_ladder/32_general_chi_kernel_theorem.md
regularity_admissibility_ladder/33_general_cross_gram_invertibility.md
regularity_admissibility_ladder/34_ladder_conclusion_report.md
```

Set:

```text
y = x^2.
```

The original rows become:

```text
psi_k(y)
=
y^k - ((2k-1)/(2k+3))y^(k-1)
=
y^(k-1)(y-r_k).
```

The pairing with balanced sources is:

```text
integral_0^1 psi_k(x) B_(R,q)(x)a^4 dx

=
1/2 integral_0^1
psi_k(y)(y^q-c_(R,q))(1-y)^(R+4)y^(-1/2) dy.
```

For degree `<=N`, the span of:

```text
psi_1,...,psi_N
```

has dimension `N` inside the `N+1` dimensional polynomial space.

The missing coefficient vector is:

```text
m_j = 3 / ((2j+1)(2j+3)),  j=0..N.
```

The identity:

```text
m_k/m_(k-1) = (2k-1)/(2k+3)
```

gives:

```text
<coeff(psi_k),m> = 0.
```

The first admissibility functional on even polynomial sources has coefficients proportional to this vector:

```text
integral_0^1 a x^(2j) dx
=
2 / ((2j+1)(2j+3))
=
(2/3)m_j.
```

Therefore, on finite even-polynomial coefficient spaces:

```text
span{psi_1,...,psi_N}
=
ker[S -> integral_0^1 aS dx].
```

For higher endpoint-contact level `R`, define:

```text
C_R[P]
=
integral_0^1 P(y)(1-y)^(R+1)y^(-1/2) dy.
```

The adapted row family is:

```text
chi_(R,k)(y)
=
y^k - ((2k-1)/(2k+2R+3))y^(k-1).
```

Then, on polynomials of degree `<=N`:

```text
span{chi_(R,1),...,chi_(R,N)} = ker C_R.
```

Proof mechanism:

```text
C_R[y^k] / C_R[y^(k-1)]
=
(2k-1)/(2k+2R+3),
```

so:

```text
C_R[chi_(R,k)] = 0.
```

The rows are independent because each has a unique highest-degree term; the kernel dimension is `N`.

The original row family is:

```text
psi_k = chi_(0,k).
```

## 11. Primitive power as endpoint-contact level

Sources:

```text
regularity_admissibility_ladder/31_primitive_m_regular_ladder_connection.md
regularity_admissibility_ladder/32_general_chi_kernel_theorem.md
regularity_admissibility_ladder/34_ladder_conclusion_report.md
```

The generalized endpoint-contact row ratio is:

```text
(2k-1)/(2k+2R+3).
```

The primitive-power ratio is:

```text
(2k-1)/(2k+2m-1).
```

They agree when:

```text
m = R + 2.
```

Thus:

```text
m=2 <-> R=0
m=3 <-> R=1
m=4 <-> R=2
...
```

The observed primitive power `m=2` is the boundedness-level (`R=0`) member of the regularity/admissibility ladder for `f=u/a^3`.

This refines the earlier artifact warning:

```text
The primitive family is not just arbitrary duplication.
It labels endpoint-contact/admissibility level plus 2.
```

External gap:

```text
The bounded/non-contact admissibility problem itself still needs a physical/geometric derivation.
```

## 12. Matrix and determinant facts

Sources:

```text
regularity_admissibility_ladder/8_projection_matrix_closed_form.md
regularity_admissibility_ladder/9_galerkin_variational_matrix_test.md
regularity_admissibility_ladder/11_low_order_matrix_patterns.md
regularity_admissibility_ladder/19_balanced_projection_signatures.md
regularity_admissibility_ladder/21_projection_determinant_evidence.md
regularity_admissibility_ladder/25_symbolic_determinant_pattern_probe.md
regularity_admissibility_ladder/29_r0_invertibility_theorem.md
regularity_admissibility_ladder/33_general_cross_gram_invertibility.md
```

Moment closed form:

```text
A[k,j]
=
2[M(2k+2j,4) - r_k M(2k+2j-2,4)].
```

Equivalently:

```text
A[k,j]
=
2 M(2k+2j-2,4)
[
(k+j-1/2)/(k+j+9/2)
-
(2k-1)/(2k+3)
].
```

Pullback basis formula:

```text
L[x^(2j)] = 2j x^(2j-1) - (2j+6)x^(2j+1).
```

The variational stiffness matrix is:

```text
K[i,j] = <L phi_i, L phi_j>_w.
```

It satisfies:

```text
<phi_i, L^*_w L phi_j>_w = <L phi_i, L phi_j>_w.
```

But the original projection matrix:

```text
A[k,j] = 2<psi_k,phi_j>_w
```

is not the same as the stiffness matrix. Example:

```text
A[1,0] = -512/5775
K[0,0] = 512/385.
```

Finite evidence:

```text
original projection principal determinants nonzero through N=8
balanced signature determinants nonzero for R=0..5 through N=7
general chi/balanced cross-Gram determinants nonzero for R=0..4 through N=5
```

Conceptual `R=0` invertibility mechanism:

```text
In y=x^2, psi_k and the first balanced basis B_q both span the same finite kernel:

ker[S -> integral_0^1 aS dx].

The projection matrix between them is a cross Gram matrix under the positive weight:

(1-y)^4 y^(-1/2).

Because the positive inner product is nondegenerate on the finite kernel,
the cross Gram matrix between two bases of that kernel is invertible.
```

General determinant/product formulas remain open beyond the established kernel theorem and finite determinant evidence.

## 13. Guardrails

Sources:

```text
4_m2_selector_tests.md
conclusion.md
regularity_admissibility_ladder/9_galerkin_variational_matrix_test.md
regularity_admissibility_ladder/12_orthogonal_polynomial_nonidentification.md
regularity_admissibility_ladder/18_projection_vs_admissibility_rowspace.md
regularity_admissibility_ladder/34_ladder_conclusion_report.md
```

Negative or limiting results:

```text
psi_k is not a direct same-weight a^4 orthogonal row.

A is not the variational stiffness matrix K.

The psi hierarchy is not identical to the low-order endpoint-contact ladder
{integral aS, S(1), S'(1), ...} as row spaces.

Gegenbauer/Jacobi structure is contextual, not an identification of psi_k.

Compactified radial measure r=x/a^c gives a^(-cn-1), so it does not produce a^4
for c>0, n>0.

Adjoint closure gives m<->5-m, not m=2 uniquely.

Boundary cleanliness of the IBP term is family-wide, not m=2-specific.

Physical meanings of x, f, S, w, E[f], and the domain are not yet derived.
```

