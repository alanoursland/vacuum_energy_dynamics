# Candidate non-A sector mass-neutrality inventory
#
# Group:
#   21_source_routing_and_mass_neutrality
#
# Script type:
#   INVENTORY / REQUIREMENTS
#
# Purpose
# -------
# Inventory every non-A sector that could accidentally carry or shift the
# ordinary exterior mass charge after the A-sector mass coin has been defined.
#
# Locked-door question:
#
#   Which non-A sectors could accidentally carry or shift exterior mass?
#
# This script does not prove non-A mass neutrality.
# It does not define a parent mass law.
# It does not activate O, J_V, J_sub, J_exch, zeta/kappa residuals,
# curvature diagnostics, correction tensors, boundary smoothing, or dark labels.
#
# It records the inventory and theorem burden:
#
#   rho / M_enc -> A-sector mass charge
#   delta M_A | non-A = 0   remains required unless independently derived.

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
        dependency_id="A_sector_mass_definition_dependency_21",
        upstream_script_id="21_source_routing_and_mass_neutrality__candidate_A_sector_mass_charge_definition",
        upstream_derivation_id="A_sector_mass_definition_21",
        expected_record_kind=RecordKind.DERIVATION,
    )
    ns.declare_dependency(
        dependency_id="A_sector_schwarzschild_mass_residual_dependency_21",
        upstream_script_id="21_source_routing_and_mass_neutrality__candidate_A_sector_mass_charge_definition",
        upstream_derivation_id="A_sector_schwarzschild_mass_residual_21",
        expected_record_kind=RecordKind.DERIVATION,
    )
    ns.declare_dependency(
        dependency_id="group20_no_overlap_projection_status_marker",
        upstream_script_id="20_no_overlap_and_projection_operators__candidate_no_overlap_projection_group_status_summary",
        upstream_derivation_id="no_overlap_projection_group_status_summary_marker",
        expected_record_kind=RecordKind.INVENTORY_MARKER,
    )

    return archive, ns, invalidated


def status_mark(status: str) -> StatusMark:
    return {
        "REFERENCE": StatusMark.PASS,
        "REQUIRED": StatusMark.OBLIGATION,
        "THEOREM_TARGET": StatusMark.DEFER,
        "UNRESOLVED": StatusMark.DEFER,
        "ROLE_LEVEL": StatusMark.INFO,
        "DIAGNOSTIC_ONLY": StatusMark.INFO,
        "SAFE_IF": StatusMark.INFO,
        "PROVISIONAL": StatusMark.INFO,
        "RISK": StatusMark.WARN,
        "DEFER": StatusMark.DEFER,
        "NOT_INSERTABLE": StatusMark.FAIL,
        "REJECTED": StatusMark.FAIL,
    }.get(status, StatusMark.INFO)


# =============================================================================
# Data models
# =============================================================================


@dataclass
class NonAMassNeutralityEntry:
    name: str
    sector: str
    current_role: str
    can_enter_A_flux: str
    can_create_scalar_tail: str
    can_shift_boundary_Aprime: str
    can_change_M_A: str
    can_alter_measured_M_ext: str
    required_condition: str
    status: str
    consequence: str
    obligation_id: str


@dataclass
class InventorySummary:
    total: int
    theorem_targets: int
    unresolved_or_deferred: int
    risks: int
    diagnostic_or_role_level: int
    not_insertable_or_rejected: int


# =============================================================================
# Inventory content
# =============================================================================


def build_entries() -> List[NonAMassNeutralityEntry]:
    return [
        NonAMassNeutralityEntry(
            name="N1: B_s / A_spatial insertion",
            sector="B_s / A_spatial",
            current_role="spatial recovery / metric insertion theorem target",
            can_enter_A_flux="not licensed; dangerous if it changes A or A'",
            can_create_scalar_tail="possible if treated as independent scalar companion",
            can_shift_boundary_Aprime="possible through insertion or matching rule",
            can_change_M_A="must be zero unless future insertion theorem redefines total mass",
            can_alter_measured_M_ext="yes if B_s is used to hide or duplicate mass response",
            required_condition="derive B_s insertion with delta M_A = 0 and no recovery-chosen coefficient",
            status="THEOREM_TARGET",
            consequence="B_s may be audited, but it is not a second mass-charge carrier.",
            obligation_id="derive_Bs_A_spatial_mass_neutrality_21",
        ),
        NonAMassNeutralityEntry(
            name="N2: zeta residual",
            sector="zeta_residual",
            current_role="volume-form candidate / residual diagnostic unless inserted",
            can_enter_A_flux="not licensed",
            can_create_scalar_tail="yes; 1/r tail would be exterior scalar charge",
            can_shift_boundary_Aprime="possible through boundary residual or smoothing layer",
            can_change_M_A="must be zero",
            can_alter_measured_M_ext="yes if residual metric trace survives as scalar tail",
            required_condition="zeta residual is non-metric, killed, compact-neutral, or proves C_zeta = 0 outside",
            status="RISK",
            consequence="residual zeta cannot carry ordinary exterior mass by declaration.",
            obligation_id="derive_zeta_residual_mass_neutrality_21",
        ),
        NonAMassNeutralityEntry(
            name="N3: kappa residual",
            sector="kappa_residual",
            current_role="diagnostic / uncompensated trace-like residual unless derived otherwise",
            can_enter_A_flux="not licensed",
            can_create_scalar_tail="yes; 1/r tail would break scalar silence",
            can_shift_boundary_Aprime="possible if kappa is allowed to repair boundary mismatch",
            can_change_M_A="must be zero",
            can_alter_measured_M_ext="yes if residual kappa becomes metric trace source",
            required_condition="kappa residual is non-metric, suppressed, compact-neutral, or proves C_kappa = 0 outside",
            status="RISK",
            consequence="kappa remains diagnostic or theorem-targeted, not a second mass channel.",
            obligation_id="derive_kappa_residual_mass_neutrality_21",
        ),
        NonAMassNeutralityEntry(
            name="N4: epsilon_vac_config",
            sector="epsilon_vac_config",
            current_role="configuration-energy/accounting label",
            can_enter_A_flux="not licensed",
            can_create_scalar_tail="possible if converted into scalar source reservoir",
            can_shift_boundary_Aprime="possible if accounting term is used as boundary repair",
            can_change_M_A="must be zero unless source law is derived",
            can_alter_measured_M_ext="yes if configuration energy is counted as exterior mass source",
            required_condition="configuration energy remains diagnostic/accounting or proves source-neutrality",
            status="SAFE_IF",
            consequence="configuration bookkeeping cannot become mass energy by vocabulary.",
            obligation_id="derive_epsilon_vac_config_mass_neutrality_21",
        ),
        NonAMassNeutralityEntry(
            name="N5: e_kappa",
            sector="e_kappa",
            current_role="kappa-energy diagnostic / stiffness bookkeeping",
            can_enter_A_flux="not licensed",
            can_create_scalar_tail="possible if e_kappa sources kappa Poisson behavior",
            can_shift_boundary_Aprime="possible if kappa energy is used as boundary reservoir",
            can_change_M_A="must be zero",
            can_alter_measured_M_ext="yes if kappa energy becomes exterior source energy",
            required_condition="e_kappa does not source A, does not source exterior kappa tail, and stays diagnostic",
            status="SAFE_IF",
            consequence="kappa stiffness may suppress imbalance but cannot add mass charge.",
            obligation_id="derive_e_kappa_mass_neutrality_21",
        ),
        NonAMassNeutralityEntry(
            name="N6: J_V",
            sector="J_V",
            current_role="unresolved umbrella vacuum-current notation",
            can_enter_A_flux="not licensed; no flux law exists",
            can_create_scalar_tail="possible if J_V leaves scalar residue",
            can_shift_boundary_Aprime="possible if J_V is used as boundary current",
            can_change_M_A="must be zero until J_V is defined and neutral",
            can_alter_measured_M_ext="yes if J_V becomes hidden mass current",
            required_condition="define J_V, source side, domain, flux direction, and prove delta M_A|J_V = 0",
            status="UNRESOLVED",
            consequence="J_V cannot carry ordinary exterior mass while undefined.",
            obligation_id="derive_JV_mass_neutrality_21",
        ),
        NonAMassNeutralityEntry(
            name="N7: J_sub",
            sector="J_sub",
            current_role="role-level pure-wind / substrate-current label",
            can_enter_A_flux="not licensed",
            can_create_scalar_tail="possible if wind is allowed to gravitate by existence",
            can_shift_boundary_Aprime="possible if wind cancels a boundary mismatch",
            can_change_M_A="must be zero",
            can_alter_measured_M_ext="yes if pure wind becomes preferred-frame force or mass source",
            required_condition="pure wind neutrality, no scalar trace, no ordinary matter push, no M_ext shift",
            status="ROLE_LEVEL",
            consequence="pure wind is not gravity without an independent theorem.",
            obligation_id="derive_Jsub_mass_neutrality_21",
        ),
        NonAMassNeutralityEntry(
            name="N8: J_exch",
            sector="J_exch",
            current_role="role-level exchange-current label",
            can_enter_A_flux="not licensed",
            can_create_scalar_tail="possible if exchange residue becomes scalar source",
            can_shift_boundary_Aprime="possible if exchange repairs ordinary matter routing",
            can_change_M_A="must be zero in ordinary closed regime unless source law derives otherwise",
            can_alter_measured_M_ext="yes if J_exch patches boundary or source mismatch",
            required_condition="exchange source/support law and zero-net or zero-creation ordinary branch",
            status="ROLE_LEVEL",
            consequence="exchange is not a repair current and not an ordinary mass route.",
            obligation_id="derive_Jexch_mass_neutrality_21",
        ),
        NonAMassNeutralityEntry(
            name="N9: Sigma_V / R_V",
            sector="Sigma_V / R_V",
            current_role="volume creation/destruction role labels",
            can_enter_A_flux="not licensed",
            can_create_scalar_tail="possible if net creation leaves exterior scalar charge",
            can_shift_boundary_Aprime="possible if relaxation cancels boundary mismatch",
            can_change_M_A="must be zero in ordinary closed regime unless net source is derived",
            can_alter_measured_M_ext="yes if Sigma/R become hidden source terms",
            required_condition="derive operators, signs, strengths, domains, and ordinary-sector zero-net condition",
            status="THEOREM_TARGET",
            consequence="Sigma/R remain theorem targets, not tuning knobs.",
            obligation_id="derive_SigmaV_RV_mass_neutrality_21",
        ),
        NonAMassNeutralityEntry(
            name="N10: Sigma_exch / R_exch",
            sector="Sigma_exch / R_exch",
            current_role="exchange-side role labels",
            can_enter_A_flux="not licensed",
            can_create_scalar_tail="possible if exchange source leaks trace",
            can_shift_boundary_Aprime="possible if exchange relaxation is used as repair",
            can_change_M_A="must be zero unless exchange source law derives mass modification",
            can_alter_measured_M_ext="yes if exchange duplicates ordinary matter mass",
            required_condition="derive exchange source routing and prove no ordinary A-mass double count",
            status="THEOREM_TARGET",
            consequence="exchange roles cannot route ordinary mass by convenience.",
            obligation_id="derive_Sigma_exch_R_exch_mass_neutrality_21",
        ),
        NonAMassNeutralityEntry(
            name="N11: A_curv",
            sector="A_curv",
            current_role="curvature admissibility diagnostic / branch-filter target",
            can_enter_A_flux="not licensed",
            can_create_scalar_tail="possible if promoted into scalar curvature charge",
            can_shift_boundary_Aprime="possible if admissibility filters boundary behavior after recovery failure",
            can_change_M_A="must be zero",
            can_alter_measured_M_ext="yes if curvature admissibility becomes dynamics",
            required_condition="A_curv remains diagnostic/branch-filter or receives independent source-neutral dynamics",
            status="DIAGNOSTIC_ONLY",
            consequence="curvature admissibility is not source energy.",
            obligation_id="derive_A_curv_mass_neutrality_21",
        ),
        NonAMassNeutralityEntry(
            name="N12: e_curv",
            sector="e_curv",
            current_role="curvature energy diagnostic / accounting only",
            can_enter_A_flux="not licensed",
            can_create_scalar_tail="possible if e_curv becomes source reservoir",
            can_shift_boundary_Aprime="possible if curvature energy smooths mass by repair",
            can_change_M_A="must be zero",
            can_alter_measured_M_ext="yes if e_curv is counted as ordinary exterior mass",
            required_condition="e_curv stays diagnostic/accounting and never sources A without derivation",
            status="DIAGNOSTIC_ONLY",
            consequence="curvature accounting cannot become mass source by naming it energy.",
            obligation_id="derive_e_curv_mass_neutrality_21",
        ),
        NonAMassNeutralityEntry(
            name="N13: J_curv",
            sector="J_curv",
            current_role="unresolved curvature-current theorem target",
            can_enter_A_flux="not licensed",
            can_create_scalar_tail="possible if curvature flux becomes exterior scalar current",
            can_shift_boundary_Aprime="possible if J_curv cancels boundary or singular behavior",
            can_change_M_A="must be zero unless independently derived",
            can_alter_measured_M_ext="yes if J_curv is used as repair current",
            required_condition="define J_curv, orientation, source side, boundary law, and mass neutrality",
            status="UNRESOLVED",
            consequence="J_curv cannot be a curvature rescue or mass route while undefined.",
            obligation_id="derive_J_curv_mass_neutrality_21",
        ),
        NonAMassNeutralityEntry(
            name="N14: H_curv",
            sector="H_curv",
            current_role="undefined correction-tensor candidate",
            can_enter_A_flux="not licensed",
            can_create_scalar_tail="possible if tensor trace leaks scalar charge",
            can_shift_boundary_Aprime="possible if used as boundary counterterm",
            can_change_M_A="must be zero before any future insertion",
            can_alter_measured_M_ext="yes if inserted as M_ext correction",
            required_condition="tensor definition, source separation, divergence safety, boundary neutrality, mass neutrality",
            status="NOT_INSERTABLE",
            consequence="H_curv remains non-insertable.",
            obligation_id="derive_H_curv_mass_neutrality_21",
        ),
        NonAMassNeutralityEntry(
            name="N15: H_exch",
            sector="H_exch",
            current_role="undefined correction-tensor candidate",
            can_enter_A_flux="not licensed",
            can_create_scalar_tail="possible if tensor trace cancels exchange residue",
            can_shift_boundary_Aprime="possible if used as exchange boundary repair",
            can_change_M_A="must be zero before any future insertion",
            can_alter_measured_M_ext="yes if inserted as hidden exchange-mass correction",
            required_condition="tensor definition, exchange source side, divergence safety, boundary neutrality, mass neutrality",
            status="NOT_INSERTABLE",
            consequence="H_exch remains non-insertable.",
            obligation_id="derive_H_exch_mass_neutrality_21",
        ),
        NonAMassNeutralityEntry(
            name="N16: boundary smoothing",
            sector="boundary_smoothing",
            current_role="matching / transition behavior theorem target",
            can_enter_A_flux="not licensed",
            can_create_scalar_tail="yes if smoothing leaves residual 1/r mode",
            can_shift_boundary_Aprime="yes; this is the main danger",
            can_change_M_A="must be zero",
            can_alter_measured_M_ext="yes if smoothing tunes exterior A' or hides shell source",
            required_condition="derive delta F_A|boundary,non-A = 0 with no shell source and no recovery tuning",
            status="THEOREM_TARGET",
            consequence="boundary purse remains closed until a theorem opens it.",
            obligation_id="derive_boundary_smoothing_mass_neutrality_21",
        ),
        NonAMassNeutralityEntry(
            name="N17: metric insertion / residual-kill convention",
            sector="metric_insertion / residual_kill",
            current_role="provisional safety convention / theorem target",
            can_enter_A_flux="not licensed",
            can_create_scalar_tail="possible if killed residual later re-enters metric",
            can_shift_boundary_Aprime="possible if insertion is selected after recovery check",
            can_change_M_A="must be zero",
            can_alter_measured_M_ext="yes if residual-kill hides source overlap",
            required_condition="derive insertion/no-overlap or keep residual strictly non-metric and diagnostic",
            status="PROVISIONAL",
            consequence="residual-kill is safer than residual mass, but it is not a theorem.",
            obligation_id="derive_metric_insertion_residual_kill_mass_neutrality_21",
        ),
        NonAMassNeutralityEntry(
            name="N18: dark-sector labels",
            sector="dark_sector_labels",
            current_role="optional downstream labels only",
            can_enter_A_flux="not licensed in ordinary sector",
            can_create_scalar_tail="possible if used to patch ordinary scalar leakage",
            can_shift_boundary_Aprime="possible if dark label absorbs boundary mismatch",
            can_change_M_A="must be zero for ordinary-sector audit",
            can_alter_measured_M_ext="yes if dark label patches ordinary mass failure",
            required_condition="derive independent dark coupling after ordinary-sector neutrality, not before",
            status="DEFER",
            consequence="dark sector is not an ordinary mass patch.",
            obligation_id="derive_dark_label_mass_neutrality_21",
        ),
    ]


def build_summary(entries: List[NonAMassNeutralityEntry]) -> InventorySummary:
    theorem_targets = sum(1 for e in entries if e.status == "THEOREM_TARGET")
    unresolved_or_deferred = sum(1 for e in entries if e.status in {"UNRESOLVED", "DEFER"})
    risks = sum(1 for e in entries if e.status == "RISK")
    diagnostic_or_role_level = sum(1 for e in entries if e.status in {"DIAGNOSTIC_ONLY", "ROLE_LEVEL", "SAFE_IF", "PROVISIONAL"})
    not_insertable_or_rejected = sum(1 for e in entries if e.status in {"NOT_INSERTABLE", "REJECTED"})
    return InventorySummary(
        total=len(entries),
        theorem_targets=theorem_targets,
        unresolved_or_deferred=unresolved_or_deferred,
        risks=risks,
        diagnostic_or_role_level=diagnostic_or_role_level,
        not_insertable_or_rejected=not_insertable_or_rejected,
    )


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Non-A mass-neutrality inventory problem")
    print("Question:")
    print()
    print("  Which non-A sectors could accidentally carry or shift exterior mass?")
    print()
    print("Reference from the prior script:")
    print()
    print("  F_A(r) = 4*pi*r^2*A'(r)")
    print("  M_A(r) = c^2*F_A(r)/(8*pi*G)")
    print()
    print("Discipline:")
    print()
    print("  A carries the ordinary exterior mass coin.")
    print("  Every non-A sector must show delta M_A = 0, remain diagnostic,")
    print("  remain non-metric, or stay theorem-targeted.")
    print("  No active O is assumed.")
    print("  No boundary repair, recovery tuning, or second mass spoon is allowed.")

    with out.governance_assessments():
        out.line(
            "non-A mass-neutrality inventory opened",
            StatusMark.INFO,
            "A-sector mass charge is the reference; non-A sectors are audited for leakage",
        )


def case_1_print_inventory(entries: List[NonAMassNeutralityEntry], out: ScriptOutput) -> None:
    header("Case 1: Non-A sector mass-leak inventory")

    for entry in entries:
        print()
        print("-" * 120)
        print(entry.name)
        print("-" * 120)
        print(f"Sector: {entry.sector}")
        print(f"Current role: {entry.current_role}")
        print(f"Can enter A-flux? {entry.can_enter_A_flux}")
        print(f"Can create scalar tail? {entry.can_create_scalar_tail}")
        print(f"Can shift boundary A'? {entry.can_shift_boundary_Aprime}")
        print(f"Can change M_A? {entry.can_change_M_A}")
        print(f"Can alter measured M_ext? {entry.can_alter_measured_M_ext}")
        print(f"Required condition: {entry.required_condition}")
        print(f"[{status_mark(entry.status).value}] {entry.name}: {entry.status}")
        print(f"Consequence: {entry.consequence}")

    with out.governance_assessments():
        out.line(
            "non-A sector inventory populated",
            StatusMark.PASS,
            f"{len(entries)} sectors audited for possible exterior mass leakage",
        )


def case_2_classification_summary(summary: InventorySummary, out: ScriptOutput) -> None:
    header("Case 2: Inventory classification summary")
    print(f"Total audited sectors: {summary.total}")
    print(f"Theorem targets: {summary.theorem_targets}")
    print(f"Unresolved or deferred: {summary.unresolved_or_deferred}")
    print(f"Risk entries: {summary.risks}")
    print(f"Diagnostic / role-level / provisional safe-if entries: {summary.diagnostic_or_role_level}")
    print(f"Not insertable or rejected entries: {summary.not_insertable_or_rejected}")
    print()
    print("Inventory result:")
    print()
    print("  No non-A sector is licensed here as an independent ordinary exterior mass carrier.")
    print("  Every non-A route either requires delta M_A = 0, remains diagnostic/non-metric,")
    print("  remains role-level, is deferred, or is non-insertable.")

    with out.governance_assessments():
        out.line(
            "no non-A exterior mass carrier licensed",
            StatusMark.PASS,
            "inventory produces requirements and deferrals, not a second mass law",
        )

    with out.unresolved_obligations():
        out.line(
            "derive non-A mass neutrality theorem",
            StatusMark.OBLIGATION,
            "ordinary closed regime still needs delta M_A|non-A = 0 sector by sector",
        )


def case_3_failure_controls(out: ScriptOutput) -> None:
    header("Case 3: Failure controls")
    print("The non-A mass-neutrality audit fails if a later script allows:")
    print()
    print("1. zeta/kappa/J_V/curvature/correction residuals to carry a nonzero 1/r scalar tail")
    print("2. a non-A boundary or smoothing layer to tune exterior A'")
    print("3. ordinary matter to be routed into multiple independent mass sources")
    print("4. O to enforce mass neutrality without domain/kernel/image/boundary law")
    print("5. J_sub to gravitate by being a pure wind")
    print("6. J_exch, R_V, or curvature balance to repair ordinary-sector mismatch")
    print("7. e_curv, e_kappa, or epsilon_vac_config to become source reservoirs")
    print("8. H_curv/H_exch to enter a parent equation before definition and neutrality")
    print("9. dark labels to patch ordinary mass leakage")
    print("10. Schwarzschild/PPN/recovery targets to choose a non-A mass route")

    with out.governance_assessments():
        out.line(
            "no second mass spoon guardrail",
            StatusMark.OBLIGATION,
            "future scripts must not convert non-A labels into exterior mass sources by declaration",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("The inventory result is intentionally conservative:")
    print()
    print("  M_A remains the only currently licensed reduced ordinary exterior mass charge.")
    print("  Non-A sectors are not proven mass-neutral here.")
    print("  Instead, this script records the sector-by-sector theorem burden.")
    print()
    print("Current Group 21 rule:")
    print()
    print("  non-A sectors must satisfy delta M_A = 0, remain diagnostic,")
    print("  remain non-metric, stay role-level, or remain theorem-targeted.")
    print()
    print("Possible next script:")
    print("  candidate_residual_scalar_tail_flux_audit.py")

    with out.governance_assessments():
        out.line(
            "non-A mass-neutrality inventory complete",
            StatusMark.PASS,
            "next step should test residual scalar tails by surface flux",
        )


# =============================================================================
# Archive recording
# =============================================================================


def record_inventory_marker(ns, entries: List[NonAMassNeutralityEntry], summary: InventorySummary) -> None:
    # This marker exists only so downstream scripts can verify the inventory ran.
    # The contentful records are the claims, obligations, route, and branch decision below.
    sector_symbols = [sp.Symbol(entry.sector.replace(" / ", "_").replace(" ", "_")) for entry in entries]
    output = sp.Symbol("non_A_mass_neutrality_inventory_complete_21")
    ns.record_derivation(
        derivation_id="non_A_sector_mass_neutrality_inventory_marker_21",
        inputs=sector_symbols,
        output=output,
        method="sector-by-sector governance inventory; no symbolic theorem claimed",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        result_type="inventory_marker",
        scope=f"{summary.total} non-A sectors audited for mass-neutrality obligations",
    )


def record_obligations(ns, entries: List[NonAMassNeutralityEntry]) -> None:
    for entry in entries:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=entry.obligation_id,
            script_id=SCRIPT_ID,
            title=f"Prove mass neutrality for {entry.sector}",
            status=ObligationStatus.OPEN,
            required_by=["ordinary_closed_regime_mass_neutrality_theorem_21"],
            description=(
                f"Current role: {entry.current_role}. Required condition: {entry.required_condition}. "
                f"This sector must not change M_A or measured M_ext unless a future parent identity "
                f"or sector-specific source law derives the modification."
            ),
        ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_ordinary_closed_regime_mass_neutrality_theorem_21",
        script_id=SCRIPT_ID,
        title="Derive ordinary closed-regime mass neutrality theorem",
        status=ObligationStatus.OPEN,
        required_by=["group21_mass_neutrality_audit_route"],
        description=(
            "Show that M_ext = M_A in the ordinary closed regime and that every non-A sector "
            "is mass-neutral, diagnostic-only, non-metric, compact/neutral, role-level, or deferred."
        ),
    ))


def record_governance(ns, entries: List[NonAMassNeutralityEntry], summary: InventorySummary) -> None:
    obligation_ids = [entry.obligation_id for entry in entries]
    obligation_ids.append("derive_ordinary_closed_regime_mass_neutrality_theorem_21")

    ns.record_route(RouteRecord(
        route_id="non_A_sector_mass_neutrality_audit_route_21",
        script_id=SCRIPT_ID,
        name="Non-A sector mass-neutrality audit route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "M_A remains the reduced ordinary exterior reference mass charge",
            "no active O is assumed to enforce neutrality",
            "each non-A sector proves delta M_A = 0 or remains diagnostic/non-metric/deferred",
            "scalar tails, boundary flux, and source double-counting are audited before parent insertion",
        ],
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_non_A_exterior_mass_carrier_branches_21",
        script_id=SCRIPT_ID,
        branch_id="non_A_exterior_mass_carrier_branches",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=obligation_ids,
        description=(
            "All non-A exterior mass-carrier branches remain deferred pending sector-specific "
            "mass-neutrality, boundary-neutrality, scalar-silence, and source-routing theorems."
        ),
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_second_mass_spoon_by_declaration_21",
        script_id=SCRIPT_ID,
        branch_id="second_mass_spoon_by_declaration",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=["derive_ordinary_closed_regime_mass_neutrality_theorem_21"],
        description=(
            "Reject any route where a residual scalar, current, curvature diagnostic, correction tensor, "
            "boundary label, or dark label is declared to carry ordinary exterior mass without derivation."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="non_A_sector_mass_neutrality_inventory_21",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            f"The Group 21 inventory audited {summary.total} non-A sector roles. No non-A sector is "
            "licensed by this script as an independent ordinary exterior mass carrier; each must prove "
            "delta M_A = 0, remain diagnostic/non-metric/role-level, or stay theorem-targeted."
        ),
        derivation_ids=["non_A_sector_mass_neutrality_inventory_marker_21"],
        obligation_ids=obligation_ids,
    ))

    ns.record_claim(ClaimRecord(
        claim_id="A_sector_remains_only_licensed_mass_coin_after_inventory_21",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "After the non-A inventory, the A-sector mass charge remains the only currently licensed "
            "reduced ordinary exterior mass coin. This is a governance rule for Group 21, not a final "
            "parent mass theorem."
        ),
        derivation_ids=[
            "A_sector_mass_definition_21",
            "A_sector_schwarzschild_mass_residual_21",
            "non_A_sector_mass_neutrality_inventory_marker_21",
        ],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Non-A Sector Mass-Neutrality Inventory")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    entries = build_entries()
    summary = build_summary(entries)

    case_0_problem_statement(out)
    case_1_print_inventory(entries, out)
    case_2_classification_summary(summary, out)
    case_3_failure_controls(out)
    final_interpretation(out)

    record_inventory_marker(ns, entries, summary)
    record_obligations(ns, entries)
    record_governance(ns, entries, summary)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
