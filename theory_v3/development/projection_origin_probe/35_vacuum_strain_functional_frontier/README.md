# Vacuum Strain Functional Frontier

This folder marks the transition from GR-branch reconstruction to vacuum-theory construction.

It is not a proof-script group. It is a frontier specification folder: it records that the prior proof chain has **localized** the remaining field-equation problem to one object, the strain/gradient sector of the vacuum configuration functional.

The current chain has largely constrained the local response side of the theory:

```text
directional interval response -> Hessian/quadratic response -> metric data
```

The remaining dynamics have been compressed into a single completion object:

```text
vacuum strain/gradient functional -> transport law -> curvature dynamics -> radiation -> epsilon
```

The key object is the strain sector of the vacuum configuration functional:

```text
S_vac[X] = ∫ ( V_local(X) + K_strain(X, ∇X, ∇∇X, ...) ).
```

The local part can explain why metric-like data appears. The strain part must explain why the metric propagates, why the transport law is what it is, why GR is recovered or modified, and whether any nonmetric residual survives.

The point is not simply that this functional is missing. The point is stronger: the prior gates have localized field equations, dynamics, radiation, and any deviation from GR to this functional.

Read in order:

```text
proof_chain_plan.md
1_problem_statement.md
2_current_closure_ledger.md
3_local_response_vs_strain_dynamics.md
4_localized_strain_functional.md
5_accumulated_constraints_on_kstrain.md
6_candidate_functional_branches.md
7_epsilon_residual_definition.md
8_field_equation_generation_target.md
9_success_failure_criteria.md
10_next_proof_groups.md
11_frontier_conclusion.md
```
