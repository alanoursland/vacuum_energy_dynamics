# 4. Compactification endpoint gate

This script checks a basic compactification:

```text
x = r/(r + L).
```

Its inverse is

```text
r = L x/(1 - x),
```

and spatial infinity maps to the endpoint:

```text
lim_(r->oo) x = 1.
```

SymPy also verifies the inverse map:

```text
r(x)/(r(x)+L) = x
```

Conclusion: a boundary endpoint can represent compactified infinity. The
endpoint is an analysis representative of an asymptotic regime, not necessarily
a material wall or fundamental physical substance.
