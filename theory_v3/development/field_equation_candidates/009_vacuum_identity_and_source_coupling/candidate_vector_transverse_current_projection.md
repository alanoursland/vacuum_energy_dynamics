# Candidate Vector Transverse Current Projection

## What This Document Is

This document is a development note for the `09_vacuum_identity_and_source_coupling/` group.

It is not a full vector gauge theory, not a final Helmholtz decomposition theorem for the parent theory, and not a derivation of vector normalization. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_vector_transverse_current_projection.py
```

The guiding question was:

```text
Which part of the current should source the vector/curl sector W_i?
```

The answer is:

```text
The current should not feed the vector sector raw.

j_T -> W_i vector/curl sector
j_L -> scalar continuity / A_constraint sector
```

where:

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

The projected vector equation is:

\[
\nabla\times(\nabla\times W)
=
-\frac{\alpha_W}{2K_c}j_T.
\]

Under:

\[
\nabla\cdot W=0,
\]

this becomes:

\[
\Delta W
=
\frac{\alpha_W}{2K_c}j_T.
\]

The coefficient remains missing.

---

## Why This Study Matters

The curl-energy vector equation gave:

\[
\nabla\times(\nabla\times W)
=
-\frac{\alpha_W}{2K_c}j.
\]

But the vector curl sector should not blindly absorb all current.

Mass continuity is:

\[
\partial_t\rho+\nabla\cdot j=0.
\]

Some current represents accumulation or compression. That belongs with scalar continuity and \(A_{\rm constraint}\).

Some current represents circulation or rotation. That belongs with the vector/curl sector \(W_i\).

This study formalizes that separation.

---

## Helmholtz-Style Split

For suitable boundary conditions, a vector current can be decomposed as:

\[
j=j_T+\nabla\chi.
\]

where:

\[
\nabla\cdot j_T=0,
\]

and:

\[
\nabla\times\nabla\chi=0.
\]

The longitudinal piece is:

\[
j_L=\nabla\chi.
\]

The script classified this split as:

```text
CONSTRAINED_BY_IDENTITY — requires boundary conditions.
```

That is the correct caution.

The split is not free-floating; it depends on domain and boundary behavior.

---

## Gradient Current Is Longitudinal

For:

\[
j_L=\nabla\chi,
\]

the curl vanishes:

\[
\nabla\times j_L=0.
\]

The script verified this symbolically and classified it as:

```text
DERIVED_REDUCED
```

This is important because it gives a clean criterion for the current piece that should not source curl \(W\).

A purely longitudinal current belongs with scalar continuity, not the vector curl sector.

---

## Rotational Current Is Transverse

The script tested a rotational current:

\[
j_T=(-J_0y,\;J_0x,\;0).
\]

It found:

\[
\nabla\cdot j_T=0,
\]

and:

\[
\nabla\times j_T=(0,\;0,\;2J_0).
\]

The script classified this as:

```text
DERIVED_REDUCED
```

This is exactly the kind of current that should source vector/curl response.

It carries circulation.

It is tied to angular momentum.

It is the natural \(W_i\) source.

---

## Continuity Allocation

Mass continuity is:

\[
\partial_t\rho+\nabla\cdot j=0.
\]

If:

\[
j=j_T+j_L,
\]

and:

\[
\nabla\cdot j_T=0,
\]

then:

\[
\partial_t\rho+\nabla\cdot j_L=0.
\]

Interpretation:

```text
j_T carries circulation/rotation and sources W_i.
j_L carries compression/accumulation and belongs with scalar constraint.
```

This prevents the vector sector from swallowing scalar continuity.

The script classified this as:

```text
CONSTRAINED_BY_IDENTITY — formal projection/boundary conditions still needed.
```

---

## Projected Vector Field Equation

The curl-energy vector equation is:

\[
\nabla\times(\nabla\times W)
=
-\frac{\alpha_W}{2K_c}j.
\]

The projected source policy is:

\[
\nabla\times(\nabla\times W)
=
-\frac{\alpha_W}{2K_c}j_T.
\]

Under:

\[
\nabla\cdot W=0,
\]

this becomes:

\[
\Delta W
=
\frac{\alpha_W}{2K_c}j_T.
\]

The coefficient remains:

\[
\frac{\alpha_W}{2K_c}.
\]

The script classified this as:

```text
CONSTRAINED_BY_IDENTITY — coefficient and projection operator missing.
```

---

## Projection Safety Table

The script produced this table:

| Current piece | Property | Sector assignment | Status |
|---|---|---|---|
| \(j_T\) | \(\nabla\cdot j_T=0\) | \(W_i\) vector/curl sector | CONSTRAINED_BY_IDENTITY |
| \(j_L\) | \(\nabla\times j_L=0\) | scalar continuity / \(A_{\rm constraint}\) | CONSTRAINED_BY_IDENTITY |
| full \(j\) | continuity source | split required | PARTIAL |
| time-dependent split | needs projection operator | MISSING |
| coefficient \(\alpha_W/(2K_c)\) | normalization | MISSING |

This table is the main result.

---

## Failure Controls

The projection fails if:

1. \(j_L\) is allowed to source \(W_i\) directly.
2. \(j_T\) is disconnected from angular momentum or current circulation.
3. Projection depends on arbitrary gauge choices without boundary rules.
4. The coefficient is inserted from GR matching.
5. Time-dependent longitudinal pieces violate scalar constraint propagation.

These are the goblin traps.

---

## What This Study Established

This study established:

1. The current should be split:
   \[
   j=j_T+j_L.
   \]

2. \(j_T\) is divergence-free:
   \[
   \nabla\cdot j_T=0.
   \]

3. \(j_L\) is curl-free:
   \[
   \nabla\times j_L=0.
   \]

4. \(j_T\) should source \(W_i\).

5. \(j_L\) should remain with scalar continuity and \(A_{\rm constraint}\).

6. The vector equation should use:
   \[
   j_T
   \]
   rather than raw \(j\).

---

## What This Study Did Not Establish

This study did not derive the projection operator.

It did not solve boundary conditions.

It did not derive the vector coefficient.

It did not solve time-dependent scalar/vector constraint propagation.

It did not connect the projected current to a measured frame-dragging normalization.

It only established the sector-allocation rule.

---

## Current Best Interpretation

The current should not feed the vector sector raw.

The natural policy is:

```text
j_T -> W_i vector/curl sector
j_L -> scalar continuity / A_constraint sector
```

Projected vector equation:

\[
\nabla\times(\nabla\times W)
=
-\frac{\alpha_W}{2K_c}j_T.
\]

Under transverse gauge:

\[
\Delta W
=
\frac{\alpha_W}{2K_c}j_T.
\]

The coefficient is still missing.

---

## Next Development Target

The next script should be:

```text
candidate_vector_current_projection_operator.py
```

Purpose:

```text
Write the formal transverse projector and test simple examples.
```

Expected result:

```text
P_T removes longitudinal/gradient current and preserves transverse/rotational current.
```

This turns the projection rule into an operator instead of just a verbal split.

---

## Summary

The vector transverse-current projection study gives the clean allocation rule:

\[
j_T\rightarrow W_i,
\]

and:

\[
j_L\rightarrow A_{\rm constraint}/\text{scalar continuity}.
\]

The vector sector should only eat the rotational/transverse current.

The next step is to write the formal projector.
