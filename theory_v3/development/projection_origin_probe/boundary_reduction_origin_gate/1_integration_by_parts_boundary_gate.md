# 1. Integration by parts boundary gate

This script checks the algebraic origin of a boundary term.

For smooth functions `f` and `g`,

```text
(f g)' = f' g + f g'
```

so

```text
f' g = (f g)' - f g'.
```

After integration over an interval, the total derivative becomes endpoint data.
This is the smallest model of the boundary-reduction idea: the boundary term is
created by rewriting a bulk derivative, not by declaring the boundary to be the
underlying physics.

SymPy check:

```text
(f*g)' - f'*g - f*g' = 0
```

Conclusion: boundary terms are produced by bulk differential identities.
