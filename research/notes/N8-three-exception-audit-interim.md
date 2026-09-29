# Three-exception group audit: interim checkpoint

Status: supporting evidence only. The at-most-three-exception, leading-degree12
and class26 extensions remain unadopted. Current N8 candidate scope is unchanged.

Two actual weighted group blocks place the third exceptional offset at or before
the first quadratic layer. Weights(1,5),class20 have exceptions4,6,8, a31x28
block, complete integer kernel rank2 and steps16,4; the terminal exceptional
kernel has rank1. Weights(1,6),class23 have exceptions5,7,9, a37x35 block,
complete integer kernel rank3 and steps32,8,2; the terminal map is injective.
Both have later-column cokernel rank0 and one finite parameter family. They
are NOT surviving unbounded absorbed-quadratic branches.

Independent native GAP checks reconstruct the torsion-free weighted groups
(Hirsch lengths65,73), verify63 block columns,24 terminal columns,15 quadratic
samples, complete integral lattices and four actual group witnesses in total.
Separate complete-family and integer-arithmetic replays verify the integer
fibers and all finite decisions, with41 parameter specializations per fixture.

Four exact formal substitutions in weights(1,10),class26 have offsets9,11,13,15.
Polynomial interpolation with proved degree bounds floor(26/t) gives sufficient
integer powers12804747411456000,72,454053600,29937600. These powers are not
claimed minimal. Full homogeneous kernel dimensions at offsets9..15 are
1,0,1,0,1,0,1. Independent GAP verifies both inverse compositions, commutator
preservation,704 image boundary relations,16 inverse equalities, and rejects
a wrong right-Nielsen control. These formal maps have not yet been specialized
to the ambient class26 block or used to certify its full period quotient.

All25 completed runs are retained:10 successful,15 unsuccessful. The latter
comprise one bounded-factorial search cap, nine intentional performance
interruptions, three collector-flag assertion failures, and two incorrect
success-marker configurations. For the last two, the mathematical replay
printed its correct PASS line and exited0; the wrapper expected singular
'integer' instead of plural 'integers'. Corrected runs pass. Superseded GAP
sources are retained with the runs. No mathematical counterexample was found.

GAP's Polycyclic runtime combinatorial flag defaults false. IsWeightedCollector
therefore returned false even after assigning valid nilpotent weights. Setting
that flag alone did not solve the expensive large-exponent collection; native
AddHallPolynomials did. Final independent replays finish in2.8--4.9 seconds.
Installed package sources/docs were read, not modified; no NQ overflow guard
was removed. All defining relations and requested checks remain in place.

A larger class26 constructor and independent quotient preflight are running.
The constructor has reached the first delayed quadratic and full four-parameter
block (330x273,steps128,1,4,2); its complete certificate is not yet available.
The latest diagnostics identify the generic polynomial Smith calculation as
a bottleneck. This is progress evidence, not a passed class26 audit.

Separately, the F38 shortening dependency was reread against Sela2001 at the
specific passages listed in F38-29sep-shortening-recheck.md. No new gap found;
no candidate or novelty promotion. No new full structural-theorem audit claimed.

Peak reserved resources this work period:7cores/32GB; at this checkpoint two
jobs reserve2cores/20GB. No push, contacts, subagents, or parent/preparation
changes. Original48-hour deadline remains30September2026,10:04:49UTC.
