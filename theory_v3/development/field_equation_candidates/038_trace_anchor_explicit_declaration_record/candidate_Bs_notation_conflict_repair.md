# Candidate B_s Notation Conflict Repair

## Script result

`candidate_Bs_notation_conflict_repair.py` classified the repair routes for the current `B_s` notation conflict.

The conflict is real: prior collection found both metric-like and scale-like usage, so a single silent `B_s` convention cannot be installed safely.

## Main result

The safest repair candidate is a notation split.

```text
B_s_metric:
  metric-coefficient spatial response language;
  candidate normalization would use log(B_s_metric)=2*zeta/d.

b_s_scale:
  scale-factor / per-direction response language;
  candidate normalization would use log(b_s_scale)=zeta/d.

F_zeta:
  neutral response-functional placeholder;
  cannot hide or choose the factor-of-two convention.
```

The split is a repair route, not a declaration completion. It preserves both usages and prevents the same `B_s` symbol from carrying both metric-coefficient and scale-factor meanings.

## Accepted / deferred repair routes

`R1: notation split route` is the best repair candidate. It is allowed if metric-like and scale-like usages are assigned distinct names before any declaration is installed.

`R2: explicit theory-choice route` remains possible, but it must be recorded as a deliberate declaration choice rather than as an evidence-derived theorem.

`R3: neutral F_zeta route` remains a safe deferral route only if `F_zeta` does not install either `zeta/d` or `2*zeta/d` by implication.

`R4: source-priority route` remains possible as a later evidence-quality script, but it is not enough here to choose the convention.

## Rejected repair routes

The script rejected choosing the convention by silent majority of collector hits, because repeated snippets and recovery-facing contexts do not provide clean notation-origin evidence.

It also rejected immediate declaration despite conflict. A convention cannot be installed by ignoring the mixed usage.

## Forbidden shortcuts

The script rejected the following shortcuts:

```text
metric-like hits as decisive while ignoring scale-like/root hits;
scale-like/root hits as decisive while ignoring inherited metric usage;
F_zeta as a hidden convention repair;
hit count as theorem or declaration;
notation repair as B_s/F_zeta insertion readiness.
```

## Open obligations

The repair result leaves four obligations open:

```text
preserve conflict visibility;
repair by notation split or explicit theory choice;
block F_zeta from hiding the factor-of-two burden;
keep insertion, active O, residual control, and parent closure closed.
```

## Safe handoff

The next script should attempt a notation-split declaration surface.

It may introduce distinct names for metric-coefficient and scale-factor uses, but it must not select either as the active trace-anchor declaration. It also must not adopt Package B, prove trace normalization or safe membership, derive insertion, or open parent closure.
