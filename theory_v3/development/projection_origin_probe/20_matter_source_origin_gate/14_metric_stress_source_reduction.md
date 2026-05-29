# Matter Source Origin Gate 14: Metric Stress Source Reduction

## Purpose

This proof checks the local metric-coupling source reduction behind the
A-sector matter law.

It does not derive the gravitational coupling constant. It verifies the source
type: nonrelativistic matter enters the weak metric through mass-energy density.

## Validated Checks

- metric matter variation is proportional to rho c^2 in the A component: passed
- standard 8*pi/c^4 coupling maps T00=rho c^2 to 8*pi*rho/c^2: passed

## A-Sector Variation

In the static weak sector:

```text
g_00 = -A
delta g_00 = -delta A.
```

For nonrelativistic matter:

```text
T^00 approximately rho c^2.
```

The standard metric variation has the local form:

```text
delta S_m = (1/2) T^00 delta g_00.
```

Therefore:

```text
delta S_m = -(1/2) rho c^2 delta A.
```

So the A-component source is proportional to ordinary mass density.

## Normalization Proxy

With the standard geometric coupling scale:

```text
kappa = 8*pi/c^4
```

the stress source maps as:

```text
kappa T^00 = 8*pi rho/c^2.
```

Restoring `G` gives the coefficient used earlier:

```text
8*pi*G*rho/c^2.
```

## Gate Interpretation

This is the covariant source-type bridge. The A-sector source is not an
arbitrary scalar; it is the weak static reduction of metric coupling to
stress-energy.
