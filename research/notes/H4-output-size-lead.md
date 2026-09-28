# H4: a possible output-size obstruction

Uncounted lead, first argument approximately 20:59--21:01 UTC on
28 September 2026. Needs statement, proof, implementation and novelty
audits before it can enter the candidate ledger.

Suppose a finite group has a Dehn presentation of explicit size
m = number of generators + sum of relator lengths. Include free
cancellations and all prefixes of length floor(L/2)+1 of cyclic
rotations of each relator and its inverse among the forbidden subwords.
The language avoiding them has a deterministic prefix automaton with
at most 1+2r+sum L^2 <= (m+1)^2 nonfailure states. This language is
factor-closed. If there were an accessible cycle, its label would have
arbitrarily large accepted powers; a power equal to 1 in the finite
group would contradict the Dehn property. Hence the accessible
automaton is acyclic. Every geodesic is accepted, so

    |G| <= (2m)^((m+1)^2).

This bounds all explicit Dehn presentations, even with changed generators.
It does not address compressed descriptions of exponentially many relators.

Now take generators x,t_0,...,t_n with relations

    t_i=t_(i-1)^2 (1<=i<=n), t_n=1,
    t_0*x*t_0^-1=x^2.

The presentation has size 4n+8 in the generator-letter model. Eliminating
the t_i gives <x,t | t^(2^n)=1, t*x*t^-1=x^2>. Put Q=2^n, M=2^Q-1.
Conjugating repeatedly gives x^M=1. Since M is odd, <x> is normal,
and the presented group has order at most MQ. The semidirect product
C_M semidirect C_Q, with action x -> x^2, satisfies the presentation
and has order MQ, proving equality. It is finite, hence hyperbolic.

The order bound for a Dehn output of size m would imply
(m+1)^2 log_2(2m) >= 2^n-1. Thus its explicit output size is
exponential in n up to polynomial factors. The input bit length is
O(n log n), still excluding a polynomial-time output algorithm.

Potential qualification: check the exact convention for Dehn presentations
and whether H4 implicitly fixes a group or allows compressed output.
The displayed question varies the input presentation and asks for a Dehn
presentation, so the usual explicit uniform interpretation appears to
match. The argument also works for cyclic Dehn reduction by taking a
sufficiently large power of the cycle label.

Initial searches found the same H4 question on Kharlampovich's IAS lecture
slides, and a related 2012 MathOverflow discussion suggesting that finite
groups can require many Dehn relators. Those observations must be credited;
no exhaustive novelty check has yet been done. The finite-group/output-size
strategy is therefore not claimed to be new.
