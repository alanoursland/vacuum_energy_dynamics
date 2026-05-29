# 19. Closure dependency table

This folder separates two inputs:

```text
L = local traceless tensor data,
T = transport / constraint law.
```

A schematic closure flag is

```text
closure = L T.
```

Validated checks:

```text
L=0 -> no Weyl dynamics
T=0 -> no Weyl dynamics
L=T=1 -> closure flag present
```

Result: local tensor probes and transport closure are both required.
