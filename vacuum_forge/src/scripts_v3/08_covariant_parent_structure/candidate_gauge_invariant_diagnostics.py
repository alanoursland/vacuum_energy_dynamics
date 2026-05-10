# Candidate gauge-invariant diagnostics
#
# Group:
#   08_covariant_parent_structure
#
# Script type:
#   AUDIT
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
    RouteRecord,
    ScriptOutput,
    StatusMark,
)


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"


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


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="metric_recombination_marker",
        upstream_script_id="08_covariant_parent_structure__candidate_metric_geometric_recombination",
        upstream_derivation_id="metric_recombination_marker",
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

    return counts


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
# Case 6: Controlled failure case (audit discipline)
# =============================================================================

def case_6_good_failure():
    header("Case 6: Controlled failure case - A_rad used as observable without suppression flag")

    print("Bad usage pattern (controlled failure):")
    print()
    print("  If A_rad is treated as a physical observable without an explicit suppression flag,")
    print("  the theory may compare a forbidden scalar breathing mode to observations.")
    print()
    print("Expected outcome of this bad pattern:")
    print("  A_rad without suppression flag -> FAIL")
    print("  Reason: unsuppressed massless scalar wave is not allowed as observable.")
    print()

    # Check: if the 'A_rad scalar radiation amplitude' diagnostic has RISK status,
    # flag it correctly.
    diags = build_diagnostics()
    a_rad_diag = next((d for d in diags if "A_rad" in d.name), None)
    if a_rad_diag is not None:
        if a_rad_diag.status == "RISK":
            print("[PASS] Controlled failure: A_rad correctly has RISK status in audit.")
        else:
            print(f"[FAIL] Controlled failure: A_rad has unexpected status {a_rad_diag.status}.")
    else:
        print("[FAIL] Controlled failure: A_rad diagnostic not found.")

    status_line("controlled failure case passed", "SAFE_GAUGE_FIXED",
                "A_rad RISK status correctly flagged")


# =============================================================================
# Case 7: Next study recommendation
# =============================================================================

def case_7_next_study():
    header("Case 7: Next study recommendation")

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
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement()
    diags = build_diagnostics()
    case_2_print_diagnostics(diags)
    case_3_table(diags)
    counts = case_4_status_counts(diags)
    case_5_safe_comparison_policy()
    case_6_good_failure()
    case_7_next_study()
    final_interpretation(diags)

    # --- Governance claims ---

    ns.record_claim(ClaimRecord(
        claim_id="safe_diagnostic_policy",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Safe diagnostics for reduced comparisons: areal radius R (spherical), "
            "normalized static A, TT strain. "
            "Gauge-aware diagnostics (AB/kappa_areal, kappa response) must be labeled "
            "as gauge-aware. "
            "A_rad, raw W_i, and raw coordinate trace must not be used as physical observables "
            "without explicit suppression flags or parent derivation."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="missing_observable_set_is_parent_blocker",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.OPEN_RISK,
        statement=(
            "The gauge-invariant observable set is missing. Without curvature-like "
            "diagnostics and conservation flux identities, comparisons to observations "
            "may rely on gauge-dependent sector variables."
        ),
    ))

    # --- ProofObligationRecord for MISSING diagnostics ---

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_frame_dragging_gauge_invariant_observable",
        script_id=SCRIPT_ID,
        title="Derive gauge-invariant frame-dragging observable from W_i",
        status=ObligationStatus.OPEN,
        description=(
            "Construct a gauge-invariant or gauge-fixed frame-dragging diagnostic from "
            "W_i, e.g. a curl or rotation of local inertial frames, that separates "
            "physical frame-dragging from shift gauge."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_curvature_like_parent_diagnostics",
        script_id=SCRIPT_ID,
        title="Derive curvature-like parent-level diagnostics",
        status=ObligationStatus.OPEN,
        description=(
            "Construct curvature-like observables from the parent metric/vacuum geometry "
            "that are gauge-invariant or have controlled gauge dependence."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_conserved_flux_source_identity_diagnostics",
        script_id=SCRIPT_ID,
        title="Derive conserved flux/source identity diagnostics",
        status=ObligationStatus.OPEN,
        description=(
            "Supply Bianchi-like or continuity identities and construct associated flux "
            "diagnostics for checking source-geometry compatibility."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_A_rad_suppression_for_observable_safety",
        script_id=SCRIPT_ID,
        title="Derive A_rad suppression to make scalar radiation diagnostic safe",
        status=ObligationStatus.OPEN,
        description=(
            "Show that A_rad is suppressed so that it cannot appear as a forbidden "
            "scalar breathing mode in observational comparisons."
        ),
    ))

    # --- Routes ---

    ns.record_route(RouteRecord(
        route_id="full_observable_set_derivation_route",
        script_id=SCRIPT_ID,
        name="Full gauge-invariant observable set derivation route",
        status=GovernanceStatus.CANDIDATE_ROUTE,
        tier=ClaimTier.CONSTRAINED,
        required_obligations=[
            "derive_frame_dragging_gauge_invariant_observable",
            "derive_curvature_like_parent_diagnostics",
            "derive_conserved_flux_source_identity_diagnostics",
        ],
        activation_conditions=[
            "frame-dragging observable is gauge-invariant or gauge-fixed",
            "curvature-like diagnostics are derived from parent geometry",
            "conservation flux diagnostics are established",
        ],
    ))

    # Inventory marker
    ns.record_derivation(
        derivation_id="gauge_invariant_diagnostics_marker",
        inputs=[],
        output=sp.Symbol("diagnostic_safety_inventory_built"),
        method="gauge_invariant_diagnostic_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )

    ns.write_run_metadata()

    n_missing = counts.get("MISSING", 0)
    n_risk = counts.get("RISK", 0)
    n_gauge_aware = counts.get("GAUGE_AWARE", 0)
    n_safe_fixed = counts.get("SAFE_GAUGE_FIXED", 0)
    n_invariant = counts.get("SAFE_INVARIANT", 0)

    with out.governance_assessments():
        out.line(f"safe invariant: {n_invariant}", StatusMark.PASS,
                 "areal radius R")
        out.line(f"safe gauge-fixed: {n_safe_fixed}", StatusMark.PASS,
                 "normalized A, orbit-space |grad R|^2, TT strain")
        out.line(f"gauge-aware: {n_gauge_aware}", StatusMark.DEFER,
                 "AB/kappa_areal, kappa interior response")
        out.line(f"missing: {n_missing}", StatusMark.FAIL,
                 "frame dragging, curvature-like, conservation flux")
        out.line(f"risk: {n_risk}", StatusMark.FAIL,
                 "A_rad scalar radiation amplitude")
        out.line("safe diagnostic policy", StatusMark.PASS,
                 "policy rule recorded")
        out.line("missing observable set is parent blocker", StatusMark.FAIL,
                 "open risk recorded")
        out.line("controlled failure case passed", StatusMark.PASS,
                 "A_rad RISK status correctly flagged")

    with out.unresolved_obligations():
        out.line("derive frame-dragging gauge-invariant observable", StatusMark.OBLIGATION,
                 "open proof obligation recorded")
        out.line("derive curvature-like parent diagnostics", StatusMark.OBLIGATION,
                 "open proof obligation recorded")
        out.line("derive conserved flux/source identity diagnostics", StatusMark.OBLIGATION,
                 "open proof obligation recorded")
        out.line("derive A_rad suppression for observable safety", StatusMark.OBLIGATION,
                 "open proof obligation recorded")

    out.print_summary()


if __name__ == "__main__":
    main()
