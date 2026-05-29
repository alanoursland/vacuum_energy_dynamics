# Synthesis Proof 10: Boundary Domain Classifier

## Purpose

This report classifies boundary behavior for model endpoint profiles.

It checks the two boundary terms used in the synthesis:

```text
[a^5 f g]_0^1
[a^5 eta L[f]]_0^1
```

## Validated Identities

- adjoint boundary model exponent: passed
- variational boundary model exponent: passed
- integer boundary tables generated: passed

## Adjoint Boundary Term

For model profiles:

```text
f = a^s
g = x^r
```

the adjoint boundary term is:

```text
a^5 f g = a^(5+s)x^r.
```

Thus:

```text
x = 1 is controlled by 5+s
x = 0 is controlled by r
```

## Variational Boundary Term

For:

```text
eta = a^t
f = a^s
```

the operator gives:

```text
L[a^s] = -2(s+3)x a^s.
```

So:

```text
a^5 eta L[f] = -2(s+3)x a^(5+s+t).
```

The exceptional model power `s=-3` makes `L[a^s]=0` formally.

## Adjoint Boundary Table

```text
s=-7, r=0: x=1 exponent a^-2 -> singular/nonvanishing; x=0 exponent x^0 -> finite nonzero
s=-7, r=1: x=1 exponent a^-2 -> singular/nonvanishing; x=0 exponent x^1 -> vanishes
s=-7, r=2: x=1 exponent a^-2 -> singular/nonvanishing; x=0 exponent x^2 -> vanishes
s=-7, r=3: x=1 exponent a^-2 -> singular/nonvanishing; x=0 exponent x^3 -> vanishes
s=-7, r=4: x=1 exponent a^-2 -> singular/nonvanishing; x=0 exponent x^4 -> vanishes
s=-6, r=0: x=1 exponent a^-1 -> singular/nonvanishing; x=0 exponent x^0 -> finite nonzero
s=-6, r=1: x=1 exponent a^-1 -> singular/nonvanishing; x=0 exponent x^1 -> vanishes
s=-6, r=2: x=1 exponent a^-1 -> singular/nonvanishing; x=0 exponent x^2 -> vanishes
s=-6, r=3: x=1 exponent a^-1 -> singular/nonvanishing; x=0 exponent x^3 -> vanishes
s=-6, r=4: x=1 exponent a^-1 -> singular/nonvanishing; x=0 exponent x^4 -> vanishes
s=-5, r=0: x=1 exponent a^ 0 -> finite nonzero; x=0 exponent x^0 -> finite nonzero
s=-5, r=1: x=1 exponent a^ 0 -> finite nonzero; x=0 exponent x^1 -> vanishes
s=-5, r=2: x=1 exponent a^ 0 -> finite nonzero; x=0 exponent x^2 -> vanishes
s=-5, r=3: x=1 exponent a^ 0 -> finite nonzero; x=0 exponent x^3 -> vanishes
s=-5, r=4: x=1 exponent a^ 0 -> finite nonzero; x=0 exponent x^4 -> vanishes
s=-4, r=0: x=1 exponent a^ 1 -> vanishes; x=0 exponent x^0 -> finite nonzero
s=-4, r=1: x=1 exponent a^ 1 -> vanishes; x=0 exponent x^1 -> vanishes
s=-4, r=2: x=1 exponent a^ 1 -> vanishes; x=0 exponent x^2 -> vanishes
s=-4, r=3: x=1 exponent a^ 1 -> vanishes; x=0 exponent x^3 -> vanishes
s=-4, r=4: x=1 exponent a^ 1 -> vanishes; x=0 exponent x^4 -> vanishes
s=-3, r=0: x=1 exponent a^ 2 -> vanishes; x=0 exponent x^0 -> finite nonzero
s=-3, r=1: x=1 exponent a^ 2 -> vanishes; x=0 exponent x^1 -> vanishes
s=-3, r=2: x=1 exponent a^ 2 -> vanishes; x=0 exponent x^2 -> vanishes
s=-3, r=3: x=1 exponent a^ 2 -> vanishes; x=0 exponent x^3 -> vanishes
s=-3, r=4: x=1 exponent a^ 2 -> vanishes; x=0 exponent x^4 -> vanishes
s=-2, r=0: x=1 exponent a^ 3 -> vanishes; x=0 exponent x^0 -> finite nonzero
s=-2, r=1: x=1 exponent a^ 3 -> vanishes; x=0 exponent x^1 -> vanishes
s=-2, r=2: x=1 exponent a^ 3 -> vanishes; x=0 exponent x^2 -> vanishes
s=-2, r=3: x=1 exponent a^ 3 -> vanishes; x=0 exponent x^3 -> vanishes
s=-2, r=4: x=1 exponent a^ 3 -> vanishes; x=0 exponent x^4 -> vanishes
s=-1, r=0: x=1 exponent a^ 4 -> vanishes; x=0 exponent x^0 -> finite nonzero
s=-1, r=1: x=1 exponent a^ 4 -> vanishes; x=0 exponent x^1 -> vanishes
s=-1, r=2: x=1 exponent a^ 4 -> vanishes; x=0 exponent x^2 -> vanishes
s=-1, r=3: x=1 exponent a^ 4 -> vanishes; x=0 exponent x^3 -> vanishes
s=-1, r=4: x=1 exponent a^ 4 -> vanishes; x=0 exponent x^4 -> vanishes
s= 0, r=0: x=1 exponent a^ 5 -> vanishes; x=0 exponent x^0 -> finite nonzero
s= 0, r=1: x=1 exponent a^ 5 -> vanishes; x=0 exponent x^1 -> vanishes
s= 0, r=2: x=1 exponent a^ 5 -> vanishes; x=0 exponent x^2 -> vanishes
s= 0, r=3: x=1 exponent a^ 5 -> vanishes; x=0 exponent x^3 -> vanishes
s= 0, r=4: x=1 exponent a^ 5 -> vanishes; x=0 exponent x^4 -> vanishes
s= 1, r=0: x=1 exponent a^ 6 -> vanishes; x=0 exponent x^0 -> finite nonzero
s= 1, r=1: x=1 exponent a^ 6 -> vanishes; x=0 exponent x^1 -> vanishes
s= 1, r=2: x=1 exponent a^ 6 -> vanishes; x=0 exponent x^2 -> vanishes
s= 1, r=3: x=1 exponent a^ 6 -> vanishes; x=0 exponent x^3 -> vanishes
s= 1, r=4: x=1 exponent a^ 6 -> vanishes; x=0 exponent x^4 -> vanishes
s= 2, r=0: x=1 exponent a^ 7 -> vanishes; x=0 exponent x^0 -> finite nonzero
s= 2, r=1: x=1 exponent a^ 7 -> vanishes; x=0 exponent x^1 -> vanishes
s= 2, r=2: x=1 exponent a^ 7 -> vanishes; x=0 exponent x^2 -> vanishes
s= 2, r=3: x=1 exponent a^ 7 -> vanishes; x=0 exponent x^3 -> vanishes
s= 2, r=4: x=1 exponent a^ 7 -> vanishes; x=0 exponent x^4 -> vanishes
s= 3, r=0: x=1 exponent a^ 8 -> vanishes; x=0 exponent x^0 -> finite nonzero
s= 3, r=1: x=1 exponent a^ 8 -> vanishes; x=0 exponent x^1 -> vanishes
s= 3, r=2: x=1 exponent a^ 8 -> vanishes; x=0 exponent x^2 -> vanishes
s= 3, r=3: x=1 exponent a^ 8 -> vanishes; x=0 exponent x^3 -> vanishes
s= 3, r=4: x=1 exponent a^ 8 -> vanishes; x=0 exponent x^4 -> vanishes
```

## Variational Boundary Table

```text
s=-7, t=-3: x=1 exponent a^-5 -> singular/nonvanishing; x=0 -> vanishes
s=-7, t=-2: x=1 exponent a^-4 -> singular/nonvanishing; x=0 -> vanishes
s=-7, t=-1: x=1 exponent a^-3 -> singular/nonvanishing; x=0 -> vanishes
s=-7, t= 0: x=1 exponent a^-2 -> singular/nonvanishing; x=0 -> vanishes
s=-7, t= 1: x=1 exponent a^-1 -> singular/nonvanishing; x=0 -> vanishes
s=-7, t= 2: x=1 exponent a^ 0 -> finite nonzero; x=0 -> vanishes
s=-7, t= 3: x=1 exponent a^ 1 -> vanishes; x=0 -> vanishes
s=-6, t=-3: x=1 exponent a^-4 -> singular/nonvanishing; x=0 -> vanishes
s=-6, t=-2: x=1 exponent a^-3 -> singular/nonvanishing; x=0 -> vanishes
s=-6, t=-1: x=1 exponent a^-2 -> singular/nonvanishing; x=0 -> vanishes
s=-6, t= 0: x=1 exponent a^-1 -> singular/nonvanishing; x=0 -> vanishes
s=-6, t= 1: x=1 exponent a^ 0 -> finite nonzero; x=0 -> vanishes
s=-6, t= 2: x=1 exponent a^ 1 -> vanishes; x=0 -> vanishes
s=-6, t= 3: x=1 exponent a^ 2 -> vanishes; x=0 -> vanishes
s=-5, t=-3: x=1 exponent a^-3 -> singular/nonvanishing; x=0 -> vanishes
s=-5, t=-2: x=1 exponent a^-2 -> singular/nonvanishing; x=0 -> vanishes
s=-5, t=-1: x=1 exponent a^-1 -> singular/nonvanishing; x=0 -> vanishes
s=-5, t= 0: x=1 exponent a^ 0 -> finite nonzero; x=0 -> vanishes
s=-5, t= 1: x=1 exponent a^ 1 -> vanishes; x=0 -> vanishes
s=-5, t= 2: x=1 exponent a^ 2 -> vanishes; x=0 -> vanishes
s=-5, t= 3: x=1 exponent a^ 3 -> vanishes; x=0 -> vanishes
s=-4, t=-3: x=1 exponent a^-2 -> singular/nonvanishing; x=0 -> vanishes
s=-4, t=-2: x=1 exponent a^-1 -> singular/nonvanishing; x=0 -> vanishes
s=-4, t=-1: x=1 exponent a^ 0 -> finite nonzero; x=0 -> vanishes
s=-4, t= 0: x=1 exponent a^ 1 -> vanishes; x=0 -> vanishes
s=-4, t= 1: x=1 exponent a^ 2 -> vanishes; x=0 -> vanishes
s=-4, t= 2: x=1 exponent a^ 3 -> vanishes; x=0 -> vanishes
s=-4, t= 3: x=1 exponent a^ 4 -> vanishes; x=0 -> vanishes
s=-3, t=-3: x=1 exponent a^-1 -> zero coefficient; x=0 -> zero coefficient
s=-3, t=-2: x=1 exponent a^ 0 -> zero coefficient; x=0 -> zero coefficient
s=-3, t=-1: x=1 exponent a^ 1 -> zero coefficient; x=0 -> zero coefficient
s=-3, t= 0: x=1 exponent a^ 2 -> zero coefficient; x=0 -> zero coefficient
s=-3, t= 1: x=1 exponent a^ 3 -> zero coefficient; x=0 -> zero coefficient
s=-3, t= 2: x=1 exponent a^ 4 -> zero coefficient; x=0 -> zero coefficient
s=-3, t= 3: x=1 exponent a^ 5 -> zero coefficient; x=0 -> zero coefficient
s=-2, t=-3: x=1 exponent a^ 0 -> finite nonzero; x=0 -> vanishes
s=-2, t=-2: x=1 exponent a^ 1 -> vanishes; x=0 -> vanishes
s=-2, t=-1: x=1 exponent a^ 2 -> vanishes; x=0 -> vanishes
s=-2, t= 0: x=1 exponent a^ 3 -> vanishes; x=0 -> vanishes
s=-2, t= 1: x=1 exponent a^ 4 -> vanishes; x=0 -> vanishes
s=-2, t= 2: x=1 exponent a^ 5 -> vanishes; x=0 -> vanishes
s=-2, t= 3: x=1 exponent a^ 6 -> vanishes; x=0 -> vanishes
s=-1, t=-3: x=1 exponent a^ 1 -> vanishes; x=0 -> vanishes
s=-1, t=-2: x=1 exponent a^ 2 -> vanishes; x=0 -> vanishes
s=-1, t=-1: x=1 exponent a^ 3 -> vanishes; x=0 -> vanishes
s=-1, t= 0: x=1 exponent a^ 4 -> vanishes; x=0 -> vanishes
s=-1, t= 1: x=1 exponent a^ 5 -> vanishes; x=0 -> vanishes
s=-1, t= 2: x=1 exponent a^ 6 -> vanishes; x=0 -> vanishes
s=-1, t= 3: x=1 exponent a^ 7 -> vanishes; x=0 -> vanishes
s= 0, t=-3: x=1 exponent a^ 2 -> vanishes; x=0 -> vanishes
s= 0, t=-2: x=1 exponent a^ 3 -> vanishes; x=0 -> vanishes
s= 0, t=-1: x=1 exponent a^ 4 -> vanishes; x=0 -> vanishes
s= 0, t= 0: x=1 exponent a^ 5 -> vanishes; x=0 -> vanishes
s= 0, t= 1: x=1 exponent a^ 6 -> vanishes; x=0 -> vanishes
s= 0, t= 2: x=1 exponent a^ 7 -> vanishes; x=0 -> vanishes
s= 0, t= 3: x=1 exponent a^ 8 -> vanishes; x=0 -> vanishes
s= 1, t=-3: x=1 exponent a^ 3 -> vanishes; x=0 -> vanishes
s= 1, t=-2: x=1 exponent a^ 4 -> vanishes; x=0 -> vanishes
s= 1, t=-1: x=1 exponent a^ 5 -> vanishes; x=0 -> vanishes
s= 1, t= 0: x=1 exponent a^ 6 -> vanishes; x=0 -> vanishes
s= 1, t= 1: x=1 exponent a^ 7 -> vanishes; x=0 -> vanishes
s= 1, t= 2: x=1 exponent a^ 8 -> vanishes; x=0 -> vanishes
s= 1, t= 3: x=1 exponent a^ 9 -> vanishes; x=0 -> vanishes
s= 2, t=-3: x=1 exponent a^ 4 -> vanishes; x=0 -> vanishes
s= 2, t=-2: x=1 exponent a^ 5 -> vanishes; x=0 -> vanishes
s= 2, t=-1: x=1 exponent a^ 6 -> vanishes; x=0 -> vanishes
s= 2, t= 0: x=1 exponent a^ 7 -> vanishes; x=0 -> vanishes
s= 2, t= 1: x=1 exponent a^ 8 -> vanishes; x=0 -> vanishes
s= 2, t= 2: x=1 exponent a^ 9 -> vanishes; x=0 -> vanishes
s= 2, t= 3: x=1 exponent a^10 -> vanishes; x=0 -> vanishes
s= 3, t=-3: x=1 exponent a^ 5 -> vanishes; x=0 -> vanishes
s= 3, t=-2: x=1 exponent a^ 6 -> vanishes; x=0 -> vanishes
s= 3, t=-1: x=1 exponent a^ 7 -> vanishes; x=0 -> vanishes
s= 3, t= 0: x=1 exponent a^ 8 -> vanishes; x=0 -> vanishes
s= 3, t= 1: x=1 exponent a^ 9 -> vanishes; x=0 -> vanishes
s= 3, t= 2: x=1 exponent a^10 -> vanishes; x=0 -> vanishes
s= 3, t= 3: x=1 exponent a^11 -> vanishes; x=0 -> vanishes
```
