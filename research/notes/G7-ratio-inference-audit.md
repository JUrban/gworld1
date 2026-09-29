# G7: a ratio-inference gap, not a group counterexample

29 September 2026. **G7 remains unresolved here; no new candidate.**

The original growth HTML was read in full and its actual G7 rendering
viewed. The question concerns ball cardinalities a(n)=|B(n)| for a
finitely generated group of subexponential growth, and asks whether
successive ratios converge. The limit, if it exists, must be 1.

Arzhantseva--Cherix, *Quantifying metric approximations of discrete groups*,
Example24 on printed/PDF page17 of the author-hosted archived version,
asserts that a(n)^(1/n)->1 implies a(n+1)/a(n)->1. It cites Lemma6.11.1
of Ceccherini-Silberstein--Coornaert, *Cellular automata and groups* (2010).
The exact displayed implication on page17 was actually viewed, not merely
inferred from extracted text. The following analysis shows why the
stated numerical implication is insufficient. It does not prove that the
conclusion is false for group growth, or that the cited book lemma is false.

## Numerical control

Put a(n)=2^ceil(log_2(n+1)) for n>=0. This is a nondecreasing positive
integer sequence with a(0)=1 and

    n+1 <= a(n) < 2(n+1).

It is submultiplicative: n+m+1<=(n+1)(m+1)<=a(n)a(m), and the last
quantity is a power of two. The least power of two at least n+m+1 is
therefore at most a(n)a(m). Its nth root tends to 1. But a(n+1)/a(n)=2
when n=2^k-1 and is 1 otherwise. The ratios do not converge.

This sequence is NOT asserted to be a group growth function. It only
rules out a proof using subexponentiality, monotonicity and
submultiplicativity alone. No computation is needed for this exact proof.

## What the numerical argument does give

For any nondecreasing positive sequence with log a(N)=o(N), and epsilon>0,

    #{0<=k<N : a(k+1)/a(k)>=1+epsilon}
      <= (log a(N)-log a(0))/log(1+epsilon) = o(N).

This follows by adding the nonnegative successive logarithmic increments.
Thus the ratios tend to 1 in natural density and have lower limit 1.
Neither assertion is the ordinary convergence required by G7.

The existence of suitable Folner balls does not require full convergence.
For each fixed n>=1 and delta>0, arbitrarily large m satisfy

    a(m+n)/a(m) <= 1+delta.

Otherwise iteration on an arithmetic progression would force a positive
exponential growth rate, contradicting subexponentiality. With

delta=1/(2n a(n)), A=B(m), and g in B(n), one has

    |gA symmetric_difference A| <= 2(a(m+n)-a(m)).

Summing over g in B(n) gives a sum at most |A|/n. This is the needed
Folner property. With the paper's page16 definition of Folner function
as minimum CARDINALITY, this proves a bound by a(m), not by the radius m.
We do not adopt the displayed radius bound at the end of Example24 as
written. The existence argument is elementary prior amenability machinery,
not a solution to G7 or a novelty claim.

## Sources and reading limits

Author source: https://www.mat.univie.ac.at/~arjantseva/Abs/mprofile.pdf
archived as `literature/raw/G7-Arzhantseva-Cherix.pdf`, SHA-256
`c106c304dd040c8f7fb5af818c4daada50127ba39557f1bd60a586d0d42ec98b`.
Read Section4.2's definition and Examples24--25 as text and viewed page17;
not a full audit of the metric-profile paper. Numbering refers to this
archived version and need not coincide with journal numbering.

The cited book's official chapter page
https://link.springer.com/chapter/10.1007/978-3-642-14034-1_6
confirms the amenability theorem's location but does not expose the full
lemma. The author's errata page
https://irma.math.unistra.fr/~coornaer/errata_caag.html
was checked; it supplies no replacement statement for Lemma6.11.1.
The exact book lemma was not obtained and is not described as read.
Search snippets, informal discussions and unofficial book mirrors were
not used to certify a current resolution or openness theorem.

The correct status is a documented limitation of this proposed literature
route. No group counterexample, full positive solution, or count increase
is claimed.
