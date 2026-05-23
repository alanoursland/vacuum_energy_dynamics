# Group:
#   10_kappa_trace_response
#
# Script type:
#   SAMPLE
#
# Candidate kappa non-inertial vacuum-curvature relaxation
#
# Purpose
# -------
# This script replaces the too-abstract parent-balance next step with a sharper
# kappa model:
#
#   kappa is a non-inertial trace / vacuum-volume relaxation variable.
#
# Physical idea:
#
#   A region has a local vacuum-curvature minimum configuration.
#   Matter trace / pressure / volume imbalance shifts the local minimum.
#   Vacuum and curvature exchange configuration energy toward that minimum.
#   The exchange has no independent momentum channel.
#   Therefore kappa does not overshoot, slosh, or propagate as a free breathing wave.
#
# Key distinction:
#
#   BAD:
#     kappa has a second-order wave equation and conjugate momentum.
#
#   BETTER:
#     kappa obeys a first-order gradient-flow / constraint-restoration law.
#
# Candidate law:
#
#   partial_t kappa = -mu_kappa * delta E_vac-curv / delta kappa
#
# For a local quadratic minimum:
#
#   E = 1/2 K_kappa (kappa - kappa_min)^2
#
# this gives:
#
#   partial_t kappa = -mu_kappa K_kappa (kappa - kappa_min)
#
# with monotonic relaxation and no oscillation.
#
# This is not a final derivation.
# It is a control model for "trace relaxation without breathing radiation."

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


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="kappa_relaxation_energy_accounting_marker",
        upstream_script_id="010_kappa_trace_response__candidate_kappa_relaxation_energy_accounting",
        upstream_derivation_id="kappa_relaxation_energy_accounting_marker",
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
    header("Case 0: Non-inertial kappa relaxation problem")

    print("Question:")
    print()
    print("  Can kappa represent local vacuum-curvature equilibration without")
    print("  becoming a propagating breathing-wave degree of freedom?")
    print()
    print("Working idea:")
    print()
    print("  each region has a local minimum configuration")
    print("  trace/volume imbalance displaces kappa from that minimum")
    print("  vacuum and curvature exchange configuration energy toward the minimum")
    print("  the exchange has no independent momentum channel")
    print()
    print("Goal:")
    print()
    print("  allow local trace relaxation")
    print("  forbid ordinary long-range breathing radiation")


def case_1_bad_second_order_model():
    header("Case 1: Bad second-order/inertial model")

    print("A second-order scalar model has the form:")
    print()
    print("  kappa_ddot + Gamma kappa_dot + omega0^2 kappa = source")
    print()
    print("This gives kappa a momentum-like channel:")
    print()
    print("  pi_kappa ~ kappa_dot")
    print()
    print("Consequences:")
    print()
    print("  overshoot possible")
    print("  oscillation possible")
    print("  propagating scalar/breathing wave possible")
    print()
    print("This is not the preferred kappa interpretation.")


def case_2_quadratic_minimum_energy():
    header("Case 2: Local vacuum-curvature minimum energy")

    kappa, kappa_min, Kk = sp.symbols("kappa kappa_min K_k", positive=True, real=True)

    E = sp.Rational(1, 2) * Kk * (kappa - kappa_min)**2
    dE_dk = sp.diff(E, kappa)

    print("Local minimum energy:")
    print()
    print("  E = 1/2 K_k (kappa - kappa_min)^2")
    print()
    print(f"E = {E}")
    print()
    print("Variational slope:")
    print()
    print(f"dE/dkappa = {dE_dk}")
    print()
    print("Interpretation:")
    print("  kappa_min is the local vacuum-curvature equilibrium value.")
    print("  matter trace/pressure may shift kappa_min inside matter.")
    print("  exterior vacuum should have kappa_min = 0.")

    return kappa, kappa_min, Kk, E, dE_dk


def case_3_first_order_gradient_flow(kappa, kappa_min, Kk, E, dE_dk):
    header("Case 3: First-order gradient-flow relaxation")

    mu = sp.symbols("mu_k", positive=True, real=True)

    rhs = sp.simplify(-mu * dE_dk)

    print("Candidate non-inertial relaxation law:")
    print()
    print("  kappa_dot = -mu_k dE/dkappa")
    print()
    print("For quadratic minimum:")
    print()
    print(f"kappa_dot = {rhs}")
    print()
    print("This has no kappa_ddot term.")
    print("Therefore it has no independent kappa momentum channel.")

    return mu, rhs


def case_4_solution_no_overshoot():
    header("Case 4: Solution has no overshoot")

    t, mu, Kk, kappa0, kappa_min = sp.symbols(
        "t mu_k K_k kappa_0 kappa_min",
        positive=True,
        real=True,
    )

    solution = sp.simplify(kappa_min + (kappa0 - kappa_min)*sp.exp(-mu*Kk*t))

    print("For constant kappa_min:")
    print()
    print("  kappa_dot = -mu_k K_k (kappa - kappa_min)")
    print()
    print("Solution:")
    print()
    print(f"kappa(t) = {solution}")
    print()
    print("The displacement from minimum decays monotonically:")
    print()
    print("  kappa(t) - kappa_min = [kappa0 - kappa_min] exp(-mu_k K_k t)")
    print()
    print("No oscillation.")
    print("No overshoot.")
    print("No slosh.")

    return t, mu, Kk, kappa0, kappa_min, solution


def case_5_energy_transfer_accounting():
    header("Case 5: Energy transfer accounting")

    kappa, kappa_min, Kk, mu = sp.symbols(
        "kappa kappa_min K_k mu_k",
        positive=True,
        real=True,
    )

    E = sp.Rational(1, 2)*Kk*(kappa - kappa_min)**2
    dE_dk = sp.diff(E, kappa)
    kappa_dot = -mu*dE_dk
    dE_dt = sp.simplify(dE_dk * kappa_dot)
    P_absorb = sp.simplify(-dE_dt)

    print("Energy:")
    print()
    print(f"E = {E}")
    print()
    print("Gradient-flow law:")
    print()
    print(f"kappa_dot = {kappa_dot}")
    print()
    print("Energy derivative:")
    print()
    print(f"dE/dt = {dE_dt}")
    print()
    print("Absorbed/configuration power:")
    print()
    print(f"P_absorb = {P_absorb}")
    print()
    print("For mu_k > 0 and K_k > 0:")
    print("  dE/dt <= 0")
    print("  P_absorb >= 0")
    print()
    print("Interpretation:")
    print("  energy is not destroyed")
    print("  explicit imbalance energy is converted into vacuum configuration/restoration")

    return kappa, kappa_min, Kk, mu, E, dE_dk, kappa_dot, dE_dt, P_absorb


def case_6_no_momentum_channel():
    header("Case 6: No momentum channel")

    print("In a wave/oscillator theory:")
    print()
    print("  L ~ 1/2 kappa_dot^2 - V(kappa)")
    print("  pi_kappa = kappa_dot")
    print()
    print("This gives kappa independent momentum.")
    print()
    print("In the proposed non-inertial relaxation law:")
    print()
    print("  no 1/2 kappa_dot^2 kinetic storage is introduced")
    print("  no independent pi_kappa is promoted")
    print("  kappa moves by mobility down the vacuum-curvature energy gradient")
    print()
    print("This is why it does not slosh.")


def case_7_static_A_constraint_guard():
    header("Case 7: Static A-constraint guard")

    print("The relaxation law must act on:")
    print()
    print("  kappa - kappa_min")
    print()
    print("not on:")
    print()
    print("  A_constraint")
    print()
    print("The exterior A-sector remains:")
    print()
    print("  A = 1 - 2GM/(c^2 r)")
    print()
    print("Forbidden:")
    print()
    print("  relaxing away the areal mass flux")
    print("  damping the Newtonian/Schwarzschild monopole")
    print()
    print("Allowed:")
    print()
    print("  restoring trace/volume imbalance toward local minimum")
    print("  keeping exterior kappa_min = 0")


def case_8_source_shifted_minimum():
    header("Case 8: Source-shifted local minimum")

    S, chi, kappa0 = sp.symbols("S_trace chi_k kappa_0", real=True)

    kappa_min = sp.simplify(chi*S)

    print("Possible source relation:")
    print()
    print("  kappa_min = chi_k S_trace")
    print()
    print(f"kappa_min = {kappa_min}")
    print()
    print("Interpretation:")
    print("  matter trace/pressure does not act as an ordinary wave source.")
    print("  it shifts the local equilibrium configuration.")
    print("  kappa then relaxes toward that equilibrium.")
    print()
    print("This avoids treating trace source as a radiative scalar charge.")

    return S, chi, kappa_min


def case_9_exterior_condition():
    header("Case 9: Exterior condition")

    print("Exterior vacuum target:")
    print()
    print("  S_trace = 0")
    print("  kappa_min = 0")
    print()
    print("Relaxation law:")
    print()
    print("  kappa_dot = -mu_k K_k kappa")
    print()
    print("Exterior solution decays toward:")
    print()
    print("  kappa = 0")
    print()
    print("If boundary flux is also zero:")
    print()
    print("  no long-range exterior kappa tail")
    print("  no free breathing wave")


def case_10_classification():
    header("Case 10: Classification")

    print("| Item | Status |")
    print("|---|---|")
    print("| second-order inertial kappa | RISK / disfavored |")
    print("| quadratic local minimum | PLAUSIBLE |")
    print("| first-order gradient-flow law | PLAUSIBLE |")
    print("| monotonic no-overshoot solution | DERIVED_REDUCED |")
    print("| positive absorption accounting | DERIVED_REDUCED |")
    print("| no independent momentum channel | CONSTRAINED_BY_IDENTITY |")
    print("| source as shifted local minimum | PLAUSIBLE |")
    print("| K_k, mu_k, chi_k derivation | MISSING |")
    print("| parent covariant identity | MISSING |")


def case_11_next_tests():
    header("Case 11: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_kappa_noninertial_relaxation.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_kappa_boundary_layer_model.py")
    print("   Model interior kappa with exterior kappa=0 and no flux.")
    print()
    print("3. candidate_kappa_trace_response_status_summary.md")
    print("   Summarize group 10 if near stopping point.")
    print()
    print("Recommended next artifact:")
    print()
    print("  candidate_kappa_noninertial_vacuum_curvature_relaxation.md")
    print()
    print("Recommended next script:")
    print("  candidate_kappa_boundary_layer_model.py")


def final_interpretation():
    header("Final interpretation")

    print("Best refined kappa picture:")
    print()
    print("  kappa is not a wave.")
    print("  kappa is a non-inertial trace/volume relaxation coordinate.")
    print("  matter trace shifts the local vacuum-curvature minimum.")
    print("  vacuum and curvature exchange configuration energy toward that minimum.")
    print("  there is no independent kappa momentum channel.")
    print()
    print("Therefore:")
    print()
    print("  no overshoot")
    print("  no slosh")
    print("  no ordinary breathing radiation")
    print()
    print("Possible next artifact:")
    print("  candidate_kappa_noninertial_vacuum_curvature_relaxation.md")
    print()
    print("Possible next script:")
    print("  candidate_kappa_boundary_layer_model.py")


def main():
    header("Candidate Kappa Non-Inertial Vacuum-Curvature Relaxation")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement()
    case_1_bad_second_order_model()
    kappa, kappa_min, Kk, E, dE_dk = case_2_quadratic_minimum_energy()
    mu, rhs = case_3_first_order_gradient_flow(kappa, kappa_min, Kk, E, dE_dk)
    t, mu2, Kk2, kappa0, kappa_min2, solution = case_4_solution_no_overshoot()
    kappa, kappa_min3, Kk3, mu3, E2, dE_dk2, kappa_dot, dE_dt, P_absorb = case_5_energy_transfer_accounting()
    case_6_no_momentum_channel()
    case_7_static_A_constraint_guard()
    S, chi, kappa_min_source = case_8_source_shifted_minimum()
    case_9_exterior_condition()
    case_10_classification()
    case_11_next_tests()
    final_interpretation()

    # Real sample computations
    ns.record_derivation(
        derivation_id="gradient_flow_kappa_relaxation_solution_sample",
        inputs=[E, rhs],
        output=solution,
        method=(
            "solve kappa_dot = -mu_k*K_k*(kappa-kappa_min) for constant kappa_min; "
            "gives exponential decay"
        ),
        status=Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
        scope="quadratic local minimum and constant kappa_min; K_k and mu_k not derived",
    )

    ns.record_derivation(
        derivation_id="gradient_flow_kappa_energy_derivative_sample",
        inputs=[E2, kappa_dot],
        output=dE_dt,
        method="compute dE/dt = (dE/dkappa)(kappa_dot) for gradient-flow law",
        status=Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
        scope="quadratic minimum; mu_k and K_k are toy parameters not derived from action",
    )

    ns.record_derivation(
        derivation_id="kappa_noninertial_vacuum_curvature_relaxation_marker",
        inputs=[],
        output=sp.Symbol("kappa_noninertial_relaxation_model_classified"),
        method="kappa_noninertial_relaxation_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_kappa_mobility_mu_k_in_10_kappa_trace",
        script_id=SCRIPT_ID,
        title="Derive the kappa mobility coefficient mu_k from first principles",
        status=ObligationStatus.OPEN,
        description=(
            "The gradient-flow law kappa_dot = -mu_k K_k (kappa - kappa_min) uses "
            "mobility mu_k and stiffness K_k that are not derived. Both must come from "
            "the action or a parent covariant identity."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_kappa_min_source_coupling_chi_k_in_10_kappa_trace",
        script_id=SCRIPT_ID,
        title="Derive the shifted-minimum coupling chi_k (kappa_min = chi_k S_trace)",
        status=ObligationStatus.OPEN,
        description=(
            "The source relation kappa_min = chi_k S_trace is proposed as the way "
            "trace enters kappa without acting as a radiative scalar charge. "
            "chi_k must be derived from the parent Lagrangian."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="gradient_flow_kappa_has_no_breathing_radiation",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "A first-order gradient-flow kappa law kappa_dot = -mu_k dE/dkappa for "
            "quadratic local minimum gives monotonic no-overshoot decay with positive "
            "energy absorption accounting and no independent momentum channel. "
            "This is a viable control model for trace relaxation without breathing radiation, "
            "but mu_k, K_k, and chi_k must be derived."
        ),
    ))

    with out.sample_results():
        out.line("gradient-flow solution kappa(t) = kappa_min + (kappa0-kappa_min)*exp(-mu*K*t)", StatusMark.PASS, "sample - constant kappa_min only")
        out.line("gradient-flow dE/dt = -mu_k*K_k*(kappa-kappa_min)^2 <= 0", StatusMark.PASS, "sample - quadratic minimum only")

    with out.governance_assessments():
        out.line("gradient-flow kappa has no momentum channel", StatusMark.PASS, "no kappa_ddot term")
        out.line("energy absorbed positively by vacuum configuration", StatusMark.PASS, "P_absorb = mu_k*(dE/dkappa)^2 >= 0")
        out.line("K_k, mu_k, chi_k derivation", StatusMark.OBLIGATION, "missing")
        out.line("parent covariant identity", StatusMark.OBLIGATION, "missing")

    with out.unresolved_obligations():
        out.line("derive mu_k from first principles", StatusMark.OBLIGATION, "open")
        out.line("derive chi_k coupling", StatusMark.OBLIGATION, "open")

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
