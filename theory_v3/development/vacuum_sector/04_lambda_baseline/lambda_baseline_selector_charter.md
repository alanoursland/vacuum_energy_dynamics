# Lambda Baseline Selector Charter

This charter records candidate ways a vacuum-sector branch might select the
`Lambda` baseline. It is not a theory file and does not adopt any selector.

The current split is:

```text
Lambda = 0:
  asymptotically flat scalar boundary-flux sector when no nonzero background
  curvature is supplied.

Lambda free:
  allowed but unvalued Lovelock/background constant.

Lambda nonzero derived:
  selector required before the value, sign, or floor is claimed.
```

## Required Fields

Every selector candidate must state:

```text
boundary data;
sign/value mechanism;
source ledger;
local-equation quarantine;
falsifier;
first concrete test.
```

No candidate may be used as live baseline physics until those fields are
available and passed through the selector sieve.

## Candidate Selector Rows

| selector | boundary data | sign/value mechanism | source ledger | local-equation quarantine | falsifier |
| --- | --- | --- | --- | --- | --- |
| variational minimum | admissible vacuum variations and endpoint data | stationary minimum or constrained extremum fixes sign and value | constant floor only; localized matter and dark excess remain separate | reduce locally to closed EH/Lovelock equation with constant `Lambda` | killed if it inserts the observed value by hand or destabilizes the flat/de Sitter branch |
| admissibility or boundary selector | explicit asymptotic, horizon, compactness, or domain boundary class | admissibility condition fixes allowed curvature floor | boundary-selected background, not local matter | boundary rule must not generate untracked local residuals | killed if value depends on localized source scale or double-counts a boundary term |
| topology or global constraint | global manifold class, compactness condition, or topological sector | integrated constraint fixes or discretizes curvature floor | global constraint ledger; no local stress tensor insertion | local equations remain EH/Lovelock except for the allowed constant | killed if an inert topological invariant is claimed to set local `Lambda` without a constraint equation |
| measure identity | measure normalization, state space, and covariance requirements | identity fixes constant density scale and sign before observation is used | measure floor only; transportable excess remains downstream | preserve diffeomorphism covariance and stress conservation | killed if it is only dimensional fitting or lacks a covariant conserved ledger |
| relaxation or nonlocal history | history domain, kernel support, initial data, and late-time admissibility class | relaxation fixed point or memory integral determines the constant floor | relaxed floor distinct from local matter and clustered excess | prove local conservation and avoid acausal closed-equation changes | killed if it violates causality, conservation, or closed local weak-field tests |
| frustration-floor microphysics | microstate class, coarse-graining rule, and vacuum reference ensemble | microphysical frustration or ground-state accounting fixes sign and value | floor only; clustered or transportable excess belongs to dark-sector bookkeeping | must not alter closed local metric response unless routed through residual gates | killed if it becomes dark matter by assertion or lacks abundance and conservation bookkeeping |

## Working Rule

A selector may open a mechanism only after it passes the first sieve:

```text
boundary data are explicit;
sign and value are determined before observational fitting;
source ledger separates floor, matter, and excess;
closed local metric equations remain quarantined;
falsifier is concrete enough to kill the branch.
```

## Non-Conclusions

This charter does not:

```text
derive a nonzero Lambda;
insert the observed Lambda value;
license a dark-sector excess;
modify the closed local gravitational equations;
select one candidate over another.
```
