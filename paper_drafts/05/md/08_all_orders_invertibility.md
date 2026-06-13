# 8. All-Orders Invertibility Theorem

The finite-order statement can be written as follows.

**Theorem.** Fix `R >= 0` and `N >= 1`.  Suppose the row family

```text
chi_{R,1}, ..., chi_{R,N}
```

and the balanced family

```text
B_{R,1}, ..., B_{R,N}
```

are bases of the same admissible polynomial space `H_{R,N}`, and suppose
`W_R` is positive almost everywhere on `(0,1)`.  Then the cross-Gram matrix

```text
A^{(R,N)}_{kq}
  = int_0^1 chi_{R,k}(y)B_{R,q}(y)W_R(y) dy
```

is invertible.

**Proof.** Let `G_U` be the self-Gram matrix of the row basis under
`<.,.>_R`.  Since `W_R` is positive on `(0,1)`, this pairing is positive
definite on finite polynomial subspaces, so `G_U` is invertible.  Since the
balanced family is another basis of the same space, there is an invertible
matrix `T` such that

```text
[B_{R,1} ... B_{R,N}] = [chi_{R,1} ... chi_{R,N}] T.
```

Taking pairings with the row basis gives

```text
A = G_U T.
```

Both factors are invertible, hence `A` is invertible.  This proves the claim.

The remaining manuscript-level work is to choose the cleanest standalone
definition of `H_{R,N}` and to make the basis-equivalence lemma independent
of the exploratory notation used in the discovery scripts.  The determinant
checks are then verification artifacts rather than load-bearing proof steps.

