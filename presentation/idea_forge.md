# How do you know a derivation in this program is actually correct?

Every claim in this program traces back to a script that checked it symbolically — the forge doesn't let a result stand on the strength of the prose around it.

## The idea

VacuumForge (the "forge") is a SymPy/SciPy verification platform, not a proof-of-concept demo. Its stated purpose is explicit: "help distinguish consequences that genuinely follow from a candidate structure from consequences that were quietly inserted by hand." The worry it exists to kill is ordinary in speculative theory-building — an equation that *looks* right because a sign, a coefficient, an expansion order, or a hidden assumption carried the result rather than the physics.

The mechanics: each numbered forge script (there are 50+ just in the `vacuum_sector` line, e.g. `037_relief_exact_geometry`, `041_frustration_relaxation_lab`) does four things in the same run:

- Defines the candidate structure symbolically (SymPy expressions, functionals, constraints).
- Runs `require_equal` / `require_zero` assertions that hard-fail (`AssertionError`) if the algebra doesn't close — there is no silent pass.
- Writes a governance record through `vacuumforge.governance`: a `ClaimRecord` (tiered — `INFORMATIONAL`, `CONSTRAINED`, `EXCLUSION`, `LICENSING`), a `ProofObligationRecord` for whatever the script *didn't* settle, and a `derivation_id` linking output back to inputs.
- Emits a human-readable `.md` report into `theory_v3/development/` — the forge is the source of truth; the prose report is a rendering of it, not the other way around.

The governance layer is the part that keeps the program honest about its own gaps. A script can pass its algebra and still record an `UNRESOLVED_PROOF_OBLIGATION` (see forge 001, `strain_underdetermination_witness.py`: two Lagrangians share the same pointwise Hessian but diverge in their Euler-Lagrange operator and boundary data — proof that "matches locally" does not mean "matches globally," recorded as an open obligation rather than swept aside). Obligations don't disappear when convenient; they get closed by a later script or they stay open and visible. Forge 029, the `vacuum_sector_program_checkpoint`, exists purely to summarize lane-by-lane status across the whole sweep — which branches are `LICENSED_CLAIM`, which are `DEFERRED_PENDING_PREREQUISITES`, which are blocked and by what.

Archives persist run-to-run (`ProjectArchive` / `.vacuumforge_archive`) and detect source invalidation: if you edit a script, its dependents know their cached derivation is stale. Downstream scripts declare dependencies on specific upstream `derivation_id`s and the forge checks them before trusting the chain.

```text
script -> SymPy/SciPy assertions (hard fail if false)
       -> derivation_id + ClaimRecord (tiered) + ProofObligationRecord
       -> .md report in theory_v3/development/
```

This is what "forge NNN" means every time another node cites it: not "we believe this," but "this script ran, its assertions passed, and its claim/obligation ledger is on record."

**Proof:** platform itself — [../vacuum_forge/README.md](../vacuum_forge/README.md); worked example of the derivation→claim→obligation pattern — [../vacuum_forge/src/vacuum_sector/001_strain_underdetermination/strain_underdetermination_witness.py](../vacuum_forge/src/vacuum_sector/001_strain_underdetermination/strain_underdetermination_witness.py); program-wide status rollup — [../vacuum_forge/src/vacuum_sector/029_vacuum_sector_program_checkpoint/vacuum_sector_program_checkpoint.py](../vacuum_forge/src/vacuum_sector/029_vacuum_sector_program_checkpoint/vacuum_sector_program_checkpoint.py).

**Where next:**
- [The Kill Conditions →](idea_kill_conditions.md) — the companion discipline: every mechanism must name what would falsify it before it can claim anything.
- [The Floor →](idea_floor.md) — a concrete forge result (derivations 037–041) built on exactly this derivation/claim/obligation machinery.
- [Proof Index →](hub_proof_index.md) — the index of forge derivations behind the wiki's claims.
- [The Graveyard →](hub_graveyard.md) — where the forge's obligations went unmet and a mechanism got killed instead of licensed.
