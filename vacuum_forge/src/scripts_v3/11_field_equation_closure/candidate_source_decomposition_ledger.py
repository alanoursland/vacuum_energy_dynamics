# Candidate source decomposition ledger
#
# Group:
#   11_field_equation_closure
#
# Script type:
#   INVENTORY
#
# Purpose
# -------
# The metric recombination map showed that recombination depends on a clean
# source split.
#
# This script makes a source ledger:
#
#   source object -> allowed sector(s) -> forbidden sector(s) -> status
#
# Goal:
#
#   prevent scalar double-counting,
#   prevent kappa from becoming a repair field,
#   prevent tensor/vector coefficients from being silently imported,
#   keep TT radiation separate from scalar trace response.
#
# This is an audit script, not a derivation.

from dataclasses import dataclass
from pathlib import Path
from typing import List

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
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
class SourceEntry:
    source: str
    allowed_role: str
    forbidden_role: str
    sector: str
    status: str
    missing: str
    risk: str


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="metric_recombination_map_marker",
        upstream_script_id="11_field_equation_closure__candidate_metric_recombination_map",
        upstream_derivation_id="metric_recombination_map_marker",
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


def build_sources() -> List[SourceEntry]:
    return [
        SourceEntry(
            source="rho",
            allowed_role="sources A-sector scalar monopole / areal flux",
            forbidden_role="must not also source an independent long-range kappa scalar",
            sector="A",
            status="DERIVED_REDUCED",
            missing="Full nonlinear nonspherical source identity.",
            risk="Double-counting scalar mass response.",
        ),
        SourceEntry(
            source="M_enc",
            allowed_role="sets exterior A flux normalization",
            forbidden_role="must not be altered by kappa boundary smoothing",
            sector="A exterior",
            status="DERIVED_REDUCED",
            missing="Parent flux identity beyond spherical reduction.",
            risk="Changing exterior mass by boundary/interface adjustment.",
        ),
        SourceEntry(
            source="j_i = rho v_i",
            allowed_role="matter current; decomposes into transverse and longitudinal parts",
            forbidden_role="must not source W_i through longitudinal/gauge part",
            sector="continuity source",
            status="CONSTRAINED",
            missing="Covariant current/source decomposition.",
            risk="Mixing scalar continuity with vector frame-dragging response.",
        ),
        SourceEntry(
            source="j_T = P_T j",
            allowed_role="sources transverse vector W_i",
            forbidden_role="must not feed scalar A except through consistency/continuity",
            sector="W_i",
            status="STRUCTURAL",
            missing="Boundary/global k=0 treatment and normalization.",
            risk="Frame-dragging coefficient imported from GR.",
        ),
        SourceEntry(
            source="j_L = P_L j",
            allowed_role="belongs to scalar continuity / density redistribution",
            forbidden_role="must not create transverse vector curl field",
            sector="A / continuity",
            status="DERIVED_REDUCED",
            missing="Full dynamic scalar-current closure.",
            risk="Vector/scalar source mixing.",
        ),
        SourceEntry(
            source="pressure p",
            allowed_role="may contribute to trace/minimum shift kappa_min",
            forbidden_role="must not source ordinary massless kappa Poisson tail or breathing wave",
            sector="kappa",
            status="CONSTRAINED",
            missing="S_trace_effective and chi_kappa.",
            risk="Exterior 1/r kappa leak or scalar radiation.",
        ),
        SourceEntry(
            source="stress trace T",
            allowed_role="may shift kappa_min / trace-volume relaxation",
            forbidden_role="must not duplicate A-sector rho source or TT radiation",
            sector="kappa",
            status="STRUCTURAL",
            missing="Gauge-invariant trace source law.",
            risk="Repair knob if trace role is not constrained.",
        ),
        SourceEntry(
            source="TT stress S_ij^TT",
            allowed_role="sources h_ij^TT tensor radiation",
            forbidden_role="must not be collapsed into scalar trace or kappa source",
            sector="h_ij^TT",
            status="STRUCTURAL",
            missing="TT source identity and coupling C_T.",
            risk="Tensor coupling matched rather than derived.",
        ),
        SourceEntry(
            source="quadrupole Q_ij^TT",
            allowed_role="far-zone tensor radiation shape",
            forbidden_role="must not imply scalar quadrupole radiation in A_rad/kappa",
            sector="h_ij^TT far zone",
            status="STRUCTURAL",
            missing="Vacuum ontology derivation of 2G/c^4 normalization.",
            risk="Using GR quadrupole formula as derivation.",
        ),
        SourceEntry(
            source="A_rad source",
            allowed_role="none as ordinary long-range scalar radiation",
            forbidden_role="forbidden unless separately derived, massive, constrained, or non-propagating",
            sector="scalar radiation hazard",
            status="REJECTED",
            missing="Parent mechanism proving absence/suppression.",
            risk="Breathing radiation contradicts scalar-radiation safety.",
        ),
        SourceEntry(
            source="Sigma_creation",
            allowed_role="special active-regime nonconservative source if separately invoked",
            forbidden_role="must not enter ordinary closed gravity field equations by default",
            sector="active regimes",
            status="RISK",
            missing="Regime conditions and conservation accounting.",
            risk="Nonconservative term breaks closure if used casually.",
        ),
        SourceEntry(
            source="Gamma_relax",
            allowed_role="relaxation toward vacuum minimum / kappa non-inertial equilibration",
            forbidden_role="must not destroy energy or damp A-sector mass field",
            sector="kappa / vacuum balance",
            status="STRUCTURAL",
            missing="Energy destination and parent balance law.",
            risk="Damping as cosmetic fix.",
        ),
    ]


def print_entry(e: SourceEntry) -> None:
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
    print(f"Source: {e.source}")
    print("-" * 120)
    print(f"Allowed role: {e.allowed_role}")
    print(f"Forbidden role: {e.forbidden_role}")
    print(f"Sector: {e.sector}")
    print(f"[{mark}] {e.source}: {e.status}")
    print(f"Missing: {e.missing}")
    print(f"Risk: {e.risk}")


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: Source decomposition ledger problem")

    print("Question:")
    print()
    print("  Which source feeds which field sector, and which source assignments are forbidden?")
    print()
    print("Goal:")
    print()
    print("  prevent double-counting and hidden GR import before stronger recombination claims")
    print()
    print("Discipline:")
    print()
    print("  rho -> A")
    print("  j_T -> W_i")
    print("  trace/pressure -> kappa_min, not scalar radiation")
    print("  TT stress/quadrupole -> h_ij^TT")
    print("  A_rad ordinary long-range scalar radiation -> rejected")

    with out.governance_assessments():
        out.line("source decomposition problem posed", StatusMark.DEFER, "structural constraint")


def case_1_source_inventory(entries: List[SourceEntry]):
    header("Case 1: Source inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[SourceEntry], out: ScriptOutput):
    header("Case 2: Compact source ledger")

    print("| Source | Allowed role | Forbidden role | Sector | Status |")
    print("|---|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.source.replace("|", "/")
            + " | "
            + e.allowed_role.replace("|", "/")
            + " | "
            + e.forbidden_role.replace("|", "/")
            + " | "
            + e.sector.replace("|", "/")
            + " | "
            + e.status
            + " |"
        )

    with out.governance_assessments():
        out.line("compact source ledger produced", StatusMark.PASS, "inventory marker")


def case_3_status_counts(entries: List[SourceEntry], out: ScriptOutput):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    with out.governance_assessments():
        out.line("source status count produced", StatusMark.PASS, "inventory marker")


def case_4_key_no_double_counting_rules(out: ScriptOutput):
    header("Case 4: Key no-double-counting rules")

    print("Rules:")
    print()
    print("1. rho is the A-sector scalar mass source.")
    print("2. kappa may respond to trace/pressure only as a local minimum shift.")
    print("3. kappa must not produce an exterior rho-like 1/r scalar field.")
    print("4. j_T sources W_i; j_L belongs to scalar continuity.")
    print("5. TT stress sources h_ij^TT; trace stress does not source TT radiation.")
    print("6. A_rad is not an ordinary active sector.")
    print("7. relaxation may transfer imbalance into vacuum configuration, but must not erase A.")

    with out.governance_assessments():
        out.line("key source rules stated", StatusMark.DEFER, "structural constraint")


def case_5_source_role_hierarchy(out: ScriptOutput):
    header("Case 5: Source role hierarchy")

    print("Hierarchy:")
    print()
    print("  conserved mass/energy density -> scalar constraint A")
    print("  transverse current -> vector response W_i")
    print("  trace-free quadrupole/shear -> tensor radiation h_ij^TT")
    print("  trace/pressure/volume imbalance -> constrained kappa_min shift")
    print("  scalar radiative residue -> rejected or non-propagating")
    print()
    print("This hierarchy keeps each source from doing too many jobs.")

    with out.governance_assessments():
        out.line("source hierarchy stated", StatusMark.DEFER, "structural constraint")


def case_6_failure_controls(out: ScriptOutput):
    header("Case 6: Failure controls")

    print("Source decomposition fails if:")
    print()
    print("1. rho sources both A and a long-range kappa field.")
    print("2. pressure trace creates a massless exterior kappa tail.")
    print("3. trace response becomes breathing radiation.")
    print("4. vector longitudinal current is treated as frame dragging.")
    print("5. TT stress coupling is matched while claimed derived.")
    print("6. Sigma_creation enters ordinary gravity closure without active-regime conditions.")
    print("7. Gamma_relax hides energy nonconservation.")
    print("8. source decomposition is chosen to imitate GR rather than forced by ontology.")

    with out.governance_assessments():
        out.line("source decomposition failure controls stated", StatusMark.WARN,
                 "open risk")


def case_7_next_tests(out: ScriptOutput):
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_source_decomposition_ledger.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_no_double_counting_constraints.py")
    print("   Turn source ledger into explicit algebraic/sector constraints.")
    print()
    print("3. candidate_constraint_vs_evolution_split.py")
    print("   Separate constrained fields from propagating fields.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_no_double_counting_constraints.py")
    print()
    print("Reason:")
    print("  The ledger identifies forbidden overlaps; the next check should formalize them.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.DEFER, "structural guidance")


def final_interpretation():
    header("Final interpretation")

    print("Current source decomposition:")
    print()
    print("  rho -> A")
    print("  j_T -> W_i")
    print("  trace/pressure -> kappa_min shift")
    print("  TT stress/quadrupole -> h_ij^TT")
    print("  A_rad ordinary long-range scalar source -> rejected")
    print()
    print("Main risk:")
    print("  any source doing two independent jobs without a parent identity.")
    print()
    print("Possible next artifact:")
    print("  candidate_source_decomposition_ledger.md")
    print()
    print("Possible next script:")
    print("  candidate_no_double_counting_constraints.py")


def record_governance(ns, entries: List[SourceEntry]) -> None:
    # DERIVED_REDUCED -> ClaimRecord HEURISTIC
    ns.record_claim(ClaimRecord(
        claim_id="src_rho_a_sector_derived_reduced",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.HEURISTIC,
        statement=(
            "rho sources the A-sector scalar monopole/areal flux. "
            "This is derived in the reduced static spherical case."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="src_j_L_scalar_continuity_derived_reduced",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.HEURISTIC,
        statement=(
            "The longitudinal current j_L = P_L j belongs to scalar continuity / "
            "density redistribution and must not create a transverse vector curl field."
        ),
    ))

    # STRUCTURAL -> ClaimRecord CANDIDATE_ROUTE
    ns.record_claim(ClaimRecord(
        claim_id="src_j_T_vector_structural",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "j_T = P_T j sources the transverse vector W_i. "
            "Boundary/global k=0 treatment and normalization are missing."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="src_TT_stress_tensor_structural",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "TT stress S_ij^TT sources h_ij^TT tensor radiation. "
            "TT source identity and coupling C_T are missing."
        ),
    ))

    # RISK -> ClaimRecord OPEN_RISK
    ns.record_claim(ClaimRecord(
        claim_id="src_sigma_creation_open_risk",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.OPEN_RISK,
        statement=(
            "Sigma_creation is a nonconservative active-regime term that must not "
            "enter ordinary closed gravity field equations by default."
        ),
    ))

    # Missing obligations
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_covariant_current_source_decomposition",
        script_id=SCRIPT_ID,
        title="Derive covariant current/source decomposition",
        status=ObligationStatus.OPEN,
        description=(
            "The split j = P_T j + P_L j with W_i sourced only by P_T j requires "
            "a covariant current decomposition proof or gauge-fixed reduced proof."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_TT_source_identity_and_coupling",
        script_id=SCRIPT_ID,
        title="Derive TT source identity and coupling C_T",
        status=ObligationStatus.OPEN,
        description=(
            "The tensor coupling C_T in Box h_ij^TT = -C_T S_ij^TT must be derived "
            "from vacuum ontology. It must not be imported from GR (2G/c^4 or 16*pi*G/c^4)."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_S_trace_effective_and_chi_kappa",
        script_id=SCRIPT_ID,
        title="Derive S_trace_effective and chi_kappa for pressure/trace kappa minimum",
        status=ObligationStatus.OPEN,
        description=(
            "The effective trace source S_trace_effective and coefficient chi_kappa "
            "that shift kappa_min must be derived. Pressure must not produce an "
            "exterior 1/r kappa tail or scalar radiation."
        ),
    ))

    # Inventory marker
    ns.record_derivation(
        derivation_id="source_decomposition_ledger_marker",
        inputs=[],
        output=sp.Symbol("source_decomposition_ledger_built"),
        method="source_decomposition_ledger_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )


def main():
    header("Candidate Source Decomposition Ledger")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    case_0_problem_statement(out)
    entries = build_sources()
    case_1_source_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_key_no_double_counting_rules(out)
    case_5_source_role_hierarchy(out)
    case_6_failure_controls(out)
    case_7_next_tests(out)
    final_interpretation()
    out.print_summary()
    with archive:
        record_governance(ns, entries)
        ns.write_run_metadata()


if __name__ == "__main__":
    main()
