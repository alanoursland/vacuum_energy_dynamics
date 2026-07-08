# Why would the Einstein-Hilbert term be the first term?

This is a conditional theorem inside the [packing model](idea_packing.md):
if the vacuum ground state is the frustrated Regge/Delaunay state described
in [`regge_delaunay_model.md`](../theory_v3/development/vacuum_sector/08_packing_microphysics/regge_delaunay_model.md),
then the leading curvature response is linear in deficit angle.

The only unusual input is the expansion point.  A regular tetrahedral
packing cannot close around an edge; five tetrahedra leave

```text
Delta_0 = 2*pi - 5*arccos(1/3) = 0.128389... rad .
```

That number is the [irreducible frustration angle](num_delta0.md), not a
fit parameter.  The exact relief calculation in
[`relief_exact_geometry_vacuumforge.md`](../theory_v3/development/vacuum_sector/relief_exact_geometry_vacuumforge.md)
also checks that curving the packing to relieve the gap does not produce a
small relaxed ground state.

Now put a smooth wedge energy on each hinge:

```text
E = sum_h V_h f(delta_h).
```

Expanding around the actual ground state, not around zero curvature, gives

```text
E = sum_h V_h f(Delta_0)
  + f'(Delta_0) sum_h V_h (delta_h - Delta_0)
  + 1/2 f''(Delta_0) sum_h V_h (delta_h - Delta_0)^2 + ...
```

The first term is the [constant floor](idea_floor.md).  The second term is
the Regge action, hence the discrete version of Einstein-Hilbert; this is
the theorem verified in
[`regge_delaunay_bridge_vacuumforge.md`](../theory_v3/development/vacuum_sector/08_packing_microphysics/regge_delaunay_bridge_vacuumforge.md)
and its forge script
[`039_regge_delaunay_bridge.py`](../vacuum_forge/src/vacuum_sector/039_regge_delaunay_bridge/regge_delaunay_bridge.py).

The point is simple but easy to miss: if the ground state were
unfrustrated, it would sit at `delta = 0`, and ordinary calculus would
force `f'(0) = 0`.  The linear term would vanish and the first surviving
response would be curvature-squared.  Because the proposed ground state
sits at `Delta_0 != 0`, no such cancellation is forced; generically
`f'(Delta_0)` survives.

So the claim is not "we prefer Einstein-Hilbert."  It is narrower:
[geometric frustration](idea_frustration.md) makes the Einstein-Hilbert
term the generic first response of this discrete energy.  The same source
also gives the [600-cell check](num_600cell_anchor.md): at the coarsest
triangulation of `S^3`, the Regge sum lands within 3.5% of the continuum
Einstein-Hilbert integral.

The same slope does double duty.  The zeroth-order term prices the
[floor](idea_floor.md) and the first-order term prices gravity, so one
wedge-energy slope sets both:

```text
rho_v = (c_e * Delta_0 / (2 * a^3)) * f'(Delta_0).
```

This is the floor-Newton lock of derivation 039: the vacuum's substance
density and the strength of gravity are two readings of `f'(Delta_0)`.

Scope matters.  This is exact discrete geometry plus a Taylor expansion;
it is not yet the [continuum-limit theorem](thm_continuum_convergence.md),
and it is not yet the [Lorentzian lift](thm_lorentzian_lift.md).  The
quadratic term also put this theorem in tension with P7', which wants the
four-derivative sector exactly empty; that tension was
[worked through, not hidden](kill_scalaron_cancellation.md) — the
surviving scalaron has a [range](num_scalaron_range.md) some thirty
orders of magnitude below the laboratory frontier.
