# candidate_general_even_shape_operator — Analysis Note

## Result

`candidate_general_even_shape_operator.py` verifies the general even compact-support operator structure.

For the `N=4` example:

```text
P_N = 1 + a1 y^2 + a2 y^4 + a3 y^6 + a4 y^8
```

the script confirms:

```text
P(-y)-P(y) = 0
J(-y)+J(y) = 0
rho(-y)-rho(y) = 0
J(-1)=J(1)=0
M1=M3=M5=M7=0
```

## Interpretation

This is the structural base of the hierarchy.

It shows that the hierarchy does not need to spend constraints on odd moments. The even shape forces:

```text
P even;
J odd;
rho even.
```

Therefore all odd moments vanish automatically on the symmetric interval.

That matters because the `N` available coefficients can be spent entirely on the first `N` nontrivial even moments:

```text
M2, M4, ..., M(2N)
```

instead of wasting capacity on odd-mode cancellation.

## What Changed

The hierarchy has a clean constraint count:

```text
N coefficients;
N even-moment constraints;
odd moments vanish by parity;
endpoint flux vanishes by compact support.
```

This makes the finite hierarchy plausible before any solving happens.

## What Did Not Change

The operator remains reduced and symmetric. The result depends on the symmetric interval and even-profile restriction. It is not yet a covariant statement.

## Steering Consequence

The next script should solve the even-moment constraints directly. If unique profiles exist at `N=1..4`, the quartic profile is not a one-off.
