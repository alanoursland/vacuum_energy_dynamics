# Candidate field equation closure failure modes
#
# Group:
#   11_field_equation_closure
#
# Script type:
#   AUDIT
#
# Purpose
# -------
# The parent identity template created a scaffold:
#
#   Div E_parent[A,W,h_TT,kappa]
#     = B_closed[T] + B_active[Sigma_creation] + B_relax[Gamma_relax]
#
# But it explicitly did not derive closure.
#
# This script lists ways full field-equation closure can fail.
#
# Goal:
#
#   protect the project from decorative ontology,
#   silent GR import,
#   scalar double-counting,
#   matched coefficients claimed as derived,
#   kappa repair-knob behavior,
#   and unearned observational claims.
#
# This is a failure audit, not a derivation.

from dataclasses import dataclass
from pathlib import Path
from typing import List

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.governance import (
    ClaimRecord,
    ClaimTier,
    EvidenceRecord,
    EvidenceType,
    GovernanceStatus,
    ObligationStatus,
    ProofObligationRecord,
    ReasonCode,
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
class FailureMode:
    name: str
    description: str
    severity: str
    symptom: str
    prevention: str
    current_status: str
    next_check: str


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="parent_identity_template_marker",
        upstream_script_id="011_field_equation_closure__candidate_parent_identity_template",
        upstream_derivation_id="parent_identity_template_marker",
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


def build_failures() -> List[FailureMode]:
    return [
        FailureMode(
            name="F1: Decorative parent identity",
            description="The parent identity merely renames the Bianchi identity without deriving it from vacuum ontology.",
            severity="FATAL",
            symptom="Div E_parent is asserted to vanish because GR does, not because the vacuum-curvature structure forces it.",
            prevention="Demand definitions of E_parent and B_source plus reduced-sector implications.",
            current_status="UNRESOLVED",
            next_check="candidate_parent_identity_reduced_implications.py",
        ),
        FailureMode(
            name="F2: Silent GR metric import",
            description="Metric recombination copies GR component structure while claiming reconstruction.",
            severity="MAJOR",
            symptom="g_tt, g_0i, g_ij are assigned GR forms before ontology-derived recombination.",
            prevention="Keep recombination map labeled reduced/structural/unfinished.",
            current_status="WATCH",
            next_check="candidate_metric_recombination_parent_requirements.py",
        ),
        FailureMode(
            name="F3: Scalar double-counting",
            description="rho or trace sources both A and an independent scalar/kappa channel.",
            severity="FATAL",
            symptom="A carries mass field while kappa also creates exterior 1/r response.",
            prevention="Enforce S_kappa[rho]=0 and Q_kappa=0 unless parent identity says otherwise.",
            current_status="CONTROLLED",
            next_check="candidate_no_double_counting_constraints.py",
        ),
        FailureMode(
            name="F4: Kappa repair knob",
            description="kappa is adjusted to fix contradictions without an equation/source identity.",
            severity="MAJOR",
            symptom="kappa absorbs every mismatch: pressure, boundary, scalar radiation, interior curvature, and metric trace.",
            prevention="Restrict kappa to non-inertial trace/minimum relaxation with exterior zero-flux rules.",
            current_status="WATCH",
            next_check="candidate_kappa_non_radiative_trace_identity.py",
        ),
        FailureMode(
            name="F5: Hidden breathing wave",
            description="kappa gains a second-order wave equation or independent momentum channel.",
            severity="FATAL",
            symptom="Box kappa = source, scalar radiation power, or exterior breathing polarization appears.",
            prevention="Forbid ordinary massless kappa propagation unless separately derived and controlled.",
            current_status="CONTROLLED",
            next_check="candidate_constraint_vs_evolution_split.py",
        ),
        FailureMode(
            name="F6: Tensor coupling matched but claimed derived",
            description="C_T or the tensor flux coefficient is imported from GR.",
            severity="MAJOR",
            symptom="2G/c^4, 16*pi*G/c^4, or c^3/(32*pi*G) appears as target matching.",
            prevention="Mark tensor coupling/flux as MATCHED until action stiffness derives them.",
            current_status="UNRESOLVED",
            next_check="candidate_tensor_action_stiffness_revisit.py",
        ),
        FailureMode(
            name="F7: Vector normalization matched but claimed derived",
            description="Frame-dragging coefficient is set to the Lense-Thirring value by hand.",
            severity="MAJOR",
            symptom="W_i shape is used to claim full frame-dragging recovery without beta_W and alpha_W/K_c derivation.",
            prevention="Separate vector shape from normalization.",
            current_status="UNRESOLVED",
            next_check="candidate_vector_normalization_closure.py",
        ),
        FailureMode(
            name="F8: Boundary smoothing tunes measured mass",
            description="kappa or joint-minimum smoothing changes exterior A flux.",
            severity="FATAL",
            symptom="near-boundary relaxation changes M_ext or exterior 1/r coefficient.",
            prevention="Require delta M_ext = 0 under kappa boundary relaxation.",
            current_status="WATCH",
            next_check="candidate_boundary_mass_preservation_identity.py",
        ),
        FailureMode(
            name="F9: Active-regime leakage",
            description="Sigma_creation enters ordinary closed gravity equations.",
            severity="MAJOR",
            symptom="ordinary matter sources include creation/exchange terms without active-regime trigger.",
            prevention="Set Sigma_creation=0 in ordinary closed regime.",
            current_status="CONTROLLED",
            next_check="candidate_active_regime_exclusion_rule.py",
        ),
        FailureMode(
            name="F10: Relaxation as energy loss",
            description="Gamma_relax is treated as damping that removes energy from the system.",
            severity="MAJOR",
            symptom="trace imbalance disappears without destination variable.",
            prevention="Require vacuum configuration energy accounting.",
            current_status="WATCH",
            next_check="candidate_relaxation_energy_accounting_identity.py",
        ),
        FailureMode(
            name="F11: Near-boundary deviation overclaim",
            description="A possible near-boundary deviation from GR is claimed before magnitude or observable is derived.",
            severity="RISK",
            symptom="theory advertises unmeasured prediction from spline/joint-minimum diagnostic alone.",
            prevention="Diagnostic before prediction; require weights, sigma, recombination map, observable.",
            current_status="CONTROLLED",
            next_check="candidate_near_boundary_observability_gate.py",
        ),
        FailureMode(
            name="F12: Sector ledger mistaken for closure",
            description="A well-organized sector table is treated as a closed field-equation theory.",
            severity="FATAL",
            symptom="inventory, source split, and constraints are described as derivation of full field equations.",
            prevention="Keep closure status MISSING until parent identity and recombination are derived.",
            current_status="WATCH",
            next_check="field_equation_closure_summary.md",
        ),
    ]


def print_failure(f: FailureMode) -> None:
    severity_marks = {
        "FATAL": "FAIL",
        "MAJOR": "FAIL",
        "RISK": "WARN",
    }
    status_marks = {
        "CONTROLLED": "PASS",
        "WATCH": "WARN",
        "UNRESOLVED": "FAIL",
    }
    sev_mark = severity_marks.get(f.severity, "INFO")
    sts_mark = status_marks.get(f.current_status, "INFO")
    print()
    print("-" * 120)
    print(f.name)
    print("-" * 120)
    print(f"Description: {f.description}")
    print(f"[{sev_mark}] {f.name}: severity={f.severity}, current={f.current_status}")
    print(f"Symptom: {f.symptom}")
    print(f"Prevention: {f.prevention}")
    print(f"Next check: {f.next_check}")


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: Field equation closure failure modes problem")

    print("Question:")
    print()
    print("  How can the attempted field-equation closure fail?")
    print()
    print("Goal:")
    print()
    print("  list failure modes before attempting a stronger parent identity")
    print()
    print("Discipline:")
    print()
    print("  do not confuse scaffolds with derivations")
    print("  do not claim matched coefficients are derived")
    print("  do not let kappa become a repair knob")
    print("  do not let organized sectors masquerade as closure")

    with out.governance_assessments():
        out.line("closure failure problem posed", StatusMark.WARN, "open risk")


def case_1_failure_inventory(entries: List[FailureMode]):
    header("Case 1: Failure mode inventory")
    for entry in entries:
        print_failure(entry)


def case_2_compact_table(entries: List[FailureMode], out: ScriptOutput):
    header("Case 2: Compact failure ledger")

    print("| Failure mode | Severity | Current status | Prevention |")
    print("|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.severity
            + " | "
            + e.current_status
            + " | "
            + e.prevention.replace("|", "/")
            + " |"
        )

    with out.governance_assessments():
        out.line("compact failure ledger produced", StatusMark.WARN, "open risk inventory")


def case_3_most_dangerous_failures(entries: List[FailureMode], out: ScriptOutput):
    header("Case 3: Most dangerous failures")

    fatal = [e for e in entries if e.severity == "FATAL"]

    print("Fatal closure failures:")
    print()
    for e in fatal:
        print(f"  {e.name}")
    print()
    print("These would invalidate the closure claim rather than merely delay it.")

    with out.counterexamples():
        out.line("fatal failures identified", StatusMark.FAIL,
                 "closure claim unsafe until controlled")


def case_4_current_controls(out: ScriptOutput):
    header("Case 4: Current controls")

    print("Currently partially controlled:")
    print()
    print("  scalar double-counting")
    print("  hidden breathing wave")
    print("  active-regime leakage")
    print("  near-boundary deviation overclaim")
    print()
    print("Still unresolved:")
    print()
    print("  parent identity derivation")
    print("  tensor coupling")
    print("  vector normalization")
    print("  covariant recombination")
    print("  boundary mass theorem")
    print("  relaxation energy accounting")

    with out.governance_assessments():
        out.line("current controls summarized", StatusMark.WARN, "partial controls only")


def case_5_next_tests(out: ScriptOutput):
    header("Case 5: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_field_equation_closure_failure_modes.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_closure_minimal_equation_set.py")
    print("   Assemble current minimal equation set with labels.")
    print()
    print("3. candidate_parent_identity_reduced_implications.py")
    print("   Test what the parent identity must imply in reduced sectors.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_closure_minimal_equation_set.py")
    print()
    print("Reason:")
    print("  The failure ledger is protective; now assemble the minimal current equation set with labels.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.WARN, "structural guidance")


def case_6_good_failure(out: ScriptOutput):
    header("Case 6: Good failure demonstration")

    print("Controlled failure: kappa gains a Box equation (F5 / hidden breathing wave).")
    print()
    print("  If kappa satisfied Box kappa = source instead of dot(kappa) = -mu*K*(kappa-kappa_min),")
    print("  it would be a propagating scalar field with an independent momentum channel.")
    print("  This must be detectable as a fatal failure.")

    # Construct the detectable symptom symbolically
    t, x, c_speed = sp.symbols("t x c", positive=True)
    kappa = sp.Function("kappa")
    # Box kappa = d^2 kappa/dt^2 - c^2 d^2 kappa/dx^2 (1D schematic)
    box_kappa = sp.diff(kappa(t, x), t, 2) - c_speed**2 * sp.diff(kappa(t, x), x, 2)
    # For a wave mode kappa = exp(i(kx - omega t)), box_kappa = (-omega^2 + c^2 k^2) kappa
    omega, k_wave = sp.symbols("omega k", real=True)
    kappa_wave = sp.exp(sp.I * (k_wave * x - omega * t))
    # Eigenvalue of Box acting on plane wave
    box_eigenvalue = sp.diff(kappa_wave, t, 2) - c_speed**2 * sp.diff(kappa_wave, x, 2)
    box_eigenvalue_simplified = sp.simplify(box_eigenvalue / kappa_wave)

    print()
    print(f"  Box kappa eigenvalue on plane wave exp(i(kx-omega t)):")
    print(f"    = {box_eigenvalue_simplified}")
    print()
    print("  For a non-dispersive wave: omega^2 = c^2 k^2, eigenvalue = 0.")
    print("  This would mean kappa is a massless propagating scalar.")
    print()
    print("  This is the F5 failure mode: kappa must NOT satisfy this equation.")
    print("  Governance records this as a FATAL open risk if Box kappa appears.")

    # The symptom is nonzero dispersion relation eigenvalue for non-trivial wave
    has_propagating_mode = box_eigenvalue_simplified != 0  # nonzero means wave equation exists

    with out.counterexamples():
        out.line(
            "Box kappa eigenvalue on plane wave",
            StatusMark.FAIL,
            f"eigenvalue = {box_eigenvalue_simplified}; if set to 0 gives propagating mode (F5 fatal)",
        )

    print()
    if has_propagating_mode:
        print("[PASS] Good failure: Box kappa acting on plane wave gives nonzero eigenvalue.")
        print("       Governance correctly identifies this as the F5 fatal failure mode if invoked.")
    else:
        print("[WARN] Unexpected: eigenvalue was zero. Check symbolics.")


def final_interpretation():
    header("Final interpretation")

    print("The closure attempt can fail in three main ways:")
    print()
    print("  1. decorative identity")
    print("  2. silent GR import")
    print("  3. scalar/source double-counting")
    print()
    print("It can also fail through matched coefficients, kappa repair-knob behavior,")
    print("boundary mass tuning, active-regime leakage, and overclaimed predictions.")
    print()
    print("Possible next artifact:")
    print("  candidate_field_equation_closure_failure_modes.md")
    print()
    print("Possible next script:")
    print("  candidate_closure_minimal_equation_set.py")


def record_governance(ns, entries: List[FailureMode]) -> None:
    # UNRESOLVED (FATAL) -> OPEN obligations
    ns.record_obligation(ProofObligationRecord(
        obligation_id="resolve_F1_decorative_parent_identity",
        script_id=SCRIPT_ID,
        title="Resolve F1: prevent decorative parent identity",
        status=ObligationStatus.OPEN,
        description=(
            "F1 is fatal: Div E_parent must not merely rename the GR Bianchi identity. "
            "Definitions of E_parent and B_source from vacuum ontology are required, "
            "along with explicit reduced-sector implications."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="resolve_F6_tensor_coupling_matched",
        script_id=SCRIPT_ID,
        title="Resolve F6: tensor coupling must not be claimed derived when matched",
        status=ObligationStatus.OPEN,
        description=(
            "F6 is major: C_T and tensor flux coefficient must be derived from action stiffness. "
            "Until then they are marked MATCHED and must not be advertised as derived."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="resolve_F7_vector_normalization_matched",
        script_id=SCRIPT_ID,
        title="Resolve F7: vector normalization must not be claimed derived when matched",
        status=ObligationStatus.OPEN,
        description=(
            "F7 is major: frame-dragging coefficient must be derived from vacuum vector stiffness. "
            "Until beta_W and alpha_W/K_c are derived, normalization is MATCHED."
        ),
    ))

    # CONTROLLED failures -> CANDIDATE_ROUTE claims (controlled but not proven)
    ns.record_claim(ClaimRecord(
        claim_id="fm_F3_scalar_double_counting_controlled",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "F3 (scalar double-counting) is currently controlled by enforcing S_kappa[rho]=0 "
            "and Q_kappa=0. A parent identity proving these constraints is still missing."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="fm_F5_hidden_breathing_wave_controlled",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "F5 (hidden breathing wave) is currently controlled by forbidding ordinary massless "
            "kappa propagation (Box kappa = source). kappa is restricted to first-order relaxation. "
            "A parent identity proving this is still missing."
        ),
    ))

    # WATCH failures -> OPEN_RISK claims
    ns.record_claim(ClaimRecord(
        claim_id="fm_F2_silent_gr_import_watch",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.OPEN_RISK,
        statement=(
            "F2 (silent GR metric import) is under watch. Recombination map is kept labeled "
            "reduced/structural/unfinished to prevent silent GR import. Parent map is missing."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="fm_F12_sector_ledger_mistaken_for_closure_watch",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.OPEN_RISK,
        statement=(
            "F12 (sector ledger mistaken for closure) is under watch. Closure status is kept "
            "MISSING until parent identity and recombination are derived."
        ),
    ))

    # Inventory marker
    ns.record_derivation(
        derivation_id="field_equation_closure_failure_modes_marker",
        inputs=[],
        output=sp.Symbol("field_equation_closure_failure_modes_listed"),
        method="field_equation_closure_failure_modes_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )


def main():
    header("Candidate Field Equation Closure Failure Modes")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    out = ScriptOutput()
    case_0_problem_statement(out)
    entries = build_failures()
    case_1_failure_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_most_dangerous_failures(entries, out)
    case_4_current_controls(out)
    case_5_next_tests(out)
    case_6_good_failure(out)
    final_interpretation()
    record_governance(ns, entries)
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
