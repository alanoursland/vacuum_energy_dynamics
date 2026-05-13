# Candidate Trace Anchor Declaration Option Problem
#
# Group:
#   37_trace_anchor_declaration_option_sieve
#
# Human title:
#   Trace Anchor Declaration Option Problem
#
# Script type:
#   OPTION SIEVE OPENER
#
# Purpose
# -------
# Open Group 37 as a declaration-option sieve after Group 36 made declaration, status, safety, and handoff locks visible.
# The group prepares possible ways to fill trace-anchor declaration blanks without filling them as theory state.
#
# This script is speculative-batch safe: it records only local inventory output.
# The later reconciliation script must compare actual archive results before any
# group close.
#
# It fills no declaration slot.
# It assigns no Package B component status as theory state.
# It selects no trace-normalization form.
# It selects no safe-membership form.
# It adopts no Package B component.
# It recommends no Package B adoption.
# It derives no coefficient law and no insertion.
# It keeps active O, residual control, and parent closure closed.
#
# Tiny goblin rule:
#   Lay out the blank forms. Do not sign them.

from pathlib import Path
import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    RecordKind,
    RouteRecord,
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


def safe_ident(name: str) -> str:
    raw = name.split(":", 1)[0].lower()
    return "".join(ch if ch.isalnum() else "_" for ch in raw).strip("_")


def status_mark(status: str) -> StatusMark:
    return {
        "ADOPTION_REQUIRES_DECISION": StatusMark.DEFER,
        "AUDIT_READY": StatusMark.INFO,
        "BLOCKED_IF_BLANK": StatusMark.DEFER,
        "CANDIDATE_OPTION": StatusMark.INFO,
        "COHERENT_OPTION": StatusMark.INFO,
        "COMPATIBLE_IF_DECLARED": StatusMark.INFO,
        "CONDITIONAL": StatusMark.DEFER,
        "DECLARATION_OPTION": StatusMark.INFO,
        "DECLARATION_READY": StatusMark.INFO,
        "DEFERRED": StatusMark.DEFER,
        "DIAGNOSTIC_ONLY": StatusMark.INFO,
        "FAIL": StatusMark.FAIL,
        "FORBIDDEN_SHORTCUT": StatusMark.FAIL,
        "HIGH_RISK": StatusMark.WARN,
        "INCOMPLETE": StatusMark.DEFER,
        "MIXED_STATUS_VISIBLE": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_ASSIGNED": StatusMark.DEFER,
        "NOT_CHOSEN": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "PASS": StatusMark.PASS,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "RECONCILE": StatusMark.OBLIGATION,
        "REJECTED_OPTION": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "STATUS_REQUIRED": StatusMark.OBLIGATION,
        "THEOREM_TARGET": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def out_line(section: str, status: str, title: str, detail: str = "") -> None:
    mark = status_mark(status).value
    print(f"[{section}]")
    if detail:
        print(f"{mark} {title} -- {status}\n{detail}")
    else:
        print(f"{mark} {title} -- {status}")


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    dependencies = [
        ("g36_summary", "36_conditional_trace_anchor_precondition_inventory__candidate_group_36_status_summary", "g36_status_summary", RecordKind.INVENTORY_MARKER),
        ("g36_pc_obl", "36_conditional_trace_anchor_precondition_inventory__candidate_trace_anchor_precondition_obligations", "g36_pc_obligations", RecordKind.INVENTORY_MARKER),
        ("g36_handoff_pc", "36_conditional_trace_anchor_precondition_inventory__candidate_trace_anchor_handoff_condition_ledger", "g36_handoff_pc", RecordKind.INVENTORY_MARKER),
        ("g36_safety_pc", "36_conditional_trace_anchor_precondition_inventory__candidate_trace_anchor_safety_precondition_ledger", "g36_safety_pc", RecordKind.INVENTORY_MARKER),
        ("g36_status_pc", "36_conditional_trace_anchor_precondition_inventory__candidate_trace_anchor_status_precondition_matrix", "g36_status_precond_matrix", RecordKind.INVENTORY_MARKER),
        ("g36_decl_pc", "36_conditional_trace_anchor_precondition_inventory__candidate_trace_anchor_declaration_precondition_ledger", "g36_decl_precond_ledger", RecordKind.INVENTORY_MARKER),
    ]
    for dependency_id, upstream_script_id, upstream_derivation_id, record_kind in dependencies:
        ns.declare_dependency(
            dependency_id=dependency_id,
            upstream_script_id=upstream_script_id,
            upstream_derivation_id=upstream_derivation_id,
            expected_record_kind=record_kind,
        )
    return archive, ns, invalidated


def ensure_archive_write_dirs(ns) -> None:
    for attr in (
        "routes_path",
        "branch_decisions_path",
        "claims_path",
        "obligations_path",
        "derivations_path",
        "governance_path",
    ):
        path_obj = getattr(ns, attr, None)
        if path_obj is not None:
            path_obj.mkdir(parents=True, exist_ok=True)


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


SYMBOL_NAMES = ['trace_norm_option', 'membership_option', 'joint_package_option', 'diagnostic_option', 'incomplete_option', 'rejected_option', 'declaration_record', 'adoption_record', 'theorem_route', 'P_insertion', 'P_active_O', 'P_residual_kill', 'P_parent']
ENTRIES = [{'name': 'P1: trace-normalization option class', 'subject': 'candidate declarations for how B_s reads zeta', 'status': 'DECLARATION_OPTION', 'summary': 'trace-normalization options may be compared but not installed', 'allowed_if': 'B_s convention, zeta convention, dimension, and scope are explicit', 'blocked_if': 'chosen from recovery, insertion convenience, parent fit, or source repair', 'consequence': 'trace-normalization option sieve should run next'}, {'name': 'P2: safe-membership option class', 'subject': 'candidate declarations for zeta_Bs -> T_zeta', 'status': 'DECLARATION_OPTION', 'summary': 'safe-membership options may be compared but not installed', 'allowed_if': 'object, sector, domain/codomain, criterion, role purity, and scope are explicit', 'blocked_if': 'membership implies incidence, residual kill, active O, insertion, source theorem, or parent readiness', 'consequence': 'safe-membership option sieve should run after normalization options'}, {'name': 'P3: joint package option class', 'subject': 'joint declaration packages combining both Package B nodes', 'status': 'DECLARATION_OPTION', 'summary': 'joint packages require node separation and status visibility', 'allowed_if': 'component options are independently visible and mixed status is carried if needed', 'blocked_if': 'one node silently licenses the other', 'consequence': 'joint package sieve should run after component option sieves'}, {'name': 'P4: diagnostic-only option class', 'subject': 'inert diagnostic labels for trace-anchor bookkeeping', 'status': 'DIAGNOSTIC_ONLY', 'summary': 'diagnostic options are safe only if inert', 'allowed_if': 'labels do not alter equations or license downstream work', 'blocked_if': 'diagnostic label becomes active projector, insertion handle, or parent input', 'consequence': 'diagnostic option remains audit-only'}, {'name': 'P5: adoption and theorem routes', 'subject': 'future use routes after option classification', 'status': 'DEFERRED', 'summary': 'future declaration/adoption/theorem routes remain separate', 'allowed_if': 'separate explicit records or proof scripts are opened later', 'blocked_if': 'option classification is treated as choice or proof', 'consequence': 'Group 37 is a sieve, not a decision'}]
INVALIDS = [{'name': 'X1: option space as declaration', 'shortcut': 'treat option inventory as filled declaration record', 'status': 'FORBIDDEN_SHORTCUT', 'reason': 'option space names possible choices; it does not choose', 'failure_mode': 'blank declarations become hidden declarations'}, {'name': 'X2: option survival as adoption', 'shortcut': 'treat surviving declaration options as adopted Package B components', 'status': 'FORBIDDEN_SHORTCUT', 'reason': 'adoption requires a separate explicit decision', 'failure_mode': 'sieve becomes theory choice'}, {'name': 'X3: option survival as theorem', 'shortcut': 'treat option coherence as proof of trace normalization or safe membership', 'status': 'FORBIDDEN_SHORTCUT', 'reason': 'coherence is weaker than derivation', 'failure_mode': 'theorem burden disappears by classification'}, {'name': 'X4: option space as insertion', 'shortcut': 'use declaration-option clarity as B_s/F_zeta insertion', 'status': 'FORBIDDEN_SHORTCUT', 'reason': 'insertion remains downstream and not ready', 'failure_mode': 'precondition clarity opens metric gate'}]
OBLIGATIONS = [{'name': 'O1: audit trace-normalization options', 'obligation': 'classify trace-normalization declaration options without installing one', 'status': 'OPEN', 'blocks': 'hidden trace-normalization declaration', 'discipline': 'options remain options until a separate declaration record'}, {'name': 'O2: audit safe-membership options', 'obligation': 'classify safe-membership declaration options without installing one', 'status': 'OPEN', 'blocks': 'hidden membership declaration', 'discipline': 'membership options remain candidate declarations only'}, {'name': 'O3: preserve route boundary', 'obligation': 'separate option sieve from declaration, adoption, theorem, insertion, and parent routes', 'status': 'OPEN', 'blocks': 'route drift', 'discipline': 'Group 37 stays a sieve'}, {'name': 'O4: downstream gates', 'obligation': 'keep insertion, active O, residual control, and parent closure closed', 'status': 'NOT_READY', 'blocks': 'downstream overreach', 'discipline': 'option sieve is not downstream readiness'}]
CONCLUSIONS = [{'name': 'C1: group opened', 'conclusion': 'Group 37 is opened as a trace-anchor declaration-option sieve', 'status': 'PASS', 'meaning': 'candidate declaration options may now be inventoried'}, {'name': 'C2: no choices made', 'conclusion': 'no declaration value, status, adoption, theorem, or insertion is supplied', 'status': 'NOT_CHOSEN', 'meaning': 'current Package B status remains compatible-if-declared only'}, {'name': 'C3: next', 'conclusion': 'trace-normalization declaration option sieve should run next', 'status': 'OPEN', 'meaning': 'first component option sieve follows'}]


def build_symbolic_loads():
    syms = {name: sp.Symbol(name) for name in SYMBOL_NAMES}
    option_load = sp.simplify(sum((syms[name] for name in SYMBOL_NAMES if not name.startswith("P_")), sp.Integer(0)))
    downstream = sp.simplify(syms.get("P_insertion", 0) + syms.get("P_active_O", 0) + syms.get("P_residual_kill", 0) + syms.get("P_parent", 0))
    total = sp.simplify(option_load + downstream)
    return syms, option_load, downstream, total


def case_0_problem() -> None:
    header("Case 0: Trace Anchor Declaration Option Problem problem")
    print("Question:\n")
    print("  " + 'What declaration-option space should be audited before any explicit trace-anchor declaration record, theorem route, adoption decision, insertion-precondition route, or parent route?'.replace("\n", "\n  "))
    print("\nDiscipline:\n")
    for line in ['This script opens the declaration-option sieve.', 'It prepares option classes only.', 'It fills no declaration slot.', 'It assigns no component status and adopts no Package B component.', 'It keeps insertion, active O, residual control, and parent closure closed.']:
        print(f"  {line}")
    print("\nTiny goblin rule:")
    print(f"  Lay out the blank forms. Do not sign them.")
    out_line("governance_assessments", "PASS", "Trace Anchor Declaration Option Problem opened", "inventory only; no declaration, status assignment, adoption, or insertion")


def case_1_symbolic() -> tuple[dict[str, sp.Symbol], sp.Basic, sp.Basic, sp.Basic]:
    header("Case 1: Symbolic ledger")
    syms, option_load, downstream, total = build_symbolic_loads()
    print("Symbols:")
    for name in SYMBOL_NAMES:
        print(f"  {name} = {syms[name]}")
    print()
    print(f"Option/precondition load:\n  L_options = {option_load}")
    print(f"Downstream closed load:\n  L_downstream_closed = {downstream}")
    print(f"Total local gap:\n  L_local_gap = {total}")
    out_line("derived_results", "PASS", "symbolic loads stated", f"L_options={option_load}; L_downstream_closed={downstream}")
    return syms, option_load, downstream, total


def case_2_entries() -> None:
    header("Case 2: Declaration-option problem classes")
    for item in ENTRIES:
        subheader(item["name"])
        print(f"Subject: {item['subject']}")
        out_line("governance_assessments", item["status"], item["name"], item.get("summary", ""))
        print(f"Allowed if: {item['allowed_if']}")
        print(f"Blocked if: {item['blocked_if']}")
        print(f"Consequence: {item['consequence']}")
    out_line("governance_assessments", "PASS", "Declaration-option problem classes stated", f"{len(ENTRIES)} entries stated")


def case_3_invalids() -> None:
    header("Case 3: Invalid upgrades and shortcuts")
    for item in INVALIDS:
        subheader(item["name"])
        print(f"Shortcut: {item['shortcut']}")
        out_line("counterexamples", item["status"], item["name"], "")
        print(f"Reason: {item['reason']}")
        print(f"Failure mode: {item['failure_mode']}")
    out_line("counterexamples", "FAIL", "invalid upgrades rejected", f"{len(INVALIDS)} shortcuts rejected")


def case_4_obligations() -> None:
    header("Case 4: Open obligations")
    for item in OBLIGATIONS:
        subheader(item["name"])
        print(f"Obligation: {item['obligation']}")
        out_line("unresolved_obligations", item["status"], item["name"], "")
        print(f"Blocks: {item['blocks']}")
        print(f"Discipline: {item['discipline']}")
    out_line("unresolved_obligations", "PASS", "obligations stated", f"{len(OBLIGATIONS)} obligations stated")


def case_5_conclusions() -> None:
    header("Case 5: Local conclusions")
    for item in CONCLUSIONS:
        subheader(item["name"])
        print(f"Conclusion: {item['conclusion']}")
        out_line("governance_assessments", item["status"], item["name"], "")
        print(f"Meaning: {item['meaning']}")
    out_line("governance_assessments", "PASS", "Trace Anchor Declaration Option Problem local conclusion stated", "local inventory complete; later reconciliation must compare actual batch results")


def final_interpretation() -> None:
    header("Final interpretation")
    print(
        "Trace Anchor Declaration Option Problem result:\n\n"
        "  Local inventory completed for Group 37 declaration-option sieve.\n"
        "  This script records options, blocks, shortcuts, and obligations only.\n"
        "  No declaration value is installed as theory state.\n"
        "  No Package B component status is assigned.\n"
        "  No trace-normalization or safe-membership form is selected, adopted, or derived.\n"
        "  Package B is not recommended for adoption.\n"
        "  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.\n\n"
        "Possible next script:\n"
        "  candidate_trace_norm_declaration_option_sieve.py\n\n"
        "Tiny goblin label:\n"
        "  Lay out the blank forms. Do not sign them.\n"
    )
    out_line("governance_assessments", "PASS", "Trace Anchor Declaration Option Problem complete", "run next script in order.txt; no adoption and downstream gates remain closed")


def record_inventory_marker(ns, option_load: sp.Basic, downstream: sp.Basic, total: sp.Basic) -> None:
    ns.record_derivation(
        derivation_id="g37_option_problem",
        inputs=[option_load, downstream],
        output=total,
        method="Trace Anchor Declaration Option Problem inventory marker",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="group37_inventory_marker",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    for item in OBLIGATIONS:
        ident = safe_ident(item["name"])
        status = ObligationStatus.DEFERRED if item["status"] == "NOT_READY" else ObligationStatus.OPEN
        ns.record_obligation(
            ProofObligationRecord(
                obligation_id=f"g37_prob_ob_{ident}",
                script_id=SCRIPT_ID,
                title=item["name"],
                status=status,
                required_by=[SCRIPT_ID],
                description=f"{item['obligation']} Blocks: {item['blocks']} Discipline: {item['discipline']}",
            )
        )


def record_governance(ns) -> None:
    ns.record_route(
        RouteRecord(
            route_id="g37_prob",
            script_id=SCRIPT_ID,
            name="Trace Anchor Declaration Option Problem",
            status=GovernanceStatus.CANDIDATE_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            required_obligations=[f"g37_prob_ob_{safe_ident(item['name'])}" for item in OBLIGATIONS],
            activation_conditions=[
                "speculative batch local inventory only",
                "no declaration values installed",
                "no component status assigned",
                "no Package B component adopted",
                "downstream gates closed",
            ],
        )
    )
    for item in ENTRIES:
        ident = safe_ident(item["name"])
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g37_prob_en_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.POLICY_RULE,
                statement=(
                    f"{item['subject']} Status: {item['status']}. {item.get('summary', '')} "
                    f"Allowed if: {item['allowed_if']}. Blocked if: {item['blocked_if']}. "
                    f"Consequence: {item['consequence']}."
                ),
                derivation_ids=["g37_option_problem"],
                obligation_ids=[],
            )
        )
    for item in INVALIDS:
        ident = safe_ident(item["name"])
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g37_prob_x_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.POLICY_RULE,
                statement=f"Forbidden shortcut: {item['shortcut']}. Reason: {item['reason']}. Failure mode: {item['failure_mode']}.",
                derivation_ids=["g37_option_problem"],
                obligation_ids=[],
            )
        )


def main() -> None:
    header("Candidate Trace Anchor Declaration Option Problem")
    archive, ns, invalidated = prepare_archive()
    ensure_archive_write_dirs(ns)
    print_archive_status(ns, invalidated)
    case_0_problem()
    _, option_load, downstream, total = case_1_symbolic()
    case_2_entries()
    case_3_invalids()
    case_4_obligations()
    case_5_conclusions()
    final_interpretation()
    record_inventory_marker(ns, option_load, downstream, total)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
