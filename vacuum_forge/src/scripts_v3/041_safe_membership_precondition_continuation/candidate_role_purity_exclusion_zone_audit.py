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

SCRIPT_LABEL = "Candidate Role Purity Exclusion Zone Audit"
MARKER_ID = "g41_role_purity"
DEPENDENCIES = [
    ("g40_safety_split", "040_split_safe_trace_anchor_precondition_audit__candidate_residual_source_safety_split_audit", "g40_safety_split"),
    ("g40_membership_precond", "040_split_safe_trace_anchor_precondition_audit__candidate_safe_membership_split_safe_preconditions", "g40_membership_precond"),
    ("g41_criterion_matrix", "041_safe_membership_precondition_continuation__candidate_membership_criterion_precondition_matrix", "g41_criterion_matrix"),
]


def build_entries() -> List[Entry]:
    zones = [
        ("E1: residual payload exclusion", "residual zeta/kappa payloads cannot enter safe membership", "membership cannot imply residual nonentry or residual kill"),
        ("E2: ordinary source payload exclusion", "ordinary matter source load must not be hidden in membership", "ordinary source routing theorem is not solved"),
        ("E3: A-sector mass payload exclusion", "A-sector mass routing must remain protected from membership payloads", "A-sector source protection remains a boundary only"),
        ("E4: correction tensor payload exclusion", "correction tensor roles cannot be smuggled into T_zeta", "H/correction insertability remains separate"),
        ("E5: boundary or shell payload exclusion", "boundary, shell, and support loads must remain visible", "visibility is not boundary neutrality theorem"),
        ("E6: divergence repair payload exclusion", "divergence or correction repair terms cannot be hidden in membership", "explicitness is not divergence safety"),
        ("E7: trace-normalization / branch-choice payload exclusion", "membership cannot carry zeta/d, 2*zeta/d, or branch selection", "trace normalization and branch choice remain separate nodes"),
        ("E8: recombination payload exclusion", "recombination or downstream merge roles cannot enter membership", "recombination gate remains closed"),
        ("E9: active O or projector payload exclusion", "membership cannot become active O or a projector", "T_zeta is not O"),
        ("E10: B_s/F_zeta insertion payload exclusion", "membership cannot insert B_s/F_zeta or F_zeta", "insertion remains downstream"),
        ("E11: parent closure payload exclusion", "parent-equation closure cannot be hidden in membership", "parent closure remains not ready"),
    ]
    return [Entry(name, subject, "POLICY_RULE", "mandatory exclusion zone for role-pure safe-membership preconditions", boundary) for name, subject, boundary in zones]


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  Which payload roles must be excluded before safe trace membership can be used later?")
    print("\nDiscipline:\n")
    print("  This script audits role-purity and exclusion zones as policy/precondition boundaries.")
    print("  It protects ordinary matter and A-sector mass routing only as a boundary.")
    print("  It does not prove source no-double-counting, residual nonentry, divergence safety, boundary neutrality, insertion, or parent closure.")
    with out.governance_assessments():
        out.line(f"{SCRIPT_LABEL} opened", StatusMark.PASS, "role-purity exclusion audit only; no source theorem or no-overlap proof")


def case_1(out: ScriptOutput, entries: List[Entry]) -> None:
    header("Case 1: Mandatory exclusion-zone entries")
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
        ("X1: exclusion as no-overlap theorem", "treat exclusions as a proved no-overlap operator", "exclusion zones are preconditions only"),
        ("X2: role purity as source theorem", "treat role purity as ordinary source no-double-counting proof", "source-routing theorem remains separate"),
        ("X3: membership as residual nonentry", "claim membership proves residual nonentry", "residual nonentry remains a separate gate"),
        ("X4: membership as branch choice", "hide trace-normalization or branch choice in membership", "node separation required"),
        ("X5: membership as downstream repair", "use membership to repair divergence, boundary, insertion, or parent gaps", "downstream repair remains forbidden"),
    ]
    for name, shortcut, reason in shortcuts:
        subheader(name)
        print(f"Shortcut: {shortcut}")
        with out.counterexamples():
            out.line(name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {reason}")


def case_3(out: ScriptOutput) -> None:
    header("Case 3: Open obligations")
    obligations = [
        ("O1: later no-double-counting theorem", "ordinary source and A-sector mass protection require separate theorem support before active use", "NOT_DERIVED"),
        ("O2: later residual nonentry theorem", "membership cannot imply residual nonentry; residual gate remains separate", "NOT_DERIVED"),
        ("O3: later divergence/boundary safety theorem", "divergence explicitness and boundary visibility require separate theorem support", "NOT_DERIVED"),
        ("O4: enforce exclusion zones in future routes", "later declaration/theorem/adoption routes must preserve all exclusion zones", "OPEN"),
    ]
    for oid, description, status in obligations:
        subheader(oid)
        with out.unresolved_obligations():
            out.line(oid, mark(status), f"{status}: {description}")


def case_4(out: ScriptOutput) -> None:
    header("Case 4: Local conclusions")
    with out.governance_assessments():
        out.line("role-purity exclusion audit complete", StatusMark.PASS, "mandatory exclusion zones stated as preconditions")
        out.line("source/residual/divergence theorems not supplied", StatusMark.DEFER, "theorem support remains separate")
    print("\nPossible next script:")
    print("  candidate_diagnostic_vs_active_membership_boundary.py")


def record_governance(ns, entries: List[Entry]) -> None:
    record_marker(ns, MARKER_ID, MARKER_ID, "Group 41 safe-membership precondition continuation")
    for idx, item in enumerate(entries, 1):
        record_claim(ns, f"{MARKER_ID}_c{idx}", MARKER_ID, f"{item.name}: {item.subject}. {item.detail}. Boundary: {item.boundary}.")
    for idx, item in enumerate(entries, 1):
        record_obligation(ns, f"{MARKER_ID}_o{idx}", item.name, f"Preserve exclusion zone: {item.subject}. {item.boundary}.", item.status)
    record_obligation(ns, f"{MARKER_ID}_source_theorem", "later source-routing theorem", "Role purity does not prove ordinary source or A-sector mass routing; later theorem support is required.", "NOT_DERIVED")
    record_obligation(ns, f"{MARKER_ID}_residual_theorem", "later residual nonentry theorem", "Membership does not imply residual nonentry; later theorem support is required.", "NOT_DERIVED")


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
