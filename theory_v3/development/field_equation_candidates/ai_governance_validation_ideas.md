# AI Governance Validation Ideas

## Motivation

These field-equation candidate scripts are being written by AI.

VacuumForge exists partly to prevent predictable AI failure modes:

- drift toward a cleaner story instead of a justified one
- lazy substitution of prose for derivation
- unsupported branch steering
- hidden coefficient fitting
- repeated output of result-like statements without machine-checkable backing

This concern is not abstract. The scripts visibly drifted toward just printing results. That is effectively the AI writing conclusions while the repository carries too little guarantee that those conclusions are backed by real algebra, real counterexamples, or real tracked proof obligations.

The danger is strongest in later groups, where the scripts increasingly say things like:

- "this branch is too risky unless X is derived"
- "do not use recovery targets to choose coefficients"
- "if overlap persists, kill the branch"

Those statements may be reasonable research instincts, but in an AI-authored repo they are dangerous unless they are formalized. Otherwise the model is just steering the search by preference and tone.

## Core Problem

Right now the repo has a better discipline for symbolic algebra than for branch governance.

VacuumForge can already help with:

- explicit derivation records
- dependency tracking
- leak detection
- concrete metric checks
- coordinate-change tracking

But it does not yet strongly distinguish:

- computed result
- mechanized exclusion
- policy warning
- heuristic preference
- unresolved proof obligation

That allows later scripts to print branch-kill or branch-defer language in a form that looks more final than the evidence warrants.

## Working Rule

These statements should not count as results unless they are backed by a machine-checkable artifact:

- "too risky unless X is derived"
- "do not use recovery targets to choose coefficients"
- "if overlap persists, kill the branch"

At minimum, they should be backed by one of:

1. a formal counterexample
2. a mechanized dependency leak
3. a duplicate-degree-of-freedom / overlap witness
4. a failed boundary-neutrality or conserved-quantity check
5. an explicit unresolved proof obligation tracked in the archive

If none of those exists, the script should not present the statement as an exclusion or kill condition.

## Better Status Discipline

Add statuses that separate non-derived governance from actual derivation:

- `HEURISTIC`
- `OPEN_RISK`
- `POLICY_RULE`
- `UNPROVEN_EXCLUSION`
- `UNRESOLVED_PROOF_OBLIGATION`

These should not be allowed to masquerade as:

- `DERIVED`
- `DERIVED_REDUCED`
- `BRANCH_KILLED`
- `FORBIDDEN`

unless evidence is attached.

## Proposed Evidence Model For Branch Claims

Branch-governance claims should require structured evidence objects.

Examples:

- `counterexample`
- `dependency_leak`
- `boundary_violation`
- `exterior_scalar_charge_witness`
- `target_selected_parameter`
- `overlap_witness`
- `recovery_precedes_origin`

If a script says a branch is killed, it should record at least one such witness.

If it does not, the strongest allowed output should be something like:

- `OPEN_RISK`
- `UNPROVEN_EXCLUSION`
- `DEFER`

## Specific Formal Checks Worth Adding

### 1. Recovery-Target Leakage Check

Represent rules like:

- coefficient origin must precede recovery checks
- `gamma_like = 1` cannot be used to choose a coefficient
- `AB -> 1` cannot be used to define an operator

Possible archive object:

- `forbid_target_selected(parameter="q", target="gamma_like=1")`

Possible failure artifact:

- `target_selected_parameter`

### 2. Overlap / Double-Carrier Check

Represent claims like:

- `B_s` and residual `zeta` cannot both carry the same scalar trace role
- `kappa` cannot reintroduce killed residual trace
- source routing cannot feed the same physical role twice

Possible archive object:

- `forbid_overlap(role="scalar_trace", carriers=[...])`

Possible failure artifact:

- `overlap_witness`

### 3. Branch-Kill Preconditions

Make `BRANCH_KILLED` require at least one structured reason:

- exterior scalar charge appears
- no-overlap cannot be satisfied
- coefficient remains free but is claimed derived
- only GR-copy / recovery-tuned routes survive

Possible archive object:

- `kill_if(exterior_scalar_charge)`
- `kill_if(unresolved_overlap)`
- `kill_if(recovery_precedes_origin)`

### 4. Proof Obligation Tracking

When a script says "unless X is derived", that should become a first-class tracked obligation.

Possible archive object:

- `requires_derivation("P_trace")`
- `requires_derivation("boundary neutrality theorem")`
- `requires_derivation("q-origin before recovery")`

Then downstream scripts can depend on the obligation status instead of prose.

## Hardcoded Dataclass Assessments

Group 08 scripts (and some in later groups) encode governance claims in
structured data rather than prose. For example:

    @dataclass
    class RequirementEntry:
        name: str
        status: str    # "SATISFIED_REDUCED", "PARTIAL", "MISSING"
        ...

    RequirementEntry(
        name="R1: Static scalar mass response",
        status="SATISFIED_REDUCED",
        ...
    )

The `status` field is hand-assigned, not computed. But because it lives
in a dataclass rather than a print statement, it looks like data -- a
downstream script iterating over a list of `RequirementEntry` objects
sees `status="SATISFIED_REDUCED"` with no way to distinguish it from
a machine-checked classification.

This is arguably more dangerous than prose governance because:

- it is structured and iterable, so automated tools will treat it as fact
- it does not carry any provenance (no link to the derivation that
  established the claim)
- it survives refactoring that might catch and question prose assertions

### Fix

Dataclass status fields that make derivation claims should either:

1. be populated by querying the archive (check whether the upstream
   derivation record exists and what its status is), or
2. carry explicit provenance linking to the derivation that backs them:

        RequirementEntry(
            name="R1: Static scalar mass response",
            status="SATISFIED_REDUCED",
            evidence_script="02_mechanics__candidate_static_spherical_exact_recovery",
            evidence_derivation="exact_schwarzschild_concrete_metric_check",
        )

3. use a governance-specific status (`ASSERTED_SATISFIED`, `UNVERIFIED`)
   when no archive link exists.

`vf-lint` could flag dataclass fields named `status` that contain
derivation-level values (`SATISFIED`, `DERIVED`, `FORBIDDEN`) without
a corresponding `evidence_script` or `evidence_derivation` field.

## Claim Severity Levels

Not all governance claims need the same evidence threshold.

"Next test selected: CONSTRAINED_BY_IDENTITY" is workflow direction --
it prioritizes but does not eliminate. "Branch killed: no viable route"
permanently removes a candidate from the search tree. These require
different levels of backing.

### Proposed severity tiers

**Tier 1 -- Informational (no evidence required):**
- workflow suggestions ("next test should be X")
- status summaries ("3 of 7 requirements satisfied")
- open questions ("does P_trace exist?")

**Tier 2 -- Constrained (rationale required):**
- risk flags ("this branch has unresolved overlap")
- priority ordering ("prefer route A over route B because...")
- deferred decisions ("postpone until X is derived")

Minimum backing: a named reason and a reference to the relevant script
or derivation. No formal witness needed.

**Tier 3 -- Exclusion (evidence required):**
- branch kills ("this route is eliminated")
- forbidden parameter values ("q cannot equal 1")
- coefficient rejections ("this coefficient is recovery-selected")

Minimum backing: at least one structured evidence object
(counterexample, overlap_witness, target_selected_parameter, etc.)

### Why this matters

Without severity levels, enforcing evidence on all governance claims
would generate noise on harmless tier-1 statements that buries the
cases where evidence actually matters. The enforcement should be
strict at tier 3, light at tier 2, and absent at tier 1.

## Better Linting For Governance Scripts

`vf-lint` currently targets validation-theater patterns in PASS-style scripts.

A second layer should look for governance-theater patterns, such as:

- branch-kill language without evidence object
- exclusion language without witness
- coefficient rejection language without dependency-direction check
- recovery-target language upstream of coefficient choice
- unsupported "forbidden", "rejected", or "killed" claims

This would be a direct response to AI drift, not a cosmetic style rule.

## Output Discipline For Future Script Pass

When a script only prints judgments, that should not be treated as a strong result.

Every strong conclusion should be tied to one of:

- explicit inputs
- explicit derived outputs
- explicit failed checks
- explicit unresolved obligations

Without that, the script is a memo, not a validated artifact.

## Process Improvements

These are not tied to one specific directory. They are recurring process
gaps in how the script tree is being generated, summarized, and handed
forward.

### 1. Summary scripts should consume archive state, not restate it from memory

Status-summary scripts are useful editorially, but they are also a major
drift surface:

- the summary can silently diverge from upstream scripts
- statuses can be upgraded or softened by narration
- downstream readers may trust the summary more than the derivations

Better pattern:

- summary scripts should query archive derivations and dependency status
- they may add interpretation, but the core status table should be built
  from upstream records
- if a summary wants to escalate a claim, it should add a new evidence
  object rather than just stronger wording

### 2. Governance tables need explicit provenance columns

Many scripts encode governance claims in dataclass tables. That is
readable, but it still lets AI assign `status="REJECTED"` or
`status="THEOREM_TARGET"` directly by hand.

Minimal improvement:

- add `evidence_script`
- add `evidence_derivation`
- add `claim_tier`
- add `claim_kind` (`derived`, `heuristic`, `policy`, `target`, `failure_mode`)

If those fields are missing, the status should not be interpreted as
machine-backed.

### 3. Separate script output into three blocks

A better default script structure would be:

1. `derived_results`
2. `governance_assessments`
3. `unresolved_obligations`

Right now these are often interleaved, which makes it too easy for a
reader to confuse:

- "we computed this"
- "we prefer this"
- "this is still missing"

The archive should mirror this split.

### 4. Common helpers should replace hand-rolled status vocabularies

Each script currently hand-defines `status_line(...)` with a local map.
That is a direct AI drift surface:

- inconsistent tags (`INFO` vs `PASS`)
- silent vocabulary changes
- accidental promotion/demotion of claim severity

VacuumForge should provide a shared helper for:

- allowed statuses
- allowed claim tiers
- whether evidence is required
- how unsupported strong claims are downgraded

This is not just cleanup. It reduces the number of places where the AI
can improvise governance semantics.

### 5. Every branch-kill or rejection should have a first-class reason code

Useful rejections should be emitted with standardized reason codes rather
than only English prose, for example:

- `reason_code="recovery_selected_parameter"`
- `reason_code="gr_copy_construction"`
- `reason_code="boundary_repair_after_failure"`
- `reason_code="double_counting_without_overlap_witness"`

That would let linting and summaries detect unsupported exclusions
automatically.

### 6. Scripts need a "memo mode" when no derivation exists

Some scripts are genuinely exploratory sieves. That is fine.
The problem is that a sieve can still print strong-looking output.

Process improvement:

- scripts with no derivation records beyond inventory markers should be
  explicitly labeled `MEMO` or `SIEVE`
- their statuses should default to governance/heuristic tiers
- they should not be allowed to emit `DERIVED`, `FORBIDDEN`, or
  `BRANCH_KILLED` unless they attach evidence

This would make it obvious when a script is organizing thought rather
than proving something.

### 7. Validate `order.txt` coverage automatically

At this point each group depends heavily on execution order and on the
assumption that `order.txt` lists the real chain.

This should be checked automatically:

- every `.py` script in a group appears in `order.txt` exactly once
- no `order.txt` entry points to a missing file
- dependency declarations are consistent with the previous script in order
- status-summary scripts are last unless explicitly marked otherwise

This would catch orphan scripts, stale filenames, and accidental chain
breaks before a narrative summary starts depending on the wrong artifact.

### 8. Make sample derivations explicitly typed as samples

Later groups benefit from toy symbolic checks:

- compact-support boundary profiles
- finite integrability samples
- nonnegative diagnostic-density samples

These are useful, but they are not theorem support for the real physics
branch by themselves.

The archive and output should distinguish:

- `DERIVATION`
- `SAMPLE_DERIVATION`
- `COUNTEREXAMPLE`
- `DIAGNOSTIC_EXAMPLE`

Without that distinction, a clean toy profile can be mistaken for
evidence that the actual mechanism has been derived.

### 9. Handoff summaries should be generated from structured upstream claims

Many groups end with status-summary scripts that re-state:

- what is unresolved
- what is rejected
- what the next group may assume

Those handoffs should be built from structured upstream claims instead
of freehand re-summarization. In particular:

- unresolved obligations should be queried from the archive
- rejected mechanisms should carry machine-readable reason codes
- handoff assumptions should be listed explicitly as imports for the next group

That would reduce the risk that a later group silently upgrades a
theorem target into a working assumption.

### 10. Distinguish "candidate route" from "licensed route"

Scripts repeatedly use language like:

- candidate safe route
- safest fallback
- theorem target

Those are not the same.

The process should explicitly track at least:

- `candidate_route`
- `provisional_convention`
- `licensed_claim`
- `deferred_route`
- `rejected_route`

Right now the scripts rely on prose to convey this difference. A later AI
can easily collapse "candidate" into "working mechanism" if the status
system does not make the distinction first-class.

### 11. Summary scripts should check for claim-strength upgrades

Group-ending summary scripts are one of the easiest places for AI drift
to hide. A summary can take upstream results like:

- `THEOREM_TARGET`
- `UNRESOLVED`
- `CANDIDATE`

and silently restate them as if they were stronger:

- "licensed"
- "required mechanism"
- "best explanation"

without any new derivation appearing in the archive.

The summary layer should therefore compare its outgoing claims against
the strongest status actually supported upstream. A summary should not be
allowed to upgrade:

- `UNRESOLVED -> CANDIDATE`
- `CANDIDATE -> LICENSED`
- `THEOREM_TARGET -> DERIVED`

unless it attaches a new evidence object or derivation.

### 12. Optional branches should default to absent, not latent

When a script explores an optional branch such as a dark-sector coupling,
the safest default is absence, not a vaguely "waiting in the wings"
latent mechanism.

Otherwise AI-written scripts start to speak as if the branch is already
part of the theory and only needs activation later.

A better rule:

- optional branch absent by default
- optional branch may become `candidate_route` only with explicit
  activation conditions
- optional branch may become `licensed_claim` only with evidence

This is especially important for speculative couplings that can easily be
used as repair patches.

### 13. Compatibility examples need explicit scope tags

Some scripts benefit from a toy symbolic check showing that a condition is
compatible in principle:

- divergence-free tangential flow
- compact-support boundary neutrality
- finite integrability sample

These are useful, but they are not the same as deriving the real branch.

The output and archive should make the scope explicit:

- `compatibility_example`
- `sample_profile`
- `toy_support_construction`

and should not let those records promote a theorem target into a
mechanism claim. This is the same principle as distinguishing
`SAMPLE_DERIVATION` from `DERIVATION`, but applied specifically to
scripts that test whether a claimed neutrality or safety condition is
even coherent.

## Practical Rule For Next Pass

For the next script pass:

- if the branch is killed by computation, record the computation
- if the branch is killed by contradiction, record the contradiction
- if the branch is only being deprioritized, say so plainly
- do not let branch preference print as theorem language

## Real Derivations Recorded As Markers

Many scripts perform genuine symbolic computation -- verifying identities,
solving equations, checking boundary conditions -- but record only generic
archive markers with empty inputs and placeholder symbol outputs.

The archive call typically looks like:

    ns.record_derivation(
        derivation_id="some_script_marker",
        inputs=[],
        output=sp.Symbol("some_script_stated"),
        method="some_script_inventory",
        status=Status.DERIVED,
    )

This records that the script ran, not what it proved. A downstream script
or audit tool can check that the marker exists, but cannot verify that the
mathematical result is unchanged.

This is the inverse of the governance problem above. The governance problem
is conclusions presented without computation. The marker problem is
computation performed without recording its content.

### Where This Appears

Identified during the v2 archive retrofit review of groups 08-15. Examples:

**Group 09** (vector sector):
- `vector_current_projection_operator`: verifies P_T^2 = P_T,
  P_T + P_L = I, P_T * P_L = 0 -- records empty marker
- `vector_curl_energy_field_equation`: verifies curl-curl identity --
  records empty marker
- `vector_transverse_current_projection`: verifies curl(grad) = 0,
  div(curl) = 0 -- records empty marker
- `vector_source_shape_factor`: computes M = 4*pi*rho*R^3/3,
  J = 2*M*R^2*Omega/5, verifies div(j) = 0 -- records empty marker

**Group 10** (kappa trace response):
- `kappa_exterior_suppression_condition`: verifies kappa=0 gives AB=1
  (the same reciprocal_scaling that ConcreteMetricCheck classifies) --
  records empty marker
- `kappa_constraint_projection_identity`: verifies projection
  idempotence -- records empty marker
- `kappa_boundary_layer_model`: verifies zero boundary flux and zero net
  charge -- records empty marker
- `kappa_joint_minimum_energy_functional`: computes Euler-Lagrange
  equation -- records empty marker

Groups 01-07 were reviewed before this pattern was identified and have not
been audited.

### What A Fix Looks Like

The infrastructure already supports richer records. Some later scripts
(groups 11-15) demonstrate the corrected pattern:

    ns.record_derivation(
        derivation_id="trace_tt_linear_volume_split",
        inputs=[pure_trace_metric, h_tt],
        output=delta_zeta,
        method="symbolic_perturbation",
        status=Status.DERIVED,
    )

The fix is mechanical: replace `inputs=[]` and `output=sp.Symbol("..._stated")`
with the actual symbolic expressions the script computed.

### What This Enables

Recording actual inputs and outputs lets the archive:

1. detect when a script's mathematical result changes (the output expression
   differs from the previous run)
2. let downstream scripts declare expected outputs and verify them
   (closing the `expected_output=None` gap in dependency checks)
3. distinguish scripts that verify identities from scripts that only
   classify inventory items
4. support a future audit mode that re-derives results from recorded
   inputs and compares against recorded outputs

### Proposed Upgrade Path

1. Audit groups 01-07 for the same pattern (not yet done).
2. For each script with real symbolic checks, replace the empty marker
   with the actual computed expressions.
3. Add `expected_output` to dependency declarations where the downstream
   script depends on a specific mathematical result, not just the
   existence of a marker.
4. Extend vf-lint to flag `record_derivation` calls with `inputs=[]`
   in scripts that contain `is_zero`, `sp.simplify`, or `sp.solve`
   calls -- these are likely computing something worth recording.

### Relationship To Governance Problem

The governance problem and the marker problem are two faces of the same gap:

- Governance problem: the script claims something it did not compute.
  Fix: require evidence objects for strong claims.
- Marker problem: the script computes something it did not claim.
  Fix: record the computation in the derivation.

Both problems weaken the archive's value as a machine-checkable proof
record. Fixing both would make the archive carry the full content of
what was derived and the full basis of what was decided.

## Immediate Development Direction

VacuumForge should grow beyond algebra validation into governance validation.

The next layer of support should cover:

- proof obligations
- forbidden dependency directions
- overlap witnesses
- branch-kill evidence
- stronger distinctions between derivation and policy

That is the missing safeguard for an AI-authored field-equation search tree.
