# Group:
#   10_kappa_trace_response
#
# Script type:
#   INVENTORY
#
# Candidate kappa source law from trace exchange
#
# Purpose
# -------
# Group 10 starts by forcing kappa to have one primary role.
#
# Current risk:
#   kappa has been used as trace response, volume response, interior correction,
#   exterior suppression variable, scalar-radiation safety mechanism, and possible
#   relaxation field.
#
# Hypothesis:
#   kappa is primarily a trace / volume response field sourced by stress,
#   pressure, or trace-sector vacuum exchange.
#
# This is not yet a final kappa equation. It is a source-law audit.

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
class KappaSourceCandidate:
    name: str
    candidate_source: str
    status: str
    reason: str
    risk: str


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="vector_source_shape_factor_marker",
        upstream_script_id="009_vacuum_identity_and_source_coupling__candidate_vector_source_shape_factor",
        upstream_derivation_id="vector_source_shape_factor_marker",
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


def print_candidate(c: KappaSourceCandidate) -> None:
    print()
    print("-" * 100)
    print(c.name)
    print("-" * 100)
    print(f"Status: {c.status}")
    print(f"Candidate source: {c.candidate_source}")
    print(f"Reason: {c.reason}")
    print(f"Risk: {c.risk}")


def case_0_problem_statement():
    header("Case 0: Kappa source-law problem")

    print("Question:")
    print()
    print("  What is the primary source law for kappa?")
    print()
    print("Working hypothesis:")
    print()
    print("  kappa is primarily a trace / volume response field.")
    print()
    print("Do not let kappa be a free repair term.")
    print()
    print("Required discipline:")
    print()
    print("  one primary source role first")
    print("  exterior suppression condition")
    print("  gauge-vs-physical distinction")
    print("  scalar-radiation safety")


def case_1_prior_kappa_relation():
    header("Case 1: Prior reduced kappa relation")

    A, B, kappa = sp.symbols("A B kappa", positive=True, real=True)

    relation = sp.Eq(A*B, sp.exp(2*kappa))
    kappa_expr = sp.Eq(kappa, sp.Rational(1, 2)*sp.log(A*B))

    print("Areal/static reduced relation:")
    print()
    print("  AB = exp(2 kappa)")
    print()
    print(relation)
    print()
    print("Equivalent:")
    print()
    print(kappa_expr)
    print()
    print("Exterior Schwarzschild recovery used:")
    print()
    print("  kappa = 0")
    print("  AB = 1")
    print()
    print("This defines a useful reduced diagnostic.")
    print("It does not yet derive a source law.")


def build_candidates() -> List[KappaSourceCandidate]:
    return [
        KappaSourceCandidate(
            name="K1: Density rho as primary kappa source",
            candidate_source="rho",
            status="REJECTED_AS_PRIMARY",
            reason=(
                "rho already sources A_constraint through the areal-flux law. "
                "Using rho again as the primary kappa source risks double-counting "
                "the scalar mass response."
            ),
            risk=(
                "Would make kappa another Newtonian potential unless a distinct "
                "trace/volume mechanism is derived."
            ),
        ),
        KappaSourceCandidate(
            name="K2: Pressure p as primary kappa source",
            candidate_source="p",
            status="PLAUSIBLE",
            reason=(
                "Pressure is absent or weak in exterior vacuum and becomes important "
                "inside matter. This fits kappa as an interior response."
            ),
            risk=(
                "A pressure-only source may miss anisotropic stress and relativistic "
                "trace structure."
            ),
        ),
        KappaSourceCandidate(
            name="K3: Spatial stress trace as primary kappa source",
            candidate_source="T^i_i or sigma^i_i",
            status="PLAUSIBLE",
            reason=(
                "A trace/volume field should plausibly couple to the trace of spatial "
                "stress or compressive vacuum exchange."
            ),
            risk=(
                "Requires a parent stress decomposition and gauge-invariant trace definition."
            ),
        ),
        KappaSourceCandidate(
            name="K4: Relativistic stress-energy trace",
            candidate_source="T = T^mu_mu",
            status="CONSTRAINED_BY_IDENTITY",
            reason=(
                "A scalar trace response should be tested against the relativistic trace. "
                "This connects kappa to source-geometry compatibility more cleanly than "
                "pressure alone."
            ),
            risk=(
                "Trace coupling can create scalar-tensor-like behavior or conflict with "
                "radiation constraints if unsuppressed."
            ),
        ),
        KappaSourceCandidate(
            name="K5: Density gradients / boundary layer source",
            candidate_source="grad rho, boundary jumps, shell terms",
            status="PLAUSIBLE",
            reason=(
                "Kappa may respond at matter/vacuum interfaces or matching layers rather "
                "than to bulk density directly."
            ),
            risk=(
                "Can become an arbitrary matching patch unless derived from variation or "
                "relaxation."
            ),
        ),
        KappaSourceCandidate(
            name="K6: Relaxation source/sink",
            candidate_source="-m_kappa^2 kappa or -Gamma_kappa kappa_dot",
            status="PLAUSIBLE",
            reason=(
                "Exterior suppression of kappa can be represented by a restoring term "
                "driving kappa -> 0 in vacuum."
            ),
            risk=(
                "Relaxation alone does not define what sources kappa inside matter."
            ),
        ),
        KappaSourceCandidate(
            name="K7: Pure gauge / coordinate volume artifact",
            candidate_source="none physical",
            status="RISK",
            reason=(
                "Some kappa-like deviations may be coordinate-volume artifacts in "
                "areal/static reductions."
            ),
            risk=(
                "If kappa is mostly gauge, treating it as a physical field produces "
                "false dynamics."
            ),
        ),
    ]


def case_3_print_candidates(candidates: List[KappaSourceCandidate]):
    header("Case 3: Kappa source candidate inventory")
    for c in candidates:
        print_candidate(c)


def case_4_schematic_equation():
    header("Case 4: Proposed schematic kappa equation")

    r = sp.symbols("r", positive=True, real=True)
    kappa = sp.Function("kappa")(r)
    Kk, ak, mk = sp.symbols("K_k alpha_k m_k", positive=True, real=True)
    S_trace = sp.Function("S_trace")(r)

    lhs = -Kk * (sp.diff(kappa, r, 2) + 2*sp.diff(kappa, r)/r) + mk**2*kappa
    rhs = ak * S_trace
    eq = sp.Eq(lhs, rhs)

    print("Candidate static trace-response equation:")
    print()
    print("  -K_k Delta_areal kappa + m_k^2 kappa = alpha_k S_trace")
    print()
    print("where:")
    print("  S_trace is pressure/stress/trace-sector source")
    print("  m_k^2 kappa provides exterior suppression / relaxation scale")
    print()
    print("Spherical static form:")
    print()
    print(eq)
    print()
    print("Important:")
    print("  This is a candidate template, not a derived law.")


def case_5_exterior_suppression():
    header("Case 5: Exterior suppression condition")

    print("Exterior vacuum target:")
    print()
    print("  rho = 0")
    print("  p = 0")
    print("  stress trace = 0")
    print("  S_trace = 0")
    print()
    print("Desired exterior solution:")
    print()
    print("  kappa -> 0")
    print()
    print("Possible mechanisms:")
    print()
    print("1. Boundary condition: kappa(infinity) = 0")
    print("2. Restoring term: m_k^2 kappa")
    print("3. Constraint projection: kappa is not an independent exterior degree of freedom")
    print("4. Gauge fixing: exterior areal/static gauge sets kappa = 0")
    print()
    print("Need to distinguish physical suppression from gauge choice.")


def case_6_perfect_fluid_trace_candidates():
    header("Case 6: Perfect-fluid trace candidates")

    rho, p, c = sp.symbols("rho p c", real=True)

    T_trace = -rho*c**2 + 3*p
    spatial_trace = 3*p

    print("For a perfect fluid with metric convention (-,+,+,+):")
    print()
    print("  T = T^mu_mu = -rho c^2 + 3p")
    print("  spatial stress trace = T^i_i = 3p")
    print()
    print(f"T = {T_trace}")
    print(f"T^i_i = {spatial_trace}")
    print()
    print("Options:")
    print()
    print("  S_trace = p")
    print("  S_trace = 3p")
    print("  S_trace = T = -rho c^2 + 3p")
    print("  S_trace = T + rho c^2 = 3p")
    print()
    print("Caution:")
    print("  Direct T coupling reintroduces density as a large source.")
    print("  Spatial trace / pressure-like coupling better isolates interior stress response.")


def case_7_density_double_counting_guard():
    header("Case 7: Density double-counting guard")

    print("Guardrail:")
    print()
    print("  rho already sources A_constraint:")
    print()
    print("    Delta_areal A = 8*pi*G rho/c^2")
    print()
    print("Therefore kappa should not be primarily another rho-sourced Newtonian scalar.")
    print()
    print("Allowed density appearances:")
    print()
    print("  through relativistic trace only if parent identity demands it")
    print("  through gradients/boundaries if matching layer demands it")
    print("  through equation-of-state relations p(rho) inside matter")
    print()
    print("Disallowed without derivation:")
    print()
    print("  Delta kappa ~ rho as a second independent mass potential")


def case_8_classification(candidates: List[KappaSourceCandidate]):
    header("Case 8: Classification table")

    print("| Candidate | Source | Status |")
    print("|---|---|---|")
    for c in candidates:
        print(f"| {c.name} | {c.candidate_source} | {c.status} |")

    print()
    print("Current best primary source candidate:")
    print()
    print("  stress/pressure trace, not raw density")
    print()
    print("Current best schematic source:")
    print()
    print("  S_trace ~ T^i_i, p, or trace-sector vacuum exchange")
    print()
    print("Rejected as primary:")
    print()
    print("  raw rho")


def case_9_failure_controls():
    header("Case 9: Failure controls")

    print("This kappa source program fails if:")
    print()
    print("1. kappa is sourced by rho without avoiding double-counting A.")
    print("2. kappa is used as arbitrary interior correction.")
    print("3. kappa is used to suppress scalar radiation without a mechanism.")
    print("4. kappa is treated as physical before gauge artifacts are separated.")
    print("5. exterior kappa=0 is imposed by hand with no suppression/constraint reason.")
    print("6. pressure/stress trace source is chosen only because GR has pressure terms.")


def case_10_next_tests():
    header("Case 10: Next tests")

    print("Possible next scripts:")
    print()
    print("1. candidate_kappa_exterior_suppression_condition.py")
    print("   Test mechanisms that force kappa -> 0 outside matter.")
    print()
    print("2. candidate_kappa_pressure_trace_model.py")
    print("   Build simple interior pressure/stress trace source model.")
    print()
    print("3. candidate_kappa_gauge_vs_physical_trace.py")
    print("   Separate gauge-volume artifact from physical trace response.")
    print()
    print("Recommended next script:")
    print()
    print("  candidate_kappa_exterior_suppression_condition.py")
    print()
    print("Reason:")
    print("  Exterior kappa=0 is required by the strongest reconstructed sector.")


def final_interpretation():
    header("Final interpretation")

    print("Kappa should not be treated as a second density-sourced scalar potential.")
    print()
    print("Current best role:")
    print()
    print("  kappa = trace / volume response")
    print()
    print("Current best source family:")
    print()
    print("  pressure / spatial stress trace / trace-sector vacuum exchange")
    print()
    print("Schematic candidate:")
    print()
    print("  -K_k Delta kappa + m_k^2 kappa = alpha_k S_trace")
    print()
    print("But:")
    print()
    print("  S_trace is not derived")
    print("  K_k is not derived")
    print("  alpha_k is not derived")
    print("  m_k is not derived")
    print("  gauge-vs-physical status is unresolved")
    print()
    print("Possible next artifact:")
    print("  candidate_kappa_source_law_from_trace_exchange.md")
    print()
    print("Possible next script:")
    print("  candidate_kappa_exterior_suppression_condition.py")


def main():
    header("Candidate Kappa Source Law From Trace Exchange")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)

    out = ScriptOutput()

    case_0_problem_statement()
    case_1_prior_kappa_relation()
    candidates = build_candidates()
    case_3_print_candidates(candidates)
    case_4_schematic_equation()
    case_5_exterior_suppression()
    case_6_perfect_fluid_trace_candidates()
    case_7_density_double_counting_guard()
    case_8_classification(candidates)
    case_9_failure_controls()
    case_10_next_tests()
    final_interpretation()

    ns.record_derivation(
        derivation_id="kappa_source_law_from_trace_exchange_marker",
        inputs=[],
        output=sp.Symbol("kappa_trace_source_family_narrowed"),
        method="kappa_source_law_inventory",
        status=Status.DERIVED,
        record_kind=RecordKind.INVENTORY_MARKER,
        is_placeholder=True,
    )

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_kappa_primary_source_law_in_10_kappa_trace",
        script_id=SCRIPT_ID,
        title="Derive primary kappa source law from first principles",
        status=ObligationStatus.OPEN,
        description=(
            "S_trace, K_k, alpha_k, and m_k are all unresolved. "
            "The source family is narrowed to pressure/stress trace but not derived."
        ),
    ))

    ns.record_obligation(ProofObligationRecord(
        obligation_id="derive_kappa_gauge_vs_physical_split_in_10_kappa_trace",
        script_id=SCRIPT_ID,
        title="Derive gauge-vs-physical split for kappa",
        status=ObligationStatus.OPEN,
        description=(
            "Whether kappa is physical or a coordinate-volume artifact in the "
            "areal/static reduction must be established before treating kappa as "
            "a physical trace-response field."
        ),
    ))

    ns.record_claim(ClaimRecord(
        claim_id="kappa_must_not_duplicate_A_sector_density_response",
        script_id=SCRIPT_ID,
        claim_kind=RecordKind.GOVERNANCE_CLAIM,
        tier=ClaimTier.CONSTRAINED,
        status=GovernanceStatus.OPEN_RISK,
        statement=(
            "Kappa must not be primarily sourced by raw density rho, "
            "as rho already sources A_constraint. Using rho as the primary "
            "kappa source risks double-counting the scalar mass response."
        ),
    ))

    with out.governance_assessments():
        out.line("kappa source family narrowed to pressure/stress trace", StatusMark.PASS, "raw rho rejected as primary")
        out.line("K_k coefficient", StatusMark.OBLIGATION, "not derived")
        out.line("alpha_k coupling", StatusMark.OBLIGATION, "not derived")
        out.line("m_k scale", StatusMark.OBLIGATION, "not derived")
        out.line("gauge-vs-physical status", StatusMark.OBLIGATION, "unresolved")

    with out.unresolved_obligations():
        out.line("derive primary kappa source law", StatusMark.OBLIGATION, "open")
        out.line("derive gauge-vs-physical split", StatusMark.OBLIGATION, "open")

    ns.write_run_metadata()


if __name__ == "__main__":
    main()
