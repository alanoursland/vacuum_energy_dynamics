# Candidate J_V Mass Neutrality Conditions

## Canonical Filename

```text
candidate_JV_mass_neutrality_conditions.md
```

This document summarizes the output of:

```text
candidate_JV_mass_neutrality_conditions.py
```

## What This Document Is

This document is the sixth artifact in `21_source_routing_and_mass_neutrality/`.

It is not a definition of `J_V`, `J_sub`, `J_exch`, `Sigma/R`, `u_vac`, a vacuum-current flux law, a source-side operator, a boundary law, or a parent field equation.

Its purpose is to audit whether the unresolved vacuum-current language can remain ordinary-sector mass-neutral without becoming a hidden exterior mass route.

The locked-door question was:

```text
Can J_V, J_sub, or J_exch be ordinary-sector mass-neutral?
```

The result is conservative:

```text
J_V remains unresolved.

J_sub and J_exch remain role-level only.

A J_V-induced 1/r scalar residue would carry exterior scalar flux.

A 1/r^2 far-zone current profile carries a constant sphere flux.

Sigma/R zero-net exchange remains a theorem target, not a declaration.

No vacuum-current branch is licensed as an ordinary exterior mass carrier.
```

Tiny goblin label:

```text
Pure wind is not gravity.
Exchange is not repair.
Undefined current carries no mass coin.
```

---

## Archive Status

The run reported a clean dependency check.

```text
zeta_kappa_inventory_dependency_21: dependency_satisfied
zeta_tail_flux_dependency_21: dependency_satisfied
kappa_tail_flux_dependency_21: dependency_satisfied
A_sector_mass_definition_dependency_21: dependency_satisfied
```

The archive chain therefore reached the J_V/current audit through the zeta/kappa residual audit and the A-sector reference mass definition.

---

## Core Diagnostics

### J_V Scalar Residue

The script tested a generic scalar residue that an unresolved vacuum current could leave behind:

\[
\phi_{JV}(r)=\frac{C_{JV}}{r}.
\]

The reduced surface flux is:

\[
F_{\phi JV}=4\pi r^2\phi_{JV}'=-4\pi C_{JV}.
\]

If incorrectly read as an A-like exterior mass contribution, this would correspond to the diagnostic mass shift:

\[
\delta M_{JV}^{\rm like}
=
\frac{c^2}{8\pi G}F_{\phi JV}
=
-\frac{C_{JV}c^2}{2G}.
\]

This is not a licensed J_V mass law. It is a danger witness showing that a nonzero `C_JV` would behave like a hidden second mass coin.

The run recorded:

```text
F_phi_JV = -4*pi*C_JV

delta_M_JV_like = -C_JV*c**2/(2*G)
```

### Far-Zone Current Flux

The script then tested generic far-zone radial current profiles:

\[
j_V^r=\frac{I_V}{4\pi r^2},
\qquad
j_{sub}^r=\frac{I_{sub}}{4\pi r^2},
\qquad
j_{exch}^r=\frac{I_{exch}}{4\pi r^2}.
\]

Their sphere fluxes are:

\[
\Phi_{JV}=I_V,
\qquad
\Phi_{Jsub}=I_{sub},
\qquad
\Phi_{Jexch}=I_{exch}.
\]

Thus ordinary exterior current-flux silence requires the relevant far-zone current coefficient to vanish unless a future current theorem derives a neutral transport interpretation.

### Zero-Net Exchange Diagnostic

The role-level neutral exchange target was represented as:

\[
\Sigma_0-R_0=0.
\]

The script recorded this as a diagnostic target, not a source law. `Sigma/R` still need operators, signs, strengths, domains, and boundary behavior before zero-net exchange can become a theorem.

---

## Condition Ledger

| Entry | Sector | Status | Consequence |
|---|---|---|---|
| JV1 | `J_V` | UNRESOLVED | `J_V` cannot carry ordinary exterior mass while undefined. |
| JV2 | `J_V` scalar residue | THEOREM_TARGET | `J_V` must not leave a hidden `1/r` scalar tail. |
| JV3 | `J_V` far-zone flux | THEOREM_TARGET | A far-zone vacuum current cannot become a second mass flux coin. |
| JV4 | `u_vac / J_V` domain | UNRESOLVED | No frame field can rescue mass routing while `J_V` is undefined. |
| JS1 | `J_sub` pure wind | ROLE_LEVEL | Pure wind is not gravity without an independent theorem. |
| JS2 | `J_sub` scalar trace leakage | THEOREM_TARGET | Substrate-current labels cannot hide a scalar mass route. |
| JS3 | `J_sub` boundary repair | REJECTED | `J_sub` cannot be a boundary purse. |
| JE1 | `J_exch` exchange current | ROLE_LEVEL | Exchange is not an ordinary mass route by vocabulary. |
| JE2 | `J_exch` repair current | REJECTED | Exchange cannot fix ordinary-sector failures after the fact. |
| SR1 | `Sigma_V / R_V` zero-net branch | THEOREM_TARGET | Zero-net exchange is promising but not a theorem here. |
| SR2 | zero-creation ordinary branch | CANDIDATE | Zero-creation remains a safe candidate, not a derived law. |
| SR3 | latent exchange branch | SAFE_IF | Latent exchange may remain bookkeeping only if it has no source, metric, boundary, or mass effect. |

---

## Rejected Vacuum-Current Mass Routes

The script rejected the following current-based routes as ordinary-sector mass mechanisms:

```text
undefined J_V mass current,
J_V scalar 1/r residue,
pure wind gravitates by existence,
exchange repair current,
Sigma/R tuning knob,
recovery-chosen u_vac.
```

These are not runtime failures. They are expected governance exclusions preserving the Group 21 rule that non-A sectors must not become second mass channels by declaration.

---

## What This Study Established

This study established reduced diagnostic witnesses for vacuum-current mass leakage:

\[
\phi_{JV}=\frac{C_{JV}}{r}
\quad\Rightarrow\quad
F_{\phi JV}=-4\pi C_{JV}.
\]

\[
j^r=\frac{I}{4\pi r^2}
\quad\Rightarrow\quad
\Phi_J=I.
\]

It also recorded the role-level zero-net exchange target:

\[
\Sigma_0-R_0=0.
\]

The operational conditions for ordinary-sector current neutrality are:

```text
C_JV = 0 for scalar residue silence,
I_V = I_sub = I_exch = 0 for no independent far-zone current flux,
Sigma/R operators before any zero-net exchange claim,
no boundary repair,
no source repair,
no matter rerouting,
no preferred-frame force,
no recovery-chosen u_vac.
```

---

## What This Study Did Not Establish

This study did not define `J_V`.

It did not define `J_sub` or `J_exch` as physical currents.

It did not derive `Sigma/R` operators.

It did not derive zero-net exchange.

It did not define `u_vac`.

It did not prove pure-wind neutrality.

It did not prove current-sector scalar silence.

It did not prove boundary neutrality.

It did not modify the A-sector mass charge.

---

## Current Safe Position

The current safe position is:

```text
J_V remains unresolved.

J_sub and J_exch remain role-level bookkeeping.

Zero-net and zero-creation ordinary branches remain theorem-targeted or candidate routes.

Vacuum-current labels do not carry ordinary exterior mass.
```

---

## Next Development Target

The next script should be:

```text
candidate_curvature_accounting_mass_neutrality.py
```

Purpose:

```text
Protect curvature admissibility, curvature energy, and unresolved curvature currents
from becoming hidden exterior mass sources or repair mechanisms.
```
