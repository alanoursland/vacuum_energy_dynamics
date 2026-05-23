# candidate_layer_energy — Result Note

## Result

The script computes a reduced gradient-energy scaling for a smooth finite layer.

Using a normalized layer coordinate `y`, it obtains:

```text
s(y)=3*y^5/16 - 5*y^3/8 + 15*y/16 + 1/2
dF/dr = 15*A*(y^4 - 2*y^2 + 1)/(16*ell)
E_density = 225*A^2*(y^4 - 2*y^2 + 1)^2/(256*ell^2)
integral E dr = 5*A^2/(7*ell)
```

## Main Findings

This is a strong accounting result. Smooth blending has an explicit finite energy cost for finite `ell`:

```text
E_layer = 5*A^2/(7*ell)
```

The scaling is important. As the layer thickness shrinks,

```text
ell -> 0
```

the energy cost grows like:

```text
1/ell
```

So the hard-shell limit is not free. This supports the physical intuition that boundary transitions should be smooth and finite-width rather than collapsed into a zero-thickness junction.

## Boundary

Finite reduced gradient energy is not safety proof. It does not prove charge neutrality, mass neutrality, or a covariant stress tensor.

## Steering Consequence

The next check must audit layer charge and mass. A finite-energy layer can still carry forbidden scalar charge or shift exterior mass.
