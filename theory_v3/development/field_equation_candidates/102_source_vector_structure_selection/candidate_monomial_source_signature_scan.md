# candidate_monomial_source_signature_scan — Analysis Note

## Result

`candidate_monomial_source_signature_scan.py` scans:

```text
S_q(x)=x^(2q)
```

for:

```text
q=0..8
k=1..12.
```

Class counts:

```text
ALL_NEGATIVE:
  1

LEADING_POSITIVE_THEN_NEGATIVE:
  2

MULTI_OR_MIXED_FLIP_1:
  6
```

Detailed pattern:

```text
q=0:
  ALL_NEGATIVE

q=1,2:
  LEADING_POSITIVE_THEN_NEGATIVE

q=3:
  [+, +, -, -, ...]

q=4,5:
  [+, +, +, -, -, ...]

q=6:
  [+, +, +, +, -, ...]

q=7,8:
  [+, +, +, +, +, -, ...]
```

## Interpretation

This is a strong formal structure result.

Monomial sources shift weight toward the endpoint `x=1` as `q` increases. Since the row tests have moving roots, higher powers produce more leading positive source-vector entries before the eventual negative tail.

That means the monomial family has an ordered signature structure:

```text
larger q -> longer initial positive run.
```

This is not random. It says the source-vector signs are measuring how much the source profile lives above the row test root.

## What It Suggests

If a future boundary/source problem produces a source concentrated near larger `x`, its `b_k` may naturally show a leading-positive-then-negative signature.

If it produces a flatter or endpoint-suppressed source, it may produce all-negative signatures.

## What It Does Not Prove

No `q` is selected physically.

The leading-positive signature is not evidence of matter, curvature energy, exchange, or boundary behavior by itself.

## Carry-forward status

```text
MONOMIAL_SOURCE_SIGNATURES_CLASSIFIED
Q0_ALL_NEGATIVE
Q1_Q2_LEADING_POSITIVE_THEN_NEGATIVE
HIGHER_Q_EXTENDS_LEADING_POSITIVE_RUN
MONOMIAL_SOURCE_NOT_PHYSICALLY_SELECTED
```
