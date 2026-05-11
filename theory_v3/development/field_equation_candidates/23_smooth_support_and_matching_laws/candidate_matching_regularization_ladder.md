# Candidate Matching Regularization Ladder

## Canonical Filename

```text
candidate_matching_regularization_ladder.md
```

This document summarizes the output of:

```text
candidate_matching_regularization_ladder.py
```

## What This Document Is

This document is the opening artifact for `23_smooth_support_and_matching_laws/`.

It is not a compact-support theorem, not a no-shell theorem, not a boundary-neutrality theorem, not a scalar-silence theorem, and not a parent field equation.

Its purpose is to build the first Group 23 matching regularization ladder.

The locked-door question was:

```text
What matching regularity is required at the boundary?
```

The result is:

```text
Value jump is rejected.

Value matching alone is risky.

Value+slope matching is a necessary diagnostic condition for zero boundary scalar flux.

Curvature / second-derivative behavior needs explicit audit.

Smooth compact bumps are useful diagnostics but not support laws.

Derived support / matching law remains theorem-targeted.
```

Tiny goblin label:

```text
Inspect the seam.
Count the jumps.
Trust no smooth paint.
```

---

## Archive Dependency Status

The run reported a clean archive dependency check:

```text
g22_summary_dep_23: dependency_satisfied
g22_smooth_dep_23: dependency_satisfied
g22_targets_dep_23: dependency_satisfied
g22_obligation_dep_23: dependency_satisfied
```

So the Group 23 opening script was connected to the Group 22 status summary, smooth compact support / no-shell audit, boundary/scalar target ledger, and boundary-neutrality theorem obligations.

---

## Diagnostic Profiles

The script audited toy profiles at a boundary \(r=R\), using:

```text
phi(R)
phi'(R)
phi''(R)
F_R = 4*pi*R^2*phi'(R)
```

### P0: value-jump constant

\[
\phi(r)=\phi_0.
\]

At the boundary:

\[
\phi(R)=\phi_0,
\]

\[
\phi'(R)=0,
\]

\[
F_R=0.
\]

If the exterior value is zero, then \(\phi(R)=\phi_0\) is a value jump. Zero interior slope does not make the boundary safe.

### P1: value-match linear

\[
\phi(r)=\phi_0\left(1-\frac{r}{R}\right).
\]

At the boundary:

\[
\phi(R)=0,
\]

\[
\phi'(R)=-\frac{\phi_0}{R},
\]

\[
F_R=-4\pi R\phi_0.
\]

So value matching alone can still carry boundary flux.

### P2: value+slope match quadratic

\[
\phi(r)=\phi_0\left(1-\frac{r}{R}\right)^2.
\]

At the boundary:

\[
\phi(R)=0,
\]

\[
\phi'(R)=0,
\]

\[
\phi''(R)=\frac{2\phi_0}{R^2},
\]

\[
F_R=0.
\]

This is a necessary diagnostic condition for no boundary scalar flux, but not a support theorem.

### P3: value+slope+curvature diagnostic

\[
\phi(r)=\phi_0\left(1-\frac{r}{R}\right)^3.
\]

At the boundary:

\[
\phi(R)=0,
\]

\[
\phi'(R)=0,
\]

\[
\phi''(R)=0,
\]

\[
F_R=0.
\]

This is a stronger diagnostic regularity level, but still not a derived support law.

### P4: smooth compact bump toy

\[
\phi(r)=\phi_0\left(1-\frac{r^2}{R^2}\right)^2.
\]

At the boundary:

\[
\phi(R)=0,
\]

\[
\phi'(R)=0,
\]

\[
\phi''(R)=\frac{8\phi_0}{R^2},
\]

\[
F_R=0.
\]

This is a useful diagnostic class, but smoothness does not prove recovery independence, source compatibility, or no hidden layer load.

---

## Matching Regularization Ladder

| Entry | Matching Level | Status | Consequence |
|---|---|---|---|
| L0 | value jump | REJECTED | not admissible as compact support or scalar silence |
| L1 | value match only | RISK | value matching alone does not prove no-shell or no-flux behavior |
| L2 | value and slope match | SAFE_IF | necessary diagnostic condition for no boundary scalar flux, not a theorem |
| L3 | curvature diagnostic match | SAFE_IF | stronger diagnostic regularity level |
| L4 | smooth compact bump | SAFE_IF | promising diagnostic class, not structural support |
| L5 | derived matching / support law | THEOREM_TARGET | positive route for future boundary / scalar silence |

---

## Rejected Ladder Upgrades

The script rejected:

```text
exterior zero becomes compact-support proof,
value match becomes no-shell proof,
slope match becomes full support law,
smooth toy profile becomes structural smoothing,
matching ladder opens parent gate.
```

These are governance exclusions. They prevent diagnostic regularity from being mistaken for derived support.

---

## What This Study Established

This study established the Group 23 opening ladder:

```text
value jump -> rejected,
value matching alone -> risky,
value+slope matching -> necessary diagnostic condition,
second-derivative behavior -> explicit audit needed,
smooth compact toy -> diagnostic only,
derived support/matching law -> theorem target.
```

It also confirmed the Group 22 warning:

```text
C1 value matching can carry boundary flux.
```

---

## What This Study Did Not Establish

This study did not prove:

```text
compact support,
no-shell matching,
boundary neutrality,
scalar silence,
distributional shell absence,
recovery-independent support,
source compatibility,
parent field equation readiness.
```

It only classifies boundary regularity diagnostics.

---

## Failure Controls

The matching regularization ladder audit fails if later scripts allow:

1. Compact support by exterior zero alone.
2. C0/value jump to count as boundary silence.
3. C1 value matching to count as no-shell/no-flux proof.
4. C2 value/slope matching to count as derived support law.
5. Smooth toy bump to count as structural smoothing.
6. Derivative or curvature jumps to be ignored.
7. Support radius chosen from recovery.
8. O, H, dark, curvature, exchange, or current repair of a seam.
9. Diagnostic matching ladder to open parent equation gate.

---

## Next Development Target

The next script should be:

```text
candidate_distributional_shell_source_audit.py
```

Purpose:

```text
Audit the distributional shell terms that appear when boundary profiles are cut off.
```

Expected role:

```text
diagnostic / requirements audit;
not a no-shell theorem.
```
