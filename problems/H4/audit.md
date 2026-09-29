# H4 candidate audit

28 September 2026. Candidate negative answer under the standard uniform,
explicit-word input/output convention. This is same-agent review with
independent computational representations, not outside specialist review.
Novelty is provisional.

## Statement and conventions

Read all of `sources/raw/probhyp.html`, the exact H4 paragraph and its
rendered screenshot. H4 imposes no torsion-free, infinite, nonelementary
or fixed-generating-set restriction. It asks for a polynomial-time
conversion from a finite presentation of a hyperbolic group to a Dehn
presentation of that group. There is no linked H4 background section.

The same question is printed on p.25 of Kharlampovich's IAS lecture
slides; that page was read and visually inspected. The standard Dehn
definition was checked in Bridson, Definition 1.4, printed p.128, and
Ciobanu--Elder, Lemma 13, printed p.110:7. The latter page was also
visually inspected. The sources allow the usual finite collection of
strict shortening rules. Their results for a fixed group with a Dehn
presentation already supplied do not give uniform conversion bounds.

The theorem permits a different output generating set. It measures
explicit words, including expanded relators, and allows binary generator
indices. It does not assert a lower bound for a compressed output grammar
or an arithmetic expression describing relators. The input uses only
explicit square relations; its length estimate uses no hidden compression.

## Proof checks

The decisive arguments are in `proof.md` and are independent of the tests:

- Prefix-pattern states give a polynomial bound in the size of every
  Dehn presentation, including presentations with redundant generators.
- The forbidden-factor language is closed under factors and contains
  every geodesic. An accessible automaton cycle would give arbitrarily
  high powers of one word in that language. Finite order supplies a
  nonempty identity word, contradicting the defining Dehn property.
  No inference from the language being regular alone is used.
- Acyclicity bounds all accepted word lengths, hence the number of group
  elements, by `(2m)^((m+1)^2)`.
- Eliminating the auxiliary generators gives the displayed metacyclic
  presentation. Conjugation forces `x^(2^(2^n)-1)=1`; its odd order makes
  `<x>` normal. The explicit semidirect product supplies the matching
  lower order bound. This proves finiteness, not merely a finite quotient.
- Every finite group meets the hyperbolicity promise. The exponential
  lower bound holds for every output presentation of that abstract group.
  It therefore excludes polynomial time through output length alone,
  without P versus NP assumptions or a search-complexity conjecture.

## Bounded implementation checks

`h4-output-size-v1` passed in 0.22 seconds, with empty stderr:

- 31 cyclic Dehn presentations of orders 2 through 32, with exact longest
  irreducible-word length, irreducible-word count and residue coverage.
- A non-Dehn presentation of C2 cubed, with the irreducible identity
  `(abc)^2`, and an infinite cyclic control. Both have accessible cycles;
  neither is incorrectly treated as a finite Dehn language.
- Ten members of the short input family, n=1,...,10: presentation sizes,
  exact affine multiplication and defining relations checked. Breadth-first
  enumeration for n<=3 reaches the predicted 6,60,2040 elements. These
  finite tests do not replace the arbitrary-n order proof.
- 10,759 comparisons between the prefix automaton and an independent
  direct forbidden-substring scan on three finite alphabets.

`h4-output-size-gap-v2` passed in 6.14 seconds with empty stderr. GAP
independently constructed affine permutation groups of orders 6,60,2040
and 1,048,560, checked generator orders and every defining relation, and
computed the order of the finitely presented group separately for the
first three cases. Version one passed in 5.99 seconds but emitted four
global-variable syntax warnings; its logs and exact source are preserved.
Version two places the variables in a declared local function. Repeated
checks of the same fixtures do not add distinct mathematical examples.

All jobs used one core and a 4 GB per-process bound. Commands, actual
exit statuses, timestamps and stream hashes are in their `process.json`
records. The data are in `research/certificates/H4-output-size/`.

## Sources, novelty and reading limits

- [Bridson, *Non-positive curvature in group theory*](https://people.maths.ox.ac.uk/bridson/papers/BATH97.pdf):
  read Definition 1.4 and the surrounding shortening algorithm; also
  Theorem 1.21 and its outline. The long survey was not fully audited.
- [Ciobanu--Elder, ICALP 2019](https://drops.dagstuhl.de/opus/volltexte/2019/10686/pdf/LIPIcs-ICALP-2019-110.pdf):
  read and viewed Lemma 13 and its surrounding conventions, not the full
  equation-solving proof. This supplies a primary-source check of the
  Dehn convention only.
- [Kharlampovich, IAS lecture 4](https://www.math.ias.edu/files/wam/OKpresentation_Princeton4.pdf):
  read and viewed the final problem slide. Its repetition of H4 is
  historical evidence, not proof of current openness.
- [Burdges's 2012 question and user6976's answer](https://mathoverflow.net/questions/94213/asymptotics-of-the-number-of-required-dehn-relators-in-hyperbolic-groups):
  prior firsthand suggestions of finite-group examples for Dehn-relator
  lower bounds, and an expander-based alternative. These are credited as
  related ideas; the answer does not provide the present automaton bound
  or short metacyclic family. No identity for the displayed username is
  assumed. The proof here does not depend on those suggestions being true.

Bounded searches included `Dehn presentation polynomial hyperbolic`,
`Dehn presentations finite groups size`, `Dehn presentation double
exponential`, `Dehn presentation output size`, and `Dehn presentation
polynomial time negative`. No matching complete result was found. This
elementary argument may already be known or folklore; specialist novelty
review remains necessary. There is no claim of established novelty.

No Kourovka argument was imported and no outside reviewer, subagent,
contact or push was used. The candidate is a negative answer to the
whole H4 entry under its standard explicit uniform interpretation.
The later [infinite-input audit](infinite-input-audit.md) records a
stronger bound and an extension to infinite non-elementary virtually
free input groups, using the classical torsion-conjugacy lemma. It is
the same candidate and retains the explicit-output and torsion qualifications.
