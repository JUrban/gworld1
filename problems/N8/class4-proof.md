# A decision procedure for one commutator in free nilpotent groups of class four

**Candidate partial answer to N8(b), 28 September 2026.** This extends the argument in [the class-three proof](class3-proof.md). Novelty remains provisional and no outside review has occurred.

**Theorem.** Uniformly for finite rank r, membership in the set of single commutators in F_r/gamma_5(F_r) is decidable, and witnesses are constructible.

We use the effective Hall collection coordinates for free nilpotent groups and their identification with the integral free Lie layers. Equivalently, the Magnus expansion through degree four is faithful on this quotient. These are the usual free-nilpotent collection facts; the remaining argument is given below. The exact original N8(b) statement has no bound on nilpotency class, so this is still a partial answer. The commutator convention is x^-1 y^-1 x y.

Let N=F_r/gamma_5. Use its integral Magnus expansion through degree four and the free Lie layers L_i.

## Nonzero degree-two image

Use the same finite list of abelianization pairs u,v as in the class-three proof. For each pair, the degree-three correction map

    (C,D) in L2+L2 -> [C,v]+[u,D]

is injective over Q when u,v are independent. Indeed u tensor D−v tensor C has its first slot supported on a two-plane; if its bracket vanishes, the class-three alternating-tensor lemma makes the tensor zero. Independence of u,v then gives C=D=0.

Thus the degree-two corrections to x,y, when they exist, are uniquely determined and can be tested for integrality. Select lifts incorporating these corrections. The remaining gamma_4 discrepancy is corrected by elements of gamma_3 in x,y; this is an integer linear system in L3+L3 -> L4. A finite list of such systems decides this case.

## Degree two zero, degree three nonzero

Normalize the abelianization pair to (z,0). Its degree-three value is [z,Y] with Y in L2. The class-three reconstruction determines the unique rational tensor. Let z0 be a primitive integral first vector and Y0 its corresponding integral second vector. If Y0 is not integral there is no solution.

All integral possibilities are z=k z0, Y=Y0/k, where the nonzero integer k divides the content of Y0. This is a finite list (include both signs). For each pair choose lifts x0,y0 with x0 of given abelianization and y0 in gamma_2 of given degree-two image. In class four,

    [x0 c,y0 d] = [x0,y0] [c,y0] [x0,d],

for c in gamma_2 and d in gamma_3. Both correction terms are central. Every possible lift is covered (higher corrections in x or y are irrelevant). Another integer linear system in L2+L3 -> L4 decides the case.

## Pure degree four

For a nonzero g in gamma_4, there are exactly two possible leading-weight types after the same normalization:

1. Both abelianizations vanish: g=[C,D] for C,D in L2.
2. One abelianization is nonzero: g=[z,Y] for z in V and Y in L3. Its potential degree-two part vanishes because [z,L2] is injective.

### Type (2,2)

The map Lambda^2(L2) -> L4 is injective: L2 embeds in V tensor V, and the map is just the inclusion of skew tensors C tensor D−D tensor C in V^tensor4. Recover its unique coefficients by rational/integer linear algebra. There is an integral pair C,D exactly when the recovered alternating form is integral and has rank two (nonzero case). The primitive support-plane construction from class three supplies such C,D. This is effective.

### Type (1,3)

For each middle pair j,k form the homogeneous quadratic polynomial

    q_jk(t) = sum_(i,l) g_ijkl t_i t_l.

If g=[z,Y], then

    q_jk(t) = (sum_i z_i t_i)
              (sum_l Y_jkl t_l − sum_i Y_ijk t_i).

Thus the linear form with coefficient vector z divides every nonzero q_jk. If all q_jk vanished for a nonzero element [z,Y], the polynomial ring being a domain would force Y_jkl=Y_ljk for every j,k,l. Then Y would be cyclically invariant. But cyclic symmetrization annihilates every Lie bracket: the tensors UV and VU have the same cyclic symmetrization. It therefore annihilates Y, whereas cyclic invariance would make that symmetrization equal to 3Y. This is a contradiction. Hence if all quadratics vanish we may reject this factorization type; otherwise factor one of them over Q. There are at most two rational linear-factor directions to test. This reasoning works in every degree for a degree-one first factor; see `research/notes/N8-degree-one-factor-lemma.md`.

For each direction choose primitive integer z0. Decide the integer linear system [z0,Y0]=g in the degree-three Hall basis by Smith normal form. If solvable, lift z0,Y0 to a solution. Conversely any integral first vector on this line is k z0 for some nonzero integer k. A solution [k z0,Y]=g would give the integral solution [z0,kY]=g, so testing the primitive vector loses nothing. This finite list of integer systems decides type (1,3).

## Additional degree-four injectivity certificate

The preceding factorization argument is sufficient for the algorithm. The following stronger statement holds specifically in degree four and independently supports the implementation's nonzero-quadratic assertion. It must not be extrapolated to higher degrees: a degree-five rational kernel is recorded in `research/certificates/N8-degree5-outer-kernel.json`.

The natural linear map sends a degree-four tensor g to the coefficients

    g_ijkl + g_ljki.

Its restriction to L4 is injective over Q. It suffices to check the multilinear component on four distinct variables, by multihomogeneous decomposition and polarization in characteristic zero; the map commutes with substitutions and polarization. A multilinear Lie basis is

    [X_a,[X_b,[X_c,X_4]]],   (a,b,c) a permutation of (1,2,3),

in lexicographic permutation order. Selecting output coordinates

    (1,2,3,4), (1,2,4,3), (1,3,4,2),
    (2,1,3,4), (2,1,4,3), (3,1,2,4)

gives the matrix

    [ 1 -1  0  0  0  0 ]
    [-1 -2  0  0 -2 -1 ]
    [-2 -1 -2 -1  0  0 ]
    [ 0  0  1 -1  0  0 ]
    [ 0  0 -1 -2 -1 -2 ]
    [ 0  0  0  0  1 -1 ]

with determinant −54. Expansion of the displayed six brackets verifies the entries. The recorded calculation `results/n8-degree4-outermap-v1` independently generated this matrix and checked rank six. For diagonal outer slots the coefficient of t_i^2 is g_ijki rather than twice that coefficient, which does not affect injectivity in characteristic zero.

## Termination, coverage and evidence

First reject an element with nonzero abelianization, and accept the identity. For any remaining element, exactly one of the three leading-degree cases above applies. Every list considered is finite: index-d sublattices, divisors of a nonzero content, or rational linear factors of a nonzero quadratic. Rational and integer linear algebra and rational polynomial factorization terminate. Every accepted case constructs two elements whose commutator is g. The normalization and layer calculations show that every possible solution is represented in one of the tests. Thus rejection is also conclusive, proving the theorem.

The implementation is `scripts/n8_class4.py`; its deterministic checks and independently evaluated GAP witnesses are recorded under `results/n8-class4-*`. The displayed degree-four certificate is generated by `scripts/probe_n8_degree4.py`, with the recorded rank and determinant in `results/n8-degree4-outermap-v1`.

The prototype is not optimized for large integer inputs: it expands words and powers explicitly. This affects efficiency, not termination. The correctness claim rests on the proof, with computations used as supporting checks. Classes three and four are one growing partial answer to N8(b), not two entries or two separately named subparts. Classes five and above are not covered here.
