# N8: higher leading weights in the actual group recursion

30 September 2026, after f41dd55; original deadline unchanged. The earlier
full-recursion exceptional controls use first leading weight one. The written
argument permits arbitrary leading weights and normalizes their fixed higher
group terms. Test that interface on an actual commutator coefficient, without
changing the solver.

1. In rank three/class six, use two independent weight-two leading factors,
   with nonprimitive scales and higher corrections. This exercises the
   exterior/Hermite leading list above degree one and its integral lifting.
2. In rank two/class eleven put C=[b,a], U=[b,C], D=[C,[C,U]], and take
   g=[C U^2,D]. The leading weights are two and seven; the kernel at offset
   one comes from [U,ad_C^2(U)]=[C,[U,[C,U]]]. Its first quadratic degree
   is eleven. The first factor C already has nontrivial higher logarithmic
   coordinates, unlike the earlier generator-based exceptional fixtures.

Use the complete leading-list solver, not only the planted branch. Keep a
flushed trace, caps from the recorded runner and explicit incomplete outcomes.
A positive decision must give the full target commutator and the intended
branch coverage must be read from the trace. If the lead enumeration times out,
retain that fact; a fixed-leading check would be a separately labeled limited
interface test. Reconstruct useful witnesses and correction blocks in native
GAP. No new problem count or general correctness claim follows from these cases.
