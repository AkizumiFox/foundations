# Proof by Contradiction and the Classical Rules

Every rule so far either builds a statement or takes one apart. The rules for negation are no exception: \( \rulename{\neg I} \) (@def-rules-negation) builds \( \neg\varphi \) from a box that opens with \( \varphi \) and ends in \( \bot \), and \( \rulename{\neg E} \) (@def-rules-contradiction) uses \( \neg\varphi \) against \( \varphi \). Yet in three places this chapter has stopped one step short of a goal. This section adds the one rule that takes a negation away, reductio ad absurdum. It then derives from it the classical laws that mathematics uses without noticing, and shows that three of them are one principle in three forms.

## Two boxes that look alike

Here are two arguments that a mathematician would both call "proof by contradiction".

The first is the proof of @thm-sqrt2-irrational. It fixes a rational number \( r \), supposes \( r^2 = 2 \), reaches a contradiction, and concludes that \( r^2 \ne 2 \). In the language of @def-rules-negation, it opens a box with the assumption \( P \) ("\( r^2 = 2 \)"), reaches \( \bot \) inside it, and closes the box to get \( \neg P \). That is \( \rulename{\neg I} \).

The second is an argument of a kind that analysis uses constantly.

::: {#exm-raa-zero}
[A number below every positive number]

Let \( x \) be a real number with \( x \ge 0 \), and suppose that \( x \le \varepsilon \) for **every** real number \( \varepsilon > 0 \). Prove that \( x = 0 \).
:::

::: {.solution}
Suppose, for a contradiction, that \( x \ne 0 \). Since \( x \ge 0 \) and \( x \ne 0 \), we have \( x > 0 \). Then \( \varepsilon \coloneqq x/2 \) is a real number with \( \varepsilon > 0 \), so the hypothesis applies to it and gives \( x \le x/2 \). Subtracting \( x/2 \) from both sides gives \( x/2 \le 0 \), and multiplying by \( 2 \) gives \( x \le 0 \). This contradicts \( x > 0 \). Hence \( x = 0 \).
:::

(The step "the hypothesis applies to it" uses a rule for "every", which Chapter 4 makes precise. The facts about \( \le \) are school algebra, which Chapter 11 derives from axioms.)

Look at its shape. The box opens with the assumption \( \neg P \), where \( P \) is "\( x = 0 \)", reaches \( \bot \), and closes to give \( P \). If we tried to justify the last line by \( \rulename{\neg I} \), we would get the negation of the box's assumption, \( \neg\neg P \): "it is not the case that \( x \ne 0 \)". That is not \( P \). The two arguments put their negations in different places. \( \rulename{\neg I} \) puts a \( \neg \) **into** the conclusion; the second argument takes one **out**.

## Where the rules so far stop short

The second argument is not a curiosity. Three times already in this chapter a derivation has stopped short in the same way: it reached a negation where the goal was not one.

1. Section 2.2 warned against the argument "suppose \( x \) is not positive; …; hence \( x \) is positive". The box opens with \( \neg(x > 0) \) and reaches \( \bot \), so \( \rulename{\neg I} \) gives \( \neg\neg(x > 0) \), and no rule so far gets from there to \( x > 0 \).
2. In @exr-derived-rules-c1, the premises \( P \to Q \) and \( \neg P \to R \) led to \( \neg(\neg Q \wedge \neg R) \), "not both \( Q \) and \( R \) fail", and not to \( Q \vee R \).
3. Section 2.4 noted, after @exm-iff-negations, that its converse, \( \neg P \leftrightarrow \neg Q \vdash P \leftrightarrow Q \), resists the rules so far. The natural box on \( \neg Q \), inside the box of \( P \), closes to \( \neg\neg Q \), not \( Q \).

Try the smallest case, \( P \) from \( \neg\neg P \). The goal \( P \) is a letter, so no introduction rule applies: the goal-directed moves have nothing to say. The premise \( \neg\neg P \) is a negation, and a negation can be used only by \( \rulename{\neg E} \), against the statement it negates, \( \neg P \). So we assume \( \neg P \) in a box. The box reaches \( \bot \) at once, and \( \rulename{\neg I} \) closes it with \( \neg\neg P \): the premise again. Every attempt goes round this circle.

In fact no derivation of \( P \) from \( \neg\neg P \) uses only the rules of Chapter 1 and Sections 2.1–2.4. That is a claim about **all** derivations, and no search can prove it. Chapter 3 proves it (@thm-raa-independent), by reading statements with more than two truth values. For the other two stalls the same is true, but we state it without proof, and nothing in this book depends on it. Here we name the missing step and add it as a rule.

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

As in every schema (@def-rule-schema), \( \varphi \) stands for any statement and \( i, j, k \) for line numbers. Read the rule clause by clause.

1. **The assumption is the exact negation of the goal.** To prove \( \varphi \), the box opens with \( \neg\varphi \): the negation of the **whole** of \( \varphi \). If \( \varphi \) is \( Q \vee R \), the box opens with \( \neg(Q \vee R) \), not with \( \neg Q \vee R \).
2. **The box must reach \( \bot \)**, as a line of the box itself: a \( \bot \) inside a smaller box depends on a further assumption, as in \( \rulename{\neg I} \).
3. **The result is \( \varphi \) itself**, not \( \neg\neg\varphi \), which \( \rulename{\neg I} \) would give from the same box. This clause is the whole content of the rule.
4. **The box closes**, its assumption is discharged, and the justification cites the box as a range \( \lines{i}{j} \).

In words: the box is a thought experiment in which \( \varphi \) fails. If the experiment ends in \( \bot \), then \( \varphi \) cannot fail, and \( \rulename{RAA} \) lets us write \( \varphi \). Set the new rule beside \( \rulename{\neg I} \):

| Rule | The box opens with | The box ends with | After the box |
|---|---|---|---|
| \( \rulename{\neg I} \) | \( \varphi \) | \( \bot \) | \( \neg\varphi \) |
| \( \rulename{RAA} \) | \( \neg\varphi \) | \( \bot \) | \( \varphi \) |

The rows differ only in where the \( \neg \) sits, and that small difference makes \( \rulename{RAA} \) different in kind. Every other primitive rule is the introduction or the elimination rule of one connective (\( \rulename{\bot E} \) counts as the elimination rule of \( \bot \)), and repetition is a clause of @def-derivation, not a rule for a connective. \( \rulename{RAA} \) belongs to no connective. It applies to every statement \( \varphi \), whatever its main connective, and even to a letter, which has none.

For one kind of goal the new rule is never needed at the last step. Suppose the goal is itself a negation \( \neg\psi \). An \( \rulename{RAA} \) box for it opens with \( \neg\neg\psi \). Replace it by a \( \rulename{\neg I} \) box that opens with \( \psi \); inside it, derive \( \neg\neg\psi \) from \( \psi \) by the three lines of @exm-double-negation-introduction (a box on \( \neg\psi \) that clashes with \( \psi \)); then continue as the \( \rulename{RAA} \) box did, citing that line wherever the \( \rulename{RAA} \) box cited its assumption. The box still ends in \( \bot \), and \( \rulename{\neg I} \) closes it with \( \neg\psi \). So the **last** step of a derivation of a negation never needs \( \rulename{RAA} \), though steps inside its box still may. \( \rulename{RAA} \) earns its place on the other goals.

::: {.warning}
The assumption that opens an \( \rulename{RAA} \) box must be the **exact** negation of the goal. To prove \( x \le 1 \) by contradiction, assume \( x > 1 \), since for real numbers "not \( x \le 1 \)" says \( x > 1 \). Assuming \( x \ge 1 \) instead is a common slip. It is not the negation: \( x = 1 \) satisfies both \( x \le 1 \) and \( x \ge 1 \). A box opened with \( x \ge 1 \) cannot honestly reach \( \bot \) while \( x = 1 \) is possible, so a "contradiction" that seems to be reached hides an error.
:::

::: {.check}
A box opens with the assumption \( \neg(x < 0) \) and reaches \( \bot \), as a line of the box itself. Which of the following may be written after it closes, and by which rule? (i) \( x < 0 \); (ii) \( \neg\neg(x < 0) \); (iii) \( x \ge 0 \).
:::

::: {.solution}
(i) By \( \rulename{RAA} \): the box opened with the negation of \( x < 0 \). (ii) By \( \rulename{\neg I} \): \( \rulename{\neg I} \) writes the negation of the box's assumption, and the assumption is \( \neg(x < 0) \). (iii) By neither. For real numbers \( x \ge 0 \) says the same as \( \neg(x < 0) \), which is exactly the statement the box has refuted.
:::

## The move: when stuck, assume the negation of the goal

Chapter 1 and Sections 2.1–2.4 built two lists of moves. From the goal: its main connective chooses an introduction rule and so a box or two subgoals. From the premises: each available line's main connective chooses the elimination rule that uses it, and a goal \( \bot \) asks for a clash. The new rule adds one move, for the moment when both lists are used up.

We are **stuck** at a gap when the goal-directed moves give nothing (the goal is a letter, or a disjunction with neither side in hand) and no premise-directed move brings the goal closer. Then open an \( \rulename{RAA} \) box on the negation of the goal. The new goal is \( \bot \), so we hunt for a clash, and the box has given us one more line to clash with: \( \neg\varphi \) itself.

*When stuck, assume the negation of the goal, and hunt for a clash.*

The move is a last resort, not a first one. Section 2.6 explains why it never does harm and still comes last. Four of the five derivations below reach the moment of being stuck, and their Ideas say where; the first shows the rule at its smallest.

## Five derivations with the new rule

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

**Nonexample by minimal change.** Change only the last line of (a), from \( \neg\neg P \) to \( P \), keeping the justification \( \rulename{\neg I}\ \lines{2}{3} \). Lines 1–3 still check. What fails is the conclusion of \( \rulename{\neg I} \), which must be the negation of the box's assumption, here \( \neg\neg P \). To write \( P \), the justification must be \( \rulename{RAA} \).

From now on both parts are derived rules in the sense of @def-derived-rule. A line \( \neg\neg\varphi \) may be justified by "\( \rulename{\neg\neg I} \) \( i \)", citing a line \( \varphi \), and a line \( \varphi \) by "\( \rulename{\neg\neg E} \) \( i \)", citing a line \( \neg\neg\varphi \). The first stall of the list above is now one line: from \( \neg\neg(x > 0) \), \( \rulename{\neg\neg E} \) gives \( x > 0 \).

**Contraposition, backwards.** @prp-contrapositive derives \( \neg Q \to \neg P \) from \( P \to Q \) with the rules for \( \to \) and \( \neg \) alone. In practice we use it the other way round. To prove "if \( n^2 \) is even then \( n \) is even", one may prove "if \( n \) is not even then \( n^2 \) is not even", and the step from that back to the original goes from \( \neg Q \to \neg P \) to \( P \to Q \).

::: {#prp-contrapositive-converse}
[Converse of the Contrapositive]

For all statements \( P \) and \( Q \), \( \neg Q \to \neg P \vdash P \to Q \).
:::

::: {.idea}
The goal is an implication, so the goal-directed move opens a box with \( P \), and the new goal is \( Q \), a letter. The premise needs \( \neg Q \) before it gives anything, and \( \neg Q \) is nowhere; the box's assumption \( P \) is a letter and cannot be taken apart. We are stuck at \( Q \), so we assume its negation, \( \neg Q \). That is exactly what the premise wanted: \( \rulename{{\to}E} \) gives \( \neg P \), which clashes with the \( P \) of the outer box, and \( \rulename{RAA} \) closes the inner box with \( Q \).
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

So contraposition behaves like double negation: going from \( P \to Q \) to \( \neg Q \to \neg P \) needs no \( \rulename{RAA} \), and our derivation of the way back uses one \( \rulename{RAA} \). That no derivation of the way back can avoid it is true, but we state it without proof. When \( Q \) is itself a negation, the inner goal is a negation, and by the paragraph after @def-rule-raa that \( \rulename{RAA} \) can be replaced by \( \rulename{\neg I} \).

**Excluded middle.** Every integer is even or odd. Every real number is \( \ge 0 \) or \( < 0 \). The purely logical form of such facts is the law \( P \vee \neg P \), which the next result derives from no premises at all.

::: {#prp-excluded-middle}
[Excluded Middle]

For every statement \( P \), \( \vdash P \vee \neg P \).
:::

::: {.idea}
The goal is a disjunction, so Section 1.6's move postpones it: choose a side only when that side is in hand. But there are no premises, so no premise-directed move applies, and neither side can be derived on its own (informally: \( P \) may be true or false; Chapter 3 makes this exact). We are stuck, so we assume the negation of the whole goal, \( \neg(P \vee \neg P) \), which says that neither side holds, and hunt for a clash. The new line can clash only with \( P \vee \neg P \), which \( \rulename{\vee I} \) builds from either side. So we manufacture a side, as in @exm-manufactured-clash. If \( P \) held, then \( P \vee \neg P \) would hold, against the assumption; so \( \neg P \), by \( \rulename{\neg I} \). But then \( P \vee \neg P \) holds after all, and that is the final clash.
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

Its use is **proof by cases on a statement**. To derive \( \chi \), derive it once in a box that assumes \( \varphi \) and once in a box that assumes \( \neg\varphi \), and combine the two boxes with the line \( \varphi \vee \neg\varphi \) by \( \rulename{\vee E} \). The paragraph after De Morgan's laws below uses it that way, and so does part (b) of the result after them.

**A law with no negation.** The last of the five is a law in which \( \neg \) does not occur at all.

::: {#prp-peirce}
[Peirce's Law]

For all statements \( P \) and \( Q \), \( \vdash ((P \to Q) \to P) \to P \).
:::

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

The assumption \( \neg P \) of line 2 is used twice: at line 4 it makes the innermost box contradictory, and at line 8 it clashes with the \( P \) that line 7 obtained. Notice where the new box went: around the stalled box, not inside it. An assumption made one level out is available in every gap inside its box, and so it could give the stalled gap the line it lacked. Peirce's law contains no \( \neg \), yet our derivation uses \( \rulename{RAA} \): the classical rule is about more than negation. (That every derivation of it must use \( \rulename{RAA} \), or one of the two rules this section shows equivalent to it, is true, and Chapter 3 proves it in the remark after @thm-raa-independent, by the same reading with more than two truth values that settles \( \neg\neg P \vdash P \).)

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

Part (d) resists. Its goal is a disjunction, so the natural last line is \( \rulename{\vee I} \), from \( \neg P \) or from \( \neg Q \). But neither follows from the premise alone: with \( P \) true and \( Q \) false the premise is true and \( \neg P \) false; with \( P \) false and \( Q \) true the premise is true and \( \neg Q \) false; and the rules never lead from true premises to a false conclusion (Chapter 3 proves this). The premise itself can be used only by \( \rulename{\neg E} \), against \( P \wedge Q \), which we do not have. We are stuck at the whole goal, so we assume its negation, \( \neg(\neg P \vee \neg Q) \), which says that neither \( \neg P \) nor \( \neg Q \) holds. It should give \( P \) and \( Q \). Each is a letter, so each gets a small \( \rulename{RAA} \) box of its own, whose clash is manufactured by \( \rulename{\vee I} \). Together \( P \) and \( Q \) clash with the premise.
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

Excluded middle makes the decision instead. Split on \( P \vee \neg P \). In the case \( \neg P \), \( \rulename{\vee I} \) gives \( \neg P \vee \neg Q \) at once. In the case \( P \), a \( \rulename{\neg I} \) box on \( Q \) builds \( P \wedge Q \), which clashes with the premise, giving \( \neg Q \); then \( \rulename{\vee I} \) gives \( \neg P \vee \neg Q \). Written out, this route is 11 lines, with \( \rulename{LEM} \) as its one classical line. Both routes use a classical rule. That no derivation of (d) avoids one is true, but we state it without proof, and nothing in this book depends on it.

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

(b) The goal is a disjunction, so we postpone it. The premise is an implication, which gives \( Q \) only once we have \( P \), and we do not. So we are stuck, and this time excluded middle is the better tool than an \( \rulename{RAA} \) box: we decide \( P \) first. In the case \( P \) the premise gives \( Q \); in the case \( \neg P \) the left side is in hand.
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

So the classical part of our rules is **one** extra principle, whichever of its three forms we write down. Chapter 5 tells the story of the mathematicians who declined it, and shows what their mathematics looks like.

The base list matters. Part ③ uses \( \rulename{\bot E} \) at line \( k + 4 \), to close the impossible case as in @exm-impossible-case, and without \( \rulename{\bot E} \) among the base rules \( \rulename{LEM} \) no longer derives \( \rulename{\neg\neg E} \). We state this without proof; nothing depends on it.

::: {.remark}
Some books call exactly our \( \rulename{RAA} \) "proof by contradiction" or PBC, and some take \( \rulename{\neg\neg E} \) as their primitive rule and derive \( \rulename{RAA} \) from it. By @thm-classical-rules-interderivable nothing changes: all these choices prove the same sequents.
:::

::: {.remark}
\( \rulename{\bot E} \) could have been dropped from the primitive rules, since \( \rulename{RAA} \) and repetition derive it (Exercise B3 below asks for the derivation). We keep it so that the primitive rules other than \( \rulename{RAA} \) form a system of their own, the one Chapter 5 studies in its last section.
:::

## How reductio looks in a mathematical proof

Return to @exm-raa-zero, and read its solution one sentence at a time, with the rule of each step in brackets.

1. "Suppose, for a contradiction, that \( x \ne 0 \)." [An \( \rulename{RAA} \) box opens, with \( \neg(x = 0) \), the exact negation of the goal \( x = 0 \).]
2. "Since \( x \ge 0 \) and \( x \ne 0 \), we have \( x > 0 \)." [\( x \ge 0 \) means \( x = 0 \vee x > 0 \), and the box's assumption refutes the left side, so \( \rulename{DS} \) (@prp-disjunctive-syllogism) gives \( x > 0 \).]
3. "Then \( \varepsilon \coloneqq x/2 \) is a real number with \( \varepsilon > 0 \)." [School algebra.]
4. "So the hypothesis applies to it and gives \( x \le x/2 \)." [The hypothesis is about **every** \( \varepsilon > 0 \); applying it to one is a rule for "every", from Chapter 4.]
5. "… gives \( x/2 \le 0 \), and … \( x \le 0 \)." [School algebra.]
6. "This contradicts \( x > 0 \)." [\( \rulename{\neg E} \): for real numbers \( x > 0 \) is \( \neg(x \le 0) \), the negation of the line \( x \le 0 \).]
7. "Hence \( x = 0 \)." [\( \rulename{RAA} \) closes the box.]

The words "for a contradiction" do not by themselves tell \( \rulename{\neg I} \) from \( \rulename{RAA} \). Look at what is assumed and what is concluded. Here the box assumes a negation, \( x \ne 0 \), and the conclusion is the positive statement \( x = 0 \), so the step is \( \rulename{RAA} \). The proof of @thm-sqrt2-irrational assumes the positive statement \( r^2 = 2 \) and concludes its negation, so it is \( \rulename{\neg I} \). Chapter 11 opens its proof that the natural numbers are not bounded above by supposing, for contradiction, that they are bounded above, and concludes that they are not: that is \( \rulename{\neg I} \) too, despite the phrase.

::: {.warning}
An \( \rulename{RAA} \) box on \( \neg\varphi \) whose assumption is used **only at its last step**, against a \( \varphi \) derived without it, is legal, but it is a direct proof in disguise: the lines before the clash already derive \( \varphi \), so the box can be deleted. The degenerate derivation of \( P \vdash P \) above is the smallest case. Chapter 5 shows how to spot this costume in written proofs and take it off. (A box that reaches \( \bot \) without using its assumption at all is a different matter: the same lines, written before the box, derive \( \bot \) without it, and \( \rulename{\bot E} \) then gives the goal at once.)
:::

::: {.warning}
Not every "proof by contradiction" is \( \rulename{RAA} \). Calling the proof of @thm-sqrt2-irrational an \( \rulename{RAA} \) is a mislabeling: its box opens with \( r^2 = 2 \), not with a negation, and it concludes \( r^2 \ne 2 \), which \( \rulename{\neg I} \) writes. The difference matters when you count classical steps: the box of that proof closes by \( \rulename{\neg I} \) and contributes none.
:::

## What the rules sound like

Written mathematics carries these rules in a handful of phrases. The Lean column is for readers who use that proof assistant; nothing later depends on it, and the full dictionary is in Chapter 5.

| Rule | You write | Lean |
|---|---|---|
| \( \rulename{RAA} \) | "Suppose, for a contradiction, that \( \varphi \) fails. … This is impossible. Hence \( \varphi \)." | `by_contra h` |
| \( \rulename{\neg\neg E} \) | "It cannot be that \( \varphi \) fails; so \( \varphi \)." | `not_not.mp h` |
| \( \rulename{LEM} \) | "Either \( \varphi \) or not. If \( \varphi \), … If not, … In either case, …" | `by_cases h : P` |

## Exercises

### A. Check your understanding

::: {#exr-reductio-and-classical-rules-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. "Suppose \( 7 \) is even. Then \( 7 = 2k \) for some integer \( k \), so \( k = 7/2 \), which is not an integer. This is impossible. Hence \( 7 \) is not even." Is the last step \( \rulename{\neg I} \), \( \rulename{RAA} \), or neither? What did the box open with?
2. "Let \( x \) be real. Suppose \( x^2 \ge 2x - 1 \) fails, that is, \( x^2 < 2x - 1 \). Then \( (x - 1)^2 < 0 \), which is impossible. Hence \( x^2 \ge 2x - 1 \)." Same questions.
3. "Assume \( P \). Then, as shown above, \( Q \). Hence \( P \to Q \)." Same questions.
4. State \( \rulename{RAA} \) and \( \rulename{\neg I} \) side by side, and say which of the two the derivation of @prp-double-negation (a) uses.
5. In the derivation of @prp-de-morgan (d), why can the last line not be \( \rulename{\vee I} \) applied to a line derived from the premise alone?
6. In the same derivation, the assumption \( \neg(\neg P \vee \neg Q) \) on line 2 is cited twice. Name the two lines that cite it, and the rule each uses.
7. In the fragment for ② in the proof of @thm-classical-rules-interderivable, which rule justifies line \( k \), and why does the box of lines \( i \) to \( j \) need no change?
:::
:::

::: {.solution}
(a) \( \rulename{\neg I} \): the box opened with "\( 7 \) is even", and the conclusion is its negation. (\( 7/2 \) is not an integer because \( 3 < 7/2 < 4 \).)

(b) \( \rulename{RAA} \): the box opened with the negation of \( x^2 \ge 2x - 1 \), and the conclusion is \( x^2 \ge 2x - 1 \) itself. (The clash: \( x^2 < 2x - 1 \) rearranges to \( (x - 1)^2 < 0 \), and squares are nonnegative.)

(c) Neither: this is \( \rulename{{\to}I} \). The box opened with \( P \) and ended with \( Q \); no \( \bot \) appears.

(d) \( \rulename{\neg I} \): a box that opens with \( \varphi \) and reaches \( \bot \) gives \( \neg\varphi \). \( \rulename{RAA} \): a box that opens with \( \neg\varphi \) and reaches \( \bot \) gives \( \varphi \). The derivation of @prp-double-negation (a) uses \( \rulename{\neg I} \), with \( \neg P \) as the assumption, so its conclusion is the negation of \( \neg P \), namely \( \neg\neg P \).

(e) \( \rulename{\vee I} \) would need \( \neg P \) or \( \neg Q \) on a line derived from the premise alone. Neither can be: with \( P \) true and \( Q \) false the premise is true and \( \neg P \) false, with \( P \) false and \( Q \) true the premise is true and \( \neg Q \) false, and the rules never lead from true premises to a false conclusion (proved in Chapter 3, @thm-soundness).

(f) Line 5 cites it, by \( \rulename{\neg E} \) against line 4, \( \neg P \vee \neg Q \); and line 9 cites it, by \( \rulename{\neg E} \) against line 8, the same statement. Both lines lie in boxes inside the box of line 2, which is still open, so the citations are legal.

(g) \( \rulename{\neg I} \): the box opens with \( \neg\varphi \) and ends with \( \bot \), so \( \rulename{\neg I} \) gives the negation of its assumption, \( \neg\neg\varphi \). The box needs no change because \( \rulename{\neg I} \), like \( \rulename{RAA} \), asks only for a box that ends with \( \bot \) as a line of the box itself; the two rules differ in what they write after the box, not in the box.
:::

### B. Practice

::: {#exr-reductio-and-classical-rules-b1}
[B1: With and without the new rule]

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
[B2: Back from negated sides]

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
[B4: Part ② on an example]

Here is a proof by \( \rulename{RAA} \) about a real number \( x \).

> Suppose \( x^2 \le x \). Suppose, for a contradiction, that \( x \le 1 \) fails, that is, \( x > 1 \). Then \( x > 0 \), and multiplying \( x > 1 \) by \( x \) gives \( x^2 > x \), which contradicts \( x^2 \le x \). Hence \( x \le 1 \).

Let \( P \) be the statement "\( x \le 1 \)".

::: {.enumerate options="label=(\alph*)"}
1. Which sentences of the argument form the \( \rulename{RAA} \) box, and what are its assumption and its last line?
2. Apply part ② of the proof of @thm-classical-rules-interderivable to this use of \( \rulename{RAA} \). Write the statement that the new line \( k \) asserts, in symbols and in words.
3. Which rule justifies the new line \( k \), and which rule the line after it?
4. Which lines of the original argument are unchanged by the replacement?
:::
:::

::: {.solution}
(a) The box opens with "\( x \le 1 \) fails", that is \( \neg P \), and runs through the sentence ending "which contradicts \( x^2 \le x \)"; its last line is \( \bot \), the clash between \( x^2 > x \) and the hypothesis \( x^2 \le x \). The last sentence, "Hence \( x \le 1 \)", is the \( \rulename{RAA} \) step.

(b) The new line \( k \) is \( \neg\neg P \), that is \( \neg\neg(x \le 1) \): "it is not the case that \( x \le 1 \) fails". The line after it is \( P \), "\( x \le 1 \)".

(c) Line \( k \) is \( \rulename{\neg I} \), closing the box that opened with \( \neg P \); the next line is \( \rulename{\neg\neg E} \), citing line \( k \).

(d) Every line of the box is unchanged: the assumption \( \neg P \) ("\( x \le 1 \) fails", that is \( x > 1 \)), the steps \( x > 0 \) and \( x^2 > x \), and the clash. Only the closing step becomes two lines. For real numbers "not not \( x \le 1 \)" and "\( x \le 1 \)" mean the same, but for the rules they are different statements, joined by \( \rulename{\neg\neg E} \).
:::

### C. Going deeper

::: {#exr-reductio-and-classical-rules-c1}
[C1: Excluded middle does the work of reductio directly]

Suppose that, instead of \( \rulename{RAA} \), we had \( \rulename{LEM} \) as a rule: \( \varphi \vee \neg\varphi \) may be written on any line, for any statement \( \varphi \).

::: {.enumerate options="label=(\alph*)"}
1. Given a box that opens with \( \neg\varphi \) and reaches \( \bot \), derive \( \varphi \) using \( \rulename{LEM} \), \( \rulename{\vee E} \), \( \rulename{\bot E} \), and the other primitive rules, but neither \( \rulename{RAA} \) nor \( \rulename{\neg\neg E} \). Write the case \( \neg\varphi \) as the given box, extended.
2. Which two parts of the proof of @thm-classical-rules-interderivable does your fragment shortcut, and which lines of their composite does it save?
:::
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
(a) Write excluded middle for \( \varphi \) just before the given box, and use the box as the second case of \( \rulename{\vee E} \), extended by one line:

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {h} {\varphi \vee \neg \varphi} \lem{}
  \open
  \hypo {h+1} {\varphi}
  \close
  \open
  \hypo {i} {\neg \varphi}
  \have {} {\vdots}
  \have {j} {\bot}
  \have {j+1} {\varphi} \be{j}
  \close
  \have {k} {\varphi} \oe{h,h+1-h+1,i-j+1}
\end{nd}$
\end{center}
```

Here \( i = h + 2 \). The first case is a one-line box that already ends with the goal. The second case is the given box with one more line, \( \rulename{\bot E} \) on its \( \bot \); its lines are unchanged and cite what they cited before, since the box has not moved into or out of any other box. No \( \rulename{RAA} \) and no \( \rulename{\neg\neg E} \) is used.

(b) It shortcuts ② followed by ③. Part ② closes the box by \( \rulename{\neg I} \), giving \( \neg\neg\varphi \), then applies \( \rulename{\neg\neg E} \); part ③ replaces that \( \rulename{\neg\neg E} \) by a split on \( \varphi \vee \neg\varphi \) whose \( \neg\varphi \) case is a new box that clashes with the line \( \neg\neg\varphi \). The fragment in (a) uses the given box itself as the \( \neg\varphi \) case, so it never writes \( \neg\neg\varphi \). Counted exactly, it saves three lines: the line \( \neg\neg\varphi \) of ②, and in ③ the assumption \( \neg\varphi \) at line \( k + 2 \) and the \( \rulename{\neg E} \) line \( k + 3 \). The \( \rulename{\bot E} \) line \( k + 4 \) of ③ survives, moved to the end of the given box.
:::

::: {#exr-reductio-and-classical-rules-c2}
[C2: Find the error]

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
3. Show that the illegal step, if it were allowed, would prove too much: use the same move to "derive" \( P \vee Q \vdash P \), and say why that sequent must not be derivable.
4. Give a correct derivation.
:::
:::

::: {.solution}
(a) Yes: part (d) below gives a derivation. The conclusion is true, and the argument is still wrong.

(b) No. Line 6 fails: it cites line 3, the assumption of the first case box, lines 3–4, which closed before line 5. By the scope rule of @def-derivation, line 3 is not available at line 6. The form of \( \rulename{\neg E} \) is right; what is broken is availability. In words, the student used the assumption of one case inside the other case, where it has not been assumed.

(c) The same move derives \( P \vee Q \vdash P \): split on the premise by \( \rulename{\vee E} \), with a first box that opens with \( P \) and ends there, and a second box that opens with \( Q \) and "repeats" \( P \) from the first. That sequent must not be derivable: with \( P \) false and \( Q \) true the premise is true and the conclusion false, and Chapter 3 proves that no derivation leads from true premises to a false conclusion (@thm-soundness). So citing a line of a sibling box is illegal in general, not just unlucky here.

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
*The search.* The goal is a disjunction, so we postpone it; there are no premises, so no premise-directed move applies; and neither side is derivable on its own (\( P \) may be false, and \( P \to Q \) is false when \( P \) is true and \( Q \) false). We are stuck, so we assume the exact negation of the goal, \( \neg(P \vee (P \to Q)) \), and hunt for a clash. The assumption can clash only with \( P \vee (P \to Q) \), which \( \rulename{\vee I} \) builds from either side. The side \( P \to Q \) is an implication, so we open a box on \( P \) with the goal \( Q \). Inside it, \( \rulename{\vee I} \) gives \( P \vee (P \to Q) \) from \( P \), which clashes with the assumption, and \( \rulename{\bot E} \) writes \( Q \). So \( P \to Q \) holds, \( \rulename{\vee I} \) gives the goal, and that is the second clash.

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

<!-- dependency ledger
exm-raa-zero (example): x >= 0 and x != 0 give x > 0; x/2 > 0 for x > 0; subtracting x/2 and multiplying by 2 preserve <= | school algebra, ch11 (promised)
exm-raa-zero (example): the hypothesis "x <= eps for every eps > 0" applies to eps = x/2 | ch04 (promised; rules for "every"), flagged in prose; the example illustrates the shape of RAA and nothing cites it
def-rule-raa (claim): no derivation of P from not-not-P uses only the rules of ch01 and s01-s04 | ch03 (promised; thm-raa-independent, optional there), flagged in prose; the motivation for RAA, nothing proved from it
def-rule-raa (claim): the other two stalls (exr-derived-rules-c1 (b), the converse of exm-iff-negations) cannot be completed without RAA | stated without proof and marked so; nothing depends on it
def-rule-raa (claim): the last step of a derivation of a negation never needs RAA (replace the RAA box on not-not-psi by a not-I box on psi) | inline (argued in the paragraph, using exm-double-negation-introduction)
prp-contrapositive-converse (claim): no derivation of the converse avoids RAA | stated without proof and marked so; nothing depends on it
prp-excluded-middle (idea): neither P nor not-P is derivable from no premises | informal, flagged "Chapter 3 makes this exact"; motivation only
prp-peirce (claim): every derivation of Peirce's law uses RAA or one of its equivalents | ch03 (promised; the remark after thm-raa-independent, optional there: value 1/2 at p = 1/2, q = 0), prose pointer; nothing depends on it
prp-de-morgan (idea): no derivation reaches not-P (or not-Q) from not(P and Q) alone, because a row makes the premise true and the disjunct false | ch03 (promised; thm-soundness), flagged as proved there; motivation only, the proof does not use it
prp-de-morgan (claim): the LEM route to (d) is 11 lines; no derivation of (d) avoids a classical rule | the route is described inline; the necessity is stated without proof and marked so; nothing depends on it
thm-classical-rules-interderivable (proof): replacing a line by a fragment keeps every citation available and the premises and last line unchanged | inline (argued in the proof)
thm-classical-rules-interderivable (claim): without bot-E in the base list, LEM no longer derives not-not-E | stated without proof and marked so; nothing depends on it
exm-raa-zero (example): in the rule-by-rule reading, x >= 0 read as (x = 0 or x > 0), and x > 0 read as not(x <= 0) | school algebra (trichotomy), ch11 (promised)
exr-reductio-and-classical-rules-a1 (solution): squares are non-negative; 3 < 7/2 < 4; x^2 < 2x - 1 iff (x - 1)^2 < 0 | school algebra, ch11 (promised)
exr-reductio-and-classical-rules-a1 (solution): the rules never lead from true premises to a false conclusion | ch03 (promised; thm-soundness), flagged in the solution as proved there
exr-reductio-and-classical-rules-b4 (solution): x > 1 gives x > 0 and x^2 > x | school algebra, ch11 (promised)
exr-reductio-and-classical-rules-c2 (solution): P or Q |- P is not derivable (the row P false, Q true) | ch03 (promised; thm-soundness), flagged in the solution; the find-the-error verdict does not depend on it
exr-reductio-and-classical-rules-c3 (solution): neither P nor P -> Q is derivable on its own (the search's motivation) | informal (a row each), motivation only; the derivation does not depend on it
-->
