# Valuations and Truth Tables

Sections 3.1 and 3.2 made formulas into objects: every formula is built from atoms and \( \bot \) by the connectives in exactly one way, and so a function on formulas can be defined one clause per connective. So far a formula is only a string of symbols. It says nothing, and it is neither true nor false. This section gives formulas a meaning. We say what it takes to fix the truth or falsity of every atom, and then compute the truth value of every formula from the values of its atoms, one connective at a time. The result is the truth table, the second way of looking at a formula that Chapters 1 and 2 kept promising.

Throughout, formulas are those of @def-formula, with atoms \( p, q, r, p_1, p_2, \dots \), and we use Chapter 1's shorthand for them (outer parentheses dropped, the usual precedence, \( \to \) grouped to the right), as Section 3.1 allows.

## Reading a table off the rules

Before any definition, a question. Suppose we want to call each statement true or false, and we want the rules of Chapters 1 and 2 to be **safe**: whenever the lines a rule cites are true, the line it writes is true. How must "true" behave for each connective? The rules answer almost completely. This subsection is motivation only; nothing later rests on it, and Section 3.6 makes it exact.

*Conjunction.* Take statements \( \varphi \) and \( \psi \). If both are true, \( \rulename{\wedge I} \) writes \( \varphi \wedge \psi \) from them, so \( \varphi \wedge \psi \) must be true. If \( \varphi \wedge \psi \) is true, \( \rulename{\wedge E} \) writes \( \varphi \) and writes \( \psi \), so both must be true; turned around, if either of them is false, then \( \varphi \wedge \psi \) must be false. All four combinations of values are settled:
\[
\begin{array}{cc|c}
\varphi & \psi & \varphi \wedge \psi \\
\hline
\mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{T} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{T} & \mathrm{F} \\
\mathrm{F} & \mathrm{F} & \mathrm{F}
\end{array}
\]
Here \( \mathrm{T} \) stands for "true" and \( \mathrm{F} \) for "false".

*Contradiction.* The rule \( \rulename{\bot E} \) writes **any** statement from \( \bot \). If \( \bot \) were ever true, \( \rulename{\bot E} \) would lead from a true line to every statement, false ones included. So \( \bot \) must be false, always.

*Negation.* The rule \( \rulename{\neg E} \) writes \( \bot \) from \( \varphi \) and \( \neg\varphi \). Since \( \bot \) is false, \( \varphi \) and \( \neg\varphi \) are never both true: if \( \varphi \) is true, \( \neg\varphi \) is false. And @prp-excluded-middle derives \( \varphi \vee \neg\varphi \) from no premises at all, so at least one of the two is true: if \( \varphi \) is false, \( \neg\varphi \) is true. Negation flips the value.

*Implication.* The rule \( \rulename{{\to}E} \) writes \( \psi \) from \( \varphi \to \psi \) and \( \varphi \). So in the combination "\( \varphi \) true, \( \psi \) false", the implication cannot be true: that is the one row where \( \varphi \to \psi \) is false. The other three rows are forced by derivations. @prp-vacuous-implication derives \( P \to Q \) from \( \neg P \), so whenever \( P \) is false (and \( \neg P \) therefore true), \( P \to Q \) must be true, whatever \( Q \) is. And \( P \to Q \) is derivable from \( Q \) alone (@exr-proving-an-implication-b2 (a) of Section 1.5):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {Q}
  \open
  \hypo {2} {P}
  \have {3} {Q} \r{1}
  \close
  \have {4} {P \to Q} \ii{2-3}
\end{nd}$
\end{center}
```

so whenever \( Q \) is true, \( P \to Q \) must be true. That settles the rows with \( P \) false (by the first derivation) and the row with both true (by the second).

The vacuous rows of \( \to \), "if \( P \) is false, then \( P \to Q \) is true", are often presented as a convention to be swallowed. Here they are forced by \( \rulename{\bot E} \), the rule that closes an impossible case, exactly as Section 2.1 said they would be. The rows of \( \vee \) and \( \leftrightarrow \) can be read off their rules in the same way, and Exercise C1 below asks for a sharper version of the argument for \( \to \). We now turn the answers into a definition.

## Valuations

A formula such as \( p \wedge \neg q \) cannot be true or false on its own, because \( p \) and \( q \) are atoms: letters with no content. What decides its value is a choice of which atoms are true. We need a word for one such choice.

*A valuation is one possible situation, described by saying which atoms are true and which are false.*

::: {#def-valuation}
[Valuation]

A **valuation** \( v \) assigns to **every** atom \( p \) **exactly one** of the two truth values \( \mathrm{T} \) and \( \mathrm{F} \). We write \( v(p) \) for the value it assigns to \( p \), and say that \( p \) is **true under** \( v \) if \( v(p) = \mathrm{T} \), **false under** \( v \) if \( v(p) = \mathrm{F} \).
:::

In words: a valuation answers, for each atom separately, the question "true or false?", and it answers every such question. Two valuations are equal when they give every atom the same value. Nothing links the values of different atoms: \( v(p) \) and \( v(q) \) may be chosen freely, and that freedom is the whole point.

Some valuations, simplest first.

- The **all-T valuation** gives every atom the value \( \mathrm{T} \); the **all-F valuation** gives every atom \( \mathrm{F} \). They are the two extreme cases, and both will return as tests.
- The valuation with \( v(p) = \mathrm{T} \), \( v(q) = \mathrm{F} \) and \( v(r) = \mathrm{F} \) for every other atom \( r \). This is the typical way to describe a valuation: give the values of the few atoms we care about, and fix the rest once and for all.
- A valuation may treat infinitely many atoms differently: \( v(p_n) = \mathrm{T} \) for odd \( n \) and \( v(p_n) = \mathrm{F} \) for even \( n \), with every other atom false. Formulas are finite, so no formula will ever see more than finitely many of these values. Making this precise is the job of the lemma in the next subsection but one.

*Nonexample.* "\( p \) is true" and "\( p \) is false" together do not describe a valuation: the definition asks for **exactly one** value per atom. And a list that gives \( p \) the value \( \mathrm{T} \) and says nothing about the other atoms is not a valuation either, since it fails "every atom". We never need more than such a partial list, but we complete it (by \( \mathrm{F} \), say) so that the definition applies.

## The value of a formula

A valuation fixes the atoms. The value of every other formula should then follow, computed from the values of its parts by the tables of the first subsection. Since formulas are built by the clauses of @def-formula, this is a definition by recursion.

*The value of a formula is computed from the bottom of its parse tree upwards, one connective at a time.*

::: {#def-truth-value}
[Truth Value of a Formula]

Let \( v \) be a valuation. The **truth value** \( v(\varphi) \) of a formula \( \varphi \) **under** \( v \) is defined by recursion on \( \varphi \):

::: {.enumerate options="label=(V\arabic*)"}
1. for an atom \( p \), \( v(p) \) is the value the valuation assigns to \( p \); and \( v(\bot) \coloneqq \mathrm{F} \);
2. \( v(\neg\varphi) \coloneqq \mathrm{T} \) if \( v(\varphi) = \mathrm{F} \), and \( v(\neg\varphi) \coloneqq \mathrm{F} \) if \( v(\varphi) = \mathrm{T} \);
3. \( v(\varphi \wedge \psi) \coloneqq \mathrm{T} \) if \( v(\varphi) = \mathrm{T} \) **and** \( v(\psi) = \mathrm{T} \); otherwise \( \mathrm{F} \);
4. \( v(\varphi \vee \psi) \coloneqq \mathrm{T} \) if \( v(\varphi) = \mathrm{T} \) **or** \( v(\psi) = \mathrm{T} \) (or both); otherwise \( \mathrm{F} \);
5. \( v(\varphi \to \psi) \coloneqq \mathrm{F} \) if \( v(\varphi) = \mathrm{T} \) and \( v(\psi) = \mathrm{F} \); otherwise \( \mathrm{T} \);
6. \( v(\varphi \leftrightarrow \psi) \coloneqq \mathrm{T} \) if \( v(\varphi) = v(\psi) \); otherwise \( \mathrm{F} \).
:::

We say \( \varphi \) is **true under** \( v \), or \( v \) **makes** \( \varphi \) true, if \( v(\varphi) = \mathrm{T} \); otherwise \( \varphi \) is **false under** \( v \).
:::

Clauses (V2)–(V6) say that the value of a compound formula depends **only** on the values of its immediate parts, and they are summed up in the tables of the five connectives:
\[
\begin{array}{c|c}
\varphi & \neg\varphi \\
\hline
\mathrm{T} & \mathrm{F} \\
\mathrm{F} & \mathrm{T}
\end{array}
\qquad
\begin{array}{cc|cccc}
\varphi & \psi & \varphi \wedge \psi & \varphi \vee \psi & \varphi \to \psi & \varphi \leftrightarrow \psi \\
\hline
\mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} \\
\mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T}
\end{array}
\]

Read them clause by clause. (V1): an atom has the value the valuation gives it, and \( \bot \) is false under every valuation. (V2): negation flips. (V3): a conjunction needs both parts. (V4): a disjunction needs at least one part; "or" is **inclusive**, as the rule \( \rulename{\vee I} \) of Section 1.6 already said, so the row with both parts true gives \( \mathrm{T} \). (V5): an implication is false in exactly one case, a true hypothesis with a false conclusion. (V6): a biconditional says the two sides agree.

The columns for \( \neg \), \( \wedge \) and \( \to \), and the value of \( \bot \), are the ones the first subsection read off the rules. Section 3.6 proves that every row of every table is, in a precise sense, a derivable sequent.

**Well defined.** Clause (V1) gives a value to every atom and to \( \bot \), and each of (V2)–(V6) gives a rule computing the value of a compound formula from the values of its immediate parts. By @thm-structural-recursion, such clauses define exactly one function on all formulas. This is what Section 3.2 was for. Without unique readability a formula could be split into immediate parts in two ways, and the two splittings could give two values. The string \( p \wedge q \vee r \), with no parentheses and no convention, shows the danger: its two readings are \( (p \wedge q) \vee r \) and \( p \wedge (q \vee r) \), and under a valuation with \( v(p) = \mathrm{F} \), \( v(q) = \mathrm{F} \) and \( v(r) = \mathrm{T} \),
\[
v\bigl( (p \wedge q) \vee r \bigr) = \mathrm{T}, \qquad v\bigl( p \wedge (q \vee r) \bigr) = \mathrm{F} .
\]
In the first, \( p \wedge q \) is \( \mathrm{F} \) and \( r \) is \( \mathrm{T} \), so the disjunction is \( \mathrm{T} \). In the second, \( q \vee r \) is \( \mathrm{T} \) but \( p \) is \( \mathrm{F} \), so the conjunction is \( \mathrm{F} \). A formula of @def-formula carries its parentheses, and has one value.

::: {#exm-value-down-the-tree}
[Computing a value]

Let \( v \) be a valuation with \( v(p) = \mathrm{F} \), \( v(q) = \mathrm{T} \) and \( v(r) = \mathrm{F} \). Compute \( v(\varphi) \) for
\[
\varphi = (p \vee \neg q) \to (q \wedge r) .
\]
:::

::: {.solution}
Work from the leaves of the parse tree up to its root, one node at a time, each time using one clause of @def-truth-value. List the subformulas so that each comes after its immediate parts:

| Subformula | Clause | Value |
|---|---|---|
| \( p \), \( q \), \( r \) | (V1) | \( \mathrm{F} \), \( \mathrm{T} \), \( \mathrm{F} \) |
| \( \neg q \) | (V2): \( v(q) = \mathrm{T} \) | \( \mathrm{F} \) |
| \( p \vee \neg q \) | (V4): both parts \( \mathrm{F} \) | \( \mathrm{F} \) |
| \( q \wedge r \) | (V3): \( v(r) = \mathrm{F} \) | \( \mathrm{F} \) |
| \( (p \vee \neg q) \to (q \wedge r) \) | (V5): the hypothesis is \( \mathrm{F} \) | \( \mathrm{T} \) |

So \( v(\varphi) = \mathrm{T} \). The last step did not need the value of \( q \wedge r \): a false hypothesis makes an implication true whatever its conclusion is. Computing by hand, one may stop a branch as soon as its value is decided.
:::

*Nonexample.* The rule "every formula gets the value \( \mathrm{T} \)" agrees with the all-T valuation on every atom, but it is not the truth value of @def-truth-value under any valuation. It breaks (V1) at \( \bot \), and it breaks (V2) at \( \neg p \), where \( p \) and \( \neg p \) would both be \( \mathrm{T} \). The truth value under the all-T valuation is the function that (V1)–(V6) produce from it, and it makes \( \neg p \) false.

::: {.warning}
Values do not distribute over connectives the way symbols seem to. The value of \( \neg(p \wedge q) \) is not computed by negating \( p \) and \( q \) and keeping the \( \wedge \): under a valuation with \( v(p) = \mathrm{T} \) and \( v(q) = \mathrm{F} \), the formula \( \neg(p \wedge q) \) is \( \mathrm{T} \) (since \( p \wedge q \) is \( \mathrm{F} \)), while \( \neg p \wedge \neg q \) is \( \mathrm{F} \) (since \( \neg p \) is \( \mathrm{F} \)). Always follow the parse tree: the main connective is applied last.
:::

::: {.check}
Let \( v(p) = \mathrm{F} \), \( v(q) = \mathrm{T} \), \( v(r) = \mathrm{T} \). What is \( v\bigl( (p \vee q) \to \neg r \bigr) \)?
:::

::: {.solution}
\( \mathrm{F} \). Bottom up: \( p \vee q \) is \( \mathrm{T} \), by (V4), since \( q \) is \( \mathrm{T} \); \( \neg r \) is \( \mathrm{F} \), by (V2); and an implication with a true hypothesis and a false conclusion is \( \mathrm{F} \), by (V5).
:::

## Only the atoms of a formula matter

A valuation fixes infinitely many values, but a formula contains only finitely many atoms. We expect the value of a formula to depend only on the values of its own atoms. That is the fact that makes truth tables finite, and it is our first proof by structural induction about meaning.

Recall from Section 3.2 that \( \atoms(\varphi) \), the set of atoms occurring in \( \varphi \), is defined by recursion: \( \atoms(p) = \{ p \} \) for an atom \( p \), \( \atoms(\bot) \) is empty, \( \atoms(\neg\varphi) = \atoms(\varphi) \), and the atoms of \( \varphi \circ \psi \), for each binary connective \( \circ \), are those of \( \varphi \) together with those of \( \psi \). Two valuations \( v \) and \( w \) **agree on** a set of atoms if \( v(p) = w(p) \) for every atom \( p \) in it.

::: {#lem-coincidence}
[Coincidence Lemma]

Let \( \varphi \) be a formula, and let \( v \) and \( w \) be valuations that agree on \( \atoms(\varphi) \). Then \( v(\varphi) = w(\varphi) \).
:::

::: {.idea}
Structural induction on \( \varphi \), with the property "for **all** valuations \( v \), \( w \) that agree on the atoms of \( \varphi \), \( v(\varphi) = w(\varphi) \)". At an atom, the two valuations agree by hypothesis. At a compound formula, both values are computed by the same clause from the values of the immediate parts, and the parts have fewer atoms to disagree on, so the hypothesis for the parts applies.
:::

::: {.proof}
We apply @thm-structural-induction to the property \( C(\varphi) \): *for all valuations \( v \) and \( w \) that agree on \( \atoms(\varphi) \), \( v(\varphi) = w(\varphi) \).*

*Atoms.* Let \( p \) be an atom and let \( v \), \( w \) agree on \( \atoms(p) = \{ p \} \). Then \( v(p) = w(p) \), which is \( C(p) \).

*\( \bot \).* By (V1), \( v(\bot) = \mathrm{F} = w(\bot) \) for all valuations \( v \), \( w \). So \( C(\bot) \) holds.

*Negation.* Assume \( C(\varphi) \), and let \( v \), \( w \) agree on \( \atoms(\neg\varphi) \). Since \( \atoms(\neg\varphi) = \atoms(\varphi) \), they agree on \( \atoms(\varphi) \), so \( v(\varphi) = w(\varphi) \) by \( C(\varphi) \). By (V2), \( v(\neg\varphi) \) is determined by \( v(\varphi) \) and \( w(\neg\varphi) \) by \( w(\varphi) \) through the same rule, so \( v(\neg\varphi) = w(\neg\varphi) \). This proves \( C(\neg\varphi) \).

*Conjunction.* Assume \( C(\varphi) \) and \( C(\psi) \), and let \( v \), \( w \) agree on \( \atoms(\varphi \wedge \psi) \). Every atom of \( \varphi \) is an atom of \( \varphi \wedge \psi \), so \( v \) and \( w \) agree on \( \atoms(\varphi) \), and \( v(\varphi) = w(\varphi) \) by \( C(\varphi) \). In the same way \( v(\psi) = w(\psi) \) by \( C(\psi) \). By (V3), \( v(\varphi \wedge \psi) = \mathrm{T} \) exactly when \( v(\varphi) = v(\psi) = \mathrm{T} \), that is, exactly when \( w(\varphi) = w(\psi) = \mathrm{T} \), that is, exactly when \( w(\varphi \wedge \psi) = \mathrm{T} \). Hence \( v(\varphi \wedge \psi) = w(\varphi \wedge \psi) \), which is \( C(\varphi \wedge \psi) \).

*Disjunction.* Assume \( C(\varphi) \) and \( C(\psi) \), and let \( v \), \( w \) agree on \( \atoms(\varphi \vee \psi) \). As in the previous case, \( v(\varphi) = w(\varphi) \) and \( v(\psi) = w(\psi) \). By (V4), \( v(\varphi \vee \psi) = \mathrm{T} \) exactly when one of \( v(\varphi) \), \( v(\psi) \) is \( \mathrm{T} \), that is, when one of \( w(\varphi) \), \( w(\psi) \) is \( \mathrm{T} \), that is, when \( w(\varphi \vee \psi) = \mathrm{T} \). So \( C(\varphi \vee \psi) \).

*Implication.* Assume \( C(\varphi) \) and \( C(\psi) \), and let \( v \), \( w \) agree on \( \atoms(\varphi \to \psi) \). Again \( v(\varphi) = w(\varphi) \) and \( v(\psi) = w(\psi) \). By (V5), \( v(\varphi \to \psi) = \mathrm{F} \) exactly when \( v(\varphi) = \mathrm{T} \) and \( v(\psi) = \mathrm{F} \), that is, when \( w(\varphi) = \mathrm{T} \) and \( w(\psi) = \mathrm{F} \), that is, when \( w(\varphi \to \psi) = \mathrm{F} \). So \( C(\varphi \to \psi) \).

*Biconditional.* Assume \( C(\varphi) \) and \( C(\psi) \), and let \( v \), \( w \) agree on \( \atoms(\varphi \leftrightarrow \psi) \). Again \( v(\varphi) = w(\varphi) \) and \( v(\psi) = w(\psi) \). By (V6), \( v(\varphi \leftrightarrow \psi) = \mathrm{T} \) exactly when \( v(\varphi) = v(\psi) \), that is, when \( w(\varphi) = w(\psi) \), that is, when \( w(\varphi \leftrightarrow \psi) = \mathrm{T} \). So \( C(\varphi \leftrightarrow \psi) \).

Every clause of @def-formula has been covered, so by @thm-structural-induction, \( C(\varphi) \) holds for every formula \( \varphi \). This proves the lemma.
:::

The four binary cases are the same argument four times: the values of the parts agree, and one clause turns equal inputs into equal outputs. Here they are written out so that the pattern can be seen in full; later proofs write such a repeated case once, and say which cases it stands for.

Two consequences. First, to know \( v(\varphi) \) we need only the values of \( v \) on the finitely many atoms of \( \varphi \): if \( \varphi \) has \( n \) atoms, it has at most \( 2^n \) different "situations", one for each way of giving its atoms the values \( \mathrm{T} \) and \( \mathrm{F} \). (Each atom has two choices, and the choices are independent, so the number of ways doubles with each new atom: \( 2, 4, 8, \dots, 2^n \). This count is itself a small induction on \( n \), by @ax-induction.) Second, the extra atoms a valuation happens to fix are irrelevant: two valuations that differ only on atoms not in \( \varphi \) give \( \varphi \) the same value.

::: {.check}
Let \( \varphi = p \to (q \vee p) \). Two valuations \( v \) and \( w \) agree on \( p \) and \( q \) but disagree on \( r \) and on every \( p_n \). What does @lem-coincidence say about \( v(\varphi) \) and \( w(\varphi) \)? Does it say anything about \( v(\varphi \wedge r) \) and \( w(\varphi \wedge r) \)?
:::

::: {.solution}
\( \atoms(\varphi) = \{ p, q \} \), and \( v \), \( w \) agree there, so \( v(\varphi) = w(\varphi) \). For \( \varphi \wedge r \) the atoms are \( p \), \( q \), \( r \), and the valuations disagree on \( r \), so the lemma does not apply. Indeed the values can differ: \( \varphi \) is true under every valuation (if \( p \) is true, so is \( q \vee p \)), so \( v(\varphi \wedge r) = v(r) \) and \( w(\varphi \wedge r) = w(r) \), which differ.
:::

## Truth tables

@lem-coincidence says that a formula's value is decided by finitely many choices, and so it can be tabulated once and for all.

*A truth table lists the value of a formula in every possible situation, one row per way of giving its atoms values.*

::: {#def-truth-table}
[Truth Table]

Let \( \varphi \) be a formula and let \( p_1, \dots, p_n \) be a list of distinct atoms that **includes every atom of** \( \varphi \). A **row** is an assignment of a truth value to each of \( p_1, \dots, p_n \). The **truth table** of \( \varphi \) (on \( p_1, \dots, p_n \)) lists, for each of the \( 2^n \) rows, the value \( v(\varphi) \) for a valuation \( v \) that **agrees with the row** on \( p_1, \dots, p_n \). We say \( \varphi \) is true (or false) **in** the row.
:::

*Well defined.* Two things must be checked. **Existence:** every row comes from a valuation, for instance the one that gives \( p_1, \dots, p_n \) the row's values and every other atom \( \mathrm{F} \). **Independence of the choice:** two valuations that agree with the same row agree on \( p_1, \dots, p_n \), hence on \( \atoms(\varphi) \), so by @lem-coincidence they give \( \varphi \) the same value. Without the lemma, "the value in a row" would not make sense, since a row says nothing about the infinitely many other atoms.

The list \( p_1, \dots, p_n \) is allowed to contain atoms that do not occur in \( \varphi \); then pairs of rows that differ only there show the same value. This freedom lets us compare several formulas in one table, over the atoms of all of them, and Section 3.4 does that constantly. When \( \varphi \) has no atoms at all, as \( \neg\bot \) or \( \bot \to \bot \) do, the list may be empty, and the table has \( 2^0 = 1 \) row: such a formula has the same value under every valuation.

**Conventions.** The atom columns come first. The rows are listed with \( \mathrm{T} \) before \( \mathrm{F} \), the last atom alternating fastest: for two atoms, TT, TF, FT, FF. In practice we add a column for each subformula, building up to \( \varphi \) in the order of the parse tree, as in @exm-value-down-the-tree, but now for every row at once.

::: {#exm-truth-table-modus-ponens}
[The truth table of modus ponens]

Make the truth table of \( ((p \to q) \wedge p) \to q \) on \( p, q \), and read off from it what \( \rulename{{\to}E} \) does.
:::

::: {.solution}
Columns for the two atoms, then for each subformula in turn:
\[
\begin{array}{cc|ccc}
p & q & p \to q & (p \to q) \wedge p & ((p \to q) \wedge p) \to q \\
\hline
\mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{T} \\
\mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{T} \\
\mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{T}
\end{array}
\]
The third column is (V5): \( \mathrm{F} \) only in the row TF. The fourth is (V3) applied to the third column and the \( p \) column: \( \mathrm{T} \) only in the first row. The last is (V5) again, with the fourth column as hypothesis and \( q \) as conclusion: the hypothesis is false in rows 2–4, so those rows are \( \mathrm{T} \), and in row 1 the conclusion \( q \) is \( \mathrm{T} \).

So the formula is true in every row. Read as a statement about \( \rulename{{\to}E} \): the only row in which both given lines \( p \to q \) and \( p \) are true is row 1, and in that row the line the rule writes, \( q \), is true as well. The rule never leads from true lines to a false one, at least when its lines are atoms. Section 3.5 proves this for every rule and every formula.
:::

Now a table built column by column for a biconditional, whose two sides Chapter 2 related by derivations.

::: {#exm-table-contrapositive}
[An implication and its contrapositive]

Make the truth table of \( (p \to q) \leftrightarrow (\neg q \to \neg p) \).
:::

::: {.solution}
\[
\begin{array}{cc|ccccc}
p & q & p \to q & \neg q & \neg p & \neg q \to \neg p & (p \to q) \leftrightarrow (\neg q \to \neg p) \\
\hline
\mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} \\
\mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} \\
\mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T}
\end{array}
\]
The columns \( p \to q \) and \( \neg q \to \neg p \) are identical: each is \( \mathrm{F} \) only in row 2. For \( \neg q \to \neg p \) that is the row where the hypothesis \( \neg q \) is \( \mathrm{T} \) and the conclusion \( \neg p \) is \( \mathrm{F} \), that is, \( q \) false and \( p \) true, which is the same row TF. So the biconditional is \( \mathrm{T} \) in every row.

Compare Chapter 2. There @prp-contrapositive derived \( \neg Q \to \neg P \) from \( P \to Q \) with the rules for implication and negation, and @prp-contrapositive-converse derived the way back with a derivation that uses \( \rulename{RAA} \). The table sees no difference between the two directions; it only sees that the two columns agree. What a table can and cannot tell about derivations is the subject of Sections 3.5 and 3.6.
:::

A table with \( n \) atoms has \( 2^n \) rows, so three atoms give 8 and five give 32. Often we do not need all of them.

::: {#exm-backwards-from-f}
[Working backwards from F]

Find every row in which
\[
\varphi = (p \to q) \to \bigl( p \to (q \wedge r) \bigr)
\]
is false: first with the full table on \( p, q, r \), then without it.
:::

::: {.solution}
*The full table.*
\[
\begin{array}{ccc|cccc}
p & q & r & p \to q & q \wedge r & p \to (q \wedge r) & (p \to q) \to (p \to (q \wedge r)) \\
\hline
\mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} \\
\mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{T} \\
\mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{T} \\
\mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{T} \\
\mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{T} \\
\mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{T}
\end{array}
\]
The formula is false in exactly one row, row 2: \( p \) and \( q \) true, \( r \) false.

*Backwards from F.* An implication is false in exactly one way, by (V5): hypothesis true, conclusion false. Apply that to the main connective of \( \varphi \), and then to whatever it forces.

1. \( \varphi \) is \( \mathrm{F} \) exactly when \( p \to q \) is \( \mathrm{T} \) and \( p \to (q \wedge r) \) is \( \mathrm{F} \).
2. \( p \to (q \wedge r) \) is \( \mathrm{F} \) exactly when \( p \) is \( \mathrm{T} \) and \( q \wedge r \) is \( \mathrm{F} \).
3. With \( p \) true, \( p \to q \) is \( \mathrm{T} \) exactly when \( q \) is \( \mathrm{T} \).
4. With \( q \) true, \( q \wedge r \) is \( \mathrm{F} \) exactly when \( r \) is \( \mathrm{F} \).

Each step was forced, so there is exactly one row making \( \varphi \) false: \( p = \mathrm{T} \), \( q = \mathrm{T} \), \( r = \mathrm{F} \). Four short steps replace eight rows.
:::

The second method has a name in this book: **working backwards from F**. Assume the formula is false, and ask what each part is forced to be, starting from the main connective. Implications and disjunctions are false in only one way, and conjunctions are true in only one way, so they force values; a false conjunction, a true disjunction, or a true implication leaves a choice, and then we split into cases. If the forcing ends in a contradiction (some atom would need both values), the formula is false in **no** row. If it ends in a consistent assignment, that assignment is a row making the formula false, and the cases that were split give all such rows.

::: {.warning}
A truth table sees only the connectives. Everything inside an atom is invisible to it. The statement "for every real \( x \), if \( x > 2 \), then \( x^2 > 4 \)" is true, but its propositional form, with the atoms \( a \): "\( x > 2 \)" and \( b \): "\( x^2 > 4 \)", is \( a \to b \), which is false in the row with \( a \) true and \( b \) false. That row cannot happen for real numbers, and the reason lies in algebra, not in the connectives. Likewise "for every \( \varepsilon > 0 \) there is an \( N \) such that …" is a single atom for a truth table, with two rows and nothing to compute. Chapter 4 looks inside atoms.
:::

::: {.check}
Why does @def-truth-table need @lem-coincidence? What would go wrong in a table for \( p \vee q \) if the value of \( p \vee q \) could depend on the atom \( r \)?
:::

::: {.solution}
A row gives values to the listed atoms only, and many valuations agree with it, differing on the other atoms. The table records "the" value of the formula in the row, so all those valuations must give the same value; @lem-coincidence guarantees it. If \( v(p \vee q) \) could depend on \( r \), the row \( p = \mathrm{F} \), \( q = \mathrm{F} \) would contain valuations giving different values, and there would be no single entry to write.
:::

## Exercises

### A. Check your understanding

::: {#exr-valuations-and-truth-tables-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Make the truth tables of \( \neg(p \wedge \neg q) \) and of \( (p \vee q) \to p \).
2. Make the truth table of \( p \leftrightarrow \neg p \). Is it true in any row?
3. Compute the value of \( (p \to \bot) \vee (\bot \to p) \) under the all-F valuation, and under the all-T valuation.
4. How many rows has the truth table of a formula on the atoms \( p, q, r, s \)?
5. True or false, with a reason: if \( v(p) \ne w(p) \), then \( v(p \to (q \to p)) \ne w(p \to (q \to p)) \).
:::
:::

::: {.solution}
(a)
\[
\begin{array}{cc|ccc}
p & q & \neg q & p \wedge \neg q & \neg(p \wedge \neg q) \\
\hline
\mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} \\
\mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} \\
\mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} \\
\mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{T}
\end{array}
\qquad
\begin{array}{cc|cc}
p & q & p \vee q & (p \vee q) \to p \\
\hline
\mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{T} \\
\mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} \\
\mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{T}
\end{array}
\]
The first formula has the same column as \( p \to q \): false only in row TF.

*(b)* In the row \( p = \mathrm{T} \), \( \neg p \) is \( \mathrm{F} \), and in the row \( p = \mathrm{F} \), \( \neg p \) is \( \mathrm{T} \); the two sides always differ, so by (V6) the formula is \( \mathrm{F} \) in both rows. It is true in no row.
\[
\begin{array}{c|cc}
p & \neg p & p \leftrightarrow \neg p \\
\hline
\mathrm{T} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{T} & \mathrm{F}
\end{array}
\]

*(c)* The disjunct \( \bot \to p \) has a false hypothesis, since \( v(\bot) = \mathrm{F} \) under every valuation (V1), so it is \( \mathrm{T} \) by (V5), and the disjunction is \( \mathrm{T} \) by (V4). This holds under both valuations (and under every other).

*(d)* \( 2^4 = 16 \).

*(e)* False. The formula \( p \to (q \to p) \) is true under every valuation: if \( v(p) = \mathrm{F} \), the hypothesis is false; if \( v(p) = \mathrm{T} \), the conclusion \( q \to p \) has a true conclusion. So \( v \) and \( w \) give it the value \( \mathrm{T} \) however they differ. @lem-coincidence says that agreement on the atoms forces agreement on the formula; it says nothing in the other direction.
:::

### B. Practice

::: {#exr-valuations-and-truth-tables-b1}
[B1: Backwards from F]

For each formula, work backwards from F to find every row on its atoms in which it is false, or show that there is none.

::: {.enumerate options="label=(\alph*)"}
1. \( \bigl( (p \vee q) \wedge ((p \to r) \wedge (q \to r)) \bigr) \to r \).
2. \( \bigl( p \to (q \to r) \bigr) \to \bigl( (p \to q) \to (p \to r) \bigr) \).
3. \( \bigl( (p \to r) \vee (q \to r) \bigr) \to \bigl( (p \vee q) \to r \bigr) \).
4. \( \bigl( (p \to q) \wedge (q \to r) \bigr) \to (r \to p) \).
:::
:::

::: {.solution}
*(a)* Suppose the formula is \( \mathrm{F} \). Then \( r \) is \( \mathrm{F} \), and the hypothesis is \( \mathrm{T} \), so each of \( p \vee q \), \( p \to r \), \( q \to r \) is \( \mathrm{T} \) (V3). With \( r \) false, \( p \to r \) true forces \( p = \mathrm{F} \), and \( q \to r \) true forces \( q = \mathrm{F} \). Then \( p \vee q \) is \( \mathrm{F} \), a contradiction. So the formula is false in no row. It is the table's version of proof by cases: if \( r \) follows from each of \( p \) and \( q \), and one of them holds, then \( r \) holds.

*(b)* Suppose it is \( \mathrm{F} \). Then \( p \to (q \to r) \) is \( \mathrm{T} \) and \( (p \to q) \to (p \to r) \) is \( \mathrm{F} \); the latter forces \( p \to q \) to be \( \mathrm{T} \) and \( p \to r \) to be \( \mathrm{F} \), and the last forces \( p = \mathrm{T} \), \( r = \mathrm{F} \). Then \( p \to q \) true with \( p \) true forces \( q = \mathrm{T} \). Now \( p \to (q \to r) \) has a true hypothesis and the conclusion \( q \to r \), which is \( \mathrm{F} \) (true \( q \), false \( r \)), so it is \( \mathrm{F} \), a contradiction. False in no row.

*(c)* Suppose it is \( \mathrm{F} \). Then \( (p \vee q) \to r \) is \( \mathrm{F} \): \( r = \mathrm{F} \) and \( p \vee q \) is \( \mathrm{T} \). And \( (p \to r) \vee (q \to r) \) is \( \mathrm{T} \): with \( r \) false, \( p \to r \) is \( \mathrm{T} \) exactly when \( p = \mathrm{F} \), and \( q \to r \) exactly when \( q = \mathrm{F} \); so at least one of \( p \), \( q \) is \( \mathrm{F} \). Together with \( p \vee q \) true: exactly one of \( p \), \( q \) is \( \mathrm{T} \). This leaves a choice, so split. The formula is false in exactly two rows: \( p = \mathrm{T}, q = \mathrm{F}, r = \mathrm{F} \) and \( p = \mathrm{F}, q = \mathrm{T}, r = \mathrm{F} \). Check the first: \( q \to r \) is \( \mathrm{T} \), so the hypothesis is \( \mathrm{T} \); \( p \vee q \) is \( \mathrm{T} \) and \( r \) is \( \mathrm{F} \), so the conclusion is \( \mathrm{F} \).

*(d)* Suppose it is \( \mathrm{F} \). Then \( r \to p \) is \( \mathrm{F} \): \( r = \mathrm{T} \), \( p = \mathrm{F} \). The hypothesis must be \( \mathrm{T} \): \( p \to q \) is \( \mathrm{T} \) because \( p \) is \( \mathrm{F} \), and \( q \to r \) is \( \mathrm{T} \) because \( r \) is \( \mathrm{T} \), whatever \( q \) is. Nothing forces \( q \). So the formula is false in exactly two rows: \( p = \mathrm{F} \), \( r = \mathrm{T} \), and \( q \) either value.
:::

::: {#exr-valuations-and-truth-tables-b2}
[B2: Counting atoms, the last step blank]

Call a formula **binary-built** if it is built from atoms by the four binary connectives only, so that neither \( \neg \) nor \( \bot \) occurs in it; the immediate parts of a binary-built formula are again binary-built. Define by recursion (@thm-structural-recursion) the number \( \mathrm{occ}(\varphi) \) of atom occurrences and the number \( \mathrm{bin}(\varphi) \) of binary connectives:
\[
\begin{aligned}
\mathrm{occ}(p) &= 1, & \mathrm{occ}(\varphi \circ \psi) &= \mathrm{occ}(\varphi) + \mathrm{occ}(\psi), \\
\mathrm{bin}(p) &= 0, & \mathrm{bin}(\varphi \circ \psi) &= \mathrm{bin}(\varphi) + \mathrm{bin}(\psi) + 1,
\end{aligned}
\]
for every atom \( p \) and every binary connective \( \circ \). (For \( \bot \) and \( \neg \) give both functions any values; they play no part below.) Here is a proof, by @thm-structural-induction, that every binary-built formula \( \varphi \) has
\[
\mathrm{occ}(\varphi) = \mathrm{bin}(\varphi) + 1 .
\]
The property is \( C(\varphi) \): *if \( \varphi \) is binary-built, then \( \mathrm{occ}(\varphi) = \mathrm{bin}(\varphi) + 1 \).*

*\( \bot \) and negation.* Neither \( \bot \) nor a formula \( \neg\varphi \) is binary-built, so \( C \) holds for them: its "if" is never met.

*Atoms.* \( \mathrm{occ}(p) = 1 = 0 + 1 = \mathrm{bin}(p) + 1 \).

*Conjunction.* Assume \( C(\varphi) \) and \( C(\psi) \), and let \( \varphi \wedge \psi \) be binary-built. Then \( \varphi \) and \( \psi \) are binary-built, so
\[
\begin{aligned}
\mathrm{occ}(\varphi \wedge \psi) &= \mathrm{occ}(\varphi) + \mathrm{occ}(\psi) = \bigl( \mathrm{bin}(\varphi) + 1 \bigr) + \bigl( \mathrm{bin}(\psi) + 1 \bigr) \\
&= \bigl( \mathrm{bin}(\varphi) + \mathrm{bin}(\psi) + 1 \bigr) + 1 = \mathrm{bin}(\varphi \wedge \psi) + 1 .
\end{aligned}
\]

*Disjunction and biconditional.* The computation is the same with \( \vee \), and with \( \leftrightarrow \), in place of \( \wedge \).

*Implication.* ______

*Name the move, then complete it.*
:::

::: {.solution}
The move is **induction on the shape of a formula** (@thm-structural-induction): the case for a compound formula uses the property for its immediate parts, and nothing else.

*Implication.* Assume \( C(\varphi) \) and \( C(\psi) \), and let \( \varphi \to \psi \) be binary-built. Its immediate parts \( \varphi \) and \( \psi \) are binary-built, so \( \mathrm{occ}(\varphi) = \mathrm{bin}(\varphi) + 1 \) and \( \mathrm{occ}(\psi) = \mathrm{bin}(\psi) + 1 \). Hence
\[
\begin{aligned}
\mathrm{occ}(\varphi \to \psi) &= \mathrm{occ}(\varphi) + \mathrm{occ}(\psi) = \bigl( \mathrm{bin}(\varphi) + 1 \bigr) + \bigl( \mathrm{bin}(\psi) + 1 \bigr) \\
&= \bigl( \mathrm{bin}(\varphi) + \mathrm{bin}(\psi) + 1 \bigr) + 1 = \mathrm{bin}(\varphi \to \psi) + 1 ,
\end{aligned}
\]
which is \( C(\varphi \to \psi) \). All clauses of @def-formula are covered, so @thm-structural-induction gives \( C(\varphi) \) for every formula, and in particular the equation for every binary-built formula.

For instance \( (p \to q) \wedge (p \vee r) \) has four atom occurrences (\( p \) counted twice) and three binary connectives.
:::

::: {#exr-valuations-and-truth-tables-b3}
[B3: A table for a named pattern]

Make the truth table of \( \bigl( (p \vee q) \wedge \neg p \bigr) \to q \), and say which derived rule of Chapter 2 it corresponds to, as @exm-truth-table-modus-ponens did for \( \rulename{{\to}E} \).
:::

::: {.solution}
\[
\begin{array}{cc|cccc}
p & q & p \vee q & \neg p & (p \vee q) \wedge \neg p & ((p \vee q) \wedge \neg p) \to q \\
\hline
\mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} \\
\mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} \\
\mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{T}
\end{array}
\]
True in every row. The only row in which both \( p \vee q \) and \( \neg p \) are true is row 3, and there \( q \) is true. This is disjunctive syllogism, \( \rulename{DS} \) (@prp-disjunctive-syllogism): from \( P \vee Q \) and \( \neg P \), infer \( Q \).
:::

### C. Going deeper

::: {#exr-valuations-and-truth-tables-c1}
[C1: The rows of implication are forced]

Pretend we do not know the table of \( \to \). Say only that there is **some** table: a rule \( t \) giving a truth value \( t(a, b) \) for each pair of truth values \( a, b \), with
\[
v(\varphi \to \psi) = t\bigl( v(\varphi), v(\psi) \bigr)
\]
for every valuation \( v \) and all formulas \( \varphi \), \( \psi \). (The other connectives keep their clauses.) Suppose the two rules for implication preserve truth in the following sense.

- (E) For every valuation \( v \) and all formulas \( \varphi, \psi \): if \( v(\varphi \to \psi) = \mathrm{T} \) and \( v(\varphi) = \mathrm{T} \), then \( v(\psi) = \mathrm{T} \).
- (I) For every list of formulas \( \Gamma \) and all formulas \( \varphi, \psi \): if every valuation that makes all of \( \Gamma \) and \( \varphi \) true makes \( \psi \) true, then every valuation that makes all of \( \Gamma \) true makes \( \varphi \to \psi \) true.

Prove that \( t \) is the table of (V5): \( t(\mathrm{T}, \mathrm{F}) = \mathrm{F} \), and \( t(a, b) = \mathrm{T} \) for the other three pairs.
:::

::: {.solution}
[Hint 1]

Each of the four values of \( t \) is one instance of (E) or of (I), with atoms for \( \varphi \) and \( \psi \) and a well-chosen valuation.
:::

::: {.solution}
[Hint 2]

For \( t(\mathrm{T}, \mathrm{T}) \) and \( t(\mathrm{F}, \mathrm{F}) \), try (I) with \( \Gamma \) empty and \( \varphi = \psi = p \).
:::

::: {.solution}
Let \( p \) and \( q \) be distinct atoms.

*\( t(\mathrm{T}, \mathrm{F}) = \mathrm{F} \).* Take a valuation \( v \) with \( v(p) = \mathrm{T} \), \( v(q) = \mathrm{F} \). If \( t(\mathrm{T}, \mathrm{F}) \) were \( \mathrm{T} \), then \( v(p \to q) = t(\mathrm{T}, \mathrm{F}) = \mathrm{T} \) and \( v(p) = \mathrm{T} \), so (E) would give \( v(q) = \mathrm{T} \), which is false. So \( t(\mathrm{T}, \mathrm{F}) = \mathrm{F} \).

*\( t(\mathrm{T}, \mathrm{T}) = t(\mathrm{F}, \mathrm{F}) = \mathrm{T} \).* Apply (I) with \( \Gamma \) empty and \( \varphi = \psi = p \). Its hypothesis, "every valuation making \( p \) true makes \( p \) true", holds. So every valuation makes \( p \to p \) true. A valuation with \( v(p) = \mathrm{T} \) gives \( t(\mathrm{T}, \mathrm{T}) = v(p \to p) = \mathrm{T} \), and one with \( v(p) = \mathrm{F} \) gives \( t(\mathrm{F}, \mathrm{F}) = \mathrm{T} \).

*\( t(\mathrm{F}, \mathrm{T}) = \mathrm{T} \).* Apply (I) with \( \Gamma \) the list \( q \), \( \varphi = p \) and \( \psi = q \). Every valuation making \( q \) and \( p \) true makes \( q \) true, so every valuation making \( q \) true makes \( p \to q \) true. A valuation with \( v(p) = \mathrm{F} \), \( v(q) = \mathrm{T} \) makes \( q \) true, so \( t(\mathrm{F}, \mathrm{T}) = v(p \to q) = \mathrm{T} \).

No step used a value of \( t \) that had not yet been found, since the formulas in \( \Gamma \), \( \varphi \) and \( \psi \) contain no \( \to \). So the only table of \( \to \) under which both rules preserve truth is the table of (V5). Conditions (E) and (I) are what Section 3.5 proves about the rules \( \rulename{{\to}E} \) and \( \rulename{{\to}I} \); the exercise shows that nothing but the standard table could have passed.

**Marking scheme.** (10 points)

- 3: the row \( (\mathrm{T}, \mathrm{F}) \) from (E), with a valuation making \( p \) true and \( q \) false, and the argument by contradiction.
- 3: the rows \( (\mathrm{T}, \mathrm{T}) \) and \( (\mathrm{F}, \mathrm{F}) \) from (I), with the hypothesis of (I) checked, and a valuation for each value of \( p \).
- 3: the row \( (\mathrm{F}, \mathrm{T}) \) from (I) with a nonempty \( \Gamma \) (or any other correct instance), hypothesis checked.
- 1: says why the argument is not circular (no \( \to \) in the formulas used).

Fatal errors (0 for the step): using the standard table of \( \to \) to justify a value of \( t \); an instance of (I) whose hypothesis is not checked.
:::

::: {#exr-valuations-and-truth-tables-c2}
[C2: Find the error]

Here is a claim and a "proof".

> **Claim.** Let \( v_{\mathrm{T}} \) be the all-T valuation. Every formula built from atoms by \( \wedge \), \( \vee \) and \( \to \) only is true under \( v_{\mathrm{T}} \).
>
> **Proof.** By @thm-structural-induction, with the property "if \( \varphi \) is built from atoms by \( \wedge \), \( \vee \), \( \to \) only, then \( v_{\mathrm{T}}(\varphi) = \mathrm{T} \)". The formulas \( \bot \), \( \neg\varphi \) and \( \varphi \leftrightarrow \psi \) are not built in this way, so the property holds for them. If a formula built in this way is \( \varphi \wedge \psi \), \( \varphi \vee \psi \) or \( \varphi \to \psi \), then \( \varphi \) and \( \psi \) are built in this way too, so the hypothesis applies to them. (1) For an atom \( p \), \( v_{\mathrm{T}}(p) = \mathrm{T} \) by the definition of \( v_{\mathrm{T}} \). (2) If \( v_{\mathrm{T}}(\varphi) = \mathrm{T} \) and \( v_{\mathrm{T}}(\psi) = \mathrm{T} \), then \( v_{\mathrm{T}}(\varphi \wedge \psi) = \mathrm{T} \) by (V3). (3) If \( v_{\mathrm{T}}(\varphi) = \mathrm{T} \) and \( v_{\mathrm{T}}(\psi) = \mathrm{T} \), then \( v_{\mathrm{T}}(\varphi \vee \psi) = \mathrm{T} \) by (V4), since at least one part is true. (4) If \( v_{\mathrm{T}}(\varphi) = \mathrm{T} \) and \( v_{\mathrm{T}}(\psi) = \mathrm{T} \), then \( v_{\mathrm{T}}(\varphi \to \psi) = \mathrm{T} \) by (V5), because \( v_{\mathrm{T}}(\varphi) = \mathrm{F} \) and an implication with a false hypothesis is true. This covers every clause, and proves the claim.

::: {.enumerate options="label=(\alph*)"}
1. Is the claim true?
2. Name the line that fails and say exactly what is wrong with it.
3. Give a formula on which the reason given in that line is false.
4. Repair the line.
:::
:::

::: {.solution}
*(a)* Yes. The claim is true, and the repaired proof in (d) proves it. So no formula is a counterexample to the claim; the error is in the argument only.

*(b)* Line (4). Its hypothesis states \( v_{\mathrm{T}}(\varphi) = \mathrm{T} \), and its reason states \( v_{\mathrm{T}}(\varphi) = \mathrm{F} \). The reason contradicts the induction hypothesis it is supposed to use: it quotes the vacuous row of (V5), which does not apply here. The conclusion \( v_{\mathrm{T}}(\varphi \to \psi) = \mathrm{T} \) is correct, but not for the reason given.

*(c)* \( p \to q \). Under \( v_{\mathrm{T}} \), \( v_{\mathrm{T}}(p) = \mathrm{T} \), so the stated reason "\( v_{\mathrm{T}}(p) = \mathrm{F} \)" is false, although \( v_{\mathrm{T}}(p \to q) = \mathrm{T} \) holds.

*(d)* *(4) If \( v_{\mathrm{T}}(\varphi) = \mathrm{T} \) and \( v_{\mathrm{T}}(\psi) = \mathrm{T} \), then \( v_{\mathrm{T}}(\varphi \to \psi) = \mathrm{T} \) by (V5), because the conclusion \( \psi \) is true, so we are not in the one row (true hypothesis, false conclusion) where an implication is false.* With this line the induction is correct, and the claim follows. Section 3.7 uses this fact to show that \( \wedge \), \( \vee \) and \( \to \) cannot express negation.

**Marking scheme.** (10 points)

- 2: the claim is true (with the reason: the repaired proof).
- 3: names line (4), and says its reason contradicts the hypothesis \( v_{\mathrm{T}}(\varphi) = \mathrm{T} \) of that very case.
- 2: a formula, such as \( p \to q \), on which the stated reason fails.
- 3: the repair, citing the row of (V5) that actually applies (conclusion true).

Fatal errors (0 for the step): calling the claim false; locating the error in line (3) (at least one part true is correct) or in the handling of \( \bot \), \( \neg \), \( \leftrightarrow \).
:::

<!-- dependency ledger
def-valuation (idea): the opening subsection reads the tables of and, bot, not, -> off the rules (motivation only; nothing later rests on it, as the text says) | prp-excluded-middle, prp-vacuous-implication, the rules of Ch 1-2, cited; the derivation of Q |- P -> Q is printed inline
def-truth-value (claim): the string p and q or r with two readings takes values T and F at p = F, q = F, r = T | inline computation; checked by verify/ch03/def-truth-table.py
lem-coincidence (proof): atoms(phi) defined by recursion (atom, bot, not, binary clauses) | Section 3.2 (thm-structural-recursion examples), recalled in prose before the lemma
lem-coincidence (claim): a formula with n atoms has 2^n rows (number of T/F assignments to n atoms) | inline, by ax-induction on n (said in the text)
def-truth-table (claim): some valuation agrees with any row (extend by F) | inline
def-truth-table (example): every printed truth table (the examples, A1, B3) and every F-row (exm-backwards-from-f, B1) | inline computations; checked by verify/ch03/def-truth-table.py, exm-backwards-from-f.py, exr-valuations-and-truth-tables-b1.py
exm-table-contrapositive (solution): the derivation of prp-contrapositive-converse uses RAA | Ch 2 Section 2.5, cited by label; visible in its printed derivation
exr-valuations-and-truth-tables-b2 (solution): the recursion for occ and bin is well defined; binary-built parts are binary-built | thm-structural-recursion (cited in the item); stated in the item
exr-valuations-and-truth-tables-c2 (solution): Section 3.7 uses the all-T fact | prose pointer within the chapter (thm-adequate-connectives proves it in its own text)
-->
