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
| GA5(b) | [Bartholdi–Sidki, arXiv:1805.04732](https://arxiv.org/abs/1805.04732), Theorem 1.2; published GGD 14 (2020), 107–115 | Exact positive answer: a self-similar action of the countably infinite-rank free abelian group on the binary tree. Full proof and original statement inspected on 28 September 2026. Replaces the earlier degree/transitivity caveat based on Dantas–Santos–Sidki 2023. |

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

## Free-group portfolio refresh, 28 September 2026 approximately 11:41–11:44 UTC

- F35: [Coulon–Fournier-Facio, arXiv:2312.11684v4](https://arxiv.org/abs/2312.11684v4), Theorem 1.1, supplies continuum many infinite simple characteristic quotients of every nonabelian finite-rank free group. First submitted in 2023; the archived September 2026 version is marked accepted. This directly answers the entry and is excluded from new-result counts.
- F34(a), F38(c), F1(b): [Lee, arXiv:0802.0584](https://arxiv.org/abs/0802.0584) explicitly answers these three algorithmic problems in rank two. Archived full text; the abstract identifies the GroupWorld labels. Higher ranks remain separate scopes.
- [Shpilrain, Automorphic orbits in free groups: recent progress](https://arxiv.org/abs/2510.00889), archived, Section 4, records further rank-two potential-positivity algorithms. Section 3 retains the general complexity question. Do not infer a higher-rank solution from a rank-two result or use extracted polynomial exponents without inspecting typography.
- F37: derived the rank-two reduction to equations via the Nielsen basis criterion: u is primitive iff some v,t satisfy [u,v]=t^-1[a,b]^(+/-1)t. Products of k such elements therefore give a finite disjunction of finite systems, decidable by Makanin; searching k<=word length computes primitive length. The underlying definability is explicitly recorded in [Kharlampovich–Myasnikov, ICM2014, Example 2.4](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM2014.2/ICM2014.2.pdf). Treat this as a routine consequence of prior results, not a new candidate. It does not extend to higher rank by the same formula.

## N8 arbitrary-class target strata, 28 September 2026 approximately 11:50–12:12 UTC

Queries included “commutator free nilpotent independent automorphisms”, “IA free nilpotent orbit problem”, “commutator free nilpotent central algorithm”, and “free Lie single commutator algorithm”. No matching theorem for the two target strata was located in these searches. This is not an exhaustive novelty audit.

- [Tolstykh, arXiv:0807.4341](https://arxiv.org/abs/0807.4341), Proposition 1.1: standard IA correction properties, stated in the infinite-rank setting. The finite-rank proof needed here is included in the candidate. Archived PDF and extracted text. General arithmetic/automorphism-orbit algorithms are also prior work; the candidate is the reduction of this commutator stratum to finitely many explicit nilpotent orbits, with a self-contained orbit procedure.
- [Blessenohl–Laue, *Algebraic combinatorics related to the free Lie algebra*](https://www.mat.univie.ac.at/~slc/opapers/s29laue.pdf), pp.3–5 and formula (9): position-permutation convention, Klyachko's Lie idempotent, and its increasing-order product factorization. Archived PDF/text; visually inspected printed p.5. Their reference [16] identifies Klyachko, Siberian Math. J. 15 (1974), 914–920. The proper-rotation vanishing lemma in the new proof is deduced from this prior theorem; the idempotent and factorization are not claimed as discoveries of this experiment.
- Roman'kov's prior class-two theorem and the general-equation undecidability results remain distinct from the present target-restricted, higher-class claims. An indexed secondary copy was not substituted for a primary full-text audit of Roman'kov 2016.

## N5 torsion-case route, 28 September 2026 approximately 12:16–12:41 UTC

Repeated targeted queries included “nilpotent groups torsion direct decomposition algorithm”, “nilpotent groups decomposability”, “nilpotent direct decomposition congruence”, and “nilpotent groups torsion decomposable algorithm”. The principal matching theorem remains the torsion-free result; no full torsion-case theorem was located. Absence from these searches does not prove novelty.

- [Baumslag–Miller–Ostheimer, arXiv:1510.05632](https://arxiv.org/abs/1510.05632), archived earlier: the introduction explicitly leaves torsion open. The new argument uses the rational decomposition framework, then a finite-kernel bound modulo the actual centre and a separate central-extension lifting procedure. A literal arbitrary-lift assertion in Lemma 24 fails the explicit example in `problems/N5/audit.md`; printed p.13 was inspected visually. This concern is kept separate from the paper's main theorem and from the structural ingredients used here.
- [Fisher–Gray–Hydon, arXiv:1303.3376](https://arxiv.org/abs/1303.3376), now archived and read, Section 3, Lemma 3.2 and Theorem 3.3: matched indecomposable summands differ only by central components. The proof uses linear algebra and applies over Q. This directly supports the finite partition reduction in the N5 candidate and does not depend on the later lifting criterion in the BMO paper. The rational decomposition algorithm is standard; BMO points to de Graaf, Section 1.15.
- The archived [Roman'kov 2021 survey](https://www.mathnet.ru/php/getFT.phtml?jrnid=pdm&paperid=736&what=fullt) also lists the torsion-free decomposability result, and records the standard effective subgroup/presentation operations used in the proof. It is not used to assert current openness.

## M0 and GA5(b) follow-up, 28 September 2026 approximately 12:50–13:05 UTC

- [Bartholdi–Sidki, arXiv:1805.04732](https://arxiv.org/abs/1805.04732), Theorem 1.2 and Section 4, gives exactly the binary-tree action needed in GA5(b). The additive group Z[1/eta] intersect Z_2, with eta a transcendental 2-adic of valuation one, is free abelian of countable rank. Division by eta on its index-two subgroup has trivial invariant core. Archived and read the primary proof. Published version: GGD 14 (2020), 107–115. This is prior work, not a discovery.
- [Dantas–Santos–Sidki 2023](https://ems.press/content/serial-article-files/30214), introduction and Theorem C, credits the previous construction and develops intransitive variants. Archived as the reference trail, not as the direct binary-degree theorem.
- [Gupta–Gupta–Roman’kov 1992](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/3EC22EA15B41760ECEFAA91FE195F19D/S0008414X00010968a.pdf/primitivity_in_free_groups_and_free_metabelian_groups.pdf), Lemma 1, p.517, states Bachmuth’s square-Jacobian criterion. Archived; exact page inspected visually. The source uses right derivatives; the M0 candidate states its left-column convention and the conversion.
- [Timoshenko 2020](https://www.mathnet.ru/php/getFT.phtml?jrnid=smj&paperid=5992&what=fullt), p.419, explicitly records the known rank-two answer and the open higher-rank individual-element question. Archived Russian primary text, read the relevant sections, and inspected this page visually.
- [Timoshenko 2015](https://www.mathnet.ru/php/getFT.phtml?jrnid=al&paperid=707&what=fullt), Corollary 1, p.514, assumes preservation of primitive systems of length r-1. Archived and checked the exact hypothesis. Its abstract must not be read as settling the individual-element problem for higher rank.

The M0 finite-field orbit argument was derived before reading the full 2015/2020 papers; the initial search had already exposed the 2020 open-status statement. Queries included “primitive preserving metabelian”, “primitive endomorphisms Fox finite”, “metabelian primitivity finite fields”, and “14.85 metabelian”, with 2025/2026 follow-ups. No matching all-rank answer was located. Novelty remains provisional. The public Kourovka statement is bibliographic overlap only; no prior-run mathematical argument or code was imported.

Additional F28 searches used “Sidki invariant subgroup free”, “virtual endomorphism elliptic”, “strongly simple endomorphism” and “F28 Sidki solution”. They found further strongly-simple terminology and related self-similar work, but no matching full answer. This does not establish novelty.
