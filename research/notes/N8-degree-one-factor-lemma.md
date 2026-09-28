# N8: the degree-one factor test works in every degree

28 September 2026, approximately 11:15 UTC. Auxiliary lemma, not a decision algorithm for the full problem in higher nilpotency classes. No additional candidate is counted.

The multilinear modular probe found a rank deficiency for the full outer-slot map beginning in degree five (rank 20 of 24 modulo 1000003). Thus the rank-two probes did not justify extrapolating full injectivity. A rational kernel check is recorded separately. However, the factor test needs a weaker property that has a direct proof in every degree.

Let V be a finite-dimensional rational vector space and L(V) its free Lie algebra in the tensor algebra. Let g be a nonzero homogeneous element of degree m+1, m>=2. We wish to decide whether g=[z,Y], where z is in V and Y in L_m(V).

For each word J of length m-1 in the basis alphabet, form

    q_J(t) = sum_(i,l) g_(i,J,l) t_i t_l.

If g=zY-Yz, then

    q_J(t) = (sum_i z_i t_i)
             (sum_l Y_(J,l) t_l - sum_i Y_(i,J) t_i).

At least one q_J is nonzero for every nonzero g admitting this factorization. Otherwise the polynomial ring being a domain and z nonzero force Y_(J,l)=Y_(l,J) for every J,l: Y is invariant under cyclic rotation of its tensor slots.

But the cyclic symmetrization of every homogeneous Lie element of degree m>=2 is zero. Indeed, each such element is a sum of brackets [U,W] of positive homogeneous degrees; concatenations UW and WU have the same cyclic symmetrization. If Y itself is cyclically invariant, its cyclic symmetrization is mY, so Y=0 over Q, a contradiction.

Consequently:

1. If all q_J vanish, reject this factorization type.
2. Otherwise factor one nonzero quadratic q_J over Q. There are at most two rational linear factors up to scalar, so at most two possible directions for z.
3. For each direction choose a primitive integer vector z0, and solve the integer linear system [z0,Y0]=g in an integral Hall basis of L_m.

This also decides **integral** factorization g=[z,Y]. If z=kz0 for a nonzero integer k, then g=[z0,kY], so a solution with z exists only if the test for primitive z0 succeeds. Conversely an integral solution for z0 is itself a solution. The map ad(z0):L_m -> L_(m+1) is injective: after a rational change of basis its associative centralizer in homogeneous degree m consists of multiples of X1^m, and that one-dimensional space meets L_m trivially for m>=2. Injectivity is helpful but is not needed for the termination of integer linear algebra.

This lemma replaces the degree-four injectivity certificate as the essential reason the type-(1,3) test terminates. The stronger degree-four certificate remains valid and was checked separately. It does not settle higher-class lifting or factorization types whose two leading degrees both exceed one.
