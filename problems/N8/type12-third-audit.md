# Audit of the type-one/two third-layer extension

29 September2026. [Candidate proof](type12-third-proof.md). This is internal
proof review and independent software replay; no outside specialist review
or established novelty is claimed.

## Scope and proof review

The original full N8 source/background and actual statement rendering were
reread/viewed during this work period. Part(b) has no class or target-layer
restriction. The present extension requires c>=8, a nonzero leading term in
degree c-2, and **no normalized integral leading pair with first weight
p>=3**. It combines both type1 and type2 branches, keeping every integral
scale. Empty leading lists are negative; excluded types/layers are
unsupported. It enlarges the same partial candidate, adding no problem
count and leaving general N8(b) unresolved.

The proof was separately checked as follows. C in L2 can be a free letter
of L'; it is not claimed to be a degree-one generator of L. Lazard
elimination is applied inside L', and its ideal quotient is concentrated
in weight2. Thus D,V and all correction spaces really lie in that ideal.
Every first correction U in L3 is a seed letter combination: neither a
positive shift nor a decomposable word can have that weight. This is the
reason the type2 argument works; arbitrary higher-weight U need not have
this property.

The support lemma is a direct prior inner-solution consequence, with the
newly located credit made explicit. Two independent U directions may be
chosen simultaneously in one seed basis, so the zero-intersection argument
bounds the first kernel by one. Projection to the U-chain kills **all** of
L4, including brackets of other weight-two seeds. It commutes with delta.
The cyclic double-primitive lemma therefore gives the required nonzero
quadratic cokernel. Weighted degree q>3 excludes its linear exception;
the omitted q=3 Nielsen case is not silently included.

The integral procedure retains the entire primitive affine line and all
roots/congruences, with final correction image [L4,D]+[C,L_(q+2)]. The
weight estimates were redone for p=2, rather than copied from p=1:
3+(q+1)=c, while two first-factor corrections enter only in q+6.
All higher coordinates are absorbed by the final linear system or cannot
affect the group commutator. Completeness of the finite leading list remains
an earlier mathematical dependency, not something certified by GAP.

## Sources and bibliography

The archived Altassan2013 thesis gives Lazard elimination as Theorem2.1,
p.19, and the inner-solution theorem as Theorem3.3, pp.24--25. It credits
the latter's two-coefficient case to Remeslennikov--Stöhr2007 and its
higher-coefficient extension to Altassan--Stöhr2012. Actual pages19 and24
were viewed; the complete relevant proof was read in extracted text.
The inaccessible journal PDFs are not described as read. Source hashes,
reading limits and the precise embedding reduction are in
`literature/LEDGER.md` and `research/notes/N8-general-first-kernel.md`,
Section7. The earlier type1 proof/audit has been updated with this credit.
The support lemma is not counted as novel. The group-stratum theorem's
novelty remains provisional. No new Kourovka transfer is used.

## Independent computation

The Python driver uses integral truncated Magnus expansions, exact Hall
coordinates and integer affine/quadratic lattice calculations. Seed:
9292700+10r+c. Every imported local Python dependency is copied before the
run. All mathematical jobs use one core,8GB and a180s timeout under the
recorded runner. All six jobs completed with exit0, expected marker and
empty stderr; there were no failed type12 runs.

| Rank, class | Target records | Positive | Negative | Unsupported | Python seconds | GAP seconds |
|---|---:|---:|---:|---:|---:|---:|
|2,11|9|4|2|3|26.505|9.851|
|2,10|8|3|2|3|4.483|2.779|
|3,8|8|3|2|3|13.914|9.701|

Rank2/class11 uses C=T=[b,a], U=[a,T], D=ad_T^2(U). Its first kernel is
one-dimensional, as predicted. Positive cases include higher corrections
and the signed nonprimitive scale C^2,D^-3. The two negative targets exhaust
all integral leading choices and fail their final quadratic tests. Rank2/
class10 and rank3/class8 have zero-kernel type2 controls. Each suite also
includes a type1 positive target to check combined dispatch, a genuine
higher-type commutator returned unsupported, and identity/degree-one scope
controls. The class10 target has **both type1 and type2 leading branches**:
the failed type1 branches were retained before its type2 witness succeeded.

GAP independently rebuilt the nilpotent quotient and Hall commutators. It
checked10 witnesses,40 full integer linear decisions(16 negative),8 quadratic
certificates(4 with no admissible parameters),40 parameter group evaluations,
18 first-map nullities and19 higher-type span controls. All8 polynomial
certificates also have a complete primitive first affine-line check.

The higher-type controls test exclusion from the rational span of brackets
with both leading degrees>=3. This is a sufficient condition satisfied by
the selected supported fixtures, not an asserted characterization of every
input admitted by the algorithm's weaker finite-integral-pair condition.
The rejected fixtures belong to this span and have a genuine higher leading
pair. GAP does not independently enumerate all leading directions/scales.
The finite root/Hermite replay tests full arithmetic identities and group
columns; five parameter evaluations rely on the written quadratic degree
bound. None of these bounded computations proves the universal Lie lemmas.

## Artifacts and reproduction

Implementation: `scripts/n8_type12_third.py`. Run
`check_n8_type12_third.py --rank R --class-bound C --directory FRESH_DIRECTORY`
with the recorded runner. Export its retained certificates using
`export_n8_type12_third_gap.py DIRECTORY`, then use a GAP driver setting
N8C9Directory to that path and reading `check_n8_type12_third_gap_core.g`.
The concrete successful drivers for r2_c11,r2_c10,r3_c8 are retained.
Process records live under `results/n8-type12-third-...` and include exact
commands, times, resource limits, actual exits and stdout/stderr hashes.
The certificate directories have SHA256 manifests, executed source versions
and both positive and negative branch records.

The preceding type1 class12 timeout and its exact versions remain unchanged.
A whitespace-only cleanup of the current leading enumerator removed an extra
EOF blank line; the executed historical copies retain their exact bytes.
Counts remain six whole-entry and three partial candidates, zero established
novel results. Independent specialist review of all nine remains outstanding.
