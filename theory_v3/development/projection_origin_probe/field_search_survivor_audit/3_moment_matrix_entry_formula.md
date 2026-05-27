# Field Search Survivor Audit 3: Moment Matrix Entry Formula

## Purpose

This report reconstructs the explicit matrix-entry formula from the weighted
projection integral.

## Validated Checks

- closed matrix entry formula: passed
- closed formula determinants positive through N=6: passed
- leading pivot ratios positive through N=6: passed

## Weighted Moment

The base moment is:

```text
M(s) = 2 integral_0^1 x^(2s)(1-x^2)^4 dx
     = 768 / [(2s+1)(2s+3)(2s+5)(2s+7)(2s+9)].
```

The projection entry is:

```text
A[k,j] = M(j+k) - r_k M(j+k-1).
```

with:

```text
r_k = (2k-1)/(2k+3).
```

## Closed Formula

SymPy verifies:

```text
A[k,j] =
1536(4j - 6k + 3)
/
[
(2k+3)
(2j+2k-1)
(2j+2k+1)
(2j+2k+3)
(2j+2k+5)
(2j+2k+7)
(2j+2k+9)
].
```

## Determinant Check

Using the closed formula, the leading determinants are positive through `N=6`:

```text
N=1: det=512/225225
N=2: det=4194304/1207285954875
N=3: det=137438953472/17020920328542903898125
N=4: det=4719772409484279808/136900210194117395471418441203109375
N=5: det=604462909807314587353088/4704128406008153848883378410764703053235857421875
N=6: det=101898825848745992209910990460944384/41698285770515442692757524169923552330398841933200077999509033203125
```

## Interpretation

This is the archived determinant/moment result in compact form. It supports the
projection hierarchy as a real moment-pairing object, while preserving the
boundary that finite determinant checks are not an all-order theorem.
