# F34: coverage reconciliation, not a new result

29 September 2026. The existing candidate algorithm covers all of F34(a)
in every finite rank. Part (b) has a prior negative answer, credited to
Aaron Clark and Richard Goldstein, *Stability of Numerical Invariants in
Free Groups*, Communications in Algebra 33 (2005), 4097–4104,
[DOI](https://doi.org/10.1080/00927870500261405).

The full 2005 paper has still not been obtained or audited; the publisher
landing-page retrieval failed. We rechecked the explicit attribution in
the frozen website background. The already archived primary 2025 paper
by Dinowitz–Koch-Hyde–O'Connor–Olive also uses the precise equality
PP_r intersect F_n = PP_n for r>=n in the proof of Theorem 6.2, crediting
Clark–Goldstein as reference [4]. Actual PDF page20 was read and viewed;
the image is `literature/figures/F34-stability-scope.png`.

There is also a complete elementary derivation of that prior conclusion
from the graph lemma already written in `problems/F34/part-a-proof.md`.
If w in F_n becomes positive after an automorphism alpha of F_m, compose
the standard inclusion i:F_n->F_m with alpha. This composition is
injective and has positive image of w. In the finite core graph of its
image subgroup, orient each geometric edge by its positive ambient
label, choose a spanning tree and orient the non-tree basis accordingly.
The positive closed path for alpha(i(w)) collapses to a positive word
in that basis. Pulling the basis back through alpha i makes w positive
in a basis of F_n. Thus w was already potentially positive in F_n.
The converse extends an automorphism of F_n by fixing the extra basis
letters. The identity satisfies both properties under the website's
convention and causes no exception. This is a recovery of the known
result, with no originality claim.

The earlier reports counted F34 as partial because only part (a) was a
candidate new answer. They counted F38 as whole-entry coverage once its
parts (a) and (c) had candidates, despite its part (b) likewise being
prior. Apply the same coverage convention to both: F34 now belongs in
whole-entry candidate coverage, explicitly composed of candidate (a)
and known (b). No newly solved subpart, new theorem or additional entry
has been added. Eight whole-entry candidates plus two partial entries
still total the same ten entries; zero results are established novel.

The old proof, audit and hash manifests are preserved as dated records.
The original statement rendering was actually re-viewed in this check.
No mathematical code changed and no mathematical tests were rerun.
Two attempted PyMuPDF imports failed because it is not installed; the
existing pdftoppm rendered the cited PDF page successfully. This was
source-reading infrastructure, not a failed mathematical computation.
