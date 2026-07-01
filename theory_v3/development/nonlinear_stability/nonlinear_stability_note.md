# Nonlinear Stability — Scoped Closure

## The Debt

Proof.md §3 established the sector signature at reduced/quadratic
level: the negative static configuration energy lives in an
elliptic/constraint sector (Theorem 2), is bound to its sources
(Theorem 3), and the propagating sector is positive (Theorem 4). The
debt was nonlinear: could strong fields open a channel — decay, mining,
or instability — that the quadratic analysis misses?

## In-House Results

### 1. Nonlinear source binding (Theorem 3 lifted)

The 019 Birkhoff family is the *complete* spherical vacuum sector at
full nonlinearity: $B = r/(C_1+r)$, $A = 1/B$. Its Kretschmann scalar
is

$$
K = \frac{12\,C_1^2}{r^6},
$$

which diverges at the center for every $C_1 \neq 0$. A regular center
therefore forces $C_1 = 0$: **flat is the unique source-free regular
spherical state, nonlinearly.** The negative reservoir supports no
free-standing configuration to decay into; it exists only as a
functional of its sources. This is Theorem 3 with the weak-field
restriction removed.

### 2. No mining (Misner–Sharp positivity)

For any spherical configuration with
$B = (1 - 2Gm(r)/c^2 r)^{-1}$ and arbitrary $A(r)$,

$$
G^t{}_t = -\frac{2G}{c^2}\frac{m'(r)}{r^2}
\qquad\text{identically},
$$

so the closed parent gives $m'(r) = (4\pi r^2/c^2)\,\rho$ — exact, no
weak-field expansion. For $\rho \ge 0$ and a regular center
($m(0)=0$),

$$
m(r) = \frac{4\pi}{c^2}\int_0^r \rho\, r'^2\,dr' \;\ge\; 0
\quad\text{for all } r .
$$

The negative configuration energy
$u_{\rm field} = -c^4 (s')^2/8\pi G$ is already bookkept inside $m$
(the exterior mass is the matter integral minus binding); no
arrangement of sources, however strong, drives a quasilocal mass
negative. **There is no nonlinear channel that extracts unbounded
energy from the static sector.**

### 3. Sector signature at quadratic order (inherited)

TT energy density is a positive sum of squares (G03, re-verified);
the scalar sector is constraint-type (ghost exclusion, G03); the
vector sector is constraint-type through general linear time
dependence (017). Combined with 1–2, every sector in which the
framework claims theorem grade is stable at its claimed level.

## The External Anchor (recorded honestly)

What remains is the global, nonspherical, small-data statement:
Minkowski-asymptotic data close to flat evolve globally and disperse.
For the equations the 018 closure fixed (Einstein–Hilbert response,
$\Lambda$ admitted, GB inert), this is:

- Christodoulou & Klainerman (1993), *The Global Nonlinear Stability
  of the Minkowski Space*;
- Lindblad & Rodnianski (2010), harmonic-gauge proof.

**Import class.** These are theorems of PDE analysis about a specific
hyperbolic system; their statements and proofs take no gravitational
phenomenology as input. This is the same import class as Fierz–Pauli
1939 in proof.md §4.1: mathematics about the derived equations, not
GR's physical content. No coefficient, no equation, and no falsifier
of the framework depends on this import; it upgrades confidence in the
flat state's global basin, nothing else.

**Honest boundary.** An in-house re-derivation at
Christodoulou–Klainerman scale is declared out of scope by decision.
The in-house content of this closure is §§1–3 above. If the theory
owner later wants the import retired the way 018 retired Deser, that
is a new program, not a hidden debt: it is recorded here, visibly.

## What This Retires

This retires the "nonlinear stability" rigor debt of
`04_field_equations/06_rigor_closures.md` at scoped level. It moves no
coefficient and changes no equation.

## Verification

```text
vacuum_forge/src/field_equation_trials/020_nonlinear_stability/nonlinear_stability_scoped.py
```

Archive records: `nonlinear_source_binding_020`,
`misner_sharp_no_mining_020`, `global_stability_external_anchor_020`;
declared dependencies on `covariant_statics_lift_019`,
`tt_positivity_sum_of_squares_g03`, `ghost_exclusion_g03`,
`vector_time_dependent_lift_017`.

## References

Christodoulou, D., & Klainerman, S. (1993). *The Global Nonlinear
Stability of the Minkowski Space*. Princeton University Press.

Lindblad, H., & Rodnianski, I. (2010). The global stability of
Minkowski space-time in harmonic gauge. *Annals of Mathematics*,
171(3), 1401–1477.
