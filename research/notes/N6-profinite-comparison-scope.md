# N6: profinite comparison does not compute the genus

29 September 2026. Bibliographic scope update; **no solution claim**.

The frozen N6 asks for a description of the finitely generated
class-two nilpotent groups of genus one. Its short wording leaves
the comparison class unstated. We retain the usual finitely generated
nilpotent/residually finite interpretation used in the literature;
we do not count a counterexample obtained by appending an unrelated
group without finite quotients to a candidate comparison group.

Dan Segal, [*Polycyclic groups and profinite isomorphism*](https://arxiv.org/abs/2605.28310),
arXiv:2605.28310v2, revised 28 May 2026, proves in Theorem 3 that the
profinite isomorphism problem is decidable for virtually polycyclic
groups. The input is two finite presentations with that promise.
Thus the theorem applies in particular to finitely generated
nilpotent groups, including those with torsion. The source credits
the torsion-free nilpotent case to earlier work in its reference GS3,
Grunewald–Segal (1984).

Crucially, the paragraph immediately following Theorem 3 says that
no procedure is known to compute the cardinality of the profinite
genus of a polycyclic group from the available comparison theorems.
Theorem 2 supplies finiteness, which is different from an effective
bound or a stopping rule for enumerating all genus representatives.

For example, isomorphism and profinite-isomorphism decisions allow
one to enumerate further nonisomorphic groups in a given genus.
Even when that genus is finite, the enumeration gives no certificate
that no further representative remains. In particular it does not
certify that the genus has cardinality one. This is a limitation of
that inference, not a proof that a genus-one algorithm cannot exist.

We read the introduction and beginning of Section 2, including the
exact hypotheses and class-number discussion. Actual PDF p.2 was
viewed and retained in `literature/figures/N6-Segal-page2.png`. The
full proof of the new virtually polycyclic theorem was not audited.
The raw PDF, extracted text and retrieval/SHA-256 metadata are under
`literature/raw/N6-Segal-profinite-2605.28310.*`.

Neither this source nor the earlier low-Hirsch-length classifications
provides the requested unrestricted description here. N6 remains
unresolved in this experiment, with no additional candidate count.

The full frozen nilpotent-groups HTML and exact N6 fragment were read.
The original paragraph was rendered and actually viewed on 29 September;
`research/statement-audits/N6/` retains the screenshot, full-page PDF and
metadata. The statement does not specify the comparison class; that
qualification above is an interpretation, not a change to the source.
Source and audit hashes are in
`research/certificates/N6-profinite-comparison/manifest.json`.
