# H4 closing proof audit

30 September 2026, approximately 02:38--02:40 UTC. Same-agent review;
no new gap identified and no new novelty determination. The candidate
continues to concern uniform conversion with explicit word output.

Read both complete proofs, the original scope/computation audit, and the
full infinite-input audit. Reread the complete original hyperbolic-group
HTML and actually viewed H4's retained statement. It has no torsion-free,
infinite, fixed-generator or non-elementary restriction. Reread Batty's
notes after Papasoglu, Theorem 3.27 with its full local proof, and viewed
printed page 29. This short torsion-representative lemma remains credited
classical material; no new audit of the entire lecture notes is claimed.

The first argument uses more than regularity of the irreducible-word
language. Its forbidden factors include cancellation and every minimal
strictly shortening relator segment. A reachable cycle would yield
arbitrarily many repetitions of its nonempty label in that factor-closed
language. Finiteness of the group makes a positive power an identity,
contradicting the Dehn property. The prefix-state bound and geodesic
coverage therefore give the stated group-order bound for **every**
explicit output presentation, regardless of its generating set.

The short input family is proved to be the full finite semidirect
product, not merely to possess that finite quotient. Eliminating auxiliary
generators bounds the cyclic normal subgroup and quotient from above;
the explicit action by doubling supplies the matching lower order.
Auxiliary square relations are ordinary length-three words, so the
O(n log n) input bit bound does not conceal compressed exponents.

For the strengthened argument a torsion representative is minimized
over its **conjugacy class**. A shortenable segment crossing a seam in
a power fits in one cyclic rotation once its length is at most that of
the representative. This gives length less than the longest relator,
including identity via the empty word. Counting its normal cyclic
subgroup uses doubling **orbits**, not distinct elements: at least
(2^(2^n)-1)/2^n classes survive.

Adding a free generator gives K_n free-product Z. The kernel of the
retraction onto K_n is free on its |K_n| conjugates of that generator;
free-product normal form proves both generation and independence. Its
finite index and rank at least six show that the input is infinite,
virtually free and non-elementary. The same normal form preserves
conjugacy classes of the finite factor. The earlier automaton acyclicity
is not applied to this infinite group.

The resulting inequality m log2(2m)>2^n-n-1 forces superpolynomial output
in the actual input bit length, even with changed generators. This is
an output-size argument independent of P versus NP. It does not cover
compressed output or a torsion-free input restriction. Successful finite
checks were not rerun; they supply examples and representation controls,
while the all-n implications remain the written argument. No count or
deadline change follows from this audit.
