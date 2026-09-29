# F41 multipattern candidate: audit and reproduction

29 September 2026, approximately 00:39--00:58 UTC. Read with
[the proof](multipattern-proof.md). This is an internal audit, not an
independent specialist review or a certification of novelty.

## Statement and counting scope

Re-read the original F41 HTML fragment, its neighboring context and its
full background paragraph. Viewed the archived statement screenshot.
The earlier full-page statement audit is retained in `audit.md`.
The frozen free-group page SHA256 is
`2163a9d6e3c70b36c7df6943042f8b12896430b9e54d24dc23fba5160be4f04d`.

The claim concerns one fixed orbit under the entire automorphism group,
counting its elements of bounded free-basis word length. It does not
count the number of different orbits meeting a ball, or the iterates of
one automorphism. Puder--Wu Question 5.4 was re-read: the sharper
cyclic-orbit formula remains outside the claimed conclusion. The identity
exception and the distinction between ball limit and spherical limsup
remain explicit. No exception is used to manufacture an easy solution.

## Imported sources and actual reading

The following original PDFs, extracted text and retrieval metadata are
archived in `literature/raw/`. The source bytes are not modified.

| Source prefix | Precise dependency | PDF SHA256 |
| --- | --- | --- |
| `F41-KM-definable-1111.0577` | Definitions 5--6; Theorem 13 for one free variable | `ba3f8ccc3c4cddc591abfe5d34f2dbf10d27f4879f1f65ba6c01f2749b4a10da` |
| `F41-Pillay-genericity-0812.1692` | Definition of generic element on p6; Fact 1.10; Theorem 2.1(i) | `7e7c8ea68c3adc2f2aa69598889fc08b5223cdcf1f9627e244b923a1a1898e32` |
| `F41-Myasnikov-Romankov-verbal-2015` | Related prior verbal-value results; not required for Section 4 | `08892f0ecac37820fefdc3d503f20664628d02216b4c8e9b7e0f97b3a4836eef` |

For KM, read the introduction, Definitions 5--6, Theorems 7, 12--13,
the proof of Theorem 13 and its Lemma 14, and Definitions 15/19 with
Proposition 16, Lemma 17 and Proposition 20. Viewed printed pages 3 and
9. Its deep quantifier-elimination/NTQ dependencies are imported; this
pass does not independently establish them. The downloaded arXiv PDF
identifies v5, dated 3 December 2012, despite a later compilation date in
its running header. The published reference is IJAC 23 (2013), 91--110.

For Pillay, read the generic-element and connectedness definitions,
Fact 1.10, Theorem 2.1 and its proof, including its free-factor step.
Viewed printed pages 6 and 7. The cited Sela/Perin theorems and the
underlying stability theory are not independently re-proved here.
The crucial generic type is **over the empty parameter set**.

Read all four pages of the Myasnikov--Roman'kov paper in extracted text;
no visual inspection of that PDF is claimed. Its page range is 399--402,
as printed in the PDF. Its cancellation-scheme discussion and density
estimate motivated this investigation. The current proof uses KM's
precise piece condition, and does not rely on the informal assertion
that all pieces appear twice in one output expression. Direct browser
PDF access failed and a ResearchGate download returned HTTP403; the
publisher PDF was successfully obtained through the local downloader.

Images actually viewed are saved under
`research/statement-audits/F41-multipattern/` and the existing
`research/statement-audits/F41/statement.png`.

## Adversarial checks on the argument

1. KM requires each first-pattern variable to be a piece, rather than
   two occurrences of that variable in the first pattern. The proof
   explicitly chooses another occurrence anywhere in the output.
2. Split the first pattern into its fixed number of variable occurrences.
   Treat their lengths independently for an upper bound. Ignoring
   equality between two formal copies of a variable only enlarges the
   set being counted. No unbounded number of blocks is introduced.
3. A block that is a piece has an occurrence distinct from its displayed
   occurrence: of the two witnesses to being a piece, at least one is
   distinct from the displayed one. Inverting a piece preserves this
   property. This handles negative occurrences in the pattern.
4. Same-orientation repeats at different starts equate different
   positions even when they overlap. Inverse repeats either do the
   same or force a forbidden self-inverse letter. Odd signed cycles
   are likewise impossible. All nonconstant singleton components are
   therefore excluded in a realizable scheme.
5. Constants contribute at most C singleton components. They cannot
   contribute a growing free segment, since coefficients are fixed
   elements and the parametrization is noncancelling.
6. The quotient of the position path is connected. Tree edges always
   join different equality components and exclude one color, with the
   appropriate signs. Extra edges, loops and fixed coefficient values
   can only reduce the number of assignments. This is why the base is
   2r-1, not the weaker 2r.
7. Piece coverage is essential. A set with only one short repeated piece
   may have full exponential growth; the negative control below exhibits
   this. KM's weaker negligible-set condition alone is not substituted
   for the stronger first-pattern hypothesis.
8. The formula phi separating w from the generic type has no parameters,
   so its complement contains every automorphic image of w. A formula
   with the basis named as parameters would not justify that assertion.
9. It is the **complement** of the orbit-containing set that contains
   a realization of the generic type, and is therefore generic. The
   growth bound forbids the complement from being a sub-multipattern;
   the KM dichotomy then selects the required side. This avoids assuming
   the primitive set or the orbit itself is definable.
10. Constants and polynomial degrees depend on w. No uniform bound over
    the union of all nonprimitive orbits is claimed. That union need
    not have the same exponential rate as each individual orbit.
11. The lower bound uses distinct reduced prefixes in conjugates, not
    an unjustified assertion that arbitrary conjugators give different
    elements. Nontriviality and parity are handled explicitly.

No gap was found in this bounded audit of the new argument. The strongest
remaining review concern is the use of the exact full KM parametrization
theorem together with the quantitative lemma, not the finite sample size.

## Finite checks and their limits

The Python script enumerates all reduced rank-two words of lengths 1--7.
For each length it enumerates all partitions into 1--3 nonempty variable
blocks, with either no coefficient or one fixed initial coefficient,
and every second start/orientation for each block. This yields **46,536
positional schemes**. Whole-word enumeration supplies exact solution
masks independently of the signed-graph component calculation. All
component-size, quotient-connectivity and tree-count bounds pass.

The implementation includes inverse repeats, overlaps, inconsistent
signed schemes and consistent schemes with no reduced solution. It
does not claim to exhaust all lengths, alphabets, numbers of blocks or
coefficient placements. Those are covered by the written proof, not
by extrapolation from the test.

A separate GAP program enumerates elements of the rank-two free group
by multiplication and reduced length. It checks **77 representative
positional schemes**, selected to cover the observed combinations of
length, coefficient presence, overlap, inverse orientation, signed
consistency and actual nonemptiness. All exact counts agree. It does
not reuse the Python signed-graph routine.

Negative control: there are exactly 2,187 length-nine reduced rank-two
words ending in `aa`, exceeding 4*3^4. Repetition of this suffix does not
cover the other positions, and the half-length conclusion is correctly
not applied.

Recorded runs, each with one CPU and a 4GB per-process limit:

| Run | Outcome | Runtime |
| --- | --- | ---: |
| `f41-piece-covers-v1` | PASS; empty stderr | 0.872s |
| `f41-piece-covers-gap-v1` | PASS counts; one GAP global-scope syntax warning | 1.877s |
| `f41-piece-covers-gap-v2` | PASS; empty stderr | 1.875s |

The warning was caused by an anonymous function referring to the global
letter-list variable before it had been bound at parse time. Replacing
it with an explicit coefficient loop removed the warning. The exact
v1 source and both logs are retained; no failed count or exception is
concealed. No test here constructs the separating formula or verifies
the imported model-theoretic theorems.

To replay the GAP checks against the saved fixtures, use a fresh run name:

```sh
python3 scripts/run_recorded.py --name f41-piece-replay --cores 1 --memory-gb 4 --timeout 120 --expect 'PASS F41 GAP piece covers' -- bin/gap -q --quitonbreak scripts/check_f41_piece_covers_gap.g
```

The Python generator refuses to overwrite `checks.json`; regenerate in
a disposable checkout after moving its generated `checks.json` and
`fixtures.g` aside, retaining the originals for comparison. Its exact
command is in `results/f41-piece-covers-v1/process.json`. Frozen scripts,
checks, fixtures and a hash manifest are retained in the certificate
directory. Do not rerun merely to increase sample volume.

## Prior scope and counting decision

Bounded searches included the combinations “automorphic orbit generic
type”, “nonprimitive growth definable”, “multipattern orbit free”,
“automorphic multipattern”, and the exact KM and Pillay titles. No
matching full orbit theorem was located. Several exact-phrase searches
returned irrelevant results; this is a limitation, not positive novelty
evidence. The existing Shpilrain survey and Puder--Wu source checks are
retained; no claim is made that the survey exhausts current literature.

The old rank-two, proper-power and Puder-threshold scopes remain prior.
The nonprimitive-abelianization route through proper verbal-value sets
also has substantial prior ingredients. The proposed full conclusion
is a short consequence of deep published work and may be known to
specialists. **Zero established novel results** remains the correct
experiment-wide count.

Promote the one existing F41 entry from a partial to a whole intended-
scope candidate, preserving its historical partial record. The candidate
tally becomes **5 whole entries and 3 partial entries**, eight entries
total. The literal identity exception remains explicit. No additional
count is assigned to the counting lemma, source readings or finite tests.

Follow-up: see `followup-audit.md` for the later parameter/uniformity
check. It changes neither the candidate scope nor the counting decision.
