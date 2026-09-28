# FP21: rank-two braid reformulation, not a resolution

28 September 2026. Sources checked approximately 15:23–15:40 UTC;
the residual-finiteness equivalence below was worked out at approximately
15:38 UTC. No new whole-entry or partial-solution count.

## Exact scope and prior work

The original FP21 asks whether, for sufficiently large m, the group
BP(n,m)=F_n/P_m fails to be residually finite, where P_m is generated
by the mth powers of all primitive elements. The whole original
`sources/raw/probFP.html`, the exact fragment, and its rendered paragraph
were inspected. The page SHA-256 is
`cc24ec170bd561a89fe5b18eac0f7b0759f269aabf5e2bbe9d94c06b46ae054e`;
the fragment starts at line 113. The statement does not print n>=2;
the rank-one cyclic case is not counted as a solution of the intended
nonabelian question.

Bou-Rabee–Hooper, *The extrinsic primitive torsion problem*,
[arXiv:1708.02093v3](https://arxiv.org/abs/1708.02093v3), published in
Algebraic & Geometric Topology 20 (2020), 3329–3376, already study
exactly these groups. Their introduction states that BP(2,m) is finite
exactly for m=1,2,3, and Theorem 4.2 gives a faithful nine-dimensional
representation for m=4. Thus m=4 is an infinite residually finite
example. For larger m their infinite linear images do not by themselves
show residual finiteness of BP(2,m). The introduction and relevant
theorem statements were read, not the full proof.

Dlugie, *Braid groups and Burnside groups*,
[arXiv:2607.13316v1](https://arxiv.org/abs/2607.13316v1), July 2026,
Theorem 1.2, gives the split exact sequence

    1 -> BP(2,m) -> Br_4(m) -> Br_3(m) -> 1,

where Br_j(m)=Br_j/<<sigma_1^m>>. All of the group-theoretic proof
in section 2 was read. It uses Br_4=F_2 semidirect Br_3 and the
transitivity of the modular action on primitive conjugacy classes.
The geometric discussion in section 3 is explicitly without proof
and is not an ingredient here. In the displayed kernel calculation
the initial expressions use an extra exponent on n, although N is
already the normal closure of sigma_1^m; the subsequent computation
uses the mixed-commutator quotient of Lemma 2.5 and the correct
conjugates g sigma_1^m g^-1. We invoke the theorem with that interpretation,
not the inconsistent intermediate notation.

## A precise residual-finiteness equivalence

For every positive integer m,

    BP(2,m) is residually finite iff Br_4(m) is residually finite.

This is a consequence of Dlugie's splitting and standard residual
properties, not an answer about which sufficiently large m satisfy it.

**Lemma 1.** If K is finitely generated and residually finite, and Q is
residually finite, then K semidirect Q is residually finite.

For (k,q) with q nontrivial, use a finite quotient of Q. For (k,1)
with k nontrivial, choose a finite-index subgroup U of K avoiding k.
There are only finitely many subgroups of K of index [K:U], since K
is finitely generated. Their intersection N is characteristic,
finite-index, and avoids k. The action of Q on K/N has finite image
A<=Aut(K/N). The map K semidirect Q -> (K/N) semidirect A separates
(k,1). This proves the lemma. The converse implication for K follows
from residual finiteness passing to subgroups.

**Lemma 2.** Br_3(m) is residually finite for every positive integer m.

For m=1 this is immediate. For m>=2 write a,b for the usual braid
generators and put v=ab, u=aba. The braid relation gives

    Br_3(m)=<u,v | u^2=v^3, (v^-1 u)^m=1>.

Here z=u^2=v^3 is central. Killing z gives the orientation-preserving
triangle group Delta(2,3,m), and the kernel is precisely the cyclic
group C=<z>, possibly finite. For m<6 the triangle group is finite,
so Br_3(m) is cyclic-by-finite and residually finite: a noncentral
element is detected in the triangle quotient, and a nontrivial element
of C is detected in a quotient by a suitable subgroup <z^k> of C.

For m>=6 the triangle group is residually finite and has a torsion-free
finite-index subgroup S that is a closed orientable surface group
(a torus for m=6). These are the standard Euclidean/hyperbolic triangle
group facts. Let E be its inverse image in Br_3(m). A nontrivial element
whose image in the triangle group is nontrivial is already separable
by a finite quotient. It remains to separate z^n nontrivial in C.

Choose surface generators and lift them to E. The central extension
has a presentation

    <a_1,b_1,...,a_g,b_g,z |
      z central, product_i [a_i,b_i]=z^e>

with additionally z^s=1 if C has finite order s. This presentation
follows by lifting the single surface relator; all other lifted
relations follow from it and centrality. If C is infinite, choose
k>=2 not dividing n. If C is finite, choose k=s. In the finite
Heisenberg group of upper-unitriangular 3x3 matrices over Z/kZ, send

    z   -> I+E_13,
    a_1 -> I+E_12,
    b_1 -> I+e E_23,

and all other a_i,b_i to identity. Use [a,b]=a^-1 b^-1 a b.
Then [a_1,b_1]=I+e E_13=z^e and z^n has nontrivial image.
This gives a finite quotient of E separating z^n. Taking the core
in Br_3(m) of its kernel gives a finite quotient of Br_3(m) separating
the same element. Hence Br_3(m) is residually finite.

The lemma is also covered by Goldman's stronger linearity result for
all dihedral Shephard groups: *2-dimensional Shephard groups*,
[arXiv:2411.15434v1](https://arxiv.org/abs/2411.15434v1), Proposition 3.7,
with Br_3(m)=Sh(m,3,m). Its introduction and the relevant proposition
were checked. The elementary argument above only needs residual
finiteness, not the stronger linearity conclusion.

Now BP(2,m) is two-generated. Apply Lemma 1 to Dlugie's splitting and
Lemma 2. The reverse direction follows from the injection of BP(2,m)
into Br_4(m). This proves the displayed equivalence.

## Why the available Shephard theorem does not finish FP21

Goldman's Corollary F proves residual finiteness for certain
triangle-free **presentation graphs**. In this convention commuting
generators are joined by a label-2 edge. The presentation graph of
Br_4(m) has three vertices and edges labeled 3,3,2: it is a triangle.
Its associated Coxeter group is the finite rank-three group of type
A3, so it also fails her two-dimensional hypothesis. The usual
unlabeled Coxeter diagram, which omits commuting edges, must not be
substituted for this presentation graph. No application of Corollary F
to Br_4(m) has been obtained.

Nor is a complex-reflection representation of a truncated braid
group automatically faithful. An infinite residually finite quotient
is insufficient; residual finiteness does not pass from a quotient
back to its source. These are the outstanding obstacles to this route.

## Artifacts and limits

The primary PDFs, retrieval metadata and derived text are in
`literature/raw/FP21-{BouRabee-Hooper-1708.02093,Dlugie-2607.13316,Goldman-2411.15434}.*`.
Their PDF hashes, in that order, are:

- `932ad1eb21a2764f9be9a15802db253e1eb62bf7a7dc2997c1da96d4909694ce`
- `34cfe917932faa1f32e8df5a77539cb24727ce864b61bf5eb8fbe8f9c46655df`
- `0f014c0fd0238c62d3318e261018cfa15e561d998f26ebb4f733173847849b94`

The finite identities behind the cited splitting were checked in GAP
4.16.1 using the faithful Artin action on a free group, separately from
the modular-action semidirect-product normal form. The check covers
all four conjugation formulas, both-sided modular inverses, the modular
braid relation, all three B4 relations in the semidirect product, and
recovery of the generators under the two maps. An incorrect-sign
control is detected. The deterministic script is
`scripts/check_fp21_braid_split.g`; run
`results/fp21-braid-split-v1` passed in 1.83 seconds with one CPU slot,
a 2GB limit, and empty stderr. Its raw stdout has an initial carriage
return, which is preserved. No random seed or bounded search is involved.
This finite presentation check does not test residual finiteness or
replace the universal argument about primitive conjugacy classes.

The written reduction has an internal argument only, not independent
specialist review. It is not claimed novel and adds no counted solution.
Higher ranks and the large-exponent assertion remain unresolved here.
