# VacuumForge Candidate Branch Charters

## Purpose

This ledger opens the first vacuum-sector candidate branch charters after the
residual gate ledger. It does not select a strain branch, compute `epsilon`, or
license new physics. It only records branch contracts, gate plans, kill
conditions, and first tests.

This ledger depends on:

```text
residual_gate_ledger_004
```

because branch charters are not meaningful until the residual gates exist.

## SymPy Coverage Check

The script constructs a branch-by-gate coverage matrix with shape:

```text
8 x 9
```

Row sums:

```text
9, 9, 9, 9, 9, 9, 9, 9
```

Each row covers all `9` residual gates. This is a governance
coverage check, not a proof that any candidate branch passes the gates.

## Charter Summary

| branch | X variable | neighboring mismatch rule | candidate invariant/scalar | expected epsilon status | status | kill condition | first concrete test |
| --- | --- | --- | --- | --- | --- | --- | --- |
| eh_ghy_baseline | metric data g_ab | Levi-Civita metric transport | R with GHY boundary completion | epsilon = 0 | admissible at epsilon = 0 | fails if used as an ontology selector without a strain-branch selector | record baseline boundary and TT-mode references in the gate ledger |
| inert_boundary_topological | metric data g_ab unless routed otherwise | Levi-Civita transport unless boundary/topology route differs | total derivatives, Euler/Gauss-Bonnet-like, or boundary-local terms | epsilon = 0 equivalent or boundary-quarantined | not yet evaluated | fails as a residual if it is only a field redefinition or inert boundary term | vary a representative total derivative and classify boundary data |
| higher_curvature_local | metric data g_ab | Levi-Civita transport | R^2, R_ab R^ab, R_abcd R^abcd, or controlled combinations | controlled epsilon != 0 only if all gates pass | fails as controlled local higher-curvature residual under current postulate set | fails if extra modes or weak-field residuals are not explicitly routed | completed by 006 scalar prototype and 007 tensor-route audit |
| metric_affine_extra_connection | metric data plus independent connection or transport variable | independent affine comparison rule | curvature, torsion, nonmetricity, or compatibility-enforcing invariant | underdetermined without new axiom | underdetermined without new axiom | fails if independent connection has no physical route or no reduction proof | Palatini-style compatibility check under the vacuum assumptions |
| holonomy_loop_mismatch | transport or frame data with metric reduction | closed-loop holonomy mismatch | leading scalar built from loop curvature or holonomy norm | not yet evaluated | not yet evaluated | fails if the leading scalar is chosen by taste rather than a mismatch rule | small-loop expansion ledger comparing candidate scalars |
| finsler_nonquadratic_directional | direction-dependent interval response | direction-dependent comparison or calibration rule | Finsler curvature or nonquadratic strain scalar | underdetermined without new axiom | underdetermined without new axiom | fails if nonquadratic response is used while citing metric-branch closure | directional perturbation prototype with explicit metric Hessian limit |
| medium_configuration_elastic | internal medium/configuration field plus metric response map | medium strain tensor or configuration-gradient mismatch | elastic energy, defect strain, or compatibility violation | underdetermined without new axiom | underdetermined without new axiom | fails if constitutive law or matter route is not specified | minimal constitutive-map contract before any dynamics |
| nonlocal_relaxation | metric data plus nonlocal kernel or relaxation state | kernel-weighted or history-dependent comparison | nonlocal action kernel, relaxation functional, or baseline selector | not yet evaluated | not yet evaluated | fails if it changes closed local equations while being used as a background channel | local-limit quarantine test for a toy relaxation kernel |

## Branch Charters

### EH/GHY baseline

```text
branch id: eh_ghy_baseline
purpose: baseline closed metric branch; defines epsilon = 0
X variable: metric data g_ab
metric reduction map: identity map to the pseudo-Riemannian metric
neighboring mismatch rule: Levi-Civita metric transport
candidate invariant/scalar: R with GHY boundary completion
boundary term or boundary data: fixed induced boundary metric plus GHY term
matter coupling route: standard metric stress tensor
expected epsilon status: epsilon = 0
known risks: treating the baseline as selected by local response alone
kill condition: fails if used as an ontology selector without a strain-branch selector
first concrete test: record baseline boundary and TT-mode references in the gate ledger
status: admissible at epsilon = 0
```

Gate plan:

- `metric_limit_test`: verify local interval response is the metric branch
- `nonquadratic_routing_test`: not applicable inside pseudo-Riemannian branch
- `diffeomorphism_identity_test`: use contracted Bianchi identity
- `boundary_variation_test`: use GHY differentiability ledger
- `mode_count_test`: verify two TT modes in the linearized limit
- `hyperbolicity_test`: verify Lorentzian principal symbol
- `source_ledger_test`: use metric stress-tensor source route
- `weak_field_residual_test`: recover Newtonian/PPN baseline
- `epsilon_classification_test`: classify as epsilon = 0 equivalent

### inert boundary or topological residual

```text
branch id: inert_boundary_topological
purpose: separate bulk-inert terms from genuine residual dynamics
X variable: metric data g_ab unless routed otherwise
metric reduction map: same pointwise metric branch as EH/GHY
neighboring mismatch rule: Levi-Civita transport unless boundary/topology route differs
candidate invariant/scalar: total derivatives, Euler/Gauss-Bonnet-like, or boundary-local terms
boundary term or boundary data: must state whether term changes admissible boundary data
matter coupling route: no new matter source unless boundary channel is explicit
expected epsilon status: epsilon = 0 equivalent or boundary-quarantined
known risks: mistaking a boundary accounting term for new bulk physics
kill condition: fails as a residual if it is only a field redefinition or inert boundary term
first concrete test: vary a representative total derivative and classify boundary data
status: not yet evaluated
```

Gate plan:

- `metric_limit_test`: show no change to local metric response
- `nonquadratic_routing_test`: show no hidden nonquadratic response
- `diffeomorphism_identity_test`: show invariant total derivative or routed boundary symmetry
- `boundary_variation_test`: compute boundary variation explicitly
- `mode_count_test`: show no new bulk modes
- `hyperbolicity_test`: show no change to bulk principal symbol
- `source_ledger_test`: show no hidden boundary source double-counting
- `weak_field_residual_test`: show no bulk Yukawa/PPN residual
- `epsilon_classification_test`: classify as inert, boundary-quarantined, or failed

### higher-curvature local residual

```text
branch id: higher_curvature_local
purpose: test local curvature corrections without hiding extra modes
X variable: metric data g_ab
metric reduction map: same pointwise metric branch as EH/GHY
neighboring mismatch rule: Levi-Civita transport
candidate invariant/scalar: R^2, R_ab R^ab, R_abcd R^abcd, or controlled combinations
boundary term or boundary data: higher-derivative boundary completion required
matter coupling route: metric stress tensor plus explicit higher-derivative residual route
expected epsilon status: controlled epsilon != 0 only if all gates pass
known risks: scalaron, spin-2 ghost, hidden Yukawa term, fourth-order boundary problem
kill condition: fails if extra modes or weak-field residuals are not explicitly routed
first concrete test: completed by 006 scalar prototype and 007 tensor-route audit
status: fails as controlled local higher-curvature residual under current postulate set
```

Gate plan:

- `metric_limit_test`: verify same pointwise metric response
- `nonquadratic_routing_test`: not applicable unless response variable changes
- `diffeomorphism_identity_test`: derive Noether identity for higher-curvature action
- `boundary_variation_test`: supply higher-derivative boundary terms
- `mode_count_test`: linearize and count scalar/tensor ghost content
- `hyperbolicity_test`: check principal symbol and derivative order
- `source_ledger_test`: separate curvature residual from matter source
- `weak_field_residual_test`: compute Yukawa/PPN residual map
- `epsilon_classification_test`: classify as controlled, failed, or routed extra-mode branch

### metric-affine connection residual

```text
branch id: metric_affine_extra_connection
purpose: test independent transport as more than metric Levi-Civita bookkeeping
X variable: metric data plus independent connection or transport variable
metric reduction map: must reduce to g_ab with compatible Levi-Civita transport in GR limit
neighboring mismatch rule: independent affine comparison rule
candidate invariant/scalar: curvature, torsion, nonmetricity, or compatibility-enforcing invariant
boundary term or boundary data: connection boundary data and compatibility constraints required
matter coupling route: spin/torsion/nonmetric matter route must be explicit
expected epsilon status: underdetermined without new axiom
known risks: untracked torsion, nonmetricity, preferred-frame effects, source duplication
kill condition: fails if independent connection has no physical route or no reduction proof
first concrete test: Palatini-style compatibility check under the vacuum assumptions
status: underdetermined without new axiom
```

Gate plan:

- `metric_limit_test`: derive metric compatibility or route deviations
- `nonquadratic_routing_test`: show connection does not hide nonmetric response
- `diffeomorphism_identity_test`: derive metric-affine Noether identity
- `boundary_variation_test`: state connection boundary data
- `mode_count_test`: count torsion/nonmetric modes
- `hyperbolicity_test`: check connection-sector principal symbol
- `source_ledger_test`: separate spin, torsion, and metric stress sources
- `weak_field_residual_test`: bound preferred-frame or torsion residuals
- `epsilon_classification_test`: classify as reduced baseline, routed extra field, or failed

### holonomy or loop-mismatch strain

```text
branch id: holonomy_loop_mismatch
purpose: test whether between-point mismatch is naturally loop/transport based
X variable: transport or frame data with metric reduction
metric reduction map: small-loop limit must recover metric curvature branch or route residuals
neighboring mismatch rule: closed-loop holonomy mismatch
candidate invariant/scalar: leading scalar built from loop curvature or holonomy norm
boundary term or boundary data: loop anchoring and boundary transport data required
matter coupling route: must state whether matter sees metric, frame, or holonomy data
expected epsilon status: not yet evaluated
known risks: assuming curvature-as-loop automatically selects EH
kill condition: fails if the leading scalar is chosen by taste rather than a mismatch rule
first concrete test: small-loop expansion ledger comparing candidate scalars
status: not yet evaluated
```

Gate plan:

- `metric_limit_test`: expand small loops and compare with metric curvature
- `nonquadratic_routing_test`: route any nonquadratic holonomy norm
- `diffeomorphism_identity_test`: prove relabeling-invariant loop construction
- `boundary_variation_test`: state boundary loop/transport data
- `mode_count_test`: linearize and identify extra transport modes
- `hyperbolicity_test`: check local limit principal symbol
- `source_ledger_test`: avoid adding holonomy as a second matter source
- `weak_field_residual_test`: compute leading weak-field holonomy residual
- `epsilon_classification_test`: classify as EH-like, controlled residual, or underdetermined

### Finsler or nonquadratic directional response

```text
branch id: finsler_nonquadratic_directional
purpose: test nonquadratic interval response without hiding it inside metric proofs
X variable: direction-dependent interval response
metric reduction map: quadratic Hessian limit plus explicit nonquadratic remainder
neighboring mismatch rule: direction-dependent comparison or calibration rule
candidate invariant/scalar: Finsler curvature or nonquadratic strain scalar
boundary term or boundary data: direction-bundle boundary data required
matter coupling route: matter calibration and null-cone route must be explicit
expected epsilon status: underdetermined without new axiom
known risks: untracked null-cone drift, preferred direction, matter calibration conflict
kill condition: fails if nonquadratic response is used while citing metric-branch closure
first concrete test: directional perturbation prototype with explicit metric Hessian limit
status: underdetermined without new axiom
```

Gate plan:

- `metric_limit_test`: show the quadratic limit and residual size
- `nonquadratic_routing_test`: route null-cone and calibration consequences
- `diffeomorphism_identity_test`: derive bundle/relabeling identity
- `boundary_variation_test`: state direction-bundle boundary variation
- `mode_count_test`: count direction-sector modes or constraints
- `hyperbolicity_test`: check causal cone and well-posedness
- `source_ledger_test`: separate calibration drift from stress tensor
- `weak_field_residual_test`: compute PPN/preferred-direction residuals
- `epsilon_classification_test`: classify as routed nonmetric branch or failed

### medium or configuration-elastic strain

```text
branch id: medium_configuration_elastic
purpose: test a deeper material/configuration variable beneath metric data
X variable: internal medium/configuration field plus metric response map
metric reduction map: constitutive map from medium state to g_ab required
neighboring mismatch rule: medium strain tensor or configuration-gradient mismatch
candidate invariant/scalar: elastic energy, defect strain, or compatibility violation
boundary term or boundary data: medium boundary data and defect admissibility required
matter coupling route: must state whether matter couples to metric only or medium channel
expected epsilon status: underdetermined without new axiom
known risks: preferred structure, extra modes, anisotropy, source double-counting
kill condition: fails if constitutive law or matter route is not specified
first concrete test: minimal constitutive-map contract before any dynamics
status: underdetermined without new axiom
```

Gate plan:

- `metric_limit_test`: derive metric response from the constitutive map
- `nonquadratic_routing_test`: route anisotropic or nonlinear response
- `diffeomorphism_identity_test`: separate gauge labels from physical medium labels
- `boundary_variation_test`: state medium and defect boundary data
- `mode_count_test`: count medium modes and freeze/routing conditions
- `hyperbolicity_test`: check medium propagation or relaxation law
- `source_ledger_test`: avoid double-counting medium stress as matter stress
- `weak_field_residual_test`: bound anisotropy and preferred-frame residuals
- `epsilon_classification_test`: classify as new axiom branch, controlled residual, or failed

### nonlocal or relaxation strain

```text
branch id: nonlocal_relaxation
purpose: test large-scale/baseline relaxation without changing closed local GR equations
X variable: metric data plus nonlocal kernel or relaxation state
metric reduction map: local limit must reduce to the closed metric branch
neighboring mismatch rule: kernel-weighted or history-dependent comparison
candidate invariant/scalar: nonlocal action kernel, relaxation functional, or baseline selector
boundary term or boundary data: history, domain, and boundary kernel data required
matter coupling route: must quarantine Lambda/dark-sector channel from ordinary stress tensor
expected epsilon status: not yet evaluated
known risks: acausal kernel, hidden local-field modification, dark-sector source insertion
kill condition: fails if it changes closed local equations while being used as a background channel
first concrete test: local-limit quarantine test for a toy relaxation kernel
status: not yet evaluated
```

Gate plan:

- `metric_limit_test`: show local metric equations remain closed or route deviation
- `nonquadratic_routing_test`: route nonlocal response outside local metric proof
- `diffeomorphism_identity_test`: derive covariant kernel identity or route breaking
- `boundary_variation_test`: state domain/history boundary data
- `mode_count_test`: identify memory/relaxation modes
- `hyperbolicity_test`: check causality and well-posed history dependence
- `source_ledger_test`: quarantine Lambda/dark excess from matter T_ab
- `weak_field_residual_test`: bound local and solar-system leakage
- `epsilon_classification_test`: classify as quarantined sector, controlled residual, or failed


## Current Conclusion

The candidate space is now chartered but not live as physics. Only the EH/GHY
baseline is currently admissible at `epsilon = 0`. The higher-curvature local
residual has now been stress-tested by 006 and 007 and fails as a controlled
local higher-curvature residual under the current postulate set. Other residual
branches remain not-yet-evaluated or underdetermined until their first concrete
tests supply gate evidence.

## Classification

```text
result type: candidate branch charter ledger
scope: starting vacuum-sector strain branches after residual gates
conclusion: candidate work may proceed branch-by-branch under explicit gates
non-conclusion: no residual branch has passed; no non-GR epsilon has been computed
```

The next technical target is the first concrete branch test:

```text
open the Lambda baseline folder after the higher-curvature local residual route
audit.
```
