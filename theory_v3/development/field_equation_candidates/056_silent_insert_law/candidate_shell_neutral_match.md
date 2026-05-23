# candidate_shell_neutral_match — Result Note

## Result

The script verifies reduced shell-neutral matching for a boundary-null interior profile matched to exterior zero.

With:

```text
phi_int = A*r^2*(R-r)^2
phi_ext'(R) = 0
```

it obtains:

```text
phi_int(R) = 0
phi_int'(R) = 0
J = 0
```

## Main Findings

This is a strong reduced consistency check. The same boundary-null profile that avoids value leakage also avoids the reduced derivative-jump shell diagnostic when matched to exterior zero.

So the reduced silent route can satisfy:

```text
zero exterior scalar value;
zero interior boundary value;
zero derivative mismatch;
zero reduced shell jump.
```

This is exactly the kind of constructive condition Group 56 was supposed to find.

## Boundary

The result is not a full junction theorem and not a proof of physical matching in the full geometric theory. It is a reduced shell-jump diagnostic.

It also does not prove source no-double-counting or covariant insertion.

## Steering Consequence

The reduced silent route now has boundary-null, charge-neutral, exterior-tail-zero, and no-shell pieces. The remaining constructive check is divergence silence.
