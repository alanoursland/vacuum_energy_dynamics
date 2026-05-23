# candidate_weighted_divergence — Result Note

## Result

The script constructs a reduced divergence-silent closure using the weighted-neutral layer shape.

It defines the weighted-neutral shape:

```text
shape = (y^2 - 1)^2*(-2*R*ell + y*(7*R^2 + ell^2))/(7*R^2 + ell^2)
```

and uses:

```text
p_r proportional to shape^2
p_t = p_r + r*p_r'/2
```

The reduced divergence diagnostic is:

```text
D = 0
```

and the endpoint stresses vanish:

```text
p_r(-1)=0
p_r(1)=0
p_t(-1)=0
p_t(1)=0
```

## Main Findings

The weighted-neutral finite layer is not automatically divergence-bad.

The same geometry-aware weighted shape can support a localized reduced stress profile that is endpoint-silent and reduced-divergence silent.

This is constructive progress because the route now satisfies:

```text
weighted charge neutrality;
reduced tail/mass diagnostic silence;
finite reduced energy;
endpoint localization;
reduced D=0 closure.
```

## Boundary

The result is not a covariant Bianchi proof. The stress closure is not an inserted parent-equation term. It does not prove source safety.

## Steering Consequence

The route is ready for classification. The classifier should preserve the result as a conditional reduced theorem surface, not as insertion.
