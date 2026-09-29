# F38 — Free groups

[Offline statement](statement.html) · [Complete archived page](../../sources/raw/probfree.html) · [Publisher](https://shpilrain.ccny.cuny.edu/gworld/problems/probfree.html)

Source begins at line 275; byte range [13587, 14646). The raw fragment is stored in `source-fragment.html`.

Heading star: False. Starred subparts: b. Hall of Fame entries: 1. Linked background sections indexed: 1.

Parts (a) and (c) now have candidate decision arguments in every finite rank: [part (a) proof](part-a-proof.md), [part (a) audit](part-a-audit.md), [part (c) proof](bounded-proof.md), and [part (c) audit](bounded-audit.md). Part (b) and the rank-two decisions are prior. The new part (c) argument proves that bounded equivalence is equivalent to commensurability of conjugacy stabilizers, importing Sela's graded shortening theorem. The implemented finite decision procedure has independent GAP checks, including reconstruction of complete Whitehead graphs. Specialist correctness and novelty review remain pending. Earlier necessary-condition and restricted positive-case notes are preserved as historical stages. The machine-readable source evidence is in `data/problems.json`; the extracted text below is a search aid, not an authoritative transcription.

```text
(F38) (I.Kapovich, P.Schupp)
(a) Is there an algorithm which, when given two elements u, v
of a free group F_n decides whether or not the cyclic length
of f(u) equals the cyclic length of f(v) for every automorphism
f of the group F_n?
*(b) Call elements with the property alluded to in part
(a)
translation equivalent,
to simplify the language. Is it true that whenever g is translation equivalent to h in F_n
and w(x,y) \in F(x,y) is arbitrary, one has w(g,h) translation equivalent to w(h,g) in F_n?
(c) We say that u is boundedly
translation equivalent to v if the ratio of the cyclic lengths
of f(u) and f(v) is bounded away from 0 and from \infty.
Is there an algorithm which, when given two elements in a finitely
generated free group, decides whether or not they are boundedly translation
equivalent?
Background
```
