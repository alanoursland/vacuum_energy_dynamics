# Candidate postulate dependency graph
#
# Group:
#   32_explicit_minimal_postulate_selection
#
# Human title:
#   Explicit Minimal Postulate Selection
#
# Script type:
#   DEPENDENCY GRAPH / NO-SMUGGLING EDGE AUDIT
#
# Purpose
# -------
# Map dependency and no-smuggling edges among the Group 32 candidate postulates.
# The graph separates prerequisite edges from forbidden implication edges, inherited
# discipline edges, and downstream gate edges.
#
# Locked-door question:
#
#   Which edges among the candidate postulates are valid prerequisites, and which
#   edges would smuggle theorem targets, residual control, insertion, active O, or
#   parent closure into an explicit-choice package?
#
# This script does not adopt a postulate.
# It does not run package minimality tests.
# It does not derive trace normalization.
# It does not derive safe trace membership.
# It does not derive trace/residual incidence.
# It does not derive the complete coefficient law.
# It does not derive B_s/F_zeta insertion.
# It does not derive active O.
# It does not derive residual control.
# It does not open the parent equation.
#
# Tiny goblin rule:
#
#   Draw the bite marks before counting the teeth as one jaw.

from dataclasses import dataclass
from pathlib import Path
from typing import List

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    BranchDecisionRecord,
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    RecordKind,
    RouteRecord,
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


def status_mark(status: str) -> StatusMark:
    return {
        "ADMISSIBLE_EDGE": StatusMark.INFO,
        "BLOCKED": StatusMark.FAIL,
        "CANDIDATE_ROUTE": StatusMark.DEFER,
        "DEPENDENCY_EDGE": StatusMark.INFO,
        "FORBIDDEN_EDGE": StatusMark.FAIL,
        "GATE_CLOSED": StatusMark.DEFER,
        "INHERITED_EDGE": StatusMark.INFO,
        "NO_SMUGGLING_RULE": StatusMark.OBLIGATION,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REQUIRED": StatusMark.OBLIGATION,
        "THEOREM_TARGET": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g32_candidate_ledger",
            "032_explicit_minimal_postulate_selection__candidate_postulate_candidate_ledger",
            "g32_candidate_postulate_ledger",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g32_problem",
            "032_explicit_minimal_postulate_selection__candidate_explicit_postulate_selection_problem",
            "g32_explicit_selection_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_summary",
            "031_source_divergence_coefficient_law__candidate_group_31_status_summary",
            "g31_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_obligations",
            "031_source_divergence_coefficient_law__candidate_source_divergence_obligations",
            "g31_obligations",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_trace_norm",
            "031_source_divergence_coefficient_law__candidate_trace_normalization_from_source_divergence",
            "g31_trace_normalization_fork",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g30_summary",
            "030_minimal_coefficient_sector_postulate_inventory__candidate_group_30_status_summary",
            "g30_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
    ]

    for dependency_id, upstream_script_id, upstream_derivation_id, expected_record_kind in dependencies:
        ns.declare_dependency(
            dependency_id=dependency_id,
            upstream_script_id=upstream_script_id,
            upstream_derivation_id=upstream_derivation_id,
            expected_record_kind=expected_record_kind,
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


@dataclass
class GraphSymbols:
    P_trace_norm: sp.Symbol
    P_safe_membership: sp.Symbol
    P_guardrail_visibility: sp.Symbol
    P_div_explicitness: sp.Symbol
    P_source_no_hidden: sp.Symbol
    P_incidence_zero: sp.Symbol
    P_active_O: sp.Symbol
    P_residual_kill: sp.Symbol
    P_insertion: sp.Symbol
    P_parent: sp.Symbol
    E_valid_prereq: sp.Expr
    E_no_smuggle: sp.Expr
    E_downstream_gate: sp.Expr
    E_package_ready_gap: sp.Expr


@dataclass
class DependencyEdge:
    name: str
    source: str
    target: str
    status: str
    edge_type: str
    meaning: str
    allowed_use: str
    forbidden_upgrade: str


@dataclass
class NoSmugglingEdge:
    name: str
    invalid_edge: str
    status: str
    reason: str
    required_fence: str
    failure_mode: str


@dataclass
class GateEdge:
    name: str
    gate: str
    status: str
    closed_because: str
    future_form: str
    forbidden_now: str


@dataclass
class GraphObligation:
    name: str
    obligation: str
    status: str
    blocks: str
    discipline: str


@dataclass
class GraphConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> GraphSymbols:
    (
        P_trace_norm,
        P_safe_membership,
        P_guardrail_visibility,
        P_div_explicitness,
        P_source_no_hidden,
        P_incidence_zero,
        P_active_O,
        P_residual_kill,
        P_insertion,
        P_parent,
    ) = sp.symbols(
        "P_trace_norm P_safe_membership P_guardrail_visibility P_div_explicitness "
        "P_source_no_hidden P_incidence_zero P_active_O P_residual_kill P_insertion P_parent",
        real=True,
    )

    E_valid_prereq = sp.simplify(
        P_trace_norm
        + P_safe_membership
        + P_guardrail_visibility
        + P_div_explicitness
        + P_source_no_hidden
    )

    E_no_smuggle = sp.simplify(
        P_incidence_zero + P_active_O + P_residual_kill + P_insertion + P_parent
    )

    E_downstream_gate = sp.simplify(P_active_O + P_residual_kill + P_insertion + P_parent)

    E_package_ready_gap = sp.simplify(
        E_valid_prereq
        + E_no_smuggle
        + E_downstream_gate
    )

    return GraphSymbols(
        P_trace_norm=P_trace_norm,
        P_safe_membership=P_safe_membership,
        P_guardrail_visibility=P_guardrail_visibility,
        P_div_explicitness=P_div_explicitness,
        P_source_no_hidden=P_source_no_hidden,
        P_incidence_zero=P_incidence_zero,
        P_active_O=P_active_O,
        P_residual_kill=P_residual_kill,
        P_insertion=P_insertion,
        P_parent=P_parent,
        E_valid_prereq=E_valid_prereq,
        E_no_smuggle=E_no_smuggle,
        E_downstream_gate=E_downstream_gate,
        E_package_ready_gap=E_package_ready_gap,
    )


def build_dependency_edges() -> List[DependencyEdge]:
    return [
        DependencyEdge(
            name="E1: trace normalization before trace-anchor package",
            source="P_trace_norm",
            target="trace-anchor package sufficiency audit",
            status="DEPENDENCY_EDGE",
            edge_type="valid prerequisite",
            meaning="a trace-anchor package cannot be evaluated unless the normalization role is named",
            allowed_use="prerequisite for later package testing",
            forbidden_upgrade="does not choose the normalization value and does not derive coefficient law",
        ),
        DependencyEdge(
            name="E2: safe membership before trace-anchor package",
            source="P_safe_membership",
            target="trace-anchor package sufficiency audit",
            status="DEPENDENCY_EDGE",
            edge_type="valid prerequisite",
            meaning="membership domain must be stated before testing whether the package is coherent",
            allowed_use="prerequisite for later package testing",
            forbidden_upgrade="does not imply zero trace/residual incidence or active no-overlap",
        ),
        DependencyEdge(
            name="E3: guardrail visibility before sufficiency classification",
            source="P_guardrail_visibility",
            target="package sufficiency audit",
            status="DEPENDENCY_EDGE",
            edge_type="valid prerequisite",
            meaning="visible guardrail loads are required before a package can be called auditable",
            allowed_use="visibility precondition",
            forbidden_upgrade="does not prove boundary, source, current, mass, support, or scalar neutrality",
        ),
        DependencyEdge(
            name="E4: divergence explicitness before sufficiency classification",
            source="P_div_explicitness",
            target="package sufficiency audit",
            status="DEPENDENCY_EDGE",
            edge_type="valid prerequisite",
            meaning="correction/divergence behavior must remain explicit and non-reservoir",
            allowed_use="explicitness precondition",
            forbidden_upgrade="does not prove divergence-safe coefficient law",
        ),
        DependencyEdge(
            name="E5: inherited source-hidden exclusion before package minimality accounting",
            source="P_source_no_hidden",
            target="package minimality accounting",
            status="INHERITED_EDGE",
            edge_type="inherited partial-constraint edge",
            meaning="hidden ordinary source pockets remain excluded by Group 31 partial constraints",
            allowed_use="anti-smuggling discipline in package accounting",
            forbidden_upgrade="does not become full source no-double-counting theorem or fresh adoption automatically",
        ),
        DependencyEdge(
            name="E6: candidate ledger before dependency graph",
            source="candidate_postulate_candidate_ledger",
            target="candidate_postulate_dependency_graph",
            status="DEPENDENCY_EDGE",
            edge_type="script dependency",
            meaning="candidate classes must be inventoried before graph edges are mapped",
            allowed_use="local Group 32 chain",
            forbidden_upgrade="does not make package tests complete",
        ),
    ]


def build_no_smuggling_edges() -> List[NoSmugglingEdge]:
    return [
        NoSmugglingEdge(
            name="N1: normalization is not membership",
            invalid_edge="P_trace_norm -> P_safe_membership",
            status="FORBIDDEN_EDGE",
            reason="normalization selects how B_s reads zeta; membership assigns zeta_Bs to T_zeta",
            required_fence="keep normalization and membership as separate candidate nodes",
            failure_mode="Package B silently collapses two choices into one",
        ),
        NoSmugglingEdge(
            name="N2: membership is not incidence",
            invalid_edge="P_safe_membership -> P_incidence_zero",
            status="FORBIDDEN_EDGE",
            reason="safe membership does not imply I(T_zeta,R_zeta)=0 or I(T_zeta,R_kappa)=0",
            required_fence="zero incidence remains high-risk theorem target or strong-postulate target",
            failure_mode="residual control is smuggled through membership",
        ),
        NoSmugglingEdge(
            name="N3: membership is not active O",
            invalid_edge="P_safe_membership -> P_active_O",
            status="FORBIDDEN_EDGE",
            reason="active O requires an actual operator with domain, codomain, kernel, image, pairing, and boundary behavior",
            required_fence="no active no-overlap operator follows from membership assignment",
            failure_mode="operator is adopted by naming a safe trace channel",
        ),
        NoSmugglingEdge(
            name="N4: explicitness is not divergence safety",
            invalid_edge="P_div_explicitness -> divergence-safe coefficient law",
            status="FORBIDDEN_EDGE",
            reason="non-reservoir explicitness is weaker than divergence-safe coefficient law",
            required_fence="full divergence-safe coefficient law remains open theorem target",
            failure_mode="visible correction is upgraded into conservation compatibility",
        ),
        NoSmugglingEdge(
            name="N5: visibility is not neutrality",
            invalid_edge="P_guardrail_visibility -> guardrail neutrality",
            status="FORBIDDEN_EDGE",
            reason="visible and auditable loads are not automatically neutral loads",
            required_fence="boundary/source/current/mass/support neutrality remain theorem burdens",
            failure_mode="auditable failure is mistaken for neutral failure",
        ),
        NoSmugglingEdge(
            name="N6: source-hidden exclusion is not source no-double-counting theorem",
            invalid_edge="P_source_no_hidden -> full source no-double-counting theorem",
            status="FORBIDDEN_EDGE",
            reason="Group 31 ruled out hidden pockets but did not derive full sector-by-sector theorem",
            required_fence="carry source no-double-counting as open theorem target",
            failure_mode="partial constraint becomes full theorem",
        ),
        NoSmugglingEdge(
            name="N7: trace-anchor package is not insertion",
            invalid_edge="Package B -> P_insertion",
            status="FORBIDDEN_EDGE",
            reason="candidate package can at most prepare insertion-precondition audits",
            required_fence="B_s/F_zeta insertion remains not ready",
            failure_mode="package survival becomes metric insertion",
        ),
        NoSmugglingEdge(
            name="N8: trace-anchor package is not parent closure",
            invalid_edge="Package B -> P_parent",
            status="FORBIDDEN_EDGE",
            reason="parent field equation remains closed until upstream gates are resolved",
            required_fence="parent closure remains forbidden immediate route",
            failure_mode="explicit-choice package opens parent equation",
        ),
    ]


def build_gate_edges() -> List[GateEdge]:
    return [
        GateEdge(
            name="G1: incidence gate",
            gate="P_incidence_zero",
            status="NOT_READY",
            closed_because="zero trace/residual incidence is not derived and is too close to residual control/no-overlap smuggling",
            future_form="separate theorem target or explicit strong-postulate decision after warnings",
            forbidden_now="cannot be included in minimal package by implication",
        ),
        GateEdge(
            name="G2: active O gate",
            gate="P_active_O",
            status="NOT_READY",
            closed_because="active no-overlap operator is not constructed",
            future_form="construction route with domain/codomain/kernel/image/pairing/boundary behavior",
            forbidden_now="cannot be adopted by name",
        ),
        GateEdge(
            name="G3: residual-control gate",
            gate="P_residual_kill",
            status="NOT_READY",
            closed_because="residual-kill law and residual-control theorem are not derived",
            future_form="residual-control theorem or separate high-risk explicit postulate decision",
            forbidden_now="cannot follow from safe membership, visibility, explicitness, or Package B",
        ),
        GateEdge(
            name="G4: insertion gate",
            gate="P_insertion",
            status="NOT_READY",
            closed_because="normalization, membership, incidence, coefficient-law, no-overlap, and residual gates remain open",
            future_form="insertion-precondition inventory or theorem route after prerequisites",
            forbidden_now="cannot be adopted as a minimal postulate now",
        ),
        GateEdge(
            name="G5: parent gate",
            gate="P_parent",
            status="GATE_CLOSED",
            closed_because="parent field equation is not ready and scalar recombination is blocked",
            future_form="future parent route after insertion/divergence/source/residual gates close",
            forbidden_now="cannot be opened by any Group 32 candidate package",
        ),
    ]


def build_obligations() -> List[GraphObligation]:
    return [
        GraphObligation(
            name="O1: keep valid prerequisites weak",
            obligation="record valid prerequisite edges without upgrading them into theorem support",
            status="OPEN",
            blocks="package sufficiency tests",
            discipline="prerequisite edge is not proof edge",
        ),
        GraphObligation(
            name="O2: preserve normalization membership split",
            obligation="keep P_trace_norm and P_safe_membership distinct in all package tests",
            status="OPEN",
            blocks="trace-anchor package accounting",
            discipline="normalization is not membership",
        ),
        GraphObligation(
            name="O3: preserve membership incidence fence",
            obligation="prevent P_safe_membership from implying P_incidence_zero, residual kill, or active O",
            status="OPEN",
            blocks="safe membership use",
            discipline="membership is not no-overlap geometry",
        ),
        GraphObligation(
            name="O4: preserve visibility neutrality fence",
            obligation="prevent P_guardrail_visibility from implying boundary/source/current/mass/support neutrality",
            status="OPEN",
            blocks="package sufficiency classification",
            discipline="visibility is not neutrality",
        ),
        GraphObligation(
            name="O5: preserve explicitness divergence-safety fence",
            obligation="prevent P_div_explicitness from implying divergence-safe coefficient law",
            status="OPEN",
            blocks="coefficient law claims",
            discipline="explicitness is not divergence safety",
        ),
        GraphObligation(
            name="O6: keep downstream gates closed",
            obligation="keep incidence, active O, residual kill, insertion, and parent closure outside package minimality",
            status="NOT_READY",
            blocks="downstream overreach",
            discipline="dependency graph is not insertion or parent closure",
        ),
    ]


def build_conclusions() -> List[GraphConclusion]:
    return [
        GraphConclusion(
            name="C1: dependency graph mapped",
            conclusion="valid prerequisite edges and invalid implication edges are separated",
            status="REQUIRED",
            meaning="package tests may now use the graph without collapsing candidates into stronger claims",
        ),
        GraphConclusion(
            name="C2: no-smuggling fences stated",
            conclusion="normalization/membership/incidence, visibility/neutrality, and explicitness/divergence-safety fences are explicit",
            status="REQUIRED",
            meaning="forbidden implication edges are visible before package testing",
        ),
        GraphConclusion(
            name="C3: downstream gates closed",
            conclusion="incidence, active O, residual kill, insertion, and parent closure remain outside the candidate graph as usable package consequences",
            status="NOT_READY",
            meaning="dependency graph does not open downstream gates",
        ),
        GraphConclusion(
            name="C4: no adoption",
            conclusion="this graph adopts no postulate",
            status="NOT_ADOPTED",
            meaning="graph edges are governance/audit structure, not explicit theory choice",
        ),
        GraphConclusion(
            name="C5: next",
            conclusion="candidate package sieve should run next",
            status="OPEN",
            meaning="packages can now be tested for insufficiency, plausibility, overstrength, and forbidden upgrades",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Postulate dependency graph problem")
    print("Question:")
    print()
    print("  Which edges among the candidate postulates are valid prerequisites, and which")
    print("  edges would smuggle theorem targets, residual control, insertion, active O, or")
    print("  parent closure into an explicit-choice package?")
    print()
    print("Discipline:")
    print()
    print("  This script maps graph edges.")
    print("  It adopts no postulate.")
    print("  It performs no package minimality test.")
    print("  It derives no coefficient law and no insertion.")
    print("  It keeps active O, residual control, and parent closure closed.")
    print()
    print("Tiny goblin rule:")
    print("  Draw the bite marks before counting the teeth as one jaw.")

    with out.governance_assessments():
        out.line(
            "postulate dependency graph opened",
            StatusMark.INFO,
            "mapping valid prerequisite edges and forbidden implication edges before package tests",
        )


def case_1_symbolic_graph(symbols: GraphSymbols, out: ScriptOutput) -> None:
    header("Case 1: Dependency graph symbolic loads")

    print("Candidate symbols:")
    print()
    for sym in (
        symbols.P_trace_norm,
        symbols.P_safe_membership,
        symbols.P_guardrail_visibility,
        symbols.P_div_explicitness,
        symbols.P_source_no_hidden,
        symbols.P_incidence_zero,
        symbols.P_active_O,
        symbols.P_residual_kill,
        symbols.P_insertion,
        symbols.P_parent,
    ):
        print(f"  {sym} = {sym}")

    print()
    print("Valid prerequisite edge load:")
    print(f"  E_valid_prereq = {symbols.E_valid_prereq}")
    print()
    print("No-smuggling edge load:")
    print(f"  E_no_smuggle = {symbols.E_no_smuggle}")
    print()
    print("Downstream gate load:")
    print(f"  E_downstream_gate = {symbols.E_downstream_gate}")
    print()
    print("Package-readiness gap:")
    print(f"  E_package_ready_gap = {symbols.E_package_ready_gap}")

    with out.derived_results():
        out.line(
            "dependency graph symbolic loads stated",
            StatusMark.OBLIGATION,
            (
                f"E_valid_prereq = {symbols.E_valid_prereq}; "
                f"E_no_smuggle = {symbols.E_no_smuggle}; "
                f"E_downstream_gate = {symbols.E_downstream_gate}"
            ),
        )


def case_2_dependency_edges(edges: List[DependencyEdge], out: ScriptOutput) -> None:
    header("Case 2: Valid prerequisite / inherited dependency edges")

    for item in edges:
        subheader(item.name)
        print(f"Source: {item.source}")
        print(f"Target: {item.target}")
        print(f"Edge type: {item.edge_type}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Meaning: {item.meaning}")
        print(f"Allowed use: {item.allowed_use}")
        print(f"Forbidden upgrade: {item.forbidden_upgrade}")

    with out.governance_assessments():
        out.line(
            "valid prerequisite edges stated",
            StatusMark.INFO,
            f"{len(edges)} dependency/inherited edges mapped",
        )


def case_3_no_smuggling_edges(edges: List[NoSmugglingEdge], out: ScriptOutput) -> None:
    header("Case 3: Forbidden implication / no-smuggling edges")

    for item in edges:
        subheader(item.name)
        print(f"Invalid edge: {item.invalid_edge}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")
        print(f"Required fence: {item.required_fence}")
        print(f"Failure mode: {item.failure_mode}")

    with out.governance_assessments():
        out.line(
            "no-smuggling edges rejected",
            StatusMark.OBLIGATION,
            f"{len(edges)} forbidden implication edges stated",
        )


def case_4_downstream_gates(gates: List[GateEdge], out: ScriptOutput) -> None:
    header("Case 4: Downstream gate edges")

    for item in gates:
        subheader(item.name)
        print(f"Gate: {item.gate}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Closed because: {item.closed_because}")
        print(f"Future form: {item.future_form}")
        print(f"Forbidden now: {item.forbidden_now}")

    with out.governance_assessments():
        out.line(
            "downstream gates remain closed",
            StatusMark.DEFER,
            f"{len(gates)} downstream gates excluded from package consequences",
        )


def case_5_obligations(obligations: List[GraphObligation], out: ScriptOutput) -> None:
    header("Case 5: Dependency-graph obligations")

    for item in obligations:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Blocks: {item.blocks}")
        print(f"Discipline: {item.discipline}")

    with out.unresolved_obligations():
        out.line(
            "dependency-graph obligations opened",
            StatusMark.OBLIGATION,
            f"{len(obligations)} obligations stated",
        )


def case_6_conclusions(conclusions: List[GraphConclusion], out: ScriptOutput) -> None:
    header("Case 6: Dependency-graph conclusions")

    for item in conclusions:
        subheader(item.name)
        print(f"Conclusion: {item.conclusion}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Meaning: {item.meaning}")

    with out.governance_assessments():
        out.line(
            "postulate dependency graph conclusion stated",
            StatusMark.PASS,
            "valid edges and forbidden implication edges mapped; candidate package sieve should run next",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Postulate dependency graph result:")
    print()
    print("  Valid prerequisite edges are mapped without treating them as theorem support.")
    print("  Trace normalization and safe membership remain separate nodes.")
    print("  Safe membership does not imply trace/residual zero incidence, residual kill, or active O.")
    print("  Guardrail visibility does not imply neutrality.")
    print("  Divergence explicitness does not imply divergence-safe coefficient law.")
    print("  Source hidden-pocket exclusion remains inherited partial constraint, not full source no-double-counting.")
    print("  Package B, if later tested, cannot imply insertion or parent closure.")
    print("  Active O, residual kill, B_s/F_zeta insertion, and parent closure remain not ready.")
    print("  No postulate is adopted by this graph.")
    print()
    print("Possible next script:")
    print("  candidate_postulate_package_sieve.py")
    print()
    print("Tiny goblin label:")
    print("  Draw the bite marks before counting the teeth as one jaw.")

    with out.governance_assessments():
        out.line(
            "postulate dependency graph complete",
            StatusMark.PASS,
            "package sieve should run next; minimality tests are now allowed but adoption remains separate",
        )


def record_inventory_marker(ns, symbols: GraphSymbols) -> None:
    ns.record_derivation(
        derivation_id="g32_postulate_dependency_graph",
        inputs=[
            symbols.P_trace_norm,
            symbols.P_safe_membership,
            symbols.P_guardrail_visibility,
            symbols.P_div_explicitness,
            symbols.P_source_no_hidden,
            symbols.P_incidence_zero,
            symbols.P_active_O,
            symbols.P_residual_kill,
            symbols.P_insertion,
            symbols.P_parent,
        ],
        output=symbols.E_package_ready_gap,
        method="map valid prerequisite, no-smuggling, and downstream gate edges without adoption",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="postulate_dependency_graph_marker",
        scope="Group 32 explicit minimal postulate selection",
        is_placeholder=True,
    )


def record_obligations(ns, obligations: List[GraphObligation]) -> None:
    obligation_id_map = {
        "O1: keep valid prerequisites weak": "g32_prerequisite_edges_not_proof_edges",
        "O2: preserve normalization membership split": "g32_preserve_normalization_membership_split",
        "O3: preserve membership incidence fence": "g32_preserve_membership_incidence_fence",
        "O4: preserve visibility neutrality fence": "g32_preserve_visibility_neutrality_fence",
        "O5: preserve explicitness divergence-safety fence": "g32_preserve_explicitness_divergence_safety_fence",
        "O6: keep downstream gates closed": "g32_keep_downstream_gates_closed",
    }

    for item in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id_map[item.name],
            script_id=SCRIPT_ID,
            title=item.obligation,
            status=ObligationStatus.OPEN,
            required_by=["g32_postulate_dependency_graph"],
            description=f"{item.discipline} Blocks: {item.blocks}.",
        ))


def record_governance(
    ns,
    dependency_edges: List[DependencyEdge],
    no_smuggling_edges: List[NoSmugglingEdge],
    gate_edges: List[GateEdge],
) -> None:
    obligation_ids = [
        "g32_prerequisite_edges_not_proof_edges",
        "g32_preserve_normalization_membership_split",
        "g32_preserve_membership_incidence_fence",
        "g32_preserve_visibility_neutrality_fence",
        "g32_preserve_explicitness_divergence_safety_fence",
        "g32_keep_downstream_gates_closed",
    ]

    ns.record_route(RouteRecord(
        route_id="g32_postulate_dependency_graph_route",
        script_id=SCRIPT_ID,
        name="Group 32 postulate dependency graph route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "candidate postulate ledger completed",
            "valid prerequisite edges must be separated from forbidden implication edges",
            "package tests require no-smuggling graph first",
            "no postulate adoption is performed by graph mapping",
        ],
    ))

    for item in dependency_edges:
        ns.record_claim(ClaimRecord(
            claim_id=f"g32_dependency_edge_{item.name.split(':')[0].lower()}",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.CANDIDATE_ROUTE,
            statement=(
                f"{item.name}: {item.source} -> {item.target} is a {item.edge_type}. "
                f"Allowed use: {item.allowed_use}. Forbidden upgrade: {item.forbidden_upgrade}."
            ),
            derivation_ids=["g32_postulate_dependency_graph"],
            obligation_ids=obligation_ids,
        ))

    for item in no_smuggling_edges:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"g32_forbidden_edge_{item.name.split(':')[0].lower()}",
            script_id=SCRIPT_ID,
            branch_id=item.invalid_edge,
            status=GovernanceStatus.POLICY_RULE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Forbidden implication edge. Reason: {item.reason}. Required fence: {item.required_fence}.",
        ))

    for item in gate_edges:
        ns.record_claim(ClaimRecord(
            claim_id=f"g32_gate_{item.gate}",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
            statement=(
                f"{item.gate} remains {item.status}. Closed because: {item.closed_because}. "
                f"Future form: {item.future_form}. Forbidden now: {item.forbidden_now}."
            ),
            derivation_ids=["g32_postulate_dependency_graph"],
            obligation_ids=obligation_ids,
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g32_postulate_dependency_graph_complete",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Group 32 postulate dependency graph is complete. Valid prerequisite edges and forbidden implication edges are separated. "
            "Normalization is not membership; membership is not incidence or active O; visibility is not neutrality; explicitness is not divergence safety. "
            "Package selection cannot license insertion or parent closure. No postulate is adopted by this graph. Package sieve should run next."
        ),
        derivation_ids=["g32_postulate_dependency_graph"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Postulate Dependency Graph")
    archive, ns, invalidated = prepare_archive()
    ensure_archive_write_dirs(ns)
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    dependency_edges = build_dependency_edges()
    no_smuggling_edges = build_no_smuggling_edges()
    gate_edges = build_gate_edges()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbolic_graph(symbols, out)
    case_2_dependency_edges(dependency_edges, out)
    case_3_no_smuggling_edges(no_smuggling_edges, out)
    case_4_downstream_gates(gate_edges, out)
    case_5_obligations(obligations, out)
    case_6_conclusions(conclusions, out)
    final_interpretation(out)

    record_inventory_marker(ns, symbols)
    record_obligations(ns, obligations)
    record_governance(ns, dependency_edges, no_smuggling_edges, gate_edges)

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
