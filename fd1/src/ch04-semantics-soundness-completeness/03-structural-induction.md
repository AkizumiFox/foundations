# Induction and Recursion on Formulas

*S3-PLACEHOLDER: opening frame of Section 4.3, split off in D2.*

## Structural induction

We return to formulas. The formation sequence of a formula plays the part that "\( 0, 1, 2, \dots \)" plays for numbers: every formula is reached from atoms and \( \bot \) by finitely many uses of the clauses. So a property of formulas can be proved in the same two parts.

A **property of formulas** is a statement \( P(\varphi) \) about a formula \( \varphi \), true or false for each particular formula: "\( \varphi \) has as many left as right parentheses", "\( \varphi \) contains the atom \( p \)".

*If every atom and \( \bot \) has a property, and each way of building a formula passes the property from the parts to the whole, then every formula has it.*

::: {#thm-structural-induction}
[Structural Induction]

Let \( P(\varphi) \) be a property of formulas. Suppose that

::: {.enumerate options="label=(\roman*)"}
1. \( P(p) \) holds for every atom \( p \), and \( P(\bot) \) holds;
2. **for every** formula \( \varphi \), if \( P(\varphi) \) holds, then \( P(\neg\varphi) \) holds;
3. **for all** formulas \( \varphi, \psi \) and **each** binary connective \( \circ \), if \( P(\varphi) \) and \( P(\psi) \) hold, then \( P((\varphi \circ \psi)) \) holds.
:::

Then \( P(\varphi) \) holds for every formula \( \varphi \).
:::

In words: (i) is the base case, one for each kind of formula of length one. (ii) and (iii) are the inductive steps, one for each building clause of @def-formula, and inside them "\( P(\varphi) \) and \( P(\psi) \)" is the induction hypothesis, assumed for the **immediate parts** of the formula being built. There are six cases in all when the four binary connectives are counted separately; often the four are handled at once, with \( \circ \) left unspecified.

::: {.idea}
Take any formula and a formation sequence ending in it. Walk along the sequence: each entry is an atom or \( \bot \), which has the property by (i), or is built from **earlier** entries, which have it already, by (ii) or (iii). "Earlier entries, any of them" is exactly the shape of strong induction, applied to the position in the list.
:::

::: {.proof}
Suppose (i)–(iii) hold, and let \( \chi \) be a formula. By @def-formula (F4) there is a formation sequence \( \chi_1, \dots, \chi_m \) with \( \chi_m = \chi \). For \( i \in \nN \), let \( Q(i) \) be the property "if \( 1 \le i \le m \), then \( P(\chi_i) \) holds". We prove \( Q(i) \) for every \( i \in \nN \) by @thm-strong-induction.

Let \( i \in \nN \), and suppose \( Q(k) \) holds for every \( k \in \nN \) with \( k < i \). If \( i = 0 \) or \( i > m \), then \( Q(i) \) holds vacuously. So let \( 1 \le i \le m \). By the definition of a formation sequence, one of three things is true.

- \( \chi_i \) is an atom or \( \bot \). Then \( P(\chi_i) \) holds by (i).
- \( \chi_i = \neg\chi_j \) for some \( j < i \). Then \( 1 \le j \le m \), and \( Q(j) \) gives \( P(\chi_j) \). The entry \( \chi_j \) is a formula (every entry of a formation sequence is one, Section 4.1), so (ii) applies and gives \( P(\chi_i) \).
- \( \chi_i = (\chi_j \circ \chi_l) \) for some \( j, l < i \) and a binary connective \( \circ \). Then \( 1 \le j, l \le m \), and \( Q(j) \) and \( Q(l) \) give \( P(\chi_j) \) and \( P(\chi_l) \), both entries are formulas, and (iii) gives \( P(\chi_i) \).

So \( Q(i) \) holds. By @thm-strong-induction, \( Q(i) \) holds for every \( i \in \nN \); in particular \( Q(m) \) gives \( P(\chi_m) \), that is, \( P(\chi) \). Since \( \chi \) was an arbitrary formula, this proves the theorem.
:::

The proof uses **strong** induction, because an entry of a formation sequence may be built from any earlier entries, not only from the one just before it.

::: {.remark}
A tempting alternative is induction on the **height** of a formula: prove the property for all formulas of height \( 1 \), then for height \( h + 1 \) assuming it for smaller heights. That route is circular here. The height was defined through "the" parse tree (@def-height), and a formula has only one parse tree only because of the unique readability theorem below, whose proof uses structural induction. Inducting on the position in a formation sequence needs nothing but @def-formula.
:::

::: {.warning}
A structural induction must cover **every** clause, the base case \( \bot \) and the step for \( \neg \) included. Try to prove "every formula contains an atom": it holds for atoms, and the steps for \( \neg \) and for \( (\varphi \circ \psi) \) keep it, since the atoms of the parts are atoms of the whole. But the case \( \bot \) fails, and so does the claim: \( \bot \), \( \neg\bot \) and \( (\bot \to \bot) \) contain no atom. A proof that "forgets" \( \bot \) proves something false.
:::

::: {.check}
Which clause of @def-formula makes step (ii) of @thm-structural-induction necessary? Give a property of formulas that holds for every atom and for \( \bot \), passes from \( \varphi \) and \( \psi \) to \( (\varphi \circ \psi) \) for every binary connective, and yet fails for some formula.
:::

::: {.solution}
Clause (F2), which builds \( \neg\varphi \) from \( \varphi \): step (ii) is the step for that clause. Without it, the formulas made by (F2) would be missed.

One such property: "\( \varphi \) is an atom, or is \( \bot \), or begins with \( ( \)". Atoms and \( \bot \) have it, and every formula \( (\varphi \circ \psi) \) begins with \( ( \), whatever its parts are. But \( \neg p \) does not have it. So (i) and (iii) alone do not prove a property of every formula; the property fails exactly at a formula made by the forgotten clause.
:::

## Counting parentheses

Our first structural induction proves the claim Section 4.2 began with, that every formula has as many left parentheses as right ones, together with two refinements: one that the next theorem needs, and one that Exercise C1 uses. We count parentheses in strings, and for this some words about strings.

An **initial segment** of a string \( s \) is the string of the first \( k \) symbols of \( s \), for some \( k \) with \( 0 \le k \le \) the length of \( s \). For \( k = 0 \) it is the **empty** string, with no symbols; for \( k \) equal to the length it is \( s \) itself. An initial segment is **proper** if it is shorter than \( s \). The **excess** of a string \( s \) is
\[
\operatorname{ex}(s) \coloneqq (\text{number of } ( \text{ in } s) - (\text{number of } ) \text{ in } s) .
\]
So a left parenthesis has excess \( 1 \), a right parenthesis \( -1 \), and any other symbol \( 0 \); and the excess of a string written as two strings one after the other is the sum of their excesses, since the counts add. For example, \( \operatorname{ex}(\,(p \wedge (q\,) = 2 \): after reading \( (p \wedge (q \) we are inside two pairs of parentheses that have not yet closed. That is the picture to keep: the excess of an initial segment is the **depth** we are at when we have read that far.

::: {#lem-parenthesis-count}
[Parenthesis Count]

Let \( \chi \) be a formula.

::: {.enumerate options="label=(\alph*)"}
1. \( \operatorname{ex}(\chi) = 0 \): \( \chi \) has as many left as right parentheses.
2. Every initial segment \( u \) of \( \chi \) has \( \operatorname{ex}(u) \ge 0 \). If moreover \( \chi \) has the form \( (\varphi \circ \psi) \) and \( u \) is proper and nonempty, then \( \operatorname{ex}(u) \ge 1 \).
3. For every occurrence of a binary connective in \( \chi \), the initial segment of \( \chi \) that ends just before that occurrence has excess at least \( 1 \).
:::
:::

In words: (a) is balance. (b) says that reading a formula from the left, we never close more parentheses than we have opened, and that inside a formula \( (\varphi \circ \psi) \) we stay at depth at least \( 1 \) until the very last symbol. (c) says that no binary connective lies outside all parentheses. Part (a) is the fact we set out to prove; (c), with (a), is what the unique readability theorem needs, and (b) shows that no proper initial segment of a formula is a formula (Exercise C1). The steps for (b) and (c) use (a) for the parts, so the three are proved together.

::: {.idea}
Induction on the shape of a formula, all three parts at once. For \( \neg\varphi \), the extra \( \neg \) changes no count. For \( (\varphi \circ \psi) \), list its initial segments by where they stop: before anything, inside \( \varphi \), at the connective, inside \( \psi \), at the end. Each is "\( ( \)" followed by pieces whose excess the induction hypothesis controls.
:::

::: {.proof}
We prove, by @thm-structural-induction, that every formula \( \chi \) has the property \( P(\chi) \): "(a), (b), and (c) hold for \( \chi \)".

*Atoms and \( \bot \).* The formula is one symbol, not a parenthesis. (a) Its excess is \( 0 \). (b) Its initial segments are the empty string and the formula itself, both of excess \( 0 \); and it does not have the form \( (\varphi \circ \psi) \), which has length at least \( 5 \). (c) It contains no binary connective.

*Negation.* Let \( \varphi \) be a formula with \( P(\varphi) \); we show \( P(\neg\varphi) \). (a) \( \operatorname{ex}(\neg\varphi) = 0 + \operatorname{ex}(\varphi) = 0 \), by (a) for \( \varphi \). (b) An initial segment of \( \neg\varphi \) is either empty, of excess \( 0 \), or \( \neg \) followed by an initial segment \( u' \) of \( \varphi \), of excess \( \operatorname{ex}(u') \ge 0 \) by (b) for \( \varphi \). The formula \( \neg\varphi \) begins with \( \neg \), so it does not have the form \( (\varphi' \circ \psi') \), and the second sentence of (b) says nothing about it. (c) A binary connective in \( \neg\varphi \) lies in \( \varphi \), and the initial segment of \( \neg\varphi \) before it is \( \neg \) followed by the initial segment of \( \varphi \) before it, whose excess is at least \( 1 \) by (c) for \( \varphi \).

*Binary connectives.* Let \( \varphi, \psi \) be formulas with \( P(\varphi) \) and \( P(\psi) \), let \( \circ \) be a binary connective, and let \( \chi = (\varphi \circ \psi) \).

*(a)* \( \operatorname{ex}(\chi) = 1 + \operatorname{ex}(\varphi) + 0 + \operatorname{ex}(\psi) - 1 = 0 \), by (a) for \( \varphi \) and for \( \psi \).

*(b)* Every initial segment of \( \chi \) is of exactly one of the following five kinds, and its excess is as shown:

- the empty string: excess \( 0 \);
- \( ( \) followed by an initial segment \( u' \) of \( \varphi \): excess \( 1 + \operatorname{ex}(u') \ge 1 \), by (b) for \( \varphi \);
- \( (\varphi\,\circ \): excess \( 1 + \operatorname{ex}(\varphi) + 0 = 1 \), by (a) for \( \varphi \);
- \( (\varphi\,\circ \) followed by a nonempty initial segment \( v' \) of \( \psi \): excess \( 1 + 0 + \operatorname{ex}(v') \ge 1 \), by (a) for \( \varphi \) and (b) for \( \psi \);
- \( \chi \) itself: excess \( 0 \), by (a) for \( \chi \).

All five have excess at least \( 0 \). The proper nonempty ones are those of the middle three kinds, and they have excess at least \( 1 \).

*(c)* An occurrence of a binary connective in \( \chi \) is the connective \( \circ \) between \( \varphi \) and \( \psi \), or lies in \( \varphi \), or lies in \( \psi \). Before \( \circ \) stands \( (\varphi \), of excess \( 1 \). Before an occurrence in \( \varphi \) stands \( ( \) followed by the initial segment of \( \varphi \) before it, of excess at least \( 1 + 1 = 2 \) by (c) for \( \varphi \). Before an occurrence in \( \psi \) stands \( (\varphi\,\circ \) followed by the initial segment of \( \psi \) before it, of excess at least \( 1 + 0 + 1 = 2 \) by (a) for \( \varphi \) and (c) for \( \psi \). In all three cases the excess is at least \( 1 \).

So \( P(\chi) \) holds. By @thm-structural-induction, every formula has the property \( P \), which proves the lemma.
:::

The proof of (c) gave more than (c) states, and the next proof uses the extra. In a formula \( (\varphi \circ \psi) \), the initial segment before the connective \( \circ \) has excess exactly \( 1 \), and the initial segment before **any other** binary connective has excess at least \( 2 \). In the language of depth: the main connective is the only binary connective at depth one. That is the recipe of Section 4.1 for finding the root of a parse tree.

The three parts were proved together for a reason. The second sentence of (b), alone, cannot be proved by structural induction. For \( (\neg(p \wedge q) \wedge r) \), the initial segment \( (\neg(p \) is \( ( \) followed by the initial segment \( \neg(p \) of the formula \( \neg(p \wedge q) \), and its excess is \( 1 + \operatorname{ex}(\neg(p) \); to know that this is at least \( 1 \), we need \( \operatorname{ex}(\neg(p) \ge 0 \), a fact about an initial segment of a **negation**, which the second sentence of (b) does not cover. The first sentence of (b) does. A property that is too weak to pass through the induction must be strengthened until it does, and here the strengthening is (b)'s first sentence.

## Unique readability

We can now prove what Section 4.1 promised: a formula can be built in only one way.

::: {#thm-unique-readability}
[Unique Readability]

Let \( \chi \) be a formula that is neither an atom nor \( \bot \). Then **exactly one** of the following holds:

::: {.enumerate options="label=(\roman*)"}
1. \( \chi = \neg\varphi \) for a formula \( \varphi \);
2. \( \chi = (\varphi \circ \psi) \) for formulas \( \varphi, \psi \) and a binary connective \( \circ \).
:::

In case (i), \( \varphi \) is **uniquely** determined by \( \chi \); in case (ii), \( \circ \), \( \varphi \) and \( \psi \) are uniquely determined by \( \chi \).
:::

In words: every compound formula has one main connective, and one way of being split into its immediate parts. This is the precise form of Chapter 1's claim that a statement built from letters by connectives can be read in only one way. Existence is the easy half; the content is **uniqueness**. The danger it excludes is a string such as \( p \wedge q \vee r \), which, if it were a formula, could be split at \( \wedge \) or at \( \vee \).

::: {.idea}
Some form holds, by looking at the last step (Section 4.1); the first symbol tells the two forms apart. For case (ii), suppose \( \chi = (\varphi \circ \psi) = (\varphi' \circ' \psi') \). By the remark after @lem-parenthesis-count, each main connective is the only binary connective at depth one; so both sit at the same position of the string, and everything else is forced.
:::

::: {.proof}
By Section 4.1 (looking at the last step), \( \chi \) is an atom, \( \bot \), \( \neg\varphi \) for a formula \( \varphi \), or \( (\varphi \circ \psi) \) for formulas \( \varphi, \psi \); by hypothesis it is one of the last two. It cannot be both, since a string of the form \( \neg\varphi \) begins with \( \neg \) and one of the form \( (\varphi \circ \psi) \) begins with \( ( \).

*Case (i).* If \( \chi = \neg\varphi = \neg\varphi' \), removing the first symbol gives \( \varphi = \varphi' \).

*Case (ii).* Let \( \chi = (\varphi \circ \psi) \). Before the connective \( \circ \) stands the initial segment \( (\varphi \), of excess \( 1 + \operatorname{ex}(\varphi) = 1 \) by @lem-parenthesis-count (a). Before a binary connective inside \( \varphi \) stands \( ( \) followed by an initial segment of \( \varphi \) of excess at least \( 1 \), by @lem-parenthesis-count (c); so the excess is at least \( 2 \). Before a binary connective inside \( \psi \) stands \( (\varphi\,\circ \) followed by an initial segment of \( \psi \) of excess at least \( 1 \), by (c) for \( \psi \) and (a) for \( \varphi \); so again at least \( 2 \). Hence the position of \( \circ \) in \( \chi \) is **the only** position of a binary connective in \( \chi \) whose initial segment before it has excess \( 1 \), and this description mentions only the string \( \chi \).

Now suppose also \( \chi = (\varphi' \circ' \psi') \) for formulas \( \varphi', \psi' \) and a binary connective \( \circ' \). By the same argument, the position of \( \circ' \) is the only position with that description. So \( \circ \) and \( \circ' \) stand at the same position of \( \chi \), and \( \circ = \circ' \). That position is the one just after \( ( \) and \( \varphi \), and also the one just after \( ( \) and \( \varphi' \), so \( \varphi \) and \( \varphi' \) have the same length; both are the string of symbols of \( \chi \) between the first symbol and that position, so \( \varphi = \varphi' \). Likewise \( \psi \) and \( \psi' \) are both the string of symbols between that position and the last symbol, so \( \psi = \psi' \). This proves the theorem.
:::

The theorem settles the question Section 4.1 left open about parse trees.

**Every formula has exactly one parse tree.** We know it has one. That it has only one is proved by structural induction. An atom or \( \bot \) has only the one-node tree, since a tree made by (T2) or (T3) of @def-parse-tree is a tree for a string beginning with \( \neg \) or \( ( \). A parse tree for \( \neg\varphi \) must have been made by (T2), from a parse tree for some \( \varphi' \) with \( \neg\varphi' = \neg\varphi \); so \( \varphi' = \varphi \), and by the induction hypothesis the tree below the root is the one parse tree of \( \varphi \). A parse tree for \( (\varphi \circ \psi) \) must have been made by (T3), from parse trees for some \( \varphi', \psi' \) and a connective \( \circ' \) with \( (\varphi' \circ' \psi') = (\varphi \circ \psi) \); by @thm-unique-readability, \( \circ' = \circ \), \( \varphi' = \varphi \) and \( \psi' = \psi \), and by the induction hypothesis the two subtrees are the parse trees of \( \varphi \) and \( \psi \). From now on we speak of **the** parse tree of a formula, and the height of @def-height is a well-defined number.

## Definition by recursion

Height, the set of atoms, the number of connectives: each is naturally defined **one clause per way of building a formula**. The height of \( \neg\varphi \) is one more than that of \( \varphi \); the atoms of \( (\varphi \circ \psi) \) are those of \( \varphi \) together with those of \( \psi \). Such a definition is called **recursive**: it defines the value at a formula through the values at its immediate parts. The question is whether it really defines something. For a string that could be split in two ways, the clauses might assign two different values, and then they would define nothing. Unique readability says this never happens.

We say **function on formulas** for a rule that assigns to each formula exactly one value; the values may be numbers, truth values, formulas, or collections of atoms. (*Sets, Relations, and Cardinality*, Chapter 1 makes "function" precise; nothing here needs more than the everyday sense.)

*Give a value for each atom and for \( \bot \), and say how to get the value of a compound formula from its parts; then exactly one function on formulas obeys these clauses.*

::: {#thm-structural-recursion}
[Structural Recursion]

Suppose we are given

- a value \( a_p \) for each atom \( p \), and a value \( a_\bot \);
- a rule \( g_\neg \) that produces a value \( g_\neg(\varphi, x) \) from any formula \( \varphi \) and any value \( x \);
- for each binary connective \( \circ \), a rule \( g_\circ \) that produces a value \( g_\circ(\varphi, \psi, x, y) \) from any formulas \( \varphi, \psi \) and any values \( x, y \).

Then there is **exactly one** function \( f \) on formulas such that, for every atom \( p \), all formulas \( \varphi, \psi \) and every binary connective \( \circ \),
\[
\begin{aligned}
f(p) &= a_p, \qquad f(\bot) = a_\bot, \\
f(\neg\varphi) &= g_\neg\bigl(\varphi, f(\varphi)\bigr), \\
f\bigl((\varphi \circ \psi)\bigr) &= g_\circ\bigl(\varphi, \psi, f(\varphi), f(\psi)\bigr).
\end{aligned}
\]
:::

In words: the three lines are the **clauses** of a recursive definition, one for each clause of @def-formula. The rules \( g_\neg \) and \( g_\circ \) may look at the immediate parts themselves as well as at their values; most definitions use only the values, and the list of subformulas below uses the parts. The theorem says the clauses define a function (**existence**) and only one (**uniqueness**).

::: {.idea}
Build the function on short formulas first. A formula with one symbol is an atom or \( \bot \), and the first clauses fix its value. A longer formula has immediate parts that are shorter, whose values are already fixed, and unique readability says which clause applies and to which parts, with no choice left. So the value at each formula is forced, length by length. Formally: an ordinary induction on \( n \), proving that there is exactly one function on the formulas of length at most \( n \) that obeys the clauses.
:::

::: {.proof}
For \( n \in \nN \) with \( n \ge 1 \), call a function \( h \), defined on the formulas of length at most \( n \), **\( n \)-good** if it obeys the three clauses at every formula of length at most \( n \). This makes sense: the immediate parts of a formula are shorter than it, so the clauses at a formula of length at most \( n \) mention values of \( h \) only at formulas of length at most \( n \). Let \( S(n) \) be "there is exactly one \( n \)-good function"; we prove \( S(n) \) for every \( n \ge 1 \) by @ax-induction, started at \( 1 \).

*Base case.* By the first-symbol test (Section 4.1), the formulas of length \( 1 \) are the atoms and \( \bot \). A \( 1 \)-good function must give each atom \( p \) the value \( a_p \) and \( \bot \) the value \( a_\bot \), and the function that does so is \( 1 \)-good, since the other two clauses concern no formula of length \( 1 \). So \( S(1) \) holds.

*Inductive step.* Let \( n \in \nN \) with \( n \ge 1 \), suppose \( S(n) \), and let \( h_n \) be the \( n \)-good function. Define \( h \) on the formulas of length at most \( n + 1 \) as follows. At a formula of length at most \( n \), let \( h \) agree with \( h_n \). Let \( \chi \) have length \( n + 1 \ge 2 \); it is neither an atom nor \( \bot \), so by @thm-unique-readability it is **either** \( \neg\varphi \) for exactly one formula \( \varphi \), **or** \( (\varphi \circ \psi) \) for exactly one \( \circ \), \( \varphi \), \( \psi \); the parts have length at most \( n \). Let \( h(\chi) \coloneqq g_\neg(\varphi, h_n(\varphi)) \) in the first case and \( h(\chi) \coloneqq g_\circ(\varphi, \psi, h_n(\varphi), h_n(\psi)) \) in the second. Unique readability leaves no choice of case or of parts, so this is one value. The function \( h \) is \( (n + 1) \)-good: at formulas of length at most \( n \) it agrees with the \( n \)-good \( h_n \), including at their parts, and at formulas of length \( n + 1 \) it obeys the clauses by construction.

For uniqueness, let \( h' \) be any \( (n + 1) \)-good function. Its restriction to the formulas of length at most \( n \) is \( n \)-good, so it is \( h_n \), by \( S(n) \). At a formula \( \chi = \neg\varphi \) of length \( n + 1 \), the clause for \( \neg \) gives \( h'(\chi) = g_\neg(\varphi, h'(\varphi)) = g_\neg(\varphi, h_n(\varphi)) = h(\chi) \); at \( \chi = (\varphi \circ \psi) \) the same argument with \( g_\circ \) gives \( h'(\chi) = h(\chi) \). So \( h' = h \), and \( S(n + 1) \) holds. By @ax-induction, started at \( 1 \), \( S(n) \) holds for every \( n \ge 1 \); let \( h_n \) denote the \( n \)-good function.

*The function \( f \).* If \( m \ge n \), the restriction of \( h_m \) to the formulas of length at most \( n \) is \( n \)-good, so it is \( h_n \). For a formula \( \chi \) of length \( n \), let \( f(\chi) \coloneqq h_n(\chi) \); then \( f(\chi) = h_m(\chi) \) for every \( m \ge n \). The function \( f \) obeys the clauses: for \( \chi = \neg\varphi \) of length \( m \), \( f(\chi) = h_m(\chi) = g_\neg(\varphi, h_m(\varphi)) = g_\neg(\varphi, f(\varphi)) \), and likewise for the other two clauses. And it is the only one: a function \( f' \) on formulas obeying the clauses restricts, for each \( n \), to an \( n \)-good function, which is \( h_n \); so \( f'(\chi) = h_n(\chi) = f(\chi) \) for a formula \( \chi \) of length \( n \). This proves the theorem.
:::

Unique readability was used at one place: to define \( h(\chi) \) by exactly one clause, applied to exactly one choice of parts. Without it, the clauses could demand two different values at one string, and then no function would obey them.

::: {#exm-recursive-definitions}
[Four recursive definitions]

Each of the following is a function on formulas by @thm-structural-recursion.

- **Height:** \( \hgt(p) = \hgt(\bot) = 1 \), \( \hgt(\neg\varphi) = \hgt(\varphi) + 1 \), and
  \[
  \hgt((\varphi \circ \psi)) = 1 + \max\{\hgt(\varphi), \hgt(\psi)\} .
  \]
- **Atoms:** \( \atoms(p) = \{p\} \); \( \atoms(\bot) \) has no members; \( \atoms(\neg\varphi) = \atoms(\varphi) \); and \( \atoms((\varphi \circ \psi)) \) consists of the members of \( \atoms(\varphi) \) together with those of \( \atoms(\psi) \).
- **Number of connectives:** \( 0 \) for atoms and \( \bot \); one more than for \( \varphi \) at \( \neg\varphi \); one more than the sum for \( \varphi \) and \( \psi \) at \( (\varphi \circ \psi) \).
- **Subformulas:** the list of subformulas of \( p \) is \( p \), and of \( \bot \) is \( \bot \); of \( \neg\varphi \), the formula \( \neg\varphi \) followed by the subformulas of \( \varphi \); of \( (\varphi \circ \psi) \), the formula \( (\varphi \circ \psi) \) followed by the subformulas of \( \varphi \) and then those of \( \psi \), each formula kept only at its first appearance.

Compute all four for \( \chi = (\neg(p \wedge q) \to (q \vee \bot)) \), and also its length.
:::

::: {.solution}
Work up from the leaves. For the parts: \( \hgt(p \wedge q) = 1 + \max\{1, 1\} = 2 \), so \( \hgt(\neg(p \wedge q)) = 3 \); \( \hgt(q \vee \bot) = 2 \). Hence
\[
\hgt(\chi) = 1 + \max\{3, 2\} = 4 .
\]
The atoms of \( \neg(p \wedge q) \) are \( p \) and \( q \), those of \( q \vee \bot \) are just \( q \) (\( \bot \) contributes none), so \( \atoms(\chi) = \{p, q\} \). The connectives: \( \wedge \) and \( \neg \) on the left, \( \vee \) on the right, \( \to \) at the root, four in all. The subformulas, in the order the clause lists them: \( \chi \), \( \neg(p \wedge q) \), \( (p \wedge q) \), \( p \), \( q \), \( (q \vee \bot) \), \( \bot \); the second \( q \) is dropped, being already listed. The length is \( 14 \): the official formula consists of the fourteen symbols
\[
(\ \neg\ (\ p\ \wedge\ q\ )\ \to\ (\ q\ \vee\ \bot\ )\ ) .
\]
:::

Two checks connect these definitions with Section 4.1. The **recursive height agrees with the tree height**: the parse tree of \( \neg\varphi \) is that of \( \varphi \) with one node on top, so each branch gains one node; the tree of \( (\varphi \circ \psi) \) is a new root over the trees of \( \varphi \) and \( \psi \), so a longest branch is the root followed by a longest branch of the taller of the two. A structural induction whose cases are these two sentences (and the one-node tree for atoms and \( \bot \)) shows the two heights are equal. In the same way, the recursive list of subformulas is the list of formulas at the nodes of the parse tree (@def-subformula): the nodes of the tree of \( \neg\varphi \) are its root, carrying \( \neg\varphi \), and the nodes of the tree of \( \varphi \).

The length of a formula also satisfies clauses of this shape, by counting symbols: a formula of length one for atoms and \( \bot \), one more at \( \neg\varphi \), and at \( (\varphi \circ \psi) \) the lengths of \( \varphi \) and \( \psi \) plus \( 3 \) (two parentheses and the connective). For \( \chi \) above: \( (p \wedge q) \) has \( 1 + 1 + 3 = 5 \) symbols, so \( \neg(p \wedge q) \) has \( 6 \); \( (q \vee \bot) \) has \( 5 \); so \( \chi \) has \( 6 + 5 + 3 = 14 \), as counted.

::: {.warning}
A recursive definition must have a clause for **every** way of building a formula, and each clause may use only the **immediate parts**. "Let \( f(\varphi) \) be \( f \) of the longest subformula of \( \varphi \) plus one" is not a recursive definition: at \( \varphi \) itself the longest subformula is \( \varphi \), and the "definition" refers to the value it is trying to define. The theorem applies only to clauses of the form it states.
:::

## Exercises

### A. Check your understanding

<!-- S3-PLACEHOLDER: items -->

### B. Practice

::: {#exr-induction-b2}
[B2]

Prove by structural induction that every formula has at most as many distinct subformulas as it has symbols. Use the recursive description of the subformulas in @exm-recursive-definitions and the clauses for the length given after it.
:::

::: {.solution}
For a formula \( \varphi \), write \( s(\varphi) \) for the number of distinct subformulas of \( \varphi \) and \( \operatorname{len}(\varphi) \) for its length. We prove \( s(\varphi) \le \operatorname{len}(\varphi) \) by @thm-structural-induction.

*Atoms and \( \bot \).* The only subformula is the formula itself: \( s = 1 = \operatorname{len} \).

*Negation.* Suppose \( s(\varphi) \le \operatorname{len}(\varphi) \). The subformulas of \( \neg\varphi \) are \( \neg\varphi \) and those of \( \varphi \), so there are at most \( 1 + s(\varphi) \) of them (fewer if one repeats). Hence \( s(\neg\varphi) \le 1 + s(\varphi) \le 1 + \operatorname{len}(\varphi) = \operatorname{len}(\neg\varphi) \).

*Binary connectives.* Suppose \( s(\varphi) \le \operatorname{len}(\varphi) \) and \( s(\psi) \le \operatorname{len}(\psi) \). The subformulas of \( (\varphi \circ \psi) \) are the formula itself and those of \( \varphi \) and of \( \psi \), so
\[
s((\varphi \circ \psi)) \le 1 + s(\varphi) + s(\psi) \le 1 + \operatorname{len}(\varphi) + \operatorname{len}(\psi) < \operatorname{len}(\varphi) + \operatorname{len}(\psi) + 3 ,
\]
and the right side is \( \operatorname{len}((\varphi \circ \psi)) \).

By @thm-structural-induction, \( s(\varphi) \le \operatorname{len}(\varphi) \) for every formula \( \varphi \). (The bound is far from tight: the parentheses never start a subformula of their own.)
:::

::: {#exr-induction-b3}
[B3]

The number of nodes of the parse tree of a formula is given by the recursion \( \operatorname{nodes}(p) = \operatorname{nodes}(\bot) = 1 \), \( \operatorname{nodes}(\neg\varphi) = \operatorname{nodes}(\varphi) + 1 \), \( \operatorname{nodes}((\varphi \circ \psi)) = \operatorname{nodes}(\varphi) + \operatorname{nodes}(\psi) + 1 \). Prove that every formula \( \varphi \) of height \( h \) satisfies \( \operatorname{nodes}(\varphi) \le 2^{h} - 1 \), and give a formula of height \( 3 \) for which equality holds.
:::

::: {.solution}
We prove \( \operatorname{nodes}(\varphi) \le 2^{\hgt(\varphi)} - 1 \) by @thm-structural-induction, using the recursive height of @exm-recursive-definitions.

*Atoms and \( \bot \).* \( \operatorname{nodes} = 1 = 2^1 - 1 \).

*Negation.* Let \( h = \hgt(\varphi) \) and suppose \( \operatorname{nodes}(\varphi) \le 2^h - 1 \). Then \( \hgt(\neg\varphi) = h + 1 \) and
\[
\operatorname{nodes}(\neg\varphi) \le 2^h - 1 + 1 = 2^h \le 2^{h + 1} - 1 ,
\]
where the last step is \( 1 \le 2^h \).

*Binary connectives.* Let \( a = \hgt(\varphi) \), \( b = \hgt(\psi) \), and suppose the bound for both. Then \( h \coloneqq \hgt((\varphi \circ \psi)) = 1 + \max\{a, b\} \), so \( a \le h - 1 \) and \( b \le h - 1 \), and \( 2^a, 2^b \le 2^{h - 1} \). Hence
\[
\operatorname{nodes}((\varphi \circ \psi)) \le (2^a - 1) + (2^b - 1) + 1 \le 2 \cdot 2^{h - 1} - 1 = 2^h - 1 .
\]

By @thm-structural-induction, the bound holds for every formula. Equality at height \( 3 \): \( ((p \wedge q) \wedge (r \wedge p)) \) has \( 7 = 2^3 - 1 \) nodes (a root, two \( \wedge \) nodes, and four leaves). Equality needs every node above the bottom level to have two children.
:::

### C. Going deeper

::: {#exr-induction-c1}
[C1: Initial segments are not formulas]

::: {.enumerate options="label=(\alph*)"}
1. Prove that no proper initial segment of a formula is a formula.
2. Deduce, in a way different from the proof in the text, the uniqueness part of case (ii) of @thm-unique-readability: if \( (\varphi \circ \psi) = (\varphi' \circ' \psi') \) for formulas \( \varphi, \psi, \varphi', \psi' \) and binary connectives \( \circ, \circ' \), then \( \varphi = \varphi' \), \( \circ = \circ' \) and \( \psi = \psi' \).
:::
:::

::: {.solution}
[Hint 1]

Structural induction on the formula whose initial segments you consider. Which part of @lem-parenthesis-count settles the case \( (\varphi \circ \psi) \) at once?
:::

::: {.solution}
[Hint 2]

For (b): remove the first symbol from both sides. Now both \( \varphi \) and \( \varphi' \) are initial segments of the same string.
:::

::: {.solution}
*(a)* The empty string is not a formula, since every formula has at least one symbol. So it is enough to show that no proper **nonempty** initial segment of a formula \( \chi \) is a formula. We prove this by @thm-structural-induction.

*Atoms and \( \bot \).* A formula of length \( 1 \) has no proper nonempty initial segment.

*Negation.* Suppose no proper nonempty initial segment of \( \varphi \) is a formula, and let \( u \) be a proper nonempty initial segment of \( \neg\varphi \). Then \( u \) is \( \neg \) followed by a proper initial segment \( u' \) of \( \varphi \). Suppose, for a contradiction, that \( u \) is a formula. It begins with \( \neg \), so it is not an atom or \( \bot \) and not of the form \( (\varphi'' \circ \psi'') \); by looking at the last step (Section 4.1), \( u = \neg\varphi'' \) for a formula \( \varphi'' \), and removing the first symbol gives \( u' = \varphi'' \). So \( u' \) is a formula, hence nonempty, and it is a proper nonempty initial segment of \( \varphi \), contradicting the induction hypothesis.

*Binary connectives.* Let \( u \) be a proper nonempty initial segment of \( (\varphi \circ \psi) \). By @lem-parenthesis-count (b), \( \operatorname{ex}(u) \ge 1 \). If \( u \) were a formula, @lem-parenthesis-count (a) would give \( \operatorname{ex}(u) = 0 \). So \( u \) is not a formula. (This case needs no induction hypothesis.)

By @thm-structural-induction, no formula has a proper nonempty initial segment that is a formula, which proves (a).

*(b)* Suppose \( (\varphi \circ \psi) = (\varphi' \circ' \psi') \). Removing the first symbol, the strings \( \varphi \circ \psi) \) and \( \varphi' \circ' \psi') \) are equal. Both \( \varphi \) and \( \varphi' \) are initial segments of this string, so the shorter of the two is an initial segment of the longer. If their lengths differed, the shorter would be a proper initial segment of the longer, and a formula, contradicting (a). So they have the same length, and being initial segments of the same string, \( \varphi = \varphi' \). The next symbol is then \( \circ \) on one side and \( \circ' \) on the other, so \( \circ = \circ' \); what remains is \( \psi) = \psi') \), and removing the last symbol gives \( \psi = \psi' \).

**Marking scheme.** (10 points)

- 1: reduces (a) to nonempty segments (the empty string is not a formula).
- 2: sets up a structural induction with the property "no proper nonempty initial segment is a formula", with the atom and \( \bot \) case.
- 3: negation case: reads the segment as \( \neg \) followed by a proper initial segment of \( \varphi \), and uses the last step of a formula beginning with \( \neg \) to reach a contradiction with the hypothesis.
- 2: binary case: excess at least \( 1 \) by @lem-parenthesis-count (b) against excess \( 0 \) by (a).
- 2: (b): compares \( \varphi \) and \( \varphi' \) as initial segments of one string, concludes equal length by (a), then reads off \( \circ \) and \( \psi \).

Fatal errors (0 for the step): using @thm-unique-readability to prove (b); assuming the lengths of \( \varphi \) and \( \varphi' \) are equal.
:::

::: {#exr-induction-c2}
[C2: Find the error]

The following argument claims to prove that every formula contains an **even** number of parentheses.

::: {.enumerate options="label=(\arabic*)"}
1. We prove, by strong induction on \( n \), that every formula with \( n \) symbols has an even number of parentheses.
2. Let \( n \in \nN \), let \( \chi \) be a formula with \( n \) symbols, and suppose that every formula with fewer than \( n \) symbols has an even number of parentheses.
3. If \( \chi \) is an atom or \( \bot \), it has no parentheses, and \( 0 \) is even.
4. If \( \chi = \neg\varphi \), then \( \varphi \) is a formula with \( n - 1 \) symbols, so by hypothesis it has an even number of parentheses; and \( \chi \) has the same parentheses as \( \varphi \).
5. If \( \chi = (\varphi \circ \psi) \), remove the outer pair of parentheses. The string \( \varphi \circ \psi \) has \( n - 2 \) symbols, so by hypothesis it has an even number of parentheses.
6. Putting the outer pair back adds \( 2 \), so \( \chi \) has an even number of parentheses.
7. By @thm-strong-induction, every formula has an even number of parentheses.
:::

::: {.enumerate options="label=(\alph*)"}
1. Is the conclusion true?
2. Which line fails, and why?
3. Show that the move made in that line is illegal by applying the same move to a different property that every formula has, and reaching a false statement.
4. Repair the argument.
:::
:::

::: {.solution}
*(a)* Yes. By @lem-parenthesis-count (a), a formula has as many left as right parentheses, say \( k \) of each, so \( 2k \) in all.

*(b)* Line 5. The induction hypothesis of line 2 is about **formulas** with fewer than \( n \) symbols, and line 5 applies it to the string \( \varphi \circ \psi \), which is not a formula: for \( \chi = (p \wedge q) \), it is \( p \wedge q \), which fails the first-symbol test of Section 4.1 (length \( 3 \), beginning with an atom). The hypothesis says nothing about such strings. Every other line is correct: line 4 applies the hypothesis to the formula \( \varphi \), and lines 1, 2, 3, 6 and 7 are a correct frame for a strong induction on the length.

*(c)* Take the property of @lem-parenthesis-count (c), that no binary connective lies outside all parentheses; every formula has it. Run the same argument for it: in the case \( \chi = (\varphi \circ \psi) \), line 5's move applies the hypothesis to the string \( \varphi \circ \psi \) and asserts that no binary connective of \( \varphi \circ \psi \) lies outside all parentheses. For \( \chi = (p \wedge q) \) this asserts it of \( p \wedge q \), whose \( \wedge \) lies outside all parentheses. So the move leads from true hypotheses to a false statement; it is not a valid step, even though in the original argument its conclusion happens to be true.

*(d)* In line 5, apply the hypothesis to the formulas \( \varphi \) and \( \psi \), each with fewer than \( n \) symbols: they have \( 2a \) and \( 2b \) parentheses for some integers \( a, b \ge 0 \), and \( \chi \) has \( 2a + 2b + 2 \), which is even. (Alternatively, prove the claim by @thm-structural-induction, with the same three cases.)
:::

::: {#exr-induction-c3}
[C3: Exit check: structural induction]

Say that a formula is a **\( \neg\wedge \)-formula** if its only connectives are \( \neg \) and \( \wedge \) and it does not contain \( \bot \). Define, by @thm-structural-recursion, the number of nodes of the parse tree and the number of negations:
\[
\begin{aligned}
\operatorname{nodes}(p) &= 1, \\
\operatorname{nodes}(\neg\varphi) &= \operatorname{nodes}(\varphi) + 1, \\
\operatorname{nodes}((\varphi \wedge \psi)) &= \operatorname{nodes}(\varphi) + \operatorname{nodes}(\psi) + 1, \\
\operatorname{neg}(p) &= 0, \\
\operatorname{neg}(\neg\varphi) &= \operatorname{neg}(\varphi) + 1, \\
\operatorname{neg}((\varphi \wedge \psi)) &= \operatorname{neg}(\varphi) + \operatorname{neg}(\psi) ,
\end{aligned}
\]
with the clauses for \( \bot \) and the other connectives chosen in any way (say, as for \( \wedge \)). Prove by structural induction that every \( \neg\wedge \)-formula \( \varphi \) satisfies \( \operatorname{nodes}(\varphi) > \operatorname{neg}(\varphi) \).
:::

::: {.solution}
[Hint 1]

@thm-structural-induction is about all formulas. Put the restriction to \( \neg\wedge \)-formulas inside the property.
:::

::: {.solution}
[Hint 2]

Let \( P(\varphi) \) be "if \( \varphi \) is a \( \neg\wedge \)-formula, then \( \operatorname{nodes}(\varphi) > \operatorname{neg}(\varphi) \)". The immediate parts of a \( \neg\wedge \)-formula are \( \neg\wedge \)-formulas.
:::

::: {.solution}
For a formula \( \varphi \), let \( P(\varphi) \) be: "if \( \varphi \) is a \( \neg\wedge \)-formula, then \( \operatorname{nodes}(\varphi) > \operatorname{neg}(\varphi) \)". We prove \( P(\varphi) \) for every formula \( \varphi \) by @thm-structural-induction; for a \( \neg\wedge \)-formula it is the claim.

The immediate parts of a \( \neg\wedge \)-formula are \( \neg\wedge \)-formulas, since every symbol of a part is a symbol of the whole.

*Atoms.* \( \operatorname{nodes}(p) = 1 > 0 = \operatorname{neg}(p) \).

*\( \bot \), and the connectives \( \vee, \to, \leftrightarrow \).* The formulas \( \bot \) and \( (\varphi \circ \psi) \) with \( \circ \) one of \( \vee, \to, \leftrightarrow \) are not \( \neg\wedge \)-formulas, so for them \( P \) holds vacuously, whatever the clauses chosen for them.

*Negation.* Suppose \( P(\varphi) \), and let \( \neg\varphi \) be a \( \neg\wedge \)-formula. Then \( \varphi \) is one, so \( \operatorname{nodes}(\varphi) > \operatorname{neg}(\varphi) \) by \( P(\varphi) \), and adding \( 1 \) to both sides gives \( \operatorname{nodes}(\neg\varphi) > \operatorname{neg}(\neg\varphi) \).

*Conjunction.* Suppose \( P(\varphi) \) and \( P(\psi) \), and let \( (\varphi \wedge \psi) \) be a \( \neg\wedge \)-formula. Then \( \varphi \) and \( \psi \) are, so \( \operatorname{nodes}(\varphi) > \operatorname{neg}(\varphi) \) and \( \operatorname{nodes}(\psi) > \operatorname{neg}(\psi) \). Adding the two inequalities and then \( 1 \),
\[
\operatorname{nodes}((\varphi \wedge \psi)) = \operatorname{nodes}(\varphi) + \operatorname{nodes}(\psi) + 1 > \operatorname{neg}(\varphi) + \operatorname{neg}(\psi) = \operatorname{neg}((\varphi \wedge \psi)) .
\]
(Since the counts are integers, each hypothesis gives at least \( 1 \) to spare, so the left side exceeds the right by at least \( 3 \).)

By @thm-structural-induction, \( P(\varphi) \) holds for every formula, which proves the claim.

**Marking scheme.** (10 points)

- 2: states the property for every formula, in a form that covers exactly the \( \neg\wedge \)-formulas, with the recursive counts.
- 1: atom case.
- 2: negation case, from the hypothesis for \( \varphi \), after checking that \( \varphi \) is a \( \neg\wedge \)-formula.
- 3: conjunction case, using the hypotheses for **both** parts.
- 2: names the induction principle and says why \( \bot \) and the other connectives are harmless (vacuous).

Fatal errors (0 for the step): applying the hypothesis to the formula being proved; a conjunction case that uses one part only and says "similarly" for the other.
:::

<!-- dependency ledger
thm-structural-induction (proof): every entry of a formation sequence is a formula | F1.3 §01, after def-formula (inline there)
lem-parenthesis-count (proof): excess of a concatenation is the sum of the excesses; every initial segment of (phi o psi) is of one of five kinds | inline (counting)
thm-unique-readability (proof): every formula is an atom, bot, neg(phi) or (phi o psi) for formulas ("looking at the last step") | F1.3 §01, after def-formula (inline there)
thm-unique-readability (claim): (paragraph after the proof) each formula has exactly one parse tree | inline structural induction, citing thm-unique-readability
thm-structural-recursion (proof): the first-symbol test (formulas of length 1 are atoms and bot); immediate parts are shorter | F1.3 §01 (inline there); inline
thm-structural-recursion (proof): "function" in the everyday sense | F2.1 (prose pointer); no property of functions beyond "one value per argument" is used
exm-recursive-definitions (example): height 4, atoms {p, q}, 4 connectives, length 14; recursive height = tree height; recursive subformula list = formulas at nodes | inline; checked by verify/ch04/exm-recursive-definitions.py
exr-induction-b2 (solution): a list of subformulas joined from lists of sizes s1, s2 plus one formula has at most 1 + s1 + s2 distinct members; len clauses | school counting; len clauses inline after exm-recursive-definitions
exr-induction-b3 (solution): 2^a <= 2^b for a <= b; 1 <= 2^h; ((p and q) and (r and p)) has 7 nodes | school algebra; checked by verify/ch04/exr-induction-b3.py
exr-induction-c2 (solution): a formula with k left and k right parentheses has 2k in all | lem-parenthesis-count (a)
-->
