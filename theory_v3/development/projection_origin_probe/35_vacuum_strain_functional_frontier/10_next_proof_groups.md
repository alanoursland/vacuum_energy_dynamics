# 10. Next Proof Groups

Future work should only create proof folders when there is a checkable claim.

## Highest-value next proof group

```text
candidate_strain_functional_tests
```

Purpose:

Test concrete candidate forms for `K_strain` against the accumulated gates.

The candidate should be written in constrained residual form:

```text
K_strain = K_EH + ε K_residual.
```

Possible residual branches:

```text
quartic/nonquadratic directional residual
higher-curvature residual
elastic configuration-gradient residual
Finsler residual
nonlocal relaxation residual
calibration-drift residual
```

Scripts should validate actual identities, orders, conservation residuals, boundary terms, mode counts, or weak-field deviations.

## Second proof group

```text
epsilon_residual_model_tests
```

Purpose:

Given one or more candidate residuals, compute whether they violate known gates:

```text
parallelogram/quadratic response
universal null cone
Bianchi/conservation compatibility
boundary differentiability
post-Newtonian tensor constraints
extra mode routing
```

## Third proof group

```text
vacuum_strain_axiom_audit
```

Purpose:

Test whether proposed axioms are independent, redundant, or strong enough to eliminate residual branches.

This can include symbolic dependency tables, branch-exclusion witnesses, and counterexamples.

## Documentation-only work

The following should remain documentation unless they contain actual checks:

```text
paper outlines
reading-order updates
assumption ledgers
storyline summaries
external-reader short paths
```

No script should exist merely to generate prose.
