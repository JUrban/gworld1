# F20: direct equational proof search, still inconclusive

29 September 2026, approximately 18:51--19:00 UTC. No new solution or
partial candidate. This changes the method from the earlier KBMAG and
finite-cover probes to explicit first-order equational proof search.

## Inputs and mathematical interpretation

The complete original free-group page and F20 background were reread, and
the original paragraph rendering was viewed again. The question concerns
normal generation by commutators of exactly weight c. The present inputs
are restricted to rank two and weights five and six.

`scripts/generate_f20_equational.py` names the Hall commutators of weight
less than c by constants c001,c002,..., using [u,v]=u^-1 v^-1 u v. The
collection encoding defines a named commutator k by uv=(vu)k. The second
encoding writes out inverses. Only weight-c Hall commutators are killed.
The remaining axioms are ordinary group identities. In particular there
is no assertion that the presented group is nilpotent.

For c=5 there are nine weight-six targets, and for c=6 there are eighteen
weight-seven targets. Both encodings also include one negative control
of weight c-1. Thus 58 complete TPTP files were generated and hashed.
They are ground presentation-consequence problems: the named Hall
elements are constants, while the group axioms are universally quantified.

GAP independently reconstructs the Hall sequence, parses every actual
TPTP file and evaluates all 1,560 clauses in its native free-group
representation. It checks the exact definition, relator and goal formulas,
their roles and completeness, the absence of extra axioms, and the group
identities. For each weight it also constructs a class-(c-1) nilpotent
quotient: every imposed relator vanishes but the selected negative control
does not. These models check the encoding; they say nothing about the
unresolved weight-seven targets.

## Bounded results

E was built from upstream commit
`3b7afc70fe77d3118bb95144c4735ca45f5f31cf`. The source checkout and binary
are ignored local tools, not claimed as included in Git. Their source URL,
build commands, version output and binary SHA256 are in
`research/certificates/F20-equational/eprover-build.json`. The upstream
version banner carries an older embedded revision; the separately recorded
Git checkout is the actual source pin. The local build used four CPU slots.

| Attempt | Limit | Result |
|---|---:|---|
| Weight-five collection target09 | 30 CPU seconds | Proof in0.020s; known positive control |
| Weight-five collection target01 | 30 CPU seconds | Proof in1.123s; known positive control |
| Weight-six collection target01, [c006,c004]=1 | 30 CPU seconds | Proof in0.820s; already found by the old rewriting probe |
| Weight-six target03, collection and inverse encodings | 30 CPU seconds each | Both reached CPU limits |
| Weight-six collection target07 | 30 CPU seconds | CPU limit |
| Weight-six collection targets03,04,05,06,07,08,11,12 | 60 CPU seconds each | All scheduled searches exhausted their budgets |

The last eight targets are precisely those missed by the earlier rewriting
probe. Automatic scheduling selected a single strategy for each input at
this bound; this was not a completed sweep of many different strategies.
Its logs report `GaveUp` with process exit9. The earlier CPU-limit exits
were8. None is interpreted as a counterexample or negative answer.

All three successful E proof objects and their full raw outputs are
retained. They have not undergone independent inference-by-inference
replay, and establish no new experimental scope: both weight-five cases
are prior, and the weight-six consequence was already observed here.
The independent GAP check concerns the entire input encoding and explicit
negative models, not the E inference engine or the unresolved theorem.

## Process record and limits

There are18 terminal recorded jobs: build1, input generation1, GAP audits2,
and E attempts14. Seven have successful process records; eleven proof
searches did not find a proof within their bounds. The first successful
GAP audit emitted harmless unbound-global syntax warnings. Its exact
source is retained as `input-audit-v1.g`; the final checker wraps its
variables in a function and passes with empty stderr. No earlier output
or failed attempt was overwritten.

The largest concurrent reservation was5 CPU slots and16GB: four E jobs
at3GB each plus one GAP job at4GB. All jobs finished, and the shared job
registry is empty. Evidence and exact run paths are indexed in the local
`F20-equational/manifest-v1.json`.

The input generator refuses to overwrite its output. For a fresh replay,
use a new output directory and new recorded-run names. The GAP checker
reads the archived inputs without modifying them:

```sh
bin/gap -q scripts/check_f20_equational_inputs.g
```

An effective next step would require additional mathematical structure
or a substantially different proof strategy. Enlarging these same search
limits is not currently prioritized. The previous rewriting and cover
notes retain their original inconclusive conclusions.

Tool source and invocation documentation:
[E upstream README](https://github.com/eprover/eprover/blob/3b7afc70fe77d3118bb95144c4735ca45f5f31cf/README.md).
The prior mathematical sources and their reading limits are recorded in
`F20-bounded-rewriting.md` and `F20-finite-cover-homology.md`.
