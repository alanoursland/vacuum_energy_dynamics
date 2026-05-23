# 13 Vacuum Substance Accounting Plan

## Recommended Directory Name

Recommended:

```text
13_vacuum_substance_accounting
```

This is still the best name.

Reason:

```text
The next unresolved object is not merely an energy term.
It is the accounting structure for vacuum-as-spacetime:
  E_vac_config,
  q_v,
  J_v,
  scalar/trace conversion,
  relaxation exchange,
  ordinary closed-regime conservation,
  and active creation regimes.
```

Alternative names:

```text
13_vacuum_configuration_accounting
13_vacuum_exchange_accounting
13_vacuum_substance_energy
13_relaxation_exchange_closure
13_vacuum_spacetime_accounting
13_volume_configuration_accounting
```

Best name:

```text
13_vacuum_substance_accounting
```

Possible later rename if the ontology sharpens:

```text
13_vacuum_spacetime_accounting
```

---

## One-Line Goal

Group 13 should define or constrain the accounting variables needed to make vacuum-substance exchange mathematically real rather than a repair reservoir.

The central target is:

```text
E_vac_config is not a thermodynamic bucket.
It is a spacetime / volume / metric-configuration variable.
```

---

## Corrected Ontology To Carry Forward

The corrected ontology is:

```text
vacuum is spacetime.
creating vacuum creates spacetime.
changing local spacetime creates curvature.
```

Therefore:

```text
vacuum configuration accounting is geometric accounting.
```

Do not treat \(E_{\rm vac,config}\) as a separate material reservoir unless the math forces that language.

Better working phrase:

```text
vacuum-spacetime configuration variable
```

or:

```text
volume-form configuration variable
```

The scalar/trace conversion picture is:

```text
curvature excess deposits into vacuum-spacetime configuration,
curvature deficit pulls from vacuum-spacetime configuration,
and both move the local geometry toward its equilibrium configuration.
```

This is not ordinary damping.

It is not a second-order scalar wave with friction.

It is closer to:

```text
conversion-limited scalar disturbance,
non-inertial scalar reconfiguration,
vacuum-volume absorption,
or constraint-mediated scalar conversion.
```

---

## Core Question

The group should answer:

```text
What is the geometric variable that receives scalar/trace conversion?
```

Candidate targets include:

\[
\sqrt{\gamma}
\]

the spatial volume element,

\[
\ln\sqrt{\gamma}
\]

local volume strain,

\[
\det\gamma_{ij}
\]

spatial metric determinant,

\[
\Omega
\]

a conformal / volume factor,

\[
\kappa
\]

the trace / volume mismatch variable,

or a constrained combination such as:

\[
\epsilon_{\rm vac,config}
\sim
F(\sqrt{\gamma},\kappa,\kappa_{\min},A,B).
\]

The group should not assume the answer.

It should test candidates.

---

## Main Discipline

Group 13 must not let \(E_{\rm vac,config}\) become:

```text
a magic energy reservoir,
a coefficient tuning knob,
a hidden Sigma_creation term,
a duplicate A-sector mass charge,
an acausal transport channel,
or a way to claim near-boundary predictions before observables exist.
```

The goblin warning:

```text
No bottomless bucket.
If vacuum is spacetime, name the geometry.
```

---

# Proposed Study Sequence

## 1. candidate_vacuum_substance_accounting_inventory.py

Purpose:

```text
Inventory all variables and balances needed to make E_vac_config / q_v / J_v more than a repair reservoir.
```

This is the recommended first script.

Questions:

```text
What variables are already named?
What variables are still undefined?
Which are geometric?
Which are bookkeeping?
Which are forbidden to carry exterior mass?
Which are forbidden to act as creation?
Which are allowed to exchange with kappa?
```

Expected inventory:

```text
epsilon_vac_config
q_v
J_v
E_kappa
kappa
kappa_min
sqrt(gamma)
ln sqrt(gamma)
Sigma_exchange
Sigma_creation
Gamma_relax
M_ext
A_flux
P_trace
P_relax
P_boundary
P_recombination
```

Expected artifact:

```text
candidate_vacuum_substance_accounting_inventory.md
```

Success condition:

```text
A clean variable ledger separating geometric variables, bookkeeping variables, forbidden roles, and missing definitions.
```

---

## 2. candidate_volume_form_configuration_variable.py

Purpose:

```text
Test whether vacuum configuration should be represented by a volume-form variable.
```

Reason:

```text
If vacuum is spacetime, creating vacuum should change a geometric volume measure.
```

Candidates:

\[
\epsilon_{\rm vac,config}\sim \ln\sqrt{\gamma}
\]

or:

\[
\epsilon_{\rm vac,config}\sim \sqrt{\gamma}-\sqrt{\gamma_0}.
\]

Questions:

```text
Does the variable represent local volume creation?
Does it distinguish trace/volume modes from TT shear?
Does it remain separate from A-sector exterior mass?
Can kappa be interpreted as a volume/trace mismatch?
Does exterior kappa=0 imply no exterior volume charge?
```

Expected artifact:

```text
candidate_volume_form_configuration_variable.md
```

Success condition:

```text
A preferred geometric candidate or an explicit reason volume form is insufficient.
```

---

## 3. candidate_trace_vs_tt_geometric_split.py

Purpose:

```text
Formalize why trace/volume modes convert into vacuum configuration while TT modes propagate.
```

Reason:

```text
This is the possible theorem behind TT-only radiation.
```

Key distinction:

```text
trace / scalar / longitudinal:
  changes volume form or vacuum amount,
  converts into spacetime configuration.

TT:
  volume-preserving shear,
  reshapes vacuum without creating/destroying it,
  can propagate.
```

Mathematical handles:

\[
\delta\ln\sqrt{\gamma}
=
\frac12\gamma^{ij}\delta\gamma_{ij}.
\]

For TT perturbations:

\[
\gamma^{ij}h_{ij}^{TT}=0.
\]

Therefore:

\[
\delta\ln\sqrt{\gamma}\big|_{TT}=0.
\]

Questions:

```text
Can the trace/TT split explain scalar absorption?
Can TT-only radiation be derived from volume preservation?
Does this distinguish vacuum creation from vacuum shear?
```

Expected artifact:

```text
candidate_trace_vs_tt_geometric_split.md
```

Success condition:

```text
A structural theorem target:
TT modes are volume-preserving;
trace modes are vacuum-volume-changing and therefore conversion-limited.
```

---

## 4. candidate_scalar_conversion_not_damping.py

Purpose:

```text
Replace the loose phrase "critical damping" with a sharper scalar-conversion model.
```

Reason:

```text
The scalar disturbance may not be a damped wave.
It may be converted into the spacetime variable it would propagate through.
```

Questions:

```text
What scalar quantity is consumed?
What geometric quantity increases?
Is there any second-order scalar mode at all?
Is the scalar sector constraint-mediated rather than wave-mediated?
What would scalar leakage mean?
```

Forbidden model unless derived:

\[
\ddot\phi+\gamma\dot\phi+\omega^2\phi=0.
\]

Preferred candidate language:

```text
scalar disturbances are conversion-limited,
not friction-damped waves.
```

Expected artifact:

```text
candidate_scalar_conversion_not_damping.md
```

Success condition:

```text
A clear distinction between damping, relaxation, and conversion.
```

---

## 5. candidate_mass_acceleration_gradient_coupling.py

Purpose:

```text
Find the covariant or reduced expression for "mass accelerating across a gradient."
```

Reason:

```text
This may be the bridge between ontology and field equations.
```

Possible candidates to test:

\[
\rho\,a^\mu\nabla_\mu A,
\]

\[
\rho\,v^i\partial_i A,
\]

\[
T^{\mu\nu}\nabla_\mu\nabla_\nu A,
\]

\[
\nabla_\mu(T^{\mu\nu}\nabla_\nu A),
\]

\[
T^{\mu\nu}P_{\rm trace}\nabla_\mu\nabla_\nu(\text{volume variable}).
\]

Questions:

```text
Is the coupling tied to acceleration, motion through gradient, stress-energy divergence, or trace/volume mismatch?
Does it vanish for geodesic free fall?
Does it represent energy exchange or geometry bookkeeping?
Does it create extra dissipative channels in binaries?
```

Expected artifact:

```text
candidate_mass_acceleration_gradient_coupling.md
```

Success condition:

```text
A short list of viable tensor/reduced coupling forms and exclusions.
```

---

## 6. candidate_binary_radiation_scalar_conversion_safety.py

Purpose:

```text
Check whether scalar/trace conversion creates an extra orbital-energy-loss channel.
```

Reason:

```text
Binary pulsar and gravitational-wave observations strongly constrain extra radiation / dissipation.
```

Current safe rule:

```text
ordinary far-zone radiation is TT-only.
```

Group 13 must ask:

```text
Is vacuum-spacetime conversion conservative/local bookkeeping,
or does it remove orbital energy as an extra channel?
```

Questions:

```text
Does scalar conversion occur only as local geometry bookkeeping already counted in conservative motion?
Does it produce far-zone flux?
Does it accumulate near sources?
Does it vanish or average out in periodic orbital motion?
Does it alter quadrupole radiation predictions?
```

Expected artifact:

```text
candidate_binary_radiation_scalar_conversion_safety.md
```

Success condition:

```text
A safety ledger for why scalar/trace conversion does not violate TT-radiation observations, or a clear risk flag.
```

---

## 7. candidate_boundary_volume_mode_no_exterior_charge.py

Purpose:

```text
Try the concrete theorem target:
local trace/volume reconfiguration has zero exterior scalar charge.
```

This is the most important concrete derivation target in the group.

Reason:

```text
It tests whether vacuum-as-spacetime produces a real mathematical constraint rather than more vocabulary.
```

Target theorem:

```text
A local volume-form / kappa reconfiguration changes interior spacetime configuration
but has zero exterior scalar charge, so A-sector exterior flux remains fixed.
```

Equivalent conditions:

\[
\delta M_{\rm ext}\big|_{\kappa{\rm\ or\ volume\ reconfiguration}}=0.
\]

\[
Q_\kappa=0.
\]

\[
F_\kappa(R+)=0.
\]

\[
\kappa_{\rm ext}=0.
\]

Questions:

```text
Can this be shown by compact support?
By compensated source projection?
By volume-form boundary conditions?
By trace/TT decomposition?
By parent projector structure?
```

Expected artifact:

```text
candidate_boundary_volume_mode_no_exterior_charge.md
```

Success condition:

```text
A theorem candidate or no-go result for boundary mass preservation.
```

---

## 8. candidate_vacuum_transport_current_constraints.py

Purpose:

```text
Constrain J_v so vacuum-substance exchange does not become acausal or arbitrary.
```

Reason:

```text
If q_v/J_v are used, they need transport rules or constraint status.
```

Questions:

```text
Is J_v a physical transport current?
Is it a constraint-current?
Is it local?
Does it propagate?
Does it have a speed?
Can it cross boundaries?
Can it change exterior mass?
```

Possible regimes:

```text
local exchange only:
  J_v=0 or compact support.

constraint redistribution:
  J_v nonlocal but not radiative.

transport current:
  J_v obeys causal law.
```

Expected artifact:

```text
candidate_vacuum_transport_current_constraints.md
```

Success condition:

```text
A classification of q_v/J_v as local, constrained, or transport variables.
```

---

## 9. candidate_vacuum_accounting_parent_balance.py

Purpose:

```text
Write the first more concrete vacuum-substance accounting balance.
```

Candidate shape:

\[
u^\mu\nabla_\mu \epsilon_{\rm vac,config}
+
\nabla_\mu J_v^\mu
=
-\Gamma_{\rm relax}
+
\Sigma_{\rm exchange}
\]

with ordinary closure:

\[
\Sigma_{\rm creation}=0.
\]

But the signs and terms must be tested.

Questions:

```text
What is exchanged with E_kappa?
What is exchanged with matter?
What is exchanged with A-sector geometry?
What is forbidden from changing M_ext?
What is local versus boundary-supported?
```

Expected artifact:

```text
candidate_vacuum_accounting_parent_balance.md
```

Success condition:

```text
A candidate balance law that is more concrete than the group-12 template but still honestly labeled.
```

---

## 10. vacuum_substance_accounting_summary.md

Purpose:

```text
Summarize group 13.
```

This should answer:

```text
What is the best candidate for E_vac_config?
Is it geometric?
Is it local?
Is q_v/J_v needed?
Is scalar conversion distinct from damping?
Does trace/TT splitting explain TT-only radiation?
Can boundary volume reconfiguration preserve exterior mass?
Is mass-acceleration-gradient coupling identified?
Does binary radiation safety survive?
```

Expected status:

```text
probably still unfinished,
but with E_vac_config much less vague.
```

---

# Proposed File List

Recommended group file sequence:

```text
candidate_vacuum_substance_accounting_inventory.py
candidate_vacuum_substance_accounting_inventory.md

candidate_volume_form_configuration_variable.py
candidate_volume_form_configuration_variable.md

candidate_trace_vs_tt_geometric_split.py
candidate_trace_vs_tt_geometric_split.md

candidate_scalar_conversion_not_damping.py
candidate_scalar_conversion_not_damping.md

candidate_mass_acceleration_gradient_coupling.py
candidate_mass_acceleration_gradient_coupling.md

candidate_binary_radiation_scalar_conversion_safety.py
candidate_binary_radiation_scalar_conversion_safety.md

candidate_boundary_volume_mode_no_exterior_charge.py
candidate_boundary_volume_mode_no_exterior_charge.md

candidate_vacuum_transport_current_constraints.py
candidate_vacuum_transport_current_constraints.md

candidate_vacuum_accounting_parent_balance.py
candidate_vacuum_accounting_parent_balance.md

vacuum_substance_accounting_summary.md
```

---

# Recommended First Script

Start with:

```text
candidate_vacuum_substance_accounting_inventory.py
```

Reason:

```text
Before testing volume forms or trace/TT theorems,
inventory every variable and forbid the dangerous roles.
```

The first script should output:

```text
a variable ledger:
  name,
  geometric interpretation,
  allowed exchange,
  forbidden role,
  status,
  missing definition,
  next test.
```

---

# What Would Count as Success for Group 13

Minimal success:

```text
E_vac_config is no longer a vague reservoir.
```

Better success:

```text
E_vac_config is tied to a geometric candidate such as volume-form strain.
```

Strong success:

```text
Trace / scalar conversion is linked to volume-form change,
while TT modes are shown to be volume-preserving.
```

Very strong success:

```text
Boundary volume reconfiguration is shown to have zero exterior scalar charge.
```

Best possible success:

```text
A concrete vacuum accounting balance emerges that can feed the parent identity.
```

---

# What Would Count as Failure

Group 13 fails if:

```text
E_vac_config remains an unnamed bucket,
q_v duplicates rho,
J_v hides acausal transport,
vacuum accounting changes exterior M_ext,
Gamma_relax acts like Sigma_creation,
scalar conversion becomes an extra radiation/dissipation channel,
or coefficients are tuned using vacuum accounting.
```

---

# Current Recommendation

Use:

```text
13_vacuum_substance_accounting
```

Start with:

```text
candidate_vacuum_substance_accounting_inventory.py
```

Main concrete target:

```text
candidate_boundary_volume_mode_no_exterior_charge.py
```

Main conceptual target:

```text
candidate_trace_vs_tt_geometric_split.py
```

Main ontology-to-equation bridge:

```text
candidate_mass_acceleration_gradient_coupling.py
```

Final warning:

```text
Do not model scalar conversion as ordinary damping unless the equations force it.
It may be a conversion of would-be scalar propagation into spacetime configuration.
