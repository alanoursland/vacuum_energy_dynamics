# Candidate volume trace coefficient origin
#
# Group:
#   29_Bs_Fzeta_coefficient_origin
#
# Script type:
#   VOLUME / TRACE COEFFICIENT-ORIGIN AUDIT
#
# Purpose
# -------
# Test whether zeta = ln sqrt(gamma) and conformal-volume trace algebra
# supply a structural coefficient-origin candidate for B_s/F_zeta.
#
# Locked-door question:
#
#   Does volume/trace algebra fix the safe scalar coefficient?
#
# This script does not derive B_s/F_zeta insertion.
# It does not derive no-overlap sector geometry.
# It does not construct active O.
# It does not derive residual control.
# It does not open the parent equation.
#
# Tiny goblin rule:
#
#   The shape of the mold is not the sword.

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


def status_mark(status: str) -> StatusMark:
    return {
        "ALLOWED_CANDIDATE": StatusMark.DEFER,
        "CANDIDATE": StatusMark.DEFER,
        "PARTIAL": StatusMark.INFO,
        "NOT_DERIVED": StatusMark.DEFER,
        "NOT_READY": StatusMark.DEFER,
        "OPEN": StatusMark.DEFER,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "STRUCTURAL": StatusMark.INFO,
        "UNDERDETERMINED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "g29_problem",
            "29_Bs_Fzeta_coefficient_origin__candidate_coefficient_origin_problem_ledger",
            "g29_coeff_problem",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "g28_summary",
            "28_sector_pairing_no_overlap__candidate_group_28_status_summary",
            "g28_status_summary",
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
    gamma: sp.Symbol
    sqrt_gamma: sp.Symbol
    zeta: sp.Symbol
    delta_zeta: sp.Symbol
    gamma_inv_trace_delta: sp.Symbol
    n: sp.Symbol
    phi: sp.Symbol
    c_volume: sp.Symbol
    c_conformal: sp.Symbol
    c_trace: sp.Symbol
    c_Bs: sp.Symbol
    volume_identity_gap: sp.Symbol
    normalization_gap: sp.Symbol
    dynamics_gap: sp.Symbol
    source_gap: sp.Symbol
    membership_gap: sp.Symbol
    insertion_gap: sp.Symbol
    vt_load: sp.Expr


@dataclass
class VolumeTraceIdentity:
    name: str
    identity: str
    status: str
    result: str
    limitation: str


@dataclass
class VolumeTraceTest:
    name: str
    test: str
    status: str
    result: str
    implication: str


@dataclass
class VolumeTraceRequirement:
    name: str
    requirement: str
    status: str
    needed_for: str
    fails_if: str


@dataclass
class RejectedVolumeTraceShortcut:
    name: str
    shortcut: str
    status: str
    reason: str


@dataclass
class VolumeTraceConclusion:
    name: str
    conclusion: str
    status: str
    meaning: str


def build_symbols() -> VolumeTraceSymbols:
    (
        gamma,
        sqrt_gamma,
        zeta,
        delta_zeta,
        gamma_inv_trace_delta,
        n,
        phi,
        c_volume,
        c_conformal,
        c_trace,
        c_Bs,
        volume_identity_gap,
        normalization_gap,
        dynamics_gap,
        source_gap,
        membership_gap,
        insertion_gap,
    ) = sp.symbols(
        "gamma sqrt_gamma zeta delta_zeta gamma_inv_trace_delta n phi "
        "c_volume c_conformal c_trace c_Bs "
        "volume_identity_gap normalization_gap dynamics_gap source_gap membership_gap insertion_gap",
        real=True,
    )

    vt_load = sp.simplify(
        volume_identity_gap
        + normalization_gap
        + dynamics_gap
        + source_gap
        + membership_gap
        + insertion_gap
    )

    return VolumeTraceSymbols(
        gamma=gamma,
        sqrt_gamma=sqrt_gamma,
        zeta=zeta,
        delta_zeta=delta_zeta,
        gamma_inv_trace_delta=gamma_inv_trace_delta,
        n=n,
        phi=phi,
        c_volume=c_volume,
        c_conformal=c_conformal,
        c_trace=c_trace,
        c_Bs=c_Bs,
        volume_identity_gap=volume_identity_gap,
        normalization_gap=normalization_gap,
        dynamics_gap=dynamics_gap,
        source_gap=source_gap,
        membership_gap=membership_gap,
        insertion_gap=insertion_gap,
        vt_load=vt_load,
    )


def build_identities() -> List[VolumeTraceIdentity]:
    return [
        VolumeTraceIdentity(
            name="I1: determinant variation",
            identity="delta ln sqrt(gamma) = 1/2 gamma^ij delta gamma_ij",
            status="STRUCTURAL",
            result="volume scalar responds to spatial metric trace",
            limitation="identity alone does not define B_s dynamics or source routing",
        ),
        VolumeTraceIdentity(
            name="I2: zeta as log-volume scalar",
            identity="zeta = ln sqrt(gamma)",
            status="ALLOWED_CANDIDATE",
            result="zeta can be treated as volume-trace scalar candidate",
            limitation="does not by itself determine F_zeta insertion",
        ),
        VolumeTraceIdentity(
            name="I3: conformal volume split",
            identity="gamma_ij = exp(2 zeta / n) bar_gamma_ij with det bar_gamma fixed",
            status="STRUCTURAL",
            result="zeta carries pure conformal/volume trace in n spatial dimensions",
            limitation="normalization depends on convention and target role",
        ),
        VolumeTraceIdentity(
            name="I4: three-dimensional conformal split",
            identity="gamma_ij = exp(2 zeta / 3) bar_gamma_ij",
            status="ALLOWED_CANDIDATE",
            result="in three spatial dimensions, zeta can parametrize volume trace",
            limitation="does not decide ordinary source coefficient",
        ),
        VolumeTraceIdentity(
            name="I5: B_s coefficient",
            identity="B_s coefficient c_Bs is fixed by volume trace alone",
            status="NOT_DERIVED",
            result="not established",
            limitation="B_s response requires dynamics/source/boundary/divergence discipline",
        ),
    ]


def build_tests() -> List[VolumeTraceTest]:
    return [
        VolumeTraceTest(
            name="T1: volume identity availability",
            test="does the theory have a structural volume-trace identity?",
            status="PARTIAL",
            result="yes: delta zeta has trace form",
            implication="volume/trace origin is a real structural candidate",
        ),
        VolumeTraceTest(
            name="T2: coefficient normalization",
            test="does volume identity alone fix the numerical B_s/F_zeta coefficient?",
            status="UNDERDETERMINED",
            result="not fully; normalization depends on how B_s uses the scalar response",
            implication="volume trace is candidate origin, not insertion theorem",
        ),
        VolumeTraceTest(
            name="T3: safe trace membership",
            test="does volume trace prove zeta_Bs -> T_zeta?",
            status="UNDERDETERMINED",
            result="not fully; it supports the anchor but does not prove sector membership",
            implication="membership bridge remains open",
        ),
        VolumeTraceTest(
            name="T4: residual handling",
            test="does volume trace kill or inert zeta/kappa residuals?",
            status="REJECTED",
            result="no",
            implication="residual discipline remains open",
        ),
        VolumeTraceTest(
            name="T5: source behavior",
            test="does volume trace determine source no-double-counting?",
            status="NOT_DERIVED",
            result="no",
            implication="source routing remains separate",
        ),
        VolumeTraceTest(
            name="T6: divergence behavior",
            test="does volume trace determine divergence-safe sector behavior?",
            status="NOT_DERIVED",
            result="no",
            implication="divergence-compatible coefficient origin remains future target",
        ),
        VolumeTraceTest(
            name="T7: insertion theorem",
            test="does volume trace derive B_s/F_zeta insertion?",
            status="NOT_DERIVED",
            result="no",
            implication="insertion gate remains closed",
        ),
    ]


def build_requirements() -> List[VolumeTraceRequirement]:
    return [
        VolumeTraceRequirement(
            name="R1: normalize B_s target",
            requirement="state how B_s reads the volume-trace scalar",
            status="REQUIRED",
            needed_for="coefficient origin",
            fails_if="volume identity is equated with insertion",
        ),
        VolumeTraceRequirement(
            name="R2: membership bridge",
            requirement="derive whether volume trace forces zeta_Bs -> T_zeta",
            status="REQUIRED",
            needed_for="sector membership improvement",
            fails_if="candidate anchor is promoted to theorem",
        ),
        VolumeTraceRequirement(
            name="R3: source discipline",
            requirement="show coefficient does not carry hidden ordinary source load",
            status="REQUIRED",
            needed_for="source no-double-counting",
            fails_if="volume coefficient becomes source reservoir",
        ),
        VolumeTraceRequirement(
            name="R4: residual discipline",
            requirement="show volume trace does not kill residuals by label",
            status="REQUIRED",
            needed_for="residual-control honesty",
            fails_if="residuals are erased by coefficient origin",
        ),
        VolumeTraceRequirement(
            name="R5: guardrail discipline",
            requirement="preserve boundary/current/mass/support visibility",
            status="REQUIRED",
            needed_for="field-equation usability",
            fails_if="volume trace hides guardrail failure",
        ),
        VolumeTraceRequirement(
            name="R6: recovery independence",
            requirement="do not choose normalization from AB=1, Schwarzschild, gamma, or weak-field success",
            status="REQUIRED",
            needed_for="anti-smuggling",
            fails_if="recovery selects coefficient",
        ),
    ]


def build_shortcuts() -> List[RejectedVolumeTraceShortcut]:
    return [
        RejectedVolumeTraceShortcut(
            name="F1: identity as insertion",
            shortcut="delta ln sqrt(gamma) identity treated as B_s/F_zeta insertion theorem",
            status="REJECTED",
            reason="volume identity is kinematic/structural, not full field equation insertion",
        ),
        RejectedVolumeTraceShortcut(
            name="F2: conformal split as dynamics",
            shortcut="conformal trace split treated as dynamic source law",
            status="REJECTED",
            reason="conformal decomposition does not determine source routing",
        ),
        RejectedVolumeTraceShortcut(
            name="F3: trace identity as residual control",
            shortcut="volume trace origin kills zeta/kappa residuals",
            status="REJECTED",
            reason="residuals are not killed by trace algebra",
        ),
        RejectedVolumeTraceShortcut(
            name="F4: volume trace as sector theorem",
            shortcut="zeta_Bs -> T_zeta treated as proven from volume identity alone",
            status="REJECTED",
            reason="membership bridge remains underdetermined",
        ),
        RejectedVolumeTraceShortcut(
            name="F5: recovery normalization",
            shortcut="choose trace normalization because AB=1, Schwarzschild, or gamma works",
            status="REJECTED",
            reason="recovery may audit but not choose coefficient",
        ),
        RejectedVolumeTraceShortcut(
            name="F6: parent closure from trace",
            shortcut="volume trace identity opens parent field equation",
            status="REJECTED",
            reason="parent equation remains closed",
        ),
    ]


def build_conclusions() -> List[VolumeTraceConclusion]:
    return [
        VolumeTraceConclusion(
            name="C1: volume trace",
            conclusion="volume/trace algebra is a real structural candidate origin",
            status="PARTIAL",
            meaning="zeta has a natural spatial volume-trace interpretation",
        ),
        VolumeTraceConclusion(
            name="C2: coefficient",
            conclusion="B_s/F_zeta coefficient is not fixed by volume identity alone",
            status="UNDERDETERMINED",
            meaning="normalization and role still require additional law",
        ),
        VolumeTraceConclusion(
            name="C3: safe membership",
            conclusion="zeta_Bs -> T_zeta is supported but not proven",
            status="CANDIDATE",
            meaning="safe trace anchor is stronger structurally, but still not theorem",
        ),
        VolumeTraceConclusion(
            name="C4: downstream gates",
            conclusion="insertion, residual control, active O, and parent closure remain closed",
            status="NOT_READY",
            meaning="volume/trace origin cannot be upgraded to downstream theorem",
        ),
        VolumeTraceConclusion(
            name="C5: next route",
            conclusion="recovery-smuggling filter should run next",
            status="OPEN",
            meaning="normalization candidates must be filtered against recovery selection",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Volume/trace coefficient-origin problem")
    print("Question:")
    print()
    print("  Does volume/trace algebra fix the safe scalar coefficient?")
    print()
    print("Discipline:")
    print()
    print("  Volume identity is not insertion.")
    print("  Conformal split is not source routing.")
    print("  Trace algebra is not residual control.")
    print()
    print("Tiny goblin rule:")
    print("  The shape of the mold is not the sword.")

    with out.governance_assessments():
        out.line(
            "volume/trace coefficient-origin audit opened",
            StatusMark.INFO,
            "testing zeta volume-trace structure without deriving insertion",
        )


def case_1_symbolic_ledger(symbols: VolumeTraceSymbols, out: ScriptOutput) -> None:
    header("Case 1: Volume/trace symbolic ledger")
    print("Volume/trace symbols:")
    print()
    for name in [
        "gamma",
        "sqrt_gamma",
        "zeta",
        "delta_zeta",
        "gamma_inv_trace_delta",
        "n",
        "phi",
        "c_volume",
        "c_conformal",
        "c_trace",
        "c_Bs",
    ]:
        print(f"  {name} = {sp.sstr(getattr(symbols, name))}")
    print()
    print("Volume/trace load:")
    print()
    print(f"  L_volume_trace = {sp.sstr(symbols.vt_load)}")
    print()
    print("Interpretation:")
    print()
    print("  Volume identity supplies structural trace information.")
    print("  It does not by itself supply B_s/F_zeta insertion.")

    with out.derived_results():
        out.line(
            "volume/trace load stated",
            StatusMark.OBLIGATION,
            f"L_volume_trace = {sp.sstr(symbols.vt_load)}",
        )


def case_2_identities(items: List[VolumeTraceIdentity], out: ScriptOutput) -> None:
    header("Case 2: Volume/trace identities")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Identity: {item.identity}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Result: {item.result}")
        print(f"Limitation: {item.limitation}")

    with out.governance_assessments():
        out.line(
            "volume/trace identities classified",
            StatusMark.DEFER,
            f"{len(items)} volume/trace identities classified",
        )


def case_3_tests(items: List[VolumeTraceTest], out: ScriptOutput) -> None:
    header("Case 3: Volume/trace coefficient tests")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Test: {item.test}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Result: {item.result}")
        print(f"Implication: {item.implication}")

    with out.governance_assessments():
        out.line(
            "volume/trace coefficient tests completed",
            StatusMark.DEFER,
            "volume trace is structural candidate; coefficient remains underdetermined",
        )


def case_4_requirements(items: List[VolumeTraceRequirement], out: ScriptOutput) -> None:
    header("Case 4: Volume/trace coefficient requirements")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Requirement: {item.requirement}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Needed for: {item.needed_for}")
        print(f"Fails if: {item.fails_if}")

    with out.unresolved_obligations():
        out.line(
            "volume/trace coefficient requirements stated",
            StatusMark.OBLIGATION,
            f"{len(items)} requirements remain open after volume/trace audit",
        )


def case_5_shortcuts(items: List[RejectedVolumeTraceShortcut], out: ScriptOutput) -> None:
    header("Case 5: Rejected volume/trace shortcuts")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Shortcut: {item.shortcut}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Reason: {item.reason}")

    with out.counterexamples():
        out.line(
            "volume/trace shortcuts rejected",
            StatusMark.FAIL,
            "identity-as-insertion, split-as-dynamics, trace-as-residual-control, sector theorem, recovery normalization, and parent closure are rejected",
        )


def case_6_conclusions(items: List[VolumeTraceConclusion], out: ScriptOutput) -> None:
    header("Case 6: Volume/trace coefficient conclusions")
    for item in items:
        print()
        print("-" * 120)
        print(item.name)
        print("-" * 120)
        print(f"Conclusion: {item.conclusion}")
        print(f"[{status_mark(item.status).value}] {item.name}: {item.status}")
        print(f"Meaning: {item.meaning}")

    with out.governance_assessments():
        out.line(
            "volume/trace coefficient conclusion stated",
            StatusMark.DEFER,
            "volume/trace supports coefficient-origin candidate but does not fix insertion",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Volume/trace coefficient-origin result:")
    print()
    print("  Volume/trace algebra is a real structural candidate origin.")
    print("  zeta has a natural spatial volume-trace interpretation.")
    print("  determinant variation gives delta zeta = 1/2 gamma^ij delta gamma_ij.")
    print("  conformal split supports zeta as pure spatial volume/trace scalar.")
    print("  B_s/F_zeta coefficient is not fixed by volume identity alone.")
    print("  zeta_Bs -> T_zeta is supported but not proven.")
    print("  source routing remains not derived.")
    print("  divergence-safe behavior remains not derived.")
    print("  residual control is not derived.")
    print("  B_s/F_zeta insertion is not derived.")
    print("  active O and parent equation remain not ready.")
    print()
    print("Possible next script:")
    print("  candidate_recovery_smuggling_filter.py")
    print()
    print("Tiny goblin label:")
    print("  The shape of the mold is not the sword.")

    with out.governance_assessments():
        out.line(
            "volume/trace coefficient-origin audit complete",
            StatusMark.PASS,
            "volume/trace is structural candidate; recovery-smuggling filter should run next",
        )


def record_derivations(ns, symbols: VolumeTraceSymbols) -> None:
    ns.record_derivation(
        derivation_id="g29_volume_trace",
        inputs=[
            symbols.volume_identity_gap,
            symbols.normalization_gap,
            symbols.dynamics_gap,
            symbols.source_gap,
            symbols.membership_gap,
            symbols.insertion_gap,
        ],
        output=symbols.vt_load,
        method="audit volume/trace algebra as coefficient-origin candidate without deriving insertion",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="volume_trace_coefficient_marker",
        scope="Group 29 B_s/F_zeta coefficient origin",
        is_placeholder=True,
    )


def record_obligations(ns) -> None:
    obligations = [
        ("g29_vt_normalize", "Define how B_s reads volume-trace scalar"),
        ("g29_vt_membership", "Derive or reject zeta_Bs -> T_zeta from volume trace"),
        ("g29_vt_source", "Prevent source hiding in coefficient"),
        ("g29_vt_residual", "Prevent residual erasure by trace algebra"),
        ("g29_vt_guardrails", "Preserve boundary/current/mass/support visibility"),
        ("g29_vt_recovery", "Reject recovery-selected normalization"),
        ("g29_vt_insertion", "Keep B_s/F_zeta insertion gate closed"),
        ("g29_vt_next", "Run recovery-smuggling filter next"),
    ]

    for obligation_id, title in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["g29_vt_route"],
            description=(
                "Volume/trace algebra is a structural candidate origin but does not derive insertion or complete coefficient law."
            ),
        ))


def record_governance(ns) -> None:
    obligation_ids = [
        "g29_vt_normalize",
        "g29_vt_membership",
        "g29_vt_source",
        "g29_vt_residual",
        "g29_vt_guardrails",
        "g29_vt_recovery",
        "g29_vt_insertion",
        "g29_vt_next",
    ]

    ns.record_route(RouteRecord(
        route_id="g29_vt_route",
        script_id=SCRIPT_ID,
        name="Group 29 volume/trace coefficient-origin route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "volume/trace algebra is treated as structural candidate only",
            "B_s/F_zeta insertion is not claimed",
            "zeta_Bs -> T_zeta remains not fully proven",
            "source, residual, guardrail, recovery, active O, and parent gates remain controlled",
            "recovery-smuggling filter runs next",
        ],
    ))

    for branch_id in [
        "identity_as_insertion",
        "conformal_split_as_dynamics",
        "trace_identity_as_residual_control",
        "volume_trace_as_sector_theorem",
        "recovery_normalization",
        "parent_closure_from_trace",
        "active_O_from_trace",
        "source_routing_from_trace",
    ]:
        ns.record_branch_decision(BranchDecisionRecord(
            decision_id=f"reject_{branch_id}",
            script_id=SCRIPT_ID,
            branch_id=branch_id,
            status=GovernanceStatus.REJECTED_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            obligation_ids=obligation_ids,
            description=f"Reject {branch_id}; volume/trace audit is not insertion, source routing, residual control, active O, or parent closure.",
        ))

    ns.record_claim(ClaimRecord(
        claim_id="g29_volume_trace_partial",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Volume/trace algebra is a real structural candidate origin: zeta has a natural spatial volume-trace interpretation, determinant variation gives "
            "delta zeta = 1/2 gamma^ij delta gamma_ij, and conformal split supports zeta as pure spatial volume/trace scalar. "
            "However, B_s/F_zeta coefficient is not fixed by volume identity alone; zeta_Bs -> T_zeta is supported but not proven; source routing, divergence safety, residual control, "
            "B_s/F_zeta insertion, active O, and parent equation remain not derived."
        ),
        derivation_ids=["g29_volume_trace"],
        obligation_ids=obligation_ids,
    ))


def main() -> None:
    header("Candidate Volume Trace Coefficient Origin")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    symbols = build_symbols()
    identities = build_identities()
    tests = build_tests()
    requirements = build_requirements()
    shortcuts = build_shortcuts()
    conclusions = build_conclusions()

    case_0_problem_statement(out)
    case_1_symbolic_ledger(symbols, out)
    case_2_identities(identities, out)
    case_3_tests(tests, out)
    case_4_requirements(requirements, out)
    case_5_shortcuts(shortcuts, out)
    case_6_conclusions(conclusions, out)
    final_interpretation(out)

    ensure_archive_write_dirs(ns)
    record_derivations(ns, symbols)
    record_obligations(ns)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
