# Group:
#   13_vacuum_substance_accounting
#
# Script type:
#   INVENTORY

# Candidate trace versus TT geometric split
#
# Purpose
# -------
# The volume-form configuration audit found:
#
#   zeta = ln sqrt(gamma)
#
# as the best current geometric candidate for vacuum-spacetime configuration.
#
# At linear order:
#
#   delta zeta = 1/2 gamma^ij delta gamma_ij
#
# and for TT perturbations:
#
#   gamma^ij h_ij^TT = 0
#
# therefore:
#
#   delta zeta|TT = 0
#
# This script tests the geometric split:
#
#   trace / scalar / longitudinal modes change volume form and are conversion-limited.
#   TT modes are volume-preserving shear and may propagate.
#
# This is not a proof of full TT-only radiation.
# It is a theorem-target audit.

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
class SplitEntry:
    name: str
    mode: str
    geometric_effect: str
    candidate_rule: str
    forbidden_interpretation: str
    status: str
    missing: str


def build_entries() -> List[SplitEntry]:
    return [
        SplitEntry(
            name="T1: volume strain variable",
            mode="trace/volume scalar",
            geometric_effect="zeta = ln sqrt(gamma) measures local volume-form strain in a chosen slice",
            candidate_rule="delta zeta = 1/2 gamma^ij delta gamma_ij",
            forbidden_interpretation="zeta as fully covariant observable without frame/foliation",
            status="CANDIDATE",
            missing="frame/foliation or covariant volume current",
        ),
        SplitEntry(
            name="T2: pure trace perturbation",
            mode="h_ij = (1/3) gamma_ij h",
            geometric_effect="changes volume form: delta zeta = h/2",
            candidate_rule="trace perturbation routes to P_trace / volume conversion",
            forbidden_interpretation="trace perturbation propagates as ordinary far-zone scalar radiation",
            status="STRUCTURAL",
            missing="parent P_trace and conversion law",
        ),
        SplitEntry(
            name="T3: TT perturbation",
            mode="h_ij^TT with gamma^ij h_ij^TT=0 and div h^TT=0",
            geometric_effect="preserves volume at linear order: delta zeta|TT=0",
            candidate_rule="TT shear may propagate without vacuum creation/destruction",
            forbidden_interpretation="TT mode treated as volume-changing scalar conversion",
            status="CANDIDATE",
            missing="nonlinear/covariant TT statement and source coefficient",
        ),
        SplitEntry(
            name="T4: scalar A-sector",
            mode="scalar mass constraint",
            geometric_effect="controls exterior mass response through A_flux, not volume-form charge",
            candidate_rule="rho -> A_flux; not rho -> zeta exterior charge",
            forbidden_interpretation="A-sector mass duplicated as volume-form exterior scalar tail",
            status="CONSTRAINED",
            missing="parent scalar constraint propagation",
        ),
        SplitEntry(
            name="T5: kappa trace/volume mismatch",
            mode="kappa",
            geometric_effect="candidate mismatch between zeta and local equilibrium zeta_min",
            candidate_rule="kappa ~ zeta - zeta_min or reduced kappa = 1/2 ln(AB)",
            forbidden_interpretation="kappa as independent rho-sourced scalar field",
            status="CANDIDATE",
            missing="precise kappa-zeta map",
        ),
        SplitEntry(
            name="T6: scalar/trace conversion",
            mode="would-be scalar wave",
            geometric_effect="conversion into vacuum-spacetime configuration rather than far-zone propagation",
            candidate_rule="trace/volume disturbance changes zeta and relaxes/exchanges with epsilon_vac_config",
            forbidden_interpretation="Box A, A_rad, or Box kappa as ordinary radiation",
            status="CONSTRAINED",
            missing="conversion operator / parent projector",
        ),
        SplitEntry(
            name="T7: longitudinal current",
            mode="P_L j",
            geometric_effect="updates scalar constraint / density redistribution, not transverse shear",
            candidate_rule="P_L j -> scalar continuity and A constraint propagation",
            forbidden_interpretation="P_L j sources W_i or TT radiation",
            status="CONSTRAINED",
            missing="scalar constraint propagation identity",
        ),
        SplitEntry(
            name="T8: transverse current",
            mode="P_T j",
            geometric_effect="sources vector shear/frame-dragging response",
            candidate_rule="P_T j -> W_i",
            forbidden_interpretation="transverse vector response treated as volume creation",
            status="STRUCTURAL",
            missing="normalization alpha_W/K_c and recombination map",
        ),
        SplitEntry(
            name="T9: nonlinear volume preservation caveat",
            mode="finite-amplitude TT/shear",
            geometric_effect="linear trace-free does not automatically prove nonlinear determinant preservation",
            candidate_rule="TT-only radiation theorem needs nonlinear/covariant extension",
            forbidden_interpretation="linear result advertised as full theorem",
            status="RISK",
            missing="nonlinear determinant/shear analysis",
        ),
        SplitEntry(
            name="T10: far-zone radiation rule",
            mode="ordinary radiation",
            geometric_effect="far-zone propagating radiation should be volume-preserving TT shear only",
            candidate_rule="ordinary far-zone radiation = h_ij^TT",
            forbidden_interpretation="scalar/trace conversion leaks into far-zone scalar flux",
            status="CANDIDATE",
            missing="binary-radiation scalar conversion safety check",
        ),
    ]


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="volume_form_configuration_variable_marker",
        upstream_script_id="013_vacuum_substance_accounting__candidate_volume_form_configuration_variable",
        upstream_derivation_id="volume_form_configuration_variable_marker",
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


def print_entry(e: SplitEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Mode: {e.mode}")
    print(f"Geometric effect: {e.geometric_effect}")
    print(f"Candidate rule: {e.candidate_rule}")
    print(f"Forbidden interpretation: {e.forbidden_interpretation}")
    print(f"Status: {e.status}")
    print(f"Missing: {e.missing}")


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: Trace versus TT geometric split problem")

    print("Question:")
    print()
    print("  Can the trace/TT split explain scalar conversion and TT-only radiation?")
    print()
    print("Goal:")
    print()
    print("  formalize the geometric difference between volume-changing modes and volume-preserving shear")
    print()
    print("Discipline:")
    print()
    print("  do not claim full theorem from linear trace-free identity")
    print("  do not let trace modes source TT radiation")
    print("  do not let scalar conversion become far-zone scalar radiation")
    print("  keep A-sector mass separate from volume-form charge")

    with out.unresolved_obligations():
        out.line("trace versus TT split problem posed", StatusMark.OBLIGATION, "open: nonlinear/covariant theorem target")


def case_1_split_inventory(entries: List[SplitEntry]):
    header("Case 1: Trace/TT split inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[SplitEntry], out: ScriptOutput):
    header("Case 2: Compact trace/TT ledger")

    print("| Entry | Mode | Candidate rule | Status | Missing |")
    print("|---|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.mode.replace("|", "/")
            + " | "
            + e.candidate_rule.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.missing.replace("|", "/")
            + " |"
        )

    with out.governance_assessments():
        out.line("compact trace/TT ledger produced", StatusMark.PASS, "ledger complete")


def case_3_status_counts(entries: List[SplitEntry], out: ScriptOutput):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  The trace/TT split is structurally promising.")
    print("  The linear TT volume-preservation result is strong but not a full theorem.")
    print("  The next danger is scalar conversion leaking into far-zone radiation.")

    with out.governance_assessments():
        out.line("trace/TT status count produced", StatusMark.PASS, "counts complete")


def case_4_minimal_geometric_split(out: ScriptOutput):
    header("Case 4: Minimal geometric split")

    print("Let:")
    print()
    print("  zeta = ln sqrt(gamma)")
    print()
    print("Then:")
    print()
    print("  delta zeta = 1/2 gamma^ij delta gamma_ij")
    print()
    print("Trace perturbation:")
    print()
    print("  h_ij = (1/3) gamma_ij h")
    print("  gamma^ij h_ij = h")
    print("  delta zeta = h/2")
    print()
    print("TT perturbation:")
    print()
    print("  gamma^ij h_ij^TT = 0")
    print("  delta zeta|TT = 0")
    print()
    print("Interpretation:")
    print()
    print("  trace changes vacuum-spacetime amount")
    print("  TT shear preserves vacuum-spacetime amount at linear order")

    with out.governance_assessments():
        out.line("minimal trace/TT split stated", StatusMark.DEFER, "candidate route: linear observation, not full theorem")


def case_4b_symbolic_trace_tt_split(ns, out: ScriptOutput) -> None:
    header("Case 4b: Symbolic trace and TT split")

    h = sp.symbols("h")
    pure_trace_metric = sp.eye(3) * (1 + h / 3)
    pure_trace_zeta = sp.simplify(sp.Rational(1, 2) * sp.log(pure_trace_metric.det()))
    pure_trace_linear = sp.simplify(sp.diff(pure_trace_zeta, h).subs(h, 0) * h)

    hxx, hxy = sp.symbols("hxx hxy")
    h_tt = sp.Matrix([[hxx, hxy, 0], [hxy, -hxx, 0], [0, 0, 0]])
    tt_trace = sp.simplify(h_tt.trace())
    tt_linear_delta = sp.simplify(sp.Rational(1, 2) * tt_trace)

    print("Pure trace sector:")
    print()
    print(f"  zeta(h) = {pure_trace_zeta}")
    print(f"  linear delta zeta = {pure_trace_linear}")
    print()
    print("TT sector sample:")
    print()
    print(f"  trace(h_TT) = {tt_trace}")
    print(f"  linear delta zeta|TT = {tt_linear_delta}")

    with out.sample_results():
        out.line("trace mode changes zeta", StatusMark.PASS, f"delta zeta = {pure_trace_linear}")
        out.line("TT mode preserves zeta linearly", StatusMark.PASS, f"delta zeta = {tt_linear_delta}")

    ns.record_derivation(
        derivation_id="trace_tt_linear_volume_split",
        inputs=[pure_trace_metric, h_tt],
        output=sp.Tuple(pure_trace_linear, tt_linear_delta),
        method="symbolic trace versus TT volume split",
        status=Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
        scope="linear perturbation, specific isotropic trace and 2D TT sample",
    )


def case_5_theorem_target(out: ScriptOutput):
    header("Case 5: TT-only radiation theorem target")

    print("Possible theorem target:")
    print()
    print("  Ordinary far-zone radiation is TT-only because")
    print("  volume-changing trace/scalar modes convert into vacuum-spacetime configuration,")
    print("  while volume-preserving TT shear propagates.")
    print()
    print("Required pieces:")
    print()
    print("1. zeta or equivalent volume-form variable.")
    print("2. P_trace conversion law.")
    print("3. P_TT propagation law.")
    print("4. scalar conversion not damping model.")
    print("5. binary radiation scalar-conversion safety.")
    print("6. nonlinear/covariant extension.")
    print()
    print("Current status:")
    print("  theorem target, not theorem.")

    with out.unresolved_obligations():
        out.line("TT-only theorem target stated", StatusMark.OBLIGATION, "open: all six required pieces remain unresolved")


def case_6_failure_controls(out: ScriptOutput):
    header("Case 6: Failure controls")

    print("The trace/TT split fails if:")
    print()
    print("1. Trace modes propagate as ordinary far-zone scalar radiation.")
    print("2. TT modes change zeta / volume at the relevant order.")
    print("3. A-sector mass is duplicated as volume-form exterior charge.")
    print("4. Kappa and zeta become independent scalar charges.")
    print("5. Linear trace-free identity is overclaimed as full covariance.")
    print("6. Binary systems acquire extra scalar energy loss.")
    print("7. P_trace and P_TT are not actually independent projectors.")

    with out.governance_assessments():
        out.line("trace/TT failure controls stated", StatusMark.DEFER, "open risk: failure conditions not yet excluded")


def case_7_next_tests(out: ScriptOutput):
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_trace_vs_tt_geometric_split.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_scalar_conversion_not_damping.py")
    print("   Replace damping language with conversion-limited scalar dynamics.")
    print()
    print("3. candidate_binary_radiation_scalar_conversion_safety.py")
    print("   Check if scalar conversion introduces extra orbital-energy loss.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_scalar_conversion_not_damping.py")
    print()
    print("Reason:")
    print("  The trace/TT split suggests scalar modes convert; now define conversion versus damping.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.PASS, "scalar conversion not damping")


def final_interpretation():
    header("Final interpretation")

    print("The trace/TT geometric split says:")
    print()
    print("  trace modes change zeta = ln sqrt(gamma)")
    print("  TT modes preserve zeta at linear order")
    print("  scalar/trace modes are candidates for conversion into vacuum-spacetime configuration")
    print("  TT modes are candidates for propagating volume-preserving shear")
    print()
    print("This is a strong theorem target, not a completed theorem.")
    print()
    print("Possible next artifact:")
    print("  candidate_trace_vs_tt_geometric_split.md")
    print()
    print("Possible next script:")
    print("  candidate_scalar_conversion_not_damping.py")


def main():
    header("Candidate Trace Versus TT Geometric Split")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    entries = build_entries()

    case_0_problem_statement(out)
    case_1_split_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_minimal_geometric_split(out)
    case_4b_symbolic_trace_tt_split(ns, out)
    case_5_theorem_target(out)
    case_6_failure_controls(out)
    case_7_next_tests(out)
    final_interpretation()

    ns.record_claim(ClaimRecord(
        claim_id="tt_modes_volume_preserving_linear",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "TT perturbations are trace-free (gamma^ij h_ij^TT = 0), hence delta zeta|TT = 0 "
            "at linear order. This is a candidate basis for TT-only far-zone radiation. "
            "The nonlinear/covariant extension remains an open theorem target."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="trace_modes_conversion_not_radiation",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "Trace/scalar perturbations change zeta = ln sqrt(gamma) and are conversion-limited. "
            "They must not propagate as ordinary far-zone scalar radiation (Box A, Box kappa)."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_tt_only_radiation_theorem",
        script_id=SCRIPT_ID,
        title="Derive TT-only radiation theorem",
        status=ObligationStatus.OPEN,
        description=(
            "Show that ordinary far-zone radiation is TT-only because trace/scalar modes convert "
            "into vacuum-spacetime configuration. Requires zeta variable, P_trace conversion law, "
            "P_TT propagation law, scalar conversion safety, and nonlinear/covariant extension."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_P_trace_and_P_TT_projectors",
        script_id=SCRIPT_ID,
        title="Derive P_trace and P_TT projector definitions",
        status=ObligationStatus.OPEN,
        description=(
            "Provide parent projector definitions for P_trace (routes trace/volume imbalance "
            "to volume conversion) and P_TT (routes TT shear to propagation)."
        ),
    ))
    ns.record_derivation(
        derivation_id="trace_vs_tt_geometric_split_marker",
        inputs=[],
        output=sp.Symbol("trace_vs_tt_geometric_split_audited"),
        method="trace_vs_tt_geometric_split_audit",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
