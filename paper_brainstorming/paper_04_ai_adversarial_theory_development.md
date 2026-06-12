# Paper 4: Adversarial Theory Development with AI

**Working title:** *Gates, Kill Conditions, and Machine-Verified
Derivation Chains: A Working Methodology for AI-Assisted Theoretical
Physics*

**Venue:** arXiv (physics.hist-ph or physics.soc-ph); AI4Science
workshops (NeurIPS/ICML satellite venues take methodology papers with
case studies); possibly a perspective piece in a venue like Royal
Society Open Science. This paper is about *how*, not *what* — it stands
even for readers who reject the physics.

**Audience:** researchers using LLMs for theory work; the growing
AI-for-science methodology community; science-studies people interested
in what verification means when an AI does the deriving.

## The claim

A solo researcher plus AI assistants ran a multi-month theory program
under an explicit adversarial discipline, and the discipline — not the
intelligence — is what made the output trustworthy. The case study: a
vacuum-substance gravity program that ended by deriving GR, killing six
of the owner's own proposed mechanisms on the way. The methodology
components, each with concrete artifacts:

1. **Charters with kill conditions** before any derivation begins
   (verdict vocabulary: PASS / KILLED / UNDERDETERMINED; no candidate
   enters without a gate that can kill it).
2. **Machine-verified derivation chains**: every theorem lives in a
   script that re-derives it from scratch on each run, with declared
   dependencies on upstream results (the "forge archive" pattern) — the
   AI cannot silently change a result without breaking the chain.
3. **Adoption records with fences**: new postulates are adopted by the
   human owner, timestamped, with explicit scope fences; the record
   shows P9/P7′ adopted *before* their decisive consequences were found.
4. **Honest-downgrade norms**: two advertised predictions were revised
   downward when derivations replaced estimates, recorded in place with
   supersession banners rather than edits.
5. **Artifact-vs-intuition separation**: a documented failure case (the
   TVN incident: the AI formalized and then killed a mechanism the
   owner never actually held) and the corrective protocol it produced.
6. **Data-gate provenance grades** (VERIFIED_FROM_ABSTRACT /
   VECTOR_EXTRACTED / FROM_MEMORY-forbidden-in-confrontations).

## Why this is publishable now

AI-assisted derivation is exploding; trustworthy-workflow literature is
thin and mostly speculative. This is a *completed* case study with a
public, machine-checkable archive — including the unflattering parts
(the kill ledger, the wrong estimates, the misattributed mechanism).
The honest selling point: the program's most cited-worthy result
(deriving GR) is exactly the outcome a sycophantic workflow would never
produce, since it required killing every exciting deviation the owner
hoped for.

## What exists vs. what's missing

- EXISTS: the entire archive (13 forge groups, 10 lab reports, closing
  report, adoption records, the TVN incident documentation).
- MISSING: the paper itself; anonymization/repo-publication decisions;
  a related-work pass on AI-for-math verification workflows (Lean/ITP
  community norms are the obvious comparison: this is "CAS-verified
  physics" rather than "ITP-verified math" — position honestly below
  that bar).

## Risks

- Methodology papers from outside academia get less traction; the
  artifact trail is the differentiator. Workshop venues are the
  low-friction entry.
- Dual-anonymity issues if submitted anywhere peer-reviewed while the
  repo is public; decide repo publication timing jointly with paper 1.

**Effort estimate:** 2–3 sessions; mostly curation and narrative. Pairs
naturally with making the repo public + Zenodo DOI.
