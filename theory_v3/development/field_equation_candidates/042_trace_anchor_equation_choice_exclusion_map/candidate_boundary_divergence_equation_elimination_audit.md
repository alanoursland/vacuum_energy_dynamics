# Candidate Boundary Divergence Equation Elimination Audit

## Result

The script eliminates or demotes boundary, support, scalar-tail, divergence, and parent-identity repair equations.

It does not prove boundary neutrality, exterior scalar silence, or parent identity.

## Main Findings

- Equations that introduce shell sources to hide matching failure are eliminated.
- Equations that add boundary counterterms after leakage appears are eliminated.
- Equations that suppress scalar tails by filter are eliminated.
- Equations that use `H_curv` or `H_exch` as divergence repair are rejected.
- Equations that use active `O` to repair divergence are rejected.
- Parent-form equations written before recombination and identity are licensed remain not ready.
- Compact-support or boundary-neutral scalar response may survive only if support follows from the equation and source law.
- A real divergence or Bianchi-like parent identity remains a later theorem target.

## Boundary

No shell source may be added as repair. Boundary behavior must be derived before recovery. Scalar silence must not be filtered after the fact. Correction tensors and active `O` are not repair tools. Reduced recovery is not parent readiness.

## Safe Handoff

Run `candidate_equation_choice_exclusion_batch_reconciliation.py` next.
