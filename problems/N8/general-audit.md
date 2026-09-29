# Audit of the general N8(b) candidate

29 September 2026, consolidated after the 18:26--18:37 UTC proof review.
The proof is `general-proof.md`. This promotes the same N8 entry from
partial to whole-entry candidate coverage: part(b) is the proposed
general theorem, while part(a) is prior. The tally becomes nine whole
candidates, one partial candidate (G9), and zero established novel
results. All ten entries still await independent specialist review.

## 1. Exact source scope

The complete frozen `sources/raw/probnil.html`, N8's exact fragment,
and its complete linked background paragraph were reread. The archived
rendering `research/statement-audits/N8/statement.png` was actually
viewed again. Part(b) asks for decidability of the single equation
[x,y]=g in every finitely generated free nilpotent group; there is no
class bound. The candidate is uniform in the standard finite rank and
class parameters and constructs factors on a positive answer.

Part(a)'s negative answer in general finitely generated class-two groups
is credited by the background to Roman'kov's 2016 paper. The same
background credits his class-two free-group algorithm. Those prior
scopes are excluded from any new-result interpretation. The frozen
website's older open-status sentence is not proof of present novelty.

## 2. Dependency review

The following arguments were reread independently of the finite test
outputs, and are included in the consolidated proof so a reviewer
need not reconstruct the chronological sequence of partial results.

| Step | Hypothesis checked | Conclusion used |
|---|---|---|
| Leading normalization | Nonidentity target; exact determinant-one pair moves | Noncommuting leading terms of weights p<=q and p+q=d |
| Unequal leading weights | No zero divisors after extension to an algebraic closure | Finite projective fibres; effective rational charts |
| Integral leading factors | Primitive first line and unique second rational factor | All signed scale divisors are retained |
| Equal leading weights | Injective exterior-square map and nonzero rank-two preimage | Every oriented index-h sublattice appears |
| First exceptional kernel | A graded tail algebra with C,U in an actual free basis | Kernel dimension at most one; D,V lie in Lie(C,U) |
| Universal kernels | A different graded tail with C,D in a free basis | Every post-Nielsen kernel has formal two-letter expressions |
| Exact universal periods | Forward and inverse rational powers both have integral Hall coordinates | Reversible pair substitutions; all finite kernel residues |
| Diagonal lemma | Lie hypothesis, characteristic zero, constant exception retained | Nonzero restricted quadratic component |
| Prefix normalization | Fixed rational filtered automorphism, identity associated graded | No lower first-factor components in the separation proof |
| Full-block induction | All earlier affine equations, not only selected directions | Every later column is annihilated by the same functional |
| Integral recursion | Full block lattice and its actual first-coordinate step | Finite prefixes without discarding integral congruences |

For the leading-pair step, the proof uses the projective-fibre argument
from `projective-factor-audit.md`. It does not need the stronger
Klyachko rotation lemma or the earlier at-most-two-direction bound.
The finite-chart rational-point algorithm is written out, including
nonreduced schemes and irrational-point exclusion. The signed divisors
and equal-weight Hermite normalization are the complete version from
`penultimate-target-proof.md`, not the central-only shortcut that can
retain just one scale allocation.

The original homogeneous free-Lie statement was reread in the archived
Bryant--Kovacs--Stoehr (2005) source and its printed p147 was actually
viewed. Only its ordinary Lie-algebra theorem is used. The restricted
positive-characteristic correction elsewhere in that paper is unrelated.

Altassan's 2013 thesis Theorem2.1 (Lazard elimination), Lemma3.2
(homogeneous Shirshov), and Theorem3.3 with its complete proof on
pp.24--25 were reread. Printed p24 was actually viewed again. The
free-basis coefficient hypothesis is satisfied in each constructed
graded tail; it is not being assumed for arbitrary C,D in the ambient
rank-r algebra. Theorem3.3 covers rank greater than the number of
coefficients; rank two is immediate, and countably infinite rank is
explicitly included. Different ambient weights of C,U do not invalidate
the theorem, which applies to arbitrary elements once those coefficients
are free basis elements.

The inner-solution theorem's two-coefficient case is credited to
Remeslennikov--Stoehr (2007). Their repository metadata was rechecked;
the original article PDF remains restricted. No new access to that
full article is claimed. Altassan's accessible full proof supplies
the precise statement actually used.

For universal periods, `universal-gauge-proof.md` was reread: the
finite construction sends [a,b] to the full logarithm of the group
commutator; exponentiated derivations are conjugated by that map;
both signs of the chosen power preserve the integral Hall lattice.
The resulting substitutions are on pairs and need not extend to
ambient group automorphisms. The symplectic-expansion construction is
credited to earlier work of Massuyeau and Kuno as in the prior audit.
The proof needs only finite exact Hall/BCH operations, not a search
cutoff or a claimed practical complexity bound.

## 3. Adversarial checks of the new step

The diagonal polynomial lemma has a general proof: the vanishing
restriction gives cyclic invariance and an averaging identity, and
positive mass-transfer compositions contract the zero-sum hyperplane.
A maximum and minimum on each invariant compact ball force constancy.
No extrapolation from the 44 computed spaces enters that argument.
The scalar D=E_0 exception is real and retained; it is excluded from
the group application by q>p+t. For higher E-letter count, a constant
positional tensor is a power of E_0 and is not a nonzero Lie element.

The rational prefix normalization is used only in the proof. It is
fixed before the block parameters, is invertible in the finite
truncation, and is a linear map on Lie elements. The actual algorithm
does not replace the integer lattice with its rational image. It
finds a separating row directly from the actual finite group matrices.

The projection algebra contains the whole L_(p+t), including arbitrary
particular first-factor components. Using only Q U at that degree
would have been insufficient. Every projected first-factor component
through p+2t has at most one E letter by its weight; this fact is
applied to all parameter directions, not just to homogeneous kernels.

Terms with two Y occurrences in log[x,y] can survive, and are subtracted
as fixed terms rather than discarded. Their variable-dependent terms
begin after the quadratic degree. The class21 fixture explicitly
retains the nonzero constant term (M^2/2)[[a,D],D].

The convolution induction uses the coefficient of the first parameter
in every already-satisfied block equation. It therefore covers all
later columns, including mixtures and universal directions. It does
not assume that an arbitrary fixed deformation separately satisfies
an inner-solution relation. That distinction explains why earlier
unrestricted Lie perturbations could look absorbable.

Once a first-parameter value is fixed, restarting at the next offset
can forget restrictions on higher block coordinates. Every original
solution is retained. A positive answer still checks the complete
original equation, so repeated or unnecessary continuations cannot
produce false positives. The fixed offset strictly increases, giving
termination. The first-exception block requires neither a quotient
by universal translations nor an integer-curve oracle. The earlier
curve arithmetic is preserved as historical work but is no longer
a dependency of this general proof.

No new gap was identified in this internal review. This statement is
not a claim of external mathematical approval or formal verification.

## 4. What the finite checks actually cover

All new checks were completed and locally committed before this scope
promotion. The sources and raw records are retained in the two
diagonal manifests and their linked audits; failures remain visible.

| New fixture | Exact finite scope | Independent reconstruction |
|---|---|---|
| Diagonal Lie spaces | m=1,...,4; E-index sum0,...,10; 44 complete spaces | GAP native free associative algebra and polynomial substitution; all dimensions agree |
| Class17 group, Hirsch59 | 24-by-22 full block, steps2,1; ranks A,[A,B],[A,B,q2]=11,12,13 | Every group column, full integer lattice, all6 quadratic coefficients, 2 witnesses |
| Class18 group, Hirsch76 | Two-E leading term; 32-by-27 block; step12; ranks15,15,16 | Every group column, full integer lattice, full one-parameter quadratic, 2 witnesses |
| Class21 group, Hirsch171 | Nonzero fixed X prefix; 95-by-80 block; steps2,2,1; ranks33,33,34 | Every group column, full integer lattice, all10 quadratic coefficients, 2 witnesses |

The class17 later column is genuinely nonzero modulo the last correction
image; it remains independent of the first quadratic. The class18
quadratic has four E letters. The class21 block includes both exceptional
offsets5,7 and the universal Nielsen offset9. Actual integer scales
and all congruences are kept in each case. Separate GAP arithmetic and
family replays verify complete integer fibers and first-parameter
root decisions for every group fixture.

Across these two checkpoints there are18 new terminal recorded jobs:
15 successful, 3 unsuccessful. The failures are a missing generated
source, an obsolete required CLI option, and an incorrectly selected
zero Hall row while adapting a parameter basis. The latter two exact
sources are retained; the first had no source to execute. Maximum
overlap was3 cores/16GB reserved memory, within the experiment limits.
The largest new certificate is below3MB. Successful stderr logs are
empty. No mathematical jobs were rerun for this textual proof audit.

Earlier evidence remains relevant with its original limits: the
projective-factor solver checks13 finite Lie cases and16 group
witnesses; the penultimate solver retains signed scales and oriented
Hermite branches; universal substitutions and inverse compositions
have native GAP replays, including specialized full period lattices.
Those earlier tests are not relabelled as new general-scope tests.

The full arbitrary-rank branch algorithm, including unrestricted
leading-pair enumeration and all universal residue branches, is not
implemented end to end. Termination and completeness rest on the
written proof. No claim is made that all enormous residue sets from
earlier examples were explicitly enumerated.

## 5. Bibliographic limits and a prior class-two notice

Fresh targeted searches for free-nilpotent single-commutator algorithms
again found the known class-two result and the prior Lie-equation
machinery, but no matching all-class decision theorem. This is a
limited search and does not establish novelty.

One additional primary-source result was identified: Kenneth W.
Weston's January1978 AMS Notices preliminary report, abstract752-20-34,
concerns free nilpotent groups of class2 and rank2. Its indexed primary
abstract asserts an algorithm for single commutator equations in that
group while distinguishing undecidable systems. This is earlier prior
scope, not a general-class result. The AMS PDF open returned403, so
the full issue and its proofs were not read. Metadata and reading
limits are recorded in `literature/N8-Weston-1978-notice.json`.

No established novelty, author confirmation or specialist review has
occurred. No Kourovka mathematics/code was imported in this argument.
The original deadline remains30 September2026 10:04:49UTC; no push,
external contact or subagent was used.

## Sources

* [Archived problem source](../../sources/raw/probnil.html) and
  [publisher background](https://shpilrain.ccny.cuny.edu/gworld/problems/Back2.html#%28N8%29).
* Bryant--Kovacs--Stoehr, *Subalgebras of free restricted Lie algebras*,
  Bull. Austral. Math. Soc.72(2005),147--156,
  [author-hosted PDF](https://archives.maths.anu.edu.au/people/Kovacs/K110.pdf),
  ordinary free-Lie statements on p147.
* Alaa Altassan, *Linear equations over free Lie algebras*, Manchester
  thesis2013, [institutional PDF](https://pure.manchester.ac.uk/ws/portalfiles/portal/54536063/FULL_TEXT.PDF),
  Theorem2.1, Lemma3.2, Theorem3.3 and proof.
* Remeslennikov--Stoehr, *The equation [x,u]+[y,v]=0 in free Lie algebras*,
  Int. J. Algebra Comput.17(2007),1165--1187,
  [institutional record](https://eprints.maths.manchester.ac.uk/994/).
* Kuno, *A combinatorial construction of symplectic expansions*,
  [arXiv:1009.2219v2](https://arxiv.org/abs/1009.2219v2), with the
  earlier Massuyeau credit and reading limits in the universal audit.
* Weston, *Commutator equations over free nilpotent class2 groups*,
  [AMS Notices January1978](https://www.ams.org/journals/notices/197801/197801FullIssue.pdf),
  abstract752-20-34, printedA-75; indexed abstract only.
