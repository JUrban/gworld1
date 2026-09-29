# GA3: focused recheck of the collapse and boundary argument

29 September2026, approximately16:25--16:27UTC. Internal dependency
review while the N8 class26 computations run. No candidate, count or
novelty change; no external specialist review is implied.

Reread the complete candidate proof and the scope/dependency audit.
Then reread the archived Guirardel2004 Sections2.3--2.6, Fact5.1,
its general-Lambda remark and its proof on printedpages1448--1449.
Actually viewed the saved image of printedpage1448. Reread the
archived Rybak2026 Lemmas2.6 and2.9 and the intervening action
classification. This is a targeted check, not a fresh full-paper audit.

The main possible defect was replacing an arbitrary ordered length group
by a real length group while silently importing a finite-height theorem.
Guirardel's remark explicitly applies Fact5.1 to every Lambda and every
convex subgroup. Its proof identifies an elliptic element's fixed set
after collapse with the image of its original axis, so it contains no
tripod. A non-infinitesimal common arc forces two such elements to commute.
Neither conclusion here requires the later Rips-machine structure theorem.

The chosen scale is also essential. The maximum of translation lengths
of generators and their two-letter products bounds the bridges between
generator axes. A finite Helly argument therefore supplies a basepoint
whose generator displacements lie in the principal convex length group.
An element attaining that maximum has a surviving axis segment after
collapse. The proof does not assume that arbitrary displacement-based
rescaling gives a nontrivial action.

The source's special definition of closed subtree was checked: axes are
closed in precisely the sense needed for projection, even in a
non-Archimedean tree. The displacement and projection formulas in
Section2.5 support the scale argument. Divisible scalar extension followed
by segment filling preserves the stabilizer conclusions: every new arc
contains an old subarc, and a new tripod contains an old tripod. Metric
completeness is not being assumed.

CSA rules out an abelian normal kernel, and hence a preserved line or
end. In the end case each zero-Busemann element fixes a terminal ray;
any two such rays have a common terminal segment. Arc fixators being
abelian therefore makes the whole kernel abelian. This step does not
mistake arbitrary elliptic elements for a common point stabilizer.

For the boundary step, Lemma2.9 states density of ordered loxodromic
endpoint pairs for general-type actions, and Lemma2.6 gives the needed
uniformity outside a neighborhood of the repelling endpoint. Three fixed
ends would force a pointwise fixed tripod. Thus each nonidentity constant
excludes at most two endpoint choices. The selected cones separate all
constants simultaneously. Finally, the identity/conjugation factor maps
are defined on the entire original group, so no subgroup-map extension
assumption is hidden in the reduction to a finitely generated subgroup.

No new gap was found in these specific reductions. The imported tree
facts, their application and novelty still require specialist review.
No code or theorem statement changed; the finite free-group control
suite was not rerun, since it cannot validate this general collapse.
