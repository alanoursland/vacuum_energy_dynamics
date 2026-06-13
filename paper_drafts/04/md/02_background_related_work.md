# 2. Background and Related Work

This paper sits between several literatures.

AI-for-science work studies how machine-learning systems can propose
hypotheses, accelerate search, and assist with scientific reasoning. Much of
that literature emphasizes capability. The concern here is different:
methodology for keeping an AI-assisted theory process adversarial and
auditable.

Interactive theorem proving provides a higher standard. Systems such as Lean,
Coq, Isabelle, and HOL Light can check formal proofs against small trusted
kernels. The workflow described here does not reach that bar. Its scripts are
computer-algebra and numerical verification artifacts, not formal proof terms.
They can check algebra, reproduce derivations, enforce dependency structure,
and expose contradictions, but they cannot by themselves prove all analytic
claims in full generality.

Computer algebra has long been part of theoretical physics. Symbolic tensor
calculation, perturbation algebra, residue checks, and variational derivations
are natural targets for executable verification. The novelty here is not the
existence of scripts. It is the archive discipline around them: charters before
derivations, declared dependencies, stable verdict states, and public records
of killed candidates.

Reproducible computational science contributes another norm: results should be
regenerable from code and data. In theory work, the relevant artifacts include
not only code and data, but also assumptions, postulate adoptions, failed
candidate paths, and downgrade records.

The closest methodological target is therefore not "AI proves physics." It is:
AI can be useful when embedded in a reproducibility and falsification workflow
that makes its outputs accountable.
