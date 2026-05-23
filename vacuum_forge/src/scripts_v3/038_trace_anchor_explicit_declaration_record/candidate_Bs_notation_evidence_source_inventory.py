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

# Group:
#   38_trace_anchor_explicit_declaration_record
# Script type:
#   AUDIT / INVENTORY

ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"
SCRIPT_LABEL = "Candidate B_s Notation Evidence Source Inventory"
MARKER_ID = "g38_bs_evsrc"

DEPENDENCIES = [
    (
        "g38_bs_audit",
        "38_trace_anchor_explicit_declaration_record__candidate_Bs_notation_usage_audit",
        "g38_bs_notation_audit",
    ),
    (
        "g38_bs_fork",
        "38_trace_anchor_explicit_declaration_record__candidate_Bs_convention_declaration_fork",
        "g38_bs_fork",
    ),
    (
        "g38_recon",
        "38_trace_anchor_explicit_declaration_record__candidate_trace_anchor_declaration_batch_reconciliation",
        "g38_recon",
    ),
    (
        "g37_joint",
        "37_trace_anchor_declaration_option_sieve__candidate_trace_anchor_joint_declaration_package_sieve",
        "g37_joint_packages",
    ),
]


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
        "ADMISSIBLE_EVIDENCE": StatusMark.INFO,
        "WEAK_EVIDENCE": StatusMark.INFO,
        "AMBIGUOUS": StatusMark.DEFER,
        "REJECTED_SELECTOR": StatusMark.FAIL,
        "MISSING": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "PASS": StatusMark.PASS,
    }.get(status, StatusMark.INFO)


@dataclass
class EvidenceSource:
    name: str
    source: str
    possible_signal: str
    admissible_if: str
    blocked_if: str
    status: str
    consequence: str


@dataclass
class EvidenceRule:
    name: str
    rule: str
    reason: str


def build_sources() -> List[EvidenceSource]:
    return [
        EvidenceSource(
            name="E1: line-element metric usage",
            source="instances where B_s or B appears directly as a metric component multiplying a differential square",
            possible_signal="metric-coefficient convention; log(B_s)=2*zeta/d",
            admissible_if="B_s is explicitly used as a metric coefficient, radial metric factor, or spatial metric factor",
            blocked_if="the notation refers instead to a square-root scale or response amplitude",
            status="ADMISSIBLE_EVIDENCE",
            consequence="strongest admissible evidence for metric-coefficient branch",
        ),
        EvidenceSource(
            name="E2: scale-factor / exponential response usage",
            source="instances where B_s is described as a scale, per-direction scale response, or exponentiated scale factor",
            possible_signal="scale-factor convention; log(B_s)=zeta/d",
            admissible_if="B_s is explicitly tied to scale factor language rather than line-element coefficient language",
            blocked_if="B_s inherits B metric-coefficient notation or is used in a metric component slot",
            status="ADMISSIBLE_EVIDENCE",
            consequence="strongest admissible evidence for scale-factor branch",
        ),
        EvidenceSource(
            name="E3: determinant / volume-root usage",
            source="instances where B_s is derived from determinant, volume element, or per-dimension volume root language",
            possible_signal="usually scale-factor branch, but only if the root convention is explicit",
            admissible_if="the document states whether the object is a volume factor, a per-direction root, or a metric coefficient",
            blocked_if="determinant language is used loosely without defining root versus coefficient convention",
            status="WEAK_EVIDENCE",
            consequence="can support scale-factor branch only after root convention is explicit",
        ),
        EvidenceSource(
            name="E4: F_zeta functional usage",
            source="instances where F_zeta is used instead of B_s",
            possible_signal="neutral response-function evidence; does not choose factor of two by itself",
            admissible_if="F_zeta is paired with an explicit B_s convention elsewhere",
            blocked_if="F_zeta is used to hide scale-vs-metric convention",
            status="AMBIGUOUS",
            consequence="cannot choose convention alone",
        ),
        EvidenceSource(
            name="E5: prior script option labels",
            source="Group 37 declaration-ready package labels: scale_typed, metric_typed, scale_rolepure, metric_rolepure",
            possible_signal="confirms both branches are live options, not which branch is chosen",
            admissible_if="used only to preserve option set and node separation",
            blocked_if="option label is treated as selected declaration",
            status="AMBIGUOUS",
            consequence="keeps both branches available unless external notation evidence chooses one",
        ),
        EvidenceSource(
            name="E6: recovery / gamma / Schwarzschild fit",
            source="AB=1, B=1/A, gamma recovery, Schwarzschild exterior, parent-fit convenience",
            possible_signal="not admissible as notation evidence",
            admissible_if="never as convention selector; may be used later as audit after declaration",
            blocked_if="used to select zeta/d or 2*zeta/d",
            status="REJECTED_SELECTOR",
            consequence="must not choose the convention",
        ),
        EvidenceSource(
            name="E7: no explicit evidence found",
            source="no line-element, scale-factor, determinant-root, or explicit convention evidence is supplied",
            possible_signal="declaration remains deferred",
            admissible_if="reported as missing evidence rather than filled declaration",
            blocked_if="later scripts pretend a convention has been chosen",
            status="MISSING",
            consequence="write source-search or theory-choice script next",
        ),
    ]


def build_rules() -> List[EvidenceRule]:
    return [
        EvidenceRule(
            name="R1: evidence before convention",
            rule="A B_s convention must be chosen from notation-origin evidence or explicit theory choice, not from recovery.",
            reason="The convention determines the meaning of zeta/d versus 2*zeta/d.",
        ),
        EvidenceRule(
            name="R2: F_zeta neutrality",
            rule="F_zeta may remain neutral only if it does not hide the B_s scale-vs-metric choice.",
            reason="Functional notation cannot erase a factor-of-two declaration burden.",
        ),
        EvidenceRule(
            name="R3: option labels are not choices",
            rule="Group 37 declaration-ready package labels cannot by themselves select the convention.",
            reason="Option survival is weaker than declaration.",
        ),
        EvidenceRule(
            name="R4: downstream gates stay closed",
            rule="Notation evidence does not license insertion, active O, residual control, or parent closure.",
            reason="Convention evidence is not a field-equation theorem.",
        ),
    ]


def case_0(out: ScriptOutput):
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  Which sources of evidence are admissible for deciding whether B_s is")
    print("  scale-factor language or metric-coefficient language?")
    print("\nDiscipline:\n")
    print("  This script inventories evidence sources only.")
    print("  It does not choose a B_s convention.")
    print("  It does not fill trace-normalization or safe-membership declarations.")
    print("  It does not adopt Package B, prove either component, or open insertion.")
    print("\nTiny goblin rule:\n  Count the jars that could have labels. Do not write the label yet.")
    with out.governance_assessments():
        out.line("B_s notation evidence source inventory opened", StatusMark.PASS, "evidence-source audit only; no convention installed")


def case_1(out: ScriptOutput):
    header("Case 1: Symbolic evidence-source ledger")
    line_metric, scale_lang, det_root, F_neutral, option_label, recovery_bad, missing = sp.symbols(
        "line_metric scale_lang det_root F_neutral option_label recovery_bad missing"
    )
    P_insertion, P_active_O, P_residual_kill, P_parent = sp.symbols(
        "P_insertion P_active_O P_residual_kill P_parent"
    )
    L_sources = sp.simplify(line_metric + scale_lang + det_root + F_neutral + option_label + recovery_bad + missing)
    L_downstream = sp.simplify(P_insertion + P_active_O + P_residual_kill + P_parent)
    print(f"Evidence-source load: L_sources = {L_sources}")
    print(f"Downstream closed load: L_downstream_closed = {L_downstream}")
    with out.derived_results():
        out.line(
            "B_s evidence-source symbolic ledger stated",
            StatusMark.PASS,
            f"L_sources={L_sources}; L_downstream_closed={L_downstream}",
        )


def case_2(out: ScriptOutput, sources: List[EvidenceSource]):
    header("Case 2: Evidence source classes")
    for item in sources:
        subheader(item.name)
        print(f"Source: {item.source}")
        print(f"Possible signal: {item.possible_signal}")
        with out.governance_assessments():
            out.line(
                item.name,
                mark(item.status),
                f"{item.status}: admissible if {item.admissible_if}; blocked if {item.blocked_if}; consequence: {item.consequence}",
            )


def case_3(out: ScriptOutput, rules: List[EvidenceRule]):
    header("Case 3: Evidence admissibility rules")
    for item in rules:
        subheader(item.name)
        print(f"Rule: {item.rule}")
        print(f"Reason: {item.reason}")
        with out.governance_assessments():
            out.line(item.name, StatusMark.OBLIGATION, f"POLICY_RULE: {item.rule} Reason: {item.reason}")


def case_4(out: ScriptOutput):
    header("Case 4: Invalid evidence-source upgrades")
    shortcuts = [
        ("X1: source class as evidence found", "treat an evidence-source inventory as actual located evidence", "source inventory does not supply evidence content"),
        ("X2: ambiguous evidence as convention", "use F_zeta or option labels to choose a convention", "ambiguous evidence can only keep branches open"),
        ("X3: recovery as evidence", "use recovery or parent fit as notation evidence", "recovery is audit, not convention source"),
        ("X4: evidence source as declaration", "treat admissible evidence class as filled declaration", "declaration requires a separate record or explicit choice"),
        ("X5: evidence source as insertion", "open B_s/F_zeta insertion from notation evidence", "downstream gates remain closed"),
    ]
    for name, shortcut, reason in shortcuts:
        subheader(name)
        print(f"Shortcut: {shortcut}")
        with out.counterexamples():
            out.line(name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {reason}")


def case_5(out: ScriptOutput):
    header("Case 5: Local conclusions")
    with out.governance_assessments():
        out.line(
            "B_s evidence-source inventory complete",
            StatusMark.PASS,
            "line-element and scale-factor usages are admissible evidence classes; recovery and F_zeta-only usage cannot choose convention",
        )
        out.line(
            "B_s convention remains unchosen",
            StatusMark.DEFER,
            "next work should either search actual files for B_s notation usage or make an explicit theory choice",
        )
        out.line(
            "downstream gates remain closed",
            StatusMark.DEFER,
            "evidence-source inventory is not declaration, adoption, theorem proof, insertion, active O, residual control, or parent readiness",
        )


def record_marker(ns, marker_id: str, symbol_name: str):
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[],
        output=sp.Symbol(symbol_name),
        method="inventory marker; no physical derivation",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
        scope="Group 38 B_s notation evidence source inventory",
    )


def record_claim(ns, claim_id: str, marker_id: str, status, statement: str):
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


def record_obligation(ns, obligation_id: str, marker_id: str, statement: str, status=ObligationStatus.OPEN):
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


def record_governance(ns, sources: List[EvidenceSource], rules: List[EvidenceRule]):
    record_marker(ns, MARKER_ID, "g38_Bs_notation_evidence_source_inventory")
    for idx, item in enumerate(sources, 1):
        status = GovernanceStatus.POLICY_RULE if item.status in {"REJECTED_SELECTOR", "MISSING"} else GovernanceStatus.CANDIDATE_ROUTE
        record_claim(
            ns,
            f"g38_evsrc_s{idx}",
            MARKER_ID,
            status,
            f"{item.name}: {item.source}. Signal: {item.possible_signal}. Admissible if {item.admissible_if}. Blocked if {item.blocked_if}. Consequence: {item.consequence}.",
        )
    for idx, item in enumerate(rules, 1):
        record_claim(
            ns,
            f"g38_evsrc_r{idx}",
            MARKER_ID,
            GovernanceStatus.POLICY_RULE,
            f"{item.name}: {item.rule} Reason: {item.reason}.",
        )
    record_obligation(
        ns,
        "g38_evsrc_find_actual_usage",
        MARKER_ID,
        "Find actual B_s/B/F_zeta notation usage or make an explicit theory choice before completing Group 38 declarations.",
    )
    record_obligation(
        ns,
        "g38_evsrc_keep_deferred",
        MARKER_ID,
        "Keep B_s convention deferred until admissible notation-origin evidence or explicit theory choice is supplied.",
    )


def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    sources = build_sources()
    rules = build_rules()
    case_0(out)
    case_1(out)
    case_2(out, sources)
    case_3(out, rules)
    case_4(out)
    case_5(out)
    record_governance(ns, sources, rules)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
