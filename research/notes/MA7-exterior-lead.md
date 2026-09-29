# MA7: truncated exterior-ring lead

First argument during the active run, 29 September 2026 approximately
07:22--07:24 UTC. Uncounted until proof, exact statement scope and independent
arithmetic checks are audited. No Kourovka-run mathematical artifact used.

For fixed n>=3, put m=2n^2+1 and take the degree-at-most-two exterior
algebra R=k + V + exterior^2(V), over k=F_3, with dim V=2m.
Let z=2 sum_i e_(2i-1) e_(2i), D=diag(1+z,1,...,1), and T=e12(1)D.
The unit commutator [1+e_(2i-1),1+e_(2i)] is 1+2e_(2i-1)e_(2i).
The standard elementary diagonal h(u)=diag(u,u^-1) gives
h(u)h(v)h(vu)^-1=diag([u,v],1). Thus D, and T, are elementary.
T has off-diagonal entry1, hence is nonscalar modulo every proper ideal.

Suppose T=[A,B] in GL_n(R). Let W span the degree-one parts of all
2n^2 entries of A and B. In the exterior quotient on V/W their entries
belong to the commutative even subring S=k+exterior^2(V/W); their inverses
do also. The determinant of their commutator is1, whereas det(T)=1+zbar.
But zbar cannot vanish: a bivector in W wedge V has alternating-matrix
rank at most2 dim W<=4n^2, and z has rank2m=4n^2+2.

This appears to handle even the stronger n>2/nonscalar condition, but
uses a NONCOMMUTATIVE ring. Check original/related problem conventions,
prior results on elementary groups over noncommutative rings, the quotient
and rank lemma, and an independent elementary factorization before any
count. For n=3 the ring has dimension742 over F_3 and the factorization
uses343 elementary transvections. No exhaustive GL_3(R) enumeration is
proposed or needed.

Follow-up 2026-09-29T07:32:23.155731+00:00: the complete argument and independent arithmetic audit
are in `problems/MA7/exterior-ring-proof.md` and `exterior-ring-audit.md`.
The website entry is already answered by prior work, so the construction
does not add a candidate. Its noncommutative-ring scope remains explicit.
