# F38(c): focused recheck of the shortening application

29 September 2026, approximately16:02--16:07UTC. Internal dependency
review while the N8 group audits run. No change to the candidate,
implementation or counts; no new external specialist validation.

Reread `problems/F38/bounded-proof.md` and its audit, then the archived
Sela2001 text around Definitions10.1--10.3 and Lemma10.4, the opening
limit construction in Section1, and the constant-sequence passage in
Proposition5.6. Actually viewed the saved image of printed page90.
This is a targeted recheck, not a new full-paper or JSJ-machinery audit.

The main concern tested was whether the proposed shortest embedding
minimizes over the correct equivalence class. Definition10.1 defines
the graded class by precomposition with graded modular automorphisms;
its generators fix the parameter vertex pointwise. It does not silently
add arbitrary target conjugations to that graded equivalence relation.
Thus minimizing over the full pointwise fixer of P=<u,z> supplies the
shortness used in this particular graded argument. The initial target
conjugation that cyclically reduces f(u) is a separate step.

Section1 uses a minimum-displacement basepoint for unrestricted limits.
The candidate instead proves a uniform lower bound on displacement at
every point and supplies a nondegenerate limiting tripod at its chosen
basepoint. Hence it does not merely assume that a sequence of injections
has a faithful nontrivial limiting action. The axes argument behind the
bound works because the f(u) axis lies in the original free factor and
the z axis meets it precisely at the identity. At least one of those
axes has distance d(x,1) from any chosen point x.

The constant-short-embedding argument is consistent with the source's
constant-sequence convention: Proposition5.6 explicitly uses such a
sequence to obtain the image as a shortening quotient. The source's
free-group graded example and Definition10.2 were rechecked as well.
The finite parameter-image length condition in Definition10.3(ii) is
the exponential2^m inequality, confirmed in the actual page90 image.

The free-factor intersection step was also checked: Kurosh makes the
intersection of two free factors a free factor of each. Since u fills
A, a free factor containing P must contain A and z. The same reasoning
forces a pointwise P-fixer to preserve A. This excludes the relative
free-product quotient factorization required by the flexible-sequence
definition when the homomorphism is injective.

No new gap was found in these specific reductions. The applicability
of Sela's graded JSJ/shortening theorem and the other imported structural
results still needs independent specialist review. No software or
mathematical statement changed, so the already passed finite suites
were not rerun. Novelty remains unverified.
