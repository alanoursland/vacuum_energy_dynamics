# VacuumForge Next Iteration Feature Design

## Purpose

This document specifies the expected behavior of the next iteration of VacuumForge.

It is a behavioral specification, not an implementation plan. It does not prescribe internal APIs, storage formats, module layouts, class names, or algorithms. It defines what the system must recognize, enforce, record, report, and refuse to overstate.

The purpose of this phase is to extend VacuumForge from algebra validation into claim-governance validation. VacuumForge already helps determine whether symbolic claims follow from equations, assumptions, mode decompositions, source rules, and energy functionals. The next iteration must also determine whether repository-level research claims are supported at the strength with which they are being used.

The central behavior is simple:

```text
A script may say only as much as its evidence supports.
```

A derivation must be backed by a computation. A branch kill must be backed by a witness. A policy rule must remain visibly different from a theorem. A summary must not outrank the archive. A toy example must not be mistaken for a mechanism derivation. An unresolved obligation must not silently become an assumption.

## Scope

This feature phase covers claim governance, evidence tracking, proof-obligation tracking, archive expressiveness, script-output discipline, summary discipline, linting support, runner visibility, and dependency verification.

It does not attempt to add validators for undefined physics objects. It does not attempt to solve the covariant parent theory. It does not convert every research judgment into a theorem. It only makes the status of each claim explicit and machine-visible.

## Core Concepts

### Derived Result

A derived result is a claim backed by machine-checkable work. Examples include symbolic simplification, equation solving, minimization, coordinate transformation, identity checking, perturbative expansion, concrete metric validation, source classification, or counterexample construction.

A derived result must record what was derived, what inputs were used, and what status the derivation has.

### Governance Assessment

A governance assessment is a research-management judgment. Examples include warnings, route preferences, branch deferrals, policy rules, exclusion criteria, and branch decisions.

Governance assessments may be useful and necessary, but they are not derivations unless they are backed by derivations or structured evidence.

### Evidence Object

An evidence object is a structured record that supports a governance claim. Examples include counterexamples, overlap witnesses, dependency leaks, target-selection violations, boundary violations, scalar-charge witnesses, failed conservation checks, and contradiction records.

Evidence objects are the basis for strong exclusions.

### Proof Obligation

A proof obligation is a tracked missing derivation or theorem target. When a script says “unless X is derived,” X must become a proof obligation rather than remaining prose.

Proof obligations may be open, satisfied, failed, superseded, abandoned, or deferred.

### Claim Tier

Claim tier is the strength of a claim and determines what support is required.

Tier 1 claims are informational. They include workflow suggestions, open questions, and descriptive summaries. They do not require formal evidence.

Tier 2 claims are constrained governance claims. They include risk flags, deferrals, preference rankings, and “not insertable yet” judgments. They require a named reason and provenance.

Tier 3 claims are exclusions or licensing claims. They include branch kills, forbidden routes, rejected coefficients, contradiction claims, and claims that a route is licensed for downstream use. They require structured evidence or derivation support.

## Feature 1: Claim Classification

VacuumForge must distinguish different kinds of claims rather than treating all script output as equivalent.

A claim must be classifiable as at least one of:

```text
derived_result
governance_assessment
evidence_object
proof_obligation
inventory_marker
memo_statement
sample_result
counterexample
branch_decision
handoff_import
```

The system must not allow a claim of one kind to silently behave like a stronger kind. In particular:

```text
memo_statement must not behave as derived_result
sample_result must not behave as theorem support
inventory_marker must not behave as proof
policy_rule must not behave as derivation
candidate_route must not behave as licensed route
open proof obligation must not behave as satisfied obligation
```

When a script emits or records a claim, VacuumForge must preserve the claim kind in any downstream summary or dependency check.

If a claim has no explicit kind, the system should treat it as unverified or memo-level rather than derived.

## Feature 2: Claim Strength And Evidence Requirements

VacuumForge must enforce a relationship between claim strength and evidence.

Tier 1 informational claims may be recorded without evidence. They must not be used as branch-kill, branch-license, theorem, or exclusion support.

Tier 2 constrained claims must include a named reason and provenance. Provenance may point to a script, prior claim, derivation, obligation, or evidence object. If provenance is missing, the claim must be downgraded or flagged as unsupported.

Tier 3 exclusion or licensing claims must include structured evidence. If a Tier 3 claim lacks required evidence, the system must not report it as killed, forbidden, rejected, derived, licensed, or closed. The strongest allowed status must be an unresolved or unproven governance status.

Examples of required downgrades:

```text
BRANCH_KILLED without evidence -> UNPROVEN_EXCLUSION
FORBIDDEN without evidence -> OPEN_RISK or POLICY_RULE
REJECTED without witness -> DEFERRED or NOT_INSERTABLE_YET
LICENSED without derivation/evidence -> CANDIDATE_ROUTE
DERIVED without computation -> UNVERIFIED
```

VacuumForge must make these downgrades visible in reports.

## Feature 3: Governance Status Vocabulary

VacuumForge must provide a controlled vocabulary for governance statuses.

At minimum, the system must distinguish:

```text
HEURISTIC
OPEN_RISK
POLICY_RULE
UNPROVEN_EXCLUSION
UNRESOLVED_PROOF_OBLIGATION
NOT_INSERTABLE_YET
DEFERRED_PENDING_PREREQUISITES
FAILED_BY_WITNESS
KILLED_BY_CONTRADICTION
CANDIDATE_ROUTE
PROVISIONAL_CONVENTION
LICENSED_CLAIM
REJECTED_ROUTE
SUPERSEDED
UNVERIFIED
```

These statuses must not be confused with derivation statuses such as:

```text
DERIVED
DERIVED_REDUCED
MATCHED
ASSUMED
FAILED
UNDETERMINED
```

A governance status may reference derivations, but it is not itself a derivation unless it is explicitly backed by derivation evidence.

## Feature 4: Evidence Objects

VacuumForge must support structured evidence objects for claims that require backing.

Evidence objects must be typed. The minimum useful evidence types are:

```text
counterexample
dependency_leak
overlap_witness
boundary_violation
exterior_scalar_charge_witness
target_selected_parameter
recovery_precedes_origin
failed_conservation_check
failed_boundary_neutrality_check
duplicate_degree_of_freedom_witness
contradiction_record
```

An evidence object must record what claim it supports or challenges.

An evidence object must preserve enough content for downstream scripts to distinguish a real witness from a prose assertion. A witness may be symbolic, algebraic, dependency-based, or structural, but it must be explicitly recorded.

If a branch decision refers to an evidence object that is missing, superseded, failed, or stale, the branch decision must not remain strong. It must be downgraded or reported as unsupported.

## Feature 5: Branch Governance

VacuumForge must treat branch decisions as first-class governance claims.

A branch or route may have statuses such as:

```text
candidate_route
provisional_convention
licensed_claim
deferred_route
not_insertable_yet
rejected_route
killed_by_contradiction
failed_by_witness
superseded_route
```

A branch may be marked as candidate without formal evidence if it is clearly labeled as candidate.

A branch may be marked as deferred if a missing prerequisite or open obligation is recorded.

A branch may be marked as rejected only if the rejection has a reason code and sufficient backing for its tier.

A branch may be marked as killed only if a structured witness or contradiction record exists.

The system must distinguish:

```text
not ready
not insertable yet
deferred pending prerequisite
risky without theorem
failed by witness
killed by contradiction
```

These are not interchangeable.

Optional branches must default to absent, not latent. An optional branch may become a candidate route only when activation conditions are recorded. It may become licensed only when evidence or derivation support exists.

## Feature 6: Reason Codes

Strong governance decisions must carry standardized reason codes.

Reason codes must be machine-readable. Examples include:

```text
recovery_selected_parameter
gr_copy_construction
boundary_repair_after_failure
double_counting_without_overlap_witness
exterior_scalar_charge
unresolved_overlap
missing_boundary_neutrality_theorem
missing_coefficient_origin
unresolved_source_identity
unresolved_parent_identity
stale_dependency
superseded_dependency
sample_only_support
```

Reports may include prose explanations, but the reason code must be present for automated checks.

If a branch decision has only prose and no reason code, the system must treat it as weak governance unless a structured evidence object is also present.

## Feature 7: Proof Obligation Tracking

VacuumForge must make unresolved derivation requirements first-class records.

When a script states or implies “unless X is derived,” “requires Y,” “cannot proceed until Z,” or “this is a theorem target,” the missing item should be recordable as a proof obligation.

A proof obligation must have a status. Minimum statuses are:

```text
OPEN
SATISFIED
FAILED
SUPERSEDED
ABANDONED
DEFERRED
```

A proof obligation must be queryable by downstream scripts.

A downstream script must not silently treat an open obligation as satisfied. If it proceeds under an open obligation, the output must say that it is operating under an unresolved prerequisite.

When an obligation is satisfied, the satisfying derivation or evidence must be referenced.

When an obligation is superseded, the replacement obligation or route must be referenced.

## Feature 8: Archive Record Kinds

The archive must distinguish record kinds beyond derivations.

At minimum, the archive must be able to represent:

```text
DERIVATION
SAMPLE_DERIVATION
COUNTEREXAMPLE
DIAGNOSTIC_EXAMPLE
COMPATIBILITY_EXAMPLE
INVENTORY_MARKER
MEMO_RECORD
GOVERNANCE_CLAIM
PROOF_OBLIGATION
EVIDENCE_OBJECT
BRANCH_DECISION
HANDOFF_IMPORT
SUPERSEDED_RECORD
UNARCHIVED_FOUNDATION
```

A dependency on a record must preserve the record kind. If a downstream script depends on a sample derivation, reports must show that the dependency is sample-level, not theorem-level.

Inventory markers must not be treated as mathematical derivations.

Memo records must not satisfy proof obligations.

Compatibility examples may show that a condition is coherent in a toy setting, but they must not license a mechanism unless additional evidence exists.

## Feature 9: Rich Derivation Records

When a script performs real symbolic computation, VacuumForge must encourage or require the actual result to be archived.

A derivation record should capture:

```text
inputs
outputs
method or derivation type
status
scope
claim kind
assumptions used
upstream dependencies
```

A derivation record that only proves a script ran must be marked as an inventory marker or run marker, not a derivation.

If a script uses symbolic operations such as simplification, solving, expansion, variation, identity checking, or boundary-condition checking, but records only an empty marker with placeholder output, the system should flag the record as insufficient for downstream mathematical reliance.

A downstream script must be able to distinguish:

```text
this script ran
this script checked an identity
this script derived this exact expression
this script gave a sample construction
this script found a counterexample
```

## Feature 10: Expected Output Dependencies

Dependency verification must be able to check more than the existence of an upstream marker.

A downstream dependency may specify:

```text
expected record exists
expected record kind
expected status
expected output
expected evidence type
expected obligation status
```

If the upstream record exists but its output differs from the expected output, the dependency must be reported as changed, not merely satisfied.

If the upstream record exists but has the wrong kind, the dependency must be reported as kind-mismatched.

If the upstream record exists but has been superseded, the dependency must be reported as superseded and must not silently pass.

If the upstream record is a sample or compatibility example and the downstream script expects a derivation, the dependency must fail or be downgraded.

## Feature 11: Summary And Handoff Discipline

Summary scripts must not restate upstream status from memory when archive state is available.

A summary must distinguish:

```text
derived upstream results
governance assessments
open obligations
rejected routes
candidate routes
handoff imports
```

A summary may add interpretation, but interpretation must remain separate from upstream derivation status.

A summary must not upgrade upstream claim strength without new evidence.

Examples of forbidden silent upgrades:

```text
UNRESOLVED -> CANDIDATE
CANDIDATE -> LICENSED
THEOREM_TARGET -> DERIVED
OPEN_RISK -> REJECTED
NOT_INSERTABLE_YET -> BRANCH_KILLED
SAMPLE_DERIVATION -> DERIVATION
```

If a summary strengthens a claim, it must attach a new derivation or evidence object.

Handoff summaries must explicitly list what the next group may assume, what remains open, and which imports are only provisional.

## Feature 12: Script Type Discipline

Scripts must be able to declare their epistemic role.

Minimum script types are:

```text
DERIVATION
SAMPLE
COUNTEREXAMPLE
DIAGNOSTIC
INVENTORY
AUDIT
REQUIREMENTS
MEMO
SIEVE
SUMMARY
HANDOFF
RUNNER
```

A script type constrains the strongest claims the script may emit without additional evidence.

Inventory, memo, sieve, requirements, and summary scripts must not emit derivation-level statuses unless they perform and record derivations.

Audit scripts should include at least one controlled failure or known-bad case when the audit claims to detect a failure mode.

A script with no derivation records beyond inventory markers should not emit `DERIVED`, `FORBIDDEN`, `BRANCH_KILLED`, or equivalent strong statuses.

## Feature 13: Output Block Discipline

Future scripts should separate output into recognizable blocks.

The required conceptual blocks are:

```text
derived_results
governance_assessments
unresolved_obligations
```

Additional blocks may include:

```text
sample_results
counterexamples
diagnostics
handoff_imports
controlled_failures
```

A result should appear in the block matching its claim kind.

A script must not intermix derived mathematical results and governance preferences in a way that makes them indistinguishable to automated readers.

Reports should preserve this separation.

## Feature 14: Status Output Discipline

VacuumForge-supported script output must distinguish pass, warning, failure, and unsupported claim.

A boolean pass/warn interface is insufficient for validation scripts because it cannot represent definitive failure.

The system must allow at least:

```text
PASS
WARN
FAIL
UNDETERMINED
UNSUPPORTED
INFO
```

A computed identity failure must be able to print or record as `FAIL`, not merely `WARN`.

A missing prerequisite must not print as `PASS` simply because the script handled the absence.

An unsupported strong claim must not print as `PASS`; it should print as unsupported, downgraded, or failed depending on severity.

## Feature 15: Governance Linting

VacuumForge’s linting layer must detect validation-theater and governance-theater patterns.

The linting behavior should flag:

```text
hardcoded dataclass statuses that claim derivation or rejection without provenance
branch-kill language without evidence object
forbidden/rejected/killed language without witness
coefficient rejection without dependency-direction check
recovery-target language upstream of coefficient origin
empty derivation markers in scripts that perform symbolic computation
boolean status helpers that cannot emit FAIL
summary claim upgrades without new evidence
sample records used as theorem support
script result files with stderr but no failure sentinel
```

Linting should not decide whether the physics is true. It should decide whether the script shape is compatible with the strength of the claim being emitted.

Lint results should distinguish warnings from failures. Harmless workflow text should not be treated like unsupported branch-kill language.

## Feature 16: Runner And Result-File Discipline

The script runner must make execution failure visible.

If a script exits nonzero, the result file must be marked as failed in a way automated readers can detect.

A result file containing stderr must not look like a clean script output.

The runner should distinguish:

```text
script completed successfully
script completed with warnings
script failed at runtime
script failed before archive marker
script produced no archive records
script produced stale or invalid records
```

A failed script may still have a result file, but the existence of the result file must not imply successful execution.

## Feature 17: Order And Coverage Discipline

VacuumForge tooling should verify group execution order metadata.

The expected behavior is:

```text
every script in a group appears in order metadata exactly once
no order entry points to a missing file
no script file is orphaned unless explicitly excluded
summary scripts are last unless explicitly marked otherwise
superseded scripts are marked superseded or removed from active order
versioned script pairs have a canonical successor relationship
dependencies are consistent with execution order or explicitly cross-group
```

If an early group lacks archive records, downstream bridge scripts should record that they depend on unarchived foundations rather than hiding the gap.

## Feature 18: Supersession And Canonicality

VacuumForge must represent when a script, record, or result has been superseded.

If two versions of a script exist, the system should be able to identify which one is canonical, which one is superseded, and whether both are still active.

A downstream script that depends on a superseded record must receive a warning or failure unless it explicitly declares that it is depending on historical behavior.

Superseded records should remain inspectable but should not satisfy current dependencies by default.

## Feature 19: Scope And Sample Discipline

VacuumForge must distinguish full derivations from limited-scope examples.

A toy construction may be recorded as:

```text
sample_derivation
diagnostic_example
compatibility_example
toy_support_construction
```

Such records may support claims like:

```text
this condition is not algebraically impossible
this profile satisfies the toy boundary condition
this diagnostic can detect the bad case
```

They must not by themselves support claims like:

```text
the physical mechanism is derived
the branch is licensed
the theorem target is satisfied
```

Reports must show sample scope visibly.

## Feature 20: Overlap And Double-Carrier Checks

VacuumForge must be able to represent claims about duplicate physical roles.

The system should support governance claims such as:

```text
these carriers overlap in scalar_trace role
this route risks double-counting source response
this field reintroduces a killed trace mode
```

A strong no-overlap or overlap-failure claim must be backed by an overlap witness.

Without a witness, the claim may be recorded as open risk or unresolved obligation, but not as a branch kill.

## Feature 21: Recovery-Target Leakage Governance

VacuumForge must distinguish deriving a coefficient from choosing a coefficient to match a recovery target.

A script must not claim a coefficient origin is derived if the coefficient was selected from a recovery requirement such as:

```text
gamma_like = 1
AB = 1
Schwarzschild recovery
GR wave-flux normalization
Lense-Thirring normalization
```

If a parameter is selected from a recovery target, the system should record a target-selection witness.

A target-selected parameter may still be useful phenomenologically, but it must not be reported as derived from the vacuum ontology.

## Feature 22: Archive-Aware Summary Reports

VacuumForge should produce reports that expose the repository’s epistemic ledger.

A useful summary must be able to answer:

```text
What was derived?
What was only sampled?
What was only inventoried?
What was rejected, and by what witness?
What was deferred, and pending which obligation?
What obligations remain open?
What claims were upgraded or downgraded?
What dependencies are stale, missing, superseded, or kind-mismatched?
What downstream assumptions rely on unarchived foundations?
```

Reports should not collapse these categories into a single pass/fail table.

## Feature 23: Downgrade Behavior

When a claim is unsupported for its requested strength, VacuumForge must prefer downgrade over false authority.

Examples:

```text
unsupported branch kill -> unproven exclusion
unsupported forbidden claim -> policy rule or open risk
unsupported derived status -> unverified claim
unsupported licensed route -> candidate route
sample used as derivation -> sample-only support warning
missing evidence object -> unsupported governance claim
open obligation used as solved -> unresolved prerequisite failure
```

The system should report both the requested status and the allowed status when it downgrades a claim.

## Feature 24: Non-Goals And Safety Boundaries

VacuumForge must not produce authoritative-looking validations for undefined objects.

If a script refers to a concept whose mathematical object is not defined well enough to validate, the correct behavior is to record an obligation, risk, placeholder, or memo-level note.

The system must avoid inventing validators for objects that are only prose names.

The system must not treat AI confidence, narrative cleanliness, or repeated prior wording as evidence.

The system must not allow summaries to become a substitute for derivations.

## Expected Behavioral Outcome

After this feature phase, a reader or downstream script should be able to tell whether a claim is:

```text
derived
assumed
matched
sampled
compatible in a toy setting
counterexample-backed
failed by witness
killed by contradiction
heuristic
policy-level
unresolved
deferred
not insertable yet
candidate only
licensed for downstream use
superseded
unverified
```

VacuumForge should make unsupported promotion difficult, visible, and reversible.

The desired result is not more positive verdicts. The desired result is better epistemic bookkeeping.

A goblin ledger is useful only if it says which coins are gold, which are painted rocks, which are debts, and which are dragons’ IOUs.
