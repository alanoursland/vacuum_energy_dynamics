# Candidate trace-normalization volume-trace ledger
#
# Group:
#   33_trace_normalization_candidate_origin
#
# Human title:
#   Trace Normalization Candidate Origin
#
# Script type:
#   STRUCTURAL LEDGER / ORIGIN-ROUTE AUDIT
#
# Purpose
# -------
# Inventory the volume-trace, determinant/unimodular, dimensional-counting,
# and linearized-trace routes for the trace-normalization candidate.
#
# Locked-door question:
#
#   What structural trace conventions can constrain how B_s reads zeta,
#   without selecting the normalization from recovery, repair, insertion,
#   active O, or parent fit?
#
# This script does not adopt trace normalization.
# It does not select a final normalization value.
# It does not derive safe trace membership.
# It does not derive trace/residual incidence.
# It does not derive the complete B_s/F_zeta coefficient law.
# It does not derive B_s/F_zeta insertion.
# It does not derive active O.
# It does not derive residual control.
# It does not open the parent equation.
#
# Tiny goblin rule:
#
#   Measure the cup before naming the drink.

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
        "ADMISSIBLE_ORIGIN_ROUTE": StatusMark.INFO,
        "CANDIDATE_FORM": StatusMark.INFO,
        "COMPATIBILITY_ONLY": StatusMark.INFO,
        "CONVENTION_DEPENDENT": StatusMark.DEFER,
        "DERIVED_STRUCTURAL_IDENTITY": StatusMark.PASS,
        "INSUFFICIENT_FOR_SELECTION": StatusMark.DEFER,
        "LINEARIZED_ONLY": StatusMark.DEFER,
        "NOT_ADOPTED": StatusMark.DEFER,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "POLICY_RULE": StatusMark.OBLIGATION,
        "REJECTED_AS_SELECTOR": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "STRUCTURAL_CONSTRAINT": StatusMark.INFO,
    }.get(status, StatusMark.INFO)


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g33_origin_problem",
            "33_trace_normalization_candidate_origin__candidate_trace_normalization_origin_problem",
            "g33_trace_normalization_origin_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g32_summary",
            "32_explicit_minimal_postulate_selection__candidate_group_32_status_summary",
            "g32_status_summary",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g32_minimality",
            "32_explicit_minimal_postulate_selection__candidate_postulate_package_minimality",
            "g32_postulate_package_minimality",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_trace_norm",
            "31_source_divergence_coefficient_law__candidate_trace_normalization_from_source_divergence",
            "g31_trace_normalization_fork",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g31_summary",
            "31_source_divergence_coefficient_law__candidate_group_31_status_summary",
            "g31_status_summary",
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
class VolumeTraceSymbols:
    zeta: sp.Symbol
    d: sp.Symbol
    q_scale: sp.Symbol
    b_metric: sp.Symbol
    N_trace: sp.Symbol
    N_volume: sp.Symbol
    N_metric: sp.Symbol
    N_scale: sp.Symbol
    N_linear: sp.Symbol
    S_recovery: sp.Symbol
    S_repair: sp.Symbol
    S_insertion: sp.Symbol
    S_parent: sp.Symbol
    log_volume_from_q: sp.Expr
    log_metric_from_zeta: sp.Expr
    log_scale_from_zeta: sp.Expr
    det_identity_residual: sp.Expr
    volume_identity_residual: sp.Expr
    L_structural_trace: sp.Expr
    L_forbidden_selectors: sp.Expr
    L_volume_trace_gap: sp.Expr


@dataclass
class StructuralRoute:
    name: str
    route: str
    status: str
    structural_content: str
    constraint: str
    boundary: str


@dataclass
class CandidateConvention:
    name: str
    convention: str
    status: str
    candidate_form: str
    requires: str
    not_equivalent_to: str


@dataclass
class SelectorFence:
    name: str
    rule: str
    status: str
    reason: str


@dataclass
class LedgerObligation:
    name: str
    obligation: str
    status: str
    blocks: str
    discipline: str


@dataclass
class LedgerConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> VolumeTraceSymbols:
    zeta = sp.symbols("zeta", real=True)
    d = sp.symbols("d", positive=True, integer=True)
    q_scale, b_metric = sp.symbols("q_scale b_metric", real=True)
    N_trace, N_volume, N_metric, N_scale, N_linear = sp.symbols(
        "N_trace N_volume N_metric N_scale N_linear",
        real=True,
    )
    S_recovery, S_repair, S_insertion, S_parent = sp.symbols(
        "S_recovery S_repair S_insertion S_parent",
        real=True,
    )

    # If zeta is the logarithm of the spatial volume element relative to a
    # unimodular companion, then a uniform spatial scale q satisfies d*q = zeta.
    log_volume_from_q = sp.simplify(d * q_scale)
    log_scale_from_zeta = sp.simplify(zeta / d)

    # If B_s is interpreted as a metric coefficient rather than a scale factor,
    # then log(B_s) carries twice the scale-factor log.
    log_metric_from_zeta = sp.simplify(2 * zeta / d)

    # Structural residuals only. They do not choose which convention B_s uses.
    volume_identity_residual = sp.simplify(d * log_scale_from_zeta - zeta)
    det_identity_residual = sp.simplify(d * log_metric_from_zeta - 2 * zeta)

    L_structural_trace = sp.simplify(N_volume + N_metric + N_scale + N_linear)
    L_forbidden_selectors = sp.simplify(S_recovery + S_repair + S_insertion + S_parent)
    L_volume_trace_gap = sp.simplify(N_trace + L_structural_trace + L_forbidden_selectors)

    return VolumeTraceSymbols(
        zeta=zeta,
        d=d,
        q_scale=q_scale,
        b_metric=b_metric,
        N_trace=N_trace,
        N_volume=N_volume,
        N_metric=N_metric,
        N_scale=N_scale,
        N_linear=N_linear,
        S_recovery=S_recovery,
        S_repair=S_repair,
        S_insertion=S_insertion,
        S_parent=S_parent,
        log_volume_from_q=log_volume_from_q,
        log_metric_from_zeta=log_metric_from_zeta,
        log_scale_from_zeta=log_scale_from_zeta,
        det_identity_residual=det_identity_residual,
        volume_identity_residual=volume_identity_residual,
        L_structural_trace=L_structural_trace,
        L_forbidden_selectors=L_forbidden_selectors,
        L_volume_trace_gap=L_volume_trace_gap,
    )


def build_structural_routes() -> List[StructuralRoute]:
    return [
        StructuralRoute(
            name="V1: volume-trace route",
            route="define zeta as the logarithmic spatial volume trace relative to a unimodular companion",
            status="ADMISSIBLE_ORIGIN_ROUTE",
            structural_content="uniform scale q obeys d*q = zeta when zeta is volume-log trace",
            constraint="can constrain scale-factor normalization to q = zeta/d under that convention",
            boundary="does not decide whether B_s is a scale factor, metric coefficient, or separately normalized variable",
        ),
        StructuralRoute(
            name="V2: determinant / unimodular route",
            route="write gamma_ij = exp(2*zeta/d) * bar_gamma_ij with det(bar_gamma)=1 under metric-coefficient convention",
            status="STRUCTURAL_CONSTRAINT",
            structural_content="det(gamma)/det(bar_gamma) = exp(2*zeta)",
            constraint="metric-coefficient log response is 2*zeta/d if zeta is volume-log trace",
            boundary="decomposition is not active O, residual kill, or insertion",
        ),
        StructuralRoute(
            name="V3: dimensional counting route",
            route="use the number d of traced spatial dimensions to distribute volume trace across isotropic directions",
            status="ADMISSIBLE_ORIGIN_ROUTE",
            structural_content="per-direction scale log is zeta/d; per-direction metric log is 2*zeta/d",
            constraint="normalization depends on the explicitly counted sector",
            boundary="counting may constrain candidates but must not be chosen after recovery target is known",
        ),
        StructuralRoute(
            name="V4: linearized trace route",
            route="use first-order trace bookkeeping delta ln sqrt(gamma) = 1/2 tr(h)",
            status="LINEARIZED_ONLY",
            structural_content="linearized convention can match the volume-log trace at first order",
            constraint="useful as first-order consistency check",
            boundary="linearized bookkeeping is not exact insertion theorem",
        ),
    ]


def build_candidate_conventions() -> List[CandidateConvention]:
    return [
        CandidateConvention(
            name="C1: scale-factor convention",
            convention="B_s is treated as a spatial scale factor",
            status="CANDIDATE_FORM",
            candidate_form="log(B_s) = zeta/d",
            requires="zeta is defined as volume-log trace and d is the traced sector dimension",
            not_equivalent_to="metric-coefficient convention, safe membership, insertion, or recovery",
        ),
        CandidateConvention(
            name="C2: metric-coefficient convention",
            convention="B_s is treated as a spatial metric coefficient factor",
            status="CANDIDATE_FORM",
            candidate_form="log(B_s) = 2*zeta/d",
            requires="zeta is defined as volume-log trace and B_s denotes metric coefficient response",
            not_equivalent_to="scale-factor convention, safe membership, residual kill, or insertion",
        ),
        CandidateConvention(
            name="C3: per-dimension normalized zeta convention",
            convention="zeta is already defined as a per-direction trace variable",
            status="CONVENTION_DEPENDENT",
            candidate_form="log(B_s) = zeta or log(B_s) = 2*zeta depending on B_s convention",
            requires="explicit declaration that zeta is already divided by the traced dimension",
            not_equivalent_to="deriving the value from recovery or Package B minimality",
        ),
        CandidateConvention(
            name="C4: linearized trace convention",
            convention="normalization is fixed only in first-order trace bookkeeping",
            status="LINEARIZED_ONLY",
            candidate_form="first-order relation between spatial trace and volume-log response",
            requires="explicit linearized scope and no exact-insertion upgrade",
            not_equivalent_to="exact B_s/F_zeta law or parent-field insertion",
        ),
    ]


def build_selector_fences() -> List[SelectorFence]:
    return [
        SelectorFence(
            name="R1: determinant split is not residual kill",
            rule="determinant/unimodular decomposition cannot delete residual zeta/kappa trace by declaration",
            status="POLICY_RULE",
            reason="residual control remains separate theorem target",
        ),
        SelectorFence(
            name="R2: dimensional count is not recovery selector",
            rule="the counted sector dimension must be declared before recovery checks",
            status="POLICY_RULE",
            reason="dimension counting may constrain normalization but cannot be chosen from AB=1, gamma, or Schwarzschild recovery",
        ),
        SelectorFence(
            name="R3: linearized trace is not exact theorem",
            rule="first-order trace convention cannot be promoted to exact coefficient law without additional derivation",
            status="POLICY_RULE",
            reason="linearized compatibility is weaker than exact B_s/F_zeta law",
        ),
        SelectorFence(
            name="R4: compatibility is not selector",
            rule="source-neutral, divergence-explicit, and safe-membership compatibility may reject candidates but cannot choose normalization",
            status="POLICY_RULE",
            reason="compatibility is not proof or adoption",
        ),
        SelectorFence(
            name="R5: no insertion or parent shortcut",
            rule="candidate trace conventions do not license B_s/F_zeta insertion or parent closure",
            status="POLICY_RULE",
            reason="downstream gates remain closed",
        ),
    ]


def build_obligations() -> List[LedgerObligation]:
    return [
        LedgerObligation(
            name="O1: declare zeta convention",
            obligation="state whether zeta is volume-log trace, metric trace, or per-dimension normalized trace before choosing a form",
            status="OPEN",
            blocks="candidate-form testing",
            discipline="trace variable convention must be explicit",
        ),
        LedgerObligation(
            name="O2: declare B_s convention",
            obligation="state whether B_s is a scale factor, metric coefficient, or separate functional response",
            status="OPEN",
            blocks="normalization comparison",
            discipline="B_s convention changes the coefficient by a factor of two",
        ),
        LedgerObligation(
            name="O3: declare traced dimension",
            obligation="state the sector dimension d and whether the trace is spatial, reduced radial, or other",
            status="OPEN",
            blocks="dimensional counting route",
            discipline="dimension count cannot be chosen from recovery",
        ),
        LedgerObligation(
            name="O4: separate structural identity from adoption",
            obligation="record determinant/volume identities as structural constraints only unless a theorem derives N_trace",
            status="OPEN",
            blocks="adoption drift",
            discipline="structural bookkeeping is not adoption",
        ),
        LedgerObligation(
            name="O5: candidate forms next",
            obligation="define candidate normalization forms visibly before compatibility sieve",
            status="OPEN",
            blocks="source/divergence/membership compatibility tests",
            discipline="do not hide normalization in prose",
        ),
        LedgerObligation(
            name="O6: downstream gates",
            obligation="keep insertion, active O, residual control, and parent equation closed",
            status="NOT_READY",
            blocks="downstream overreach",
            discipline="volume-trace ledger is not insertion or parent closure",
        ),
    ]


def build_conclusions() -> List[LedgerConclusion]:
    return [
        LedgerConclusion(
            name="C1: structural identities",
            conclusion="volume-log and determinant identities constrain candidate trace conventions",
            status="STRUCTURAL_CONSTRAINT",
            meaning="if zeta is volume-log trace, uniform scale and metric-coefficient conventions differ by a factor of two",
        ),
        LedgerConclusion(
            name="C2: convention dependence",
            conclusion="candidate normalization depends on what zeta and B_s are declared to mean",
            status="CONVENTION_DEPENDENT",
            meaning="no final normalization is selected by this ledger",
        ),
        LedgerConclusion(
            name="C3: no adoption",
            conclusion="this ledger adopts no trace-normalization postulate",
            status="NOT_ADOPTED",
            meaning="structural constraints are not explicit theory choice",
        ),
        LedgerConclusion(
            name="C4: no insertion",
            conclusion="B_s/F_zeta insertion remains not ready",
            status="NOT_READY",
            meaning="trace convention ledger is not insertion or coefficient law",
        ),
        LedgerConclusion(
            name="C5: next",
            conclusion="selector rejection ledger or candidate-form script should run next",
            status="OPEN",
            meaning="bad selectors and visible forms must be controlled before compatibility sieve",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Volume-trace / determinant origin ledger problem")

    print("Question:")
    print()
    print("  What structural trace conventions can constrain how B_s reads zeta,")
    print("  without selecting the normalization from recovery, repair, insertion,")
    print("  active O, or parent fit?")
    print()
    print("Discipline:")
    print()
    print("  This script inventories structural trace-origin routes.")
    print("  It adopts no trace-normalization postulate.")
    print("  It selects no final normalization value.")
    print("  It derives no coefficient law and no insertion.")
    print("  It keeps active O, residual control, and parent closure closed.")
    print()
    print("Tiny goblin rule:")
    print("  Measure the cup before naming the drink.")

    with out.governance_assessments():
        out.line(
            "volume-trace ledger opened",
            StatusMark.INFO,
            "structural trace conventions are inventoried before candidate-form and compatibility tests",
        )


def case_1_symbolic_ledger(symbols: VolumeTraceSymbols, out: ScriptOutput) -> None:
    header("Case 1: Volume-trace symbolic ledger")

    print("Trace symbols:")
    print()
    for name in (
        "zeta",
        "d",
        "q_scale",
        "b_metric",
        "N_trace",
        "N_volume",
        "N_metric",
        "N_scale",
        "N_linear",
        "S_recovery",
        "S_repair",
        "S_insertion",
        "S_parent",
    ):
        print(f"  {name} = {getattr(symbols, name)}")

    print()
    print("Structural trace load:")
    print(f"  L_structural_trace = {symbols.L_structural_trace}")
    print()
    print("Forbidden selector load:")
    print(f"  L_forbidden_selectors = {symbols.L_forbidden_selectors}")
    print()
    print("Volume-trace gap:")
    print(f"  L_volume_trace_gap = {symbols.L_volume_trace_gap}")

    with out.derived_results():
        out.line(
            "volume-trace symbolic loads stated",
            StatusMark.OBLIGATION,
            f"L_structural_trace = {symbols.L_structural_trace}; L_forbidden_selectors = {symbols.L_forbidden_selectors}",
        )


def case_2_structural_identities(symbols: VolumeTraceSymbols, out: ScriptOutput, ns=None) -> None:
    header("Case 2: Structural volume/determinant identities")

    print("Assume zeta is a logarithmic spatial volume trace and d is the traced sector dimension.")
    print()
    print("Uniform scale-factor convention:")
    print(f"  q_scale = zeta/d = {symbols.log_scale_from_zeta}")
    print(f"  d*q_scale - zeta = {symbols.volume_identity_residual}")
    print()
    print("Metric-coefficient convention:")
    print(f"  log(B_s)_metric = 2*zeta/d = {symbols.log_metric_from_zeta}")
    print(f"  d*log(B_s)_metric - 2*zeta = {symbols.det_identity_residual}")
    print()
    print("Interpretation:")
    print("  These identities distinguish scale-factor and metric-coefficient conventions.")
    print("  They do not choose which convention B_s uses.")

    volume_ok = is_zero(symbols.volume_identity_residual)
    det_ok = is_zero(symbols.det_identity_residual)

    with out.derived_results():
        out.line(
            "volume-log trace identity",
            StatusMark.PASS if volume_ok else StatusMark.FAIL,
            f"d*(zeta/d) - zeta = {symbols.volume_identity_residual}",
        )
        out.line(
            "determinant metric-coefficient identity",
            StatusMark.PASS if det_ok else StatusMark.FAIL,
            f"d*(2*zeta/d) - 2*zeta = {symbols.det_identity_residual}",
        )

    if ns is not None:
        ns.record_derivation(
            derivation_id="volume_log_trace_identity_residual",
            inputs=[symbols.zeta, symbols.d],
            output=symbols.volume_identity_residual,
            method="simplify(d*(zeta/d) - zeta)",
            status=Status.DERIVED if volume_ok else Status.FAILED,
            record_kind=RecordKind.DERIVATION,
            result_type="identity_residual",
            scope="abstract volume-log trace convention",
        )
        ns.record_derivation(
            derivation_id="determinant_metric_coefficient_identity_residual",
            inputs=[symbols.zeta, symbols.d],
            output=symbols.det_identity_residual,
            method="simplify(d*(2*zeta/d) - 2*zeta)",
            status=Status.DERIVED if det_ok else Status.FAILED,
            record_kind=RecordKind.DERIVATION,
            result_type="identity_residual",
            scope="abstract determinant/unimodular metric-coefficient convention",
        )


def case_3_structural_routes(routes: List[StructuralRoute], out: ScriptOutput) -> None:
    header("Case 3: Structural origin-route ledger")

    for item in routes:
        subheader(item.name)
        print(f"Route: {item.route}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Structural content: {item.structural_content}")
        print(f"Constraint: {item.constraint}")
        print(f"Boundary: {item.boundary}")

    with out.governance_assessments():
        out.line(
            "structural origin routes stated",
            StatusMark.INFO,
            f"{len(routes)} structural routes inventoried; no normalization selected",
        )


def case_4_candidate_conventions(conventions: List[CandidateConvention], out: ScriptOutput) -> None:
    header("Case 4: Candidate convention families")

    for item in conventions:
        subheader(item.name)
        print(f"Convention: {item.convention}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Candidate form: {item.candidate_form}")
        print(f"Requires: {item.requires}")
        print(f"Not equivalent to: {item.not_equivalent_to}")

    with out.governance_assessments():
        out.line(
            "candidate convention families stated",
            StatusMark.DEFER,
            f"{len(conventions)} candidate conventions stated; none selected or adopted",
        )


def case_5_selector_fences(fences: List[SelectorFence], out: ScriptOutput) -> None:
    header("Case 5: Volume-trace selector fences")

    for item in fences:
        subheader(item.name)
        print(f"Rule: {item.rule}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")

    with out.governance_assessments():
        out.line(
            "volume-trace selector fences stated",
            StatusMark.OBLIGATION,
            f"{len(fences)} selector fences stated",
        )


def case_6_obligations(obligations: List[LedgerObligation], out: ScriptOutput) -> None:
    header("Case 6: Volume-trace ledger obligations")

    for item in obligations:
        subheader(item.name)
        print(f"Obligation: {item.obligation}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Blocks: {item.blocks}")
        print(f"Discipline: {item.discipline}")

    with out.unresolved_obligations():
        out.line(
            "volume-trace ledger obligations opened",
            StatusMark.OBLIGATION,
            f"{len(obligations)} obligations stated",
        )


def case_7_conclusions(conclusions: List[LedgerConclusion], out: ScriptOutput) -> None:
    header("Case 7: Volume-trace ledger conclusions")

    for item in conclusions:
        subheader(item.name)
        print(f"Conclusion: {item.conclusion}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Meaning: {item.meaning}")

    with out.governance_assessments():
        out.line(
            "volume-trace ledger conclusion stated",
            StatusMark.PASS,
            "structural trace conventions constrained; no normalization selected or adopted",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")

    print("Volume-trace / determinant origin ledger result:")
    print()
    print("  Structural volume-log and determinant identities distinguish scale-factor and metric-coefficient conventions.")
    print("  If zeta is a volume-log trace in d traced dimensions, a uniform scale-factor convention gives log(B_s)=zeta/d.")
    print("  If B_s is a metric coefficient convention, the corresponding metric log response is 2*zeta/d.")
    print("  These are structural convention constraints, not a final normalization selection.")
    print("  The meaning of zeta, the meaning of B_s, and the traced dimension must be declared before candidate forms are tested.")
    print("  Linearized trace bookkeeping remains linearized only unless extended by a real theorem.")
    print("  Recovery, repair, insertion, active O, and parent fit remain forbidden selectors.")
    print("  No trace-normalization rule is adopted or selected by this ledger.")
    print("  B_s/F_zeta insertion, active O, residual control, and parent equation remain not ready.")
    print()
    print("Possible next script:")
    print("  candidate_trace_normalization_selector_rejection.py")
    print()
    print("Tiny goblin label:")
    print("  Measure the cup before naming the drink.")

    with out.governance_assessments():
        out.line(
            "volume-trace ledger complete",
            StatusMark.PASS,
            "candidate convention constraints stated; selector rejection or candidate-form script should run next",
        )


def record_inventory_marker(ns, symbols: VolumeTraceSymbols) -> None:
    ns.record_derivation(
        derivation_id="g33_trace_normalization_volume_trace_ledger",
        inputs=[
            symbols.N_trace,
            symbols.N_volume,
            symbols.N_metric,
            symbols.N_scale,
            symbols.N_linear,
            symbols.S_recovery,
            symbols.S_repair,
            symbols.S_insertion,
            symbols.S_parent,
        ],
        output=symbols.L_volume_trace_gap,
        method="inventory structural volume-trace, determinant, dimensional, and linearized convention ledgers",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="trace_normalization_volume_trace_ledger_marker",
        scope="Group 33 trace-normalization candidate origin",
        is_placeholder=True,
    )


def record_obligations(ns, obligations: List[LedgerObligation]) -> None:
    obligation_id_map = {
        "O1: declare zeta convention": "g33_declare_zeta_convention",
        "O2: declare B_s convention": "g33_declare_Bs_convention",
        "O3: declare traced dimension": "g33_declare_traced_dimension",
        "O4: separate structural identity from adoption": "g33_structural_identity_not_adoption",
        "O5: candidate forms next": "g33_candidate_forms_visible",
        "O6: downstream gates": "g33_volume_trace_downstream_gates_closed",
    }

    for item in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id_map[item.name],
            script_id=SCRIPT_ID,
            title=item.obligation,
            status=ObligationStatus.OPEN,
            required_by=["g33_trace_normalization_volume_trace_ledger"],
            description=f"{item.discipline} Blocks: {item.blocks}.",
        ))


def record_governance(
    ns,
    routes: List[StructuralRoute],
    conventions: List[CandidateConvention],
    fences: List[SelectorFence],
    conclusions: List[LedgerConclusion],
) -> None:
    obligation_ids = [
        "g33_declare_zeta_convention",
        "g33_declare_Bs_convention",
        "g33_declare_traced_dimension",
        "g33_structural_identity_not_adoption",
        "g33_candidate_forms_visible",
        "g33_volume_trace_downstream_gates_closed",
    ]

    ns.record_route(RouteRecord(
        route_id="g33_volume_trace_origin_route",
        script_id=SCRIPT_ID,
        name="Volume-trace / determinant trace-normalization origin route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "trace-normalization origin problem opened",
            "recovery and repair selectors rejected",
            "trace normalization remains unadopted",
            "downstream gates remain closed",
        ],
    ))

    for item in routes:
        ns.record_claim(ClaimRecord(
            claim_id=f"g33_structural_route_{item.name.split(':')[0].lower()}",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.CANDIDATE_ROUTE,
            statement=(
                f"{item.name}: {item.route}. Structural content: {item.structural_content}. "
                f"Constraint: {item.constraint}. Boundary: {item.boundary}."
            ),
            derivation_ids=["g33_trace_normalization_volume_trace_ledger"],
            obligation_ids=obligation_ids,
        ))

    for item in conventions:
        status = GovernanceStatus.CANDIDATE_ROUTE
        if item.status in {"CONVENTION_DEPENDENT", "LINEARIZED_ONLY"}:
            status = GovernanceStatus.DEFERRED_PENDING_PREREQUISITES

        ns.record_claim(ClaimRecord(
            claim_id=f"g33_candidate_convention_{item.name.split(':')[0].lower()}",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=status,
            statement=(
                f"{item.name}: {item.convention}. Candidate form: {item.candidate_form}. "
                f"Requires: {item.requires}. Not equivalent to: {item.not_equivalent_to}."
            ),
            derivation_ids=["g33_trace_normalization_volume_trace_ledger"],
            obligation_ids=obligation_ids,
        ))

    for item in fences:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"g33_volume_trace_fence_{item.name.split(':')[0].lower()}",
            script_id=SCRIPT_ID,
            branch_id=item.rule,
            status=GovernanceStatus.POLICY_RULE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"{item.rule}. Reason: {item.reason}.",
        ))

    for item in conclusions:
        status = GovernanceStatus.CANDIDATE_ROUTE
        if item.status in {"NOT_ADOPTED", "NOT_READY", "OPEN", "CONVENTION_DEPENDENT"}:
            status = GovernanceStatus.DEFERRED_PENDING_PREREQUISITES
        elif item.status == "STRUCTURAL_CONSTRAINT":
            status = GovernanceStatus.POLICY_RULE

        ns.record_claim(ClaimRecord(
            claim_id=f"g33_volume_trace_conclusion_{item.name.split(':')[0].lower()}",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=status,
            statement=f"{item.conclusion}. Meaning: {item.meaning}.",
            derivation_ids=["g33_trace_normalization_volume_trace_ledger"],
            obligation_ids=obligation_ids,
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g33_trace_normalization_volume_trace_ledger_complete",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "Volume-trace, determinant/unimodular, dimensional, and linearized trace conventions have been inventoried. "
            "The identities constrain candidate forms but do not select or adopt trace normalization. "
            "Downstream gates remain closed."
        ),
        derivation_ids=["g33_trace_normalization_volume_trace_ledger"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Trace-Normalization Volume-Trace Ledger")
    archive, ns, invalidated = prepare_archive()
    ensure_archive_write_dirs(ns)
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    routes = build_structural_routes()
    conventions = build_candidate_conventions()
    fences = build_selector_fences()
    obligations = build_obligations()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbolic_ledger(symbols, out)
    case_2_structural_identities(symbols, out, ns)
    case_3_structural_routes(routes, out)
    case_4_candidate_conventions(conventions, out)
    case_5_selector_fences(fences, out)
    case_6_obligations(obligations, out)
    case_7_conclusions(conclusions, out)
    final_interpretation(out)

    record_inventory_marker(ns, symbols)
    record_obligations(ns, obligations)
    record_governance(ns, routes, conventions, fences, conclusions)

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
