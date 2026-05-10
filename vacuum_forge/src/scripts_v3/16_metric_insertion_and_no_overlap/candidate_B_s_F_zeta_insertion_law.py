# Candidate B_s / F_zeta insertion law
#
# Group:
#   16_metric_insertion_and_no_overlap
#
# Script type:
#   SIEVE
#
# Purpose
# -------
# The current field-equation status says:
#
#   J_V-driven zeta may enter ordinary metric scalar trace only through B_s,
#   with residual zeta/kappa metric trace killed or non-metric,
#   unless a real no-overlap operator O is later derived.
#
# This first Group 16 script tests the metric-insertion door.
#
# Locked-door question:
#
#   Can J_V-driven zeta enter B_s through a concrete metric insertion rule
#   while residual zeta/kappa metric trace is killed or non-metric?
#
# New central structural candidate:
#
#   gamma_ij = exp(2 zeta / 3) * bar_gamma_ij
#   det(bar_gamma) = 1
#
# This is attractive because zeta = ln sqrt(gamma) is then the volume
# scalar, while bar_gamma_ij carries unimodular shape/shear.
#
# But it is dangerous if:
#
#   1. the conformal-volume split is treated as the full B_s law,
#   2. zeta is inserted into B_s and also left as residual metric trace,
#   3. gamma_like / AB recovery is used to choose coefficients,
#   4. the split becomes GR metric copying by another name.
#
# This script is a sieve, not a derivation.

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
class InsertionEntry:
    name: str
    candidate_rule: str
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
        dependency_id="group_15_status_after_residual_kill_marker",
        upstream_script_id="15_vacuum_current_and_exchange_continuity__candidate_group_15_status_after_residual_kill",
        upstream_derivation_id="group_15_status_after_residual_kill_marker",
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


def build_entries() -> List[InsertionEntry]:
    return [
        InsertionEntry(
            name="BI1: B_s / F_zeta insertion target",
            candidate_rule="B_s = F_zeta[A, zeta, J_V, Sigma_V, R_V] with residual zeta/kappa metric trace killed or non-metric",
            role="core Group 16 locked-door target",
            allowed_if="F_zeta is a concrete insertion rule and residual metric trace is killed/non-metric",
            forbidden_if="F_zeta is named but not defined, or zeta also remains residual metric trace",
            status="THEOREM_TARGET",
            missing="explicit F_zeta / B_s insertion law",
            consequence="decides whether J_V-driven zeta may enter ordinary metric scalar sector",
        ),
        InsertionEntry(
            name="BI2: conformal-volume split",
            candidate_rule="gamma_ij = exp(2 zeta / 3) bar_gamma_ij, det(bar_gamma)=1",
            role="structural volume/shear decomposition candidate",
            allowed_if="used as decomposition of spatial metric volume and unimodular shape, not as full dynamics",
            forbidden_if="treated as derived B_s field law or copied GR spatial metric",
            status="STRUCTURAL",
            missing="dynamics / source law / relation to B_s",
            consequence="makes zeta-volume role precise but does not derive insertion",
        ),
        InsertionEntry(
            name="BI3: determinant consistency check",
            candidate_rule="det(gamma_ij) = exp(2 zeta) det(bar_gamma) = exp(2 zeta)",
            role="consistency check for zeta = ln sqrt(gamma)",
            allowed_if="det(bar_gamma)=1 exactly within the chosen split",
            forbidden_if="zeta is also counted in bar_gamma determinant or residual metric trace",
            status="STRUCTURAL",
            missing="global/covariant status of spatial split",
            consequence="supports zeta as volume scalar in this split",
        ),
        InsertionEntry(
            name="BI4: isotropic trace insertion",
            candidate_rule="delta gamma_ij / gamma_ij includes isotropic piece (2/3) delta zeta",
            role="candidate local metric insertion for scalar volume trace",
            allowed_if="scalar trace enters only through B_s/conformal factor",
            forbidden_if="same delta zeta reappears as residual trace correction",
            status="CANDIDATE",
            missing="source law connecting J_V-driven zeta to B_s",
            consequence="minimal way zeta could affect scalar spatial metric trace",
        ),
        InsertionEntry(
            name="BI5: B_s from zeta only",
            candidate_rule="B_s = F_zeta[zeta]",
            role="minimal volume-only insertion branch",
            allowed_if="boundary-neutral and recovery checks are downstream",
            forbidden_if="chosen to force gamma_like=1 or AB recovery",
            status="RISK",
            missing="normalization, boundary theorem, recovery audit",
            consequence="simple but likely underdetermined and coefficient-prone",
        ),
        InsertionEntry(
            name="BI6: B_s from A and zeta",
            candidate_rule="B_s = F_zeta[A, zeta]",
            role="mass/volume companion insertion branch",
            allowed_if="A contribution and zeta contribution are count-once and not GR-copied",
            forbidden_if="A_spatial is imported from Schwarzschild/GR or zeta patches the leftover",
            status="CANDIDATE",
            missing="parent relation between A and zeta",
            consequence="possible bridge to A_spatial, but high GR-smuggling risk",
        ),
        InsertionEntry(
            name="BI7: B_s from J_V-supported zeta",
            candidate_rule="B_s = F_zeta[zeta(J_V)]",
            role="volume-current-supported insertion branch",
            allowed_if="J_V is real and zeta support is boundary-neutral",
            forbidden_if="J_V remains decorative or acausal repair current",
            status="CANDIDATE",
            missing="physical J_V flux law and zeta support law",
            consequence="keeps Group 15 current branch relevant without solving it here",
        ),
        InsertionEntry(
            name="BI8: B_s from Sigma/R-balanced zeta",
            candidate_rule="B_s = F_zeta[zeta] with nabla_mu J_V^mu = Sigma_V - R_V as source balance",
            role="exchange-continuity-assisted insertion branch",
            allowed_if="Sigma/R roles become operators and do not double-count",
            forbidden_if="Sigma/R are role labels used to choose B_s",
            status="RISK",
            missing="Sigma_V, R_V, flux direction, support",
            consequence="currently too underdefined for a true insertion law",
        ),
        InsertionEntry(
            name="BI9: B_s from parent trace constraint",
            candidate_rule="parent trace identity derives B_s and residual-kill/no-overlap together",
            role="best theorem-level route",
            allowed_if="identity is not GR rewrite and fixes trace count before recovery",
            forbidden_if="identity is decorative or imports Einstein spatial equation",
            status="THEOREM_TARGET",
            missing="parent trace identity",
            consequence="would be strongest route if later derived",
        ),
        InsertionEntry(
            name="BI10: B_s-only metric entry",
            candidate_rule="J_V-driven zeta enters metric scalar trace only through B_s",
            role="current safest recombination convention",
            allowed_if="residual zeta/kappa metric trace is killed or non-metric",
            forbidden_if="residual zeta/kappa remains metric-active",
            status="SAFE_IF",
            missing="derivation of residual-kill or O",
            consequence="prevents double-counting while allowing a provisional insertion branch",
        ),
        InsertionEntry(
            name="BI11: residual-kill attachment",
            candidate_rule="zeta_residual_metric = 0 and kappa_residual_metric = 0/non-metric after B_s insertion",
            role="mandatory safety attachment for B_s-only branch",
            allowed_if="marked provisional unless O/parent identity derives it",
            forbidden_if="treated as derived postulate or bypassed by energy/accounting source",
            status="REQUIRED",
            missing="residual-kill derivation",
            consequence="without this, B_s insertion double-counts scalar trace",
        ),
        InsertionEntry(
            name="BI12: kappa diagnostic fence",
            candidate_rule="kappa remains areal diagnostic / non-metric residual / separately neutral unless derived",
            role="prevents kappa from undoing residual-kill",
            allowed_if="kappa does not enter as independent metric trace",
            forbidden_if="kappa restores killed zeta residual trace",
            status="REQUIRED",
            missing="kappa cleanup theorem",
            consequence="preserves Group 14/15 safety boundary",
        ),
        InsertionEntry(
            name="BI13: energy/accounting exclusion",
            candidate_rule="epsilon_vac_config and e_kappa do not reinsert killed residual as metric source",
            role="prevents hidden second trace through accounting",
            allowed_if="accounting is diagnostic or recombined once",
            forbidden_if="killed residual becomes source energy or coefficient reservoir",
            status="REQUIRED",
            missing="energy/accounting recombination rule",
            consequence="closes common back door for double-counting",
        ),
        InsertionEntry(
            name="BI14: GR-copy insertion",
            candidate_rule="B_s copied from Schwarzschild/GR spatial metric or chosen by gamma_like=1",
            role="forbidden shortcut",
            allowed_if="never as derivation",
            forbidden_if="used as F_zeta or parent trace identity",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents recovery target from becoming construction",
        ),
        InsertionEntry(
            name="BI15: B=1/A construction",
            candidate_rule="B_s fixed by B=1/A generally",
            role="forbidden overextension of exterior diagnostic",
            allowed_if="only as reduced static exterior recovery check",
            forbidden_if="used as general B_s insertion law",
            status="REJECTED",
            missing="not pursued",
            consequence="prevents areal exterior recovery from becoming parent law",
        ),
        InsertionEntry(
            name="BI16: zeta-both branch",
            candidate_rule="zeta changes B_s and also remains independent residual metric trace",
            role="forbidden double-counting branch",
            allowed_if="never unless real O explicitly separates neutral residual",
            forbidden_if="accepted without O",
            status="REJECTED",
            missing="not pursued",
            consequence="kills the second-spoon branch",
        ),
        InsertionEntry(
            name="BI17: boundary-neutral insertion requirement",
            candidate_rule="B_s/F_zeta insertion creates no exterior zeta/kappa charge, no scalar far flux, no M_ext shift",
            role="ordinary-sector safety guard",
            allowed_if="boundary neutrality is structural",
            forbidden_if="insertion requires boundary repair or scalar charge cancellation",
            status="REQUIRED",
            missing="boundary neutrality theorem for insertion",
            consequence="unsafe insertion cannot support ordinary sector",
        ),
        InsertionEntry(
            name="BI18: recovery downstream",
            candidate_rule="gamma_like and AB are tested only after F_zeta/no-overlap are fixed",
            role="anti-smuggling guard",
            allowed_if="recovery is check only",
            forbidden_if="used to choose coefficients, residual-kill, or insertion map",
            status="RECOVERY_TARGET",
            missing="solutions after insertion law",
            consequence="keeps GR-compatible behavior from becoming construction",
        ),
        InsertionEntry(
            name="BI19: no-overlap alternative",
            candidate_rule="real O permits neutral residual metric trace without overlap",
            role="alternative to residual-kill",
            allowed_if="O is explicitly defined and boundary/mass safety are proved",
            forbidden_if="neutral residual is asserted to avoid residual-kill",
            status="RISK",
            missing="O operator, pairing/projectors, boundary theorem",
            consequence="theorem-heavy escape hatch, not current working route",
        ),
        InsertionEntry(
            name="BI20: recommended next move",
            candidate_rule="if B_s-only insertion remains safest, test exactly what is forbidden from entering separately",
            role="next local bottleneck",
            allowed_if="no explicit F_zeta is derived in this script",
            forbidden_if="jumping to parent equation with residual status unresolved",
            status="RECOMMENDED",
            missing="count-once B_s-only insertion audit",
            consequence="next script should be candidate_B_s_only_insertion_count_once.py",
        ),
    ]


def print_entry(e: InsertionEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Candidate rule: {e.candidate_rule}")
    print(f"Role: {e.role}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    print(f"[INFO] {e.name}: {e.status}")
    print(f"Missing: {e.missing}")
    print(f"Consequence: {e.consequence}")


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: B_s / F_zeta insertion problem")

    print("Question:")
    print()
    print("  Can J_V-driven zeta enter B_s through a concrete metric insertion rule")
    print("  while residual zeta/kappa metric trace is killed or non-metric?")
    print()
    print("Central structural split:")
    print()
    print("  gamma_ij = exp(2 zeta / 3) bar_gamma_ij")
    print("  det(bar_gamma) = 1")
    print()
    print("Goal:")
    print()
    print("  test whether the conformal-volume split can support B_s insertion")
    print("  without becoming a full field equation by declaration")
    print()
    print("Discipline:")
    print()
    print("  do not copy GR spatial metric")
    print("  do not tune gamma_like")
    print("  do not use B=1/A as construction")
    print("  do not let zeta enter both B_s and residual metric trace")
    print("  do not let kappa restore killed residual trace")
    print("  do not reinsert killed residual through energy/accounting")
    print("  keep recovery downstream")

    with out.governance_assessments():
        out.line("B_s/F_zeta insertion problem posed", StatusMark.OBLIGATION, "required before insertion can proceed")


def case_1_inventory(entries: List[InsertionEntry]):
    header("Case 1: B_s / F_zeta insertion inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[InsertionEntry], out: ScriptOutput):
    header("Case 2: Compact B_s / F_zeta insertion ledger")

    print("| Entry | Candidate rule | Status | Consequence |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.candidate_rule.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.consequence.replace("|", "/")
            + " |"
        )

    with out.governance_assessments():
        out.line("compact insertion ledger produced", StatusMark.INFO, "inventory of B_s/F_zeta candidate routes")


def case_3_status_counts(entries: List[InsertionEntry], out: ScriptOutput):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  The conformal-volume split is structurally useful but not a B_s field law.")
    print("  B_s-only insertion with residual-kill remains the safest provisional branch.")
    print("  B_s from A/zeta or J_V-supported zeta remains candidate/theorem-target only.")
    print("  B_s from Sigma/R is too underdefined while Sigma/R are role-level only.")
    print("  GR-copy, B=1/A construction, and zeta-both branches are rejected.")
    print("  Next gate is count-once: what exactly is forbidden from entering separately?")

    with out.governance_assessments():
        out.line("B_s/F_zeta insertion status count produced", StatusMark.INFO, "insertion inventory enumerated")


def case_4_conformal_split_check(out: ScriptOutput):
    header("Case 4: Conformal-volume split check")

    print("Given:")
    print()
    print("  gamma_ij = exp(2 zeta / 3) bar_gamma_ij")
    print("  det(bar_gamma) = 1")
    print()
    print("Then in 3 spatial dimensions:")
    print()
    print("  det(gamma_ij) = exp(2 zeta) det(bar_gamma)")
    print("                = exp(2 zeta)")
    print()
    print("Therefore:")
    print()
    print("  sqrt(gamma) = exp(zeta)")
    print("  zeta = ln sqrt(gamma)")
    print()
    print("This is a strong structural consistency check.")
    print()
    print("But it does not derive:")
    print()
    print("  source law for zeta")
    print("  B_s / F_zeta insertion dynamics")
    print("  boundary neutrality")
    print("  no-overlap")
    print("  residual-kill")
    print("  recovery coefficients")
    print("  parent equation")

    with out.governance_assessments():
        out.line("conformal-volume split checked", StatusMark.INFO, "structural consistency only, not dynamics")


def case_4b_symbolic_conformal_split(ns, out: ScriptOutput):
    header("Case 4b: Symbolic conformal-volume check")

    zeta = sp.symbols("zeta", real=True)
    delta_zeta = sp.symbols("delta_zeta", real=True)
    determinant = sp.exp(2 * zeta)
    sqrt_determinant = sp.sqrt(determinant)
    volume_scalar = sp.simplify(sp.log(sqrt_determinant).subs(sqrt_determinant, sp.exp(zeta)))
    isotropic_fraction = sp.simplify(
        sp.diff(sp.exp(sp.Rational(2, 3) * zeta), zeta) / sp.exp(sp.Rational(2, 3) * zeta) * delta_zeta
    )

    print("Principal-branch determinant relation:")
    print(f"  det(gamma_ij) = {determinant}")
    print(f"  sqrt(gamma) = exp(zeta)")
    print(f"  ln sqrt(gamma) = {volume_scalar}")
    print(f"  delta gamma_ij / gamma_ij = {isotropic_fraction}")

    if volume_scalar == zeta and isotropic_fraction == sp.Rational(2, 3) * delta_zeta:
        with out.derived_results():
            out.line(
                "symbolic conformal-volume relation",
                StatusMark.PASS,
                f"ln sqrt(gamma) = {volume_scalar}, delta gamma_ij / gamma_ij = {isotropic_fraction}",
            )
    else:
        with out.derived_results():
            out.line("symbolic conformal-volume relation", StatusMark.FAIL, "unexpected symbolic mismatch")

    ns.record_derivation(
        derivation_id="conformal_volume_split_symbolic_relation",
        inputs=[determinant, delta_zeta],
        output=sp.Tuple(volume_scalar, isotropic_fraction),
        method="symbolic conformal-volume split check",
        status=Status.DERIVED,
        record_kind=RecordKind.DERIVATION,
        scope="principal branch, det(bar_gamma)=1 convention",
    )


def case_5_decision_tree(out: ScriptOutput):
    header("Case 5: Insertion decision tree")

    print("Decision tree:")
    print()
    print("1. Conformal-volume split:")
    print("   structurally supports zeta as volume scalar, but not dynamics.")
    print()
    print("2. B_s from zeta only:")
    print("   simple but likely underdetermined and recovery-tuning-prone.")
    print()
    print("3. B_s from A and zeta:")
    print("   promising but high GR-smuggling risk.")
    print()
    print("4. B_s from J_V-supported zeta:")
    print("   keeps current branch relevant, but J_V remains unresolved.")
    print()
    print("5. B_s from Sigma/R-balanced zeta:")
    print("   too early while Sigma/R are role-level only.")
    print()
    print("6. Parent trace identity:")
    print("   strongest theorem route, still missing.")
    print()
    print("7. B_s-only with residual-kill:")
    print("   safest provisional convention.")
    print()
    print("8. Zeta as both B_s and residual trace:")
    print("   rejected unless real O is later derived.")

    with out.governance_assessments():
        out.line("insertion decision tree stated", StatusMark.INFO, "recommended next is count-once audit")


def case_6_good_failure(out: ScriptOutput):
    header("Case 6: Good failure / branch decision")

    print("Good failure:")
    print()
    print("  No concrete F_zeta insertion law can be stated without")
    print("  GR-copying, recovery tuning, or residual overlap.")
    print()
    print("Consequence:")
    print()
    print("  J_V-driven zeta remains non-metric / theorem-target only,")
    print("  or enters B_s only under provisional residual-kill convention.")
    print()
    print("Bad failure:")
    print()
    print("  Declare gamma_ij = exp(2 zeta / 3) bar_gamma_ij to be the field equation")
    print("  and allow residual zeta/kappa metric trace to remain active.")

    with out.governance_assessments():
        out.line("B_s/F_zeta insertion good failure stated", StatusMark.DEFER, "deferred pending insertion law theorem")


def case_7_failure_controls(out: ScriptOutput):
    header("Case 7: Failure controls")

    print("B_s/F_zeta insertion fails if:")
    print()
    print("1. conformal-volume split is treated as full dynamics")
    print("2. B_s is copied from GR spatial metric")
    print("3. gamma_like fixes coefficients")
    print("4. B=1/A is used as general construction")
    print("5. zeta enters both B_s and residual metric trace")
    print("6. kappa restores killed residual trace")
    print("7. killed residual reappears as energy/accounting source")
    print("8. exterior scalar charge or far-zone scalar flux appears")
    print("9. J_V shifts M_ext independently of A")
    print("10. recovery checks choose insertion or residual-kill")

    with out.governance_assessments():
        out.line("B_s/F_zeta insertion failure controls stated", StatusMark.WARN, "open risks enumerated")


def case_8_next_tests(out: ScriptOutput):
    header("Case 8: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_B_s_F_zeta_insertion_law.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_B_s_only_insertion_count_once.py")
    print("   Test exactly what is forbidden from entering separately if zeta enters through B_s.")
    print()
    print("3. candidate_metric_insertion_early_failure_summary.py")
    print("   Use if all insertion branches fail immediately.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_B_s_only_insertion_count_once.py")
    print()
    print("Reason:")
    print("  The conformal-volume split makes zeta-volume insertion structurally plausible,")
    print("  but the next gate is count-once recombination, not parent equation construction.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.INFO, "candidate_B_s_only_insertion_count_once.py")


def final_interpretation(out: ScriptOutput):
    header("Final interpretation")

    print("The conformal-volume split is a useful structural handle:")
    print()
    print("  gamma_ij = exp(2 zeta / 3) bar_gamma_ij")
    print("  det(bar_gamma) = 1")
    print()
    print("It supports zeta as the spatial volume scalar.")
    print()
    print("But it does not yet derive B_s/F_zeta insertion.")
    print()
    print("Best current interpretation:")
    print()
    print("  J_V-driven zeta may enter ordinary metric scalar trace only through B_s,")
    print("  with residual zeta/kappa metric trace killed or non-metric,")
    print("  unless a real O is later derived.")
    print()
    print("Best next script:")
    print()
    print("  candidate_B_s_only_insertion_count_once.py")

    with out.governance_assessments():
        out.line("B_s/F_zeta insertion audit complete", StatusMark.DEFER, "no insertion law derived; deferred")


def main():
    header("Candidate B_s / F_zeta Insertion Law")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement(out)
    entries = build_entries()
    case_1_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_conformal_split_check(out)
    case_4b_symbolic_conformal_split(ns, out)
    case_5_decision_tree(out)
    case_6_good_failure(out)
    case_7_failure_controls(out)
    case_8_next_tests(out)
    final_interpretation(out)

    with archive.script_namespace(SCRIPT_ID) as ns2:
        # Proof obligations for the missing insertion theorems
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_F_zeta_B_s_insertion_law",
            script_id=SCRIPT_ID,
            title="Derive explicit F_zeta / B_s insertion law",
            status=ObligationStatus.OPEN,
            required_by=["B_s_metric_insertion_route"],
            description=(
                "Derive a concrete insertion rule B_s = F_zeta[A, zeta, J_V, Sigma_V, R_V] "
                "that does not rely on GR-copying, recovery tuning, or residual overlap."
            ),
        ))

        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_residual_kill_or_O_for_insertion",
            script_id=SCRIPT_ID,
            title="Derive residual-kill or no-overlap operator O for B_s insertion",
            status=ObligationStatus.OPEN,
            required_by=["B_s_metric_insertion_route"],
            description=(
                "Show that residual zeta/kappa metric trace is structurally killed or "
                "a real no-overlap operator O is defined after B_s insertion."
            ),
        ))

        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_boundary_neutrality_for_B_s_insertion",
            script_id=SCRIPT_ID,
            title="Derive boundary neutrality theorem for B_s insertion",
            status=ObligationStatus.OPEN,
            required_by=["B_s_metric_insertion_route"],
            description=(
                "Show that B_s/F_zeta insertion creates no exterior scalar charge, "
                "no far-zone scalar flux, no shell source, and no independent M_ext shift."
            ),
        ))

        # Route for the B_s-only provisional convention
        ns2.record_route(RouteRecord(
            route_id="B_s_only_residual_kill_provisional_route",
            script_id=SCRIPT_ID,
            name="B_s-only insertion with provisional residual-kill",
            status=GovernanceStatus.CANDIDATE_ROUTE,
            tier=ClaimTier.CONSTRAINED,
            required_obligations=[
                "derive_F_zeta_B_s_insertion_law",
                "derive_residual_kill_or_O_for_insertion",
                "derive_boundary_neutrality_for_B_s_insertion",
            ],
            activation_conditions=[
                "F_zeta insertion law is explicit and not GR-copied",
                "residual zeta/kappa metric trace is killed or non-metric",
                "boundary neutrality holds structurally",
                "recovery remains downstream",
            ],
        ))

        # Branch decision: rejected routes
        ns2.record_branch_decision(BranchDecisionRecord(
            decision_id="defer_B_s_F_zeta_insertion_no_law",
            script_id=SCRIPT_ID,
            branch_id="B_s_F_zeta_metric_insertion",
            status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
            tier=ClaimTier.CONSTRAINED,
            reason_code=ReasonCode.MISSING_BOUNDARY_NEUTRALITY_THEOREM,
            obligation_ids=[
                "derive_F_zeta_B_s_insertion_law",
                "derive_residual_kill_or_O_for_insertion",
                "derive_boundary_neutrality_for_B_s_insertion",
            ],
            description=(
                "No concrete F_zeta insertion law was derived. The insertion branch "
                "remains open but cannot be licensed without insertion law, residual-kill, "
                "and boundary neutrality theorems."
            ),
        ))

        # Inventory marker for the sieve audit
        ns2.record_derivation(
            derivation_id="B_s_F_zeta_insertion_law_marker",
            inputs=[],
            output=sp.Symbol("B_s_F_zeta_insertion_law_audited"),
            method="B_s_F_zeta_insertion_law_audit",
            status=Status.DERIVED,
            record_kind=RecordKind.INVENTORY_MARKER,
            is_placeholder=True,
        )

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
