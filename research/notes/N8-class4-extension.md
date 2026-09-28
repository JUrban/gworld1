# N8(b): proposed extension to class four

Recorded 28 September 2026, approximately 10:40 UTC. **Extension lead; not yet added to the claim's verified scope.** Builds on the class-three candidate in this repository, with no imported Kourovka argument.

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

Thus the linear form with coefficient vector z divides every nonzero q_jk. At least one q_jk is nonzero for every nonzero degree-four Lie element, by the injectivity certificate below. Factor one such quadratic over Q; there are at most two rational linear-factor directions to test.

For each direction choose primitive integer z0. Solve [z0,Y0]=g in the degree-three Hall basis over Q. This map is injective: after a rational change of generators z0 is X1, and a homogeneous associative polynomial of degree three commuting with X1 must be a multiple of X1^3, which has zero intersection with the degree-three free Lie space. The coefficients of Y0 must be integers. If so lift z0,Y0 to a solution. If not, no scaling z=k z0 can help, since it replaces Y0 by Y0/k. This gives a finite decision procedure for type (1,3).

## Injectivity certificate for the symmetrized outer slots

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

## Remaining checks

- Turn the case analysis into a complete proof with all lift/correction identities and integrality conditions explicit.
- Implement the four cases with exact arithmetic and compare returned witnesses in GAP's class-four quotient.
- Check known negative examples and construct cases that exercise each branch.
- Search specifically for prior class-four commutator decision results; retain provisional novelty.
- Do not count class three and class four as separate problem entries or named subparts.
