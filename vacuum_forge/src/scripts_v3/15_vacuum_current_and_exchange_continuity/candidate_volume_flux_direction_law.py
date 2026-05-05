# Candidate volume flux direction law
#
# Purpose
# -------
# The Sigma/R split found:
#
#   Sigma_V = source / creation / destruction side
#   R_V     = relaxation / reconfiguration / return side
#
# but neither side defines the direction of J_V.
#
# A scalar source/divergence equation does not by itself determine a vector
# current. This script inventories possible flux-direction laws for J_V.
#
# It is not a derivation of J_V.

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
        "RECOVERY_TARGET": "WARN",
        "BRANCH_KILLED": "FAIL",
        "DEFER": "WARN",
        "CLOSED": "PASS",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class FluxDirectionEntry:
    name: str
    direction_law: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[FluxDirectionEntry]:
    return [
        FluxDirectionEntry(
            name="FD1: flux-direction target",
            direction_law="J_V must have a direction / transport law in addition to div J_V = Sigma_V - R_V",
            role="core missing object for defining J_V",
            allowed_if="direction follows from exchange ontology before recovery checks",
            forbidden_if="direction is chosen to cancel exterior charge or fit gamma/AB",
            status="THEOREM_TARGET",
            missing="flux direction law",
            consequence="decides whether J_V can become more than a divergence placeholder",
        ),
        FluxDirectionEntry(
            name="FD2: scalar source insufficiency",
            direction_law="Sigma_V - R_V supplies divergence strength, not vector direction",
            role="negative structural result",
            allowed_if="used as constraint on candidate laws",
            forbidden_if="scalar source is treated as current direction",
            status="REQUIRED",
            missing="not a missing law; a guardrail",
            consequence="prevents scalar source from masquerading as J_V",
        ),
        FluxDirectionEntry(
            name="FD3: zeta-gradient flux",
            direction_law="J_V^mu ~ -D_z nabla^mu zeta",
            role="minimal constitutive volume-flow candidate",
            allowed_if="grad zeta is physically meaningful, domain-limited, and non-radiative",
            forbidden_if="used where grad zeta is spacelike/null/zero or creates exterior scalar flux",
            status="RISK",
            missing="domain, sign, D_z origin, no-scalar-flux theorem",
            consequence="tempting but likely not a general u_vac-defining current",
        ),
        FluxDirectionEntry(
            name="FD4: exchange-potential flux",
            direction_law="J_V^mu ~ -D_V nabla^mu Phi_V where Phi_V is volume-exchange potential",
            role="potential-driven flux candidate",
            allowed_if="Phi_V is defined independently of recovery targets",
            forbidden_if="Phi_V is invented as a name for whatever direction is needed",
            status="CANDIDATE",
            missing="definition of Phi_V and D_V origin",
            consequence="could define direction if exchange potential becomes real",
        ),
        FluxDirectionEntry(
            name="FD5: source-gradient flux",
            direction_law="J_V^mu follows gradient of Sigma_V or source density/support profile",
            role="source-local flux candidate",
            allowed_if="gradient law is compact and boundary-neutral",
            forbidden_if="source-gradient creates exterior scalar tail or acausal repair",
            status="RISK",
            missing="support law and causality/locality rule",
            consequence="may localize redistribution but can become repair current",
        ),
        FluxDirectionEntry(
            name="FD6: relaxation-gradient flux",
            direction_law="J_V^mu follows gradient of relaxation target, e.g. nabla(zeta-zeta_min)",
            role="return-flow / restoration flux candidate",
            allowed_if="zeta_min and relaxation target are independently defined",
            forbidden_if="zeta_min chosen to cancel exterior charge",
            status="RISK",
            missing="zeta_min, target origin, boundary theorem",
            consequence="could align flux with R_V but risks coefficient/boundary patching",
        ),
        FluxDirectionEntry(
            name="FD7: causal transport current",
            direction_law="J_V obeys first-order transport with finite characteristic speed",
            role="dynamic current candidate",
            allowed_if="transport law is derived and does not become Box zeta",
            forbidden_if="creates ordinary scalar radiation or acausal repair",
            status="CANDIDATE",
            missing="transport equation, characteristic structure, source coupling",
            consequence="stronger than elliptic repair but requires new dynamics",
        ),
        FluxDirectionEntry(
            name="FD8: zero-flux local exchange",
            direction_law="J_V = 0 locally while Sigma_V and R_V balance pointwise",
            role="local exchange / no-transport branch",
            allowed_if="Sigma_V = R_V pointwise or by local constraint",
            forbidden_if="used where nonzero transport is needed for u_vac",
            status="SAFE_IF",
            missing="pointwise balance law and implication for u_vac",
            consequence="protects exterior neutrality but cannot define u_vac from J_V",
        ),
        FluxDirectionEntry(
            name="FD9: compact-support redistribution",
            direction_law="J_V nonzero only inside compact support with zero boundary flux",
            role="ordinary-sector safety branch",
            allowed_if="support and zero-flux theorem are explicit",
            forbidden_if="used as nonlocal/acausal repair current",
            status="CANDIDATE",
            missing="support law, flux direction inside support",
            consequence="can preserve exterior neutrality but still needs internal direction law",
        ),
        FluxDirectionEntry(
            name="FD10: elliptic repair current",
            direction_law="choose J_V by solving div J_V = Sigma_V - R_V with boundary conditions after the fact",
            role="dangerous mathematical completion",
            allowed_if="only as diagnostic constraint solution, not physical current",
            forbidden_if="used as transport law or ontology",
            status="RISK",
            missing="physical direction / causality",
            consequence="may be useful diagnostic but does not define real flux",
        ),
        FluxDirectionEntry(
            name="FD11: acausal repair current",
            direction_law="J_V chosen nonlocally to cancel scalar charge or enforce exterior neutrality",
            role="forbidden shortcut",
            allowed_if="never in ordinary branch",
            forbidden_if="accepted as exchange current",
            status="REJECTED",
            missing="not pursued",
            consequence="would make exchange continuity a boundary-tuning device",
        ),
        FluxDirectionEntry(
            name="FD12: boundary neutrality requirement",
            direction_law="any flux law must have zero exterior scalar charge / zero forbidden far-zone flux",
            role="ordinary-sector safety guard",
            allowed_if="boundary theorem is attached to flux law",
            forbidden_if="J_V leaks scalar flux or changes M_ext",
            status="REQUIRED",
            missing="boundary theorem for candidate flux law",
            consequence="kills flux laws that become scalar gravity",
        ),
        FluxDirectionEntry(
            name="FD13: no-overlap requirement",
            direction_law="J_V-driven zeta enters metric only through B_s, or residual trace killed/non-metric",
            role="count-once recombination guard",
            allowed_if="overlap theorem or residual-kill theorem is explicit",
            forbidden_if="flux law creates independent residual metric trace",
            status="REQUIRED",
            missing="no-overlap theorem tied to flux",
            consequence="prevents current from reintroducing zeta/kappa scalar duplicate",
        ),
        FluxDirectionEntry(
            name="FD14: timelike-domain dependency",
            direction_law="after a flux law survives, test whether J_V^2 < 0 and J_V != 0 where u_vac is used",
            role="next viability gate",
            allowed_if="tested after candidate direction exists",
            forbidden_if="normalizing J_V before domain is known",
            status="REQUIRED",
            missing="timelike/nonzero domain theorem",
            consequence="sets next script if a direction candidate survives",
        ),
        FluxDirectionEntry(
            name="FD15: recovery downstream",
            direction_law="gamma_like and AB checked only after flux, Sigma/R, and domain are defined",
            role="ordinary-regime recovery target",
            allowed_if="kept downstream",
            forbidden_if="used to choose D_z, Phi_V, support, or transport speed",
            status="RECOVERY_TARGET",
            missing="solutions after current law",
            consequence="keeps recovery from becoming construction",
        ),
        FluxDirectionEntry(
            name="FD16: recommended next move",
            direction_law="if a direction candidate survives, test timelike/nonzero domain for J_V",
            role="best next bottleneck",
            allowed_if="flux direction inventory leaves at least one candidate alive",
            forbidden_if="jumping to domain without a direction candidate",
            status="RECOMMENDED",
            missing="timelike domain test",
            consequence="next script should test whether surviving J_V candidates can define u_vac",
        ),
    ]


def print_entry(e: FluxDirectionEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Direction law: {e.direction_law}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Volume flux direction problem")

    print("Question:")
    print()
    print("  How does a scalar creation / relaxation balance become a vector current?")
    print()
    print("Goal:")
    print()
    print("  inventory possible direction laws for J_V")
    print()
    print("Discipline:")
    print()
    print("  do not treat scalar Sigma_V - R_V as a flux direction")
    print("  do not choose flux direction from recovery targets")
    print("  do not use acausal repair currents")
    print("  preserve boundary neutrality")
    print("  preserve no-overlap / residual-kill")
    print("  keep timelike-domain test downstream")

    status_line("volume flux direction problem posed", "REQUIRED")


def case_1_inventory(entries: List[FluxDirectionEntry]):
    header("Case 1: Volume flux direction inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[FluxDirectionEntry]):
    header("Case 2: Compact flux-direction ledger")

    print("| Entry | Direction law | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.direction_law.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact flux-direction ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[FluxDirectionEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Scalar Sigma_V - R_V does not determine J_V direction.")
    print("  Zeta-gradient, source-gradient, and relaxation-gradient fluxes are risky.")
    print("  Exchange-potential and causal-transport currents are candidates if their mechanisms are defined.")
    print("  Zero-flux local exchange is safe for neutrality but cannot define u_vac from J_V.")
    print("  If a current survives, the next bottleneck is timelike/nonzero domain.")

    status_line("flux-direction status count produced", "STRUCTURAL")


def case_4_direction_decision_tree():
    header("Case 4: Direction decision tree")

    print("Decision tree:")
    print()
    print("1. Zeta-gradient flux:")
    print("   tempting minimal law, but likely domain-limited and scalar-flux risky.")
    print()
    print("2. Exchange-potential flux:")
    print("   candidate only if Phi_V is independently defined.")
    print()
    print("3. Source-gradient / relaxation-gradient flux:")
    print("   may localize flow, but risks patching boundary behavior.")
    print()
    print("4. Causal transport:")
    print("   strongest physical current if derived, but introduces new dynamics.")
    print()
    print("5. Zero-flux local exchange:")
    print("   safe but cannot define u_vac by normalized J_V.")
    print()
    print("6. Acausal repair current:")
    print("   rejected.")

    status_line("flux-direction decision tree stated", "RECOMMENDED")


def case_5_good_failure():
    header("Case 5: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  no flux direction can be specified without acausal repair,")
    print("  recovery tuning, exterior scalar charge, or residual trace overlap.")
    print()
    print("Consequence:")
    print()
    print("  J_V remains a theorem target.")
    print("  Exchange continuity cannot yet define u_vac.")
    print()
    print("Bad failure:")
    print("  solve div J_V = Sigma_V - R_V after the fact and call that the current law.")

    status_line("flux-direction good failure stated", "DEFER")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("Flux-direction law fails if:")
    print()
    print("1. scalar Sigma_V - R_V is treated as vector direction")
    print("2. direction is chosen from gamma_like or AB")
    print("3. direction is chosen to cancel exterior scalar charge")
    print("4. zeta-gradient flux creates far-zone scalar flux")
    print("5. elliptic repair is promoted to physical transport")
    print("6. causal transport becomes Box zeta or scalar radiation")
    print("7. J_V creates residual metric trace outside B_s")
    print("8. boundary neutrality is absent")
    print("9. timelike/nonzero domain is skipped")

    status_line("flux-direction failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_volume_flux_direction_law.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_timelike_domain_for_volume_current.py")
    print("   Test J_V^2 < 0 and J_V != 0 for surviving current candidates.")
    print()
    print("3. candidate_exchange_continuity_early_failure_summary.py")
    print("   Use if all flux-direction routes fail or are decorative.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_timelike_domain_for_volume_current.py")
    print()
    print("Reason:")
    print("  If the flux-direction inventory leaves candidate currents alive, the next gate is whether any can define u_vac through a timelike/nonzero domain.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("The source side gives divergence, not direction.")
    print()
    print("Best current interpretation:")
    print()
    print("  J_V needs an independent flux / transport law.")
    print()
    print("If a direction candidate survives, the next missing object is:")
    print()
    print("  timelike / nonzero domain")
    print()
    print("Best next test:")
    print("  candidate_timelike_domain_for_volume_current.py")


def main():
    header("Candidate Volume Flux Direction Law")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_direction_decision_tree()
    case_5_good_failure()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
