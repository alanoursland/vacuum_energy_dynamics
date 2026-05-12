# Candidate trace residual incidence
#
# Group:
#   28_sector_pairing_no_overlap
#
# Script type:
#   TRACE / RESIDUAL INCIDENCE AUDIT
#
# Purpose
# -------
# Apply the best candidate no-overlap forms, incidence and routing, to
# T_zeta, R_zeta, and R_kappa.
#
# Locked-door question:
#
#   Can the safe trace sector be separated from zeta/kappa residual sectors?
#
# This script does not derive a no-overlap theorem.
# It does not derive active O.
# It does not derive residual control.
# It does not derive B_s/F_zeta insertion.
# It does not derive parent equation closure.
#
# Tiny goblin rule:
#
#   No secret tunnel from residue to trace.

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


# =============================================================================
# Utilities
# =============================================================================


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_mark(status: str) -> StatusMark:
    return {
        "CANDIDATE": StatusMark.DEFER,
        "CONDITIONALLY_USEFUL": StatusMark.INFO,
        "INSUFFICIENT": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "PARENT_EXCLUDED": StatusMark.FAIL,
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
            "g28_forms",
            "28_sector_pairing_no_overlap__candidate_pairing_incidence_forms",
            "g28_pair_forms",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g28_mem",
            "28_sector_pairing_no_overlap__candidate_sector_membership_rules",
            "g28_membership",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g28_inv",
            "28_sector_pairing_no_overlap__candidate_sector_inventory",
            "g28_sector_inventory",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g28_prob",
            "28_sector_pairing_no_overlap__candidate_sector_problem_ledger",
            "g28_sector_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g27_summary",
            "27_active_O_construction__candidate_group_27_status_summary",
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


# =============================================================================
# Data models
# =============================================================================


@dataclass
class TraceResidualSymbols:
    T_zeta: sp.Symbol
    R_zeta: sp.Symbol
    R_kappa: sp.Symbol
    I_T_Rz: sp.Symbol
    I_T_Rk: sp.Symbol
    E_Rz_T: sp.Symbol
    E_Rk_T: sp.Symbol
    E_Rz_src: sp.Symbol
    E_Rk_src: sp.Symbol
    zeta_Bs: sp.Symbol
    zeta_res: sp.Symbol
    kappa_res: sp.Symbol
    trace_gap: sp.Symbol
    incidence_gap: sp.Symbol
    edge_gap: sp.Symbol
    residual_gap: sp.Symbol
    reentry_gap: sp.Symbol
    tr_load: sp.Expr


@dataclass
class IncidenceCandidate:
    name: str
    candidate: str
    status: str
    works_if: str
    hazard: str


@dataclass
class IncidenceTest:
    name: str
    test: str
    status: str
    result: str
    implication: str


@dataclass
class TraceResidualRequirement:
    name: str
    requirement: str
    status: str
    needed_for: str
    fails_if: str


@dataclass
class RejectedIncidenceShortcut:
    name: str
    shortcut: str
    status: str
    reason: str


@dataclass
class TraceResidualConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


# =============================================================================
# Builders
# =============================================================================


def build_symbols() -> TraceResidualSymbols:
    (
        T_zeta,
        R_zeta,
        R_kappa,
        I_T_Rz,
        I_T_Rk,
        E_Rz_T,
        E_Rk_T,
        E_Rz_src,
        E_Rk_src,
        zeta_Bs,
        zeta_res,
        kappa_res,
        trace_gap,
        incidence_gap,
        edge_gap,
        residual_gap,
        reentry_gap,
    ) = sp.symbols(
        "T_zeta R_zeta R_kappa I_T_Rz I_T_Rk E_Rz_T E_Rk_T E_Rz_src E_Rk_src "
        "zeta_Bs zeta_res kappa_res trace_gap incidence_gap edge_gap residual_gap reentry_gap",
        real=True,
    )

    tr_load = sp.simplify(trace_gap + incidence_gap + edge_gap + residual_gap + reentry_gap)

    return TraceResidualSymbols(
        T_zeta=T_zeta,
        R_zeta=R_zeta,
        R_kappa=R_kappa,
        I_T_Rz=I_T_Rz,
        I_T_Rk=I_T_Rk,
        E_Rz_T=E_Rz_T,
        E_Rk_T=E_Rk_T,
        E_Rz_src=E_Rz_src,
        E_Rk_src=E_Rk_src,
        zeta_Bs=zeta_Bs,
        zeta_res=zeta_res,
        kappa_res=kappa_res,
        trace_gap=trace_gap,
        incidence_gap=incidence_gap,
        edge_gap=edge_gap,
        residual_gap=residual_gap,
        reentry_gap=reentry_gap,
        tr_load=tr_load,
    )


def build_candidates() -> List[IncidenceCandidate]:
    return [
        IncidenceCandidate(
            name="I1: safe trace incidence",
            candidate="zeta_Bs is incident to T_zeta",
            status="CANDIDATE",
            works_if="T_zeta is defined by safe zeta_to_Bs trace role",
            hazard="T_zeta also admits residual trace reentry",
        ),
        IncidenceCandidate(
            name="I2: zeta residual non-incidence",
            candidate="I(T_zeta, R_zeta) = 0",
            status="UNDERDETERMINED",
            works_if="incidence zero is defined by a trace/residual role law",
            hazard="zero incidence is declared by notation",
        ),
        IncidenceCandidate(
            name="I3: kappa residual non-incidence",
            candidate="I(T_zeta, R_kappa) = 0",
            status="UNDERDETERMINED",
            works_if="kappa cannot route back into ordinary trace/source role",
            hazard="kappa residual is hidden by sector label",
        ),
        IncidenceCandidate(
            name="I4: residual-to-trace edge exclusion",
            candidate="no directed edge R_zeta -> T_zeta and no directed edge R_kappa -> T_zeta",
            status="CANDIDATE",
            works_if="edge rules are construction-derived and not selected by recovery/repair",
            hazard="edge deletion by desire",
        ),
        IncidenceCandidate(
            name="I5: residual-to-source edge exclusion",
            candidate="no directed edge R_zeta/R_kappa -> ordinary source sector",
            status="UNDERDETERMINED",
            works_if="source-routing law prevents ordinary source duplication",
            hazard="source no-double-counting assumed",
        ),
        IncidenceCandidate(
            name="I6: support-only separation",
            candidate="support(T_zeta) disjoint from support(R_zeta/R_kappa)",
            status="INSUFFICIENT",
            works_if="also paired with boundary/divergence/reentry controls",
            hazard="transition and boundary terms reintroduce overlap",
        ),
        IncidenceCandidate(
            name="I7: recovery-selected incidence",
            candidate="incidence chosen so AB=1 or Schwarzschild recovery works",
            status="REJECTED",
            works_if="never allowed",
            hazard="recovery constructs incidence",
        ),
    ]


def build_tests() -> List[IncidenceTest]:
    return [
        IncidenceTest(
            name="T1: safe trace assignment",
            test="can zeta_Bs -> T_zeta remain candidate?",
            status="CANDIDATE",
            result="yes, as safe-trace assignment only",
            implication="safe trace survives as candidate anchor",
        ),
        IncidenceTest(
            name="T2: zeta residual zero incidence",
            test="can I(T_zeta, R_zeta)=0 be derived now?",
            status="NOT_DERIVED",
            result="no; zero incidence has no derived rule yet",
            implication="zeta residual non-overlap remains open",
        ),
        IncidenceTest(
            name="T3: kappa residual zero incidence",
            test="can I(T_zeta, R_kappa)=0 be derived now?",
            status="NOT_DERIVED",
            result="no; kappa reentry exclusion has no derived rule yet",
            implication="kappa residual non-overlap remains open",
        ),
        IncidenceTest(
            name="T4: residual-to-trace route exclusion",
            test="can residual-to-trace edges be excluded now?",
            status="UNDERDETERMINED",
            result="not yet; edge rules are not derived",
            implication="routing graph remains promising but open",
        ),
        IncidenceTest(
            name="T5: residual-to-source route exclusion",
            test="can residual-to-source edges be excluded now?",
            status="UNDERDETERMINED",
            result="not yet; source routing law remains open",
            implication="source no-double-counting remains a required audit",
        ),
        IncidenceTest(
            name="T6: support-only separation",
            test="does support-only separation close trace/residual incidence?",
            status="INSUFFICIENT",
            result="no; support cannot control trace/source/divergence reentry alone",
            implication="support can only be auxiliary",
        ),
        IncidenceTest(
            name="T7: downstream closure",
            test="does trace/residual incidence close active O or residual control now?",
            status="REJECTED",
            result="no",
            implication="downstream gates remain closed",
        ),
    ]


def build_requirements() -> List[TraceResidualRequirement]:
    return [
        TraceResidualRequirement(
            name="R1: define trace incidence",
            requirement="state what it means for zeta_Bs to be incident to T_zeta",
            status="REQUIRED",
            needed_for="safe trace membership theorem",
            fails_if="T_zeta is just a name",
        ),
        TraceResidualRequirement(
            name="R2: define residual non-incidence",
            requirement="state what I(T_zeta, R_zeta)=0 and I(T_zeta, R_kappa)=0 mean",
            status="REQUIRED",
            needed_for="no-overlap theorem",
            fails_if="zero incidence is notation only",
        ),
        TraceResidualRequirement(
            name="R3: edge rules",
            requirement="derive routing graph edge rules",
            status="REQUIRED",
            needed_for="residual-to-trace/source exclusion",
            fails_if="edges are deleted because closure needs them gone",
        ),
        TraceResidualRequirement(
            name="R4: no residual erasure",
            requirement="residual non-incidence cannot mean residuals are killed",
            status="REQUIRED",
            needed_for="honest residual classification",
            fails_if="R_zeta/R_kappa become inert by label",
        ),
        TraceResidualRequirement(
            name="R5: source/boundary compatibility",
            requirement="trace/residual incidence must preserve source/boundary/support auditability",
            status="REQUIRED",
            needed_for="guardrail safety",
            fails_if="incidence hides source or boundary leakage",
        ),
        TraceResidualRequirement(
            name="R6: recovery independence",
            requirement="incidence cannot be selected from AB=1, Schwarzschild, gamma, PPN, weak-field, or kappa=0",
            status="REQUIRED",
            needed_for="anti-smuggling",
            fails_if="recovery chooses incidence",
        ),
        TraceResidualRequirement(
            name="R7: downstream separation",
            requirement="trace/residual incidence does not license active O, residual control, insertion, or parent closure",
            status="REQUIRED",
            needed_for="not overclaiming",
            fails_if="incidence audit becomes theorem closure",
        ),
    ]


def build_shortcuts() -> List[RejectedIncidenceShortcut]:
    return [
        RejectedIncidenceShortcut(
            name="F1: zero by notation",
            shortcut="I(T_zeta,R_zeta)=0 written without incidence law",
            status="REJECTED",
            reason="zero incidence must have content",
        ),
        RejectedIncidenceShortcut(
            name="F2: edge deletion by desire",
            shortcut="delete R_zeta/R_kappa -> T_zeta edges because residual control needs them gone",
            status="REJECTED",
            reason="edge rules must be derived",
        ),
        RejectedIncidenceShortcut(
            name="F3: residual non-incidence as inertness",
            shortcut="non-incidence means residuals are inert or killed",
            status="REJECTED",
            reason="non-incidence is not residual erasure",
        ),
        RejectedIncidenceShortcut(
            name="F4: source route ignored",
            shortcut="trace incidence declared while residual-to-source route remains unaudited",
            status="REJECTED",
            reason="source duplication must remain visible",
        ),
        RejectedIncidenceShortcut(
            name="F5: support-only proof",
            shortcut="support disjointness treated as complete trace/residual separation",
            status="REJECTED",
            reason="support separation is insufficient alone",
        ),
        RejectedIncidenceShortcut(
            name="F6: recovery-selected incidence",
            shortcut="choose incidence because recovery succeeds",
            status="REJECTED",
            reason="recovery may audit but not construct",
        ),
        RejectedIncidenceShortcut(
            name="F7: incidence opens parent",
            shortcut="trace/residual incidence treated as parent readiness",
            status="REJECTED",
            reason="parent equation remains closed",
        ),
    ]


def build_conclusions() -> List[TraceResidualConclusion]:
    return [
        TraceResidualConclusion(
            name="C1: safe trace anchor",
            conclusion="zeta_Bs -> T_zeta remains candidate",
            status="CANDIDATE",
            meaning="safe trace anchor survives but is not full no-overlap",
        ),
        TraceResidualConclusion(
            name="C2: zeta residual incidence",
            conclusion="I(T_zeta,R_zeta)=0 is not derived",
            status="NOT_DERIVED",
            meaning="zeta residual non-overlap remains open",
        ),
        TraceResidualConclusion(
            name="C3: kappa residual incidence",
            conclusion="I(T_zeta,R_kappa)=0 is not derived",
            status="NOT_DERIVED",
            meaning="kappa residual non-overlap remains open",
        ),
        TraceResidualConclusion(
            name="C4: routing edges",
            conclusion="residual-to-trace/source routing exclusion is underdetermined",
            status="UNDERDETERMINED",
            meaning="routing graph remains promising but requires edge law",
        ),
        TraceResidualConclusion(
            name="C5: next route",
            conclusion="accounting/source incidence should be audited next",
            status="OPEN",
            meaning="residual-to-source and accounting reservoir risks remain central",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Trace/residual incidence problem")
    print("Question:")
    print()
    print("  Can the safe trace sector be separated from zeta/kappa residual sectors?")
    print()
    print("Reference discipline:")
    print()
    print("  Incidence zero must have content.")
    print("  Routing edges must be derived.")
    print("  Residual non-incidence is not residual erasure.")

    with out.governance_assessments():
        out.line(
            "trace/residual incidence audit opened",
            StatusMark.INFO,
            "testing incidence/routing candidates on T_zeta, R_zeta, and R_kappa",
        )


def case_1_symbol_ledger(symbols: TraceResidualSymbols, out: ScriptOutput) -> None:
    header("Case 1: Trace/residual incidence symbolic ledger")
    print("Trace/residual incidence symbols:")
    print()
    for name in [
        "I_T_Rz",
        "I_T_Rk",
        "E_Rz_T",
        "E_Rk_T",
        "E_Rz_src",
        "E_Rk_src",
    ]:
        print(f"  {name} = {sp.sstr(getattr(symbols, name))}")
    print()
    print("Trace/residual incidence load:")
    print()
    print(f"  L_trace_residual = {sp.sstr(symbols.tr_load)}")
    print()
    print("Interpretation:")
    print()
    print("  Trace/residual incidence is not derived.")
    print("  Candidate safe-trace anchoring survives, but residual edge rules remain open.")

    with out.derived_results():
        out.line(
            "trace/residual incidence load stated",
            StatusMark.OBLIGATION,
            f"L_trace_residual = {sp.sstr(symbols.tr_load)}",
        )


def case_2_candidates(items: List[IncidenceCandidate], out: ScriptOutput) -> None:
    header("Case 2: Trace/residual incidence candidates")
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
            "trace/residual incidence candidates classified",
            StatusMark.DEFER,
            f"{len(items)} trace/residual incidence candidates classified",
        )


def case_3_tests(items: List[IncidenceTest], out: ScriptOutput) -> None:
    header("Case 3: Trace/residual incidence tests")
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
            "trace/residual incidence tests completed",
            StatusMark.DEFER,
            "safe trace anchor survives; residual incidence/routing non-overlap not derived",
        )


def case_4_requirements(items: List[TraceResidualRequirement], out: ScriptOutput) -> None:
    header("Case 4: Trace/residual incidence requirements")
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
            "trace/residual incidence requirements stated",
            StatusMark.OBLIGATION,
            f"{len(items)} requirements remain open for trace/residual non-overlap",
        )


def case_5_shortcuts(items: List[RejectedIncidenceShortcut], out: ScriptOutput) -> None:
    header("Case 5: Rejected trace/residual incidence shortcuts")
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
            "trace/residual incidence shortcuts rejected",
            StatusMark.FAIL,
            "zero by notation, edge deletion by desire, residual inertness, source route ignored, support-only proof, recovery-selected incidence, and parent readiness are rejected",
        )


def case_6_conclusions(items: List[TraceResidualConclusion], out: ScriptOutput) -> None:
    header("Case 6: Trace/residual incidence conclusions")
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
            "trace/residual incidence conclusion stated",
            StatusMark.DEFER,
            "trace/residual non-overlap not derived; accounting/source incidence should be audited next",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Trace/residual incidence result:")
    print()
    print("  zeta_Bs -> T_zeta remains a candidate safe-trace anchor.")
    print("  I(T_zeta, R_zeta)=0 is not derived.")
    print("  I(T_zeta, R_kappa)=0 is not derived.")
    print("  residual-to-trace edge exclusion is underdetermined.")
    print("  residual-to-source edge exclusion is underdetermined.")
    print("  support-only separation is insufficient.")
    print("  residual non-incidence does not mean residual erasure.")
    print("  recovery-selected incidence is rejected.")
    print("  no active O, residual control, insertion, or parent closure is licensed.")
    print()
    print("Possible next script:")
    print("  candidate_accounting_source_incidence.py")
    print()
    print("Tiny goblin label:")
    print("  No secret tunnel from residue to trace.")

    with out.governance_assessments():
        out.line(
            "trace/residual incidence audit complete",
            StatusMark.PASS,
            "safe trace anchor candidate survives; residual incidence not derived",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, symbols: TraceResidualSymbols) -> None:
    ns.record_derivation(
        derivation_id="g28_trace_res",
        inputs=[
            symbols.trace_gap,
            symbols.incidence_gap,
            symbols.edge_gap,
            symbols.residual_gap,
            symbols.reentry_gap,
        ],
        output=symbols.tr_load,
        method="audit trace/residual incidence and classify residual non-overlap as not derived",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="trace_residual_incidence_marker",
        scope="Group 28 sector pairing/no-overlap geometry",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g28_tr_trace", "Define safe trace incidence"),
        ("g28_tr_zeta", "Derive or reject I(T_zeta,R_zeta)=0"),
        ("g28_tr_kappa", "Derive or reject I(T_zeta,R_kappa)=0"),
        ("g28_tr_edges", "Derive routing graph edge rules"),
        ("g28_tr_no_erase", "Prevent residual erasure by non-incidence"),
        ("g28_tr_source", "Audit residual-to-source route"),
        ("g28_tr_recovery", "Reject recovery-selected incidence"),
        ("g28_tr_downstream", "Keep O/residual/insertion/parent gates closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g28_tr_route"],
            description=(
                "Trace/residual incidence is audited here. Safe trace anchor survives as candidate, but residual non-overlap is not derived."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g28_tr_trace",
        "g28_tr_zeta",
        "g28_tr_kappa",
        "g28_tr_edges",
        "g28_tr_no_erase",
        "g28_tr_source",
        "g28_tr_recovery",
        "g28_tr_downstream",
    ]

    ns.record_route(RouteRecord(
        route_id="g28_tr_route",
        script_id=SCRIPT_ID,
        name="Group 28 trace/residual incidence route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "safe trace anchor remains candidate",
            "residual zero incidence is not assumed",
            "routing edges are not deleted by desire",
            "residual non-incidence is not erasure",
            "downstream gates remain closed",
        ],
    ))

    for branch_id in [
        "zero_by_notation",
        "edge_deletion_by_desire",
        "residual_nonincidence_as_inertness",
        "source_route_ignored",
        "support_only_proof",
        "recovery_selected_incidence",
        "incidence_opens_parent",
        "incidence_as_active_O",
        "incidence_as_residual_control",
        "incidence_as_insertion",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; trace/residual incidence audit is not no-overlap theorem closure.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g28_trace_res_not_derived",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "zeta_Bs -> T_zeta remains a candidate safe-trace anchor, but I(T_zeta,R_zeta)=0 and I(T_zeta,R_kappa)=0 are not derived. "
            "Residual-to-trace and residual-to-source edge exclusions are underdetermined. Support-only separation is insufficient. "
            "Residual non-incidence is not residual erasure, recovery-selected incidence is rejected, and no downstream gate is opened."
        ),
        derivation_ids=["g28_trace_res"],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Trace Residual Incidence")
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
