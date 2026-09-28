# Braid entries: prior answers and exact scope

28 September 2026, approximately 14:02–14:15 UTC. The complete frozen
`sources/raw/probBr.html` and the B3, B8 and B13 rendered paragraphs were
read and inspected. Source hash:
`775c0308e0e9e5dd3927bac2f43d0f193bd699c50fbedc93a0f10db0da6b45e2`.
These are bibliographic exclusions, not discoveries of this experiment.

## B3

Vasudha Bharathram, Joan S. Birman and Tara E. Brendle,
[*The Burau representation of the braid group is faithful for n=4*](https://arxiv.org/abs/2607.05283v2),
first submitted 6 July 2026, revised 14 September 2026, states precisely
the positive answer as its Main Theorem. Archived v2 PDF, metadata and
derived text; inspected the first theorem page visually and read the
introduction and proof strategy. The arXiv record describes v2 as minor
corrections and improved exposition; it is not marked withdrawn.

This is a prior preprint result. The full geometric proof has not been
independently audited here. The question is therefore excluded from
our discovery portfolio without representing this bibliographic check
as an independent validation of the theorem.

## B8

Jean Fromentin,
[*Every braid admits a short sigma-definite expression*](https://ems.press/content/serial-article-files/31799),
J. Eur. Math. Soc. 13 (2011), 1591–1631, Theorem 1, supplies the bound
`6(n-1)^2 ||beta||_sigma`. Hence `c(n)=6(n-1)^2` works, with the usual
empty-word treatment of the identity.

There is a convention change: Fromentin uses the *maximal* generator
index; GroupWorld uses the *minimal*. Apply the theorem to the image
of beta under the braid automorphism `sigma_i -> sigma_(n-i)` and map
the resulting word back. This preserves lengths and converts the
required sign condition. The length of the shortest word is at most
the input length N, so the theorem has exactly the needed bound.

The literal wording omits the identity exception: no nonempty definite
word represents 1. This familiar convention issue is not used to claim
a new negative solution. Archived the full published paper; read the
opening theorems and final length estimate (Theorem 6.13), and viewed
printed p.1591. A complete new audit of all intermediate proofs was
not performed.

## B13

Mark C. Bell and Saul Schleimer,
[*The word problem for the mapping class group in quasi-linear time*](https://arxiv.org/abs/2511.02459),
submitted 4 November 2025. Remark 1.7 explicitly answers GroupWorld B13:
for each fixed strand number r, word length N is handled in
`O(N log^3 N)` time. Remark 1.6 explains the pointwise-boundary variant
needed for braid groups. The paper specifies a multitape Turing model;
its divide-and-conquer proof of Theorem 3.14 uses the intersection
algorithm of Theorem 6.18.

Archived and read the introduction, relevant conventions, and the
divide-and-conquer proof; viewed p.2 containing the exact B13 statement.
The full train-track proof has not been independently audited here.
The claim is for fixed r, not a rank-uniform complexity bound with r
charged as part of the input. This is prior work, not a new algorithm
produced in the run.

## B12 remains separate

A search found Mangioni–Sisto, arXiv:2602.23275v2. Its Theorem B(1),
checked in the primary HTML full text, gives a non-elementary hyperbolic
quotient of B4 receiving only virtually cyclic images from Bn for n>=5.
This does not rule out other non-elementary hyperbolic quotients of Bn.
Nor does an acylindrically hyperbolic quotient settle the word-hyperbolic
question. No B12 answer is inferred.
