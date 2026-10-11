# Using an Implication: Modus Ponens

Section 1.3 gave the two rules for "and". This section gives one rule for "implies": the rule that **uses** an implication already in hand. Proving an implication needs a new device, an assumption with a boundary, and that is the subject of Section 1.5. Using one needs nothing new, and it is what a proof does every time it applies a theorem. The rule is short; the work of the section is to see exactly what it allows and what it does not, and to find chains of implications both forwards and backwards.

## Four cards

Before the rule, a puzzle about what "if … then" says.

::: {#exm-wason-selection}
[Four cards]

Each of four cards has a whole number on one side and a color on the other. They lie on a table showing
\[
6, \qquad 7, \qquad \text{red}, \qquad \text{green} .
\]
Someone claims: *if a card shows an even number on one side, then its other side is red.* Which cards must be turned over to find out whether the claim is true of these four cards? Decide before reading the solution.
:::

::: {.solution}
The claim is an implication about each card: if its number is even, its color is red. Take the cards one at a time and ask whether the hidden side could show that the claim is false. The claim is false for a card exactly when that card has an even number and is not red.

*The card showing \( 6 \).* Its number is even, so the hypothesis of the implication holds, and the claim says its other side is red. If that side is green, the claim is false. This card must be turned.

*The card showing \( 7 \).* Its number is odd, so the hypothesis fails, and the claim says nothing about this card. Whatever its color, the card cannot contradict the claim. Leave it.

*The red card.* Its color is the **conclusion** of the implication. If its number is even, the card fits the claim; if its number is odd, the card still fits, since the claim says only what even cards look like and nothing about which cards are red. No hidden number can contradict the claim. Leave it.

*The green card.* If its number is even, it is an even card that is not red, and the claim is false. This card must be turned.

So the answer is the \( 6 \) and the green card. Many people, asked this, choose the \( 6 \) and the **red** card. The \( 6 \) is right. The red card is the tell: choosing it means reading the claim as if it also said "if a card is red, then its number is even", which is the **converse**. An implication and its converse are different claims, and the claim here is only the first.
:::

The two cards that matter are the two ways an implication meets a case. The \( 6 \) shows the **hypothesis**, and an implication together with its hypothesis gives its conclusion: that is the rule of this section. The red card shows the **conclusion**, and an implication together with its conclusion gives nothing: that is the most important thing the rule does *not* allow. The green card shows that the conclusion fails; saying exactly what follows from that needs the rules for "not", and Section 2.3 returns to this card with the rule behind it, called modus tollens.

## The rule

*An implication fires on its hypothesis, and gives its conclusion.*

::: {#def-rule-implication-elimination}
[Implication Elimination]

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {i} {\varphi \to \psi}
  \have {j} {\varphi}
  \have {k} {\psi} \ie{i,j}
\end{nd}$
\end{center}
```

This rule is called \( \rulename{{\to}E} \) (**implication-elimination**, or **modus ponens**).
:::

Read the schema clause by clause, as we read those of @def-rules-conjunction.

**Two given lines.** One line is an implication \( \varphi \to \psi \), the other is \( \varphi \). Both must stand earlier in the derivation; they may be anywhere above line \( k \), in either order.

**Reading the implication.** To see a line as \( \varphi \to \psi \), its **main connective** (@def-main-connective) must be \( \to \). Then \( \varphi \), the **hypothesis**, is everything that this \( \to \) joins on its left, and \( \psi \), the **conclusion**, is everything on its right. In \( (P \wedge Q) \to R \), the hypothesis is \( P \wedge Q \) and the conclusion is \( R \). In \( P \to (Q \to R) \), the hypothesis is \( P \) and the conclusion is \( Q \to R \), itself an implication.

**The hypothesis must match exactly.** Line \( j \) must be the statement \( \varphi \), symbol for symbol: the letter \( \varphi \) occurs in both given lines, and a use of the rule replaces it by the same statement in both (@def-rule-schema). A part of \( \varphi \) will not do, and neither will a statement that "says the same thing". From \( (P \wedge Q) \to R \) and \( Q \wedge P \), the rule gives nothing, although \( Q \wedge P \) and \( P \wedge Q \) are each derivable from the other (@prp-and-commutes); the hypothesis must first be rebuilt, in the right order, by \( \rulename{\wedge E} \) and \( \rulename{\wedge I} \).

**The new line is the conclusion, and only the conclusion.** The rule writes \( \psi \), the whole of what stands right of the main \( \to \). If \( \psi \) is \( Q \wedge R \), the rule writes \( Q \wedge R \), and getting \( Q \) takes one more line, by \( \rulename{\wedge E} \).

**The citation.** We cite the implication first and the hypothesis second: "\( \rulename{{\to}E} \) \( i, j \)", as in the schema. Unlike the citation of \( \rulename{\wedge I} \), the order here cannot change the new line, since only \( \psi \) can come out; the fixed order just makes every \( \rulename{{\to}E} \) line read the same way.

**A degenerate case.** The statements \( \varphi \) and \( \psi \) may be the same. From \( P \to P \) and \( P \), the rule writes \( P \), which was already there. The line is legal and useless.

*Why this rule.* It is what "by Theorem so-and-so" means. A theorem of school algebra says: if \( a < b \) and \( b < c \), then \( a < c \). Take its instance with \( a = \sqrt{2} \), \( b = 1.5 \), and \( c = 2 \) (passing from "for all \( a, b, c \)" to one instance is a rule of its own, which Chapter 4 states; here we take the instance as given):
\[
\bigl( (\sqrt{2} < 1.5) \wedge (1.5 < 2) \bigr) \to \sqrt{2} < 2 .
\]
We know \( \sqrt{2} < 1.5 \), because \( 1.5^2 = 2.25 > 2 \), and we know \( 1.5 < 2 \). Then \( \rulename{\wedge I} \) builds the hypothesis \( (\sqrt{2} < 1.5) \wedge (1.5 < 2) \), and \( \rulename{{\to}E} \) gives \( \sqrt{2} < 2 \). Every application of a theorem has this shape: check the theorem's hypotheses, assemble them into exactly the theorem's hypothesis, and fire.

*Why it is safe.* If \( \varphi \to \psi \) is true and \( \varphi \) is true, then \( \psi \) is true; that is what "if \( \varphi \), then \( \psi \)" asserts. Chapter 3 proves this for the rule as part of the soundness theorem (@thm-soundness).

*Why nothing more.* From \( \varphi \to \psi \) alone, \( \rulename{{\to}E} \) cannot fire: an implication by itself asserts neither its hypothesis nor its conclusion. And \( \rulename{{\to}E} \) does not run backwards: from \( \varphi \to \psi \) together with its conclusion \( \psi \), it gives nothing about \( \varphi \). That pattern,
\[
\varphi \to \psi, \ \psi \ \text{ therefore } \ \varphi ,
\]
is called **affirming the consequent**, and it is the red card of the puzzle. It is not an instance of \( \rulename{{\to}E} \), because the second given line of \( \rulename{{\to}E} \) must be the hypothesis \( \varphi \), and here it is the conclusion \( \psi \). It can lead from true premises to a false conclusion: the Quick check on the form of an argument in Section 1.1 took "if \( n \) is divisible by \( 4 \), then \( n \) is even" and "\( n \) is even" at \( n = 2 \), both true, where "\( n \) is divisible by \( 4 \)" is false. It is also the step that would repair Argument B of Section 1.1. Chapter 3 proves more: no derivation of \( P \to Q, \ Q \vdash P \) exists at all, whichever rules of Chapters 1 and 2 it uses (@cor-refuting-row).

::: {.warning}
Affirming the consequent looks like modus ponens and is not. Let \( x \) be a real number. "If \( x > 2 \), then \( x^2 > 4 \)" is true for every \( x \), and at \( x = -3 \) we have \( x^2 = 9 > 4 \); but \( x > 2 \) is false there. From an implication and its **conclusion**, nothing follows about the hypothesis.
:::

::: {.check}
Line 1 is \( P \to (Q \to R) \). What does \( \rulename{{\to}E} \) give from line 1 and a line \( Q \)? And from line 1 and a line \( P \)?
:::

::: {.solution}
From line 1 and \( Q \): nothing. The main connective of line 1 is the first \( \to \), so its hypothesis is \( P \), and \( Q \) does not match it. From line 1 and \( P \): the conclusion \( Q \to R \). A second application, to \( Q \to R \) and the line \( Q \), would then give \( R \).
:::

::: {.remark}
At this point an implication can be **used** but not **proved**. A derivation can write an implication only by taking it out of a line that already contains it: \( \rulename{\wedge E} \) applied to \( (P \to Q) \wedge R \), or \( \rulename{{\to}E} \) applied to \( P \to (Q \to R) \) and \( P \). No rule so far builds a new \( \to \). Section 1.5 gives the rule that does.
:::

## Chains of implications

With \( \rulename{{\to}E} \), a derivation can pass along a chain: from \( P \) and \( P \to Q \) to \( Q \), from \( Q \) and \( Q \to R \) to \( R \), and so on. Such a chain can be found from either end.

*Forwards, from the premises.* An available implication (for now, one on an earlier line) whose hypothesis is also available can **fire**: \( \rulename{{\to}E} \) writes its conclusion, which becomes available in turn and may be the hypothesis of another implication. Keep firing until the goal appears. This is premise-directed reasoning, as in Section 1.3: the premise's main connective, \( \to \), picks the elimination rule that uses it.

*Backwards, from the goal.* Suppose the goal is \( \psi \). Look among the available lines for an implication whose **conclusion** is \( \psi \), say \( \varphi \to \psi \). If there is one, it is enough to reach \( \varphi \): then \( \rulename{{\to}E} \) writes \( \psi \). So \( \varphi \) becomes the new goal, and we repeat. This is goal-directed reasoning, but of a new kind. In Section 1.3 the goal's main connective chose an introduction rule. Here the goal may be a letter, with no main connective at all, and it still directs the search: it tells us which implication to look for.

The two directions meet in the middle, when a line reached forwards is a goal reached backwards. In written mathematics the backward step has a standard phrase, "to show \( \psi \), it suffices to show \( \varphi \)", and Chapter 5 collects it with the other phrases that stand for rules.

::: {.check}
The premises are \( P \), \( P \to R \), \( Q \to S \), and \( R \to S \), and the goal is \( S \). Search backwards: which implications could give the goal, and which of them leads to a derivation?
:::

::: {.solution}
Two premises have conclusion \( S \): \( Q \to S \) and \( R \to S \). The first makes \( Q \) the new goal, and no line is \( Q \) or has conclusion \( Q \), so that branch is a dead end. The second makes \( R \) the new goal; \( P \to R \) has conclusion \( R \), and its hypothesis \( P \) is a premise. So the derivation is \( R \) by \( \rulename{{\to}E} \) from \( P \to R \) and \( P \), then \( S \) by \( \rulename{{\to}E} \) from \( R \to S \) and \( R \). A backward search may branch, and a branch that stalls is abandoned for the next one.
:::

::: {#exm-implication-chains}
[Chains of implications]

Give a derivation of each sequent.

::: {.enumerate options="label=(\alph*)"}
1. \( P \to Q, \ P \vdash Q \).
2. \( P, \ P \to Q, \ Q \to R \vdash R \).
3. \( P \wedge Q, \ P \to (Q \to R) \vdash R \).
4. \( (P \wedge Q) \to R, \ P, \ Q \vdash R \).
5. \( (P \to Q) \wedge (R \to S), \ P \wedge R \vdash Q \wedge S \).
:::
:::

::: {.solution}
(a) *Idea.* There is nothing to choose: the premises are an implication and its hypothesis, and the rule fires once.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {P}
  \have {3} {Q} \ie{1,2}
\end{nd}$
\end{center}
```

This is the sequent that Section 1.1 said \( \rulename{{\to}E} \) makes true, and now it is shown: a derivation with these premises and this last line exists.

(b) *Idea, forwards.* The premise \( P \to Q \) has its hypothesis \( P \) available, so it fires and gives \( Q \). Now \( Q \to R \) has its hypothesis available, so it fires and gives \( R \), the goal.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \hypo {2} {P \to Q}
  \hypo {3} {Q \to R}
  \have {4} {Q} \ie{2,1}
  \have {5} {R} \ie{3,4}
\end{nd}$
\end{center}
```

*Idea, backwards.* The same derivation can be found from the other end. The goal \( R \) is a letter. Which available implication has conclusion \( R \)? Only \( Q \to R \), so it suffices to reach \( Q \) (left picture: the goal at the bottom, its new subgoal \( Q \) above it). Which implication has conclusion \( Q \)? Only \( P \to Q \), so it suffices to reach \( P \); and \( P \) is a premise, so the gap closes (right picture).

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \hypo {2} {P \to Q}
  \hypo {3} {Q \to R}
  \have[\ ][0] {} {\vdots}
  \have[][4] {4} {Q}
  \have {5} {R} \ie{3,4}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {P}
  \hypo {2} {P \to Q}
  \hypo {3} {Q \to R}
  \have {4} {Q} \ie{2,1}
  \have {5} {R} \ie{3,4}
\end{nd}$
\end{center}
```

Both searches write the same five lines. The forward search wrote each line as soon as it could; the backward one wrote the last line first and worked up. In a derivation this small they cost the same. Exercise B3 has a case where they do not.

(c) *Idea.* The goal \( R \) is a letter. From the goal: the only line that mentions \( R \) is \( P \to (Q \to R) \), but its conclusion is \( Q \to R \), not \( R \); the \( R \) sits one implication deeper. From the premises: \( P \wedge Q \) is a conjunction, so take it apart by \( \rulename{\wedge E} \), giving \( P \) and \( Q \). Now \( P \) is exactly the hypothesis of \( P \to (Q \to R) \), whose main connective is the first \( \to \), so it fires and gives \( Q \to R \). This new line is an implication whose hypothesis \( Q \) is available, so it fires too.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge Q}
  \hypo {2} {P \to (Q \to R)}
  \have {3} {P} \ae{1}
  \have {4} {Q} \ae{1}
  \have {5} {Q \to R} \ie{2,3}
  \have {6} {R} \ie{5,4}
\end{nd}$
\end{center}
```

Line 6 is the first line in this chapter where \( \rulename{{\to}E} \) fires on an implication that was itself **written by** \( \rulename{{\to}E} \), not given as a premise. A line is a line, however it was obtained.

(d) *Idea.* This time the goal leads. The goal \( R \) is the conclusion of \( (P \wedge Q) \to R \), so it suffices to reach its hypothesis \( P \wedge Q \). That subgoal is a conjunction, so, goal-directed as in Section 1.3, it comes from \( \rulename{\wedge I} \) with subgoals \( P \) and \( Q \), and both are premises.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge Q) \to R}
  \hypo {2} {P}
  \hypo {3} {Q}
  \have {4} {P \wedge Q} \ai{2,3}
  \have {5} {R} \ie{1,4}
\end{nd}$
\end{center}
```

Compare (c). There the implication took its two hypotheses one at a time, \( P \to (Q \to R) \), and the conjunction was a premise to be taken apart. Here the implication takes both hypotheses at once, \( (P \wedge Q) \to R \), and the conjunction is a subgoal to be built. The content is the same; the brackets decide which rules the derivation uses. (Section 1.5 shows that each of the two implications is derivable from the other.)

(e) *Idea.* Both ends at once. From the goal: \( Q \wedge S \) is a conjunction, so its last line is \( \rulename{\wedge I} \), with subgoals \( Q \) and \( S \). From the premises: both are conjunctions, so \( \rulename{\wedge E} \) takes each apart, giving \( P \to Q \), \( R \to S \), \( P \), and \( R \). The two ends meet through \( \rulename{{\to}E} \): \( P \to Q \) fires on \( P \) and gives the subgoal \( Q \), and \( R \to S \) fires on \( R \) and gives the subgoal \( S \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \to Q) \wedge (R \to S)}
  \hypo {2} {P \wedge R}
  \have {3} {P \to Q} \ae{1}
  \have {4} {R \to S} \ae{1}
  \have {5} {P} \ae{2}
  \have {6} {R} \ae{2}
  \have {7} {Q} \ie{3,5}
  \have {8} {S} \ie{4,6}
  \have {9} {Q \wedge S} \ai{7,8}
\end{nd}$
\end{center}
```

Lines 3–6 came from the premises, line 9 from the goal, and lines 7–8 are where the two searches met.
:::

Each derivation in the example is a box-free derivation (@def-box-free-derivation) with \( \rulename{\wedge I} \), \( \rulename{\wedge E} \), and \( \rulename{{\to}E} \) as its rules, so by @def-derivable each shows its sequent. In each, the Idea chose a rule for a reason that can be stated: the goal's main connective, an available line's main connective, or an available implication whose conclusion is the goal.

## Checking a line of modus ponens

Finding a chain can take some searching; checking one never does. For a line justified "\( \rulename{{\to}E} \) \( i, j \)", the questions of Section 1.2 (which rule? is it an instance? are the cited lines earlier?) become four small ones:

1. Are lines \( i \) and \( j \) earlier than this line?
2. Is the main connective of line \( i \) a \( \to \)? If so, read off \( \varphi \) (its left side) and \( \psi \) (its right side).
3. Is line \( j \) exactly \( \varphi \), symbol for symbol?
4. Is this line exactly \( \psi \)?

Here is the check run on the lines of (c) above that use \( \rulename{{\to}E} \), and on a tempting wrong line, "\( R \) — \( \rulename{{\to}E} \) 2, 4", that a hurried reader might write instead of lines 5 and 6.

| Line | Cites | \( \varphi \), \( \psi \) read off line \( i \) | Line \( j \) is \( \varphi \)? | Line is \( \psi \)? |
|---|---|---|---|---|
| 5: \( Q \to R \) | 2, 3 | \( P \), \( Q \to R \) | yes (\( P \)) | yes |
| 6: \( R \) | 5, 4 | \( Q \), \( R \) | yes (\( Q \)) | yes |
| wrong: \( R \) | 2, 4 | \( P \), \( Q \to R \) | no (\( Q \) is not \( P \)) | no (\( R \) is not \( Q \to R \)) |

The wrong line fails twice: it feeds line 2 the wrong hypothesis and takes out a part of the conclusion. Both failures come from reading \( P \to (Q \to R) \) as though its hypothesis were \( Q \) and its conclusion \( R \). The main connective settles it: the first \( \to \) is the one applied last, so everything after it, \( Q \to R \), is the conclusion.

## How this looks in a mathematical proof

Let \( x \) be a real number with \( x > 2 \). Suppose we know two facts of school algebra:

- if \( x > 2 \), then \( x^2 > 4 \) (since \( x > 2 > 0 \), multiplying \( x > 2 \) by \( x \) gives \( x^2 > 2x \), and \( 2x > 4 \));
- if \( x^2 > 4 \), then \( x^2 + 1 > 5 \) (add \( 1 \) to both sides).

A written proof that \( x^2 + 1 > 5 \) takes one sentence: *Since \( x > 2 \), we have \( x^2 > 4 \), and so \( x^2 + 1 > 5 \).* As a derivation, with the two facts and the hypothesis as premises, it reads as follows.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(x > 2) \to (x^2 > 4)}
  \hypo {2} {(x^2 > 4) \to (x^2 + 1 > 5)}
  \hypo {3} {x > 2}
  \have {4} {x^2 > 4} \ie{1,3}
  \have {5} {x^2 + 1 > 5} \ie{2,4}
\end{nd}$
\end{center}
```

Each piece of the sentence is one line.

| Line | Sentence |
|---|---|
| 3 | "Since \( x > 2 \), …" (the hypothesis) |
| 4 | "… we have \( x^2 > 4 \), …" (\( \rulename{{\to}E} \), firing the first fact) |
| 5 | "… and so \( x^2 + 1 > 5 \)." (\( \rulename{{\to}E} \), firing the second fact) |

The sentence never mentions lines 1 and 2. That is normal: when an implication is a known theorem or a fact of school algebra, writers leave it unstated and write only "since … we get …". Each "since \( \varphi \), \( \psi \)" in a proof is one application of \( \rulename{{\to}E} \) to an implication that the reader is trusted to supply. When a proof is hard to follow, writing the unstated implications down is often how one finds a gap: either the implication is false, or its hypothesis was never established.

## Common errors

The warning above was about the wrong given line: the conclusion in place of the hypothesis. The other common error is a hypothesis that is only partly there.

::: {.warning}
\( \rulename{{\to}E} \) needs the **whole** hypothesis. From \( (P \wedge Q) \to R \) and \( P \) alone, it gives nothing. This is the commonest slip in analysis: "\( f \) is continuous, so by the theorem \( f \) attains a maximum". The theorem meant (proved in Part I) has a second hypothesis, that \( f \) is defined on a closed bounded interval, and without it the conclusion fails: \( f(x) = x \) on the open interval \( (0, 1) \) is continuous and has no largest value, since \( \frac{a + 1}{2} \) is a larger value than \( a \) for every \( a \) in \( (0, 1) \).
:::

A near relative is a hypothesis in the wrong order, as in the clause-by-clause reading: \( Q \wedge P \) is not the hypothesis of \( (P \wedge Q) \to R \). The repair is two \( \rulename{\wedge E} \) lines and one \( \rulename{\wedge I} \) line, and Exercise B1 asks for it.

## What the rules sound like

The table of Section 1.3 grows by one row.

| Rule | You write | Lean |
|------|--------------------------------------|------------------------|
| \( \rulename{\wedge I} \) | "We show \( P \), and we show \( Q \)." | `constructor` |
| \( \rulename{\wedge E} \) | "In particular, \( P \)." | `h.1` (and `h.2`) |
| \( \rulename{{\to}E} \) | "Since \( P \) implies \( Q \), and \( P \) holds, \( Q \)." | `exact h hp` |

In the Lean column, `h` is the implication and `hp` the proof of its hypothesis; `h hp` applies the one to the other, which is modus ponens.

## Exercises

### A. Check your understanding

::: {#exr-using-an-implication-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Write the schema of \( \rulename{{\to}E} \) from memory.
2. Lines 1 and 2 of a derivation are \( P \to (Q \wedge R) \) and \( P \). Which of the following can line 3 be, by one application of \( \rulename{{\to}E} \)? \( Q \wedge R \); \( Q \); \( R \wedge Q \); \( P \to Q \).
3. In @exm-wason-selection, why is the red card not worth turning?
4. True or false, with a reason: from lines \( P \to Q \) and \( Q \to R \), \( \rulename{{\to}E} \) gives \( P \to R \).
:::
:::

::: {.solution}
(a) Given lines \( i \): \( \varphi \to \psi \) and \( j \): \( \varphi \); new line \( k \): \( \psi \), justified "\( \rulename{{\to}E} \) \( i, j \)" (@def-rule-implication-elimination).

(b) Only \( Q \wedge R \), the conclusion of line 1. The line \( Q \) needs a further \( \rulename{\wedge E} \), and \( R \wedge Q \) two further \( \rulename{\wedge E} \) lines and a \( \rulename{\wedge I} \) line. The line \( P \to Q \) is not the conclusion of line 1, so \( \rulename{{\to}E} \) cannot write it.

(c) The claim is "even \( \to \) red", and the red card shows the conclusion. An odd number behind it would not contradict the claim, which says nothing about which cards are red; an even number would fit it. Inferring anything about its number from its color would be affirming the consequent.

(d) False. \( \rulename{{\to}E} \) needs an implication and a line that is its hypothesis. The hypothesis of \( Q \to R \) is \( Q \), and \( P \to Q \) is not \( Q \); the hypothesis of \( P \to Q \) is \( P \), which is not a line. So \( \rulename{{\to}E} \) does not apply at all. (The sequent \( P \to Q, \ Q \to R \vdash P \to R \) does hold, but its derivation needs the rule of Section 1.5.)
:::

### B. Practice

::: {#exr-using-an-implication-b1}
[B1: Two chains]

Give a derivation of each sequent. For each, say which step you found first, and whether it came from the goal or from a premise.

::: {.enumerate options="label=(\alph*)"}
1. \( P, \ P \to Q, \ Q \to (R \wedge S) \vdash S \wedge Q \).
2. \( (P \wedge Q) \to R, \ Q \wedge P \vdash R \).
:::
:::

::: {.solution}
(a) The first step found was from the goal: \( S \wedge Q \) is a conjunction, so the last line is \( \rulename{\wedge I} \) with subgoals \( S \) and \( Q \). Then from the premises: \( P \to Q \) fires on \( P \) and gives \( Q \), and \( Q \to (R \wedge S) \) fires on \( Q \) and gives \( R \wedge S \), which \( \rulename{\wedge E} \) takes apart.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \hypo {2} {P \to Q}
  \hypo {3} {Q \to (R \wedge S)}
  \have {4} {Q} \ie{2,1}
  \have {5} {R \wedge S} \ie{3,4}
  \have {6} {S} \ae{5}
  \have {7} {S \wedge Q} \ai{6,4}
\end{nd}$
\end{center}
```

Line 4 is cited twice, by line 5 and by line 7.

(b) The first step found was from the goal: \( R \) is the conclusion of line 1, so it suffices to reach \( P \wedge Q \) exactly. The premise \( Q \wedge P \) is not it. So take the premise apart and rebuild in the right order.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge Q) \to R}
  \hypo {2} {Q \wedge P}
  \have {3} {Q} \ae{2}
  \have {4} {P} \ae{2}
  \have {5} {P \wedge Q} \ai{4,3}
  \have {6} {R} \ie{1,5}
\end{nd}$
\end{center}
```
:::

::: {#exr-using-an-implication-b2}
[B2: Two facts and a number]

Let \( x \) be a real number. Take as premises the two facts "if \( 0 < x < 1 \), then \( x^2 < x \)" and "if \( x^2 < x \), then \( x^3 < x^2 \)", and the hypothesis \( 0 < x < 1 \). Derive \( x^3 < x^2 \), naming the rule on each line. Then write the argument as one or two sentences of prose.
:::

::: {.solution}
The hypothesis \( 0 < x < 1 \) is the conjunction \( (0 < x) \wedge (x < 1) \), which is exactly the hypothesis of the first fact, so the first fact fires on it at once.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {((0 < x) \wedge (x < 1)) \to (x^2 < x)}
  \hypo {2} {(x^2 < x) \to (x^3 < x^2)}
  \hypo {3} {(0 < x) \wedge (x < 1)}
  \have {4} {x^2 < x} \ie{1,3}
  \have {5} {x^3 < x^2} \ie{2,4}
\end{nd}$
\end{center}
```

In prose: *Since \( 0 < x < 1 \), we have \( x^2 < x \), and therefore \( x^3 < x^2 \).* Both facts are true for every real \( x \): if \( 0 < x < 1 \), multiplying \( x < 1 \) by \( x > 0 \) gives \( x^2 < x \); and if \( x^2 < x \), then \( x(x - 1) < 0 \), so \( x > 0 \), and multiplying \( x^2 < x \) by \( x \) gives \( x^3 < x^2 \).
:::

::: {#exr-using-an-implication-b3}
[B3: Which premises are needed?]

Find a derivation of
\[
P, \ P \to Q, \ P \to R, \ R \to S, \ S \to U, \ Q \to T \ \vdash \ T ,
\]
and list the premises it uses. Explain why a backward search finds the needed premises faster than a forward one here.
:::

::: {.solution}
Search backwards. The goal \( T \) is the conclusion of \( Q \to T \) only, so it suffices to reach \( Q \). The goal \( Q \) is the conclusion of \( P \to Q \) only, so it suffices to reach \( P \), a premise.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \hypo {2} {P \to Q}
  \hypo {3} {P \to R}
  \hypo {4} {R \to S}
  \hypo {5} {S \to U}
  \hypo {6} {Q \to T}
  \have {7} {Q} \ie{2,1}
  \have {8} {T} \ie{6,7}
\end{nd}$
\end{center}
```

It uses premises 1, 2, and 6. The others are never cited, which is allowed: a derivation need not use every premise (@def-derivable). Deleting lines 3–5 and renumbering gives a derivation of \( P, \ P \to Q, \ Q \to T \vdash T \).

A forward search fires every implication whose hypothesis is available, relevant or not: from \( P \) it writes \( Q \) and \( R \), then \( S \) from \( R \), then \( U \) from \( S \), and \( T \) from \( Q \) — five new lines, three of them useless. The backward search looks only at implications whose conclusion is the current goal, and at each stage exactly one qualifies, so it writes only the two lines the derivation needs.
:::

### C. Going deeper

::: {#exr-using-an-implication-c1}
[C1: Find the error]

Here is an argument, followed by the derivation its author offers for it.

> If \( 10 \) is divisible by \( 6 \), then \( 10 \) is even. And \( 10 \) is even. So \( 10 \) is divisible by \( 6 \).

With \( D \): "\( 10 \) is divisible by \( 6 \)" and \( E \): "\( 10 \) is even":

```{=latex}
\begin{center}
% expect-invalid: a deliberately flawed derivation (affirming the consequent)
$\begin{nd}
  \hypo {1} {D \to E}
  \hypo {2} {E}
  \have {3} {D} \ie{1,2}
\end{nd}$
\end{center}
```

::: {.enumerate options="label=(\alph*)"}
1. Name the line that fails, and say why it is not an instance of the schema of \( \rulename{{\to}E} \).
2. Show that the step can lead from true premises to a false conclusion.
3. What new statement about divisibility can be correctly derived from the two premises with the rules so far?
:::
:::

::: {.solution}
(a) Line 3. The schema needs, besides the implication \( \varphi \to \psi \), a line that is its hypothesis \( \varphi \). Matching line 1 gives \( \varphi \coloneqq D \) and \( \psi \coloneqq E \), so the second cited line would have to be \( D \); line 2 is \( E \), which is \( \psi \). The line affirms the consequent.

(b) This instance already does. The first premise is true, because every multiple of \( 6 \) is even (\( 6k = 2(3k) \)); the second is true, since \( 10 = 2 \cdot 5 \); and the conclusion is false, since \( 10 = 6 \cdot 1 + 4 \) leaves remainder \( 4 \) on division by \( 6 \). So the step at line 3 leads from two true premises to a false line, and no safe rule can allow it.

(c) None. \( \rulename{{\to}E} \) cannot fire, since no line is the hypothesis \( D \); \( \rulename{\wedge E} \) has no conjunction to take apart; and \( \rulename{\wedge I} \) only joins the premises into conjunctions such as \( (D \to E) \wedge E \), which say nothing the premises did not. The premises tell us nothing about whether \( 10 \) is divisible by \( 6 \), which is why the conclusion had to be smuggled in.
:::

::: {#exr-using-an-implication-c2}
[C2: Both ends]

Consider the sequent
\[
P \to (Q \to R), \ S \to P, \ S \wedge Q \ \vdash \ R \wedge S .
\]

::: {.enumerate options="label=(\alph*)"}
1. Describe a search for a derivation in words, in three parts: what the goal asks for; what the premises give; where the two meet.
2. Write the derivation, naming the rule on every line.
:::
:::

::: {.solution}
[Hint 1]

Two premises have main connective \( \to \) and one has \( \wedge \); the goal has \( \wedge \). Write down what each main connective lets you do.
:::

::: {.solution}
[Hint 2]

The goal splits into \( R \) and \( S \). Which available implication could end in \( R \), and after how many firings?
:::

::: {.solution}
(a) *From the goal:* \( R \wedge S \) is a conjunction, so the last line is \( \rulename{\wedge I} \) with subgoals \( R \) and \( S \). The only line mentioning \( R \) is \( P \to (Q \to R) \), whose conclusion is \( Q \to R \); so \( R \) needs \( Q \to R \) and \( Q \), and \( Q \to R \) needs \( P \). *From the premises:* \( S \wedge Q \) splits by \( \rulename{\wedge E} \) into \( S \) and \( Q \); then \( S \to P \) fires on \( S \) and gives \( P \). *Where they meet:* \( S \) is at once a subgoal and a piece of the premise; \( P \), reached forwards, is the hypothesis the backward search asked for; and \( Q \), from \( \rulename{\wedge E} \), is the last hypothesis \( R \) needs.

(b) The derivation, with the rule on every line:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \to R)}
  \hypo {2} {S \to P}
  \hypo {3} {S \wedge Q}
  \have {4} {S} \ae{3}
  \have {5} {Q} \ae{3}
  \have {6} {P} \ie{2,4}
  \have {7} {Q \to R} \ie{1,6}
  \have {8} {R} \ie{7,5}
  \have {9} {R \wedge S} \ai{8,4}
\end{nd}$
\end{center}
```

Line 4 is cited twice, by line 6 and by line 9.

**Marking scheme.** (10 points)

- 2: from the goal, splits \( R \wedge S \) into the subgoals \( R \) and \( S \) for a final \( \rulename{\wedge I} \).
- 2: takes \( S \wedge Q \) apart by \( \rulename{\wedge E} \).
- 3: fires \( S \to P \), then \( P \to (Q \to R) \), then \( Q \to R \), each \( \rulename{{\to}E} \) citing an implication and exactly its hypothesis.
- 2: the final \( \rulename{\wedge I} \), with the citation order giving \( R \wedge S \).
- 1: the three-part description names where the searches meet.

Any other correct derivation earns the same points step for step (its lines may come in another order, as long as each cites only earlier lines). Fatal errors (0 for the step): \( \rulename{{\to}E} \) on \( P \to (Q \to R) \) with \( Q \) (the wrong hypothesis); affirming the consequent anywhere.
:::

<!-- dependency ledger
exm-wason-selection (solution): a card falsifies "even -> red" exactly when its number is even and its color is not red; odd/even and red/green are exhaustive for the hidden side | reading of the claim, stated in the solution; checked by verify/ch01/exm-wason-selection.py
def-rule-implication-elimination (example): if a < b and b < c then a < c; sqrt(2) < 1.5 since 1.5^2 = 2.25 > 2; 1.5 < 2 | school algebra -> ch11 (promised); passing to the instance is forall-E, ch04 (named in prose, taken as given); checked by verify/ch01/def-rule-implication-elimination.py
def-rule-implication-elimination (example): the n = 2 witness recalled from Section 1.1's Quick check (divisible by 4 implies even; 2 even, not divisible by 4) | Section 1.1 (def-sequent's Quick check), recalled in prose
def-rule-implication-elimination (example): warning witness x = -3 (x > 2 implies x^2 > 4 for every real x; 9 > 4; -3 > 2 false) | school algebra -> ch11 (promised); checked by verify/ch01/def-rule-implication-elimination.py
def-rule-implication-elimination (example): x > 2 implies x^2 > 4; x^2 > 4 implies x^2 + 1 > 5 (the "How this looks" example) | school algebra -> ch11 (promised), argued inline; checked by verify/ch01/def-rule-implication-elimination.py
def-rule-implication-elimination (example): f(x) = x on (0, 1) is continuous and has no maximum ((a + 1)/2 > a in (0, 1)); the extreme value theorem's hypotheses | continuity: Part I (promised, named in prose only, not used in any argument); (a + 1)/2 argued inline
exr-using-an-implication-b2 (solution): 0 < x < 1 implies x^2 < x; x^2 < x implies x^3 < x^2 (for every real x) | school algebra -> ch11 (promised), argued inline; checked by verify/ch01/exr-using-an-implication-b2.py
exr-using-an-implication-c1 (solution): every multiple of 6 is even; 10 = 2 * 5; 10 = 6 * 1 + 4 is not divisible by 6 | inline arithmetic; checked by verify/ch01/exr-using-an-implication-c1.py
-->
