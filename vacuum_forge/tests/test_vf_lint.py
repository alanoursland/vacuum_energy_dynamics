"""Tests for the standalone vf-lint analyzer.

Covers Milestones 42-44 completion criteria:
- All three pattern types detected.
- Dataclass-literal verdicts classified as FAIL.
- Unconditional PASS classified as WARN.
- PASS gated on ``if True`` classified as WARN.
- PASS gated on ``if is_zero(expr)`` classified as OK.
- Trace-back through variable assignment to validation call classified as OK.
- Missing validation imports flagged.
- JSON output is well-formed.
- Quiet mode suppresses non-FAIL output.
"""

from pathlib import Path

from tools.vf_lint.analyzer import lint_file


# -- Pattern detection (Milestone 42) -----------------------------------------

def test_detects_dataclass_literal(tmp_path: Path):
    script = tmp_path / "bad.py"
    script.write_text("Entry(status='PASS')\n", encoding="utf-8")
    result = lint_file(script)
    assert result.severity == "FAIL"
    assert result.classifications[0].rule_name == "verdict_in_dataclass_literal"


def test_detects_multiple_dataclass_literals(tmp_path: Path):
    script = tmp_path / "bad.py"
    script.write_text(
        "Entry(status='CLOSED')\nEntry(status='DERIVED')\nEntry(status='DEFER')\n",
        encoding="utf-8",
    )
    result = lint_file(script)
    assert result.severity == "FAIL"
    dataclass_hits = [c for c in result.classifications if c.site.pattern == "dataclass_status"]
    assert len(dataclass_hits) == 3


def test_detects_print_verdict(tmp_path: Path):
    script = tmp_path / "p.py"
    script.write_text("print('[PASS] ok')\n", encoding="utf-8")
    result = lint_file(script)
    assert len(result.classifications) >= 1
    assert any(c.site.pattern == "pass_print" for c in result.classifications)


def test_detects_status_line(tmp_path: Path):
    script = tmp_path / "s.py"
    script.write_text("status_line('test', True)\n", encoding="utf-8")
    result = lint_file(script)
    assert any(c.site.pattern == "status_line" for c in result.classifications)


def test_verdict_site_has_column(tmp_path: Path):
    script = tmp_path / "col.py"
    script.write_text("Entry(status='PASS')\n", encoding="utf-8")
    result = lint_file(script)
    site = result.classifications[0].site
    assert hasattr(site, "column")
    assert isinstance(site.column, int)


def test_handles_syntax_error(tmp_path: Path):
    script = tmp_path / "broken.py"
    script.write_text("def (:\n", encoding="utf-8")
    result = lint_file(script)
    assert result.syntax_error is not None
    assert result.severity == "FAIL"


# -- Trace-back analysis (Milestone 43) ---------------------------------------

def test_validation_gated_pass_is_ok(tmp_path: Path):
    script = tmp_path / "good.py"
    script.write_text(
        "from vacuumforge.core.simplify import is_zero\n"
        "if is_zero(x):\n"
        "    print('[PASS] ok')\n",
        encoding="utf-8",
    )
    result = lint_file(script)
    assert result.severity == "OK"


def test_unconditional_pass_is_warn(tmp_path: Path):
    script = tmp_path / "uncond.py"
    script.write_text("print('[PASS] done')\n", encoding="utf-8")
    result = lint_file(script)
    assert result.severity == "WARN"
    assert any(c.rule_name == "unconditional_pass_print" for c in result.classifications)


def test_literal_gate_is_warn(tmp_path: Path):
    script = tmp_path / "lit.py"
    script.write_text(
        "if True:\n"
        "    print('[PASS] always')\n",
        encoding="utf-8",
    )
    result = lint_file(script)
    assert result.severity == "WARN"


def test_traceback_through_variable(tmp_path: Path):
    """PASS gated on a variable assigned from is_zero() should be OK."""
    script = tmp_path / "trace.py"
    script.write_text(
        "from vacuumforge.core.simplify import is_zero\n"
        "result = is_zero(expr)\n"
        "if result:\n"
        "    print('[PASS] traced')\n",
        encoding="utf-8",
    )
    result = lint_file(script)
    assert result.severity == "OK"


def test_traceback_literal_returning_function_is_warn(tmp_path: Path):
    """PASS gated on ``if my_func()`` where my_func is not a validation call."""
    script = tmp_path / "non_val.py"
    script.write_text(
        "def my_func():\n"
        "    return True\n"
        "if my_func():\n"
        "    print('[PASS] not validated')\n",
        encoding="utf-8",
    )
    result = lint_file(script)
    assert result.severity == "WARN"


def test_status_line_literal_is_warn(tmp_path: Path):
    script = tmp_path / "sl.py"
    script.write_text("status_line('test', True)\n", encoding="utf-8")
    result = lint_file(script)
    assert result.severity == "WARN"
    assert any(c.rule_name == "status_line_with_literal" for c in result.classifications)


def test_status_line_validation_is_ok(tmp_path: Path):
    script = tmp_path / "sl_ok.py"
    script.write_text(
        "from vacuumforge.core.simplify import is_zero\n"
        "status_line('test', is_zero(x))\n",
        encoding="utf-8",
    )
    result = lint_file(script)
    verdicts = [c for c in result.classifications if c.site.pattern == "status_line"]
    assert all(c.severity == "OK" for c in verdicts)


def test_status_line_no_computation_is_warn(tmp_path: Path):
    script = tmp_path / "sl_nc.py"
    script.write_text("status_line('test', len([1, 2]) == 2)\n", encoding="utf-8")
    result = lint_file(script)
    assert result.severity == "WARN"
    assert any(c.rule_name == "status_line_with_no_computation" for c in result.classifications)


# -- Import awareness (Milestone 43) ------------------------------------------

def test_import_alias_recognized(tmp_path: Path):
    """``import sympy as sp; sp.simplify(...)`` should be recognized."""
    script = tmp_path / "alias.py"
    script.write_text(
        "import sympy as sp\n"
        "if sp.simplify(x) == 0:\n"
        "    print('[PASS] simplified')\n",
        encoding="utf-8",
    )
    result = lint_file(script)
    assert result.severity == "OK"


def test_missing_validation_imports_flagged(tmp_path: Path):
    script = tmp_path / "no_imports.py"
    script.write_text(
        "Entry(status='PASS')\n"
        "print('[PASS] nothing imported')\n",
        encoding="utf-8",
    )
    result = lint_file(script)
    assert not result.has_validation_imports
    assert any(c.rule_name == "missing_validation_imports" for c in result.classifications)


# -- Mixed scripts (Milestone 43) ---------------------------------------------

def test_partial_validation_produces_mixed(tmp_path: Path):
    """A script with some real and some hardcoded verdicts should produce
    a mix of OK and WARN/FAIL, and overall severity should not be OK."""
    script = tmp_path / "mixed.py"
    script.write_text(
        "from vacuumforge.core.simplify import is_zero\n"
        "if is_zero(expr):\n"
        "    print('[PASS] real')\n"
        "print('[PASS] hardcoded')\n",
        encoding="utf-8",
    )
    result = lint_file(script)
    severities = {c.severity for c in result.classifications}
    assert "OK" in severities
    assert "WARN" in severities
    assert result.severity == "WARN"


# -- Output formats (Milestone 44) --------------------------------------------

def test_json_output(tmp_path: Path):
    from tools.vf_lint.cli import _result_to_json
    script = tmp_path / "j.py"
    script.write_text("Entry(status='PASS')\n", encoding="utf-8")
    result = lint_file(script)
    j = _result_to_json(result)
    assert j["classification"] == "FAIL"
    assert isinstance(j["violations"], list)
    assert len(j["violations"]) >= 1
    assert "column" in j["violations"][0]


def test_quiet_mode(tmp_path: Path, capsys):
    from tools.vf_lint.cli import main as cli_main
    good = tmp_path / "good.py"
    good.write_text(
        "from vacuumforge.core.simplify import is_zero\n"
        "if is_zero(x):\n"
        "    print('[PASS] ok')\n",
        encoding="utf-8",
    )
    bad = tmp_path / "bad.py"
    bad.write_text("Entry(status='PASS')\n", encoding="utf-8")
    code = cli_main(["--quiet", str(good), str(bad)])
    captured = capsys.readouterr()
    # Quiet mode should suppress the good script.
    assert "good.py" not in captured.out
    # Bad script should still appear.
    assert "bad.py" in captured.out
    assert code == 2
