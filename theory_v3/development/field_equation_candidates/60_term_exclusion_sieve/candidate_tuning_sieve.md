# candidate_tuning_sieve — Result Note

## Result

The script tests arbitrary admixture of a good neutral basis with a bad constant basis:

```text
candidate = a*eta + b
```

It finds:

```text
Q = 2*b*(3*R^2 + ell^2)/3
```

and endpoint values:

```text
left endpoint = b
right endpoint = b
```

So both weighted neutrality and endpoint locality force:

```text
b = 0
```

The script's `solve` output shows empty lists because `b` was declared positive, and `b=0` is outside that assumption. The expressions themselves make the condition clear.

## Main Findings

The constant admixture is rejected.

A bad basis cannot be kept by saying its coefficient can be tuned away. If the coefficient must be zero, the term is not a surviving basis.

The neutral amplitude:

```text
a*eta
```

remains allowed as a reduced neutral family, but its physical coefficient is not derived here.

## Boundary

This does not derive the amplitude `a`. It only rejects the bad constant admixture.

## Steering Consequence

Future work must derive any surviving amplitude from energy/stress accounting, variational origin, source safety, or another admissible principle. Arbitrary coefficient choice remains blocked.
