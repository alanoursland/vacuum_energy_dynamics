# candidate_exact_operator_requirements — Analysis Note

## Result

`candidate_exact_operator_requirements.py` derives the exactness requirement:

```text
rho = dJ(y)/dy
```

so:

```text
∫[-1,1] rho dy = -J(-1) + J(1)
```

If:

```text
J(-1) = J(1)
```

and especially if both endpoint fluxes vanish, then the flat integrated `rho` charge is zero.

## Interpretation

This is the basic mathematical theorem behind the group.

The important point is not merely that the integral vanishes. The important point is that exactness has a specific, limited power:

```text
it can remove the global flat charge of rho
```

but only through boundary flux. That means exactness is not a local annihilator. It is a redistribution structure. It can make the total charge zero while leaving positive and negative local structure inside the layer.

This matters for the broader theory because the lift residual problem was ambiguous before Group 82. We were asking whether `rho` could be “exact” or “nonphysical.” This script clarifies that exactness alone only buys a global statement unless additional assumptions prove local inertness or covariant neutrality.

## Conceptual Consequence

This result should be recorded as a genuine reduced theorem:

```text
Exact derivative + controlled endpoint flux -> flat integrated neutrality.
```

But it should not be recorded as:

```text
rho removed;
rho harmless;
rho covariantly neutral;
rho physically inert.
```

Those remain separate debts.

## Boundary

The script correctly rejects the dangerous overclaim:

```text
vanishing integral = local rho vanishing
```

That distinction is central to everything Group 82 teaches.

## Steering Consequence

This script earns the group’s theorem attempt. It gives the exactness route its first legitimate positive foothold, but it also sharply limits what that foothold means.
