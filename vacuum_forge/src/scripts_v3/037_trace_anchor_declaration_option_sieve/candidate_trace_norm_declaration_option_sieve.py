# Candidate Trace-Normalization Declaration Option Sieve
#
# Group:
#   37_trace_anchor_declaration_option_sieve
#
# Human title:
#   Trace-Normalization Declaration Option Sieve
#
# Script type:
#   OPTION SIEVE
#
# Purpose
# -------
# Classify possible declaration packages for P_trace_norm after Group 33 and Group 36.
# Surviving forms remain options only and do not become declarations or adopted postulates.
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
#   Sort the measuring cups. Do not pour.

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
        ("g36_status_summary", "036_conditional_trace_anchor_precondition_inventory__candidate_group_36_status_summary", "g36_status_summary", RecordKind.INVENTORY_MARKER),
        ("g36_pc_obl", "036_conditional_trace_anchor_precondition_inventory__candidate_trace_anchor_precondition_obligations", "g36_pc_obligations", RecordKind.INVENTORY_MARKER),
        ("g36_handoff_pc", "036_conditional_trace_anchor_precondition_inventory__candidate_trace_anchor_handoff_condition_ledger", "g36_handoff_pc", RecordKind.INVENTORY_MARKER),
        ("g36_safety_pc", "036_conditional_trace_anchor_precondition_inventory__candidate_trace_anchor_safety_precondition_ledger", "g36_safety_pc", RecordKind.INVENTORY_MARKER),
        ("g36_status_pc", "036_conditional_trace_anchor_precondition_inventory__candidate_trace_anchor_status_precondition_matrix", "g36_status_precond_matrix", RecordKind.INVENTORY_MARKER),
        ("g36_decl_pc", "036_conditional_trace_anchor_precondition_inventory__candidate_trace_anchor_declaration_precondition_ledger", "g36_decl_precond_ledger", RecordKind.INVENTORY_MARKER),
        ("g37_problem", "037_trace_anchor_declaration_option_sieve__candidate_trace_anchor_declaration_option_problem", "g37_option_problem", RecordKind.INVENTORY_MARKER),
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


SYMBOL_NAMES = ['scale_factor_log_option', 'metric_coefficient_log_option', 'per_dimension_option', 'linearized_only_option', 'ambiguous_Bs_option', 'ambiguous_zeta_option', 'recovery_selected_option', 'insertion_selected_option', 'P_insertion', 'P_active_O', 'P_residual_kill', 'P_parent']
ENTRIES = [{'name': 'N1: scale-factor volume-log option', 'subject': 'declare B_s as scale-factor language with log(B_s)=zeta/d', 'status': 'DECLARATION_READY', 'summary': 'coherent option if zeta is total volume-log trace and d is declared', 'allowed_if': 'B_s is explicitly scale-factor response, zeta is total volume-log trace, d is stated, and scope is exact or specified', 'blocked_if': 'chosen because Schwarzschild recovery, gamma, insertion, or parent fit works', 'consequence': 'may enter joint package sieve as a declaration-ready option, not as chosen'}, {'name': 'N2: metric-coefficient volume-log option', 'subject': 'declare B_s as metric-coefficient language with log(B_s)=2*zeta/d', 'status': 'DECLARATION_READY', 'summary': 'coherent option if B_s refers to metric coefficient rather than scale factor', 'allowed_if': 'metric-coefficient convention, total zeta trace, d, and scope are explicit', 'blocked_if': 'factor of two is hidden or selected from recovery', 'consequence': 'may enter joint package sieve as a declaration-ready option, not as chosen'}, {'name': 'N3: per-dimension zeta option', 'subject': 'declare zeta as already dimension-normalized', 'status': 'CANDIDATE_OPTION', 'summary': 'notation-dependent option that can be coherent if normalization is explicit', 'allowed_if': 'zeta_per_dim convention is declared before comparing forms', 'blocked_if': 'dimension factors are hidden by notation after the fact', 'consequence': 'may survive as notation option but should be marked notation-risk'}, {'name': 'N4: linearized-only trace option', 'subject': 'use first-order trace bookkeeping only', 'status': 'DIAGNOSTIC_ONLY', 'summary': 'safe only as linearized audit label', 'allowed_if': 'first-order scope is explicit and not promoted to exact determinant law', 'blocked_if': 'used as exact trace-normalization theorem', 'consequence': 'may support diagnostic audits only'}, {'name': 'N5: ambiguous convention option', 'subject': 'leave B_s or zeta convention unspecified', 'status': 'INCOMPLETE', 'summary': 'not declaration-ready', 'allowed_if': 'never for handoff use; may remain an open blank', 'blocked_if': 'used as if declaration-ready', 'consequence': 'blocks joint package declaration readiness'}, {'name': 'N6: recovery-selected option', 'subject': 'choose normalization from recovery, gamma, insertion, or parent fit', 'status': 'REJECTED_OPTION', 'summary': 'forbidden selector', 'allowed_if': 'never as declaration selector', 'blocked_if': 'recovery or downstream fit chooses normalization', 'consequence': 'rejected as shortcut, not a theorem about impossibility'}]
INVALIDS = [{'name': 'X1: hidden factor of two', 'shortcut': 'omit whether B_s is scale-factor or metric-coefficient language', 'status': 'FORBIDDEN_SHORTCUT', 'reason': 'factor-of-two ambiguity changes the declaration meaning', 'failure_mode': 'two different forms are silently conflated'}, {'name': 'X2: hidden dimension', 'shortcut': 'use zeta/d or per-dimension zeta without declaring d and convention', 'status': 'FORBIDDEN_SHORTCUT', 'reason': 'dimension factor can be hidden in notation', 'failure_mode': 'normalization is selected by symbols rather than declaration'}, {'name': 'X3: linearized as exact', 'shortcut': 'promote first-order trace bookkeeping to exact law', 'status': 'FORBIDDEN_SHORTCUT', 'reason': 'linearized compatibility is weaker than exact determinant structure', 'failure_mode': 'scope boundary collapses'}, {'name': 'X4: recovery-selected normalization', 'shortcut': 'choose normalization because recovery or parent fit works', 'status': 'FORBIDDEN_SHORTCUT', 'reason': 'recovery is audit, not construction rule', 'failure_mode': 'target-selected postulate enters as declaration'}]
OBLIGATIONS = [{'name': 'O1: preserve option status', 'obligation': 'carry surviving trace-normalization forms as options only', 'status': 'OPEN', 'blocks': 'selection drift', 'discipline': 'declaration-ready is not selected or adopted'}, {'name': 'O2: declare conventions before use', 'obligation': 'require B_s convention, zeta convention, dimension, and scope before future use', 'status': 'OPEN', 'blocks': 'hidden normalization', 'discipline': 'no convention may be inferred from recovery or insertion'}, {'name': 'O3: keep linearized scope fenced', 'obligation': 'keep linearized-only option from becoming exact law', 'status': 'OPEN', 'blocks': 'scope drift', 'discipline': 'first-order bookkeeping remains first-order'}, {'name': 'O4: downstream gates', 'obligation': 'keep insertion, active O, residual control, and parent closure closed', 'status': 'NOT_READY', 'blocks': 'downstream overreach', 'discipline': 'normalization option classification is not insertion'}]
CONCLUSIONS = [{'name': 'C1: normalization options classified', 'conclusion': 'scale-factor and metric-coefficient volume-log options are declaration-ready options; per-dimension and linearized options require fencing', 'status': 'PASS', 'meaning': 'trace-normalization option set can feed joint package sieve'}, {'name': 'C2: no normalization selected', 'conclusion': 'no trace-normalization option is selected, adopted, or derived', 'status': 'NOT_CHOSEN', 'meaning': 'current status remains compatible-if-declared only'}, {'name': 'C3: next', 'conclusion': 'safe-membership declaration option sieve should run next', 'status': 'OPEN', 'meaning': 'second Package B component option sieve follows'}]


def build_symbolic_loads():
    syms = {name: sp.Symbol(name) for name in SYMBOL_NAMES}
    option_load = sp.simplify(sum((syms[name] for name in SYMBOL_NAMES if not name.startswith("P_")), sp.Integer(0)))
    downstream = sp.simplify(syms.get("P_insertion", 0) + syms.get("P_active_O", 0) + syms.get("P_residual_kill", 0) + syms.get("P_parent", 0))
    total = sp.simplify(option_load + downstream)
    return syms, option_load, downstream, total


def case_0_problem() -> None:
    header("Case 0: Trace-Normalization Declaration Option Sieve problem")
    print("Question:\n")
    print("  " + 'Which trace-normalization declaration options are coherent enough to carry into a joint declaration package sieve?'.replace("\n", "\n  "))
    print("\nDiscipline:\n")
    for line in ['This script classifies trace-normalization declaration options.', 'It fills no declaration slot as theory state.', 'It selects no trace-normalization form.', 'It adopts no Package B component.', 'It keeps insertion, active O, residual control, and parent closure closed.']:
        print(f"  {line}")
    print("\nTiny goblin rule:")
    print(f"  Sort the measuring cups. Do not pour.")
    out_line("governance_assessments", "PASS", "Trace-Normalization Declaration Option Sieve opened", "inventory only; no declaration, status assignment, adoption, or insertion")


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
    header("Case 2: Trace-normalization declaration options")
    for item in ENTRIES:
        subheader(item["name"])
        print(f"Subject: {item['subject']}")
        out_line("governance_assessments", item["status"], item["name"], item.get("summary", ""))
        print(f"Allowed if: {item['allowed_if']}")
        print(f"Blocked if: {item['blocked_if']}")
        print(f"Consequence: {item['consequence']}")
    out_line("governance_assessments", "PASS", "Trace-normalization declaration options stated", f"{len(ENTRIES)} entries stated")


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
    out_line("governance_assessments", "PASS", "Trace-Normalization Declaration Option Sieve local conclusion stated", "local inventory complete; later reconciliation must compare actual batch results")


def final_interpretation() -> None:
    header("Final interpretation")
    print(
        "Trace-Normalization Declaration Option Sieve result:\n\n"
        "  Local inventory completed for Group 37 declaration-option sieve.\n"
        "  This script records options, blocks, shortcuts, and obligations only.\n"
        "  No declaration value is installed as theory state.\n"
        "  No Package B component status is assigned.\n"
        "  No trace-normalization or safe-membership form is selected, adopted, or derived.\n"
        "  Package B is not recommended for adoption.\n"
        "  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.\n\n"
        "Possible next script:\n"
        "  candidate_safe_membership_declaration_option_sieve.py\n\n"
        "Tiny goblin label:\n"
        "  Sort the measuring cups. Do not pour.\n"
    )
    out_line("governance_assessments", "PASS", "Trace-Normalization Declaration Option Sieve complete", "run next script in order.txt; no adoption and downstream gates remain closed")


def record_inventory_marker(ns, option_load: sp.Basic, downstream: sp.Basic, total: sp.Basic) -> None:
    ns.record_derivation(
        derivation_id="g37_norm_options",
        inputs=[option_load, downstream],
        output=total,
        method="Trace-Normalization Declaration Option Sieve inventory marker",
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
                obligation_id=f"g37_norm_ob_{ident}",
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
            route_id="g37_norm",
            script_id=SCRIPT_ID,
            name="Trace-Normalization Declaration Option Sieve",
            status=GovernanceStatus.CANDIDATE_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            required_obligations=[f"g37_norm_ob_{safe_ident(item['name'])}" for item in OBLIGATIONS],
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
                claim_id=f"g37_norm_en_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.POLICY_RULE,
                statement=(
                    f"{item['subject']} Status: {item['status']}. {item.get('summary', '')} "
                    f"Allowed if: {item['allowed_if']}. Blocked if: {item['blocked_if']}. "
                    f"Consequence: {item['consequence']}."
                ),
                derivation_ids=["g37_norm_options"],
                obligation_ids=[],
            )
        )
    for item in INVALIDS:
        ident = safe_ident(item["name"])
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g37_norm_x_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.POLICY_RULE,
                statement=f"Forbidden shortcut: {item['shortcut']}. Reason: {item['reason']}. Failure mode: {item['failure_mode']}.",
                derivation_ids=["g37_norm_options"],
                obligation_ids=[],
            )
        )


def main() -> None:
    header("Candidate Trace-Normalization Declaration Option Sieve")
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
