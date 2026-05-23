# Candidate O construction obstruction
#
# Group:
#   27_active_O_construction
#
# Script type:
#   CONSTRUCTION OBSTRUCTION / STATUS CLASSIFIER
#
# Purpose
# -------
# Consolidate the active-O construction attempt and classify whether O is
# constructed, partially constructed, underdetermined, blocked by missing
# structure, or rejected as shortcut.
#
# Locked-door question:
#
#   Can active O actually be constructed from current theory objects?
#
# This script does not derive active O unless every construction burden has closed.
# Under current upstream results, that does not happen.
#
# It does not derive residual control.
# It does not derive B_s/F_zeta insertion.
# It does not derive parent equation closure.
#
# Tiny goblin rule:
#
#   If the tool is not forged, do not swing it.

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
        "CONSTRUCTED": StatusMark.PASS,
        "CONTROLLED_OBSTRUCTION": StatusMark.DEFER,
        "DEFERRED": StatusMark.DEFER,
        "INSUFFICIENT": StatusMark.DEFER,
        "NOT_CONSTRUCTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "PARTIAL": StatusMark.INFO,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
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
class ConstructionLoadSymbols:
    domain_gap: sp.Symbol
    codomain_gap: sp.Symbol
    kernel_gap: sp.Symbol
    image_gap: sp.Symbol
    pairing_gap: sp.Symbol
    alg_gap: sp.Symbol
    div_gap: sp.Symbol
    bsm_gap: sp.Symbol
    recovery_gap: sp.Symbol
    insertion_gap: sp.Symbol
    parent_gap: sp.Symbol
    construction_gap: sp.Expr


@dataclass
class ConstructionStatus:
    name: str
    object_piece: str
    status: str
    result: str
    blocker: str


@dataclass
class ConstructionRoute:
    name: str
    route: str
    status: str
    result: str
    implication: str


@dataclass
class MissingObject:
    name: str
    missing_object: str
    status: str
    blocks: str
    next_possible_route: str


@dataclass
class RejectedConstructionUpgrade:
    name: str
    upgrade: str
    status: str
    reason: str


@dataclass
class ConstructionConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> ConstructionLoadSymbols:
    (
        domain_gap,
        codomain_gap,
        kernel_gap,
        image_gap,
        pairing_gap,
        alg_gap,
        div_gap,
        bsm_gap,
        recovery_gap,
        insertion_gap,
        parent_gap,
    ) = sp.symbols(
        "domain_gap codomain_gap kernel_gap image_gap pairing_gap alg_gap div_gap bsm_gap recovery_gap insertion_gap parent_gap",
        real=True,
    )

    construction_gap = sp.simplify(
        domain_gap
        + codomain_gap
        + kernel_gap
        + image_gap
        + pairing_gap
        + alg_gap
        + div_gap
        + bsm_gap
        + recovery_gap
        + insertion_gap
        + parent_gap
    )

    return ConstructionLoadSymbols(
        domain_gap=domain_gap,
        codomain_gap=codomain_gap,
        kernel_gap=kernel_gap,
        image_gap=image_gap,
        pairing_gap=pairing_gap,
        alg_gap=alg_gap,
        div_gap=div_gap,
        bsm_gap=bsm_gap,
        recovery_gap=recovery_gap,
        insertion_gap=insertion_gap,
        parent_gap=parent_gap,
        construction_gap=construction_gap,
    )


def build_statuses() -> List[ConstructionStatus]:
    return [
        ConstructionStatus(
            name="S1: domain/codomain",
            object_piece="candidate domain and codomain",
            status="PARTIAL",
            result="candidate ledgers exist",
            blocker="not narrowed to a final operator domain/codomain",
        ),
        ConstructionStatus(
            name="S2: kernel/image",
            object_piece="candidate kernel and image",
            status="UNDERDETERMINED",
            result="zeta_Bs belongs in image candidate; zeta/kappa residuals are plausible kernel/inert/projected candidates",
            blocker="kernel membership and image safety require no-overlap criterion and operator law",
        ),
        ConstructionStatus(
            name="S3: no-overlap criterion",
            object_piece="pairing / sector split / no-overlap criterion",
            status="NOT_DERIVED",
            result="no explicit mathematical pairing is derived; sector-projection split remains best candidate",
            blocker="projection/replacement law and sector composition are not derived",
        ),
        ConstructionStatus(
            name="S4: algebraic law",
            object_piece="projection / replacement / constraint law",
            status="NOT_DERIVED",
            result="O^2=O, linearity, and residual kill are not derived; O(zeta_Bs)=zeta_Bs remains candidate",
            blocker="composition, residual action, no-overlap, and divergence behavior remain open",
        ),
        ConstructionStatus(
            name="S5: divergence behavior",
            object_piece="divergence / conservation safety",
            status="NOT_DERIVED",
            result="Div(OX)=O(Div X) is not derived; correction route is candidate but constrained",
            blocker="correction, source, boundary, current, and parent gaps remain open",
        ),
        ConstructionStatus(
            name="S6: boundary/source/mass behavior",
            object_piece="mass, scalar-tail, current, source, shell, support behavior",
            status="NOT_DERIVED",
            result="mass neutrality, scalar-tail neutrality, current neutrality, source neutrality, and support neutrality are not derived",
            blocker="guardrail behavior remains open",
        ),
        ConstructionStatus(
            name="S7: recovery independence",
            object_piece="anti-smuggling recovery discipline",
            status="PARTIAL",
            result="recovery selection is rejected; recovery audit remains conditionally safe",
            blocker="O itself is not structurally defined, so full recovery-independent construction is not complete",
        ),
        ConstructionStatus(
            name="S8: downstream separation",
            object_piece="insertion and parent gates",
            status="REQUIRED",
            result="insertion and parent gates remain closed",
            blocker="O construction cannot license downstream closure",
        ),
    ]


def build_routes() -> List[ConstructionRoute]:
    return [
        ConstructionRoute(
            name="R1: full O constructed",
            route="construct complete active O",
            status="NOT_DERIVED",
            result="not achieved",
            implication="O cannot be used as operator",
        ),
        ConstructionRoute(
            name="R2: partial O structure",
            route="candidate domain/codomain and preservation direction",
            status="PARTIAL",
            result="candidate inventories exist and O(zeta_Bs)=zeta_Bs remains a candidate preservation law",
            implication="useful structure, but not enough to act on residuals",
        ),
        ConstructionRoute(
            name="R3: residual-kill O",
            route="O(zeta_res)=O(kappa_res)=0",
            status="NOT_DERIVED",
            result="not licensed",
            implication="would smuggle residual kill without kernel/no-overlap theorem",
        ),
        ConstructionRoute(
            name="R4: inert replacement O",
            route="map residuals to inert sector",
            status="UNDERDETERMINED",
            result="candidate only",
            implication="requires inert-sector no-reentry and guardrail behavior",
        ),
        ConstructionRoute(
            name="R5: constraint-style O",
            route="constraint operator with auditability",
            status="UNDERDETERMINED",
            result="candidate only",
            implication="may be safer than eraser O but requires divergence and boundary/source behavior",
        ),
        ConstructionRoute(
            name="R6: O as shortcut",
            route="O by name / magic eraser / recovery-selected / repair-selected",
            status="REJECTED",
            result="rejected",
            implication="cannot be used",
        ),
    ]


def build_missing_objects() -> List[MissingObject]:
    return [
        MissingObject(
            name="M1: final sector decomposition",
            missing_object="structural trace/residual/accounting/source/boundary sector split",
            status="OPEN",
            blocks="domain/codomain narrowing and projection law",
            next_possible_route="sector_pairing_and_no_overlap_geometry",
        ),
        MissingObject(
            name="M2: no-overlap pairing",
            missing_object="mathematical pairing or criterion making overlap meaningful",
            status="OPEN",
            blocks="kernel/image and no-overlap theorem",
            next_possible_route="sector_pairing_and_no_overlap_geometry",
        ),
        MissingObject(
            name="M3: algebraic operator law",
            missing_object="projection/replacement/constraint law with composition behavior",
            status="OPEN",
            blocks="O action and residual-control retest",
            next_possible_route="operator_algebra_and_constraint_law",
        ),
        MissingObject(
            name="M4: divergence law",
            missing_object="strict commutation or explicit correction law",
            status="OPEN",
            blocks="field-equation use of O",
            next_possible_route="divergence_safe_operator_structure",
        ),
        MissingObject(
            name="M5: boundary/source/mass theorem",
            missing_object="mass, scalar, current, source, shell, support neutrality theorem",
            status="OPEN",
            blocks="guardrail-compatible O",
            next_possible_route="operator_boundary_source_compatibility",
        ),
        MissingObject(
            name="M6: B_s/F_zeta coefficient origin",
            missing_object="insertion law / coefficient origin",
            status="OPEN",
            blocks="zeta residual interpretation and possible O classification",
            next_possible_route="Bs_Fzeta_coefficient_origin",
        ),
    ]


def build_upgrades() -> List[RejectedConstructionUpgrade]:
    return [
        RejectedConstructionUpgrade(
            name="U1: partial structure becomes O",
            upgrade="candidate domain/codomain/preservation direction treated as constructed O",
            status="REJECTED",
            reason="kernel/image, no-overlap, algebraic law, divergence, and guardrail behavior remain open",
        ),
        RejectedConstructionUpgrade(
            name="U2: O construction obstruction becomes O impossibility",
            upgrade="under current objects O not constructed becomes O impossible",
            status="REJECTED",
            reason="this is controlled underdetermination, not mathematical impossibility",
        ),
        RejectedConstructionUpgrade(
            name="U3: O obstruction becomes residual control",
            upgrade="failure to construct O treated as residual-control result",
            status="REJECTED",
            reason="residual control remains open",
        ),
        RejectedConstructionUpgrade(
            name="U4: O obstruction licenses insertion",
            upgrade="O construction status licenses B_s/F_zeta insertion",
            status="REJECTED",
            reason="insertion law remains separate",
        ),
        RejectedConstructionUpgrade(
            name="U5: O obstruction opens parent",
            upgrade="O construction status opens parent equation",
            status="REJECTED",
            reason="parent gate remains closed",
        ),
        RejectedConstructionUpgrade(
            name="U6: recovery audit constructs O",
            upgrade="recovery audit treated as recovery-independent O construction",
            status="REJECTED",
            reason="recovery selection is rejected but O is not structurally derived",
        ),
    ]


def build_conclusions() -> List[ConstructionConclusion]:
    return [
        ConstructionConclusion(
            name="C1: active O construction",
            conclusion="not constructed",
            status="NOT_CONSTRUCTED",
            meaning="current objects do not yet supply full active O",
        ),
        ConstructionConclusion(
            name="C2: partial structure",
            conclusion="partial candidate structure exists",
            status="PARTIAL",
            meaning="domain/codomain ledgers and safe trace preservation candidate are useful but insufficient",
        ),
        ConstructionConclusion(
            name="C3: obstruction type",
            conclusion="controlled underdetermination",
            status="CONTROLLED_OBSTRUCTION",
            meaning="the obstruction is missing structure, not a proof of impossibility",
        ),
        ConstructionConclusion(
            name="C4: immediate use",
            conclusion="O is not usable as operator",
            status="NOT_READY",
            meaning="do not use O in residual control or field equations yet",
        ),
        ConstructionConclusion(
            name="C5: next summary",
            conclusion="obligations summary is ready",
            status="OPEN",
            meaning="the group should summarize open obligations and handoff choices next",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: O construction obstruction problem")
    print("Question:")
    print()
    print("  Can active O actually be constructed from current theory objects?")
    print()
    print("Reference discipline:")
    print()
    print("  Candidate structure is not full construction.")
    print("  Controlled underdetermination is not mathematical impossibility.")
    print("  O cannot be used before it is forged.")

    with out.governance_assessments():
        out.line(
            "O construction obstruction classifier opened",
            StatusMark.INFO,
            "classifying active-O construction status after major burden audits",
        )


def case_1_symbol_ledger(symbols: ConstructionLoadSymbols, out: ScriptOutput) -> None:
    header("Case 1: O construction gap ledger")
    print("Construction gaps:")
    print()
    for name in [
        "domain_gap",
        "codomain_gap",
        "kernel_gap",
        "image_gap",
        "pairing_gap",
        "alg_gap",
        "div_gap",
        "bsm_gap",
        "recovery_gap",
        "insertion_gap",
        "parent_gap",
    ]:
        print(f"  {name} = {sp.sstr(getattr(symbols, name))}")
    print()
    print("Total construction gap:")
    print()
    print(f"  L_O_construction_gap = {sp.sstr(symbols.construction_gap)}")
    print()
    print("Interpretation:")
    print()
    print("  Active O is constructed only if these gaps are closed by theorem.")
    print("  Under current audited objects, they remain open or only partially reduced.")

    with out.derived_results():
        out.line(
            "O construction gap ledger stated",
            StatusMark.OBLIGATION,
            f"L_O_construction_gap = {sp.sstr(symbols.construction_gap)}",
        )


def case_2_statuses(items: List[ConstructionStatus], out: ScriptOutput) -> None:
    header("Case 2: Active-O construction status ledger")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Object piece: {item.object_piece}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Result: {item.result}")
        print(f"Blocker: {item.blocker}")

    with out.governance_assessments():
        out.line(
            "O construction status ledger populated",
            StatusMark.DEFER,
            f"{len(items)} construction pieces classified",
        )


def case_3_routes(items: List[ConstructionRoute], out: ScriptOutput) -> None:
    header("Case 3: O construction routes")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Route: {item.route}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Result: {item.result}")
        print(f"Implication: {item.implication}")

    with out.governance_assessments():
        out.line(
            "O construction routes classified",
            StatusMark.DEFER,
            "full O not constructed; partial structure exists; shortcut routes rejected",
        )


def case_4_missing_objects(items: List[MissingObject], out: ScriptOutput) -> None:
    header("Case 4: Missing objects")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Missing object: {item.missing_object}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Blocks: {item.blocks}")
        print(f"Next possible route: {item.next_possible_route}")

    with out.unresolved_obligations():
        out.line(
            "O construction missing objects summarized",
            StatusMark.OBLIGATION,
            f"{len(items)} missing objects block full O construction",
        )


def case_5_rejected_upgrades(items: List[RejectedConstructionUpgrade], out: ScriptOutput) -> None:
    header("Case 5: Rejected construction upgrades")
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
            "O construction upgrades rejected",
            StatusMark.FAIL,
            "partial structure, construction obstruction, recovery audit, insertion, and parent upgrades are rejected",
        )


def case_6_conclusions(items: List[ConstructionConclusion], out: ScriptOutput) -> None:
    header("Case 6: Construction conclusions")
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
            "O construction obstruction conclusion stated",
            StatusMark.DEFER,
            "active O not constructed; controlled underdetermination; obligations summary is next",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("O construction obstruction result:")
    print()
    print("  Active O is not constructed from current objects.")
    print("  Candidate domain/codomain ledgers exist.")
    print("  O(zeta_Bs)=zeta_Bs remains a useful candidate preservation direction.")
    print("  zeta/kappa residual action is not derived.")
    print("  no-overlap pairing is not derived.")
    print("  projection/replacement/constraint law is not derived.")
    print("  divergence behavior is not derived.")
    print("  boundary/source/mass behavior is not derived.")
    print("  recovery selection is rejected, but that does not construct O.")
    print("  This is controlled underdetermination, not a proof that O is impossible.")
    print("  O is not usable in residual control or field equations yet.")
    print()
    print("Possible next script:")
    print("  candidate_O_obligations.py")
    print()
    print("Tiny goblin label:")
    print("  If the tool is not forged, do not swing it.")

    with out.governance_assessments():
        out.line(
            "O construction obstruction classifier complete",
            StatusMark.PASS,
            "active O not constructed; obligations summary remains next",
        )


def record_derivations(ns, symbols: ConstructionLoadSymbols) -> None:
    ns.record_derivation(
        derivation_id="g27_O_obstruction",
        inputs=[
            symbols.domain_gap,
            symbols.codomain_gap,
            symbols.kernel_gap,
            symbols.image_gap,
            symbols.pairing_gap,
            symbols.alg_gap,
            symbols.div_gap,
            symbols.bsm_gap,
            symbols.recovery_gap,
            symbols.insertion_gap,
            symbols.parent_gap,
        ],
        output=symbols.construction_gap,
        method="classify active-O construction as controlled underdetermination under current objects",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="O_obstruction_marker",
        scope="Group 27 active O construction",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g27_obs_sector", "Derive final sector decomposition"),
        ("g27_obs_pairing", "Derive no-overlap pairing or criterion"),
        ("g27_obs_alg", "Derive O algebraic law"),
        ("g27_obs_div", "Derive O divergence behavior"),
        ("g27_obs_bsm", "Derive O boundary/source/mass behavior"),
        ("g27_obs_insert", "Keep B_s/F_zeta insertion separate"),
        ("g27_obs_parent", "Keep parent equation closed"),
        ("g27_obs_next", "Summarize O obligations next"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g27_obs_route"],
            description=(
                "Active O is not constructed under current objects. This is controlled underdetermination, not impossibility."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g27_obs_sector",
        "g27_obs_pairing",
        "g27_obs_alg",
        "g27_obs_div",
        "g27_obs_bsm",
        "g27_obs_insert",
        "g27_obs_parent",
        "g27_obs_next",
    ]

    ns.record_route(RouteRecord(
        route_id="g27_obs_route",
        script_id=SCRIPT_ID,
        name="Group 27 O construction obstruction route",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "active O is not treated as constructed",
            "partial structure is not promoted to usable O",
            "controlled underdetermination is not promoted to impossibility",
            "insertion and parent gates remain closed",
            "obligations summary is next",
        ],
    ))

    for branch_id in [
        "partial_structure_as_O",
        "obstruction_as_impossibility",
        "obstruction_as_residual_control",
        "obstruction_licenses_insertion",
        "obstruction_opens_parent",
        "recovery_audit_constructs_O",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; active O remains not constructed and downstream gates remain closed.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g27_O_not_constructed",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Active O is not constructed from current objects. Candidate domain/codomain and safe-trace preservation structure exist, "
            "but zeta/kappa residual action, no-overlap pairing, algebraic law, divergence behavior, and boundary/source/mass behavior remain underived. "
            "Recovery selection is rejected but does not construct O. This is controlled underdetermination, not O impossibility; O is not usable yet."
        ),
        derivation_ids=["g27_O_obstruction"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate O Construction Obstruction")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    statuses = build_statuses()
    routes = build_routes()
    missing = build_missing_objects()
    upgrades = build_upgrades()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbol_ledger(symbols, out)
    case_2_statuses(statuses, out)
    case_3_routes(routes, out)
    case_4_missing_objects(missing, out)
    case_5_rejected_upgrades(upgrades, out)
    case_6_conclusions(conclusions, out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, symbols)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
