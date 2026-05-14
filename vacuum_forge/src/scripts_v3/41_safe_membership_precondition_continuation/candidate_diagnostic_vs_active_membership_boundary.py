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


def prepare_archive(dependencies):
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    for dep_id, upstream_script_id, upstream_derivation_id in dependencies:
        ns.declare_dependency(
            dependency_id=dep_id,
            upstream_script_id=upstream_script_id,
            upstream_derivation_id=upstream_derivation_id,
            expected_record_kind=RecordKind.INVENTORY_MARKER,
        )
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


def mark(status: str) -> StatusMark:
    return {
        "PASS": StatusMark.PASS,
        "INFO": StatusMark.INFO,
        "SPLIT_SAFE": StatusMark.INFO,
        "BRANCH_INDEXED": StatusMark.INFO,
        "DIAGNOSTIC_ONLY": StatusMark.INFO,
        "COMPATIBLE_IF_DECLARED": StatusMark.INFO,
        "CONDITIONAL": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "DEFER": StatusMark.DEFER,
        "BLOCKED": StatusMark.DEFER,
        "BRANCH_REQUIRED": StatusMark.OBLIGATION,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "NOT_READY": StatusMark.DEFER,
        "NOT_DECLARED": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "REJECTED": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "MATCHED_EXPECTATION": StatusMark.PASS,
    }.get(status, StatusMark.INFO)


def obligation_status(status: str) -> ObligationStatus:
    if status in {"NOT_READY", "NOT_DECLARED", "NOT_ADOPTED", "NOT_DERIVED", "BRANCH_REQUIRED", "CONDITIONAL"}:
        return ObligationStatus.DEFERRED
    return ObligationStatus.OPEN


def record_marker(ns, marker_id: str, symbol_name: str, scope: str) -> None:
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[],
        output=sp.Symbol(symbol_name),
        method="inventory marker; no physical derivation",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
        scope=scope,
    )


def record_claim(ns, claim_id: str, marker_id: str, statement: str, status=GovernanceStatus.POLICY_RULE) -> None:
    ns.record_claim(
        ClaimRecord(
            claim_id=claim_id,
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=status,
            statement=statement,
            derivation_ids=[marker_id],
            obligation_ids=[],
        )
    )


def record_obligation(ns, obligation_id: str, title: str, description: str, status: str = "OPEN") -> None:
    ns.record_obligation(
        ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=obligation_status(status),
            required_by=[SCRIPT_ID],
            description=description,
        )
    )


@dataclass(frozen=True)
class Entry:
    name: str
    subject: str
    status: str
    detail: str
    boundary: str


# Group:
#   41_safe_membership_precondition_continuation
# Script type:
#   AUDIT / PRECONDITION

SCRIPT_LABEL = "Candidate Diagnostic vs Active Membership Boundary"
MARKER_ID = "g41_active_boundary"
DEPENDENCIES = [
    ("g40_summary", "40_split_safe_trace_anchor_precondition_audit__candidate_group_40_status_summary", "g40_summary"),
    ("g41_role_purity", "41_safe_membership_precondition_continuation__candidate_role_purity_exclusion_zone_audit", "g41_role_purity"),
]


def build_entries() -> List[Entry]:
    return [
        Entry(
            "L1: diagnostic_label",
            "diagnostic membership labels object/sector compatibility only",
            "DIAGNOSTIC_ONLY",
            "no source, metric, divergence, projection, insertion, theorem, adoption, or parent effect",
            "safest current membership status",
        ),
        Entry(
            "L2: compatible_if_declared",
            "zeta_Bs -> T_zeta may remain compatible-if-declared only",
            "COMPATIBLE_IF_DECLARED",
            "compatibility is conditional on later declaration support",
            "not declaration-ready or theorem-ready",
        ),
        Entry(
            "L3: candidate_if_preconditions_met",
            "membership may become a future candidate only if preconditions close",
            "CONDITIONAL",
            "object, sector, domain/codomain, criterion, role-purity, branch-status, scope, and exclusions are required",
            "candidate status is not active membership",
        ),
        Entry(
            "L4: future_declaration_candidate",
            "a later declaration route may evaluate safe membership after obligations are satisfied",
            "NOT_DECLARED",
            "future declaration candidate remains a route label only",
            "not a current declaration",
        ),
        Entry(
            "L5: future_theorem_target",
            "a later theorem route may try to prove membership after declarations and assumptions are explicit",
            "NOT_DERIVED",
            "future theorem target requires actual derivation or proof",
            "not proved in Group 41",
        ),
        Entry(
            "L6: active_membership_forbidden_here",
            "active membership is forbidden in Group 41",
            "NOT_READY",
            "no active Package B membership, active T_zeta sector, active O, insertion, or parent route is opened",
            "current group sharpens preconditions only",
        ),
    ]


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  Where is the boundary between diagnostic compatibility and active safe membership?")
    print("\nDiscipline:\n")
    print("  This script states the diagnostic-versus-active status ladder.")
    print("  It uses future declaration candidate and future theorem target only as fenced future route labels.")
    print("  Active membership is forbidden in Group 41.")
    with out.governance_assessments():
        out.line(f"{SCRIPT_LABEL} opened", StatusMark.PASS, "diagnostic/active boundary audit only; no active membership installed")


def case_1(out: ScriptOutput, entries: List[Entry]) -> None:
    header("Case 1: Membership status ladder")
    for item in entries:
        subheader(item.name)
        print(f"Subject: {item.subject}")
        print(f"Detail: {item.detail}")
        print(f"Boundary: {item.boundary}")
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.detail}. Boundary: {item.boundary}")


def case_2(out: ScriptOutput) -> None:
    header("Case 2: Invalid upgrades and forbidden shortcuts")
    shortcuts = [
        ("X1: diagnostic as active projector", "turn diagnostic membership label into active O", "diagnostic labels are inert"),
        ("X2: compatibility as declaration", "treat compatible-if-declared as declared", "declaration route remains future"),
        ("X3: candidate as adopted Package B", "treat future candidate as Package B adoption", "adoption requires separate explicit decision"),
        ("X4: future theorem as proof", "treat future theorem target as proved membership", "proof is not supplied"),
        ("X5: active membership as insertion", "use active membership to insert B_s/F_zeta", "active membership and insertion are forbidden here"),
        ("X6: membership as residual control", "treat membership as residual zero-incidence or residual control", "residual control remains separate"),
    ]
    for name, shortcut, reason in shortcuts:
        subheader(name)
        print(f"Shortcut: {shortcut}")
        with out.counterexamples():
            out.line(name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {reason}")


def case_3(out: ScriptOutput) -> None:
    header("Case 3: Open obligations")
    obligations = [
        ("O1: keep diagnostic membership inert", "diagnostic labels must remain without source, metric, divergence, projection, insertion, theorem, adoption, or parent effect", "DIAGNOSTIC_ONLY"),
        ("O2: keep compatible-if-declared fenced", "compatibility cannot become declaration-ready without later record", "COMPATIBLE_IF_DECLARED"),
        ("O3: keep future routes future", "future declaration and theorem routes need separate later group support", "NOT_DECLARED"),
        ("O4: block active membership", "active membership remains forbidden in Group 41", "NOT_READY"),
    ]
    for oid, description, status in obligations:
        subheader(oid)
        with out.unresolved_obligations():
            out.line(oid, mark(status), f"{status}: {description}")


def case_4(out: ScriptOutput) -> None:
    header("Case 4: Local conclusions")
    with out.governance_assessments():
        out.line("diagnostic/active boundary complete", StatusMark.PASS, "status ladder stated conservatively")
        out.line("active membership remains forbidden", StatusMark.DEFER, "Group 41 remains precondition-only")
    print("\nPossible next script:")
    print("  candidate_safe_membership_precondition_batch_reconciliation.py")


def record_governance(ns, entries: List[Entry]) -> None:
    record_marker(ns, MARKER_ID, MARKER_ID, "Group 41 safe-membership precondition continuation")
    for idx, item in enumerate(entries, 1):
        record_claim(ns, f"{MARKER_ID}_c{idx}", MARKER_ID, f"{item.name}: {item.subject}. {item.detail}. Boundary: {item.boundary}.")
    for idx, item in enumerate(entries, 1):
        record_obligation(ns, f"{MARKER_ID}_o{idx}", item.name, f"Preserve membership status boundary: {item.subject}. {item.boundary}.", item.status)


def main() -> None:
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    entries = build_entries()
    case_0(out)
    case_1(out, entries)
    case_2(out)
    case_3(out)
    case_4(out)
    record_governance(ns, entries)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
