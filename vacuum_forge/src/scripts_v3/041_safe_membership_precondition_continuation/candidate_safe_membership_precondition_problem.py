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

SCRIPT_LABEL = "Candidate Safe-Membership Precondition Problem"
MARKER_ID = "g41_problem"
DEPENDENCIES = [
    ("g40_summary", "040_split_safe_trace_anchor_precondition_audit__candidate_group_40_status_summary", "g40_summary"),
    ("g39_summary", "039_trace_anchor_branch_choice_readiness_audit__candidate_group_39_status_summary", "g39_summary"),
    ("g38_summary", "038_trace_anchor_explicit_declaration_record__candidate_group_38_status_summary", "g38_summary"),
]


def build_entries() -> List[Entry]:
    return [
        Entry(
            "P1: current membership status",
            "zeta_Bs -> T_zeta is diagnostic / compatible-if-declared only",
            "COMPATIBLE_IF_DECLARED",
            "current use may label a possible compatibility surface only",
            "not declaration-ready, selected, adopted, derived, incidence, active O, insertion, or parent readiness",
        ),
        Entry(
            "P2: future declaration route",
            "future declaration or theorem route remains possible only after preconditions close",
            "CONDITIONAL",
            "object, sector, domain/codomain, criterion, role-purity, branch-status, diagnostic/active scope, and exclusion-zone obligations must be satisfied first",
            "future route is not current readiness",
        ),
        Entry(
            "P3: sharpened precondition slots",
            "Group 41 may sharpen membership object, T_zeta sector, criterion, role-purity, diagnostic scope, and exclusion zones",
            "SPLIT_SAFE",
            "preconditions may be made explicit under split notation if no active branch or expression is installed",
            "precondition visibility is not proof",
        ),
        Entry(
            "P4: branch status visibility",
            "branch-neutral and branch-indexed membership status must remain distinct",
            "BRANCH_INDEXED",
            "zeta_Bs may remain shorthand only where branch sensitivity is absent; branch-sensitive cases must be expanded",
            "no branch choice by prose",
        ),
        Entry(
            "P5: downstream gate boundary",
            "insertion, active O, residual control, Package B adoption, and parent closure remain closed",
            "NOT_READY",
            "Group 41 is safe-membership precondition continuation only",
            "membership preconditions cannot open field-equation routes",
        ),
    ]


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  Which preconditions must be sharpened before zeta_Bs -> T_zeta can be used")
    print("  in any later declaration, theorem, adoption, or insertion-precondition route?")
    print("\nDiscipline:\n")
    print("  This script opens Group 41 as a safe-membership precondition continuation.")
    print("  It keeps zeta_Bs -> T_zeta diagnostic / compatible-if-declared only.")
    print("  It does not choose a B_s branch, install membership, adopt Package B, prove incidence,")
    print("  open active O, insert B_s/F_zeta, or open parent closure.")
    with out.governance_assessments():
        out.line(
            f"{SCRIPT_LABEL} opened",
            StatusMark.PASS,
            "precondition audit only; no branch choice, declaration completion, adoption, theorem, insertion, or parent route",
        )


def case_1(out: ScriptOutput, entries: List[Entry]) -> None:
    header("Case 1: Safe-membership precondition opening entries")
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
        ("X1: compatibility as declaration", "treat compatible-if-declared as declaration-ready", "current status is diagnostic only"),
        ("X2: future candidate as selected", "treat a possible future declaration route as selected", "future route requires closed obligations"),
        ("X3: membership as incidence", "use membership to prove trace/residual zero incidence", "incidence remains separate theorem work"),
        ("X4: membership as active O", "let T_zeta behave like an active projector", "T_zeta is not O"),
        ("X5: precondition as insertion", "open B_s/F_zeta insertion from sharpened preconditions", "downstream gates remain closed"),
    ]
    for name, shortcut, reason in shortcuts:
        subheader(name)
        print(f"Shortcut: {shortcut}")
        with out.counterexamples():
            out.line(name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {reason}")


def case_3(out: ScriptOutput) -> None:
    header("Case 3: Open obligations")
    obligations = [
        ("O1: preserve current/future status separation", "current diagnostic compatibility must stay distinct from future declaration/theorem candidates", "COMPATIBLE_IF_DECLARED"),
        ("O2: sharpen membership slots", "object, sector, domain/codomain, criterion, role-purity, diagnostic scope, and exclusion zones must be inventoried", "OPEN"),
        ("O3: preserve branch visibility", "branch-sensitive membership claims must be branch-indexed rather than hidden under neutral zeta_Bs", "OPEN"),
        ("O4: preserve downstream locks", "insertion, active O, residual control, adoption, and parent closure must remain closed", "NOT_READY"),
    ]
    for oid, description, status in obligations:
        subheader(oid)
        with out.unresolved_obligations():
            out.line(oid, mark(status), f"{status}: {description}")


def case_4(out: ScriptOutput) -> None:
    header("Case 4: Local conclusions")
    conclusions = [
        ("Group 41 opener complete", "PASS", "safe-membership precondition continuation opened"),
        ("active membership not installed", "DEFER", "zeta_Bs -> T_zeta remains compatible-if-declared only"),
    ]
    with out.governance_assessments():
        for name, status, detail in conclusions:
            out.line(name, mark(status), detail)
    print("\nPossible next script:")
    print("  candidate_zeta_Bs_object_precondition_ledger.py")


def record_governance(ns, entries: List[Entry]) -> None:
    record_marker(ns, MARKER_ID, MARKER_ID, "Group 41 safe-membership precondition continuation")
    for idx, item in enumerate(entries, 1):
        record_claim(ns, f"{MARKER_ID}_c{idx}", MARKER_ID, f"{item.name}: {item.subject}. {item.detail}. Boundary: {item.boundary}.")
    for idx, item in enumerate(entries, 1):
        if item.status in {"COMPATIBLE_IF_DECLARED", "CONDITIONAL", "BRANCH_INDEXED", "NOT_READY"}:
            record_obligation(
                ns,
                f"{MARKER_ID}_o{idx}",
                item.name,
                f"Carry forward {item.subject} without treating it as branch choice, adoption, theorem proof, incidence, active O, insertion, or parent readiness.",
                item.status,
            )


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
