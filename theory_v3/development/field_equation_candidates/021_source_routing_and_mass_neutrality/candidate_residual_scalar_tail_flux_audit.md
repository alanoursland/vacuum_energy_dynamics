# Candidate Residual Scalar Tail Flux Audit

## Canonical Filename

```text
candidate_residual_scalar_tail_flux_audit.md
```

This document summarizes the output of:

```text
candidate_residual_scalar_tail_flux_audit.py
```

## What This Document Is

This document is the third artifact for `21_source_routing_and_mass_neutrality/`.

It is a reduced symbolic flux audit and requirements artifact. It is not a scalar-silence theorem, not a zeta field equation, not a kappa field equation, not a vacuum-current law, not a curvature-current law, not a correction-tensor law, and not a boundary neutrality theorem.

Its purpose is to test the surface flux carried by ordinary non-A residual scalar tails after the A-sector mass charge and the non-A mass-neutrality inventory have been established.

The locked-door question was:

```text
What exterior scalar tails are automatically mass-dangerous?
```

The core result is:

```text
For a residual exterior scalar tail

  phi_tail = C/r

one obtains

  F_phi = 4*pi*r^2*phi_tail' = -4*pi*C.

Therefore a nonzero ordinary residual 1/r scalar tail carries exterior flux.
It is neutral only if C = 0, unless a future theorem routes it through the A-sector
without double counting.
```

Tiny goblin label:

```text
No hidden 1/r tail.
Show C = 0 or drop the coin.
```

---

## Archive Dependency Status

The run reported clean upstream dependency resolution:

```text
non_A_sector_mass_neutrality_inventory_dependency_21: dependency_satisfied
A_sector_mass_definition_dependency_21: dependency_satisfied
```

No missing-parent, traceback, archive-write, or computation-health issue appeared in the run. The warning and failure labels in the run are expected governance classifications for risky or rejected branches, not operational errors.

---

## Reference Discipline

The audit preserves the Group 21 reference rule:

```text
A-sector mass charge remains the reduced ordinary exterior reference.
Non-A residual scalar tails must not create a second exterior flux coin.
```

It does not prove scalar silence sector by sector. It supplies the reduced surface-flux witness that future scalar-silence and boundary-neutrality theorems must satisfy.

---

## Core Derivation

For a generic residual scalar tail:

\[
\phi_{\rm tail}(r)=\frac{C}{r},
\]

we have:

\[
\phi'_{\rm tail}(r)=-\frac{C}{r^2}.
\]

The reduced surface flux is:

\[
F_\phi=4\pi r^2\phi'_{\rm tail}=-4\pi C.
\]

The run recorded the residual:

```text
F_phi + 4*pi*C = 0
```

and the neutrality condition:

```text
C = 0
```

Thus the symbolic witness is:

```text
C != 0  ->  F_phi != 0.
```

This is why an ordinary-sector residual `1/r` scalar tail is mass-dangerous.

---

## Power-Tail Diagnostic

The script also evaluated a diagnostic power tail:

\[
\phi_n(r)=\frac{C}{r^n}.
\]

The corresponding surface flux is:

\[
F_n=-4\pi C n r^{1-n}.
\]

Special cases:

```text
n = 1: F_n = -4*pi*C
n = 2: F_n = -8*pi*C/r
```

Interpretation:

```text
The 1/r tail is the constant-flux danger.
Faster falloff may remove far-zone constant flux,
but boundary and domain behavior still need separate checks.
```

This is a diagnostic example, not a theorem licensing arbitrary faster-falloff residuals.

---

## Sector Tail Inventory

The run audited six residual-tail sectors:

| Entry | Sector | Dangerous tail | Status | Required condition |
|---|---|---|---|---|
| T1 | `zeta_residual` | `zeta_tail = C_zeta/r` | RISK | `C_zeta = 0` outside, or residual zeta is strictly non-metric, killed, or compact-neutral |
| T2 | `kappa_residual` | `kappa_tail = C_kappa/r` | RISK | `C_kappa = 0` outside, or kappa is suppressed, non-metric, or compact-neutral |
| T3 | `J_V_residue` | `phi_JV = C_JV/r` | UNRESOLVED | define `J_V` and prove `C_JV = 0` or derive A-sector routing |
| T4 | `A_curv / e_curv / J_curv residue` | `phi_curv = C_curv/r` | THEOREM_TARGET | keep curvature objects diagnostic/branch-filter or prove `C_curv = 0` |
| T5 | `H_curv / H_exch trace leakage` | `phi_H = C_H/r` | THEOREM_TARGET | keep `H` non-insertable or prove scalar trace neutrality `C_H = 0` |
| T6 | `boundary_smoothing / shell residue` | `phi_boundary = C_boundary/r` | THEOREM_TARGET | derive no shell scalar source and `C_boundary = 0` without recovery-tuned smoothing |

The key point is not that these sectors are proven silent. They are not.

The key point is:

```text
Each sector now has an explicit scalar-tail coefficient burden.
```

---

## Branch Classification

The script classified four scalar-tail branches:

| Branch | Status | Condition | Consequence |
|---|---|---|---|
| nonzero residual scalar tail | REJECTED | `F_phi = -4*pi*C` is nonzero | ordinary residual scalar tail carries exterior flux and fails scalar silence |
| zero-amplitude scalar tail | SAFE_IF | `C = 0` | dangerous exterior `1/r` scalar flux vanishes |
| compact or faster-decaying diagnostic residual | SAFE_IF | no exterior `1/r` coefficient and no boundary shell flux | may remain diagnostic if it has no metric, source, boundary, or A-flux effect |
| A-sector-routed tail by future theorem | THEOREM_TARGET | future source identity derives routing and avoids double counting | not licensed here; high-burden future route |

The run recorded the nonzero residual `1/r` tail as a rejected branch because it carries the flux witness:

\[
F_\phi=-4\pi C.
\]

---

## Main Result

The script recorded the claim:

```text
residual_1_over_r_tail_flux_rule_21
```

with the content:

```text
For a reduced exterior residual scalar tail phi = C/r,
the surface flux is F_phi = -4*pi*C.
Therefore C = 0 is required for zero flux of that residual tail.
```

It also recorded the policy rule:

```text
ordinary_residual_scalar_silence_requirement_21
```

which states that ordinary-sector non-A residual scalar tails must either:

```text
have zero exterior 1/r coefficient,
remain diagnostic/non-metric/compact-neutral,
or stay theorem-targeted.
```

A nonzero `1/r` residual tail is not mass-neutral by declaration.

---

## Open Obligations

The script records sector-specific scalar-silence obligations, including:

```text
derive_zeta_no_exterior_scalar_tail_21
derive_kappa_no_exterior_scalar_tail_21
derive_JV_no_scalar_residue_21
derive_curvature_no_scalar_residue_21
derive_H_no_scalar_leakage_21
derive_boundary_no_shell_scalar_residue_21
```

It also records the group-level theorem target:

```text
derive_ordinary_closed_regime_scalar_silence_theorem_21
```

This theorem would need to show that ordinary-sector non-A residual scalar tails have zero `1/r` coefficient, remain non-metric/diagnostic, are compact-neutral with no shell flux, or are routed through a derived A-sector source law without double counting.

The audit does not satisfy those obligations. It defines their flux witness.

---

## Failure Controls

The run says this audit fails if a later script allows any of the following:

1. `zeta` or `kappa` residuals to carry `C/r` outside with `C != 0`.
2. `J_V` to leave a scalar `1/r` residue while undefined.
3. Curvature diagnostics to become scalar curvature charge.
4. `H_curv` or `H_exch` trace leakage to cancel or modify exterior mass.
5. Boundary smoothing or shell behavior to leave `C_boundary/r`.
6. Scalar silence to be imposed by `O` without kernel, image, and boundary law.
7. Faster falloff to be treated as safe without boundary and domain checks.
8. A residual scalar tail to be routed through A without a no-double-counting theorem.

---

## What This Study Established

This study established the reduced exterior flux identity:

\[
\phi_{\rm tail}=\frac{C}{r}
\quad\Rightarrow\quad
F_\phi=-4\pi C.
\]

Therefore:

\[
F_\phi=0 \quad\Rightarrow\quad C=0
\]

for the ordinary residual `1/r` scalar-tail channel.

It also established that a nonzero residual `1/r` scalar tail is a concrete flux witness against scalar silence.

---

## What This Study Did Not Establish

This study did not prove scalar silence for every sector.

It did not derive a zeta source law, kappa source law, `J_V` current law, curvature current, correction tensor, boundary law, or parent scalar field equation.

It did not prove that compact or faster-decaying residuals are automatically safe. It only showed that the `1/r` tail is the constant-flux danger and that faster falloff still requires boundary/domain checks.

It did not license routing a residual tail through the A-sector. That remains a future theorem target.

---

## Next Development Target

The next script should be:

```text
candidate_boundary_flux_mass_preservation.py
```

Purpose:

```text
Test whether boundary or smoothing behavior can preserve A-sector mass without repair.
```

Expected conservative result:

```text
Boundary mass preservation remains theorem-targeted.
Only compact/neutral diagnostic behavior is safe.
No shell source, counterterm, recovery-tuned smoothing, or boundary purse is licensed.
```
