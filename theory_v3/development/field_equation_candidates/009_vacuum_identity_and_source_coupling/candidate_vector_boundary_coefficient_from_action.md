# Candidate Vector Boundary Coefficient From Action

## What This Document Is

This document is a development note for the `09_vacuum_identity_and_source_coupling/` group.

It is not a derivation of Lense-Thirring normalization, not a final vector-source action, and not a completed frame-dragging theory. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_vector_boundary_coefficient_from_action.py
```

The guiding question was:

```text
Can the exterior/boundary coefficient be tied to the curl-energy source ratio
alpha_W/(2K_c)?
```

The answer is:

```text
The boundary coefficient is not a totally new free knob.

It can be related structurally to:
  alpha_W/K_c,
  source geometry / shape factor.

But the actual normalization is still missing because:
  alpha_W/K_c is missing,
  C_shape is missing,
  beta_W is missing.
```

This is a useful narrowing result.

---

## Why This Study Matters

The previous boundary-value study found the exterior shape:

\[
W_\phi=\frac{C_JJ\sin\theta}{r^2},
\]

and therefore:

\[
B_W=\nabla\times W\sim\frac{J}{r^3}.
\]

But it left the normalization unresolved:

```text
C_b,
C_J,
C_W,
beta_W.
```

This study asks whether \(C_b\) is an extra arbitrary coefficient, or whether it is controlled by the vector action ratio.

The result is that \(C_b\) should be controlled by the action ratio and source geometry.

That reduces the number of free knobs.

It does not finish the normalization.

---

## Curl-Energy Source Ratio

The curl-energy equation is:

\[
\nabla\times(\nabla\times W)
=
-\frac{\alpha_W}{2K_c}j_T.
\]

The coefficient ratio is:

\[
\lambda_{\rm eq}
=
\frac{\alpha_W}{2K_c}.
\]

The script classified this as:

```text
MISSING — alpha_W/(2K_c) not derived.
```

This remains the main vector-action normalization gap.

---

## Green-Function Amplitude

Under transverse gauge:

\[
\Delta W=\frac{\alpha_W}{2K_c}j_T.
\]

Using the usual Poisson Green-function convention introduces a factor:

\[
\frac{1}{4\pi}.
\]

So schematically:

\[
W(x)
\sim
\frac{\alpha_W}{8\pi K_c}
\int
\frac{j_T(x')}{|x-x'|}
\,d^3x'.
\]

The Green-function amplitude is:

\[
\lambda_{\rm green}
=
\frac{\alpha_W}{8\pi K_c}.
\]

The script classified this as:

```text
CONSTRAINED_BY_IDENTITY — absolute ratio still missing.
```

This is not a GR coefficient.

It only says that the exterior amplitude is tied to the missing action ratio.

---

## Far-Field Relation to Angular Momentum

For a compact rotating source, the far-field vector amplitude should have the form:

\[
C_JJ.
\]

The script parameterized:

\[
C_J
=
C_{\rm shape}
\frac{\alpha_W}{8\pi K_c}.
\]

Here:

```text
C_shape:
  angular/source-geometry factor

alpha_W/K_c:
  vector action/source ratio
```

The script classified this as:

```text
CONSTRAINED_BY_IDENTITY — shape factor and action ratio not fully derived.
```

This is important because it says the far-field coefficient is not arbitrary once the source model and action ratio are known.

---

## Boundary Coefficient Relation

The boundary coefficient can be parameterized as:

\[
C_b
=
C_{\rm shape}
\frac{\alpha_W}{8\pi K_c}.
\]

This means:

```text
C_b should not be treated as an independent new knob if the action and source
model are specified.
```

But:

```text
C_shape and alpha_W/K_c are still missing.
```

The script classified this as:

```text
CONSTRAINED_BY_IDENTITY — not a final normalization.
```

This is the main result.

The boundary coefficient has been reduced to deeper missing pieces.

---

## Precession Coefficient Separation

The observable precession coefficient separates into:

\[
C_{\rm total}
=
\beta_W
C_{\rm shape}
\frac{\alpha_W}{8\pi K_c}.
\]

So:

```text
vector field normalization
```

and:

```text
precession/observable coupling
```

are separate.

The missing pieces are:

```text
beta_W,
C_shape,
alpha_W/K_c.
```

The script classified this as:

```text
MISSING — observable normalization not derived.
```

This means even if the vector field coefficient is structurally controlled, the measured gyroscope/precession response still needs an observable coupling law.

---

## No New Free Boundary Knob

The script’s key practical conclusion is:

```text
C_b should not be treated as an independent free coefficient once the vector
action, source coupling, and boundary/source model are fixed.
```

Instead:

\[
C_b
\]

is controlled by:

```text
alpha_W/K_c,
geometry/source shape factors.
```

Remaining danger:

```text
if alpha_W/K_c, beta_W, and C_shape are all independently fitted, the vector
sector becomes a fit machine.
```

This is the right warning.

---

## Classification

The script produced this classification:

| Item | Status |
|---|---|
| curl-energy equation ratio \(\alpha_W/(2K_c)\) | MISSING |
| Green-function amplitude \(\alpha_W/(8\pi K_c)\) | CONSTRAINED_BY_IDENTITY |
| boundary coefficient \(C_b\) from action ratio | CONSTRAINED_BY_IDENTITY |
| source/shape factor \(C_{\rm shape}\) | MISSING |
| precession coupling \(\beta_W\) | MISSING |
| Lense-Thirring normalization | HAND_ASSIGNED if inserted now |

This is the current honest normalization status.

---

## What This Study Established

This study established:

1. \(C_b\) is not a completely independent coefficient.
2. \(C_b\) can be related to:
   \[
   C_{\rm shape}\frac{\alpha_W}{8\pi K_c}.
   \]
3. The action ratio:
   \[
   \frac{\alpha_W}{K_c}
   \]
   remains missing.
4. The shape/source factor:
   \[
   C_{\rm shape}
   \]
   remains missing.
5. The observable precession coupling:
   \[
   \beta_W
   \]
   remains missing.
6. Lense-Thirring normalization must not be inserted by hand.

---

## What This Study Did Not Establish

This study did not derive \(\alpha_W/K_c\).

It did not derive \(C_{\rm shape}\).

It did not derive \(\beta_W\).

It did not recover Lense-Thirring normalization.

It did not solve the precession observable.

It only showed that the boundary coefficient should be controlled by the action/source structure rather than treated as a separate arbitrary knob.

---

## Current Best Interpretation

The boundary coefficient is not a totally new free knob.

It can be related structurally to:

```text
alpha_W/K_c,
source geometry / shape factor.
```

But the actual normalization is still missing because:

```text
alpha_W/K_c is missing,
C_shape is missing,
beta_W is missing.
```

---

## Next Development Target

The next script should be:

```text
candidate_vector_source_shape_factor.py
```

Purpose:

```text
Compute the source/shape factor for a simple uniformly rotating sphere
symbolically.
```

Expected result:

```text
The far-field vector amplitude should be proportional to the angular momentum J,
with a calculable source-geometry factor under the chosen Green-function
convention.
```

Rules:

```text
Keep alpha_W/K_c symbolic.
Do not insert Lense-Thirring normalization.
Separate source-shape factor from action ratio and precession coupling.
```

---

## Summary

The vector boundary-coefficient study removes one fake degree of freedom.

The boundary coefficient is not:

```text
an independent arbitrary knob.
```

It should be:

\[
C_b
=
C_{\rm shape}
\frac{\alpha_W}{8\pi K_c}.
\]

But the vector normalization is still not reconstructed.

The next goblin is \(C_{\rm shape}\).
