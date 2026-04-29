# Trace kernel test: a focused example demonstrating the geometric reason
# exchange can be trace-free.
#
# Setup:
#   - Two pre-mode variables (q_t, q_x) with direct projection a = q_t, b = q_x.
#   - The trace projection is the row vector [1, 1] (since kappa ~ a + b).
#   - Exchange delta = (S, -S) lies in the kernel of [1, 1]:
#       [1, 1] . [S, -S] = 0  =>  J_kappa = 0 (trace-free).
#   - Creation delta = (C, C) lies in the trace direction:
#       [1, 1] . [C, C] = 2C  =>  J_kappa = 2C (traceful).
#
# This is the cleanest illustration of the core idea: exchange is trace-free
# when its operator direction is orthogonal to the trace projection.
# The open physics question is why exchange must take that direction.

import sympy as sp

from vacuumforge import TheoryContext
from vacuumforge.structure_search import (
    VacuumStructure,
    ProjectionMap,
    SourceOperator,
    StructureAnalyzer,
)

ctx = TheoryContext("trace_kernel_test")
ctx.define_equal_response_algebraic_symbols()

q_t, q_x, S, C = sp.symbols("q_t q_x S C")

projection = ProjectionMap(
    id="direct_tx_projection",
    variables=[q_t, q_x],
    a_expr=q_t,
    b_expr=q_x,
)

# Exchange direction lies in kernel of trace projection [1, 1]:
# [1, 1] dot [S, -S] = 0
exchange = SourceOperator(
    id="trace_kernel_exchange",
    kind="exchange",
    deltas={q_t: S, q_x: -S},
    source_symbols=[S],
)

# Creation direction does not lie in kernel:
# [1, 1] dot [C, C] = 2C
creation = SourceOperator(
    id="trace_direction_creation",
    kind="creation",
    deltas={q_t: C, q_x: C},
    source_symbols=[C],
)

structure = VacuumStructure(
    id="trace_kernel_structure",
    variables=[q_t, q_x],
    projection=projection,
    exchange_operators=[exchange],
    creation_operators=[creation],
    description="Exchange lies in the trace kernel; creation lies in the trace direction.",
)

analyzer = StructureAnalyzer()
result = analyzer.analyze(structure, ctx)

print(result.summary())

ex = result.exchange_results[0]
cr = result.creation_results[0]

print("\nExchange:")
print("  J_a     =", ex.J_a)
print("  J_b     =", ex.J_b)
print("  J_kappa =", ex.J_kappa)
print("  J_sigma =", ex.J_sigma)
print("  status  =", ex.status)

print("\nCreation:")
print("  J_a     =", cr.J_a)
print("  J_b     =", cr.J_b)
print("  J_kappa =", cr.J_kappa)
print("  J_sigma =", cr.J_sigma)
print("  status  =", cr.status)

print("\nInterpretation:")
print("  If this structure is physically justified, local exchange is trace-free")
print("  because its operator lies in the kernel of the trace projection.")
print("  The remaining physics question is why exchange must take that direction.")
