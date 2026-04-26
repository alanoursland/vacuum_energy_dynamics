"""Tests for CLI interface (M31)."""

import os
import tempfile

import sympy
from vacuumforge import TheoryContext
from vacuumforge.cli import main, build_parser


def test_parser_new():
    parser = build_parser()
    args = parser.parse_args(["new", "test_session"])
    assert args.command == "new"
    assert args.name == "test_session"


def test_parser_validate():
    parser = build_parser()
    args = parser.parse_args(["validate", "session.yaml"])
    assert args.command == "validate"
    assert args.session == "session.yaml"


def test_cli_new_and_validate():
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, "test.yaml")
        main(["new", "cli_test", "--out", path])
        assert os.path.exists(path)

        # Validate the created session (may exit with 0 or 1)
        # Since no assumptions are set, some requirements will be undetermined
        try:
            main(["validate", path])
        except SystemExit:
            pass  # Expected if some requirements are undetermined


def test_cli_report():
    with tempfile.TemporaryDirectory() as tmpdir:
        session_path = os.path.join(tmpdir, "session.yaml")
        report_path = os.path.join(tmpdir, "report.md")

        ctx = TheoryContext("report_test")
        ms = ctx.define_equal_response_algebraic_symbols()
        ctx.assumptions.add("A_exp", sympy.Eq(ms.A, sympy.exp(ms.Phi / ms.c**2)))
        ctx.assumptions.add("B_exp", sympy.Eq(ms.B, sympy.exp(-ms.Phi / ms.c**2)))
        ctx.save(session_path)

        main(["report", session_path, "--out", report_path])
        assert os.path.exists(report_path)
        with open(report_path) as f:
            content = f.read()
        assert "Validation Report" in content
