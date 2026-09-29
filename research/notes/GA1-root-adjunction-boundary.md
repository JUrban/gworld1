# GA1: root adjunction and a rejected surface obstruction

28 September 2026, approximately 22:33–22:36 UTC. No new solution.

**29 September update:** the later
[fourth-power obstruction](GA1-prior-fourth-power-obstruction.md)
settles the nonabelian GA1 case negatively as an immediate consequence
of Brady–Ciobanu–Martino–O Rourke (2009). The earlier failed surface
obstruction below is preserved; it is compatible with that theorem.

The exact original GA1 fragment asks whether the free Q-group acts freely
on some Lambda-tree. The ordered abelian length group is unrestricted.
Read the fragment again in this pass; no new visual statement audit is
claimed here.

A possible negative route was to use a nonorientable genus-three surface
subgroup arising from root adjunction. Its failure to be fully residually
free, or to act freely on an R-tree, does **not** obstruct the requested
action. The distinction is settled directly by prior results:

- Martino–O'Rourke, *Some free actions on non-archimedean trees*,
  Theorem 3.1 proves that
  `<a,b,x_1,...,x_n | a b a^-1 b^epsilon = w(x_1,...,x_n)>`
  is Z^2-free, except when epsilon=1 and w=1. Corollary 3.3 includes
  every closed surface group except the projective plane and Klein
  bottle, hence includes the genus-three nonorientable case.
- Their *Free actions on Z^n-trees: a survey*, Theorem 4.3 explicitly
  gives that genus-three group as Z^2-free while every homomorphism
  from it to a free group has cyclic image.

The first paper's proof was read through Theorem 3.1 and Corollaries
3.2–3.3. It splits an even-length word into equal halves, changes basis,
and applies a length-matched HNN combination theorem; the odd-length
case embeds into an even-length one. In particular, root adjunction
`<a,b,c | [a,b]=c^m>` lies in this prior positive family. This is useful
negative evidence against the proposed obstruction, not a new partial
answer to GA1.

The same papers' cyclic-amalgam combination theorems assume the edge
subgroup is maximal abelian in both factors. They cannot be applied
directly to a general root adjunction

    G *_(u=t^m) <t>,       m>1,

because `<t^m>` is properly contained in the cyclic factor. The special
one-relator theorem does not supply a general closure-under-roots result.
No such missing closure theorem was proved in this pass. Nor was a
compatible direct-limit free action constructed. Thus this line leaves
GA1 unresolved and should not be extended by simply invoking the Bass
combination theorem.

## Sources and reading limits

Both author-hosted PDFs were archived with retrieval metadata:

1. https://mathematics.mtu.ie/contentfiles/some-free-actions.pdf
   `literature/raw/GA-MartinoORourke-actions.pdf`
   SHA-256 `8b18851b24fb1ec60d330e5baab780e1cc9be7aaf0de3ca43e623863bd6208b2`.
   Read sections 2.1–2.4, Theorem 3.1 and its proof, Corollaries 3.2–3.4,
   and the stated hypotheses of Theorem 4.3. This is the 2003 manuscript
   of the paper published in Journal of Group Theory 7 (2004).
2. https://mathematics.mtu.ie/contentfiles/zn-survey.pdf
   `literature/raw/GA-ORourke-survey.pdf`
   SHA-256 `2ad687976504c83e9463286aad6af61cc6990360786af32b8381f10c99450bc7`.
   Read title/intro, Corollary 3.3, Theorems 4.2–4.4 and Questions
   4.6–4.10. No assertion that this historical survey describes the
   complete current status of its questions.

Queries included the exact first-paper title, `free Q-group tree-free`,
`free Q-groups Lambda`, and `Q-completion trees group free`.
The earlier affine/isometric distinction remains in force. A search
result announcing affine actions from residual torsion-free nilpotence
was not treated as an isometric-action theorem. No computational search
or new research claim was added.
