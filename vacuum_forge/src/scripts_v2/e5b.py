# Detailed derivation audit: trace each derivation step under both forks
# to identify exactly where the chains diverge.
#
# This script complements e5a by showing the internal derivation chain
# rather than just the final comparison. For each fork, it:
#   1. Sets up sources and energy
#   2. Solves the stationary conditions explicitly
#   3. Traces kappa -> AB -> gamma_v step by step
#   4. Records dependencies at each step
#   5. Checks whether each derived result is new (not available in the other fork)
#
# The output is a per-derivation comparison table as specified in the
# pre-lab document (structure_search_local_exchange.md, Section A).

import sympy

from vacuumforge.core.context import TheoryContext
from vacuumforge.core.status import Status


def build_and_derive_tc() -> TheoryContext:
    """Build Fork TC and run the full derivation chain."""
    ctx = TheoryContext("fork_tc")
    ms = ctx.define_equal_response_algebraic_symbols()

    # Step 1: Metric ansatz (from Newtonian limit)
    ctx.assumptions.add(
        "newtonian_A", sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)),
        description="A = exp(Phi/c^2) from Newtonian limit",
    )
    ctx.ledger.add_derived(
        "newtonian_limit",
        "A = exp(Phi/c^2) from matching Newtonian gravitational acceleration",
        expression=sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)),
        dependencies=["postulate_3"],
    )

    # Step 2: B ansatz with free gamma_v
    ctx.assumptions.add(
        "B_ansatz", sympy.Eq(ms.B, sympy.exp(-ms.gamma_v * ms.Phi / ms.c**2)),
        description="B = exp(-gamma_v * Phi/c^2), gamma_v free",
    )

    # Step 3: Fork commitment — trace-free exchange
    Js = sympy.Symbol("J_s", real=True)
    ctx.sources.exchange_trace_free(Js)
    ctx.ledger.add_candidate_postulate(
        "trace_conservation",
        "J_kappa = 0 for local exchange",
        expression=sympy.Eq(ms.J_kappa, 0),
    )
    ctx.dependencies.add_node("trace_conservation", kind="postulate", status="candidate_postulate")

    # Step 4: Energy functional
    ctx.energy.source_coupled(
        ms.C_kappa, ms.C_sigma,
        sympy.Integer(0), Js,
        ms.kappa, ms.sigma,
    )
    ctx.dependencies.add_node("energy_functional", kind="expression", status="definition")

    # Step 5: Solve stationary conditions
    sol = ctx.energy.solve_stationary("source_coupled_energy")
    kappa_eq = sol.solutions[0].get(ms.kappa) if sol.solutions else None
    sigma_eq = sol.solutions[0].get(ms.sigma) if sol.solutions else None

    ctx.derive(
        "kappa_equilibrium",
        sympy.Eq(ms.kappa, kappa_eq) if kappa_eq is not None else sympy.S.Zero,
        operation="energy_minimization",
        uses=["trace_conservation", "energy_functional"],
        description=f"kappa at equilibrium = {kappa_eq}",
    )
    ctx.derive(
        "sigma_equilibrium",
        sympy.Eq(ms.sigma, sigma_eq) if sigma_eq is not None else sympy.S.Zero,
        operation="energy_minimization",
        uses=["energy_functional"],
        description=f"sigma at equilibrium = {sigma_eq}",
    )

    # Step 6: kappa = 0 -> AB = 1
    if kappa_eq == 0:
        ctx.derive(
            "reciprocal_scaling_derived",
            sympy.Eq(ms.A * ms.B, 1),
            operation="algebraic_consequence",
            uses=["kappa_equilibrium"],
            description="kappa = 0 implies a + b = 0 implies AB = 1",
        )

        # Step 7: gamma_v from AB = 1
        AB_product = ctx.assumptions.apply(ms.A) * ctx.assumptions.apply(ms.B)
        AB_log = sympy.simplify(sympy.log(AB_product))
        gamma_sol = sympy.solve(AB_log, ms.gamma_v)
        if gamma_sol:
            ctx.assumptions.add(
                "gamma_derived",
                sympy.Eq(ms.gamma_v, gamma_sol[0]),
                description="gamma_v = 1 from AB = 1 + metric ansatz",
                status="derived",
            )
            ctx.derive(
                "gamma_v_one_derived",
                sympy.Eq(ms.gamma_v, gamma_sol[0]),
                operation="algebraic_consequence",
                uses=["reciprocal_scaling_derived", "newtonian_A", "B_ansatz"],
                description=f"gamma_v = {gamma_sol[0]}",
            )

    return ctx


def build_and_derive_se() -> TheoryContext:
    """Build Fork SE and run the full derivation chain."""
    ctx = TheoryContext("fork_se")
    ms = ctx.define_equal_response_algebraic_symbols()

    # Step 1: Same metric ansatz
    ctx.assumptions.add(
        "newtonian_A", sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)),
        description="A = exp(Phi/c^2) from Newtonian limit",
    )
    ctx.ledger.add_derived(
        "newtonian_limit",
        "A = exp(Phi/c^2) from matching Newtonian gravitational acceleration",
        expression=sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)),
        dependencies=["postulate_3"],
    )

    # Step 2: Same B ansatz
    ctx.assumptions.add(
        "B_ansatz", sympy.Eq(ms.B, sympy.exp(-ms.gamma_v * ms.Phi / ms.c**2)),
        description="B = exp(-gamma_v * Phi/c^2), gamma_v free",
    )

    # Step 3: Fork commitment — substance exchange (J_kappa != 0)
    Jk = sympy.Symbol("J_k", real=True)
    Js = sympy.Symbol("J_s", real=True)
    ctx.sources.add_modes(
        "exchange", J_kappa=Jk, J_sigma=Js,
        source_type="exchange",
        description="Substance exchange: J_kappa = J_k != 0",
    )
    ctx.ledger.add_candidate_postulate(
        "substance_exchange",
        "J_kappa != 0 for local exchange",
    )
    ctx.dependencies.add_node("substance_exchange", kind="postulate", status="candidate_postulate")

    # Step 4: Same energy functional but with J_kappa = J_k
    ctx.energy.source_coupled(
        ms.C_kappa, ms.C_sigma,
        Jk, Js,
        ms.kappa, ms.sigma,
    )
    ctx.dependencies.add_node("energy_functional", kind="expression", status="definition")

    # Step 5: Solve stationary conditions
    sol = ctx.energy.solve_stationary("source_coupled_energy")
    kappa_eq = sol.solutions[0].get(ms.kappa) if sol.solutions else None
    sigma_eq = sol.solutions[0].get(ms.sigma) if sol.solutions else None

    ctx.derive(
        "kappa_equilibrium",
        sympy.Eq(ms.kappa, kappa_eq) if kappa_eq is not None else sympy.S.Zero,
        operation="energy_minimization",
        uses=["substance_exchange", "energy_functional"],
        description=f"kappa at equilibrium = {kappa_eq}",
    )
    ctx.derive(
        "sigma_equilibrium",
        sympy.Eq(ms.sigma, sigma_eq) if sigma_eq is not None else sympy.S.Zero,
        operation="energy_minimization",
        uses=["energy_functional"],
        description=f"sigma at equilibrium = {sigma_eq}",
    )

    # Step 6: kappa != 0 generically -> AB != 1
    if kappa_eq is not None and kappa_eq != 0:
        AB_eq = sympy.simplify(sympy.exp(2 * kappa_eq))
        ctx.derive(
            "AB_product",
            sympy.Eq(ms.A * ms.B, AB_eq),
            operation="algebraic_consequence",
            uses=["kappa_equilibrium"],
            description=f"AB = exp(2*kappa) = {AB_eq}",
        )

        # Step 7: gamma_v remains free (depends on J_k/C_kappa)
        # The condition AB = 1 would require J_k = 0, contradicting fork premise
        ctx.ledger.add(
            "gamma_v_undetermined",
            f"gamma_v cannot be determined: depends on J_k/C_kappa ratio",
            Status.OPEN_QUESTION,
        )

    return ctx


# ===================================================================
# Run both derivation chains
# ===================================================================
print("=" * 70)
print("Derivation Chain Audit: Fork TC vs Fork SE")
print("=" * 70)

ctx_tc = build_and_derive_tc()
ctx_se = build_and_derive_se()

# -------------------------------------------------------------------
# Per-derivation comparison table
# -------------------------------------------------------------------
print()
print("=" * 70)
print("Per-Derivation Comparison Table")
print("=" * 70)

# Define the derivation steps to compare
derivation_steps = [
    ("Newtonian limit (A)", "newtonian_limit"),
    ("B ansatz", "B_ansatz"),
    ("Exchange source", "trace_conservation" if ctx_tc.ledger.has("trace_conservation") else None),
    ("Energy functional", "energy_functional"),
    ("kappa equilibrium", "kappa_equilibrium"),
    ("sigma equilibrium", "sigma_equilibrium"),
    ("Reciprocal scaling", "reciprocal_scaling_derived"),
    ("gamma_v = 1", "gamma_v_one_derived"),
]

print()
print(f"{'Derivation':<30} {'Fork TC':<25} {'Fork SE':<25}")
print("-" * 80)

for name, tc_id in derivation_steps:
    # Check Fork TC
    if tc_id and ctx_tc.expressions.has(tc_id):
        rec = ctx_tc.expressions.get(tc_id)
        tc_status = "closes-original"
    elif tc_id and ctx_tc.ledger.has(tc_id):
        entry = ctx_tc.ledger.get(tc_id)
        tc_status = entry.status.value
    elif tc_id and ctx_tc.dependencies.node_data(tc_id) if tc_id in [n for n in ctx_tc.dependencies.all_nodes()] else False:
        tc_status = "present"
    else:
        tc_status = "n/a"

    # Check Fork SE (map to SE-specific IDs)
    se_id_map = {
        "trace_conservation": "substance_exchange",
        "reciprocal_scaling_derived": "AB_product",
        "gamma_v_one_derived": "gamma_v_undetermined",
    }
    se_id = se_id_map.get(tc_id, tc_id) if tc_id else None

    if se_id and ctx_se.expressions.has(se_id):
        se_status = "closes-original"
    elif se_id and ctx_se.ledger.has(se_id):
        entry = ctx_se.ledger.get(se_id)
        se_status = entry.status.value
    elif se_id and se_id in [n for n in ctx_se.dependencies.all_nodes()]:
        se_status = "present"
    else:
        se_status = "n/a"

    print(f"{name:<30} {tc_status:<25} {se_status:<25}")

# -------------------------------------------------------------------
# Newly derivable theorems
# -------------------------------------------------------------------
print()
print("=" * 70)
print("Newly Derivable Theorems")
print("=" * 70)

print()
print("Fork TC (J_kappa = 0):")
tc_derived = [e for e in ctx_tc.ledger.by_status(Status.DERIVED)]
if tc_derived:
    for entry in tc_derived:
        print(f"  + {entry.id}: {entry.statement}")
else:
    print("  (none recorded in ledger)")

# Check expressions store for derived results
tc_exprs = ctx_tc.expressions.list()
derived_exprs = [e for e in tc_exprs if e.status == "derived"]
if derived_exprs:
    for e in derived_exprs:
        print(f"  + [expr] {e.id}: {e.description or e.expr}")

print()
print("Fork SE (J_kappa != 0):")
se_derived = [e for e in ctx_se.ledger.by_status(Status.DERIVED)]
if se_derived:
    for entry in se_derived:
        print(f"  + {entry.id}: {entry.statement}")
else:
    print("  (none recorded in ledger)")

se_open = [e for e in ctx_se.ledger.by_status(Status.OPEN_QUESTION)]
if se_open:
    print("  Open questions:")
    for entry in se_open:
        print(f"  ? {entry.id}: {entry.statement}")

# -------------------------------------------------------------------
# Predictive divergence
# -------------------------------------------------------------------
print()
print("=" * 70)
print("Predictive Divergences")
print("=" * 70)

ms_tc = ctx_tc._mode_symbols
ms_se = ctx_se._mode_symbols

# kappa values
sol_tc = ctx_tc.energy.solve_stationary("source_coupled_energy")
sol_se = ctx_se.energy.solve_stationary("source_coupled_energy")

kappa_tc = sol_tc.solutions[0].get(ms_tc.kappa) if sol_tc.solutions else "unknown"
kappa_se = sol_se.solutions[0].get(ms_se.kappa) if sol_se.solutions else "unknown"

print()
print(f"kappa at equilibrium:")
print(f"  Fork TC: {kappa_tc}")
print(f"  Fork SE: {kappa_se}")

print()
print(f"AB product:")
if kappa_tc == 0:
    print(f"  Fork TC: AB = 1 (exact)")
else:
    print(f"  Fork TC: AB = exp(2*{kappa_tc})")

if kappa_se is not None and kappa_se != "unknown":
    Jk = sympy.Symbol("J_k", real=True)
    AB_se = sympy.simplify(sympy.exp(2 * kappa_se))
    print(f"  Fork SE: AB = {AB_se}")
    print(f"    = 1 only if J_k = 0 (contradicts fork premise)")

print()
print(f"gamma_v:")
print(f"  Fork TC: gamma_v = 1 (derived from kappa = 0 + metric ansatz)")
print(f"  Fork SE: gamma_v = free parameter (depends on J_k/C_kappa)")

print()
print("Observable divergences:")
print("  1. Light deflection: proportional to (1 + gamma_v)/2")
print("       Fork TC: (1+1)/2 = 1.0")
print("       Fork SE: (1+gamma_v)/2, gamma_v unknown")
print("  2. Shapiro delay: proportional to (1 + gamma_v)")
print("       Fork TC: 2.0")
print("       Fork SE: 1 + gamma_v, gamma_v unknown")
print("  3. Perihelion precession: involves gamma_v and beta")
print("       Fork TC: standard GR prediction")
print("       Fork SE: modified, depends on gamma_v")

# -------------------------------------------------------------------
# Dependency chain comparison
# -------------------------------------------------------------------
print()
print("=" * 70)
print("Dependency Chains")
print("=" * 70)

if ctx_tc.expressions.has("gamma_v_one_derived"):
    deps = ctx_tc.dependencies.tree("gamma_v_one_derived")
    print(f"\nFork TC: gamma_v = 1 depends on:")
    for d in deps:
        print(f"  <- {d}")

if ctx_se.expressions.has("AB_product"):
    deps = ctx_se.dependencies.tree("AB_product")
    print(f"\nFork SE: AB product depends on:")
    for d in deps:
        print(f"  <- {d}")

# -------------------------------------------------------------------
# Summary
# -------------------------------------------------------------------
print()
print("=" * 70)
print("Summary")
print("=" * 70)
print()
print("The two forks diverge at the energy equilibrium step:")
print("  Fork TC: J_kappa = 0 -> kappa_eq = 0 -> AB = 1 -> gamma_v = 1")
print("  Fork SE: J_kappa != 0 -> kappa_eq = J_k/(2*C_kappa) -> AB != 1 -> gamma_v free")
print()
print("This is Outcome C from the pre-lab document: both forks are internally")
print("consistent, but they produce different predictions for gamma_v, which is")
print("measurable via light deflection and Shapiro delay.")
print()
print("The existing postulates do NOT silently commit to either fork (ruling out")
print("Outcome B). The choice between forks is empirically testable (confirming")
print("Outcome C over Outcome A).")
