# candidate_source_coupling — Result Note

## Result

The script tests direct ordinary-source dependence in the transition stress amplitude.

It uses:

```text
p0 = p_free + lambda*rho_M
p_r = eta^2*(lambda*rho_M + p_free)
```

and finds:

```text
d(p_r)/d(rho_M) = eta^2*lambda
```

The source-neutral condition is:

```text
lambda = 0
```

## Main Findings

Direct matter-density coupling in the transition amplitude is rejected.

If `lambda != 0`, then the stress-only transition response has hidden ordinary-source dependence. That would undermine the source-clean interpretation.

A source-independent amplitude remains possible:

```text
p0 = p_free
```

but `p_free` is not derived. Its origin remains an energy/stress accounting burden.

## Boundary

This does not prove that `p_free` is source-safe. It only rejects direct `rho_M` coupling.

## Steering Consequence

The next check should test whether the stress response has a nonzero mass/energy moment even if it is not directly source-coupled.
