# N8: full negative control above first leading weight one

30 September 2026, after 684c115. The preceding goal turn made concrete
progress through B9 reductions, G9 bounds/credit, and N8 higher-weight tests.
The original deadline and clean committed checkout were revalidated.

The class-eleven higher-weight positive fixture gives scalar obstruction
T^2-2T at its first weight-(2,7) branch. Its separating functional is the
114th coordinate of the degree-eleven Hall layer (zero-based index 113).
Multiply the target by the square of that central Hall generator. For the
same normalized branch the expected polynomial is T^2-2T+2, with no real
roots. That observation alone does not make the target a noncommutator.

Run the unchanged complete solver through all four possible normalized
weight types (1,8), (2,7), (3,6), (4,5). Preserve a positive witness if
another branch succeeds, rather than declaring the first obstruction global.
Retain every leading list and rejection trace. Use one CPU/eight GB and
240 seconds; a timeout is incomplete. If all branches reject, reconstruct
their actual group blocks and quadratics in GAP. This is a targeted
negative interface test, not proof of the candidate's general completeness.
