# Candidate projection boundary and exterior neutrality
#
# Group:
#   20_no_overlap_and_projection_operators
#
# Script type:
#   REQUIREMENTS / DIAGNOSTIC
#
# Purpose
# -------
# Test whether projection can preserve boundary neutrality, exterior mass,
# and scalar silence without becoming a counterterm, shell source, far-zone
# patch, or recovery-tuned filter.
#
# Locked-door question:
#
#   Can O preserve boundary neutrality, M_ext, and exterior scalar silence?


from dataclasses import dataclass
from pathlib import Path
from typing import List

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    BranchDecisionRecord,
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    RecordKind,
    RouteRecord,
    ScriptOutput,
    StatusMark,
)


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


@dataclass
class BoundaryEntry:
    name: str
    candidate: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="projection_commutation_and_divergence_marker",
        upstream_script_id="020_no_overlap_and_projection_operators__candidate_projection_commutation_and_divergence",
        upstream_derivation_id="projection_commutation_and_divergence_marker",
    )
    return archive, ns, invalidated


def print_archive_status(ns, invalidated: bool) -> None:
    if invalidated:
        print("[INFO] Archive invalidated due to source change.")
    checks = ns.verify_dependencies()
    if not checks:
        print("[INFO] Archive dependencies: none declared.")
        return
    print("[INFO] Archive dependency check:")
    for check in checks:
        print(f"  - {check.dependency.dependency_id}: {check.status} ({check.message})")


def entry_status_mark(status: str) -> StatusMark:
    return {
        "CANDIDATE": StatusMark.INFO,
        "DEFER": StatusMark.DEFER,
        "RECOMMENDED": StatusMark.PASS,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "RISK": StatusMark.WARN,
        "SAFE_IF": StatusMark.INFO,
        "THEOREM_TARGET": StatusMark.DEFER,
        "UNRESOLVED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def build_entries() -> List[BoundaryEntry]:
    return [
        BoundaryEntry(
            name="B1: boundary/exterior-neutral projection target",
            candidate="O preserves boundary neutrality, M_ext, and exterior scalar silence",
            role="core exterior safety target",
            allowed_if="surface flux, mass neutrality, and scalar neutrality are derived",
            forbidden_if="projection cancels boundary failure after it appears",
            status="THEOREM_TARGET",
            missing="boundary flux theorem, M_ext theorem, scalar silence theorem",
            consequence="boundary-neutral projection remains theorem target",
        ),
        BoundaryEntry(
            name="B2: diagnostic-only boundary label",
            candidate="O labels interior/exterior evidence without modifying equations",
            role="safe fallback",
            allowed_if="label has no source, metric, or flux effect",
            forbidden_if="label becomes an active boundary filter",
            status="SAFE_IF",
            missing="none for diagnostic use",
            consequence="safe while active boundary projection remains deferred",
        ),
        BoundaryEntry(
            name="B3: compact-support structural projector",
            candidate="projected sector has structural zero flux at exterior boundary",
            role="promising candidate class",
            allowed_if="compact support is derived from the field law",
            forbidden_if="support cutoff is imposed to hide leakage",
            status="CANDIDATE",
            missing="support theorem and smooth matching law",
            consequence="candidate route for exterior scalar silence",
        ),
        BoundaryEntry(
            name="B4: trace-free exterior-neutral split",
            candidate="projected metric/source sector is trace-neutral outside the active domain",
            role="scalar silence route",
            allowed_if="trace neutrality follows from equations and boundary conditions",
            forbidden_if="trace is deleted to fix exterior scalar charge",
            status="THEOREM_TARGET",
            missing="exterior trace-neutrality theorem",
            consequence="scalar silence remains unproved",
        ),
        BoundaryEntry(
            name="B5: source-neutral boundary projector",
            candidate="O removes ordinary/exchange/curvature source overlap at the boundary",
            role="source routing target",
            allowed_if="source neutrality is derived before projection is applied",
            forbidden_if="boundary mismatch is relabeled as source routing",
            status="THEOREM_TARGET",
            missing="boundary source-routing theorem",
            consequence="source boundary neutrality remains theorem target",
        ),
        BoundaryEntry(
            name="B6: interior branch filter",
            candidate="O acts only as an admissibility filter for interior candidate branches",
            role="safe candidate use",
            allowed_if="filtered branches are not patched after recovery failure",
            forbidden_if="filter is tuned by exterior recovery",
            status="CANDIDATE",
            missing="branch admissibility criteria",
            consequence="usable only as pre-recovery diagnostic filter",
        ),
        BoundaryEntry(
            name="B7: boundary counterterm projection",
            candidate="O adds or selects counterterms to cancel boundary leakage",
            role="forbidden repair branch",
            allowed_if="never as repair",
            forbidden_if="counterterm is selected after leakage appears",
            status="REJECTED",
            missing="not pursued",
            consequence="projection cannot become a boundary counterterm",
        ),
        BoundaryEntry(
            name="B8: shell source from projection",
            candidate="projection produces a shell source at the matching surface",
            role="forbidden source shortcut",
            allowed_if="never without independent source law",
            forbidden_if="shell hides discontinuity or mass shift",
            status="REJECTED",
            missing="not pursued",
            consequence="projection cannot create shell matter",
        ),
        BoundaryEntry(
            name="B9: far-zone hidden flux projector",
            candidate="projection suppresses far-zone leakage or scalar tail",
            role="forbidden exterior patch",
            allowed_if="never as a patch",
            forbidden_if="tail is removed to preserve exterior recovery",
            status="REJECTED",
            missing="not pursued",
            consequence="far-zone silence must be derived, not filtered",
        ),
        BoundaryEntry(
            name="B10: recovery-tuned exterior projector",
            candidate="choose O so Schwarzschild/PPN/exterior recovery works",
            role="forbidden recovery shortcut",
            allowed_if="never",
            forbidden_if="recovery chooses boundary behavior",
            status="REJECTED",
            missing="not pursued",
            consequence="recovery remains downstream diagnostic",
        ),
        BoundaryEntry(
            name="B11: dark boundary patch",
            candidate="optional dark label absorbs boundary or exterior mismatch",
            role="forbidden optional-sector patch",
            allowed_if="never as repair",
            forbidden_if="dark label fixes ordinary-sector failure",
            status="REJECTED",
            missing="not pursued",
            consequence="dark sector remains optional downstream only",
        ),
        BoundaryEntry(
            name="B12: boundary neutrality decision",
            candidate="active boundary-neutral O remains deferred; diagnostic labels and compact-support candidates survive",
            role="current branch decision",
            allowed_if="future scripts keep exterior neutrality as obligation",
            forbidden_if="projection is used as boundary repair",
            status="RECOMMENDED",
            missing="surface flux, M_ext, scalar silence theorems",
            consequence="Group 20 can close with O still theorem-targeted",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Boundary and exterior projection problem")
    print("Question:")
    print()
    print("  Can O preserve boundary neutrality, M_ext, and exterior scalar silence?")
    print()
    print("Goal:")
    print()
    print("  prevent projection from becoming a boundary counterterm or exterior recovery patch")
    print()
    print("Discipline:")
    print()
    print("  no M_ext shift")
    print("  no exterior scalar charge")
    print("  no shell source from projection")
    print("  no far-zone hidden flux")
    print("  no recovery-tuned projection")
    print("  no dark boundary patch")
    with out.unresolved_obligations():
        out.line("boundary projection problem posed", StatusMark.OBLIGATION, "boundary-neutral O not yet derived")


def case_1_inventory(entries: List[BoundaryEntry]) -> None:
    header("Case 1: Boundary and exterior neutrality inventory")
    for entry in entries:
        print()
        print("-" * 120)
        print(entry.name)
        print("-" * 120)
        print(f"Candidate: {entry.candidate}")
        print(f"Role: {entry.role}")
        print(f"Allowed if: {entry.allowed_if}")
        print(f"Forbidden if: {entry.forbidden_if}")
        print(f"[{entry_status_mark(entry.status).value}] {entry.name}: {entry.status}")
        print(f"Missing: {entry.missing}")
        print(f"Consequence: {entry.consequence}")


def case_2_compact_table(entries: List[BoundaryEntry], out: ScriptOutput) -> None:
    header("Case 2: Compact boundary ledger")
    print("| Entry | Candidate | Status | Consequence |")
    print("|---|---|---|---|")
    for entry in entries:
        print(f"| {entry.name} | {entry.candidate} | {entry.status} | {entry.consequence} |")
    with out.governance_assessments():
        out.line("compact boundary projection ledger produced", StatusMark.INFO, "boundary-neutral O remains theorem target")


def case_3_status_counts(entries: List[BoundaryEntry], out: ScriptOutput) -> None:
    header("Case 3: Status counts")
    counts = {}
    for entry in entries:
        counts[entry.status] = counts.get(entry.status, 0) + 1
    for status in sorted(counts):
        print(f"{status}: {counts[status]}")
    print()
    print("Interpretation:")
    print("  Boundary/exterior-neutral projection remains theorem-targeted.")
    print("  Diagnostic labels and structurally compact-support candidates remain safe routes.")
    print("  Counterterm, shell, far-zone, recovery, and dark patches are rejected.")
    with out.governance_assessments():
        out.line("boundary projection status count produced", StatusMark.INFO, str(counts))


def case_4_surface_flux_check(out: ScriptOutput) -> None:
    header("Case 4: Surface flux diagnostic")
    r, R, A, phi0 = sp.symbols("r R A phi0", positive=True)
    tail = A / r
    compact = phi0 * (1 - r**2 / R**2) ** 2
    tail_flux = sp.simplify(4 * sp.pi * r**2 * sp.diff(tail, r))
    compact_flux_at_R = sp.simplify((4 * sp.pi * r**2 * sp.diff(compact, r)).subs(r, R))

    print("Exterior scalar-tail diagnostic:")
    print()
    print("  phi_tail = A/r")
    print(f"  4*pi*r^2*d(phi_tail)/dr = {tail_flux}")
    print()
    print("Compact-support toy diagnostic:")
    print()
    print("  phi_compact = phi0*(1 - r^2/R^2)^2")
    print(f"  [4*pi*r^2*d(phi_compact)/dr] at r=R = {compact_flux_at_R}")
    print()
    print("Interpretation:")
    print("  A 1/r exterior scalar tail carries nonzero surface flux.")
    print("  A compact-support toy can have zero boundary flux, but only as a diagnostic shape.")
    print("  A real theory must derive support and matching; projection cannot impose them after leakage appears.")
    with out.sample_results():
        out.line("exterior scalar tail has nonzero surface flux", StatusMark.PASS, f"tail flux = {tail_flux}")
        out.line("compact-support toy has zero boundary flux", StatusMark.PASS, f"boundary flux = {compact_flux_at_R}")
    with out.governance_assessments():
        out.line("surface flux diagnostic is not a boundary theorem", StatusMark.DEFER, "support and matching law missing")


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("Boundary/exterior projection fails if:")
    print()
    print("1. O shifts M_ext.")
    print("2. O hides exterior scalar charge.")
    print("3. O adds a boundary counterterm.")
    print("4. O creates a shell source at the matching surface.")
    print("5. O suppresses far-zone hidden flux.")
    print("6. O is tuned by Schwarzschild/PPN recovery.")
    print("7. O invokes a dark boundary patch.")
    print("8. O converts boundary mismatch into source-sector routing.")
    with out.counterexamples():
        out.line("boundary counterterm projection rejected", StatusMark.FAIL, "projection cannot repair leakage")
        out.line("shell source from projection rejected", StatusMark.FAIL, "projection cannot create matching-surface matter")
        out.line("far-zone hidden flux projector rejected", StatusMark.FAIL, "exterior silence must be derived")
        out.line("recovery-tuned exterior projector rejected", StatusMark.FAIL, "recovery remains downstream")
        out.line("dark boundary patch rejected", StatusMark.FAIL, "dark labels cannot patch ordinary boundary failure")


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Boundary/exterior-neutral projection is not solved.")
    print()
    print("Allowed status:")
    print()
    print("  diagnostic-only boundary labels remain safe")
    print("  compact-support and interior branch filters remain candidate classes")
    print("  trace-free exterior-neutral and source-neutral projectors remain theorem targets")
    print()
    print("Rejected:")
    print()
    print("  boundary counterterm projection")
    print("  shell source from projection")
    print("  far-zone hidden flux projector")
    print("  recovery-tuned exterior projector")
    print("  dark boundary patch")
    print()
    print("Missing before boundary-neutral O can be real:")
    print()
    print("  boundary flux theorem")
    print("  M_ext neutrality theorem")
    print("  exterior scalar silence theorem")
    print("  support and smooth matching law")
    print("  source boundary routing theorem")
    print()
    print("Possible next artifact:")
    print("  candidate_projection_boundary_and_exterior_neutrality.md")
    print()
    print("Possible next script:")
    print("  candidate_no_overlap_projection_group_status_summary.py")
    with out.governance_assessments():
        out.line("boundary-neutral O remains theorem target", StatusMark.DEFER, "surface flux and exterior neutrality laws missing")


def record_governance(ns) -> None:
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_boundary_neutral_O_20",
        script_id=SCRIPT_ID,
        title="Derive boundary-neutral projection operator",
        status=ObligationStatus.OPEN,
        required_by=["boundary_exterior_projection_route_20"],
        description="Define boundary behavior for O without counterterms, shell sources, or exterior patches.",
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_projection_M_ext_neutrality_20",
        script_id=SCRIPT_ID,
        title="Derive M_ext neutrality under projection",
        status=ObligationStatus.OPEN,
        required_by=["boundary_exterior_projection_route_20"],
        description="Show that projection does not shift exterior mass or move mass source outside the protected A-sector.",
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_projection_scalar_silence_20",
        script_id=SCRIPT_ID,
        title="Derive exterior scalar silence under projection",
        status=ObligationStatus.OPEN,
        required_by=["boundary_exterior_projection_route_20"],
        description="Prove that projection creates no exterior scalar tail or scalar trace leakage.",
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_projection_support_matching_20",
        script_id=SCRIPT_ID,
        title="Derive projection support and smooth matching",
        status=ObligationStatus.OPEN,
        required_by=["boundary_exterior_projection_route_20"],
        description="Derive compact support or smooth boundary matching from the field law, not by imposed cutoff.",
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_boundary_source_routing_20",
        script_id=SCRIPT_ID,
        title="Derive boundary source-routing neutrality",
        status=ObligationStatus.OPEN,
        required_by=["boundary_exterior_projection_route_20"],
        description="Show that boundary mismatch is not converted into ordinary, exchange, curvature, or dark source routing.",
    ))

    ns.record_route(RouteRecord(
        route_id="boundary_exterior_projection_route_20",
        script_id=SCRIPT_ID,
        name="Boundary/exterior-neutral projection theorem route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[
            "derive_boundary_neutral_O_20",
            "derive_projection_M_ext_neutrality_20",
            "derive_projection_scalar_silence_20",
            "derive_projection_support_matching_20",
            "derive_boundary_source_routing_20",
        ],
        activation_conditions=[
            "surface flux law is derived",
            "M_ext is unchanged by projection",
            "exterior scalar charge vanishes by theorem",
            "boundary source routing is neutral",
        ],
    ))
    ns.record_route(RouteRecord(
        route_id="diagnostic_boundary_label_route_20",
        script_id=SCRIPT_ID,
        name="Diagnostic-only boundary label fallback",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[],
        activation_conditions=[
            "boundary labels do not alter field equations",
            "labels are not used to claim exterior neutrality",
        ],
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_boundary_neutral_O_20",
        script_id=SCRIPT_ID,
        branch_id="boundary_exterior_neutral_projection",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "derive_boundary_neutral_O_20",
            "derive_projection_M_ext_neutrality_20",
            "derive_projection_scalar_silence_20",
            "derive_projection_support_matching_20",
            "derive_boundary_source_routing_20",
        ],
        description="Boundary-neutral O remains deferred until exterior mass, scalar silence, support, matching, and source-routing neutrality are derived.",
    ))
    for decision_id, branch_id, description in [
        (
            "reject_boundary_counterterm_projection_20",
            "boundary_counterterm_projection",
            "Reject projection that adds or selects boundary counterterms to cancel leakage.",
        ),
        (
            "reject_shell_source_from_projection_20",
            "shell_source_from_projection",
            "Reject projection-created shell sources at the matching surface.",
        ),
        (
            "reject_far_zone_hidden_flux_projector_20",
            "far_zone_hidden_flux_projector",
            "Reject projection that suppresses far-zone flux or scalar tails after the fact.",
        ),
        (
            "reject_recovery_tuned_exterior_projector_20",
            "recovery_tuned_exterior_projector",
            "Reject choosing boundary behavior from Schwarzschild, PPN, or exterior recovery.",
        ),
        (
            "reject_dark_boundary_patch_20",
            "dark_boundary_patch",
            "Reject optional dark labels as boundary or exterior repair patches.",
        ),
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=decision_id,
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            description=description,
        ))

    ns.record_claim(ClaimRecord(
        claim_id="projection_boundary_exterior_neutrality_summary",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.HEURISTIC,
        statement=(
            "Boundary/exterior-neutral projection is not solved. Diagnostic labels and compact-support "
            "candidates remain safe, but active projection cannot shift M_ext, hide scalar charge, create shell "
            "sources, tune recovery, or patch boundary failure."
        ),
        obligation_ids=[
            "derive_boundary_neutral_O_20",
            "derive_projection_M_ext_neutrality_20",
            "derive_projection_scalar_silence_20",
            "derive_projection_support_matching_20",
            "derive_boundary_source_routing_20",
        ],
    ))


def main():
    header("Candidate Projection Boundary And Exterior Neutrality")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    case_0_problem_statement(out)
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_surface_flux_check(out)
    case_5_failure_controls(out)
    final_interpretation(out)

    record_governance(ns)
    ns.record_derivation(
        derivation_id="projection_boundary_and_exterior_neutrality_marker",
        inputs=[],
        output=sp.Symbol("projection_boundary_and_exterior_neutrality_complete"),
        method="projection_boundary_and_exterior_neutrality",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
