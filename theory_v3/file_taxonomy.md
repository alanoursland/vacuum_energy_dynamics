# File Taxonomy

This document describes the prefix system used to organize the framework's content. Each file's prefix indicates what kind of claim the file makes and how it relates to the rest of the framework.

The taxonomy is the framework's way of keeping epistemic structure visible. A reader looking at any file can tell from the prefix what kind of claim it contains, what other content it depends on, and what would be required to revise it.

---

## Prefixes

**`sr_`** — **Special Relativity Imports**

Content adopted wholesale from special relativity. These are not framework commitments; they are background physics the framework inherits. Each SR import is labeled SR1, SR2, etc., and downstream content cites imports by label.

The framework does not attempt to rederive SR. SR imports are stable commitments that other documents depend on without justification beyond "this is established physics."

**`p#_`** — **Postulates**

Foundational commitments of the framework. Each postulate is numbered (P1, P2, P3, P3a, P4, P5, P6) in approximate dependency order — earlier postulates establish what later ones build on.

Postulates are the framework's "what if" content. They are not derived from anything more fundamental within the framework; they are the suppositions whose consequences the framework explores. If a postulate is wrong, the framework's claims downstream of that postulate need revision.

Variant labels (like P3a) indicate postulates that fit in the dependency structure between adjacent integer-numbered postulates without forcing a renumbering of everything.

**`t#_`** — **Theorems**

Specific quantitative results derived from the postulates and SR imports. Theorems are numbered in derivation-dependency order: T1 depends only on postulates and SR imports, T2 may also depend on T1, T3 may depend on T1 and T2, and so on.

Each theorem document contains the statement of the result and its proof. Lemmas used in the proof are normally embedded in the theorem document; they are factored into separate `l#_` documents only when reused across multiple theorems.

A theorem is the kind of claim the framework derives, not adopts. If a theorem is wrong, either the postulates are wrong or the proof is wrong.

**`c#_`** — **Consequences**

Qualitative implications of the postulates. Consequences trace what the postulates commit the framework to say about some phenomenon or domain, without producing a specific quantitative result.

The defining feature of a consequence (as opposed to a theorem) is that it is qualitative rather than quantitative, and structural rather than calculational. "Singular configurations are forbidden" or "gravity wells exist as constrained minima" are consequence-like; "the redshift formula is $\Delta E/E = -gh/c^2$" is theorem-like.

**`e#_`** — **Empirical Consequences**

Qualitative implications of the postulates plus specific observed facts about the universe. Empirical consequences depend on both framework content and empirical input.

The defining feature of an empirical consequence is that it adopts an observational fact (the universe expands, gravitational waves have been detected, dark energy density appears constant at large scales) and works out what the framework's postulates commit it to say about that fact. The framework's contribution is the interpretive content, not the prediction of the observation.

Each empirical consequence document explicitly lists its empirical inputs alongside its postulate and SR import dependencies. This makes the dependency structure transparent: the claim depends on the postulates, the SR imports, and the named observations.

If the postulates turn out to be wrong, an empirical consequence may need revision. If the empirical input turns out to be wrong (an observation reinterpreted, a different observation favored), the consequence may also need revision. The split between these two failure modes is part of why empirical consequences are categorized separately from pure consequences.

**`h#_`** — **Hypotheses**

Provisional commitments adopted to enable derivations the framework cannot yet do without them. A hypothesis is something the framework treats as if it were a postulate for the purpose of getting derivations through, while explicitly acknowledging that it has not been derived from the postulates and may be wrong.

Hypotheses are flagged so that downstream content depending on them inherits their provisional status. A theorem that depends on a hypothesis is conditional: it would be unconditional if the hypothesis were derived, but as long as the hypothesis remains adopted-but-not-derived, the theorem's status is conditional.

Hypotheses are candidates for being elevated to derived status (becoming theorems or being subsumed by new postulates) once the framework develops enough to derive them. Until then, they are honest about being load-bearing assumptions that the framework hasn't justified internally.

**`l#_`** — **Lemmas**

Intermediate results used in proving theorems. Lemmas are normally embedded in their parent theorem documents and only get their own `l#_` document when reused across multiple theorems.

A factored-out lemma is a real result with its own proof, not just a stepping stone. The reason to factor it is that the same intermediate result is needed in multiple places and putting it in one location makes the dependency structure clearer.

---

## Files Without Prefixes

Framework-level documents do not get prefixes. These include:

- `README.md` — entry point for the framework
- `overview.md` — high-level description of the framework's content
- `taxonomy.md` — this document
- summary or organizational documents that describe the framework's content rather than making claims within it

Working notes about the framework's development (research notes, candidate path analyses, informal explorations that aren't yet ready to be claims) live in a `process/` folder without prefixes. These are documents about the framework's development rather than the framework's content.

---

## Imports Section

Every content document includes an Imports section listing what the document depends on:

- Postulate dependencies (which P# documents the claim relies on)
- SR import dependencies (which SR# imports the claim invokes)
- Other framework documents (which T#, C#, E#, H#, or L# documents the claim builds on)
- Empirical inputs (only for `e#_` documents — observations the document depends on)

The Imports section makes the dependency structure of any claim visible at a glance. A reader can see what would need to be true for the claim to hold, and what would need to change if any dependency failed.

---

## Why the Taxonomy

The system has three purposes.

First, it keeps documents focused. A postulate document commits to one thing and stays out of derivation territory. A theorem document derives one result without smuggling in new commitments. A consequence document traces implications without claiming to derive specific numbers. Each kind of document does its specific job.

Second, it makes dependency structure auditable. When something goes wrong — a derivation fails, an empirical observation contradicts a prediction, a consequence turns out to be inconsistent with another claim — the prefix system plus the imports sections make it possible to trace which claims depend on which others and where the problem might live.

Third, it makes the framework's epistemic position honest. Some claims are foundational suppositions the framework is exploring (postulates). Some are rigorously derived from those suppositions (theorems). Some are interpretive commitments the framework makes about observed phenomena (empirical consequences). Some are provisional adoptions to keep derivations moving (hypotheses). These are different epistemic statuses and the taxonomy keeps them distinct.

A claim's prefix is the framework's first-line answer to the question: how do you know this?
