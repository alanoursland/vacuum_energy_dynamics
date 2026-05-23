# Candidate Nonspherical Degree Inventory

## What This Document Is

This document is a development note.

It is not a postulate, theorem, proof, or complete nonspherical theory. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_nonspherical_degree_inventory.py
```

The guiding question was:

```text
What degrees of freedom are present in the current reduced program, and what
degrees of freedom are still missing for nonspherical gravity?
```

The answer is:

```text
The theory currently has a credible weak scalar sector, but not a full
nonspherical gravity sector.
```

Present:

```text
scalar A / Newtonian potential,
first-order scalar spatial compensation,
reduced kappa trace-response candidate.
```

Missing:

```text
trace-free spatial shear,
vector/frame-dragging modes,
tensor/wave modes,
nonlinear nonspherical closure.
```

The run also exposed one cosmetic script issue: the spatial conformal sector was correctly identified as pure trace/conformal, but the helper marked that line as `[WARN]` because of a SymPy matrix simplification check. The mathematical result is fine: the trace-free part is the zero matrix.

---

## Background

The weak multipole metric reconstruction showed that the scalar sector works at first order.

Let:

$$\psi=\frac{\Phi}{c^2}.$$

Then:

$$A=1+2\psi.$$

Reciprocal compensation gives:

$$B=\frac1A\approx1-2\psi.$$

This reproduces the standard weak scalar spatial factor and a \(\gamma=1\) proxy at first order.

However, nonspherical gravity requires more than scalar \(A\).

The degree-inventory script was written to prevent overclaiming.

---

## Metric Component Count

A symmetric four-dimensional metric has ten components:

```text
g_tt: 1
g_ti: 3
g_ij symmetric spatial: 6
```

A covariant theory has coordinate/gauge freedom, but the physical scalar/vector/tensor structures still need to be represented somehow.

A single scalar \(A\) covers only the weak temporal scalar/Newtonian component.

Therefore scalar \(A\) alone cannot represent the full metric perturbation.

---

## Scalar A / Newtonian Sector

The scalar \(A\)-sector is present.

With:

$$\psi=\frac{\Phi}{c^2},$$

we have:

$$A=1+2\psi.$$

This controls:

```text
g_tt weak scalar/Newtonian potential,
ordinary weak multipoles through Phi.
```

This is the strongest currently established nonspherical extension.

It connects the reduced program to the Newtonian weak-field scalar sector.

---

## Kappa / Trace-Response Sector

In the reduced spherical log variables:

$$a=\ln A,$$

and:

$$b=\ln B.$$

Then:

$$\kappa=\frac{a+b}{2},$$

and:

$$s=\frac{a-b}{2}.$$

The known status is:

```text
exterior source-free branch suppresses kappa;
matter interiors may source kappa;
kappa is not yet generalized covariantly for nonspherical fields.
```

Thus \(\kappa\) exists as a reduced trace/imbalance mode, especially useful in the interior/exterior matching program.

But it does not yet have a full nonspherical parent definition.

---

## Spatial Conformal Scalar Sector

The weak scalar spatial perturbation is:

$$h_{ij}^{\rm scalar}=-2\psi\delta_{ij}.$$

In matrix form:

$$
h_{ij}^{\rm scalar}
=
\begin{pmatrix}
-2\psi & 0 & 0 \\
0 & -2\psi & 0 \\
0 & 0 & -2\psi
\end{pmatrix}.
$$

Its trace is:

$$-6\psi.$$

Its trace-free part is zero:

$$
h_{ij}^{\rm scalar,TF}=0.
$$

So this sector is purely conformal/trace.

This is exactly what is expected for the weak scalar spatial factor.

But it also means scalar \(A\) does not encode trace-free spatial shear.

---

## Trace-Free Spatial Shear Sector

A general symmetric spatial perturbation is:

$$
h_{ij}
=
\begin{pmatrix}
h_{xx} & h_{xy} & h_{xz} \\
h_{xy} & h_{yy} & h_{yz} \\
h_{xz} & h_{yz} & h_{zz}
\end{pmatrix}.
$$

Its trace-free part is:

$$
h_{ij}^{\rm TF}
=
h_{ij}
-
\frac13{\rm Tr}(h)\delta_{ij}.
$$

This contains five independent components.

The scalar conformal perturbation cannot represent these trace-free spatial degrees of freedom.

Therefore a full nonspherical theory needs a spatial shear sector.

This is one of the largest missing sectors.

---

## Vector / Frame-Dragging Sector

Weak rotating sources introduce off-diagonal components:

$$g_{ti}\neq0.$$

These are vector, gravitomagnetic, or frame-dragging degrees of freedom.

The script represented the vector sector as:

$$g_{ti}=(V_x,V_y,V_z).$$

Scalar \(A\) and scalar reciprocal compensation do not produce such components.

Therefore frame dragging requires a vector sector beyond scalar \(A\).

This motivates:

```text
candidate_vector_sector_frame_dragging.py
```

---

## Tensor / Wave Sector

Linearized gravitational waves require transverse-traceless spatial perturbations:

$$h_{ij}^{\rm TT}.$$

For a wave propagating in the \(z\)-direction, an example transverse-traceless matrix is:

$$
h_{ij}^{\rm TT}
=
\begin{pmatrix}
h_+ & h_\times & 0 \\
h_\times & -h_+ & 0 \\
0 & 0 & 0
\end{pmatrix}.
$$

Its trace is zero.

This sector is required for gravitational waves and radiative tensor degrees of freedom.

It is not represented by scalar \(A\).

Therefore the current theory does not yet contain a wave sector.

---

## Scalar-Vector-Tensor Inventory

The current weak-field inventory is:

| Sector | Current status | Needed for |
|---|---|---|
| scalar \(A/\Phi\) | present | Newtonian potential, weak multipoles |
| scalar spatial conformal | present at first order via reciprocal compensation | \(\gamma=1\) scalar spatial metric |
| \(\kappa\) trace response | reduced/interior candidate | matter trace/interior deviation |
| spatial shear | missing | anisotropic spatial geometry |
| vector \(g_{ti}\) | missing | frame dragging / rotation |
| tensor TT | missing | gravitational waves |
| nonlinear closure | missing | strong nonspherical gravity |

This table is the current guardrail against overclaiming.

---

## Claim Boundaries

Currently supported claims:

1. Static spherical exterior recovery works in the reduced sector.
2. Weak scalar multipoles are compatible with:
   $$A=1+2\Phi/c^2.$$
3. Reciprocal compensation gives the \(\gamma=1\) scalar spatial factor at first order.
4. Interior \(\kappa\)-response is plausible and boundary-contained.

Not yet supported:

1. Full nonlinear nonspherical metric reconstruction.
2. Frame dragging.
3. Gravitational waves.
4. Complete covariant field equations.
5. Full matter stress-energy coupling.

---

## What This Study Established

This study established:

1. The scalar \(A\)-sector is present.
2. The weak spatial scalar/conformal sector is present at first order.
3. The reduced \(\kappa\)-sector exists but needs a nonspherical parent.
4. Trace-free spatial shear is missing.
5. Vector/frame-dragging modes are missing.
6. Tensor/wave modes are missing.
7. Nonlinear nonspherical closure is missing.
8. The current theory should not be described as a full nonspherical gravity theory.

---

## What This Study Did Not Establish

This study did not construct missing sectors.

It did not derive a vector field equation.

It did not derive tensor wave equations.

It did not define a nonspherical \(\kappa\) parent.

It did not solve nonlinear nonspherical closure.

It only classified what is present and what remains open.

---

## Current Best Interpretation

The current best interpretation is:

```text
The program has a credible weak scalar sector and a promising static spherical
recovery.

It does not yet have the full degree content of relativistic gravity.

The next missing sector to probe is the vector/frame-dragging sector.
```

This is why the next script should be:

```text
candidate_vector_sector_frame_dragging.py
```

---

## Summary

The nonspherical degree inventory makes the current boundary clear.

Present:

```text
scalar A / Newtonian potential,
first-order scalar spatial compensation,
reduced kappa trace-response candidate.
```

Missing:

```text
trace-free spatial shear,
vector/frame-dragging modes,
tensor/wave modes,
nonlinear nonspherical closure.
```

The immediate next target is the vector sector, because scalar \(A\) cannot produce \(g_{ti}\) components or frame dragging.
