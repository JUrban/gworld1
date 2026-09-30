# B9: test an all-strand permutation extension

30 September 2026, original active window. The latest completed scope
refresh is committed at 8c2d289. The preceding four-strand reduction leaves
one necessary permutation pair, with pure parameter and underlying
exponents differing by one. Investigate whether this pattern persists
when the underlying second braid has arbitrarily many strands.

This is a new structural question, not an increased special-term search.
For each strand number q, construct necessary permutation sets from the
right-branch representation I_p(H). At p=1 recurse through the preceding
set of possible special permutations; at p>=2 allow all permutations of
q-1 positions for H. These sets are upper bounds, not lists of special
braids. Keep the identity only at exponent zero.

For g=pi(v), put c=J1(g). If a=pi(A) is one of the three even permutations
supported on the first three positions, then J1(f)=a S(c)^-1. Writing
b=a S(c)^-1 gives f s1=b S(f), hence f(2)=b(1),
f(1)=b(f(1)+1), and f(i)=b(f(i-1)+1) for i>=3. Enumerate f(1), reconstruct
f, check the complete original equation and membership in the next
necessary permutation set. This avoids a quadratic product of sets.

Initially inspect q=3,...,7. Distinguish possible permutations from exact
minimum braid strand numbers: a fixed final position does not prove a
braid lies in a smaller strand subgroup. Retain any failure of the
proposed pure/exponent pattern. A universal deduction requires a written
argument; finite agreement alone will not establish it. If a compact
counterexample to a shortcut appears, verify it separately in GAP.
