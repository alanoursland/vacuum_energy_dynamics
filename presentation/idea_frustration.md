# Why can't regular tetrahedra fill space — and what happens when they can't?

The packing model's founding fact: regular tetrahedra tile flat 3-space with a leftover gap at every edge, and that leftover gap, not zero, is where the vacuum's floor and gravity's coupling both come from.

## The idea

Take the theory owner's original picture literally: space is a graph of "bits" — vertices connected by edges with lengths $l_e$ — glued into piecewise-flat simplices, with all geometric content living in those edge lengths (this is Regge calculus, not a new formalism, just a new ground state for it). Curvature isn't smeared over a manifold; it's concentrated entirely on hinges, as deficit angles:

```text
delta_h = 2*pi - (sum of dihedral angles meeting at hinge h)
```

Now try to pack regular tetrahedra around a shared edge in flat space. Five of them almost close the gap — five dihedral angles of $\arccos(1/3) \approx 70.53°$ sum to $\approx 352.6°$, not $360°$. The shortfall is exact and irreducible:

```text
Delta_0 = 2*pi - 5*arccos(1/3)   (exact, derivation 037)
```

This is **geometric frustration**: no rearrangement of regular tetrahedra removes the gap. You can spend energy curving the packing to relieve it locally, but derivation 037 shows curving costs more than it saves at any sub-packing scale — so the minimum-energy configuration is the flat one, sitting at deficit $\Delta_0$ at *every* hinge, not at deficit zero. The ground state is frustrated by construction, not by accident.

Why this matters is entirely in what a frustrated ground state does to the energy functional. Give every hinge a smooth per-wedge energy $f(\delta_h)$ (weighted by hinge measure $V_h$) and expand about the true minimum $\Delta_0$:

```text
E = sum_h V_h f(Delta_0)                          <- floor (constant, sequestered)
  + f'(Delta_0) sum_h V_h (delta_h - Delta_0)      <- linear: Regge action -> Einstein-Hilbert
  + (1/2) f''(Delta_0) sum_h V_h (delta_h-Delta_0)^2  <- R^2-class, Planck-suppressed
```

Because $\Delta_0 \neq 0$, the linear term's coefficient $f'(\Delta_0)$ is generically nonzero — the leading response to bending the packing away from flat is *linear* in the deficit, which is exactly the Regge-calculus form of the Einstein-Hilbert action. An unfrustrated packing (one whose ground state actually sits at $\delta = 0$) would have $f'(0) = 0$ by definition of being a minimum, and its leading response would be curvature-squared — a fundamentally different (and much weaker, higher-derivative) theory of gravity.

So frustration is not a curiosity about tetrahedra. It's the reason the constant term (a fixed, nonzero floor of wedge energy) and the linear term (Einstein-Hilbert gravity) are forced to coexist in the same expansion, with the *same* stiffness $f'(\Delta_0)$ setting both. One frustrated ground state, two readings: the vacuum's substance density and the strength of gravity.

Sanity check at the other end of the scale: triangulating the unit 3-sphere with the 600-cell (720 edges, five flat tetrahedra per edge, every hinge sitting at exactly $\Delta_0$) reproduces the Einstein-Hilbert action to within 3.5% at the coarsest possible mesh — the same $\Delta_0$ that seeds the floor also seeds curvature globally.

**Proof:** derivation 037 (exact irreducibility of $\Delta_0$, relief-costs-more-than-it-saves), derivation 039 (expansion-point theorem, 600-cell check, floor–Newton lock) → [../theory_v3/development/vacuum_sector/08_packing_microphysics/regge_delaunay_model.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/regge_delaunay_model.md)

**Where next:**
- [The Packing Model →](idea_packing.md) — the full axiomatic statement: graph, flat cells, per-hinge energy, frustrated ground state, stated as a candidate strain axiom.
- [The Floor →](idea_floor.md) — what the constant term $\sum_h V_h f(\Delta_0)$ actually means as the vacuum's substance energy.
- [Hinge Deficit and Curvature →](idea_deficit_angle.md) — Regge's insight in its own right: how a piecewise-flat complex stores geometry in angle gaps.
- [Flatness Is Bought →](idea_flatness_is_bought.md) — the campaign-wide theme this node instantiates: zero curvature isn't free, and frustration is the receipt.
