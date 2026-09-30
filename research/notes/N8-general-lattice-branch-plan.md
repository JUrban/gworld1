# N8: remaining integral-block implementation branches

30 September 2026, after 59b4726. The previous goal turn made progress:
complete N8 recursion, the word command and current scope reconciliation.
The original deadline remains 10:04:49.670358 UTC.

The first integration suite had varying exceptional parameters of unit step.
Its controls did not exercise the branch where the longer affine block fixes
that parameter, or a nonunit first-coordinate step after the unimodular change.
These are distinct implementation paths in the candidate's integral recursion.

Use rank two/class ten, U=[b,[b,a]], D=[a,[a,U]], and the delayed offset-two
family. Add the fixed earlier prefix [b,a] to the first factor; separately use
leading scales two and three. Run only these targeted controls under one
CPU/eight GB/180 seconds. Record every trace, whether or not the hoped-for
branch occurs. A positive outcome alone is not evidence that the intended
branch was exercised. Reconstruct any useful certificates in native GAP and
preserve failed probes. Do not change the general solver to fit these examples.

After this focused concern, refresh the artifact/resource inventories; they
currently predate the recent N5/N8 implementation work. This is still an interim
checkpoint. The original deadline freeze and final report remain outstanding.
