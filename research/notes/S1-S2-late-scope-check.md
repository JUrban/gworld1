# S1/S2: two distinctions retained after a late source check

29 September 2026, approximately 23:44–23:47 UTC. No new candidate.
The frozen solvable-group statements and their complete linked background
paragraphs were reread. This pass did not make a new rendered-statement
inspection or a full literature survey.

For S1, the [publisher's background](https://shpilrain.ccny.cuny.edu/gworld/problems/Back2.html#(S1))
separates failure of generation by elementary Nielsen automorphisms,
failure of lifting to the next derived length, and finite generation of
the automorphism group. The first two do not by themselves settle the
third. The targeted current search did not supply a theorem resolving
finite generation in the remaining higher-derived-length scope. This is
not a claim that no such theorem exists.

For S2, put G=F/<<w>>. A presentation with this single relator in the
variety of derived length at most d presents G/G^(d). Thus the requested
word problem is membership in G^(d), not just the word problem in G.
For example, in G=<a,b | a^2>=C2*Z the reduced free-product commutator
[a,b] is nontrivial, but it dies in G/G'. An algorithm deciding whether
a word is trivial in G alone does not answer the quotient question.
The background's many-relator undecidability result also cannot simply
be substituted for the single-relator requirement.

A relevant recent primary source is Marco Linton,
[*Residually rationally solvable one-relator groups*, arXiv:2407.09272v2](https://arxiv.org/html/2407.09272v2),
19 September2025. Read the HTML introduction, Corollary4.4 and its proof,
and Section4.1; no claim of a visual PDF check or independent audit of the
whole main proof. Theorem1.1 identifies the intersection of the rational
derived series by one normal generator, and Corollary4.4 computes that
generator and decides residual rational solvability. Corollary4.7 transfers
the structural assertion to the ordinary derived series under H^2(G)=0;
Conjecture4.8 records the general ordinary-series assertion separately.
These are not stated as algorithms for membership in each finite ordinary
derived term. No such algorithm was extracted here.

There is a concrete reason not to silently replace ordinary with rational
derived quotients: in the same C2*Z example, a survives the ordinary
abelianization C2⊕Z, whereas it dies in rational abelianization. Any use
of the recent result for S2 needs an additional argument retaining the
requested integral information and the specified finite derived length.
This observation is an elementary scope control, not a new theorem count.

The primary HTML is archived as
`literature/raw/S2-Linton-2407.09272v2.html`, with retrieval metadata in the
adjacent JSON. SHA256:
`deecf1228557b35495db957b32d93572f8cd44cd436a7da44be642e3f5317ac7`.
No mathematical job, solver expansion, or external contact was initiated
for this source check. S1 and S2 remain unresolved in this experiment.
