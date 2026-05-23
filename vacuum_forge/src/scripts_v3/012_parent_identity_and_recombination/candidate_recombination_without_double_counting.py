# Candidate recombination without double-counting
#
# Group:
#   12_parent_identity_and_recombination
#
# Script type:
#   INVENTORY

# Purpose
# -------
# The boundary mass preservation audit found:
#
#   exterior mass is A-sector flux,
#   delta M_ext from kappa relaxation must vanish,
#   Q_kappa must vanish,
#   F_kappa(R+) must vanish,
#   exterior kappa must relax to zero,
#   recombination must preserve exterior Schwarzschild.
#
# The next gate is recombination:
#
#   How do A, W_i, h_TT, and kappa combine into a geometry-like object
#   without reintroducing scalar double-counting or silently importing GR?
#
# This script builds a disciplined recombination ledger.
#
# It is not a covariant recombination derivation.

from dataclasses import dataclass
from pathlib import Path
from typing import List

import sympy as sp

from vacuumforge import ProjectArchive, Status, TheoryContext
from vacuumforge.metric.concrete_check import check_concrete_metric
from vacuumforge.governance import (
    BranchDecisionRecord,
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


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


@dataclass
class RecombinationEntry:
    name: str
    component: str
    allowed_source: str
    forbidden_source: str
    candidate_form: str
    status: str
    risk: str
    missing: str


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="boundary_mass_preservation_identity_marker",
        upstream_script_id="012_parent_identity_and_recombination__candidate_boundary_mass_preservation_identity",
        upstream_derivation_id="boundary_mass_preservation_identity_marker",
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


def build_entries() -> List[RecombinationEntry]:
    return [
        RecombinationEntry(
            name="R1: lapse/time scalar from A",
            component="g_tt-like component",
            allowed_source="A-sector scalar mass response",
            forbidden_source="independent kappa mass scalar or A_rad",
            candidate_form="g_tt ~ -A*c^2 in reduced/static weak map",
            status="DERIVED_REDUCED",
            risk="Overextending reduced static scalar result.",
            missing="Covariant parent lapse/recombination map.",
        ),
        RecombinationEntry(
            name="R2: exterior radial reciprocal from A and kappa",
            component="g_rr-like radial scalar piece",
            allowed_source="AB=e^(2*kappa), exterior kappa=0",
            forbidden_source="independent B chosen by GR form or exterior kappa tail",
            candidate_form="kappa_ext=0 -> B=1/A",
            status="DERIVED_REDUCED",
            risk="Treating areal-gauge relation as full covariant derivation.",
            missing="Gauge/physical split for B and kappa.",
        ),
        RecombinationEntry(
            name="R3: vector shift from W_i",
            component="g_0i-like component",
            allowed_source="transverse W_i sourced by j_T",
            forbidden_source="longitudinal current P_L j or scalar continuity",
            candidate_form="g_0i ~ coefficient * W_i",
            status="STRUCTURAL",
            risk="GR shift coefficient imported by hand.",
            missing="beta_W / normalization / parent shift map.",
        ),
        RecombinationEntry(
            name="R4: tensor radiation from h_TT",
            component="trace-free spatial tensor",
            allowed_source="h_ij^TT sourced by P_TT stress",
            forbidden_source="trace stress or kappa trace response",
            candidate_form="g_ij contains h_ij^TT as trace-free radiative part",
            status="STRUCTURAL",
            risk="TT form correct but coupling/normalization matched.",
            missing="C_T, K_T, tensor action stiffness.",
        ),
        RecombinationEntry(
            name="R5: kappa limited to trace/volume matching",
            component="scalar spatial / AB diagnostic role",
            allowed_source="trace/pressure shifts kappa_min; kappa relaxes first-order",
            forbidden_source="rho-sourced long-range scalar mass response",
            candidate_form="kappa enters AB=e^(2*kappa) or local trace/volume matching only",
            status="CONSTRAINED",
            risk="Kappa becomes second scalar gravity field.",
            missing="P_recombination role of kappa.",
        ),
        RecombinationEntry(
            name="R6: scalar response counted once",
            component="scalar part of recombined geometry",
            allowed_source="A-sector mass response plus constrained kappa trace correction",
            forbidden_source="same rho response counted in both A and kappa",
            candidate_form="rho -> A; trace -> kappa_min; no duplicate scalar mass channel",
            status="REQUIRED",
            risk="Scalar double-counting.",
            missing="Explicit scalar accounting rule in recombination map.",
        ),
        RecombinationEntry(
            name="R7: exterior Schwarzschild preservation",
            component="exterior recombined geometry",
            allowed_source="A_ext and B=1/A with kappa_ext=0",
            forbidden_source="recombination reintroduces exterior trace/scalar field",
            candidate_form="outside ordinary matter: kappa=0, A=1-2GM/(c^2r), B=1/A",
            status="REQUIRED",
            risk="Exterior scalar deviation introduced by recombination.",
            missing="P_recombination proof.",
        ),
        RecombinationEntry(
            name="R8: scalar radiation excluded after recombination",
            component="radiative content",
            allowed_source="h_TT only as ordinary long-range radiation",
            forbidden_source="A_rad, Box kappa, free vector radiation",
            candidate_form="ordinary radiation projector selects h_ij^TT only",
            status="CONSTRAINED",
            risk="Hidden breathing mode after metric assembly.",
            missing="Parent radiation projector.",
        ),
        RecombinationEntry(
            name="R9: boundary smoothing remains local/diagnostic",
            component="near-boundary geometry",
            allowed_source="kappa/joint-minimum smoothing with fixed M_ext",
            forbidden_source="boundary smoothing changes exterior 1/r coefficient",
            candidate_form="near-boundary adjustments preserve A_ext coefficient",
            status="CONSTRAINED",
            risk="Boundary mass tuning / overclaimed prediction.",
            missing="Boundary mass theorem and observable map.",
        ),
        RecombinationEntry(
            name="R10: coefficient map remains labeled",
            component="observable coefficients",
            allowed_source="parent action/stiffness only",
            forbidden_source="GR coefficient insertion as derivation",
            candidate_form="alpha_W/K_c, beta_W, C_T, K_T remain UNKNOWN/MATCHED until derived",
            status="MISSING",
            risk="Silent GR import.",
            missing="P_coeff / action stiffness derivation.",
        ),
    ]


def print_entry(e: RecombinationEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Component: {e.component}")
    print(f"Allowed source: {e.allowed_source}")
    print(f"Forbidden source: {e.forbidden_source}")
    print(f"Candidate form: {e.candidate_form}")
    print(f"[INFO] {e.name}: {e.status}")
    print(f"Risk: {e.risk}")
    print(f"Missing: {e.missing}")


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: Recombination without double-counting problem")

    print("Question:")
    print()
    print("  How can A, W_i, h_TT, and kappa recombine without scalar double-counting?")
    print()
    print("Goal:")
    print()
    print("  state a disciplined recombination map with forbidden overlaps")
    print()
    print("Discipline:")
    print()
    print("  A carries exterior mass")
    print("  kappa does not carry rho mass response")
    print("  h_TT is trace-free radiation")
    print("  W_i is transverse")
    print("  exterior Schwarzschild must be preserved when kappa=0")
    print("  do not import GR coefficients as derivation")

    with out.unresolved_obligations():
        out.line("recombination problem posed", StatusMark.OBLIGATION, "P_recombination not yet derived")


def case_1_recombination_inventory(entries: List[RecombinationEntry]):
    header("Case 1: Recombination inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[RecombinationEntry], out: ScriptOutput):
    header("Case 2: Compact recombination ledger")

    print("| Recombination piece | Component | Candidate form | Status | Missing |")
    print("|---|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.component.replace("|", "/")
            + " | "
            + e.candidate_form.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.missing.replace("|", "/")
            + " |"
        )

    with out.governance_assessments():
        out.line("compact recombination ledger produced", StatusMark.INFO, "10 recombination pieces recorded")


def case_3_status_counts(entries: List[RecombinationEntry], out: ScriptOutput):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Exterior scalar pieces are reduced-derived.")
    print("  Vector/tensor/kappa recombination is structural or constrained.")
    print("  Coefficient mapping remains missing.")

    with out.governance_assessments():
        out.line("recombination status count produced", StatusMark.INFO, str(counts))


def case_4_candidate_reduced_map(out: ScriptOutput):
    header("Case 4: Candidate reduced recombination map")

    print("Candidate reduced map:")
    print()
    print("  g_tt  <- A")
    print("  g_0i  <- W_i")
    print("  g_ij  <- scalar_spatial_response(A) + kappa_trace_matching + h_ij^TT")
    print()
    print("with constraints:")
    print()
    print("  rho -> A only")
    print("  trace/pressure -> kappa_min only")
    print("  kappa_ext = 0")
    print("  h_ij^TT trace-free")
    print("  W_i transverse")
    print("  source(A_rad ordinary massless)=0")
    print("  delta M_ext|kappa_relaxation = 0")
    print()
    print("This is a reduced map, not a covariant derivation.")

    with out.governance_assessments():
        out.line("candidate reduced recombination map stated", StatusMark.DEFER, "covariant derivation remains open")


def case_5_no_double_counting_checks(out: ScriptOutput):
    header("Case 5: No-double-counting checks")

    print("Recombination checks:")
    print()
    print("1. Does rho appear anywhere except A-sector mass response?")
    print("2. Does kappa produce an exterior 1/r field?")
    print("3. Does trace stress enter h_TT?")
    print("4. Does P_L j enter W_i?")
    print("5. Does boundary smoothing change M_ext?")
    print("6. Does A_rad reappear after recombination?")
    print("7. Are vector/tensor coefficients labeled rather than imported?")
    print("8. Does exterior kappa=0 preserve B=1/A?")
    print("9. Is scalar spatial response counted exactly once?")
    print("10. Is near-boundary deviation still diagnostic-only?")

    with out.governance_assessments():
        out.line("recombination no-double-counting checks stated", StatusMark.DEFER, "all 10 checks are requirements")


def case_5b_vf_recombination_crosscheck(ns, out: ScriptOutput):
    header("Case 5b: VacuumForge recombination cross-check")

    ctx = TheoryContext("candidate_recombination_without_double_counting")
    ms = ctx.define_equal_response_algebraic_symbols()
    A_value = 1 - 2 * ms.G * ms.M / (ms.r * ms.c**2)
    B_value = 1 / A_value
    result = check_concrete_metric(ctx, A_value, B_value, ["reciprocal_scaling"])[0]
    product = sp.simplify(A_value * B_value)

    print(f"A_value = {A_value}")
    print(f"B_value = {B_value}")
    print(f"A_value * B_value = {product}")
    print(f"ConcreteMetricCheck status = {result.status}")

    ok = result.status == "satisfied_by_construction" and product == 1

    with out.derived_results():
        out.line(
            "recombination ledger preserves reciprocal exterior metric condition",
            StatusMark.PASS if ok else StatusMark.FAIL,
            f"A*B = {product}; check = {result.status}",
        )

    ns.record_derivation(
        derivation_id="recombination_reciprocal_metric_crosscheck",
        inputs=[A_value, B_value],
        output=product,
        method="ConcreteMetricCheck reciprocal_scaling",
        status=Status.DERIVED,
        record_kind=RecordKind.COMPATIBILITY_EXAMPLE,
    )


def case_6_failure_controls(out: ScriptOutput):
    header("Case 6: Failure controls")

    print("Recombination fails if:")
    print()
    print("1. It copies GR metric components and calls them derived.")
    print("2. A and kappa both carry the same rho scalar response.")
    print("3. Kappa reintroduces exterior scalar charge.")
    print("4. h_TT receives trace stress.")
    print("5. W_i receives longitudinal current.")
    print("6. Boundary smoothing changes the exterior 1/r coefficient.")
    print("7. Scalar radiation appears as A_rad or Box kappa.")
    print("8. Coefficients are matched but claimed derived.")

    with out.governance_assessments():
        out.line("recombination failure controls stated", StatusMark.DEFER, "failure controls policy-guarded")


def case_7_next_tests(out: ScriptOutput):
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_recombination_without_double_counting.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_relaxation_energy_accounting_identity.py")
    print("   Define the energy destination for Gamma_relax.")
    print()
    print("3. candidate_parent_identity_template_v2.py")
    print("   Attempt a tighter parent identity scaffold using exclusions/projectors/recombination.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_relaxation_energy_accounting_identity.py")
    print()
    print("Reason:")
    print("  Recombination can be constrained, but relaxation energy remains explicitly missing.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.DEFER, "relaxation energy accounting script is the next gate")


def final_interpretation():
    header("Final interpretation")

    print("A disciplined recombination map is possible only if:")
    print()
    print("  A carries exterior mass")
    print("  W_i carries transverse vector response")
    print("  h_TT carries trace-free radiation")
    print("  kappa is limited to trace/volume matching")
    print("  scalar response is counted once")
    print("  exterior kappa=0 preserves Schwarzschild")
    print("  scalar radiation stays rejected")
    print("  boundary smoothing preserves M_ext")
    print("  coefficients remain labeled until derived")
    print()
    print("Possible next artifact:")
    print("  candidate_recombination_without_double_counting.md")
    print()
    print("Possible next script:")
    print("  candidate_relaxation_energy_accounting_identity.py")


def main():
    header("Candidate Recombination Without Double-Counting")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement(out)
    entries = build_entries()
    case_1_recombination_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_candidate_reduced_map(out)
    case_5_no_double_counting_checks(out)
    case_5b_vf_recombination_crosscheck(ns, out)
    case_6_failure_controls(out)
    case_7_next_tests(out)
    final_interpretation()

    # Proof obligations for missing recombination pieces
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_P_recombination_scalar_counted_once_R6",
        script_id=SCRIPT_ID,
        title="Derive explicit scalar accounting rule in recombination map (R6)",
        status=ObligationStatus.OPEN,
        description=(
            "Show that rho routes to A only and that trace routes to kappa_min only, "
            "with no duplication of rho scalar mass response in both A and kappa sectors."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_P_recombination_exterior_Schwarzschild_R7",
        script_id=SCRIPT_ID,
        title="Derive P_recombination proof for exterior Schwarzschild preservation (R7)",
        status=ObligationStatus.OPEN,
        description=(
            "Show that metric recombination gives exterior Schwarzschild reduced form "
            "A=1-2GM/(c^2*r), B=1/A when kappa_ext=0. P_recombination proof required."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_P_coeff_action_stiffness_recombination_R10",
        script_id=SCRIPT_ID,
        title="Derive P_coeff / action stiffness principle for observable coefficients (R10)",
        status=ObligationStatus.OPEN,
        description=(
            "alpha_W/K_c, beta_W, C_T, K_T must be derived from parent action/stiffness, "
            "not matched to GR. They remain UNKNOWN/MATCHED until this derivation is completed."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_covariant_recombination_lapse_shift_R1_R3",
        script_id=SCRIPT_ID,
        title="Derive covariant parent lapse/recombination and shift map (R1, R3)",
        status=ObligationStatus.OPEN,
        description=(
            "The reduced map g_tt <- A and g_0i <- W_i must be elevated to a covariant "
            "parent recombination derivation. beta_W normalization must be derived."
        ),
    ))

    # Policy claim: GR metric copying forbidden in recombination
    ns.record_claim(ClaimRecord(
        claim_id="gr_metric_copying_in_recombination_forbidden",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Recombination of A, W_i, h_TT, kappa into a geometry-like object must not "
            "copy GR metric components by form. g_tt, g_0i, g_ij cannot be assigned the "
            "full GR weak-field form before parent recombination is derived."
        ),
    ))

    # Candidate route: reduced recombination map
    ns.record_route(RouteRecord(
        route_id="reduced_recombination_map_candidate",
        script_id=SCRIPT_ID,
        name="Candidate reduced recombination map: g_tt<-A, g_0i<-W_i, g_ij<-scalar+kappa+h_TT",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[
            "derive_P_recombination_scalar_counted_once_R6",
            "derive_P_recombination_exterior_Schwarzschild_R7",
            "derive_covariant_recombination_lapse_shift_R1_R3",
        ],
        activation_conditions=[
            "rho routes to A only",
            "trace routes to kappa_min only",
            "kappa_ext = 0 gives B = 1/A",
            "h_ij^TT trace-free and A*B reciprocal crosscheck passes",
            "no GR coefficients inserted as derivation",
        ],
    ))

    # Branch decision: covariant recombination derivation deferred
    ns.record_branch_decision(BranchDecisionRecord(
        decision_id="defer_covariant_recombination_derivation",
        script_id=SCRIPT_ID,
        branch_id="covariant_recombination_derivation",
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        tier=ClaimTier.CONSTRAINED,
        obligation_ids=[
            "derive_P_recombination_scalar_counted_once_R6",
            "derive_P_recombination_exterior_Schwarzschild_R7",
            "derive_P_coeff_action_stiffness_recombination_R10",
            "derive_covariant_recombination_lapse_shift_R1_R3",
        ],
        description=(
            "Covariant recombination cannot be derived until scalar accounting, "
            "exterior Schwarzschild preservation, and coefficient derivation gates are met."
        ),
    ))

    ns.record_derivation(
        derivation_id="recombination_without_double_counting_marker",
        inputs=[],
        output=sp.Symbol("recombination_without_double_counting_built"),
        method="recombination_without_double_counting_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
