# 57_layer_unify_probe — Plan

## Purpose

Group 57 starts the finite transition-layer unification probe.

The current snapshot says the reduced static spherical A-sector remains the strongest reconstructed branch, while recombination, boundary behavior, source neutrality, mass neutrality, divergence safety, and parent readiness remain unresolved. Group 56 constructed a reduced silent/inert theorem surface, but it is not an insertion law and not a covariant theorem.

The new idea is that the interior and exterior laws may be asymptotic faces of one underlying rule, while the boundary layer is where the full mixed rule becomes visible.

Group 57 should therefore stop treating the boundary only as a hard junction. It should model a finite layer:

```text
R - ell <= r <= R + ell
```

and compute the residue terms created when an interior profile is smoothly blended into an exterior profile.

The layer is not a patch. It is a diagnostic laboratory for the missing unified rule.

## Group Name

```text
57_layer_unify_probe
```

Short name chosen to avoid Windows/archive path overflow.

## Central Question

```text
When interior and exterior reduced laws are smoothly blended across a finite layer,
what residue terms appear, and can they be finite, localized, neutral, and divergence-compatible?
```

## Starting State

Group 57 imports the Group 56 status:

```text
reduced silent/inert theorem surface constructed;
boundary-null profile exists;
charge-neutral profile exists;
exterior tail can vanish for C0=0,Q=0;
shell-neutral match exists in reduced hard-boundary form;
reduced divergence-silent closure exists;
no insertion occurred;
covariant lift and actual insertion law remain required.
```

Group 57 uses that as a base, but changes the boundary picture from:

```text
hard matching at R
```

to:

```text
finite transition layer around R.
```

## Desired Outcome

Best possible useful result:

```text
A finite smooth transition layer can be modeled with a quintic smoothstep.
The blended field is continuous with vanishing first and second derivative mismatch at layer endpoints.
Differential residues are localized in the layer and explicit.
Layer gradient energy is finite and localized.
Layer charge/mass diagnostics can be stated explicitly.
A reduced divergence-compatible closure can be written for the layer stress.
The transition-layer route survives conditionally as a unification probe.
No insertion, active O, recombination, or parent closure opens.
```

A possible negative result:

```text
Blending inevitably creates unavoidable scalar charge, mass shift, boundary energy divergence,
or divergence failure, so the silent non-O route is obstructed.
```

Either result is real progress.

## What This Group May Do

Group 57 may:

```text
construct a finite-layer coordinate x=(r-(R-ell))/(2ell);
construct a quintic smoothstep s(x)=10x^3-15x^4+6x^5;
verify s, s', and s'' endpoint behavior;
blend interior and exterior reduced profiles;
compute first and second derivative blending residues;
compute reduced layer gradient energy;
compute reduced net layer charge and mass-shift diagnostics;
compute a reduced divergence-silent layer stress closure;
classify whether the finite-layer route survives conditionally.
```

## What This Group Must Not Do

Group 57 must not:

```text
adopt Package B;
choose B_s_metric or b_s_scale;
fix numeric d;
insert B_s/F_zeta into a field equation;
claim a covariant parent equation;
claim full boundary theorem;
construct active O;
use the layer as a hidden source, hidden shell, hidden mass, or repair term;
open recombination;
open parent closure.
```

## Recommended Script Batch

```text
candidate_layer_problem.py
candidate_smoothstep_profile.py
candidate_blend_residue.py
candidate_layer_energy.py
candidate_layer_charge_mass.py
candidate_layer_divergence.py
candidate_layer_route_classifier.py
candidate_layer_batch_reconcile.py
order.txt
```

## Script Intent

### 1. candidate_layer_problem.py

Open the finite-layer unification probe and declare the allowed scope.

### 2. candidate_smoothstep_profile.py

Construct the layer coordinate and smoothstep:

```text
x=(r-(R-ell))/(2ell)
s(x)=10x^3-15x^4+6x^5
```

Verify endpoint behavior:

```text
s(0)=0
s(1)=1
s'(0)=s'(1)=0
s''(0)=s''(1)=0
```

This replaces hard matching with a smooth finite layer.

### 3. candidate_blend_residue.py

Blend interior and exterior reduced profiles:

```text
F=(1-s)F_in+sF_out
```

Compute derivative residues:

```text
F' - [(1-s)F_in' + sF_out']
F'' - [(1-s)F_in'' + sF_out'']
```

These residues contain the transition terms that a unified rule must explain.

### 4. candidate_layer_energy.py

Compute reduced gradient energy density and layer-local support indicators:

```text
E_grad ~ (F')^2
E_res ~ residue^2
```

The goal is to state finite localized layer energy conditions.

### 5. candidate_layer_charge_mass.py

Compute a reduced net layer charge diagnostic:

```text
Q_layer = integral r^2 rho_layer dr
```

and a mass-shift diagnostic:

```text
Delta_M_layer = alpha Q_layer
```

Classify zero-charge or charge-neutral profile conditions.

### 6. candidate_layer_divergence.py

Construct a reduced divergence-silent stress closure for a layer stress profile:

```text
D=p_r'+2(p_r-p_t)/r
p_t=p_r+r*p_r'/2
```

using a layer-local radial pressure profile.

### 7. candidate_layer_route_classifier.py

Classify whether the finite transition-layer route survives conditionally.

### 8. candidate_layer_batch_reconcile.py

Prepare result notes and summary.

## Expected Summary Shape

Likely result:

```text
Group 57 modeled a finite transition layer with smooth endpoint behavior.
Blending residues were made explicit.
The residues are localized and can be treated as candidate layer-response terms.
Layer energy/charge/mass/divergence conditions are explicit.
The layer route survives conditionally as a unification probe, but no parent equation or insertion opens.
```

## Safe Handoff Options

Depending on outputs, Group 58 could be:

```text
58_layer_energy_accounting
58_layer_candidate_terms
58_covariant_layer_lift
58_active_o_necessity_audit
```

The handoff must follow actual Group 57 results.
