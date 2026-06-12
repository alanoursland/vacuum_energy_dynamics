# TODO (Alan): Email Requests for Official alpha(lambda) Limit Tables

**Created:** 2026-06-12
**Why:** Two curves matter to the program. Lee 2020 is already extracted
from the arXiv PDF's vector paths (anchor-validated, 0.03%); an official
table would upgrade its provenance. Tan 2020 has NO arXiv preprint, so an
author table (or the published PDF) is the only route to its curve.
Neither request is urgent — Lee 2020 is the binding limit in the 38–55 um
window the program uses — but both are cheap emails.

---

## Request 1: Tan 2020 (HUST) — the one we actually need

**Paper:** W.-H. Tan et al., "Improvement for Testing the Gravitational
Inverse-Square Law at the Submillimeter Range," PRL 124, 051301 (2020).
https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.124.051301

**Who to email:** the corresponding authors are in the PRL paper footer
(typically Jun Luo and/or Cheng-Gang Shao, Center for Gravitational
Experiments, Huazhong University of Science and Technology, Wuhan).
Find the exact addresses on the paper's first page (institutional access
or the PubMed record), or via the group's recent arXiv postings (HUST
gravity papers list author emails on the title page).

**Draft (copy/paste/edit):**

> Subject: Data request: 95% CL Yukawa limit curve from PRL 124, 051301
>
> Dear Prof. [Shao/Luo],
>
> I am working on a phenomenological analysis of short-range
> gravitational-strength Yukawa interactions, and I am using the 95%
> confidence limits from your paper "Improvement for Testing the
> Gravitational Inverse-Square Law at the Submillimeter Range"
> (Phys. Rev. Lett. 124, 051301 (2020)).
>
> Would it be possible to obtain the 95% CL upper-limit curve
> |alpha|(lambda) from the exclusion plot as a numerical table (any
> format is fine — CSV, text, or the plotting file)? I want to evaluate
> crossings at coupling values other than |alpha| = 1, in particular
> alpha = 1/3, and I would prefer to use your numbers rather than
> digitize the published figure.
>
> I will of course cite the paper as the source of the data.
>
> Thank you and best regards,
> Alan Oursland

**When the data arrives:**
1. Drop the file into `src_exp/dataexp/.data/alpha_lambda/` (gitignored).
2. Validate: the curve must cross |alpha| = 1 at 48 um (the abstract
   anchor) within ~2%.
3. Tell Claude to wire it into `short_range_gravity.py` as a Dataset
   with that anchor as the integrity check, and to record the
   provenance upgrade (AUTHOR_PROVIDED_TABLE) in the next forge script.

---

## Request 2: Lee 2020 (Eot-Wash) — provenance upgrade, optional

**Paper:** J. G. Lee et al., "New Test of the Gravitational 1/r^2 Law at
Separations down to 52 um," PRL 124, 101101 (2020). arXiv:2002.11761.

**Who to email:** Eric Adelberger or the Eot-Wash group, University of
Washington. Contacts via https://www.npl.washington.edu/eotwash/ (People
page). You're local — this is also the lab-tour target.

**Draft (copy/paste/edit):**

> Subject: Data request: 95% CL Yukawa limit curve from PRL 124, 101101
>
> Dear Prof. Adelberger,
>
> I am using the 95% confidence Yukawa limits from "New Test of the
> Gravitational 1/r^2 Law at Separations down to 52 um" (PRL 124,
> 101101 (2020)) in a phenomenological analysis, and I would like to
> evaluate the limit curve at coupling values other than |alpha| = 1
> (specifically alpha = 1/3).
>
> Is the 95% CL |alpha|(lambda) curve from Fig. 5 available as a
> numerical table? I have extracted it from the vector paths of the
> arXiv figure (it reproduces the 38.6 um crossing quoted in the
> abstract to 0.03%), but I would prefer to cite your official numbers.
>
> I'm in Bellevue, so if a visit ever suits the group better than
> email, I'd welcome that too.
>
> Thank you and best regards,
> Alan Oursland

**When the data arrives:** same three steps as above; the validation
anchor is 38.6 um at |alpha| = 1, and the official table supersedes
`lee2020_alpha_lambda_95cl.csv` (record the swap, keep the extraction
tool as the reproducibility fallback).

---

## Status tracker

| request | sent | received | wired in |
|---|---|---|---|
| Tan 2020 (HUST) | [ ] | [ ] | [ ] |
| Lee 2020 (Eot-Wash) | [ ] | [ ] | [ ] |
