# Candidate Spatial-Response Equation Family Sieve

## Result

The script classifies scalar spatial-response and `B_s/F_zeta` equation families.

It eliminates or demotes response families that violate recovery-selector, neutrality, source, scalar-tail, or well-posedness guardrails, while keeping `B_s/F_zeta` insertion not ready.

## Main Findings

- `B_s/F_zeta` chosen from `AB=1` or `B=1/A` is eliminated.
- Response chosen from Schwarzschild recovery, weak-field success, or PPN gamma is eliminated.
- Neutral `F_zeta` carrying a concrete response expression is eliminated.
- Branch-indexed non-active response candidate forms may be inventoried without insertion.
- A real scalar spatial-response insertion law likely requires a later explicit axiom or derivation.
- Response equations that duplicate the protected A-sector mass coin are eliminated.
- Ordinary long-range scalar-tail response is eliminated or demoted.
- Response equations with undefined object, sector, domain, codomain, or branch status are not well-posed.

## Boundary

Recovery is audit only. Neutral means expression-free. Candidate forms are not insertable. Future response laws need source no-double-counting support, typed objects, explicit branch status, and prior gates closed.

## Safe Handoff

Run `candidate_residual_source_equation_elimination_audit.py` next.
