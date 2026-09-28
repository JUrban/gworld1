# F6: the 2025 outer-conjugacy theorem does not retire the entry

Scope check, 28 September 2026. No new candidate is proposed.

The original F6 asks about conjugacy in Aut(F_n) for finite rank. The
original HTML paragraph, linked background and rendered statement were
read. The background already distinguishes the earlier results for
irreducible outer automorphisms. Rendering evidence is under
`research/statement-audits/F6/`.

Dahmani, Francaviglia, Martino and Touikan, *The conjugacy problem for
Out(F_3)*, Forum of Mathematics, Sigma 13 (2025), e41,
[doi:10.1017/fms.2025.3](https://doi.org/10.1017/fms.2025.3), gives a full
algorithm for conjugacy of **outer classes in rank three**. Theorem 1.1
takes representatives in Aut(F_3), but its output concerns their classes
in Out(F_3). The input format does not change the conclusion into an
Aut(F_3) decision theorem.

The archived primary preprint is
[arXiv:2311.04010v1](https://arxiv.org/abs/2311.04010v1), November 2023,
stored as `literature/raw/F6-DFMT-OutF3-2023v1.pdf`, with retrieval metadata.
Theorem 1.1 and the rank-two theorem were checked visually on printed
pages 2 and 13. The latter is Theorem 3.9 in this preprint and Theorem
3.10 in the published article. It explicitly credits the prior solution
for Aut(F_2) to Bogopolski and Bogopolski--Martino--Ventura. Preprint
Remark 3.10, printed page 15, also distinguishes the automorphism
conjugacy problem from the outer one. This is a check of the exact
statements and the rank-two discussion, not a complete audit of the
long rank-three proof or all its dependencies.

There is an elementary reason an outer-conjugacy answer alone is
insufficient. In a nonabelian free group, the identity automorphism and
conjugation by a nontrivial basis element have the same outer class.
The latter is not the identity, because the centre of a nonabelian free
group is trivial. It therefore cannot be conjugate to the identity in
Aut(F_n). A positive answer after quotienting by inner automorphisms
loses information required by F6.

This does not rule out a more elaborate algorithm using outer conjugacy
as a subroutine. Such an algorithm would still need to control the
available outer centralizer and the remaining inner-conjugacy choices;
no complete reduction is supplied here. Rank at most two is prior;
the wider Aut(F_n) scope remains unresolved in this experiment. The
bounded search is not an exhaustive current-status claim.
