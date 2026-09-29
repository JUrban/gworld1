# N9 supplement: isolated inputs and the free-nilpotent boundary

29 September 2026, approximately 22:00 UTC. This strengthens the existing
[fixed-group candidate](proof.md), without adding a problem to the tally.
Correctness and novelty still require external specialist review. The
original proof and its first evidence manifest remain unchanged.

## 1. Every subgroup in the construction is isolated

Use the notation of the candidate proof: the full integer kernel L has
basis B1,...,Bs, the ambient group has central coordinates z1,...,zs,
and

    H_n = <a,b_n>,  a=x0,  b_n=x1^(3n+1)x2^-1,
    c_n=[a,b_n],    q_n=(3n+1)B[0,1]-B[0,2].

An isolated subgroup H means that g^k in H, for g in G and an integer
k>0, implies g in H. No normality of H is assumed.

**Proposition.** In the candidate construction, G/G' is free abelian of
rank D and G' is exactly the central coordinate subgroup Z^s. For every
n in N, H_n is isolated. Moreover,

    H_n intersect G' = H_n' = <c_n>,

and the inclusions H_n/H_n' into G/G' and H_n' into G' identify direct
summands of these free abelian groups.

**Proof.** First, L is a saturated sublattice of Z^E, where E consists
of the upper-triangular matrix positions. Indeed L is the kernel of an
integer matrix, so Z^E/L is isomorphic to a subgroup of a free abelian
group and is torsion-free. Consequently a basis of L extends to a basis
of Z^E. The matrix K whose rows are the flattened B_l therefore has an
integer right inverse. Its columns generate Z^s. Those columns are
exactly the central coordinates of the commutators [xi,xj]. Hence
G'=Z^s, and the explicit normal form from the original proof identifies
G/G' with Z^D.

The original choice of the nonrecursive set S included both 0 and 1.
Choose the two matrices M0,M1 supplied by solutions at those parameters,
and write Mj=sum_l mu_j[l] B_l. Their normalization gives

    M0[0,1]=M1[0,1]=1,   M0[0,2]=0,   M1[0,2]=3.

For every integer n, put mu(n)=(1-n)mu_0+n mu_1. Then

    mu(n) dot q_n
      = (1-n)(3n+1) + n(3n-2)
      = 1.                                                   (A)

Thus q_n is primitive in Z^s for every n, including parameters outside
S. In particular <c_n> is a direct summand of G'. These two witnesses
and their coefficients are fixed; the argument does not need a
Diophantine solution at the input n.

The image of H_n in G/G' is

    V_n = <e0, (3n+1)e1-e2>.

This is a rank-two direct summand: the minor on coordinates 0,2 has
determinant -1. Since each element of H_n has unique form
a^r b_n^s c_n^j, its abelianized image vanishes exactly when r=s=0.
This proves H_n intersect G'=<c_n>=H_n'.

Now suppose g^k lies in H_n, k>0. Since V_n is primitive, the image of g
in G/G' lies in V_n. Choose h in H_n with the same image and write
g=h z, z in G'. Centrality gives g^k=h^k z^k, so
z^k lies in H_n intersect G'=<c_n>. Primitivity of q_n implies
z lies in <c_n>. Therefore g lies in H_n. This proves isolation. QED.

**Consequence.** Conditional on the main candidate proof, the retract
problem remains undecidable even for a computable family of isolated
rank-two free class-two subgroups, with primitive embeddings on both
lower-central layers. All H_n are still in the same one fixed G.
Separate splittings of the two abelian layers need not combine to a
homomorphism of groups.

There is a useful warning in (A). The interpolated matrix
M(n)=(1-n)M0+n M1 lies in L and satisfies the affine unit equation for
every n. It need not have rank two. On coordinates 0,1,2,3 its Pfaffian
is 9n(1-n), since M(n)[2,3]=9n and M(n)[0,2]=3n. For n other than 0
and 1 this particular interpolation fails the rank condition. This
does not exclude another rank-two matrix; for example n=4 is a positive
parameter of the toy circuit. The rank condition, not merely integral
primitivity, carries the Diophantine restriction.

## 2. Primary-source attribution clarified

The full Russian original of Roman'kov--Khisamiev--Konyrkhanova,
*Algebraically and verbally closed subgroups and retracts of finitely
generated nilpotent groups*, Sibirsk. Mat. Zh. 58(3) (2017), 686--699,
is now [archived from MathNet](https://www.mathnet.ru/php/getFT.phtml?jrnid=smj&paperid=2889&what=fullt).
English translation: Siberian Math. J. 58(3), 536--545.

Theorem 13, printed pp.695--696, supplies the free-nilpotent algorithm.
Theorem 10 on p.693 supplies its necessary generation condition. Both
proofs were read; actual pages 687,693,695,696 were rendered and viewed.
The rest of the paper was not fully audited.

The introduction on p.687 describes a class-wide undecidability result
and calls N9(a) solved, referring to Roman'kov's 2016 paper. That source
expressly distinguishes the uniform version in its introduction and
definitions, and its Theorem 3.4 varies the ambient group. The frozen
GroupWorld background also explicitly leaves the fixed-group question
open. Thus the 2017 introductory wording is not evidence of a further
fixed-group theorem. This remains an attribution point for specialist
review, not a novelty guarantee.

The 2016 reading is still of the author-uploaded extracted text, not a
visually inspected original PDF. Its introduction, definitions and
Theorem 3.4 had already been read on 28 September; it would be inaccurate
to describe our earlier access to that paper as abstract-only. Only the
2017 source was previously limited to its primary abstract.

The new PDF has SHA256
`c65c7061d476b11b71ad44956ca675d08ec66006d432ea16a34d6d19596996f7`.
The exact bytes, retrieval record, derived text and four page images are
included in the supplement manifest. See the earlier
[audit](audit.md) and [2016 scope note](../../research/notes/N9-fixed-ambient-and-coproduct.md)
for the source links and the separate product-notation qualification.

## 3. An elementary explanation of the algorithm's boundary

The following is an exposition of the credited free-case result, not a
new algorithm. Let N be a finite-rank free nilpotent group and H a
finitely generated subgroup. Write alpha:N->N/N' for abelianization.
Integral basis reduction of the supplied generators yields
h1,...,hm whose images form a basis of alpha(H), and additional
generators u1,...,uk in N'.

If H is a retract, H intersect N'=H': applying the retraction to an
element in the intersection proves the nontrivial containment. The
induced map on abelianizations then makes alpha(H) a direct summand.
Also H is generated by h1,...,hm. Indeed their images generate H/H',
and generation modulo the commutator subgroup implies generation in a
nilpotent group (successively use its terminating lower central series).
Consequently every u_j must belong to <h1,...,hm>.

Conversely, suppose alpha(H) is a direct summand and all the u_j belong
to <h1,...,hm>. Extend the abelianized h_i to a basis of N/N' and choose
lifts for the extra basis vectors. The resulting tuple generates N by
nilpotency. The endomorphism of the free nilpotent group taking its
fixed free basis to that tuple is surjective and hence an automorphism,
using the standard Hopf property of finitely generated nilpotent
groups. Sending the extra new basis elements to 1 gives a retraction
onto H. Integer basis reduction and the prior nilpotent subgroup
membership algorithm make these conditions decidable. The trivial
subgroup is included by taking m=0.

The last step uses freeness in the nilpotent variety. For a general
nilpotent G, extending an abelianized basis does not authorize arbitrary
images for the lifted generators: the extra defining relations must
still hold. The proposition above shows that the main candidate's
inputs meet even the primitive graded conditions, without removing
this obstruction. Neither Theorem 10's necessary condition nor the
free-case algorithm contradicts the fixed-group construction.

## 4. New verification and its limits

`scripts/check_n9_isolated_inputs.g` reads the existing toy fixture for
(y+1)^2=n. It checks an integer right inverse of the entire commutator
matrix and the polynomial identity (A), with an indeterminate n. It
also verifies the interpolated Pfaffian 9n(1-n).

GAP/nq constructs the actual toy group of Hirsch length 82 and verifies
G'=Z^68 and G/G'=Z^14. For n=-1,0,1,2,3,4,9, it checks H_n's Hirsch
length 3, H_n intersect G'=H_n', and the two torsion-free graded
quotients, of ranks 12 and 67. These checks cover necessary structural
conditions, not a search excluding retractions. The square-equation
obstruction for n=-1,2,3 still uses the main written proof.

Controls double the commutator vector (gcd 2 instead of 1) and replace
H_9 by <a^2,b_9>, which omits a although it contains a^2 and has a
nonprimitive abelianized image. The written argument, not finite root
enumeration, establishes isolation for every input.

Run `n9-isolated-inputs-gap-v1` failed at the polynomial unit comparison:
GAP distinguishes the constant polynomial 1 from the scalar integer 1
in that equality. The exact first script and logs are retained. Run v2
compares with `One(poln)` and explicitly prints the former scalar
comparison as false. It passed in 4.68 seconds with empty stderr. Both
runs reserved one core, 8 GB and 180 seconds; no random seed was used.
The first GAP process returned zero despite its error, and the recorder
correctly rejected it because the success marker was absent.

The universal DPRM circuit is still not numerically expanded. No full
formalization, external proof review or additional novelty claim is
made. This supplement introduces no dependence on the 2017 theorem into
the undecidability proof.
