# candidate_sieve_reconcile — Result Note

## Result

The reconciliation confirms that Group 60 narrowed the Group 59 survivor through stricter exclusion without upgrading it.

The stable result is:

```text
raw residue and counterterm repair rejected;
eta derivative burden found;
eta^2 has stronger endpoint silence;
eta^2 rejected as scalar response;
constant admixture rejected;
source repair/carrying rejected;
trace double-count rejected;
radial-only stress rejected;
closure-supported stress survives with energy burden;
stress-only localized weighted-neutral-generated closure-supported response survives narrowly.
```

Physical use remains blocked.

## Main Findings

The reconciliation preserves the correct non-result:

```text
no insertion;
no active O;
no recombination;
no parent closure;
no covariant theorem;
no source theorem.
```

It also correctly warns against overclaiming the sieve:

```text
only reduced families were tested.
```

So the result is not “all possible candidates except this one are dead.” It is narrower:

```text
within the tested reduced families, the survivor has been sharply narrowed.
```

## Boundary

The survivor is still only an audit candidate.

## Steering Consequence

The next script should be `candidate_group_60_status_summary.py`. The summary should preserve both the kill-list and the narrowed survivor.
