# Group:
#   13_vacuum_substance_accounting
#
# Script type:
#   AUDIT

# Candidate vacuum transport current constraints
#
# Purpose
# -------
# The boundary volume/no-exterior-charge audit found:
#
#   local trace/volume reconfiguration is safe only if:
#     zeta_ext -> 0
#     kappa_ext -> 0
#     Q_volume = 0
#     F_zeta(R+) = 0
#     F_kappa(R+) = 0
#     delta M_ext|volume/kappa = 0
#
# It also introduced a possible divergence/boundary identity:
#
#   integral div J_volume d^3x = surface J_volume dot dS = 0
#
# The next question is:
#
#   If J_v exists, is it local, constrained, or transport?
#
# This script constrains J_v so it does not become an acausal repair current
# or a hidden far-zone scalar-radiation channel.
#
# This is not a derivation.

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
class TransportEntry:
    name: str
    option: str
    allowed_if: str
    forbidden_if: str
    status: str
    missing: str


def build_entries() -> List[TransportEntry]:
    return [
        TransportEntry(
            name="J1: no transport current",
            option="J_v = 0 in ordinary local relaxation",
            allowed_if="conversion is purely local exchange between e_kappa and epsilon_vac_config",
            forbidden_if="used where compensation requires redistribution between regions",
            status="SAFE_IF",
            missing="proof that local exchange alone enforces Q_volume=0",
        ),
        TransportEntry(
            name="J2: compact-support current",
            option="J_v nonzero only inside/near matter support",
            allowed_if="surface flux at exterior boundary vanishes",
            forbidden_if="J_v reaches infinity or sources far-zone scalar flux",
            status="SAFE_IF",
            missing="support law and interface condition",
        ),
        TransportEntry(
            name="J3: constrained redistribution current",
            option="J_v enforces integral compensation with zero exterior flux",
            allowed_if="nonlocality is declared as constraint bookkeeping, not propagation",
            forbidden_if="presented as physical superluminal transport",
            status="CANDIDATE",
            missing="constraint origin and parent projector",
        ),
        TransportEntry(
            name="J4: causal transport current",
            option="J_v obeys a causal evolution/transport law",
            allowed_if="finite speed and stress-energy accounting are specified",
            forbidden_if="it becomes an extra propagating scalar radiation channel",
            status="UNRESOLVED",
            missing="transport law, speed, characteristic structure",
        ),
        TransportEntry(
            name="J5: boundary flux condition",
            option="surface integral J_v dot dS at R+ = 0",
            allowed_if="no vacuum-configuration current leaks into exterior as scalar charge",
            forbidden_if="nonzero exterior boundary flux creates zeta/kappa 1/r tail",
            status="REQUIRED",
            missing="boundary/interface law",
        ),
        TransportEntry(
            name="J6: volume charge conservation",
            option="dQ_volume/dtau + surface flux = source compensation",
            allowed_if="Q_volume remains zero in ordinary isolated systems",
            forbidden_if="ordinary evolution generates nonzero Q_volume",
            status="REQUIRED",
            missing="definition of Q_volume and S_volume",
        ),
        TransportEntry(
            name="J7: exterior vacuum fixed point",
            option="J_v_ext=0, zeta_ext=0, kappa_ext=0",
            allowed_if="ordinary exterior vacuum contains no transport current or volume mode",
            forbidden_if="exterior vacuum carries persistent J_v or volume pressure",
            status="CONSTRAINED",
            missing="exterior stability proof",
        ),
        TransportEntry(
            name="J8: no far-zone scalar energy flux",
            option="F_scalar_far[J_v,zeta,kappa] = 0",
            allowed_if="J_v is local/constrained and not radiative",
            forbidden_if="J_v transports scalar energy to infinity",
            status="REQUIRED",
            missing="radiation/energy flux definition",
        ),
        TransportEntry(
            name="J9: relation to Sigma_exchange",
            option="nabla_mu J_v^mu = Sigma_exchange - Gamma_relax",
            allowed_if="terms are geometric and ordinary Sigma_creation remains zero",
            forbidden_if="Sigma_exchange becomes a free source knob",
            status="CANDIDATE",
            missing="sign conventions, variables, and parent balance",
        ),
        TransportEntry(
            name="J10: relation to A-sector mass",
            option="J_v does not alter A_flux or M_ext",
            allowed_if="vacuum transport is trace/volume bookkeeping only",
            forbidden_if="J_v changes exterior mass coefficient",
            status="CONSTRAINED",
            missing="boundary mass preservation theorem",
        ),
        TransportEntry(
            name="J11: acausal repair current",
            option="J_v instantaneously fixes any mismatch",
            allowed_if="never, unless explicitly derived as a constraint with fixed rule",
            forbidden_if="used as arbitrary repair reservoir/current",
            status="FORBIDDEN",
            missing="not pursued",
        ),
        TransportEntry(
            name="J12: coefficient tuning current",
            option="J_v adjusts alpha_W/K_c, beta_W, C_T, K_T",
            allowed_if="never",
            forbidden_if="used to tune observable coefficients",
            status="FORBIDDEN",
            missing="not pursued",
        ),
    ]


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="boundary_volume_mode_no_exterior_charge_marker",
        upstream_script_id="13_vacuum_substance_accounting__candidate_boundary_volume_mode_no_exterior_charge",
        upstream_derivation_id="boundary_volume_mode_no_exterior_charge_marker",
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


def print_entry(e: TransportEntry) -> None:
    print()
    print("-" * 120)
    print(e.name)
    print("-" * 120)
    print(f"Option: {e.option}")
    print(f"Allowed if: {e.allowed_if}")
    print(f"Forbidden if: {e.forbidden_if}")
    print(f"Status: {e.status}")
    print(f"Missing: {e.missing}")


def case_0_problem_statement(out: ScriptOutput):
    header("Case 0: Vacuum transport current constraints problem")

    print("Question:")
    print()
    print("  If J_v exists, is it local, constrained, or transport?")
    print()
    print("Goal:")
    print()
    print("  constrain J_v so it does not become an acausal repair current or hidden scalar-radiation channel")
    print()
    print("Discipline:")
    print()
    print("  no exterior J_v flux")
    print("  no far-zone scalar energy flux")
    print("  no change to M_ext")
    print("  no Sigma_creation leakage")
    print("  no coefficient tuning")
    print("  nonlocality must be declared as constraint, not physical transport")

    with out.unresolved_obligations():
        out.line("vacuum transport current problem posed", StatusMark.OBLIGATION, "open: J_v class selection and support law required")


def case_1_inventory(entries: List[TransportEntry]):
    header("Case 1: J_v option inventory")
    for entry in entries:
        print_entry(entry)


def case_2_compact_table(entries: List[TransportEntry], out: ScriptOutput):
    header("Case 2: Compact J_v ledger")

    print("| Entry | Option | Status | Forbidden if | Missing |")
    print("|---|---|---|---|---|")
    for e in entries:
        print(
            "| "
            + e.name.replace("|", "/")
            + " | "
            + e.option.replace("|", "/")
            + " | "
            + e.status
            + " | "
            + e.forbidden_if.replace("|", "/")
            + " | "
            + e.missing.replace("|", "/")
            + " |"
        )

    with out.governance_assessments():
        out.line("compact J_v ledger produced", StatusMark.PASS, "ledger complete")


def case_3_status_counts(entries: List[TransportEntry], out: ScriptOutput):
    header("Case 3: Status counts")

    counts = {}
    for e in entries:
        counts[e.status] = counts.get(e.status, 0) + 1

    for status in sorted(counts):
        print(f"{status}: {counts[status]}")

    print()
    print("Interpretation:")
    print("  J_v is safest if absent, compact, or constrained.")
    print("  A causal transport version is possible but unresolved.")
    print("  Acausal repair and coefficient tuning currents are forbidden.")

    with out.governance_assessments():
        out.line("J_v status count produced", StatusMark.PASS, "counts complete")


def case_4_allowed_classes(out: ScriptOutput):
    header("Case 4: Allowed J_v classes")

    print("Allowed or potentially allowed classes:")
    print()
    print("1. J_v = 0:")
    print("   local exchange only.")
    print()
    print("2. Compact J_v:")
    print("   nonzero only inside/near matter support, zero exterior flux.")
    print()
    print("3. Constraint J_v:")
    print("   enforces compensation with no physical propagation claim.")
    print()
    print("4. Causal transport J_v:")
    print("   only if an evolution law and finite speed are derived.")

    with out.governance_assessments():
        out.line("allowed J_v classes stated", StatusMark.DEFER, "candidate route: four allowed classes constrained")


def case_5_forbidden_classes(out: ScriptOutput):
    header("Case 5: Forbidden J_v classes")

    print("Forbidden classes:")
    print()
    print("1. Acausal repair current.")
    print("2. Far-zone scalar-energy current.")
    print("3. Exterior persistent vacuum pressure/current.")
    print("4. Current that changes M_ext.")
    print("5. Current that acts as Sigma_creation in ordinary gravity.")
    print("6. Current that tunes observable coefficients.")
    print("7. Unlabeled nonlocal transport.")

    with out.governance_assessments():
        out.line("forbidden J_v classes stated", StatusMark.PASS, "policy rule: seven forbidden classes")


def case_6_candidate_balance_shape(out: ScriptOutput):
    header("Case 6: Candidate balance shape")

    print("Candidate local/constrained balance skeleton:")
    print()
    print("  u^mu nabla_mu epsilon_vac_config + nabla_mu J_v^mu")
    print("    = Sigma_exchange - Gamma_relax")
    print()
    print("Ordinary closed conditions:")
    print()
    print("  Sigma_creation = 0")
    print("  surface J_v dot dS at exterior = 0")
    print("  Q_volume = 0")
    print("  delta M_ext = 0")
    print("  F_scalar_far = 0")
    print()
    print("This is a balance skeleton, not a derived equation.")

    with out.governance_assessments():
        out.line("candidate J_v balance skeleton stated", StatusMark.DEFER, "candidate route: skeleton only, not derived")


def case_7_next_tests(out: ScriptOutput):
    header("Case 7: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_vacuum_transport_current_constraints.md")
    print("   Artifact for this script.")
    print()
    print("2. candidate_vacuum_accounting_parent_balance.py")
    print("   Write a more concrete vacuum-substance accounting balance.")
    print()
    print("3. candidate_boundary_volume_mode_no_exterior_charge_refinement.py")
    print("   Refine theorem using J_v classes.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_vacuum_accounting_parent_balance.py")
    print()
    print("Reason:")
    print("  J_v classes are now constrained enough to write the first concrete accounting balance skeleton.")

    with out.governance_assessments():
        out.line("next test selected", StatusMark.PASS, "vacuum accounting parent balance")


def final_interpretation():
    header("Final interpretation")

    print("J_v is allowed only as:")
    print()
    print("  absent/local exchange")
    print("  compact support current")
    print("  constraint redistribution with zero exterior flux")
    print("  causal transport if separately derived")
    print()
    print("J_v is forbidden as:")
    print()
    print("  acausal repair current")
    print("  far-zone scalar radiation current")
    print("  coefficient tuning knob")
    print("  exterior mass-changing current")
    print()
    print("Possible next artifact:")
    print("  candidate_vacuum_transport_current_constraints.md")
    print()
    print("Possible next script:")
    print("  candidate_vacuum_accounting_parent_balance.py")


def main():
    header("Candidate Vacuum Transport Current Constraints")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()
    entries = build_entries()

    case_0_problem_statement(out)
    case_1_inventory(entries)
    case_2_compact_table(entries, out)
    case_3_status_counts(entries, out)
    case_4_allowed_classes(out)
    case_5_forbidden_classes(out)
    case_6_candidate_balance_shape(out)
    case_7_next_tests(out)
    final_interpretation()

    ns.record_claim(ClaimRecord(
        claim_id="J_v_acausal_coefficient_tuning_forbidden",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.POLICY_RULE,
        statement=(
            "J_v as an acausal repair current (J11) or as a coefficient-tuning current (J12) "
            "is forbidden. Nonlocality in J_v must be declared as constraint bookkeeping, not physical transport. "
            "J_v must not alter A_flux, M_ext, or observable coefficients."
        ),
    ))
    ns.record_claim(ClaimRecord(
        claim_id="J_v_allowed_classes_constrained",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.CANDIDATE_ROUTE,
        statement=(
            "J_v is allowed as: absent/zero (J1), compact-support (J2), constrained redistribution (J3), "
            "or causal transport if separately derived (J4). "
            "All cases require zero exterior flux (J5) and zero far-zone scalar energy flux (J8)."
        ),
    ))
    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_J_v_class_and_support_law",
        script_id=SCRIPT_ID,
        title="Derive J_v class and support law",
        status=ObligationStatus.OPEN,
        description=(
            "Select the J_v class (absent, compact, constrained, or causal) "
            "and derive the support/interface law that enforces zero exterior flux and zero Q_volume."
        ),
    ))
    ns.record_derivation(
        derivation_id="vacuum_transport_current_constraints_marker",
        inputs=[],
        output=sp.Symbol("vacuum_transport_current_constraints_audited"),
        method="vacuum_transport_current_constraints_audit",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
