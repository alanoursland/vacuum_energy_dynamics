# VacuumForge Residual Gate Ledger

## Purpose

This ledger makes the residual gate manifest operational. It does not test a
candidate residual. It records the gates that every candidate must pass or
explicitly route before it can be classified as:

```text
controlled epsilon != 0
```

This ledger depends on:

```text
neighboring_mismatch_inventory_003
```

because mismatch rules do not become candidate branches until residual tests
are defined.

## Gate Ledger

| gate | purpose | required evidence | fail route | blocks |
| --- | --- | --- | --- | --- |
| metric_limit_test | preserve Q_p(v) = g_ab v^a v^b at lowest order or explicitly leave the metric branch | local-response expansion and metric-reduction map | route as nonmetric/nonquadratic branch or reject | hidden change to closed metric response |
| nonquadratic_routing_test | prevent Finsler or nonquadratic response from being hidden inside pseudo-Riemannian proofs | explicit nonquadratic variable, coupling route, and observable suppression or channel | route outside metric branch or reject | untracked null-cone or calibration drift |
| diffeomorphism_identity_test | ensure variational equations imply the correct Noether/conservation identity | Noether/Bianchi-style identity or explicit symmetry-breaking route | route as extra-field/nonconserved sector or reject | unconserved source or coordinate-label dependence |
| boundary_variation_test | make the variational problem well posed | total derivative accounting and boundary data/counterterm | supply boundary completion or reject | uncontrolled boundary equations or hidden boundary source |
| mode_count_test | preserve two TT modes in the GR branch unless extra modes are explicitly routed | linearized mode count around Minkowski or GR background | route extra scalar/vector/tensor modes or reject | hidden scalaron, vector, ghost, or medium mode |
| hyperbolicity_test | preserve Lorentzian causal propagation in the GR limit | principal-symbol or propagation-speed check | route dissipative/nonlocal/elliptic behavior or reject | wrong causal cone or ill-posed evolution |
| source_ledger_test | avoid double-counting matter, scalar flux, Lambda baseline, torsion, nonmetric drift, or dark excess | source-role purity ledger | move to the appropriate source/baseline/extra-field ledger or reject | source duplication and hidden dark-sector insertion |
| weak_field_residual_test | detect hidden Yukawa, PPN, preferred-frame, scalaron, or propagation deviations | weak-field expansion or observational residual map | route as testable residual with bound/kill condition or reject | unnoticed conflict with closed weak-field sector |
| epsilon_classification_test | classify candidate as epsilon = 0 equivalent, controlled epsilon != 0, failed, or underdetermined | results from all earlier gates plus kill condition | retain as not yet evaluated or underdetermined | free-knob epsilon language |

## Current Conclusion

No candidate residual is currently licensed as controlled `epsilon != 0`.
Candidate branches may be chartered only as not-yet-evaluated or
underdetermined until they provide gate evidence.

This is a gate-ledger result, not a no-go theorem against residuals.

## Classification

```text
result type: residual gate ledger / governance classification
scope: required tests for K_residual candidates
conclusion: controlled epsilon != 0 is unavailable until gates pass or route
non-conclusion: no residual tested; no residual killed; no epsilon computed
```

The next technical target is candidate branch chartering:

```text
open candidate branches only with explicit kill conditions and gate plan.
```
