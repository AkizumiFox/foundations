# Tautologies, Entailment and Equivalence

Section 3.3 gave every formula a value under every valuation, and collected the values in a truth table. One formula at a time, though, is not what Chapters 1 and 2 were about. They were about **sequents**: premises on the left, a conclusion on the right, and the claim that the conclusion can be derived. This section defines the counterpart of a sequent in terms of truth, \( \Gamma \models \psi \): every valuation that makes the premises true makes the conclusion true. On the way it names the formulas that are true in every row, and the pairs of formulas that are true in the same rows. It ends with two lemmas about changing a formula, by replacing one part or by putting formulas in for its atoms, that later sections use.

## Tautologies and contradictions

Some tables of Section 3.3 had a last column made entirely of \( \mathrm{T} \): the formula \( ((p \to q) \wedge p) \to q \) of @exm-truth-table-modus-ponens, and the biconditional of @exm-table-contrapositive. Their truth does not depend on the situation. One table in Exercise A1 there, that of \( p \leftrightarrow \neg p \), was all \( \mathrm{F} \). These extremes deserve names.

*A tautology is true for reasons of form alone: whatever the atoms mean, it comes out true.*

::: {#def-tautology}
[Tautology and Contradiction]

A formula \( \varphi \) is a **tautology** if \( v(\varphi) = \mathrm{T} \) for **every** valuation \( v \). It is a **contradiction** if \( v(\varphi) = \mathrm{F} \) for **every** valuation \( v \).
:::

By @lem-coincidence, the value of \( \varphi \) under a valuation depends only on the row the valuation gives to the atoms of \( \varphi \). So \( \varphi \) is a tautology exactly when its truth table has \( \mathrm{T} \) in every row, and a contradiction exactly when it has \( \mathrm{F} \) in every row. Infinitely many valuations, finitely many rows to check.

Examples, simplest first.

- \( p \to p \) and \( p \vee \neg p \) are tautologies: in the row \( p = \mathrm{T} \) both are true, and in the row \( p = \mathrm{F} \), \( p \to p \) has a false hypothesis and \( \neg p \) is true.
- \( p \wedge \neg p \) and \( p \leftrightarrow \neg p \) are contradictions: in each row one of \( p \), \( \neg p \) is false, and the two sides of the biconditional differ.
- A formula with no atoms, such as \( \bot \) or \( \neg\bot \), has the same value under every valuation (its table has one row). So it is either a contradiction, like \( \bot \), or a tautology, like \( \neg\bot \). This degenerate case is the only one in which "not a tautology" forces "a contradiction".
- *Nonexample.* \( p \to q \) is neither: it is \( \mathrm{T} \) in the row TT and \( \mathrm{F} \) in the row TF. Most formulas are like this. Changing one symbol of the tautology \( p \to p \), to get \( p \to q \), loses the property: the rows in which the hypothesis and conclusion differ are no longer excluded by their being the same atom.

The formulas in between also need a word, and so do **lists** of formulas, because a list of premises can fail to be true together even when each premise alone can be true.

::: {#def-satisfiable}
[Satisfiable]

A formula \( \varphi \) is **satisfiable** if **there is** a valuation \( v \) with \( v(\varphi) = \mathrm{T} \). A list of formulas \( \Gamma = \varphi_1, \dots, \varphi_n \), where \( n \ge 0 \), is **satisfiable** if **there is** a valuation that makes **every** \( \varphi_i \) true. A formula or list that is not satisfiable is **unsatisfiable**.
:::

In words: a formula is satisfiable if some row makes it true, and a list is satisfiable if some **single** row makes all its members true at once. So a formula is unsatisfiable exactly when it is a contradiction. The **empty list** (\( n = 0 \)) is satisfiable: every valuation makes all of its members true, since it has none to check.

The list \( p, \neg p \) is unsatisfiable, although each of its members is satisfiable: a row making \( p \) true makes \( \neg p \) false. Satisfiability of a list is about a common row, not about each formula separately. And the list \( p \to q, \ q \to r, \ r \to \neg p \) is satisfiable, by the row with \( p \) false and \( q \), \( r \) true (the first two have true conclusions, and the third has conclusion \( \neg p \), which is true); in fact \( p \) is false in every row that makes all three true.

Tautologies and unsatisfiable formulas are two sides of one coin. For every formula \( \psi \),
\[
\psi \text{ is a tautology} \iff \neg\psi \text{ is unsatisfiable.}
\]
Indeed, by (V2) of @def-truth-value, \( v(\neg\psi) = \mathrm{T} \) exactly when \( v(\psi) = \mathrm{F} \). So "no valuation makes \( \neg\psi \) true" says "no valuation makes \( \psi \) false", which is "every valuation makes \( \psi \) true". Section 3.7 uses this to turn a question about tautologies into one about satisfiability.

::: {.warning}
"Not a tautology" does not mean "a contradiction". The formula \( p \to q \) is neither: some rows make it true and some false. To show a formula is **not** a tautology, one row making it false is enough; to show it **is** a contradiction, every row must make it false.
:::

## Semantic entailment

Now the counterpart of a sequent. A derivation from premises \( \Gamma \) to a conclusion \( \psi \) is a promise that \( \psi \) follows from \( \Gamma \). In terms of truth, "follows" should mean: no situation makes the premises true and the conclusion false. We want to prove, in the next two sections, that the rules of Chapters 1 and 2 derive exactly the sequents that pass this test; for that we need a precise name for the test.

*An argument is valid when its conclusion is true in every row in which all its premises are true.*

::: {#def-valid-argument}
[Semantic Entailment]

Let \( \Gamma = \varphi_1, \dots, \varphi_n \) be a list of formulas, where \( n \ge 0 \), and let \( \psi \) be a formula. We say \( \Gamma \) **semantically entails** \( \psi \), and write
\[
\Gamma \models \psi ,
\]
if **every** valuation that makes **all** of \( \varphi_1, \dots, \varphi_n \) true also makes \( \psi \) true. We then also call the argument from \( \Gamma \) to \( \psi \) **valid**. We write \( \varphi_1, \dots, \varphi_n \models \psi \) for \( \Gamma \models \psi \), and \( \models \psi \) when \( \Gamma \) is empty. If \( \Gamma \models \psi \) fails, we write \( \Gamma \not\models \psi \), and a valuation that makes every formula of \( \Gamma \) true and \( \psi \) false is a **refuting valuation**, or **refuting row**.
:::

Clause by clause. "Every valuation": the condition is checked in all situations, not in the actual one; a valid argument cannot be spoiled by what the atoms happen to mean. "That makes all of \( \varphi_1, \dots, \varphi_n \) true": rows in which some premise is false are ignored, whatever the conclusion does there. "Also makes \( \psi \) true": in the remaining rows, the conclusion must hold. In symbols, for every valuation \( v \),
\[
\bigl( v(\varphi_1) = \mathrm{T} \text{ and } \dots \text{ and } v(\varphi_n) = \mathrm{T} \bigr) \ \Rightarrow \ v(\psi) = \mathrm{T} .
\]
And \( \Gamma \not\models \psi \) says: **there is** a valuation making every premise true and the conclusion false. One refuting row is enough.

*Checking it.* By @lem-coincidence, whether a valuation makes the premises and the conclusion true depends only on its row on the atoms occurring in \( \Gamma \) and \( \psi \). So \( \Gamma \models \psi \) can be decided by one truth table on those atoms (@def-truth-table allows extra atoms in the list): find the rows in which every premise is \( \mathrm{T} \), and look at the conclusion there.

*First examples.* Row 1 of @exm-truth-table-modus-ponens is the only row making \( p \to q \) and \( p \) true, and \( q \) is true there, so \( p \to q, \ p \models q \). By @exm-table-contrapositive, \( p \to q \models \neg q \to \neg p \) and \( \neg q \to \neg p \models p \to q \), since the two columns are equal.

*The empty list.* When \( \Gamma \) is empty, every valuation makes "all of \( \Gamma \)" true, so \( \models \psi \) says that every valuation makes \( \psi \) true: \( \models \psi \) holds exactly when \( \psi \) is a tautology.

*Unsatisfiable premises.* If \( \Gamma \) is unsatisfiable, no valuation makes all of \( \Gamma \) true, so the condition has no row to check and holds: \( \Gamma \models \psi \) for **every** formula \( \psi \). For example \( p, \neg p \models q \) and \( \bot \models q \). This is the table's version of @prp-ex-falso, \( P, \neg P \vdash Q \), and of \( \rulename{\bot E} \).

*More premises.* If \( \Gamma \models \psi \), and \( \Delta \) is a list containing every formula of \( \Gamma \) (and perhaps others), then \( \Delta \models \psi \): a valuation making all of \( \Delta \) true makes all of \( \Gamma \) true, and so makes \( \psi \) true. Adding premises never destroys an entailment. In the same way, the order of the premises and repetitions among them do not matter: only which formulas occur in the list does.

*A test by satisfiability.* Finally, for every list \( \Gamma \) and formula \( \psi \),
\[
\Gamma \models \psi \iff \text{the list } \Gamma, \neg\psi \text{ is unsatisfiable.}
\]
Both sides say that no valuation makes every formula of \( \Gamma \) true and \( \psi \) false, because \( v(\neg\psi) = \mathrm{T} \) exactly when \( v(\psi) = \mathrm{F} \). With \( \Gamma \) empty this is the equivalence between tautologies and unsatisfiable negations above.

::: {#exm-affirming-the-consequent}
[Affirming the consequent is not valid]

Show that \( p \to q, \ q \not\models p \).
:::

::: {.solution}
We need one row making both premises true and the conclusion false. The conclusion \( p \) must be \( \mathrm{F} \), and the premise \( q \) must be \( \mathrm{T} \). In the row \( p = \mathrm{F} \), \( q = \mathrm{T} \), the premise \( p \to q \) is \( \mathrm{T} \), since its hypothesis is false. So this row makes \( p \to q \) and \( q \) true and \( p \) false: it is a refuting row.

The pattern is the one of Section 1.4, "from \( \varphi \to \psi \) and \( \psi \), infer \( \varphi \)", which is not an instance of \( \rulename{{\to}E} \). Section 1.1's Quick check gave the row a face: with \( P \): "\( n \) is divisible by \( 4 \)" and \( Q \): "\( n \) is even", at \( n = 2 \) the premises \( P \to Q \) and \( Q \) are true and \( P \) is false. It is also the step that would repair Argument B of Section 1.1: from "if \( n \) is even, then \( n^2 \) is even" and "\( n^2 \) is even", conclude "\( n \) is even". The conclusion of that instance happens to be true for every integer \( n \), as Argument A proves; the refuting row shows that the **form** does not guarantee it, so the step proves nothing. Section 3.5 upgrades this row from "not valid" to "not derivable by any derivation".
:::

A valid argument with several premises is checked in the same way, and working backwards from F often settles it without a table.

::: {#exm-three-premise-entailment}
[Two cases, two conclusions]

Show that \( p \vee q, \ p \to r, \ q \to s \models r \vee s \).
:::

::: {.solution}
Suppose a valuation \( v \) makes all three premises true and the conclusion false; we derive a contradiction. Since \( r \vee s \) is \( \mathrm{F} \), both \( r \) and \( s \) are \( \mathrm{F} \) (V4). Since \( p \to r \) is \( \mathrm{T} \) and \( r \) is \( \mathrm{F} \), the hypothesis \( p \) is \( \mathrm{F} \) (V5). In the same way \( q \to s \) forces \( q \) to be \( \mathrm{F} \). But then \( p \vee q \) is \( \mathrm{F} \), contradicting the first premise. So no refuting valuation exists, and the entailment holds.

The search replaced a table of \( 2^4 = 16 \) rows by four forced steps. The entailment is the table's picture of a proof by cases with \( \rulename{\vee E} \): in the case \( p \), the second premise gives \( r \), and \( \rulename{\vee I} \) gives \( r \vee s \); in the case \( q \), the third gives \( s \), and \( \rulename{\vee I} \) again.
:::

Changing the grouping of a formula can change what it entails.

::: {#exm-grouping-of-implications}
[One grouping entails the other, not conversely]

Decide whether \( (p \to q) \to r \models p \to (q \to r) \), and whether \( p \to (q \to r) \models (p \to q) \to r \).
:::

::: {.solution}
*The first holds.* Suppose a valuation makes \( (p \to q) \to r \) true and \( p \to (q \to r) \) false. The latter forces \( p = \mathrm{T} \) and \( q \to r \) false, so \( q = \mathrm{T} \) and \( r = \mathrm{F} \). Then \( p \to q \) is \( \mathrm{T} \), and \( (p \to q) \to r \) has a true hypothesis and a false conclusion, so it is \( \mathrm{F} \), a contradiction.

*The second fails.* Take \( p = \mathrm{F} \) and \( r = \mathrm{F} \), with \( q \) either value. Then \( p \to (q \to r) \) is \( \mathrm{T} \), since its hypothesis is false. But \( p \to q \) is \( \mathrm{T} \) for the same reason, so \( (p \to q) \to r \) is \( \mathrm{T} \to \mathrm{F} \), which is \( \mathrm{F} \). These two rows are refuting rows.

So the two groupings are not interchangeable, which is why Chapter 1 fixed a convention (\( \to \) groups to the right) and why the convention matters.
:::

::: {.warning}
\( \models \) is not \( \to \). The formula \( \varphi \to \psi \) is a formula: it has a value in each row and can be a part of larger formulas. The statement \( \varphi \models \psi \) is not a formula at all. It is a claim **about** two formulas, true or false once and for all, like \( \varphi \vdash \psi \). They are related (Exercise B3 shows \( \varphi \models \psi \) holds exactly when \( \varphi \to \psi \) is a tautology), but writing \( p \models q \models r \), or \( \neg(p \models q) \) inside a formula, mixes the two levels and means nothing.
:::

::: {.check}
Is \( p, \neg p \models q \)? Is \( p \to q, \ \neg p \models \neg q \)?
:::

::: {.solution}
The first holds: the list \( p, \neg p \) is unsatisfiable, so there is no row to check. The second fails: the row \( p = \mathrm{F} \), \( q = \mathrm{T} \) makes \( p \to q \) true (false hypothesis) and \( \neg p \) true, and \( \neg q \) false. It is the pattern "denying the hypothesis", the mirror image of affirming the consequent.
:::

## Semantic equivalence

Two formulas can be different strings and still say the same thing in every situation, as \( p \to q \) and \( \neg q \to \neg p \) did in @exm-table-contrapositive. Chapter 2 had a word for formulas that derive each other, provable equivalence (@def-provable-equivalence). Here is the counterpart in terms of truth.

*Two formulas are equivalent when they have the same truth table.*

::: {#def-semantic-equivalence}
[Semantic Equivalence]

Formulas \( \varphi \) and \( \psi \) are **semantically equivalent**, written \( \varphi \equiv \psi \), if \( \varphi \models \psi \) **and** \( \psi \models \varphi \).
:::

In words, each entails the other. Equivalently, \( v(\varphi) = v(\psi) \) for **every** valuation \( v \). Indeed, if \( \varphi \equiv \psi \) and \( v(\varphi) = \mathrm{T} \), then \( v(\psi) = \mathrm{T} \) by \( \varphi \models \psi \); if \( v(\varphi) = \mathrm{F} \), then \( v(\psi) \) cannot be \( \mathrm{T} \), since \( \psi \models \varphi \) would make \( v(\varphi) = \mathrm{T} \). The converse is plain. By (V6) of @def-truth-value, "\( v(\varphi) = v(\psi) \) for every \( v \)" says that \( \varphi \leftrightarrow \psi \) is true under every \( v \), so
\[
\varphi \equiv \psi \iff \models \varphi \leftrightarrow \psi .
\]
From "same value under every valuation" it follows at once that \( \equiv \) is reflexive, symmetric, and transitive: \( \varphi \equiv \varphi \); if \( \varphi \equiv \psi \), then \( \psi \equiv \varphi \); if \( \varphi \equiv \psi \) and \( \psi \equiv \chi \), then \( \varphi \equiv \chi \).

Examples: \( p \wedge q \equiv q \wedge p \) (the clause (V3) does not care about the order); \( p \equiv \neg\neg p \) (two flips); \( p \vee \neg p \equiv \neg\bot \) (both are true under every valuation). The degenerate case: any two tautologies are equivalent, and so are any two contradictions. *Nonexample:* \( p \wedge q \) and \( p \) are not equivalent. One direction holds, \( p \wedge q \models p \), but the other fails in the row \( p = \mathrm{T} \), \( q = \mathrm{F} \). Entailment in one direction is not equivalence. Nor is equivalence identity: \( p \wedge q \) and \( q \wedge p \) are different formulas, with different parse trees, and \( \rulename{{\to}E} \) treats them as different (Section 1.4).

The equivalences used most often are collected below. They are stated for arbitrary formulas \( \varphi, \psi, \chi \), not just atoms, since Section 3.7 applies them to compound formulas.

::: {#prp-standard-equivalences}
[Standard Equivalences]

For all formulas \( \varphi \), \( \psi \) and \( \chi \):

::: {.enumerate options="label=(\alph*)"}
1. (contrapositive) \( \varphi \to \psi \equiv \neg\psi \to \neg\varphi \);
2. (De Morgan) \( \neg(\varphi \wedge \psi) \equiv \neg\varphi \vee \neg\psi \) and \( \neg(\varphi \vee \psi) \equiv \neg\varphi \wedge \neg\psi \);
3. (implication as a disjunction) \( \varphi \to \psi \equiv \neg\varphi \vee \psi \);
4. (double negation) \( \neg\neg\varphi \equiv \varphi \);
5. (biconditional) \( \varphi \leftrightarrow \psi \equiv (\varphi \to \psi) \wedge (\psi \to \varphi) \);
6. (commutativity) \( \varphi \wedge \psi \equiv \psi \wedge \varphi \) and \( \varphi \vee \psi \equiv \psi \vee \varphi \);
7. (distributivity) \( \varphi \wedge (\psi \vee \chi) \equiv (\varphi \wedge \psi) \vee (\varphi \wedge \chi) \) and \( \varphi \vee (\psi \wedge \chi) \equiv (\varphi \vee \psi) \wedge (\varphi \vee \chi) \);
8. (associativity) \( (\varphi \wedge \psi) \wedge \chi \equiv \varphi \wedge (\psi \wedge \chi) \) and \( (\varphi \vee \psi) \vee \chi \equiv \varphi \vee (\psi \vee \chi) \).
:::
:::

::: {.idea}
For atoms these are truth-table checks. For arbitrary formulas the same tables work, with \( \varphi, \psi, \chi \) in the place of atoms: under a fixed valuation, each of \( \varphi, \psi, \chi \) has some value, and both sides are computed from those values by the clauses (V2)–(V6), exactly as in a table whose first columns are \( \varphi, \psi, \chi \).
:::

::: {.proof}
Fix a valuation \( v \), and let \( a = v(\varphi) \), \( b = v(\psi) \), \( c = v(\chi) \). Each side of each equivalence is built from \( \varphi, \psi, \chi \) by connectives, so by (V2)–(V6) of @def-truth-value its value under \( v \) is computed from \( a, b, c \) by the clauses of those connectives. The combination \( (a, b) \), or \( (a, b, c) \), is one row of the tables below, whose first columns list all 4 (or 8) combinations. In each table the columns of the two sides of each equivalence agree in every row, as the reader can check column by column. Hence both sides have the same value under \( v \), and since \( v \) was arbitrary, they are equivalent by the paraphrase of @def-semantic-equivalence.

Parts (a), (b), (c), and (e):
\[
\begin{array}{cc|cccc}
\varphi & \psi & \varphi \to \psi & \neg\psi \to \neg\varphi & \neg\varphi \vee \psi & (\varphi \to \psi) \wedge (\psi \to \varphi) \\
\hline
\mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{F} \\
\mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T}
\end{array}
\]
The first three formula columns agree, which gives (a) and (c). The last agrees with the column of \( \varphi \leftrightarrow \psi \) in the table of @def-truth-value (\( \mathrm{T} \) exactly when \( a = b \)), which gives (e).
\[
\begin{array}{cc|cccc}
\varphi & \psi & \neg(\varphi \wedge \psi) & \neg\varphi \vee \neg\psi & \neg(\varphi \vee \psi) & \neg\varphi \wedge \neg\psi \\
\hline
\mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} \\
\mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T}
\end{array}
\]
This gives (b). For (d): if \( a = \mathrm{T} \), then \( v(\neg\varphi) = \mathrm{F} \) and \( v(\neg\neg\varphi) = \mathrm{T} \); if \( a = \mathrm{F} \), then \( v(\neg\varphi) = \mathrm{T} \) and \( v(\neg\neg\varphi) = \mathrm{F} \); in both cases \( v(\neg\neg\varphi) = a \). For (f): clause (V3) makes \( v(\varphi \wedge \psi) = \mathrm{T} \) exactly when \( a = b = \mathrm{T} \), a condition that does not change when \( a \) and \( b \) are swapped, so \( v(\varphi \wedge \psi) = v(\psi \wedge \varphi) \); likewise (V4) for \( \vee \).

Parts (g) and (h):
\[
\begin{array}{ccc|cccc}
\varphi & \psi & \chi & \varphi \wedge (\psi \vee \chi) & (\varphi \wedge \psi) \vee (\varphi \wedge \chi) & \varphi \vee (\psi \wedge \chi) & (\varphi \vee \psi) \wedge (\varphi \vee \chi) \\
\hline
\mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} \\
\mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} \\
\mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F}
\end{array}
\]
\[
\begin{array}{ccc|cccc}
\varphi & \psi & \chi & (\varphi \wedge \psi) \wedge \chi & \varphi \wedge (\psi \wedge \chi) & (\varphi \vee \psi) \vee \chi & \varphi \vee (\psi \vee \chi) \\
\hline
\mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} \\
\mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} \\
\mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} \\
\mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} \\
\mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} \\
\mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} \\
\mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F}
\end{array}
\]
In each of the two tables the first two formula columns agree, and so do the last two. This proves all parts.
:::

Chapters 1 and 2 derived many of these laws as pairs of sequents, some directions with derivations that use \( \rulename{RAA} \) or \( \rulename{LEM} \) (@prp-de-morgan (d), @prp-double-negation, @prp-implication-as-disjunction) and others without. That some of them cannot do without a classical rule, Chapter 2 stated without proof (for De Morgan (d), for instance); for \( \neg\neg P \vdash P \), Section 3.5 proves it in an optional result. The tables do not see that difference: they see only that the two sides agree in every row. Section 3.6 shows that every such agreement can be turned into derivations, with \( \rulename{RAA} \) among the rules.

**Long conjunctions and disjunctions.** Associativity lets us stop worrying about grouping. We write \( \varphi_1 \wedge \varphi_2 \wedge \dots \wedge \varphi_n \) for the conjunction grouped to the right, \( \varphi_1 \wedge (\varphi_2 \wedge (\dots \wedge \varphi_n)) \), and likewise for \( \vee \); for \( n = 1 \) it is \( \varphi_1 \) itself. Then, for every valuation \( v \) and every \( n \ge 1 \),
\[
\begin{aligned}
v(\varphi_1 \wedge \dots \wedge \varphi_n) = \mathrm{T} &\iff v(\varphi_i) = \mathrm{T} \text{ for every } i \text{ with } 1 \le i \le n, \\
v(\varphi_1 \vee \dots \vee \varphi_n) = \mathrm{T} &\iff v(\varphi_i) = \mathrm{T} \text{ for some } i \text{ with } 1 \le i \le n .
\end{aligned}
\]
For the conjunction, we prove by @ax-induction on \( n \), started at \( 1 \), that the first line holds for **every** list of \( n \) formulas. For \( n = 1 \) both sides say \( v(\varphi_1) = \mathrm{T} \). If it holds for every list of \( n \) formulas, take a list of \( n + 1 \). The conjunction is \( \varphi_1 \wedge \theta \), where \( \theta = \varphi_2 \wedge \dots \wedge \varphi_{n+1} \) has \( n \) terms. By (V3), \( v(\varphi_1 \wedge \theta) = \mathrm{T} \) exactly when \( v(\varphi_1) = \mathrm{T} \) and \( v(\theta) = \mathrm{T} \), and by the hypothesis for \( n \), \( v(\theta) = \mathrm{T} \) exactly when \( v(\varphi_i) = \mathrm{T} \) for \( 2 \le i \le n + 1 \). Together: exactly when every \( v(\varphi_i) = \mathrm{T} \). The disjunction is the same with (V4) and "some". Two consequences follow at once, since the right-hand sides do not care about order or grouping. Reordering the terms of a long conjunction, or grouping them differently, gives an equivalent formula; likewise for disjunctions. And De Morgan's laws extend to many terms:
\[
\neg(\varphi_1 \wedge \dots \wedge \varphi_n) \equiv \neg\varphi_1 \vee \dots \vee \neg\varphi_n, \qquad \neg(\varphi_1 \vee \dots \vee \varphi_n) \equiv \neg\varphi_1 \wedge \dots \wedge \neg\varphi_n ,
\]
since, for instance, both sides of the first are true exactly when some \( \varphi_i \) is false.

::: {.check}
Is \( p \to (q \to r) \equiv (p \wedge q) \to r \)? And is \( p \to (q \to r) \equiv (p \to q) \to r \)?
:::

::: {.solution}
The first holds. Each side is false in exactly one row, \( p = q = \mathrm{T} \), \( r = \mathrm{F} \): the left needs \( p \) true and \( q \to r \) false, the right needs \( p \wedge q \) true and \( r \) false. (Chapter 1 derived the two from each other, @prp-curry.) The second fails: by @exm-grouping-of-implications, the row \( p = r = \mathrm{F} \) makes \( p \to (q \to r) \) true and \( (p \to q) \to r \) false.
:::

## Replacing a part by an equivalent part

In algebra, if \( a = b \), then \( a \) may be replaced by \( b \) inside any expression. Semantic equivalence behaves in the same way, because the value of a formula depends only on the values of its parts. This is what makes chains of equivalences, one standard equivalence applied deep inside a formula at a time, a legitimate way of computing.

Recall from Section 3.1 that the subformulas of \( \chi \) are the formulas at the nodes of its parse tree (@def-subformula). An **occurrence** of \( \varphi \) in \( \chi \) is a node whose subtree is a parse tree of \( \varphi \); **replacing** that occurrence by \( \varphi' \) means putting a parse tree of \( \varphi' \) in place of that subtree, which gives the parse tree of a new formula \( \chi' \).

::: {#lem-replacement}
[Replacement]

Let \( \varphi \equiv \varphi' \). If \( \chi' \) is obtained from a formula \( \chi \) by replacing one occurrence of \( \varphi \) in \( \chi \) by \( \varphi' \), then \( \chi' \equiv \chi \).
:::

::: {.idea}
Induct on the shape of \( \chi \). Either the occurrence is all of \( \chi \), and then \( \chi \) is \( \varphi \) and \( \chi' \) is \( \varphi' \), equivalent by hypothesis; or it sits inside one immediate part of \( \chi \), the other part is untouched, and the value of \( \chi \) is computed from the values of its parts, one of which has not changed and one of which has not changed its value.
:::

::: {.proof}
We apply @thm-structural-induction to the property \( C(\chi) \): *for every formula \( \chi' \) obtained from \( \chi \) by replacing one occurrence of \( \varphi \) by \( \varphi' \), and every valuation \( v \), \( v(\chi') = v(\chi) \).* By the paraphrase of @def-semantic-equivalence, \( C(\chi) \) says that each such \( \chi' \) is equivalent to \( \chi \).

In every case, the replaced occurrence sits either at the top node of the tree of \( \chi \) or at a node below it; in the second case the node lies in the subtree of exactly one immediate part of \( \chi \), since those subtrees are the parse trees of the immediate parts (@def-parse-tree). If the occurrence is the root, then \( \chi = \varphi \) and \( \chi' = \varphi' \), and \( v(\chi') = v(\chi) \) because \( \varphi \equiv \varphi' \). It remains to treat an occurrence below the root.

*Atoms and \( \bot \).* The parse tree is one node, so there is no node below the root.

*Negation.* Let \( \chi = \neg\theta \) and assume \( C(\theta) \). An occurrence below the root lies in \( \theta \), so \( \chi' = \neg\theta' \), where \( \theta' \) is obtained from \( \theta \) by replacing that occurrence. By \( C(\theta) \), \( v(\theta') = v(\theta) \), and (V2) gives \( v(\neg\theta') = v(\neg\theta) \).

*Binary connectives.* Let \( \chi = \theta_1 \circ \theta_2 \), with \( \circ \) one of \( \wedge, \vee, \to, \leftrightarrow \), and assume \( C(\theta_1) \) and \( C(\theta_2) \). If the occurrence lies in \( \theta_1 \), then \( \chi' = \theta_1' \circ \theta_2 \), with \( \theta_1' \) obtained from \( \theta_1 \) by the replacement, and \( v(\theta_1') = v(\theta_1) \) by \( C(\theta_1) \). The clause of @def-truth-value for \( \circ \) computes \( v(\chi') \) from \( v(\theta_1') \) and \( v(\theta_2) \), and \( v(\chi) \) from \( v(\theta_1) \) and \( v(\theta_2) \), by the same rule, so \( v(\chi') = v(\chi) \). An occurrence in \( \theta_2 \) is the same with the roles of the parts exchanged.

This covers every clause of @def-formula, so \( C(\chi) \) holds for every \( \chi \), which proves the lemma.
:::

Replacing several occurrences, one after another, keeps equivalence at each step, and \( \equiv \) is transitive, so the final formula is equivalent to the first. For instance, with (b), (d), and then (c) of @prp-standard-equivalences, each applied inside the formula:
\[
\begin{aligned}
p \to \neg(q \wedge \neg r) &\equiv p \to (\neg q \vee \neg\neg r) \\
&\equiv p \to (\neg q \vee r) \\
&\equiv \neg p \vee (\neg q \vee r) .
\end{aligned}
\]
The first step replaces the subformula \( \neg(q \wedge \neg r) \) by an equivalent one (De Morgan with \( \varphi = q \), \( \psi = \neg r \)); the second replaces \( \neg\neg r \) by \( r \); the third replaces the whole formula, by (c) with \( \varphi = p \) and \( \psi = \neg q \vee r \). Section 3.7 computes normal forms this way.

::: {.warning}
Replacement needs **equivalence**; entailment in one direction is not enough. We have \( p \wedge q \models p \), but replacing \( p \wedge q \) by \( p \) inside \( \neg(p \wedge q) \) gives \( \neg p \), and the row \( p = \mathrm{T} \), \( q = \mathrm{F} \) makes \( \neg(p \wedge q) \) true and \( \neg p \) false. A negation reverses the direction of an entailment, so one-way information cannot pass through it.
:::

## Substituting formulas for atoms

The letters \( P \), \( Q \) of Chapters 1 and 2 stood for arbitrary statements, and Section 3.1 turned that into a remark about derivations: a derivation written with letters is a pattern, and putting formulas in for the letters, uniformly, gives a derivation again. The truth table of @exm-truth-table-modus-ponens, though, was computed for the atoms \( p \) and \( q \). Does it tell us anything about \( (r \vee s) \to \neg t \) in place of \( p \)? It should: the table only used the values of \( p \) and \( q \), and a compound formula also has a value in each row. This subsection makes that precise.

Let \( p_1, \dots, p_n \) be distinct atoms and \( \varphi_1, \dots, \varphi_n \) formulas. The **substitution** \( \sigma \) of \( \varphi_1, \dots, \varphi_n \) for \( p_1, \dots, p_n \) is the function on formulas defined by recursion (@thm-structural-recursion):
\[
\begin{aligned}
\sigma(p_i) &= \varphi_i \ (1 \le i \le n), & \sigma(q) &= q \ \text{ for every other atom } q, & \sigma(\bot) &= \bot, \\
\sigma(\neg\chi) &= \neg\sigma(\chi), & \sigma(\chi \circ \theta) &= \sigma(\chi) \circ \sigma(\theta) \ \text{ for each binary } \circ . & &
\end{aligned}
\]
In words: \( \sigma(\chi) \) replaces **every** occurrence of each \( p_i \) in \( \chi \) by \( \varphi_i \), all at once, and changes nothing else. For a list \( \Gamma = \gamma_1, \dots, \gamma_m \), we write \( \sigma(\Gamma) \) for the list \( \sigma(\gamma_1), \dots, \sigma(\gamma_m) \). For example, with \( \sigma \) putting \( q \wedge r \) for \( p \) and \( p \) for \( q \),
\[
\sigma\bigl( (p \to q) \vee \neg p \bigr) = \bigl( (q \wedge r) \to p \bigr) \vee \neg(q \wedge r) .
\]
The \( p \) that \( \sigma \) puts in for \( q \) is not replaced again: the replacements happen simultaneously, in one pass over the parse tree.

::: {#lem-substitution}
[Substitution]

Let \( \sigma \) be the substitution of \( \varphi_1, \dots, \varphi_n \) for the distinct atoms \( p_1, \dots, p_n \).

::: {.enumerate options="label=(\alph*)"}
1. If \( \models \chi \), then \( \models \sigma(\chi) \).
2. If \( \Gamma \models \psi \), then \( \sigma(\Gamma) \models \sigma(\psi) \).
:::
:::

::: {.idea}
Under a valuation \( v \), the formula \( \sigma(\chi) \) behaves exactly like \( \chi \) itself under a different valuation \( w \): the one that gives each atom \( p_i \) the value that \( v \) gives to \( \varphi_i \). So every row for \( \sigma(\chi) \) is, in disguise, a row for \( \chi \), and whatever holds in all rows of \( \chi \) holds in all rows of \( \sigma(\chi) \). The disguise is proved by induction on the shape of \( \chi \).
:::

::: {.proof}
Let \( v \) be a valuation, and let \( w \) be the valuation with \( w(p) \coloneqq v(\sigma(p)) \) for every atom \( p \); so \( w(p_i) = v(\varphi_i) \) and \( w(q) = v(q) \) for every other atom \( q \).

::: {.claim}
\( v(\sigma(\chi)) = w(\chi) \) for every formula \( \chi \).
:::

::: {.proofofclaim}
By @thm-structural-induction. For an atom \( p \), \( v(\sigma(p)) = w(p) \) is the definition of \( w \). For \( \bot \), \( v(\sigma(\bot)) = v(\bot) = \mathrm{F} = w(\bot) \) by (V1). For a negation, assume \( v(\sigma(\chi)) = w(\chi) \); then \( v(\sigma(\neg\chi)) = v(\neg\sigma(\chi)) \), which by (V2) is the flip of \( v(\sigma(\chi)) = w(\chi) \), and so equals \( w(\neg\chi) \). For a binary connective \( \circ \), assume the claim for \( \chi \) and \( \theta \); then \( v(\sigma(\chi \circ \theta)) = v(\sigma(\chi) \circ \sigma(\theta)) \) is computed by the clause for \( \circ \) from \( v(\sigma(\chi)) = w(\chi) \) and \( v(\sigma(\theta)) = w(\theta) \), and so equals \( w(\chi \circ \theta) \), which the same clause computes from the same two values.
:::

*(a)* Let \( \models \chi \), and let \( v \) be any valuation. By the claim, \( v(\sigma(\chi)) = w(\chi) = \mathrm{T} \), since \( \chi \) is a tautology. So \( \sigma(\chi) \) is true under every valuation.

*(b)* Let \( \Gamma \models \psi \), and let \( v \) make every formula of \( \sigma(\Gamma) \) true. For each \( \gamma \) in \( \Gamma \), the claim gives \( w(\gamma) = v(\sigma(\gamma)) = \mathrm{T} \), so \( w \) makes every formula of \( \Gamma \) true. By \( \Gamma \models \psi \), \( w(\psi) = \mathrm{T} \), and by the claim again \( v(\sigma(\psi)) = w(\psi) = \mathrm{T} \). This proves \( \sigma(\Gamma) \models \sigma(\psi) \).
:::

So a table computed once for atoms settles infinitely many instances. From \( \models p \vee \neg p \) we get \( \models (q \to r) \vee \neg(q \to r) \), and every other instance of excluded middle. From \( p \to q, \ p \models q \) (@exm-truth-table-modus-ponens) we get \( \varphi \to \psi, \ \varphi \models \psi \) for all formulas \( \varphi, \psi \), which is the table's version of \( \rulename{{\to}E} \) as a schema. And from @exm-affirming-the-consequent's refuting row we learn something about all instances too, but only in one direction; the next warning says which.

::: {.warning}
Substitution must be **uniform**: every occurrence of \( p_i \) is replaced by the same \( \varphi_i \). Replacing only the first \( p \) of the tautology \( p \to p \) by \( q \) gives \( q \to p \), which is false in the row \( q = \mathrm{T} \), \( p = \mathrm{F} \). And the lemma runs one way only. An instance can be a tautology when the pattern is not: \( p \vee q \) is not a tautology, but its instance with \( \neg p \) put in for \( q \) is \( p \vee \neg p \), which is. So a refuting row for a pattern with atoms shows that the **pattern** is not valid, not that every instance fails.
:::

## Two questions, side by side

We now have two ways of saying that \( \psi \) follows from \( \Gamma \). They were built from different materials, and it is worth setting them next to each other before the next two sections connect them.

| | \( \Gamma \vdash \psi \) | \( \Gamma \models \psi \) |
|---|---|---|
| What it says | **there is** a derivation from premises in \( \Gamma \) to \( \psi \) | **every** valuation making all of \( \Gamma \) true makes \( \psi \) true |
| What it is about | syntax: lines, rules, boxes | meaning: truth values |
| How to show it holds | exhibit one derivation | check every row (or work backwards from F) |
| How to show it fails | no method yet: a failed search proves nothing | exhibit one refuting row |
| Defined in | @def-derivable (Section 1.2) | @def-valid-argument (this section) |

Look at the fourth row. To show that something is **not** derivable, we would have to survey infinitely many derivations; to show that something is **not** valid, one row suffices. And to show that something **is** valid takes a finite, mechanical check, while showing it derivable may need an idea. Each column is easy exactly where the other is hard.

The next two sections prove that the two columns always give the same answer. Section 3.5 proves **soundness**: if \( \Gamma \vdash \psi \), then \( \Gamma \models \psi \); so a refuting row proves that no derivation exists, which answers the question Chapter 2 ended on. Section 3.6 proves **completeness**: if \( \Gamma \models \psi \), then \( \Gamma \vdash \psi \); so a successful table check guarantees that a derivation exists, even before anyone has found it.

## Exercises

### A. Check your understanding

::: {#exr-entailment-and-equivalence-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Classify each formula as a tautology, a contradiction, or satisfiable but not a tautology: \( p \to (q \to p) \); \( p \wedge \neg(p \vee q) \); \( (p \to q) \wedge (q \to p) \); \( \neg(p \to p) \); \( (p \wedge q) \to (p \vee r) \).
2. For each, decide whether it holds, and give a refuting row if it does not: \( p \wedge q \models p \leftrightarrow q \); \( p \leftrightarrow q \models p \wedge q \); \( \neg p \to p \models p \).
3. True or false, with a reason: if \( \Gamma \models \psi \) and \( \Gamma \models \neg\psi \), then \( \Gamma \) is unsatisfiable.
4. True or false, with a reason: \( p \vee q \models p \) or \( p \vee q \models q \).
:::
:::

::: {.solution}
*(a)* \( p \to (q \to p) \): a tautology (if \( p \) is \( \mathrm{T} \), the conclusion \( q \to p \) is \( \mathrm{T} \); if \( p \) is \( \mathrm{F} \), the hypothesis is false). \( p \wedge \neg(p \vee q) \): a contradiction (if \( p \) is \( \mathrm{T} \), so is \( p \vee q \), and \( \neg(p \vee q) \) is \( \mathrm{F} \)). \( (p \to q) \wedge (q \to p) \): satisfiable, not a tautology (\( \mathrm{T} \) in the row TT, \( \mathrm{F} \) in TF). \( \neg(p \to p) \): a contradiction, since \( p \to p \) is a tautology. \( (p \wedge q) \to (p \vee r) \): a tautology (if the hypothesis is \( \mathrm{T} \), then \( p \) is \( \mathrm{T} \), so is \( p \vee r \)).

*(b)* \( p \wedge q \models p \leftrightarrow q \) holds: the only row making \( p \wedge q \) true has \( p = q = \mathrm{T} \), where \( p \leftrightarrow q \) is true. \( p \leftrightarrow q \models p \wedge q \) fails: the row \( p = q = \mathrm{F} \) makes \( p \leftrightarrow q \) true and \( p \wedge q \) false. \( \neg p \to p \models p \) holds: in the row \( p = \mathrm{F} \), the premise \( \neg p \to p \) has a true hypothesis and a false conclusion, so it is false; the only row making the premise true has \( p = \mathrm{T} \).

*(c)* True. If a valuation made all of \( \Gamma \) true, it would make both \( \psi \) and \( \neg\psi \) true, which (V2) forbids. So no valuation makes all of \( \Gamma \) true.

*(d)* False. The row \( p = \mathrm{F} \), \( q = \mathrm{T} \) refutes \( p \vee q \models p \), and the row \( p = \mathrm{T} \), \( q = \mathrm{F} \) refutes \( p \vee q \models q \). Each disjunct fails in some row where the disjunction holds, although in every such row one of them holds: \( \models \) must work row by row with a single conclusion.
:::

### B. Practice

::: {#exr-entailment-and-equivalence-b1}
[B1: Valid or not]

Decide whether each entailment holds, by a table or by working backwards from F. If it holds, also give a derivation of the corresponding sequent with \( \vdash \) in place of \( \models \), using the rules of Chapters 1 and 2; if it fails, give a refuting row.

::: {.enumerate options="label=(\alph*)"}
1. \( p \to q, \ \neg q \models \neg p \).
2. \( p \to (q \vee r), \ \neg q \models p \to r \).
3. \( p \to q \models \neg p \to \neg q \).
4. \( p \vee q, \ p \to r, \ q \to r \models r \).
:::
:::

::: {.solution}
*(a)* Holds. Backwards from F: \( \neg p \) false means \( p = \mathrm{T} \); \( \neg q \) true means \( q = \mathrm{F} \); then \( p \to q \) is \( \mathrm{F} \), so no row makes the premises true and the conclusion false. A derivation, with modus tollens (@prp-modus-tollens) as a derived rule:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {p \to q}
  \hypo {2} {\neg q}
  \have {3} {\neg p} \mt{1,2}
\end{nd}$
\end{center}
```

*(b)* Holds. Backwards from F: \( p \to r \) false means \( p = \mathrm{T} \), \( r = \mathrm{F} \); \( \neg q \) true means \( q = \mathrm{F} \); then \( q \vee r \) is \( \mathrm{F} \), and \( p \to (q \vee r) \) is \( \mathrm{F} \), contradicting the first premise. A derivation, with disjunctive syllogism (@prp-disjunctive-syllogism), which refutes the left disjunct:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {p \to (q \vee r)}
  \hypo {2} {\neg q}
  \open
  \hypo {3} {p}
  \have {4} {q \vee r} \ie{1,3}
  \have {5} {r} \ds{4,2}
  \close
  \have {6} {p \to r} \ii{3-5}
\end{nd}$
\end{center}
```

*(c)* Fails. The row \( p = \mathrm{F} \), \( q = \mathrm{T} \) makes \( p \to q \) true (false hypothesis) and \( \neg p \to \neg q \) false (\( \neg p \) true, \( \neg q \) false). It is the pattern of the Quick check, "denying the hypothesis", in the form of an implication.

*(d)* Holds. Backwards from F: \( r = \mathrm{F} \); then \( p \to r \) true forces \( p = \mathrm{F} \), and \( q \to r \) true forces \( q = \mathrm{F} \); then \( p \vee q \) is \( \mathrm{F} \), a contradiction. A derivation by cases:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {p \vee q}
  \hypo {2} {p \to r}
  \hypo {3} {q \to r}
  \open
  \hypo {4} {p}
  \have {5} {r} \ie{2,4}
  \close
  \open
  \hypo {6} {q}
  \have {7} {r} \ie{3,6}
  \close
  \have {8} {r} \oe{1,4-5,6-7}
\end{nd}$
\end{center}
```
:::

::: {#exr-entailment-and-equivalence-b2}
[B2: A biconditional as a disjunction]

Show by a truth table that \( p \leftrightarrow q \equiv (p \wedge q) \vee (\neg p \wedge \neg q) \). Which theorem of this chapter will guarantee, without any search, that each side can be derived from the other?
:::

::: {.solution}
\[
\begin{array}{cc|ccccc}
p & q & p \leftrightarrow q & p \wedge q & \neg p \wedge \neg q & (p \wedge q) \vee (\neg p \wedge \neg q) \\
\hline
\mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{T} \\
\mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{T}
\end{array}
\]
The columns of \( p \leftrightarrow q \) and of the disjunction agree in every row, so the two formulas are equivalent: each side entails the other. The theorem that turns each entailment into a derivation is completeness, in Section 3.6: if \( \Gamma \models \psi \), then \( \Gamma \vdash \psi \). So \( p \leftrightarrow q \vdash (p \wedge q) \vee (\neg p \wedge \neg q) \) and its converse are both derivable, before any derivation has been written.
:::

::: {#exr-entailment-and-equivalence-b3}
[B3: Entailment and implication]

Let \( \Gamma \) be a list of formulas and \( \varphi, \psi \) formulas. Prove:

::: {.enumerate options="label=(\alph*)"}
1. \( \varphi \models \psi \) if and only if \( \models \varphi \to \psi \);
2. \( \Gamma, \varphi \models \psi \) if and only if \( \Gamma \models \varphi \to \psi \).
:::
:::

::: {.solution}
We prove (b); then (a) is (b) with \( \Gamma \) empty, since \( \Gamma, \varphi \) is then the one-formula list \( \varphi \).

\( (\Rightarrow) \) Suppose \( \Gamma, \varphi \models \psi \), and let \( v \) make every formula of \( \Gamma \) true. If \( v(\varphi) = \mathrm{F} \), then \( v(\varphi \to \psi) = \mathrm{T} \) by (V5). If \( v(\varphi) = \mathrm{T} \), then \( v \) makes every formula of the list \( \Gamma, \varphi \) true, so \( v(\psi) = \mathrm{T} \) by hypothesis, and again \( v(\varphi \to \psi) = \mathrm{T} \). So \( \Gamma \models \varphi \to \psi \).

\( (\Leftarrow) \) Suppose \( \Gamma \models \varphi \to \psi \), and let \( v \) make every formula of \( \Gamma, \varphi \) true. Then \( v \) makes every formula of \( \Gamma \) true, so \( v(\varphi \to \psi) = \mathrm{T} \), and \( v(\varphi) = \mathrm{T} \). By (V5), an implication with a true hypothesis is true only if its conclusion is, so \( v(\psi) = \mathrm{T} \). So \( \Gamma, \varphi \models \psi \).

Part (b) is the table's version of \( \rulename{{\to}I} \) (the direction \( \Rightarrow \)) and of \( \rulename{{\to}E} \) (the direction \( \Leftarrow \)).
:::

### C. Going deeper

::: {#exr-entailment-and-equivalence-c1}
[C1: Substitution with a new connective, the last half blank]

Extend the formulas by a new binary connective \( \mathbin{|} \) ("not both", often called NAND): add to @def-formula the clause "if \( \varphi \) and \( \psi \) are formulas, so is \( (\varphi \mathbin{|} \psi) \)", and to @def-truth-value the clause

> (V7) \( v(\varphi \mathbin{|} \psi) \coloneqq \mathrm{F} \) if \( v(\varphi) = v(\psi) = \mathrm{T} \); otherwise \( \mathrm{T} \).

Assume that structural induction and recursion work for the extended formulas as before, with one more clause. A substitution \( \sigma \) of \( \varphi_1, \dots, \varphi_n \) for \( p_1, \dots, p_n \) is defined by the clauses in the text, with \( \sigma(\chi \mathbin{|} \theta) \coloneqq \sigma(\chi) \mathbin{|} \sigma(\theta) \) added. Prove that if \( \chi \) is a tautology of the extended language, so is \( \sigma(\chi) \).

Here is the first half of a proof. *Let \( v \) be a valuation, and let \( w \) be the valuation with \( w(p) \coloneqq v(\sigma(p)) \) for every atom \( p \). We show \( v(\sigma(\chi)) = w(\chi) \) for every formula \( \chi \) of the extended language, by structural induction. Atoms: \( v(\sigma(p)) = w(p) \) is the definition of \( w \).*

*Name the move, then complete it.*
:::

::: {.solution}
The move is **induction on the shape of a formula**, now with eight cases: atoms, \( \bot \), \( \neg \), and five binary connectives. The property is \( C(\chi) \): \( v(\sigma(\chi)) = w(\chi) \).

*\( \bot \).* \( \sigma(\bot) = \bot \), so \( v(\sigma(\bot)) = \mathrm{F} = w(\bot) \) by (V1).

*Negation.* Assume \( C(\chi) \). Then \( v(\sigma(\neg\chi)) = v(\neg\sigma(\chi)) \), which by (V2) is \( \mathrm{T} \) exactly when \( v(\sigma(\chi)) = \mathrm{F} \), that is, when \( w(\chi) = \mathrm{F} \), that is, when \( w(\neg\chi) = \mathrm{T} \).

*The four old binary connectives.* Assume \( C(\chi) \) and \( C(\theta) \), and let \( \circ \) be one of \( \wedge, \vee, \to, \leftrightarrow \). Then \( v(\sigma(\chi \circ \theta)) = v(\sigma(\chi) \circ \sigma(\theta)) \) is computed by the clause for \( \circ \) from the two values \( v(\sigma(\chi)) = w(\chi) \) and \( v(\sigma(\theta)) = w(\theta) \); the same clause computes \( w(\chi \circ \theta) \) from the same two values. So they are equal.

*The new connective.* Assume \( C(\chi) \) and \( C(\theta) \). By (V7), \( v(\sigma(\chi \mathbin{|} \theta)) = v(\sigma(\chi) \mathbin{|} \sigma(\theta)) \) is \( \mathrm{F} \) exactly when \( v(\sigma(\chi)) = v(\sigma(\theta)) = \mathrm{T} \), that is, when \( w(\chi) = w(\theta) = \mathrm{T} \), that is, when \( w(\chi \mathbin{|} \theta) = \mathrm{F} \).

This covers every clause, so \( C(\chi) \) holds for every formula. Now let \( \chi \) be a tautology and \( v \) any valuation: \( v(\sigma(\chi)) = w(\chi) = \mathrm{T} \). So \( \sigma(\chi) \) is a tautology.

Only one case is new. The proof of @lem-substitution never looked at what the clauses say, only that each computes the value of a compound from the values of its parts; any connective defined by a table passes.

**Marking scheme.** (10 points)

- 1: names the move and states the property \( v(\sigma(\chi)) = w(\chi) \) for all \( \chi \).
- 1: the \( \bot \) case.
- 2: the \( \neg \) case, from the hypothesis for \( \chi \).
- 2: the old binary cases, using the hypotheses for both parts.
- 3: the \( \mathbin{|} \) case, with (V7) and both hypotheses.
- 1: the conclusion for tautologies.

Fatal errors (0 for the step): omitting the \( \mathbin{|} \) case; using \( w \) where \( v \) is meant in the conclusion.
:::

::: {#exr-entailment-and-equivalence-c2}
[C2: Is equivalence preserved by substitution?]

Let \( \sigma \) be a substitution and suppose \( \varphi \equiv \psi \). Is \( \sigma(\varphi) \equiv \sigma(\psi) \)? Prove it, or give a counterexample. Then suppose that De Morgan's law (b) of @prp-standard-equivalences had been checked only for atoms, \( \neg(p \wedge q) \equiv \neg p \vee \neg q \), by its four-row table. Use your answer to deduce from this, in one line, that \( \neg((r \to s) \wedge \neg t) \equiv \neg(r \to s) \vee \neg\neg t \).
:::

::: {.solution}
Yes. By the paraphrase of @def-semantic-equivalence, \( \varphi \equiv \psi \) means \( \models \varphi \leftrightarrow \psi \). By @lem-substitution (a), \( \models \sigma(\varphi \leftrightarrow \psi) \), and by the definition of \( \sigma \), \( \sigma(\varphi \leftrightarrow \psi) = \sigma(\varphi) \leftrightarrow \sigma(\psi) \). So \( \models \sigma(\varphi) \leftrightarrow \sigma(\psi) \), that is, \( \sigma(\varphi) \equiv \sigma(\psi) \). (Alternatively, apply @lem-substitution (b) to \( \varphi \models \psi \) and to \( \psi \models \varphi \).)

For the instance: the substitution of \( r \to s \) for \( p \) and \( \neg t \) for \( q \) turns the two sides of \( \neg(p \wedge q) \equiv \neg p \vee \neg q \) into \( \neg((r \to s) \wedge \neg t) \) and \( \neg(r \to s) \vee \neg\neg t \), so these are equivalent by the first part. Checking a law for atoms, by one small table, is therefore enough.

A tempting counterexample fails for a reason worth seeing. With \( \sigma \) putting \( \neg p \) for \( q \), the nonequivalent formulas \( p \) and \( \neg q \) become the equivalent \( p \) and \( \neg\neg p \): substitution can create equivalences. It cannot destroy one, which is what the question asks.

**Marking scheme.** (10 points)

- 3: reduces \( \equiv \) to a tautology \( \models \varphi \leftrightarrow \psi \), or to two entailments, citing the definition.
- 3: applies @lem-substitution correctly.
- 2: computes \( \sigma(\varphi \leftrightarrow \psi) = \sigma(\varphi) \leftrightarrow \sigma(\psi) \) from the definition of \( \sigma \).
- 2: the instance, with the substitution named.

Fatal errors (0 for the step): answering "no" by a pair that is not equivalent before the substitution; using a nonuniform replacement.
:::

<!-- dependency ledger
def-tautology (claim): a formula with no atoms has the same value under every valuation | lem-coincidence with atoms(phi) empty; def-truth-table (one-row table), Section 3.3
def-satisfiable (claim): p -> q, q -> r, r -> not-p is satisfiable at p = F, q = r = T, and p is F in every satisfying row | inline; checked by verify/ch03/exr-entailment-and-equivalence-a1.py
def-valid-argument (claim): psi tautology iff not-psi unsatisfiable; Gamma |= psi iff Gamma, not-psi unsatisfiable; adding premises keeps |=; order and repetition irrelevant | inline, from V2 and the definitions
def-semantic-equivalence (claim): phi == psi iff same value under every v iff |= phi <-> psi; == is reflexive, symmetric, transitive | inline, from V6
prp-standard-equivalences (proof): the value of a compound built from phi, psi, chi depends only on (v(phi), v(psi), v(chi)) through the clauses | def-truth-value (V2)-(V6), stated in the proof; all tables checked by verify/ch03/prp-standard-equivalences.py
prp-standard-equivalences (claim): v of a right-grouped n-term conjunction is T iff every term is T (disjunction: some term); De Morgan for n terms | inline, by ax-induction on n
lem-replacement (proof): a node below the root of a parse tree lies in the subtree of exactly one immediate part, and those subtrees are the parse trees of the immediate parts | def-parse-tree (Section 3.1), with thm-unique-readability for "the" parse tree
lem-substitution (proof): the recursion defining sigma is well defined | thm-structural-recursion (values are formulas), cited in the text
exm-affirming-the-consequent (solution): n = 2 witness (divisible by 4 implies even; 2 even, not divisible by 4); Argument A proves n^2 even implies n even | Section 1.1 (def-sequent's Quick check and Argument A), recalled in prose
exm-three-premise-entailment (solution): this and every other entailment verdict and refuting row of the section (exm-grouping-of-implications, the Quick checks, A1, B1, B2) | inline; checked by verify/ch03/exm-three-premise-entailment.py, exm-grouping-of-implications.py, exr-entailment-and-equivalence-a1.py, exr-entailment-and-equivalence-b1.py
exr-entailment-and-equivalence-b1 (solution): the derivations of (a), (b), (d) | checked with the Fitch checker on a capital-letter copy; MT and DS are prp-modus-tollens and prp-disjunctive-syllogism (Ch 2)
exr-entailment-and-equivalence-b2 (solution): completeness (Section 3.6) | forward pointer in an exercise solution, used as a pointer only (no argument rests on it)
exr-entailment-and-equivalence-c1 (solution): structural induction and recursion for the extended language | assumed in the item's statement
-->
