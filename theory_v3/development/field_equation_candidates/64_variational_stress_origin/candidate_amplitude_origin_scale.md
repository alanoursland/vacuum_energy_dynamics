# candidate_amplitude_origin_scale — Result Note

## Result

The script audits possible amplitude origins for `p_free`.

It tests:

```text
p0 = p_free + lambda*rho_M
```

and finds:

```text
d p0 / d rho_M = lambda
```

It also shows that normalization or energy-unit targets can solve for a value:

```text
p_free = N_target/k_trace
p_free = E_unit/k_mass
```

and that:

```text
p_free = 0
```

is the zero-response route.

## Main Findings

No acceptable amplitude origin is found.

Rejected:

```text
source-coupled amplitude;
diagnostic repair amplitude;
zero response.
```

Normalization remains only a scale convention. It can set units or match a target, but it does not derive the physics of `p_free`.

Therefore:

```text
p_free remains underived.
```

This weakens conditional audit retention because the amplitude is one of the required pieces in the Group 63 retention contract.

## Boundary

This does not prove no amplitude principle exists. It only rejects source-coupling, normalization-as-origin, diagnostic repair, and zero-response origins.

## Steering Consequence

Proceed to boundary variation. Endpoint silence was part of the construction; the next question is whether it can supply a variational origin.
