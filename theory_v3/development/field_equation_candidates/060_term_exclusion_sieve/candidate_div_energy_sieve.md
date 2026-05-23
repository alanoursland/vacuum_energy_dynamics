# candidate_div_energy_sieve — Result Note

## Result

The script tests the narrowed stress-like candidate against reduced divergence and energy burdens.

For:

```text
p_r = p0*eta^2
```

the radial-only candidate:

```text
p_t=0
```

gives nonzero reduced divergence and is rejected.

The closure-supported candidate:

```text
p_t = p_r + r*p_r'/2
```

gives:

```text
D = 0
```

The layer energy/stress burden is explicit:

```text
E_layer =
256*ell*p0*(49*R^4 + 58*R^2*ell^2 + ell^4)
/
(3465*(7*R^2 + ell^2)^2)
```

with:

```text
E_layer/ell -> 256*p0/3465
```

in the thin-layer coefficient diagnostic.

## Main Findings

The radial-only stress route remains dead.

The closure-supported stress route survives the reduced divergence filter, but it is not free. It carries explicit energy/stress accounting burden.

This is a good narrowing result. The survivor is not:

```text
scalar eta;
scalar eta^2;
raw residue;
constant;
radial-only pressure.
```

It is:

```text
stress-like eta^2 with tangential closure.
```

## Boundary

Reduced `D=0` is not a Bianchi proof. The energy expression is reduced accounting, not a covariant stress-energy theorem.

## Steering Consequence

The classifier should report a narrowed survivor, not a physical term: stress-only, localized, weighted-neutral-generated, closure-supported, nonfree, and audit-only.
