# Candidate Vacuum-Substance Continuity Identity

## What This Document Is

This document is a development note for the `09_vacuum_identity_and_source_coupling/` group.

It is not a covariant conservation law, not a Bianchi identity, and not a completed source-coupling theory. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_vacuum_substance_continuity_identity.py
```

The guiding question was:

```text
If the vacuum is treated as a substance-like ontology, what balance law does
that ontology demand before importing GR identities?
```

The answer is a candidate ontology-native balance law:

```text
partial_t q_v + div J_v = Sigma_exchange + Sigma_creation - Gamma_relax
```

or:

\[
\partial_t q_v+\nabla\cdot J_v
=
\Sigma_{\rm exchange}
+
\Sigma_{\rm creation}
-
\Gamma_{\rm relax}.
\]

This is not yet a covariant identity.

But it is the first attempt to make the vacuum-substance ontology produce equation structure instead of merely interpreting already-chosen equations.

---

## Why This Study Matters

Group 08 found that conservation/source identities are missing.

That was a major blocker because the current sectors cannot remain independent source assignments forever:

```text
A_constraint <- mass density
kappa        <- pressure/stress/trace candidate
W_i          <- mass current/angular momentum
h_ij^TT      <- trace-free quadrupole derivatives
```

If the ontology is doing real work, then at least some of these source assignments should follow from vacuum bookkeeping.

This script asks what the vacuum-substance picture itself suggests.

---

## Candidate Balance Law

The candidate identity is:

\[
\partial_t q_v+\nabla\cdot J_v
=
\Sigma_{\rm exchange}
+
\Sigma_{\rm creation}
-
\Gamma_{\rm relax}.
\]

Interpretation:

```text
q_v:
  scalar vacuum-substance density / charge proxy

J_v:
  vacuum flow / current proxy

Sigma_exchange:
  exchange with matter or source sector

Sigma_creation:
  genuine nonconservative vacuum amount creation/destruction

Gamma_relax:
  relaxation back toward a vacuum minimum
```

This law expresses:

```text
accumulation + outflow = exchange + creation - relaxation
```

The script marked this as partial because the terms still need sector-specific definitions.

---

## Pure Conservation Branch

The pure conservation limit is:

\[
\partial_t q_v+\nabla\cdot J_v=0.
\]

In one dimension, the script wrote:

\[
\partial_x J_v(t,x)+\partial_t q_v(t,x).
\]

This branch is useful because it establishes the bookkeeping structure.

But it remains partial because:

```text
q_v is not yet physically defined.
```

The script explicitly warns that \(q_v\) is not mass density. It is a vacuum bookkeeping charge/density proxy.

The parent theory must define what this vacuum charge actually measures.

---

## Exchange / Creation / Relaxation Balance

The full balance law is:

\[
\partial_t q_v+\nabla\cdot J_v
=
\Sigma_{\rm exchange}
+
\Sigma_{\rm creation}
-
\Gamma_{\rm relax}.
\]

The script interprets the terms as:

```text
exchange:
  matter/vacuum transfer or coupling

creation:
  nonconservative vacuum amount change

relaxation:
  return toward vacuum minimum
```

This ties directly to the earlier exchange/creation/relaxation regime language.

The important improvement is that the regime language now has a candidate equation form.

---

## Static Exterior Consistency

For the static exterior scalar field:

\[
A=1-\frac{2GM}{c^2r},
\]

the areal flux is:

\[
F_A=4\pi r^2A'=\frac{8\pi GM}{c^2}.
\]

The flux derivative is:

\[
\frac{dF_A}{dr}=0.
\]

The script confirmed:

```text
static exterior compatible with zero local source.
```

Exterior policy:

```text
Sigma_exchange = 0 outside matter
Sigma_creation = 0 in ordinary exterior
Gamma_relax = 0 for settled static constraint configuration
```

Thus the static exterior field is compatible with conserved scalar flux and no local vacuum creation.

This is a good result.

It means the ontology-native balance law does not break the strongest existing reconstruction.

---

## Matter Exchange as A_constraint Source

The reduced scalar source law is:

\[
\Delta_{\rm areal}A=\frac{8\pi G}{c^2}\rho.
\]

The areal flux derivative is:

\[
\frac{dF_A}{dr}
=
4\pi r^2
\frac{8\pi G}{c^2}\rho.
\]

The script wrote:

\[
\frac{dF_A}{dr}
=
\frac{32\pi^2Gr^2\rho(r)}{c^2}.
\]

Ontology interpretation:

```text
matter density acts as an exchange term for scalar vacuum flux.
```

Candidate identification:

\[
\Sigma_{{\rm exchange},A}
\sim
\frac{8\pi G}{c^2}\rho.
\]

This is partial because the normalization still comes from the reduced \(A\)-flux result.

It is not yet derived from the deeper ontology.

---

## Vacuum Current and W_i Source Hint

If scalar exchange uses density:

\[
\rho,
\]

then vector response should plausibly use matter transport/current:

\[
j_i=\rho v_i.
\]

The script wrote:

\[
j_i=\rho v_i
=
(\rho v_x,\rho v_y,\rho v_z).
\]

Ontology hint:

```text
If scalar exchange uses density rho, vector response should use transport/current j_i.
```

This is useful because it gives \(W_i\) an ontology-native source direction:

```text
W_i should be tied to vacuum/matter current continuity,
not assigned only by analogy to frame dragging.
```

But the script correctly marks this as partial.

No \(W_i\) field equation or coefficient has been derived yet.

---

## Relaxation and A_rad Suppression

A relaxation law for scalar radiative perturbation can be written:

\[
\frac{dA_{\rm rad}}{d\tau}
=
-\Gamma\mu^2A_{\rm rad}.
\]

The solution is:

\[
A_{\rm rad}(\tau)=a_0e^{-\Gamma\mu^2\tau}.
\]

Ontology interpretation:

```text
scalar perturbations can relax back toward the vacuum minimum.
```

This encodes the vacuum absorption idea:

```text
A_rad may be generated locally but relaxed away before becoming long-range scalar radiation.
```

The caveat is critical:

```text
This must suppress A_rad without erasing A_constraint.
```

So relaxation must act on radiative/deviation modes, not on the settled static constraint field.

---

## Creation Regime as Nonconservative Special Case

If:

\[
\Sigma_{\rm creation}\neq0,
\]

then the vacuum-substance bookkeeping is locally nonconservative.

The script marks this as a risk.

Creation may be allowed only in special regimes:

```text
cosmological creation,
strong-field vacuum restructuring,
phase/defect transitions.
```

But ordinary exterior gravity should usually set:

\[
\Sigma_{\rm creation}=0.
\]

Otherwise the creation term becomes a free knob.

This is an important guardrail.

---

## Sector Source Classification

The continuity attempt gives this current source classification:

| Sector | Source from continuity picture | Status |
|---|---|---|
| \(A_{\rm constraint}\) | scalar exchange with density \(\rho\) | PARTIAL |
| \(W_i\) | current / transport \(j_i=\rho v_i\) | PARTIAL |
| \(\kappa\) | stress / trace / volume exchange | MISSING |
| \(h_{ij}^{TT}\) | quadrupole time-varying conserved source | PARTIAL |
| \(A_{\rm rad}\) | relaxation / absorption-controlled perturbation | PARTIAL |
| creation regime | explicit nonconservative source | RISK |

Interpretation:

```text
The continuity picture begins to constrain A and W_i source types.
It does not yet derive kappa, tensor normalization, or closure identities.
```

This is exactly the right level of progress for the first group-09 script.

---

## Failure Controls

The script listed six failure controls.

This ontology-native identity attempt fails if:

1. \(q_v\) remains undefined forever.
2. \(\Sigma_{\rm exchange}\) is chosen separately for every sector.
3. \(\Sigma_{\rm creation}\) becomes a free knob for any mismatch.
4. \(\Gamma_{\rm relax}\) suppresses unwanted modes but also destroys static gravity.
5. \(W_i\) current coupling is set only by GR matching.
6. No Bianchi-like closure emerges from the balance law.

These are the right traps to keep visible.

---

## What This Study Established

This study established:

1. The vacuum-substance ontology suggests a balance identity:
   \[
   \partial_t q_v+\nabla\cdot J_v
   =
   \Sigma_{\rm exchange}
   +
   \Sigma_{\rm creation}
   -
   \Gamma_{\rm relax}.
   \]

2. The static exterior \(A\)-flux result is compatible with zero local source.

3. Matter density can be interpreted as scalar exchange for \(A_{\rm constraint}\).

4. Matter current naturally points toward a \(W_i\) source.

5. Relaxation can encode vacuum absorption of \(A_{\rm rad}\).

6. Creation must be treated as a special nonconservative regime, not a free knob.

7. The identity is useful but incomplete.

---

## What This Study Did Not Establish

This study did not define \(q_v\).

It did not derive coefficients.

It did not derive \(\kappa\)'s source.

It did not derive the tensor source from the identity.

It did not derive \(W_i\)'s equation.

It did not produce Bianchi-like closure.

It did not become a covariant conservation law.

---

## Current Best Interpretation

The vacuum-substance ontology now has its first candidate balance law:

```text
partial_t q_v + div J_v = Sigma_exchange + Sigma_creation - Gamma_relax
```

This begins to turn the exchange/creation/relaxation language into equation structure.

It suggests:

```text
density -> scalar exchange / A_constraint
current -> vector response / W_i
relaxation -> suppression of A_rad
creation -> special nonconservative regime, not a free knob
```

But it is not yet enough.

The next step is to map source coupling from vacuum exchange more explicitly.

---

## Next Development Target

The next script should be:

```text
candidate_source_coupling_from_vacuum_exchange.py
```

Purpose:

```text
Ask how density, current, stress/trace, and time-varying quadrupole structure
could arise as different projections of one vacuum-exchange balance law.
```

Expected categories:

```text
derived from continuity,
partially constrained,
still hand-assigned,
risk/free knob.
```

The goal is to reduce hand assignment.

---

## Summary

The vacuum-substance continuity identity is not a finished law.

But it is an important move because it asks the ontology to do work.

The candidate identity is:

\[
\partial_t q_v+\nabla\cdot J_v
=
\Sigma_{\rm exchange}
+
\Sigma_{\rm creation}
-
\Gamma_{\rm relax}.
\]

This is ontology-native.

It supports the static exterior, suggests \(A\) and \(W_i\) source directions, includes relaxation as \(A_{\rm rad}\) suppression, and quarantines creation as a special nonconservative regime.

The missing goblin hoard remains:

```text
define q_v,
derive coefficients,
derive kappa source,
derive tensor source,
derive closure.
```
