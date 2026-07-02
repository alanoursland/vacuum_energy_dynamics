# How does this program keep itself honest?

Every other node in this wiki makes a claim; this one explains the machine that is allowed to make claims at all — read it before you decide how much to trust the rest.

## The rules

This is not a theory presented after the fact with its failures scrubbed. It is a working ledger, and the ledger's discipline is the actual product, not decoration around the physics.

**Kill conditions before claims.** No mechanism is adopted until its failure mode is written down first. The predictions register states, for every entry: what the theory commits to, which postulate or derivation forces it, what observation would kill it, current status, and what open obligation (if any) could change the entry — in that order, before the entry counts as live. A mechanism proposed without a pre-stated kill condition doesn't get a page here; it gets rejected on procedure, independent of whether it happens to be right.

**No backsolving, ever.** You may not look at an observed number and then reverse-engineer a mechanism to hit it. This is enforced explicitly, not just as a norm: the w = −1 entry in the register pre-registers its own trap — invoking the dark-sector excess lane to absorb an adverse w(z) result *without independent production physics* is named, in advance, as a forbidden backsolve. If it happens anyway, the entry is a kill, not a save.

**No softening after an adverse result** except through an explicit, recorded postulate-level move — the register calls this the "P7′-appeal pattern." A theory that quietly loosens its own commitment after the data comes in isn't making predictions, it's making excuses; the house rule blocks that move by requiring the appeal itself to be visible and dated.

**The forge.** Every derivation that matters is checked by a script — sympy for algebra, scipy for numerics — not asserted in prose. These live under `vacuum_forge/` and are numbered (forge 001, 002, ... currently past 054); every theorem node in this wiki cites its forge number so a skeptic can run the check, not just read the claim.

**The register.** The single place every observable commitment lives, tiered by sharpness (Tier A = live-fire testable now, down through structural commitments still gated on obligations). Nothing is claimed as a prediction outside the register, and nothing enters the register without a kill direction attached.

**Fences.** A result that holds under a narrow, explicit scope is fenced to that scope rather than quietly generalized. Example from the vacuum-sector ledger: local interval response alone reconstructs pointwise metric data but does not determine between-point strain dynamics — that's recorded as "underdetermined without a new axiom," not stretched into a claim it doesn't support. Fences also show up as forbidden-use markers on candidate mechanisms and as explicit "no dimensionful scale supplied" verdicts across the Lambda-baseline selector sweep — the recurring finding there is that *sector selection is not value selection* without a derived scale, and every one of nine independent selector routes (variational, boundary, topological, measure-identity, relaxation, frustration-floor microphysics) is fenced off rather than allowed to smuggle in an underived number.

**Honest negatives, recorded with the same care as positives.** The clearest evidence of the discipline: this program has killed its own proposals. The scalaron-cancellation mechanism was proposed in-house and refuted in-house, same week, once the Bianchi identity was checked. The founding motivation for the whole research program — extracting vacuum energy through an engineered boundary — died by 54–114 orders of magnitude once its own operator was derived. Both are written up at full length, not buried.

```text
house order: kill condition -> forge check -> register entry -> fence if scope is narrower than the claim
```

**Proof:** [../theory_v3/development/vacuum_sector/README.md](../theory_v3/development/vacuum_sector/README.md) (branch-admissibility framework, gate manifests, the "underdetermined without a new axiom" verdict) and [../theory_v3/development/predictions/README.md](../theory_v3/development/predictions/README.md) (the five-field register house rule and the no-backsolve/no-soften-except-by-recorded-appeal clauses).

**Where next:**
- [The Graveyard →](hub_graveyard.md) — the discipline in action: every idea this program killed itself, each with its death certificate.
- [The Falsifier Trail →](hub_predictions.md) — the register itself, tiered, with live status against real observations.
- [The Cosmological-Constant Trail →](hub_lambda.md) — the fence discipline's clearest case study: nine selector routes tried, all fenced off, none smuggling in an unfixed scale.
- [Front door →](README.md) — back to the three entrances.
