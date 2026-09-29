# Delayed class26 quadratic: interim audit

Status: constructor and arithmetic passed; native group and period replays
are still running. The three-exception/class26 scope remains unadopted.

The actual weighted group model has weights(1,4), leading terms2a and
3ad_a^6(e), Hirsch length680 and class26. Earlier exceptional coordinates
at offsets3,5 are fixed. Offset7 is the last exception; the full block
7..13 also retains universal kernels9,11,13. The330x273 integer system
has kernel rank4 with adapted steps128,1,4,2. Its complete quadratic
residual at weights25,26 includes the same-factor quadratic term that
can occur at26; the approximate block-column formula is used only through24.

The final291x237 matrix includes all offset14/15 coordinates and has
kernel dimension1. The constant family matrix has240 columns after the
three later block parameters are included. The last-column cokernel rank
is0, so the target has one finite first-parameter family. This is NOT a
surviving unbounded absorbed-quadratic example. All9 polynomial samples,
full block integer lattice, direct planted target and reconstructed witness
pass in Python. Constructor runtime1041.789seconds after the recorded
constant-matrix optimization. Largest certificate75046692 bytes, below
the90000000-byte repository threshold.

Independent GAP replays of complete integer fibers and arithmetic pass
in3.433 and59.578seconds. The native group replay has so far passed the
two witnesses, all273 low-block columns and joint controls, and the complete
integer block lattice. Its remaining quadratic/terminal group checks are
not yet reported as passed. The class26 native quotient is independently
constructed and torsion-free; building its full multiplication polynomials
is still running separately. The group checker currently uses the native
combinatorial collector instead.

Formal universal maps at offsets9,11,13,15 have been specialized in the
Python tensor model. The first three give a full rank3 period lattice on
the later block parameters, leaving the first parameter fixed. A complete
Hermite representative box has bounds

    6402373705728000, 36, 1816214400,

whose product is418610999466884018995200000. Every integer triple in that
box is represented symbolically; this set was not enumerated. The final
one-dimensional integer kernel has period479001600; dividing its integral
translation by the gcd of its coordinates gives a primitive basis. All
479001600 terminal residues must be retained. Python v1 passes; v2 adds
this explicit terminal step and passes. These are two versions of the same
fixture, not two mathematical examples.

The first native period replay times out at180seconds before its first
map-stage print. Its exact source is preserved. The precise stalled
operation was not profiled. Version2 uses a simple pair with one unit
correction in each input at offset7, rather than a full fiber representative;
the universal substitution and constant-prefix assertions apply to both.
It adds stage prints and checks the explicit terminal primitive step.
Version2 is running, and no independent native period pass is claimed yet.

The ignored local GAP workspace quotient.ws is91776352 bytes and is not
committed. SHA256:
9497ee7df283fd6f203d3e47fb5b3481d79862b9fe44d9c6e079da283baa3346.
It is a performance cache, not an omitted mathematical certificate.
Regenerate by making large-artifacts/N8-class26-workspace and running the
recorded command in results/n8-delayed-quotient-c26-v2/process.json with
scripts/probe_n8_delayed_quotient.g. The script saves this cache immediately
after native quotient/rank/torsion checks, before the expensive polynomial
construction. Replays compare its presentation string and defining relations;
the group verifier also has an uncached reconstruction path. GAP4.16.1 and
the same installed package setup are required to load this local workspace.

Separately, a complete successor-compatible Lie-space probe passes in native
GAP and an independent E-index tensor implementation. It yields a uniform
separating-functional lemma for that restricted model, written in
N8-compatible-deformation-functional.md. It does not replace the general
rank-one group reduction or exclude all possible absorption branches.

Eight terminal runs are listed in the checkpoint manifest:7 passed and one
native-period timeout. Earlier class26 timeouts remain in the preceding
checkpoint. Three native jobs are live. Current adopted N8 scope and counts
8 whole/2 partial/0 established novel are unchanged. No push/contact/subagent;
original30September10:04:49UTC deadline unchanged.
