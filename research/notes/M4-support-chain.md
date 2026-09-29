# M4: explicit obstruction to closing finite coordinate supports

29 September 2026. **Failed reduction made explicit; no answer to M4.**

The original M4 question concerns countably infinite rank projective
groups in the variety of all metabelian groups. The full original HTML,
background, exact fragment and archived rendering were checked again.
The finite-rank theorem and the two missing infinite-rank steps are
documented in [the earlier module audit](M4-countable-module-obstruction.md).

Here is a concrete reason that one cannot obtain a finite invariant
coordinate free factor merely by repeatedly adjoining the supports of
images under a retraction. It applies even after diagonalizing the
induced map on abelianization, as in the beginning of Artamonov's proof.

Let M be the free metabelian group on x_i,y_i, for integers i>=0.
Use [a,b]=a^-1 b^-1 a b and put

    h_i = x_i [y_(i+1),x_(i+1)],
    pi(x_i)=h_i,     pi(y_i)=1.

This specifies an endomorphism. For every i,

    pi(h_i)=h_i [1,h_(i+1)] = h_i,

so pi^2=pi. In particular pi is a genuine retraction onto its image H,
not an arbitrary endomorphism chosen to have expanding supports. On
abelianization it fixes every x_i and kills every y_i; the induced
projection is already diagonal.

Suppose S is a subset of this fixed basis such that the coordinate
subgroup M(S) is pi-invariant, and suppose x_i belongs to S. Then
h_i belongs to M(S). It follows that both x_(i+1) and y_(i+1) belong
to S. Indeed, if either were missing, the coordinate retraction killing
that missing generator and fixing all others would fix every element
of M(S), but would send h_i to x_i. These two elements are distinct:
the commutator [y_(i+1),x_(i+1)] is nontrivial, as witnessed by sending
these two generators to I+E12 and I+E23 in UT_3(Z). This is a
metabelian image, so the witness applies to M.

Consequently S must contain x_(i+1),x_(i+2),... and is infinite.
Any finite invariant coordinate subgroup therefore contains only
y-generators and has trivial image under pi. There is no exhaustion
by finite invariant coordinate free factors with nontrivial images
in this basis. Idempotence and diagonal abelianization do not make
the proposed support-closure procedure terminate.

**This example is not a nonfree projective group.** In fact H is free
metabelian of countable rank. Let M_X be free metabelian on x_i alone,
and let j:M_X->M send x_i to h_i. Killing all y_i defines q:M->M_X
with qj=id. Hence j is injective and H is exactly its image. The
argument does not rule out a different finite-stage construction or
a suitable change of coordinates for general projective groups.

## Check and scope

`scripts/check_m4_support_chain_gap.g` uses ordinary free-group words
to check the splitting and idempotence identities for nine successive
lifts, and an exact integer UT_3 representation for the nontrivial
commutator. Free-group identities descend to the metabelian quotient.
The finite model fixes its terminal x-generator and kills all y's.
It therefore has a boundary; its support closure is not evidence for
the infinite conclusion, which is proved symbolically above.

This supplies an explicit control for a previously identified failed
strategy. It does not close either the module-freeness or the
augmentation-compatible-basis gap in M4. No novelty claim, solution
count, imported Kourovka argument, or external specialist review is
attached to it.

The recorded run `m4-support-chain-gap-v1` passed in 1.925 seconds at
one core / 4 GB, with empty stderr, exit zero and the expected marker.
It checks 20 idempotence identities, nine lift/splitting identities and
the integer matrix separator. The source and logs are included in
`research/certificates/M4-support-chain/manifest.json`.
