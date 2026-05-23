# candidate_burden_ledger_role_problem — Analysis Note

## Result

`candidate_burden_ledger_role_problem.py` opens Group 98 as a physical-role audit for the determinant/Schur hierarchy.

It imports the Group 97 state correctly:

```text
difference numerator positivity target identified;
all-order difference numerator theorem open;
all-order parity gap / ratio-bound / Schur positivity / determinant nonzero remain open.
```

It asks the correct bridge question:

```text
Is the hierarchy configuration energy, exchange compensation, interface smoothing, total burden, or auxiliary admissibility?
```

The governance section correctly blocks overreach:

```text
hierarchy as J_curv by name:
  rejected because J_curv is not covariantly defined;

hierarchy as H_exch by name:
  rejected because H_exch is not insertable or independently defined;

hierarchy as total burden by name:
  rejected because total burden functional has not been defined;

parent equation jump:
  rejected because a role audit cannot write a parent equation.
```

## Interpretation

This is the right opening for Group 98.

After Groups 91–97, the hierarchy branch had become mathematically rich enough that it was tempting to treat it as physically identified. Group 98 puts the brakes on that.

The key distinction is:

```text
mathematical admissibility target
  !=
physical burden ledger
```

The hierarchy may still be important, but this script correctly refuses to call it `J_curv`, `H_exch`, interface energy, or total burden without a source/functional derivation.

## What Changed

The branch stops pretending that mathematical progress automatically implies physical assignment.

The hierarchy is now explicitly under audit.

## What Did Not Change

The numerator theorem remains open.

The physical burden functional remains undefined.

The parent equation remains unavailable.

## Carry-forward status

```text
HIERARCHY_ROLE_AUDIT_OPENED
PHYSICAL_LEDGER_ASSIGNMENT_QUESTION_OPENED
HIERARCHY_AS_J_CURV_NOT_LICENSED
HIERARCHY_AS_H_EXCH_NOT_LICENSED
HIERARCHY_AS_TOTAL_BURDEN_NOT_LICENSED
PARENT_EQUATION_JUMP_BLOCKED
```
