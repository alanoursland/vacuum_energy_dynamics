# Candidate A-sector mass charge definition
#
# Group:
#   21_source_routing_and_mass_neutrality
#
# Script type:
#   DERIVATION / REQUIREMENTS
#
# Purpose
# -------
# Define the operational exterior mass charge currently licensed by the reduced
# theory: the A-sector areal flux charge.
#
# Locked-door question:
#
#   What is the operational exterior mass charge in the current theory?
#
# This script does not define a parent mass, ADM mass, correction-tensor mass,
# curvature mass, zeta mass, kappa mass, or vacuum-current mass.
#
# It only establishes the reduced ordinary-exterior reference charge:
#
#   F_A(r) = 4*pi*r^2*A'(r)
#   M_A(r) = c^2*F_A(r)/(8*pi*G)
#
# and verifies that, for the reduced Schwarzschild exterior A-sector solution,
# M_A = M.

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


@dataclass
class MassChargeExpressionSet:
    r: sp.Symbol
    G: sp.Symbol
    c: sp.Symbol
    M: sp.Symbol
    A: sp.Expr
    F_A: sp.Expr
    M_A: sp.Expr
    dF_A_dr: sp.Expr
    mass_residual: sp.Expr


@dataclass
class MassChargeLedgerEntry:
    name: str
    statement: str
    status: str
    consequence: str


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)

    ns.declare_dependency(
        dependency_id="group20_no_overlap_projection_status_marker",
        upstream_script_id="020_no_overlap_and_projection_operators__candidate_no_overlap_projection_group_status_summary",
        upstream_derivation_id="no_overlap_projection_group_status_summary_marker",
        expected_record_kind=RecordKind.INVENTORY_MARKER,
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


def status_mark(status: str) -> StatusMark:
    return {
        "DERIVED_REDUCED": StatusMark.PASS,
        "REFERENCE": StatusMark.PASS,
        "REQUIRED": StatusMark.OBLIGATION,
        "THEOREM_TARGET": StatusMark.DEFER,
        "REJECTED": StatusMark.FAIL,
        "SAFE_IF": StatusMark.INFO,
        "UNRESOLVED": StatusMark.DEFER,
    }.get(status, StatusMark.INFO)


def build_mass_charge_expressions() -> MassChargeExpressionSet:
    r = sp.Symbol("r", positive=True)
    G = sp.Symbol("G", positive=True)
    c = sp.Symbol("c", positive=True)
    M = sp.Symbol("M", positive=True)

    A = 1 - (2 * G * M) / (c**2 * r)
    F_A = sp.simplify(4 * sp.pi * r**2 * sp.diff(A, r))
    M_A = sp.simplify((c**2 / (8 * sp.pi * G)) * F_A)
    dF_A_dr = sp.simplify(sp.diff(F_A, r))
    mass_residual = sp.simplify(M_A - M)

    return MassChargeExpressionSet(
        r=r,
        G=G,
        c=c,
        M=M,
        A=A,
        F_A=F_A,
        M_A=M_A,
        dF_A_dr=dF_A_dr,
        mass_residual=mass_residual,
    )


def build_ledger() -> List[MassChargeLedgerEntry]:
    return [
        MassChargeLedgerEntry(
            name="A1: A-sector flux definition",
            statement="Define F_A(r) = 4*pi*r^2*A'(r) as the reduced areal A-flux.",
            status="DERIVED_REDUCED",
            consequence="A-flux is the operational exterior mass-charge carrier in the reduced ordinary exterior.",
        ),
        MassChargeLedgerEntry(
            name="A2: A-sector mass definition",
            statement="Define M_A(r) = c^2*F_A(r)/(8*pi*G).",
            status="REFERENCE",
            consequence="All non-A sectors in Group 21 are audited against delta M_A = 0.",
        ),
        MassChargeLedgerEntry(
            name="A3: exterior Schwarzschild A check",
            statement="For A = 1 - 2GM/(c^2*r), the A-flux gives M_A = M.",
            status="DERIVED_REDUCED",
            consequence="The reduced A-sector reproduces the exterior mass charge used by the current ordinary branch.",
        ),
        MassChargeLedgerEntry(
            name="A4: vacuum constancy check",
            statement="For the exterior A solution, dF_A/dr = 0.",
            status="DERIVED_REDUCED",
            consequence="The exterior A-flux is conserved outside the source.",
        ),
        MassChargeLedgerEntry(
            name="A5: non-A mass neutrality requirement",
            statement="Non-A sectors may not shift M_A unless a future parent identity derives a new total mass law.",
            status="REQUIRED",
            consequence="zeta, kappa, J_V, currents, curvature diagnostics, and H candidates must show empty mass pockets.",
        ),
        MassChargeLedgerEntry(
            name="A6: no second mass spoon",
            statement="No residual scalar, current, curvature, correction tensor, boundary, or dark label may become a second exterior mass source by declaration.",
            status="REQUIRED",
            consequence="Next script should inventory all non-A mass-leak routes.",
        ),
    ]


def case_0_problem_statement(out: ScriptOutput) -> None:
    header("Case 0: A-sector exterior mass charge problem")
    print("Question:")
    print()
    print("  What is the operational exterior mass charge in the current theory?")
    print()
    print("Goal:")
    print()
    print("  define the reduced A-sector mass charge before auditing non-A sectors")
    print()
    print("Discipline:")
    print()
    print("  A-sector mass charge is a reduced ordinary-exterior reference")
    print("  it is not a final covariant parent mass definition")
    print("  non-A sectors may not shift it by declaration")
    print("  recovery checks may test the exterior branch but may not define new mass routes")
    print()
    with out.governance_assessments():
        out.line(
            "A-sector mass audit opened",
            StatusMark.INFO,
            "M_A is defined first; non-A neutrality is audited later",
        )


def case_1_define_reference_charge(exprs: MassChargeExpressionSet, out: ScriptOutput) -> None:
    header("Case 1: Define A-sector mass charge")
    print("Definitions:")
    print()
    print("  F_A(r) = 4*pi*r^2*dA/dr")
    print("  M_A(r) = c^2*F_A(r)/(8*pi*G)")
    print()
    print("Current exterior A-sector solution:")
    print()
    print(f"  A(r) = {sp.sstr(exprs.A)}")
    print()
    print("This script treats M_A as the operational reduced exterior mass charge.")
    print("It does not define a final parent mass, ADM mass, or non-A mass contribution.")
    with out.derived_results():
        out.line(
            "A-sector reference charge defined",
            StatusMark.PASS,
            "M_A = c^2*F_A/(8*pi*G)",
        )


def case_2_schwarzschild_flux_check(exprs: MassChargeExpressionSet, out: ScriptOutput) -> None:
    header("Case 2: Exterior Schwarzschild A-flux check")
    print("For:")
    print()
    print(f"  A(r) = {sp.sstr(exprs.A)}")
    print()
    print("the derivative is:")
    print()
    print(f"  A'(r) = {sp.sstr(sp.diff(exprs.A, exprs.r))}")
    print()
    print("so the areal A-flux is:")
    print()
    print(f"  F_A(r) = {sp.sstr(exprs.F_A)}")
    print()
    print("and the A-sector mass charge is:")
    print()
    print(f"  M_A(r) = {sp.sstr(exprs.M_A)}")
    print()
    print("mass residual:")
    print()
    print(f"  M_A - M = {sp.sstr(exprs.mass_residual)}")
    print()
    with out.derived_results():
        out.line(
            "Schwarzschild A-flux mass check",
            StatusMark.PASS if exprs.mass_residual == 0 else StatusMark.FAIL,
            f"M_A - M simplifies to {sp.sstr(exprs.mass_residual)}",
        )


def case_3_exterior_flux_constancy(exprs: MassChargeExpressionSet, out: ScriptOutput) -> None:
    header("Case 3: Exterior A-flux constancy")
    print("For the exterior A-sector solution:")
    print()
    print(f"  F_A(r) = {sp.sstr(exprs.F_A)}")
    print()
    print("therefore:")
    print()
    print(f"  dF_A/dr = {sp.sstr(exprs.dF_A_dr)}")
    print()
    print("Interpretation:")
    print()
    print("  exterior A-flux is constant outside the source")
    print("  the constant flux defines the reduced exterior mass charge")
    print("  later sectors must not shift this charge without a derived parent identity")
    with out.derived_results():
        out.line(
            "exterior A-flux conserved",
            StatusMark.PASS if exprs.dF_A_dr == 0 else StatusMark.FAIL,
            f"dF_A/dr simplifies to {sp.sstr(exprs.dF_A_dr)}",
        )


def case_4_mass_charge_ledger(entries: List[MassChargeLedgerEntry], out: ScriptOutput) -> None:
    header("Case 4: A-sector mass-charge ledger")
    for entry in entries:
        print()
        print("-" * 120)
        print(entry.name)
        print("-" * 120)
        print(f"Statement: {entry.statement}")
        print(f"[{status_mark(entry.status).value}] {entry.name}: {entry.status}")
        print(f"Consequence: {entry.consequence}")
    with out.governance_assessments():
        out.line(
            "A-sector mass-charge ledger complete",
            StatusMark.PASS,
            "A-sector reference charge ready for non-A neutrality audit",
        )


def case_5_failure_controls(out: ScriptOutput) -> None:
    header("Case 5: Failure controls")
    print("This A-sector mass-charge definition fails if later scripts allow:")
    print()
    print("1. zeta or kappa residuals to carry a 1/r exterior scalar tail")
    print("2. J_V to shift exterior mass without a derived flux law")
    print("3. J_sub to gravitate by being a pure wind")
    print("4. J_exch to repair ordinary matter routing")
    print("5. A_curv or e_curv to become source energy")
    print("6. H_curv or H_exch to enter a field equation")
    print("7. boundary smoothing to preserve mass by name")
    print("8. gamma_like, AB, B=1/A, or Schwarzschild recovery to define non-A mass routes")
    print("9. ordinary T_mu_nu to be rerouted into multiple independent mass sources")
    print()
    with out.counterexamples():
        out.line(
            "second exterior mass spoon rejected",
            StatusMark.FAIL,
            "non-A sectors must not shift M_A by declaration",
        )
        out.line(
            "recovery-defined mass route rejected",
            StatusMark.FAIL,
            "recovery is downstream, not a construction rule",
        )


def final_interpretation(out: ScriptOutput) -> None:
    header("Final interpretation")
    print("The A-sector currently provides the only reduced exterior mass charge:")
    print()
    print("  M_A = c^2 F_A / (8*pi*G)")
    print()
    print("For the exterior A-sector solution:")
    print()
    print("  A = 1 - 2GM/(c^2*r)")
    print()
    print("the charge evaluates to:")
    print()
    print("  M_A = M")
    print()
    print("Therefore:")
    print()
    print("  A-sector mass charge is the reference coin for Group 21.")
    print("  All non-A sectors must prove delta M_A = 0, remain diagnostic, remain non-metric,")
    print("  or stay theorem-targeted until a future parent identity derives otherwise.")
    print()
    print("Possible next artifact:")
    print("  candidate_A_sector_mass_charge_definition.md")
    print()
    print("Possible next script:")
    print("  candidate_non_A_sector_mass_neutrality_inventory.py")
    with out.governance_assessments():
        out.line(
            "A-sector mass charge established as Group 21 reference",
            StatusMark.PASS,
            "non-A sectors must show empty mass pockets",
        )


def record_derivations(ns, exprs: MassChargeExpressionSet) -> None:
    ns.record_derivation(
        derivation_id="A_sector_flux_definition_21",
        inputs=[exprs.A],
        output=exprs.F_A,
        method="F_A = simplify(4*pi*r**2*diff(A, r))",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="areal_flux_definition",
        scope="reduced static spherical ordinary exterior",
    )

    ns.record_derivation(
        derivation_id="A_sector_mass_definition_21",
        inputs=[exprs.F_A],
        output=exprs.M_A,
        method="M_A = simplify(c**2*F_A/(8*pi*G))",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="mass_charge_definition",
        scope="reduced static spherical ordinary exterior",
    )

    ns.record_derivation(
        derivation_id="A_sector_flux_constancy_residual_21",
        inputs=[exprs.F_A],
        output=exprs.dF_A_dr,
        method="simplify(diff(F_A, r))",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
        scope="Schwarzschild exterior A-sector branch",
    )

    ns.record_derivation(
        derivation_id="A_sector_schwarzschild_mass_residual_21",
        inputs=[exprs.A, exprs.F_A, exprs.M_A],
        output=exprs.mass_residual,
        method="simplify(M_A - M)",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
        scope="Schwarzschild exterior A-sector branch",
    )


def record_governance(ns) -> None:
    ns.record_obligation(ProofObligationRecord(
        obligation_id="inventory_non_A_mass_neutrality_21",
        script_id=SCRIPT_ID,
        title="Inventory non-A mass neutrality obligations",
        status=ObligationStatus.OPEN,
        required_by=["group21_mass_neutrality_audit_route"],
        description=(
            "Audit B_s, zeta residual, kappa residual, epsilon_vac_config, e_kappa, "
            "J_V, J_sub, J_exch, Sigma/R, A_curv/e_curv, J_curv, H_curv/H_exch, "
            "boundary smoothing, and dark labels for possible exterior mass leakage."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_non_A_delta_MA_zero_21",
        script_id=SCRIPT_ID,
        title="Derive non-A delta M_A equals zero",
        status=ObligationStatus.OPEN,
        required_by=["ordinary_closed_regime_mass_neutrality_theorem_21"],
        description=(
            "Show that every non-A sector in the ordinary closed regime is mass-neutral, "
            "diagnostic-only, non-metric, compact/neutral, or theorem-targeted."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_boundary_mass_preservation_21",
        script_id=SCRIPT_ID,
        title="Derive boundary mass preservation",
        status=ObligationStatus.OPEN,
        required_by=["ordinary_closed_regime_mass_neutrality_theorem_21"],
        description=(
            "Show that non-A boundary behavior does not change exterior A-flux, does not "
            "create shell source, and does not tune M_ext by recovery."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_no_residual_scalar_tail_21",
        script_id=SCRIPT_ID,
        title="Derive no residual exterior scalar tail",
        status=ObligationStatus.OPEN,
        required_by=["ordinary_closed_regime_mass_neutrality_theorem_21"],
        description=(
            "Show that zeta/kappa/J_V/curvature/correction-tensor residual scalar tails "
            "vanish outside ordinary sources unless routed through the A-sector mass charge."
        ),
    ))

    ns.record_route(RouteRecord(
        route_id="group21_mass_neutrality_audit_route",
        script_id=SCRIPT_ID,
        name="Group 21 source routing and mass neutrality audit",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[
            "inventory_non_A_mass_neutrality_21",
            "derive_non_A_delta_MA_zero_21",
            "derive_boundary_mass_preservation_21",
            "derive_no_residual_scalar_tail_21",
        ],
        activation_conditions=[
            "A-sector mass charge remains the reduced exterior reference",
            "non-A sectors are audited against delta M_A = 0",
            "no recovery target defines a non-A mass route",
            "no active O is assumed",
        ],
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_non_A_mass_carrier_routes_21",
        script_id=SCRIPT_ID,
        branch_id="non_A_exterior_mass_carrier",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "derive_non_A_delta_MA_zero_21",
            "derive_boundary_mass_preservation_21",
            "derive_no_residual_scalar_tail_21",
        ],
        description=(
            "Non-A sectors are deferred as exterior mass carriers unless a future parent identity "
            "or sector-specific theorem derives a modified mass law."
        ),
    ))

    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="reject_mass_neutrality_by_declaration_21",
        script_id=SCRIPT_ID,
        branch_id="mass_neutrality_by_declaration",
        status=GovernanceStatus.REJECTED_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=["derive_non_A_delta_MA_zero_21"],
        description=(
            "Reject mass neutrality by declaration: zeta, kappa, currents, curvature diagnostics, "
            "correction tensors, and boundary smoothing must not be called neutral without a check."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="A_sector_mass_charge_reference_21",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.LICENSING,
        status=GovernanceStatus.LICENSED_CLAIM,
        statement=(
            "In the reduced static spherical ordinary exterior, the A-sector areal flux defines "
            "the current operational mass charge M_A = c^2 F_A/(8*pi*G), and the Schwarzschild "
            "A-sector branch gives M_A = M."
        ),
        derivation_ids=[
            "A_sector_flux_definition_21",
            "A_sector_mass_definition_21",
            "A_sector_flux_constancy_residual_21",
            "A_sector_schwarzschild_mass_residual_21",
        ],
    ))

    ns.record_claim(ClaimRecord(
        claim_id="non_A_mass_routes_require_neutrality_21",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Group 21 should audit all non-A sectors against delta M_A = 0. No non-A sector "
            "is currently licensed to shift ordinary exterior mass by declaration."
        ),
        derivation_ids=["A_sector_schwarzschild_mass_residual_21"],
        obligation_ids=[
            "inventory_non_A_mass_neutrality_21",
            "derive_non_A_delta_MA_zero_21",
            "derive_boundary_mass_preservation_21",
            "derive_no_residual_scalar_tail_21",
        ],
    ))


def main() -> None:
    header("Candidate A-Sector Mass Charge Definition")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    exprs = build_mass_charge_expressions()
    entries = build_ledger()

    case_0_problem_statement(out)
    case_1_define_reference_charge(exprs, out)
    case_2_schwarzschild_flux_check(exprs, out)
    case_3_exterior_flux_constancy(exprs, out)
    case_4_mass_charge_ledger(entries, out)
    case_5_failure_controls(out)
    final_interpretation(out)

    record_derivations(ns, exprs)
    record_governance(ns)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
