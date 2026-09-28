# S3 and S9: source scope and a remaining module obstruction

28 September 2026, approximately 17:52–18:03 UTC. No new solution.

## S9 is already fully answered

The full original solvable-group page, S9 fragment and screenshot were
inspected. The final paragraph of the linked background already cites
Timoshenko's 2006 full answer; stopping at its earlier 2001 paragraph
would wrongly leave the higher derived lengths open.

[Timoshenko, *Computing Test Rank for a Free Solvable Group*](https://www.mathnet.ru/eng/al154),
Algebra and Logic 45 (2006), 254–260, proves test rank r-1 for the
relevant nonabelian free solvable groups of finite rank r. In rank two
this supplies test elements in every derived length at least two.
The introduction, theorem and corollary were read; the corollary on
Russian printed page456 was also inspected visually. The entire proof
was not independently audited. Primary PDF/abstract and retrieval
metadata are archived under `literature/raw/S9-Timoshenko-2006*`.
Exclude S9 as a prior full positive answer.

## S3 has additional prior positive cases

The complete original page, fragment, linked background and screenshot
were inspected. The intended nonabelian solvable setting is retained.
The background's Gupta–Shpilrain result has a proper-power restriction;
the general question is not settled merely by citing its title.

[Timoshenko, *Center of some solvable groups with one defining relation*](https://www.mathnet.ru/eng/mzm1471),
Math. Notes64 (1998),798–803, is archived as
`literature/raw/S3-Timoshenko-1998-ru.pdf`. The English endpoint returned
non-PDF content and was rejected. The Russian PDF's text extraction
is garbled; conclusions below come from viewed printed pages925,926,
930,931, retained in `literature/figures/S3-Timoshenko-1998/`.

Theorem2 assumes F free of finite rank at least two, T normal in F
with T<=F', f in F', R the normal closure of f, and Q=F/(TR)
centreless with Z[Q] having no zero divisors. It concludes that
F/(T'R) is centreless. The final corollary covers relators in the last
nontrivial derived subgroup of a free solvable group of derived length
at least three, including proper powers there. It credits prior work
of Krasnikov–Timoshenko. This does not remove the group-ring hypothesis
or settle arbitrary relators in S3.

## A precise remaining module question

The following elementary reduction records where a possible extension
would need new work. It is not a solution or novelty claim.

Let F=F(x_1,...,x_n), R=normal_closure(r), Gamma=F/R, and d>=2.
Put N=F^(d-1), Q=F/(NR), and G=F/(N'R)=Gamma/Gamma^(d).
Then

    1 -> A -> G -> Q -> 1,
    A = (NR)/(N'R) = Gamma^(d-1)/Gamma^(d).

Here (NR)'R=N'R, by expanding commutators and absorbing every factor
involving R into R. Thus A is the abelianization of the kernel of
Gamma -> Q.

The regular Q-cover of the ordinary presentation complex for
<x_1,...,x_n | r> has cellular boundary maps over Z[Q]

    Z[Q] --D(r)--> Z[Q]^n --boundary--> Z[Q],
    boundary(v_1,...,v_n) = sum_i v_i(q_i-1).

Use left module coefficients and the Fox identity
r-1=sum_i (partial_i r)(x_i-1). The image of the first map is the
left cyclic module Z[Q]D(r). Its first homology is the abelianization
of the cover's fundamental group, so

    A = ker(boundary) / Z[Q]D(r).

This uses H_1=pi_1 abelianization and needs no asphericity assertion
about the presentation complex. The deck action agrees with the
conjugation action up to the harmless inverse convention.

If Z(Q)=1, every central element of G lies in A, and conversely an
element of A is central exactly when fixed by Q. Therefore

    Z(G) = A^Q  when Z(Q)=1.

Proving that this invariant module vanishes in the outstanding cases
would supply the needed induction step. Merely writing its finite
chain complex does not decide its invariants or prove their vanishing.

In particular, suppose the literal free relator is r=u^m with m>1,
and u has nontrivial image v in Q. Then v^m=1 and

    D(r) = (1+v+...+v^(m-1))D(u),
    (v-1)D(r)=0.

The nonzero group-ring elements v-1 and 1+v+...+v^(m-1) multiply to
zero. Thus the domain assumption in the prior theorem actually fails
in this case, and cancellation of the Fox relator column is invalid.
No argument controlling this annihilator has been obtained here.

The module reduction and the scope audit add no candidate count.
No computational search of solvable quotients was undertaken and no
Kourovka-run argument or code was imported.
