# Audit of the penultimate-layer N8 candidate

28 September 2026. Internal audit only; independent specialist review
has not occurred. This extends the existing partial N8(b) candidate and
does not create an additional entry in the tally.

## Scope and completeness checks

- Original N8 HTML, fragment and rendered statement were inspected in the
  earlier audit, retained at `research/statement-audits/N8/`. The question
  concerns every finitely generated free nilpotent group, so the present
  target restriction is explicitly partial.
- A nontrivial solution can be normalized using exact transformations
  preserving `x^-1 y^-1 x y`. This matters for noncentral targets; a
  transformation preserving only its conjugacy class would not suffice.
- Different-weight leading elements cannot commute, using the earlier
  rotation lemma. Equal dependent leading elements are reduced by an
  exact Euclidean Nielsen operation, raising one weight. Thus the first
  nonzero target degree is the sum of the resulting factor weights.
- Unequal-weight factorization retains both possible rational factor lines
  and every signed divisor of the unique second-factor content. Choosing
  only a primitive first factor, as is sufficient for central targets,
  would lose solutions here.
- Equal-weight pairs retain every index-h sublattice of the primitive
  support plane. Bases of the same oriented sublattice differ by SL_2(Z),
  which is realized by exact commutator-preserving operations.
- The final correction lies in the actual central group layer. Its
  tensor coordinate is taken from `[x0,y0]^-1*g`, not from the raw
  highest-degree coefficient of g. The latter need not be a Lie element.
- Cross corrections and conjugation errors have weight at least c+1.
  The final test is an integral linear system, not just a rational one.
- The proof does not extend this single lifting step to targets below
  gamma_(c-1); surviving interactions would require a further argument.

## Recorded checks

`results/n8-penultimate-checks-v1`: one CPU slot, 4 GB limit, 180-second
timeout. Passed in 58.56 seconds, with empty stderr. Fixed seed 9282618.
The 85 records comprise nine basis builds, 44 constructed positive
targets, 24 independent central perturbations, five negative leading-term
controls, two complete unequal-weight scaling checks and one equal-weight
sublattice enumeration check. Parameters cover rank two/classes four
through nine and rank three/classes five through seven.

Of the 24 central perturbations, 19 are negative and five positive.
The five negative leading-term controls have an independent metabelian
Eisenstein obstruction, as in the earlier central-target audit. All 14
class-five targets agree with the separate class-five implementation,
including negative cases and two delegated central targets. The index-six
equal-weight example has exactly 12 Hermite sublattices, all distinct and
all giving the required exterior tensor.

In 27 positive records, at least one earlier branch fails before a later
branch succeeds. A particularly useful scale control is record 17
(zero-based) of `research/certificates/N8-penultimate/checks.json`, rank two,
class six. The primitive leading first factor has coordinates `[1,0]`
and second factor `[0,0,6]`; both signed primitive branches fail.
The scale allocation `[2,0]`, `[0,0,3]` succeeds. Thus retaining all
divisor allocations has observable mathematical significance.

`results/n8-penultimate-gap-v1`: one CPU slot, 4 GB limit, 180-second
timeout. Passed in 120.23 seconds. It independently constructed free
nilpotent groups using GAP/nq and checked all 49 positive word witnesses.
For each of 187 lifting branches it independently evaluated the group
words x0,y0 and the correction commutators, checked that the residual
and all correction generators were central, and decided membership in
the subgroup they generate. All 187 answers agreed, including 140
negative answers. This uses GAP's group/subgroup algorithms rather than
the Python tensor coordinates or its integer-system solver.

The GAP log contains two nonfatal static warnings about x,y inside lambda
expressions in a top-level loop. Both variables are assigned before the
expressions are evaluated; no error occurred, all checks completed, and
the final marker and zero exit status were inspected. The script and log
are retained exactly as run. No failed run was discarded.

Compact certificate files and both checker sources are included in Git.
The checks support the implementations and lifting identity; finiteness
and completeness for arbitrary parameters rest on the mathematical proof.

## Literature and provenance

The homogeneous factor argument explicitly imports the earlier candidate's
rotation consequence of Klyachko's classical Lie idempotent theorem. Hall
collection, Hermite/Smith normal forms, and exact Nielsen operations are
standard. The new step is the finite enumeration of all integral leading
pairs needed for a noncentral lift, followed by the central correction.

Targeted searches for “commutator equation penultimate nilpotent”, “single
commutator nilpotent central algorithm” and “N8 commutator nilpotent” found
no matching theorem. This is not an exhaustive novelty audit. The older
class-two theorem and general-equation undecidability results remain
separate. No Kourovka mathematics or code was imported.
