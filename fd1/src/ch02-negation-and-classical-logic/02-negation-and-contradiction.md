# Proving a Negation

The rules of Section 2.1 **use** a negation: \( \rulename{\neg E} \) records a clash, and \( \rulename{\bot E} \) turns a clash into any statement we like. Neither rule can **prove** a negation that was not already there. So we still cannot prove that no rational number has square \( 2 \), or even that \( x^2 + 1 \) is never \( 0 \). This section adds the one rule that proves a negation, \( \rulename{\neg I} \), and uses it for one of the oldest proofs in mathematics.

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

Read the schema of \( \rulename{\neg I} \) clause by clause.

1. **Open a box** whose first line is the assumption \( \varphi \). It is the **unnegated** statement: the thing we want to refute, not the thing we want to prove. Any statement may be assumed.
2. **Inside the box** every rule may be used, and every line available just above the box may be cited, as in any box (@def-derivation).
3. **The last line of the box** is exactly \( \bot \), and it is a line of that box itself, not inside a further box opened within it. This is the same wording as for \( \rulename{{\to}I} \), and every box rule shares it; Chapter 3's soundness proof (@thm-soundness) relies on it.
4. **Close the box** and write \( \neg\varphi \) on the next line, outside it. The justification cites the box as a range, "\( \rulename{\neg I} \) \( i \)–\( j \)". The assumption is discharged: after the box closes, nothing inside it may be cited, and only the negation leaves.
5. **The new line is always a negation.** \( \rulename{\neg I} \) never writes a statement whose main connective is not \( \neg \).

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

**Why this rule.** The statement \( \neg\varphi \) says that \( \varphi \) fails, and the box shows what would happen if \( \varphi \) held: together with the lines above it, it would lead to \( \bot \), which never holds. So in any situation where the lines above the box hold, \( \varphi \) cannot hold. That is exactly what \( \neg\varphi \) claims. As for Section 2.1's rules, Chapter 3 turns this into a proof (@thm-soundness).

The rules for \( \neg \) have the same shapes as rules we already know, with \( \bot \) in one slot. Put them beside the rules for \( \to \), applied to the statement \( \varphi \to \bot \):

| To … | a negation \( \neg\varphi \) | an implication \( \varphi \to \bot \) |
|---|---|---|
| prove it | box from \( \varphi \) to \( \bot \), then \( \rulename{\neg I} \) | box from \( \varphi \) to \( \bot \), then \( \rulename{{\to}I} \) |
| use it, given \( \varphi \) | \( \bot \) by \( \rulename{\neg E} \) | \( \bot \) by \( \rulename{{\to}E} \) |

::: {.remark}
Row by row, \( \neg\varphi \) behaves exactly like \( \varphi \to \bot \): "not \( \varphi \)" means "\( \varphi \) leads to contradiction". Some presentations of logic take this as the definition of \( \neg \). This book keeps \( \neg \) as a connective with its own rules, and Chapter 5 returns to the reading \( \neg\varphi \approx \varphi \to \bot \) when it asks what a proof of a negation provides.
:::

::: {.warning}
\( \rulename{\neg I} \) proves **negative** statements only. Its box opens with \( \varphi \) and ends by writing \( \neg\varphi \). A proof that says "suppose \( x \) is **not** positive; …; contradiction; hence \( x \) is positive" has a box opened by \( \neg(x > 0) \), and \( \rulename{\neg I} \) applied to that box gives \( \neg\neg(x > 0) \), not \( x > 0 \). Getting from there to \( x > 0 \) needs a rule we have not met. Section 2.5 is about that rule, and contrasts the two kinds of box in full.
:::

::: {.warning}
Do not open the box with what you want to prove. To prove \( \neg\varphi \), the box opens with \( \varphi \). A box opened by \( \neg\varphi \) and ending in \( \bot \) gives \( \neg\neg\varphi \) by \( \rulename{\neg I} \), the negation of the goal, not the goal. This is the negation's version of the converse error that Section 1.5 found in Argument B.
:::

## First derivations with not-introduction

The goal-directed move of this section: *a goal \( \neg\varphi \) opens a box with \( \varphi \), and the new goal is \( \bot \).* From there, Section 2.1's move takes over: *goal \( \bot \), find a clash*, among the available lines or by manufacturing its missing half.

::: {#exm-double-negation-introduction}
[Two negations from one premise]

Show that (a) \( P \vdash \neg\neg P \), and (b) \( (P \vee Q) \to \neg P \vdash \neg P \).
:::

::: {.idea}
(a) The goal \( \neg\neg P \) is \( \neg(\neg P) \), a negation of \( \neg P \). So the box opens with what is negated, \( \neg P \), and aims at \( \bot \). The clash is immediate: the premise \( P \) and the assumption \( \neg P \). (b) The goal \( \neg P \) opens a box on \( P \). Inside it the premise is an implication, and the premise-directed move feeds it its hypothesis \( P \vee Q \), which \( \rulename{\vee I} \) manufactures from \( P \). The premise then hands back \( \neg P \), and that clashes with the box's own assumption. The assumption is used twice: once to build the hypothesis, once in the clash.
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

::: {.warning}
A box may reach \( \bot \) without ever using its assumption. That is legal, but it is a sign: if no line of the box depends on \( \varphi \), the same lines could have been written just above the box, where \( \bot \) would then stand, and \( \rulename{\bot E} \) would have written \( \neg\varphi \), or anything else, directly. The lines available above the box were already contradictory. When your \( \rulename{\neg I} \) box never uses its assumption, look for the error above the box, not in it.
:::

The first example about numbers is the goal we could not reach at the start of the section.

::: {#exm-square-plus-one}
[A negative statement proved by not-introduction]

Let \( x \) be a real number. Prove that \( x^2 + 1 \ne 0 \), naming the rules.
:::

::: {.idea}
The goal \( x^2 + 1 \ne 0 \) is \( \neg(x^2 + 1 = 0) \), a negation, so open a box on \( x^2 + 1 = 0 \) and look for a clash. The school fact \( x^2 \ge 0 \), that is \( \neg(x^2 < 0) \), is the negation available; its unnegated half \( x^2 < 0 \) is the subgoal, and algebra on the assumption produces it.
:::

::: {.solution}
The goal \( x^2 + 1 \ne 0 \) is \( \neg(x^2 + 1 = 0) \), so we use \( \rulename{\neg I} \). Suppose \( x^2 + 1 = 0 \) \( [\text{assumption for } \rulename{\neg I}] \). Then \( x^2 = -1 \), so \( x^2 < 0 \). But \( x^2 \ge 0 \), that is, \( \neg(x^2 < 0) \), so we have a contradiction \( [\rulename{\neg E}] \). Hence \( x^2 + 1 \ne 0 \) \( [\rulename{\neg I}] \).
:::

## How the rule looks in a mathematical proof

The proof that no rational number has square \( 2 \) has the shape of \( \rulename{\neg I} \): the claim is negative, so we assume its opposite and look for \( \bot \). The tool that finds the clash is @thm-square-even-implies-even, and the school fact it needs is about writing fractions:

**(L)** Every rational number can be written as \( p/q \) with \( p \) and \( q \) integers, \( q \ne 0 \), and \( p \) and \( q \) **not both even**.

This holds because a fraction whose numerator and denominator are both even can be reduced by \( 2 \), and the reduction cannot go on for ever, since the denominator shrinks in absolute value each time. Making "cannot go on for ever" precise needs the well-ordering of the natural numbers, which comes in Chapter 7; here we take (L) as known.

::: {#thm-sqrt2-irrational}
[Irrationality of the Square Root of Two]

There is no rational number whose square is \( 2 \). In other words, \( \sqrt{2} \) is irrational.
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

Line 13 is \( r^2 \ne 2 \). The box \( \lines{5}{12} \) is a \( \rulename{\neg I} \) box as the schema asks: opened by the unnegated statement \( r^2 = 2 \), and ending on \( \bot \) as a line of its own. Two steps of the proof lie outside the derivation: choosing \( p \), \( q \), and \( m \), and passing from the arbitrary \( r \) to every rational number. Both are quantifier rules, which come in Chapter 4.

Notice also what the proof does **not** need: that \( \sqrt{2} \) exists as a real number. The theorem is a statement about rational numbers only. Chapter 11 uses it in exactly this form, as evidence that the rational numbers have a gap where \( \sqrt{2} \) should be.

And notice which rule closes it. "Suppose \( r^2 = 2 \)" opens a box whose **negation** is the goal, so the proof is \( \rulename{\neg I} \), even though it is what everyone calls a proof by contradiction. Section 2.5 meets a second kind of box, which looks the same on the page and is a different rule; the distinction starts from the warning above about \( \neg(x > 0) \).

## What the rule sounds like

Here is the row of the rule, phrase, and Lean table for this section's rule; the rows for \( \rulename{\neg E} \) and \( \rulename{\bot E} \) are in Section 2.1.

| Rule | You write | Lean |
|------|--------------------------------------|------------------------|
| \( \rulename{\neg I} \) | "Suppose \( \varphi \). … This is a contradiction. Hence not \( \varphi \)." | `intro hp` (goal `False`) |

In Lean, the negation of `P` is defined to be `P → False`, with `False` playing the part of \( \bot \): the reading of the remark above. So `intro` performs both \( \rulename{{\to}I} \) and \( \rulename{\neg I} \).

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

(e) With \( r^2 = 4 \) we get \( p^2 = 4q^2 = 2(2q^2) \), so \( p^2 \) is even and \( p \) is even, \( p = 2k \). Then \( 4k^2 = 4q^2 \), so \( q^2 = k^2 \). This is where the proof stalls: nothing says \( q^2 \) is even, so @thm-square-even-implies-even cannot be applied to \( q \). Indeed for \( r = 2 = 2/1 \) we have \( q = 1 \), which is odd. Every step before the stall is valid; the proof simply fails to reach \( \bot \).
:::

### B. Practice

::: {#exr-negation-and-contradiction-b1}
[B1: A box inside a box]

Show that \( P \to \neg Q \vdash Q \to \neg P \). Name the move that opens each box.
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
[B3: The square root of three]

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

### C. Going deeper

::: {#exr-negation-and-contradiction-c1}
[C1: The square root of six]

Prove that no rational number has square \( 6 \). Use only the facts (E1)–(E3) of Section 2.1, (L), and @thm-square-even-implies-even, and name the rule at each logical step.
:::

::: {.solution}
[Hint 1]

Follow the proof of @thm-sqrt2-irrational. After writing \( p = 2m \), you will need to show that \( q \) is even without knowing that \( q^2 \) is even.
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
- 3: derives \( q \) even from \( 3q^2 = 2m^2 \), with the odd case ruled out by a correct parity computation and (E2).
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
def-rules-negation (claim): if the lines above a box hold and the box leads from phi to bot, then phi fails (not-I never leads from true lines to a false one) | ch03 (promised; soundness, thm-soundness), a remark used in no proof
exm-square-plus-one (example): x^2 >= 0 for real x, i.e. not(x^2 < 0); x^2 = -1 gives x^2 < 0 | school algebra (ch02 blueprint, Allowed prerequisites); ch11 (promised)
thm-sqrt2-irrational (proof): (L) every rational is p/q with q != 0, p and q not both even | school fact stated as (L) in the text, with its informal reason; ch07 (promised; lem-lowest-terms, by well-ordering)
thm-sqrt2-irrational (proof): p^2 = r^2 q^2; 4m^2 = 2q^2 gives q^2 = 2m^2; "p^2 = 2q^2, so p^2 is even" (definition of even) | school algebra, inline
thm-sqrt2-irrational (proof): choosing p, q, m; "r arbitrary, so every rational" | quantifier steps used as school reasoning; ch04 (promised)
exr-negation-and-contradiction-a1 (solution): 1 != 0; 2 = 4/2; p^2 = 4q^2 = 2(2q^2), p = 2k gives q^2 = k^2; 2 = 2/1 | arithmetic, inline
exr-negation-and-contradiction-b2 (solution): x^2 - x + 1 = (x - 1/2)^2 + 3/4; a square of a real is never negative | algebra inline; school algebra, ch11 (promised)
exr-negation-and-contradiction-b3 (solution): every integer is 3k, 3k+1 or 3k+2 in one way only; the mod-3 form of (L) | stated in the item as usable facts
exr-negation-and-contradiction-b3 (solution): (3k+1)^2 = 3(3k^2+2k)+1, (3k+2)^2 = 3(3k^2+4k+1)+1; 9m^2 = 3q^2 gives q^2 = 3m^2 | algebra, inline
exr-negation-and-contradiction-c1 (solution): (E1)-(E3) and (L) | stated in the text (Section 2.1 and this section)
exr-negation-and-contradiction-c1 (solution): p^2 = 6q^2 = 2(3q^2); 4m^2 = 6q^2 gives 3q^2 = 2m^2; q^2 = 2j+1 gives 3q^2 = 2(3j+1)+1 | algebra, inline
exr-negation-and-contradiction-c2 (solution): 2^2 = 4 and 4 does not divide 2 | arithmetic
-->
