# Candidate minimal postulate set obstruction
#
# Group:
#   30_minimal_coefficient_sector_postulate_inventory
#
# Script type:
#   MINIMAL POSTULATE SET OBSTRUCTION CLASSIFIER
#
# Purpose
# -------
# Classify whether Group 30 has identified a minimal admissible postulate set,
# found underdetermination, found an overlarge set, or found a blocked route.
#
# Locked-door question:
#
#   Has the minimal coefficient/sector postulate set been identified, or is
#   the choice still underdetermined?
#
# This script does not adopt a new postulate.
# It does not derive B_s/F_zeta insertion.
# It does not derive no-overlap sector geometry.
# It does not construct active O.
# It does not derive residual control.
# It does not open the parent equation.
#
# Tiny goblin rule:
#
#   A tray of teeth is not yet a key.

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
        "ADMISSIBLE_CANDIDATE": StatusMark.INFO,
        "BLOCKED": StatusMark.FAIL,
        "HIGH_RISK": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_IDENTIFIED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "OVERLARGE": StatusMark.FAIL,
        "PARTIAL_INVENTORY": StatusMark.INFO,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "THEOREM_ROUTE_PREFERRED": StatusMark.INFO,
        "UNDERDETERMINED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g30_isd",
            "30_minimal_coefficient_sector_postulate_inventory__candidate_incidence_source_divergence_postulate_inventory",
            "g30_incidence_source_divergence",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_safe_membership",
            "30_minimal_coefficient_sector_postulate_inventory__candidate_safe_trace_membership_postulate",
            "g30_safe_membership",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_trace_norm",
            "30_minimal_coefficient_sector_postulate_inventory__candidate_trace_normalization_postulate",
            "g30_trace_normalization",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_filter",
            "30_minimal_coefficient_sector_postulate_inventory__candidate_postulate_smuggling_filter",
            "g30_postulate_smuggling_filter",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_minimality",
            "30_minimal_coefficient_sector_postulate_inventory__candidate_postulate_minimality_tests",
            "g30_postulate_minimality",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_problem",
            "30_minimal_coefficient_sector_postulate_inventory__candidate_minimal_postulate_problem_ledger",
            "g30_postulate_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g29_summary",
            "29_Bs_Fzeta_coefficient_origin__candidate_group_29_status_summary",
            "g29_status_summary",
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
class ObstructionSymbols:
    P_trace_norm: sp.Symbol
    P_safe_membership: sp.Symbol
    P_guardrail_visibility: sp.Symbol
    P_divergence_explicit: sp.Symbol
    I_high_risk: sp.Symbol
    S_theorem: sp.Symbol
    D_theorem: sp.Symbol
    adoption_gap: sp.Symbol
    minimal_set_gap: sp.Symbol
    insertion_gap: sp.Symbol
    parent_gap: sp.Symbol
    obstruction_load: sp.Expr


@dataclass
class SetCandidate:
    name: str
    set_description: str
    status: str
    result: str
    blocker: str


@dataclass
class ObstructionFinding:
    name: str
    finding: str
    status: str
    meaning: str


@dataclass
class RejectedSet:
    name: str
    set_description: str
    status: str
    reason: str


@dataclass
class ObstructionObligation:
    name: str
    obligation: str
    status: str
    blocks: str
    discipline: str


@dataclass
class ObstructionConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> ObstructionSymbols:
    (
        P_trace_norm,
        P_safe_membership,
        P_guardrail_visibility,
        P_divergence_explicit,
        I_high_risk,
        S_theorem,
        D_theorem,
        adoption_gap,
        minimal_set_gap,
        insertion_gap,
        parent_gap,
    ) = sp.symbols(
        "P_trace_norm P_safe_membership P_guardrail_visibility P_divergence_explicit "
        "I_high_risk S_theorem D_theorem adoption_gap minimal_set_gap insertion_gap parent_gap",
        real=True,
    )

    obstruction_load = sp.simplify(
        P_trace_norm
        + P_safe_membership
        + P_guardrail_visibility
        + P_divergence_explicit
        + I_high_risk
        + S_theorem
        + D_theorem
        + adoption_gap
        + minimal_set_gap
        + insertion_gap
        + parent_gap
    )

    return ObstructionSymbols(
        P_trace_norm=P_trace_norm,
        P_safe_membership=P_safe_membership,
        P_guardrail_visibility=P_guardrail_visibility,
        P_divergence_explicit=P_divergence_explicit,
        I_high_risk=I_high_risk,
        S_theorem=S_theorem,
        D_theorem=D_theorem,
        adoption_gap=adoption_gap,
        minimal_set_gap=minimal_set_gap,
        insertion_gap=insertion_gap,
        parent_gap=parent_gap,
        obstruction_load=obstruction_load,
    )


def build_set_candidates() -> List[SetCandidate]:
    return [
        SetCandidate(
            name="S1: narrow admissible pair",
            set_description="trace normalization + safe trace membership",
            status="PARTIAL_INVENTORY",
            result="admissible as candidate pair only",
            blocker="does not solve incidence, source, divergence, insertion",
        ),
        SetCandidate(
            name="S2: visibility pair",
            set_description="guardrail visibility + divergence explicitness",
            status="PARTIAL_INVENTORY",
            result="admissible as protection pair only",
            blocker="does not derive guardrail neutralities or divergence-safe coefficient law",
        ),
        SetCandidate(
            name="S3: four-candidate set",
            set_description="trace normalization + safe membership + guardrail visibility + divergence explicitness",
            status="UNDERDETERMINED",
            result="best admissible candidate inventory, but not adopted and not sufficient",
            blocker="source no-double-counting and divergence-safe coefficient law remain theorem-route preferred",
        ),
        SetCandidate(
            name="S4: add source no-double-counting",
            set_description="four-candidate set + source no-double-counting postulate",
            status="UNDERDETERMINED",
            result="possible only if source/divergence theorem route fails",
            blocker="source route currently theorem-route preferred",
        ),
        SetCandidate(
            name="S5: add trace/residual incidence",
            set_description="four-candidate set + incidence postulate",
            status="HIGH_RISK",
            result="not adopted; too close to no-overlap/residual control",
            blocker="incidence remains high-risk",
        ),
        SetCandidate(
            name="S6: insertion-ready set",
            set_description="trace normalization + membership + incidence + source once + divergence safety",
            status="OVERLARGE",
            result="rejected",
            blocker="endpoint-selected insertion bundle",
        ),
    ]


def build_findings() -> List[ObstructionFinding]:
    return [
        ObstructionFinding(
            name="F1: minimal set",
            finding="a complete minimal admissible postulate set is not identified",
            status="NOT_IDENTIFIED",
            meaning="candidate inventory exists, but choice remains underdetermined",
        ),
        ObstructionFinding(
            name="F2: admissible candidates",
            finding="trace normalization, safe membership, guardrail visibility, and divergence explicitness survive as admissible candidates",
            status="ADMISSIBLE_CANDIDATE",
            meaning="these are possible teeth, not adopted teeth",
        ),
        ObstructionFinding(
            name="F3: source/divergence route",
            finding="source no-double-counting and divergence-safe coefficient law should remain theorem-route preferred",
            status="THEOREM_ROUTE_PREFERRED",
            meaning="a theorem route may avoid postulating too much",
        ),
        ObstructionFinding(
            name="F4: incidence",
            finding="trace/residual incidence remains high-risk",
            status="HIGH_RISK",
            meaning="too close to no-overlap/residual-control smuggling",
        ),
        ObstructionFinding(
            name="F5: downstream gates",
            finding="insertion, active O, residual control, and parent equation remain not ready",
            status="NOT_READY",
            meaning="postulate inventory does not open theorem closure",
        ),
    ]


def build_rejected_sets() -> List[RejectedSet]:
    return [
        RejectedSet(
            name="R1: adoption by inventory",
            set_description="adopt all admissible candidates because they survived filters",
            status="REJECTED",
            reason="survival is not adoption",
        ),
        RejectedSet(
            name="R2: incidence shortcut",
            set_description="add zero incidence to get no-overlap",
            status="REJECTED",
            reason="incidence remains high-risk and not adopted",
        ),
        RejectedSet(
            name="R3: source repair shortcut",
            set_description="add source no-double-counting to repair source leakage",
            status="REJECTED",
            reason="source failure may reject but not select",
        ),
        RejectedSet(
            name="R4: divergence reservoir shortcut",
            set_description="add divergence correction to absorb hidden loads",
            status="REJECTED",
            reason="correction must remain explicit and non-reservoir",
        ),
        RejectedSet(
            name="R5: insertion bundle",
            set_description="add enough postulates to make B_s/F_zeta insertion work",
            status="REJECTED",
            reason="endpoint-selected closure bundle",
        ),
        RejectedSet(
            name="R6: parent bundle",
            set_description="add enough postulates to open parent equation",
            status="REJECTED",
            reason="parent fit cannot select postulates",
        ),
    ]


def build_obligations() -> List[ObstructionObligation]:
    return [
        ObstructionObligation(
            name="O1: no adoption",
            obligation="do not adopt any candidate postulate in Group 30 summary unless explicitly chosen by user/theory update",
            status="REQUIRED",
            blocks="governance honesty",
            discipline="inventory survival is not adoption",
        ),
        ObstructionObligation(
            name="O2: source/divergence handoff",
            obligation="preserve source/divergence coefficient law as preferred theorem route",
            status="OPEN",
            blocks="field-equation usability",
            discipline="do not postulate source/divergence prematurely",
        ),
        ObstructionObligation(
            name="O3: incidence caution",
            obligation="keep trace/residual incidence high-risk and separate",
            status="REQUIRED",
            blocks="no-overlap/residual-control honesty",
            discipline="do not adopt as shortcut",
        ),
        ObstructionObligation(
            name="O4: summarize inventory",
            obligation="write obligations summary next",
            status="OPEN",
            blocks="Group 30 closure",
            discipline="summary must report underdetermination",
        ),
        ObstructionObligation(
            name="O5: downstream closure",
            obligation="keep insertion/O/residual/parent gates closed",
            status="NOT_READY",
            blocks="premature closure",
            discipline="minimal set obstruction is not theorem closure",
        ),
    ]


def build_conclusions() -> List[ObstructionConclusion]:
    return [
        ObstructionConclusion(
            name="C1: minimal set status",
            conclusion="minimal admissible postulate set is not identified",
            status="UNDERDETERMINED",
            meaning="candidate inventory is narrowed but still not a chosen set",
        ),
        ObstructionConclusion(
            name="C2: admissible core",
            conclusion="admissible core candidates are trace normalization, safe membership, guardrail visibility, and divergence explicitness",
            status="ADMISSIBLE_CANDIDATE",
            meaning="survive filters only; no adoption",
        ),
        ObstructionConclusion(
            name="C3: theorem route",
            conclusion="source/divergence coefficient law remains preferred theorem route",
            status="THEOREM_ROUTE_PREFERRED",
            meaning="may reduce need for source/divergence postulates",
        ),
        ObstructionConclusion(
            name="C4: incidence",
            conclusion="trace/residual incidence remains high-risk",
            status="HIGH_RISK",
            meaning="not safe to adopt directly",
        ),
        ObstructionConclusion(
            name="C5: next",
            conclusion="obligations summary should run next",
            status="OPEN",
            meaning="Group 30 can close as inventory/obstruction, not adoption",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Minimal postulate set obstruction problem")
    print("Question:")
    print()
    print("  Has the minimal coefficient/sector postulate set been identified, or is the choice still underdetermined?")
    print()
    print("Discipline:")
    print()
    print("  This classifier adopts no postulate.")
    print("  It derives no insertion.")
    print("  It opens no parent gate.")
    print()
    print("Tiny goblin rule:")
    print("  A tray of teeth is not yet a key.")

    with out.governance_assessments():
        out.line(
            "minimal postulate set obstruction classifier opened",
            StatusMark.INFO,
            "classifying candidate inventory as identified, underdetermined, overlarge, or blocked",
        )


def case_1_symbolic_ledger(symbols: ObstructionSymbols, out: ScriptOutput) -> None:
    header("Case 1: Minimal postulate set obstruction ledger")
    print("Obstruction symbols:")
    print()
    for name in [
        "P_trace_norm",
        "P_safe_membership",
        "P_guardrail_visibility",
        "P_divergence_explicit",
        "I_high_risk",
        "S_theorem",
        "D_theorem",
        "adoption_gap",
        "minimal_set_gap",
        "insertion_gap",
        "parent_gap",
    ]:
        print(f"  {name} = {sp.sstr(getattr(symbols, name))}")
    print()
    print("Minimal postulate set obstruction load:")
    print()
    print(f"  L_minimal_postulate_set_obstruction = {sp.sstr(symbols.obstruction_load)}")

    with out.derived_results():
        out.line(
            "minimal postulate set obstruction load stated",
            StatusMark.OBLIGATION,
            f"L_minimal_postulate_set_obstruction = {sp.sstr(symbols.obstruction_load)}",
        )


def case_2_set_candidates(items: List[SetCandidate], out: ScriptOutput) -> None:
    header("Case 2: Candidate postulate sets")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Set: {item.set_description}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Result: {item.result}")
        print(f"Blocker: {item.blocker}")

    with out.governance_assessments():
        out.line(
            "candidate postulate sets classified",
            StatusMark.DEFER,
            f"{len(items)} candidate sets classified",
        )


def case_3_findings(items: List[ObstructionFinding], out: ScriptOutput) -> None:
    header("Case 3: Obstruction findings")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Finding: {item.finding}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Meaning: {item.meaning}")

    with out.governance_assessments():
        out.line(
            "minimal postulate set obstruction findings stated",
            StatusMark.DEFER,
            f"{len(items)} obstruction findings stated",
        )


def case_4_rejected_sets(items: List[RejectedSet], out: ScriptOutput) -> None:
    header("Case 4: Rejected postulate sets")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Set: {item.set_description}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")

    with out.counterexamples():
        out.line(
            "rejected postulate sets stated",
            StatusMark.FAIL,
            "adoption-by-inventory, incidence shortcut, source repair, divergence reservoir, insertion bundle, and parent bundle rejected",
        )


def case_5_obligations(items: List[ObstructionObligation], out: ScriptOutput) -> None:
    header("Case 5: Minimal postulate set obstruction obligations")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Obligation: {item.obligation}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Blocks: {item.blocks}")
        print(f"Discipline: {item.discipline}")

    with out.unresolved_obligations():
        out.line(
            "minimal postulate set obstruction obligations stated",
            StatusMark.OBLIGATION,
            f"{len(items)} obligations remain",
        )


def case_6_conclusions(items: List[ObstructionConclusion], out: ScriptOutput) -> None:
    header("Case 6: Minimal postulate set obstruction conclusions")
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
            "minimal postulate set obstruction conclusion stated",
            StatusMark.PASS,
            "minimal set underdetermined; obligations summary next",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Minimal postulate set obstruction result:")
    print()
    print("  A complete minimal admissible postulate set is not identified.")
    print("  The best admissible core candidates are:")
    print("    trace normalization;")
    print("    safe trace membership;")
    print("    guardrail visibility;")
    print("    divergence explicitness.")
    print("  These are not adopted.")
    print("  Source no-double-counting and divergence-safe coefficient law remain theorem-route preferred.")
    print("  Trace/residual incidence remains high-risk.")
    print("  Overlarge insertion/no-overlap/residual/parent bundles are rejected.")
    print("  B_s/F_zeta insertion is not derived.")
    print("  Active O, residual control, and parent equation remain not ready.")
    print()
    print("Possible next script:")
    print("  candidate_minimal_postulate_obligations.py")
    print()
    print("Tiny goblin label:")
    print("  A tray of teeth is not yet a key.")

    with out.governance_assessments():
        out.line(
            "minimal postulate set obstruction classifier complete",
            StatusMark.PASS,
            "Group 30 obligations summary should run next",
        )


def record_derivations(ns, symbols: ObstructionSymbols) -> None:
    ns.record_derivation(
        derivation_id="g30_postulate_set_obstruction",
        inputs=[
            symbols.P_trace_norm,
            symbols.P_safe_membership,
            symbols.P_guardrail_visibility,
            symbols.P_divergence_explicit,
            symbols.I_high_risk,
            symbols.S_theorem,
            symbols.D_theorem,
            symbols.adoption_gap,
            symbols.minimal_set_gap,
            symbols.insertion_gap,
            symbols.parent_gap,
        ],
        output=symbols.obstruction_load,
        method="classify minimal postulate set as underdetermined without adopting postulates",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="minimal_postulate_set_obstruction_marker",
        scope="Group 30 minimal coefficient/sector postulate inventory",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g30_obs_no_adoption", "Do not adopt candidate postulates in Group 30 summary"),
        ("g30_obs_admissible_core", "Preserve admissible core as candidates only"),
        ("g30_obs_source_div_theorem", "Preserve source/divergence theorem route"),
        ("g30_obs_incidence_high_risk", "Keep trace/residual incidence high-risk"),
        ("g30_obs_no_bundles", "Reject overlarge closure bundles"),
        ("g30_obs_summary_next", "Write minimal postulate obligations summary next"),
        ("g30_obs_downstream", "Keep insertion/O/residual/parent gates closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g30_obs_route"],
            description=(
                "Minimal admissible postulate set is not identified. Candidate inventory remains underdetermined and unadopted."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g30_obs_no_adoption",
        "g30_obs_admissible_core",
        "g30_obs_source_div_theorem",
        "g30_obs_incidence_high_risk",
        "g30_obs_no_bundles",
        "g30_obs_summary_next",
        "g30_obs_downstream",
    ]

    ns.record_route(RouteRecord(
        route_id="g30_obs_route",
        script_id=SCRIPT_ID,
        name="Group 30 minimal postulate set obstruction route",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "minimal postulate set not identified",
            "admissible core candidates remain unadopted",
            "source/divergence theorem route remains preferred",
            "trace/residual incidence remains high-risk",
            "overlarge closure bundles rejected",
            "downstream gates remain closed",
        ],
    ))

    for branch_id in [
        "adoption_by_inventory",
        "incidence_shortcut",
        "source_repair_shortcut",
        "divergence_reservoir_shortcut",
        "insertion_bundle",
        "parent_bundle",
        "obstruction_as_adoption",
        "obstruction_as_insertion",
        "obstruction_as_parent_readiness",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; minimal set obstruction is not adoption or theorem closure.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g30_minimal_postulate_set_underdetermined",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "A complete minimal admissible postulate set is not identified. The best admissible core candidates are trace normalization, safe trace membership, guardrail visibility, and divergence explicitness, but these are not adopted. "
            "Source no-double-counting and divergence-safe coefficient law remain theorem-route preferred. Trace/residual incidence remains high-risk. "
            "Overlarge insertion/no-overlap/residual/parent bundles are rejected. B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready."
        ),
        derivation_ids=["g30_postulate_set_obstruction"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Minimal Postulate Set Obstruction")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    sets = build_set_candidates()
    findings = build_findings()
    rejected = build_rejected_sets()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbolic_ledger(symbols, out)
    case_2_set_candidates(sets, out)
    case_3_findings(findings, out)
    case_4_rejected_sets(rejected, out)
    case_5_obligations(obligations, out)
    case_6_conclusions(conclusions, out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, symbols)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
