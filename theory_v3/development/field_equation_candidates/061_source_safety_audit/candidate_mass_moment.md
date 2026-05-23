# candidate_mass_moment — Result Note

## Result

The script computes the reduced layer energy/mass-moment diagnostic for the stress-only response.

It finds:

```text
E_layer =
256*ell*p0*(49*R^4 + 58*R^2*ell^2 + ell^4)
/
(3465*(7*R^2 + ell^2)^2)
```

and:

```text
Delta_M =
256*beta*ell*p0*(49*R^4 + 58*R^2*ell^2 + ell^4)
/
(3465*(7*R^2 + ell^2)^2)
```

## Main Findings

The stress-only response has a nonzero reduced layer moment.

That means weighted scalar neutrality is not enough to claim mass safety. The stress-like route is nonfree and can carry a mass-shift diagnostic if it is mass-coupled.

The unsafe condition is:

```text
beta != 0
```

because then:

```text
Delta_M != 0
```

So the mass-coupled interpretation remains blocked unless a theorem shows the layer stress is inert, compensated, or otherwise mass-neutral.

## Boundary

This is a reduced diagnostic, not a full mass theorem.

## Steering Consequence

The next check should ask whether trace-free and active-mass-neutral closure can be satisfied together. That determines whether a simple energy-density choice can save the route.
