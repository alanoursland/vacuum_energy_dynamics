"""Tests for coordinate transformation helpers.

Covers Milestones 45-47 completion criteria:
- CoordinateChange is instantiable with canonical examples.
- transform_scale_factor: temporal has no Jacobian, radial has (df/dR)².
- transform_log_modes: a_new = a(f(R)), b_new = b(f(R)) + 2·ln(f'(R)).
- transform_metric: produces a new WeakFieldMetric.
- Round-trip reconstruction test.
- Registration appears in the dependency graph.
- Validator returns pass/fail/undetermined.
"""

import sympy

from vacuumforge import TheoryContext
from vacuumforge.coordinates import CoordinateChange, validate_coordinate_invariance
from vacuumforge.metric.weak_field import WeakFieldMetric


# -- Milestone 45: skeleton ---------------------------------------------------

def test_coordinate_change_instantiation():
    R = sympy.Symbol("R", positive=True)
    r = sympy.Symbol("r", positive=True)
    f = sympy.Function("f")(R)
    change = CoordinateChange(old_coord=r, new_coord=R, transform=f)
    assert change.old_coord == r
    assert change.new_coord == R
    assert change.transform == f


def test_jacobian():
    r, R, lam = sympy.symbols("r R lambda", positive=True)
    change = CoordinateChange(old_coord=r, new_coord=R, transform=lam * R)
    assert change.jacobian() == lam


# -- Milestone 46: core transformation methods --------------------------------

def test_scale_factor_temporal_no_jacobian():
    """Temporal scale factor: A_new(R) = A(f(R)), no Jacobian factor."""
    r, R, lam = sympy.symbols("r R lambda", positive=True)
    A = sympy.Function("A")(r)
    change = CoordinateChange(old_coord=r, new_coord=R, transform=lam * R)
    result = change.transform_scale_factor(A, "temporal")
    assert result == sympy.Function("A")(lam * R)


def test_scale_factor_radial_jacobian_squared():
    """Radial scale factor: B_new(R) = B(f(R)) · (df/dR)²."""
    r, R, lam = sympy.symbols("r R lambda", positive=True)
    B = sympy.Function("B")(r)
    change = CoordinateChange(old_coord=r, new_coord=R, transform=lam * R)
    result = change.transform_scale_factor(B, "radial")
    expected = lam**2 * sympy.Function("B")(lam * R)
    assert sympy.simplify(result - expected) == 0


def test_log_modes_radial_gets_2_log_jacobian():
    """b_new = b(f(R)) + 2·ln(f'(R))."""
    r, R = sympy.symbols("r R", positive=True)
    f = sympy.Function("f")(R)
    a = sympy.Function("a")(r)
    b = sympy.Function("b")(r)
    change = CoordinateChange(old_coord=r, new_coord=R, transform=f)

    a_new, b_new = change.transform_log_modes(a, b)

    assert a_new == sympy.Function("a")(f)
    expected_b = sympy.Function("b")(f) + 2 * sympy.log(sympy.diff(f, R))
    assert sympy.simplify(b_new - expected_b) == 0


def test_log_modes_concrete_lambda():
    """Concrete r = λR: b_new = b(λR) + 2·ln(λ)."""
    r, R, lam = sympy.symbols("r R lambda", positive=True)
    a = sympy.Function("a")(r)
    b = sympy.Function("b")(r)
    change = CoordinateChange(old_coord=r, new_coord=R, transform=lam * R)

    a_new, b_new = change.transform_log_modes(a, b)

    assert a_new == sympy.Function("a")(lam * R)
    expected_b = sympy.Function("b")(lam * R) + 2 * sympy.log(lam)
    assert sympy.simplify(b_new - expected_b) == 0


def test_transform_metric():
    r, R, lam = sympy.symbols("r R lambda", positive=True)
    metric = WeakFieldMetric(A=sympy.Integer(1), B=sympy.Function("B")(r))
    change = CoordinateChange(old_coord=r, new_coord=R, transform=lam * R)

    transformed = change.transform_metric(metric)

    assert transformed.A == 1
    expected_B = lam**2 * sympy.Function("B")(lam * R)
    assert sympy.simplify(transformed.B - expected_B) == 0


def test_invalid_kind_raises():
    r, R = sympy.symbols("r R", positive=True)
    change = CoordinateChange(old_coord=r, new_coord=R, transform=2 * R)
    try:
        change.transform_scale_factor(r, "angular")
        assert False, "Expected ValueError"
    except ValueError:
        pass


# -- Round-trip reconstruction -------------------------------------------------

def test_round_trip_scale_factor():
    """Apply r = λR, then R = r/λ; result should recover original."""
    r, R, lam = sympy.symbols("r R lambda", positive=True)
    A_r = sympy.Function("A")(r)

    forward = CoordinateChange(old_coord=r, new_coord=R, transform=lam * R)
    A_R = forward.transform_scale_factor(A_r, "temporal")

    backward = CoordinateChange(old_coord=R, new_coord=r, transform=r / lam)
    A_roundtrip = backward.transform_scale_factor(A_R, "temporal")

    assert sympy.simplify(A_roundtrip - A_r) == 0


def test_round_trip_radial():
    """Apply r = λR forward and backward for radial scale factor."""
    r, R, lam = sympy.symbols("r R lambda", positive=True)
    B_r = sympy.Function("B")(r)

    forward = CoordinateChange(old_coord=r, new_coord=R, transform=lam * R)
    B_R = forward.transform_scale_factor(B_r, "radial")

    backward = CoordinateChange(old_coord=R, new_coord=r, transform=r / lam)
    B_roundtrip = backward.transform_scale_factor(B_R, "radial")

    assert sympy.simplify(B_roundtrip - B_r) == 0


# -- Milestone 47: registration and validator ----------------------------------

def test_register_appears_in_dependency_graph():
    ctx = TheoryContext("coord_reg")
    r, R = sympy.symbols("r R", positive=True)
    change = CoordinateChange(old_coord=r, new_coord=R, transform=2 * R)
    change.register(ctx, derivation_id="test_radial_reparam")

    assert change.derivation_id == "test_radial_reparam"
    assert "test_radial_reparam" in ctx.dependencies._derivations
    record = ctx.dependencies._derivations["test_radial_reparam"]
    assert record.operation == "coordinate_change_chain_rule"


def test_invariance_validator_pass():
    """A constant expression is invariant under any coordinate change."""
    ctx = TheoryContext("inv_pass")
    r, R = sympy.symbols("r R", positive=True)
    change = CoordinateChange(old_coord=r, new_coord=R, transform=2 * R)
    result = validate_coordinate_invariance(ctx, "const_inv", sympy.Integer(1), change)
    assert result.status == "pass"


def test_invariance_validator_fail():
    """r itself is not invariant under r = 2R."""
    ctx = TheoryContext("inv_fail")
    r, R = sympy.symbols("r R", positive=True)
    change = CoordinateChange(old_coord=r, new_coord=R, transform=2 * R)
    result = validate_coordinate_invariance(ctx, "r_invariant", r, change)
    assert result.status == "fail"
    assert len(result.evidence) >= 1
