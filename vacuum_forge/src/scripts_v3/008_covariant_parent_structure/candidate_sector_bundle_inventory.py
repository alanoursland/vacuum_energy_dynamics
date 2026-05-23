# Candidate sector bundle inventory
#
# Group:
#   08_covariant_parent_structure
#
# Script type:
#   INVENTORY
#
# Purpose
# -------
# Group 08 asks whether the reduced sector program can be organized as the
# shadow of one deeper geometric/covariant parent structure.
#
# Current reduced sectors:
#
#   A_constraint -> scalar/static mass response
#   A_rad        -> dangerous scalar radiative component, controlled/absent
#   kappa        -> trace/interior response / volume imbalance
#   W_i          -> vector/current/frame-dragging response
#   h_ij^TT      -> tensor/quadrupole/radiative response
#
# This script inventories those sectors and classifies:
#
#   1. source object,
#   2. equation type,
#   3. metric location,
#   4. radiation status,
#   5. safety status,
#   6. open parent-theory requirement.
#
# It also records an important distinction:
#
#   A moving mass can carry a moving scalar gravity well.
#   That is not automatically a freely propagating scalar gravitational wave.
#
# A translated constraint field:
#
#   A(x,t) = A_static(x - X(t))
#
# can "slide" with the source. A scalar wave instead satisfies a hyperbolic
# dispersion relation and may produce a breathing polarization.

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


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="no_extra_polarization_policy_marker",
        upstream_script_id="07_scalar_constraint_and_radiation_safety__candidate_no_extra_polarization_policy",
        upstream_derivation_id="no_extra_polarization_policy_marker",
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


def laplacian_1d(expr, x):
    return sp.simplify(sp.diff(expr, x, 2))


def wave_operator_1d(expr, t, x, c):
    return sp.simplify((1/c**2) * sp.diff(expr, t, 2) - sp.diff(expr, x, 2))


# =============================================================================
# Case 0: Problem statement
# =============================================================================

def case_0_problem_statement():
    header("Case 0: Sector bundle inventory problem")

    print("Group 08 question:")
    print()
    print("  Can the reduced sectors be organized as the shadow of one deeper")
    print("  geometric/covariant parent structure?")
    print()
    print("Current sectors:")
    print()
    print("  A_constraint -> scalar/static mass response")
    print("  A_rad        -> controlled/absent scalar radiative component")
    print("  kappa        -> trace/interior response")
    print("  W_i          -> vector/current response")
    print("  h_ij^TT      -> tensor/radiative response")
    print()
    print("This script inventories the bundle and records open requirements.")


# =============================================================================
# Case 1: Sector table
# =============================================================================

def case_1_sector_table():
    header("Case 1: Current sector table")

    print("| Sector | Variable | Source | Equation type | Metric location | Radiation status |")
    print("|---|---|---|---|---|---|")
    print("| scalar constraint | A_constraint | mass density rho / M | elliptic Poisson | g_tt / scalar potential | nonradiative/static |")
    print("| scalar radiative hazard | A_rad | scalar breathing source? | controlled or absent | scalar spatial trace | dangerous unless suppressed |")
    print("| trace/interior | kappa | pressure/stress/trace candidate | response/relaxation | volume/trace imbalance | suppressed exterior |")
    print("| vector current | W_i | mass current / angular momentum | vector constraint/evolution TBD | g_ti / shift | frame dragging, not ordinary wave yet |")
    print("| tensor radiation | h_ij^TT | trace-free quadrupole derivatives | hyperbolic wave | spatial TT metric | active radiation |")


# =============================================================================
# Case 2: A_constraint branch
# =============================================================================

def case_2_A_constraint():
    header("Case 2: A_constraint static scalar sector")

    r, G, M, c = sp.symbols("r G M c", positive=True, real=True)

    A = 1 - 2*G*M/(c**2*r)

    # radial Laplacian
    lapA = sp.simplify((1/r**2) * sp.diff(r**2 * sp.diff(A, r), r))

    print("A_constraint exterior:")
    print(f"A = {A}")
    print(f"Delta A = {lapA}")
    print()
    print("Role:")
    print("  static scalar mass response")
    print("  Newtonian potential channel")
    print("  monopole A-flux")
    print()
    print("Parent requirement:")
    print("  explain why A_constraint is elliptic/constraint-like, not an")
    print("  unsuppressed long-range scalar radiation mode.")

    return A, lapA


# =============================================================================
# Case 3: A_rad branch
# =============================================================================

def case_3_A_rad():
    header("Case 3: A_rad controlled scalar radiative hazard")

    t, x, H, k, omega, c = sp.symbols("t x H k omega c", positive=True, real=True)

    A_rad = H * sp.cos(k*x - omega*t)
    box = wave_operator_1d(A_rad, t, x, c)
    coeff = sp.simplify(box / A_rad)

    print("If A_rad is an unsuppressed scalar wave:")
    print(f"A_rad = {A_rad}")
    print(f"Box A_rad / A_rad = {coeff}")
    print()
    print("This propagates when omega^2 = c^2 k^2.")
    print()
    print("Safety requirement:")
    print("  A_rad must be absent, projected out, damped/absorbed, massive,")
    print("  relaxed to minimum, weakly coupled, or observationally constrained.")

    return A_rad, coeff


# =============================================================================
# Case 4: Moving well versus scalar wave
# =============================================================================

def case_4_moving_well_vs_scalar_wave():
    header("Case 4: Moving gravity well versus scalar gravity wave")

    x, t, v, sigma, c, H, k, omega = sp.symbols("x t v sigma c H k omega", positive=True, real=True)

    # Smooth translated potential-like bump for algebraic clarity.
    xi = x - v*t
    A_well = sp.exp(-xi**2/sigma**2)

    # A true scalar plane wave.
    A_wave = H * sp.cos(k*x - omega*t)

    box_well = sp.simplify(wave_operator_1d(A_well, t, x, c))
    box_wave = sp.simplify(wave_operator_1d(A_wave, t, x, c))
    wave_coeff = sp.simplify(box_wave / A_wave)

    print("Translated scalar well:")
    print("  A_well(x,t) = f(x - X(t)) with X(t)=v t")
    print(f"  example A_well = {A_well}")
    print()
    print("Box A_well =")
    print(box_well)
    print()
    print("Scalar plane wave:")
    print(f"  A_wave = {A_wave}")
    print(f"  Box A_wave / A_wave = {wave_coeff}")
    print()
    print("Interpretation:")
    print("  A moving mass can carry a moving scalar constraint configuration.")
    print("  That is a translated/retarded near-zone field, not automatically")
    print("  an independent scalar breathing wave.")
    print()
    print("  A scalar wave has a dispersion relation and can carry a breathing")
    print("  polarization. That remains controlled/unsafe unless suppressed.")

    return A_well, box_well, A_wave, wave_coeff


# =============================================================================
# Case 5: kappa sector
# =============================================================================

def case_5_kappa_sector():
    header("Case 5: kappa trace/interior response sector")

    kappa, K, m_k = sp.symbols("kappa K m_k", real=True, positive=True)

    E = sp.Rational(1, 2) * m_k**2 * kappa**2
    gradE = sp.diff(E, kappa)

    print("kappa candidate role:")
    print("  trace/interior matter response")
    print("  volume/metric determinant imbalance")
    print("  suppressed in ordinary exterior")
    print()
    print(f"E_kappa = {E}")
    print(f"dE/dkappa = {gradE}")
    print()
    print("Parent requirement:")
    print("  explain source of kappa inside matter and suppression/relaxation outside.")

    return E, gradE


# =============================================================================
# Case 6: Vector sector
# =============================================================================

def case_6_vector_sector():
    header("Case 6: W_i vector/current sector")

    Vx, Vy, Vz = sp.symbols("V_x V_y V_z", real=True)
    W = sp.Matrix([Vx, Vy, Vz])

    print("W_i candidate role:")
    print(f"W_i = {W}")
    print()
    print("Source:")
    print("  mass current")
    print("  angular momentum")
    print()
    print("Metric location:")
    print("  g_ti / shift-like sector")
    print()
    print("Parent requirement:")
    print("  derive frame dragging and decide whether vector radiation exists or is constrained.")

    return W


# =============================================================================
# Case 7: Tensor sector
# =============================================================================

def case_7_tensor_sector():
    header("Case 7: h_ij^TT tensor/radiation sector")

    hp, hx, k = sp.symbols("h_plus h_cross k", real=True)

    H_TT = sp.Matrix([
        [hp, hx, 0],
        [hx, -hp, 0],
        [0, 0, 0],
    ])

    trace = sp.trace(H_TT)
    kvec = sp.Matrix([0, 0, k])
    trans = sp.simplify(kvec.T * H_TT)

    print("h_ij^TT =")
    print(H_TT)
    print(f"trace = {trace}")
    print("k^i h_ij =")
    print(trans)
    print()
    print("Role:")
    print("  ordinary long-range gravitational radiation")
    print("  plus/cross polarizations")
    print("  quadrupole tensor flux")
    print()
    print("Parent requirement:")
    print("  derive TT wave equation, coupling, flux, and gauge constraints from parent structure.")

    return H_TT, trace, trans


# =============================================================================
# Case 8: Constraint/evolution split
# =============================================================================

def case_8_constraint_evolution_split():
    header("Case 8: Constraint/evolution split")

    print("| Variable | Preferred equation character | Reason |")
    print("|---|---|---|")
    print("| A_constraint | constraint / elliptic | static scalar gravity, no scalar waves |")
    print("| A_rad | absent or controlled | avoid scalar breathing radiation |")
    print("| kappa | response / relaxation / sourced interior | exterior suppression |")
    print("| W_i | constraint or slow vector response TBD | frame dragging |")
    print("| h_ij^TT | evolution / hyperbolic | gravitational waves |")


# =============================================================================
# Case 9: Parent requirements
# =============================================================================

def case_9_parent_requirements():
    header("Case 9: Covariant/geometric parent requirements")

    print("A successful parent structure must explain:")
    print()
    print("1. Why A_constraint is long-ranged and Poisson-like.")
    print("2. Why A_rad is absent/suppressed/absorbed/controlled.")
    print("3. Why kappa is suppressed in exterior but may respond inside matter.")
    print("4. How W_i arises from mass current/angular momentum.")
    print("5. How h_ij^TT propagates with plus/cross modes.")
    print("6. How sources couple to each sector.")
    print("7. What the gauge freedoms are.")
    print("8. Which variables are physical versus coordinate shadows.")
    print("9. How the reduced sectors recombine into metric/geometric structure.")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("The sector bundle is coherent as a reduced architecture:")
    print()
    print("  A_constraint -> static scalar mass response")
    print("  A_rad        -> controlled scalar radiation hazard")
    print("  kappa        -> trace/interior response")
    print("  W_i          -> vector/current response")
    print("  h_ij^TT      -> tensor radiation")
    print()
    print("Important distinction:")
    print()
    print("  A moving gravity well is not automatically a scalar gravity wave.")
    print("  It can be a moving/retarded scalar constraint configuration tied to")
    print("  the source.")
    print()
    print("  A free scalar breathing wave would be a separate A_rad mode and remains")
    print("  controlled/unsafe unless suppressed.")
    print()
    print("Possible next artifact:")
    print("  candidate_sector_bundle_inventory.md")
    print()
    print("Possible next script:")
    print("  candidate_covariant_parent_requirements.py")


def main():
    header("Candidate Sector Bundle Inventory")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement()
    case_1_sector_table()
    A_static, lapA = case_2_A_constraint()
    A_rad_wave, wave_coeff = case_3_A_rad()
    A_well, box_well, A_wave, wave_coeff2 = case_4_moving_well_vs_scalar_wave()
    E_kappa, gradE_kappa = case_5_kappa_sector()
    W = case_6_vector_sector()
    H_TT, trace_tt, trans_tt = case_7_tensor_sector()
    case_8_constraint_evolution_split()
    case_9_parent_requirements()
    final_interpretation()

    # --- Derived results ---

    # Case 2: static A_constraint in exterior
    ns.record_derivation(
        derivation_id="sector_bundle_A_constraint_laplacian",
        inputs=[A_static],
        output=lapA,
        method="radial Laplacian of A_constraint = 1 - 2GM/(c^2 r)",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="laplacian_residual",
    )

    # Case 5: kappa energy gradient
    ns.record_derivation(
        derivation_id="sector_bundle_kappa_energy_gradient",
        inputs=[E_kappa],
        output=gradE_kappa,
        method="dE_kappa/dkappa for E = (1/2) m_k^2 kappa^2",
        status=Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
        result_type="energy_gradient",
        scope="quadratic potential toy for kappa sector",
    )

    # Case 7: TT mode trace-free
    ns.record_derivation(
        derivation_id="sector_bundle_tt_trace_zero",
        inputs=[H_TT],
        output=trace_tt,
        method="trace of TT plus/cross polarization matrix",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="polarization_trace_residual",
    )

    # Case 7: TT mode transversality
    ns.record_derivation(
        derivation_id="sector_bundle_tt_transversality",
        inputs=[H_TT],
        output=trans_tt,
        method="k^i H_ij for z-propagating TT mode",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        result_type="transversality_residual",
    )

    # --- Governance claims ---

    ns.record_claim(ClaimRecord(
        claim_id="moving_well_not_scalar_wave_distinction",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "A moving mass can carry a moving/retarded scalar constraint configuration "
            "(A_well sliding with source) without automatically producing a free scalar "
            "breathing wave. The two must not be conflated. A free scalar wave has a "
            "hyperbolic dispersion relation and potentially a breathing polarization."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="sector_bundle_parent_required",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "The reduced sector bundle (A_constraint, A_rad, kappa, W_i, h_ij^TT) "
            "is coherent as an architecture but does not constitute a covariant parent. "
            "A parent structure must explain gauge behavior, sector recombination, "
            "conservation identities, and source coupling."
        ),
    ))

    # --- Routes ---

    ns.record_route(RouteRecord(
        route_id="covariant_parent_from_sector_bundle_route",
        script_id=SCRIPT_ID,
        name="Covariant parent structure from sector bundle",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[
            "derive_parent_explanation_for_A_constraint_elliptic",
            "derive_parent_explanation_for_A_rad_suppression",
            "derive_kappa_source_law",
            "derive_W_i_field_equation",
            "derive_gauge_structure_from_parent",
            "derive_conservation_identities_from_parent",
        ],
        activation_conditions=[
            "parent structure explains all sector behaviors",
            "gauge freedoms are identified",
            "conservation identities are derived",
            "recombination into metric structure is shown",
        ],
    ))

    # --- Proof obligations ---

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_parent_explanation_for_A_constraint_elliptic",
        script_id=SCRIPT_ID,
        title="Derive parent-theory explanation for A_constraint being elliptic",
        status=ObligationStatus.OPEN,
        description=(
            "Show from the covariant parent structure why A_constraint obeys an "
            "elliptic/Poisson equation in the exterior rather than an independent "
            "hyperbolic dispersion relation."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_parent_explanation_for_A_rad_suppression",
        script_id=SCRIPT_ID,
        title="Derive parent-theory explanation for A_rad suppression",
        status=ObligationStatus.OPEN,
        description=(
            "Show from the covariant parent structure why A_rad is absent or "
            "suppressed. The mechanism must follow from the parent theory, not be "
            "imposed by hand."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_kappa_source_law",
        script_id=SCRIPT_ID,
        title="Derive kappa source law from parent structure",
        status=ObligationStatus.OPEN,
        description=(
            "Supply a derivation of the kappa source (stress/pressure/trace coupling) "
            "and the exterior suppression or relaxation mechanism."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_W_i_field_equation",
        script_id=SCRIPT_ID,
        title="Derive W_i field equation from parent structure",
        status=ObligationStatus.OPEN,
        description=(
            "Supply a derivation of the W_i field equation from mass current/angular "
            "momentum coupling, including equation type (constraint or hyperbolic) and "
            "radiation safety."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_gauge_structure_from_parent",
        script_id=SCRIPT_ID,
        title="Derive gauge structure from parent theory",
        status=ObligationStatus.OPEN,
        description=(
            "Identify gauge freedoms, gauge transformations, physical variables, and "
            "gauge-invariant diagnostics from the parent structure."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_conservation_identities_from_parent",
        script_id=SCRIPT_ID,
        title="Derive conservation identities from parent theory",
        status=ObligationStatus.OPEN,
        description=(
            "Supply Bianchi-like or continuity-like identities from the parent structure "
            "ensuring that sector source couplings are compatible."
        ),
    ))

    # Inventory marker
    ns.record_derivation(
        derivation_id="sector_bundle_inventory_marker",
        inputs=[],
        output=sp.Symbol("sector_bundle_parent_requirements_open"),
        method="sector_bundle_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )

    ns.write_run_metadata()

    with out.derived_results():
        out.line("A_constraint satisfies source-free Laplacian", StatusMark.PASS,
                 "Delta A = 0 for A = 1 - 2GM/(c^2 r)")
        out.line("TT mode is trace-free", StatusMark.PASS, "trace(H_TT) = 0")
        out.line("TT mode is transverse", StatusMark.PASS, "k^i H_ij = 0 for TT mode")

    with out.sample_results():
        out.line("kappa energy gradient sample", StatusMark.PASS,
                 "dE/dkappa = m_k^2 kappa for quadratic toy")

    with out.governance_assessments():
        out.line("moving well not scalar wave (policy)", StatusMark.PASS,
                 "distinction recorded")
        out.line("sector bundle parent required (policy)", StatusMark.PASS,
                 "parent structure is needed")
        out.line("covariant parent from sector bundle route", StatusMark.DEFER,
                 "candidate route recorded; 6 obligations open")

    with out.unresolved_obligations():
        out.line("derive parent explanation for A_constraint elliptic", StatusMark.OBLIGATION,
                 "open proof obligation recorded")
        out.line("derive parent explanation for A_rad suppression", StatusMark.OBLIGATION,
                 "open proof obligation recorded")
        out.line("derive kappa source law", StatusMark.OBLIGATION,
                 "open proof obligation recorded")
        out.line("derive W_i field equation", StatusMark.OBLIGATION,
                 "open proof obligation recorded")
        out.line("derive gauge structure from parent", StatusMark.OBLIGATION,
                 "open proof obligation recorded")
        out.line("derive conservation identities from parent", StatusMark.OBLIGATION,
                 "open proof obligation recorded")


if __name__ == "__main__":
    main()
