# candidate_measure_gradient_identity — Analysis Note

## Result

`candidate_measure_gradient_identity.py` derives the weighted integration-by-parts identity.

With:

```text
rho = dJ/dy
mu = R^2 + 2Rell y + ell^2 y^2
mu' = 2Rell + 2ell^2 y
```

the weighted charge becomes:

```text
∫ mu rho dy
  = [mu J]_{-1}^{1} - ∫ mu' J dy
```

The script writes the endpoint terms explicitly:

```text
-(R^2 - 2Rell + ell^2)J(-1)
+ (R^2 + 2Rell + ell^2)J(1)
```

With compact endpoint flux:

```text
J(-1) = J(1) = 0
```

the weighted charge reduces to:

```text
Q_mu = -∫ mu' J dy
```

## Interpretation

This is the first key theorem-level result of Group 83.

Group 82 showed that a nonconstant measure breaks automatic flat neutrality. Group 83 explains why: the obstruction is not mysterious. It is the interior pairing between the flux and the measure gradient.

That means the weighted problem is not “exactness failed.” It is more precise:

```text
exactness moves the problem from rho to the flux J paired against mu'
```

So weighted neutrality requires:

```text
∫ mu' J dy = 0
```

This is a geometric orthogonality condition.

## What Changed

The weighted obstruction is now reinterpreted structurally.

Before this script, the weighted charge looked like an output residual:

```text
weighted charge = 1024 ell^2 / 1155
```

After this script, it is understood as:

```text
measure-gradient flux imbalance
```

That is stronger because it gives a mechanism for the obstruction and a legitimate route to removing it.

## What Did Not Change

This identity does not prove weighted neutrality by itself. It only transforms the problem.

The following remain open:

```text
find a flux shape orthogonal to mu';
derive the skew from that condition;
lift the reduced result covariantly;
prove local rho inertness.
```

## Steering Consequence

This script justifies the next move: decompose `J` into parity pieces and identify which pieces pair with the constant and odd parts of `mu'`.
