# Candidate O obligations
#
# Group:
#   27_active_O_construction
#
# Script type:
#   OBLIGATION / HANDOFF SUMMARY
#
# Purpose
# -------
# Summarize what the active-O construction attempt closed, what remains open,
# and what handoff is now licensed.
#
# Locked-door question:
#
#   What did the active-O construction attempt close, and what remains open?
#
# This script does not derive active O.
# It does not derive residual control.
# It does not derive B_s/F_zeta insertion.
# It does not derive parent equation closure.
#
# Tiny goblin rule:
#
#   Count the missing teeth before biting.

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
        "CANDIDATE": StatusMark.DEFER,
        "CONTROLLED_OBSTRUCTION": StatusMark.DEFER,
        "HANDOFF_READY": StatusMark.PASS,
        "NOT_CONSTRUCTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "PARTIAL": StatusMark.INFO,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "SAFE_IF": StatusMark.INFO,
        "UNDERDETERMINED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        ("g27_O_problem", "027_active_O_construction__candidate_O_problem_ledger", "g27_O_problem", RecordKind.INVENTORY_MARKER),
        ("g27_dc", "027_active_O_construction__candidate_O_domain_codomain", "g27_O_domain_codomain", RecordKind.INVENTORY_MARKER),
        ("g27_ki", "027_active_O_construction__candidate_O_kernel_image", "g27_O_kernel_image", RecordKind.INVENTORY_MARKER),
        ("g27_pair", "027_active_O_construction__candidate_O_no_overlap_pairing", "g27_O_pairing", RecordKind.INVENTORY_MARKER),
        ("g27_alg", "027_active_O_construction__candidate_O_projection_law", "g27_O_alg_law", RecordKind.INVENTORY_MARKER),
        ("g27_div", "027_active_O_construction__candidate_O_divergence_commutation", "g27_O_divergence", RecordKind.INVENTORY_MARKER),
        ("g27_bsm", "027_active_O_construction__candidate_O_boundary_source_mass", "g27_O_bsm", RecordKind.INVENTORY_MARKER),
        ("g27_rec", "027_active_O_construction__candidate_O_recovery_independence", "g27_O_recovery", RecordKind.INVENTORY_MARKER),
        ("g27_obs", "027_active_O_construction__candidate_O_construction_obstruction", "g27_O_obstruction", RecordKind.INVENTORY_MARKER),
        ("g26_summary", "026_residual_control_theorem_attempt__candidate_group_26_status_summary", "g26_status_summary", RecordKind.INVENTORY_MARKER),
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
    for attr in ("routes_path", "branch_decisions_path", "claims_path", "obligations_path", "derivations_path", "governance_path"):
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
class OObligationStatus:
    name: str
    obligation: str
    status: str
    current_result: str
    blocks: str


@dataclass
class OHandoff:
    name: str
    route: str
    status: str
    why: str
    caution: str


@dataclass
class OClosedItem:
    name: str
    item: str
    status: str
    meaning: str


@dataclass
class RejectedOUpgrade:
    name: str
    upgrade: str
    status: str
    reason: str


@dataclass
class OObligationConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_closed_items() -> List[OClosedItem]:
    return [
        OClosedItem(
            name="D1: construction burden",
            item="active-O construction burden is explicit",
            status="PARTIAL",
            meaning="the theory now knows what O would have to carry",
        ),
        OClosedItem(
            name="D2: candidate domain/codomain",
            item="candidate domain/codomain ledgers exist",
            status="PARTIAL",
            meaning="possible input/output sectors are inventoried",
        ),
        OClosedItem(
            name="D3: safe trace preservation",
            item="O(zeta_Bs)=zeta_Bs remains a candidate preservation direction",
            status="CANDIDATE",
            meaning="the safe trace channel is protected as candidate image direction",
        ),
        OClosedItem(
            name="D4: recovery selection",
            item="recovery-selected O is rejected",
            status="REJECTED",
            meaning="AB=1, weak-field, Schwarzschild, gamma/PPN, kappa=0, and parent-fit cannot construct O",
        ),
        OClosedItem(
            name="D5: repair selection",
            item="boundary/source/mass repair-selected O is rejected",
            status="REJECTED",
            meaning="guardrail failure may reject O but cannot select it",
        ),
        OClosedItem(
            name="D6: downstream gates",
            item="insertion and parent gates remain closed",
            status="REQUIRED",
            meaning="O construction status cannot license B_s/F_zeta insertion or parent equation",
        ),
    ]


def build_obligation_statuses() -> List[OObligationStatus]:
    return [
        OObligationStatus(
            name="O1: final domain/codomain",
            obligation="derive final O domain and codomain",
            status="OPEN",
            current_result="candidate ledgers exist only",
            blocks="full operator definition",
        ),
        OObligationStatus(
            name="O2: kernel/image",
            obligation="derive O kernel and image",
            status="OPEN",
            current_result="zeta_Bs image candidate exists; zeta/kappa residual membership underdetermined",
            blocks="residual action",
        ),
        OObligationStatus(
            name="O3: no-overlap criterion",
            obligation="derive mathematical no-overlap pairing or criterion",
            status="OPEN",
            current_result="explicit pairing not derived; sector-projection candidate remains",
            blocks="kernel/image closure",
        ),
        OObligationStatus(
            name="O4: algebraic law",
            obligation="derive projection/replacement/constraint law and composition behavior",
            status="OPEN",
            current_result="O^2=O, linearity, and residual kill not derived",
            blocks="operator action",
        ),
        OObligationStatus(
            name="O5: divergence behavior",
            obligation="derive strict commutation or explicit correction law",
            status="OPEN",
            current_result="Div(OX)=O(Div X) not derived; correction route constrained candidate",
            blocks="field-equation use",
        ),
        OObligationStatus(
            name="O6: boundary/source/mass behavior",
            obligation="derive mass, scalar-tail, current, source, shell, support neutrality",
            status="OPEN",
            current_result="all guardrail neutralities remain not derived",
            blocks="guardrail-compatible O",
        ),
        OObligationStatus(
            name="O7: full recovery-independent construction",
            obligation="define O structurally before recovery audit",
            status="OPEN",
            current_result="recovery selection rejected, but O not constructed",
            blocks="full recovery-independent O",
        ),
        OObligationStatus(
            name="O8: B_s/F_zeta coefficient origin",
            obligation="derive insertion law / coefficient origin if needed",
            status="OPEN",
            current_result="still separate and not derived",
            blocks="possible O classification and residual interpretation",
        ),
        OObligationStatus(
            name="O9: residual-control retest",
            obligation="retest residual control only after usable O or alternate structure exists",
            status="NOT_READY",
            current_result="O is not usable",
            blocks="residual-control theorem",
        ),
        OObligationStatus(
            name="O10: parent equation",
            obligation="keep parent field equation closed",
            status="NOT_READY",
            current_result="parent gate closed",
            blocks="parent closure",
        ),
    ]


def build_handoffs() -> List[OHandoff]:
    return [
        OHandoff(
            name="H1: sector pairing and no-overlap geometry",
            route="028_sector_pairing_and_no_overlap_geometry",
            status="HANDOFF_READY",
            why="no explicit pairing is derived, and sector-projection remains the best candidate",
            caution="must not assume ordinary orthogonality or projection algebra",
        ),
        OHandoff(
            name="H2: B_s/F_zeta coefficient origin",
            route="028_Bs_Fzeta_coefficient_origin",
            status="HANDOFF_READY",
            why="coefficient origin may decide residual interpretation and O classification",
            caution="must keep residual control and O construction explicitly open",
        ),
        OHandoff(
            name="H3: operator algebra and constraint law",
            route="028_operator_algebra_and_constraint_law",
            status="SAFE_IF",
            why="constraint-style O may be safer than eraser O",
            caution="requires a sector/no-overlap criterion first or must state its own criterion",
        ),
        OHandoff(
            name="H4: divergence-safe operator structure",
            route="028_divergence_safe_operator_structure",
            status="SAFE_IF",
            why="O cannot enter field equations without divergence behavior",
            caution="must not turn correction terms into hidden sources",
        ),
        OHandoff(
            name="H5: residual-control retest with O",
            route="028_O_residual_control_retest",
            status="NOT_READY",
            why="O is not usable yet",
            caution="do not retest residual control until actual O structure exists",
        ),
        OHandoff(
            name="H6: parent field equation",
            route="parent_field_equation",
            status="NOT_READY",
            why="parent closure remains blocked by residual control, insertion, divergence, boundary/source/support, and parent identity",
            caution="forbidden as next step",
        ),
    ]


def build_rejected_upgrades() -> List[RejectedOUpgrade]:
    return [
        RejectedOUpgrade(
            name="U1: obligations as construction",
            upgrade="open obligation summary treated as active-O construction",
            status="REJECTED",
            reason="obligations are not theorem closure",
        ),
        RejectedOUpgrade(
            name="U2: partial structure as usable O",
            upgrade="candidate domain/codomain and trace preservation treated as usable O",
            status="REJECTED",
            reason="residual action, pairing, algebraic law, divergence, and guardrail behavior remain open",
        ),
        RejectedOUpgrade(
            name="U3: handoff as theorem",
            upgrade="handoff to sector pairing or coefficient origin treated as result",
            status="REJECTED",
            reason="handoff is a next route, not a derivation",
        ),
        RejectedOUpgrade(
            name="U4: O obstruction as O impossible",
            upgrade="controlled underdetermination treated as impossibility",
            status="REJECTED",
            reason="missing structure is not a no-go theorem",
        ),
        RejectedOUpgrade(
            name="U5: O obligations license insertion",
            upgrade="O obligation state licenses B_s/F_zeta insertion",
            status="REJECTED",
            reason="insertion remains separate",
        ),
        RejectedOUpgrade(
            name="U6: O obligations open parent",
            upgrade="O obligation state opens parent equation",
            status="REJECTED",
            reason="parent gate remains closed",
        ),
    ]


def build_conclusions() -> List[OObligationConclusion]:
    return [
        OObligationConclusion(
            name="C1: active O",
            conclusion="not constructed",
            status="NOT_CONSTRUCTED",
            meaning="O cannot be used as operator",
        ),
        OObligationConclusion(
            name="C2: progress",
            conclusion="partial construction map exists",
            status="PARTIAL",
            meaning="the missing structure is now well localized",
        ),
        OObligationConclusion(
            name="C3: best handoff",
            conclusion="sector pairing / no-overlap geometry is the cleanest next constructive route",
            status="HANDOFF_READY",
            meaning="the missing pairing blocks kernel/image and projection law",
        ),
        OObligationConclusion(
            name="C4: alternate handoff",
            conclusion="B_s/F_zeta coefficient origin remains handoff-ready",
            status="HANDOFF_READY",
            meaning="coefficient origin may decide residual interpretation and O need",
        ),
        OObligationConclusion(
            name="C5: downstream gates",
            conclusion="residual control and parent equation remain not ready",
            status="NOT_READY",
            meaning="do not use O or proceed to parent closure",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: O obligations problem")
    print("Question:")
    print()
    print("  What did the active-O construction attempt close, and what remains open?")
    print()
    print("Reference discipline:")
    print()
    print("  This is an obligation/handoff summary, not O construction.")
    print("  Missing teeth are counted before the bite.")

    with out.governance_assessments():
        out.line(
            "O obligations summary opened",
            StatusMark.INFO,
            "summarizing active-O construction status and handoff choices",
        )


def case_1_closed_items(items: List[OClosedItem], out: ScriptOutput) -> None:
    header("Case 1: What the active-O attempt clarified")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Item: {item.item}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Meaning: {item.meaning}")

    with out.governance_assessments():
        out.line(
            "O clarified items summarized",
            StatusMark.PASS,
            f"{len(items)} clarified/rejected/protected items summarized",
        )


def case_2_obligations(items: List[OObligationStatus], out: ScriptOutput) -> None:
    header("Case 2: Open active-O obligations")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Obligation: {item.obligation}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Current result: {item.current_result}")
        print(f"Blocks: {item.blocks}")

    with out.unresolved_obligations():
        out.line(
            "O open obligations summarized",
            StatusMark.OBLIGATION,
            f"{len(items)} active-O obligations remain open or not ready",
        )


def case_3_handoffs(items: List[OHandoff], out: ScriptOutput) -> None:
    header("Case 3: Handoff recommendations")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Route: {item.route}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Why: {item.why}")
        print(f"Caution: {item.caution}")

    with out.governance_assessments():
        out.line(
            "O handoff recommendations stated",
            StatusMark.PASS,
            "sector pairing/no-overlap geometry and B_s/F_zeta coefficient origin are handoff-ready",
        )


def case_4_rejected_upgrades(items: List[RejectedOUpgrade], out: ScriptOutput) -> None:
    header("Case 4: Rejected O-obligation upgrades")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Upgrade: {item.upgrade}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")

    with out.counterexamples():
        out.line(
            "O obligation upgrades rejected",
            StatusMark.FAIL,
            "obligations, partial structure, handoffs, obstruction, insertion, and parent upgrades are rejected",
        )


def case_5_conclusions(items: List[OObligationConclusion], out: ScriptOutput) -> None:
    header("Case 5: O obligation conclusions")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Conclusion: {item.conclusion}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Meaning: {item.meaning}")

    with out.governance_assessments():
        out.line(
            "O obligations conclusion stated",
            StatusMark.PASS,
            "active O not constructed; handoff to sector pairing or coefficient origin is ready",
        )


def case_6_failure_controls(out: ScriptOutput) -> None:
    header("Case 6: Failure controls")
    print("The O obligations summary fails if a later script allows:")
    print()
    print("1. obligations treated as active-O construction")
    print("2. partial structure treated as usable O")
    print("3. handoff treated as theorem closure")
    print("4. controlled underdetermination treated as impossibility")
    print("5. O obligation state licenses B_s/F_zeta insertion")
    print("6. O obligation state opens parent equation")
    print("7. residual-control retest before usable O exists")
    print("8. parent field equation attempted next")
    print("9. recovery audit treated as O construction")
    print("10. repair-selected O reintroduced")

    with out.governance_assessments():
        out.line(
            "O obligations failure controls stated",
            StatusMark.OBLIGATION,
            "future work must not upgrade obligations or handoffs to theorem closure",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("O obligations result:")
    print()
    print("  Active O is not constructed.")
    print("  Candidate domain/codomain and safe trace preservation structure exist.")
    print("  Kernel/image, no-overlap pairing, algebraic law, divergence behavior, and boundary/source/mass behavior remain open.")
    print("  Recovery-selected and repair-selected O are rejected.")
    print("  This is controlled underdetermination, not impossibility.")
    print("  O is not usable in residual control or field equations.")
    print()
    print("Best next group options:")
    print("  28_sector_pairing_and_no_overlap_geometry")
    print("  28_Bs_Fzeta_coefficient_origin")
    print()
    print("Preferred constructive handoff:")
    print("  28_sector_pairing_and_no_overlap_geometry")
    print()
    print("Tiny goblin label:")
    print("  Count the missing teeth before biting.")

    with out.governance_assessments():
        out.line(
            "O obligations summary complete",
            StatusMark.PASS,
            "active-O construction attempt summarized; sector pairing/no-overlap geometry is preferred handoff",
        )


def record_derivations(ns) -> None:
    ns.record_derivation(
        derivation_id="g27_O_obligations",
        inputs=[
            sp.Symbol("O_not_constructed"),
            sp.Symbol("partial_domain_codomain"),
            sp.Symbol("safe_trace_candidate"),
            sp.Symbol("pairing_missing"),
            sp.Symbol("alg_law_missing"),
            sp.Symbol("divergence_missing"),
            sp.Symbol("bsm_missing"),
            sp.Symbol("recovery_selection_rejected"),
        ],
        output=sp.Symbol("g27_O_obligations_open"),
        method="summarize active-O construction obligations and handoff choices",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="O_obligations_marker",
        scope="Group 27 active O construction",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g27_ob_final_sector", "Derive final sector decomposition"),
        ("g27_ob_pairing", "Derive no-overlap pairing/criterion"),
        ("g27_ob_alg", "Derive O algebraic law"),
        ("g27_ob_div", "Derive O divergence behavior"),
        ("g27_ob_bsm", "Derive O boundary/source/mass behavior"),
        ("g27_ob_coeff", "Derive B_s/F_zeta coefficient origin if needed"),
        ("g27_ob_no_retest", "Do not retest residual control before usable O"),
        ("g27_ob_parent_closed", "Keep parent equation closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g27_ob_route"],
            description=(
                "Active O is not constructed. This obligation remains open for future constructive work."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g27_ob_final_sector",
        "g27_ob_pairing",
        "g27_ob_alg",
        "g27_ob_div",
        "g27_ob_bsm",
        "g27_ob_coeff",
        "g27_ob_no_retest",
        "g27_ob_parent_closed",
    ]

    ns.record_route(RouteRecord(
        route_id="g27_ob_route",
        script_id=SCRIPT_ID,
        name="Group 27 O obligations route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "active O is not constructed",
            "partial structure is not promoted to usable O",
            "sector pairing/no-overlap geometry and B_s/F_zeta coefficient origin are handoff-ready",
            "residual-control retest and parent equation remain not ready",
        ],
    ))

    for branch_id in [
        "obligations_as_O",
        "partial_structure_as_usable_O",
        "handoff_as_theorem",
        "underdetermination_as_impossibility",
        "obligations_license_insertion",
        "obligations_open_parent",
        "residual_retest_before_O",
        "parent_as_next",
        "recovery_audit_constructs_O",
        "repair_selected_O",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; O obligations summary is not active-O construction or downstream closure.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g27_O_obligations_open",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Active O is not constructed. Candidate domain/codomain and safe trace preservation structure exist, but kernel/image, no-overlap pairing, "
            "algebraic law, divergence behavior, and boundary/source/mass behavior remain open. Recovery-selected and repair-selected O are rejected. "
            "The preferred constructive handoff is sector pairing/no-overlap geometry; B_s/F_zeta coefficient origin remains an alternate handoff. "
            "Residual-control retest and parent equation are not ready."
        ),
        derivation_ids=["g27_O_obligations"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate O Obligations")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    closed_items = build_closed_items()
    obligations = build_obligation_statuses()
    handoffs = build_handoffs()
    upgrades = build_rejected_upgrades()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_closed_items(closed_items, out)
    case_2_obligations(obligations, out)
    case_3_handoffs(handoffs, out)
    case_4_rejected_upgrades(upgrades, out)
    case_5_conclusions(conclusions, out)
    case_6_failure_controls(out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
