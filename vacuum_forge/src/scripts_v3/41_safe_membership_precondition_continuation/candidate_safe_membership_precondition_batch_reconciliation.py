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

SCRIPT_LABEL = "Candidate Safe-Membership Precondition Batch Reconciliation"
MARKER_ID = "g41_recon"
DEPENDENCIES = [
    ("g40_summary", "40_split_safe_trace_anchor_precondition_audit__candidate_group_40_status_summary", "g40_summary"),
    ("g41_problem", "41_safe_membership_precondition_continuation__candidate_safe_membership_precondition_problem", "g41_problem"),
    ("g41_zeta_object", "41_safe_membership_precondition_continuation__candidate_zeta_Bs_object_precondition_ledger", "g41_zeta_object"),
    ("g41_tzeta_sector", "41_safe_membership_precondition_continuation__candidate_Tzeta_sector_precondition_ledger", "g41_tzeta_sector"),
    ("g41_criterion_matrix", "41_safe_membership_precondition_continuation__candidate_membership_criterion_precondition_matrix", "g41_criterion_matrix"),
    ("g41_role_purity", "41_safe_membership_precondition_continuation__candidate_role_purity_exclusion_zone_audit", "g41_role_purity"),
    ("g41_active_boundary", "41_safe_membership_precondition_continuation__candidate_diagnostic_vs_active_membership_boundary", "g41_active_boundary"),
]


def build_entries() -> List[Entry]:
    return [
        Entry(
            "Q1: opener expectation",
            "Group 41 opened as safe-membership precondition continuation",
            "PASS",
            "expected if current membership remained diagnostic / compatible-if-declared only",
            "summary may call this precondition sharpening only",
        ),
        Entry(
            "Q2: object expectation",
            "zeta_Bs object slot was sharpened without becoming F_zeta, insertion, normalization, or branch choice",
            "PASS",
            "expected if branch-sensitive objects are explicitly indexed",
            "summary must preserve object/declaration boundary",
        ),
        Entry(
            "Q3: sector expectation",
            "T_zeta safe trace-sector target was sharpened without becoming active O",
            "PASS",
            "expected if diagnostic and future sector statuses remain separate",
            "summary must preserve T_zeta is not projector/O",
        ),
        Entry(
            "Q4: criterion expectation",
            "membership criteria were stated as preconditions only",
            "PASS",
            "expected if testability means precondition clarity, not theorem readiness",
            "summary must preserve criterion/theorem boundary",
        ),
        Entry(
            "Q5: role-purity expectation",
            "mandatory exclusion zones were stated as policy/precondition boundaries",
            "PASS",
            "expected if residual/source/divergence/boundary gates remain separate theorem routes",
            "summary must not claim no-double-counting or residual nonentry theorem",
        ),
        Entry(
            "Q6: diagnostic-active expectation",
            "diagnostic membership and future declaration/theorem routes were separated",
            "PASS",
            "expected if active membership remains forbidden here",
            "summary must preserve active membership not installed",
        ),
        Entry(
            "Q7: downstream gates",
            "Package B adoption, insertion, active O, residual control, and parent closure remain closed",
            "NOT_READY",
            "expected final boundary",
            "summary must not open field-equation routes",
        ),
    ]


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  Did the Group 41 batch produce the expected safe-membership precondition sharpening shape,")
    print("  and what should a later status summary preserve?")
    print("\nDiscipline:\n")
    print("  This script reconciles the Group 41 batch.")
    print("  It does not close the group as final summary.")
    print("  It does not choose a branch, complete declarations, adopt Package B, prove membership,")
    print("  prove incidence, install active O, insert B_s/F_zeta, or open parent closure.")
    with out.governance_assessments():
        out.line(f"{SCRIPT_LABEL} opened", StatusMark.PASS, "batch reconciliation only; no final summary or downstream route")


def case_1(out: ScriptOutput, entries: List[Entry]) -> None:
    header("Case 1: Batch reconciliation entries")
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
        ("X1: reconciliation as final summary", "treat this script as group close", "final summary should be written after actual outputs are reviewed"),
        ("X2: preconditions as declaration", "say sharpened membership slots completed safe-membership declaration", "preconditions are not declarations"),
        ("X3: criteria as theorem", "say membership criteria prove membership", "theorem support remains separate"),
        ("X4: role-purity as no-overlap", "say exclusion zones prove no-overlap or source no-double-counting", "proof remains separate"),
        ("X5: diagnostic status as active", "use diagnostic membership as active projector or insertion support", "diagnostic labels are inert"),
        ("X6: readiness as downstream readiness", "open insertion, active O, residual control, adoption, or parent route", "downstream gates remain closed"),
    ]
    for name, shortcut, reason in shortcuts:
        subheader(name)
        print(f"Shortcut: {shortcut}")
        with out.counterexamples():
            out.line(name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {reason}")


def case_3(out: ScriptOutput) -> None:
    header("Case 3: Open obligations for final summary")
    obligations = [
        ("O1: summary must follow actual outputs", "final summary must report any mismatch in batch outputs", "OPEN"),
        ("O2: preserve compatible-if-declared status", "final summary must keep zeta_Bs -> T_zeta diagnostic / compatible-if-declared only", "COMPATIBLE_IF_DECLARED"),
        ("O3: preserve precondition/theorem boundary", "precondition sharpening must not become proof or declaration", "POLICY_RULE"),
        ("O4: preserve downstream locks", "Package B adoption, insertion, active O, residual control, and parent closure remain closed", "NOT_READY"),
    ]
    for oid, description, status in obligations:
        subheader(oid)
        with out.unresolved_obligations():
            out.line(oid, mark(status), f"{status}: {description}")


def case_4(out: ScriptOutput) -> None:
    header("Case 4: Local conclusions")
    conclusions = [
        ("batch reconciliation prepared", "PASS", "write summary only after actual outputs are reviewed"),
        ("no group close here", "DEFER", "candidate_group_41_status_summary.py should be written after review"),
    ]
    with out.governance_assessments():
        for name, status, detail in conclusions:
            out.line(name, mark(status), detail)
    print("\nPossible next script:")
    print("  candidate_group_41_status_summary.py")


def record_governance(ns, entries: List[Entry]) -> None:
    record_marker(ns, MARKER_ID, MARKER_ID, "Group 41 safe-membership precondition continuation")
    for idx, item in enumerate(entries, 1):
        record_claim(ns, f"{MARKER_ID}_c{idx}", MARKER_ID, f"{item.name}: {item.subject}. {item.detail}. Boundary: {item.boundary}.")
    for idx, item in enumerate(entries, 1):
        if item.status in {"PASS", "NOT_READY"}:
            record_obligation(ns, f"{MARKER_ID}_o{idx}", item.name, f"Final summary must preserve: {item.subject}. {item.boundary}.", item.status)


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
