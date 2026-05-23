# Candidate Trace Anchor Option Failure Controls
#
# Group:
#   37_trace_anchor_declaration_option_sieve
#
# Human title:
#   Trace Anchor Option Failure Controls
#
# Script type:
#   FAILURE CONTROL LEDGER
#
# Purpose
# -------
# State failure controls for the speculative declaration-option batch before reconciliation.
# This prevents option-classification results from drifting into declarations, adoptions, or theorem claims.
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
#   Count the cracked keys before the door goblin cheats.

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
        ("g36_summary", "036_conditional_trace_anchor_precondition_inventory__candidate_group_36_status_summary", "g36_status_summary", RecordKind.INVENTORY_MARKER),
        ("g36_pc_obl", "036_conditional_trace_anchor_precondition_inventory__candidate_trace_anchor_precondition_obligations", "g36_pc_obligations", RecordKind.INVENTORY_MARKER),
        ("g36_handoff_pc", "036_conditional_trace_anchor_precondition_inventory__candidate_trace_anchor_handoff_condition_ledger", "g36_handoff_pc", RecordKind.INVENTORY_MARKER),
        ("g36_safety_pc", "036_conditional_trace_anchor_precondition_inventory__candidate_trace_anchor_safety_precondition_ledger", "g36_safety_pc", RecordKind.INVENTORY_MARKER),
        ("g36_status_pc", "036_conditional_trace_anchor_precondition_inventory__candidate_trace_anchor_status_precondition_matrix", "g36_status_precond_matrix", RecordKind.INVENTORY_MARKER),
        ("g36_decl_pc", "036_conditional_trace_anchor_precondition_inventory__candidate_trace_anchor_declaration_precondition_ledger", "g36_decl_precond_ledger", RecordKind.INVENTORY_MARKER),
        ("g37_problem", "037_trace_anchor_declaration_option_sieve__candidate_trace_anchor_declaration_option_problem", "g37_option_problem", RecordKind.INVENTORY_MARKER),
        ("g37_norm", "037_trace_anchor_declaration_option_sieve__candidate_trace_norm_declaration_option_sieve", "g37_norm_options", RecordKind.INVENTORY_MARKER),
        ("g37_mem", "037_trace_anchor_declaration_option_sieve__candidate_safe_membership_declaration_option_sieve", "g37_membership_options", RecordKind.INVENTORY_MARKER),
        ("g37_joint", "037_trace_anchor_declaration_option_sieve__candidate_trace_anchor_joint_declaration_package_sieve", "g37_joint_packages", RecordKind.INVENTORY_MARKER),
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


SYMBOL_NAMES = ['declaration_drift', 'status_drift', 'adoption_drift', 'theorem_drift', 'diagnostic_drift', 'hidden_payload_drift', 'one_node_license', 'batch_mismatch', 'P_insertion', 'P_active_O', 'P_residual_kill', 'P_parent']
ENTRIES = [{'name': 'F1: declaration drift control', 'subject': 'declaration-ready must not become declared', 'status': 'POLICY_RULE', 'summary': 'option classification cannot fill declaration slots', 'allowed_if': 'separate declaration record installs values later', 'blocked_if': 'summary language says declarations are now filled', 'consequence': 'declaration-ready remains option status'}, {'name': 'F2: status drift control', 'subject': 'status modes must not be assigned by option scripts', 'status': 'POLICY_RULE', 'summary': 'status classification cannot change theory state', 'allowed_if': 'separate status assignment record changes component status later', 'blocked_if': 'declaration options are treated as selected, declared, adopted, or derived', 'consequence': 'current component status remains compatible-if-declared only'}, {'name': 'F3: adoption drift control', 'subject': 'declaration packages must not become adopted postulates', 'status': 'POLICY_RULE', 'summary': 'adoption requires explicit decision', 'allowed_if': 'separate adoption record names adopted components', 'blocked_if': 'coherent package is described as adopted Package B', 'consequence': 'Package B remains unadopted'}, {'name': 'F4: theorem drift control', 'subject': 'coherent packages must not become theorem proofs', 'status': 'POLICY_RULE', 'summary': 'proof requires derivation scripts', 'allowed_if': 'later theorem route after declarations attempts proof', 'blocked_if': 'coherence is reported as derivation', 'consequence': 'trace-normalization and safe-membership remain not derived'}, {'name': 'F5: downstream drift control', 'subject': 'option clarity must not become insertion or parent readiness', 'status': 'POLICY_RULE', 'summary': 'downstream gates remain closed', 'allowed_if': 'separate downstream theorem support exists later', 'blocked_if': 'package coherence opens B_s/F_zeta or parent route', 'consequence': 'insertion and parent closure remain not ready'}, {'name': 'F6: batch mismatch control', 'subject': 'speculative batch expectations must be reconciled against actual outputs', 'status': 'RECONCILE', 'summary': 'reconciliation script must compare outputs before group close', 'allowed_if': 'actual outputs match or exceptions are recorded', 'blocked_if': 'final group summary assumes expected result without checking batch', 'consequence': 'batch reconciliation should run next'}]
INVALIDS = [{'name': 'X1: coherent option as declaration', 'shortcut': 'write group summary as if coherent options were selected', 'status': 'FORBIDDEN_SHORTCUT', 'reason': 'option coherence is not selection', 'failure_mode': 'Group 37 accidentally fills declarations'}, {'name': 'X2: option as status assignment', 'shortcut': 'describe declaration-ready as assigned theory status', 'status': 'FORBIDDEN_SHORTCUT', 'reason': 'status assignment requires separate record', 'failure_mode': 'component status changes by prose'}, {'name': 'X3: coherent package as theorem', 'shortcut': 'describe a coherent package as derived trace-anchor law', 'status': 'FORBIDDEN_SHORTCUT', 'reason': 'sieve output is not proof', 'failure_mode': 'theorem burden disappears'}, {'name': 'X4: batch expectation as result', 'shortcut': 'close group from expected plan rather than actual script outputs', 'status': 'FORBIDDEN_SHORTCUT', 'reason': 'speculative batch must be reconciled', 'failure_mode': 'unexpected results are overwritten by plan'}]
OBLIGATIONS = [{'name': 'O1: preserve option boundaries', 'obligation': 'keep declaration-ready, diagnostic, mixed, incomplete, and rejected classes distinct', 'status': 'OPEN', 'blocks': 'classification drift', 'discipline': 'do not flatten all surviving options into one recommendation'}, {'name': 'O2: reconcile actual batch outputs', 'obligation': 'compare actual script markers and local conclusions before group close', 'status': 'OPEN', 'blocks': 'speculative-plan overclaim', 'discipline': 'summary must follow actual archive records'}, {'name': 'O3: keep adoption separate', 'obligation': 'do not adopt Package B or either component in failure controls', 'status': 'OPEN', 'blocks': 'accidental adoption', 'discipline': 'explicit decision remains separate'}, {'name': 'O4: downstream gates', 'obligation': 'keep insertion, active O, residual control, and parent closure closed', 'status': 'NOT_READY', 'blocks': 'downstream overreach', 'discipline': 'failure controls are not downstream readiness'}]
CONCLUSIONS = [{'name': 'C1: failure controls stated', 'conclusion': 'declaration, status, adoption, theorem, diagnostic, downstream, and batch-mismatch drift controls are visible', 'status': 'PASS', 'meaning': 'reconciliation can safely compare actual batch results'}, {'name': 'C2: no route changed', 'conclusion': 'no declaration, status assignment, adoption, theorem, or downstream route is opened', 'status': 'NOT_CHOSEN', 'meaning': 'failure controls do not change theory state'}, {'name': 'C3: next', 'conclusion': 'batch reconciliation should run next', 'status': 'OPEN', 'meaning': 'reconciliation will compare speculative batch results before any summary'}]


def build_symbolic_loads():
    syms = {name: sp.Symbol(name) for name in SYMBOL_NAMES}
    option_load = sp.simplify(sum((syms[name] for name in SYMBOL_NAMES if not name.startswith("P_")), sp.Integer(0)))
    downstream = sp.simplify(syms.get("P_insertion", 0) + syms.get("P_active_O", 0) + syms.get("P_residual_kill", 0) + syms.get("P_parent", 0))
    total = sp.simplify(option_load + downstream)
    return syms, option_load, downstream, total


def case_0_problem() -> None:
    header("Case 0: Trace Anchor Option Failure Controls problem")
    print("Question:\n")
    print("  " + 'Which failure controls must govern Group 37 declaration-option results before the batch reconciliation script compares actual outputs?'.replace("\n", "\n  "))
    print("\nDiscipline:\n")
    for line in ['This script records failure controls.', 'It chooses no declaration package.', 'It fills no declaration slot and assigns no component status.', 'It adopts no Package B component.', 'It keeps insertion, active O, residual control, and parent closure closed.']:
        print(f"  {line}")
    print("\nTiny goblin rule:")
    print(f"  Count the cracked keys before the door goblin cheats.")
    out_line("governance_assessments", "PASS", "Trace Anchor Option Failure Controls opened", "inventory only; no declaration, status assignment, adoption, or insertion")


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
    header("Case 2: Failure-control rules")
    for item in ENTRIES:
        subheader(item["name"])
        print(f"Subject: {item['subject']}")
        out_line("governance_assessments", item["status"], item["name"], item.get("summary", ""))
        print(f"Allowed if: {item['allowed_if']}")
        print(f"Blocked if: {item['blocked_if']}")
        print(f"Consequence: {item['consequence']}")
    out_line("governance_assessments", "PASS", "Failure-control rules stated", f"{len(ENTRIES)} entries stated")


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
    out_line("governance_assessments", "PASS", "Trace Anchor Option Failure Controls local conclusion stated", "local inventory complete; later reconciliation must compare actual batch results")


def final_interpretation() -> None:
    header("Final interpretation")
    print(
        "Trace Anchor Option Failure Controls result:\n\n"
        "  Local inventory completed for Group 37 declaration-option sieve.\n"
        "  This script records options, blocks, shortcuts, and obligations only.\n"
        "  No declaration value is installed as theory state.\n"
        "  No Package B component status is assigned.\n"
        "  No trace-normalization or safe-membership form is selected, adopted, or derived.\n"
        "  Package B is not recommended for adoption.\n"
        "  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.\n\n"
        "Possible next script:\n"
        "  candidate_trace_anchor_option_batch_reconciliation.py\n\n"
        "Tiny goblin label:\n"
        "  Count the cracked keys before the door goblin cheats.\n"
    )
    out_line("governance_assessments", "PASS", "Trace Anchor Option Failure Controls complete", "run next script in order.txt; no adoption and downstream gates remain closed")


def record_inventory_marker(ns, option_load: sp.Basic, downstream: sp.Basic, total: sp.Basic) -> None:
    ns.record_derivation(
        derivation_id="g37_fail_controls",
        inputs=[option_load, downstream],
        output=total,
        method="Trace Anchor Option Failure Controls inventory marker",
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
                obligation_id=f"g37_fail_ob_{ident}",
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
            route_id="g37_fail",
            script_id=SCRIPT_ID,
            name="Trace Anchor Option Failure Controls",
            status=GovernanceStatus.CANDIDATE_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            required_obligations=[f"g37_fail_ob_{safe_ident(item['name'])}" for item in OBLIGATIONS],
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
                claim_id=f"g37_fail_en_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.POLICY_RULE,
                statement=(
                    f"{item['subject']} Status: {item['status']}. {item.get('summary', '')} "
                    f"Allowed if: {item['allowed_if']}. Blocked if: {item['blocked_if']}. "
                    f"Consequence: {item['consequence']}."
                ),
                derivation_ids=["g37_fail_controls"],
                obligation_ids=[],
            )
        )
    for item in INVALIDS:
        ident = safe_ident(item["name"])
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g37_fail_x_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.POLICY_RULE,
                statement=f"Forbidden shortcut: {item['shortcut']}. Reason: {item['reason']}. Failure mode: {item['failure_mode']}.",
                derivation_ids=["g37_fail_controls"],
                obligation_ids=[],
            )
        )


def main() -> None:
    header("Candidate Trace Anchor Option Failure Controls")
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
