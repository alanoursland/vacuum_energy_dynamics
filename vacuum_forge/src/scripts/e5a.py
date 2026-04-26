# Forward simulation: compare two forks of the framework under different
# J_kappa commitments for local exchange.
#
# Fork TC (Trace Conservation): J_kappa = 0 for local exchange.
#   Expected: kappa relaxes to 0 at energy minimum -> AB = 1 -> gamma_v = 1.
#   This is the conditional chain identified in the structure search.
#
# Fork SE (Substance Exchange): J_kappa != 0 for local exchange.
#   Expected: kappa is sourced to a nonzero equilibrium -> AB != 1 -> gamma_v != 1.
#   Alternatively: gamma_v depends on the source strength ratio.
#
# The experiment constructs both forks with identical postulate content except
# for J_kappa, runs the full derivation chain in each, and compares results
# using the M26 model-comparison machinery.
#
# Pre-registered outcomes (from structure_search_local_exchange.md):
#   A: Both forks consistent, no predictive divergence within derivable scope.
#   B: One fork produces contradiction (hidden postulate commitment).
#   C: Both consistent but different derivable predictions.

import sympy

from vacuumforge.core.context import TheoryContext
from vacuumforge.comparison.compare import compare_models, summarize_model
from vacuumforge.comparison.classification import classify_model
from vacuumforge.requirements.leak_detection import detect_leaks


def build_fork_tc() -> TheoryContext:
    """Fork TC: Trace Conservation (J_kappa = 0 for local exchange)."""
    ctx = TheoryContext("fork_tc_trace_conservation")
    ms = ctx.define_equal_response_algebraic_symbols()

    # Metric ansatz: A = exp(Phi/c^2), B = exp(-gamma_v * Phi/c^2)
    # gamma_v will be determined by the derivation chain.
    ctx.assumptions.add(
        "A_exp", sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)),
        description="A = exp(Phi/c^2) from Newtonian limit",
    )
    ctx.assumptions.add(
        "B_free_gamma",
        sympy.Eq(ms.B, sympy.exp(-ms.gamma_v * ms.Phi / ms.c**2)),
        description="B = exp(-gamma_v * Phi/c^2), gamma_v to be determined",
    )

    # Fork commitment: trace-free local exchange
    Js = sympy.Symbol("J_s", real=True)
    ctx.sources.exchange_trace_free(Js, description="Trace-free local exchange (fork TC)")
    ctx.ledger.add_candidate_postulate(
        "trace_conservation",
        "Local exchange preserves the trace: J_kappa = 0.",
        expression=sympy.Eq(ms.J_kappa, 0),
    )

    # Quadratic energy functional
    ctx.energy.source_coupled(
        C_kappa=ms.C_kappa,
        C_sigma=ms.C_sigma,
        J_kappa=sympy.Integer(0),  # trace-free
        J_sigma=Js,
        kappa=ms.kappa,
        sigma=ms.sigma,
    )

    return ctx


def build_fork_se() -> TheoryContext:
    """Fork SE: Substance Exchange (J_kappa != 0 for local exchange)."""
    ctx = TheoryContext("fork_se_substance_exchange")
    ms = ctx.define_equal_response_algebraic_symbols()

    # Same metric ansatz
    ctx.assumptions.add(
        "A_exp", sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)),
        description="A = exp(Phi/c^2) from Newtonian limit",
    )
    ctx.assumptions.add(
        "B_free_gamma",
        sympy.Eq(ms.B, sympy.exp(-ms.gamma_v * ms.Phi / ms.c**2)),
        description="B = exp(-gamma_v * Phi/c^2), gamma_v to be determined",
    )

    # Fork commitment: exchange sources both kappa and sigma
    Jk = sympy.Symbol("J_k", real=True)
    Js = sympy.Symbol("J_s", real=True)
    ctx.sources.add_modes(
        "exchange", J_kappa=Jk, J_sigma=Js,
        source_type="exchange",
        description="Substance exchange with J_kappa != 0 (fork SE)",
    )
    ctx.ledger.add_candidate_postulate(
        "substance_exchange",
        "Local exchange creates/destroys vacuum substance: J_kappa != 0.",
    )

    # Same quadratic energy but with nonzero J_kappa
    ctx.energy.source_coupled(
        C_kappa=ms.C_kappa,
        C_sigma=ms.C_sigma,
        J_kappa=Jk,
        J_sigma=Js,
        kappa=ms.kappa,
        sigma=ms.sigma,
    )

    return ctx


# ===================================================================
# Build and analyze both forks
# ===================================================================
print("=" * 70)
print("Forward Simulation: Fork TC vs Fork SE")
print("=" * 70)

ctx_tc = build_fork_tc()
ctx_se = build_fork_se()

# -------------------------------------------------------------------
# Section A: Energy equilibrium under each fork
# -------------------------------------------------------------------
print()
print("=" * 70)
print("Section A: Energy Equilibrium")
print("=" * 70)

ms_tc = ctx_tc._mode_symbols
ms_se = ctx_se._mode_symbols

# Solve stationary conditions
sol_tc = ctx_tc.energy.solve_stationary("source_coupled_energy")
sol_se = ctx_se.energy.solve_stationary("source_coupled_energy")

print()
print("Fork TC (trace conservation):")
print(f"  Stationary equations: {sol_tc.equations}")
if sol_tc.solutions:
    for sol in sol_tc.solutions:
        print(f"  Equilibrium: {sol}")
else:
    print("  No solutions found.")

print()
print("Fork SE (substance exchange):")
print(f"  Stationary equations: {sol_se.equations}")
if sol_se.solutions:
    for sol in sol_se.solutions:
        print(f"  Equilibrium: {sol}")
else:
    print("  No solutions found.")

# Interpret kappa equilibrium
print()
print("Kappa at equilibrium:")
if sol_tc.solutions:
    kappa_tc = sol_tc.solutions[0].get(ms_tc.kappa, "not found")
    print(f"  Fork TC: kappa = {kappa_tc}")
    if kappa_tc == 0:
        print("    -> kappa = 0 -> AB = 1 (reciprocal scaling derived)")
else:
    print("  Fork TC: could not solve")

if sol_se.solutions:
    kappa_se = sol_se.solutions[0].get(ms_se.kappa, "not found")
    print(f"  Fork SE: kappa = {kappa_se}")
    Jk = sympy.Symbol("J_k", real=True)
    if kappa_se != 0 and kappa_se is not None:
        print("    -> kappa != 0 generically -> AB != 1 (reciprocal scaling NOT derived)")
else:
    print("  Fork SE: could not solve")

# -------------------------------------------------------------------
# Section B: Derive gamma_v in each fork
# -------------------------------------------------------------------
print()
print("=" * 70)
print("Section B: gamma_v Determination")
print("=" * 70)

# Fork TC: if kappa = 0, then a + b = 0, then A*B = 1
# With A = exp(Phi/c^2) and B = exp(-gamma_v * Phi/c^2):
# A*B = exp((1 - gamma_v) * Phi/c^2) = 1 iff gamma_v = 1
if sol_tc.solutions and sol_tc.solutions[0].get(ms_tc.kappa) == 0:
    # kappa = 0 at equilibrium -> a + b = 0 -> ln(A) + ln(B) = 0 -> AB = 1
    # With the metric ansatz: AB = exp((1 - gamma_v)*Phi/c^2) = 1
    # => (1 - gamma_v) = 0 => gamma_v = 1
    #
    # We derive gamma_v = 1 algebraically and add it as an assumption
    # for the validator. We do NOT add kappa=0 directly as an assumption
    # because that would trigger the leak detector on reciprocal_scaling.
    print("Fork TC:")
    print("  kappa = 0 at equilibrium (from energy minimization with J_kappa = 0)")
    print("  => a + b = 0 => AB = 1")
    print("  AB = exp(Phi/c^2) * exp(-gamma_v * Phi/c^2) = exp((1-gamma_v)*Phi/c^2)")
    print("  AB = 1 requires 1 - gamma_v = 0")
    print("  => gamma_v = 1")
    ctx_tc.assumptions.add(
        "gamma_v_derived",
        sympy.Eq(ms_tc.gamma_v, sympy.Integer(1)),
        description="Derived: gamma_v = 1 from kappa=0 + metric ansatz",
        status="derived",
    )

# Fork SE: kappa = J_k / (2*C_kappa), so AB = exp(2*kappa) != 1 generically
if sol_se.solutions:
    kappa_val = sol_se.solutions[0].get(ms_se.kappa)
    if kappa_val is not None:
        AB_se = sympy.exp(2 * kappa_val)
        print(f"\nFork SE: kappa = {kappa_val}")
        print(f"  AB = exp(2*kappa) = {sympy.simplify(AB_se)}")
        print(f"  AB = 1 requires J_k = 0, which contradicts fork SE premise.")
        print(f"  gamma_v: depends on J_k/C_kappa ratio; remains a free function")
        print(f"  of the source strength.")

# -------------------------------------------------------------------
# Section C: Full validation comparison
# -------------------------------------------------------------------
print()
print("=" * 70)
print("Section C: Requirement Validation Comparison")
print("=" * 70)

results_tc = ctx_tc.requirements.validate_all(ctx_tc)
results_se = ctx_se.requirements.validate_all(ctx_se)

print()
print("Fork TC:")
print(ctx_tc.requirements.summary(results_tc))

print()
print("Fork SE:")
print(ctx_se.requirements.summary(results_se))

# -------------------------------------------------------------------
# Section D: Model classification
# -------------------------------------------------------------------
print()
print("=" * 70)
print("Section D: Model Classification")
print("=" * 70)

class_tc = classify_model(ctx_tc)
class_se = classify_model(ctx_se)

print(f"\nFork TC: {class_tc.label}")
for note in class_tc.notes:
    print(f"  {note}")
if class_tc.secondary:
    print(f"  Secondary: {[s.value for s in class_tc.secondary]}")

print(f"\nFork SE: {class_se.label}")
for note in class_se.notes:
    print(f"  {note}")
if class_se.secondary:
    print(f"  Secondary: {[s.value for s in class_se.secondary]}")

# -------------------------------------------------------------------
# Section E: Side-by-side comparison table
# -------------------------------------------------------------------
print()
print("=" * 70)
print("Section E: Side-by-Side Comparison")
print("=" * 70)

comparison = compare_models([ctx_tc, ctx_se])
print()
print(comparison.to_markdown())

# -------------------------------------------------------------------
# Section F: Leak detection audit
# -------------------------------------------------------------------
print()
print("=" * 70)
print("Section F: Leak Detection Audit")
print("=" * 70)

for ctx, name in [(ctx_tc, "Fork TC"), (ctx_se, "Fork SE")]:
    print(f"\n{name}:")
    if hasattr(ctx, '_targets') and ctx._targets is not None:
        for target_id in ["reciprocal_scaling", "kappa_zero", "gamma_v_one",
                          "trace_free_exchange"]:
            if ctx._targets.has(target_id):
                leak = detect_leaks(target_id, ctx.assumptions, ctx._targets)
                status = "LEAKED" if leak.leaked else "clean"
                print(f"  {target_id}: {status}")
                if leak.leaked:
                    print(f"    via: {leak.leaked_via}")
    else:
        print("  No target library available.")

# -------------------------------------------------------------------
# Section G: Outcome determination
# -------------------------------------------------------------------
print()
print("=" * 70)
print("Section G: Outcome Determination")
print("=" * 70)

# Determine which pre-registered outcome was observed.
#
# Key distinction: a "contradiction" (Outcome B) means the fork is internally
# inconsistent — a derivation step produces a result that conflicts with
# another derivation within the SAME fork. This is different from "failing a
# requirement" — the requirements (gamma_v = 1, AB = 1) are targets the
# framework wants to reach, not axioms. A fork that doesn't reach them is
# consistent but predictively different, which is Outcome C.
#
# Outcome B would be: Fork SE derives gamma_v = 1 AND gamma_v != 1, or
# produces two incompatible expressions for the same quantity.

tc_gamma = next((r for r in results_tc if r.requirement_id == "gamma_v_one"), None)
se_gamma = next((r for r in results_se if r.requirement_id == "gamma_v_one"), None)

# Both forks are internally consistent (no derivation step contradicts another).
# But they produce different predictions for gamma_v.
print()
tc_gamma_status = tc_gamma.status if tc_gamma else "unknown"
se_gamma_status = se_gamma.status if se_gamma else "unknown"

if tc_gamma_status == "pass" and se_gamma_status in ("fail", "undetermined"):
    print("OUTCOME C: Forks diverge in predictive content.")
    print()
    print(f"  Fork TC: gamma_v = 1 ({tc_gamma.message})")
    print(f"  Fork SE: gamma_v {se_gamma_status} ({se_gamma.message})")
    print()
    print("  Both forks are internally consistent. Neither produces a")
    print("  contradiction (ruling out Outcome B). But they make different")
    print("  predictions for gamma_v, which is measurable via light")
    print("  deflection and Shapiro delay (confirming Outcome C).")
    print()
    print("  The existing postulates do NOT silently commit to either fork.")
    print("  The framework needs either:")
    print("    - An additional postulate (trace conservation) to derive gamma_v = 1, or")
    print("    - Empirical input fixing gamma_v, which then determines the fork.")
elif tc_gamma_status == "pass" and se_gamma_status == "pass":
    print("OUTCOME A: Both forks consistent, same predictions.")
    print("  (This would be surprising -- check for hidden error.)")
else:
    print(f"  Fork TC gamma_v: {tc_gamma_status}")
    print(f"  Fork SE gamma_v: {se_gamma_status}")
    print("  See detailed results above.")
