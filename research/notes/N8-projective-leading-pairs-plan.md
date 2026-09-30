# N8: complete leading pairs by the general proof's projective route

30 September 2026, within the original experiment window. This is a
verification/implementation supplement to the existing N8(b) candidate,
not a new result or an implementation of its full arbitrary-class recursion.

The written general proof retains every signed divisor of the content of
the second factor after primitive normalization of the first. The earlier
projective-chart implementation retains only the primitive pair, which is
sufficient for its central-target purpose. Implement the complete list
using that implementation's exact rational points, with all signed scales.
For equal weights use the existing exterior/Hermite construction. Do not
invoke the stronger block-quadratic/Klyachko routine in the new route.

Compare complete unequal-weight lists, including signs, with the separate
older block-quadratic implementation on small structured examples. Include
multiple rational directions, a repeated direction, irrational directions,
and positive contents with several divisors. Include the equal-weight
index-six lattice boundary with twelve oriented Hermite representatives.

The principal new control is an actual noncentral target in rank two,
class five: with z=[b,a] and d=[z,a], try

    g = [a^2 z, d^3].

Its leading type is (1,3). Compute every leading branch's full final
integer correction system. Determine whether retaining primitive first
factors alone loses the positive solution. This is a hypothesis to test,
not a recorded outcome. If confirmed, retain every failed primitive branch
and a successful nonprimitive branch, and independently reconstruct their
central correction-subgroup membership in GAP/nq. If the hypothesis fails,
record that failure before changing the example.

Use recorded bounded jobs, preserve unsuccessful sources and outputs,
inspect stderr and the mathematical assertions, and bind exact artifacts.
Reread the original N8 page/paragraph and inspect its retained rendering.
Keep the ten whole-entry coverage candidates, two partial candidates and
zero established-new-result counts unchanged.
