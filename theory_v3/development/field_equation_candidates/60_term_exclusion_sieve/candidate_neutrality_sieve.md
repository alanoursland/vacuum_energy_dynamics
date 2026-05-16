# candidate_neutrality_sieve — Result Note

## Result

The script tests weighted scalar charge for:

```text
eta
eta^2
constant
```

It finds:

```text
Q[eta] = 0
```

but:

```text
Q[eta^2] =
256*(637*R^6 + 173*R^4*ell^2 + 3*R^2*ell^4 + 3*ell^6)
/
(45045*(7*R^2 + ell^2)^2)
```

and:

```text
Q[constant] = 2*(3*R^2 + ell^2)/3
```

So `eta` is weighted-neutral as a scalar basis, while `eta^2` and the constant basis are not weighted-neutral scalar responses.

## Main Findings

This is the key narrowing result of Group 60.

The derivative sieve made `eta^2` attractive because it has stronger endpoint derivative silence. But the neutrality sieve says:

```text
eta^2 cannot be used as a scalar-charge response.
```

Therefore `eta^2` can survive only as a stress-like or energy-like basis, not as a scalar source/profile.

That is a good goblin trap exposed: the prettier derivative object is not scalar-neutral.

## Boundary

The script does not reject `eta^2` completely. It rejects `eta^2` as a scalar response. Its only possible survival is stress-only, closure-supported, and source-safe.

## Steering Consequence

The survivor is now much narrower:

```text
not raw residue;
not scalar eta^2;
not constant;
stress-like eta^2 only, if closure/source/covariant burdens are met.
```
