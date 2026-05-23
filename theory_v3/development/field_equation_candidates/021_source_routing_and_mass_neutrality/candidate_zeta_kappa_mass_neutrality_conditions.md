# Candidate Zeta/Kappa Mass Neutrality Conditions

## Canonical Filename

```text
candidate_zeta_kappa_mass_neutrality_conditions.md
```

This document summarizes the output of:

```text
candidate_zeta_kappa_mass_neutrality_conditions.py
```

## What This Document Is

This document is the fifth artifact for `21_source_routing_and_mass_neutrality/`.

It is not a zeta insertion theorem, not a kappa field equation, not a residual-kill proof, not a no-overlap proof, not a parent mass theorem, and not a license for `Box zeta` or `Box kappa`.

Its purpose is to apply the Group 21 mass-neutrality discipline to the residual trace variables `zeta` and `kappa`.

The locked-door question was:

```text
Under what conditions can zeta/kappa exist without shifting exterior mass?
```

The result is intentionally conservative:

```text
Residual zeta/kappa tails are mass-dangerous if they carry nonzero 1/r coefficients.

Ordinary exterior scalar silence requires:

  C_zeta = 0
  C_kappa = 0

unless the residual variables are strictly non-metric/diagnostic,
killed/suppressed, compact-neutral, or routed through a future parent identity
that avoids double counting.
```

Tiny goblin label:

```text
No trace-tail pockets.
No cancellation cloak.
No Box gremlin.
```

---

## Archive Status

The run was operationally clean. The archive dependency check reported satisfied dependencies for:

```text
residual_scalar_tail_flux_dependency_21
boundary_tail_delta_A_flux_dependency_21
boundary_mass_preservation_inventory_dependency_21
A_sector_mass_definition_dependency_21
```

The warning and failure marks in the body are governance classifications for risk and rejected routes, not runtime errors.

---

## Core Flux Witness

The script considers independent residual exterior tails:

\[
\zeta_{\rm tail}(r)=\frac{C_\zeta}{r},
\]

and:

\[
\kappa_{\rm tail}(r)=\frac{C_\kappa}{r}.
\]

Their reduced surface fluxes are:

\[
F_\zeta
=4\pi r^2\zeta_{\rm tail}'
=-4\pi C_\zeta,
\]

and:

\[
F_\kappa
=4\pi r^2\kappa_{\rm tail}'
=-4\pi C_\kappa.
\]

The run recorded the residual checks:

```text
F_zeta + 4*pi*C_zeta = 0
F_kappa + 4*pi*C_kappa = 0
```

Therefore ordinary exterior scalar silence requires independent vanishing coefficients:

\[
C_\zeta=0,
\qquad
C_\kappa=0.
\]

This is the central reduced witness of the script. It does not by itself derive scalar silence; it defines the condition that a future theorem must satisfy.

---

## A-Like Mass-Shift Diagnostic

The script also computed the danger diagnostic obtained if a residual scalar tail were incorrectly allowed to behave like an A-sector exterior mass contribution.

Using the A-sector mass normalization:

\[
M_A=\frac{c^2}{8\pi G}F_A,
\]

the A-like mass shifts would be:

\[
\delta M_{\zeta,\rm like}
=\frac{c^2}{8\pi G}F_\zeta
=-\frac{c^2 C_\zeta}{2G},
\]

and:

\[
\delta M_{\kappa,\rm like}
=\frac{c^2}{8\pi G}F_\kappa
=-\frac{c^2 C_\kappa}{2G}.
\]

The run recorded:

```text
delta_M_zeta_like + c^2*C_zeta/(2*G) = 0
delta_M_kappa_like + c^2*C_kappa/(2*G) = 0
```

This is not a licensed zeta or kappa mass law. It is a danger diagnostic showing the mass-equivalent size of the leak if residual trace variables were allowed to enter an A-like flux channel.

---

## Cancellation Is Not Sector Neutrality

The script also tested a combined residual tail:

\[
\phi_{zk}(r)=\zeta_{\rm tail}+\kappa_{\rm tail}
=\frac{C_\zeta+C_\kappa}{r}.
\]

Its surface flux is:

\[
F_{zk}=-4\pi(C_\zeta+C_\kappa).
\]

A total-flux cancellation condition would be:

\[
C_\zeta+C_\kappa=0.
\]

But this is not sector neutrality. It can hide nonzero scalar pockets:

\[
C_\zeta\neq0,
\qquad
C_\kappa\neq0,
\qquad
C_\zeta=-C_\kappa.
\]

The script rejected cancellation by hand. Group 21 requires empty pockets, non-metric residuals, compact-neutral residuals, or a future parent theorem with explicit source routing and no double counting.

---

## Condition Ledger

| Entry | Sector | Status | Consequence |
|---|---|---|---|
| ZK1 | zeta residual non-metric branch | SAFE_IF | safest current zeta residual route if it has no source, flux, metric, or A-effect |
| ZK2 | zeta residual exterior-neutral branch | THEOREM_TARGET | possible only if `C_zeta = 0` outside with no shell or recovery-tuned support |
| ZK3 | zeta residual metric 1/r tail | REJECTED | zeta cannot carry the ordinary exterior mass coin by declaration |
| ZK4 | kappa suppressed exterior branch | SAFE_IF | matches current reduced exterior discipline: kappa remains suppressed/diagnostic |
| ZK5 | kappa residual exterior-neutral branch | THEOREM_TARGET | possible only if `C_kappa = 0` outside with no shell or recovery-tuned support |
| ZK6 | kappa residual metric 1/r tail | REJECTED | kappa leak is scalar-silence and equal-response danger |
| ZK7 | e_kappa diagnostic stiffness | SAFE_IF | kappa stiffness may suppress imbalance but cannot add mass charge |
| ZK8 | epsilon_vac_config accounting | SAFE_IF | configuration bookkeeping cannot shift `M_A` without a source theorem |
| ZK9 | zeta/kappa cancellation branch | REJECTED | cancellation is not sector neutrality |
| ZK10 | residual-kill / non-metric convention | PROVISIONAL | safest current convention, but not a theorem |
| ZK11 | Box zeta / Box kappa route | REJECTED | no ordinary long-range residual scalar charge is licensed |
| ZK12 | B_s / zeta insertion dependency | THEOREM_TARGET | B_s/F_zeta insertion remains outside this script's license |

---

## Rejected Residual Routes

The script rejected these routes as ordinary-sector mass-neutrality shortcuts:

```text
nonzero zeta exterior tail,
nonzero kappa exterior tail,
residual cancellation by hand,
Box zeta / Box kappa scalar source,
residual relaxation repairs A-flux,
recovery-chosen residual status.
```

These are rejected as current ordinary-regime routes, not declared metaphysical impossibilities. A future parent identity could reopen some structure only if it derives source routing, mass accounting, boundary neutrality, and no double counting.

---

## Open Obligations

The script records the following theorem burden:

```text
derive zeta/kappa residual mass-neutrality theorem
```

In expanded form, the required future theorem must show that residual trace variables are one of:

```text
strictly non-metric,
killed / suppressed,
compact-neutral with no shell flux,
exterior-neutral with C_zeta = C_kappa = 0,
or routed through a future parent identity with no double counting.
```

It must also show that:

```text
e_kappa does not become a source reservoir,
epsilon_vac_config does not shift M_A,
residual relaxation does not alter A-flux,
B_s/zeta insertion is not chosen from recovery targets,
O is not used as a neutrality patch.
```

---

## What This Study Established

This study established the reduced flux witnesses:

\[
\zeta_{\rm tail}=\frac{C_\zeta}{r}
\quad\Rightarrow\quad
F_\zeta=-4\pi C_\zeta,
\]

and:

\[
\kappa_{\rm tail}=\frac{C_\kappa}{r}
\quad\Rightarrow\quad
F_\kappa=-4\pi C_\kappa.
\]

It also established that ordinary exterior scalar silence requires:

\[
C_\zeta=0,
\qquad
C_\kappa=0,
\]

unless residuals are non-metric/diagnostic, killed/suppressed, compact-neutral, or future-routed through a derived parent identity.

---

## What This Study Did Not Establish

This study did not derive a zeta insertion law.

It did not derive a kappa field equation.

It did not prove residual-kill.

It did not prove no-overlap.

It did not prove scalar silence for every sector.

It did not license `Box zeta` or `Box kappa`.

It did not define a parent mass law.

It did not make B_s/F_zeta insertion ready.

---

## Next Development Target

The next script should be:

```text
candidate_JV_mass_neutrality_conditions.py
```

Purpose:

```text
Audit J_V, J_sub, and J_exch for exterior mass leakage, scalar residue,
far-zone current flux, boundary repair, and ordinary-sector source rerouting.
```
