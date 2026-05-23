# Candidate Vector Current Projection Operator

## What This Document Is

This document is a development note for the `09_vacuum_identity_and_source_coupling/` group.

It is not a full vector gauge theory, not a boundary-condition theory, and not a derivation of frame-dragging normalization. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_vector_current_projection_operator.py
```

The guiding question was:

```text
Can the current split j = j_T + j_L be written as a formal projection operator?
```

The answer is yes for nonzero Fourier modes.

The transverse projector is:

\[
P_T
=
I-\frac{kk^T}{k^2}.
\]

The longitudinal projector is:

\[
P_L
=
\frac{kk^T}{k^2}.
\]

Then:

\[
j_T=P_Tj,
\]

and:

\[
j_L=P_Lj.
\]

The projector works locally for \(k^2\neq0\), but the \(k=0\) / global rotation mode requires boundary treatment.

---

## Why This Study Matters

The previous current-projection study established the allocation rule:

```text
j_T -> W_i vector/curl sector
j_L -> scalar continuity / A_constraint sector
```

But that was still mostly verbal.

This script formalizes the split with a projection operator.

That matters because the vector sector should not eat raw current. It should only see the transverse current.

---

## Formal Projectors

In Fourier space, with:

\[
k=(k_x,k_y,k_z),
\]

and:

\[
k^2=k_x^2+k_y^2+k_z^2,
\]

the longitudinal projector is:

\[
P_L=\frac{kk^T}{k^2}.
\]

The transverse projector is:

\[
P_T=I-P_L.
\]

The script printed the full matrix forms and marked them as:

```text
CONSTRAINED_BY_IDENTITY — valid for k^2 != 0.
```

The \(k^2\neq0\) caveat is important.

---

## Projector Identities

The script verified:

\[
P_T^2=P_T,
\]

\[
P_L^2=P_L,
\]

\[
P_TP_L=0,
\]

and:

\[
P_T+P_L=I.
\]

All checks returned zero matrices.

The script classified this as:

```text
DERIVED_REDUCED
```

This means the local projector algebra is sound.

---

## k-Aligned Test Currents

For \(k\) along the \(z\)-axis:

\[
P_T=
\begin{pmatrix}
1&0&0\\
0&1&0\\
0&0&0
\end{pmatrix},
\]

and:

\[
P_L=
\begin{pmatrix}
0&0&0\\
0&0&0\\
0&0&1
\end{pmatrix}.
\]

For a longitudinal current:

\[
j_{\rm long}=(0,0,J),
\]

the script found:

\[
P_Tj_{\rm long}=0,
\]

and:

\[
P_Lj_{\rm long}=j_{\rm long}.
\]

For a transverse current:

\[
j_{\rm trans}=(J,0,0),
\]

the script found:

\[
P_Tj_{\rm trans}=j_{\rm trans},
\]

and:

\[
P_Lj_{\rm trans}=0.
\]

The script classified this as:

```text
DERIVED_REDUCED
```

This is the clean local test of the projector.

---

## Projected Vector Field Equation

The projected current is:

\[
j_T=P_Tj.
\]

The curl-energy equation becomes:

\[
\nabla\times(\nabla\times W)
=
-\frac{\alpha_W}{2K_c}j_T.
\]

Under:

\[
\nabla\cdot W=0,
\]

the equation becomes:

\[
\Delta W
=
\frac{\alpha_W}{2K_c}j_T.
\]

The coefficient remains:

\[
\frac{\alpha_W}{2K_c}.
\]

The script marked this as:

```text
CONSTRAINED_BY_IDENTITY — coefficient remains missing.
```

This is now the cleanest vector-sector field equation structure.

---

## Scalar / Vector Allocation

The projection policy is:

```text
j_T = P_T j -> W_i vector/curl sector
j_L = P_L j -> scalar continuity / A_constraint
```

Mass continuity is:

\[
\partial_t\rho+\nabla\cdot j=0.
\]

In Fourier form, longitudinal current controls density accumulation:

\[
\partial_t\rho_k+i\,k\cdot j_L=0.
\]

The transverse current satisfies:

\[
k\cdot j_T=0.
\]

So \(j_T\) does not directly change density.

The script classified this as:

```text
CONSTRAINED_BY_IDENTITY — time-domain/boundary implementation still needed.
```

This is a good result: the vector current can now be separated from scalar continuity.

---

## k=0 Zero-Mode Warning

The Fourier projector uses:

\[
\frac{1}{k^2}.
\]

Therefore:

\[
k=0
\]

requires separate treatment.

The script interprets this as:

```text
total conserved momentum / global current / boundary rotation modes may not be
captured by the local projector alone.
```

This is not a local algebra failure.

It is a boundary/global-mode issue.

This is the next problem.

---

## Classification

The script produced this classification:

| Item | Status |
|---|---|
| \(P_T\) definition | CONSTRAINED_BY_IDENTITY |
| \(P_T\) idempotence | DERIVED_REDUCED |
| \(P_T\) kills longitudinal current | DERIVED_REDUCED |
| \(P_T\) preserves transverse current | DERIVED_REDUCED |
| projected vector equation | CONSTRAINED_BY_IDENTITY |
| coefficient \(\alpha_W/(2K_c)\) | MISSING |
| \(k=0\) / global modes | RISK / boundary issue |

This is the current honest status.

---

## What This Study Established

This study established:

1. The formal transverse projector is:
   \[
   P_T=I-\frac{kk^T}{k^2}.
   \]

2. The longitudinal projector is:
   \[
   P_L=\frac{kk^T}{k^2}.
   \]

3. \(P_T\) and \(P_L\) are valid projectors for \(k^2\neq0\).

4. \(P_T\) kills longitudinal current.

5. \(P_T\) preserves transverse current.

6. The vector equation should use:
   \[
   j_T=P_Tj.
   \]

7. The \(k=0\) / global mode requires boundary treatment.

---

## What This Study Did Not Establish

This study did not derive the vector coefficient.

It did not solve boundary conditions.

It did not handle global rotation.

It did not derive Lense-Thirring.

It did not solve vector gauge behavior globally.

It only solved the local nonzero-mode projector algebra.

---

## Current Best Interpretation

The formal transverse projector works:

\[
P_T=I-\frac{kk^T}{k^2}.
\]

It kills longitudinal current and preserves transverse current.

Projected policy:

```text
j_T = P_T j -> W_i
j_L = P_L j -> scalar continuity
```

The vector coefficient remains missing.

The \(k=0\) / global rotation mode requires boundary treatment.

---

## Next Development Target

The next script should be:

```text
candidate_vector_global_rotation_mode.py
```

Purpose:

```text
Study k=0 / global angular momentum and boundary conditions.
```

Reason:

```text
The projector exposes a global mode that cannot be handled by the local
Fourier projector alone.
```

The vector sector cannot claim frame dragging until global rotation and angular momentum boundary data are handled.

---

## Summary

The current projection operator study gives a clean local result:

\[
j_T=P_Tj,
\qquad
P_T=I-\frac{kk^T}{k^2}.
\]

This protects the vector sector from absorbing scalar continuity.

But the next goblin is global:

```text
k=0 / total rotation / boundary angular momentum.
```

That is the next vector-sector test.
