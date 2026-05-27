# Vacuum Action Origin 11: First Vacuum-Action Candidate Audit

## Purpose

This report audits the first action candidate suggested by the previous gates:

```text
S[q] = integral [(1/2)q_t^2 - (1/2)c^2 q_x^2 - (1/2)m^2 q^2] dt dx
```

with boundary-flux source terms added where needed.

The audit is intentionally conservative: this candidate passes several
vacuum-action gates, but it is not yet an Einstein-Hilbert derivation.

## Validated Checks

- supporting reports exist: passed
- scalar candidate Euler-Lagrange equation: passed
- scalar candidate wave equation: passed
- scalar candidate dof mismatch against 4D massless spin-2: passed
- scalar candidate canonical momentum: passed

## Supporting Reports

- `1_response_reciprocity_interval_metric.md`
- `4_relabeling_invariance_density_gate.md`
- `5_boundary_flux_variational_source.md`
- `7_lorentzian_propagation_signature_gate.md`
- `8_local_additivity_to_gradient_strain.md`
- `10_boundary_flux_completion_commutes.md`

## Euler-Lagrange Equation

SymPy verifies:

```text
delta S / delta q
  =
  -q_tt + c^2 q_xx - m^2 q.
```

Equivalently:

```text
q_tt - c^2 q_xx + m^2 q = 0.
```

So the scalar candidate is local, hyperbolic, and second order.

## What It Passes

The scalar candidate matches these gates:

```text
local response variable;
Lorentzian propagation signature;
local gradient strain;
relabeling-compatible density in geometric form;
boundary-flux source compatibility.
```

## What It Does Not Prove

The scalar candidate has one propagating field degree of freedom. The
four-dimensional massless metric field has two.

SymPy verifies the simple count:

```text
2 - 1 = 1.
```

So the scalar action is not the final gravitational action. It is the minimal
prototype action showing how the vacuum-action gates fit together.

## Interpretation

The first assembled action candidate is useful because it exposes the next
required lift:

```text
scalar gradient strain
  -> metric/connection strain.
```

The next target is not another scalar proof. It is the action-origin reason why
the response variable must become the metric and why the strain must become
Levi-Civita curvature/connection strain.
