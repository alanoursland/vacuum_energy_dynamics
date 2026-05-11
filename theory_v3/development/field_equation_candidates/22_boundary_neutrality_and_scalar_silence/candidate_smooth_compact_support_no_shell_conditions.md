# Candidate Smooth Compact Support No-Shell Conditions

## Canonical Filename

```text
candidate_smooth_compact_support_no_shell_conditions.md
```

This document summarizes the output of:

```text
candidate_smooth_compact_support_no_shell_conditions.py
```

## What This Document Is

This document is the second artifact for `22_boundary_neutrality_and_scalar_silence/`.

It is not a compact-support theorem, not a boundary-neutrality proof, not a scalar-silence proof, not a residual-kill derivation, and not a recovery construction.

Its purpose is to test when compact support or boundary matching avoids hiding a shell source.

The locked-door question was:

```text
When does compact support avoid hiding a shell source?
```

The result is:

```text
Value matching alone is not enough.

A C1-style profile can have phi(R)=0 while carrying nonzero boundary flux.

Value and slope matching are safer diagnostic conditions.

Sharp support can hide a shell if the value or derivative matching is uncontrolled.

Compact support is safe only with matching/no-shell conditions,
and those conditions remain theorem-targeted.
```

Tiny goblin label:

```text
A smooth edge is not a magic edge.
Show the seam.
```

---

## Archive Dependency Status

The run reported a clean archive dependency check:

```text
boundary_scalar_silence_target_ledger_dependency_22: dependency_satisfied
scalar_tail_flux_witness_dependency_22: dependency_satisfied
boundary_A_tail_mass_witness_dependency_22: dependency_satisfied
```

So the script was correctly connected to the Group 22 target ledger and its scalar-tail / boundary-tail witnesses.

---

## Diagnostic Boundary Profiles

The script compared four toy profile types at a boundary \(r=R\).

### C0-style interior constant profile

\[
\phi_{C0}(r)=\phi_0.
\]

At the boundary:

\[
\phi_{C0}(R)=\phi_0,
\]

\[
\phi'_{C0}(R)=0,
\]

\[
4\pi R^2\phi'_{C0}(R)=0.
\]

If the exterior value is zero, then nonzero \(\phi_0\) means a value jump. Zero interior slope does not make a discontinuous cutoff safe.

### C1-style value-match profile

\[
\phi_{C1}(r)=\phi_0\left(1-\frac{r}{R}\right).
\]

At the boundary:

\[
\phi_{C1}(R)=0,
\]

\[
\phi'_{C1}(R)=-\frac{\phi_0}{R},
\]

\[
4\pi R^2\phi'_{C1}(R)=-4\pi R\phi_0.
\]

So value matching alone can still leave boundary flux.

### C2-style value-and-slope profile

\[
\phi_{C2}(r)=\phi_0\left(1-\frac{r}{R}\right)^2.
\]

At the boundary:

\[
\phi_{C2}(R)=0,
\]

\[
\phi'_{C2}(R)=0,
\]

\[
4\pi R^2\phi'_{C2}(R)=0.
\]

This is safer as a diagnostic boundary profile, though it is still not a derived compact-support law.

### Smooth compact toy profile

\[
\phi_{\rm compact}(r)=\phi_0\left(1-\frac{r^2}{R^2}\right)^2.
\]

At the boundary:

\[
\phi_{\rm compact}(R)=0,
\]

\[
\phi'_{\rm compact}(R)=0,
\]

\[
4\pi R^2\phi'_{\rm compact}(R)=0.
\]

This is a promising diagnostic class for no-shell behavior, but support and matching must still be structural, not chosen after leakage appears.

---

## Sharp Support / Shell Danger

The sharp-support toy is:

```text
phi_inside(r) = phi0
phi_outside(r) = 0
```

At the boundary, there is a value jump if \(\phi_0\neq0\), even though the inside slope and inside flux are zero.

Interpretation:

```text
zero interior slope does not save a sharp cutoff if the value jumps.

A value jump can encode distributional boundary behavior.

Compact support must include matching/no-shell conditions,
not only exterior zero.
```

---

## Smooth Compact Support Branch Ledger

| Entry | Branch | Status | Consequence |
|---|---|---|---|
| B1 | C0 / value-jump profile | REJECTED | not a safe compact-support condition |
| B2 | C1 value match | RISK | value continuity alone does not prove no-shell/no-flux behavior |
| B3 | C2 value and slope match | SAFE_IF | safe diagnostic condition, not a compact-support theorem |
| B4 | smooth compact bump | SAFE_IF | promising diagnostic class for no-shell behavior |
| B5 | sharp cutoff | REJECTED | sharp support is not neutral by declaration |
| B6 | derivative jump | REJECTED | no-shell condition must control derivative matching |
| B7 | derived compact support | THEOREM_TARGET | target for future boundary neutrality theorem |

---

## Rejected Compact-Support Shortcuts

The script rejected:

```text
compact support by declaration,
recovery-selected support radius,
derivative jump shell,
residual-kill called support theorem,
smoothing as repair.
```

These are governance exclusions. They do not prove no-shell behavior; they prevent fake no-shell behavior.

---

## What This Study Established

This study established the diagnostic matching burden:

```text
phi(R) = 0,
phi'(R) = 0,
no derivative jump,
no shell source,
support/matching law derived before recovery.
```

It also established that:

```text
C1 value matching may still carry boundary flux.

C2 and smooth compact toy profiles are safer diagnostics because they have zero value and zero slope at the boundary.

Sharp support is not safe by name.
```

---

## What This Study Did Not Establish

This study did not derive:

```text
compact support,
boundary neutrality,
scalar silence,
no-shell theorem,
residual-kill theorem,
support law,
recovery-independent boundary data,
parent field equation.
```

---

## Failure Controls

The smooth compact support no-shell audit fails if later scripts allow:

1. Compact support by declaration.
2. Exterior zero to replace boundary matching.
3. Value continuity alone to prove no shell.
4. Derivative jump to hide shell flux.
5. Smoothing selected after recovery failure.
6. Support radius chosen from Schwarzschild, PPN, gamma_like, AB, or \(B=1/A\).
7. Residual-kill treated as a compact-support theorem.
8. Sharp cutoff called scalar silence.
9. \(O\), \(H\), dark label, curvature, or exchange used to repair a boundary seam.

---

## Next Development Target

The next script should be:

```text
candidate_scalar_tail_silence_sector_conditions.py
```

Purpose:

```text
Apply scalar silence to each residual sector.
```

Expected role:

```text
requirements / sector audit;
not a scalar-silence theorem.
```
