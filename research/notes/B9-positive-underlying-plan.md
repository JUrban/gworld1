# B9: positive underlying second braid, without a strand bound

30 September 2026. The three-strand exclusion is committed as d876338.
Try to strengthen its positive-v half to every v=tau_(q-1), q>=3.
Every positive special braid has this form by the credited classification.

If A=I1(u) S(I1(v)) were in B3, support would give m(u)=q+1.
Write f=pi(u) and a=pi(A). The latter is an even permutation of three
positions, while pi(I1(v))=(q q+1). The exact permutation equation is
f(1 2)=a(q+1 q+2)S(f). Use the prior small-class theorem f^-1(1)<=2.
If f(1)=1, a is the descending three-cycle; the preimage of 2 gives an
injectivity contradiction. If f(2)=1, then a is identity and the
recurrence forces f=pi(tau_q). The epsilon/nu theorem then forces
u=tau_q itself. The Burau last columns of u and I1(v) have first entries
0 and -2, respectively, excluding their required right-B_q difference.

Write out the universal finite-permutation argument and matrix action.
For interface checks, reconstruct every possible f from a and f(1) at
q=3,...,64, compare both sides of the full permutation equation, and
retain the non-special survivor when the small-class hypothesis is
dropped. Independently check a finite range with native GAP permutations
and matrix products. Include q=2 as a valid boundary outside the theorem.
These checks support the universal written proof; they are not an
unbounded enumeration or a complete B4 classification.
