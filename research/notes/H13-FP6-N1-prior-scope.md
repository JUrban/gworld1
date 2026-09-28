# Further prior answers and scope checks

28 September 2026, approximately 15:23–15:39 UTC. No new candidate.

## H13: negative under the standard synchronous definition

The entire original hyperbolic-group page and exact H13 paragraph
were read, and the screenshot in `research/statement-audits/H13/`
was inspected. The question asks whether combable groups are automatic;
the original page supplies no definition of combability.

Bridson, *Combings of groups and the grammar of reparameterization*,
[Comment. Math. Helv. 78 (2003), 752–771](https://ems.press/content/serial-article-files/42987),
Corollary C and Corollary 4.2, already answers negatively. The examples
are synchronously combable with cubic Dehn function, whereas automatic
groups have a quadratic isoperimetric inequality. One explicit example,
printed on p.753, is

    <a1,b1,s,t1,a2,b2,t2 |
      t1*a1=t2*a2,
      [ai,s]=[ai,ti]=[bi,s]=[bi,ti]=1 (i=1,2)>.

Definition (1.1) is the synchronous fellow-traveller property.
Bridson explicitly distinguishes it from the stronger original
Epstein–Thurston definition. Thus the classification here means
the standard synchronous definition used in that paper, with that
terminology qualification visible. It is not based merely on examples
that admit asynchronous combings.

Read pp.752–755, Theorem 3.4 and its proof, and section 4. The cited
cubic-area lower bound from Bridson's earlier work has not been
independently re-proved. This is a prior-source scope audit, not a new
proof or independent validation of the published theorem.

Archived PDF SHA-256:
`4b5b27aaeaa8202ad695b780faafa78c81e5ec741d4767ea0bef553672b0793a`.

## FP6: all classical knot groups are virtually free-by-cyclic

The whole original finitely-presented-group page, exact FP6 paragraph
and screenshot were inspected. For the standard meaning of knot group,
let M be the compact exterior of a tame knot in S^3. M is compact,
orientable and irreducible, with nonempty torus boundary.

The prior virtual-fibering results cover all three geometric cases:

- Hyperbolic M: the results of Wise and Agol.
- Graph-manifold M, including Seifert exteriors: the boundary case
  of Wang–Yu, also a consequence of virtual specialness.
- Mixed M: Przytycki–Wise, Corollary 1.3 of
  [*Mixed 3-manifolds are virtually special*, JAMS 31 (2018), 319–347](https://www.math.mcgill.ca/pprzytyc/JAMS.pdf).

The archived author-hosted publication explicitly states the mixed
corollary on p.319 and explains the hyperbolic and graph-manifold
cases on p.320. The case distinctions and their hypotheses were also
checked in Aschenbrenner–Friedl–Wilton, *3-Manifold Groups* (2015),
sections 4.7 and 5.2(H.20), printed pp.74–75 and 88–89. The latter
records Wang–Yu's nonempty-boundary theorem and the fibration exact
sequence. The proofs of virtual specialness/fibering were not
independently audited here.

A finite cover M' fibers over S^1 with a compact connected surface
fiber Sigma. Since M' has nonempty boundary, Sigma has nonempty
boundary. Hence pi_1(Sigma) is a finitely generated free group, and

    1 -> pi_1(Sigma) -> pi_1(M') -> Z -> 1

splits. Therefore pi_1(M') is free-by-cyclic and has finite index in
the knot group. The unknot has group Z and fits with trivial free
kernel. Composite knot exteriors are still irreducible; no prime-knot
restriction has been inserted. This routine consequence is excluded
from discovery counts.

Archived PDF hashes:

- Przytycki–Wise: `b52a03c2015253e41fc19f46a96b7555f3c3e4e7f622290f636fecb767def5f0`.
- Aschenbrenner–Friedl–Wilton: `31551e1a7cb6ce01026ba33e56806bfecf2c3e4d3afbec4dbf6c6bf0b7ef28ae`.

An initial download URL misspelled Aschenbrenner and returned 404;
the corrected URL in the archived metadata succeeded.

## N1: higher ranks are already included in the site's update

Read the original nilpotent page and its N1 rendering, plus the full
N1 background at `sources/raw/Back2.html`, lines716–732. The latter
explicitly credits Papistas (2001) and Formanek (2002) with the full
classification of the pairs (rank,class) admitting nontrivial elements
fixed by every automorphism. It is not limited to Bludov's earlier
rank-two examples.

The [primary publisher abstract for Papistas](https://www.tandfonline.com/doi/abs/10.1081/AGB-100106781)
also explicitly announces a full answer, in a more general
polynilpotent setting. This abstract was read through the web tool;
a direct archiving request returned 403. No full Papistas/Formanek
proof was obtained in this pass and no unverified explicit formula
for the classification is supplied. The site's full-resolution scope
is corroborated; N1 stays outside the discovery queue.

## H4: a complexity lead with an unresolved logical step

Gardam–Kielak–Logan,
[*JSJ decompositions and polytopes for two-generator one-relator groups*, arXiv:2101.02193v3](https://arxiv.org/abs/2101.02193v3),
printed p.6, discusses the lack of recursive time bounds for the
known general hyperbolic preprocessing algorithms, including Dehn
presentations. Read its introduction and that discussion; the PDF
is archived as `literature/raw/H4-Gardam-Kielak-Logan-2101.02193.pdf`,
SHA-256 `128957caa12f2ac4f5273d3b3b54b0d2a3886f7c48eafd744b62f69b1dd81ca3`.

This observation is not being promoted to a proof that every
algorithm promised a hyperbolic input must have unbounded recursive
complexity. A recognition procedure, which halts exactly on
hyperbolic inputs, is a different specification from a promise
procedure allowed arbitrary behavior on nonhyperbolic inputs.
An impossibility argument for H4 needs to handle that distinction
and the required output representation/isomorphism data. No such
complete reduction was obtained. H4's status is unchanged.

Further passes over N4, S2–S8, GA1/GA3 and other free-group questions
did not produce a completed argument. In particular, a terminating
transfinite automorphism tower does not imply finitely many types in
the finite tower of N4; adjoining roots in an affine tree action does
not automatically supply GA1's free isometric action. No new claims
or counts follow from these searches.
