"""Candidate structure families for systematic exploration.

Provides reusable templates for common candidate structures
as described in the design document.
"""

from __future__ import annotations

import sympy

from vacuumforge.structure_search.operators import SourceOperator
from vacuumforge.structure_search.projection import ProjectionMap
from vacuumforge.structure_search.structure import VacuumStructure


def direct_mode_basis() -> VacuumStructure:
    """Family 1: Direct mode basis (kappa, sigma).

    This is a tautological control. It defines exchange as
    delta kappa = 0 directly, so trace-free exchange is assumed.

    Variables: kappa, sigma
    Projection: a = kappa + sigma, b = kappa - sigma
    Exchange: delta kappa = 0, delta sigma = S
    Creation: delta kappa = C, delta sigma = 0
    """
    kappa, sigma = sympy.symbols("kappa sigma", real=True)
    S, C = sympy.symbols("S C")

    projection = ProjectionMap(
        id="direct_mode_projection",
        variables=[kappa, sigma],
        a_expr=kappa + sigma,
        b_expr=kappa - sigma,
        description="a = kappa + sigma, b = kappa - sigma",
    )

    exchange = SourceOperator(
        id="direct_mode_exchange",
        kind="exchange",
        deltas={kappa: sympy.Integer(0), sigma: S},
        source_symbols=[S],
        description="Exchange in mode basis: delta kappa = 0, delta sigma = S",
    )

    creation = SourceOperator(
        id="direct_mode_creation",
        kind="creation",
        deltas={kappa: C, sigma: sympy.Integer(0)},
        source_symbols=[C],
        description="Creation in mode basis: delta kappa = C, delta sigma = 0",
    )

    return VacuumStructure(
        id="direct_mode_basis",
        variables=[kappa, sigma],
        projection=projection,
        exchange_operators=[exchange],
        creation_operators=[creation],
        description="Direct mode basis — tautological control structure",
    )


def symmetric_antisymmetric_pair() -> VacuumStructure:
    """Family 2: Symmetric/antisymmetric pair basis.

    Variables: q_plus, q_minus
    Projection: a = q_plus + q_minus, b = q_plus - q_minus
    Exchange: delta q_plus = 0, delta q_minus = S
    Creation: delta q_plus = C, delta q_minus = 0
    """
    q_plus, q_minus = sympy.symbols("q_+ q_-", real=True)
    S, C = sympy.symbols("S C")

    projection = ProjectionMap(
        id="sym_antisym_projection",
        variables=[q_plus, q_minus],
        a_expr=q_plus + q_minus,
        b_expr=q_plus - q_minus,
        description="a = q_+ + q_-, b = q_+ - q_-",
    )

    exchange = SourceOperator(
        id="sym_antisym_exchange",
        kind="exchange",
        deltas={q_plus: sympy.Integer(0), q_minus: S},
        source_symbols=[S],
        description="Exchange: delta q_+ = 0, delta q_- = S",
    )

    creation = SourceOperator(
        id="sym_antisym_creation",
        kind="creation",
        deltas={q_plus: C, q_minus: sympy.Integer(0)},
        source_symbols=[C],
        description="Creation: delta q_+ = C, delta q_- = 0",
    )

    return VacuumStructure(
        id="symmetric_antisymmetric_pair",
        variables=[q_plus, q_minus],
        projection=projection,
        exchange_operators=[exchange],
        creation_operators=[creation],
        description="Symmetric/antisymmetric pair basis",
    )


def two_channel_exchange() -> VacuumStructure:
    """Family 3: Two-channel exchange basis.

    Variables: q_t, q_x
    Projection: a = q_t, b = q_x
    Exchange: delta q_t = S, delta q_x = -S  (antisymmetric)
    Creation: delta q_t = C, delta q_x = C   (symmetric)
    """
    q_t, q_x = sympy.symbols("q_t q_x", real=True)
    S, C = sympy.symbols("S C")

    projection = ProjectionMap(
        id="two_channel_projection",
        variables=[q_t, q_x],
        a_expr=q_t,
        b_expr=q_x,
        description="a = q_t, b = q_x (direct channel mapping)",
    )

    exchange = SourceOperator(
        id="antisymmetric_exchange",
        kind="exchange",
        deltas={q_t: S, q_x: -S},
        source_symbols=[S],
        description="Antisymmetric exchange: delta q_t = S, delta q_x = -S",
    )

    creation = SourceOperator(
        id="symmetric_creation",
        kind="creation",
        deltas={q_t: C, q_x: C},
        source_symbols=[C],
        description="Symmetric creation: delta q_t = C, delta q_x = C",
    )

    return VacuumStructure(
        id="two_channel_exchange",
        variables=[q_t, q_x],
        projection=projection,
        exchange_operators=[exchange],
        creation_operators=[creation],
        description="Two-channel antisymmetric exchange / symmetric creation",
    )


def general_linear_projection(
    n_vars: int = 2,
) -> VacuumStructure:
    """Family 4: General linear projection family.

    Variables: q_1, ..., q_n
    Projection: a = sum alpha_i q_i, b = sum beta_i q_i
    Exchange: delta q_i = e_i * S
    Creation: delta q_i = c_i * C

    The trace-free exchange condition becomes:
        sum (alpha_i + beta_i) * e_i = 0

    The traceful creation condition becomes:
        sum (alpha_i + beta_i) * c_i != 0
    """
    q_syms = sympy.symbols(
        " ".join(f"q_{i+1}" for i in range(n_vars)), real=True
    )
    if n_vars == 1:
        q_syms = [q_syms]
    else:
        q_syms = list(q_syms)

    alpha_syms = sympy.symbols(
        " ".join(f"alpha_{i+1}" for i in range(n_vars)), real=True
    )
    beta_syms = sympy.symbols(
        " ".join(f"beta_{i+1}" for i in range(n_vars)), real=True
    )
    e_syms = sympy.symbols(
        " ".join(f"e_{i+1}" for i in range(n_vars)), real=True
    )
    c_syms = sympy.symbols(
        " ".join(f"c_{i+1}" for i in range(n_vars)), real=True
    )
    if n_vars == 1:
        alpha_syms = [alpha_syms]
        beta_syms = [beta_syms]
        e_syms = [e_syms]
        c_syms = [c_syms]
    else:
        alpha_syms = list(alpha_syms)
        beta_syms = list(beta_syms)
        e_syms = list(e_syms)
        c_syms = list(c_syms)

    S, C = sympy.symbols("S C")

    a_expr = sum(alpha_syms[i] * q_syms[i] for i in range(n_vars))
    b_expr = sum(beta_syms[i] * q_syms[i] for i in range(n_vars))

    projection = ProjectionMap(
        id=f"general_linear_{n_vars}d",
        variables=q_syms,
        a_expr=a_expr,
        b_expr=b_expr,
        description=f"a = sum alpha_i q_i, b = sum beta_i q_i (n={n_vars})",
    )

    exchange_deltas = {q_syms[i]: e_syms[i] * S for i in range(n_vars)}
    exchange = SourceOperator(
        id=f"general_linear_exchange_{n_vars}d",
        kind="exchange",
        deltas=exchange_deltas,
        source_symbols=[S],
        description=f"General exchange: delta q_i = e_i * S",
    )

    creation_deltas = {q_syms[i]: c_syms[i] * C for i in range(n_vars)}
    creation = SourceOperator(
        id=f"general_linear_creation_{n_vars}d",
        kind="creation",
        deltas=creation_deltas,
        source_symbols=[C],
        description=f"General creation: delta q_i = c_i * C",
    )

    return VacuumStructure(
        id=f"general_linear_projection_{n_vars}d",
        variables=q_syms,
        projection=projection,
        exchange_operators=[exchange],
        creation_operators=[creation],
        description=f"General linear projection with {n_vars} pre-mode variables",
    )


def conserved_volume_family() -> VacuumStructure:
    """Family 6: Conserved-volume family.

    Tests whether a conservation principle delta(a+b) = 0
    can derive trace-free exchange.

    Variables: q_t, q_x
    Projection: a = q_t, b = q_x
    Exchange: delta q_t = S, delta q_x = -S  (conserves a+b)
    Creation: delta q_t = C, delta q_x = 0   (does not conserve a+b)
    """
    q_t, q_x = sympy.symbols("q_t q_x", real=True)
    S, C = sympy.symbols("S C")

    projection = ProjectionMap(
        id="conserved_volume_projection",
        variables=[q_t, q_x],
        a_expr=q_t,
        b_expr=q_x,
        description="a = q_t, b = q_x",
    )

    exchange = SourceOperator(
        id="volume_conserving_exchange",
        kind="exchange",
        deltas={q_t: S, q_x: -S},
        source_symbols=[S],
        constraints=[sympy.Eq(S + (-S), 0)],
        description="Volume-conserving exchange: delta(a+b) = 0",
    )

    creation = SourceOperator(
        id="volume_breaking_creation",
        kind="creation",
        deltas={q_t: C, q_x: sympy.Integer(0)},
        source_symbols=[C],
        description="Volume-breaking creation: delta q_t = C, delta q_x = 0",
    )

    return VacuumStructure(
        id="conserved_volume",
        variables=[q_t, q_x],
        projection=projection,
        exchange_operators=[exchange],
        creation_operators=[creation],
        symmetries=["volume_conservation: delta(a+b) = 0 for exchange"],
        description="Conserved-volume family testing delta(a+b)=0 as derivation path",
    )


def mixed_exchange_family() -> VacuumStructure:
    """A failing test family where exchange sources both kappa and sigma.

    Variables: q_t, q_x
    Projection: a = q_t, b = q_x
    Exchange: delta q_t = S, delta q_x = 0  (NOT antisymmetric)
    """
    q_t, q_x = sympy.symbols("q_t q_x", real=True)
    S, C = sympy.symbols("S C")

    projection = ProjectionMap(
        id="mixed_exchange_projection",
        variables=[q_t, q_x],
        a_expr=q_t,
        b_expr=q_x,
        description="a = q_t, b = q_x",
    )

    exchange = SourceOperator(
        id="one_sided_exchange",
        kind="exchange",
        deltas={q_t: S, q_x: sympy.Integer(0)},
        source_symbols=[S],
        description="One-sided exchange: delta q_t = S, delta q_x = 0",
    )

    creation = SourceOperator(
        id="symmetric_creation_mixed",
        kind="creation",
        deltas={q_t: C, q_x: C},
        source_symbols=[C],
        description="Symmetric creation: delta q_t = C, delta q_x = C",
    )

    return VacuumStructure(
        id="mixed_exchange_family",
        variables=[q_t, q_x],
        projection=projection,
        exchange_operators=[exchange],
        creation_operators=[creation],
        description="Failing family: exchange sources both kappa and sigma",
    )
