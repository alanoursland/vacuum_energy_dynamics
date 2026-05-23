# Candidate Curvature Boundary And Mass Neutrality

## Canonical Filename

```text
candidate_curvature_boundary_and_mass_neutrality.md
```

This document summarizes the output of:

```text
candidate_curvature_boundary_and_mass_neutrality.py
```

## What This Document Is

This document is a Group 17 curvature-energy / finite-admissibility artifact.

It is not a proof of exterior neutrality, not a definition of \(J_{\rm curv}\), not an anti-singularity theorem, and not a parent correction tensor.

Its purpose is to test whether curvature admissibility or \(J_{\rm curv}\) alters exterior mass, creates boundary repair behavior, or leaks an ordinary-sector scalar charge.

The locked-door question was:

```text
Does curvature admissibility or J_curv alter exterior mass,
create boundary repair behavior,
or leak an ordinary-sector scalar charge?
```

The result is:

```text
Curvature boundary/mass neutrality is required but not derived.

Safest fallback:

  curvature admissibility remains interior diagnostic / branch-filter only.

Candidate safe routes:

  compact support
  smooth transition
  exterior-neutral J_curv
  boundary diagnostic only

Rejected:

  e_curv mass reservoir
  J_curv boundary repair
  boundary counterterm singularity avoidance
  recovery-tuned smoothing

Best next script:

  candidate_curvature_anti_singularity_claim_audit.py
```

## Core Result

Boundary/mass neutrality is required, but not derived.

The ordinary-sector safety requirement is:

```text
curvature admissibility / J_curv creates:
  no exterior mass shift,
  no boundary repair current,
  no exterior scalar charge,
  no far-zone hidden flux,
  no hidden matter coupling,
  no recovery-tuned smoothing,
  no boundary counterterm singularity avoidance,
  no H_curv repair.
```

The safest current role remains:

```text
interior-only diagnostic / branch-filter admissibility.
```

## Compact Curvature Neutrality Ledger

| Entry | Neutrality Rule | Status | Consequence |
|---|---|---|---|
| CN1: curvature boundary/mass neutrality target | curvature admissibility / \(J_{\rm curv}\) creates no exterior mass shift, boundary repair, or ordinary scalar leakage | THEOREM_TARGET | decides whether curvature admissibility can remain ordinary-sector safe |
| CN2: no \(M_{\rm ext}\) shift | \(\delta M_{\rm ext}|_{\rm curv}=0\) unless derived through A-sector source law | REQUIRED | protects strongest reduced A-sector result |
| CN3: no boundary repair current | \(J_{\rm curv}\) or boundary functional does not cancel blowup, leakage, or mass shift at boundary | REQUIRED | prevents singularity avoidance by boundary patch |
| CN4: no exterior scalar charge | curvature admissibility creates no exterior \(\zeta/\kappa\)/scalar charge | REQUIRED | prevents curvature admissibility from becoming scalar gravity |
| CN5: no far-zone curvature flux | no ordinary-sector far-zone curvature/admissibility flux unless a real radiative channel is derived | REQUIRED | protects ordinary radiation constraints |
| CN6: no hidden matter coupling | curvature admissibility does not modify ordinary matter coupling or double-count \(T_{\mu\nu}\) | REQUIRED | prevents matter-sector repair behavior |
| CN7: no recovery-tuned smoothing | boundary smoothing/support is not chosen to pass \(\gamma_{\rm like}\), \(AB\), or exterior matching | REQUIRED | keeps recovery downstream |
| CN8: interior-only admissibility branch | finite admissibility acts only as interior branch filter / diagnostic | SAFE_IF | keeps anti-singularity claim at diagnostic/branch-filter level |
| CN9: compact curvature support candidate | curvature admissibility support is compact or decays structurally with no exterior tail | CANDIDATE | possible path to exterior neutrality if made real |
| CN10: boundary flux diagnostic only | boundary flux may diagnose admissibility leakage but cannot define physical repair flux | SAFE_IF | useful for audits without hardening scaffold |
| CN11: smooth finite-admissible transition candidate | interior finite-admissible region transitions smoothly to exterior without shell source | CANDIDATE | possible if no recovery tuning or shell source |
| CN12: \(J_{\rm curv}\) exterior-neutral candidate | \(J_{\rm curv}\) is zero, tangent, diagnostic, or compact at ordinary exterior boundary | CANDIDATE | could keep current candidate alive if current is later defined |
| CN13: \(e_{\rm curv}\) mass reservoir rejection | \(e_{\rm curv}\) contributes to \(M_{\rm ext}\) or boundary mass as free reservoir | REJECTED | preserves curvature-energy fence |
| CN14: \(J_{\rm curv}\) boundary repair rejection | \(J_{\rm curv}\) chosen to cancel boundary leakage, singularity, or mass shift | REJECTED | prevents painted current safety |
| CN15: singularity avoidance by boundary counterterm rejection | finite admissibility restored by boundary counterterm/cutoff | REJECTED | prevents boundary hiding |
| CN16: \(\zeta\)/volume coupling guard | curvature-volume coupling cannot reopen \(B_s/F_\zeta\), residual trace, or \(O\) | RISK | keeps curvature branch from undoing metric-insertion controls |
| CN17: \(H_{\rm curv}\) deferred | \(H_{\rm curv}\) is not introduced to enforce neutrality in Group 17 | DEFER | prevents premature parent correction |
| CN18: anti-singularity claim guard | boundary/mass neutral admissibility does not by itself prove bounce or regular core | REQUIRED | keeps anti-singularity claims honest |
| CN19: neutrality failure | curvature admissibility/\(J_{\rm curv}\) shifts \(M_{\rm ext}\), repairs boundary, leaks scalar charge, or reroutes matter | BRANCH_KILLED | curvature admissibility must remain diagnostic-only or be rejected |
| CN20: recommended next move | after boundary/mass neutrality audit, test anti-singularity claim level | RECOMMENDED | next script should be `candidate_curvature_anti_singularity_claim_audit.py` |

## Status Counts

```text
BRANCH_KILLED: 1
CANDIDATE:     3
DEFER:         1
RECOMMENDED:   1
REJECTED:      3
REQUIRED:      7
RISK:          1
SAFE_IF:       2
THEOREM_TARGET:1
```

Interpretation:

```text
Boundary/mass neutrality is required but not derived.

Interior-only diagnostic admissibility is the safest fallback.

Compact support, smooth transition, and exterior-neutral J_curv are candidates only if support/orientation laws become real.

e_curv mass reservoir, J_curv boundary repair, and boundary counterterm avoidance are rejected.

H_curv remains deferred.

Next gate is anti-singularity claim level.
```

## Possible Neutrality Routes

Possible safe routes:

```text
1. interior-only admissibility diagnostic
2. compact curvature support
3. boundary flux diagnostic only
4. smooth finite-admissible transition
5. J_curv exterior-neutral candidate
```

Rejected routes:

```text
1. e_curv mass reservoir
2. J_curv boundary repair
3. boundary counterterm singularity avoidance
4. recovery-tuned smoothing
5. hidden ordinary matter rerouting
```

## Boundary/Mass Neutrality Decision Tree

```text
1. Interior diagnostic only:
   safest if no exterior mass/charge/flux effect.

2. Compact support:
   candidate only if support is derived.

3. Smooth transition:
   candidate only if not recovery-tuned and no shell source.

4. J_curv exterior-neutral:
   candidate only if J_curv has real direction/support law.

5. Boundary flux diagnostic:
   allowed only as diagnostic, not physical repair.

6. Any M_ext shift, scalar leakage, matter rerouting, or boundary repair:
   branch killed.
```

## Good Failure / Branch Decision

Good failure:

```text
curvature admissibility/J_curv cannot be made exterior-neutral.
```

Consequence:

```text
keep curvature admissibility diagnostic-only or reject the unsafe current/object.
do not patch with boundary counterterms, e_curv reservoirs, or H_curv.
```

Bad failure:

```text
call a boundary repair current “neutrality”
and proceed to anti-singularity claims.
```

## Failure Controls

Curvature boundary/mass neutrality fails if:

1. \(M_{\rm ext}\) shifts independently of \(A\).
2. boundary repair current appears.
3. exterior scalar charge appears.
4. hidden far-zone curvature/scalar flux appears.
5. ordinary matter coupling is rerouted.
6. recovery-tuned smoothing is used.
7. singularity avoidance uses boundary counterterm.
8. \(e_{\rm curv}\) becomes mass reservoir.
9. \(\zeta\)/volume coupling reopens Group 16.
10. \(H_{\rm curv}\) is introduced as repair.
11. neutrality is used to claim bounce / regular core.

## What This Study Established

This study established that curvature admissibility must be ordinary-sector neutral before it can support stronger claims.

It did not prove neutrality.

The safest current role remains:

```text
interior diagnostic / branch-filter only.
```

## What This Study Did Not Establish

This study did not prove no \(M_{\rm ext}\) shift.

It did not prove boundary neutrality.

It did not prove no exterior scalar charge.

It did not prove no far-zone hidden flux.

It did not define \(J_{\rm curv}\).

It did not define a support law.

It did not justify \(H_{\rm curv}\).

It did not license bounce, regular-core, or dynamical singularity-avoidance claims.

## Current Best Interpretation

```text
Curvature admissibility is allowed to diagnose or filter branches.

It cannot yet alter exterior mass,
repair boundaries,
leak scalar charge,
reroute matter,
or support a dynamical anti-singularity claim.
```

## Next Development Target

The next script should be:

```text
candidate_curvature_anti_singularity_claim_audit.py
```

Purpose:

```text
Audit what anti-singularity claim, if any, is currently licensed.
```

Reason:

```text
After fencing object, condition, energy, current, balance, and neutrality,
the next risk is overclaim:
bounce,
regular core,
or dynamical avoidance.
```

Expected result:

```text
An anti-singularity claim ledger:
  diagnostic claim,
  branch-kill claim,
  dynamical avoidance claim,
  bounce claim,
  regular-core claim,
  finite-admissibility theorem target,
  required dynamics/solution burden,
  overclaim rejection,
  H_curv deferral.
```

## Summary

The neutrality result is:

```text
Curvature may diagnose the interior.
It may not steal mass from the exterior.
```

Tiny goblin plaque:

```text
No boundary patch coins.
No mass coins from A’s purse.
