# Matter Source Origin Gate 22: Boundary Source As Thin-Shell Stress

## Purpose

This proof connects the reduced boundary-source representation to a stress
source limit.

It models a compact shell centered at `R` and asks what happens as its width
goes to zero.

## Validated Checks

- centered thin-shell stress coupling tends to M A(R): passed
- first centered finite-width correction is O(epsilon^2): passed
- variation of boundary source M A(R) gives source coefficient M: passed

## Taylor Model

Write:

```text
A(R+s) = A0 + A1 s + (1/2) A2 s^2.
```

A centered normalized shell has moments:

```text
mu0 = 1
mu1 = 0
mu2 = epsilon^2.
```

The source coupling is:

```text
M integral shell(s) A(R+s) ds
  =
  M [A0 + (1/2) A2 epsilon^2].
```

Taking the thin-shell limit:

```text
epsilon -> 0
```

gives:

```text
M A(R).
```

## Gate Interpretation

The boundary source term is not a separate kind of mass by itself. In this
reduced model it is the thin-shell limit of an ordinary stress/source coupling.
