# Portfolio and F38 follow-up, 29 September 2026

This pass adds no mathematical candidate or solved subpart.

## Unresolved portfolio

- B11: reread the complete archived braid page and the exact background.
  The previously archived primary BYU seminar announcement by Mark
  Shoemaker (26 February 2025) explicitly claims torsion-freeness of the
  Burau image. New targeted searches for the author, torsion-freeness and
  rational-subspace construction located that announcement again, but
  no full proof. Keep the existing `prior_solution_announced` status;
  neither a new proof nor independent confirmation is recorded.
  https://math.byu.edu/events/algebraic-geometry-seminar-mark-shoemaker-colorado-state-university-2025-02-26
- B8 and B13: the existing full primary-source scope audits already
  give prior answers. They should not return to the unsolved queue.
  B9's bounded special-braid counts still lack a fixed-strand exhaustion
  argument. No further bounded enumeration was run.
- H15: new searches again find quasiconvex malnormal subgroups and
  infinitely generated nonquasiconvex malnormal subgroups, not an answer
  to the finitely generated malnormal question. No new full source was
  audited and no inference of a solution is made.
- AUX4: no proof of the required pq normal generators was obtained.
  Reducing one projection by Nielsen moves leaves a normal-generation
  issue in the other factor; it does not establish simultaneous Nielsen
  equivalence to the standard product generators.
- F39: the starred primitive-membership part(b) is already credited to
  Clifford–Goldstein in the frozen background. The existing example
  S=<a^2,b^2>, phi(a)=a^2, phi(b)=b^2 still blocks substituting arbitrary
  nonzero-determinant endomorphisms for automorphisms in part(a).
  No general orbit/subgroup intersection algorithm was obtained.

These are screening observations, not exhaustive current-status claims.

## Targeted internal F38(c) recheck

Reread `problems/F38/bounded-proof.md`, its audit, and the primary Sela
text from Definition9.1 through Lemma10.4 and its local proof. The
following possible objections do not expose a new gap in this reading:

- Definition10.1 uses precomposition by the graded modular group to
  define the graded modular class. It does not demand minimization
  under all target conjugations at that point. Thus minimization under
  the larger pointwise parameter fixer supplies the asserted shortness.
- The pointwise fixer preserves A because A and its image are free
  factors whose intersection contains the free-factor-filling word u.
  The free-factor intersection and equal-rank argument applies to these
  actual subgroups, not merely to their conjugacy classes.
- The source explicitly permits isomorphic graded shortening quotients
  in its free-group example. The existing proof explains its use of a
  constant shortest embedding and the maximality of the identity
  quotient; ordinary ungraded shortening is not substituted for this.
- The proof gives a uniform displacement lower bound and a nondegenerate
  limiting tripod. Injectivity alone would not identify the action
  kernel; the cited eventual tripod-kernel property remains necessary.

This remains an internal check of selected hypotheses, not a new proof
of the deep graded-shortening theorem or independent specialist review.
The archived PDF pages89–90 were viewed in the original audit; this pass
reread the extracted primary text and does not claim another image view.
No theorem, source, code or certificate was changed, and no additional
finite tests were justified by these checks. The full F38 candidate and
novelty claim remain provisional.
