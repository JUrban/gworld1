# B9: repeated right translations did not give an infinite family

29 September 2026,19:43 UTC. Follow-up to the verified height-bound
counterexample, not another candidate or a general nonexistence result.

The special braid shelf has acyclic left division: a is strictly below
a ▷ b in its division order. Consequently, an infinite sequence obtained
by repeating a -> a ▷ b inside one fixed Bn would consist of distinct
special braids and establish infinitude there. This is the structural
hypothesis tested, not an attempt to improve a finite lower-bound count.

Seeds were the52 height-at-most-four braids and11 independently verified
new B5 examples, all distinct by finite Burau images. For each ordered
pair a,b of these63 seeds, the program repeatedly replaces a by a ▷ b,
holding b fixed. A dimension-six Burau image not supported in the first
five coordinates certifies departure from B5. Surviving steps are checked
with the pinned CBraid strand-deletion/canonical-form checker. The same
word and matrix conventions as the main B9 audit apply.

The nominal caps were8 steps and2000 letters per unreduced shelf word.
Neither cap was reached. Of3969 starting pairs, respectively270,66,13,1
remain in B5 after1,2,3,4 steps; all leave on or before step5. Every
departure is already certified by the finite matrix obstruction. The
unique trajectory retained for four steps starts with a=b=1, the ordinary
successive left powers. Its word lengths are0,1,3,7,15.

`b9-fixed-strand-orbits-v1` passed in1.02seconds, one CPU/4GB, empty stderr.
The input hashes,63 explicit seed words, stage counts and longest
trajectory are in
`research/certificates/B9-strand-drop/fixed-strand-orbits-v1.json`.
The deterministic script is `scripts/probe_b9_fixed_strand_orbits.py`.
No independent second implementation of this exploratory orbit search
was run; the eleven height counterexamples retain their separate GAP proof.

This only tests these fixed right arguments and starting seeds. It does
not exclude variable right arguments, other seeds, other strand numbers,
or a different infinite-family construction. Park this route unless a
new structural invariant or explicit recurrence suggests otherwise.
The nine whole-entry candidates and one partial candidate are unchanged.
