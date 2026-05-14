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

SCRIPT_LABEL = "Candidate zeta_Bs Object Precondition Ledger"
MARKER_ID = "g41_zeta_object"
DEPENDENCIES = [
    ("g40_summary", "40_split_safe_trace_anchor_precondition_audit__candidate_group_40_status_summary", "g40_summary"),
    ("g40_membership_precond", "40_split_safe_trace_anchor_precondition_audit__candidate_safe_membership_split_safe_preconditions", "g40_membership_precond"),
    ("g41_problem", "41_safe_membership_precondition_continuation__candidate_safe_membership_precondition_problem", "g41_problem"),
]


def build_entries() -> List[Entry]:
    return [
        Entry(
            "O1: neutral shorthand object",
            "zeta_Bs may name the payload object being tested for membership only where branch sensitivity is absent",
            "CONDITIONAL",
            "the shorthand is allowed as precondition bookkeeping, not as a branch relation or declaration",
            "expand into branch-aware variants when branch sensitivity matters",
        ),
        Entry(
            "O2: metric branch object",
            "zeta_Bs_metric is the branch-indexed membership-object candidate associated with B_s_metric",
            "BRANCH_INDEXED",
            "may be carried as a parallel object candidate while non-active",
            "not active metric branch choice and not trace-normalization declaration",
        ),
        Entry(
            "O3: scale branch object",
            "zeta_Bs_scale is the branch-indexed membership-object candidate associated with b_s_scale",
            "BRANCH_INDEXED",
            "may be carried as a parallel object candidate while non-active",
            "not active scale branch choice and not trace-normalization declaration",
        ),
        Entry(
            "O4: diagnostic object label",
            "diagnostic_zeta_Bs_label may label object/sector compatibility only",
            "DIAGNOSTIC_ONLY",
            "diagnostic label has no source, metric, divergence, projection, insertion, or theorem effect",
            "diagnostic label is not active membership",
        ),
        Entry(
            "O5: invalid payload versions",
            "residual/source/correction/boundary/divergence/recombination/insertion/parent payload versions are excluded",
            "POLICY_RULE",
            "membership object must not smuggle downstream or non-trace roles into T_zeta",
            "object role purity is a precondition, not a solved source theorem",
        ),
        Entry(
            "O6: undefined object case",
            "object slot missing or undefined makes membership not well-posed",
            "OPEN",
            "a later declaration/theorem route needs a defined membership-test object domain",
            "undefined object is not a null object and not neutral F_zeta deferral",
        ),
    ]


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  What objects may occupy the zeta_Bs membership-test slot before membership can be used later?")
    print("\nDiscipline:\n")
    print("  This script inventories object preconditions only.")
    print("  zeta_Bs names the payload object being tested for membership, not a relation between zeta and a B_s branch.")
    print("  It is not F_zeta, not B_s/F_zeta insertion, and not a trace-normalization expression.")
    with out.governance_assessments():
        out.line(f"{SCRIPT_LABEL} opened", StatusMark.PASS, "object precondition ledger only; no active membership installed")


def case_1(out: ScriptOutput, entries: List[Entry]) -> None:
    header("Case 1: zeta_Bs object precondition entries")
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
        ("X1: object as F_zeta", "treat zeta_Bs as neutral F_zeta response", "membership object and response placeholder remain separate"),
        ("X2: object as insertion", "treat zeta_Bs as B_s/F_zeta insertion payload", "insertion remains closed"),
        ("X3: object as normalization", "use zeta_Bs to install zeta/d or 2*zeta/d", "trace normalization remains separate and branch-required"),
        ("X4: object chooses branch", "let object naming select metric or scale branch", "branch choice requires explicit record"),
        ("X5: invalid payload as trace object", "allow residual/source/correction payloads into zeta_Bs", "role-purity exclusion required"),
    ]
    for name, shortcut, reason in shortcuts:
        subheader(name)
        print(f"Shortcut: {shortcut}")
        with out.counterexamples():
            out.line(name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {reason}")


def case_3(out: ScriptOutput) -> None:
    header("Case 3: Open obligations")
    obligations = [
        ("O1: define membership-test object domain", "later use requires a defined object domain for candidate trace payloads", "OPEN"),
        ("O2: branch-index object where needed", "branch-sensitive object claims must use zeta_Bs_metric or zeta_Bs_scale", "BRANCH_INDEXED"),
        ("O3: preserve object-role purity", "object slot must exclude residual/source/correction/boundary/downstream payloads", "OPEN"),
        ("O4: keep object distinct from F_zeta and trace normalization", "object inventory must not install response expressions", "POLICY_RULE"),
    ]
    for oid, description, status in obligations:
        subheader(oid)
        with out.unresolved_obligations():
            out.line(oid, mark(status), f"{status}: {description}")


def case_4(out: ScriptOutput) -> None:
    header("Case 4: Local conclusions")
    with out.governance_assessments():
        out.line("zeta_Bs object ledger complete", StatusMark.PASS, "object slot sharpened without membership declaration")
        out.line("active object membership not installed", StatusMark.DEFER, "object candidates remain diagnostic / compatible-if-declared only")
    print("\nPossible next script:")
    print("  candidate_Tzeta_sector_precondition_ledger.py")


def record_governance(ns, entries: List[Entry]) -> None:
    record_marker(ns, MARKER_ID, MARKER_ID, "Group 41 safe-membership precondition continuation")
    for idx, item in enumerate(entries, 1):
        record_claim(ns, f"{MARKER_ID}_c{idx}", MARKER_ID, f"{item.name}: {item.subject}. {item.detail}. Boundary: {item.boundary}.")
    for idx, item in enumerate(entries, 1):
        if item.status in {"CONDITIONAL", "BRANCH_INDEXED", "OPEN", "POLICY_RULE"}:
            record_obligation(ns, f"{MARKER_ID}_o{idx}", item.name, f"Carry forward {item.subject} as an object precondition only. {item.boundary}.", item.status)


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
