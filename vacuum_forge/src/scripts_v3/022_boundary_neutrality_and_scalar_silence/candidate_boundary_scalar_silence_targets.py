# Candidate boundary scalar silence targets
#
# Group:
#   22_boundary_neutrality_and_scalar_silence
#
# Script type:
#   REQUIREMENTS / DIAGNOSTIC
#
# Purpose
# -------
# Open Group 22 by making the boundary-neutrality and exterior scalar-silence
# targets explicit.
#
# Locked-door question:
#
#   What exactly must vanish for boundary neutrality and exterior scalar silence?
#
# This script does not prove boundary neutrality.
# It does not prove scalar silence.
# It does not define a parent field equation.
# It does not assume an active O, H tensor, dark patch, shell source, or
# recovery-tuned smoothing law.
#
# It records the reduced target ledger inherited from Group 21:
#
#   delta F_A|boundary,non-A = 0
#   C_zeta = 0
#   C_kappa = 0
#   C_JV = 0
#   C_curv = 0
#   C_H = 0
#   I_nonA = 0
#   no shell source
#   no recovery-tuned smoothing
#   no active O
#   no H insertion

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


# =============================================================================
# Utilities
# =============================================================================


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def status_mark(status: str) -> StatusMark:
    return {
        "CLOSED_REDUCED": StatusMark.PASS,
        "CONSTRAINED": StatusMark.INFO,
        "DEFER": StatusMark.DEFER,
        "FORBIDDEN": StatusMark.FAIL,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "SAFE_IF": StatusMark.INFO,
        "THEOREM_TARGET": StatusMark.DEFER,
        "UNRESOLVED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    dependencies = [
        (
            "group21_status_summary_dependency_22",
            "021_source_routing_and_mass_neutrality__candidate_group_21_source_routing_status_summary",
            "group21_source_routing_status_summary_marker_21",
            RecordKind.INVENTORY_MARKER,
        ),
        (
            "A_sector_mass_definition_dependency_22",
            "021_source_routing_and_mass_neutrality__candidate_a_sector_mass_charge_definition",
            "A_sector_mass_definition_21",
            RecordKind.DERIVATION,
        ),
        (
            "residual_scalar_tail_flux_dependency_22",
            "021_source_routing_and_mass_neutrality__candidate_residual_scalar_tail_flux_audit",
            "residual_scalar_tail_flux_1_over_r_21",
            RecordKind.DERIVATION,
        ),
        (
            "boundary_tail_delta_A_flux_dependency_22",
            "021_source_routing_and_mass_neutrality__candidate_boundary_flux_mass_preservation",
            "boundary_tail_delta_A_flux_21",
            RecordKind.DERIVATION,
        ),
        (
            "source_routing_no_double_counting_dependency_22",
            "021_source_routing_and_mass_neutrality__candidate_source_routing_no_double_counting",
            "source_routing_no_double_counting_marker_21",
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


# =============================================================================
# Data models
# =============================================================================


@dataclass
class BoundarySilenceExpressionSet:
    r: sp.Symbol
    G: sp.Symbol
    c: sp.Symbol
    C: sp.Symbol
    q: sp.Symbol
    I: sp.Symbol
    phi_tail: sp.Expr
    F_phi: sp.Expr
    delta_A_boundary: sp.Expr
    delta_F_A_boundary: sp.Expr
    delta_M_A_boundary: sp.Expr
    j_radial: sp.Expr
    current_flux: sp.Expr
    scalar_flux_residual: sp.Expr
    boundary_flux_residual: sp.Expr
    boundary_mass_residual: sp.Expr
    current_flux_residual: sp.Expr


@dataclass
class SilenceTargetEntry:
    name: str
    target: str
    reason: str
    status: str
    failure_if: str
    consequence: str


@dataclass
class ForbiddenShortcutEntry:
    name: str
    forbidden_route: str
    forbidden_use: str
    status: str
    consequence: str


# =============================================================================
# Builders
# =============================================================================


def build_expressions() -> BoundarySilenceExpressionSet:
    r = sp.Symbol("r", positive=True)
    G = sp.Symbol("G", positive=True)
    c = sp.Symbol("c", positive=True)
    C = sp.Symbol("C", real=True)
    q = sp.Symbol("q", real=True)
    I = sp.Symbol("I", real=True)

    phi_tail = C / r
    F_phi = sp.simplify(4 * sp.pi * r**2 * sp.diff(phi_tail, r))

    delta_A_boundary = q / r
    delta_F_A_boundary = sp.simplify(4 * sp.pi * r**2 * sp.diff(delta_A_boundary, r))
    delta_M_A_boundary = sp.simplify(c**2 * delta_F_A_boundary / (8 * sp.pi * G))

    j_radial = I / (4 * sp.pi * r**2)
    current_flux = sp.simplify(4 * sp.pi * r**2 * j_radial)

    return BoundarySilenceExpressionSet(
        r=r,
        G=G,
        c=c,
        C=C,
        q=q,
        I=I,
        phi_tail=phi_tail,
        F_phi=F_phi,
        delta_A_boundary=delta_A_boundary,
        delta_F_A_boundary=delta_F_A_boundary,
        delta_M_A_boundary=delta_M_A_boundary,
        j_radial=j_radial,
        current_flux=current_flux,
        scalar_flux_residual=sp.simplify(F_phi + 4 * sp.pi * C),
        boundary_flux_residual=sp.simplify(delta_F_A_boundary + 4 * sp.pi * q),
        boundary_mass_residual=sp.simplify(delta_M_A_boundary + c**2 * q / (2 * G)),
        current_flux_residual=sp.simplify(current_flux - I),
    )


def build_targets() -> List[SilenceTargetEntry]:
    return [
        SilenceTargetEntry(
            name="S1: non-A boundary A-flux neutrality",
            target="delta F_A|boundary,non-A = 0",
            reason="non-A boundary behavior must not shift the protected A-sector exterior mass charge",
            status="REQUIRED",
            failure_if="boundary smoothing, insertion, or residual behavior changes exterior A'",
            consequence="boundary mass preservation remains theorem-targeted",
        ),
        SilenceTargetEntry(
            name="S2: zeta scalar silence",
            target="C_zeta = 0",
            reason="a zeta residual 1/r tail carries nonzero exterior scalar flux",
            status="REQUIRED",
            failure_if="zeta_tail = C_zeta/r with C_zeta != 0 survives as metric/source effect",
            consequence="zeta residual must be killed, non-metric, compact-neutral, or theorem-routed",
        ),
        SilenceTargetEntry(
            name="S3: kappa scalar silence",
            target="C_kappa = 0",
            reason="a kappa residual 1/r tail carries nonzero exterior scalar flux",
            status="REQUIRED",
            failure_if="kappa_tail = C_kappa/r with C_kappa != 0 survives as metric/source effect",
            consequence="kappa remains diagnostic/suppressed/non-metric unless a theorem derives otherwise",
        ),
        SilenceTargetEntry(
            name="S4: J_V residue silence",
            target="C_JV = 0",
            reason="an unresolved J_V-induced scalar residue would be a hidden scalar charge",
            status="REQUIRED",
            failure_if="J_V leaves C_JV/r while J_V itself remains undefined",
            consequence="J_V residue must vanish or remain strictly diagnostic/non-metric",
        ),
        SilenceTargetEntry(
            name="S5: curvature residue silence",
            target="C_curv = 0",
            reason="curvature diagnostics cannot leave an exterior scalar mass tail",
            status="REQUIRED",
            failure_if="A_curv/e_curv/J_curv residue becomes C_curv/r exterior source behavior",
            consequence="curvature remains diagnostic/accounting/branch-filter unless source-neutral dynamics are derived",
        ),
        SilenceTargetEntry(
            name="S6: correction-tensor trace silence",
            target="C_H = 0",
            reason="H trace leakage would mimic hidden scalar mass correction",
            status="REQUIRED",
            failure_if="H trace leakage phi_H = C_H/r survives outside",
            consequence="H_curv/H_exch remain non-insertable unless future tensor theorem proves trace neutrality",
        ),
        SilenceTargetEntry(
            name="S7: non-A far-zone current silence",
            target="I_nonA = 0",
            reason="j^r = I/(4*pi*r^2) carries sphere flux I",
            status="REQUIRED",
            failure_if="J_V/J_sub/J_exch/J_curv/H far-zone current flux is nonzero in ordinary exterior",
            consequence="non-A far-zone currents must vanish or be theorem-routed as neutral transport",
        ),
        SilenceTargetEntry(
            name="S8: no shell source",
            target="no shell source",
            reason="a derivative jump or shell can hide boundary mass/scalar flux",
            status="REQUIRED",
            failure_if="sharp support, smoothing, or insertion produces a shell contribution without independent source law",
            consequence="compact support is unsafe unless matching/no-shell conditions are derived",
        ),
        SilenceTargetEntry(
            name="S9: no recovery-tuned smoothing",
            target="no recovery-tuned smoothing",
            reason="boundary behavior must not be chosen from Schwarzschild, PPN, AB, gamma_like, or B=1/A recovery",
            status="REQUIRED",
            failure_if="smoothing is selected after a recovery or boundary leakage problem appears",
            consequence="recovery remains downstream diagnostic, not construction rule",
        ),
        SilenceTargetEntry(
            name="S10: no active O",
            target="no active O",
            reason="Group 20 did not derive a universal active no-overlap operator",
            status="REQUIRED",
            failure_if="O is used as scalar-tail eraser, boundary filter, source separator, or shell-source suppressor",
            consequence="no-overlap remains theorem-targeted; diagnostic labels only are safe",
        ),
        SilenceTargetEntry(
            name="S11: no H insertion",
            target="no H insertion",
            reason="Group 21 left H_curv/H_exch non-insertable",
            status="REQUIRED",
            failure_if="H acts as boundary counterterm, scalar-tail cancellation, M_ext correction, or Bianchi paint",
            consequence="H labels remain diagnostic audit placeholders only",
        ),
    ]


def build_forbidden_shortcuts() -> List[ForbiddenShortcutEntry]:
    return [
        ForbiddenShortcutEntry(
            name="F1: smoothing repair",
            forbidden_route="smoothing selected to preserve mass or recovery",
            forbidden_use="boundary behavior chosen after leakage or recovery failure",
            status="REJECTED",
            consequence="smoothing cannot be a boundary purse",
        ),
        ForbiddenShortcutEntry(
            name="F2: O scalar-tail eraser",
            forbidden_route="O removes scalar tails by declaration",
            forbidden_use="projection language used without domain/kernel/image/boundary law",
            status="REJECTED",
            consequence="O cannot provide scalar silence by naming itself",
        ),
        ForbiddenShortcutEntry(
            name="F3: H boundary counterterm",
            forbidden_route="H absorbs shell or boundary flux",
            forbidden_use="undefined correction tensor inserted as boundary repair",
            status="REJECTED",
            consequence="H remains non-insertable",
        ),
        ForbiddenShortcutEntry(
            name="F4: hidden shell source",
            forbidden_route="sharp support hides derivative jump",
            forbidden_use="compact support imposed without matching/no-shell theorem",
            status="REJECTED",
            consequence="compact support must show smooth edge, not hide flux at the seam",
        ),
        ForbiddenShortcutEntry(
            name="F5: recovery-tuned boundary condition",
            forbidden_route="boundary condition chosen from Schwarzschild/PPN/gamma_like/AB/B=1/A",
            forbidden_use="recovery target used as construction rule",
            status="REJECTED",
            consequence="recovery tests may audit, not build, boundary neutrality",
        ),
        ForbiddenShortcutEntry(
            name="F6: dark boundary patch",
            forbidden_route="dark label absorbs ordinary boundary/scalar failure",
            forbidden_use="optional sector used to patch ordinary leakage",
            status="REJECTED",
            consequence="dark sector is not an ordinary boundary patch",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Boundary/scalar silence target problem")
    print("Question:")
    print()
    print("  What exactly must vanish for boundary neutrality and exterior scalar silence?")
    print()
    print("Reference discipline:")
    print()
    print("  A-sector mass charge remains the reduced ordinary exterior reference.")
    print("  Group 21 protected the mass coin but did not prove boundary neutrality.")
    print("  Group 22 starts by making the vanishing targets explicit.")
    print("  No active O, no H insertion, no shell source, no dark patch,")
    print("  and no recovery-tuned smoothing is assumed.")
    print("  This script records a target ledger, not a theorem.")

    with out.governance_assessments():
        out.line(
            "boundary/scalar silence target audit opened",
            StatusMark.INFO,
            "Group 22 starts by stating the required vanishing targets explicitly",
        )


def case_1_reduced_witnesses(exprs: BoundarySilenceExpressionSet, out: ScriptOutput) -> None:
    header("Case 1: Reduced danger witnesses")

    print("Residual scalar tail:")
    print()
    print(f"  phi_tail(r) = {sp.sstr(exprs.phi_tail)}")
    print(f"  F_phi = 4*pi*r^2*phi_tail' = {sp.sstr(exprs.F_phi)}")
    print(f"  residual F_phi + 4*pi*C = {sp.sstr(exprs.scalar_flux_residual)}")
    print()

    print("Boundary A-tail:")
    print()
    print(f"  delta_A_boundary(r) = {sp.sstr(exprs.delta_A_boundary)}")
    print(f"  delta_F_A = 4*pi*r^2*delta_A_boundary' = {sp.sstr(exprs.delta_F_A_boundary)}")
    print(f"  delta_M_A = c^2*delta_F_A/(8*pi*G) = {sp.sstr(exprs.delta_M_A_boundary)}")
    print(f"  residual delta_F_A + 4*pi*q = {sp.sstr(exprs.boundary_flux_residual)}")
    print(f"  residual delta_M_A + c^2*q/(2*G) = {sp.sstr(exprs.boundary_mass_residual)}")
    print()

    print("Far-zone radial current:")
    print()
    print(f"  j^r = {sp.sstr(exprs.j_radial)}")
    print(f"  Phi = 4*pi*r^2*j^r = {sp.sstr(exprs.current_flux)}")
    print(f"  residual Phi - I = {sp.sstr(exprs.current_flux_residual)}")
    print()

    with out.derived_results():
        out.line(
            "residual scalar-tail flux witness",
            StatusMark.PASS if is_zero(exprs.scalar_flux_residual) else StatusMark.FAIL,
            f"F_phi = {sp.sstr(exprs.F_phi)}",
        )
        out.line(
            "boundary A-tail mass-shift witness",
            StatusMark.PASS if is_zero(exprs.boundary_mass_residual) else StatusMark.FAIL,
            f"delta_M_A = {sp.sstr(exprs.delta_M_A_boundary)}",
        )
        out.line(
            "far-zone current flux witness",
            StatusMark.PASS if is_zero(exprs.current_flux_residual) else StatusMark.FAIL,
            f"Phi = {sp.sstr(exprs.current_flux)}",
        )


def case_2_silence_target_ledger(targets: List[SilenceTargetEntry], out: ScriptOutput) -> None:
    header("Case 2: Boundary/scalar silence target ledger")
    for entry in targets:
        print()
        print("-" * 120)
        print(entry.name)
        print("-" * 120)
        print(f"Target: {entry.target}")
        print(f"Reason: {entry.reason}")
        print(f"[{status_mark(entry.status).value}] {entry.name}: {entry.status}")
        print(f"Failure if: {entry.failure_if}")
        print(f"Consequence: {entry.consequence}")

    with out.governance_assessments():
        out.line(
            "boundary/scalar silence targets populated",
            StatusMark.PASS,
            f"{len(targets)} vanishing/no-repair targets stated for Group 22",
        )


def case_3_forbidden_shortcuts(shortcuts: List[ForbiddenShortcutEntry], out: ScriptOutput) -> None:
    header("Case 3: Forbidden boundary/scalar-silence shortcuts")
    for entry in shortcuts:
        print()
        print("-" * 120)
        print(entry.name)
        print("-" * 120)
        print(f"Forbidden route: {entry.forbidden_route}")
        print(f"Forbidden use: {entry.forbidden_use}")
        print(f"[{status_mark(entry.status).value}] {entry.name}: {entry.status}")
        print(f"Consequence: {entry.consequence}")

    with out.counterexamples():
        out.line(
            "boundary/scalar silence repair shortcuts rejected",
            StatusMark.FAIL,
            "smoothing, O, H, shell hiding, recovery tuning, and dark patches do not prove silence",
        )


def case_4_theorem_targets(out: ScriptOutput) -> None:
    header("Case 4: Theorem obligations opened")
    print("Group 22 theorem obligations:")
    print()
    print("  derive no-shell boundary condition")
    print("  derive residual scalar silence")
    print("  derive non-A boundary A-flux neutrality")
    print("  derive far-zone non-A current flux silence")
    print("  derive compact-support matching law")
    print("  derive diagnostic residual non-reentry")
    print("  derive no recovery-tuned boundary data")
    print("  derive source-routing compatibility with boundary/scalar silence")
    print()
    print("These obligations are prerequisites for claiming boundary neutrality.")

    with out.unresolved_obligations():
        out.line(
            "boundary/scalar silence theorem obligations opened",
            StatusMark.OBLIGATION,
            "vanishing targets are explicit but not derived",
        )


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("The boundary/scalar silence target audit fails if a later script allows:")
    print()
    print("1. boundary neutrality by assumption")
    print("2. scalar silence by assumption")
    print("3. O as scalar-tail eraser")
    print("4. H as boundary counterterm")
    print("5. smoothing chosen after recovery failure")
    print("6. shell source hidden by derivative jump")
    print("7. compact support without matching law")
    print("8. residual-kill treated as derived no-overlap")
    print("9. dark label boundary patch")
    print("10. curvature or exchange boundary repair")
    print("11. J_V boundary current without definition")
    print("12. source cancellation across non-A sectors")
    print("13. recovery-selected boundary condition")

    with out.governance_assessments():
        out.line(
            "boundary/scalar silence overclaim controls stated",
            StatusMark.OBLIGATION,
            "future scripts must not treat target conditions as solved claims",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("Group 22 starts from explicit vanishing targets:")
    print()
    print("  delta F_A|boundary,non-A = 0")
    print("  C_zeta = C_kappa = C_JV = C_curv = C_H = 0")
    print("  I_nonA = 0")
    print("  no shell source")
    print("  no recovery-tuned smoothing")
    print("  no active O")
    print("  no H insertion")
    print()
    print("The reduced witnesses are:")
    print()
    print("  phi_tail = C/r -> F_phi = -4*pi*C")
    print("  delta_A_boundary = q/r -> delta_M_A = -c^2*q/(2G)")
    print("  j^r = I/(4*pi*r^2) -> Phi = I")
    print()
    print("This script does not prove silence.")
    print("It defines the target ledger for the next Group 22 scripts.")
    print()
    print("Possible next script:")
    print("  candidate_smooth_compact_support_no_shell_conditions.py")
    print()
    print("Tiny goblin label:")
    print("  No boundary purse. No tail ghost. Show the empty edge.")

    with out.governance_assessments():
        out.line(
            "boundary/scalar silence target audit complete",
            StatusMark.PASS,
            "Group 22 targets are explicit; theorem burden remains open",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, exprs: BoundarySilenceExpressionSet) -> None:
    ns.record_derivation(
        derivation_id="boundary_scalar_silence_scalar_tail_flux_witness_22",
        inputs=[exprs.phi_tail, exprs.C],
        output=exprs.F_phi,
        method="simplify(4*pi*r**2*diff(C/r, r))",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="surface_flux_witness",
        scope="reduced ordinary exterior residual scalar tail",
    )

    ns.record_derivation(
        derivation_id="boundary_scalar_silence_boundary_A_tail_mass_witness_22",
        inputs=[exprs.delta_A_boundary, exprs.q],
        output=exprs.delta_M_A_boundary,
        method="simplify(c**2*(4*pi*r**2*diff(q/r, r))/(8*pi*G))",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="mass_shift_witness",
        scope="reduced ordinary exterior non-A boundary A-tail",
    )

    ns.record_derivation(
        derivation_id="boundary_scalar_silence_far_zone_current_flux_witness_22",
        inputs=[exprs.j_radial, exprs.I],
        output=exprs.current_flux,
        method="simplify(4*pi*r**2*(I/(4*pi*r**2)))",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="current_flux_witness",
        scope="reduced ordinary exterior non-A radial current",
    )

    ns.record_derivation(
        derivation_id="boundary_scalar_silence_target_ledger_marker_22",
        inputs=[sp.Symbol("delta_F_A_boundary_non_A"), sp.Symbol("C_residual"), sp.Symbol("I_nonA")],
        output=sp.Symbol("boundary_scalar_silence_targets_stated"),
        method="Group 22 opening target ledger",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="target_ledger_marker",
        scope="Group 22 boundary neutrality and scalar silence",
        is_placeholder=True,
    )


def record_obligations(ns, targets: List[SilenceTargetEntry]) -> None:
    obligations = [
        (
            "derive_no_shell_boundary_condition_22",
            "Derive no-shell boundary condition",
            "Show boundary matching does not hide derivative jumps, shell sources, or boundary scalar/mass flux.",
        ),
        (
            "derive_residual_scalar_silence_22",
            "Derive residual scalar silence",
            "Show zeta/kappa/J_V/curvature/H/boundary residual scalar coefficients vanish outside ordinary sources or remain strictly non-metric/diagnostic.",
        ),
        (
            "derive_non_A_boundary_A_flux_neutrality_22",
            "Derive non-A boundary A-flux neutrality",
            "Show non-A boundary behavior has delta F_A = 0 and does not shift M_A.",
        ),
        (
            "derive_far_zone_non_A_current_flux_silence_22",
            "Derive far-zone non-A current flux silence",
            "Show non-A far-zone current coefficients vanish or are derived neutral transport with no ordinary mass effect.",
        ),
        (
            "derive_compact_support_matching_law_22",
            "Derive compact-support matching law",
            "Show compact residual support has smooth matching, no shell source, and no recovery-tuned support.",
        ),
        (
            "derive_diagnostic_residual_non_reentry_22",
            "Derive diagnostic residual non-reentry",
            "Show diagnostic/non-metric residuals do not later re-enter metric, source, boundary, coefficient, or mass routing.",
        ),
        (
            "derive_no_recovery_tuned_boundary_data_22",
            "Derive no recovery-tuned boundary data",
            "Show boundary conditions are structural and not chosen from Schwarzschild, PPN, gamma_like, AB, or B=1/A recovery.",
        ),
    ]

    for obligation_id, title, description in obligations:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=obligation_id,
            script_id=SCRIPT_ID,
            title=title,
            status=ObligationStatus.OPEN,
            required_by=["ordinary_closed_regime_boundary_scalar_silence_theorem_22"],
            description=description,
        ))

    for target in targets:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=f"preserve_{target.name.split(':', 1)[0].replace('-', '_').replace(' ', '_').lower()}_target_22",
            script_id=SCRIPT_ID,
            title=f"Preserve boundary/scalar target: {target.name}",
            status=ObligationStatus.OPEN,
            required_by=["ordinary_closed_regime_boundary_scalar_silence_theorem_22"],
            description=(
                f"Target: {target.target}. Reason: {target.reason}. "
                f"Failure if: {target.failure_if}. Consequence: {target.consequence}."
            ),
        ))


def record_governance(ns) -> None:
    core_obligations = [
        "derive_no_shell_boundary_condition_22",
        "derive_residual_scalar_silence_22",
        "derive_non_A_boundary_A_flux_neutrality_22",
        "derive_far_zone_non_A_current_flux_silence_22",
        "derive_compact_support_matching_law_22",
        "derive_diagnostic_residual_non_reentry_22",
        "derive_no_recovery_tuned_boundary_data_22",
    ]

    ns.record_route(RouteRecord(
        route_id="ordinary_closed_regime_boundary_scalar_silence_theorem_22",
        script_id=SCRIPT_ID,
        name="Ordinary closed-regime boundary neutrality and scalar silence theorem target",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=core_obligations,
        activation_conditions=[
            "delta F_A|boundary,non-A = 0",
            "all ordinary residual exterior 1/r coefficients vanish or remain non-metric/diagnostic",
            "no shell source or hidden boundary flux exists",
            "no smoothing, O, H, dark label, exchange, curvature, or recovery repair is used",
        ],
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_boundary_scalar_silence_by_declaration_22",
        script_id=SCRIPT_ID,
        branch_id="boundary_scalar_silence_by_declaration",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=core_obligations,
        description=(
            "Reject boundary/scalar silence by declaration. Vanishing coefficients, boundary flux neutrality, "
            "no-shell behavior, current silence, and no-repair discipline must be shown."
        ),
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_parent_equation_until_boundary_scalar_silence_22",
        script_id=SCRIPT_ID,
        branch_id="parent_equation_after_group22",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=core_obligations,
        description=(
            "Do not attempt parent closure until boundary neutrality and exterior scalar silence are either derived or explicitly constrained."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="group22_boundary_scalar_silence_targets_explicit",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Group 22 boundary/scalar silence requires delta F_A|boundary,non-A = 0, vanishing ordinary exterior residual scalar coefficients, "
            "far-zone non-A current silence, no shell source, no recovery-tuned smoothing, no active O, and no H insertion."
        ),
        derivation_ids=[
            "boundary_scalar_silence_scalar_tail_flux_witness_22",
            "boundary_scalar_silence_boundary_A_tail_mass_witness_22",
            "boundary_scalar_silence_far_zone_current_flux_witness_22",
            "boundary_scalar_silence_target_ledger_marker_22",
        ],
        obligation_ids=core_obligations,
    ))

    ns.record_claim(ClaimRecord(
        claim_id="group22_boundary_scalar_silence_not_derived",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "This opening Group 22 script does not prove boundary neutrality or scalar silence. "
            "It only states the target ledger and records reduced danger witnesses."
        ),
        derivation_ids=["boundary_scalar_silence_target_ledger_marker_22"],
        obligation_ids=core_obligations,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Boundary Scalar Silence Targets")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    exprs = build_expressions()
    targets = build_targets()
    shortcuts = build_forbidden_shortcuts()

    case_0_problem_statement(out)
    case_1_reduced_witnesses(exprs, out)
    case_2_silence_target_ledger(targets, out)
    case_3_forbidden_shortcuts(shortcuts, out)
    case_4_theorem_targets(out)
    case_5_failure_controls(out)
    final_interpretation(out)

    record_derivations(ns, exprs)
    record_obligations(ns, targets)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
