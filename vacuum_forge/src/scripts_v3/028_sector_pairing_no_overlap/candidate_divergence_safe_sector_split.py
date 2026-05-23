# Candidate divergence safe sector split
#
# Group:
#   28_sector_pairing_no_overlap
#
# Script type:
#   DIVERGENCE-SAFE SECTOR SPLIT AUDIT
#
# Purpose
# -------
# Audit whether any candidate sector split can be preserved by derivative/divergence
# without creating hidden correction sources.
#
# Locked-door question:
#
#   Is the candidate sector split preserved by derivative/divergence?
#
# This script does not derive a no-overlap theorem.
# It does not derive active O.
# It does not derive residual control.
# It does not derive B_s/F_zeta insertion.
# It does not derive parent equation closure.
#
# Tiny goblin rule:
#
#   The tunnel must survive the wind.

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
        "INSUFFICIENT": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "UNDERDETERMINED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        ("g28_bdy", "28_sector_pairing_no_overlap__candidate_boundary_support_incidence", "g28_bdy_sup", RecordKind.INVENTORY_MARKER),
        ("g28_as", "28_sector_pairing_no_overlap__candidate_accounting_source_incidence", "g28_acct_src", RecordKind.INVENTORY_MARKER),
        ("g28_tr", "28_sector_pairing_no_overlap__candidate_trace_residual_incidence", "g28_trace_res", RecordKind.INVENTORY_MARKER),
        ("g28_forms", "28_sector_pairing_no_overlap__candidate_pairing_incidence_forms", "g28_pair_forms", RecordKind.INVENTORY_MARKER),
        ("g28_mem", "28_sector_pairing_no_overlap__candidate_sector_membership_rules", "g28_membership", RecordKind.INVENTORY_MARKER),
        ("g28_inv", "28_sector_pairing_no_overlap__candidate_sector_inventory", "g28_sector_inventory", RecordKind.INVENTORY_MARKER),
        ("g28_prob", "28_sector_pairing_no_overlap__candidate_sector_problem_ledger", "g28_sector_problem", RecordKind.INVENTORY_MARKER),
        ("g27_summary", "27_active_O_construction__candidate_group_27_status_summary", "g27_status_summary", RecordKind.INVENTORY_MARKER),
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
class DivergenceSectorSymbols:
    T_zeta: sp.Symbol
    R_zeta: sp.Symbol
    R_kappa: sp.Symbol
    A_eps: sp.Symbol
    A_kappa: sp.Symbol
    Div_T: sp.Symbol
    Div_Rz: sp.Symbol
    Div_Rk: sp.Symbol
    C_div: sp.Symbol
    J_leak: sp.Symbol
    S_hidden: sp.Symbol
    B_hidden: sp.Symbol
    comm_gap: sp.Symbol
    correction_gap: sp.Symbol
    source_gap: sp.Symbol
    boundary_gap: sp.Symbol
    current_gap: sp.Symbol
    sector_gap: sp.Symbol
    div_load: sp.Expr


@dataclass
class DivergenceSectorCandidate:
    name: str
    candidate: str
    status: str
    works_if: str
    hazard: str


@dataclass
class DivergenceSectorTest:
    name: str
    test: str
    status: str
    result: str
    implication: str


@dataclass
class DivergenceSectorRequirement:
    name: str
    requirement: str
    status: str
    needed_for: str
    fails_if: str


@dataclass
class RejectedDivergenceShortcut:
    name: str
    shortcut: str
    status: str
    reason: str


@dataclass
class DivergenceSectorConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> DivergenceSectorSymbols:
    (
        T_zeta,
        R_zeta,
        R_kappa,
        A_eps,
        A_kappa,
        Div_T,
        Div_Rz,
        Div_Rk,
        C_div,
        J_leak,
        S_hidden,
        B_hidden,
        comm_gap,
        correction_gap,
        source_gap,
        boundary_gap,
        current_gap,
        sector_gap,
    ) = sp.symbols(
        "T_zeta R_zeta R_kappa A_eps A_kappa Div_T Div_Rz Div_Rk C_div J_leak S_hidden B_hidden "
        "comm_gap correction_gap source_gap boundary_gap current_gap sector_gap",
        real=True,
    )

    div_load = sp.simplify(comm_gap + correction_gap + source_gap + boundary_gap + current_gap + sector_gap)

    return DivergenceSectorSymbols(
        T_zeta=T_zeta,
        R_zeta=R_zeta,
        R_kappa=R_kappa,
        A_eps=A_eps,
        A_kappa=A_kappa,
        Div_T=Div_T,
        Div_Rz=Div_Rz,
        Div_Rk=Div_Rk,
        C_div=C_div,
        J_leak=J_leak,
        S_hidden=S_hidden,
        B_hidden=B_hidden,
        comm_gap=comm_gap,
        correction_gap=correction_gap,
        source_gap=source_gap,
        boundary_gap=boundary_gap,
        current_gap=current_gap,
        sector_gap=sector_gap,
        div_load=div_load,
    )


def build_candidates() -> List[DivergenceSectorCandidate]:
    return [
        DivergenceSectorCandidate(
            name="D1: strict sector preservation",
            candidate="Div(T_zeta) stays in T_zeta and Div(R_zeta/R_kappa) stays outside T_zeta",
            status="NOT_DERIVED",
            works_if="sector derivative behavior is explicitly derived",
            hazard="sector split is assumed derivative-stable",
        ),
        DivergenceSectorCandidate(
            name="D2: divergence non-reentry",
            candidate="Div(R_zeta/R_kappa) has no route into T_zeta or S_src",
            status="UNDERDETERMINED",
            works_if="routing edge and source laws are derived",
            hazard="residual reentry is hidden by divergence notation",
        ),
        DivergenceSectorCandidate(
            name="D3: explicit correction term",
            candidate="Div(sector split) = sector Div + C_div",
            status="CANDIDATE",
            works_if="C_div is explicit, auditable, and not a hidden source/boundary/current term",
            hazard="correction term becomes hidden source",
        ),
        DivergenceSectorCandidate(
            name="D4: accounting divergence neutrality",
            candidate="Div(A_eps/A_kappa) has no ordinary source/current role",
            status="UNDERDETERMINED",
            works_if="accounting no-reservoir and no-source role laws are derived",
            hazard="accounting sector becomes divergence reservoir",
        ),
        DivergenceSectorCandidate(
            name="D5: support/divergence compatibility",
            candidate="support/matching split is stable under derivative/divergence",
            status="UNDERDETERMINED",
            works_if="boundary/support transition terms are controlled",
            hazard="seam/shell terms become hidden correction",
        ),
        DivergenceSectorCandidate(
            name="D6: recovery-selected divergence split",
            candidate="choose divergence behavior because recovery works",
            status="REJECTED",
            works_if="never allowed",
            hazard="recovery constructs sector geometry",
        ),
    ]


def build_tests() -> List[DivergenceSectorTest]:
    return [
        DivergenceSectorTest(
            name="T1: strict preservation",
            test="is the candidate sector split preserved by derivative/divergence?",
            status="NOT_DERIVED",
            result="no; strict sector preservation is not derived",
            implication="sector geometry is not field-equation usable yet",
        ),
        DivergenceSectorTest(
            name="T2: residual divergence non-reentry",
            test="is Div(R_zeta/R_kappa) excluded from T_zeta and S_src?",
            status="NOT_DERIVED",
            result="no; residual divergence route exclusion is not derived",
            implication="residual non-reentry remains open",
        ),
        DivergenceSectorTest(
            name="T3: correction term admissibility",
            test="can an explicit correction term be allowed?",
            status="CANDIDATE",
            result="yes as candidate if explicit and not a hidden source/boundary/current term",
            implication="correction route remains possible but constrained",
        ),
        DivergenceSectorTest(
            name="T4: accounting divergence neutrality",
            test="is accounting divergence neutrality derived?",
            status="NOT_DERIVED",
            result="no; accounting no-reservoir/source laws are still missing",
            implication="accounting cannot be trusted as divergence sink",
        ),
        DivergenceSectorTest(
            name="T5: support divergence safety",
            test="is support/matching split divergence-safe?",
            status="NOT_DERIVED",
            result="no; seam/shell/transition behavior remains open",
            implication="support split is auxiliary only",
        ),
        DivergenceSectorTest(
            name="T6: downstream closure",
            test="does divergence-safe sector audit close active O or residual control?",
            status="REJECTED",
            result="no",
            implication="downstream gates remain closed",
        ),
    ]


def build_requirements() -> List[DivergenceSectorRequirement]:
    return [
        DivergenceSectorRequirement(
            name="R1: derivative stability",
            requirement="derive how Div acts on candidate sectors",
            status="REQUIRED",
            needed_for="field-equation usability",
            fails_if="sector split is assumed derivative-stable",
        ),
        DivergenceSectorRequirement(
            name="R2: residual non-reentry",
            requirement="prove residual divergence does not reenter trace/source sectors",
            status="REQUIRED",
            needed_for="residual-control pathway",
            fails_if="Div residual becomes ordinary trace/source load",
        ),
        DivergenceSectorRequirement(
            name="R3: explicit correction",
            requirement="any correction term must be explicit and auditable",
            status="REQUIRED",
            needed_for="safe correction route",
            fails_if="C_div becomes hidden source/boundary/current term",
        ),
        DivergenceSectorRequirement(
            name="R4: accounting no-sink",
            requirement="accounting sectors cannot absorb divergence load",
            status="REQUIRED",
            needed_for="accounting discipline",
            fails_if="A_eps/A_kappa become divergence reservoirs",
        ),
        DivergenceSectorRequirement(
            name="R5: support transition control",
            requirement="support/matching derivative terms must remain visible",
            status="REQUIRED",
            needed_for="boundary/support safety",
            fails_if="seam/shell/transition hides correction",
        ),
        DivergenceSectorRequirement(
            name="R6: recovery independence",
            requirement="divergence behavior cannot be selected from recovery success",
            status="REQUIRED",
            needed_for="anti-smuggling",
            fails_if="AB=1/Schwarzschild/gamma chooses divergence law",
        ),
        DivergenceSectorRequirement(
            name="R7: downstream separation",
            requirement="divergence audit does not license active O, residual control, insertion, or parent closure",
            status="REQUIRED",
            needed_for="not overclaiming",
            fails_if="divergence audit becomes theorem closure",
        ),
    ]


def build_shortcuts() -> List[RejectedDivergenceShortcut]:
    return [
        RejectedDivergenceShortcut(
            name="F1: derivative-stable by naming",
            shortcut="sector split is assumed stable under Div because sectors are named",
            status="REJECTED",
            reason="derivative behavior must be derived",
        ),
        RejectedDivergenceShortcut(
            name="F2: residual divergence erased",
            shortcut="Div(R_zeta/R_kappa) declared non-reentrant without edge law",
            status="REJECTED",
            reason="residual divergence non-reentry is not derived",
        ),
        RejectedDivergenceShortcut(
            name="F3: correction as hidden source",
            shortcut="C_div absorbs source/boundary/current failure",
            status="REJECTED",
            reason="correction terms must remain explicit and auditable",
        ),
        RejectedDivergenceShortcut(
            name="F4: accounting divergence sink",
            shortcut="A_eps/A_kappa absorb divergence load",
            status="REJECTED",
            reason="accounting cannot be divergence reservoir",
        ),
        RejectedDivergenceShortcut(
            name="F5: support transition hidden",
            shortcut="seam/shell/transition terms hidden inside support split",
            status="REJECTED",
            reason="support derivative terms must remain visible",
        ),
        RejectedDivergenceShortcut(
            name="F6: recovery-selected divergence",
            shortcut="choose divergence behavior because recovery succeeds",
            status="REJECTED",
            reason="recovery may audit but not construct",
        ),
        RejectedDivergenceShortcut(
            name="F7: divergence audit opens parent",
            shortcut="divergence-safe sector split treated as parent readiness",
            status="REJECTED",
            reason="parent equation remains closed",
        ),
    ]


def build_conclusions() -> List[DivergenceSectorConclusion]:
    return [
        DivergenceSectorConclusion(
            name="C1: strict sector preservation",
            conclusion="strict divergence preservation is not derived",
            status="NOT_DERIVED",
            meaning="sector split is not field-equation usable yet",
        ),
        DivergenceSectorConclusion(
            name="C2: residual divergence non-reentry",
            conclusion="residual divergence non-reentry is not derived",
            status="NOT_DERIVED",
            meaning="Div residual may not yet be excluded from trace/source roles",
        ),
        DivergenceSectorConclusion(
            name="C3: correction route",
            conclusion="explicit correction route remains candidate but constrained",
            status="CANDIDATE",
            meaning="correction cannot be hidden source/boundary/current load",
        ),
        DivergenceSectorConclusion(
            name="C4: accounting/support divergence",
            conclusion="accounting and support divergence safety are not derived",
            status="NOT_DERIVED",
            meaning="accounting/support cannot absorb divergence load",
        ),
        DivergenceSectorConclusion(
            name="C5: next route",
            conclusion="recovery-independent sector geometry should be audited next",
            status="OPEN",
            meaning="divergence behavior cannot be selected from recovery",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Divergence-safe sector split problem")
    print("Question:")
    print()
    print("  Is the candidate sector split preserved by derivative/divergence?")
    print()
    print("Reference discipline:")
    print()
    print("  Sector split is not derivative-stable by naming.")
    print("  Correction terms must not become hidden sources.")
    print("  Divergence behavior may not be recovery-selected.")

    with out.governance_assessments():
        out.line(
            "divergence-safe sector split audit opened",
            StatusMark.INFO,
            "testing derivative/divergence safety without deriving no-overlap theorem",
        )


def case_1_symbol_ledger(symbols: DivergenceSectorSymbols, out: ScriptOutput) -> None:
    header("Case 1: Divergence-safe sector symbolic ledger")
    print("Divergence sector symbols:")
    print()
    for name in ["Div_T", "Div_Rz", "Div_Rk", "C_div", "J_leak", "S_hidden", "B_hidden"]:
        print(f"  {name} = {sp.sstr(getattr(symbols, name))}")
    print()
    print("Divergence-safe sector load:")
    print()
    print(f"  L_div_sector = {sp.sstr(symbols.div_load)}")
    print()
    print("Interpretation:")
    print()
    print("  Strict divergence preservation is not derived.")
    print("  Explicit correction route remains candidate but constrained.")

    with out.derived_results():
        out.line(
            "divergence-safe sector load stated",
            StatusMark.OBLIGATION,
            f"L_div_sector = {sp.sstr(symbols.div_load)}",
        )


def case_2_candidates(items: List[DivergenceSectorCandidate], out: ScriptOutput) -> None:
    header("Case 2: Divergence-safe sector candidates")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Candidate: {item.candidate}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Works if: {item.works_if}")
        print(f"Hazard: {item.hazard}")

    with out.governance_assessments():
        out.line(
            "divergence-safe sector candidates classified",
            StatusMark.DEFER,
            f"{len(items)} divergence-sector candidates classified",
        )


def case_3_tests(items: List[DivergenceSectorTest], out: ScriptOutput) -> None:
    header("Case 3: Divergence-safe sector tests")
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
            "divergence-safe sector tests completed",
            StatusMark.DEFER,
            "strict sector preservation and residual divergence non-reentry are not derived",
        )


def case_4_requirements(items: List[DivergenceSectorRequirement], out: ScriptOutput) -> None:
    header("Case 4: Divergence-safe sector requirements")
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
            "divergence-safe sector requirements stated",
            StatusMark.OBLIGATION,
            f"{len(items)} divergence-sector requirements remain open",
        )


def case_5_shortcuts(items: List[RejectedDivergenceShortcut], out: ScriptOutput) -> None:
    header("Case 5: Rejected divergence-sector shortcuts")
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
            "divergence-sector shortcuts rejected",
            StatusMark.FAIL,
            "derivative-stable by naming, residual divergence erased, correction as hidden source, accounting sink, support transition hiding, recovery selection, and parent readiness are rejected",
        )


def case_6_conclusions(items: List[DivergenceSectorConclusion], out: ScriptOutput) -> None:
    header("Case 6: Divergence-safe sector conclusions")
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
            "divergence-safe sector conclusion stated",
            StatusMark.DEFER,
            "divergence safety not derived; recovery-independent sector geometry is next",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Divergence-safe sector split result:")
    print()
    print("  Strict divergence preservation is not derived.")
    print("  Residual divergence non-reentry is not derived.")
    print("  Explicit correction route remains candidate but constrained.")
    print("  Correction cannot become hidden source, boundary, current, or support load.")
    print("  Accounting sectors cannot absorb divergence load.")
    print("  Support/matching derivative terms must remain visible.")
    print("  Recovery-selected divergence behavior is rejected.")
    print("  No active O, residual control, insertion, or parent closure is licensed.")
    print()
    print("Possible next script:")
    print("  candidate_recovery_independent_sector_geometry.py")
    print()
    print("Tiny goblin label:")
    print("  The tunnel must survive the wind.")

    with out.governance_assessments():
        out.line(
            "divergence-safe sector split audit complete",
            StatusMark.PASS,
            "divergence safety not derived; recovery-independent sector geometry should be audited next",
        )


def record_derivations(ns, symbols: DivergenceSectorSymbols) -> None:
    ns.record_derivation(
        derivation_id="g28_div_safe",
        inputs=[
            symbols.comm_gap,
            symbols.correction_gap,
            symbols.source_gap,
            symbols.boundary_gap,
            symbols.current_gap,
            symbols.sector_gap,
        ],
        output=symbols.div_load,
        method="audit divergence-safe sector split and classify strict preservation as not derived",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="divergence_safe_sector_marker",
        scope="Group 28 sector pairing/no-overlap geometry",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g28_div_derivative", "Derive sector derivative behavior"),
        ("g28_div_residual", "Derive residual divergence non-reentry"),
        ("g28_div_correction", "Constrain explicit divergence correction"),
        ("g28_div_accounting", "Prevent accounting divergence sink"),
        ("g28_div_support", "Preserve support/matching derivative visibility"),
        ("g28_div_recovery", "Reject recovery-selected divergence behavior"),
        ("g28_div_downstream", "Keep O/residual/insertion/parent gates closed"),
        ("g28_div_next_rec", "Audit recovery-independent sector geometry next"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g28_div_route"],
            description=(
                "Divergence-safe sector split is audited here. Strict preservation and residual divergence non-reentry are not derived."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g28_div_derivative",
        "g28_div_residual",
        "g28_div_correction",
        "g28_div_accounting",
        "g28_div_support",
        "g28_div_recovery",
        "g28_div_downstream",
        "g28_div_next_rec",
    ]

    ns.record_route(RouteRecord(
        route_id="g28_div_route",
        script_id=SCRIPT_ID,
        name="Group 28 divergence-safe sector split route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "sector split is not derivative-stable by naming",
            "residual divergence non-reentry is not assumed",
            "correction route remains explicit and auditable",
            "accounting/support cannot absorb divergence load",
            "recovery does not select divergence behavior",
            "downstream gates remain closed",
        ],
    ))

    for branch_id in [
        "derivative_stable_by_naming",
        "residual_divergence_erased",
        "correction_as_hidden_source",
        "accounting_divergence_sink",
        "support_transition_hidden",
        "recovery_selected_divergence",
        "divergence_audit_opens_parent",
        "divergence_audit_as_active_O",
        "divergence_audit_as_residual_control",
        "divergence_audit_as_insertion",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; divergence-safe sector audit is not no-overlap theorem closure.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g28_div_safe_not_derived",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Strict divergence preservation is not derived, and residual divergence non-reentry is not derived. Explicit correction route remains candidate but constrained; "
            "correction cannot become hidden source, boundary, current, or support load. Accounting sectors cannot absorb divergence load, support/matching derivative terms must remain visible, "
            "recovery-selected divergence behavior is rejected, and no downstream gate is opened."
        ),
        derivation_ids=["g28_div_safe"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Divergence Safe Sector Split")
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
    case_1_symbol_ledger(symbols, out)
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
