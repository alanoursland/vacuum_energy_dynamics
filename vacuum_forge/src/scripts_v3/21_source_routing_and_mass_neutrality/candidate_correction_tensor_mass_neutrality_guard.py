# Candidate correction tensor mass neutrality guard
#
# Group:
#   21_source_routing_and_mass_neutrality
#
# Script type:
#   DIAGNOSTIC / REQUIREMENTS
#
# Purpose
# -------
# Audit why H_curv and H_exch remain non-insertable as correction tensors
# unless future definitions prove source separation, divergence safety,
# scalar trace neutrality, boundary neutrality, far-zone flux neutrality, and
# A-sector mass neutrality.
#
# Locked-door question:
#
#   Could H_curv or H_exch alter exterior mass if inserted?
#
# This script does not define H_curv, H_exch, their source sides, their
# divergence identities, or a parent field equation.
#
# It derives reduced diagnostic witnesses for correction-tensor leak routes:
#
#   scalar trace leakage: phi_H = C_H/r -> F_H = -4*pi*C_H
#   A-tail correction:    delta_A_H = q_H/r -> delta_M_H = -c^2*q_H/(2G)
#   far-zone H flux:      j_H^r = I_H/(4*pi*r^2) -> Phi_H = I_H
#
# The conclusion is deliberately narrow: H_curv/H_exch remain non-insertable
# until future structure defines them and proves mass neutrality.

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


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    ns.declare_dependency(
        dependency_id="curvature_accounting_inventory_dependency_21",
        upstream_script_id="21_source_routing_and_mass_neutrality__candidate_curvature_accounting_mass_neutrality",
        upstream_derivation_id="curvature_accounting_mass_neutrality_inventory_marker_21",
        expected_record_kind=RecordKind.INVENTORY_MARKER,
    )
    ns.declare_dependency(
        dependency_id="curvature_scalar_residue_flux_dependency_21",
        upstream_script_id="21_source_routing_and_mass_neutrality__candidate_curvature_accounting_mass_neutrality",
        upstream_derivation_id="curvature_scalar_residue_flux_21",
        expected_record_kind=RecordKind.DERIVATION,
    )
    ns.declare_dependency(
        dependency_id="e_curv_A_tail_flux_dependency_21",
        upstream_script_id="21_source_routing_and_mass_neutrality__candidate_curvature_accounting_mass_neutrality",
        upstream_derivation_id="e_curv_A_tail_flux_diagnostic_21",
        expected_record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
    )
    ns.declare_dependency(
        dependency_id="A_sector_mass_definition_dependency_21",
        upstream_script_id="21_source_routing_and_mass_neutrality__candidate_A_sector_mass_charge_definition",
        upstream_derivation_id="A_sector_mass_definition_21",
        expected_record_kind=RecordKind.DERIVATION,
    )

    return archive, ns, invalidated


def entry_status_mark(status: str) -> StatusMark:
    return {
        "CANDIDATE": StatusMark.INFO,
        "DEFER": StatusMark.DEFER,
        "DIAGNOSTIC_ONLY": StatusMark.INFO,
        "NOT_INSERTABLE": StatusMark.FAIL,
        "PROVISIONAL": StatusMark.INFO,
        "REJECTED": StatusMark.FAIL,
        "REQUIRED": StatusMark.OBLIGATION,
        "RISK": StatusMark.WARN,
        "SAFE_IF": StatusMark.INFO,
        "THEOREM_TARGET": StatusMark.DEFER,
        "UNDEFINED": StatusMark.DEFER,
        "UNRESOLVED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


# =============================================================================
# Data models
# =============================================================================


@dataclass
class CorrectionTensorExpressionSet:
    r: sp.Symbol
    G: sp.Symbol
    c: sp.Symbol
    C_H: sp.Symbol
    q_H: sp.Symbol
    I_H: sp.Symbol
    Div_H: sp.Symbol
    S_H: sp.Symbol
    phi_H: sp.Expr
    F_phi_H: sp.Expr
    F_phi_H_residual: sp.Expr
    delta_M_H_like: sp.Expr
    delta_M_H_like_residual: sp.Expr
    delta_A_H: sp.Expr
    delta_F_A_H: sp.Expr
    delta_F_A_H_residual: sp.Expr
    delta_M_A_H: sp.Expr
    delta_M_A_H_residual: sp.Expr
    j_H_radial: sp.Expr
    Phi_H: sp.Expr
    Phi_H_residual: sp.Expr
    source_divergence_gap: sp.Expr
    source_divergence_gap_residual: sp.Expr


@dataclass
class CorrectionTensorConditionEntry:
    name: str
    sector: str
    allowed_condition: str
    forbidden_condition: str
    status: str
    consequence: str
    obligation_id: str | None = None


@dataclass
class RejectedCorrectionTensorRoute:
    name: str
    route: str
    forbidden_use: str
    consequence: str
    obligation_id: str | None = None


# =============================================================================
# Builders
# =============================================================================


def build_expressions() -> CorrectionTensorExpressionSet:
    r = sp.Symbol("r", positive=True)
    G = sp.Symbol("G", positive=True)
    c = sp.Symbol("c", positive=True)
    C_H = sp.Symbol("C_H", real=True)
    q_H = sp.Symbol("q_H", real=True)
    I_H = sp.Symbol("I_H", real=True)
    Div_H = sp.Symbol("Div_H", real=True)
    S_H = sp.Symbol("S_H", real=True)

    # Generic scalar trace leakage that an inserted correction tensor must not
    # leave in the ordinary exterior unless a future parent identity derives a
    # neutral route.
    phi_H = C_H / r
    F_phi_H = sp.simplify(4 * sp.pi * r**2 * sp.diff(phi_H, r))
    F_phi_H_residual = sp.simplify(F_phi_H + 4 * sp.pi * C_H)
    delta_M_H_like = sp.simplify((c**2 / (8 * sp.pi * G)) * F_phi_H)
    delta_M_H_like_residual = sp.simplify(delta_M_H_like + c**2 * C_H / (2 * G))

    # Danger diagnostic only: if H were allowed to induce an A-like exterior
    # correction q_H/r, it would shift the A-sector mass. This is not a tensor
    # source law.
    delta_A_H = q_H / r
    delta_F_A_H = sp.simplify(4 * sp.pi * r**2 * sp.diff(delta_A_H, r))
    delta_F_A_H_residual = sp.simplify(delta_F_A_H + 4 * sp.pi * q_H)
    delta_M_A_H = sp.simplify((c**2 / (8 * sp.pi * G)) * delta_F_A_H)
    delta_M_A_H_residual = sp.simplify(delta_M_A_H + c**2 * q_H / (2 * G))

    # Far-zone correction-current / boundary-flux diagnostic.
    j_H_radial = I_H / (4 * sp.pi * r**2)
    Phi_H = sp.simplify(4 * sp.pi * r**2 * j_H_radial)
    Phi_H_residual = sp.simplify(Phi_H - I_H)

    # Role-level divergence/source counterpart diagnostic. This is not a Bianchi
    # identity; it just names the missing equality a future H insertion would need.
    source_divergence_gap = sp.simplify(Div_H - S_H)
    source_divergence_gap_residual = sp.simplify(source_divergence_gap - (Div_H - S_H))

    return CorrectionTensorExpressionSet(
        r=r,
        G=G,
        c=c,
        C_H=C_H,
        q_H=q_H,
        I_H=I_H,
        Div_H=Div_H,
        S_H=S_H,
        phi_H=phi_H,
        F_phi_H=F_phi_H,
        F_phi_H_residual=F_phi_H_residual,
        delta_M_H_like=delta_M_H_like,
        delta_M_H_like_residual=delta_M_H_like_residual,
        delta_A_H=delta_A_H,
        delta_F_A_H=delta_F_A_H,
        delta_F_A_H_residual=delta_F_A_H_residual,
        delta_M_A_H=delta_M_A_H,
        delta_M_A_H_residual=delta_M_A_H_residual,
        j_H_radial=j_H_radial,
        Phi_H=Phi_H,
        Phi_H_residual=Phi_H_residual,
        source_divergence_gap=source_divergence_gap,
        source_divergence_gap_residual=source_divergence_gap_residual,
    )


def build_condition_entries() -> List[CorrectionTensorConditionEntry]:
    return [
        CorrectionTensorConditionEntry(
            name="H1: H_curv undefined tensor candidate",
            sector="H_curv",
            allowed_condition="H_curv remains non-insertable until tensor definition, source side, divergence safety, and mass neutrality are derived",
            forbidden_condition="H_curv is inserted as curvature rescue, M_ext correction, boundary counterterm, or Bianchi paint",
            status="NOT_INSERTABLE",
            consequence="H_curv cannot alter exterior mass while undefined.",
            obligation_id="define_H_curv_tensor_before_insertion_21",
        ),
        CorrectionTensorConditionEntry(
            name="H2: H_exch undefined tensor candidate",
            sector="H_exch",
            allowed_condition="H_exch remains non-insertable until exchange source side, tensor definition, divergence safety, and mass neutrality are derived",
            forbidden_condition="H_exch is inserted as exchange repair, hidden mass correction, or scalar-tail cancellation",
            status="NOT_INSERTABLE",
            consequence="H_exch cannot repair ordinary-sector failures while undefined.",
            obligation_id="define_H_exch_tensor_before_insertion_21",
        ),
        CorrectionTensorConditionEntry(
            name="H3: scalar trace leakage neutrality",
            sector="H_curv / H_exch trace",
            allowed_condition="C_H = 0 outside, or future tensor structure proves trace-neutral non-metric behavior",
            forbidden_condition="phi_H = C_H/r with C_H != 0 treated as an exterior scalar mass correction",
            status="THEOREM_TARGET",
            consequence="Correction tensor trace leakage must not become a hidden scalar mass route.",
            obligation_id="derive_H_scalar_trace_neutrality_21",
        ),
        CorrectionTensorConditionEntry(
            name="H4: A-tail correction neutrality",
            sector="H-induced A-tail",
            allowed_condition="q_H = 0 unless a future parent identity redefines total mass without double counting",
            forbidden_condition="H induces delta_A = q_H/r and shifts M_A as an exterior mass correction",
            status="REJECTED",
            consequence="H cannot be used as an M_ext correction by declaration.",
            obligation_id="preserve_no_H_A_tail_mass_correction_21",
        ),
        CorrectionTensorConditionEntry(
            name="H5: far-zone H flux neutrality",
            sector="H boundary/current flux",
            allowed_condition="I_H = 0 in ordinary exterior unless future tensor conservation derives neutral transport",
            forbidden_condition="nonzero H far-zone flux shifts or mimics ordinary exterior mass",
            status="THEOREM_TARGET",
            consequence="Correction tensor flux cannot become a second mass coin.",
            obligation_id="derive_H_far_zone_flux_neutrality_21",
        ),
        CorrectionTensorConditionEntry(
            name="H6: divergence safety prerequisite",
            sector="divergence of H",
            allowed_condition="divergence identity, source counterpart, and constraint compatibility are derived before insertion",
            forbidden_condition="Bianchi compatibility is asserted because the object is called a correction tensor",
            status="THEOREM_TARGET",
            consequence="Divergence safety remains a prerequisite, not a label.",
            obligation_id="derive_H_divergence_safety_21",
        ),
        CorrectionTensorConditionEntry(
            name="H7: source separation prerequisite",
            sector="H source side",
            allowed_condition="ordinary matter, A-sector mass, curvature diagnostics, exchange labels, and dark labels are separated before H is sourced",
            forbidden_condition="H defines its own source by divergence or absorbs ordinary source mismatch",
            status="THEOREM_TARGET",
            consequence="H source side cannot be manufactured by the tensor itself.",
            obligation_id="derive_H_source_separation_21",
        ),
        CorrectionTensorConditionEntry(
            name="H8: boundary neutrality prerequisite",
            sector="H boundary behavior",
            allowed_condition="H has no shell source, no boundary counterterm, no far-zone patch, and no recovery-tuned boundary behavior",
            forbidden_condition="H is used as boundary purse or smoothing repair",
            status="THEOREM_TARGET",
            consequence="Correction tensors cannot preserve mass by boundary repair.",
            obligation_id="derive_H_boundary_neutrality_21",
        ),
        CorrectionTensorConditionEntry(
            name="H9: ordinary matter separation",
            sector="ordinary matter routing with H",
            allowed_condition="ordinary rho/T_mu_nu remains routed through established ordinary source channels unless a parent identity derives otherwise",
            forbidden_condition="ordinary matter mismatch is absorbed into H_curv or H_exch",
            status="REQUIRED",
            consequence="H cannot become a second ordinary-matter source channel.",
            obligation_id="derive_H_ordinary_matter_separation_21",
        ),
        CorrectionTensorConditionEntry(
            name="H10: dark patch exclusion",
            sector="dark labels and H",
            allowed_condition="dark labels remain optional downstream and do not patch ordinary H failure",
            forbidden_condition="H is routed into dark-sector language to absorb ordinary mass leakage",
            status="REJECTED",
            consequence="Dark labels cannot make H insertable in the ordinary sector.",
            obligation_id="preserve_no_H_dark_patch_21",
        ),
        CorrectionTensorConditionEntry(
            name="H11: O cannot license H",
            sector="O / projection dependency",
            allowed_condition="role-specific projectors must be derived before any H insertion uses no-overlap language",
            forbidden_condition="O is named to make H source-separated, divergence-safe, or boundary-neutral",
            status="REJECTED",
            consequence="No-overlap language cannot insert undefined correction tensors.",
            obligation_id="preserve_no_O_licenses_H_21",
        ),
        CorrectionTensorConditionEntry(
            name="H12: diagnostic-only audit label",
            sector="H_curv / H_exch labels",
            allowed_condition="H labels may remain diagnostic audit placeholders with no source, metric, divergence, boundary, or mass effect",
            forbidden_condition="diagnostic H label enters a field equation or modifies exterior mass",
            status="SAFE_IF",
            consequence="H labels are safe only as non-inserted diagnostics.",
        ),
    ]


def build_rejected_routes() -> List[RejectedCorrectionTensorRoute]:
    return [
        RejectedCorrectionTensorRoute(
            name="RH1: H as M_ext correction",
            route="H_M_ext_correction",
            forbidden_use="H_curv or H_exch shifts exterior mass or A-flux by tensor correction language",
            consequence="M_ext corrections require a future parent identity, not an inserted placeholder tensor.",
            obligation_id="preserve_no_H_M_ext_correction_21",
        ),
        RejectedCorrectionTensorRoute(
            name="RH2: H scalar tail cancellation",
            route="H_scalar_tail_cancellation",
            forbidden_use="H trace cancels zeta/kappa/J_V/curvature scalar tails after leakage appears",
            consequence="Scalar silence must be derived, not patched by correction tensor trace.",
            obligation_id="preserve_no_H_scalar_tail_cancellation_21",
        ),
        RejectedCorrectionTensorRoute(
            name="RH3: H boundary counterterm",
            route="H_boundary_counterterm",
            forbidden_use="H absorbs shell flux, boundary leakage, or smoothing mismatch",
            consequence="Boundary neutrality cannot be supplied by an undefined counterterm.",
            obligation_id="preserve_no_H_boundary_counterterm_21",
        ),
        RejectedCorrectionTensorRoute(
            name="RH4: H as Bianchi paint",
            route="H_Bianchi_paint",
            forbidden_use="H is called divergence-safe because it is meant to repair a Bianchi or conservation mismatch",
            consequence="Divergence compatibility must be derived before insertion.",
            obligation_id="preserve_no_H_Bianchi_paint_21",
        ),
        RejectedCorrectionTensorRoute(
            name="RH5: H source by divergence",
            route="H_source_by_divergence",
            forbidden_use="source side is defined as whatever divergence of H requires",
            consequence="H cannot define its own source side.",
            obligation_id="preserve_no_H_source_by_divergence_21",
        ),
        RejectedCorrectionTensorRoute(
            name="RH6: H dark-sector patch",
            route="H_dark_sector_patch",
            forbidden_use="dark label absorbs ordinary correction-tensor failure",
            consequence="Dark sector is not an ordinary mass-neutrality patch.",
            obligation_id="preserve_no_H_dark_sector_patch_21",
        ),
        RejectedCorrectionTensorRoute(
            name="RH7: recovery-chosen H insertion",
            route="recovery_chosen_H_insertion",
            forbidden_use="H form, coefficient, trace, boundary behavior, or source side is chosen from Schwarzschild/PPN/gamma_like/AB recovery",
            consequence="Recovery remains downstream diagnostic, not a tensor-construction rule.",
            obligation_id="preserve_no_recovery_chosen_H_21",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Correction tensor mass-neutrality guard problem")
    print("Question:")
    print()
    print("  Could H_curv or H_exch alter exterior mass if inserted?")
    print()
    print("Reference discipline:")
    print()
    print("  A-sector mass charge remains the reduced ordinary exterior reference.")
    print("  H_curv and H_exch are not defined and not insertable.")
    print("  Divergence safety, source separation, scalar trace neutrality, boundary neutrality,")
    print("  far-zone flux neutrality, and A-sector mass neutrality are required but not derived.")
    print("  This script records reduced diagnostics and theorem burden, not correction-tensor dynamics.")

    with out.governance_assessments():
        out.line(
            "correction-tensor mass-neutrality guard opened",
            StatusMark.INFO,
            "H_curv/H_exch are audited for trace leakage, A-tail mass shift, far-zone flux, boundary repair, and insertion danger",
        )


def case_1_scalar_trace_leakage(exprs: CorrectionTensorExpressionSet, out: ScriptOutput) -> None:
    header("Case 1: Correction-tensor scalar trace leakage")
    print("Take a generic scalar trace leakage from an inserted correction tensor:")
    print()
    print("  phi_H(r) = C_H/r")
    print()
    print("Then:")
    print()
    print(f"  F_phi_H = 4*pi*r^2*phi_H' = {sp.sstr(exprs.F_phi_H)}")
    print(f"  delta_M_H_like = c^2*F_phi_H/(8*pi*G) = {sp.sstr(exprs.delta_M_H_like)}")
    print()
    print("Residual checks:")
    print()
    print(f"  F_phi_H + 4*pi*C_H = {sp.sstr(exprs.F_phi_H_residual)}")
    print(f"  delta_M_H_like + c^2*C_H/(2*G) = {sp.sstr(exprs.delta_M_H_like_residual)}")
    print()
    print("Interpretation:")
    print()
    print("  This is a danger diagnostic, not a licensed correction-tensor mass law.")
    print("  H trace leakage with C_H != 0 would behave like hidden scalar mass charge.")

    with out.derived_results():
        out.line(
            "H scalar trace leakage flux derived",
            StatusMark.PASS if is_zero(exprs.F_phi_H_residual) else StatusMark.FAIL,
            f"F_phi_H = {sp.sstr(exprs.F_phi_H)}",
        )
        out.line(
            "H trace A-like mass-shift diagnostic derived",
            StatusMark.PASS if is_zero(exprs.delta_M_H_like_residual) else StatusMark.FAIL,
            f"delta_M_H_like = {sp.sstr(exprs.delta_M_H_like)}",
        )


def case_2_A_tail_correction_diagnostic(exprs: CorrectionTensorExpressionSet, out: ScriptOutput) -> None:
    header("Case 2: H-induced A-tail correction diagnostic")
    print("If an undefined correction tensor were incorrectly allowed to induce an exterior A-tail:")
    print()
    print("  delta_A_H(r) = q_H/r")
    print()
    print("then:")
    print()
    print(f"  delta_F_A|H = 4*pi*r^2*delta_A_H' = {sp.sstr(exprs.delta_F_A_H)}")
    print(f"  delta_M_A|H = c^2*delta_F_A/(8*pi*G) = {sp.sstr(exprs.delta_M_A_H)}")
    print()
    print("Residual checks:")
    print()
    print(f"  delta_F_A|H + 4*pi*q_H = {sp.sstr(exprs.delta_F_A_H_residual)}")
    print(f"  delta_M_A|H + c^2*q_H/(2*G) = {sp.sstr(exprs.delta_M_A_H_residual)}")
    print()
    print("Interpretation:")
    print()
    print("  This is not an H source law.")
    print("  It shows why H cannot be inserted as an exterior mass correction by vocabulary.")

    with out.derived_results():
        out.line(
            "H A-tail flux diagnostic derived",
            StatusMark.PASS if is_zero(exprs.delta_F_A_H_residual) else StatusMark.FAIL,
            f"delta_F_A|H = {sp.sstr(exprs.delta_F_A_H)}",
        )
        out.line(
            "H A-like mass-shift diagnostic derived",
            StatusMark.PASS if is_zero(exprs.delta_M_A_H_residual) else StatusMark.FAIL,
            f"delta_M_A|H = {sp.sstr(exprs.delta_M_A_H)}",
        )


def case_3_far_zone_flux_and_divergence_gap(exprs: CorrectionTensorExpressionSet, out: ScriptOutput) -> None:
    header("Case 3: Far-zone H flux and source/divergence gap diagnostic")
    print("Use a generic far-zone radial correction flux profile:")
    print()
    print("  j_H^r = I_H/(4*pi*r**2)")
    print()
    print("Its sphere flux is:")
    print()
    print(f"  Phi_H = 4*pi*r^2*j_H^r = {sp.sstr(exprs.Phi_H)}")
    print()
    print("Role-level divergence/source counterpart diagnostic:")
    print()
    print(f"  source_divergence_gap = Div_H - S_H = {sp.sstr(exprs.source_divergence_gap)}")
    print()
    print("Residual checks:")
    print()
    print(f"  Phi_H - I_H = {sp.sstr(exprs.Phi_H_residual)}")
    print(f"  source_divergence_gap - (Div_H - S_H) = {sp.sstr(exprs.source_divergence_gap_residual)}")
    print()
    print("Interpretation:")
    print()
    print("  H far-zone flux and divergence/source matching are theorem targets, not insertion licenses.")
    print("  Divergence safety and source side must be derived before H can enter a parent equation.")

    with out.derived_results():
        out.line(
            "H far-zone flux diagnostic derived",
            StatusMark.PASS if is_zero(exprs.Phi_H_residual) else StatusMark.FAIL,
            f"Phi_H = {sp.sstr(exprs.Phi_H)}",
        )
        out.line(
            "H divergence/source gap diagnostic stated",
            StatusMark.PASS if is_zero(exprs.source_divergence_gap_residual) else StatusMark.FAIL,
            "role-level target is Div_H - S_H = 0 only after tensor and source definitions exist",
        )
    with out.unresolved_obligations():
        out.line(
            "derive H tensor definitions before insertion",
            StatusMark.OBLIGATION,
            "H_curv/H_exch cannot be inserted while tensor definition, source side, divergence safety, and neutrality are missing",
        )


def case_4_condition_ledger(entries: List[CorrectionTensorConditionEntry], out: ScriptOutput) -> None:
    header("Case 4: Correction tensor condition ledger")
    for entry in entries:
        print()
        print("-" * 120)
        print(entry.name)
        print("-" * 120)
        print(f"Sector: {entry.sector}")
        print(f"Allowed condition: {entry.allowed_condition}")
        print(f"Forbidden condition: {entry.forbidden_condition}")
        print(f"[{entry_status_mark(entry.status).value}] {entry.name}: {entry.status}")
        print(f"Consequence: {entry.consequence}")

    with out.governance_assessments():
        out.line(
            "correction tensor ledger populated",
            StatusMark.PASS,
            f"{len(entries)} H_curv/H_exch conditions classified for mass-neutrality and insertability burden",
        )


def case_5_rejected_H_routes(routes: List[RejectedCorrectionTensorRoute], out: ScriptOutput) -> None:
    header("Case 5: Rejected correction-tensor mass routes")
    for route in routes:
        print()
        print("-" * 120)
        print(route.name)
        print("-" * 120)
        print(f"Route: {route.route}")
        print(f"Forbidden use: {route.forbidden_use}")
        print(f"[FAIL] {route.name}: REJECTED")
        print(f"Consequence: {route.consequence}")

    with out.counterexamples():
        out.line(
            "correction-tensor mass routes rejected",
            StatusMark.FAIL,
            "H as M_ext correction, scalar-tail cancellation, boundary counterterm, Bianchi paint, source-by-divergence, dark patch, and recovery-chosen insertion are not licensed",
        )


def case_6_failure_controls(out: ScriptOutput) -> None:
    header("Case 6: Failure controls")
    print("The correction-tensor mass-neutrality guard fails if a later script allows:")
    print()
    print("1. H_curv or H_exch to enter a parent equation before definition")
    print("2. H trace leakage with C_H/r outside and C_H != 0")
    print("3. H to induce delta_A = q_H/r and shift M_A")
    print("4. H far-zone flux to count as ordinary exterior mass")
    print("5. H to repair scalar tails, boundary flux, source mismatch, or recovery failure")
    print("6. divergence safety or Bianchi compatibility to be asserted by naming H")
    print("7. H to define its own source side by divergence")
    print("8. H to absorb ordinary matter, curvature diagnostics, exchange labels, or dark labels")
    print("9. recovery targets to choose H form, coefficient, trace, source side, or boundary behavior")
    print("10. O to license H without domain/kernel/image/boundary law")

    with out.unresolved_obligations():
        out.line(
            "derive correction-tensor mass-neutrality and insertability theorem",
            StatusMark.OBLIGATION,
            "show H_curv/H_exch have definitions, source separation, divergence safety, scalar trace neutrality, boundary neutrality, far-zone flux neutrality, and delta_M_A = 0 before insertion",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("The reduced diagnostics are:")
    print()
    print("  phi_H = C_H/r          -> F_phi_H = -4*pi*C_H")
    print("  delta_A_H = q_H/r      -> delta_M_A|H = -c^2*q_H/(2*G)")
    print("  j_H^r = I_H/(4*pi*r^2) -> sphere H flux = I_H")
    print("  source/divergence gap  -> Div_H - S_H = 0 only after H and source side exist")
    print()
    print("Therefore future H insertion requires:")
    print()
    print("  independent tensor definition")
    print("  independent source-side counterpart")
    print("  divergence safety")
    print("  ordinary matter separation")
    print("  A-sector mass neutrality")
    print("  scalar trace neutrality")
    print("  boundary neutrality")
    print("  far-zone flux neutrality")
    print("  no shell source")
    print("  no recovery tuning")
    print()
    print("This script does not define H_curv or H_exch.")
    print("It records why correction tensors remain non-insertable.")
    print()
    print("Possible next script:")
    print("  candidate_source_routing_no_double_counting.py")

    with out.governance_assessments():
        out.line(
            "correction-tensor mass-neutrality guard complete",
            StatusMark.PASS,
            "H_curv/H_exch remain diagnostic-only audit labels; no correction tensor is insertable",
        )


# =============================================================================
# Archive records
# =============================================================================


def record_derivations(ns, exprs: CorrectionTensorExpressionSet) -> None:
    ns.record_derivation(
        derivation_id="H_scalar_trace_leakage_flux_21",
        inputs=[exprs.phi_H, exprs.r, exprs.C_H],
        output=exprs.F_phi_H,
        method="F_phi_H = simplify(4*pi*r**2*diff(C_H/r, r))",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="surface_flux",
        scope="reduced ordinary exterior correction-tensor scalar trace diagnostic",
    )
    ns.record_derivation(
        derivation_id="H_scalar_trace_A_like_mass_shift_21",
        inputs=[exprs.F_phi_H, exprs.c, exprs.G],
        output=exprs.delta_M_H_like,
        method="delta_M_H_like = simplify(c**2*F_phi_H/(8*pi*G))",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="mass_shift_diagnostic",
        scope="danger diagnostic only; not a licensed H mass law",
    )
    ns.record_derivation(
        derivation_id="H_A_tail_flux_diagnostic_21",
        inputs=[exprs.delta_A_H, exprs.r, exprs.q_H],
        output=exprs.delta_F_A_H,
        method="delta_F_A_H = simplify(4*pi*r**2*diff(q_H/r, r))",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="A_flux_shift_diagnostic",
        scope="danger diagnostic only; not a licensed H source law",
    )
    ns.record_derivation(
        derivation_id="H_A_like_mass_shift_diagnostic_21",
        inputs=[exprs.delta_F_A_H, exprs.c, exprs.G],
        output=exprs.delta_M_A_H,
        method="delta_M_A_H = simplify(c**2*delta_F_A_H/(8*pi*G))",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="mass_shift_diagnostic",
        scope="danger diagnostic only; not a licensed H mass law",
    )
    ns.record_derivation(
        derivation_id="H_far_zone_flux_diagnostic_21",
        inputs=[exprs.j_H_radial, exprs.r, exprs.I_H],
        output=exprs.Phi_H,
        method="Phi_H = simplify(4*pi*r**2*(I_H/(4*pi*r**2)))",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="current_flux_diagnostic",
        scope="far-zone correction-tensor flux diagnostic only",
    )
    ns.record_derivation(
        derivation_id="H_source_divergence_gap_diagnostic_21",
        inputs=[exprs.Div_H, exprs.S_H],
        output=exprs.source_divergence_gap,
        method="source_divergence_gap = simplify(Div_H - S_H)",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="source_divergence_gap_diagnostic",
        scope="role-level diagnostic only; not a divergence identity",
    )


def record_inventory_marker(ns, entries: List[CorrectionTensorConditionEntry]) -> None:
    names = [sp.Symbol(entry.name.split(":", 1)[0].replace("-", "_").replace(" ", "_")) for entry in entries]
    ns.record_derivation(
        derivation_id="correction_tensor_mass_neutrality_guard_marker_21",
        inputs=names,
        output=sp.Symbol("correction_tensor_mass_neutrality_guard_conditions_stated"),
        method="H_curv/H_exch mass-neutrality guard and rejected-route inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="inventory_marker",
        scope="Group 21 source routing and mass neutrality",
        is_placeholder=True,
    )


def record_obligations(
    ns,
    entries: List[CorrectionTensorConditionEntry],
    routes: List[RejectedCorrectionTensorRoute],
) -> None:
    for entry in entries:
        if entry.obligation_id is None:
            continue
        ns.record_obligation(ProofObligationRecord(
            obligation_id=entry.obligation_id,
            script_id=SCRIPT_ID,
            title=f"Resolve correction-tensor condition: {entry.name}",
            status=ObligationStatus.OPEN,
            required_by=["correction_tensor_mass_neutrality_and_insertability_theorem_21"],
            description=(
                f"Sector: {entry.sector}. Allowed condition: {entry.allowed_condition}. "
                f"Forbidden condition: {entry.forbidden_condition}. Consequence: {entry.consequence}."
            ),
        ))

    for route in routes:
        if route.obligation_id is None:
            continue
        ns.record_obligation(ProofObligationRecord(
            obligation_id=route.obligation_id,
            script_id=SCRIPT_ID,
            title=f"Preserve rejection: {route.name}",
            status=ObligationStatus.OPEN,
            required_by=["correction_tensor_mass_neutrality_and_insertability_theorem_21"],
            description=(
                f"Route: {route.route}. Forbidden use: {route.forbidden_use}. "
                f"Consequence: {route.consequence}."
            ),
        ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="correction_tensor_mass_neutrality_and_insertability_theorem_21",
        script_id=SCRIPT_ID,
        title="Derive correction-tensor mass-neutrality and insertability theorem",
        status=ObligationStatus.OPEN,
        required_by=["ordinary_closed_regime_mass_neutrality_theorem_21"],
        description=(
            "Show any future H_curv/H_exch has an independent tensor definition, independent source-side counterpart, "
            "divergence safety, ordinary matter separation, A-sector mass neutrality, scalar trace neutrality, boundary neutrality, "
            "far-zone flux neutrality, no shell source, and no recovery tuning before insertion."
        ),
    ))


def record_governance(
    ns,
    entries: List[CorrectionTensorConditionEntry],
    routes: List[RejectedCorrectionTensorRoute],
) -> None:
    obligation_ids = [entry.obligation_id for entry in entries if entry.obligation_id is not None]
    obligation_ids.extend(route.obligation_id for route in routes if route.obligation_id is not None)
    obligation_ids.append("correction_tensor_mass_neutrality_and_insertability_theorem_21")

    ns.record_route(RouteRecord(
        route_id="correction_tensor_mass_neutrality_guard_route_21",
        script_id=SCRIPT_ID,
        name="H_curv / H_exch mass-neutrality and insertability guard route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "A-sector mass charge remains the reduced ordinary exterior reference",
            "H_curv and H_exch remain undefined and non-insertable unless future tensor definitions are derived",
            "source separation, divergence safety, scalar trace neutrality, boundary neutrality, far-zone flux neutrality, and A-sector mass neutrality are required before insertion",
            "no H mass correction, scalar-tail cancellation, boundary counterterm, Bianchi paint, source-by-divergence, dark patch, active O, or recovery tuning is assumed",
        ],
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="keep_H_curv_H_exch_non_insertable_21",
        script_id=SCRIPT_ID,
        branch_id="H_curv_H_exch_insertion",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "define_H_curv_tensor_before_insertion_21",
            "define_H_exch_tensor_before_insertion_21",
            "derive_H_divergence_safety_21",
            "derive_H_source_separation_21",
            "derive_H_scalar_trace_neutrality_21",
            "derive_H_boundary_neutrality_21",
            "derive_H_far_zone_flux_neutrality_21",
            "correction_tensor_mass_neutrality_and_insertability_theorem_21",
        ],
        description=(
            "H_curv/H_exch remain non-insertable until tensor definitions, source separation, divergence safety, scalar trace neutrality, "
            "boundary neutrality, far-zone flux neutrality, and A-sector mass neutrality are derived."
        ),
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_H_mass_repair_routes_21",
        script_id=SCRIPT_ID,
        branch_id="H_mass_repair_routes",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[route.obligation_id for route in routes if route.obligation_id is not None],
        description=(
            "Reject H as M_ext correction, scalar-tail cancellation, boundary counterterm, Bianchi paint, source-by-divergence, "
            "dark-sector patch, or recovery-chosen insertion."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="correction_tensor_mass_neutrality_guard_conditions_21",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "H_curv and H_exch are not licensed as ordinary exterior mass carriers or correction-tensor insertions in Group 21. "
            "They must remain diagnostic/non-inserted labels unless future structure derives tensor definitions, source separation, "
            "divergence safety, scalar trace neutrality, boundary neutrality, far-zone flux neutrality, and delta_M_A = 0."
        ),
        derivation_ids=[
            "H_scalar_trace_leakage_flux_21",
            "H_A_tail_flux_diagnostic_21",
            "H_far_zone_flux_diagnostic_21",
            "H_source_divergence_gap_diagnostic_21",
        ],
        obligation_ids=obligation_ids,
    ))

    ns.record_claim(ClaimRecord(
        claim_id="correction_tensor_mass_repair_routes_rejected_21",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Correction tensors may not be used as repair mechanisms: H cannot shift M_ext, cancel scalar tails, act as boundary counterterm, "
            "paint over Bianchi/divergence issues, define its own source, patch through dark labels, or be chosen by recovery."
        ),
        derivation_ids=[
            "H_scalar_trace_leakage_flux_21",
            "H_A_tail_flux_diagnostic_21",
            "H_source_divergence_gap_diagnostic_21",
        ],
        obligation_ids=[route.obligation_id for route in routes if route.obligation_id is not None],
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Correction Tensor Mass Neutrality Guard")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    exprs = build_expressions()
    entries = build_condition_entries()
    routes = build_rejected_routes()

    case_0_problem_statement(out)
    case_1_scalar_trace_leakage(exprs, out)
    case_2_A_tail_correction_diagnostic(exprs, out)
    case_3_far_zone_flux_and_divergence_gap(exprs, out)
    case_4_condition_ledger(entries, out)
    case_5_rejected_H_routes(routes, out)
    case_6_failure_controls(out)
    final_interpretation(out)

    record_derivations(ns, exprs)
    record_inventory_marker(ns, entries)
    record_obligations(ns, entries, routes)
    record_governance(ns, entries, routes)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
