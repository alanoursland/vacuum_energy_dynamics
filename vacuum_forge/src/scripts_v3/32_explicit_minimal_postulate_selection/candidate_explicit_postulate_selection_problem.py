# Candidate explicit postulate selection problem
#
# Group:
#   32_explicit_minimal_postulate_selection
#
# Human title:
#   Explicit Minimal Postulate Selection
#
# Script type:
#   PROBLEM LEDGER / EXPLICIT-CHOICE ROUTE OPENER
#
# Purpose
# -------
# Open the explicit minimal postulate selection route.
# Define candidate postulate classes, forbidden shortcuts, and adoption discipline.
#
# Locked-door question:
#
#   Can we identify a minimal explicit postulate package sufficient to move the
#   coefficient/sector architecture forward, without pretending the package was derived?
#
# This script does not adopt a postulate.
# It does not derive the complete coefficient law.
# It does not derive B_s/F_zeta insertion.
# It does not derive active O.
# It does not derive residual control.
# It does not open the parent equation.
#
# Tiny goblin rule:
#
#   No more pockets. Now choose teeth openly.

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
        "CANDIDATE_ROUTE": StatusMark.DEFER,
        "DEFERRED": StatusMark.DEFER,
        "EXPLICIT_CHOICE_REQUIRED": StatusMark.OBLIGATION,
        "FORBIDDEN_AS_POSTULATE": StatusMark.FAIL,
        "HIGH_RISK": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "PARTIAL_CONSTRAINT": StatusMark.INFO,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g31_summary",
            "31_source_divergence_coefficient_law__candidate_group_31_status_summary",
            "g31_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_obligations",
            "31_source_divergence_coefficient_law__candidate_source_divergence_obligations",
            "g31_obligations",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_trace_norm",
            "31_source_divergence_coefficient_law__candidate_trace_normalization_from_source_divergence",
            "g31_trace_normalization_fork",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_summary",
            "30_minimal_coefficient_sector_postulate_inventory__candidate_group_30_status_summary",
            "g30_status_summary",
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
class SelectionSymbols:
    P_trace_norm: sp.Symbol
    P_safe_membership: sp.Symbol
    P_guardrail_visibility: sp.Symbol
    P_div_explicitness: sp.Symbol
    P_source_no_hidden: sp.Symbol
    P_incidence_zero: sp.Symbol
    P_active_O: sp.Symbol
    P_residual_kill: sp.Symbol
    P_insertion: sp.Symbol
    P_parent: sp.Symbol
    adoption_load: sp.Expr
    forbidden_load: sp.Expr


@dataclass
class CandidateClass:
    name: str
    candidate: str
    status: str
    role: str
    caution: str


@dataclass
class PackageFamily:
    name: str
    package: str
    status: str
    expected_result: str
    forbidden_upgrade: str


@dataclass
class RejectedShortcut:
    name: str
    shortcut: str
    status: str
    reason: str


@dataclass
class InitialObligation:
    name: str
    obligation: str
    status: str
    blocks: str
    discipline: str


@dataclass
class InitialConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> SelectionSymbols:
    (
        P_trace_norm,
        P_safe_membership,
        P_guardrail_visibility,
        P_div_explicitness,
        P_source_no_hidden,
        P_incidence_zero,
        P_active_O,
        P_residual_kill,
        P_insertion,
        P_parent,
    ) = sp.symbols(
        "P_trace_norm P_safe_membership P_guardrail_visibility P_div_explicitness "
        "P_source_no_hidden P_incidence_zero P_active_O P_residual_kill P_insertion P_parent",
        real=True,
    )

    adoption_load = sp.simplify(
        P_trace_norm
        + P_safe_membership
        + P_guardrail_visibility
        + P_div_explicitness
        + P_source_no_hidden
    )

    forbidden_load = sp.simplify(
        P_incidence_zero + P_active_O + P_residual_kill + P_insertion + P_parent
    )

    return SelectionSymbols(
        P_trace_norm=P_trace_norm,
        P_safe_membership=P_safe_membership,
        P_guardrail_visibility=P_guardrail_visibility,
        P_div_explicitness=P_div_explicitness,
        P_source_no_hidden=P_source_no_hidden,
        P_incidence_zero=P_incidence_zero,
        P_active_O=P_active_O,
        P_residual_kill=P_residual_kill,
        P_insertion=P_insertion,
        P_parent=P_parent,
        adoption_load=adoption_load,
        forbidden_load=forbidden_load,
    )


def build_candidate_classes() -> List[CandidateClass]:
    return [
        CandidateClass(
            name="P1: trace normalization",
            candidate="P_trace_norm",
            status="ADMISSIBLE_CANDIDATE",
            role="choose how B_s reads zeta",
            caution="not derived by source/divergence; must not be recovery-selected or repair-selected",
        ),
        CandidateClass(
            name="P2: safe trace membership",
            candidate="P_safe_membership",
            status="ADMISSIBLE_CANDIDATE",
            role="anchor zeta_Bs -> T_zeta as membership discipline",
            caution="not complete no-overlap geometry and not trace/residual incidence",
        ),
        CandidateClass(
            name="P3: guardrail visibility",
            candidate="P_guardrail_visibility",
            status="ADMISSIBLE_CANDIDATE",
            role="require boundary/source/current/mass/support loads to remain visible and auditable",
            caution="visibility is not neutrality theorem",
        ),
        CandidateClass(
            name="P4: divergence explicitness",
            candidate="P_div_explicitness",
            status="ADMISSIBLE_CANDIDATE",
            role="require correction/divergence behavior to be explicit, auditable, and non-reservoir",
            caution="not full divergence-safe coefficient law",
        ),
        CandidateClass(
            name="P5: source hidden-pocket exclusion",
            candidate="P_source_no_hidden",
            status="ADMISSIBLE_CANDIDATE",
            role="forbid ordinary source load hidden in coefficient/residual/boundary/support/correction/exchange/curvature/parent channels",
            caution="not full source no-double-counting theorem",
        ),
        CandidateClass(
            name="P6: trace/residual zero incidence",
            candidate="P_incidence_zero",
            status="HIGH_RISK",
            role="would assert I(T_zeta,R_zeta)=0 and I(T_zeta,R_kappa)=0",
            caution="too close to no-overlap/residual-control smuggling unless separately derived or explicitly marked as strong postulate",
        ),
        CandidateClass(
            name="P7: active O",
            candidate="P_active_O",
            status="FORBIDDEN_AS_POSTULATE",
            role="would introduce active no-overlap operator",
            caution="operator is not constructed; cannot be adopted by naming",
        ),
        CandidateClass(
            name="P8: residual kill",
            candidate="P_residual_kill",
            status="FORBIDDEN_AS_POSTULATE",
            role="would kill residual trace by declaration",
            caution="residual-control theorem attempt did not derive this",
        ),
        CandidateClass(
            name="P9: insertion",
            candidate="P_insertion",
            status="FORBIDDEN_AS_POSTULATE",
            role="would license B_s/F_zeta insertion",
            caution="insertion is not ready",
        ),
        CandidateClass(
            name="P10: parent closure",
            candidate="P_parent",
            status="FORBIDDEN_AS_POSTULATE",
            role="would open parent field equation",
            caution="parent gate remains closed",
        ),
    ]


def build_package_families() -> List[PackageFamily]:
    return [
        PackageFamily(
            name="Package A: Visibility Only",
            package="P_guardrail_visibility + P_div_explicitness + P_source_no_hidden",
            status="CANDIDATE_ROUTE",
            expected_result="safe discipline package but likely insufficient for coefficient law",
            forbidden_upgrade="must not be treated as trace normalization, membership, insertion, or parent readiness",
        ),
        PackageFamily(
            name="Package B: Trace Anchor",
            package="P_trace_norm + P_safe_membership + P_guardrail_visibility + P_div_explicitness + P_source_no_hidden",
            status="CANDIDATE_ROUTE",
            expected_result="minimal plausible coefficient/sector postulate package if explicit adoption is chosen",
            forbidden_upgrade="must not license residual control, trace/residual incidence, active O, insertion, or parent closure",
        ),
        PackageFamily(
            name="Package C: Too-Strong No-Overlap",
            package="P_trace_norm + P_safe_membership + P_incidence_zero + P_residual_kill",
            status="HIGH_RISK",
            expected_result="likely smuggles no-overlap or residual control",
            forbidden_upgrade="must not be accepted unless explicitly adopted as strong postulate with warning",
        ),
        PackageFamily(
            name="Package D: Parent Closure",
            package="P_insertion + P_active_O + P_parent",
            status="REJECTED",
            expected_result="not ready and not constructed",
            forbidden_upgrade="cannot be adopted as minimal package",
        ),
    ]


def build_rejected_shortcuts() -> List[RejectedShortcut]:
    return [
        RejectedShortcut(
            name="R1: adoption as derivation",
            shortcut="treat adopted postulate as theorem result",
            status="REJECTED",
            reason="explicit choice is not proof",
        ),
        RejectedShortcut(
            name="R2: partial constraints as adoption",
            shortcut="treat Group 31 partial constraints as postulate adoption",
            status="REJECTED",
            reason="Group 31 explicitly adopted no postulate",
        ),
        RejectedShortcut(
            name="R3: recovery-selected postulate",
            shortcut="choose a postulate because AB=1, B=1/A, Schwarzschild, weak-field, gamma/PPN, or kappa=0 recovery works",
            status="REJECTED",
            reason="recovery may audit only after construction",
        ),
        RejectedShortcut(
            name="R4: repair-selected postulate",
            shortcut="choose a postulate because it repairs source, divergence, boundary, residual, or parent failure",
            status="REJECTED",
            reason="failure may reject but not select",
        ),
        RejectedShortcut(
            name="R5: incidence smuggling",
            shortcut="adopt trace/residual incidence inside safe membership",
            status="REJECTED",
            reason="safe membership is not zero incidence",
        ),
        RejectedShortcut(
            name="R6: insertion by package",
            shortcut="treat Package B or any package as B_s/F_zeta insertion",
            status="REJECTED",
            reason="postulate package can at most prepare later insertion-precondition audits",
        ),
        RejectedShortcut(
            name="R7: parent by package",
            shortcut="open parent equation from explicit postulate package",
            status="REJECTED",
            reason="parent gate remains closed",
        ),
    ]


def build_obligations() -> List[InitialObligation]:
    return [
        InitialObligation(
            name="O1: candidate ledger",
            obligation="inventory candidate postulates and classify admissible/high-risk/forbidden status",
            status="OPEN",
            blocks="explicit selection",
            discipline="no accidental adoption",
        ),
        InitialObligation(
            name="O2: dependency graph",
            obligation="map dependencies and no-smuggling edges among candidates",
            status="OPEN",
            blocks="minimality",
            discipline="safe membership is not incidence; explicitness is not divergence-safe theorem",
        ),
        InitialObligation(
            name="O3: package tests",
            obligation="test packages for sufficiency, minimality, and overreach",
            status="OPEN",
            blocks="package recommendation",
            discipline="partial constraint is not coefficient law",
        ),
        InitialObligation(
            name="O4: adoption boundary",
            obligation="do not adopt any postulate in opener script",
            status="REQUIRED",
            blocks="governance integrity",
            discipline="selection route is opened, not executed",
        ),
        InitialObligation(
            name="O5: downstream gates",
            obligation="keep insertion, active O, residual control, and parent equation closed",
            status="NOT_READY",
            blocks="premature closure",
            discipline="postulate-selection problem is not insertion",
        ),
    ]


def build_conclusions() -> List[InitialConclusion]:
    return [
        InitialConclusion(
            name="C1: route opened",
            conclusion="explicit minimal postulate selection route is opened",
            status="CANDIDATE_ROUTE",
            meaning="next honest route after theorem routes closed as partial/underdetermined",
        ),
        InitialConclusion(
            name="C2: no adoption yet",
            conclusion="no postulate is adopted by this opener",
            status="NOT_ADOPTED",
            meaning="candidate ledger only",
        ),
        InitialConclusion(
            name="C3: candidate classes",
            conclusion="admissible, high-risk, and forbidden candidate classes are distinguished",
            status="REQUIRED",
            meaning="prevents accidental overreach",
        ),
        InitialConclusion(
            name="C4: no downstream closure",
            conclusion="B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready",
            status="NOT_READY",
            meaning="postulate-selection route does not open downstream gates",
        ),
        InitialConclusion(
            name="C5: next",
            conclusion="candidate postulate ledger should run next",
            status="OPEN",
            meaning="first concrete audit in Group 32",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Explicit postulate selection problem")
    print("Question:")
    print()
    print("  Can we identify a minimal explicit postulate package sufficient to move the coefficient/sector architecture forward, without pretending the package was derived?")
    print()
    print("Discipline:")
    print()
    print("  This script opens an explicit-choice route.")
    print("  It adopts no postulate.")
    print("  It derives no insertion.")
    print()
    print("Tiny goblin rule:")
    print("  No more pockets. Now choose teeth openly.")

    with out.governance_assessments():
        out.line(
            "explicit postulate selection route opened",
            StatusMark.INFO,
            "opening choice route after Group 31 partial-constraint closure",
        )


def case_1_symbolic_ledger(symbols: SelectionSymbols, out: ScriptOutput) -> None:
    header("Case 1: Explicit selection symbolic ledger")
    print("Candidate postulate symbols:")
    print()
    for name in [
        "P_trace_norm",
        "P_safe_membership",
        "P_guardrail_visibility",
        "P_div_explicitness",
        "P_source_no_hidden",
        "P_incidence_zero",
        "P_active_O",
        "P_residual_kill",
        "P_insertion",
        "P_parent",
    ]:
        print(f"  {name} = {sp.sstr(getattr(symbols, name))}")

    print()
    print("Admissible-package load:")
    print(f"  L_adoption_candidate = {sp.sstr(symbols.adoption_load)}")
    print()
    print("Forbidden/too-strong load:")
    print(f"  L_forbidden = {sp.sstr(symbols.forbidden_load)}")

    with out.derived_results():
        out.line(
            "explicit postulate selection ledgers stated",
            StatusMark.OBLIGATION,
            f"L_adoption_candidate = {sp.sstr(symbols.adoption_load)}; L_forbidden = {sp.sstr(symbols.forbidden_load)}",
        )


def case_2_candidates(items: List[CandidateClass], out: ScriptOutput) -> None:
    header("Case 2: Candidate postulate classes")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Candidate: {item.candidate}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Role: {item.role}")
        print(f"Caution: {item.caution}")

    with out.governance_assessments():
        out.line(
            "candidate postulate classes initialized",
            StatusMark.DEFER,
            f"{len(items)} candidate classes initialized",
        )


def case_3_packages(items: List[PackageFamily], out: ScriptOutput) -> None:
    header("Case 3: Candidate package families")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Package: {item.package}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Expected result: {item.expected_result}")
        print(f"Forbidden upgrade: {item.forbidden_upgrade}")

    with out.governance_assessments():
        out.line(
            "candidate package families initialized",
            StatusMark.DEFER,
            f"{len(items)} package families initialized",
        )


def case_4_rejected(items: List[RejectedShortcut], out: ScriptOutput) -> None:
    header("Case 4: Rejected selection shortcuts")
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
            "explicit selection shortcuts rejected",
            StatusMark.FAIL,
            "adoption-as-derivation, recovery selection, repair selection, incidence smuggling, insertion, and parent shortcuts rejected",
        )


def case_5_obligations(items: List[InitialObligation], out: ScriptOutput) -> None:
    header("Case 5: Initial explicit-selection obligations")
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
            "initial explicit-selection obligations stated",
            StatusMark.OBLIGATION,
            f"{len(items)} obligations opened",
        )


def case_6_conclusions(items: List[InitialConclusion], out: ScriptOutput) -> None:
    header("Case 6: Initial explicit-selection conclusions")
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
            "explicit-selection problem conclusion stated",
            StatusMark.PASS,
            "route opened; no postulate adopted; downstream gates closed",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Explicit minimal postulate selection opener result:")
    print()
    print("  Group 32 is opened as an explicit-choice route.")
    print("  Group 31 is treated as partial constraint only, not law or adoption.")
    print("  No postulate is adopted by this opener.")
    print("  Candidate postulate classes are initialized.")
    print("  Visibility-only and trace-anchor packages are candidate routes.")
    print("  Too-strong no-overlap and parent-closure packages are high-risk or rejected.")
    print("  Adoption-as-derivation, recovery-selected postulates, repair-selected postulates, incidence smuggling, insertion shortcuts, and parent shortcuts are rejected.")
    print("  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.")
    print()
    print("Possible next script:")
    print("  candidate_postulate_candidate_ledger.py")
    print()
    print("Tiny goblin label:")
    print("  No more pockets. Now choose teeth openly.")

    with out.governance_assessments():
        out.line(
            "explicit postulate selection opener complete",
            StatusMark.PASS,
            "candidate postulate ledger should run next",
        )


def record_derivations(ns, symbols: SelectionSymbols) -> None:
    ns.record_derivation(
        derivation_id="g32_explicit_selection_problem",
        inputs=[
            symbols.P_trace_norm,
            symbols.P_safe_membership,
            symbols.P_guardrail_visibility,
            symbols.P_div_explicitness,
            symbols.P_source_no_hidden,
            symbols.P_incidence_zero,
            symbols.P_active_O,
            symbols.P_residual_kill,
            symbols.P_insertion,
            symbols.P_parent,
        ],
        output=symbols.adoption_load + symbols.forbidden_load,
        method="open explicit minimal postulate selection route and classify candidate/forbidden loads",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="explicit_postulate_selection_problem_marker",
        scope="Group 32 explicit minimal postulate selection",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g32_candidate_ledger", "Inventory candidate postulates"),
        ("g32_dependency_graph", "Map postulate dependencies and no-smuggling edges"),
        ("g32_package_tests", "Test package sufficiency, minimality, and overreach"),
        ("g32_no_accidental_adoption", "Do not adopt postulates accidentally"),
        ("g32_no_insertion", "Do not treat package selection as insertion"),
        ("g32_downstream_closed", "Keep insertion/O/residual/parent gates closed"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g32_explicit_selection_route"],
            description=(
                "Group 32 opens explicit minimal postulate selection. This opener adopts no postulate and derives no downstream theorem."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g32_candidate_ledger",
        "g32_dependency_graph",
        "g32_package_tests",
        "g32_no_accidental_adoption",
        "g32_no_insertion",
        "g32_downstream_closed",
    ]

    ns.record_route(RouteRecord(
        route_id="g32_explicit_selection_route",
        script_id=SCRIPT_ID,
        name="Group 32 explicit minimal postulate selection route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "Group 31 closed as partial constraint only",
            "complete coefficient law not derived",
            "trace normalization remains open",
            "safe membership remains open",
            "trace/residual incidence remains high-risk",
            "no Group 30 candidate postulate was adopted",
            "downstream gates remain closed",
        ],
    ))

    for branch_id in [
        "adoption_as_derivation",
        "group31_partial_constraints_as_adoption",
        "recovery_selected_postulate",
        "repair_selected_postulate",
        "incidence_smuggled_in_membership",
        "package_as_insertion",
        "package_as_parent_readiness",
        "active_O_by_postulate_name",
        "residual_kill_by_postulate_name",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; explicit selection opener is not derivation, insertion, O, residual control, or parent closure.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g32_explicit_selection_problem_opened",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Group 32 is opened as an explicit-choice route. Group 31 is treated as partial constraint only, not law or adoption. "
            "No postulate is adopted by this opener. Candidate postulate classes are initialized; visibility-only and trace-anchor packages are candidate routes; "
            "too-strong no-overlap and parent-closure packages are high-risk or rejected. Adoption-as-derivation, recovery-selected postulates, repair-selected postulates, "
            "incidence smuggling, insertion shortcuts, and parent shortcuts are rejected. B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready."
        ),
        derivation_ids=["g32_explicit_selection_problem"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Explicit Postulate Selection Problem")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    candidates = build_candidate_classes()
    packages = build_package_families()
    rejected = build_rejected_shortcuts()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbolic_ledger(symbols, out)
    case_2_candidates(candidates, out)
    case_3_packages(packages, out)
    case_4_rejected(rejected, out)
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
