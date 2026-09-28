# Literature ledger

Checked during the active run, 28 September 2026. A primary source's announcement or theorem is evidence of prior work, not our independent certification of its proof. IDs refer to the frozen GroupWorld website, whose numbering may differ from later books.

| Entry | Primary source | What it says / remaining scope |
|---|---|---|
| F11 | [Snopce–Tanushevski–Zalesskii, 2019](https://arxiv.org/abs/1902.02378), archived PDF | Theorem A(ii) and Example 3.5 give negative answers; rank-two subgroup case is positive. Our cyclic retract example rediscovers this mechanism. |
| F15 | [Tursunbaev, September 2026](https://arxiv.org/abs/2609.06755), archived PDF | Announces that two subgroups of a free group with the same nontrivial derived subgroup coincide, yielding a positive answer. Proof not audited here. |
| F30 | [Jaikin-Zapirain, revised February 2026](https://andreijaikin.wordpress.com/wp-content/uploads/2026/02/compressed_implies_inert25.pdf), archived PDF | Compressed implies inert for finitely generated free groups. A later update about the equalizer conjecture must not be read as retracting this assertion. |
| F31 | [Lei–Zhang, April 2026](https://arxiv.org/abs/2604.24502), archived PDF | Equalizers of pairs of injections from rank n free groups can have rank at least 2n−2, contradicting the proposed bound for n≥3. |
| F40 | [Koch-Hyde–O'Connor–Olive–Shpilrain, 2025](https://arxiv.org/abs/2505.00477) | Orbit-blocking words for nontrivial free-group elements. Exact original subpart comparison still required. |
| F42 | [Koch-Hyde–Olive, September 2026](https://arxiv.org/abs/2609.00382), archived PDF; [GAGTA abstract](https://profbsteinberg-math.github.io/BSteinberg-math.github.io/abstracts.html), archived HTML | Theorem 1.9 gives the exact answer for spheres and balls: (2r−1)^m at n=2m, r(2r−1)^m at n=2m+1. Independently reached the same formula before reading this proof; no novelty claimed. |
| F34 | [Koch-Hyde–O'Connor–Olive, June 2026](https://arxiv.org/abs/2606.13933) | Potential positivity is still discussed beyond rank two. Its numbering is F33 in a newer book; match statements rather than numbers. |
| N5 | [Baumslag–Miller–Ostheimer](https://arxiv.org/abs/1510.05632) | Direct decomposability algorithm for finitely generated **torsion-free** nilpotent groups. General torsion case not established by this reference. |
| B11 | [Mark Shoemaker, BYU seminar, 26 February 2025](https://math.byu.edu/events/algebraic-geometry-seminar-mark-shoemaker-colorado-state-university-2025-02-26) | Announces a proof that the Burau image is torsion-free. Full proof and bibliographic details still sought. Avoid spending search time seeking a counterexample without following this up. |
| B12 | [Mangioni–Sisto](https://poisson.phc.dm.unipi.it/~mangioni/Articoli/Teichmullerisation_with_quote.pdf), Theorem B | Constructs non-elementary hyperbolic quotients of B4 that cannot receive a non-virtually-cyclic image of any specified higher braid group. This does **not** settle whether higher braid groups have other non-elementary hyperbolic quotients. |
| GA5(b) | [Dantas–Santos–Sidki, 2023](https://ems.press/content/serial-article-files/30215), Theorem C | Published constructions of countably infinite-rank free abelian self-similar groups. Check required degree/transitivity against original statement. Earlier preprint claims denying infinite rank must not override this later work. |

## Scope traps retained for follow-up

- N9(a): a class-two undecidability construction varies the ambient nilpotent group with the input. Check whether the requested algorithm is uniform or for a fixed group before calling it a full answer.
- N8(b): undecidability of arbitrary equations does not imply undecidability of a single commutator equation.
- N3: countable and periodic locally nilpotent groups have prior positive results; uncountable unrestricted scope may differ.
- N4: automorphism towers for free nilpotent groups do not settle arbitrary finitely generated torsion-free nilpotent groups.
- F20: a theorem using basic commutators of weights six **and seven** does not answer the question using weight six alone. Finite nilpotent quotients cannot distinguish the relevant normal closure from the lower central subgroup.
- F25: a polynomial bound under distinct letter-frequency assumptions is not the unrestricted bound.
- F41, B5 and E4 contain implicit nontriviality conventions; do not count vacuous literal counterexamples.

The archived `.json` files give retrieval times, URLs and SHA-256 hashes. Text extracts are finding aids, not authoritative mathematical typography.

## N8(b) class-three follow-up

Searched on 28 September 2026 for “commutator problem free nilpotent groups”, “single commutator class three”, “N8 class 3 nilpotent”, and variants with “decidable” and “algorithm”. No prior theorem matching the candidate's full class-three/all-finite-rank scope was located in this initial check; this is not proof of novelty.

- [Roman’kov 2016](https://doi.org/10.1515/jgth-2016-0504): publisher abstract and author-uploaded paper text identify the class-two free-group result and undecidability for particular nonfree class-two groups. Publisher archive attempt returned an empty HTTP 202 response; metadata marks it unusable.
- [Roman’kov, Algorithmic theory of solvable groups, 2021](https://www.mathnet.ru/php/getFT.phtml?jrnid=pdm&paperid=736&what=fullt): archived survey; source publication date is 2021 despite fresh search-engine crawl dates.
- [Truss 1995](https://doi.org/10.1112/blms/27.1.39): class-three undecidability concerns general equation/unification problems, not specifically [x,y]=g.
- [Akhavan-Malayeri–Rhemtulla 1998](https://doi.org/10.1017/S0017089500032407): archived primary paper supplies the rank-two negative example [a,b]^2 and discusses commutator width. It does not state the decision algorithm proposed here.

Class-four N8 follow-up: searched “commutator equation class four”, “commutator class 4 algorithm nilpotent”, “genus problem nilpotent”, and “commutator free nilpotent decidable”. No primary source matching the proposed class-four single-commutator algorithm was located. Results on general equations, profinite genus, and commutator width answer different questions.

B9 follow-up: Dehornoy's [The braid shelf](https://dehornoy.lmno.cnrs.fr/Surveys/Dja.pdf), Question 3.19, still discusses the special-braid strand/complexity question. Do not conflate its special braids with the differently defined family in *Unprovability results involving braids*. Extracted bounds such as “2n” require the original typography before use.

## Further algorithmic status corrections

- A3: [Rauzy, arXiv:2002.02541](https://arxiv.org/abs/2002.02541), Theorem 29, explicitly supplies the requested fixed finitely presented group, citing Bridson–Wilton's extraction from Slobodskoi. Archived the PDF and checked the theorem's exact quantifiers. This is a prior positive answer.
- A5: [Jayadevan, arXiv:2609.10281](https://arxiv.org/abs/2609.10281), Theorem 1.1, announces effective enumeration of ordinary finite presentations of metabelian groups. Archived the September 2026 preprint; neither its proof nor its reported Lean formalization has been audited here.
- MA7: the related question [Kourovka 16.23](https://alglog.org/21tkt.pdf) explicitly imposes n>2 and a nonscalar-modulo-proper-ideals condition. The short website version omits these; preserve the stronger intended scope rather than count the immediate n=2 example. This is a bibliographic comparison, not reuse of a Kourovka-run argument.

## F28: initial novelty comparison

The elliptic matrix construction in `research/notes/F28-matrix-lead.md` was derived before the targeted search below, at approximately 11:02 UTC on 28 September 2026. It uses no imported Kourovka argument.

Queries included “Sidki free group index two invariant subgroup”, “free group strongly simple virtual”, “F28 Sidki solution”, “virtual endomorphism elliptic free”, and “free group conjugation virtual endomorphism rotation”. No matching full negative answer was found in this initial search. This is provisional bibliographic evidence, not a guarantee of novelty.

- The original background points to [Nekrashevych–Sidki, *Automorphisms of the binary tree: state-closed subgroups and dynamics of 1/2-endomorphisms*](https://bremy.perso.math.cnrs.fr/BielefeldKM.pdf). Archived the containing volume/prepublication version (its pagination is 309ff, different from the final 2004 citation). The introduction and Section 3 concern simplicity, excluding normal invariant subgroups. The archived version does not provide the stronger F28 conclusion in the inspected portions.
- [Berlatto–Sidki, *Virtual endomorphisms of nilpotent groups*, GGD 1 (2007), 21–46](https://ems.press/content/serial-article-files/29462), p.22, defines strong simplicity by excluding all nontrivial invariant subgroups. Its examples and main results concern nilpotent groups, and its discussion of free groups concerns faithful self-similar representations. No assertion matching the present rank-two, degree-two, strongly simple example was located.
- [Kapovich, *Arithmetic aspects of self-similar groups*, GGD 6 (2012), 737–754](https://www.math.ucdavis.edu/~kapovich/EPR/com.pdf), Theorem 2 and Example 16, uses rational conjugation for arithmetic groups but excludes normal invariant subgroups. Its explicit PSL(2,Z) example uses diagonal conjugation and an index-three domain, with a nontrivial triangular invariant subgroup. The present construction instead uses elliptic conjugation, an index-two domain in F2, and excludes every invariant subgroup. This is related prior methodology, located after the derivation; it must be credited without identifying its weaker conclusion with F28.

## Additional status cautions, 28 September 2026

- F8 is already answered positively by [Antolín–Jaikin-Zapirain, *The Hanna Neumann conjecture for surface groups*](https://www.cambridge.org/core/journals/compositio-mathematica/article/hanna-neumann-conjecture-for-surface-groups/AABCA00E7D74BE96CB547BC4FF76D000), Corollary 1.5 (2022), which expressly covers fixed subgroups of arbitrary endomorphisms. No new answer is claimed.
- MA1: Knudson's [arXiv:0808.1239v1](https://arxiv.org/abs/0808.1239v1) announces a negative elementary-generation result, but the [v2 abstract](https://arxiv.org/abs/0808.1239v2) removes that claim and retains only the homology result. Do not retire MA1 using the indexed v1 theorem without reading the final version and resolving the change. Current status remains unverified.
- S3: the website already records the metabelian case and the general case under a no-proper-power hypothesis. An elementary metabelian argument would be a rediscovery; the remaining proper-power cases need separate work.

## N8(b) class-five follow-up, 28 September 2026

Queries included “commutator nilpotent class five decidable”, “commutator free nilpotent algorithm decidable”, and “commutator width Poroshenko algorithm Lie”. No matching class-five single-commutator decision theorem was located. This search does not establish novelty.

- [Roman’kov 2021 survey](https://www.mathnet.ru/php/getFT.phtml?jrnid=pdm&paperid=736&what=fullt), already archived, distinguishes the class-two free-group decision theorem from undecidability for nonfree groups and for general equations.
- [Duchin–Liang–Shapiro, Equations in nilpotent groups](https://arxiv.org/abs/1401.2471), author preprint abstract: single equations are decidable in class-two groups with rank-one commutator subgroup; systems are undecidable in nonabelian free nilpotent groups. Neither statement answers the present single-commutator question in higher free classes.
- [Poroshenko 2014](https://www.mathnet.ru/eng/al652), publisher abstract: an algorithm for the width of elements of a free metabelian Lie algebra over an algebraically closed field of characteristic zero. The coefficient domain and Lie/group setting differ from the integral free nilpotent problem here.
- [Roman’kov 2016, commutator width](https://www.mathnet.ru/eng/smj2789), publisher abstract: exact widths of several relatively free Lie algebras, Lie rings and groups. A global width formula alone does not decide whether a specified element is a single commutator. Full proof comparison remains outstanding; no exclusion based merely on a title is asserted.
