# Candidate H_exch Definition Requirements

## Canonical Filename

```text
candidate_H_exch_definition_requirements.md
```

This document summarizes the output of:

```text
candidate_H_exch_definition_requirements.py
```

## What This Document Is

This document is a Group 19 parent-correction tensor audit artifact.

It is not a definition of \(H_{\rm exch}\), not a parent field equation, not an exchange-continuity law, and not a divergence-safety proof.

Its purpose is to state what \(H_{\rm exch}\) would need to be before it can become more than exchange-continuity paint.

The locked-door question was:

```text
What must H_exch be to be more than exchange-continuity paint?
```

The result is:

```text
H_exch is not defined yet.

It survives only as theorem target / diagnostic-only fallback requiring:

  J_V or J_exch definition
  Sigma/R operators
  source/relaxation distinction
  domain
  orientation / flux behavior
  projection class
  tensor symmetry
  divergence behavior
  boundary behavior
  ordinary matter decoupling
  M_ext neutrality
  scalar trace neutrality
  coefficient origin
  zero-net / zero-creation preservation

Rejected:

  exchange-continuity paint
  Sigma/R tuning tensor
  boundary repair tensor
  ordinary matter rerouting
  dark-sector patch
  recovery-fit correction

Best next script:

  candidate_correction_tensor_divergence_safety.py
```

## Core Result

\(H_{\rm exch}\) is not defined yet.

It remains a theorem target or diagnostic-only fallback.

A real \(H_{\rm exch}\) must have:

```text
J_V or J_exch definition,
Sigma/R operators,
source/relaxation distinction,
ordinary-sector source-side status,
domain,
orientation / flux behavior,
projection class,
tensor symmetry / trace behavior,
divergence behavior,
boundary behavior,
ordinary matter decoupling,
M_ext neutrality,
scalar trace neutrality,
coefficient origin,
zero-net / zero-creation preservation,
dark-sector no-patch guard.
```

The current safest fallback is:

```text
diagnostic-only H_exch-like audit object,
not inserted into a field equation.
```

## Compact H_exch Requirements Ledger

| Entry | Requirement | Status | Consequence |
|---|---|---|---|
| HE1: \(H_{\rm exch}\) definition target | \(H_{\rm exch}\) has \(J_V/J_{\rm exch}\) definition, \(\Sigma/R\) operators, source/relaxation distinction, domain, orientation, projection class, tensor symmetry, divergence behavior, boundary behavior, ordinary matter decoupling, \(M_{\rm ext}\) neutrality, and scalar trace neutrality | THEOREM_TARGET | decides whether exchange correction tensor language can become technical |
| HE2: \(J_V\) absence guard | \(J_V\) remains unresolved and cannot be used as \(H_{\rm exch}\) source/current | REQUIRED | preserves Group 18 vacuum-current result |
| HE3: \(J_{\rm exch}\) theorem-target guard | \(J_{\rm exch}\) remains active-exchange theorem target only | REQUIRED | prevents exchange-current hardening by tensor name |
| HE4: \(\Sigma/R\) operator requirement | \(\Sigma_{\rm exch}\) and \(R_{\rm exch}\) are defined as operators before \(H_{\rm exch}\) uses them | REQUIRED | prevents exchange-continuity paint |
| HE5: source/relaxation distinction requirement | \(\Sigma_{\rm exch}\) and \(R_{\rm exch}\) are not two names for one hidden tuning mechanism | REQUIRED | prevents exchange tuning tensor |
| HE6: ordinary-sector source-side absence guard | no active ordinary-sector source side for \(J_{\rm exch}\) is derived | REQUIRED | preserves zero-net / zero-creation ordinary branches |
| HE7: domain requirement | domain \(D_{\rm exch}/H_{\rm exch}\) where correction acts is specified | REQUIRED | prevents convenient exchange-support tensor |
| HE8: orientation / flux behavior requirement | \(H_{\rm exch}\) relation to exchange flux direction or transport behavior is specified | REQUIRED | prevents repair-current tensor |
| HE9: projection class requirement | \(H_{\rm exch}\) projection class is specified: spacetime tensor, spatial tensor, projected exchange-sector tensor, or diagnostic-only object | REQUIRED | prevents fake covariant-enough exchange tensor |
| HE10: tensor symmetry requirement | \(H_{\rm exch}\) tensor rank, symmetry, trace behavior, and index placement are specified | REQUIRED | prevents decorative tensor symbol |
| HE11: divergence behavior requirement | \(H_{\rm exch}\) divergence behavior is specified without decorative continuity or Bianchi language | REQUIRED | prevents fake parent compatibility |
| HE12: boundary behavior requirement | \(H_{\rm exch}\) has no boundary repair flux, shell hiding, scalar tail cancellation, or \(M_{\rm ext}\) shift | REQUIRED | protects exterior sector |
| HE13: ordinary matter decoupling requirement | \(H_{\rm exch}\) does not reroute ordinary \(T_{\mu\nu}\), ordinary \(\rho\), or scalar charge | REQUIRED | protects ordinary matter coupling |
| HE14: \(M_{\rm ext}\) neutrality requirement | \(\delta M_{\rm ext}|_{H_{\rm exch}}=0\) unless derived through established A-sector source law | REQUIRED | protects strongest reduced A-sector result |
| HE15: scalar trace neutrality requirement | \(H_{\rm exch}\) does not reopen \(B_s/F_\zeta\), residual trace, \(\kappa\), or exterior scalar charge | REQUIRED | preserves Group 16 guardrails |
| HE16: coefficient origin requirement | \(H_{\rm exch}\) coefficients have ontology-native, action, stiffness, or exchange-source origin | REQUIRED | prevents exchange-continuity tuning |
| HE17: zero-net / zero-creation preservation requirement | \(H_{\rm exch}\) preserves ordinary-sector zero-net exchange and zero-creation branches unless source theorem derives otherwise | REQUIRED | preserves Group 18 safest branches |
| HE18: dark-sector no-patch guard | \(H_{\rm exch}\) does not use dark-sector coupling as ordinary-sector patch | REQUIRED | preserves no-dark-patch result |
| HE19: diagnostic-only \(H_{\rm exch}\) branch | \(H_{\rm exch}\)-like object used only as diagnostic audit and never inserted into field equation | SAFE_IF | allows exchange correction audits without parent insertion |
| HE20: identically divergence-free \(H_{\rm exch}\) candidate | \(H_{\rm exch}\) divergence vanishes by constructed identity | CANDIDATE | possible future divergence-safe route if constructed |
| HE21: source-balanced \(H_{\rm exch}\) candidate | divergence of \(H_{\rm exch}\) balances independently defined exchange source/relaxation side | CANDIDATE | possible future route if source partner is real |
| HE22: projected \(H_{\rm exch}\) candidate | \(H_{\rm exch}\) lives in defined exchange/current projector subspace | CANDIDATE | possible route to no-overlap if projector is real |
| HE23: exchange-continuity paint rejection | \(H_{\rm exch}\) is whatever makes \(\nabla_\mu J_{\rm exch}^\mu=\Sigma_{\rm exch}-R_{\rm exch}\) work | REJECTED | prevents decorative exchange closure |
| HE24: \(\Sigma/R\) tuning tensor rejection | \(H_{\rm exch}\) uses \(\Sigma/R\) as coefficient knobs or cancellation terms | REJECTED | prevents hidden tuning mechanism |
| HE25: boundary repair tensor rejection | \(H_{\rm exch}\) cancels boundary leakage, shell source, scalar tail, or \(M_{\rm ext}\) shift | REJECTED | prevents boundary repair tensor |
| HE26: ordinary matter rerouting rejection | \(H_{\rm exch}\) reroutes ordinary matter to fix exchange, curvature, or boundary behavior | REJECTED | preserves ordinary matter decoupling |
| HE27: dark-sector patch rejection | \(H_{\rm exch}\) invokes dark sector to patch ordinary exchange-source failure | REJECTED | preserves optional/deferred dark-sector status |
| HE28: recovery-fit correction rejection | \(H_{\rm exch}\) chosen to recover \(\gamma_{\rm like}\), \(AB\), exterior matching, or PPN behavior | REJECTED | keeps recovery downstream |
| HE29: \(H_{\rm exch}\) failure | \(H_{\rm exch}\) cannot meet current, source, divergence, boundary, matter, mass, scalar, and zero-net requirements | BRANCH_KILLED | \(H_{\rm exch}\) cannot be inserted into parent equation |
| HE30: recommended next move | after \(H_{\rm curv}\) and \(H_{\rm exch}\) burdens are stated, audit correction tensor divergence safety | RECOMMENDED | next script should be `candidate_correction_tensor_divergence_safety.py` |

## Status Counts

```text
BRANCH_KILLED: 1
CANDIDATE:     3
RECOMMENDED:   1
REJECTED:      6
REQUIRED:      17
SAFE_IF:       1
THEOREM_TARGET:1
```

Interpretation:

```text
H_exch is not defined yet.

A real H_exch requires real current/source structure:
J_V or J_exch,
Sigma/R operators,
source/relaxation distinction,
domain,
orientation,
projection class,
tensor symmetry,
divergence behavior,
boundary behavior,
ordinary matter decoupling,
M_ext neutrality,
scalar trace neutrality,
and coefficient origin.

J_V remains unresolved.

J_exch remains theorem target only.

Sigma/R remain role-level only.

No active ordinary-sector source side for J_exch is derived.

Diagnostic-only H_exch is the safest fallback.

Exchange-continuity paint,
Sigma/R tuning,
boundary repair,
matter rerouting,
dark patch,
and recovery-fit correction are rejected.

Next gate is correction tensor divergence safety.
```

## Required H_exch Fields

```text
1. J_V or J_exch definition
2. Sigma/R operators
3. source/relaxation distinction
4. ordinary-sector source-side status
5. domain
6. orientation / flux behavior
7. projection class
8. tensor symmetry / trace behavior
9. divergence behavior
10. boundary behavior
11. ordinary matter decoupling
12. M_ext neutrality
13. scalar trace neutrality
14. coefficient origin
15. zero-net / zero-creation preservation
16. dark-sector no-patch guard
```

## H_exch Definition Decision Tree

```text
1. H_exch has J/source/relaxation, divergence behavior, and neutrality:
   exchange correction theorem target survives.

2. J_V remains unresolved:
   H_exch cannot use J_V.

3. J_exch remains theorem target only:
   H_exch cannot use J_exch as operator.

4. Sigma/R remain role-level:
   H_exch remains diagnostic-only or deferred.

5. H_exch makes exchange continuity work:
   rejected as paint.

6. H_exch reroutes matter, shifts mass, leaks scalar, or patches dark:
   rejected.

7. H_exch cannot meet requirements:
   keep deferred or diagnostic-only.
```

## Good Failure / Branch Decision

Good failure:

```text
H_exch cannot be defined without current/source origin,
divergence behavior,
boundary neutrality,
matter decoupling,
and zero-net ordinary-sector control.
```

Consequence:

```text
keep H_exch deferred or diagnostic-only.
do not insert it into a parent equation.
```

Bad failure:

```text
call H_exch an exchange correction because exchange continuity needs a tensor.
```

## Failure Controls

\(H_{\rm exch}\) definition fails if:

1. \(J_V\) is used before definition.
2. \(J_{\rm exch}\) is promoted from theorem target to operator.
3. \(\Sigma/R\) are undefined.
4. \(\Sigma/R\) become tuning knobs.
5. ordinary-sector source side is invented.
6. domain/orientation hide leakage.
7. projection hides overlap.
8. tensor symmetry is unspecified.
9. divergence safety is exchange-continuity paint.
10. boundary behavior repairs failure.
11. ordinary matter is rerouted.
12. \(M_{\rm ext}\) shifts.
13. scalar trace leaks.
14. dark sector patches ordinary failure.
15. coefficients tune recovery or exchange closure.

## What This Study Established

This study established that \(H_{\rm exch}\) is not defined yet.

It also established that \(H_{\rm exch}\) cannot be used as exchange-continuity paint, \(\Sigma/R\) tuning tensor, boundary repair tensor, ordinary-matter rerouting tensor, dark-sector patch, or recovery-fit correction.

## What This Study Did Not Establish

This study did not define \(H_{\rm exch}\).

It did not define \(J_V\).

It did not define \(J_{\rm exch}\).

It did not define \(\Sigma_{\rm exch}\).

It did not define \(R_{\rm exch}\).

It did not prove divergence safety.

It did not define a projection class.

It did not prove boundary neutrality.

It did not prove ordinary matter decoupling.

It did not prove \(M_{\rm ext}\) neutrality.

It did not prove scalar-trace neutrality.

It did not justify insertion into a parent field equation.

## Current Best Interpretation

```text
H_exch remains a theorem target or diagnostic-only fallback.

It may not enter the parent equation until it has:
  current/source origin,
  source/relaxation distinction,
  tensor identity,
  divergence behavior,
  boundary neutrality,
  matter decoupling,
  mass neutrality,
  scalar-trace neutrality,
  zero-net / zero-creation protection,
  and no dark-sector patching.
```

## Next Development Target

The next script should be:

```text
candidate_correction_tensor_divergence_safety.py
```

Purpose:

```text
Audit what divergence-safe means without being decorative.
```

Reason:

```text
H_curv and H_exch have now both been burdened.

The next shared bottleneck is what divergence-safe actually means
without decoration.
```

Expected result:

```text
A correction tensor divergence-safety ledger:
  identically divergence-free tensor,
  constraint-compatible tensor,
  source-balanced tensor,
  projected tensor,
  diagnostic tensor,
  boundary-supported tensor,
  decorative tensor rejection,
  Bianchi-like language rejection,
  recovery-chosen divergence rejection,
  leakage-canceling divergence rejection.
```

## Summary

The \(H_{\rm exch}\) requirements result is:

```text
Exchange correction cannot be continuity paint.
It needs real current/source structure first.
```

Tiny goblin plaque:

```text
No exchange paint.
No Sigma/R knobs.
No dark patch over an ordinary leak.
