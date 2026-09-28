# Internal audit of the class-six extension

28 September 2026. No external specialist review has occurred. The
extension is one further parameter range of the existing N8(b) partial
candidate, not an additional solved entry.

## Proof checks

The only new target layers are first nonzero degree three and four.
The other layers use previously recorded algorithms. The original N8
source and rendered statement audit remains at
`research/statement-audits/N8/`; no claim about all classes is made.

The main new injection `L2 tensor L3 -> L5` has an explicit proof using
position permutations, not a dimension estimate or a few sampled pairs.
The separate degree-four metabelian kernel calculation gives both an
inclusion and equality of dimensions, with surjectivity onto the complete
polynomial syzygy space proved by induction. The subsequent three
correction lemmas use the tensor injection and independence of a pure
tensor from the alternating subspace. They apply over Q; integrality is
still decided separately by Smith normal form.

The degree-three branch retains all signed leading-factor scales and all
integer residues under the exact move `(x,y)->(yx,y)`. The period is
nonzero because the second leading term is nonzero. Degree-five kernels
then vanish, making that correction unique. Every lift is an actual group
element and its complete commutator is recomputed before the next step.
In particular, higher terms changed by the finite normalization are not
silently fixed or discarded.

A concrete nonzero correction kernel in weights (1,4) is preserved as a
negative control against overgeneralization. Its two corrections have a
nonzero cross bracket in degree seven. None of the class-six proof relies
on its kernel being zero.

## Verification evidence

All three recorded jobs used one CPU slot, a 4 GB process limit and a
180-second timeout. All completed with zero return code, expected marker
and empty stderr; logs and hashes were inspected.

- `n8-class6-kernels-v1`: 44 exact records, 11.61 seconds, seed 9282619.
  The full (2,3) tensor bracket matrices are injective in ranks two,
  three and four; the three correction lemmas were checked on 40
  parameter choices. The final record gives the nonzero higher-degree
  kernel and its nonzero degree-seven cross term in Hall coordinates.
- `n8-class6-checks-v1`: 63 group-target records, 11.31 seconds, seed
  9282620. These include 32 constructed positives over ranks two and
  three and all normalized weight types, 24 independently chosen
  middle-layer perturbations (19 negative, five positive), two negative
  class-five-quotient controls, four identity/abelian boundaries and
  one degree-two dispatcher check. There are 40 positive answers in
  total. Nontrivial normalization periods three and six occur; a
  successful branch requires residue one modulo three.
- `n8-class6-gap-v1`: 8.85 seconds. GAP/nq independently evaluated all
  40 positive word witnesses in class six. It also checked all 133 new
  lifting steps, including 76 negative answers. Each step is evaluated
  in the quotient of class equal to the degree being matched. The
  checker verifies that the residual and correction commutators are
  central, then decides membership in their generated subgroup using
  GAP's polycyclic algorithms. It does not use the Python tensor
  coordinates or integer solver.

Sources and compact certificates are under `scripts/` and
`research/certificates/N8-class6/`. No failed run occurred and no
computation is presented as a proof of the arbitrary-rank theorem.

## Literature and provenance

Targeted searches for class-six and free-nilpotent commutator decision
algorithms found no matching theorem. The archived Roman'kov survey's
class-two and general-equation results remain distinct. Search extraction
can render the symbol “at most” as a numeral six; such snippets are not
treated as a class-six theorem. Novelty remains provisional.

Hall/Witt theory, integral normal forms, and the preceding N8 candidate
lemmas are explicit dependencies. No Kourovka mathematics or code was
imported. A general zero-kernel statement for all weights is false,
as the retained higher-degree control demonstrates.
