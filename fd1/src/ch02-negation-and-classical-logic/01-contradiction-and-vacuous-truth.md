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

**Why may \( \rulename{\bot E} \) write anything?** A line \( \bot \) can stand only where the premises and open assumptions cannot all hold together: a derivation that reaches \( \bot \) describes a situation that never happens. Nothing said there can ever be caught false, just as a promise whose condition is never met is never broken; the subsection "Vacuous truth" below returns to this.

As in every schema (@def-rule-schema), \( \varphi \) is one statement, the same wherever it occurs, and \( i, j, k \) are line numbers. We read \( \rulename{\neg E} \) in four bullets.

- **Two given lines,** both available (the scope rule of @def-derivation), in either order on the page.
- **Exactly \( \varphi \) and \( \neg\varphi \):** the second is the first with one \( \neg \) in front of the whole of it, symbol for symbol. "Contradicts it in spirit" is not enough: \( x < 1 \) and \( x > 1 \) cannot both hold, but neither is the other's negation as written (the box below).
- **The citation** lists the unnegated line first: "\( \rulename{\neg E} \) \( i, j \)" says that line \( i \) is \( \varphi \).
- **The new line** is \( \bot \) and nothing else; what to do with the clash is the business of \( \rulename{\bot E} \).

And \( \rulename{\bot E} \) in three.

- **Schema.** The right one in the block above.
- **Reading.** One available line \( \bot \), cited alone; write **any** statement, related to nothing above, a negation or \( \bot \) itself included.
- **Example.** From line 4 \( \bot \), "\( \rulename{\bot E} \) 4" writes \( R \), or \( \neg R \), or \( x = 7 \).

::: {.second-reading title="Where a line ⊥ comes from, and why ⊥E is honest"}
Two more observations complete the reading. First, \( \rulename{\bot E} \) is the **elimination** rule of \( \bot \): it says how a line \( \bot \) is used. There is no introduction rule of its own for \( \bot \). Other rules can pass a \( \bot \) along (\( \rulename{\bot E} \) may write it again, and \( \rulename{{\to}E} \) writes it from \( \varphi \to \bot \) and \( \varphi \)), but each of them needs \( \bot \) already written in a line it uses. Apart from being assumed, the only way a line \( \bot \) first appears is by \( \rulename{\neg E} \): it is the one rule whose new line is always \( \bot \), from lines in which \( \bot \) need not occur. So \( \rulename{\neg E} \) plays two parts at once: it is the way a negation is used, and it is the way \( \bot \) is produced.

Second, why is \( \rulename{\bot E} \) honest? A rule should never lead from lines that hold to a line that fails. A line \( \bot \) can stand only in a part of a derivation where the premises and the open assumptions cannot all hold together, at least when the \( \bot \) was written by \( \rulename{\neg E} \), from some \( \varphi \) and \( \neg\varphi \) that were both available there; that the rules which only pass a \( \bot \) along keep this property is part of what Section 1.2's Looking-ahead box promised for every rule. In such a place there is no situation in which the conclusion of \( \rulename{\bot E} \) would have to be checked, so it cannot be caught failing.
:::

In the Givens/Goal table, \( \rulename{\neg E} \) adds \( \bot \) to the Givens once \( \varphi \) and \( \neg\varphi \) are both there; and with \( \bot \) among the Givens, \( \rulename{\bot E} \) ticks off any goal.

::: {.check}
Which of these pairs of lines are, as written, an instance of the given lines of \( \rulename{\neg E} \), and in which order must each be cited? The pairs are (i) \( Q \wedge R \) and \( \neg(Q \wedge R) \); (ii) \( \neg P \) and \( \neg\neg P \); (iii) \( P \to Q \) and \( \neg P \to Q \).
:::

::: {.solution}
(i) Yes, with \( \varphi = Q \wedge R \); cite the line \( Q \wedge R \) first. (ii) Yes, with \( \varphi = \neg P \): the second line is \( \neg(\neg P) \). Cite \( \neg P \) first, then \( \neg\neg P \). (iii) No. The main connective of \( \neg P \to Q \) is \( \to \) (@def-main-connective), so it is not a negation at all; the \( \neg \) applies to \( P \) alone. The negation of \( P \to Q \) would be \( \neg(P \to Q) \).
:::

::: {.remark}
**Convention: negations of order and equality.** For real numbers \( a \) and \( b \), exactly one of \( a < b \) and \( a \ge b \) holds. So \( a \ge b \) says the same as \( \neg(a < b) \), and likewise \( a > b \) the same as \( \neg(a \le b) \), \( a \le b \) as \( \neg(a > b) \), and \( a < b \) as \( \neg(a \ge b) \); and \( a \ne b \) **means** \( \neg(a = b) \), by definition. A derivation writes the negation out whenever \( \rulename{\neg E} \) or \( \rulename{\neg I} \) must see it; otherwise, and in prose, the short forms stay. Together with the box of Section 1.5, which writes \( a \le b \) out as \( (a < b) \vee (a = b) \) when \( \rulename{\vee I} \) or \( \rulename{\vee E} \) must see the disjunction, this fixes how an inequality looks on a line.
:::

The fact "no integer is both even and odd" is a negation of a conjunction, \( \neg(E \wedge O) \) with \( E \) for "\( n \) is even" and \( O \) for "\( n \) is odd". It clashes only with a line \( E \wedge O \), which \( \rulename{\wedge I} \) builds from separate lines \( E \) and \( O \).

::: {.check}
For a real number \( x \), which pairs are a clash as written, once the convention is used? (i) \( x^2 < 0 \) and \( x^2 \ge 0 \); (ii) \( x = 2 \) and \( x \ne 2 \); (iii) \( x < 1 \) and \( x > 1 \).
:::

::: {.solution}
(i) Yes: \( x^2 \ge 0 \) is \( \neg(x^2 < 0) \); cite \( x^2 < 0 \) first. (ii) Yes: \( x \ne 2 \) is \( \neg(x = 2) \); cite \( x = 2 \) first. (iii) No: \( x > 1 \) is \( \neg(x \le 1) \), and \( x < 1 \) is not \( x \le 1 \). The line \( x \le 1 \), written out, must first be built by \( \rulename{\vee I} \) (drill A2(l)).
:::

::: {.warning}
A clash must have the exact shape \( \varphi \), \( \neg\varphi \). And some pairs that look opposed do not clash at all: \( x \ge 1 \) and \( x \le 1 \) both hold at \( x = 1 \).
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

Snapshots for (b): the goal alone; then the goal handed to \( \rulename{\bot E} \), with \( \bot \) as the new goal.

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge Q}
  \hypo {2} {\neg Q}
  \have[\ ][0] {} {\vdots}
  \have[][5] {5} {R}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {P \wedge Q}
  \hypo {2} {\neg Q}
  \have[\ ][0] {} {\vdots}
  \have[][4] {4} {\bot}
  \have {5} {R} \be{4}
\end{nd}$
\end{center}
```
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

Snapshots: the box with its goal \( Q \); then the clash named as the subgoal.

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P}
  \open
  \hypo {2} {P}
  \have[\ ][0] {} {\vdots}
  \have[][4] {4} {Q}
  \close
  \have {5} {P \to Q} \ii{2-4}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {\neg P}
  \open
  \hypo {2} {P}
  \have[\ ][0] {} {\vdots}
  \have[][3] {3} {\bot}
  \have {4} {Q} \be{3}
  \close
  \have {5} {P \to Q} \ii{2-4}
\end{nd}$
\end{center}
```
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

Snapshots: the box with its goal \( R \); then the subgoal \( \bot \), for which the premise asks for \( P \vee Q \).

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \vee Q)}
  \open
  \hypo {2} {P}
  \have[\ ][0] {} {\vdots}
  \have[][5] {5} {R}
  \close
  \have {6} {P \to R} \ii{2-5}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {\neg (P \vee Q)}
  \open
  \hypo {2} {P}
  \have[\ ][0] {} {\vdots}
  \have[][4] {4} {\bot}
  \have {5} {R} \be{4}
  \close
  \have {6} {P \to R} \ii{2-5}
\end{nd}$
\end{center}
```
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

::: {.check}
Inside the box of \( P \), could \( \rulename{\bot E} \) write \( R \) straight from line 2? Which lines must come first?
:::

::: {.solution}
No. \( \rulename{\bot E} \) needs a line \( \bot \), and \( \bot \) needs the pair \( P \vee Q \), \( \neg(P \vee Q) \): first \( P \vee Q \) by \( \rulename{\vee I} \) 2, then \( \bot \) by \( \rulename{\neg E} \) 3, 1.
:::

The last derivation of this section is the pattern of the opening argument: a case split in which one case is impossible.

::: {#exm-impossible-case}
[An impossible case]

Show that \( P \vee Q, \ P \to R, \ \neg R \vdash Q \).
:::

::: {.idea}
The goal \( Q \) is a letter, so the goal gives no introduction rule to aim at. The premises do: \( P \vee Q \) is a disjunction, and Chapter 1's premise-directed move for a disjunction is \( \rulename{\vee E} \), with two boxes that both end in the current goal \( Q \). The box of \( Q \) ends as soon as it opens: its assumption is already the goal. The box of \( P \) cannot reach \( Q \) honestly, because nothing in it produces \( Q \). So we look for a clash: \( P \) feeds the premise \( P \to R \), and \( R \) clashes with \( \neg R \). The box ends on \( Q \) by \( \rulename{\bot E} \). This is the second new move: *an impossible case closes itself.*

Snapshots: the split set up; then the first box's goal handed to \( \rulename{\bot E} \).

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \hypo {2} {P \to R}
  \hypo {3} {\neg R}
  \open
  \hypo {4} {P}
  \have[\ ][0] {} {\vdots}
  \have[][7] {7} {Q}
  \close
  \open
  \hypo {8} {Q}
  \close
  \have {9} {Q} \oe{1,4-7,8-8}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {P \vee Q}
  \hypo {2} {P \to R}
  \hypo {3} {\neg R}
  \open
  \hypo {4} {P}
  \have[\ ][0] {} {\vdots}
  \have[][6] {6} {\bot}
  \have {7} {Q} \be{6}
  \close
  \open
  \hypo {8} {Q}
  \close
  \have {9} {Q} \oe{1,4-7,8-8}
\end{nd}$
\end{center}
```
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

and \( 2k^2 + 2k \) is an integer, so \( n^2 \) is odd.

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

Line 8 cites line 4, the assumption of the outer box; it may, since the box \( \lines{4}{11} \) contains line 8 (@def-derivation). Two steps of the proof are not in the derivation: passing from the facts (E1)–(E3), about every integer, to their instances for this \( n \) and this \( n^2 \), and naming the \( k \) of (E3). Both are steps about "every" and "some", used as ordinary reasoning (the note at the start of this chapter).

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

Vacuous truth is not a curiosity; it is what makes case splits work. In @exm-impossible-case, line 7 closed the impossible case by \( \rulename{\bot E} \), and line 10 of the derivation of @thm-square-even-implies-even did the same.

::: {.warning}
"True" is not "useful". The statements "if \( x^2 < 0 \), then \( x = 7 \)" and "if \( x^2 < 0 \), then \( x \ne 7 \)" are both true, and neither says anything about \( x \) or about \( 7 \). Likewise "if \( n \) is an even prime greater than \( 2 \), then \( n = 17 \)" is true and empty. When a hypothesis turns out to be impossible, suspect the hypothesis; do not believe the conclusion.
:::

## Two sequents that sound wrong

Two sequents in hand sound wrong when read aloud with unrelated statements. The first is \( Q \vdash P \to Q \): a box opened with \( P \), whose only other line repeats \( Q \) (line 1 lies in no box), closed by \( \rulename{{\to}I} \), as in Exercise B2 of Section 1.4. The second is \( \neg P \vdash P \to Q \), @prp-vacuous-implication. Read aloud: "\( 7 \) is odd; so, if every square is negative, then \( 7 \) is odd", and "\( 7 \) is not even; so, if \( 7 \) is even, then every square is negative". They are called the **paradoxes of material implication**.

Each comes from a rule, so whoever rejects one must say which rule goes: the first rests on \( \rulename{{\to}I} \) closing a box whose assumption no line uses (with \( \rulename{R} \) copying a line in from outside), the second on \( \rulename{\bot E} \). Some logics, built for purposes other than mathematics, do drop \( \rulename{\bot E} \); this book keeps it, and Exercise B3 of Section 2.5 shows that the classical rule would bring it back anyway. The same rule gives @prp-ex-falso: from a clash, anything.

Mathematics does not suffer: its "if" almost always sits under "every", joining two statements about one variable, as in "for every integer \( n \), if \( n \) is a multiple of \( 4 \), then \( n \) is even". Instances with a false hypothesis ("if \( 3 \) is a multiple of \( 4 \), then \( 3 \) is even") are true and empty, as the paradoxes say; the content lies where the hypothesis holds, and there the promise is exact. Nobody wants to prove a sentence whose two parts share nothing.

::: {.check}
Let \( x \) be a real number. Which of the two sequents makes "if \( x^2 < 0 \), then \( x > 5 \)" true, and which makes "if \( x < -3 \), then \( x^2 + 1 > 0 \)" true?
:::

::: {.solution}
The first by \( \neg P \vdash P \to Q \), since \( x^2 < 0 \) fails (\( x^2 \ge 0 \) is \( \neg(x^2 < 0) \), the convention box); the second by \( Q \vdash P \to Q \), since \( x^2 + 1 > 0 \) holds whatever \( x \) is.
:::

::: {.second-reading title="The 'if' of a counterfactual"}
"If \( 7 \) were even, \( 7 \) would be divisible by \( 2 \)" sounds true, and "if \( 7 \) were even, \( 7 \) would be divisible by \( 3 \)" sounds false, though the two share the false hypothesis "\( 7 \) is even". By \( \neg P \vdash P \to Q \), both material implications are true. So the subjunctive "if" of everyday talk is not the connective \( \to \): whether it holds depends on more than the truth of its two parts. Mathematics rarely uses it. When a proof says "if \( n \) were odd, then \( n^2 \) would be odd", it is working inside a box whose assumption is "\( n \) is odd", and its "if" is the material one.
:::

## The rule card

Before the card, the two rules at work on large statements, one use per row.

::: {#exm-contradiction-and-vacuous-truth-instances}
[Instances of \( \rulename{\neg E} \) and \( \rulename{\bot E} \)]

| Rule | \( \varphi \) | Cited lines | New line |
|---|---|---|---|
| \( \rulename{\neg E} \) | \( P \vee (Q \wedge R) \) | \( P \vee (Q \wedge R) \), then \( \neg(P \vee (Q \wedge R)) \) | \( \bot \) |
| \( \rulename{\neg E} \) | \( \neg(P \to Q) \) | \( \neg(P \to Q) \), then \( \neg\neg(P \to Q) \) | \( \bot \) |
| \( \rulename{\bot E} \) | \( (P \wedge Q) \to \neg R \) | \( \bot \) | \( (P \wedge Q) \to \neg R \) |

**Not instances.** (i) The lines \( P \to Q \) and \( P \to \neg Q \) are no pair for \( \rulename{\neg E} \): the second is an implication, not \( \neg(P \to Q) \), and no single \( \varphi \) makes the two lines \( \varphi \) and \( \neg\varphi \). (ii) From the line \( P \wedge \neg P \), "\( Q \) — \( \rulename{\bot E} \)" is not an instance: \( \rulename{\bot E} \) cites a line that is \( \bot \) itself. Take \( P \) and \( \neg P \) out by \( \rulename{\wedge E} \), write \( \bot \) by \( \rulename{\neg E} \), then \( \rulename{\bot E} \).
:::

Chapter 1's seven rules are on the card at the end of Section 1.6; here are this chapter's so far.

| Rule | Shape | You write | Lean |
|---|---|---|---|
| \( \rulename{\neg E} \) | \( \varphi \), \( \neg\varphi \) \( \Longrightarrow \) \( \bot \) | "…, which contradicts …" | `exact hn hp` (goal `False`) |
| \( \rulename{\bot E} \) | \( \bot \) \( \Longrightarrow \) any \( \varphi \) | "This case cannot occur." "So there is nothing to prove." | `exfalso` |

In Lean the two steps are often taken together: `absurd hp hn` closes any goal from a proof `hp` of \( P \) and a proof `hn` of \( \neg P \), which is \( \rulename{\neg E} \) followed by \( \rulename{\bot E} \), and the tactic `contradiction` finds such a pair by itself.

::: {.warning}
[Not allowed: \( \rulename{\neg E} \) and \( \rulename{\bot E} \)]

Each step breaks the bullet of the rule's reading named after it.

- "\( \bot \) from \( x < 1 \) and \( x > 1 \), as written": the lines must be exactly \( \varphi \) and \( \neg\varphi \) (*Exactly \( \varphi \) and \( \neg\varphi \)*; the convention box, drill A2(l)).
- "\( \bot \) — \( \rulename{\neg E} \) \( j, i \)", with line \( j \) the negation: the unnegated line is cited first (*The citation*).
- "\( \bot \) from the one line \( P \)": \( \rulename{\neg E} \) needs two lines, and \( \rulename{\bot E} \) runs from \( \bot \), never to it (*Two given lines*; the warning that \( \rulename{\bot E} \) does not run backwards).
:::

::: {.remark}
[Looking ahead]

Chapter 4 gives each connective a truth table. The rows of \( \to \) with a false hypothesis are exactly the ones that \( \rulename{{\to}I} \) and \( \rulename{\bot E} \) force here.
:::

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

::: {#exr-contradiction-and-vacuous-truth-a2}
[A2: Drill]

Each part takes a line or two. Lines are numbered as in a derivation. The parts run from one step, through a missing line, a justification column and steps to judge, to short derivations.

::: {.enumerate options="label=(\alph*)"}
1. Lines 1 \( \neg(P \wedge Q) \), 2 \( P \wedge Q \). What does "\( \rulename{\neg E} \) 2, 1" write?
2. Lines 1 \( \neg\neg P \), 2 \( \neg P \). Which line is \( \varphi \) for \( \rulename{\neg E} \), and how is the step cited?
3. Line 1 is \( \bot \). Which of \( P \), \( \neg P \), \( \bot \), \( x = 7 \) may "\( \rulename{\bot E} \) 1" write?
4. Lines 4 \( (P \to Q) \wedge R \) and 6 \( \neg((P \to Q) \wedge R) \) are available at line 7. Write line 7 by \( \rulename{\neg E} \), with its citation.
5. Line 7 is \( \bot \), justified "\( \rulename{\neg E} \) 5, 2", and line 2 is \( \neg(Q \vee R) \). What is line 5?
6. Line 9 is \( \neg P \vee R \), justified "\( \rulename{\bot E} \) 8". What is line 8?
7. Justify each line, the first three being premises: 1 \( \neg(P \vee Q) \), 2 \( R \to P \), 3 \( R \), 4 \( P \), 5 \( P \vee Q \), 6 \( \bot \), 7 \( S \).
8. Lines 1 \( \neg P \wedge Q \), 2 \( P \). Is "3. \( \bot \) — \( \rulename{\neg E} \) 2, 1" legal?
9. Line 1 is \( P \). May "2. \( \bot \) — \( \rulename{\bot E} \) 1" be written?
10. For a real number \( x \), do the lines \( x \ge 1 \) and \( x \le 1 \) clash?
11. Find the illegal line: 1 \( P \to Q \); 2 \( \neg Q \); 3 | \( P \); 4 | \( Q \), \( \rulename{{\to}E} \) 1, 3; 5 | \( \bot \), \( \rulename{\neg E} \) 2, 4; 6 | \( R \), \( \rulename{\bot E} \) 5; 7 \( P \to R \), \( \rulename{{\to}I} \) 3–6.
12. For one real number \( x \), lines 1 \( x < 1 \) and 2 \( x > 1 \) are given. Make them a clash, line by line.
13. Derive \( P, \ \neg P \wedge Q \vdash R \).
14. Derive \( \neg Q \vdash Q \to P \).
15. Derive \( P \to Q, \ \neg Q, \ P \vdash R \).
:::
:::

::: {.solution}
(a) \( \bot \).

(b) \( \varphi = \neg P \) (line 2), and \( \neg\varphi = \neg\neg P \) (line 1): the step is cited "\( \rulename{\neg E} \) 2, 1".

(c) All four: \( \rulename{\bot E} \) writes any statement.

(d) 7 \( \bot \), "\( \rulename{\neg E} \) 4, 6": line 4 is \( \varphi \), line 6 is \( \neg\varphi \).

(e) \( Q \vee R \), the unnegated form of line 2.

(f) \( \bot \): \( \rulename{\bot E} \) cites one line, and it is \( \bot \).

(g) 4 \( \rulename{{\to}E} \) 2, 3; 5 \( \rulename{\vee I} \) 4; 6 \( \rulename{\neg E} \) 5, 1; 7 \( \rulename{\bot E} \) 6.

(h) No: line 1's main connective is \( \wedge \), so it is not a negation. First write \( \neg P \) by \( \rulename{\wedge E} \) 1 as line 3, then \( \bot \) by \( \rulename{\neg E} \) 2, 3.

(i) No: \( \rulename{\bot E} \) starts from a line \( \bot \); no rule writes \( \bot \) from a single line \( P \).

(j) No: both hold at \( x = 1 \).

(k) Line 5: the unnegated line comes first. With line 2 as \( \varphi \), line 4 would have to be \( \neg\neg Q \). Correct: "\( \rulename{\neg E} \) 4, 2".

(l) Write line 2 as \( \neg((x < 1) \vee (x = 1)) \) (\( x > 1 \) says that \( x \le 1 \) fails, and \( x \le 1 \) is written out because \( \rulename{\vee I} \) must build it); 3 \( (x < 1) \vee (x = 1) \), \( \rulename{\vee I} \) 1; 4 \( \bot \), \( \rulename{\neg E} \) 3, 2.

(m) 3 \( \neg P \), \( \rulename{\wedge E} \) 2; 4 \( \bot \), \( \rulename{\neg E} \) 1, 3; 5 \( R \), \( \rulename{\bot E} \) 4.

(n) 2 | \( Q \), assumption; 3 | \( \bot \), \( \rulename{\neg E} \) 2, 1; 4 | \( P \), \( \rulename{\bot E} \) 3; 5 \( Q \to P \), \( \rulename{{\to}I} \) 2–4.

(o) 4 \( Q \), \( \rulename{{\to}E} \) 1, 3; 5 \( \bot \), \( \rulename{\neg E} \) 4, 2; 6 \( R \), \( \rulename{\bot E} \) 5.
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

::: {#exr-contradiction-and-vacuous-truth-b4}
[B4: An impossible case, scaffolded]

A search for \( P \vee Q, \ P \to R, \ Q \to S, \ \neg R \vdash S \) has reached the stage below. *Name the move, then complete it.*

```{=latex}
% schema (partial derivation: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \hypo {2} {P \to R}
  \hypo {3} {Q \to S}
  \hypo {4} {\neg R}
  \open
  \hypo {5} {P} \purpose{\oe}
  \have[\ ][0] {} {\vdots}
  \have[][8] {8} {S} \by{?}{}
  \close
  \open
  \hypo {9} {Q} \purpose{\oe}
  \have[\ ][0] {} {\vdots}
  \have[][10] {10} {S} \by{?}{}
  \close
  \have {11} {S} \oe{1,5-8,9-10}
\end{nd}$
\end{center}
```
:::

::: {.solution}
The move is *an impossible case closes itself*. The case \( P \) cannot reach \( S \) honestly: nothing in it produces \( S \). So it reaches a clash: \( P \) fires line 2, and \( R \) clashes with line 4. The case \( Q \) reaches \( S \) by firing line 3.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \hypo {2} {P \to R}
  \hypo {3} {Q \to S}
  \hypo {4} {\neg R}
  \open
  \hypo {5} {P}
  \have {6} {R} \ie{2,5}
  \have {7} {\bot} \ne{6,4}
  \have {8} {S} \be{7}
  \close
  \open
  \hypo {9} {Q}
  \have {10} {S} \ie{3,9}
  \close
  \have {11} {S} \oe{1,5-8,9-10}
\end{nd}$
\end{center}
```
:::

::: {#exr-contradiction-and-vacuous-truth-b5}
[B5: Derive or break]

For each claim, either derive it with the rules of Chapter 1 and of this section (\( \rulename{\neg E} \) and \( \rulename{\bot E} \); no other rule for "not" yet), or break it by statements about a real number \( x \) that make its counterexample set true at one value of \( x \).

::: {.enumerate options="label=(\alph*)"}
1. \( (P \wedge \neg Q) \vee R, \ Q \vdash R \).
2. \( P \vee Q, \ \neg Q \vdash \neg P \).
3. \( P \to \neg P, \ P \vdash Q \).
4. \( P \to Q, \ \neg P \vdash \neg Q \).
5. \( \neg(P \wedge Q), \ P \vdash Q \to R \).
6. \( \neg(P \wedge Q) \vdash \neg P \vee Q \).
7. \( P \vee Q, \ P \to R, \ \neg R \vdash P \).
8. \( P \to (Q \wedge \neg R), \ R \vdash P \to S \).
:::
:::

::: {.solution}
(a) Derive. Split on the first premise; the case \( P \wedge \neg Q \) is impossible beside the premise \( Q \), and the case \( R \) is the goal.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge \neg Q) \vee R}
  \hypo {2} {Q}
  \open
  \hypo {3} {P \wedge \neg Q}
  \have {4} {\neg Q} \ae{3}
  \have {5} {\bot} \ne{2,4}
  \have {6} {R} \be{5}
  \close
  \open
  \hypo {7} {R}
  \close
  \have {8} {R} \oe{1,3-6,7-7}
\end{nd}$
\end{center}
```

(b) Break. Take \( P \): "\( x > 0 \)", \( Q \): "\( x > 5 \)". At \( x = 1 \), \( P \vee Q \) is true (\( 1 > 0 \)), \( \neg Q \) is true (\( 1 > 5 \) fails), and \( P \) is true, so \( \neg\neg P \) is true: the counterexample set \( P \vee Q \), \( \neg Q \), \( \neg\neg P \) is true.

(c) Derive. The premise \( P \) fires the implication, and its conclusion clashes with \( P \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to \neg P}
  \hypo {2} {P}
  \have {3} {\neg P} \ie{1,2}
  \have {4} {\bot} \ne{2,3}
  \have {5} {Q} \be{4}
\end{nd}$
\end{center}
```

(d) Break. Take \( P \): "\( x > 3 \)", \( Q \): "\( x > 1 \)". The premise \( P \to Q \) holds for every \( x \). At \( x = 2 \), \( \neg P \) is true (\( 2 > 3 \) fails) and \( Q \) is true (\( 2 > 1 \)), so \( \neg\neg Q \) is true: the counterexample set \( P \to Q \), \( \neg P \), \( \neg\neg Q \) is true.

(e) Derive. The goal is an implication; inside its box, \( \rulename{\wedge I} \) manufactures the other half of the clash with the first premise.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \wedge Q)}
  \hypo {2} {P}
  \open
  \hypo {3} {Q}
  \have {4} {P \wedge Q} \ai{2,3}
  \have {5} {\bot} \ne{4,1}
  \have {6} {R} \be{5}
  \close
  \have {7} {Q \to R} \ii{3-6}
\end{nd}$
\end{center}
```

(f) Break. Take \( P \): "\( x > 0 \)", \( Q \): "\( x > 5 \)". At \( x = 1 \), \( P \wedge Q \) is false, so \( \neg(P \wedge Q) \) is true; and \( \neg P \) and \( Q \) are both false, so \( \neg P \vee Q \) is false. The counterexample set \( \neg(P \wedge Q) \), \( \neg(\neg P \vee Q) \) is true.

(g) Break. Take \( P \): "\( x > 5 \)", \( Q \): "\( x > 0 \)", \( R \): "\( x > 3 \)". The premise \( P \to R \) holds for every \( x \). At \( x = 1 \), \( P \vee Q \) is true (\( 1 > 0 \)), \( \neg R \) is true (\( 1 > 3 \) fails), and \( P \) is false, so \( \neg P \) is true: the counterexample set \( P \vee Q \), \( P \to R \), \( \neg R \), \( \neg P \) is true.

(h) Derive. Inside the box of \( P \), the first premise fires, and its half \( \neg R \) clashes with the premise \( R \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \wedge \neg R)}
  \hypo {2} {R}
  \open
  \hypo {3} {P}
  \have {4} {Q \wedge \neg R} \ie{1,3}
  \have {5} {\neg R} \ae{4}
  \have {6} {\bot} \ne{2,5}
  \have {7} {S} \be{6}
  \close
  \have {8} {P \to S} \ii{3-7}
\end{nd}$
\end{center}
```

The four that break are look-alikes. (b) draws the wrong conclusion from a refuted disjunct: the disjunctive syllogism of Section 2.3 gives \( P \), not \( \neg P \). (d) denies the antecedent, the look-alike of the modus tollens that Section 2.3 derives. (g) is a look-alike of @exm-impossible-case, whose conclusion is the other disjunct. (f) is a look-alike of a De Morgan law of Section 2.5. The four that derive follow worked patterns of this section: @exm-impossible-case for (a), @prp-ex-falso for (c), @prp-vacuous-implication for (e) and (h).

**Marking scheme.** (16 points) For each claim: 1 for the verdict; 1 for a derivation every line of which checks, or for a choice of statements and one value of \( x \) at which **every** member of the counterexample set is true. Fatal errors (0 for the claim): a "break" at which some premise is false; a derivation that uses a rule not yet available (\( \rulename{\neg I} \), \( \rulename{RAA} \) or a derived rule of Section 2.3).
:::

::: {#exr-contradiction-and-vacuous-truth-b6}
[B6: Name the rule you reject]

::: {.enumerate options="label=(\alph*)"}
1. List the rules used by a derivation of \( \neg P \vdash P \to Q \) and by one of \( Q \vdash P \to Q \).
2. Suppose \( \rulename{\bot E} \) were dropped. Derive \( \neg P \vdash P \to \bot \) without it, and say what this derivation stops short of.
3. Suppose instead \( \rulename{{\to}I} \) were allowed only when the box's assumption is cited by some line of the box or is itself the box's last line. Which of the two derivations of (a) is lost? Is the one-line box of \( \vdash P \to P \) lost? Is the sequent \( Q \vdash P \to Q \) lost?
4. Let \( n \) be an integer. For \( n = 3 \), \( n = 6 \) and \( n = 8 \), write the instance of "if \( n \) is a multiple of \( 4 \), then \( n \) is even", and say for each whether the first sequent of (a), the second, or neither, decides its truth.
:::
:::

::: {.solution}
(a) \( \neg P \vdash P \to Q \): \( \rulename{{\to}I} \), \( \rulename{\neg E} \), \( \rulename{\bot E} \) (@prp-vacuous-implication). \( Q \vdash P \to Q \): \( \rulename{{\to}I} \) and repetition.

(b) Four lines:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P}
  \open
  \hypo {2} {P}
  \have {3} {\bot} \ne{2,1}
  \close
  \have {4} {P \to \bot} \ii{2-3}
\end{nd}$
\end{center}
```

It stops at \( \bot \) inside the box, where the derivation of @prp-vacuous-implication wrote \( Q \): the step from \( \bot \) to \( Q \) was \( \rulename{\bot E} \)'s. What survives says only that \( P \) leads to a contradiction.

(c) The derivation of \( Q \vdash P \to Q \) is lost: no line of its box cites the assumption \( P \) (line 3 repeats line 1). The box of \( \vdash P \to P \) is kept: its last line is its assumption, which the restriction allows. The derivation of @prp-vacuous-implication is kept: line 3 cites the assumption. But the sequent \( Q \vdash P \to Q \) is not lost. This derivation meets the restriction, since line 3 cites the assumption:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {Q}
  \open
  \hypo {2} {P}
  \have {3} {P \wedge Q} \ai{2,1}
  \have {4} {Q} \ae{3}
  \close
  \have {5} {P \to Q} \ii{2-4}
\end{nd}$
\end{center}
```

The restriction kills one derivation, not the sequent; a logic that really rejects the paradox has to restrict more than one rule.

(d) \( n = 3 \): "if \( 3 \) is a multiple of \( 4 \), then \( 3 \) is even"; hypothesis and conclusion are both false, so only \( \neg P \vdash P \to Q \) decides it. \( n = 6 \): "if \( 6 \) is a multiple of \( 4 \), then \( 6 \) is even"; the hypothesis is false and the conclusion true, so either sequent decides it. \( n = 8 \): "if \( 8 \) is a multiple of \( 4 \), then \( 8 \) is even"; both parts are true (\( 8 = 4 \cdot 2 \)), so the first sequent does not apply and the second does, since the conclusion is true. This is the one instance of the three whose hypothesis holds, the kind in which the theorem says something: here it can be fired by \( \rulename{{\to}E} \).

**Marking scheme.** (10 points) 2: (a), both rule lists. 2: (b), a correct four-line derivation (1) and the remark that the step to \( Q \) is \( \rulename{\bot E} \)'s (1). 3: (c), the right derivation lost and the reason, that the assumption is never cited (1); \( \vdash P \to P \) kept (1); and a derivation of \( Q \vdash P \to Q \) that meets the restriction (1). 3: (d), one point per value, each with the truth values of hypothesis and conclusion. Fatal error (0 for (b)): a derivation of \( P \to Q \) itself without \( \rulename{\bot E} \) that cites a line inside a closed box.
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
def-rules-contradiction (claim): a line bot stands only where the premises and open assumptions cannot all hold, so bot-E never leads from true lines to a false one (main-line "Why may bot-E write anything?" and fold) | Section 1.2's Looking-ahead box (soundness promised for every rule of Chapters 1 and 2; F1.3, thm-soundness), stated as a remark, used in no proof
def-rules-contradiction (example): convention box: for reals, exactly one of a < b, a >= b holds, so a >= b says not(a < b); likewise a > b is not(a <= b), a <= b is not(a > b), a < b is not(a >= b); a != b means not(a = b); x <= 1 means (x < 1) or (x = 1) (the box of Section 1.5) | school algebra (F1.2 blueprint, Allowed prerequisites); AN1.1 (promised) proves the order facts
def-rules-contradiction (solution): Quick check on the convention: x^2 >= 0 for real x, written not(x^2 < 0); x != 2 is not(x = 2); x > 1 is not(x <= 1) | school algebra; the convention box
exm-vacuous-square (example): x^2 >= 0 for real x, written not(x^2 < 0) | school algebra; AN1.1 (promised)
thm-square-even-implies-even (proof): (E1) every integer is even or odd; (E2) no integer is both | school facts stated in the text (F1.2 blueprint, Allowed prerequisites); F2.2 (promised)
thm-square-even-implies-even (proof): (E3) the square of an odd integer is odd | computed inline: (2k+1)^2 = 2(2k^2+2k)+1
thm-square-even-implies-even (proof): instantiating (E1)-(E3) at n and n^2; naming k with n = 2k+1 | steps about "every" and "some", used as ordinary reasoning (index note); F1.4 (promised)
prp-vacuous-implication (example): "Two sequents that sound wrong": 7 is odd and not even; no square is negative (x^2 >= 0); 3 is not a multiple of 4 and not even | school arithmetic and algebra
prp-vacuous-implication (claim): some logics drop bot-E (relevance and paraconsistent logics; none named) | remark about other logics, used in no proof; 2.5 B3 derives bot-E from RAA and repetition
prp-vacuous-implication (solution): Quick check on the paradoxes: x^2 < 0 fails for every real x; x^2 + 1 > 0 for every real x | school algebra; AN1.1 (promised)
prp-vacuous-implication (example): fold on the counterfactual: 7 is not divisible by 2 and not divisible by 3 | arithmetic
exr-contradiction-and-vacuous-truth-a2 (solution): (j) x >= 1 and x <= 1 both hold at x = 1; (l) x > 1 is not(x <= 1), and x <= 1 is written (x < 1) or (x = 1) | arithmetic; the convention box
exr-contradiction-and-vacuous-truth-b2 (solution): n = 2k gives n + 1 = 2k + 1, odd by the definition of odd | inline; (E1), (E2) as in the text
exr-contradiction-and-vacuous-truth-b3 (solution): x^2 + 1 >= 1 > 0 for real x, and x^2 + 1 > 0 says not(x^2 + 1 <= 0); no real is both > 100 and < -100 | school algebra; AN1.1 (promised)
exr-contradiction-and-vacuous-truth-b5 (solution): the breaks: (b) at x = 1 with x > 0, x > 5; (d) at x = 2 with x > 3, x > 1, and x > 3 implies x > 1 for every x; (f) at x = 1 with x > 0, x > 5; (g) at x = 1 with x > 5, x > 0, x > 3, and x > 5 implies x > 3 for every x | arithmetic
exr-contradiction-and-vacuous-truth-b6 (solution): 3 and 6 are not multiples of 4, 8 = 4 * 2; 3 is odd, 6 and 8 are even | arithmetic
exr-contradiction-and-vacuous-truth-c1 (solution): x != 1 means not(x = 1) | definition of the symbol, stated in the text
exr-contradiction-and-vacuous-truth-c2 (solution): at x = -1, not(x > 0) holds and x = 7 fails | arithmetic
-->
