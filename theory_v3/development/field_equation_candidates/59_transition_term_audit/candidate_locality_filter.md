# candidate_locality_filter — Result Note

## Result

The script applies an endpoint-locality filter to candidate layer bases.

It verifies endpoint value and derivative localization for:

```text
w
eta
eta^2
```

at:

```text
y=-1
y=1
```

The results are:

```text
w(-1)=w(1)=0
w'(-1)=w'(1)=0

eta(-1)=eta(1)=0
eta'(-1)=eta'(1)=0

eta^2(-1)=eta^2(1)=0
(eta^2)'(-1)=(eta^2)'(1)=0
```

It rejects the constant candidate:

```text
constant(-1)=constant(1)=1
```

## Main Findings

The weighted layer bases pass the reduced endpoint-locality filter. This means they can be treated as layer-local candidate surfaces in the reduced model.

The constant term fails because it does not vanish at the layer endpoints. It cannot be interpreted as a layer-only response.

This is real restriction progress. It kills a common repair-term temptation:

```text
add a constant background layer response
```

That would leak outside the layer and would not be a localized transition term.

## Boundary

Endpoint locality is not weighted neutrality. It is also not covariant compact support. It is only a reduced radial locality test.

## Steering Consequence

After locality, the next required filter is weighted neutrality. Candidate scalar profiles must not carry weighted scalar charge.
