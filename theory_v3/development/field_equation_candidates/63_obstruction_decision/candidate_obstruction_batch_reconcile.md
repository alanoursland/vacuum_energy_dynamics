# candidate_obstruction_batch_reconcile — Result Note

## Result

The reconciliation confirms that Group 63 classified the obstructed transition response without falsely solving or inserting it.

Stable status:

```text
obstruction status classified;
insertion rejected;
unqualified retention rejected;
diagnostic-only downgrade allowed and defined;
conditional audit retention allowed only with explicit contract;
valid future routes must derive something real;
stress accounting remains unclosed;
physical use remains blocked.
```

## Main Findings

The reconciliation preserves the important distinction between:

```text
diagnostic-only downgrade
```

and:

```text
conditional audit retention.
```

Diagnostic-only downgrade preserves useful evidence while forbidding physical use.

Conditional audit retention keeps the candidate in the audit inventory only if the retention contract remains attached.

The script rejects four bad summary moves:

```text
downgrade as useless failure;
conditional retention without contract;
obstruction decision as closure theorem;
summary as insertion.
```

## Boundary

No stress closure was derived. No insertion, active O, recombination, or parent closure was opened.

## Steering Consequence

The next script should be `candidate_group_63_status_summary.py`. It should preserve the status classification, not pretend to close the obstruction.
