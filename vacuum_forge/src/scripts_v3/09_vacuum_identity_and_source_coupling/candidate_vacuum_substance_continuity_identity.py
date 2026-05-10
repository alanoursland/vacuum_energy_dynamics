# Candidate vacuum-substance continuity identity
#
# Group:
#   09_vacuum_identity_and_source_coupling
#
# Script type:
#   DERIVATION
#
# Purpose
# -------
# Group 09 begins with the hardest ontology-native question:
#
#   If the vacuum is treated as a substance-like ontology, what balance law does it demand?
#
# The goal is NOT to import GR's Bianchi identity.
# The goal is to ask what the vacuum-substance picture itself requires.
#
# Candidate schematic identity:
#
#   partial_t q_v + div J_v = Sigma_exchange + Sigma_creation - Gamma_relax
#
# where:
#
#   q_v            = scalar vacuum-substance density/charge proxy
#   J_v            = vacuum flow/current proxy
#   Sigma_exchange = exchange with matter/source sector
#   Sigma_creation = genuine creation/destruction regime
#   Gamma_relax    = relaxation back toward vacuum minimum
#
# This is not yet a covariant identity.
# It is the first ontology-native continuity/balance attempt.

from pathlib import Path

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    ReasonCode,
    RecordKind,
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
        dependency_id="conservation_identity_requirements_marker",
        upstream_script_id="08_covariant_parent_structure__candidate_conservation_identity_requirements",
        upstream_derivation_id="conservation_identity_requirements_marker",
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


def case_0_problem_statement():
    header("Case 0: Vacuum-substance continuity problem")

    print("Question:")
    print()
    print("  If the vacuum is a substance-like ontology, what balance law does it demand?")
    print()
    print("Do not start from GR.")
    print("Start from vacuum bookkeeping:")
    print()
    print("  accumulation + outflow = exchange + creation - relaxation")
    print()
    print("Candidate identity:")
    print()
    print("  partial_t q_v + div J_v = Sigma_exchange + Sigma_creation - Gamma_relax")
    print()
    print("Goal:")
    print("  see whether sector source assignments begin to follow from this identity.")


def case_1_pure_conservation_identity():
    header("Case 1: Pure vacuum-substance conservation identity")

    t, x = sp.symbols("t x", real=True)
    q = sp.Function("q_v")(t, x)
    J = sp.Function("J_v")(t, x)

    continuity = sp.diff(q, t) + sp.diff(J, x)

    print("Pure conservation branch:")
    print()
    print("  partial_t q_v + div J_v = 0")
    print()
    print(f"1D expression = {continuity}")
    print()
    print("Interpretation:")
    print("  q_v is not yet mass density.")
    print("  It is a vacuum bookkeeping charge/density proxy.")
    print("  The parent theory must define what q_v physically is.")

    return continuity


def case_2_exchange_creation_relaxation():
    header("Case 2: Exchange / creation / relaxation balance")

    t, x = sp.symbols("t x", real=True)
    q = sp.Function("q_v")(t, x)
    J = sp.Function("J_v")(t, x)
    Sigma_ex = sp.Function("Sigma_exchange")(t, x)
    Sigma_cr = sp.Function("Sigma_creation")(t, x)
    Gamma_rel = sp.Function("Gamma_relax")(t, x)

    balance = sp.Eq(
        sp.diff(q, t) + sp.diff(J, x),
        Sigma_ex + Sigma_cr - Gamma_rel
    )

    print("General ontology-native balance:")
    print()
    print("  partial_t q_v + div J_v = Sigma_exchange + Sigma_creation - Gamma_relax")
    print()
    print(f"1D balance = {balance}")
    print()
    print("Interpretation:")
    print("  exchange: matter/vacuum transfer or coupling")
    print("  creation: nonconservative vacuum amount change")
    print("  relaxation: return toward vacuum minimum")

    return balance


def case_3_static_exterior_consistency():
    header("Case 3: Static exterior consistency")

    r, G, M, c = sp.symbols("r G M c", positive=True, real=True)

    A = 1 - 2*G*M/(c**2*r)
    flux_A = sp.simplify(4*sp.pi*r**2*sp.diff(A, r))
    flux_derivative = sp.simplify(sp.diff(flux_A, r))

    print("Exterior A_constraint:")
    print(f"A = {A}")
    print(f"F_A = 4*pi*r^2 A' = {flux_A}")
    print(f"dF_A/dr = {flux_derivative}")
    print()
    print("Vacuum exterior policy:")
    print("  Sigma_exchange = 0 outside matter")
    print("  Sigma_creation = 0 in ordinary exterior")
    print("  Gamma_relax = 0 for settled static constraint configuration")
    print()
    print("Then exterior flux is conserved.")

    return flux_derivative


def case_4_matter_exchange_A_source():
    header("Case 4: Matter exchange as A_constraint source")

    r, G, c = sp.symbols("r G c", positive=True, real=True)
    rho = sp.Function("rho")(r)

    source_A = 8*sp.pi*G*rho/c**2
    flux_derivative_density = sp.simplify(4*sp.pi*r**2 * source_A)

    print("Reduced A source law:")
    print()
    print("  Delta_areal A = 8*pi*G*rho/c^2")
    print()
    print("Areal flux derivative:")
    print()
    print("  dF_A/dr = 4*pi*r^2 * 8*pi*G*rho/c^2")
    print()
    print(f"dF_A/dr = {flux_derivative_density}")
    print()
    print("Ontology interpretation:")
    print("  matter density acts as an exchange term for scalar vacuum flux.")
    print()
    print("Candidate identification:")
    print("  Sigma_exchange,A ~ 8*pi*G*rho/c^2")

    return source_A, flux_derivative_density


def case_5_current_flow_Wi_source():
    header("Case 5: Vacuum current and W_i source hint")

    rho, vx, vy, vz = sp.symbols("rho v_x v_y v_z", real=True)
    j = sp.Matrix([rho*vx, rho*vy, rho*vz])

    print("Matter current proxy:")
    print(f"j_i = rho v_i = {j}")
    print()
    print("Ontology hint:")
    print("  If scalar exchange uses density rho, vector response should use")
    print("  transport/current j_i.")
    print()
    print("Candidate direction:")
    print("  W_i source should be tied to vacuum/matter current continuity,")
    print("  not assigned only by analogy to frame dragging.")
    print()
    print("But no W_i field equation is derived here.")

    return j


def case_6_relaxation_suppresses_A_rad():
    header("Case 6: Relaxation term and A_rad suppression")

    tau, Gamma, mu, a0 = sp.symbols("tau Gamma mu a0", positive=True, real=True)

    A_rad = a0 * sp.exp(-Gamma*mu**2*tau)

    print("Relaxation law for scalar radiative perturbation:")
    print()
    print("  dA_rad/dtau = -Gamma mu^2 A_rad")
    print()
    print(f"A_rad(tau) = {A_rad}")
    print()
    print("Ontology interpretation:")
    print("  scalar perturbations can relax back toward the vacuum minimum.")
    print()
    print("Important caveat:")
    print("  This must suppress A_rad without erasing A_constraint.")

    return A_rad


def case_7_creation_regime_nonconservative():
    header("Case 7: Creation regime is explicitly nonconservative")

    print("If Sigma_creation != 0, then vacuum-substance bookkeeping is not")
    print("locally conservative.")
    print()
    print("That may be allowed only in special regimes:")
    print("  cosmological creation")
    print("  strong-field vacuum restructuring")
    print("  phase/defect transitions")
    print()
    print("But ordinary exterior gravity should usually set:")
    print("  Sigma_creation = 0")
    print()
    print("Otherwise source closure becomes too flexible.")


def case_8_sector_source_classification():
    header("Case 8: Sector source classification from continuity attempt")

    print("| Sector | Source from continuity picture | Status |")
    print("|---|---|---|")
    print("| A_constraint | scalar exchange with density rho | PARTIAL |")
    print("| W_i | current/transport j_i = rho v_i | PARTIAL |")
    print("| kappa | stress/trace/volume exchange | MISSING |")
    print("| h_ij^TT | quadrupole time-varying conserved source | PARTIAL |")
    print("| A_rad | relaxation/absorption-controlled perturbation | PARTIAL |")
    print("| creation regime | explicit nonconservative source | RISK |")
    print()
    print("Interpretation:")
    print("  The continuity picture begins to constrain A and W_i source types.")
    print("  It does not yet derive kappa, tensor normalization, or closure identities.")


def case_9_failure_controls():
    header("Case 9: Failure controls")

    print("This ontology-native identity attempt fails if:")
    print()
    print("1. q_v remains undefined forever.")
    print("2. Sigma_exchange is chosen separately for every sector.")
    print("3. Sigma_creation becomes a free knob for any mismatch.")
    print("4. Gamma_relax suppresses unwanted modes but also destroys static gravity.")
    print("5. W_i current coupling is set only by GR matching.")
    print("6. No Bianchi-like closure emerges from the balance law.")


def final_interpretation():
    header("Final interpretation")

    print("The vacuum-substance ontology suggests a real balance identity:")
    print()
    print("  partial_t q_v + div J_v = Sigma_exchange + Sigma_creation - Gamma_relax")
    print()
    print("This is not yet a covariant conservation law.")
    print("But it is ontology-native and begins to constrain source assignments:")
    print()
    print("  density -> scalar exchange / A_constraint")
    print("  current -> vector response / W_i")
    print("  relaxation -> suppression of A_rad")
    print("  creation -> special nonconservative regime, not a free knob")
    print()
    print("Main missing pieces:")
    print("  define q_v")
    print("  derive coefficients")
    print("  derive kappa source")
    print("  derive tensor source from identity")
    print("  derive closure / Bianchi-like compatibility")
    print()
    print("Possible next artifact:")
    print("  candidate_vacuum_substance_continuity_identity.md")
    print()
    print("Possible next script:")
    print("  candidate_source_coupling_from_vacuum_exchange.py")


def main():
    header("Candidate Vacuum-Substance Continuity Identity")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    continuity = case_1_pure_conservation_identity()
    balance = case_2_exchange_creation_relaxation()
    flux_derivative = case_3_static_exterior_consistency()
    source_A, flux_density = case_4_matter_exchange_A_source()
    j = case_5_current_flow_Wi_source()
    A_rad = case_6_relaxation_suppresses_A_rad()
    case_7_creation_regime_nonconservative()
    case_8_sector_source_classification()
    case_9_failure_controls()
    final_interpretation()

    out = ScriptOutput()

    with out.derived_results():
        out.line(
            "pure 1D continuity expression formulated",
            StatusMark.PASS,
            "partial_t q_v + partial_x J_v = 0 written symbolically",
        )
        out.line(
            "exchange/creation/relaxation balance formulated",
            StatusMark.PASS,
            "1D balance law with Sigma_exchange + Sigma_creation - Gamma_relax",
        )
        static_ok = is_zero(flux_derivative)
        out.line(
            "static exterior flux derivative vanishes",
            StatusMark.PASS if static_ok else StatusMark.FAIL,
            "exterior A-flux satisfies div=0 (dF_A/dr=0) when matter absent",
        )
        out.line(
            "matter exchange sources A-flux",
            StatusMark.PASS,
            "Sigma_exchange,A ~ 8*pi*G*rho/c^2 from reduced flux law",
        )
        out.line(
            "current j_i = rho v_i identified as W_i source candidate",
            StatusMark.PASS,
            "ontology-native vector source hint from continuity bookkeeping",
        )
        out.line(
            "relaxation law A_rad exponential decay",
            StatusMark.PASS,
            "A_rad ~ exp(-Gamma mu^2 tau) represents vacuum absorption",
        )

    with out.governance_assessments():
        out.line(
            "kappa source derivation",
            StatusMark.DEFER,
            "kappa source from continuity not yet derived",
        )
        out.line(
            "creation regime is nonconservative special case",
            StatusMark.DEFER,
            "Sigma_creation must not be used as free knob",
        )
        out.line(
            "W_i coefficient matching forbidden",
            StatusMark.DEFER,
            "coefficient must not be set by GR analogy at this stage",
        )

    with out.unresolved_obligations():
        out.line(
            "derive q_v physical definition",
            StatusMark.OBLIGATION,
            "open proof obligation recorded",
        )
        out.line(
            "derive vector coefficient alpha_W / K_c",
            StatusMark.OBLIGATION,
            "open proof obligation recorded",
        )
        out.line(
            "derive kappa source from continuity/trace exchange",
            StatusMark.OBLIGATION,
            "open proof obligation recorded",
        )
        out.line(
            "derive vector source identity",
            StatusMark.OBLIGATION,
            "open proof obligation recorded",
        )

    out.print()

    with archive.open() as ns2:
        # Contentful derivation: the 1D continuity expression is computed from SymPy
        t, x = sp.symbols("t x", real=True)
        q = sp.Function("q_v")(t, x)
        J = sp.Function("J_v")(t, x)
        continuity_expr = sp.diff(q, t) + sp.diff(J, x)

        ns2.record_derivation(
            derivation_id="vacuum_substance_1d_continuity_expression",
            inputs=[q, J],
            output=continuity_expr,
            method="symbolic differentiation partial_t q_v + partial_x J_v",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="continuity_expression",
        )

        # Contentful derivation: static exterior flux derivative vanishes
        r, G, M, c = sp.symbols("r G M c", positive=True, real=True)
        A = 1 - 2*G*M/(c**2*r)
        flux_A = sp.simplify(4*sp.pi*r**2*sp.diff(A, r))
        flux_deriv = sp.simplify(sp.diff(flux_A, r))

        ns2.record_derivation(
            derivation_id="static_exterior_A_flux_divergence_free",
            inputs=[A],
            output=flux_deriv,
            method="d/dr(4*pi*r^2 * dA/dr) for Schwarzschild A",
            status=Status.DERIVED,
            record_kind=RecordKind.DERIVATION,
            result_type="identity_residual",
        )

        # Proof obligation: q_v definition
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_q_v_physical_definition",
            script_id=SCRIPT_ID,
            title="Derive q_v physical definition",
            status=ObligationStatus.OPEN,
            description=(
                "Define q_v as a concrete physical quantity within the vacuum-substance "
                "ontology. The balance law partial_t q_v + div J_v = ... is ill-defined "
                "until q_v has a physical interpretation."
            ),
        ))

        # Proof obligation: vector coefficient
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_vector_coefficient_alpha_W_K_c",
            script_id=SCRIPT_ID,
            title="Derive vector coefficient alpha_W / K_c",
            status=ObligationStatus.OPEN,
            description=(
                "The W_i source equation Delta W_i ~ (alpha_W/K_c) j_i requires "
                "the ratio alpha_W/K_c to be derived from the vacuum exchange ontology, "
                "not matched to Lense-Thirring."
            ),
        ))

        # Proof obligation: kappa source
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_kappa_source_from_trace_exchange",
            script_id=SCRIPT_ID,
            title="Derive kappa source from trace/volume exchange",
            status=ObligationStatus.OPEN,
            description=(
                "The kappa sector source is MISSING from the vacuum-substance continuity "
                "picture. Whether kappa couples to pressure, stress trace, or relaxation "
                "must be derived."
            ),
        ))

        # Proof obligation: vector source identity
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_vector_source_identity",
            script_id=SCRIPT_ID,
            title="Derive vector source identity",
            status=ObligationStatus.OPEN,
            description=(
                "The identification of j_i = rho v_i as the W_i source is ontology-motivated "
                "but the full field equation and closure identity are not derived."
            ),
        ))

        # Governance claim: creation regime must not be a free knob
        ns2.record_claim(ClaimRecord(
            claim_id="creation_regime_not_free_knob",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.POLICY_RULE,
            statement=(
                "Sigma_creation must not be used as a free knob to resolve "
                "sector mismatches. Creation is a special-regime term allowed only "
                "in cosmological, strong-field, or phase-transition contexts."
            ),
            reason_code=ReasonCode.RECOVERY_SELECTED_PARAMETER,
        ))

        # Inventory marker (kept as placeholder for the balance law structure)
        ns2.record_derivation(
            derivation_id="vacuum_substance_continuity_identity_marker",
            inputs=[],
            output=sp.Symbol("vacuum_substance_continuity_identity_stated"),
            method="vacuum_substance_continuity_inventory",
            status=Status.DERIVED,
            record_kind=RecordKind.INVENTORY_MARKER,
            is_placeholder=True,
        )

        ns2.write_run_metadata()


if __name__ == "__main__":
    main()
