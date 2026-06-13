# 4. Workflow Component 1: Charters With Kill Conditions

Each investigation should begin with a charter. A charter states the question,
the allowed assumptions, the forbidden shortcuts, the expected artifacts, and
the possible verdict states.

A useful verdict vocabulary is:

| verdict | meaning |
|---|---|
| `PASS` | the candidate passed the declared gate |
| `KILLED` | the candidate contradicted a gate or failed a required bound |
| `UNDERDETERMINED` | the current evidence cannot decide |
| `NOT_READY` | prerequisites are missing |
| `HANDOFF_READY` | the result is ready for a later stage but not itself final |

The rule is simple: a candidate should not enter the archive unless there is a
condition that could kill it. This is the main defense against sycophantic
theory-building. A model can always produce a plausible continuation of an
idea. A gate asks what would make the continuation unacceptable.

Examples from the case study include:

- a dark-sector budget gate that killed depletion-history explanations when
  the available budget missed by orders of magnitude;
- a radiative coefficient gate where binary-pulsar-class energy loss could
  have killed the derived normalization;
- a higher-curvature health gate where TT ghost residues killed spin-2
  quadratic curvature terms;
- a scalaron/P7-prime gate where static hair killed the remaining `R^2`
  freedom;
- a boundary-admissibility gate where smoothing survived only if it respected
  static frame indifference.

The charter is written before the derivation so the verdict cannot be moved
after the result is emotionally inconvenient.
