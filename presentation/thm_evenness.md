# Why can't the packing produce linear Lorentz violation, ever?

A reader who knows P10 predicts Planck-suppressed dispersion needs to see why the leading (linear) term is not just small but structurally forbidden — this is the theorem that turned a self-threat into a sharpened prediction.

## The theorem

Discreteness at the Planck scale is a standard worry: a lattice-like substrate usually leaks a linear-in-(E/E_Planck) term into the photon dispersion relation, and existing gamma-ray-burst timing bounds already exclude linear Lorentz-invariance violation (LIV) at scales far below E_Planck. If the packing behaved like a generic lattice, P10 would be dead on arrival against existing data.

It isn't, and the reason is structural, not a lucky cancellation:

- Take ANY harmonic network — any graph, any topology, no lattice symmetry assumed — whose energy is a real quadratic form built from finite-range couplings (pair springs, angle/wedge terms, arbitrary multi-body terms; this is the entire P10 class of actions).
- Reality of the strain energy alone forces the dynamical matrix to satisfy `D(-k) = D(k)*` and `D(k)^dagger = D(k)` (Hermitian). Its characteristic polynomial therefore has real coefficients and is manifestly even in k.
- An even characteristic polynomial means omega^2(k) is an even function of k along every direction — there is no algebraic room for an odd (linear) term to appear, in any direction, for any admissible packing.

```text
omega(k) = c k (1 + c2 (ka)^2 + O(k^4 a^4))   -- no linear term exists, by parity of D(k)
```

The protection is reality of the strain energy — the same structural fact that underlies the whole vacuum sector — not lattice point-group symmetry, which a disordered or frustrated packing might not even have. That is the load-bearing point: this is not "our lattice happens to be centrosymmetric," it is "any real quadratic action on any graph is even," so no future refinement of the packing's connectivity can reintroduce a linear term.

What the theorem does NOT forbid: quadratic-order dispersion. The (ka)^2 term survives and is model-dependent at O(1). Verified witnesses (exact monatomic chain, a fully symbolic generic two-band model with no inversion symmetry, and a diatomic chain) all give the predicted even spectrum, with the monatomic chain's coefficient computed exactly (-1/24) and subluminal. Putting in numbers: the linear scale is infinite (there is none), the quadratic scale runs at E_QG,2 ~ sqrt(24) E_Planck ~ 6e19 GeV — about 8-9 orders of magnitude below current quadratic GRB bounds (~1e11 GeV), giving a 1 TeV photon a |dv/c| ~ 3e-34. Scope is TT modes directly; matter is covered under the real-couplings assumption, with chiral matter couplings, non-locality, and anharmonicity logged as watch items, not loopholes yet exploited.

**Proof:** forge 046 (`packing_dispersion_046`) → [../theory_v3/development/vacuum_sector/08_packing_microphysics/packing_dispersion_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/packing_dispersion_vacuumforge.md), verification script `vacuum_forge/src/vacuum_sector/046_packing_dispersion/packing_dispersion.py`.

**Where next:**
- [The Falsifier Trail →](hub_predictions.md) — A5's place in the full predictions register, alongside the other standing and resolved commitments.
- [The Microstructure Trail →](hub_packing.md) — the packing model this theorem is a property of, and where its other microphysics predictions live.
- [The Graveyard →](hub_graveyard.md) — the skeptic's entrance; A5 started life there as a self-threat before this derivation resolved it.
- [The Lorentzian Lift →](thm_lorentzian_lift.md) — the full 4D/Lorentzian kinematics this parity argument sits inside.
