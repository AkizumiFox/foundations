# Or, Introduced

Sections 1.3 to 1.5 gave the rules for "and" and "implies". With them we can take a conjunction apart, fire an implication on its hypothesis, and prove an implication by opening a box. This section starts on the third connective of the chapter, "or". It gives the rule that **proves** a disjunction, \( \rulename{\vee I} \), and a habit that goes with it: when the goal is a disjunction, commit to one of its sides only when that side is in hand. Near its end it meets a goal that the rules still cannot reach, and that goal is the question the next section answers.

## Throwing information away on purpose

Suppose a proof has just shown that a real number \( x \) satisfies \( x > 0 \), and the definition it is checking asks for \( x \ge 0 \). Every writer takes the step "so \( x \ge 0 \)" without a pause. Look at what the step does. Section 1.1 noted that the symbol \( \le \) hides a disjunction, so \( x \ge 0 \) is the statement
\[
(x > 0) \vee (x = 0) .
\]
The step turns a statement into a disjunction of which it is one side.

The step loses something. "\( x > 0 \)" tells us that \( x \) is not \( 0 \); "\( x \ge 0 \)" no longer does. A proof that takes the step throws information away, and it does so on purpose: the definition asks for the weaker statement, and the stronger one is not in the form it asks for.

The same move appears whenever a known fact has a disjunction as its hypothesis. School algebra says that if \( a = 0 \) or \( b = 0 \), then \( a \cdot b = 0 \). To use this on a product whose first factor we know to be \( 0 \), we must hand the fact its hypothesis, "\( a = 0 \) or \( b = 0 \)". What we have is only "\( a = 0 \)". So again the step goes from one side to the whole disjunction, and only then does the fact fire.

Both steps are instances of one rule. This section states it as a pattern, reads the pattern clause by clause, and then uses it in two ways: when the goal is a disjunction, and when a premise needs one.

## The rule of or-introduction

*To prove a disjunction, it is enough to prove one of its two sides.*

The rule is defined, like every rule since Section 1.3, by its schema (@def-rule-schema). The Greek letters stand for arbitrary statements, and \( i \), \( k \) for line numbers. The rule has two forms, one for each side, so it is printed as two schemas.

::: {#def-rule-disjunction-introduction}
[Or-Introduction]

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
\end{center}
```

The rule given by these two schemas is called \( \rulename{\vee I} \) (**or-introduction**).
:::

In words, clause by clause.

- **One given line.** Line \( i \) holds a statement \( \varphi \), which may be any statement at all, and it must be available at line \( k \), in the sense of the scope rule of @def-derivation: an earlier line, not inside a box that has already closed. The justification "\( \rulename{\vee I} \) \( i \)" cites that one line. There is no box: \( \rulename{\vee I} \) is a one-step rule, like \( \rulename{\wedge E} \) and \( \rulename{{\to}E} \).
- **Either side.** The new line is a disjunction with \( \varphi \) as one of its two sides: on the left in the first schema, on the right in the second. Both forms have the same name, and the justification does not say which was used; the shape of the new line shows it.
- **Any other side.** The letter \( \psi \) appears in no given line. It stands for **any statement at all**. It need not be true, it need not have been mentioned before, and it need not have anything to do with \( \varphi \). This is the rule's one surprising clause. No earlier rule has it: \( \rulename{\wedge I} \), \( \rulename{\wedge E} \), \( \rulename{{\to}E} \), and \( \rulename{{\to}I} \) all build their new line out of statements that already stand on the lines or boxes they cite.
- **Consistent replacement.** As @def-rule-schema requires, \( \varphi \) is replaced by the whole cited statement, symbol for symbol. If line 3 is \( P \wedge Q \), then \( \rulename{\vee I} \) 3 may write \( (P \wedge Q) \vee R \), with \( \varphi \) replaced by \( P \wedge Q \) and \( \psi \) by \( R \). The brackets matter: the main connective of the new line (@def-main-connective) must be the \( \vee \) that the rule introduces.

Here is an instance. Let \( x \) be a real number, and suppose line 4 of some derivation is \( x > 0 \). Then each of the lines
\[
(x > 0) \vee (x = 0), \qquad (x = 0) \vee (x > 0), \qquad (x > 0) \vee (x < -7)
\]
may be written as a later line, justified by "\( \rulename{\vee I} \) 4". The first and third use the first schema, with \( \psi \) replaced by \( x = 0 \) and by \( x < -7 \); the second uses the second schema. The third line is silly, and it is correct: it is true whenever line 4 is, and nothing in the rule asks the added side to be useful.

The degenerate case is \( \psi \) equal to \( \varphi \). From \( P \) the rule writes \( P \vee P \), and then the two schemas give the same line. It is a legal step, and the next section uses the statement \( P \vee P \) once.

Now three nonexamples, each a small change of an instance. Take line 1 to be the statement named in each, and line 2 the line shown.

- From \( P \), the line "\( P \wedge Q \) — \( \rulename{\vee I} \) 1" is not an instance. The new line of \( \rulename{\vee I} \) is a disjunction, and the main connective of \( P \wedge Q \) is \( \wedge \).
- From \( Q \vee P \), the line "\( P \vee Q \) — \( \rulename{\vee I} \) 1" is not an instance. With \( \varphi \) replaced by \( Q \vee P \), the two schemas give \( (Q \vee P) \vee \psi \) and \( \psi \vee (Q \vee P) \). In both, the cited statement is one whole side of the new line, and \( Q \vee P \) is not a side of \( P \vee Q \). Whether \( P \vee Q \) follows from \( Q \vee P \) at all is the question at the end of this section.
- From \( P \vee Q \), the line "\( P \) — \( \rulename{\vee I} \) 1" is not an instance. It runs the rule backwards, from a disjunction to one of its sides.

**Why this rule.** In mathematics "or" is inclusive (Section 1.1): \( \varphi \vee \psi \) is true when \( \varphi \) is true, when \( \psi \) is true, and when both are. So \( \varphi \vee \psi \) is true whenever \( \varphi \) is, whatever \( \psi \) says. The rule is this first clause read as a permission. It is also the only rule of the chapter so far whose new line is a disjunction built on the spot. The other rules can produce a disjunction only by copying a line that already is one (\( \rulename{R} \)), or by cutting one out of a bigger line, as \( \rulename{\wedge E} \) cuts a side out of a conjunction and \( \rulename{{\to}E} \) the conclusion out of an implication. That is why, below, every derivation that needs a disjunction it cannot cut out of a line reaches for \( \rulename{\vee I} \).

**Why it is safe.** If the given line is true, the new line is true, whatever \( \psi \) is, by the inclusive reading. What the step loses is information: a reader of \( \varphi \vee \psi \) can no longer tell which side holds. Chapter 3 proves that derivations built from the rules of this chapter and the next never lead from true premises to a false conclusion (@thm-soundness); for \( \rulename{\vee I} \) the reason is the sentence just given.

*\( \rulename{\vee I} \) loses information, never truth.*

::: {.warning}
\( \rulename{\vee I} \) runs one way only. From \( \varphi \) it gives \( \varphi \vee \psi \); from \( \varphi \vee \psi \) it gives nothing, and in general \( \varphi \) does not follow from \( \varphi \vee \psi \) at all. The phrase "in particular" belongs to \( \rulename{\wedge E} \), not to "or". For a concrete failure, let \( x \) be a real number: "\( x \ge 0 \) or \( x < 0 \)" is true whatever \( x \) is, and "in particular \( x \ge 0 \)" is false at \( x = -1 \).
:::

::: {.warning}
Do not read "or" as "one but not both" when checking a step. From \( x = 2 \), \( \rulename{\vee I} \) gives "\( x = 2 \) or \( x \le 5 \)", although at \( x = 2 \) both sides are true. The step is correct: the disjunction is inclusive, and the rule never claims that the added side is false.
:::

::: {.check}
Let \( x \) be a real number, and suppose line 1 of a derivation is \( x = 2 \). Which of the following may line 2 be, justified by one application of \( \rulename{\vee I} \) to line 1?

::: {.enumerate options="label=(\roman*)"}
1. \( (x = 2) \vee (x = 3) \).
2. \( (x = 3) \vee (x = 2) \).
3. \( (x = 2) \vee (1 = 0) \).
4. \( x \ge 2 \).
:::
:::

::: {.solution}
(i) Yes, by the first schema, with \( \psi \) replaced by \( x = 3 \). (ii) Yes, by the second schema. (iii) Yes, by the first schema, with \( \psi \) replaced by the false statement \( 1 = 0 \). The line is true, since its left side is, and it is useless; the rule allows it. (iv) Only once \( x \ge 2 \) is written out as \( (x > 2) \vee (x = 2) \), the disjunction that the symbol \( \ge \) hides (Section 1.1). In that form it is an instance of the second schema, with \( \varphi \) replaced by \( x = 2 \). A checker who matches symbols sees the difference, which is why a derivation writes the disjunction out.
:::

## A disjunction as a goal

Section 1.3 asked two questions before writing any line: *what is the goal's main connective?* (goal-directed reasoning, from the bottom up) and *what are the available lines' main connectives?* (premise-directed reasoning, from the top down). Each rule so far added an answer. A conjunction as a goal splits into two subgoals, both needed (\( \rulename{\wedge I} \)); an implication as a goal opens a box (\( \rulename{{\to}I} \), @def-rules-implication).

Now \( \vee \) joins the list of goals. If the goal is \( \varphi \vee \psi \), its last line can be \( \rulename{\vee I} \), and then the subgoal is \( \varphi \) **or** \( \psi \): one of the two, of our choosing. That choice is new. A conjunction's two subgoals are both needed, so there is nothing to choose; here only one side is needed, and a wrong choice can leave us working towards a statement that does not follow from what we have. A goal \( P \vee Q \) from the premise \( Q \) shows the danger in miniature: choose \( P \), and the new subgoal \( P \) cannot be reached from \( Q \) at all: with \( P \) false and \( Q \) true, a derivation would lead from a true premise to a false conclusion, and Chapter 3 proves that no derivation does (@thm-soundness).

So the goal-directed step for \( \vee \) comes with a caution:

*Postpone a disjunction: choose a side of a goal \( \varphi \vee \psi \) only when that side is in hand.*

"In hand" means that the side stands on an available line, or is plainly one step away. Until then, work from the premises: take conjunctions apart, fire implications, open the boxes the goal asks for, and look at what appears. When one side of the goal turns up, the choice has been made for us.

Here are four derivations, in order of difficulty. Each Idea says, for each rule, whether it was chosen by the goal or by a premise.

::: {#exm-disjunction-introduction-derivations}
[Derivations with or-introduction]

Show that:

::: {.enumerate options="label=(\alph*)"}
1. \( P \vdash P \vee Q \), and \( P \vdash Q \vee P \);
2. \( P \wedge Q \vdash P \vee Q \);
3. \( P \to Q \vdash P \to (Q \vee R) \);
4. \( (P \wedge Q) \to R \vdash P \to (Q \to (R \vee S)) \).
:::
:::

::: {.solution}
(a) *Idea.* The goal is a disjunction, and one of its sides, \( P \), is the premise: in hand from the start. The only choice is which schema, and the goal decides it: \( P \) sits on the left of \( P \vee Q \) and on the right of \( Q \vee P \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \have {2} {P \vee Q} \oi{1}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {P}
  \have {2} {Q \vee P} \oi{1}
\end{nd}$
\end{center}
```

In the first, line 2 is the first schema with \( \varphi \) replaced by \( P \) and \( \psi \) by \( Q \); in the second, it is the second schema with the same replacement. The letter \( Q \) appears in no premise. That is the clause "any other side" at work.

(b) *Idea.* The goal \( P \vee Q \) is a disjunction, and neither side stands on a line yet, so we postpone it. Premise-directed: the premise's main connective is \( \wedge \), so \( \rulename{\wedge E} \) takes it apart. After that, **both** sides of the goal are in hand, and either choice finishes.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge Q}
  \have {2} {P} \ae{1}
  \have {3} {P \vee Q} \oi{2}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {P \wedge Q}
  \have {2} {Q} \ae{1}
  \have {3} {P \vee Q} \oi{2}
\end{nd}$
\end{center}
```

The left derivation chose the left side (first schema); the right one chose the right side (second schema). Both are correct, and the choice was free precisely because both sides were in hand. That will not usually be so.

(c) *Idea.* The goal's main connective is the outer \( \to \); the \( \vee \) sits inside its conclusion. Goal-directed: open a box with the hypothesis \( P \), and the new goal inside it is \( Q \vee R \), a disjunction, so we postpone it. Premise-directed: the premise \( P \to Q \) is an implication whose hypothesis \( P \) is now on a line, so \( \rulename{{\to}E} \) fires and gives \( Q \). The left side of the goal is in hand; \( \rulename{\vee I} \) takes it, and \( \rulename{{\to}I} \) closes the box.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \open
  \hypo {2} {P}
  \have {3} {Q} \ie{1,2}
  \have {4} {Q \vee R} \oi{3}
  \close
  \have {5} {P \to (Q \vee R)} \ii{2-4}
\end{nd}$
\end{center}
```

Line 3 cites line 1, which lies in no box, and line 2, the assumption of the box that contains line 3. Line 4 is a line of the box itself, so \( \rulename{{\to}I} \) may cite the box \( \lines{2}{4} \).

(d) *Idea.* The goal has two arrows at the top of its structure, \( P \to (Q \to \cdots) \), so, as in @prp-curry, we open two nested boxes, first \( P \), then \( Q \); the inner one will close first. The innermost goal is \( R \vee S \): postpone. Premise-directed: the only line that mentions \( R \) is the premise \( (P \wedge Q) \to R \). Its hypothesis is \( P \wedge Q \), which is not on any line, but both of its halves are: the two assumptions. So \( \rulename{\wedge I} \) builds it, \( \rulename{{\to}E} \) fires, and \( R \) is in hand. Then \( \rulename{\vee I} \), and the two boxes close.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge Q) \to R}
  \open
  \hypo {2} {P}
  \open
  \hypo {3} {Q}
  \have {4} {P \wedge Q} \ai{2,3}
  \have {5} {R} \ie{1,4}
  \have {6} {R \vee S} \oi{5}
  \close
  \have {7} {Q \to (R \vee S)} \ii{3-6}
  \close
  \have {8} {P \to (Q \to (R \vee S))} \ii{2-7}
\end{nd}$
\end{center}
```

This derivation uses every rule of the chapter so far except \( \rulename{\wedge E} \) and \( \rulename{R} \). Line 4 cites line 2, from the outer box, which is still open at line 4. Line 5 cites line 1 from inside two boxes: a line in no box is available everywhere below it. Line 7 is a line of the outer box itself, which is why \( \rulename{{\to}I} \) at line 8 may cite \( \lines{2}{7} \).
:::

Derivation (c) is where the habit of postponing pays. Suppose that, inside the box, we had committed at once to the goal's right side, planning to reach \( Q \vee R \) from \( R \). The box would then need \( R \) itself, from the premise \( P \to Q \) and the assumption \( P \) alone. The instance in the next warning makes both of these true and \( R \) false, so no derivation reaches \( R \) from them (a derivation never leads from true lines to a false one, which Chapter 3 proves: @thm-soundness). The plan was dead from its first step.

::: {.warning}
Choosing a side of a disjunctive goal too early turns a reachable goal into an unreachable one. In (c), the goal inside the box is \( Q \vee R \). A writer who opens with "we show \( R \)" has set out to prove, from \( P \to Q \) and \( P \), the statement \( R \); with \( x \) a real number, \( P \): "\( x > 2 \)", \( Q \): "\( x > 1 \)" and \( R \): "\( x > 3 \)", the premise and the assumption hold at \( x = 2.5 \), and \( R \) fails there. Keep the goal as the whole disjunction until one side appears on a line.
:::

## Manufacturing a hypothesis

In every derivation so far, \( \rulename{\vee I} \) produced the goal, or the goal of a box. It has a second use. A premise whose hypothesis is a disjunction can fire only when that disjunction stands on a line, **exactly** as written (the matching clause of @def-rule-implication-elimination). If one side of it is in hand, \( \rulename{\vee I} \) builds the whole hypothesis.

::: {#exm-or-hypothesis-split}
[A disjunctive hypothesis splits into two implications]

Show that \( (P \vee Q) \to R \vdash (P \to R) \wedge (Q \to R) \).
:::

::: {.solution}
*Idea.* Goal-directed: the goal is a conjunction, so \( \rulename{\wedge I} \) splits it into two subgoals, \( P \to R \) and \( Q \to R \), and each is an implication, so each gets its own box. Inside the box of \( P \), the goal is \( R \). Premise-directed: the only line that mentions \( R \) is the premise, and \( \rulename{{\to}E} \) on it needs its hypothesis \( P \vee Q \) on a line. We have \( P \), one side of that hypothesis. So \( \rulename{\vee I} \) manufactures \( P \vee Q \), and the premise fires. Here \( \rulename{\vee I} \) is chosen not because the goal is a disjunction (the goal is \( R \)) but because a premise's hypothesis is one. The box of \( Q \) is the same, with the other schema.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \vee Q) \to R}
  \open
  \hypo {2} {P}
  \have {3} {P \vee Q} \oi{2}
  \have {4} {R} \ie{1,3}
  \close
  \have {5} {P \to R} \ii{2-4}
  \open
  \hypo {6} {Q}
  \have {7} {P \vee Q} \oi{6}
  \have {8} {R} \ie{1,7}
  \close
  \have {9} {Q \to R} \ii{6-8}
  \have {10} {(P \to R) \wedge (Q \to R)} \ai{5,9}
\end{nd}$
\end{center}
```

Line 3 uses the first schema of @def-rule-disjunction-introduction (\( P \) on the left), line 7 the second (\( Q \) on the right). Both produce the same statement \( P \vee Q \), the one the premise asks for. The two boxes are separate: the second opens after the first has closed, and nothing in it cites a line of the first. Line 10 cites lines 5 and 9, which lie in no box.
:::

This is the first place in this section where \( \rulename{\vee I} \) manufactures the hypothesis of a premise, and it will not be the last: the product example below, and several exercises, do the same. Weakening is how a strong fact is fed to a rule, or a theorem, that asks for a weaker one.

In mathematical terms, the derivation says that a theorem with a hypothesis "\( P \) or \( Q \)" splits into two theorems. Let \( x \) be a real number, and suppose we know "if \( x \ge 0 \), then \( x^3 \ge 0 \)", that is, "if \( x > 0 \) or \( x = 0 \), then \( x^3 \ge 0 \)". Then we know "if \( x > 0 \), then \( x^3 \ge 0 \)" and "if \( x = 0 \), then \( x^3 \ge 0 \)". The way back, from the two implications to the single one with the disjunctive hypothesis, needs the rule of the next section; it is derived there.

::: {.check}
In the derivation of @exm-or-hypothesis-split, line 3 could not have been skipped by letting line 4 cite line 2 directly, as "\( R \) — \( \rulename{{\to}E} \) 1, 2". Why not?
:::

::: {.solution}
\( \rulename{{\to}E} \) (@def-rule-implication-elimination) needs the implication on one cited line and its hypothesis, exactly, on the other. The hypothesis of line 1 is \( P \vee Q \), and line 2 is \( P \), which does not match it symbol for symbol. Line 3 writes the hypothesis out, and only then does line 1 fire.
:::

## A goal we cannot reach yet

The most obvious fact about "or" is that the order of its sides does not matter: \( P \vee Q \vdash Q \vee P \). Try to derive it with the rules so far.

The goal \( Q \vee P \) is a disjunction, so we postpone it and look at the premise. Its main connective is \( \vee \), and no rule so far takes a disjunction apart. \( \rulename{\wedge E} \) needs a conjunction and \( \rulename{{\to}E} \) an implication; \( \rulename{\wedge I} \), \( \rulename{\vee I} \), and \( \rulename{R} \) may cite \( P \vee Q \), but only to copy it or to build something larger around it. So the premise gives us nothing, and neither side of the goal ever comes into hand.

We can get this far, though. Each side of the premise, **assumed** in a box, leads to the goal:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \open
  \hypo {2} {P}
  \have {3} {Q \vee P} \oi{2}
  \close
  \have {4} {P \to (Q \vee P)} \ii{2-3}
  \open
  \hypo {5} {Q}
  \have {6} {Q \vee P} \oi{5}
  \close
  \have {7} {Q \to (Q \vee P)} \ii{5-6}
\end{nd}$
\end{center}
```

This is a correct derivation, with a disappointing last line: it shows \( P \vee Q \vdash Q \to (Q \vee P) \), and line 1 is never cited. (A derivation need not use every premise, @def-derivable.) What we would like is to put the three lines 1, 4, and 7 together: *one of \( P \), \( Q \) holds, and either one leads to \( Q \vee P \); so \( Q \vee P \)*. That is a proof by cases, and none of the rules so far performs it. With them we cannot find a derivation of \( P \vee Q \vdash Q \vee P \).

The missing move is to **use** a disjunction, as \( \rulename{\wedge E} \) uses a conjunction and \( \rulename{{\to}E} \) uses an implication. The next section gives the rule that does this, and with it the six-line derivation that this attempt lacks.

## How this looks in a mathematical proof

In written mathematics \( \rulename{\vee I} \) is almost always silent. Here are the two steps of the opening, written out as derivations.

::: {#exm-product-zero}
[A product with a zero factor]

Let \( a \) and \( b \) be real numbers, and take as known the school fact "if \( a = 0 \) or \( b = 0 \), then \( a \cdot b = 0 \)". Prove that if \( a = 0 \), then \( a \cdot b = 0 \), naming the rule behind each step. Then write the step from \( x > 0 \) to \( x \ge 0 \) as a derivation.
:::

::: {.solution}
The goal is an implication, so the proof supposes \( a = 0 \) (a box). Inside, the fact needs its hypothesis "\( a = 0 \) or \( b = 0 \)", which \( \rulename{\vee I} \) manufactures, as in @exm-or-hypothesis-split. In prose, with each step's rule in brackets:

> Suppose \( a = 0 \). Then \( a = 0 \) or \( b = 0 \) \( [\rulename{\vee I}] \). So, by the school fact, \( a \cdot b = 0 \) \( [\rulename{{\to}E}] \). Hence, if \( a = 0 \), then \( a \cdot b = 0 \) \( [\rulename{{\to}I}] \).

As a derivation, with the school fact as the premise:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(a = 0 \vee b = 0) \to a \cdot b = 0}
  \open
  \hypo {2} {a = 0}
  \have {3} {a = 0 \vee b = 0} \oi{2}
  \have {4} {a \cdot b = 0} \ie{1,3}
  \close
  \have {5} {a = 0 \to a \cdot b = 0} \ii{2-4}
\end{nd}$
\end{center}
```

A written proof would say "if \( a = 0 \), then \( a \cdot b = 0 \) by the fact", and leave out the words "\( a = 0 \) or \( b = 0 \)". The derivation shows what that sentence leaves out: a box, a weakening, and one use of the fact.

For the second step, let \( x \) be a real number with \( x > 0 \). Written out, \( x \ge 0 \) is \( (x > 0) \vee (x = 0) \), and the step is one application of the first schema:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {x > 0}
  \have {2} {(x > 0) \vee (x = 0)} \oi{1}
\end{nd}$
\end{center}
```

Line 2 is \( x \ge 0 \), written out.
:::

Every "so \( x \ge 0 \)" after \( x > 0 \), every "so \( \abs{t} \le 1 \)" after \( \abs{t} < 1 \), and every "so \( n \) is even or \( n > 5 \)" after "\( n \) is even" is this rule. A reader who checks a proof line by line should see it, even where the writer did not name it. It is a step that never leads from a truth to a falsehood, and it is also the step that explains why a conclusion can say less than the proof knew.

## What the rules sound like

Since Section 1.3, each rule has had a row in a table that pairs it with the sentence a written proof uses for it and, for readers who meet a proof assistant, with the Lean code that performs it. Here is the row for \( \rulename{\vee I} \); nothing later depends on the last column.

| Rule | You write | Lean |
|------|--------------------------------------|------------------------|
| \( \rulename{\vee I} \) | "So \( P \) or \( Q \) holds." | `left` (or `Or.inl hp`); `right` |

The phrase is different from the "in particular" of \( \rulename{\wedge E} \) on purpose. "In particular" announces that a part is being taken out of something bigger; "so \( P \) or \( Q \)" announces that something bigger, and weaker, is being built. Chapters 2 and 4 add rows for the remaining rules, and Chapter 5 turns the table into a dictionary between derivations and prose.

## Exercises

### A. Check your understanding

::: {#exr-disjunction-introduction-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Write the two schemas of @def-rule-disjunction-introduction from memory, and say which letter in them may stand for a statement that appears in no earlier line.
2. Which of the following sentences, taken from proofs about a real number \( x \) or real numbers \( a \), \( b \), use \( \rulename{\vee I} \)? For each of the others, name the rule it uses.
    - "We have \( x < 3 \), so \( x \le 3 \)."
    - "We found that \( a = 0 \). So \( a = 0 \) or \( b = 0 \), and therefore \( a \cdot b = 0 \)."
    - "Since \( 0 < x < 1 \), in particular \( x < 1 \)."
    - "Since \( \abs{x - 2} < 1 \) implies \( 1 < x < 3 \), and \( \abs{x - 2} < 1 \), we get \( 1 < x < 3 \)."
3. True or false, with a reason: \( \rulename{\vee I} \) may introduce a side that is false.
4. To show \( Q, \ (P \vee Q) \to (Q \to R) \vdash R \), which rule writes the first line after the premises, and what is that line? Why is that rule used, although the goal is not a disjunction?
:::
:::

::: {.solution}
(a) From a line \( i \) holding \( \varphi \), a line \( k \) holding \( \varphi \vee \psi \), justified "\( \rulename{\vee I} \) \( i \)"; and, from the same line, a line \( k \) holding \( \psi \vee \varphi \), with the same justification (@def-rule-disjunction-introduction). The letter \( \psi \) appears in no given line: it may be any statement.

(b) The first uses \( \rulename{\vee I} \): \( x \le 3 \) is \( (x < 3) \vee (x = 3) \), and its left side is in hand. The second uses \( \rulename{\vee I} \) to build "\( a = 0 \) or \( b = 0 \)" from its left side, and then \( \rulename{{\to}E} \) on the fact about products, as in @exm-product-zero. The third uses \( \rulename{\wedge E} \): \( 0 < x < 1 \) is \( (0 < x) \wedge (x < 1) \), and the sentence takes out its right half. The fourth uses \( \rulename{{\to}E} \), with the implication first and its hypothesis second.

(c) True. The added side \( \psi \) may be any statement, false ones included, as in the line \( (x = 2) \vee (1 = 0) \) of the Quick check after the definition. The new line is still true whenever the cited line is, because "or" is inclusive: one true side is enough.

(d) The rule is \( \rulename{\vee I} \), by its second schema, and line 3 is \( P \vee Q \), from line 1. It is used because a premise's hypothesis is a disjunction. The goal \( R \) occurs only in the premise \( (P \vee Q) \to (Q \to R) \), and \( \rulename{{\to}E} \) fires on that premise only when \( P \vee Q \) itself stands on a line. Only its right side \( Q \) is on a line, and \( \rulename{\vee I} \) turns it into \( P \vee Q \). Then \( Q \to R \) follows by \( \rulename{{\to}E} \) 2, 3, and \( R \) by \( \rulename{{\to}E} \) 4, 1. The move is the one of @exm-or-hypothesis-split, where \( \rulename{\vee I} \) builds a premise's hypothesis.
:::

### B. Practice

::: {#exr-disjunction-introduction-b1}
[B1: Committing to a side]

Show that \( P \wedge (Q \to R) \vdash Q \to (R \vee S) \), and that \( P \vdash (Q \vee P) \vee R \). For each derivation, say at which line you committed to a side of a disjunctive goal, and why that was safe.
:::

::: {.solution}
For the first, the goal is an implication, so open a box with \( Q \); the goal inside is \( R \vee S \), which we postpone. Premise-directed, \( \rulename{\wedge E} \) takes out \( Q \to R \), and \( \rulename{{\to}E} \) fires on the assumption \( Q \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge (Q \to R)}
  \open
  \hypo {2} {Q}
  \have {3} {Q \to R} \ae{1}
  \have {4} {R} \ie{3,2}
  \have {5} {R \vee S} \oi{4}
  \close
  \have {6} {Q \to (R \vee S)} \ii{2-5}
\end{nd}$
\end{center}
```

We committed at line 5, to the left side \( R \), and only after line 4 had put \( R \) on a line. The other conjunct of the premise, \( P \), is never used.

For the second, the goal \( (Q \vee P) \vee R \) is a disjunction whose left side, \( Q \vee P \), is itself a disjunction, and \( P \) is one side of that.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \have {2} {Q \vee P} \oi{1}
  \have {3} {(Q \vee P) \vee R} \oi{2}
\end{nd}$
\end{center}
```

Line 2 uses the second schema (\( P \) on the right) and line 3 the first, with \( \varphi \) replaced by \( Q \vee P \). We committed twice, at lines 2 and 3, and both times the side was in hand: at line 2 the side \( P \) was the premise, and at line 3 the side \( Q \vee P \) was line 2. Choosing the side \( R \) at the outer level would have left the subgoal \( R \), which the premise \( P \) cannot give.
:::

::: {#exr-disjunction-introduction-b2}
[B2: The last line]

A search for \( P \to Q, \ Q \to R \vdash P \to (S \vee R) \) has reached the stage below; only the last line is missing. *Name the move, then complete it.*

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {Q \to R}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {R} \ie{2,4}
  \have {6} {S \vee R} \oi{5}
  \close
  \have {7} {\;\textbf{?}} \by{?}{}
\end{nd}$
\end{center}
```
:::

::: {.solution}
The move is the one read off the goal: an implication goal opens a box with its hypothesis, and the box is closed by \( \rulename{{\to}I} \) once its last line is the implication's conclusion. The box opened with \( P \) at line 3, and its last line, line 6, is \( S \vee R \), the conclusion of the goal. So line 7 closes the box:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {Q \to R}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {R} \ie{2,4}
  \have {6} {S \vee R} \oi{5}
  \close
  \have {7} {P \to (S \vee R)} \ii{3-6}
\end{nd}$
\end{center}
```

Line 7 cites the box as the range \( \lines{3}{6} \), not its lines one by one. Inside the box, the disjunction \( S \vee R \) was postponed until \( R \) came into hand at line 5; the side in hand was the right one, so line 6 uses the second schema.
:::

::: {#exr-disjunction-introduction-b3}
[B3: A theorem with a weaker hypothesis]

Let \( x \) be a real number, and take as known the school fact "if \( x \ge 1 \), then \( x^2 \ge x \)". Prove that if \( x > 1 \), then \( x^2 \ge x \). Write the proof as a derivation whose premise is the school fact, with \( x \ge 1 \) written out as a disjunction, and then as two or three sentences of prose.
:::

::: {.solution}
Written out, \( x \ge 1 \) is \( (x > 1) \vee (x = 1) \), so the premise is an implication whose hypothesis is a disjunction. The goal is an implication: open a box with \( x > 1 \). Inside, \( \rulename{\vee I} \) manufactures the premise's hypothesis, and \( \rulename{{\to}E} \) fires.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(x > 1 \vee x = 1) \to x^2 \ge x}
  \open
  \hypo {2} {x > 1}
  \have {3} {x > 1 \vee x = 1} \oi{2}
  \have {4} {x^2 \ge x} \ie{1,3}
  \close
  \have {5} {x > 1 \to x^2 \ge x} \ii{2-4}
\end{nd}$
\end{center}
```

In prose: *Suppose \( x > 1 \). Then \( x \ge 1 \), so \( x^2 \ge x \) by the fact. Hence if \( x > 1 \), then \( x^2 \ge x \).* The words "then \( x \ge 1 \)" are line 3. For instance, at \( x = 3 \) the conclusion reads \( 9 \ge 3 \).
:::

### C. Going deeper

::: {#exr-disjunction-introduction-c1}
[C1: Which new rules are safe?]

Suppose someone proposes new rules for the derivations of this chapter. Let \( x \) be a real number.

::: {.enumerate options="label=(\alph*)"}
1. Take the rule "from \( \varphi \vee \psi \), write \( \varphi \)". Starting from the premise "\( x \ge 0 \) or \( x < 0 \)", which is true for every real \( x \), derive with it a line that is false at \( x = -1 \).
2. \( \rulename{\vee I} \) adds a side \( \psi \) that may be any statement at all. Explain why it can never lead from a true line to a false one.
3. Is the rule "from \( \varphi \), write \( \varphi \wedge \psi \), for any statement \( \psi \)" safe in the same sense? Justify your answer with an instance.
:::
:::

::: {.solution}
(a) With \( \varphi \) replaced by \( x \ge 0 \) and \( \psi \) by \( x < 0 \), the proposed rule turns the premise into the line \( x \ge 0 \). At \( x = -1 \) the premise is true, since \( -1 < 0 \), and the line \( -1 \ge 0 \) is false. So the rule can lead from a true line to a false one.

(b) Suppose the cited line \( \varphi \) is true. The new line \( \varphi \vee \psi \) (or \( \psi \vee \varphi \)) is true when at least one of its sides is true, because "or" is inclusive (Section 1.1), and its side \( \varphi \) is true. So the new line is true, whatever \( \psi \) is. The truth or falsity of \( \psi \) never enters.

(c) No. The new line \( \varphi \wedge \psi \) is true only when both sides are, and \( \psi \) is arbitrary. With \( \varphi \) replaced by \( x = -1 \) and \( \psi \) by \( x \ge 0 \), at \( x = -1 \) the cited line is true and the new line, "\( x = -1 \) and \( x \ge 0 \)", is false. The contrast with (b) is the whole difference between \( \vee \) and \( \wedge \): a disjunction needs one true side, so an arbitrary second side is harmless; a conjunction needs both, so it is not. That is why \( \rulename{\wedge I} \) asks for both sides on lines.

**Marking scheme.** (10 points)

- 3: (a) applies the proposed rule to the premise to get \( x \ge 0 \), and checks at \( x = -1 \) that the premise is true and the new line false.
- 3: (b) argues from the inclusive meaning of "or": one true side makes the disjunction true, whatever the other side is.
- 3: (c) answers no, with an instance in which \( \varphi \) is true and \( \varphi \wedge \psi \) is false.
- 1: (c) names the difference: a conjunction needs both sides true.

Fatal errors (0 for the step): in (a), a premise that is false at \( x = -1 \); in (b), an argument that assumes \( \psi \) is true; in (c), "safe" on the grounds that \( \varphi \) is true.
:::

::: {#exr-disjunction-introduction-c2}
[C2: Predicting the manufacture]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( (P \vee Q) \to (R \wedge S) \vdash P \to S \).
2. Show that \( (P \vee Q) \to R \vdash (P \wedge Q) \to R \).
3. In each derivation, which rule built the hypothesis of the premise? Could you have predicted, from the premise's main connective and the shape of its hypothesis alone, that this rule would be needed?
:::
:::

::: {.solution}
(a) The goal is an implication: open a box with \( P \); the goal inside is \( S \). The only line mentioning \( S \) is the premise, whose conclusion \( R \wedge S \) contains it; to use the premise, \( \rulename{{\to}E} \) needs \( P \vee Q \), built from \( P \) by \( \rulename{\vee I} \). Then \( \rulename{\wedge E} \) takes out \( S \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \vee Q) \to (R \wedge S)}
  \open
  \hypo {2} {P}
  \have {3} {P \vee Q} \oi{2}
  \have {4} {R \wedge S} \ie{1,3}
  \have {5} {S} \ae{4}
  \close
  \have {6} {P \to S} \ii{2-5}
\end{nd}$
\end{center}
```

(b) The goal is an implication: open a box with \( P \wedge Q \); the goal inside is \( R \). The premise fires on \( P \vee Q \). The assumption gives \( P \) by \( \rulename{\wedge E} \), and \( \rulename{\vee I} \) builds \( P \vee Q \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \vee Q) \to R}
  \open
  \hypo {2} {P \wedge Q}
  \have {3} {P} \ae{2}
  \have {4} {P \vee Q} \oi{3}
  \have {5} {R} \ie{1,4}
  \close
  \have {6} {(P \wedge Q) \to R} \ii{2-5}
\end{nd}$
\end{center}
```

Taking \( Q \) at line 3 instead, and building \( P \vee Q \) by the second schema, works equally well.

(c) In both, \( \rulename{\vee I} \) built the hypothesis (line 3 in (a), line 4 in (b)), and in both it could be predicted. The premise's main connective is \( \to \), so the premise is used by \( \rulename{{\to}E} \), which needs its hypothesis \( P \vee Q \) on a line of its own, exactly. That disjunction occurs only inside the premise, as its hypothesis, and no rule takes the hypothesis out of an implication (\( \rulename{{\to}E} \) gives the conclusion). So it had to be built, and the only rule of the chapter so far that builds a disjunction is \( \rulename{\vee I} \). The one question left was which side would be in hand; in (b) the conjunction \( P \wedge Q \) offered both.
:::

<!-- dependency ledger
def-rule-disjunction-introduction (example): "or" is inclusive; x >= 0 is (x > 0) or (x = 0), and <= hides a disjunction | Section 1.1 (the connective table and the warning on inclusive "or", prose, no label)
def-rule-disjunction-introduction (example): if the cited line is true, the new line of or-I is true; no rule leads from true lines to a false one | argued inline from the inclusive reading; general soundness ch03 (promised)
def-rule-disjunction-introduction (example): the warning's witnesses x = -1 (x >= 0 or x < 0) and x = 2.5 (P: x > 2, Q: x > 1, R: x > 3) | school algebra; ch11 (promised)
exm-or-hypothesis-split (example): if x >= 0 then x^3 >= 0 | school algebra, used only as a reading; ch11 (promised)
exm-product-zero (example): if a = 0 or b = 0, then a * b = 0 | school algebra, taken as known in the example; ch11 (promised)
exr-disjunction-introduction-a1 (solution): |x - 2| < 1 implies 1 < x < 3; 0 < x < 1 abbreviates (0 < x) and (x < 1) | school algebra; Section 1.1 (chained inequalities)
exr-disjunction-introduction-b3 (solution): if x >= 1 then x^2 >= x | school algebra, taken as known in the item; ch11 (promised)
exr-disjunction-introduction-c1 (solution): x >= 0 or x < 0 for every real x | school algebra, stated in the item; ch11 (promised)
-->
