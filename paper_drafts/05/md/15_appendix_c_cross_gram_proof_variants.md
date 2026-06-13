# Appendix C. Cross-Gram Proof Variants

There are two equivalent ways to write the invertibility proof.

## Basis-change proof

Let `U = (u_1,...,u_N)` and `V = (v_1,...,v_N)` be two bases of the same
finite-dimensional space `H`.  Let `<.,.>` be positive definite on `H`.
Define

```text
A_ij = <u_i,v_j>.
```

If `G_ij = <u_i,u_j>` and `V = U T`, then

```text
A = G T.
```

Both `G` and `T` are invertible, so `A` is invertible.

## Annihilator proof

Suppose `A c = 0`.  Let

```text
v = sum_j c_j v_j.
```

Then

```text
<u_i,v> = 0
```

for every basis vector `u_i`, hence `<h,v> = 0` for every `h in H`.  Since
`v in H` and the pairing is positive definite, taking `h = v` gives

```text
<v,v> = 0,
```

so `v = 0`.  Because `V` is a basis, all `c_j = 0`.  Thus the nullspace is
trivial and `A` is invertible.

The annihilator proof is probably the cleanest version for the final paper.

