# Candidate safe trace membership obligations
#
# Group:
#   34_safe_trace_membership_candidate_origin
#
# Human title:
#   Safe Trace Membership Candidate Origin
#
# Script type:
#   OBLIGATIONS / STATUS BRIDGE
#
# Purpose
# -------
# Summarize surviving safe-membership candidate forms, failed forms,
# unresolved membership decisions, and safe handoffs before the Group 34 status
# summary.
#
# Locked-door question:
#
#   What safe-membership obligations remain after the compatibility sieve,
#   and what can safely be handed off without selecting or adopting membership?
#
# This script does not choose safe membership.
# It does not adopt a safe-membership postulate.
# It does not derive a safe-membership theorem.
# It does not derive trace/residual zero incidence.
# It does not derive B_s/F_zeta insertion.
# It does not open active O, residual control, or parent closure.
#
# Tiny goblin rule:
#
#   Count the shelves. Still no shelving.

from dataclasses import dataclass
from pathlib import Path
from typing import List

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
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


def subheader(title: str) -> None:
    print()
    print("-" * 120)
    print(title)
    print("-" * 120)


def status_mark(status: str) -> StatusMark:
    return {
        "COMPATIBLE_IF_DECLARED": StatusMark.INFO,
        "COMPATIBILITY_ONLY": StatusMark.INFO,
        "FILTER_FAIL": StatusMark.FAIL,
        "HANDOFF_READY": StatusMark.INFO,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REQUIRED": StatusMark.OBLIGATION,
        "SUMMARY": StatusMark.INFO,
        "VALID_IF_INERT": StatusMark.INFO,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g34_compatibility_sieve",
            "034_safe_trace_membership_candidate_origin__candidate_safe_trace_membership_compatibility_sieve",
            "g34_safe_membership_compatibility_sieve",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g34_candidate_forms",
            "034_safe_trace_membership_candidate_origin__candidate_safe_trace_membership_candidate_forms",
            "g34_safe_membership_candidate_forms",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g34_selector_firewall",
            "034_safe_trace_membership_candidate_origin__candidate_safe_trace_membership_selector_rejection",
            "g34_safe_membership_selector_rejection",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g34_domain_ledger",
            "034_safe_trace_membership_candidate_origin__candidate_safe_trace_membership_domain_ledger",
            "g34_safe_membership_domain_ledger",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g34_origin_problem",
            "034_safe_trace_membership_candidate_origin__candidate_safe_trace_membership_origin_problem",
            "g34_safe_membership_origin_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g33_summary",
            "033_trace_normalization_candidate_origin__candidate_group_33_status_summary",
            "g33_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g32_summary",
            "032_explicit_minimal_postulate_selection__candidate_group_32_status_summary",
            "g32_status_summary",
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
class MembershipObligationSymbols:
    M_safe: sp.Symbol
    M_typed: sp.Symbol
    M_role_pure: sp.Symbol
    M_norm_compat: sp.Symbol
    M_diag: sp.Symbol
    O_membership_criterion: sp.Symbol
    O_role_purity: sp.Symbol
    O_norm_separation: sp.Symbol
    O_inert_label: sp.Symbol
    F_ambiguous_domain: sp.Symbol
    F_hidden_source: sp.Symbol
    F_hidden_divergence: sp.Symbol
    F_residual_payload: sp.Symbol
    F_membership_collapse: sp.Symbol
    F_downstream_use: sp.Symbol
    P_insertion: sp.Symbol
    P_active_O: sp.Symbol
    P_residual_kill: sp.Symbol
    P_parent: sp.Symbol
    L_surviving_forms: sp.Expr
    L_failed_modes: sp.Expr
    L_open_decisions: sp.Expr
    L_downstream_closed: sp.Expr
    L_obligation_gap: sp.Expr


@dataclass
class SurvivingFormEntry:
    name: str
    form: str
    status: str
    survives_if: str
    remaining_decision: str
    boundary: str


@dataclass
class FailureModeEntry:
    name: str
    failure: str
    status: str
    reason: str
    consequence: str


@dataclass
class OpenDecisionEntry:
    name: str
    decision: str
    status: str
    blocks: str
    discipline: str


@dataclass
class HandoffEntry:
    name: str
    handoff: str
    status: str
    reason: str
    caution: str


@dataclass
class MembershipObligationEntry:
    name: str
    obligation: str
    status: str
    blocks: str
    discipline: str


def case_0_problem(out: ScriptOutput) -> None:
    header("Case 0: Safe-membership obligations problem")
    print("Question:\n")
    print("  What safe-membership obligations remain after the compatibility sieve,")
    print("  and what can safely be handed off without selecting or adopting membership?\n")
    print("Discipline:\n")
    print("  This script summarizes obligations.")
    print("  It adopts no safe-membership postulate.")
    print("  It selects no final membership form.")
    print("  It derives no safe-membership theorem.")
    print("  It derives no trace/residual zero incidence.")
    print("  It derives no coefficient law and no insertion.")
    print("  It keeps active O, residual control, and parent closure closed.\n")
    print("Tiny goblin rule:")
    print("  Count the shelves. Still no shelving.\n")

    with out.governance_assessments():
        out.line(
            "safe-membership obligations summary opened",
            StatusMark.INFO,
            "summarizing surviving forms, failed filters, open decisions, and safe handoffs",
        )


def case_1_symbolic_ledger(out: ScriptOutput) -> MembershipObligationSymbols:
    header("Case 1: Safe-membership obligations symbolic ledger")

    M_safe, M_typed, M_role_pure, M_norm_compat, M_diag = sp.symbols(
        "M_safe M_typed M_role_pure M_norm_compat M_diag"
    )
    O_membership_criterion, O_role_purity, O_norm_separation, O_inert_label = sp.symbols(
        "O_membership_criterion O_role_purity O_norm_separation O_inert_label"
    )
    F_ambiguous_domain, F_hidden_source, F_hidden_divergence, F_residual_payload = sp.symbols(
        "F_ambiguous_domain F_hidden_source F_hidden_divergence F_residual_payload"
    )
    F_membership_collapse, F_downstream_use = sp.symbols(
        "F_membership_collapse F_downstream_use"
    )
    P_insertion, P_active_O, P_residual_kill, P_parent = sp.symbols(
        "P_insertion P_active_O P_residual_kill P_parent"
    )

    L_surviving_forms = sp.simplify(M_typed + M_role_pure + M_norm_compat + M_diag)
    L_failed_modes = sp.simplify(
        F_ambiguous_domain + F_hidden_source + F_hidden_divergence + F_residual_payload + F_membership_collapse + F_downstream_use
    )
    L_open_decisions = sp.simplify(
        O_membership_criterion + O_role_purity + O_norm_separation + O_inert_label
    )
    L_downstream_closed = sp.simplify(P_active_O + P_insertion + P_parent + P_residual_kill)
    L_obligation_gap = sp.simplify(
        M_safe + L_surviving_forms + L_failed_modes + L_open_decisions + L_downstream_closed
    )

    print("Candidate / decision / gate symbols:\n")
    for sym in (
        M_safe,
        M_typed,
        M_role_pure,
        M_norm_compat,
        M_diag,
        O_membership_criterion,
        O_role_purity,
        O_norm_separation,
        O_inert_label,
    ):
        print(f"  {sym} = {sym}")
    print()
    print(f"Surviving-form load:\n  L_surviving_forms = {L_surviving_forms}\n")
    print(f"Failed-mode load:\n  L_failed_modes = {L_failed_modes}\n")
    print(f"Open-decision load:\n  L_open_decisions = {L_open_decisions}\n")
    print(f"Downstream closed load:\n  L_downstream_closed = {L_downstream_closed}\n")
    print(f"Obligation gap:\n  L_obligation_gap = {L_obligation_gap}\n")

    with out.derived_results():
        out.line(
            "safe-membership obligation loads stated",
            StatusMark.OBLIGATION,
            f"L_open_decisions={L_open_decisions}; L_downstream_closed={L_downstream_closed}",
        )

    return MembershipObligationSymbols(
        M_safe=M_safe,
        M_typed=M_typed,
        M_role_pure=M_role_pure,
        M_norm_compat=M_norm_compat,
        M_diag=M_diag,
        O_membership_criterion=O_membership_criterion,
        O_role_purity=O_role_purity,
        O_norm_separation=O_norm_separation,
        O_inert_label=O_inert_label,
        F_ambiguous_domain=F_ambiguous_domain,
        F_hidden_source=F_hidden_source,
        F_hidden_divergence=F_hidden_divergence,
        F_residual_payload=F_residual_payload,
        F_membership_collapse=F_membership_collapse,
        F_downstream_use=F_downstream_use,
        P_insertion=P_insertion,
        P_active_O=P_active_O,
        P_residual_kill=P_residual_kill,
        P_parent=P_parent,
        L_surviving_forms=L_surviving_forms,
        L_failed_modes=L_failed_modes,
        L_open_decisions=L_open_decisions,
        L_downstream_closed=L_downstream_closed,
        L_obligation_gap=L_obligation_gap,
    )


def case_2_surviving_forms(out: ScriptOutput) -> List[SurvivingFormEntry]:
    header("Case 2: Surviving membership forms")
    entries = [
        SurvivingFormEntry(
            name="S1: typed trace-sector assignment",
            form="zeta_Bs -> T_zeta with declared object, sector, domain, codomain, and criterion",
            status="COMPATIBLE_IF_DECLARED",
            survives_if="membership objects and criterion are declared before use",
            remaining_decision="declare the actual membership criterion and whether it is theorem target or explicit choice",
            boundary="survival is not selection, adoption, theorem proof, incidence, or insertion",
        ),
        SurvivingFormEntry(
            name="S2: role-pure trace-payload assignment",
            form="zeta_Bs belongs to T_zeta only as trace-sector payload",
            status="COMPATIBLE_IF_DECLARED",
            survives_if="residual, source, correction, and downstream payloads remain excluded",
            remaining_decision="state how role purity is enforced without claiming residual kill or source theorem",
            boundary="role-purity is not full source/divergence/residual theorem",
        ),
        SurvivingFormEntry(
            name="S3: normalization-compatible membership",
            form="membership coexists with separately declared N_trace",
            status="COMPATIBILITY_ONLY",
            survives_if="trace normalization remains a separate Group 33 node",
            remaining_decision="declare compatibility after N_trace convention is stated, without collapse",
            boundary="compatibility does not choose normalization or membership",
        ),
        SurvivingFormEntry(
            name="S4: diagnostic-only trace label",
            form="zeta_Bs is labeled as T_zeta for audit only",
            status="VALID_IF_INERT",
            survives_if="label has no source, metric, residual, insertion, parent, or equation-modifying effect",
            remaining_decision="decide whether future use remains diagnostic-only or seeks active membership theorem",
            boundary="diagnostic label is not adopted membership or insertion",
        ),
    ]

    for item in entries:
        subheader(item.name)
        print(f"Form: {item.form}")
        with out.governance_assessments():
            out.line(item.name, status_mark(item.status), item.status)
        print(f"Survives if: {item.survives_if}")
        print(f"Remaining decision: {item.remaining_decision}")
        print(f"Boundary: {item.boundary}")

    with out.governance_assessments():
        out.line("surviving membership forms summarized", StatusMark.DEFER, "forms survive conditionally; none selected or adopted")

    return entries


def case_3_failure_modes(out: ScriptOutput) -> List[FailureModeEntry]:
    header("Case 3: Failed forms and filter failures")
    entries = [
        FailureModeEntry(
            name="F1: undeclared membership objects",
            failure="membership object, sector, domain, codomain, or criterion is undeclared",
            status="FILTER_FAIL",
            reason="sector label alone is not proof",
            consequence="membership remains ambiguous",
        ),
        FailureModeEntry(
            name="F2: residual payload",
            failure="membership form includes residual zeta or residual kappa payload",
            status="FILTER_FAIL",
            reason="membership is not residual control",
            consequence="form smuggles residual kill or incidence",
        ),
        FailureModeEntry(
            name="F3: hidden ordinary source load",
            failure="membership form carries ordinary source load",
            status="FILTER_FAIL",
            reason="ordinary source load must remain visible and protected",
            consequence="form becomes hidden source pocket",
        ),
        FailureModeEntry(
            name="F4: hidden divergence reservoir",
            failure="membership form carries hidden correction/divergence reservoir load",
            status="FILTER_FAIL",
            reason="divergence explicitness requires non-reservoir behavior",
            consequence="form becomes correction reservoir",
        ),
        FailureModeEntry(
            name="F5: normalization collapse",
            failure="membership chooses trace normalization or is chosen by trace normalization",
            status="FILTER_FAIL",
            reason="Package B keeps normalization and membership separate",
            consequence="Package B collapses into one hidden choice",
        ),
        FailureModeEntry(
            name="F6: downstream use",
            failure="membership form is treated as insertion, active O, residual control, or parent readiness",
            status="FILTER_FAIL",
            reason="downstream gates remain closed",
            consequence="candidate compatibility becomes theorem closure by shortcut",
        ),
    ]

    for item in entries:
        subheader(item.name)
        print(f"Failure: {item.failure}")
        with out.counterexamples():
            out.line(item.name, status_mark(item.status), item.status)
        print(f"Reason: {item.reason}")
        print(f"Consequence: {item.consequence}")

    with out.counterexamples():
        out.line("failed compatibility modes summarized", StatusMark.FAIL, "ambiguous objects, hidden payloads, Package B collapse, and downstream use fail")

    return entries


def case_4_open_decisions(out: ScriptOutput) -> List[OpenDecisionEntry]:
    header("Case 4: Open membership decisions")
    entries = [
        OpenDecisionEntry(
            name="D1: membership criterion",
            decision="declare the criterion by which zeta_Bs belongs to T_zeta",
            status="OPEN",
            blocks="safe-membership theorem attempt or explicit adoption",
            discipline="compatible-if-declared is not selected",
        ),
        OpenDecisionEntry(
            name="D2: role-purity enforcement",
            decision="state how residual/source/correction payloads remain outside membership",
            status="OPEN",
            blocks="hidden-load smuggling control",
            discipline="role-purity is not residual kill or source theorem",
        ),
        OpenDecisionEntry(
            name="D3: normalization compatibility declaration",
            decision="state compatibility with the separately declared Group 33 trace-normalization convention",
            status="OPEN",
            blocks="Package B component use",
            discipline="membership is not normalization",
        ),
        OpenDecisionEntry(
            name="D4: diagnostic versus active membership scope",
            decision="decide whether membership remains diagnostic-only or seeks an active typed-sector theorem",
            status="OPEN",
            blocks="future downstream use",
            discipline="diagnostic label cannot alter equations",
        ),
        OpenDecisionEntry(
            name="D5: adoption boundary",
            decision="whether to explicitly adopt P_safe_membership remains a separate user/theory decision",
            status="OPEN",
            blocks="postulate use downstream",
            discipline="obligations summary is not adoption",
        ),
    ]

    for item in entries:
        subheader(item.name)
        print(f"Decision: {item.decision}")
        with out.unresolved_obligations():
            out.line(item.name, status_mark(item.status), item.status)
        print(f"Blocks: {item.blocks}")
        print(f"Discipline: {item.discipline}")

    with out.unresolved_obligations():
        out.line("open membership decisions summarized", StatusMark.OBLIGATION, "membership criterion, role purity, normalization compatibility, scope, and adoption remain open")

    return entries


def case_5_handoffs(out: ScriptOutput) -> List[HandoffEntry]:
    header("Case 5: Safe handoffs")
    entries = [
        HandoffEntry(
            name="H1: Group 34 status summary",
            handoff="candidate_group_34_status_summary.py",
            status="HANDOFF_READY",
            reason="compatibility sieve has enough information to summarize surviving forms and open decisions",
            caution="summary must not select or adopt safe membership",
        ),
        HandoffEntry(
            name="H2: explicit safe-membership decision",
            handoff="explicit adoption decision record",
            status="OPEN",
            reason="P_safe_membership remains candidate if the theory owner wants to choose it explicitly",
            caution="adopted postulate must not be called derived",
        ),
        HandoffEntry(
            name="H3: safe-membership theorem route",
            handoff="theorem attempt for a declared typed membership criterion",
            status="OPEN",
            reason="surviving forms remain theorem targets after declarations",
            caution="must declare object, sector, domain, codomain, criterion, and exclusion zones first",
        ),
        HandoffEntry(
            name="H4: trace-anchor package continuation",
            handoff="Package B component compatibility continuation",
            status="CONDITIONAL",
            reason="membership and normalization remain separate components that may later be jointly audited",
            caution="Package B compatibility is not insertion",
        ),
        HandoffEntry(
            name="H5: insertion-precondition inventory",
            handoff="conditional precondition inventory only",
            status="NOT_READY",
            reason="safe membership is not selected/adopted and incidence/residual/no-overlap gates remain open",
            caution="must not be called insertion theorem",
        ),
        HandoffEntry(
            name="H6: parent field equation",
            handoff="parent route",
            status="NOT_READY",
            reason="scalar recombination and downstream gates remain unresolved",
            caution="parent gate remains closed",
        ),
    ]

    for item in entries:
        subheader(item.name)
        print(f"Handoff: {item.handoff}")
        with out.governance_assessments():
            out.line(item.name, status_mark(item.status), item.status)
        print(f"Reason: {item.reason}")
        print(f"Caution: {item.caution}")

    with out.governance_assessments():
        out.line("safe-membership handoffs summarized", StatusMark.DEFER, "status summary is ready; adoption and insertion remain separate/not ready")

    return entries


def case_6_obligations(out: ScriptOutput) -> List[MembershipObligationEntry]:
    header("Case 6: Safe-membership final obligations")
    entries = [
        MembershipObligationEntry(
            name="O1: preserve compatible-if-declared status",
            obligation="record surviving typed and role-pure forms as compatible-if-declared only",
            status="OPEN",
            blocks="selection drift",
            discipline="do not shorten to selected, adopted, or derived",
        ),
        MembershipObligationEntry(
            name="O2: declare membership criterion before use",
            obligation="require zeta_Bs object, T_zeta sector, domain, codomain, and criterion before any theorem or adoption use",
            status="OPEN",
            blocks="typed membership claims",
            discipline="label is not proof",
        ),
        MembershipObligationEntry(
            name="O3: preserve role purity",
            obligation="keep residual/source/correction payloads outside membership unless separately derived",
            status="OPEN",
            blocks="hidden-load smuggling",
            discipline="membership is not cleanup",
        ),
        MembershipObligationEntry(
            name="O4: keep normalization separate from membership",
            obligation="carry Group 33 trace-normalization forms as separate compatibility nodes only",
            status="OPEN",
            blocks="Package B collapse",
            discipline="membership is not normalization",
        ),
        MembershipObligationEntry(
            name="O5: adoption remains separate",
            obligation="keep P_safe_membership unadopted unless a separate explicit decision is requested",
            status="OPEN",
            blocks="accidental adoption",
            discipline="candidate survival is not adoption",
        ),
        MembershipObligationEntry(
            name="O6: downstream gates remain closed",
            obligation="keep B_s/F_zeta insertion, active O, residual control, and parent equation closed",
            status="NOT_READY",
            blocks="downstream overreach",
            discipline="obligations summary is not insertion or parent closure",
        ),
    ]

    for item in entries:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        with out.unresolved_obligations():
            out.line(item.name, status_mark(item.status), item.status)
        print(f"Blocks: {item.blocks}")
        print(f"Discipline: {item.discipline}")

    with out.unresolved_obligations():
        out.line("safe-membership final obligations stated", StatusMark.OBLIGATION, "6 obligations stated before Group 34 status summary")

    return entries


def case_7_conclusions(out: ScriptOutput) -> None:
    header("Case 7: Safe-membership obligations conclusions")
    conclusions = [
        ("C1: surviving forms", "typed and role-pure membership forms survive if declared", "COMPATIBLE_IF_DECLARED", "both remain candidate forms; neither is selected"),
        ("C2: diagnostic scope", "diagnostic-only trace label survives only if strictly inert", "VALID_IF_INERT", "not adopted membership or insertion"),
        ("C3: invalid forms", "undeclared objects, hidden payloads, Package B collapse, and downstream use fail", "REQUIRED", "membership cannot smuggle hidden load or theorem closure"),
        ("C4: no derivation", "this obligations summary derives no safe-membership theorem", "NOT_DERIVED", "open decisions remain"),
        ("C5: no adoption", "this obligations summary adopts no safe-membership postulate", "NOT_ADOPTED", "explicit decision remains separate"),
        ("C6: next", "Group 34 status summary should run next", "OPEN", "summarize without selecting or adopting membership"),
    ]

    for name, conclusion, status, meaning in conclusions:
        subheader(name)
        print(f"Conclusion: {conclusion}")
        with out.governance_assessments():
            out.line(name, status_mark(status), status)
        print(f"Meaning: {meaning}")

    with out.governance_assessments():
        out.line(
            "safe-membership obligations conclusion stated",
            StatusMark.PASS,
            "surviving forms and obligations summarized; no selection or adoption",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Safe-membership obligations result:\n")
    print("  Typed trace-sector and role-pure membership forms survive as compatible-if-declared candidates.")
    print("  Normalization-compatible membership remains compatibility only and does not collapse Package B.")
    print("  Diagnostic-only trace labels remain safe only if strictly equation-inert.")
    print("  Undeclared objects, hidden source load, hidden divergence reservoirs, residual payloads, normalization collapse, and downstream use fail.")
    print("  The remaining open decisions are membership criterion, role-purity enforcement, normalization compatibility, diagnostic/active scope, and adoption boundary.")
    print("  No safe-membership theorem is selected, adopted, or derived by this obligations summary.")
    print("  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.\n")
    print("Possible next script:")
    print("  candidate_group_34_status_summary.py\n")
    print("Tiny goblin label:")
    print("  Count the shelves. Still no shelving.\n")

    with out.governance_assessments():
        out.line(
            "safe-membership obligations summary complete",
            StatusMark.PASS,
            "Group 34 status summary should run next; adoption and downstream gates remain closed",
        )


def record_inventory_marker(ns, symbols: MembershipObligationSymbols) -> None:
    ns.record_derivation(
        derivation_id="g34_safe_membership_obligations",
        inputs=[symbols.M_safe],
        output=symbols.L_obligation_gap,
        method="safe-membership obligations summary ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="obligations_summary_marker",
        is_placeholder=True,
    )


def record_governance(
    ns,
    surviving: List[SurvivingFormEntry],
    failures: List[FailureModeEntry],
    decisions: List[OpenDecisionEntry],
    handoffs: List[HandoffEntry],
) -> None:
    obligation_ids = [
        "g34_membership_obligation_o1",
        "g34_membership_obligation_o2",
        "g34_membership_obligation_o3",
        "g34_membership_obligation_o4",
        "g34_membership_obligation_o5",
        "g34_membership_obligation_o6",
    ]

    for item in surviving:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_route(
            RouteRecord(
                route_id=f"g34_obligations_surviving_{ident}",
                script_id=SCRIPT_ID,
                name=item.name,
                status=GovernanceStatus.CANDIDATE_ROUTE,
                tier=ClaimTier.CONSTRAINED,
                required_obligations=obligation_ids,
                activation_conditions=[
                    item.form,
                    f"Survives if: {item.survives_if}",
                    f"Remaining decision: {item.remaining_decision}",
                    f"Boundary: {item.boundary}",
                ],
            )
        )

    for item in failures:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g34_obligations_failure_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.REJECTED_ROUTE,
                statement=f"{item.failure}. Reason: {item.reason}. Consequence: {item.consequence}.",
                derivation_ids=["g34_safe_membership_obligations"],
                obligation_ids=obligation_ids,
            )
        )

    for item in decisions:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g34_open_decision_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
                statement=f"{item.decision}. Blocks: {item.blocks}. Discipline: {item.discipline}.",
                derivation_ids=["g34_safe_membership_obligations"],
                obligation_ids=obligation_ids,
            )
        )

    for item in handoffs:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g34_handoff_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=(
                    GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
                    if item.status == "NOT_READY"
                    else GovernanceStatus.CANDIDATE_ROUTE
                ),
                statement=f"{item.handoff}. Reason: {item.reason}. Caution: {item.caution}.",
                derivation_ids=["g34_safe_membership_obligations"],
                obligation_ids=obligation_ids,
            )
        )


def record_obligations(ns, obligations: List[MembershipObligationEntry]) -> None:
    for item in obligations:
        ident = item.name.split(":", 1)[0].lower().replace("-", "_")
        ns.record_obligation(
            ProofObligationRecord(
                obligation_id=f"g34_membership_obligation_{ident}",
                script_id=SCRIPT_ID,
                title=item.name,
                status=ObligationStatus.OPEN if item.status != "NOT_READY" else ObligationStatus.DEFERRED,
                required_by=[SCRIPT_ID],
                description=f"{item.obligation} Blocks: {item.blocks}. Discipline: {item.discipline}.",
            )
        )


def main() -> None:
    out = ScriptOutput()
    archive, ns, invalidated = prepare_archive()
    ensure_archive_write_dirs(ns)

    header("Candidate Safe Trace Membership Obligations")
    print_archive_status(ns, invalidated)

    case_0_problem(out)
    symbols = case_1_symbolic_ledger(out)
    surviving = case_2_surviving_forms(out)
    failures = case_3_failure_modes(out)
    decisions = case_4_open_decisions(out)
    handoffs = case_5_handoffs(out)
    obligations = case_6_obligations(out)
    case_7_conclusions(out)
    final_interpretation(out)

    record_inventory_marker(ns, symbols)
    record_obligations(ns, obligations)
    record_governance(ns, surviving, failures, decisions, handoffs)

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
