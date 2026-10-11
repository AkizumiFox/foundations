# Contradiction: Using a Negation

Chapter 1 gave rules for "and", "implies", and "or", and not one of them mentions "not". Yet written proofs are full of sentences such as "this is impossible", "this case cannot occur", and "which contradicts what we assumed". This section gives the two rules that **use** a negation: the first says exactly what a clash between two lines is, and the second says what a clash buys. The rule that **proves** a negation is the subject of the next section.

## A case that cannot occur

Here is Argument A of Section 1.1, told as a proof by cases. Let \( n \) be an integer whose square is even. Every integer is even or odd, so there are two cases. If \( n \) is even, we are done. If \( n \) is odd, then \( n^2 \) is odd; but \( n^2 \) is even, and no integer is both, so this case cannot occur. Hence \( n \) is even.

Chapter 1 has a rule for a proof by cases: \( \rulename{\vee E} \) of @def-rules-disjunction. It asks for a disjunction and two boxes, one opened by each disjunct, and **both boxes must end on the same line**, the goal. In the argument above the goal is "\( n \) is even". The first box reaches it at once. The second box does not reach it at all. It reaches "impossible", and then simply declares itself finished.

Two things are missing, and no rule of Chapter 1 supplies them.

- A way to **record** the impossibility: the lines "\( n^2 \) is even" and "\( n^2 \) is odd", together with "no integer is both", should produce a line that says "contradiction".
- A way to **close** the impossible box with the goal: from the line "contradiction", the box should be allowed to write "\( n \) is even", so that both boxes end on the same line and \( \rulename{\vee E} \) applies.

Section 1.1 introduced the symbols for both. The connective \( \neg \) forms the **negation** \( \neg\varphi \), read "not \( \varphi \)". The constant \( \bot \), read "contradiction", is a statement that is false however things stand. There they were symbols only. The two rules below give them their first uses.

## The rules for a clash

The rule for recording a clash has a simple content. The statement \( \neg\varphi \) says that \( \varphi \) fails, so a derivation that has both \( \varphi \) and \( \neg\varphi \) available is working in a situation that cannot occur. The rule writes this down as the line \( \bot \). A second rule then says what such a line is good for.

*A statement and its negation clash; from a clash, anything follows.*

::: {#def-rules-contradiction}
[Rules for Contradiction]

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {i} {\varphi}
  \have {j} {\neg \varphi}
  \have {k} {\bot} \ne{i,j}
\end{nd}$
\qquad
$\begin{nd}[schema]
  \have {i} {\bot}
  \have {k} {\varphi} \be{i}
\end{nd}$
\end{center}
```

The left schema is \( \rulename{\neg E} \) (**not-elimination**): if \( \varphi \) and \( \neg\varphi \) stand on lines \( i \) and \( j \) available at line \( k \), write \( \bot \), citing both, the unnegated line first. The right schema is \( \rulename{\bot E} \) (**contradiction-elimination**, or *ex falso*): if \( \bot \) stands on a line \( i \) available at line \( k \), write **any** statement \( \varphi \), citing line \( i \).
:::

As with every rule of Chapter 1, the letters \( \varphi \) and \( i, j, k \) follow @def-rule-schema: \( \varphi \) stands for one statement, the same one wherever it occurs in the schema, and \( i, j, k \) for line numbers. Let us read the two schemas clause by clause.

**\( \rulename{\neg E} \), the given lines.** There are two, and they must be **exactly** \( \varphi \) and \( \neg\varphi \): the second is the first with one \( \neg \) written in front of the whole of it, symbol for symbol. It is not enough that the second line "contradicts the first in spirit". The lines \( x < 1 \) and \( x > 1 \) cannot both hold, but neither is the negation of the other as written, so they are not an instance of the schema. (The warning below shows how to turn them into one.)

**\( \rulename{\neg E} \), availability.** Both lines must be available at line \( k \), in the sense of the scope rule of @def-derivation: each is earlier than \( k \), and not inside a box that has already closed. They may stand in either order on the page. The citation fixes their roles: "\( \rulename{\neg E} \) \( i, j \)" says that line \( i \) is \( \varphi \) and line \( j \) is \( \neg\varphi \).

**\( \rulename{\neg E} \), the new line.** It is \( \bot \) and nothing else. The rule does not write the goal, or \( \neg\varphi \) again, or anything else; it records the clash and stops. What to do with the clash is the business of the second rule. Splitting the work this way keeps each rule to one step, and it lets the next section aim at the line \( \bot \) as a goal in its own right.

**\( \rulename{\bot E} \), the given line.** One line, \( \bot \), available at line \( k \).

**\( \rulename{\bot E} \), the new line.** **Any** statement at all, chosen by the writer. Like the second disjunct in \( \rulename{\vee I} \) (@def-rule-disjunction-introduction), the statement \( \varphi \) occurs in no given line: it need not be related to anything above, and it may itself be a negation, or \( \bot \) again.

Two more observations complete the reading. First, \( \rulename{\bot E} \) is the **elimination** rule of \( \bot \): it says how a line \( \bot \) is used. There is no introduction rule of its own for \( \bot \). Other rules can pass a \( \bot \) along (\( \rulename{\bot E} \) may write it again, and \( \rulename{{\to}E} \) writes it from \( \varphi \to \bot \) and \( \varphi \)), but each of them needs \( \bot \) already written in a line it uses. Apart from being assumed, the only way a line \( \bot \) first appears is by \( \rulename{\neg E} \): it is the one rule whose new line is always \( \bot \), from lines in which \( \bot \) need not occur. So \( \rulename{\neg E} \) plays two parts at once: it is the way a negation is used, and it is the way \( \bot \) is produced.

Second, why is \( \rulename{\bot E} \) honest? A rule should never lead from lines that hold to a line that fails. A line \( \bot \) can stand only in a part of a derivation where the premises and the open assumptions cannot all hold together, at least when the \( \bot \) was written by \( \rulename{\neg E} \), from some \( \varphi \) and \( \neg\varphi \) that were both available there; that the rules which only pass a \( \bot \) along keep this property is part of what Chapter 3 checks in proving @thm-soundness. In such a place there is no situation in which the conclusion of \( \rulename{\bot E} \) would have to be checked, so it cannot be caught failing. Chapter 3's soundness theorem turns this remark into a proof.

::: {.check}
Which of these pairs of lines are, as written, an instance of the given lines of \( \rulename{\neg E} \), and in which order must each be cited? The pairs are (i) \( Q \wedge R \) and \( \neg(Q \wedge R) \); (ii) \( \neg P \) and \( \neg\neg P \); (iii) \( P \to Q \) and \( \neg P \to Q \).
:::

::: {.solution}
(i) Yes, with \( \varphi = Q \wedge R \); cite the line \( Q \wedge R \) first. (ii) Yes, with \( \varphi = \neg P \): the second line is \( \neg(\neg P) \). Cite \( \neg P \) first, then \( \neg\neg P \). (iii) No. The main connective of \( \neg P \to Q \) is \( \to \) (@def-main-connective), so it is not a negation at all; the \( \neg \) applies to \( P \) alone. The negation of \( P \to Q \) would be \( \neg(P \to Q) \).
:::

**Clashes in school mathematics.** In derivations about numbers, the clash usually comes from a school fact written as a negation. For real numbers \( a \) and \( b \), exactly one of \( a < b \) and \( a \ge b \) holds, so \( a \ge b \) says the same as \( \neg(a < b) \), and we use them interchangeably. So a line \( x^2 < 0 \) and the school fact \( x^2 \ge 0 \), written as \( \neg(x^2 < 0) \), give \( \bot \) by \( \rulename{\neg E} \). The symbol \( a \ne b \) **means** \( \neg(a = b) \), by definition. And the fact "no integer is both even and odd" is a negation of a conjunction, \( \neg(E \wedge O) \) with \( E \) for "\( n \) is even" and \( O \) for "\( n \) is odd". It clashes only with a line \( E \wedge O \), which \( \rulename{\wedge I} \) builds from separate lines \( E \) and \( O \).

::: {.warning}
A clash must have the exact shape \( \varphi \), \( \neg\varphi \). The lines \( x < 1 \) and \( x > 1 \) are not yet a clash. To make them one, write \( x > 1 \) as \( \neg(x \le 1) \) (for real numbers, \( x > 1 \) holds exactly when \( x \le 1 \) fails), and get \( x \le 1 \) from \( x < 1 \) by \( \rulename{\vee I} \), since \( x \le 1 \) means \( (x < 1) \vee (x = 1) \). And some pairs that look opposed do not clash at all: \( x \ge 1 \) and \( x \le 1 \) both hold at \( x = 1 \).
:::

::: {.warning}
\( \rulename{\bot E} \) does not run backwards. From \( \bot \) we may write \( \varphi \), or \( \neg\varphi \), or anything; but from \( \varphi \) alone no rule writes \( \bot \). If it could, the true line \( x = 1 \) would give \( \bot \), and then \( \rulename{\bot E} \) would give the false line \( x = 2 \).
:::

## First derivations with a clash

The five derivations below grow in difficulty. Each Idea says why each rule was chosen, in the two directions Chapter 1 used: from the goal (what does the goal's main connective ask for?) and from the premises (what does an available line's main connective let us do?). This section adds one question to each list. From the goal: *when nothing produces the goal, can a clash produce it?* From the premises: *an available negation \( \neg\varphi \) is used in exactly one way, by \( \rulename{\neg E} \), so it asks for \( \varphi \).*

::: {#exm-first-contradictions}
[The first clashes]

Show that (a) \( \bot \vdash P \), and (b) \( P \wedge Q, \ \neg Q \vdash R \).
:::

::: {.idea}
(a) is the rule \( \rulename{\bot E} \) itself, the degenerate case with no clash to find. In (b), the first premise is a conjunction, so the premise-directed move takes it apart by \( \rulename{\wedge E} \). Its half \( Q \) and the premise \( \neg Q \) are exactly a pair \( \varphi \), \( \neg\varphi \). The goal \( R \) has nothing to do with the premises: no rule builds it from them. Only \( \rulename{\bot E} \) can write it, and \( \rulename{\bot E} \) needs a line \( \bot \), which the clash supplies.
:::

::: {.solution}
(a) Two lines: the premise, and one application of \( \rulename{\bot E} \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\bot}
  \have {2} {P} \be{1}
\end{nd}$
\end{center}
```

(b) Five lines.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge Q}
  \hypo {2} {\neg Q}
  \have {3} {Q} \ae{1}
  \have {4} {\bot} \ne{3,2}
  \have {5} {R} \be{4}
\end{nd}$
\end{center}
```

Line 4 cites line 3 first because line 3 plays \( \varphi \) and line 2 plays \( \neg\varphi \), with \( \varphi = Q \). The half \( P \) of the first premise is never used; a derivation need not use every premise (@def-derivable).
:::

The next result is the pattern of (b) with nothing extra around it. We state it as a proposition, because later sections cite it.

::: {#prp-ex-falso}
[Contradictory Premises Prove Anything]

\( P, \ \neg P \vdash Q \).
:::

::: {.idea}
The premises are a clash as they stand, so \( \rulename{\neg E} \) writes \( \bot \) at once, and \( \rulename{\bot E} \) writes the goal, which nothing else could produce.
:::

::: {.proof}
The derivation

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \hypo {2} {\neg P}
  \have {3} {\bot} \ne{1,2}
  \have {4} {Q} \be{3}
\end{nd}$
\end{center}
```

has premises \( P \) and \( \neg P \) and last line \( Q \). This proves the proposition.
:::

In the next derivation the clash happens inside a box, and the rule \( \rulename{\bot E} \) writes the box's goal.

::: {#prp-vacuous-implication}
[Vacuous Implication]

\( \neg P \vdash P \to Q \).
:::

::: {.idea}
The goal is an implication, so the goal-directed move of Chapter 1 (\( \rulename{{\to}I} \), @def-rules-implication) opens a box with its hypothesis \( P \); the new goal is \( Q \). Nothing available mentions \( Q \), so no rule can build it. But inside the box, the assumption \( P \) and the premise \( \neg P \) clash, and \( \rulename{\bot E} \) writes the box's goal \( Q \). This is the section's goal-directed move: *when nothing produces the goal, look for a clash.*
:::

::: {.proof}
The derivation

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P}
  \open
  \hypo {2} {P}
  \have {3} {\bot} \ne{2,1}
  \have {4} {Q} \be{3}
  \close
  \have {5} {P \to Q} \ii{2-4}
\end{nd}$
\end{center}
```

has premise \( \neg P \) and last line \( P \to Q \). Line 3 may cite line 1, which lies in no box. This proves the proposition.
:::

Line 4 is the line that makes the box close properly: \( \rulename{{\to}I} \) needs the box to end on \( Q \), as a line of that box itself, and \( \rulename{\bot E} \) put it there.

In the next example no clash is lying about. It has to be made.

::: {#exm-manufactured-clash}
[Manufacturing the other half of a clash]

Show that \( \neg(P \vee Q) \vdash P \to R \).
:::

::: {.idea}
As before, the goal \( P \to R \) opens a box on \( P \), and the new goal \( R \) occurs nowhere else, so a clash must write it. Inside the box there is no \( \neg P \) to clash with. The only negation available is the premise \( \neg(P \vee Q) \), and the premise-directed question says what it asks for: the line \( P \vee Q \). That line is one \( \rulename{\vee I} \) away from the assumption \( P \). So the clash is **manufactured**: the unnegated half of the premise becomes a subgoal, and \( \rulename{\vee I} \) is chosen not because the goal is a disjunction but because the premise's clash needs one.
:::

::: {.solution}
Six lines.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \vee Q)}
  \open
  \hypo {2} {P}
  \have {3} {P \vee Q} \oi{2}
  \have {4} {\bot} \ne{3,1}
  \have {5} {R} \be{4}
  \close
  \have {6} {P \to R} \ii{2-5}
\end{nd}$
\end{center}
```

Line 4 cites line 3 as \( \varphi \) and line 1 as \( \neg\varphi \), with \( \varphi = P \vee Q \). In words: if neither \( P \) nor \( Q \) holds, then \( P \) cannot hold, so an implication with hypothesis \( P \) is true whatever its conclusion. The mirror image, with \( Q \) as the hypothesis, is exercise B1.
:::

The last derivation of this section is the pattern of the opening argument: a case split in which one case is impossible.

::: {#exm-impossible-case}
[An impossible case]

Show that \( P \vee Q, \ P \to R, \ \neg R \vdash Q \).
:::

::: {.idea}
The goal \( Q \) is a letter, so the goal gives no introduction rule to aim at. The premises do: \( P \vee Q \) is a disjunction, and Chapter 1's premise-directed move for a disjunction is \( \rulename{\vee E} \), with two boxes that both end in the current goal \( Q \). The box of \( Q \) ends as soon as it opens: its assumption is already the goal. The box of \( P \) cannot reach \( Q \) honestly, because nothing in it produces \( Q \). So we look for a clash: \( P \) feeds the premise \( P \to R \), and \( R \) clashes with \( \neg R \). The box ends on \( Q \) by \( \rulename{\bot E} \). This is the second new move: *an impossible case closes itself.*
:::

::: {.solution}
Nine lines.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \hypo {2} {P \to R}
  \hypo {3} {\neg R}
  \open
  \hypo {4} {P}
  \have {5} {R} \ie{2,4}
  \have {6} {\bot} \ne{5,3}
  \have {7} {Q} \be{6}
  \close
  \open
  \hypo {8} {Q}
  \close
  \have {9} {Q} \oe{1,4-7,8-8}
\end{nd}$
\end{center}
```

The second box consists of its assumption alone, a one-line box, just as in the derivation of \( P \vee P \vdash P \) in @exm-disjunction-first-derivations: its last line is its first line, and that line is \( Q \), which is what \( \rulename{\vee E} \) needs. The two boxes are separate, so line 7 could not cite line 8, and nothing in the second box could cite lines 4–7.
:::

Look at line 7 of this derivation again. The box of \( P \) is a case "that cannot occur", and line 7 is the sentence "so there is nothing to prove": the case is closed with whatever the other case reaches. Every proof by cases with an impossible case has this line somewhere, usually unwritten.

::: {.warning}
The impossible case must be impossible **from what is available in its own box**. A clash with a line of a sibling box, or of a box that has already closed, is a scope error (@def-derivation), even when the clash "looks right". In @exm-impossible-case the clash in the box of \( P \) uses line 5, from that box, and the premise on line 3; neither lives in another box. Exercise C2 shows the error and what it can prove.
:::

The moves of this section, in one place. **Goal \( \bot \): find a clash.** Look for \( \varphi \) and \( \neg\varphi \) among the available lines; if only \( \neg\varphi \) is there, make \( \varphi \) a subgoal. **An impossible case closes itself.** In a case split, a case that reaches \( \bot \) ends by \( \rulename{\bot E} \) on the current goal. The next section adds a way to reach the goal \( \bot \) deliberately, by assuming something.

## How the rules look in a mathematical proof

We can now prove the fact of Argument A in Section 1.1, with every rule named. Three school facts about integers enter as premises. An integer \( n \) is **even** if \( n = 2k \) for some integer \( k \), and **odd** if \( n = 2k + 1 \) for some integer \( k \). And:

::: {.enumerate options="label=(E\arabic*)"}
1. every integer is even or odd;
2. no integer is both even and odd;
3. the square of an odd integer is odd.
:::

The third is a computation. If \( n = 2k + 1 \) for an integer \( k \), then

\[
n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1 ,
\]

and \( 2k^2 + 2k \) is an integer, so \( n^2 \) is odd. Taking "an integer \( k \) with \( n = 2k + 1 \)" and working with it is a step about "there exists"; the rules for such steps come in Chapter 4, and here we use the step as school algebra.

::: {#thm-square-even-implies-even}
[Even Square, Even Number]

Let \( n \) be an integer. If \( n^2 \) is even, then \( n \) is even.
:::

::: {.idea}
The hypothesis "\( n^2 \) is even" hands us nothing to compute with: it says \( n^2 = 2j \) for some integer \( j \), and no algebra turns that into a statement about \( n \). The word "odd" does hand us something, since \( n = 2k + 1 \) can be squared. So we split on (E1) and show that the odd case is impossible: there (E3) makes \( n^2 \) odd, which clashes with the hypothesis through (E2). The impossible case then closes itself.
:::

::: {.proof}
Suppose \( n^2 \) is even \( [\text{assumption for } \rulename{{\to}I}] \). By (E1), \( n \) is even or \( n \) is odd, and we argue by cases \( [\rulename{\vee E}] \).

*Case \( n \) even.* This is the goal.

*Case \( n \) odd.* By (E3), \( n^2 \) is odd \( [\rulename{{\to}E}] \). So \( n^2 \) is both even and odd \( [\rulename{\wedge I}] \); this contradicts (E2) \( [\rulename{\neg E}] \). So this case cannot occur, and in it \( n \) is even \( [\rulename{\bot E}] \).

In both cases \( n \) is even \( [\rulename{\vee E}] \). This proves that if \( n^2 \) is even, then \( n \) is even \( [\rulename{{\to}I}] \).
:::

The logic of the proof fits in a derivation. Write \( E \) for "\( n \) is even", \( O \) for "\( n \) is odd", \( S \) for "\( n^2 \) is even", and \( T \) for "\( n^2 \) is odd". Then (E1) for \( n \) is \( E \vee O \), (E2) for \( n^2 \) is \( \neg(S \wedge T) \), and (E3) for \( n \) is \( O \to T \); these are the premises.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {E \vee O}
  \hypo {2} {\neg (S \wedge T)}
  \hypo {3} {O \to T}
  \open
  \hypo {4} {S}
  \open
  \hypo {5} {E}
  \close
  \open
  \hypo {6} {O}
  \have {7} {T} \ie{3,6}
  \have {8} {S \wedge T} \ai{4,7}
  \have {9} {\bot} \ne{8,2}
  \have {10} {E} \be{9}
  \close
  \have {11} {E} \oe{1,5-5,6-10}
  \close
  \have {12} {S \to E} \ii{4-11}
\end{nd}$
\end{center}
```

Each line is one sentence of the proof.

| Line | Sentence of the proof |
|---|---|
| 1–3 | (E1) for \( n \), (E2) for \( n^2 \), (E3) for \( n \) |
| 4 | Suppose \( n^2 \) is even. |
| 5 | Case \( n \) even. (A one-line box: it is the goal.) |
| 6 | Case \( n \) odd. |
| 7 | By (E3), \( n^2 \) is odd. |
| 8 | So \( n^2 \) is both even and odd, |
| 9 | which contradicts (E2). |
| 10 | So this case cannot occur, and in it \( n \) is even. |
| 11 | In both cases \( n \) is even. |
| 12 | This proves that if \( n^2 \) is even, then \( n \) is even. |

Line 8 cites line 4, the assumption of the outer box; it may, since the box \( \lines{4}{11} \) contains line 8 (@def-derivation). Two steps of the proof are not in the derivation: passing from the facts (E1)–(E3), which are about every integer, to their instances for this \( n \) and this \( n^2 \); and naming the \( k \) of (E3). Both are quantifier steps, and Chapter 4 gives their rules.

::: {.check}
Which sentence of the proof of @thm-square-even-implies-even is the rule \( \rulename{\bot E} \), and what does it write?
:::

::: {.solution}
The sentence "So this case cannot occur, and in it \( n \) is even", line 10 of the derivation. It cites the line \( \bot \) (line 9) and writes \( E \), "\( n \) is even", which is the goal of the case, so that the box of \( O \) ends on the same line as the box of \( E \).
:::

Every rule in this proof is a primitive rule: \( \rulename{{\to}I} \), \( \rulename{\vee E} \), \( \rulename{{\to}E} \), \( \rulename{\wedge I} \), \( \rulename{\neg E} \), and \( \rulename{\bot E} \). The next section uses the theorem twice, to prove that no rational number has square \( 2 \). Section 2.3 reads the same proof again with shorter steps, as mathematicians usually write it, "by the contrapositive".

## Vacuous truth

We can now settle the question that makes many readers distrust logic. Is the sentence

> if \( x^2 < 0 \), then \( x = 7 \)

true, for a real number \( x \)? The hypothesis never holds, and the conclusion has nothing to do with it. Everyday intuition is unsure what to say. The rules are not unsure.

::: {#exm-vacuous-square}
[An implication with an impossible hypothesis]

Let \( x \) be a real number. Show that if \( x^2 < 0 \), then \( x = 7 \).
:::

::: {.idea}
The goal is an implication, so open a box with \( x^2 < 0 \), aiming at \( x = 7 \). Nothing produces \( x = 7 \), so look for a clash: the school fact \( x^2 \ge 0 \) is \( \neg(x^2 < 0) \), which clashes with the assumption. This is exactly the derivation of @prp-vacuous-implication, with \( P \) read as "\( x^2 < 0 \)" and \( Q \) as "\( x = 7 \)".
:::

::: {.solution}
With the school fact as the premise:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (x^2 < 0)}
  \open
  \hypo {2} {x^2 < 0}
  \have {3} {\bot} \ne{2,1}
  \have {4} {x = 7} \be{3}
  \close
  \have {5} {x^2 < 0 \to x = 7} \ii{2-4}
\end{nd}$
\end{center}
```

In prose: *suppose \( x^2 < 0 \); this contradicts \( x^2 \ge 0 \); so this case cannot occur, and in it \( x = 7 \); hence if \( x^2 < 0 \), then \( x = 7 \).*
:::

We wrote out all five lines rather than citing @prp-vacuous-implication as a single step. Using an already proved sequent as one line of a new derivation is a genuine new permission, and Section 2.3 grants it; until then, a derivation repeats the steps.

An implication whose hypothesis cannot hold is called **vacuously true**. Nothing about it was decided by convention. It is forced by two rules that each look harmless: \( \rulename{{\to}I} \), which proves an implication by assuming its hypothesis, and \( \rulename{\bot E} \), which closes an impossible case.

Everyday language agrees. A friend says: "if you finish the exercises by Friday, I will buy you lunch". You do not finish them. Whatever your friend does on Friday, the promise has not been broken. *A promise never tested is never broken.*

Vacuous truth is not a curiosity; it is what makes case splits work. In @exm-impossible-case, line 7 closed the impossible case by \( \rulename{\bot E} \), and line 10 of the derivation of @thm-square-even-implies-even did the same. When Chapter 3 gives each connective a truth table (@def-truth-value), the rows of \( \to \) with a false hypothesis are the ones these two rules force. Chapter 4 meets the same phenomenon in another dress: a statement about "every element of the empty set" is true, because there is no element to test.

::: {.warning}
"True" is not "useful". The statements "if \( x^2 < 0 \), then \( x = 7 \)" and "if \( x^2 < 0 \), then \( x \ne 7 \)" are both true, and neither says anything about \( x \) or about \( 7 \). Likewise "if \( n \) is an even prime greater than \( 2 \), then \( n = 17 \)" is true and empty. When a hypothesis turns out to be impossible, suspect the hypothesis; do not believe the conclusion.
:::

## What the rules sound like

Here are the rows of the rule, phrase and Lean table for this section's rules. The last column is for readers who use a proof assistant; nothing depends on it.

| Rule | You write | Lean |
|------|--------------------------------------|------------------------|
| \( \rulename{\neg E} \) | "…, which contradicts …" | `exact hn hp` (goal `False`) |
| \( \rulename{\bot E} \) | "This case cannot occur." "So there is nothing to prove." | `exfalso` |

In Lean the two steps are often taken together: `absurd hp hn` closes any goal from a proof `hp` of \( P \) and a proof `hn` of \( \neg P \), which is \( \rulename{\neg E} \) followed by \( \rulename{\bot E} \), and the tactic `contradiction` finds such a pair by itself.

## Exercises

### A. Check your understanding

::: {#exr-contradiction-and-vacuous-truth-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Write the schemas of \( \rulename{\neg E} \) and \( \rulename{\bot E} \) from memory.
2. Match each sentence, taken from proofs, with the rule it uses, \( \rulename{\neg E} \) or \( \rulename{\bot E} \): "But \( n \) was assumed odd, and we have just shown it is even"; "In this case \( x^2 < 0 \), which is impossible, so there is nothing to prove".
3. True or false, with a reason: \( \rulename{\bot E} \) lets us write \( \bot \) from any line.
4. In @exm-impossible-case, why is the second box only one line long?
5. In the derivation after @thm-square-even-implies-even, why does line 8 need line 4, and why may it cite it?
:::
:::

::: {.solution}
(a) \( \rulename{\neg E} \): from a line \( i \) with \( \varphi \) and a line \( j \) with \( \neg\varphi \), both available, write \( \bot \) at line \( k \), citing \( i, j \). \( \rulename{\bot E} \): from an available line \( i \) with \( \bot \), write any statement \( \varphi \) at line \( k \), citing \( i \). The two schemas are those of @def-rules-contradiction.

(b) The first is \( \rulename{\neg E} \): "odd" and "even" clash through (E2), and the sentence records the clash. The second is \( \rulename{\bot E} \): "impossible" records a clash (an \( \rulename{\neg E} \) against \( x^2 \ge 0 \), left unsaid), and "there is nothing to prove" closes the case with whatever the case needs.

(c) False. \( \rulename{\bot E} \) runs from \( \bot \) to any statement, not from any statement to \( \bot \). \( \rulename{\bot E} \) needs a line \( \bot \) to start from. The rule that records a clash as \( \bot \) is \( \rulename{\neg E} \), and it needs two lines \( \varphi \) and \( \neg\varphi \).

(d) The box is opened by \( Q \), and \( Q \) is already the goal of both boxes. So the box's first line is also its last line, which is all \( \rulename{\vee E} \) asks of it.

(e) Line 8 is \( S \wedge T \), built by \( \rulename{\wedge I} \) from \( S \) and \( T \); line 4 is the only line that says \( S \). It may cite line 4 because the only box containing line 4, the box \( \lines{4}{11} \), also contains line 8 (the scope rule of @def-derivation).
:::

### B. Practice

::: {#exr-contradiction-and-vacuous-truth-b1}
[B1: Two clashes]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \neg(P \vee Q) \vdash Q \to R \).
2. Show that \( (P \to Q) \wedge \neg Q, \ P \vdash \neg R \), and say why \( \rulename{\bot E} \) may write a negation.
:::
:::

::: {.solution}
(a) As in @exm-manufactured-clash, with \( Q \) in place of \( P \): the box of \( Q \) manufactures \( P \vee Q \) by \( \rulename{\vee I} \) on the other side.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \vee Q)}
  \open
  \hypo {2} {Q}
  \have {3} {P \vee Q} \oi{2}
  \have {4} {\bot} \ne{3,1}
  \have {5} {R} \be{4}
  \close
  \have {6} {Q \to R} \ii{2-5}
\end{nd}$
\end{center}
```

(b) Take the first premise apart, fire the implication on the second premise, and clash.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \to Q) \wedge \neg Q}
  \hypo {2} {P}
  \have {3} {P \to Q} \ae{1}
  \have {4} {\neg Q} \ae{1}
  \have {5} {Q} \ie{3,2}
  \have {6} {\bot} \ne{5,4}
  \have {7} {\neg R} \be{6}
\end{nd}$
\end{center}
```

Line 7 is an instance of \( \rulename{\bot E} \) with \( \varphi = \neg R \): the schema allows **any** statement in place of \( \varphi \), and a negation is a statement.
:::

::: {#exr-contradiction-and-vacuous-truth-b2}
[B2: An even successor]

Let \( n \) be an integer. Prove that if \( n + 1 \) is even, then \( n \) is odd, by cases on (E1) with one case shown impossible. Tag each step with its rule, as in the proof of @thm-square-even-implies-even.
:::

::: {.solution}
Suppose \( n + 1 \) is even \( [\text{assumption for } \rulename{{\to}I}] \). By (E1), \( n \) is even or \( n \) is odd, and we argue by cases \( [\rulename{\vee E}] \).

*Case \( n \) even.* Write \( n = 2k \) with \( k \) an integer. Then \( n + 1 = 2k + 1 \), so \( n + 1 \) is odd, by the definition of odd. So \( n + 1 \) is both even and odd \( [\rulename{\wedge I}] \); this contradicts (E2) \( [\rulename{\neg E}] \). So this case cannot occur, and in it \( n \) is odd \( [\rulename{\bot E}] \).

*Case \( n \) odd.* This is the goal.

In both cases \( n \) is odd \( [\rulename{\vee E}] \). This proves that if \( n + 1 \) is even, then \( n \) is odd \( [\rulename{{\to}I}] \).

The step "\( n \) even, so \( n + 1 \) odd" plays the part that (E3) played in the theorem: it is the implication fired by \( \rulename{{\to}E} \) inside the impossible case. Here the impossible case is the **first** one, and the other case is the goal.
:::

::: {#exr-contradiction-and-vacuous-truth-b3}
[B3: Two vacuous promises]

Let \( x \) be a real number. Prove that if \( x^2 + 1 \le 0 \), then \( x > 100 \); and that if \( x^2 + 1 \le 0 \), then \( x < -100 \). Write each as a derivation with one premise, a school fact, and explain why the two statements together are no paradox.
:::

::: {.solution}
The school fact is \( x^2 + 1 > 0 \), true for every real \( x \) since \( x^2 \ge 0 \) gives \( x^2 + 1 \ge 1 > 0 \). For real numbers, \( x^2 + 1 > 0 \) says the same as \( \neg(x^2 + 1 \le 0) \). The first derivation is the pattern of @exm-vacuous-square:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (x^2 + 1 \le 0)}
  \open
  \hypo {2} {x^2 + 1 \le 0}
  \have {3} {\bot} \ne{2,1}
  \have {4} {x > 100} \be{3}
  \close
  \have {5} {x^2 + 1 \le 0 \to x > 100} \ii{2-4}
\end{nd}$
\end{center}
```

The second is the same, with \( x < -100 \) on lines 4 and 5: \( \rulename{\bot E} \) may write any statement.

No real number is both greater than \( 100 \) and less than \( -100 \). That is no paradox, because neither implication ever applies: its hypothesis holds for no real \( x \). Both are vacuously true, and both say nothing about \( x \), as the warning on vacuous truth says.
:::

### C. Going deeper

::: {#exr-contradiction-and-vacuous-truth-c1}
[C1: A disjunct that cannot hold]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( P \vee (Q \wedge \neg Q) \vdash P \).
2. What does (a) say about the statement "\( x > 0 \), or \( x = 1 \) and \( x \ne 1 \)", for a real number \( x \)?
:::
:::

::: {.solution}
(a) The premise is a disjunction, so split it by \( \rulename{\vee E} \), with both boxes ending in the goal \( P \). The box of \( P \) is a one-line box. The box of \( Q \wedge \neg Q \) is impossible: \( \rulename{\wedge E} \) gives a clash, and \( \rulename{\bot E} \) closes the case.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee (Q \wedge \neg Q)}
  \open
  \hypo {2} {P}
  \close
  \open
  \hypo {3} {Q \wedge \neg Q}
  \have {4} {Q} \ae{3}
  \have {5} {\neg Q} \ae{3}
  \have {6} {\bot} \ne{4,5}
  \have {7} {P} \be{6}
  \close
  \have {8} {P} \oe{1,2-2,3-7}
\end{nd}$
\end{center}
```

(b) With \( P \): "\( x > 0 \)" and \( Q \): "\( x = 1 \)", the statement is \( P \vee (Q \wedge \neg Q) \), since \( x \ne 1 \) is \( \neg(x = 1) \). By (a), it gives \( x > 0 \). So the second disjunct adds nothing: a disjunct that can never hold is an impossible case, and it closes itself. (Conversely, \( x > 0 \) gives the whole statement by \( \rulename{\vee I} \), so the two say the same thing.)
:::

::: {#exr-contradiction-and-vacuous-truth-c2}
[C2: A clash that escaped its box]

A student wants to show \( \neg P \vdash P \to Q \) and writes:

```{=latex}
% expect-invalid
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P}
  \open
  \hypo {2} {P}
  \have {3} {\bot} \ne{2,1}
  \close
  \have {4} {Q} \be{3}
  \open
  \hypo {5} {P}
  \have {6} {Q} \r{4}
  \close
  \have {7} {P \to Q} \ii{5-6}
\end{nd}$
\end{center}
```

::: {.enumerate options="label=(\alph*)"}
1. Is the sequent \( \neg P \vdash P \to Q \) derivable?
2. Find the first line that is not justified, and name the clause of @def-derivation it breaks.
3. Show that the move made at that line can lead from a true premise to a false conclusion.
4. Write a correct derivation.
:::
:::

::: {.solution}
(a) Yes: it is @prp-vacuous-implication. The conclusion is true; the question is whether this argument proves it.

(b) Line 4. It cites line 3, which lies inside the box \( \lines{2}{3} \), and that box has closed before line 4. By the scope rule of @def-derivation, a line inside a closed box is not available. (Lines 1–3 are fine: a box may close without a rule discharging it, although nothing then leaves it. Lines 5–7 would be fine if line 4 were.)

(c) Lines 1–4 alone would "derive" \( \neg P \vdash Q \) by the same move. Read \( P \) as "\( x > 0 \)" and \( Q \) as "\( x = 7 \)", and take \( x = -1 \). The premise \( \neg(x > 0) \) is true, and the conclusion \( x = 7 \) is false. So the move "write, outside a box, what a closed box's \( \bot \) would allow" can lead from a true premise to a false line. The line \( \bot \) on line 3 holds only under the assumption \( P \); once the box closes, that assumption is gone, and so is the clash.

(d) Move the \( \rulename{\bot E} \) inside the box, where the clash is:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P}
  \open
  \hypo {2} {P}
  \have {3} {\bot} \ne{2,1}
  \have {4} {Q} \be{3}
  \close
  \have {5} {P \to Q} \ii{2-4}
\end{nd}$
\end{center}
```

**Marking scheme.** (10 points)
- 2: answers (a) yes, citing @prp-vacuous-implication or giving a derivation.
- 3: names line 4 as the first failure and the scope rule (a line inside a closed box is not available) as the clause broken.
- 3: gives a counterexample **to the step**, not only to some conclusion: a reading of \( P \), \( Q \) under which lines 1–4 go from a true premise to a false line.
- 2: a correct derivation, with every citation available.

Fatal errors (0 for the step): blaming line 7 or line 6 (they are correct once line 4 is); saying that \( \rulename{\bot E} \) itself is the error.
:::

<!-- dependency ledger
def-rules-contradiction (claim): a line bot stands only where the premises and open assumptions cannot all hold, so bot-E never leads from true lines to a false one | ch03 (promised; soundness, thm-soundness), stated as a remark, used in no proof
def-rules-contradiction (example): for reals, a >= b says the same as not(a < b) (exactly one of a < b, a >= b holds); a != b means not(a = b); x > 1 iff not(x <= 1); x <= 1 means (x < 1) or (x = 1) | school algebra (ch02 blueprint, Allowed prerequisites); ch11 (promised) proves the order facts
exm-vacuous-square (example): x^2 >= 0 for real x, written not(x^2 < 0) | school algebra; ch11 (promised)
thm-square-even-implies-even (proof): (E1) every integer is even or odd; (E2) no integer is both | school facts stated in the text (ch02 blueprint, Allowed prerequisites); ch07 (promised)
thm-square-even-implies-even (proof): (E3) the square of an odd integer is odd | computed inline: (2k+1)^2 = 2(2k^2+2k)+1
thm-square-even-implies-even (proof): instantiating (E1)-(E3) at n and n^2; naming k with n = 2k+1 | quantifier steps, used as school reasoning; ch04 (promised)
exr-contradiction-and-vacuous-truth-b2 (solution): n = 2k gives n + 1 = 2k + 1, odd by the definition of odd | inline; (E1), (E2) as in the text
exr-contradiction-and-vacuous-truth-b3 (solution): x^2 + 1 >= 1 > 0 for real x, and x^2 + 1 > 0 says not(x^2 + 1 <= 0); no real is both > 100 and < -100 | school algebra; ch11 (promised)
exr-contradiction-and-vacuous-truth-c1 (solution): x != 1 means not(x = 1) | definition of the symbol, stated in the text
exr-contradiction-and-vacuous-truth-c2 (solution): at x = -1, not(x > 0) holds and x = 7 fails | arithmetic
-->
