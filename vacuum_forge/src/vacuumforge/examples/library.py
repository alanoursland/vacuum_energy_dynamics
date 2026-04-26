"""Research examples library (M39).

Each example produces a TheoryContext with a validation report,
demonstrating a specific aspect of the equal-response problem.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import sympy

from vacuumforge.core.context import TheoryContext


@dataclass
class ExampleResult:
    """Result of running a research example."""

    name: str
    description: str
    context: TheoryContext
    report: str


def _reciprocal_exponential() -> ExampleResult:
    """Reciprocal exponential: A=exp(Phi/c^2), B=exp(-Phi/c^2).

    Demonstrates: AB=1 holds exactly, gamma_v=1, beta=1.
    The gold-standard equal-response model.
    """
    ctx = TheoryContext("reciprocal_exponential")
    ms = ctx.define_equal_response_algebraic_symbols()
    ctx.assumptions.add("A_exp", sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)))
    ctx.assumptions.add("B_exp", sympy.Eq(ms.B, sympy.exp(-ms.Phi / ms.c**2)))

    report = ctx.reports.validation()
    return ExampleResult(
        "reciprocal_exponential",
        "Reciprocal exponential scaling: AB=1 exactly.",
        ctx, str(report),
    )


def _parallel_scaling_failure() -> ExampleResult:
    """Parallel scaling: A=B=exp(Phi/c^2).

    Demonstrates: AB = exp(2*Phi/c^2) != 1, gamma_v = -1.
    Shows what goes wrong when spatial and temporal scale factors are equal.
    """
    ctx = TheoryContext("parallel_scaling_failure")
    ms = ctx.define_equal_response_algebraic_symbols()
    ctx.assumptions.add("A_exp", sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)))
    ctx.assumptions.add("B_par", sympy.Eq(ms.B, sympy.exp(ms.Phi / ms.c**2)))

    report = ctx.reports.validation()
    return ExampleResult(
        "parallel_scaling_failure",
        "Parallel scaling A=B fails reciprocal condition.",
        ctx, str(report),
    )


def _free_gamma_metric() -> ExampleResult:
    """Free gamma: A=exp(Phi/c^2), B=exp(-gamma_v*Phi/c^2).

    Demonstrates: gamma_v remains symbolic, beta=1 but gamma_v != 1.
    """
    ctx = TheoryContext("free_gamma")
    ms = ctx.define_equal_response_algebraic_symbols()
    ctx.assumptions.add("A_exp", sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)))
    ctx.assumptions.add(
        "B_free",
        sympy.Eq(ms.B, sympy.exp(-ms.gamma_v * ms.Phi / ms.c**2)),
    )

    report = ctx.reports.validation()
    return ExampleResult(
        "free_gamma",
        "Free gamma: gamma_v remains undetermined.",
        ctx, str(report),
    )


def _mismatch_energy() -> ExampleResult:
    """Mismatch energy: E = C_mu * mu^2 = 4*C*kappa^2.

    Demonstrates: mismatch energy penalizes kappa deviation.
    """
    ctx = TheoryContext("mismatch_energy")
    ms = ctx.define_equal_response_algebraic_symbols()
    ctx.assumptions.add("A_exp", sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)))
    ctx.assumptions.add("B_exp", sympy.Eq(ms.B, sympy.exp(-ms.Phi / ms.c**2)))

    from vacuumforge.search.families import mismatch_energy
    E, C = mismatch_energy(ms.kappa)
    ctx.energy.add("mismatch_energy", E, [ms.kappa], description="Mismatch penalty")

    report = ctx.reports.validation()
    return ExampleResult(
        "mismatch_energy",
        "Mismatch energy penalizes AB != 1 via kappa^2 term.",
        ctx, str(report),
    )


def _trace_free_exchange_minimization() -> ExampleResult:
    """Trace-free exchange + quadratic energy + minimization.

    Demonstrates: With J_kappa=0 (trace-free exchange) and quadratic energy,
    energy minimization forces kappa=0, hence AB=1.
    """
    ctx = TheoryContext("trace_free_plus_minimization")
    ms = ctx.define_equal_response_algebraic_symbols()
    ctx.assumptions.add("A_exp", sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)))
    ctx.assumptions.add("B_exp", sympy.Eq(ms.B, sympy.exp(-ms.Phi / ms.c**2)))

    Js = sympy.Symbol("J_s")
    ctx.sources.exchange_trace_free(Js)
    ctx.energy.source_coupled(
        ms.C_kappa, ms.C_sigma, ms.J_kappa, ms.J_sigma,
        ms.kappa, ms.sigma,
    )
    result = ctx.energy.solve_stationary(
        "source_coupled_energy", extra_subs={ms.J_kappa: 0},
    )

    report = ctx.reports.validation()
    return ExampleResult(
        "trace_free_exchange_minimization",
        "Trace-free exchange + energy minimization -> kappa=0.",
        ctx, str(report),
    )


def _mixed_source_nonzero_kappa() -> ExampleResult:
    """Mixed source: both J_kappa and J_sigma nonzero.

    Demonstrates: kappa != 0 when exchange has a trace component.
    """
    ctx = TheoryContext("mixed_source")
    ms = ctx.define_equal_response_algebraic_symbols()
    ctx.assumptions.add("A_exp", sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)))
    ctx.assumptions.add("B_exp", sympy.Eq(ms.B, sympy.exp(-ms.Phi / ms.c**2)))

    Jk = sympy.Symbol("J_k", positive=True)
    Js = sympy.Symbol("J_s")
    ctx.sources.add_modes("mixed_exchange", Jk, Js, source_type="exchange")

    ctx.energy.source_coupled(
        ms.C_kappa, ms.C_sigma, Jk, Js, ms.kappa, ms.sigma,
    )
    result = ctx.energy.solve_stationary("source_coupled_energy")

    report = ctx.reports.validation()
    return ExampleResult(
        "mixed_source",
        "Mixed source with J_kappa != 0: kappa != 0.",
        ctx, str(report),
    )


def _creation_source() -> ExampleResult:
    """Creation source excites kappa.

    Demonstrates: creation sources are traceful, exciting kappa.
    """
    ctx = TheoryContext("creation_source")
    ms = ctx.define_equal_response_algebraic_symbols()
    ctx.assumptions.add("A_exp", sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)))
    ctx.assumptions.add("B_exp", sympy.Eq(ms.B, sympy.exp(-ms.Phi / ms.c**2)))

    Jc = sympy.Symbol("J_c", positive=True)
    ctx.sources.creation_uniform(Jc)

    report = ctx.reports.validation()
    return ExampleResult(
        "creation_source",
        "Creation source excites kappa mode.",
        ctx, str(report),
    )


def _counterexample_exchange_trace() -> ExampleResult:
    """Counterexample: exchange does NOT imply trace-free.

    Demonstrates: total energy conservation allows J_kappa != 0.
    """
    from vacuumforge.search.counterexamples import exchange_with_nonzero_trace

    ctx = TheoryContext("counterexample_exchange_trace")
    ctx.define_equal_response_algebraic_symbols()

    cx = exchange_with_nonzero_trace()

    report = (
        f"# Counterexample: {cx.claim}\n\n"
        f"## Construction\n{cx.construction}\n\n"
        f"## Verification\n{cx.verification}\n\n"
        f"## Conclusion\n{cx.conclusion}"
    )

    return ExampleResult(
        "counterexample_exchange_trace",
        cx.claim,
        ctx, report,
    )


def _counterexample_density_kappa() -> ExampleResult:
    """Counterexample: density constancy does NOT forbid kappa.

    Demonstrates: conformal rescaling preserves density ratio.
    """
    from vacuumforge.search.counterexamples import density_with_nonzero_kappa

    ctx = TheoryContext("counterexample_density_kappa")
    ctx.define_equal_response_algebraic_symbols()

    cx = density_with_nonzero_kappa()

    report = (
        f"# Counterexample: {cx.claim}\n\n"
        f"## Construction\n{cx.construction}\n\n"
        f"## Conclusion\n{cx.conclusion}"
    )

    return ExampleResult(
        "counterexample_density_kappa",
        cx.claim,
        ctx, report,
    )


ALL_EXAMPLES: dict[str, Callable[[], ExampleResult]] = {
    "reciprocal_exponential": _reciprocal_exponential,
    "parallel_scaling_failure": _parallel_scaling_failure,
    "free_gamma": _free_gamma_metric,
    "mismatch_energy": _mismatch_energy,
    "trace_free_exchange_minimization": _trace_free_exchange_minimization,
    "mixed_source": _mixed_source_nonzero_kappa,
    "creation_source": _creation_source,
    "counterexample_exchange_trace": _counterexample_exchange_trace,
    "counterexample_density_kappa": _counterexample_density_kappa,
}


def run_example(name: str) -> ExampleResult:
    """Run a named example."""
    if name not in ALL_EXAMPLES:
        raise ValueError(f"Unknown example: {name}. Available: {list(ALL_EXAMPLES.keys())}")
    return ALL_EXAMPLES[name]()


def run_all_examples() -> dict[str, ExampleResult]:
    """Run all examples and return results."""
    return {name: builder() for name, builder in ALL_EXAMPLES.items()}
