#!/usr/bin/env python3
"""
make_1_archive_survivor_guardrail_audit.py

Audit the field_equation_candidates postmortem for the surviving branch and
the guardrails that should constrain future proof work.

Output:
    1_archive_survivor_guardrail_audit.md
"""

from pathlib import Path


here = Path(__file__).resolve().parent
development = Path(__file__).resolve().parents[2]
field_candidates = development / "field_equation_candidates"
postmortem_path = field_candidates / "postmortem.md"

if not postmortem_path.exists():
    raise AssertionError(f"missing postmortem: {postmortem_path}")

postmortem = postmortem_path.read_text(encoding="utf-8")

required_phrases = [
    "archive of guardrails, diagnostics, and reduced mathematical artifacts",
    "formal weighted projection hierarchy with possible admissibility significance",
    "theory_v3/development/projection_origin_probe",
    "No object, no theorem attempt.",
    "No compatibility-only promotion.",
    "No diagnostic promotion.",
    "No parent equation before conservation identity.",
    "No physical ledger assignment without source/origin.",
]

missing = [phrase for phrase in required_phrases if phrase not in postmortem]
if missing:
    raise AssertionError(f"postmortem missing required guardrails: {missing}")

projection_probe = development / "projection_origin_probe"
required_probe_reports = [
    projection_probe / "regularity_admissibility_ladder" / "34_ladder_conclusion_report.md",
    projection_probe / "boundary_flux_field_bridge" / "75_scalar_bridge_final_status.md",
    projection_probe / "geometric_field_lift" / "97_geometric_lift_final_status.md",
    projection_probe / "einstein_hilbert_origin_tests" / "126_status_after_assumption_origin_gates.md",
    projection_probe / "vacuum_action_origin" / "33_vacuum_action_origin_conclusion.md",
]

missing_reports = [str(path) for path in required_probe_reports if not path.exists()]
if missing_reports:
    raise AssertionError(f"missing migrated proof-chain reports: {missing_reports}")

validation_bullets = "\n".join(
    "- " + item + ": passed"
    for item in [
        "field_equation_candidates postmortem exists",
        "archive status guardrail phrases present",
        "projection_origin_probe successor path present",
        "migrated proof-chain reports present",
    ]
)

report_lines = "\n".join("- `" + str(path.relative_to(development)) + "`" for path in required_probe_reports)

md = f"""# Field Search Survivor Audit 1: Archive Guardrails

## Purpose

This report checks the status of the old `field_equation_candidates` search
before extracting further proof work from it.

## Validated Checks

{validation_bullets}

## Archive Status

The postmortem marks `field_equation_candidates` as:

```text
archive of guardrails, diagnostics, and reduced mathematical artifacts
```

It also identifies the surviving branch as:

```text
formal weighted projection hierarchy with possible admissibility significance
```

and recommends:

```text
theory_v3/development/projection_origin_probe
```

as the successor directory.

## Guardrails Preserved

The postmortem explicitly preserves these decision rules:

```text
No object, no theorem attempt.
No compatibility-only promotion.
No diagnostic promotion.
No parent equation before conservation identity.
No physical ledger assignment without source/origin.
```

## Migrated Proof Chain Present

The audit found these migrated proof-chain reports:

{report_lines}

## Interpretation

The old search tree should not be resumed as a field-equation generator. Its
useful role is to supply guardrails and the projection hierarchy that the later
focused folders tested.
"""

out = here / "1_archive_survivor_guardrail_audit.md"
out.write_text(md, encoding="utf-8")

print("All archive guardrail checks passed.")
print(f"Wrote {out.resolve()}")
