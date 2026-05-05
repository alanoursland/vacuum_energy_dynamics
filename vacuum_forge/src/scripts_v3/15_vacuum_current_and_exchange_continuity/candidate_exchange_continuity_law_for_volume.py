# Candidate exchange continuity law for volume
#
# Purpose
# -------
# This is the first script of:
#
#   15_vacuum_current_and_exchange_continuity
#
# Group 14 closed with J_V/u_vac as the surviving bottleneck.
#
# Locked door:
#
#   Can a real exchange continuity law define J_V?
#
# Strongest possible structure:
#
#   nabla_mu J_V^mu = Sigma_V - R_V
#
# This script inventories what an exchange continuity law would need in order
# to define J_V without decoration, circularity, scalar charge, or recovery tuning.
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
class ExchangeContinuityEntry:
    name: str
    law: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[ExchangeContinuityEntry]:
    return [
        ExchangeContinuityEntry(
            name="EC1: exchange continuity theorem target",
            law="nabla_mu J_V^mu = Sigma_V - R_V",
            role="core candidate law for defining vacuum-volume current",
            allowed_if="J_V, Sigma_V, and R_V are independently meaningful",
            forbidden_if="continuity law is written with unnamed terms",
            status="THEOREM_TARGET",
            missing="J_V flux law, Sigma_V, R_V, boundary conditions",
            consequence="decides whether u_vac can become a real ontology object",
        ),
        ExchangeContinuityEntry(
            name="EC2: J_V as flux, not density-times-clock",
            law="J_V^mu must define u_vac, not depend on u_vac",
            role="prevents circular frame definition",
            allowed_if="J_V has transport/flux direction before u_vac normalization",
            forbidden_if="J_V^mu = n_V u_vac^mu is used to define u_vac",
            status="REQUIRED",
            missing="non-circular flux direction",
            consequence="without flux direction, no vacuum clock",
        ),
        ExchangeContinuityEntry(
            name="EC3: Sigma_V source term",
            law="Sigma_V may include source-driven volume creation, e.g. chi rho a^mu nabla_mu A",
            role="creation/destruction source candidate",
            allowed_if="frame/projection and chi-origin are defined independently",
            forbidden_if="Sigma_V is tuned to recover gamma_like or AB",
            status="CANDIDATE",
            missing="complete Sigma_V law",
            consequence="source term remains theorem target until frame and chi are fixed",
        ),
        ExchangeContinuityEntry(
            name="EC4: R_V relaxation/exchange term",
            law="R_V represents relaxation/reconfiguration of vacuum volume",
            role="sink/rebalancing term in volume continuity",
            allowed_if="R_V follows from vacuum exchange ontology, not damping patch",
            forbidden_if="R_V is inserted to kill unwanted scalar charge by hand",
            status="CANDIDATE",
            missing="R_V operator and frame/sign convention",
            consequence="could distinguish creation from relaxation, but risks patching",
        ),
        ExchangeContinuityEntry(
            name="EC5: flux direction law",
            law="J_V direction must follow from gradient, transport, or exchange structure",
            role="turns scalar source into vector current",
            allowed_if="direction is specified before recovery checks",
            forbidden_if="direction is chosen after desired exterior behavior is known",
            status="REQUIRED",
            missing="transport / constitutive law",
            consequence="scalar Sigma_V alone cannot define J_V",
        ),
        ExchangeContinuityEntry(
            name="EC6: timelike/nonzero domain",
            law="J_V^2 < 0 and J_V != 0 where u_vac = J_V / sqrt(-J_V^2) is used",
            role="mathematical viability condition",
            allowed_if="domain is proved or explicitly restricted",
            forbidden_if="normalization used where J_V is null/spacelike/zero",
            status="REQUIRED",
            missing="domain theorem",
            consequence="defines where vacuum clock exists",
        ),
        ExchangeContinuityEntry(
            name="EC7: static-source neutrality",
            law="static equilibrium sources have zero or boundary-neutral independent J_V/zeta charge",
            role="ordinary-sector safety",
            allowed_if="continuity law gives no exterior scalar volume charge for static mass",
            forbidden_if="static sources create scalar gravity",
            status="REQUIRED",
            missing="static neutrality proof",
            consequence="kills continuity laws that produce ordinary scalar charge",
        ),
        ExchangeContinuityEntry(
            name="EC8: boundary/no-overlap",
            law="J_V-driven zeta is boundary-neutral and enters metric only through B_s, or residual killed",
            role="protects exterior neutrality and count-once recombination",
            allowed_if="boundary and residual-kill/no-overlap theorems are attached",
            forbidden_if="J_V creates independent residual metric trace",
            status="REQUIRED",
            missing="boundary/no-overlap theorem",
            consequence="continuity law fails if accounting fails",
        ),
        ExchangeContinuityEntry(
            name="EC9: sign/orientation",
            law="orientation of J_V and signs of Sigma_V/R_V define creation versus destruction",
            role="resolves physical interpretation",
            allowed_if="orientation follows from exchange ontology",
            forbidden_if="sign chosen from gamma_like or AB",
            status="UNRESOLVED",
            missing="orientation convention",
            consequence="needed before simulations or recovery claims",
        ),
        ExchangeContinuityEntry(
            name="EC10: decorative continuity rejection",
            law="nabla_mu J_V^mu = Sigma_V - R_V with unnamed J_V/Sigma_V/R_V",
            role="rejected shortcut",
            allowed_if="never as derivation",
            forbidden_if="used to promote u_vac",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents Group 15 from becoming another painted tunnel",
        ),
        ExchangeContinuityEntry(
            name="EC11: recovery checks downstream",
            law="after J_V/Sigma_V/R_V are fixed, test gamma_like and AB",
            role="ordinary-regime recovery target",
            allowed_if="checked after exchange continuity is defined",
            forbidden_if="used to choose continuity terms",
            status="RECOVERY_TARGET",
            missing="solutions after exchange law",
            consequence="keeps recovery from becoming construction",
        ),
        ExchangeContinuityEntry(
            name="EC12: recommended next move",
            law="split Sigma_V and R_V definitions before claiming exchange continuity",
            role="best current next bottleneck",
            allowed_if="J_V remains a theorem target until both sides are specified",
            forbidden_if="declaring continuity law complete now",
            status="RECOMMENDED",
            missing="Sigma_V/R_V branch inventory",
            consequence="next script should inventory Sigma_V and R_V roles in the continuity law",
        ),
    ]


def print_entry(e: ExchangeContinuityEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Law: {e.law}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: Exchange continuity law problem")

    print("Question:")
    print()
    print("  Can a real exchange continuity law define J_V?")
    print()
    print("Goal:")
    print()
    print("  open Group 15 by testing the strongest surviving structure from Group 14")
    print()
    print("Discipline:")
    print()
    print("  do not declare J_V without flux direction")
    print("  do not define J_V circularly from u_vac")
    print("  do not name Sigma_V/R_V without operators")
    print("  preserve static-source neutrality")
    print("  preserve boundary neutrality and no-overlap")
    print("  keep gamma/AB recovery downstream")

    status_line("exchange continuity law problem posed", "REQUIRED")


def case_1_inventory(entries: List[ExchangeContinuityEntry]):
    header("Case 1: Exchange continuity inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[ExchangeContinuityEntry]):
    header("Case 2: Compact exchange-continuity ledger")

    print("| Entry | Law | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.law.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact exchange-continuity ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[ExchangeContinuityEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Exchange continuity is the right next locked door, but not yet a law.")
    print("  J_V needs a flux direction, not only a divergence equation.")
    print("  Sigma_V and R_V must be defined separately.")
    print("  Static neutrality, boundary neutrality, and no-overlap remain mandatory.")

    status_line("exchange-continuity status count produced", "STRUCTURAL")


def case_4_minimal_law_requirements():
    header("Case 4: Minimal law requirements")

    print("A real exchange continuity law must provide:")
    print()
    print("1. J_V flux direction / transport law")
    print("2. Sigma_V source creation law")
    print("3. R_V relaxation / exchange law")
    print("4. timelike/nonzero domain for J_V")
    print("5. static-source neutrality")
    print("6. boundary neutrality")
    print("7. no-overlap / residual-kill theorem")
    print("8. sign/orientation convention")
    print("9. recovery checks downstream")
    print()
    print("Missing these turns continuity into decoration.")

    status_line("minimal exchange-continuity requirements stated", "REQUIRED")


def case_5_good_failure():
    header("Case 5: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  exchange continuity cannot be defined without unnamed Sigma_V/R_V or arbitrary flux direction.")
    print()
    print("Consequence:")
    print()
    print("  J_V/u_vac remains a theorem target.")
    print("  Return to postulate-level derivation of vacuum exchange rather than writing field equations.")
    print()
    print("Bad failure:")
    print("  write nabla_mu J_V^mu = Sigma_V - R_V and pretend the current has been defined.")

    status_line("exchange-continuity good failure stated", "DEFER")


def case_6_failure_controls():
    header("Case 6: Failure controls")

    print("Exchange continuity law fails if:")
    print()
    print("1. J_V has no flux direction")
    print("2. J_V is defined as n_V u_vac before u_vac exists")
    print("3. Sigma_V is unnamed or recovery-tuned")
    print("4. R_V is unnamed or used as scalar-charge patch")
    print("5. static sources create exterior volume charge")
    print("6. J_V creates residual metric trace outside B_s")
    print("7. sign/orientation is chosen from gamma/AB")
    print("8. continuity is used as decorative conservation language")

    status_line("exchange-continuity failure controls stated", "RISK")


def case_7_next_tests():
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_exchange_continuity_law_for_volume.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_sigma_R_split_for_volume_exchange.py")
    print("   Split Sigma_V and R_V roles before defining J_V.")
    print()
    print("3. candidate_volume_flux_direction_law.py")
    print("   Test what determines J_V direction.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_sigma_R_split_for_volume_exchange.py")
    print()
    print("Reason:")
    print("  The continuity equation cannot define J_V until the source and relaxation/exchange terms are split and named.")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("Group 15 begins with the right locked door:")
    print()
    print("  nabla_mu J_V^mu = Sigma_V - R_V")
    print()
    print("But the law is not real until Sigma_V, R_V, and J_V flux direction are defined.")
    print()
    print("Best next test:")
    print("  candidate_sigma_R_split_for_volume_exchange.py")


def main():
    header("Candidate Exchange Continuity Law For Volume")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_minimal_law_requirements()
    case_5_good_failure()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
