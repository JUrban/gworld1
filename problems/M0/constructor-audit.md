# M0: constructing a witness from an input endomorphism

28 September 2026, approximately 15:58–16:05 UTC. This strengthens the
implementation evidence for the existing M0 candidate; it is not another
result or independent specialist review.

`scripts/m0_witness.py` takes signed-letter words for the images of a
finite free basis. Unlike the earlier specially constructed examples,
it computes the necessary abelianization normalization, finite field,
character, character normalization and primitive witness from the input.
It returns one of three explicit statuses:

- `nonautomorphism_certificate`: a free basis and its two-sided inverse,
  a finite-field character, and a zero Fox column for the image of the
  first basis word. This certifies a primitive element with nonprimitive
  image in the free metabelian group.
- `metabelian_automorphism`: an exact unit Laurent determinant after
  unimodular normalization. The mathematical implication invokes the
  prior Bachmuth criterion used in `proof.md`.
- `inconclusive_bound`: the prescribed finite-field or prime bound was
  exhausted. This is never interpreted as a positive answer. In the
  nonunimodular abelianization branch, nonautomorphy is already known,
  but a finite-field witness within the prescribed bound was not found.

## Construction

If the integer abelianization matrix B is not unimodular, find a small
prime p dividing det B (any prime when the determinant is zero). An
elementary-matrix reduction of a nonzero vector in ker(B mod p) gives an
actual integral unimodular lift, realized by Nielsen moves. Its first
basis word maps to an abelianization divisible by p; equivalently its
Fox column vanishes at the trivial character in F_p.

If B is unimodular, integer row operations construct an explicit free
automorphism beta for which beta o phi is IA. The determinant is
computed exactly in a sparse integer Laurent ring. If it is nonunit,
the program enumerates all nonzero-coordinate characters over fields
of increasing prime-power order up to the stated bound. Field models
use monic irreducible polynomials checked by SymPy, not an assumption
that every polynomial quotient is a field.

After a singular character is found, Euclidean column operations on
its discrete logarithms construct a Nielsen basis alpha with character
(1,...,1,t). The kernel and the proof's elementary transvections then
construct the witness. All basis changes retain explicit inverse words.

Finally the certificate is transferred from beta o phi to the original
input phi. The chain rule gives

    D(beta(phi(w)))(chi)
      = J_beta(chi) D(phi(w))(chi o beta).

Since J_beta is invertible, the original image column also vanishes at
chi o beta. The implementation directly evaluates that final column;
the certificate does not require a verifier to trust the normalization.

The main proof guarantees eventual discovery if the field bound is
increased without limit for a nonunit determinant. The distributed
prototype is explicitly bounded; it makes no complexity guarantee and
may produce large words. Rank zero is omitted from the input interface
and is the trivial case of the theorem.

## Checks and independent verification

`scripts/check_m0_witness.py`, seed **9282626**, tested 44 inputs in ranks
one through four. There were 29 negative witnesses, 13 exact unit
determinants, and two intentional bound-exhaustion controls. Twenty-four
inputs were randomized IA words with independently chosen domain and
range Nielsen changes. Nine controls were free automorphisms. The
remaining explicit inputs exercised rank one, singular or nonunimodular
abelianization, an extension-field root, and bounds.

The extension-field example has

    phi(x)=x z [x,z]^-3 z^-1,  phi(y)=y,  phi(z)=z,

where [x,z]=x z x^-1 z^-1. Its normalized determinant is
1-3XZ(1-Z). Modulo 3 it is one. Over F_2 its torus has only the
augmentation point. The first singular character found is in F_4;
the test asserts this and a bound of three deliberately remains
inconclusive. This exercises field selection as part of the algorithm.

The positive Python run `results/m0-constructor-v1/` took **0.72 seconds**
with one core and a 4GB per-process limit. Fields of orders 2,3,4 occurred
in the negative certificates; the longest witness-basis word had length
76. The Python constructor shares elementary word/field utilities with
the earlier M0 program, so those two programs are not independent.

`scripts/check_m0_witness_gap.g` supplies independent arithmetic and word
verification. It checks two-sided inverses of all supplied free bases,
evaluates the original image words by affine matrices over GAP finite
fields, and confirms all 29 zero image columns. For all 13 positive
cases it separately computes the normalized symbolic Fox determinant
over multivariate rational functions and compares its exact monomial
and coefficient. The successful run `results/m0-constructor-gap-v4/`
took **1.87 seconds**, one core/4GB, with empty stderr.

Three failed GAP runs are preserved, together with their exact checker
versions. Runs v1/v2 compared an integer constant with a polynomial
constant using GAP object equality; the diagnostic displayed actual=1
and expected=1 for rank-one inversion. Subtracting before `IsZero`
corrected that type distinction. Run v3 then encountered GAP's missing
generic inverse method for the mixed symbolic matrices. The final
checker builds their explicit affine inverses and multiplies them
directly. None of these failures was treated as a passing check merely
because GAP returned exit code zero; the recorded runner required the
success marker. The mathematical construction and Python certificates
were unchanged during those checker corrections.

Certificates are `research/certificates/M0-constructor/checks.json` and
`checks.g`. For a new input JSON array of generator-image words, use the
recorded runner around:

    .venv/bin/python scripts/m0_witness.py input.json --max-field-size 16

The checks substantiate these finite constructions and conventions.
They do not replace the universal proof or a novelty audit. The M0
scope and the total experiment candidate count are unchanged.
