# Do gravitational waves carry any signature of the packing?

a standing null: VED predicts LIGO/Virgo/KAGRA see exactly what GR sees, nothing more.

## The claim

Gravitational waves in this theory have three properties, all forced,
none adjustable:

- **exactly two polarizations** — transverse-traceless (TT), the
  massless spin-2 set. No breathing mode, no longitudinal mode, no
  vector polarization.
- **no dispersion** — they propagate at exactly $c$, at every
  frequency accessible to any current or near-future detector.
- **exactly the quadrupole rate** — radiated power follows the GR
  quadrupole formula with GR's coefficient, not a rescaled one.

This is a *null* prediction, and in this framework nulls are load-bearing:
the theory doesn't merely fail to predict extra structure, it actively
forbids it, for three independent reasons stacked on top of each other.

**Why only two polarizations.** The vector sector carries no radiative
degree of freedom (derivation 017: no vector radiation). The scalar
sector is constraint-type, not propagating. Under the P10 packing
closure, the TT modes are the *only* propagating modes the frustrated
packing supports (derivation 043, importing the Roček–Williams result
for embedded discrete structures) — there is no fourth channel for a
signal to ride in on.

**Why no dispersion.** This is inherited from the packing's discreteness
theorem (derivation 046): for any real, finite-range, harmonic action on
the packing, reality of the strain energy forces the dispersion relation
even in $k$ — $D(-k) = D(k)^*$ — killing every linear-order term. The
leading correction is quadratic and Planck-suppressed
($E_{QG,2} \sim \sqrt{24}\,E_P$), roughly 8-9 orders below current
quadratic gamma-ray-burst bounds. For GW frequencies and baselines, this
is unmeasurably close to zero.

**Why the quadrupole rate, exactly.** This is Theorem 5 of the closure
proof: coupling the linear (Fierz-Pauli) graviton to its own stress
tensor, iterated to self-consistency (Theorem 5u), fixes the radiative
normalization $K_T = c^4/16\pi G$ per polarization with no free constant
left over. The corollary is the quadrupole formula itself:

```text
P = (G / 5c^5) * < d^3Q_ij/dt^3 * d^3Q_ij/dt^3 >
```

— GR's formula, GR's coefficient, derived independently through the
substance-accounting route (P3a/P6/P7'/P9 + Newton) and the field-theory
closure route (K1-K3 + P9 + Newton), which meet at the same
Schwarzschild exterior. There is no adjustable normalization left for a
GW amplitude anomaly to hide in.

**Proof:** proof.md Theorems 4-5 (radiative positivity, closure
uniqueness, quadrupole power); derivation 017 (no vector radiation);
derivation 043 (P10 packing closure: TT-only propagation); derivation
046 (dispersion evenness theorem). Register entry A2 —
[../theory_v3/development/predictions/predictions_register.md](../theory_v3/development/predictions/predictions_register.md).

**Where next:**
- [No Linear Lorentz Violation →](pred_no_linear_liv.md) — the same evenness theorem (046) that kills GW dispersion also forbids linear LIV everywhere, and comes with an outright-kill condition on P10.
- [Black Holes Stay GR →](pred_gr_black_holes.md) — the companion standing null: exteriors and ringdowns, not just the waves crossing empty space between sources.
- [The Falsifier Trail →](hub_predictions.md) — see where this A2 null sits among the theory's other five sharp standing nulls and one live-fire prediction.
- [The Skeptic's Entrance →](hub_graveyard.md) — for readers who want the failure modes and near-misses before the wins.
