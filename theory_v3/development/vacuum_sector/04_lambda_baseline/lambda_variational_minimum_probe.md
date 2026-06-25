# Lambda Variational-Minimum Probe

This probe tests the first concrete selector route opened by the selector
sieve: a variational minimum over the `Lambda` baseline. It tests selector
functionals `F(Lambda)`, not variation of the full EH action with respect to
`Lambda`.

It does not derive a nonzero `Lambda`. It asks what a bare stationarity
principle can choose before a boundary class, bias, target value, measure
identity, relaxation law, or microphysical scale is supplied.

## Probe Cases

| case | stationarity outcome | disposition |
| --- | --- | --- |
| no selector functional | `dF/dLambda = 0` identically | `Lambda` remains free |
| no-scale convex minimum | `F = a Lambda^2 / 2` gives `Lambda = 0` | selects zero, not a nonzero floor |
| linear bias only | `F = b Lambda` gives no interior stationary point for nonzero `b` on an unconstrained continuous domain | no bare minimum |
| biased convex minimum | `F = a Lambda^2 / 2 + b Lambda` gives `Lambda = -b/a` | nonzero value comes from imported `b/a` |
| target-inserted minimum | `F = a (Lambda - Lambda_star)^2 / 2` gives `Lambda = Lambda_star` | target is inserted, not derived |

## Working Conclusion

The variational-minimum route is not mechanism-ready as a derived nonzero
baseline. It can do one of three things with the current inputs:

```text
leave Lambda free;
select Lambda = 0;
produce nonzero Lambda only from an imported bias, target, or scale.
```

This does not kill variational selection in general. It says the next missing
object is the source of scale or the admissibility condition that gives the
variational problem content.

A boundary extremum for a restricted `Lambda` domain is not part of this bare
probe. That possibility belongs to the boundary/admissibility route.

## Next Handoff

The next selector to test is the boundary/admissibility route:

```text
can explicit boundary data select a nonzero baseline without observed-value
insertion or local-equation modification?
```
