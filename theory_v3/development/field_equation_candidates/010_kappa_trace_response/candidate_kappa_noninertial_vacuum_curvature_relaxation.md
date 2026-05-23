# Candidate Kappa Non-Inertial Vacuum-Curvature Relaxation

## What This Document Is

This document is a development note for the `10_kappa_trace_response/` group.

It is not a final \(\kappa\) field equation, not a covariant derivation, and not a completed parent ontology. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_kappa_noninertial_vacuum_curvature_relaxation.py
```

The guiding question was:

```text
Can kappa represent local vacuum-curvature equilibration without becoming a
propagating breathing-wave degree of freedom?
```

The answer is:

```text
Yes, as a control model.

Best refined kappa picture:
  kappa is not a wave.
  kappa is a non-inertial trace/volume relaxation coordinate.
  matter trace shifts the local vacuum-curvature minimum.
  vacuum and curvature exchange configuration energy toward that minimum.
  there is no independent kappa momentum channel.

Therefore:
  no overshoot,
  no slosh,
  no ordinary breathing radiation.
```

This fits the previous finding that breathing waves are not allowed:

```text
they may appear only as local trace relaxation,
not as propagating waves.
```

---

## Why This Study Matters

Earlier studies rejected ordinary massless scalar breathing radiation.

But there remained a possible fallback:

```text
what if the math forces a trace/breathing response?
```

This script sharpens that fallback.

The acceptable version is not a wave.

It is a local, non-inertial vacuum-curvature equilibration process.

That means \(\kappa\) can adjust toward a local minimum without carrying independent momentum or radiating as a scalar field.

---

## Bad Model: Second-Order Inertial Kappa

A second-order scalar model has the form:

\[
\ddot{\kappa}
+
\Gamma\dot{\kappa}
+
\omega_0^2\kappa
=
\text{source}.
\]

This gives \(\kappa\) a momentum-like channel:

\[
\pi_\kappa\sim\dot{\kappa}.
\]

Consequences:

```text
overshoot possible,
oscillation possible,
propagating scalar/breathing wave possible.
```

Status:

```text
RISK — can create breathing radiation.
```

This is not the preferred \(\kappa\) interpretation.

---

## Local Vacuum-Curvature Minimum

The proposed local minimum energy is:

\[
E_{\rm vac-curv}
=
\frac12K_\kappa(\kappa-\kappa_{\min})^2.
\]

The variational slope is:

\[
\frac{dE}{d\kappa}
=
K_\kappa(\kappa-\kappa_{\min}).
\]

Interpretation:

```text
kappa_min:
  local vacuum-curvature equilibrium value

matter trace / pressure:
  may shift kappa_min inside matter

exterior vacuum:
  should have kappa_min = 0
```

Status:

```text
PLAUSIBLE — K_kappa and kappa_min source law not derived.
```

---

## First-Order Gradient-Flow Relaxation

The candidate non-inertial relaxation law is:

\[
\dot{\kappa}
=
-\mu_\kappa
\frac{dE}{d\kappa}.
\]

For the quadratic minimum:

\[
\dot{\kappa}
=
-\mu_\kappa K_\kappa(\kappa-\kappa_{\min}).
\]

This has no \(\ddot{\kappa}\) term.

Therefore it has no independent \(\kappa\)-momentum channel.

Status:

```text
PLAUSIBLE — mobility mu_kappa not derived.
```

This is the core model.

---

## Monotonic No-Overshoot Solution

For constant \(\kappa_{\min}\):

\[
\dot{\kappa}
=
-\mu_\kappa K_\kappa(\kappa-\kappa_{\min}).
\]

The solution is:

\[
\kappa(t)-\kappa_{\min}
=
[\kappa(0)-\kappa_{\min}]
e^{-\mu_\kappa K_\kappa t}.
\]

Therefore:

```text
No oscillation.
No overshoot.
No slosh.
```

Status:

```text
DERIVED_REDUCED — for fixed local minimum.
```

This is the strongest result of the run.

---

## Energy Transfer Accounting

With:

\[
E=\frac12K_\kappa(\kappa-\kappa_{\min})^2,
\]

and:

\[
\dot{\kappa}
=
-\mu_\kappa K_\kappa(\kappa-\kappa_{\min}),
\]

the energy derivative is:

\[
\frac{dE}{dt}
=
-\mu_\kappa K_\kappa^2
(\kappa-\kappa_{\min})^2.
\]

The absorbed/configuration power is:

\[
P_{\rm absorb}
=
\mu_\kappa K_\kappa^2
(\kappa-\kappa_{\min})^2.
\]

For:

\[
\mu_\kappa>0,
\qquad
K_\kappa>0,
\]

we have:

\[
\frac{dE}{dt}\le0,
\]

and:

\[
P_{\rm absorb}\ge0.
\]

Interpretation:

```text
energy is not destroyed;
explicit imbalance energy is converted into vacuum configuration/restoration.
```

Status:

```text
DERIVED_REDUCED — destination variable E_vac still needs parent ontology.
```

---

## No Momentum Channel

In a wave/oscillator theory:

\[
L\sim\frac12\dot{\kappa}^2-V(\kappa),
\]

so:

\[
\pi_\kappa=\dot{\kappa}.
\]

This gives \(\kappa\) independent momentum.

In the proposed non-inertial relaxation law:

```text
no 1/2 kappa_dot^2 kinetic storage is introduced,
no independent pi_kappa is promoted,
kappa moves by mobility down the vacuum-curvature energy gradient.
```

This is why it does not slosh.

Status:

```text
CONSTRAINED_BY_IDENTITY — must be implemented without hidden second-order dynamics.
```

---

## Static A-Constraint Guard

The relaxation law must act on:

\[
\kappa-\kappa_{\min},
\]

not on:

\[
A_{\rm constraint}.
\]

The exterior \(A\)-sector remains:

\[
A=1-\frac{2GM}{c^2r}.
\]

Forbidden:

```text
relaxing away the areal mass flux,
damping the Newtonian/Schwarzschild monopole.
```

Allowed:

```text
restoring trace/volume imbalance toward local minimum,
keeping exterior kappa_min = 0.
```

Status:

```text
CONSTRAINED_BY_IDENTITY — sector split still must be derived.
```

---

## Source-Shifted Local Minimum

A possible source relation is:

\[
\kappa_{\min}
=
\chi_\kappa S_{\rm trace}.
\]

Interpretation:

```text
matter trace / pressure does not act as an ordinary wave source;
it shifts the local equilibrium configuration;
kappa then relaxes toward that equilibrium.
```

This avoids treating trace source as a radiative scalar charge.

Status:

```text
PLAUSIBLE — chi_kappa and S_trace definition not derived.
```

This is important: the source is not a charge for radiation, but a local equilibrium shift.

---

## Exterior Condition

Exterior vacuum target:

\[
S_{\rm trace}=0,
\]

and:

\[
\kappa_{\min}=0.
\]

The relaxation law becomes:

\[
\dot{\kappa}
=
-\mu_\kappa K_\kappa\kappa.
\]

So exterior \(\kappa\) decays toward:

\[
\kappa=0.
\]

If boundary flux is also zero:

```text
no long-range exterior kappa tail,
no free breathing wave.
```

Status:

```text
CONSTRAINED_BY_IDENTITY — boundary flux and parent constraint still needed.
```

---

## Classification

The script produced this classification:

| Item | Status |
|---|---|
| second-order inertial \(\kappa\) | RISK / disfavored |
| quadratic local minimum | PLAUSIBLE |
| first-order gradient-flow law | PLAUSIBLE |
| monotonic no-overshoot solution | DERIVED_REDUCED |
| positive absorption accounting | DERIVED_REDUCED |
| no independent momentum channel | CONSTRAINED_BY_IDENTITY |
| source as shifted local minimum | PLAUSIBLE |
| \(K_\kappa,\mu_\kappa,\chi_\kappa\) derivation | MISSING |
| parent covariant identity | MISSING |

---

## What This Study Established

This study established:

1. Second-order inertial \(\kappa\) is dangerous because it can support breathing radiation.
2. A first-order gradient-flow \(\kappa\) has no independent momentum channel.
3. For a fixed local minimum, \(\kappa\) relaxes monotonically.
4. There is no overshoot or slosh.
5. Energy decreases in the explicit imbalance coordinate and can be interpreted as vacuum configuration restoration.
6. Matter trace can be interpreted as shifting the local minimum rather than sourcing a radiative scalar charge.
7. Exterior vacuum relaxes toward \(\kappa=0\).

---

## What This Study Did Not Establish

This study did not derive \(K_\kappa\).

It did not derive \(\mu_\kappa\).

It did not derive \(\chi_\kappa\).

It did not derive \(S_{\rm trace}\).

It did not derive the parent covariant identity.

It did not solve boundary flux.

It only established a promising control model.

---

## Current Best Interpretation

The best refined \(\kappa\) picture is:

```text
kappa is not a wave.
kappa is a non-inertial trace/volume relaxation coordinate.
matter trace shifts the local vacuum-curvature minimum.
vacuum and curvature exchange configuration energy toward that minimum.
there is no independent kappa momentum channel.
```

Therefore:

```text
no overshoot,
no slosh,
no ordinary breathing radiation.
```

---

## Relation to the Breathing-Wave Rule

Previous result:

```text
breathing waves are not allowed.
```

Refined interpretation:

```text
propagating breathing waves are not allowed.
```

A local trace-volume adjustment may look like breathing, but it is not a wave if:

```text
it has no independent momentum channel,
it relaxes monotonically,
it does not propagate,
it is boundary-confined,
it preserves exterior kappa=0.
```

This keeps the cleaner rule while preserving a fallback if the math forces local trace adjustment.

---

## Next Development Target

The next script should be:

```text
candidate_kappa_boundary_layer_model.py
```

Purpose:

```text
Model interior kappa with exterior kappa=0 and no flux.
```

Reason:

```text
The non-inertial relaxation model requires a concrete boundary mechanism:
interior kappa can exist, but exterior kappa must vanish.
```

Expected result:

```text
A boundary-layer or compact-support model that permits interior trace relaxation
while enforcing kappa(R+)=0 and kappa'(R+)=0.
```

---

## Summary

This study gives the cleanest current \(\kappa\) interpretation:

\[
\dot{\kappa}
=
-\mu_\kappa K_\kappa(\kappa-\kappa_{\min}).
\]

It is first-order.

It has no \(\kappa\)-momentum.

It relaxes monotonically.

It does not slosh.

It does not propagate as breathing radiation.

The next goblin door is the boundary layer.
