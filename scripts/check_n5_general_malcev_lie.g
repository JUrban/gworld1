# Full native GAP Lie/centroid/CRT replay of the new group-derived fixtures.
Read("scripts/n5_rational_lie_gap_checker.g");
Read("research/certificates/N5-general-malcev-input/decompositions-v1.g");
N5MalcevLieCounts:=List(N5MalcevLieFixtures,N5LieReplay);;
Print("PASS N5 general Malcev GAP Lie replay: ",Length(N5MalcevLieCounts),
    " groups; ",Sum(N5MalcevLieCounts,x->x[2])," factors\n");
QUIT;
