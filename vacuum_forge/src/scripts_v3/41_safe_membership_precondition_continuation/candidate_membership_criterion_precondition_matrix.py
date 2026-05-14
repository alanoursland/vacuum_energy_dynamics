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

SCRIPT_LABEL = "Candidate Membership Criterion Precondition Matrix"
MARKER_ID = "g41_criterion_matrix"
DEPENDENCIES = [
    ("g40_membership_precond", "40_split_safe_trace_anchor_precondition_audit__candidate_safe_membership_split_safe_preconditions", "g40_membership_precond"),
    ("g41_zeta_object", "41_safe_membership_precondition_continuation__candidate_zeta_Bs_object_precondition_ledger", "g41_zeta_object"),
    ("g41_tzeta_sector", "41_safe_membership_precondition_continuation__candidate_Tzeta_sector_precondition_ledger", "g41_tzeta_sector"),
]


def build_entries() -> List[Entry]:
    return [
        Entry(
            "C1: type criterion",
            "candidate object must be typed as a membership-test trace payload object",
            "CONDITIONAL",
            "type check makes the test well-posed but does not prove membership",
            "not a theorem and not declaration support by itself",
        ),
        Entry(
            "C2: trace-payload criterion",
            "payload must be trace-only and suitable for T_zeta safe trace-sector testing",
            "SPLIT_SAFE",
            "trace-payload criterion can be stated branch-independently if no branch expression is installed",
            "not trace-normalization declaration",
        ),
        Entry(
            "C3: role-purity criterion",
            "payload must not carry residual, source, correction, boundary, divergence, recombination, insertion, active O, or parent roles",
            "POLICY_RULE",
            "role-purity check blocks hidden downstream roles",
            "not full source no-double-counting theorem",
        ),
        Entry(
            "C4: branch-index consistency criterion",
            "branch-sensitive membership tests must keep metric and scale variants explicitly indexed",
            "BRANCH_INDEXED",
            "zeta_Bs_metric and zeta_Bs_scale remain parallel when needed",
            "branch consistency is not branch choice",
        ),
        Entry(
            "C5: diagnostic-inertness criterion",
            "diagnostic membership labels must have no source, metric, divergence, projection, insertion, theorem, or adoption effect",
            "DIAGNOSTIC_ONLY",
            "diagnostic compatibility is the safest current status",
            "diagnostic label cannot become active projector",
        ),
        Entry(
            "C6: exclusion-zone criterion",
            "mandatory exclusion zones must be named before any later declaration or theorem route",
            "POLICY_RULE",
            "exclusion-zone visibility blocks payload smuggling",
            "exclusion visibility is not no-overlap proof",
        ),
        Entry(
            "C7: declaration-support criterion",
            "later declaration support needs closed object, sector, domain/codomain, criterion, role-purity, branch-status, and scope obligations",
            "NOT_DECLARED",
            "declaration support is a future route only",
            "not ready in Group 41",
        ),
        Entry(
            "C8: theorem-support criterion",
            "later theorem support needs an actual derivation or proof beyond criteria visibility",
            "NOT_DERIVED",
            "criteria state what a theorem would need",
            "membership testable does not mean theorem-ready",
        ),
        Entry(
            "C9: testability meaning",
            "membership testable means preconditions are explicit enough to know what a later theorem or declaration would require",
            "COMPATIBLE_IF_DECLARED",
            "testability is precondition clarity only",
            "not proof, declaration, adoption, insertion, or parent readiness",
        ),
    ]


def case_0(out: ScriptOutput) -> None:
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  Which criteria would make zeta_Bs -> T_zeta membership testable in a later route?")
    print("\nDiscipline:\n")
    print("  This script states criterion preconditions only.")
    print("  Membership-testable means the requirements are explicit enough to know what a later theorem or declaration would need.")
    print("  It does not mean theorem-ready, declaration-ready, adopted, derived, or insertable.")
    with out.governance_assessments():
        out.line(f"{SCRIPT_LABEL} opened", StatusMark.PASS, "membership criterion matrix only; no membership declaration or theorem proof")


def case_1(out: ScriptOutput, entries: List[Entry]) -> None:
    header("Case 1: Membership criterion precondition entries")
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
        ("X1: criterion as proof", "treat a listed criterion as proof of membership", "criterion visibility is not theorem support"),
        ("X2: testable as theorem-ready", "treat membership-testable as theorem-ready", "testable means preconditions are explicit only"),
        ("X3: role criterion as source theorem", "treat role purity as source no-double-counting theorem", "source theorem remains separate"),
        ("X4: branch criterion as choice", "let branch-index consistency choose metric or scale branch", "branch indexing is not branch choice"),
        ("X5: diagnostic criterion as active", "let diagnostic-inert label become active membership", "diagnostic remains inert"),
    ]
    for name, shortcut, reason in shortcuts:
        subheader(name)
        print(f"Shortcut: {shortcut}")
        with out.counterexamples():
            out.line(name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {reason}")


def case_3(out: ScriptOutput) -> None:
    header("Case 3: Open obligations")
    obligations = [
        ("O1: define domain/codomain", "domain and codomain must be stated before a later membership test", "OPEN"),
        ("O2: keep criteria non-theorem", "criteria must not be reported as proofs or declarations", "POLICY_RULE"),
        ("O3: preserve diagnostic inertness", "diagnostic labels must not gain source, metric, projector, or insertion effects", "DIAGNOSTIC_ONLY"),
        ("O4: record theorem/declaration support separately", "later theorem or declaration routes require explicit records beyond this matrix", "NOT_DECLARED"),
    ]
    for oid, description, status in obligations:
        subheader(oid)
        with out.unresolved_obligations():
            out.line(oid, mark(status), f"{status}: {description}")


def case_4(out: ScriptOutput) -> None:
    header("Case 4: Local conclusions")
    with out.governance_assessments():
        out.line("membership criterion matrix complete", StatusMark.PASS, "criteria made explicit as preconditions only")
        out.line("membership theorem not supplied", StatusMark.DEFER, "later proof/declaration support remains separate")
    print("\nPossible next script:")
    print("  candidate_role_purity_exclusion_zone_audit.py")


def record_governance(ns, entries: List[Entry]) -> None:
    record_marker(ns, MARKER_ID, MARKER_ID, "Group 41 safe-membership precondition continuation")
    for idx, item in enumerate(entries, 1):
        record_claim(ns, f"{MARKER_ID}_c{idx}", MARKER_ID, f"{item.name}: {item.subject}. {item.detail}. Boundary: {item.boundary}.")
    for idx, item in enumerate(entries, 1):
        if item.status in {"CONDITIONAL", "POLICY_RULE", "BRANCH_INDEXED", "DIAGNOSTIC_ONLY", "NOT_DECLARED", "NOT_DERIVED", "COMPATIBLE_IF_DECLARED"}:
            record_obligation(ns, f"{MARKER_ID}_o{idx}", item.name, f"Carry forward {item.subject} as a criterion precondition only. {item.boundary}.", item.status)


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
