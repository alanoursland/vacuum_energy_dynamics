# candidate_status_decision_surface — Result Note

## Result

The script classifies the licensed status routes after the Group 62 obstruction.

Rejected:

```text
insert_now;
retain_unqualified;
zero_response;
repair_amplitude.
```

Allowed:

```text
retain_with_contract;
downgrade_diagnostic_only.
```

## Main Findings

This is the central Group 63 result.

The candidate cannot be inserted because stress accounting is not closed.

The candidate also cannot remain as an unqualified live candidate, because that would hide the obstruction and create candidate-hoarding drift.

The two clean statuses are:

```text
diagnostic-only downgrade;
conditional audit retention with explicit contract.
```

Diagnostic-only downgrade means the algebraic and boundary-layer lessons are kept, but the object is no longer treated as a candidate term.

Conditional audit retention means the object can stay in the candidate inventory only if its unresolved burdens remain attached.

## Boundary

This is a status decision surface, not a physical theorem.

## Steering Consequence

The next script should define diagnostic-only semantics so downgrade is not confused with deletion or with permission for physical use.
