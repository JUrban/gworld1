# G11: horocyclic growth does not yet give whole-group approximation

29 September 2026, active run. No new solution or partial candidate.

## Statement and sources

Read the full archived growth page and G11 background. Viewed the original
rendered paragraphs for all three subparts: the default paragraph capture
contains only (a), so a separate unmodified-page crop includes (a), (b)
and (c). These are retained in `research/statement-audits/G11/`.

Freden--Knudson--Schofield, *Growth in Baumslag--Solitar groups I:
subgroups and rationality*, LMS J. Comput. Math. 14 (2011), 34--71,
[DOI 10.1112/S146115700900028X](https://doi.org/10.1112/S146115700900028X),
separates horocyclic growth from the distribution of cosets. The explicit
convolution in Section 3 treats BS(1,3); it is not a formula for BS(2,3).
Read the introduction, the geometric setup, Section 3's formulas, and the
start of Section 4; viewed printed page 41. No full audit of the later
horocyclic algorithms or the 38-page proof is claimed.

Freden's [2017 conference slides](https://mathshistory.st-andrews.ac.uk/Groups/2017/slides/freden_em.pdf)
were read, with slide 21 viewed. That slide leaves the comparison between
group and weighted-tree growth as a conjecture for q<2p when p does not
divide q. It therefore does not justify replacing group growth by tree
growth here. The slides' other asymptotic assertions are not independently
verified in this pass.

Both PDFs, metadata, extracted text and the specified page images are
archived with prefixes `G11-Freden-Knudson-Schofield-2011` and
`G11-Freden-2017-slides`. These dated sources do not certify current
openness. The earlier Burillo--Elder metric-bound reference remains prior.

## An elementary bound and its limitation

Use G=BS(p,q)=<a,t | t a^p t^-1=a^q>, with 1<p<q, and alpha=q/p.
There is a homomorphism to the affine group of the rational line sending
a to translation by 1 and t to dilation by alpha. It is injective on
<a>, since the image of a has infinite order; it is not asserted to be
injective on G.

If a word of length at most n represents a^m, its t-exponent sum is
zero. Writing h for the t-height before each a-letter, the affine
translation is

    m = sum_(a-letters) epsilon alpha^h,       epsilon in {+1,-1}.

Every such height is at most n/2: an integer height walk ending at zero
uses at least twice its maximum height in t-letters. There are at most
n summands. Thus |m| <= n alpha^(n/2), and the relative ball count in
the horocyclic subgroup satisfies

    |<a> intersect B_G(n)| <= 2 floor(n alpha^(n/2)) + 1.

In particular its exponential limsup is at most sqrt(3/2) in BS(2,3).
This elementary observation is not offered as a new result: it is in the
scope of known distortion and metric estimates.

The observation does not give a bound on the entire group with that
base. The number of cosets grows too, their shortest representatives
vary, and one cannot assume additive word length between a representative
and its a-power tail. In particular, the growth series is not the product
of an unweighted coset series and this one horocyclic series. No uniform
tail estimate for the needed coset sum has been proved here.

Exact finite balls give computable upper approximations to the group
growth constant by submultiplicativity. Without converging certified
lower bounds they do not supply a terminating approximation algorithm.
The successful flow separation used for G9 is not available merely from
the height homomorphism of a Baumslag--Solitar group.

## Outcome

G11(a), (b) and (c) remain unresolved in this run. No growth computation
was launched and no candidate count changes. A future approach must
control the coset contribution or give a different injective construction
with a proved error bound; the horocyclic estimate alone is insufficient.
