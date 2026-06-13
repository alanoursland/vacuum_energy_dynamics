# Paper 4 Outline: Adversarial AI-Assisted Theory Development

## Working Title

**Gates, Kill Conditions, and Machine-Verified Derivation Chains: A
Working Methodology for AI-Assisted Theoretical Physics**

Shorter title option:

**Adversarial Workflows for AI-Assisted Theoretical Physics**

## Target Venues

Primary:

- arXiv physics.hist-ph, physics.soc-ph, or physics.comp-ph.
- AI-for-science workshops where methodology case studies are accepted.

Possible journal target:

- Royal Society Open Science perspective or methodology article, if the
  archive is public and the narrative is polished.

## Central Claim

The useful part of AI-assisted theory development is not the model's
fluency. It is the workflow discipline around the model: predeclared kill
conditions, machine-verified derivation chains, adoption records with
fences, provenance-graded data, and honest downgrade records. A completed
case study in vacuum-substance gravity shows that this discipline can
prevent sycophantic theory-building and can make AI-assisted derivations
auditable.

## Intended Reader

- Researchers using LLMs in theoretical science.
- AI-for-science methodology researchers.
- Science-studies readers interested in verification and provenance.
- Physicists skeptical of AI-generated derivations.

The paper should stand even if the reader rejects the underlying physics.

## Abstract Skeleton

Large language models are increasingly used in theoretical research, but
their tendency toward fluent rationalization makes methodology more
important than raw capability. We describe an adversarial workflow for
AI-assisted theoretical physics and report a completed case study. The
workflow requires charters with kill conditions before derivations begin,
machine-verified scripts that rederive theorem claims from scratch,
explicit human adoption records for new postulates, provenance grades for
data, and public supersession records when estimates are downgraded. In
the case study, a vacuum-substance gravity program killed multiple
candidate mechanisms proposed by the theory owner and closed on general
relativity's gravitational sector rather than on the owner's preferred
deviations. We analyze the workflow's components, failure modes, and limits,
including an incident where an AI formalized and killed a mechanism the
owner did not actually hold. The result is a practical methodology for
using AI systems as adversarial derivation assistants rather than as
persuasive coauthors.

## Section Plan

### 1. Introduction

Problem:

- LLMs can generate plausible derivations.
- Plausibility is dangerous in theory work.
- Verification must be designed into the workflow.

Contribution:

- a concrete workflow;
- a completed case study;
- artifacts including killed hypotheses and downgrade records;
- lessons for AI-assisted science.

### 2. Background and Related Work

Topics:

- AI for science and mathematical reasoning.
- Formal verification / interactive theorem proving.
- Computer algebra in theoretical physics.
- Reproducible computational science.
- Human-in-the-loop scientific discovery.

Positioning:

- This is not Lean-level formal proof.
- It is CAS-verified physics derivation with explicit provenance.
- The contribution is workflow, not a claim that LLMs are reliable on
  their own.

### 3. The Case Study

Describe the vacuum-substance gravity program only as much as necessary.

Include:

- starting goal: investigate non-GR vacuum-energy dynamics;
- final gravitational-sector result: GR recovered, deviations killed;
- number of forge groups / lab reports / adoption records;
- examples of candidate mechanisms killed.

Important:

- This section must be understandable without buying the theory.
- The methodology paper is about process quality.

### 4. Workflow Component 1: Charters With Kill Conditions

Content:

- Each investigation begins with a question, allowed assumptions, and
  explicit verdict states.
- Verdict vocabulary:
  - PASS,
  - KILLED,
  - UNDERDETERMINED,
  - NOT_READY,
  - HANDOFF_READY.
- A candidate should not enter the archive unless there is a condition
  that could kill it.

Example:

- scalaron/four-derivative sector;
- boundary smoothing;
- dark matter depletion budget;
- radiative coefficient.

Figure:

- gate lifecycle: charter -> derivation -> verdict -> handoff or kill.

### 5. Workflow Component 2: Machine-Verified Derivation Chains

Content:

- Theorem claims live in scripts.
- Scripts rederive claims from scratch on each run.
- Scripts declare dependencies on upstream archived results.
- Dependency checks prevent silent mutation of earlier conclusions.

Discuss:

- what CAS verification can and cannot prove;
- symbolic witnesses vs general proofs;
- why script execution is a reproducibility floor, not epistemic finality.

Table:

- theorem;
- script;
- dependencies;
- verdict.

### 6. Workflow Component 3: Adoption Records and Fences

Content:

- Some theory moves are not derived; they are adopted.
- Adoption must be explicit, timestamped, human-owned, and fenced.
- Example: P9 and P7-prime adoption before their strongest consequences.

Key norm:

Do not call a postulate a theorem. Do not hide an adoption inside a proof.

### 7. Workflow Component 4: Honest Downgrades and Supersession

Content:

- Estimates later replaced by derivations must be downgraded in place.
- Supersession banners preserve the record.
- Failed predictions are evidence of process quality if handled honestly.

Examples:

- linear kappa-leak estimate superseded by second-order matter-era result;
- earlier speculative mechanisms killed rather than patched.

### 8. Workflow Component 5: Data Provenance Grades

Content:

- Data used in confrontations must carry provenance labels.
- Proposed grades:
  - FROM_MEMORY forbidden for confrontations;
  - TEXT_STATED;
  - VERIFIED_FROM_ABSTRACT;
  - VECTOR_EXTRACTED;
  - AUTHOR_PROVIDED.
- Anchor validation for extracted curves.

Bridge to Paper 3:

- vector extraction method as one data-gate tool.

### 9. Failure Case: Artifact vs Intuition

Content:

- The TVN incident: AI formalized and killed a mechanism the owner did not
  actually hold.
- What failed:
  - insufficient articulation of the owner's actual intuition;
  - formal artifact became a target too early.
- Corrective protocol:
  - separate intuition capture from formal candidate;
  - require owner confirmation before gate construction;
  - mark artifacts as probes until adopted.

Purpose:

- Show unflattering parts. This is what makes the methodology credible.

### 10. Outcomes of the Case Study

Content:

- mechanisms killed;
- postulates adopted with fences;
- final field-equation closure;
- surviving open obligations;
- no accessible gravitational deviations currently predicted.

Important framing:

The strongest evidence for workflow discipline is that it did not preserve
the owner's exciting deviations. It killed them.

### 11. Limits of the Method

Content:

- CAS verification is not formal proof.
- LLMs can still bias framing and candidate selection.
- Human owner can still choose bad postulates.
- Archive discipline costs time.
- Public artifacts create anonymity and reputational complications.

### 12. Recommendations

Practical checklist:

- require charters;
- predeclare kill conditions;
- separate postulates from theorems;
- write scripts for algebraic claims;
- keep dependency ledgers;
- use data provenance grades;
- record downgrades;
- publish killed candidates.

### 13. Conclusion

Close on:

AI-assisted theory work can be useful if the AI is placed inside an
adversarial verification workflow. Without such a workflow, fluency is a
risk. With it, the model becomes a generator of candidates, derivations,
and attacks whose outputs remain accountable to explicit gates.

## Figures and Tables

- Figure 1: adversarial theory-development loop.
- Figure 2: archive dependency graph.
- Figure 3: adoption/theorem/failure-state separation.
- Table 1: workflow components and artifacts.
- Table 2: killed mechanisms and kill conditions.
- Table 3: data provenance grades.
- Table 4: failure modes and mitigations.

## Appendices

- Appendix A: sample charter template.
- Appendix B: sample adoption record template.
- Appendix C: sample lab-report structure.
- Appendix D: data provenance checklist.
- Appendix E: public archive map.

## Claims To Avoid

- Do not claim AI produced trustworthy theory by itself.
- Do not claim CAS scripts are equivalent to formal proof.
- Do not make the paper depend on readers accepting VED.
- Do not hide the human owner's role in postulate adoption.

## Claims To Emphasize

- Discipline, not intelligence, is the core contribution.
- Killed ideas are positive evidence.
- Adoption boundaries matter.
- Machine-checkable provenance changes the character of AI-assisted work.

## Assumed Missing Pieces By Writing Time

1. Decision on repo publication and anonymization.
2. Clean archive map.
3. Final count of forge groups, lab reports, and killed candidates.
4. Related-work pass on AI-for-science verification workflows.
5. Venue-specific AI disclosure language.
6. Permission/comfort decision around showing the TVN incident.
