# Proving a Negation

The rules of Section 2.1 **use** a negation: \( \rulename{\neg E} \) records a clash, and \( \rulename{\bot E} \) turns a clash into any statement we like. Neither rule can **prove** a negation unless the lines already clash: \( \rulename{\bot E} \) writes one only from a line \( \bot \). So we still cannot prove that no rational number has square \( 2 \), or even that \( x^2 + 1 \) is never \( 0 \). This section adds the one rule that proves a negation, \( \rulename{\neg I} \), and uses it for one of the oldest proofs in mathematics.

## How to prove that something is not so

To show that no rational number has square \( 2 \), we cannot inspect the rational numbers one by one: there are infinitely many. A mathematician instead supposes the opposite and shows that it leads to something impossible: "suppose \( r \) is rational and \( r^2 = 2 \); …; this is a contradiction; hence \( r^2 \ne 2 \)."

Try the smaller goal \( x^2 + 1 \ne 0 \), for a real number \( x \), with the rules so far. The goal is \( \neg(x^2 + 1 = 0) \), and its main connective is \( \neg \). Chapter 1's goal-directed move asks for the introduction rule of the main connective, and \( \neg \) has none yet. The rules of Section 2.1 do not help: \( \rulename{\bot E} \) could write the goal, but only from a line \( \bot \), and nothing available clashes. The statement \( x^2 + 1 = 0 \) is not a line of anything; it is the thing we want to rule out.

The mathematician's sentence shows the missing rule. "Suppose \( r^2 = 2 \)" opens a box, exactly like the box of \( \rulename{{\to}I} \) in @def-rules-implication, and "this is a contradiction" is its last line, \( \bot \). The only new thing is what the box gives when it closes.

*To prove "not \( \varphi \)", assume \( \varphi \) and reach a contradiction.*

::: {#def-rules-negation}
[Rules for Negation]

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \open
  \hypo {i} {\varphi}
  \have {} {\vdots}
  \have {j} {\bot}
  \close
  \have {k} {\neg \varphi} \ni{i-j}
\end{nd}$
\qquad
$\begin{nd}[schema]
  \have {i} {\varphi}
  \have {j} {\neg \varphi}
  \have {k} {\bot} \ne{i,j}
\end{nd}$
\end{center}
```

The left schema is \( \rulename{\neg I} \) (**not-introduction**): the assumption \( \varphi \) is **discharged** when the box closes, and the line \( \bot \) is a line of that box itself, not of a box inside it. The right schema is \( \rulename{\neg E} \), recalled from @def-rules-contradiction, so that the rule that proves a negation and the rule that uses one stand together.
:::

This rule has conditions that matter; read each one.

1. **Open a box** whose first line is the assumption \( \varphi \). It is the **unnegated** statement: the thing we want to refute, not the thing we want to prove. Any statement may be assumed. In a finished derivation this assumption is printed **"asm, for \( \rulename{\neg I} \)"**: the annotation names the rule that will close the box, as "asm, for \( \rulename{{\to}I} \)" did in Section 1.4.
2. **Inside the box** every rule may be used, and every line available just above the box may be cited, as in any box (@def-derivation).
3. **The last line of the box** is exactly \( \bot \), and it is a line of that box itself, not inside a further box opened within it. This is the same wording as for \( \rulename{{\to}I} \), and every box rule shares it.
4. **Close the box** and write \( \neg\varphi \) on the next line, outside it. The justification cites the box as a range, "\( \rulename{\neg I} \) \( i \)–\( j \)". The assumption is discharged: after the box closes, nothing inside it may be cited, and only the negation leaves.
5. **The new line is always a negation.** \( \rulename{\neg I} \) never writes a statement whose main connective is not \( \neg \).

::: {.second-reading title="Edge cases of not-introduction"}
The degenerate case is a box of one line, whose assumption is already \( \bot \). The box \( \lines{1}{1} \) then ends on \( \bot \) as soon as it opens, and \( \rulename{\neg I} \) gives \( \neg\bot \):

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {\bot}
  \close
  \have {2} {\neg \bot} \ni{1-1}
\end{nd}$
\end{center}
```

So \( \vdash \neg\bot \): "it is not the case that contradiction" is derivable from nothing, as it should be.

**A noninstance by one change.** Take a box opened by \( \varphi \) whose last line is \( \neg\varphi \) instead of \( \bot \). It looks as if the assumption has refuted itself, and \( \rulename{\neg I} \) still does not apply: the box must end on \( \bot \). One more line, \( \bot \) by \( \rulename{\neg E} \) citing the assumption and the line \( \neg\varphi \), repairs it. The same holds if \( \bot \) is reached only inside a smaller box within the box: it is not then a line of the box itself.

**A box that never uses its assumption.** A box may reach \( \bot \) without ever using its assumption. That is legal, but it is a sign: if no line of the box depends on \( \varphi \), the same lines could have been written just above the box, where \( \bot \) would then stand, and \( \rulename{\bot E} \) would have written \( \neg\varphi \), or anything else, directly. The lines available above the box were already contradictory. When your \( \rulename{\neg I} \) box never uses its assumption, look for the error above the box, not in it.
:::

**Why this rule.** The statement \( \neg\varphi \) says that \( \varphi \) fails, and the box shows what would happen if \( \varphi \) held: together with the lines above it, it would lead to \( \bot \), which never holds. So in any situation where the lines above the box hold, \( \varphi \) cannot hold. That is exactly what \( \neg\varphi \) claims.

The rules for \( \neg \) have the same shapes as rules we already know, with \( \bot \) in one slot. Put them beside the rules for \( \to \), applied to the statement \( \varphi \to \bot \):

| To … | a negation \( \neg\varphi \) | an implication \( \varphi \to \bot \) |
|---|---|---|
| prove it | box from \( \varphi \) to \( \bot \), then \( \rulename{\neg I} \) | box from \( \varphi \) to \( \bot \), then \( \rulename{{\to}I} \) |
| use it, given \( \varphi \) | \( \bot \) by \( \rulename{\neg E} \) | \( \bot \) by \( \rulename{{\to}E} \) |

::: {.remark}
Row by row, \( \neg\varphi \) behaves exactly like \( \varphi \to \bot \): "not \( \varphi \)" means "\( \varphi \) leads to contradiction". Some presentations of logic take this as the definition of \( \neg \). This book keeps \( \neg \) as a connective with its own rules.
:::

::: {.warning}
Do not open the box with what you want to prove. To prove \( \neg\varphi \), the box opens with \( \varphi \). A box opened by \( \neg\varphi \) and ending in \( \bot \) gives \( \neg\neg\varphi \) by \( \rulename{\neg I} \), the negation of the goal, not the goal. So a box opened with \( \neg(x > 0) \) and closed by \( \rulename{\neg I} \) gives \( \neg\neg(x > 0) \), not \( x > 0 \); Section 2.5 shows the other kind of "suppose not". This is the negation's version of the converse error that Section 1.4 found in Argument B.
:::

In the Givens/Goal table, \( \rulename{\neg I} \) moves \( \varphi \) into the Givens and makes \( \bot \) the goal.

## The first example: a number that is never zero

The goal we could not reach at the start of the section comes first.

::: {#exm-square-plus-one}
[A negative statement proved by not-introduction]

Let \( x \) be a real number. Prove that \( x^2 + 1 \ne 0 \), naming the rules.
:::

::: {.idea}
The goal \( x^2 + 1 \ne 0 \) is \( \neg(x^2 + 1 = 0) \), a negation, so open a box on \( x^2 + 1 = 0 \) and look for a clash. The school fact \( x^2 \ge 0 \), that is \( \neg(x^2 < 0) \), is the negation available; its unnegated half \( x^2 < 0 \) is the subgoal, and algebra on the assumption produces it.
:::

::: {.solution}
The goal \( x^2 + 1 \ne 0 \) is \( \neg(x^2 + 1 = 0) \), so we use \( \rulename{\neg I} \). Suppose \( x^2 + 1 = 0 \) \( [\text{assumption for } \rulename{\neg I}] \). Then \( x^2 = -1 \), so \( x^2 < 0 \). But \( x^2 \ge 0 \), that is, \( \neg(x^2 < 0) \), so we have a contradiction \( [\rulename{\neg E}] \). Hence \( x^2 + 1 \ne 0 \) \( [\rulename{\neg I}] \).

With the school fact as the premise:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg(x^2 < 0)}
  \open
  \hypo {2} {x^2 + 1 = 0}
  \have {3} {x^2 < 0} \by{algebra}{2}
  \have {4} {\bot} \ne{3,1}
  \close
  \have {5} {\neg(x^2 + 1 = 0)} \ni{2-4}
\end{nd}$
\end{center}
```
:::

::: {.check}
In this derivation, which box does \( \rulename{\neg I} \) cite, and which statement opened it?
:::

::: {.solution}
The box \( \lines{2}{4} \), opened by \( x^2 + 1 = 0 \), the unnegated statement. The conclusion on line 5 is its negation, \( x^2 + 1 \ne 0 \).
:::

## First derivations with not-introduction

The goal-directed move of this section: *a goal \( \neg\varphi \) opens a box with \( \varphi \), and the new goal is \( \bot \).* From there, Section 2.1's move takes over: *goal \( \bot \), find a clash*, among the available lines or by manufacturing its missing half.

::: {#exm-double-negation-introduction}
[Two negations from one premise]

Show that (a) \( P \vdash \neg\neg P \), and (b) \( (P \vee Q) \to \neg P \vdash \neg P \).
:::

::: {.idea}
(a) The goal \( \neg\neg P \) is \( \neg(\neg P) \), a negation of \( \neg P \). So the box opens with what is negated, \( \neg P \), and aims at \( \bot \). The clash is immediate: the premise \( P \) and the assumption \( \neg P \).

The goal alone (left); then the box opened on \( \neg P \), its goal \( \bot \) at its foot (right).

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \have[\ ][0] {} {\vdots}
  \have[][4] {4} {\neg\neg P}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {P}
  \open
  \hypo {2} {\neg P}
  \have[\ ][0] {} {\vdots}
  \have[][3] {3} {\bot}
  \close
  \have {4} {\neg\neg P} \ni{2-3}
\end{nd}$
\end{center}
```

(b) The goal \( \neg P \) opens a box on \( P \). Inside it the premise is an implication, and the premise-directed move feeds it its hypothesis \( P \vee Q \), which \( \rulename{\vee I} \) manufactures from \( P \). The premise then hands back \( \neg P \), and that clashes with the box's own assumption. The assumption is used twice: once to build the hypothesis, once in the clash.

The box opened, its goal \( \bot \) at its foot (left); then the hypothesis \( P \vee Q \) manufactured, with line 5 still to reach (right).

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {(P \vee Q) \to \neg P}
  \open
  \hypo {2} {P}
  \have[\ ][0] {} {\vdots}
  \have[][5] {5} {\bot}
  \close
  \have {6} {\neg P} \ni{2-5}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {(P \vee Q) \to \neg P}
  \open
  \hypo {2} {P}
  \have {3} {P \vee Q} \oi{2}
  \have[\ ][0] {} {\vdots}
  \have[][5] {5} {\bot}
  \close
  \have {6} {\neg P} \ni{2-5}
\end{nd}$
\end{center}
```
:::

::: {.solution}
(a) Four lines.

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

(b) Six lines.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \vee Q) \to \neg P}
  \open
  \hypo {2} {P}
  \have {3} {P \vee Q} \oi{2}
  \have {4} {\neg P} \ie{1,3}
  \have {5} {\bot} \ne{2,4}
  \close
  \have {6} {\neg P} \ni{2-5}
\end{nd}$
\end{center}
```

In (b), line 4 already says \( \neg P \), but it lies inside the box of \( P \) and depends on that assumption, so it cannot be the conclusion. Line 6 is the same statement outside the box, where it depends on the premise alone.
:::

Derivation (a) adds two negations. The reverse passage, from \( \neg\neg P \) alone to \( P \), would have to **remove** two, and no rule so far has a negation as its one given line and the unnegated statement as its new line: \( \rulename{\neg E} \) needs a second line and writes only \( \bot \), and \( \rulename{\neg I} \) only adds a \( \neg \). Section 2.5 returns to this.

::: {.check}
Is \( \neg(P \vee Q) \vdash \neg P \)? If so, give a derivation and name its rules. Compare it with @exm-manufactured-clash, which has the same premise.
:::

::: {.solution}
Yes. The goal \( \neg P \) is a negation, so assume \( P \) and aim at \( \bot \); \( \rulename{\vee I} \) turns \( P \) into \( P \vee Q \), which clashes with the premise.

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
\end{nd}$
\end{center}
```

The rules are \( \rulename{\vee I} \), \( \rulename{\neg E} \), and \( \rulename{\neg I} \). The box is the same as in @exm-manufactured-clash up to its line \( \bot \). There the goal was \( P \to R \), so the box had to end on \( R \), written by \( \rulename{\bot E} \), and closed by \( \rulename{{\to}I} \). Here the goal is \( \neg P \), so the box ends on \( \bot \) itself and closes by \( \rulename{\neg I} \). In words: if neither \( P \) nor \( Q \) holds, then in particular \( P \) does not.
:::

In the next derivation the clash itself creates a goal that is a negation, and the move of this section is used a second time, one box inside another.

::: {#exm-triple-negation}
[Three negations become one]

Show that \( \neg\neg\neg P \vdash \neg P \).
:::

::: {.idea}
The goal \( \neg P \) opens a box on \( P \), with goal \( \bot \). Which clash? The only negation available is the premise \( \neg(\neg\neg P) \), so the premise-directed question asks for its unnegated half, \( \neg\neg P \): that becomes the subgoal. It is itself a negation, \( \neg(\neg P) \), so the goal-directed move opens a second \( \rulename{\neg I} \) box, on \( \neg P \), with goal \( \bot \). Inside it, \( \neg P \) clashes with the outer assumption \( P \). This is the first derivation in which a \( \rulename{\neg I} \) box is opened for a subgoal that a clash created.

The outer box opened, its goal \( \bot \) at its foot (left); then the clash with the premise chosen, so that \( \neg\neg P \) becomes the goal of the gap (right).

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {\neg\neg\neg P}
  \open
  \hypo {2} {P}
  \have[\ ][0] {} {\vdots}
  \have[][6] {6} {\bot}
  \close
  \have {7} {\neg P} \ni{2-6}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {\neg\neg\neg P}
  \open
  \hypo {2} {P}
  \have[\ ][0] {} {\vdots}
  \have[][5] {5} {\neg\neg P}
  \have {6} {\bot} \ne{5,1}
  \close
  \have {7} {\neg P} \ni{2-6}
\end{nd}$
\end{center}
```
:::

::: {.solution}
Seven lines.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg\neg\neg P}
  \open
  \hypo {2} {P}
  \open
  \hypo {3} {\neg P}
  \have {4} {\bot} \ne{2,3}
  \close
  \have {5} {\neg\neg P} \ni{3-4}
  \have {6} {\bot} \ne{5,1}
  \close
  \have {7} {\neg P} \ni{2-6}
\end{nd}$
\end{center}
```

Line 4 may cite line 2, because the only box containing line 2, the box \( \lines{2}{6} \), also contains line 4 (@def-derivation). The inner box \( \lines{3}{4} \) ends on \( \bot \) as a line of its own, and so does the outer box \( \lines{2}{6} \), at line 6; each \( \rulename{\neg I} \) cites its own box. Notice what did **not** happen: no line removes a pair of negations. Three became one by adding them, twice, and clashing.
:::

## How the rule looks in a mathematical proof

The proof that no rational number has square \( 2 \) has the shape of \( \rulename{\neg I} \): the claim is negative, so we assume its opposite and look for \( \bot \). The tool that finds the clash is @thm-square-even-implies-even, and the school fact it needs is about writing fractions:

**(L)** Every rational number can be written as \( p/q \) with \( p \) and \( q \) integers, \( q \ne 0 \), and \( p \) and \( q \) **not both even**.

This holds because a fraction whose numerator and denominator are both even can be reduced by \( 2 \), and the reduction cannot go on for ever, since the denominator shrinks in absolute value each time. Making "cannot go on for ever" precise needs a fact about the natural numbers that this book does not prove; here we take (L) as known.

::: {#thm-sqrt2-irrational}
[Irrationality of the Square Root of Two]

There is no rational number whose square is \( 2 \). So if a real number \( \sqrt{2} \) with square \( 2 \) exists, it is irrational.
:::

::: {.idea}
Fix a rational number \( r \) and prove the negative statement \( r^2 \ne 2 \) by \( \rulename{\neg I} \): assume \( r^2 = 2 \) and hunt for \( \bot \). Write \( r = p/q \) as in (L), so that the equation becomes \( p^2 = 2q^2 \). The only available negation is "not both even", so the clash must come from showing that \( p \) and \( q \) **are** both even; @thm-square-even-implies-even is the tool for that, used twice. *Before reading on: the second use of @thm-square-even-implies-even needs the line "\( q^2 \) is even". From which two earlier lines of the proof will it come?*
:::

::: {.proof}
Let \( r \) be a rational number, and suppose \( r^2 = 2 \) \( [\text{assumption for } \rulename{\neg I}] \). By (L), \( r = p/q \) for integers \( p \) and \( q \) with \( q \ne 0 \), not both even. Then \( p^2 = r^2 q^2 = 2q^2 \), so \( p^2 \) is even. By @thm-square-even-implies-even, \( p \) is even \( [\rulename{{\to}E}] \), say \( p = 2m \) for an integer \( m \). Then \( 4m^2 = 2q^2 \), so \( q^2 = 2m^2 \), and \( q^2 \) is even. By @thm-square-even-implies-even again, \( q \) is even \( [\rulename{{\to}E}] \). So \( p \) and \( q \) are both even \( [\rulename{\wedge I}] \), while they were chosen not both even; this is a contradiction \( [\rulename{\neg E}] \). Hence \( r^2 \ne 2 \) \( [\rulename{\neg I}] \).

Since \( r \) was an arbitrary rational number, no rational number has square \( 2 \). This proves the theorem.
:::

::: {.check}
In the proof, which step is \( \rulename{\neg E} \), and which two statements does it cite?
:::

::: {.solution}
The step "this is a contradiction". It cites "\( p \) and \( q \) are both even", derived inside the box of \( r^2 = 2 \) by \( \rulename{\wedge I} \), and "\( p \) and \( q \) are not both even", which (L) supplied when \( p \) and \( q \) were chosen. In the derivation below these are lines 11 and 2, and the step is line 12.
:::

The propositional part of the proof fits in a derivation. Fix \( r \) and the integers \( p \), \( q \) that (L) supplies. Lines 1 and 2 record what (L) says about them; lines 3 and 4 are @thm-square-even-implies-even for \( n = p \) and \( n = q \); the lines marked "algebra" are the computations of the proof.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {r = p/q,\ q \neq 0}
  \hypo {2} {\neg(p \text{ even} \wedge q \text{ even})}
  \hypo {3} {p^2 \text{ even} \to p \text{ even}}
  \hypo {4} {q^2 \text{ even} \to q \text{ even}}
  \open
  \hypo {5} {r^2 = 2}
  \have {6} {p^2 = 2q^2} \by{algebra}{1,5}
  \have {7} {p^2 \text{ even}} \by{def.\ of even}{6}
  \have {8} {p \text{ even}} \ie{3,7}
  \have {9} {q^2 \text{ even}} \by{algebra}{6,8}
  \have {10} {q \text{ even}} \ie{4,9}
  \have {11} {p \text{ even} \wedge q \text{ even}} \ai{8,10}
  \have {12} {\bot} \ne{11,2}
  \close
  \have {13} {\neg(r^2 = 2)} \ni{5-12}
\end{nd}$
\end{center}
```

Line 13 is \( r^2 \ne 2 \). The box \( \lines{5}{12} \) is a \( \rulename{\neg I} \) box as the schema asks: opened by the unnegated statement \( r^2 = 2 \), and ending on \( \bot \) as a line of its own. Three steps of the proof lie outside the derivation: applying @thm-square-even-implies-even, a fact about every integer, to \( p \) and to \( q \); choosing \( p \), \( q \) and \( m \); and passing from the arbitrary \( r \) to every rational number. All three are steps about "some" and "every", used as ordinary reasoning (the note at the start of this chapter).

Notice also what the proof does **not** need: that \( \sqrt{2} \) exists as a real number. The theorem is a statement about rational numbers only.

And notice which rule closes it. "Suppose \( r^2 = 2 \)" opens a box whose **negation** is the goal, so the proof is \( \rulename{\neg I} \), even though it is what everyone calls a proof by contradiction.

## The rule card

Before the card, the rule at work on large statements. Each row is one use of \( \rulename{\neg I} \): the box, and the line it writes.

::: {#exm-negation-and-contradiction-instances}
[Instances of \( \rulename{\neg I} \)]

| \( \varphi \) | The box | New line |
|------------|------------------------|----------------------------|
| \( P \vee \neg Q \) | from \( P \vee \neg Q \) (asm) to \( \bot \) | \( \neg(P \vee \neg Q) \) |
| \( Q \to R \) | from \( Q \to R \) (asm) to \( \bot \) | \( \neg(Q \to R) \) |
| \( \neg(P \wedge R) \) | from \( \neg(P \wedge R) \) (asm) to \( \bot \) | \( \neg\neg(P \wedge R) \) |

**Not an instance.** From the third box, the line "\( P \wedge R \) — \( \rulename{\neg I} \)" is not an instance: \( \rulename{\neg I} \) puts one \( \neg \) in front of the whole assumption and never takes one away. (The rule that writes \( P \wedge R \) from that box is Section 2.5's.)
:::

Chapter 1's seven rules are on the card at the end of Section 1.6; here are this chapter's so far.

| Rule | Shape | You write | Lean |
|---|---|---|---|
| \( \rulename{\neg E} \) | \( \varphi \), \( \neg\varphi \) \( \Longrightarrow \) \( \bot \) | "…, which contradicts …" | `exact hn hp` (goal `False`) |
| \( \rulename{\bot E} \) | \( \bot \) \( \Longrightarrow \) any \( \varphi \) | "This case cannot occur." "So there is nothing to prove." | `exfalso` |
| \( \rulename{\neg I} \) | box \( \varphi \) … \( \bot \) \( \Longrightarrow \) \( \neg\varphi \) | "Suppose \( P \). … This is a contradiction. Hence not \( P \)." | `intro hp` (goal `False`) |

In Lean, the negation of `P` is defined to be `P → False`, with `False` playing the part of \( \bot \): the reading of the remark above. So `intro` performs both \( \rulename{{\to}I} \) and \( \rulename{\neg I} \).

::: {.warning}
[Not allowed: \( \rulename{\neg I} \)]

Each step below is wrong; the tag names the clause of the rule's reading that it breaks.

- Close the box on \( \neg\varphi \) instead of \( \bot \): clause 3, the last line is \( \bot \) (one \( \rulename{\neg E} \) line repairs it; the fold "Edge cases of not-introduction").
- Close it on a \( \bot \) that stands in a box inside it: clause 3, the last line is a line of the box itself.
- Write \( \varphi \) after a box opened by \( \neg\varphi \): clause 4, the new line is the negation of the whole assumption, here \( \neg\neg\varphi \).
- Write the negation of part of the assumption: clause 4, the whole assumption is negated (the pair below).
- Cite a line of the box after it has closed: clause 4, only the negation leaves.

The discharge is where the rule bites, so here is one wrong step beside the right one, with the premise \( \neg(Q \vee R) \). On the left, line 6 negates only \( P \), part of the assumption; on the right, line 6 negates the whole assumption.

```{=latex}
\begin{center}
% expect-invalid: line 6 negates P, but the box 2-5 assumed P and Q, so not-I may write only not(P and Q)
$\begin{nd}
  \hypo {1} {\neg(Q \vee R)}
  \open
  \hypo {2} {P \wedge Q} \purpose{\ni}
  \have {3} {Q} \ae{2}
  \have {4} {Q \vee R} \oi{3}
  \have {5} {\bot} \ne{4,1}
  \close
  \have {6} {\neg P} \ni{2-5}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {\neg(Q \vee R)}
  \open
  \hypo {2} {P \wedge Q}
  \have {3} {Q} \ae{2}
  \have {4} {Q \vee R} \oi{3}
  \have {5} {\bot} \ne{4,1}
  \close
  \have {6} {\neg(P \wedge Q)} \ni{2-5}
\end{nd}$
\end{center}
```

The left list would show \( \neg(Q \vee R) \vdash \neg P \), which breaks. Let \( x \) be a real number, with \( P \): "\( x > 0 \)", \( Q \): "\( x > 5 \)", \( R \): "\( x < -5 \)". At \( x = 1 \) the premise is true and \( \neg P \) is false.
:::

::: {.remark}
[Looking ahead]

*Sets and Functions*, Chapter 2 proves (L) from a fact about the natural numbers called well-ordering. *Analysis on the Real Line*, Chapter 1 uses this section's theorem in exactly the form proved here, as evidence that the rational numbers have a gap where \( \sqrt{2} \) should be.
:::

## Exercises

### A. Check your understanding

::: {#exr-negation-and-contradiction-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Write the schema of \( \rulename{\neg I} \) from memory, and say which statement opens its box.
2. Which rule does this sentence use, and which box does it close? "Suppose \( 0 \) had a reciprocal \( y \). Then \( 1 = 0 \cdot y = 0 \), which is absurd. So \( 0 \) has no reciprocal."
3. In the proof of @thm-sqrt2-irrational, the sentence "\( p \) is even" follows from "\( p^2 \) is even". Which result and which rule justify it?
4. Where in the proof of @thm-sqrt2-irrational is (L) used, and what would go wrong if (L) said only "\( r = p/q \) with \( q \ne 0 \)"?
5. Run the proof of @thm-sqrt2-irrational with \( 4 \) in place of \( 2 \): assume \( r^2 = 4 \) and write \( r = p/q \) as in (L). Which step can no longer be justified? (The conclusion "no rational number has square \( 4 \)" is false, so some step must fail.)
:::
:::

::: {.solution}
(a) The schema is the left one of @def-rules-negation: a box opened by the assumption \( \varphi \), ending on \( \bot \) as a line of the box itself, then \( \neg\varphi \) outside it, citing the box. The box opens with the **unnegated** statement \( \varphi \).

(b) \( \rulename{\neg I} \). The conclusion is the negative statement "\( 0 \) has no reciprocal"; the box opens with "\( 0 \) has a reciprocal \( y \)", and "which is absurd" is its line \( \bot \), reached by \( \rulename{\neg E} \) from \( 1 = 0 \) and the fact \( 1 \ne 0 \).

(c) @thm-square-even-implies-even, for \( n = p \), is the implication "if \( p^2 \) is even, then \( p \) is even"; together with "\( p^2 \) is even" it gives "\( p \) is even" by \( \rulename{{\to}E} \) (line 8 of the derivation, citing lines 3 and 7).

(d) The fact (L) supplies the line "\( p \) and \( q \) are not both even" (line 2 of the derivation), which the \( \rulename{\neg E} \) of line 12 cites. Without that clause the proof still derives "both even", but it contradicts nothing (\( 2 = 4/2 \) has both even), and no \( \bot \) is reached.

(e) With \( r^2 = 4 \) we get \( p^2 = 4q^2 = 2(2q^2) \), so \( p^2 \) is even and \( p \) is even, \( p = 2k \). Then \( 4k^2 = 4q^2 \), so \( q^2 = k^2 \). This is where the proof stalls: nothing says \( q^2 \) is even, so @thm-square-even-implies-even cannot be applied to \( q \). Indeed for \( r = 2 = 2/1 \) we have \( q = 1 \), which is odd. Every step before the stall is correct; the proof simply fails to reach \( \bot \).
:::

::: {#exr-negation-and-contradiction-a2}
[A2: Drill]

The parts run from one step, through a missing line, a justification column and steps to judge, to short derivations.

::: {.enumerate options="label=(\alph*)"}
1. Which statement opens the \( \rulename{\neg I} \) box for the goal \( \neg(P \vee Q) \)?
2. A box opens with \( \neg P \) and ends with \( \bot \). What does \( \rulename{\neg I} \) write after it?
3. For a real number \( x \), the goal is \( x \ne 3 \). Which statement opens the box?
4. A box runs from line 4, \( (P \to Q) \wedge \neg R \), to line 8, \( \bot \), a line of that box itself. What does "\( \rulename{\neg I} \) 4–8" write?
5. Line 10 is \( \neg(Q \vee \neg P) \), justified "\( \rulename{\neg I} \) 6–9". What are lines 6 and 9?
6. Inside a box opened at line 3 by \( P \), line 5 is \( \bot \), justified "\( \rulename{\neg E} \) 4, 2", and line 2 is \( \neg(P \vee R) \). What is line 4?
7. Fill in (i)–(iv), and say what the derivation shows, written with \( \vdash \).

    ```{=latex}
    \begin{center}
    $\begin{nd}
      \hypo {1} {\neg Q}
      \hypo {2} {P \to (Q \wedge R)}
      \open
      \hypo {3} {P} \purpose{\ni}
      \have {4} {Q \wedge R} \by{(i)}{}
      \have {5} {Q} \by{(ii)}{}
      \have {6} {\bot} \by{(iii)}{}
      \close
      \have {7} {\neg P} \by{(iv)}{}
    \end{nd}$
    \end{center}
    ```

8. A box opens with \( P \) and its last line is \( \neg P \). May \( \rulename{\neg I} \) close it?
9. Line 1 is the premise \( \neg Q \); line 2, \( Q \), opens a box; line 3, \( \bot \), justified "\( \rulename{\neg E} \) 2, 1", is the last line of that box. What may line 4, just after the box, be by \( \rulename{\neg I} \)?
10. Find the illegal line, and say why it is illegal.

    ```{=latex}
    \begin{center}
    % expect-invalid: line 7 cites line 3, inside the closed box 3-5
    $\begin{nd}
      \hypo {1} {P \to Q}
      \hypo {2} {\neg Q}
      \open
      \hypo {3} {P}
      \have {4} {Q} \ie{1,3}
      \have {5} {\bot} \ne{4,2}
      \close
      \have {6} {\neg P} \ni{3-5}
      \have {7} {Q} \ie{1,3}
    \end{nd}$
    \end{center}
    ```

11. Lines 3–7 form a box opened by \( P \wedge Q \). Inside it, lines 4–6 form a box opened by \( R \), whose last line, 6, is \( \bot \); line 7 is \( \neg R \), justified "\( \rulename{\neg I} \) 4–6". Is "8. \( \neg(P \wedge Q) \) — \( \rulename{\neg I} \) 3–7" correct?
12. "Suppose \( x^2 + 4 = 2x \) for a real \( x \). Then \( (x - 1)^2 = -3 < 0 \), which contradicts \( (x - 1)^2 \ge 0 \)." What may "Hence" write, and by which rule?
13. Derive \( \neg P \vdash \neg(P \wedge Q) \).
14. Derive \( P \to \neg P \vdash \neg P \).
15. Derive \( P \wedge \neg Q \vdash \neg(P \to Q) \).
:::
:::

::: {.solution}
(a) \( P \vee Q \), the statement the goal negates.

(b) \( \neg\neg P \): one \( \neg \) in front of the whole assumption.

(c) \( x = 3 \), since \( x \ne 3 \) is \( \neg(x = 3) \).

(d) \( \neg((P \to Q) \wedge \neg R) \), the negation of the whole assumption of line 4.

(e) Line 6 is the assumption \( Q \vee \neg P \), which opens the box; line 9 is \( \bot \), the last line of that box.

(f) \( P \vee R \), the unnegated half of line 2; it comes from line 3 by \( \rulename{\vee I} \).

(g) Line 3 is the assumption for \( \rulename{\neg I} \); (i) \( \rulename{{\to}E} \) 2, 3; (ii) \( \rulename{\wedge E} \) 4; (iii) \( \rulename{\neg E} \) 5, 1; (iv) \( \rulename{\neg I} \) \( \lines{3}{6} \). The derivation shows \( \neg Q, \ P \to (Q \wedge R) \vdash \neg P \).

(h) No: the last line must be \( \bot \). First write \( \bot \) by \( \rulename{\neg E} \), citing the assumption and the line \( \neg P \); then \( \rulename{\neg I} \) closes the box.

(i) \( \neg Q \), the negation of the box's assumption; not \( Q \).

(j) Line 7: it cites line 3, which lies inside the box \( \lines{3}{5} \), closed before line 7.

(k) No. The box \( \lines{3}{7} \) ends on \( \neg R \), not on \( \bot \); the \( \bot \) at line 6 is a line of the inner box, not of the box \( \lines{3}{7} \) itself (clause 3). The outer box needs a line \( \bot \) of its own.

(l) \( x^2 + 4 \ne 2x \), by \( \rulename{\neg I} \). The supposition opens the box, and the contradiction is its line \( \bot \); the step to \( (x - 1)^2 = -3 \) is the identity \( x^2 + 4 - 2x = (x - 1)^2 + 3 \).

(m) 2 \( P \wedge Q \), assumption, for \( \rulename{\neg I} \); 3 \( P \), \( \rulename{\wedge E} \) 2; 4 \( \bot \), \( \rulename{\neg E} \) 3, 1; 5 \( \neg(P \wedge Q) \), \( \rulename{\neg I} \) \( \lines{2}{4} \).

(n) 2 \( P \), assumption, for \( \rulename{\neg I} \); 3 \( \neg P \), \( \rulename{{\to}E} \) 1, 2; 4 \( \bot \), \( \rulename{\neg E} \) 2, 3; 5 \( \neg P \), \( \rulename{\neg I} \) \( \lines{2}{4} \).

(o) 2 \( P \to Q \), assumption, for \( \rulename{\neg I} \); 3 \( P \), \( \rulename{\wedge E} \) 1; 4 \( Q \), \( \rulename{{\to}E} \) 2, 3; 5 \( \neg Q \), \( \rulename{\wedge E} \) 1; 6 \( \bot \), \( \rulename{\neg E} \) 4, 5; 7 \( \neg(P \to Q) \), \( \rulename{\neg I} \) \( \lines{2}{6} \).
:::

### B. Practice

::: {#exr-negation-and-contradiction-b1}
[B1: A box inside a box]

A search for \( P \to \neg Q \vdash Q \to \neg P \) has reached the stage below. *Name the move that opens each box, then complete it.*

```{=latex}
% schema (partial derivation: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {P \to \neg Q}
  \have[\ ][0] {} {\vdots}
  \have[][7] {7} {Q \to \neg P} \by{?}{}
\end{nd}$
\end{center}
```
:::

::: {.solution}
The goal is an implication, so the outer box opens on \( Q \), with goal \( \neg P \). That goal is a negation, so the inner box opens on \( P \), with goal \( \bot \). Inside it, the premise fires on \( P \) and gives \( \neg Q \), which clashes with the outer assumption \( Q \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to \neg Q}
  \open
  \hypo {2} {Q}
  \open
  \hypo {3} {P}
  \have {4} {\neg Q} \ie{1,3}
  \have {5} {\bot} \ne{2,4}
  \close
  \have {6} {\neg P} \ni{3-5}
  \close
  \have {7} {Q \to \neg P} \ii{2-6}
\end{nd}$
\end{center}
```

Line 5 may cite line 2 because the box \( \lines{2}{6} \) contains line 5. Both boxes were read off the goal: the outer one by Chapter 1's move for an implication, the inner one by this section's move for a negation. In words: if \( P \) rules out \( Q \), then \( Q \) rules out \( P \).
:::

::: {#exr-negation-and-contradiction-b2}
[B2: A quadratic with no zero]

Let \( x \) be a real number. Prove that \( x^2 - x + 1 \ne 0 \), naming the rules.

*Hint: complete the square.*
:::

::: {.solution}
The goal is \( \neg(x^2 - x + 1 = 0) \), a negation, so we use the rule \( \rulename{\neg I} \). Suppose that \( x^2 - x + 1 = 0 \), as the assumption for \( \rulename{\neg I} \). Completing the square,

\[
x^2 - x + 1 = \left( x - \tfrac12 \right)^2 + \tfrac34 ,
\]

so \( (x - \tfrac12)^2 = -\tfrac34 \), and therefore \( (x - \tfrac12)^2 < 0 \). But the square of a real number is never negative, that is, \( \neg((x - \tfrac12)^2 < 0) \); this is a contradiction \( [\rulename{\neg E}] \). Hence \( x^2 - x + 1 \ne 0 \) \( [\rulename{\neg I}] \).

This is the pattern of @exm-square-plus-one, with the square \( (x - \tfrac12)^2 \) in place of \( x^2 \). The identity can be checked by expanding: \( (x - \tfrac12)^2 = x^2 - x + \tfrac14 \), and \( \tfrac14 + \tfrac34 = 1 \).
:::

::: {#exr-negation-and-contradiction-b3}
[B3: The square root of three, used later]

You may use that every integer can be written as \( 3k \), \( 3k + 1 \) or \( 3k + 2 \) with \( k \) an integer, in one way only, and that every rational number can be written as \( p/q \) with integers \( p \), \( q \), \( q \ne 0 \), and \( p \), \( q \) not both divisible by \( 3 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( n \) is an integer and \( n^2 \) is divisible by \( 3 \), then \( n \) is divisible by \( 3 \).
2. Hence prove that no rational number has square \( 3 \).
:::
:::

::: {.solution}
(a) Suppose \( n^2 \) is divisible by \( 3 \) \( [\text{assumption for } \rulename{{\to}I}] \), so \( n^2 \) has the form \( 3j \) with \( j \) an integer. The integer \( n \) has the form \( 3k \), \( 3k + 1 \) or \( 3k + 2 \), and we argue by cases \( [\rulename{\vee E}] \); a three-way split is two uses of \( \rulename{\vee E} \), one inside a box of the other.

*Case \( n = 3k \).* Then \( n \) is divisible by \( 3 \), as required.

*Cases \( n = 3k + 1 \) and \( n = 3k + 2 \).* Then

\[
\begin{aligned}
(3k + 1)^2 &= 9k^2 + 6k + 1 = 3(3k^2 + 2k) + 1, \\
(3k + 2)^2 &= 9k^2 + 12k + 4 = 3(3k^2 + 4k + 1) + 1 ,
\end{aligned}
\]

so \( n^2 \) has the form \( 3j' + 1 \) as well as the form \( 3j \). An integer has only one of the three forms, so this is a contradiction \( [\rulename{\neg E}] \), and the case cannot occur. By \( \rulename{\bot E} \), \( n \) is divisible by \( 3 \) in this case too.

All cases give that \( n \) is divisible by \( 3 \) \( [\rulename{\vee E}] \), which proves (a) \( [\rulename{{\to}I}] \). The two impossible cases were closed exactly as the odd case in the proof of @thm-square-even-implies-even.

(b) Let \( r \) be a rational number and suppose \( r^2 = 3 \) \( [\text{assumption for } \rulename{\neg I}] \). Write \( r = p/q \) with \( p \), \( q \) not both divisible by \( 3 \). Then \( p^2 = 3q^2 \), so \( 3 \) divides \( p^2 \), and by (a), \( p = 3m \) for an integer \( m \). Then \( 9m^2 = 3q^2 \), so \( q^2 = 3m^2 \), and by (a) again, \( 3 \) divides \( q \). So \( 3 \) divides both \( p \) and \( q \) \( [\rulename{\wedge I}] \); this contradicts their choice \( [\rulename{\neg E}] \). Hence \( r^2 \ne 3 \) \( [\rulename{\neg I}] \). Since \( r \) was an arbitrary rational number, no rational number has square \( 3 \).

The form of (L) matters: the argument ends at "\( 3 \) divides \( p \) and \( q \)", which clashes only with "not both divisible by \( 3 \)". The form "not both even" of the text would give no clash, since \( p = q = 3 \) are both divisible by \( 3 \) and not both even.
:::

::: {#exr-negation-and-contradiction-b4}
[B4: A premise that turns on itself]

Show that \( P \to Q, \ Q \to \neg P \vdash \neg P \). Then say in one sentence what the sequent means.
:::

::: {.solution}
The goal \( \neg P \) is a negation, so assume \( P \). The two premises, used in turn, turn \( P \) into \( \neg P \), and the clash gives \( \bot \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {Q \to \neg P}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {\neg P} \ie{2,4}
  \have {6} {\bot} \ne{3,5}
  \close
  \have {7} {\neg P} \ni{3-6}
\end{nd}$
\end{center}
```

In words: if \( P \) leads to \( Q \), and \( Q \) rules \( P \) out, then \( P \) refutes itself, and so \( P \) fails. Line 5 is the moment of self-refutation: the assumption has produced its own negation. Line 6 is still needed, because the box must end on \( \bot \), not on \( \neg P \).
:::

::: {#exr-negation-and-contradiction-b5}
[B5: From \( \sqrt 2 \) to \( \sqrt p \)]

Let \( p \) be a prime number. You may use two facts.

- (\( \mathrm{L}_p \)) Every rational number can be written as \( a/b \) with integers \( a \), \( b \), \( b \ne 0 \), and \( a \), \( b \) not both divisible by \( p \).
- (\( \mathrm{E}_p \)) For every integer \( n \), if \( p \) divides \( n^2 \), then \( p \) divides \( n \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that no rational number has square \( p \), naming the rule at each logical step.
2. Where does your proof use (\( \mathrm{E}_p \)), and where (\( \mathrm{L}_p \))?
3. Your proof never used that \( p \) is prime, only the two facts. Put \( 6 \) and \( 9 \) in place of \( p \). (\( \mathrm{E}_6 \)) is true (Exercise C1 of Section 2.4 proves it; take it as given here). Does (\( \mathrm{L}_6 \)) follow from (L)? Is (\( \mathrm{E}_9 \)) true? What does the argument then prove about \( \sqrt 6 \), and why does it prove nothing about \( \sqrt 9 \)?
:::
:::

::: {.solution}
(a) Let \( r \) be a rational number, and suppose \( r^2 = p \) \( [\text{assumption for } \rulename{\neg I}] \). By (\( \mathrm{L}_p \)), \( r = a/b \) with \( b \ne 0 \) and \( a \), \( b \) not both divisible by \( p \). Then \( a^2 = r^2 b^2 = p b^2 \), so \( p \) divides \( a^2 \), and by (\( \mathrm{E}_p \)) \( p \) divides \( a \) \( [\rulename{{\to}E}] \); write \( a = pm \). Then \( p^2 m^2 = p b^2 \), so \( b^2 = p m^2 \), \( p \) divides \( b^2 \), and by (\( \mathrm{E}_p \)) again \( p \) divides \( b \) \( [\rulename{{\to}E}] \). So \( p \) divides both \( a \) and \( b \) \( [\rulename{\wedge I}] \), which contradicts their choice \( [\rulename{\neg E}] \). Hence \( r^2 \ne p \) \( [\rulename{\neg I}] \); since \( r \) was arbitrary, no rational number has square \( p \).

(b) (\( \mathrm{E}_p \)) twice, once for \( a \) and once for \( b \), in the places where @thm-sqrt2-irrational used @thm-square-even-implies-even. (\( \mathrm{L}_p \)) when \( a \) and \( b \) are chosen, and again at the clash, which cites "not both divisible by \( p \)".

(c) For \( 6 \): (\( \mathrm{L}_6 \)) follows from (L) of the text, since integers \( a \), \( b \) that are not both even are not both divisible by \( 6 \). With (\( \mathrm{E}_6 \)) as given, the argument proves that \( \sqrt 6 \) is irrational; Exercise C1 of this section does it by another route, with (L) and @thm-square-even-implies-even in place of (\( \mathrm{E}_6 \)). (\( \mathrm{E}_6 \)) itself is not proved here: its proof is Exercise C1 of Section 2.4. For \( 9 \): (\( \mathrm{E}_9 \)) is false, since \( 9 \) divides \( 3^2 \) but not \( 3 \). The proof breaks at its first use of (\( \mathrm{E}_9 \)), as it must, since \( 9 = 3^2 \) and \( 3 = 3/1 \) is rational: with \( r = 3/1 \), \( 9 \) divides \( a^2 = 9 \), but not \( a = 3 \).

**Marking scheme.** (10 points)

- 2: the \( \rulename{\neg I} \) frame, a fixed rational \( r \), and \( a/b \) from (\( \mathrm{L}_p \)).
- 2: \( a^2 = pb^2 \) and the first use of (\( \mathrm{E}_p \)).
- 2: \( b^2 = pm^2 \) and the second use.
- 1: the clash with (\( \mathrm{L}_p \)), \( \rulename{\neg I} \), and the passage from \( r \) to every rational number.
- 1: (b).
- 2: (c), (\( \mathrm{L}_6 \)) from (L) with the conclusion about \( \sqrt 6 \) (1), and \( 9 \) with a witness against (\( \mathrm{E}_9 \)) (1).

Fatal errors (0 for the step): using "\( p \) divides \( n^2 \), so \( p \) divides \( n \)" for \( p = 9 \) or \( p = 4 \); dividing by \( p \) before \( p \) is known to divide \( a \).
:::

::: {#exr-negation-and-contradiction-b6}
[B6: Derive or break]

For each claim, either derive it with the rules of Chapter 1 and Sections 2.1–2.2, or break it by statements about a real number \( x \) that make its counterexample set true at one value of \( x \).

::: {.enumerate options="label=(\alph*)"}
1. \( P \vdash \neg(\neg P \wedge Q) \).
2. \( \neg(P \wedge Q) \vdash \neg P \).
3. \( (P \wedge Q) \to \neg P, \ Q \vdash \neg P \).
4. \( P \to (Q \to R), \ \neg R \vdash \neg(P \wedge Q) \).
5. \( \neg Q \vdash \neg(P \to Q) \).
6. \( P \to Q, \ P \to \neg Q \vdash \neg P \).
7. \( \neg\neg(P \wedge Q) \vdash \neg\neg P \).
8. \( \neg\neg P \vdash \neg\neg(P \wedge Q) \).
:::
:::

::: {.solution}
(a) Derive. The goal is a negation, so the box opens on \( \neg P \wedge Q \), and its first half clashes with the premise.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \open
  \hypo {2} {\neg P \wedge Q}
  \have {3} {\neg P} \ae{2}
  \have {4} {\bot} \ne{1,3}
  \close
  \have {5} {\neg(\neg P \wedge Q)} \ni{2-4}
\end{nd}$
\end{center}
```

(b) Break. Take \( P \): "\( x > 0 \)", \( Q \): "\( x > 5 \)". At \( x = 1 \), \( P \wedge Q \) is false (\( 1 > 5 \) fails), so \( \neg(P \wedge Q) \) is true, and \( P \) is true, so \( \neg\neg P \) is true. The counterexample set \( \neg(P \wedge Q) \), \( \neg\neg P \) (@def-counterexample-set) is true.

(c) Derive. On the assumption \( P \), the premise \( Q \) completes the antecedent, and the assumption produces its own negation.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge Q) \to \neg P}
  \hypo {2} {Q}
  \open
  \hypo {3} {P}
  \have {4} {P \wedge Q} \ai{3,2}
  \have {5} {\neg P} \ie{1,4}
  \have {6} {\bot} \ne{3,5}
  \close
  \have {7} {\neg P} \ni{3-6}
\end{nd}$
\end{center}
```

(d) Derive. Inside the box of \( P \wedge Q \), feed the premise its two hypotheses one at a time; the \( R \) it hands back clashes with \( \neg R \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \to R)}
  \hypo {2} {\neg R}
  \open
  \hypo {3} {P \wedge Q}
  \have {4} {P} \ae{3}
  \have {5} {Q \to R} \ie{1,4}
  \have {6} {Q} \ae{3}
  \have {7} {R} \ie{5,6}
  \have {8} {\bot} \ne{7,2}
  \close
  \have {9} {\neg(P \wedge Q)} \ni{3-8}
\end{nd}$
\end{center}
```

(e) Break. Take \( P \): "\( x > 5 \)", \( Q \): "\( x > 3 \)". The implication \( P \to Q \) holds for every \( x \). At \( x = 0 \), \( \neg Q \) is true, and \( P \to Q \) is true, so \( \neg\neg(P \to Q) \) is true: the counterexample set \( \neg Q \), \( \neg\neg(P \to Q) \) is true.

(f) Derive. On the assumption \( P \), the two premises give \( Q \) and \( \neg Q \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {P \to \neg Q}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {\neg Q} \ie{2,3}
  \have {6} {\bot} \ne{4,5}
  \close
  \have {7} {\neg P} \ni{3-6}
\end{nd}$
\end{center}
```

(g) Derive. The goal \( \neg\neg P \) opens a box on \( \neg P \). The only way to use the premise is to clash with it, so \( \neg(P \wedge Q) \) becomes a subgoal, and a second box proves it, as in @exm-triple-negation.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg\neg(P \wedge Q)}
  \open
  \hypo {2} {\neg P}
  \open
  \hypo {3} {P \wedge Q}
  \have {4} {P} \ae{3}
  \have {5} {\bot} \ne{4,2}
  \close
  \have {6} {\neg(P \wedge Q)} \ni{3-5}
  \have {7} {\bot} \ne{6,1}
  \close
  \have {8} {\neg\neg P} \ni{2-7}
\end{nd}$
\end{center}
```

(h) Break. Take \( P \): "\( x > 0 \)", \( Q \): "\( x > 5 \)". At \( x = 1 \), \( P \) is true, so \( \neg\neg P \) is true; \( P \wedge Q \) is false, so \( \neg(P \wedge Q) \) is true and \( \neg\neg(P \wedge Q) \) is false. The counterexample set \( \neg\neg P \), \( \neg\neg\neg(P \wedge Q) \) is true.

(b) and (h) are the look-alikes, each moving a negation or a conjunct the wrong way: (b) would refute a conjunct from a refuted conjunction, and (h) would add a conjunct under two negations. (g) keeps both negations because \( \rulename{\neg I} \) can only add them, as the warning of this section says. (d) unpacks its nested premise inside the \( \rulename{\neg I} \) box, one \( \rulename{{\to}E} \) per hypothesis, as the two forms of @prp-curry suggest.

**Marking scheme.** (16 points) For each claim: 1 for the verdict; 1 for a derivation every line of which checks, or for a choice of statements and one value of \( x \) at which **every** member of the counterexample set is true. Fatal errors (0 for the claim): a "break" at which some premise is false; a derivation that uses a rule other than those of Chapter 1 and Sections 2.1–2.2.
:::

### C. Going deeper

::: {#exr-negation-and-contradiction-c1}
[C1: The square root of six]

Prove that no rational number has square \( 6 \). Use only the facts (E1)–(E3) of Section 2.1, (L), and @thm-square-even-implies-even, and name the rule at each logical step.
:::

::: {.solution}
[Hint 1]

Follow the proof of @thm-sqrt2-irrational. After writing \( p = 2m \), you will need to show that \( q \) is even from \( 3q^2 = 2m^2 \), where \( q^2 \) is not yet known to be even.
:::

::: {.solution}
[Hint 2]

You will reach \( 3q^2 = 2m^2 \), so \( 3q^2 \) is even. The proof of @thm-square-even-implies-even passed from "\( n^2 \) is even" to "\( n \) is even"; imitate its shape for \( 3q^2 \) and \( q \).
:::

::: {.solution}
Let \( r \) be a rational number and suppose \( r^2 = 6 \) \( [\text{assumption for } \rulename{\neg I}] \). By (L), \( r = p/q \) with integers \( p \), \( q \), \( q \ne 0 \), not both even. Then \( p^2 = 6q^2 = 2(3q^2) \) is even, so \( p \) is even by @thm-square-even-implies-even \( [\rulename{{\to}E}] \); write \( p = 2m \). Then \( 4m^2 = 6q^2 \), that is, \( 3q^2 = 2m^2 \), so \( 3q^2 \) is even.

We show that \( q \) is even. By (E1), \( q \) is even or odd, and we argue by cases \( [\rulename{\vee E}] \). *Case \( q \) even:* this is the goal. *Case \( q \) odd:* then \( q^2 \) is odd by (E3) \( [\rulename{{\to}E}] \), say \( q^2 = 2j + 1 \), and then \( 3q^2 = 6j + 3 = 2(3j + 1) + 1 \) is odd. So \( 3q^2 \) is both even and odd \( [\rulename{\wedge I}] \); this contradicts (E2) \( [\rulename{\neg E}] \), so this case cannot occur, and in it \( q \) is even \( [\rulename{\bot E}] \). In both cases \( q \) is even \( [\rulename{\vee E}] \).

So \( p \) and \( q \) are both even \( [\rulename{\wedge I}] \); this contradicts (L) \( [\rulename{\neg E}] \). Hence \( r^2 \ne 6 \) \( [\rulename{\neg I}] \), and since \( r \) was arbitrary, no rational number has square \( 6 \).

**Marking scheme.** (10 points)
- 2: opens with \( \rulename{\neg I} \): a fixed rational \( r \), the assumption \( r^2 = 6 \), and \( r = p/q \) with \( p \), \( q \) not both even from (L).
- 2: derives \( p \) even from \( p^2 = 2(3q^2) \) by @thm-square-even-implies-even.
- 3: derives \( q \) even from \( 3q^2 = 2m^2 \), either by ruling out the odd case (a correct parity computation and (E2)) or by showing \( q^2 = 2(m^2 - q^2) \) even and applying @thm-square-even-implies-even.
- 2: reaches \( \bot \) by clashing "both even" with (L), and concludes \( r^2 \ne 6 \) by \( \rulename{\neg I} \).
- 1: rules named at the logical steps, and the passage from the arbitrary \( r \) to every rational number.

Fatal errors (0 for the step): applying @thm-square-even-implies-even to \( q \) with only \( 3q^2 \) known to be even; using "if \( 6 \) divides \( n^2 \), then \( 6 \) divides \( n \)" without proof.
:::

::: {#exr-negation-and-contradiction-c2}
[C2: A proof that proves too much]

Here is a "proof" that \( \sqrt{4} \) is irrational, modeled on @thm-sqrt2-irrational.

> Suppose \( r \) is rational and \( r^2 = 4 \). Write \( r = p/q \) with \( p \), \( q \) integers, \( q \ne 0 \), not both divisible by \( 4 \). Then \( p^2 = 4q^2 \), so \( 4 \) divides \( p^2 \). Since \( n^2 \) divisible by \( 4 \) implies \( n \) divisible by \( 4 \), we get \( p = 4m \). Then \( 16m^2 = 4q^2 \), so \( q^2 = 4m^2 \), and as before \( 4 \) divides \( q \). This contradicts the choice of \( p \) and \( q \). Hence no rational number has square \( 4 \).

::: {.enumerate options="label=(\alph*)"}
1. Explain why the conclusion must be false.
2. Find the step that fails, and show that it fails with a specific integer.
3. Every other step is a correct use of a rule. Which rule turns the "contradiction" into the conclusion, and why is the argument still wrong?
:::
:::

::: {.solution}
(a) \( 2 = 2/1 \) is rational and \( 2^2 = 4 \).

(b) The step "\( n^2 \) divisible by \( 4 \) implies \( n \) divisible by \( 4 \)" is a false lemma: for \( n = 2 \), \( n^2 = 4 \) is divisible by \( 4 \), but \( 2 \) is not. It fails exactly on the witness of (a): with \( r = 2/1 \) we have \( p = 2 \), and the lemma would claim that \( 4 \) divides \( 2 \).

(c) The last step is \( \rulename{\neg I} \), applied to the box opened by "\( r^2 = 4 \)". The rule is applied correctly, but the box contains a line that is not justified: the false lemma was used as if it were a premise available everywhere, through \( \rulename{{\to}E} \). A derivation is only as good as its premises. In @thm-sqrt2-irrational the corresponding lemma is @thm-square-even-implies-even, which we proved; here nothing proves the lemma, and nothing could. Compare part (e) of A1, where the honest proof stalls without reaching \( \bot \); here \( \bot \) is "reached" through a false line.
:::

<!-- dependency ledger
def-rules-negation (claim): if the lines above a box hold and the box leads from phi to bot, then phi fails (not-I never leads from true lines to a false one) | argued informally in the text ("Why this rule"); a remark used in no proof
exm-square-plus-one (example): x^2 >= 0 for real x, i.e. not(x^2 < 0); x^2 = -1 gives x^2 < 0 | school algebra (F1.2 blueprint, Allowed prerequisites); AN1.1 (promised)
exm-square-plus-one (solution): derivation line 3 "algebra 2": x^2 + 1 = 0 gives x^2 < 0 | school algebra, inline
thm-sqrt2-irrational (proof): (L) every rational is p/q with q != 0, p and q not both even | school fact stated as (L) in the text, with its informal reason; F2.2 (promised; lem-lowest-terms, by well-ordering)
thm-sqrt2-irrational (proof): p^2 = r^2 q^2; 4m^2 = 2q^2 gives q^2 = 2m^2; "p^2 = 2q^2, so p^2 is even" (definition of even) | school algebra, inline
thm-sqrt2-irrational (proof): applying thm-square-even-implies-even (about every integer n) at n = p and n = q; choosing p, q, m; "r arbitrary, so every rational" | quantifier steps used as school reasoning; F1.4 (promised)
exm-negation-and-contradiction-instances (example): the Not-allowed WRONG/RIGHT pair: at x = 1, x > 5 and x < -5 both fail, so not(Q or R) is true, and x > 0 holds, so not P is false | arithmetic, inline; checked by verify/ch02/exm-negation-and-contradiction-instances.py
exr-negation-and-contradiction-a2 (solution): (l) x^2 + 4 - 2x = (x - 1)^2 + 3 | algebra, inline; checked by verify/ch02/exr-negation-and-contradiction-a2.py
exr-negation-and-contradiction-a1 (solution): y a reciprocal of 0 means 0 * y = 1; 0 * y = 0 | school algebra, AN1.1 (promised)
exr-negation-and-contradiction-a1 (solution): 1 != 0; 2 = 4/2; p^2 = 4q^2 = 2(2q^2), p = 2k gives q^2 = k^2; 2 = 2/1 | arithmetic, inline
exr-negation-and-contradiction-b2 (solution): x^2 - x + 1 = (x - 1/2)^2 + 3/4; a square of a real is never negative | algebra inline; school algebra, AN1.1 (promised)
exr-negation-and-contradiction-b3 (solution): every integer is 3k, 3k+1 or 3k+2 in one way only; the mod-3 form of (L) | stated in the item as usable facts; F2.2 (promised; thm-division-algorithm with n = 3; exr-induction-in-practice-c2, the general form of lem-lowest-terms, for the mod-3 lowest terms)
exr-negation-and-contradiction-b3 (solution): (3k+1)^2 = 3(3k^2+2k)+1, (3k+2)^2 = 3(3k^2+4k+1)+1; 9m^2 = 3q^2 gives q^2 = 3m^2 | algebra, inline
exr-negation-and-contradiction-b5 (solution): (L_p), stated in the item, every rational is a/b with b != 0 and a, b not both divisible by the prime p (lowest terms) | stated in the item as a usable fact; F2.2 (promised; exr-induction-in-practice-c2, the general form of lem-lowest-terms)
exr-negation-and-contradiction-b5 (solution): (E_p), stated in the item, for every integer n, if the prime p divides n^2 then p divides n | stated in the item as a usable fact; F3.5 (promised; cor-prime-divides-product)
exr-negation-and-contradiction-b5 (solution): a^2 = r^2 b^2 = p b^2; a = pm gives p^2 m^2 = p b^2, so b^2 = p m^2 | algebra, inline
exr-negation-and-contradiction-b5 (solution): (L_6) from (L): a, b not both even are not both divisible by 6 | inline (6 = 2 * 3)
exr-negation-and-contradiction-b5 (solution): (E_6) taken as given | stated in the item as a usable fact; proved in Section 2.4, exr-biconditional-and-definitions-c1 (an exercise of this chapter; nothing here rests on it)
exr-negation-and-contradiction-b5 (solution): 9 divides 3^2 = 9 but not 3; 3 = 3/1 | arithmetic; checked by verify/ch02/exr-negation-and-contradiction-b5.py
exr-negation-and-contradiction-b6 (solution): breaks: (b) at x = 1 with x > 0, x > 5; (e) at x = 0 with x > 5, x > 3 (x > 5 implies x > 3 for every real x); (h) at x = 1 with x > 0, x > 5 | arithmetic, inline; school algebra; checked by verify/ch02/exr-negation-and-contradiction-b6.py
exr-negation-and-contradiction-c1 (solution): (E1)-(E3) and (L) | stated in the text (F1.2 §01 and this section)
exr-negation-and-contradiction-c1 (solution): p^2 = 6q^2 = 2(3q^2); 4m^2 = 6q^2 gives 3q^2 = 2m^2; q^2 = 2j+1 gives 3q^2 = 2(3j+1)+1; (marking scheme alternative) q^2 = 3q^2 - 2q^2 = 2(m^2 - q^2) | algebra, inline
exr-negation-and-contradiction-c2 (solution): 2^2 = 4 and 4 does not divide 2 | arithmetic
exr-negation-and-contradiction-c2 (solution): every rational is p/q with p, q not both divisible by 4 (part (c), "every other step") | from (L): not both even implies not both divisible by 4 (inline)
-->
