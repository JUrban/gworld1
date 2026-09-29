# F38(c): scope, proof dependencies and finite verification

Work period: 29 September 2026, approximately 10:33--11:00 UTC.
The graded-shortening lead was identified around 10:40; the complete
written candidate and all current computational checks were produced
before the original 30 September 10:04:49 UTC deadline.

## What is claimed

`bounded-proof.md` gives a candidate decision of the actual F38(c) for
every finite ambient rank. Its stronger one-sided characterization is

    ||alpha(v)|| <= C ||alpha(u)|| for all alpha
    iff Stab_Out([u]) has finite orbit on [v].

Two-sided comparison is therefore equivalent to commensurable
conjugacy stabilizers. The necessary condition, the full stabilizer
algorithm and the finite-orbit algorithm were already in this repository;
the new mathematical step is sufficiency, via a quantitative application
of graded shortening. Older notes and their hashes are preserved.

The outcome upgrades F38 from a partial-entry candidate to a whole-entry
candidate when combined with `part-a-proof.md` and the **prior** answer
to part (b). It is one entry, not separate counts for each theorem or
subpart. Rank-two decisions were already known. The experiment now has
seven whole candidates, three partial candidates, and zero established
novel results. Specialist correctness and novelty review remain pending.

## Statement fidelity and prior work

Read the complete frozen F38 fragment and its background again, and
viewed the actual archived paragraph rendering. The source is
`sources/raw/probfree.html`, lines 275 onward, bytes [13587,14646);
the preserved fragment and source hashes are included in the manifest.
The background is `sources/raw/Back.html`, lines 794--819. Part (b)
is starred and credits Lee; the heading's lack of a star is not an
openness certificate.

The quantifier is over automorphisms of the specified ambient group.
The separate tree-action definition in KLSS Problem 8.4 is stronger
for bounded comparison and is not substituted here. The Lee pair
in rank two and its failure after inclusion in rank three are retained
as explicit controls. Identity ratios are excluded by the software;
the mathematical inequality extension is stated separately. Conjugacy
classes are oriented: inversion is not silently identified.

The bounded searches included combinations of “bounded translation
equivalence”, “stabilizers”, “commensurable”, “algorithm rank”, and
“free group linear bound relative shortening”. They located Lee's
rank-two decision, the already archived filling results, and the
graded-shortening source, but no matching full criterion. Search
failure does not establish novelty. A current GAGTA 2026 abstract
also discusses bounded translation equivalence without giving this
general theorem; no unpublished result is inferred from that abstract.

## The essential imported theorem and hypothesis audit

Sela's primary source was downloaded from
<https://www.numdam.org/item/10.1007/s10240-001-8188-y.pdf>.
The archived PDF has SHA256
`165d5ca99cd4f59d422e6e18377c439809f6d74bd69a9eb52c21a9b607d2789c`.
The relevant passages read are Section 1, Definition 9.1, Theorem 9.2,
Definitions 10.1--10.3, Lemma 10.4 and its local proof, the free-group
example on printed page 89, and the constant-sequence passage in
Proposition 5.6. Actual printed pages 89--90 were viewed and retained
as images. In particular the growth factor is **2^m**, not “2m” as
plain-text extraction can suggest.

The reduction in the proof explicitly checks:

1. The source word u is in no proper free factor of A. The arbitrary
   input reduction, which is separate, handles the other words.
2. G=A*<z> is freely indecomposable relative to P=<u,z>. Intersections
   of free factors prove this, and also show every pointwise P-fixer
   preserves A and fixes z.
3. The coefficient-free graded setup is used, with u,z as parameters.
   Both rigid and solid cases are covered. A constant shortest embedding
   supplies the identity shortening quotient in the nontrivial-JSJ
   case. This does not require computing a JSJ decomposition.
4. The maps are minimized over the full pointwise P-fixer and are
   therefore short for the smaller graded modular group. A hypothetical
   failure of a linear bound supplies the exact flexible-sequence
   inequality from Definition 10.3(ii).
5. Injectivity excludes a nontrivial relative free-product **quotient**
   factorization. Merely embedding a group into a larger free product
   with an unused factor is not the factorization in this condition.
6. The rescaled actions cannot have a global fixed point, by the explicit
   displacement inequality M/(|u|+1). Three explicit orbit points form
   a tripod in the limit. The action kernel is trivial by the eventual
   tripod-kernel assertion and injectivity, rather than by an unchecked
   blanket assertion about limits of embeddings.
7. Lemma 10.4(ii) would make this same quotient proper, giving the
   contradiction. Its substantial JSJ/Rips shortening proof is imported,
   not independently formalized or re-proved here.

Ould Houcine--Vallino, *Algebraic and definable closure in free groups*,
AIF 66(6) (2016), 2525--2563, was also downloaded. Definitions and
Theorems 2.15--2.16 were read as extracted text, but its PDF was not
visually inspected. The bounded-parameter theorem alone does **not**
yield the quantitative statement; it was not used as if it did.

The decision additionally imports the full Whitehead/McCool stabilizer
construction and Handel--Mosher's Theorem 4.1 on the level-three kernel.
Their precise primary references, previous source inspections and
reading limits are in `research/notes/F38-stabilizer-obstruction.md`.
No computational control proves these structural theorems.

## Executable decision procedure

`scripts/f38_bounded_equivalence.py` adds:

- `bounded_equivalence(rank,u,v)`, returning a two-sided answer;
- `one_sided_comparison(rank,u,v)`, deciding the directed inequality.

Words are signed nonzero basis-index sequences. Both functions reject
invalid ranks, invalid letters and identity inputs. Rank one returns
the exact constant ratio. Larger ranks use the preserved
`f38_stabilizer_obstruction.py`; only the new wrapper upgrades a passed
necessary test to a positive answer, with an explicit reference to
the new theorem. There is no cutoff interpreted as a mathematical NO.
Large instances can still exhaust external resources; no practical
large-rank complexity claim or numerical bound-constructor is made.

The Python suite checks ten two-sided cases and five directed cases.
They include Lee's known positive, its rank-three negative, a pair
inside a proper filling free factor, a cyclic-HNN vertex pair,
commutator powers, transported nonminimal words, rank four primitive
powers, and both directions of genuinely asymmetric comparisons.
Six malformed-input controls are rejected.

The new elementary reductions have separate finite controls:

- 2,376 twist records, from ranks three/four and cyclic lengths up to
  five/three, check the two complementary-letter twists and exact
  eventual growth. The simultaneous zero-growth condition excludes
  precisely the complementary letter in these enumerated words.
- 39 certified rank-two automorphisms, from Whitehead chains of depths
  0--12 with seed 9292638, act on six fixed words in <a,bab^-1>.
  All 234 checks verify the commutator length and the proved 3L bound.
- Explicit injections a->a,b->b^n at n=2,5,11 retain the failure of
  the blanket injection replacement for Lee's pair.

## Independent GAP verification

`scripts/check_f38_bounded_equivalence_gap.g` uses GAP's native free
group words. For positive instances it reconstructs the entire
Whitehead move set, independently minimizes the fixed word, explores
the complete minimum graph, constructs every spanning-tree loop and
transports it back to the original input. It then checks preservation
of the supplied finite orbit under every resulting loop map. This
closes the implementation-audit limitation of the earlier stabilizer
checks, which did not independently reconstruct the full minimum graphs.

The completed replay checks 12 distinct minimum graphs, 148 vertices,
20,948 directed edges and 1,058 distinct loop-image maps across those
graphs. Fifteen finite-orbit fixtures require 1,150 loop/orbit
transitions. Six negative witnesses have two-sided inverses, fix one
input class, move the other, and act identically modulo three on
abelianization. Imported aperiodicity is what makes their iterates
infinite; a finite sample is not used to infer that.

GAP also independently evaluates all 2,376 twist records and uses the
two-vertex carrier graphs to check their zero-growth assertions. It
replays all 234 rank-two inequalities, checks the actual ambient
automorphisms, and reconstructs the two-generator carrier expressions.
These finite checks support the stated formulas and implementation,
not the universal graded-shortening application.

## Process evidence and reproduction

Both jobs used one CPU slot and an 8 GB per-process memory reservation,
sequentially. They completed with actual exit status zero, the required
marker, and empty stderr:

| Recorded run | Seconds |
| --- | ---: |
| `f38-bounded-python-v1` | 1.223096 |
| `f38-bounded-gap-v1` | 8.447054 |

No failed mathematical/checker run preceded these two passes. A
read-only attempt to inspect `stdout.txt` failed because the runner
uses `stdout.log`; the correct actual logs were then inspected. No
failed evidence or mathematical expectation was overwritten.

Commands, versions and log hashes are in each `results/` process record.
The artifact manifest includes the sources, proof, audit, frozen
statement, implementation snapshots, fixture files and both runs.
The Python exporter refuses to overwrite its output directory. To
regenerate, use a disposable checkout and remove only that checkout's
`research/certificates/F38-bounded/` first. GAP replay itself is read-only:

```sh
bin/gap -q scripts/check_f38_bounded_equivalence_gap.g
```

All work is local, with no subagents, imported Kourovka material,
pushes or author contacts. The original experiment clock is unchanged.
The primary remaining risks are the correctness of the structural
theorem application and novelty, both requiring independent review.
