# Candidate Vector Sector Status Summary

## Purpose

This document summarizes the vector-current / frame-dragging line inside the `09_vacuum_identity_and_source_coupling/` group.

The purpose of this line was not to reproduce the Lense-Thirring coefficient by matching.

The purpose was to ask:

```text
Does the vacuum-substance / continuity picture actually demand a vector-current
sector, and how far can that sector be reconstructed before coefficient
matching would be required?
```

The answer is:

```text
The vector sector now has a real structural reconstruction.

It has:
  source type,
  projection rule,
  curl-energy field equation,
  global angular momentum source,
  exterior far-field shape.

It does not have:
  normalization,
  beta_W observable coupling,
  alpha_W/K_c action ratio,
  Lense-Thirring coefficient.
```

In short:

```text
Vector structure: yes.
Vector normalization: no.
```

---

## Files in This Vector Line

The vector line consists of:

```text
candidate_vector_current_from_continuity.py
candidate_vector_current_from_continuity.md

candidate_vector_frame_dragging_observable.py
candidate_vector_frame_dragging_observable.md

candidate_vector_coefficient_normalization.py
candidate_vector_coefficient_normalization.md

candidate_vector_stiffness_from_vacuum_transport.py
candidate_vector_stiffness_from_vacuum_transport.md

candidate_vector_curl_energy_field_equation.py
candidate_vector_curl_energy_field_equation.md

candidate_vector_transverse_current_projection.py
candidate_vector_transverse_current_projection.md

candidate_vector_current_projection_operator.py
candidate_vector_current_projection_operator.md

candidate_vector_global_rotation_mode.py
candidate_vector_global_rotation_mode.md

candidate_vector_boundary_value_problem.py
candidate_vector_boundary_value_problem.md

candidate_vector_boundary_coefficient_from_action.py
candidate_vector_boundary_coefficient_from_action.md

candidate_vector_source_shape_factor.py
candidate_vector_source_shape_factor.md

candidate_vector_sector_status_summary.md
```

This is a complete vector subline for now.

---

## Main Result

The main result is:

```text
Continuity forces a natural vector source:
  j_i = rho v_i.
```

If density sources scalar exchange:

\[
\rho\rightarrow A_{\rm constraint},
\]

then current naturally sources vector transport:

\[
j_i=\rho v_i\rightarrow W_i.
\]

That is ontology work, not GR matching.

The vector sector then develops as:

\[
j_i
\rightarrow
j_T
\rightarrow
W_i
\rightarrow
B_W=\nabla\times W
\rightarrow
B_W\sim\frac{J}{r^3}.
\]

But the coefficient remains missing.

---

## Step 1: Current From Continuity

The continuity equation is:

\[
\partial_t\rho+\nabla\cdot j=0.
\]

This implies that if \(\rho\) is the scalar source, then \(j_i=\rho v_i\) is the natural vector source.

The minimal vector source form was:

\[
\Delta W_i\sim j_i.
\]

Status:

```text
source type constrained,
coefficient missing.
```

This was the first real vector reconstruction step.

---

## Step 2: Safer Observable Candidate

Raw \(W_i\) is gauge-sensitive.

The safer diagnostic is:

\[
B_W=\nabla\times W.
\]

This is useful because:

\[
\nabla\times\nabla\phi=0.
\]

So curl removes pure-gradient gauge-like pieces.

A symbolic precession relation was written:

\[
\Omega_{\rm drag}=\beta_WB_W.
\]

Status:

```text
B_W diagnostic candidate constrained,
beta_W missing.
```

---

## Step 3: Coefficient Discipline

The vector coefficient was kept symbolic.

The forbidden move is:

```text
choose alpha_W/K_W only to match Lense-Thirring.
```

The honest options are:

```text
shared scalar/vector stiffness,
independent vector stiffness,
phenomenological coefficient.
```

Status:

```text
source type constrained,
coefficient missing.
```

This prevented fake reconstruction.

---

## Step 4: Vacuum Transport Stiffness

A more gauge-aware vector action was proposed:

\[
E_W\sim K_c|\nabla\times W|^2+\alpha_W j_iW_i.
\]

This is better than raw \(|\nabla W|^2\) because the curl term ignores pure-gradient pieces.

But the missing ratio remained:

\[
\frac{\alpha_W}{K_c}.
\]

Status:

```text
action structure plausible,
coefficient missing.
```

---

## Step 5: Curl-Energy Field Equation

Varying the curl-energy action gives:

\[
\nabla\times(\nabla\times W)
=
-\frac{\alpha_W}{2K_c}j.
\]

Under transverse gauge:

\[
\nabla\cdot W=0,
\]

this becomes:

\[
\Delta W
=
\frac{\alpha_W}{2K_c}j.
\]

Status:

```text
field equation structure derived,
coefficient missing.
```

This is one of the strongest structural results in the vector line.

---

## Step 6: Transverse Current Projection

The vector/curl sector should not eat raw current.

The current should split:

\[
j=j_T+j_L,
\]

with:

\[
\nabla\cdot j_T=0,
\]

and:

\[
\nabla\times j_L=0.
\]

Sector allocation:

```text
j_T -> W_i vector/curl sector
j_L -> scalar continuity / A_constraint sector
```

The projected vector equation is:

\[
\nabla\times(\nabla\times W)
=
-\frac{\alpha_W}{2K_c}j_T.
\]

Status:

```text
sector allocation constrained,
coefficient missing.
```

---

## Step 7: Projection Operator

In Fourier space, the transverse projector is:

\[
P_T=I-\frac{kk^T}{k^2}.
\]

The longitudinal projector is:

\[
P_L=\frac{kk^T}{k^2}.
\]

Then:

\[
j_T=P_Tj,
\]

and:

\[
j_L=P_Lj.
\]

The projector:

```text
is idempotent,
kills longitudinal current,
preserves transverse current.
```

Status:

```text
local projector algebra derived for k^2 != 0.
```

The caveat is:

```text
k=0 / global rotation requires boundary treatment.
```

---

## Step 8: Global Rotation Mode

Global angular momentum is:

\[
J=\int r\times j\,d^3x.
\]

This is not solved by the local \(k\neq0\) projector alone.

A compact rotating source should set exterior vector boundary data through \(J\).

Status:

```text
global source object constrained,
boundary coefficient missing.
```

---

## Step 9: Boundary-Value Shape

A symbolic exterior vector field was used:

\[
W_\phi(r,\theta)
=
\frac{C_JJ\sin\theta}{r^2}.
\]

Its curl components scale as:

\[
B_r\sim \frac{J\cos\theta}{r^3},
\]

and:

\[
B_\theta\sim \frac{J\sin\theta}{r^3}.
\]

Thus:

\[
B_W\sim\frac{J}{r^3}.
\]

Status:

```text
far-field shape derived,
normalization missing.
```

This is a real structural reconstruction.

---

## Step 10: Boundary Coefficient From Action

The boundary coefficient is not a totally independent knob.

It can be related to:

\[
C_b
=
C_{\rm shape}
\frac{\alpha_W}{8\pi K_c}.
\]

So the vector normalization is controlled by:

```text
action ratio alpha_W/K_c,
source-shape factor C_shape,
observable coupling beta_W.
```

Status:

```text
boundary knob reduced,
normalization still missing.
```

---

## Step 11: Source Shape Factor

For a uniformly rotating sphere:

\[
M=\frac{4\pi R^3\rho}{3},
\]

\[
j=\rho(\Omega\times r),
\]

\[
\nabla\cdot j=0,
\]

\[
\int j\,d^3x=0,
\]

and:

\[
J=\frac{2}{5}MR^2\Omega.
\]

So the source geometry reduces cleanly to angular momentum \(J\).

Status:

```text
source geometry derived,
normalization missing.
```

---

## What Is Now Reconstructed

The vector line reconstructs the following structure:

### Source Type

\[
j_i=\rho v_i.
\]

### Sector Projection

\[
j_T=P_Tj.
\]

### Vector Field Equation

\[
\nabla\times(\nabla\times W)
=
-\frac{\alpha_W}{2K_c}j_T.
\]

### Transverse Gauge Form

\[
\Delta W
=
\frac{\alpha_W}{2K_c}j_T.
\]

### Observable Candidate

\[
B_W=\nabla\times W.
\]

### Global Source

\[
J=\int r\times j\,d^3x.
\]

### Far-Field Shape

\[
B_W\sim\frac{J}{r^3}.
\]

This is meaningful.

It is not just a label map.

---

## What Is Not Reconstructed

The vector line does not reconstruct:

```text
alpha_W/K_c,
beta_W,
absolute C_shape,
Lense-Thirring normalization,
measured gyroscope precession coupling,
full covariant gauge behavior,
radiation behavior of W_i.
```

These are still open.

The most important missing normalization chain is:

\[
\Omega_{\rm drag}
=
\beta_W
\left(
C_{\rm shape}
\frac{\alpha_W}{8\pi K_c}
\right)
\frac{J}{r^3}.
\]

The missing pieces are:

```text
alpha_W/K_c,
C_shape,
beta_W.
```

---

## Honest Status

The honest status is:

```text
Vector source:
  reconstructed from continuity.

Vector projection:
  reconstructed locally.

Vector equation:
  derived from curl-energy action.

Global source:
  angular momentum J.

Far-field shape:
  J/r^3.

Normalization:
  missing.
```

So the vector sector is no longer merely asserted by analogy.

But it has not yet reproduced GR frame dragging.

---

## Relation to Claude's Criticism

The criticism was that \(W_i\) was previously asserted by analogy.

That criticism was fair before this group.

After this vector line, the updated status is:

```text
W_i is no longer merely asserted.

It is structurally motivated by:
  continuity,
  transverse projection,
  curl-energy,
  angular momentum boundary data.

But its normalization is still not reconstructed.
```

So the criticism has been partially answered.

Not fully.

---

## Recommended Next Move

The vector line has reached a natural boundary.

Continuing would likely chase normalization without the deeper missing ontology pieces.

The better next move is one of:

```text
candidate_kappa_source_law_from_trace_exchange.py
candidate_tensor_source_from_exchange_identity.py
```

The stronger choice is probably:

```text
candidate_kappa_source_law_from_trace_exchange.py
```

Reason:

```text
kappa remains the least disciplined sector.
It still needs one primary role and one source law.
```

---

## Summary

The vector-current line now has real structure:

\[
\rho\rightarrow j_i\rightarrow j_T\rightarrow W_i\rightarrow\nabla\times W\rightarrow J/r^3.
\]

That is progress.

But the coefficient remains unreconstructed.

So the vector sector status is:

```text
structure yes,
normalization no.
```

This is a good stopping point for the vector subline.
