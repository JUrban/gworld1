# F38(c): rigid/solid and quotient-map check

29 September 2026, approximately 22:25–22:29 UTC. This is another
targeted internal source check, not independent review or a new result.
It supplements the earlier [shortening recheck](F38-29sep-shortening-recheck.md).
The candidate and its manifest-bound proof are unchanged.

The concern was whether existence of a shortest embedding really supplies
the **unique maximal graded shortening quotient** required in Definition
10.2, rather than merely some abstractly isomorphic group. Read again
the archived source's Sections 9–10 through Lemma 10.4 and its local proof,
the canonical quotient/equivalence definitions in Section 5, and the
constant-sequence step in Proposition 5.6. Actually viewed the retained
images of printed pages 89 and 90. The publisher's
[bibliographic page](https://www.numdam.org/item/PMIHES_2001__93__31_0/)
was also reopened; no replacement PDF was downloaded.

For G=A*<z>, P=<u,z>, the proof has already shown relative free
indecomposability and identified Aut(G/P) with extensions of Aut(A/u).
When its graded JSJ is nontrivial, take any embedding of G into the
fixed target free group and minimize its length in the graded modular
orbit. A constant sequence of this minimizing embedding has the image
as its limit group, and its canonical map eta_0 from G is an isomorphism.
This uses the bounded constant-sequence convention explicitly present
in Proposition 5.6, not a claim that every divergent sequence of
embeddings has trivial limiting action kernel.

For any other graded shortening quotient with canonical epimorphism
eta:G→Q, the map eta composed with eta_0 inverse is an epimorphism from
the first quotient to Q and makes the canonical maps commute. Thus the
first quotient dominates every other quotient in the source's order.
Every maximal quotient must be equivalent to it. This gives the
maximality and uniqueness required for the solid case. If the graded
JSJ is trivial, Definition 10.2 instead puts G in the rigid case.
The source's free-group example immediately before that definition is
consistent with this use; no general claim that all limit groups are
rigid or solid is made.

The separate flexible-sequence argument retains its other hypotheses:
graded modular automorphisms fix P pointwise, the hypothetical failure
of the bound supplies the displayed 2^m inequality, and injectivity
excludes a nontrivial relative free-product quotient. An embedding into
a larger free product with an unused factor is not such a quotient.
The candidate's explicit displacement bound and limiting tripod deal
separately with nontriviality and the action kernel of its divergent
sequence. None of these checks is supplied by finite Whitehead examples.

No new gap was found in this precise quotient-map step. Lemma 10.4 and
its JSJ/shortening machinery remain imported; this check does not
independently re-prove them. The shared F34(a)/F38(a) polynomial argument
was also reread while preparing the review index: its output components
are tracked by separate designated letters, not by the total Parikh
vector of a concatenation. No change or new computational test resulted.
The twelve-candidate tally and novelty qualifications are unchanged.
