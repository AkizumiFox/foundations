# Derived Rules: Proved Sequents as New Rules

Section 2.1 closed an impossible case by hand, and Section 2.2 proved negations by hand, one box at a time. By now the same few patterns keep coming back: the impossible case of @exm-impossible-case, and a box that turns a known implication round. Mathematicians give such patterns names ("by contraposition", "since \( P \) fails, \( Q \)") and use them in one breath. This section proves three of them once, from the rules we have, and then allows each to be used as a single line. The one new thing is that permission: a **derived rule**.

## A box that keeps coming back

Here are two short arguments from different corners of mathematics.

> Let \( n \) be an integer whose square is not even. Suppose \( n \) is even. Then \( n^2 \) is even, which contradicts the hypothesis. Hence \( n \) is not even.

> Let \( x \) be a real number with \( x^2 < 1 \). Suppose \( x \ge 1 \). Then \( x^2 \ge x \ge 1 \), which contradicts \( x^2 < 1 \). Hence \( x < 1 \).

The subjects differ; the steps are the same. Each has a known implication ("if \( n \) is even, then \( n^2 \) is even"; "if \( x \ge 1 \), then \( x^2 \ge 1 \)"), and a fact saying that the implication's conclusion fails. Each then opens a box on the implication's hypothesis, fires the implication inside it by \( \rulename{{\to}E} \), meets the clash with \( \rulename{\neg E} \), and closes the box by \( \rulename{\neg I} \) (@def-rules-negation). (For reals, \( x^2 < 1 \) and \( x < 1 \) are the exact negations of \( x^2 \ge 1 \) and \( x \ge 1 \).) The same four lines appear whenever an implication is used backwards, from the failure of its conclusion to the failure of its hypothesis.

A mathematician does not write these four lines. She writes "since \( n^2 \) is not even, \( n \) is not even", or "by contraposition", and moves on: the lines are the same every time. But a derivation is checked line by line against the rules, and "by contraposition" is not one of the rules. What licenses the short form? First we derive the pattern once, as a sequent, with the rules we have. Then we say exactly when a sequent already derived may be used as a single line.

## Modus tollens, from the rules we have

The pattern of the two arguments is: from an implication and the negation of its conclusion, infer the negation of its hypothesis.

::: {#prp-modus-tollens}
[Modus Tollens]

\( P \to Q, \; \neg Q \vdash \neg P \).
:::

::: {.idea}
Read the skeleton off the goal. The goal \( \neg P \) is a negation, and Section 2.2's move for a negated goal is a box opened on what is negated, here \( P \), with goal \( \bot \). Inside the box, look for a clash (Section 2.1's move for the goal \( \bot \)). The premise \( \neg Q \) will clash with \( Q \), so \( Q \) is the subgoal, and the premise \( P \to Q \) gives it from the box's own assumption. In the pictures, the box on \( P \) stands with its goal \( \bot \); then \( \rulename{\neg E} \) writes \( \bot \) from the subgoal \( Q \), still unjustified.

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {\neg Q}
  \open
  \hypo {3} {P}
  \have[\ ][0] {} {\vdots}
  \have[][5] {5} {\bot}
  \close
  \have {6} {\neg P} \ni{3-5}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {\neg Q}
  \open
  \hypo {3} {P}
  \have[\ ][0] {} {\vdots}
  \have[][4] {4} {Q}
  \have {5} {\bot} \ne{4,2}
  \close
  \have {6} {\neg P} \ni{3-5}
\end{nd}$
\end{center}
```
:::

::: {.proof}
The following is a derivation with premises \( P \to Q \) and \( \neg Q \), and last line \( \neg P \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {\neg Q}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {\bot} \ne{4,2}
  \close
  \have {6} {\neg P} \ni{3-5}
\end{nd}$
\end{center}
```

Line 5 cites the premise on line 2, which lies in no box and so is available everywhere below it. The box \( \lines{3}{5} \) ends in \( \bot \) as a line of its own, so \( \rulename{\neg I} \) closes it on line 6. This proves the proposition.
:::

The name is Latin for "the mode that takes away": denying the conclusion takes away the hypothesis. Its partner, from \( P \to Q \) and \( P \) to \( Q \), is \( \rulename{{\to}E} \), traditionally *modus ponens*, "the mode that puts" (@def-rule-implication-elimination). The derivation uses \( \rulename{{\to}E} \), \( \rulename{\neg E} \), and \( \rulename{\neg I} \), and nothing else.

A second form of the same fact packs the two premises into one implication. It is the form in which mathematicians state it: an implication **implies** its contrapositive.

::: {#prp-contrapositive}
[Contrapositive]

\( P \to Q \vdash \neg Q \to \neg P \).
:::

::: {.idea}
The goal is an implication, so Chapter 1's first goal-directed move applies: open a box with its hypothesis \( \neg Q \), and the new goal is \( \neg P \). That goal is a negation, so open a second box, on \( P \), inside the first. Inside both boxes we are exactly where the proof of @prp-modus-tollens was: \( P \) and \( P \to Q \) give \( Q \), which clashes with \( \neg Q \).
:::

::: {.proof}
The following is a derivation with premise \( P \to Q \) and last line \( \neg Q \to \neg P \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \open
  \hypo {2} {\neg Q}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {\bot} \ne{4,2}
  \close
  \have {6} {\neg P} \ni{3-5}
  \close
  \have {7} {\neg Q \to \neg P} \ii{2-6}
\end{nd}$
\end{center}
```

Line 5 may cite line 2, because the only box containing line 2, the box \( \lines{2}{6} \), also contains line 5 (the scope rule of @def-derivation). The inner box closes on line 6, a line of the outer box itself, and line 7 closes the outer box. This proves the proposition.
:::

The statement \( \neg Q \to \neg P \) is called the **contrapositive** of \( P \to Q \). Like modus tollens, its derivation uses only the rules so far: \( \rulename{{\to}I} \), \( \rulename{{\to}E} \), \( \rulename{\neg I} \), and \( \rulename{\neg E} \). The passage back, from \( \neg Q \to \neg P \) to \( P \to Q \), is a different matter (Common errors, below).

Now compare the two derivations. Lines 3–6 of the derivation of @prp-modus-tollens are, line for line and citation for citation, lines 3–6 of the derivation of @prp-contrapositive: \( P \), then \( Q \) by \( \rulename{{\to}E}\ 1, 3 \), then \( \bot \) by \( \rulename{\neg E}\ 4, 2 \), then \( \neg P \) by \( \rulename{\neg I}\ \lines{3}{5} \). And they are the four lines of the two arguments that opened this section. Writing them out every time buries the argument in bookkeeping.

## What a derived rule is

*A sequent that has been derived may be used as a rule.*

This is what a mathematician does when she writes "by Lemma 3": the lemma was proved once, and each use of it is a single step. For derivations we must say exactly what that step may do.

::: {#def-derived-rule}
[Derived Rule]

Let \( \varphi_1, \dots, \varphi_n \vdash \psi \) be a sequent, written with statement letters, that has **already been derived** earlier in the book. In a later derivation, replace each letter in \( \varphi_1, \dots, \varphi_n, \psi \) by a statement, the **same** statement for every occurrence of the same letter. If lines \( i_1, \dots, i_n \), all **available** at line \( k \), hold the resulting instances of \( \varphi_1, \dots, \varphi_n \), we may write the resulting instance of \( \psi \) on line \( k \). The justification names the result and cites \( i_1, \dots, i_n \). A sequent used in this way is a **derived rule**. For example, @prp-modus-tollens becomes the rule \( \rulename{MT} \):

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {i} {\varphi \to \psi}
  \have {j} {\neg \psi}
  \have {k} {\neg \varphi} \mt{i,j}
\end{nd}$
\end{center}
```
:::

In words: a proved sequent is a new rule. Its premises become the cited lines, its conclusion the line written, and its letters the metavariables of a schema (@def-rule-schema). Read the definition clause by clause.

1. **"Already derived."** The sequent must have been derived **before** the line that uses it: earlier in the book, and never inside its own derivation. A derivation that used a sequent to derive that same sequent would prove nothing.
2. **"Replace each letter … the same statement for every occurrence."** The letters of a derived sequent stood for arbitrary statements all along (@def-derivable), so they may be replaced by any statements, provided the replacement is **uniform**. From \( (A \wedge B) \to C \) and \( \neg C \), the rule \( \rulename{MT} \) gives \( \neg(A \wedge B) \), with \( \varphi \) replaced by \( A \wedge B \) and \( \psi \) by \( C \).
3. **"Available at line \( k \)."** The scope rule of @def-derivation still governs every citation. A derived rule may not reach into a closed box, just as a primitive rule may not.
4. **"The resulting instance of \( \psi \)."** The rule writes the conclusion, with the same replacement, and nothing else. The derived rule does not open or close any box of the derivation that uses it.

We give the derived rules of this section short tags: \( \rulename{MT} \) for @prp-modus-tollens, \( \rulename{CP} \) for @prp-contrapositive, and, once it is proved below, \( \rulename{DS} \) for @prp-disjunctive-syllogism. Every other derived sequent is a derived rule too, cited by its name: the five lines written out in @exm-vacuous-square, for instance, are now one line citing @prp-vacuous-implication.

**Left: with the derived rule. Right: written out.**

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {\neg Q}
  \have {3} {\neg P} \mt{1,2}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {\neg Q}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {\bot} \ne{4,2}
  \close
  \have {6} {\neg P} \ni{3-5}
\end{nd}$
\end{center}
```

*Line 3 on the left stands for lines 3–6 on the right: the same premises, the same last line.*

A derived rule is shorthand for lines we could always write out, so it lets us prove nothing that the primitive rules could not.

::: {.check}
In the figure, which lines does line 3 on the left cite, and which lines on the right use those same two premises?
:::

::: {.solution}
Lines 1 and 2. On the right, line 4 cites line 1 and line 5 cites line 2.
:::

::: {.second-reading title="Why a derived rule adds no power"}
**Convenience, not power.** A derived-rule line abbreviates a stretch of derivation that we could write out in full. To expand it, repeat each cited line by (D3) of @def-derivation, then copy the derivation of the sequent below the repetitions, with its letters replaced, its premises replaced by the repetitions, and its line numbers shifted. Every citation inside the copy points inside the copy or to a repetition, all in the current box, so every citation is available. The copy's boxes close before its last line, which is the instance of \( \psi \). If the copy itself uses derived rules, expand those lines in the same way; this stops, because each derivation cites only results proved before it. So whatever can be derived with derived rules can be derived with the primitive rules alone.

The degenerate case is a sequent with nothing done to its premise, \( P \vdash P \), whose derivation is the single premise line (part (a) of @exm-derivations): as a derived rule it copies an available line, which repetition already does. The first use with content is modus tollens proved a second time, with \( \rulename{CP} \) as a rule. The premise \( P \to Q \) invites \( \rulename{CP} \), and its conclusion \( \neg Q \to \neg P \) is an implication whose hypothesis is the other premise.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {\neg Q}
  \have {3} {\neg Q \to \neg P} \ctp{1}
  \have {4} {\neg P} \ie{3,2}
\end{nd}$
\end{center}
```

Line 3 is the instance of @prp-contrapositive with \( P \) and \( Q \) replaced by themselves; line 4 is modus ponens on it. Written out in full, line 3 would become a repetition of line 1 followed by lines 2–7 of the derivation of @prp-contrapositive. This is honest because @prp-contrapositive was derived from the primitive rules, not from @prp-modus-tollens: the chain of derived rules ends in primitive rules, without a loop.
:::

::: {.warning}
A derived rule must match its sequent exactly, under one uniform replacement of letters. From \( P \to Q \) and \( \neg R \), \( \rulename{MT} \) gives nothing: no single statement in place of \( \psi \) turns the pair into \( \varphi \to \psi \) and \( \neg\psi \). Equally, from \( P \to \neg Q \) and \( Q \), \( \rulename{MT} \) gives nothing yet: it needs the negation of the conclusion, \( \neg\neg Q \), and \( Q \) is not that line. (Here \( \rulename{\neg I} \) would give \( \neg\neg Q \) first, as in @exm-double-negation-introduction, and then \( \rulename{MT} \) applies.) Likewise \( \rulename{DS} \), as stated below, refutes the **left** disjunct; applied blindly to \( P \vee Q \) and \( \neg Q \), it does not match.
:::

In the Givens/Goal table, a derived rule adds its conclusion to the Givens in one row, as an elimination rule does.

## Pasting whole derivations: weakening and cut

The figure expands one derived-rule line inside a derivation. Outside every box there is a cleaner statement, about whole derivations: two derivations can be joined end to end, and premises that are never used do no harm.

::: {#lem-weakening-cut}
[Weakening and Cut]

Let \( \Gamma \) and \( \Delta \) be lists of statements, and let \( \varphi \), \( \psi \), \( \alpha_1, \dots, \alpha_m \) (\( m \ge 1 \)), and \( \beta \) be statements.

::: {.enumerate options="label=(\alph*)"}
1. **Weakening.** If \( \Gamma \vdash \psi \) and every member of \( \Gamma \) is a member of \( \Delta \), then \( \Delta \vdash \psi \). In particular, \( \Gamma \vdash \psi \) implies \( \Gamma, \varphi \vdash \psi \).
2. **Cut.** If \( \Gamma \vdash \varphi \) and \( \Gamma, \varphi \vdash \psi \), then \( \Gamma \vdash \psi \).
3. **Chaining.** If \( \Gamma \vdash \alpha_i \) for **every** \( i = 1, \dots, m \), and \( \alpha_1, \dots, \alpha_m \vdash \beta \), then \( \Gamma \vdash \beta \).
:::
:::

*In words: (a) extra premises never hurt; (b) a statement that has been derived may be used as a premise; (c) a sequent already proved can be applied to statements already derived. Part (c) is @def-derived-rule for whole derivations, outside every box; inside a box, the expansion of the fold "Why a derived rule adds no power" does the same job.*

Cut is the reason a derived rule is legitimate: a derivation that cites a proved sequent as one line, outside every box, becomes a derivation in the primitive rules when the sequent's own derivation is pasted in front of it.

::: {.second-reading title="The proof: pasting derivations"}
::: {.idea}
Part (a) is read off @def-derivable, which asks only that the premises of the derivation **belong to** the list. For (b) and (c), write the derivations one after another and let the last one cite, instead of its premise \( \alpha_i \), the last line of the derivation of \( \alpha_i \). The only thing to check is the scope rule of @def-derivation: the last line of a derivation lies in no box, so it stays available to everything written after it.
:::

::: {.proof}
*(a)* A derivation witnessing \( \Gamma \vdash \psi \) has premises that belong to \( \Gamma \), hence to \( \Delta \), and its last line is \( \psi \). By @def-derivable it witnesses \( \Delta \vdash \psi \). The second sentence is the case where \( \Delta \) is \( \Gamma, \varphi \).

For (b) and (c) we prove one statement that contains both:

\( (\ast) \) If \( \Gamma \vdash \alpha_i \) for every \( i = 1, \dots, m \), and \( \Gamma, \alpha_1, \dots, \alpha_m \vdash \beta \), then \( \Gamma \vdash \beta \).

Part (b) is \( (\ast) \) with \( m = 1 \), \( \alpha_1 = \varphi \) and \( \beta = \psi \). Part (c) follows from \( (\ast) \), since \( \alpha_1, \dots, \alpha_m \vdash \beta \) gives \( \Gamma, \alpha_1, \dots, \alpha_m \vdash \beta \) by (a).

To prove \( (\ast) \), let \( D_i \) be a derivation of \( \alpha_i \) with premises in \( \Gamma \), for each \( i \), and let \( E \) be a derivation of \( \beta \) with premises in \( \Gamma, \alpha_1, \dots, \alpha_m \). If the last line of \( E \) is one of its premises, then \( \beta \) is a member of \( \Gamma \), and the one-line derivation whose only line is the premise \( \beta \) shows \( \Gamma \vdash \beta \); or \( \beta \) is some \( \alpha_i \), and \( D_i \) shows \( \Gamma \vdash \beta \). Otherwise, build a list of lines \( F \) as follows.

1. First, as premises, every premise of \( D_1, \dots, D_m \), and every premise of \( E \) that is a member of \( \Gamma \).
2. Then the lines of \( D_1 \) that are not premises, then those of \( D_2 \), and so on up to \( D_m \), each with its boxes.
3. Then the lines of \( E \) that are not premises, with its boxes.

Renumber the lines, and change each citation as follows. A citation of a premise that is in \( \Gamma \) now cites the premise line of step 1 carrying that statement. A citation in \( E \) of a premise \( \alpha_i \) that is not in \( \Gamma \) now cites the last line of \( D_i \); that line is not a premise of \( D_i \), because the premises of \( D_i \) are in \( \Gamma \) and \( \alpha_i \) is not, so it was copied in step 2. Every other citation follows its line to its new number.

We check that \( F \) is a derivation (@def-derivation). The premises come first and lie in no box. The boxes are those of the \( D_i \) and of \( E \), moved as blocks, so two boxes are still disjoint or nested, each still begins with its assumption, and each line lies in exactly the boxes it lay in before. Hence a line and a box that were available at a citing line are still available there, since the boxes containing each are unchanged. A premise line of step 1 lies in no box and comes first, so it is available at every later line. The last line of \( D_i \) lies in no box (it was the last line of a derivation) and comes before every line of \( E \), so it is available at every line of \( E \). Each line carries the same statement and the same justification as before, citing lines with the same statements, so it is an instance of the same rule. Finally, the last line of \( F \) is the last line of \( E \), namely \( \beta \), and it lies in no box. The premises of \( F \) are all in \( \Gamma \). Therefore \( \Gamma \vdash \beta \), which proves \( (\ast) \).
:::
:::

::: {.check}
Given @prp-modus-tollens, which part of @lem-weakening-cut gives \( P \to Q, \ \neg Q, \ R \vdash \neg P \) at once? Given also @prp-vacuous-implication, which part gives \( P \to Q, \ \neg Q \vdash P \to R \)?
:::

::: {.solution}
Part (a), weakening, with \( R \) as the extra premise. Part (c), chaining, with \( m = 1 \), \( \alpha_1 = \neg P \) and \( \beta = P \to R \): @prp-modus-tollens gives \( P \to Q, \ \neg Q \vdash \neg P \), and @prp-vacuous-implication with \( R \) in place of \( Q \) gives \( \neg P \vdash P \to R \). (Part (a) and then part (b) do the same.)
:::

## Disjunctive syllogism: the impossible case, filed

The second pattern is the impossible case of Section 2.1. Every integer is even or odd; this one is not odd; so it is even. A disjunction, one side refuted, the other side left.

::: {#prp-disjunctive-syllogism}
[Disjunctive Syllogism]

\( P \vee Q, \; \neg P \vdash Q \).
:::

::: {.idea}
This is @exm-impossible-case with a simpler clash. There, the case \( P \) produced \( R \) by \( \rulename{{\to}E} \), which clashed with \( \neg R \). Here the case \( P \) clashes with the premise \( \neg P \) at once. So: split the premise \( P \vee Q \) by \( \rulename{\vee E} \), both boxes ending in the current goal \( Q \). The \( Q \) box is its own assumption. The \( P \) box cannot reach \( Q \) honestly, so it reaches a clash and closes by \( \rulename{\bot E} \): an impossible case closes itself.
:::

::: {.proof}
The following is a derivation with premises \( P \vee Q \) and \( \neg P \), and last line \( Q \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \hypo {2} {\neg P}
  \open
  \hypo {3} {P}
  \have {4} {\bot} \ne{3,2}
  \have {5} {Q} \be{4}
  \close
  \open
  \hypo {6} {Q}
  \close
  \have {7} {Q} \oe{1,3-5,6-6}
\end{nd}$
\end{center}
```

The two boxes \( \lines{3}{5} \) and \( \lines{6}{6} \) are separate. The second consists of its assumption alone, which is already the statement \( Q \) that \( \rulename{\vee E} \) needs. This proves the proposition.
:::

Set the derivation beside that of @exm-impossible-case. Both split \( P \vee Q \) into the same two boxes, and in both the \( Q \) box is one line long. Inside the \( P \) box, two lines reached \( \bot \) there (lines 5–6) and one line does here (line 4); then \( \rulename{\bot E} \) closes the box in the same way. From now on this whole stretch is one line, tagged \( \rulename{DS} \).

The rule as stated refutes the **left** disjunct. To refute the right one, first put the disjunction in the other order; that, too, is now one line, since @exm-disjunction-first-derivations derived \( P \vee Q \vdash Q \vee P \). (Exercise B1 derives the mirror image directly.)

::: {#exm-derived-rules-in-use}
[Derived rules in use]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( P \to Q, \; Q \to R, \; \neg R \vdash \neg P \), and then write the derivation out with primitive rules only.
2. Show that \( P \vee Q, \; \neg P, \; Q \to R \vdash R \).
:::
:::

::: {.solution}
*Idea.* A derived rule is a **premise-directed shortcut**: a line \( \varphi \to \psi \) with a line \( \neg\psi \) invites \( \rulename{MT} \); a disjunction with one side refuted invites \( \rulename{DS} \). This is the move this section adds to the search for derivations: before opening a box by hand, ask whether a derived rule takes the step at once.

(a) Work backwards from the goal \( \neg P \). The premise \( P \to Q \) would give it by \( \rulename{MT} \) if \( \neg Q \) were available. And \( \neg Q \) comes by \( \rulename{MT} \) from \( Q \to R \) and \( \neg R \). So \( \rulename{MT} \) is used twice, the second time on the conclusion of the first.

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {Q \to R}
  \hypo {3} {\neg R}
  \have[\ ][0] {} {\vdots}
  \have[][5] {5} {\neg P}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {Q \to R}
  \hypo {3} {\neg R}
  \have[\ ][0] {} {\vdots}
  \have[][4] {4} {\neg Q}
  \have {5} {\neg P} \mt{1,4}
\end{nd}$
\end{center}
```

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {Q \to R}
  \hypo {3} {\neg R}
  \have {4} {\neg Q} \mt{2,3}
  \have {5} {\neg P} \mt{1,4}
\end{nd}$
\end{center}
```

Line 4 is the instance with \( \varphi \) replaced by \( Q \) and \( \psi \) by \( R \); line 5 the instance with \( P \) and \( Q \). In primitive rules, each \( \rulename{MT} \) line becomes its four lines, as in lines 3–6 of the derivation of @prp-modus-tollens: a box on the hypothesis, \( \rulename{{\to}E} \), \( \rulename{\neg E} \), \( \rulename{\neg I} \). This natural expansion has eleven lines.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {Q \to R}
  \hypo {3} {\neg R}
  \open
  \hypo {4} {Q}
  \have {5} {R} \ie{2,4}
  \have {6} {\bot} \ne{5,3}
  \close
  \have {7} {\neg Q} \ni{4-6}
  \open
  \hypo {8} {P}
  \have {9} {Q} \ie{1,8}
  \have {10} {\bot} \ne{9,7}
  \close
  \have {11} {\neg P} \ni{8-10}
\end{nd}$
\end{center}
```

The literal expansion of @def-derived-rule adds a repetition of each cited line and is longer; the natural one cites the available lines directly.

(b) The disjunction \( P \vee Q \) has its left side refuted by \( \neg P \), so \( \rulename{DS} \) gives \( Q \), and then \( Q \to R \) fires.

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \hypo {2} {\neg P}
  \hypo {3} {Q \to R}
  \have[\ ][0] {} {\vdots}
  \have[][5] {5} {R}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {P \vee Q}
  \hypo {2} {\neg P}
  \hypo {3} {Q \to R}
  \have[\ ][0] {} {\vdots}
  \have[][4] {4} {Q}
  \have {5} {R} \ie{3,4}
\end{nd}$
\end{center}
```

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \hypo {2} {\neg P}
  \hypo {3} {Q \to R}
  \have {4} {Q} \ds{1,2}
  \have {5} {R} \ie{3,4}
\end{nd}$
\end{center}
```

Expanded, line 4 becomes the seven lines of the derivation of @prp-disjunctive-syllogism, with a case split on line 1 and the case \( P \) closed by \( \rulename{\bot E} \).
:::

::: {.check}
Which derived rule of this section, if any, gives a new line in one step from each pair of available lines?

(i) \( P \to Q \) and \( \neg Q \). (ii) \( P \vee Q \) and \( \neg P \). (iii) \( P \vee Q \) and \( Q \to R \). (iv) \( P \to \neg Q \) and \( Q \).
:::

::: {.solution}
(i) \( \rulename{MT} \) gives \( \neg P \). (ii) \( \rulename{DS} \) gives \( Q \). (iii) None: nothing is known about the case \( P \). (iv) None in one step: \( \rulename{MT} \) needs the negation of the conclusion \( \neg Q \), which is \( \neg\neg Q \), not \( Q \). A \( \rulename{\neg I} \) box gives \( \neg\neg Q \) from \( Q \) first, as in @exm-double-negation-introduction, and then \( \rulename{MT} \) gives \( \neg P \).
:::

## Modus tollens on numbers, and the green card

In a mathematical proof, \( \rulename{MT} \) is the step "since the conclusion fails, the hypothesis fails". Here it is with numbers.

::: {#exm-modus-tollens-instance}
[Modus tollens on numbers]

Let \( x \) be a real number with \( x^2 \le 4 \). Use the implication "if \( x > 2 \), then \( x^2 > 4 \)" to show that \( x \le 2 \), naming the derived rule.
:::

::: {.solution}
Take \( P \): "\( x > 2 \)" and \( Q \): "\( x^2 > 4 \)". The implication is \( P \to Q \). (It holds because \( x > 2 > 0 \) gives \( x^2 = x \cdot x > 2x > 4 \).) The hypothesis \( x^2 \le 4 \) is \( \neg Q \), since for real numbers \( x^2 \le 4 \) and \( x^2 > 4 \) are exact negations of each other. By \( \rulename{MT} \) (@prp-modus-tollens), \( \neg P \), that is, \( \neg(x > 2) \), which is \( x \le 2 \).
:::

The claim of @exm-wason-selection (Section 1.3), for one card, is \( E \to R \), with \( E \): "this card's number is even" and \( R \): "its color side is red".

| The card shows | So we have | What a rule gives | Turn it? |
|---|---|---|---|
| \( 6 \) | \( E \) | \( \rulename{{\to}E} \): \( R \); the back must be red | yes: a green back would break the claim |
| \( 7 \) | \( \neg E \) | nothing: no rule uses \( E \to R \) with \( \neg E \) | no |
| red | \( R \) | nothing about \( E \): concluding \( E \) would be affirming the consequent | no |
| green | \( \neg R \) | \( \rulename{MT} \): \( \neg E \); the number must be odd | yes: an even number would break the claim |

Turning the green card tests exactly the line \( \rulename{MT} \) wrote: an even number there gives \( E \), and with \( \neg R \) and \( E \to R \), \( \rulename{{\to}E} \) and \( \rulename{\neg E} \) reach \( \bot \). Modus tollens is the step people skip.

\( \rulename{CP} \) turns the claim into its contrapositive \( \neg R \to \neg E \), "a card whose color is not red has an odd number", which carries the claim's content to the green card; Section 2.5 derives the passage back, so the two say the same. The converse \( R \to E \), "a red card has an even number", is a different claim, and the card rule never made it.

::: {.check}
Which card would \( \rulename{MT} \) settle if the claim were "if a card's color side is red, then its number is even"?
:::

::: {.solution}
The \( 7 \). The claim is \( R \to E \), the \( 7 \) shows \( \neg E \), and \( \rulename{MT} \) gives \( \neg R \), so its back must not be red: turn it.
:::

::: {.second-reading title="Modus tollens and testing a claim"}
A claim about every integer of a kind makes one prediction per instance. "For every prime \( p \), the number \( 2^p - 1 \) is prime" predicts that \( 3 \), \( 7 \), \( 31 \) and \( 127 \) are prime, for \( p = 2, 3, 5, 7 \), and all four are. Write \( A \) for the claim and \( B \) for one prediction, so that \( A \to B \). The form "from \( A \to B \) and \( B \), conclude \( A \)" breaks (it is affirming the consequent, Section 1.3), so no number of confirming instances proves the claim. One failed instance refutes it, by \( \rulename{MT} \) on that instance: for \( p = 11 \), \( 2^{11} - 1 = 2047 = 23 \cdot 89 \), so the prediction \( B \) fails, and from \( A \to B \) and \( \neg B \), \( \rulename{MT} \) gives \( \neg A \). Scientists call a hypothesis that has survived many tests *corroborated*, not proved; a mathematician calls such a claim a conjecture.
:::

## How this rule looks in a mathematical proof

@thm-square-even-implies-even (Section 2.1) says that for an integer \( n \), if \( n^2 \) is even then \( n \) is even. Section 2.1 proved it by cases, with the odd case shown impossible and closed by \( \rulename{\bot E} \). Here is the same theorem argued as mathematicians usually write it, with the derived rules doing the work. We use the facts (E1)–(E3) of Section 2.1: every integer is even or odd; no integer is both; the square of an odd integer is odd.

Written the way a mathematician would write it, the proof is four sentences: *Suppose \( n^2 \) is even. Then \( n^2 \) is not odd, since no integer is both. By the contrapositive of (E3), \( n \) is not odd. As every integer is even or odd, \( n \) is even.* Each sentence after the first is one named step: \( \rulename{\neg I} \) with (E2); \( \rulename{CP} \) with \( \rulename{{\to}E} \); \( \rulename{DS} \), after exchanging the disjuncts of (E1), as line 11 of the derivation below does. The example below writes the same proof with every step tagged, and then as a derivation.

::: {#exm-square-even-via-contrapositive}
[Even square, even number, by contraposition]

Let \( n \) be an integer. Prove that if \( n^2 \) is even, then \( n \) is even, using \( \rulename{CP} \) and \( \rulename{DS} \), and label each step with its rule.
:::

::: {.solution}
*Idea.* The hypothesis "\( n^2 \) is even" hands us nothing to compute with, while "\( n \) is odd" hands us \( n = 2k + 1 \). So we turn (E3) round by \( \rulename{CP} \): a number whose square is not odd is not odd itself. Then (E1), with one side refuted, leaves "even" by \( \rulename{DS} \).

Suppose \( n^2 \) is even \( [\text{assumption for } \rulename{{\to}I}] \). If \( n^2 \) were odd \( [\text{assumption for } \rulename{\neg I}] \), it would be both even and odd \( [\rulename{\wedge I}] \), contradicting (E2) \( [\rulename{\neg E}] \); hence \( n^2 \) is not odd \( [\rulename{\neg I}] \). By (E3), if \( n \) is odd then \( n^2 \) is odd, so by contraposition, if \( n^2 \) is not odd then \( n \) is not odd \( [\rulename{CP}] \). Hence \( n \) is not odd \( [\rulename{{\to}E}] \). By (E1), \( n \) is even or odd, so \( n \) is odd or even \( [\text{or commutes}] \), by the exchange of disjuncts of @exm-disjunction-first-derivations used as a derived rule. Since \( n \) is not odd, \( n \) is even \( [\rulename{DS}] \). This proves that if \( n^2 \) is even, then \( n \) is even \( [\rulename{{\to}I}] \).

With \( E \): "\( n \) is even", \( O \): "\( n \) is odd", \( S \): "\( n^2 \) is even", \( T \): "\( n^2 \) is odd", and the three facts as premises, the skeleton is this derivation.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {E \vee O}
  \hypo {2} {\neg (S \wedge T)}
  \hypo {3} {O \to T}
  \open
  \hypo {4} {S}
  \open
  \hypo {5} {T}
  \have {6} {S \wedge T} \ai{4,5}
  \have {7} {\bot} \ne{6,2}
  \close
  \have {8} {\neg T} \ni{5-7}
  \have {9} {\neg T \to \neg O} \ctp{3}
  \have {10} {\neg O} \ie{9,8}
  \have {11} {O \vee E} \by{or commutes}{1}
  \have {12} {E} \ds{11,10}
  \close
  \have {13} {S \to E} \ii{4-12}
\end{nd}$
\end{center}
```

Line 11 is @exm-disjunction-first-derivations used as a derived rule, so that line 12 refutes the left disjunct, as \( \rulename{DS} \) requires.
:::

::: {.second-reading title="The two derivations of Even Square, line for line"}
Compare this with the twelve-line derivation after @thm-square-even-implies-even in Section 2.1. There, line 11 split on (E1) at once, and the odd case, lines 6–10, got \( T \) from (E3), built \( S \wedge T \), clashed with (E2), and closed by \( \rulename{\bot E} \). Here the same work is spread over named steps. The \( \rulename{\neg I} \) box on lines 5–7 does the clash with (E2), which there was lines 8–9. Lines 9 and 10, \( \rulename{CP} \) and \( \rulename{{\to}E} \), abbreviate a box that assumes \( O \), gets \( T \) by (E3), as line 7 did there, and clashes with line 8. Line 12, \( \rulename{DS} \), abbreviates a case split on the disjunction with the case \( O \) closed by \( \rulename{\bot E} \), as lines 5–11 did there. The short version reads the way people talk.
:::

## Common errors

::: {.warning}
A derived rule may be used only **after** its sequent has been derived, and never inside its own derivation. A "derivation" of @prp-contrapositive that justifies one of its lines by \( \rulename{CP} \) proves nothing: it assumes what it sets out to show. Exercise C2 is an example.
:::

::: {.warning}
The converse of the contrapositive is a different sequent. \( \rulename{CP} \) passes from \( P \to Q \) to \( \neg Q \to \neg P \); it does not pass from \( \neg Q \to \neg P \) back to \( P \to Q \). Try it: in a box on \( P \) the goal is \( Q \), a letter with no negation, and the natural box, on \( \neg Q \), reaches \( \bot \) and so closes to \( \neg\neg Q \), not \( Q \). Section 2.5 derives the passage back with a new rule.
:::

## The rule card

::: {#exm-derived-rules-instances}
[Instances of \( \rulename{MT} \), \( \rulename{CP} \) and \( \rulename{DS} \)]

A sequent is proved once, for letters, and used for every statement put in their place. So it pays to prove a lemma with the fewest premises and the most general letters it allows: one derivation, written once, serves every row of its rule below.

| Rule | Letters replaced | Cited lines | New line |
|---|---|---|---|
| \( \rulename{MT} \) | \( \varphi \coloneqq P \vee Q \), \( \psi \coloneqq R \wedge S \) | \( (P \vee Q) \to (R \wedge S) \), \( \neg(R \wedge S) \) | \( \neg(P \vee Q) \) |
| \( \rulename{CP} \) | \( \varphi \coloneqq \neg P \), \( \psi \coloneqq Q \to R \) | \( \neg P \to (Q \to R) \) | \( \neg(Q \to R) \to \neg\neg P \) |
| \( \rulename{DS} \) | \( \varphi \coloneqq P \to Q \), \( \psi \coloneqq \neg R \vee S \) | \( (P \to Q) \vee (\neg R \vee S) \), \( \neg(P \to Q) \) | \( \neg R \vee S \) |

**Not an instance.** From \( (P \to Q) \vee R \) and \( \neg P \), \( \rulename{DS} \) gives nothing: the refuted line must be the negation of the whole left disjunct, \( \neg(P \to Q) \), and \( \neg P \) is not that line.
:::

Chapter 1's seven rules are on the card at the end of Section 1.6; here are this chapter's so far.

| Rule | Shape | You write | Lean |
|---|---|---|---|
| \( \rulename{\neg E} \) | \( \varphi \), \( \neg\varphi \) \( \Longrightarrow \) \( \bot \) | "…, which contradicts …" | `exact hn hp` (goal `False`) |
| \( \rulename{\bot E} \) | \( \bot \) \( \Longrightarrow \) any \( \varphi \) | "This case cannot occur." "So there is nothing to prove." | `exfalso` |
| \( \rulename{\neg I} \) | box \( \varphi \) … \( \bot \) \( \Longrightarrow \) \( \neg\varphi \) | "Suppose \( P \). … This is a contradiction. Hence not \( P \)." | `intro hp` (goal `False`) |
| \( \rulename{MT} \) | (derived) \( \varphi \to \psi \), \( \neg\psi \) \( \Longrightarrow \) \( \neg\varphi \) | "Since \( Q \) fails, so does \( P \)." | `mt h hnq` |
| \( \rulename{CP} \) | (derived) \( \varphi \to \psi \) \( \Longrightarrow \) \( \neg\psi \to \neg\varphi \) | "We prove the contrapositive: suppose not \( Q \); … so not \( P \)." | `mt` |
| \( \rulename{DS} \) | (derived) \( \varphi \vee \psi \), \( \neg\varphi \) \( \Longrightarrow \) \( \psi \) | "\( P \) is impossible, so \( Q \)." | `h.resolve_left hnp` |

::: {.warning}
[Not allowed: derived rules]

Each step breaks the clause of the reading of @def-derived-rule shown.

- "\( \rulename{CP} \) on a line of the derivation of @prp-contrapositive": the sequent is not yet derived where it is used (clause 1; Exercise C2).
- "\( \neg P \) by \( \rulename{MT} \) from \( (P \wedge Q) \to R \) and \( \neg R \)": \( \rulename{MT} \) writes the negation of the whole hypothesis, \( \neg(P \wedge Q) \) (clause 4).
- "\( \rulename{MT} \) citing a line inside a closed box": the scope rule still governs every citation (clause 3).
- "\( \neg P \) in one line from \( P \to Q \), \( Q \to R \), \( \neg R \)": one instance per line; @exm-derived-rules-in-use (a) takes two \( \rulename{MT} \) lines (clause 4).
- "\( P \) by \( \rulename{\neg\neg E} \) from \( \neg\neg P \), here": \( \rulename{\neg\neg E} \) is derived only in Section 2.5 (clause 1).
:::

::: {.remark}
[Looking ahead]

Chapter 4 makes exact the replacement of letters that a derived rule allows, under the name substitution.
:::

## Exercises

### A. Check your understanding

::: {#exr-derived-rules-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State @def-derived-rule in your own words, including what "already derived" and "the same statement" require.
2. Here is a derivation that uses \( \rulename{MT} \). Rewrite it with primitive rules only.

    ```{=latex}
    \begin{center}
    $\begin{nd}
      \hypo {1} {R \to P}
      \hypo {2} {\neg P}
      \have {3} {\neg R} \mt{1,2}
      \have {4} {\neg R \vee S} \oi{3}
    \end{nd}$
    \end{center}
    ```
3. True or false, with a reason: "\( \neg Q \to \neg P \) follows from \( P \to Q \) by \( \rulename{CP} \), so \( P \to Q \) follows from \( \neg Q \to \neg P \) by \( \rulename{CP} \)."
:::
:::

::: {.solution}
(a) If a sequent has been derived earlier (not inside the derivation that uses it), then in a later derivation we may replace its letters by statements, each letter by one statement everywhere it occurs, and, when available lines hold the resulting instances of its premises, write the resulting instance of its conclusion on one line, citing the sequent and those lines.

(b) Line 3 becomes a box on \( R \), then \( \rulename{{\to}E} \), \( \rulename{\neg E} \), and \( \rulename{\neg I} \):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {R \to P}
  \hypo {2} {\neg P}
  \open
  \hypo {3} {R}
  \have {4} {P} \ie{1,3}
  \have {5} {\bot} \ne{4,2}
  \close
  \have {6} {\neg R} \ni{3-5}
  \have {7} {\neg R \vee S} \oi{6}
\end{nd}$
\end{center}
```

(c) False. \( \rulename{CP} \) is the sequent \( P \to Q \vdash \neg Q \to \neg P \). Applied to \( \neg Q \to \neg P \), with \( P \) replaced by \( \neg Q \) and \( Q \) by \( \neg P \), it gives \( \neg\neg P \to \neg\neg Q \), not \( P \to Q \). The passage from \( \neg Q \to \neg P \) to \( P \to Q \) is the converse, a different sequent; Section 2.5 derives it with a new rule.
:::

::: {#exr-derived-rules-a2}
[A2: Drill]

Each part takes a line or two. The parts run from single steps, through a missing line and a justification column, to whole derivations. Let \( x \) be a real number.

::: {.enumerate options="label=(\alph*)"}
1. Lines 1 \( (A \wedge B) \to C \), 2 \( \neg C \). What does "\( \rulename{MT} \) 1, 2" write?
2. Lines 1 \( \neg P \vee Q \), 2 \( \neg\neg P \). What does "\( \rulename{DS} \) 1, 2" write?
3. What does \( \rulename{CP} \) write from \( (x > 0) \to (x^2 > 0) \)?
4. Line 3 is \( \neg(P \vee Q) \) and line 5 is \( \neg R \to (P \vee Q) \). What does "\( \rulename{MT} \) 5, 3" write?
5. Written out with primitive rules, citing available lines directly, how many lines does one \( \rulename{MT} \) line become?
6. Line 8 is \( \neg(R \wedge S) \), justified "\( \rulename{MT} \) 2, 6", and line 6 is \( \neg T \). What is line 2?
7. Line 9 is \( R \to S \), justified "\( \rulename{DS} \) 4, 7", and line 7 is \( \neg(P \wedge Q) \). What is line 4?
8. Lines 1–4 are the premises \( P \vee (Q \to R) \), \( \neg P \), \( S \to Q \), \( \neg R \). Justify 5 \( Q \to R \); 6 \( \neg Q \); 7 \( \neg S \).
9. Lines 1 \( P \to \neg Q \), 2 \( Q \). Does \( \rulename{MT} \) apply?
10. Lines 1 \( P \vee Q \), 2 \( \neg Q \). Does \( \rulename{DS} \), as stated, apply?
11. May a derivation of @prp-contrapositive use \( \rulename{CP} \) on one of its lines?
12. Find the illegal line: 1 \( P \to Q \); 2 \( \neg P \); 3 \( \neg Q \), \( \rulename{MT} \) 1, 2.
13. Derive \( P \to (Q \wedge R), \ \neg R \vdash \neg P \).
14. Derive \( P \vee Q, \ \neg P, \ \neg Q \vdash R \).
15. Derive \( \neg P \to Q, \ \neg Q \vdash \neg\neg P \) in one line.
:::
:::

::: {.solution}
(a) \( \neg(A \wedge B) \).

(b) \( Q \) (the letter \( P \) of \( \rulename{DS} \) replaced by \( \neg P \)).

(c) \( \neg(x^2 > 0) \to \neg(x > 0) \), that is, \( (x^2 \le 0) \to (x \le 0) \).

(d) \( \neg\neg R \), with \( \varphi \coloneqq \neg R \) and \( \psi \coloneqq P \vee Q \).

(e) Four: an assumption, \( \rulename{{\to}E} \), \( \rulename{\neg E} \), \( \rulename{\neg I} \) (the figure).

(f) \( (R \wedge S) \to T \).

(g) \( (P \wedge Q) \vee (R \to S) \).

(h) 5 \( \rulename{DS} \) 1, 2; 6 \( \rulename{MT} \) 5, 4; 7 \( \rulename{MT} \) 3, 6.

(i) Not yet: \( \rulename{MT} \) needs \( \neg\neg Q \). Write it from \( Q \) by a \( \rulename{\neg I} \) box first; then \( \rulename{MT} \) gives \( \neg P \).

(j) No: \( \rulename{DS} \) refutes the left disjunct. Use the other form (Exercise B1 (a)) or exchange the disjuncts first.

(k) No: a derived rule may be used only after its sequent has been derived.

(l) Line 3: \( \rulename{MT} \) needs the negation of the conclusion, \( \neg Q \), and gives \( \neg P \); line 3 runs it backwards, from \( \neg P \) to \( \neg Q \). The form breaks at \( P \) false, \( Q \) true.

(m) 3 \( P \), assumption; 4 \( Q \wedge R \), \( \rulename{{\to}E} \) 1, 3; 5 \( R \), \( \rulename{\wedge E} \) 4; 6 \( \bot \), \( \rulename{\neg E} \) 5, 2; 7 \( \neg P \), \( \rulename{\neg I} \) 3–6. (\( \rulename{MT} \) does not match: \( \neg(Q \wedge R) \) is not available.)

(n) 4 \( Q \), \( \rulename{DS} \) 1, 2; 5 \( \bot \), \( \rulename{\neg E} \) 4, 3; 6 \( R \), \( \rulename{\bot E} \) 5.

(o) 3 \( \neg\neg P \), \( \rulename{MT} \) 1, 2.
:::

### B. Practice

::: {#exr-derived-rules-b1}
[B1: The other disjunctive syllogism, used later]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( P \vee Q, \; \neg Q \vdash P \) by a derivation from the primitive rules.
2. Let \( x \) be a real number with \( x^2 = 1 \) and \( x > 0 \). You may use that \( x^2 = 1 \) implies \( x = 1 \) or \( x = -1 \). Deduce that \( x = 1 \), naming the result you use.
:::
:::

::: {.solution}
(a) As in @prp-disjunctive-syllogism, with the roles of the boxes exchanged: now the case \( Q \) is the impossible one.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \hypo {2} {\neg Q}
  \open
  \hypo {3} {P}
  \close
  \open
  \hypo {4} {Q}
  \have {5} {\bot} \ne{4,2}
  \have {6} {P} \be{5}
  \close
  \have {7} {P} \oe{1,3-3,4-6}
\end{nd}$
\end{center}
```

(b) Since \( x^2 = 1 \), we have \( x = 1 \) or \( x = -1 \). Since \( x > 0 \) and \( -1 < 0 \), we have \( x \ne -1 \). By part (a), with \( P \): "\( x = 1 \)" and \( Q \): "\( x = -1 \)", used as a derived rule (@def-derived-rule), we conclude \( x = 1 \).
:::

::: {#exr-derived-rules-b2}
[B2: Putting a derivation in order]

Here are nine lines, each a statement with its justification. Seven of them, in the right order and with the right boxes, form a derivation of \( P \to Q \vdash \neg Q \to \neg P \) from the primitive rules. Give the order, and say where each box opens and closes. Then say why each of the other two lines cannot be used.

::: {.enumerate options="label=(\roman*)"}
1. \( \neg Q \to \neg P \), by \( \rulename{{\to}I} \) on the box from \( \neg Q \) to \( \neg P \).
2. \( Q \), by \( \rulename{{\to}E} \) from \( P \to Q \) and \( P \).
3. \( P \to Q \), premise.
4. \( \neg P \), by \( \rulename{\neg I} \) on the box from \( P \) to \( \bot \).
5. \( \neg Q \), assumption.
6. \( \bot \), by \( \rulename{\neg E} \) from \( Q \) and \( \neg Q \).
7. \( P \), assumption.
8. \( \neg P \), assumption, opening the box for the \( \rulename{\neg I} \) that proves \( \neg P \).
9. \( Q \), by \( \rulename{{\to}E} \) from \( P \to Q \) and the assumption \( P \) of (vii), written directly below (iv).
:::
:::

::: {.solution}
The order is (iii), (v), (vii), (ii), (vi), (iv), (i), with one box opened by (v) and closed after (iv), and a second box inside it, opened by (vii) and closed after (vi). This is the derivation of @prp-contrapositive. It is the only admissible order. The premise comes first. (i) needs a box from \( \neg Q \) to \( \neg P \), so (v) opens a box whose last line is (iv). (iv) needs a box from \( P \) to \( \bot \) inside it, so (vii) opens a box whose last line is (vi). Inside that box, (ii) needs (vii), and (vi) needs (ii) and (v).

(viii) cannot be used. \( \rulename{\neg I} \) proves \( \neg P \) from a box opened by \( P \), the statement being negated (@def-rules-negation). A box opened by \( \neg P \) and ending in \( \bot \) would give \( \neg\neg P \). (ix) cannot be used where it is placed. Directly below (iv), the box opened by (vii) has closed, so the assumption \( P \) is not available (@def-derivation). Placed inside that box, the same line is (ii).
:::

::: {#exr-derived-rules-b3}
[B3: Two refutations]

A search for \( (P \vee Q) \to R, \; \neg R \vdash \neg P \wedge \neg Q \) has reached the stage below. You may use the derived rules of this section. *Name the move, then complete it.*

```{=latex}
% schema (partial derivation: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {(P \vee Q) \to R}
  \hypo {2} {\neg R}
  \have {3} {\neg (P \vee Q)} \mt{1,2}
  \have[\ ][0] {} {\vdots}
  \have[][12] {12} {\neg P \wedge \neg Q}
\end{nd}$
\end{center}
```
:::

::: {.solution}
The premises are an implication and the negation of its conclusion, which invites \( \rulename{MT} \): it gives \( \neg(P \vee Q) \). The goal is a conjunction, so we need \( \neg P \) and \( \neg Q \), each a negation, each by a \( \rulename{\neg I} \) box. In the box of \( P \), the clash is manufactured: \( \rulename{\vee I} \) gives \( P \vee Q \), which clashes with line 3. The box of \( Q \) is the same.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \vee Q) \to R}
  \hypo {2} {\neg R}
  \have {3} {\neg (P \vee Q)} \mt{1,2}
  \open
  \hypo {4} {P}
  \have {5} {P \vee Q} \oi{4}
  \have {6} {\bot} \ne{5,3}
  \close
  \have {7} {\neg P} \ni{4-6}
  \open
  \hypo {8} {Q}
  \have {9} {P \vee Q} \oi{8}
  \have {10} {\bot} \ne{9,3}
  \close
  \have {11} {\neg Q} \ni{8-10}
  \have {12} {\neg P \wedge \neg Q} \ai{7,11}
\end{nd}$
\end{center}
```

Line 3 is \( \rulename{MT} \) with \( \varphi \) replaced by \( P \vee Q \) and \( \psi \) by \( R \).
:::

::: {#exr-derived-rules-b4}
[B4: Dilemmas as derived rules, used later]

::: {.enumerate options="label=(\alph*)"}
1. Section 1.6 derived the constructive dilemma, @exm-constructive-dilemma. Use it as a derived rule, tagged \( \rulename{CD} \), together with @exm-disjunction-first-derivations, to derive \( (P \to R) \wedge (Q \to R), \ P \vee Q \vdash R \) in four lines.
2. Derive the destructive dilemma \( (P \to R) \wedge (Q \to S), \ \neg R \vee \neg S \vdash \neg P \vee \neg Q \), using \( \rulename{MT} \).
3. Derive \( \neg(P \wedge Q) \vdash P \to \neg Q \): "\( P \) rules out \( Q \)", the form in which the traditional *modus ponendo tollens* is used. Then break "from \( \neg(P \wedge Q) \) and \( \neg P \), conclude \( Q \)".
4. Let \( n \) be an integer. Use (b) to show: if \( n \) is odd or \( n \) is not a multiple of \( 3 \), then \( n \) is not a multiple of \( 4 \) or not a multiple of \( 9 \). Take as premises that a multiple of \( 4 \) is even and a multiple of \( 9 \) is a multiple of \( 3 \), and read "odd" as "not even".
:::
:::

::: {.solution}
(a) Line 3 is @exm-constructive-dilemma, \( (P \to R) \wedge (Q \to S), \ P \vee Q \vdash R \vee S \), with \( S \) replaced by \( R \). Line 4 is the second sequent of @exm-disjunction-first-derivations, \( P \vee P \vdash P \), with \( P \) replaced by \( R \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \to R) \wedge (Q \to R)}
  \hypo {2} {P \vee Q}
  \have {3} {R \vee R} \by{CD}{1,2}
  \have {4} {R} \by{or merges}{3}
\end{nd}$
\end{center}
```

(b) Split the premise \( \neg R \vee \neg S \); in each case \( \rulename{MT} \) refutes one hypothesis, and \( \rulename{\vee I} \) builds the goal.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \to R) \wedge (Q \to S)}
  \hypo {2} {\neg R \vee \neg S}
  \have {3} {P \to R} \ae{1}
  \have {4} {Q \to S} \ae{1}
  \open
  \hypo {5} {\neg R}
  \have {6} {\neg P} \mt{3,5}
  \have {7} {\neg P \vee \neg Q} \oi{6}
  \close
  \open
  \hypo {8} {\neg S}
  \have {9} {\neg Q} \mt{4,8}
  \have {10} {\neg P \vee \neg Q} \oi{9}
  \close
  \have {11} {\neg P \vee \neg Q} \oe{2,5-7,8-10}
\end{nd}$
\end{center}
```

(c) The goal is an implication, so open a box on \( P \); its goal \( \neg Q \) is a negation, so open a \( \rulename{\neg I} \) box on \( Q \) inside it.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \wedge Q)}
  \open
  \hypo {2} {P}
  \open
  \hypo {3} {Q}
  \have {4} {P \wedge Q} \ai{2,3}
  \have {5} {\bot} \ne{4,1}
  \close
  \have {6} {\neg Q} \ni{3-5}
  \close
  \have {7} {P \to \neg Q} \ii{2-6}
\end{nd}$
\end{center}
```

The look-alike breaks with \( P \): "\( x > 5 \)" and \( Q \): "\( x > 3 \)", at \( x = 0 \): \( \neg(P \wedge Q) \) and \( \neg P \) are true and \( Q \) is false, so the counterexample set \( \neg(P \wedge Q) \), \( \neg P \), \( \neg Q \) is true. *Modus ponendo tollens* uses a negated conjunction and **affirms** one conjunct; \( \rulename{DS} \) uses a disjunction and **refutes** one disjunct; mixing the two is the error of the look-alike.

(d) Write \( F \): "\( n \) is a multiple of \( 4 \)", \( E \): "\( n \) is even", \( N \): "\( n \) is a multiple of \( 9 \)", \( T \): "\( n \) is a multiple of \( 3 \)". The premises are \( (F \to E) \wedge (N \to T) \) (since \( 4k = 2(2k) \) and \( 9k = 3(3k) \)), and the hypothesis is \( \neg E \vee \neg T \). Open a box on the hypothesis; inside it, (b) as a derived rule, with \( P \), \( Q \), \( R \), \( S \) replaced by \( F \), \( N \), \( E \), \( T \), gives \( \neg F \vee \neg N \); then \( \rulename{{\to}I} \) closes the box on \( (\neg E \vee \neg T) \to (\neg F \vee \neg N) \). For instance \( n = 7 \) is odd, and not a multiple of \( 4 \).

**Marking scheme.** (10 points)

- 2: (a), \( \rulename{CD} \) with the replacement \( S \coloneqq R \) named, then \( P \vee P \vdash P \).
- 3: (b), \( \rulename{MT} \) in each case box, both boxes ending in \( \neg P \vee \neg Q \).
- 3: (c), the nested \( \rulename{\neg I} \) box inside the \( \rulename{{\to}I} \) box (2), and a correct break of the look-alike (1).
- 2: (d), the letters, the premises, and the use of (b) inside a \( \rulename{{\to}I} \) box.

Fatal error (0 for (b)): a case box citing a line of the other case box.
:::

::: {#exr-derived-rules-b5}
[B5: Derive or break]

For each claim, derive it with the rules so far, including \( \rulename{MT} \), \( \rulename{CP} \), \( \rulename{DS} \) and the sequents derived in this book so far, or break it by statements about a real number \( x \) that make its counterexample set true at one value of \( x \).

::: {.enumerate options="label=(\alph*)"}
1. \( P \vee Q, \ Q \vdash \neg P \).
2. \( (P \vee R) \to \neg Q, \ Q \vdash \neg R \).
3. \( \neg P \to Q \vdash \neg Q \to \neg P \).
4. \( P \vee (Q \wedge R), \ \neg P \vdash R \).
5. \( (P \wedge Q) \to R, \ \neg R, \ P \vdash \neg Q \).
6. \( P \to (Q \vee R), \ \neg Q \vdash P \to R \).
7. \( P \to (Q \vee R), \ \neg Q \vdash R \).
8. \( (P \to Q) \wedge (R \to S), \ \neg Q \vee \neg S \vdash \neg P \wedge \neg R \).
:::
:::

::: {.solution}
(a) Break. Take \( P \): "\( x > 0 \)" and \( Q \): "\( x > 1 \)". At \( x = 2 \), \( P \vee Q \) and \( Q \) are true and \( P \) is true, so the counterexample set \( P \vee Q \), \( Q \), \( \neg\neg P \) is true. This is affirming a disjunct (Section 1.6).

(b) Derive. The goal is a negation: open a box on \( R \), and manufacture the premise's hypothesis by \( \rulename{\vee I} \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \vee R) \to \neg Q}
  \hypo {2} {Q}
  \open
  \hypo {3} {R}
  \have {4} {P \vee R} \oi{3}
  \have {5} {\neg Q} \ie{1,4}
  \have {6} {\bot} \ne{2,5}
  \close
  \have {7} {\neg R} \ni{3-6}
\end{nd}$
\end{center}
```

(c) Break. Take \( P \): "\( x > 0 \)" and \( Q \): "\( x > 5 \)". At \( x = 1 \), \( \neg P \to Q \) is true (its hypothesis fails), \( \neg Q \) is true and \( \neg P \) is false, so the counterexample set \( \neg P \to Q \), \( \neg(\neg Q \to \neg P) \) is true. (\( \rulename{CP} \) on \( \neg P \to Q \) gives \( \neg Q \to \neg\neg P \), not this.)

(d) Derive.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee (Q \wedge R)}
  \hypo {2} {\neg P}
  \have {3} {Q \wedge R} \ds{1,2}
  \have {4} {R} \ae{3}
\end{nd}$
\end{center}
```

(e) Derive. \( \rulename{MT} \) refutes the conjunction; then a \( \rulename{\neg I} \) box on \( Q \) rebuilds it from the premise \( P \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge Q) \to R}
  \hypo {2} {\neg R}
  \hypo {3} {P}
  \have {4} {\neg (P \wedge Q)} \mt{1,2}
  \open
  \hypo {5} {Q}
  \have {6} {P \wedge Q} \ai{3,5}
  \have {7} {\bot} \ne{6,4}
  \close
  \have {8} {\neg Q} \ni{5-7}
\end{nd}$
\end{center}
```

(f) Derive.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \vee R)}
  \hypo {2} {\neg Q}
  \open
  \hypo {3} {P}
  \have {4} {Q \vee R} \ie{1,3}
  \have {5} {R} \ds{4,2}
  \close
  \have {6} {P \to R} \ii{3-5}
\end{nd}$
\end{center}
```

(g) Break. Take \( P \): "\( x > 5 \)", \( Q \): "\( x > 3 \)", \( R \): "\( x > 4 \)". The premise \( P \to (Q \vee R) \) is true for every \( x \). At \( x = 0 \), \( \neg Q \) is true and \( R \) is false, so the counterexample set \( P \to (Q \vee R) \), \( \neg Q \), \( \neg R \) is true.

(h) Break. Take \( P \): "\( x > 5 \)", \( Q \): "\( x > 9 \)", \( R \): "\( x > 0 \)", \( S \): "\( x > -1 \)". At \( x = 1 \), \( P \to Q \) is true (its hypothesis fails) and \( R \to S \) is true (for every \( x \)), \( \neg Q \vee \neg S \) is true since \( \neg Q \) is, and \( \neg P \wedge \neg R \) is false, since \( R \) is true. So the counterexample set \( (P \to Q) \wedge (R \to S) \), \( \neg Q \vee \neg S \), \( \neg(\neg P \wedge \neg R) \) is true.

(a) and (c) are the look-alikes of \( \rulename{DS} \) and of \( \rulename{CP} \); (g) drops the hypothesis that (f) keeps in its box; (h) is the destructive dilemma of Exercise B4 (b) with the \( \vee \) of its conclusion made \( \wedge \).

**Marking scheme.** (16 points) For each claim: 1 for the verdict; 1 for a derivation every line of which checks, or for a choice of statements and one value of \( x \) at which **every** member of the counterexample set is true. Fatal errors (0 for the claim): a "break" at which a premise fails; \( \rulename{RAA} \) or \( \rulename{\neg\neg E} \) in a derivation.
:::

### C. Going deeper

::: {#exr-derived-rules-c1}
[C1: Two premises that cannot both fail, used later]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( P \to Q, \; \neg P \to R, \; \neg Q, \; \neg R \vdash \bot \), using \( \rulename{MT} \) twice.
2. Hence show that \( P \to Q, \; \neg P \to R \vdash \neg(\neg Q \wedge \neg R) \) with the rules so far.
3. In words, the conclusion of (b) says that \( Q \) and \( R \) do not both fail. Explain why a derivation with the rules so far naturally ends at \( \neg(\neg Q \wedge \neg R) \) rather than at \( Q \vee R \).
:::
:::

::: {.solution}
(a) The first \( \rulename{MT} \) has \( \varphi = P \), \( \psi = Q \). The second has \( \varphi = \neg P \), \( \psi = R \), so it gives the negation of \( \neg P \), which is \( \neg\neg P \). Lines 5 and 6 then clash.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {\neg P \to R}
  \hypo {3} {\neg Q}
  \hypo {4} {\neg R}
  \have {5} {\neg P} \mt{1,3}
  \have {6} {\neg\neg P} \mt{2,4}
  \have {7} {\bot} \ne{5,6}
\end{nd}$
\end{center}
```

Line 7 cites \( \neg P \) and then \( \neg\neg P \): the unnegated line first, with \( \varphi \) of \( \rulename{\neg E} \) replaced by \( \neg P \).

(b) The goal is a negation, so open a box on \( \neg Q \wedge \neg R \) and aim at \( \bot \). Inside, \( \rulename{\wedge E} \) supplies the two negated premises of (a), and the rest is (a).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {\neg P \to R}
  \open
  \hypo {3} {\neg Q \wedge \neg R}
  \have {4} {\neg Q} \ae{3}
  \have {5} {\neg R} \ae{3}
  \have {6} {\neg P} \mt{1,4}
  \have {7} {\neg\neg P} \mt{2,5}
  \have {8} {\bot} \ne{6,7}
  \close
  \have {9} {\neg (\neg Q \wedge \neg R)} \ni{3-8}
\end{nd}$
\end{center}
```

(c) To reach \( Q \vee R \) by \( \rulename{\vee I} \) we would need \( Q \) or \( R \) on its own. The premises give \( Q \) once \( P \) is known and \( R \) once \( \neg P \) is known, and nothing available says which of \( P \), \( \neg P \) holds. What the rules so far can do is refute the opposite, \( \neg Q \wedge \neg R \), by a \( \rulename{\neg I} \) box, and that gives the negation in (b). The step from (b) to \( Q \vee R \) uses the rule of Section 2.5.
:::

::: {#exr-derived-rules-c2}
[C2: A circular derivation]

A student offers this derivation of \( P \to Q \vdash \neg Q \to \neg P \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \open
  \hypo {2} {\neg Q}
  \have {3} {\neg Q \to \neg P} \ctp{1}
  \have {4} {\neg P} \ie{3,2}
  \close
  \have {5} {\neg Q \to \neg P} \ii{2-4}
\end{nd}$
\end{center}
```

::: {.enumerate options="label=(\alph*)"}
1. Every line is an instance of the rule it names. What is wrong?
2. Give a correct derivation. May line 3 be replaced by a line "\( \neg P \), \( \rulename{MT} \) 1, 2"?
:::
:::

::: {.solution}
(a) Line 3 uses \( \rulename{CP} \), the derived rule whose sequent, \( P \to Q \vdash \neg Q \to \neg P \), is the very one being derived. @def-derived-rule allows a sequent to be used only when it has **already been derived**; here it has not, so line 3 has no justification. (The whole derivation is also pointless: line 3 alone is already the goal.)

(b) The derivation of @prp-contrapositive, from the primitive rules:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \open
  \hypo {2} {\neg Q}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {\bot} \ne{4,2}
  \close
  \have {6} {\neg P} \ni{3-5}
  \close
  \have {7} {\neg Q \to \neg P} \ii{2-6}
\end{nd}$
\end{center}
```

Yes: a line "\( \neg P \), \( \rulename{MT} \) 1, 2" inside the box of \( \neg Q \) is legitimate, because @prp-modus-tollens was derived from the primitive rules, without \( \rulename{CP} \). What matters is that the chain of derived rules ends in primitive rules, without a loop.
:::

::: {#exr-derived-rules-c3}
[C3: Exit check: labeling a proof]

Here is a proof that for an integer \( n \), if \( n^2 \) is odd, then \( n \) is odd.

> Suppose \( n^2 \) is odd. If \( n \) were even, \( n = 2k \), then \( n^2 = 2(2k^2) \) would be even; so, by contraposition, since \( n^2 \) is not even (it is odd, and no integer is both), \( n \) is not even. As every integer is even or odd, \( n \) is odd.

Label each sentence, or part of a sentence, with the rule or rules it uses, primitive or derived. Take as premises the facts (E1) and (E2) of Section 2.1 and the school computation "if \( n \) is even, then \( n^2 \) is even".
:::

::: {.solution}
Write \( E \): "\( n \) is even", \( O \): "\( n \) is odd", \( S \): "\( n^2 \) is even", \( T \): "\( n^2 \) is odd".

- "Suppose \( n^2 \) is odd": the assumption \( T \) of the box for \( \rulename{{\to}I} \), whose goal is \( O \).
- "If \( n \) were even, \( n = 2k \), then \( n^2 = 2(2k^2) \) would be even": the implication \( E \to S \), a premise (the school computation). Reading the sentence as a \( \rulename{{\to}I} \) box that proves \( E \to S \), assuming \( E \) and computing, is equally correct.
- "\( n^2 \) is not even (it is odd, and no integer is both)": \( \neg S \), by \( \rulename{\neg I} \): a box on \( S \) builds \( S \wedge T \) by \( \rulename{\wedge I} \) and clashes with (E2), \( \neg(S \wedge T) \), by \( \rulename{\neg E} \).
- "by contraposition … \( n \) is not even": \( \rulename{CP} \) on \( E \to S \) gives \( \neg S \to \neg E \), and \( \rulename{{\to}E} \) with \( \neg S \) gives \( \neg E \). (One \( \rulename{MT} \) line does both.)
- "As every integer is even or odd, \( n \) is odd": \( \rulename{DS} \) on (E1), \( E \vee O \), with the left side \( E \) refuted, gives \( O \).
- The frame as a whole: \( \rulename{{\to}I} \), closing the box of \( T \) on \( O \), gives \( T \to O \).

As a derivation:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {E \vee O}
  \hypo {2} {E \to S}
  \hypo {3} {\neg (S \wedge T)}
  \open
  \hypo {4} {T}
  \open
  \hypo {5} {S}
  \have {6} {S \wedge T} \ai{5,4}
  \have {7} {\bot} \ne{6,3}
  \close
  \have {8} {\neg S} \ni{5-7}
  \have {9} {\neg S \to \neg E} \ctp{2}
  \have {10} {\neg E} \ie{9,8}
  \have {11} {O} \ds{1,10}
  \close
  \have {12} {T \to O} \ii{4-11}
\end{nd}$
\end{center}
```

The computation is right: \( (2k)^2 = 4k^2 = 2(2k^2) \), and \( 2k^2 \) is an integer.

**Marking scheme.** (10 points)

- 2: identifies the frame as \( \rulename{{\to}I} \), with the box opened on the hypothesis "\( n^2 \) is odd".
- 2: identifies "\( n^2 \) is not even" as \( \rulename{\neg I} \), naming the clash (with "no integer is both", by \( \rulename{\neg E} \)).
- 3: identifies \( \rulename{CP} \) (then \( \rulename{{\to}E} \)), or \( \rulename{MT} \), applied to "if \( n \) is even, then \( n^2 \) is even", with that antecedent and consequent. Reading the "if \( n \) were even" sentence as a premise or as a \( \rulename{{\to}I} \) box that proves the implication earns these points equally.
- 2: identifies \( \rulename{DS} \) on "every integer is even or odd", naming "even" as the refuted side.
- 1: names the closing \( \rulename{{\to}I} \).

Fatal errors (0 for the step): naming anything but \( \rulename{\neg I} \) for the "not even" step (it concludes a negation from a box on the unnegated statement); applying \( \rulename{CP} \) to the converse, "if \( n^2 \) is even, then \( n \) is even".
:::

<!-- dependency ledger
prp-modus-tollens (claim): the motivating arguments: n even gives n^2 even; x >= 1 gives x^2 >= x >= 1; x^2 < 1 and x < 1 are the exact negations of x^2 >= 1 and x >= 1 | school algebra, shown inline; AN1.1 (promised)
def-derived-rule (claim): pasting a derivation (repetitions, shifted line numbers) keeps every citation available; iterated expansion terminates | argued inline in the fold "Why a derived rule adds no power", from def-derivation's scope rule and (D3)
def-derived-rule (claim): letters of a derived sequent may be replaced uniformly by any statements | def-derivable and def-rule-schema (cited); made exact in F1.3 (substitution, the Looking-ahead box)
def-derived-rule (claim): the figure: line 3 on the left stands for lines 3-6 on the right | read off the two derivations (prp-modus-tollens, cited)
lem-weakening-cut (proof): renumbering lines and moving boxes as blocks preserves nesting, availability and rule instances | inline (checked clause by clause against def-derivation)
lem-weakening-cut (proof): a one-line derivation whose only line is a premise is a derivation | def-derivation, def-derivable (a premise line; the last line lies in no box)
lem-weakening-cut (claim): cut is why a derived-rule line outside every box is legitimate | lem-weakening-cut (c), def-derived-rule (cited)
exm-derived-rules-instances (example): each row is an instance of its rule's sequent under the stated replacement; the look-alike is not | read off prp-modus-tollens, prp-contrapositive, prp-disjunctive-syllogism (cited)
exm-modus-tollens-instance (example): x > 2 implies x^2 > 4; x^2 <= 4 is the negation of x^2 > 4; x <= 2 is the negation of x > 2 | school algebra, shown inline
exm-modus-tollens-instance (example): (the green-card table) a card's color side has one color, so green is not red; the turned cards 6 and green | stated in the table; exm-wason-selection (cited)
exm-modus-tollens-instance (example): the passage from the contrapositive back to the claim | F1.2 s05 prp-contrapositive-converse (prose pointer, later section of this chapter; nothing here depends on it)
exm-modus-tollens-instance (example): (fold "Modus tollens and testing a claim") 2^p - 1 is 3, 7, 31, 127 for p = 2, 3, 5, 7, all prime; 2^11 - 1 = 2047 = 23 * 89 | arithmetic, inline; checked by verify/ch02/exm-modus-tollens-instance.py
exm-modus-tollens-instance (example): (same fold) affirming the consequent breaks | F1.1 §04 (Section 1.3, affirming the consequent; prose pointer)
exm-square-even-via-contrapositive (example): (E1)-(E3) and the parity computation | school facts stated in F1.2 §01 (thm-square-even-implies-even)
exr-derived-rules-a2 (solution): (c) not(x^2 > 0) is x^2 <= 0 and not(x > 0) is x <= 0; (l) the break at P false, Q true | order convention of F1.2 §01 (prose); inline
exr-derived-rules-b1 (solution): -1 < 0; x^2 = 1 gives x = 1 or x = -1 | school algebra; the second is supplied by the item
exr-derived-rules-b4 (solution): (a) uses exm-constructive-dilemma and exm-disjunction-first-derivations as derived rules | cited; def-derived-rule
exr-derived-rules-b4 (solution): a multiple of 4 is even (4k = 2(2k)); a multiple of 9 is a multiple of 3 (9k = 3(3k)); 7 is odd and not a multiple of 4; the look-alike break at x = 0 | school arithmetic, inline; checked by verify/ch02/exr-derived-rules-b4.py
exr-derived-rules-b5 (solution): the four breaks (x = 2, 1, 0, 1) and the premises true for every x in (g), (h) | order of the reals, inline; checked by verify/ch02/exr-derived-rules-b5.py
exr-derived-rules-c3 (solution): (2k)^2 = 2(2k^2); (E1), (E2) | computation inline; facts of F1.2 §01
-->
