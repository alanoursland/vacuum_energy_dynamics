# Candidate Residual Source Equation Elimination Audit

## Result

The script eliminates or demotes equation families that mishandle residuals or hide source load.

It does not prove residual nonentry or source no-double-counting.

## Main Findings

- Equations that ignore residual `zeta/kappa` metric re-entry are eliminated.
- Equations that kill residuals by declaration are eliminated.
- Equations using safe membership as residual nonentry are eliminated.
- Equations using undefined active `O` as a residual eraser are rejected.
- Equations that make `B_s`, `zeta`, or `kappa` independent ordinary mass channels are eliminated.
- Equations that hide source load in `H_curv`, `H_exch`, `J` labels, `Sigma/R`, curvature accounting, or dark labels are eliminated.
- Strict non-metric / inert residual status may survive only as a later theorem route.
- A source-routing axiom may be required if derivation cannot close the source theorem.

## Boundary

Ignoring residuals is not residual control. Declaration is not residual proof. Membership cannot imply residual nonentry. Undefined or diagnostic objects cannot serve as source reservoirs or repair tools. The protected A-sector mass response must not be duplicated.

## Safe Handoff

Run `candidate_boundary_divergence_equation_elimination_audit.py` next.
