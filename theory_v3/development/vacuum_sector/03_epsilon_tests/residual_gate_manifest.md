# Residual Gate Manifest

Every candidate residual must be tested against this manifest before it is
treated as physically live.

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
