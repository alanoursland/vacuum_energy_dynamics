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

# Group:
#   38_trace_anchor_explicit_declaration_record
# Script type:
#   REPAIR / NOTATION-SPLIT DECLARATION SURFACE
#
# Purpose:
#   Record a safe notation split after the B_s notation conflict repair.
#   This names distinct metric-coefficient and scale-factor objects, but it
#   does not choose either as the installed Package B declaration.

SCRIPT_LABEL = "Candidate B_s Notation Split Declaration"
MARKER_ID = "g38_bs_split_decl"

DEPENDENCIES = [
    ("g38_bs_repair", "038_trace_anchor_explicit_declaration_record__candidate_Bs_notation_conflict_repair", "g38_bs_conflict_repair"),
    ("g38_bs_usage", "038_trace_anchor_explicit_declaration_record__candidate_Bs_actual_notation_usage_collector", "g38_bs_usage"),
    ("g38_bs_evsrc", "038_trace_anchor_explicit_declaration_record__candidate_Bs_notation_evidence_source_inventory", "g38_bs_evsrc"),
    ("g38_recon", "038_trace_anchor_explicit_declaration_record__candidate_trace_anchor_declaration_batch_reconciliation", "g38_recon"),
]

# Configuration:
# The split can be recorded as a notation repair without choosing the active
# declaration branch. Leave ACTIVE_DECLARATION_BRANCH=None unless the theory
# owner explicitly chooses a branch in this script.
#
# Allowed values:
#   None
#   "metric_coefficient"
#   "scale_factor"
ACTIVE_DECLARATION_BRANCH = None


@dataclass(frozen=True)
class SplitObject:
    name: str
    symbol: str
    role: str
    candidate_normalization: str
    allowed_use: str
    forbidden_use: str
    status: str
    consequence: str


@dataclass(frozen=True)
class Rule:
    name: str
    rule: str
    reason: str


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
        "SPLIT_RECORDED": StatusMark.PASS,
        "DECLARATION_READY": StatusMark.INFO,
        "DECLARATION_DEFERRED": StatusMark.DEFER,
        "CHOSEN": StatusMark.PASS,
        "NOT_CHOSEN": StatusMark.DEFER,
        "CONFLICT": StatusMark.FAIL,
        "REJECTED": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
    }.get(status, StatusMark.INFO)


def record_marker(ns, marker_id: str, symbol_name: str):
    ns.record_derivation(
        derivation_id=marker_id,
        inputs=[],
        output=sp.Symbol(symbol_name),
        method="notation split inventory marker; no physical derivation",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
        scope="Group 38 B_s notation split declaration surface",
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


def record_obligation(ns, obligation_id: str, marker_id: str, description: str, status=ObligationStatus.OPEN):
    ns.record_obligation(
        ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=obligation_id,
            status=status,
            required_by=[SCRIPT_ID],
            description=description,
        )
    )


def build_split_objects() -> List[SplitObject]:
    return [
        SplitObject(
            name="S1: metric-coefficient object",
            symbol="B_s_metric",
            role="metric-coefficient spatial response notation",
            candidate_normalization="log(B_s_metric)=2*zeta/d",
            allowed_use="may carry inherited B-like metric-coefficient usage as an option",
            forbidden_use="must not be conflated with scale-factor or volume-root notation",
            status="DECLARATION_READY",
            consequence="eligible named branch for later explicit declaration choice",
        ),
        SplitObject(
            name="S2: scale-factor object",
            symbol="b_s_scale",
            role="scale-factor or per-direction spatial response notation",
            candidate_normalization="log(b_s_scale)=zeta/d",
            allowed_use="may carry scale-factor, determinant-root, or per-direction volume-root usage as an option",
            forbidden_use="must not be conflated with metric-coefficient B notation",
            status="DECLARATION_READY",
            consequence="eligible named branch for later explicit declaration choice",
        ),
        SplitObject(
            name="S3: neutral functional placeholder",
            symbol="F_zeta",
            role="neutral response-functional placeholder",
            candidate_normalization="none installed",
            allowed_use="may remain neutral until a named metric or scale object is explicitly selected",
            forbidden_use="must not hide the factor-of-two choice or install zeta/d or 2*zeta/d by implication",
            status="DECLARATION_DEFERRED",
            consequence="safe deferral object, not a completed declaration",
        ),
    ]


def build_rules() -> List[Rule]:
    return [
        Rule(
            name="R1: split is not choice",
            rule="Naming B_s_metric and b_s_scale repairs notation conflict but does not select either as the active declaration.",
            reason="The conflict repair recommended split or explicit choice; split alone is weaker than choice.",
        ),
        Rule(
            name="R2: explicit branch choice remains separate",
            rule="A later declaration record must state if metric_coefficient or scale_factor is the active Package B branch.",
            reason="Group 38 batch was choice-tolerant and remains deferred unless a branch is explicitly selected.",
        ),
        Rule(
            name="R3: F_zeta remains neutral",
            rule="F_zeta cannot install a concrete normalization while pretending to stay convention-neutral.",
            reason="Neutral functional notation cannot erase the factor-of-two burden.",
        ),
        Rule(
            name="R4: downstream gates stay closed",
            rule="Notation split does not license B_s/F_zeta insertion, active O, residual control, or parent closure.",
            reason="Notation repair is not a field-equation theorem.",
        ),
    ]


def branch_result() -> str:
    if ACTIVE_DECLARATION_BRANCH is None:
        return "DECLARATION_DEFERRED"
    if ACTIVE_DECLARATION_BRANCH in {"metric_coefficient", "scale_factor"}:
        return "CHOSEN"
    return "CONFLICT"


def case_0(out):
    header(SCRIPT_LABEL)
    print("Question:\n")
    print("  Can the B_s notation conflict be repaired by splitting metric-coefficient")
    print("  and scale-factor meanings into distinct named objects before any explicit")
    print("  trace-anchor declaration is installed?")
    print("\nDiscipline:\n")
    print("  This script records a notation split surface only.")
    print("  It does not choose a B_s convention unless ACTIVE_DECLARATION_BRANCH is explicitly configured.")
    print("  It does not fill trace-normalization or safe-membership declarations by default.")
    print("  It adopts no Package B component and opens no downstream gate.")
    print("\nTiny goblin rule:\n  Make two labeled jars. Do not pour from either yet.")
    with out.governance_assessments():
        out.line("B_s notation split declaration opened", StatusMark.PASS, "split repair only; no default active declaration")


def case_1(out):
    header("Case 1: Symbolic notation split ledger")
    B_metric, B_scale, F_neutral, branch_choice, split_only = sp.symbols("B_metric B_scale F_neutral branch_choice split_only")
    P_insertion, P_active_O, P_residual_kill, P_parent = sp.symbols("P_insertion P_active_O P_residual_kill P_parent")
    L_split = sp.simplify(B_metric + B_scale + F_neutral + branch_choice + split_only)
    L_downstream = sp.simplify(P_insertion + P_active_O + P_residual_kill + P_parent)
    print(f"Notation split load: L_split = {L_split}")
    print(f"Downstream closed load: L_downstream_closed = {L_downstream}")
    with out.derived_results():
        out.line("B_s notation split symbolic ledger stated", StatusMark.PASS, f"L_split={L_split}; L_downstream_closed={L_downstream}")


def case_2(out, split_objects):
    header("Case 2: Split notation objects")
    for item in split_objects:
        subheader(item.name)
        print(f"Symbol: {item.symbol}")
        print(f"Role: {item.role}")
        print(f"Candidate normalization: {item.candidate_normalization}")
        print(f"Allowed use: {item.allowed_use}")
        print(f"Forbidden use: {item.forbidden_use}")
        print(f"Consequence: {item.consequence}")
        with out.governance_assessments():
            out.line(item.name, mark(item.status), f"{item.status}: {item.consequence}")


def case_3(out):
    header("Case 3: Active branch configuration")
    print(f"ACTIVE_DECLARATION_BRANCH = {ACTIVE_DECLARATION_BRANCH!r}")
    result = branch_result()
    if result == "CHOSEN":
        detail = f"explicit branch chosen: {ACTIVE_DECLARATION_BRANCH}; still declared candidate only, not adoption or theorem"
    elif result == "DECLARATION_DEFERRED":
        detail = "no active branch chosen; notation split repairs conflict but declaration remains deferred"
    else:
        detail = "invalid branch configuration; must be None, metric_coefficient, or scale_factor"
    with out.governance_assessments():
        out.line("active B_s declaration branch classified", mark(result), f"{result}: {detail}")


def case_4(out, rules):
    header("Case 4: Split governance rules")
    for item in rules:
        subheader(item.name)
        print(f"Rule: {item.rule}")
        print(f"Reason: {item.reason}")
        with out.governance_assessments():
            out.line(item.name, StatusMark.OBLIGATION, f"POLICY_RULE: {item.rule} Reason: {item.reason}")


def case_5(out):
    header("Case 5: Invalid notation-split upgrades")
    shortcuts = [
        ("X1: split as active declaration", "treat split notation as choosing metric or scale branch", "split repairs naming but does not select branch"),
        ("X2: split as theorem", "treat B_s_metric or b_s_scale as derived law", "notation is not proof"),
        ("X3: F_zeta as hidden branch", "use F_zeta to install either zeta/d or 2*zeta/d without branch choice", "F_zeta neutrality must remain honest"),
        ("X4: branch choice as adoption", "treat explicit branch choice as Package B adoption", "adoption requires separate decision"),
        ("X5: split as insertion", "treat notation repair as B_s/F_zeta insertion readiness", "downstream gates remain closed"),
    ]
    for name, shortcut, reason in shortcuts:
        subheader(name)
        print(f"Shortcut: {shortcut}")
        with out.counterexamples():
            out.line(name, StatusMark.FAIL, f"FORBIDDEN_SHORTCUT: {reason}")


def case_6(out):
    header("Case 6: Local conclusions")
    result = branch_result()
    with out.governance_assessments():
        out.line("B_s notation split recorded", StatusMark.PASS, "metric-coefficient and scale-factor meanings are separated into distinct named objects")
        if result == "CHOSEN":
            out.line("active branch explicitly configured", StatusMark.PASS, f"{ACTIVE_DECLARATION_BRANCH}; still not adoption, theorem, or insertion")
        elif result == "DECLARATION_DEFERRED":
            out.line("active branch remains deferred", StatusMark.DEFER, "write explicit branch-choice or declaration-completion script next")
        else:
            out.line("active branch conflict", StatusMark.FAIL, "invalid configuration requires repair")
        out.line("downstream gates remain closed", StatusMark.DEFER, "notation split is not insertion, active O, residual control, or parent readiness")


def record_governance(ns, split_objects, rules):
    record_marker(ns, MARKER_ID, "g38_Bs_notation_split_recorded")
    for idx, item in enumerate(split_objects, 1):
        record_claim(
            ns,
            f"g38_bs_split_obj_{idx}",
            MARKER_ID,
            GovernanceStatus.POLICY_RULE,
            f"{item.name}: {item.symbol}. Role: {item.role}. Candidate normalization: {item.candidate_normalization}. Status: {item.status}. {item.consequence}",
        )
    for idx, item in enumerate(rules, 1):
        record_claim(
            ns,
            f"g38_bs_split_rule_{idx}",
            MARKER_ID,
            GovernanceStatus.POLICY_RULE,
            f"{item.name}: {item.rule} Reason: {item.reason}",
        )
    result = branch_result()
    record_obligation(
        ns,
        "g38_bs_split_active_branch",
        MARKER_ID,
        "Choose an active branch explicitly in a later declaration-completion script unless ACTIVE_DECLARATION_BRANCH is deliberately configured here.",
        ObligationStatus.OPEN if result != "CHOSEN" else ObligationStatus.CLOSED,
    )
    record_obligation(
        ns,
        "g38_bs_split_downstream_closed",
        MARKER_ID,
        "Keep B_s/F_zeta insertion, active O, residual control, and parent closure closed after notation split.",
        ObligationStatus.DEFERRED,
    )


def main():
    archive, ns, invalidated = prepare_archive(DEPENDENCIES)
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    split_objects = build_split_objects()
    rules = build_rules()
    case_0(out)
    case_1(out)
    case_2(out, split_objects)
    case_3(out)
    case_4(out, rules)
    case_5(out)
    case_6(out)
    record_governance(ns, split_objects, rules)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
