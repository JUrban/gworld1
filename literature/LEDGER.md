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

## One-relator prior results, 28 September 2026 approximately 13:08–13:18 UTC

Exact scope audit and elementary consequence arguments are in `research/notes/OR-prior-resolutions.md`. Full original HTML and the complete rendered page were inspected, including the separately paragraphed OR7 subparts. Six entries are excluded from discovery counts.

- [Wang–Zhang, arXiv:2607.21493](https://arxiv.org/abs/2607.21493), submitted 23 July 2026, Theorem 1.3, Corollary 1.4, proofs in Sections 2–5: all three subparts of both OR7 and OR8 have negative answers. Primary PDF archived and proofs read. The authors credit ChatGPT assistance in their disclosure; these are their prior examples, not examples produced during this run.
- [Minasyan–Zalesskii, arXiv:1211.0488](https://arxiv.org/abs/1211.0488), Theorem 1.1: hereditary conjugacy separability answers OR11 positively. Archived and read. The introduction records Wise's residual-finiteness theorem (giving OR6 by an elementary case split), and Section 2 explains Newman's hyperbolicity theorem.
- [Dahmani–Guirardel, arXiv:1002.2590](https://arxiv.org/abs/1002.2590), Theorem 1: isomorphism of arbitrary hyperbolic groups is decidable, including torsion, hence OR2 has a prior positive answer. Archived primary statement checked.
- [Louder–Wilton, arXiv:2107.08911](https://arxiv.org/abs/2107.08911), Theorems 5.1 and 6.5(i), plus the Fischer–Karrass–Solitar ends theorem as used in Section 3 of [Logan's primary paper](https://eprints.gla.ac.uk/121498/19/121498.pdf), imply OR12. Both PDFs archived and relevant proofs read. The note gives the necessary finite-index transfer explicitly; no general commensurability invariance of co-Hopficity is assumed. This is a consequence of prior work, not a novelty claim.

The same scan found narrower metabelian results, not full answers to M1–M4: a 2026 Robinson isomorphism paper concerns a special polynomial-associated family, and Artamonov's 1975 nonfree projective examples concern a different metabelian variety. The latter title alone does not answer M4. Follow-up references for AUX3(b) (Myropolska, arXiv:1304.2668) and FP17 (Ould Houcine 2007) remain pending full scope checks.

## N8 penultimate-layer extension, 28 September 2026 approximately 13:21–13:30 UTC

Queries “commutator equation penultimate nilpotent”, “single commutator nilpotent central algorithm”, and “N8 commutator nilpotent” did not locate a matching theorem. The argument builds on the previously credited homogeneous factor method and adds complete integral scale/sublattice enumeration followed by one central integer lift. No additional theorem from the Kourovka run was imported. This limited search is not a novelty certification.

## Class six and further prior answers, 28 September 2026 approximately 13:36–13:45 UTC

N8 searches for “single commutator class six nilpotent”, “commutator free nilpotent decidable”, and “equation free nilpotent groups class 6” found no matching decision theorem. A survey snippet rendered an inequality sign as “6”; the archived primary text, not that extraction, remains the scope evidence. The new class-six proof includes its degree-five bracket and module-kernel lemmas explicitly; no additional external theorem was silently imported.

- [Myropolska, arXiv:1304.2668](https://arxiv.org/abs/1304.2668), Theorem 1.3 and the following Grigorchuk corollary, answer AUX3(b) positively. Archived full PDF and read the exact theorem/proof. AUX3(a) remains separate.
- [Ould Houcine, J. Algebra 307 (2007), 1–23](https://doi.org/10.1016/j.jalgebra.2006.07.015), primary publisher's indexed abstract, explicitly answers FP17 positively, even with one universal finitely presented group having solvable word problem. Full-text access failed (publisher 403, old author link 404); only the primary abstract scope was checked. Details in `research/notes/AUX3-FP17-prior-resolutions.md`.

## Matrix/metabelian scope checks, 28 September 2026 approximately 13:47–14:01 UTC

No additional candidate. Detailed conclusions and failed reductions are in
`research/notes/matrix-metabelian-scope-audit.md`.

- [Krasil'nikov, Math. USSR-Izvestiya 37 (1991), 539–553](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&paperid=1041&what=fullteng), Theorem 1 and its corollary, prove finite identity bases for groups with nilpotent derived subgroup and for connected linear groups. Archived Russian original and English translation; English p.539 inspected visually. This does not settle MA5's finite-extension case. An initial stale hash URL failed the PDF check; the `what=fullt` request then returned Russian despite `option_lang=eng`, correctly identified and retained as `-ru`.
- [Chorna–Geller–Shpilrain, arXiv:1605.05226v4](https://arxiv.org/abs/1605.05226), Section 2 and Theorem 4, concern special two-generator parabolic subgroups. Archived full text and read the relevant statements. The integer-parameter membership algorithm does not solve general MA3(b); the paper also retains MA6's rational-parameter question. No claim of current openness follows merely from its 2017 status discussion.
- [Artamonov, Uspekhi Mat. Nauk 32:3(195) (1977), 166](https://www.mathnet.ru/eng/rm3198), Theorem 1, explicitly assumes finite rank. Archived and read/viewed the one-page primary announcement. Its nonfree examples concern a different variety. The longer 1978 proof was not obtained; no infinite-rank M4 answer inferred.
- [Baumslag–Cannonito–Miller, Math. Z. 153 (1977), 117–134](https://doi.org/10.1007/BF01179785), publication verified at the publisher; full text unavailable here. The **bounded local degree** scope is reported in [Kourovka 5.16](https://alglog.org/20tkt.pdf), not independently checked in the original proof. FP9 remains unresolved here. A non-effective universal-tree observation is saved as a lead, with the recursive-presentation gap explicit.

## Braid scope audit, 28 September 2026 approximately 14:02–14:17 UTC

- [Bharathram–Birman–Brendle, arXiv:2607.05283v2](https://arxiv.org/abs/2607.05283v2), Main Theorem, answers B3 positively. First submitted July 2026, revised 14 September 2026. Archived primary PDF and checked the exact theorem/introduction; full proof not independently audited. Excluded as a prior preprint result.
- [Fromentin, JEMS 13 (2011), 1591–1631](https://ems.press/content/serial-article-files/31799), Theorem 1, answers B8 with c(n)=6(n-1)^2. The minimum/maximum index conversion and identity convention are recorded in `research/notes/braid-prior-resolutions.md`.
- [Bell–Schleimer, arXiv:2511.02459](https://arxiv.org/abs/2511.02459), Remark 1.7, explicitly answers B13 in O(N log^3 N) for fixed strand number. Archived; exact scope and divide-and-conquer argument checked, not a full independent audit of train-track machinery.
- [Dehornoy, arXiv:1711.09794](https://arxiv.org/abs/1711.09794), Section 3.2 and Question 3.19, gives the relevant B9 terminology. Its printed p.13 numerical bound 2^n conflicts with the certified 52 examples in B5; this does not refute the actual height-converse question. Exact scope and computational evidence are in `research/notes/B9-bounded-enumeration.md`.

All four original paragraphs and primary theorem pages were inspected visually. No additional candidate solution results from this pass.

## Free-group/group-action scope pass, 28 September 2026 approximately 14:20–14:47 UTC

- [Moravec–Morse, *Basic commutators as relations: A computational perspective*](https://users.fmf.uni-lj.si/moravec/Papers/mmpaper.pdf), Contemp. Math. 511 (2010), 83–92: archived and read in full. The weight-five result and failed rank-two weight-six attempt inform the bounded F20 probes. Jackson's [2008 publisher abstract](https://doi.org/10.1080/00927870802108148) uses weights six and seven together; a full-text CiteSeer attempt failed with 404. See `research/notes/F20-bounded-rewriting.md`.
- [Kharlampovich–Vdovina, arXiv:1710.10306](https://arxiv.org/abs/1710.10306), sections 2.3, 3.2, 6: archived and exact scope read. Corollary 3 is the finitely presented biautomaticity theorem; Conjecture 1 records the finite-generation gap. Neither CSA nor an affine tree action is silently promoted to a stronger property. See `research/notes/GA-scope-audit.md`.
- Further N8 class-seven/free-nilpotent commutator searches located no matching algorithm theorem. Earlier primary Roman'kov background remains credited. The rank-two extension proves its additional Lie minor and polynomial-lattice facts explicitly. Novelty remains provisional.

The original F20, GA2 and GA3 paragraph screenshots were inspected. No new whole-entry or additional partial count arises from these scope checks.

## Equations, algorithmic scope and N8 structure, 28 September 2026 approximately 14:48–15:11 UTC

- [Sela, arXiv:1012.0044](https://arxiv.org/abs/1012.0044), Theorem 9.1 and all of section 9: E5 has a prior full positive answer, including systems with coefficients and factors of arbitrary cardinality. Archived primary source and read printed pages 138–142; earlier Makanin–Razborov machinery was not independently audited.
- [Groves–Hull, arXiv:1704.03491](https://arxiv.org/abs/1704.03491), Theorem D, introduction and Definition 3.1: H12 has a prior positive answer, including torsion. The authors credit earlier Reinfeldt–Weidmann work. The coefficient/family distinction and the finite-generation conversion are recorded in `research/notes/equations-and-algorithms-scope-audit.md`; the full shortening proof was not independently audited.
- [Chiodo, arXiv:1002.2786v3](https://arxiv.org/abs/1002.2786v3), introduction and Theorem 4.2: bounded-length nontrivial-element output is impossible. This restricted result does not answer full A6. Archived and read the exact scope; original E5/H12/A6 full HTML and screenshots inspected.
- [Bryant–Kovacs–Stohr, 2005](https://archives.maths.anu.edu.au/people/Kovacs/K110.pdf), introduction, printed pp.147–148: explicitly states the homogeneous irredundant-set form of Shirshov's lemma for ordinary free Lie algebras. Archived and read this structural ingredient for the all-rank class-seven N8 argument. The restricted-Lie correction discussed elsewhere in that paper is not invoked.

Further searches for “free nilpotent commutator class seven”, “free nilpotent single commutator algorithm”, and “free nilpotent commutator equation decidable” did not locate a matching full decision theorem. The old class-two result and undecidability of general systems remain different scopes. This search does not certify novelty. Targeted F28/N5/M0 checks likewise did not locate a matching full prior answer; their novelty and correctness remain separate provisional assessments.

A title-level lead for Truss, [*Equation-Solving in Free Nilpotent groups Class 2 and 3*](https://doi.org/10.1112/blms/27.1.39), was checked against the primary publisher abstract: its negative class-three result concerns general unification, and its positive restricted result concerns class two. Neither statement supplies the present higher-class single-commutator algorithm. Only the abstract was read in this follow-up; no full-text claim is made.

## A4 follow-up, 28 September 2026 approximately 15:18–15:21 UTC

[Hass, arXiv:math/9712269](https://arxiv.org/abs/math/9712269), section6/Theorem10: archived and read the full finite-quotient argument. Its positive branch uses a geometric disk search. Replacing that branch by enumeration of proofs that all generator commutators vanish gives the requested presentation-only cyclicity algorithm, since knot-group abelianization is Z. This routine consequence of prior residual finiteness is excluded from discovery counts. Full original page, background and exact screenshot inspected. See `research/notes/A4-prior-cyclicity-algorithm.md`.

A further S5 search again found restricted direct-product results and the 2026 Deré–Vandermeersch co-Hopfian minimax paper, not a full answer for arbitrary finitely generated solvable Hopfian factors. No new scope claim or computation follows.

## Wider scope pass, 28 September 2026 approximately 15:23–15:45 UTC

- [Bou-Rabee–Hooper, arXiv:1708.02093v3](https://arxiv.org/abs/1708.02093v3), published AGT20 (2020),3329–3376: introductory classification and Theorem4.2 read. BP(2,4) is infinite and linear; larger-exponent linear images do not prove residual finiteness of their sources. Full PDF archived, not a full independent proof audit.
- [Dlugie, arXiv:2607.13316v1](https://arxiv.org/abs/2607.13316v1), Theorem1.2 and full group-theoretic section2: split sequence BP(2,m)->Br_4(m)->Br_3(m). The proof's mixed-commutator notation discrepancy and the unproved geometric section are distinguished in `research/notes/FP21-braid-reduction.md`. GAP separately checked the finite presentation maps using faithful free-group Artin actions.
- [Goldman, arXiv:2411.15434v1](https://arxiv.org/abs/2411.15434v1), introduction, graph conventions, Proposition3.7 and its proof: Br_3(m)=Sh(m,3,m) is linear. CorollaryF's triangle-free hypothesis does not hold for the Br_4(m) presentation graph, which includes its label-2 commuting edge. The elementary RF reduction is written out in the FP21 note; no solution or novelty claim follows.
- [Bridson, CMH78 (2003),752–771](https://ems.press/content/serial-article-files/42987), CorollaryC/4.2: negative H13 under the standard synchronous definition. Read definitions, introductory example, Theorem3.4 and section4; the older cubic-area proof remains a cited dependency. Original full HTML and screenshot inspected.
- [Przytycki–Wise, JAMS31 (2018),319–347](https://www.math.mcgill.ca/pprzytyc/JAMS.pdf), Corollary1.3 and pp.319–320, together with [Aschenbrenner–Friedl–Wilton (2015)](https://www.maths.gla.ac.uk/~mpowell/Aschenbrenner-Friedl-Wilton-3-manifold-groups-final-version-031115.pdf), sections4.7 and5.2(H.20): all knot-exterior cases virtually fiber. The compact boundary fiber gives a finitely generated free kernel, answering FP6 by a prior consequence. Both texts archived; original FP6 page and screenshot inspected. A mistyped monograph URL returned404 before correction.
- [Papistas, Comm.Algebra29 (2001),4693–4699](https://www.tandfonline.com/doi/abs/10.1081/AGB-100106781): primary abstract corroborates the original N1 background's full classification, not merely rank two. Abstract read online; direct archive request403, full proof not obtained. Original N1 page, linked background and screenshot inspected.
- [Gardam–Kielak–Logan, arXiv:2101.02193v3](https://arxiv.org/abs/2101.02193v3), introduction p.6: known hyperbolic preprocessing lacks recursive complexity bounds. This is not silently promoted to a lower bound for every promise algorithm in H4. Archived; no full H4 answer claimed.

Further searches over N4, solvable-group entries and group actions supplied no completed argument. All primary scope claims and limitations are in `research/notes/H13-FP6-N1-prior-scope.md`. No Kourovka mathematical/code transfer occurred.

## F27 follow-up, 28 September 2026 approximately 15:53–16:05 UTC

- [Barmak, *The winding invariant*](https://mate.dm.uba.ar/~jbarmak/windinginv4.pdf), section11.2, printed pp.52–53: archived and read the normal-root discussion, Question101 and the tiling examples. The examples are in the commutator subgroup; the actual F27 question excludes it. No full-paper audit claimed.
- [Linton–Nyberg-Brodda, arXiv:2501.18306](https://arxiv.org/abs/2501.18306), section1.3.2, printed pp.24–25, and the normal-root discussion in section2.8.2: archived and read these passages. The specific noncommutator-subgroup/infinite-root question is still stated as open. Its history and broader normal-root questions were kept separate; no audit of all cited original proofs claimed.
- [Cornell Topology Festival 2019 panel report](https://e.math.cornell.edu/sites/topology/2019/Panel-Discussion.pdf), Barmak segment, printed pp.6–7: read via web as an additional historical lead, not used in place of Barmak's paper. Not archived locally.

Full original F27 HTML, linked background and actual containing-paragraph screenshot were inspected. The finite abelianization constraint and free-factor reduction in `research/notes/F27-normal-root-lead.md` are elementary observations, not new solution claims. This limited search is not a certification that no later answer exists.

## N8 class-eight follow-up, 28 September 2026 approximately 16:29–16:40 UTC

Targeted searches for free-nilpotent single-commutator algorithms, class
eight and commutator equations found no matching full higher-class
decision theorem. This is a limited search, not novelty certification.
The already credited class-two result and general equation-system
undecidability are distinct scopes.

The primary abstract by Kenneth W. Weston, *Commutator equations over
free nilpotent class 2 groups*, AMS Notices January 1978, abstract
752-20-34, printed p.A-75, was read online in the
[original issue](https://www.ams.org/journals/notices/197801/197801FullIssue.pdf).
It announces a rank-two/class-two single-equation algorithm while
distinguishing undecidability of systems. Only this preliminary-report
abstract was read; no full proof audit or new prior scope beyond the
known class-two setting is inferred. An attempted archive of the full
issue was refused by `fetch_literature.py` because it exceeds its
20-MiB download limit. No local full-issue archive is claimed.

## M4 full-proof follow-up, 28 September 2026 approximately 17:29–17:38 UTC

Obtained and read Artamonov's full 1978 proof, [MathNet im1711, English PDF](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&paperid=1711&what=fullteng), including visual inspection of printed pages 221–222. Theorem 4 is explicitly finite-rank. The module freeness step and the basis compatible with the augmentation map both require an extension for M4. Bass's [original 1963 paper](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/bassbig.pdf), Theorem 3.1/Corollary 3.2, requires R/J(R) to be Noetherian; this fails for the countable Laurent ring. No full answer follows. Source files, exact hypotheses and the remaining gap: `research/notes/M4-countable-module-obstruction.md`. This supersedes the earlier inability to obtain the 1978 full proof.

## N3: published full-answer claim with a false construction lemma

28 September 2026, approximately 17:32–17:43 UTC. [Göbel–Shelah–Wallutis, Illinois J. Math. 47 (2003), 223–236](https://shelah.logic.at/files/203632/Sh-742.pdf), Corollary 3.7, states the full positive answer, without the cardinal assumption in the separate Theorem 3.8. Section 3 was read and printed pages 232–233 viewed. However, Proposition 3.5 is false: the monotone three-generator profile with singleton bound 1, pair bound 2 and full bound 5 has an explicit central element of order two. Exact integer-series and independent GAP certificates are retained. The preceding degree-three spanning step also has a small missing-conjugate counterexample.

Do not record N3 as a verified prior resolution from this paper. Equally, do not mistake the failed construction for a negative answer to N3: this particular nilpotent group has an obvious torsion-free nilpotent cover. Bounded title/correction/gap searches found no repair; novelty and broader bibliographic status remain unassessed. Detailed proof, limitations, failed first witness search and reproduction: `research/notes/N3-published-cover-audit.md`.

## Solvable-group scope refresh, approximately 17:52–18:03 UTC

- S9: [Timoshenko2006, MathNet al154](https://www.mathnet.ru/eng/al154), theorem and corollary, gives test rank r-1 and hence the full rank-two answer in every derived length. The final original background paragraph already records this. Primary PDF and abstract archived; printed p.456 visually inspected. Full proof not independently audited. Retired as a prior positive answer.
- S3: [Timoshenko1998, MathNet mzm1471](https://www.mathnet.ru/eng/mzm1471), Theorem2 and final corollary, covers last-derived relators, including proper powers there. The broader theorem assumes a centreless quotient and a group ring without zero divisors. Read the exact Russian PDF pages925,926,930,931 visually because extraction is garbled. English full-text endpoint returned non-PDF content. The module-invariant reduction and its unresolved annihilator obstruction are in `research/notes/S3-S9-scope-followup.md`.
- H16: the Roman'kov2018 paper with DOI10.1017/S0017089516000677 concerns **biautomatic** soluble groups. Its Theorem6.3 does not by itself answer the original **automatic** metabelian question. No full proof audit made in this pass.
- S4–S8: the targeted searches did not yield a further full answer. In particular, commutator-width results for free solvable Lie rings, and co-Hopfian direct-product results, retain their earlier scope cautions.

## N9 fixed-ambient follow-up, approximately 18:09–18:21 UTC

Read the introduction, definitions and final corollaries/theorem in the
web-extracted [author copy of Roman'kov2016](https://www.researchgate.net/publication/300075306_Diophantine_questions_in_the_class_of_finitely_generated_nilpotent_groups).
The fixed/uniform distinction is explicit. The original PDF could not
be retrieved: publisher HTTP202/empty, author-page HTTP403. Archived
and visually checked [Myasnikov's 2016 slides](https://www.macs.hw.ac.uk/~lc45/Conferences/2016/Slides_for_web/Miasnikov_Diablerets.pdf),
slide35 (physical PDF page65), which repeat the uniform construction.

The literal central-direct-product interpretation has a
cross-commutation obstruction. A class-two coproduct quotient repairs
the reduction, with the base embedding proved explicitly; the uniform
theorem is retained. Source terminology is qualified pending the
original PDF. The fixed-group question is still unresolved, and an
attempted encoding by retracts of a fixed base fails by equation
reflection. See `research/notes/N9-fixed-ambient-and-coproduct.md`.
No new candidate or novelty assertion follows.

## F41: rank-two growth and a candidate transfer, approximately 18:22--18:45 UTC

Archived and read the exact conjecture in [Puder--Wu,
Question 5.4](https://arxiv.org/abs/1304.7979), viewing PDF page18.
Archived [Puder's expansion paper](https://arxiv.org/abs/1212.5216),
read Lemma4.1/Claim4.2/Proposition4.3 and Theorem8.2, and viewed
pages14,37. The twice-traversal lemma is prior work. The primitivity-rank
bound already implies F41 for pi=2 in ambient ranks at least five.

[Erlandsson--Souto, Theorem1.1](https://arxiv.org/abs/1508.02265)
gives a polynomial bound for fixed curve orbits on the punctured torus.
Its precise statement was read and page1 viewed. Converting geodesic
length to an upper word-length count gives the needed polynomial
Aut(F2) cyclic-orbit bound, with powers and peripheral curves handled
separately. The entire deep curve-counting proof is not independently
audited here. The cited Khan rank-two bound in Shpilrain's
[Whitehead paper](https://shpilrain.ccny.cuny.edu/White3.pdf) was not
used, because the accessible descriptions concern minimum-length words
and the original Khan paper was not obtained.

A candidate transfer estimate through labelled core graphs yields
F41 for pi(w)<=2. Only pi=2 in ambient ranks three and four is retained
as potentially new scope, pending specialist/bibliographic review.
Bounded searches found no matching theorem, which is not proof of
novelty. The [2025 orbit-blocking paper](https://arxiv.org/abs/2505.00477)
and [Shpilrain's recent survey](https://arxiv.org/abs/2510.00889) were
also checked for scope and archived; neither is used to establish
novelty. Culler1981 was read for an abandoned quadratic-word route,
not used in the final argument. Exact reading limits, prior credit,
proof and finite evidence: `problems/F41/audit.md`.


## N8 class-nine structural source, 28 September 2026 approximately 19:09--19:34 UTC

- Poroshenko--Timoshenko, *Universal equivalence of partially commutative
  metabelian Lie algebras*, [arXiv:1107.0430](https://arxiv.org/abs/1107.0430),
  Theorem4.3, printed p.8: the derived ideal of the free metabelian Lie
  algebra is torsion-free over the polynomial ring. Archived exact PDF and
  text, read the theorem/proof, and visually inspected p.8. Used over Q to
  obtain injectivity of ad_z on L'/L''. The ordinary homogeneous Shirshov
  lemma remains credited to the earlier Bryant--Kovacs--Stohr source.
- Searches for free-nilpotent commutator decidability, single-commutator
  algorithms and class-nine commutator equations located no matching new
  primary theorem. The earlier Roman'kov and Duchin--Liang--Shapiro scope
  distinctions still apply. This bounded search does not certify novelty.

## N4 and MA6 scope refresh, 28 September2026 approximately20:56–21:11 UTC

Archived Kassabov math/0311488, Tolstykh0807.4341v2, Choi–Jo–Kim–Lee
2406.11378v1 and Jang–Yi2512.20524v3. Read their relevant introductions
and stated theorems, not the complete deep proofs. Original N4/MA6 pages,
background and actual renders inspected. Free-nilpotent tower theorems
do not cover all N4. The July2026 parabolic paper retains the rational
non-freeness conjecture and rules out using failure of the orbit test as
a freeness certificate. Precise references, reading limits and scope:
`research/notes/N4-MA6-current-scope.md`. No new mathematical count.

## H4 output-size candidate, 28 September2026 approximately21:00–21:15 UTC

Read the standard Dehn convention in Bridson Definition1.4 and
Ciobanu–Elder ICALP2019 Lemma13; viewed the latter page and the IAS
question slide. Archived sources and the 2012 MathOverflow discussion,
which supplies prior firsthand finite-group lower-bound suggestions.
The argument here uses a prefix-automaton order bound and short
metacyclic presentations. It is a candidate under explicit uniform
input/output, with novelty unresolved. Search queries and exact credit:
`problems/H4/audit.md`. No reliance on a claim that a historical problem
list establishes current openness.


## 2026-09-28T21:27:09.307003+00:00 — wider scope audit

Archived Diao-Feighn 2005 (F24(b), explicit prior full answer), Rees arXiv:2205.14911 (automatic-group scope), and the 22 July 2020 manuscript Polynomial-time proofs that groups are hyperbolic (positive certification may fail). Reading limits and exact implications are in research/notes/F24-automatic-scope-refresh.md. No exhaustive novelty or proof audit claimed.


## 2026-09-28T21:41:56.112567+00:00 — nonlinear class-ten extension

A bounded follow-up search for free-nilpotent single-commutator algorithms and class-ten equations found no matching nonlinear-family theorem. Rechecked the primary Truss1995 abstract (doi:10.1112/blms/27.1.39); its general class-three unification obstruction and restricted class-two positive result do not answer this scope. Novelty remains provisional. Archived the official Magma hyperbolicity page underlying the preceding H5 scope note.


## 2026-09-28T22:08:34.500889+00:00 — F38 decision-procedure dependencies and scope

Archived KLSS math/0409284 (Cor1.4 plus Section2), Ciobanu-Diekert-Elder1508.02149 (Theorem4/Cor5), Diekert-Elder1701.03297v6 (Theorem4.3, full constrained tuple relation), Lee math/0610833 (prior rank-two theorem), Ciobanu-Zetzsche2405.07911 (related prior counting inequations), and GAGTA2026 abstracts (OConnor rank-two algorithm). Rechecked Shpilrain2510.00889, whose archived version was published17June2026. Precise pages, actual visual checks, queries and reading limits are in problems/F38/part-a-audit.md. No exhaustive novelty or imported-proof audit is claimed.


## 2026-09-28T22:21:55.381017+00:00 — F34 higher-rank scope

Archived Dinowitz-Koch-Hyde-OConnor-Olive2512.13967v1 (Introduction/Question1.3, Section7) and Koch-Hyde-OConnor-Olive2606.13933v2 (Introduction/Question1.5); viewed page2 of each. Both discuss the higher-rank algorithmic gap. Reused prior Lee0802.0584 and June2026 Shpilrain survey records for credit. Newer book F33 corresponds to frozen website F34. Clark-Goldstein part(b) credited via source background; its full paper not obtained. Reading limits and queries are in problems/F34/part-a-audit.md; no novelty certification.
