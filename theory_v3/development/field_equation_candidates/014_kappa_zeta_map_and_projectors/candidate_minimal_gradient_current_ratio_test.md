# Candidate Minimal Gradient-Current Ratio Test

## Canonical Filename

```text
candidate_minimal_gradient_current_ratio_test.md
```

This document summarizes the output of:

```text
candidate_minimal_gradient_current_ratio_test.py
```

---

## What This Document Is

This document is a development note for the `14_kappa_zeta_map_and_projectors/` group.

It is not a parent balance identity, not a current derivation, and not a final coefficient-origin theorem.

Its purpose is to test whether the minimal local current genuinely fixes \(q\), or merely moves the ratio problem from \(c_x/c_s\) to \(a/b\).

The guiding question was:

```text
Is a/b real structure, or just c_x/c_s wearing a conservation cloak?
```

The answer is:

```text
Minimal gradient current gives:

  q = -a/b

This is not a q derivation unless a/b is derived.

Best next test:
  candidate_parent_balance_identity_for_A_spatial.py
```

---

## Why This Study Matters

The conservation-current coefficient-origin audit found that the minimal current:

\[
J_A^i
=
a\nabla^iA
+
b\nabla^iB_s
\]

could fix:

\[
q=-\frac{a}{b}
\]

only if \(a/b\) had a pre-recovery origin.

This study tested that current explicitly and found that the local current relocates the coefficient problem rather than solving it.

---

## Compact Gradient-Current Ledger

| Entry | Statement | Status | Consequence |
|---|---|---|---|
| GC1: minimal gradient current | \(J_A^i=a\nabla^iA+b\nabla^iB_s\) | STRUCTURAL | current is explicit but ratio remains exposed |
| GC2: divergence calculation | \({\rm div}\,J_A=a\Delta A+b\Delta B_s=(a+bq)S_A\) | THEOREM_TARGET | with nonzero \(S_A\), \({\rm div}\,J_A=0\) implies \(q=-a/b\) |
| GC3: ratio relocation | \(q=-a/b\) | DEFER | minimal current relocates the problem unless \(a/b\) is fixed |
| GC4: free current ratio | choose \(a/b\) freely | REJECTED | turns conservation into coefficient tuning |
| GC5: stiffness-current equivalence | \(a:b\) maps to \(c_x:c_s\) or Noether current of coupled stiffness | CONSTRAINED | may collapse conservation route back into stiffness-ratio problem |
| GC6: field-space metric origin | \(a/b\) fixed by metric on \((A,B_s)\) field space | CANDIDATE | could rescue local current if concrete |
| GC7: source-balance origin | \(a/b\) fixed by matching current divergence to source routing | RISK | may require parent balance identity rather than local current |
| GC8: parent balance origin | \(a/b\) fixed by \({\rm Div}\,E_{\rm parent}=B_{\rm closed}[T]+B_{\rm relax}\) | CANDIDATE | likely next route if local current ratio remains free |
| GC9: \(\gamma\)-like recovery check | after \(a/b\) fixed, weak-field output gives \(\gamma_{\rm like}=1\) | RECOVERY_TARGET | tests but does not determine \(a/b\) |
| GC10: \(AB\) diagnostic check | after \(a/b\) fixed, exterior solution gives \(AB\to1\) diagnostic | RECOVERY_TARGET | keeps \(AB\) diagnostic-only |
| GC11: no-overlap trace condition | current-fixed \(B_s\) must not overlap \(\zeta/\kappa\) residual trace | THEOREM_TARGET | current route still fails if trace accounting overlaps |
| GC12: recommended next move | if \(a/b\) has no local origin, move to parent balance or volume-exchange origin | RECOMMENDED | next script should test parent balance identity or volume-exchange stiffness ratio origin |

---

## Status Counts

The run counted:

```text
CANDIDATE:       2
CONSTRAINED:     1
DEFER:           1
RECOMMENDED:     1
RECOVERY_TARGET: 2
REJECTED:        1
RISK:            1
STRUCTURAL:      1
THEOREM_TARGET:  2
```

Interpretation:

```text
The minimal current is explicit but does not derive q unless a/b has an origin.
Free a/b is rejected.
Field-space metric and parent balance are the main surviving origins.
Local conservation likely defers to parent balance or volume-exchange identity.
```

---

## Minimal Gradient-Current Calculation

Current:

\[
J_A^i
=
a\nabla^iA
+
b\nabla^iB_s.
\]

Divergence:

\[
{\rm div}\,J_A
=
a\Delta A
+
b\Delta B_s.
\]

Using:

\[
\Delta A=S_A,
\qquad
\Delta B_s=qS_A,
\]

gives:

\[
{\rm div}\,J_A
=
(a+bq)S_A.
\]

If:

\[
{\rm div}\,J_A=0
\]

and:

\[
S_A\ne0,
\]

then:

\[
q=-\frac{a}{b}.
\]

Interpretation:

```text
This fixes q only if a/b is fixed independently.
```

---

## Good Failure / Defer Outcome

Good failure:

```text
minimal current gives q=-a/b,
but a/b has no local pre-recovery origin.
```

Consequence:

```text
local conservation current does not derive q.
Move to parent balance identity or volume-exchange stiffness-ratio origin.
```

Bad failure:

```text
choose a/b from gamma_like=1 and call it a conservation law.
```

---

## Failure Controls

Gradient-current ratio test fails if:

1. \(a/b\) is chosen from \(\gamma_{\rm like}\).
2. \(a/b\) is chosen from \(AB=1\).
3. \(a/b\) is declared by normalization without a field-space metric.
4. Current is just Noether restatement of coupled stiffness with no new identity.
5. Source-balance origin is invented to repair recovery.
6. Parent balance terms are named but undefined.
7. No-overlap trace theorem is ignored.
8. \(q\) is claimed derived while \(a/b\) remains free.

---

## What This Study Established

This study established that the minimal gradient current:

\[
J_A^i
=
a\nabla^iA
+
b\nabla^iB_s
\]

implies:

\[
q=-\frac{a}{b}
\]

only after imposing \({\rm div}\,J_A=0\).

That does not derive \(q\) unless \(a/b\) has an independent pre-recovery origin.

Therefore local conservation-current closure is not yet a coefficient-origin theorem.

---

## What This Study Did Not Establish

This study did not derive \(a/b\).

It did not define a field-space metric.

It did not define the parent balance operator.

It did not derive \(\gamma_{\rm like}=1\).

It did not derive \(AB\to1\).

It did not define the no-overlap operator.

---

## Current Best Interpretation

The local current route has reached the same wall as coupled stiffness:

```text
ratio origin.
```

The strongest next non-decorative route is a parent balance identity that can define the current coefficient ratio rather than merely naming it.

---

## Next Development Target

The next script should be:

```text
candidate_parent_balance_identity_for_A_spatial.py
```

Purpose:

```text
Test whether a parent balance identity can fix the current ratio.
```

Reason:

```text
Local gradient current relocates q to a/b.
A parent balance identity is the next non-decorative route for fixing a/b.
```

Expected result:

```text
A parent-balance ledger:
  E_parent operator candidate,
  B_closed[T] source-balance candidate,
  B_relax residual/relaxation candidate,
  current-ratio derivation target,
  no decorative Bianchi-like language,
  gamma/AB checks downstream,
  no-overlap trace requirement,
  defer to volume-exchange if balance remains unnamed.
```

---

## Summary

The gradient-current result is:

```text
A local current can wear the coefficient problem,
but it cannot digest it.
```

The next goblin gate is:

```text
can parent balance fix a/b, or is balance just another painted tunnel?
```
