# GA1: negative answer from a prior power-equation theorem

29 September 2026, approximately 03:15–03:20 UTC.
**Prior consequence; excluded from new-result counts.**

For a nonabelian free Q-group the answer to GA1 is **no**. This follows
immediately from Brady–Ciobanu–Martino–O Rourke (2009). In fact every
divisible group acting freely without inversions on a Lambda-tree is
abelian. No finite-generation or restriction on the ordered abelian
length group is needed.

The complete original `sources/raw/probact.html` was read and the actual
GA1 paragraph rendered and viewed. It asks about the free Q-group F^Q;
no additional background or named subpart is linked. We use the usual
free-action convention excluding inversions.

## Prior theorem and its short consequence

N. Brady, L. Ciobanu, A. Martino and S. O Rourke,
*The equation x^p y^q = z^r and groups that act freely on Lambda-trees*,
*Transactions of the American Mathematical Society* **361** (2009),
223–236, DOI `10.1090/S0002-9947-08-04639-4`, prove that in a
Lambda-free group the equation x^p y^q=z^r, for p,q,r>=4, forces
x,y,z to commute. The [author-hosted PDF](https://math.ou.edu/~nbrady/papers/trees.pdf)
is archived. Its introduction calls the result Theorem 3.2; the body
numbers it Theorem 3.6. The published bibliographic record uses Theorem
3.2. This numbering difference does not change the stated hypotheses.

Now let D be divisible and Lambda-free, and choose arbitrary a,b in D.
Choose fourth roots x,y,z in D with

    x^4=a,  y^4=b,  z^4=ab.

Then x^4 y^4=z^4, so the prior theorem gives xy=yx. It follows that
ab=x^4 y^4=y^4 x^4=ba. Since a,b were arbitrary, D is abelian.
Surjectivity of the fourth-power map alone suffices; uniqueness of roots
is not needed for this inference.

A free Q-group on at least two generators is divisible and nonabelian,
so it cannot have the action requested in GA1. Nonabelianness follows
either from the usual embedding of the initial free group, or directly
from its universal property: the rational Heisenberg group is a uniquely
divisible nonabelian group, and two free generators can be sent to
noncommuting elements in it.

For clarity about the unstated rank: the free Q-group of rank one is
the additive group Q and acts freely by translations on the Q-line.
Rank zero is trivial. Thus the substantive nonabelian case is negative,
while the elementary ranks zero and one are positive.

## Why this was missed in the earlier pass

The preceding note correctly rejected the genus-three nonorientable
surface as an obstruction: the exponent-two group is tree-free. The
power-equation theorem distinguishes exponents at least four. It rules
out further root adjunction, rather than contradicting the earlier
surface example. The previous note is retained with a dated update.

The present exploration considered small translations arising from
arbitrarily deep roots. A targeted search for the Lyndon–Schützenberger
equation in tree-free groups then located the explicit 2009 theorem.
No new general tree argument is needed or claimed. The result is a
direct consequence of prior work, regardless of whether GA1 itself is
named in that paper; the unstarred publisher entry is not evidence
that it remains open.

## Evidence and reading limits

- The full author PDF is archived with URL, retrieval time and SHA-256
  `61cb83a7f54882f6f24a5078d4b76a542fbb7d4ff56c82bdce59a6a30012ff43`.
  Its introduction and main proof (PDF pages 10–14) were read as text;
  pages 1, 11 and 13 were actually viewed, including the stated theorem
  and the delicate exact-axis-overlap case. The underlying tree lemmas
  were read in part, not independently formalized. The CAT(-1) section
  is not needed or claimed as audited.
- Primary 2007 seminar abstracts led to the paper. The theorem itself,
  rather than those announcements, is the dependency. Direct access to
  the AMS landing page was blocked; the author-hosted full text supplied
  the mathematical statement and proof.
- The first statement renderer invocation failed on a missing browser
  shared library. Re-running with the already documented local browser
  library path succeeded. The actual screenshot and frozen source hash
  are under `research/statement-audits/GA1/`.

There is no mathematical computation or new candidate to verify here:
the displayed root argument is a direct deduction from the published
theorem. The exploratory small-translation idea is not counted as an
independent proof. No Kourovka material was imported.
