# Boundary Flux Field Bridge 67: Monopole Dominance in the Far Field

## Purpose

This report validates why the monopole controls the far field whenever it is
present.

## Validated Checks

- mode-to-monopole potential ratio: passed
- mode-to-monopole field ratio: passed
- explicit potential suppression for l=1..7: passed
- leading mode potential exponent: passed
- leading mode field exponent: passed

## Exterior Mode Decay

The monopole mode is:

```text
u_0(r) = U_0 R/r.
```

The `l`th exterior mode is:

```text
u_l(r) = U_l (R/r)^(l+1).
```

Therefore:

```text
u_l/u_0 = (U_l/U_0)(R/r)^l.
```

For `r >> R`, every `l>0` mode is suppressed relative to the monopole.

## Field Strength

The field ratio is:

```text
(-u_l')/(-u_0') = (l+1)(U_l/U_0)(R/r)^l.
```

So higher modes are also suppressed in field strength by the same far-field
power, up to the factor `l+1`.

## Leading Nonzero Mode

If the first nonzero mode is `L`, then:

```text
u_L(r) ~ r^(-(L+1))
|grad u_L| ~ r^(-(L+2)).
```

The inverse-square field is therefore specifically the nonzero monopole case
in three spatial dimensions.
