# Equations and algorithmic scope checks

28 September 2026, approximately 14:48–15:05 UTC. This pass also
re-read the complete candidate proofs for F28, N5 and M0. No gap was
identified in that internal pass; this is not independent specialist
validation and adds no new experimental check to those candidates.

## E5: prior full positive answer

Sela, *Diophantine Geometry over Groups X: The Elementary Theory of
Free Products of Groups*, [arXiv:1012.0044](https://arxiv.org/abs/1012.0044),
Theorem 9.1, gives precisely the positive answer. The archived full
source is `literature/raw/E5-Sela-1012.0044.pdf`; SHA-256
`485122a663977ca9bf688e7e2d28331c30ed1b8fcd0bf190c81d57b368891e7a`.

Read section 9, printed pages 138–142, including the continuation
after the coefficient-free argument. This matters: the original
problem does not assume finite generation. Sela explicitly treats
systems with coefficients, first for countable factors and then
arbitrary factors. Thus this is not merely a coefficient-free or
finitely generated answer. The Makanin–Razborov machinery invoked
earlier in the paper has not been independently re-proved here.
E5 is excluded from new-result counts.

## H12: prior positive answer, including torsion

Groves–Hull, *Homomorphisms to acylindrically hyperbolic groups I:
Equationally noetherian groups and families*,
[arXiv:1704.03491](https://arxiv.org/abs/1704.03491), Theorem D,
proves the relative-hyperbolic statement with equationally Noetherian
peripheral groups. In particular it applies to every hyperbolic
group, with trivial peripheral group. The text also credits the
earlier general hyperbolic result to Reinfeldt–Weidmann, extending
Sela's torsion-free theorem. No torsion-free restriction is imposed
in Theorem D.

Archived full source SHA-256
`7793b46db0919a6b3db96793cc2946c8122146454552121c303ee1b8c2233cfa`.
Read the introduction, Definition 3.1 and the distinction between
coefficient systems and families. Hyperbolic groups are finitely
generated, so coefficient-free Noetherianity also supplies the
coefficient version: replace a fixed finite generating set appearing
in all coefficient words by finitely many additional variables, take
a finite subsystem, and specialize those variables back. This step
does not assume a uniform finite set of coefficients in the original
system. The full shortening-argument proof was not audited. H12 is
excluded as a prior answer.

## A6: a prior restricted impossibility is not the full answer

Chiodo, *Finding non-trivial elements and splittings in groups*,
[arXiv:1002.2786v3](https://arxiv.org/abs/1002.2786v3), Theorem 4.2,
rules out algorithms whose output has any fixed bounded length.
It does not rule out an algorithm producing an arbitrary word.
The introduction explicitly retains this latter question and
explains why ordinary undecidability of triviality is insufficient.
The full primary text is archived; SHA-256
`a9a0fed290d8bcad20d2cbfd734cd2816cbdffda832d99ace568f99dd6fb40ab`.
Read the abstract, introduction, motivating question and theorem
statement. No full A6 resolution is inferred.

The original complete equation, hyperbolic and algorithmic pages,
exact E5/H12/A6 fragments, and all three rendered paragraphs were
inspected. Their evidence is in `research/statement-audits/`.

Further targeted searches for solvable S4–S8, normal roots F27 and
automorphic subgroup-orbit F39 did not supply a new full answer.
In particular, Silva–Weil's primary
[2010 abstract](https://doi.org/10.1142/S0218196710005790) treats rank
two fully and almost-bounded automorphisms in larger rank; it does
not settle arbitrary-rank F39(a). No claim of exhaustive current
openness follows from this search. No Kourovka mathematics/code was
imported, and no new candidate count results from this scope pass.
