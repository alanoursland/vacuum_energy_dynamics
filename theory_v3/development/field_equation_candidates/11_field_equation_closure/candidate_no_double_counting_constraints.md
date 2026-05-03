# Candidate No-Double-Counting Constraints

## What This Document Is

This document is a development note for the `11_field_equation_closure/` group.

It is not a final parent identity, not a proof of conservation closure, and not a covariant source-decomposition theorem. It does not add a formal commitment to the theory.

Its purpose is to summarize the result of:

```text
candidate_no_double_counting_constraints.py
```

The guiding question was:

```text
Which overlaps between sources and sectors are forbidden or constrained?
```

The answer is:

```text
The current no-double-counting rule is:

  rho -> A, not long-range kappa
  trace -> kappa_min, not scalar wave
  j_T -> W_i, not scalar continuity
  TT stress -> h_ij^TT, not scalar trace
  relaxation -> vacuum restoration, not A damping
```

These are currently constraints, not full derivations.

---

## Why This Study Matters

The source-decomposition ledger separated source roles.

This study turns those roles into explicit constraints.

The central rule is:

```text
one source may contribute to total stress-energy,
but it must not become multiple independent gravity sources unless a parent
identity forces the split.
```

Without this rule, the theory can accidentally double-count gravity while appearing to have a richer ontology.

---

## Constraint Ledger

| Constraint | Expression | Status | Risk If Violated |
|---|---|---|---|
| C1: \(\rho\) not double-sourced into \(\kappa\) | \(S_\kappa[\rho]=0\) as independent long-range scalar source | CONSTRAINED | Double-counted scalar gravity and exterior \(\kappa\) tail |
| C2: exterior \(\kappa\) charge vanishes | \(Q_\kappa=\int S_\kappa d^3x=0\) | CONSTRAINED | \(\kappa_{\rm ext}\sim1/r\) scalar gravity |
| C3: pressure / trace shifts minimum, not wave source | trace, \(p\to\kappa_{\min}\); not \(\Box\kappa=\alpha\,{\rm trace}\) | CONSTRAINED | Breathing radiation or massless scalar tail |
| C4: transverse current only sources \(W_i\) | \({\rm source}(W_i)=P_Tj\), \(P_Lj\) excluded | STRUCTURAL | Longitudinal / gauge current contaminates vector sector |
| C5: longitudinal current belongs to scalar continuity | \(P_Lj\to\) continuity / \(\dot\rho\), not \(\nabla\times W\) | DERIVED_REDUCED | Scalar / vector source mixing |
| C6: TT stress remains trace-free tensor source | \({\rm source}(h_{TT})=P_{TT}S_{ij}\), trace excluded | STRUCTURAL | Trace stress double-counted as tensor radiation |
| C7: scalar radiation source rejected | \({\rm source}(A_{\rm rad}\,{\rm ordinary\ massless})=0\) | REJECTED | Observable breathing mode / scalar radiation |
| C8: \(\kappa\) relaxation cannot erase \(A\) | \(\Gamma_{\rm relax}[A_{\rm mass\ flux}]=0\) | CONSTRAINED | Gravity mass flux disappears or is tuned by relaxation |
| C9: boundary smoothing preserves exterior mass | \(\delta M_{\rm ext}\) from \(\kappa\) boundary smoothing \(=0\) | CONSTRAINED | Surface smoothing changes measured mass |
| C10: creation term excluded from ordinary closure | \(\Sigma_{\rm creation}=0\) in ordinary closed gravity regime | CONSTRAINED | Nonconservative source breaks closure |

---

## Status Counts

The run counted:

```text
CONSTRAINED:      6
DERIVED_REDUCED:  1
REJECTED:         1
STRUCTURAL:       2
```

Interpretation:

```text
Most no-double-counting rules are constraints, not derivations.
```

That matters.

The rules are necessary for safety, but the parent identity still has to explain them.

---

## Most Dangerous Violations

The most dangerous violations are:

1. \(\rho\) also sources long-range \(\kappa\).
2. Pressure trace creates \(\Box\kappa\) scalar waves.
3. \(\kappa\) smoothing changes exterior mass flux.
4. TT coupling is matched but claimed derived.
5. \(\Sigma_{\rm creation}\) enters ordinary closure.
6. Recombination duplicates scalar spatial response.

These are the current goblin traps.

---

## Parent Identity Requirements

The constraints require a parent identity that explains:

```text
why rho sources A and not long-range kappa,
why trace shifts kappa_min but does not radiate,
why TT stress sources only TT radiation,
why transverse and longitudinal currents split cleanly,
why boundary smoothing preserves exterior mass,
why ordinary closed gravity has Sigma_creation = 0.
```

Without that parent identity, these are safety constraints, not derivations.

Status:

```text
UNFINISHED
```

This is the key weakness exposed by the run.

---

## What This Study Established

This study established:

1. \(\rho\) must not source an independent long-range \(\kappa\) field.
2. Exterior \(\kappa\) charge must vanish.
3. Trace / pressure may shift \(\kappa_{\min}\), but must not create \(\Box\kappa\) waves.
4. \(W_i\) must be sourced only by transverse current.
5. Longitudinal current belongs to scalar continuity.
6. TT stress must remain trace-free tensor source.
7. Ordinary long-range scalar radiation remains rejected.
8. \(\kappa\) relaxation must not erase the \(A\)-sector mass field.
9. Boundary smoothing must preserve exterior mass.
10. \(\Sigma_{\rm creation}\) is excluded from ordinary closed gravity.

---

## What This Study Did Not Establish

This study did not derive the parent identity.

It did not derive covariant source decomposition.

It did not derive the trace source law.

It did not derive current splitting covariantly.

It did not derive the TT source identity.

It did not prove boundary smoothing preserves mass.

It only formalized the constraints required for closure.

---

## Current Best Interpretation

The current no-double-counting rule is:

```text
rho -> A, not long-range kappa
trace -> kappa_min, not scalar wave
j_T -> W_i, not scalar continuity
TT stress -> h_ij^TT, not scalar trace
relaxation -> vacuum restoration, not A damping
```

These are currently constraints.

They must eventually become consequences of the parent identity.

---

## Next Development Target

The next script should be:

```text
candidate_constraint_vs_evolution_split.py
```

Purpose:

```text
Separate constraint fields from propagating / evolving fields.
```

Reason:

```text
Source double-counting is controlled; next we must separate constraints from
evolution.
```

Expected result:

```text
A sector ledger classifying:
  A as scalar constraint,
  W_i as transverse vector constraint / stationary response,
  h_ij^TT as true propagating radiation,
  kappa as non-inertial relaxation / constrained trace response,
  A_rad as rejected.
```

---

## Summary

The no-double-counting constraints are now clear.

But they are mostly constraints, not derivations.

The next closure question is:

```text
Which fields are constraints, and which fields really propagate?
```
