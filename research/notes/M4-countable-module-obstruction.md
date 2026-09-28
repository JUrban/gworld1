# M4: full finite-rank proof and the countable module obstruction

28 September 2026, approximately 17:29–17:38 UTC. No candidate solution.

The original question asks whether projective metabelian groups of
countably infinite rank are free metabelian. The full original page,
fragment, background and rendering were inspected in the earlier scope
audit. Its record is `research/statement-audits/M4/render.json`.

## Primary source now obtained

V. A. Artamonov, *Projective metabelian groups and Lie algebras*,
Math. USSR-Izvestiya **12** (1978), 213–223, English translation of
Izv. AN SSSR Ser. Mat. **42** (1978), 226–236.
[Primary source](https://www.mathnet.ru/php/getFT.phtml?jrnid=im&paperid=1711&what=fullteng).
The PDF, retrieval/hash record and extracted text are archived under
`literature/raw/M4-Artamonov-im1711-en.*`. The entire extracted text was
read; printed pages 221–222 were also inspected visually and retained in
`literature/figures/`.

Theorem 4 explicitly assumes finite rank, including the variety of all
metabelian groups at parameter zero. Section 1 associates a projective
module S over E_r=Z[X_1^±1,...,X_r^±1] and a map from S onto its
augmentation ideal. The proof on page 222 uses module freeness and
Theorem 3 to obtain a basis t_i with l(t_i)=X_i−1. Theorem 3 is proved by
induction on the finite number of variables. Both steps matter: an
arbitrary module basis would not by itself provide the required group
generators. This supersedes the earlier access limitation, without
extending the theorem's scope.

## Why the obvious big-module shortcut does not apply

H. Bass, *Big projective modules are free*, Illinois J. Math. **7** (1963),
24–31, is archived under `M4-Bass-big-projectives-1963.*` from
[this copy of the original paper](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/bassbig.pdf).
Theorem 3.1 and Corollary 3.2 require R/J(R) to be left Noetherian.
Corollary 4.5 covers connected commutative Noetherian rings.
The relevant text was read. Lam's author-written survey,
[arXiv:math/0002217v1](https://arxiv.org/abs/math/0002217v1), section 1,
is also archived and was used to locate the precise hypotheses before
checking Bass's original statements.

For the countable Laurent ring

    E = Z[X_1^±1,X_2^±1,...],

the ideals (X_1−1,...,X_n−1) form a strictly increasing chain. Moreover
J(E)=0: any nonzero Laurent polynomial involves only finitely many
variables and has a nonzero evaluation at nonzero integers; reduction
modulo a prime avoiding that value and those integers gives a map to a
finite field on which the polynomial is nonzero. Send every unused
variable to 1. Thus the intersection of maximal ideals is zero.
Consequently E/J(E) is not Noetherian and the cited hypotheses fail.
This does not prove that a countably generated projective E-module can
be nonfree; it only rules out this direct invocation of Bass.

Even a module freeness theorem for E would leave the compatibility with
the augmentation map to prove. No infinite-basis version of Artamonov's
Theorem 3 was established here. Likewise, closing finite supports under
a group retraction need not produce a finite set, so the prior missing
exhaustion by finite-rank projective retracts remains missing.

Searches included the exact countable-rank question, projective modules
over infinitely many polynomial variables, and later Artamonov titles.
No matching full answer was established. No Kourovka argument or code
was imported, and no result count changes.
