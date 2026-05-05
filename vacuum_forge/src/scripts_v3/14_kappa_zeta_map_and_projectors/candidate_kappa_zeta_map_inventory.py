# Candidate kappa-zeta map inventory
#
# Purpose
# -------
# Group 14 begins here.
#
# Group 13 ended with:
#
#   zeta = ln sqrt(gamma)
#
# as the leading vacuum-spacetime volume configuration variable.
#
# It also kept:
#
#   epsilon_vac_config =
#       1/2 K_zeta (zeta-zeta_min)^2
#       + 1/2 L_zeta |grad zeta|^2
#
# separate from:
#
#   e_kappa = 1/2 K_kappa (kappa-kappa_min)^2
#
# to avoid double-counting until the kappa-zeta map is derived.
#
# The next question is:
#
#   What exactly is kappa relative to zeta?
#
# This script inventories possible kappa-zeta relations and classifies
# which are safe, risky, or rejected.
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
        "SAFE_IF": "WARN",
        "CANDIDATE": "WARN",
        "STRUCTURAL": "WARN",
        "CONSTRAINED": "WARN",
        "RECOMMENDED": "PASS",
        "REQUIRED": "WARN",
        "MISSING": "FAIL",
        "UNRESOLVED": "FAIL",
        "RISK": "WARN",
        "FORBIDDEN": "PASS",
        "REJECTED": "WARN",
        "DANGER": "FAIL",
        "THEOREM_TARGET": "WARN",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class MapCandidate:
    name: str
    map_form: str
    kappa_role: str
    zeta_role: str
    energy_accounting: str
    exterior_neutrality: str
    double_counting_risk: str
    scalar_radiation_risk: str
    status: str
    missing: str
    next_test: str


def build_candidates() -> List[MapCandidate]:
    return [
        MapCandidate(
            name="M1: direct equality",
            map_form="kappa = zeta - zeta_min",
            kappa_role="raw local volume deviation from equilibrium",
            zeta_role="primary volume-form configuration variable",
            energy_accounting="e_kappa and epsilon_vac_config likely collapse unless one is removed",
            exterior_neutrality="safe only if zeta_ext=0 and zeta_min_ext=0",
            double_counting_risk="high: e_kappa may duplicate K_zeta volume displacement",
            scalar_radiation_risk="low only if zeta remains non-radiative/constraint-like",
            status="RISK",
            missing="whether kappa is redundant and which energy survives",
            next_test="candidate_kappa_as_zeta_mismatch.py",
        ),
        MapCandidate(
            name="M2: projected zeta mismatch",
            map_form="kappa = P_trace(zeta - zeta_min)",
            kappa_role="projected trace/volume mismatch",
            zeta_role="geometric volume-form configuration",
            energy_accounting="e_kappa may remain separate if projection defines a relaxation residual",
            exterior_neutrality="promising if P_trace removes exterior monopole / enforces compensation",
            double_counting_risk="moderate: depends on whether projection is diagnostic or energetic",
            scalar_radiation_risk="low if P_trace is constraint/projector, not wave operator",
            status="CANDIDATE",
            missing="definition of P_trace and whether it includes boundary compensation",
            next_test="candidate_kappa_as_projected_zeta_mismatch.py",
        ),
        MapCandidate(
            name="M3: relaxed projected mismatch",
            map_form="kappa = P_relax P_trace(zeta - zeta_min)",
            kappa_role="first-order relaxation variable tracking projected volume residual",
            zeta_role="configuration field whose residual relaxes through kappa",
            energy_accounting="e_kappa is residual energy; epsilon_vac_config is zeta configuration energy",
            exterior_neutrality="promising if P_relax/P_boundary enforce zero exterior charge",
            double_counting_risk="moderate but controllable if residual and configuration are separated",
            scalar_radiation_risk="low if relaxation remains first-order",
            status="CANDIDATE",
            missing="P_relax, P_trace, and P_boundary definitions",
            next_test="candidate_kappa_as_projected_zeta_mismatch.py",
        ),
        MapCandidate(
            name="M4: independent kappa relaxation variable",
            map_form="kappa independent; coupled to zeta only through Gamma_relax",
            kappa_role="separate first-order non-inertial relaxation coordinate",
            zeta_role="vacuum-spacetime volume configuration energy coordinate",
            energy_accounting="e_kappa outside epsilon_vac_config; exchange de_kappa + d epsilon = 0",
            exterior_neutrality="must separately impose kappa_ext=0 and zeta_ext=0",
            double_counting_risk="moderate: independence may become two scalar responses",
            scalar_radiation_risk="moderate unless first-order/no-wave rule is enforced",
            status="SAFE_IF",
            missing="coupling law tying kappa to zeta without extra degree of freedom",
            next_test="candidate_kappa_independent_relaxation_variable.py",
        ),
        MapCandidate(
            name="M5: areal-gauge diagnostic only",
            map_form="kappa = 1/2 ln(A B)",
            kappa_role="reduced spherical diagnostic of mismatch between A and B",
            zeta_role="separate physical volume-form candidate",
            energy_accounting="no independent e_kappa unless physical kappa is separately defined",
            exterior_neutrality="safe in Schwarzschild exterior because AB=1 -> kappa=0",
            double_counting_risk="low if diagnostic is not counted as physical energy",
            scalar_radiation_risk="low if diagnostic is not promoted to wave field",
            status="SAFE_IF",
            missing="whether there is a covariant physical kappa beyond diagnostic",
            next_test="candidate_areal_kappa_diagnostic_vs_physical_variable.py",
        ),
        MapCandidate(
            name="M6: boundary/interface mismatch only",
            map_form="kappa = P_boundary(zeta - zeta_min)",
            kappa_role="interface matching variable that smooths interior/exterior volume transition",
            zeta_role="interior volume-form configuration variable",
            energy_accounting="e_kappa may be boundary/interface energy only",
            exterior_neutrality="promising if support is compact and boundary flux vanishes",
            double_counting_risk="low to moderate if boundary energy is not also volume energy",
            scalar_radiation_risk="low if boundary mode has no propagation",
            status="CANDIDATE",
            missing="interface law and boundary mass preservation theorem",
            next_test="candidate_boundary_projector_for_volume_neutrality.py",
        ),
        MapCandidate(
            name="M7: auxiliary Lagrange multiplier",
            map_form="kappa enforces C[zeta,T]=0 as a multiplier/constraint variable",
            kappa_role="constraint enforcer, not physical scalar energy",
            zeta_role="physical volume configuration variable",
            energy_accounting="no e_kappa as physical energy unless multiplier dynamics are derived",
            exterior_neutrality="safe if constraint enforces Q_volume=0 and exterior fixed point",
            double_counting_risk="low if kappa has no separate energy",
            scalar_radiation_risk="low if kappa has no kinetic/wave term",
            status="CANDIDATE",
            missing="constraint C and whether prior e_kappa language must be retired",
            next_test="candidate_trace_projector_definition.py",
        ),
        MapCandidate(
            name="M8: penalty locking energy",
            map_form="1/2 K_lock (kappa - (zeta-zeta_min))^2 counted as physical energy",
            kappa_role="independent scalar coordinate locked to zeta by finite stiffness",
            zeta_role="volume-form coordinate",
            energy_accounting="adds third energy unless e_kappa/epsilon are revised",
            exterior_neutrality="risky unless both fields have zero exterior charge",
            double_counting_risk="high: K_lock plus e_kappa plus epsilon may overcount",
            scalar_radiation_risk="moderate/high if finite stiffness creates oscillatory mode",
            status="REJECTED",
            missing="would require derived degree-of-freedom count and action",
            next_test="not recommended",
        ),
        MapCandidate(
            name="M9: raw trace source kappa",
            map_form="Delta kappa = alpha T or alpha p",
            kappa_role="ordinary scalar sourced by trace/pressure",
            zeta_role="not essential",
            energy_accounting="independent scalar energy likely required",
            exterior_neutrality="fails generically for positive pressure: exterior charge likely nonzero",
            double_counting_risk="high: trace source may duplicate A-sector mass/stress response",
            scalar_radiation_risk="high if promoted dynamically",
            status="REJECTED",
            missing="not pursued in ordinary sector",
            next_test="not recommended",
        ),
        MapCandidate(
            name="M10: scalar wave kappa or zeta",
            map_form="Box kappa = alpha S or Box zeta = alpha S",
            kappa_role="ordinary scalar radiative field",
            zeta_role="ordinary scalar radiative field",
            energy_accounting="requires scalar wave energy and far-zone flux",
            exterior_neutrality="fails unless source forbidden",
            double_counting_risk="high",
            scalar_radiation_risk="fatal: creates breathing/scalar radiation channel",
            status="FORBIDDEN",
            missing="not pursued",
            next_test="not recommended",
        ),
        MapCandidate(
            name="M11: recombination-only kappa",
            map_form="kappa appears only inside spatial metric recombination, not as separate source variable",
            kappa_role="bookkeeping component of g_ij trace assembly",
            zeta_role="underlying volume-form variable",
            energy_accounting="e_kappa may be removed or reinterpreted after recombination",
            exterior_neutrality="safe if recombination forces kappa_ext=0",
            double_counting_risk="low if A/zeta/kappa are assembled once",
            scalar_radiation_risk="low if no evolution equation is attached",
            status="STRUCTURAL",
            missing="P_recombination and relation to AB=e^(2kappa)",
            next_test="candidate_recombination_projector_for_trace_volume.py",
        ),
        MapCandidate(
            name="M12: hybrid provisional convention",
            map_form="zeta primary; kappa separate first-order residual; K_lock diagnostic only",
            kappa_role="temporary residual/relaxation coordinate pending map derivation",
            zeta_role="primary geometric volume configuration",
            energy_accounting="epsilon_zeta and e_kappa counted separately; no K_lock energy",
            exterior_neutrality="requires both zeta and kappa neutrality conditions",
            double_counting_risk="controlled by explicitly not counting K_lock",
            scalar_radiation_risk="controlled by first-order kappa and no Box zeta/kappa",
            status="RECOMMENDED",
            missing="actual kappa-zeta map and projectors",
            next_test="candidate_kappa_as_projected_zeta_mismatch.py",
        ),
    ]


def print_candidate(c: MapCandidate) -> None:
    print()
    print("-" * 120)
    print(c.name)
    print("-" * 120)
    print(f"Map form: {c.map_form}")
    print(f"Kappa role: {c.kappa_role}")
    print(f"Zeta role: {c.zeta_role}")
    print(f"Energy accounting: {c.energy_accounting}")
    print(f"Exterior neutrality: {c.exterior_neutrality}")
    print(f"Double-counting risk: {c.double_counting_risk}")
    print(f"Scalar-radiation risk: {c.scalar_radiation_risk}")
    status_line(c.name, c.status)
    print(f"Missing: {c.missing}")
    print(f"Next test: {c.next_test}")


def case_0_problem_statement():
    header("Case 0: Kappa-zeta map inventory problem")

    print("Question:")
    print()
    print("  What exactly is kappa relative to zeta = ln sqrt(gamma)?")
    print()
    print("Goal:")
    print()
    print("  inventory possible kappa-zeta relations and classify safe/risky/rejected maps")
    print()
    print("Discipline:")
    print()
    print("  do not let kappa and zeta become two scalar gravities")
    print("  do not count e_kappa and epsilon_vac_config over the same mismatch twice")
    print("  do not count K_lock as physical energy unless derived")
    print("  do not allow exterior kappa/zeta scalar charge")
    print("  do not allow Box kappa or Box zeta")
    print("  do not duplicate A-sector mass")

    status_line("kappa-zeta inventory problem posed", "REQUIRED")


def case_1_inventory(entries: List[MapCandidate]):
    header("Case 1: Kappa-zeta map candidate inventory")
    for entry in entries:
        print_candidate(entry)


def case_2_compact_table(entries: List[MapCandidate]):
    header("Case 2: Compact kappa-zeta map ledger")

    print("| Map | Form | Status | Double-counting risk | Next test |")
    print("|---|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.map_form.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.double_counting_risk.replace("|", "/")
            + " | "
            + e.next_test.replace("|", "/")
            + " |"
        )

    status_line("compact kappa-zeta ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[MapCandidate]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Several safe-if/candidate interpretations survive.")
    print("  Raw trace scalar and wave interpretations are rejected.")
    print("  The recommended provisional convention remains hybrid:")
    print("    zeta primary, kappa separate first-order residual, K_lock diagnostic only.")
    print("  The strongest next test is projected zeta mismatch.")

    status_line("kappa-zeta status count produced", "STRUCTURAL")


def case_4_survivor_shortlist():
    header("Case 4: Survivor shortlist")

    print("Surviving interpretations:")
    print()
    print("1. kappa = P_trace(zeta-zeta_min)")
    print("   Projected volume mismatch.")
    print()
    print("2. kappa = P_relax P_trace(zeta-zeta_min)")
    print("   Relaxed projected mismatch.")
    print()
    print("3. kappa independent but first-order, coupled through Gamma_relax.")
    print("   Safe only if it does not become a second scalar charge.")
    print()
    print("4. kappa = 1/2 ln(AB) as areal-gauge diagnostic only.")
    print("   Safe if not promoted to independent scalar energy.")
    print()
    print("5. kappa as boundary/interface mismatch.")
    print("   Safe if exterior flux and charge vanish.")
    print()
    print("6. kappa as auxiliary constraint variable.")
    print("   Safe if no independent kinetic or energy term is attached.")

    status_line("survivor shortlist stated", "CANDIDATE")


def case_5_rejections():
    header("Case 5: Rejected or forbidden maps")

    print("Rejected or forbidden:")
    print()
    print("1. raw trace/pressure sourced Poisson kappa")
    print("   risk: exterior scalar charge and scalar double-counting")
    print()
    print("2. Box kappa")
    print("   risk: scalar breathing radiation")
    print()
    print("3. Box zeta")
    print("   risk: scalar volume radiation")
    print()
    print("4. finite K_lock energy counted before derivation")
    print("   risk: double-counting and extra scalar mode")
    print()
    print("5. kappa and zeta as independent exterior scalar charges")
    print("   risk: second scalar gravity")

    status_line("rejected kappa-zeta maps stated", "REJECTED")


def case_6_recommended_convention():
    header("Case 6: Recommended provisional convention")

    print("Recommended for now:")
    print()
    print("  zeta is the primary volume-form configuration variable:")
    print("    zeta = ln sqrt(gamma)")
    print()
    print("  epsilon_vac_config is zeta-volume energy:")
    print("    epsilon = 1/2 K_zeta (zeta-zeta_min)^2 + 1/2 L_zeta |grad zeta|^2")
    print()
    print("  kappa is a separate first-order residual/relaxation coordinate:")
    print("    e_kappa = 1/2 K_kappa (kappa-kappa_min)^2")
    print()
    print("  K_lock is diagnostic only:")
    print("    kappa ~ zeta-zeta_min")
    print()
    print("  do not count K_lock as energy yet.")
    print()
    print("Next preferred map to test:")
    print("  kappa = P_trace(zeta-zeta_min)")

    status_line("recommended provisional convention stated", "RECOMMENDED")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_kappa_zeta_map_inventory.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_kappa_as_projected_zeta_mismatch.py")
    print("   Test kappa = P_trace(zeta-zeta_min).")
    print()
    print("3. candidate_kappa_as_zeta_mismatch.py")
    print("   Test direct equality kappa = zeta-zeta_min.")
    print()
    print("4. candidate_areal_kappa_diagnostic_vs_physical_variable.py")
    print("   Separate areal diagnostic from physical kappa.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_kappa_as_projected_zeta_mismatch.py")
    print()
    print("Reason:")
    print("  Projection is the best current chance to relate kappa to zeta while preserving exterior neutrality and avoiding double-counting.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("The inventory says:")
    print()
    print("  Direct equality kappa = zeta-zeta_min is clean but risky.")
    print("  Raw trace-sourced or wave kappa/zeta is rejected.")
    print("  The safest provisional convention remains:")
    print("    zeta primary; kappa separate first-order residual; K_lock diagnostic only.")
    print()
    print("Best next target:")
    print("  kappa = P_trace(zeta-zeta_min)")
    print()
    print("Possible next artifact:")
    print("  candidate_kappa_zeta_map_inventory.md")
    print()
    print("Possible next script:")
    print("  candidate_kappa_as_projected_zeta_mismatch.py")


def main():
    header("Candidate Kappa-Zeta Map Inventory")
    case_0_problem_statement()
    entries = build_candidates()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_survivor_shortlist()
    case_5_rejections()
    case_6_recommended_convention()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
