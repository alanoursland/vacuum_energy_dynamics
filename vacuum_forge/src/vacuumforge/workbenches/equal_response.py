"""Standard Equal-Response Workbench (M36).

Packages the main equal-response investigation into a ready-to-use
workbench with standard targets, requirements, candidate families,
and reports pre-loaded.
"""

from __future__ import annotations

import sympy

from vacuumforge.core.context import TheoryContext
from vacuumforge.comparison.compare import ModelSummary, compare_models, summarize_model
from vacuumforge.comparison.classification import classify_model, ClassificationResult
from vacuumforge.theorems.candidates import TheoremCandidate, TheoremRegistry


def equal_response() -> TheoryContext:
    """Create a fully-configured equal-response workbench.

    Returns a TheoryContext with:
    - Standard algebraic symbols
    - Standard requirements loaded
    - Standard target library
    - Scope set to algebraic_prototype
    - Notation set to framework convention

    The user can immediately explore reciprocal scaling, trace-free
    exchange, mismatch energy, gamma/beta extraction, and leak audits.
    """
    ctx = TheoryContext("equal_response_workbench")
    ms = ctx.define_equal_response_algebraic_symbols()

    # Set scope
    ctx.scope.default = ctx.scope._default  # already algebraic

    # Set notation
    from vacuumforge.core.notation import FRAMEWORK_PROFILE
    ctx._notation = FRAMEWORK_PROFILE

    # Register standard theorem candidates
    ctx.theorems.create(
        "trace_free_exchange",
        "Local exchange interactions are trace-free (J_kappa = 0).",
        scope="algebraic_prototype",
        assumptions=["exchange-creation separation"],
    )
    ctx.theorems.create(
        "kappa_relaxation",
        "Unsourced kappa relaxes to zero under positive energy.",
        scope="algebraic_prototype",
        assumptions=["positive energy", "J_kappa = 0"],
    )
    ctx.theorems.create(
        "reciprocal_from_exchange",
        "Reciprocal scaling (AB=1) follows from trace-free exchange + energy minimization.",
        scope="algebraic_prototype",
        assumptions=["trace-free exchange", "quadratic energy", "energy minimization"],
    )

    return ctx


def demo_reciprocal_exponential() -> TheoryContext:
    """Build a reciprocal exponential model: A=exp(Phi/c^2), B=exp(-Phi/c^2)."""
    ctx = equal_response()
    ms = ctx._mode_symbols
    ctx.assumptions.add("A_exp", sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)))
    ctx.assumptions.add("B_exp", sympy.Eq(ms.B, sympy.exp(-ms.Phi / ms.c**2)))
    ctx.name = "reciprocal_exponential"
    return ctx


def demo_parallel_scaling() -> TheoryContext:
    """Build a parallel scaling model: A=B=exp(Phi/c^2)."""
    ctx = equal_response()
    ms = ctx._mode_symbols
    ctx.assumptions.add("A_exp", sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)))
    ctx.assumptions.add("B_exp", sympy.Eq(ms.B, sympy.exp(ms.Phi / ms.c**2)))
    ctx.name = "parallel_scaling"
    return ctx


def demo_free_gamma() -> TheoryContext:
    """Build a free-gamma model: A=exp(Phi/c^2), B=exp(-gamma_v*Phi/c^2)."""
    ctx = equal_response()
    ms = ctx._mode_symbols
    ctx.assumptions.add("A_exp", sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)))
    ctx.assumptions.add(
        "B_free_gamma",
        sympy.Eq(ms.B, sympy.exp(-ms.gamma_v * ms.Phi / ms.c**2)),
    )
    ctx.name = "free_gamma"
    return ctx


def demo_trace_free_exchange() -> TheoryContext:
    """Build a model with trace-free exchange + quadratic energy."""
    ctx = equal_response()
    ms = ctx._mode_symbols
    ctx.assumptions.add("A_exp", sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)))
    ctx.assumptions.add("B_exp", sympy.Eq(ms.B, sympy.exp(-ms.Phi / ms.c**2)))

    Js = sympy.Symbol("J_s")
    ctx.sources.exchange_trace_free(Js)
    ctx.energy.quadratic_modes(ms.C_kappa, ms.C_sigma, ms.kappa, ms.sigma)
    ctx.name = "trace_free_exchange"
    return ctx


def demo_assumed_reciprocal() -> TheoryContext:
    """Build a model that directly assumes B=1/A (leak test)."""
    ctx = equal_response()
    ms = ctx._mode_symbols
    ctx.assumptions.add("B_reciprocal", sympy.Eq(ms.B, 1 / ms.A))
    ctx.name = "assumed_reciprocal"
    return ctx


DEMO_BUILDERS = {
    "reciprocal_exponential": demo_reciprocal_exponential,
    "parallel_scaling": demo_parallel_scaling,
    "free_gamma": demo_free_gamma,
    "trace_free_exchange": demo_trace_free_exchange,
    "assumed_reciprocal": demo_assumed_reciprocal,
}


def run_standard_comparison() -> str:
    """Run the standard five-model comparison and return markdown."""
    contexts = [builder() for builder in DEMO_BUILDERS.values()]
    comparison = compare_models(contexts)
    return comparison.to_markdown()


def classify_demos() -> dict[str, ClassificationResult]:
    """Classify all demo models."""
    return {
        name: classify_model(builder())
        for name, builder in DEMO_BUILDERS.items()
    }
