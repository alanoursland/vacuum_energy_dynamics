# Synthesis Proof 9: Galerkin and Variational Matrix Test

## Purpose

This report compares three exact matrices:

```text
A[k,j] = 2 <psi_k, phi_j>_w
K[i,j] = <L phi_i, L phi_j>_w
P[i,j] = <phi_i, L*_w L phi_j>_w
```

The goal is to clarify whether the existing projection matrix is directly the
variational stiffness matrix.

## Validated Identities

- Galerkin stiffness identity on even monomial grid: passed
- projection matrix is not identical to stiffness matrix: passed
- psi-tested parent matrix is distinct from A: passed

## Result

The variational stiffness matrix is:

```text
K[i,j] = <L phi_i, L phi_j>_w.
```

SymPy verifies on the exact even-monomial grid that:

```text
<phi_i, L*_w L phi_j>_w = <L phi_i, L phi_j>_w.
```

The original projection matrix:

```text
A[k,j] = 2 <psi_k, phi_j>_w
```

is not the same matrix as `K`. For example:

```text
A[1,0] = -512/5775
K[0,0] = 512/385
```

Thus `A` is not directly the stiffness matrix of the candidate variational
problem. It is the once-integrated projection/pullback matrix associated with
the row tests `psi_k`.

## Exact Matrices

`A`, rows `k=1..5`, columns `j=0..4`:

```text
Matrix([[-512/5775, 512/225225, 512/225225, 512/425425, 512/799425], [-512/35035, -512/315315, -512/5360355, 512/4849845, 512/4849845], [-512/135135, -512/626535, -3584/18706545, -512/14549535, 512/91265265], [-512/401115, -512/1344915, -512/4103715, -1536/37182145, -512/42902475], [-1536/3002285, -11776/63047985, -512/6938295, -512/16900975, -5632/456326325]])
```

`K`, rows/columns `i,j=0..4`:

```text
Matrix([[512/385, -512/15015, -512/15015, -1536/85085, -512/53295], [-512/15015, 512/9009, 512/36465, 14848/4849845, 512/2078505], [-512/15015, 512/36465, 11776/1616615, 14848/4849845, 45568/37182145], [-1536/85085, 14848/4849845, 14848/4849845, 66048/37182145, 15872/16900975], [-512/53295, 512/2078505, 45568/37182145, 15872/16900975, 20992/35102025]])
```

`Q[k,j] = <psi_k, L*_w L phi_j>_w`, rows `k=1..5`, columns `j=0..4`:

```text
Matrix([[-2048/6825, 2048/32175, 2048/98175, 161792/24249225, 2048/944775], [-2048/105105, -6144/595595, 2048/1616615, 59392/33948915, 124928/111546435], [2048/2297295, -206848/43648605, -2048/2078505, 75776/1003917915, 432128/1673196525], [14336/7621185, -2048/1203345, -886784/1227010785, -391168/2045017975, 2048/5019589575], [2048/1616615, -288768/483367885, -190464/483367885, -333824/1977414075, -2048/38357865]])
```
