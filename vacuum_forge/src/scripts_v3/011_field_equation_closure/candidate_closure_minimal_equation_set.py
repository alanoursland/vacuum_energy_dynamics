# Candidate closure minimal equation set
#
# Group:
#   11_field_equation_closure
#
# Script type:
#   SUMMARY
#
# Purpose
# -------
# The failure-mode audit identified how closure can fail.
#
# The next step is constructive but cautious:
#
#   assemble the current minimal equation set,
#   with every piece labeled.
#
# This script presents the smallest current field-equation set that reflects
# the project honestly:
#
#   A scalar constraint
#   B/kappa reduced relation
#   W_i transverse vector response
#   h_ij^TT tensor radiation
#   kappa non-inertial trace relaxation
#   scalar-radiation rejection
#   source no-double-counting constraints
#   closure status
#
# This is not a final theory.
# It is a current-status equation set.

from dataclasses import dataclass
from pathlib import Path
from typing import List

import sympy as sp

from vacuumforge import ProjectArchive, Status, TheoryContext
from vacuumforge.metric.concrete_check import check_concrete_metric
from vacuumforge.governance import (
    ClaimRecord,
    ClaimTier,
    GovernanceStatus,
    HandoffImportRecord,
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


@dataclass
class EquationEntry:
    name: str
    equation: str
    role: str
    source: str
    status: str
    missing: str
    caveat: str


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="field_equation_closure_failure_modes_marker",
        upstream_script_id="011_field_equation_closure__candidate_field_equation_closure_failure_modes",
        upstream_derivation_id="field_equation_closure_failure_modes_marker",
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


def build_equations() -> List[EquationEntry]:
    return [
        EquationEntry(
            name="E1: A-sector scalar constraint",
            equation="Delta_areal A = 8*pi*G*rho/c^2",
            role="scalar monopole / mass flux constraint",
            source="rho, M_enc",
            status="DERIVED_REDUCED",
            missing="full nonlinear nonspherical parent equation",
            caveat="valid strongest in static spherical/reduced scalar sector",
        ),
        EquationEntry(
            name="E2: exterior A solution",
            equation="A(r) = 1 - 2*G*M/(c^2*r)",
            role="static spherical exterior scalar factor",
            source="M = integral rho dV",
            status="DERIVED_REDUCED",
            missing="general exterior/nonspherical nonlinear form",
            caveat="main real reconstruction result",
        ),
        EquationEntry(
            name="E3: B/kappa areal relation",
            equation="A*B = exp(2*kappa); exterior kappa=0 -> B=1/A",
            role="radial reciprocal companion / kappa diagnostic",
            source="exterior vacuum target kappa=0",
            status="DERIVED_REDUCED",
            missing="covariant gauge/physical split",
            caveat="reduced areal-gauge relation, not full parent metric",
        ),
        EquationEntry(
            name="E4: weak scalar multipole limit",
            equation="A ~= 1 + 2*Phi/c^2; nabla^2 Phi = 4*pi*G*rho",
            role="weak scalar/Newtonian limit",
            source="rho",
            status="DERIVED_REDUCED",
            missing="full nonlinear nonspherical closure",
            caveat="supports weak multipoles and reduced gamma=1, not full PPN audit",
        ),
        EquationEntry(
            name="E5: vector current response",
            equation="curl curl W = -(alpha_W/(2*K_c))*j_T; div W=0",
            role="transverse vector / frame-dragging shape",
            source="j_T = P_T(rho*v)",
            status="STRUCTURAL",
            missing="alpha_W/K_c, beta_W, normalization",
            caveat="far-field shape/J dependence supported; coefficient not derived",
        ),
        EquationEntry(
            name="E6: tensor radiation equation",
            equation="Box h_ij^TT = -C_T*S_ij^TT",
            role="ordinary long-range gravitational radiation",
            source="TT stress / quadrupole source",
            status="STRUCTURAL",
            missing="C_T, TT source identity, tensor action stiffness",
            caveat="TT role structural; coupling coefficient not derived",
        ),
        EquationEntry(
            name="E7: tensor radiation energy flux",
            equation="F_T ~ K_T <dot(h_ij^TT) dot(h_ij^TT)>",
            role="tensor radiation energy accounting",
            source="TT wave strain",
            status="MATCHED",
            missing="K_T from vacuum action/stiffness",
            caveat="absolute GR flux coefficient not derived",
        ),
        EquationEntry(
            name="E8: kappa non-inertial relaxation",
            equation="dot(kappa) = -mu_kappa*K_kappa*(kappa-kappa_min)",
            role="trace / vacuum-volume relaxation",
            source="kappa_min = chi_kappa*S_trace_effective",
            status="STRUCTURAL",
            missing="K_kappa, mu_kappa, chi_kappa, S_trace_effective, covariant origin",
            caveat="not a wave equation; no independent momentum channel",
        ),
        EquationEntry(
            name="E9: exterior kappa safety",
            equation="kappa -> 0; kappa_min -> 0; F_kappa(R+) = 0",
            role="no exterior scalar/kappa charge",
            source="vacuum minimum / boundary projection",
            status="CONSTRAINED",
            missing="boundary/interface theorem",
            caveat="required to avoid scalar tail and mass tuning",
        ),
        EquationEntry(
            name="E10: scalar radiation rejection",
            equation="source(A_rad ordinary massless) = 0; Box kappa ordinary scalar rejected",
            role="TT-only ordinary radiation safety",
            source="scalar-radiation hazard",
            status="REJECTED",
            missing="parent mechanism proving exclusion",
            caveat="constraint, not yet derivation",
        ),
        EquationEntry(
            name="E11: ordinary closed regime",
            equation="Sigma_creation = 0",
            role="ordinary conservative closure",
            source="active-regime exclusion",
            status="CONSTRAINED",
            missing="active-regime trigger/exclusion law",
            caveat="creation/exchange regimes not part of ordinary gravity closure by default",
        ),
        EquationEntry(
            name="E12: parent closure target",
            equation="Div E_parent[A,W,h_TT,kappa] = B_closed[T] + B_relax[Gamma_relax]",
            role="candidate parent identity target",
            source="source balance / vacuum exchange",
            status="MISSING",
            missing="E_parent, B_closed, B_relax definitions and proof",
            caveat="template only; not closure",
        ),
    ]


def print_equation(e: EquationEntry) -> None:
    marks = {
        "DERIVED": "PASS",
        "DERIVED_REDUCED": "PASS",
        "STRUCTURAL": "WARN",
        "CONSTRAINED": "WARN",
        "MATCHED": "WARN",
        "MISSING": "FAIL",
        "REJECTED": "WARN",
        "UNFINISHED": "FAIL",
        "RISK": "WARN",
    }
    mark = marks.get(e.status, "INFO")
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Equation: {e.equation}")
    print(f"Role: {e.role}")
    print(f"Source: {e.source}")
    print(f"[{mark}] {e.name}: {e.status}")
    print(f"Missing: {e.missing}")
    print(f"Caveat: {e.caveat}")


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: Minimal closure equation set problem")

    print("Question:")
    print()
    print("  What is the smallest honest current field-equation set?")
    print()
    print("Goal:")
    print()
    print("  assemble the current equations with labels and caveats")
    print()
    print("Discipline:")
    print()
    print("  do not hide matched coefficients")
    print("  do not claim closure")
    print("  keep kappa non-radiative")
    print("  keep parent identity marked missing")

    with out.governance_assessments():
        out.line("minimal equation set problem posed", StatusMark.DEFER,
                 "structural constraint on scope")


def case_1_equation_inventory(entries: List[EquationEntry]):
    header("Case 1: Minimal equation inventory")
    for entry in entries:
        print_equation(entry)


def case_2_compact_table(entries: List[EquationEntry], out: ScriptOutput):
    header("Case 2: Compact minimal equation table")

    print("| Equation | Role | Status | Missing |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.role.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.missing.replace("|", "/")
            + " |"
        )

    with out.governance_assessments():
        out.line("compact minimal equation table produced", StatusMark.PASS, "inventory marker")


def case_3_status_counts(entries: List[EquationEntry], out: ScriptOutput):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  The minimal set has strong reduced scalar equations, structural vector/tensor/kappa rules,")
    print("  constrained scalar-radiation safety, one matched tensor energy coefficient, and missing parent closure.")

    with out.governance_assessments():
        out.line("minimal equation status count produced", StatusMark.PASS, "inventory marker")


def case_4_minimal_reduced_system(out: ScriptOutput):
    header("Case 4: Minimal reduced system")

    print("Minimal current reduced system:")
    print()
    print("  Delta_areal A = 8*pi*G*rho/c^2")
    print("  A_ext = 1 - 2*G*M/(c^2*r)")
    print("  A*B = exp(2*kappa), exterior kappa=0 -> B=1/A")
    print("  curl curl W = -(alpha_W/(2*K_c))*j_T")
    print("  Box h_TT = -C_T*S_TT")
    print("  dot(kappa) = -mu_kappa*K_kappa*(kappa-kappa_min)")
    print("  kappa_min = chi_kappa*S_trace_effective")
    print("  source(A_rad ordinary massless) = 0")
    print("  Sigma_creation = 0 in ordinary closed regime")
    print()
    print("Parent closure target:")
    print()
    print("  Div E_parent = B_closed + B_relax")

    with out.governance_assessments():
        out.line("minimal reduced system stated", StatusMark.DEFER, "structural constraint")


def case_5_gr_recovery_status(out: ScriptOutput):
    header("Case 5: GR recovery status")

    print("Recovered strongly/reduced:")
    print("  static spherical exterior A")
    print("  B=1/A once exterior kappa=0")
    print("  weak scalar/Newtonian limit")
    print()
    print("Supported structurally:")
    print("  vector frame-dragging shape")
    print("  TT tensor radiation sector")
    print("  kappa non-radiative trace relaxation")
    print()
    print("Matched or missing:")
    print("  vector normalization")
    print("  tensor coupling")
    print("  tensor energy flux coefficient")
    print("  parent conservation identity")
    print("  covariant recombination")

    with out.governance_assessments():
        out.line("GR recovery status restated", StatusMark.DEFER, "structural assessment")


def case_5b_vf_minimal_metric_crosscheck(ns, out: ScriptOutput):
    header("Case 5b: VacuumForge minimal metric cross-check")

    ctx = TheoryContext("candidate_closure_minimal_equation_set")
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
            "minimal equation set reproduces reciprocal concrete metric classification",
            StatusMark.PASS if ok else StatusMark.FAIL,
            f"A*B = {product}; ConcreteMetricCheck: {result.status}",
        )

    ns.record_derivation(
        derivation_id="closure_minimal_reciprocal_metric_crosscheck",
        inputs=[A_value, B_value],
        output=product,
        method="ConcreteMetricCheck reciprocal_scaling",
        status=Status.DERIVED,
        record_kind=RecordKind.COMPATIBILITY_EXAMPLE,
    )


def case_6_failure_controls(out: ScriptOutput):
    header("Case 6: Failure controls")

    print("This minimal set fails if:")
    print()
    print("1. Parent closure target is advertised as derived.")
    print("2. Tensor/vector coefficients are advertised as derived.")
    print("3. Kappa becomes a second scalar gravity field.")
    print("4. Boundary smoothing changes exterior M.")
    print("5. A_rad or Box kappa scalar radiation appears.")
    print("6. Sigma_creation enters ordinary closed regime.")
    print("7. Recombination silently copies GR.")

    with out.governance_assessments():
        out.line("minimal set failure controls stated", StatusMark.WARN, "open risk")


def case_7_next_tests(out: ScriptOutput):
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_closure_minimal_equation_set.md")
    print("   Artifact for this script.")
    print()
    print("2. field_equation_closure_summary.md")
    print("   Summarize group 11.")
    print()
    print("3. candidate_parent_identity_reduced_implications.py")
    print("   Test reduced implications of the parent identity template.")
    print()
    print("Recommended next:")
    print()
    print("  field_equation_closure_summary.md")
    print()
    print("Reason:")
    print("  Group 11 has reached a natural summary point after inventory, recombination, sources, constraints,")
    print("  evolution split, GR audit, parent scaffold, failure modes, and minimal equation set.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.DEFER, "structural guidance")


def final_interpretation():
    header("Final interpretation")

    print("The current minimal equation set is coherent enough to state.")
    print()
    print("It is not closed.")
    print()
    print("Strongest result:")
    print("  reduced Schwarzschild exterior from A-sector")
    print()
    print("Main missing result:")
    print("  parent conservation/recombination identity")
    print()
    print("Possible next artifact:")
    print("  candidate_closure_minimal_equation_set.md")
    print()
    print("Recommended next:")
    print("  field_equation_closure_summary.md")


def record_governance(ns, entries: List[EquationEntry]) -> None:
    # DERIVED_REDUCED equations -> HEURISTIC claims
    ns.record_claim(ClaimRecord(
        claim_id="min_E1_A_sector_scalar_constraint",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.HEURISTIC,
        statement=(
            "E1: Delta_areal A = 8*pi*G*rho/c^2 is derived in the reduced static spherical "
            "scalar sector. Full nonlinear nonspherical parent equation is missing."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="min_E2_exterior_A_solution",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.HEURISTIC,
        statement=(
            "E2: A(r) = 1 - 2*G*M/(c^2*r) is the main real reconstruction result. "
            "Valid in static spherical/reduced scalar sector only."
        ),
    ))

    # STRUCTURAL equations -> CANDIDATE_ROUTE claims
    ns.record_claim(ClaimRecord(
        claim_id="min_E5_vector_current_response",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "E5: curl curl W = -(alpha_W/(2*K_c))*j_T has structural source/shape support. "
            "alpha_W/K_c, beta_W, and normalization are not derived."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="min_E6_tensor_radiation_equation",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "E6: Box h_ij^TT = -C_T*S_ij^TT has structural TT radiation support. "
            "C_T, TT source identity, and tensor action stiffness are not derived."
        ),
    ))

    # MATCHED equation -> PROVISIONAL_CONVENTION + obligation
    ns.record_claim(ClaimRecord(
        claim_id="min_E7_tensor_energy_flux_matched",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.PROVISIONAL_CONVENTION,
        statement=(
            "E7: F_T ~ K_T <dot h_ij^TT dot h_ij^TT> has correct structural form. "
            "K_T is matched to GR; absolute flux coefficient is not derived."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_K_T_from_vacuum_action_stiffness",
        script_id=SCRIPT_ID,
        title="Derive K_T tensor energy flux coefficient from vacuum action stiffness",
        status=ObligationStatus.OPEN,
        description=(
            "K_T in F_T ~ K_T <dot h_TT^2> must be derived from vacuum tensor ontology. "
            "GR radiation formula must not be copied."
        ),
    ))

    # MISSING equation -> OPEN obligation
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_E12_parent_closure_identity",
        script_id=SCRIPT_ID,
        title="Derive E12: parent closure identity Div E_parent = B_closed + B_relax",
        status=ObligationStatus.OPEN,
        description=(
            "E12 is the main missing result. E_parent, B_closed, and B_relax must be "
            "defined and derived from vacuum ontology. This identity must imply A constraint "
            "propagation, W_i sourcing, h_TT radiation, kappa trace relaxation, exterior mass "
            "preservation, and ordinary Sigma_creation = 0."
        ),
    ))

    # Summary claim for Group 11 closure status
    ns.record_claim(ClaimRecord(
        claim_id="group_11_closure_not_complete",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.SUMMARY_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        statement=(
            "Group 11 does not license closure of the field-equation system. "
            "The minimal equation set is coherent and the A-sector is genuinely reduced-derived, "
            "but the parent conservation/recombination identity (E12) remains missing. "
            "Vector and tensor coefficients remain matched. Covariant recombination is unfinished."
        ),
        obligation_ids=[
            "derive_E12_parent_closure_identity",
            "derive_K_T_from_vacuum_action_stiffness",
            "derive_alpha_W_K_c_and_beta_W",
            "derive_C_T_tensor_coupling_from_stiffness",
        ],
        source_claim_ids=[
            "min_E1_A_sector_scalar_constraint",
            "min_E5_vector_current_response",
            "min_E6_tensor_radiation_equation",
            "min_E7_tensor_energy_flux_matched",
        ],
    ))

    # HandoffImportRecord - what Group 12 may import from Group 11
    ns.record_handoff_import(HandoffImportRecord(
        handoff_id="group_11_field_equation_closure_handoff",
        script_id=SCRIPT_ID,
        imported_as=RecordKind.SUMMARY_CLAIM,
        status=GovernanceStatus.DEFERRED_PENDING_PREREQUISITES,
        imported_record_refs=[
            # Derived results
            "claim:inv_a_sector_derived_reduced",
            "claim:gr_static_spherical_exterior_A",
            "claim:gr_exterior_B_reciprocal",
            "claim:min_E1_A_sector_scalar_constraint",
            "claim:min_E2_exterior_A_solution",
            # Provisional conventions (matched, not derived)
            "claim:gr_frame_dragging_normalization_matched",
            "claim:gr_tensor_coupling_matched",
            "claim:gr_quadrupole_radiation_power_matched",
            "claim:min_E7_tensor_energy_flux_matched",
            # Structural candidate routes
            "claim:dyn_h_TT_true_propagating",
            "claim:dyn_kappa_non_inertial_relaxation",
            "claim:dyn_TT_only_radiation_rule",
            # Open obligations that must not be silently inherited as satisfied
            "obligation:derive_E12_parent_closure_identity",
            "obligation:derive_K_T_from_vacuum_action_stiffness",
            "obligation:derive_alpha_W_K_c_and_beta_W",
            "obligation:derive_C_T_tensor_coupling_from_stiffness",
            "obligation:derive_I10_bianchi_like_closure",
            "obligation:derive_covariant_metric_recombination_parent_map",
            # Summary claim
            "claim:group_11_closure_not_complete",
        ],
        description=(
            "What Group 12 or downstream groups may import from Group 11. "
            "Derived results: reduced A-sector exterior (A=1-2GM/c^2r, B=1/A, weak limit). "
            "Provisional conventions (matched, not derived): vector normalization, tensor coupling, "
            "tensor flux coefficient. "
            "Structural candidate routes: TT radiation sector, kappa non-inertial relaxation, "
            "TT-only radiation rule. "
            "Open obligations (must not be treated as satisfied): parent closure identity (E12), "
            "tensor flux coefficient K_T, vector coefficients alpha_W/K_c and beta_W, "
            "tensor coupling C_T, Bianchi-like closure, covariant recombination map. "
            "Group summary: field-equation closure is not yet licensed."
        ),
    ))

    # Inventory marker
    ns.record_derivation(
        derivation_id="closure_minimal_equation_set_marker",
        inputs=[],
        output=sp.Symbol("closure_minimal_equation_set_stated"),
        method="closure_minimal_equation_set_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )


def main():
    header("Candidate Closure Minimal Equation Set")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    case_0_problem_statement(out)
    entries = build_equations()
    case_1_equation_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_minimal_reduced_system(out)
    case_5_gr_recovery_status(out)
    case_5b_vf_minimal_metric_crosscheck(ns, out)
    case_6_failure_controls(out)
    case_7_next_tests(out)
    final_interpretation()
    record_governance(ns, entries)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
