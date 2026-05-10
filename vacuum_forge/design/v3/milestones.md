# VacuumForge Governance Validation Milestones

## Purpose

This document breaks the governance-validation technical design into implementation milestones.

The goal of this development phase is to extend VacuumForge from an algebra-validation workbench into a governance-aware research workbench. VacuumForge should continue to validate symbolic derivations, dependency chains, leaks, coordinate transformations, and concrete-metric checks. This phase adds the missing layer: machine-visible distinctions among derivations, samples, evidence, governance claims, proof obligations, branch decisions, route status, summaries, and script metadata.

The milestones are ordered so that each step leaves the codebase in a usable state. Early milestones add schemas and archive compatibility. Middle milestones add validation, dependency strengthening, and reporting. Later milestones add linting, runner/order checks, and script migration.

This is an implementation milestone plan, not a feature-specification document. Behavioral requirements live in `feature_design.md`; implementation detail lives in `technical_design.md`.

## Development Principles

The implementation should preserve existing VacuumForge behavior. Old derivation records, old dependency declarations, and old scripts should continue to load and run unless strict mode is explicitly requested.

The new governance layer should not replace the algebra layer. It should sit above it and make epistemic status explicit.

Strong claims should not be silently rejected by default during the migration period. They should be recorded with an effective downgraded status and a warning. Strict mode can turn unsupported Tier 3 claims into failures.

Every milestone below should include tests before being considered complete.

## Milestone GV-01: Governance Enum Skeleton

### Goal

Create the shared vocabulary for governance records without changing archive behavior yet.

### Deliverables

- New package directory at `src/vacuumforge/governance/`.
- `kinds.py` with `RecordKind`.
- `tiers.py` with `ClaimTier`.
- `statuses.py` with `GovernanceStatus`.
- `evidence.py` or `reasons.py` with `EvidenceType` and `ReasonCode`.
- `__init__.py` exporting the public enum set.
- Unit tests verifying enum values and string round-tripping.

### Required Capabilities

The codebase can import:

```python
from vacuumforge.governance import RecordKind, ClaimTier, GovernanceStatus
```

No existing code path should change behavior.

### Completion Criteria

- The new package imports cleanly.
- Enum values match the technical design vocabulary.
- Existing VacuumForge tests still pass.
- No archive schema changes are required yet.

### Notes

This milestone is deliberately small. It gives later milestones a stable vocabulary before archive records or validators depend on it.

## Milestone GV-02: Governance Record Dataclasses

### Goal

Define the new record types used by the governance layer, without storing them persistently yet.

### Deliverables

- `records.py` under `src/vacuumforge/governance/` or additions to `src/vacuumforge/archive/records.py`.
- `EvidenceRecord`.
- `ProofObligationRecord` and `ObligationStatus`.
- `ClaimRecord`.
- `BranchDecisionRecord`.
- `RouteRecord`.
- Optional `ArchiveRecordBase` for shared fields.
- Basic validation helpers for required IDs and enum coercion.

### Required Capabilities

A test can instantiate each record type with minimal fields and inspect its enum-backed status fields.

### Completion Criteria

- All record dataclasses instantiate successfully.
- Required fields are explicit.
- Optional symbolic fields can hold SymPy expressions.
- No persistent archive writes are added yet.
- Existing derivation records remain unchanged.

### Notes

Do not force the existing `DerivationRecord` to inherit from the new base record in this milestone. Backward compatibility should remain simple until serialization is ready.

## Milestone GV-03: Serialization Support For Governance Records

### Goal

Teach the archive serializer how to round-trip governance records and optional SymPy fields.

### Deliverables

- Serialization helpers for optional SymPy expressions.
- Enum serialization and deserialization helpers.
- JSON conversion helpers for every new governance record type.
- A new `archive/json_records.py` module, or equivalent, to avoid bloating `archive.py`.
- Tests for round-trip serialization of all governance record types.

### Required Capabilities

The following objects can round-trip through JSON:

```text
EvidenceRecord
ProofObligationRecord
ClaimRecord
BranchDecisionRecord
RouteRecord
```

Records containing `expression`, `expected`, `observed`, and `residual` SymPy fields should deserialize back to equivalent SymPy expressions.

### Completion Criteria

- Round-trip tests pass for all record types.
- Metadata remains JSON-safe.
- Optional symbolic fields can be absent.
- Old derivation serialization still works.

### Notes

This milestone should not add new archive directories yet. It only creates reliable JSON conversion utilities.

## Milestone GV-04: Archive Storage Directories For Governance Records

### Goal

Extend each archive script namespace so it can store governance records alongside derivations.

### Deliverables

- Per-script directories:

```text
evidence/
obligations/
claims/
branches/
routes/
```

- Lazy or eager directory creation in `ScriptNamespace`.
- Private file helpers similar to `_derivation_file`.
- Low-level atomic write/read helpers for the new record directories.
- Tests using a temporary archive root.

### Required Capabilities

A script namespace created through `ProjectArchive.script_namespace(script_id)` has paths for derivations and all governance record directories.

### Completion Criteria

- Archive namespace creation does not break old archives.
- New directories are created when needed.
- Existing derivation storage remains unchanged.
- Missing governance directories in old archives are tolerated.

### Notes

This milestone creates the storage shape but should not yet expose high-level recording APIs.

## Milestone GV-05: Archive APIs For Evidence And Proof Obligations

### Goal

Add the first useful governance archive APIs: evidence records and proof obligations.

### Deliverables

- `ScriptNamespace.record_evidence`.
- `ScriptNamespace.get_evidence`.
- `ScriptNamespace.list_evidence`.
- Convenience wrappers for common evidence types, if desired.
- `ScriptNamespace.record_obligation`.
- `ScriptNamespace.get_obligation`.
- `ScriptNamespace.list_obligations`.
- `ScriptNamespace.update_obligation_status`.
- Tests for writing, reading, listing, and updating obligations.

### Required Capabilities

A script can record an open proof obligation and later mark it satisfied by a derivation or evidence record.

Example behavior:

```text
record_obligation("derive_boundary_neutrality_theorem", status=OPEN)
update_obligation_status(..., status=SATISFIED, by="script:derivation")
```

### Completion Criteria

- Evidence records persist to JSON and load correctly.
- Proof obligation records persist to JSON and load correctly.
- Obligation status updates preserve or append simple history metadata.
- The archive can list open obligations.

### Notes

This milestone already makes “unless X is derived” machine-visible. It is one of the highest-value early milestones.

## Milestone GV-06: Archive APIs For Claims, Branch Decisions, And Routes

### Goal

Allow scripts to record governance claims, branch decisions, and candidate or licensed routes.

### Deliverables

- `ScriptNamespace.record_claim`.
- `ScriptNamespace.get_claim`.
- `ScriptNamespace.list_claims`.
- `ScriptNamespace.record_branch_decision`.
- `ScriptNamespace.get_branch_decision`.
- `ScriptNamespace.list_branch_decisions`.
- `ScriptNamespace.record_route`.
- `ScriptNamespace.get_route`.
- `ScriptNamespace.list_routes`.
- Tests for persistence and filtering.

### Required Capabilities

A script can record:

```text
an informational candidate route;
a constrained open-risk claim;
an exclusion-tier branch decision;
a licensing-tier route claim.
```

At this point, validation may still be permissive. Strong unsupported claims may be stored, but they should be visibly identifiable.

### Completion Criteria

- Claims, branch decisions, and routes round-trip through archive storage.
- Listing methods can filter by status or tier where applicable.
- Existing archive APIs remain backward compatible.

### Notes

Claim validation and downgrading happen in the next milestone. This milestone focuses on storage and retrieval.

## Milestone GV-07: Claim Validation And Downgrade Rules

### Goal

Implement the governance rules that distinguish supported claims from unsupported or over-strong claims.

### Deliverables

- `validation.py` under `src/vacuumforge/governance/`.
- `ClaimValidationResult`.
- `validate_claim_support`.
- `validate_branch_decision`.
- `validate_route`.
- `downgrade_unsupported_status`.
- Resolver protocol or adapter for archive lookups.
- Integration with `record_claim`, `record_branch_decision`, and `record_route`.

### Required Capabilities

The system applies these rules:

```text
Tier 1 informational claims need no evidence.
Tier 2 constrained claims need a reason or provenance.
Tier 3 exclusions need evidence or derivation support.
Tier 3 licensing claims need evidence or derivation support.
Sample-only support cannot license a route.
Unsupported branch kills downgrade to UNPROVEN_EXCLUSION.
Unsupported licensed claims downgrade to CANDIDATE_ROUTE.
```

### Completion Criteria

- Unsupported Tier 3 branch kills are downgraded.
- Supported Tier 3 branch kills remain strong.
- Tier 2 claims without provenance become `HEURISTIC` or `UNVERIFIED`.
- Licensed claims with only sample support downgrade.
- Validation results expose requested status and effective status.

### Notes

Default behavior should record and downgrade rather than throw. Strict behavior can be added later through CLI or environment controls.

## Milestone GV-08: Expected Output Dependency Verification

### Goal

Strengthen archive dependency checks so downstream scripts can depend on specific mathematical results, not merely marker existence.

### Deliverables

- Extend `DependencyDeclaration` with:

```text
expected_output
expected_status
expected_record_kind
allow_superseded
```

- Extend dependency JSON serialization.
- Extend `DependencyCheckResult` with actual/expected output, status, kind, and residual fields.
- Update `ScriptNamespace.verify_dependencies` to compare expected outputs using existing simplification/equivalence helpers.
- Tests for old and new dependency declarations.

### Required Capabilities

A downstream script can declare:

```text
I depend on upstream derivation X producing residual 0.
```

Verification should distinguish:

```text
dependency_satisfied
dependency_changed
dependency_missing
dependency_superseded
```

### Completion Criteria

- Existing dependency declarations without expected outputs still verify.
- Matching expected output verifies successfully.
- Changed expected output produces `dependency_changed` with residual evidence.
- Superseded records fail unless explicitly allowed.

### Notes

This milestone directly addresses the placeholder-marker problem and makes the archive more than a script-ran ledger.

## Milestone GV-09: Derivation Record Quality Classification

### Goal

Classify derivation records as contentful, placeholder, inventory marker, sample, or unknown.

### Deliverables

- `DerivationRecordQuality` enum.
- `classify_derivation_record(record)`.
- Optional `record_kind`, `scope`, `result_type`, `superseded_by`, and `is_placeholder` fields on `DerivationRecord`.
- Archive CLI display support can be deferred, but unit tests should exist now.

### Required Capabilities

The classifier identifies:

```text
inputs=[] and output=Symbol("..._stated") -> PLACEHOLDER
method contains inventory -> INVENTORY_MARKER
record_kind=SAMPLE_DERIVATION -> SAMPLE
inputs nonempty and non-placeholder output -> CONTENTFUL
```

### Completion Criteria

- Classifier tests cover the known patterns.
- Old derivation records are accepted.
- Placeholder classification is non-fatal.

### Notes

This classifier is later used by archive doctor, lint rules, and summaries.

## Milestone GV-10: Governance-Aware Output Helper

### Goal

Replace hand-rolled script status output with a shared helper that can emit `FAIL`, `OPEN`, `DEFER`, `MEMO`, and evidence/obligation marks.

### Deliverables

- `governance/output.py`.
- `StatusMark` enum.
- `OutputEvent` dataclass.
- `status_line(label, mark, detail, ...)` helper.
- Deprecated `pass_warn_line(label, ok, detail)` compatibility helper.
- Optional `ScriptOutput` block helper for derived results, governance assessments, and unresolved obligations.
- Tests for formatting and deprecation behavior.

### Required Capabilities

A script can emit:

```text
[PASS]
[FAIL]
[WARN]
[INFO]
[OPEN]
[DEFER]
[MEMO]
[EVIDENCE]
[OBLIGATION]
```

The primary API should not be boolean-only.

### Completion Criteria

- The new helper prints stable, parseable output.
- Boolean helper emits a deprecation warning.
- Existing scripts can gradually migrate without breaking.

### Notes

This milestone addresses the early-script problem where computed failures could only print as warnings.

## Milestone GV-11: Governance Manager In TheoryContext

### Goal

Expose governance operations inside `TheoryContext` for notebooks, demos, and in-memory workflows.

### Deliverables

- `governance/manager.py`.
- `GovernanceManager`.
- `TheoryContext.__init__` attaches `self.governance`.
- In-memory methods for claim, evidence, obligation, branch decision, and route records.
- Tests showing the manager works without a persistent archive.

### Required Capabilities

A user can call:

```python
ctx.governance.obligation(...)
ctx.governance.claim(...)
ctx.governance.evidence(...)
```

without needing `ProjectArchive`.

### Completion Criteria

- `TheoryContext` still initializes cleanly.
- Existing context tests pass.
- Governance manager can validate a claim using in-memory evidence.

### Notes

Do not make this manager the source of truth for cross-script dependencies. Persistent script workflows should still use `ProjectArchive` and `ScriptNamespace`.

## Milestone GV-12: Archive CLI Counts And Governance Listing

### Goal

Make the archive CLI aware of governance records.

### Deliverables

- Extend `vf archive list` to show counts for:

```text
derivations
evidence
obligations
claims
branches
routes
dependencies
```

- Show derivation quality where possible.
- Show open obligation counts.
- Show unsupported or downgraded claim counts.
- Tests for CLI output against a temporary archive.

### Required Capabilities

A user can inspect a script namespace and see whether it contains only derivation markers, actual evidence, open obligations, or branch decisions.

### Completion Criteria

- Old archive namespaces list correctly.
- New record counts appear when governance records exist.
- Placeholder derivations are visibly marked.

### Notes

This milestone is mostly observability. It makes the new data useful to humans before stricter verification lands.

## Milestone GV-13: Archive CLI Verification And Doctor Governance Checks

### Goal

Extend archive verification and doctor commands so unsupported governance claims become visible.

### Deliverables

- `vf archive verify --claims`.
- `vf archive verify --branches`.
- `vf archive verify --obligations`.
- `vf archive verify --strict`.
- Doctor checks for:

```text
claims referencing missing evidence;
branch decisions without required evidence;
open obligations marked satisfied without satisfying records;
superseded records still used by dependencies;
placeholder derivations in derivation-script namespaces;
summary claims stronger than upstream support, where detectable.
```

- Tests for each check.

### Required Capabilities

Archive verification can distinguish:

```text
valid claim support;
unsupported Tier 3 claim;
missing evidence reference;
open proof obligation;
superseded dependency.
```

Strict mode exits nonzero for unsupported Tier 3 claims.

### Completion Criteria

- Non-strict mode reports warnings without breaking old archives.
- Strict mode fails on unsupported Tier 3 claims.
- Doctor reports governance consistency issues.

### Notes

This milestone turns governance records into enforceable archive structure.

## Milestone GV-14: Archive Query Commands

### Goal

Add query commands that summary scripts and humans can use to inspect archive state.

### Deliverables

- `vf archive query obligations --status open`.
- `vf archive query claims --tier exclusion`.
- `vf archive query evidence --type overlap_witness`.
- `vf archive query branches --status rejected_route`.
- `ProjectArchive.query_claims`.
- `ProjectArchive.query_obligations`.
- `ProjectArchive.query_evidence`.
- `ProjectArchive.query_branch_decisions`.
- Tests for query filtering.

### Required Capabilities

A summary script can query open obligations and rejected routes from the archive instead of restating them from memory.

### Completion Criteria

- Query commands return stable machine-readable or human-readable output.
- Query methods work across multiple script namespaces.
- Missing record directories are tolerated.

### Notes

This milestone prepares for archive-generated handoff summaries.

## Milestone GV-15: Governance Summary Builder

### Goal

Generate summaries from structured upstream archive records rather than freehand status narration.

### Deliverables

- `governance/summaries.py`.
- `SummarySpec`.
- `GovernanceSummaryBuilder`.
- `GovernanceSummary` data object.
- Summary sections for:

```text
derived results;
sample results;
counterexamples;
governance claims;
branch decisions;
open obligations;
failed obligations;
superseded records;
unsupported claims.
```

- Tests using a temporary archive with mixed record kinds.

### Required Capabilities

A summary builder can consume several upstream script namespaces and produce a structured report of what is derived, what is open, what is only a sample, and what is unsupported.

### Completion Criteria

- Summary output does not silently promote samples to derivations.
- Open obligations are listed.
- Unsupported Tier 3 claims are listed separately.
- Old archives with only derivations still summarize.

### Notes

This is the first milestone that directly supports replacing memory-based group-ending status summaries.

## Milestone GV-16: Claim-Strength Upgrade Detection

### Goal

Detect when a summary or downstream script strengthens an upstream claim without new evidence.

### Deliverables

- Claim strength ordering.
- `check_claim_strength_upgrade`.
- `UpgradeCheckResult`.
- Integration into `GovernanceSummaryBuilder` or archive doctor.
- Tests for common upgrades:

```text
UNRESOLVED -> CANDIDATE
CANDIDATE_ROUTE -> LICENSED_CLAIM
THEOREM_TARGET-like claim -> DERIVED
SAMPLE_DERIVATION -> DERIVATION
UNPROVEN_EXCLUSION -> KILLED_BY_CONTRADICTION
```

### Required Capabilities

If a summary claim references upstream claims but is stronger than all of them and has no new evidence, the system flags a claim-strength upgrade.

### Completion Criteria

- Supported upgrades with new evidence pass.
- Unsupported upgrades are reported.
- Upgrade checks produce record references useful for debugging.

### Notes

This milestone addresses one of the most important AI-drift surfaces: summary scripts silently upgrading the strength of previous results.

## Milestone GV-17: Handoff Import Records

### Goal

Make group-to-group handoffs explicit and queryable.

### Deliverables

- `HandoffImportRecord`.
- Archive storage for handoff imports, either in `claims/` or a dedicated `handoffs/` directory.
- `record_handoff_import` and listing methods.
- Summary builder support for handoff imports.
- Tests for importing derived, sample, open, and unsupported records.

### Required Capabilities

A group-ending script can record what the next group is allowed to assume, with clear distinctions among:

```text
derived import;
sample-only import;
open obligation import;
unsupported claim import.
```

### Completion Criteria

- Handoff imports persist.
- Summary output shows import status.
- Unsupported or open imports are not displayed as licensed assumptions.

### Notes

This milestone can be delayed if summaries are not yet being migrated. It becomes important once group-ending scripts start depending on structured upstream claims.

## Milestone GV-18: vf-lint Skeleton And Existing Validation-Theater Rules

### Goal

Create the standalone linting tool and implement the original validation-theater checks.

### Deliverables

- `tools/vf_lint/` package.
- CLI entrypoint.
- AST parser and import collector.
- Verdict-site detector for:

```text
print("[PASS] ...")
status_line(...)
dataclass status fields
```

- Basic trace-back rules for literal versus computed conditions.
- Output formats: human-readable and JSON.
- Exit codes: 0 OK, 1 WARN, 2 FAIL.
- Fixtures for good and bad scripts.

### Required Capabilities

The tool can detect:

```text
unconditional PASS print;
status_line with literal True;
dataclass verdict literal;
missing validation imports in verdict-heavy script.
```

### Completion Criteria

- Known-good fixture passes.
- Known-bad closure-summary-style fixture fails.
- JSON output is parseable.
- The tool does not import VacuumForge internals unless explicitly designed to do so.

### Notes

This milestone implements the linting foundation. Governance-specific rules come next.

## Milestone GV-19: vf-lint Governance-Theater Rules

### Goal

Detect unsupported branch kills, forbidden/rejected claims, and hardcoded derivation/governance statuses.

### Deliverables

- `governance_rules.py`.
- Detection of strong words in string literals and dataclass fields.
- Detection of evidence-recording calls.
- Rules for:

```text
branch_kill_without_evidence;
forbidden_without_evidence;
rejected_without_evidence;
licensed_without_derivation_or_evidence;
hardcoded_derivation_status_without_provenance;
status_field_without_evidence_columns;
not_insertable_reported_as_killed.
```

- Tests for each rule.

### Required Capabilities

A script that hardcodes `status="BRANCH_KILLED"` without evidence fields or evidence-recording calls fails lint.

A script that records a branch decision with evidence IDs passes the corresponding rule.

### Completion Criteria

- Strong unsupported exclusion language is detected.
- Governance statuses with provenance are accepted.
- Heuristic/open-risk statuses are not over-penalized.
- Rule severities are configurable.

### Notes

This milestone targets AI governance drift directly.

## Milestone GV-20: vf-lint Archive Marker Rules

### Goal

Detect scripts that perform real symbolic computation but record only empty archive markers.

### Deliverables

- `archive_rules.py`.
- Detection of symbolic work calls:

```text
sp.simplify
is_zero
check_equal
sp.solve
sp.diff
euler_lagrange_1d
check_quadratic_positivity
check_concrete_metric
CoordinateChange
StructureSearchEngine.analyze
```

- Detection of placeholder archive calls:

```text
record_derivation(inputs=[], output=sp.Symbol("..._stated"))
```

- Rules for missing expected outputs in math-result dependencies.
- Tests for symbolic work plus placeholder marker.

### Required Capabilities

A script that simplifies or solves symbolic expressions and records only a placeholder derivation emits a warning.

Inventory scripts with explicit `INVENTORY_MARKER` record kind or inventory methods should be lower severity.

### Completion Criteria

- Placeholder-after-symbolic-work warning works.
- Inventory marker exception works.
- Expected-output-missing rule works for dependency declarations where a mathematical result is referenced.

### Notes

This milestone addresses the inverse of governance theater: real computation not being captured by the archive.

## Milestone GV-21: vf-lint Script Hygiene Rules

### Goal

Add lower-severity rules for recurring script hygiene issues that confuse downstream readers and AI passes.

### Deliverables

- Boolean `status_line(label, ok)` detection.
- Stale `# Suggested location:` header detection.
- Missing script metadata header detection for new scripts.
- Versioned script pair without supersession metadata detection where practical.
- Tests for each rule.

### Required Capabilities

The linter reports:

```text
boolean status helper cannot emit FAIL;
replace Suggested location with Group metadata;
script missing Script type header;
versioned script appears canonical without supersession marker.
```

### Completion Criteria

- Rules are low severity by default.
- Existing old scripts are not blocked unless strict lint configuration is enabled.
- New-script fixtures can enforce the stricter convention.

### Notes

These rules are cleanup aids, not proof machinery. They should not drown out evidence and claim-support issues.

## Milestone GV-22: Runner Failure Sentinel

### Goal

Make script execution failures visible in result files and console output.

### Deliverables

- Update the script runner if it is part of the repository.
- Nonzero script exits produce result files beginning with:

```text
[SCRIPT_FAILED]
exit_code=<code>
```

- Console summary shows a failure marker.
- Result-file scanner detects traceback or stderr sections.
- Tests using scripts that pass and fail.

### Required Capabilities

A failed script cannot look like a successful script merely because a result file exists.

### Completion Criteria

- Failed result files include the sentinel.
- Console output marks the script as failed.
- Existing successful result files are unchanged.

### Notes

This is outside core VF if the runner lives outside the package. It is still part of the development phase because archive markers can be absent when scripts fail.

## Milestone GV-23: order.txt Coverage Checker

### Goal

Validate group execution order files and catch orphan, duplicate, missing, or superseded scripts.

### Deliverables

- `vf-order-check` tool or equivalent script.
- Reads `order.txt` and group directory files.
- Checks:

```text
every .py file appears exactly once unless ignored;
every order entry exists;
summary scripts are last unless marked otherwise;
versioned scripts carry supersession metadata;
dependency declarations are roughly consistent with execution order, where detectable.
```

- Tests with fixture groups.

### Required Capabilities

A group with a missing script, duplicate script, stale order entry, or unmarked version pair produces a warning or failure.

### Completion Criteria

- Clean fixture group passes.
- Missing file fails.
- Duplicate entry fails.
- Versioned pair without supersession metadata warns.

### Notes

This tool should parse metadata comments, not execute scripts.

## Milestone GV-24: Script Metadata Standard

### Goal

Define and support stable script metadata so tools can distinguish derivation, audit, inventory, summary, memo, and sieve scripts.

### Deliverables

- Metadata parser for comments such as:

```text
# Group: 11_field_equation_closure
# Script type: DERIVATION
# Canonical: true
# Superseded by: candidate_parent_identity_template_v2.py
# Archive script id: candidate_parent_identity_template_v2
```

- Optional `record_script_metadata` archive method or integration with `write_run_metadata`.
- Lint support for missing or malformed metadata in new scripts.
- Tests for metadata parsing.

### Required Capabilities

Tools can determine whether a script is intended to be a derivation, sample, audit, requirements, summary, memo, or sieve script.

### Completion Criteria

- Metadata parser works without executing scripts.
- Archive can store parsed script metadata.
- `order.txt` checker can use metadata.
- Lint can warn on missing metadata.

### Notes

This milestone helps prevent `Status.DERIVED` markers in inventory scripts from being misread as mathematical derivations.

## Milestone GV-25: Pilot Retrofit — Group 09 Vector Scripts

### Goal

Apply the new archive and lint conventions to a concrete high-value group with known placeholder-marker issues.

### Deliverables

Retrofit selected Group 09 vector-sector scripts so that they:

```text
record actual symbolic inputs and outputs;
tag samples and diagnostics correctly;
replace boolean status helpers where practical;
add script metadata headers;
add expected_output dependencies where downstream scripts rely on specific results;
record obligations or governance claims only when appropriate.
```

Priority scripts include:

```text
vector_current_projection_operator
vector_curl_energy_field_equation
vector_transverse_current_projection
vector_source_shape_factor
```

### Required Capabilities

Running the retrofitted scripts produces contentful derivation records for identities such as projector idempotence, curl identities, divergence checks, or source-shape factors.

### Completion Criteria

- Placeholder derivation warnings are removed or intentionally downgraded to inventory markers.
- Contentful records appear in the archive.
- Dependencies using those results can specify expected outputs.
- vf-lint passes or only emits accepted legacy warnings.

### Notes

This is the first real migration test. Do not retrofit every group until this pilot shows that the new pattern is usable.

## Milestone GV-26: Pilot Retrofit — Group 10 Kappa Scripts

### Goal

Apply the new conventions to the kappa trace-response group, where governance and mathematical-result distinctions are both important.

### Deliverables

Retrofit selected Group 10 scripts such as:

```text
kappa_exterior_suppression_condition
kappa_constraint_projection_identity
kappa_boundary_layer_model
kappa_joint_minimum_energy_functional
```

Record:

```text
actual reciprocal-scaling residuals;
projection idempotence results;
boundary flux and net-charge outputs;
Euler-Lagrange equations;
proof obligations for unproved source laws or boundary-neutrality theorems;
sample tags for toy profiles.
```

### Required Capabilities

The archive distinguishes:

```text
contentful derivation;
sample profile;
open proof obligation;
governance claim;
unsupported exclusion.
```

### Completion Criteria

- Toy boundary profiles are not recorded as full mechanism derivations.
- Open source-law obligations are explicit.
- Strong branch decisions, if any, have evidence or are downgraded.
- Lint and archive doctor results are clean enough to guide further migration.

### Notes

This group is a good test of the “sample is not theorem” distinction.

## Milestone GV-27: Summary Script Migration Pilot

### Goal

Convert one group-ending summary script from freehand status narration into an archive-backed governance summary.

### Deliverables

- Choose one summary script from Group 10 or Group 11.
- Replace manually assembled core status tables with `GovernanceSummaryBuilder` output where possible.
- Record handoff imports for the next group.
- Add claim-strength upgrade checks.
- Tests or run logs showing the summary consumes upstream archive records.

### Required Capabilities

The summary script can list:

```text
contentful derived results;
sample-only results;
open obligations;
unsupported claims;
licensed handoff assumptions.
```

without manually upgrading upstream status.

### Completion Criteria

- Summary output is generated from archive state for core status claims.
- Freehand interpretation is clearly separated from archive-backed status.
- Claim-strength upgrades are detected or absent.

### Notes

This milestone proves whether archive-backed summaries are practical before wider migration.

## Milestone GV-28: Early-Group Foundation Gap Annotation

### Goal

Make the pre-archive foundation gap visible without forcing an immediate full retrofit of Groups 00–06.

### Deliverables

- A convention or record kind for `UNARCHIVED_FOUNDATION` or equivalent.
- Bridge records noting that later groups depend on pre-archive results.
- Optional script metadata updates for Groups 00–06.
- Documentation explaining the gap.

### Required Capabilities

The archive and summaries no longer imply that the dependency chain begins cleanly at Group 07. They can report that some foundational claims are pre-archive and not machine-verified.

### Completion Criteria

- Group 07 or bridge-level records identify pre-archive dependencies.
- Summaries expose the unarchived foundation gap.
- No requirement exists yet to retrofit every early script.

### Notes

This milestone is honest accounting. It prevents the archive from looking more complete than it is.

## Milestone GV-29: Strict Mode And Configuration

### Goal

Allow projects to opt into stronger enforcement once migration has progressed.

### Deliverables

- `VF_STRICT_GOVERNANCE=1` environment behavior where appropriate.
- CLI `--strict` support across archive verification and linting.
- Configuration for vf-lint rule severities.
- Tests showing default mode warns while strict mode fails.

### Required Capabilities

In default mode:

```text
unsupported Tier 3 claim -> downgraded and warned
placeholder marker -> warned
legacy metadata missing -> warned or ignored
```

In strict mode:

```text
unsupported Tier 3 claim -> failure
missing evidence for branch kill -> failure
placeholder marker after symbolic work -> configurable failure
```

### Completion Criteria

- Strict and non-strict behavior are tested.
- Old scripts remain runnable in default mode.
- New-script CI can opt into strict mode.

### Notes

Strict mode should not be the default until after pilot retrofits.

## Milestone GV-30: Documentation And Migration Guide

### Goal

Document the new governance workflow so future scripts use it consistently.

### Deliverables

- Developer guide for governance records.
- Examples for:

```text
contentful derivation;
sample derivation;
proof obligation;
evidence record;
branch decision;
candidate route;
archive-backed summary;
expected-output dependency.
```

- Migration checklist for old scripts.
- Lint rule reference.
- Archive CLI reference updates.

### Required Capabilities

A developer or AI assistant can write a new VF script and know:

```text
what to record;
which status to use;
when evidence is required;
how to avoid placeholder markers;
how to tag samples;
how to declare dependencies with expected outputs.
```

### Completion Criteria

- Documentation is committed alongside code.
- At least one migrated script is used as a reference example.
- The guide explains permissive versus strict mode.

### Notes

This milestone is last in the list but should be drafted incrementally as earlier milestones land.

## Recommended Implementation Order

The recommended order is:

```text
GV-01  Governance Enum Skeleton
GV-02  Governance Record Dataclasses
GV-03  Serialization Support
GV-04  Archive Storage Directories
GV-05  Evidence And Proof Obligation APIs
GV-06  Claims, Branches, Routes APIs
GV-07  Claim Validation And Downgrade Rules
GV-08  Expected Output Dependency Verification
GV-09  Derivation Record Quality Classification
GV-12  Archive CLI Counts And Listing
GV-13  Archive Verification And Doctor Checks
GV-10  Governance-Aware Output Helper
GV-18  vf-lint Skeleton
GV-19  vf-lint Governance Rules
GV-20  vf-lint Archive Marker Rules
GV-21  vf-lint Script Hygiene Rules
GV-23  order.txt Coverage Checker
GV-24  Script Metadata Standard
GV-25  Group 09 Pilot Retrofit
GV-26  Group 10 Pilot Retrofit
GV-15  Governance Summary Builder
GV-16  Claim-Strength Upgrade Detection
GV-17  Handoff Import Records
GV-27  Summary Script Migration Pilot
GV-28  Early-Group Foundation Gap Annotation
GV-22  Runner Failure Sentinel
GV-29  Strict Mode And Configuration
GV-30  Documentation And Migration Guide
```

`GV-11` can be implemented any time after `GV-07`, because it exposes the same concepts through `TheoryContext` but is not required for archive-first script migration.

`GV-22` depends on where the runner lives. If runner work is outside this package, it can proceed independently.

## Minimal Viable Cut

The smallest useful version of this phase is:

```text
GV-01 through GV-09
GV-12 through GV-13
GV-18 through GV-20
GV-25
```

That gives the project:

```text
governance records;
evidence and obligations;
claim validation and downgrades;
expected-output dependencies;
placeholder derivation detection;
archive visibility;
linting for governance theater;
one migrated script group proving the workflow.
```

Everything after that improves coverage, reporting, strictness, and migration quality.

## Full Completion Criteria For The Phase

This development phase is complete when:

1. VF can store derivations, samples, diagnostics, evidence, obligations, claims, branch decisions, routes, and handoff imports as distinct record kinds.
2. Strong governance claims require structured evidence or are downgraded.
3. Downstream dependencies can verify expected outputs, statuses, and record kinds.
4. Placeholder derivation records are visible and lintable.
5. Summary scripts can consume archive state rather than restating status from memory.
6. Claim-strength upgrades can be detected.
7. vf-lint catches validation theater, governance theater, and placeholder-marker patterns.
8. Script failures and order-file drift are visible to tooling.
9. At least two high-value groups have been retrofitted to record actual derivations and obligations.
10. Documentation explains how to write new governance-aware VF scripts.

## Final Note

This milestone plan intentionally separates schema, archive behavior, validation, linting, runner hygiene, and migration. The project should resist the temptation to jump directly into retrofitting all scripts before the record model and validation rules are stable.

The first goblin treasure is not a cleaner story. It is a better ledger.
