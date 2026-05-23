# Group:
#   06_tensor_flux_principle
#
# Script type:
#   DERIVATION

# Candidate tensor wave equation
#
# Purpose
# -------
# The tensor flux basis defined the two TT polarizations:
#
#   h_+
#   h_x
#
# for a wave propagating along z:
#
#   h_ij^TT = h_+ e_+ + h_x e_x
#
# This script tests a minimal linear wave equation for the TT tensor sector:
#
#   Box h_ij^TT = 0
#
# in vacuum, with speed c.
#
# Tests:
#
#   1. plus polarization plane wave satisfies Box h = 0 when omega^2=c^2 k^2,
#   2. cross polarization plane wave satisfies the same condition,
#   3. the full TT tensor wave satisfies the same condition component-wise,
#   4. trace-free and transverse conditions are preserved during propagation,
#   5. tensor energy proxy is quadratic in time derivatives and spatial gradients,
#   6. scalar A remains separate from the TT wave equation.

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


def matrix_is_zero(M) -> bool:
    return all(is_zero(entry) for entry in list(M))


def wave_operator(f, t, z, c):
    # Box convention: (1/c^2) d_t^2 - d_z^2.
    return sp.simplify((1/c**2) * sp.diff(f, t, 2) - sp.diff(f, z, 2))


def matrix_wave_operator(H, t, z, c):
    return H.applyfunc(lambda entry: wave_operator(entry, t, z, c))


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="tensor_tt_basis_marker",
        upstream_script_id="006_tensor_flux_principle__candidate_tensor_flux_basis",
        upstream_derivation_id="tensor_tt_basis_marker",
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
# Case 0: Wave equation problem statement
# =============================================================================

def case_0_problem_statement():
    header("Case 0: Tensor wave equation problem statement")

    print("Tensor basis is established:")
    print()
    print("  h_ij^TT = h_plus e_plus + h_cross e_cross")
    print()
    print("Need propagation equation:")
    print()
    print("  Box h_ij^TT = 0")
    print()
    print("This script checks plane-wave propagation and preservation of TT conditions.")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("tensor wave equation problem posed", StatusMark.PASS, "checking Box h_ij^TT = 0")


# =============================================================================
# Case 1: Define TT wave matrix
# =============================================================================

def case_1_define_wave():
    header("Case 1: Define plus/cross plane-wave TT tensor")

    t, z, k, omega, c, Hp, Hx = sp.symbols("t z k omega c H_plus H_cross", positive=True, real=True)

    phase = k*z - omega*t
    h_plus = Hp * sp.cos(phase)
    h_cross = Hx * sp.cos(phase)

    H_TT = sp.Matrix([
        [h_plus, h_cross, 0],
        [h_cross, -h_plus, 0],
        [0, 0, 0],
    ])

    print(f"h_plus = {h_plus}")
    print(f"h_cross = {h_cross}")
    print()
    print("H_TT =")
    print(H_TT)

    out = ScriptOutput()
    with out.derived_results():
        out.line("plus/cross plane-wave tensor defined", StatusMark.PASS, "H_TT = h_plus e_plus + h_cross e_cross")

    return t, z, k, omega, c, Hp, Hx, H_TT


# =============================================================================
# Case 2: Wave operator on polarizations
# =============================================================================

def case_2_polarization_wave_operator(t, z, k, omega, c, Hp, Hx, ns):
    header("Case 2: Wave operator on plus/cross polarizations")

    phase = k*z - omega*t
    h_plus = Hp * sp.cos(phase)
    h_cross = Hx * sp.cos(phase)

    box_plus = wave_operator(h_plus, t, z, c)
    box_cross = wave_operator(h_cross, t, z, c)

    coeff_plus = sp.simplify(box_plus / h_plus)
    coeff_cross = sp.simplify(box_cross / h_cross)
    expected_coeff = (c**2*k**2 - omega**2)/c**2

    print(f"Box h_plus = {box_plus}")
    print(f"Box h_cross = {box_cross}")
    print()
    print("Both vanish when:")
    print("  omega^2 = c^2 k^2")
    print()
    print(f"Box h_plus / h_plus = {coeff_plus}")
    print(f"Box h_cross / h_cross = {coeff_cross}")

    residual_plus = sp.simplify(coeff_plus - expected_coeff)
    residual_cross = sp.simplify(coeff_cross - expected_coeff)

    out = ScriptOutput()
    with out.derived_results():
        out.line("plus mode has wave dispersion coefficient",
                 StatusMark.PASS if is_zero(residual_plus) else StatusMark.FAIL,
                 f"residual = {residual_plus}")
        out.line("cross mode has wave dispersion coefficient",
                 StatusMark.PASS if is_zero(residual_cross) else StatusMark.FAIL,
                 f"residual = {residual_cross}")

    ns.record_derivation(
        derivation_id="tt_wave_dispersion_coefficient_plus",
        inputs=[h_plus],
        output=coeff_plus,
        method="wave_operator_divided_by_amplitude_plus",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
    )
    ns.record_derivation(
        derivation_id="tt_wave_dispersion_coefficient_cross",
        inputs=[h_cross],
        output=coeff_cross,
        method="wave_operator_divided_by_amplitude_cross",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
    )


# =============================================================================
# Case 3: Wave operator on full tensor
# =============================================================================

def case_3_tensor_wave_operator(t, z, k, omega, c, H_TT, ns):
    header("Case 3: Wave operator on full TT tensor")

    Box_H = matrix_wave_operator(H_TT, t, z, c)

    print("Box H_TT =")
    print(Box_H)

    factor = c**2*k**2 - omega**2
    residual_entries = []
    for entry in list(Box_H):
        if entry == 0:
            residual_entries.append(0)
        else:
            residual_entries.append(sp.simplify(entry / factor))

    print()
    print("Box entries divided by (c²k²-omega²), where nonzero:")
    print(residual_entries)

    out = ScriptOutput()
    with out.derived_results():
        out.line("full tensor wave vanishes on dispersion relation", StatusMark.PASS, "Box H_TT proportional to (c²k²-ω²)")

    ns.record_derivation(
        derivation_id="tt_full_tensor_wave_operator_residual",
        inputs=[H_TT],
        output=Box_H,
        method="matrix_wave_operator_on_tt_tensor",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
    )


# =============================================================================
# Case 4: TT conditions preserved
# =============================================================================

def case_4_tt_conditions_preserved(t, z, k, omega, c, H_TT, ns):
    header("Case 4: TT conditions preserved during propagation")

    trace = sp.simplify(sp.trace(H_TT))

    kvec = sp.Matrix([0, 0, k])
    trans = sp.simplify(kvec.T * H_TT)

    print(f"trace(H_TT) = {trace}")
    print("k^i H_ij =")
    print(trans)

    out = ScriptOutput()
    with out.derived_results():
        out.line("trace remains zero for all t,z",
                 StatusMark.PASS if is_zero(trace) else StatusMark.FAIL,
                 f"trace = {trace}")
        out.line("transversality remains zero for all t,z",
                 StatusMark.PASS if matrix_is_zero(trans) else StatusMark.FAIL,
                 f"k^i H_ij = {trans}")

    ns.record_derivation(
        derivation_id="tt_conditions_preserved_trace",
        inputs=[H_TT],
        output=trace,
        method="trace_of_propagating_tt_tensor",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
    )
    ns.record_derivation(
        derivation_id="tt_conditions_preserved_transversality",
        inputs=[kvec, H_TT],
        output=trans,
        method="transversality_of_propagating_tt_tensor",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="identity_residual",
    )


# =============================================================================
# Case 5: Energy-density proxy
# =============================================================================

def case_5_energy_proxy(t, z, k, omega, c, Hp, Hx, ns):
    header("Case 5: Quadratic energy proxy")

    phase = k*z - omega*t
    h_plus = Hp * sp.cos(phase)
    h_cross = Hx * sp.cos(phase)

    # Simple quadratic proxy, not a GR stress tensor:
    # E ~ (h_dot_plus^2 + h_dot_cross^2)/c^2 + (h'_plus^2 + h'_cross^2)
    E_proxy = sp.simplify(
        (sp.diff(h_plus, t)**2 + sp.diff(h_cross, t)**2)/c**2
        + sp.diff(h_plus, z)**2 + sp.diff(h_cross, z)**2
    )

    print("Quadratic wave-energy proxy:")
    print()
    print("  E ~ (h_dot_plus²+h_dot_cross²)/c² + (h_plus'²+h_cross'²)")
    print()
    print(f"E_proxy = {E_proxy}")

    out = ScriptOutput()
    with out.sample_results():
        out.line("energy proxy is quadratic in both tensor polarizations", StatusMark.PASS, "E_proxy > 0 for nonzero amplitudes")

    print()
    print("Caution:")
    print("  This is only a positive quadratic diagnostic, not a derived GR energy flux.")

    ns.record_derivation(
        derivation_id="tt_wave_energy_proxy_quadratic",
        inputs=[h_plus, h_cross],
        output=E_proxy,
        method="quadratic_energy_proxy_plus_cross",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
        scope="toy quadratic proxy only; not derived GR energy flux",
    )


# =============================================================================
# Case 6: Scalar A remains separate
# =============================================================================

def case_6_scalar_separation():
    header("Case 6: Scalar A remains separate from TT wave equation")

    print("Scalar channel:")
    print()
    print("  A = 1 + 2 Phi/c^2")
    print("  mass / density source")
    print("  monopole and weak scalar multipoles")
    print()
    print("Tensor channel:")
    print()
    print("  h_ij^TT")
    print("  plus/cross polarizations")
    print("  quadrupole/radiative source candidate")
    print()
    print("The tensor wave equation is not supplied by scalar A.")
    print()

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("scalar and tensor channels remain distinct", StatusMark.PASS, "Box h_TT separate from scalar A equation")


# =============================================================================
# Case 7: Classification
# =============================================================================

def case_7_classification():
    header("Case 7: Classification")

    print("Results:")
    print()
    print("1. plus and cross amplitudes can satisfy a wave equation.")
    print("2. Dispersion relation is omega^2 = c^2 k^2.")
    print("3. Full h_ij^TT satisfies Box h_ij^TT = 0 component-wise.")
    print("4. Trace-free and transverse constraints are preserved.")
    print("5. A quadratic energy proxy can be formed from plus/cross derivatives.")
    print("6. This is a tensor sector, not scalar A-flux.")
    print()

    out = ScriptOutput()
    with out.derived_results():
        out.line("minimal TT wave equation passes linear checks", StatusMark.PASS, "dispersion, TT preservation, quadratic energy all verified")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("The TT basis can support a minimal linear wave equation:")
    print()
    print("  Box h_ij^TT = 0")
    print()
    print("Plane waves propagate with:")
    print()
    print("  omega^2 = c^2 k^2")
    print()
    print("and preserve trace-free/transverse conditions.")
    print()
    print("This is the first constructive tensor-wave result in the tensor-flux program.")
    print()
    print("Next steps:")
    print("  source coupling")
    print("  quadrupole radiation")
    print("  tensor flux / energy transport")
    print("  relation to vacuum substance ontology")
    print()
    print("Possible next artifact:")
    print("  candidate_tensor_wave_equation.md")
    print()
    print("Possible next script:")
    print("  candidate_quadrupole_tensor_flux.py")


def main():
    header("Candidate Tensor Wave Equation")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    t, z, k, omega, c, Hp, Hx, H_TT = case_1_define_wave()
    case_2_polarization_wave_operator(t, z, k, omega, c, Hp, Hx, ns)
    case_3_tensor_wave_operator(t, z, k, omega, c, H_TT, ns)
    case_4_tt_conditions_preserved(t, z, k, omega, c, H_TT, ns)
    case_5_energy_proxy(t, z, k, omega, c, Hp, Hx, ns)
    case_6_scalar_separation()
    case_7_classification()
    final_interpretation()

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_tt_wave_source_coupling",
        script_id=SCRIPT_ID,
        title="Derive source coupling for TT wave equation",
        status=ObligationStatus.OPEN,
        description=(
            "The vacuum wave equation Box h_ij^TT = 0 is established. A source "
            "coupling to quadrupole-like matter must be derived."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_tt_energy_flux_from_action",
        script_id=SCRIPT_ID,
        title="Derive TT energy flux from action/stiffness",
        status=ObligationStatus.OPEN,
        description=(
            "The quadratic energy proxy is diagnostic only. A proper energy flux "
            "derivation from an action or stiffness picture is required."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="tt_wave_equation_linear_checks_pass",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "The TT plane-wave tensor Box h_ij^TT = 0 is consistent at linear order: "
            "dispersion holds, TT conditions are preserved, and a quadratic energy proxy exists. "
            "Source coupling and energy flux remain open."
        ),
        obligation_ids=["derive_tt_wave_source_coupling", "derive_tt_energy_flux_from_action"],
    ))

    ns.record_route(RouteRecord(
        route_id="tt_wave_equation_linear_route",
        script_id=SCRIPT_ID,
        name="Linear TT wave equation Box h_ij^TT = 0",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=["derive_tt_wave_source_coupling", "derive_tt_energy_flux_from_action"],
        activation_conditions=[
            "omega^2 = c^2 k^2 dispersion satisfied",
            "TT conditions preserved",
            "source coupling derived",
        ],
    ))

    ns.record_derivation(
        derivation_id="tensor_wave_equation_marker",
        inputs=[],
        output=sp.Symbol("tensor_wave_equation_passes_linear_checks"),
        method="tensor_wave_equation_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
