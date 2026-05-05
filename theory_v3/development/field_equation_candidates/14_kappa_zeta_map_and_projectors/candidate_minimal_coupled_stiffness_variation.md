# Candidate Minimal Coupled Stiffness Variation

## Canonical Filename

```text
candidate_minimal_coupled_stiffness_variation.md
```

This document summarizes the output of:

```text
candidate_minimal_coupled_stiffness_variation.py
```

---

## What This Document Is

This document is a development note for the `14_kappa_zeta_map_and_projectors/` group.

It is not a final action, not a coefficient-origin theorem, and not a completed \(A_{\rm spatial}\) derivation.

Its purpose is to vary a concrete minimal coupled stiffness functional and determine whether it derives \(q\), or merely moves the tuning knob from \(q\) to a stiffness ratio.

The guiding question was:

```text
Does coupled stiffness derive q, or only move the tuning knob?
```

The answer is:

```text
Coupled stiffness variation produces the right form:

  ΔB_s = q_action S_A
  q_action = -(c_x/c_s)

But it does not fully derive q unless c_x/c_s is derived.

Best next test:
  candidate_stiffness_ratio_origin_inventory.py
```

Here \(B_s\) denotes the reduced \(A_{\rm spatial}\) scalar variable used in the symbolic test.

---

## Why This Study Matters

The parent action / stiffness audit found that action / stiffness is legitimate only if it writes a functional and derives \(q\) before recovery checks.

The minimal coupled stiffness functional is:

\[
S
=
\int
\left[
\frac12c_A|\nabla A|^2
+
\frac12c_s|\nabla B_s|^2
+
c_x\nabla A\cdot\nabla B_s
+
c_mAS_A
\right]
dV.
\]

This study varies that functional and asks whether \(q\) is really derived.

---

## Compact Coupled-Variation Ledger

| Entry | Statement | Status | Consequence |
|---|---|---|---|
| CV1: minimal coupled functional | \(S=\int[\frac12c_A|\nabla A|^2+\frac12c_s|\nabla B_s|^2+c_x\nabla A\cdot\nabla B_s+c_mAS_A]dV\) | STRUCTURAL | functional can be varied, but coefficient freedom remains visible |
| CV2: variation with respect to \(B_s\) | \(\delta S/\delta B_s\rightarrow -c_s\Delta B_s-c_x\Delta A=0\) | CANDIDATE | gives \(\Delta B_s=-(c_x/c_s)\Delta A\) |
| CV3: using \(A\) constraint | with \(\Delta A=S_A\), variation gives \(\Delta B_s=q_{\rm action}S_A\), where \(q_{\rm action}=-(c_x/c_s)\) | THEOREM_TARGET | \(q\) is reduced to stiffness-ratio origin, not fully derived yet |
| CV4: variation with respect to \(A\) | \(\delta S/\delta A\rightarrow -c_A\Delta A-c_x\Delta B_s+c_mS_A=0\) | RISK | coupled action may disturb the existing \(A\) constraint unless constrained |
| CV5: independent stiffness failure | if \(c_x=0\), then \(B_s\) has no sourced spatial companion equation | BRANCH_KILLED | independent stiffness alone cannot derive \(A_{\rm spatial}\) from \(A\) |
| CV6: direct \(B_s\) source coupling | add \(c_bB_sS_A\) | RISK | could derive \(q\) only if \(c_b/c_s\) has prior origin |
| CV7: stiffness-ratio free parameter problem | \(q_{\rm action}=-(c_x/c_s)\) | DEFER | action variation moves the problem to coefficient origin unless \(c_x/c_s\) is constrained |
| CV8: \(\gamma\)-like recovery check | weak-field output checks whether \(q_{\rm action}\) produces \(\gamma_{\rm like}=1\) | RECOVERY_TARGET | tests but does not determine stiffness ratio |
| CV9: \(AB\) exterior diagnostic check | exterior solution checks \(\kappa_{\rm areal}\to0\) / \(AB\to1\) | RECOVERY_TARGET | keeps \(AB\) diagnostic-only |
| CV10: no-overlap trace condition | \(O[B_s,{\rm trace}_{\rm residual}]=0\) or residual killed / non-metric | THEOREM_TARGET | derived \(q\) still fails if trace accounting overlaps |
| CV11: stiffness tuning failure | choose \(c_x/c_s\) after checking \(\gamma_{\rm like}\) or Schwarzschild expansion | REJECTED | kills coupled stiffness as \(q\)-origin if unavoidable |
| CV12: recommended next move | test whether \(c_x/c_s\) can be fixed by symmetry, normalization, or conservation | RECOMMENDED | next script should audit \(c_x/c_s\) origin or move to conservation-current origin |

---

## Status Counts

The run counted:

```text
BRANCH_KILLED:  1
CANDIDATE:      1
DEFER:          1
RECOMMENDED:    1
RECOVERY_TARGET: 2
REJECTED:       1
RISK:           2
STRUCTURAL:     1
THEOREM_TARGET: 2
```

Interpretation:

```text
Coupled stiffness can produce the A_spatial equation form.
It does not by itself derive the stiffness ratio c_x/c_s.
Independent stiffness alone is killed as a q-origin.
The branch must now find a ratio origin or defer to conservation/current identity.
```

---

## Minimal Variation Calculation

Functional:

\[
S
=
\int
\left[
\frac12c_A|\nabla A|^2
+
\frac12c_s|\nabla B_s|^2
+
c_x\nabla A\cdot\nabla B_s
+
c_mAS_A
\right]
dV.
\]

Variation with respect to \(B_s\):

\[
-c_s\Delta B_s-c_x\Delta A=0.
\]

Therefore:

\[
\Delta B_s
=
-\frac{c_x}{c_s}\Delta A.
\]

Using:

\[
\Delta A=S_A,
\]

gives:

\[
\Delta B_s
=
q_{\rm action}S_A,
\]

where:

\[
q_{\rm action}
=
-\frac{c_x}{c_s}.
\]

Interpretation:

```text
Variation derives q only if c_x/c_s is itself derived.
Otherwise it moves the tuning knob from q to stiffness ratio.
```

---

## Good Failure / Defer Outcome

Good failure:

```text
coupled variation yields q_action = -(c_x/c_s),
but no pre-recovery principle fixes c_x/c_s.
```

Consequence:

```text
coupled stiffness does not fully derive q.
It exposes the next bottleneck: stiffness-ratio origin.
Search should test symmetry/normalization/conservation origin
or defer to conservation-current identity.
```

Bad failure:

```text
choose c_x/c_s to make gamma_like=1 and call the action derived.
```

---

## Failure Controls

Coupled stiffness variation fails if:

1. \(c_x/c_s\) is chosen from \(\gamma_{\rm like}=1\).
2. \(c_x/c_s\) is chosen from Schwarzschild expansion.
3. \(AB=1\) is used as action constraint or boundary condition.
4. \(A\) variation destroys the existing \(A\) constraint without explanation.
5. \(B_s\) source coupling is added only to repair \(q\).
6. \(\zeta/\kappa\) residual trace overlaps with \(B_s\).
7. Variation result is claimed to derive \(q\) while \(c_x/c_s\) remains free.

---

## What This Study Established

This study established that coupled stiffness can produce the right equation form:

\[
\Delta B_s=q_{\rm action}S_A.
\]

It also established:

\[
q_{\rm action}
=
-\frac{c_x}{c_s}.
\]

But this does not fully derive \(q\). It exposes the next bottleneck:

```text
stiffness-ratio origin.
```

Independent stiffness alone is killed as a \(q\)-origin because if \(c_x=0\), \(B_s\) has no sourced spatial companion equation.

---

## What This Study Did Not Establish

This study did not derive \(c_x/c_s\).

It did not derive \(\gamma_{\rm like}=1\).

It did not derive \(AB\to1\).

It did not define the overlap operator \(O\).

It did not prove that the coupled action preserves the existing \(A\)-constraint normalization.

It did not decide whether \(B_s\) source coupling is allowed.

---

## Current Best Interpretation

The action / stiffness branch survives, but only after being narrowed:

```text
coupled stiffness reduces q-origin to c_x/c_s origin.
```

The next script should not claim \(q\) is derived. It should audit possible pre-recovery origins of \(c_x/c_s\).

---

## Next Development Target

The next script should be:

```text
candidate_stiffness_ratio_origin_inventory.py
```

Purpose:

```text
Test whether c_x/c_s can come from symmetry, normalization, conservation, or ontology.
```

Reason:

```text
Coupled variation produces q_action = -c_x/c_s.
The next bottleneck is whether c_x/c_s has a pre-recovery origin.
```

---

## Summary

The coupled-stiffness result is:

```text
The equation shape survives.
The coefficient origin does not.
```

The next goblin gate is:

```text
who fixed c_x/c_s before gamma looked at it?
```
