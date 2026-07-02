# Is dark energy exactly w = −1, forever, or does it evolve?

The theory's single live-fire confrontation: it forbids dark-energy evolution outright, and current DESI-class data is leaning the other way.

## The claim

VED commits to `w(z) = -1` exactly, at every redshift, with zero drift — `w0 = -1, wa = 0` in the usual CPL parametrization. This is not a fitted value that happens to sit near −1; it's structurally forced.

Why it can't be anything else:

- Λ is not a field, not a potential, not quintessence. It is the *integration constant* of the unimodular (trace-free) conservation law — a number fixed once, not a dynamical degree of freedom that can track redshift. See [thm_lambda_integration_constant.md](thm_lambda_integration_constant.md).
- The frustration floor — the real, constant vacuum energy density the packing carries — is sequestered: it cancels out of the field equations exactly (shift `T_ab -> T_ab - rho_f g_ab` just relabels Λ, doesn't perturb the dynamics). A constant floor contributes nothing to Λ's *value*, and having no dynamics, it certainly contributes no *evolution*. See [idea_sequestering.md](idea_sequestering.md).
- Between "Λ can't evolve" and "the floor can't evolve," there is no mechanism left anywhere in the closed sector that could produce a w(z) drifting away from −1.

```text
commitment:  w(z) = -1 exactly, at every redshift, forever (w0=-1, wa=0)
kills it:    any CONFIRMED w(z) != -1 at decisive significance
```

**Status: UNDER LIVE FIRE.** DESI BAO releases (2024–2025), combined with CMB and supernovae, report a several-sigma model-dependent preference for evolving dark energy (`w0 > -1`, `wa < 0`). Not yet decisive — systematics and dataset tensions are under active debate — but this is the theory's most exposed near-term prediction, not a comfortable standing null.

**The discipline trap, pre-registered.** The theory does have a gated "dark-excess" lane: a `w != -1` component riding *over* the sequestered floor, licensed only by independent production physics passing the 017–019 gates and the P9 fence. That lane exists on the books today, before any adverse DESI result. The trap: if evolving DE gets confirmed, reaching for that excess lane *after the fact*, with no independent gate-passing production mechanism already in hand, is a backsolve — explicitly forbidden by house rule. If DESI's result firms up and no such excess already exists on independent grounds, the register does not let the theory dodge; it records a kill against the closed vacuum sector. The trap is stated now, in ink, before the data forces the question — that's the entire point of pre-registering it.

**Proof:** predictions register A1, current through derivation 045 and the P10 adoption; forced by 033/034 (Λ as integration constant) and 035/038 (sequestering) → [../theory_v3/development/predictions/predictions_register.md](../theory_v3/development/predictions/predictions_register.md)

**Where next:**
- [The falsifier trail →](hub_predictions.md) — see this sitting alongside the other five Tier-A commitments, the full kill-zone inventory.
- [The cosmological-constant trail →](hub_lambda.md) — the full argument for why Λ is an integration constant and not a coupling, start to finish.
- [The sequestering edge →](pred_sequestering_edge.md) — the sibling commitment: constant vacuum-energy shifts (EW/QCD) also can't gravitate, same mechanism, different observational face.
- [The skeptic's entrance →](hub_graveyard.md) — the house discipline (no backsolving) that makes the discipline trap enforceable rather than rhetorical.
