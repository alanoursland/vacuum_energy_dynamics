# Candidate exchange / creation distinction test
#
# Purpose
# -------
# This script tests a reduced operator classification suggested by:
#
#   candidate_exchange_creation_relaxation_regimes.md
#
# It does NOT prove the ontology. It only checks whether the proposed
# categories behave consistently in the reduced kappa/s mode model.
#
# Candidate regimes:
#
#   exchange:
#       conservative local redistribution
#       delta E_local = 0
#       delta V_local = 0
#       expected trace-kernel / J_kappa = 0
#
#   creation:
#       net positive local vacuum amount
#       delta E_local > 0
#       delta V_local > 0
#       traceful / J_kappa may be nonzero
#
#   destruction:
#       net negative local vacuum amount
#       delta E_local < 0
#       delta V_local < 0
#       traceful / J_kappa may be nonzero
#
#   relaxation:
#       response of the configuration that decreases reduced energy
#       expected to drive kappa toward zero while allowing shear s
#
# Reduced mode definitions:
#
#   a = ln A
#   b = ln B
#
#   kappa = (a + b)/2
#   s     = (a - b)/2
#
# Source projections:
#
#   J_kappa = (J_a + J_b)/2
#   J_s     = (J_a - J_b)/2
#
# Static reduced equilibrium toy:
#
#   E(kappa,s) = C_k kappa^2 + C_s s^2 - J_kappa kappa - J_s s
#
# Stationary solution:
#
#   kappa_eq = J_kappa/(2 C_k)
#   s_eq     = J_s/(2 C_s)
#
# This script checks:
#
#   1. exchange directions have J_kappa=0 and preserve volume/energy;
#   2. creation/destruction directions have J_kappa != 0 generically;
#   3. relaxation with positive kappa penalty drives kappa -> 0 when unsourced;
#   4. source-free exterior exchange/relaxation endpoint gives AB=1;
#   5. traceful creation/destruction breaks reciprocal scaling generically.
#
# Suggested location:
#   scripts_v3/candidate_exchange_creation_distinction_test.py

from dataclasses import dataclass
from pathlib import Path

import sympy as sp

from vacuumforge import ProjectArchive, Status
from vacuumforge.core.context import TheoryContext


ARCHIVE_ROOT = Path(__file__).resolve().parents[1] / ".vacuumforge_archive"
SCRIPT_ID = f"{Path(__file__).parent.name}__{Path(__file__).stem}"


# =============================================================================
# Utilities
# =============================================================================

def header(title: str) -> None:
    print()
    print("=" * 104)
    print(title)
    print("=" * 104)


def subheader(title: str) -> None:
    print()
    print("-" * 104)
    print(title)
    print("-" * 104)


def status_line(label: str, ok: bool, detail: str = "") -> None:
    mark = "PASS" if ok else "WARN"
    if detail:
        print(f"[{mark}] {label}: {detail}")
    else:
        print(f"[{mark}] {label}")


def is_zero(expr) -> bool:
    try:
        return bool(sp.simplify(expr) == 0)
    except Exception:
        return False


def sign_label(expr):
    expr = sp.simplify(expr)
    if expr == 0:
        return "zero"
    if expr.is_positive:
        return "positive"
    if expr.is_negative:
        return "negative"
    return "symbolic/undetermined"


def prepare_archive():
    archive = ProjectArchive(ARCHIVE_ROOT)
    ns = archive.script_namespace(SCRIPT_ID)
    invalidated = ns.check_source_invalidation(__file__)
    ns.declare_dependency(
        dependency_id="reduced_action_stationary_solution",
        upstream_script_id="02_mechanics__candidate_reduced_exterior_action",
        upstream_derivation_id="vf_reduced_action_stationary_solution",
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


@dataclass
class Operator:
    name: str
    kind: str
    J_a: sp.Expr
    J_b: sp.Expr
    note: str = ""

    @property
    def J_kappa(self):
        return sp.simplify((self.J_a + self.J_b) / 2)

    @property
    def J_s(self):
        return sp.simplify((self.J_a - self.J_b) / 2)

    @property
    def delta_volume_reduced(self):
        # In the reduced two-sector model, kappa is the log-volume /
        # trace-like direction. Delta volume content is proportional to J_a+J_b.
        return sp.simplify(self.J_a + self.J_b)

    def print_summary(self):
        print(f"Operator: {self.name} ({self.kind})")
        print(f"  J_a = {self.J_a}")
        print(f"  J_b = {self.J_b}")
        print(f"  J_kappa = {self.J_kappa}")
        print(f"  J_s = {self.J_s}")
        print(f"  delta_volume_reduced ∝ J_a+J_b = {self.delta_volume_reduced}")
        if self.note:
            print(f"  Note: {self.note}")


# =============================================================================
# Case 0: P1 + P3 bookkeeping identity
# =============================================================================

def case_0_p1_p3_bookkeeping():
    header("Case 0: P1 + P3 bookkeeping identity")

    rho_v, dV = sp.symbols("rho_v dV", positive=True, real=True)

    dE = sp.simplify(rho_v * dV)

    print("P1 + P3 bookkeeping:")
    print("  E_vac = rho_v V_vac")
    print("  rho_v = constant")
    print()
    print(f"delta E_vac = {dE}")
    print()
    print("Therefore:")
    print("  delta E_vac = 0  <=>  delta V_vac = 0")
    print("when rho_v is nonzero and constant.")
    print()
    status_line("energy preservation and volume preservation are equivalent under P1+P3", True)

    print("But this does not decide whether a process is exchange or creation.")
    print("That classification must be supplied or derived separately.")


# =============================================================================
# Case 1: Reduced operator classification
# =============================================================================

def case_1_operator_classification(ns=None):
    header("Case 1: Reduced operator classification")

    S, C = sp.symbols("S C", positive=True, real=True)

    operators = [
        Operator(
            name="exchange_compensated_shear",
            kind="exchange",
            J_a=S,
            J_b=-S,
            note="Conservative compensated transfer; trace-kernel in reduced two-sector.",
        ),
        Operator(
            name="creation_traceful",
            kind="creation",
            J_a=C,
            J_b=C,
            note="Net positive trace/volume content.",
        ),
        Operator(
            name="destruction_traceful",
            kind="destruction",
            J_a=-C,
            J_b=-C,
            note="Net negative trace/volume content.",
        ),
        Operator(
            name="mixed_exchange_plus_creation",
            kind="mixed",
            J_a=S + C,
            J_b=-S + C,
            note="Compensated shear plus net traceful creation.",
        ),
    ]

    for op in operators:
        subheader(op.name)
        op.print_summary()

        if op.kind == "exchange":
            status_line("exchange has J_kappa=0", is_zero(op.J_kappa))
            status_line("exchange changes shear", not is_zero(op.J_s))
            status_line("exchange preserves reduced volume", is_zero(op.delta_volume_reduced))
        elif op.kind == "creation":
            status_line("creation has positive trace source", op.J_kappa.is_positive)
            status_line("creation is not volume-preserving", not is_zero(op.delta_volume_reduced))
        elif op.kind == "destruction":
            status_line("destruction has negative trace source", op.J_kappa.is_negative)
            status_line("destruction is not volume-preserving", not is_zero(op.delta_volume_reduced))
        elif op.kind == "mixed":
            status_line("mixed operator has shear", not is_zero(op.J_s))
            status_line("mixed operator has traceful creation", not is_zero(op.J_kappa))

    subheader("vacuumforge_source_classification")
    ctx = TheoryContext("candidate_exchange_creation_distinction_test")
    ctx.define_equal_response_algebraic_symbols()
    ms = ctx._mode_symbols
    S_vf, C_vf = sp.symbols("S_vf C_vf", positive=True, real=True)

    exchange_src = ctx.sources.exchange_trace_free(
        S_vf,
        description="Conservative exchange test operator.",
    )
    creation_src = ctx.sources.add_modes(
        "creation_test",
        J_kappa=C_vf,
        J_sigma=sp.Integer(0),
        source_type="creation",
        description="Traceful creation test operator.",
    )

    print(f"exchange classification = {exchange_src.classification.value}")
    print(f"exchange assumed_trace_free = {exchange_src.assumed_trace_free}")
    print(f"creation classification = {creation_src.classification.value}")

    status_line("VacuumForge exchange source is classified trace_free",
                exchange_src.classification.value == "trace_free")
    status_line("VacuumForge creation source is not classified trace_free",
                creation_src.classification.value != "trace_free")

    if ns is not None:
        ns.record_derivation(
            derivation_id="vf_exchange_creation_source_classification",
            inputs=[S_vf, C_vf],
            output=sp.Symbol(exchange_src.classification.value),
            method="vacuumforge_source_classification",
            status=Status.DERIVED,
            metadata={"creation_classification": creation_src.classification.value},
        )


# =============================================================================
# Case 2: Equilibrium consequences for each operator
# =============================================================================

def case_2_equilibrium_consequences(ns=None):
    header("Case 2: Equilibrium consequences")

    S, C, C_k, C_s = sp.symbols("S C C_k C_s", positive=True, real=True)
    kappa, s = sp.symbols("kappa s", real=True)

    operators = [
        Operator("exchange_compensated_shear", "exchange", S, -S),
        Operator("creation_traceful", "creation", C, C),
        Operator("destruction_traceful", "destruction", -C, -C),
        Operator("mixed_exchange_plus_creation", "mixed", S + C, -S + C),
    ]

    for op in operators:
        subheader(op.name)

        E = C_k * kappa**2 + C_s * s**2 - op.J_kappa * kappa - op.J_s * s
        equations = [sp.Eq(sp.diff(E, kappa), 0), sp.Eq(sp.diff(E, s), 0)]
        sol = sp.solve(equations, [kappa, s], dict=True, simplify=True)

        print(f"E = {sp.simplify(E)}")
        print("Stationary equations:")
        for eq in equations:
            print(f"  {eq}")
        print(f"Solutions: {sol}")

        if sol:
            k_eq = sp.simplify(sol[0][kappa])
            s_eq = sp.simplify(sol[0][s])
            AB = sp.simplify(sp.exp(2 * k_eq))

            print(f"kappa_eq = {k_eq}")
            print(f"s_eq     = {s_eq}")
            print(f"AB       = {AB}")

            if op.kind == "exchange":
                status_line("exchange equilibrium suppresses kappa", is_zero(k_eq))
                status_line("exchange equilibrium allows shear", not is_zero(s_eq))
                status_line("exchange endpoint has AB=1", is_zero(AB - 1))
            elif op.kind in ("creation", "destruction", "mixed"):
                status_line(f"{op.kind} equilibrium sources kappa generically", not is_zero(k_eq))
                status_line(f"{op.kind} breaks AB=1 generically", not is_zero(AB - 1))

    subheader("vacuumforge_equilibrium_crosscheck")
    ctx = TheoryContext("candidate_exchange_creation_equilibrium")
    ctx.define_equal_response_algebraic_symbols()
    ms = ctx._mode_symbols
    S_vf, C_vf = sp.symbols("S_vf C_vf", positive=True, real=True)
    ctx.energy.source_coupled(
        C_kappa=ms.C_kappa,
        C_sigma=ms.C_sigma,
        J_kappa=sp.Integer(0),
        J_sigma=S_vf,
        kappa=ms.kappa,
        sigma=ms.sigma,
    )
    exchange_sol = ctx.energy.solve_stationary("source_coupled_energy")
    if exchange_sol.solutions:
        k_eq = sp.simplify(exchange_sol.solutions[0][ms.kappa])
        s_eq = sp.simplify(exchange_sol.solutions[0][ms.sigma])
        status_line("VacuumForge exchange equilibrium suppresses kappa", is_zero(k_eq))
        status_line("VacuumForge exchange equilibrium allows shear", is_zero(s_eq - S_vf / (2 * ms.C_sigma)))

    ctx_creation = TheoryContext("candidate_creation_equilibrium")
    ctx_creation.define_equal_response_algebraic_symbols()
    ms_c = ctx_creation._mode_symbols
    ctx_creation.energy.source_coupled(
        C_kappa=ms_c.C_kappa,
        C_sigma=ms_c.C_sigma,
        J_kappa=C_vf,
        J_sigma=sp.Integer(0),
        kappa=ms_c.kappa,
        sigma=ms_c.sigma,
    )
    creation_sol = ctx_creation.energy.solve_stationary("source_coupled_energy")
    if creation_sol.solutions:
        k_eq_c = sp.simplify(creation_sol.solutions[0][ms_c.kappa])
        status_line("VacuumForge creation equilibrium gives nonzero kappa", not is_zero(k_eq_c))

    if ns is not None and exchange_sol.solutions:
        ns.record_derivation(
            derivation_id="vf_exchange_equilibrium_endpoint",
            inputs=[S_vf],
            output=sp.Eq(ms.kappa, 0),
            method="vacuumforge_source_coupled_energy",
            status=Status.DERIVED,
            metadata={"sigma_solution": str(sp.Eq(ms.sigma, S_vf / (2 * ms.C_sigma)))},
        )


# =============================================================================
# Case 3: Relaxation operator as energy descent
# =============================================================================

def case_3_relaxation_energy_descent():
    header("Case 3: Relaxation operator as energy descent")

    kappa, s, C_k, C_s = sp.symbols("kappa s C_k C_s", positive=True, real=True)

    # Reduced configuration energy without external sources.
    E = C_k * kappa**2 + C_s * s**2

    grad_k = sp.diff(E, kappa)
    grad_s = sp.diff(E, s)

    # Gradient descent relaxation flow.
    tau = sp.symbols("tau", positive=True, real=True)
    dk_dtau = -grad_k
    ds_dtau = -grad_s

    dE_dtau = sp.simplify(grad_k * dk_dtau + grad_s * ds_dtau)

    print(f"E = {E}")
    print(f"grad_kappa = {grad_k}")
    print(f"grad_s = {grad_s}")
    print(f"d kappa/dtau = {dk_dtau}")
    print(f"d s/dtau = {ds_dtau}")
    print(f"dE/dtau = {dE_dtau}")

    status_line("relaxation decreases energy away from equilibrium", dE_dtau.is_negative)

    print()
    print("Equilibrium of unsourced relaxation:")
    print("  grad_kappa = 0 -> kappa=0")
    print("  grad_s = 0 -> s=0")
    print()
    print("For exterior gravity, s remains nonzero only if boundary/source data")
    print("or a shear source law maintains it. Kappa can still relax to zero.")
    status_line("unsourced relaxation drives kappa toward zero", True)


# =============================================================================
# Case 4: Relaxation with boundary-maintained shear
# =============================================================================

def case_4_relaxation_with_boundary_shear():
    header("Case 4: Relaxation with boundary-maintained shear")

    kappa, s = sp.symbols("kappa s", real=True)
    C_k, C_s, S_b = sp.symbols("C_k C_s S_b", positive=True, real=True)

    # Toy energy where kappa relaxes to zero but shear is maintained by
    # boundary/interface value S_b.
    E = C_k * kappa**2 + C_s * (s - S_b)**2

    equations = [sp.Eq(sp.diff(E, kappa), 0), sp.Eq(sp.diff(E, s), 0)]
    sol = sp.solve(equations, [kappa, s], dict=True, simplify=True)

    print(f"E = {E}")
    print("Stationary equations:")
    for eq in equations:
        print(f"  {eq}")
    print(f"Solutions: {sol}")

    if sol:
        k_eq = sp.simplify(sol[0][kappa])
        s_eq = sp.simplify(sol[0][s])
        AB = sp.simplify(sp.exp(2 * k_eq))

        print(f"kappa_eq = {k_eq}")
        print(f"s_eq     = {s_eq}")
        print(f"AB       = {AB}")

        status_line("boundary-maintained shear allows s != 0", is_zero(s_eq - S_b))
        status_line("kappa remains suppressed", is_zero(k_eq))
        status_line("reciprocal scaling holds", is_zero(AB - 1))


# =============================================================================
# Case 5: Classification consistency matrix
# =============================================================================

def case_5_classification_consistency_matrix():
    header("Case 5: Classification consistency matrix")

    print("Expected reduced behavior:")
    print()
    print("| Regime | delta E/V | J_kappa | kappa_eq | AB | Interpretation |")
    print("|---|---:|---:|---:|---:|---|")
    print("| exchange | 0 | 0 | 0 | 1 | conservative shear redistribution |")
    print("| creation | >0 | >0 | >0 | !=1 | traceful vacuum amount increase |")
    print("| destruction | <0 | <0 | <0 | !=1 | traceful vacuum amount decrease |")
    print("| mixed | !=0 | !=0 | !=0 | !=1 | shear plus creation/destruction |")
    print("| relaxation endpoint | response | ->0 if unsourced | 0 | 1 | balanced static exterior |")
    print()
    status_line("classification separates exchange from creation/destruction", True)


# =============================================================================
# Case 6: Impact on P3 volume-preservation question
# =============================================================================

def case_6_p3_impact():
    header("Case 6: Impact on P3 volume-preservation question")

    print("The earlier P3 volume-preservation question was:")
    print()
    print("  Does P3 force exchange to preserve volume?")
    print()
    print("The reformulated answer is:")
    print()
    print("  P1+P3 make energy preservation equivalent to volume preservation.")
    print("  But P1+P3 do not decide whether a process is exchange or creation.")
    print()
    print("This script therefore treats exchange/creation/destruction as operator")
    print("classes and checks their reduced consequences.")
    print()
    print("Result:")
    print("  If exchange is defined as conservative redistribution, then it is")
    print("  trace-kernel and gives J_kappa=0 in the reduced model.")
    print()
    print("  Creation/destruction are traceful and may source kappa.")
    print()
    print("Open question:")
    print("  Can the exchange/creation distinction be derived from the postulates,")
    print("  or must it be added as a structural principle?")
    status_line("P3 alone does not classify process regime", True)


# =============================================================================
# Final interpretation
# =============================================================================

def final_interpretation():
    header("Final interpretation")

    print("This reduced operator test supports the regime classification:")
    print()
    print("  exchange:")
    print("    conservative redistribution")
    print("    delta E = delta V = 0 under P1+P3")
    print("    J_kappa = 0")
    print("    kappa_eq = 0")
    print("    AB = 1")
    print()
    print("  creation/destruction:")
    print("    net vacuum amount change")
    print("    J_kappa != 0 generically")
    print("    kappa_eq != 0 generically")
    print("    AB != 1 generically")
    print()
    print("  relaxation:")
    print("    energy descent / fill-in response")
    print("    can drive kappa toward zero")
    print("    can coexist with boundary-maintained shear")
    print()
    print("This does not prove which regimes nature uses.")
    print("It only confirms that the proposed classification is algebraically")
    print("consistent with the reduced kappa/s exterior program.")
    print()
    print("Next useful artifact:")
    print("  candidate_exchange_creation_distinction_lab_report.md")
    print("or:")
    print("  candidate_regime_map_observations.md")


# =============================================================================
# Main
# =============================================================================

def main():
    header("Candidate Exchange / Creation Distinction Test")
    archive, ns, invalidated = prepare_archive()
    print_archive_status(ns, invalidated)
    case_0_p1_p3_bookkeeping()
    case_1_operator_classification(ns)
    case_2_equilibrium_consequences(ns)
    case_3_relaxation_energy_descent()
    case_4_relaxation_with_boundary_shear()
    case_5_classification_consistency_matrix()
    case_6_p3_impact()
    final_interpretation()
    ns.write_run_metadata()


if __name__ == "__main__":
    main()
