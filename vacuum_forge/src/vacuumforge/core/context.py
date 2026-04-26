"""Central TheoryContext for VacuumForge.

The TheoryContext is the main object that organizes all symbolic
variables, assumptions, expressions, sources, dependencies, and
the theory ledger for a given investigation.
"""

from __future__ import annotations

from typing import Any

import sympy

from vacuumforge.core.assumptions import AssumptionManager
from vacuumforge.core.dependency import DependencyGraph, DerivationRecord
from vacuumforge.core.dimensions import DimensionChecker
from vacuumforge.core.expressions import ExpressionStore
from vacuumforge.core.ledger import TheoryLedger
from vacuumforge.core.notation import FRAMEWORK_PROFILE, NotationProfile
from vacuumforge.core.scope import ScopeLevel, ScopeManager
from vacuumforge.core.symbols import SymbolRegistry
from vacuumforge.energy.functional import EnergyManager
from vacuumforge.energy.positivity import check_quadratic_positivity
from vacuumforge.metric.expansion import ExpansionEngine
from vacuumforge.metric.ppn import PPNResult, extract_all, extract_beta, extract_gamma
from vacuumforge.metric.reciprocal import (
    ReciprocalCheckResult,
    check_exact_reciprocal,
    check_kappa_zero,
    check_perturbative_reciprocal,
)
from vacuumforge.metric.weak_field import WeakFieldMetric
from vacuumforge.modes.sources import SourceManager
from vacuumforge.modes.standard import AlgebraicModeSymbols, create_algebraic_symbols
from vacuumforge.modes.transforms import TransformEngine
from vacuumforge.reports.markdown import ReportManager
from vacuumforge.requirements.targets import TargetLibrary, build_standard_targets
from vacuumforge.requirements.validators import RequirementManager
from vacuumforge.structure_search.search import StructureSearchEngine
from vacuumforge.theorems.candidates import TheoremRegistry


class _ModeProxy:
    """Proxy providing mode transform methods on the context."""

    def __init__(self, ctx: TheoryContext) -> None:
        self._ctx = ctx

    @property
    def _engine(self) -> TransformEngine:
        if self._ctx._mode_symbols is None:
            raise RuntimeError("Call define_equal_response_algebraic_symbols() first.")
        return self._ctx._mode_symbols.transforms

    def to_log(self, expr: sympy.Basic) -> sympy.Basic:
        return self._engine.to_log(expr)

    def to_scale(self, expr: sympy.Basic) -> sympy.Basic:
        return self._engine.to_scale(expr)

    def to_modes(self, expr: sympy.Basic) -> sympy.Basic:
        return self._engine.to_modes(expr)

    def from_modes(self, expr: sympy.Basic) -> sympy.Basic:
        return self._engine.from_modes(expr)

    def modes_to_scale(self, expr: sympy.Basic) -> sympy.Basic:
        return self._engine.modes_to_scale(expr)

    def scale_to_modes(self, expr: sympy.Basic) -> sympy.Basic:
        return self._engine.scale_to_modes(expr)


class _MetricProxy:
    """Proxy providing metric construction and PPN extraction."""

    def __init__(self, ctx: TheoryContext) -> None:
        self._ctx = ctx

    def from_scale_factors(self, A: sympy.Basic, B: sympy.Basic) -> WeakFieldMetric:
        metric = WeakFieldMetric(A=A, B=B)
        self._ctx.expressions.add("metric.g00", metric.g00, description="g_00 = -A^2")
        self._ctx.expressions.add(
            "metric.gij_factor", metric.gij_factor, description="g_ij factor = B^2"
        )
        return metric


class _ExpansionProxy:
    """Proxy providing weak-field expansion methods."""

    def __init__(self, ctx: TheoryContext) -> None:
        self._ctx = ctx
        self._engine: ExpansionEngine | None = None

    def _get_engine(self) -> ExpansionEngine:
        if self._engine is not None:
            return self._engine
        syms = self._ctx._mode_symbols
        if syms is None:
            raise RuntimeError("Call define_equal_response_algebraic_symbols() first.")
        self._engine = ExpansionEngine(Phi=syms.Phi, c=syms.c)
        return self._engine

    def weak_field(self, expr: sympy.Basic, order: int = 2):
        return self._get_engine().weak_field(expr, order)

    def coefficient(self, expr: sympy.Basic, power: int = 1) -> sympy.Basic:
        return self._get_engine().coefficient(expr, power)

    def expand_and_collect(self, expr: sympy.Basic, order: int = 2):
        return self._get_engine().expand_and_collect(expr, order)


class _PPNProxy:
    """Proxy providing PPN parameter extraction."""

    def __init__(self, ctx: TheoryContext) -> None:
        self._ctx = ctx

    def _get_expansion(self) -> ExpansionEngine:
        return self._ctx.expansion._get_engine()

    def extract_gamma(self, metric: WeakFieldMetric) -> PPNResult:
        return extract_gamma(metric, self._get_expansion())

    def extract_beta(self, metric: WeakFieldMetric) -> PPNResult:
        return extract_beta(metric, self._get_expansion())

    def extract_all(self, metric: WeakFieldMetric) -> dict[str, PPNResult]:
        return extract_all(metric, self._get_expansion())


class _ChecksProxy:
    """Proxy providing built-in checks (reciprocal scaling, etc.)."""

    def __init__(self, ctx: TheoryContext) -> None:
        self._ctx = ctx

    def reciprocal_scaling(
        self,
        A: sympy.Basic | None = None,
        B: sympy.Basic | None = None,
    ) -> ReciprocalCheckResult:
        """Check exact reciprocal scaling A*B = 1."""
        if A is None or B is None:
            syms = self._ctx._mode_symbols
            if syms is None:
                raise RuntimeError("Provide A, B or define standard symbols first.")
            # Apply assumptions to get concrete A and B
            A_expr = self._ctx.assumptions.apply(syms.A) if A is None else A
            B_expr = self._ctx.assumptions.apply(syms.B) if B is None else B
        else:
            A_expr, B_expr = A, B
        return check_exact_reciprocal(A_expr, B_expr)

    def reciprocal_scaling_perturbative(
        self,
        A: sympy.Basic,
        B: sympy.Basic,
        order: int = 2,
    ) -> ReciprocalCheckResult:
        syms = self._ctx._mode_symbols
        if syms is None:
            raise RuntimeError("Define standard symbols first.")
        return check_perturbative_reciprocal(A, B, syms.Phi, syms.c, order)

    def kappa_zero(self, kappa_value: sympy.Basic) -> ReciprocalCheckResult:
        return check_kappa_zero(kappa_value)


class TheoryContext:
    """Central object for a VacuumForge theory investigation.

    Stores symbolic variables, assumptions, expressions, sources,
    dependency graph, and theory ledger.

    Example::

        ctx = TheoryContext("equal_response_demo")
        ctx.define_equal_response_algebraic_symbols()
        A = ctx.symbols.get("A")
        B = ctx.symbols.get("B")
    """

    def __init__(self, name: str = "unnamed") -> None:
        self.name = name
        self.symbols = SymbolRegistry()
        self.assumptions = AssumptionManager()
        self.expressions = ExpressionStore()
        self.dependencies = DependencyGraph()
        self.ledger = TheoryLedger()
        self.sources = SourceManager()
        self.energy = EnergyManager()
        self.requirements = RequirementManager()
        self.reports = ReportManager(self)
        self.dimensions = DimensionChecker()
        self.scope = ScopeManager()
        self.theorems = TheoremRegistry()
        self.structure_search = StructureSearchEngine()

        # Notation profile
        self._notation: NotationProfile = FRAMEWORK_PROFILE

        # Subsystem proxies
        self.modes = _ModeProxy(self)
        self.metric = _MetricProxy(self)
        self.expansion = _ExpansionProxy(self)
        self.ppn = _PPNProxy(self)
        self.checks = _ChecksProxy(self)

        # Display proxy (lazy import to avoid circular)
        self._display = None

        # Internal state
        self._mode_symbols: AlgebraicModeSymbols | None = None
        self._targets: TargetLibrary | None = None

    @property
    def display(self):
        """Lazy-loaded display proxy for notebook/terminal output."""
        if self._display is None:
            from vacuumforge.display import DisplayProxy
            self._display = DisplayProxy(self)
        return self._display

    @property
    def notation(self) -> NotationProfile:
        return self._notation

    @notation.setter
    def notation(self, profile: NotationProfile) -> None:
        self._notation = profile

    def define_equal_response_algebraic_symbols(self) -> AlgebraicModeSymbols:
        """Define the standard algebraic symbol set for equal-response analysis.

        Creates: A, B, a, b, kappa, sigma, mu, J_a, J_b, J_kappa, J_sigma,
                 gamma_v, beta, c, G, M, Phi, r, C_kappa, C_sigma.
        """
        ms = create_algebraic_symbols()
        self._mode_symbols = ms

        # Register all symbols
        self.symbols.define_constant("c", positive=True, description="Speed of light")
        self.symbols.define_constant("G", positive=True, description="Gravitational constant")
        self.symbols.define_constant("M", positive=True, description="Source mass")
        self.symbols.define_coordinate("r", positive=True, description="Radial coordinate")
        self.symbols.define_symbol("Phi", kind="potential", description="Gravitational potential")
        self.symbols.define_symbol("A", kind="scale_factor", positive=True,
                                   description="Temporal scale factor")
        self.symbols.define_symbol("B", kind="scale_factor", positive=True,
                                   description="Spatial scale factor")
        self.symbols.define_symbol("a", kind="log_variable", real=True,
                                   description="ln(A)")
        self.symbols.define_symbol("b", kind="log_variable", real=True,
                                   description="ln(B)")
        self.symbols.define_symbol("kappa", kind="mode", real=True,
                                   description="Conformal cell mode (a+b)/2")
        self.symbols.define_symbol("sigma", kind="mode", real=True,
                                   description="Shear mode (a-b)/2")
        self.symbols.define_symbol("mu", kind="mode", real=True,
                                   description="Mismatch variable a+b = 2*kappa")
        self.symbols.define_source("J_a", description="Source for a")
        self.symbols.define_source("J_b", description="Source for b")
        self.symbols.define_source("J_kappa", description="Source for kappa (trace)")
        self.symbols.define_source("J_sigma", description="Source for sigma (shear)")
        self.symbols.define_coefficient("gamma_v", description="PPN spatial response parameter")
        self.symbols.define_coefficient("beta", description="PPN second-order temporal parameter")
        self.symbols.define_coefficient("C_kappa", positive=True,
                                        description="Kappa stiffness coefficient")
        self.symbols.define_coefficient("C_sigma", positive=True,
                                        description="Sigma stiffness coefficient")

        # Store mode definitions as expressions
        self.expressions.add("def.a", sympy.Eq(ms.a, sympy.log(ms.A)),
                            description="a = ln(A)")
        self.expressions.add("def.b", sympy.Eq(ms.b, sympy.log(ms.B)),
                            description="b = ln(B)")
        self.expressions.add("def.kappa", sympy.Eq(ms.kappa, (ms.a + ms.b) / 2),
                            description="kappa = (a+b)/2")
        self.expressions.add("def.sigma", sympy.Eq(ms.sigma, (ms.a - ms.b) / 2),
                            description="sigma = (a-b)/2")
        self.expressions.add("def.mu", sympy.Eq(ms.mu, ms.a + ms.b),
                            description="mu = a+b = 2*kappa")

        # Build target library
        self._targets = build_standard_targets(
            A=ms.A, B=ms.B, a=ms.a, b=ms.b,
            kappa=ms.kappa, sigma=ms.sigma, mu=ms.mu,
            gamma_v=ms.gamma_v, beta=ms.beta,
            Phi=ms.Phi, c=ms.c,
        )

        # Load standard requirements
        self.requirements.add_standard()

        return ms

    def derive(
        self,
        result_id: str,
        expr: sympy.Basic,
        operation: str,
        uses: list[str] | None = None,
        inputs: list[str] | None = None,
        description: str | None = None,
        exactness: str = "exact",
        scope: str | None = None,
    ) -> sympy.Basic:
        """Store a derived result with dependency tracking."""
        self.expressions.add(
            result_id, expr,
            description=description,
            status="derived",
            dependencies=(uses or []) + (inputs or []),
            exactness=exactness,
            scope=scope,
        )
        record = DerivationRecord(
            id=f"deriv.{result_id}",
            operation=operation,
            inputs=inputs or [],
            outputs=[result_id],
            assumptions=uses or [],
        )
        self.dependencies.record_derivation(record)
        return expr

    def clone(self) -> TheoryContext:
        """Create a shallow copy for interactive exploration."""
        import copy
        return copy.deepcopy(self)

    def save(self, path: str) -> None:
        """Save this context to a YAML session file."""
        from vacuumforge.persistence.session import save_session
        save_session(self, path)

    @classmethod
    def load(cls, path: str) -> TheoryContext:
        """Load a context from a YAML session file."""
        from vacuumforge.persistence.session import load_session
        return load_session(path)

    def summary(self) -> str:
        parts = [
            f"TheoryContext: {self.name}",
            "=" * 40,
            self.symbols.summary(),
            self.assumptions.summary(),
            self.expressions.summary(),
            self.sources.summary(),
            self.ledger.summary(),
            self.dependencies.summary(),
            self.scope.summary(),
        ]
        if self.theorems.list():
            parts.append(self.theorems.summary())
        return "\n\n".join(parts)
