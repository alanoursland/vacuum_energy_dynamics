# Plan for Group 15: Vacuum Current and Exchange Continuity

## Canonical Group Name

```text
15_vacuum_current_and_exchange_continuity
```

## Purpose

Group 15 exists because Group 14 closed with a precise bottleneck:

```text
J_V / u_vac definition for vacuum-volume exchange.
```

Group 14 did not derive \(A_{\rm spatial}\). It reduced the spatial-trace origin problem to the question:

```text
Can a real vacuum-volume current J_V^mu be defined?
```

The strongest candidate structure is:

\[
\nabla_\mu J_V^\mu
=
\Sigma_V
-
R_V.
\]

But this is not yet a law.

It becomes a law only if the group can define:

```text
J_V flux direction / transport law,
Sigma_V source creation law,
R_V relaxation / exchange law,
timelike / nonzero domain for J_V,
static-source neutrality,
boundary neutrality,
no-overlap / residual-kill theorem,
sign / orientation convention.
```

The locked door for Group 15 is therefore:

```text
Can a real exchange continuity law define J_V?
```

---

## What Group 15 Is Not

Group 15 is not allowed to become another broad projector loop.

It is not allowed to reopen every Group 14 branch.

It is not allowed to derive \(A_{\rm spatial}\) by tuning recovery targets.

It is not allowed to declare:

\[
\nabla_\mu J_V^\mu
=
\Sigma_V
-
R_V
\]

and pretend the current has been defined.

It is not allowed to define:

\[
J_V^\mu=n_Vu_{\rm vac}^\mu
\]

as the definition of \(u_{\rm vac}\). That is circular.

It is not allowed to use \(J_V\) as:

```text
decorative flux,
coefficient tuning current,
far-zone scalar current,
acausal repair current,
boundary mass-changing current.
```

Tiny goblin warning:

```text
No flux law, no vacuum clock.
```

---

## Central Objects

### Vacuum-Volume Current

\[
J_V^\mu
\]

Candidate role:

```text
vacuum-volume flux current.
```

Needed for:

\[
u_{\rm vac}^\mu
=
\frac{J_V^\mu}{\sqrt{-J_V^2}}.
\]

Required conditions:

```text
J_V^2 < 0 where u_vac is used,
J_V != 0 where u_vac is used,
J_V is non-circular,
J_V has a flux / transport direction,
J_V is boundary-neutral in ordinary closed gravity,
J_V does not create residual metric trace outside B_s.
```

---

### Source Creation Term

\[
\Sigma_V
\]

Candidate role:

```text
source-driven vacuum-volume creation / destruction.
```

Current leading candidate inherited from Group 14:

\[
\Sigma_V
\sim
\chi\rho a^\mu\nabla_\mu A.
\]

Status:

```text
CANDIDATE / UNFINISHED
```

Still missing:

```text
frame / projection,
chi-origin,
static-source safety,
sign convention,
covariant source expression,
relation to zeta and B_s.
```

---

### Relaxation / Exchange Term

\[
R_V
\]

Candidate role:

```text
vacuum-volume relaxation,
reconfiguration,
or return toward local equilibrium.
```

Important distinction:

```text
R_V is not energy destruction.
R_V is not damping pasted onto scalar waves.
R_V is exchange / restoration / reconfiguration.
```

Still missing:

```text
operator,
sign convention,
local equilibrium target,
relation to zeta_min,
relation to kappa relaxation,
boundary neutrality,
no-overlap with residual trace.
```

---

### Vacuum Rest Frame

\[
u_{\rm vac}^\mu
\]

Desired definition:

\[
u_{\rm vac}^\mu
=
\frac{J_V^\mu}{\sqrt{-J_V^2}}.
\]

Status:

```text
UNRESOLVED
```

Group 15 should not define \(u_{\rm vac}\) directly unless \(J_V\) is real.

---

## Group 15 Success Criteria

Group 15 succeeds if it does one of the following.

### Strong Success

It defines a non-circular vacuum-volume current:

\[
J_V^\mu
\]

and shows how the exchange law:

\[
\nabla_\mu J_V^\mu
=
\Sigma_V
-
R_V
\]

can be meaningful without GR smuggling, coefficient tuning, scalar exterior charge, or residual trace double-counting.

### Useful Partial Success

It does not define \(J_V^\mu\), but it identifies exactly which ingredient blocks the current:

```text
Sigma_V source law,
R_V exchange law,
flux direction,
timelike domain,
boundary neutrality,
or no-overlap.
```

### Good Failure

It proves that, with the current ingredients, no non-circular, timelike, boundary-neutral \(J_V^\mu\) can be defined.

Then:

```text
u_vac remains undefined,
acceleration-gradient volume creation remains a theorem target,
A_spatial remains a recovery theorem target,
and the project must return to postulate-level ontology before field equations.
```

---

## Group 15 Failure Modes

Fatal failure modes:

```text
decorative exchange continuity,
decorative J_V,
J_V defined circularly from u_vac,
Sigma_V named but not defined,
R_V named but not defined,
scalar source converted into flux direction without transport law,
static sources creating exterior scalar charge,
zeta residual trace reintroduced after being killed,
gamma_like or AB used to choose coefficients,
boundary neutrality dropped,
no-overlap dropped.
```

Major risks:

```text
R_V as damping patch,
Sigma_V as gamma repair spell,
J_V as acausal repair current,
u_vac as arbitrary preferred frame,
zeta-gradient current used outside timelike/nonzero domain,
exchange continuity written before source and relaxation terms are split.
```

---

## Recommended Script Sequence

### 15.1 `candidate_exchange_continuity_law_for_volume.py`

Purpose:

```text
Open Group 15 by testing the strongest surviving structure:
  nabla_mu J_V^mu = Sigma_V - R_V.
```

Main question:

```text
Can a real exchange continuity law define J_V?
```

This script should establish the minimal requirements:

```text
J_V flux direction,
Sigma_V source law,
R_V exchange law,
timelike/nonzero J_V domain,
static-source neutrality,
boundary neutrality,
no-overlap,
sign/orientation.
```

Expected result:

```text
The continuity equation is the right locked door,
but it is not yet a law until Sigma_V, R_V, and flux direction are defined.
```

Recommended next script:

```text
candidate_sigma_R_split_for_volume_exchange.py
```

---

### 15.2 `candidate_sigma_R_split_for_volume_exchange.py`

Purpose:

```text
Split Sigma_V and R_V before claiming exchange continuity.
```

Main question:

```text
What is creation/source, and what is relaxation/reconfiguration?
```

Candidate ledger entries:

```text
Sigma_V as source-driven creation/destruction,
Sigma_V as acceleration-gradient source,
Sigma_V as trace/volume conversion source,
R_V as local equilibrium restoration,
R_V as zeta_min relaxation,
R_V as kappa-linked relaxation,
R_V as boundary-neutral reconfiguration,
Sigma/R double-counting risk,
sign convention,
ordinary closed-regime constraints.
```

Expected result:

```text
Sigma_V and R_V must be independent enough to make continuity meaningful,
but tied enough to avoid becoming two scalar reservoirs.
```

Recommended next script:

```text
candidate_volume_flux_direction_law.py
```

unless the split fails, in which case:

```text
candidate_group_15_early_failure_summary.py
```

---

### 15.3 `candidate_volume_flux_direction_law.py`

Purpose:

```text
Test what determines the direction of J_V.
```

Main question:

```text
How does a scalar creation term become a vector current?
```

Candidate branches:

```text
gradient-driven flux,
zeta-gradient flux,
source-gradient flux,
exchange-potential flux,
constitutive law J_V ~ -D nabla zeta,
causal transport law,
zero-flux local exchange,
compact-support redistribution,
forbidden acausal repair current.
```

Important guardrail:

```text
Sigma_V gives divergence/source strength.
It does not by itself determine the direction of J_V.
```

Expected result:

```text
Either a flux-direction law survives,
or J_V cannot yet be defined.
```

Recommended next script:

```text
candidate_timelike_domain_for_volume_current.py
```

if a flux direction survives.

---

### 15.4 `candidate_timelike_domain_for_volume_current.py`

Purpose:

```text
Determine where J_V can define u_vac.
```

Main question:

```text
Is J_V timelike and nonzero in the regimes where u_vac is needed?
```

Test conditions:

\[
J_V^2<0,
\qquad
J_V\ne0.
\]

Branches:

```text
timelike current in active exchange regions,
zero current in static equilibrium,
spacelike redistribution current,
null transition current,
domain-limited u_vac,
equilibrium-frame fallback,
no global u_vac.
```

Expected result:

```text
u_vac may only exist where J_V is timelike/nonzero,
or else u_vac requires a separate equilibrium-frame definition.
```

Recommended next script:

```text
candidate_static_source_neutrality_for_J_V.py
```

---

### 15.5 `candidate_static_source_neutrality_for_J_V.py`

Purpose:

```text
Protect ordinary static gravity from scalar volume charge.
```

Main question:

```text
Does the proposed J_V / Sigma_V / R_V structure create exterior scalar charge around static sources?
```

Required ordinary-sector conditions:

```text
Q_volume = 0,
F_scalar_far = 0,
delta M_ext|volume = 0,
static equilibrium has no independent exterior zeta charge.
```

Forbidden outcomes:

```text
static mass creates 1/r zeta tail,
J_V leaks into far-zone scalar flux,
boundary smoothing changes measured mass,
R_V cancels scalar charge by tuning.
```

Expected result:

```text
Either the continuity law is static-neutral,
or it is rejected for ordinary gravity.
```

Recommended next script:

```text
candidate_boundary_no_overlap_for_volume_current.py
```

---

### 15.6 `candidate_boundary_no_overlap_for_volume_current.py`

Purpose:

```text
Ensure J_V-driven zeta enters metric only through allowed channels.
```

Main question:

```text
Does volume exchange double-count B_s, zeta residual, kappa residual, or exterior mass?
```

Required conditions:

```text
zeta may become B_s companion only if residual zeta trace is killed/non-metric,
kappa remains diagnostic/non-metric unless separately proven,
J_V does not create independent residual metric trace,
boundary flux is compact or neutral,
P_boundary and P_recombination remain active guardrails.
```

Expected result:

```text
No-overlap becomes a theorem target tied to J_V, not just a projector slogan.
```

Recommended next script:

```text
candidate_exchange_continuity_checkpoint.py
```

---

### 15.7 `candidate_exchange_continuity_checkpoint.py`

Purpose:

```text
Decide whether the exchange-continuity branch is alive.
```

Main question:

```text
Do we have enough to promote J_V from theorem target to candidate current?
```

Checkpoint table:

```text
Sigma_V defined?
R_V defined?
Flux direction defined?
Timelike/nonzero domain defined?
Static-source neutrality passed?
Boundary/no-overlap passed?
Sign/orientation defined?
Chi-origin still honest?
Recovery checks kept downstream?
```

Possible outcomes:

```text
PROMOTE_JV_CANDIDATE:
  if all required structures exist.

DEFER_JV:
  if one or two concrete pieces remain missing.

KILL_DECORATIVE_CONTINUITY:
  if J_V remains a name.

RETURN_TO_POSTULATES:
  if exchange continuity cannot be written without arbitrary structure.
```

---

## Optional Scripts

These should only be written if needed.

### `candidate_zeta_gradient_current_limit.py`

Use only if the zeta-gradient current remains tempting:

\[
J_V^\mu=\beta_z\nabla^\mu\zeta.
\]

Purpose:

```text
test whether grad zeta can be timelike/nonzero in the needed regimes.
```

Likely result:

```text
RISK / limited diagnostic,
not general u_vac definition.
```

---

### `candidate_equilibrium_frame_without_JV.py`

Use only if \(J_V\) is zero in static equilibrium but a rest frame is still needed.

Purpose:

```text
test whether vacuum equilibrium defines u_vac without active flux.
```

Risk:

```text
could become arbitrary preferred slicing.
```

---

### `candidate_chi_origin_for_source_volume_coupling.py`

Use only after \(\Sigma_V\) is structurally defined.

Purpose:

```text
test whether chi has ontology/source-coupling origin,
or remains recovery fit.
```

---

## Recommended Group 15 Endpoint

Group 15 should end when one of these is true.

### Endpoint A: Current Defined

```text
J_V is a candidate real vacuum-volume current.
u_vac can be defined as normalized J_V on a stated domain.
Exchange continuity is a candidate law.
```

Next group would then be:

```text
16_volume_exchange_to_spatial_trace_recombination
```

Purpose:

```text
test whether the defined J_V/u_vac/Sigma_V/R_V system can actually support A_spatial without double-counting.
```

### Endpoint B: Current Not Defined

```text
J_V remains decorative or circular.
u_vac remains undefined.
Acceleration-gradient volume creation remains a theorem target.
A_spatial remains recovery theorem target.
```

Next group should then be:

```text
16_postulate_level_vacuum_exchange_derivation
```

Purpose:

```text
return upstream and derive the missing vacuum-volume current from ontology,
rather than continuing field-equation scaffolding.
```

### Endpoint C: Branch Rejected

```text
exchange continuity creates scalar charge,
requires arbitrary preferred frame,
or cannot avoid double-counting.
```

Next group should then be:

```text
16_A_spatial_recovery_without_volume_current
```

Purpose:

```text
look for a different origin of spatial trace,
with volume-current branch killed under ordinary-regime constraints.
```

---

## Recommended First Artifact

After the first script, write:

```text
candidate_exchange_continuity_law_for_volume.md
```

It should be compact and should not overclaim. It should say:

```text
exchange continuity is the right locked door,
but not yet a law.

J_V needs flux direction,
Sigma_V and R_V must be split,
and recovery checks remain downstream.
```

---

## Final Plan Summary

Group 15 should be short compared with Group 14.

It has one locked door:

```text
Can a real exchange continuity law define J_V?
```

Its first three scripts should be:

```text
candidate_exchange_continuity_law_for_volume.py
candidate_sigma_R_split_for_volume_exchange.py
candidate_volume_flux_direction_law.py
```

Then it should test viability:

```text
candidate_timelike_domain_for_volume_current.py
candidate_static_source_neutrality_for_J_V.py
candidate_boundary_no_overlap_for_volume_current.py
candidate_exchange_continuity_checkpoint.py
```

If \(J_V\) is still unnamed after those, stop.

Dragon counsel:

```text
Do not build a palace around a missing current.
Find the current, or mark the empty riverbed.
```
