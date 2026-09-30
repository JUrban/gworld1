# N5 closing proof reread

30 September 2026, approximately 01:53--01:59 UTC. Same-agent review;
no independent mathematical referee or new novelty determination.

Read the complete current `problems/N5/proof.md` and
`problems/N5/integrality-audit.md`, after completing and checking the
class-two input supplement. The original N5 page, fragment and rendered
statement were also rechecked during this work period. The whole question
concerns all finitely generated nilpotent groups, including torsion;
the implemented class-two interface must not replace that scope.

The following implications were checked in the written argument:

1. The kernel of G/Z(G) -> R/Z(R) is exactly the finite torsion subgroup
   of G/Z(G). A characteristic torsion-free power subgroup of finite index
   gives a central power of each element central modulo T(G). Conversely,
   a central power has central image in the torsion-free quotient by unique
   roots. The commutator used in the forward direction lies in both the
   finite torsion subgroup and the torsion-free normal power subgroup.
2. For an actual decomposition G=A times B, rational uniqueness modulo
   the center gives the selected support partition. The full support
   preimage in G/Z(G) is Y_i S, hence [K_i:Y_i] <= |S|. The finite list
   includes finite groups, central factors and trivial quotient factors.
   It does not simply substitute one arbitrary rational lift for all lifts.
3. Full preimages of candidate quotient factors must commute. Central
   changes cannot alter cross commutators, so rejection at this stage is
   necessary. For commuting preimages, the relator defects change by
   exactly E_i z; the section criterion is the vanishing of these defects
   in Z/Z_i. Smith row and column operations remain valid with torsion.
4. Every direct splitting of the finitely generated abelian center is a
   finite torsion splitting and a torsion-valued shear of complementary
   free summands. Saturating exact constraints is necessary. Disjointness
   and primitivity of their sum are precisely the conditions for extending
   them to an integral direct splitting before congruences are imposed.
5. The integral stabilizer fixing the two exact summands pointwise acts
   transitively on splittings of each allowed remaining rank. The proof
   searches its finite image modulo the common modulus while retaining
   integral lifts. It does not replace integral splittings by arbitrary
   modular idempotents, which the explicit mixed-prime controls show would
   be wrong. Nontriviality is determined by the retained free rank and
   finite torsion factor, so it is not lost on passing to this finite image.
6. The constructed corrected lifts and central summands yield commuting
   factors with trivial intersection and full product. Termination uses
   finite enumeration and the explicitly imported effective nilpotent/
   rational-group operations. The full higher-class pipeline has not been
   implemented or computationally validated on arbitrary inputs.

No new logical gap was identified in these steps during this reread.
This conclusion is bounded by the review actually performed: the imported
rational decomposition uniqueness and effective Malcev algorithms were
not proved from scratch or given a fresh full primary-source proof audit
here. Their earlier source audits remain the evidence for those imports.
No successful mathematical suite was rerun merely for this note.

The new class-two interface has a separate sharp boundary: a computed
class-two quotient is identified with the input group only under its
explicit promise. Its native pcp input checks the class condition, but
the arbitrary-finite-presentation interface does not recognize it.
Positive original-generator factor words were verified through the
epimorphism; the promise is what makes that epimorphism an isomorphism.

The N5 whole-entry candidate and provisional novelty status remain as
before. This reread neither adds a result nor establishes novelty.
