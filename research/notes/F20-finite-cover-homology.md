# F20: bounded integral homology of finite covers

29 September 2026, approximately 01:47–01:58 UTC.
**Inconclusive search, not a solution or a new partial candidate.**

For the rank-two presentation using only the nine weight-six Hall
commutators as relators, none of the eighteen weight-seven Hall words
survives in the first integral homology of any of the 143 selected finite
regular covers. An additional 75 weight-five presentations provide known
positive controls. GAP and an independent Python/FLINT calculation agree
on all 218 covers, including the integral lattice membership tests.
This does not prove the weight-seven words trivial in the presented group.

## Exact question and motivation

The original F20 HTML, linked background and actual rendered paragraph
were re-read/viewed. The question is normal generation by commutators of
**exactly** the specified weight, in arbitrary finite rank. This probe
only concerns rank two. The previous rewriting computations remain in
`F20-bounded-rewriting.md`; their limits and failed reduction are unchanged.

This probe changes the method rather than increasing the rewriting budget.
A word nonzero in a subgroup's abelianization is nontrivial in the group.
Thus finite-cover homology can certify a negative answer when it detects
a target. A zero class has no corresponding implication about the word
itself. Finite nilpotent quotients alone cannot distinguish the candidate
presentation from its maximal nilpotent quotient; the present test retains
the abelianization of the cover subgroup, not just its finite quotient.

## Why the integer test is sound

Let F=<a,b> be free, R the normal closure of the weight-c Hall relators,
and P=F/R. Choose a finite quotient Q of F of nilpotency class less than c.
Every relator vanishes in Q. Let S be the kernel of F->Q, so R is contained
in S. The corresponding subgroup of P is S/R, with abelianization

    S / ([S,S] R).

The directed Cayley graph of Q for a,b has |Q| vertices and 2|Q| positive
edges, retaining loops and parallel edges. Its integer cycle lattice is
S/[S,S], of rank |Q|+1. For every defining relator and every vertex, record
the signed number of traversals of each positive edge in its lifted loop.
Let L be the integer span of these vectors. It is precisely the image of
R: arbitrary conjugates by F reduce to these |Q| lifts, since conjugation
by S is trivial in S/[S,S]. The access path from the base vertex to the
lift cancels with its return path in the edge-count vector.

For a target word t that closes in Q, its edge-count vector belongs to L
if and only if its class in the cover subgroup's abelianization is zero.
We work in the full free edge module; no rational saturation of L is
taken. Integer Hermite normal form decides membership exactly, including
torsion obstructions. Although all translates of each relator are needed,
testing a target at one vertex suffices here: L is invariant under the
left action of Q on the graph, and every other starting vertex is a
translate. We choose vertex 1 in the saved enumeration, which need not
be the identity element.

## Enumeration, controls and results

The Hall order starts with a<b and increases by weight; within each
weight it orders parent indices lexicographically. A pair (i,j) contributes
when i>j and the right parent of i, if present, is at most j. The convention
is [u,v]=u^-1 v^-1 u v. Counts in weights 1 through 7 are
2,1,2,3,6,9,18. Only weight c is imposed; weight c+1 supplies targets.

The finite-group enumeration uses GAP's Small Groups library. It retains
every nilpotent group with at most two generators of the indicated orders,
and one minimal generating tuple for each group, padded by the identity
if necessary. The complete right-action transition tables are saved, so
replay does not depend on the library choosing the same tuple later.
It is **not** an enumeration of all generating pairs or all finite covers.

| Input presentations | Quotient orders | Covers | Targets per cover | Survivors |
| --- | --- | ---: | ---: | ---: |
| weight 5, known positive controls | all orders 1 through 32 | 75 | 9 | 0 |
| weight 6 | all orders 1 through 32 | 75 | 18 | 0 |
| weight 6 | 64, 81, 125 | 68 | 18 | 0 |

There are 3,249 individual target checks. Every tested cover has first
Betti number two. Neither this Betti number nor the vanishing targets
establishes nilpotence of P.

Three extra controls use the two-sheeted graph where a interchanges the
vertices and b fixes them. The word [b,a] survives with no relators,
vanishes when it is a relator, and survives as torsion when only its square
is imposed. The last control checks the need for integral membership.
Both implementations pass all three.

GAP constructs freely reduced Hall words and reduces target vectors by
its row Hermite form. Python independently constructs the bracket words
without free reduction, verifies all inverse transitions, graph
connectivity and cycle boundaries, and compares integer lattices before
and after adding target vectors. Its final version uses FLINT Hermite
forms. It reuses the saved finite quotient tables, not GAP's relation
matrices or Hall words. This is independent arithmetic replay, not
independent reconstruction of the Small Groups database.

## Runs, failures and reproduction

All runs used one CPU slot, a 4 GB per-process limit, and a 180-second
timeout, under `scripts/run_recorded.py`. No random search was used.

- `f20-cover-homology-v1`: failed after 1.774 seconds because GAP's minimal
  generating set was immutable and the trivial-group tuple needed padding.
  No cover record was completed. The incomplete two-byte JSON output,
  exact original script, stderr and misleading GAP exit code zero are
  retained. The runner correctly recorded `process_ok=false`.
- `f20-cover-homology-v2`: after making an explicit mutable copy, all
  150 initial covers and three controls passed in 2.828 seconds.
- `f20-cover-homology-class5`: the 68 additional covers and three controls
  passed in 8.748 seconds, using the same corrected GAP script.
- `f20-cover-homology-python-v1`: the SymPy-Hermite replay reached its
  180.220-second timeout after 152 completed cover records. Its stdout is
  only a verified prefix; the suite did not pass and wrote no final JSON.
  Its exact source is saved separately.
- `f20-cover-homology-python-v2`: switched to FLINT and batched the lattice
  equality check. All 218 covers and three controls passed in 38.048
  seconds. Final Python and both completed GAP runs have empty stderr.

Exact sources, transition tables, final independent records and hashes are
in `research/certificates/F20-cover-homology/`. Process evidence remains in
the five corresponding `results/` directories. GAP 4.16.1,
Python 3.12 and python-flint 0.9.0 were used; the failed first Python
replay used SymPy 1.14.0.

For a replay during the active experiment, choose a fresh output and job:

```sh
python3 scripts/run_recorded.py --name f20-cover-independent-repeat \
  --cores 1 --memory-gb 4 --timeout 180 \
  --expect 'PASS F20 independent cover homology:' \
  -- .venv/bin/python scripts/check_f20_cover_homology.py \
  research/certificates/F20-cover-homology/checks-v2.json \
  research/certificates/F20-cover-homology/checks-class5.json \
  --output scratch/f20-cover-independent-repeat.json
```

After the deadline the same Python command can be used directly for
verification, without restarting the experimental clock or overwriting
the archived evidence.

## Prior scope and next useful step

The already archived Moravec–Morse paper proves the weight-five case;
Jackson's weight-six-and-seven result remains separate from weight six
alone. A targeted search also located the author-uploaded text of
Jackson–Gaglione–Spellman, *Basic commutators as relators*, J. Group Theory
5 (2002), 351–363, [DOI 10.1515/jgth.2002.008](https://doi.org/10.1515/jgth.2002.008).
Its Theorem 3.8 gives prior positive answers in the metabelian variety and
in the variety satisfying [[x,y,z],[u,v]]=1. The theorem was checked in the
[author-uploaded extracted text](https://www.researchgate.net/publication/243106291_Basic_commutators_as_relators);
the original PDF was not obtained or visually inspected. This result is
background, not a new conclusion of the probe. The abelian-quotient
controls therefore explore a case already constrained by the metabelian
theorem.

The bounded search found no later full resolution, which does not prove
current openness. Increasing the finite-cover range is a low priority.
A useful next F20 step would need a structural argument about the kernel
of P->F/gamma_6(F), a genuinely different quotient, or a derivation of the
remaining weight-seven relators in the original normal closure. No such
argument is supplied here.
