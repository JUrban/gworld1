# MA7 exterior-ring argument: audit and evidence

29 September 2026, approximately 07:22--07:31 UTC. Read with
`exterior-ring-proof.md`. This is an internal audit; no outside review.

## Source and interpretation

Read the complete original `sources/raw/probmat.html`, including MA7.
Actually viewed the new capture `research/statement-audits/MA7/statement.png`.
Its source SHA256 is
`f6a0eec50bb53695c25cd4c158901b7815de41fc332dc3b9be499028386ea808`.
There is no linked MA7 background paragraph in the frozen catalogue.

The literal question omits a lower dimension bound, commutativity of R,
and a nonscalar condition. The earlier ledger already compares it with
Kourovka 16.23, which adds n>2 and nonscalarity modulo every proper ideal.
Rechecked that wording in the public primary problem collection's indexed
text. A new local download of https://alglog.org/21tkt.pdf failed with an
expired-certificate error; no fresh visual inspection of that PDF is
claimed. No old experiment proof or computation was imported.

The construction uses n=3 and has an actual off-diagonal entry 1, so it
does not rely on the easy n=2 exception or a scalar reduction. Nevertheless
its ring is noncommutative. This remains explicit throughout; it does not
settle any version restricted to commutative rings. The ambient group for
“commutator” is GL_n(R), not a stable general linear group.

## Bibliography and reading limits

Dennis--Vaserstein (1988), Theorem 1 and the surrounding introduction were
read in the indexed extracted text of the author-listed ResearchGate
article. The theorem gives the C[x] example used in the proof's prior-scope
paragraph. The authors' institutional publication record independently
confirms the metadata and the unbounded-width result:
https://pure.psu.edu/en/publications/on-a-question-of-m-newman-on-the-number-of-commutators/ .
That institutional HTML is archived with retrieval metadata, SHA256
`0c1bfa1132dcf543f98f0a836276e9bdd2d7464640154a123a9c14f7336ab6bb`.

The publisher DOI and old author-host URLs failed in the web tool. Direct
publisher and ResearchGate downloads returned HTTP403. No local PDF of
Dennis--Vaserstein, visual inspection of its pages, or reading of its full
proof is claimed. The recorded prior consequence imports Theorem 1.
In particular the paper's existence alone is not used to assert the
additional nonscalar condition.

Downloaded and read Speyer's complete one-page Problem Set Five in
extracted text, particularly Problem 6 and its footnote. The PDF,
extraction and metadata are archived as `MA7-Speyer-exterior-exercise.*`;
PDF SHA256
`65217e8ac9cf6c468557bd064fb6833e514948136ec01f93f4cf8f1bc8ec4e3c`.
No visual inspection is claimed. This credits the familiar truncated
exterior-unit construction; it does not itself contain our GL_n quotient
argument. Failure of targeted searches to find that matrix argument is
not proof of novelty.

## Adversarial mathematical checks

- The degree-one coefficient span includes every entry of both proposed
  factors, even if their coefficients use every original basis vector.
  Its dimension is bounded by the number of entries, not by support size.
- Killing this span is an actual quotient of exterior algebras; its kernel
  on degree two is W wedge V. Merely deleting selected coordinate vectors
  would not suffice for arbitrary factors.
- The rank loss is at most **twice** dim W. We deliberately use 19 pairs
  for n=3, not 10 pairs; the latter naive dimension estimate would fail.
- Degree-two entries can have unrestricted support, but lie in a central
  square-zero ideal after the quotient. Thus they do not prevent use of
  a commutative coefficient subring.
- Inverses of the two quotient matrices are over that subring. The proof
  supplies the inverse formula rather than inferring this from ambient
  invertibility without justification.
- The ordinary determinant is applied only after this step. Applying it
  directly over the original noncommutative ring would be invalid.
- The elementary diagonal identity uses h(vu), not h(uv). Its second
  diagonal entry then cancels in the correct order.
- Multiplication by E_12(1) leaves the determinant obstruction intact
  after quotienting and makes the nonscalar condition hold for every
  proper ideal, without a classification of ideals.

No gap was found in this pass. All elementary ingredients are proved in
the note; specialist review and a full novelty/convention check remain.

## Computations

Python uses sparse ordered exterior monomials with coefficients modulo 3,
and explicit n-by-n matrix multiplication. GAP independently constructs
the 742-dimensional algebra from its structure constants and uses native
algebra and matrix multiplication. It does not import Python ring code.

Both verify the complete product of 343 elementary transvections and the
target's unit off-diagonal entry. Python also checks all 19 intermediate
unit-commutator and diagonal identities. GAP independently verifies the
rank-38 alternating matrix and seven quotient matrices. The latter have
kernel dimension 18; the projected bivector ranks are
2,20,20,18,20,20,18. The first attains the worst possible bound.

A boundary control has kernel dimension 19 and kills the bivector
entirely. This illustrates the strict dimension requirement rather than
being classified as a counterexample. The six other quotient matrices
use the fixed Python random seed 7292026, and are fully saved for replay.
These samples check arithmetic, not the universal quantifier over all
putative factors; that is established by the written rank/quotient proof.

| Recorded run | Actual outcome | Time |
| --- | --- | ---: |
| `ma7-exterior-v1` | exit 0; empty stderr | 0.320s |
| `ma7-exterior-gap-v1` | exit 0; empty stderr | 2.327s |

Each run reserves one CPU and 4GB. Raw logs and process hashes are in
`results/`; frozen scripts, fixtures, checks and their hash manifest are
in `research/certificates/MA7-exterior/`. There were no failed mathematical
runs. Download failures above are distinct from the completed computations.

Replay GAP with a fresh result name:

```sh
.venv/bin/python scripts/run_recorded.py --name ma7-exterior-replay --cores 1 --memory-gb 4 --timeout 120 --expect 'PASS MA7 GAP exterior' -- bin/gap -q --quitonbreak scripts/check_ma7_exterior_gap.g
```

The Python script accepts a fresh `--output` directory and refuses to
overwrite its checks. It does not enumerate the ring or its general
linear group.

## Counting

The short MA7 entry is a prior affirmative existence answer, excluded from discovery
counts. The explicit finite noncommutative construction is retained as an
additional research artifact, not a newly solved GroupWorld entry. Six
whole candidates, three partial candidates, zero established novel results
remain the correct tally. No claim about a commutative-ring strengthening
or any other whole problem is added.
