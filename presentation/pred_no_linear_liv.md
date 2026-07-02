# Does the packing's discreteness leak a linear-order photon dispersion?

A reader who knows the packing is discrete at the Planck scale needs to see why that doesn't produce the generic lattice sin — the theorem that turned this from the theory's sharpest self-threat into an outright kill condition on P10.

## The claim

Discrete substrates usually don't get away with it: a generic lattice underlying spacetime leaks a linear-in-(E/E_Planck) term into the photon/GW dispersion relation, and gamma-ray-burst time-of-flight bounds already exclude linear Lorentz-invariance violation (LIV) at scales far below E_Planck. If the packing behaved like a generic lattice, adopting P10 (finite-range harmonic microphysics) would have been dead against existing data on day one — this entry started life in the register as a self-threat, not a prediction, precisely because nobody had checked.

It's checked now, and the answer is structural, not a lucky numerical near-miss:

- For ANY harmonic network — any graph, any topology, no lattice point-group symmetry assumed — whose energy is a real quadratic form built from finite-range couplings (pair springs, angle/wedge terms, arbitrary multi-body terms: the entire P10 class of actions), the dynamical matrix satisfies `D(-k) = D(k)*` and is Hermitian. Its characteristic polynomial is therefore real and manifestly even in k.
- Even characteristic polynomial means omega^2(k) is an even function of k in every direction. There is no algebraic room left for a linear (odd) term, for any admissible packing, disordered or not.

```text
omega(k) = c k (1 + c2 (ka)^2 + O(k^4 a^4))   -- no linear term, by parity of D(k)
```

The protection is the reality of the strain energy — not a symmetry a frustrated or disordered packing might lack. That's why the theorem, not a computation on one specific lattice, is what's load-bearing: no future refinement of the packing's connectivity graph can reintroduce a linear term.

Verified witnesses (forge 046): the exact monatomic chain gives omega/ck = 1 − (ka)²/24 exactly, subluminal; a fully symbolic generic two-band model with no inversion symmetry confirms trace and det stay even in k; a diatomic chain (also no inversion symmetry) gives the textbook acoustic branch with zero k³ term. Putting in numbers: the linear scale is not small, it is infinite — there is none. The surviving quadratic scale runs at E_QG,2 ~ sqrt(24) E_Planck ~ 6e19 GeV, about 8-9 orders of magnitude below current quadratic GRB bounds (~1e11 GeV); a 1 TeV photon's predicted |dv/c| ~ 3e-34.

What was a standing constraint the microphysics had to respect (register entries O-P10-1/O-P10-4: "compute the dispersion face, don't assume it's benign") is now resolved into a prediction, and the resolution sharpens the stakes rather than retiring them: because the no-linear-term result is theorem-grade, not model-fit, a single confirmed linear-order LIV detection would falsify P10 outright — it cannot be dialed down or accommodated by retuning a coupling, because no coupling choice within the P10 class produces a linear term in the first place. The one recorded escape hatch is chiral (time-reversal-breaking) matter discretizations, which evade the parity argument and are logged as a watch item requiring a re-run, not a loophole anyone has exploited.

**Proof:** derivation 046 (`packing_dispersion_046`) → [../theory_v3/development/vacuum_sector/08_packing_microphysics/packing_dispersion_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/packing_dispersion_vacuumforge.md), register entry A5 in [../theory_v3/development/predictions/predictions_register.md](../theory_v3/development/predictions/predictions_register.md).

**Where next:**
- [The falsifier trail →](hub_predictions.md) — A5's place among the other five sharp standing nulls and the one live-fire commitment.
- [The microstructure trail →](hub_packing.md) — the packing model this dispersion theorem is a property of, and its other microphysics commitments.
- [Gravitational waves: exactly two polarizations →](pred_gw_purity.md) — the sibling standing null on the same propagating TT modes, no dispersion either.
- [The skeptic's entrance →](hub_graveyard.md) — where this entry started, as a self-inflicted threat before derivation 046 cleared it.
