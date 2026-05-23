# Candidate Safe-Membership Declaration Option Sieve
#
# Group:
#   37_trace_anchor_declaration_option_sieve
#
# Human title:
#   Safe-Membership Declaration Option Sieve
#
# Script type:
#   OPTION SIEVE
#
# Purpose
# -------
# Classify possible declaration packages for P_safe_membership after Group 34 and Group 36.
# Surviving membership forms remain options only and do not become declarations or adopted postulates.
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
#   Sort the name tags. Do not pin them on.

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


SYMBOL_NAMES = ['typed_membership_option', 'role_pure_option', 'norm_compatible_option', 'diagnostic_label_option', 'residual_payload_option', 'source_payload_option', 'correction_payload_option', 'incidence_collapse_option', 'P_insertion', 'P_active_O', 'P_residual_kill', 'P_parent']
ENTRIES = [{'name': 'M1: typed trace-sector membership option', 'subject': 'declare zeta_Bs as typed member of T_zeta', 'status': 'DECLARATION_READY', 'summary': 'coherent option if object, sector, domain, codomain, and criterion are explicit', 'allowed_if': 'zeta_Bs object and T_zeta sector are defined with typed domain/codomain and membership criterion', 'blocked_if': 'membership implies incidence, residual kill, active O, or insertion', 'consequence': 'may enter joint package sieve as a declaration-ready option'}, {'name': 'M2: role-pure trace-payload option', 'subject': 'declare zeta_Bs payload as trace-sector only with explicit exclusion zones', 'status': 'DECLARATION_READY', 'summary': 'coherent option if role purity and exclusion zones are explicit', 'allowed_if': 'residual, ordinary-source, correction/divergence, boundary/support, and downstream payloads are excluded', 'blocked_if': 'membership becomes hidden-load pocket', 'consequence': 'may enter joint package sieve as strong membership option'}, {'name': 'M3: normalization-compatible membership option', 'subject': 'membership compatible with selected normalization notation but not chosen by it', 'status': 'CANDIDATE_OPTION', 'summary': 'coherence option, not a selector', 'allowed_if': 'normalization and membership remain separate nodes', 'blocked_if': 'normalization chooses membership or membership chooses normalization', 'consequence': 'may survive only with node-separation warning'}, {'name': 'M4: diagnostic-only membership label', 'subject': 'use zeta_Bs -> T_zeta as inert audit label only', 'status': 'DIAGNOSTIC_ONLY', 'summary': 'safe fallback if strictly inert', 'allowed_if': 'label does not alter equations, project sectors, or support insertion', 'blocked_if': 'diagnostic label becomes active membership or projector', 'consequence': 'audit-safe but not active Package B use'}, {'name': 'M5: residual-inclusive membership option', 'subject': 'membership carries residual or kappa/zeta non-entry burden', 'status': 'REJECTED_OPTION', 'summary': 'rejected as shortcut', 'allowed_if': 'never as declaration option', 'blocked_if': 'membership hides residual control', 'consequence': 'must remain separate residual theorem target'}, {'name': 'M6: source/correction-inclusive membership option', 'subject': 'membership carries ordinary source, correction, divergence, boundary, or support load', 'status': 'REJECTED_OPTION', 'summary': 'rejected as hidden-load shortcut', 'allowed_if': 'never as declaration option', 'blocked_if': 'membership becomes reservoir', 'consequence': 'source/divergence obligations remain separate'}]
INVALIDS = [{'name': 'X1: membership as incidence', 'shortcut': 'treat zeta_Bs -> T_zeta as trace/residual zero incidence', 'status': 'FORBIDDEN_SHORTCUT', 'reason': 'membership and incidence are separate nodes', 'failure_mode': 'no-overlap theorem burden disappears'}, {'name': 'X2: membership as residual control', 'shortcut': 'use safe membership as residual kill, residual inertness, or active O', 'status': 'FORBIDDEN_SHORTCUT', 'reason': 'membership is not residual-control theorem', 'failure_mode': 'residual gate is bypassed'}, {'name': 'X3: membership as source theorem', 'shortcut': 'treat role purity as source no-double-counting theorem', 'status': 'FORBIDDEN_SHORTCUT', 'reason': 'role purity is precondition, not full source theorem', 'failure_mode': 'ordinary source duplication risk is hidden'}, {'name': 'X4: diagnostic as active', 'shortcut': 'use diagnostic-only label to alter equations or support insertion', 'status': 'FORBIDDEN_SHORTCUT', 'reason': 'diagnostic labels are safe only if inert', 'failure_mode': 'audit tag becomes active projector'}]
OBLIGATIONS = [{'name': 'O1: preserve membership option status', 'obligation': 'carry surviving safe-membership forms as options only', 'status': 'OPEN', 'blocks': 'membership selection drift', 'discipline': 'declaration-ready is not selected or adopted'}, {'name': 'O2: require object and criterion', 'obligation': 'require zeta_Bs object, T_zeta sector, domain/codomain, and criterion before future use', 'status': 'OPEN', 'blocks': 'ill-posed membership', 'discipline': 'membership must be testable before theorem/adoption routes'}, {'name': 'O3: preserve exclusion zones', 'obligation': 'keep residual, source, correction, boundary/support, and downstream payloads excluded', 'status': 'OPEN', 'blocks': 'hidden-load pocket', 'discipline': 'membership remains role-pure trace-sector membership'}, {'name': 'O4: downstream gates', 'obligation': 'keep insertion, active O, residual control, and parent closure closed', 'status': 'NOT_READY', 'blocks': 'downstream overreach', 'discipline': 'membership option classification is not insertion'}]
CONCLUSIONS = [{'name': 'C1: membership options classified', 'conclusion': 'typed and role-pure membership options are declaration-ready options; diagnostic labels remain inert-only', 'status': 'PASS', 'meaning': 'safe-membership option set can feed joint package sieve'}, {'name': 'C2: no membership selected', 'conclusion': 'no safe-membership option is selected, adopted, or derived', 'status': 'NOT_CHOSEN', 'meaning': 'current status remains compatible-if-declared only'}, {'name': 'C3: next', 'conclusion': 'joint declaration package sieve should run next', 'status': 'OPEN', 'meaning': 'component options can be combined under node-separation rules'}]


def build_symbolic_loads():
    syms = {name: sp.Symbol(name) for name in SYMBOL_NAMES}
    option_load = sp.simplify(sum((syms[name] for name in SYMBOL_NAMES if not name.startswith("P_")), sp.Integer(0)))
    downstream = sp.simplify(syms.get("P_insertion", 0) + syms.get("P_active_O", 0) + syms.get("P_residual_kill", 0) + syms.get("P_parent", 0))
    total = sp.simplify(option_load + downstream)
    return syms, option_load, downstream, total


def case_0_problem() -> None:
    header("Case 0: Safe-Membership Declaration Option Sieve problem")
    print("Question:\n")
    print("  " + 'Which safe-membership declaration options are coherent enough to carry into a joint declaration package sieve?'.replace("\n", "\n  "))
    print("\nDiscipline:\n")
    for line in ['This script classifies safe-membership declaration options.', 'It fills no declaration slot as theory state.', 'It selects no safe-membership form.', 'It adopts no Package B component.', 'It keeps insertion, active O, residual control, and parent closure closed.']:
        print(f"  {line}")
    print("\nTiny goblin rule:")
    print(f"  Sort the name tags. Do not pin them on.")
    out_line("governance_assessments", "PASS", "Safe-Membership Declaration Option Sieve opened", "inventory only; no declaration, status assignment, adoption, or insertion")


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
    header("Case 2: Safe-membership declaration options")
    for item in ENTRIES:
        subheader(item["name"])
        print(f"Subject: {item['subject']}")
        out_line("governance_assessments", item["status"], item["name"], item.get("summary", ""))
        print(f"Allowed if: {item['allowed_if']}")
        print(f"Blocked if: {item['blocked_if']}")
        print(f"Consequence: {item['consequence']}")
    out_line("governance_assessments", "PASS", "Safe-membership declaration options stated", f"{len(ENTRIES)} entries stated")


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
    out_line("governance_assessments", "PASS", "Safe-Membership Declaration Option Sieve local conclusion stated", "local inventory complete; later reconciliation must compare actual batch results")


def final_interpretation() -> None:
    header("Final interpretation")
    print(
        "Safe-Membership Declaration Option Sieve result:\n\n"
        "  Local inventory completed for Group 37 declaration-option sieve.\n"
        "  This script records options, blocks, shortcuts, and obligations only.\n"
        "  No declaration value is installed as theory state.\n"
        "  No Package B component status is assigned.\n"
        "  No trace-normalization or safe-membership form is selected, adopted, or derived.\n"
        "  Package B is not recommended for adoption.\n"
        "  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.\n\n"
        "Possible next script:\n"
        "  candidate_trace_anchor_joint_declaration_package_sieve.py\n\n"
        "Tiny goblin label:\n"
        "  Sort the name tags. Do not pin them on.\n"
    )
    out_line("governance_assessments", "PASS", "Safe-Membership Declaration Option Sieve complete", "run next script in order.txt; no adoption and downstream gates remain closed")


def record_inventory_marker(ns, option_load: sp.Basic, downstream: sp.Basic, total: sp.Basic) -> None:
    ns.record_derivation(
        derivation_id="g37_membership_options",
        inputs=[option_load, downstream],
        output=total,
        method="Safe-Membership Declaration Option Sieve inventory marker",
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
                obligation_id=f"g37_mem_ob_{ident}",
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
            route_id="g37_mem",
            script_id=SCRIPT_ID,
            name="Safe-Membership Declaration Option Sieve",
            status=GovernanceStatus.CANDIDATE_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            required_obligations=[f"g37_mem_ob_{safe_ident(item['name'])}" for item in OBLIGATIONS],
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
                claim_id=f"g37_mem_en_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.POLICY_RULE,
                statement=(
                    f"{item['subject']} Status: {item['status']}. {item.get('summary', '')} "
                    f"Allowed if: {item['allowed_if']}. Blocked if: {item['blocked_if']}. "
                    f"Consequence: {item['consequence']}."
                ),
                derivation_ids=["g37_membership_options"],
                obligation_ids=[],
            )
        )
    for item in INVALIDS:
        ident = safe_ident(item["name"])
        ns.record_claim(
            ClaimRecord(
                claim_id=f"g37_mem_x_{ident}",
                script_id=SCRIPT_ID,
                claim_kind=RecordKind.GOVERNANCE_CLAIM,
                tier=ClaimTier.CONSTRAINED,
                status=GovernanceStatus.POLICY_RULE,
                statement=f"Forbidden shortcut: {item['shortcut']}. Reason: {item['reason']}. Failure mode: {item['failure_mode']}.",
                derivation_ids=["g37_membership_options"],
                obligation_ids=[],
            )
        )


def main() -> None:
    header("Candidate Safe-Membership Declaration Option Sieve")
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
