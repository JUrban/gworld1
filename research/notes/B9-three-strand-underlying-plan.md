# B9: exclude the next underlying strand number

30 September 2026, within the original window. After the N8 group-block
supplement, consider the total-exponent-two parameter
A=I1(u) S(I1(v)) in B3, where u,v are special. The existing support
argument gives m(u)=m(v)+1 for nontrivial v. It already handles v in B2.

New bounded target: exclude m(v)=3 for all special u, including the
unknown exponent-two sector of special B4. The known B3 classification
leaves v=s^2 t^-1 or ts, and u must have four strands. Its exponent
is 1,2 or3. The exponent-one and -three sectors are already classified;
at exponent two, the identity epsilon(u)=nu(pi(u)) restricts its
permutation to three explicitly enumerable permutations in S4.

Test the six latter permutation possibilities in the full parameter
I1(u) S(I1(v)). Every permutation of a B3 braid fixes positions4,5.
For the known exponent-one/-three possibilities, test the same necessary
condition and use an exact last-column or faithful-action obstruction
for the one expected survivor u=tau3,v=tau2. In that case A in B3
would require u^-1 I1(v) in B3, which fixes the fourth basis vector in
Burau and the fourth free generator in the faithful Artin action.

Use separate exact Python and native GAP constructions. These exhaust
only the finite permutation restrictions and explicitly known sectors;
they do not enumerate the unknown special B4 sector or higher-strand
underlying inputs. The universal deduction uses the prior epsilon/nu
theorem, support argument and small-strand classification. No new term
height or word-length search is planned. Retain every run and exact
input. B9 remains partial even if this exclusion succeeds.
