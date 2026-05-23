# Candidate coefficient origin problem ledger
#
# Group:
#   29_Bs_Fzeta_coefficient_origin
#
# Human title:
#   B_s/F_zeta Coefficient Origin
#
# Script type:
#   PROBLEM LEDGER / ROUTE CLASSIFIER
#
# Purpose
# -------
# Open the B_s/F_zeta coefficient-origin problem.
# Classify allowed and forbidden origins for the scalar spatial response coefficient.
#
# Locked-door question:
#
#   What fixes the B_s/F_zeta coefficient and safe scalar membership?
#
# This script does not derive B_s/F_zeta insertion.
# It does not derive no-overlap sector geometry.
# It does not construct active O.
# It does not derive residual control.
# It does not open the parent equation.
#
# Tiny goblin rule:
#
#   Find where the metal came from before forging the key.

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
        "ALLOWED_CANDIDATE": StatusMark.DEFER,
        "CANDIDATE": StatusMark.DEFER,
        "FORBIDDEN": StatusMark.FAIL,
        "HANDOFF_OPEN": StatusMark.PASS,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "THEOREM_TARGET": StatusMark.OBLIGATION,
        "UNDERDETERMINED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g28_summary",
            "028_sector_pairing_no_overlap__candidate_group_28_status_summary",
            "g28_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g28_obligations",
            "028_sector_pairing_no_overlap__candidate_sector_geometry_obligations",
            "g28_obligations",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g27_summary",
            "027_active_O_construction__candidate_group_27_status_summary",
            "g27_status_summary",
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
class CoefficientSymbols:
    B_s: sp.Symbol
    F_zeta: sp.Symbol
    zeta: sp.Symbol
    zeta_Bs: sp.Symbol
    T_zeta: sp.Symbol
    R_zeta: sp.Symbol
    R_kappa: sp.Symbol
    c_vol: sp.Symbol
    c_trace: sp.Symbol
    c_source: sp.Symbol
    c_div: sp.Symbol
    c_recovery: sp.Symbol
    c_postulate: sp.Symbol
    volume_gap: sp.Symbol
    trace_gap: sp.Symbol
    source_gap: sp.Symbol
    divergence_gap: sp.Symbol
    recovery_gap: sp.Symbol
    membership_gap: sp.Symbol
    residual_gap: sp.Symbol
    coefficient_load: sp.Expr


@dataclass
class OriginCandidate:
    name: str
    origin: str
    status: str
    allowed_if: str
    risk: str


@dataclass
class ForbiddenOrigin:
    name: str
    origin: str
    status: str
    reason: str


@dataclass
class Burden:
    name: str
    burden: str
    status: str
    blocks: str
    must_not_do: str


@dataclass
class InitialConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> CoefficientSymbols:
    (
        B_s,
        F_zeta,
        zeta,
        zeta_Bs,
        T_zeta,
        R_zeta,
        R_kappa,
        c_vol,
        c_trace,
        c_source,
        c_div,
        c_recovery,
        c_postulate,
        volume_gap,
        trace_gap,
        source_gap,
        divergence_gap,
        recovery_gap,
        membership_gap,
        residual_gap,
    ) = sp.symbols(
        "B_s F_zeta zeta zeta_Bs T_zeta R_zeta R_kappa "
        "c_vol c_trace c_source c_div c_recovery c_postulate "
        "volume_gap trace_gap source_gap divergence_gap recovery_gap membership_gap residual_gap",
        real=True,
    )

    coefficient_load = sp.simplify(
        volume_gap
        + trace_gap
        + source_gap
        + divergence_gap
        + recovery_gap
        + membership_gap
        + residual_gap
    )

    return CoefficientSymbols(
        B_s=B_s,
        F_zeta=F_zeta,
        zeta=zeta,
        zeta_Bs=zeta_Bs,
        T_zeta=T_zeta,
        R_zeta=R_zeta,
        R_kappa=R_kappa,
        c_vol=c_vol,
        c_trace=c_trace,
        c_source=c_source,
        c_div=c_div,
        c_recovery=c_recovery,
        c_postulate=c_postulate,
        volume_gap=volume_gap,
        trace_gap=trace_gap,
        source_gap=source_gap,
        divergence_gap=divergence_gap,
        recovery_gap=recovery_gap,
        membership_gap=membership_gap,
        residual_gap=residual_gap,
        coefficient_load=coefficient_load,
    )


def build_allowed_candidates() -> List[OriginCandidate]:
    return [
        OriginCandidate(
            name="A1: volume-variation origin",
            origin="zeta = ln sqrt(gamma), delta zeta = 1/2 gamma^ij delta gamma_ij",
            status="ALLOWED_CANDIDATE",
            allowed_if="used as structural trace information, not as full B_s insertion",
            risk="volume algebra may not fix normalization or source behavior",
        ),
        OriginCandidate(
            name="A2: conformal trace origin",
            origin="gamma_ij = exp(2 zeta / 3) bar_gamma_ij, det bar_gamma = 1",
            status="ALLOWED_CANDIDATE",
            allowed_if="used to test trace coefficient and safe scalar channel",
            risk="conformal split is structural, not dynamics",
        ),
        OriginCandidate(
            name="A3: source-routing origin",
            origin="coefficient fixed by count-once ordinary source routing",
            status="THEOREM_TARGET",
            allowed_if="source no-double-counting is independently derived",
            risk="ordinary source load is hidden inside coefficient",
        ),
        OriginCandidate(
            name="A4: divergence-compatible origin",
            origin="coefficient fixed by parent divergence or correction law",
            status="THEOREM_TARGET",
            allowed_if="divergence identity is independently defined",
            risk="divergence language becomes hidden source or parent closure",
        ),
        OriginCandidate(
            name="A5: sector-membership origin",
            origin="coefficient origin upgrades zeta_Bs -> T_zeta from candidate anchor to structural membership",
            status="OPEN",
            allowed_if="membership follows from non-recovery coefficient law",
            risk="sector membership is assumed from desired no-overlap",
        ),
        OriginCandidate(
            name="A6: minimal postulate origin",
            origin="coefficient introduced as explicit new choice/postulate",
            status="HANDOFF_OPEN",
            allowed_if="clearly marked as postulate, not derivation",
            risk="new choice is disguised as theorem",
        ),
    ]


def build_forbidden_origins() -> List[ForbiddenOrigin]:
    return [
        ForbiddenOrigin(
            name="F1: AB=1 selection",
            origin="choose coefficient to make AB=1",
            status="REJECTED",
            reason="AB=1 is downstream recovery audit, not construction",
        ),
        ForbiddenOrigin(
            name="F2: B=1/A selection",
            origin="choose coefficient to make B=1/A",
            status="REJECTED",
            reason="B=1/A is reduced exterior recovery, not parent insertion",
        ),
        ForbiddenOrigin(
            name="F3: Schwarzschild selection",
            origin="choose coefficient from Schwarzschild exterior success",
            status="REJECTED",
            reason="Schwarzschild recovery may audit but not forge the coefficient",
        ),
        ForbiddenOrigin(
            name="F4: gamma/PPN selection",
            origin="choose coefficient to make gamma or PPN work",
            status="REJECTED",
            reason="phenomenology cannot define coefficient origin",
        ),
        ForbiddenOrigin(
            name="F5: weak-field-only selection",
            origin="choose coefficient from weak-field success alone",
            status="REJECTED",
            reason="weak-field recovery is audit-only unless structural coefficient origin is supplied",
        ),
        ForbiddenOrigin(
            name="F6: kappa=0 selection",
            origin="choose coefficient to force kappa_areal = 0",
            status="REJECTED",
            reason="areal kappa is a reduced diagnostic, not coefficient construction",
        ),
        ForbiddenOrigin(
            name="F7: residual cleanup selection",
            origin="choose coefficient to hide zeta/kappa residual trace",
            status="REJECTED",
            reason="coefficient cannot be residual-control repair",
        ),
        ForbiddenOrigin(
            name="F8: boundary/source repair selection",
            origin="choose coefficient to repair boundary, current, mass, support, or source leakage",
            status="REJECTED",
            reason="repair failure may reject but not select coefficient",
        ),
        ForbiddenOrigin(
            name="F9: active-O selection",
            origin="choose coefficient to make active O possible",
            status="REJECTED",
            reason="O is not constructed and cannot select coefficient",
        ),
        ForbiddenOrigin(
            name="F10: parent-fit selection",
            origin="choose coefficient to make parent equation close",
            status="REJECTED",
            reason="parent equation remains closed",
        ),
    ]


def build_burdens() -> List[Burden]:
    return [
        Burden(
            name="B1: coefficient origin",
            burden="derive or classify what fixes the B_s/F_zeta coefficient",
            status="OPEN",
            blocks="B_s/F_zeta insertion",
            must_not_do="choose coefficient from recovery target",
        ),
        Burden(
            name="B2: safe scalar membership",
            burden="determine whether zeta_Bs -> T_zeta is structurally forced",
            status="OPEN",
            blocks="sector membership and no-overlap geometry",
            must_not_do="treat candidate anchor as theorem",
        ),
        Burden(
            name="B3: source discipline",
            burden="prevent ordinary source load from hiding in coefficient",
            status="REQUIRED",
            blocks="source no-double-counting",
            must_not_do="make coefficient a source reservoir",
        ),
        Burden(
            name="B4: residual discipline",
            burden="prevent coefficient origin from killing residuals by label",
            status="REQUIRED",
            blocks="residual-control honesty",
            must_not_do="claim residual control or active O",
        ),
        Burden(
            name="B5: guardrail discipline",
            burden="preserve boundary/current/mass/support visibility",
            status="REQUIRED",
            blocks="field-equation usability",
            must_not_do="repair guardrail failure with coefficient choice",
        ),
        Burden(
            name="B6: divergence discipline",
            burden="classify whether coefficient origin requires divergence identity or correction law",
            status="OPEN",
            blocks="parent readiness",
            must_not_do="use Bianchi-like language as closure",
        ),
        Burden(
            name="B7: parent gate",
            burden="keep parent equation closed",
            status="NOT_READY",
            blocks="premature field equation",
            must_not_do="open parent closure from coefficient-origin audit",
        ),
    ]


def build_conclusions() -> List[InitialConclusion]:
    return [
        InitialConclusion(
            name="C1: group target",
            conclusion="B_s/F_zeta coefficient origin is the correct next target",
            status="HANDOFF_OPEN",
            meaning="Group 28 left safe scalar membership and residual interpretation unresolved",
        ),
        InitialConclusion(
            name="C2: insertion status",
            conclusion="B_s/F_zeta insertion is not derived",
            status="NOT_DERIVED",
            meaning="this group opens coefficient origin only",
        ),
        InitialConclusion(
            name="C3: safe trace anchor",
            conclusion="zeta_Bs -> T_zeta remains candidate",
            status="CANDIDATE",
            meaning="the group may test whether coefficient origin improves this status",
        ),
        InitialConclusion(
            name="C4: recovery selection",
            conclusion="recovery-selected coefficients are rejected",
            status="REJECTED",
            meaning="AB=1, B=1/A, Schwarzschild, gamma/PPN, weak-field, kappa=0, and parent fit cannot choose coefficient",
        ),
        InitialConclusion(
            name="C5: downstream gates",
            conclusion="active O, residual control, insertion, and parent equation remain not ready",
            status="NOT_READY",
            meaning="coefficient-origin audit may not be upgraded to theorem closure",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: B_s/F_zeta coefficient-origin problem")
    print("Question:")
    print()
    print("  What fixes the B_s/F_zeta coefficient and safe scalar membership?")
    print()
    print("Discipline:")
    print()
    print("  Coefficient origin is not insertion.")
    print("  Coefficient origin is not active O.")
    print("  Coefficient origin is not residual control.")
    print("  Coefficient origin is not parent closure.")
    print()
    print("Tiny goblin rule:")
    print("  Find where the metal came from before forging the key.")

    with out.governance_assessments():
        out.line(
            "coefficient-origin problem ledger opened",
            StatusMark.INFO,
            "opening B_s/F_zeta coefficient-origin route after sector-geometry controlled underdetermination",
        )


def case_1_symbol_ledger(symbols: CoefficientSymbols, out: ScriptOutput) -> None:
    header("Case 1: Coefficient-origin symbolic ledger")
    print("Coefficient-origin symbols:")
    print()
    for name in [
        "B_s",
        "F_zeta",
        "zeta",
        "zeta_Bs",
        "T_zeta",
        "R_zeta",
        "R_kappa",
        "c_vol",
        "c_trace",
        "c_source",
        "c_div",
        "c_recovery",
        "c_postulate",
    ]:
        print(f"  {name} = {sp.sstr(getattr(symbols, name))}")
    print()
    print("Coefficient-origin load:")
    print()
    print(f"  L_coefficient_origin = {sp.sstr(symbols.coefficient_load)}")
    print()
    print("Interpretation:")
    print()
    print("  Coefficient origin is open.")
    print("  Recovery may audit coefficient consequences, but may not choose the coefficient.")

    with out.derived_results():
        out.line(
            "coefficient-origin load stated",
            StatusMark.OBLIGATION,
            f"L_coefficient_origin = {sp.sstr(symbols.coefficient_load)}",
        )


def case_2_allowed_candidates(candidates: List[OriginCandidate], out: ScriptOutput) -> None:
    header("Case 2: Allowed coefficient-origin candidates")
    for item in candidates:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Origin: {item.origin}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Allowed if: {item.allowed_if}")
        print(f"Risk: {item.risk}")

    with out.governance_assessments():
        out.line(
            "allowed coefficient-origin candidates classified",
            StatusMark.DEFER,
            f"{len(candidates)} allowed or conditional coefficient-origin candidates classified",
        )


def case_3_forbidden_origins(origins: List[ForbiddenOrigin], out: ScriptOutput) -> None:
    header("Case 3: Forbidden coefficient-origin candidates")
    for item in origins:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Origin: {item.origin}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")

    with out.counterexamples():
        out.line(
            "forbidden coefficient-origin candidates rejected",
            StatusMark.FAIL,
            "recovery, repair, active-O, residual-cleanup, and parent-fit coefficient origins are rejected",
        )


def case_4_burdens(burdens: List[Burden], out: ScriptOutput) -> None:
    header("Case 4: Coefficient-origin burdens")
    for item in burdens:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Burden: {item.burden}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Blocks: {item.blocks}")
        print(f"Must not do: {item.must_not_do}")

    with out.unresolved_obligations():
        out.line(
            "coefficient-origin burdens stated",
            StatusMark.OBLIGATION,
            f"{len(burdens)} burdens opened for coefficient-origin route",
        )


def case_5_conclusions(conclusions: List[InitialConclusion], out: ScriptOutput) -> None:
    header("Case 5: Initial coefficient-origin conclusions")
    for item in conclusions:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Conclusion: {item.conclusion}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Meaning: {item.meaning}")

    with out.governance_assessments():
        out.line(
            "coefficient-origin initial conclusion stated",
            StatusMark.PASS,
            "B_s/F_zeta coefficient origin opened as next constructive route; downstream gates remain closed",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Coefficient-origin problem ledger result:")
    print()
    print("  B_s/F_zeta coefficient origin is opened as the next constructive target.")
    print("  B_s/F_zeta insertion is not derived.")
    print("  zeta_Bs -> T_zeta remains candidate.")
    print("  Volume/trace structure is an allowed candidate origin.")
    print("  Source-routing and divergence-compatible origins are theorem targets only.")
    print("  Minimal postulate origin remains allowed if clearly marked as a choice.")
    print("  Recovery-selected coefficients are rejected.")
    print("  Repair-selected coefficients are rejected.")
    print("  Active-O-selected coefficients are rejected.")
    print("  Parent-fit-selected coefficients are rejected.")
    print("  Active O, residual control, insertion, and parent equation remain not ready.")
    print()
    print("Possible next script:")
    print("  candidate_volume_trace_coefficient_origin.py")
    print()
    print("Tiny goblin label:")
    print("  Find where the metal came from before forging the key.")

    with out.governance_assessments():
        out.line(
            "coefficient-origin problem ledger complete",
            StatusMark.PASS,
            "volume/trace coefficient-origin audit should run next",
        )


def record_derivations(ns, symbols: CoefficientSymbols) -> None:
    ns.record_derivation(
        derivation_id="g29_coeff_problem",
        inputs=[
            symbols.volume_gap,
            symbols.trace_gap,
            symbols.source_gap,
            symbols.divergence_gap,
            symbols.recovery_gap,
            symbols.membership_gap,
            symbols.residual_gap,
        ],
        output=symbols.coefficient_load,
        method="open B_s/F_zeta coefficient-origin burden and classify allowed/rejected origin routes",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="coefficient_origin_problem_marker",
        scope="Group 29 B_s/F_zeta coefficient origin",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g29_coeff_origin", "Derive or classify B_s/F_zeta coefficient origin"),
        ("g29_safe_membership", "Test whether coefficient origin forces zeta_Bs -> T_zeta"),
        ("g29_volume_trace", "Audit volume/trace coefficient origin"),
        ("g29_source", "Prevent coefficient from carrying ordinary source load"),
        ("g29_residual", "Prevent coefficient from acting as residual cleanup"),
        ("g29_guardrails", "Preserve boundary/current/mass/support guardrails"),
        ("g29_divergence", "Classify divergence compatibility"),
        ("g29_recovery", "Reject recovery-selected coefficients"),
        ("g29_downstream", "Keep active O/residual/insertion/parent gates closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g29_coeff_route"],
            description=(
                "The coefficient-origin route is opened. No insertion, active O, residual control, or parent closure is derived."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g29_coeff_origin",
        "g29_safe_membership",
        "g29_volume_trace",
        "g29_source",
        "g29_residual",
        "g29_guardrails",
        "g29_divergence",
        "g29_recovery",
        "g29_downstream",
    ]

    ns.record_route(RouteRecord(
        route_id="g29_coeff_route",
        script_id=SCRIPT_ID,
        name="Group 29 B_s/F_zeta coefficient-origin route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "coefficient origin is not insertion",
            "coefficient origin is not residual control",
            "coefficient origin is not active O",
            "coefficient origin is not parent closure",
            "recovery and repair may not select coefficient",
            "volume/trace origin may be tested next",
        ],
    ))

    for branch_id in [
        "AB1_selected_coefficient",
        "B_inverse_A_selected_coefficient",
        "Schwarzschild_selected_coefficient",
        "gamma_PPN_selected_coefficient",
        "weak_field_selected_coefficient",
        "kappa0_selected_coefficient",
        "residual_cleanup_selected_coefficient",
        "boundary_source_repair_selected_coefficient",
        "active_O_selected_coefficient",
        "parent_fit_selected_coefficient",
        "coefficient_origin_as_insertion",
        "coefficient_origin_as_residual_control",
        "coefficient_origin_as_parent_closure",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; coefficient origin cannot be selected by recovery, repair, active O, residual cleanup, or parent fit.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g29_coeff_origin_opened",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "B_s/F_zeta coefficient origin is opened as the next constructive target after sector-geometry controlled underdetermination. "
            "Volume/trace structure is an allowed candidate origin; source-routing and divergence-compatible origins are theorem targets; minimal postulate origin remains allowed if marked as a choice. "
            "Recovery-selected, repair-selected, residual-cleanup-selected, active-O-selected, and parent-fit-selected coefficients are rejected. "
            "B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready."
        ),
        derivation_ids=["g29_coeff_problem"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Coefficient Origin Problem Ledger")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    allowed = build_allowed_candidates()
    forbidden = build_forbidden_origins()
    burdens = build_burdens()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbol_ledger(symbols, out)
    case_2_allowed_candidates(allowed, out)
    case_3_forbidden_origins(forbidden, out)
    case_4_burdens(burdens, out)
    case_5_conclusions(conclusions, out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, symbols)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
