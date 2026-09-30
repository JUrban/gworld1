# G9: complete certified bridge atoms under terminal horizontal powers

30 September 2026, within the original window.

The quantitative flow-unfolding argument and its noncommutative extension
were reread without finding a new gap. Seek a stronger numerical lower
bound by completing the existing finite atom alphabet analytically,
without enumerating a larger ball or bridge-word radius.

For a rank-two strict bridge atom ending at height H, right multiplication
by b^k changes only horizontal flow on the terminal height H. It preserves
the atom property. Delete those terminal horizontal edges from its flow,
and retain H: this should identify precisely its right <b> orbit among
bridge atoms. For two flows with the same remaining data, their difference
is a finitely supported flow on one integer line, determined by its
boundary; hence it is exactly the terminal horizontal segment between
their endpoints.

Group the existing 21,483 certified atoms into those orbits. For one orbit
with known endpoint/cost pairs (y_j,l_j), use cost
f(y)=min_j(l_j+|y-y_j|) for every integer endpoint y. This is an explicit
representative cost, not a claim of global geodesicity. Between the least
and greatest recorded endpoints sum individually. Outside that interval,
the costs increase by one at each step, giving two geometric tails.
The sum over all these disjoint orbits is therefore a rational alphabet
generating function. The existing unique atom-factorization argument
applies to every finite subset; taking their increasing union should give
the reciprocal of its unique positive root as a lower growth bound.

Verify orbit grouping and cost envelopes from the original words in
Python and separately in native GAP. Prove the entire-tail statement in
writing; finite suffix checks are controls only. Keep the existing upper
bound and all original certificates unchanged. If successful, update the
current G9 numerical enclosure with explicit old/new provenance, retaining
partial status and the unresolved exact constant.
