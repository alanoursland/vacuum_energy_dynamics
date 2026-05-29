# Origin Story: From `r_k` to Boundary Admissibility

The project started with the coefficient

```text
r_k = (2k - 1)/(2k + 3).
```

It appeared in the projection row

```text
psi_k(x) = x^(2k) - r_k x^(2k-2).
```

At first, the question was whether this coefficient was numerology, engineered cancellation, or a physically meaningful signature.

The current answer is precise:

```text
r_k is a scalar boundary/admissibility coefficient.
```

It is the base case of the endpoint-contact ladder

```text
r_(R,k) = (2k - 1)/(2k + 2R + 3),
```

with `R = 0`.

The same coefficient is obtained through several equivalent routes.

## Moment-kernel route

The compactified moment functional has the form

```text
C_R[P] = integral_0^1 P(y) (1-y)^(R+1) y^(-1/2) dy.
```

The kernel row

```text
chi_(R,k)(y) = y^k - r_(R,k) y^(k-1)
```

is chosen so that

```text
C_R[chi_(R,k)] = 0.
```

At `R = 0`, this gives the original `r_k`.

## Primitive / integration-by-parts route

The same ratio appears from a primitive with endpoint contact. The primitive derivative produces the `psi_k` row up to a scalar factor, and the boundary term is killed by endpoint contact. This explains why the coefficient is natural rather than tuned.

## Boundary-reduction route

The coefficient also appears as the finite-dimensional shadow of ordinary boundary reduction: integration by parts, compactified endpoints, flux ledgers, and moment-pairing admissibility.

## Consequence

The original mystery is solved. That is not a disappointment. It is the best possible resolution for the initial hook.

The coefficient did not turn out to be the final field equation. It turned out to be the breadcrumb that exposed a scalar boundary/admissibility structure.

The correct status is:

```text
r_k is real structure.
r_k is not standalone physics.
r_k is not the full vacuum ontology.
r_k is the scalar boundary trace of a deeper problem.
```

This solved problem motivated the rest of the chain.
