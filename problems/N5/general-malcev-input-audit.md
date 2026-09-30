# Higher-class native-group input for N5

30 September 2026. This implements the rational Malcev input stage for a
native nilpotent pcp group of arbitrary finite class. It extends the earlier
class-two interface, but is **not yet the complete higher-class decision
pipeline**. No candidate count or novelty assessment changes.

## Construction and conventions

For G, compute its finite torsion subgroup T and the torsion-free quotient
Q=G/T. Rebase Q along its upper central series, using Smith normal form for
each abelian factor. These factors are torsion-free: a torsion-free nilpotent
group has torsion-free quotient by its center, and the same statement applies
successively. Thus the new pcp presentation has exactly h infinite relative
orders, where h is the Hirsch length. The program checks this condition.

Use the installed Polycyclic implementation of a faithful unitriangular
matrix representation. Its [manual](https://gap-packages.github.io/polycyclic/doc/chap9.html)
requires a presentation without power relations. This differs from merely
checking abstract torsion-freeness. The input control with generators a,b,c,d
and a^2=c, [b,a]=d, [c,b]=d^-2, with the other basic commutators trivial,
is torsion-free but starts with a relative order two. The rebase removes it.
The installed `PcpGroupBySeries` returns its `bijection` in the direction
new group to old group; the converter checks source and range explicitly.

For m by m unipotent matrices, use the exact finite series

    log(I+U) = sum_{k=1}^{m-1} (-1)^(k+1) U^k/k,
    exp(X)   = sum_{k=0}^{m-1} X^k/k!.

The logarithms of the central-series pcp generators form a basis of the
rational Malcev Lie algebra. Their independence, dimension h, and closure
under [X,Y]=XY-YX are checked directly; GAP returns the rational structure
constants in that ordered basis. This uses the usual Malcev correspondence
and the faithful representation supplied by Polycyclic, rather than a new
proof or formal verification of those tools. Matrix images here are lower
unitriangular. Ordered pcp exponent vectors represent ordered products of
generator powers. No transpose is used as a group homomorphism.

The converter retains G -> Q, the rebasing isomorphism, and the matrix map,
as well as functions taking original group elements to matrices and Lie
coordinates. If Q is trivial, the output Lie algebra is zero and the matrix
conversion is bypassed. This case includes finite nonabelian groups; it does
not mean the original group has no nontrivial direct factors.

## Verification

The nine inputs are the trivial group, D8, Z^3, the integral Heisenberg
group, free rank-two nilpotent groups of classes three and four, the product
of the class-three group with the Heisenberg group and Z, the product of
the class-three group with D8, and the finite-relative-order control above.
Their rational factor dimensions are respectively

    [], [], [1,1,1], [3], [5], [8], [1,3,5], [5], [3].

GAP checks presentation relations in the matrix representation, exact
logarithm/exponential recovery, and 108 native group words. Python separately
recomputes the matrix series, all 222 bracket entries and all 108 ordered-word
matrices before invoking the existing rational Lie decomposition algorithm.
Twenty-three word matrices reject the false shortcut log(I+U)=U. A deliberately
altered bracket coefficient also fails matrix recovery for each nonzero input.

Finally GAP reconstructs each Lie algebra and checks its nilpotency class,
central/stem split, full centroid, trace radical, nilpotence of the radical,
rational characteristic-polynomial factors, repeated-factor CRT projections,
projection orthogonality and complete factor dimensions. This reuses the
earlier checker definitions verbatim, without rerunning its old fixture suite.
All nine new inputs and eleven rational factors pass. This is independent
program reconstruction by the same agent, not outside specialist review.

Three sequential runs, each reserving one CPU and eight decimal GB:

| Run | Seconds | Result |
| --- | ---: | --- |
| `n5-general-malcev-input-v1` | 2.176 | native group export passes |
| `n5-general-malcev-python-v1` | 3.181 | independent matrices and Lie solver pass |
| `n5-general-malcev-lie-gap-v1` | 1.875 | full native Lie/centroid replay passes |

All stderr files are empty. The manifest binds source, outputs, receipts,
statement evidence and process closure. The original full nilpotent-problems
HTML and N5 paragraph were reread, and the retained statement rendering was
actually viewed. The input convention remains the one in the controlling
proof: finite presentations with the nilpotency promise, converted to native
pcp form. This new module itself starts from pcp form; it does not implement
that general promised-finite-presentation conversion.

## Remaining integration

General rational-support preimages, the complete bounded-index search in
G/Z(G), and connection to the central-lifting solver are not supplied by this
module. The existing complete finite-presentation command still requires the
class-at-most-two promise. These boundaries must remain explicit when reporting
implementation evidence for the general written candidate.
