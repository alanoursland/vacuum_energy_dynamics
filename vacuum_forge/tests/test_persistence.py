"""Tests for session persistence."""

import os
import tempfile

import sympy
from vacuumforge import TheoryContext


def test_save_and_load_roundtrip():
    """Save a context and load it back."""
    ctx = TheoryContext("persistence_test")
    ms = ctx.define_equal_response_algebraic_symbols()
    ctx.assumptions.add("A_exp", sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)))
    ctx.assumptions.add("B_exp", sympy.Eq(ms.B, sympy.exp(-ms.Phi / ms.c**2)))

    Js = sympy.Symbol("J_s")
    ctx.sources.exchange_trace_free(Js)
    ctx.energy.quadratic_modes(ms.C_kappa, ms.C_sigma, ms.kappa, ms.sigma)

    with tempfile.NamedTemporaryFile(suffix=".yaml", delete=False, mode="w") as f:
        path = f.name

    try:
        ctx.save(path)

        # Load it back
        ctx2 = TheoryContext.load(path)
        assert ctx2.name == "persistence_test"
        assert ctx2.assumptions.has("A_exp")
        assert ctx2.assumptions.has("B_exp")
        assert ctx2.sources.has("exchange")
        assert ctx2.energy.has("quadratic_mode_energy")

        # Validate that the loaded context still works
        results = ctx2.requirements.validate_all(ctx2)
        rs = {r.requirement_id: r for r in results}
        assert rs["reciprocal_scaling"].status == "pass"
        assert rs["gamma_v_one"].status == "pass"
    finally:
        os.unlink(path)


def test_save_contains_version():
    """Session file includes version metadata."""
    import yaml

    ctx = TheoryContext("version_test")
    ctx.define_equal_response_algebraic_symbols()

    with tempfile.NamedTemporaryFile(suffix=".yaml", delete=False, mode="w") as f:
        path = f.name

    try:
        ctx.save(path)
        with open(path, "r") as f:
            data = yaml.safe_load(f)
        assert "vacuumforge_version" in data
        assert data["vacuumforge_version"] == "0.1.0"
    finally:
        os.unlink(path)
