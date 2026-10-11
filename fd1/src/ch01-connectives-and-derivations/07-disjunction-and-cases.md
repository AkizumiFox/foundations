# Using Or: Proof by Cases

The previous section met a goal the rules could not reach: from \( P \vee Q \), derive \( Q \vee P \). The rules could build a disjunction (\( \rulename{\vee I} \), @def-rule-disjunction-introduction), but none of them could use one. This section gives the rule that uses a disjunction, \( \rulename{\vee E} \). It is the most familiar move in mathematics after "suppose": the split into cases, "if \( x \ge 0 \), then …; if \( x < 0 \), then …". It is also the last rule of this chapter. We use it to reach the stalled goal, to prove the laws that let "and" and "or" be rearranged, and to prove three facts about absolute values; the section ends with all the rules of the chapter on one page.

## A proof that needs two cases

The absolute value of a real number is defined in two cases:
\[
\abs{x} \coloneqq
\begin{cases}
x & \text{if } x \ge 0, \\
-x & \text{if } x < 0 .
\end{cases}
\]
Suppose we want to prove that \( \abs{xy} = \abs{x}\abs{y} \) for all real numbers \( x \) and \( y \). There is no single computation to do. Which formula gives \( \abs{xy} \) depends on the sign of \( xy \), and that depends on the signs of \( x \) and \( y \). Yet once the signs are fixed, each case is one line: if \( x \ge 0 \) and \( y < 0 \), for instance, then \( \abs{xy} = -xy = x \cdot (-y) = \abs{x}\abs{y} \).

So the proof we want has the shape "every real number is \( \ge 0 \) or \( < 0 \); in the first case …; in the second case …; so in every case …". The rules so far cannot say this. The attempt at \( P \vee Q \vdash Q \vee P \) at the end of Section 1.6 met the same wall from the other side. It derived that each side of the premise, assumed in a box, leads to the goal: lines 4 and 7 there were \( P \to (Q \vee P) \) and \( Q \to (Q \vee P) \). What it lacked was a rule to say "one of \( P \), \( Q \) holds, and either one leads to \( Q \vee P \); so \( Q \vee P \)". No rule of \( \wedge \) or \( \to \) takes a statement "\( \varphi \) or \( \psi \)", which does not say **which** side holds, and still reaches a definite conclusion. That is the job of the elimination rule for "or".

## The rule of or-elimination

*To use "\( \varphi \) or \( \psi \)", reach your goal from \( \varphi \), and reach it again from \( \psi \).*

The definition block states both rules for disjunction, so that the pair stands in one place: the new rule first, and then the two schemas of \( \rulename{\vee I} \) recalled from Section 1.6. As in every schema (@def-rule-schema), the Greek letters stand for arbitrary statements and \( i, j, k, l, m, n \) for line numbers.

::: {#def-rules-disjunction}
[Rules for Disjunction]

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {i} {\varphi \vee \psi}
  \open
  \hypo {j} {\varphi}
  \have {} {\vdots}
  \have {k} {\chi}
  \close
  \open
  \hypo {l} {\psi}
  \have {} {\vdots}
  \have {m} {\chi}
  \close
  \have {n} {\chi} \oe{i,j-k,l-m}
\end{nd}$
\qquad
$\begin{nd}[schema]
  \have {i} {\varphi}
  \have {k} {\varphi \vee \psi} \oi{i}
\end{nd}$
\qquad
$\begin{nd}[schema]
  \have {i} {\varphi}
  \have {k} {\psi \vee \varphi} \oi{i}
\end{nd}$
\end{center}
```

The first schema is the rule \( \rulename{\vee E} \) (**or-elimination**, or **proof by cases**); the other two are \( \rulename{\vee I} \), as in @def-rule-disjunction-introduction. In \( \rulename{\vee E} \), each line \( \chi \) (line \( k \) and line \( m \)) is a line of its box itself, not of a box inside it.
:::

In words, clause by clause.

- **The disjunction.** Line \( i \) holds a disjunction \( \varphi \vee \psi \), available at line \( n \). The cases are not ours to invent: they are the two sides of a disjunction we already have, as a premise, an assumption, or a line derived earlier. Writing "Case 1 … Case 2 …" does not create it.
- **Two boxes.** The first box opens with the left side \( \varphi \) as its assumption, the second with the right side \( \psi \). They are separate: the second opens after the first has closed, and the drawing shows a break in the vertical bar between them. So, by the scope rule of @def-derivation, no line of the second box may cite a line of the first. The disjunction does not tell us which side holds, so we must be ready for both, and each case's assumption is in force only inside its own box.
- **The same last line.** Both boxes end in the **same** statement \( \chi \), and in each box \( \chi \) is a line of that box itself, not of a box opened inside it. The rule then writes \( \chi \) a third time, outside both boxes, where neither \( \varphi \) nor \( \psi \) is assumed. That is honest only because \( \chi \) was reached whichever case holds.
- **Three citations.** The justification "\( \rulename{\vee E} \) \( i, \lines{j}{k}, \lines{l}{m} \)" cites the disjunction first, then the box of the left side, then the box of the right side, each box as a range. Both boxes must be available at line \( n \): closed, and sitting directly in the part of the derivation where line \( n \) is (@def-derivation).
- **Any conclusion.** The statement \( \chi \) need not mention \( \varphi \) or \( \psi \). It is whatever we are trying to reach. The next subsection says how to choose it.

The degenerate case is a box of one line, whose assumption is already \( \chi \). Nothing in the rule asks a box to contain more than its assumption, just as nothing in \( \rulename{{\to}I} \) did (@exm-first-boxes). The second derivation below has two such boxes.

::: {.warning}
A case may use only its own assumption. Here is the error in its usual form. Let \( x \) be a real number, and split on "\( x \ge 0 \) or \( x < 0 \)". *Case \( x \ge 0 \): then \( \abs{x} = x \). Case \( x < 0 \): since \( x \ge 0 \), again \( \abs{x} = x \). So \( \abs{x} = x \).* The second case cites the assumption of the first, whose box has closed, which the scope rule forbids. The conclusion is false at \( x = -1 \).
:::

## Cases end in the current goal

Section 1.3 set up two questions: *what is the goal's main connective?* and *what are the available lines' main connectives?* Section 1.6 answered the first for \( \vee \): postpone a disjunctive goal until one side is in hand. Now we can answer the second. A disjunction on an available line invites \( \rulename{\vee E} \): split on it.

What should the two boxes end in? The rule leaves \( \chi \) to us, and the choice is always the same. It is the **current goal**: whatever we are trying to reach at the point where the split is made. That may be the goal of the whole derivation, or a subgoal inside other boxes. The boxes of the split end in it, and the \( \rulename{\vee E} \) line that closes the split then writes it outside both boxes, exactly where it was wanted.

*Cases end in the current goal.*

The two habits fit together. Faced with a goal \( \varphi \vee \psi \) and an available disjunction \( \alpha \vee \beta \), do not choose a side of the goal yet: split on \( \alpha \vee \beta \) first. Inside each case the current goal is still \( \varphi \vee \psi \), but now a new line is in hand, the case's assumption, and it may be one side of the goal. Then choose, and the choice may be different in the two boxes. This is exactly how the stalled goal of Section 1.6 goes.

::: {#exm-disjunction-first-derivations}
[First derivations with "or"]

Show that \( P \vee Q \vdash Q \vee P \), and that \( P \vee P \vdash P \).
:::

::: {.solution}
*Idea.* For the first: the goal \( Q \vee P \) is a disjunction, and neither side is in hand, so we postpone it. The premise is a disjunction, so we split on it; the current goal is \( Q \vee P \), so both boxes will end there. In the box of \( P \), the right side of the goal is in hand, and \( \rulename{\vee I} \) takes it; in the box of \( Q \), the left side is, and \( \rulename{\vee I} \) takes that. The choice of side differs between the boxes, and each is safe because it is made inside its own case.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \open
  \hypo {2} {P}
  \have {3} {Q \vee P} \oi{2}
  \close
  \open
  \hypo {4} {Q}
  \have {5} {Q \vee P} \oi{4}
  \close
  \have {6} {Q \vee P} \oe{1,2-3,4-5}
\end{nd}$
\end{center}
```

The two boxes are separate: the break in the vertical bar between lines 3 and 4 shows where the first closes and the second opens. Line 3 uses the second schema of \( \rulename{\vee I} \) (\( P \) on the right) and line 5 the first (\( Q \) on the left). Both boxes end in \( Q \vee P \), and line 6 cites the disjunction on line 1 and the boxes \( \lines{2}{3} \) and \( \lines{4}{5} \). Compare the stalled attempt of Section 1.6: its two boxes are these two boxes, and line 6 is the step it could not take.

For the second, the goal is \( P \), and the premise is a disjunction, so we split. Both cases are already the goal, so each box consists of its assumption alone.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee P}
  \open
  \hypo {2} {P}
  \close
  \open
  \hypo {3} {P}
  \close
  \have {4} {P} \oe{1,2-2,3-3}
\end{nd}$
\end{center}
```

This is the degenerate case split, in which the two cases are the same case. The box \( \lines{2}{2} \) is a legal box whose last line is \( P \), a line of that box itself, and so is \( \lines{3}{3} \).
:::

Change one line of the first derivation and it stops being a derivation. Suppose the second box stops at its assumption \( Q \), and the last line still claims \( Q \vee P \):

```{=latex}
% expect-invalid
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \open
  \hypo {2} {P}
  \have {3} {Q \vee P} \oi{2}
  \close
  \open
  \hypo {4} {Q}
  \close
  \have {5} {Q \vee P} \oe{1,2-3,4-4}
\end{nd}$
\end{center}
```

Everything cited exists and is available: the disjunction, a box opened by \( P \), a box opened by \( Q \). What fails is the clause about the last lines. The box \( \lines{4}{4} \) ends in \( Q \), the box \( \lines{2}{3} \) ends in \( Q \vee P \), and \( \rulename{\vee E} \) needs one statement that ends both. The repair is the missing line 5 of the correct derivation.

::: {.check}
A derivation contains a line \( P \vee Q \) and a box opened by \( P \) that ends in \( R \). No box is opened by \( Q \). Which clause of \( \rulename{\vee E} \) stops us writing \( R \)? What single change to the derivation would allow it?
:::

::: {.solution}
The clause "two boxes": the rule needs one box opened by each side of the disjunction, and the box opened by \( Q \) is missing. Adding a box opened by \( Q \) whose last line is \( R \) (a derivation of \( R \) from \( Q \) and the lines available there) allows \( \rulename{\vee E} \), citing the disjunction and both boxes.
:::

**Why is the rule built like this?** Drop the second box, and from "\( x \ge 0 \) or \( x < 0 \)" and a derivation of \( \abs{x} = x \) from \( x \ge 0 \) we could conclude \( \abs{x} = x \) for every real \( x \), which fails at \( x = -1 \). Allow the two boxes to end in different statements \( \chi_1 \) and \( \chi_2 \), and ask what may be written after them: all we honestly know is "\( \chi_1 \) or \( \chi_2 \)". That is already reachable with the rule as it stands, by \( \rulename{\vee I} \) at the end of each box, turning both last lines into \( \chi_1 \vee \chi_2 \) (exercise B3 carries this out). So the rule asks for one common last line and loses nothing.

The next derivation splits on a disjunction that is not a premise but an **assumption**, opened because the goal asked for it.

::: {#exm-cases-on-hypothesis}
[Cases on a hypothesis are two implications]

Show that \( (P \to R) \wedge (Q \to R) \vdash (P \vee Q) \to R \).
:::

::: {.solution}
*Idea.* Goal-directed: the goal is an implication, so we open a box with its hypothesis \( P \vee Q \), and the current goal inside is \( R \). Premise-directed: the assumption just made is a disjunction, so we split on it, and both case boxes end in the current goal \( R \). In the case \( P \), the premise's main connective is \( \wedge \); \( \rulename{\wedge E} \) takes out \( P \to R \), and \( \rulename{{\to}E} \) fires on the case's assumption. The case \( Q \) is the same with the other half of the premise.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \to R) \wedge (Q \to R)}
  \open
  \hypo {2} {P \vee Q}
  \open
  \hypo {3} {P}
  \have {4} {P \to R} \ae{1}
  \have {5} {R} \ie{4,3}
  \close
  \open
  \hypo {6} {Q}
  \have {7} {Q \to R} \ae{1}
  \have {8} {R} \ie{7,6}
  \close
  \have {9} {R} \oe{2,3-5,6-8}
  \close
  \have {10} {(P \vee Q) \to R} \ii{2-9}
\end{nd}$
\end{center}
```

Line 9 closes the split inside the outer box: it cites line 2 and the boxes \( \lines{3}{5} \) and \( \lines{6}{8} \), all of which sit directly in the box \( \lines{2}{9} \), as line 9 does. Line 9 is a line of the outer box itself, so \( \rulename{{\to}I} \) at line 10 may cite \( \lines{2}{9} \). Lines 4 and 7 cite line 1, which lies in no box.
:::

Section 1.6 derived the converse, \( (P \vee Q) \to R \vdash (P \to R) \wedge (Q \to R) \), in @exm-or-hypothesis-split, using only \( \rulename{\vee I} \). So each of the two statements is derivable from the other: *cases on a hypothesis are two implications*. This is how mathematicians prove "if \( P \) or \( Q \), then \( R \)": they prove "if \( P \), then \( R \)" and "if \( Q \), then \( R \)". To show that an integer which is one more, or three more, than a multiple of \( 4 \) is odd, one treats the two forms separately, and the derivation above is the reason that is enough.

## Laws of "or"

Case splits are not only about numbers. The same two rules prove the laws that let us rearrange "and" and "or". The first says that "and" distributes over "or", in both directions.

::: {#prp-distributivity}
[Distributivity]

\( P \wedge (Q \vee R) \vdash (P \wedge Q) \vee (P \wedge R) \), and \( (P \wedge Q) \vee (P \wedge R) \vdash P \wedge (Q \vee R) \).
:::

*Try it first (ten minutes): derive the first sequent. Which rule will give its last line, and which disjunction will you split on?*

::: {.idea}
The natural first attempt reads the goal: it is a disjunction, so end with \( \rulename{\vee I} \) and aim at one side, say \( P \wedge Q \). That needs \( Q \) on a line, and the premise offers only \( P \) and \( Q \vee R \); nothing turns \( Q \vee R \) into \( Q \). The other side fails the same way. So the goal must be postponed, and the attempt shows why: the premise holds a disjunction, \( Q \vee R \), and neither of its sides is known. Premise-directed, then: \( \rulename{\wedge E} \) takes the premise apart into \( P \) and \( Q \vee R \), and we split on \( Q \vee R \), both cases ending in the current goal \( (P \wedge Q) \vee (P \wedge R) \). In the case \( Q \), the side \( P \wedge Q \) is one \( \rulename{\wedge I} \) away, and \( \rulename{\vee I} \) weakens it to the whole goal; the case \( R \) builds the other side. In the second sequent the premise itself is the disjunction, so we split on it at once; each case is a conjunction containing \( P \), and \( \rulename{\vee I} \) turns its other half into \( Q \vee R \).

*Before reading on: in the first derivation, which line does each box end on, and why must the two be the same?*
:::

::: {.proof}
For the first sequent, the following is a derivation with premise \( P \wedge (Q \vee R) \) and last line \( (P \wedge Q) \vee (P \wedge R) \).
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge (Q \vee R)}
  \have {2} {P} \ae{1}
  \have {3} {Q \vee R} \ae{1}
  \open
  \hypo {4} {Q}
  \have {5} {P \wedge Q} \ai{2,4}
  \have {6} {(P \wedge Q) \vee (P \wedge R)} \oi{5}
  \close
  \open
  \hypo {7} {R}
  \have {8} {P \wedge R} \ai{2,7}
  \have {9} {(P \wedge Q) \vee (P \wedge R)} \oi{8}
  \close
  \have {10} {(P \wedge Q) \vee (P \wedge R)} \oe{3,4-6,7-9}
\end{nd}$
\end{center}
```
Lines 5 and 8 may cite line 2, which lies in no box and so is available everywhere below it. Both boxes end in the goal, lines 6 and 9, as \( \rulename{\vee E} \) at line 10 requires.

For the second sequent, the following is a derivation with premise \( (P \wedge Q) \vee (P \wedge R) \) and last line \( P \wedge (Q \vee R) \).
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge Q) \vee (P \wedge R)}
  \open
  \hypo {2} {P \wedge Q}
  \have {3} {P} \ae{2}
  \have {4} {Q} \ae{2}
  \have {5} {Q \vee R} \oi{4}
  \have {6} {P \wedge (Q \vee R)} \ai{3,5}
  \close
  \open
  \hypo {7} {P \wedge R}
  \have {8} {P} \ae{7}
  \have {9} {R} \ae{7}
  \have {10} {Q \vee R} \oi{9}
  \have {11} {P \wedge (Q \vee R)} \ai{8,10}
  \close
  \have {12} {P \wedge (Q \vee R)} \oe{1,2-6,7-11}
\end{nd}$
\end{center}
```
This proves both sequents.
:::

The answer to the prompt: the boxes end on lines 6 and 9, both \( (P \wedge Q) \vee (P \wedge R) \). They must be the same statement because line 10 writes that statement outside both boxes, where neither \( Q \) nor \( R \) is assumed, and that is honest only if it was reached in each case.

In the second derivation, line 8 derives \( P \) a second time instead of citing line 3. It has to: line 3 lies in the box \( \lines{2}{6} \), which has closed, so line 3 is not available at line 8. Each case must earn its own \( P \).

For a real number \( x \), take \( P \): "\( x \ne 0 \)", \( Q \): "\( x > 0 \)" and \( R \): "\( x < 0 \)". The first sequent then reads: a nonzero number that is positive or negative is a positive nonzero number or a negative nonzero number. The law is dull in words, which is as it should be. Its use is in derivations, where it moves a case split from inside a conjunction to the outside, and in the laws of sets, where "and" and "or" become intersection and union.

The next derivation shows a case split **inside** a case: \( \rulename{\vee E} \) applied within one box of another \( \rulename{\vee E} \).

::: {#exm-disjunction-regroup}
[Regrouping a disjunction]

Show that \( P \vee (Q \vee R) \vdash (P \vee Q) \vee R \).
:::

::: {.solution}
*Idea.* The goal is a disjunction, and no side of it is in hand: postpone. The premise is a disjunction: split on it, with both boxes ending in the current goal \( (P \vee Q) \vee R \). The case \( P \) is two weakenings: first to \( P \vee Q \), then to the goal. The case \( Q \vee R \) is itself a disjunction, and neither \( Q \) nor \( R \) is known; so, inside that box, we split again, and the inner boxes end in the same current goal. In the inner case \( Q \) the goal is two weakenings away, and in the inner case \( R \) one.

*Before reading on: which disjunction does the inner \( \rulename{\vee E} \) cite, and which box must contain it?*

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee (Q \vee R)}
  \open
  \hypo {2} {P}
  \have {3} {P \vee Q} \oi{2}
  \have {4} {(P \vee Q) \vee R} \oi{3}
  \close
  \open
  \hypo {5} {Q \vee R}
  \open
  \hypo {6} {Q}
  \have {7} {P \vee Q} \oi{6}
  \have {8} {(P \vee Q) \vee R} \oi{7}
  \close
  \open
  \hypo {9} {R}
  \have {10} {(P \vee Q) \vee R} \oi{9}
  \close
  \have {11} {(P \vee Q) \vee R} \oe{5,6-8,9-10}
  \close
  \have {12} {(P \vee Q) \vee R} \oe{1,2-4,5-11}
\end{nd}$
\end{center}
```

Line 11 is the inner case split. It cites the disjunction on line 5, the assumption of the outer box it sits in, and the boxes \( \lines{6}{8} \) and \( \lines{9}{10} \), all of which sit inside the box \( \lines{5}{11} \), as line 11 does. Line 12 is the outer case split. Its second box is \( \lines{5}{11} \), whose last line, line 11, is a line of that box itself and not of a further box inside it, as @def-rules-disjunction requires. That is why line 11 is needed at all: without it, the box \( \lines{5}{11} \) would end inside the inner box \( \lines{9}{10} \).
:::

## From a skeleton to a proof about numbers

Almost every proof by cases in analysis has the same skeleton. A known fact supplies the cases, and each case is handled by a separate argument, a small lemma that turns the case's assumption into the goal. As a derivation, with the fact and the two lemmas as premises:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \hypo {2} {P \to R}
  \hypo {3} {Q \to R}
  \open
  \hypo {4} {P}
  \have {5} {R} \ie{2,4}
  \close
  \open
  \hypo {6} {Q}
  \have {7} {R} \ie{3,6}
  \close
  \have {8} {R} \oe{1,4-5,6-7}
\end{nd}$
\end{center}
```

The idea behind it is the whole method of this section at its simplest. The goal \( R \) is atomic, so the goal suggests nothing. Premise-directed, the disjunction on line 1 is split, both boxes ending in the current goal \( R \). In each box the matching lemma fires on the case's assumption. (@exm-cases-on-hypothesis did the same with the two lemmas packed into one conjunction, and inside a box.)

In a proof about real numbers, the disjunction is usually a fact about the order. The facts about \( \le \) and the absolute value used below are school algebra: every real number \( a \) satisfies \( a \ge 0 \) or \( a < 0 \); the rules of signs for products; adding two inequalities of the same direction. Chapter 11 proves all of them from the axioms of an ordered field. Here we take them as known. In the language of this chapter, "every real number \( a \) satisfies \( a \ge 0 \) or \( a < 0 \)" is a supply of disjunctions: for each number we meet, it gives a line \( (a \ge 0) \vee (a < 0) \) that \( \rulename{\vee E} \) may cite.

The first example is the smallest, and it is written twice: as a proof in which every step carries its rule in brackets, and as a derivation.

::: {#exm-abs-at-least-x}
[A number is at most its absolute value]

Let \( x \) be a real number. Prove that \( \abs{x} \ge x \), by cases, labeling each step with its rule.
:::

::: {.solution}
The goal \( \abs{x} \ge x \) is the disjunction \( (\abs{x} > x) \vee (\abs{x} = x) \), and neither side is known for every \( x \) (the first fails at \( x = 1 \), the second at \( x = -1 \)), so we postpone it. The fact "\( x \ge 0 \) or \( x < 0 \)" is a disjunction to split on. In prose:

> We have \( x \ge 0 \) or \( x < 0 \), and we argue by cases \( [\rulename{\vee E}] \).
>
> *Case \( x \ge 0 \).* By the definition of the absolute value, \( \abs{x} = x \) \( [\rulename{{\to}E}] \). So \( \abs{x} \ge x \) \( [\rulename{\vee I}] \).
>
> *Case \( x < 0 \).* By the definition, \( \abs{x} = -x \), and \( -x > 0 > x \); so \( \abs{x} > x \) \( [\rulename{{\to}E}] \), which is the school-algebra fact "if \( x < 0 \), then \( \abs{x} > x \)" used on the case's assumption. So \( \abs{x} \ge x \) \( [\rulename{\vee I}] \).
>
> In either case \( \abs{x} \ge x \), so \( \abs{x} \ge x \).

As a derivation, with the order fact, the definition's first clause, and the school-algebra fact about negative numbers as premises, and with \( \abs{x} \ge x \) written out:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {x \ge 0 \vee x < 0}
  \hypo {2} {x \ge 0 \to \abs{x} = x}
  \hypo {3} {x < 0 \to \abs{x} > x}
  \open
  \hypo {4} {x \ge 0}
  \have {5} {\abs{x} = x} \ie{2,4}
  \have {6} {\abs{x} > x \vee \abs{x} = x} \oi{5}
  \close
  \open
  \hypo {7} {x < 0}
  \have {8} {\abs{x} > x} \ie{3,7}
  \have {9} {\abs{x} > x \vee \abs{x} = x} \oi{8}
  \close
  \have {10} {\abs{x} > x \vee \abs{x} = x} \oe{1,4-6,7-9}
\end{nd}$
\end{center}
```

It is the skeleton above, with a weakening at the end of each box: line 6 takes the right side of the goal (second schema of \( \rulename{\vee I} \)) and line 9 the left side (first schema). Each case took the side it had in hand. At \( x = 3 \), the first case applies and line 6 reads \( 3 > 3 \) or \( 3 = 3 \); at \( x = -2 \), the second applies and line 8 reads \( 2 > -2 \).
:::

The next two examples are longer, and in each the case split is doing real work.

::: {#exm-abs-product-cases}
[The absolute value of a product]

Let \( x \) and \( y \) be real numbers. Prove that \( \abs{xy} = \abs{x}\abs{y} \).
:::

::: {.solution}
We use that \( \abs{a} = -a \) whenever \( a \le 0 \): for \( a < 0 \) this is the definition, and for \( a = 0 \) both sides are \( 0 \).

The number \( x \) satisfies \( x \ge 0 \) or \( x < 0 \), and we argue by cases \( [\rulename{\vee E}] \). Inside each case, \( y \ge 0 \) or \( y < 0 \), and we argue by cases again.

*Case \( x \ge 0 \), \( y \ge 0 \).* Then \( xy \ge 0 \), so \( \abs{xy} = xy = \abs{x}\abs{y} \).

*Case \( x \ge 0 \), \( y < 0 \).* Then \( xy \le 0 \), so \( \abs{xy} = -xy = x \cdot (-y) = \abs{x}\abs{y} \).

*Case \( x < 0 \), \( y \ge 0 \).* Then \( xy \le 0 \), so \( \abs{xy} = -xy = (-x) \cdot y = \abs{x}\abs{y} \).

*Case \( x < 0 \), \( y < 0 \).* Then \( xy > 0 \), so \( \abs{xy} = xy = (-x)(-y) = \abs{x}\abs{y} \).

Each inner case split reaches \( \abs{xy} = \abs{x}\abs{y} \), so each outer case does, and hence the equation holds.
:::

The structure is two uses of \( \rulename{\vee E} \), one inside each box of the other: two outer boxes (the sign of \( x \)), each containing two inner boxes (the sign of \( y \)), and every one of the four inner boxes ending in the same equation, the current goal. The second and third cases needed the remark about \( a \le 0 \). When \( x = 0 \) and \( y < 0 \), the product is \( 0 \), not negative, and without the remark the case would have a hole at exactly that point.

A case split need not be the obvious one. The triangle inequality has an equally short proof with two cases, if we split on the sign of the right quantity.

::: {#exm-triangle-inequality-cases}
[The triangle inequality by cases]

Let \( x \) and \( y \) be real numbers. Prove that \( \abs{x + y} \le \abs{x} + \abs{y} \).
:::

::: {.solution}
First, every real number \( a \) satisfies \( a \le \abs{a} \) and \( -a \le \abs{a} \). This is itself a proof by cases \( [\rulename{\vee E}] \): if \( a \ge 0 \), then \( \abs{a} = a \), so \( a \le \abs{a} \), and \( -a \le 0 \le a = \abs{a} \); if \( a < 0 \), then \( \abs{a} = -a \), so \( -a \le \abs{a} \), and \( a < 0 < -a = \abs{a} \).

Now \( x + y \ge 0 \) or \( x + y < 0 \), and we argue by cases \( [\rulename{\vee E}] \).

*Case \( x + y \ge 0 \).* Then \( \abs{x + y} = x + y \le \abs{x} + \abs{y} \), adding \( x \le \abs{x} \) and \( y \le \abs{y} \).

*Case \( x + y < 0 \).* Then \( \abs{x + y} = -x - y = (-x) + (-y) \le \abs{x} + \abs{y} \), adding \( -x \le \abs{x} \) and \( -y \le \abs{y} \).

Both cases reach \( \abs{x + y} \le \abs{x} + \abs{y} \), so it holds.
:::

Two case splits appear here, one after the other rather than one inside the other. The first proves a small lemma for an arbitrary number \( a \), both halves at once, and its first half, \( a \le \abs{a} \), is @exm-abs-at-least-x again. The second uses both halves of the lemma, for \( a = x \) and for \( a = y \). Splitting on the sign of \( x + y \) instead of the signs of \( x \) and \( y \) is what saves two cases: the absolute value in the goal is \( \abs{x + y} \), and its sign is the only one the goal's left side cares about.

::: {.warning}
A case split must cover every possibility. A common faulty proof of the triangle inequality treats "\( x \ge 0 \) and \( y \ge 0 \)" and "\( x < 0 \) and \( y < 0 \)", checks both, and stops. The disjunction of these two cases is not a fact: \( x = 1 \), \( y = -1 \) satisfies neither. So there is no line \( \varphi \vee \psi \) for \( \rulename{\vee E} \) to cite, and the rule was never legally applied. The missing mixed-sign cases are the interesting ones: at \( x = 1 \), \( y = -1 \) the inequality reads \( 0 \le 2 \), and it is strict.
:::

The warning is about the first thing \( \rulename{\vee E} \) cites. The disjunction must itself be on an available line, derived or known, before the boxes are opened.

::: {.warning}
Cases must **exhaust**, and a split that silently drops a value is a missing case in disguise. "Every real \( x \) satisfies \( x > 0 \) or \( x < 0 \)" is false: \( x = 0 \) satisfies neither. A proof that splits into \( x > 0 \) and \( x < 0 \) cites a disjunction that is not available, and proves nothing about \( x = 0 \). The true disjunctions are "\( x \ge 0 \) or \( x < 0 \)", and "\( x > 0 \), or \( x = 0 \), or \( x < 0 \)".
:::

Cases may overlap, however. "\( x \ge 0 \) or \( x \le 0 \)" is true for every real \( x \), and \( x = 0 \) lies in both cases. Nothing in \( \rulename{\vee E} \) forbids this: the rule asks that the goal be reached in each case, not that the cases be disjoint. (This is the inclusive "or" of Section 1.1.)

::: {.check}
Each of the following begins a proof that \( x^2 \ge 0 \) for every real number \( x \). Which case splits are exhaustive, so that \( \rulename{\vee E} \) may be applied?

::: {.enumerate options="label=(\roman*)"}
1. Case \( x \ge 0 \); case \( x < 0 \).
2. Case \( x > 0 \); case \( x < 0 \).
3. Case \( x \ge 0 \); case \( x \le 0 \).
:::
:::

::: {.solution}
(i) Exhaustive: every real number is \( \ge 0 \) or \( < 0 \). (ii) Not exhaustive: \( x = 0 \) is in neither case, so the disjunction cited is false. The claim is still true at \( 0 \), but this split never proves it there. (iii) Exhaustive. The cases overlap at \( x = 0 \), which does no harm: \( x^2 = 0 \ge 0 \) is reached in both.
:::

## What the rules sound like

Here is the row of the rule, phrase, and Lean table for \( \rulename{\vee E} \). As before, the last column is for readers who use a proof assistant, and nothing depends on it.

| Rule | You write | Lean |
|------|--------------------------------------|------------------------|
| \( \rulename{\vee E} \) | "Case 1: \( P \). … so \( R \). Case 2: \( Q \). … so \( R \). In either case, \( R \)." | `Or.elim h` (or `cases h`) |

The phrase has three parts, and a written proof often drops the first: "we argue by cases" without saying which disjunction supplies them. When the disjunction is a standard fact ("\( x \ge 0 \) or \( x < 0 \)"), that is harmless. When it is not, the reader should ask for it, because it is the line the rule cites first.

## The rules of this chapter

This chapter has introduced six rules, one or two at a time, and the structural clause \( \rulename{R} \). Here they are on one page, as schemas. Letters in the number column stand for line numbers; every cited line must be available (@def-derivation), and each box rule needs the box's last line as a line of that box itself.

**Conjunction** (@def-rules-conjunction): \( \rulename{\wedge I} \), and the two forms of \( \rulename{\wedge E} \).

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

**Implication** (@def-rules-implication): \( \rulename{{\to}E} \) and \( \rulename{{\to}I} \); and **repetition**, clause (D3) of @def-derivation.

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {i} {\varphi \to \psi}
  \have {j} {\varphi}
  \have {k} {\psi} \ie{i,j}
\end{nd}$
\qquad
$\begin{nd}[schema]
  \open
  \hypo {i} {\varphi}
  \have {} {\vdots}
  \have {j} {\psi}
  \close
  \have {k} {\varphi \to \psi} \ii{i-j}
\end{nd}$
\qquad
$\begin{nd}[schema]
  \have {i} {\varphi}
  \have {} {\vdots}
  \have {k} {\varphi} \r{i}
\end{nd}$
\end{center}
```

**Disjunction** (@def-rules-disjunction): the two forms of \( \rulename{\vee I} \), and \( \rulename{\vee E} \).

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {i} {\varphi}
  \have {k} {\varphi \vee \psi} \oi{i}
\end{nd}$
\qquad
$\begin{nd}[schema]
  \have {i} {\varphi}
  \have {k} {\psi \vee \varphi} \oi{i}
\end{nd}$
\qquad
$\begin{nd}[schema]
  \have {i} {\varphi \vee \psi}
  \open
  \hypo {j} {\varphi}
  \have {} {\vdots}
  \have {k} {\chi}
  \close
  \open
  \hypo {l} {\psi}
  \have {} {\vdots}
  \have {m} {\chi}
  \close
  \have {n} {\chi} \oe{i,j-k,l-m}
\end{nd}$
\end{center}
```

Each rule is also a move in the search for a derivation. Read by the goal's main connective, the introduction rules say how a goal is built: that is the move *read the skeleton off the goal*. Read by an available line's main connective, the elimination rules say how that line is used: *use a premise by its main connective*.

| Main connective | As the goal (goal-directed) | As an available line (premise-directed) |
|---|---|---|
| \( \wedge \) | two subgoals, one per side; finish with \( \rulename{\wedge I} \) | take it apart with \( \rulename{\wedge E} \) |
| \( \to \) | open a box with the hypothesis; the new goal is the conclusion; close with \( \rulename{{\to}I} \) | fire it with \( \rulename{{\to}E} \) once its hypothesis is on a line, or make the hypothesis a subgoal |
| \( \vee \) | postpone; choose a side with \( \rulename{\vee I} \) when that side is in hand | split with \( \rulename{\vee E} \); both boxes end in the current goal |

And here is the full rule, phrase, and Lean table for the chapter, assembled from the rows of Sections 1.3 to 1.7.

| Rule | You write | Lean |
|------|--------------------------------------|------------------------|
| \( \rulename{\wedge I} \) | "We show \( P \), and we show \( Q \)." | `constructor` |
| \( \rulename{\wedge E} \) | "In particular, \( P \)." | `h.1` (and `h.2`) |
| \( \rulename{{\to}E} \) | "Since \( P \) implies \( Q \), and \( P \) holds, \( Q \)." | `exact h hp` |
| \( \rulename{{\to}I} \) | "Assume \( P \). … Hence \( Q \)." | `intro hp` |
| \( \rulename{R} \) | "As shown above, \( P \)." | `exact hp` |
| \( \rulename{\vee I} \) | "So \( P \) or \( Q \) holds." | `left` (or `Or.inl hp`); `right` |
| \( \rulename{\vee E} \) | "Case 1: \( P \). … so \( R \). Case 2: \( Q \). … so \( R \). In either case, \( R \)." | `Or.elim h` (or `cases h`) |

The rules for "not", for \( \bot \), and for "if and only if", the rule for proof by contradiction, and the method that turns the table of moves above into a way of finding derivations are the subject of Chapter 2.

## Exercises

### A. Check your understanding

::: {#exr-disjunction-and-cases-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the rule \( \rulename{\vee E} \) as a schema, and name the three things its justification cites.
2. For each sentence, taken from a proof, name the disjunction that supplies the cases and the statement both cases end in.
    - "If \( n \) is even, then \( n^2 + n = n(n + 1) \) is even; if \( n \) is odd, then \( n + 1 \) is even and so is \( n(n + 1) \). Either way, \( n^2 + n \) is even."
    - "Both possibilities for the sign of \( t \) give \( t^2 \ge 0 \)."
3. Let \( n \) be an integer. True or false, with a reason: "If \( n \) is even, then \( n^2 \) is even. Since every integer is even or odd, \( n^2 \) is even" is a correct proof by cases that \( n^2 \) is even.
4. The following is offered as a derivation of \( P \vee Q, \; P \to R \vdash R \). Name the line that is not justified and the clause of @def-rules-disjunction it violates.
   ```{=latex}
   % expect-invalid
   \begin{center}
   $\begin{nd}
     \hypo {1} {P \vee Q}
     \hypo {2} {P \to R}
     \open
     \hypo {3} {P}
     \have {4} {R} \ie{2,3}
     \close
     \have {5} {R} \oe{1,3-4}
   \end{nd}$
   \end{center}
   ```
5. In the first derivation of @prp-distributivity, which line is the disjunction that \( \rulename{\vee E} \) cites at line 10, and where did it come from? Why does each box end in \( (P \wedge Q) \vee (P \wedge R) \) rather than in \( P \wedge Q \) and \( P \wedge R \)?
6. In the same derivation, why does line 6 use \( \rulename{\vee I} \) to put \( P \wedge Q \) on the **left**? Could line 6 have been \( (P \wedge R) \vee (P \wedge Q) \)?
:::
:::

::: {.solution}
(a) The schema is the first one of @def-rules-disjunction: from a line \( i \) holding \( \varphi \vee \psi \), a box \( \lines{j}{k} \) opened by \( \varphi \), and a box \( \lines{l}{m} \) opened by \( \psi \), each ending in the same statement \( \chi \) as a line of its own, a line \( n \) holding \( \chi \). The justification "\( \rulename{\vee E} \) \( i, \lines{j}{k}, \lines{l}{m} \)" cites the disjunction and the two boxes.

(b) In the first, the disjunction is "\( n \) is even or \( n \) is odd", and both cases end in "\( n^2 + n \) is even". In the second, it is "\( t \ge 0 \) or \( t < 0 \)" (the sentence does not say it, and a careful reader supplies it), and both cases end in \( t^2 \ge 0 \).

(c) False. The disjunction "\( n \) is even or \( n \) is odd" does not say which side holds, so \( \rulename{\vee E} \) needs a second case, reaching "\( n^2 \) is even" from "\( n \) is odd", and the argument has none. Here the second case cannot be supplied: at \( n = 1 \) the number \( n^2 = 1 \) is odd, so the claim itself is false.

(d) Line 5. \( \rulename{\vee E} \) needs two boxes, one opened by each side of the disjunction (the clause "two boxes"); line 5 cites only the box opened by \( P \), and no box opened by \( Q \) exists. Nothing available reaches \( R \) from \( Q \) either, so the gap cannot be filled from these premises. An instance shows the claim itself fails (informally: a derivation never leads from true premises to a false conclusion, which Chapter 3 proves: @thm-soundness): for a real number \( x \), take \( P \): "\( x > 1 \)", \( Q \): "\( x < 1 \)", \( R \): "\( x > 0 \)". At \( x = -1 \) both premises hold and \( R \) does not.

(e) Line 3, \( Q \vee R \), obtained from the premise by \( \rulename{\wedge E} \). Each box must end in the current goal, \( (P \wedge Q) \vee (P \wedge R) \), because line 10 writes one statement, the same one that ends both boxes; boxes ending in \( P \wedge Q \) and \( P \wedge R \) would end in different statements, and \( \rulename{\vee E} \) could not be applied to them.

(f) Line 6 must be the current goal exactly, since both boxes end in it and line 10 writes it. The goal \( (P \wedge Q) \vee (P \wedge R) \) has \( P \wedge Q \) as its **left** side, so line 6 uses the first schema of \( \rulename{\vee I} \). The line \( (P \wedge R) \vee (P \wedge Q) \) is also an instance of \( \rulename{\vee I} \) on line 5 (the second schema), but it is a different statement: the first box would then end differently from the second, whose last line 9 is \( (P \wedge Q) \vee (P \wedge R) \), and \( \rulename{\vee E} \) could not cite both boxes.
:::

### B. Practice

::: {#exr-disjunction-and-cases-b1}
[B1: The other distributive law]

Show that \( (P \vee Q) \wedge (P \vee R) \vdash P \vee (Q \wedge R) \).

*Hint: after taking the premise apart, you will need a case split inside a case.*
:::

::: {.solution}
The goal is a disjunction with no side in hand, so we postpone it. The premise gives two disjunctions. Split on \( P \vee Q \), both cases ending in the goal. In the case \( P \), the goal is one weakening away. In the case \( Q \), we still lack \( R \), so we split on \( P \vee R \) inside that box: its case \( P \) weakens as before, and its case \( R \) combines with \( Q \).
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \vee Q) \wedge (P \vee R)}
  \have {2} {P \vee Q} \ae{1}
  \have {3} {P \vee R} \ae{1}
  \open
  \hypo {4} {P}
  \have {5} {P \vee (Q \wedge R)} \oi{4}
  \close
  \open
  \hypo {6} {Q}
  \open
  \hypo {7} {P}
  \have {8} {P \vee (Q \wedge R)} \oi{7}
  \close
  \open
  \hypo {9} {R}
  \have {10} {Q \wedge R} \ai{6,9}
  \have {11} {P \vee (Q \wedge R)} \oi{10}
  \close
  \have {12} {P \vee (Q \wedge R)} \oe{3,7-8,9-11}
  \close
  \have {13} {P \vee (Q \wedge R)} \oe{2,4-5,6-12}
\end{nd}$
\end{center}
```
Line 10 cites line 6, the assumption of the enclosing box, which is still open at line 10. Line 12 cites line 3, which lies in no box. Splitting on \( P \vee R \) first, with the roles of \( Q \) and \( R \) exchanged, works equally well.
:::

::: {#exr-disjunction-and-cases-b2}
[B2: The larger of two numbers]

For real numbers \( a \) and \( b \), let \( \max(a, b) \coloneqq a \) if \( a \ge b \), and \( \max(a, b) \coloneqq b \) if \( a < b \). Prove that \( \max(a, b) \ge a \) and \( \max(a, b) \ge b \). Hence deduce that \( \max(a, b) \ge \frac{1}{2}(a + b) \): the larger of two numbers is at least their average.
:::

::: {.solution}
We have \( a \ge b \) or \( a < b \), and we argue by cases \( [\rulename{\vee E}] \); the current goal is the conjunction "\( \max(a, b) \ge a \) and \( \max(a, b) \ge b \)".

*Case \( a \ge b \).* Then \( \max(a, b) = a \). So \( \max(a, b) \ge a \), since \( a = a \) and \( \ge \) allows equality \( [\rulename{\vee I}] \); and \( \max(a, b) = a \ge b \). So both hold \( [\rulename{\wedge I}] \).

*Case \( a < b \).* Then \( \max(a, b) = b \). So \( \max(a, b) = b > a \), which gives \( \max(a, b) \ge a \) \( [\rulename{\vee I}] \); and \( \max(a, b) = b \ge b \) \( [\rulename{\vee I}] \). So both hold \( [\rulename{\wedge I}] \).

In either case \( \max(a, b) \ge a \) and \( \max(a, b) \ge b \), so both hold.

Adding the two inequalities gives \( 2\max(a, b) \ge a + b \), and dividing by \( 2 > 0 \) gives \( \max(a, b) \ge \frac{1}{2}(a + b) \). For instance, \( \max(3, -5) = 3 \ge -1 = \frac{1}{2}(3 + (-5)) \).
:::

::: {#exr-disjunction-and-cases-b3}
[B3: Two cases, two conclusions]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( P \vee Q, \; P \to R, \; Q \to S \vdash R \vee S \).
2. Use (a) to prove: for every integer \( n \), \( n^2 \) is a multiple of \( 4 \) or \( n^2 \) is one more than a multiple of \( 4 \). You may use that every integer is even or odd.
:::
:::

::: {.solution}
(a) The goal is a disjunction: postpone. Split on \( P \vee Q \). In each case the matching implication gives one of \( R \), \( S \), and \( \rulename{\vee I} \) weakens it to the common last line \( R \vee S \), the current goal.
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \hypo {2} {P \to R}
  \hypo {3} {Q \to S}
  \open
  \hypo {4} {P}
  \have {5} {R} \ie{2,4}
  \have {6} {R \vee S} \oi{5}
  \close
  \open
  \hypo {7} {Q}
  \have {8} {S} \ie{3,7}
  \have {9} {R \vee S} \oi{8}
  \close
  \have {10} {R \vee S} \oe{1,4-6,7-9}
\end{nd}$
\end{center}
```

(b) Take \( P \): "\( n \) is even", \( Q \): "\( n \) is odd", \( R \): "\( n^2 \) is a multiple of \( 4 \)", \( S \): "\( n^2 \) is one more than a multiple of \( 4 \)". The premise \( P \vee Q \) is the fact we may use. For \( P \to R \): if \( n = 2k \) for an integer \( k \), then \( n^2 = 4k^2 \). For \( Q \to S \): if \( n = 2k + 1 \), then \( n^2 = 4k^2 + 4k + 1 = 4(k^2 + k) + 1 \). By (a), \( R \vee S \). For instance, \( 6^2 = 36 = 4 \cdot 9 \) and \( 7^2 = 49 = 4 \cdot 12 + 1 \).
:::

### C. Going deeper

::: {#exr-disjunction-and-cases-c1}
[C1: The reverse triangle inequality]

Let \( x \) and \( y \) be real numbers. Prove that
\[
\bigl\lvert \abs{x} - \abs{y} \bigr\rvert \le \abs{x - y}
\]
by splitting into the two cases \( \abs{x} \ge \abs{y} \) and \( \abs{x} < \abs{y} \), using in each case the triangle inequality of @exm-triangle-inequality-cases. Then explain why these two cases exhaust all possibilities, and why a split on the signs of \( x \) and \( y \) would need four cases.
:::

::: {.solution}
[Hint 1]

The triangle inequality bounds \( \abs{u + v} \). Write \( x \) as a sum of two numbers whose absolute values appear in the goal.
:::

::: {.solution}
[Hint 2]

In the case \( \abs{x} \ge \abs{y} \), the left side is \( \abs{x} - \abs{y} \). Start from \( x = (x - y) + y \).
:::

::: {.solution}
We use two school facts: for real numbers \( a \), \( b \), either \( a \ge b \) or \( a < b \); and \( \abs{-a} = \abs{a} \) for every real \( a \) (if \( a \ge 0 \) then \( -a \le 0 \), so \( \abs{-a} = a \); if \( a < 0 \) then \( -a > 0 \), so \( \abs{-a} = -a = \abs{a} \)).

By the first fact, \( \abs{x} \ge \abs{y} \) or \( \abs{x} < \abs{y} \), and we argue by cases \( [\rulename{\vee E}] \).

*Case \( \abs{x} \ge \abs{y} \).* Then \( \abs{x} - \abs{y} \ge 0 \), so \( \bigl\lvert \abs{x} - \abs{y} \bigr\rvert = \abs{x} - \abs{y} \). By @exm-triangle-inequality-cases applied to the numbers \( x - y \) and \( y \),
\[
\abs{x} = \abs{(x - y) + y} \le \abs{x - y} + \abs{y} ,
\]
so \( \abs{x} - \abs{y} \le \abs{x - y} \), which is the goal in this case.

*Case \( \abs{x} < \abs{y} \).* Then \( \abs{x} - \abs{y} < 0 \), so \( \bigl\lvert \abs{x} - \abs{y} \bigr\rvert = \abs{y} - \abs{x} \). By @exm-triangle-inequality-cases applied to \( y - x \) and \( x \),
\[
\abs{y} = \abs{(y - x) + x} \le \abs{y - x} + \abs{x} ,
\]
so \( \abs{y} - \abs{x} \le \abs{y - x} = \abs{-(x - y)} = \abs{x - y} \).

Both cases reach the goal, which proves the inequality.

The two cases exhaust all possibilities because they are the two sides of the disjunction "\( a \ge b \) or \( a < b \)" with \( a = \abs{x} \), \( b = \abs{y} \), and that disjunction holds for all real numbers. The split was chosen by the goal: the outer absolute value is of \( \abs{x} - \abs{y} \), and its formula depends only on the sign of that difference.

A split on signs would decide \( \abs{x} \) and \( \abs{y} \) separately: \( x \ge 0 \) or \( x < 0 \) gives the formula for \( \abs{x} \), and inside each case \( y \ge 0 \) or \( y < 0 \) gives the formula for \( \abs{y} \). That is a case split inside each box of another, with \( 2 \cdot 2 = 4 \) inner boxes, as in @exm-abs-product-cases. Fewer would not do for that method: with only the sign of \( x \) fixed, \( \abs{y} \) still has no formula.

**Marking scheme.** (10 points)

- 2: states the disjunction \( \abs{x} \ge \abs{y} \) or \( \abs{x} < \abs{y} \) and says it holds for all reals.
- 3: in the first case, removes the outer absolute value correctly and derives \( \abs{x} - \abs{y} \le \abs{x - y} \) from the triangle inequality for \( (x - y) + y \).
- 3: in the second case, the same with the roles exchanged, including \( \abs{y - x} = \abs{x - y} \).
- 2: explains the four sign cases as a split inside each case of another.

Fatal errors (0 for the step): using \( \bigl\lvert \abs{x} - \abs{y} \bigr\rvert = \abs{x} - \abs{y} \) in both cases; applying the triangle inequality to a difference as if \( \abs{u - v} \le \abs{u} - \abs{v} \).
A proof that squares both sides instead, or splits on signs, earns the 6 points of the two middle lines if every case is complete.
:::

::: {#exr-disjunction-and-cases-c2}
[C2: Find the error]

Here is a proof, by four cases, that \( \abs{x - y} \le \abs{x} + \abs{y} \) for all real numbers \( x \) and \( y \).

> *Case 1: \( x \ge 0 \).* Then \( \abs{x} = x \).
>
> *Case 1a: \( y \ge 0 \).* Then \( \abs{y} = y \), and \( \abs{x - y} \) is \( x - y \) or \( y - x \). Since \( x - y \le x \le x + y \) and \( y - x \le y \le x + y \), we get \( \abs{x - y} \le x + y = \abs{x} + \abs{y} \).
>
> *Case 1b: \( y < 0 \).* Then \( \abs{y} = -y \), and \( x - y > 0 \), so \( \abs{x - y} = x - y = \abs{x} + \abs{y} \).
>
> *Case 2: \( x < 0 \).* Then \( \abs{x} = -x \).
>
> *Case 2a: \( y \ge 0 \).* Then \( \abs{y} = y \), and \( x - y < 0 \), so \( \abs{x - y} = y - x = \abs{y} + \abs{x} \).
>
> *Case 2b: \( y < 0 \).* Then \( \abs{y} = -y \). Since \( x \ge 0 \) and \( y < 0 \), we have \( x - y > 0 \), so \( \abs{x - y} = x - y \le \abs{x} + \abs{y} \), because \( x \le \abs{x} \) and \( -y = \abs{y} \).
>
> All four cases give \( \abs{x - y} \le \abs{x} + \abs{y} \).

::: {.enumerate options="label=(\alph*)"}
1. Is the statement true?
2. Find the line that is not justified, and name the rule whose conditions it breaks.
3. Show with specific numbers that the step fails.
4. Repair Case 2b.
:::
:::

::: {.solution}
(a) Yes. For instance, it follows from @exm-triangle-inequality-cases applied to \( x \) and \( -y \), since \( \abs{-y} = \abs{y} \) (shown in the solution of @exr-disjunction-and-cases-c1). So the question is not whether the conclusion holds but whether this argument proves it.

(b) The sentence "Since \( x \ge 0 \) and \( y < 0 \), we have \( x - y > 0 \)" in Case 2b. The assumption \( x \ge 0 \) is the assumption of Case 1. In derivation terms, it opens the first box of the outer \( \rulename{\vee E} \), and Case 2b lies inside the **second** box, which is opened by \( x < 0 \). Once the first box has closed, its lines are not available (the scope rule of @def-derivation), so Case 2b may not cite \( x \ge 0 \): the rule broken is \( \rulename{\vee E} \), whose second box may use only its own assumption and the lines available outside both boxes. The sentence is the reasoning of Case 1b copied into Case 2b, where its assumption is no longer in force. So the box of Case 2 does not reach the goal from the lines available to it, and the final \( \rulename{\vee E} \) has no right to cite it.

(c) Take \( x = -3 \) and \( y = -1 \), which is Case 2b. Then \( x - y = -2 \), which is not \( > 0 \), and \( \abs{x - y} = 2 \ne -2 = x - y \). The conclusion of Case 2b still holds here (\( 2 \le 3 + 1 \)), but the step used to reach it is false.

(d) In Case 2b, \( x < 0 \) and \( y < 0 \), so \( \abs{x} = -x \) and \( \abs{y} = -y \). The number \( \abs{x - y} \) is \( x - y \) or \( y - x \). Since \( x < 0 \), we have \( x - y < -y = \abs{y} \le \abs{x} + \abs{y} \). Since \( y < 0 \), we have \( y - x < -x = \abs{x} \le \abs{x} + \abs{y} \). So in either case \( \abs{x - y} \le \abs{x} + \abs{y} \), using only the assumptions of Case 2b.
:::

::: {#exr-disjunction-and-cases-c3}
[C3: Exit check: a distributive law, rule by rule]

Derive \( (P \wedge Q) \vee (R \wedge Q) \vdash (P \vee R) \wedge Q \), naming the rule and the cited lines on every line. Then say which steps would change if the premise were \( (P \wedge Q) \vee (P \wedge R) \) and the goal \( P \wedge (Q \vee R) \), and which would stay the same.
:::

::: {.solution}
The goal is a conjunction, but neither of its sides is on a line, and the premise is a disjunction, so we split on the premise first; both cases end in the current goal \( (P \vee R) \wedge Q \). In each case, \( \rulename{\wedge E} \) takes the assumption apart, \( \rulename{\vee I} \) builds \( P \vee R \) from the side in hand, and \( \rulename{\wedge I} \) builds the goal.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge Q) \vee (R \wedge Q)}
  \open
  \hypo {2} {P \wedge Q}
  \have {3} {P} \ae{2}
  \have {4} {Q} \ae{2}
  \have {5} {P \vee R} \oi{3}
  \have {6} {(P \vee R) \wedge Q} \ai{5,4}
  \close
  \open
  \hypo {7} {R \wedge Q}
  \have {8} {R} \ae{7}
  \have {9} {Q} \ae{7}
  \have {10} {P \vee R} \oi{8}
  \have {11} {(P \vee R) \wedge Q} \ai{10,9}
  \close
  \have {12} {(P \vee R) \wedge Q} \oe{1,2-6,7-11}
\end{nd}$
\end{center}
```

Line by line: 1 is the premise; 2 is the assumption of the first case; 3 and 4 are \( \rulename{\wedge E} \) on line 2; 5 is \( \rulename{\vee I} \) on line 3, first schema; 6 is \( \rulename{\wedge I} \) on lines 5 and 4, in that order, so that \( P \vee R \) is the left conjunct; 7 is the assumption of the second case; 8 and 9 are \( \rulename{\wedge E} \) on line 7; 10 is \( \rulename{\vee I} \) on line 8, second schema; 11 is \( \rulename{\wedge I} \) on lines 10 and 9; 12 is \( \rulename{\vee E} \), citing the disjunction on line 1 and the boxes \( \lines{2}{6} \) and \( \lines{7}{11} \), both of which end in the goal as lines of their own. No line of the second box cites the first.

With premise \( (P \wedge Q) \vee (P \wedge R) \) and goal \( P \wedge (Q \vee R) \), the shape stays the same: a split on the premise, \( \rulename{\wedge E} \) twice in each box, one \( \rulename{\vee I} \) and one \( \rulename{\wedge I} \) in each box, and \( \rulename{\vee E} \) at the end. What changes is which part is weakened and where it goes. The common conjunct is now \( P \), and the parts that differ between the cases are \( Q \) and \( R \); so the \( \rulename{\vee I} \) lines build \( Q \vee R \) (from \( Q \) in the first box, first schema; from \( R \) in the second, second schema), and the \( \rulename{\wedge I} \) lines cite the line holding \( P \) first, since \( P \) is now the left conjunct of the goal. That derivation is the second one of @prp-distributivity.

**Marking scheme.** (10 points)

- 2: splits on the premise by \( \rulename{\vee E} \), with two boxes opened by its two sides.
- 2: in each box, takes the assumption apart by \( \rulename{\wedge E} \) into both conjuncts.
- 2: in each box, uses \( \rulename{\vee I} \) to build \( P \vee R \) from the side in hand, with the correct schema.
- 2: in each box, builds the goal by \( \rulename{\wedge I} \), so that both boxes end in the same line, the goal.
- 2: the \( \rulename{\vee E} \) line cites the disjunction and both boxes as ranges, and the final sentences name the changed steps (the \( \rulename{\vee I} \) lines, now building \( Q \vee R \), and the order of the \( \rulename{\wedge I} \) citations).

Fatal errors (0 for the step): a line in one box citing a line of the other box; a conclusion drawn inside one box only and then used outside it.

A second route is also correct: split the premise twice, once ending both boxes in \( P \vee R \) and once ending both in \( Q \), and then join the two results by \( \rulename{\wedge I} \) outside every box (14 lines). Its points map as follows: 2 for either split with two boxes opened by the premise's sides; 2 for the \( \rulename{\wedge E} \) lines in the boxes; 2 for the \( \rulename{\vee I} \) sides; 2 for the final \( \rulename{\wedge I} \), with the boxes of each split ending in the same line; 2 for the citations and the final sentences.
:::

::: {#exr-disjunction-and-cases-c4}
[C4: The second half]

A search for \( Q \vee R, \ Q \to (P \to S), \ R \to S \vdash P \to S \) has written the premises and opened one box; the rest is blank. The finished derivation has 11 lines. *Name the move, then complete it.*

```{=latex}
% schema
\begin{center}
$\begin{nd}
  \hypo {1} {Q \vee R}
  \hypo {2} {Q \to (P \to S)}
  \hypo {3} {R \to S}
  \open
  \hypo {4} {P}
  \have[\ ][0] {} {\vdots}
  \close
\end{nd}$
\end{center}
```
:::

::: {.solution}
[Hint 1]

Inside the box, what is the current goal, and which available line is a disjunction?
:::

::: {.solution}
[Hint 2]

Inside the box the goal is \( S \), and no available line gives \( S \) at once. What can you do with the one disjunction available?
:::

::: {.solution}
The moves are two. First, the box of line 4 was read off the goal: \( P \to S \) is an implication, so the box opened with \( P \), and its current goal is \( S \); it will be closed by \( \rulename{{\to}I} \). Second, inside it, the available disjunction \( Q \vee R \) (line 1, in no box, so available inside the box) is split, and **both case boxes end in the current goal \( S \)**. In the case \( Q \), line 2 fires to give \( P \to S \), which fires on line 4; in the case \( R \), line 3 fires.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {Q \vee R}
  \hypo {2} {Q \to (P \to S)}
  \hypo {3} {R \to S}
  \open
  \hypo {4} {P}
  \open
  \hypo {5} {Q}
  \have {6} {P \to S} \ie{2,5}
  \have {7} {S} \ie{6,4}
  \close
  \open
  \hypo {8} {R}
  \have {9} {S} \ie{3,8}
  \close
  \have {10} {S} \oe{1,5-7,8-9}
  \close
  \have {11} {P \to S} \ii{4-10}
\end{nd}$
\end{center}
```

Line 7 cites line 4, the assumption of the outer box, which contains line 7. Line 10 is a line of the box \( \lines{4}{10} \) itself (the case boxes have closed), so \( \rulename{{\to}I} \) may cite that box at line 11. Splitting outside the box instead, with both case boxes ending in \( P \to S \), is also a correct derivation of the sequent; it does not complete the lines given, because it would split before line 4, not after.
:::

### R. Review

::: {#exr-disjunction-and-cases-r1}
[R1]

Let \( f \) be a function and \( [a, b] \) an interval. Take the atomic statements \( C \): "\( f \) is continuous on \( [a, b] \)", \( B \): "\( f \) is bounded on \( [a, b] \)" and \( I \): "\( f \) is integrable on \( [a, b] \)"; you need not know what the words mean. Translate the argument "If \( f \) is continuous on \( [a, b] \) and bounded there, then \( f \) is integrable on \( [a, b] \). \( f \) is bounded on \( [a, b] \). \( f \) is continuous on \( [a, b] \). So \( f \) is integrable on \( [a, b] \) and bounded there." into a sequent, and derive it.
:::

::: {.solution}
The sequent is \( (C \wedge B) \to I, \ B, \ C \vdash I \wedge B \): three premises and a conclusion, as in @def-sequent. The goal is a conjunction, so it splits into the subgoals \( I \) and \( B \). \( B \) is a premise. The only line that mentions \( I \) is the first premise, whose hypothesis \( C \wedge B \) is built by \( \rulename{\wedge I} \) (@def-rules-conjunction) from two premises; then \( \rulename{{\to}E} \) (@def-rule-implication-elimination) gives \( I \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(C \wedge B) \to I}
  \hypo {2} {B}
  \hypo {3} {C}
  \have {4} {C \wedge B} \ai{3,2}
  \have {5} {I} \ie{1,4}
  \have {6} {I \wedge B} \ai{5,2}
\end{nd}$
\end{center}
```

Line 4 cites line 3 first, so that \( C \) is the left conjunct, as in the hypothesis of line 1; the hypothesis must match exactly. Line 2 is cited twice, at lines 4 and 6: a line is not used up by being cited.
:::

::: {#exr-disjunction-and-cases-r2}
[R2]

Show that \( (P \to Q) \wedge (Q \to R), \ P \wedge S \vdash R \wedge S \), and say in one sentence which step you found by working backwards from the goal.
:::

::: {.solution}
Premise-directed, both premises are conjunctions and are taken apart by \( \rulename{\wedge E} \) (@def-rules-conjunction); goal-directed, the goal \( R \wedge S \) splits into \( R \) and \( S \), and \( S \) is already in hand. For \( R \), work backwards as in @exm-implication-chains: \( Q \to R \) is available, so \( Q \) becomes the subgoal; \( P \to Q \) is available, so \( P \) does; and \( P \) is in hand.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \to Q) \wedge (Q \to R)}
  \hypo {2} {P \wedge S}
  \have {3} {P \to Q} \ae{1}
  \have {4} {Q \to R} \ae{1}
  \have {5} {P} \ae{2}
  \have {6} {S} \ae{2}
  \have {7} {Q} \ie{3,5}
  \have {8} {R} \ie{4,7}
  \have {9} {R \wedge S} \ai{8,6}
\end{nd}$
\end{center}
```

The chain of lines 7 and 8 was found backwards, from the subgoal \( R \) to \( Q \) to \( P \), and written forwards.
:::

::: {#exr-disjunction-and-cases-r3}
[R3]

Is \( \vdash (P \wedge (P \to Q)) \to (Q \vee R) \)? Justify your answer.
:::

::: {.solution}
Yes. The goal's main connective is the outer \( \to \), so the move is to open a box with its hypothesis \( P \wedge (P \to Q) \) (@def-rules-implication). Inside, the current goal is \( Q \vee R \), which we postpone. The assumption is a conjunction, so \( \rulename{\wedge E} \) gives \( P \) and \( P \to Q \); \( \rulename{{\to}E} \) gives \( Q \); now the left side of the goal is in hand, and \( \rulename{\vee I} \) (@def-rule-disjunction-introduction) takes it.

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {P \wedge (P \to Q)}
  \have {2} {P} \ae{1}
  \have {3} {P \to Q} \ae{1}
  \have {4} {Q} \ie{3,2}
  \have {5} {Q \vee R} \oi{4}
  \close
  \have {6} {(P \wedge (P \to Q)) \to (Q \vee R)} \ii{1-5}
\end{nd}$
\end{center}
```

The derivation has no premises, so it shows \( \vdash (P \wedge (P \to Q)) \to (Q \vee R) \). The look-alike start fails: the statement contains \( \vee \), and one might begin with \( \rulename{\vee I} \) on the whole goal. But the goal's main connective is \( \to \), not \( \vee \), so \( \rulename{\vee I} \) cannot produce it; and even inside the box, choosing a side of \( Q \vee R \) before \( Q \) is on a line would have left the subgoal \( R \), which nothing supplies.
:::

<!-- dependency ledger
exm-abs-at-least-x (example): x >= 0 or x < 0; |x| = x for x >= 0 (definition of |x|); if x < 0 then |x| = -x > 0 > x; |x| >= x is (|x| > x) or (|x| = x) | school algebra, taken as known (blueprint, Allowed prerequisites), stated in prose before the example; ch11 (promised); the unfolding of >= is Section 1.1
exm-abs-product-cases (example): every real a satisfies a >= 0 or a < 0; sign rules for products; |a| = -a for a <= 0 | school algebra, taken as known; stated in prose before exm-abs-at-least-x; ch11 (promised)
exm-triangle-inequality-cases (example): adding two inequalities of the same direction; -a <= 0 <= a for a >= 0 | school algebra, taken as known; ch11 (promised)
exm-cases-on-hypothesis (example): an integer of the form 4k + 1 or 4k + 3 is odd (a reading, not a step) | school fact; ch07 (promised)
prp-distributivity (example): the reading with x != 0, x > 0, x < 0; "and" and "or" become intersection and union in the laws of sets | school algebra; the set reading is a prose pointer only, nothing depends on it
exr-disjunction-and-cases-a1 (solution): n^2 + n = n(n + 1); every integer is even or odd; t >= 0 or t < 0; t^2 >= 0; 1^2 = 1 is odd | school facts; ch07 (promised) for even or odd; ch11 (promised)
exr-disjunction-and-cases-a1 (solution): (d) a derivation never leads from true premises to a false conclusion | ch03 (promised), flagged in the text as proved there; the answer (line 5) does not use it
exr-disjunction-and-cases-b2 (solution): a >= b or a < b; dividing an inequality by 2 > 0; adding inequalities | school algebra, taken as known; ch11 (promised)
exr-disjunction-and-cases-b3 (solution): every integer is even or odd (stated in the item); n = 2k or n = 2k + 1 with k an integer (naming k is a quantifier step, Chapter 4) | stated in the item; school fact; ch07 (promised)
exr-disjunction-and-cases-c1 (solution): a >= b or a < b; |-a| = |a| | school algebra; |-a| = |a| proved inline by cases
exr-disjunction-and-cases-c2 (solution): order facts for x, y < 0 | school algebra, taken as known; ch11 (promised)
-->
