# Candidate gauge-invariant diagnostics
#
# Purpose
# -------
# The recombination study showed that a schematic metric map exists, but it
# cannot be trusted until we know which diagnostics are invariant, gauge-fixed,
# gauge-aware, or unsafe.
#
# This script classifies current diagnostics:
#
#   R_areal
#   A with asymptotic normalization
#   AB / kappa_areal
#   h_ij^TT strain
#   W_i / frame-dragging observable
#   kappa interior response
#   A_rad scalar radiation hazard
#   curvature-like diagnostics
#
# Status categories:
#
#   SAFE_INVARIANT
#   SAFE_GAUGE_FIXED
#   GAUGE_AWARE
#   MISSING
#   RISK
#
# This is not a derivation of gauge invariants. It is an inventory of which
# diagnostics are safe and which require parent structure.
#
# Suggested location:
#   theory_v3/development/field_equation_candidates/08_covariant_parent_structure/
#   or:
#   scripts_v3/candidate_gauge_invariant_diagnostics.py

from dataclasses import dataclass
from typing import List


# =============================================================================
# Utilities
# =============================================================================

def header(title: str) -> None:
    print()
    print("=" * 120)
    print(title)
    print("=" * 120)


def status_line(label: str, status: str, detail: str = "") -> None:
    marks = {
        "SAFE_INVARIANT": "PASS",
        "SAFE_GAUGE_FIXED": "PASS",
        "GAUGE_AWARE": "WARN",
        "MISSING": "FAIL",
        "RISK": "WARN",
    }
    mark = marks.get(status, "INFO")
    if detail:
        print(f"[{mark}] {label}: {status} — {detail}")
    else:
        print(f"[{mark}] {label}: {status}")


@dataclass
class Diagnostic:
    name: str
    status: str
    use: str
    condition: str
    risk: str


def print_diag(d: Diagnostic) -> None:
    print()
    print("-" * 100)
    print(d.name)
    print("-" * 100)
    status_line(d.name, d.status)
    print(f"Use: {d.use}")
    print(f"Condition: {d.condition}")
    print(f"Risk: {d.risk}")


# =============================================================================
# Case 0: Problem statement
# =============================================================================

def case_0_problem_statement():
    header("Case 0: Gauge-invariant diagnostics problem")

    print("Problem:")
    print()
    print("  Recombination cannot be trusted unless diagnostics are classified.")
    print()
    print("Need to know which quantities are:")
    print()
    print("  invariant")
    print("  safe only after gauge fixing")
    print("  gauge-aware but not invariant")
    print("  missing")
    print("  risky")

    status_line("diagnostics problem posed", "SAFE_GAUGE_FIXED")


# =============================================================================
# Case 1: Build diagnostics
# =============================================================================

def build_diagnostics() -> List[Diagnostic]:
    return [
        Diagnostic(
            name="Areal radius R",
            status="SAFE_INVARIANT",
            use="Spherical reduction anchor; area of symmetry sphere is 4*pi*R^2.",
            condition="Valid in spherical/orbit-space reduction where symmetry spheres exist.",
            risk="Not available as a global scalar in arbitrary nonspherical geometries.",
        ),
        Diagnostic(
            name="Lapse A with asymptotic normalization",
            status="SAFE_GAUGE_FIXED",
            use="Static scalar potential / redshift diagnostic.",
            condition="Requires static slicing and normalization A -> 1 at infinity.",
            risk="Time reparameterization can change unnormalized lapse.",
        ),
        Diagnostic(
            name="AB or kappa_areal",
            status="GAUGE_AWARE",
            use="Areal-gauge compensation diagnostic; kappa = 1/2 ln(AB).",
            condition="Safe only after areal radius and static/diagonal form are specified.",
            risk="Can include coordinate artifacts outside its gauge-aware domain.",
        ),
        Diagnostic(
            name="Orbit-space gradient |grad R|^2",
            status="SAFE_GAUGE_FIXED",
            use="Gauge-aware spherical diagnostic replacing raw radial B.",
            condition="Requires orbit-space formulation and areal-radius scalar R.",
            risk="Still belongs to spherical reduction, not a full arbitrary-spacetime invariant by itself.",
        ),
        Diagnostic(
            name="TT strain h_ij^TT",
            status="SAFE_GAUGE_FIXED",
            use="Far-zone tensor radiation; plus/cross polarizations.",
            condition="Requires TT projection / far-zone wave gauge.",
            risk="Parent derivation of TT projection still needed.",
        ),
        Diagnostic(
            name="Frame-dragging observable from W_i",
            status="MISSING",
            use="Physical vector/current observable, e.g. rotation of local inertial frames.",
            condition="Need gauge-invariant curl/frame-dragging diagnostic.",
            risk="Raw W_i may be shift gauge rather than physical frame dragging.",
        ),
        Diagnostic(
            name="kappa interior response",
            status="GAUGE_AWARE",
            use="Trace/interior matter response diagnostic.",
            condition="Requires gauge-fixed or invariant definition of trace/volume response.",
            risk="May double-count coordinate volume changes.",
        ),
        Diagnostic(
            name="A_rad scalar radiation amplitude",
            status="RISK",
            use="Potential scalar breathing radiation diagnostic.",
            condition="Allowed only if explicitly controlled, suppressed, or observationally constrained.",
            risk="Unsuppressed A_rad creates forbidden extra scalar radiation.",
        ),
        Diagnostic(
            name="Curvature-like diagnostics",
            status="MISSING",
            use="Gauge-invariant parent-level observables.",
            condition="Need construction from parent metric/vacuum geometry.",
            risk="Without curvature-like diagnostics, comparisons may rely on gauge variables.",
        ),
        Diagnostic(
            name="Conserved flux/source identities",
            status="MISSING",
            use="Check source-geometry compatibility.",
            condition="Need Bianchi-like or continuity identities.",
            risk="Source couplings may be inconsistent across sectors.",
        ),
    ]


# =============================================================================
# Case 2: Print diagnostics
# =============================================================================

def case_2_print_diagnostics(diags: List[Diagnostic]):
    header("Case 2: Diagnostic inventory")

    for d in diags:
        print_diag(d)


# =============================================================================
# Case 3: Diagnostic table
# =============================================================================

def case_3_table(diags: List[Diagnostic]):
    header("Case 3: Diagnostic safety table")

    print("| Diagnostic | Status | Use |")
    print("|---|---|---|")
    for d in diags:
        print(f"| {d.name} | {d.status} | {d.use} |")

    status_line("diagnostic table produced", "GAUGE_AWARE",
                "several diagnostics remain gauge-aware or missing")


# =============================================================================
# Case 4: Status counts
# =============================================================================

def case_4_status_counts(diags: List[Diagnostic]):
    header("Case 4: Status counts")

    counts = {}
    for d in diags:
        counts[d.status] = counts.get(d.status, 0) + 1

    for status in ["SAFE_INVARIANT", "SAFE_GAUGE_FIXED", "GAUGE_AWARE", "MISSING", "RISK"]:
        print(f"{status}: {counts.get(status, 0)}")

    if counts.get("MISSING", 0) > 0 or counts.get("RISK", 0) > 0:
        status_line("diagnostic set incomplete", "MISSING",
                    "observable set and risky scalar radiation remain unresolved")
    else:
        status_line("diagnostic set complete", "SAFE_INVARIANT")


# =============================================================================
# Case 5: Safe comparison policy
# =============================================================================

def case_5_safe_comparison_policy():
    header("Case 5: Safe comparison policy")

    print("Use safely now:")
    print("  areal radius R in spherical reduction")
    print("  asymptotically normalized static A")
    print("  TT strain in TT/far-zone gauge")
    print()
    print("Use with gauge warnings:")
    print("  AB / kappa_areal")
    print("  kappa interior response")
    print("  orbit-space |grad R|^2 outside spherical context")
    print()
    print("Do not use as physical observable yet:")
    print("  raw W_i")
    print("  raw A_rad")
    print("  raw coordinate trace")
    print()
    status_line("safe comparison policy stated", "GAUGE_AWARE",
                "some diagnostics are safe only in reduced gauges")


# =============================================================================
# Case 6: Next study recommendation
# =============================================================================

def case_6_next_study():
    header("Case 6: Next study recommendation")

    print("Recommended next script:")
    print()
    print("  candidate_conservation_identity_requirements.py")
    print()
    print("Reason:")
    print("  Diagnostics expose another blocker: source-geometry compatibility.")
    print("  We need conservation/Bianchi-like identities so sector sources do not")
    print("  contradict one another.")
    print()
    print("Alternative:")
    print("  candidate_metric_parent_gap_summary.py")

    status_line("next study selected", "GAUGE_AWARE",
                "conservation identities are the next blocker")


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation(diags: List[Diagnostic]):
    header("Final interpretation")

    print("Some diagnostics are safe in reduced settings:")
    print()
    print("  areal radius R")
    print("  normalized static A")
    print("  TT strain")
    print()
    print("Several are gauge-aware or missing:")
    print()
    print("  AB/kappa_areal")
    print("  kappa response")
    print("  W_i frame-dragging observable")
    print("  curvature-like parent diagnostics")
    print("  conservation identities")
    print()
    print("Possible next artifact:")
    print("  candidate_gauge_invariant_diagnostics.md")
    print()
    print("Possible next script:")
    print("  candidate_conservation_identity_requirements.py")


def main():
    header("Candidate Gauge-Invariant Diagnostics")
    case_0_problem_statement()
    diags = build_diagnostics()
    case_2_print_diagnostics(diags)
    case_3_table(diags)
    case_4_status_counts(diags)
    case_5_safe_comparison_policy()
    case_6_next_study()
    final_interpretation(diags)


if __name__ == "__main__":
    main()
