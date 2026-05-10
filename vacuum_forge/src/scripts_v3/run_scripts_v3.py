"""Run scripts_v3 groups and capture their output under a mirrored results tree.

Usage:
    python run_scripts_v3.py <group-directory-name|all>

Examples:
    python run_scripts_v3.py 01_foundations
    python run_scripts_v3.py all
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path
import os


SCRIPT_ROOT = Path(__file__).resolve().parent
RESULTS_ROOT = SCRIPT_ROOT / "results"
SKIP_DIRS = {"results", "__pycache__"}


def print_usage() -> None:
    print("Usage: python run_scripts_v3.py <group-directory-name|all>")
    print()
    print("Examples:")
    print("  python run_scripts_v3.py 01_foundations")
    print("  python run_scripts_v3.py all")
    print()
    print("Available groups:")
    for group_dir in list_group_directories():
        print(f"  {group_dir.name}")


def list_group_directories() -> list[Path]:
    return sorted(
        [
            path
            for path in SCRIPT_ROOT.iterdir()
            if path.is_dir() and path.name not in SKIP_DIRS
        ],
        key=lambda path: path.name,
    )


def read_group_order(group_dir: Path) -> list[Path]:
    order_file = group_dir / "order.txt"
    if order_file.exists():
        ordered_paths: list[Path] = []
        for raw_line in order_file.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue
            candidate = group_dir / line
            if candidate.suffix != ".py":
                candidate = candidate.with_suffix(".py")
            if not candidate.exists():
                raise FileNotFoundError(
                    f"Listed script does not exist in {group_dir.name}: {line}"
                )
            ordered_paths.append(candidate)
        return ordered_paths

    return sorted(
        [
            path
            for path in group_dir.glob("*.py")
            if path.name != Path(__file__).name
        ],
        key=lambda path: path.name,
    )


def resolve_requested_groups(arg: str) -> list[Path]:
    all_groups = list_group_directories()
    if arg == "all":
        return all_groups

    exact = [path for path in all_groups if path.name == arg]
    if exact:
        return exact

    raise ValueError(f"Unknown group '{arg}'.")


def build_output_path(script_path: Path) -> Path:
    relative = script_path.relative_to(SCRIPT_ROOT)
    return (RESULTS_ROOT / relative).with_suffix(".txt")


def print_failure_details(script_path: Path, completed: subprocess.CompletedProcess[str]) -> None:
    relative = script_path.relative_to(SCRIPT_ROOT)
    if completed.stderr:
        print(f"[stderr] {relative}")
        print(completed.stderr, end="" if completed.stderr.endswith("\n") else "\n")
    if not completed.stderr:
        print(f"[stderr] {relative}")
        print(f"Script exited with code {completed.returncode} and produced no output.")


def run_script(script_path: Path) -> int:
    output_path = build_output_path(script_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"[RUN ] {script_path.relative_to(SCRIPT_ROOT)}")
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    existing_pythonpath = env.get("PYTHONPATH", "")
    src_root = str(SCRIPT_ROOT.parent)
    env["PYTHONPATH"] = src_root if not existing_pythonpath else os.pathsep.join([src_root, existing_pythonpath])

    completed = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=str(SCRIPT_ROOT.parent),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        env=env,
    )

    combined_output = completed.stdout
    if completed.stderr:
        if combined_output and not combined_output.endswith("\n"):
            combined_output += "\n"
        combined_output += "\n[stderr]\n"
        combined_output += completed.stderr
    if completed.returncode != 0:
        combined_output = f"[SCRIPT_FAILED]\nexit_code={completed.returncode}\n\n" + combined_output

    output_path.write_text(combined_output, encoding="utf-8")

    relative = script_path.relative_to(SCRIPT_ROOT)
    status = "PASS" if completed.returncode == 0 else "FAIL"
    print(f"[{status}] {relative} -> {output_path.relative_to(SCRIPT_ROOT)}")
    if completed.returncode != 0:
        print_failure_details(script_path, completed)
    return completed.returncode


def run_group(group_dir: Path) -> int:
    print()
    print(f"=== Running group: {group_dir.name} ===")
    scripts = read_group_order(group_dir)
    if not scripts:
        print(f"[SKIP] {group_dir.name}: no scripts found")
        return 0

    failures = 0
    for script_path in scripts:
        code = run_script(script_path)
        if code != 0:
            failures += 1
    print(f"=== Completed group: {group_dir.name} ({len(scripts)} scripts, {failures} failures) ===")
    return failures


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print_usage()
        return 1

    arg = argv[1].strip()
    try:
        groups = resolve_requested_groups(arg)
    except ValueError as exc:
        print(exc)
        print()
        print_usage()
        return 1

    total_failures = 0
    for group_dir in groups:
        total_failures += run_group(group_dir)

    print()
    print(f"Finished. Total group failures: {total_failures}")
    return 0 if total_failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
