# Group:
#   38_trace_anchor_explicit_declaration_record
# Script type:
#   AUDIT / EXPLORATION

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

SCRIPT_LABEL = "Candidate B_s Notation Usage Audit"
MARKER_ID = "g38_bs_usage"

DEPENDENCIES = [
    ("g38_recon", "38_trace_anchor_explicit_declaration_record__candidate_trace_anchor_declaration_batch_reconciliation", "g38_recon"),
    ("g38_bs_fork", "38_trace_anchor_explicit_declaration_record__candidate_Bs_convention_declaration_fork", "g38_bs_fork"),
    ("g38_norm", "38_trace_anchor_explicit_declaration_record__candidate_trace_normalization_declaration_attempt", "g38_norm"),
    ("g37_joint", "37_trace_anchor_declaration_option_sieve__candidate_trace_anchor_joint_declaration_package_sieve", "g37_joint_packages"),
]


# Configuration notes:
# This script deliberately does not choose a convention. If later evidence is
# supplied, fill these with explicit strings and update the cases accordingly.
# Allowed evidence tags:
#   "metric_coefficient", "scale_factor", "ambiguous", "diagnostic_only"
BS_SYMBOL_USAGE_EVIDENCE: List[str] = []
BS_TEXTUAL_USAGE_NOTES: List[str] = []


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
        "LEADING_HYPOTHESIS": StatusMark.INFO,
        "SUPPORTED_IF": StatusMark.INFO,
        "AMBIGUOUS": StatusMark.DEFER,
        "DEFER": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "REJECTED": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "NOT_READY": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
    }.get(status, StatusMark.INFO)


def record_marker(ns, marker_id: str, symbol_name: str):
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[],
        output=sp.Symbol(symbol_name),
        method="notation usage audit marker; no physical derivation",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
        scope="Group 38 B_s notation usage audit",
    )


def record_claim(ns, claim_id: str, marker_id: str, statement: str):
    ns.record_claim(
        ClaimRecord(
            claim_id=claim_id,
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.POLICY_RULE,
            statement=statement,
            derivation_ids=[marker_id],
            obligation_ids=[],
        )
    )


def record_obligation(ns, obligation_id: str, statement: str, status=ObligationStatus.OPEN):
    ns.record_obligation(
        ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=obligation_id,
            status=status,
            required_by=[SCRIPT_ID],
            description=statement,
        )
    )


@dataclass
class UsageEntry:
    name: str
    evidence_class: str
    implication: str
    status: str
    allowed_if: str
    blocked_if: str
    consequence: str


def build_entries() -> List[UsageEntry]:
    return [
        UsageEntry(
            name="U1: inherited B notation",
            evidence_class="B and B_s appear metric-coefficient-like if they denote radial metric factors rather than square-root scale factors",
            implication="metric-coefficient convention would give log(B_s)=2*zeta/d",
            status="SUPPORTED_IF",
            allowed_if="B_s is explicitly declared as a metric coefficient or radial/spatial metric factor",
            blocked_if="B_s is actually a scale factor, determinant factor, or square-root metric response",
            consequence="metric-coefficient branch becomes leading only after notation evidence is explicit",
        ),
        UsageEntry(
            name="U2: scale-factor language",
            evidence_class="B_s appears scale-factor-like if it is described as a scale response, exponential scale, or per-direction volume factor",
            implication="scale-factor convention would give log(B_s)=zeta/d",
            status="SUPPORTED_IF",
            allowed_if="B_s is explicitly declared as a scale factor rather than metric coefficient",
            blocked_if="B_s inherits metric coefficient notation from B or from line-element use",
            consequence="scale-factor branch remains coherent but requires explicit notation support",
        ),
        UsageEntry(
            name="U3: F_zeta functional language",
            evidence_class="F_zeta may describe a response functional rather than deciding scale-vs-metric notation",
            implication="F_zeta alone does not choose zeta/d or 2*zeta/d",
            status="AMBIGUOUS",
            allowed_if="F_zeta is kept as neutral response placeholder until B_s convention is fixed",
            blocked_if="F_zeta is used to hide the factor-of-two choice",
            consequence="functional language must not bypass B_s convention declaration",
        ),
        UsageEntry(
            name="U4: recovery-compatible notation",
            evidence_class="Schwarzschild, gamma, AB=1, B=1/A, insertion convenience, or parent fit",
            implication="not valid notation evidence",
            status="REJECTED",
            allowed_if="never as convention selector",
            blocked_if="recovery or downstream fit chooses the convention",
            consequence="target-selected declaration is rejected as shortcut",
        ),
        UsageEntry(
            name="U5: no evidence supplied",
            evidence_class="no explicit notation evidence has been supplied in this batch",
            implication="declaration remains deferred",
            status="DEFER",
            allowed_if="Group 38 remains exploration rather than completed declaration record",
            blocked_if="later scripts pretend B_s convention was chosen",
            consequence="write further notation-origin exploration or supply explicit theory choice",
        ),
    ]


def classify_configured_evidence():
    evidence = set(BS_SYMBOL_USAGE_EVIDENCE)
    if "metric_coefficient" in evidence and "scale_factor" in evidence:
        return "CONFLICT", "both metric_coefficient and scale_factor evidence tags were supplied"
    if "metric_coefficient" in evidence:
        return "METRIC_LEADING", "configured evidence points to metric-coefficient convention"
    if "scale_factor" in evidence:
        return "SCALE_LEADING", "configured evidence points to scale-factor convention"
    if "diagnostic_only" in evidence:
        return "DIAGNOSTIC_ONLY", "configured evidence supports diagnostic-only use, not active declaration"
    return "DEFERRED", "no explicit B_s notation evidence supplied"


def case_0(out: ScriptOutput):
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  What notation evidence, if any, supports treating B_s as a scale factor")
    print("  versus a metric coefficient before Group 38 can fill trace-anchor declarations?")
    print("\nDiscipline:\n")
    print("  This script audits notation usage evidence only.")
    print("  It does not choose a B_s convention.")
    print("  It does not fill trace-normalization or safe-membership declarations.")
    print("  It does not adopt Package B, prove either component, or open insertion.")
    print("\nTiny goblin rule:\n  Read the label on the jar before pouring the zeta.")
    with out.governance_assessments():
        out.line("B_s notation usage audit opened", StatusMark.PASS, "exploration only; no convention installed")


def case_1(out: ScriptOutput):
    header("Case 1: Symbolic B_s notation ledger")
    B_metric, B_scale, F_neutral, no_evidence, conflict = sp.symbols("B_metric B_scale F_neutral no_evidence conflict")
    P_insertion, P_active_O, P_residual_kill, P_parent = sp.symbols("P_insertion P_active_O P_residual_kill P_parent")
    L_notation = sp.simplify(B_metric + B_scale + F_neutral + no_evidence + conflict)
    L_downstream = sp.simplify(P_insertion + P_active_O + P_residual_kill + P_parent)
    print(f"Notation evidence load: L_Bs_notation = {L_notation}")
    print(f"Downstream closed load: L_downstream_closed = {L_downstream}")
    with out.derived_results():
        out.line("B_s notation symbolic ledger stated", StatusMark.PASS, f"L_Bs_notation={L_notation}; L_downstream_closed={L_downstream}")


def case_2(out: ScriptOutput, entries: List[UsageEntry]):
    header("Case 2: Notation evidence classes")
    for item in entries:
        subheader(item.name)
        print(f"Evidence class: {item.evidence_class}")
        print(f"Implication: {item.implication}")
        with out.governance_assessments():
            out.line(
                item.name,
                mark(item.status),
                f"{item.status}: allowed if {item.allowed_if}; blocked if {item.blocked_if}; consequence: {item.consequence}",
            )


def case_3(out: ScriptOutput):
    header("Case 3: Configured evidence classification")
    classification, detail = classify_configured_evidence()
    print(f"Configured BS_SYMBOL_USAGE_EVIDENCE = {BS_SYMBOL_USAGE_EVIDENCE}")
    print(f"Configured BS_TEXTUAL_USAGE_NOTES = {BS_TEXTUAL_USAGE_NOTES}")
    print(f"classification = {classification}")
    print(f"detail = {detail}")

    status_mark = {
        "METRIC_LEADING": StatusMark.INFO,
        "SCALE_LEADING": StatusMark.INFO,
        "DIAGNOSTIC_ONLY": StatusMark.INFO,
        "DEFERRED": StatusMark.DEFER,
        "CONFLICT": StatusMark.FAIL,
    }.get(classification, StatusMark.INFO)

    with out.governance_assessments():
        out.line("configured B_s notation evidence classified", status_mark, f"{classification}: {detail}")
        out.line("no convention installed", StatusMark.DEFER, "classification is evidence audit, not declaration record")


def case_4(out: ScriptOutput):
    header("Case 4: Invalid notation shortcuts")
    shortcuts = [
        ("X1: B_s by recovery", "choose scale or metric convention from Schwarzschild, AB=1, gamma, or B=1/A", "recovery is audit, not notation source"),
        ("X2: hidden factor of two", "leave scale-vs-metric language implicit while using zeta/d or 2*zeta/d", "factor-of-two ambiguity must be explicit"),
        ("X3: F_zeta hides convention", "use F_zeta as a neutral name while smuggling a chosen convention", "functional language cannot hide declaration choice"),
        ("X4: notation evidence as adoption", "treat convention evidence as Package B adoption", "adoption requires separate explicit decision"),
        ("X5: notation evidence as insertion", "treat convention evidence as B_s/F_zeta insertion", "insertion remains downstream and not ready"),
    ]
    for name, shortcut, reason in shortcuts:
        subheader(name)
        print(f"Shortcut: {shortcut}")
        with out.counterexamples():
            out.line(name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {reason}")


def case_5(out: ScriptOutput):
    header("Case 5: Local conclusions")
    classification, detail = classify_configured_evidence()
    with out.governance_assessments():
        if classification == "DEFERRED":
            out.line("B_s convention remains deferred", StatusMark.DEFER, "no explicit notation evidence supplied; Group 38 declaration remains blocked")
        elif classification == "CONFLICT":
            out.line("B_s convention evidence conflict", StatusMark.FAIL, "conflicting notation evidence requires repair before declaration")
        else:
            out.line("B_s convention has a leading notation hypothesis", StatusMark.INFO, f"{classification}: {detail}; not installed")
        out.line("downstream gates remain closed", StatusMark.DEFER, "notation audit is not trace-anchor declaration, adoption, theorem proof, insertion, active O, residual control, or parent readiness")


def record_governance(ns, entries: List[UsageEntry]):
    record_marker(ns, MARKER_ID, "g38_bs_notation_usage_audit")
    for idx, item in enumerate(entries, 1):
        record_claim(
            ns,
            f"g38_bs_usage_c{idx}",
            MARKER_ID,
            f"{item.name}: {item.evidence_class}. Implication: {item.implication}. Allowed if {item.allowed_if}. Blocked if {item.blocked_if}. Consequence: {item.consequence}.",
        )
    classification, detail = classify_configured_evidence()
    record_claim(ns, "g38_bs_usage_actual", MARKER_ID, f"Configured B_s notation evidence classification: {classification}. {detail}. This does not install a convention.")
    record_obligation(ns, "g38_bs_usage_supply_evidence_or_choose", "Supply explicit B_s notation evidence or make a separate theory choice before completing Group 38 declaration values.")
    record_obligation(ns, "g38_bs_usage_downstream_closed", "Keep insertion, active O, residual control, and parent closure closed after notation audit.", ObligationStatus.DEFERRED)


def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    entries = build_entries()
    case_0(out)
    case_1(out)
    case_2(out, entries)
    case_3(out)
    case_4(out)
    case_5(out)
    record_governance(ns, entries)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
