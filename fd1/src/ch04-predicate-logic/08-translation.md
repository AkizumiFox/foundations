# Translating Mathematics: Nested and Bounded Quantifiers

The calculus is now complete: Sections 4.3–4.7 gave a rule for using and a rule for proving each quantifier, and the two rules for equality. Before any of those rules can act on a definition from analysis, the definition has to be written as a formula, and written correctly. The definitions of analysis have three or four quantifiers stacked in a fixed order, most of them carrying a bound such as \( \varepsilon > 0 \) or \( n \ge N \), and every bound costs extra lines in a derivation. This section does three things. It translates the standard definitions into formulas, by a procedure that works from the outside in. It turns each quantifier rule into a **bounded** rule that handles the bound in the same step. And it collects the steps of Sections 4.3–4.7 into the search method of Section 2.6, extended to quantifiers and equality.

## Four pieces in one sentence

"The sequence \( (a_n) \) converges to \( L \)" is written \( a_n \to L \), and a first course defines it in one breath: for every \( \varepsilon > 0 \) there is \( N \in \nN \) such that \( \abs{a_n - L} < \varepsilon \) for all \( n \ge N \). The sentence has three quantifiers, each with a bound (\( \varepsilon > 0 \), \( N \in \nN \), \( n \in \nN \)), and a fourth condition, \( n \ge N \), hidden in "for all \( n \ge N \)", which will turn out to sit under an implication. Each piece has a job, and a slip in any piece changes the meaning:

- drop the bound \( \varepsilon > 0 \), and the challenger may choose \( \varepsilon = -1 \); then \( \abs{a_n - L} < -1 \) is impossible, and **no** sequence converges;
- swap "for every \( \varepsilon \)" and "there is \( N \)", and one \( N \) must serve every \( \varepsilon \); then only sequences that are eventually equal to \( L \) converge;
- read "for all \( n \ge N \)" as "for all \( n \)", and the first terms must already be close to \( L \); then \( 1, \frac12, \frac13, \dots \) converges to nothing.

So translation deserves a procedure, and the rules deserve a form that handles bounds without fuss. We take them in that order.

## Translation from the outside in

*Find the outermost claim, name its quantifier and its bound, then translate what it claims about each object, in the same way.*

The procedure, in three steps:

1. **Fix the domain.** State what the variables range over. By the one-domain convention of Section 4.1 (after @def-bounded-quantifier), a sentence that mixes kinds of object uses the largest kind as the domain, and each smaller kind enters as a bound: \( N \in \nN \) inside the domain \( \nR \). A sequence \( (a_n) \) is a function symbol \( a \), with \( a_n \) its value at \( n \).
2. **Find the outermost claim.** Ask what the sentence says first, before any detail: "every \( \varepsilon > 0 \) has a property", "there is an \( M \) with a property", "no prime is largest". That gives the outermost quantifier (or connective) and its bound.
3. **Recurse.** Translate the property, which is a sentence about the object just quantified, by the same two steps. Stop at atomic formulas: equations, inequalities, membership, and predicate symbols such as \( \mathrm{Prime}(p) \).

A bound is attached to its own quantifier with the connective of @def-bounded-quantifier: \( \to \) under \( \forall \), \( \wedge \) under \( \exists \). The bounded notation \( \forall \varepsilon > 0 \), \( \exists N \in \nN \) does this automatically, which is why we use it.

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

*(b)* Domain \( \nR \); \( A \) names a set of reals, and \( x \in A \) is a one-place predicate of \( x \) (Section 4.1). "Bounded above" means that some real number is at least every element of \( A \). Outermost claim: there is an \( M \). Its property: every element of \( A \) is at most \( M \):
\[
\exists M \; \forall x \in A \; (x \le M).
\]
The bound \( x \in A \) belongs to the \( \forall \); there is no bound on \( M \), which may be any real number.

*(c)* Domain \( \nR \), with \( f \) a one-place function symbol and \( a \) a variable, free in the formula:
\[
\forall \varepsilon > 0 \; \exists \delta > 0 \; \forall x \; \bigl( \abs{x - a} < \delta \to \abs{f(x) - f(a)} < \varepsilon \bigr).
\]
The last quantifier has no bound of the form "\( x \in \) something", because \( f \) is defined on all of \( \nR \); its restriction \( \abs{x - a} < \delta \) goes under the implication, like \( n \ge N \) in (a). For \( f \) defined on a set \( A \), the last quantifier would be \( \forall x \in A \).

*(d)* Domain \( \nN \), with \( \mathrm{Prime}(p) \) the predicate "\( p \) is prime". Section 4.1 read the sentence as \( \neg\exists p\, \bigl( \mathrm{Prime}(p) \wedge \forall q\, (\mathrm{Prime}(q) \to q \le p) \bigr) \). A mathematician more often states it positively, "for every prime there is a larger prime":
\[
\forall p \; \bigl( \mathrm{Prime}(p) \to \exists q \; (\mathrm{Prime}(q) \wedge p < q) \bigr).
\]
The two forms say the same thing over \( \nN \): the laws of Section 4.9 push the \( \neg \) inside and give \( \forall p\, \bigl( \mathrm{Prime}(p) \to \exists q\, (\mathrm{Prime}(q) \wedge \neg(q \le p)) \bigr) \), and the order fact that \( \neg(q \le p) \) is the same as \( p < q \) finishes the job. (They are not provably equivalent in logic alone: that last step is a fact about the order of \( \nN \), not a law of logic.)

*(e)* Domain \( \nZ \). Outermost claim: every integer greater than \( 1 \) has a property, \( \forall n > 1 \). The property: some \( p \) is prime and divides \( n \). "Divides" is itself a quantifier: \( p \mid n \) means \( n = p \cdot k \) for some integer \( k \). So
\[
\forall n > 1 \; \exists p \; \bigl( \mathrm{Prime}(p) \wedge \exists k \; (n = p \cdot k) \bigr).
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
**Three mistranslations to avoid.** (1) An \( \exists \) with \( \to \) under it, such as \( \exists x\, (x \in A \to x > 5) \): it is true as soon as something lies outside \( A \) (Section 4.1). (2) A bound on the wrong quantifier: "\( f \) is bounded on \( A \)" is \( \exists M\, \forall x \in A\, (\abs{f(x)} \le M) \); the form \( \exists M \in A\, \forall x\, (\abs{f(x)} \le M) \) asks for a bound that lies in \( A \) and works on all of \( \nR \), and it fails for \( f(x) = x \) on \( A = [0, 1] \), which is bounded on \( A \) by \( 1 \). (3) "For all large \( n \)" read as "for all \( n \)": "\( a_n > 0 \) for all large \( n \)" is \( \exists N \in \nN\; \forall n \in \nN\; (n \ge N \to a_n > 0) \), not \( \forall n \in \nN\, (a_n > 0) \). The sequence \( a_n = n - 3 \) satisfies the first (take \( N = 4 \)) and not the second (\( a_0 = -3 \)).
:::

## Rules for bounded quantifiers

Every analysis formula has bounds, and each bound doubles the work of a rule. To use \( \forall \varepsilon > 0\, \varphi \) at the term \( 1 \), \( \rulename{\forall E} \) gives \( 1 > 0 \to \varphi[1/\varepsilon] \), and a second step, \( \rulename{{\to}E} \) with a line \( 1 > 0 \), gives \( \varphi[1/\varepsilon] \). To prove \( \exists N \in \nN\, \psi \) with the witness \( 7 \), \( \rulename{\wedge I} \) builds \( 7 \in \nN \wedge \psi[7/N] \) and \( \rulename{\exists I} \) finishes. Every step is legal and every step is predictable, and a derivation about limits drowns in them. So we fold each pair into one step.

*A bounded quantifier gets a rule of its own: the bound travels with the quantifier.*

::: {#prp-bounded-quantifier-rules}
[Rules for Bounded Quantifiers]

Let \( A \) be a fixed set, so that \( \in A \) is a one-place predicate symbol (Section 4.2), \( x \) a variable and \( \varphi \) a formula. The following four rules, the **bounded rules**, may be used in derivations, with the rule names of the unbounded rules and the same side conditions: in \( \forall x \in A \; \rulename{E} \) and \( \exists x \in A \; \rulename{I} \), the term \( t \) is free for \( x \) in \( \varphi \); in \( \forall x \in A \; \rulename{I} \), the name \( x_0 \) appears in no premise, in no assumption of a box still open at line \( k \), and not in \( \forall x \in A\; \varphi \); in \( \exists x \in A \; \rulename{E} \), it appears in no premise, in no assumption of a box still open at line \( k \), and not in \( \chi \) or in \( \exists x \in A\; \varphi \). The last line of each box is a line of that box itself.

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

Every use of a bounded rule can be replaced by a block of steps of the unbounded rules (Sections 4.3–4.6) and of Chapter 1, with the same premises, the same assumptions open, and the same last line. Hence any derivation that uses the bounded rules converts into one that does not. The same holds with \( x \in A \) and \( t \in A \) replaced by \( x > a \) and \( t > a \), or by the bounds \( \ge a \), \( < a \), \( \le a \), for a term \( a \) in which \( x \) does not occur.
:::

In words: to **use** "every \( x \) in \( A \) has \( \varphi \)", produce an element \( t \) of \( A \) and conclude \( \varphi \) for \( t \). To **prove** "some \( x \) in \( A \) has \( \varphi \)", exhibit an element \( t \) of \( A \) with \( \varphi \). To **prove** "every \( x \) in \( A \) has \( \varphi \)", let \( x_0 \) be an arbitrary element of \( A \) (the box opens with the assumption \( x_0 \in A \)) and prove \( \varphi \) for it. To **use** "some \( x \) in \( A \) has \( \varphi \)", take such an element \( x_0 \), with both facts about it as assumptions, and derive something that does not mention it. These are exactly the sentences a mathematician writes: "let \( \varepsilon > 0 \)", "since \( \delta > 0 \), the hypothesis applies to \( \delta \)", "take \( N = 7 \in \nN \)", "choose \( \delta > 0 \) such that …".

The bounded \( \rulename{\forall I} \) box is the only flagged box with an assumption that closes by \( \rulename{\forall I} \). Its assumption \( x_0 \in A \) mentions the flag, and that is allowed: the side condition asks about assumptions of boxes **still open at line \( k \)**, and the box's own assumption has closed there.

Why is this a proposition and not simply a definition? Because the calculus is fixed: its rules are those of Chapters 1–2 and Sections 4.3–4.7, and a new rule is admissible only if it adds no derivable sequents. @def-derived-rule gave one way to show that: a proved sequent, written with statement letters, may be used as one line. It does not cover these rules. The bounded \( \rulename{\forall E} \) and \( \rulename{\exists I} \) are one line each, but they are schemas in a formula, a variable and a term, not in statement letters; the bounded \( \rulename{\forall I} \) and \( \rulename{\exists E} \) close boxes, which no proved sequent can. So the proposition proves admissibility the direct way: each bounded step is shown to be an abbreviation of a block of unbounded steps. In this sense the bounded rules are derived rules, in a looser sense that extends Chapter 2's: a line citing one abbreviates a block of primitive steps, not a proved sequent.

::: {.idea}
A bounded quantifier is an abbreviation (@def-bounded-quantifier): \( \forall x \in A\; \varphi \) **is** the formula \( \forall x\, (x \in A \to \varphi) \), and \( \exists x \in A\; \varphi \) **is** \( \exists x\, (x \in A \wedge \varphi) \). So each bounded rule should be an unbounded rule on the unfolded formula, plus the connective rule that handles \( \to \) or \( \wedge \). Write the block, then check two things: the block is a correct piece of derivation wherever the bounded step was, and its side conditions hold exactly when the bounded ones do.
:::

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

The lines between \( i \) and \( j \) are unchanged. Each of them lies inside both new boxes, so every line it cited is still available (@def-derivation, with the flagged boxes of Section 4.4): a line outside the old box is outside both new ones, and a line inside the old box is inside the new \( \rulename{{\to}I} \) box. The side conditions inside the old box are unaffected too: a line inside it has the same open assumptions as before, \( x_0 \in A \) (now the assumption of the \( \rulename{{\to}I} \) box) together with the outer ones, because the flagged box adds none; so every flagged box that closes inside the old box still meets its side condition. Line \( m \) is \( \rulename{{\to}I} \), and it is the last line of the flagged box, as \( \rulename{\forall I} \) requires; it is the instance at \( x_0 \) of \( x \in A \to \varphi \). Now the side condition of \( \rulename{\forall I} \) at line \( k \): the premises are the same as before; the boxes still open at line \( k \) are the same as those open at line \( k \) in the bounded version, because the \( \rulename{{\to}I} \) box on \( x_0 \in A \) has **closed** before line \( k \); and the conclusion is the same formula. So the unbounded side condition holds exactly when the bounded one does.

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
Run the search. The goal starts with \( \forall \varepsilon > 0 \): open a bounded \( \rulename{\forall I} \) box, "let \( \varepsilon_0 > 0 \)". The new goal starts with \( \exists N \in \nN \): **postpone** it (the step of Section 4.5), since no witness is in sight. Turn to the premise: it starts with \( \forall \varepsilon > 0 \), and the step of Section 4.3 says to instantiate it at the term the goal needs. Which term? The goal will need \( \abs{2 a_n - 2 L} < \varepsilon_0 \), which follows from \( \abs{a_n - L} < \varepsilon_0 / 2 \): so instantiate at \( \varepsilon_0 / 2 \), after an "arith" line \( \varepsilon_0 / 2 > 0 \) for the bound. That gives an \( \exists N \in \nN \) line: open its \( \rulename{\exists E} \) box **at once**, with a witness \( N_0 \) (the step of Section 4.6), and let the box's last line be the current goal. Now the postponed goal has its witness: \( N_0 \) itself. The remaining goal \( \forall n \in \nN\, (\dots) \) opens a bounded \( \rulename{\forall I} \) box for \( n_0 \), and a \( \rulename{{\to}I} \) box on \( n_0 \ge N_0 \) finishes with one \( \rulename{\forall E} \), one \( \rulename{{\to}E} \), and the second "arith" line. This is the pattern of @prp-exists-forall-swap: **fix** \( \varepsilon_0 \), **obtain** \( N_0 \), **choose** \( N_0 \) as the witness.
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

Line 4 is where \( N \) comes to depend on \( \varepsilon \): the witness \( N_0 \) is obtained from the premise **at \( \varepsilon_0 / 2 \)**, so it depends on \( \varepsilon_0 \), exactly as the order \( \forall \varepsilon\, \exists N \) allows. Section 4.10 makes this reading of dependence precise.

In prose, line by line:

> Let \( \varepsilon > 0 \) [lines 2, 16]. Then \( \varepsilon / 2 > 0 \) [3], so, since \( a_n \to L \), there is \( N \in \nN \) with \( \abs{a_n - L} < \varepsilon/2 \) for every \( n \ge N \) [4]; choose such an \( N \) [5, 6, 15]. Let \( n \in \nN \) with \( n \ge N \) [7, 9]. Then \( \abs{a_n - L} < \varepsilon / 2 \) [8, 10], so \( \abs{2 a_n - 2 L} = 2 \abs{a_n - L} < \varepsilon \) [11]. So this \( N \) works [12–14].

Written with the unbounded rules, the same derivation has 22 lines, since each of its six bounded steps (lines 4, 8, 13, 14, 15, and 16) costs one line more. The claim "\( \frac1n \to 0 \)" (for \( n \ge 1 \)) is not derived here: its proof needs a fact about \( \nN \) inside \( \nR \), the Archimedean property, which is a theorem of Chapter 11, not of logic.

## The search method, extended

Section 2.6 put the moves for the connectives in order. Each of Sections 4.3–4.7 added a step. Here is the method with all of them.

::: {.algorithm}
**Searching for a derivation of \( \Gamma \vdash \varphi \) in predicate logic.**

1. **Set up.** Write the premises \( \Gamma \) at the top and \( \varphi \) at the bottom, with one gap between. Translate any definition in words into a formula first, as in @exm-translate-limit.
2. **Goal-directed step.** Take the current goal's main symbol and set up its introduction rule:
   - \( \wedge \), \( \to \), \( \neg \), \( \leftrightarrow \): as in Section 2.6;
   - \( \forall x\, \psi \): open a **flagged box** with a fresh name \( x_0 \); the new goal, the box's last line, is \( \psi[x_0/x] \) (Section 4.4). For \( \forall x \in A\; \psi \), the box opens with the assumption \( x_0 \in A \);
   - \( \vee \): **postpone**, as in Section 2.6;
   - \( \exists x\, \psi \): **postpone**; work on the premises until an available line shows a term \( t \) with \( \psi[t/x] \), then use \( \rulename{\exists I} \) (Section 4.5). For \( \exists x \in A\; \psi \), the line \( t \in A \) is needed too.

   Repeat while the goal is \( \wedge \), \( \to \), \( \neg \), \( \leftrightarrow \), or \( \forall \).
3. **Premise-directed step.** Take the main symbol of a resource and apply its elimination rule:
   - \( \wedge \), \( \to \), \( \vee \), \( \leftrightarrow \), and the derived rules: as in Section 2.6;
   - \( \exists x\, \psi \): open the \( \rulename{\exists E} \) box **early**, as soon as the line is available, with a fresh witness \( x_0 \), and make its last line the current goal, which must not mention \( x_0 \) (Section 4.6). An early box lets the witness serve the goals that come later;
   - \( \forall x\, \psi \): do not instantiate blindly; instantiate at the term that the goal, or another resource, mentions (Section 4.3). For \( \forall x \in A\; \psi \), the line \( t \in A \) is needed too;
   - an equation \( t_1 = t_2 \): use \( \rulename{{=}E} \) with a \( \varphi \) chosen so that one substitution turns an available line into the goal, turning the equation round first if needed (Section 4.7).
4. **Clash.** As in Section 2.6: for the goal \( \bot \), find or manufacture a pair \( \chi \), \( \neg\chi \); an impossible case closes itself by \( \rulename{\bot E} \).
5. **Stuck.** As in Section 2.6: \( \rulename{RAA} \) on the current goal, or \( \rulename{LEM} \) on a well-chosen statement.

When no gap is left, number the lines and check the derivation as @def-derivation, extended in Section 4.4, says: every citation is available, and every side condition holds (\( t \) free for \( x \) at \( \rulename{\forall E} \) and \( \rulename{\exists I} \), bounded or not; \( t_1 \) and \( t_2 \) free for \( x \) at \( \rulename{{=}E} \); a fresh name at each line that closes a flagged box).
:::

Two of the new steps deserve a word on their place in the order. The goal step for \( \forall \) is safe in the same way as the goal steps for \( \to \) and \( \neg \) (Section 2.6): if \( \forall x\, \psi \) is derivable at all, then so is \( \psi[x_0/x] \) for a fresh \( x_0 \), by one more \( \rulename{\forall E} \); so opening the box loses nothing. The goal step for \( \exists \) is unsafe in the same way as the one for \( \vee \): a witness chosen too early may be the wrong one, as in @exm-existential-introduction-derivations, where "take \( y = c \)" stalled. That is why \( \exists \) is postponed and the \( \rulename{\exists E} \) boxes of the premises are opened early: the witnesses they supply are often the terms the postponed goal is waiting for, as \( N_0 \) was in the limit derivation above.

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

### B. Practice

::: {#exr-translation-b1}
[B1: Three definitions]

Formalize each statement, stating the domain and the kind of each symbol (variable, constant, function symbol, predicate symbol; membership \( \in A \) in a fixed set \( A \) is a one-place predicate symbol, as in Section 4.2).

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

*(c)* Domain \( \nR \); \( M \), \( n \) variables (bound); \( a \) a one-place function symbol (the one-domain convention of Section 4.1), and \( \abs{\cdot} \) a one-place function symbol; \( \in \nN \) a one-place and \( \le \) a two-place predicate symbol. \( \exists M\; \forall n \in \nN\; (\abs{a_n} \le M) \).

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

The only difference is the position of \( \forall x \in A \): in (a) it stands after \( \exists \delta > 0 \), in (b) before it. In (b) the defender chooses \( \delta \) knowing \( x \), so \( \delta \) may depend on \( x \) and on \( \varepsilon \); in (a) \( \delta \) is chosen before any \( x \) is given, so one \( \delta \) must serve every \( x \in A \) at once, and it depends on \( \varepsilon \) only. Section 4.10 derives (b) from (a) and shows that \( x^2 \) on \( \nR \) satisfies (b) but not (a); Section 4.11 turns this example into a counter-model, so (b) does not derive (a).
:::

::: {#exr-translation-c2}
[C2: Six orders, four statements]

Fix a formula \( \mu \) (the "matrix") in the variables \( x \), \( y \), \( z \), and consider the six sentences obtained by putting the prefixes \( \forall x \), \( \exists y \), \( \forall z \) in front of \( \mu \) in the six possible orders: \( \forall x\, \exists y\, \forall z\, \mu \), \( \forall z\, \exists y\, \forall x\, \mu \), and so on. Call two of these orders **essentially the same** if the two sentences are provably equivalent (\( \dashv\vdash \)) for every matrix \( \mu \), and **essentially different** if some matrix over \( \nZ \) gives them different truth values (read informally, as in Section 4.1).

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

*(b)* Call the groups F (\( \exists y \) first), L (last), \( M_x \) (\( \forall x\, \exists y\, \forall z \)) and \( M_z \) (\( \forall z\, \exists y\, \forall x \)). Over \( \nZ \), evaluate each group with the two matrices, reading informally (Section 4.1):

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

<!-- dependency ledger
exm-translate-limit (solution): p | n means n = p * k for some integer k | NOTATION.md row for d | n (definition, first used Ch 2); stated in the solution
exm-translate-limit (solution): (d) the two forms of "no largest prime" say the same thing over N; not (q <= p) iff p < q over N | order fact (school arithmetic); the logical part is Section 4.9 (later section of this chapter; prose pointer only, nothing here rests on it)
translation-check (solution): (0, 1) is bounded above by 1 (x < 1 for x in (0, 1)) and has no maximum (m < (m+1)/2 < 1 for m in (0, 1)) | school algebra (order); ch11 (prose pointer); checked by verify/ch04/exm-translate-limit.py
exm-translate-limit (claim, the opening list): 1, 1/2, 1/3, ... has terms not all close to any L; only eventually-L sequences satisfy the swapped form | informal reading, illustrative only; no result rests on it
exm-translate-limit (claim, the warning): f(x) = x is bounded by 1 on [0, 1] and not on R; a_n = n - 3 has a_0 = -3 and a_n > 0 for n >= 4 | school arithmetic; checked by verify/ch04/exm-translate-limit.py
prp-bounded-quantifier-rules (proof): (x in A -> phi)[t/x] is t in A -> phi[t/x]; t free for x in (x in A -> phi) iff t free for x in phi; likewise with x > a when x does not occur in a | def-substitution, def-free-for (cited); argued inline
prp-bounded-quantifier-rules (proof): moving lines into a new enclosing box keeps each citation available | def-derivation's scope rule (Ch 1, cited as def-derivation via Section 4.4's extension to flagged boxes); argued inline
prp-bounded-quantifier-rules (claim): a new rule is admissible if every use can be replaced by old steps | def-derived-rule (cited), extended; argued in the text
prp-bounded-quantifier-rules (example, the limit derivation): eps_0 > 0 gives eps_0/2 > 0; |a - L| < eps_0/2 gives |2a - 2L| < eps_0 since |2u - 2v| = 2|u - v| | arith lines (school algebra); ch11 (prose pointer for the Archimedean remark only)
prp-bounded-quantifier-rules (example, the limit derivation): the unbounded version has 22 lines | inline count: 16 lines + one per bounded step (six)
prp-bounded-quantifier-rules (claim, the search method): opening a forall box loses nothing: forall-E at a fresh name recovers psi[x_0/x] | inline, as in Section 2.6's argument for ->
exr-translation-a1 (solution): 7 not in {0}; no natural number exceeds every natural number; 1 divides every n | school arithmetic; checked by verify/ch04/exr-translation-a1.py
exr-translation-c2 (solution): exchange of adjacent foralls for any matrix | exm-universal-introduction-derivations (cited); its derivation uses nothing about R(x, y) but that it is a formula
exr-translation-c2 (solution): truth values over Z of the eight sentences in the table | informal truth, Section 4.1; witnesses y = x + 1, y = z + 1 given; checked by verify/ch04/exr-translation-c2.py
-->
