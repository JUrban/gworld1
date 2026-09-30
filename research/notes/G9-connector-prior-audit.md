# G9: prior work on flow connections and geodesics

30 September 2026, approximately 08:50--08:54 UTC. This source check follows
the finite connector refinement; it changes credit, not the numeric bound.

A. Myasnikov, V. Roman'kov, A. Ushakov and A. Vershik,
[*The Word and Geodesic Problems in Free Solvable Groups*](https://arxiv.org/abs/0807.1032),
arXiv:0807.1032v1, Section 2.7, equation (6), Theorem 2.10 and Proposition
2.11, already describe the support-connection/Euler construction and its
minimum-forest formulation. Theorem 4.1 proves NP-completeness of bounded
geodesic length in nonabelian free metabelian groups. This is prior machinery,
not a new geodesic algorithm or complexity result from the experiment.

Read the introduction, Section 2.7 and its proof, and the statement/context
of Theorem 4.1. Actually viewed printed pages 15 and 16, retained in
`literature/figures/G9-MRUV-page-15.png` and `G9-MRUV-page-16.png`. Equation
(6) explicitly uses absolute flow coefficients; our implementation also
counts signed multiplicities by absolute value. No full independent audit
of the paper's complexity reduction was performed.

The archived PDF has 368017 bytes and SHA-256
`7cc29f5714bc3ed0a8d04e46ef492e4bb3068ebc002fffa9bc2c88cce860329b`.
Retrieval metadata and extracted text accompany it. The version identifier
is the 2008 v1 submission; a PDF compilation date is not treated as a new
publication or theorem date.

The experiment uses this construction on a specific finite list of strict
bridge flows, then recomputes its two-ended rational atom-cost series.
The full-flow GAP certificates independently verify the resulting words.
Neither their validity nor the bound depends on novelty of the connection
method. The current G9 argument now credits this additional predecessor.

Targeted searches included free-metabelian growth bounds, computable growth
in free metabelian/solvable groups, and recent growth-rate work. They returned
the already credited Arzhantseva--Guba--Guyot and Bodart--Osin papers, among
other subjects, and did not locate a matching stronger numeric bound or
replacement computability theorem in this bounded pass. This is not a
complete novelty clearance. The arXiv history confirms that the already
archived Bodart--Osin v3 is the April 2026 revision; no source was silently
replaced. No problem status, count or mathematical test changed.
