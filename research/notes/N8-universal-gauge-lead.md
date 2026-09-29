# N8: universal exact commutator-preserving corrections

29 September 2026, developed about11:54–12:03UTC. **New proof lead;
implementation, statement/source recheck and audit pending. Not yet counted.**

Let C,D be noncommuting homogeneous elements of a free rational Lie
algebra, of weights p<=q. The existing correction map is
A_t(U,V)=[U,D]+[C,V], U in L_(p+t), V in L_(q+t).
The prior inner-solution lemma, applied in
Q*C+Q*D+L_(>=q+1), shows every kernel for t>q-p lies in Lie(C,D).
At t=q-p>0 the kernel is the Nielsen line. The same inner-solution
conclusion holds at every positive t when p=q.

## Universal integration of a kernel direction

Take the weighted free Lie algebra on a,b of weights p,q, truncated
above c. Put W=log(exp(-a)exp(-b)exp(a)exp(b)). There is a rational
filtered automorphism sigma with sigma([a,b])=W and leading identity.
Construct it degree by degree: every homogeneous derived Lie component
is spanned by [a,L]+[L,b], by Jacobi induction. In degree p+q+t its
correction can therefore be written [U,b]+[a,V], with U,V of weights
p+t,q+t. Adding those corrections to the two current generator images
removes the error at that degree and changes only higher degrees.
Associated-graded identity makes the resulting finite substitution an
automorphism. This is an elementary finite symplectic-expansion argument.

A homogeneous derivation delta with delta(a)=U, delta(b)=V and
[U,b]+[a,V]=0 preserves [a,b]. It raises weight by t>0, so its exponential
is a finite rational unipotent automorphism. Consequently

    alpha = sigma exp(delta) sigma^(-1)

fixes W exactly and has first generator increments U,V at offset t.

Let Gamma be the weighted nilpotent group on two generators obtained
by killing all basic commutators of weight>c. Hall collection gives
unique integer coordinates on the retained basic commutators; the
omitted coordinates form an isolated normal subgroup. Thus Gamma is
torsion-free and its rational Malcev algebra is the weighted truncation
just used. For alpha^n and alpha^(-n), the Hall coordinates of both
generator images are rational polynomials in n, with integral constant
terms. A common multiple M of their nonconstant denominators makes
both directions integral at n=M. Hence alpha^M is an automorphism of
Gamma fixing its group commutator. Its generator images are actual
finite group words. Testing factorial powers terminates by this argument.

For ANY group of nilpotency class<=c and ANY pair x in gamma_p,
y in gamma_q, substitution a->x,b->y factors through Gamma. The same
two words therefore change x,y while preserving [x,y] exactly. Their
first increments are M U(C,D), M V(C,D); lower offsets are unchanged.
No extension to an automorphism of the ambient group is required.
The leading terms need not be primitive or free generators in a larger
graded-tail algebra. Injectivity of Lie(a,b)->Lie(C,D) follows because
noncommuting C,D freely generate a two-generator Lie subalgebra.

For a Z-basis of ker A_t choose its rational expressions in Lie(C,D)
and perform the preceding construction. It supplies a full-rank lattice
of exact first increments inside the integral kernel. All integer
correction solutions can then be reduced to finitely many residues,
with every commutator and earlier correction kept unchanged.

## Immediate branch scope

If every pre-Nielsen A_t (0<t<q-p) is injective, every layer has either
one correction or finitely many exact-gauge residues. The usual integral
linear system at each layer therefore gives a complete terminating
branch algorithm in arbitrary class. Stop at t=c-p-q; corrections beyond
this point do not affect the commutator. A negative answer requires
checking every finite residue branch.

In particular this holds for q-p<=2. Only the gap-two case has a possible
pre-Nielsen offset, t=1. The inner-solution lemma would force nonzero
D,V into Lie(C,U), with U of weight p+1. If p>=2 there is no nonzero
Lie word of weight p+2 in C,U. For p=1, D is a scalar [C,U]; the two
sides [U,D] and [C,V] have different C,U multidegrees and cannot agree
unless D=0. Thus A_1 is injective. This covers every degree-four target
in arbitrary class, including the previously excluded type(1,3).

## Separated exceptional offsets

More generally let the nonzero pre-Nielsen kernel offsets be
 t_1<...<t_k. Each has dimension1, the next offset is injective,
and its quadratic obstruction at offset2t_i is nonzero modulo im A_(2t_i),
by the existing general-offset proof. Suppose consecutive exceptional
offsets satisfy t_(i+1)>=2t_i.

After earlier choices are fixed, let t be the first remaining exceptional
offset. If 2t>c-p-q, all remaining equations in the as-yet free corrections
are jointly linear; decide their complete integer system. Otherwise
consider the layers from t through2t-1. Their equations are jointly
affine linear in the exceptional parameter k and every later correction:
two still-variable corrections cannot interact below offset2t.

Any kernel at an intermediate offset is an exact universal gauge. Its
action on this finite block is translation by an integer vector independent
of k and the other unknown corrections: its first offset exceeds t, so
interaction with such unknowns first appears above2t. Successive leading
coordinates show these translation vectors span, over Q, the full kernel
of projection of the joint solution space to k. Their lattice therefore
has finite index in the integral fiber kernel. Smith/Hermite operations
produce finitely many affine points or integer lines modulo this lattice.
On a line k=k0+m*s, m!=0, all correction coordinates are affine in s.

At offset2t the residual is quadratic in s with nonzero coefficient
m^2[U,V] modulo im A_(2t). Higher offset corrections in the block contribute
only affinely there. A nonzero rational cokernel coordinate gives finitely
many integer roots; retain exactly those passing the full integral layer
system. Handle an exceptional kernel at offset2t only AFTER fixing k;
it is not an intermediate variable and does not cancel the obstruction.
Iterate. Exact gauges normalize all subsequent post-Nielsen kernels.

The separation condition follows automatically from the proved absence
of consecutive exceptional offsets whenever q-p<=5 (pre-Nielsen offsets
then lie in {1,2,3,4}). Thus this lead would cover ALL leading target
degrees<=7 in arbitrary class, and, with the existing six-final-layer
scope, all targets in classes<=13. These are consequences still requiring
a separate written audit and finite construction controls before recording.

No general claim is made when pre-Nielsen offsets overlap, e.g.3 and5.
The earlier warning about such interactions remains valid.


## Candidate proof and finite construction audit completed (2026-09-29T12:13:43.448957+00:00)

The lead is now assembled in `problems/N8/universal-gauge-proof.md`, with
its precise statement and evidence in `universal-gauge-audit.md`. All22
universal maps and32 decomposable-pair substitutions pass independent GAP
checks. The full branch algorithm remains unimplemented end to end. The
recorded partial scope is leading degrees <=7 in arbitrary class and all
targets in classes <=13, plus the more general separated-offset criterion.
This supersedes the lead-pending status above; it is not a full N8 answer
or established novelty.
