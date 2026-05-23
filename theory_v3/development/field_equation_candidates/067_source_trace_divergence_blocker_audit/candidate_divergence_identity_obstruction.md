# candidate_divergence_identity_obstruction — Result Note

## Result

The script derives a reduced divergence-balance obstruction.

Count divergence:

```text
D_count =
D_res*i_res
+ D_source*(i_A + i_src_extra - 1)
+ D_trace*(i_B + i_res + i_trace_extra - 1)
```

Parent divergence balance:

```text
D_parent =
D_O
+ D_boundary
+ D_lift
+ D_repair
+ D_res*i_res
+ D_source*(i_A + i_src_extra - 1)
+ D_trace*(i_B + i_res + i_trace_extra - 1)
```

In the strict incidence state:

```text
D_count(strict) = 0
```

but:

```text
D_parent(strict) = D_O + D_boundary + D_lift + D_repair
```

The forced repair choice would be:

```text
D_repair = -D_O - D_boundary - D_lift
```

and is rejected.

## Main Findings

This is the strongest Group 67 result.

Strict count-once incidence removes the count residual contribution, but it does not prove a parent divergence identity.

Remaining burdens:

```text
boundary divergence burden;
covariant lift burden;
active O decision burden;
repair-current burden.
```

The script correctly rejects:

```text
count-once equals divergence;
forced repair current;
reduced balance as covariant identity.
```

So Group 67 makes progress but does not overclaim.

## Boundary

This is a reduced balance obstruction, not a covariant conservation theorem.

## Steering Consequence

Proceed to conservation dependencies. The next script should record what a real parent divergence identity still requires.
