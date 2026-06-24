# Residual Gate Manifest

Every candidate residual must be tested against this manifest before it is
treated as physically live.

Current managed ledger:

```text
residual_gate_ledger_vacuumforge.md
```

That ledger records the required evidence, fail route, and blocked failure mode
for each gate. Its current conclusion is that no candidate residual is
currently licensed as controlled `epsilon != 0`. This is a gate-ledger result,
not a no-go theorem against residuals.

## Tests

```text
metric_limit_test:
  Does the branch reduce to Q_p(v) = g_ab v^a v^b at lowest order?
```

```text
nonquadratic_routing_test:
  If response is Finsler/nonquadratic, is it explicitly routed outside the
  metric branch?
```

```text
diffeomorphism_identity_test:
  Does the variational equation imply the correct Noether/conservation identity?
```

```text
boundary_variation_test:
  Are all total derivative terms canceled or assigned boundary data?
```

```text
mode_count_test:
  Around a Minkowski or GR background, are there only two TT modes unless extra
  modes are explicitly routed?
```

```text
hyperbolicity_test:
  Does the principal symbol preserve Lorentzian causal propagation in the GR
  limit?
```

```text
source_ledger_test:
  Does the residual avoid double-counting matter, scalar flux, Lambda baseline,
  torsion, nonmetric drift, or dark-sector excess?
```

```text
weak_field_residual_test:
  Does the residual produce hidden Yukawa, PPN, preferred-frame, scalaron, or
  propagation effects?
```

```text
epsilon_classification_test:
  Is the candidate physically equivalent to epsilon = 0, controlled
  epsilon != 0, failed, or underdetermined?
```

## Result Labels

Use these labels for each test:

```text
passed
failed
requires explicit route
boundary-equivalent
topological/inert
observationally constrained
underdetermined
not yet evaluated
```

## Gate Rule

A residual that fails a gate is not dead if it has an explicit route. But an
unrouted failure cannot be treated as a valid vacuum-sector residual.

## Current Gate-Ledger Summary

```text
metric_limit_test:
  evidence: local-response expansion and metric-reduction map
  blocks: hidden change to closed metric response

nonquadratic_routing_test:
  evidence: explicit nonquadratic variable, coupling route, and observable suppression or channel
  blocks: untracked null-cone or calibration drift

diffeomorphism_identity_test:
  evidence: Noether/Bianchi-style identity or explicit symmetry-breaking route
  blocks: unconserved source or coordinate-label dependence

boundary_variation_test:
  evidence: total derivative accounting and boundary data/counterterm
  blocks: uncontrolled boundary equations or hidden boundary source

mode_count_test:
  evidence: linearized mode count around Minkowski or GR background
  blocks: hidden scalaron, vector, ghost, or medium mode

hyperbolicity_test:
  evidence: principal-symbol or propagation-speed check
  blocks: wrong causal cone or ill-posed evolution

source_ledger_test:
  evidence: source-role purity ledger
  blocks: source duplication and hidden dark-sector insertion

weak_field_residual_test:
  evidence: weak-field expansion or observational residual map
  blocks: unnoticed conflict with closed weak-field sector

epsilon_classification_test:
  evidence: results from all earlier gates plus kill condition
  blocks: free-knob epsilon language
```

Next target:

```text
open candidate branch charters only with explicit kill conditions and gate plans.
```
