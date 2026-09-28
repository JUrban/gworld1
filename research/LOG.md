# Research log

Preparation, 28 September 2026: sources downloaded and indexed; site status markers and Hall of Fame cross-referenced; one external bibliographic status correction recorded; shared GAP installation and infrastructure checked. No targets selected, no mathematical searches or proof attempts performed. The 48-hour clock remains unstarted.

After explicit launch, append UTC time, problem/subpart, action, evidence, result, and next step. Record failed approaches and uncertainty as well as successful ones.

## 2026-09-28 10:04–10:10 UTC — launch and initial portfolio

User explicitly launched the 48-hour experiment. Deadline 2026-09-30 10:04:49 UTC, 20 CPU cores / 100 GB RAM. Preparation revision e1dc7b2; initialized clock committed as 90a2de7. A literal apostrophe-escape typo in the recorded launch quotation was corrected without altering either timestamp.

Read the full extracted text of the 146 entries without heading stars; identified convention traps (e.g. trivial solutions to the literal E4 wording) to avoid counting as intended new answers. Began primary-literature checks for free-group and self-similarity questions. A September 2026 preprint explicitly claims F15; F30 has a recent positive result. These are not our solutions. An early self-similarity preprint and later publication appear to differ, so version-sensitive checks are needed.

Developed a tentative exact answer to F42 using the rank of a folded core graph and finite coverings with all fundamental loops of length n. Saved the first argument before proceeding to verification and novelty research. No claims counted.

## 2026-09-28 10:22 UTC — first status checkpoint

Inspected original HTML renderings for F11 and F42. Both early arguments match already published/preprinted results and are excluded from novelty counts. Updated working triage (frozen source catalogue untouched). Located prior work on F15, F30, F31, F40 and a B11 announcement. Installed isolated Python/browser dependencies and locally extracted eight Ubuntu browser libraries; no root access used. Corrected a literal escape in the launch text only, without changing start/deadline.

## 2026-09-28 10:35 UTC — N8(b) class-three candidate

Derived a finite decision procedure in all finite ranks. For nonzero degree-two image, enumerate finite-index lattices in the support plane and solve integer central correction systems; commutator-preserving Nielsen moves prove completeness. For zero degree-two image, normalize one factor into gamma_2 and reconstruct the unique possible rank-one tensor using exact rational formulas. Wrote a self-contained candidate proof and prototype.

The Python recorded run passed 173 checks (fixed seed 9282608). The initial GAP run returned shell status zero but no marker: nq had aborted on rank one. This is retained as a failed run. Handling rank one directly as the infinite cyclic group and using --quitonbreak gave a successful rerun with 165 independently evaluated witnesses. Both successful runs used one CPU slot and 4 GB address-space limits.

Targeted literature searches found the known class-two theorem (Roman’kov 2016), the distinct general-equation undecidability results, and useful 1998 negative examples, but no class-three single-commutator decision result yet. Candidate novelty remains provisional.

Download caveats: the GA5 thesis returned HTTP 503; no PDF archived. A Roman’kov publisher request returned HTTP 202 with zero bytes, now explicitly marked unusable in its metadata. The downloader was tightened to require nonempty HTTP 200 responses. The 2021 Roman’kov survey and 1998 Akhavan-Malayeri–Rhemtulla PDF were archived successfully.

## 2026-09-28 10:49 UTC — class-four extension checked

Extended the N8(b) procedure to class four by splitting according to the first nonzero Lie layer. Nonzero degree two has unique degree-two factor corrections, followed by linear degree-four corrections. Nonzero degree three has only finitely many scaling choices. Pure degree four reduces to either an exterior decomposition in L2 or at most two rational linear factors of a quadratic, followed by integer linear algebra. The key natural map on L4 has a six-by-six multilinear minor with determinant -54; polarization extends injectivity to every rank. Full candidate proof written.

The class-four prototype passed 108 checks, fixed seed 9282604 (178.67 s on one CPU slot, 4 GB limit); GAP independently evaluated all 100 positive witnesses in 2.48 s. No test failure occurred. Classes three and four are one partial candidate, with bibliographic novelty still provisional. Targeted class-four literature searches did not locate a matching decision theorem.

A separate bounded probe found outer-slot injectivity in rank two for degrees three through seven; this is only a finite calculation and establishes no general higher-degree theorem. The degree-two map is zero, as expected.

Completed the textual pass through all 49 heading-star entries as well. Neither a star nor its absence substitutes for an exact subpart/background audit.

## 2026-09-28 10:54 UTC — broader follow-up portfolio

Archived and checked primary statements for prior resolutions of A3 and A5 (the latter a September 2026 preprint claim). Marked both outside the new-result count. Recorded unproved routes/gaps for N5, N9(a), B9, F28 and higher-class N8 in research/notes/portfolio-followups.md. No additional candidate claimed. The generated problem READMEs retain the preparation snapshot; the main README now explicitly points to the live triage and dated claims.
