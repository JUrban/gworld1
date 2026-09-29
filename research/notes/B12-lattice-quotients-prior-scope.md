# B12: prior hyperbolic quotients for 5 through 12 strands

29 September 2026. A consequence of established results, recorded as
prior coverage rather than a discovery candidate. The full range n>4
is not answered here: n>=13 remains outside this argument.

The complete frozen `sources/raw/probBr.html`, its B12 paragraph, and
`Back2.html#(B12)` were reread. The existing actual B12 paragraph capture
was viewed again. The question asks for non-elementary word-hyperbolic
quotients of B_n, not merely acylindrically hyperbolic quotients or
quotients of a finite-index subgroup. Its background records the familiar
B3/B4 examples but not the consequence below.

## 1. Quotients of the full braid group that are lattices

Curtis T. McMullen, [*Braid groups and Hodge theory*](https://people.math.harvard.edu/~ctm/papers/home/text/papers/bn/bn.pdf),
author version dated 25 April 2009, constructs representations

    rho_q : B_n -> U(r,s),       q=exp(-2 pi i k/d).

Table 9, printed page 32, supplies the following arithmetic ambient
lattices. Corollary 10.4 to Theorem 10.3 says that the **image** of B_n
is also a lattice when the signature is (1,s):

| n | k/d | Signature |
|---|---|---|
| 5 | 1/4 | (1,3) |
| 6 | 1/4 | (1,4) |
| 7 | 1/6 | (1,5) |
| 8 | 1/6 | (1,6) |
| 9 | 1/6 | (1,7) |
| 10 | 1/6 | (1,8) |
| 11 | 1/6 | (1,9) |
| 12 | 1/6 | (1,9) |

Thus for each n in this range there is an epimorphism from B_n onto
a finite-covolume discrete subgroup Gamma of U(1,s). Projecting to
PU(1,s) yields an epimorphism onto a complex-hyperbolic lattice Gamma_bar.
The compact central kernel of U(1,s)->PU(1,s) meets Gamma in a finite
group; projection through that compact kernel preserves discreteness and
finite covolume. In particular Gamma_bar is finitely generated and
non-elementary.

The n=12 row is deliberate. It is the sphere-moduli case also stated in
Theorem 10.1, not an extrapolation of the n<=11 plane-moduli cases.
There is no need to extend a quotient of P_n to B_n: the cited
representations are already defined on the full B_n.

## 2. From a lattice quotient to a word-hyperbolic quotient

A finite-volume complex-hyperbolic lattice is relatively hyperbolic
with respect to its maximal cusp subgroups. These subgroups are finitely
generated and virtually nilpotent, including when the lattice has torsion.
One can use its geometrically finite convergence action on the boundary;
passing to a torsion-free finite-index subgroup and then attempting to
extend a chosen quotient is neither needed nor asserted.

Every finitely generated virtually nilpotent group is residually finite.
It is therefore fully residually finite, by intersecting finitely many
finite-index normal subgroups, and hence fully residually hyperbolic,
since finite groups are hyperbolic.

Denis Osin, [*Peripheral fillings of relatively hyperbolic groups*](https://arxiv.org/abs/math/0510195v3),
Corollary 1.6, applies to a finitely generated group with such peripherals.
It has no torsion-free assumption. When the group is non-elementary and
the peripheral subgroups are proper, the corollary gives epimorphisms
onto non-elementary word-hyperbolic groups. These hypotheses hold for
Gamma_bar. In the cocompact case Gamma_bar is already word-hyperbolic.

Choose one such epimorphism Gamma_bar -> Q. The composition

    B_n -> Gamma_bar -> Q

is onto and Q is non-elementary word-hyperbolic. If a proper quotient
is desired, it is automatically proper: the infinite central full twist
of B_n has finite image in the finite centre of a non-elementary
hyperbolic group, so some nontrivial central power lies in the kernel.

This proves the affirmative answer for every 5<=n<=12, using prior
theorems. The cusp-filling step matters: a nonuniform complex-hyperbolic
lattice itself need not be word-hyperbolic.

## 3. Scope and audit limits

- This argument does not provide a quotient for n>=13. The absence of
  a suitable row of McMullen's table is not a nonexistence theorem for
  other representations or other quotients.
- It does not claim that B_n is fully residually hyperbolic: only the
  particular lattice quotient is used. The initial map may have a large
  kernel.
- It does not rely on residual finiteness of all hyperbolic groups.
- It gives existence, not an explicit finite presentation or a computed
  filling threshold for Q. No computational certificate of hyperbolicity
  was produced.
- This strengthens the earlier B12 scope note, which only checked why
  Mangioni--Sisto's selected four-strand quotients did not answer the
  higher-strand question. That earlier observation remains valid.

McMullen's introduction, Table 9 and its stated scope, Section 10 through
Theorem 10.7 and the adjacent discussion were read. Actual printed pages
32 and 46 were viewed and retained. Osin's Theorem 1.1, Corollaries
1.2 and 1.6--1.7, and the proof of Corollary 1.6 on pages 28--29 were
read; actual page 5 was viewed and retained. The latter proof preserves
two noncommensurable infinite-order elements, so non-elementarity is
not inferred merely from injectivity on a finite ball.

The full geometric/arithmetic and filling proofs were not independently
reproved. The standard relative-hyperbolicity and cusp facts for
finite-volume rank-one lattices are imported; Osin's introduction
also records the geometrically finite convergence-group formulation.
No separate specialist review or claim of novelty is made. Both primary
PDFs, derived text, metadata and page images are archived under B12 in
`literature/`. The discovery tally is unchanged.
