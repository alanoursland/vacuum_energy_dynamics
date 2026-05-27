# Field Search Survivor Audit 4: Source Signature Endpoint Formula

## Purpose

This report reconstructs the source-family signature formula from the archived
boundary-condition trend analysis.

For:

```text
S_pq(x) = x^(2q)(1-x^2)^p,
```

the goal is to record what is formal mathematics and what remains physical
interpretation.

## Validated Checks

- source-family sign numerator: passed
- balanced p=q sign expression: passed
- endpoint-concentrated q=p+2 sign expression: passed
- origin order: passed
- endpoint order: passed
- effective endpoint order under projection weight: passed
- low-q source sign expression: passed

## Endpoint Orders

The formal endpoint orders are:

```text
origin order at x=0: 2q
endpoint order at x=1: p
effective endpoint order under w=(1-x^2)^4: p+4.
```

So `q` controls origin suppression / endpoint concentration, while `p` controls
endpoint suppression.

## Sign Formula

For the projected source vector component, the sign-relevant beta-ratio
difference has numerator:

```text
(2k+2q-1)(2k+3)
  - (2k-1)(2k+2q+2p+9).
```

SymPy verifies this equals:

```text
-2(2kp + 6k - p - 4q - 3).
```

This is the formula behind the endpoint-signature trends.

## Interpretation

The source signatures are not arbitrary. They track endpoint suppression versus
endpoint concentration.

But this does not select a physical source law. It is a formal boundary/domain
trend until a physical boundary or source principle is supplied.
