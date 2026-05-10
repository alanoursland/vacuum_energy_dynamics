# Group:
#   13_vacuum_substance_accounting
#
# Script type:
#   AUDIT

# Candidate scalar conversion not damping
#
# Purpose
# -------
# The trace/TT split found:
#
#   trace modes change zeta = ln sqrt(gamma)
#   TT modes preserve zeta at linear order
#
# This suggests:
#
#   scalar/trace disturbances do not propagate as ordinary damped waves.
#   They convert into vacuum-spacetime configuration.
#
# The user explicitly noted:
#
#   "Scalar waves that create spacetime as they propagate and erase themselves
#    is a weird model that may not be modellable with 2nd order equations."
#
# This script distinguishes:
#
#   damping
#   relaxation
#   conversion
#
# and protects the theory from accidentally importing a second-order damped
# scalar-wave model.

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
class ConversionEntry:
    name: str
    concept: str
    candidate_form: str
    allowed_interpretation: str
    forbidden_interpretation: str
    status: str
    missing: str


def build_entries() -> List[ConversionEntry]:
    return [
        ConversionEntry(
            name="C1: ordinary damping rejected as primary model",
            concept="damped scalar wave",
            candidate_form="phi_tt + gamma phi_t + omega^2 phi = 0",
            allowed_interpretation="toy/foil only if a second-order scalar mode is derived",
            forbidden_interpretation="default model for scalar conversion",
            status="REJECTED",
            missing="no derived scalar inertia/momentum channel",
        ),
        ConversionEntry(
            name="C2: first-order relaxation allowed",
            concept="non-inertial relaxation",
            candidate_form="u^mu nabla_mu kappa = -lambda_kappa (kappa-kappa_min)",
            allowed_interpretation="local trace/volume mismatch moves toward equilibrium",
            forbidden_interpretation="hidden Box kappa or oscillator/sloshing mode",
            status="CONSTRAINED",
            missing="u^mu, lambda_kappa, kappa_min source law",
        ),
        ConversionEntry(
            name="C3: conversion into volume form",
            concept="scalar/trace conversion",
            candidate_form="trace disturbance -> delta zeta, with zeta=ln sqrt(gamma)",
            allowed_interpretation="would-be scalar propagation changes vacuum-spacetime configuration",
            forbidden_interpretation="scalar wave loses energy to unrelated reservoir",
            status="CANDIDATE",
            missing="conversion operator P_trace and zeta-kappa map",
        ),
        ConversionEntry(
            name="C4: no independent scalar momentum channel",
            concept="no scalar sloshing",
            candidate_form="no term like 1/2 (u^mu nabla_mu zeta)^2 unless separately derived",
            allowed_interpretation="scalar/trace channel is constraint/relaxation/conversion-mediated",
            forbidden_interpretation="second-order scalar radiation channel by default",
            status="CONSTRAINED",
            missing="parent reason for absence of scalar inertia",
        ),
        ConversionEntry(
            name="C5: energy accounting is geometric",
            concept="vacuum-spacetime configuration exchange",
            candidate_form="d e_kappa/dtau + d epsilon_vac_config/dtau = 0",
            allowed_interpretation="curvature excess deposits into vacuum configuration; deficit pulls from it",
            forbidden_interpretation="energy destruction or one-way thermodynamic mouth",
            status="CANDIDATE",
            missing="epsilon_vac_config functional and measure",
        ),
        ConversionEntry(
            name="C6: scalar far-zone radiation forbidden",
            concept="radiation safety",
            candidate_form="source(A_rad ordinary massless)=0; Box kappa rejected",
            allowed_interpretation="ordinary far-zone radiation is TT-only",
            forbidden_interpretation="trace/volume conversion leaks into far-zone scalar flux",
            status="CONSTRAINED",
            missing="binary-radiation scalar conversion safety proof",
        ),
        ConversionEntry(
            name="C7: trace/TT split as conversion gate",
            concept="geometric projector split",
            candidate_form="trace changes zeta; TT preserves zeta at linear order",
            allowed_interpretation="trace converts, TT propagates",
            forbidden_interpretation="trace and TT not separated by projectors",
            status="STRUCTURAL",
            missing="nonlinear/covariant extension and P_trace/P_TT derivation",
        ),
        ConversionEntry(
            name="C8: A-sector mass remains separate",
            concept="mass scalar constraint",
            candidate_form="rho -> A_flux; not rho -> zeta exterior charge",
            allowed_interpretation="A carries exterior mass; zeta/kappa carries local trace-volume reconfiguration",
            forbidden_interpretation="rho double-sourced into volume-form scalar charge",
            status="CONSTRAINED",
            missing="scalar constraint propagation and boundary theorem",
        ),
        ConversionEntry(
            name="C9: conversion may be local or constrained",
            concept="support/locality status",
            candidate_form="conversion support compact or compensated; exterior zeta/kappa -> 0",
            allowed_interpretation="scalar conversion changes local geometry without far-zone scalar tail",
            forbidden_interpretation="acausal nonlocal repair unless declared constraint",
            status="UNRESOLVED",
            missing="local versus constrained conversion law",
        ),
        ConversionEntry(
            name="C10: 1D toy as foil",
            concept="dissipative curvature-metric flow",
            candidate_form="ds=e^phi dx, phi analogous to zeta_1D",
            allowed_interpretation="use phi as volume-form analogy",
            forbidden_interpretation="import R reservoir or Lambda sink as final theory",
            status="STRUCTURAL",
            missing="conservative/geometric replacement for toy reservoir",
        ),
    ]


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="trace_vs_tt_geometric_split_marker",
        upstream_script_id="13_vacuum_substance_accounting__candidate_trace_vs_tt_geometric_split",
        upstream_derivation_id="trace_vs_tt_geometric_split_marker",
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


def print_entry(e: ConversionEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Concept: {e.concept}")
    print(f"Candidate form: {e.candidate_form}")
    print(f"Allowed interpretation: {e.allowed_interpretation}")
    print(f"Forbidden interpretation: {e.forbidden_interpretation}")
    print(f"Status: {e.status}")
    print(f"Missing: {e.missing}")


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: Scalar conversion-not-damping problem")

    print("Question:")
    print()
    print("  What does it mean for scalar/trace disturbances to convert into vacuum-spacetime configuration,")
    print("  rather than propagate as damped scalar waves?")
    print()
    print("Goal:")
    print()
    print("  distinguish damping, relaxation, and conversion")
    print()
    print("Discipline:")
    print()
    print("  do not assume a second-order scalar oscillator")
    print("  do not model conversion as energy loss to an unrelated reservoir")
    print("  do not let scalar conversion leak into far-zone radiation")
    print("  do not duplicate A-sector exterior mass")

    with out.unresolved_obligations():
        out.line("scalar conversion-not-damping problem posed", StatusMark.OBLIGATION, "open: conversion operator and locality law required")


def case_1_conversion_inventory(entries: List[ConversionEntry]):
    header("Case 1: Conversion inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[ConversionEntry], out: ScriptOutput):
    header("Case 2: Compact conversion ledger")

    print("| Entry | Concept | Candidate form | Status | Missing |")
    print("|---|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.concept.replace("|", "/")
            + " | "
            + e.candidate_form.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.missing.replace("|", "/")
            + " |"
        )

    with out.governance_assessments():
        out.line("compact conversion ledger produced", StatusMark.PASS, "ledger complete")


def case_3_status_counts(entries: List[ConversionEntry], out: ScriptOutput):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  Damped scalar waves are rejected as the default model.")
    print("  First-order relaxation and geometric conversion remain viable.")
    print("  The central missing object is the conversion operator / parent projector.")

    with out.governance_assessments():
        out.line("conversion status count produced", StatusMark.PASS, "counts complete")


def case_4_distinctions(out: ScriptOutput):
    header("Case 4: Damping versus relaxation versus conversion")

    print("Damping:")
    print()
    print("  an existing wave degree loses energy to another channel")
    print("  usually assumes scalar inertia/momentum")
    print()
    print("Relaxation:")
    print()
    print("  a non-inertial variable moves first-order toward a local minimum")
    print("  no overshoot or slosh unless inertia is added")
    print()
    print("Conversion:")
    print()
    print("  the would-be scalar disturbance changes the geometry/volume-form variable itself")
    print("  the scalar wave does not remain the same propagating degree of freedom")
    print()
    print("Current preferred language:")
    print()
    print("  scalar/trace disturbances are conversion-limited, not friction-damped waves.")

    with out.governance_assessments():
        out.line("damping/relaxation/conversion distinction stated", StatusMark.PASS, "policy rule: conversion-limited language required")


def case_5_candidate_conversion_shape(out: ScriptOutput):
    header("Case 5: Candidate conversion shape")

    print("Candidate conversion skeleton:")
    print()
    print("  P_trace[source/geometry] -> delta zeta")
    print()
    print("  zeta = ln sqrt(gamma)")
    print()
    print("  kappa ~ zeta - zeta_min")
    print()
    print("  u^mu nabla_mu kappa = -lambda_kappa (kappa-kappa_min)")
    print()
    print("  d e_kappa/dtau + d epsilon_vac_config/dtau = 0")
    print()
    print("Forbidden:")
    print()
    print("  Box A")
    print("  A_rad ordinary massless source")
    print("  Box kappa")
    print("  exterior zeta/kappa 1/r tail")
    print()
    print("This is a skeleton, not a derivation.")

    with out.governance_assessments():
        out.line("candidate conversion skeleton stated", StatusMark.DEFER, "candidate route: skeleton only, not derived")


def case_6_failure_controls(out: ScriptOutput):
    header("Case 6: Failure controls")

    print("Scalar conversion fails if:")
    print()
    print("1. A second-order scalar wave is inserted without derivation.")
    print("2. Conversion becomes ordinary damping into a thermodynamic sink.")
    print("3. A_rad or Box kappa appears.")
    print("4. zeta/kappa creates an exterior scalar charge.")
    print("5. rho is duplicated into A and volume-form charge.")
    print("6. TT modes lose volume-preserving status.")
    print("7. Binary systems acquire extra far-zone scalar energy loss.")
    print("8. Conversion operator remains arbitrary.")

    with out.governance_assessments():
        out.line("scalar conversion failure controls stated", StatusMark.DEFER, "open risk: failure conditions not yet excluded")


def case_7_next_tests(out: ScriptOutput):
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_scalar_conversion_not_damping.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_mass_acceleration_gradient_coupling.py")
    print("   Find covariant/reduced expression for mass accelerating across a gradient.")
    print()
    print("3. candidate_binary_radiation_scalar_conversion_safety.py")
    print("   Check scalar conversion does not add orbital-energy-loss channel.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_mass_acceleration_gradient_coupling.py")
    print()
    print("Reason:")
    print("  Conversion needs a source/coupling expression; mass accelerating across a gradient is the ontology-to-equation bridge.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.PASS, "mass acceleration gradient coupling")


def final_interpretation():
    header("Final interpretation")

    print("Scalar conversion should currently be treated as:")
    print()
    print("  not a damped scalar wave")
    print("  not a second-order oscillator")
    print("  not energy loss to a thermodynamic mouth")
    print()
    print("but rather:")
    print()
    print("  conversion of scalar/trace disturbance into vacuum-spacetime configuration")
    print("  with zeta = ln sqrt(gamma) as the leading geometric candidate")
    print()
    print("Possible next artifact:")
    print("  candidate_scalar_conversion_not_damping.md")
    print()
    print("Possible next script:")
    print("  candidate_mass_acceleration_gradient_coupling.py")


def main():
    header("Candidate Scalar Conversion Not Damping")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    entries = build_entries()

    case_0_problem_statement(out)
    case_1_conversion_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_distinctions(out)
    case_5_candidate_conversion_shape(out)
    case_6_failure_controls(out)
    case_7_next_tests(out)
    final_interpretation()
    out.print_all()

    ns.record_claim(ClaimRecord(
        claim_id="scalar_conversion_not_damping_policy",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "Scalar/trace disturbances must be treated as conversion-limited, not friction-damped waves. "
            "A second-order scalar oscillator model (phi_tt + gamma phi_t + omega^2 phi = 0) is rejected "
            "as the default for scalar dynamics. First-order relaxation and geometric conversion remain viable. "
            "This is a policy/governance statement, not a derivation."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="no_scalar_kinetic_channel_by_default",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "No scalar kinetic/momentum channel (Box zeta, Box kappa, A_rad) is admitted by default. "
            "A second-order scalar radiation channel requires separate derivation."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_conversion_operator_P_trace",
        script_id=SCRIPT_ID,
        title="Derive conversion operator P_trace",
        status=ObligationStatus.OPEN,
        description=(
            "Provide a parent-derived conversion operator P_trace that routes scalar/trace disturbances "
            "into changes of the volume-form variable zeta, preventing far-zone scalar radiation."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_kappa_zeta_map",
        script_id=SCRIPT_ID,
        title="Derive kappa-zeta map",
        status=ObligationStatus.OPEN,
        description=(
            "Show precisely how kappa relates to zeta - zeta_min, "
            "and whether kappa is an independent variable or a diagnostic projection of zeta mismatch."
        ),
    ))
    ns.record_derivation(
        derivation_id="scalar_conversion_not_damping_marker",
        inputs=[],
        output=sp.Symbol("scalar_conversion_not_damping_audited"),
        method="scalar_conversion_not_damping_audit",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
