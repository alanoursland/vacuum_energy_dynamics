# Candidate coefficient source boundary divergence guardrails
#
# Group:
#   29_Bs_Fzeta_coefficient_origin
#
# Script type:
#   SOURCE / BOUNDARY / DIVERGENCE GUARDRAIL AUDIT
#
# Purpose
# -------
# Audit whether coefficient-origin candidates preserve source, boundary,
# current, mass, support, and divergence discipline.
#
# Locked-door question:
#
#   Does the surviving coefficient-origin candidate preserve field-equation guardrails?
#
# This script does not derive B_s/F_zeta insertion.
# It does not derive no-overlap sector geometry.
# It does not construct active O.
# It does not derive residual control.
# It does not open the parent equation.
#
# Tiny goblin rule:
#
#   A clean blade still must not cut the pouch.

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
        "CANDIDATE": StatusMark.DEFER,
        "COMPATIBLE_CANDIDATE": StatusMark.INFO,
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
        (
            "g29_residual",
            "29_Bs_Fzeta_coefficient_origin__candidate_residual_interpretation_from_coefficient",
            "g29_residual_interpretation",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g29_membership",
            "29_Bs_Fzeta_coefficient_origin__candidate_coefficient_membership_bridge",
            "g29_membership_bridge",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g29_filter",
            "29_Bs_Fzeta_coefficient_origin__candidate_recovery_smuggling_filter",
            "g29_recovery_filter",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g29_volume_trace",
            "29_Bs_Fzeta_coefficient_origin__candidate_volume_trace_coefficient_origin",
            "g29_volume_trace",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g29_problem",
            "29_Bs_Fzeta_coefficient_origin__candidate_coefficient_origin_problem_ledger",
            "g29_coeff_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g28_summary",
            "28_sector_pairing_no_overlap__candidate_group_28_status_summary",
            "g28_status_summary",
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
class GuardrailSymbols:
    c_Bs: sp.Symbol
    zeta_Bs: sp.Symbol
    T_zeta: sp.Symbol
    S_src: sp.Symbol
    B_bdy: sp.Symbol
    J_cur: sp.Symbol
    M_A: sp.Symbol
    U_sup: sp.Symbol
    Div_c: sp.Symbol
    C_div: sp.Symbol
    source_gap: sp.Symbol
    boundary_gap: sp.Symbol
    current_gap: sp.Symbol
    mass_gap: sp.Symbol
    support_gap: sp.Symbol
    divergence_gap: sp.Symbol
    insertion_gap: sp.Symbol
    guardrail_load: sp.Expr


@dataclass
class GuardrailCandidate:
    name: str
    candidate: str
    status: str
    safe_meaning: str
    risk: str


@dataclass
class GuardrailTest:
    name: str
    test: str
    status: str
    result: str
    implication: str


@dataclass
class GuardrailRequirement:
    name: str
    requirement: str
    status: str
    needed_for: str
    fails_if: str


@dataclass
class RejectedGuardrailShortcut:
    name: str
    shortcut: str
    status: str
    reason: str


@dataclass
class GuardrailConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> GuardrailSymbols:
    (
        c_Bs,
        zeta_Bs,
        T_zeta,
        S_src,
        B_bdy,
        J_cur,
        M_A,
        U_sup,
        Div_c,
        C_div,
        source_gap,
        boundary_gap,
        current_gap,
        mass_gap,
        support_gap,
        divergence_gap,
        insertion_gap,
    ) = sp.symbols(
        "c_Bs zeta_Bs T_zeta S_src B_bdy J_cur M_A U_sup Div_c C_div "
        "source_gap boundary_gap current_gap mass_gap support_gap divergence_gap insertion_gap",
        real=True,
    )

    guardrail_load = sp.simplify(
        source_gap
        + boundary_gap
        + current_gap
        + mass_gap
        + support_gap
        + divergence_gap
        + insertion_gap
    )

    return GuardrailSymbols(
        c_Bs=c_Bs,
        zeta_Bs=zeta_Bs,
        T_zeta=T_zeta,
        S_src=S_src,
        B_bdy=B_bdy,
        J_cur=J_cur,
        M_A=M_A,
        U_sup=U_sup,
        Div_c=Div_c,
        C_div=C_div,
        source_gap=source_gap,
        boundary_gap=boundary_gap,
        current_gap=current_gap,
        mass_gap=mass_gap,
        support_gap=support_gap,
        divergence_gap=divergence_gap,
        insertion_gap=insertion_gap,
        guardrail_load=guardrail_load,
    )


def build_candidates() -> List[GuardrailCandidate]:
    return [
        GuardrailCandidate(
            name="G1: source-safe candidate",
            candidate="coefficient origin does not itself introduce ordinary source load",
            status="COMPATIBLE_CANDIDATE",
            safe_meaning="candidate coefficient can remain source-audit compatible",
            risk="source no-double-counting still not derived",
        ),
        GuardrailCandidate(
            name="G2: boundary-safe candidate",
            candidate="coefficient origin does not repair boundary scalar-tail/shell failure by choice",
            status="COMPATIBLE_CANDIDATE",
            safe_meaning="boundary failure may reject but not select coefficient",
            risk="boundary neutrality still not derived",
        ),
        GuardrailCandidate(
            name="G3: current/mass-safe candidate",
            candidate="coefficient origin does not hide current flux or A-sector mass shift",
            status="COMPATIBLE_CANDIDATE",
            safe_meaning="current and mass loads remain visible",
            risk="current/mass neutralities still not derived",
        ),
        GuardrailCandidate(
            name="G4: support-safe candidate",
            candidate="coefficient origin does not hide seam/support/matching failure",
            status="COMPATIBLE_CANDIDATE",
            safe_meaning="support transition terms remain auditable",
            risk="support/matching neutrality still not derived",
        ),
        GuardrailCandidate(
            name="G5: divergence-compatible candidate",
            candidate="coefficient origin may require explicit divergence correction C_div",
            status="UNDERDETERMINED",
            safe_meaning="correction route allowed if explicit",
            risk="correction becomes hidden source/boundary/current/support load",
        ),
        GuardrailCandidate(
            name="G6: guardrails as insertion",
            candidate="guardrail-compatible coefficient derives B_s/F_zeta insertion",
            status="REJECTED",
            safe_meaning="none",
            risk="guardrail compatibility is not insertion theorem",
        ),
    ]


def build_tests() -> List[GuardrailTest]:
    return [
        GuardrailTest(
            name="T1: source guardrail",
            test="does coefficient origin derive source no-double-counting?",
            status="NOT_DERIVED",
            result="no; it only preserves source audit compatibility",
            implication="source routing remains open",
        ),
        GuardrailTest(
            name="T2: boundary guardrail",
            test="does coefficient origin derive boundary scalar-tail/shell neutrality?",
            status="NOT_DERIVED",
            result="no; boundary failure remains visible",
            implication="boundary neutrality remains open",
        ),
        GuardrailTest(
            name="T3: current guardrail",
            test="does coefficient origin derive current-flux neutrality?",
            status="NOT_DERIVED",
            result="no; current leakage remains visible",
            implication="current neutrality remains open",
        ),
        GuardrailTest(
            name="T4: mass guardrail",
            test="does coefficient origin derive A-sector mass neutrality?",
            status="NOT_DERIVED",
            result="no; mass shifts remain visible",
            implication="mass neutrality remains open",
        ),
        GuardrailTest(
            name="T5: support guardrail",
            test="does coefficient origin derive support/matching neutrality?",
            status="NOT_DERIVED",
            result="no; seam/support/matching terms remain visible",
            implication="support neutrality remains open",
        ),
        GuardrailTest(
            name="T6: divergence guardrail",
            test="does coefficient origin derive divergence-safe behavior?",
            status="NOT_DERIVED",
            result="no; explicit correction route remains candidate only",
            implication="divergence-safe coefficient law remains open",
        ),
        GuardrailTest(
            name="T7: insertion and parent",
            test="does guardrail compatibility derive insertion or parent readiness?",
            status="REJECTED",
            result="no",
            implication="downstream gates remain closed",
        ),
    ]


def build_requirements() -> List[GuardrailRequirement]:
    return [
        GuardrailRequirement(
            name="R1: source visibility",
            requirement="ordinary source load must remain visible and not be hidden in coefficient",
            status="REQUIRED",
            needed_for="source no-double-counting",
            fails_if="coefficient becomes source reservoir",
        ),
        GuardrailRequirement(
            name="R2: boundary visibility",
            requirement="boundary scalar-tail and shell loads must remain visible",
            status="REQUIRED",
            needed_for="boundary neutrality",
            fails_if="coefficient repairs boundary failure by definition",
        ),
        GuardrailRequirement(
            name="R3: current visibility",
            requirement="current-flux loads must remain visible",
            status="REQUIRED",
            needed_for="current neutrality",
            fails_if="coefficient hides current leakage",
        ),
        GuardrailRequirement(
            name="R4: mass visibility",
            requirement="A-sector mass shifts must remain visible",
            status="REQUIRED",
            needed_for="mass neutrality",
            fails_if="coefficient absorbs mass shift",
        ),
        GuardrailRequirement(
            name="R5: support visibility",
            requirement="support, seam, smoothing, and matching loads must remain visible",
            status="REQUIRED",
            needed_for="support/matching neutrality",
            fails_if="coefficient hides support transition failure",
        ),
        GuardrailRequirement(
            name="R6: divergence explicitness",
            requirement="any divergence correction must be explicit and auditable",
            status="REQUIRED",
            needed_for="divergence-safe coefficient law",
            fails_if="C_div becomes hidden source/boundary/current/support load",
        ),
        GuardrailRequirement(
            name="R7: downstream closure",
            requirement="guardrail compatibility must not be upgraded to insertion, O, residual control, or parent closure",
            status="REQUIRED",
            needed_for="theorem hygiene",
            fails_if="compatibility becomes theorem closure",
        ),
    ]


def build_shortcuts() -> List[RejectedGuardrailShortcut]:
    return [
        RejectedGuardrailShortcut(
            name="F1: source hidden in coefficient",
            shortcut="ordinary source load carried by coefficient",
            status="REJECTED",
            reason="source visibility must remain explicit",
        ),
        RejectedGuardrailShortcut(
            name="F2: boundary repair coefficient",
            shortcut="coefficient chosen to cancel boundary scalar-tail/shell failure",
            status="REJECTED",
            reason="boundary failure may reject but not select coefficient",
        ),
        RejectedGuardrailShortcut(
            name="F3: current leak hidden",
            shortcut="current-flux leakage hidden by coefficient",
            status="REJECTED",
            reason="current visibility must remain explicit",
        ),
        RejectedGuardrailShortcut(
            name="F4: mass shift hidden",
            shortcut="A-sector mass shift hidden by coefficient",
            status="REJECTED",
            reason="mass behavior must remain visible",
        ),
        RejectedGuardrailShortcut(
            name="F5: support failure hidden",
            shortcut="support/matching/seam failure hidden by coefficient",
            status="REJECTED",
            reason="support visibility must remain explicit",
        ),
        RejectedGuardrailShortcut(
            name="F6: divergence correction as reservoir",
            shortcut="C_div absorbs source/boundary/current/support failure",
            status="REJECTED",
            reason="correction must be explicit and auditable",
        ),
        RejectedGuardrailShortcut(
            name="F7: guardrail compatibility as insertion",
            shortcut="guardrail-compatible coefficient derives B_s/F_zeta insertion",
            status="REJECTED",
            reason="guardrail compatibility is not insertion theorem",
        ),
        RejectedGuardrailShortcut(
            name="F8: guardrail compatibility opens parent",
            shortcut="guardrail-compatible coefficient opens parent equation",
            status="REJECTED",
            reason="parent gate remains closed",
        ),
    ]


def build_conclusions() -> List[GuardrailConclusion]:
    return [
        GuardrailConclusion(
            name="C1: guardrail compatibility",
            conclusion="coefficient-origin candidate remains guardrail-compatible only as candidate",
            status="COMPATIBLE_CANDIDATE",
            meaning="it preserves visibility but does not prove neutralities",
        ),
        GuardrailConclusion(
            name="C2: source",
            conclusion="source no-double-counting is not derived",
            status="NOT_DERIVED",
            meaning="source routing remains open",
        ),
        GuardrailConclusion(
            name="C3: boundary/current/mass/support",
            conclusion="guardrail neutralities are not derived",
            status="NOT_DERIVED",
            meaning="boundary/current/mass/support loads remain visible obligations",
        ),
        GuardrailConclusion(
            name="C4: divergence",
            conclusion="divergence-safe coefficient law is not derived",
            status="NOT_DERIVED",
            meaning="explicit correction route remains candidate only",
        ),
        GuardrailConclusion(
            name="C5: next route",
            conclusion="coefficient-origin obstruction classifier should run next",
            status="OPEN",
            meaning="classify whether Group 29 derived, partially constrained, or obstructed coefficient origin",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Coefficient guardrail problem")
    print("Question:")
    print()
    print("  Does the surviving coefficient-origin candidate preserve field-equation guardrails?")
    print()
    print("Discipline:")
    print()
    print("  Compatibility is not neutrality.")
    print("  Visibility is not closure.")
    print("  Guardrail survival is not insertion.")
    print()
    print("Tiny goblin rule:")
    print("  A clean blade still must not cut the pouch.")

    with out.governance_assessments():
        out.line(
            "coefficient guardrail audit opened",
            StatusMark.INFO,
            "testing source/boundary/current/mass/support/divergence visibility for coefficient-origin candidate",
        )


def case_1_symbolic_ledger(symbols: GuardrailSymbols, out: ScriptOutput) -> None:
    header("Case 1: Coefficient guardrail symbolic ledger")
    print("Guardrail symbols:")
    print()
    for name in [
        "c_Bs",
        "zeta_Bs",
        "T_zeta",
        "S_src",
        "B_bdy",
        "J_cur",
        "M_A",
        "U_sup",
        "Div_c",
        "C_div",
    ]:
        print(f"  {name} = {sp.sstr(getattr(symbols, name))}")
    print()
    print("Coefficient guardrail load:")
    print()
    print(f"  L_coefficient_guardrails = {sp.sstr(symbols.guardrail_load)}")

    with out.derived_results():
        out.line(
            "coefficient guardrail load stated",
            StatusMark.OBLIGATION,
            f"L_coefficient_guardrails = {sp.sstr(symbols.guardrail_load)}",
        )


def case_2_candidates(items: List[GuardrailCandidate], out: ScriptOutput) -> None:
    header("Case 2: Coefficient guardrail candidates")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Candidate: {item.candidate}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Safe meaning: {item.safe_meaning}")
        print(f"Risk: {item.risk}")

    with out.governance_assessments():
        out.line(
            "coefficient guardrail candidates classified",
            StatusMark.DEFER,
            f"{len(items)} guardrail candidates classified",
        )


def case_3_tests(items: List[GuardrailTest], out: ScriptOutput) -> None:
    header("Case 3: Coefficient guardrail tests")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Test: {item.test}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Result: {item.result}")
        print(f"Implication: {item.implication}")

    with out.governance_assessments():
        out.line(
            "coefficient guardrail tests completed",
            StatusMark.DEFER,
            "guardrail compatibility survives only as candidate; neutralities not derived",
        )


def case_4_requirements(items: List[GuardrailRequirement], out: ScriptOutput) -> None:
    header("Case 4: Coefficient guardrail requirements")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Requirement: {item.requirement}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Needed for: {item.needed_for}")
        print(f"Fails if: {item.fails_if}")

    with out.unresolved_obligations():
        out.line(
            "coefficient guardrail requirements stated",
            StatusMark.OBLIGATION,
            f"{len(items)} guardrail requirements remain open",
        )


def case_5_shortcuts(items: List[RejectedGuardrailShortcut], out: ScriptOutput) -> None:
    header("Case 5: Rejected coefficient guardrail shortcuts")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Shortcut: {item.shortcut}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")

    with out.counterexamples():
        out.line(
            "coefficient guardrail shortcuts rejected",
            StatusMark.FAIL,
            "source hiding, boundary repair, current hiding, mass hiding, support hiding, divergence reservoir, insertion, and parent shortcuts are rejected",
        )


def case_6_conclusions(items: List[GuardrailConclusion], out: ScriptOutput) -> None:
    header("Case 6: Coefficient guardrail conclusions")
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
            "coefficient guardrail conclusion stated",
            StatusMark.DEFER,
            "coefficient-origin obstruction classifier should run next",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Coefficient guardrail result:")
    print()
    print("  Coefficient-origin candidate remains guardrail-compatible only as candidate.")
    print("  It preserves source/boundary/current/mass/support/divergence visibility.")
    print("  Source no-double-counting is not derived.")
    print("  Boundary neutrality is not derived.")
    print("  Current neutrality is not derived.")
    print("  A-sector mass neutrality is not derived.")
    print("  Support/matching neutrality is not derived.")
    print("  Divergence-safe coefficient law is not derived.")
    print("  Explicit correction route remains candidate only.")
    print("  B_s/F_zeta insertion is not derived.")
    print("  Active O, residual control, and parent equation remain not ready.")
    print()
    print("Possible next script:")
    print("  candidate_coefficient_origin_obstruction.py")
    print()
    print("Tiny goblin label:")
    print("  A clean blade still must not cut the pouch.")

    with out.governance_assessments():
        out.line(
            "coefficient guardrail audit complete",
            StatusMark.PASS,
            "visibility preserved; neutralities not derived; obstruction classifier next",
        )


def record_derivations(ns, symbols: GuardrailSymbols) -> None:
    ns.record_derivation(
        derivation_id="g29_guardrails",
        inputs=[
            symbols.source_gap,
            symbols.boundary_gap,
            symbols.current_gap,
            symbols.mass_gap,
            symbols.support_gap,
            symbols.divergence_gap,
            symbols.insertion_gap,
        ],
        output=symbols.guardrail_load,
        method="audit coefficient-origin source/boundary/current/mass/support/divergence guardrails",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="coefficient_guardrail_marker",
        scope="Group 29 B_s/F_zeta coefficient origin",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g29_gr_source", "Derive source no-double-counting if needed"),
        ("g29_gr_boundary", "Derive boundary scalar-tail/shell neutrality"),
        ("g29_gr_current", "Derive current-flux neutrality"),
        ("g29_gr_mass", "Derive A-sector mass neutrality"),
        ("g29_gr_support", "Derive support/matching neutrality"),
        ("g29_gr_divergence", "Derive divergence-safe coefficient law"),
        ("g29_gr_correction", "Keep divergence correction explicit and auditable"),
        ("g29_gr_downstream", "Keep insertion/O/residual/parent gates closed"),
        ("g29_gr_next_obstruction", "Run coefficient-origin obstruction classifier next"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g29_gr_route"],
            description=(
                "Coefficient-origin candidate preserves guardrail visibility only as candidate; neutralities and divergence-safe law are not derived."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g29_gr_source",
        "g29_gr_boundary",
        "g29_gr_current",
        "g29_gr_mass",
        "g29_gr_support",
        "g29_gr_divergence",
        "g29_gr_correction",
        "g29_gr_downstream",
        "g29_gr_next_obstruction",
    ]

    ns.record_route(RouteRecord(
        route_id="g29_gr_route",
        script_id=SCRIPT_ID,
        name="Group 29 coefficient source/boundary/divergence guardrail route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "coefficient-origin candidate preserves visibility only",
            "source no-double-counting is not claimed",
            "boundary/current/mass/support neutralities are not claimed",
            "divergence-safe law is not claimed",
            "insertion, active O, residual control, and parent gates remain closed",
        ],
    ))

    for branch_id in [
        "source_hidden_in_coefficient",
        "boundary_repair_coefficient",
        "current_leak_hidden",
        "mass_shift_hidden",
        "support_failure_hidden",
        "divergence_correction_as_reservoir",
        "guardrail_compatibility_as_insertion",
        "guardrail_compatibility_as_active_O",
        "guardrail_compatibility_as_residual_control",
        "guardrail_compatibility_opens_parent",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; coefficient guardrail compatibility is not insertion, active O, residual control, or parent closure.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g29_guardrails_partial",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Coefficient-origin candidate remains guardrail-compatible only as candidate. It preserves source/boundary/current/mass/support/divergence visibility, "
            "but source no-double-counting, boundary neutrality, current neutrality, A-sector mass neutrality, support/matching neutrality, and divergence-safe coefficient law are not derived. "
            "Explicit correction remains candidate only. B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready."
        ),
        derivation_ids=["g29_guardrails"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Coefficient Source Boundary Divergence Guardrails")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    candidates = build_candidates()
    tests = build_tests()
    requirements = build_requirements()
    shortcuts = build_shortcuts()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbolic_ledger(symbols, out)
    case_2_candidates(candidates, out)
    case_3_tests(tests, out)
    case_4_requirements(requirements, out)
    case_5_shortcuts(shortcuts, out)
    case_6_conclusions(conclusions, out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, symbols)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
