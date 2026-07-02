# What has to be true for a claim to enter the archive at all?

Before this program will let a derivation count as a result, it has to name the observation that would kill it — and the name has to be on record before the result comes in.

## The idea

The house rule: no mechanism, candidate, or postulate is admitted to the theory's archive unless it carries a **charter** — a statement, written before the derivation runs, of what would make the result unacceptable. A charter fixes four things in advance: the question, the allowed assumptions, the forbidden shortcuts, and the possible verdict states. The verdict vocabulary is deliberately narrow:

```text
PASS            candidate passed the declared gate
KILLED          candidate contradicted a gate or failed a required bound
UNDERDETERMINED current evidence cannot decide
NOT_READY       prerequisites are missing
HANDOFF_READY   result is ready for a later stage, not itself final
```

Nothing gets "quietly accepted." Every candidate reaches one of these five states, and `KILLED` is not a failure of the process — it *is* the process working. This is the primary defense against what the house calls sycophantic theory-building: a model (human or LLM) can always generate a plausible continuation of an idea. A charter forces the question that continuation-generation never asks on its own: what would make this unacceptable?

Two rules give the charter its teeth:

- **No backsolving.** A kill condition cannot be tuned, narrowed, or reinterpreted after an adverse result to save the candidate. If a bound was violated by 54 orders of magnitude, the candidate is dead — not "dead in this window, alive in a redefined one." The predictions register calls this out explicitly for the dark-energy entry (A1): using the gated defect-excess lane to absorb an adverse w(z) measurement, without independent production physics for that excess, would be exactly this move, and it is pre-registered as forbidden *before* the DESI result is decisive.
- **No softening after the fact.** An entry in the predictions register may not be weakened once an adverse result lands, except by an explicitly recorded postulate-level move (the "P7-appeal pattern": revising an axiom's scope, on the record, as its own derivation — not quietly redrawing a boundary).

The register itself is the ledger this produces: every commitment states (i) what the theory commits to, (ii) which postulate or derivation forces it, (iii) what observation would kill it, (iv) current experimental status, and (v) what open obligation could change the entry. Concrete kills already on the books, not hypothetical: a dark-sector abundance gate that killed a depletion-history explanation for dark matter when the available budget missed by orders of magnitude; a higher-curvature health gate where ghost residues killed spin-2 quadratic curvature terms; the P7-prime gate where static hair killed the remaining four-derivative freedom, leaving the R^2-class scalaron at a Planck-suppressed, unobservable range. Near-misses are tracked with the same discipline as kills — the register flags that Newton's constant drift (A6) is forbidden outright by the theory while sitting only ~480x above the current lunar-laser-ranging bound, "under genuine experimental pressure and tightening." That sentence is what a charter-run archive looks like when it's honest about its own risk.

**Proof:** methodology stated in [../paper_drafts/04/md/04_charters_kill_conditions.md](../paper_drafts/04/md/04_charters_kill_conditions.md); applied at scale in the live register [../theory_v3/development/predictions/predictions_register.md](../theory_v3/development/predictions/predictions_register.md) and its house rules in [../theory_v3/development/predictions/README.md](../theory_v3/development/predictions/README.md).

**Where next:**
- [The Predictions Trail →](hub_predictions.md) — the register itself: one live-fire confrontation, five standing nulls, and the discipline trap spelled out for each.
- [The Verification Forge →](idea_forge.md) — the other half of the same discipline: no theorem is trusted until a script checks it, the same way no claim is trusted until it names its killer.
- [Matter as Defect →](idea_matter_as_defect.md) — a worked example of a gated charter: dark matter as packing defects, admitted only conditionally, with its own kill clause (B2).
- [The Graveyard →](hub_graveyard.md) — where the killed candidates actually live; this node explains the rule, that one shows the bodies.
