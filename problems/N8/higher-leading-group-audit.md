# N8: higher leading weights in the complete group recursion

30 September 2026, within the original experiment. This is a targeted
implementation check after the [general command](general-word-audit.md)
and [integral block audit](general-lattice-branches-audit.md). The solver
was unchanged. The structural proof and novelty still require specialist
review; these two examples are not additional solved problems.

The earlier exceptional integration cases had first leading weight one.
The general argument also allows a higher-weight first coefficient with
nontrivial fixed higher logarithmic terms. The new tests exercise that
case in actual free nilpotent groups, using the complete leading-pair
enumeration rather than supplying only the planted branch.

## Two exact inputs

Use [x,y]=x^-1 y^-1 x y. In the first case, work in rank three/class six
with generators a,b,c. Set

```
C=[b,a], U=[b,C], D=[c,a], V=[c,[b,D]],
g=[C^2 U, D^3 V].
```

The weight-(1,3) leading list is empty. The complete weight-(2,2) list
contains twelve exterior/Hermite pairs. The solver rejects earlier
branches by integral obstructions and then recovers a full witness.
The returned factors both have leading weight two. This checks the
nonprimitive equal-weight normalization above degree one and its lifts.

In the second case, work in rank two/class eleven and set

```
C=[b,a], U=[b,C], D=[C,[C,U]],
g=[C U^2,D].
```

The weight-(1,8) leading list is empty; the weight-(2,7) list has two
pairs. The first branch reaches an exceptional correction at offset one.
Its affine block has 99 rows, 32 columns and a one-dimensional complete
integer kernel. The adapted step is one. Its projected obstruction is

```
T^2-2T,
```

with complete integer root list {0,2}. The solver proceeds through the
remaining linear tail and returns a full commutator witness whose factors
have weights two and seven. The planted root need not be the only possible
one; the recovered full group equality is what is checked.

The corresponding leading Lie identity is
[U,ad_C^2(U)]=[C,[U,[C,U]]]. Here C is a group commutator, rather than
a free group generator, so its fixed higher logarithmic terms are present.
This is the specific normalization interface being tested.

## Separate reconstruction

The [GAP wrapper](../../scripts/check_n8_higher_leading_gap.g) checks both
returned leading-weight pairs. For the exceptional block it compares the
exported integer kernel with a native integral nullspace using canonical
Hermite forms, verifies the affine point, and checks that the adapted
kernel change is integral with determinant +/-1.

The existing [native group checker](../../scripts/check_n8_general_solver_gap.g)
then constructs the two free nilpotent groups independently in GAP/nq. It
reconstructs both full witnesses, 195 actual correction columns in six
affine blocks, their integral positive/negative membership decisions, and
the quadratic at six integer samples. It verifies all projected later
columns and the complete integer root list. The imported leading-list
completeness and all-rank structural lemmas remain written proof dependencies.

Three recorded jobs used one CPU and an 8 GB per-process limit each.
The two Python jobs overlap briefly, reserving at most two CPUs/16 GB,
and pass in 1.223 and 11.959 seconds with empty stderr. The GAP replay
passes in 5.989 seconds. Its stderr contains one retained parse-time
warning for the global fixture variable populated by `Read` before use;
there is no runtime error. The successful source and warning are retained
without an unnecessary rerun.

The full archived nilpotent-group page, exact N8 fragment and background
were reread, and the retained statement rendering was viewed. Part (a)'s
general class-two negative answer remains credited prior work. No new
source theorem, novelty conclusion, candidate count or outside mathematical
review is introduced. Exact commands and artifacts are bound in
`research/certificates/N8-higher-leading-exception-v1/manifest-v1.json`.
