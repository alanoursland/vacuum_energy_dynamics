# 3. Local Response vs. Strain Dynamics

The most important structural distinction in the project is now this:

```text
local response is not the same as strain dynamics.
```

## Local response

A local directional interval-response object can be written schematically as:

```text
Q_p(v).
```

If it satisfies the parallelogram/quadratic gate, polarization reconstructs a symmetric bilinear form:

```text
g_p(u,v) = ( Q_p(u+v) - Q_p(u) - Q_p(v) ) / 2.
```

This is a local result. It lives at one point.

It explains how metric data can appear from local reciprocal interval response.

## Strain dynamics

Field equations require a relation between nearby points.

That means the theory needs to know how the configuration changes across a neighborhood:

```text
X(p), X(p + dp), ∇X, ∇∇X, ...
```

The energy cost of those differences is the strain functional.

This strain functional determines:

```text
transport law
connection dynamics
curvature
wave propagation
radiative degrees of freedom
constraint evolution
field equations
possible deviations from GR.
```

## Localization result

The proof chain has repeatedly derived local structures and imported strain/transport structures.

That pattern is not just a weakness. It is evidence that the ontology's remaining freedom has been localized. The same missing object explains why transport, field equations, radiation, and `ε` have not yet been generated directly:

```text
K_strain.
```
