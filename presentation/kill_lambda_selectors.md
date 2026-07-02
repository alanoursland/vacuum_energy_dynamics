# Can any first-principles selector pick a nonzero cosmological constant?

Nine derivations tried to make `Lambda != 0` fall out of a mechanism instead of being inserted by hand. All nine failed — and the failures turned out to be theorems, not dead ends.

## The kill

Before the packing microphysics existed, the vacuum-sector program ran a
structured sweep: charter every plausible way a baseline `Lambda` could be
*selected* rather than *fitted*, then test each one against a fixed bar.

The bar (the selector charter) required every candidate to supply, before
touching the observed value:

```text
boundary data; sign/value mechanism; source ledger;
local-equation quarantine; falsifier; first concrete test.
```

Six selector classes were chartered and probed in turn — derivations 008
through 016, nine derivations total (inventory, charter, sieve, and one probe
per class):

- **Variational minimum** — `F(Lambda)` stationarity. A convex bare minimum
  gives `Lambda = 0`; any nonzero answer requires an imported linear bias `b`
  or an inserted target `Lambda_star`. No bare minimum produces a value.
- **Boundary/admissibility** — explicit asymptotic or horizon boundary data
  can convert a *supplied* length/volume/radius into a `Lambda` relation, but
  never derives that scale itself.
- **Topology/global constraint** — topology is dimensionless; it can restrict
  which sector you're in but cannot set a dimensionful constant on its own.
- **Measure identity** — only becomes a selector if it derives a covariantly
  conserved constant floor before observation is used; otherwise it's
  dimensional fitting.
- **Relaxation/fixed-point** — scale-free relaxation selects `Lambda = 0`;
  nonzero fixed points import a target, domain length, or kernel scale.
- **Frustration-floor microphysics** — potential shape can supply minima and
  excitations, but the absolute constant offset stays free unless
  microphysics derives it.

Every row hit the same wall: sector selection is not value selection without
a derived scale. None of the six ever got past "not mechanism-ready" in the
selector sieve (derivation 010) — no candidate ever supplied even the first
required object (an instantiated selector, a boundary class, a conserved
measure identity, a kernel, a coarse-graining map).

```text
Sector selection is not value selection without a derived scale.
```

The twist: this sweep was not wasted motion. Once the unimodular reading of
the field equations was found (derivation 033 — P3 is the fixed-measure
constraint, `Lambda` is an integration constant fixed by one global datum,
bulk vacuum energy is sequestered), the 008–016 negatives were re-read as
*theorems of that reading*: each selector class fails for the same reason —
none of them touches the actual free datum, which is not a mechanism at all
but a single global boundary condition. The sweep didn't miss a mechanism; it
correctly found there wasn't one at that level.

**Proof:** derivations 008–016 → [../theory_v3/development/vacuum_sector/04_lambda_baseline/lambda_selector_sieve.md](../theory_v3/development/vacuum_sector/04_lambda_baseline/lambda_selector_sieve.md), [../theory_v3/development/vacuum_sector/04_lambda_baseline/lambda_baseline_selector_charter.md](../theory_v3/development/vacuum_sector/04_lambda_baseline/lambda_baseline_selector_charter.md), [../theory_v3/development/vacuum_sector/04_lambda_baseline/lambda_variational_minimum_probe.md](../theory_v3/development/vacuum_sector/04_lambda_baseline/lambda_variational_minimum_probe.md); unimodular reframing (derivation 033) → [../theory_v3/development/vacuum_sector/summary.md](../theory_v3/development/vacuum_sector/summary.md)

**Where next:**
- [The Frustration-Relief Value Is Dead →](kill_partial_relief.md) — the sweep that came after: does the global datum at least give a value? No.
- [The Scalaron Cancellation Kill →](kill_scalaron_cancellation.md) — a later, sharper attempt to derive a constraint from the same unimodular structure, also refuted.
- [The Cosmological-Constant Trail →](hub_lambda.md) — where this kill sits in the larger Lambda story.
- [The Graveyard →](hub_graveyard.md) — more killed mechanisms, same even tone.
