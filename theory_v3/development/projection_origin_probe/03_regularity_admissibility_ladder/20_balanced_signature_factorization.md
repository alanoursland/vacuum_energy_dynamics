# Synthesis Proof 20: Balanced Signature Factorization

## Purpose

This report factors the balanced source projection signatures.

Balanced sources are:

```text
B_(R,q) = a^R [x^(2q) - c_(R,q)].
```

The signature matrix is:

```text
P_R[k,q] = integral psi_k B_(R,q) a^4 dx.
```

## Validated Checks

- P_R = M_R T_R verified for R=0..4 N=2..5: passed
- balancing transform T_R has full column rank: passed
- balanced projection signatures have full tested rank: passed

## Factorization

Define the raw projection matrix:

```text
M_R[k,j] = integral psi_k x^(2j) a^(R+4) dx
```

with `j=0..N`, and define the balancing transform `T_R` by:

```text
T_R[:,q] = e_q - c_(R,q)e_0.
```

Then:

```text
P_R = M_R T_R.
```

This explains the balanced signatures as ordinary monomial projection rows
after a source-space balancing transform.

## Rank Data

```text
R=0, N=2: rank(M_R)=2, rank(T_R)=2, rank(P_R)=2
R=0, N=3: rank(M_R)=3, rank(T_R)=3, rank(P_R)=3
R=0, N=4: rank(M_R)=4, rank(T_R)=4, rank(P_R)=4
R=0, N=5: rank(M_R)=5, rank(T_R)=5, rank(P_R)=5
R=1, N=2: rank(M_R)=2, rank(T_R)=2, rank(P_R)=2
R=1, N=3: rank(M_R)=3, rank(T_R)=3, rank(P_R)=3
R=1, N=4: rank(M_R)=4, rank(T_R)=4, rank(P_R)=4
R=1, N=5: rank(M_R)=5, rank(T_R)=5, rank(P_R)=5
R=2, N=2: rank(M_R)=2, rank(T_R)=2, rank(P_R)=2
R=2, N=3: rank(M_R)=3, rank(T_R)=3, rank(P_R)=3
R=2, N=4: rank(M_R)=4, rank(T_R)=4, rank(P_R)=4
R=2, N=5: rank(M_R)=5, rank(T_R)=5, rank(P_R)=5
R=3, N=2: rank(M_R)=2, rank(T_R)=2, rank(P_R)=2
R=3, N=3: rank(M_R)=3, rank(T_R)=3, rank(P_R)=3
R=3, N=4: rank(M_R)=4, rank(T_R)=4, rank(P_R)=4
R=3, N=5: rank(M_R)=5, rank(T_R)=5, rank(P_R)=5
R=4, N=2: rank(M_R)=2, rank(T_R)=2, rank(P_R)=2
R=4, N=3: rank(M_R)=3, rank(T_R)=3, rank(P_R)=3
R=4, N=4: rank(M_R)=4, rank(T_R)=4, rank(P_R)=4
R=4, N=5: rank(M_R)=5, rank(T_R)=5, rank(P_R)=5
```

## Interpretation

The balanced projection signatures do not require a new projection mechanism.
They are the original moment/projection mechanism composed with the
admissibility balancing transform.
