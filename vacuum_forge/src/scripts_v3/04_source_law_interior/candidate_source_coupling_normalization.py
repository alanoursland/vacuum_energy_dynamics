# Group:
#   04_source_law_interior
#
# Script type:
#   DERIVATION
#
# Candidate source coupling normalization
#
# Purpose
# -------
# The boundary flux action found that a source/interface coupling:
#
#   E_boundary = -q A(R)
#
# produces the boundary condition:
#
#   2 K_A R^2 A'(R) = q
#
# Therefore:
#
#   F_A(R) = 4*pi*R^2 A'(R) = 2*pi*q/K_A
#
# To recover Schwarzschild exterior:
#
#   F_A = 8*pi*G*M/c^2
#
# so:
#
#   q_M = 4 K_A G M / c^2
#
# This script checks how that normalization follows from:
#
#   1. weak-field Newtonian matching,
#   2. Schwarzschild radius coefficient,
#   3. boundary momentum normalization,
#   4. dimensional reduced charge structure,
#   5. additivity in mass.
#
# It does not derive K_A from first principles.

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
    ScriptOutput,
    StatusMark,
)


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"


def header(title: str) -> None:
    print()
    print("=" * 112)
    print(title)
    print("=" * 112)


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def case_0_boundary_relation(out: ScriptOutput):
    header("Case 0: Boundary relation recap")

    R, K_A, q = sp.symbols("R K_A q", positive=True, real=True)

    Aprime = q/(2*K_A*R**2)
    flux = sp.simplify(4*sp.pi*R**2*Aprime)

    print("Boundary condition from action:")
    print()
    print("  2 K_A R^2 A'(R) = q")
    print()
    print(f"A'(R) = {Aprime}")
    print(f"F_A = 4*pi*R^2*A'(R) = {flux}")

    with out.derived_results():
        out.line("boundary charge q fixes A-flux",
                 StatusMark.PASS,
                 f"F_A = {flux}")


def case_1_newtonian_matching(out: ScriptOutput, ns=None):
    header("Case 1: Weak-field Newtonian matching")

    r, G, M, c, F = sp.symbols("r G M c F", positive=True, real=True)

    # Exterior conserved flux:
    #   4pi r^2 A' = F
    # so A' = F/(4pir^2)
    # with A(infty)=1:
    #   A = 1 - F/(4pi r)
    # Weak field requires:
    #   A = 1 + 2 Phi/c^2 = 1 - 2GM/(c^2 r)
    A_from_flux = 1 - F/(4*sp.pi*r)
    A_target = 1 - 2*G*M/(c**2*r)

    F_solution = sp.solve(sp.Eq(A_from_flux, A_target), F)

    print(f"A_from_flux = {A_from_flux}")
    print(f"A_target Newtonian = {A_target}")
    print(f"F solution = {F_solution}")

    newtonian_ok = (bool(F_solution) and
                    is_zero(F_solution[0] - 8*sp.pi*G*M/c**2))

    with out.derived_results():
        out.line("Newtonian matching fixes F_A=8piGM/c^2",
                 StatusMark.PASS if newtonian_ok else StatusMark.FAIL,
                 f"F_solution = {F_solution}")

    if ns is not None:
        ns.record_derivation(
            derivation_id="newtonian_matching_flux_normalization",
            inputs=[A_from_flux, A_target, r, G, M, c],
            output=F_solution[0] if F_solution else sp.nan,
            method="solve F from A=1-F/(4pi r) vs A=1-2GM/(c^2 r)",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="normalization",
        )


def case_2_boundary_charge_from_flux(out: ScriptOutput, ns=None):
    header("Case 2: Boundary charge from flux")

    K_A, G, M, c = sp.symbols("K_A G M c", positive=True, real=True)

    F_target = 8*sp.pi*G*M/c**2
    q_from_flux = sp.simplify(K_A * F_target / (2*sp.pi))
    q_target = 4*K_A*G*M/c**2

    print(f"F_target = {F_target}")
    print("Since F_A = 2*pi*q/K_A:")
    print(f"q = K_A*F/(2*pi) = {q_from_flux}")
    print(f"q_target = {q_target}")

    residual = sp.simplify(q_from_flux - q_target)
    ok = is_zero(residual)

    with out.derived_results():
        out.line("boundary charge normalization follows from Newtonian flux",
                 StatusMark.PASS if ok else StatusMark.FAIL,
                 f"q_from_flux - q_target = {residual}")

    if ns is not None:
        ns.record_derivation(
            derivation_id="boundary_charge_normalization_derivation",
            inputs=[F_target, K_A],
            output=residual,
            method="q = K_A * F_target / (2*pi) vs q_target = 4*K_A*G*M/c^2",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="normalization_residual",
        )


def case_3_schwarzschild_radius_matching(out: ScriptOutput, ns=None):
    header("Case 3: Schwarzschild radius coefficient matching")

    r, r_s, G, M, c, F = sp.symbols("r r_s G M c F", positive=True, real=True)

    A = 1 - r_s/r
    flux = sp.simplify(4*sp.pi*r**2*sp.diff(A, r))
    F_target = 8*sp.pi*G*M/c**2

    rs_solution = sp.solve(sp.Eq(flux, F_target), r_s)

    print(f"A = {A}")
    print(f"F_A = {flux}")
    print(f"F_target = {F_target}")
    print(f"r_s solution = {rs_solution}")

    rs_ok = (bool(rs_solution) and
             is_zero(rs_solution[0] - 2*G*M/c**2))

    with out.derived_results():
        out.line("flux normalization fixes r_s=2GM/c^2",
                 StatusMark.PASS if rs_ok else StatusMark.FAIL,
                 f"r_s = {rs_solution}")

    if ns is not None:
        ns.record_derivation(
            derivation_id="schwarzschild_radius_flux_derivation",
            inputs=[A, flux, F_target],
            output=rs_solution[0] if rs_solution else sp.nan,
            method="solve r_s from 4pi*r^2*dA/dr = 8piGM/c^2",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="coefficient",
        )


def case_4_additivity(out: ScriptOutput, ns=None):
    header("Case 4: Additivity in mass")

    K_A, G, c, M1, M2 = sp.symbols("K_A G c M1 M2", positive=True, real=True)

    q = lambda M: 4*K_A*G*M/c**2
    F = lambda M: 8*sp.pi*G*M/c**2

    q_total = sp.simplify(q(M1 + M2))
    q_sum = sp.simplify(q(M1) + q(M2))

    F_total = sp.simplify(F(M1 + M2))
    F_sum = sp.simplify(F(M1) + F(M2))

    print(f"q(M1+M2) = {q_total}")
    print(f"q(M1)+q(M2) = {q_sum}")
    print()
    print(f"F(M1+M2) = {F_total}")
    print(f"F(M1)+F(M2) = {F_sum}")

    q_additive = is_zero(q_total - q_sum)
    F_additive = is_zero(F_total - F_sum)

    with out.derived_results():
        out.line("boundary charge is additive in mass",
                 StatusMark.PASS if q_additive else StatusMark.FAIL,
                 f"q(M1+M2) - (q(M1)+q(M2)) = {sp.simplify(q_total - q_sum)}")
        out.line("flux is additive in mass",
                 StatusMark.PASS if F_additive else StatusMark.FAIL,
                 f"F(M1+M2) - (F(M1)+F(M2)) = {sp.simplify(F_total - F_sum)}")

    if ns is not None:
        ns.record_derivation(
            derivation_id="boundary_charge_mass_additivity",
            inputs=[M1, M2, K_A, G, c],
            output=sp.simplify(q_total - q_sum),
            method="q(M1+M2) - q(M1) - q(M2)",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="identity_residual",
        )


def case_5_energy_coupling_interpretation(out: ScriptOutput):
    header("Case 5: Energy coupling interpretation")

    K_A, G, M, c, A_R = sp.symbols("K_A G M c A_R", positive=True, real=True)

    q_M = 4*K_A*G*M/c**2
    E_boundary = -q_M*A_R

    print("Boundary coupling:")
    print()
    print(f"q_M = {q_M}")
    print(f"E_boundary = {E_boundary}")
    print()
    print("Interpretation:")
    print("  q_M has length-like mass coupling GM/c^2 multiplied by K_A.")
    print("  The exact coefficient is fixed by Newtonian/Schwarzschild matching.")
    print("  K_A remains a reduced stiffness/normalization parameter.")
    print()

    with out.governance_assessments():
        out.line("source coupling can be normalized by weak-field matching",
                 StatusMark.PASS,
                 "q_M = 4 K_A G M/c^2 follows from Newtonian limit; K_A origin remains open")


def case_6_what_is_not_derived(out: ScriptOutput):
    header("Case 6: What remains underived")

    print("The script fixes q_M from required weak-field/exterior matching.")
    print()
    print("It does NOT derive:")
    print("  K_A from vacuum microphysics,")
    print("  why matter couples to A rather than another variable,")
    print("  why the boundary action is exactly -q A(R),")
    print("  how pressure/stress modifies q or sources kappa,")
    print("  a full covariant source action.")
    print()

    with out.governance_assessments():
        out.line("normalization is matched, not fundamental yet",
                 StatusMark.PASS,
                 "q_M matched to Newtonian limit; K_A and coupling form not derived")

    with out.unresolved_obligations():
        out.line("derive K_A from vacuum microphysics",
                 StatusMark.OBLIGATION, "origin of K_A missing")
        out.line("derive why matter couples to A via boundary action -q A(R)",
                 StatusMark.OBLIGATION, "coupling form is ansatz; covariant derivation missing")
        out.line("derive how pressure/stress modifies source coupling q or kappa",
                 StatusMark.OBLIGATION, "pressure/stress coupling channel not yet established")
        out.line("derive full covariant source action",
                 StatusMark.OBLIGATION, "reduced boundary action is non-covariant toy")


def final_interpretation():
    header("Final interpretation")

    print("The boundary charge normalization is not arbitrary once the")
    print("weak-field Newtonian limit is imposed.")
    print()
    print("Exterior flux gives:")
    print("  A = 1 - F_A/(4*pi*r)")
    print()
    print("Newtonian matching requires:")
    print("  F_A = 8*pi*G*M/c^2")
    print()
    print("The boundary relation F_A = 2*pi*q/K_A then requires:")
    print("  q_M = 4*K_A*G*M/c^2")
    print()
    print("This explains the coefficient at the reduced matching level,")
    print("but does not yet derive the coupling from deeper principles.")
    print()
    print("Possible next artifact:")
    print("  candidate_source_coupling_normalization.md")


def main():
    header("Candidate Source Coupling Normalization")

    out = ScriptOutput()

    with ProjectArchive(root=ARCHIVE_ROOT) as archive:
        ns = archive.script_namespace(SCRIPT_ID)
        ns.prepare_archive()

        case_0_boundary_relation(out)
        case_1_newtonian_matching(out, ns)
        case_2_boundary_charge_from_flux(out, ns)
        case_3_schwarzschild_radius_matching(out, ns)
        case_4_additivity(out, ns)
        case_5_energy_coupling_interpretation(out)
        case_6_what_is_not_derived(out)
        final_interpretation()

        out.print_summary()

        ns.record_obligation(ProofObligationRecord(
            obligation_id="derive_K_A_from_vacuum_microphysics",
            script_id=SCRIPT_ID,
            title="Derive K_A from vacuum microphysics",
            status=ObligationStatus.OPEN,
            description=(
                "K_A appears as the reduced stiffness/normalization parameter in the "
                "boundary action. Its value is fixed by Newtonian/Schwarzschild matching "
                "but its origin from vacuum microphysics is not derived."
            ),
        ))

        ns.record_obligation(ProofObligationRecord(
            obligation_id="derive_boundary_action_coupling_form",
            script_id=SCRIPT_ID,
            title="Derive why matter couples to A via boundary action -q A(R)",
            status=ObligationStatus.OPEN,
            description=(
                "The boundary coupling E_boundary = -q A(R) is an ansatz. A covariant "
                "derivation of the coupling form and why matter couples to A rather than "
                "another field variable has not been given."
            ),
        ))

        ns.record_obligation(ProofObligationRecord(
            obligation_id="derive_pressure_stress_q_kappa_modification",
            script_id=SCRIPT_ID,
            title="Derive how pressure/stress modifies source coupling q or sources kappa",
            status=ObligationStatus.OPEN,
            description=(
                "The current normalization uses density-only mass M. How pressure and "
                "stress modify the effective source charge q or contribute an independent "
                "kappa source has not been derived."
            ),
        ))

        ns.record_obligation(ProofObligationRecord(
            obligation_id="derive_covariant_source_action",
            script_id=SCRIPT_ID,
            title="Derive full covariant source action",
            status=ObligationStatus.OPEN,
            description=(
                "The reduced boundary action is a non-covariant toy. A full covariant "
                "source action that reduces to the boundary coupling in the static "
                "spherical case remains an open obligation."
            ),
        ))

        ns.record_claim(ClaimRecord(
            claim_id="q_M_normalization_fixed_by_newtonian_matching",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.CANDIDATE_ROUTE,
            statement=(
                "The boundary charge normalization q_M = 4 K_A G M/c^2 is fixed by "
                "the requirement that the exterior flux gives A = 1 - 2GM/(c^2 r) in "
                "the weak-field/Schwarzschild limit. This is a matching result; K_A "
                "and the coupling form are not derived from first principles."
            ),
            obligation_ids=["derive_K_A_from_vacuum_microphysics",
                            "derive_boundary_action_coupling_form"],
        ))

        ns.record_route(RouteRecord(
            route_id="newtonian_matched_boundary_charge_route",
            script_id=SCRIPT_ID,
            name="Newtonian-matched boundary charge normalization route",
            status=GovernanceStatus.CANDIDATE_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            required_obligations=["derive_K_A_from_vacuum_microphysics",
                                  "derive_boundary_action_coupling_form",
                                  "derive_covariant_source_action"],
        ))

        ns.write_run_metadata()


if __name__ == "__main__":
    main()
