# Sign pattern enumeration: systematically test all exchange delta combinations
# from {-1, 0, +1} x {-1, 0, +1} (excluding trivial (0,0)) on a direct 2D
# projection (a = q_1, b = q_2) with symmetric creation (delta q_i = C).
#
# This brute-force sweep classifies each sign pattern as:
#   - trace_free_derived: J_kappa = 0 structurally (e.g. antisymmetric (+1, -1))
#   - conditional: trace-free under parameter constraints
#   - failed: J_kappa != 0 generically
#   - tautological: trace-free is assumed, not derived
#
# Key result: only the antisymmetric patterns (+1, -1) and (-1, +1) derive
# trace-free exchange; patterns with equal signs fail; patterns with a zero
# component zero out part of the source.

from vacuumforge import TheoryContext

ctx = TheoryContext("sign_pattern_search")
ctx.define_equal_response_algebraic_symbols()

result = ctx.structure_search.enumerate_sign_patterns(n_vars=2)

print(result.summary())

print("\nTrace-free derived candidates:")
for item in result.trace_free_derived:
    print("  -", item.structure_id if hasattr(item, "structure_id") else item)

print("\nConditional candidates:")
for item in result.conditional:
    print("  -", item.structure_id if hasattr(item, "structure_id") else item)

print("\nFailed candidates:")
for item in result.failed:
    print("  -", item.structure_id if hasattr(item, "structure_id") else item)
