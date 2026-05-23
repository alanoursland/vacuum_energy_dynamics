# Candidate no-overlap operator minimum burden
#
# Group:
#   25_residual_kill_or_no_overlap_theorem
#
# Script type:
#   REQUIREMENTS / DIAGNOSTIC
#
# Purpose
# -------
# Define the minimum structure an active no-overlap operator O would require
# before it can remove residual overlap.
#
# Locked-door question:
#
#   What minimum structure would active O need before it can remove overlap?
#
# This script does not derive active O.
# It does not derive residual kill.
# It does not derive non-metric inertness.
# It does not derive B_s/F_zeta insertion.
# It does not open parent equation closure.
#
# It records that active O remains unavailable unless this structure is derived.

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


def status_mark(status: str) -> StatusMark:
    return {
        "BLOCKED": StatusMark.FAIL,
        "DIAGNOSTIC_ONLY": StatusMark.INFO,
        "NOT_READY": StatusMark.DEFER,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "SAFE_IF": StatusMark.INFO,
        "THEOREM_TARGET": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "residual_problem_dep_25",
            "025_residual_kill_or_no_overlap_theorem__candidate_residual_kill_problem_ledger",
            "residual_kill_problem_ledger_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "classification_dep_25",
            "025_residual_kill_or_no_overlap_theorem__candidate_metric_trace_residual_classification",
            "metric_trace_residual_classification_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "reentry_dep_25",
            "025_residual_kill_or_no_overlap_theorem__candidate_residual_reentry_exclusion_audit",
            "residual_reentry_exclusion_marker_25",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g20_summary_dep_25",
            "020_no_overlap_and_projection_operators__candidate_no_overlap_projection_group_status_summary",
            "no_overlap_projection_group_status_summary_marker",
            RecordKind.INVENTORY_MARKER,
        ),
    ]

    for dependency_id, upstream_script_id, upstream_derivation_id, expected_record_kind in dependencies:
        ns.declare_dependency(
            dependency_id=dependency_id,
            upstream_script_id=upstream_script_id,
            upstream_derivation_id=upstream_derivation_id,
            expected_record_kind=expected_record_kind,
        )

    return archive, ns, invalidated


def ensure_archive_write_dirs(ns) -> None:
    for attr in (
        "routes_path",
        "branch_decisions_path",
        "claims_path",
        "obligations_path",
        "derivations_path",
        "governance_path",
    ):
        path_obj = getattr(ns, attr, None)
        if path_obj is not None:
            path_obj.mkdir(parents=True, exist_ok=True)


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


@dataclass
class OStructureLedger:
    domain: sp.Symbol
    codomain: sp.Symbol
    kernel: sp.Symbol
    image: sp.Symbol
    idempotence: sp.Symbol
    composition: sp.Symbol
    pairing: sp.Symbol
    orthogonality: sp.Symbol
    derivative_behavior: sp.Symbol
    divergence_behavior: sp.Symbol
    boundary_behavior: sp.Symbol
    source_behavior: sp.Symbol
    mass_behavior: sp.Symbol
    scalar_tail_behavior: sp.Symbol
    current_flux_behavior: sp.Symbol
    support_matching_behavior: sp.Symbol
    recovery_independence: sp.Symbol
    missing_structure_load: sp.Expr


@dataclass
class ORequirement:
    name: str
    requirement: str
    status: str
    failure_if: str
    consequence: str


@dataclass
class ORoute:
    name: str
    route: str
    status: str
    allowed_if: str
    rejected_if: str


@dataclass
class RejectedOShortcut:
    name: str
    shortcut: str
    forbidden_use: str
    status: str
    consequence: str


def build_ledger() -> OStructureLedger:
    names = (
        "domain codomain kernel image idempotence composition pairing orthogonality "
        "derivative_behavior divergence_behavior boundary_behavior source_behavior mass_behavior "
        "scalar_tail_behavior current_flux_behavior support_matching_behavior recovery_independence"
    )
    (
        domain,
        codomain,
        kernel,
        image,
        idempotence,
        composition,
        pairing,
        orthogonality,
        derivative_behavior,
        divergence_behavior,
        boundary_behavior,
        source_behavior,
        mass_behavior,
        scalar_tail_behavior,
        current_flux_behavior,
        support_matching_behavior,
        recovery_independence,
    ) = sp.symbols(names, real=True)

    # This is a burden ledger, not a theorem.
    # Each symbol represents a missing required structure item.
    missing_structure_load = sp.simplify(
        domain
        + codomain
        + kernel
        + image
        + idempotence
        + composition
        + pairing
        + orthogonality
        + derivative_behavior
        + divergence_behavior
        + boundary_behavior
        + source_behavior
        + mass_behavior
        + scalar_tail_behavior
        + current_flux_behavior
        + support_matching_behavior
        + recovery_independence
    )

    return OStructureLedger(
        domain=domain,
        codomain=codomain,
        kernel=kernel,
        image=image,
        idempotence=idempotence,
        composition=composition,
        pairing=pairing,
        orthogonality=orthogonality,
        derivative_behavior=derivative_behavior,
        divergence_behavior=divergence_behavior,
        boundary_behavior=boundary_behavior,
        source_behavior=source_behavior,
        mass_behavior=mass_behavior,
        scalar_tail_behavior=scalar_tail_behavior,
        current_flux_behavior=current_flux_behavior,
        support_matching_behavior=support_matching_behavior,
        recovery_independence=recovery_independence,
        missing_structure_load=missing_structure_load,
    )


def build_requirements() -> List[ORequirement]:
    return [
        ORequirement(
            name="O1: domain",
            requirement="define what objects O acts on",
            status="REQUIRED",
            failure_if="O erases unspecified residuals",
            consequence="operator action is undefined",
        ),
        ORequirement(
            name="O2: codomain",
            requirement="define where O sends projected objects",
            status="REQUIRED",
            failure_if="O output has no declared sector/status",
            consequence="residual may re-enter under output label",
        ),
        ORequirement(
            name="O3: kernel",
            requirement="define what O kills",
            status="REQUIRED",
            failure_if="killed objects are named but not structurally characterized",
            consequence="residual kill by declaration returns",
        ),
        ORequirement(
            name="O4: image",
            requirement="define what O preserves",
            status="REQUIRED",
            failure_if="surviving image can still carry trace/source/load",
            consequence="overlap remains possible",
        ),
        ORequirement(
            name="O5: projection / idempotence law",
            requirement="derive O^2 = O or the correct replacement law",
            status="REQUIRED",
            failure_if="repeated application changes the residual status",
            consequence="projection is not well-defined",
        ),
        ORequirement(
            name="O6: composition law",
            requirement="derive how O composes with insertion, residual split, boundary, source, and support maps",
            status="REQUIRED",
            failure_if="composition creates hidden reentry",
            consequence="O becomes context-dependent eraser",
        ),
        ORequirement(
            name="O7: measure / pairing",
            requirement="define the pairing or measure under which no-overlap is meaningful",
            status="REQUIRED",
            failure_if="overlap has no mathematical criterion",
            consequence="no-overlap is just a name",
        ),
        ORequirement(
            name="O8: orthogonality / no-overlap criterion",
            requirement="derive the actual zero-overlap condition",
            status="REQUIRED",
            failure_if="overlap is assumed absent",
            consequence="count-once theorem is smuggled",
        ),
        ORequirement(
            name="O9: derivative / divergence behavior",
            requirement="derive how O behaves under derivatives and divergence",
            status="REQUIRED",
            failure_if="projected residuals reappear after differentiation",
            consequence="field equation consistency fails",
        ),
        ORequirement(
            name="O10: boundary behavior",
            requirement="derive boundary behavior of O-projected residuals",
            status="REQUIRED",
            failure_if="O creates boundary flux, scalar tail, current flux, or shell/source load",
            consequence="boundary/scalar silence fails",
        ),
        ORequirement(
            name="O11: source / mass behavior",
            requirement="derive source and mass behavior of O-projected residuals",
            status="REQUIRED",
            failure_if="O shifts A-sector mass or duplicates ordinary source load",
            consequence="source/mass guardrails fail",
        ),
        ORequirement(
            name="O12: support / matching behavior",
            requirement="derive support, smoothing, transition, and matching behavior",
            status="REQUIRED",
            failure_if="O hides residuals in support or transition layer",
            consequence="smooth support guardrails fail",
        ),
        ORequirement(
            name="O13: recovery independence",
            requirement="derive O without selecting it from Schwarzschild/gamma/AB/B=1/A/PPN recovery",
            status="REQUIRED",
            failure_if="recovery target chooses O",
            consequence="O becomes recovery smuggling",
        ),
    ]


def build_routes() -> List[ORoute]:
    return [
        ORoute(
            name="R1: real active no-overlap O",
            route="O removes residual overlap with full operator structure",
            status="THEOREM_TARGET",
            allowed_if="all domain/codomain/kernel/image/composition/divergence/boundary/source/support/recovery requirements are derived",
            rejected_if="any required structure is missing",
        ),
        ORoute(
            name="R2: O as diagnostic placeholder",
            route="O appears only as future theorem placeholder",
            status="SAFE_IF",
            allowed_if="used only to list missing structure and not to erase residuals",
            rejected_if="used to close L_double",
        ),
        ORoute(
            name="R3: O eraser by name",
            route="O deletes residual overlap because it is called no-overlap",
            status="REJECTED",
            allowed_if="never",
            rejected_if="operator structure is absent",
        ),
        ORoute(
            name="R4: recovery-selected O",
            route="O chosen to make gamma/AB/Schwarzschild recovery work",
            status="REJECTED",
            allowed_if="never",
            rejected_if="recovery target chooses operator action",
        ),
    ]


def build_rejected_shortcuts() -> List[RejectedOShortcut]:
    return [
        RejectedOShortcut(
            name="S1: unnamed domain",
            shortcut="O acts on whatever residual is inconvenient",
            forbidden_use="operator domain is undefined",
            status="REJECTED",
            consequence="O becomes universal eraser",
        ),
        RejectedOShortcut(
            name="S2: unnamed kernel",
            shortcut="O kills the overlap without kernel definition",
            forbidden_use="kernel is not derived",
            status="REJECTED",
            consequence="residual kill by declaration returns",
        ),
        RejectedOShortcut(
            name="S3: no pairing",
            shortcut="no-overlap asserted without measure/pairing",
            forbidden_use="overlap criterion is absent",
            status="REJECTED",
            consequence="orthogonality is meaningless",
        ),
        RejectedOShortcut(
            name="S4: no divergence behavior",
            shortcut="O projection ignores derivative/divergence behavior",
            forbidden_use="projected residual can reappear in field equations",
            status="REJECTED",
            consequence="operator is not field-equation compatible",
        ),
        RejectedOShortcut(
            name="S5: boundary/source blind O",
            shortcut="O ignores boundary, source, mass, scalar-tail, current-flux, and support behavior",
            forbidden_use="operator breaks downstream guardrails",
            status="REJECTED",
            consequence="residual cleanup becomes repair route",
        ),
        RejectedOShortcut(
            name="S6: parent from O",
            shortcut="active O opens parent equation",
            forbidden_use="operator burden is treated as parent identity",
            status="REJECTED",
            consequence="parent closure is smuggled",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: No-overlap operator minimum burden problem")
    print("Question:")
    print()
    print("  What minimum structure would active O need before it can remove overlap?")
    print()
    print("Reference discipline:")
    print()
    print("  O cannot erase overlap by name.")
    print("  If active O is used, it must be a real operator with domain, codomain, kernel, image, composition, pairing, divergence, boundary, source, support, and recovery-independence behavior.")
    print("  This script defines the burden; it does not derive O.")

    with out.governance_assessments():
        out.line(
            "no-overlap operator minimum burden audit opened",
            StatusMark.INFO,
            "defining minimum structure required before active O can remove residual overlap",
        )


def case_1_structure_ledger(ledger: OStructureLedger, out: ScriptOutput) -> None:
    header("Case 1: Active O missing-structure ledger")
    print("Required active-O structure items:")
    print()
    for name in [
        "domain",
        "codomain",
        "kernel",
        "image",
        "idempotence",
        "composition",
        "pairing",
        "orthogonality",
        "derivative_behavior",
        "divergence_behavior",
        "boundary_behavior",
        "source_behavior",
        "mass_behavior",
        "scalar_tail_behavior",
        "current_flux_behavior",
        "support_matching_behavior",
        "recovery_independence",
    ]:
        print(f"  {name} = {sp.sstr(getattr(ledger, name))}")
    print()
    print("Missing-structure load:")
    print()
    print(f"  L_O_missing = {sp.sstr(ledger.missing_structure_load)}")
    print()
    print("Interpretation:")
    print()
    print("  Active O is unavailable while this burden is unmet.")
    print("  O may be a placeholder only, not a residual eraser.")

    with out.derived_results():
        out.line(
            "active O missing-structure burden stated",
            StatusMark.OBLIGATION,
            f"L_O_missing = {sp.sstr(ledger.missing_structure_load)}",
        )


def case_2_requirements(requirements: List[ORequirement], out: ScriptOutput) -> None:
    header("Case 2: Active O minimum requirements")
    for req in requirements:
        print()
        print("-" * 120)
        print(req.name)
        print("-" * 120)
        print(f"Requirement: {req.requirement}")
        print(f"[{status_mark(req.status).value}] {req.name}: {req.status}")
        print(f"Failure if: {req.failure_if}")
        print(f"Consequence: {req.consequence}")

    with out.unresolved_obligations():
        out.line(
            "active O minimum requirements populated",
            StatusMark.OBLIGATION,
            f"{len(requirements)} active-O requirements remain open",
        )


def case_3_routes(routes: List[ORoute], out: ScriptOutput) -> None:
    header("Case 3: Active O route ledger")
    for route in routes:
        print()
        print("-" * 120)
        print(route.name)
        print("-" * 120)
        print(f"Route: {route.route}")
        print(f"[{status_mark(route.status).value}] {route.name}: {route.status}")
        print(f"Allowed if: {route.allowed_if}")
        print(f"Rejected if: {route.rejected_if}")

    with out.governance_assessments():
        out.line(
            "active O routes classified",
            StatusMark.PASS,
            f"{len(routes)} active-O routes classified",
        )


def case_4_rejected_shortcuts(shortcuts: List[RejectedOShortcut], out: ScriptOutput) -> None:
    header("Case 4: Rejected active-O shortcuts")
    for shortcut in shortcuts:
        print()
        print("-" * 120)
        print(shortcut.name)
        print("-" * 120)
        print(f"Shortcut: {shortcut.shortcut}")
        print(f"Forbidden use: {shortcut.forbidden_use}")
        print(f"[{status_mark(shortcut.status).value}] {shortcut.name}: {shortcut.status}")
        print(f"Consequence: {shortcut.consequence}")

    with out.counterexamples():
        out.line(
            "active O shortcuts rejected",
            StatusMark.FAIL,
            "unnamed domain/kernel, no pairing, no divergence behavior, boundary/source blind O, and parent from O remain rejected",
        )


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("The no-overlap operator minimum burden audit fails if a later script allows:")
    print()
    print("1. O acts without declared domain")
    print("2. O output has no declared codomain/status")
    print("3. O kills residuals without kernel definition")
    print("4. O preserves image with hidden trace/source/load")
    print("5. O lacks idempotence/projection or replacement law")
    print("6. O lacks composition with insertion/residual/boundary/source/support maps")
    print("7. O lacks measure/pairing or no-overlap criterion")
    print("8. O lacks derivative/divergence behavior")
    print("9. O lacks boundary/source/mass/scalar/current/support behavior")
    print("10. O is selected from recovery")
    print("11. O opens insertion or parent gate by itself")

    with out.governance_assessments():
        out.line(
            "active O failure controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not invoke active O without full operator burden",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("No-overlap operator minimum-burden result:")
    print()
    print("  Active O requires real operator structure.")
    print("  Required: domain, codomain, kernel, image, idempotence/composition, pairing/no-overlap criterion, derivative/divergence behavior, boundary behavior, source/mass behavior, scalar-tail/current-flux behavior, support/matching behavior, and recovery independence.")
    print("  Without this, O remains a placeholder and cannot remove residual overlap.")
    print("  Active O remains theorem-targeted.")
    print()
    print("Possible next script:")
    print("  candidate_residual_kill_recovery_independence.py")
    print()
    print("Tiny goblin label:")
    print("  No fake eraser. Show the teeth.")

    with out.governance_assessments():
        out.line(
            "no-overlap operator minimum burden audit complete",
            StatusMark.PASS,
            "active-O burden explicit; O theorem remains open",
        )


def record_derivations(ns, ledger: OStructureLedger) -> None:
    ns.record_derivation(
        derivation_id="no_overlap_operator_minimum_burden_25",
        inputs=[
            ledger.domain,
            ledger.codomain,
            ledger.kernel,
            ledger.image,
            ledger.idempotence,
            ledger.composition,
            ledger.pairing,
            ledger.orthogonality,
            ledger.derivative_behavior,
            ledger.divergence_behavior,
            ledger.boundary_behavior,
            ledger.source_behavior,
            ledger.mass_behavior,
            ledger.scalar_tail_behavior,
            ledger.current_flux_behavior,
            ledger.support_matching_behavior,
            ledger.recovery_independence,
        ],
        output=ledger.missing_structure_load,
        method="sum minimum active-O structure requirements as an obligation ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="active_O_minimum_burden",
        scope="Group 25 residual kill or no-overlap theorem",
    )

    ns.record_derivation(
        derivation_id="no_overlap_operator_minimum_burden_marker_25",
        inputs=[
            sp.Symbol("O_domain"),
            sp.Symbol("O_codomain"),
            sp.Symbol("O_kernel"),
            sp.Symbol("O_image"),
            sp.Symbol("O_idempotence"),
            sp.Symbol("O_divergence"),
            sp.Symbol("O_boundary"),
            sp.Symbol("O_source"),
            sp.Symbol("O_recovery_independence"),
        ],
        output=sp.Symbol("no_overlap_operator_minimum_burden_stated"),
        method="Group 25 active O minimum burden ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="requirements_marker",
        scope="Group 25 residual kill or no-overlap theorem",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g25_derive_O_domain_codomain", "Derive O domain and codomain"),
        ("g25_derive_O_kernel_image", "Derive O kernel and image"),
        ("g25_derive_O_idempotence_composition", "Derive O idempotence and composition"),
        ("g25_derive_O_pairing_orthogonality", "Derive O pairing and no-overlap criterion"),
        ("g25_derive_O_derivative_divergence", "Derive O derivative/divergence behavior"),
        ("g25_derive_O_boundary_behavior", "Derive O boundary behavior"),
        ("g25_derive_O_source_mass_behavior", "Derive O source/mass behavior"),
        ("g25_derive_O_scalar_current_support_behavior", "Derive O scalar/current/support behavior"),
        ("g25_derive_O_recovery_independence", "Derive O recovery independence"),
        ("g25_keep_O_from_parent_shortcut", "Keep O from opening insertion or parent gate by itself"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g25_active_O_minimum_burden_route"],
            description=(
                "Active O remains theorem-targeted until full operator structure and compatibility behavior are derived."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g25_derive_O_domain_codomain",
        "g25_derive_O_kernel_image",
        "g25_derive_O_idempotence_composition",
        "g25_derive_O_pairing_orthogonality",
        "g25_derive_O_derivative_divergence",
        "g25_derive_O_boundary_behavior",
        "g25_derive_O_source_mass_behavior",
        "g25_derive_O_scalar_current_support_behavior",
        "g25_derive_O_recovery_independence",
        "g25_keep_O_from_parent_shortcut",
    ]

    ns.record_route(RouteRecord(
        route_id="g25_active_O_minimum_burden_route",
        script_id=SCRIPT_ID,
        name="Group 25 active no-overlap operator minimum burden",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "O domain/codomain/kernel/image are derived",
            "O idempotence/composition and pairing/no-overlap criterion are derived",
            "O derivative/divergence and boundary/source/mass/scalar/current/support behavior are derived",
            "O is recovery-independent",
            "O does not open insertion or parent gate by itself",
        ],
    ))

    for branch_id in [
        "O_unnamed_domain",
        "O_unnamed_kernel",
        "O_no_pairing",
        "O_no_divergence_behavior",
        "O_boundary_source_blind",
        "O_recovery_selected",
        "parent_from_active_O",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}_25",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; active O cannot remove overlap without full operator burden.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g25_active_O_requires_full_structure",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Active no-overlap O cannot erase residual overlap by name. It requires domain, codomain, kernel, image, "
            "idempotence/composition, pairing/no-overlap criterion, derivative/divergence behavior, boundary behavior, "
            "source/mass behavior, scalar-tail/current-flux/support behavior, and recovery independence. "
            "This script does not derive O."
        ),
        derivation_ids=[
            "no_overlap_operator_minimum_burden_25",
            "no_overlap_operator_minimum_burden_marker_25",
        ],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate No-Overlap Operator Minimum Burden")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    ledger = build_ledger()
    requirements = build_requirements()
    routes = build_routes()
    shortcuts = build_rejected_shortcuts()

    case_0_problem_statement(out)
    case_1_structure_ledger(ledger, out)
    case_2_requirements(requirements, out)
    case_3_routes(routes, out)
    case_4_rejected_shortcuts(shortcuts, out)
    case_5_failure_controls(out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, ledger)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
