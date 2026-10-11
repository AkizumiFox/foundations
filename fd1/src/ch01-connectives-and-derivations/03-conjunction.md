# Conjunction: the Rules for And

Section 1.2 set up the format of a derivation and practiced it on two toy rules about numbers, which the book now puts away. This section introduces the first two rules of logic, one for proving a statement of the form "\( P \) and \( Q \)" and one for using it. Both are defined by their schemas, in the sense of @def-rule-schema, and every derivation below is checked against those schemas and nothing else. The rules are so simple that we can spend the section on something harder: how to *find* a derivation. Two questions will organize every search in Part 0, and they appear here for the first time: what does the goal ask for, and what do the lines we already have allow?

## A conjunction in disguise

Much of analysis is written in chains such as \( 0 < x < 1 \). As Section 1.1 observed, the chain is a conjunction in disguise: it says \( 0 < x \) **and** \( x < 1 \), that is, \( (0 < x) \wedge (x < 1) \). Watch what proofs do with it.

A proof that **uses** \( 0 < x < 1 \) usually needs only one half at a time. "Since \( 0 < x < 1 \), in particular \( x > 0 \), so we may divide by \( x \)." The proof takes the conjunction apart and keeps the piece it wants.

A proof that **proves** \( 0 < x < 1 \) must prove both halves. It shows \( 0 < x \), then shows \( x < 1 \), and then writes "hence \( 0 < x < 1 \)". Nothing else will do: one half is not the whole claim.

Section 1.1 previewed these two moves in a table, informally. Here they become rules, stated as patterns of lines, so that a derivation using them can be checked by matching, exactly as Tr was matched in Section 1.2.

## The two rules

Recall from @def-rule-schema that a schema has given lines at the top and exactly one new line at the bottom, whose justification names the rule and cites the given lines. From this section on, the letters in a schema are the Greek letters \( \varphi \) ("phi"), \( \psi \) ("psi") and \( \chi \) ("chi"), and each stands for an arbitrary statement. A use of the rule replaces each Greek letter by one statement, the same statement everywhere the letter occurs.

*To prove "\( \varphi \) and \( \psi \)", prove each; to use it, take either.*

::: {#def-rules-conjunction}
[Rules for Conjunction]

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {i} {\varphi}
  \have {j} {\psi}
  \have {k} {\varphi \wedge \psi} \ai{i,j}
\end{nd}$
\qquad
$\begin{nd}[schema]
  \have {i} {\varphi \wedge \psi}
  \have {k} {\varphi} \ae{i}
\end{nd}$
\qquad
$\begin{nd}[schema]
  \have {i} {\varphi \wedge \psi}
  \have {k} {\psi} \ae{i}
\end{nd}$
\end{center}
```

The first schema is the rule \( \rulename{\wedge I} \) (**and-introduction**). The second and third are the two forms of the rule \( \rulename{\wedge E} \) (**and-elimination**), one writing the left conjunct and one the right.
:::

Read the schemas clause by clause.

**\( \rulename{\wedge I} \), the given lines.** Two lines, \( \varphi \) and \( \psi \), must stand earlier in the derivation. They may be anywhere above line \( k \), in either order, with other lines between them; the schema draws them next to each other only to save space.

**\( \rulename{\wedge I} \), the order of the citation.** The justification "\( \rulename{\wedge I} \) \( i, j \)" puts the statement of line \( i \) on the **left** of the new conjunction and the statement of line \( j \) on the right. So the citation, not the position of the lines, decides the order of the conjuncts: if line 3 is \( Q \) and line 2 is \( P \), then "\( \rulename{\wedge I} \) 3, 2" writes \( Q \wedge P \), and "\( \rulename{\wedge I} \) 2, 3" writes \( P \wedge Q \).

**\( \rulename{\wedge I} \), the degenerate case.** Nothing says that \( i \) and \( j \) are different lines. With \( i = j \), the letters \( \varphi \) and \( \psi \) are replaced by the same statement, and the rule writes \( \varphi \wedge \varphi \). It is a silly line, and a legal one.

**\( \rulename{\wedge E} \), one conjunction, either conjunct.** One given line, whose statement is a conjunction \( \varphi \wedge \psi \). The rule writes one conjunct per application: to get both halves, apply it twice, on two lines, each citing the same conjunction. That is why the rule has two schemas and not one schema with two new lines.

**\( \rulename{\wedge E} \) looks only at the main connective.** To apply \( \rulename{\wedge E} \) to a line, we must see the line's statement as \( \varphi \wedge \psi \), and that means its main connective (@def-main-connective) must be \( \wedge \). The two conjuncts are then the two parts that this \( \wedge \) joins, and nothing smaller. Take \( (P \wedge Q) \wedge R \). Its main connective is the second \( \wedge \), so the replacement is
\[
\varphi \coloneqq P \wedge Q, \qquad \psi \coloneqq R ,
\]
and one application of \( \rulename{\wedge E} \) writes \( P \wedge Q \) or \( R \). It does not write \( P \), and it does not write \( Q \). Getting to \( Q \) takes a second application, to the new line \( P \wedge Q \).

**What the rules do not say.** They say nothing about what \( \varphi \) and \( \psi \) mean. A line is justified by \( \rulename{\wedge I} \) or \( \rulename{\wedge E} \) when it and the lines it cites are an **instance** of a schema (@def-rule-schema), and that can be seen by looking at symbols.

::: {.warning}
\( \rulename{\wedge E} \) reaches one layer at a time. From line 1, \( (P \wedge Q) \wedge R \), the line "\( Q \) — \( \rulename{\wedge E} \) 1" is not an instance of either \( \rulename{\wedge E} \) schema, because line 1's conjuncts are \( P \wedge Q \) and \( R \). The line is wrong as a justification even though \( Q \) does follow; the repair costs one line, \( P \wedge Q \) by \( \rulename{\wedge E} \) 1 first, then \( Q \) from it.
:::

::: {.check}
Which statements can \( \rulename{\wedge E} \) write, in one application each, from the line \( (P \wedge Q) \wedge (R \wedge S) \)?
:::

::: {.solution}
Only \( P \wedge Q \) and \( R \wedge S \). The main connective is the middle \( \wedge \), so \( \varphi \) is \( P \wedge Q \) and \( \psi \) is \( R \wedge S \). Each of \( P, Q, R, S \) needs a second application, to one of those two lines.
:::

::: {.check}
Line 2 is \( P \wedge Q \) and line 5 is \( R \). Which line does "\( \rulename{\wedge I} \) 5, 2" justify, and which does "\( \rulename{\wedge I} \) 2, 5" justify?
:::

::: {.solution}
"\( \rulename{\wedge I} \) 5, 2" justifies \( R \wedge (P \wedge Q) \), and "\( \rulename{\wedge I} \) 2, 5" justifies \( (P \wedge Q) \wedge R \). The first line cited becomes the left conjunct, and a compound statement placed inside a conjunction keeps its brackets.
:::

**Why these rules.** They are exactly the two moves of the opening paragraph, "prove both" and "use either", and nothing more. Section 1.1's slogan said that each connective comes with a way to prove it and a way to use it; for \( \wedge \), the way to prove it is \( \rulename{\wedge I} \) and the way to use it is \( \rulename{\wedge E} \).

**Why they are safe.** If the given lines are true statements, so is the new line: if \( \varphi \) and \( \psi \) are both true, so is \( \varphi \wedge \psi \), and if \( \varphi \wedge \psi \) is true, so is each conjunct. Chapter 3 proves this property for every rule of the calculus at once, and calls it soundness (@thm-soundness).

## Two directions of reasoning

A derivation has premises at the top and its goal, the conclusion we want, at the bottom. Between them is a gap, and finding a derivation means filling the gap. There are two places to start.

*From the goal.* Ask: **what is the goal's main connective?** If it is \( \wedge \), the last line can be written by \( \rulename{\wedge I} \), and then the goal \( \varphi \wedge \psi \) splits into two **subgoals**, \( \varphi \) and \( \psi \), each to be reached on some line above. This is **goal-directed** reasoning. It works backwards, from the bottom of the gap upwards, and its first question is which **introduction** rule builds the goal's main connective.

*From the premises.* Ask: **what are the main connectives of the lines we already have?** A line whose main connective is \( \wedge \) can be taken apart by \( \rulename{\wedge E} \), and each conjunct becomes a new line to work with. This is **premise-directed** reasoning. It works forwards, from the top of the gap downwards, and its first question is which **elimination** rule uses the line's main connective.

*Work from both ends: take the premises apart, and build the goal from its parts.*

The derivation is finished when the two ends meet: when every subgoal read off the goal is a line obtained from the premises. Section 1.2 already found one derivation backwards, from the goal \( u < z \) of part (c) of @exm-chaining-derivation; the toy rule Tr played the part that introduction rules play from now on. Each later section of this chapter adds one rule to one of the two lists (an introduction rule to the goal-directed list, an elimination rule to the premise-directed one), and Section 2.6 collects the lists into a method.

## First derivations

In each example below, the Idea says, for each line, whether it was found from the goal or from a premise.

::: {#exm-conjunction-warm-ups}
[Three warm-ups]

Give a derivation of each sequent.

::: {.enumerate options="label=(\alph*)"}
1. \( P, \ Q \vdash Q \wedge P \).
2. \( P \vdash P \wedge P \).
3. \( P \wedge Q \vdash Q \).
:::
:::

::: {.solution}
(a) *Idea.* The goal \( Q \wedge P \) has main connective \( \wedge \), so, goal-directed, its last line is \( \rulename{\wedge I} \) with subgoals \( Q \) and \( P \). Both subgoals are premises, so the two ends meet at once.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \hypo {2} {Q}
  \have {3} {Q \wedge P} \ai{2,1}
\end{nd}$
\end{center}
```

The citation is "2, 1", because \( Q \), on line 2, must be the left conjunct. Written "\( \rulename{\wedge I} \) 1, 2", the line would have to be \( P \wedge Q \).

(b) *Idea.* The goal is again a conjunction, so \( \rulename{\wedge I} \), with the subgoals \( P \) and \( P \). One premise meets both.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \have {2} {P \wedge P} \ai{1,1}
\end{nd}$
\end{center}
```

This is the degenerate case \( i = j \) of \( \rulename{\wedge I} \).

(c) *Idea.* The goal \( Q \) is a letter, with no main connective, so the goal suggests no rule. The premise has main connective \( \wedge \), so, premise-directed, take it apart; its right conjunct is the goal.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge Q}
  \have {2} {Q} \ae{1}
\end{nd}$
\end{center}
```

Line 2 is the second form of \( \rulename{\wedge E} \), with \( \varphi \coloneqq P \) and \( \psi \coloneqq Q \).
:::

The three derivations are box-free derivations in the sense of @def-box-free-derivation, with \( \rulename{\wedge I} \) and \( \rulename{\wedge E} \) as the list of rules: premises first, and every later line an instance of a schema whose given lines are earlier. By @def-derivable they show the three sequents. When the goal is a letter, as in (c), only the premises can suggest a step. When every subgoal is a premise, as in (a) and (b), the premises need no taking apart. The next derivation needs both ends.

The first result is that the order of a conjunction does not matter.

::: {#prp-and-commutes}
[Conjunction Commutes]

\( P \wedge Q \vdash Q \wedge P \).
:::

::: {.idea}
Write the premise at the top, the goal at the bottom, and leave a gap (left picture; the lines carry the numbers they will have at the end). Start from the goal. Its main connective is \( \wedge \), so the last line will be \( \rulename{\wedge I} \), and we need \( P \) and \( Q \) on earlier lines (right picture: two subgoals, not yet justified). Now start from the premise. Its main connective is \( \wedge \), so \( \rulename{\wedge E} \) gives \( P \) and gives \( Q \). That closes the gap: the pieces the goal asks for are the pieces the premise supplies.

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge Q}
  \have[\ ][0] {} {\vdots}
  \have[][4] {4} {Q \wedge P}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {P \wedge Q}
  \have[\ ][0] {} {\vdots}
  \have[][2] {2} {P}
  \have {3} {Q}
  \have {4} {Q \wedge P} \ai{3,2}
\end{nd}$
\end{center}
```
:::

::: {.proof}
The following is a box-free derivation with the single premise \( P \wedge Q \) and last line \( Q \wedge P \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge Q}
  \have {2} {P} \ae{1}
  \have {3} {Q} \ae{1}
  \have {4} {Q \wedge P} \ai{3,2}
\end{nd}$
\end{center}
```

Lines 2 and 3 are the two forms of \( \rulename{\wedge E} \) applied to line 1, and line 4 is \( \rulename{\wedge I} \) applied to lines 3 and 2, in that order, so line 3 becomes the left half. By @def-derivable, \( P \wedge Q \vdash Q \wedge P \).
:::

Read back in words, the derivation is a short paragraph: *We are given that \( P \) and \( Q \). In particular \( P \) holds, and in particular \( Q \) holds. So \( Q \) and \( P \) both hold.* Each sentence is one line, and each "in particular" is one application of \( \rulename{\wedge E} \).

Nothing in the derivation looks at what \( P \) and \( Q \) say. With \( P \): "\( 0 < x \)" and \( Q \): "\( x < 1 \)" it turns "\( 0 < x \) and \( x < 1 \)" into "\( x < 1 \) and \( 0 < x \)"; with any other two statements it does the same. Because the letters stand for arbitrary statements, one derivation written with letters proves every such instance at once.

The second result is that the grouping of a conjunction does not matter either. It needs the premise taken apart in two layers.

::: {#prp-and-associative}
[Conjunction Is Associative]

\( (P \wedge Q) \wedge R \vdash P \wedge (Q \wedge R) \).
:::

::: {.idea}
From the goal: its main connective is the **outer** \( \wedge \), so the last line is \( \rulename{\wedge I} \) with the subgoals \( P \) and \( Q \wedge R \). The second subgoal is itself a conjunction, so it is again \( \rulename{\wedge I} \), with the subgoals \( Q \) and \( R \). The goal-directed search stops at the letters \( P \), \( Q \), \( R \).

From the premise: its main connective is also an outer \( \wedge \), so \( \rulename{\wedge E} \) gives \( P \wedge Q \) and \( R \). The line \( P \wedge Q \) is a conjunction, so \( \rulename{\wedge E} \) again gives \( P \) and \( Q \). The premise-directed search also stops at the three letters, and the ends meet there. Since \( \rulename{\wedge E} \) reaches one layer at a time, the premise must be peeled in two rounds.
:::

::: {.proof}
The following is a box-free derivation with the single premise \( (P \wedge Q) \wedge R \) and last line \( P \wedge (Q \wedge R) \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge Q) \wedge R}
  \have {2} {P \wedge Q} \ae{1}
  \have {3} {R} \ae{1}
  \have {4} {P} \ae{2}
  \have {5} {Q} \ae{2}
  \have {6} {Q \wedge R} \ai{5,3}
  \have {7} {P \wedge (Q \wedge R)} \ai{4,6}
\end{nd}$
\end{center}
```

Lines 2 and 3 apply \( \rulename{\wedge E} \) to line 1, with \( \varphi \coloneqq P \wedge Q \) and \( \psi \coloneqq R \). Lines 4 and 5 apply \( \rulename{\wedge E} \) to line 2, with \( \varphi \coloneqq P \) and \( \psi \coloneqq Q \). Line 6 applies \( \rulename{\wedge I} \) to lines 5 and 3, and line 7 applies \( \rulename{\wedge I} \) to lines 4 and 6, with \( \varphi \coloneqq P \) and \( \psi \coloneqq Q \wedge R \). By @def-derivable, \( (P \wedge Q) \wedge R \vdash P \wedge (Q \wedge R) \).
:::

The lines could come in other orders. Line 3 could come after lines 4 and 5, for instance, since it is used only at line 6. What cannot move is the dependence: every line must come after each line it cites.

::: {.remark}
The converse, \( P \wedge (Q \wedge R) \vdash (P \wedge Q) \wedge R \), is derived the same way, peeling the premise's inner conjunction on the right instead of the left; Exercise B1 asks you to write it out. With both directions, the brackets in a chain of conjunctions carry no information, which is why the chain \( 0 < x < 1 < y \) is written without any.
:::

### A line is not used up

A line of a derivation is a statement that has been established. Citing it does not consume it: it can be cited again, by as many later lines as need it. The derivation of \( P \wedge Q, \ R \vdash (P \wedge R) \wedge (Q \wedge R) \) shows this.

::: {.idea}
From the goal: \( \rulename{\wedge I} \) at the bottom, with subgoals \( P \wedge R \) and \( Q \wedge R \); each is a conjunction, so \( \rulename{\wedge I} \) again, with subgoals \( P \), \( R \) and \( Q \), \( R \). From the premises: \( \rulename{\wedge E} \) on line 1 gives \( P \) and \( Q \), and \( R \) is already a premise. Both subgoals that need \( R \) cite the same line 2.
:::

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge Q}
  \hypo {2} {R}
  \have {3} {P} \ae{1}
  \have {4} {Q} \ae{1}
  \have {5} {P \wedge R} \ai{3,2}
  \have {6} {Q \wedge R} \ai{4,2}
  \have {7} {(P \wedge R) \wedge (Q \wedge R)} \ai{5,6}
\end{nd}$
\end{center}
```

Line 2 is cited by lines 5 and 6, and line 1 by lines 3 and 4. In a written proof this is the everyday "we use the hypothesis \( x > 0 \) again".

### Take everything apart, rebuild in the new order

The last derivation of the section rearranges four letters: \( (P \wedge Q) \wedge (R \wedge S) \vdash (S \wedge Q) \wedge (P \wedge R) \).

::: {.idea}
From the premise: two layers of \( \wedge \), so \( \rulename{\wedge E} \) twice on line 1 and then twice on each of the two new lines, which leaves the four letters on lines 4 to 7. From the goal: two layers of \( \wedge \), so \( \rulename{\wedge I} \) builds \( S \wedge Q \) and \( P \wedge R \) from the letters and then joins them. There is nothing to choose; the only care needed is the order of each citation.
:::

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge Q) \wedge (R \wedge S)}
  \have {2} {P \wedge Q} \ae{1}
  \have {3} {R \wedge S} \ae{1}
  \have {4} {P} \ae{2}
  \have {5} {Q} \ae{2}
  \have {6} {R} \ae{3}
  \have {7} {S} \ae{3}
  \have {8} {S \wedge Q} \ai{7,5}
  \have {9} {P \wedge R} \ai{4,6}
  \have {10} {(S \wedge Q) \wedge (P \wedge R)} \ai{8,9}
\end{nd}$
\end{center}
```

The recipe visibly does not depend on these particular letters or brackets. Take the premise apart with \( \rulename{\wedge E} \) until only letters remain, then build the goal from the letters with \( \rulename{\wedge I} \), inside out. It works whenever the premise and the goal are both built from letters by \( \wedge \) alone and every letter of the goal occurs in the premise, whatever the bracketing and the order on either side. So "\( \wedge \) is commutative and associative" is, in the end, the observation that \( \rulename{\wedge E} \) can always take a conjunction down to its letters and \( \rulename{\wedge I} \) can always build one back up. (Chapter 3's completeness theorem, @thm-completeness, gives another reason, from the truth tables.)

## How this looks in a mathematical proof

Real proofs mix the logical rules with facts about their subject. The rules supply the joints; the facts supply the content.

::: {#exm-product-in-unit-interval}
[A product of numbers in the unit interval]

Let \( x \) and \( y \) be real numbers with \( 0 < x < 1 \) and \( 0 < y < 1 \). Show that \( 0 < xy < 1 \), and name the rule behind each logical step.
:::

::: {.solution}
The hypothesis \( 0 < x < 1 \) is the conjunction \( (0 < x) \wedge (x < 1) \). By \( \rulename{\wedge E} \) we have \( 0 < x \) and \( x < 1 \) separately, and likewise \( 0 < y \) and \( y < 1 \).

Since \( x > 0 \) and \( y > 0 \), the product \( xy \) is positive. Since \( y < 1 \) and \( x > 0 \), multiplying by \( x \) gives \( xy < x \); together with \( x < 1 \) this gives \( xy < 1 \). These steps are school algebra, not logic.

Finally, from \( 0 < xy \) and \( xy < 1 \), \( \rulename{\wedge I} \) gives \( (0 < xy) \wedge (xy < 1) \), which is \( 0 < xy < 1 \).

As a derivation, the same proof reads as follows.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(0 < x) \wedge (x < 1)}
  \hypo {2} {(0 < y) \wedge (y < 1)}
  \have {3} {0 < x} \ae{1}
  \have {4} {x < 1} \ae{1}
  \have {5} {0 < y} \ae{2}
  \have {6} {y < 1} \ae{2}
  \have {7} {0 < xy} \by{algebra}{3,5}
  \have {8} {xy < 1} \by{algebra}{3,4,6}
  \have {9} {(0 < xy) \wedge (xy < 1)} \ai{7,8}
\end{nd}$
\end{center}
```

Lines 7 and 8 are justified "algebra": each is a step by a fact about numbers used as a rule, exactly as Tr was used in Section 1.2, and not a rule of logic. Line 7 uses "a product of two positive numbers is positive"; line 8 uses "multiplying an inequality by a positive number keeps its direction", then the pattern of Tr.
:::

The facts about numbers supply the content of the solution; the rules supply the joints, taking statements apart and putting the pieces back together. The goal-directed reading is visible in the prose too: "show \( 0 < xy < 1 \)" is a conjunction, so the solution sets itself two subgoals, and it says "finally" when the two meet.

## Common errors

The warning above covered \( \rulename{\wedge E} \) applied through a layer. Two more errors are common.

::: {.warning}
\( \rulename{\wedge E} \) applies only to a line whose **main connective** is \( \wedge \). The line \( (P \wedge Q) \to R \) contains a \( \wedge \), but its main connective is \( \to \), so "\( P \) — \( \rulename{\wedge E} \) 1" is illegal. With \( x \) a real number, \( P \): "\( x > 0 \)", \( Q \): "\( x > 1 \)" and \( R \): "\( x^2 > 1 \)", the premise "if \( x > 0 \) and \( x > 1 \), then \( x^2 > 1 \)" is true for every \( x \), yet at \( x = -1 \) the line \( x > 0 \) is false.
:::

```{=latex}
\begin{center}
% expect-invalid: a deliberately flawed derivation (and-E applied to an implication)
$\begin{nd}
  \hypo {1} {(P \wedge Q) \to R}
  \have {2} {P} \ae{1}
\end{nd}$
\end{center}
```

The illegal step leads from a true premise to a false line, so no rule that allowed it could be safe.

The third error is a mismatch between the citation and the line. Suppose line 3 is \( Q \) and line 2 is \( P \), and someone writes "\( P \wedge Q \) — \( \rulename{\wedge I} \) 3, 2". The statement \( P \wedge Q \) is fine, and it does follow from lines 2 and 3. But "\( \rulename{\wedge I} \) 3, 2" names line 3 as the left conjunct, so the line it justifies is \( Q \wedge P \). A checker compares the line with the citation and rejects it; the repair is to write "2, 3". This looks pedantic, and it is the point: a justification that says something false about the line it justifies cannot be checked by matching, and then nothing can be checked by matching.

## What the rules sound like

Every rule is something mathematicians already say. The table pairs each rule of this section with the sentence that uses it in a written proof and, for readers who meet a proof assistant, with the Lean code that performs it (`h.1` names the left half of a hypothesis `h`). Nothing later depends on the last column.

| Rule | You write | Lean |
|------|--------------------------------------|------------------------|
| \( \rulename{\wedge I} \) | "We show \( P \), and we show \( Q \)." | `constructor` |
| \( \rulename{\wedge E} \) | "In particular, \( P \)." | `h.1` (and `h.2`) |

Section 1.4 adds the first rule for "implies", and the table grows with each new rule.

## Exercises

### A. Check your understanding

::: {#exr-conjunction-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Write the three schemas of @def-rules-conjunction from memory, and name the rule of each.
2. Which statements does one application of \( \rulename{\wedge E} \) give from the line \( P \wedge (Q \wedge R) \)?
3. True or false, with a reason: \( \rulename{\wedge E} \) may be applied to the line \( P \wedge Q \to R \).
4. In the derivation in the proof of @prp-and-associative, why must line 2 come before line 4?
5. Fill in the justifications (i)–(iv) of the following derivation.

   ```{=latex}
   \begin{center}
   $\begin{nd}
     \hypo {1} {P \wedge (Q \wedge R)}
     \have {2} {P} \by{(i)}{}
     \have {3} {Q \wedge R} \by{(ii)}{}
     \have {4} {R} \by{(iii)}{}
     \have {5} {R \wedge P} \by{(iv)}{}
   \end{nd}$
   \end{center}
   ```
:::
:::

::: {.solution}
(a) See @def-rules-conjunction: \( \rulename{\wedge I} \) has given lines \( i \): \( \varphi \) and \( j \): \( \psi \) and new line \( k \): \( \varphi \wedge \psi \), cited "\( \rulename{\wedge I} \) \( i, j \)"; the two forms of \( \rulename{\wedge E} \) each have the given line \( i \): \( \varphi \wedge \psi \) and the new line \( k \): \( \varphi \), respectively \( \psi \), cited "\( \rulename{\wedge E} \) \( i \)".

(b) \( P \), or \( Q \wedge R \). The main connective is the first \( \wedge \), so \( \varphi \) is \( P \) and \( \psi \) is \( Q \wedge R \).

(c) False. By the conventions of Section 1.1, \( \wedge \) binds more tightly than \( \to \), so the line is \( (P \wedge Q) \to R \), whose main connective is \( \to \). It is not of the form \( \varphi \wedge \psi \).

(d) Line 4 is \( P \), obtained by \( \rulename{\wedge E} \) from line 2, \( P \wedge Q \). A rule may cite only earlier lines (@def-box-free-derivation), and \( P \) cannot be obtained from line 1 in one step, since line 1's conjuncts are \( P \wedge Q \) and \( R \).

(e) (i) \( \rulename{\wedge E} \) 1; (ii) \( \rulename{\wedge E} \) 1; (iii) \( \rulename{\wedge E} \) 3; (iv) \( \rulename{\wedge I} \) 4, 2.
:::

### B. Practice

::: {#exr-conjunction-b1}
[B1: The other grouping]

Give a derivation of \( P \wedge (Q \wedge R) \vdash (P \wedge Q) \wedge R \). For each line, say whether you found it from the goal or from the premise.
:::

::: {.solution}
From the goal: \( \rulename{\wedge I} \) with subgoals \( P \wedge Q \) and \( R \), and \( P \wedge Q \) by \( \rulename{\wedge I} \) from \( P \) and \( Q \). From the premise: \( \rulename{\wedge E} \) gives \( P \) and \( Q \wedge R \), and \( \rulename{\wedge E} \) on \( Q \wedge R \) gives \( Q \) and \( R \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge (Q \wedge R)}
  \have {2} {P} \ae{1}
  \have {3} {Q \wedge R} \ae{1}
  \have {4} {Q} \ae{3}
  \have {5} {R} \ae{3}
  \have {6} {P \wedge Q} \ai{2,4}
  \have {7} {(P \wedge Q) \wedge R} \ai{6,5}
\end{nd}$
\end{center}
```

Lines 2–5 were found from the premise, lines 6–7 from the goal. With @prp-and-associative, each of \( (P \wedge Q) \wedge R \) and \( P \wedge (Q \wedge R) \) is derivable from the other.
:::

::: {#exr-conjunction-b2}
[B2: Annotating a proof]

Let \( x \) and \( y \) be real numbers. Here is a proof.

> Let \( 1 < x < 2 \) and \( 3 < y < 4 \). Then \( 4 < x + y < 6 \).

Write out the proof in full, naming each use of \( \rulename{\wedge E} \) and \( \rulename{\wedge I} \), and marking the steps that are school algebra rather than logic.
:::

::: {.solution}
The hypotheses are the conjunctions \( (1 < x) \wedge (x < 2) \) and \( (3 < y) \wedge (y < 4) \), and the goal is \( (4 < x + y) \wedge (x + y < 6) \).

By \( \rulename{\wedge E} \), four times, we have \( 1 < x \), \( x < 2 \), \( 3 < y \), and \( y < 4 \) separately. Adding \( 1 < x \) and \( 3 < y \) gives \( 1 + 3 < x + y \), that is, \( 4 < x + y \) (school algebra: two inequalities in the same direction may be added). Adding \( x < 2 \) and \( y < 4 \) gives \( x + y < 6 \) (school algebra again). Finally \( \rulename{\wedge I} \) joins \( 4 < x + y \) and \( x + y < 6 \) into \( 4 < x + y < 6 \).

As a derivation it has the same shape as the one in @exm-product-in-unit-interval: two premises, four \( \rulename{\wedge E} \) lines, two lines justified "algebra", and one \( \rulename{\wedge I} \) line.
:::

::: {#exr-conjunction-b3}
[B3: Which lines are instances?]

A derivation begins as follows.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge (Q \wedge R)}
  \hypo {2} {S}
  \have {3} {Q \wedge R} \ae{1}
\end{nd}$
\end{center}
```

Determine which of the following candidates for line 4 are correct. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( P \) — \( \rulename{\wedge E} \) 1.
2. \( R \) — \( \rulename{\wedge E} \) 1.
3. \( (Q \wedge R) \wedge S \) — \( \rulename{\wedge I} \) 3, 2.
4. \( S \wedge (Q \wedge R) \) — \( \rulename{\wedge I} \) 3, 2.
5. \( Q \) — \( \rulename{\wedge E} \) 3.
:::
:::

::: {.solution}
(a) Correct: the first form of \( \rulename{\wedge E} \) with \( \varphi \coloneqq P \) and \( \psi \coloneqq Q \wedge R \).

(b) Incorrect. Line 1's conjuncts are \( P \) and \( Q \wedge R \); \( R \) lies one layer deeper. "\( R \) — \( \rulename{\wedge E} \) 3" would be correct.

(c) Correct: \( \rulename{\wedge I} \) with line 3 on the left and line 2 on the right, \( \varphi \coloneqq Q \wedge R \) and \( \psi \coloneqq S \).

(d) Incorrect. The citation "3, 2" puts line 3 on the left, so it justifies \( (Q \wedge R) \wedge S \), not \( S \wedge (Q \wedge R) \). "\( \rulename{\wedge I} \) 2, 3" would be correct.

(e) Correct: the first form of \( \rulename{\wedge E} \) with \( \varphi \coloneqq Q \) and \( \psi \coloneqq R \).
:::

### C. Going deeper

::: {#exr-conjunction-c1}
[C1: What conjunction cannot do]

Show that no box-free derivation whose only premise is \( P \wedge Q \), and whose only rules are \( \rulename{\wedge I} \) and \( \rulename{\wedge E} \), has a line whose statement contains the letter \( R \). Deduce that, with these two rules, \( P \wedge Q \vdash P \wedge R \) cannot be shown.
:::

::: {.solution}
[Hint 1]

Suppose some line does contain \( R \), and look at the **first** such line.
:::

::: {.solution}
[Hint 2]

That first line is not a premise. Which rule wrote it, and which letters can that rule write?
:::

::: {.solution}
Suppose, for a contradiction, that some line of such a derivation contains \( R \). The derivation has finitely many lines, so there is a first such line; call it line \( k \). Every line before line \( k \) is free of \( R \).

Line \( k \) is not a premise, because every premise is \( P \wedge Q \), which does not contain \( R \). So line \( k \) is justified by one of the two rules, citing earlier lines (@def-box-free-derivation).

If it is \( \rulename{\wedge I} \), citing lines \( i \) and \( j \), then its statement is \( \varphi \wedge \psi \), where \( \varphi \) and \( \psi \) are the statements of lines \( i \) and \( j \). Both are earlier than \( k \), so neither contains \( R \), and neither does \( \varphi \wedge \psi \).

If it is \( \rulename{\wedge E} \), citing line \( i \), then its statement is one conjunct of the statement of line \( i \): a part of it. Line \( i \) is earlier than \( k \) and free of \( R \), so the part is free of \( R \) too.

Either way line \( k \) does not contain \( R \), which contradicts the choice of \( k \). So no line contains \( R \). In particular no such derivation has the last line \( P \wedge R \), and \( P \wedge Q \vdash P \wedge R \) cannot be shown with these rules.

The argument, "look at the first bad line; it cannot be a premise, and no rule can create it from good lines", is an argument by induction on the lines of a derivation. Chapter 3 makes such arguments exact (@thm-strong-induction); the proof of @thm-soundness is one.

**Marking scheme.** (10 points)

- 2: considers a first line containing \( R \), and says why a first one exists (finitely many lines); or, equally, goes down the derivation line by line, showing each line free of \( R \) because every line it cites is.
- 2: rules out a premise.
- 2: \( \rulename{\wedge I} \) case: the new line is built from the statements of two earlier, \( R \)-free lines.
- 2: \( \rulename{\wedge E} \) case: the new line is part of an earlier, \( R \)-free line.
- 2: concludes that no line contains \( R \), and so that \( P \wedge R \) is never a last line.

Fatal errors (0 for the step): arguing about one particular derivation instead of every derivation; arguing that \( R \) is "not true" instead of about which symbols the rules can write.
:::

::: {#exr-conjunction-c2}
[C2: A shortcut through two layers]

A student offers the following derivation of \( P \wedge (Q \wedge R) \vdash Q \wedge P \).

```{=latex}
\begin{center}
% expect-invalid: a deliberately flawed derivation (and-E through two layers)
$\begin{nd}
  \hypo {1} {P \wedge (Q \wedge R)}
  \have {2} {Q} \ae{1}
  \have {3} {P} \ae{1}
  \have {4} {Q \wedge P} \ai{2,3}
\end{nd}$
\end{center}
```

::: {.enumerate options="label=(\alph*)"}
1. Is line 2 an instance of a schema of \( \rulename{\wedge E} \)? Justify your answer.
2. Is the conclusion derivable from the premise? Justify your answer.
3. The step at line 2 never leads from a true line to a false one. Why must a checker still reject it?
4. State, as a schema, a rule \( \wedge\mathrm{E}^{*} \) that would allow line 2. Show that every use of \( \wedge\mathrm{E}^{*} \) in a derivation can be replaced by two uses of \( \rulename{\wedge E} \).
:::
:::

::: {.solution}
(a) No. To match line 1 with \( \varphi \wedge \psi \), we must read \( \varphi \) and \( \psi \) off line 1's main connective, which is the first \( \wedge \): \( \varphi \) is \( P \) and \( \psi \) is \( Q \wedge R \). So \( \rulename{\wedge E} \) writes \( P \) or \( Q \wedge R \), and \( Q \) is neither.

(b) Yes. Insert the missing layer.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge (Q \wedge R)}
  \have {2} {P} \ae{1}
  \have {3} {Q \wedge R} \ae{1}
  \have {4} {Q} \ae{3}
  \have {5} {Q \wedge P} \ai{4,2}
\end{nd}$
\end{center}
```

(c) A derivation is checked by matching each line against the schemas of the rules on the list, and line 2 matches none. A checker that also accepted steps that "obviously follow" would need to understand the statements, and then its verdict would be only as reliable as that understanding. The steps that seem obvious are the ones nobody looks at twice, and they are where unnoticed errors live. (This item is not a find-the-error exercise in the usual sense: the step has no counterexample, since it never leads from truth to falsehood. It is simply not a step of this calculus.)

(d) One such rule, in schema form:

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {i} {\varphi \wedge (\psi \wedge \chi)}
  \have {k} {\psi} \by{$\wedge$E$^{*}$}{i}
\end{nd}$
\end{center}
```

Suppose line \( k \) of a derivation is \( \psi \), justified "\( \wedge\mathrm{E}^{*} \) \( i \)", with line \( i \) the statement \( \varphi \wedge (\psi \wedge \chi) \). Replace line \( k \) by two lines: first \( \psi \wedge \chi \), justified \( \rulename{\wedge E} \) \( i \) (the second form, with the conjuncts \( \varphi \) and \( \psi \wedge \chi \)), then \( \psi \), justified by \( \rulename{\wedge E} \) citing that new line (the first form, with the conjuncts \( \psi \) and \( \chi \)). Renumber the later lines, and every citation of them, up by one; a later citation of line \( k \) now cites the second new line, which carries the same statement \( \psi \). Every other line is unchanged and still cites earlier lines. Doing this for each \( \wedge\mathrm{E}^{*} \) line, one at a time, gives a derivation with the same premises and last line that uses only \( \rulename{\wedge E} \) and \( \rulename{\wedge I} \). A rule that can always be replaced in this way adds convenience and no new power; Section 2.3 calls such a rule a derived rule.

**Marking scheme.** (10 points)

- 2: (a) no, reading \( \varphi \) and \( \psi \) off the main connective of line 1.
- 2: (b) yes, with a correct derivation.
- 2: (c) checking is by matching the schemas; a step that is not an instance is rejected, whether or not it is true.
- 2: (d) a correct schema, one given line and one new line.
- 2: (d) the replacement by two \( \rulename{\wedge E} \) lines, with the renumbering of later citations.

Fatal errors (0 for the step): claiming the conclusion is not derivable; offering a counterexample to line 2.
:::

<!-- dependency ledger
exm-product-in-unit-interval (solution): a product of two positive reals is positive; multiplying an inequality by a positive number keeps its direction; transitivity of < | school algebra (blueprint, Allowed prerequisites) -> ch11 (promised); checked by verify/ch01/exm-product-in-unit-interval.py
def-rules-conjunction (example): the Common-errors warning's instance: (x > 0 and x > 1) implies x^2 > 1 for every real x, and x > 0 fails at x = -1 | school algebra -> ch11 (promised); checked by verify/ch01/exm-product-in-unit-interval.py
exr-conjunction-b2 (solution): two inequalities in the same direction may be added | school algebra -> ch11 (promised); checked by verify/ch01/exm-product-in-unit-interval.py
exr-conjunction-a1 (solution): the precedence convention (and binds more tightly than implies) | Section 1.1 (the four conventions, before def-main-connective), recalled in prose
exr-conjunction-c1 (solution): a finite non-empty set of line numbers has a first element (least-number principle, "first bad line") | school fact about finite lists; induction (ch03) named in prose as the exact version, not used
-->
