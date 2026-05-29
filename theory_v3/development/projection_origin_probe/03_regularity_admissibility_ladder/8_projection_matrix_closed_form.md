# Synthesis Proof 8: Projection Matrix Closed Form

## Purpose

This report validates exact closed forms for:

```text
A[k,j] = 2 integral_0^1 psi_k(x) x^(2j) a^4 dx
```

and for the IBP pullback expression:

```text
A[k,j] = 2/(2k+3) integral_0^1 x^(2k-1) a^4 L[x^(2j)] dx.
```

## Validated Identities

- closed form factored source signature: passed
- projection matrix pullback closed form: passed
- direct finite matrix grid K=1..6 J=0..5: passed

## Closed Form

Let:

```text
M(n,p) = integral_0^1 x^n (1-x^2)^p dx.
```

Then:

```text
A[k,j] = 2[M(2k+2j,4) - r_k M(2k+2j-2,4)].
```

Equivalently:

```text
A[k,j]
  = 2 M(2k+2j-2,4)
    [ (k+j-1/2)/(k+j+9/2) - (2k-1)/(2k+3) ].
```

The pullback form uses:

```text
L[x^(2j)] = 2j x^(2j-1) - (2j+6)x^(2j+1).
```

## Sample Exact Matrix

Rows are `k=1..6`; columns are `j=0..5`.

```text
[-512/5775, 512/225225, 512/225225, 512/425425, 512/799425, 512/1426425]
[-512/35035, -512/315315, -512/5360355, 512/4849845, 512/4849845, 5632/70984095]
[-512/135135, -512/626535, -3584/18706545, -512/14549535, 512/91265265, 512/35102025]
[-512/401115, -512/1344915, -512/4103715, -1536/37182145, -512/42902475, -512/386122275]
[-1536/3002285, -11776/63047985, -512/6938295, -512/16900975, -5632/456326325, -512/111205575]
[-512/2204475, -14848/152108775, -512/11700675, -512/25072875, -8704/898198875, -6656/1465482375]
```
