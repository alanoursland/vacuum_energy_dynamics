# Matter Source Origin Gate 10: Boundary Point Source Equivalence

## Purpose

This proof checks the reduced boundary-source version of the A-sector mass
coupling.

It is useful because the broader ontology often treats matter as a boundary or
constraint on the vacuum rather than as an arbitrary bulk field.

## Validated Checks

- boundary coupling fixes exterior derivative jump: passed
- regular interior gives exterior flux F_A=q/K: passed
- q=K*8*pi*G*M/c^2 reproduces the A-sector mass flux: passed

## Interface Variation

For two radial bulk regions joined at `R`, with source coupling:

```text
E_boundary = + q A(R),
```

the interface variation coefficient is:

```text
4*pi*K*R^2 (A'_in - A'_ext) + q.
```

Stationarity gives:

```text
A'_ext = A'_in + q/(4*pi*K*R^2).
```

If the interior is regular with:

```text
A'_in = 0,
```

then:

```text
F_A = 4*pi*R^2 A'_ext = q/K.
```

Choosing:

```text
q = K * 8*pi*G*M/c^2
```

reproduces:

```text
F_A = 8*pi*G*M/c^2.
```

## Gate Interpretation

This proves a reduced equivalence between ordinary A-sector mass flux and a
boundary source coupling. It does not yet derive the boundary coupling from a
covariant matter action.
