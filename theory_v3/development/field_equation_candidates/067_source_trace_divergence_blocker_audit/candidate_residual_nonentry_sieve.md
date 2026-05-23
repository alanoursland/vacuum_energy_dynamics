# candidate_residual_nonentry_sieve — Result Note

## Result

The script audits residual trace-incidence states.

The only role-safe trace state is:

```text
i_B = 1
i_res = 0
i_trace_extra = 0
```

Residual-entry states are rejected:

```text
(0,1,0)
(0,1,1)
(1,1,0)
(1,1,1)
```

## Main Findings

Residual channels cannot enter the parent as trace or source carriers.

The result clarifies:

```text
residuals may remain diagnostic;
residuals may remain rejected-route records;
residuals may not become parent carriers.
```

Rejected residual routes:

```text
residual as trace carrier;
residual as source repair;
residual as parent clue-term.
```

This closes a common leak path. Residuals have repeatedly appeared as useful signs of obstruction, but useful obstruction evidence is not a parent term.

## Boundary

Residual nonentry is necessary, not sufficient. It blocks residual carrier routes but does not prove source safety, trace safety, or divergence identity.

## Steering Consequence

Proceed to divergence obstruction. The next question is whether strict count-once and residual nonentry are enough for conservation. Expected answer: no.
