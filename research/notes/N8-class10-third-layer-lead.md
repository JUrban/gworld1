# N8(b): possible complete gamma_8 stratum in class ten

First developed 28 September 2026, approximately 22:38–22:43 UTC.
**Uncounted lead.** The earlier nonlinear family does not yet establish
this broader scope. A bounded structural probe is the next test.

The proposed extension decides every target in gamma_8 of F_r/gamma_11,
not every class-ten target. The gamma_9/gamma_10 cases are already covered.
For a nonzero degree-eight leading term the possible normalized types
are (1,7), (2,6), (3,5), (4,4). Finite integral leading-pair enumeration
is already available from the central/penultimate algorithms. It remains
to control the first correction map into L9; the last correction is
linear into L10.

Use the delta-stable free alphabet of L' from the class-nine proof when
C=z has degree one. Otherwise use any homogeneous free alphabet of L'.
Write E,B,W,G,H,J for free-generator spaces of weights 2 through 7.

## Proposed first-correction classification

1. Type (1,7): the kernel of L2+L8 -> L9 is zero unless

       D = sigma*(2[T,delta^3 T]+3[delta T,delta^2 T]),
       delta=ad_z,  0 != T in E,  0 != sigma in Q.

   In that case it is the one-dimensional line already treated in
   `class10-nonlinear-proof.md`. That proof established the kernel for
   the displayed family; the new step would show that there are no
   other exceptional D.
2. Type (2,6): L3+L7 -> L9 is injective for every nonzero C,D.
3. Type (3,5): L4+L6 -> L9 is injective for every nonzero C,D.
4. Type (4,4): L5+L5 -> L9 is injective when C,D are independent.

## Argument proposed for the missing type (1,7) direction

Suppose [U,D]+delta V=0 with nonzero U in E. Include U as a weight-two
seed of the delta-stable free alphabet and decompose by alphabet length.
There are at most three letters in D, of total original weight seven.

For length-one D, project [U,D] to associative words with prescribed
seed sequence. Delta is multiplication by the sum of the jet variables.
Any seed other than U gives a polynomial independent of the first jet
variable, so cannot be divisible by that sum. For the U seed itself,
D is proportional to U_5, and the polynomial v^5-u^5 is not divisible
by u+v. Thus this component is zero.

For length-two D, a component containing two seeds other than U is
excluded using ordered seed sequence U,S,T. A component with exactly
one other seed S is excluded using sequence U,U,S: its polynomial is
independent of the first jet variable. These statements include repeated
other seeds and are coefficientwise; they do not substitute equal jets.
Thus only the U,U seed component survives. Its weight seven basis is
[U_0,U_3], [U_1,U_2]. The possible length-three, weight-eight V terms
are A=[U_0,[U_0,U_2]] and B=[U_1,[U_0,U_1]]. In the degree-nine basis

    X=[U_0,[U_0,U_3]],
    Y=[U_1,[U_0,U_2]],
    Z=[U_0,[U_1,U_2]],

one has delta A=X+Y+Z and delta B=2Y-Z. Hence c0 X+c1 Z is a delta
image exactly when c1=3c0/2. This gives precisely the old nonlinear
exception, with no new rational-points decision problem.

For length-three D, the possible V has length four and weight eight,
so belongs to Lie_4(E). Treat each multidegree in the E seeds separately.
Every nonzero such component uses some seed other than U. Substitute
delta U -> 0 and delta S -> S for every other E seed into the equation,
leaving E unchanged. The left derivative becomes m V for a positive
integer m. Thus V=[U,A] with A in Lie_3(E). Restoring the original
derivation yields [delta U,A] in ad_U(L'). Since A contains no delta U
letter, this forces A to be a polynomial in U in the free associative
algebra, hence zero in homogeneous Lie degree three.

The last implication uses an elementary auxiliary fact to be written
carefully in the final proof: if t is a fresh free letter, a is one
old letter, and P is a polynomial in the old letters, then

    [t,P] in [a, T(old letters + t)]  implies P in Q[a].

Project to terms with exactly one t. Modulo aQ-Qa, move each initial
run of a letters to the end of the word. These are canonical word
representatives for this vector-space quotient, since its generating
relations identify exactly these shifts. Every tP monomial is already
canonical and retains its individual coefficient. If a monomial of P
contains another old letter, its Pt representative starts with that
letter, whereas its tP representative starts with t. There can be no
cancellation between the two families. The pure a powers do cancel.
Thus P belongs to Q[a]. For homogeneous Lie degree greater than one,
P is zero. This establishes the proposed
exclusion of the length-three component, subject to the full audit.

## The other proposed injectivities

For (2,6), U is in B and V decomposes as
J+[E,G]+[B,W]+Lie_(2E,1B). The alphabet-length and weight-type components
first kill D_H, V_J and V_(EG) if U is nonzero. The B^3 component kills
D_(BB). Setting C=0 in the E,B,W component then forces D_(EW)=[C,S]
for S in W. Projection to words B,C,W forces S=0. The remaining
D lies in Lie_3(E), and the auxiliary fresh-letter fact applied to
[U,D] in ad_C(L') kills it. Thus nonzero D admits no nonzero kernel.

For (3,5), write D=D_G+D_(EB), U=U_W+U_(EE), and
V=V_H+V_(EW)+V_(BB)+V_(EEE). If D_G is nonzero, its disjoint weight
types force both parts of U to vanish. Otherwise V_H=0. The E,B,W
component forces U_W=0: quotienting by C makes D=[S,C], and words
W,C,E then force S=0 if U_W is nonzero. Also V_(EW)=V_(BB)=0.
If U_(EE) is nonzero, separate the B directions in D. Every direction
other than C vanishes because commuting equal-length tensors are
proportional and their letter types differ. Thus D=[S,C]. In
[U,[S,C]], the internal-C terms -U C S and -S C U have C in different
positions, and cannot occur in [C,V]. Consequently U or S is zero.
This proves the proposed injectivity.

For (4,4), bracket is injective on

    (W + Lambda^2 E) tensor (G + [E,B]).

Its four summands have disjoint alphabet weight types. The W,G case is
immediate; the W,E,B and E,E,G cases are seen by coefficients with
the single distinguished letter at an end; the E,E,E,B case follows
from the injection of the exterior square of the degree-two free Lie
space into associative two-block tensors. Therefore
C tensor V-D tensor U=0; independence of C,D forces U=V=0.

## Consequence if these checks survive

Solve the first correction integrally. An injective case gives at most
one choice, followed by the complete final integral linear system.
In the sole proposed exception use the already proved nonzero quadratic
cokernel obstruction, retaining at most two integer parameters. This
would cover all normalized leading pairs and hence all gamma_8 targets
in class ten. It would extend the existing partial candidate only.

Do not count this until the new classification, auxiliary fact, complete
implementation and independent target replays have been checked. The
rotation lemma is already proved using Klyachko in `central-target-proof.md`;
there is no need to repeat its old bounded tests.


Update 2026-09-28T22:55:03.075849+00:00: the all-rank proof and completed bounded independent audit are now in `problems/N8/class10-third-proof.md` and `class10-third-audit.md`. The rank-three timeout and two fixture-loading failures remain preserved. The scope was added to the same partial N8 candidate, with no additional problem count.
