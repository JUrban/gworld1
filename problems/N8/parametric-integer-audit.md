# Audit of the one-parameter arithmetic component

29 September 2026. This component is supporting prior mathematics. N8
remains partial with its previously recorded scope: leading degrees <=8
in arbitrary class, and all targets in classes <=14, among other recorded
families. The proposed ten-final-layer/class-18 extension is not counted.

## Exact computational evidence

The constructor `scripts/check_parametric_integer_linear.py` supplies 24
systems. They include divisibility, inconsistent rational solutions,
integer versus irrational roots, rectangular matrices, zero-rank systems,
rank-drop exceptions, nonconstant determinant, free coordinates, rational
coefficients, and nontrivial periodic congruences. Every accepted parameter
set is represented by the exhaustive finite/periodic argument, not inferred
from testing a bounded set of parameters.

For each system a further 85 direct integer solves at -40 through 40 and
at +/-101, +/-10000 compare against the certified answer: 2,040 comparisons.
The fixture named `constant_lattice_period17` receives a safe period 289;
the period is not claimed minimal. Nineteen systems have an integral
witness; five do not.

Independent GAP replay reads rational polynomial certificate data, not
Python code or SymPy lattice results. It checks U P V=D, U b=beta, polynomial
invertibility of U,V, inverse denominator clearing, complete integer roots,
the proper-fraction bound, the complete free columns, all K residues and
every exceptional parameter using native `SolutionIntMat`. Polynomial
equality is entrywise vanishing of differences. It checks all 2,040 fixed
specializations independently and the 19 final witnesses. The proof of
exhaustion is audited in `parametric-integer-proof.md`; sampled comparisons
are additional controls and do not replace that proof.

Final replay totals: **24 complete systems, 268 finite checks, 352 residue
checks, 2,040 specializations, 19 final witnesses**. Python v2 passes in
2.980141 seconds; GAP v3 passes in 2.226663 seconds. Both have empty stderr,
successful process status, and the intended final marker. Every job used
one CPU core and 8 GB per-process address-space reservation, sequentially.
All processes and completion handles are terminal.

Certificates are in `research/certificates/N8-parametric-integers/v2/`.
Commands, output, errors, times and resource settings are preserved in
`results/n8-parametric-integers-*`. The arithmetic algorithm contains no
finite search cap, although large denominators can make its proven finite
enumerations impractical. The suite tests positive dimensions only. No
performance assertion or independent specialist approval is claimed.

## Preserved failures and evidence limits

- Python v1 stopped at an assertion comparing unsimplified symbolic
  expressions in V V^(-1). It was a structural-equality implementation
  error; replacing it with expansion of the difference resolved it.
  The failed source and logs are preserved. It is not a successful suite.
- GAP v1 treated a constant polynomial as a rational object using `IsRat`.
  The polynomial determinant was mathematically constant but failed that
  type check. GAP v2 then exposed the analogous matrix object-equality
  issue for V V^(-1). Both runs exited with code zero despite GAP errors;
  the missing success marker correctly leaves `process_ok=false`.
  Their exact checker sources and error logs are retained.
- GAP v3 checks constant nonzero coefficient lists and entrywise algebraic
  equality. It completed all systems and emitted the final totals above.
- A preliminary SymPy API/one-row example was inspected outside the recorded
  runner before the suites. It is not counted as verification evidence.
- The certificate verifier checks a final witness when supplied. Its
  exhaustive accepted-set checks plus the constructor's selection logic
  establish witness availability; it has no separate assertion that a
  malformed certificate must include a final witness whenever nonempty.
  This is a certificate-format limitation, not an omitted existence case.

## Bibliographic reading and prior credit

Schuster's thesis PDF is archived as
`literature/raw/N8-Schuster-parametric-2007.pdf`, SHA-256
`a0bca8710c312b22d80b634b9e1f85187881c64354a588b40924f2f91ad25238`.
The introduction, relevant portions around Theorem 69 and Section 4.1.6
(printed pages 66–69) were read. Printed page 67 was actually rendered and
viewed; its PNG is retained. Theorem 71 and the preceding construction
give prior algorithmic parametrization, including residue classes and
exceptional values. The statement visibly prints `U=AS`, inconsistent
with the surrounding `UA=S` and matrix dimensions; this typographical
issue is not copied into our independent Smith argument. The complete
thesis proof has not been audited.

The primary publisher abstract for Bozga–Iosif–Lakhnech (2009), DOI
10.3233/FI-2009-0044, explicitly states one-parameter Diophantine
decidability. Its full proof was not read. The author's indexed PDF URL
`https://nts.imag.fr/images/7/7d/Fundamenta09.pdf` failed retrieval (web
timeout, local HTTPS protocol error; HTTP variant 404), so no downloaded
PDF is claimed. Earlier priority references appearing in search excerpts
have not been checked at their original sources. None of this arithmetic
is claimed as a new theorem of this experiment.

No new N8 statement interpretation, imported Kourovka argument, subagent,
push or external contact. Candidate counts remain 8 whole-entry coverage
candidates, 2 partial entries, and 0 established novel results. The next
step is the actual group reduction and overlap fixtures, not another
repetition of this successful arithmetic suite.
