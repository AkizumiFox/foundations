# Four Levels of One Proof

Sections 5.1 and 5.2 matched each rule with the phrases that carry it. A dictionary works one word at a time; a proof is read and written whole. This section puts the dictionary to work on two complete proofs, the irrationality of \( \sqrt 2 \) and "uniformly continuous implies continuous", and writes each of them four times: as a full derivation, as a skeleton, as prose with every rule tagged, and as the plain prose of a textbook. The four texts are one proof written for four different readers. The section names the four levels, fixes exactly which steps the last level may leave unsaid, and ends with the use of the levels that matters most to a reader working alone: when a sentence looks doubtful, rewrite it, and only it, at level 1, as a skeleton, and look.

## One proof, four texts

The book has already printed some proofs twice. In Section 2.2 the proof of @thm-sqrt2-irrational appears as a paragraph with a rule in brackets after several of its steps, and then, below it, as a 13-line derivation of its propositional part. In Section 4.10, @exm-uniform-implies-continuous is an 11-line derivation, followed by three sentences of prose with line numbers in brackets. In both places the derivation and the paragraph say the same thing, and the reader is asked to match them. What was not said is how many such texts there are, what each leaves out, and who each is for.

There are four, and the differences between them are not matters of taste.

*A derivation, a skeleton and a paragraph are the same proof; they differ in what the reader is trusted to restore.*

::: {#def-levels-of-proof}
[Levels of Proof]

A proof can be written at four **levels**.

- **Level 0, the full derivation.** A derivation in the sense of @def-derivation, with the rules of Chapters 1, 2 and 4: **every line** is a premise, an assumption, or **one** rule applied to available lines. A derived rule used as one line (@def-derived-rule), such as the bounded rules of @prp-bounded-quantifier-rules, counts as one rule. Facts about numbers enter as premises, or as lines justified "arith", each of which records **one** such fact applied to the lines it cites.
- **Level 1, the skeleton.** The boxes and the logical lines only: every assumption, every flagged name, every line that opens or closes a box, with the rule that closes it, and every line that such a closing line cites. Each stretch of mathematics between them is compressed into one line, justified "arith", "by def", or by a cited result; a stretch of routine logical steps inside one box is compressed into one line justified by the names of its rules in order, such as "\( \rulename{\forall E} \), \( \rulename{\exists I} \)".
- **Level 2, annotated prose.** Sentences, each tagged in brackets with the rule or rules it carries, such as [\( \rulename{\forall I} \)] or [\( \rulename{\exists E} \)].
- **Level 3, plain prose.** Sentences without tags, in which some steps are left unsaid. Which steps may be left unsaid is fixed by the convention that follows, not by the writer.
:::

In words: level 0 hides no logic. Every line other than an arith line can be checked mechanically against the schema of its rule, and each arith line records one fact about numbers that can be checked by hand. Level 1 keeps the logical architecture and lets the arithmetic run in blocks. Level 2 is level 1 turned into sentences, with the architecture still labeled. Level 3 removes the labels and some of the lines, following a fixed convention.

The levels are already on the page in earlier chapters. The derivation in Section 4.10 is level 0. The paragraph after @thm-sqrt2-irrational, with its tags \( [\rulename{{\to}E}] \), \( [\rulename{\wedge I}] \), \( [\rulename{\neg E}] \), \( [\rulename{\neg I}] \), is level 2 for the rules Chapter 2 had; its quantifier steps carry no tags. The derivation printed below that paragraph is not quite level 0, and the reason is instructive: it fixes \( r \), \( p \) and \( q \) in advance and leaves out the two quantifier steps, choosing \( p \), \( q \) (and later \( m \)) and passing from one \( r \) to every \( r \), because Chapter 2 had no rules for them yet. Section 2.2 says so in the paragraph after the derivation. With Chapter 4's rules those steps can be written. The example below writes the choices of \( p \) and \( q \) and the step to every \( r \); the choice of \( m \) stays inside the arithmetic fact of its line 15, since evenness is treated there as a single predicate \( E \).

A **non-example**, by one change: take a level-1 skeleton and delete one of its boxes, say the box in which a name \( N_0 \) is chosen, keeping the lines inside. The result is not a shorter skeleton. It is a list in which \( N_0 \) appears from nowhere, and no reader can tell whether it was chosen, given, or assumed. A skeleton may compress the work inside a box; it may not compress the boxes.

Why four levels and not two? Because each serves a task. Level 0 is for settling a doubt completely: nothing in it is taken on trust. Level 1 is for planning a proof and for reading one: it is what you write on scratch paper before the first sentence (Section 5.5 turns this into a procedure), and what you reconstruct from a textbook when a proof will not come clear (Section 5.4). Level 2 is for learning, which is why Part 0 (Chapters 1–8) uses it and later Parts do not: from Chapter 11, the start of Part I, proofs are written at level 3, in plain prose, and a rule tag appears only where the rule is itself the point, as in a review exercise that looks back at Part 0. Level 3 is what mathematicians read and write.

::: {.warning}
**A skeleton is not a finished proof.** A level-1 text with lines such as "\( \abs{x_0 - y} < \delta_0 \to \abs{f(x_0) - f(y)} < \varepsilon_0 \), arith" is a plan: it says that a computation goes there, and it can hide a computation that does not work. For \( f(x) = x^2 \) on \( \nR \), a skeleton of "\( f \) is uniformly continuous" with one line "arith" at that point looks exactly like a correct skeleton for \( f(x) = 3x + 1 \), where \( \delta = \varepsilon/3 \) works because \( \abs{(3x+1)-(3y+1)} = 3\abs{x-y} \); the claim is false for the first function (@exm-square-not-uniform), and only writing out the arithmetic shows where it fails. Expand every "arith" line before calling the proof done.
:::

## Which steps may be silent

Level 3 leaves things out. If it left out whatever a writer happened to find obvious, a reader could never tell an omission from a gap. So the book fixes the omissions once, by rule. The principle behind the list: a step may go unsaid when a reader who knows the rules can restore it uniquely from what is written. A step that **creates** something (a name, a witness, a case split), **assumes** something, or **cites** something cannot be restored that way, so it is always written.

*Silent steps are the ones whose result is forced by the lines around them; every choice, assumption and citation is spoken.*

::: {#def-silent-steps}
[Silent Steps]

In level-3 prose the following steps **may be silent**, that is, left unwritten:

- \( \rulename{\wedge I} \) when both conjuncts are displayed, and \( \rulename{\wedge E} \);
- \( \rulename{R} \);
- \( \rulename{\vee I} \);
- \( \rulename{\bot E} \), once the contradiction or the empty case has been stated;
- the **name** of \( \rulename{DS} \) (not the fact it uses);
- the exchange of the two members of a disjunction or of a conjunction (@exm-disjunction-first-derivations, @prp-and-commutes), made only to match the schema of a rule, with no citation;
- \( \rulename{{\leftrightarrow}E} \) with a definition ("that is", "by definition", or nothing);
- \( \rulename{\forall E} \) at the obvious term;
- \( \rulename{{\to}E} \) whose implication is a line already in the proof that is neither a hypothesis of the statement, nor a cited result, nor an instance of one (for instance, an instance of the property of a chosen name), when its antecedent is displayed or has just been assumed;
- \( \rulename{{=}I} \) and \( \rulename{{=}E} \) inside a chain of equalities or inequalities;
- the phrase "it suffices to show", when the claim of the cut is displayed and then used;
- the **closing** lines of \( \rulename{{\to}I} \) ("hence if \( P \) then \( Q \)"), of \( \rulename{\forall I} \) ("since \( x \) was arbitrary"), of \( \rulename{\vee E} \) ("in either case") and of \( \rulename{\exists E} \) (the conclusion repeated outside the box of the chosen name).

The following are **never silent**:

- the openings of \( \rulename{{\to}I} \), \( \rulename{\neg I} \), \( \rulename{RAA} \) and \( \rulename{\forall I} \), and of \( \rulename{\exists E} \) **with a fresh name**;
- the conclusions of \( \rulename{\neg I} \) and of \( \rulename{RAA} \) ("hence \( \neg P \)", "hence \( P \)");
- a \( \rulename{\neg\neg E} \) or \( \rulename{LEM} \) step, written as an explicit case split or as an explicit removal of a double negation (@prp-double-negation (b); "\( P \) must hold, since …"), with the flag of Section 5.7 when the step is genuinely non-constructive;
- the case split of \( \rulename{\vee E} \), with the reason the cases exhaust;
- the clash of \( \rulename{\neg E} \): both members of the clashing pair are named;
- the witness of \( \rulename{\exists I} \), with what it depends on;
- an instance of \( \rulename{\forall E} \) at a term that is not the obvious one;
- every citation, and so every \( \rulename{{\to}E} \) whose implication is a hypothesis of the statement or a cited result, or an instance of one;
- both directions of \( \rulename{{\leftrightarrow}I} \), and both halves of an \( \exists! \) proof;
- the base case and the step of an induction, with the induction hypothesis stated;
- the announcement of a contrapositive;
- the negated form, after De Morgan (@prp-de-morgan) or a quantifier negation (@prp-quantifier-negation, @prp-bounded-quantifier-negation);
- the claim of a cut;
- a "without loss of generality", together with the symmetry that licenses it.
:::

The two lists collect the last column of the dictionary in Sections 5.1 and 5.2 in one place, together with the requirements stated in the text under its tables: the reason a case split exhausts and the flag on a genuinely non-constructive step (Section 5.1), and chains of inequalities as well as equalities (Section 5.2). The dictionary gives each row its phrase and an example, and this definition gives the reader one list to check against. Two items are made explicit here that the dictionary leaves implicit. The first is the \( \rulename{{\to}E} \) whose implication is a line already in the proof rather than a citation, as in "for every \( n \ge N \)" after \( N \) is chosen. The second is the closing line of \( \rulename{\exists E} \), which the dictionary's row for \( \rulename{\exists E} \) leaves implicit: when a proof says "choose \( N \) such that …" and goes on to prove something that does not mention \( N \), the \( \rulename{\exists E} \) line that carries that conclusion outside the box of \( N \) is never written in prose. What is written is the choice, with its fresh name.

Read the two lists against the principle. Everything in the first list is forced. \( \rulename{\wedge E} \) has one premise and two possible conclusions, and the next sentence shows which was used. The closing line of a box is determined by the box. \( \rulename{\forall E} \) at the obvious term \( x \), when \( x \) is the name in sight, is forced by the sentence that uses it. Everything in the second list carries information that the surrounding lines do not determine. Which name is chosen, and that it is fresh; which witness, and what it depends on; which cases, and why they are all the cases; which result is cited. A reader who meets "Then \( p \) is even" with no citation has to guess what licensed it, and a guess is not a check.

A small example. In "since \( x \in (0, 1) \), in particular \( x > 0 \)", the step from the conjunction "\( 0 < x \) and \( x < 1 \)" to its first conjunct is \( \rulename{\wedge E} \), and the unwinding of \( x \in (0, 1) \) into that conjunction is \( \rulename{{\leftrightarrow}E} \) with the definition of an interval. Both may be silent, and here the writer kept the phrase "in particular" anyway, which is allowed: the convention says what **may** be omitted, never what must be. On the other side, "suppose \( r^2 = 2 \)" can never be omitted from the proof of @thm-sqrt2-irrational: without it, the reader does not know that a box has opened, and the final "\( r^2 \ne 2 \)" has no visible source.

::: {.warning}
**Level 3 is not level 0 with steps missing at random.** A proof that skips the reason a case split is exhaustive, or chooses \( \delta \) without saying what it depends on, or uses a lemma without naming it, is not "written at level 3": it has a gap, because those steps are in the never-silent list. Conversely, a proof that omits "since \( \varepsilon \) was arbitrary" has no gap. When you judge whether a written proof is complete, judge it against @def-silent-steps, not against your sense of what is obvious.
:::

## The irrationality of the square root of two, four times

The first example is the proof of @thm-sqrt2-irrational, now with every quantifier step written. It uses the fact that Section 2.2 calls (L): every rational number is \( p/q \) for integers \( p \), \( q \) with \( q \ne 0 \), not both even. Write \( E(x) \) for "\( x \) is even". The proof uses only two clauses of (L), and in a convenient form: \( r = p/q \) with \( q \ne 0 \) gives \( p = r \cdot q \), which avoids division; and "not both even" is \( \neg(E(p) \wedge E(q)) \). The clause \( q \ne 0 \) is then not needed at all, since \( q = 0 \) would force \( p = 0 \), and both would be even. It also uses @thm-square-even-implies-even, which we write as the formula \( \forall n \in \nZ \; (E(n \cdot n) \to E(n)) \).

::: {#exm-sqrt2-four-levels}
[The irrationality of the square root of two at four levels]

Write the proof of @thm-sqrt2-irrational, that no rational number has square \( 2 \), at levels 0, 1, 2 and 3 of @def-levels-of-proof, and match the levels line by line.
:::

::: {.idea}
The move this example shows in full is **skeleton first**: before any arithmetic, write the first and the last line of every box. The goal \( \forall r \in \nQ \; \neg(r \cdot r = 2) \) dictates the outer box (\( \rulename{\forall I} \), "let \( r \in \nQ \)") and the next one (\( \rulename{\neg I} \), "suppose \( r^2 = 2 \)", ending in \( \bot \)). Inside, (L) instantiated at \( r_0 \) is an existential, so its \( \rulename{\exists E} \) boxes open at once, with fresh names \( p_0 \), \( q_0 \), and they too end in \( \bot \). Only then is there something to compute: the arithmetic fills the innermost box, and it has a target, the clash with "not both even". Sections 5.5 and 5.6 come back to this move twice, with parts of the proof left blank.

*Before reading on: the level-3 proof below has four sentences. Which lines of the level-0 derivation does its second sentence, "By (L), write \( r = p/q \) …", stand for?*
:::

::: {.solution}
**Level 0.** Premise 1 is (L) in the form above, premise 2 is @thm-square-even-implies-even. The derivation has 24 lines.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall r \in \nQ \; \exists p \in \nZ \; \exists q \in \nZ \; (p = r \cdot q \wedge \neg(E(p) \wedge E(q)))}
  \hypo {2} {\forall n \in \nZ \; (E(n \cdot n) \to E(n))}
  \open[r_0]
  \hypo {3} {r_0 \in \nQ}
  \open
  \hypo {4} {r_0 \cdot r_0 = 2}
  \have {5} {\exists p \in \nZ \; \exists q \in \nZ \; (p = r_0 \cdot q \wedge \neg(E(p) \wedge E(q)))} \Ae{1,3}
  \open[p_0]
  \hypo {6} {p_0 \in \nZ}
  \hypo {7} {\exists q \in \nZ \; (p_0 = r_0 \cdot q \wedge \neg(E(p_0) \wedge E(q)))}
  \open[q_0]
  \hypo {8} {q_0 \in \nZ}
  \hypo {9} {p_0 = r_0 \cdot q_0 \wedge \neg(E(p_0) \wedge E(q_0))}
  \have {10} {p_0 = r_0 \cdot q_0} \ae{9}
  \have {11} {p_0 \cdot p_0 = 2 \cdot (q_0 \cdot q_0)} \by{arith}{4,10}
  \have {12} {E(p_0 \cdot p_0)} \by{arith}{8,11}
  \have {13} {E(p_0 \cdot p_0) \to E(p_0)} \Ae{2,6}
  \have {14} {E(p_0)} \ie{13,12}
  \have {15} {E(q_0 \cdot q_0)} \by{arith}{6,8,11,14}
  \have {16} {E(q_0 \cdot q_0) \to E(q_0)} \Ae{2,8}
  \have {17} {E(q_0)} \ie{16,15}
  \have {18} {E(p_0) \wedge E(q_0)} \ai{14,17}
  \have {19} {\neg(E(p_0) \wedge E(q_0))} \ae{9}
  \have {20} {\bot} \ne{18,19}
  \close
  \have {21} {\bot} \Ee{7,8-20}
  \close
  \have {22} {\bot} \Ee{5,6-21}
  \close
  \have {23} {\neg(r_0 \cdot r_0 = 2)} \ni{4-22}
  \close
  \have {24} {\forall r \in \nQ \; \neg(r \cdot r = 2)} \Ai{3-23}
\end{nd}$
\end{center}
```

The three "arith" lines are facts about integers, each checkable by hand. Line 11: \( p_0 \cdot p_0 = (r_0 q_0)(r_0 q_0) = (r_0 \cdot r_0)(q_0 \cdot q_0) = 2 \cdot (q_0 \cdot q_0) \), by lines 10 and 4. Line 12: \( p_0 \cdot p_0 \) is \( 2 \) times the integer \( q_0 \cdot q_0 \), so it is even. Line 15: by line 14, \( p_0 = 2m \) for an integer \( m \); then line 11 reads \( 4m^2 = 2 q_0^2 \), so \( q_0^2 = 2m^2 \) is even. The side conditions at the flagged lines hold: at line 21 the flag \( q_0 \) is not in \( \bot \), in line 7, in a premise, or in the assumptions still open (lines 3, 4, 6, 7); at line 22 the flag \( p_0 \) is not in \( \bot \), in line 5, in a premise, or in lines 3 and 4; at line 24 the flag \( r_0 \) is in no premise and not in line 24.

**Level 1.** Lines 10–17, the \( \rulename{\wedge E} \) that extracts \( p_0 = r_0 \cdot q_0 \), the arithmetic and the two uses of @thm-square-even-implies-even, cited as "lemma", are compressed into two lines, and the logical steps of lines 18–20 into one line; every box, every assumption and every closing line is kept.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall r \in \nQ \; \exists p \in \nZ \; \exists q \in \nZ \; (p = r \cdot q \wedge \neg(E(p) \wedge E(q)))}
  \open[r_0]
  \hypo {2} {r_0 \in \nQ}
  \open
  \hypo {3} {r_0 \cdot r_0 = 2}
  \have {4} {\exists p \in \nZ \; \exists q \in \nZ \; (p = r_0 \cdot q \wedge \neg(E(p) \wedge E(q)))} \Ae{1,2}
  \open[p_0]
  \hypo {5} {p_0 \in \nZ}
  \hypo {6} {\exists q \in \nZ \; (p_0 = r_0 \cdot q \wedge \neg(E(p_0) \wedge E(q)))}
  \open[q_0]
  \hypo {7} {q_0 \in \nZ}
  \hypo {8} {p_0 = r_0 \cdot q_0 \wedge \neg(E(p_0) \wedge E(q_0))}
  \have {9} {E(p_0)} \by{$\wedge$E; arith; lemma}{3,5,7,8}
  \have {10} {E(q_0)} \by{arith; lemma}{3,5,7,8,9}
  \have {11} {\bot} \by{$\wedge$E, $\wedge$I, $\neg$E}{8,9,10}
  \close
  \have {12} {\bot} \Ee{6,7-11}
  \close
  \have {13} {\bot} \Ee{4,5-12}
  \close
  \have {14} {\neg(r_0 \cdot r_0 = 2)} \ni{3-13}
  \close
  \have {15} {\forall r \in \nQ \; \neg(r \cdot r = 2)} \Ai{2-14}
\end{nd}$
\end{center}
```

Level-1 line 9 is level-0 lines 10–14; line 10 is lines 15–17; line 11 is lines 18–20. Premise 2 is not a line of level 1; it is cited as "lemma". Every other line of level 1 is a line of level 0, renumbered.

**Level 2.**

> Let \( r \in \nQ \) [\( \rulename{\forall I} \): the box of \( r_0 \)], and suppose \( r^2 = 2 \) [assumption for \( \rulename{\neg I} \)]. By (L), there are integers \( p \) and \( q \) with \( p = rq \), not both even; choose such \( p \) and \( q \) [\( \rulename{\forall E} \) at \( r \), then \( \rulename{\exists E} \) twice, with fresh names]. Then \( p^2 = r^2 q^2 = 2q^2 \) [arith], so \( p^2 \) is even [arith], and by @thm-square-even-implies-even \( p \) is even [\( \rulename{\forall E} \) at \( p \), \( \rulename{{\to}E} \)]. Writing \( p = 2m \), we get \( 4m^2 = 2q^2 \), so \( q^2 = 2m^2 \) is even [arith], and by the same theorem \( q \) is even [\( \rulename{\forall E} \) at \( q \), \( \rulename{{\to}E} \)]. So \( p \) and \( q \) are both even [\( \rulename{\wedge I} \)], while they were chosen not both even: a contradiction [\( \rulename{\neg E} \); then \( \rulename{\exists E} \) twice, since \( \bot \) mentions neither \( p \) nor \( q \)]. Hence \( r^2 \ne 2 \) [\( \rulename{\neg I} \)]. Since \( r \) was arbitrary, no rational number has square \( 2 \) [\( \rulename{\forall I} \)].

**Level 3.**

> Let \( r \) be rational, and suppose \( r^2 = 2 \). By (L), write \( r = p/q \) with integers \( p \), \( q \), not both even. Then \( p^2 = 2q^2 \), so \( p^2 \) is even, and \( p \) is even by @thm-square-even-implies-even; writing \( p = 2m \) gives \( q^2 = 2m^2 \), so \( q \) is even by the same theorem. Thus \( p \) and \( q \) are both even, a contradiction; hence \( r^2 \ne 2 \).

The answer to the prompt: "By (L), write \( r = p/q \) with integers \( p \), \( q \), not both even" stands for line 5 (\( \rulename{\forall E} \) of premise 1 at \( r_0 \)) and for the openings of the two \( \rulename{\exists E} \) boxes, lines 6–9. It also displays the conjunct, in the form \( r = p/q \), on its own, so the \( \rulename{\wedge E} \) of line 10 that extracts it has nothing left to say and can be silent.
:::

Look at what the four texts share. Every level has the box of \( r \), the box of the assumption \( r^2 = 2 \), the choice of \( p \) and \( q \), two uses of the lemma, and a contradiction followed by "hence \( r^2 \ne 2 \)". That common part is the proof; the rest is how much of the routine work each reader is trusted to do. The skeleton is the place where you can see it most clearly: fifteen lines, of which only lines 9 and 10 carry the mathematics; every other line is a decision about logic.

::: {.check}
Which lines of the level-0 derivation in @exm-sqrt2-four-levels have no counterpart in the level-3 text, and which item of @def-silent-steps lets each go?
:::

::: {.solution}
Eight lines. Line 5 is \( \rulename{\forall E} \) of premise 1 at the obvious term \( r_0 \), the name in sight; "By (L)" cites premise 1, and the instance is not written. Lines 10 and 19 are \( \rulename{\wedge E} \). Lines 13 and 16 are \( \rulename{\forall E} \) of the lemma at the obvious terms \( p_0 \) and \( q_0 \); the citations "by @thm-square-even-implies-even" and "by the same theorem" remain, and they are the \( \rulename{{\to}E} \) lines 14 and 17. Lines 21 and 22 are the closing lines of the two \( \rulename{\exists E} \) boxes. Line 24 is the closing line of \( \rulename{\forall I} \): level 3 never says "since \( r \) was arbitrary". Every other line has a phrase: lines 1 and 2, the premises, are the citations "By (L)" and "by @thm-square-even-implies-even"; lines 3, 4, 6–9 the openings; lines 11, 12, 15 the arithmetic; lines 14, 17 the citations; lines 18 and 20 the clash, "both even, a contradiction", which names the pair through "not both even" two sentences earlier; and line 23, "hence \( r^2 \ne 2 \)", the conclusion of \( \rulename{\neg I} \), which is never silent.
:::

## Uniform continuity, four times

The second example has no arithmetic at all. That makes it a good test of the levels: what is left when there is nothing to compress?

::: {#exm-uniform-four-levels}
[Uniformly continuous implies continuous, at four levels]

Write the proof of @exm-uniform-implies-continuous, that a function uniformly continuous on \( A \) is continuous at every point of \( A \), at levels 0, 1, 2 and 3, and say where each level records what \( \delta \) depends on.
:::

::: {.solution}
**Level 0** is the derivation of @exm-uniform-implies-continuous, copied here with the same line numbers. Line 1 is uniform continuity (UC), line 11 is continuity at every point (C).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall \varepsilon > 0 \; \exists \delta > 0 \; \forall x \in A \; \forall y \in A \; (\abs{x - y} < \delta \to \abs{f(x) - f(y)} < \varepsilon)}
  \open[x_0]
  \hypo {2} {x_0 \in A}
  \open[\varepsilon_0]
  \hypo {3} {\varepsilon_0 > 0}
  \have {4} {\exists \delta > 0 \; \forall x \in A \; \forall y \in A \; (\abs{x - y} < \delta \to \abs{f(x) - f(y)} < \varepsilon_0)} \Ae{1,3}
  \open[\delta_0]
  \hypo {5} {\delta_0 > 0}
  \hypo {6} {\forall x \in A \; \forall y \in A \; (\abs{x - y} < \delta_0 \to \abs{f(x) - f(y)} < \varepsilon_0)}
  \have {7} {\forall y \in A \; (\abs{x_0 - y} < \delta_0 \to \abs{f(x_0) - f(y)} < \varepsilon_0)} \Ae{6,2}
  \have {8} {\exists \delta > 0 \; \forall y \in A \; (\abs{x_0 - y} < \delta \to \abs{f(x_0) - f(y)} < \varepsilon_0)} \Ei{5,7}
  \close
  \have {9} {\exists \delta > 0 \; \forall y \in A \; (\abs{x_0 - y} < \delta \to \abs{f(x_0) - f(y)} < \varepsilon_0)} \Ee{4,5-8}
  \close
  \have {10} {\forall \varepsilon > 0 \; \exists \delta > 0 \; \forall y \in A \; (\abs{x_0 - y} < \delta \to \abs{f(x_0) - f(y)} < \varepsilon)} \Ai{3-9}
  \close
  \have {11} {\forall x \in A \; \forall \varepsilon > 0 \; \exists \delta > 0 \; \forall y \in A \; (\abs{x - y} < \delta \to \abs{f(x) - f(y)} < \varepsilon)} \Ai{2-10}
\end{nd}$
\end{center}
```

**Level 1.** Every line of level 0 other than the premise opens or closes a box, or is cited by a closing line, except line 7: lines 7 and 8, which specialize the chosen \( \delta_0 \) to the point \( x_0 \) and repackage the result, are the one stretch of work inside a box. They become one line.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall \varepsilon > 0 \; \exists \delta > 0 \; \forall x \in A \; \forall y \in A \; (\abs{x - y} < \delta \to \abs{f(x) - f(y)} < \varepsilon)}
  \open[x_0]
  \hypo {2} {x_0 \in A}
  \open[\varepsilon_0]
  \hypo {3} {\varepsilon_0 > 0}
  \have {4} {\exists \delta > 0 \; \forall x \in A \; \forall y \in A \; (\abs{x - y} < \delta \to \abs{f(x) - f(y)} < \varepsilon_0)} \Ae{1,3}
  \open[\delta_0]
  \hypo {5} {\delta_0 > 0}
  \hypo {6} {\forall x \in A \; \forall y \in A \; (\abs{x - y} < \delta_0 \to \abs{f(x) - f(y)} < \varepsilon_0)}
  \have {7} {\exists \delta > 0 \; \forall y \in A \; (\abs{x_0 - y} < \delta \to \abs{f(x_0) - f(y)} < \varepsilon_0)} \by{$\forall$E, $\exists$I}{2,5,6}
  \close
  \have {8} {\exists \delta > 0 \; \forall y \in A \; (\abs{x_0 - y} < \delta \to \abs{f(x_0) - f(y)} < \varepsilon_0)} \Ee{4,5-7}
  \close
  \have {9} {\forall \varepsilon > 0 \; \exists \delta > 0 \; \forall y \in A \; (\abs{x_0 - y} < \delta \to \abs{f(x_0) - f(y)} < \varepsilon)} \Ai{3-8}
  \close
  \have {10} {\forall x \in A \; \forall \varepsilon > 0 \; \exists \delta > 0 \; \forall y \in A \; (\abs{x - y} < \delta \to \abs{f(x) - f(y)} < \varepsilon)} \Ai{2-9}
\end{nd}$
\end{center}
```

**Level 2.**

> Let \( x \in A \) [\( \rulename{\forall I} \)] and let \( \varepsilon > 0 \) [\( \rulename{\forall I} \)]. By uniform continuity, applied at \( \varepsilon \) [\( \rulename{\forall E} \)], there is \( \delta > 0 \) such that \( \abs{u - v} < \delta \) implies \( \abs{f(u) - f(v)} < \varepsilon \) for all \( u, v \in A \); choose such a \( \delta \), which depends on \( \varepsilon \) only [\( \rulename{\exists E} \)]. Taking \( u = x \) [\( \rulename{\forall E} \)], every \( y \in A \) with \( \abs{x - y} < \delta \) has \( \abs{f(x) - f(y)} < \varepsilon \). So this \( \delta \) works for \( x \) and \( \varepsilon \) [\( \rulename{\exists I} \); then \( \rulename{\exists E} \) closes, since "some \( \delta \) works" does not mention the chosen one]. Since \( \varepsilon \) and \( x \) were arbitrary, \( f \) is continuous at every point of \( A \) [\( \rulename{\forall I} \) twice].

As in Section 4.10, the prose renames the bound variables of UC to \( u \), \( v \), so that \( x \) can name the fixed point.

**Level 3.**

> Let \( x \in A \) and \( \varepsilon > 0 \). By uniform continuity, choose \( \delta > 0 \) (depending on \( \varepsilon \) only) such that \( \abs{f(u) - f(v)} < \varepsilon \) for all \( u, v \in A \) with \( \abs{u - v} < \delta \). In particular \( \abs{f(x) - f(y)} < \varepsilon \) for every \( y \in A \) with \( \abs{x - y} < \delta \), so this \( \delta \) works for \( x \) and \( \varepsilon \).

**Where the dependence of \( \delta \) is recorded.** At level 0, in two places: the box of \( \delta_0 \) lies inside the boxes of \( x_0 \) and \( \varepsilon_0 \), so \( \delta_0 \) **may** depend on both; and the line it comes from, line 4, mentions \( \varepsilon_0 \) and not \( x_0 \), so it **does** depend only on \( \varepsilon_0 \) (Section 4.10). At level 1 the record is the same, lines 3 to 5 being unchanged. At level 2 it is the clause "which depends on \( \varepsilon \) only", placed at the \( \rulename{\exists E} \) tag, after the \( \rulename{\forall E} \) at \( \varepsilon \) that produced it. At level 3 it is the parenthesis "(depending on \( \varepsilon \) only)", and nothing else: the parenthesis is the whole of the box structure that survives.
:::

Here the gap between level 0 and level 1 is one line, because there is no arithmetic to compress. The large step is from level 1 to level 3: ten lines become three sentences. What the level-3 text keeps is exactly the never-silent part of @def-silent-steps: the openings of the two \( \rulename{\forall I} \) boxes ("let \( x \in A \) and \( \varepsilon > 0 \)"), the citation and the choice with its fresh name ("by uniform continuity, choose \( \delta \)"), the dependence of the witness, and the witness itself ("this \( \delta \) works"). The \( \rulename{\forall E} \) at \( u = x \) is the obvious instance and is reduced to "in particular". The \( \rulename{\exists E} \) closing line 9 and the two \( \rulename{\forall I} \) closing lines 10 and 11 of level 0 are silent.

## Expand to check

The levels are not only a way to write. They are a way to check. When a sentence of a level-3 proof leaves you uneasy, rewrite that stretch, and only that stretch, at level 1. Either every line of the expansion is legal, and the doubt is settled, or one line breaks a rule, and you have found the error and its exact address.

Here is a sentence that sounds like the level-3 proof above run backwards, from continuity to uniform continuity.

> Let \( \varepsilon > 0 \). For each \( x \in A \), continuity at \( x \) gives some \( \delta > 0 \) such that \( \abs{f(x) - f(y)} < \varepsilon \) for every \( y \in A \) with \( \abs{x - y} < \delta \). Hence, choosing \( \delta \) as above for every \( x \), we have \( \abs{f(x) - f(y)} < \varepsilon \) whenever \( x, y \in A \) and \( \abs{x - y} < \delta \), so \( f \) is uniformly continuous on \( A \).

Expand it. "Let \( \varepsilon > 0 \)" opens a box for \( \varepsilon_0 \). "For each \( x \in A \)" opens a box for \( x_0 \). "Continuity at \( x \) gives some \( \delta \)" is \( \rulename{\forall E} \) twice and the opening of an \( \rulename{\exists E} \) box for \( \delta_0 \). At level 1, with the line the sentence needs as line 7, its rule marked with a question mark:

```{=latex}
% expect-invalid
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x \in A \; \forall \varepsilon > 0 \; \exists \delta > 0 \; \forall y \in A \; (\abs{x - y} < \delta \to \abs{f(x) - f(y)} < \varepsilon)}
  \open[\varepsilon_0]
  \hypo {2} {\varepsilon_0 > 0}
  \open[x_0]
  \hypo {3} {x_0 \in A}
  \have {4} {\exists \delta > 0 \; \forall y \in A \; (\abs{x_0 - y} < \delta \to \abs{f(x_0) - f(y)} < \varepsilon_0)} \by{$\forall$E twice}{1,3,2}
  \open[\delta_0]
  \hypo {5} {\delta_0 > 0}
  \hypo {6} {\forall y \in A \; (\abs{x_0 - y} < \delta_0 \to \abs{f(x_0) - f(y)} < \varepsilon_0)}
  \have {7} {\forall x \in A \; \forall y \in A \; (\abs{x - y} < \delta_0 \to \abs{f(x) - f(y)} < \varepsilon_0)} \by{$\forall$I?}{3-6}
  \close
  \close
  \close
\end{nd}$
\end{center}
```

Line 7 is what the phrase "choosing \( \delta \) as above for every \( x \)" needs: one \( \delta_0 \) that works for all \( x \) and \( y \), so that \( \rulename{\exists I} \) can then produce UC's \( \exists \delta \) inside the box of \( \varepsilon_0 \). But line 7 would be a \( \rulename{\forall I} \) over \( x_0 \), and no such step is legal here. The box of \( x_0 \) opened at line 3 is still open, so \( \rulename{\forall I} \) cannot cite it; and a new box with the flag \( x_0 \), opened inside the box of \( \delta_0 \), breaks the side condition of \( \rulename{\forall I} \) (@def-rules-universal), because \( x_0 \) appears in the open assumptions on lines 3 and 6. The phrase "for every \( x \)" has generalized over a name on which the chosen \( \delta_0 \) depends. This is the first blocked line of @exm-converse-fails, met there in the search; here it was found by expanding one English sentence. Section 5.6 catalogues the error, and @exm-square-not-uniform shows that no repair is possible: for \( x^2 \) on \( \nR \) the conclusion is false.

The expansion took six lines, and it was enough to expand the one doubtful stretch. That is the general pattern: you never need to rewrite a whole proof at level 0 to check it. Find the sentence you do not trust, find the boxes open at that sentence, and write the few lines it stands for.

## Exercises

### A. Check your understanding

::: {#exr-levels-of-abbreviation-a1}
[A1]

Parts (a)–(c) are about @exm-uniform-four-levels, parts (d) and (e) about @exm-sqrt2-four-levels.

::: {.enumerate options="label=(\alph*)"}
1. Which lines of the level-0 derivation does the level-3 sentence "Let \( x \in A \) and \( \varepsilon > 0 \)" stand for? Which of them open a box and which close one, and which are written at level 3?
2. Where is the dependence of \( \delta \) recorded at each of the four levels?
3. State the idea of the proof in two sentences.
4. At which line of each of the four levels is the "not both even" clause of (L) used to reach the contradiction?
5. True or false, with a reason: at level 3, the sentence "hence \( r^2 \ne 2 \)" may be left out of the proof of @thm-sqrt2-irrational, since the reader has just been told that a contradiction was reached.
:::
:::

::: {.solution}
*(a)* Lines 2, 3, 10 and 11. Lines 2 and 3 open the flagged boxes of \( x_0 \) and \( \varepsilon_0 \), with their bounds \( x_0 \in A \) and \( \varepsilon_0 > 0 \); lines 10 and 11 close them by \( \rulename{\forall I} \). The openings are written ("let"); the closings are silent at level 3 (@def-silent-steps), and at level 2 they are the sentence "since \( \varepsilon \) and \( x \) were arbitrary".

*(b)* At level 0 and level 1: the box of \( \delta_0 \) sits inside the boxes of \( x_0 \) and \( \varepsilon_0 \), and the line it comes from (line 4) mentions \( \varepsilon_0 \) only. At level 2: the clause "which depends on \( \varepsilon \) only" at the \( \rulename{\exists E} \) tag. At level 3: the parenthesis "(depending on \( \varepsilon \) only)".

*(c)* Uniform continuity at \( \varepsilon \) provides one \( \delta \) that serves all pairs of points of \( A \) at once, and it provides it before any point is named. Continuity at a point \( x \) asks only for the pairs whose first point is \( x \), so the same \( \delta \) works.

*(d)* Level 0: the clause is line 9's second conjunct, taken out by \( \rulename{\wedge E} \) at line 19 and used in the \( \rulename{\neg E} \) of line 20. Level 1: it is the second conjunct of the assumption on line 8, used at line 11. Level 2: "while they were chosen not both even: a contradiction". Level 3: "Thus \( p \) and \( q \) are both even, a contradiction", where the clash refers back to "not both even" in the sentence that chose \( p \) and \( q \).

*(e)* False. "Hence \( r^2 \ne 2 \)" is the conclusion of \( \rulename{\neg I} \), which @def-silent-steps puts among the steps that are never silent. A contradiction alone does not say which assumption it refutes; in this proof the boxes of \( p \), \( q \) and of \( r^2 = 2 \) are all open when it is reached, and the sentence says which box closes and what it gives.
:::

### B. Practice

::: {#exr-levels-of-abbreviation-b1}
[B1: Some-all gives all-some, on the natural numbers]

Read @prp-exists-forall-swap over the domain \( \nN \), with \( R(x, y) \) as "\( x \le y \)": from \( \exists x\, \forall y\, (x \le y) \), conclude \( \forall y\, \exists x\, (x \le y) \). The premise is true, with the witness \( x = 0 \). Write the proof at levels 1, 2 and 3. Your proof must use the premise, although this instance of the conclusion also has a one-line proof, with \( x = y \).
:::

::: {.solution}
**Level 1.** The proof has no arithmetic, so the skeleton is the level-0 derivation of @prp-exists-forall-swap with \( R(x, y) \) read as \( x \le y \):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\exists x \, \forall y \, (x \le y)}
  \open[y_0]
  \open[x_0]
  \hypo {2} {\forall y \, (x_0 \le y)}
  \have {3} {x_0 \le y_0} \Ae{2}
  \have {4} {\exists x \, (x \le y_0)} \Ei{3}
  \close
  \have {5} {\exists x \, (x \le y_0)} \Ee{1,2-4}
  \close
  \have {6} {\forall y \, \exists x \, (x \le y)} \Ai{2-5}
\end{nd}$
\end{center}
```

**Level 2.**

> Let \( y \in \nN \) [\( \rulename{\forall I} \)]. By hypothesis, some natural number is at most every natural number; choose such a number \( x_0 \), which depends on nothing, since the hypothesis mentions no \( y \) [\( \rulename{\exists E} \), \( x_0 \) fresh]. In particular \( x_0 \le y \) [\( \rulename{\forall E} \) at \( y \)], so some natural number is at most \( y \) [\( \rulename{\exists I} \) with witness \( x_0 \); then \( \rulename{\exists E} \) closes, since this does not mention \( x_0 \)]. Since \( y \) was arbitrary, every natural number has a natural number at most it [\( \rulename{\forall I} \)].

**Level 3.**

> Let \( y \in \nN \). By hypothesis, choose \( x_0 \in \nN \) with \( x_0 \le z \) for every \( z \in \nN \); the hypothesis does not mention \( y \), so \( x_0 \) does not depend on \( y \). In particular \( x_0 \le y \), so \( x_0 \) is a natural number at most \( y \).

The level-3 text renames the bound variable of the hypothesis to \( z \), so that \( y \) can name the fixed number. The witness \( x_0 \) was chosen inside the box of \( y_0 \), but it comes from line 1, which mentions no \( y \); so it does not depend on \( y \). The one-line proof, "\( y \le y \), so take \( x = y \)", is \( \rulename{\exists I} \) with the witness \( y \), which **does** depend on \( y \). Both prove the conclusion; only the first is an instance of @prp-exists-forall-swap, and only the first shows that a single \( x \) serves every \( y \).
:::

::: {#exr-levels-of-abbreviation-b2}
[B2: Back from prose to a skeleton]

Here is a level-3 proof.

> **Claim.** If \( n \) is an odd integer, then \( 8 \mid n^2 - 1 \).
>
> Let \( n \) be odd, say \( n = 2k + 1 \) with \( k \) an integer. Then \( n^2 - 1 = 4k(k + 1) \), so it suffices to show that \( k(k + 1) \) is even. If \( k = 2j \) for an integer \( j \), then \( k(k + 1) = 2 \cdot j(2j + 1) \); if \( k = 2j + 1 \), then \( k(k + 1) = 2 \cdot (2j + 1)(j + 1) \). Either way \( k(k + 1) = 2i \) for an integer \( i \), and then \( n^2 - 1 = 8i \).

Reconstruct its level-1 skeleton. Work over the domain \( \nZ \), with "\( n \) is odd" as \( \exists k\, (n = 2k + 1) \) and \( 8 \mid m \) as \( \exists t\, (m = 8t) \). Name the rule that closes each box, and say where the proof uses the fact (E1) of Section 2.1, that every integer is even or odd.
:::

::: {.solution}
The goal is \( \forall n\, (\exists k\, (n = 2k + 1) \to \exists t\, (n^2 - 1 = 8t)) \): its skeleton is a \( \rulename{\forall I} \) box for \( n_0 \), and inside it a \( \rulename{{\to}I} \) box. The hypothesis is an existential, so its \( \rulename{\exists E} \) box (name \( k_0 \)) opens at once. "It suffices to show that \( k(k+1) \) is even" is a cut: the claim \( \exists i\, (k_0(k_0 + 1) = 2i) \) is proved by \( \rulename{\vee E} \) on (E1) for \( k_0 \), with an \( \rulename{\exists E} \) and an \( \rulename{\exists I} \) in each case, and is then used through one more \( \rulename{\exists E} \) and the final \( \rulename{\exists I} \).

```{=latex}
\begin{center}
$\begin{nd}
  \open[n_0]
  \open
  \hypo {1} {\exists k \, (n_0 = 2 \cdot k + 1)}
  \open[k_0]
  \hypo {2} {n_0 = 2 \cdot k_0 + 1}
  \have {3} {n_0 \cdot n_0 - 1 = 4 \cdot (k_0 \cdot (k_0 + 1))} \by{arith}{2}
  \have {4} {\exists j \, (k_0 = 2 \cdot j) \vee \exists j \, (k_0 = 2 \cdot j + 1)} \by{(E1)}{}
  \open
  \hypo {5} {\exists j \, (k_0 = 2 \cdot j)}
  \open[j_0]
  \hypo {6} {k_0 = 2 \cdot j_0}
  \have {7} {k_0 \cdot (k_0 + 1) = 2 \cdot (j_0 \cdot (2 \cdot j_0 + 1))} \by{arith}{6}
  \have {8} {\exists i \, (k_0 \cdot (k_0 + 1) = 2 \cdot i)} \Ei{7}
  \close
  \have {9} {\exists i \, (k_0 \cdot (k_0 + 1) = 2 \cdot i)} \Ee{5,6-8}
  \close
  \open
  \hypo {10} {\exists j \, (k_0 = 2 \cdot j + 1)}
  \open[j_1]
  \hypo {11} {k_0 = 2 \cdot j_1 + 1}
  \have {12} {k_0 \cdot (k_0 + 1) = 2 \cdot ((2 \cdot j_1 + 1) \cdot (j_1 + 1))} \by{arith}{11}
  \have {13} {\exists i \, (k_0 \cdot (k_0 + 1) = 2 \cdot i)} \Ei{12}
  \close
  \have {14} {\exists i \, (k_0 \cdot (k_0 + 1) = 2 \cdot i)} \Ee{10,11-13}
  \close
  \have {15} {\exists i \, (k_0 \cdot (k_0 + 1) = 2 \cdot i)} \oe{4,5-9,10-14}
  \open[i_0]
  \hypo {16} {k_0 \cdot (k_0 + 1) = 2 \cdot i_0}
  \have {17} {n_0 \cdot n_0 - 1 = 8 \cdot i_0} \by{arith}{3,16}
  \have {18} {\exists t \, (n_0 \cdot n_0 - 1 = 8 \cdot t)} \Ei{17}
  \close
  \have {19} {\exists t \, (n_0 \cdot n_0 - 1 = 8 \cdot t)} \Ee{15,16-18}
  \close
  \have {20} {\exists t \, (n_0 \cdot n_0 - 1 = 8 \cdot t)} \Ee{1,2-19}
  \close
  \have {21} {\exists k \, (n_0 = 2 \cdot k + 1) \to \exists t \, (n_0 \cdot n_0 - 1 = 8 \cdot t)} \ii{1-20}
  \close
  \have {22} {\forall n \, (\exists k \, (n = 2 \cdot k + 1) \to \exists t \, (n \cdot n - 1 = 8 \cdot t))} \Ai{1-21}
\end{nd}$
\end{center}
```

The arithmetic lines: \( (2k_0 + 1)^2 - 1 = 4k_0^2 + 4k_0 = 4k_0(k_0 + 1) \) (line 3); \( 2j_0(2j_0 + 1) \) for \( k_0 = 2j_0 \) (line 7); \( (2j_1 + 1)(2j_1 + 2) = 2(2j_1 + 1)(j_1 + 1) \) (line 12); \( 4 \cdot 2i_0 = 8i_0 \) (line 17). The boxes close by \( \rulename{\exists E} \) (lines 9, 14, 19, 20), \( \rulename{\vee E} \) (line 15), \( \rulename{{\to}I} \) (line 21) and \( \rulename{\forall I} \) (line 22). The fact (E1) enters at line 4, instantiated at \( k_0 \); in the prose it is the words "if \( k = 2j \) … if \( k = 2j + 1 \)", whose reason for exhausting the cases is left to the reader. By @def-silent-steps that reason should be written ("since every integer is even or odd"), so the given proof is slightly short of level 3 at exactly this point. The two case names may both be \( j \) in the prose, because their boxes are disjoint; here they are \( j_0 \) and \( j_1 \) to keep the lines apart.
:::

### C. Going deeper

::: {#exr-levels-of-abbreviation-c1}
[C1: Arbitrarily close numbers, at two levels]

Consider @prp-arbitrarily-close-equal: for real numbers \( a \) and \( b \), if \( \abs{a - b} < \varepsilon \) for every \( \varepsilon > 0 \), then \( a = b \).

::: {.enumerate options="label=(\alph*)"}
1. Write its proof at level 1, as a skeleton in which school facts about \( \abs{\cdot} \) and \( < \) are lines justified "arith".
2. Write it at level 3.
3. Which lines of your skeleton are silent at level 3? Which instance of \( \rulename{\forall E} \) must the level-3 text name, and why?
:::
:::

::: {.solution}
*(a)* The statement is an implication, so the outer box is \( \rulename{{\to}I} \); the goal \( a = b \) is atomic, and the proof in Section 4.9 opens an \( \rulename{RAA} \) box on \( a \ne b \).

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {\forall \varepsilon > 0 \; (\abs{a - b} < \varepsilon)}
  \open
  \hypo {2} {\neg(a = b)}
  \have {3} {\abs{a - b} > 0} \by{arith}{2}
  \have {4} {\abs{a - b} < \abs{a - b}} \Ae{1,3}
  \have {5} {\neg(\abs{a - b} < \abs{a - b})} \by{arith}{}
  \have {6} {\bot} \ne{4,5}
  \close
  \have {7} {a = b} \raa{2-6}
  \close
  \have {8} {\forall \varepsilon > 0 \; (\abs{a - b} < \varepsilon) \to a = b} \ii{1-7}
\end{nd}$
\end{center}
```

Line 4 is the bounded \( \rulename{\forall E} \) at the term \( \abs{a - b} \), whose bound \( \abs{a - b} > 0 \) is line 3. Line 5 is the school fact that no real number is less than itself.

*(b)*

> Suppose \( \abs{a - b} < \varepsilon \) for every \( \varepsilon > 0 \), and suppose, for a contradiction, that \( a \ne b \). Then \( \abs{a - b} > 0 \), so the hypothesis applies with \( \varepsilon = \abs{a - b} \) and gives \( \abs{a - b} < \abs{a - b} \); but no real number is less than itself. Hence \( a = b \).

*(c)* Only line 8, the closing line of \( \rulename{{\to}I} \), is silent: "hence if … then \( a = b \)" is not written. Line 5 is not silent: it is one member of the clashing pair of the \( \rulename{\neg E} \) on line 6, and level 3 names it ("no real number is less than itself"). The instance of line 4 must be named, \( \varepsilon = \abs{a - b} \), because it is not the obvious term: no name in sight is the obvious candidate for \( \varepsilon \), and the whole proof turns on choosing this one. Saying only "by the hypothesis" would leave the reader to find the instance, and that instance is the idea of the proof. The \( \rulename{RAA} \) opening, "suppose, for a contradiction, that \( a \ne b \)", and its conclusion, "hence \( a = b \)", are also never silent.

**Marking scheme.** (10 points)
- 2: (a) the \( \rulename{{\to}I} \) box on the hypothesis, and inside it a box opened on \( a \ne b \).
- 2: (a) the box closed by \( \rulename{RAA} \) (\( \rulename{\neg I} \) alone would give only \( \neg\neg(a = b) \)), with \( \bot \) as its last line.
- 2: (a) the \( \rulename{\forall E} \) at \( \abs{a - b} \), citing a line \( \abs{a - b} > 0 \).
- 2: (b) a level-3 text with the opening of the contradiction, the instance, the clash and "hence \( a = b \)", and no tags.
- 2: (c) the silent line identified, and the instance \( \varepsilon = \abs{a - b} \) said to be named because it is not the obvious term.
- Other routes: a \( \rulename{\neg I} \) box on \( a \ne b \) followed by \( \rulename{\neg\neg E} \), or a split on \( \abs{a - b} > 0 \) or \( \abs{a - b} = 0 \) (arith) whose first case reaches \( \bot \) by the same \( \rulename{\forall E} \) and clash and then \( a = b \) by \( \rulename{\bot E} \), while the second gives \( a = b \) by arith, earns the 4 points of the first two lines, provided the \( \rulename{\neg\neg E} \) line is written explicitly, or the disjunction of the split is justified (from \( \abs{a - b} \ge 0 \), or by trichotomy). In the split, the case assumption \( \abs{a - b} > 0 \) is the line the \( \rulename{\forall E} \) cites for the third line, and for (b) and (c) the opening of the \( \rulename{\neg I} \) box or of the split stands in for the opening of the contradiction.
Fatal errors (0 for the step): the box closed by \( \neg I \) with the conclusion \( a = b \); the hypothesis applied at an \( \varepsilon \) not known to be positive.
:::

::: {#exr-levels-of-abbreviation-c2}
[C2: Exit check: levels]

Let \( (a_n) \) be a sequence of real numbers with \( a_n \to L \), and let \( c \ne 0 \) be a real number. Here is a level-0 derivation that \( c \, a_n \to cL \), with the definition of a limit as in @exm-translate-limit (a), the hypothesis \( c \ne 0 \) as premise 2, and two lines of school arithmetic justified "arith".

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall \varepsilon > 0 \; \exists N \in \nN \; \forall n \in \nN \; (n \ge N \to \abs{a_n - L} < \varepsilon)}
  \hypo {2} {\neg(c = 0)}
  \open[\varepsilon_0]
  \hypo {3} {\varepsilon_0 > 0}
  \have {4} {\varepsilon_0 / \abs{c} > 0} \by{arith}{2,3}
  \have {5} {\exists N \in \nN \; \forall n \in \nN \; (n \ge N \to \abs{a_n - L} < \varepsilon_0 / \abs{c})} \Ae{1,4}
  \open[N_0]
  \hypo {6} {N_0 \in \nN}
  \hypo {7} {\forall n \in \nN \; (n \ge N_0 \to \abs{a_n - L} < \varepsilon_0 / \abs{c})}
  \open[n_0]
  \hypo {8} {n_0 \in \nN}
  \have {9} {n_0 \ge N_0 \to \abs{a_{n_0} - L} < \varepsilon_0 / \abs{c}} \Ae{7,8}
  \open
  \hypo {10} {n_0 \ge N_0}
  \have {11} {\abs{a_{n_0} - L} < \varepsilon_0 / \abs{c}} \ie{9,10}
  \have {12} {\abs{c \cdot a_{n_0} - c \cdot L} < \varepsilon_0} \by{arith}{2,11}
  \close
  \have {13} {n_0 \ge N_0 \to \abs{c \cdot a_{n_0} - c \cdot L} < \varepsilon_0} \ii{10-12}
  \close
  \have {14} {\forall n \in \nN \; (n \ge N_0 \to \abs{c \cdot a_n - c \cdot L} < \varepsilon_0)} \Ai{8-13}
  \have {15} {\exists N \in \nN \; \forall n \in \nN \; (n \ge N \to \abs{c \cdot a_n - c \cdot L} < \varepsilon_0)} \Ei{6,14}
  \close
  \have {16} {\exists N \in \nN \; \forall n \in \nN \; (n \ge N \to \abs{c \cdot a_n - c \cdot L} < \varepsilon_0)} \Ee{5,6-15}
  \close
  \have {17} {\forall \varepsilon > 0 \; \exists N \in \nN \; \forall n \in \nN \; (n \ge N \to \abs{c \cdot a_n - c \cdot L} < \varepsilon)} \Ai{3-16}
\end{nd}$
\end{center}
```

Write the proof at level 2 and at level 3. Then say in one sentence how the case \( c = 0 \) goes.
:::

::: {.solution}
**Level 2.**

> Let \( \varepsilon > 0 \) [\( \rulename{\forall I} \)]. Since \( c \ne 0 \), \( \abs{c} > 0 \), so \( \varepsilon / \abs{c} > 0 \) [arith]. Applying the definition of \( a_n \to L \) with \( \varepsilon / \abs{c} \) in place of \( \varepsilon \) [\( \rulename{\forall E} \)], choose \( N \in \nN \), depending on \( \varepsilon \) (and on the fixed number \( c \)), such that \( \abs{a_n - L} < \varepsilon / \abs{c} \) for every \( n \ge N \) [\( \rulename{\exists E} \), \( N \) fresh]. Let \( n \in \nN \) [\( \rulename{\forall I} \)] with \( n \ge N \) [assumption for \( \rulename{{\to}I} \)]. Then \( \abs{a_n - L} < \varepsilon / \abs{c} \) [\( \rulename{\forall E} \), \( \rulename{{\to}E} \)], so
\[
\abs{c\, a_n - cL} = \abs{c} \, \abs{a_n - L} < \abs{c} \cdot \frac{\varepsilon}{\abs{c}} = \varepsilon
\]
[arith]. So this \( N \) works for \( \varepsilon \) [\( \rulename{{\to}I} \), \( \rulename{\forall I} \), \( \rulename{\exists I} \) with witness \( N \); then \( \rulename{\exists E} \) closes]. Since \( \varepsilon > 0 \) was arbitrary, \( c\, a_n \to cL \) [\( \rulename{\forall I} \)].

**Level 3.**

> Let \( \varepsilon > 0 \). Since \( c \ne 0 \), we have \( \varepsilon / \abs{c} > 0 \), so by the definition of \( a_n \to L \), applied with \( \varepsilon / \abs{c} \), there is \( N \in \nN \) (depending on \( \varepsilon \) and \( c \)) such that \( \abs{a_n - L} < \varepsilon / \abs{c} \) for every \( n \ge N \). For every \( n \ge N \),
> \[
> \abs{c\, a_n - cL} = \abs{c} \, \abs{a_n - L} < \abs{c} \cdot \frac{\varepsilon}{\abs{c}} = \varepsilon .
> \]
> So this \( N \) works for \( \varepsilon \), and \( c\, a_n \to cL \).

**The case \( c = 0 \).** Then \( c\, a_n = 0 = cL \) for every \( n \), so \( \abs{c\, a_n - cL} = 0 < \varepsilon \) for every \( \varepsilon > 0 \) and every \( n \), and any \( N \) works, for instance \( N = 0 \); the hypothesis \( a_n \to L \) is not needed.

At level 3, the silent steps are those @def-silent-steps allows: the \( \rulename{\forall E} \) and \( \rulename{{\to}E} \) of lines 9 and 11 at the obvious \( n \) (the implication of line 11 is line 9, an instance of the property of the chosen \( N_0 \), not of a hypothesis or a result), carried by "for every \( n \ge N \)", and the closing lines 13, 14, 16 and 17. The \( \rulename{\forall E} \) of line 5 is **not** silent, because its instance \( \varepsilon / \abs{c} \) is not the obvious one; it is named ("applied with \( \varepsilon / \abs{c} \)"). The witness of line 15 is named ("this \( N \)"), and its dependence is stated.

**Marking scheme.** (10 points)
- 4: every never-silent step is present at level 3, one point each: \( \varepsilon > 0 \) fixed first (\( \rulename{\forall I} \)); the hypothesis applied at \( \varepsilon / \abs{c} \), with its positivity justified, and \( N \) chosen from it (\( \rulename{\exists E} \)); the witness \( N \) produced with its dependence on \( \varepsilon \) stated (\( \rulename{\exists I} \)); \( n \ge N \) taken arbitrary (\( \rulename{\forall I} \)).
- 3: the level-2 tags are correct: \( \rulename{\forall I} \) for \( \varepsilon \) and for \( n \), \( \rulename{\forall E} \) at \( \varepsilon / \abs{c} \), \( \rulename{\exists E} \) for \( N \), \( \rulename{{\to}I} \) for \( n \ge N \), \( \rulename{\exists I} \) for the witness. Deduct one point per wrong or missing tag, down to 0.
- 2: no step silent at level 3 beyond those @def-silent-steps allows, steps already scored in the first line not counted again; in particular the estimate \( \abs{c\, a_n - cL} = \abs{c} \, \abs{a_n - L} < \abs{c} \cdot \varepsilon / \abs{c} = \varepsilon \) is written out for an arbitrary \( n \ge N \).
- 1: the case \( c = 0 \) handled, or excluded explicitly with a reason.
A level 3 that writes "for every \( n \ge N \)" as the single phrase for \( \rulename{\forall I} \) together with \( \rulename{{\to}I} \) earns the \( \rulename{\forall I} \) point, as in the solution.
Fatal errors (0 for the step): \( N \) chosen before \( \varepsilon \) is fixed; dividing by \( \abs{c} \) in the case \( c = 0 \).
:::

<!-- dependency ledger
def-levels-of-proof (claim): f(x) = 3x + 1 is uniformly continuous on R with delta = eps/3, since |(3x+1)-(3y+1)| = 3|x-y| | inline (school algebra)
def-levels-of-proof (claim): the derivation after thm-sqrt2-irrational in Section 2.2 fixes r, p, q and leaves out the two quantifier steps (choosing p, q and m), as the paragraph after it says | thm-sqrt2-irrational (Section 2.2, cited), read on the page
def-levels-of-proof (claim): from ch11 (Part I) on proofs are written at level 3 in plain prose, rule tags only where the rule is itself the point (e.g. an R item looking back at Part 0, as ch11 exr-nested-intervals-r3); Part 0 (ch01-ch08) may use level 2 | STYLE section 10 (book convention); prose pointer to ch11, nothing rests on it
def-levels-of-proof (claim): Section 5.5 turns level 1 into a procedure; Section 5.4 reconstructs it when reading | this chapter (sections 04, 05; prose pointers, nothing rests on them)
def-silent-steps (claim): the two lists are the last column of the dictionary of Sections 5.1 and 5.2, with the requirements in the text under its tables (exhaustion of a case split, the 5.7 flag, chains of inequalities) | ch05 sections 01, 02 (dictionary and the prose under its tables; drafted in parallel from the same frozen blueprint); the closing line of exists-E and the to-E on a line already in the proof are added here explicitly; the exchange of the members of a disjunction or conjunction is the Disjunction table's last row (exm-disjunction-first-derivations, prp-and-commutes, cited)
def-silent-steps (example): x in (0, 1) unwinds to 0 < x and x < 1 | definition of an open interval (school fact)
exm-sqrt2-four-levels (example): premise 1 follows from (L): r = p/q with q != 0 gives p = r q; q = 0 forces p = 0, both even | (L) of Section 2.2 (stated there and taken as known; its proof is promised there to ch07); school algebra
exm-sqrt2-four-levels (example): premise 2 is thm-square-even-implies-even written as a formula | thm-square-even-implies-even (cited)
exm-sqrt2-four-levels (example): arith lines 11, 12, 15: p^2 = 2 q^2 from p = r q, r^2 = 2; 2 times an integer is even; p = 2m and p^2 = 2q^2 give q^2 = 2 m^2 | school algebra; definition of even (Ch 1 section 1.1, Ch 2 section 2.1); checked by verify/ch05/exm-sqrt2-four-levels.py
exm-sqrt2-four-levels (example): side conditions at lines 21, 22, 24 | def-rules-existential, def-rules-universal, prp-bounded-quantifier-rules (Ch 4; checked on the page)
exm-sqrt2-four-levels (claim): level 0 has 24 lines, level 1 has 15; the correspondence of lines between levels | read off the two derivations; checked by verify/ch05/exm-sqrt2-four-levels.py
exm-uniform-four-levels (example): level 0 is the derivation of exm-uniform-implies-continuous with its line numbers; dependence read off the boxes | exm-uniform-implies-continuous and Section 4.10's reading of dependence (cited)
exm-uniform-four-levels (example): renaming of the bound variables of UC to u, v in prose | renaming of bound variables in prose, Section 4.2's convention, as in Section 4.10; not used in any derivation
exm-uniform-four-levels (claim): [subsection "Expand to check"] the line forall-I over x_0 inside the box of delta_0 breaks the side condition; it is the first blocked line of exm-converse-fails; x^2 on R refutes the conclusion | def-rules-universal, exm-converse-fails, exm-square-not-uniform (cited); Section 5.6 catalogue (prose pointer, nothing rests on it)
exr-levels-of-abbreviation-a1 (solution): (e) a contradiction alone does not say which open assumption it refutes | def-rules-negation (Ch 2); def-silent-steps
exr-levels-of-abbreviation-b1 (solution): 0 <= y for every y in N; y <= y | order on N (school fact); checked by verify/ch05/exr-levels-of-abbreviation-b1.py
exr-levels-of-abbreviation-b2 (solution): (2k + 1)^2 - 1 = 4k(k + 1); k(k + 1) = 2 j(2j + 1) or 2 (2j + 1)(j + 1); 4 (2i) = 8i | school algebra; checked by verify/ch05/exr-levels-of-abbreviation-b2.py
exr-levels-of-abbreviation-b2 (solution): (E1) every integer is even or odd | (E1) of Section 2.1 (school fact, stated there)
exr-levels-of-abbreviation-b2 (solution): the claim "it suffices" is a cut | lem-weakening-cut (Ch 3), named in Section 5.2's dictionary
exr-levels-of-abbreviation-c1 (solution): a != b gives |a - b| > 0; no real number is less than itself | school facts about | . | and <, as in prp-arbitrarily-close-equal's proof (Section 4.9)
exr-levels-of-abbreviation-c1 (solution): [marking scheme, other routes] |a - b| > 0 or |a - b| = 0 from |a - b| >= 0 or trichotomy, not flagged | trichotomy of the order (school fact); Section 5.1's rule that such a split is never flagged
exr-levels-of-abbreviation-c2 (solution): eps/|c| > 0 for c != 0, eps > 0; |c a - c L| = |c| |a - L| < eps | school algebra; |uv| = |u||v| exm-abs-product-cases (Ch 1); checked by verify/ch05/exr-levels-of-abbreviation-c2.py
exr-levels-of-abbreviation-c2 (solution): case c = 0: c a_n = 0 = c L, any N works | school algebra
-->
