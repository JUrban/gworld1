# N8(b): central targets in every free nilpotency class

Candidate argument, 28 September 2026. Scope: given a finite rank r, a class c, and g in the last lower-central term gamma_c of N=F_r/gamma_(c+1), decide whether g is a single commutator and produce factors on a positive answer. This is a partial scope of N8(b), not a solution of the entire entry. The proof uses Klyachko's classical Lie idempotent theorem, credited below. Novelty and independent review remain outstanding.

An [alternative finiteness proof and solver](projective-factor-audit.md),
added on 29 September, uses projective fibres and Shirshov--Witt instead
of the rotation lemma. It supplies a separate route to the same central
target decision statement, without the stronger two-direction bound.

Use [x,y]=x^-1 y^-1 x y. The associated graded Lie ring of F_r is the free integral Lie ring L on its generators, embedded in the free associative algebra T. Write L_j for its homogeneous component of degree j. Integral Hall bases and all the maps below are effective. The rank-one and class-one cases are immediate; g=1 always has the identity factors.

## 1. A rotation consequence of Klyachko's theorem

**Lemma.** If 0<s<n, the only homogeneous Lie tensor D in L_n over Q invariant under rotation of its n tensor positions by s places is zero.

Extend scalars to C and let epsilon be a primitive n-th root of unity. Use the position-permutation left action from Blessenohl–Laue, *Algebraic combinatorics related to the free Lie algebra*, pp.3–5. With tau_j=(j ... 1), their formula (9) and Klyachko's theorem give the Lie idempotent

    lambda_n = (1/n) product_(j=1)^n (1 + epsilon tau_j + ... + epsilon^(j-1) tau_j^(j-1)).

Products are in increasing j, so the j=n factor acts first. A Lie idempotent fixes every degree-n Lie tensor, including tensors with repeated letters; this extension from the multilinear component is explained on their p.4.

Let tau=tau_n and d=gcd(s,n)<n. If tau^s D=D, then tau^d D=D. Consequently

    sum_(i=0)^(n-1) epsilon^i tau^i D
      = sum_(a=0)^(d-1) epsilon^a tau^a D * sum_(b=0)^(n/d-1) epsilon^(bd)
      = 0.

The rightmost factor of lambda_n therefore kills D. But lambda_n D=D, so D=0. This proves the lemma. The direction of the chosen cyclic rotation does not matter.

Reference: [Blessenohl–Laue](https://www.mat.univie.ac.at/~slc/opapers/s29laue.pdf), archived as `literature/raw/N8-Laue-freeLie.pdf`; their reference [16] is A. A. Klyachko, *Lie elements in the tensor algebra*, Siberian Math. J. 15 (1974), 914–920. The displayed product on printed p.5 was also inspected visually. The rotation lemma is a deduction here from that prior theorem; no novelty claim is made for the Lie idempotent or its factorization.

## 2. Deciding homogeneous brackets with unequal weights

Fix p<q and a target W in L_(p+q). For every word J of length q-p form a commutative quadratic in variables T_I indexed by words I of length p:

    Q_J(T) = sum_(I,K) W_(I J K) T_I T_K.

Suppose W=[C,D]=CD-DC with C in L_p and D in L_q, both nonzero. Direct multiplication gives

    Q_J(T) = C(T) * (sum_K D_(J K) T_K - sum_I D_(I J) T_I),
    C(T) = sum_I C_I T_I.

If every Q_J vanished, the polynomial ring being a domain would imply D_(J K)=D_(K J) for every J,K. Thus D would be invariant under rotation by p places, contrary to Section 1. At least one Q_J is nonzero. This also proves that nonzero homogeneous Lie elements of different weights cannot commute, without an additional centralizer theorem.

Choose any nonzero Q_J and factor it over Q. It has at most two homogeneous rational linear factors up to nonzero scalar. Every possible C lies on one of these rational lines. Test each line for membership in L_p over Q, using a Hall basis; reject it if it fails. Otherwise clear denominators in its Hall coordinates and divide by their gcd to obtain a primitive integral element C_0. Every integral Lie element on this line is k C_0 for an integer k.

Now solve the integer linear system

    [C_0,D_0] = W,  D_0 in L_q,

using Smith normal form. This is sufficient: any decomposition C=k C_0, D yields D_0=kD, while an integral solution D_0 itself supplies the factors C_0,D_0. If all linear factors fail, there is no integral homogeneous bracket of type (p,q). If all Q_J vanish and W is nonzero, reject this type immediately.

All tensor dimensions are finite. No efficiency bound is claimed.

## 3. Equal weights

For p=q the map

    Lambda^2 L_p -> L_(2p),  C wedge D -> [C,D],

is injective over Q: embed L_p in T_p, split length-2p tensor words into their two length-p blocks, and identify the map with the injection C wedge D -> C tensor D - D tensor C. The same map is injective over Z.

Express W in the images of the exterior Hall basis by integer linear algebra. If no integral preimage exists, reject. Otherwise its alternating matrix A is uniquely determined. A nonzero integral exterior tensor is a single wedge if and only if rank_Q A=2. To see sufficiency, compute the primitive lattice P=(support_Q A) intersect L_p. In an oriented integral basis u,v of P the tensor is d u wedge v for a nonzero integer d; the factors d u,v realize it. This is exactly the lattice calculation used in the preceding low-class algorithms. It also shows that commuting equal-weight Lie elements are rationally dependent.

## 4. Reduction of central group targets

Let g be nontrivial and in gamma_c, and suppose [x,y]=g. Let p,q be the first nonzero lower-central weights of x,y. Neither factor is the identity.

If p=q and their leading Lie elements are dependent, write them aC,bC with C primitive integral. Elementary determinant-one operations on the pair (a,b) take it to (d,0), d=gcd(a,b). The exact group transformations (x,y)->(yx,y) and (x,y)->(x,xy), together with their inverses, realize these operations and preserve [x,y] exactly. The transformed factors have unequal first weights p<q. A factor cannot have become the identity, since g is nontrivial. If the initial pair had p>q, its leading bracket [C,D]=[-D,C] supplies the same target with the weights in increasing order, so considering p<=q loses nothing.

For unequal weights, Section 2 says their leading bracket is nonzero. For equal weights with independent leading terms, Section 3 says the same. Therefore p+q=c: a smaller sum would give a nonzero lower term of g, and a larger sum would give [x,y]=1. The central target's only nonzero Lie coordinate is thus a homogeneous integral bracket of one of the finitely many types p+q=c.

Conversely, if that coordinate is [C,D] with C in L_p, D in L_q and p+q=c, choose any group lifts x in gamma_p and y in gamma_q. Their commutator has this coordinate in gamma_c, and no higher terms survive in N. Hence [x,y]=g exactly.

Enumerate p=1,...,floor(c/2), put q=c-p, and apply Sections 2–3. Accept with the constructed group lifts if one type succeeds, otherwise reject. The preceding argument proves termination and both answers.

## 5. Verification and remaining scope

`scripts/n8_central.py` implements the homogeneous factor tests with exact rational factorization and integer Smith systems, then lifts factors to group words. `scripts/check_n8_central.py` passed 54 records in 4.08 seconds, with fixed seed 9282612. They include positive factors of every weight type in rank two/classes four through eight and rank three/class six, nonprimitive factors, two identity boundary cases, five independently justified negative targets, a negative equal-weight exterior-rank control, and eight comparisons with the separate class-five algorithm. All 35 positive witnesses (33 nonidentity and two identity witnesses) were independently evaluated in GAP's nilpotent quotients in 2.18 seconds. Certificates and exact commands are under `research/certificates/N8-central` and `results/n8-central-{checks-v1,gap-v1}`. The GAP check reuses the common witness evaluator; its marker retains the historical "N8 IA" name, while its input is explicitly the central-target fixture file.

The five negative targets, for c=4,...,8, have leading Lie tensor

    ad_a^(c-1)(b) - 2 ad_b^(c-1)(a).

Here ad_a(z)=[a,z]. An independent obstruction is visible in the metabelian Lie representation A=(s,1), B=(t,0), with bracket [(d,u),(e,v)]=(0,dv-eu) over Q[s,t]. Every element of the derived Lie algebra maps to (0,-tP). The target maps to (0,-t(s^(c-2)+2t^(c-2))). A bracket of two derived elements maps to zero; a bracket of a linear element alpha A+beta B with a higher-degree element would force the rational linear factor alpha s+beta t in s^(c-2)+2t^(c-2). No such factor exists: dehomogenization is Eisenstein at 2, and neither s nor t divides the homogeneous polynomial. This verifies the negative expectation without relying on the implementation's block-quadratic calculation.

Earlier bounded multilinear computations found full ranks 6/6 for degree four/shift two, 120/120 for degree six/shift two, and 120/120 for degree six/shift three modulo 1000003. They support only those finite checks; the arbitrary-degree assertion rests on the proof in Section 1. The archived primary source's formula was checked visually; targeted bibliography searches did not locate a matching all-class central-target theorem. This does not establish novelty.

Together with `independent-abelianization-proof.md`, this covers the nonzero-degree-two and last-central-layer target strata in arbitrary class. Intermediate target layers in higher classes remain unresolved here. No mathematics or code from Kourovka has been imported.
