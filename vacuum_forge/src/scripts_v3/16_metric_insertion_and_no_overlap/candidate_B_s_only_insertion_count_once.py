# Candidate B_s-only insertion count-once
#
# Group:
#   16_metric_insertion_and_no_overlap
#
# Script type:
#   SIEVE
#
# Purpose
# -------
# The B_s / F_zeta insertion audit found:
#
#   gamma_ij = exp(2 zeta / 3) bar_gamma_ij
#   det(bar_gamma) = 1
#
# is a strong structural handle for zeta as spatial volume scalar.
#
# But it does not derive B_s/F_zeta insertion.
#
# The safest provisional branch remains:
#
#   J_V-driven zeta may enter ordinary metric scalar trace only through B_s,
#   with residual zeta/kappa metric trace killed or non-metric,
#   unless a real O is later derived.
#
# This script tests the count-once rule:
#
#   If zeta enters through B_s, what exactly is forbidden from entering separately?
#
# It is not a derivation of residual-kill.
# It is a count-once safety audit.

from dataclasses import dataclass
from pathlib import Path
from typing import List

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    BranchDecisionRecord,
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    ReasonCode,
    RecordKind,
    RouteRecord,
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


@dataclass
class CountOnceEntry:
    name: str
    rule: str
    role: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str
    consequence: str


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="B_s_F_zeta_insertion_law_marker",
        upstream_script_id="16_metric_insertion_and_no_overlap__candidate_B_s_F_zeta_insertion_law",
        upstream_derivation_id="B_s_F_zeta_insertion_law_marker",
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


def build_entries() -> List[CountOnceEntry]:
    return [
        CountOnceEntry(
            name="CO1: B_s-only count-once target",
            rule="Trace[g_ij^scalar] receives J_V-driven zeta only through B_s",
            role="core count-once target",
            allowed_if="residual zeta/kappa metric trace is killed or non-metric",
            forbidden_if="same zeta change appears as residual metric trace",
            status="THEOREM_TARGET",
            missing="derivation of B_s-only insertion / residual-kill",
            consequence="decides whether zeta-volume insertion can enter ordinary metric sector safely",
        ),
        CountOnceEntry(
            name="CO2: conformal-volume contribution",
            rule="gamma_ij = exp(2 zeta / 3) bar_gamma_ij supplies isotropic volume trace",
            role="structural source of possible B_s trace contribution",
            allowed_if="treated as decomposition, not full dynamics",
            forbidden_if="treated as complete field law",
            status="STRUCTURAL",
            missing="dynamical B_s/F_zeta law",
            consequence="identifies where zeta can enter once",
        ),
        CountOnceEntry(
            name="CO3: zeta residual metric killed",
            rule="zeta_residual_metric = 0 after B_s insertion",
            role="direct residual-kill rule for zeta",
            allowed_if="marked provisional unless O/parent identity derives it",
            forbidden_if="zeta_residual remains metric-active",
            status="SAFE_IF",
            missing="residual-kill theorem",
            consequence="prevents zeta from taking a second metric spoon",
        ),
        CountOnceEntry(
            name="CO4: kappa residual metric killed / diagnostic",
            rule="kappa_residual_metric = 0, or kappa remains diagnostic / non-metric / separately neutral",
            role="prevents kappa from restoring killed trace",
            allowed_if="kappa does not become independent metric trace",
            forbidden_if="kappa substitutes for killed zeta residual",
            status="REQUIRED",
            missing="kappa cleanup theorem",
            consequence="keeps areal kappa diagnostic fence intact",
        ),
        CountOnceEntry(
            name="CO5: epsilon_vac_config exclusion",
            rule="epsilon_vac_config does not source extra metric scalar trace after B_s insertion",
            role="prevents energy-accounting back door",
            allowed_if="configuration energy remains bookkeeping or recombines once",
            forbidden_if="epsilon_vac_config becomes coefficient/source reservoir",
            status="REQUIRED",
            missing="energy/accounting recombination rule",
            consequence="prevents killed residual from returning as energy source",
        ),
        CountOnceEntry(
            name="CO6: e_kappa exclusion",
            rule="e_kappa does not source extra metric scalar trace after B_s insertion",
            role="prevents kappa energy back door",
            allowed_if="e_kappa remains diagnostic/provisional bookkeeping",
            forbidden_if="e_kappa restores residual scalar trace or shifts M_ext",
            status="REQUIRED",
            missing="e_kappa status after insertion",
            consequence="blocks kappa reservoir behavior",
        ),
        CountOnceEntry(
            name="CO7: P_relax non-metric branch",
            rule="P_relax residual may survive only as first-order non-radiative non-metric relaxation",
            role="possible safe residual role",
            allowed_if="first-order, boundary-neutral, non-radiative, and not metric trace",
            forbidden_if="P_relax becomes Box zeta, Box kappa, scalar wave, or metric source",
            status="CANDIDATE",
            missing="P_relax mechanism",
            consequence="allows residual dynamics without ordinary scalar gravity",
        ),
        CountOnceEntry(
            name="CO8: non-metric bookkeeping branch",
            rule="residual zeta/kappa may remain as diagnostic/configuration bookkeeping, not direct metric trace",
            role="preserves useful variables without double-counting",
            allowed_if="bookkeeping cannot shift M_ext or create scalar exterior charge",
            forbidden_if="bookkeeping becomes hidden source term",
            status="CANDIDATE",
            missing="bookkeeping/accounting rule",
            consequence="keeps residual goblin alive but takes away metric spoon",
        ),
        CountOnceEntry(
            name="CO9: neutral residual alternative",
            rule="residual metric trace survives only if real O proves no overlap, boundary neutrality, and no mass overlap",
            role="theorem-heavy alternative to residual-kill",
            allowed_if="O is explicit and safety theorems are proved",
            forbidden_if="neutral residual is asserted to avoid residual-kill",
            status="RISK",
            missing="O operator, boundary theorem, no-mass-overlap theorem",
            consequence="keeps neutral residual branch alive only at high proof burden",
        ),
        CountOnceEntry(
            name="CO10: forbidden zeta second trace",
            rule="zeta enters B_s and also enters residual metric trace",
            role="forbidden double-counting branch",
            allowed_if="never unless real O explicitly separates neutral residual",
            forbidden_if="accepted without O",
            status="REJECTED",
            missing="not pursued",
            consequence="kills zeta-both branch",
        ),
        CountOnceEntry(
            name="CO11: forbidden kappa restoration",
            rule="kappa restores killed zeta residual trace as independent metric scalar",
            role="forbidden regression",
            allowed_if="never in ordinary branch",
            forbidden_if="accepted as recombination",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents kappa from sneaking through residual door",
        ),
        CountOnceEntry(
            name="CO12: no M_ext shift",
            rule="B_s-only insertion and killed/non-metric residual do not alter A-sector exterior mass",
            role="A-sector mass protection",
            allowed_if="volume trace recombines without changing measured mass independently",
            forbidden_if="residual/accounting shifts M_ext",
            status="REQUIRED",
            missing="mass-accounting theorem",
            consequence="protects strongest reduced A-sector result",
        ),
        CountOnceEntry(
            name="CO13: no exterior scalar charge",
            rule="killed/non-metric residual creates no exterior zeta/kappa charge or far-zone scalar flux",
            role="ordinary-sector exterior safety",
            allowed_if="residual-kill also removes exterior scalar tail",
            forbidden_if="residual bookkeeping leaks scalar charge",
            status="REQUIRED",
            missing="boundary neutrality theorem",
            consequence="prevents B_s insertion from reviving scalar gravity",
        ),
        CountOnceEntry(
            name="CO14: recovery downstream",
            rule="gamma_like and AB tested only after count-once status is fixed",
            role="anti-smuggling guard",
            allowed_if="recovery is check only",
            forbidden_if="used to choose what gets killed or counted",
            status="RECOVERY_TARGET",
            missing="solutions after count-once rule",
            consequence="prevents recovery from becoming recombination construction",
        ),
        CountOnceEntry(
            name="CO15: parent trace identity route",
            rule="parent identity derives B_s insertion and residual-kill/no-overlap together",
            role="strongest future derivation route",
            allowed_if="identity is not GR rewrite and fixes count-once before recovery",
            forbidden_if="decorative identity asserts count-once without mechanism",
            status="THEOREM_TARGET",
            missing="parent trace identity",
            consequence="future route for turning convention into theorem",
        ),
        CountOnceEntry(
            name="CO16: diagnostic overlap audit",
            rule="diagnostic projection may measure overlap but cannot define physical O",
            role="allowed diagnostic tool",
            allowed_if="kept explicitly diagnostic",
            forbidden_if="projection is promoted to ontology",
            status="SAFE_IF",
            missing="physical no-overlap mechanism",
            consequence="can help test branches without hardening scaffold",
        ),
        CountOnceEntry(
            name="CO17: count-once failure",
            rule="residual cannot be killed/non-metric and no O exists",
            role="branch failure condition",
            allowed_if="used to block metric insertion",
            forbidden_if="patched by relabeling residual variables",
            status="BRANCH_KILLED",
            missing="applies if demonstrated",
            consequence="J_V-driven zeta cannot enter ordinary metric scalar sector",
        ),
        CountOnceEntry(
            name="CO18: recommended next move",
            rule="if residual variables remain useful only non-metrically, test their allowed bookkeeping/relaxation roles",
            role="next local bottleneck",
            allowed_if="B_s-only count-once survives as provisional convention",
            forbidden_if="jumping to parent equation before residual bookkeeping is fenced",
            status="RECOMMENDED",
            missing="non-metric residual bookkeeping audit",
            consequence="next script should be candidate_residual_nonmetric_bookkeeping_rule.py",
        ),
    ]


def print_entry(e: CountOnceEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Rule: {e.rule}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    print(f"[INFO] {e.name}: {e.status}")
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: B_s-only count-once problem")

    print("Question:")
    print()
    print("  If zeta enters through B_s, what exactly is forbidden from entering separately?")
    print()
    print("Target:")
    print()
    print("  Trace[g_ij^scalar] receives J_V-driven zeta only through B_s")
    print()
    print("Current convention:")
    print()
    print("  zeta_residual_metric = 0")
    print("  kappa_residual_metric = 0 or diagnostic/non-metric/separately neutral")
    print()
    print("Goal:")
    print()
    print("  fence every possible second-spoon route")
    print()
    print("Discipline:")
    print()
    print("  do not treat residual-kill as derived")
    print("  do not let kappa restore killed trace")
    print("  do not let energy/accounting become metric source")
    print("  do not let P_relax become scalar radiation")
    print("  do not allow exterior scalar charge")
    print("  keep recovery downstream")

    with out.governance_assessments():
        out.line("B_s-only count-once problem posed", StatusMark.OBLIGATION, "required before insertion can proceed")


def case_1_inventory(entries: List[CountOnceEntry]):
    header("Case 1: B_s-only count-once inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[CountOnceEntry], out: ScriptOutput):
    header("Case 2: Compact B_s-only count-once ledger")

    print("| Entry | Rule | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.rule.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    with out.governance_assessments():
        out.line("compact count-once ledger produced", StatusMark.INFO, "inventory of second-spoon routes")


def case_3_status_counts(entries: List[CountOnceEntry], out: ScriptOutput):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  B_s-only insertion survives only with residual-kill/non-metric residual attached.")
    print("  Zeta residual metric and kappa residual metric are blocked unless O is real.")
    print("  Energy/accounting and P_relax are major second-spoon risks.")
    print("  Neutral residual remains possible but theorem-heavy.")
    print("  Next gate is non-metric residual bookkeeping: what can residual variables still do safely?")

    with out.governance_assessments():
        out.line("B_s-only count-once status count produced", StatusMark.INFO, "second-spoon routes enumerated")


def case_4_second_spoon_routes(out: ScriptOutput):
    header("Case 4: Second-spoon routes to block")

    print("Second-spoon routes:")
    print()
    print("1. zeta residual metric trace after B_s insertion")
    print("2. kappa residual metric trace after zeta residual is killed")
    print("3. epsilon_vac_config as extra metric source")
    print("4. e_kappa as extra metric source")
    print("5. P_relax as hidden scalar wave")
    print("6. non-metric bookkeeping shifting M_ext")
    print("7. exterior residual scalar charge")
    print("8. diagnostic overlap projection promoted to physical O")
    print("9. recovery check choosing what gets counted")
    print()
    print("All must be blocked unless a real O / parent identity permits a neutral residual.")

    with out.governance_assessments():
        out.line("second-spoon routes listed", StatusMark.WARN, "nine routes require blocking")


def case_4b_symbolic_count_once(ns, out: ScriptOutput):
    header("Case 4b: Symbolic count-once check")

    delta_zeta = sp.symbols("delta_zeta", real=True)
    spatial_dim = sp.Integer(3)
    fractional_entry = sp.Rational(2, spatial_dim) * delta_zeta
    scalar_trace = sp.simplify(spatial_dim * fractional_entry)

    print("For gamma_ij = exp(2 zeta / 3) bar_gamma_ij in 3 spatial dimensions:")
    print(f"  fractional scalar entry = {fractional_entry}")
    print(f"  total scalar trace contribution = {scalar_trace}")

    if scalar_trace == 2 * delta_zeta:
        with out.derived_results():
            out.line(
                "symbolic count-once scalar trace",
                StatusMark.PASS,
                f"delta gamma_ij / gamma_ij = {fractional_entry}, trace contribution = {scalar_trace}",
            )
    else:
        with out.derived_results():
            out.line("symbolic count-once scalar trace", StatusMark.FAIL, "unexpected scalar trace factor")

    ns.record_derivation(
        derivation_id="B_s_only_scalar_trace_factor",
        inputs=[delta_zeta],
        output=sp.Tuple(fractional_entry, scalar_trace),
        method="symbolic count-once trace factor",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        scope="3 spatial dimensions, det(bar_gamma)=1 convention",
    )


def case_5_decision_tree(out: ScriptOutput):
    header("Case 5: Count-once decision tree")

    print("Decision tree:")
    print()
    print("1. B_s-only insertion + residual-kill:")
    print("   safest current convention.")
    print()
    print("2. Non-metric residual bookkeeping:")
    print("   allowed if it cannot source metric trace, M_ext, or scalar exterior charge.")
    print()
    print("3. P_relax-only residual:")
    print("   possible only if first-order, non-radiative, boundary-neutral, and non-metric.")
    print()
    print("4. Neutral residual metric trace:")
    print("   possible only if O and boundary/mass safety are derived.")
    print()
    print("5. Any second metric trace without O:")
    print("   rejected or branch-killed.")
    print()
    print("6. Parent trace identity:")
    print("   future route to derive count-once, not available here.")

    with out.governance_assessments():
        out.line("count-once decision tree stated", StatusMark.INFO, "recommended next is non-metric bookkeeping audit")


def case_6_good_failure(out: ScriptOutput):
    header("Case 6: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  B_s-only insertion cannot be protected because residual zeta/kappa")
    print("  keeps reappearing as metric trace or source energy.")
    print()
    print("Consequence:")
    print()
    print("  J_V-driven zeta cannot enter ordinary metric scalar sector.")
    print("  Keep it non-metric / theorem-target only.")
    print()
    print("Bad failure:")
    print()
    print("  Declare residual killed, then reinsert it through kappa, energy accounting,")
    print("  or P_relax scalar radiation.")

    with out.governance_assessments():
        out.line(
            "B_s-only count-once good failure stated",
            StatusMark.DEFER,
            "deferred pending residual-kill or O theorem",
        )


def case_7_failure_controls(out: ScriptOutput):
    header("Case 7: Failure controls")

    print("B_s-only count-once fails if:")
    print()
    print("1. residual-kill is treated as derived")
    print("2. zeta residual remains metric-active")
    print("3. kappa restores killed trace")
    print("4. epsilon_vac_config becomes metric source")
    print("5. e_kappa becomes metric source")
    print("6. P_relax becomes Box zeta / Box kappa")
    print("7. non-metric bookkeeping shifts M_ext")
    print("8. residual creates exterior scalar charge")
    print("9. recovery checks choose counted sector")
    print("10. O is named but not defined")

    with out.governance_assessments():
        out.line("B_s-only count-once failure controls stated", StatusMark.WARN, "open second-spoon risks")


def case_8_next_tests(out: ScriptOutput):
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_B_s_only_insertion_count_once.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_residual_nonmetric_bookkeeping_rule.py")
    print("   Test what residual zeta/kappa may still do safely if not metric trace.")
    print()
    print("3. candidate_metric_insertion_early_failure_summary.py")
    print("   Use if count-once cannot be protected.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_residual_nonmetric_bookkeeping_rule.py")
    print()
    print("Reason:")
    print("  B_s-only count-once blocks metric residuals, but residual variables may still")
    print("  have safe non-metric bookkeeping or relaxation roles that need fencing.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.INFO, "candidate_residual_nonmetric_bookkeeping_rule.py")


def final_interpretation(out: ScriptOutput):
    header("Final interpretation")

    print("B_s-only insertion remains the safest provisional count-once rule.")
    print()
    print("Current rule:")
    print()
    print("  J_V-driven zeta may enter ordinary metric scalar trace only through B_s.")
    print("  Residual zeta/kappa metric trace is killed or non-metric.")
    print()
    print("Not derived:")
    print()
    print("  residual-kill")
    print("  O")
    print("  parent trace identity")
    print("  F_zeta/B_s dynamics")
    print()
    print("Best next script:")
    print()
    print("  candidate_residual_nonmetric_bookkeeping_rule.py")

    with out.governance_assessments():
        out.line(
            "B_s-only count-once audit complete",
            StatusMark.DEFER,
            "no count-once theorem derived; deferred",
        )


def main():
    header("Candidate B_s-Only Insertion Count-Once")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement(out)
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_second_spoon_routes(out)
    case_4b_symbolic_count_once(ns, out)
    case_5_decision_tree(out)
    case_6_good_failure(out)
    case_7_failure_controls(out)
    case_8_next_tests(out)
    final_interpretation(out)

    with archive.script_namespace(SCRIPT_ID) as ns2:
        # Proof obligations for count-once theorems
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_residual_kill_theorem_count_once",
            script_id=SCRIPT_ID,
            title="Derive residual-kill theorem for B_s-only count-once",
            status=ObligationStatus.OPEN,
            required_by=["B_s_only_count_once_route"],
            description=(
                "Derive that zeta_residual_metric = 0 and kappa_residual_metric = 0 "
                "or non-metric follow structurally from B_s insertion, not by convention."
            ),
        ))

        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_energy_accounting_recombination_rule",
            script_id=SCRIPT_ID,
            title="Derive energy/accounting recombination rule after B_s insertion",
            status=ObligationStatus.OPEN,
            required_by=["B_s_only_count_once_route"],
            description=(
                "Show that epsilon_vac_config and e_kappa cannot re-source killed residual "
                "metric scalar trace after B_s-only insertion."
            ),
        ))

        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_mass_accounting_theorem_count_once",
            script_id=SCRIPT_ID,
            title="Derive mass-accounting theorem for B_s-only insertion",
            status=ObligationStatus.OPEN,
            required_by=["B_s_only_count_once_route"],
            description=(
                "Show that B_s-only insertion and killed/non-metric residual "
                "do not alter A-sector exterior mass M_ext independently."
            ),
        ))

        # Route: B_s-only count-once provisional convention
        ns2.record_route(RouteRecord(
            route_id="B_s_only_count_once_provisional_convention",
            script_id=SCRIPT_ID,
            name="B_s-only count-once with provisional residual-kill",
            status=GovernanceStatus.CANDIDATE_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            required_obligations=[
                "derive_residual_kill_theorem_count_once",
                "derive_energy_accounting_recombination_rule",
                "derive_mass_accounting_theorem_count_once",
            ],
            activation_conditions=[
                "residual zeta/kappa metric trace is killed or non-metric",
                "energy/accounting cannot source extra metric trace",
                "no exterior scalar charge from residual",
                "M_ext is not shifted independently",
                "recovery remains downstream",
            ],
        ))

        # Branch decision: deferred pending theorems
        ns2.record_branch_decision(BranchDecisionRecord(
            decision_id="defer_count_once_no_residual_kill_theorem",
            script_id=SCRIPT_ID,
            branch_id="B_s_only_count_once",
            status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
            tier=ClaimTier.CONSTRAINED,
            reason_code=ReasonCode.MISSING_BOUNDARY_NEUTRALITY_THEOREM,
            obligation_ids=[
                "derive_residual_kill_theorem_count_once",
                "derive_energy_accounting_recombination_rule",
                "derive_mass_accounting_theorem_count_once",
            ],
            description=(
                "B_s-only count-once cannot be licensed because residual-kill and "
                "energy/accounting recombination theorems are missing. "
                "Convention survives provisionally."
            ),
        ))

        # Inventory marker
        ns2.record_derivation(
            derivation_id="B_s_only_insertion_count_once_marker",
            inputs=[],
            output=sp.Symbol("B_s_only_insertion_count_once_audited"),
            method="B_s_only_insertion_count_once_audit",
            status=Status.DERIVED,
            record_kind=RecordKind.INVENTORY_MARKER,
            is_placeholder=True,
        )

    out.print_summary()
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
