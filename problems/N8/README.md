# N8 — Nilpotent groups

[Offline statement](statement.html) · [Complete archived page](../../sources/raw/probnil.html) · [Publisher](https://shpilrain.ccny.cuny.edu/gworld/problems/probnil.html)

Source begins at line 42; byte range [1669, 2038). The raw fragment is stored in `source-fragment.html`.

Heading star: False. Starred subparts: a. Hall of Fame entries: 1. Linked background sections indexed: 1.

Current research: **whole-entry candidate coverage**, combining the proposed general algorithm for N8(b) with the prior negative answer to N8(a). The [general proof](general-proof.md) decides a single commutator equation in every finite rank and class; the [audit](general-audit.md) distinguishes its mathematical argument from the bounded independent computations. A diagonal separation lemma replaces the former exception-count bound. Independent GAP reconstructs44 complete Lie spaces and three new actual group fixtures, with full integer lattices and all quadratic coefficients. The all-rank/class algorithm is now implemented end to end in the [general word command](general-word-audit.md), with [native group reconstruction](general-implementation-audit.md). Its structural proof and novelty remain subject to specialist review. Earlier partial proofs and failed approaches are retained as dated stages. The following is the original preparation source metadata. The machine-readable source evidence is in `data/problems.json`; the extracted text below is a search aid, not an authoritative transcription.

```text
(N8) (A.Miasnikov) * (a) Is it true that equations of the form [x,y] = g (g \in
G) are decidable in every finitely generated 2-nilpotent group G?
(b) Are equations of the form [x,y] = g (g \in G) decidable
in every finitely generated free nilpotent group? Background
```

The [projective-factor audit](projective-factor-audit.md) gives an
alternative central-target decision argument and implementation, with
13 exact Lie cases and 16 independent GAP group-witness checks. This
is an earlier implementation stage, superseded by the complete recursion.
