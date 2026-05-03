# Candidate source decomposition ledger
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
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/11_field_equation_closure/
#   or:
#   scripts_v3/candidate_source_decomposition_ledger.py

from dataclasses import dataclass
from typing import List


def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_line(label: str, status: str, detail: str = "") -> None:
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
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class SourceEntry:
    source: str
    allowed_role: str
    forbidden_role: str
    sector: str
    status: str
    missing: str
    risk: str


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
    print()
    print("-" * 120)
    print(f"Source: {e.source}")
    print("-" * 120)
    print(f"Allowed role: {e.allowed_role}")
    print(f"Forbidden role: {e.forbidden_role}")
    print(f"Sector: {e.sector}")
    status_line(e.source, e.status)
    print(f"Missing: {e.missing}")
    print(f"Risk: {e.risk}")


def case_0_problem_statement():
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

    status_line("source decomposition problem posed", "CONSTRAINED")


def case_1_source_inventory(entries: List[SourceEntry]):
    header("Case 1: Source inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[SourceEntry]):
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

    status_line("compact source ledger produced", "STRUCTURAL")


def case_3_status_counts(entries: List[SourceEntry]):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    status_line("source status count produced", "STRUCTURAL")


def case_4_key_no_double_counting_rules():
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

    status_line("key source rules stated", "CONSTRAINED")


def case_5_source_role_hierarchy():
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

    status_line("source hierarchy stated", "CONSTRAINED")


def case_6_failure_controls():
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

    status_line("source decomposition failure controls stated", "RISK")


def case_7_next_tests():
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

    status_line("next test selected", "CONSTRAINED")


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


def main():
    header("Candidate Source Decomposition Ledger")
    case_0_problem_statement()
    entries = build_sources()
    case_1_source_inventory(entries)
    case_2_compact_table(entries)
    case_3_status_counts(entries)
    case_4_key_no_double_counting_rules()
    case_5_source_role_hierarchy()
    case_6_failure_controls()
    case_7_next_tests()
    final_interpretation()


if __name__ == "__main__":
    main()
