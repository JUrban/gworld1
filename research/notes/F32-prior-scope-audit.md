# F32: nonlinearity is prior; finite presentability remains separate

30 September 2026. This corrects an unsplit bibliographic lead in the
triage. It adds no candidate from this experiment.

The full archived free-group page, F32 fragment and background were read.
The original-page rendering was inspected: the star attaches to (b).
Part (a) asks finite presentability of IA(F_n) for n>3; part (b) asks
linearity for n>2. Neither the star nor the answer to one part settles
the other.

**Part (b): prior negative answer.** Bardakov--Mikhailov,
[*On certain questions of the free group automorphisms theory*](https://arxiv.org/abs/math/0701441v1),
Theorem 5 on printed p10, embeds the non-linear Formanek--Procesi poison
group in IA(F3). Fixing additional free generators embeds IA(F3) in IA(F_n)
for every n>=3. Thus the theorem covers exactly the requested ranks.
Section 4, including its construction, was read; pp9--10 were viewed.
The construction uses inner automorphisms and maps fixing x1,x2 and
sending x3 to x3 a_i, with independent a_i in the commutator subgroup
of F(x1,x2). These maps act trivially on abelianization. The underlying
Formanek--Procesi nonlinearity theorem is imported, not reproved or
formally checked in this audit. No computational verification is claimed.

**Part (a): unresolved here.** Ershov,
[*On finite presentability of some partial Torelli subgroups of Aut(F_n)*](https://arxiv.org/abs/2601.01377v1),
4 January 2026, explicitly retains this question in its introduction.
Theorem 1.1 proves finite presentability of IAC_(n,d) and IAR_(n,d) when
n>=d+115, and of their d=1 cases for n>=26. These are preimages of row
or column stabilizers in GL_n(Z). The full group IA_n occurs at d=n,
outside those inequalities. Finite presentability of these overgroups
does not answer F32(a). The introduction and precise theorem were read,
and printed p2 was viewed. The 85-page proof was not audited. This
January source is dated evidence, not an exhaustive certification that
no later answer exists.

Both versioned PDFs and extracted text are retained, with URLs and
hashes in `literature/F32-scope-sources-v1.json`. The original-page
rendering was reused from the F31 audit after checking its original
HTML hash; F32's selected page is retained separately. The source
download metadata records reading as pending at creation; this note
records the subsequent actual reading and viewing.

Three sequential recorded jobs requested one CPU and 2 decimal GB each.
`f32-scope-sources-v1` failed because its text-output directory did not
exist, after downloading Ershov's PDF. Its exact source is preserved.
`f32-scope-sources-v2` reused those PDF bytes and passed in 1.674 seconds;
`f32-primary-renders-v1` passed in 1.323 seconds. Both successful stderr
logs are empty. This is source/status work, not a mathematical search.

The earlier triage bytes are archived before changing only the F32 row.
The dated scope-ledger snapshot is unchanged pending reconciliation at
closeout. Broader queries for S7 and AUX4 supplied no new proof. O11,
H15 and their exact statements were also reread without a new route.
