# Candidate Projection Boundary And Exterior Neutrality

## Canonical Filename

```text
candidate_projection_boundary_and_exterior_neutrality.md
```

This document summarizes the output of:

```text
candidate_projection_boundary_and_exterior_neutrality.py
```

## What This Document Is

This document is a Group 20 no-overlap / projection-operator artifact.

It is not a boundary theorem, not an exterior mass theorem, not a scalar-silence theorem, and not a derivation of an active boundary projection operator.

Its purpose is to test whether projection can preserve:

```text
boundary neutrality,
M_ext,
exterior scalar silence,
source routing neutrality,
smooth matching,
far-zone silence.
```

The locked-door question was:

```text
Can O preserve boundary neutrality, M_ext, and exterior scalar silence?
```

The result is:

```text
Boundary/exterior-neutral projection is not solved.

Diagnostic-only boundary labels remain safe.
Compact-support and interior branch filters remain candidate classes.
Counterterm, shell, far-zone, recovery, and dark patches are rejected.

Best next script:
  candidate_no_overlap_projection_group_status_summary.py
```

## Core Result

Allowed status:

```text
diagnostic-only boundary labels remain safe,
compact-support and interior branch filters remain candidate classes,
trace-free exterior-neutral and source-neutral projectors remain theorem targets.
```

Rejected:

```text
boundary counterterm projection,
shell source from projection,
far-zone hidden flux projector,
recovery-tuned exterior projector,
dark boundary patch.
```

Missing before boundary-neutral \(O\) can be real:

```text
boundary flux theorem,
M_ext neutrality theorem,
exterior scalar silence theorem,
support and smooth matching law,
source boundary routing theorem.
```

## Compact Boundary Ledger

| Entry | Candidate | Status | Consequence |
|---|---|---|---|
| B1: boundary/exterior-neutral projection target | \(O\) preserves boundary neutrality, \(M_{\rm ext}\), and exterior scalar silence | THEOREM_TARGET | boundary-neutral projection remains theorem target |
| B2: diagnostic-only boundary label | \(O\) labels interior/exterior evidence without modifying equations | SAFE_IF | safe while active boundary projection remains deferred |
| B3: compact-support structural projector | projected sector has structural zero flux at exterior boundary | CANDIDATE | candidate route for exterior scalar silence |
| B4: trace-free exterior-neutral split | projected metric/source sector is trace-neutral outside the active domain | THEOREM_TARGET | scalar silence remains unproved |
| B5: source-neutral boundary projector | \(O\) removes ordinary/exchange/curvature source overlap at the boundary | THEOREM_TARGET | source boundary neutrality remains theorem target |
| B6: interior branch filter | \(O\) acts only as an admissibility filter for interior candidate branches | CANDIDATE | usable only as pre-recovery diagnostic filter |
| B7: boundary counterterm projection | \(O\) adds or selects counterterms to cancel boundary leakage | REJECTED | projection cannot become a boundary counterterm |
| B8: shell source from projection | projection produces a shell source at the matching surface | REJECTED | projection cannot create shell matter |
| B9: far-zone hidden flux projector | projection suppresses far-zone leakage or scalar tail | REJECTED | far-zone silence must be derived, not filtered |
| B10: recovery-tuned exterior projector | choose \(O\) so Schwarzschild/PPN/exterior recovery works | REJECTED | recovery remains downstream diagnostic |
| B11: dark boundary patch | optional dark label absorbs boundary or exterior mismatch | REJECTED | dark sector remains optional downstream only |
| B12: boundary neutrality decision | active boundary-neutral \(O\) remains deferred; diagnostic labels and compact-support candidates survive | RECOMMENDED | Group 20 can close with \(O\) still theorem-targeted |

## Status Counts

The run counted:

```text
CANDIDATE:      2
RECOMMENDED:    1
REJECTED:       5
SAFE_IF:        1
THEOREM_TARGET: 3
```

Interpretation:

```text
Boundary/exterior-neutral projection remains theorem-targeted.
Diagnostic labels and structurally compact-support candidates remain safe routes.
Counterterm, shell, far-zone, recovery, and dark patches are rejected.
```

## Surface Flux Diagnostic

The script tested an exterior scalar-tail diagnostic:

\[
\phi_{\rm tail}=\frac{A}{r}.
\]

The surface flux proxy is:

\[
4\pi r^2\frac{d\phi_{\rm tail}}{dr} =
-4\pi A.
\]

This is nonzero unless \(A=0\), so a \(1/r\) exterior scalar tail carries surface flux.

The script also tested a compact-support toy profile:

\[
\phi_{\rm compact} =
\phi_0\left(1-\frac{r^2}{R^2}\right)^2.
\]

At \(r=R\):

```text
[4*pi*r^2*d(phi_compact)/dr] at r=R = 0
```

Interpretation:

```text
A compact-support toy can have zero boundary flux, but only as a diagnostic shape.
A real theory must derive support and matching; projection cannot impose them after leakage appears.
```

## Rejected Boundary Branches

Rejected:

```text
boundary counterterm projection,
shell source from projection,
far-zone hidden flux projector,
recovery-tuned exterior projector,
dark boundary patch.
```

These rejections preserve the prior guardrails:

```text
no M_ext shift,
no exterior scalar charge,
no boundary repair,
no shell source from projection,
no far-zone hidden flux,
no recovery-chosen projection,
no dark-sector patch.
```

## Failure Controls

Boundary/exterior projection fails if:

1. \(O\) shifts \(M_{\rm ext}\).
2. \(O\) hides exterior scalar charge.
3. \(O\) adds a boundary counterterm.
4. \(O\) creates a shell source at the matching surface.
5. \(O\) suppresses far-zone hidden flux.
6. \(O\) is tuned by Schwarzschild/PPN recovery.
7. \(O\) invokes a dark boundary patch.
8. \(O\) converts boundary mismatch into source-sector routing.

## What This Study Established

This study established that boundary/exterior-neutral projection remains theorem-targeted.

The surface-flux diagnostic shows why exterior scalar silence cannot be asserted by naming a projector. A \(1/r\) scalar tail carries nonzero surface flux. A compact-support toy can have zero boundary flux, but the support and matching law must be derived, not imposed after leakage appears.

## What This Study Did Not Establish

This study did not define a boundary-neutral \(O\).

It did not prove \(M_{\rm ext}\) neutrality.

It did not prove exterior scalar silence.

It did not derive compact support or smooth matching.

It did not derive source boundary routing.

It did not make boundary counterterms, shell sources, far-zone filters, recovery-tuned projectors, or dark boundary patches admissible.

## Next Development Target

The next script should be:

```text
candidate_no_overlap_projection_group_status_summary.py
```

Purpose:

```text
Close Group 20 by summarizing the no-overlap/projector status,
the role-specific projector requirements, all deferred obligations,
the rejected repair branches, and the consequence for parent equation readiness.
```
