# Synthesis Proof 18: Projection vs. Admissibility Row Spaces

## Purpose

This report tests the proposed bridge:

```text
Are the psi_k projection rows equivalent to the endpoint-contact/admissibility rows?
```

The comparison is finite-dimensional, on even polynomial source spaces:

```text
S(x) = sum_j c_j x^(2j).
```

## Validated Checks

- degree 2: projection and full admissibility row spaces both full rank: passed
- degree 3: projection and full admissibility row spaces both full rank: passed
- degree 4: projection and full admissibility row spaces both full rank: passed
- degree 5: projection and full admissibility row spaces both full rank: passed
- degree 6: projection and full admissibility row spaces both full rank: passed
- degree 7: projection and full admissibility row spaces both full rank: passed
- degree 8: projection and full admissibility row spaces both full rank: passed
- low-order endpoint-contact ladders are not equal to full projection rowspace: passed
- kernel dimensions distinguish projection rows from finite contact ladders: passed

## Row Families

Projection rows:

```text
P_k[S] = integral_0^1 psi_k(x) S(x) a^4 dx.
```

Admissibility rows:

```text
C_0[S] = integral_0^1 aS dx
C_1[S] = S(1)
C_2[S] = S'(1)
C_3[S] = S''(1)
...
```

where the endpoint-contact ladder uses:

```text
R contact level:
  integral aS = 0
  S vanishes to order R at x=1.
```

## Result

The projection rows are full rank on the tested even polynomial truncations.
The full admissibility row family is also full rank once enough endpoint
derivatives are included.

But the low-order endpoint-contact ladders are not equal to the projection rowspace.
They have smaller rank and larger nullspaces.

Exact row-space data:

```text
degree=2: P_rank=3, full_adm_rank=3, C0 row in P rowspace? True, ladder=[(0, 1, True, False), (1, 2, True, False)]
degree=3: P_rank=4, full_adm_rank=4, C0 row in P rowspace? True, ladder=[(0, 1, True, False), (1, 2, True, False), (2, 3, True, False)]
degree=4: P_rank=5, full_adm_rank=5, C0 row in P rowspace? True, ladder=[(0, 1, True, False), (1, 2, True, False), (2, 3, True, False), (3, 4, True, False)]
degree=5: P_rank=6, full_adm_rank=6, C0 row in P rowspace? True, ladder=[(0, 1, True, False), (1, 2, True, False), (2, 3, True, False), (3, 4, True, False), (4, 5, True, False)]
degree=6: P_rank=7, full_adm_rank=7, C0 row in P rowspace? True, ladder=[(0, 1, True, False), (1, 2, True, False), (2, 3, True, False), (3, 4, True, False), (4, 5, True, False)]
degree=7: P_rank=8, full_adm_rank=8, C0 row in P rowspace? True, ladder=[(0, 1, True, False), (1, 2, True, False), (2, 3, True, False), (3, 4, True, False), (4, 5, True, False)]
degree=8: P_rank=9, full_adm_rank=9, C0 row in P rowspace? True, ladder=[(0, 1, True, False), (1, 2, True, False), (2, 3, True, False), (3, 4, True, False), (4, 5, True, False)]
```

Kernel comparison on degree 6:

```text
projection nullity on degree 6: 0
R=0 contact/admissibility nullity on degree 6: 6
R=1 contact/admissibility nullity on degree 6: 5
R=2 contact/admissibility nullity on degree 6: 4
R=3 contact/admissibility nullity on degree 6: 3
R=4 contact/admissibility nullity on degree 6: 2
R=5 contact/admissibility nullity on degree 6: 1
```

## Interpretation

This is a partial negative result for the strongest bridge claim.

The `psi_k` hierarchy is not simply the same rowspace as the low-order
endpoint-contact/admissibility ladder:

```text
integral aS = 0,
S(1)=0,
S'(1)=0,
...
```

on finite even polynomial source spaces.

Instead:

```text
projection rows:
  full-rank moment diagnostics on the tested source space

admissibility rows:
  lower-rank boundary/contact constraints until the full derivative tower is
  included
```

So the projection hierarchy is adjacent to the admissibility problem, and it
resolves admissible balanced source spaces, but it is not identical to the
low-order endpoint-contact ladder.
