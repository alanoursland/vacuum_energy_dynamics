"""Run field-equation trial scripts and capture logs under the proof archive.

Usage from vacuum_forge/src:
    python field_equation_trials/run_all.py [all|group-directory-name|group+]

Examples:
    python field_equation_trials/run_all.py
    python field_equation_trials/run_all.py all
    python field_equation_trials/run_all.py 008_radiative_bootstrap
    python field_equation_trials/run_all.py 008_radiative_bootstrap+

Each trial folder supplies its local order in order.txt. The runner keeps
that local order, then applies the small known cross-folder dependency move
needed by E3, whose P7' scalaron appeal check depends on the G20 archive.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path


SRC_ROOT = Path(__file__).resolve().parents[1]
TRIAL_ROOT = Path(__file__).resolve().parent
ARCHIVE_ROOT = TRIAL_ROOT / ".vacuumforge_archive"
LOG_ROOT = ARCHIVE_ROOT / "run_logs"
SKIP_DIRS = {".vacuumforge_archive", "__pycache__"}


CROSS_FOLDER_AFTER = {
    # E3 depends on G20's alpha_one_third_g20. Keep 009/order.txt as the
    # within-folder order, but move E3 after the G20 gate globally.
    "009_trial_E_boundary_admissibility/trial_E3_p7prime_vs_scalaron.py":
        "010_gate_G20_beta_health/gate_G20_beta_health.py",
}


def list_trial_directories() -> list[Path]:
    return sorted(
        [
            path
            for path in TRIAL_ROOT.iterdir()
            if path.is_dir() and path.name not in SKIP_DIRS
        ],
        key=lambda path: path.name,
    )


def read_group_order(group_dir: Path) -> list[Path]:
    path = group_dir / "order.txt"
    if not path.exists():
        return sorted(group_dir.glob("*.py"), key=lambda p: p.name)

    scripts: list[Path] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
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
        scripts.append(candidate)
    return scripts


def resolve_requested_groups(arg: str) -> list[Path]:
    groups = list_trial_directories()
    if arg == "all":
        return groups

    if arg.endswith("+"):
        group_name = arg[:-1]
        matching = [path for path in groups if path.name == group_name]
        if not matching:
            raise ValueError(f"Unknown group '{group_name}'.")
        return groups[groups.index(matching[0]):]

    exact = [path for path in groups if path.name == arg]
    if exact:
        return exact

    raise ValueError(f"Unknown group '{arg}'.")


def apply_cross_folder_ordering(scripts: list[Path]) -> list[Path]:
    ordered = scripts[:]
    for script_rel, dependency_rel in CROSS_FOLDER_AFTER.items():
        script = TRIAL_ROOT / script_rel
        dependency = TRIAL_ROOT / dependency_rel
        if script not in ordered or dependency not in ordered:
            continue
        ordered.remove(script)
        dependency_index = ordered.index(dependency)
        ordered.insert(dependency_index + 1, script)
    return ordered


def discover_ordered_scripts(groups: list[Path]) -> list[Path]:
    scripts: list[Path] = []
    for group_dir in groups:
        scripts.extend(read_group_order(group_dir))

    return apply_cross_folder_ordering(scripts)


def print_usage() -> None:
    print("Usage: python field_equation_trials/run_all.py [all|group-directory-name|group+]")
    print()
    print("Examples:")
    print("  python field_equation_trials/run_all.py")
    print("  python field_equation_trials/run_all.py all")
    print("  python field_equation_trials/run_all.py 008_radiative_bootstrap")
    print("  python field_equation_trials/run_all.py 008_radiative_bootstrap+")
    print()
    print("Available groups:")
    for group_dir in list_trial_directories():
        print(f"  {group_dir.name}")


def build_env() -> dict[str, str]:
    env = os.environ.copy()
    existing = env.get("PYTHONPATH")
    root = str(SRC_ROOT)
    env["PYTHONPATH"] = root if not existing else root + os.pathsep + existing
    return env


def run_script(script: Path, env: dict[str, str], log_dir: Path) -> int:
    script_rel = script.relative_to(TRIAL_ROOT)
    log_file = log_dir / (str(script_rel).replace("/", "__").replace("\\", "__") + ".log")
    command = [sys.executable, str(script)]

    print()
    print("=" * 120)
    print(f"RUN {script_rel}")
    print("=" * 120)

    proc = subprocess.run(
        command,
        cwd=str(SRC_ROOT),
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )

    log_file.write_text(proc.stdout, encoding="utf-8")
    print(proc.stdout)
    print(f"[run_all] {script_rel}: exit={proc.returncode}; log={log_file}")
    return proc.returncode


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "target",
        nargs="?",
        default="all",
        help="Trial group, group+ range, or all. Defaults to all.",
    )
    parser.add_argument(
        "--continue-on-failure",
        action="store_true",
        help="Run remaining scripts after a failure and return nonzero at the end.",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="Print the ordered script list and exit.",
    )
    args = parser.parse_args()

    try:
        groups = resolve_requested_groups(args.target)
    except ValueError as exc:
        print(exc)
        print()
        print_usage()
        return 1

    if args.list:
        for script in discover_ordered_scripts(groups):
            print(script.relative_to(TRIAL_ROOT))
        return 0

    ordered_scripts = discover_ordered_scripts(groups)
    missing = [script for script in ordered_scripts if not script.exists()]
    if missing:
        print("[run_all] Missing scripts:")
        for script in missing:
            print(f"  - {script.relative_to(TRIAL_ROOT)}")
        return 2

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_dir = LOG_ROOT / stamp
    log_dir.mkdir(parents=True, exist_ok=True)

    env = build_env()
    failures: list[tuple[Path, int]] = []
    attempted = 0
    for script in ordered_scripts:
        attempted += 1
        code = run_script(script, env, log_dir)
        if code != 0:
            failures.append((script, code))
            if not args.continue_on_failure:
                break

    print()
    print("=" * 120)
    print("SUMMARY")
    print("=" * 120)
    print(f"scripts attempted: {attempted}")
    print(f"logs: {log_dir}")
    if failures:
        print("failures:")
        for script, code in failures:
            print(f"  - {script.relative_to(TRIAL_ROOT)}: exit={code}")
        return 1

    print("all scripts passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
