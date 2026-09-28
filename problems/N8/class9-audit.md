# Class nine: proof scope and computational audit

28 September 2026, during the original 48-hour run. This accompanies
`class9-proof.md`, first drafted approximately 19:14 UTC. Independent
specialist review and a comprehensive novelty assessment remain outstanding.
The extension is **under audit** while the final rank-three replay runs.

The original N8(b) concerns arbitrary finitely generated free nilpotent
groups. An all-rank class-nine algorithm would extend the existing partial
candidate, not solve the whole entry or add another candidate. Part (a)'s
prior negative result is not changed. The exact original page, background
paragraph and rendered statement were inspected; retained evidence is in
`research/statement-audits/N8/`.

## Mathematical audit

The new homogeneous free basis of L' is built from graded complements
in L'/L'' and actual adjoint iterates. Injectivity on the metabelian
derived module follows from Poroshenko--Timoshenko, arXiv:1107.0430,
Theorem 4.3, printed p.8. The archived primary theorem and proof were
read, and that page visually inspected. Homogeneous Shirshov freeness
is credited to the ordinary-Lie formulation in the previously archived
Bryant--Kovacs--Stohr source. There is no unsupported appeal to freeness
of an arbitrary infinitely generated torsion-free module over a PID.

Five explicit correction-kernel arguments complete the earlier
class-seven/eight calculations. The third type-(1,2) kernel is handled
by simultaneous conjugation by the current factors' exact commutator.
This operation fixes their commutator and all earlier correction choices,
and supplies a nonzero period in the full primitive integral kernel.
For type (1,6), the exceptional condition is D=ad_z^4(T), and the
quadratic coefficient is outside the final rational correction image.
At most two integer parameters remain; every integer congruence is
still tested. A final-layer kernel is allowed and retained.

The proof separately checks every leading weight type, all linear-tail
weight inequalities, finite signed leading scales, and the exact Nielsen
periods. In particular, the type-(1,4) second correction must be fixed
before the class-nine tail: the old class-eight tail is not linear in
class nine. None of these all-rank assertions is inferred from finite
matrix ranks alone.

## Arithmetic changes and bounded checks

The new Magnus class uses the same Hall group words and integer
noncommutative series, with homogeneous projections split by letter-count
multidegree. Each small inverse and the complete reconstruction are checked.
The exact tail formula uses the group commutator identities and explicit
weight bounds, then checks the constructed answer in the full original
series. The component Hermite routine separates rows only when their
nonzero column supports are disjoint. It verifies H=U*B and det(U)=+/-1;
all particular solutions and the full integral kernel are preserved.

| Completed run | Supporting evidence | Seconds |
| --- | --- | ---: |
| `n8-class9-kernels-rank2-v1` | 21 kernel records, 2 obstructions | 1.02 |
| `n8-class9-kernels-rank3-v3` | 23 kernel records, 2 obstructions | 115.16 |
| `n8-class9-kernel-gap-rank2-v2` | Independent nq check of 21 kernels and 2 obstructions | 11.36 |
| `n8-class9-kernel-modular-gap-rank3-v1` | Independent GAP associative-algebra check of 23 kernels and 2 obstructions | 88.12 |
| `n8-multigraded-magnus-v2` | 128 coordinate/rational-line comparisons and 8 word-collection comparisons | 6.99 |
| `n8-class9-tail-v1` | 18 comparisons with full group commutators | 4.33 |
| `n8-component-hnf-v3` | 80 normal forms, 30 polynomial systems, 160 affine-system comparisons | 0.52 |

The rank-three independent kernel checker rebuilds the Hall Lie
polynomials and checks the actual Hall free-group words. Full rank modulo
251 supplies a lower bound on rational rank. Each predicted one-dimensional
kernel has an exact nonzero integer relation, supplying the matching upper
bound. For both obstruction fixtures the correction rows and the extra
obstruction row have full rank modulo 251 (818 and 819). These particular
modular rank increases certify rational independence; a generic increase
between two non-full modular ranks would not suffice.

The rank-three Python kernel run has scheduled stack snapshots in stderr
and completed normally. Other successful runs in this table have empty
stderr except the earlier rank-two GAP version, which had harmless parser
warnings and was rerun with local declarations as version two.

## Group decisions and independent replay

The final rank-two suite `n8-class9-targets-rank2-v2` passed 27 target
records in 17.73 seconds. These include repeated controls, so 27 is not
a count of distinct targets. There are 21 positive word witnesses,
68 linear branch decisions and 17 polynomial branches. The earlier
version-one suite passed the same count in 28.97 seconds.

`n8-class9-target-gap-rank2-v2` independently verified all 21 witnesses,
all 68 linear decisions (15 negative), all 17 polynomial certificates
(eight empty parameter lists), and 85 actual group parameter samples
in 76.63 seconds. GAP checks the integer Hermite transformation,
unimodularity, complete integer root list, congruences, actual correction
columns, and exact group residuals. The first replay of the earlier
suite passed the same counts in 75.62 seconds.

A nonprimitive type-(1,2) fixture has leading coordinates C=[1,0],
D=[4]. Its first Nielsen period is four and succeeds at residue two;
its third simultaneous-conjugation period is also four and succeeds
at residue one. This checks a nonzero residue of the new exact gauge,
not only cases in which the period or selected residue is trivial.

The rank-three version-three Python benchmark saved **seven completed
new-stratum decisions**, five positive and two negative, before timing
out in the older penultimate-layer delegate. It is not a passing full
benchmark. The saved prefix covers generic types (1,6),(2,5),(3,4),
two exceptional positive parameters, and two negative degree-nine
perturbations. It has five witnesses, 12 linear steps and six polynomial
branches. The input data and every completed record are retained in
`research/certificates/N8-class9-rank3-v3/`.

The first independent rank-three group replay was deliberately interrupted
after 524.46 seconds: it had checked all five witnesses and one linear
decision. Its incomplete outcome, exact source and reason are retained.
The next checker uses the certified additive suffix of nq's integral
polycyclic coordinates for integer membership, plus balanced cached word
evaluation. These methods were justified in the earlier class-eight audit.
It first reproduced every rank-two certificate in 5.44 seconds.

A further version decomposes integer systems by disconnected support
components and checks certificate unimodularity on the corresponding
square blocks. Sparse row combinations verify every entry of H=U*B.
Independent echelon reduction replaces inversion of a large U; it verifies
the same particular polynomials and every congruence. This version also
reproduced the complete rank-two suite, in 5.59 seconds. The rank-three
replays are pending at the time this paragraph is written. Their eventual
terminal outcomes must be reported before describing them as successful.

## Preserved unsuccessful runs

Every process record retains the actual return code, timeout or deliberate
interruption, stdout/stderr and hashes. Relevant original scripts are
copied beside the logs when subsequent code changes would obscure them.

- `n8-class9-kernels-rank3-v1`: 300.05-second timeout during the original
  Hall constructor; no completed kernel suite.
- `n8-class9-kernels-rank3-v2`: 300.05-second timeout with an early block
  projection implementation; partial records retained.
- `n8-class9-kernel-gap-rank3-v1`: 300.02-second timeout without individual
  completion markers. Its completed phase is not asserted.
- `n8-multigraded-magnus-v1`: 180.02-second timeout during a long-word
  collection comparison. The later passing comparison used shorter words;
  it is not represented as completion of this harder benchmark.
- `n8-class9-targets-rank3-v1`: 400.05-second timeout in the first
  type-(1,2) tail, with no completed target decision.
- `n8-class9-targets-rank3-v2`: 400.13-second timeout in the old polynomial
  Hermite calculation after three completed generic positive records.
- `n8-class9-targets-rank3-v3`: 400.36-second timeout in the penultimate
  delegate after the seven completed records described above.
- `n8-component-hnf-v1`: arithmetic assertions completed, but JSON
  serialization of an fmpz failed after 0.47 seconds. No PASS is claimed;
  conversion to plain integers and later comparisons passed.
- `n8-class9-target-gap-rank3-v1`: deliberately interrupted incomplete
  replay, as described above.

Repeated faulthandler messages saying `Timeout (0:01:00)!` are scheduled
stack snapshots, not process outcomes. The process JSON is authoritative.

## Reproduction and limits

All mathematical runs use `scripts/run_recorded.py`, one CPU and an 8 GB
per-process address-space limit. Concurrent reservations remain within the
overall 20-CPU/100-GB budget. The exact commands, seeds and terminal
outcomes are in the named `results/` directories. The generators refuse
to overwrite their completed `checks.json`; use fresh output paths.

`export_n8_class9_gap.py` converts saved certificates to GAP literals
without recomputing group decisions. Large sparse polynomial fixtures are
gzip compressed; GAP reads them directly. Every retained blob is below
the repository's 90,000,000-byte threshold. No external certificate store,
unpublished large file or omitted solver output is required for the
reported checks.

Bounded literature searches located no matching class-nine theorem, but
do not certify novelty. The preceding class-two results and structural
theorems remain credited. There has been no outside proof review, imported
Kourovka mathematical result, external contact or push during this extension.
