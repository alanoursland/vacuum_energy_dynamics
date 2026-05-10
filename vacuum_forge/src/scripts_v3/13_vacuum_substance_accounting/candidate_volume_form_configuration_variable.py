# Group:
#   13_vacuum_substance_accounting
#
# Script type:
#   INVENTORY

# Candidate volume form configuration variable
#
# Purpose
# -------
# The vacuum substance accounting inventory found:
#
#   E_vac_config must be geometric or tightly constrained bookkeeping.
#   The best immediate geometric targets are sqrt_gamma and ln_sqrt_gamma.
#
# This script tests whether vacuum-spacetime configuration can be represented
# by a volume-form variable.
#
# Corrected ontology:
#
#   vacuum is spacetime.
#   creating vacuum creates spacetime.
#   changing local spacetime creates curvature.
#
# Therefore a natural candidate is:
#
#   physical volume element = sqrt(gamma) d^3x
#
# and a natural local strain variable is:
#
#   zeta = ln sqrt(gamma)
#
# This script is not a derivation.
# It is a candidate-variable audit.

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
class VolumeCandidate:
    name: str
    candidate_form: str
    role: str
    allowed_use: str
    forbidden_use: str
    status: str
    missing: str
    next_test: str


def build_candidates() -> List[VolumeCandidate]:
    return [
        VolumeCandidate(
            name="V1: physical volume element",
            candidate_form="dV_phys = sqrt(gamma) d^3x",
            role="Geometric expression of local vacuum/spacetime amount in a chosen slice.",
            allowed_use="candidate basis for epsilon_vac_config",
            forbidden_use="treated as gauge-invariant observable without slicing/frame definition",
            status="CANDIDATE",
            missing="choice of spatial metric gamma_ij and foliation/frame",
            next_test="trace_vs_TT_split",
        ),
        VolumeCandidate(
            name="V2: logarithmic volume strain",
            candidate_form="zeta = ln sqrt(gamma)",
            role="Additive local trace/volume configuration variable.",
            allowed_use="candidate scalar/trace conversion variable",
            forbidden_use="duplicate A-sector mass response or exterior scalar charge",
            status="CANDIDATE",
            missing="reference volume / background subtraction and relation to kappa",
            next_test="trace_vs_TT_split",
        ),
        VolumeCandidate(
            name="V3: perturbative trace relation",
            candidate_form="delta zeta = 1/2 gamma^ij delta gamma_ij",
            role="Shows that volume change is trace part of spatial metric perturbation.",
            allowed_use="separate trace/volume channel from TT shear",
            forbidden_use="allowing trace to source h_TT or scalar radiation",
            status="STRUCTURAL",
            missing="parent projector P_trace",
            next_test="candidate_trace_vs_tt_geometric_split.py",
        ),
        VolumeCandidate(
            name="V4: TT volume preservation",
            candidate_form="gamma^ij h_ij^TT = 0 -> delta zeta|TT = 0",
            role="Candidate reason TT modes propagate without vacuum creation/destruction.",
            allowed_use="theorem target behind TT-only radiation",
            forbidden_use="claiming theorem before parent projector derivation",
            status="CANDIDATE",
            missing="full nonlinear/covariant statement and TT source identity",
            next_test="candidate_trace_vs_tt_geometric_split.py",
        ),
        VolumeCandidate(
            name="V5: 1D toy analog",
            candidate_form="ds = e^phi dx, so zeta_1D = phi",
            role="Concrete analog: local expansion field multiplies physical length.",
            allowed_use="intuition and toy diagnostic for volume-form accounting",
            forbidden_use="importing the toy's irreversible reservoir R as theory",
            status="STRUCTURAL",
            missing="higher-dimensional generalization and conservative exchange law",
            next_test="scalar_conversion_not_damping",
        ),
        VolumeCandidate(
            name="V6: kappa relation candidate",
            candidate_form="kappa ~ zeta - zeta_min or kappa = 1/2 ln(AB) in reduced areal gauge",
            role="Relates kappa to volume/trace mismatch rather than independent scalar field.",
            allowed_use="kappa as constrained trace/volume relaxation diagnostic",
            forbidden_use="kappa as rho-sourced exterior scalar charge",
            status="CANDIDATE",
            missing="precise map between kappa and volume-form strain",
            next_test="candidate_scalar_conversion_not_damping.py",
        ),
        VolumeCandidate(
            name="V7: epsilon_vac_config candidate",
            candidate_form="epsilon_vac_config = F(zeta, zeta_min, grad zeta, ...)",
            role="Geometric local configuration density built from volume strain.",
            allowed_use="destination/source for scalar/trace conversion",
            forbidden_use="bottomless reservoir or coefficient tuning functional",
            status="CANDIDATE",
            missing="functional form F and stiffness coefficients",
            next_test="vacuum_accounting_parent_balance",
        ),
        VolumeCandidate(
            name="V8: A-sector separation",
            candidate_form="M_ext determined by A_flux, not by integral zeta",
            role="Protects exterior mass from volume-form relaxation.",
            allowed_use="volume reconfiguration may be compact/compensated while A_flux remains fixed",
            forbidden_use="using volume strain integral to alter exterior mass",
            status="CONSTRAINED",
            missing="boundary volume mode no exterior charge theorem",
            next_test="candidate_boundary_volume_mode_no_exterior_charge.py",
        ),
        VolumeCandidate(
            name="V9: exterior neutrality",
            candidate_form="zeta_ext -> 0, kappa_ext -> 0, Q_volume = 0",
            role="Prevents volume-form scalar tail outside ordinary matter.",
            allowed_use="compact or compensated trace/volume reconfiguration",
            forbidden_use="zeta_ext ~ 1/r scalar charge",
            status="CONSTRAINED",
            missing="projection/boundary theorem",
            next_test="candidate_boundary_volume_mode_no_exterior_charge.py",
        ),
        VolumeCandidate(
            name="V10: slicing/frame caveat",
            candidate_form="zeta = ln sqrt(gamma) depends on spatial decomposition",
            role="Flags that volume-form accounting needs a frame/foliation or covariant replacement.",
            allowed_use="temporary reduced/3+1 candidate",
            forbidden_use="pretending zeta is fully covariant without extra structure",
            status="UNRESOLVED",
            missing="frame u^mu, foliation, or covariant volume current",
            next_test="candidate_vacuum_transport_current_constraints.py",
        ),
    ]


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="vacuum_substance_accounting_inventory_marker",
        upstream_script_id="13_vacuum_substance_accounting__candidate_vacuum_substance_accounting_inventory",
        upstream_derivation_id="vacuum_substance_accounting_inventory_marker",
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


def print_candidate(v: VolumeCandidate) -> None:
    print()
    print("-" * 120)
    print(v.name)
    print("-" * 120)
    print(f"Candidate form: {v.candidate_form}")
    print(f"Role: {v.role}")
    print(f"Allowed use: {v.allowed_use}")
    print(f"Forbidden use: {v.forbidden_use}")
    print(f"Status: {v.status}")
    print(f"Missing: {v.missing}")
    print(f"Next test: {v.next_test}")


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: Volume-form configuration variable problem")

    print("Question:")
    print()
    print("  Can vacuum-spacetime configuration be represented by a volume-form variable?")
    print()
    print("Goal:")
    print()
    print("  test sqrt(gamma) and ln sqrt(gamma) as geometric candidates for epsilon_vac_config")
    print()
    print("Discipline:")
    print()
    print("  volume form is geometric but slicing/frame dependent")
    print("  volume strain must not duplicate A-sector mass")
    print("  TT modes should be volume-preserving")
    print("  scalar/trace modes should be conversion-limited")
    print("  do not import the 1D toy's one-way reservoir as theory")

    with out.unresolved_obligations():
        out.line("volume-form problem posed", StatusMark.OBLIGATION, "open: geometric definition of epsilon_vac_config required")


def case_1_candidate_inventory(entries: List[VolumeCandidate]):
    header("Case 1: Volume-form candidate inventory")
    for entry in entries:
        print_candidate(entry)


def case_2_compact_table(entries: List[VolumeCandidate], out: ScriptOutput):
    header("Case 2: Compact volume-form ledger")

    print("| Candidate | Role | Status | Forbidden use | Missing |")
    print("|---|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.candidate_form.replace("|", "/")
            + " | "
            + e.role.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.forbidden_use.replace("|", "/")
            + " | "
            + e.missing.replace("|", "/")
            + " |"
        )

    with out.governance_assessments():
        out.line("compact volume-form ledger produced", StatusMark.PASS, "ledger complete")


def case_3_status_counts(entries: List[VolumeCandidate], out: ScriptOutput):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  The volume-form candidate is promising but not covariant yet.")
    print("  The key structural fact is that TT perturbations are trace-free, hence volume-preserving at linear order.")
    print("  The key risk is duplicating A-sector scalar mass response.")

    with out.governance_assessments():
        out.line("volume-form status count produced", StatusMark.PASS, "counts complete")


def case_3b_linear_volume_relation(ns, out: ScriptOutput) -> None:
    header("Case 3b: Linear volume-form relation")

    h = sp.symbols("h")
    scale = 1 + h / 3
    zeta = sp.simplify(sp.Rational(3, 2) * sp.log(scale))
    linear_delta = sp.simplify(sp.diff(zeta, h).subs(h, 0) * h)

    print("Pure trace perturbation model:")
    print()
    print("  gamma_ij = (1 + h/3) delta_ij")
    print(f"  zeta(h) = {zeta}")
    print(f"  linear delta zeta = {linear_delta}")
    print()
    print("Interpretation:")
    print("  the isotropic trace perturbation gives delta zeta = h/2 at linear order.")

    with out.sample_results():
        out.line("linear trace-volume relation", StatusMark.PASS, f"delta zeta = {linear_delta}")

    ns.record_derivation(
        derivation_id="volume_form_linear_trace_relation",
        inputs=[scale],
        output=linear_delta,
        method="linearized volume-form perturbation",
        status=Status.DERIVED,
        record_kind=RecordKind.SAMPLE_DERIVATION,
        scope="isotropic trace perturbation only",
    )


def case_4_minimal_candidate_definition(out: ScriptOutput):
    header("Case 4: Minimal candidate definition")

    print("Minimal candidate:")
    print()
    print("  zeta = ln sqrt(gamma)")
    print()
    print("Perturbative variation:")
    print()
    print("  delta zeta = 1/2 gamma^ij delta gamma_ij")
    print()
    print("TT perturbation:")
    print()
    print("  gamma^ij h_ij^TT = 0")
    print()
    print("Therefore:")
    print()
    print("  delta zeta|TT = 0")
    print()
    print("Interpretation:")
    print()
    print("  trace/volume modes change vacuum-spacetime amount")
    print("  TT modes are volume-preserving shear")
    print()
    print("This is a linear structural observation, not a full theorem.")

    with out.governance_assessments():
        out.line("minimal volume-form candidate stated", StatusMark.DEFER, "candidate route: linear observation, not full theorem")


def case_5_relation_to_1d_toy(out: ScriptOutput):
    header("Case 5: Relation to 1D toy model")

    print("The 1D toy has:")
    print()
    print("  ds = e^phi dx")
    print()
    print("so:")
    print()
    print("  phi = ln(ds/dx)")
    print()
    print("This is the 1D analog of:")
    print()
    print("  zeta = ln sqrt(gamma)")
    print()
    print("Useful extraction:")
    print()
    print("  physical length/volume is coordinate measure multiplied by a vacuum-configuration factor")
    print()
    print("Rejected extraction:")
    print()
    print("  a one-way thermodynamic reservoir R as final theory")
    print()
    print("Reinterpreted extraction:")
    print()
    print("  scalar/trace conversion changes the geometry/volume-form variable itself")

    with out.governance_assessments():
        out.line("1D toy relation stated", StatusMark.PASS, "analogy accepted; reservoir rejected")


def case_6_failure_controls(out: ScriptOutput):
    header("Case 6: Failure controls")

    print("The volume-form candidate fails if:")
    print()
    print("1. zeta duplicates A-sector exterior mass.")
    print("2. zeta produces an exterior 1/r scalar tail.")
    print("3. zeta is treated as gauge-invariant without frame/foliation.")
    print("4. kappa and zeta become independent scalar charges.")
    print("5. TT modes accidentally change volume.")
    print("6. scalar conversion becomes far-zone scalar radiation.")
    print("7. epsilon_vac_config becomes a coefficient tuning reservoir.")

    with out.governance_assessments():
        out.line("volume-form failure controls stated", StatusMark.DEFER, "open risk: failure conditions not yet excluded")


def case_7_next_tests(out: ScriptOutput):
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_volume_form_configuration_variable.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_trace_vs_tt_geometric_split.py")
    print("   Formalize why trace/volume modes convert while TT modes propagate.")
    print()
    print("3. candidate_scalar_conversion_not_damping.py")
    print("   Replace damping language with conversion-limited scalar dynamics.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_trace_vs_tt_geometric_split.py")
    print()
    print("Reason:")
    print("  The volume-form candidate points directly to the trace/TT split as the possible TT-only radiation theorem.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.PASS, "trace vs TT geometric split")


def final_interpretation():
    header("Final interpretation")

    print("The best current geometric candidate is:")
    print()
    print("  zeta = ln sqrt(gamma)")
    print()
    print("with:")
    print()
    print("  dV_phys = sqrt(gamma) d^3x")
    print("  delta zeta = 1/2 gamma^ij delta gamma_ij")
    print("  delta zeta|TT = 0")
    print()
    print("Interpretation:")
    print()
    print("  trace/volume modes change vacuum-spacetime amount")
    print("  TT modes are volume-preserving shear")
    print()
    print("Possible next artifact:")
    print("  candidate_volume_form_configuration_variable.md")
    print()
    print("Possible next script:")
    print("  candidate_trace_vs_tt_geometric_split.py")


def main():
    header("Candidate Volume Form Configuration Variable")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    entries = build_candidates()

    case_0_problem_statement(out)
    case_1_candidate_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_3b_linear_volume_relation(ns, out)
    case_4_minimal_candidate_definition(out)
    case_5_relation_to_1d_toy(out)
    case_6_failure_controls(out)
    case_7_next_tests(out)
    final_interpretation()
    out.print_all()

    ns.record_claim(ClaimRecord(
        claim_id="zeta_volume_strain_candidate",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "zeta = ln sqrt(gamma) is the leading geometric candidate for the vacuum-spacetime "
            "configuration variable. Trace/volume modes change zeta; TT modes preserve zeta "
            "at linear order. This is a linear observation, not a full covariant theorem."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="zeta_must_not_duplicate_A_sector_mass",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "zeta and kappa must not create an exterior 1/r scalar tail or duplicate A-sector "
            "exterior mass. M_ext is determined by A_flux, not by integral zeta."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_zeta_covariant_or_foliation_frame",
        script_id=SCRIPT_ID,
        title="Derive covariant extension or foliation/frame specification for zeta",
        status=ObligationStatus.OPEN,
        description=(
            "zeta = ln sqrt(gamma) depends on spatial metric and foliation. "
            "A frame u^mu or covariant volume current is required before zeta is an observable."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_boundary_exterior_charge_zero_for_zeta",
        script_id=SCRIPT_ID,
        title="Derive boundary/exterior charge zero theorem for zeta",
        status=ObligationStatus.OPEN,
        description=(
            "Show that local volume reconfiguration produces no exterior 1/r scalar tail "
            "and no exterior kappa/zeta charge."
        ),
    ))
    ns.record_derivation(
        derivation_id="volume_form_configuration_variable_marker",
        inputs=[],
        output=sp.Symbol("volume_form_configuration_variable_audited"),
        method="volume_form_configuration_variable_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
