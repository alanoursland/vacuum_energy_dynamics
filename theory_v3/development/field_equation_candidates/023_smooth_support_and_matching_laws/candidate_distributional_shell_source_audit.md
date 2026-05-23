# Candidate Distributional Shell Source Audit

## Canonical Filename

```text
candidate_distributional_shell_source_audit.md
```

This document summarizes the output of:

```text
candidate_distributional_shell_source_audit.py
```

## What This Document Is

This document is the second artifact for `23_smooth_support_and_matching_laws/`.

It is not a no-shell theorem, not a compact-support theorem, not a boundary-neutrality theorem, not a scalar-silence theorem, and not a parent field equation.

Its purpose is to audit distributional shell terms that appear when boundary profiles are cut off.

The locked-door question was:

```text
What distributional shell terms appear when boundary profiles are cut off?
```

The result is:

```text
A sharp cutoff can create delta-shell behavior from nonzero f(R).

Value matching f(R)=0 removes the first value-jump diagnostic,
but does not remove slope / flux danger.

Slope matching f'(R)=0 is a necessary diagnostic no-flux condition.

Value+slope matching is still not a support theorem.

Structural support, distributional shell absence, recovery independence,
and source compatibility remain open.
```

Tiny goblin label:

```text
Sharp edge makes shell crumbs.
Sweep before claiming silence.
```

---

## Archive Dependency Status

The run reported a clean archive dependency check:

```text
matching_ladder_dep_23: dependency_satisfied
g22_targets_dep_23: dependency_satisfied
g22_repair_dep_23: dependency_satisfied
```

So the shell-source audit was connected to the Group 23 matching ladder, the Group 22 target ledger, and the Group 22 repair-route exclusion ledger.

---

## Cutoff Profile Form

The script audited profiles of the form:

\[
\phi(r)=f(r)\Theta(R-r).
\]

The diagnostic derivative rule is:

\[
\frac{d}{dr}\left[f(r)\Theta(R-r)\right]
=
f'(r)\Theta(R-r)-f(R)\delta(R-r).
\]

So a nonzero boundary value \(f(R)\) creates a value-jump delta-shell diagnostic.

The reduced boundary flux diagnostic is:

\[
F_R=4\pi R^2 f'(R).
\]

So even when \(f(R)=0\), a nonzero \(f'(R)\) can still carry boundary flux.

---

## Cutoff Profile Diagnostics

### S0: constant cutoff

\[
f(r)=\phi_0.
\]

At \(R\):

\[
f(R)=\phi_0,
\]

\[
f'(R)=0.
\]

The first-derivative delta coefficient is:

\[
-f(R)=-\phi_0.
\]

Status:

```text
REJECTED
```

Interpretation:

```text
Exterior zero does not erase a nonzero boundary value.
```

### S1: linear value-match cutoff

\[
f(r)=\phi_0\left(1-\frac{r}{R}\right).
\]

At \(R\):

\[
f(R)=0,
\]

\[
f'(R)=-\frac{\phi_0}{R}.
\]

The first-derivative delta coefficient is zero, but the boundary flux is:

\[
4\pi R^2 f'(R)=-4\pi R\phi_0.
\]

The shell-like second-order coefficient is:

\[
-R^2f'(R)=R\phi_0.
\]

Status:

```text
RISK
```

Interpretation:

```text
Value matching alone does not prove no-shell / no-flux behavior.
```

### S2: quadratic value+slope cutoff

\[
f(r)=\phi_0\left(1-\frac{r}{R}\right)^2.
\]

At \(R\):

\[
f(R)=0,
\]

\[
f'(R)=0.
\]

The value-jump coefficient, boundary flux, and slope-shell diagnostic vanish.

Status:

```text
SAFE_IF
```

Interpretation:

```text
Diagnostically safe only if higher distributional, support, source, and recovery burdens are also controlled.
```

### S3: cubic value+slope+curvature cutoff

\[
f(r)=\phi_0\left(1-\frac{r}{R}\right)^3.
\]

At \(R\):

\[
f(R)=0,
\]

\[
f'(R)=0.
\]

The value-jump coefficient, boundary flux, and slope-shell diagnostic vanish.

Status:

```text
SAFE_IF
```

Interpretation:

```text
Stronger toy regularity, still not a support theorem.
```

### S4: smooth bump cutoff

\[
f(r)=\phi_0\left(1-\frac{r^2}{R^2}\right)^2.
\]

At \(R\):

\[
f(R)=0,
\]

\[
f'(R)=0.
\]

The value-jump coefficient, boundary flux, and slope-shell diagnostic vanish.

Status:

```text
SAFE_IF
```

Interpretation:

```text
Useful diagnostic class, but still requires support origin, recovery independence, and source compatibility.
```

---

## Distributional Shell Audit Ledger

| Entry | Shell Source | Appears When | Status | Consequence |
|---|---|---|---|---|
| D1 | \(\delta(R-r)\) from \(d[f(r)\Theta(R-r)]/dr\) | \(f(R)\neq0\) | REJECTED | exterior zero does not erase a nonzero boundary value |
| D2 | boundary flux / reduced radial shell-like term from \(f'(R)\) | \(f(R)=0\) but \(f'(R)\neq0\) | RISK | value matching alone does not prove no-shell / no-flux behavior |
| D3 | curvature / second-derivative edge behavior | higher derivatives uncontrolled or profile only toy-smooth | SAFE_IF | higher derivative behavior must be audited before support theorem claims |
| D4 | structural support law | support origin, value/slope matching, distributional shell absence, recovery independence, and source compatibility are derived | THEOREM_TARGET | positive no-shell route remains open but not derived |

---

## Rejected Shell-Source Shortcuts

The script rejected:

```text
sharp cutoff as scalar silence,
value match as no-shell,
slope match as full theorem,
smoothing hides shell,
repair object cancels shell.
```

These are governance exclusions. They prevent cutoff diagnostics from being mistaken for no-shell support.

---

## What This Study Established

This study established that:

```text
f(r)*Theta(R-r) is not compact support by declaration.

A nonzero f(R) creates a value-jump delta-shell diagnostic.

f(R)=0 alone is not enough.

A nonzero f'(R) can still carry boundary flux or shell-like radial diagnostic.

f(R)=0 and f'(R)=0 are necessary diagnostic no-shell/no-flux conditions.

Value+slope matching is still not a full support theorem.
```

---

## What This Study Did Not Establish

This study did not prove:

```text
no-shell matching,
compact support,
boundary neutrality,
scalar silence,
support origin,
higher derivative regularity,
transition-layer neutrality,
recovery-independent support,
source compatibility,
parent field equation readiness.
```

---

## Failure Controls

The distributional shell source audit fails if later scripts allow:

1. \(f(r)\Theta(R-r)\) to count as compact support by declaration.
2. Nonzero \(f(R)\) value jump to be ignored.
3. \(f(R)=0\) alone to prove no shell.
4. Nonzero \(f'(R)\) boundary flux to be ignored.
5. \(f(R)=f'(R)=0\) to be treated as full support law.
6. Smoothing layer to replace distributional audit.
7. O, H, dark, curvature, exchange, or current repair to cancel shell terms.
8. Recovery-selected support to determine where the cutoff lives.
9. Parent equation to open from no-shell diagnostics alone.

---

## Next Development Target

The next script should be:

```text
candidate_compact_support_admissibility_conditions.py
```

Purpose:

```text
Separate admissible structural compact support from declared compact support.
```

Expected role:

```text
diagnostic / requirements audit;
not a compact-support theorem.
```
