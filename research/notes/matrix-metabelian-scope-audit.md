# Matrix, metabelian and embedding scope audit

28 September 2026, approximately 13:47–14:01 UTC. No new candidate is
claimed in this pass. The four existing candidate entries are unchanged.

## MA5: connected linear groups are prior; finite extensions remain

The complete original `probmat.html`, the MA5 fragment and its rendered
paragraph were inspected. The question asks for a finite basis of the
identities of **any** linear group, without a connectedness hypothesis.

A. N. Krasil'nikov, *The identities of a group with nilpotent commutator
subgroup are finitely based*, Math. USSR-Izvestiya 37 (1991), 539–553,
Theorem 1, proves the result for groups with nilpotent derived subgroup.
The following corollary proves it for Zariski-connected linear groups.
The exact first page was read and inspected visually; it is retained at
`literature/figures/MA5-Krasilnikov-page539.png`. The English PDF and
extracted text are `literature/raw/MA5-Krasilnikov-im1041-en.*`.

The introduction also explains the relevant reduction: a linear group
satisfying a nontrivial identity is soluble-by-finite and is a finite
extension of a group with nilpotent derived subgroup. This does **not**
remove the finite extension from the problem. No closure theorem under
such extensions was established in this pass. Groups with no nontrivial
identity have the empty basis, so they are not the remaining difficulty.

Access record: an old MathNet hash URL returned a non-PDF response and
the archiver correctly refused it. The `what=fullt&option_lang=eng`
endpoint returned the Russian original, despite the language option;
these bytes are retained under the `-ru` key. The separate
`what=fullteng` endpoint successfully supplied the English translation.

## MA3 and MA6: special two-generator algorithms do not settle them

Chorna–Geller–Shpilrain, arXiv:1605.05226v4 (5 February 2017), is archived
as `literature/raw/MA3-Chorna-Geller-Shpilrain-1605.05226.*`. Theorem 4(c)
and its following algorithm concern the particular subgroup generated
by the two standard parabolic matrices with an **integer** parameter
k >= 2. The real-parameter peak-reduction assertion in Theorem 4(b)
has a different scope. Section 2 explicitly retains the general
SL2(Q) membership problem and the rational-parameter freeness question.

The full original matrix page and the MA3 rendering were inspected;
the latter includes both (a) SL3(Z) and (b) SL2(Q). Neither subpart is
resolved by this source. Its 2017 open-status statement is evidence of
scope at that date, not a certification of present openness.

For MA6, a suggested p-adic ping-pong argument was not developed into a
proof. For a rational unipotent parameter a and any fixed prime p,
the powers with exponents p^j have off-diagonal entry p^j a tending to
zero p-adically. Thus a proposed uniform displacement argument for all
nonzero powers cannot follow merely from |a|_p > 1. This is an obstacle
to that naive argument, not a proof of nonfreeness.

## MA1 and MA4: maintain previous scope cautions

The version caution for Knudson arXiv:0808.1239 remains in force:
the v1 elementary-generation assertion is absent from the v2 abstract.
No resolution is inferred from the earlier version. Likewise a theorem
of non-finite-presentability would not establish non-finite-generation.

For MA4, finite generation cannot be silently added to the question.
The familiar residual-finiteness obstruction for finitely generated
simple linear groups leaves the infinitely generated case. No
construction of a simple torsion-free linear group was obtained.

## M4: the primary announcement explicitly assumes finite rank

The original full metabelian page, M4 fragment, background and rendered
statement were inspected. The entry asks about **countably infinite**
rank in the variety of all metabelian groups.

Artamonov's 1977 announcement, Uspekhi Mat. Nauk 32:3(195), p.166,
Theorem 1, explicitly assumes finite rank. It states the positive
result for projective groups in A_m A, in particular A^2. The entire
one-page announcement was read and viewed; PDF, text and image are
retained under `M4-Artamonov-rm3198` and
`literature/figures/M4-Artamonov-page166.png`.

Its preceding paragraph also identifies the 1975 nonfree examples as
belonging to A A_n, a different variety. They do not answer M4.
The website background cites the longer 1978 proof. Access to its
volume/page URL was denied; that full proof has not been audited here.

An attempted passage from finite-rank projective groups to a countable
projective group has no established exhaustion by finite-rank
projective retracts. Closing a finite set of free generators under the
support of a retraction need not terminate in a finite set. Nor would
an arbitrary increasing union of free groups in a variety automatically
be free. No countable-rank conclusion is being asserted.

## M2, M3, S3 and FP9: unclosed reductions

- M2: infinite generation of a kernel of Aut(F_n) -> Aut(M_n), by
  itself, would not prove that Aut(M_n) is not finitely presented.
  Finite **normal** generation is the relevant issue for a quotient of
  a finitely presented group. Results about rank three or particular
  automorphism subgroups do not settle the requested rank > 3 group.
- M3: the existence of finitely presented solvable groups with
  undecidable word problem is not already a reduction to detecting
  metabelianity. In particular, triviality within the promised solvable
  class is detected by abelianization: a perfect solvable group is
  trivial. No suitable undecidability reduction was constructed.
- S3: the original background's positive result includes a restriction
  on proper powers modulo the derived terms. The scan located that
  same result, not a removal of its hypothesis. No solution is claimed
  from the abelian derived-length-one reading of the bare statement.
- FP9: the current Kourovka 5.16 annotation records the
  Baumslag–Cannonito–Miller 1977 theorem with **bounded** local linear
  degree. The original full proof was not obtained here. A countable
  universal-group observation and its missing effective step are
  written separately in `FP9-universal-tree-lead.md`; this is not a
  candidate answer.

Queries included the exact problem wording, “linear groups identities
finite basis”, “projective metabelian groups infinite”, “one-relator
solvable centre”, “locally linear finitely presented”, and “recognizing
metabelian solvable”. Searches and partial historical sources do not
certify current openness. No Kourovka-run proof or code was imported.
