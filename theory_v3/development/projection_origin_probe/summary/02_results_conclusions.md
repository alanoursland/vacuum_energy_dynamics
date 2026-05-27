# Results and Conclusions Packet

This file states what the uploaded proof corpus establishes, what it does not establish, and what remains worth proving next.

## Executive conclusion

Sources:

```text
conclusion.md
regularity_admissibility_ladder/34_ladder_conclusion_report.md
regularity_admissibility_ladder/speculative_synthesis.md
```

The projection hierarchy is not random algebraic debris.

It has a real integration-by-parts origin, a weighted-divergence pullback operator, a transformed Dirichlet-energy form in `u=a^3 f`, and a strong connection to the first regularity/admissibility kernel.

The strongest current formal label is:

```text
regularity-adapted weighted projection/admissibility hierarchy
```

not:

```text
field equation
source law
curvature energy
exchange energy
vacuum burden
physical residual
```

The later ladder files improve the original root-level pause result:

```text
Earlier status:
  m=2 was selected by the observed projection ratio but not independently forced.

Refined internal status:
  m=2 is the R=0 member of the regularity/admissibility ladder,
  corresponding to boundedness of f=u/a^3.

Remaining external gap:
  the bounded/non-contact admissibility problem itself has not been physically/geometrically derived.
```

## Main established mathematical results

### 1. `psi_k` is derived by integration by parts

Sources:

```text
1_psi_k_ibp_origin.md
conclusion.md
```

The row function:

```text
psi_k(x)
=
x^(2k) - ((2k-1)/(2k+3))x^(2k-2)
```

comes from:

```text
G_k(x)=x^(2k-1)(1-x^2)^2
```

through:

```text
G_k'(x)=-(2k+3)(1-x^2)psi_k(x).
```

So the ratio:

```text
(2k-1)/(2k+3)
```

is product-rule structure, not arbitrary fitting.

### 2. Projection rows pull back to odd moments of `L[f]`

Sources:

```text
1_psi_k_ibp_origin.md
2_operator_L_origin_tests.md
```

With:

```text
w=a^4
L[f]=af'-6xf
```

the core pullback identity is:

```text
<psi_k,f>_w
=
1/(2k+3)<x^(2k-1),L[f]>_w.
```

The operator is:

```text
L[f]=a^(-2)d(a^3f)/dx.
```

Thus the projection hierarchy is more naturally read as an admissibility/moment test of a transformed flux-like derivative than as a positive energy row.

### 3. The primitive-power family exists

Sources:

```text
3_primitive_power_family_test.md
4_m2_selector_tests.md
```

For:

```text
G_(k,m)=x^(2k-1)a^m
```

one obtains:

```text
psi_(k,m)(x)
=
x^(2k)-((2k-1)/(2k+2m-1))x^(2k-2)
```

and:

```text
L_m[f]=af'-2(5-m)xf.
```

The observed hierarchy is the `m=2` member.

This was originally an artifact warning because the IBP mechanism itself is not unique.

### 4. `m=2` has a refined internal explanation through regularity

Sources:

```text
regularity_admissibility_ladder/30_generalized_admissibility_rows.md
regularity_admissibility_ladder/31_primitive_m_regular_ladder_connection.md
regularity_admissibility_ladder/32_general_chi_kernel_theorem.md
regularity_admissibility_ladder/34_ladder_conclusion_report.md
```

The generalized regularity row family is:

```text
chi_(R,k)(y)
=
y^k - ((2k-1)/(2k+2R+3))y^(k-1).
```

The primitive-power family ratio matches this exactly when:

```text
m = R+2.
```

Therefore:

```text
m=2 <-> R=0.
```

The original rows are the boundedness-level rows:

```text
psi_k = chi_(0,k).
```

This does not make the whole framework physical, but it does remove some of the earlier worry that the primitive family was merely arbitrary.

### 5. The `u=a^3 f` transform exposes the admissibility problem

Sources:

```text
regularity_admissibility_ladder/13_energy_minimization_u_transform.md
regularity_admissibility_ladder/14_u_green_regular_solution.md
regularity_admissibility_ladder/15_regularity_admissibility_conditions.md
```

The candidate energy:

```text
E[f]=1/2<Lf,Lf>_w - <S,f>_w
```

becomes:

```text
E[u]=1/2 integral (u')^2 dx - integral aS u dx
```

under:

```text
u=a^3f.
```

Its Euler-Lagrange equation is:

```text
-u''=aS.
```

Regularity of:

```text
f=u/a^3
```

at `x=1` imposes cancellations on `F=aS`. The first nontrivial condition is:

```text
integral_0^1 aS dx=0.
```

This is the first admissibility condition.

### 6. The original `psi_k` rows span the first admissibility kernel

Sources:

```text
regularity_admissibility_ladder/24_span_complement_tests.md
regularity_admissibility_ladder/26_psi_missing_direction_closed_form.md
regularity_admissibility_ladder/27_first_admissibility_kernel_bridge.md
regularity_admissibility_ladder/32_general_chi_kernel_theorem.md
```

In `y=x^2`:

```text
psi_k(y)=y^k-((2k-1)/(2k+3))y^(k-1).
```

In polynomials of degree `<=N`, the span of `psi_1,...,psi_N` has codimension one. The missing coefficient vector is:

```text
m_j=3/((2j+1)(2j+3)).
```

The first admissibility functional has coefficients proportional to:

```text
integral_0^1 a x^(2j)dx
=
2/((2j+1)(2j+3)).
```

Therefore:

```text
span{psi_1,...,psi_N}
=
ker[S -> integral_0^1 aS dx]
```

on finite even-polynomial coefficient spaces.

This is the strongest non-speculative bridge in the corpus.

### 7. Balanced source classes preserve diagnostic rank

Sources:

```text
regularity_admissibility_ladder/16_regular_source_basis.md
regularity_admissibility_ladder/17_regularity_ladder_source_classes.md
regularity_admissibility_ladder/19_balanced_projection_signatures.md
regularity_admissibility_ladder/20_balanced_signature_factorization.md
regularity_admissibility_ladder/21_projection_determinant_evidence.md
regularity_admissibility_ladder/22_psi_adapted_balanced_basis.md
regularity_admissibility_ladder/33_general_cross_gram_invertibility.md
```

The balanced source basis is:

```text
B_(R,q)(x)=a^R[x^(2q)-c_(R,q)].
```

with:

```text
c_(R,q)
=
integral x^(2q)a^(R+1)dx / integral a^(R+1)dx.
```

These classes satisfy the first admissibility cancellation and endpoint vanishing appropriate to endpoint-contact level `R`.

The projection signatures:

```text
P_R[k,q]=integral psi_k B_(R,q)a^4 dx
```

retain full tested rank. For `R=0`, invertibility has a conceptual proof: both `psi_k` and the balanced basis span the same finite kernel, and the cross Gram matrix under the positive Jacobi-type weight is nondegenerate.

Finite `psi`-adapted balanced bases can be built by inverting `P_R`.

## Important negative results and guardrails

### Same-weight orthogonality fails

Sources:

```text
1_psi_k_ibp_origin.md
regularity_admissibility_ladder/12_orthogonal_polynomial_nonidentification.md
```

The ratio expected from same-weight `a^4` constant orthogonality is:

```text
(2k-1)/(2k+9),
```

not the observed:

```text
(2k-1)/(2k+3).
```

So the rows are not direct `a^4` orthogonal polynomial rows.

### Orthogonal-polynomial neighborhood is contextual only

Sources:

```text
regularity_admissibility_ladder/12_orthogonal_polynomial_nonidentification.md
regularity_admissibility_ladder/23_y_variable_pairing_structure.md
```

The weight relates to Gegenbauer/Jacobi structure, especially after `y=x^2`, but `psi_k` is not the corresponding monic Gegenbauer or shifted Jacobi family. The Jacobi setting is useful context, not an identification.

### The projection matrix is not the stiffness matrix

Sources:

```text
regularity_admissibility_ladder/9_galerkin_variational_matrix_test.md
```

The stiffness matrix:

```text
K[i,j]=<L phi_i,L phi_j>_w
```

is not the same as:

```text
A[k,j]=2<psi_k,phi_j>_w.
```

Therefore `A` should not be described as the variational stiffness matrix. It is a once-integrated projection/pullback matrix.

### Low-order admissibility rowspaces are not identical to the projection rows

Sources:

```text
regularity_admissibility_ladder/18_projection_vs_admissibility_rowspace.md
```

The `psi_k` hierarchy is not simply the same rowspace as:

```text
integral aS
S(1)
S'(1)
...
```

at low order. The better statement is:

```text
psi_k rows encode the first admissibility kernel in coefficient space,
while higher endpoint contact requires generalized rows and rebalanced source classes.
```

### Compactified radial measure does not produce the weight

Sources:

```text
4_m2_selector_tests.md
regularity_admissibility_ladder/7_synthesis_family_ladder_selectors.md
```

For:

```text
r=x/a^c
```

an `n`-dimensional radial measure gives:

```text
a^(-cn-1).
```

For positive `c,n`, this cannot produce:

```text
a^4.
```

The standard compactification would formally require negative dimension. Therefore radial compactification alone does not explain the projection weight.

### Physical interpretation is not derived

Sources:

```text
conclusion.md
regularity_admissibility_ladder/34_ladder_conclusion_report.md
speculation.md
regularity_admissibility_ladder/speculative_synthesis.md
```

The corpus does not derive physical meanings for:

```text
x
f
S
w=a^4
E[f]
the Green-domain boundary conditions
the source pairing
```

Speculation exists, but it is quarantined in the speculation file.

## Current best dependency graph

```text
Projection form A[k,j]
  -> row functions psi_k

psi_k
  -> IBP primitive G_k=x^(2k-1)a^2
  -> ratio r_k=(2k-1)/(2k+3)

IBP primitive
  -> pullback L[f]=af'-6xf
  -> divergence form L=a^(-2)(a^3 f)'

L and w=a^4
  -> weighted adjoint L*_w=-a d/dx + 4x
  -> second-order candidate L*_w L
  -> energy candidate 1/2<Lf,Lf>_w

u=a^3f
  -> energy becomes 1D Dirichlet
  -> equation becomes -u''=aS
  -> boundedness/contact of f generates admissibility conditions

first admissibility C0[S]=integral aS=0
  -> balanced source basis B_q=x^(2q)-3/((2q+1)(2q+3))
  -> y=x^2 psi span equals ker C0

higher endpoint-contact R
  -> balanced classes B_(R,q)=a^R[y^q-c_(R,q)]
  -> generalized rows chi_(R,k)
  -> primitive power m=R+2
```

## Best current conclusion

The strongest formal result is:

```text
The observed projection hierarchy is the R=0 endpoint-contact/admissibility row family
for the transformed problem u=a^3f, where boundedness of f=u/a^3 produces
the first admissibility kernel integral aS=0.
```

The strongest unresolved issue is:

```text
The transformed energy/domain/regularity problem has not been derived from
an external physical or geometric principle.
```

## Good next mathematical targets

The next work should be theorem-sized, not speculation-sized.

### Target 1: Prove general cross-Gram invertibility

Turn finite determinant evidence into a theorem for:

```text
G_R[k,q]
=
1/2 integral_0^1
chi_(R,k)(y)(y^q-c_(R,q))(1-y)^(R+4)y^(-1/2)dy.
```

Known facts to use:

```text
chi_(R,k) span ker C_R
balanced polynomials y^q-c_(R,q) span ker C_R
positive Jacobi-type inner product is nondegenerate
```

Need clarify whether the weight in the cross Gram matches the same kernel functional or requires an additional argument.

### Target 2: Derive or reject a closed determinant formula

Finite determinant data is nonzero and structured, but a closed product formula is not established.

### Target 3: Formalize the regularity theorem in operator-domain language

State precisely:

```text
Given -u''=aS, u'(0)=0, u(1)=0, f=u/a^3.
Then f in C^R at x=1 iff integral aS=0 and S vanishes to order R at x=1
```

under suitable smoothness assumptions.

### Target 4: Identify the minimal external object needed

The mathematical ladder is coherent, but physical interpretation requires at least one concrete external object:

```text
a measure deriving w=a^4
a variational principle deriving E[f]
a boundary/domain derivation of u'(0)=0,u(1)=0
a geometric meaning for x
a source-pairing derivation
a physical reason boundedness R=0 is the selected target
```

Until one appears, do not promote the hierarchy to physics.

