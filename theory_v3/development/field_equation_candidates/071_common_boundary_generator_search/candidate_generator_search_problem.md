# candidate_generator_search_problem — Result Note

## Result

`candidate_generator_search_problem.py` correctly opens Group 71 as a common boundary generator search.

The script imports the Group 70 compatibility package:

```text
sigma = 1
a_jump = a_layer = a_tail = -1
L_bulk = 0
L_gauge = 0
```

and states the correct Group 71 target:

```text
Separate derived common-generator anti-match from selected cancellation / repair paint.
```

## Analysis

This opener is conceptually sound. It does not try to re-prove Group 70, and it does not promote the compatibility package into a theorem. It frames the problem as a generator-origin search: the missing object is not the algebraic anti-match itself, but the geometric reason the anti-match should hold.

The counterexamples are the right ones for the start of the group:

```text
B-with-hat;
chosen signs;
diagnostic layer;
active O escape.
```

These preserve the key Group 71 wall rule:

```text
If the generator is only B with a hat, it is not a generator.
```

## Boundary

The script proves no matching theorem, no parent divergence identity, no recombination rule, and no parent equation. It only opens the search and records the immediate obligations.

## Unexpected Results

None. This output matches the plan.

## Steering Consequence

Proceed to `candidate_boundary_generator_requirements.py`. The opener has done enough; no additional opener script is needed.
