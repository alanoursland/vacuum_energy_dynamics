# How far below the Planck scale does the packing's leading dispersion kick in?

A reader who already knows the packing forbids linear Lorentz violation needs the number for the quadratic term it does leave behind, and how much room that number leaves before an experiment could see it.

## The number

The packing is a discrete network — bonds, angles, finite-range couplings — so it cannot be perfectly Lorentz invariant at all scales; the question is only how the dispersion relation `omega(k)` deviates from `ck` as `k` approaches the lattice cutoff. Parity of the dynamical matrix (see the theorem this number belongs to) kills the linear term outright, for every admissible packing, not just symmetric ones. What survives is the next term in the expansion:

```text
omega(k) = c k (1 - (ka)^2/24 + O(k^4 a^4))
```

exact for the monatomic chain witness, with the `1/24` coefficient model-dependent O(1) in general but the k^2 scaling structural. Converting the lattice cutoff into an energy scale gives the number:

- **E_QG,2 ~ sqrt(24) * E_Planck ~ 6e19 GeV** — the quadratic-suppression scale, a factor of ~sqrt(24) *above* the bare Planck energy, not below it.
- Current quadratic-order GRB bounds sit around **~1e11 GeV**.
- Margin: **~6e8**, i.e. roughly 8-9 orders of magnitude of headroom between the packing's predicted onset and what gamma-ray-burst time-of-flight data can currently probe.
- Concretely: a 1 TeV photon's predicted fractional speed shift is **|dv/c| ~ 3e-34** — unmeasurable with any foreseeable timing experiment.

This is not a fit to avoid falsification — the coefficient (1/24 in the exact chain witness, O(1) generically) falls out of the same harmonic-network algebra that forbids the linear term. There was no free parameter to tune once the packing class (P10: finite-range, real, quadratic-form microphysics) was fixed. The number is a consequence, not a choice.

The asymmetry with the linear-order result is the point: the linear scale isn't merely large, it's *infinite* — no admissible coupling in the P10 class produces a linear term at any order, so there is no "linear scale" to compare against bounds at all. The quadratic scale is the first place a real number exists, and it lands nine orders past where anyone is currently looking.

**Proof:** derivation 046 (`packing_dispersion_046`) → [../theory_v3/development/vacuum_sector/08_packing_microphysics/packing_dispersion_vacuumforge.md](../theory_v3/development/vacuum_sector/08_packing_microphysics/packing_dispersion_vacuumforge.md), register entry A5 in [../theory_v3/development/predictions/predictions_register.md](../theory_v3/development/predictions/predictions_register.md).

**Where next:**
- [Does the packing's discreteness leak a linear-order photon dispersion? →](pred_no_linear_liv.md) — the theorem this number is the quantitative tail of: why the linear term is exactly zero, for any packing.
- [The falsifier trail →](hub_predictions.md) — A5 alongside the program's other standing nulls and its one live-fire commitment.
- [The microstructure trail →](hub_packing.md) — the packing model whose harmonic-network structure forces both the zero and the 6e19 GeV scale.
- [Gravitational waves: exactly two polarizations →](pred_gw_purity.md) — the sibling standing null on the same propagating TT modes.
