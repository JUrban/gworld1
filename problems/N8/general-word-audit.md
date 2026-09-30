# N8: general word-input decision command

30 September 2026, approximately 06:31 UTC, within the original research
window. This completes the input/output interface and elementary boundaries
left open at the preceding [implementation checkpoint](general-implementation-audit.md).
The arbitrary-rank/class candidate algorithm is now implemented end to end.
Correctness of its structural proof and novelty remain subject to specialist
review. The finite tests below do not establish the all-rank theorem.

## Usage and output

Input is JSON, for example:

```json
{"rank": 2, "class_bound": 7, "word": [-1, -2, 1, 2]}
```

The input group is F_rank/gamma_(class_bound+1). Signed indices refer to its
free generators, and [x,y]=x^-1 y^-1 x y. Rank/class are nonnegative integers;
class zero denotes the trivial quotient. Rank zero, rank one and class one
are handled directly, using exponent sums in the abelian cases. All other
inputs use the full integral recursion, including a direct identity check.

During the active run:

```sh
python3 scripts/run_recorded.py --name UNIQUE-N8-JOB \
  --cores 1 --memory-gb 8 --timeout 180 \
  --expect 'PASS N8 general word command' -- \
  .venv/bin/python scripts/n8_general_word.py \
  --input INPUT.json --output FRESH_OUTPUT_DIRECTORY
```

The Python environment needs the already installed SymPy and python-flint.
The command has no internal word-length, rank, class, coordinate or residue
cutoff. It can be extremely expensive; a timeout or resource failure does not
produce a negative answer. The original runner refuses post-deadline research.
Later replay must be explicitly dated as review and cannot restart that clock.

The output directory preserves input bytes/hash, a flushed event trace,
status, and, only after a complete decision, `decision.json`. Positive
solutions are given by two integer coordinate vectors and a Hall-word DAG:
the first rank nodes are the free generators; every subsequent pair [i,j]
means the group commutator of the earlier zero-based nodes i and j. A vector
means the ordered product of those nodes to the stated powers. Thus these
are compact words in the original generators, without potentially enormous
literal expansion. The returned commutator is checked against the whole input.

An explicit exception records failed status and is re-raised. A killed process
can leave a running status and partial trace; only a successful process receipt,
completed status and hash-bound decision constitute a completed execution.
The procedure remains an implementation of the written candidate proof.

## Checks

Eight elementary controls cover rank zero, class zero, arbitrary-class cyclic
groups and class-one free abelian groups, including positive and negative
targets. Four malformed rank/class/word inputs are rejected. Four actual
standalone commands were then run: trivial-group positive, abelian negative,
nonprimitive universal-period positive, and exceptional-quadratic negative.
Their input and decision hashes and expected answers were checked.

GAP separately reconstructs the ten elementary cases (eight API fixtures and
the two elementary command outputs) using native abelian groups. It then
replays the two nonabelian command outputs in native free nilpotent groups:
one full witness, 70 correction columns in six affine blocks, and two
quadratic obstructions with twelve actual group samples. The wider preceding
audit supplies the delayed class-ten and rank-three/four controls, full
leading-branch negative checks and independent universal automorphisms.

Six additional recorded jobs pass, each one CPU/eight decimal GB, maximum
overlap two CPUs/16 GB. The native replay took 1.975 seconds; all stderr files
are empty. Receipt/input/decision hashes and terminal PIDs were checked. No
proof, candidate count, novelty assessment or deadline changed. The previous
proof/implementation audits retain their original dated scope statements.

The current report, draft, research-plan header and problem entry point now
describe this complete command. Exact earlier file versions were archived
before those edits, preserving old manifest bindings. The dated 06:00 scope
ledger remains an earlier assessment until its next explicit reconciliation.
Bindings for this stage are in
`research/certificates/N8-general-word/manifest-v1.json`.
