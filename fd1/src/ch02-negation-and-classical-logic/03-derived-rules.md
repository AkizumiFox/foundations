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
Read the skeleton off the goal. The goal \( \neg P \) is a negation, and Section 2.2's move for a negated goal is a box opened on what is negated, here \( P \), with goal \( \bot \). Inside the box, look for a clash (Section 2.1's move for the goal \( \bot \)). The premise \( \neg Q \) will clash with \( Q \), so \( Q \) is the subgoal, and the premise \( P \to Q \) gives it from the box's own assumption.
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

The statement \( \neg Q \to \neg P \) is called the **contrapositive** of \( P \to Q \). Like modus tollens, its derivation uses only the rules so far: \( \rulename{{\to}I} \), \( \rulename{{\to}E} \), \( \rulename{\neg I} \), and \( \rulename{\neg E} \). The passage back, from \( \neg Q \to \neg P \) to \( P \to Q \), is a different matter; the warnings below return to it.

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
2. **"Replace each letter … the same statement for every occurrence."** The letters of a derived sequent stood for arbitrary statements all along (@def-derivable), so they may be replaced by any statements, provided the replacement is **uniform**. From \( (A \wedge B) \to C \) and \( \neg C \), the rule \( \rulename{MT} \) gives \( \neg(A \wedge B) \), with \( \varphi \) replaced by \( A \wedge B \) and \( \psi \) by \( C \). Chapter 3 makes this replacement exact, under the name substitution.
3. **"Available at line \( k \)."** The scope rule of @def-derivation still governs every citation. A derived rule may not reach into a closed box, just as a primitive rule may not.
4. **"The resulting instance of \( \psi \)."** The rule writes the conclusion, with the same replacement, and nothing else. The derived rule does not open or close any box of the derivation that uses it.

We give the derived rules of this section short tags: \( \rulename{MT} \) for @prp-modus-tollens, \( \rulename{CP} \) for @prp-contrapositive, and, once it is proved below, \( \rulename{DS} \) for @prp-disjunctive-syllogism. Every other derived sequent is a derived rule too, cited by its name: the five lines written out in @exm-vacuous-square, for instance, are now one line citing @prp-vacuous-implication.

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

::: {.warning}
A derived rule must match its sequent exactly, under one uniform replacement of letters. From \( P \to Q \) and \( \neg R \), \( \rulename{MT} \) gives nothing: no single statement in place of \( \psi \) turns the pair into \( \varphi \to \psi \) and \( \neg\psi \). Equally, from \( P \to \neg Q \) and \( Q \), \( \rulename{MT} \) gives nothing yet: it needs the negation of the conclusion, \( \neg\neg Q \), and \( Q \) is not that line. (Here \( \rulename{\neg I} \) would give \( \neg\neg Q \) first, as in @exm-double-negation-introduction, and then \( \rulename{MT} \) applies.) Likewise \( \rulename{DS} \), as stated below, refutes the **left** disjunct; applied blindly to \( P \vee Q \) and \( \neg Q \), it does not match.
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

The same step settles the card most people leave on the table in @exm-wason-selection (Section 1.4): the cards show \( 6 \), \( 7 \), red, and green, and the claim is "if a card shows an even number on one side, then its other side is red". For the green card, let \( E \) be "this card's number is even" and \( R \) "its color side is red". The claim, for this card, is \( E \to R \). The card shows green, so \( \neg R \). If the claim holds, \( \rulename{MT} \) gives \( \neg E \): the hidden number must be odd. Turning the card tests exactly that line: an even number there would give \( E \), and with \( \neg R \) and \( E \to R \), \( \rulename{{\to}E} \) and \( \rulename{\neg E} \) would reach \( \bot \). The red card offers only \( R \), and from \( E \to R \) and \( R \) no rule gives anything about \( E \); that was Section 1.4's affirming the consequent. So the green card must be turned and the red one need not be.

Modus tollens is the step people skip. \( \rulename{CP} \) turns the claim into its contrapositive \( \neg R \to \neg E \), "a card whose color is not red has an odd number", which carries the claim's content to the green card; Section 2.5 derives the passage back, so the two say the same. The converse \( R \to E \), "a red card has an even number", is a different claim, and the card rule never made it.

## How this rule looks in a mathematical proof

@thm-square-even-implies-even (Section 2.1) says that for an integer \( n \), if \( n^2 \) is even then \( n \) is even. Section 2.1 proved it by cases, with the odd case shown impossible and closed by \( \rulename{\bot E} \). Here is the same theorem argued as mathematicians usually write it, with the derived rules doing the work. We use the facts (E1)–(E3) of Section 2.1: every integer is even or odd; no integer is both; the square of an odd integer is odd.

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

Compare this with the twelve-line derivation after @thm-square-even-implies-even in Section 2.1. There, line 11 split on (E1) at once, and the odd case, lines 6–10, got \( T \) from (E3), built \( S \wedge T \), clashed with (E2), and closed by \( \rulename{\bot E} \). Here the same work is spread over named steps. The \( \rulename{\neg I} \) box on lines 5–7 does the clash with (E2), which there was lines 8–9. Lines 9 and 10, \( \rulename{CP} \) and \( \rulename{{\to}E} \), abbreviate a box that assumes \( O \), gets \( T \) by (E3), as line 7 did there, and clashes with line 8. Line 12, \( \rulename{DS} \), abbreviates a case split on the disjunction with the case \( O \) closed by \( \rulename{\bot E} \), as lines 5–11 did there. The short version reads the way people talk.

Notice also what the argument never does. It feels like "suppose not", and written out in full it does contain one: \( \rulename{CP} \) assumes that \( n \) is odd, reaches \( \bot \), and concludes that \( n \) is **not** odd. What it never does is assume that \( n \) is **not even** and conclude from a contradiction that \( n \) **is** even. Every negation in it is introduced; none is removed. The difference will matter in Section 2.5.

## Common errors

::: {.warning}
A derived rule may be used only **after** its sequent has been derived, and never inside its own derivation. A "derivation" of @prp-contrapositive that justifies one of its lines by \( \rulename{CP} \) proves nothing: it assumes what it sets out to show. Exercise C2 is an example, and Section 2.6 returns to the error in general.
:::

::: {.warning}
The converse of the contrapositive is a different sequent. \( \rulename{CP} \) passes from \( P \to Q \) to \( \neg Q \to \neg P \); it does not pass from \( \neg Q \to \neg P \) back to \( P \to Q \). Try it: in a box on \( P \) the goal is \( Q \), a letter with no negation, and the natural box, on \( \neg Q \), reaches \( \bot \) and so closes to \( \neg\neg Q \), not \( Q \). Section 2.5 derives the passage back with a new rule. That no derivation with the rules so far exists is true, but we state it without proof, and nothing depends on it.
:::

::: {.warning}
"Suppose \( x \ge 0 \)" inside a proof framed "Assume \( x^3 < 0 \); we show \( x < 0 \)" is **not** the contrapositive. It is a box on the negation of the goal \( x < 0 \), and closing such a box on the unnegated goal needs the rule of Section 2.5. The contrapositive route replaces the frame: prove "if \( x \ge 0 \), then \( x^3 \ge 0 \)", and \( \rulename{CP} \) turns it into "if \( x^3 < 0 \), then \( x < 0 \)", since \( x^3 < 0 \) and \( x < 0 \) are the exact negations of \( x^3 \ge 0 \) and \( x \ge 0 \).
:::

## What the rules sound like

Here are the rows of the rule, phrase, and Lean table for this section's derived rules. As before, the last column is for readers who use a proof assistant, and nothing depends on it.

| Rule | You write | Lean |
|------|--------------------------------------|------------------------|
| \( \rulename{MT} \) | "Since \( Q \) fails, so does \( P \)." | `mt h hnq` |
| \( \rulename{CP} \) | "We prove the contrapositive: suppose not \( Q \); … so not \( P \)." | `mt` |
| \( \rulename{DS} \) | "\( P \) is impossible, so \( Q \)." | `h.resolve_left hnp` |

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

### B. Practice

::: {#exr-derived-rules-b1}
[B1: The other disjunctive syllogism]

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
[B3]

Show that \( (P \vee Q) \to R, \; \neg R \vdash \neg P \wedge \neg Q \). You may use the derived rules of this section.
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

### C. Going deeper

::: {#exr-derived-rules-c1}
[C1: Two premises that cannot both fail]

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
prp-modus-tollens (claim): the motivating arguments: n even gives n^2 even; x >= 1 gives x^2 >= x >= 1; x^2 < 1 and x < 1 are the exact negations of x^2 >= 1 and x >= 1 | school algebra, shown inline; ch11 (promised)
prp-contrapositive (claim): no derivation of the converse with the rules so far exists | stated without proof and marked so; nothing depends on it
def-derived-rule (claim): pasting a derivation (repetitions, shifted line numbers) keeps every citation available; iterated expansion terminates | argued inline in the paragraph after the definition, from def-derivation's scope rule and (D3)
def-derived-rule (claim): letters of a derived sequent may be replaced uniformly by any statements | def-derivable and def-rule-schema (cited); made exact in ch03 (substitution, prose pointer)
exm-modus-tollens-instance (example): x > 2 implies x^2 > 4; x^2 <= 4 is the negation of x^2 > 4; x <= 2 is the negation of x > 2 | school algebra, shown inline
exm-modus-tollens-instance (example): (the green card) a card's color side has one color, so green is not red | stated in the paragraph; exm-wason-selection (cited)
exm-modus-tollens-instance (example): the passage from the contrapositive back to the claim | ch02 s05 prp-contrapositive-converse (prose pointer, later section of this chapter; nothing here depends on it)
exm-square-even-via-contrapositive (example): (E1)-(E3) and the parity computation | school facts stated in Section 2.1 (thm-square-even-implies-even)
exr-derived-rules-b1 (solution): -1 < 0; x^2 = 1 gives x = 1 or x = -1 | school algebra; the second is supplied by the item
exr-derived-rules-c3 (solution): (2k)^2 = 2(2k^2); (E1), (E2) | computation inline; facts of Section 2.1
-->
