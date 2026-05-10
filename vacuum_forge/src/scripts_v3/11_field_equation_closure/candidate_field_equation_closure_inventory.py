# Candidate field equation closure inventory
#
# Group:
#   11_field_equation_closure
#
# Script type:
#   INVENTORY
#
# Purpose
# -------
# Group 11 begins field-equation closure.
#
# The goal is not to add another mechanism.
# The goal is to make a ledger of the current field-equation system:
#
#   Sector | Field | Equation / rule | Source | Status | Missing
#
# This inventory incorporates group 10:
#
#   kappa is not an ordinary propagating scalar field.
#   kappa is best treated as a constrained non-inertial trace / volume
#   relaxation response.
#
# This script is an audit tool, not a derivation.

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
class SectorEntry:
    sector: str
    field: str
    equation_or_rule: str
    source: str
    status: str
    missing: str
    risk: str


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="kappa_near_boundary_deviation_diagnostic_marker",
        upstream_script_id="10_kappa_trace_response__candidate_kappa_near_boundary_deviation_diagnostic",
        upstream_derivation_id="kappa_near_boundary_deviation_diagnostic_marker",
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


def build_inventory() -> List[SectorEntry]:
    return [
        SectorEntry(
            sector="Scalar monopole / areal flux",
            field="A",
            equation_or_rule="Delta_areal A = 8*pi*G*rho/c^2",
            source="rho, M_enc",
            status="DERIVED_REDUCED",
            missing="Full nonlinear nonspherical parent equation.",
            risk="Overextending spherical reduced derivation.",
        ),
        SectorEntry(
            sector="Exterior reciprocal radial factor",
            field="B with kappa diagnostic",
            equation_or_rule="AB = exp(2*kappa); exterior kappa=0 -> B=1/A",
            source="Exterior vacuum / areal gauge condition",
            status="DERIVED_REDUCED",
            missing="Covariant/gauge-invariant parent interpretation of kappa.",
            risk="Treating gauge-conditioned relation as full physical derivation.",
        ),
        SectorEntry(
            sector="Weak scalar multipoles",
            field="A ~ 1 + 2 Phi/c^2",
            equation_or_rule="nabla^2 Phi = 4*pi*G*rho",
            source="rho",
            status="DERIVED_REDUCED",
            missing="Full nonlinear nonspherical closure.",
            risk="Assuming weak multipole success implies complete scalar sector.",
        ),
        SectorEntry(
            sector="Scalar radiation hazard",
            field="A_rad",
            equation_or_rule="ordinary massless scalar wave rejected / projected / suppressed",
            source="Forbidden scalar radiative deviation",
            status="CONSTRAINED",
            missing="Parent mechanism separating static scalar constraint from scalar radiation.",
            risk="Unwanted breathing radiation.",
        ),
        SectorEntry(
            sector="Vector current / frame dragging",
            field="W_i",
            equation_or_rule="curl curl W = -(alpha_W/(2K_c)) j_T; div W=0 -> Delta W = (alpha_W/(2K_c)) j_T",
            source="j_T = P_T(rho v)",
            status="STRUCTURAL",
            missing="alpha_W/K_c, observable coupling beta_W, global boundary normalization.",
            risk="Frame-dragging normalization remains matched or arbitrary.",
        ),
        SectorEntry(
            sector="Vector observable",
            field="B_W = curl W",
            equation_or_rule="Omega_drag = beta_W B_W; far-field B_W ~ J/r^3",
            source="Angular momentum J = integral r x j d^3x",
            status="DERIVED_REDUCED",
            missing="beta_W and absolute normalization.",
            risk="Shape success without coefficient derivation.",
        ),
        SectorEntry(
            sector="Tensor radiation",
            field="h_ij^TT",
            equation_or_rule="Box h_ij^TT = -C_T S_ij^TT",
            source="TT stress / quadrupole source",
            status="STRUCTURAL",
            missing="C_T, source identity, vacuum tensor stiffness.",
            risk="Importing 2G/c^4 or 16*pi*G/c^4 by matching.",
        ),
        SectorEntry(
            sector="Tensor radiation energy",
            field="h_ij^TT energy flux",
            equation_or_rule="F_T ~ K_T <dot h_ij^TT dot h_ij^TT>",
            source="TT wave strain",
            status="MATCHED",
            missing="K_T from vacuum action/stiffness.",
            risk="Energy flux copied from GR rather than derived.",
        ),
        SectorEntry(
            sector="Kappa trace / volume relaxation",
            field="kappa",
            equation_or_rule="dot kappa = -mu_kappa K_kappa (kappa-kappa_min)",
            source="kappa_min = chi_kappa S_trace_effective",
            status="STRUCTURAL",
            missing="K_kappa, mu_kappa, chi_kappa, S_trace_effective, covariant origin.",
            risk="Becoming a repair knob or hidden scalar wave.",
        ),
        SectorEntry(
            sector="Kappa exterior suppression",
            field="kappa boundary/exterior",
            equation_or_rule="kappa -> 0, kappa_min -> 0, F_kappa(R+) = 0",
            source="Vacuum minimum / boundary projection",
            status="CONSTRAINED",
            missing="Physical interface law and parent projection identity.",
            risk="Hand-imposed exterior suppression.",
        ),
        SectorEntry(
            sector="Kappa near-boundary joint minimum",
            field="f_joint or kappa_min profile",
            equation_or_rule="lambda_2 fourth_derivative(f) - lambda_1 second_derivative(f) + (W_i+W_e)f = W_i f_int + W_e f_ext",
            source="Interior quadratic tendency + exterior reciprocal tendency + smoothness energy",
            status="STRUCTURAL",
            missing="Weights, transition width sigma, variable identification, observable map.",
            risk="Curve-fitting or unquantified near-boundary deviation.",
        ),
        SectorEntry(
            sector="Vacuum-substance balance",
            field="q_v, J_v",
            equation_or_rule="partial_t q_v + div J_v = Sigma_exchange + Sigma_creation - Gamma_relax",
            source="Ontology-native vacuum exchange / creation / relaxation",
            status="UNFINISHED",
            missing="Definitions, conservation identity, Bianchi-compatible closure.",
            risk="Decorative ontology if it does not force equations.",
        ),
        SectorEntry(
            sector="Metric recombination",
            field="g_tt, g_ti, g_ij",
            equation_or_rule="g_tt ~ -A c^2; g_ti ~ W_i; g_ij ~ scalar/kappa + h_ij^TT",
            source="Sector recombination",
            status="UNFINISHED",
            missing="Covariant parent map and no-double-counting rules.",
            risk="Silently importing GR metric form.",
        ),
    ]


def print_entry(e: SectorEntry) -> None:
    marks = {
        "DERIVED": "PASS",
        "DERIVED_REDUCED": "PASS",
        "STRUCTURAL": "WARN",
        "CONSTRAINED": "WARN",
        "MATCHED": "WARN",
        "MISSING": "FAIL",
        "RISK": "WARN",
        "REJECTED": "WARN",
        "UNFINISHED": "FAIL",
    }
    mark = marks.get(e.status, "INFO")
    print()
    print("-" * 120)
    print(f"Sector: {e.sector}")
    print("-" * 120)
    print(f"Field: {e.field}")
    print(f"Equation / rule: {e.equation_or_rule}")
    print(f"Source: {e.source}")
    print(f"[{mark}] {e.sector}: {e.status}")
    print(f"Missing: {e.missing}")
    print(f"Risk: {e.risk}")


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: Field equation closure inventory problem")

    print("Question:")
    print()
    print("  What is the current field-equation system, sector by sector?")
    print()
    print("Goal:")
    print()
    print("  make a ledger of equations, source roles, status labels, missing pieces, and risks")
    print()
    print("Discipline:")
    print()
    print("  do not add new mechanisms")
    print("  do not hide matched coefficients")
    print("  do not let kappa become a repair field")
    print("  mark unfinished closure explicitly")

    with out.governance_assessments():
        out.line("closure inventory problem posed", StatusMark.DEFER, "structural constraint on inventory scope")


def case_1_inventory(entries: List[SectorEntry]):
    header("Case 1: Field equation inventory")
    for entry in entries:
        print_entry(entry)


def case_2_markdown_table(entries: List[SectorEntry], out: ScriptOutput):
    header("Case 2: Compact markdown ledger")

    print("| Sector | Field | Equation / rule | Source | Status | Missing |")
    print("|---|---|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.sector.replace("|", "/")
            + " | "
            + e.field.replace("|", "/")
            + " | "
            + e.equation_or_rule.replace("|", "/")
            + " | "
            + e.source.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.missing.replace("|", "/")
            + " |"
        )

    with out.governance_assessments():
        out.line("compact ledger produced", StatusMark.PASS, "inventory marker")


def case_3_status_counts(entries: List[SectorEntry], out: ScriptOutput):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  The system has strong reduced scalar results, structural vector/tensor/kappa sectors,")
    print("  and unfinished covariant closure.")

    with out.governance_assessments():
        out.line("status count produced", StatusMark.PASS, "inventory marker")


def case_4_strongest_and_weakest(out: ScriptOutput):
    header("Case 4: Strongest and weakest sectors")

    print("Strongest sector:")
    print()
    print("  A-sector static spherical exterior.")
    print("  It reconstructs A=1-2GM/(c^2 r) and B=1/A in the reduced exterior.")
    print()
    print("Most dangerous unfinished sectors:")
    print()
    print("  tensor coupling normalization")
    print("  vector observable normalization")
    print("  kappa covariant/source identity")
    print("  metric recombination map")
    print("  parent conservation/Bianchi-like closure")

    with out.governance_assessments():
        out.line("strong/weak sector audit stated", StatusMark.DEFER, "structural assessment")


def case_5_no_double_counting_first_rules(out: ScriptOutput):
    header("Case 5: Initial no-double-counting rules")

    print("Initial rules:")
    print()
    print("1. rho sources A, not an independent long-range kappa scalar.")
    print("2. pressure/trace may shift kappa_min, but must not create scalar radiation.")
    print("3. j_T sources W_i; longitudinal current belongs to scalar continuity.")
    print("4. TT stress/quadrupole sources h_ij^TT.")
    print("5. kappa boundary smoothing must not alter A-sector mass flux by hand.")
    print("6. recombination must not count the same trace response in both kappa and h_ij^TT.")

    with out.governance_assessments():
        out.line("initial no-double-counting rules stated", StatusMark.DEFER, "structural constraint")


def case_6_next_tests(out: ScriptOutput):
    header("Case 6: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_field_equation_closure_inventory.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_metric_recombination_map.py")
    print("   State how A, W_i, h_ij^TT, and kappa recombine into a metric-like object.")
    print()
    print("3. candidate_source_decomposition_ledger.py")
    print("   Separate rho, j_T, trace, and TT stress source roles.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_metric_recombination_map.py")
    print()
    print("Reason:")
    print("  Once the inventory is explicit, recombination is the next place errors can hide.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.DEFER, "structural guidance")


def final_interpretation():
    header("Final interpretation")

    print("Current field-equation closure status:")
    print()
    print("  A-sector is genuinely reconstructed in the reduced exterior.")
    print("  W_i sector has structural source/projection/shape but missing normalization.")
    print("  h_ij^TT sector has correct structural radiation role but missing coupling derivation.")
    print("  kappa is now constrained as non-inertial trace relaxation, not scalar radiation.")
    print("  parent conservation/covariant closure remains missing.")
    print()
    print("Possible next artifact:")
    print("  candidate_field_equation_closure_inventory.md")
    print()
    print("Possible next script:")
    print("  candidate_metric_recombination_map.py")


def record_governance(ns, entries: List[SectorEntry]) -> None:
    # DERIVED_REDUCED entries -> ClaimRecord HEURISTIC (inventory claim, not a theorem)
    ns.record_claim(ClaimRecord(
        claim_id="inv_a_sector_derived_reduced",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.HEURISTIC,
        statement=(
            "The A-sector scalar monopole equation Delta_areal A = 8*pi*G*rho/c^2 "
            "is derived in the reduced static spherical exterior."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="inv_b_kappa_exterior_derived_reduced",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.HEURISTIC,
        statement=(
            "The exterior relation AB = exp(2*kappa) with kappa=0 giving B=1/A "
            "is derived in the reduced areal-gauge exterior."
        ),
    ))

    # STRUCTURAL entries -> ClaimRecord CANDIDATE_ROUTE
    ns.record_claim(ClaimRecord(
        claim_id="inv_vector_sector_structural",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "The vector current sector curl curl W = -(alpha_W/(2K_c)) j_T has structural "
            "source/projection/shape support but normalization is not derived."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="inv_tensor_radiation_structural",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "The tensor radiation sector Box h_ij^TT = -C_T S_ij^TT has correct structural "
            "TT radiation role but coupling coefficient C_T is not derived."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="inv_kappa_relaxation_structural",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "Kappa is treated as a non-inertial trace relaxation variable "
            "dot(kappa) = -mu_kappa K_kappa (kappa-kappa_min). "
            "Source coefficients and covariant origin are not yet derived."
        ),
    ))

    # MATCHED entry -> ClaimRecord PROVISIONAL_CONVENTION + obligation for coefficient origin
    ns.record_claim(ClaimRecord(
        claim_id="inv_tensor_energy_flux_matched",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.PROVISIONAL_CONVENTION,
        statement=(
            "Tensor radiation energy flux F_T ~ K_T <dot h_ij^TT dot h_ij^TT> "
            "has the correct structural form. K_T is matched to GR, not yet derived."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_K_T_tensor_energy_flux_coefficient",
        script_id=SCRIPT_ID,
        title="Derive tensor energy flux coefficient K_T",
        status=ObligationStatus.OPEN,
        description=(
            "K_T must be derived from vacuum action stiffness or tensor ontology. "
            "It must not be imported from GR radiation formula."
        ),
    ))

    # MISSING / UNFINISHED entries -> ProofObligationRecord
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_vacuum_substance_balance_closure",
        script_id=SCRIPT_ID,
        title="Derive vacuum-substance balance closure",
        status=ObligationStatus.OPEN,
        description=(
            "The vacuum balance partial_t q_v + div J_v = Sigma_exchange + Sigma_creation - Gamma_relax "
            "requires definitions, a conservation identity, and Bianchi-compatible closure."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_metric_recombination_covariant_map",
        script_id=SCRIPT_ID,
        title="Derive covariant metric recombination map",
        status=ObligationStatus.OPEN,
        description=(
            "The metric recombination g_tt ~ -A c^2, g_ti ~ W_i, g_ij ~ scalar/kappa + h_ij^TT "
            "is currently a bookkeeping ansatz. A covariant parent map with no-double-counting "
            "rules must be derived."
        ),
    ))

    # CONSTRAINED entries -> ClaimRecord CANDIDATE_ROUTE
    ns.record_claim(ClaimRecord(
        claim_id="inv_scalar_radiation_constrained",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "Ordinary massless scalar wave radiation is rejected/projected/suppressed "
            "as a structural constraint. Parent mechanism separating static scalar "
            "constraint from scalar radiation is missing."
        ),
    ))

    # RISK entries -> ClaimRecord OPEN_RISK
    ns.record_claim(ClaimRecord(
        claim_id="inv_alpha_W_normalization_risk",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.OPEN_RISK,
        statement=(
            "Frame-dragging normalization alpha_W/K_c, observable coupling beta_W, "
            "and global boundary normalization remain matched or arbitrary."
        ),
    ))

    # Inventory marker
    ns.record_derivation(
        derivation_id="field_equation_closure_inventory_marker",
        inputs=[],
        output=sp.Symbol("field_equation_closure_inventory_built"),
        method="field_equation_closure_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )


def main():
    header("Candidate Field Equation Closure Inventory")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    case_0_problem_statement(out)
    entries = build_inventory()
    case_1_inventory(entries)
    case_2_markdown_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_strongest_and_weakest(out)
    case_5_no_double_counting_first_rules(out)
    case_6_next_tests(out)
    final_interpretation()
    record_governance(ns, entries)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
