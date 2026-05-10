# Group:
#   06_tensor_flux_principle
#
# Script type:
#   DIAGNOSTIC

# Candidate quadrupole coupling normalization
#
# Purpose
# -------
# The tensor-flux principle identifies:
#
#   A-flux        -> scalar monopole channel
#   h_ij^TT      -> tensor quadrupole radiative channel
#   Q_ij^TF      -> source-side quadrupole tensor
#
# The next question is normalization:
#
#   What coefficient maps quadrupole acceleration to far-zone h_ij^TT?
#
# In GR-like weak radiation, the schematic far-zone relation is:
#
#   h_ij^TT ~ (2G/(c^4 R)) d^2 Q_ij^TT/dt^2
#
# where R is distance to observer.
#
# This script does not assume the full GR derivation. It checks:
#
#   1. dimensional consistency of a coupling C_Q ~ G/(c^4 R),
#   2. plus/cross amplitude scaling from Q_plus, Q_cross,
#   3. rotating quadrupole frequency scaling h ~ Omega^2 Q0 / R,
#   4. distinction between amplitude normalization and power normalization,
#   5. scalar monopole normalization versus tensor quadrupole normalization.

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


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="quadrupole_tensor_flux_marker",
        upstream_script_id="06_tensor_flux_principle__candidate_quadrupole_tensor_flux",
        upstream_derivation_id="quadrupole_tensor_flux_marker",
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
# Case 0: Normalization problem
# =============================================================================

def case_0_problem_statement():
    header("Case 0: Quadrupole coupling normalization problem")

    print("Tensor-flux source structure:")
    print()
    print("  Q_ij^TF -> h_ij^TT")
    print()
    print("Need amplitude normalization:")
    print()
    print("  h_ij^TT ~ C_Q * d²Q_ij^TT/dt²")
    print()
    print("GR-like weak far-zone scaling uses:")
    print()
    print("  C_Q = 2G/(c^4 R)")
    print()
    print("This script treats that as a target normalization, not a derivation.")

    out = ScriptOutput()
    with out.unresolved_obligations():
        out.line("quadrupole coupling normalization problem posed", StatusMark.OBLIGATION, "C_Q = 2G/(c^4 R) is a target, not yet derived")


# =============================================================================
# Case 1: Symbolic far-zone amplitude law
# =============================================================================

def case_1_far_zone_amplitude_law(ns):
    header("Case 1: Symbolic far-zone amplitude law")

    G, c, R = sp.symbols("G c R", positive=True, real=True)
    Qdd_plus, Qdd_cross = sp.symbols("Qdd_plus Qdd_cross", real=True)

    C_Q = 2*G/(c**4 * R)

    h_plus = sp.simplify(C_Q * Qdd_plus)
    h_cross = sp.simplify(C_Q * Qdd_cross)

    print(f"C_Q = {C_Q}")
    print(f"h_plus = {h_plus}")
    print(f"h_cross = {h_cross}")

    out = ScriptOutput()
    with out.sample_results():
        out.line("far-zone amplitude normalization stated", StatusMark.PASS, f"h ~ C_Q Qdd; C_Q = {C_Q}")

    ns.record_derivation(
        derivation_id="far_zone_amplitude_coupling_law",
        inputs=[C_Q, Qdd_plus, Qdd_cross],
        output=sp.Matrix([h_plus, h_cross]),
        method="far_zone_amplitude_GR_like_coupling",
        status=Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
        scope="GR-like target normalization; not derived from first principles",
    )

    return C_Q, h_plus, h_cross


# =============================================================================
# Case 2: Rotating quadrupole amplitude scaling
# =============================================================================

def case_2_rotating_quadrupole_scaling(ns):
    header("Case 2: Rotating quadrupole amplitude scaling")

    G, c, R, Q0, Omega, t = sp.symbols("G c R Q0 Omega t", positive=True, real=True)

    Q_plus = Q0 * sp.cos(2*Omega*t)
    Q_cross = Q0 * sp.sin(2*Omega*t)

    Qdd_plus = sp.diff(Q_plus, t, 2)
    Qdd_cross = sp.diff(Q_cross, t, 2)

    C_Q = 2*G/(c**4 * R)

    h_plus = sp.simplify(C_Q * Qdd_plus)
    h_cross = sp.simplify(C_Q * Qdd_cross)

    amp_sq = sp.simplify(h_plus**2 + h_cross**2)
    expected = 64*G**2*Omega**4*Q0**2/(R**2*c**8)
    residual = sp.simplify(amp_sq - expected)

    print(f"Q_plus = {Q_plus}")
    print(f"Q_cross = {Q_cross}")
    print()
    print(f"Qdd_plus = {Qdd_plus}")
    print(f"Qdd_cross = {Qdd_cross}")
    print()
    print(f"h_plus = {h_plus}")
    print(f"h_cross = {h_cross}")
    print()
    print(f"h_plus² + h_cross² = {amp_sq}")

    out = ScriptOutput()
    with out.sample_results():
        out.line("amplitude scales as G Omega² Q0/(c⁴ R)",
                 StatusMark.PASS if is_zero(residual) else StatusMark.FAIL,
                 f"amp_sq residual = {residual}")

    ns.record_derivation(
        derivation_id="rotating_quadrupole_amplitude_scaling",
        inputs=[Q_plus, Q_cross, C_Q],
        output=amp_sq,
        method="rotating_quadrupole_h_amplitude_squared",
        status=Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
        scope="rotating quadrupole toy model with GR-like C_Q target",
    )


# =============================================================================
# Case 3: Dimensional scaling sanity check
# =============================================================================

def case_3_dimensional_scaling():
    header("Case 3: Dimensional scaling sanity check")

    print("Dimension check:")
    print()
    print("  [G]      = L^3 / (M T^2)")
    print("  [Q]      = M L^2")
    print("  [Qdd]    = M L^2 / T^2")
    print("  [c^4 R]  = (L^4/T^4) * L = L^5/T^4")
    print()
    print("  [G Qdd/(c^4 R)]")
    print("    = [L^3/(M T^2)] [M L^2/T^2] [T^4/L^5]")
    print("    = dimensionless")
    print()

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("quadrupole amplitude coefficient is dimensionally consistent", StatusMark.PASS, "G Qdd/(c^4 R) is dimensionless")


# =============================================================================
# Case 4: Amplitude versus power normalization
# =============================================================================

def case_4_amplitude_vs_power(ns):
    header("Case 4: Amplitude versus power normalization")

    G, c, Q0, Omega = sp.symbols("G c Q0 Omega", positive=True, real=True)

    # Amplitude proxy from second derivative:
    amp_source = 16*Omega**4*Q0**2

    # Power proxy from third derivative:
    power_source = 64*Omega**6*Q0**2

    # GR-like power coefficient schematic:
    # P ~ G/(5 c^5) < Qdddot_ij Qdddot_ij >
    P_proxy = sp.simplify(G * power_source / (5*c**5))

    print(f"amplitude-source proxy Qdd² = {amp_source}")
    print(f"power-source proxy Qddd² = {power_source}")
    print(f"GR-like power proxy coefficient G/(5c^5): {P_proxy}")
    print()
    print("Interpretation:")
    print("  amplitude normalization uses G/c^4")
    print("  power normalization uses G/c^5")
    print("  they are related but not the same step")

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("amplitude and power normalizations kept distinct", StatusMark.PASS, "amplitude G/c^4; power G/c^5")

    ns.record_derivation(
        derivation_id="amplitude_vs_power_normalization_proxy",
        inputs=[Q0, Omega, G, c],
        output=sp.Matrix([sp.Integer(amp_source), P_proxy]),
        method="second_third_derivative_amplitude_power_distinction",
        status=Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
        scope="rotating quadrupole toy; coefficient targets only",
    )


# =============================================================================
# Case 5: Compare scalar and tensor normalizations
# =============================================================================

def case_5_scalar_tensor_normalization_comparison(ns):
    header("Case 5: Scalar versus tensor normalization")

    G, M, c, R, Qdd = sp.symbols("G M c R Qdd", positive=True, real=True)

    # Scalar exterior A perturbation at distance R:
    delta_A = -2*G*M/(c**2 * R)

    # Tensor far-zone strain:
    h_TT = 2*G*Qdd/(c**4 * R)

    print("Scalar monopole amplitude:")
    print(f"  delta A ~ {delta_A}")
    print()
    print("Tensor quadrupole amplitude:")
    print(f"  h_TT ~ {h_TT}")
    print()
    print("Comparison:")
    print("  scalar mass channel uses GM/(c²R)")
    print("  tensor quadrupole channel uses G Qdd/(c⁴R)")
    print()

    out = ScriptOutput()
    with out.governance_assessments():
        out.line("scalar and tensor coupling normalizations are distinct", StatusMark.PASS, "scalar G/c^2; tensor G/c^4")

    ns.record_derivation(
        derivation_id="scalar_vs_tensor_coupling_comparison",
        inputs=[delta_A, h_TT],
        output=sp.Matrix([delta_A, h_TT]),
        method="scalar_monopole_vs_tensor_quadrupole_normalization",
        status=Status.DERIVED,
        record_kind=RecordKind.DIAGNOSTIC_EXAMPLE,
    )


# =============================================================================
# Case 6: Coupling target classification
# =============================================================================

def case_6_classification():
    header("Case 6: Coupling target classification")

    print("Results:")
    print()
    print("1. A GR-like far-zone tensor amplitude has coefficient 2G/(c^4 R).")
    print("2. This coefficient is dimensionally consistent.")
    print("3. Rotating quadrupole amplitudes scale as Omega² Q0.")
    print("4. Radiated-power proxies scale as Omega^6 Q0².")
    print("5. Scalar monopole normalization GM/(c²R) is distinct from tensor")
    print("   quadrupole normalization GQdd/(c⁴R).")
    print()

    out = ScriptOutput()
    with out.unresolved_obligations():
        out.line("quadrupole coupling normalization target established", StatusMark.OBLIGATION, "C_Q = 2G/(c^4 R) is target; derivation from action remains open")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("This script establishes the target normalization for the tensor")
    print("quadrupole amplitude:")
    print()
    print("  h_ij^TT ~ (2G/(c^4 R)) Qdd_ij^TT")
    print()
    print("It does not derive the coefficient from a tensor action.")
    print("It identifies the normalization that a successful tensor-flux theory")
    print("should reproduce.")
    print()
    print("Next steps:")
    print("  derive this coefficient from tensor action/stiffness")
    print("  connect amplitude normalization to radiation energy flux")
    print("  check no unwanted scalar radiation")
    print()
    print("Possible next artifact:")
    print("  candidate_quadrupole_coupling_normalization.md")
    print()
    print("Possible next script:")
    print("  candidate_tensor_radiation_energy_flux.py")


def main():
    header("Candidate Quadrupole Coupling Normalization")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    case_1_far_zone_amplitude_law(ns)
    case_2_rotating_quadrupole_scaling(ns)
    case_3_dimensional_scaling()
    case_4_amplitude_vs_power(ns)
    case_5_scalar_tensor_normalization_comparison(ns)
    case_6_classification()
    final_interpretation()

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_tensor_coupling_from_action",
        script_id=SCRIPT_ID,
        title="Derive tensor coupling coefficient C_Q = 2G/(c^4 R) from action",
        status=ObligationStatus.OPEN,
        description=(
            "The far-zone amplitude h ~ (2G/(c^4 R)) Qdd is a GR-like target. "
            "It must be derived from a tensor stiffness/action picture, not assumed."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="quadrupole_coupling_normalization_target",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.HEURISTIC,
        statement=(
            "The GR-like far-zone normalization h ~ (2G/(c^4 R)) Qdd is dimensionally "
            "consistent and the correct recovery target. It has not been derived from the "
            "tensor-flux action. This is a heuristic target, not a derived claim."
        ),
        obligation_ids=["derive_tensor_coupling_from_action"],
    ))

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
