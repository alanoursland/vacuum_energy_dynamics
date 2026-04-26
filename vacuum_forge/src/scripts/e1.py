# Baseline family analysis: run all 5 built-in structure families through the
# StructureAnalyzer and print detailed results for each.
#
# Families tested:
#   - direct_mode_basis: projects (kappa, sigma) directly to (a, b).
#     Expected TAUTOLOGICAL — exchange sets delta_kappa = 0 by definition,
#     so trace-free is assumed, not derived.
#   - two_channel_exchange: two pre-mode variables with antisymmetric exchange.
#     Expected DERIVED — the projection geometry forces J_kappa = 0.
#   - general_linear_projection(n=2): symbolic coefficients (alpha, beta, gamma, delta).
#     Expected CONDITIONAL — trace-free holds only under coefficient constraints.
#   - conserved_volume_family: nonlinear projection with a volume constraint.
#     Expected DERIVED — the constraint structure forces trace-free exchange.
#   - mixed_exchange_family: exchange sources both kappa and sigma.
#     Expected FAILED — J_kappa != 0 for generic exchange.

from vacuumforge import TheoryContext
from vacuumforge.structure_search import StructureAnalyzer
from vacuumforge.structure_search.families import (
    direct_mode_basis,
    two_channel_exchange,
    general_linear_projection,
    conserved_volume_family,
    mixed_exchange_family,
)

ctx = TheoryContext("structure_search_baseline")
ctx.define_equal_response_algebraic_symbols()

analyzer = StructureAnalyzer()

families = [
    ("direct_mode_basis", direct_mode_basis()),
    ("two_channel_exchange", two_channel_exchange()),
    ("general_linear_projection_n2", general_linear_projection(n_vars=2)),
    ("conserved_volume_family", conserved_volume_family()),
    ("mixed_exchange_family", mixed_exchange_family()),
]

for name, structure in families:
    print("\n" + "=" * 80)
    print(name)
    print("=" * 80)

    result = analyzer.analyze(structure, ctx)

    print(result.summary())

    print("\nExchange results:")
    for ex in result.exchange_results:
        print(f"  operator: {ex.operator_id}")
        print(f"  status: {ex.status}")
        print(f"  classification: {ex.classification}")
        print(f"  J_a = {ex.J_a}")
        print(f"  J_b = {ex.J_b}")
        print(f"  J_kappa = {ex.J_kappa}")
        print(f"  J_sigma = {ex.J_sigma}")
        if ex.conditions:
            print(f"  conditions: {ex.conditions}")

    print("\nCreation results:")
    for cr in result.creation_results:
        print(f"  operator: {cr.operator_id}")
        print(f"  status: {cr.status}")
        print(f"  classification: {cr.classification}")
        print(f"  J_a = {cr.J_a}")
        print(f"  J_b = {cr.J_b}")
        print(f"  J_kappa = {cr.J_kappa}")
        print(f"  J_sigma = {cr.J_sigma}")
        if cr.conditions:
            print(f"  conditions: {cr.conditions}")

    if result.leak_warnings:
        print("\nLeak warnings:")
        for warning in result.leak_warnings:
            print(f"  - {warning}")

    if result.failures:
        print("\nFailures:")
        for failure in result.failures:
            print(f"  - {failure}")

    if result.conditions:
        print("\nStructure-level conditions:")
        for condition in result.conditions:
            print(f"  - {condition}")

