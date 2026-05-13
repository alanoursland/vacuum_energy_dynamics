# Group:
#   35_trace_anchor_joint_declaration_inventory
#
# Script type:
#   OBLIGATION SUMMARY / DECLARATION-HANDOFF LEDGER
#
# candidate_trace_anchor_declaration_obligations.py
#
# Purpose
# -------
# Summarize the declaration and status obligations left by the Group 35
# component declaration ledger, joint consistency matrix, and status-mode sieve.
#
# This script does not:
#
#   * fill declaration slots,
#   * select a trace-normalization form,
#   * select a safe-membership form,
#   * adopt either Package B component,
#   * recommend Package B adoption,
#   * derive a coefficient law,
#   * derive B_s/F_zeta insertion,
#   * construct active O,
#   * derive residual control,
#   * open the parent field equation.
#
# It only records what must remain explicit before future theorem, adoption,
# or conditional-precondition work.

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    RecordKind,
    StatusMark,
)


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"


# ----------------------------------------------------------------------------------------------------------------------
# Output helpers
# ----------------------------------------------------------------------------------------------------------------------


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


def mark(status: str) -> StatusMark:
    mapping = {
        "PASS": StatusMark.PASS,
        "FAIL": StatusMark.FAIL,
        "INFO": StatusMark.INFO,
        "OPEN": StatusMark.DEFER,
        "DEFER": StatusMark.DEFER,
        "OBLIGATION": StatusMark.OBLIGATION,
        "REQUIRED": StatusMark.OBLIGATION,
        "NOT_READY": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_CHOSEN": StatusMark.DEFER,
        "CONDITIONAL": StatusMark.DEFER,
        "COMPATIBLE_IF_DECLARED": StatusMark.INFO,
        "MIXED_STATUS_VISIBLE": StatusMark.DEFER,
        "DECLARATION_OBLIGATION": StatusMark.OBLIGATION,
        "HANDOFF_READY": StatusMark.INFO,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
    }
    return mapping.get(status, StatusMark.INFO)


def out_line(channel: str, status: str, label: str, detail: str = "") -> None:
    tag = mark(status).name
    if detail:
        print(f"[{channel}]\n[{tag}] {label} -- {status}\n{detail}")
    else:
        print(f"[{channel}]\n[{tag}] {label} -- {status}")


# ----------------------------------------------------------------------------------------------------------------------
# Archive helpers
# ----------------------------------------------------------------------------------------------------------------------


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)

    dependencies = [
        (
            "g35_status_mode_sieve",
            "35_trace_anchor_joint_declaration_inventory__candidate_trace_anchor_status_mode_sieve",
            "g35_status_mode_sieve",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g35_joint_consistency_matrix",
            "35_trace_anchor_joint_declaration_inventory__candidate_trace_anchor_joint_consistency_matrix",
            "g35_joint_consistency_matrix",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g35_component_ledger",
            "35_trace_anchor_joint_declaration_inventory__candidate_trace_anchor_component_declaration_ledger",
            "g35_component_declaration_ledger",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g35_problem",
            "35_trace_anchor_joint_declaration_inventory__candidate_trace_anchor_joint_declaration_problem",
            "g35_joint_declaration_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g34_summary",
            "34_safe_trace_membership_candidate_origin__candidate_group_34_status_summary",
            "g34_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g33_summary",
            "33_trace_normalization_candidate_origin__candidate_group_33_status_summary",
            "g33_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g32_summary",
            "32_explicit_minimal_postulate_selection__candidate_group_32_status_summary",
            "g32_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
    ]

    for dependency_id, upstream_script_id, upstream_derivation_id, record_kind in dependencies:
        ns.declare_dependency(
            dependency_id=dependency_id,
            upstream_script_id=upstream_script_id,
            upstream_derivation_id=upstream_derivation_id,
            expected_record_kind=record_kind,
        )

    invalidated = ns.check_source_invalidation(__file__)
    return archive, ns, invalidated


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


def safe_ident(name: str) -> str:
    raw = name.split(":", 1)[0].strip().lower()
    keep = []
    for ch in raw:
        if ch.isalnum():
            keep.append(ch)
        elif ch in {" ", "-", "_", "/"}:
            keep.append("_")
    ident = "".join(keep).strip("_")
    while "__" in ident:
        ident = ident.replace("__", "_")
    return ident or "entry"


# ----------------------------------------------------------------------------------------------------------------------
# Data
# ----------------------------------------------------------------------------------------------------------------------


@dataclass(frozen=True)
class ObligationEntry:
    name: str
    obligation: str
    status: str
    blocks: str
    discipline: str


@dataclass(frozen=True)
class HandoffEntry:
    name: str
    handoff: str
    status: str
    reason: str
    caution: str


@dataclass(frozen=True)
class FailureControl:
    name: str
    shortcut: str
    status: str
    reason: str
    failure_mode: str


@dataclass(frozen=True)
class ConclusionEntry:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_obligations() -> list[ObligationEntry]:
    return [
        ObligationEntry(
            "O1: trace-normalization declarations",
            "Keep B_s convention, zeta convention, traced dimension, exact/linearized scope, and trace-normalization status mode explicit before use",
            "OPEN",
            "trace-normalization theorem, adoption, or handoff",
            "compatible-if-declared remains conditional until declarations are explicit",
        ),
        ObligationEntry(
            "O2: safe-membership declarations",
            "Keep zeta_Bs object, T_zeta sector, domain, codomain, membership criterion, role-purity, and diagnostic/active scope explicit before use",
            "OPEN",
            "safe-membership theorem, adoption, or handoff",
            "label visibility is prerequisite, not proof",
        ),
        ObligationEntry(
            "O3: component status modes",
            "Require status mode for each Package B component before any future theorem, adoption, or precondition route",
            "OPEN",
            "ambiguous downstream status",
            "current status remains compatible-if-declared unless later changed explicitly",
        ),
        ObligationEntry(
            "O4: mixed-status visibility",
            "If trace normalization and safe membership have different statuses, carry the mixed status explicitly",
            "OPEN",
            "Package B overclaim",
            "one component status cannot license the other",
        ),
        ObligationEntry(
            "O5: node separation",
            "Keep P_trace_norm and P_safe_membership separate in all future use",
            "OPEN",
            "Package B collapse",
            "joint declarations are not node merger",
        ),
        ObligationEntry(
            "O6: postulate/theorem boundary",
            "Do not call adopted postulates derived and do not call theorem targets proved",
            "OPEN",
            "governance drift",
            "choice and proof remain separate",
        ),
        ObligationEntry(
            "O7: adoption boundary",
            "Do not adopt Package B or either component in this obligation summary",
            "REQUIRED",
            "accidental adoption",
            "adoption requires a separate explicit user/theory decision record",
        ),
        ObligationEntry(
            "O8: downstream gates",
            "Keep B_s/F_zeta insertion, active O, residual control, and parent closure closed",
            "NOT_READY",
            "downstream overreach",
            "declaration obligations are not insertion or parent readiness",
        ),
    ]


def build_handoffs() -> list[HandoffEntry]:
    return [
        HandoffEntry(
            "H1: Group 35 status summary",
            "candidate_group_35_status_summary.py",
            "HANDOFF_READY",
            "the declaration surface, consistency matrix, and status-mode sieve have enough information to summarize Group 35",
            "summary must not fill declarations, assign status, adopt Package B, or open insertion",
        ),
        HandoffEntry(
            "H2: explicit declaration record",
            "record concrete B_s, zeta, dimension, scope, membership criterion, role-purity, and status-mode declarations",
            "OPEN",
            "future work may need actual declaration values before theorem or adoption routes",
            "declaration record is not adoption and not theorem proof",
        ),
        HandoffEntry(
            "H3: explicit Package B adoption decision",
            "separate explicit user/theory decision record",
            "OPEN",
            "adoption remains possible only as deliberate theory choice",
            "adopted postulates must not be called derived",
        ),
        HandoffEntry(
            "H4: theorem route after declarations",
            "trace-normalization and/or safe-membership theorem attempt after declaration slots are filled",
            "OPEN",
            "surviving forms may be theorem targets once declarations are explicit",
            "theorem target is not theorem proof",
        ),
        HandoffEntry(
            "H5: conditional trace-anchor precondition inventory",
            "precondition inventory only under explicit declaration/status assumptions",
            "CONDITIONAL",
            "may help organize later insertion prerequisites",
            "precondition inventory is not B_s/F_zeta insertion theorem",
        ),
        HandoffEntry(
            "H6: B_s/F_zeta insertion theorem",
            "downstream insertion route",
            "NOT_READY",
            "component status and recombination safety gates remain unresolved",
            "forbidden as immediate route from Group 35 alone",
        ),
        HandoffEntry(
            "H7: parent field equation",
            "parent route",
            "NOT_READY",
            "scalar recombination, residual control, no-overlap, and divergence safety remain unresolved",
            "parent gate remains closed",
        ),
    ]


def build_failure_controls() -> list[FailureControl]:
    return [
        FailureControl(
            "X1: hidden declaration handoff",
            "future handoff uses Package B components while declarations remain blank",
            "FORBIDDEN_SHORTCUT",
            "compatible-if-declared status is conditional",
            "hidden declarations enter downstream work",
        ),
        FailureControl(
            "X2: hidden status handoff",
            "future handoff omits component status mode",
            "FORBIDDEN_SHORTCUT",
            "status mode is mandatory before use",
            "audit status becomes ambiguous theory status",
        ),
        FailureControl(
            "X3: compatible-if-declared as chosen",
            "compatible-if-declared is shortened to selected, adopted, or derived",
            "FORBIDDEN_SHORTCUT",
            "filter survival is weaker than choice, adoption, or proof",
            "Group 35 accidentally chooses Package B",
        ),
        FailureControl(
            "X4: node collapse",
            "trace normalization and safe membership are treated as one joint choice",
            "FORBIDDEN_SHORTCUT",
            "Package B has two separate candidate nodes",
            "one hidden choice licenses the other",
        ),
        FailureControl(
            "X5: status as insertion",
            "status bookkeeping is treated as B_s/F_zeta insertion, active O, residual control, or parent readiness",
            "FORBIDDEN_SHORTCUT",
            "downstream gates remain closed",
            "declaration clarity opens field-equation gates prematurely",
        ),
    ]


def build_conclusions() -> list[ConclusionEntry]:
    return [
        ConclusionEntry(
            "C1: declaration obligations summarized",
            "the remaining declaration and status obligations are visible",
            "DECLARATION_OBLIGATION",
            "Group 35 can close as an inventory without filling slots",
        ),
        ConclusionEntry(
            "C2: current status preserved",
            "trace-normalization and safe-membership surviving forms remain compatible-if-declared only",
            "COMPATIBLE_IF_DECLARED",
            "current audit status is not selected, adopted, derived, or insertable",
        ),
        ConclusionEntry(
            "C3: handoffs separated",
            "declaration, theorem, adoption, precondition, insertion, and parent routes are separated",
            "REQUIRED",
            "future work must state which route it is using",
        ),
        ConclusionEntry(
            "C4: no choices made",
            "this obligation summary chooses no declaration value and assigns no component status",
            "NOT_CHOSEN",
            "obligation summary is not declaration record",
        ),
        ConclusionEntry(
            "C5: no adoption",
            "this obligation summary adopts no Package B component and recommends no adoption",
            "NOT_ADOPTED",
            "explicit decision remains separate",
        ),
        ConclusionEntry(
            "C6: next",
            "Group 35 status summary should run next",
            "OPEN",
            "summarize the joint declaration inventory without selecting components",
        ),
    ]


# ----------------------------------------------------------------------------------------------------------------------
# Cases
# ----------------------------------------------------------------------------------------------------------------------


def case_0_problem() -> None:
    header("Case 0: Trace-anchor declaration obligations problem")

    print(
        "Question:\n\n"
        "  What declaration and status obligations remain after the joint consistency\n"
        "  matrix and status-mode sieve, and what can safely be handed off without\n"
        "  filling declarations, assigning status, adopting Package B, or opening\n"
        "  downstream gates?\n"
    )

    print(
        "Discipline:\n\n"
        "  This script summarizes declaration obligations.\n"
        "  It fills no declaration slot.\n"
        "  It assigns no Package B component status as theory state.\n"
        "  It selects no trace-normalization form.\n"
        "  It selects no safe-membership form.\n"
        "  It adopts no Package B component.\n"
        "  It recommends no Package B adoption.\n"
        "  It derives no coefficient law and no insertion.\n"
        "  It keeps active O, residual control, and parent closure closed.\n"
    )

    print("Tiny goblin rule:\n  Count the blank tags. Still do not hang them.\n")
    out_line(
        "governance_assessments",
        "INFO",
        "trace-anchor declaration obligations summary opened",
        "summarizing obligations after joint consistency and status-mode sieves",
    )


def case_1_symbolic_ledger():
    header("Case 1: Declaration-obligations symbolic ledger")

    names = [
        "B_s_decl",
        "zeta_decl",
        "d_decl",
        "exact_scope",
        "N_trace_status",
        "zeta_Bs_decl",
        "T_zeta_decl",
        "domain_decl",
        "codomain_decl",
        "membership_criterion",
        "role_purity",
        "diagnostic_scope",
        "norm_membership_separation",
        "component_status_mode",
        "mixed_status",
        "postulate_theorem_boundary",
        "adoption_boundary",
        "P_insertion",
        "P_active_O",
        "P_residual_kill",
        "P_parent",
    ]

    syms = {name: sp.symbols(name) for name in names}

    L_trace_norm_declarations = sp.simplify(
        syms["B_s_decl"]
        + syms["zeta_decl"]
        + syms["d_decl"]
        + syms["exact_scope"]
        + syms["N_trace_status"]
    )
    L_membership_declarations = sp.simplify(
        syms["zeta_Bs_decl"]
        + syms["T_zeta_decl"]
        + syms["domain_decl"]
        + syms["codomain_decl"]
        + syms["membership_criterion"]
        + syms["role_purity"]
        + syms["diagnostic_scope"]
    )
    L_status_obligations = sp.simplify(
        syms["component_status_mode"]
        + syms["mixed_status"]
        + syms["postulate_theorem_boundary"]
        + syms["adoption_boundary"]
        + syms["norm_membership_separation"]
    )
    L_downstream_closed = sp.simplify(
        syms["P_active_O"] + syms["P_insertion"] + syms["P_parent"] + syms["P_residual_kill"]
    )
    L_obligation_surface = sp.simplify(
        L_trace_norm_declarations + L_membership_declarations + L_status_obligations + L_downstream_closed
    )

    print("Obligation symbols:")
    for name in names:
        print(f"  {name} = {syms[name]}")

    print()
    print(f"Trace-normalization declaration obligation load:\n  L_trace_norm_declarations = {L_trace_norm_declarations}")
    print(f"\nSafe-membership declaration obligation load:\n  L_membership_declarations = {L_membership_declarations}")
    print(f"\nStatus obligation load:\n  L_status_obligations = {L_status_obligations}")
    print(f"\nDownstream closed load:\n  L_downstream_closed = {L_downstream_closed}")
    print(f"\nDeclaration-obligation surface:\n  L_obligation_surface = {L_obligation_surface}")

    out_line(
        "derived_results",
        "OBLIGATION",
        "declaration-obligation symbolic loads stated",
        f"L_status_obligations={L_status_obligations}; L_downstream_closed={L_downstream_closed}",
    )

    return {
        "symbols": syms,
        "L_trace_norm_declarations": L_trace_norm_declarations,
        "L_membership_declarations": L_membership_declarations,
        "L_status_obligations": L_status_obligations,
        "L_downstream_closed": L_downstream_closed,
        "L_obligation_surface": L_obligation_surface,
    }


def case_2_obligations(obligations: Iterable[ObligationEntry]) -> None:
    header("Case 2: Declaration and status obligations")

    for item in obligations:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        out_line("unresolved_obligations", item.status, item.name, f"Blocks: {item.blocks}\nDiscipline: {item.discipline}")

    out_line(
        "unresolved_obligations",
        "OBLIGATION",
        "declaration/status obligations summarized",
        "trace-normalization, safe-membership, status, mixed-status, node-separation, adoption, and downstream obligations stated",
    )


def case_3_safe_handoffs(handoffs: Iterable[HandoffEntry]) -> None:
    header("Case 3: Safe handoffs")

    for item in handoffs:
        subheader(item.name)
        print(f"Handoff: {item.handoff}")
        out_line("governance_assessments", item.status, item.name, f"Reason: {item.reason}\nCaution: {item.caution}")

    out_line(
        "governance_assessments",
        "DEFER",
        "safe handoffs summarized",
        "status summary is ready; declaration, theorem, adoption, precondition, insertion, and parent routes remain separated",
    )


def case_4_failure_controls(controls: Iterable[FailureControl]) -> None:
    header("Case 4: Failure controls")

    for item in controls:
        subheader(item.name)
        print(f"Shortcut: {item.shortcut}")
        out_line("counterexamples", item.status, item.name, f"Reason: {item.reason}\nFailure mode: {item.failure_mode}")

    out_line(
        "counterexamples",
        "FAIL",
        "declaration-obligation failure controls stated",
        "hidden declarations/status, compatible-if-declared-as-chosen, node collapse, and downstream upgrades are rejected",
    )


def case_5_no_overclaim_rules() -> None:
    header("Case 5: Declaration-obligation no-overclaim rules")

    rules = [
        (
            "R1: obligation summary is not declaration",
            "summarizing blank slots does not fill them",
            "declaration values require a separate record or theory decision",
        ),
        (
            "R2: obligation summary is not status assignment",
            "classifying required modes does not assign a component status as theory state",
            "status mode must be explicitly recorded later before use",
        ),
        (
            "R3: obligation summary is not adoption",
            "no Package B component is adopted here",
            "adoption requires a separate explicit decision record",
        ),
        (
            "R4: obligation summary is not theorem proof",
            "open theorem routes remain open",
            "proof requires separate derivation scripts",
        ),
        (
            "R5: obligation summary is not insertion",
            "no handoff may treat declaration clarity as B_s/F_zeta insertion or parent readiness",
            "downstream gates remain closed",
        ),
    ]

    for name, rule, reason in rules:
        subheader(name)
        print(f"Rule: {rule}")
        out_line("governance_assessments", "OBLIGATION", name, f"Reason: {reason}")

    out_line(
        "governance_assessments",
        "OBLIGATION",
        "declaration-obligation no-overclaim rules stated",
        "5 no-overclaim rules stated",
    )


def case_6_conclusions(conclusions: Iterable[ConclusionEntry]) -> None:
    header("Case 6: Declaration-obligation conclusions")

    for item in conclusions:
        subheader(item.name)
        print(f"Conclusion: {item.conclusion}")
        out_line("governance_assessments", item.status, item.name, f"Meaning: {item.meaning}")

    out_line(
        "governance_assessments",
        "PASS",
        "trace-anchor declaration obligations conclusion stated",
        "obligations summarized; no declarations filled, no status assigned, no adoption, downstream gates closed",
    )


def final_interpretation() -> None:
    header("Final interpretation")
    print(
        "Trace-anchor declaration obligations result:\n\n"
        "  The remaining declaration and status obligations are now summarized.\n"
        "  Trace-normalization declarations remain open: B_s convention, zeta convention,\n"
        "  traced dimension, exact/linearized scope, and status mode.\n"
        "  Safe-membership declarations remain open: zeta_Bs object, T_zeta sector,\n"
        "  domain/codomain, membership criterion, role purity, and diagnostic/active scope.\n"
        "  Package B node separation and component status-mode discipline remain required.\n"
        "  Group 33/34 surviving forms remain compatible-if-declared only.\n"
        "  No declaration value is filled by this script.\n"
        "  No Package B component status is assigned as theory state.\n"
        "  No trace-normalization or safe-membership form is selected, adopted, or derived.\n"
        "  Package B is not recommended for adoption.\n"
        "  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.\n\n"
        "Possible next script:\n"
        "  candidate_group_35_status_summary.py\n\n"
        "Tiny goblin label:\n"
        "  Count the blank tags. Still do not hang them.\n"
    )
    out_line(
        "governance_assessments",
        "PASS",
        "trace-anchor declaration obligations summary complete",
        "Group 35 status summary should run next; adoption and downstream gates remain closed",
    )


# ----------------------------------------------------------------------------------------------------------------------
# Archive records
# ----------------------------------------------------------------------------------------------------------------------


def record_inventory_marker(ns, symbolic) -> None:
    ns.record_derivation(
        derivation_id="g35_declaration_obligations",
        inputs=[
            symbolic["L_trace_norm_declarations"],
            symbolic["L_membership_declarations"],
            symbolic["L_status_obligations"],
            symbolic["L_downstream_closed"],
        ],
        output=symbolic["L_obligation_surface"],
        method=(
            "obligation summary for declaration slots, component status modes, mixed-status visibility, "
            "node separation, adoption boundary, and downstream gate closure"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="declaration_obligation_summary_marker",
    )


def record_obligations(ns, obligations: Iterable[ObligationEntry]) -> None:
    for item in obligations:
        ident = safe_ident(item.name)
        status = ObligationStatus.OPEN if item.status != "NOT_READY" else ObligationStatus.DEFERRED
        ns.record_obligation(
            ProofObligationRecord(
                obligation_id=f"g35_declaration_obligation_{ident}",
                script_id=SCRIPT_ID,
                title=item.name,
                status=status,
                required_by=[SCRIPT_ID],
                description=f"{item.obligation}. Blocks: {item.blocks}. Discipline: {item.discipline}.",
            )
        )


def record_governance(ns, failures: Iterable[FailureControl]) -> None:
    for item in failures:
        ident = safe_ident(item.name)
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g35_failure_control_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.REJECTED_ROUTE,
                statement=f"{item.shortcut}. Rejected because: {item.reason}. Failure mode: {item.failure_mode}.",
                derivation_ids=["g35_declaration_obligations"],
                obligation_ids=[],
            )
        )

    policy_rules = [
        (
            "g35_policy_no_declaration_by_summary",
            "Declaration-obligation summary does not fill declaration slots.",
        ),
        (
            "g35_policy_no_status_assignment_by_summary",
            "Declaration-obligation summary does not assign Package B component status as theory state.",
        ),
        (
            "g35_policy_no_adoption_by_summary",
            "Declaration-obligation summary adopts no Package B component.",
        ),
        (
            "g35_policy_downstream_gates_closed",
            "Declaration obligations do not license B_s/F_zeta insertion, active O, residual control, or parent closure.",
        ),
    ]
    for claim_id, statement in policy_rules:
        ns.record_claim(
            ClaimRecord(
                claim_id=claim_id,
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.POLICY_RULE,
                statement=statement,
                derivation_ids=["g35_declaration_obligations"],
                obligation_ids=[],
            )
        )


# ----------------------------------------------------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------------------------------------------------


def main() -> None:
    header("Candidate Trace Anchor Declaration Obligations")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    obligations = build_obligations()
    handoffs = build_handoffs()
    failures = build_failure_controls()
    conclusions = build_conclusions()

    case_0_problem()
    symbolic = case_1_symbolic_ledger()
    case_2_obligations(obligations)
    case_3_safe_handoffs(handoffs)
    case_4_failure_controls(failures)
    case_5_no_overclaim_rules()
    case_6_conclusions(conclusions)
    final_interpretation()

    record_inventory_marker(ns, symbolic)
    record_obligations(ns, obligations)
    record_governance(ns, failures)

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
