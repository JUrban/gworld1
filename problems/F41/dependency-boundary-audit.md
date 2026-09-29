# F41: what the additional model-theoretic source does and does not verify

29 September 2026, approximately 21:15--21:20 UTC. Internal source audit;
no new solution, external review, or novelty determination.

## Additional primary source

Chloe Perin, Anand Pillay, Rizos Sklinos and Katrin Tent, *On groups and
fields interpretable in torsion-free hyperbolic groups*,
[arXiv:1210.5757v2](https://arxiv.org/abs/1210.5757v2).
The archived PDF is `literature/raw/F41-PPST-1210.5757v2.pdf`, 200626
bytes, SHA-256
`ab7a1c594775c919ff96abb0b20a6e21cdebf89fad894b40c7ed6dc456225d5f`.
Retrieval metadata and extracted text accompany it. The attempted author
copy at `ivv5hpp.uni-muenster.de/u/tent/AbelInterGroups%28MJM%29.pdf`
failed certificate verification; the successful archive is the arXiv
version, not that copy or the journal edition.

Read the introduction, the free-group discussion at the start of Section
2, Theorem 3.3 and its proof, Corollary 3.4, Proposition 3.5 and its proof,
and the relevant references. Actually viewed printed page 7 in
`literature/figures/F41-PPST-page7.png`. The elimination-of-imaginaries
machinery used by this paper was not independently reproved.

## Scope of the independent argument

Theorem 3.3 supplies an independent proof that a proper definable subgroup
of a torsion-free hyperbolic group is cyclic. The introduction explicitly
distinguishes this from the earlier statement in Kharlampovich--Myasnikov.
It uses Sela's description of imaginaries as an imported result.

This does **not** independently establish KM Theorem 13, the dichotomy
for arbitrary definable subsets used by our F41 argument. A separating
set P = {x : not phi(x)} in that argument need not be a subgroup. Thus
the subgroup theorem cannot replace the multipattern theorem. Likewise,
negligibility from a single long piece would not replace the full piece
cover needed for the square-root exponent. These are distinct dependencies.

The additional source supports the connectedness and basis-genericity
background, but it supplies neither our quantitative piece-cover estimate
nor an independent proof of F41. It must not be reported as external
validation of the candidate.

## A shortcut that the source rules out

Proposition 3.5 says that for free rank at least three the automorphism
orbit of a nontrivial finite tuple is not definable, even with parameters.
This includes the nontrivial single-word orbits relevant to F41. The
identity is excluded: its singleton orbit is definable.

Consequently one cannot apply KM directly to the orbit by treating it
as a definable set. Our proof does not do that: it contains the orbit in
the complement of one parameter-free formula from the generic type.
Automorphism invariance gives containment, not equality. The distinction
is essential, rather than a dispensable technical formulation.

The source also recalls the exceptional definability of finite-tuple
orbits in rank two using parameters. This does not justify a parameterized
version of the separating-formula argument: a basis element generic over
the empty set need not be generic over those parameters. The negative
control in `followup-audit.md` still applies.

## Outcome

The searches for a correction to the cited multipattern theorem and a
matching orbit-growth result did not produce either in this bounded pass.
That is not a certification that no correction or prior solution exists.
The publisher DOI landing page could not be retrieved through the web
tool, so no comparison with the final publisher PDF is claimed.

No new defect was identified in the candidate's use of its stated
dependencies. The additional source sharpens the dependency boundary;
it does not remove it. The original finite counting checks were not rerun.
F41 remains one whole intended-scope candidate with specialist and
bibliographic review outstanding. The experiment tally remains ten
whole-entry candidates, two partial candidates, and zero established
novel results.
