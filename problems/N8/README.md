# N8 — Nilpotent groups

[Offline statement](statement.html) · [Complete archived page](../../sources/raw/probnil.html) · [Publisher](https://shpilrain.ccny.cuny.edu/gworld/problems/probnil.html)

Source begins at line 42; byte range [1669, 2038). The raw fragment is stored in `source-fragment.html`.

Heading star: False. Starred subparts: a. Hall of Fame entries: 1. Linked background sections indexed: 1.

Current research: one partial candidate for N8(b), covering all targets through class 26, all targets with c-d<=13 (d the nonzero target's leading degree), leading degrees through twelve in arbitrary class, branches with at most three remaining exceptional offsets, and the earlier separated-offset and weighted-orbit families. See the [three-exception proof](three-exception-proof.md) and [audit](three-exception-audit.md), together with the [fourteen-layer proof](fourteen-layer-proof.md). Independent GAP reconstructs all degree-two coefficients in an actual weighted class-26 group fixture and checks complete integer fibers, exact substitutions, all residue descriptions and group witnesses. The all-rank branch algorithm is not implemented end to end. General N8, independent specialist review and novelty remain unresolved. The following is the original preparation source metadata. The machine-readable source evidence is in `data/problems.json`; the extracted text below is a search aid, not an authoritative transcription.

```text
(N8) (A.Miasnikov) * (a) Is it true that equations of the form [x,y] = g (g \in
G) are decidable in every finitely generated 2-nilpotent group G?
(b) Are equations of the form [x,y] = g (g \in G) decidable
in every finitely generated free nilpotent group? Background
```

The [projective-factor audit](projective-factor-audit.md) gives an
alternative central-target decision argument and implementation, with
13 exact Lie cases and 16 independent GAP group-witness checks. This
does not enlarge the current partial scope.
