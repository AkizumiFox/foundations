# Proof by Contradiction and the Classical Rules

Every rule so far either builds a statement or takes one apart. The rules for negation are no exception: \( \rulename{\neg I} \) (@def-rules-negation) builds \( \neg\varphi \) from a box that opens with \( \varphi \) and ends in \( \bot \), and \( \rulename{\neg E} \) (@def-rules-contradiction) uses \( \neg\varphi \) against \( \varphi \). Yet in three places this chapter has stopped one step short of a goal. This section adds the one rule that takes a negation away, reductio ad absurdum. It then derives from it the classical laws that mathematics uses without noticing, and shows that three of them are one principle in three forms.

## Two boxes that look alike

Here are two arguments that a mathematician would both call "proof by contradiction".

The first is the proof of @thm-sqrt2-irrational. It fixes a rational number \( r \), supposes \( r^2 = 2 \), reaches a contradiction, and concludes that \( r^2 \ne 2 \). In the language of @def-rules-negation, it opens a box with the assumption \( P \) ("\( r^2 = 2 \)"), reaches \( \bot \) inside it, and closes the box to get \( \neg P \). That is \( \rulename{\neg I} \).

The second is about a real number.

::: {#exm-raa-at-most-one}
[A number whose square is at most itself]

Let \( x \) be a real number with \( x^2 \le x \). Prove that \( x \le 1 \).
:::

::: {.solution}
Suppose, for a contradiction, that \( x \le 1 \) fails, that is, \( x > 1 \). Then \( x > 0 \), and multiplying \( x > 1 \) by \( x \) gives \( x^2 > x \). This contradicts \( x^2 \le x \). Hence \( x \le 1 \).
:::

Look at its shape. The box opens with the assumption \( \neg P \), where \( P \) is "\( x \le 1 \)", reaches \( \bot \), and closes to give \( P \). If we tried to justify the last line by \( \rulename{\neg I} \), we would get the negation of the box's assumption, \( \neg\neg P \): "it is not the case that \( x \le 1 \) fails". That is not \( P \). The two arguments put their negations in different places. \( \rulename{\neg I} \) puts a \( \neg \) **into** the conclusion; the second argument takes one **out**.

## Where the rules so far stop short

The second argument is not a curiosity. Three times already in this chapter a derivation has stopped short in the same way: it reached a negation where the goal was not one.

1. Section 2.2 noted that a box opened with \( \neg(x > 0) \) and closed by \( \rulename{\neg I} \) gives \( \neg\neg(x > 0) \), and no rule so far gets from there to \( x > 0 \).
2. If you did Exercise C1 of Section 2.3, you met a second: @exr-derived-rules-c1 led from \( P \to Q \) and \( \neg P \to R \) to \( \neg(\neg Q \wedge \neg R) \), and not to \( Q \vee R \).
3. Section 2.4 noted, after @exm-iff-negations, that its converse, \( \neg P \leftrightarrow \neg Q \vdash P \leftrightarrow Q \), resists the rules so far. The natural box on \( \neg Q \), inside the box of \( P \), closes to \( \neg\neg Q \), not \( Q \).

Try the smallest case, \( P \) from \( \neg\neg P \). The goal \( P \) is a letter, so no introduction rule applies: the goal-directed moves have nothing to say. The premise \( \neg\neg P \) is a negation, and a negation can be used only by \( \rulename{\neg E} \), against the statement it negates, \( \neg P \). So we assume \( \neg P \) in a box. The box reaches \( \bot \) at once, and \( \rulename{\neg I} \) closes it with \( \neg\neg P \): the premise again. Every attempt goes round this circle.

That no derivation of \( P \) from \( \neg\neg P \) exists with the rules so far is a claim about **all** derivations, which no search can settle; this section's Looking-ahead box says where it is proved. Here we name the missing step and add it as a rule.

## Reductio ad absurdum

*To prove \( \varphi \), it is enough to show that "not \( \varphi \)" leads to a contradiction.*

::: {#def-rule-raa}
[Reductio ad Absurdum]

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \open
  \hypo {i} {\neg \varphi}
  \have {} {\vdots}
  \have {j} {\bot}
  \close
  \have {k} {\varphi} \raa{i-j}
\end{nd}$
\end{center}
```

This is the rule \( \rulename{RAA} \) (**reductio ad absurdum**, "reduction to the absurd"). The line \( \neg\varphi \) is an assumption, which opens the box and is **discharged** when the box closes. The line \( \bot \) is a line **of that box itself**, not of a box inside it.
:::

As in every schema (@def-rule-schema), \( \varphi \) stands for any statement and \( i, j, k \) for line numbers. This rule has conditions that matter; read each one.

1. **The assumption is the exact negation of the goal.** To prove \( \varphi \), the box opens with \( \neg\varphi \): the negation of the **whole** of \( \varphi \). If \( \varphi \) is \( Q \vee R \), the box opens with \( \neg(Q \vee R) \), not with \( \neg Q \vee R \). In a finished derivation this assumption is printed **"asm, for \( \rulename{RAA} \)"**; in prose it is the sentence "suppose, for a contradiction, that \( \varphi \) fails".
2. **The box must reach \( \bot \)**, as a line of the box itself: a \( \bot \) inside a smaller box depends on a further assumption, as in \( \rulename{\neg I} \).
3. **The result is \( \varphi \) itself**, not \( \neg\neg\varphi \), which \( \rulename{\neg I} \) would give from the same box. This clause is the whole content of the rule.
4. **The box closes**, its assumption is discharged, and the justification cites the box as a range \( \lines{i}{j} \).

In words: the box is a thought experiment in which \( \varphi \) fails. If the experiment ends in \( \bot \), then \( \varphi \) cannot fail, and \( \rulename{RAA} \) lets us write \( \varphi \). Set the new rule beside \( \rulename{\neg I} \):

| Rule | The box opens with | The box ends with | After the box |
|---|---|---|---|
| \( \rulename{\neg I} \) | \( \varphi \) | \( \bot \) | \( \neg\varphi \) |
| \( \rulename{RAA} \) | \( \neg\varphi \) | \( \bot \) | \( \varphi \) |

The rows differ only in where the \( \neg \) sits, and that makes \( \rulename{RAA} \) different in kind: every other primitive rule is the introduction or elimination rule of one connective (\( \rulename{\bot E} \) counts as the elimination rule of \( \bot \), and \( \rulename{R} \) is the repetition clause of @def-derivation), while \( \rulename{RAA} \) applies to every statement, whatever its main connective, even a letter.

In the Givens/Goal table, \( \rulename{RAA} \) adds \( \neg\varphi \) to the Givens and makes \( \bot \) the goal.

With the convention of Section 2.1, the argument of @exm-raa-at-most-one is this derivation.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {x^2 \le x}
  \open
  \hypo {2} {\neg (x \le 1)}
  \have {3} {x > 1} \by{algebra}{2}
  \have {4} {\neg (x^2 \le x)} \by{algebra}{3}
  \have {5} {\bot} \ne{1,4}
  \close
  \have {6} {x \le 1} \raa{2-5}
\end{nd}$
\end{center}
```

::: {.warning}
The assumption that opens an \( \rulename{RAA} \) box must be the **exact** negation of the goal. To prove \( x \le 1 \) by contradiction, assume \( x > 1 \), since for real numbers "not \( x \le 1 \)" says \( x > 1 \). Assuming \( x \ge 1 \) instead is a common slip. It is not the negation: \( x = 1 \) satisfies both \( x \le 1 \) and \( x \ge 1 \). A box opened with \( x \ge 1 \) cannot honestly reach \( \bot \) while \( x = 1 \) is possible, so a "contradiction" that seems to be reached hides an error.
:::

::: {.check}
A box opens with the assumption \( \neg(x < 0) \) and reaches \( \bot \), as a line of the box itself. Which of the following may be written after it closes, and by which rule? (i) \( x < 0 \); (ii) \( \neg\neg(x < 0) \); (iii) \( x \ge 0 \).
:::

::: {.solution}
(i) By \( \rulename{RAA} \): the box opened with the negation of \( x < 0 \). (ii) By \( \rulename{\neg I} \): \( \rulename{\neg I} \) writes the negation of the box's assumption, and the assumption is \( \neg(x < 0) \). (iii) By neither. For real numbers \( x \ge 0 \) says the same as \( \neg(x < 0) \), which is exactly the statement the box has refuted.
:::

::: {.check}
In the derivation of @exm-raa-at-most-one above, which line is the \( \rulename{RAA} \) step, which box does it cite, and what would \( \rulename{\neg I} \) have written there instead?
:::

::: {.solution}
Line 6 is the \( \rulename{RAA} \) step, and it cites the box \( \lines{2}{5} \). \( \rulename{\neg I} \) would have written \( \neg\neg(x \le 1) \).
:::

## The move: when stuck, assume the negation of the goal

Chapter 1 and Sections 2.1–2.4 built two lists of moves. From the goal: its main connective chooses an introduction rule and so a box or two subgoals. From the premises: each available line's main connective chooses the elimination rule that uses it, and a goal \( \bot \) asks for a clash. The new rule adds one move, for the moment when both lists are used up.

We are **stuck** at a gap when the goal-directed moves give nothing (the goal is a letter, or a disjunction with neither side in hand) and no premise-directed move brings the goal closer. Then open an \( \rulename{RAA} \) box on the negation of the goal. The new goal is \( \bot \), so we hunt for a clash, and the box has given us one more line to clash with: \( \neg\varphi \) itself.

*When stuck, assume the negation of the goal, and hunt for a clash.*

The move is a last resort, not a first one: try every other move first. Three of the derivations under the next heading reach the moment of being stuck, and their Ideas say where.

**When \( \rulename{RAA} \) earns its place.** Look ahead at where the classical step enters the derivations below: a goal that is a letter with nothing to build it (@prp-double-negation), and a disjunction neither of whose sides follows from what is available, each side's step breaking on its own (@prp-excluded-middle, De Morgan's law (d)). Premises that say little and a goal that decides something: that is where to expect \( \rulename{RAA} \). Exercise B6 meets a third such disjunction.

## Derivations with the new rule

**The stall, resolved.** The next result is the one on which we got stuck.

::: {#prp-double-negation}
[Double Negation]

For every statement \( P \):

::: {.enumerate options="label=(\alph*)"}
1. \( P \vdash \neg\neg P \), by a derivation that does not use \( \rulename{RAA} \);
2. \( \neg\neg P \vdash P \), by a derivation that uses \( \rulename{RAA} \).
:::
:::

::: {.idea}
In (a) the goal \( \neg\neg P \) is the negation of \( \neg P \), so the goal-directed move of Section 2.2 opens a \( \rulename{\neg I} \) box with \( \neg P \), and the premise clashes with it at once.

In (b) the goal \( P \) is a letter, so no introduction rule applies. The only premise is a negation, which can only clash; the attempt above showed that clashing it inside a \( \rulename{\neg I} \) box leads back to the premise. We are stuck, so we assume the negation of the goal: an \( \rulename{RAA} \) box on \( \neg P \). The premise clashes with it at once.
:::

::: {.proof}
(a) This is the derivation of @exm-double-negation-introduction (a), which uses the rules of @def-rules-negation alone; we repeat it to set it beside (b).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \open
  \hypo {2} {\neg P}
  \have {3} {\bot} \ne{1,2}
  \close
  \have {4} {\neg\neg P} \ni{2-3}
\end{nd}$
\end{center}
```

(b) An \( \rulename{RAA} \) box on \( \neg P \):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg\neg P}
  \open
  \hypo {2} {\neg P}
  \have {3} {\bot} \ne{2,1}
  \close
  \have {4} {P} \raa{2-3}
\end{nd}$
\end{center}
```

Line 3 applies \( \rulename{\neg E} \) to the statement \( \neg P \) on line 2 and to its negation \( \neg\neg P \) on line 1. This proves both parts.
:::

In both derivations, lines 2 and 3 form a box that opens with \( \neg P \) and reaches \( \bot \) by a clash with line 1. Only the rule that closes the box differs, and with it the last line. So the two directions are not mirror images: one needs only the rules for \( \neg \), and the derivation of the other uses the new rule.

::: {.second-reading title="Edge cases of reductio"}
**The degenerate case.** The smallest use of \( \rulename{RAA} \) proves \( P \) from \( P \).

::: {.idea}
There is nothing to find: the premise is the goal. The derivation is here only to show the rule at its smallest. The box opens with \( \neg P \), and the one line it needs, \( \bot \), comes from the clash of the assumption with the premise.
:::

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \open
  \hypo {2} {\neg P}
  \have {3} {\bot} \ne{1,2}
  \close
  \have {4} {P} \raa{2-3}
\end{nd}$
\end{center}
```

It is legal and pointless, since line 1 already is the goal. It is the purest case of a pattern that turns up in real proofs: a contradiction box whose assumption does nothing except clash with a line we already had. The warnings at the end of this section return to it.

**Nonexample by minimal change.** Change only the last line of (a), from \( \neg\neg P \) to \( P \), keeping the justification \( \rulename{\neg I}\ \lines{2}{3} \). Lines 1–3 still check. What fails is the conclusion of \( \rulename{\neg I} \), which must be the negation of the box's assumption, here \( \neg\neg P \). To write \( P \), the justification must be \( \rulename{RAA} \).
:::

From now on both parts are derived rules in the sense of @def-derived-rule. A line \( \neg\neg\varphi \) may be justified by "\( \rulename{\neg\neg I} \) \( i \)", citing a line \( \varphi \), and a line \( \varphi \) by "\( \rulename{\neg\neg E} \) \( i \)", citing a line \( \neg\neg\varphi \). The first stall of the list above is now one line: from \( \neg\neg(x > 0) \), \( \rulename{\neg\neg E} \) gives \( x > 0 \).

**Contraposition, backwards.** @prp-contrapositive derives \( \neg Q \to \neg P \) from \( P \to Q \) with the rules for \( \to \) and \( \neg \) alone. In practice we use it the other way round. To prove "if \( n^2 \) is even then \( n \) is even", one may prove "if \( n \) is not even then \( n^2 \) is not even", and the step from that back to the original goes from \( \neg Q \to \neg P \) to \( P \to Q \).

::: {#prp-contrapositive-converse}
[Converse of the Contrapositive]

For all statements \( P \) and \( Q \), \( \neg Q \to \neg P \vdash P \to Q \).
:::


::: {.idea}
The goal is an implication, so the goal-directed move opens a box with \( P \), and the new goal is \( Q \), a letter. The premise needs \( \neg Q \) before it gives anything, and \( \neg Q \) is nowhere; the box's assumption \( P \) is a letter and cannot be taken apart. We are stuck at \( Q \), so we assume its negation, \( \neg Q \). That is exactly what the premise wanted: \( \rulename{{\to}E} \) gives \( \neg P \), which clashes with the \( P \) of the outer box, and \( \rulename{RAA} \) closes the inner box with \( Q \).

In pictures: the stall at the letter \( Q \); then the \( \rulename{RAA} \) box on \( \neg Q \).

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {\neg Q \to \neg P}
  \open
  \hypo {2} {P}
  \have[\ ][0] {} {\vdots}
  \have[][6] {6} {Q}
  \close
  \have {7} {P \to Q} \ii{2-6}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {\neg Q \to \neg P}
  \open
  \hypo {2} {P}
  \open
  \hypo {3} {\neg Q}
  \have[\ ][0] {} {\vdots}
  \have[][5] {5} {\bot}
  \close
  \have {6} {Q} \raa{3-5}
  \close
  \have {7} {P \to Q} \ii{2-6}
\end{nd}$
\end{center}
```
:::

::: {.proof}
The derivation is:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg Q \to \neg P}
  \open
  \hypo {2} {P}
  \open
  \hypo {3} {\neg Q}
  \have {4} {\neg P} \ie{1,3}
  \have {5} {\bot} \ne{2,4}
  \close
  \have {6} {Q} \raa{3-5}
  \close
  \have {7} {P \to Q} \ii{2-6}
\end{nd}$
\end{center}
```

Line 5 may cite line 2 because line 2 lies in a box that is still open. \( \rulename{RAA} \) enters at line 6. This proves the proposition.
:::

So contraposition behaves like double negation: going from \( P \to Q \) to \( \neg Q \to \neg P \) needs no \( \rulename{RAA} \), and our derivation of the way back uses one \( \rulename{RAA} \).

**Excluded middle.** Every integer is even or odd. Every real number is \( \ge 0 \) or \( < 0 \). The purely logical form of such facts is the law \( P \vee \neg P \), which the next result derives from no premises at all.

::: {#prp-excluded-middle}
[Excluded Middle]

For every statement \( P \), \( \vdash P \vee \neg P \).
:::


::: {.idea}
The goal is a disjunction, so Section 1.5's move postpones it: choose a side only when that side is in hand. But there are no premises, so no premise-directed move applies, and neither side is worth aiming at: \( P \) false breaks the step to \( P \), and \( P \) true breaks the step to \( \neg P \). We are stuck, so we assume the negation of the whole goal, \( \neg(P \vee \neg P) \), which says that neither side holds, and hunt for a clash. The new line can clash only with \( P \vee \neg P \), which \( \rulename{\vee I} \) builds from either side. So we manufacture a side, as in @exm-manufactured-clash. If \( P \) held, then \( P \vee \neg P \) would hold, against the assumption; so \( \neg P \), by \( \rulename{\neg I} \). But then \( P \vee \neg P \) holds after all, and that is the final clash.

In pictures: the \( \rulename{RAA} \) box; then the final clash, written backwards.

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {\neg (P \vee \neg P)}
  \have[\ ][0] {} {\vdots}
  \have[][7] {7} {\bot}
  \close
  \have {8} {P \vee \neg P} \raa{1-7}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \open
  \hypo {1} {\neg (P \vee \neg P)}
  \have[\ ][0] {} {\vdots}
  \have[][5] {5} {\neg P}
  \have {6} {P \vee \neg P} \oi{5}
  \have {7} {\bot} \ne{6,1}
  \close
  \have {8} {P \vee \neg P} \raa{1-7}
\end{nd}$
\end{center}
```
:::

::: {.proof}
The derivation is:

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {\neg (P \vee \neg P)}
  \open
  \hypo {2} {P}
  \have {3} {P \vee \neg P} \oi{2}
  \have {4} {\bot} \ne{3,1}
  \close
  \have {5} {\neg P} \ni{2-4}
  \have {6} {P \vee \neg P} \oi{5}
  \have {7} {\bot} \ne{6,1}
  \close
  \have {8} {P \vee \neg P} \raa{1-7}
\end{nd}$
\end{center}
```

The derivation has no premises, so it shows \( \vdash P \vee \neg P \). \( \rulename{RAA} \) is used once, at line 8. This proves the proposition.
:::

The assumption of line 1 is used twice, at lines 4 and 7. The first use refutes \( P \); the second uses that refutation. Excluded middle now becomes a derived rule with no premises: a line \( \varphi \vee \neg\varphi \) may be written anywhere, for any statement \( \varphi \), justified by \( \rulename{LEM} \) with no line cited. Pasting in the eight lines above would replace it.

Its use is **proof by cases on a statement**. To derive \( \chi \), derive it once in a box that assumes \( \varphi \) and once in a box that assumes \( \neg\varphi \), and combine the two boxes with the line \( \varphi \vee \neg\varphi \) by \( \rulename{\vee E} \). The fold after De Morgan's laws below uses it that way, and so does part (b) of the result after them.

**A law with no negation.** The last is a law in which \( \neg \) does not occur at all.

::: {#prp-peirce}
[Peirce's Law]

For all statements \( P \) and \( Q \), \( \vdash ((P \to Q) \to P) \to P \).
:::

*In words: a law with no \( \neg \) in it, whose derivation here still uses \( \rulename{RAA} \). The derivation is in the fold below.*

::: {.second-reading title="Peirce's law, derived"}
*Try it first (ten minutes): use the goal-directed and premise-directed moves of the earlier sections on this goal until they stall. At which gap do they stall, and which line, if it were available there, would let you finish?*

::: {.idea}
The goal is an implication, so we open a box on \( (P \to Q) \to P \) with the goal \( P \), a letter. The only line that can produce \( P \) is the assumption itself, by \( \rulename{{\to}E} \), once we have its hypothesis \( P \to Q \). So \( P \to Q \) becomes a subgoal, and the goal-directed move opens a box on \( P \) with the goal \( Q \). There the moves stall: the resources are \( (P \to Q) \to P \) and \( P \), and neither says anything about \( Q \). What the stalled gap lacks is a clash, which \( \rulename{\bot E} \) would turn into \( Q \).

We are stuck, so the new move applies, but where? Assuming \( \neg Q \) at the stalled gap gives nothing new: a clash with \( \neg Q \) needs \( Q \), the stalled goal itself. So apply the move one level out, to the goal \( P \), and assume \( \neg P \). That is exactly what the stalled gap lacked: inside the box of \( P \), the pair \( P \), \( \neg P \) gives \( \bot \), and \( \rulename{\bot E} \) gives \( Q \). Then \( P \to Q \), then \( P \) by \( \rulename{{\to}E} \), which clashes with \( \neg P \).
:::

::: {.proof}
The derivation is:

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {(P \to Q) \to P}
  \open
  \hypo {2} {\neg P}
  \open
  \hypo {3} {P}
  \have {4} {\bot} \ne{3,2}
  \have {5} {Q} \be{4}
  \close
  \have {6} {P \to Q} \ii{3-5}
  \have {7} {P} \ie{1,6}
  \have {8} {\bot} \ne{7,2}
  \close
  \have {9} {P} \raa{2-8}
  \close
  \have {10} {((P \to Q) \to P) \to P} \ii{1-9}
\end{nd}$
\end{center}
```

The derivation has no premises, and \( \rulename{RAA} \) enters at line 9. This proves the proposition.
:::

The assumption \( \neg P \) of line 2 is used twice: at line 4 it makes the innermost box contradictory, and at line 8 it clashes with the \( P \) that line 7 obtained. Notice where the new box went: around the stalled box, not inside it. An assumption made one level out is available in every gap inside its box, and so it could give the stalled gap the line it lacked. Peirce's law contains no \( \neg \), yet our derivation uses \( \rulename{RAA} \): the classical rule is about more than negation.
:::

## De Morgan's laws

The negation of an "and" is an "or" of negations, and the negation of an "or" is an "and" of negations. For example, a real number \( x \) fails to lie in the interval \( [0, 1] \), that is, \( \neg(0 \le x \wedge x \le 1) \), exactly when \( x < 0 \) or \( x > 1 \). Each law has two directions, so there are four derivations to give.

::: {#prp-de-morgan}
[De Morgan's Laws]

For all statements \( P \) and \( Q \):

::: {.enumerate options="label=(\alph*)"}
1. \( \neg(P \vee Q) \vdash \neg P \wedge \neg Q \);
2. \( \neg P \wedge \neg Q \vdash \neg(P \vee Q) \);
3. \( \neg P \vee \neg Q \vdash \neg(P \wedge Q) \);
4. \( \neg(P \wedge Q) \vdash \neg P \vee \neg Q \).
:::
:::

*Try it first (ten minutes): look for a derivation of (d) with the rules of the earlier sections. Which rule would give its last line, and what would that rule need?*

::: {.idea}
Parts (a)–(c) yield to their goals. In (a) the goal is a conjunction of negations: two \( \rulename{\neg I} \) boxes, one per conjunct. In (b) and (c) the goal is a negation: one \( \rulename{\neg I} \) box, with the disjunction used inside it by \( \rulename{\vee E} \).

In pictures, for (a): two subgoals; then a box under each.

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \vee Q)}
  \have[\ ][0] {} {\vdots}
  \have[][5] {5} {\neg P}
  \have[\ ][0] {} {\vdots}
  \have[][9] {9} {\neg Q}
  \have {10} {\neg P \wedge \neg Q} \ai{5,9}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {\neg (P \vee Q)}
  \open
  \hypo {2} {P}
  \have[\ ][0] {} {\vdots}
  \have[][4] {4} {\bot}
  \close
  \have {5} {\neg P} \ni{2-4}
  \open
  \hypo {6} {Q}
  \have[\ ][0] {} {\vdots}
  \have[][8] {8} {\bot}
  \close
  \have {9} {\neg Q} \ni{6-8}
  \have {10} {\neg P \wedge \neg Q} \ai{5,9}
\end{nd}$
\end{center}
```

For (b): the box on \( P \vee Q \); then the two cases inside it.

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P \wedge \neg Q}
  \have {2} {\neg P} \ae{1}
  \have {3} {\neg Q} \ae{1}
  \open
  \hypo {4} {P \vee Q}
  \have[\ ][0] {} {\vdots}
  \have[][9] {9} {\bot}
  \close
  \have {10} {\neg (P \vee Q)} \ni{4-9}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {\neg P \wedge \neg Q}
  \have {2} {\neg P} \ae{1}
  \have {3} {\neg Q} \ae{1}
  \open
  \hypo {4} {P \vee Q}
  \open
  \hypo {5} {P}
  \have[\ ][0] {} {\vdots}
  \have[][6] {6} {\bot}
  \close
  \open
  \hypo {7} {Q}
  \have[\ ][0] {} {\vdots}
  \have[][8] {8} {\bot}
  \close
  \have {9} {\bot} \oe{4,5-6,7-8}
  \close
  \have {10} {\neg (P \vee Q)} \ni{4-9}
\end{nd}$
\end{center}
```

Part (d) resists. Its goal is a disjunction, so the natural last line is \( \rulename{\vee I} \), from \( \neg P \) or from \( \neg Q \). But the step from the premise to \( \neg P \) can be broken: with \( P \) true and \( Q \) false the premise is true and \( \neg P \) false; and the step to \( \neg Q \) breaks with \( P \) false and \( Q \) true. So neither side is worth aiming at. The premise itself can be used only by \( \rulename{\neg E} \), against \( P \wedge Q \), which we do not have. We are stuck at the whole goal, so we assume its negation, \( \neg(\neg P \vee \neg Q) \), which says that neither \( \neg P \) nor \( \neg Q \) holds. It should give \( P \) and \( Q \). Each is a letter, so each gets a small \( \rulename{RAA} \) box of its own, whose clash is manufactured by \( \rulename{\vee I} \). Together \( P \) and \( Q \) clash with the premise.

For (d): the \( \rulename{RAA} \) box on the negated goal; then a box for each of \( P \) and \( Q \).

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \wedge Q)}
  \open
  \hypo {2} {\neg (\neg P \vee \neg Q)}
  \have[\ ][0] {} {\vdots}
  \have[][11] {11} {P \wedge Q}
  \have {12} {\bot} \ne{11,1}
  \close
  \have {13} {\neg P \vee \neg Q} \raa{2-12}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {\neg (P \wedge Q)}
  \open
  \hypo {2} {\neg (\neg P \vee \neg Q)}
  \open
  \hypo {3} {\neg P} \purpose{\raa}
  \have[\ ][0] {} {\vdots}
  \have[][5] {5} {\bot}
  \close
  \have {6} {P}
  \open
  \hypo {7} {\neg Q} \purpose{\raa}
  \have[\ ][0] {} {\vdots}
  \have[][9] {9} {\bot}
  \close
  \have {10} {Q}
  \have {11} {P \wedge Q} \ai{6,10}
  \have {12} {\bot} \ne{11,1}
  \close
  \have {13} {\neg P \vee \neg Q} \raa{2-12}
\end{nd}$
\end{center}
```
:::

::: {.proof}
(a) Two \( \rulename{\neg I} \) boxes, one for each conjunct, then \( \rulename{\wedge I} \):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \vee Q)}
  \open
  \hypo {2} {P}
  \have {3} {P \vee Q} \oi{2}
  \have {4} {\bot} \ne{3,1}
  \close
  \have {5} {\neg P} \ni{2-4}
  \open
  \hypo {6} {Q}
  \have {7} {P \vee Q} \oi{6}
  \have {8} {\bot} \ne{7,1}
  \close
  \have {9} {\neg Q} \ni{6-8}
  \have {10} {\neg P \wedge \neg Q} \ai{5,9}
\end{nd}$
\end{center}
```

(b) One \( \rulename{\neg I} \) box that opens with \( P \vee Q \). Inside it, \( \rulename{\vee E} \) splits into two cases, and each case clashes with one half of the premise:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P \wedge \neg Q}
  \have {2} {\neg P} \ae{1}
  \have {3} {\neg Q} \ae{1}
  \open
  \hypo {4} {P \vee Q}
  \open
  \hypo {5} {P}
  \have {6} {\bot} \ne{5,2}
  \close
  \open
  \hypo {7} {Q}
  \have {8} {\bot} \ne{7,3}
  \close
  \have {9} {\bot} \oe{4,5-6,7-8}
  \close
  \have {10} {\neg (P \vee Q)} \ni{4-9}
\end{nd}$
\end{center}
```

(c) The same shape as (b), with the roles of \( \wedge \) and \( \vee \) exchanged:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P \vee \neg Q}
  \open
  \hypo {2} {P \wedge Q}
  \have {3} {P} \ae{2}
  \have {4} {Q} \ae{2}
  \open
  \hypo {5} {\neg P}
  \have {6} {\bot} \ne{3,5}
  \close
  \open
  \hypo {7} {\neg Q}
  \have {8} {\bot} \ne{4,7}
  \close
  \have {9} {\bot} \oe{1,5-6,7-8}
  \close
  \have {10} {\neg (P \wedge Q)} \ni{2-9}
\end{nd}$
\end{center}
```

(d) \( \rulename{RAA} \) on the goal, and inside it two smaller \( \rulename{RAA} \) boxes:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \wedge Q)}
  \open
  \hypo {2} {\neg (\neg P \vee \neg Q)}
  \open
  \hypo {3} {\neg P}
  \have {4} {\neg P \vee \neg Q} \oi{3}
  \have {5} {\bot} \ne{4,2}
  \close
  \have {6} {P} \raa{3-5}
  \open
  \hypo {7} {\neg Q}
  \have {8} {\neg P \vee \neg Q} \oi{7}
  \have {9} {\bot} \ne{8,2}
  \close
  \have {10} {Q} \raa{7-9}
  \have {11} {P \wedge Q} \ai{6,10}
  \have {12} {\bot} \ne{11,1}
  \close
  \have {13} {\neg P \vee \neg Q} \raa{2-12}
\end{nd}$
\end{center}
```

The derivations of (a), (b), and (c) close every box by \( \rulename{\neg I} \) or \( \rulename{\vee E} \) and use no \( \rulename{RAA} \). The derivation of (d) uses \( \rulename{RAA} \) at lines 6, 10, and 13. This proves all four laws.
:::

Laws (a)–(c) conclude negations or a conjunction of negations, and \( \rulename{\neg I} \) builds negations. Law (d) concludes a **disjunction**, and \( \rulename{\vee I} \) needs to know **which** side holds, while the premise says only that \( P \) and \( Q \) do not both hold. \( \rulename{RAA} \) gets round the missing decision without making it.

::: {.second-reading title="De Morgan (d) by excluded middle"}
Excluded middle makes the decision instead. Split on \( P \vee \neg P \). In the case \( \neg P \), \( \rulename{\vee I} \) gives \( \neg P \vee \neg Q \) at once. In the case \( P \), a \( \rulename{\neg I} \) box on \( Q \) builds \( P \wedge Q \), which clashes with the premise, giving \( \neg Q \); then \( \rulename{\vee I} \) gives \( \neg P \vee \neg Q \). Written out, this route is 11 lines, with \( \rulename{LEM} \) as its one classical line. Both routes use a classical rule.
:::

::: {.check}
Suppose \( \rulename{RAA} \) were deleted from the list of rules. Which of the four derivations in the proof of @prp-de-morgan would still be correct, and what is the first line of the others that would lose its justification?
:::

::: {.solution}
The derivations of (a), (b), and (c) would still be correct: they use \( \rulename{\neg I} \), \( \rulename{\neg E} \), \( \rulename{\vee I} \), \( \rulename{\vee E} \), \( \rulename{\wedge I} \), and \( \rulename{\wedge E} \) only. In the derivation of (d), line 6 is the first to lose its justification: it closes the box that opened with \( \neg P \) and writes \( P \), which is \( \rulename{RAA} \). (Lines 10 and 13 lose theirs too.)
:::

## Implication as a disjunction

In everyday mathematics "if \( P \) then \( Q \)" and "either \( P \) fails or \( Q \) holds" are used interchangeably. One direction of that exchange needs only the earlier rules; our derivation of the other uses a classical rule.

::: {#prp-implication-as-disjunction}
[Implication as a Disjunction]

For all statements \( P \) and \( Q \):

::: {.enumerate options="label=(\alph*)"}
1. \( \neg P \vee Q \vdash P \to Q \), by a derivation that does not use \( \rulename{RAA} \);
2. \( P \to Q \vdash \neg P \vee Q \), by a derivation that uses \( \rulename{LEM} \).
:::
:::

::: {.idea}
(a) The premise is a disjunction, so we use it by cases, each ending in the current goal \( P \to Q \). In each case that goal is an implication, so we open a box with \( P \). In the case \( \neg P \), the box clashes at once and \( \rulename{\bot E} \) gives \( Q \): this is the derivation of @prp-vacuous-implication. In the case \( Q \), the box repeats \( Q \).

In pictures, for (a): the two cases; then a box on \( P \) in each.

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P \vee Q}
  \open
  \hypo {2} {\neg P}
  \have[\ ][0] {} {\vdots}
  \have[][6] {6} {P \to Q}
  \close
  \open
  \hypo {7} {Q}
  \have[\ ][0] {} {\vdots}
  \have[][10] {10} {P \to Q}
  \close
  \have {11} {P \to Q} \oe{1,2-6,7-10}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {\neg P \vee Q}
  \open
  \hypo {2} {\neg P}
  \open
  \hypo {3} {P}
  \have[\ ][0] {} {\vdots}
  \have[][5] {5} {Q}
  \close
  \have {6} {P \to Q} \ii{3-5}
  \close
  \open
  \hypo {7} {Q}
  \open
  \hypo {8} {P}
  \have[\ ][0] {} {\vdots}
  \have[][9] {9} {Q}
  \close
  \have {10} {P \to Q} \ii{8-9}
  \close
  \have {11} {P \to Q} \oe{1,2-6,7-10}
\end{nd}$
\end{center}
```

(b) The goal is a disjunction, so we postpone it. The premise is an implication, which gives \( Q \) only once we have \( P \), and we do not. So we are stuck, and this time excluded middle is the better tool than an \( \rulename{RAA} \) box: we decide \( P \) first. In the case \( P \) the premise gives \( Q \); in the case \( \neg P \) the left side is in hand.

For (b): the split; then \( \rulename{{\to}E} \) in the case \( P \).

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \have {2} {P \vee \neg P} \lem{}
  \open
  \hypo {3} {P}
  \have[\ ][0] {} {\vdots}
  \have[][5] {5} {\neg P \vee Q}
  \close
  \open
  \hypo {6} {\neg P}
  \have[\ ][0] {} {\vdots}
  \have[][7] {7} {\neg P \vee Q}
  \close
  \have {8} {\neg P \vee Q} \oe{2,3-5,6-7}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {P \to Q}
  \have {2} {P \vee \neg P} \lem{}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have[\ ][0] {} {\vdots}
  \have[][5] {5} {\neg P \vee Q}
  \close
  \open
  \hypo {6} {\neg P}
  \have[\ ][0] {} {\vdots}
  \have[][7] {7} {\neg P \vee Q}
  \close
  \have {8} {\neg P \vee Q} \oe{2,3-5,6-7}
\end{nd}$
\end{center}
```
:::

::: {.proof}
(a) \( \rulename{\vee E} \) on the premise, with an implication built in each case:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P \vee Q}
  \open
  \hypo {2} {\neg P}
  \open
  \hypo {3} {P}
  \have {4} {\bot} \ne{3,2}
  \have {5} {Q} \be{4}
  \close
  \have {6} {P \to Q} \ii{3-5}
  \close
  \open
  \hypo {7} {Q}
  \open
  \hypo {8} {P}
  \have {9} {Q} \r{7}
  \close
  \have {10} {P \to Q} \ii{8-9}
  \close
  \have {11} {P \to Q} \oe{1,2-6,7-10}
\end{nd}$
\end{center}
```

Line 9 repeats line 7 inside the box of line 8, because \( \rulename{{\to}I} \) needs \( Q \) as a line of that box itself.

(b) Cases on \( P \):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \have {2} {P \vee \neg P} \lem{}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {\neg P \vee Q} \oi{4}
  \close
  \open
  \hypo {6} {\neg P}
  \have {7} {\neg P \vee Q} \oi{6}
  \close
  \have {8} {\neg P \vee Q} \oe{2,3-5,6-7}
\end{nd}$
\end{center}
```

Line 2 is @prp-excluded-middle used as a derived rule, and the only \( \rulename{RAA} \) is inside it. This proves both parts.
:::

The two routes of the section now stand side by side. \( \rulename{RAA} \) assumes the goal fails and hunts for a clash; \( \rulename{LEM} \) splits on a statement of our choosing and gives each case a resource it lacked. When a premise is waiting for a statement \( S \) (here \( P \to Q \) waits for \( P \)), splitting on \( S \) is usually the shorter route.

## One principle in three forms

\( \rulename{RAA} \) gave us \( \rulename{\neg\neg E} \) and excluded middle. Had we added one of those two as the new primitive rule instead of \( \rulename{RAA} \), would we have proved less?

To say this exactly, we need two rule forms and one notion. **\( \rulename{\neg\neg E} \) taken as a rule** says: if \( \neg\neg\varphi \) stands on an available line, we may write \( \varphi \). **\( \rulename{LEM} \) taken as a rule** says: we may write \( \varphi \vee \neg\varphi \) on any line, for any statement \( \varphi \), citing nothing. Given a list of rules, a rule \( \mathsf{X} \) **derives** a rule \( \mathsf{Y} \) over that list if every use of \( \mathsf{Y} \) in a derivation can be replaced by a fragment that uses only \( \mathsf{X} \) and the rules of the list, without changing the premises or the last line. Then every sequent derivable with \( \mathsf{Y} \) added to the list is derivable with \( \mathsf{X} \) added instead.

::: {#thm-classical-rules-interderivable}
[The Classical Rules Are Interderivable]

Over the primitive rules other than \( \rulename{RAA} \), each of the three rules \( \rulename{RAA} \), \( \rulename{\neg\neg E} \), and \( \rulename{LEM} \) derives the other two. In particular, adding any one of the three to the other primitive rules gives the same derivable sequents.
:::

*In words: \( \rulename{RAA} \), \( \rulename{\neg\neg E} \) and \( \rulename{LEM} \) are one principle in three forms; adding any one of them to the other rules proves exactly what adding any other does.*

In the picture, an arrow from X to Y means that X derives Y over the other primitive rules; going round the solid cycle, each rule derives the other two. ① is @prp-excluded-middle on the solid arrow and @prp-double-negation (b) on the dashed one; ② closes the box by \( \rulename{\neg I} \), then applies \( \rulename{\neg\neg E} \); ③ splits on \( \varphi \vee \neg\varphi \).

```{=latex}
\begin{center}
\begin{tikzpicture}[flowchart]
  \node[fc step] (r) {RAA};
  \node[fc step, below right=of r] (l) {LEM};
  \node[fc step, below left=of r] (d) {$\neg\neg$E};
  \draw[fc arrow] (r) -- node[midway, font=\scriptsize, auto] {\textcircled{\scriptsize 1}} (l);
  \draw[fc arrow] (l) -- node[midway, font=\scriptsize, auto] {\textcircled{\scriptsize 3}} (d);
  \draw[fc arrow] (d) to[bend left=25] node[midway, font=\scriptsize, auto] {\textcircled{\scriptsize 2}} (r);
  \draw[fc arrow, dashed] (r) to[bend left=25] node[pos=0.35, font=\scriptsize, auto] {\textcircled{\scriptsize 1}} (d);
\end{tikzpicture}
\end{center}
```

Part ② says that a step of \( \rulename{RAA} \) can be replaced by \( \rulename{\neg I} \) followed by \( \rulename{\neg\neg E} \), keeping the box. On the derivation of @exm-raa-at-most-one, line 6 becomes two lines:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {x^2 \le x}
  \open
  \hypo {2} {\neg (x \le 1)}
  \have {3} {x > 1} \by{algebra}{2}
  \have {4} {\neg (x^2 \le x)} \by{algebra}{3}
  \have {5} {\bot} \ne{1,4}
  \close
  \have {6} {\neg\neg (x \le 1)} \ni{2-5}
  \have {7} {x \le 1} \nne{6}
\end{nd}$
\end{center}
```

Line 6 is correct by \( \rulename{\neg I} \): the box opens with \( \neg(x \le 1) \), and \( \neg\neg(x \le 1) \) is the negation of that assumption. The box itself is unchanged: both rules ask for \( \bot \) as a line of the box, and differ only in what they write after it. Part ③, shown on the same example in the fold below, replaces that \( \rulename{\neg\neg E} \) line by a split written by \( \rulename{LEM} \).

So the classical part of our rules is **one** extra principle, whichever of its three forms we write down.

::: {.second-reading title="Part ③ on the example, and the proof: replacing one rule by another"}
**Part ③ on the example.** Part ③ replaces the \( \rulename{\neg\neg E} \) line of ② by a split on \( (x \le 1) \vee \neg(x \le 1) \), written by \( \rulename{LEM} \):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {x^2 \le x}
  \open
  \hypo {2} {\neg (x \le 1)}
  \have {3} {x > 1} \by{algebra}{2}
  \have {4} {\neg (x^2 \le x)} \by{algebra}{3}
  \have {5} {\bot} \ne{1,4}
  \close
  \have {6} {\neg\neg (x \le 1)} \ni{2-5}
  \have {7} {(x \le 1) \vee \neg (x \le 1)} \lem{}
  \open
  \hypo {8} {x \le 1}
  \close
  \open
  \hypo {9} {\neg (x \le 1)}
  \have {10} {\bot} \ne{9,6}
  \have {11} {x \le 1} \be{10}
  \close
  \have {12} {x \le 1} \oe{7,8-8,9-11}
\end{nd}$
\end{center}
```

The first case is the goal; the second clashes with line 6 and closes itself. Together, ② and ③ turned the one \( \rulename{RAA} \) line into steps of \( \rulename{\neg I} \), \( \rulename{LEM} \) and the rules of the earlier sections: that is how \( \rulename{LEM} \) derives \( \rulename{RAA} \).

::: {.idea}
Replacements can be chained, so it is enough to go once round a cycle. ① \( \rulename{RAA} \) derives the other two: that is @prp-excluded-middle and @prp-double-negation (b). ② \( \rulename{\neg\neg E} \) derives \( \rulename{RAA} \): \( \rulename{\neg I} \) closes an \( \rulename{RAA} \) box, which runs from \( \neg\varphi \) to \( \bot \), with \( \neg\neg\varphi \), and \( \rulename{\neg\neg E} \) finishes. ③ \( \rulename{LEM} \) derives \( \rulename{\neg\neg E} \): split on \( \varphi \vee \neg\varphi \); the case \( \varphi \) is the goal, and the case \( \neg\varphi \) clashes with \( \neg\neg\varphi \).

*Before reading on: in the fragment for ③ below, which rule does line \( k + 4 \) use, and why may line \( k + 3 \) cite line \( m \)?*
:::

::: {.proof}
① Suppose a derivation uses \( \rulename{\neg\neg E} \) at line \( k \), writing \( \varphi \) and citing a line \( m \) that holds \( \neg\neg\varphi \). Replace line \( k \) by the last three lines of the derivation in @prp-double-negation (b), with its premise replaced by line \( m \): a box opening with \( \neg\varphi \), the line \( \bot \) by \( \rulename{\neg E} \) citing the assumption and line \( m \), and then \( \varphi \) by \( \rulename{RAA} \). A use of \( \rulename{LEM} \), writing \( \varphi \vee \neg\varphi \), is replaced by the eight lines of the derivation in @prp-excluded-middle, with \( \varphi \) for \( P \); that derivation has no premises. So \( \rulename{RAA} \) derives \( \rulename{\neg\neg E} \) and \( \rulename{LEM} \).

② Suppose a derivation uses \( \rulename{RAA} \) at line \( k \), closing a box, lines \( i \) to \( j \), that opens with \( \neg\varphi \) and ends with \( \bot \). Keep the box and replace line \( k \) by two lines:

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \open
  \hypo {i} {\neg \varphi}
  \have {} {\vdots}
  \have {j} {\bot}
  \close
  \have {k} {\neg\neg \varphi} \ni{i-j}
  \have {k+1} {\varphi} \nne{k}
\end{nd}$
\end{center}
```

Line \( k \) is correct by \( \rulename{\neg I} \), since the box opens with \( \neg\varphi \) and \( \neg\neg\varphi \) is the negation of that assumption. Both rules ask for \( \bot \) as a line of the box itself, so the box needs no change. So \( \rulename{\neg\neg E} \) derives \( \rulename{RAA} \).

③ Suppose a derivation uses \( \rulename{\neg\neg E} \) at line \( k \), writing \( \varphi \) and citing a line \( m \) that holds \( \neg\neg\varphi \). Replace line \( k \) by six lines:

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {m} {\neg\neg \varphi}
  \have {} {\vdots}
  \have {k} {\varphi \vee \neg \varphi} \lem{}
  \open
  \hypo {k+1} {\varphi}
  \close
  \open
  \hypo {k+2} {\neg \varphi}
  \have {k+3} {\bot} \ne{k+2,m}
  \have {k+4} {\varphi} \be{k+3}
  \close
  \have {k+5} {\varphi} \oe{k,k+1-k+1,k+2-k+4}
\end{nd}$
\end{center}
```

The first case is a one-line box: it opens with \( \varphi \) and so already ends with the goal. In the second case, line \( k + 3 \) may cite line \( m \), because line \( m \) was available at the old line \( k \) and every new line sits in the same boxes as the old line \( k \), or in boxes opened after it. No rule other than \( \rulename{LEM} \) and the rules of the list is used. So \( \rulename{LEM} \) derives \( \rulename{\neg\neg E} \).

In each replacement the later lines are renumbered, and a later citation of the old line \( k \) now cites the fragment's last line, which holds the same statement in the same boxes. The premises and the last line of the derivation are unchanged.

Finally, replacements can be chained. \( \rulename{LEM} \) derives \( \rulename{RAA} \): replace each use of \( \rulename{RAA} \) by the fragment of ②, and then each use of \( \rulename{\neg\neg E} \) so created by the fragment of ③. \( \rulename{\neg\neg E} \) derives \( \rulename{LEM} \): replace each use of \( \rulename{LEM} \) by the derivation of ①, and then each use of \( \rulename{RAA} \) in it by the fragment of ②. With ①, ②, and ③, this shows that each of the three rules derives the other two, as claimed.
:::

The base list matters: part ③ uses \( \rulename{\bot E} \) at line \( k + 4 \), to close the impossible case as in @exm-impossible-case.
:::

::: {.second-reading title="Other books, and a rule we could drop"}
::: {.remark}
Some books call exactly our \( \rulename{RAA} \) "proof by contradiction" or PBC, and some take \( \rulename{\neg\neg E} \) as their primitive rule and derive \( \rulename{RAA} \) from it. By @thm-classical-rules-interderivable nothing changes: all these choices prove the same sequents.
:::


::: {.remark}
\( \rulename{\bot E} \) could have been dropped from the primitive rules, since \( \rulename{RAA} \) and repetition derive it (Exercise B3 below asks for the derivation). We keep it so that the primitive rules other than \( \rulename{RAA} \) form a system of their own.
:::
:::

## How reductio looks in a mathematical proof

Here is an argument of a kind that analysis uses constantly; read it one sentence at a time, with the rule of each step in brackets.

::: {#exm-raa-zero}
[A number below every positive number]

Let \( x \) be a real number with \( x \ge 0 \), and suppose that \( x \le \varepsilon \) for **every** real number \( \varepsilon > 0 \). Prove that \( x = 0 \).
:::

::: {.solution}
Suppose, for a contradiction, that \( x \ne 0 \). Since \( x \ge 0 \) and \( x \ne 0 \), we have \( x > 0 \). Then \( \varepsilon \coloneqq x/2 \) is a real number with \( \varepsilon > 0 \), so the hypothesis applies to it and gives \( x \le x/2 \). Subtracting \( x/2 \) from both sides gives \( x/2 \le 0 \), and multiplying by \( 2 \) gives \( x \le 0 \). This contradicts \( x > 0 \). Hence \( x = 0 \).
:::

1. "Suppose, for a contradiction, that \( x \ne 0 \)." [An \( \rulename{RAA} \) box opens, with \( \neg(x = 0) \), the exact negation of the goal \( x = 0 \).]
2. "Since \( x \ge 0 \) and \( x \ne 0 \), we have \( x > 0 \)." [\( x \ge 0 \) means \( x = 0 \vee x > 0 \), and the box's assumption refutes the left side, so \( \rulename{DS} \) (@prp-disjunctive-syllogism) gives \( x > 0 \).]
3. "Then \( \varepsilon \coloneqq x/2 \) is a real number with \( \varepsilon > 0 \)." [School algebra.]
4. "So the hypothesis applies to it and gives \( x \le x/2 \)." [The hypothesis is about **every** \( \varepsilon > 0 \); applying it to one is a step about "every", used as ordinary reasoning (the note at the start of this chapter).]
5. "… gives \( x/2 \le 0 \), and … \( x \le 0 \)." [School algebra.]
6. "This contradicts \( x > 0 \)." [\( \rulename{\neg E} \): for real numbers \( x > 0 \) is \( \neg(x \le 0) \), the negation of the line \( x \le 0 \).]
7. "Hence \( x = 0 \)." [\( \rulename{RAA} \) closes the box.]

**\( \rulename{\neg I} \) or \( \rulename{RAA} \)?** The phrase "suppose not" covers two rules. Here is one statement proved both ways, for a real number \( x \): *if \( x^3 < 0 \), then \( x < 0 \).*

- **By the contrapositive (\( \rulename{CP} \)).** We prove that if \( x \ge 0 \), then \( x^3 \ge 0 \). Suppose \( x \ge 0 \) [assumption for \( \rulename{{\to}I} \)]. Then \( x^3 = x \cdot x \cdot x \ge 0 \) [algebra]. So if \( x \ge 0 \), then \( x^3 \ge 0 \) [\( \rulename{{\to}I} \)], and by contraposition, if \( x^3 \) is not \( \ge 0 \), then \( x \) is not \( \ge 0 \) [\( \rulename{CP} \)]: that is, if \( x^3 < 0 \), then \( x < 0 \).
- **By contradiction (\( \rulename{RAA} \)).** Suppose \( x^3 < 0 \) [assumption for \( \rulename{{\to}I} \)]. Suppose, for a contradiction, that \( x < 0 \) fails, that is, \( x \ge 0 \) [an \( \rulename{RAA} \) box on \( \neg(x < 0) \)]. Then \( x^3 \ge 0 \), which contradicts \( x^3 < 0 \) [\( \rulename{\neg E} \)]. Hence \( x < 0 \) [\( \rulename{RAA} \)], and so if \( x^3 < 0 \), then \( x < 0 \) [\( \rulename{{\to}I} \)].

The first proof introduces negations and removes none; the second removes one, at its \( \rulename{RAA} \) step. Which rule a "suppose not" uses is decided by the lines as written: what the box assumes, and what is written after it. Under the convention of Section 2.1 an order statement can be written either way: with the goal \( x < 0 \) written as \( \neg(x \ge 0) \), the box on \( x \ge 0 \) closes by \( \rulename{\neg I} \); and @exm-raa-at-most-one, with its goal written \( \neg(x > 1) \) and its box on \( x > 1 \), would close by \( \rulename{\neg I} \) too.

The proof of @thm-sqrt2-irrational assumes the positive statement \( r^2 = 2 \) and concludes its negation, so it is \( \rulename{\neg I} \).

::: {.check}
\( \rulename{\neg I} \) or \( \rulename{RAA} \)? (i) "Suppose \( 15 \) is prime. Then … This is a contradiction. Hence \( 15 \) is not prime." (ii) "Suppose \( n \) is not odd. Then … This is a contradiction. Hence \( n \) is odd."
:::

::: {.solution}
(i) \( \rulename{\neg I} \): the box opens with the statement whose negation is concluded. (ii) \( \rulename{RAA} \): the box opens with \( \neg \)(\( n \) is odd), and the conclusion is "\( n \) is odd".
:::

::: {.second-reading title="RAA is never needed to finish a negation"}
For one kind of goal the new rule is never needed at the last step. Suppose the goal is itself a negation \( \neg\psi \). An \( \rulename{RAA} \) box for it opens with \( \neg\neg\psi \). Replace it by a \( \rulename{\neg I} \) box that opens with \( \psi \); inside it, derive \( \neg\neg\psi \) from \( \psi \) by the three lines of @exm-double-negation-introduction (a box on \( \neg\psi \) that clashes with \( \psi \)); then continue as the \( \rulename{RAA} \) box did, citing that line wherever the \( \rulename{RAA} \) box cited its assumption. The box still ends in \( \bot \), and \( \rulename{\neg I} \) closes it with \( \neg\psi \). So the **last** step of a derivation of a negation never needs \( \rulename{RAA} \), though steps inside its box still may. \( \rulename{RAA} \) earns its place on the other goals.

When \( Q \) is itself a negation, the inner goal in @prp-contrapositive-converse is a negation, and its \( \rulename{RAA} \) can be replaced by \( \rulename{\neg I} \) in this way.
:::

::: {.warning}
An \( \rulename{RAA} \) box on \( \neg\varphi \) whose assumption is used **only at its last step**, against a \( \varphi \) derived without it, is legal, but it is a direct proof in disguise: the lines before the clash already derive \( \varphi \), so the box can be deleted. The smallest case opens a box on \( \neg P \) only to clash with a premise \( P \) that is already the goal. It is a direct proof in costume. (A box that reaches \( \bot \) without using its assumption at all is a different matter: the same lines, written before the box, derive \( \bot \) without it, and \( \rulename{\bot E} \) then gives the goal at once.)
:::

::: {.warning}
Not every "proof by contradiction" is \( \rulename{RAA} \). Calling the proof of @thm-sqrt2-irrational an \( \rulename{RAA} \) is a mislabeling: its box opens with \( r^2 = 2 \), not with a negation, and it concludes \( r^2 \ne 2 \), which \( \rulename{\neg I} \) writes. The difference matters when you count classical steps: the box of that proof closes by \( \rulename{\neg I} \) and contributes none.
:::

## The rule card

Before the card, the new rule on large statements; each box runs from the assumption shown to \( \bot \).

::: {#exm-reductio-and-classical-rules-instances}
[Instances of \( \rulename{RAA} \)]

| \( \varphi \) | The box opens with | New line |
|---|---|---|
| \( P \vee \neg Q \) | \( \neg(P \vee \neg Q) \) | \( P \vee \neg Q \) |
| \( (P \to Q) \to R \) | \( \neg((P \to Q) \to R) \) | \( (P \to Q) \to R \) |
| \( \neg Q \) | \( \neg\neg Q \) | \( \neg Q \) |

The third row is legal; a \( \rulename{\neg I} \) box opened by \( Q \) would also do (the fold "RAA is never needed to finish a negation").

**Not an instance.** A box opens with \( \neg P \vee \neg Q \) and reaches \( \bot \). The line "\( P \wedge Q \) — \( \rulename{RAA} \)" is not an instance: the assumption must be \( \neg(P \wedge Q) \), the negation of the whole line written. \( \neg P \vee \neg Q \) says the same only after a derivation (De Morgan's laws), and the rule compares symbols.
:::

Chapter 1's seven rules are on the card at the end of Section 1.6; here are this chapter's so far.

| Rule | Shape | You write | Lean |
|---|---|---|---|
| \( \rulename{\neg E} \) | \( \varphi \), \( \neg\varphi \) \( \Longrightarrow \) \( \bot \) | "…, which contradicts …" | `exact hn hp` (goal `False`) |
| \( \rulename{\bot E} \) | \( \bot \) \( \Longrightarrow \) any \( \varphi \) | "This case cannot occur." "So there is nothing to prove." | `exfalso` |
| \( \rulename{\neg I} \) | box \( \varphi \) … \( \bot \) \( \Longrightarrow \) \( \neg\varphi \) | "Suppose \( P \). … This is a contradiction. Hence not \( P \)." | `intro hp` (goal `False`) |
| \( \rulename{MT} \) (derived) | \( \varphi \to \psi \), \( \neg\psi \) \( \Longrightarrow \) \( \neg\varphi \) | "Since \( Q \) fails, so does \( P \)." | `mt h hnq` |
| \( \rulename{CP} \) (derived) | \( \varphi \to \psi \) \( \Longrightarrow \) \( \neg\psi \to \neg\varphi \) | "We prove the contrapositive: suppose not \( Q \); … so not \( P \)." | `mt` |
| \( \rulename{DS} \) (derived) | \( \varphi \vee \psi \), \( \neg\varphi \) \( \Longrightarrow \) \( \psi \) | "\( P \) is impossible, so \( Q \)." | `h.resolve_left hnp` |
| \( \rulename{{\leftrightarrow}I} \) | box \( \varphi \) … \( \psi \), box \( \psi \) … \( \varphi \) \( \Longrightarrow \) \( \varphi \leftrightarrow \psi \) | "\( (\Rightarrow) \) Suppose \( P \). … so \( Q \). \( (\Leftarrow) \) Suppose \( Q \). … so \( P \)." | `constructor` |
| \( \rulename{{\leftrightarrow}E} \) | \( \varphi \leftrightarrow \psi \), \( \varphi \) \( \Longrightarrow \) \( \psi \) (or with \( \psi \), \( \varphi \)) | "Since \( P \) holds if and only if \( Q \) does, and \( P \) holds, so does \( Q \)." | `h.mp hp` / `h.mpr hq` |
| \( \rulename{RAA} \) | box \( \neg\varphi \) … \( \bot \) \( \Longrightarrow \) \( \varphi \) | "Suppose, for a contradiction, that \( P \) fails. … This is impossible. Hence \( P \)." | `by_contra h` |
| \( \rulename{\neg\neg E} \) (derived) | \( \neg\neg\varphi \) \( \Longrightarrow \) \( \varphi \) | "It cannot be that \( P \) fails; so \( P \)." | `not_not.mp h` |
| \( \rulename{LEM} \) (derived) | nothing \( \Longrightarrow \) \( \varphi \vee \neg\varphi \) | "Either \( P \) or not. If \( P \), … If not, … In either case, …" | `by_cases h : P` |

The Lean column is for readers who use that proof assistant; nothing later depends on it.

::: {.warning}
[Not allowed: \( \rulename{RAA} \)]

Each step is wrong; the tag names the clause it breaks.

- Open the box for \( Q \vee R \) with \( \neg Q \vee R \): clause 1, the box opens with the negation of the **whole** goal.
- Write \( \varphi \) after a box opened by \( \varphi \): clause 1 (the pair below).
- Close the box on a \( \bot \) of a box inside it: clause 2.
- Write \( \neg\neg\varphi \) by \( \rulename{RAA} \): clause 3; \( \neg\neg\varphi \) is the line \( \rulename{\neg I} \) writes.
- To prove \( x \le 1 \), assume \( x \ge 1 \): clause 1, the negation of \( x \le 1 \) is \( x > 1 \).

Clause 1 is where the rule bites. Premises \( (P \vee R) \to Q \) and \( \neg Q \); wrong on the left, right on the right:

```{=latex}
\begin{center}
% expect-invalid: line 7 writes P by RAA after a box that opened with P, not with its negation
$\begin{nd}
  \hypo {1} {(P \vee R) \to Q}
  \hypo {2} {\neg Q}
  \open
  \hypo {3} {P} \purpose{\raa}
  \have {4} {P \vee R} \oi{3}
  \have {5} {Q} \ie{1,4}
  \have {6} {\bot} \ne{5,2}
  \close
  \have {7} {P} \raa{3-6}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {(P \vee R) \to Q}
  \hypo {2} {\neg Q}
  \open
  \hypo {3} {P}
  \have {4} {P \vee R} \oi{3}
  \have {5} {Q} \ie{1,4}
  \have {6} {\bot} \ne{5,2}
  \close
  \have {7} {\neg P} \ni{3-6}
\end{nd}$
\end{center}
```

The left box opened with \( P \), not \( \neg P \), so it refuted \( P \) and cannot conclude it. The claim \( (P \vee R) \to Q, \ \neg Q \vdash P \) breaks: let \( x \) be a real number, with \( P \): "\( x > 2 \)", \( R \): "\( x < -2 \)", \( Q \): "\( x^2 > 4 \)". The first premise holds for every \( x \), and at \( x = 0 \) the second holds and \( P \) fails.
:::

::: {.check}
A box opens with \( \neg(x \ne 2) \), for a real number \( x \), and reaches \( \bot \) as a line of the box itself. What may \( \rulename{RAA} \) write after it, and what may \( \rulename{\neg I} \)?
:::

::: {.solution}
\( \rulename{RAA} \) writes \( x \ne 2 \); \( \rulename{\neg I} \) writes \( \neg\neg(x \ne 2) \), that is \( \neg\neg\neg(x = 2) \).
:::

::: {.remark}
[Looking ahead]

Chapter 4 proves that \( P \) cannot be derived from \( \neg\neg P \), nor Peirce's law from no premises, without \( \rulename{RAA} \) or one of its two equivalents, and states the same, without proof, for De Morgan's law (d) and for \( (P \to Q) \vee (Q \to P) \). Chapter 8 tells the story of the mathematicians who declined the classical principle, and shows how to spot a proof by contradiction that is a direct proof in costume.
:::

## Exercises

### A. Check your understanding

::: {#exr-reductio-and-classical-rules-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. "Suppose \( 7 \) is even. Then \( 7 = 2k \) for some integer \( k \), so \( k = 7/2 \), which is not an integer. This is impossible. Hence \( 7 \) is not even." Is the last step \( \rulename{\neg I} \), \( \rulename{RAA} \), or neither? What did the box open with?
2. "Let \( x \) be real. Suppose \( x^2 \ge 2x - 1 \) fails, that is, \( x^2 < 2x - 1 \). Then \( (x - 1)^2 < 0 \), which is impossible. Hence \( x^2 \ge 2x - 1 \)." Same questions.
3. "Assume \( P \). Then, as shown above, \( Q \). Hence \( P \to Q \)." Same questions.
4. State \( \rulename{RAA} \) and \( \rulename{\neg I} \) side by side, and say which of the two the derivation of @prp-double-negation (a) uses.
5. In the derivation of @prp-de-morgan (d), why is a last line \( \rulename{\vee I} \), from \( \neg P \) or \( \neg Q \) derived from the premise alone, not worth aiming at?
6. In the same derivation, the assumption \( \neg(\neg P \vee \neg Q) \) on line 2 is cited twice. Name the two lines that cite it, and the rule each uses.
7. In the instance of ② on the opening example (in "One principle in three forms"), which rule justifies the line \( \neg\neg(x \le 1) \), and why does the box of lines 2–5 need no change?
:::
:::

::: {.solution}
(a) \( \rulename{\neg I} \): the box opened with "\( 7 \) is even", and the conclusion is its negation. (\( 7/2 \) is not an integer because \( 3 < 7/2 < 4 \).)

(b) \( \rulename{RAA} \): the box opened with the negation of \( x^2 \ge 2x - 1 \), and the conclusion is \( x^2 \ge 2x - 1 \) itself. (The clash: \( x^2 < 2x - 1 \) rearranges to \( (x - 1)^2 < 0 \), and squares are nonnegative.)

(c) Neither: this is \( \rulename{{\to}I} \). The box opened with \( P \) and ended with \( Q \); no \( \bot \) appears.

(d) \( \rulename{\neg I} \): a box that opens with \( \varphi \) and reaches \( \bot \) gives \( \neg\varphi \). \( \rulename{RAA} \): a box that opens with \( \neg\varphi \) and reaches \( \bot \) gives \( \varphi \). The derivation of @prp-double-negation (a) uses \( \rulename{\neg I} \), with \( \neg P \) as the assumption, so its conclusion is the negation of \( \neg P \), namely \( \neg\neg P \).

(e) \( \rulename{\vee I} \) would need \( \neg P \) or \( \neg Q \) on a line derived from the premise alone, and each of those steps can be broken: with \( P \) true and \( Q \) false the premise is true and \( \neg P \) false, and with \( P \) false and \( Q \) true the premise is true and \( \neg Q \) false. So neither step is worth aiming at: each breaks (Section 1.1's test).

(f) Line 5 cites it, by \( \rulename{\neg E} \) against line 4, \( \neg P \vee \neg Q \); and line 9 cites it, by \( \rulename{\neg E} \) against line 8, the same statement. Both lines lie in boxes inside the box of line 2, which is still open, so the citations are legal.

(g) \( \rulename{\neg I} \): the box opens with \( \neg(x \le 1) \) and ends with \( \bot \), so \( \rulename{\neg I} \) gives the negation of its assumption, \( \neg\neg(x \le 1) \). The box needs no change because \( \rulename{\neg I} \), like \( \rulename{RAA} \), asks only for a box that ends with \( \bot \) as a line of the box itself; the two rules differ in what they write after the box, not in the box.
:::

::: {#exr-reductio-and-classical-rules-a2}
[A2: Drill]

The parts run from one step, through a missing line, a justification column and steps to judge, to short derivations.

::: {.enumerate options="label=(\alph*)"}
1. A box opens with \( \neg(P \wedge Q) \) and ends with \( \bot \), a line of the box itself. What may \( \rulename{RAA} \) write after it, and what may \( \rulename{\neg I} \)?
2. Line 1 is \( \neg\neg(P \to Q) \). What does "\( \rulename{\neg\neg E} \) 1" write?
3. To prove \( Q \vee R \) by \( \rulename{RAA} \), which statement opens the box?
4. Let \( x \) be a real number. To prove \( x \ge 2 \) by contradiction, what is assumed?
5. Line 9 is \( P \to Q \), justified "\( \rulename{RAA} \) 4–8". What are lines 4 and 8?
6. Line 6 is \( Q \vee R \), justified "\( \rulename{\neg\neg E} \) 5". What is line 5, and by which rule is such a line usually written?
7. Fill in the justifications (i)–(iv).

    ```{=latex}
    \begin{center}
    $\begin{nd}
      \hypo {1} {\neg\neg (P \wedge Q)}
      \hypo {2} {Q \to R}
      \have {3} {P \wedge Q} \by{(i)}{}
      \have {4} {Q} \by{(ii)}{}
      \have {5} {R} \by{(iii)}{}
      \have {6} {R \vee S} \by{(iv)}{}
    \end{nd}$
    \end{center}
    ```

8. "Suppose \( 9 \) is prime. … This is impossible. Hence \( 9 \) is not prime." Is the last step \( \rulename{\neg I} \) or \( \rulename{RAA} \)?
9. "Suppose \( n^2 \) is not even. … This is impossible. Hence \( n^2 \) is even." Is the last step \( \rulename{\neg I} \) or \( \rulename{RAA} \)?
10. Which of \( \rulename{\neg\neg I} \), \( \rulename{\neg\neg E} \), \( \rulename{LEM} \), \( \rulename{MT} \), \( \rulename{DS} \) are derived in this chapter by a derivation that uses \( \rulename{RAA} \)?
11. Find the illegal line, and say why it is illegal.

    ```{=latex}
    \begin{center}
    % expect-invalid: line 7 cites 2-5, which is not a box (the box opened at line 2 ends at line 6)
    $\begin{nd}
      \hypo {1} {\neg (P \wedge Q)}
      \open
      \hypo {2} {\neg P}
      \open
      \hypo {3} {P \wedge Q}
      \have {4} {P} \ae{3}
      \have {5} {\bot} \ne{4,2}
      \close
      \have {6} {\neg (P \wedge Q)} \ni{3-5}
      \close
      \have {7} {P} \raa{2-5}
    \end{nd}$
    \end{center}
    ```

12. A box opens at line 2 with \( \neg P \); line 4, a line of that box itself, is \( \bot \). Is "5. \( \neg\neg P \) — \( \rulename{RAA} \) 2–4" correct?
13. Derive \( \neg\neg P, \ P \to Q \vdash Q \).
14. Derive \( \neg P \to P \vdash P \).
15. Derive \( \neg P \to Q, \ \neg Q \vdash P \) in two lines after the premises.
:::
:::

::: {.solution}
(a) \( \rulename{RAA} \) writes \( P \wedge Q \); \( \rulename{\neg I} \) writes \( \neg\neg(P \wedge Q) \).

(b) \( P \to Q \).

(c) \( \neg(Q \vee R) \), the negation of the whole goal; not \( \neg Q \vee R \).

(d) \( x < 2 \), that is \( \neg(x \ge 2) \); not \( x \le 2 \), which \( x = 2 \) satisfies together with the goal.

(e) Line 4 is the assumption \( \neg(P \to Q) \), "asm, for \( \rulename{RAA} \)"; line 8 is \( \bot \), the last line of the box.

(f) Line 5 is \( \neg\neg(Q \vee R) \). Such a line is usually written by \( \rulename{\neg I} \), closing a box opened by \( \neg(Q \vee R) \) (or it is a premise).

(g) (i) \( \rulename{\neg\neg E} \) 1; (ii) \( \rulename{\wedge E} \) 3; (iii) \( \rulename{{\to}E} \) 2, 4; (iv) \( \rulename{\vee I} \) 5.

(h) \( \rulename{\neg I} \): the box opens with "\( 9 \) is prime", and the conclusion is its negation.

(i) \( \rulename{RAA} \): the box opens with the negation of "\( n^2 \) is even", and the conclusion is that statement itself.

(j) \( \rulename{\neg\neg E} \) and \( \rulename{LEM} \); \( \rulename{\neg\neg I} \), \( \rulename{MT} \) and \( \rulename{DS} \) are derived without it.

(k) Line 7: lines 2–5 are not a box (the box opened at line 2 ends at line 6), and \( \rulename{RAA} \) needs \( \bot \) as a line of the box itself.

(l) No: \( \rulename{RAA} \) writes \( P \), the statement whose negation opened the box (clause 3); \( \neg\neg P \) is the line \( \rulename{\neg I} \) writes after the same box.

(m) 3 \( P \), \( \rulename{\neg\neg E} \) 1; 4 \( Q \), \( \rulename{{\to}E} \) 2, 3.

(n) 2 \( \neg P \), assumption, for \( \rulename{RAA} \); 3 \( P \), \( \rulename{{\to}E} \) 1, 2; 4 \( \bot \), \( \rulename{\neg E} \) 3, 2; 5 \( P \), \( \rulename{RAA} \) \( \lines{2}{4} \).

(o) 3 \( \neg\neg P \), \( \rulename{MT} \) 1, 2; 4 \( P \), \( \rulename{\neg\neg E} \) 3.
:::

### B. Practice

::: {#exr-reductio-and-classical-rules-b1}
[B1: With and without the new rule, used later]

::: {.enumerate options="label=(\alph*)"}
1. Derive \( \neg\neg P, \ \neg\neg(P \to Q) \vdash \neg\neg Q \) **without** \( \rulename{RAA} \). Then say in one sentence why your derivation does not give \( Q \).
2. Derive \( \neg P \to Q, \ \neg P \to \neg Q \vdash P \), using \( \rulename{RAA} \).
:::

*Hint: in (a) the goal is a negation; in (b) it is a letter.*
:::

::: {.solution}
(a) The goal \( \neg\neg Q \) is a negation, so we open a \( \rulename{\neg I} \) box on \( \neg Q \), with the goal \( \bot \). The premises are negations, so each can only clash: \( \neg\neg P \) against \( \neg P \), and \( \neg\neg(P \to Q) \) against \( \neg(P \to Q) \). Both of those are negations, so each is itself a subgoal for a \( \rulename{\neg I} \) box. Make \( \neg P \) the subgoal: a box on \( P \). Inside it, make \( \neg(P \to Q) \) the subgoal: a box on \( P \to Q \), where \( \rulename{{\to}E} \) gives \( Q \), which clashes with \( \neg Q \). The boxes then close from the inside out.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg\neg P}
  \hypo {2} {\neg\neg (P \to Q)}
  \open
  \hypo {3} {\neg Q}
  \open
  \hypo {4} {P}
  \open
  \hypo {5} {P \to Q}
  \have {6} {Q} \ie{5,4}
  \have {7} {\bot} \ne{6,3}
  \close
  \have {8} {\neg (P \to Q)} \ni{5-7}
  \have {9} {\bot} \ne{8,2}
  \close
  \have {10} {\neg P} \ni{4-9}
  \have {11} {\bot} \ne{10,1}
  \close
  \have {12} {\neg\neg Q} \ni{3-11}
\end{nd}$
\end{center}
```

All three boxes close by \( \rulename{\neg I} \), so no \( \rulename{RAA} \) is used. The derivation does not give \( Q \) because its last box opens with \( \neg Q \), and \( \rulename{\neg I} \) can only write the negation of that assumption, \( \neg\neg Q \); removing the two negations is \( \rulename{\neg\neg E} \), a classical step.

(b) The goal \( P \) is a letter, and both premises want \( \neg P \), which is nowhere. We are stuck, so we open an \( \rulename{RAA} \) box with \( \neg P \), and it feeds both premises:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P \to Q}
  \hypo {2} {\neg P \to \neg Q}
  \open
  \hypo {3} {\neg P}
  \have {4} {Q} \ie{1,3}
  \have {5} {\neg Q} \ie{2,3}
  \have {6} {\bot} \ne{4,5}
  \close
  \have {7} {P} \raa{3-6}
\end{nd}$
\end{center}
```

In words: "Suppose, for a contradiction, that \( P \) fails. Then the premises give both \( Q \) and \( \neg Q \), which is impossible. Hence \( P \)."
:::

::: {#exr-reductio-and-classical-rules-b2}
[B2: Back from negated sides, used later]

Derive \( \neg P \leftrightarrow \neg Q \vdash P \leftrightarrow Q \). Say where \( \rulename{RAA} \) enters and why.
:::

::: {.solution}
The goal is a biconditional, so by @def-rules-biconditional we need two boxes, one from \( P \) to \( Q \) and one from \( Q \) to \( P \). In the first, the goal \( Q \) is a letter and the premise speaks only about \( \neg Q \), so we are stuck: we assume \( \neg Q \) and argue by \( \rulename{RAA} \). The second box is symmetric.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P \leftrightarrow \neg Q}
  \open
  \hypo {2} {P}
  \open
  \hypo {3} {\neg Q}
  \have {4} {\neg P} \bie{1,3}
  \have {5} {\bot} \ne{2,4}
  \close
  \have {6} {Q} \raa{3-5}
  \close
  \open
  \hypo {7} {Q}
  \open
  \hypo {8} {\neg P}
  \have {9} {\neg Q} \bie{1,8}
  \have {10} {\bot} \ne{7,9}
  \close
  \have {11} {P} \raa{8-10}
  \close
  \have {12} {P \leftrightarrow Q} \bi{2-6,7-11}
\end{nd}$
\end{center}
```

\( \rulename{RAA} \) enters at lines 6 and 11: each inner goal is a letter, and the premise produces only negations. In the converse, \( P \leftrightarrow Q \vdash \neg P \leftrightarrow \neg Q \) (@exm-iff-negations), the inner goals are negations, \( \rulename{\neg I} \) builds them, and no \( \rulename{RAA} \) is used.
:::

::: {#exr-reductio-and-classical-rules-b3}
[B3: The redundant rule]

Show that \( \rulename{\bot E} \) is derivable from \( \rulename{RAA} \) and repetition: given a line \( \bot \), derive an arbitrary statement \( P \) in one box, without \( \rulename{\bot E} \).
:::

::: {.solution}
Open an \( \rulename{RAA} \) box with \( \neg P \) and repeat the \( \bot \) inside it:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\bot}
  \open
  \hypo {2} {\neg P}
  \have {3} {\bot} \r{1}
  \close
  \have {4} {P} \raa{2-3}
\end{nd}$
\end{center}
```

The repetition at line 3 is needed because \( \rulename{RAA} \) asks for \( \bot \) as a line of the box itself. So every use of \( \rulename{\bot E} \) can be replaced by these three lines; the book keeps the rule for the reason given in the remark after @thm-classical-rules-interderivable.
:::

::: {#exr-reductio-and-classical-rules-b4}
[B4: Stuck at a letter]

A search for \( (\neg P \to Q) \wedge (\neg P \to R), \ \neg(Q \wedge R) \vdash P \) has reached the stage below. *Name the move, then complete it.*

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {(\neg P \to Q) \wedge (\neg P \to R)}
  \hypo {2} {\neg (Q \wedge R)}
  \have[\ ][0] {} {\vdots}
  \have[][10] {10} {P}
\end{nd}$
\end{center}
```
:::

::: {.solution}
The goal \( P \) is a letter, so no introduction rule applies, and both halves of the first premise wait for \( \neg P \), which is nowhere. The move is *when stuck, assume the negation of the goal*: open an \( \rulename{RAA} \) box on \( \neg P \), and hunt for a clash. The assumption feeds both halves, and \( Q \wedge R \) then clashes with the second premise.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(\neg P \to Q) \wedge (\neg P \to R)}
  \hypo {2} {\neg (Q \wedge R)}
  \open
  \hypo {3} {\neg P}
  \have {4} {\neg P \to Q} \ae{1}
  \have {5} {Q} \ie{4,3}
  \have {6} {\neg P \to R} \ae{1}
  \have {7} {R} \ie{6,3}
  \have {8} {Q \wedge R} \ai{5,7}
  \have {9} {\bot} \ne{8,2}
  \close
  \have {10} {P} \raa{3-9}
\end{nd}$
\end{center}
```

The assumption on line 3 is cited twice, at lines 5 and 7; the clash on line 9 is between a line built from it and the second premise.
:::

::: {#exr-reductio-and-classical-rules-b5}
[B5: Derive or break, used later]

For each claim, derive it with any of the rules of Chapters 1 and 2, or break it by statements about a real number \( x \). In each derivation, mark the classical line (\( \rulename{RAA} \), or \( \rulename{\neg\neg E} \) or \( \rulename{LEM} \) used as a derived rule), if there is one. (A derivation by \( \rulename{RAA} \) of \( \Gamma \vdash \varphi \) derives \( \bot \) from \( \Gamma \) together with \( \neg\varphi \): from the counterexample set of the claim, @def-counterexample-set.)

::: {.enumerate options="label=(\alph*)"}
1. \( P \vee Q, \ \neg P \vee R \vdash Q \vee R \).
2. \( \neg(P \wedge Q) \vdash \neg P \wedge \neg Q \).
3. \( P \to Q \vdash (P \leftrightarrow Q) \vee Q \).
4. \( (P \to Q) \vee (P \to R) \vdash P \to (Q \wedge R) \).
5. \( \neg\neg P \vee Q \vdash P \vee Q \).
6. \( \neg(P \leftrightarrow Q) \vdash P \leftrightarrow \neg Q \).
7. \( \neg(P \leftrightarrow Q) \vdash \neg P \wedge Q \).
8. \( (P \wedge Q) \to R \vdash (P \to R) \vee (Q \to R) \).
:::
:::

::: {.solution}
(a) Derive, with no classical line. Split on the first premise; in the case \( P \), split on the second, where the case \( \neg P \) closes itself.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \hypo {2} {\neg P \vee R}
  \open
  \hypo {3} {P}
  \open
  \hypo {4} {\neg P}
  \have {5} {\bot} \ne{3,4}
  \have {6} {Q \vee R} \be{5}
  \close
  \open
  \hypo {7} {R}
  \have {8} {Q \vee R} \oi{7}
  \close
  \have {9} {Q \vee R} \oe{2,4-6,7-8}
  \close
  \open
  \hypo {10} {Q}
  \have {11} {Q \vee R} \oi{10}
  \close
  \have {12} {Q \vee R} \oe{1,3-9,10-11}
\end{nd}$
\end{center}
```

(b) Break. Take \( P \): "\( x > 0 \)", \( Q \): "\( x > 5 \)". At \( x = 1 \), \( P \wedge Q \) is false, so \( \neg(P \wedge Q) \) is true, and \( \neg P \) is false, so \( \neg P \wedge \neg Q \) is false: the counterexample set \( \neg(P \wedge Q) \), \( \neg(\neg P \wedge \neg Q) \) is true. This is the wrong De Morgan law.

(c) Derive; the classical line is line 2, \( \rulename{LEM} \) (@prp-excluded-middle as a derived rule). Each side of the goal breaks on its own: with \( P \): "\( x > 5 \)", \( Q \): "\( x > 3 \)", the premise holds at every \( x \), \( P \leftrightarrow Q \) fails at \( x = 4 \) and \( Q \) at \( x = 0 \). So decide a letter first. The letter is \( Q \): in the case \( Q \) the right side is in hand, and in the case \( \neg Q \) the premise and the clash with \( \neg Q \) build \( P \leftrightarrow Q \) in two boxes.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \have {2} {Q \vee \neg Q} \lem{}
  \open
  \hypo {3} {Q}
  \have {4} {(P \leftrightarrow Q) \vee Q} \oi{3}
  \close
  \open
  \hypo {5} {\neg Q}
  \open
  \hypo {6} {P}
  \have {7} {Q} \ie{1,6}
  \close
  \open
  \hypo {8} {Q}
  \have {9} {\bot} \ne{8,5}
  \have {10} {P} \be{9}
  \close
  \have {11} {P \leftrightarrow Q} \bi{6-7,8-10}
  \have {12} {(P \leftrightarrow Q) \vee Q} \oi{11}
  \close
  \have {13} {(P \leftrightarrow Q) \vee Q} \oe{2,3-4,5-12}
\end{nd}$
\end{center}
```

Deciding \( P \) first, as the Idea of @prp-implication-as-disjunction (b) does, would leave the case \( \neg P \) with neither side in hand.

(d) Break. Take \( P \): "\( x > 0 \)", \( Q \): "\( x > -1 \)", \( R \): "\( x > 5 \)". At \( x = 1 \), \( P \to Q \) is true, so the premise is, and \( Q \wedge R \) is false while \( P \) is true, so \( P \to (Q \wedge R) \) is false: the counterexample set is true.

(e) Derive; the classical line is line 3, \( \rulename{\neg\neg E} \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg\neg P \vee Q}
  \open
  \hypo {2} {\neg\neg P}
  \have {3} {P} \nne{2}
  \have {4} {P \vee Q} \oi{3}
  \close
  \open
  \hypo {5} {Q}
  \have {6} {P \vee Q} \oi{5}
  \close
  \have {7} {P \vee Q} \oe{1,2-4,5-6}
\end{nd}$
\end{center}
```

(f) Derive; the classical line is line 21, \( \rulename{RAA} \). The goal is a biconditional, so two boxes. In the first, \( \neg Q \) is a negation and \( \rulename{\neg I} \) builds it; in the second, the goal \( P \) is a letter, and an \( \rulename{RAA} \) box on \( \neg P \) gives the clash.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \leftrightarrow Q)}
  \open
  \hypo {2} {P}
  \open
  \hypo {3} {Q}
  \open
  \hypo {4} {P}
  \have {5} {Q} \r{3}
  \close
  \open
  \hypo {6} {Q}
  \have {7} {P} \r{2}
  \close
  \have {8} {P \leftrightarrow Q} \bi{4-5,6-7}
  \have {9} {\bot} \ne{8,1}
  \close
  \have {10} {\neg Q} \ni{3-9}
  \close
  \open
  \hypo {11} {\neg Q}
  \open
  \hypo {12} {\neg P}
  \open
  \hypo {13} {P}
  \have {14} {\bot} \ne{13,12}
  \have {15} {Q} \be{14}
  \close
  \open
  \hypo {16} {Q}
  \have {17} {\bot} \ne{16,11}
  \have {18} {P} \be{17}
  \close
  \have {19} {P \leftrightarrow Q} \bi{13-15,16-18}
  \have {20} {\bot} \ne{19,1}
  \close
  \have {21} {P} \raa{12-20}
  \close
  \have {22} {P \leftrightarrow \neg Q} \bi{2-10,11-21}
\end{nd}$
\end{center}
```

(g) Break. Take \( P \): "\( x > 0 \)", \( Q \): "\( x > 5 \)". At \( x = 1 \), \( P \) is true and \( Q \) false, so \( P \leftrightarrow Q \) is false and the premise is true; \( \neg P \) is false, so \( \neg P \wedge Q \) is false.

(h) Derive; the classical line is line 14, \( \rulename{RAA} \). Each side of the goal breaks on its own: with \( P \): "\( x > 0 \)", \( Q \): "\( x > 5 \)", \( R \): "\( x > 3 \)", the premise holds at every \( x \) and \( P \to R \) fails at \( x = 1 \); exchanging the statements for \( P \) and \( Q \) breaks the step to \( Q \to R \) at the same \( x \). So assume the negation of the whole goal. Inside, the box on \( P \) turns the clash into \( R \), and the box on \( Q \) inside it builds \( P \wedge Q \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge Q) \to R}
  \open
  \hypo {2} {\neg ((P \to R) \vee (Q \to R))}
  \open
  \hypo {3} {P}
  \open
  \hypo {4} {Q}
  \have {5} {P \wedge Q} \ai{3,4}
  \have {6} {R} \ie{1,5}
  \close
  \have {7} {Q \to R} \ii{4-6}
  \have {8} {(P \to R) \vee (Q \to R)} \oi{7}
  \have {9} {\bot} \ne{8,2}
  \have {10} {R} \be{9}
  \close
  \have {11} {P \to R} \ii{3-10}
  \have {12} {(P \to R) \vee (Q \to R)} \oi{11}
  \have {13} {\bot} \ne{12,2}
  \close
  \have {14} {(P \to R) \vee (Q \to R)} \raa{2-13}
\end{nd}$
\end{center}
```

(a) needs no classical line, although its goal is a disjunction, because each case of the premise hands over one side. (c) and (h) are disjunctions whose sides break on their own, the place "When \( \rulename{RAA} \) earns its place" points to, and the answers use both classical tools there: (c) decides a letter first with \( \rulename{LEM} \), as @prp-implication-as-disjunction (b) does, but the letter is \( Q \), a side of the goal, not \( P \); (h) assumes the negation of the goal. In (f) the classical line closes a box whose goal is a letter, \( P \) from \( \neg Q \), as in @prp-double-negation, the other case that paragraph names; the box \( \lines{2}{10} \) of (f) has no classical line. (b), (d) and (g) are look-alikes. Worked examples of these types: @prp-excluded-middle, @prp-de-morgan (d), Exercise C3.

**Marking scheme.** (16 points) For each claim: 1 for the verdict; 1 for a derivation every line of which checks, with the classical line correctly marked, or for a choice of statements and one value of \( x \) at which **every** member of the counterexample set is true. Fatal errors (0 for the claim): a "break" at which a premise fails; a classical line not marked, or a non-classical line marked as classical.
:::

::: {#exr-reductio-and-classical-rules-b6}
[B6: A law that sounds false]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( (P \to Q) \vee (Q \to P) \) cannot be broken: whatever statements \( P \) and \( Q \) are, one disjunct is true.
2. Let \( n \) be an integer, \( P \): "\( n \) is even", \( Q \): "\( n > 5 \)". Check the statement at \( n = 2 \) and at \( n = 7 \), saying which disjunct holds.
3. The sentence "every even integer is greater than \( 5 \), or every integer greater than \( 5 \) is even" is false. Why is that no counterexample to (a)?
4. Show that each disjunct, as a claim from no premises, breaks. Which move of this section does a derivation of \( (P \to Q) \vee (Q \to P) \) then call for?
:::
:::

::: {.solution}
(a) If \( P \) is false, \( P \to Q \) is true, since its hypothesis fails. If \( P \) is true, \( Q \to P \) is true, since its conclusion holds. Either way one disjunct is true.

(b) At \( n = 2 \): \( P \) is true and \( Q \) false, so \( Q \to P \) holds (and \( P \to Q \) fails). At \( n = 7 \): \( P \) is false and \( Q \) true, so \( P \to Q \) holds (and \( Q \to P \) fails).

(c) The false sentence puts "every" in front of each disjunct separately: (for every \( n \), \( P \to Q \)) or (for every \( n \), \( Q \to P \)). The value \( n = 2 \) refutes the first and \( n = 7 \) the second. What (a) gives is, for each \( n \), the disjunction itself, as (b) checked at two values. "Every" does not pass inside an "or". This is the point of "Two sequents that sound wrong" in Section 2.1: the mathematical "if" sits under an "every".

(d) \( P \to Q \) breaks with \( P \): "\( x > 0 \)", \( Q \): "\( x > 5 \)", at \( x = 1 \); \( Q \to P \) breaks with the same two statements exchanged, at \( x = 1 \). So \( \rulename{\vee I} \) from either side is not worth aiming at, and the goal is a disjunction with neither side within reach: the case of "When \( \rulename{RAA} \) earns its place", and the move *when stuck, assume the negation of the goal*. (The derivation itself is Exercise C2 of Section 3.1, where the search method finds it; Chapter 4 states, without proof, that every derivation of it uses \( \rulename{RAA} \) or one of its equivalents.)

**Marking scheme.** (10 points) 3: (a), both cases. 2: (b), the disjunct that holds at each value. 3: (c), the scope of "every" named, with a refuting value for each separated disjunct. 2: (d), the two breaks and the move named. Fatal error (0 for (c)): calling the false sentence an instance of (a).
:::

### C. Going deeper

::: {#exr-reductio-and-classical-rules-c1}
[C1: Challenge: Excluded middle does the work of reductio directly]

Suppose that, instead of \( \rulename{RAA} \), we had \( \rulename{LEM} \) as a rule: \( \varphi \vee \neg\varphi \) may be written on any line, for any statement \( \varphi \).

Given a box that opens with \( \neg\varphi \) and reaches \( \bot \), derive \( \varphi \) using \( \rulename{LEM} \), \( \rulename{\vee E} \), \( \rulename{\bot E} \), and the other primitive rules, but neither \( \rulename{RAA} \) nor \( \rulename{\neg\neg E} \). Write the case \( \neg\varphi \) as the given box, extended.
:::

::: {.solution}
[Hint 1]

Write \( \varphi \vee \neg\varphi \) just before the given box. What must each of the two case boxes end with?
:::

::: {.solution}
[Hint 2]

The first case box is a single line.
:::

::: {.solution}
Write excluded middle for \( \varphi \) just before the given box, and use the box as the second case of \( \rulename{\vee E} \), extended by one line:

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {h} {\varphi \vee \neg \varphi} \lem{}
  \open
  \hypo {h+1} {\varphi} \purpose{\oe}
  \close
  \open
  \hypo {i} {\neg \varphi} \purpose{\oe}
  \have {} {\vdots}
  \have {j} {\bot}
  \have {j+1} {\varphi} \be{j}
  \close
  \have {k} {\varphi} \oe{h,h+1-h+1,i-j+1}
\end{nd}$
\end{center}
```

Here \( i = h + 2 \). The first case is a one-line box that already ends with the goal. The second case is the given box with one more line, \( \rulename{\bot E} \) on its \( \bot \); its lines are unchanged and cite what they cited before, since the box has not moved into or out of any other box. No \( \rulename{RAA} \) and no \( \rulename{\neg\neg E} \) is used.
:::

::: {#exr-reductio-and-classical-rules-c2}
[C2: Find the error, used later]

A student derives \( \neg(\neg P \wedge \neg Q) \vdash P \vee Q \) as follows.

```{=latex}
% expect-invalid
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (\neg P \wedge \neg Q)}
  \have {2} {P \vee \neg P} \lem{}
  \open
  \hypo {3} {P}
  \have {4} {P \vee Q} \oi{3}
  \close
  \open
  \hypo {5} {\neg P}
  \have {6} {\bot} \ne{3,5}
  \have {7} {Q} \be{6}
  \have {8} {P \vee Q} \oi{7}
  \close
  \have {9} {P \vee Q} \oe{2,3-4,5-8}
\end{nd}$
\end{center}
```

::: {.enumerate options="label=(\alph*)"}
1. Is the sequent \( \neg(\neg P \wedge \neg Q) \vdash P \vee Q \) derivable?
2. Does the student's derivation derive it? Name the first line that fails and the rule or clause it breaks.
3. Show that the illegal step, if it were allowed, would prove too much: use the same move to "derive" \( P \vee Q \vdash P \), and break that sequent.
4. Give a correct derivation.
:::
:::

::: {.solution}
(a) Yes: part (d) below gives a derivation. The conclusion is true, and the argument is still wrong.

(b) No. Line 6 fails: it cites line 3, the assumption of the first case box, lines 3–4, which closed before line 5. By the scope rule of @def-derivation, line 3 is not available at line 6. The form of \( \rulename{\neg E} \) is right; what is broken is availability. In words, the student used the assumption of one case inside the other case, where it has not been assumed.

(c) The same move derives \( P \vee Q \vdash P \): split on the premise by \( \rulename{\vee E} \), with a first box that opens with \( P \) and ends there, and a second box that opens with \( Q \) and "repeats" \( P \) from the first. That sequent breaks: with \( P \) false and \( Q \) true the premise is true and the conclusion false, so the move can carry a true premise to a false conclusion. So citing a line of a sibling box is illegal in general, not just unlucky here.

(d) Keep lines 1–5, and in the case \( \neg P \) we are stuck at the goal \( Q \), so we argue for it by \( \rulename{RAA} \), using the premise:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (\neg P \wedge \neg Q)}
  \have {2} {P \vee \neg P} \lem{}
  \open
  \hypo {3} {P}
  \have {4} {P \vee Q} \oi{3}
  \close
  \open
  \hypo {5} {\neg P}
  \open
  \hypo {6} {\neg Q}
  \have {7} {\neg P \wedge \neg Q} \ai{5,6}
  \have {8} {\bot} \ne{7,1}
  \close
  \have {9} {Q} \raa{6-8}
  \have {10} {P \vee Q} \oi{9}
  \close
  \have {11} {P \vee Q} \oe{2,3-4,5-10}
\end{nd}$
\end{center}
```

Line 7 cites line 5, the assumption of the enclosing case box, which is still open: the legal version of what the student wanted.
:::

::: {#exr-reductio-and-classical-rules-c3}
[C3: Exit check: a classical disjunction]

Derive \( \vdash P \vee (P \to Q) \) using the **primitive** rules only (those of Chapter 1, \( \rulename{\neg E} \), \( \rulename{\bot E} \), \( \rulename{\neg I} \), \( \rulename{{\leftrightarrow}I} \), \( \rulename{{\leftrightarrow}E} \), and \( \rulename{RAA} \)), with no derived rule, so neither \( \rulename{LEM} \) nor \( \rulename{\neg\neg E} \) as a single line. Name the rule on every line, and say which line is classical.
:::

::: {.solution}
*The search.* The goal is a disjunction, so we postpone it; there are no premises, so no premise-directed move applies; and neither side is worth aiming at: \( P \) false breaks the step to \( P \), and \( P \) true with \( Q \) false breaks the step to \( P \to Q \). We are stuck, so we assume the exact negation of the goal, \( \neg(P \vee (P \to Q)) \), and hunt for a clash. The assumption can clash only with \( P \vee (P \to Q) \), which \( \rulename{\vee I} \) builds from either side. The side \( P \to Q \) is an implication, so we open a box on \( P \) with the goal \( Q \). Inside it, \( \rulename{\vee I} \) gives \( P \vee (P \to Q) \) from \( P \), which clashes with the assumption, and \( \rulename{\bot E} \) writes \( Q \). So \( P \to Q \) holds, \( \rulename{\vee I} \) gives the goal, and that is the second clash.

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {\neg (P \vee (P \to Q))}
  \open
  \hypo {2} {P}
  \have {3} {P \vee (P \to Q)} \oi{2}
  \have {4} {\bot} \ne{3,1}
  \have {5} {Q} \be{4}
  \close
  \have {6} {P \to Q} \ii{2-5}
  \have {7} {P \vee (P \to Q)} \oi{6}
  \have {8} {\bot} \ne{7,1}
  \close
  \have {9} {P \vee (P \to Q)} \raa{1-8}
\end{nd}$
\end{center}
```

Lines 1 and 2 are assumptions, of the \( \rulename{RAA} \) box and of the \( \rulename{{\to}I} \) box; every other line names its rule on the right. The classical line is line 9; every other rule used is a rule for a connective. The shape is that of @prp-excluded-middle: there the inner box closed by \( \rulename{\neg I} \) to give \( \neg P \); here it ends with \( \rulename{\bot E} \) and closes by \( \rulename{{\to}I} \) to give \( P \to Q \).

A second correct route first derives \( P \vee \neg P \) by the eight lines of @prp-excluded-middle, written out, and then splits on it: in the case \( P \), \( \rulename{\vee I} \) gives the goal; in the case \( \neg P \), a box on \( P \) clashes with \( \neg P \), \( \rulename{\bot E} \) writes \( Q \), \( \rulename{{\to}I} \) gives \( P \to Q \), and \( \rulename{\vee I} \) the goal. Its classical line is the \( \rulename{RAA} \) inside the written-out excluded middle.

**Marking scheme.** (10 points)

- 2: an \( \rulename{RAA} \) box opened with \( \neg(P \vee (P \to Q)) \), the exact negation of the goal.
- 3: an inner box on \( P \) that reaches \( \bot \) by \( \rulename{\vee I} \) and \( \rulename{\neg E} \) against the outer assumption, and then \( Q \) by \( \rulename{\bot E} \).
- 2: \( P \to Q \) by \( \rulename{{\to}I} \), then \( P \vee (P \to Q) \) by \( \rulename{\vee I} \), and the second clash.
- 2: \( \rulename{RAA} \) closes the outer box, and it is named as the classical step.
- 1: every citation is available.

The second route earns the same points, step for step: 2 for the written-out excluded middle opened correctly (its \( \rulename{RAA} \) box on \( \neg(P \vee \neg P) \)); 3 for the box on \( P \) in the case \( \neg P \), closed by \( \rulename{\bot E} \); 2 for \( \rulename{{\to}I} \), the two \( \rulename{\vee I} \) lines, and the \( \rulename{\vee E} \); 2 for naming the \( \rulename{RAA} \) inside excluded middle as the classical step; 1 for availability. Fatal errors (0 for the step): opening the outer box with anything but \( \neg(P \vee (P \to Q)) \); closing the outer box by \( \rulename{\neg I} \) (that gives \( \neg\neg(P \vee (P \to Q)) \)); a line justified by \( \rulename{\neg\neg E} \) or \( \rulename{LEM} \) taken as a rule, which the item excludes.
:::

::: {#exr-reductio-and-classical-rules-c4}
[C4: Challenge: Smaller rule sets]

::: {.enumerate options="label=(\alph*)"}
1. Show that, once \( \rulename{RAA} \) is a rule, \( \rulename{\neg I} \) could be dropped: given a box that opens with \( \varphi \) and reaches \( \bot \) as a line of its own, derive \( \neg\varphi \) with \( \rulename{RAA} \), \( \rulename{\neg E} \) and the box's lines, without \( \rulename{\neg I} \). Use your method to derive @prp-modus-tollens without \( \rulename{\neg I} \).
2. With neither \( \rulename{\bot E} \) nor \( \rulename{RAA} \) (\( \rulename{\neg I} \) allowed), derive \( \neg P \vdash P \to \neg Q \).
3. Exercise B3 derived \( \rulename{\bot E} \) from \( \rulename{RAA} \) and repetition. Does its derivation use \( \rulename{\neg I} \), and does your fragment in (a) use \( \rulename{\bot E} \)? What do (a) and B3 together say about the list of thirteen primitive rules?
4. Which of the two paradoxes of Section 2.1 survives in a system with neither \( \rulename{\bot E} \) nor \( \rulename{RAA} \), by the derivation given there?
:::
:::

::: {.solution}
(a) Replace the old box by this one. Line \( i \): \( \neg\neg\varphi \), assumption, for \( \rulename{RAA} \). Line \( i + 1 \): \( \neg\varphi \), assumption, for \( \rulename{RAA} \). Line \( i + 2 \): \( \bot \), \( \rulename{\neg E} \) \( i + 1 \), \( i \). Line \( i + 3 \): \( \varphi \), \( \rulename{RAA} \) \( \lines{i+1}{i+2} \). Then the old box's lines after its assumption, renumbered, each citation of the old assumption now citing line \( i + 3 \); the last of them is \( \bot \), a line of the new box. Then \( \neg\varphi \), by \( \rulename{RAA} \) on the new box: \( \rulename{RAA} \) writes \( \psi \) from a box opened by \( \neg\psi \), here with \( \psi \) the statement \( \neg\varphi \). Every old citation stays available: the old lines sit in the new box exactly as they sat in the old one, and line \( i + 3 \) is a line of that box.

For modus tollens:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {\neg Q}
  \open
  \hypo {3} {\neg\neg P}
  \open
  \hypo {4} {\neg P}
  \have {5} {\bot} \ne{4,3}
  \close
  \have {6} {P} \raa{4-5}
  \have {7} {Q} \ie{1,6}
  \have {8} {\bot} \ne{7,2}
  \close
  \have {9} {\neg P} \raa{3-8}
\end{nd}$
\end{center}
```

(b) A box on \( P \), and inside it a box on \( Q \) whose \( \bot \) comes from the clash of \( P \) with the premise:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P}
  \open
  \hypo {2} {P}
  \open
  \hypo {3} {Q}
  \have {4} {\bot} \ne{2,1}
  \close
  \have {5} {\neg Q} \ni{3-4}
  \close
  \have {6} {P \to \neg Q} \ii{2-5}
\end{nd}$
\end{center}
```

The \( \rulename{\neg I} \) box never uses its assumption; the fold "Edge cases of not-introduction" of Section 2.2 explains why that is legal: the lines above it, \( P \) and \( \neg P \), already clash.

(c) No, and no: B3 uses \( \rulename{RAA} \) and repetition only, and (a) uses \( \rulename{RAA} \) and \( \rulename{\neg E} \) only. So \( \rulename{\bot E} \) and \( \rulename{\neg I} \) can be dropped together, and the remaining eleven rules derive every sequent the thirteen do (replace the lines one at a time, innermost boxes first). The book keeps both for the reason the remark after @thm-classical-rules-interderivable gives for \( \rulename{\bot E} \): the primitive rules other than \( \rulename{RAA} \) are to form a system of their own.

(d) \( Q \vdash P \to Q \): its derivation uses \( \rulename{{\to}I} \) and repetition only. The derivation of \( \neg P \vdash P \to Q \) given in Section 2.1 uses \( \rulename{\bot E} \).

**Marking scheme.** (10 points) 5: (a), the general replacement (2 for the inner \( \rulename{RAA} \) producing \( \varphi \); 1 for re-citing the old assumption; 1 for closing by \( \rulename{RAA} \) with \( \psi \) the statement \( \neg\varphi \)) and 1 for the modus tollens derivation. 2: (b). 2: (c), both answers and the conclusion about the list. 1: (d). Fatal error (0 for (a)): closing the new box by \( \rulename{\neg I} \), or opening it with \( \varphi \).
:::

### R. Review

::: {#exr-reductio-and-classical-rules-r1}
[R1]

Let \( n \) be an integer. Prove that \( n^2 \ne 4n + 2 \), naming the rule at each logical step.
:::

::: {.solution}
The goal is \( \neg(n^2 = 4n + 2) \), a negation, so we use \( \rulename{\neg I} \). Suppose \( n^2 = 4n + 2 \) [assumption for \( \rulename{\neg I} \)]. Then \( n^2 = 2(2n + 1) \) is even, so \( n \) is even by @thm-square-even-implies-even [\( \rulename{{\to}E} \)]; write \( n = 2k \) with \( k \) an integer. Then \( 4k^2 = 8k + 2 \), so \( 2k^2 = 4k + 1 \). The left side is even and the right side odd, so \( 2k^2 \) is both even and odd [\( \rulename{\wedge I} \)], and no integer is both [\( \rulename{\neg E} \) with (E2)]. Hence \( n^2 \ne 4n + 2 \) [\( \rulename{\neg I} \)].

There is no \( \rulename{RAA} \) here: the box opens with the unnegated equation, and the conclusion is its negation.
:::

::: {#exr-reductio-and-classical-rules-r2}
[R2]

Call an integer \( n \) **balanced** if \( n \) is even exactly when \( n \) is a multiple of \( 3 \). Write \( E \): "\( n \) is even", \( T \): "\( n \) is a multiple of \( 3 \)".

::: {.enumerate options="label=(\alph*)"}
1. Write "\( n \) is balanced" in \( E \) and \( T \), and decide it for \( n = 4, 6, 7, 9 \).
2. Show that "\( n \) is balanced" says the same as "\( n \) is both even and a multiple of \( 3 \), or neither", by deriving \( E \leftrightarrow T \dashv\vdash (E \wedge T) \vee (\neg E \wedge \neg T) \). In which direction does your derivation use a classical line (\( \rulename{RAA} \), \( \rulename{\neg\neg E} \) or \( \rulename{LEM} \))?
:::
:::

::: {.solution}
(a) \( E \leftrightarrow T \): a definition's "if" is read as an iff (Section 2.4). At \( 4 \), \( E \) is true and \( T \) false: not balanced. At \( 6 \), both are true: balanced. At \( 7 \), both are false: balanced. At \( 9 \), \( E \) is false and \( T \) true: not balanced.

(b) Left to right; the classical line is line 2, \( \rulename{LEM} \) (@prp-excluded-middle as a derived rule):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {E \leftrightarrow T}
  \have {2} {E \vee \neg E} \lem{}
  \open
  \hypo {3} {E}
  \have {4} {T} \bie{1,3}
  \have {5} {E \wedge T} \ai{3,4}
  \have {6} {(E \wedge T) \vee (\neg E \wedge \neg T)} \oi{5}
  \close
  \open
  \hypo {7} {\neg E}
  \open
  \hypo {8} {T}
  \have {9} {E} \bie{1,8}
  \have {10} {\bot} \ne{9,7}
  \close
  \have {11} {\neg T} \ni{8-10}
  \have {12} {\neg E \wedge \neg T} \ai{7,11}
  \have {13} {(E \wedge T) \vee (\neg E \wedge \neg T)} \oi{12}
  \close
  \have {14} {(E \wedge T) \vee (\neg E \wedge \neg T)} \oe{2,3-6,7-13}
\end{nd}$
\end{center}
```

Right to left, with no classical line:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(E \wedge T) \vee (\neg E \wedge \neg T)}
  \open
  \hypo {2} {E \wedge T}
  \open
  \hypo {3} {E}
  \have {4} {T} \ae{2}
  \close
  \open
  \hypo {5} {T}
  \have {6} {E} \ae{2}
  \close
  \have {7} {E \leftrightarrow T} \bi{3-4,5-6}
  \close
  \open
  \hypo {8} {\neg E \wedge \neg T}
  \open
  \hypo {9} {E}
  \have {10} {\neg E} \ae{8}
  \have {11} {\bot} \ne{9,10}
  \have {12} {T} \be{11}
  \close
  \open
  \hypo {13} {T}
  \have {14} {\neg T} \ae{8}
  \have {15} {\bot} \ne{13,14}
  \have {16} {E} \be{15}
  \close
  \have {17} {E \leftrightarrow T} \bi{9-12,13-16}
  \close
  \have {18} {E \leftrightarrow T} \oe{1,2-7,8-17}
\end{nd}$
\end{center}
```

The classical line of these derivations is in the left-to-right direction, the \( \rulename{LEM} \) at line 2. There the goal is a disjunction neither of whose sides holds for every balanced \( n \) (at \( n = 7 \) the left fails, at \( n = 6 \) the right): the case "When \( \rulename{RAA} \) earns its place" names.
:::

::: {#exr-reductio-and-classical-rules-r3}
[R3]

Let \( n \) be an integer, \( P \): "\( n \) is a multiple of \( 6 \)", \( Q \): "\( n \) is even", so that \( P \to Q \) is true. For each statement, say whether it follows from \( P \to Q \) by the rules of Chapters 1 and 2, naming the result that gives it, or break the step from \( P \to Q \) to it at a value of \( n \): (i) \( \neg Q \to \neg P \); (ii) \( Q \to P \); (iii) \( \neg P \to \neg Q \); (iv) \( \neg P \vee Q \); (v) \( P \to (P \wedge Q) \); (vi) \( P \leftrightarrow Q \). Which of the derivations you cite uses a classical line (\( \rulename{RAA} \), \( \rulename{\neg\neg E} \) or \( \rulename{LEM} \))?
:::

::: {.solution}
(i) Follows: @prp-contrapositive (\( \rulename{CP} \)).

(ii) Breaks at \( n = 2 \): \( P \to Q \) is true, \( Q \) is true and \( P \) false, so \( Q \to P \) is false.

(iii) Breaks at \( n = 2 \): \( \neg P \) is true and \( \neg Q \) false.

(iv) Follows: @prp-implication-as-disjunction, the direction \( P \to Q \vdash \neg P \vee Q \), whose derivation in this section uses \( \rulename{LEM} \). It is the one cited derivation with a classical line.

(v) Follows, with no classical line:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \open
  \hypo {2} {P}
  \have {3} {Q} \ie{1,2}
  \have {4} {P \wedge Q} \ai{2,3}
  \close
  \have {5} {P \to (P \wedge Q)} \ii{2-4}
\end{nd}$
\end{center}
```

(vi) Breaks at \( n = 2 \): \( P \) is false and \( Q \) true.

The breaks are of the step with this \( P \) and \( Q \): at \( n = 2 \) the premise is true (a multiple of \( 6 \) is \( 6k = 2(3k) \), so \( P \to Q \) holds for every \( n \)) and the conclusion false, so the form is bad.
:::

<!-- dependency ledger
exm-raa-at-most-one (example): x > 1 gives x > 0 and x^2 > x (multiply x > 1 by x > 0); "x <= 1 fails" is x > 1 | school algebra, AN1.1 (promised); the order convention of F1.2 s01; checked by verify/ch02/exm-raa-at-most-one.py
exm-raa-at-most-one (example): in the derivation after def-rule-raa and its instances of parts 2 and 3, line 3 "algebra 2" (not x <= 1 gives x > 1) and line 4 "algebra 3" (x > 1 gives x^2 > x, written not(x^2 <= x)) | school algebra, AN1.1 (promised); the order convention of F1.2 s01
def-rule-raa (claim): no derivation of P from not-not-P uses only the rules of F1.1 and s01-s04 | F1.3 (promised; thm-raa-independent, optional there); stated only as a claim "which no search can settle", with the Looking-ahead box saying where it is proved; the motivation for RAA, nothing proved from it
def-rule-raa (claim): in the fold "RAA is never needed to finish a negation", the last step of a derivation of a negation never needs RAA (replace the RAA box on not-not-psi by a not-I box on psi) | inline (argued in the paragraph, using exm-double-negation-introduction)
prp-excluded-middle (idea): P false breaks the step to P, P true breaks the step to not-P | read off Section 1.1's test (breaking); motivation only
prp-de-morgan (idea): the step from not(P and Q) to not-P breaks (P true, Q false), and the step to not-Q breaks (P false, Q true) | read off Section 1.1's test (breaking); motivation only, the proof does not use it
prp-de-morgan (claim): in the fold "De Morgan (d) by excluded middle", the LEM route to (d) is 11 lines | described inline; nothing depends on it
thm-classical-rules-interderivable (proof): replacing a line by a fragment keeps every citation available and the premises and last line unchanged | inline (argued in the proof)
exm-raa-zero (example): x >= 0 and x != 0 give x > 0; x/2 > 0 for x > 0; subtracting x/2 and multiplying by 2 preserve <= | school algebra, AN1.1 (promised)
exm-raa-zero (example): the hypothesis "x <= eps for every eps > 0" applies to eps = x/2 | F1.4 (promised; rules for "every"), used as ordinary reasoning under the index note; the example illustrates the shape of RAA and nothing cites it for its logic
exm-raa-zero (example): in the rule-by-rule reading, x >= 0 read as (x = 0 or x > 0), and x > 0 read as not(x <= 0) | school algebra (trichotomy), AN1.1 (promised); the order convention of F1.2 s01
exm-raa-zero (claim): in the x^3 comparison of "Not-I or RAA?" after it, x >= 0 implies x^3 = x*x*x >= 0; "x^3 not >= 0" is x^3 < 0 and "x not >= 0" is x < 0 | school algebra, AN1.1 (promised); the order convention of F1.2 s01; checked by verify/ch02/exm-raa-at-most-one.py
exm-raa-zero (claim): in the Quick check after "Not-I or RAA?", 15 = 3 * 5 is not prime | arithmetic
exm-reductio-and-classical-rules-instances (example): in the Not-allowed WRONG/RIGHT pair after it, (x > 2 or x < -2) implies x^2 > 4 for every real x; at x = 0, not(x^2 > 4) holds and x > 2 fails | school algebra, AN1.1 (promised); checked by verify/ch02/exm-reductio-and-classical-rules-instances.py
exm-reductio-and-classical-rules-instances (claim): in the Quick check after the Not-allowed block, x != 2 is not(x = 2) | the order convention of F1.2 s01 (a != b as not(a = b))
exr-reductio-and-classical-rules-a1 (solution): squares are non-negative; 3 < 7/2 < 4; x^2 < 2x - 1 iff (x - 1)^2 < 0 | school algebra, AN1.1 (promised)
exr-reductio-and-classical-rules-a1 (solution): in (e), the steps to not-P and to not-Q break at the two stated cases | read off Section 1.1's test (breaking)
exr-reductio-and-classical-rules-a2 (solution): in (d), "not x >= 2" is x < 2; x = 2 satisfies both x <= 2 and x >= 2 | school algebra; the order convention of F1.2 s01
exr-reductio-and-classical-rules-a2 (solution): in (h), 9 = 3 * 3 is not prime | arithmetic
exr-reductio-and-classical-rules-b5 (solution): the breaks (b), (g) at x = 1 with x > 0, x > 5; (d) at x = 1 with x > 0, x > -1, x > 5; (c)'s sides at x = 4 and x = 0 with x > 5, x > 3; (h)'s sides at x = 1 with x > 0, x > 5, x > 3 | inline arithmetic; checked by verify/ch02/exr-reductio-and-classical-rules-b5.py
exr-reductio-and-classical-rules-b6 (solution): n = 2 is even and not > 5; n = 7 is odd and > 5; the breaks of P -> Q and Q -> P at x = 1 with x > 0, x > 5 | arithmetic; checked by verify/ch02/exr-reductio-and-classical-rules-b6.py
exr-reductio-and-classical-rules-b6 (solution): Chapter 4 states, without proof, that every derivation of (P -> Q) or (Q -> P) uses RAA or an equivalent; the derivation itself is exr-finding-derivations-c2 | plain pointers in a solution (F1.3, the remark after thm-raa-independent; F1.7 s01); nothing depends on them
exr-reductio-and-classical-rules-c2 (solution): P or Q |- P breaks (P false, Q true) | read off Section 1.1's test (breaking); the find-the-error verdict does not depend on it
exr-reductio-and-classical-rules-c3 (solution): P false breaks the step to P; P true and Q false break the step to P -> Q (the search's motivation) | read off Section 1.1's test (breaking); motivation only, the derivation does not depend on it
exr-reductio-and-classical-rules-c4 (solution): in (c), replacing the uses of bot-E and not-I one at a time, innermost boxes first, terminates and uses neither dropped rule | inline (each fragment uses RAA, not-E and repetition only)
exr-reductio-and-classical-rules-r1 (solution): n^2 = 4n + 2 = 2(2n + 1) is even; n = 2k gives 4k^2 = 8k + 2, so 2k^2 = 4k + 1, even against odd | thm-square-even-implies-even (cited), (E2) of F1.2 s01; arithmetic checked by verify/ch02/exr-reductio-and-classical-rules-r1.py
exr-reductio-and-classical-rules-r2 (solution): a definition's "if" read as an iff; 4, 6, 7, 9 against "even" and "multiple of 3" | F1.2 s04 (the definition convention); arithmetic checked by verify/ch02/exr-reductio-and-classical-rules-r2.py
exr-reductio-and-classical-rules-r3 (solution): a multiple of 6 is 6k = 2(3k), so even; n = 2 is even and not a multiple of 6 | arithmetic; checked by verify/ch02/exr-reductio-and-classical-rules-r3.py
-->
