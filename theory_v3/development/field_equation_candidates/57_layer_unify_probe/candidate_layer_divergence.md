# candidate_layer_divergence — Result Note

## Result

The script constructs a reduced layer-local stress profile and a divergence-silent closure.

It uses a layer-local radial stress proportional to:

```text
[s(1-s)]^2
```

and chooses:

```text
p_t = p_r + r*p_r'/2
```

For the reduced radial divergence diagnostic:

```text
D = p_r' + 2*(p_r-p_t)/r
```

it verifies:

```text
D = 0
```

It also verifies endpoint silence:

```text
p_r(left)=0
p_r(right)=0
p_t(left)=0
p_t(right)=0
```

## Main Findings

This is real reduced progress. A finite layer can carry a localized stress-like response while remaining reduced-divergence silent and vanishing at the layer endpoints.

That supports the idea that the boundary layer may contain nontrivial response structure without automatically creating a reduced divergence obstruction.

But the script correctly rejects overclaiming:

```text
D=0 is not a covariant Bianchi proof;
layer stress is not a parent term;
divergence silence does not prove charge neutrality.
```

## Boundary

The closure is reduced and radial. It is not a covariant identity and not a field-equation insertion.

## Steering Consequence

The finite layer route survives the reduced divergence diagnostic, but still needs weighted charge neutrality and covariant lift.
