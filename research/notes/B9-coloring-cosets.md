# B9: bounded coloring-coset probe and a rejected shortcut

29 September 2026, approximately 20:58--21:08 UTC. No new special B4
braid or count is claimed. This records a different search from the
earlier finite-height and fixed-right-argument probes.

## Target and algorithm

The remaining B4 exponent-two sector is represented by right cosets
A B2 in B3 with A=a S(c), where a,c are special. The coloring of the
three-strand braid A, when defined on (1,1,1), is then (a,c,1).

The C++ probe explores the graph of valid colorings from (1,1,1), using
generators s1,s2 and their inverses. A positive crossing replaces (a,c)
by (a▷c,a). For a negative crossing it solves c▷d=a by testing

    S(d)=c^-1 a S(c) s1^-1.

First-strand deletion produces a proposed d, and exact CBraid canonical
forms check that reinserting the first strand recovers the original
braid. Every accepted division is checked again by c▷d=a. By the prior
coloring-closure lemma (Dehornoy, *Strange Questions*, Lemma 2.1), colors
remain special. Undefined steps are discarded. This is a bounded graph
search, not a complete membership test applied to every short braid word;
another representative may admit a coloring when a particular path does
not.

Vertices are identified by exact canonical forms in B3. At every vertex
with third color 1, compute I_2(A) in B4 and compare its canonical form
with the four already known examples. Explicit limits are depth 12,
100,000 states, 20,000 letters per intermediate word and ambient rank 20.
The completed search visits 1,891 states and 46 vertices with third color
1. All belong to the four known cosets. No state, word or rank cap is hit.
This does **not** exhaust the unbounded graph.

## A structural shortcut fails

The first probe suggested testing whether every admissible three-strand
braid lies in one of two positive right cones,

    B3^+ union u2 B3^+,       u2=s1^2 s2^-1.

A second pass records all states and tests precisely this additional
hypothesis. Of the 1,891 states, 1,581 are positive, 143 are in the
second cone but not positive, and 167 lie outside both. The shortest
counterexample found is

    A=s2 s1^2 s2^-1.

It has the explicit special decomposition

    A=(tau_2▷1) S(1) S^2(s1),       tau_2=s2 s1.

Indeed, tau_2▷1=s2 s1^2 s2^-1 s3^-1, and multiplying by s3 cancels
the final factor. Its coloring path is

    (1,1,1) -> (1,s1,1) -> (tau_2,1,1)
            -> (tau_2▷1,tau_2,1) -> (tau_2▷1,1,s1),

with labels s2,s1,s1,s2^-1. Every color is an explicit special term.

To verify the cone exclusions independently of CBraid, note epsilon(A)=2.
If A were positive, it would equal one of the four positive words of
length two in s1,s2. Faithful Artin actions distinguish it from all four.
Likewise epsilon(u2^-1 A)=1, and that braid differs from both s1 and s2.
Thus A is in neither cone. The final color is s1, not 1, so this is a
counterexample to the proposed shortcut, **not** a new B4 special braid.

## Reproduction and evidence

`scripts/probe_b9_coloring_cosets.cpp` is the second version, which also
exports every state as JSONL. The exact first version is retained as
`research/certificates/B9-coloring-cosets/probe-v1.cpp`. Both use CBraid
at commit `891fcaf7cf9af3ec9ca0f1b0e46b0f86cf461b78`, already obtained
earlier in the run. The ignored upstream source and binaries live under
`large-artifacts/tools/`; the manifest records their identities. Regenerate
the binary with

```
g++ -O2 -std=c++17 -Ilarge-artifacts/tools/cbraid/include \
  scripts/probe_b9_coloring_cosets.cpp \
  large-artifacts/tools/cbraid/lib/libcbraid.a \
  -o large-artifacts/tools/b9_coloring_cosets_v2
```

Recorded jobs `b9-coloring-cosets-build-v1/v2` and
`b9-coloring-cosets-depth12-v1`, `b9-coloring-two-cones-v1` all passed.
The two search runs took 7.69 and 7.95 seconds, respectively, with one
CPU and a 6 GB per-process cap. The second pass tested a newly proposed
structural condition and exported evidence; it did not enlarge a search
bound merely to look for another non-hit. Both searches are deterministic.

`scripts/check_b9_two_cone_obstruction.g` independently verifies the exact
counterexample, its special decomposition, the division step, all six
positive-word exclusions and an extra-cone positive control. Its recorded
run is `b9-two-cone-obstruction-gap-v1`. It does not recheck all 1,891
CBraid graph states, whose status remains exploratory computational
evidence. No universal exhaustion claim rests on either implementation.

All jobs are terminal. No Kourovka material was imported. B9 remains
one partial candidate; the remaining four-strand coset problem is still
open in this run. Do not repeat or enlarge this probe without a new
structural reason.
