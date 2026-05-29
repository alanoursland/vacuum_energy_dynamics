# Quadratic Response Selector 14: Null-Cone Instability Witness

## Purpose

This proof shows that a nonquadratic correction can move or thicken the null
condition relative to a fixed metric cone.

## Computation

Start with the 1+1 metric branch:

```text
Q_lor = -t^2 + x^2.
```

Add a quartic directional correction:

```text
Q = Q_lor + eps (t^2+x^2)^2.
```

On the original metric null line `x=t`, SymPy finds:

```text
Q(t,t) = 4*eps*t**4
```

## Interpretation

Unless `eps=0`, the original null cone is no longer a universal zero set of
the response. Nonquadratic response therefore threatens the shared causal cone
unless routed as a separate medium/Finsler correction.
