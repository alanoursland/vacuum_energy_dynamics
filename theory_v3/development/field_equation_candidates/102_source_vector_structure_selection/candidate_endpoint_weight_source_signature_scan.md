# candidate_endpoint_weight_source_signature_scan — Analysis Note

## Result

`candidate_endpoint_weight_source_signature_scan.py` scans:

```text
S_p(x)=(1-x^2)^p
```

for:

```text
p=0..6
k=1..12.
```

The result is uniform:

```text
endpoint class counts:
  {'ALL_NEGATIVE': 7}
```

Every tested endpoint-weight source has the sign pattern:

```text
[-, -, -, -, -, -, -, -, -, -, -, -].
```

## Interpretation

This is one of the cleanest results in Group 102.

Endpoint-weighted sources suppress the region near `x=1` and concentrate weight closer to the low/interior part of the interval. Against the row tests:

```text
psi_k(x)=x^(2k-2)(x^2-r_k),
```

that produces all-negative source projections through the tested range.

So endpoint-weight profiles form a clean formal class:

```text
S=(1-x^2)^p -> ALL_NEGATIVE.
```

This includes `p=0`, the constant source, which is also all-negative.

## What It Suggests

If a future boundary/source derivation wants an all-negative right-hand side, endpoint-weight families are natural candidates.

But this is only a formal compatibility clue.

## What It Does Not Prove

No `p` is selected physically.

All-negative signature does not imply physical source correctness.

## Carry-forward status

```text
ENDPOINT_WEIGHT_SOURCE_SIGNATURES_CLASSIFIED
ENDPOINT_WEIGHT_FAMILY_ALL_NEGATIVE_P0_TO_P6
ALL_NEGATIVE_FORMAL_SOURCE_CLASS_IDENTIFIED
ENDPOINT_SOURCE_NOT_PHYSICALLY_SELECTED
```
