# 6. Trace-free tidal vacuum witness

Take

```text
Phi = a (x^2-y^2)/2.
```

Then

```text
Delta Phi = 0
```

but the Hessian is nonzero:

```text
H = Matrix([
[a,  0, 0],
[0, -a, 0],
[0,  0, 0]]).
```

So a vacuum scalar trace equation can have nonzero trace-free tidal data.

This is the Newtonian analogue of the Ricci/Weyl separation:

```text
trace/source channel can vanish while tidal/free data remains.
```
