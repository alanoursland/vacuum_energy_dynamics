# Next Research Program

The project should now shift from GR branch reconstruction to vacuum strain dynamics.

The previous phases were successful:

```text
Phase I: solve r_k.
Phase II: identify scalar boundary/admissibility structure.
Phase III: separate scalar trace from tensor/Weyl sectors.
Phase IV: conditionally reconstruct the GR branch at epsilon = 0.
```

The next phase is:

```text
Phase V: specify or derive the vacuum strain functional.
```

## Primary target

Write or derive a functional of the form

```text
S_vac[X] = integral ( V_local(X) + K_strain(X, grad X, grad grad X, ...) ).
```

The local part should recover the metric-producing Hessian.

The strain part should generate transport, field equations, radiation, and possible deviations.

## Candidate axiom families

### 1. Minimal calibration-coherent strain

The strain energy is the minimal scalar measuring failure of neighboring interval responses to remain calibration-coherent.

Target:

```text
K_strain -> EH/GHY branch
```

with no residual.

### 2. Holonomy mismatch energy

The strain energy measures failure of interval-comparison transport to close around infinitesimal loops.

Target:

```text
curvature as transport mismatch;
EH-like action as minimal quadratic curvature/connection-strain completion.
```

### 3. Elastic/medium strain branch

The vacuum behaves like a medium with a constitutive tensor controlling response to configuration gradients.

Target:

```text
possible deviations from GR,
preferred-frame or anisotropic residuals,
extra modes unless constrained.
```

### 4. Finsler/nonquadratic residual branch

Nonquadratic directional response is allowed as a physical correction.

Target:

```text
epsilon != 0
```

with concrete consequences for null cones, post-Newtonian structure, or propagation.

### 5. Nonlocal or relaxation branch

The strain sector includes global or nonlocal terms.

Target:

```text
Lambda relaxation,
dark-sector-like behavior,
scale-dependent gravitational response.
```

## Success criteria

### Exact GR rederivation

```text
The functional is specified from vacuum principles and forces epsilon = 0.
```

This would make the project an ontology-based rederivation of GR.

### Predictive extension

```text
The functional predicts epsilon != 0 or an additional routed branch.
```

This would make the project a candidate extension of GR.

### Underdetermination result

```text
The current ontology cannot determine K_strain.
```

This would be an honest and valuable result. It would identify the missing physical axiom precisely.

## Recommended next folder

The next folder should be documentation plus targeted tests, not another broad GR reconstruction.

Suggested name:

```text
vacuum_strain_functional_frontier
```

It should contain:

```text
1_problem_statement.md
2_local_vs_gradient_split.md
3_candidate_functional_forms.md
4_epsilon_definition.md
5_required_axioms.md
6_testable_residuals.md
7_frontier_conclusion.md
```

Scripts should be added only where they validate a concrete candidate term, variation, degree count, or residual witness.

## Guiding rule

Do not continue proving that GR follows after choosing the GR strain branch.

The new question is:

```text
What chooses the strain branch?
```
