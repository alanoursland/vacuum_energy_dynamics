# Candidate Trace Anchor Joint Declaration Package Sieve
#
# Group:
#   37_trace_anchor_declaration_option_sieve
#
# Human title:
#   Trace Anchor Joint Declaration Package Sieve
#
# Script type:
#   PACKAGE SIEVE
#
# Purpose
# -------
# Combine trace-normalization and safe-membership declaration options into joint candidate packages.
# Classify joint packages without selecting, adopting, or declaring any package as theory state.
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
#   Bundle the papers. Do not file them.

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
        ("g37_problem", "37_trace_anchor_declaration_option_sieve__candidate_trace_anchor_declaration_option_problem", "g37_option_problem", RecordKind.INVENTORY_MARKER),
        ("g37_norm", "37_trace_anchor_declaration_option_sieve__candidate_trace_norm_declaration_option_sieve", "g37_norm_options", RecordKind.INVENTORY_MARKER),
        ("g37_mem", "37_trace_anchor_declaration_option_sieve__candidate_safe_membership_declaration_option_sieve", "g37_membership_options", RecordKind.INVENTORY_MARKER),
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


SYMBOL_NAMES = ['package_scale_typed', 'package_metric_typed', 'package_scale_rolepure', 'package_metric_rolepure', 'package_diag_only', 'package_mixed_scope', 'package_incomplete', 'package_rejected', 'one_node_license', 'P_insertion', 'P_active_O', 'P_residual_kill', 'P_parent']
ENTRIES = [{'name': 'J1: scale-factor plus typed-membership package', 'subject': 'log(B_s)=zeta/d plus typed zeta_Bs -> T_zeta membership', 'status': 'DECLARATION_READY', 'summary': 'coherent if scale-factor B_s convention and typed membership criterion are explicit', 'allowed_if': 'normalization and membership are separately declared and status modes are visible', 'blocked_if': 'scale-factor normalization chooses membership or membership supplies normalization', 'consequence': 'candidate declaration package for later explicit declaration record'}, {'name': 'J2: metric-coefficient plus typed-membership package', 'subject': 'log(B_s)=2*zeta/d plus typed zeta_Bs -> T_zeta membership', 'status': 'DECLARATION_READY', 'summary': 'coherent if metric-coefficient B_s convention and typed membership criterion are explicit', 'allowed_if': 'factor of two, total trace, d, and membership criterion are explicit', 'blocked_if': 'metric coefficient convention is hidden or chosen from recovery', 'consequence': 'candidate declaration package for later explicit declaration record'}, {'name': 'J3: scale-factor plus role-pure package', 'subject': 'scale-factor normalization with role-pure trace-payload membership', 'status': 'DECLARATION_READY', 'summary': 'coherent strong package if role-purity exclusions are explicit', 'allowed_if': 'exclusion zones and diagnostic/active scope are declared', 'blocked_if': 'role purity is reported as source theorem or residual control', 'consequence': 'candidate declaration package with stronger safety fencing'}, {'name': 'J4: metric-coefficient plus role-pure package', 'subject': 'metric-coefficient normalization with role-pure trace-payload membership', 'status': 'DECLARATION_READY', 'summary': 'coherent strong package if factor-of-two and role-purity fences are explicit', 'allowed_if': 'metric coefficient convention, trace dimension, and exclusion zones are declared', 'blocked_if': 'factors or exclusions are hidden', 'consequence': 'candidate declaration package with stronger safety fencing'}, {'name': 'J5: diagnostic-only package', 'subject': 'linearized/diagnostic normalization plus inert membership label', 'status': 'DIAGNOSTIC_ONLY', 'summary': 'safe for audit only, not active Package B use', 'allowed_if': 'all labels remain inert and first-order/diagnostic scope is explicit', 'blocked_if': 'diagnostic-only package is used for theorem/adoption/insertion', 'consequence': 'may support audit language only'}, {'name': 'J6: mixed-scope package', 'subject': 'exact normalization option paired with diagnostic-only membership or linearized normalization paired with active membership', 'status': 'MIXED_STATUS_VISIBLE', 'summary': 'possible only if mixed scope is visible', 'allowed_if': 'mixed status and scope mismatch are explicitly carried', 'blocked_if': 'reported as uniform declaration-ready package', 'consequence': 'deferred or conditional package, not recommendation'}, {'name': 'J7: incomplete package', 'subject': 'one or more declaration slots remain blank', 'status': 'INCOMPLETE', 'summary': 'not ready for explicit declaration record', 'allowed_if': 'carried as open blank only', 'blocked_if': 'used downstream as declaration-ready', 'consequence': 'blocks declaration route until completed'}, {'name': 'J8: hidden-load package', 'subject': 'package hides residual, source, divergence, insertion, or parent payload', 'status': 'REJECTED_OPTION', 'summary': 'rejected as current declaration package', 'allowed_if': 'never as Package B declaration package', 'blocked_if': 'any hidden payload enters component', 'consequence': 'must be rejected as shortcut'}]
INVALIDS = [{'name': 'X1: one-node licensing', 'shortcut': 'one component declaration licenses the other component', 'status': 'FORBIDDEN_SHORTCUT', 'reason': 'Package B has two separate candidate nodes', 'failure_mode': 'second hidden choice enters package'}, {'name': 'X2: diagnostic package as active', 'shortcut': 'diagnostic-only package is used for theorem, adoption, or insertion', 'status': 'FORBIDDEN_SHORTCUT', 'reason': 'diagnostic labels are inert only', 'failure_mode': 'audit package becomes active mechanism'}, {'name': 'X3: incomplete package as declaration-ready', 'shortcut': 'blank slots are ignored and package is treated as ready', 'status': 'FORBIDDEN_SHORTCUT', 'reason': 'Group 36 made blank slots mandatory', 'failure_mode': 'hidden declarations enter later record'}, {'name': 'X4: declaration-ready as adopted', 'shortcut': 'joint declaration-ready package is treated as adopted Package B', 'status': 'FORBIDDEN_SHORTCUT', 'reason': 'declaration readiness is weaker than adoption', 'failure_mode': 'package sieve becomes theory choice'}]
OBLIGATIONS = [{'name': 'O1: preserve package option status', 'obligation': 'carry coherent joint packages as declaration options only', 'status': 'OPEN', 'blocks': 'package selection drift', 'discipline': 'declaration-ready package is not the selected declaration'}, {'name': 'O2: preserve mixed status', 'obligation': 'carry mixed-scope or mixed-status packages visibly', 'status': 'OPEN', 'blocks': 'uniform-package overclaim', 'discipline': 'mixed package cannot be reported as uniformly ready'}, {'name': 'O3: reject hidden-load packages', 'obligation': 'reject packages that hide residual, source, divergence, insertion, or parent payload', 'status': 'OPEN', 'blocks': 'trace-anchor smuggling', 'discipline': 'Package B components are not cleanup reservoirs'}, {'name': 'O4: downstream gates', 'obligation': 'keep insertion, active O, residual control, and parent closure closed', 'status': 'NOT_READY', 'blocks': 'downstream overreach', 'discipline': 'joint package coherence is not insertion'}]
CONCLUSIONS = [{'name': 'C1: joint packages classified', 'conclusion': 'several coherent declaration-ready packages exist as options, with diagnostic/mixed/incomplete/rejected classes separated', 'status': 'PASS', 'meaning': 'later declaration record could choose among options, but no choice is made here'}, {'name': 'C2: no package selected', 'conclusion': 'no joint package is selected, adopted, recommended, or derived', 'status': 'NOT_CHOSEN', 'meaning': 'Package B remains compatible-if-declared only'}, {'name': 'C3: next', 'conclusion': 'declaration-option failure controls should run next', 'status': 'OPEN', 'meaning': 'shortcuts and expected-vs-actual reconciliation controls follow'}]


def build_symbolic_loads():
    syms = {name: sp.Symbol(name) for name in SYMBOL_NAMES}
    option_load = sp.simplify(sum((syms[name] for name in SYMBOL_NAMES if not name.startswith("P_")), sp.Integer(0)))
    downstream = sp.simplify(syms.get("P_insertion", 0) + syms.get("P_active_O", 0) + syms.get("P_residual_kill", 0) + syms.get("P_parent", 0))
    total = sp.simplify(option_load + downstream)
    return syms, option_load, downstream, total


def case_0_problem() -> None:
    header("Case 0: Trace Anchor Joint Declaration Package Sieve problem")
    print("Question:\n")
    print("  " + 'Which joint declaration packages are coherent enough to present to a later explicit declaration record?'.replace("\n", "\n  "))
    print("\nDiscipline:\n")
    for line in ['This script classifies joint declaration packages.', 'It chooses no package as the theory declaration.', 'It assigns no component status and adopts no Package B component.', 'It derives no trace normalization, safe membership, coefficient law, or insertion.', 'It keeps active O, residual control, and parent closure closed.']:
        print(f"  {line}")
    print("\nTiny goblin rule:")
    print(f"  Bundle the papers. Do not file them.")
    out_line("governance_assessments", "PASS", "Trace Anchor Joint Declaration Package Sieve opened", "inventory only; no declaration, status assignment, adoption, or insertion")


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
    header("Case 2: Joint declaration package options")
    for item in ENTRIES:
        subheader(item["name"])
        print(f"Subject: {item['subject']}")
        out_line("governance_assessments", item["status"], item["name"], item.get("summary", ""))
        print(f"Allowed if: {item['allowed_if']}")
        print(f"Blocked if: {item['blocked_if']}")
        print(f"Consequence: {item['consequence']}")
    out_line("governance_assessments", "PASS", "Joint declaration package options stated", f"{len(ENTRIES)} entries stated")


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
    out_line("governance_assessments", "PASS", "Trace Anchor Joint Declaration Package Sieve local conclusion stated", "local inventory complete; later reconciliation must compare actual batch results")


def final_interpretation() -> None:
    header("Final interpretation")
    print(
        "Trace Anchor Joint Declaration Package Sieve result:\n\n"
        "  Local inventory completed for Group 37 declaration-option sieve.\n"
        "  This script records options, blocks, shortcuts, and obligations only.\n"
        "  No declaration value is installed as theory state.\n"
        "  No Package B component status is assigned.\n"
        "  No trace-normalization or safe-membership form is selected, adopted, or derived.\n"
        "  Package B is not recommended for adoption.\n"
        "  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.\n\n"
        "Possible next script:\n"
        "  candidate_trace_anchor_option_failure_controls.py\n\n"
        "Tiny goblin label:\n"
        "  Bundle the papers. Do not file them.\n"
    )
    out_line("governance_assessments", "PASS", "Trace Anchor Joint Declaration Package Sieve complete", "run next script in order.txt; no adoption and downstream gates remain closed")


def record_inventory_marker(ns, option_load: sp.Basic, downstream: sp.Basic, total: sp.Basic) -> None:
    ns.record_derivation(
        derivation_id="g37_joint_packages",
        inputs=[option_load, downstream],
        output=total,
        method="Trace Anchor Joint Declaration Package Sieve inventory marker",
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
                obligation_id=f"g37_joint_ob_{ident}",
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
            route_id="g37_joint",
            script_id=SCRIPT_ID,
            name="Trace Anchor Joint Declaration Package Sieve",
            status=GovernanceStatus.CANDIDATE_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            required_obligations=[f"g37_joint_ob_{safe_ident(item['name'])}" for item in OBLIGATIONS],
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
                claim_id=f"g37_joint_en_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.POLICY_RULE,
                statement=(
                    f"{item['subject']} Status: {item['status']}. {item.get('summary', '')} "
                    f"Allowed if: {item['allowed_if']}. Blocked if: {item['blocked_if']}. "
                    f"Consequence: {item['consequence']}."
                ),
                derivation_ids=["g37_joint_packages"],
                obligation_ids=[],
            )
        )
    for item in INVALIDS:
        ident = safe_ident(item["name"])
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g37_joint_x_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.POLICY_RULE,
                statement=f"Forbidden shortcut: {item['shortcut']}. Reason: {item['reason']}. Failure mode: {item['failure_mode']}.",
                derivation_ids=["g37_joint_packages"],
                obligation_ids=[],
            )
        )


def main() -> None:
    header("Candidate Trace Anchor Joint Declaration Package Sieve")
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
