# N5: finite-presentation input and explicit factor words in class two

30 September 2026, within the original 48-hour experiment. The
[mixed coordinate solver](class2-mixed-audit.md) now has an input interface
for arbitrary finite presentations **promised to define a group of
nilpotency class at most two**. Positive answers return generating words
for both factors in the original presentation. Higher nilpotency classes
remain outside the implementation. This is an implementation extension
of the existing N5 candidate, not an additional solution or novelty claim.

## Conversion and its mathematical scope

`scripts/n5_class2_input.g` provides two interfaces:

- `N5ClassTwoCoordinates(G)` takes a native GAP polycyclic group. It
  computes its full center Z and rejects unless G' is contained in Z.
  It obtains independent cyclic bases of Z and G/Z using `Pcp(...,"snf")`,
  moves infinite coordinates first, and reads the actual commutators and
  finite quotient power relations in the central basis.
- `N5FpClassTwo(P,true)` takes a finite presentation under the explicit
  class-two promise. GAP/nq computes its class-two quotient, which is
  isomorphic to P precisely because gamma_3(P)=1 is assumed. Computing
  that quotient is **not a recognition test** for the promise. Passing
  `false` returns `fail` before this computation.

The conversion uses the documented [Polycyclic subfactor routines](https://gap-packages.github.io/polycyclic/doc/chap5.html#X7DD931697DD93169)
and [nq epimorphism construction](https://gap-packages.github.io/nq/doc/chap3.html#X8758F663782AE655).
Their exact algorithms are imported software dependencies, not newly
proved algorithms in this experiment. The installed implementations of
the Smith-basis and exponent routines were read; the documentation was
also checked online.

There are two elementary boundary cases. A presentation with zero
generators defines the trivial group and is handled directly. Otherwise
the interface first computes the abelianization. If it is cyclic, a
class-two group with that abelianization is cyclic: every generator is
a power of one lift times an element of the central derived subgroup,
so all generators commute. The abelianization map is then already an
isomorphism under the promise. This also avoids the installed nq's
previously recorded assertion failure when asking for class two on
cyclic inputs. Noncyclic abelianization uses the class-two quotient.

For an element g of the native group, first compute its quotient
coordinates u. If x^u denotes the ordered word in the chosen quotient
lifts, then (x^u)^-1 g lies in Z and has central coordinates z. The
interface returns (u,z), and checks x^u z=g. Central membership is checked
before invoking the exponent routine; this matters because its installed
source warns that out-of-subgroup inputs need not return a reliable
failure. These bases supply exactly the full-center normal form required
by the mixed solver, with all finite powers retained.

Apply the existing complete coordinate algorithm. On success, decode
its factor generators in the native group and verify nontriviality,
commutation, trivial intersection, and generation of the whole group.
Then use the recorded epimorphism to obtain preimage words in P and
check their images individually. Under the class-two promise this map
is an isomorphism, so these words generate the claimed direct factors
of the original group. The universal negative direction still depends
on the written N5 proof and its mixed-center algorithm; testing positive
factor words alone does not establish it.

## Standalone use

`scripts/n5_class2_fp.py` accepts JSON with a nonnegative integer
`generators` and a list `relators`. Each relator is an even-length list
`[i,e,j,f,...]`, denoting x_i^e x_j^f ..., with one-based indices and
integer exponents. Inputs are validated as data, not executed as GAP
source. Extra metadata fields do not affect the presentation.

For example, this fully recorded command uses the retained three-generator
presentation of H_3 times C_2, with the two triple commutators, the order-two
relation, and the two centrality relations:

```sh
python3 scripts/run_recorded.py --name n5-fp-fresh-example \
  --cores 1 --memory-gb 8 --timeout 180 --expect 'PASS N5 fp command' -- \
  .venv/bin/python scripts/n5_class2_fp.py \
  --input research/certificates/N5-class2-input/standalone-inputs/H3_C2_two_step.json \
  --assume-class-at-most-two \
  --output research/certificates/N5-class2-input/fresh-example
```

Use fresh job/output names. The command retains the normalized input,
extracted coordinates, all solver branches, GAP source and output, and
`answer.json`. A true answer includes factor words in the same indexed
format as the input relators. A false answer has an empty factor list.
The required flag states a hypothesis; it does not certify it. A
presentation of higher class can have a quite different class-two
quotient. There is no assertion about the original group in that case.
No practical complexity or resource sufficiency bound is claimed.

## Verification and remaining limits

The test driver starts from all twenty earlier mixed-coordinate groups,
but presents them as ordinary finitely presented groups and recomputes
the center and quotient bases. Six variants change generators and add
a redundant generator with its defining relation; an infinite cyclic
presentation is also added. These give 27 presentations. The zero-generator
trivial presentation and a one-generator redundant presentation of the
trivial group both occur.

GAP exports ten deterministic pairs of words per presentation. Python
checks 810 native-versus-coordinate product, inverse and signed-power
identities, and evaluates all 251 original relators as the identity.
The coordinate solver gives the expected answer in all 27 cases. A fresh
GAP process reconstructs the original presentations, checks exact input
binding, verifies all twelve positive direct decompositions, and writes
their factor words in the original generators. Twelve here counts
decompositions, each consisting of two factors. The log's label
`positive factors` refers to this count of successful decompositions.

The separate public command then passes three additional input formats:
H_3 times C_2 without a named central commutator generator; G_2 on its two
original generators with central commutator of order two; and C_6 on two
generators with a redundant defining relation. It returns true, false,
and true respectively. The G_2 negative proof remains in the original
N5 audit. These are command/interface checks, not additional families
of mathematical results. Native class-three input and fp input without
the promise are explicit rejection controls.

The new tests do not independently reimplement nq, prove that an
arbitrary supplied presentation satisfies the promise, or reimplement
every mixed central-splitting rejection in GAP. The prior negative
fixtures and their proofs retain the exact limitations stated in the
mixed-coordinate audit. There has been no independent specialist review.

## Recorded failures, resources and source fidelity

Eight bounded jobs are retained. The first export failed at the
zero-generator nq epimorphism with a generator/image-list mismatch, and
also emitted an unbound-global syntax warning. Version two handles the
zero-generator group directly, binds the later replay variable, and fixes
an inspected redundant-word construction. It completes the mathematical
conversions but fails while sorting the immutable list returned by
`RecNames` during JSON export. Version three copies that list before
sorting and passes in 2.33 seconds. Both failed jobs have GAP exit zero
but missing completion markers; the recorded runner correctly marks them
unsuccessful. Their sources and stderr are preserved, as is version two's
empty output file.

The Python check passes in 1.67 seconds; GAP reconstruction and factor-word
replay pass in 2.18 seconds. The three standalone commands pass in
4.08, 4.64 and 4.53 seconds. All successful stderr logs are empty. Each
job reserves one CPU and 8 GB; only the last two commands overlap, using
two CPU slots and 16 GB in reservations. The usual per-process/aggregate
memory distinction of the runner still applies. All processes are terminal.

The full original nilpotent-problems HTML and the exact N5 fragment were
reread, and the retained rendered statement was actually viewed again.
The problem is not restricted to class two: the general candidate remains
a written argument, while this supplement describes the now executable
class-two specialization. Source, process and artifact hashes are bound
in `research/certificates/N5-class2-input/manifest-v1.json`. The original
deadline and the ten-whole-entry/two-partial/zero-established-novel tally
are unchanged. Nothing was pushed or sent to another person.
