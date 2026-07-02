# How do you check any claim in this wiki?

Every claim node in this wiki carries a forge number; this page explains what that number is and how to chase it to a script.

## The spine

Nothing in this program is asserted on authority. The chain is fixed and always the same four links:

1. **Claim** — a sentence in a node file (this wiki) or a theory-section file (`theory_v3/`).
2. **Theorem/result** — the precise statement, usually named in `theory_v3/development/vacuum_sector/00_orientation/current_status.md`, the log this whole wiki is built from.
3. **Derivation number** — a three-digit forge ID, e.g. `037`, assigned in commit order as the program worked through its obligation queue. The status log records each one as it closes: `derivation: relief_exact_geometry_037`.
4. **Verification script** — a numbered folder under `vacuum_forge/src/vacuum_sector/`, e.g. `037_relief_exact_geometry/`, containing the actual sympy/scipy code that either proves the claim symbolically or measures it numerically. No folder, no forge number, no claim.

```text
claim  ->  theorem  ->  derivation NNN  ->  vacuum_forge/src/vacuum_sector/NNN_.../
```

The numbering is literal and continuous — `001_strain_underdetermination` through the current end of the queue — and it is append-only. A closed derivation is never renumbered or silently edited; if a result is later overturned (see `kill_scalaron_cancellation` for an example: the program refuted its own week-old mechanism), the refutation gets its *own* new number and the old one stays on the books with its status corrected in prose, not deleted.

## What "obligation opened / obligation satisfied" means

Reading `current_status.md` you'll see almost every entry in this form:

```text
derivation: <name>_NNN
obligation satisfied: <what this derivation closed>
obligation opened:    <what it owes next>
```

This is the program's actual control loop, not decoration. Every derivation either discharges a standing obligation from the queue or opens a new one (usually both). There is no derivation that exists because it seemed interesting — each one is there because a prior result required it. That's what makes the chain auditable end to end: you can start at any current claim and walk the "obligation satisfied" pointers backward to the postulates, or walk "obligation opened" forward to see what still isn't nailed down.

Two disciplines keep this from becoming a wall of assertions:

- **Kill conditions precede claims.** A mechanism is not allowed to publish a result until its failure mode is stated. `higher_curvature_scalar_prototype_006` is a clean example: it exists specifically to try to break the higher-curvature residual branch, and it succeeds (the branch is not licensed) — recorded with the same weight as a positive result.
- **No backsolving.** A derivation may not be shaped, after the fact, to hit an observed number. `lambda_relaxation_fixed_point_probe_015` and its neighbors are explicit about this: several routes are rejected specifically because the only way to get a nonzero value was to import the target.

## Reading the log itself

`current_status.md` runs sequentially, oldest section first, and is the closest thing this program has to a lab notebook — roughly fifty entries as of forge 054, from `001_strain_underdetermination` (the opening result: pointwise interval response alone cannot select a strain functional) through the most recent theory-owner rulings. Each section name is a milestone; each `derivation:` block is the audit anchor for that milestone.

**Proof:** the spine itself is [../theory_v3/development/vacuum_sector/00_orientation/current_status.md](../theory_v3/development/vacuum_sector/00_orientation/current_status.md); the numbered scripts it points to live under [../vacuum_forge/src/vacuum_sector/](../vacuum_forge/src/vacuum_sector/) (e.g. `037_relief_exact_geometry/` for the partial-relief kill, `046_packing_dispersion/` for the evenness theorem).

**Where next:**
- [The Rules →](hub_rules.md) — the discipline this index exists to enforce: kill-conditions-first, the forge, honest negatives.
- [The Assumption Ledger →](hub_postulates.md) — the ten postulates every derivation number ultimately traces back to.
- [The Falsifier Trail →](hub_predictions.md) — where the chain points forward, into commitments that can still fail.
- [The Skeptic's Entrance →](hub_graveyard.md) — the other side of the ledger: derivations that closed a branch as dead, not alive.
