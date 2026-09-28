# N8 penultimate-layer lead, 28 September 2026 approximately 13:21 UTC

Not yet added to the claim ledger. Proposed extension: decide single
commutators for every target in gamma_(c-1) of a finite-rank free nilpotent
group of class c. Central targets are already handled by the earlier
candidate; this concerns a nonzero degree-(c-1) leading term W.

The existing homogeneous bracket argument gives more than existence.
For unequal leading weights p<q, at most two rational lines for C occur.
For primitive C0 on such a line, [C0,D0]=W has at most one rational
solution, because different-weight nonzero Lie elements cannot commute.
All integral pairs on that line are (k C0,D0/k), where nonzero k divides
the content of D0. Hence the leading pairs form a finite list.

For equal weights, the exterior tensor W has rank two. Its primitive
support plane P and integral content d give a finite list of index-|d|
sublattices of P, each with an oriented Hermite basis. Exact Nielsen
transformations preserving the commutator realize SL_2(Z), so these
bases represent all possible leading pairs, allowing arbitrary higher
terms of the factors.

After choosing group lifts x0,y0 of a leading pair C,D, every further
factor correction relevant in class c has the form x=x0*u,y=y0*v,
where u,v have respective weights p+1,q+1. Its effect is exactly
[U,D]+[C,V] in the central degree c. Cross corrections have degree
p+q+2=c+1 and disappear. An integer linear system therefore decides
each of the finitely many branches.

Checks still required: complete normalization argument, both signs and
all integral scalings, all equal-weight Hermite branches, independent
word witnesses, negative controls and comparison with the earlier
class-five algorithm. No claim of covering other intermediate layers.

Update, approximately 13:30 UTC: the preceding checks are now complete.
Full proof and audit are in `problems/N8/penultimate-target-proof.md` and
`penultimate-audit.md`. Python passed 85 records; GAP checked 49 positive
witnesses and all 187 central membership branches, including 140 negative
branches. The original lead above is retained as a chronological record.
