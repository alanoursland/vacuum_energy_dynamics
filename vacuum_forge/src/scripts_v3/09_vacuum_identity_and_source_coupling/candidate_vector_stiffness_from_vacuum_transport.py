# Candidate vector stiffness from vacuum transport
#
# Group:
#   09_vacuum_identity_and_source_coupling
#
# Script type:
#   AUDIT
#
# Purpose
# -------
# The vector coefficient normalization study found:
#
#   source object j_i = rho v_i          -> constrained by continuity
#   vector equation Delta W_i ~ j_i      -> plausible reduced form
#   vector coefficient alpha_W/K_W       -> missing
#
# This script asks whether K_W can be motivated from a vacuum-transport
# energy rather than inserted to match frame dragging.
#
# It does NOT derive Lense-Thirring.
# It does NOT set K_W to a GR value.
#
# It tests three possibilities:
#
#   1. shared stiffness: K_W = K_A
#   2. independent transport stiffness: K_W != K_A but ontology-justified
#   3. missing/phenomenological stiffness

from pathlib import Path

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


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="vector_coefficient_normalization_marker",
        upstream_script_id="09_vacuum_identity_and_source_coupling__candidate_vector_coefficient_normalization",
        upstream_derivation_id="vector_coefficient_normalization_marker",
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


def case_0_problem_statement():
    header("Case 0: Vector stiffness from vacuum transport problem")

    print("Problem:")
    print()
    print("  W_i has a continuity-constrained source j_i = rho v_i,")
    print("  but its stiffness K_W is missing.")
    print()
    print("Question:")
    print()
    print("  Does vacuum transport suggest a vector stiffness K_W?")
    print()
    print("Allowed outcomes:")
    print()
    print("  K_W related to scalar stiffness K_A")
    print("  K_W independent but ontology-justified")
    print("  K_W missing / phenomenological")


def case_1_scalar_energy_reference():
    header("Case 1: Scalar exchange energy reference")

    K_A, x = sp.symbols("K_A x", positive=True, real=True)
    A = sp.Function("A")(x)

    E_A_density = K_A * sp.diff(A, x)**2

    print("Scalar reduced energy density:")
    print()
    print("  E_A ~ K_A |grad A|^2")
    print()
    print(f"1D form = {E_A_density}")
    print()
    print("K_A measures scalar exchange stiffness.")

    return E_A_density


def case_2_vector_transport_energy():
    header("Case 2: Candidate vector transport energy")

    K_W, x = sp.symbols("K_W x", positive=True, real=True)
    W = sp.Function("W")(x)

    E_W_density = K_W * sp.diff(W, x)**2

    print("Candidate vector transport energy density:")
    print()
    print("  E_W ~ K_W |grad W_i|^2")
    print()
    print(f"1D schematic = {E_W_density}")
    print()
    print("If varied with source alpha_W j_i W_i, this yields:")
    print()
    print("  Delta W_i ~ - (alpha_W/K_W) j_i")
    print()
    print("But K_W is not yet derived.")

    return E_W_density


def case_3_shared_stiffness_option():
    header("Case 3: Shared scalar/vector stiffness option")

    K_A, K_W, lambda_K = sp.symbols("K_A K_W lambda_K", positive=True, real=True)

    relation = sp.Eq(K_W, lambda_K*K_A)

    print("Shared-stiffness parameterization:")
    print()
    print(f"{relation}")
    print()
    print("Special case:")
    print()
    print("  lambda_K = 1 gives K_W = K_A")
    print()
    print("Interpretation:")
    print("  scalar exchange and vector transport are two modes of the same vacuum")
    print("  stiffness only if lambda_K is derived or fixed by ontology.")

    return relation


def case_4_independent_transport_stiffness():
    header("Case 4: Independent vector transport stiffness option")

    print("Independent option:")
    print()
    print("  K_W is a distinct vector-transport stiffness.")
    print()
    print("This may be legitimate if the ontology says:")
    print()
    print("  scalar compression/exchange and vector circulation/transport cost")
    print("  different vacuum energies.")
    print()
    print("But if K_W is introduced only to fit frame dragging, that is hand matching.")


def case_5_curl_energy_option():
    header("Case 5: Curl-energy option")

    print("A more gauge-aware vector energy may use:")
    print()
    print("  E_W ~ K_c |curl W|^2")
    print()
    print("rather than:")
    print()
    print("  E_W ~ K_W |grad W|^2")
    print()
    print("Reason:")
    print("  curl W removes pure-gradient gauge-like pieces.")
    print()
    print("Open issue:")
    print("  variation of |curl W|^2 gives a transverse vector equation,")
    print("  but gauge fixing and boundary conditions are needed.")


def case_6_source_coupling_energy():
    header("Case 6: Source coupling energy")

    alpha_W, j, W = sp.symbols("alpha_W j W", real=True)

    source_term = alpha_W*j*W

    print("Candidate source coupling:")
    print()
    print("  E_source ~ alpha_W j_i W_i")
    print()
    print(f"1D symbolic term = {source_term}")
    print()
    print("Interpretation:")
    print("  alpha_W controls how matter current exchanges with vector vacuum transport.")
    print()
    print("Missing:")
    print("  alpha_W is no more derived than K_W.")

    return source_term


def case_7_dimensionless_ratio():
    header("Case 7: Dimensionless stiffness/coupling ratio")

    alpha_W, K_W = sp.symbols("alpha_W K_W", positive=True, real=True)

    ratio = alpha_W/K_W

    print("Only the ratio enters the reduced source equation:")
    print()
    print("  Delta W_i = - (alpha_W/K_W) j_i")
    print()
    print(f"ratio = {ratio}")
    print()
    print("Therefore deriving K_W alone is not enough.")
    print("Need either:")
    print()
    print("  alpha_W and K_W separately")
    print("  or their ratio directly")

    return ratio


def case_8_classification():
    header("Case 8: Classification")

    print("| Option | Status |")
    print("|---|---|")
    print("| vector transport energy K_W | CONSTRAINED_BY_IDENTITY |")
    print("| K_W = K_A | CONSTRAINED_BY_IDENTITY if lambda_K derived |")
    print("| independent K_W | INDEPENDENT_STIFFNESS if ontology-justified |")
    print("| curl-energy K_c | CONSTRAINED_BY_IDENTITY, gauge-aware option |")
    print("| source coupling alpha_W | MISSING |")
    print("| coefficient alpha_W/K_W | MISSING |")
    print("| GR normalization inserted directly | HAND_ASSIGNED / RISK |")


def case_9_next_tests():
    header("Case 9: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_vector_curl_energy_field_equation.py")
    print("   Derive the Euler-Lagrange equation from |curl W|^2 + j.W.")
    print()
    print("2. candidate_kappa_source_law_from_trace_exchange.py")
    print("   Work the missing kappa source sector.")
    print()
    print("3. candidate_tensor_source_from_exchange_identity.py")
    print("   Work the hand-assigned tensor coupling.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_vector_curl_energy_field_equation.py")


def final_interpretation():
    header("Final interpretation")

    print("Vacuum transport motivates a vector energy, but not yet a coefficient.")
    print()
    print("Promising path:")
    print()
    print("  E_W ~ K_c |curl W|^2 + alpha_W j_i W_i")
    print()
    print("because curl W is more gauge-aware than raw W_i.")
    print()
    print("But:")
    print()
    print("  K_c is missing")
    print("  alpha_W is missing")
    print("  alpha_W/K_c is missing")
    print()
    print("Possible next artifact:")
    print("  candidate_vector_stiffness_from_vacuum_transport.md")
    print()
    print("Possible next script:")
    print("  candidate_vector_curl_energy_field_equation.py")


def main():
    header("Candidate Vector Stiffness From Vacuum Transport")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_problem_statement()
    E_A = case_1_scalar_energy_reference()
    E_W = case_2_vector_transport_energy()
    shared_relation = case_3_shared_stiffness_option()
    case_4_independent_transport_stiffness()
    case_5_curl_energy_option()
    source_term = case_6_source_coupling_energy()
    ratio = case_7_dimensionless_ratio()
    case_8_classification()
    case_9_next_tests()
    final_interpretation()

    out = ScriptOutput()

    with out.governance_assessments():
        out.line(
            "scalar stiffness K_A as reference",
            StatusMark.PASS,
            "E_A ~ K_A |grad A|^2 provides scalar reference",
        )
        out.line(
            "vector stiffness K_W",
            StatusMark.FAIL,
            "K_W not derived; curl-energy K_c is better gauge-aware option",
        )
        out.line(
            "source coupling alpha_W",
            StatusMark.FAIL,
            "alpha_W not derived; ratio alpha_W/K_W fully missing",
        )
        out.line(
            "GR normalization matching",
            StatusMark.DEFER,
            "forbidden at this stage; must derive from vacuum transport action",
        )

    with out.unresolved_obligations():
        out.line(
            "derive vector coefficient alpha_W / K_c",
            StatusMark.OBLIGATION,
            "open proof obligation recorded",
        )
        out.line(
            "derive global boundary normalization",
            StatusMark.OBLIGATION,
            "open proof obligation recorded",
        )

    out.print()

    with archive.open() as ns2:
        # Proof obligation: vector coefficient (alpha_W/K_c is the ratio after curl-energy)
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_vector_coefficient_alpha_W_K_c",
            script_id=SCRIPT_ID,
            title="Derive vector coefficient alpha_W / K_c",
            status=ObligationStatus.OPEN,
            description=(
                "The vector source equation Delta W_i ~ (alpha_W/K_c) j_i requires "
                "the ratio alpha_W/K_c to be derived from the vacuum transport action. "
                "Neither alpha_W nor K_c is currently derived."
            ),
        ))

        # Proof obligation: global boundary normalization
        ns2.record_obligation(ProofObligationRecord(
            obligation_id="derive_global_boundary_normalization",
            script_id=SCRIPT_ID,
            title="Derive global boundary normalization",
            status=ObligationStatus.OPEN,
            description=(
                "The boundary/far-field coefficient for the vector sector is controlled "
                "by alpha_W/K_c plus source geometry. The absolute normalization is missing "
                "until the action ratio is derived."
            ),
        ))

        # Governance claim: no recovery smuggling for K_W
        ns2.record_claim(ClaimRecord(
            claim_id="no_recovery_smuggling_K_W",
            script_id=SCRIPT_ID,
            claim_kind=RecordKind.GOVERNANCE_CLAIM,
            tier=ClaimTier.CONSTRAINED,
            status=GovernanceStatus.POLICY_RULE,
            statement=(
                "K_W and alpha_W must not be chosen to reproduce the Lense-Thirring "
                "frame-dragging coefficient. Deriving K_W from frame-dragging matching "
                "is recovery smuggling, not ontology work."
            ),
            reason_code=ReasonCode.RECOVERY_SELECTED_PARAMETER,
        ))

        # Inventory marker
        ns2.record_derivation(
            derivation_id="vector_stiffness_from_vacuum_transport_marker",
            inputs=[],
            output=sp.Symbol("vector_transport_stiffness_options_classified"),
            method="vector_stiffness_from_vacuum_transport_inventory",
            status=Status.DERIVED,
            record_kind=RecordKind.INVENTORY_MARKER,
            is_placeholder=True,
        )

        ns2.write_run_metadata()


if __name__ == "__main__":
    main()
