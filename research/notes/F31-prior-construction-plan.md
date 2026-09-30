# F31: check the prior counterexample beyond its abstract

30 September 2026. Previous turn made progress at 8c2d289 and d6d2b39;
the worktree and job registry are clean, and the original clock is active.
The broader portfolio scan did not find a new proof for H15, S7 or AUX4.
F31 was retired on the abstract of Lei--Zhang, arXiv:2604.24502v2.
Read its actual graph construction and the free-factor argument and
verify that they answer the site's one-injective-map formulation.

The key issue is not merely constructing a rank-(2n-2) subgroup inside
an equalizer: subgroup rank need not be monotone. The source's injective
coloring makes the natural core-graph map injective, which supplies a
free factor and the required rank inequality. Inspect that implication.

Check the explicit maps g(t)=a, h(t)=b,
g(x_i)=h(x_i)=(a^-i b^i)^2. Build their folded subgroup graphs,
the colored graph with t-chain and two x_i loops, and every coloring
identity for n=2,...,12. Separately reconstruct subgroup ranks and
word equalities in native GAP. Include a rank-three subgroup of the
rank-two identity equalizer as a negative control for dropping color
injectivity. Finite checks support the interface; the all-rank result
remains the authors' written theorem.

Render the original F31 paragraph and selected primary proof pages,
then actually inspect them. Keep this as credited prior work, not a
new candidate, novel result, or external specialist review. Preserve
the prior triage bytes before updating its evidence field.
