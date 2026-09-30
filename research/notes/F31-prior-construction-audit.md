# F31: audit of Lei--Zhang's prior counterexample

30 September 2026. **Prior work, excluded from our candidate count.**
The earlier triage rested on an abstract. This pass reads the main
construction and proof, checks the original problem, and reproduces
its finite word and graph interfaces in two implementations.

Primary source: Jialin Lei and Teng Zhang,
[*Colored Stallings graphs and Counterexamples to Stallings equalizer
conjecture*, arXiv:2604.24502v2](https://arxiv.org/abs/2604.24502v2),
9 May 2026. The arXiv record was reopened and still lists that version;
no journal acceptance or external validation is inferred. The retained
PDF has SHA256
`f1d96297adc895bad8e8b62100fb5c789e08ccace5c2cccd7d3ea593169fc223`.

## Exact scope and the important proof step

F31 asks whether one injective map F_n -> F_m suffices for the equalizer
rank bound n. The authors' examples have **both** maps injective, target
rank two, and equalizer rank at least 2n-2. Thus n=3 already refutes the
original universal assertion. The n=2 case of this family is a boundary
control, not a counterexample.

Writing F_n=<t,x_1,...,x_(n-1)> and c_i=a^-i b^i, their maps are

    g(t)=a, h(t)=b, g(x_i)=h(x_i)=c_i^2.

Sections 2--4 were read, especially Lemma 2.10, Proposition 3.3 and
Lemma 4.3. The colored graph has a t-chain of n vertices, with x_i-loops
at its base and its i-th vertex; its colors are c_i. Its rank is 2n-2.
If two vertices merged in the natural map to the equalizer's core,
the two paths to them would have equal twisted differences g(p)^-1 h(p).
Their colors would coincide. Distinct colors prevent that merge, and
foldedness prevents edge identifications. The graph therefore embeds,
giving a **free factor** of the equalizer. This justifies the rank
inequality; subgroup inclusion alone would not.

The image-rank argument uses the basis t,t^i x_i, whose g-images are
a,b^i a^-i b^i. The displayed folded graph makes these a free basis
of their image. Swapping a and b gives the corresponding assertion
for h. No missing hypothesis was found in this same-agent reading of
the main argument. This is not a new proof or a specialist assessment.

## Exact checks and a negative control

The [Python check](../../scripts/check_f31_prior_construction.py) builds
folded subgroup graphs for n=2,...,12. For all eleven ranks it verifies
both image ranks, the colored graph rank, its foldedness, distinct colors,
every edge identity and membership of every displayed basis word in the
equalizer. There are 198 edge identities. It does **not** compute the
whole equalizer or claim that 2n-2 is its exact rank.

The [GAP check](../../scripts/check_f31_prior_construction.g) independently
constructs the maps and words with native free groups and computes
subgroup ranks using the fga package. It reads no Python certificate.
It verifies the same eleven ranks and 198 identities. Both checks
ensure that t itself is outside the equalizer.

The negative control uses g=h=id on F(t,x). Then Eq(g,h)=F(t,x) has
rank two, although <t^2,x,t x t^-1> has rank three. Its two-vertex core
can be colored constantly by 1. This checks why injectivity of colors,
not just the edge equations and subgroup membership, is indispensable.

The mathematical jobs passed in 0.119 and 1.877 seconds, respectively,
with empty stderr. Finite reproduction supports these interfaces; the
universal all-rank implication is the authors' written argument.

## Source inspection and reproducibility

The complete archived free-group HTML page, F31 fragment and linked
background passage were read. The original HTML was rendered directly,
without mathematical transcription, and the page containing F31 was
actually viewed. Its one-injective-map hypothesis agrees with the
scope above. Printed primary-source pages 7,9,11 were also rendered
and viewed, covering the graph embedding, image basis and rank argument.

The first Chromium render failed with SIGTRAP under its recorded cap;
the exact cause is not established. A static WeasyPrint attempt then
failed because Pango was absent. Five Ubuntu libraries were downloaded
and unpacked into ignored scratch, after which the static rendering
passed in 2.477 seconds. Its print layout differs from Chromium, while
the input is the original archived HTML. WeasyPrint 70.0 and all Python
dependency versions are recorded in the render metadata. The native
package URLs and hashes are retained; the installed software is not
represented as committed. No system installation was performed.

Seven jobs cover the two mathematical checks, three rendering attempts
and two dependency setup commands. Each used one CPU and a 2 GB
per-process address-space cap; their maximum overlap was three CPU
reservations and 6 GB of requested caps, not measured aggregate memory.
The pip setup printed an unrelated pre-existing asciinema metadata
warning. All failed logs and the original renderer version are retained.
Successful mathematical and final rendering jobs had empty stderr.

The [manifest](../certificates/F31-prior-construction/manifest-v1.json)
binds inputs, source versions, renders, outputs and terminal receipts.
The original catalogue/source snapshots and previous triage version
remain available. No candidate, novelty count, deadline or publication
status changes, and no Kourovka material is imported.
