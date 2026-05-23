# Candidate Boundary Flux Mass Preservation

## Canonical Filename

```text
candidate_boundary_flux_mass_preservation.md
```

This document summarizes the output of:

```text
candidate_boundary_flux_mass_preservation.py
```

## What This Document Is

This document is the fourth artifact for `21_source_routing_and_mass_neutrality/`.

It is not a boundary theorem, not a matching law, not a shell-source law, not a no-overlap proof, not a smoothing mechanism, and not a parent field equation.

Its purpose is to test the reduced mass danger of boundary or smoothing behavior before allowing any non-A boundary contribution to be treated as neutral.

The locked-door question was:

```text
Can boundary or smoothing behavior preserve A-sector mass without repair?
```

The result is:

```text
A non-A boundary contribution with an exterior 1/r coefficient shifts A-flux.

For

  delta_A_boundary = q/r

one obtains

  delta_F_A = -4*pi*q
  delta_M_A = -c^2*q/(2*G)

Therefore the reduced boundary-tail neutrality condition is

  q = 0

unless a future parent/source identity derives a new mass law without double counting.
```

Tiny goblin label:

```text
No boundary purse.
No shell coin.
No smoothing spoon.
```

---

## Archive Status

The run had clean upstream dependencies:

```text
residual_scalar_tail_flux_dependency_21: dependency_satisfied
residual_scalar_zero_flux_condition_dependency_21: dependency_satisfied
A_sector_mass_definition_dependency_21: dependency_satisfied
```

So this run had no missing-parent archive issue.

---

## Core Reduced Boundary Witness

The script takes a generic exterior non-A boundary contribution:

\[
\delta A_{\rm boundary}(r)=\frac{q}{r}.
\]

The A-flux shift is:

\[
\delta F_A
=4\pi r^2 \frac{d}{dr}\left(\frac{q}{r}\right)
=-4\pi q.
\]

The corresponding A-sector mass-charge shift, if this contribution were allowed to behave as an A-like exterior mass contribution, is:

\[
\delta M_A
=\frac{c^2}{8\pi G}\delta F_A
=-\frac{c^2 q}{2G}.
\]

The run recorded the residual checks:

```text
delta_F_A + 4*pi*q = 0
delta_M_A + c^2*q/(2*G) = 0
```

The neutrality condition is:

\[
q=0.
\]

Interpretation:

```text
A non-A boundary or smoothing contribution with a nonzero exterior 1/r coefficient changes the A-sector mass charge.
```

---

## Boundary Profile Diagnostics

The script tested three toy profile classes. These are diagnostic examples, not derived boundary laws.

### C1-style profile

\[
\phi_{C1}(r)=\phi_0\left(1-\frac{r}{R}\right).
\]

At the boundary:

```text
phi_C1(R) = 0
phi_C1'(R) = -phi0/R
boundary flux at R = -4*pi*R*phi0
```

This shows that value-continuity alone is not enough. A profile can vanish at the boundary while still carrying nonzero boundary flux.

### C2-style profile

\[
\phi_{C2}(r)=\phi_0\left(1-\frac{r}{R}\right)^2.
\]

At the boundary:

```text
phi_C2(R) = 0
phi_C2'(R) = 0
boundary flux at R = 0
```

This is safer as a diagnostic profile because both value and first derivative vanish at the boundary.

### Smooth compact toy profile

\[
\phi_{\rm compact}(r)=\phi_0\left(1-\frac{r^2}{R^2}\right)^2.
\]

At the boundary:

```text
phi_compact(R) = 0
phi_compact'(R) = 0
boundary flux at R = 0
```

This is also safer as a diagnostic profile.

Important caveat:

```text
Compact support and smoothing must be derived, not chosen after recovery failure.
```

---

## Boundary Branch Ledger

| Entry | Branch | Status | Result |
|---|---|---|---|
| BND1 | smooth compact residual | SAFE_IF | Safe only as diagnostic/sample until a compact-support law is derived |
| BND2 | C1 residual profile | RISK | Value matches at boundary but derivative/flux may be nonzero |
| BND3 | C2 residual profile | SAFE_IF | Value and first derivative vanish in the toy profile |
| BND4 | boundary shell source | REJECTED | Hidden shell source cannot preserve ordinary mass |
| BND5 | surface counterterm | REJECTED | Counterterm selected after leakage is repair, not theorem |
| BND6 | diagnostic boundary audit | SAFE_IF | Safe only if it has no source, metric, flux, or recovery effect |
| BND7 | residual-kill convention | PROVISIONAL | Safer than residual mass, but not a derived no-overlap theorem |
| BND8 | neutral residual theorem target | THEOREM_TARGET | Desired future theorem: \(\delta F_A|_{boundary,non-A}=0\) with no shell and no recovery tuning |

The run populated this ledger and reported it as complete.

---

## Rejected Boundary Repair Routes

The script rejected these repair routes:

```text
boundary repair current,
R_V boundary cancellation,
H boundary counterterm,
curvature boundary rescue,
recovery-tuned smoothing,
sharp support hiding shell charge.
```

The shared reason is:

```text
A repair route that cancels leakage after it appears is not a mass-preservation theorem.
```

---

## Failure Controls

The boundary flux mass-preservation audit fails if a later script allows:

```text
1. non-A boundary behavior to change exterior A' or A-flux,
2. a smoothing layer to tune M_ext after recovery failure,
3. a shell source or derivative jump to hide mass leakage,
4. R_V, J_exch, curvature balance, or H to act as boundary repair,
5. compact support to be imposed without matching and no-shell conditions,
6. residual-kill to be treated as a derived boundary theorem,
7. boundary conditions to be chosen by Schwarzschild/PPN/AB recovery,
8. O to enforce boundary neutrality without domain/kernel/image/boundary law.
```

The run opened the proof obligation:

```text
derive boundary mass-preservation theorem
```

with the requirement:

```text
show delta F_A|boundary,non-A = 0 with no shell source, no repair current, and no recovery tuning.
```

---

## What This Study Established

This study established the reduced boundary-tail warning:

\[
\delta A_{\rm boundary}=\frac{q}{r}
\quad\Rightarrow\quad
\delta F_A=-4\pi q
\quad\Rightarrow\quad
\delta M_A=-\frac{c^2q}{2G}.
\]

Therefore:

```text
A non-A boundary or smoothing contribution with q != 0 shifts the A-sector mass charge.
```

It also showed, using toy profiles, that:

```text
boundary value matching is not enough;
boundary flux neutrality requires derivative/slope control;
compact or C2-like toy profiles can be flux-neutral in the sample;
but such profiles are not mechanism derivations.
```

---

## What This Study Did Not Establish

This study did not derive boundary mass preservation.

It did not derive compact support.

It did not derive a smoothing law.

It did not derive no-shell matching.

It did not derive residual-kill.

It did not make `R_V`, `J_exch`, curvature balance, or `H` into boundary repair mechanisms.

It did not define a no-overlap operator.

It did not make the parent equation ready.

---

## Governance Status

The script recorded the licensed reduced warning claim:

```text
boundary_tail_A_flux_shift_rule_21
```

with supporting derivations:

```text
boundary_tail_delta_A_flux_21
boundary_tail_delta_MA_21
boundary_tail_zero_flux_condition_21
```

It also recorded the policy claim:

```text
boundary_mass_preservation_requirement_21
```

and the route:

```text
boundary_flux_mass_preservation_audit_route_21
```

The branch-level repair exclusions remain governance claims backed by reduced witnesses and requirements, not complete theorems.

---

## Next Development Target

The next script should be:

```text
candidate_zeta_kappa_mass_neutrality_conditions.py
```

Purpose:

```text
Apply the scalar-tail and boundary-flux rules to residual trace variables zeta and kappa.
```

Expected result:

```text
Residual-kill / non-metric residual remains the safest convention.
Neutral residual metric trace remains theorem-heavy.
No exterior zeta/kappa 1/r tail is licensed.
```
