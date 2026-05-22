# candidate_flux_parity_decomposition — Analysis Note

## Result

`candidate_flux_parity_decomposition.py` decomposes the flux into two parity components.

With:

```text
f = (1 - y^2)^3
w = (1 - y^2)^2
Xi = f(1 + c y)
J = w dXi/dy
```

the flux is decomposed as:

```text
J = J0 + c J1
J0 = -6y(y - 1)^4(y + 1)^4
J1 = -(y - 1)^4(y + 1)^4(7y^2 - 1)
```

The important moments are:

```text
∫ J0 dy = 0
∫ y J1 dy = 0
∫ J1 dy = 1024/3465
∫ y J0 dy = -512/1155
```

The measure-gradient pairing reduces to:

```text
∫ mu' J dy = 1024 ell(2R c - 3ell)/3465
```

## Interpretation

This is the second key result of Group 83.

The skew is no longer an arbitrary knob. It has a parity role.

The decomposition shows:

```text
J0 is odd
J1 is even
mu' = 2Rell + 2ell^2 y
```

The constant part of `mu'` pairs with the even flux component `cJ1`. The odd part of `mu'` pairs with the odd flux component `J0`.

So the skew coefficient `c` is not decorative. It controls the even flux component needed to balance the measure-gradient contribution created by finite layer thickness.

## What Changed

This result gives the coefficient a structural meaning:

```text
c balances the surviving parity moments of the flux against the measure gradient.
```

That is much better than:

```text
c was selected to cancel a residual.
```

The surviving terms are forced by parity. The zero terms are not ignored; they vanish because their parity makes the integrands odd on a symmetric interval.

## What Did Not Change

The derivation is still inside a chosen compact-support shape family:

```text
f = (1-y^2)^3
w = (1-y^2)^2
linear skew = 1 + cy
```

So it does not yet prove that nature chooses this shape family. It proves that within this family, the skew has a geometric/parity role.

## Steering Consequence

The next script should derive `c` from the ratio of the surviving moments:

```text
c = -ell * ∫ yJ0 dy / (R * ∫ J1 dy)
```

That will be a stronger statement than solving weighted charge directly.
