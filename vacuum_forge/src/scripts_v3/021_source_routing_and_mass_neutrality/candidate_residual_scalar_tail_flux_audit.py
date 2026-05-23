# Candidate residual scalar tail flux audit
#
# Group:
#   21_source_routing_and_mass_neutrality
#
# Script type:
#   DERIVATION / DIAGNOSTIC / REQUIREMENTS
#
# Purpose
# -------
# Audit exterior residual scalar tails by surface flux after the A-sector mass
# charge and non-A mass-leak inventory have been defined.
#
# Locked-door question:
#
#   What exterior scalar tails are automatically mass-dangerous?
#
# This script does not prove scalar silence for every sector.
# It does not define a parent scalar field, zeta field equation, kappa field
# equation, J_V flux law, curvature current, correction tensor, or boundary law.
#
# It derives the reduced surface-flux fact:
#
#   phi_tail = C/r
#   F_phi = 4*pi*r^2*phi_tail' = -4*pi*C
#
# Therefore a residual ordinary-sector 1/r scalar tail has nonzero exterior
# scalar flux unless C = 0 or a future theorem explicitly routes that tail
# through the A-sector mass charge.

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
        dependency_id="non_A_sector_mass_neutrality_inventory_dependency_21",
        upstream_script_id="21_source_routing_and_mass_neutrality__candidate_non_A_sector_mass_neutrality_inventory",
        upstream_derivation_id="non_A_sector_mass_neutrality_inventory_marker_21",
        expected_record_kind=RecordKind.INVENTORY_MARKER,
    )
    ns.declare_dependency(
        dependency_id="A_sector_mass_definition_dependency_21",
        upstream_script_id="21_source_routing_and_mass_neutrality__candidate_A_sector_mass_charge_definition",
        upstream_derivation_id="A_sector_mass_definition_21",
        expected_record_kind=RecordKind.DERIVATION,
    )

    return archive, ns, invalidated


def status_mark(status: str) -> StatusMark:
    return {
        "DERIVED_REDUCED": StatusMark.PASS,
        "DIAGNOSTIC": StatusMark.INFO,
        "REQUIRED": StatusMark.OBLIGATION,
        "THEOREM_TARGET": StatusMark.DEFER,
        "REJECTED": StatusMark.FAIL,
        "SAFE_IF": StatusMark.INFO,
        "UNRESOLVED": StatusMark.DEFER,
        "RISK": StatusMark.WARN,
    }.get(status, StatusMark.INFO)


# =============================================================================
# Data models
# =============================================================================


@dataclass
class ScalarTailExpressionSet:
    r: sp.Symbol
    C: sp.Symbol
    n: sp.Symbol
    phi_tail: sp.Expr
    dphi_dr: sp.Expr
    F_phi: sp.Expr
    flux_residual: sp.Expr
    zero_flux_condition: sp.Equality
    phi_power: sp.Expr
    F_power: sp.Expr
    F_power_at_n1: sp.Expr
    F_power_at_n2: sp.Expr


@dataclass
class ScalarTailSectorEntry:
    name: str
    sector: str
    dangerous_tail: str
    why_dangerous: str
    required_condition: str
    current_status: str
    consequence: str
    obligation_id: str


@dataclass
class ScalarTailBranchEntry:
    name: str
    branch: str
    status: str
    condition: str
    consequence: str


# =============================================================================
# Symbolic construction
# =============================================================================


def build_tail_expressions() -> ScalarTailExpressionSet:
    r = sp.Symbol("r", positive=True)
    C = sp.Symbol("C", real=True)
    n = sp.Symbol("n", positive=True)

    phi_tail = C / r
    dphi_dr = sp.simplify(sp.diff(phi_tail, r))
    F_phi = sp.simplify(4 * sp.pi * r**2 * dphi_dr)
    flux_residual = sp.simplify(F_phi + 4 * sp.pi * C)
    zero_flux_condition = sp.Eq(C, 0)

    phi_power = C / r**n
    F_power = sp.simplify(4 * sp.pi * r**2 * sp.diff(phi_power, r))
    F_power_at_n1 = sp.simplify(F_power.subs(n, 1))
    F_power_at_n2 = sp.simplify(F_power.subs(n, 2))

    return ScalarTailExpressionSet(
        r=r,
        C=C,
        n=n,
        phi_tail=phi_tail,
        dphi_dr=dphi_dr,
        F_phi=F_phi,
        flux_residual=flux_residual,
        zero_flux_condition=zero_flux_condition,
        phi_power=phi_power,
        F_power=F_power,
        F_power_at_n1=F_power_at_n1,
        F_power_at_n2=F_power_at_n2,
    )


def build_sector_entries() -> List[ScalarTailSectorEntry]:
    return [
        ScalarTailSectorEntry(
            name="T1: zeta residual scalar tail",
            sector="zeta_residual",
            dangerous_tail="zeta_tail = C_zeta/r",
            why_dangerous="nonzero C_zeta gives exterior scalar flux and can behave as a second scalar mass route",
            required_condition="C_zeta = 0 outside, or residual zeta is strictly non-metric / killed / compact-neutral",
            current_status="RISK",
            consequence="zeta residual cannot carry ordinary exterior scalar charge by declaration.",
            obligation_id="derive_zeta_no_exterior_scalar_tail_21",
        ),
        ScalarTailSectorEntry(
            name="T2: kappa residual scalar tail",
            sector="kappa_residual",
            dangerous_tail="kappa_tail = C_kappa/r",
            why_dangerous="nonzero C_kappa breaks exterior scalar silence and can duplicate A-sector mass response",
            required_condition="C_kappa = 0 outside, or kappa is suppressed / non-metric / compact-neutral",
            current_status="RISK",
            consequence="kappa residual remains diagnostic or theorem-targeted, not an exterior scalar mass channel.",
            obligation_id="derive_kappa_no_exterior_scalar_tail_21",
        ),
        ScalarTailSectorEntry(
            name="T3: J_V-induced scalar residue",
            sector="J_V_residue",
            dangerous_tail="phi_JV = C_JV/r",
            why_dangerous="an unresolved vacuum current leaving a 1/r residue becomes a hidden scalar current charge",
            required_condition="define J_V and prove C_JV = 0 or route it through a derived A-sector law",
            current_status="UNRESOLVED",
            consequence="J_V cannot leave a scalar residue while the current itself is undefined.",
            obligation_id="derive_JV_no_scalar_residue_21",
        ),
        ScalarTailSectorEntry(
            name="T4: curvature scalar residue",
            sector="A_curv / e_curv / J_curv residue",
            dangerous_tail="phi_curv = C_curv/r",
            why_dangerous="curvature diagnostics become source dynamics if they carry exterior scalar flux",
            required_condition="curvature objects remain diagnostic/branch-filter or prove C_curv = 0",
            current_status="THEOREM_TARGET",
            consequence="curvature admissibility cannot become scalar mass energy by being named curvature.",
            obligation_id="derive_curvature_no_scalar_residue_21",
        ),
        ScalarTailSectorEntry(
            name="T5: correction-tensor scalar leakage",
            sector="H_curv / H_exch trace leakage",
            dangerous_tail="phi_H = C_H/r",
            why_dangerous="tensor trace leakage can mimic a hidden scalar correction to exterior mass",
            required_condition="H remains non-insertable, or future tensor definition proves scalar trace neutrality C_H = 0",
            current_status="THEOREM_TARGET",
            consequence="H_curv/H_exch cannot enter as scalar tail cancellation or mass correction.",
            obligation_id="derive_H_no_scalar_leakage_21",
        ),
        ScalarTailSectorEntry(
            name="T6: boundary shell scalar residue",
            sector="boundary_smoothing / shell residue",
            dangerous_tail="phi_boundary = C_boundary/r",
            why_dangerous="a boundary shell or smoothing layer can tune exterior flux while pretending to preserve mass",
            required_condition="derive no shell scalar source and C_boundary = 0 without recovery-tuned smoothing",
            current_status="THEOREM_TARGET",
            consequence="boundary purse stays closed until scalar silence and mass preservation are derived.",
            obligation_id="derive_boundary_no_shell_scalar_residue_21",
        ),
    ]


def build_branch_entries() -> List[ScalarTailBranchEntry]:
    return [
        ScalarTailBranchEntry(
            name="B1: residual 1/r tail with C != 0",
            branch="nonzero_residual_scalar_tail",
            status="REJECTED",
            condition="F_phi = -4*pi*C is nonzero",
            consequence="ordinary-sector residual scalar tail carries exterior flux and fails scalar silence",
        ),
        ScalarTailBranchEntry(
            name="B2: residual 1/r tail with C = 0",
            branch="zero_amplitude_scalar_tail",
            status="SAFE_IF",
            condition="C = 0",
            consequence="the dangerous exterior 1/r scalar flux vanishes",
        ),
        ScalarTailBranchEntry(
            name="B3: compact or faster-decaying diagnostic residual",
            branch="compact_or_diagnostic_residual",
            status="SAFE_IF",
            condition="no exterior 1/r coefficient and no boundary shell flux",
            consequence="may remain diagnostic if it has no metric, source, boundary, or A-flux effect",
        ),
        ScalarTailBranchEntry(
            name="B4: tail routed through A-sector by future theorem",
            branch="A_sector_routed_tail",
            status="THEOREM_TARGET",
            condition="future parent/source identity derives route and avoids double counting",
            consequence="not licensed in this script; remains a high-burden future route",
        ),
    ]


# =============================================================================
# Cases
# =============================================================================


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: Residual scalar tail flux problem")
    print("Question:")
    print()
    print("  What exterior scalar tails are automatically mass-dangerous?")
    print()
    print("Reference discipline:")
    print()
    print("  A-sector mass charge remains the reduced ordinary exterior reference.")
    print("  Non-A residual scalar tails must not create a second exterior flux coin.")
    print("  This script tests the surface flux of a generic 1/r residual tail.")
    print("  It does not prove scalar silence for every sector.")
    print()

    with out.governance_assessments():
        out.line(
            "residual scalar tail audit opened",
            StatusMark.INFO,
            "testing whether a generic non-A 1/r residual carries exterior surface flux",
        )


def case_1_generic_tail_flux(exprs: ScalarTailExpressionSet, out: ScriptOutput) -> None:
    header("Case 1: Generic 1/r scalar tail flux")
    print("Take a generic residual scalar tail:")
    print()
    print(f"  phi_tail(r) = {sp.sstr(exprs.phi_tail)}")
    print()
    print("Then:")
    print()
    print(f"  dphi_tail/dr = {sp.sstr(exprs.dphi_dr)}")
    print()
    print("The reduced surface flux is:")
    print()
    print(f"  F_phi = 4*pi*r^2*dphi_tail/dr = {sp.sstr(exprs.F_phi)}")
    print()
    print("Flux residual:")
    print()
    print(f"  F_phi + 4*pi*C = {sp.sstr(exprs.flux_residual)}")
    print()
    print("Neutrality condition for this tail:")
    print()
    print(f"  {sp.sstr(exprs.zero_flux_condition)}")

    tail_flux_ok = is_zero(exprs.flux_residual)
    nonzero_flux = not is_zero(exprs.F_phi)

    with out.derived_results():
        out.line(
            "1/r tail flux derived",
            StatusMark.PASS if tail_flux_ok else StatusMark.FAIL,
            f"F_phi = {sp.sstr(exprs.F_phi)}",
        )
        out.line(
            "generic nonzero C gives nonzero scalar flux",
            StatusMark.PASS if nonzero_flux else StatusMark.FAIL,
            "F_phi vanishes only when the tail coefficient C vanishes",
        )


def case_2_power_tail_diagnostic(exprs: ScalarTailExpressionSet, out: ScriptOutput) -> None:
    header("Case 2: Power-tail diagnostic")
    print("For a diagnostic power tail:")
    print()
    print(f"  phi_n(r) = {sp.sstr(exprs.phi_power)}")
    print()
    print("the reduced surface flux is:")
    print()
    print(f"  F_n = {sp.sstr(exprs.F_power)}")
    print()
    print("Special cases:")
    print()
    print(f"  n = 1: F_n = {sp.sstr(exprs.F_power_at_n1)}")
    print(f"  n = 2: F_n = {sp.sstr(exprs.F_power_at_n2)}")
    print()
    print("Interpretation:")
    print()
    print("  The 1/r tail is the constant-flux danger.")
    print("  Faster falloff may remove far-zone constant flux, but still needs boundary/domain checks.")

    with out.sample_results():
        out.line(
            "1/r tail is constant-flux scalar residue",
            StatusMark.PASS if sp.simplify(exprs.F_power_at_n1 - exprs.F_phi) == 0 else StatusMark.FAIL,
            f"F_n at n=1 is {sp.sstr(exprs.F_power_at_n1)}",
        )
        out.line(
            "faster-falloff diagnostic still boundary-sensitive",
            StatusMark.INFO,
            f"F_n at n=2 is {sp.sstr(exprs.F_power_at_n2)}",
        )


def case_3_sector_tail_inventory(entries: List[ScalarTailSectorEntry], out: ScriptOutput) -> None:
    header("Case 3: Sector tail inventory")
    for entry in entries:
        print()
        print("-" * 120)
        print(entry.name)
        print("-" * 120)
        print(f"Sector: {entry.sector}")
        print(f"Dangerous tail: {entry.dangerous_tail}")
        print(f"Why dangerous: {entry.why_dangerous}")
        print(f"Required condition: {entry.required_condition}")
        print(f"[{status_mark(entry.current_status).value}] {entry.name}: {entry.current_status}")
        print(f"Consequence: {entry.consequence}")

    with out.governance_assessments():
        out.line(
            "sector scalar-tail inventory populated",
            StatusMark.PASS,
            f"{len(entries)} residual-tail sectors audited for scalar-flux danger",
        )


def case_4_branch_classification(branches: List[ScalarTailBranchEntry], out: ScriptOutput) -> None:
    header("Case 4: Branch classification")
    for branch in branches:
        print()
        print("-" * 120)
        print(branch.name)
        print("-" * 120)
        print(f"Branch: {branch.branch}")
        print(f"Condition: {branch.condition}")
        print(f"[{status_mark(branch.status).value}] {branch.name}: {branch.status}")
        print(f"Consequence: {branch.consequence}")

    with out.counterexamples():
        out.line(
            "nonzero residual 1/r scalar tail rejected",
            StatusMark.FAIL,
            "C != 0 gives F_phi = -4*pi*C, a nonzero exterior scalar flux",
        )

    with out.governance_assessments():
        out.line(
            "scalar-tail branch ledger complete",
            StatusMark.PASS,
            "safe branches require C = 0, compact/diagnostic behavior, or future A-sector routing theorem",
        )


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("The residual scalar-tail audit fails if a later script allows:")
    print()
    print("1. zeta or kappa residuals to carry C/r outside with C != 0")
    print("2. J_V to leave a scalar 1/r residue while undefined")
    print("3. curvature diagnostics to become scalar curvature charge")
    print("4. H_curv/H_exch trace leakage to cancel or modify exterior mass")
    print("5. boundary smoothing or shell behavior to leave C_boundary/r")
    print("6. scalar silence to be imposed by O without kernel/image/boundary law")
    print("7. faster falloff to be treated as safe without boundary/domain checks")
    print("8. a residual scalar tail to be routed through A without a no-double-counting theorem")

    with out.unresolved_obligations():
        out.line(
            "derive residual scalar silence theorem",
            StatusMark.OBLIGATION,
            "show all ordinary-sector residual scalar tail coefficients vanish or are non-metric/diagnostic",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("The symbolic result is simple:")
    print()
    print("  phi_tail = C/r")
    print("  F_phi = 4*pi*r^2*phi_tail' = -4*pi*C")
    print()
    print("Therefore:")
    print()
    print("  an ordinary-sector residual 1/r scalar tail is not neutral unless C = 0")
    print("  or a future theorem explicitly routes it through the A-sector mass charge")
    print("  without double-counting.")
    print()
    print("This script does not prove scalar silence sector by sector.")
    print("It gives the reduced flux witness that defines the next proof burden.")
    print()
    print("Possible next script:")
    print("  candidate_boundary_flux_mass_preservation.py")

    with out.governance_assessments():
        out.line(
            "residual scalar-tail flux audit complete",
            StatusMark.PASS,
            "ordinary residual scalar silence requires vanishing 1/r coefficients",
        )


# =============================================================================
# Archive recording
# =============================================================================


def record_derivations(ns, exprs: ScalarTailExpressionSet) -> None:
    ns.record_derivation(
        derivation_id="residual_scalar_tail_flux_1_over_r_21",
        inputs=[exprs.phi_tail, exprs.r, exprs.C],
        output=exprs.F_phi,
        method="F_phi = simplify(4*pi*r**2*diff(C/r, r))",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="surface_flux",
        scope="reduced static spherical exterior residual scalar tail",
    )

    ns.record_derivation(
        derivation_id="residual_scalar_tail_flux_residual_21",
        inputs=[exprs.F_phi, exprs.C],
        output=exprs.flux_residual,
        method="simplify(F_phi + 4*pi*C)",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
        scope="reduced scalar-tail flux identity",
    )

    ns.record_derivation(
        derivation_id="residual_scalar_tail_zero_flux_condition_21",
        inputs=[exprs.F_phi],
        output=exprs.zero_flux_condition,
        method="solve F_phi = 0 for 1/r tail coefficient",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="neutrality_condition",
        scope="ordinary-sector residual 1/r scalar tail",
    )

    ns.record_derivation(
        derivation_id="residual_power_tail_flux_diagnostic_21",
        inputs=[exprs.phi_power, exprs.r, exprs.C, exprs.n],
        output=exprs.F_power,
        method="F_n = simplify(4*pi*r**2*diff(C/r**n, r))",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        result_type="surface_flux_diagnostic",
        scope="power-law residual scalar tail diagnostic",
    )


def record_obligations(ns, entries: List[ScalarTailSectorEntry]) -> None:
    for entry in entries:
        ns.record_obligation(ProofObligationRecord(
            obligation_id=entry.obligation_id,
            script_id=SCRIPT_ID,
            title=f"Prove no exterior scalar tail for {entry.sector}",
            status=ObligationStatus.OPEN,
            required_by=["ordinary_closed_regime_scalar_silence_theorem_21"],
            description=(
                f"Dangerous form: {entry.dangerous_tail}. Required condition: {entry.required_condition}. "
                "The sector must not leave a nonzero ordinary exterior 1/r scalar tail unless a future "
                "source-routing theorem explicitly routes it through the A-sector without double counting."
            ),
        ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_ordinary_closed_regime_scalar_silence_theorem_21",
        script_id=SCRIPT_ID,
        title="Derive ordinary closed-regime scalar silence theorem",
        status=ObligationStatus.OPEN,
        required_by=["ordinary_closed_regime_mass_neutrality_theorem_21"],
        description=(
            "Show that ordinary-sector non-A residual scalar tails have zero 1/r coefficient, "
            "remain non-metric/diagnostic, are compact-neutral with no shell flux, or are routed "
            "through a derived A-sector source law without double counting."
        ),
    ))


def record_governance(
    ns,
    entries: List[ScalarTailSectorEntry],
    branches: List[ScalarTailBranchEntry],
) -> None:
    obligation_ids = [entry.obligation_id for entry in entries]
    obligation_ids.append("derive_ordinary_closed_regime_scalar_silence_theorem_21")

    ns.record_route(RouteRecord(
        route_id="residual_scalar_tail_flux_audit_route_21",
        script_id=SCRIPT_ID,
        name="Residual scalar-tail flux audit route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=obligation_ids,
        activation_conditions=[
            "A-sector mass charge remains the reduced exterior reference",
            "non-A residual scalar tails are audited by surface flux",
            "ordinary residual 1/r coefficients vanish unless a future A-sector routing theorem is derived",
            "no active O or boundary repair is assumed",
        ],
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_nonzero_residual_1_over_r_tail_21",
        script_id=SCRIPT_ID,
        branch_id="nonzero_residual_scalar_1_over_r_tail",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=["derive_ordinary_closed_regime_scalar_silence_theorem_21"],
        description=(
            "Reject ordinary-sector residual scalar tails phi = C/r with C != 0 as neutral branches, "
            "because the reduced surface flux is F_phi = -4*pi*C. A future theorem may route scalar "
            "content through the A-sector only if it also proves no double counting."
        ),
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_A_sector_routed_residual_tail_21",
        script_id=SCRIPT_ID,
        branch_id="A_sector_routed_residual_scalar_tail",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "derive_ordinary_closed_regime_scalar_silence_theorem_21",
            "derive_ordinary_closed_regime_mass_neutrality_theorem_21",
        ],
        description=(
            "Defer any route that tries to keep a residual scalar tail by routing it through A-sector mass. "
            "Such a route requires a future source identity and no-double-counting theorem."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="residual_1_over_r_tail_flux_rule_21",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.LICENSING,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "For a reduced exterior residual scalar tail phi = C/r, the surface flux is "
            "F_phi = 4*pi*r^2*phi' = -4*pi*C. Therefore C = 0 is required for zero flux "
            "of that residual tail."
        ),
        derivation_ids=[
            "residual_scalar_tail_flux_1_over_r_21",
            "residual_scalar_tail_flux_residual_21",
            "residual_scalar_tail_zero_flux_condition_21",
        ],
    ))

    ns.record_claim(ClaimRecord(
        claim_id="ordinary_residual_scalar_silence_requirement_21",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Ordinary-sector non-A residual scalar tails must have zero exterior 1/r coefficient, "
            "remain diagnostic/non-metric/compact-neutral, or stay theorem-targeted. A nonzero "
            "1/r residual tail is not mass-neutral by declaration."
        ),
        derivation_ids=["residual_scalar_tail_flux_1_over_r_21"],
        obligation_ids=obligation_ids,
    ))


# =============================================================================
# Main
# =============================================================================


def main() -> None:
    header("Candidate Residual Scalar Tail Flux Audit")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    exprs = build_tail_expressions()
    sector_entries = build_sector_entries()
    branch_entries = build_branch_entries()

    case_0_problem_statement(out)
    case_1_generic_tail_flux(exprs, out)
    case_2_power_tail_diagnostic(exprs, out)
    case_3_sector_tail_inventory(sector_entries, out)
    case_4_branch_classification(branch_entries, out)
    case_5_failure_controls(out)
    final_interpretation(out)

    record_derivations(ns, exprs)
    record_obligations(ns, sector_entries)
    record_governance(ns, sector_entries, branch_entries)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
