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

SCRIPT_LABEL = "Candidate Tzeta Sector Precondition Ledger"
MARKER_ID = "g41_tzeta_sector"
DEPENDENCIES = [
    ("g40_summary", "40_split_safe_trace_anchor_precondition_audit__candidate_group_40_status_summary", "g40_summary"),
    ("g40_membership_precond", "40_split_safe_trace_anchor_precondition_audit__candidate_safe_membership_split_safe_preconditions", "g40_membership_precond"),
    ("g41_zeta_object", "41_safe_membership_precondition_continuation__candidate_zeta_Bs_object_precondition_ledger", "g41_zeta_object"),
]


def build_entries() -> List[Entry]:
    return [
        Entry(
            "T1: safe trace-sector target",
            "T_zeta is the safe trace-sector target for membership testing",
            "COMPATIBLE_IF_DECLARED",
            "sector label may describe where a valid trace payload would land if declared",
            "not an active projector, not O, and not a field-equation sector",
        ),
        Entry(
            "T2: diagnostic sector label",
            "diagnostic_T_zeta_label may label compatibility only",
            "DIAGNOSTIC_ONLY",
            "diagnostic sector has no source, metric, divergence, projection, insertion, theorem, or adoption effect",
            "diagnostic label is not active membership",
        ),
        Entry(
            "T3: branch-neutral default",
            "T_zeta is branch-neutral by default only when the membership test remains branch-insensitive",
            "CONDITIONAL",
            "branch-neutral sector naming must not hide metric/scale differences",
            "branch-neutral is not a branch choice",
        ),
        Entry(
            "T4: branch-indexed sector variants",
            "T_zeta_metric and T_zeta_scale may be listed as conditional variants",
            "BRANCH_INDEXED",
            "variants are allowed only as explicitly parallel non-active sector candidates",
            "parallel sectors are not completed declarations",
        ),
        Entry(
            "T5: future sector route",
            "future_active_T_zeta_sector is a later declaration/theorem target only after obligations close",
            "NOT_DECLARED",
            "future route requires object, domain/codomain, criterion, role-purity, branch-status, and exclusion-zone support",
            "not declaration-ready in Group 41",
        ),
        Entry(
            "T6: sector exclusion boundary",
            "T_zeta excludes residual, source, correction, boundary, divergence repair, recombination, insertion, active O, and parent payloads",
            "POLICY_RULE",
            "safe trace-sector membership cannot become a downstream payload reservoir",
            "exclusion boundary is not a solved no-overlap theorem",
        ),
    ]


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  What must T_zeta mean before safe membership can be claimed in a later route?")
    print("\nDiscipline:\n")
    print("  This script inventories the safe trace-sector target only.")
    print("  T_zeta is not an active projector and not O.")
    print("  It is not incidence, no-overlap, residual control, insertion, or parent closure.")
    with out.governance_assessments():
        out.line(f"{SCRIPT_LABEL} opened", StatusMark.PASS, "T_zeta sector precondition ledger only; no active membership installed")


def case_1(out: ScriptOutput, entries: List[Entry]) -> None:
    header("Case 1: T_zeta sector precondition entries")
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
        ("X1: sector as active projector", "treat T_zeta as O or as an active projection map", "T_zeta is a sector target only"),
        ("X2: diagnostic sector as theorem", "treat diagnostic_T_zeta_label as theorem support", "diagnostic labels are inert"),
        ("X3: branch-neutral sector as hidden branch", "hide metric/scale differences under T_zeta", "branch-sensitive variants must be explicit"),
        ("X4: future sector as declared sector", "treat future_active_T_zeta_sector as current declaration", "future route remains not declared"),
        ("X5: sector as payload reservoir", "allow source/residual/correction/boundary payloads into T_zeta", "exclusion boundary required"),
    ]
    for name, shortcut, reason in shortcuts:
        subheader(name)
        print(f"Shortcut: {shortcut}")
        with out.counterexamples():
            out.line(name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {reason}")


def case_3(out: ScriptOutput) -> None:
    header("Case 3: Open obligations")
    obligations = [
        ("O1: define T_zeta sector criteria", "later use requires a sector definition with allowed trace-only payloads", "OPEN"),
        ("O2: preserve diagnostic inertness", "diagnostic_T_zeta_label must remain source/metric/divergence/projector/insertion inert", "DIAGNOSTIC_ONLY"),
        ("O3: branch-index sector variants if needed", "T_zeta_metric and T_zeta_scale must remain parallel when branch-sensitive", "BRANCH_INDEXED"),
        ("O4: keep T_zeta distinct from active O", "no active projector or no-overlap claim follows from sector naming", "POLICY_RULE"),
    ]
    for oid, description, status in obligations:
        subheader(oid)
        with out.unresolved_obligations():
            out.line(oid, mark(status), f"{status}: {description}")


def case_4(out: ScriptOutput) -> None:
    header("Case 4: Local conclusions")
    with out.governance_assessments():
        out.line("T_zeta sector ledger complete", StatusMark.PASS, "safe trace-sector target sharpened without active projector or declaration")
        out.line("active T_zeta sector not installed", StatusMark.DEFER, "future sector route remains not declared")
    print("\nPossible next script:")
    print("  candidate_membership_criterion_precondition_matrix.py")


def record_governance(ns, entries: List[Entry]) -> None:
    record_marker(ns, MARKER_ID, MARKER_ID, "Group 41 safe-membership precondition continuation")
    for idx, item in enumerate(entries, 1):
        record_claim(ns, f"{MARKER_ID}_c{idx}", MARKER_ID, f"{item.name}: {item.subject}. {item.detail}. Boundary: {item.boundary}.")
    for idx, item in enumerate(entries, 1):
        if item.status in {"COMPATIBLE_IF_DECLARED", "CONDITIONAL", "BRANCH_INDEXED", "NOT_DECLARED", "POLICY_RULE"}:
            record_obligation(ns, f"{MARKER_ID}_o{idx}", item.name, f"Carry forward {item.subject} as a sector precondition only. {item.boundary}.", item.status)


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
