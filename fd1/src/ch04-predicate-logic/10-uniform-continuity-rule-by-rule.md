# Uniformly Continuous Implies Continuous, Rule by Rule

This chapter opened with a question. Continuity and uniform continuity differ only in where one quantifier stands; why does one imply the other in a few lines, while the converse is false? Section 4.1 gave the informal answer: a variable may depend on the variables quantified to its left, and only on them. @exr-translation-c1 of Section 4.8 asked for both translations into formulas, and Section 4.9 negated uniform continuity (@exm-negating-definitions (c)). This section answers the question with the rules. It derives "uniformly continuous implies continuous" in full, line by line, with the bounded rules of @prp-bounded-quantifier-rules. It then reads off the derivation the one thing this section adds: **which boxes are open where a constant is chosen**, and what that says about what the constant may depend on. The same reading locates the exact lines at which the converse breaks down, and the function \( x^2 \) shows that the converse is not merely unproved but false.

## Two definitions that differ in one place

Let \( A \) be a set of real numbers and \( f \) a function defined on \( A \). We work over the domain \( \nR \), with \( f \) a one-place function symbol, \( \in A \) a one-place predicate symbol (Section 4.2), and \( \abs{\cdot} \) the absolute value. Chapters 15 and 16 define continuity and uniform continuity properly and develop them. Here the two definitions are only **quantifier patterns**, and nothing is used about \( f \) except that \( f(x) \) is a term. (A function symbol has a value at every real number; the values outside \( A \) are never used, because \( f \) is only applied to variables bounded by \( \in A \), as with sequences in Section 4.1.)

\( f \) is **uniformly continuous on \( A \)** (UC) when
\[
\forall \varepsilon > 0 \; \exists \delta > 0 \; \forall x \in A \; \forall y \in A \; \bigl( \abs{x - y} < \delta \to \abs{f(x) - f(y)} < \varepsilon \bigr).
\]
\( f \) is **continuous at every point of \( A \)** (C) when
\[
\forall x \in A \; \forall \varepsilon > 0 \; \exists \delta > 0 \; \forall y \in A \; \bigl( \abs{x - y} < \delta \to \abs{f(x) - f(y)} < \varepsilon \bigr).
\]

The two formulas have the same matrix and the same four bounded quantifiers. Only \( \forall x \in A \) has moved: in C it stands **before** \( \exists \delta > 0 \), in UC **after** it. In the game of Section 4.1, the defender chooses \( \delta \) in C after seeing \( x \) and \( \varepsilon \), and in UC after seeing only \( \varepsilon \). So in UC a single \( \delta \) must serve every point of \( A \) at once: that is what **uniformly** means.

::: {.check}
Swap the first two quantifiers of UC, to get \( \exists \delta > 0 \; \forall \varepsilon > 0 \; \forall x \in A \; \forall y \in A \; ( \abs{x - y} < \delta \to \abs{f(x) - f(y)} < \varepsilon ) \). What does the new formula say about two points of \( A \) closer than \( \delta \)? Does \( f(x) = x \) on \( \nR \) satisfy it?
:::

::: {.solution}
Now \( \delta \) is chosen before \( \varepsilon \), so it must work for every \( \varepsilon > 0 \) at once. For two points \( x, y \in A \) with \( \abs{x - y} < \delta \), this says \( \abs{f(x) - f(y)} < \varepsilon \) for every \( \varepsilon > 0 \), and by @prp-arbitrarily-close-equal, \( f(x) = f(y) \). So the formula says: for some \( \delta > 0 \), any two points of \( A \) closer than \( \delta \) have the **same** value. The function \( f(x) = x \) on \( \nR \) fails it: whatever \( \delta > 0 \) is proposed, the points \( 0 \) and \( \delta/2 \) are closer than \( \delta \) and have different values. Yet \( f(x) = x \) is uniformly continuous, with \( \delta = \varepsilon \). Swapping \( \forall \varepsilon \) and \( \exists \delta \) asks far too much.
:::

## The derivation

::: {#exm-uniform-implies-continuous}
[Uniformly continuous implies continuous]

Derive C from UC, with the bounded rules of @prp-bounded-quantifier-rules.
:::

::: {.idea}
Run the search method of Section 4.8. The goal C begins \( \forall x \in A \), then \( \forall \varepsilon > 0 \): the **goal-directed** steps open two bounded \( \rulename{\forall I} \) boxes, "let \( x_0 \in A \)" and "let \( \varepsilon_0 > 0 \)", and write the last two lines. The new goal begins \( \exists \delta > 0 \), and no witness is in sight, so it is **postponed** (Section 4.5). Turn to the premise UC. It begins \( \forall \varepsilon > 0 \), and the term the goal mentions is \( \varepsilon_0 \), whose bound \( \varepsilon_0 > 0 \) is on a line: \( \rulename{\forall E} \) at \( \varepsilon_0 \) (Section 4.3). That gives an \( \exists \delta > 0 \) line, and its \( \rulename{\exists E} \) box is opened **at once**, with a witness \( \delta_0 \) (Section 4.6), aiming for the postponed goal as its last line. Inside, the premise has become "\( \delta_0 \) works for all \( x, y \in A \)"; instantiate it at the point we have, \( x_0 \). Now the postponed goal has its witness: \( \delta_0 \) itself.

*Before reading on: which lines does the line introducing \( \delta_0 \) rest on, and does any of them mention \( x_0 \)?*
:::

::: {.solution}
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall \varepsilon > 0 \; \exists \delta > 0 \; \forall x \in A \; \forall y \in A \; (\abs{x - y} < \delta \to \abs{f(x) - f(y)} < \varepsilon)}
  \open[x_0]
  \hypo {2} {x_0 \in A}
  \open[\varepsilon_0]
  \hypo {3} {\varepsilon_0 > 0}
  \have {4} {\exists \delta > 0 \; \forall x \in A \; \forall y \in A \; (\abs{x - y} < \delta \to \abs{f(x) - f(y)} < \varepsilon_0)} \Ae{1,3}
  \open[\delta_0]
  \hypo {5} {\delta_0 > 0}
  \hypo {6} {\forall x \in A \; \forall y \in A \; (\abs{x - y} < \delta_0 \to \abs{f(x) - f(y)} < \varepsilon_0)}
  \have {7} {\forall y \in A \; (\abs{x_0 - y} < \delta_0 \to \abs{f(x_0) - f(y)} < \varepsilon_0)} \Ae{6,2}
  \have {8} {\exists \delta > 0 \; \forall y \in A \; (\abs{x_0 - y} < \delta \to \abs{f(x_0) - f(y)} < \varepsilon_0)} \Ei{5,7}
  \close
  \have {9} {\exists \delta > 0 \; \forall y \in A \; (\abs{x_0 - y} < \delta \to \abs{f(x_0) - f(y)} < \varepsilon_0)} \Ee{4,5-8}
  \close
  \have {10} {\forall \varepsilon > 0 \; \exists \delta > 0 \; \forall y \in A \; (\abs{x_0 - y} < \delta \to \abs{f(x_0) - f(y)} < \varepsilon)} \Ai{3-9}
  \close
  \have {11} {\forall x \in A \; \forall \varepsilon > 0 \; \exists \delta > 0 \; \forall y \in A \; (\abs{x - y} < \delta \to \abs{f(x) - f(y)} < \varepsilon)} \Ai{2-10}
\end{nd}$
\end{center}
```

Every line is tagged with its rule; lines 4, 7 and 8 are the one-line bounded rules, and lines 9, 10 and 11 close bounded boxes. The terms and the side conditions:

- Line 4: \( \rulename{\forall E} \) at \( \varepsilon_0 \), with its bound on line 3. The term \( \varepsilon_0 \) is a variable that does not appear in line 1, so it is free for \( \varepsilon \).
- Line 7: \( \rulename{\forall E} \) at \( x_0 \), with its bound on line 2, which is available because the box of line 2 is still open.
- Line 8: \( \rulename{\exists I} \) with the witness \( \delta_0 \), its bound on line 5 and the instance on line 7.
- Line 9 (\( \rulename{\exists E} \), flag \( \delta_0 \)): \( \delta_0 \) does not appear in line 9 (the witness was forgotten at line 8), in line 4, in the premise, or in the assumptions still open at line 9, lines 2 and 3.
- Line 10 (\( \rulename{\forall I} \), flag \( \varepsilon_0 \)): \( \varepsilon_0 \) does not appear in the premise, in line 10, or in the assumption still open at line 10, line 2.
- Line 11 (\( \rulename{\forall I} \), flag \( x_0 \)): \( x_0 \) does not appear in the premise or in line 11, and no assumption is open.

The answer to the prompt: line 5 is the assumption of the \( \rulename{\exists E} \) box, so it rests on line 4, which rests on lines 1 and 3. None of the three mentions \( x_0 \). The witness \( \delta_0 \) was obtained from the premise at \( \varepsilon_0 \) alone, before \( x_0 \) played any part. That is uniformity, read off the lines.
:::

The derivation has 11 lines. Written with the unbounded rules it has 17, since each of its six bounded steps (lines 4, 7, 8, 9, 10 and 11) costs one line more (Section 4.8). The bounded rules keep it at the level at which a mathematician thinks, and the same argument in prose is three sentences, each aligned with the lines it abbreviates:

> Let \( x \in A \) and \( \varepsilon > 0 \) [lines 2, 3, 10, 11]. By uniform continuity there is \( \delta > 0 \) such that \( \abs{u - v} < \delta \) implies \( \abs{f(u) - f(v)} < \varepsilon \) for all \( u, v \in A \); choose such a \( \delta \) [4, 5, 6, 9]. Applied with \( u = x \), this gives \( \abs{f(x) - f(y)} < \varepsilon \) for every \( y \in A \) with \( \abs{x - y} < \delta \), so this \( \delta \) works for \( x \) and \( \varepsilon \) [7, 8].

The prose renames the bound variables of UC to \( u, v \), so that "\( x \)" can name the fixed point; a derivation needs no such care, because \( \rulename{\forall E} \) handles bound variables by substitution. Chapter 5 studies this passage from a derivation to prose, at several levels of detail.

## Reading dependence off the boxes

The derivation shows something the informal proof leaves unsaid: the exact place where \( \delta \) is chosen, and what surrounds it there.

*A constant chosen in a box may depend on the names of the boxes open around that box, and it does depend only on the names in the line it comes from.*

::: {.check}
In the derivation above, which flagged boxes surround the box of \( \delta_0 \), opened at line 5? What may \( \delta_0 \) therefore depend on, and what does it in fact depend on?
:::

::: {.solution}
The boxes of \( x_0 \) (opened at line 2) and of \( \varepsilon_0 \) (opened at line 3). So \( \delta_0 \) may depend on \( x_0 \) and on \( \varepsilon_0 \), as C allows. In fact it depends only on \( \varepsilon_0 \): it comes from line 4, which mentions \( \varepsilon_0 \) and not \( x_0 \).
:::

Why "may"? Inside the boxes of \( x_0 \) and \( \varepsilon_0 \), every term built from \( x_0 \) and \( \varepsilon_0 \) is available, so a premise could have been instantiated at such a term, and a witness obtained from the resulting \( \exists \) line would depend on both names. The side conditions permit that here, because the goal C puts \( \exists \delta \) inside both \( \forall \)'s: the witness is forgotten by \( \rulename{\exists I} \) (line 8) before either box closes. Why "does"? Because everything known about \( \delta_0 \) is what its \( \exists \) line says, and line 4 mentions \( \varepsilon_0 \) alone. So \( \delta_0 \) could have been obtained before \( x_0 \) entered at all: fix \( \varepsilon_0 \), obtain \( \delta_0 \), and only then let \( x_0 \in A \). That is the order of UC itself. A derivation in that order nests the boxes as \( \varepsilon_0 \), \( \delta_0 \), \( x_0 \) (the box of \( \delta_0 \) rests on line 4, so it stays inside the box of \( \varepsilon_0 \)), and it ends in \( \forall \varepsilon > 0 \; \forall x \in A \; \exists \delta > 0 \; \forall y \in A \; (\dots) \), which is C with its first two quantifiers exchanged. C follows by exchanging them back, as in the swap of @exm-universal-introduction-derivations (c), here with the bounded rules: boxes for \( x_1 \in A \) and \( \varepsilon_1 > 0 \), \( \rulename{\forall E} \) at \( \varepsilon_1 \) and then at \( x_1 \), and two \( \rulename{\forall I} \) lines. C's order of choices allows more dependence than this proof uses.

The limit derivation of Section 4.8 showed the same thing on a smaller scale: its witness \( N_0 \) came from a line obtained at \( \varepsilon_0 / 2 \), inside the box of \( \varepsilon_0 \) only, and so it depended on \( \varepsilon_0 \).

## The converse breaks at a side condition

The converse, from C to UC, is the interesting direction. The search for it fails, and the failure has an exact address.

::: {#exm-converse-fails}
[The search from C to UC]

Run the search method on the sequent with premise C and goal UC, and find where it stops.
:::

*Try it first (ten minutes): start the search. Where does a \( \delta \) come from, and at what moment can you get one?*

::: {.idea}
The obvious plan copies the derivation above: fix \( \varepsilon_0 \), obtain \( \delta_0 \) from the premise, choose it as the witness. It runs into an obstacle at the second step. In C, \( \exists \delta \) stands behind \( \forall x \in A \), so to reach it the premise must first be instantiated at a point, and the bounded \( \rulename{\forall E} \) needs a line \( t \in A \). No such line exists until we assume one, in a box for some \( x_0 \). The \( \delta_0 \) obtained inside that box comes from a line that mentions \( x_0 \), and both side conditions then hold it in: it cannot leave its own box while a line about it still mentions it, and \( x_0 \) cannot be generalized while a line about \( \delta_0 \) still mentions \( x_0 \).
:::

::: {.solution}
The goal UC begins \( \forall \varepsilon > 0 \), so open a box for \( \varepsilon_0 \). The new goal \( \exists \delta > 0 \; \forall x \in A \; \forall y \in A \; (\dots) \) is postponed. The premise C begins \( \forall x \in A \), and no line \( t \in A \) is available; the only way to get one is to assume it, so open a bounded box "let \( x_0 \in A \)". Then the premise yields a \( \delta \). Here is how far the search gets, every line legal:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x \in A \; \forall \varepsilon > 0 \; \exists \delta > 0 \; \forall y \in A \; (\abs{x - y} < \delta \to \abs{f(x) - f(y)} < \varepsilon)}
  \open[\varepsilon_0]
  \hypo {2} {\varepsilon_0 > 0}
  \open[x_0]
  \hypo {3} {x_0 \in A}
  \have {4} {\forall \varepsilon > 0 \; \exists \delta > 0 \; \forall y \in A \; (\abs{x_0 - y} < \delta \to \abs{f(x_0) - f(y)} < \varepsilon)} \Ae{1,3}
  \have {5} {\exists \delta > 0 \; \forall y \in A \; (\abs{x_0 - y} < \delta \to \abs{f(x_0) - f(y)} < \varepsilon_0)} \Ae{4,2}
  \open[\delta_0]
  \hypo {6} {\delta_0 > 0}
  \hypo {7} {\forall y \in A \; (\abs{x_0 - y} < \delta_0 \to \abs{f(x_0) - f(y)} < \varepsilon_0)}
  \have {8} {\exists \delta > 0 \; \forall y \in A \; (\abs{x_0 - y} < \delta \to \abs{f(x_0) - f(y)} < \varepsilon_0)} \Ei{6,7}
  \close
  \have {9} {\exists \delta > 0 \; \forall y \in A \; (\abs{x_0 - y} < \delta \to \abs{f(x_0) - f(y)} < \varepsilon_0)} \Ee{5,6-8}
  \close
  \have {10} {\forall x \in A \; \exists \delta > 0 \; \forall y \in A \; (\abs{x - y} < \delta \to \abs{f(x) - f(y)} < \varepsilon_0)} \Ai{3-9}
  \close
  \have {11} {\forall \varepsilon > 0 \; \forall x \in A \; \exists \delta > 0 \; \forall y \in A \; (\abs{x - y} < \delta \to \abs{f(x) - f(y)} < \varepsilon)} \Ai{2-10}
\end{nd}$
\end{center}
```

The goal inside the box of \( \varepsilon_0 \) needs a \( \delta \) that works for **all** points: the line \( \forall x \in A \; \forall y \in A \; (\abs{x - y} < \delta_0 \to \abs{f(x) - f(y)} < \varepsilon_0) \), so that \( \rulename{\exists I} \) at \( \delta_0 \) could finish. Line 7 says this only for the point \( x_0 \). There are two ways to try to generalize it, and each is stopped by a side condition.

- **Generalize inside the box of \( \delta_0 \).** After line 7, open a new flagged box with the name \( x_0 \) and the assumption \( x_0 \in A \), repeat line 7 in it, and close it by \( \rulename{\forall I} \) with the conclusion \( \forall x \in A \; \forall y \in A \; (\abs{x - y} < \delta_0 \to \dots) \). That line breaks the side condition of \( \rulename{\forall I} \): \( x_0 \) appears in assumptions still open there, line 3 and line 7. (With a different name \( x_1 \) the box is legal, but line 7 says nothing about \( x_1 \), so the box cannot reach its last line.)
- **Leave the box of \( \delta_0 \) first, carrying line 7.** Close the \( \rulename{\exists E} \) box with line 7 itself as its conclusion, in order to generalize over \( x_0 \) outside it. That line breaks the side condition of \( \rulename{\exists E} \): its conclusion mentions the witness \( \delta_0 \).

The only legal way out of the box of \( \delta_0 \) is to forget \( \delta_0 \), as line 8 does with \( \rulename{\exists I} \) before line 9 closes the box. Then \( \rulename{\forall I} \) on \( x_0 \) is legal, and line 10 is what it gives: \( \forall x \in A \; \exists \delta > 0 \), with \( \delta \) still behind \( x \). That is C at \( \varepsilon_0 \) again, not UC, and closing the box of \( \varepsilon_0 \) gives line 11, which is C with its first two quantifiers exchanged. The search has gone round in a circle.

These are the same two blocks that stopped the converse of @prp-exists-forall-swap: a \( \rulename{\forall I} \) blocked by an open assumption that mentions its name, and an \( \rulename{\exists E} \) box that cannot close on a line mentioning its witness. That is no coincidence: with the bounds and the matrix stripped away, C to UC is the swap \( \forall x\, \exists \delta \) to \( \exists \delta\, \forall x \).
:::

A failed search proves nothing about all derivations: a cleverer route might exist. For this sequent none does. The evidence is a function for which C is true and UC is false, and Section 4.11 explains why such a function settles the question.

## A function that is continuous and not uniformly continuous

::: {#exm-square-not-uniform}
[The square function on the real line]

Let \( f(x) = x^2 \) on \( A = \nR \). Show that \( f \) satisfies C and does not satisfy UC.
:::

::: {.solution}
*C holds.* Let \( x \in \nR \) and \( \varepsilon > 0 \). Let
\[
\delta \coloneqq \min\Bigl( 1, \, \frac{\varepsilon}{2\abs{x} + 1} \Bigr),
\]
which is positive, since \( \varepsilon > 0 \) and \( 2\abs{x} + 1 \ge 1 > 0 \). It depends on \( \varepsilon \) **and on \( x \)**. Let \( y \in \nR \) with \( \abs{x - y} < \delta \). By the triangle inequality (@exm-triangle-inequality-cases), used twice, and since \( \delta \le 1 \), \( \abs{y} \le \abs{x} + \abs{y - x} < \abs{x} + 1 \), so \( \abs{x + y} \le \abs{x} + \abs{y} < 2\abs{x} + 1 \). Hence
\[
\abs{x^2 - y^2} = \abs{x - y} \cdot \abs{x + y} \le \abs{x - y} \, (2\abs{x} + 1) < \delta \, (2\abs{x} + 1) \le \varepsilon ,
\]
where the strict step uses \( 2\abs{x} + 1 > 0 \), and the last step uses \( \delta \le \varepsilon / (2\abs{x} + 1) \). So this \( \delta \) works for \( x \) and \( \varepsilon \).

*UC fails.* By the negation of uniform continuity in @exm-negating-definitions (c), with the bounds \( x \in \nR \) and \( y \in \nR \) dropped because they always hold, we must show
\[
\exists \varepsilon > 0 \; \forall \delta > 0 \; \exists x \; \exists y \; \bigl( \abs{x - y} < \delta \wedge \abs{x^2 - y^2} \ge \varepsilon \bigr).
\]
Take \( \varepsilon = 1 \). Let \( \delta > 0 \) be arbitrary, and take \( x \coloneqq 1/\delta \) and \( y \coloneqq 1/\delta + \delta/2 \), which depend on \( \delta \). Then \( \abs{x - y} = \delta/2 < \delta \), and, since \( y > x > 0 \) (so \( y - x \) and \( y + x \) are both positive),
\[
\abs{x^2 - y^2} = (y - x)(y + x) = \frac{\delta}{2} \Bigl( \frac{2}{\delta} + \frac{\delta}{2} \Bigr) = 1 + \frac{\delta^2}{4} \ge 1 .
\]
Since \( \delta \) was arbitrary, UC fails.
:::

The \( \delta \) for C grows smaller as \( \abs{x} \) grows, and no single \( \delta \) serves the whole line. The proof of failure says why: however small \( \delta \) is, far enough out (at \( x = 1/\delta \)) the graph is so steep that two points \( \delta/2 \) apart have values more than \( 1 \) apart. The function is the semantic side of @exm-converse-fails. Read in the real numbers, with \( f \) as squaring, the premise C is true and the conclusion UC is false; Section 4.11 calls such a reading a **counter-model**, and explains why a counter-model rules out every derivation, so that no derivation of UC from C exists.

::: {.warning}
**"Depending on \( \varepsilon \)" is a claim, and it can be false.** When a proof says "choose \( \delta \) (depending on \( \varepsilon \))", the parenthesis records which boxes are open where \( \delta \) is chosen, and which names its formula uses. This is the logical origin of the book's rule that every chosen constant says what it depends on: the dependence is a record of the open boxes, and a reader can check it. A proof of uniform continuity must be able to write "depending on \( \varepsilon \)" truthfully. A "proof" that \( x^2 \) is uniformly continuous on \( \nR \) that takes \( \delta = \min(1, \varepsilon/(2\abs{x} + 1)) \) "(depending on \( \varepsilon \))" has a formula for \( \delta \) that mentions \( x \): the \( \delta \) was chosen inside the box of \( x \), so the proof shows only C, and @exm-square-not-uniform shows that UC is false.
:::

## Exercises

### A. Check your understanding

::: {#exr-uniform-continuity-rule-by-rule-a1}
[A1]

These parts are about the derivation of @exm-uniform-implies-continuous.

::: {.enumerate options="label=(\alph*)"}
1. Why is line 7 legal? Name the rule, the term, and the lines it cites, and say why those lines are available.
2. At which line is the premise's "for all \( x \in A \)" used, and at which term?
3. State the idea of the derivation in two sentences.
4. Run the derivation for \( f(x) = 3x + 1 \) on \( A = \nR \), where UC holds with \( \delta = \varepsilon/3 \). For a given \( x_0 \) and \( \varepsilon_0 > 0 \), which \( \delta \) does the derivation hand to C at line 8, and does it depend on \( x_0 \)? Check that it works.
:::
:::

::: {.solution}
*(a)* Line 7 is the bounded \( \rulename{\forall E} \) at the term \( x_0 \). It cites line 6, \( \forall x \in A \; \forall y \in A \; (\dots) \), and line 2, \( x_0 \in A \), the bound's instance. Line 6 is the assumption of the \( \rulename{\exists E} \) box that contains line 7, and line 2 is the assumption of the box of \( x_0 \), which also contains line 7; both boxes are still open at line 7. The term \( x_0 \) is a variable not appearing in line 6, so it is free for \( x \).

*(b)* At line 7, at the term \( x_0 \). Line 6 says that \( \delta_0 \) works for **all** pairs of points of \( A \), and line 7 uses that for pairs with first point \( x_0 \).

*(c)* Uniform continuity at \( \varepsilon \) supplies one \( \delta \) that works for all points at once, and it is supplied before any point is named. Continuity at a point \( x \) then takes that same \( \delta \), specialized to the point \( x \).

*(d)* Line 4 says that some \( \delta > 0 \) works at \( \varepsilon_0 \), and line 8 hands C that witness \( \delta_0 \), whatever it is; the derivation knows only lines 5 and 6 about it. Here \( \varepsilon_0 / 3 \) is such a witness (so is any \( \delta \) with \( 0 < \delta \le \varepsilon_0/3 \)). Reading the derivation with the witness the exercise names, \( \delta_0 = \varepsilon_0 / 3 \), the \( \delta \) handed to C is \( \varepsilon_0 / 3 \). It does not depend on \( x_0 \). It works: for every real \( y \) with \( \abs{x_0 - y} < \varepsilon_0/3 \),
\[
\abs{f(x_0) - f(y)} = \abs{(3x_0 + 1) - (3y + 1)} = 3\abs{x_0 - y} < 3 \cdot \frac{\varepsilon_0}{3} = \varepsilon_0 .
\]
:::

### B. Practice

::: {#exr-uniform-continuity-rule-by-rule-b1}
[B1: Lipschitz implies uniformly continuous]

A function \( f \) is **Lipschitz** on \( A \) when
\[
\exists L \ge 0 \; \forall x \in A \; \forall y \in A \; \bigl( \abs{f(x) - f(y)} \le L \cdot \abs{x - y} \bigr).
\]
Prove that a function that is Lipschitz on \( A \) is uniformly continuous on \( A \), first as a derivation with the bounded rules (lines of arithmetic justified "arith"), then as a short proof in prose. Say what your \( \delta \) depends on. (The bound \( L \ge 0 \) is part of the definition: if \( A \) has at most one point, then \( x = y \) in the matrix, and any \( L \), even \( L = -1 \), would satisfy it. The bound rules this out, so a proof may use \( L \ge 0 \), for instance to divide by \( L + 1 \).)
:::

::: {.solution}
The goal UC begins \( \forall \varepsilon > 0 \): open a box for \( \varepsilon_0 \). The new goal \( \exists \delta > 0 \dots \) is postponed until a witness is in hand. The premise begins \( \exists L \ge 0 \): open its \( \rulename{\exists E} \) box at once, with a witness \( L_0 \), aiming for the postponed goal, which does not mention \( L_0 \). Work backwards from what the boxes for \( x_0 \) and \( y_0 \) will need: from \( \abs{x_0 - y_0} < \delta \) we want \( \abs{f(x_0) - f(y_0)} < \varepsilon_0 \), and the premise gives \( \abs{f(x_0) - f(y_0)} \le L_0 \abs{x_0 - y_0} < L_0 \delta \) when \( L_0 > 0 \). So \( \delta = \varepsilon_0 / L_0 \) is the natural guess, but \( L_0 = 0 \) is allowed and then \( \varepsilon_0/L_0 \) is undefined. Take \( \delta = \varepsilon_0 / (L_0 + 1) \) instead: \( L_0 + 1 \ge 1 > 0 \), and \( L_0 \delta = \varepsilon_0 \cdot L_0/(L_0 + 1) < \varepsilon_0 \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\exists L \ge 0 \; \forall x \in A \; \forall y \in A \; (\abs{f(x) - f(y)} \le L \cdot \abs{x - y})}
  \open[\varepsilon_0]
  \hypo {2} {\varepsilon_0 > 0}
  \open[L_0]
  \hypo {3} {L_0 \ge 0}
  \hypo {4} {\forall x \in A \; \forall y \in A \; (\abs{f(x) - f(y)} \le L_0 \cdot \abs{x - y})}
  \have {5} {\varepsilon_0 / (L_0 \! + \! 1) > 0} \by{arith}{2,3}
  \open[x_0]
  \hypo {6} {x_0 \in A}
  \open[y_0]
  \hypo {7} {y_0 \in A}
  \open
  \hypo {8} {\abs{x_0 - y_0} < \varepsilon_0 / (L_0 \! + \! 1)}
  \have {9} {\forall y \in A \; (\abs{f(x_0) - f(y)} \le L_0 \cdot \abs{x_0 - y})} \Ae{4,6}
  \have {10} {\abs{f(x_0) - f(y_0)} \le L_0 \cdot \abs{x_0 - y_0}} \Ae{9,7}
  \have {11} {\abs{f(x_0) - f(y_0)} < \varepsilon_0} \by{arith}{2,3,8,10}
  \close
  \have {12} {\abs{x_0 - y_0} < \varepsilon_0 / (L_0 \! + \! 1) \to \abs{f(x_0) - f(y_0)} < \varepsilon_0} \ii{8-11}
  \close
  \have {13} {\forall y \in A \; (\abs{x_0 - y} < \varepsilon_0 / (L_0 \! + \! 1) \to \abs{f(x_0) - f(y)} < \varepsilon_0)} \Ai{7-12}
  \close
  \have {14} {\forall x \in A \; \forall y \in A \; (\abs{x - y} < \varepsilon_0 / (L_0 \! + \! 1) \to \abs{f(x) - f(y)} < \varepsilon_0)} \Ai{6-13}
  \have {15} {\exists \delta > 0 \; \forall x \in A \; \forall y \in A \; (\abs{x - y} < \delta \to \abs{f(x) - f(y)} < \varepsilon_0)} \Ei{5,14}
  \close
  \have {16} {\exists \delta > 0 \; \forall x \in A \; \forall y \in A \; (\abs{x - y} < \delta \to \abs{f(x) - f(y)} < \varepsilon_0)} \Ee{1,3-15}
  \close
  \have {17} {\forall \varepsilon > 0 \; \exists \delta > 0 \; \forall x \in A \; \forall y \in A \; (\abs{x - y} < \delta \to \abs{f(x) - f(y)} < \varepsilon)} \Ai{2-16}
\end{nd}$
\end{center}
```

Line 11 is arithmetic from lines 2, 3, 8 and 10: \( \abs{f(x_0) - f(y_0)} \le L_0 \abs{x_0 - y_0} \le L_0 \cdot \varepsilon_0/(L_0 + 1) \), where the second step uses \( L_0 \ge 0 \), and \( L_0/(L_0 + 1) < 1 \) with \( \varepsilon_0 > 0 \) gives \( L_0 \varepsilon_0/(L_0 + 1) < \varepsilon_0 \). Line 15 is the bounded \( \rulename{\exists I} \) at the term \( \varepsilon_0/(L_0 + 1) \), with its bound on line 5. At line 16, \( L_0 \) does not appear in line 16 (the witness term was forgotten at line 15), in line 1, which is the premise, or in the assumption \( \varepsilon_0 > 0 \) still open there. At lines 13, 14 and 17 the flags \( y_0 \), \( x_0 \), \( \varepsilon_0 \) do not appear in the premise, in the line itself, or in the assumptions then open (among lines 2, 3, 4 and 6).

In prose: *Let \( L \ge 0 \) be a constant with \( \abs{f(x) - f(y)} \le L \abs{x - y} \) for all \( x, y \in A \). Let \( \varepsilon > 0 \), and let \( \delta \coloneqq \varepsilon / (L + 1) \), which is positive and depends on \( \varepsilon \) (and on the constant \( L \), which is fixed before \( \varepsilon \)), but not on any point. For \( x, y \in A \) with \( \abs{x - y} < \delta \), \( \abs{f(x) - f(y)} \le L \abs{x - y} \le L\delta = \varepsilon L/(L + 1) < \varepsilon \). So \( f \) is uniformly continuous on \( A \).* The box of \( L_0 \) is open where \( \delta \) is chosen, so \( \delta \) may depend on \( L_0 \). That is harmless: \( L_0 \) is a constant of the function, not a point, and its box could as well have been opened first, outside the box of \( \varepsilon_0 \).
:::

::: {#exr-uniform-continuity-rule-by-rule-b2}
[B2: Put the proof in order]

Below are ten sentences. Eight of them, in a suitable order, form a proof that a function \( f \) uniformly continuous on \( A \) is continuous at every point of \( A \); two are distractors. Write down an order for the eight, and say why each distractor is wrong.

::: {.enumerate options="label=(\roman*)"}
1. Since \( x \) and \( y \) lie in \( A \) and \( \abs{x - y} < \delta \), the choice of \( \delta \), applied to \( u = x \) and \( v = y \), gives \( \abs{f(x) - f(y)} < \varepsilon \).
2. Let \( \delta > 0 \) be arbitrary.
3. Let \( \varepsilon > 0 \).
4. Since \( \varepsilon > 0 \) and \( x \in A \) were arbitrary, \( f \) is continuous at every point of \( A \).
5. Suppose \( f \) is uniformly continuous on \( A \).
6. By uniform continuity, applied to \( \varepsilon \), choose \( \delta > 0 \) such that for all \( u, v \in A \), \( \abs{u - v} < \delta \) implies \( \abs{f(u) - f(v)} < \varepsilon \).
7. Choose \( \delta > 0 \) for this \( x \) and this \( \varepsilon \), and then let \( x \in A \) be arbitrary.
8. Let \( x \in A \).
9. So for every \( y \in A \), \( \abs{x - y} < \delta \) implies \( \abs{f(x) - f(y)} < \varepsilon \): this \( \delta \) works for \( x \) and \( \varepsilon \).
10. Let \( y \in A \) with \( \abs{x - y} < \delta \).
:::
:::

::: {.solution}
An admissible order: (v), (viii), (iii), (vi), (x), (i), (ix), (iv).

(v) is the hypothesis of the implication being proved, so it opens the proof (its \( \rulename{{\to}I} \) box is the outermost one). After it, other orders are admissible as long as each sentence comes after what it uses. (vi) uses the \( \varepsilon \) of (iii); (x) uses the \( \delta \) of (vi) and the \( x \) of (viii); then (i), (ix), (iv) follow in that order. So exactly three orders are admissible: (viii), (iii), (vi); or (iii), (viii), (vi); or (iii), (vi), (viii), each preceded by (v) and followed by (x), (i), (ix), (iv). Only the first matches the derivation of @exm-uniform-implies-continuous directly. The second and the third fix \( \varepsilon \) before \( x \); the third even chooses \( \delta \) before any point is given, which is possible because uniform continuity supplies \( \delta \) from \( \varepsilon \) alone. They correspond to variants of that derivation in which the box of \( \varepsilon_0 \) (in the third, also that of \( \delta_0 \)) is opened outside the box of \( x_0 \). Both variants end in \( \forall \varepsilon > 0 \; \forall x \in A \; \exists \delta > 0 \; \forall y \in A \; (\dots) \), and C follows by exchanging the two bounded universal quantifiers (the swap of @exm-universal-introduction-derivations (c), with the bounded rules); sentence (iv), "since \( \varepsilon \) and \( x \) were arbitrary", covers both steps in prose.

Distractor (ii) introduces \( \delta \) as an arbitrary object, by \( \rulename{\forall I} \). But in "continuous at \( x \)" the \( \delta \) is under \( \exists \): the proof must **produce** it, by a choice from the hypothesis, not receive it from a challenger. A proof that took \( \delta \) arbitrary would have to show that every \( \delta > 0 \) works, which is false in general.

Distractor (vii) chooses \( \delta \) and only afterwards lets \( x \) be arbitrary. It looks legitimate, because when (vii) is read after (viii), \( x \) is already fixed, and continuity at \( x \) does allow \( \delta \) to depend on \( x \). But the sentence reverses the order of the two steps: a \( \delta \) fitted to one particular \( x \) is followed by "let \( x \) be arbitrary", which claims that the same \( \delta \) works for every \( x \). In the rules: if \( \delta \) really was chosen for this \( x \), its \( \rulename{\exists E} \) box assumes a line that mentions \( x \), and generalizing over \( x \) while that assumption is open breaks the side condition of \( \rulename{\forall I} \), the first blocked line of @exm-converse-fails. If \( \delta \) does not depend on \( x \), as here, then "for this \( x \)" is idle and the sentence should be (vi).
:::

::: {#exr-uniform-continuity-rule-by-rule-b3}
[B3: The square root]

Prove that \( f(x) = \sqrt{x} \) is uniformly continuous on \( A = [0, \infty) \). You may use the school inequality \( \abs{\sqrt{x} - \sqrt{y}} \le \sqrt{\abs{x - y}} \) for all \( x, y \ge 0 \). State what your \( \delta \) depends on.
:::

::: {.solution}
Let \( \varepsilon > 0 \), and let \( \delta \coloneqq \varepsilon^2 \), which is positive and depends on \( \varepsilon \) only. Let \( x, y \in [0, \infty) \) with \( \abs{x - y} < \delta \). Then, by the inequality given and because the square root is strictly increasing on \( [0, \infty) \),
\[
\abs{\sqrt{x} - \sqrt{y}} \le \sqrt{\abs{x - y}} < \sqrt{\varepsilon^2} = \varepsilon .
\]
Since \( x \) and \( y \) were arbitrary, this \( \delta \) works for all pairs of points; since \( \varepsilon \) was arbitrary, \( f \) is uniformly continuous on \( [0, \infty) \). The \( \delta \) was chosen before the points: in a derivation of this proof, its \( \rulename{\exists I} \) line would lie inside the box of \( \varepsilon_0 \) only.
:::

### C. Going deeper

::: {#exr-uniform-continuity-rule-by-rule-c1}
[C1: Composition, half done]

Let \( f \) be uniformly continuous on \( A \), with \( f(x) \in B \) for every \( x \in A \), and let \( g \) be uniformly continuous on \( B \). Here is the start of a proof that the composite \( x \mapsto g(f(x)) \) is uniformly continuous on \( A \):

> Fix \( \varepsilon > 0 \). By the uniform continuity of \( g \), choose \( \eta > 0 \) such that \( \abs{u - v} < \eta \) implies \( \abs{g(u) - g(v)} < \varepsilon \) for all \( u, v \in B \).

The rest is blank. *Name the move, then complete it.*
:::

::: {.solution}
[Hint 1]

The goal asks for a \( \delta \). Which hypothesis can produce one, and at which positive number should it be applied?
:::

::: {.solution}
[Hint 2]

"By the uniform continuity of \( f \), applied to \( \eta \), choose \( \delta > 0 \) such that …"
:::

::: {.solution}
*The move* is fix, obtain, choose: \( \varepsilon \) was fixed (\( \rulename{\forall I} \)), \( \eta \) obtained from the hypothesis on \( g \) (\( \rulename{\forall E} \) at \( \varepsilon \), then \( \rulename{\exists E} \)); now obtain \( \delta \) from the hypothesis on \( f \) at the term the goal needs, \( \eta \) (\( \rulename{\forall E} \) at \( \eta \), then \( \rulename{\exists E} \)), and choose that \( \delta \) as the witness (\( \rulename{\exists I} \)).

*Completion.* Since \( \eta > 0 \), the uniform continuity of \( f \), applied to \( \eta \), gives \( \delta > 0 \) such that \( \abs{x - y} < \delta \) implies \( \abs{f(x) - f(y)} < \eta \) for all \( x, y \in A \); choose such a \( \delta \). It depends on \( \eta \), hence on \( \varepsilon \), and on no point. Let \( x, y \in A \) with \( \abs{x - y} < \delta \). Then \( \abs{f(x) - f(y)} < \eta \), and \( f(x), f(y) \in B \), so the choice of \( \eta \), applied to \( u = f(x) \) and \( v = f(y) \), gives \( \abs{g(f(x)) - g(f(y))} < \varepsilon \). Since \( x, y \) were arbitrary, this \( \delta \) works for all pairs of points of \( A \); since \( \varepsilon > 0 \) was arbitrary, \( x \mapsto g(f(x)) \) is uniformly continuous on \( A \).

**Marking scheme.** (10 points)
- 2: names the move (fix, obtain, choose), or the rules \( \rulename{\forall E} \) at \( \eta \), \( \rulename{\exists E} \), \( \rulename{\exists I} \).
- 3: applies the uniform continuity of \( f \) at \( \eta \) (not at \( \varepsilon \)), using \( \eta > 0 \), and chooses \( \delta \) before any point.
- 3: for arbitrary \( x, y \in A \) with \( \abs{x - y} < \delta \), gets \( \abs{f(x) - f(y)} < \eta \) and then \( \abs{g(f(x)) - g(f(y))} < \varepsilon \), using \( f(x), f(y) \in B \).
- 2: concludes with the quantifiers in the order \( \varepsilon \), \( \delta \), points, and says \( \delta \) depends on \( \varepsilon \) only.
Fatal errors (0 for the step): \( \delta \) chosen after \( x \) or depending on \( x \); the uniform continuity of \( g \) applied to points not known to lie in \( B \).
:::

::: {#exr-uniform-continuity-rule-by-rule-c2}
[C2: Gluing two sets]

Let \( A \) and \( B \) be sets of real numbers and \( S \) the set of numbers that lie in \( A \) or in \( B \). Suppose \( f \) is uniformly continuous on \( A \) and uniformly continuous on \( B \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( f \) need not be uniformly continuous on \( S \): take \( A = (0, 1) \), \( B = (1, 2) \), and \( f(x) = 0 \) for \( x < 1 \), \( f(x) = 1 \) for \( x \ge 1 \).
2. Prove that \( f \) is uniformly continuous on \( S \) when \( A = [a, b] \) and \( B = [b, c] \) with \( a < b < c \).
:::
:::

::: {.solution}
[Hint 1]

For (b), the two sets share the point \( b \). Two points on opposite sides of \( b \) are each close to \( b \).
:::

::: {.solution}
[Hint 2]

For (b), apply the two hypotheses at \( \varepsilon/2 \) and take \( \delta = \min(\delta_1, \delta_2) \).
:::

::: {.solution}
*(a)* On \( A = (0, 1) \), \( f \) is constantly \( 0 \), so every \( \delta > 0 \) works for every \( \varepsilon > 0 \): \( \abs{f(x) - f(y)} = 0 < \varepsilon \). The same holds on \( B = (1, 2) \), where \( f \) is constantly \( 1 \). On \( S \) we prove the negation of uniform continuity (@exm-negating-definitions (c)). Take \( \varepsilon = 1 \). Let \( \delta > 0 \), and let \( \eta \coloneqq \min(\delta/4, \tfrac12) \), \( x \coloneqq 1 - \eta \), \( y \coloneqq 1 + \eta \). Then \( \tfrac12 \le x < 1 \), so \( x \in A \subseteq S \); \( 1 < y \le \tfrac32 \), so \( y \in B \subseteq S \); \( \abs{x - y} = 2\eta \le \delta/2 < \delta \); and \( \abs{f(x) - f(y)} = \abs{0 - 1} = 1 \ge \varepsilon \). So \( f \) is not uniformly continuous on \( S \). The gluing fails because the two sets come arbitrarily close at \( 1 \) but have no point in common: points close to \( 1 \) on opposite sides are each controlled only by their own set, and no common point links them.

*(b)* Let \( \varepsilon > 0 \). By the uniform continuity on \( A \) at \( \varepsilon/2 \), choose \( \delta_1 > 0 \) such that \( \abs{f(x) - f(y)} < \varepsilon/2 \) for all \( x, y \in A \) with \( \abs{x - y} < \delta_1 \); likewise choose \( \delta_2 > 0 \) for \( B \). Let \( \delta \coloneqq \min(\delta_1, \delta_2) > 0 \), which depends on \( \varepsilon \) only. Let \( x, y \in S \) with \( \abs{x - y} < \delta \). There are three cases.

- *Case 1: \( x, y \in A \).* Then \( \abs{f(x) - f(y)} < \varepsilon/2 < \varepsilon \), since \( \abs{x - y} < \delta \le \delta_1 \).
- *Case 2: \( x, y \in B \).* The same, with \( \delta_2 \).
- *Case 3: one point in each set*, say \( x \in A \) and \( y \in B \) (the other way round is the same with the letters exchanged). Then \( x \le b \le y \), so \( \abs{x - b} = b - x \le y - x = \abs{x - y} < \delta \le \delta_1 \), and \( b \in A \); hence \( \abs{f(x) - f(b)} < \varepsilon/2 \). Likewise \( \abs{b - y} \le \abs{x - y} < \delta_2 \) and \( b \in B \), so \( \abs{f(b) - f(y)} < \varepsilon/2 \). By the triangle inequality (@exm-triangle-inequality-cases),
\[
\abs{f(x) - f(y)} \le \abs{f(x) - f(b)} + \abs{f(b) - f(y)} < \varepsilon .
\]

Every point of \( S \) lies in \( A \) or in \( B \), so the cases cover all pairs. So \( f \) is uniformly continuous on \( S \). The common point \( b \) is what (a) lacked: there, \( A \) and \( B \) came arbitrarily close at \( 1 \) but had no point in common.

**Marking scheme.** (10 points)
- 3: (a) uniform continuity on \( A \) and on \( B \) checked, and the negation on \( S \) proved: \( \varepsilon \) first, then for arbitrary \( \delta \) two points depending on \( \delta \), with all three conditions checked.
- 2: (b) \( \delta_1 \) for \( A \) at some \( \varepsilon_1 > 0 \) and \( \delta_2 \) for \( B \) at some \( \varepsilon_2 > 0 \) with \( \varepsilon_1 + \varepsilon_2 \le \varepsilon \) (the solution takes \( \varepsilon_1 = \varepsilon_2 = \varepsilon/2 \)), and \( \delta = \min(\delta_1, \delta_2) \), depending on \( \varepsilon \) only.
- 2: the cases with both points in one set.
- 3: the mixed case, through the point \( b \), with \( \abs{x - b}, \abs{b - y} \le \abs{x - y} \) justified and the triangle inequality cited.
Fatal errors (0 for the step): a \( \delta \) depending on \( x \) or \( y \); the mixed case omitted; in (a), points chosen before \( \delta \).
:::

::: {#exr-uniform-continuity-rule-by-rule-c3}
[C3: Exit check: a quantifier derivation]

::: {.enumerate options="label=(\alph*)"}
1. Give a full derivation of
\[
\exists x\, \bigl( P(x) \wedge \forall y\, R(x, y) \bigr) \vdash \forall y\, \exists x\, \bigl( P(x) \wedge R(x, y) \bigr),
\]
and check the side condition of every line that closes a flagged box.
2. For the converse, \( \forall y\, \exists x\, \bigl( P(x) \wedge R(x, y) \bigr) \vdash \exists x\, \bigl( P(x) \wedge \forall y\, R(x, y) \bigr) \), give a domain with two elements and a reading of \( P \) and \( R \) under which the premise is true and the conclusion false, checking both with the informal reading of Section 4.1.
:::
:::

::: {.solution}
*(a)* The goal is a \( \forall \): open a flagged box for \( y_0 \). The premise is an \( \exists \): open its \( \rulename{\exists E} \) box at once, with a witness \( x_0 \), aiming for the goal's instance. Inside, take the conjunction apart, instantiate \( \forall y \) at \( y_0 \), and choose \( x_0 \) as the witness:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\exists x\, (P(x) \wedge \forall y\, R(x, y))}
  \open[y_0]
  \open[x_0]
  \hypo {2} {P(x_0) \wedge \forall y\, R(x_0, y)}
  \have {3} {P(x_0)} \ae{2}
  \have {4} {\forall y\, R(x_0, y)} \ae{2}
  \have {5} {R(x_0, y_0)} \Ae{4}
  \have {6} {P(x_0) \wedge R(x_0, y_0)} \ai{3,5}
  \have {7} {\exists x\, (P(x) \wedge R(x, y_0))} \Ei{6}
  \close
  \have {8} {\exists x\, (P(x) \wedge R(x, y_0))} \Ee{1,2-7}
  \close
  \have {9} {\forall y\, \exists x\, (P(x) \wedge R(x, y))} \Ai{2-8}
\end{nd}$
\end{center}
```

- Line 8 (\( \rulename{\exists E} \), flag \( x_0 \)): \( x_0 \) does not appear in line 8, in line 1 (the premise), or in any assumption still open at line 8 (there is none: the box of \( y_0 \) has no assumption). Line 7, the last line of the box of \( x_0 \), is a line of that box itself and is the formula \( \exists x\, (P(x) \wedge R(x, y_0)) \) that line 8 repeats (@def-rules-existential).
- Line 9 (\( \rulename{\forall I} \), flag \( y_0 \)): \( y_0 \) does not appear in the premise or in line 9, and no assumption is open. Line 8, the last line of the box of \( y_0 \), is the instance at \( y_0 \) of \( \exists x\, (P(x) \wedge R(x, y)) \).

The other nesting, with the box of \( y_0 \) inside the box of \( x_0 \), works too: \( \rulename{\forall I} \) at the end of the inner box (its name \( y_0 \) is in no open assumption, since the assumption on line 2 does not mention it), then \( \rulename{\exists E} \) on a conclusion without \( x_0 \).

*(b)* Take a domain with two elements \( a \), \( b \); let \( P \) be true of both, and let \( R(x, y) \) mean "\( x \) is \( y \)". The premise is true: for \( y = a \) the witness \( x = a \) has \( P(a) \) and \( R(a, a) \), and for \( y = b \) the witness \( x = b \) works. The conclusion is false: \( x = a \) fails \( \forall y\, R(a, y) \) at \( y = b \), and \( x = b \) fails it at \( y = a \). The witness in the premise depends on \( y \); the conclusion asks for one \( x \) that serves every \( y \). (Section 4.11 makes this informal reading a structure, and shows that it proves the converse is not derivable.)

**Marking scheme.** (10 points)
- 2: a flagged box with a fresh name \( y_0 \) for the \( \rulename{\forall I} \), closed correctly.
- 3: an \( \rulename{\exists E} \) box with a fresh witness \( x_0 \), whose conclusion does not contain \( x_0 \), with the side condition checked.
- 2: \( \rulename{\wedge E} \), \( \rulename{\forall E} \) at \( y_0 \) and \( \rulename{\exists I} \) with the witness \( x_0 \), with the correct terms.
- 3: the two-element reading: domain, meaning of \( P \) and \( R \), the premise checked for each \( y \) and the conclusion refuted for each \( x \).
Either nesting of the two boxes earns full marks.
Fatal errors (0 for the step): \( \rulename{\forall I} \) on a name that appears in an open assumption; an \( \rulename{\exists E} \) conclusion containing the witness.
:::

<!-- dependency ledger
exm-uniform-implies-continuous (example): continuity and uniform continuity used only as quantifier patterns; Chapters 15 and 16 own the definitions | prose pointer (Ch 15, Ch 16); nothing rests on it
exm-uniform-implies-continuous (claim): 17 lines with the unbounded rules | inline count: 11 lines + one per bounded step (six), as in prp-bounded-quantifier-rules' line saving
exm-uniform-implies-continuous (claim): a derivation opening the boxes of eps_0 and delta_0 outside the box of x_0 ends in forall eps forall x exists delta (...), and C follows by exchanging the two bounded universals (also used in exr-uniform-continuity-rule-by-rule-b2's solution) | exm-universal-introduction-derivations (c) and the remark after it (Section 4.4, cited), carried out with prp-bounded-quantifier-rules
exm-uniform-implies-continuous (claim): the prose may rename bound variables of UC | renaming of bound variables, Section 4.2 (prose); not used in the derivation
exm-uniform-implies-continuous (solution): the Quick check before it: f(x) = x is uniformly continuous with delta = eps; 0 and delta/2 have different values | arithmetic; prp-arbitrarily-close-equal (cited)
exm-converse-fails (claim): the two attempted lines break the side conditions of forall-I and exists-E | def-rules-universal, def-rules-existential, prp-bounded-quantifier-rules (side conditions as stated in Section 4.8)
exm-converse-fails (claim): the same two blocks stopped the converse of prp-exists-forall-swap | prp-exists-forall-swap (Section 4.6, cited)
exm-converse-fails (claim): no derivation of UC from C exists | Section 4.11 (prose pointer: counter-model and soundness statement); nothing here rests on it
exm-square-not-uniform (solution): |y| <= |x| + |y - x|; |x + y| <= |x| + |y|; |x^2 - y^2| = |x - y| |x + y| | exm-triangle-inequality-cases (cited); |uv| = |u||v| exm-abs-product-cases (Ch 1), school algebra
exm-square-not-uniform (solution): delta = min(1, eps/(2|x| + 1)) > 0 works; x = 1/delta, y = 1/delta + delta/2 give |x^2 - y^2| = (y - x)(y + x) = 1 + delta^2/4, the bars dropped since y > x > 0 | school algebra; |uv| = |u||v| exm-abs-product-cases (Ch 1); checked by verify/ch04/exm-square-not-uniform.py
exm-square-not-uniform (claim): the real structure is a counter-model; Section 4.11 shows non-derivability | Section 4.11 (prose pointer); nothing here rests on it
exr-uniform-continuity-rule-by-rule-a1 (solution): |(3x + 1) - (3y + 1)| = 3|x - y| | school algebra; checked by verify/ch04/exr-uniform-continuity-rule-by-rule-a1.py
exr-uniform-continuity-rule-by-rule-b1 (solution): eps/(L + 1) > 0 for L >= 0, eps > 0; L eps/(L + 1) < eps | arith lines (school algebra); checked by verify/ch04/exr-uniform-continuity-rule-by-rule-b1.py
exr-uniform-continuity-rule-by-rule-b2 (solution): taking every delta > 0 to work is false in general | informal; illustrative
exr-uniform-continuity-rule-by-rule-b3 (solution): |sqrt x - sqrt y| <= sqrt |x - y| for x, y >= 0; sqrt strictly increasing on [0, infinity) | stated in the item (school inequality); school fact; checked by verify/ch04/exr-uniform-continuity-rule-by-rule-b3.py
exr-uniform-continuity-rule-by-rule-c1 (solution): the composite x -> g(f(x)) and the hypothesis f(x) in B for x in A | defined and stated in the item
exr-uniform-continuity-rule-by-rule-c2 (solution): eta = min(delta/4, 1/2); 1/2 <= 1 - eta < 1 < 1 + eta <= 3/2; x <= b <= y gives |x - b|, |b - y| <= |x - y|; triangle inequality | school algebra; exm-triangle-inequality-cases (cited); checked by verify/ch04/exr-uniform-continuity-rule-by-rule-c2.py
exr-uniform-continuity-rule-by-rule-c3 (solution): the two-element reading makes the premise true and the conclusion false | informal truth (Section 4.1); checked by verify/ch04/exr-uniform-continuity-rule-by-rule-c3.py; Section 4.11 (prose pointer) makes it a structure
-->
