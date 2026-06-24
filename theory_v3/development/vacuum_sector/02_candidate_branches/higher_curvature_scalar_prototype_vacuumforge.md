# VacuumForge Higher-Curvature Scalar Prototype

## Purpose

This report runs the first concrete branch test for the higher-curvature local
residual charter. It is a scalar prototype, not a tensor/covariant theorem.
Its job is to test whether a local higher-derivative residual can share the
same pointwise local response while changing the strain dynamics.

This report depends on:

```text
candidate_branch_charters_005
```

because the higher-curvature branch was opened only as a gated candidate.
It satisfies:

```text
higher_curvature_scalar_prototype_required_005
```

## Prototype Functional

Use one scalar configuration `q(x)` as a proxy for one linearized strain
channel:

```text
L_baseline = Derivative(q(x), x)**2/2
L_residual = epsilon*Derivative(q(x), (x, 2))**2/2 + Derivative(q(x), x)**2/2
```

The pointwise local-response piece has Hessian:

```text
V_local = a*q0**2/2
d^2 V_local / dq0^2 = a
```

Adding the derivative residual does not change this pointwise Hessian.

## Euler-Lagrange Check

SymPy verifies:

```text
EL_baseline = -Derivative(q(x), (x, 2))
EL_residual = epsilon*Derivative(q(x), (x, 4)) - Derivative(q(x), (x, 2))
```

The residual equation contains the fourth derivative with coefficient
`epsilon`. Therefore this branch cannot be treated as the closed second-order
metric branch unless the extra derivative structure is routed or removed by a
degeneracy.

## Boundary Variation Check

The second-derivative Lagrangian has boundary variation coefficients:

```text
coefficient of delta q      = -epsilon*Derivative(q(x), (x, 3)) + Derivative(q(x), x)
coefficient of delta qprime = epsilon*Derivative(q(x), (x, 2))
```

The `delta qprime` term is absent in the baseline first-derivative functional.
The higher-curvature branch therefore requires additional boundary data,
boundary counterterms, or a degeneracy argument before it is a well-posed
strain branch.

## Mode And Weak-Field Pole Check

For a static Fourier mode, the baseline and residual symbols are:

```text
baseline symbol = k**2
residual symbol = epsilon*k**4 + k**2
```

The residual propagator decomposes as:

```text
-epsilon/(epsilon*k**2 + 1) + k**(-2)
```

This exposes an extra pole at the scale set by `epsilon`. In a full metric
theory, the sign, tensor sector, and physical interpretation depend on the
covariant parent; the scalar prototype only proves that a weak-field residual
channel exists unless explicitly routed.

The characteristic polynomial is:

```text
epsilon*lambda**4 - lambda**2
```

with roots:

```text
0, -sqrt(1/epsilon), sqrt(1/epsilon)
```

Multiplicity:

```text
-sqrt(1/epsilon) with multiplicity 1, sqrt(1/epsilon) with multiplicity 1, 0 with multiplicity 2
```

The double zero root is the baseline second-order branch. The nonzero roots
are the extra mode data that the branch must classify.

## Gate Ledger Result

| gate | scalar-prototype result | branch consequence |
| --- | --- | --- |
| metric_limit_test | passes only at pointwise `V_local` Hessian level | local response is not enough to license dynamics |
| nonquadratic_routing_test | not triggered by this scalar metric-branch proxy | no Finsler/nonquadratic claim made |
| diffeomorphism_identity_test | not tested by scalar prototype | covariant Noether identity still owed |
| boundary_variation_test | obstruction found: `delta qprime` boundary term | boundary completion or extra data required |
| mode_count_test | obstruction found: fourth-order equation and extra roots | extra mode must be routed or killed |
| hyperbolicity_test | principal symbol changes from quadratic to quartic | full Lorentzian principal-symbol audit owed |
| source_ledger_test | not tested by scalar prototype | curvature residual must not be counted as matter |
| weak_field_residual_test | obstruction found: extra static pole | Yukawa/PPN residual map owed |
| epsilon_classification_test | controlled `epsilon != 0` not licensed | branch remains routed/underdetermined |

## Current Conclusion

The higher-curvature local residual branch fails to become a controlled
`epsilon != 0` branch at the scalar-prototype level. The prototype does not
prove that every covariant higher-curvature parent is impossible. It proves the
burden that any such parent must carry: boundary completion, extra-mode
classification, principal-symbol control, source-ledger purity, and weak-field
residual bounds.

## Classification

```text
result type: scalar prototype obstruction / first branch test
scope: local higher-derivative residual proxy
conclusion: generic higher-derivative residual is not licensed as controlled epsilon != 0
non-conclusion: no full tensor f(R), Ricci^2, Weyl^2, or Gauss-Bonnet theorem is proved here
```

The next technical target is a tensor-route audit for the higher-curvature
branch:

```text
separate inert/topological terms, scalaron/f(R)-type routes that are
ghost-safe only after mode routing, and spin-2/Weyl-type ghost routes before
any higher-curvature residual is reused.
```
