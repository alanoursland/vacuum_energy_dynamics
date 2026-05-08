"""Command line interface for vf-lint."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .analyzer import FileLintResult, lint_file

EXIT_CODES = {"OK": 0, "WARN": 1, "FAIL": 2}


def main(argv: list[str] | None = None) -> int:
    """Entry point. Returns 0 if all files pass, 1 if any warn, 2 if any fail."""
    parser = argparse.ArgumentParser(prog="vf-lint")
    parser.add_argument("files", nargs="+", help="Python files to lint")
    parser.add_argument("--format", choices=["human", "json"], default="human",
                        help="Output format (default: human)")
    parser.add_argument("--quiet", action="store_true",
                        help="Only print FAIL results")
    parser.add_argument("--config", default=None,
                        help="Path to vf_lint.toml config file")
    args = parser.parse_args(argv)

    rule_overrides = _load_config(args.config)
    results = [lint_file(Path(p)) for p in args.files]

    # Apply rule severity overrides.
    if rule_overrides:
        for result in results:
            _apply_overrides(result, rule_overrides)

    if args.format == "json":
        print(json.dumps([_result_to_json(r) for r in results], indent=2))
    else:
        for result in results:
            if args.quiet and result.severity != "FAIL":
                continue
            print(_format_human(result))

    severities = [r.severity for r in results]
    return max(EXIT_CODES.get(s, 0) for s in severities)


def _load_config(config_path: str | None) -> dict[str, str]:
    """Load rule severity overrides from a vf_lint.toml file.

    Returns a dict mapping rule_name -> severity_override.
    """
    if config_path is not None:
        path = Path(config_path)
    else:
        path = Path("vf_lint.toml")
    if not path.exists():
        return {}

    try:
        import tomllib
    except ModuleNotFoundError:
        try:
            import tomli as tomllib  # type: ignore[no-redef]
        except ModuleNotFoundError:
            return {}

    with open(path, "rb") as f:
        data = tomllib.load(f)

    overrides: dict[str, str] = {}
    rules_section = data.get("rules", {})
    for rule_name, rule_config in rules_section.items():
        if isinstance(rule_config, dict) and "severity" in rule_config:
            overrides[rule_name] = rule_config["severity"]
    return overrides


def _apply_overrides(result: FileLintResult, overrides: dict[str, str]) -> None:
    """Mutate classifications in *result* to apply severity overrides."""
    for cls in result.classifications:
        if cls.rule_name in overrides:
            cls.severity = overrides[cls.rule_name]


def _result_to_json(result: FileLintResult) -> dict[str, object]:
    return {
        "file": str(result.path),
        "classification": result.severity,
        "has_validation_imports": result.has_validation_imports,
        "syntax_error": result.syntax_error,
        "violations": [
            {
                "line": c.site.line,
                "column": c.site.column,
                "severity": c.severity,
                "pattern": c.site.pattern,
                "rule": c.rule_name,
                "message": c.message,
            }
            for c in result.classifications
            if c.severity != "OK"
        ],
    }


def _format_human(result: FileLintResult) -> str:
    if result.syntax_error:
        return f"{result.path}: FAIL\n  {result.syntax_error}"
    violations = [c for c in result.classifications if c.severity != "OK"]
    if not violations:
        total = len(result.classifications)
        return f"{result.path}: OK ({total} verdict sites, all gated on real computation)"
    lines = [f"{result.path}: {result.severity}"]
    for c in violations:
        lines.append(f"  Line {c.site.line}: {c.message} ({c.site.pattern})")
    if not result.has_validation_imports:
        lines.append("  No sympy or vacuumforge imports detected.")
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
