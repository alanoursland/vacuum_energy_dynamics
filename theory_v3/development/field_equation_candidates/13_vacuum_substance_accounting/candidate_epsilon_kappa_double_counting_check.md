# Candidate Epsilon Kappa Double Counting Check

## Canonical Filename

```text
candidate_epsilon_kappa_double_counting_check.md
```

This document summarizes the output of:

```text
candidate_epsilon_kappa_double_counting_check.py
```

---

## What This Document Is

This document is a development note for the `13_vacuum_substance_accounting/` group.

It is not a derivation of the \(\kappa\)-\(\zeta\) map, not a final accounting convention, and not a parent recombination identity. It does not add a formal commitment to the theory.

Its purpose is to prevent the same trace / volume mismatch from being counted twice.

The guiding question was:

```text
Should e_kappa be inside or outside epsilon_vac_config?
```

The answer is:

```text
To avoid double-counting:
  keep e_kappa outside epsilon_vac_config for now,
  keep epsilon_vac_config as zeta displacement plus gradient / interface terms,
  treat K_lock as diagnostic / constraint target, not physical energy,
  revisit after the kappa-zeta map is derived.
```

---

## Why This Study Matters

The candidate \(\epsilon_{\rm vac,config}\) functional originally allowed a locking term:

\[
\frac12K_{\rm lock}
\left[
\kappa-(\zeta-\zeta_{\min})
\right]^2.
\]

Existing \(\kappa\) relaxation accounting already had:

\[
e_\kappa
=
\frac12K_\kappa(\kappa-\kappa_{\min})^2.
\]

If the \(\epsilon_{\rm vac,config}\) functional contains a \(\kappa\)-mismatch energy and \(e_\kappa\) is also counted separately, the same trace / volume imbalance may be counted twice.

This study prevents that.

---

## Compact Double-Counting Ledger

| Entry | Option | Status | Accounting Rule | Missing |
|---|---|---|---|---|
| D1: \(e_\kappa\) outside \(\epsilon_{\rm vac,config}\) | \(\epsilon_{\rm vac,config}\) contains \(\zeta\) geometry; \(e_\kappa\) is separate sector relaxation energy | SAFE_IF | \(E_{\rm total}\) includes \(\epsilon_{\rm vac,config}+e_\kappa\) once each | whether \(\kappa\) is independent or just \(\zeta\) mismatch |
| D2: \(e_\kappa\) inside \(\epsilon_{\rm vac,config}\) | \(\epsilon_{\rm vac,config}\) includes \(\kappa\) mismatch energy | SAFE_IF | \(E_{\rm total}\) includes \(\epsilon_{\rm vac,config}\) only; do not add \(e_\kappa\) separately | how \(\Gamma_{\rm relax}\) is written when \(e_\kappa\) is internal |
| D3: \(\kappa\)-\(\zeta\) locking as constraint, not energy | \(K_{\rm lock}\to\) constraint enforcing \(\kappa=\zeta-\zeta_{\min}\) | CANDIDATE | locking term not counted as physical energy if it is a Lagrange constraint | constraint versus penalty interpretation |
| D4: \(\kappa\)-\(\zeta\) locking as penalty energy | finite \(K_{\rm lock}\) penalty energy included in \(\epsilon_{\rm vac,config}\) | RISK | locking energy counted inside \(\epsilon\); no duplicate \(e_\kappa\) for same mismatch | degree-of-freedom count and projector identity |
| D5: \(\Gamma_{\rm relax}\) with external \(e_\kappa\) | \(\Gamma_{\rm relax}\) transfers from \(e_\kappa\) to \(\epsilon_{\rm vac,config}\) | CANDIDATE | \(de_\kappa/d\tau+d\epsilon_{\rm vac,config}/d\tau=0\) | sign convention and source of relaxation rate |
| D6: \(\Gamma_{\rm relax}\) with internal \(e_\kappa\) | \(\Gamma_{\rm relax}\) is internal redistribution within \(\epsilon_{\rm vac,config}\) | CANDIDATE | \(d\epsilon_{\rm vac,config}/d\tau\) accounts for \(\kappa\) relaxation internally | internal bookkeeping decomposition |
| D7: forbidden duplicate total energy | \(E_{\rm total}=\epsilon_{\rm vac,config}+e_\kappa\) when \(\epsilon\) already includes \(\kappa\) mismatch | FORBIDDEN | do not do this | not pursued |
| D8: forbidden duplicate source response | \(\rho\) or trace response creates \(A\) mass, \(\zeta\) charge, and \(\kappa\) charge independently | FORBIDDEN | source response must be routed once by projectors | \(P_{\rm recombination}\) and source projector identity |
| D9: recommended provisional convention | treat \(e_\kappa\) outside \(\epsilon_{\rm vac,config}\) for now; keep \(\epsilon\) purely \(\zeta\)-volume until \(\kappa\)-\(\zeta\) map is derived | RECOMMENDED | \(\epsilon_{\rm vac,config}=\zeta\) displacement + gradient / interface terms; \(e_\kappa\) separate; no \(K_{\rm lock}\) energy counted yet | later revisit after \(\kappa\)-\(\zeta\) map |
| D10: later unified convention | after \(\kappa\)-\(\zeta\) map, absorb \(e_\kappa\) into \(\epsilon_{\rm vac,config}\) or eliminate \(\kappa\) as independent energy | STRUCTURAL | single trace / volume energy functional | parent projector / recombination derivation |

---

## Status Counts

The run counted:

```text
CANDIDATE:    3
FORBIDDEN:    2
RECOMMENDED:  1
RISK:         1
SAFE_IF:      2
STRUCTURAL:   1
```

Interpretation:

```text
Both inside and outside conventions are possible.
The safest provisional convention is to keep e_kappa outside epsilon_vac_config.
K_lock should remain diagnostic / constraint-like until the kappa-zeta map is derived.
```

---

## Recommended Provisional Convention

Recommended for now:

\[
\epsilon_{\rm vac,config}
=
\frac12K_\zeta(\zeta-\zeta_{\min})^2
+
\frac12L_\zeta|\nabla\zeta|^2.
\]

Separate \(\kappa\) relaxation energy:

\[
e_\kappa
=
\frac12K_\kappa(\kappa-\kappa_{\min})^2.
\]

Provisional exchange accounting:

\[
\frac{de_\kappa}{d\tau}
+
\frac{d\epsilon_{\rm vac,config}}{d\tau}
=
0.
\]

Constraint target:

\[
\kappa\sim\zeta-\zeta_{\min}.
\]

But:

```text
no K_lock energy counted until derived.
```

Reason:

```text
the kappa-zeta map is not derived,
so combining them risks double-counting.
```

Status:

```text
RECOMMENDED / PROVISIONAL
```

---

## Forbidden Patterns

Forbidden:

1. \(\epsilon\) includes \(\kappa\) mismatch and \(E_{\rm total}\) also adds \(e_\kappa\).
2. \(K_{\rm lock}\) enforces equality exactly and is also counted as finite energy.
3. \(\rho\) contributes to \(A\) mass, \(\zeta\) exterior charge, and \(\kappa\) exterior charge.
4. \(\Gamma_{\rm relax}\) transfers energy between two terms that are already the same term.
5. Recombination counts \(\zeta\) and \(\kappa\) as independent scalar gravity sectors.

---

## What This Study Established

This study established a provisional convention:

```text
e_kappa stays outside epsilon_vac_config for now.
epsilon_vac_config stays purely zeta-volume plus gradient / interface terms.
K_lock is diagnostic / constraint target, not physical energy.
```

It also established the later revision path:

```text
after the kappa-zeta map is derived,
e_kappa may be absorbed into epsilon_vac_config
or kappa may be eliminated as an independent energy.
```

---

## What This Study Did Not Establish

This study did not derive the \(\kappa\)-\(\zeta\) map.

It did not decide whether \(\kappa\) is an independent variable or a diagnostic projection.

It did not derive \(K_\zeta,L_\zeta,K_\kappa\).

It did not derive \(\Gamma_{\rm relax}\).

It did not derive \(P_{\rm recombination}\).

It only fixed a provisional accounting convention.

---

## Current Best Interpretation

For now:

\[
\epsilon_{\rm vac,config}
=
\frac12K_\zeta(\zeta-\zeta_{\min})^2
+
\frac12L_\zeta|\nabla\zeta|^2.
\]

and:

\[
e_\kappa
=
\frac12K_\kappa(\kappa-\kappa_{\min})^2.
\]

They are counted separately.

No \(K_{\rm lock}\) energy is counted yet.

---

## Next Development Target

The output recommended:

```text
vacuum_substance_accounting_summary.md
```

Reason:

```text
Group 13 has reached a natural summary point with a provisional accounting convention.
```

---

## Summary

The double-counting result is:

```text
do not count kappa mismatch energy twice.
```

The group-13 provisional convention is:

```text
epsilon_vac_config is zeta-volume configuration,
e_kappa is separate kappa relaxation energy,
K_lock is only a diagnostic / constraint target until derived.
```
