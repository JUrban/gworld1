# Audit of the nonlinear class-ten family

28 September 2026. Same-agent proof review with independent computational
representations; no external specialist review. This extends the existing
partial N8 candidate and does not change the entry tally.

## Scope and proof review

Re-read the archived N8 paragraph, its rendered screenshot, and the N8
background. Part (a) alone is starred. Part (b) asks about every finitely
generated free nilpotent group. The new theorem covers only the specified
nonlinear degree-eight family in class ten, with arbitrary two later
layers. The full question and all other uncovered class-ten targets remain
unanswered here. No result is inferred from the star or historical wording.

The proof checks separate five issues:

- Two distinct alphabet-weight types exclude both leading factors having
  degree at least two. Pure outer-square coefficients -15 and 20 prove
  the unique degree-one direction, including T with and without a part
  avoiding z. No rank-two argument is substituted for the all-rank proof.
- Polarization embeds Sym^2(L2) in L7. Rational recognition reduces to a
  linear system and symmetric rank-one test, not general quadratic
  solvability over Q. An arbitrary nonzero scalar permits either sign.
- The first kernel is exactly one line: the independent S,T,T seed
  component is not divisible by u+s+t. The explicit Jacobi identity
  supplies the surviving line in every rank.
- The AAAB coefficient after evaluation of the jets annihilates the last
  correction image but is 20 on the proposed obstruction.
- All signed integral scales and the full first-correction integral
  lattice are retained. The weight bound gives an actual quadratic final
  residual; at most two integral parameters remain before the final
  unsaturated lattice test.

Dependencies on the earlier exact Nielsen normalization and the
delta-stable homogeneous free basis are explicit in the proof. Those
structural lemmas still require specialist review with the rest of N8.

## Bounded checks and actual outcomes

`n8-class10-nonlinear-lead-v2` passed in 1.53 seconds. In rank two it
checks every possible leading weight type, finds a first correction
matrix of rank 30 with 31 columns, and shows that adding the proposed
quadratic obstruction raises the last matrix rank from 58 to 59. It
also uses separate untruncated associative-word arithmetic to verify
the formal derivative identity, the evaluation of V, the AAAB value,
and both pure-square coefficients used in the direction proof.

Version one failed after 1.37 seconds because the probe called the
unequal-weight helper with p=q=4. No mathematical assertion failed:
the equal-weight helper was then used for that case. The actual failed
logs and exact source are retained in its result directory. The two
versions are not counted as separate mathematical datasets.

`n8-class10-nonlinear-rank2-v1` passed in 32.33 seconds, with eight
records: three supported positives, two supported negative last-layer
perturbations, and three outside-scope controls. One positive has
nonprimitive leading scales and a negative scalar. The same-degree
outside control is itself a commutator in the earlier iterated-adjoint
family and correctly receives None, not False. The other outside controls
are identity and degree one. All supported first kernels have dimension
one; final polynomial coefficients are checked at additional parameters.

`n8-class10-nonlinear-rank2-gap-v1` passed in 6.09 seconds, using GAP's
independent nq representation. It checked three complete witnesses,
seven first-layer membership decisions, and seven polynomial certificates,
four of which have empty admissible parameter sets. Thirty-five sampled
group evaluations and all final correction columns were checked. The
negative target decisions rely on exhausting their signed leading
branches in the proof; the GAP replay checks the retained arithmetic and
group identities. Its success marker still says "class9 GAP" because it
reuses the verified generic checker; the fixtures, quotient construction
and run record explicitly use class ten.

`n8-class10-nonlinear-rank3-leading-v2` passed in 23.30 seconds. Two
positive recognition cases exercise a non-z two-form and a mixed
degree-one direction/form with negative scalar. Two outside controls
exercise a rank-two polarization matrix and a target with nonzero
metabelian leading image. This is leading-term recognition in a degree-eight
Lie truncation, not four class-ten group decisions or a rank-three GAP
replay. Version one passed the same two positive cases in 15.27 seconds;
its exact source is preserved and those repeated cases are not double-counted.

All successful runs had empty stderr. Each requested one core and at
most 8 GB per-process memory; no more than two ran simultaneously.
Commands, real return codes, wall times and stream hashes are in
`results/`. No timed-out or failed computation is represented as a pass.

## Novelty and reproducibility limits

A further bounded search for free-nilpotent single-commutator algorithms
and class-ten commutator equations located no matching family theorem.
Truss's primary 1995 abstract again distinguishes general class-three
unification from its restricted class-two positive result; that title
does not settle this class-ten family. This is not an exhaustive novelty
audit and no established new theorem is claimed.

All original source bytes and the original experiment clock are preserved.
The earlier shared arithmetic and GAP checker modules were not modified.
The manifest at `research/certificates/N8-class10-nonlinear/artifact-hashes.json`
identifies the proof, audit, new and shared code, and evidence files.
No subagent, author contact, outside review, push or new Kourovka import
was used. Current tally: four whole-entry candidates, two partial
candidates, zero established novel results.
