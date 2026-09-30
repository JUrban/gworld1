# G9: disjoint shear tails of the existing atom alphabet

30 September 2026, after c5d9081, within the original window. The preceding
turn completed the N8 higher-weight negative integration check. The
original deadline remains 10:04:49.670358 UTC; reserve the final half hour
for reporting and closure. Do not enlarge the bridge-word enumeration.

For a strict bridge of height H>=3, apply the Nielsen automorphism
alpha_k(a)=a b^k, alpha_k(b)=b. It shifts a vertical edge based at height h
by hk horizontally and inserts only horizontal steps. Thus bridge height
and the atom condition are preserved. It commutes with both boundary
operations P_(u,v)(w)=a b^u a^-1 w b^v.

Let x1,x2 be the minimum horizontal positions of nonzero vertical edges
at internal heights one and two, and let y be the endpoint. Put
d=x2-x1, u=x1-d, v=y-x1-(H-1)d. A shear changes d by k and leaves u,v
fixed; P changes u,v independently. Normalize all three coordinates to
zero using these exact operations and retain the full resulting flow.
Equality of normalized flows should classify the resulting Z^3 orbits.

Within each such orbit, the old two-boundary alphabet occupies finitely
many d values but all u,v at each one. Let l,m be the smallest/largest
old d. Add only shear tails with d>m or d<l; this avoids all old letters,
including their entire horizontal completions. Choose one old seed for
each tail. If it has cost c, V vertical letters and starts at d0, the
positive tail costs c+V(m+1-d0+n), n>=0, before boundary completion.
Its series is t^(c+V(m+1-d0))/(1-t^V) times ((1+t)/(1-t))^2.
The negative tail has the analogous l-1 boundary. Different normalized
flows and opposite tails must be proved disjoint, not inferred from samples.

Use the current retained Steiner seeds, preserving the old alphabet and
adding these tails only. Export compact full-flow orbit data and literal
control words. Recompute exact rational lower bounds and independently
reconstruct the canonical flows, seed coverage, cost series and controls
in GAP. One CPU/6GB per job, bounded stages and fresh output names. If the
construction or replay fails, preserve the failure and retain the old bound.
No novelty or complete G9 solution follows from a successful refinement.
