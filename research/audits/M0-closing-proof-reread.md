# M0 closing proof audit

30 September 2026, approximately 02:38--02:40 UTC. Same-agent review
within the original window. No new gap was identified; the all-rank
candidate still awaits specialist correctness and novelty review.

Read the full main proof and original audit, terminating Kronecker
constructor supplement, and integral-flow inverse supplement. Reread
the complete original metabelian/free-group HTML, M0's reference to F3,
and F3's background. Actually viewed both original statement images.
Reread the introduction and Lemma 1 in the archived Gupta--Gupta--Roman'kov
paper and viewed printed page 517. The fresh source audit concerns that
square-Jacobian criterion and conventions, not the whole paper or a new
literature-status search.

The abelianization argument uses preservation of every primitive vector,
not just the standard basis. A nonzero finite-field kernel vector has a
primitive integral lift through elementary matrices. This forces a
unimodular abelianization and permits IA normalization by an actual free
automorphism. All later changes of basis preserve the original
primitive-word hypothesis.

A nonunit Laurent determinant with augmentation one retains at least
two monomials modulo a suitable prime. A maximal ideal then gives a
finite field with nontrivial character. Integral changes of character
exponents need only give a gcd coprime to the cyclic image order, not
gcd one over the integers. The chosen surviving character value still
generates the image and the residue field. Because the map is IA, the
evaluated change of Fox matrix is a similarity at the same character;
the proof does not discard a semilinear twist for a non-IA map.

The Fox identity puts the singular kernel in the first n-1 coordinates.
Each required transvection there is the Jacobian of an explicit **free**
automorphism, whose appended word omits the changed generator. Its
conjugator-coordinate derivatives cancel because the other letter has
character one. These automorphisms preserve the character, so evaluated
Jacobians multiply without twisting. For n at least three the elementary
matrices reach every nonzero vector in that subspace. Rank two uses the
kernel line directly; ranks zero and one are separate. Thus an actual
primitive word, rather than an arbitrary unimodular column, detects the
singularity. Only the necessary Fox condition for a primitive element
is used here.

The classical square criterion matches the stated left-column convention:
right rows are obtained by transpose, Laurent inversion and invertible
diagonal monomial factors. The integral-flow supplement also supplies
its sufficiency directly. The abelian covering graph has fundamental
group F-prime; zero loop chain is exactly F-double-prime. Every finite
integral cycle splits into directed closed trails, and connectors cancel
even for disconnected support. Consequently all columns of the inverse
IA Jacobian are realized by actual words. Both compositions have identity
abelianization and Jacobian and are identity by this faithful model.

In the effective version, base-B exponents separate the determinant's
finite support after coordinate shifts. The chosen prime preserves the
constant and leading coefficients; g(1)=1 excludes the unit character.
The resulting finite extension and explicit Nielsen basis give a
terminating construction, albeit potentially enormous. Its finite tests
and the flow checks are not an all-input complexity bound. No rerun was
needed, and neither the reproved classical criterion nor the already
known low ranks add to the result count.
