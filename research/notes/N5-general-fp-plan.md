# N5: promised-nilpotent finite-presentation interface

After 17075b3, add a command accepting an ordinary finite presentation with
an explicit nilpotency promise, without a class bound. The nq manual states
that omitting the class computes the largest nilpotent quotient when one
exists. Under the promise this quotient is the input group. Do not infer the
promise from the quotient, or treat successful stabilization for an arbitrary
group as a proof that its kernel is trivial.

Handle the zero-generator presentation directly. Compute the abelianization
first and handle its cyclic cases directly: a finitely generated nilpotent
group with cyclic abelianization is cyclic. This also avoids the installed
nq cyclic/high-class assertion encountered in the earlier class-two work.
For other inputs use unbounded-class nq under the overall recorder timeout.

Verify the conversion on known native groups of classes three/four, mixed
torsion, alternate presentations and a redundant-generator Tietze extension.
Connect the resulting native pipeline, bind reconstructed presentation and
generator images across stages, and return factor words in the original
presentation. Check all positive native factors before reporting a result.
Exercise positive and negative standalone commands and an omitted-promise
rejection. Preserve failed sources and outputs; reserve one CPU/eight GB,
with 180-second initial limits. No change to result count or novelty status.
