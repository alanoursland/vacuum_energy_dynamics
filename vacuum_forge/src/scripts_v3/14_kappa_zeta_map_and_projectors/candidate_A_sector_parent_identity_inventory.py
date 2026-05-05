# Candidate A-sector parent identity inventory
#
# Purpose
# -------
# The A_spatial recovery audit found:
#
#   A_spatial is currently a recovery theorem target,
#   not a derived metric component.
#
# Best surviving branch:
#
#   derive A and A_spatial together from a parent scalar/spatial identity.
#
# Rejected:
#
#   copying GR spatial metric,
#   imposing B=1/A,
#   tuning gamma=1,
#   using kappa_areal as physical scalar.
#
# This script inventories what kind of parent identity could derive A and
# A_spatial together without GR smuggling.
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
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class ParentIdentityEntry:
    name: str
    identity_class: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def build_entries() -> List[ParentIdentityEntry]:
    return [
        ParentIdentityEntry(
            name="PI1: action/stiffness identity",
            identity_class="A and A_spatial arise from one variational stiffness/action principle",
            role="candidate mechanism for deriving lapse and spatial scalar response together",
            allowed_if="action terms are specified and coefficients are not tuned by hand",
            forbidden_if="action is chosen only to reproduce GR metric coefficients",
            status="CANDIDATE",
            missing="actual action/stiffness functional",
            consequence="could derive gamma=1-like recovery without coefficient repair",
        ),
        ParentIdentityEntry(
            name="PI2: constraint propagation identity",
            identity_class="scalar constraint for A forces compatible spatial response through propagation/closure",
            role="candidate parent closure mechanism",
            allowed_if="constraint propagation yields A_spatial and preserves source conservation",
            forbidden_if="A_spatial is appended after solving A",
            status="CANDIDATE",
            missing="constraint propagation equation and closure condition",
            consequence="would keep A-sector local but requires non-decorative closure",
        ),
        ParentIdentityEntry(
            name="PI3: conservation / Bianchi-like identity",
            identity_class="Div E_parent = B_closed[T] + B_relax",
            role="broad parent identity connecting sector equations and source balance",
            allowed_if="E_parent and balance terms are defined",
            forbidden_if="called Bianchi-like without defining conserved current/operator",
            status="CANDIDATE",
            missing="E_parent, B_closed, B_relax, conserved current",
            consequence="could derive A/A_spatial relation plus trace/residual routing",
        ),
        ParentIdentityEntry(
            name="PI4: vacuum-volume exchange identity",
            identity_class="A_spatial follows from volume/curvature exchange with zeta",
            role="possible ontology-native route to spatial scalar response",
            allowed_if="zeta becomes non-overlapping A_spatial companion or residual by identity",
            forbidden_if="zeta patches A_spatial while also remaining independent residual",
            status="RISK",
            missing="zeta-A_spatial identity and no-overlap proof",
            consequence="may force zeta to be A_spatial bookkeeping or kill independent residual trace",
        ),
        ParentIdentityEntry(
            name="PI5: projector recombination identity",
            identity_class="P_recombination derives Trace_A_mass + Trace_residual_neutral with zero overlap",
            role="count-once identity for scalar spatial trace",
            allowed_if="projection formula is explicit and residual neutrality is preserved",
            forbidden_if="recombination is bookkeeping renamed as derivation",
            status="THEOREM_TARGET",
            missing="explicit P_recombination and overlap operator",
            consequence="would decide what remains for zeta/kappa after A_spatial",
        ),
        ParentIdentityEntry(
            name="PI6: exterior recovery identity",
            identity_class="identity is inferred from Schwarzschild-like exterior recovery",
            role="recovery constraint, not derivation",
            allowed_if="used only to test candidates",
            forbidden_if="exterior matching alone is used to define local field equations",
            status="RECOVERY_TARGET",
            missing="interior/local parent derivation",
            consequence="keeps AB/gamma targets as tests, not construction rules",
        ),
        ParentIdentityEntry(
            name="PI7: pure boundary matching identity",
            identity_class="A_spatial determined by matching interior to exterior boundary conditions",
            role="possible constraint on solutions but not full field equation",
            allowed_if="used as interface condition only",
            forbidden_if="boundary matching substitutes for local equation",
            status="SAFE_IF",
            missing="local interior equation and interface law",
            consequence="cannot by itself derive A_spatial throughout the domain",
        ),
        ParentIdentityEntry(
            name="PI8: GR-rewrite identity",
            identity_class="rewrite Einstein equations / Schwarzschild metric with new variable names",
            role="none",
            allowed_if="never as derivation in current branch",
            forbidden_if="used as parent identity",
            status="REJECTED",
            missing="not pursued",
            consequence="would end field-equation search by smuggling GR",
        ),
        ParentIdentityEntry(
            name="PI9: B=1/A identity",
            identity_class="AB=1 or B=1/A imposed as parent identity",
            role="shortcut to exterior recovery",
            allowed_if="used only as exterior diagnostic after derivation",
            forbidden_if="used as parent identity or interior law",
            status="REJECTED",
            missing="parent exterior recovery theorem",
            consequence="AB=1 remains recovery check, not identity",
        ),
        ParentIdentityEntry(
            name="PI10: coefficient-fit identity",
            identity_class="choose stiffness/coefficient ratios to recover gamma=1",
            role="repair knob",
            allowed_if="coefficients follow from action/identity",
            forbidden_if="chosen by observational fit inside parent identity",
            status="REJECTED",
            missing="coefficient principle",
            consequence="prevents gamma=1 tuning from masquerading as derivation",
        ),
        ParentIdentityEntry(
            name="PI11: A-only local scalar constraint",
            identity_class="A equation alone derives lapse response but not spatial companion",
            role="strong reduced branch but insufficient parent identity",
            allowed_if="kept as A-sector success and theorem target for companion",
            forbidden_if="claimed to derive A_spatial without additional identity",
            status="CONSTRAINED",
            missing="spatial companion identity",
            consequence="if no companion identity exists, A-sector-local branch is insufficient",
        ),
        ParentIdentityEntry(
            name="PI12: recommended next search",
            identity_class="inventory narrows to action/stiffness, constraint-propagation, conservation/Bianchi-like, or volume-exchange identities",
            role="working search set",
            allowed_if="each candidate must derive A/A_spatial and preserve no-overlap trace theorem",
            forbidden_if="identity only renames missing equation",
            status="RECOMMENDED",
            missing="specific candidate parent identity",
            consequence="next work should test surviving identity classes rather than add new projectors",
        ),
    ]


def print_entry(e: ParentIdentityEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Identity class: {e.identity_class}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    status_line(e.name, e.status)
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement():
    header("Case 0: A-sector parent identity inventory problem")

    print("Question:")
    print()
    print("  What kind of parent identity could derive A and A_spatial together without GR smuggling?")
    print()
    print("Goal:")
    print()
    print("  inventory identity classes and their consequences")
    print("  without renaming the missing field equations")
    print()
    print("Discipline:")
    print()
    print("  do not rewrite Einstein equations with new labels")
    print("  do not impose B=1/A")
    print("  do not tune gamma=1")
    print("  do not use exterior matching alone as local equation")
    print("  do not call bookkeeping a parent identity")
    print("  preserve count-once trace theorem")

    status_line("A-sector parent identity problem posed", "REQUIRED")


def case_1_inventory(entries: List[ParentIdentityEntry]):
    header("Case 1: Parent identity class inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[ParentIdentityEntry]):
    header("Case 2: Compact parent-identity ledger")

    print("| Entry | Identity class | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.identity_class.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    status_line("compact parent-identity ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[ParentIdentityEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  A pure A-only scalar constraint is not enough unless a companion identity is found.")
    print("  Surviving identity classes are action/stiffness, constraint propagation, conservation/Bianchi-like, volume-exchange, and recombination identity.")
    print("  GR rewrite, B=1/A identity, and coefficient-fit identity are rejected.")
    print("  The next step should test one surviving identity class concretely.")

    status_line("parent-identity status count produced", "STRUCTURAL")


def case_4_legitimate_identity_test():
    header("Case 4: Legitimate parent identity test")

    print("A proposed parent identity is useful only if it rules in or rules out future field-equation classes.")
    print()
    print("Useful identity statement:")
    print()
    print("  This identity derives A and A_spatial together,")
    print("  preserves Trace_A_mass + Trace_residual_neutral with no overlap,")
    print("  and does not import B=1/A or gamma=1 by hand.")
    print()
    print("Unhelpful identity statement:")
    print()
    print("  There exists a parent identity that does the needed thing.")
    print()
    print("Rule:")
    print()
    print("  An identity must carry a mechanism, a closure condition, or a no-go consequence.")

    status_line("legitimate identity test stated", "REQUIRED")


def case_5_count_once_theorem_target():
    header("Case 5: Count-once trace theorem target")

    print("Any viable parent identity must derive or resolve:")
    print()
    print("  Trace[g_ij scalar] = Trace_A_mass + Trace_residual_neutral")
    print()
    print("with:")
    print()
    print("  overlap = 0")
    print()
    print("Allowed resolutions:")
    print()
    print("1. derive both terms and their orthogonality")
    print("2. derive Trace_residual_neutral = 0")
    print("3. make zeta/kappa diagnostic/non-metric after A_spatial")
    print()
    print("Forbidden:")
    print()
    print("  overlapping A_spatial and zeta/kappa trace")

    status_line("count-once theorem target preserved", "THEOREM_TARGET")


def case_6_revisit_triggers():
    header("Case 6: Revisit triggers")

    print("Revisit provisional conventions if:")
    print()
    print("1. zeta primary")
    print("   Revisit if parent identity makes zeta the A_spatial companion.")
    print()
    print("2. kappa residual unresolved")
    print("   Revisit if parent identity leaves no residual trace.")
    print()
    print("3. K_lock diagnostic only")
    print("   Revisit only if parent identity derives a locking term.")
    print()
    print("4. A_spatial recovery theorem target")
    print("   Revisit if parent identity derives it or kills independent A_spatial.")

    status_line("revisit triggers stated", "STRUCTURAL")


def case_7_failure_controls():
    header("Case 7: Failure controls")

    print("Parent identity inventory fails if:")
    print()
    print("1. Einstein equations are rewritten with new labels")
    print("2. B=1/A is called a parent identity")
    print("3. Schwarzschild form is used as variational target")
    print("4. gamma=1 is tuned by coefficient choice")
    print("5. zeta/kappa residual is hidden inside A_spatial without no-overlap proof")
    print("6. conservation identity is declared without conserved current")
    print("7. gauge condition is called a parent identity")
    print("8. exterior matching alone determines local field equations")
    print("9. vacuum minimization uses tunable weights as black box")
    print("10. epsilon_vac_config or Sigma_creation patches ordinary recovery")

    status_line("parent-identity failure controls stated", "RISK")


def case_8_next_tests():
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_A_sector_parent_identity_inventory.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_parent_constraint_propagation_identity.py")
    print("   Test whether a scalar constraint can force its spatial companion.")
    print()
    print("3. candidate_parent_action_stiffness_identity.py")
    print("   Test whether an action/stiffness principle can derive A and A_spatial together.")
    print()
    print("4. candidate_kappa_diagnostic_or_residual_after_A_spatial.py")
    print("   If A_spatial consumes trace, decide kappa/zeta residual status.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_parent_constraint_propagation_identity.py")
    print()
    print("Reason:")
    print("  The closest surviving route from the existing A-sector success is constraint propagation: can the A constraint force a compatible spatial companion without GR import?")

    status_line("next test selected", "STRUCTURAL")


def final_interpretation():
    header("Final interpretation")

    print("The A-sector parent identity search has narrowed:")
    print()
    print("Rejected:")
    print("  GR rewrite")
    print("  B=1/A identity")
    print("  gamma=1 coefficient fit")
    print()
    print("Surviving identity classes:")
    print("  action/stiffness")
    print("  constraint propagation")
    print("  conservation/Bianchi-like")
    print("  volume-exchange")
    print("  recombination/no-overlap identity")
    print()
    print("Best next test:")
    print("  candidate_parent_constraint_propagation_identity.py")
    print()
    print("Reason:")
    print("  It is the nearest possible bridge from the existing A-sector constraint to A_spatial.")


def main():
    header("Candidate A-Sector Parent Identity Inventory")
    case_0_problem_statement()
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_legitimate_identity_test()
    case_5_count_once_theorem_target()
    case_6_revisit_triggers()
    case_7_failure_controls()
    case_8_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
