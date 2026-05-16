# candidate_divergence_silent_stress — Result Note

## Result

The script constructs a reduced divergence-silent anisotropic stress closure.

It chooses:

```text
p_r = p0*r^2*(R-r)^2
p_t = p_r + r*p_r'/2
```

which gives:

```text
p_t = p0*r^2*(R-r)*(2*R-3*r)
```

For the reduced radial divergence diagnostic:

```text
D = p_r' + 2*(p_r-p_t)/r
```

the script verifies:

```text
D = 0
```

It also verifies boundary-null stress:

```text
p_r(R)=0
p_t(R)=0
```

## Main Findings

This is the main reduced divergence result of Group 56.

The script shows that a nontrivial reduced anisotropic closure can be built so that the reduced divergence diagnostic vanishes while the stress is boundary-null.

That is real field-equation-adjacent progress. It gives the silent/inert route a concrete reduced compatibility condition with divergence silence, instead of leaving “divergence safety” as pure prose.

## Boundary

This is not a covariant Bianchi identity proof. It is not a full stress-energy law. It is not adopted physics. It does not insert `B_s/F_zeta`.

## Steering Consequence

The reduced silent route now has all of the intended pieces:

```text
boundary-null profile;
charge-neutral internal profile;
zero exterior tail under Q=0 and C0=0;
no-shell reduced match;
reduced divergence-silent closure.
```

The classifier should decide whether this survives as a conditional theorem surface.
