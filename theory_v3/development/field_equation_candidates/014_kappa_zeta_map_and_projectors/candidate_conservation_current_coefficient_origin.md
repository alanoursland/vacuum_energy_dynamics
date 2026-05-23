# Candidate Conservation-Current Coefficient Origin

## Canonical Filename

```text
candidate_conservation_current_coefficient_origin.md
```

This document summarizes the output of:

```text
candidate_conservation_current_coefficient_origin.py
```

---

## What This Document Is

This document is a development note for the `14_kappa_zeta_map_and_projectors/` group.

It is not a conservation-law derivation, not a parent balance identity, and not a final coefficient-origin theorem.

Its purpose is to test whether a conserved current / balance law can fix the stiffness ratio:

\[
r_s=\frac{c_x}{c_s}
\]

before recovery checks.

The guiding question was:

```text
Can a real conserved current fix c_x/c_s before recovery checks?
```

The answer is:

```text
Conservation current can fix q only if the current coefficient ratio is derived.

Minimal current:
  J_A^i = a grad^i A + b grad^i B_s

gives:
  q = -a/b

This is useful only if a/b is fixed before recovery checks.

Best next test:
  candidate_minimal_gradient_current_ratio_test.py
```

---

## Why This Study Matters

The stiffness-ratio inventory found:

\[
r_s=\frac{c_x}{c_s},
\qquad
q_{\rm action}=-r_s.
\]

Free \(r_s\) was rejected.

Symmetry and normalization remained possible but unspecified. Conservation-current origin was the strongest next non-tuning route, provided it could define a real current rather than decorative balance language.

---

## Compact Conservation-Current Ledger

| Entry | Current | Status | Consequence |
|---|---|---|---|
| CC1: conservation-current target | \({\rm div}\,J_A[A,B_s,T]=0\) fixes \(r_s=c_x/c_s\) | CANDIDATE | could rescue stiffness-ratio origin if non-decorative |
| CC2: gradient current | \(J_A^i=a\nabla^iA+b\nabla^iB_s\) | CANDIDATE | risks moving ratio problem from \(c_x/c_s\) to \(a:b\) |
| CC3: source-balance current | \({\rm div}\,J_A=S_A-S_{\rm spatial}\) or equivalent balance equation | RISK | may derive ratio if source balance is real, but high tuning risk |
| CC4: parent balance identity | \({\rm Div}\,E_{\rm parent}=B_{\rm closed}[T]+B_{\rm relax}\) | CANDIDATE | likely necessary if local current is insufficient |
| CC5: stiffness-current equivalence | \(J_A\) derived from variation of coupled stiffness functional | CONSTRAINED | prevents conservation route from duplicating stiffness ratio problem |
| CC6: current fixes ratio theorem target | \(r_s=r_J[J_A]\) before \(\gamma/AB\) checks | THEOREM_TARGET | decides whether conservation route rescues \(q\)-origin |
| CC7: decorative conservation failure | declare \({\rm div}\,J_A=0\) without defining \(J_A\) | REJECTED | kills conservation-current route if no current can be written |
| CC8: \(\gamma\)-like recovery check | weak-field output after \(r_s\) fixed gives \(\gamma_{\rm like}=1\) | RECOVERY_TARGET | tests but does not determine the current |
| CC9: \(AB\) exterior diagnostic check | exterior solution after current-fixed \(r_s\) gives \(AB\to1\) diagnostic | RECOVERY_TARGET | keeps \(AB\) diagnostic-only |
| CC10: no-overlap compatibility | current-fixed \(B_s\) must not overlap \(\zeta/\kappa\) residual trace | THEOREM_TARGET | conservation-derived ratio still fails if trace accounting fails |
| CC11: conservation route failure | no explicit current / balance law fixes \(r_s\) before recovery | DEFER | action / stiffness plus conservation cannot derive \(q\) locally |
| CC12: recommended next move | attempt minimal gradient-current ledger before volume-exchange branch | RECOMMENDED | next script should test gradient-current ansatz and whether it merely relocates the ratio |

---

## Status Counts

The run counted:

```text
CANDIDATE:       3
CONSTRAINED:     1
DEFER:           1
RECOMMENDED:     1
RECOVERY_TARGET: 2
REJECTED:        1
RISK:            1
THEOREM_TARGET:  2
```

Interpretation:

```text
Conservation-current origin is viable only if J_A is explicit.
Minimal gradient currents risk moving the ratio from c_x/c_s to a:b.
A parent balance identity may be needed if local current is insufficient.
Decorative conservation is rejected.
```

---

## Minimal Current Shape

Minimal local current ansatz:

\[
J_A^i=a\nabla^iA+b\nabla^iB_s.
\]

Then:

\[
{\rm div}\,J_A
=
a\Delta A+b\Delta B_s.
\]

Using:

\[
\Delta A=S_A,
\qquad
\Delta B_s=qS_A,
\]

gives:

\[
{\rm div}\,J_A=(a+bq)S_A.
\]

For:

\[
{\rm div}\,J_A=0
\]

with nonzero \(S_A\):

\[
q=-\frac{a}{b}.
\]

Interpretation:

```text
conservation fixes q only if a/b is itself derived.
Otherwise the ratio problem has merely moved from c_x/c_s to a/b.
```

---

## Good Failure / Defer Outcome

Good failure:

```text
minimal current gives q = -a/b, but no pre-recovery principle fixes a/b.
```

Consequence:

```text
local conservation current does not solve q-origin.
Move to broader parent balance or volume-exchange identity.
```

Bad failure:

```text
choose a/b from gamma_like=1 and call it conservation.
```

---

## Failure Controls

Conservation-current origin fails if:

1. \(J_A\) is not defined.
2. Current coefficients are chosen from \(\gamma_{\rm like}\).
3. Current coefficients are chosen from \(AB=1\).
4. Source-balance term is invented to repair recovery.
5. Current merely restates stiffness ratio.
6. \(a/b\) remains free but \(q\) is claimed derived.
7. No-overlap theorem is ignored after current fixes \(q\).
8. Parent balance terms are named but not defined.

---

## What This Study Established

This study established that a local conservation current can only rescue coefficient origin if its coefficient ratio is itself derived.

The minimal current:

\[
J_A^i=a\nabla^iA+b\nabla^iB_s
\]

gives:

\[
q=-\frac{a}{b}.
\]

So the local current route does not yet derive \(q\). It relocates the coefficient-origin problem from:

```text
c_x/c_s
```

to:

```text
a/b.
```

---

## What This Study Did Not Establish

This study did not derive \(a/b\).

It did not define a parent current \(J_A\) from ontology.

It did not define \(E_{\rm parent}\), \(B_{\rm closed}\), or \(B_{\rm relax}\).

It did not derive \(\gamma_{\rm like}=1\).

It did not derive \(AB\to1\).

It did not define the no-overlap operator.

---

## Current Best Interpretation

The conservation-current branch is viable only if the current coefficient ratio has a pre-recovery origin.

The next script must test the minimal gradient-current ratio explicitly.

---

## Next Development Target

The next script should be:

```text
candidate_minimal_gradient_current_ratio_test.py
```

Purpose:

```text
Test whether J_A^i = a grad A + b grad B_s genuinely fixes q or moves the ratio.
```

Reason:

```text
The conservation route must now test the minimal current shape explicitly before claiming q-origin.
```

Expected result:

```text
A gradient-current ratio ledger:
  minimal current calculation,
  q = -a/b,
  free a/b rejected,
  symmetry/normalization/current-origin candidates,
  equivalence with stiffness ratio,
  gamma/AB checks downstream,
  no-overlap condition,
  defer to parent balance or volume-exchange if a/b remains free.
```

---

## Summary

The conservation-current result is:

```text
A current can fix q only if someone fixed the current.
```

The next goblin gate is:

```text
is a/b real structure, or just c_x/c_s wearing a conservation cloak?
```
