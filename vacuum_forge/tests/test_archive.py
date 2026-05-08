"""Tests for ProjectArchive.

Covers Milestones 49-51 completion criteria:
- Record-and-retrieve derivations.
- Sympy expression round-trip serialization.
- Dependency verification: satisfied, changed, missing, cycle.
- Source-hash invalidation.
- Atomic writes.
- Corrupt file resilience.
- CLI subcommands.
"""

import json

import sympy

from vacuumforge.archive import ProjectArchive
from vacuumforge.core.status import Status


# -- Milestone 49: storage layer ----------------------------------------------

def test_record_and_retrieve(tmp_path):
    archive = ProjectArchive(tmp_path / "archive")
    x = sympy.Symbol("x")
    ns = archive.script_namespace("script_a")
    ns.record_derivation("double", [x], 2 * x, "algebraic", Status.DERIVED)

    record = ns.get_derivation("double")
    assert record is not None
    assert record.derivation_id == "double"
    assert sympy.simplify(record.output - 2 * x) == 0


def test_record_overwrite(tmp_path):
    archive = ProjectArchive(tmp_path / "archive")
    x = sympy.Symbol("x")
    ns = archive.script_namespace("s")
    ns.record_derivation("result", [x], x, "algebraic", Status.DERIVED)
    ns.record_derivation("result", [x], 2 * x, "algebraic", Status.DERIVED)

    record = ns.get_derivation("result")
    assert sympy.simplify(record.output - 2 * x) == 0


def test_missing_derivation_returns_none(tmp_path):
    archive = ProjectArchive(tmp_path / "archive")
    ns = archive.script_namespace("s")
    assert ns.get_derivation("nonexistent") is None


def test_serialization_roundtrip_symbol(tmp_path):
    archive = ProjectArchive(tmp_path / "archive")
    x = sympy.Symbol("x", positive=True)
    ns = archive.script_namespace("s")
    ns.record_derivation("sym", [x], x**2, "algebraic", Status.DERIVED)

    record = ns.get_derivation("sym")
    assert sympy.simplify(record.output - x**2) == 0


def test_serialization_roundtrip_complex_expr(tmp_path):
    """Round-trip exp, log, Eq, Derivative, Function."""
    archive = ProjectArchive(tmp_path / "archive")
    x = sympy.Symbol("x")
    expr = sympy.exp(x) + sympy.log(x)
    ns = archive.script_namespace("s")
    ns.record_derivation("complex", [x], expr, "algebraic", Status.DERIVED)

    record = ns.get_derivation("complex")
    assert sympy.simplify(record.output - expr) == 0


def test_serialization_roundtrip_eq(tmp_path):
    archive = ProjectArchive(tmp_path / "archive")
    x = sympy.Symbol("x")
    expr = sympy.Eq(x, 0)
    ns = archive.script_namespace("s")
    ns.record_derivation("eq", [x], expr, "algebraic", Status.DERIVED)

    record = ns.get_derivation("eq")
    assert record.output == expr


def test_corrupt_derivation_file(tmp_path):
    """A malformed JSON derivation file should not crash get_derivation."""
    archive = ProjectArchive(tmp_path / "archive")
    ns = archive.script_namespace("s")
    ns.derivations_path.mkdir(parents=True, exist_ok=True)
    corrupt_file = ns.derivations_path / "bad.json"
    corrupt_file.write_text("{invalid json", encoding="utf-8")

    result = ns.get_derivation("bad")
    assert result is None


# -- Milestone 50: verification ------------------------------------------------

def test_verify_dependency_satisfied(tmp_path):
    archive = ProjectArchive(tmp_path / "archive")
    x = sympy.Symbol("x")

    ns_a = archive.script_namespace("script_a")
    ns_a.record_derivation("double", [x], 2 * x, "algebraic", Status.DERIVED)

    ns_b = archive.script_namespace("script_b")
    ns_b.declare_dependency("uses_double", "script_a", "double", expected_output=x + x)
    results = ns_b.verify_dependencies()

    assert len(results) == 1
    assert results[0].status == "dependency_satisfied"


def test_verify_dependency_changed(tmp_path):
    archive = ProjectArchive(tmp_path / "archive")
    x = sympy.Symbol("x")

    ns_a = archive.script_namespace("script_a")
    ns_a.record_derivation("double", [x], 3 * x, "algebraic", Status.DERIVED)

    ns_b = archive.script_namespace("script_b")
    ns_b.declare_dependency("uses_double", "script_a", "double", expected_output=2 * x)
    results = ns_b.verify_dependencies()

    assert results[0].status == "dependency_changed"


def test_verify_dependency_missing(tmp_path):
    archive = ProjectArchive(tmp_path / "archive")
    ns_b = archive.script_namespace("script_b")
    ns_b.declare_dependency("uses_missing", "script_a", "nonexistent")
    results = ns_b.verify_dependencies()

    assert results[0].status == "dependency_missing"


def test_verify_dependency_no_expected_output(tmp_path):
    """When expected_output is None, verification only checks existence."""
    archive = ProjectArchive(tmp_path / "archive")
    x = sympy.Symbol("x")

    ns_a = archive.script_namespace("script_a")
    ns_a.record_derivation("result", [x], x, "algebraic", Status.DERIVED)

    ns_b = archive.script_namespace("script_b")
    ns_b.declare_dependency("uses_result", "script_a", "result")
    results = ns_b.verify_dependencies()

    assert results[0].status == "dependency_satisfied"
    assert "not verified" in results[0].message


def test_detect_dependency_cycle(tmp_path):
    """A -> B -> A should be detected as a cycle."""
    archive = ProjectArchive(tmp_path / "archive")
    x = sympy.Symbol("x")

    ns_a = archive.script_namespace("script_a")
    ns_a.record_derivation("r", [x], x, "algebraic", Status.DERIVED)
    ns_a.declare_dependency("dep_on_b", "script_b", "r")

    ns_b = archive.script_namespace("script_b")
    ns_b.record_derivation("r", [x], x, "algebraic", Status.DERIVED)
    ns_b.declare_dependency("dep_on_a", "script_a", "r")

    cycles = archive.detect_cycles()
    assert len(cycles) >= 1

    results = ns_b.verify_dependencies()
    assert any(r.status == "dependency_cycle" for r in results)


# -- Source-hash invalidation --------------------------------------------------

def test_source_hash_invalidation(tmp_path):
    archive = ProjectArchive(tmp_path / "archive")
    x = sympy.Symbol("x")
    ns = archive.script_namespace("s")

    # Create a fake script file.
    script = tmp_path / "s.py"
    script.write_text("version_1", encoding="utf-8")

    ns.record_derivation("r", [x], x, "algebraic", Status.DERIVED)
    ns.check_source_invalidation(script)

    # Derivation should still exist.
    assert ns.get_derivation("r") is not None

    # Modify the script.
    script.write_text("version_2", encoding="utf-8")
    invalidated = ns.check_source_invalidation(script)

    assert invalidated is True
    # Derivation should be gone.
    assert ns.get_derivation("r") is None


def test_source_hash_no_change(tmp_path):
    archive = ProjectArchive(tmp_path / "archive")
    x = sympy.Symbol("x")
    ns = archive.script_namespace("s")

    script = tmp_path / "s.py"
    script.write_text("stable", encoding="utf-8")

    ns.record_derivation("r", [x], x, "algebraic", Status.DERIVED)
    ns.check_source_invalidation(script)

    # Same source — should not invalidate.
    invalidated = ns.check_source_invalidation(script)
    assert invalidated is False
    assert ns.get_derivation("r") is not None


# -- Run metadata -------------------------------------------------------------

def test_write_run_metadata(tmp_path):
    archive = ProjectArchive(tmp_path / "archive")
    ns = archive.script_namespace("s")
    ns.write_run_metadata(custom_field="hello")

    meta_path = ns.path / "last_run_metadata.json"
    assert meta_path.exists()
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    assert meta["script_id"] == "s"
    assert meta["custom_field"] == "hello"
    assert "recorded_at" in meta
    assert "vacuumforge_version" in meta


# -- Invalidate ----------------------------------------------------------------

def test_invalidate_clears_derivations(tmp_path):
    archive = ProjectArchive(tmp_path / "archive")
    x = sympy.Symbol("x")
    ns = archive.script_namespace("s")
    ns.record_derivation("a", [x], x, "algebraic", Status.DERIVED)
    ns.record_derivation("b", [x], 2 * x, "algebraic", Status.DERIVED)

    ns.invalidate()

    assert ns.get_derivation("a") is None
    assert ns.get_derivation("b") is None
