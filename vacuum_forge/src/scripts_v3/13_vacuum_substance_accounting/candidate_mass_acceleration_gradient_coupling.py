# Candidate mass-acceleration-gradient coupling
#
# Purpose
# -------
# The scalar conversion-not-damping audit found:
#
#   scalar/trace conversion needs a source/coupling expression.
#
# The ontology says:
#
#   vacuum is spacetime.
#   creating vacuum creates spacetime.
#   changing local spacetime creates curvature.
#
# The user's proposed coupling language:
#
#   mass accelerating across a gradient triggers vacuum creation/destruction,
#   changing the mass's kinetic energy, which is creation/reconfiguration of spacetime.
#
# This script audits possible reduced and covariant expressions for:
#
#   "mass accelerating across a gradient"
#
# without prematurely choosing one.
#
# It is not a derivation.

from dataclasses import dataclass
from typing import List


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_line(label: str, status: str, detail: str = "") -> None:
    marks = {
        "CANDIDATE": "WARN",
        "STRUCTURAL": "WARN",
        "CONSTRAINED": "WARN",
        "REQUIRED": "WARN",
        "MISSING": "FAIL",
        "UNRESOLVED": "FAIL",
        "RISK": "WARN",
        "FORBIDDEN": "PASS",
        "REJECTED": "WARN",
        "DERIVED_REDUCED": "PASS",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class CouplingCandidate:
    name: str
    expression: str
    interpretation: str
    allowed_role: str
    danger: str
    status: str
    missing: str


def build_candidates() -> List[CouplingCandidate]:
    return [
        CouplingCandidate(
            name="G1: reduced power-like coupling",
            expression="rho * v^i * partial_i A",
            interpretation="matter moving through scalar potential/gradient changes kinetic/geometric accounting",
            allowed_role="reduced diagnostic for exchange along motion",
            danger="nonzero for ordinary orbital motion may imply extra dissipation unless conservative bookkeeping",
            status="CANDIDATE",
            missing="whether this is energy exchange, constraint bookkeeping, or coordinate artifact",
        ),
        CouplingCandidate(
            name="G2: acceleration-gradient coupling",
            expression="rho * a^i * partial_i A",
            interpretation="mass acceleration across gradient triggers vacuum/spacetime reconfiguration",
            allowed_role="closer to user's phrase 'accelerating across a gradient'",
            danger="proper acceleration vanishes for geodesic free fall in GR-like motion",
            status="CANDIDATE",
            missing="definition of a^i: coordinate acceleration, proper acceleration, or relative acceleration",
        ),
        CouplingCandidate(
            name="G3: covariant force-gradient scalar",
            expression="rho * a^mu * nabla_mu A",
            interpretation="covariantized acceleration-gradient candidate",
            allowed_role="possible non-geodesic/source-internal coupling",
            danger="zero for geodesic dust if a^mu=0; may miss gravitational free-fall exchange",
            status="RISK",
            missing="whether a^mu should be proper acceleration or flow derivative relative to vacuum frame",
        ),
        CouplingCandidate(
            name="G4: stress-energy Hessian coupling",
            expression="T^munu * nabla_mu nabla_nu A",
            interpretation="stress-energy samples curvature/second gradient of scalar configuration",
            allowed_role="covariant scalar candidate tied to tidal/curvature structure",
            danger="may duplicate A-sector field equation or introduce higher-derivative source",
            status="CANDIDATE",
            missing="projection removing double-counting and boundary terms",
        ),
        CouplingCandidate(
            name="G5: divergence of stress-gradient current",
            expression="nabla_mu(T^munu * nabla_nu A)",
            interpretation="exchange as divergence of stress-energy weighted scalar-gradient current",
            allowed_role="may turn into boundary/constraint bookkeeping rather than local loss",
            danger="could be identically related to stress conservation, or become decorative",
            status="STRUCTURAL",
            missing="relation to nabla_mu T^munu=0 and parent balance",
        ),
        CouplingCandidate(
            name="G6: trace-volume coupling",
            expression="P_trace[T] -> delta zeta",
            interpretation="stress trace/volume content drives vacuum-spacetime volume configuration",
            allowed_role="most aligned with trace/TT split and zeta=ln sqrt(gamma)",
            danger="trace source may leak into exterior scalar charge if uncompensated",
            status="CANDIDATE",
            missing="P_trace definition, compensation law, relation to A-sector mass",
        ),
        CouplingCandidate(
            name="G7: kinetic-energy exchange rate",
            expression="d/dtau (1/2 rho v_phys^2) <-> d epsilon_vac_config/dtau",
            interpretation="vacuum creation/destruction changes kinetic-energy bookkeeping",
            allowed_role="ontology-level accounting candidate",
            danger="may produce extra orbital damping if not conservative/geometric",
            status="UNRESOLVED",
            missing="definition of physical velocity, frame, and conservative balance",
        ),
        CouplingCandidate(
            name="G8: geodesic identity interpretation",
            expression="u^nu nabla_nu u^mu + Gamma^mu_{alpha beta} u^alpha u^beta = 0",
            interpretation="geodesic motion and vacuum exchange are the same geometric event",
            allowed_role="top-down ontology interpretation; exchange is geometry bookkeeping",
            danger="may become only a restatement of GR geodesic motion if not tied to zeta conversion",
            status="STRUCTURAL",
            missing="explicit map from connection/volume change to Sigma_exchange",
        ),
        CouplingCandidate(
            name="G9: volume-current coupling",
            expression="nabla_mu J_v^mu = Sigma_exchange - Gamma_relax",
            interpretation="vacuum-spacetime configuration current balances exchange/conversion",
            allowed_role="parent-accounting candidate once q_v/J_v are geometric",
            danger="J_v may hide acausal repair transport",
            status="CANDIDATE",
            missing="definition of J_v and locality/constraint status",
        ),
        CouplingCandidate(
            name="G10: rejected free scalar-wave source",
            expression="Box zeta = alpha * rho or Box kappa = alpha * T",
            interpretation="ordinary sourced scalar radiation",
            allowed_role="none in ordinary gravity",
            danger="far-zone scalar radiation and binary-energy-loss failure",
            status="REJECTED",
            missing="not pursued unless observations/theory force a new controlled mode",
        ),
    ]


def print_candidate(c: CouplingCandidate) -> None:
    print()
    print("-" * 120)
    print(c.name)
    print("-" * 120)
    print(f"Expression: {c.expression}")
    print(f"Interpretation: {c.interpretation}")
    print(f"Allowed role: {c.allowed_role}")
    print(f"Danger: {c.danger}")
    status_line(c.name, c.status)
    print(f"Missing: {c.missing}")


def case_0_problem_statement():
    header("Case 0: Mass-acceleration-gradient coupling problem")

    print("Question:")
    print()
    print("  What mathematical expression corresponds to mass accelerating across a gradient?")
    print()
    print("Goal:")
    print()
    print("  inventory reduced and covariant candidate couplings without choosing too early")
    print()
    print("Discipline:")
    print()
    print("  do not create an extra dissipative binary channel")
    print("  do not duplicate A-sector mass source")
    print("  do not make Sigma_exchange a free knob")
    print("  do not replace scalar conversion with Box scalar radiation")
    print("  distinguish geodesic bookkeeping from non-geodesic force")

    status_line("mass-acceleration-gradient problem posed", "REQUIRED")


def case_1_candidate_inventory(entries: List[CouplingCandidate]):
    header("Case 1: Coupling candidate inventory")
    for entry in entries:
        print_candidate(entry)


def case_2_compact_table(entries: List[CouplingCandidate]):
    header("Case 2: Compact coupling ledger")

    print("| Candidate | Expression | Status | Danger | Missing |")
    print("|---|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.expression.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.danger.replace("|", "/")
            + " | "
            + e.missing.replace("|", "/")
            + " |"
        )

    status_line("compact coupling ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[CouplingCandidate]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Several candidate couplings exist, but none are selected.")
    print("  Proper acceleration forms may vanish for geodesic motion.")
    print("  Trace-volume coupling best matches the zeta/TT split.")
    print("  Binary-radiation safety is the next hard filter.")

    status_line("coupling status count produced", "STRUCTURAL")


def case_4_key_distinctions():
    header("Case 4: Key distinctions")

    print("Coordinate acceleration versus proper acceleration:")
    print()
    print("  coordinate acceleration can be nonzero in a gravitational field")
    print("  proper acceleration vanishes for freely falling geodesic dust")
    print()
    print("Geodesic bookkeeping versus dissipative exchange:")
    print()
    print("  if exchange is the geometry of geodesic motion, it should be conservative")
    print("  if exchange removes orbital energy, it becomes an observable radiation/dissipation channel")
    print()
    print("Trace-volume coupling versus A-sector mass:")
    print()
    print("  A carries exterior mass")
    print("  zeta/kappa carries local trace-volume configuration")
    print()
    print("Current caution:")
    print()
    print("  the coupling must not turn ordinary orbital motion into extra scalar damping.")

    status_line("key coupling distinctions stated", "CONSTRAINED")


def case_5_preferred_survivors():
    header("Case 5: Preferred survivors")

    print("Most plausible survivors for next testing:")
    print()
    print("1. P_trace[T] -> delta zeta")
    print("   Reason: matches trace/TT geometric split.")
    print()
    print("2. nabla_mu(T^munu nabla_nu A)")
    print("   Reason: may express exchange as divergence/boundary bookkeeping.")
    print()
    print("3. T^munu nabla_mu nabla_nu A")
    print("   Reason: covariant scalar tied to tidal/curvature structure.")
    print()
    print("4. geodesic identity interpretation")
    print("   Reason: may avoid extra dissipation by treating exchange as geometry bookkeeping.")
    print()
    print("High-risk candidates:")
    print()
    print("  rho v dot grad A")
    print("  rho a dot grad A")
    print()
    print("Reason:")
    print("  they may be useful reduced diagnostics, but risk frame dependence or extra orbital dissipation.")

    status_line("preferred coupling survivors stated", "CANDIDATE")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("The coupling fails if:")
    print()
    print("1. It produces far-zone scalar radiation.")
    print("2. It creates extra orbital energy loss beyond TT radiation.")
    print("3. It duplicates A-sector mass source.")
    print("4. It depends on coordinate acceleration without a frame rule.")
    print("5. It vanishes for geodesic motion when the ontology needs geodesic exchange.")
    print("6. It becomes a free Sigma_exchange knob.")
    print("7. It turns zeta/kappa into exterior scalar charge.")
    print("8. It is just a decorative rewriting of GR geodesics.")

    status_line("coupling failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_mass_acceleration_gradient_coupling.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_binary_radiation_scalar_conversion_safety.py")
    print("   Check whether candidate couplings create forbidden extra radiation/dissipation.")
    print()
    print("3. candidate_boundary_volume_mode_no_exterior_charge.py")
    print("   Test local volume reconfiguration with zero exterior scalar charge.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_binary_radiation_scalar_conversion_safety.py")
    print()
    print("Reason:")
    print("  Any coupling candidate must survive the binary-radiation safety filter.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("The mass-acceleration-gradient phrase has multiple possible mathematical meanings.")
    print()
    print("Most promising directions:")
    print()
    print("  P_trace[T] -> delta zeta")
    print("  nabla_mu(T^munu nabla_nu A)")
    print("  T^munu nabla_mu nabla_nu A")
    print("  geodesic identity / geometry bookkeeping")
    print()
    print("Most dangerous directions:")
    print()
    print("  raw rho v dot grad A")
    print("  raw rho a dot grad A")
    print("  Box zeta or Box kappa")
    print()
    print("Possible next artifact:")
    print("  candidate_mass_acceleration_gradient_coupling.md")
    print()
    print("Possible next script:")
    print("  candidate_binary_radiation_scalar_conversion_safety.py")


def main():
    header("Candidate Mass Acceleration Gradient Coupling")
    case_0_problem_statement()
    entries = build_candidates()
    case_1_candidate_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_key_distinctions()
    case_5_preferred_survivors()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
