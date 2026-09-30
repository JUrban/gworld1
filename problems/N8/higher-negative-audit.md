# N8: a complete higher-weight negative control

30 September 2026, during the original experiment. This extends the
[higher-leading positive checks](higher-leading-group-audit.md) without
changing the solver or the proposed theorem. It is finite implementation
evidence; the general completeness argument still requires review.

In rank two and class eleven use the positive target

```
C=[b,a], U=[b,C], D=[C,[C,U]], g=[C U^2,D].
```

The previous exceptional branch has scalar obstruction T^2-2T. Its
separating functional is the coordinate with zero-based index 113 in the
degree-eleven Hall layer. Let h be that central Hall generator, using the
exact dictionary in the certificate, and set g_negative = g h^2. The
literal input word, dictionary, original target and source hash are
retained. The Magnus calculation checks this product before solving.

The unchanged complete solver considers all normalized weight types
(1,8), (2,7), (3,6), (4,5). The first, third and fourth have empty leading
lists. The (2,7) list has both signed integral pairs. Each leads to a
99-by-32 exceptional block at offset one, with a one-dimensional full
integer kernel and unit adapted step. Their scalar obstructions are

```
T^2-2T+2 = (T-1)^2+1,
T^2+2T+2 = (T+1)^2+1.
```

Both have empty integer root lists, so the solver rejects all branches.
This tests rejection of an entire input, rather than rejection of only
the branch used to design it. The projective leading-list computation
and its completeness remain dependencies of that conclusion.

The [GAP wrapper](../../scripts/check_n8_higher_negative_gap.g) compares
both exported kernels with native integer nullspaces via Hermite normal
forms, verifies their affine points and unimodular adapted changes, and
checks the full trace and the two rootless polynomials. The existing
[native group checker](../../scripts/check_n8_general_solver_gap.g) then
reconstructs all 64 correction columns in two blocks, both right sides,
both quadratics at twelve total integer samples, all later correction
columns and both complete integer root lists in GAP/nq. It does not
independently recompute the projective leading lists, nor does sampling
alone prove the general polynomial-degree assertion.

The Python and GAP jobs pass in 11.107 and 6.940 seconds respectively,
each using one CPU and an 8 GB per-process limit. They run sequentially,
have empty stderr, and retain successful markers, terminal receipts and
log hashes. The [certificate manifest](../../research/certificates/N8-higher-negative-v1/manifest-v1.json)
binds their exact inputs, implementations, dependencies and outputs.
No new candidate, novelty conclusion or outside review is claimed.
