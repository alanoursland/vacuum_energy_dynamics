# VacuumForge Next Iteration Overview

## Purpose of This Phase

The next iteration of VacuumForge is about strengthening the reliability of an AI-assisted theory-development workflow.

VacuumForge already provides useful symbolic machinery for testing algebraic claims: mode decompositions, source classifications, energy functionals, weak-field checks, concrete metric checks, coordinate transformations, structure search, and archive-backed dependency tracking. That is necessary, but it is no longer sufficient.

As the Vacuum Dynamics work has moved from early algebraic checks into larger field-equation search trees, a new failure mode has become visible: scripts can begin to govern the research program without actually proving the claims they use to steer it. They can recommend, defer, reject, or kill branches using language that looks like a result, even when the backing is only heuristic, editorial, or unresolved. In an AI-authored repository, this is especially dangerous. The system can drift toward a cleaner story instead of a justified one.

This phase exists to make that drift harder.

The goal is not to make VacuumForge more ambitious in its physics claims. The goal is to make it more disciplined about what kind of claim is being made, what evidence supports it, and whether downstream scripts are allowed to rely on it.

## Motivation

The original purpose of VacuumForge was to reduce algebraic self-deception. If a candidate equation is supposed to imply reciprocal scaling, trace-free exchange, positive configuration energy, or a weak-field recovery target, VacuumForge should help determine whether that implication actually follows or whether it was smuggled in as an assumption.

That mission remains intact.

The new concern is governance self-deception.

Later scripts increasingly make claims of the form:

- this route is too risky unless a missing theorem is derived;
- this coefficient must not be chosen from a recovery target;
- this branch should be killed if an overlap persists;
- this mechanism is not insertable yet;
- this candidate route is safer than that one;
- this status summary carries forward what the previous group established.

Some of those claims are useful research guidance. Some may eventually become hard exclusions. But they are not all the same kind of statement. A warning is not a contradiction. A policy rule is not a derivation. A candidate route is not a licensed mechanism. A summary is not a proof record.

The current tooling does not distinguish those cases strongly enough.

That creates several risks:

- hand-assigned dataclass statuses can look machine-checked;
- summary scripts can silently upgrade unresolved claims into working assumptions;
- branch-kill language can appear without a counterexample or witness;
- scripts can perform real symbolic checks but archive only empty run markers;
- downstream scripts can depend on the existence of a marker rather than the content of a result;
- toy compatibility examples can be mistaken for mechanism derivations;
- failed scripts can still leave result files that look like normal output;
- boolean pass/warn helpers can hide definitive failures as mere warnings.

This phase addresses those risks by expanding VacuumForge from algebra validation into claim-governance validation.

## Development Theme

The theme of this phase is:

> Make claim strength machine-visible.

VacuumForge should not merely ask whether an expression simplifies to zero. It should also ask what kind of claim a script is making and whether that claim has the right kind of support.

A derivation should point to the computation that derived it.

A counterexample should be recorded as a counterexample, not as prose.

A branch kill should require a structured reason.

An unresolved theorem target should remain unresolved until an actual derivation changes its status.

A sample profile should remain a sample profile.

A summary should query upstream records rather than restating them from memory.

This phase is about giving the repository enough structure that later scripts cannot easily mistake one of these claim types for another.

## What Changes Conceptually

The next iteration should introduce a clearer separation among four categories of repository output.

### 1. Derived results

These are claims backed by symbolic computation, algebraic identity checks, minimization, field-equation derivation, coordinate transformation, concrete metric validation, or other machine-checkable work.

They should be archived with actual inputs and outputs, not placeholder symbols that only prove the script ran.

### 2. Governance assessments

These are research-management judgments: warnings, route preferences, branch deferrals, policy rules, exclusion criteria, and branch decisions.

They may be valid and useful, but they should not masquerade as derived physics. Their strength should depend on their evidence.

### 3. Evidence objects

These are structured records that justify strong governance claims. Examples include counterexamples, leak witnesses, overlap witnesses, boundary violations, exterior scalar charge witnesses, recovery-selected-parameter witnesses, and failed conservation checks.

A strong exclusion should point to one or more evidence objects.

### 4. Unresolved obligations

These are missing derivations or unresolved proof targets that later scripts must not silently treat as solved.

When a script says “unless X is derived,” X should become a tracked obligation. Downstream scripts should be able to query whether that obligation is still open, satisfied, superseded, or failed.

## Working Principle

A script should be allowed to say less with weak evidence, but not more.

Informational workflow suggestions can remain light. A script can recommend the next test or identify an open question without a formal witness.

Constrained governance claims need at least a named reason and provenance. A script can defer a branch or mark a route risky if it says why and points to the relevant upstream record.

Exclusion-level claims require evidence. A script should not emit branch-kill, forbidden, rejected, or no-viable-route language unless it attaches a structured witness such as a counterexample, dependency leak, overlap witness, target-selection violation, boundary violation, or contradiction record.

This does not make the workflow bureaucratic. It keeps the strictness where it matters: at the point where a candidate route is removed, downgraded, or carried forward as licensed.

## Relationship to the Existing Archive

The current archive is the right foundation, but it needs to become more expressive.

The first archive layer records derivations and dependencies. That is still needed. However, the next iteration should avoid treating every important record as a derivation. A derivation, a proof obligation, a counterexample, an inventory marker, a sample derivation, and a branch decision are different objects.

The archive should therefore evolve from a derivation ledger into a broader epistemic ledger.

It should still answer:

- did this upstream derivation exist?
- did its output change?
- are declared dependencies satisfied?

But it should also answer:

- what kind of claim is this?
- what is its strength?
- what evidence supports it?
- is it derived, assumed, heuristic, policy-level, unresolved, or failed by witness?
- is this downstream summary upgrading the upstream claim strength?
- is this branch decision licensed by the required evidence?

This is not a replacement for the archive design. It is the next layer above it.

## Relationship to Scripts

This phase should also change the expected shape of future scripts.

Scripts should separate their output into recognizable blocks:

1. derived results;
2. governance assessments;
3. unresolved obligations.

A script that only inventories possibilities should identify itself as an inventory or memo script. It should not emit derivation-level statuses unless it performs and records derivations.

A script that performs symbolic computation should record the computation’s actual content. Empty derivation markers are not enough when the script has checked real identities, solved equations, or verified boundary conditions.

A script that rejects a branch should record a reason code and evidence object. If it lacks evidence, it should say the branch is unresolved, deferred, risky, or not insertable yet rather than killed.

A script that summarizes a group should build its status table from archive state wherever possible. If it adds interpretation, that interpretation should remain visibly separate from the upstream derivation record.

## Relationship to Linting and Runner Discipline

Not all of this belongs inside the core symbolic engine.

Some checks are better handled by linting and runner infrastructure.

A governance-aware lint pass should catch patterns such as:

- hardcoded dataclass status fields that claim derived or rejected status without provenance;
- branch-kill or forbidden language without evidence records;
- placeholder derivation markers in scripts that perform symbolic computation;
- boolean status helpers that cannot emit definitive failures;
- unsupported use of strong result vocabulary in memo or inventory scripts.

The script runner should also make execution failure impossible to miss. A result file containing stderr is not the same as a successful run. Failed scripts should produce explicit failure sentinels, and archive-marker absence should be visible to automated readers.

These tools are part of the same discipline: prevent result-shaped output from being mistaken for validated output.

## What This Phase Is Not

This phase is not an attempt to solve the covariant parent theory.

It is not an attempt to validate undefined physics objects.

It is not a feature sprint for every possible future validator.

It is not a license to turn every research instinct into a formal rule.

The point is narrower and more important: make the repository honest about the status of its own claims.

VacuumForge should remain conservative. It should not produce authoritative-looking verdicts for concepts that the theory has not yet defined well enough to validate. Where the mathematics is not ready, the system should record obligations, risks, and missing structure rather than pretend closure.

## Expected Outcome

After this phase, the next iteration of VacuumForge should make it much harder for AI-authored scripts to drift from exploration into unsupported conclusion-writing.

A reader should be able to inspect the archive and distinguish:

- what was actually derived;
- what was only sampled;
- what was merely compatible in a toy setting;
- what was rejected by witness;
- what was deferred by policy;
- what remains an unresolved proof obligation;
- what a summary imported from upstream;
- what a downstream script is allowed to rely on.

The repository should become less vulnerable to narrative momentum.

The best outcome is not that VacuumForge says “yes” more often. The best outcome is that it says “derived,” “assumed,” “heuristic,” “sample,” “counterexample,” “unresolved,” “deferred,” and “failed by witness” with enough precision that later work cannot blur those categories.

## Guiding Sentence

This phase turns VacuumForge from a symbolic validation workbench into a disciplined claim-governance workbench for AI-assisted field-equation search.

It keeps the goblin ledger sharp: no branch gets buried without a body, no theorem gets crowned without a derivation, and no pretty summary gets to outrank the archive.
