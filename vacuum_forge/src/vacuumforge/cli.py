"""Command-line interface for VacuumForge (M31).

Usage:
    vacuumforge new SESSION_NAME
    vacuumforge validate SESSION.yaml
    vacuumforge report SESSION.yaml --out report.md
    vacuumforge compare SESSION1.yaml SESSION2.yaml --out comparison.md
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def cmd_new(args: argparse.Namespace) -> None:
    """Create a new session file."""
    from vacuumforge import TheoryContext

    ctx = TheoryContext(args.name)
    ctx.define_equal_response_algebraic_symbols()

    out = args.out or f"{args.name}.yaml"
    ctx.save(out)
    print(f"Created new session: {out}")


def cmd_validate(args: argparse.Namespace) -> None:
    """Validate a session file."""
    from vacuumforge import TheoryContext

    ctx = TheoryContext.load(args.session)
    results = ctx.requirements.validate_all(ctx)
    summary = ctx.requirements.summary(results)
    print(summary)

    # Return non-zero if any failures
    if any(r.status == "fail" for r in results):
        sys.exit(1)


def cmd_report(args: argparse.Namespace) -> None:
    """Generate a validation report."""
    from vacuumforge import TheoryContext

    ctx = TheoryContext.load(args.session)
    handle = ctx.reports.validation()

    if args.out:
        handle.to_markdown(args.out)
        print(f"Report written to: {args.out}")
    else:
        print(handle.content)


def cmd_compare(args: argparse.Namespace) -> None:
    """Compare multiple session files."""
    from vacuumforge import TheoryContext
    from vacuumforge.comparison.compare import compare_models

    contexts = [TheoryContext.load(s) for s in args.sessions]
    comparison = compare_models(contexts)
    md = comparison.to_markdown()

    if args.out:
        Path(args.out).write_text(md, encoding="utf-8")
        print(f"Comparison written to: {args.out}")
    else:
        print(md)


def cmd_summary(args: argparse.Namespace) -> None:
    """Print a model summary."""
    from vacuumforge import TheoryContext

    ctx = TheoryContext.load(args.session)
    print(ctx.summary())


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="vacuumforge",
        description="VacuumForge: Symbolic research workbench for vacuum-based gravity theory.",
    )
    sub = parser.add_subparsers(dest="command")

    # new
    p_new = sub.add_parser("new", help="Create a new session")
    p_new.add_argument("name", help="Session name")
    p_new.add_argument("--out", help="Output file path")

    # validate
    p_val = sub.add_parser("validate", help="Validate a session")
    p_val.add_argument("session", help="Path to session YAML")

    # report
    p_rep = sub.add_parser("report", help="Generate a report")
    p_rep.add_argument("session", help="Path to session YAML")
    p_rep.add_argument("--out", help="Output markdown file")

    # compare
    p_cmp = sub.add_parser("compare", help="Compare sessions")
    p_cmp.add_argument("sessions", nargs="+", help="Paths to session YAMLs")
    p_cmp.add_argument("--out", help="Output markdown file")

    # summary
    p_sum = sub.add_parser("summary", help="Print model summary")
    p_sum.add_argument("session", help="Path to session YAML")

    return parser


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)

    commands = {
        "new": cmd_new,
        "validate": cmd_validate,
        "report": cmd_report,
        "compare": cmd_compare,
        "summary": cmd_summary,
    }

    if args.command in commands:
        commands[args.command](args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
