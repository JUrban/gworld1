# B9: the least remaining parameter exponent and a failed rigidity extension

29 September 2026. This continues `positive-parameter-reduction.md`.
It gives necessary conditions and a bounded probe, **not a new B4 count**.
All strand groups use the standard inclusions; write s=sigma1 and t=sigma2.

An additional four-strand special braid would have a terminal parameter
A=a S(c) in B3 with both a,c nontrivial special. The least possible total
exponent epsilon(A) is two. In that case epsilon(a)=epsilon(c)=1, so
uniquely

    a=I_1(u)=u s S(u)^-1,       c=I_1(v)=v s S(v)^-1,

where u,v are special. Uniqueness follows from Dehornoy's Lemma 5.6
because B1 is trivial. The parameter is therefore

    A=u s S(u)^-1 S(v) t S^2(v)^-1.                           (1)

Let m(w) be its smallest standard strand number, with m(1)=1.

## 1. Necessary adjacent strand numbers

Suppose A in (1) belongs to B3. Put r=m(u), q=m(v).

If v=1, then r<=2. Indeed, A=u s S(u)^-1 t, so
S(u)^-1=s^-1 u^-1 A t^-1. If r>=3, the right side belongs to B_r,
whereas S(u) has smallest strand number r+1, a contradiction.

If v is nontrivial, so q>=2, then

    r=q+1.                                                   (2)

For if r<=q, rearranging (1) gives

    S^2(v)=A^-1 u s S(u^-1 v) t in B_(q+1),

contradicting m(S^2(v))=q+2. If r>=q+2, then r>=4 and

    S(u)^-1=s^-1 u^-1 A S^2(v) t^-1 S(v)^-1 in B_r,

again contradicting m(S(u))=r+1. These are standard parabolic support
arguments, not inferences from a finite list of terms.

There is a further necessary condition. Since c=I_1(v), (1) is also

    A=u s S(u^-1 c).

For q>=2, (2) and A in B3 imply S(u^-1 c) in B_(q+1), hence

    h=u^-1 c in B_q.                                        (3)

In particular, the faithful Artin actions of u and c must send the
(q+1)-st free generator to exactly the same word. This last condition
is used only as a necessary test, not as a complete subgroup-membership
criterion.

The pair (a,c) is nonterminal precisely when u=c. An inverse step would
require a=c triangle d. Since epsilon(a)=1, special d must have exponent
zero, and therefore d=1. Thus I_1(u)=I_1(c), equivalent to u=c.

## 2. The smaller underlying braid cannot lie in B2

We first use a general elementary rigidity fact:

    If b,d are nontrivial special braids and b^-1 d in B2,
    then b=d.                                               (4)

Write d=b s^k. For k>0, its special decomposition is obtained by applying
T^k to (b,1), where T(x,y)=(x triangle y,x). After the first step both
colors are nontrivial and remain so. It cannot equal the special
decomposition (d,1), which is unique. For k<0 interchange b and d.
Thus k=0. The nontriviality hypothesis matters: 1 and s give a counterexample
if it is dropped.

If v=1, Section 1 gives u in B2, hence u=1 or s. These yield respectively
A=s t and A=s^2. Only the former has a terminal pair.

If v is the only nontrivial special braid in B2, namely s, then q=2,
c=s triangle 1=s^2 t^-1 and r=3. Condition (3), together with (4), forces
u=c. This gives A=c s and is nonterminal.

Thus in the present sector there are exactly three parameters with
v in B2: s t, s^2 and (s^2 t^-1)s. They are all in known cosets.
This statement concerns two nontrivial colors of exponent one; it does
not omit the previously handled parameter t s with colors (t s,1).

Consequently any **additional terminal parameter of total exponent two**
must have

    m(v)>=3, m(u)=m(v)+1, u!=I_1(v), u^-1 I_1(v) in B_(m(v)).

Its colors c and a have at least four and five strands respectively,
even though a S(c) would belong to B3. The identity m(I_1(w))=m(w)+1
follows from the support lemma in `small-strand-proof.md`, including
w=1 directly. We have not excluded this cancellation at higher strands.

## 3. The analogous rigidity assertion for B4 is false

One cannot replace B2 by B_q in (4), even when both special braids
lie outside B_q. Here is a compact counterexample. Put

    z=s triangle 1=s^2 t^-1,
    v=1 triangle z,
    u=1 triangle (z triangle 1),
    c=v triangle 1.

All are explicit special terms. By left self-distributivity, u=v triangle s.
It follows that

    u^-1 c=S(v) s^-1 t^-1 s S(v)^-1
           =sigma3^2 t s^-1 t^-1 s t^-1 sigma3^-2.             (5)

For the second equality use S(v)=sigma3^2 sigma4^-1 t and commute
sigma4 past s and t. Exact faithful actions verify

    m(u)=m(c)=5,       u!=c,       m(u^-1 c)=4.

Thus (3) need not force u=c. For this example the parameter
I_1(u) S(c) has smallest strand number five, so it is **not** a new
four-strand special braid. It rules out a proposed proof shortcut.

## 4. Targeted finite probe and independent checks

The earlier height-at-most-four list has 52 explicit special braids.
Among its 2704 ordered pairs (u,v), precisely 268 meet Section 1's strand
condition. This is a fixed term-height family, not an exhaustion of the
unknown higher-strand case. No earlier search depth was increased.

Of these 268, 254 fail the last-generator necessary condition in (3).
Ten have u=c and simplify to A=c s. Four need direct support checks.
Exactly three give A in B3, the three parameters in Section 2. The direct
checks yield two parameters of minimum strand number three, one of strand
number two, two of strand number four, and nine of strand number five.
No new coset is found.

The optimized Python implementation caches the underlying Artin actions,
uses the necessary-condition witnesses before constructing large expressions,
and checks the fourteen remaining support decisions both with faithful
free-group actions and the previously pinned CBraid canonical forms.
The independent GAP checker verifies the complete 268-pair coverage,
every obstruction, every u=c simplification and each direct support
decision. It also verifies (5) and its exact strand numbers. It does not
expand the 254 rejected large expressions; the proved implication (3)
is the justification for their rejection.

A boundary control for u=t s, v=s gives the pure braid

    t s^2 t^-1 sigma3^-1 t^2 sigma3^-1.

Its linking numbers with the fourth strand are respectively +1 for
strand two and -1 for strand three. Thus its trivial permutation cannot
be used to assert B3 membership. Python checks the linking numbers and
GAP independently checks exact strand number four.

### Retained runs and limits

- `b9-exponent-two-parameters-v1`: 90-second timeout, no usable output.
  The initial implementation had no stage logging, so the precise
  location of the timeout is unverified. Its exact source is retained.
- `b9-exponent-two-parameters-v2`: the filtered implementation passed in
  0.17 seconds; it has the same 268-pair mathematical scope.
- `b9-exponent-two-parameters-gap-v1`: failed because `rec` was used as
  an identifier although it is a GAP keyword. Exit code zero did not
  pass the marker/stderr checks. Exact failed source and logs retained.
- `b9-exponent-two-parameters-gap-v2`: corrected checker, including the
  compact rigidity counterexample, passed in 1.83 seconds with empty stderr.

All used one CPU and a 6 GB cap. The ignored CBraid binary is the earlier
`large-artifacts/tools/b9_strands_cbraid`, built from
`scripts/check_b9_strands_cbraid.cpp` and upstream CBraid revision
`891fcaf7cf9af3ec9ca0f1b0e46b0f86cf461b78`. The new certificate manifest
records the binary hash, both Python and GAP source versions, input
identities, outputs and all four run records. To replay a preserved first
version, put it at its original script path in a separate checkout; the
scripts resolve inputs relative to that path. Use fresh output paths or
a clean artifact directory, since successful outputs are never overwritten.

The original B9 statement and conventions are those already checked in
the preceding supplement. Imported ingredients remain Dehornoy's special
decomposition uniqueness, closure under left division and standard braid
parabolic support; no new external source or Kourovka transfer is used.
These are structural deductions and a failed-strategy certificate, not
a separate novelty claim. B9 remains partial. The experiment tally stays
at ten whole-entry candidates, two partial candidates and zero established
novel results; specialist review remains outstanding.
