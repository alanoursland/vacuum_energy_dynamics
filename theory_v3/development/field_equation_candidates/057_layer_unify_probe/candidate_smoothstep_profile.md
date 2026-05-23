# candidate_smoothstep_profile — Result Note

## Result

The script constructs the finite-layer coordinate:

```text
x(r)=(-R+ell+r)/(2*ell)
```

and the quintic smoothstep:

```text
s(x)=10*x^3 - 15*x^4 + 6*x^5
```

It verifies the endpoint behavior:

```text
s(0)=0
s(1)=1
s'(0)=s'(1)=0
s''(0)=s''(1)=0
```

and the corresponding radial endpoint behavior:

```text
s_r(R-ell)=0
s_r(R+ell)=1
s_r'(R-ell)=s_r'(R+ell)=0
s_r''(R-ell)=s_r''(R+ell)=0
```

## Main Findings

This is useful reduced boundary-layer progress. The layer can transition from interior to exterior while avoiding endpoint value, slope, and curvature mismatch in the reduced coordinate.

That matters because the previous hard-boundary picture only tested a shell jump at a single radius. The smoothstep gives a finite region where the transition can be distributed while still matching smoothly to the asymptotic interior/exterior regimes.

## Boundary

The smoothstep is a probe function, not a physical law. Endpoint smoothness is not charge neutrality, mass neutrality, or divergence safety.

## Steering Consequence

The next check must compute the derivative residues created by blending. A smooth layer is not free; the transition terms must be explicit.
