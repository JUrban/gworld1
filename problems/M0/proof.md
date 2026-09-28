# M0 — primitive-preserving endomorphisms of free metabelian groups

**Status:** whole-entry candidate, derived during the active GroupWorld run on
28 September 2026. The potentially new scope is finite rank at least three;
rank at most two was already known. Internally audited and checked on explicit
words; independent specialist review and further novelty checking remain due.

## Statement and conventions

Let F_n be the free group with basis x_1,...,x_n and let M_n=F_n/F_n''.
An element is *primitive* if it belongs to a free basis in the metabelian
variety. If an endomorphism phi of M_n sends every primitive element to a
primitive element, must phi be an automorphism?

This is the question obtained from the original M0 instruction, “the same as
F3, but for free metabelian groups.” In particular the rank is **finite**.
The original M0 and F3 fragments and their rendered statements were checked;
see `research/statement-audits/M0/` and `research/statement-audits/F3/`.

**Candidate theorem.** The answer is yes for every finite n. In fact, it is
enough to require that the images in M_n of primitive words of F_n are sent to
primitive elements of M_n.

We use left Fox derivatives, followed by abelianization, and put

    R = Z[X_1^{+-1},...,X_n^{+-1}],
    D(w) = (partial_1 w,...,partial_n w)^t,
    J_phi = (D(phi(x_1)),...,D(phi(x_n))),
    lambda = (X_1-1,...,X_n-1).

The standard formulas are

    D(uv) = D(u) + bar(u) D(v),
    lambda D(w) = bar(w)-1,
    D(phi(w)) = J_phi bar(phi)(D(w)).                 (1)

These derivatives factor through M_n. One way to see the last assertion is
that derivatives on F_n' are additive, so they vanish on F_n''.

We use Bachmuth's classical inverse function theorem: phi is an automorphism
of M_n if and only if J_phi is invertible over R. A precise primary statement
is [Gupta–Gupta–Roman'kov (1992), Lemma 1, p.517](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/3EC22EA15B41760ECEFAA91FE195F19D/S0008414X00010968a.pdf/primitivity_in_free_groups_and_free_metabelian_groups.pdf).
That paper uses right derivatives and row matrices. Transposition, the
involution X_i -> X_i^-1, and multiplication by diagonal monomial matrices
convert its criterion to the convention above. The criterion is prior work.

We will also use its elementary necessary consequence: if w is primitive in
M_n, D(w) cannot become the zero column under any homomorphism R -> K to a
field. Indeed, it is a column of an invertible basis Jacobian. This consequence
does not require a sufficient criterion for a *single* column to be primitive.

## 1. Reduce to an IA endomorphism

The assertion is immediate for n=0 or n=1. Assume n>=2.

Every primitive vector of Z^n is the abelianization of a primitive word of F_n.
Consequently the integer matrix B induced by phi sends all primitive integer
vectors to primitive vectors. It follows that det B=+-1. Otherwise, for some
prime p the matrix B modulo p has a nonzero kernel vector v. There is a
primitive integral lift of v: choose an element of SL_n(F_p) sending e_1 to v,
express it by elementary matrices and lift those matrices integrally. Its
first column is such a lift. B sends that column to a vector divisible by p,
a contradiction.

Lift B^-1 to a free-group automorphism and compose it with phi. We may
therefore assume that phi induces the identity on the abelianization. This
preserves both the hypothesis and the question whether phi is an automorphism.
In this IA case, (1) gives

    lambda J_phi = lambda,            J_phi(1,...,1)=I_n.       (2)

## 2. Detect a nonunit determinant over a finite field

Suppose for a contradiction that Delta=det J_phi is not a unit of R.
Its augmentation is one by (2). Thus Delta has at least two nonzero Laurent
monomials: a single monomial with augmentation one would be a unit.
Choose a prime p preserving two of its nonzero coefficients. The reduction
of Delta is a nonunit of F_p[X_1^{+-1},...,X_n^{+-1}]. A maximal ideal containing
it has residue field K finite over F_p, by the standard field form of
Zariski's lemma.

Let z_i be the images of X_i. Each z_i is nonzero. The corresponding character

    chi: M_n -> K*,                 chi(x_i)=z_i

has J_phi(chi) singular. Not all z_i are one, because Delta(1,...,1)=1.
We choose K to be this residue field, so K is generated as a field by the z_i.

The image of chi is a nontrivial finite cyclic group. Write z_i=s^{a_i} for a
generator s of that image, of order m. Since the z_i generate the image,
gcd(a_1,...,a_n,m)=1. Integer elementary basis changes send the exponent row
(a_1,...,a_n) to (0,...,0,d), where d=gcd(a_1,...,a_n). The element t=s^d
still generates the image, since gcd(d,m)=1. Lift the basis change to Nielsen
transformations. In the resulting free basis we have

    chi(x_1)=...=chi(x_{n-1})=1,     chi(x_n)=t != 1,
    K=F_p(t).                                               (3)

Changing basis retains singularity. More explicitly, if C is the evaluated
Fox matrix of the new basis in the old basis, then C is invertible. Because
phi is IA, the chain rule transforms the evaluated matrix by
C^-1 J_phi(chi) C. There is no differing target character in this formula.

Equations (2) and (3) now show that every vector in ker J_phi(chi) belongs to

    W = K e_1 + ... + K e_{n-1}.                            (4)

Indeed, applying lambda(chi) to J_phi(chi)v=0 gives
(t-1)v_n=0, whence v_n=0.

## 3. Primitive words detect every direction in W

Assume first that n>=3. For distinct i,j<n and an integer polynomial
P(T)=sum_{k>=0} a_k T^k, define a free-group automorphism theta by fixing all
generators except x_i and putting

    theta(x_i) = x_i product_{k>=0} (x_n^k x_j^{a_k} x_n^{-k}).       (5)

There are finitely many factors. This is an automorphism because the appended
word uses only generators other than x_i; its inverse appends the inverse
word. It preserves chi. At (3), the derivative of x_n^k x_j^{a_k} x_n^{-k}
is exactly a_k t^k e_j: the two x_n contributions cancel because chi(x_j)=1.
Thus the evaluated Fox matrix of theta is

    J_theta(chi) = I_n + P(t) E_{ji}.                         (6)

Since K=F_p(t), every element of K is P(t) for some such integer polynomial.
All elementary transvections on W are therefore realized by these actual
free-group automorphisms. Every theta preserves chi, so their evaluated
Jacobians multiply in the usual way, by (1). They realize SL_{n-1}(K), which
acts transitively on the nonzero vectors of W. Consequently, for each
nonzero v in W there is a primitive word w=theta(x_1) with

    D(w)(chi)=v.                                            (7)

No assertion that all metabelian automorphisms are tame is used; (5) supplies
the particular tame automorphisms needed, including in rank three.

For n=2 we need a slightly weaker statement. W is the line K e_1, so any
nonzero subspace of W contains e_1. The primitive word x_1 supplies that
column directly. No transitivity assertion for SL_1 is made.

## 4. Finish the proof

For n>=3 choose a nonzero v in ker J_phi(chi) and a primitive word w as in
(7). For n=2 choose w=x_1, whose column belongs to the nonzero kernel by (4).
Since phi is IA, the last formula of (1) gives

    D(phi(w))(chi) = J_phi(chi) D(w)(chi) = 0.

But phi(w) is primitive in M_n by hypothesis, contradicting the necessary
Fox-column condition above. Thus Delta is a unit. The adjugate formula makes
J_phi invertible over R, and Bachmuth's theorem makes phi an automorphism.
Undoing the initial composition proves the candidate theorem. QED.

## Scope, prior work and evidence

[Timoshenko (2020), Russian original p.419](https://www.mathnet.ru/php/getFT.phtml?jrnid=smj&paperid=5992&what=fullt)
records the rank-two positive answer of Gupta–Timoshenko (1997), leaves rank
greater than two open, and identifies Kourovka 14.85. The earlier
[Timoshenko (2015) result](https://www.mathnet.ru/php/getFT.phtml?jrnid=al&paperid=707&what=fullt)
about preserving primitive systems of length n-1 is distinct from preserving
individual elements. We inspected the original 2020 PDF and p.419 visually. The
[21st Kourovka Notebook, 14.85](https://alglog.org/21tkt.pdf) likewise lists
the question with the known low-rank case. This is a bibliographic comparison;
no argument or code from the previous Kourovka experiment was reused.

The novel candidate step is the finite-field detection argument above, using
the explicit transvections (5). Bachmuth's theorem, Fox calculus, Nielsen
basis changes, finite-field multiplicative cyclicity and Zariski's lemma are
standard ingredients, not discoveries of this experiment. Targeted searches
found no matching prior all-rank answer; this is not an exhaustive novelty
certification.

`scripts/check_m0_finite_fields.py` constructs 177 exact records with seed
9282617: 103 primitive-column orbits, 20 singular examples (including 16
changes of basis), and 54 automorphism controls. The fields have orders
3,4,5,8,9,16; ranks range from two to four. Every claimed primitive word comes
with an explicit free basis and its inverse. The largest basis word has
length 353. The Python run took 0.32 seconds on one core with a 4 GB limit.

`scripts/check_m0_gap.g` independently checks all 177 records using GAP finite
fields and affine-matrix evaluation of words, together with free-group
verification of both inverse-basis compositions. The successful run took
1.93 seconds on one core with a 4 GB limit. An initial checker failure used
an unavailable GAP function `KroneckerDelta`; its logs are retained as
`results/m0-gap-v1`. Replacing that call by explicit index comparisons gave
`results/m0-gap-v2`, with no errors or warnings. The computations check the
construction and conventions; the unbounded theorem rests on the proof.

Artifacts: `research/certificates/M0/checks.json`, `checks.g`; full run metadata
in `results/m0-finite-fields-v1/` and `results/m0-gap-v2/`. Further audit and
concrete examples are in `audit.md`.
