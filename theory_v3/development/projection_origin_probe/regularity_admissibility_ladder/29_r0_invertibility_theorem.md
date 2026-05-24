# Synthesis Proof 29: R=0 Invertibility Mechanism

## Purpose

This report isolates why the original balanced projection signatures are
invertible in the first-admissibility class.

## Validated Checks

- psi and balanced rows both span first-admissibility kernel for N=1..8: passed
- R=0 cross Gram determinants are nonzero for N=1..8: passed

## Mechanism

In `y=x^2`, the original row functions are:

```text
psi_k(y) = y^k - ((2k-1)/(2k+3))y^(k-1).
```

The first balanced source basis is:

```text
B_q(y) = y^q - 3/((2q+1)(2q+3)).
```

Both families span the same finite coefficient-space kernel:

```text
ker[S -> integral_0^1 aS dx].
```

The projection matrix is their cross Gram matrix under the positive weight:

```text
(1-y)^4 y^(-1/2).
```

Because a positive inner product is nondegenerate on this finite kernel, the
cross Gram matrix between two bases of the same kernel is invertible.

## Determinant Evidence

```text
N=1: det=2048/102375
N=2: det=33554432/3250385263125
N=3: det=367236883677184/1787196634497004909303125
N=4: det=133738894534394249216/715473949204550189002209500405390625
N=5: det=20735495658030119604560330752/2435603035041807932447721615090759184287462041015625
N=6: det=12850145495751201086813441779377696145408/626099760844289372031754225411402138240938611626999171162628133544921875
N=7: det=29615389623648667531959433866077024079941992448/10900357821209564796361887348087832420430523477433627706776217147086062871780250244140625
N=8: det=407119479715992417645766150936724927457264556622617792433094656/20093486765330534647955389178089780026776004348824728408909131063709965022763780642053495241287621416579437255859375
```

## Interpretation

This gives a conceptual invertibility proof for the `R=0` balanced source
class. The original `psi_k` rows are exactly adapted to the first
admissibility condition.
