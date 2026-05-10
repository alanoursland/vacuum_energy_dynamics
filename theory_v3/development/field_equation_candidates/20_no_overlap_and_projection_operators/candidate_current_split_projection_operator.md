# Candidate Current-Split Projection Operator

## Canonical Filename

```text
candidate_current_split_projection_operator.md
```

This document summarizes the output of:

```text
candidate_current_split_projection_operator.py
```

## What This Document Is

This document is a Group 20 no-overlap / projection-operator artifact.

It is not a definition of \(O_{\rm current}\), not a definition of \(J_V\), not a source-side law, and not a proof that \(J_{\rm sub}\) or \(J_{\rm exch}\) are physical currents.

Its purpose is to test whether projection language can strengthen the Group 18 role-level current split:

```text
J_V,
J_sub,
J_exch,
Sigma/R,
pure-wind neutrality,
ordinary-sector exchange neutrality,
timelike current domain.
```

The locked-door question was:

```text
Can O make J_sub/J_exch or J_V split operator-level?
```

The result is:

```text
Current-split projection is not solved.

J_V remains unresolved umbrella notation.
J_sub/J_exch remains role-level bookkeeping.
Zero-net and zero-creation ordinary-sector branches remain candidates.

Best next script:
  candidate_projection_commutation_and_divergence.py
```

## Core Result

Allowed current status:

```text
J_V remains unresolved umbrella notation
J_sub/J_exch remains role-level bookkeeping
zero-net exchange branch remains candidate
zero-creation ordinary-sector branch remains candidate
u_vac remains domain-limited theorem target
```

Rejected:

```text
remainder-current split,
repair-current projection,
projection as definition of J_V or source sides.
```

Missing before \(O_{\rm current}\) can be real:

```text
physical J_V flux law,
J_sub/J_exch split criterion,
Sigma/R operators,
pure wind neutrality,
ordinary matter decoupling,
M_ext/scalar/boundary neutrality.
```

## Compact Current-Split Ledger

| Entry | Candidate | Status | Consequence |
|---|---|---|---|
| C1: current-split projection target | \(O_{\rm current}\) makes \(J_V \to J_{\rm sub}+J_{\rm exch}\) operator-level | THEOREM_TARGET | current split remains theorem target |
| C2: unresolved umbrella \(J_V\) | \(J_V\) remains unresolved umbrella notation | SAFE_IF | projection cannot split an undefined current into defined parts |
| C3: support-based split | \(J_{\rm sub}\) and \(J_{\rm exch}\) separated by support/domain | CANDIDATE | possible only after current support is real |
| C4: divergence-based split | \(J_{\rm sub}\) divergence-free, \(J_{\rm exch}\) carries source/relaxation divergence | THEOREM_TARGET | cannot proceed while \(\Sigma/R\) remain role-level |
| C5: pure-wind neutral subspace | \(J_{\rm sub}\) lies in a pure-wind neutral subspace | THEOREM_TARGET | \(J_{\rm sub}\) remains theorem target only |
| C6: active-exchange support subspace | \(J_{\rm exch}\) lives only where exchange source/relaxation operators are active | THEOREM_TARGET | \(J_{\rm exch}\) remains theorem target only |
| C7: zero-net ordinary-sector projection | project ordinary sector onto \(\Sigma_V-R_V=0\) branch | CANDIDATE | zero-net branch remains live but not derived |
| C8: zero-creation ordinary-sector projection | project ordinary sector onto \(\Sigma_V=R_V=0\) branch | CANDIDATE | zero-creation branch remains a safe candidate |
| C9: timelike/domain projection | restrict \(u_{\rm vac}\) normalization to \(D_V=\{J_V^2<0,\ J_V\ne0\}\) | REQUIRED | \(u_{\rm vac}\) remains unresolved and domain-limited |
| C10: remainder-current split | define \(J_{\rm sub}=J_V-J_{\rm exch}\) or \(J_{\rm exch}=J_V-J_{\rm sub}\) | REJECTED | current split cannot be defined by remainder |
| C11: repair-current projection | projection chooses current subspace to cancel leakage, mass shift, or scalar charge | REJECTED | current projection cannot repair boundary or recovery failures |
| C12: current-split decision | \(O_{\rm current}\) cannot make \(J_{\rm sub}/J_{\rm exch}\) operator-level until \(J_V\) and source sides exist | RECOMMENDED | next script should test projection commutation and divergence |

## Status Counts

The run counted:

```text
CANDIDATE:      3
RECOMMENDED:    1
REJECTED:       2
REQUIRED:       1
SAFE_IF:        1
THEOREM_TARGET: 4
```

Interpretation:

```text
O_current cannot make J_sub/J_exch operator-level until J_V and source sides exist.
Zero-net and zero-creation ordinary-sector branches remain useful candidates.
Remainder-current and repair-current projections are rejected.
```

## Toy Current Split Check

The script tested a role-level current vector:

\[
J_{\rm role}=
\begin{pmatrix}
j_{\rm sub}\\
j_{\rm exch}
\end{pmatrix}.
\]

The toy projectors were:

\[
P_{\rm sub}=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\qquad
P_{\rm exch}=
\begin{pmatrix}
0&0\\
0&1
\end{pmatrix}.
\]

Then:

\[
P_{\rm sub}J_{\rm role}=
\begin{pmatrix}
j_{\rm sub}\\
0
\end{pmatrix},
\qquad
P_{\rm exch}J_{\rm role}=
\begin{pmatrix}
0\\
j_{\rm exch}
\end{pmatrix}.
\]

The overlap check gives:

```text
P_sub P_exch J_role = [0, 0]^T
```

and the additive reconstruction gives:

```text
P_sub J_role + P_exch J_role = [j_sub, j_exch]^T
```

Interpretation:

```text
A toy block split can label roles without overlap.
It does not define physical J_V, J_sub, J_exch, Sigma/R, or boundary behavior.
```

## Rejected Current Branches

Rejected:

```text
remainder-current split,
repair-current projection,
undefined J_V operator split.
```

These rejections preserve the Group 18 guardrails:

```text
J_sub is not whatever remains after J_exch,
J_exch is not a repair current,
projection cannot split an undefined physical current.
```

## Failure Controls

Current-split projection fails if:

1. \(J_V\) is assumed defined.
2. \(J_{\rm sub}\) is whatever remains after \(J_{\rm exch}\).
3. \(J_{\rm exch}\) is repair current.
4. \(\Sigma/R\) become tuning knobs.
5. \(J_{\rm sub}/J_{\rm exch}\) become ordinary matter channels.
6. Current projection shifts \(M_{\rm ext}\).
7. Current projection leaks scalar trace or boundary charge.
8. \(u_{\rm vac}\) is normalized outside a timelike/nonzero \(J_V\) domain.

## What This Study Established

This study established that current-split projection remains theorem-targeted.

The split can be represented as a toy role-level block projector, but that only shows algebraic non-overlap of labels. It does not supply physical current definitions, source sides, divergence laws, or neutrality theorems.

## What This Study Did Not Establish

This study did not define \(O_{\rm current}\).

It did not define \(J_V\).

It did not derive a physical \(J_{\rm sub}/J_{\rm exch}\) split criterion.

It did not derive \(\Sigma/R\) operators.

It did not prove pure-wind neutrality.

It did not establish ordinary matter decoupling, \(M_{\rm ext}\) neutrality, scalar neutrality, or boundary neutrality.

## Next Development Target

The next script should be:

```text
candidate_projection_commutation_and_divergence.py
```

Purpose:

```text
Test whether the proposed projection roles commute with divergence,
source conservation, and sector neutrality requirements without creating
repair terms or hidden overlap.
```
