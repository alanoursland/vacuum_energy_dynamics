# candidate_moment_ratio_identity — Analysis Note

## Result

`candidate_moment_ratio_identity.py` derives the integration-by-parts identity behind the hierarchy.

After two integrations by parts, the kernel check gives:

```text
kernel difference = 0
```

The reduced moment-ratio identity is:

```text
M_(2k)=0
iff
I_k = r_k I_(k-1)
```

where:

```text
r_k = (2k - 1)/(2k + 3)
```

and:

```text
I_k(P) = ∫_0^1 t^(k-1/2)(1-t)^4 P(t) dt.
```

## Interpretation

This is the core structural result of Group 88.

Before this script, the hierarchy was expressed as many separate constraints:

```text
M2 = 0;
M4 = 0;
...
M(2N) = 0.
```

This script shows those constraints share a common form:

```text
successive weighted t-moments must obey a fixed ratio.
```

That is a real simplification. It changes the hierarchy from a black-box sequence of integrals into a moment-ratio problem.

The key insight is that the exactness operator and compact-support envelope convert the payload suppression condition into a relation among `I_k(P)` moments. That is the doorway to a general coefficient formula.

## What Changed

The hierarchy is no longer just:

```text
solve M2..M(2N) directly.
```

It is now:

```text
choose P_N so its Beta-weighted moment sequence satisfies
I_k/I_(k-1) = (2k-1)/(2k+3)
for k=1..N.
```

That is a sharper and more reusable statement.

## What Did Not Change

This does not prove the hierarchy exists for all `N`. It only rewrites the condition. Existence and uniqueness still depend on the linear system being invertible.

## Steering Consequence

The next correct move is to express the `I_k(P_N)` moments as Beta sums. That is what the next script does.
