# Translating Mathematics: Nested and Bounded Quantifiers

The calculus is now complete: Sections 5.3–5.7 gave a rule for using and a rule for proving each quantifier, and the two rules for equality. Before any of those rules can act on a definition from analysis, the definition has to be written as a formula, and written correctly. The definitions of analysis have three or four quantifiers stacked in a fixed order, most of them carrying a bound such as \( \varepsilon > 0 \) or \( n \ge N \), and every bound costs extra lines in a derivation. This section does three things. It translates the standard definitions into formulas, by a procedure that works from the outside in. It turns each quantifier rule into a **bounded** rule that handles the bound in the same step. And it collects the traps that make a translation wrong, each with a reading that shows the wrong formula wrong.

::: {.remark}
[Looking back]

Section 3.3 turned an argument in words into a derivation, with one key for a whole paragraph. This section does the same for definitions with quantifiers. What is new is the order of the quantifiers and the bounds they carry, which the propositional key never had.
:::

## Four pieces in one sentence

"The sequence \( (a_n) \) converges to \( L \)" is written \( a_n \to L \), and a first course defines it in one breath: for every \( \varepsilon > 0 \) there is \( N \in \nN \) such that \( \abs{a_n - L} < \varepsilon \) for all \( n \ge N \). The sentence has three quantifiers, each with a bound (\( \varepsilon > 0 \), \( N \in \nN \), \( n \in \nN \)), and a fourth condition, \( n \ge N \), hidden in "for all \( n \ge N \)", which will turn out to sit under an implication. Each piece has a job, and a slip in any piece changes the meaning:

- drop the bound \( \varepsilon > 0 \), and the challenger may choose \( \varepsilon = -1 \); then \( \abs{a_n - L} < -1 \) is impossible, and **no** sequence converges;
- swap "for every \( \varepsilon \)" and "there is \( N \)", and one \( N \) must serve every \( \varepsilon \); then only sequences that are eventually equal to \( L \) converge;
- read "for all \( n \ge N \)" as "for all \( n \)", and the first terms must already be close to \( L \); then \( 1, \frac12, \frac13, \dots \) converges to nothing.

So translation deserves a procedure, and the rules deserve a form that handles bounds without fuss. We take them in that order.

## Translation from the outside in

*Find the outermost claim, name its quantifier and its bound, then translate what it claims about each object, in the same way.*

The procedure, in three steps:

1. **Fix the domain.** State what the variables range over. A sentence of analysis often mixes kinds of objects: **One domain per formula.** The logic of this book has a single domain for all the variables of a formula. Mathematics often mixes kinds of objects in one sentence: in "for every \( \varepsilon > 0 \) there is an \( N \in \nN \) such that for every \( n \ge N \), …", the letter \( \varepsilon \) is a real number, while \( N \) and \( n \) are natural numbers. The convention is: **the domain is the larger kind** (here \( \nR \)), and **the smaller kind enters as a bound** (\( \exists N \in \nN \), \( \forall n \in \nN \)). So the sentence begins
   \[
   \forall \varepsilon > 0 \; \exists N \in \nN \; \forall n \in \nN \; \bigl( n \ge N \to \dots \bigr),
   \]
   and \( n \) ranges over real numbers that happen to be required, by the bound, to be natural numbers. A sequence \( (a_n) \) becomes a function symbol \( a \), with \( a(n) \), written \( a_n \), the \( n \)-th term. Its values at real numbers that are not natural numbers are never used, because \( a \) is only ever applied to variables bounded by \( n \in \nN \). Section 5.1 stated this convention in two sentences ("Mixing kinds of number"); here it is in full, and every translation in this chapter follows it.
2. **Find the outermost claim.** Ask what the sentence says first, before any detail: "every \( \varepsilon > 0 \) has a property", "there is an \( M \) with a property", "no prime is largest". That gives the outermost quantifier (or connective) and its bound.
3. **Recurse.** Translate the property, which is a sentence about the object just quantified, by the same two steps. Stop at atomic formulas: equations, inequalities, membership, and predicate symbols such as \( \mathrm{Prime}(m) \).

A bound is attached to its own quantifier with the connective of @def-bounded-quantifier: \( \to \) under \( \forall \), \( \wedge \) under \( \exists \). The bounded notation \( \forall \varepsilon > 0 \), \( \exists N \in \nN \) does this automatically, which is why we use it.

**A mixed stage.** Halfway through, a translation is part words and part symbols, and writing that stage down catches most slips. Take "for every positive \( \varepsilon \), some element of \( A \) lies within \( \varepsilon \) of \( s \)". Each line below translates one more quantifier and leaves the rest in words, in square brackets, until no words are left:
\[
\begin{aligned}
&\forall \varepsilon > 0 \; [\text{some element of } A \text{ lies within } \varepsilon \text{ of } s] \\
&\forall \varepsilon > 0 \; \exists x \in A \; [x \text{ lies within } \varepsilon \text{ of } s] \\
&\forall \varepsilon > 0 \; \exists x \in A \; (\abs{x - s} < \varepsilon)
\end{aligned}
\]
Read the last line back, symbol by symbol, into words: if the words are the sentence you began with, the translation is done.

::: {#exm-translate-limit}
[Five definitions, translated]

Translate each sentence into a formula, stating the domain.

::: {.enumerate options="label=(\alph*)"}
1. \( a_n \to L \): for every \( \varepsilon > 0 \) there is \( N \in \nN \) such that \( \abs{a_n - L} < \varepsilon \) for every \( n \ge N \).
2. The set \( A \) of real numbers is bounded above.
3. The function \( f \colon \nR \to \nR \) is continuous at \( a \): for every \( \varepsilon > 0 \) there is \( \delta > 0 \) such that \( \abs{f(x) - f(a)} < \varepsilon \) for every real \( x \) with \( \abs{x - a} < \delta \).
4. There is no largest prime.
5. Every integer greater than \( 1 \) has a prime divisor.
:::
:::

::: {.solution}
*(a)* Domain \( \nR \). The outermost claim is about every \( \varepsilon > 0 \): \( \forall \varepsilon > 0 \). What it says about \( \varepsilon \) is that some natural number \( N \) works: \( \exists N \in \nN \). What it says about \( N \) is that every natural number \( n \) from \( N \) on is good: \( \forall n \in \nN \), with the further condition \( n \ge N \) under an implication. So
\[
\forall \varepsilon > 0 \; \exists N \in \nN \; \forall n \in \nN \; \bigl( n \ge N \to \abs{a_n - L} < \varepsilon \bigr).
\]
The phrase "for every \( n \ge N \)" carries two bounds on \( n \), membership in \( \nN \) and \( n \ge N \); the first is a bounded quantifier, the second the hypothesis of the implication. The free variable is \( L \) (and the statement is also about the function symbol \( a \), which is not a variable).

*(b)* Domain \( \nR \); \( A \) names a set of reals, and \( x \in A \) is a one-place predicate of \( x \) (Section 5.1). "Bounded above" means that some real number is at least every element of \( A \). Outermost claim: there is an \( M \). Its property: every element of \( A \) is at most \( M \):
\[
\exists M \; \forall x \in A \; (x \le M).
\]
The bound \( x \in A \) belongs to the \( \forall \); there is no bound on \( M \), which may be any real number.

*(c)* Domain \( \nR \), with \( f \) a one-place function symbol and \( a \) a variable, free in the formula:
\[
\forall \varepsilon > 0 \; \exists \delta > 0 \; \forall x \; \bigl( \abs{x - a} < \delta \to \abs{f(x) - f(a)} < \varepsilon \bigr).
\]
The last quantifier has no bound of the form "\( x \in \) something", because \( f \) is defined on all of \( \nR \); its restriction \( \abs{x - a} < \delta \) goes under the implication, like \( n \ge N \) in (a). For \( f \) defined on a set \( A \), the last quantifier would be \( \forall x \in A \).

*(d)* Domain \( \nN \), with \( \mathrm{Prime}(m) \) the predicate "\( m \) is prime". Section 5.1 read the sentence as \( \neg\exists m\, \bigl( \mathrm{Prime}(m) \wedge \forall n\, (\mathrm{Prime}(n) \to n \le m) \bigr) \). A mathematician more often states it positively, "for every prime there is a larger prime":
\[
\forall m \; \bigl( \mathrm{Prime}(m) \to \exists n \; (\mathrm{Prime}(n) \wedge m < n) \bigr).
\]
The two forms say the same thing over \( \nN \): the laws of Section 6.2 push the \( \neg \) inside and give \( \forall m\, \bigl( \mathrm{Prime}(m) \to \exists n\, (\mathrm{Prime}(n) \wedge \neg(n \le m)) \bigr) \), and the order fact that \( \neg(n \le m) \) is the same as \( m < n \) finishes the job. (They are not provably equivalent in logic alone: that last step is a fact about the order of \( \nN \), not a law of logic.)

*(e)* Domain \( \nZ \). Outermost claim: every integer greater than \( 1 \) has a property, \( \forall n > 1 \). The property: some \( m \) is prime and divides \( n \). "Divides" is itself a quantifier: \( m \mid n \) means \( n = m \cdot k \) for some integer \( k \). So
\[
\forall n > 1 \; \exists m \; \bigl( \mathrm{Prime}(m) \wedge \exists k \; (n = m \cdot k) \bigr).
\]
Unfolded, the first bound is \( \forall n\, (n > 1 \to \dots) \). The innermost quantifier came from a **defined** word, "divides", which is typical: a definition in words often hides quantifiers, and a translation unfolds them.
:::

Two remarks on the example. First, the order of the quantifiers in (a) and (c) is the order in which the objects are **chosen**: \( \varepsilon \) first, by a challenger; then \( N \) or \( \delta \), by the defender, knowing \( \varepsilon \); then \( n \) or \( x \), by the challenger again, knowing both. That is the game reading of @exm-quantifier-order-sum. Second, in (c) the letter \( a \) is free, so the formula is a statement about \( a \); "\( f \) is continuous at every point" would add \( \forall a \) in front.

::: {.check}
Translate "\( A \) has a maximum" (an element of \( A \) that is at least every element of \( A \)) over \( \nR \). Which quantifier carries the bound \( x \in A \), and does the other quantifier carry a bound too?
:::

::: {.solution}
\( \exists m \in A \; \forall x \in A \; (x \le m) \). The bound \( x \in A \) belongs to the \( \forall \): "every element of \( A \)". The \( \exists \) carries a bound too, \( m \in A \), because a maximum must itself lie in \( A \); dropping it gives \( \exists m\, \forall x \in A\, (x \le m) \), which is "\( A \) is bounded above", a weaker statement. For \( A = (0, 1) \) the weaker statement is true (\( m = 1 \)) and the stronger one is false.
:::

::: {.warning}
**Three mistranslations to avoid.** (1) An \( \exists \) with \( \to \) under it, such as \( \exists x\, (x \in A \to x > 5) \): it is true as soon as something lies outside \( A \) (Section 5.1). (2) A bound on the wrong quantifier: "\( f \) is bounded on \( A \)" is \( \exists M\, \forall x \in A\, (\abs{f(x)} \le M) \); the form \( \exists M \in A\, \forall x\, (\abs{f(x)} \le M) \) asks for a bound that lies in \( A \) and works on all of \( \nR \), and it fails for \( f(x) = x \) on \( A = [0, 1] \), which is bounded on \( A \) by \( 1 \). (3) "For all large \( n \)" read as "for all \( n \)": "\( a_n > 0 \) for all large \( n \)" is \( \exists N \in \nN\; \forall n \in \nN\; (n \ge N \to a_n > 0) \), not \( \forall n \in \nN\, (a_n > 0) \). The sequence \( a_n = n - 3 \) satisfies the first (take \( N = 4 \)) and not the second (\( a_0 = -3 \)).
:::

## Five traps

The warning above caught three slips. Here are five more, each with the reading that shows the wrong formula saying something else.

::: {#exm-translation-traps}
[Five traps, each with a separating reading]

The domain is \( \nR \) unless the row says \( \nN \). \( A \) and \( B \) are sets of reals, and \( x \in A \) is a one-place predicate (Section 5.1).

| | Sentence | Wrong | Right | A reading that separates them |
|---|---|---|---|---|
| (a) | Some natural number lies strictly between \( \tfrac13 \) and \( \tfrac23 \). | \( \exists n\, (\tfrac13 < n \wedge n < \tfrac23) \) | \( \exists n \in \nN\; (\tfrac13 < n \wedge n < \tfrac23) \) | The domain is \( \nR \), by step 1. The sentence is false, since \( 0 < \tfrac13 \) and \( \tfrac23 < 1 \); the wrong formula is true, with \( n = \tfrac12 \). Under one domain, a letter for a natural number ranges over the reals unless its bound \( n \in \nN \) says otherwise. |
| (b) | Every element of \( A \) and of \( B \) is positive. | \( \forall x\, ((x \in A \wedge x \in B) \to x > 0) \) | \( \forall x\, ((x \in A \vee x \in B) \to x > 0) \) | \( A = \{1\} \), \( B = \{-1\} \): the sentence is false (\( -1 \in B \)). The wrong formula speaks only of common elements, and there are none, so it is true. The "and" of the sentence is an "or" in the restriction. |
| (c) | Only even numbers are multiples of \( 4 \). (Over \( \nN \).) | \( \forall n\, (\mathrm{Even}(n) \to 4 \mid n) \) | \( \forall n\, (4 \mid n \to \mathrm{Even}(n)) \) | The right formula is true; the wrong one is false at \( n = 2 \). "Only \( E \) are \( M \)" puts \( E \) after the arrow, as "only if" did in Section 1.1. |
| (d) | If a natural number is divisible by \( 6 \), then it is even. (Over \( \nN \).) | \( \exists n\, (6 \mid n) \to \mathrm{Even}(n) \) | \( \forall n\, (6 \mid n \to \mathrm{Even}(n)) \) | The right formula is true. In the wrong one the last \( n \) is free, and read at \( n = 1 \) it says "if some number is divisible by \( 6 \), then \( 1 \) is even": the hypothesis is true (\( 6 \mid 6 \)) and the conclusion false. "A … it" hides a "for every". |
| (e) | If any element of \( A \) is negative, then \( 0 \) is not a lower bound of \( A \). | \( \forall x \in A\, (x < 0) \to \neg\forall x \in A\, (0 \le x) \) | \( \exists x \in A\, (x < 0) \to \neg\forall x \in A\, (0 \le x) \) | \( A = \emptyset \): the right formula is true, since its hypothesis is false. In the wrong one the hypothesis "every element of \( \emptyset \) is negative" is true and the conclusion "not every element of \( \emptyset \) is at least \( 0 \)" is false (Section 5.1, the empty set). This is Section 5.1's warning on "any", now with the reading that separates the two formulas: the empty set. |
:::

A reading like these is a counter-reading for the step from one formula to the other; it shows that the two say different things, which is all a translation needs to know.

**Infinitely many, and eventually.** "\( a_n > 0 \) for infinitely many \( n \)" says that however far out you start, some later term is positive:
\[
\forall N \in \nN\; \exists n \in \nN\; (n \ge N \wedge a_n > 0).
\]
"Eventually \( a_n > 0 \)", that is, \( a_n > 0 \) for all large \( n \) (warning (3) above), says
\[
\exists N \in \nN\; \forall n \in \nN\; (n \ge N \to a_n > 0).
\]
The quantifiers are swapped, and the bound \( n \ge N \) moves from \( \wedge \) to \( \to \), as the two connectives of @def-bounded-quantifier require. For \( a_n = (-1)^n \) the first is true (every even \( n \ge N \) will do) and the second is false (every odd \( n \ge N \) fails).

::: {.check}
Translate "\( a_n = 0 \) for only finitely many \( n \)".
:::

::: {.solution}
From some index on, no term is \( 0 \): \( \exists N \in \nN\; \forall n \in \nN\; (n \ge N \to a_n \ne 0) \). Finitely many exceptions all lie below some \( N \).
:::

**Translation error or derivation error?** When a derivation ends in a statement you believe false, there are two places to look. A **derivation error** is an illegal line, and checking the derivation line by line finds it. A **translation error** is a formula that does not say what its sentence says, and no line check finds it, because every line may be correct. Suppose a reader translates "some element of \( A \) exceeds \( 5 \)" as \( \exists x\, (x \in A \to x > 5) \), the slip of warning (1) above, and takes \( A = \{1, 2\} \). From the true line \( \neg(7 \in A) \), two steps derive that formula: \( 7 \in A \to 7 > 5 \) by @prp-vacuous-implication, then \( \rulename{\exists I} \) at \( 7 \). Both steps are legal. The conclusion is a true formula about \( A \), and the sentence it was meant to translate is false, since neither \( 1 \) nor \( 2 \) exceeds \( 5 \). The fault is in the translation, not in the derivation. So check a surprising conclusion in two ways: run the line check, and read the formulas back into words.

## Rules for bounded quantifiers

Every analysis formula has bounds, and each bound doubles the work of a rule. To use \( \forall \varepsilon > 0\, \varphi \) at the term \( 1 \), \( \rulename{\forall E} \) gives \( 1 > 0 \to \varphi[1/\varepsilon] \), and a second step, \( \rulename{{\to}E} \) with a line \( 1 > 0 \), gives \( \varphi[1/\varepsilon] \). To prove \( \exists N \in \nN\, \psi \) with the witness \( 7 \), \( \rulename{\wedge I} \) builds \( 7 \in \nN \wedge \psi[7/N] \) and \( \rulename{\exists I} \) finishes. Every step is legal and every step is predictable, and a derivation about limits drowns in them. So we fold each pair into one step.

*A bounded quantifier gets a rule of its own: the bound travels with the quantifier.*

::: {#prp-bounded-quantifier-rules}
[Rules for Bounded Quantifiers]

Let \( A \) be a fixed set, so that \( \in A \) is a one-place predicate symbol (Section 5.2), \( x \) a variable and \( \varphi \) a formula. The following four rules, the **bounded rules**, may be used in derivations, with the rule names of the unbounded rules and the same side conditions: in \( \forall x \in A \; \rulename{E} \) and \( \exists x \in A \; \rulename{I} \), the term \( t \) is free for \( x \) in \( \varphi \); in \( \forall x \in A \; \rulename{I} \), the name \( x_0 \) appears in no premise, in no assumption of a box still open at line \( k \), and not in \( \forall x \in A\; \varphi \); in \( \exists x \in A \; \rulename{E} \), it appears in no premise, in no assumption of a box still open at line \( k \), and not in \( \chi \) or in \( \exists x \in A\; \varphi \). The last line of each box is a line of that box itself.

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {i} {\forall x \in A \; \varphi}
  \have {j} {t \in A}
  \have {k} {\varphi[t/x]} \Ae{i,j}
\end{nd}$
\qquad
% schema
$\begin{nd}[schema]
  \have {i} {t \in A}
  \have {j} {\varphi[t/x]}
  \have {k} {\exists x \in A \; \varphi} \Ei{i,j}
\end{nd}$
\end{center}
```

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \open[x_0]
  \hypo {i} {x_0 \in A}
  \have {} {\vdots}
  \have {j} {\varphi[x_0/x]}
  \close
  \have {k} {\forall x \in A \; \varphi} \Ai{i-j}
\end{nd}$
\qquad
% schema
$\begin{nd}[schema]
  \have {h} {\exists x \in A \; \varphi}
  \open[x_0]
  \hypo {i} {x_0 \in A}
  \hypo {j} {\varphi[x_0/x]}
  \have {} {\vdots}
  \have {l} {\chi}
  \close
  \have {k} {\chi} \Ee{h,i-l}
\end{nd}$
\end{center}
```

Every use of a bounded rule can be replaced by a block of steps of the unbounded rules (Sections 5.3–5.6) and of Chapter 1, with the same premises, the same assumptions open, and the same last line. Hence any derivation that uses the bounded rules converts into one that does not. The same holds with \( x \in A \) and \( t \in A \) replaced by \( x > a \) and \( t > a \), or by the bounds \( \ge a \), \( < a \), \( \le a \), for a term \( a \) in which \( x \) does not occur.
:::

In words: to **use** "every \( x \) in \( A \) has \( \varphi \)", produce an element \( t \) of \( A \) and conclude \( \varphi \) for \( t \). To **prove** "some \( x \) in \( A \) has \( \varphi \)", exhibit an element \( t \) of \( A \) with \( \varphi \). To **prove** "every \( x \) in \( A \) has \( \varphi \)", let \( x_0 \) be an arbitrary element of \( A \) (the box opens with the assumption \( x_0 \in A \)) and prove \( \varphi \) for it. To **use** "some \( x \) in \( A \) has \( \varphi \)", take such an element \( x_0 \), with both facts about it as assumptions, and derive something that does not mention it. These are exactly the sentences a mathematician writes: "let \( \varepsilon > 0 \)", "since \( \delta > 0 \), the hypothesis applies to \( \delta \)", "take \( N = 7 \in \nN \)", "choose \( \delta > 0 \) such that …".

The bounded \( \rulename{\forall I} \) box is the only flagged box with an assumption that closes by \( \rulename{\forall I} \). Its assumption \( x_0 \in A \) mentions the flag, and that is allowed: the side condition asks about assumptions of boxes **still open at line \( k \)**, and the box's own assumption has closed there.

In a finished derivation, the assumption \( x_0 \in A \) of a bounded \( \rulename{\forall I} \) box is printed "asm, for \( \rulename{\forall I} \)", since the box closes by \( \rulename{\forall I} \).

::: {.second-reading title="Why a proposition, not a definition"}
Why is this a proposition and not simply a definition? Because the calculus is fixed: its rules are those of Chapters 1–2 and Sections 5.3–5.7, and a new rule is admissible only if it adds no derivable sequents. @def-derived-rule gave one way to show that: a proved sequent, written with statement letters, may be used as one line. It does not cover these rules. The bounded \( \rulename{\forall E} \) and \( \rulename{\exists I} \) are one line each, but they are schemas in a formula, a variable and a term, not in statement letters; the bounded \( \rulename{\forall I} \) and \( \rulename{\exists E} \) close boxes, which no proved sequent can. So the proposition proves admissibility the direct way: each bounded step is shown to be an abbreviation of a block of unbounded steps. In this sense the bounded rules are derived rules, in a looser sense that extends Chapter 2's: a line citing one abbreviates a block of primitive steps, not a proved sequent.
:::

::: {.idea}
A bounded quantifier is an abbreviation (@def-bounded-quantifier): \( \forall x \in A\; \varphi \) **is** the formula \( \forall x\, (x \in A \to \varphi) \), and \( \exists x \in A\; \varphi \) **is** \( \exists x\, (x \in A \wedge \varphi) \). So each bounded rule should be an unbounded rule on the unfolded formula, plus the connective rule that handles \( \to \) or \( \wedge \). Write the block, then check two things: the block is a correct piece of derivation wherever the bounded step was, and its side conditions hold exactly when the bounded ones do.
:::

::: {.warning}
[Not allowed: the bounded rules]

Each step below is wrong; the tag names the condition of @prp-bounded-quantifier-rules that it breaks.

- From \( \forall \varepsilon > 0\; \varphi \) alone, write \( \varphi[1/\varepsilon] \): the bounded \( \rulename{\forall E} \) cites two lines, and the line \( 1 > 0 \) is missing.
- From \( \abs{a_7 - L} < 1 \) alone, write \( \exists N \in \nN\; (\abs{a_N - L} < 1) \): the bounded \( \rulename{\exists I} \) needs the line \( 7 \in \nN \) too.
- Close a bounded \( \rulename{\forall I} \) box on \( \varepsilon_0 \) while the assumption \( \delta_0 < \varepsilon_0 \) of an enclosing box is still open: the flag appears in an assumption of a box still open.
- Close a bounded \( \rulename{\exists E} \) box on \( N_0 \) with the last line \( N_0 + 1 \in \nN \): the conclusion \( \chi \) mentions the witness.
:::

The proof writes out, for each bounded rule, the block of unbounded steps it abbreviates, and checks that the side conditions match; it is in the fold below.

:::: {.second-reading title="The proof: each bounded rule as a block of unbounded steps"}
::: {.proof}
We give the replacement block for each rule and check it. In each block, the lines of the bounded version keep their labels, and new lines get new letters.

*Bounded \( \rulename{\forall E} \).* Line \( i \) is \( \forall x\, (x \in A \to \varphi) \). Replace line \( k \) by two lines:

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {i} {\forall x\, (x \in A \to \varphi)}
  \have {j} {t \in A}
  \have {m} {t \in A \to \varphi[t/x]} \Ae{i}
  \have {k} {\varphi[t/x]} \ie{m,j}
\end{nd}$
\end{center}
```

Line \( m \) is \( \rulename{\forall E} \) at \( t \): the formula \( (x \in A \to \varphi)[t/x] \) is \( t \in A \to \varphi[t/x] \) by @def-substitution, since \( A \) is not a variable. Its side condition asks that \( t \) be free for \( x \) in \( x \in A \to \varphi \) (@def-free-for), which holds exactly when \( t \) is free for \( x \) in \( \varphi \), since \( x \in A \) has no quantifier. Lines \( i \) and \( j \) are available at \( m \) and \( k \) because they were available at \( k \).

*Bounded \( \rulename{\exists I} \).* Replace line \( k \) by:

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {i} {t \in A}
  \have {j} {\varphi[t/x]}
  \have {m} {t \in A \wedge \varphi[t/x]} \ai{i,j}
  \have {k} {\exists x\, (x \in A \wedge \varphi)} \Ei{m}
\end{nd}$
\end{center}
```

Line \( m \) is the instance at \( t \) of \( x \in A \wedge \varphi \), and \( t \) is free for \( x \) there exactly when it is free for \( x \) in \( \varphi \).

*Bounded \( \rulename{\forall I} \).* Replace the box and line \( k \) by a flagged box with no assumption, which contains a \( \rulename{{\to}I} \) box holding the old lines:

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \open[x_0]
  \open
  \hypo {i} {x_0 \in A}
  \have {} {\vdots}
  \have {j} {\varphi[x_0/x]}
  \close
  \have {m} {x_0 \in A \to \varphi[x_0/x]} \ii{i-j}
  \close
  \have {k} {\forall x\, (x \in A \to \varphi)} \Ai{i-m}
\end{nd}$
\end{center}
```

The lines between \( i \) and \( j \) are unchanged. Each of them lies inside both new boxes, so every line it cited is still available (@def-derivation, with the flagged boxes of Section 5.4): a line outside the old box is outside both new ones, and a line inside the old box is inside the new \( \rulename{{\to}I} \) box. The side conditions inside the old box are unaffected too: a line inside it has the same open assumptions as before, \( x_0 \in A \) (now the assumption of the \( \rulename{{\to}I} \) box) together with the outer ones, because the flagged box adds none; so every flagged box that closes inside the old box still meets its side condition. Line \( m \) is \( \rulename{{\to}I} \), and it is the last line of the flagged box, as \( \rulename{\forall I} \) requires; it is the instance at \( x_0 \) of \( x \in A \to \varphi \). Now the side condition of \( \rulename{\forall I} \) at line \( k \): the premises are the same as before; the boxes still open at line \( k \) are the same as those open at line \( k \) in the bounded version, because the \( \rulename{{\to}I} \) box on \( x_0 \in A \) has **closed** before line \( k \); and the conclusion is the same formula. So the unbounded side condition holds exactly when the bounded one does.

*Bounded \( \rulename{\exists E} \).* Line \( h \) is \( \exists x\, (x \in A \wedge \varphi) \). Replace the box's two assumptions by one assumption and two lines of \( \rulename{\wedge E} \):

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {h} {\exists x\, (x \in A \wedge \varphi)}
  \open[x_0]
  \hypo {g} {x_0 \in A \wedge \varphi[x_0/x]}
  \have {i} {x_0 \in A} \ae{g}
  \have {j} {\varphi[x_0/x]} \ae{g}
  \have {} {\vdots}
  \have {l} {\chi}
  \close
  \have {k} {\chi} \Ee{h,g-l}
\end{nd}$
\end{center}
```

Lines \( i \) and \( j \) now hold the same formulas as the old assumptions, inside the same box, so every line that cited them may still cite them. At a line inside the box, the open assumptions are now \( g \) together with the outer ones, where before they were \( x_0 \in A \) and \( \varphi[x_0/x] \) together with the outer ones. A name appears in \( g \) exactly when it appears in \( x_0 \in A \) or in \( \varphi[x_0/x] \), so every flagged box that closes inside the box still meets its side condition. The box assumes the instance at \( x_0 \) of \( x \in A \wedge \varphi \), as \( \rulename{\exists E} \) requires. Its side condition at line \( k \) names \( \chi \), the formula \( \exists x\, (x \in A \wedge \varphi) \), the premises and the assumptions open at line \( k \): the same four things as the bounded side condition, with the same result.

For the bounds \( x > a \) and the others, the same four blocks work with \( x > a \) and \( t > a \) in place of \( x \in A \) and \( t \in A \). One point needs the hypothesis that \( x \) does not occur in \( a \): then \( (x > a)[t/x] \) is \( t > a \), and the bound contains no bound variable, so free-for conditions are unaffected by it.

Replacing the bounded steps one at a time, each by its block, removes them all; the premises and the last line do not change. This proves the proposition.
:::
::::

Each block is one line longer than the bounded step it replaces: two lines for one in \( \rulename{\forall E} \) and \( \rulename{\exists I} \); the extra \( \rulename{{\to}I} \) line in \( \rulename{\forall I} \); three lines (an assumption and two \( \rulename{\wedge E} \)) for two assumptions in \( \rulename{\exists E} \). So **each bounded step saves exactly one line**, and a derivation with many bounds saves many. More than the count, the bounded rules keep the derivation at the level at which a mathematician thinks: "let \( \varepsilon > 0 \)" is one step, not two.

::: {.check}
Unfolded, \( \exists N \in \nN\; \psi \) is \( \exists N\, (N \in \nN \wedge \psi) \). A student uses the bounded \( \rulename{\exists E} \) on it and writes the box with the single assumption \( N_0 \in \nN \wedge \psi[N_0/N] \). Is that wrong?
:::

::: {.solution}
No, it is the unbounded \( \rulename{\exists E} \), which is always available, since the bounded formula **is** the unfolded one. It costs two \( \rulename{\wedge E} \) lines inside the box to separate \( N_0 \in \nN \) from \( \psi[N_0/N] \). The bounded rule opens the box with the two assumptions already separated. Both are correct; the bounded one is shorter by one line.
:::

## A limit derivation with bounds

Here is the first derivation in the book about a limit. The claim is the school fact "if \( a_n \to L \), then \( 2a_n \to 2L \)", with the definition of @exm-translate-limit (a).

**Claim.** Over \( \nR \),
\[
\forall \varepsilon > 0 \; \exists N \in \nN \; \forall n \in \nN \; \bigl( n \ge N \to \abs{a_n - L} < \varepsilon \bigr)
\]
derives the same formula with \( 2 \cdot a_n \) and \( 2 \cdot L \) in place of \( a_n \) and \( L \), using two lines of arithmetic, justified "arith": \( \varepsilon_0 > 0 \) gives \( \varepsilon_0 / 2 > 0 \), and \( \abs{a_{n_0} - L} < \varepsilon_0 / 2 \) gives \( \abs{2 \cdot a_{n_0} - 2 \cdot L} < \varepsilon_0 \) (because \( \abs{2 u - 2 v} = 2 \abs{u - v} \)).

::: {.idea}
Run the search. The goal starts with \( \forall \varepsilon > 0 \): open a bounded \( \rulename{\forall I} \) box, "let \( \varepsilon_0 > 0 \)". The new goal starts with \( \exists N \in \nN \): **postpone** it (the step of Section 5.5), since no witness is in sight. Turn to the premise: it starts with \( \forall \varepsilon > 0 \), and the step of Section 5.3 says to instantiate it at the term the goal needs. Which term? The goal will need \( \abs{2 a_n - 2 L} < \varepsilon_0 \), which follows from \( \abs{a_n - L} < \varepsilon_0 / 2 \): so instantiate at \( \varepsilon_0 / 2 \), after an "arith" line \( \varepsilon_0 / 2 > 0 \) for the bound. That gives an \( \exists N \in \nN \) line: open its \( \rulename{\exists E} \) box **at once**, with a witness \( N_0 \) (the step of Section 5.6), and let the box's last line be the current goal. Now the postponed goal has its witness: \( N_0 \) itself. The remaining goal \( \forall n \in \nN\, (\dots) \) opens a bounded \( \rulename{\forall I} \) box for \( n_0 \), and a \( \rulename{{\to}I} \) box on \( n_0 \ge N_0 \) finishes with one \( \rulename{\forall E} \), one \( \rulename{{\to}E} \), and the second "arith" line. This is the pattern of @prp-exists-forall-swap: **fix** \( \varepsilon_0 \), **obtain** \( N_0 \), **choose** \( N_0 \) as the witness.
:::

Two abbreviations show the shape. Write \( G(N, \varepsilon) \) for \( \forall n \in \nN\; (n \ge N \to \abs{a_n - L} < \varepsilon) \), "from \( N \) on, every term is within \( \varepsilon \) of \( L \)", and \( G_2(N, \varepsilon) \) for the same formula with \( 2 \cdot a_n \) and \( 2 \cdot L \). The premise is \( \forall \varepsilon > 0\; \exists N \in \nN\; G(N, \varepsilon) \), and the goal is the same with \( G_2 \). With the lines that look inside \( G \) left as a gap, the derivation is:

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {\forall \varepsilon > 0 \; \exists N \in \nN \; G(N, \varepsilon)}
  \open[\varepsilon_0]
  \hypo {2} {\varepsilon_0 > 0}
  \have {3} {\varepsilon_0 / 2 > 0} \by{arith}{2}
  \have {4} {\exists N \in \nN \; G(N, \varepsilon_0 / 2)} \Ae{1,3}
  \open[N_0]
  \hypo {5} {N_0 \in \nN}
  \hypo {6} {G(N_0, \varepsilon_0 / 2)}
  \have[\ ][0] {} {\vdots}
  \have[][13] {13} {G_2(N_0, \varepsilon_0)}
  \have {14} {\exists N \in \nN \; G_2(N, \varepsilon_0)} \Ei{5,13}
  \close
  \have {15} {\exists N \in \nN \; G_2(N, \varepsilon_0)} \Ee{4,5-14}
  \close
  \have {16} {\forall \varepsilon > 0 \; \exists N \in \nN \; G_2(N, \varepsilon)} \Ai{2-15}
\end{nd}$
\end{center}
```

Lines 7–12 are the only lines that look inside \( G \) and \( G_2 \): they unfold \( G(N_0, \varepsilon_0/2) \) at a fresh \( n_0 \) and prove the instance that line 13 folds back into \( G_2(N_0, \varepsilon_0) \). Here is the derivation in full; its lines 1–6 and 13–16 are the lines above, written out.

::: {.check}
In the outline, line 4 instantiates the premise at \( \varepsilon_0/2 \). Why that term, and not \( \varepsilon_0 \)?
:::

::: {.solution}
The goal needs \( \abs{2a_n - 2L} < \varepsilon_0 \), which is \( 2\abs{a_n - L} < \varepsilon_0 \), so it is enough to have \( \abs{a_n - L} < \varepsilon_0/2 \). The term is read off the goal (Section 5.3's step), not off the premise.
:::

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall \varepsilon > 0 \; \exists N \in \nN \; \forall n \in \nN \; (n \ge N \to \abs{a_n - L} < \varepsilon)}
  \open[\varepsilon_0]
  \hypo {2} {\varepsilon_0 > 0}
  \have {3} {\varepsilon_0 / 2 > 0} \by{arith}{2}
  \have {4} {\exists N \in \nN \; \forall n \in \nN \; (n \ge N \to \abs{a_n - L} < \varepsilon_0 / 2)} \Ae{1,3}
  \open[N_0]
  \hypo {5} {N_0 \in \nN}
  \hypo {6} {\forall n \in \nN \; (n \ge N_0 \to \abs{a_n - L} < \varepsilon_0 / 2)}
  \open[n_0]
  \hypo {7} {n_0 \in \nN}
  \have {8} {n_0 \ge N_0 \to \abs{a_{n_0} - L} < \varepsilon_0 / 2} \Ae{6,7}
  \open
  \hypo {9} {n_0 \ge N_0}
  \have {10} {\abs{a_{n_0} - L} < \varepsilon_0 / 2} \ie{8,9}
  \have {11} {\abs{2 \cdot a_{n_0} - 2 \cdot L} < \varepsilon_0} \by{arith}{10}
  \close
  \have {12} {n_0 \ge N_0 \to \abs{2 \cdot a_{n_0} - 2 \cdot L} < \varepsilon_0} \ii{9-11}
  \close
  \have {13} {\forall n \in \nN \; (n \ge N_0 \to \abs{2 \cdot a_n - 2 \cdot L} < \varepsilon_0)} \Ai{7-12}
  \have {14} {\exists N \in \nN \; \forall n \in \nN \; (n \ge N \to \abs{2 \cdot a_n - 2 \cdot L} < \varepsilon_0)} \Ei{5,13}
  \close
  \have {15} {\exists N \in \nN \; \forall n \in \nN \; (n \ge N \to \abs{2 \cdot a_n - 2 \cdot L} < \varepsilon_0)} \Ee{4,5-14}
  \close
  \have {16} {\forall \varepsilon > 0 \; \exists N \in \nN \; \forall n \in \nN \; (n \ge N \to \abs{2 \cdot a_n - 2 \cdot L} < \varepsilon)} \Ai{2-15}
\end{nd}$
\end{center}
```

Check the side conditions at the three lines that close flagged boxes, and the witness line.

- Line 13 (\( \forall n \in \nN \; \rulename{I} \), flag \( n_0 \)): \( n_0 \) is not in the premise, not in line 13, and not in the assumptions still open at line 13, which are lines 2, 5, and 6.
- Line 14 (\( \exists N \in \nN \; \rulename{I} \)): the witness \( N_0 \), with its bound on line 5 and the instance on line 13.
- Line 15 (\( \exists N \in \nN \; \rulename{E} \), flag \( N_0 \)): \( N_0 \) is not in line 15, the conclusion (the witness has been forgotten by line 14), not in line 4, not in the premise, and not in the open assumption on line 2.
- Line 16 (\( \forall \varepsilon > 0 \; \rulename{I} \), flag \( \varepsilon_0 \)): \( \varepsilon_0 \) is not in the premise and not in line 16, and no assumption is open at line 16.

Line 4 is where \( N \) comes to depend on \( \varepsilon \): the witness \( N_0 \) is obtained from the premise **at \( \varepsilon_0 / 2 \)**, so it depends on \( \varepsilon_0 \), exactly as the order \( \forall \varepsilon\, \exists N \) allows. Section 6.4 makes this reading of dependence precise.

In prose, line by line:

> Let \( \varepsilon > 0 \) [lines 2, 16]. Then \( \varepsilon / 2 > 0 \) [3], so, since \( a_n \to L \), there is \( N \in \nN \) with \( \abs{a_n - L} < \varepsilon/2 \) for every \( n \ge N \) [4]; choose such an \( N \) [5, 6, 15]. Let \( n \in \nN \) with \( n \ge N \) [7, 9]. Then \( \abs{a_n - L} < \varepsilon / 2 \) [8, 10], so \( \abs{2 a_n - 2 L} = 2 \abs{a_n - L} < \varepsilon \) [11]. So this \( N \) works [12–14].

Written with the unbounded rules, the same derivation has 22 lines, since each of its six bounded steps (lines 4, 8, 13, 14, 15, and 16) costs one line more. The claim "\( \frac1n \to 0 \)" (for \( n \ge 1 \)) is not derived here: its proof needs the Archimedean property, a fact about \( \nN \) inside \( \nR \), not a law of logic.

::: {.remark}
[Looking ahead]

Induction ("a set of natural numbers that contains \( 0 \) and contains \( n + 1 \) whenever it contains \( n \) contains every natural number") and the least-upper-bound property of the real numbers say "for every **set** of numbers", and the variables of this chapter range over numbers only. Chapter 7's optional last section says what that costs.
:::

## Exercises

### A. Check your understanding

::: {#exr-translation-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Translate into formulas, stating the domain: (i) every real number has a cube root; (ii) the function \( f \) is bounded on \( A \); (iii) between any two different real numbers there is a rational number; (iv) the sequence \( (a_n) \) is eventually constant; (v) some natural number divides every natural number.
2. Three students translate "some element of \( A \) is larger than every element of \( B \)", over \( \nR \):
   (i) \( \exists x \in A \; \forall y \in B \; (x > y) \); (ii) \( \exists x\, \bigl( x \in A \to \forall y \in B\; (x > y) \bigr) \); (iii) \( \forall y \in B \; \exists x \in A \; (x > y) \). Which are correct? For each wrong one, give sets \( A \), \( B \) for which it has the wrong truth value.
3. Which variables are free in your answer to (a)(iv)?
4. Write the bounded rule \( \exists x \in A \; \rulename{I} \) as a block of two unbounded steps, and name the two rules.
:::
:::

::: {.solution}
*(a)* (i) Over \( \nR \): \( \forall x\, \exists y\, (y \cdot y \cdot y = x) \). (ii) Over \( \nR \): \( \exists M\, \forall x \in A\, (\abs{f(x)} \le M) \). (iii) Over \( \nR \), with \( \in \nQ \) a one-place predicate symbol: \( \forall x\, \forall y\, \bigl( x < y \to \exists q \in \nQ\; (x < q \wedge q < y) \bigr) \); "different" is carried by \( x < y \), which names the smaller number \( x \) (the case \( y < x \) is the same statement with the letters exchanged). (iv) Over \( \nR \), with \( a \) a function symbol: \( \exists N \in \nN\; \forall n \in \nN\; (n \ge N \to a_n = a_N) \). (v) Over \( \nN \): \( \exists d\, \forall n\, \exists k\, (n = d \cdot k) \); it is true, with \( d = 1 \).

*(b)* Only (i) is correct. (ii) has \( \to \) under \( \exists \): with \( A = \{0\} \) and \( B = \{5\} \), the sentence in words is false, but (ii) is true, because \( x = 7 \notin A \) makes the implication vacuously true. (iii) has the quantifiers in the wrong order: it lets the element of \( A \) depend on \( y \). With \( A = B = \nN \), (iii) is true (for each \( y \), take \( x = y + 1 \)), and the sentence in words is false, since no natural number exceeds every natural number.

*(c)* None of the variables: \( N \) and \( n \) are bound. The formula is a statement about the function symbol \( a \), which is not a variable.

*(d)* From \( t \in A \) and \( \varphi[t/x] \): first \( t \in A \wedge \varphi[t/x] \) by \( \rulename{\wedge I} \), then \( \exists x\, (x \in A \wedge \varphi) \) by \( \rulename{\exists I} \), which is \( \exists x \in A\; \varphi \) unfolded.
:::

::: {#exr-translation-a2}
[A2: Drill]

Each part takes a line or two. The domain is \( \nR \), and \( A \), \( B \) are sets of reals. The parts run from translating, through unfolding and judging, to single steps of the bounded rules.

::: {.enumerate options="label=(\alph*)"}
1. Translate "\( f \) is bounded above on \( A \)".
2. Translate "every element of \( A \) is less than some element of \( B \)".
3. Translate "some element of \( A \) is less than every element of \( B \)".
4. Unfold the bounds of (c).
5. Write the mixed stage, then the formula, for "every element of \( A \) has a larger element in \( A \)".
6. Translate "\( a_n > 0 \) for all large \( n \)".
7. Translate "\( a_n \le 0 \) for infinitely many \( n \)".
8. Translate "not every element of \( A \) is positive" and "no element of \( A \) is positive", and decide both for \( A = \{-1, 1\} \).
9. Translate "if \( x \cdot x < 0 \) for any real \( x \), then \( 0 = 1 \)".
10. Lines 1 \( \forall \varepsilon > 0\; \varphi \) and 2 \( 1 > 0 \). What does the bounded \( \rulename{\forall E} \) 1, 2 give?
11. Lines 1 \( 3 \in \nN \) and 2 \( 3 + 3 = 6 \). What does the bounded \( \rulename{\exists I} \) 1, 2 give, with \( \varphi \) the formula \( n + n = 6 \)?
12. How many lines does a bounded \( \rulename{\exists E} \) save over the unbounded rule?
:::
:::

::: {.solution}
(a) \( \exists M\; \forall x \in A\; (f(x) \le M) \).

(b) \( \forall x \in A\; \exists y \in B\; (x < y) \).

(c) \( \exists x \in A\; \forall y \in B\; (x < y) \).

(d) \( \exists x\, (x \in A \wedge \forall y\, (y \in B \to x < y)) \).

(e) \( \forall x \in A\; [\text{some element of } A \text{ is larger than } x] \), then \( \forall x \in A\; \exists y \in A\; (x < y) \).

(f) \( \exists N \in \nN\; \forall n \in \nN\; (n \ge N \to a_n > 0) \).

(g) \( \forall N \in \nN\; \exists n \in \nN\; (n \ge N \wedge a_n \le 0) \).

(h) \( \neg\forall x \in A\; (x > 0) \), true for \( \{-1, 1\} \) (because of \( -1 \)); \( \neg\exists x \in A\; (x > 0) \), or \( \forall x \in A\; \neg(x > 0) \), false (because of \( 1 \)). One word apart, opposite truth values.

(i) \( \exists x\, (x \cdot x < 0) \to 0 = 1 \): "any" after "if" is "some". It is true, since no real square is negative.

(j) \( \varphi[1/\varepsilon] \).

(k) \( \exists n \in \nN\; (n + n = 6) \).

(l) One: two assumptions in place of one assumption and two \( \rulename{\wedge E} \) lines.
:::

### B. Practice

::: {#exr-translation-b1}
[B1: Three definitions]

Formalize each statement, stating the domain and the kind of each symbol (variable, constant, function symbol, predicate symbol; membership \( \in A \) in a fixed set \( A \) is a one-place predicate symbol, as in Section 5.2).

::: {.enumerate options="label=(\alph*)"}
1. The set \( A \) of real numbers is bounded (above and below).
2. The function \( f \colon \nR \to \nR \) is increasing on \( A \): for all \( x, y \in A \), \( x < y \) implies \( f(x) \le f(y) \).
3. The sequence \( (a_n) \) is bounded: there is a real \( M \) with \( \abs{a_n} \le M \) for all \( n \).
:::

Then, for (c), write the formula with the two quantifiers in the other order, and say why it holds for every sequence.
:::

::: {.solution}
No constants occur in any of the three parts.

*(a)* Domain \( \nR \); \( m \), \( M \), \( x \) variables (all bound); \( \in A \) a one-place and \( \le \) a two-place predicate symbol. \( \exists m\, \exists M\, \forall x \in A\, (m \le x \wedge x \le M) \). The two witnesses are chosen before \( x \), so they must work for every element of \( A \).

*(b)* Domain \( \nR \); \( x \), \( y \) variables (bound); \( f \) a one-place function symbol; \( \in A \) a one-place and \( < \), \( \le \) two-place predicate symbols. \( \forall x \in A\; \forall y \in A\; \bigl( x < y \to f(x) \le f(y) \bigr) \).

*(c)* Domain \( \nR \); \( M \), \( n \) variables (bound); \( a \) a one-place function symbol (the one-domain convention, step 1 of the procedure), and \( \abs{\cdot} \) a one-place function symbol; \( \in \nN \) a one-place and \( \le \) a two-place predicate symbol. \( \exists M\; \forall n \in \nN\; (\abs{a_n} \le M) \).

Swapped: \( \forall n \in \nN\; \exists M\; (\abs{a_n} \le M) \). It holds for every sequence, because the witness may depend on \( n \): take \( M = \abs{a_n} \). The sequence \( a_n = n \), which is not bounded, satisfies it. As in @exm-quantifier-order-sum, the swap turns a statement about one \( M \) for all \( n \) into a statement about each term separately.
:::

::: {#exr-translation-b2}
[B2: A bounded rehearsal]

Using the bounded rules of @prp-bounded-quantifier-rules, derive
\[
\forall x \in A \; (P(x) \to Q(x)), \;\; \exists x \in A \; P(x) \;\vdash\; \exists x \in A \; Q(x).
\]
Then say how many lines the derivation would have with the unbounded rules only.
:::

::: {.solution}
The goal is an \( \exists \): postpone it. The second premise is an \( \exists \): open its bounded \( \rulename{\exists E} \) box at once, with a witness \( x_0 \) and the two assumptions \( x_0 \in A \) and \( P(x_0) \), and aim for the goal as the box's last line. Inside, the first premise is a \( \forall x \in A \), and the term the box offers is \( x_0 \), with its bound on a line. The witness for the goal is \( x_0 \) again.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x \in A \; (P(x) \to Q(x))}
  \hypo {2} {\exists x \in A \; P(x)}
  \open[x_0]
  \hypo {3} {x_0 \in A}
  \hypo {4} {P(x_0)}
  \have {5} {P(x_0) \to Q(x_0)} \Ae{1,3}
  \have {6} {Q(x_0)} \ie{5,4}
  \have {7} {\exists x \in A \; Q(x)} \Ei{3,6}
  \close
  \have {8} {\exists x \in A \; Q(x)} \Ee{2,3-7}
\end{nd}$
\end{center}
```

At line 8, \( x_0 \) is not in line 8, not in line 2, and not in either premise; no other box is open. The derivation uses three bounded steps (lines 5, 7 and 8), each of which costs one more line unbounded, so the unbounded derivation has \( 8 + 3 = 11 \) lines: the \( \rulename{\exists E} \) box assumes \( x_0 \in A \wedge P(x_0) \) and splits it with two \( \rulename{\wedge E} \) lines; line 5 becomes \( \rulename{\forall E} \) then \( \rulename{{\to}E} \); line 7 becomes \( \rulename{\wedge I} \) then \( \rulename{\exists I} \).

The bound is the whole point of the exercise: the witness \( x_0 \) must carry its membership in \( A \) from the premise to the conclusion, and the bounded rules make that one assumption and one citation.
:::

::: {#exr-translation-b3}
[B3: One key, twenty sentences]

The domain is \( \nN = \{0, 1, 2, \dots\} \). Use only \( \mathrm{Prime}(x) \) ("\( x \) is prime"), \( \mathrm{Even}(x) \), \( x < y \), \( x \mid y \) ("\( x \) divides \( y \)", that is, \( y = x \cdot k \) for some \( k \)), \( = \) and the constants \( 1 \), \( 2 \), \( 9 \), with variables \( x \), \( y \), \( z \). Translate sentences 1–18 into formulas. Then translate 19 and 20 into English and decide whether each is true.

1. \( 2 \) is an even prime.
2. Some prime divides \( 9 \).
3. Every prime greater than \( 2 \) is odd.
4. No prime is less than \( 2 \).
5. Every even number is divisible by \( 2 \).
6. Only odd numbers divide \( 9 \).
7. \( 1 \) divides every number.
8. Some number divides every number.
9. Every number is divisible by some number.
10. There is no largest prime.
11. There are infinitely many primes.
12. Every number greater than \( 1 \) has a prime divisor.
13. The only divisors of a prime are \( 1 \) and the prime itself.
14. If a number divides \( 2 \), it is \( 1 \) or \( 2 \).
15. Not every odd number is prime.
16. Between any two numbers, one less than the other, there is a third.
17. Some prime divides every even number.
18. Every divisor of \( 1 \) is \( 1 \).
19. \( \forall x\, \forall y\, ((x \mid y \wedge y \mid x) \to x = y) \).
20. \( \forall x\, (\mathrm{Even}(x) \to \exists y\, (\mathrm{Prime}(y) \wedge y \mid x \wedge \neg(y = 2))) \).
:::

::: {.solution}
1. \( \mathrm{Even}(2) \wedge \mathrm{Prime}(2) \).
2. \( \exists x\, (\mathrm{Prime}(x) \wedge x \mid 9) \).
3. \( \forall x\, ((\mathrm{Prime}(x) \wedge 2 < x) \to \neg\mathrm{Even}(x)) \).
4. \( \neg\exists x\, (\mathrm{Prime}(x) \wedge x < 2) \), or \( \forall x\, (\mathrm{Prime}(x) \to \neg(x < 2)) \).
5. \( \forall x\, (\mathrm{Even}(x) \to 2 \mid x) \).
6. \( \forall x\, (x \mid 9 \to \neg\mathrm{Even}(x)) \).
7. \( \forall x\, (1 \mid x) \).
8. \( \exists x\, \forall y\, (x \mid y) \).
9. \( \forall y\, \exists x\, (x \mid y) \).
10. \( \forall x\, (\mathrm{Prime}(x) \to \exists y\, (\mathrm{Prime}(y) \wedge x < y)) \).
11. \( \forall x\, \exists y\, (x < y \wedge \mathrm{Prime}(y)) \).
12. \( \forall x\, (1 < x \to \exists y\, (\mathrm{Prime}(y) \wedge y \mid x)) \).
13. \( \forall x\, (\mathrm{Prime}(x) \to \forall y\, (y \mid x \to (y = 1 \vee y = x))) \).
14. \( \forall x\, (x \mid 2 \to (x = 1 \vee x = 2)) \).
15. \( \neg\forall x\, (\neg\mathrm{Even}(x) \to \mathrm{Prime}(x)) \).
16. \( \forall x\, \forall y\, (x < y \to \exists z\, (x < z \wedge z < y)) \).
17. \( \exists x\, (\mathrm{Prime}(x) \wedge \forall y\, (\mathrm{Even}(y) \to x \mid y)) \).
18. \( \forall x\, (x \mid 1 \to x = 1) \).
19. "Two numbers that divide each other are equal." True in \( \nN \): if \( y = xk \) and \( x = yl \), then \( x = xkl \), so either \( x = 0 \), and then \( y = 0 \) too, or \( kl = 1 \), which in \( \nN \) means \( k = l = 1 \).
20. "Every even number has a prime divisor other than \( 2 \)." False: at \( x = 2 \), and at every power of \( 2 \) (\( 4, 8, 16, 32, \dots \)), the only prime divisor is \( 2 \).

Sentence 10 restricts \( x \) to primes and 11 does not; both are true, and in \( \nN \) each follows from the other. Sentence 16 is false (take \( x = 0 \), \( y = 1 \)), and its translation is still correct: a correct translation of a false sentence is a false formula.
:::

::: {#exr-translation-b4}
[B4: Unfold, then fold back]

Over \( \nR \), for fixed sets \( A \), \( B \), \( C \) of reals, write \( A \subseteq B \) for "every element of \( A \) is an element of \( B \)", \( A \cup B \) for the set of reals in \( A \) or in \( B \), and \( A \cap B \) for the set of those in both. Use only the predicates \( \in A \), \( \in B \), \( \in C \).

::: {.enumerate options="label=(\alph*)"}
1. Unfold \( A \subseteq B \cap C \).
2. Unfold \( A \cup B \subseteq C \).
3. Unfold "\( A \cap B \) has no element".
4. Fold back \( \forall x\, (x \in A \to x \in B) \wedge \forall x\, (x \in B \to x \in C) \).
5. Fold back \( \forall x\, ((x \in A \wedge x \in B) \to x \in C) \).
6. A reader unfolds \( A \cup B \subseteq C \) as the formula in (e). Give sets that separate the two, and say why the reader's formula is wrong.
:::
:::

::: {.solution}
*(a)* \( \forall x\, (x \in A \to (x \in B \wedge x \in C)) \).

*(b)* \( \forall x\, ((x \in A \vee x \in B) \to x \in C) \).

*(c)* \( \neg\exists x\, (x \in A \wedge x \in B) \).

*(d)* \( A \subseteq B \) and \( B \subseteq C \).

*(e)* \( A \cap B \subseteq C \).

*(f)* \( A = \{1\} \), \( B = \{2\} \), \( C = \emptyset \). Then \( A \cup B \subseteq C \) is false, since \( 1 \in A \cup B \) and \( 1 \notin C \). The formula of (e) is true, because \( A \cap B \) has no element, so its hypothesis \( x \in A \wedge x \in B \) is false for every \( x \). The reader's mistake is trap (b) of the section: "in \( A \) or in \( B \)" is the restriction of (b), and it must be written with \( \vee \); the "and" of "every element of \( A \) and of \( B \)" is an "or" in the restriction.

**Marking scheme.** (10 points)
- 2: (a)–(c) together, with every bound attached by \( \to \) under \( \forall \) (and by \( \wedge \) under the \( \exists \) of (c)).
- 2: (d) and (e).
- 3: (f): the two sets, with one sentence on each truth value.
- 3: the reason in words that the restriction of (b) is an "or".
Fatal error (0 for (f)): a pair of sets on which the two formulas agree.
:::

### C. Going deeper

::: {#exr-translation-c1}
[C1: Where the \( \forall x \) stands]

Let \( f \colon \nR \to \nR \) and \( A \subseteq \nR \). Translate, over \( \nR \):

::: {.enumerate options="label=(\alph*)"}
1. \( f \) is **uniformly continuous** on \( A \): for every \( \varepsilon > 0 \) there is \( \delta > 0 \) such that for all \( x, y \in A \), \( \abs{x - y} < \delta \) implies \( \abs{f(x) - f(y)} < \varepsilon \);
2. \( f \) is continuous at every point of \( A \): for every \( x \in A \) and every \( \varepsilon > 0 \) there is \( \delta > 0 \) such that for every \( y \in A \), \( \abs{x - y} < \delta \) implies \( \abs{f(x) - f(y)} < \varepsilon \).
:::

Then describe, in one sentence, the only difference between the two formulas, and say what it means for the choice of \( \delta \).
:::

::: {.solution}
*(a)* \( \forall \varepsilon > 0 \; \exists \delta > 0 \; \forall x \in A \; \forall y \in A \; \bigl( \abs{x - y} < \delta \to \abs{f(x) - f(y)} < \varepsilon \bigr) \).

*(b)* \( \forall x \in A \; \forall \varepsilon > 0 \; \exists \delta > 0 \; \forall y \in A \; \bigl( \abs{x - y} < \delta \to \abs{f(x) - f(y)} < \varepsilon \bigr) \).

The only difference is the position of \( \forall x \in A \): in (a) it stands after \( \exists \delta > 0 \), in (b) before it. In (b) the defender chooses \( \delta \) knowing \( x \), so \( \delta \) may depend on \( x \) and on \( \varepsilon \); in (a) \( \delta \) is chosen before any \( x \) is given, so one \( \delta \) must serve every \( x \in A \) at once, and it depends on \( \varepsilon \) only. Section 6.4 derives (b) from (a) and shows that \( x^2 \) on \( \nR \) satisfies (b) but not (a); Section 7.2 turns this example into a counter-model, so (b) does not derive (a).
:::

::: {#exr-translation-c2}
[C2: Six orders, four statements]

Fix a formula \( \mu \) (the "matrix") in the variables \( x \), \( y \), \( z \), and consider the six sentences obtained by putting the prefixes \( \forall x \), \( \exists y \), \( \forall z \) in front of \( \mu \) in the six possible orders: \( \forall x\, \exists y\, \forall z\, \mu \), \( \forall z\, \exists y\, \forall x\, \mu \), and so on. Call two of these orders **essentially the same** if the two sentences are provably equivalent (\( \dashv\vdash \)) for every matrix \( \mu \), and **essentially different** if some matrix over \( \nZ \) gives them different truth values (read informally, as in Section 5.1).

::: {.enumerate options="label=(\alph*)"}
1. Show that the six orders fall into four groups, with any two orders in one group essentially the same.
2. Using the matrices \( y > x \) and \( y > z \) over \( \nZ \), show that any two orders from different groups are essentially different. So the six orders say four different things.
:::
:::

::: {.solution}
[Hint 1]

Two \( \forall \)'s side by side can be exchanged: that was one of the derivations of @exm-universal-introduction-derivations. What is left to decide is where \( \exists y \) stands.
:::

::: {.solution}
[Hint 2]

List the six orders by the position of \( \exists y \): first, middle or last. When it is first or last, the two \( \forall \)'s are side by side.
:::

::: {.solution}
*(a)* Sort the orders by the position of \( \exists y \).

- \( \exists y \) first: \( \exists y\, \forall x\, \forall z\, \mu \) and \( \exists y\, \forall z\, \forall x\, \mu \).
- \( \exists y \) last: \( \forall x\, \forall z\, \exists y\, \mu \) and \( \forall z\, \forall x\, \exists y\, \mu \).
- \( \exists y \) in the middle: \( \forall x\, \exists y\, \forall z\, \mu \), and \( \forall z\, \exists y\, \forall x\, \mu \).

Two adjacent \( \forall \)'s may be exchanged: \( \forall x\, \forall z\, \psi \dashv\vdash \forall z\, \forall x\, \psi \) for every formula \( \psi \), by the derivation of @exm-universal-introduction-derivations that exchanges two universal quantifiers (it uses nothing about its matrix but that it is a formula). This gives the "last" pair at once. For the "first" pair the \( \forall \)'s sit under \( \exists y \): open the \( \rulename{\exists E} \) box on \( \exists y\, \forall x\, \forall z\, \mu \) with a witness \( y_0 \), exchange the two \( \forall \)'s inside it, and close with \( \rulename{\exists I} \) at \( y_0 \); the other direction is the same. So there are at most four groups: \( \{\exists y\, \forall x\, \forall z, \ \exists y\, \forall z\, \forall x\} \), \( \{\forall x\, \forall z\, \exists y, \ \forall z\, \forall x\, \exists y\} \), \( \{\forall x\, \exists y\, \forall z\} \) and \( \{\forall z\, \exists y\, \forall x\} \).

*(b)* Call the groups F (\( \exists y \) first), L (last), \( M_x \) (\( \forall x\, \exists y\, \forall z \)) and \( M_z \) (\( \forall z\, \exists y\, \forall x \)). Over \( \nZ \), evaluate each group with the two matrices, reading informally (Section 5.1):

| Group | \( \mu = (y > x) \) | \( \mu = (y > z) \) |
|---|---|---|
| F | false: no \( y \) exceeds every \( x \) | false: no \( y \) exceeds every \( z \) |
| L | true: given \( x \), \( z \), take \( y = x + 1 \) | true: take \( y = z + 1 \) |
| \( M_x \) | true: given \( x \), take \( y = x + 1 \) | false: no \( y \) exceeds every \( z \) |
| \( M_z \) | false: no \( y \) exceeds every \( x \) | true: given \( z \), take \( y = z + 1 \) |

Every two rows differ in at least one column, so every two groups are separated by one of the two matrices: F from L, from \( M_x \) and from \( M_z \) by the column in which the other group has "true"; L from \( M_x \) by \( y > z \) and from \( M_z \) by \( y > x \); \( M_x \) from \( M_z \) by either. So the six orders say four different things: within a group the sentences are provably equivalent by (a), and across groups some matrix over \( \nZ \) tells them apart.

**Marking scheme.** (10 points)
- 2: lists the six orders and sorts them by the position of \( \exists y \).
- 3: justifies the two collapses, citing the exchange of adjacent \( \forall \)'s, and handles the pair under \( \exists y \) (by an \( \rulename{\exists E} \) box, or equivalently).
- 3: gives, for each of the six pairs of groups, a matrix and the two truth values, with witnesses for the true sentences.
- 2: concludes that the six orders say four different things, combining (a) and (b).
Fatal errors (0 for the step): exchanging \( \forall \) with \( \exists \); a "separation" in which the two sentences have the same truth value.
:::

::: {#exr-translation-c3}
[C3: Eventually, therefore infinitely often]

::: {.enumerate options="label=(\alph*)"}
1. With the bounded rules, derive
   \[
   \exists N \in \nN\; \forall n \in \nN\; (n \ge N \to P(n)) \;\vdash\; \forall M \in \nN\; \exists n \in \nN\; (n \ge M \wedge P(n)).
   \]
   Lines of arithmetic may be justified "arith".
2. For the converse, give a reading of \( P \) over \( \nN \) under which the premise is true and the conclusion false.
:::
:::

::: {.solution}
*(a)* The goal is a bounded \( \forall \): open its box first, with \( M_0 \in \nN \). The premise is a bounded \( \exists \): open its box early, with \( N_0 \in \nN \) and its property. The postponed goal \( \exists n \in \nN \) needs a term that is at least \( M_0 \) and at which the premise applies, so at least \( N_0 \): the sum \( N_0 + M_0 \) is both.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\exists N \in \nN \; \forall n \in \nN \; (n \ge N \to P(n))}
  \open[M_0]
  \hypo {2} {M_0 \in \nN}
  \open[N_0]
  \hypo {3} {N_0 \in \nN}
  \hypo {4} {\forall n \in \nN \; (n \ge N_0 \to P(n))}
  \have {5} {N_0 + M_0 \in \nN} \by{arith}{2,3}
  \have {6} {N_0 + M_0 \ge N_0 \to P(N_0 + M_0)} \Ae{4,5}
  \have {7} {N_0 + M_0 \ge N_0} \by{arith}{2}
  \have {8} {P(N_0 + M_0)} \ie{6,7}
  \have {9} {N_0 + M_0 \ge M_0} \by{arith}{3}
  \have {10} {N_0 + M_0 \ge M_0 \wedge P(N_0 + M_0)} \ai{9,8}
  \have {11} {\exists n \in \nN \; (n \ge M_0 \wedge P(n))} \Ei{5,10}
  \close
  \have {12} {\exists n \in \nN \; (n \ge M_0 \wedge P(n))} \Ee{1,3-11}
  \close
  \have {13} {\forall M \in \nN \; \exists n \in \nN \; (n \ge M \wedge P(n))} \Ai{2-12}
\end{nd}$
\end{center}
```

Lines 7 and 9 use \( M_0 \ge 0 \) and \( N_0 \ge 0 \), which hold for natural numbers. The side conditions:

- At line 12, \( N_0 \) is not in line 12, not in line 1, not in the premise, and not in the open assumption on line 2.
- At line 13, \( M_0 \) is not in the premise and not in line 13, and no assumption is open.
- At lines 6 and 11, the term \( N_0 + M_0 \) is free for \( n \).

The witness \( N_0 + M_0 \) is built from the two names in play: fix \( M_0 \), obtain \( N_0 \), choose a term made from both.

*(b)* Let \( P(n) \) be "\( n \) is even". The premise of the converse, \( \forall M \in \nN\; \exists n \in \nN\; (n \ge M \wedge P(n)) \), is true: beyond any \( M \) there is an even number, such as \( 2M \). Its conclusion, \( \exists N \in \nN\; \forall n \in \nN\; (n \ge N \to P(n)) \), is false: beyond any \( N \) there is an odd number, \( 2N + 1 \). This is a counter-reading (Section 7.2).

**Marking scheme.** (10 points)
- 2: opens the box of \( M_0 \) first, and the \( \rulename{\exists E} \) box on the premise early.
- 3: a witness that depends on both names, with both bounds checked by arith lines.
- 2: checks the side conditions at lines 12 and 13.
- 3: (b): a reading, with both truth values justified.
Fatal errors (0 for the step): a witness chosen before \( M_0 \) is given; the witness \( N_0 \) itself, which need not be at least \( M_0 \).
:::

<!-- dependency ledger
exm-translate-limit (solution): m | n means n = m * k for some integer k | NOTATION.md row for d | n (definition, first used F1.2); stated in the solution
exm-translate-limit (solution): (d) the two forms of "no largest prime" say the same thing over N; not (n <= m) iff m < n over N | order fact (school arithmetic); the logical part is F1.8 §02 (later section of this chapter; prose pointer only, nothing here rests on it)
translation-check (solution): (0, 1) is bounded above by 1 (x < 1 for x in (0, 1)) and has no maximum (m < (m+1)/2 < 1 for m in (0, 1)) | school algebra (order); AN1.1 (prose pointer); checked by verify/ch06/exm-translate-limit.py
exm-translate-limit (claim): the opening list: 1, 1/2, 1/3, ... has terms not all close to any L; only eventually-L sequences satisfy the swapped form | informal reading, illustrative only; no result rests on it
exm-translate-limit (claim): the warning: f(x) = x is bounded by 1 on [0, 1] and not on R; a_n = n - 3 has a_0 = -3 and a_n > 0 for n >= 4 | school arithmetic; checked by verify/ch06/exm-translate-limit.py
prp-bounded-quantifier-rules (proof): (x in A -> phi)[t/x] is t in A -> phi[t/x]; t free for x in (x in A -> phi) iff t free for x in phi; likewise with x > a when x does not occur in a | def-substitution, def-free-for (cited); argued inline
prp-bounded-quantifier-rules (proof): moving lines into a new enclosing box keeps each citation available | def-derivation's scope rule (F1.1, cited as def-derivation via F1.4 §04's extension to flagged boxes); argued inline
prp-bounded-quantifier-rules (claim): a new rule is admissible if every use can be replaced by old steps | def-derived-rule (cited), extended; argued in the text
prp-bounded-quantifier-rules (example): the limit derivation: eps_0 > 0 gives eps_0/2 > 0; |a - L| < eps_0/2 gives |2a - 2L| < eps_0 since |2u - 2v| = 2|u - v| | arith lines (school algebra); AN1.1 (prose pointer for the Archimedean remark only)
prp-bounded-quantifier-rules (example): the limit derivation: the unbounded version has 22 lines | inline count: 16 lines + one per bounded step (six)
exr-translation-a1 (solution): 7 not in {0}; no natural number exceeds every natural number; 1 divides every n | school arithmetic; checked by verify/ch06/exr-translation-a1.py
exr-translation-c2 (solution): exchange of adjacent foralls for any matrix | exm-universal-introduction-derivations (cited); its derivation uses nothing about R(x, y) but that it is a formula
exr-translation-c2 (solution): truth values over Z of the eight sentences in the table | informal truth, F1.4 §01; witnesses y = x + 1, y = z + 1 given; checked by verify/ch06/exr-translation-c2.py
exm-translate-limit (claim): step 1 of the procedure, a convention: one domain per formula; the larger kind is the domain and the smaller kind enters as a bound; a sequence is a function symbol | convention of this book, no fact (moved from old 5.1; 5.1 keeps two sentences, "Mixing kinds of number")
exm-translate-limit (example): the mixed stage: the three stages say the same thing as "for every positive eps, some element of A lies within eps of s" | no fact; reading back
exm-translation-traps (example): no natural number lies strictly between 1/3 and 2/3, and 1/2 does; 2 is even and not a multiple of 4, and every multiple of 4 is even; 6 divides 6, 1 is odd, every multiple of 6 is even; A = {1}, B = {-1} has no common element; every element of the empty set has every property | school arithmetic; the empty set and "any" from F1.4 §01 (cited as Section 5.1); one-domain convention of step 1; checked by verify/ch06/exm-translation-traps.py
exm-translation-traps (claim): infinitely many and eventually: (-1)^n is positive at every even n and negative at every odd n | parity (school arithmetic)
exm-translation-traps (claim): translation error or derivation error: not (7 in {1, 2}); 7 > 5; neither 1 nor 2 exceeds 5; the two steps are prp-vacuous-implication and exists-I | school arithmetic; prp-vacuous-implication (F1.2, cited)
prp-bounded-quantifier-rules (claim): the Not-allowed block: each wrong step breaks the named condition of the proposition | prp-bounded-quantifier-rules (cited); no entry is legal
prp-bounded-quantifier-rules (example): the outline of the limit derivation: lines 1-6 and 13-16 of the outline are those of the full derivation with G and G_2 abbreviated | inline; the full derivation is checked line by line
exr-translation-a2 (solution): (h) on {-1, 1}; (i) x * x >= 0 for every real x | school algebra; checked by verify/ch06/exr-translation-a2.py
exr-translation-b3 (solution): the twenty formulas against their sentences over N; 19 true (x = xkl gives x = 0 = y or k = l = 1); 20 false at powers of 2; 16 false at (0, 1); 10 and 11 both true (Euclid, school fact) | school arithmetic; checked by verify/ch06/exr-translation-b3.py (bounded search to 60)
exr-translation-b4 (solution): A = {1}, B = {2}, C = empty separate (b) from (e) | school arithmetic; checked by verify/ch06/exr-translation-b4.py
exr-translation-c3 (solution): N_0 + M_0 is in N and at least N_0 and M_0 for N_0, M_0 in N; beyond any M there is an even number (2M) and beyond any N an odd one (2N + 1) | arith lines (school arithmetic); checked by verify/ch06/exr-translation-c3.py; counter-reading pointer to F1.6 §02 (prose, nothing rests on it)
-->
