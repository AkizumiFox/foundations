# Induction and Recursion on Formulas

Section 4.2 proved statements about every natural number. This section proves statements about every formula in the same way, and with them answers two questions Section 4.1 left open: is every formula read in only one way, and does a definition with one clause per connective define exactly one thing? It ends by showing what goes wrong when an object can be built in two ways.

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

Section 4.2's checklist reads: objects, the formulas; property, \( P(\varphi) \), with any restriction inside it; base cases, every atom and \( \bot \); steps, one for \( \neg \) and one for each binary connective; principle, @thm-structural-induction.

::: {.idea}
Take any formula and a formation sequence ending in it. Walk along the sequence: each entry is an atom or \( \bot \), which has the property by (i), or is built from **earlier** entries, which have it already, by (ii) or (iii). "Earlier entries, any of them" is exactly the shape of strong induction, applied to the position in the list.
:::

```{=latex}
\begin{center}
\begin{tikzpicture}[every node/.style={font=\normalsize}, >=Stealth]
  \node (f1) at (0,0) {$p$};
  \node (f2) at (1.6,0) {$q$};
  \node (f3) at (3.2,0) {$\neg q$};
  \node (f4) at (5.4,0) {$(p \wedge \neg q)$};
  \node (f5) at (8.9,0) {$((p \wedge \neg q) \to p)$};
  \node[font=\scriptsize] (k1) at (0,0.55) {1};
  \node[font=\scriptsize] (k2) at (1.6,0.55) {2};
  \node[font=\scriptsize] (k3) at (3.2,0.55) {3};
  \node[font=\scriptsize] (k4) at (5.4,0.55) {4};
  \node[font=\scriptsize] (k5) at (8.9,0.55) {5};
  \draw[->] (k3.north) to[bend right=50] (k2.north);
  \draw[->] (k4.north) to[bend right=45] (k3.north);
  \draw[->] (k4.north) to[bend right=40] (k1.north);
  \draw[->] (k5.north) to[bend right=40] (k4.north);
  \draw[->] (k5.north) to[bend right=30] (k1.north);
  \node[font=\scriptsize, align=center] at (0,-0.75) {$\checkmark$ by (i)};
  \node[font=\scriptsize, align=center] at (1.6,-0.75) {$\checkmark$ by (i)};
  \node[font=\scriptsize, align=center] at (3.2,-0.75) {$\checkmark$ by (ii),\\ from 2};
  \node[font=\scriptsize, align=center] at (5.4,-0.75) {$\checkmark$ by (iii),\\ from 1 and 3};
  \node[font=\scriptsize, align=center] at (8.9,-0.75) {$\checkmark$ by (iii),\\ from 4 and 1};
\end{tikzpicture}
\end{center}
```

The property spreads from left to right. Each entry gets its check mark from (i), or from entries to its left that already have one.

The proof, in the fold below, makes "from left to right" exact with strong induction on the position in the list.

::: {.second-reading title="The proof of structural induction"}
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
A tempting alternative is induction on the **height** of a formula (the number of nodes on a longest branch of its parse tree, defined later in this section). That route is circular here. The height is read off the parse tree, and that a formula has only one parse tree is proved below from unique readability, whose proof uses structural induction. Inducting on the position in a formation sequence needs nothing but @def-formula.
:::
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

::: {.second-reading title="Sets built from a base"}
Section 4.1 called the formulas the **smallest** collection of strings closed under (F1)–(F3). Here is that sentence made exact.

Call a collection \( C \) of strings **closed** if it contains every atom and \( \bot \), contains \( \neg s \) whenever it contains \( s \), and contains \( (s \circ t) \) whenever it contains \( s \) and \( t \), for each binary connective \( \circ \). The collection of all strings is closed, and closed collections can be much larger than we want.

(i) *Every closed collection \( C \) contains every formula.* Given a formula and a formation sequence \( \chi_1, \dots, \chi_m \) ending in it, show "if \( 1 \le i \le m \), then \( \chi_i \in C \)" for every \( i \in \nN \) by @thm-strong-induction, case by case as in the proof of @thm-structural-induction: each entry is an atom or \( \bot \), or is built by one clause from earlier entries, which are in \( C \) already. The last entry is the formula.

(ii) *The formulas form a closed collection*, by (F1)–(F3).

So the formulas are the smallest closed collection: contained in every closed collection, and one of them. Structural induction is (i) applied to one particular collection. If a property \( P \) satisfies (i)–(iii) of @thm-structural-induction, the collection of formulas that have \( P \) is closed: it contains every atom and \( \bot \) by (i), and the formulas built from members of it are formulas with \( P \), by (ii) and (iii). So it contains every formula. The top-down description ("the smallest closed collection") and the bottom-up one ("whatever a formation sequence reaches") pick out the same strings. The word "collection" keeps its everyday sense here.
:::

## Counting parentheses: the depth profile

Section 4.1 met the string \( p \wedge q \vee r \), which can be read as \( (p \wedge q) \vee r \) or as \( p \wedge (q \vee r) \). With \( p \) and \( q \) false and \( r \) true, the first reading is true and the second false. Section 4.4 defines the truth value of a formula one clause per connective, and the clause to use is decided by the main connective. A string with two main connectives would get two values. Formulas carry parentheses, and the parentheses are meant to settle the reading. This subsection and the next prove that they do, for every formula. The tool is a count.

Read a formula from left to right, keeping a running count: add one at each \( ( \), subtract one at each \( ) \). The count just before a symbol is its **depth**: how many pairs of parentheses are open around it.

```{=latex}
\begin{center}
\begin{tikzpicture}[x=9mm, y=6mm, every node/.style={font=\normalsize}, >=Stealth]
  \draw[->] (-0.8,0) -- (9.4,0);
  \draw[->] (-0.8,0) -- (-0.8,3) node[above, font=\scriptsize] {depth};
  \node[left, font=\scriptsize] at (-0.8,1) {1};
  \node[left, font=\scriptsize] at (-0.8,2) {2};
  \draw[thick] (-0.5,0) -- (0.5,0) -- (0.5,1) -- (1.5,1) -- (1.5,2) -- (5.5,2) -- (5.5,1) -- (8.5,1) -- (8.5,0) -- (9.2,0);
  \node at (0,-0.8) {$($};
  \node at (1,-0.8) {$($};
  \node at (2,-0.8) {$p$};
  \node at (3,-0.8) {$\wedge$};
  \node at (4,-0.8) {$q$};
  \node at (5,-0.8) {$)$};
  \node at (6,-0.8) {$\vee$};
  \node at (7,-0.8) {$r$};
  \node at (8,-0.8) {$)$};
  \draw (6,-0.8) circle [radius=3mm];
  \node[font=\scriptsize, align=center] at (6,-2) {main connective,\\ depth 1};
  \node[font=\scriptsize] at (3,-1.7) {depth 2};
\end{tikzpicture}
\end{center}
```

The depth profile of \( ((p \wedge q) \vee r) \). It starts at 0, stays at 1 or more strictly inside, comes back to 0 only after the last symbol, and the only binary connective at depth 1 is the main connective.

For every formula of the form \( (\varphi \circ \psi) \) the lemma below says the same: (a) the count returns to 0, (b) it never goes below 0 and stays at 1 or more strictly inside, (c) every binary connective is at depth 1 or more. The remark after the proof adds that only the main connective is at depth exactly 1.

We count parentheses in strings, and for this some words about strings.

An **initial segment** of a string \( s \) is the string of the first \( k \) symbols of \( s \), for some \( k \) with \( 0 \le k \le \) the length of \( s \). For \( k = 0 \) it is the **empty** string, with no symbols; for \( k \) equal to the length it is \( s \) itself. An initial segment is **proper** if it is shorter than \( s \). The **excess** of a string \( s \) is
\[
\operatorname{ex}(s) \coloneqq (\text{number of } ( \text{ in } s) - (\text{number of } ) \text{ in } s) .
\]
So a left parenthesis has excess \( 1 \), a right parenthesis \( -1 \), and any other symbol \( 0 \); and the excess of a string written as two strings one after the other is the sum of their excesses, since the counts add. For example, \( \operatorname{ex}(\,(p \wedge (q\,) = 2 \): after reading \( (p \wedge (q \) we are inside two pairs of parentheses that have not yet closed. That is the picture to keep: the excess of an initial segment is the **depth** we are at when we have read that far. So the depth of a symbol is the excess of the initial segment that ends just before it.

::: {#lem-parenthesis-count}
[Parenthesis Count]

Let \( \chi \) be a formula.

::: {.enumerate options="label=(\alph*)"}
1. \( \operatorname{ex}(\chi) = 0 \): \( \chi \) has as many left as right parentheses.
2. Every initial segment \( u \) of \( \chi \) has \( \operatorname{ex}(u) \ge 0 \). If moreover \( \chi \) has the form \( (\varphi \circ \psi) \) and \( u \) is proper and non-empty, then \( \operatorname{ex}(u) \ge 1 \).
3. For every occurrence of a binary connective in \( \chi \), the initial segment of \( \chi \) that ends just before that occurrence has excess at least \( 1 \).
:::
:::

In words: (a) is balance. (b) says that reading a formula from the left, we never close more parentheses than we have opened, and that inside a formula \( (\varphi \circ \psi) \) we stay at depth at least \( 1 \) until the very last symbol. (c) says that no binary connective lies outside all parentheses. Part (a) is the fact we set out to prove; (c), with (a), is what the unique readability theorem needs, and (b) shows that no proper initial segment of a formula is a formula (Exercise C1). The steps for (b) and (c) use (a) for the parts, so the three are proved together. Part (b)'s second sentence, alone, does not pass through the step; that is why the lemma proves more, as @exm-strengthen-the-claim did (fold below).

::: {.idea}
Induction on the shape of a formula, all three parts at once. For \( \neg\varphi \), the extra \( \neg \) changes no count. For \( (\varphi \circ \psi) \), list its initial segments by where they stop: before anything, inside \( \varphi \), at the connective, inside \( \psi \), at the end. Each is "\( ( \)" followed by pieces whose excess the induction hypothesis controls.
:::

::: {.second-reading title="The proof of the parenthesis count"}
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
- \( (\varphi\,\circ \) followed by a non-empty initial segment \( v' \) of \( \psi \): excess \( 1 + 0 + \operatorname{ex}(v') \ge 1 \), by (a) for \( \varphi \) and (b) for \( \psi \);
- \( \chi \) itself: excess \( 0 \), by (a) for \( \chi \).

All five have excess at least \( 0 \). The proper non-empty ones are those of the middle three kinds, and they have excess at least \( 1 \).

*(c)* An occurrence of a binary connective in \( \chi \) is the connective \( \circ \) between \( \varphi \) and \( \psi \), or lies in \( \varphi \), or lies in \( \psi \). Before \( \circ \) stands \( (\varphi \), of excess \( 1 \). Before an occurrence in \( \varphi \) stands \( ( \) followed by the initial segment of \( \varphi \) before it, of excess at least \( 1 + 1 = 2 \) by (c) for \( \varphi \). Before an occurrence in \( \psi \) stands \( (\varphi\,\circ \) followed by the initial segment of \( \psi \) before it, of excess at least \( 1 + 0 + 1 = 2 \) by (a) for \( \varphi \) and (c) for \( \psi \). In all three cases the excess is at least \( 1 \).

So \( P(\chi) \) holds. By @thm-structural-induction, every formula has the property \( P \), which proves the lemma.
:::

The three parts were proved together for a reason. The second sentence of (b), alone, cannot be proved by structural induction. For \( (\neg(p \wedge q) \wedge r) \), the initial segment \( (\neg(p \) is \( ( \) followed by the initial segment \( \neg(p \) of the formula \( \neg(p \wedge q) \), and its excess is \( 1 + \operatorname{ex}(\neg(p) \); to know that this is at least \( 1 \), we need \( \operatorname{ex}(\neg(p) \ge 0 \), a fact about an initial segment of a **negation**, which the second sentence of (b) does not cover. The first sentence of (b) does. A property that is too weak to pass through the induction must be strengthened until it does, and here the strengthening is (b)'s first sentence, as the strengthening of @exm-strengthen-the-claim was \( S_n = \frac{n}{n+1} \).
:::

The proof (in the fold) gives a little more than (c) states, and the next proof uses the extra. In a formula \( (\varphi \circ \psi) \), the initial segment before the connective \( \circ \) has excess exactly \( 1 \), and the initial segment before **any other** binary connective has excess at least \( 2 \). In the language of depth: the main connective is the only binary connective at depth one. That is the recipe of Section 4.1 for finding the root of a parse tree.

::: {.check}
Write down the depth of each symbol of \( (p \wedge (q \vee r)) \). Which binary connective is at depth 1?
:::

::: {.solution}
\( ( \) 0, \( p \) 1, \( \wedge \) 1, \( ( \) 1, \( q \) 2, \( \vee \) 2, \( r \) 2, \( ) \) 2, \( ) \) 1, and 0 after the last symbol. The \( \wedge \) is at depth 1, and it is the main connective. Compare the figure, whose main connective was the \( \vee \).
:::

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

**Every formula has exactly one parse tree.** We know it has one. That it has only one is proved by structural induction. An atom or \( \bot \) has only the one-node tree, since a tree made by (T2) or (T3) of @def-parse-tree is a tree for a string beginning with \( \neg \) or \( ( \). A parse tree for \( \neg\varphi \) must have been made by (T2), from a parse tree for some \( \varphi' \) with \( \neg\varphi' = \neg\varphi \); so \( \varphi' = \varphi \), and by the induction hypothesis the tree below the root is the one parse tree of \( \varphi \). A parse tree for \( (\varphi \circ \psi) \) must have been made by (T3), from parse trees for some \( \varphi', \psi' \) and a connective \( \circ' \) with \( (\varphi' \circ' \psi') = (\varphi \circ \psi) \); by @thm-unique-readability, \( \circ' = \circ \), \( \varphi' = \varphi \) and \( \psi' = \psi \), and by the induction hypothesis the two subtrees are the parse trees of \( \varphi \) and \( \psi \). From now on we speak of **the** parse tree of a formula.

With one parse tree for each formula, a measurement of that tree is a measurement of the formula.

::: {#def-height}
[Height]

The **height** of a formula \( \varphi \), written \( \hgt(\varphi) \), is the number of nodes on a **longest** branch of its parse tree.
:::

Atoms and \( \bot \) have height \( 1 \): their tree is one node, and its only branch has one node. (Some books count edges instead of nodes and give atoms height \( 0 \); with nodes, every formula has height at least \( 1 \).) In @exm-parse-trees, (b) has height \( 4 \), along the branch \( \neg, \wedge, \neg, q \), and (c) has height \( 4 \) too, along \( \vee, \leftrightarrow, \neg, q \) or along \( \vee, \wedge, \to, \bot \).

::: {.warning}
The height counts the nodes on the longest **branch**, not the symbols of the formula. The formula \( \neg(p \wedge \neg q) \) has seven symbols, \( \neg \), \( ( \), \( p \), \( \wedge \), \( \neg \), \( q \), \( ) \), and height \( 4 \); the formula \( ((p \wedge q) \wedge (r \wedge p)) \) has thirteen symbols and height only \( 3 \). Parentheses never count towards the height, and a wide tree can be shallow.
:::

## Definition by recursion

Height, the set of atoms, the number of connectives: each is naturally defined **one clause per way of building a formula**. The height of \( \neg\varphi \) is one more than that of \( \varphi \); the atoms of \( (\varphi \circ \psi) \) are those of \( \varphi \) together with those of \( \psi \). Such a definition is called **recursive**: it defines the value at a formula through the values at its immediate parts. The question is whether it really defines something. For a string that could be split in two ways, the clauses might assign two different values, and then they would define nothing. Unique readability says this never happens.

We say **function on formulas** for a rule that assigns to each formula exactly one value; the values may be numbers, truth values, formulas, or collections of atoms. Nothing here needs more than this everyday sense of "function".

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

::: {.second-reading title="The proof of structural recursion"}
::: {.proof}
For \( n \in \nN \) with \( n \ge 1 \), call a function \( h \), defined on the formulas of length at most \( n \), **\( n \)-good** if it obeys the three clauses at every formula of length at most \( n \). This makes sense: the immediate parts of a formula are shorter than it, so the clauses at a formula of length at most \( n \) mention values of \( h \) only at formulas of length at most \( n \). Let \( S(n) \) be "there is exactly one \( n \)-good function"; we prove \( S(n) \) for every \( n \ge 1 \) by @ax-induction, started at \( 1 \).

*Base case.* By the first-symbol test (Section 4.1), the formulas of length \( 1 \) are the atoms and \( \bot \). A \( 1 \)-good function must give each atom \( p \) the value \( a_p \) and \( \bot \) the value \( a_\bot \), and the function that does so is \( 1 \)-good, since the other two clauses concern no formula of length \( 1 \). So \( S(1) \) holds.

*Inductive step.* Let \( n \in \nN \) with \( n \ge 1 \), suppose \( S(n) \), and let \( h_n \) be the \( n \)-good function. Define \( h \) on the formulas of length at most \( n + 1 \) as follows. At a formula of length at most \( n \), let \( h \) agree with \( h_n \). Let \( \chi \) have length \( n + 1 \ge 2 \); it is neither an atom nor \( \bot \), so by @thm-unique-readability it is **either** \( \neg\varphi \) for exactly one formula \( \varphi \), **or** \( (\varphi \circ \psi) \) for exactly one \( \circ \), \( \varphi \), \( \psi \); the parts have length at most \( n \). Let \( h(\chi) \coloneqq g_\neg(\varphi, h_n(\varphi)) \) in the first case and \( h(\chi) \coloneqq g_\circ(\varphi, \psi, h_n(\varphi), h_n(\psi)) \) in the second. Unique readability leaves no choice of case or of parts, so this is one value. The function \( h \) is \( (n + 1) \)-good: at formulas of length at most \( n \) it agrees with the \( n \)-good \( h_n \), including at their parts, and at formulas of length \( n + 1 \) it obeys the clauses by construction.

For uniqueness, let \( h' \) be any \( (n + 1) \)-good function. Its restriction to the formulas of length at most \( n \) is \( n \)-good, so it is \( h_n \), by \( S(n) \). At a formula \( \chi = \neg\varphi \) of length \( n + 1 \), the clause for \( \neg \) gives \( h'(\chi) = g_\neg(\varphi, h'(\varphi)) = g_\neg(\varphi, h_n(\varphi)) = h(\chi) \); at \( \chi = (\varphi \circ \psi) \) the same argument with \( g_\circ \) gives \( h'(\chi) = h(\chi) \). So \( h' = h \), and \( S(n + 1) \) holds. By @ax-induction, started at \( 1 \), \( S(n) \) holds for every \( n \ge 1 \); let \( h_n \) denote the \( n \)-good function.

*The function \( f \).* If \( m \ge n \), the restriction of \( h_m \) to the formulas of length at most \( n \) is \( n \)-good, so it is \( h_n \). For a formula \( \chi \) of length \( n \), let \( f(\chi) \coloneqq h_n(\chi) \); then \( f(\chi) = h_m(\chi) \) for every \( m \ge n \). The function \( f \) obeys the clauses: for \( \chi = \neg\varphi \) of length \( m \), \( f(\chi) = h_m(\chi) = g_\neg(\varphi, h_m(\varphi)) = g_\neg(\varphi, f(\varphi)) \), and likewise for the other two clauses. And it is the only one: a function \( f' \) on formulas obeying the clauses restricts, for each \( n \), to an \( n \)-good function, which is \( h_n \); so \( f'(\chi) = h_n(\chi) = f(\chi) \) for a formula \( \chi \) of length \( n \). This proves the theorem.
:::

Unique readability was used at one place: to define \( h(\chi) \) by exactly one clause, applied to exactly one choice of parts. Without it, the clauses could demand two different values at one string, and then no function would obey them.
:::

**What goes wrong without it.** The positive integers are built from \( 1 \) by two steps, "add one" and "double"; adding one alone reaches every positive integer. Try to define a function one clause per building step: \( g(1) \coloneqq 0 \), \( g(n + 1) \coloneqq g(n) + 1 \), \( g(2n) \coloneqq g(n) \). The number \( 2 \) is built in two ways, as \( 1 + 1 \) and as twice \( 1 \). The first clause gives \( g(2) = g(1) + 1 = 1 \), the second \( g(2) = g(1) = 0 \), and no function obeys both. The positive integers are not built **freely** by these two steps: one number can come out of two different steps, which is exactly what @thm-unique-readability rules out for formulas.

::: {.check}
Do the clauses \( h(1) \coloneqq 1 \), \( h(n + 1) \coloneqq h(n) + 2 \), \( h(2n) \coloneqq 2h(n) \) define a function on the positive integers?
:::

::: {.solution}
No. At \( 2 \), the first step clause gives \( h(2) = h(1) + 2 = 3 \) and the second \( h(2) = 2h(1) = 2 \).
:::

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

Two checks connect these definitions with the parse trees. The **recursive height agrees with the tree height**: the parse tree of \( \neg\varphi \) is that of \( \varphi \) with one node on top, so each branch gains one node; the tree of \( (\varphi \circ \psi) \) is a new root over the trees of \( \varphi \) and \( \psi \), so a longest branch is the root followed by a longest branch of the taller of the two. A structural induction whose cases are these two sentences (and the one-node tree for atoms and \( \bot \)) shows the two heights are equal. In the same way, the recursive list of subformulas is the list of formulas at the nodes of the parse tree (@def-subformula): the nodes of the tree of \( \neg\varphi \) are its root, carrying \( \neg\varphi \), and the nodes of the tree of \( \varphi \).

The length of a formula also satisfies clauses of this shape, by counting symbols: a formula of length one for atoms and \( \bot \), one more at \( \neg\varphi \), and at \( (\varphi \circ \psi) \) the lengths of \( \varphi \) and \( \psi \) plus \( 3 \) (two parentheses and the connective). For \( \chi \) above: \( (p \wedge q) \) has \( 1 + 1 + 3 = 5 \) symbols, so \( \neg(p \wedge q) \) has \( 6 \); \( (q \vee \bot) \) has \( 5 \); so \( \chi \) has \( 6 + 5 + 3 = 14 \), as counted.

::: {.warning}
A recursive definition must have a clause for **every** way of building a formula, and each clause may use only the **immediate parts**. "Let \( f(\varphi) \) be \( f \) of the longest subformula of \( \varphi \) plus one" is not a recursive definition: at \( \varphi \) itself the longest subformula is \( \varphi \), and the "definition" refers to the value it is trying to define. The theorem applies only to clauses of the form it states.
:::

::: {.remark}
[Looking ahead]

Chapter 5 builds the formulas of predicate logic by clauses of the same kind, and proves things about all of them by inductions of this kind.
:::

## Exercises

### A. Check your understanding

::: {#exr-structural-induction-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Which kind of induction fits "every formula contains an atom or \( \bot \)"? Write down its base cases and the statements of its steps, without proving them.
2. A reader proves "every formula has at least one symbol that is not a parenthesis" by structural induction. They check atoms, the step for \( \neg \), and the step for \( (\varphi \circ \psi) \). Which case is missing? Does the claim hold there?
3. Write down, without proving them, the base cases and the inductive steps of a structural induction for: every formula has exactly as many left parentheses as binary connectives.
4. Which parts of @lem-parenthesis-count does the proof of @thm-unique-readability use, and for which formulas?
5. Why does @thm-structural-recursion not apply to the positive integers built from \( 1 \) by "add one" and "double"?
:::
:::

::: {.solution}
*(a)* Structural induction. Base cases: an atom contains itself, and \( \bot \) contains \( \bot \). Steps: if \( \varphi \) contains an atom or \( \bot \), so does \( \neg\varphi \); if \( \varphi \) and \( \psi \) do, so does \( (\varphi \circ \psi) \), for each binary \( \circ \). (Compare the warning in the section: with "an atom" alone, the case \( \bot \) fails.)

*(b)* The case \( \bot \) is missing. The claim holds there, since \( \bot \) is itself such a symbol. The proof is incomplete, though the claim is true; compare the warning on "every formula contains an atom", where the missing case makes the claim false.

*(c)* Base cases: an atom and \( \bot \) have none of either. Step for \( \neg \): if \( \varphi \) has as many of each, so has \( \neg\varphi \), which adds neither. Step for \( (\varphi \circ \psi) \): if each of \( \varphi, \psi \) has as many of each, the whole adds one left parenthesis and one binary connective.

*(d)* Part (a) for \( \varphi \), to get excess \( 1 \) before the main connective and to get excess \( 1 + 0 \) before the part \( \psi \); part (c) for \( \varphi \) and for \( \psi \), to get excess at least \( 2 \) before every other binary connective. Here \( \chi = (\varphi \circ \psi) \) is the formula being read. Part (b) is not used in that proof.

*(e)* Its proof needs each compound object to be built in exactly one way, which for formulas is unique readability. The number \( 2 \) is built as \( 1 + 1 \) and as twice \( 1 \), so clauses can demand two values at one number. Some clauses happen to agree wherever a number is built twice: \( g(1) \coloneqq 1 \), \( g(n + 1) \coloneqq g(n) + 1 \), \( g(2n) \coloneqq 2g(n) \) is obeyed by \( g(n) = n \). But without unique building nothing guarantees this in advance.
:::

::: {#exr-structural-induction-a2}
[A2: Drill]

The parts run from naming the induction, through computing depths, heights and recursive values, to judging claims and definitions and running the checklist.

::: {.enumerate options="label=(\alph*)"}
1. Which kind of induction proves "every formula has as many left as right parentheses"?
2. Write down the depth of each symbol of \( \neg(p \to \neg q) \). Which binary connective is at depth 1?
3. What is the excess of the initial segment \( ((p \wedge (q \) of \( ((p \wedge (q \vee r)) \to p) \)?
4. Find the main connective of \( ((p \to q) \wedge (r \vee p)) \) by depth.
5. What is the height of \( ((p \wedge q) \vee \neg\neg r) \)?
6. True or false: every subformula of \( \varphi \) other than \( \varphi \) itself has smaller height than \( \varphi \).
7. Compute the recursive height and the recursive list of subformulas of \( \neg(p \vee \neg p) \).
8. Define by recursion the number \( b(\varphi) \) of occurrences of \( \bot \) in \( \varphi \), and compute \( b((\bot \to \neg\bot)) \).
9. Is "\( f(\varphi) \coloneqq f(\varphi) + 1 \) for every formula \( \varphi \)" a definition by recursion?
10. "Every formula has odd length or begins with \( \neg \)." Which case of a structural induction fails, and on which formula does the claim fail?
11. Do the clauses \( g(1) \coloneqq 1 \), \( g(n + 1) \coloneqq g(n) + 1 \), \( g(2n) \coloneqq g(n) + 1 \) define a function on the positive integers built by "add one" and "double"?
12. Run the checklist on "every formula with no \( \neg \) and no \( \bot \) has odd length".
:::
:::

::: {.solution}
(a) Structural induction, or strong induction on the position in a formation sequence, which is how structural induction is proved.

(b) \( \neg \) 0, \( ( \) 0, \( p \) 1, \( \to \) 1, \( \neg \) 1, \( q \) 1, \( ) \) 1, and 0 after. The \( \to \) is at depth 1: it is the main connective of the part inside the parentheses. The main connective of the whole formula is the first \( \neg \).

(c) \( 3 \): three left parentheses, no right one.

(d) The \( \wedge \), the only binary connective at depth 1; the \( \to \) and the \( \vee \) are at depth 2.

(e) \( 1 + \max\{2, 3\} = 4 \).

(f) True. A subformula other than \( \varphi \) sits at a node below the root, and the part of the tree below that node is its parse tree. A longest branch of that part, with the path from the root of \( \varphi \)'s tree down to the node added in front, is a branch of \( \varphi \)'s tree with at least one more node. So \( \varphi \)'s tree has a branch longer than every branch of the subformula's tree.

(g) Height \( 4 \) (\( p \): 1, \( \neg p \): 2, \( (p \vee \neg p) \): 3). List: \( \neg(p \vee \neg p) \), \( (p \vee \neg p) \), \( p \), \( \neg p \).

(h) \( b(p) = 0 \) for every atom \( p \), \( b(\bot) = 1 \), \( b(\neg\varphi) = b(\varphi) \), \( b((\varphi \circ \psi)) = b(\varphi) + b(\psi) \). Value \( 1 + 1 = 2 \).

(i) No. It gives no value at atoms or \( \bot \), and it defines the value at \( \varphi \) from the value at \( \varphi \) itself, not from the immediate parts. No function obeys it, since no number equals itself plus one.

(j) The step for \( (\varphi \circ \psi) \), whose length is \( \operatorname{len}(\varphi) + \operatorname{len}(\psi) + 3 \): the hypothesis allows a part that begins with \( \neg \) and has even length. The claim fails on \( (p \wedge \neg q) \), of length \( 6 \), beginning with \( ( \).

(k) No: \( g(2) = 2 \) and \( g(3) = 3 \) by the first step clause, and then \( g(4) = g(3) + 1 = 4 \) by the first step clause but \( g(4) = g(2) + 1 = 3 \) by the second.

(l) Objects: formulas. Property: "if \( \varphi \) contains no \( \neg \) and no \( \bot \), then its length is odd", the restriction inside. Base cases: an atom (length \( 1 \)), and \( \bot \) (vacuous). Steps: \( \neg\varphi \) is vacuous; for \( (\varphi \circ \psi) \) without \( \neg \) and \( \bot \), its parts satisfy the restriction, so their lengths are odd, and odd \( + \) odd \( + 3 \) is odd. Principle: @thm-structural-induction. (Compare (j): with \( \neg \) allowed the claim fails.)
:::

### B. Practice

::: {#exr-induction-b2}
[B1]

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
[B2]

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

::: {#exr-structural-induction-b3}
[B3: The mirror image of a formula]

Define a function \( m \) on formulas by recursion: \( m(p) = p \) for every atom \( p \), \( m(\bot) = \bot \), \( m(\neg\varphi) = \neg m(\varphi) \), and \( m((\varphi \circ \psi)) = (m(\psi) \circ m(\varphi)) \) for each binary connective \( \circ \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( m((p \to (q \wedge \neg r))) \).
2. Prove that \( m(m(\varphi)) = \varphi \) for every formula \( \varphi \).
3. Prove that \( \hgt(m(\varphi)) = \hgt(\varphi) \) for every formula \( \varphi \).
4. Give a formula \( \varphi \), not an atom or \( \bot \), with \( m(\varphi) = \varphi \).
:::
:::

::: {.solution}
*(a)* \( m((p \to (q \wedge \neg r))) = (m((q \wedge \neg r)) \to p) = ((\neg r \wedge q) \to p) \).

*(b)* By @thm-structural-induction, with \( P(\varphi) \): "\( m(m(\varphi)) = \varphi \)". *Atoms and \( \bot \):* \( m \) fixes them, so \( m(m(p)) = p \) and \( m(m(\bot)) = \bot \). *Negation:* if \( m(m(\varphi)) = \varphi \), then \( m(m(\neg\varphi)) = m(\neg m(\varphi)) = \neg m(m(\varphi)) = \neg\varphi \). *Binary connectives:* if \( m(m(\varphi)) = \varphi \) and \( m(m(\psi)) = \psi \), then
\[
m(m((\varphi \circ \psi))) = m((m(\psi) \circ m(\varphi))) = (m(m(\varphi)) \circ m(m(\psi))) = (\varphi \circ \psi) .
\]

*(c)* By @thm-structural-induction, with the recursive height of @exm-recursive-definitions. *Atoms and \( \bot \):* both sides are \( 1 \). *Negation:* \( \hgt(m(\neg\varphi)) = \hgt(\neg m(\varphi)) = \hgt(m(\varphi)) + 1 = \hgt(\varphi) + 1 = \hgt(\neg\varphi) \). *Binary connectives:*
\[
\hgt(m((\varphi \circ \psi))) = 1 + \max\{\hgt(m(\psi)), \hgt(m(\varphi))\} = 1 + \max\{\hgt(\varphi), \hgt(\psi)\} = \hgt((\varphi \circ \psi)) ,
\]
using the hypothesis for both parts.

*(d)* \( (p \wedge p) \), or \( \neg(q \vee q) \).

**Marking scheme.** (8 points)

- 1: (a).
- 3: (b), all four cases (atoms, \( \bot \), negation, binary).
- 3: (c), with the recursive height and the hypothesis for both parts.
- 1: (d).
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
*(a)* The empty string is not a formula, since every formula has at least one symbol. So it is enough to show that no proper **non-empty** initial segment of a formula \( \chi \) is a formula. We prove this by @thm-structural-induction.

*Atoms and \( \bot \).* A formula of length \( 1 \) has no proper non-empty initial segment.

*Negation.* Suppose no proper non-empty initial segment of \( \varphi \) is a formula, and let \( u \) be a proper non-empty initial segment of \( \neg\varphi \). Then \( u \) is \( \neg \) followed by a proper initial segment \( u' \) of \( \varphi \). Suppose, for a contradiction, that \( u \) is a formula. It begins with \( \neg \), so it is not an atom or \( \bot \) and not of the form \( (\varphi'' \circ \psi'') \); by looking at the last step (Section 4.1), \( u = \neg\varphi'' \) for a formula \( \varphi'' \), and removing the first symbol gives \( u' = \varphi'' \). So \( u' \) is a formula, hence non-empty, and it is a proper non-empty initial segment of \( \varphi \), contradicting the induction hypothesis.

*Binary connectives.* Let \( u \) be a proper non-empty initial segment of \( (\varphi \circ \psi) \). By @lem-parenthesis-count (b), \( \operatorname{ex}(u) \ge 1 \). If \( u \) were a formula, @lem-parenthesis-count (a) would give \( \operatorname{ex}(u) = 0 \). So \( u \) is not a formula. (This case needs no induction hypothesis.)

By @thm-structural-induction, no formula has a proper non-empty initial segment that is a formula, which proves (a).

*(b)* Suppose \( (\varphi \circ \psi) = (\varphi' \circ' \psi') \). Removing the first symbol, the strings \( \varphi \circ \psi) \) and \( \varphi' \circ' \psi') \) are equal. Both \( \varphi \) and \( \varphi' \) are initial segments of this string, so the shorter of the two is an initial segment of the longer. If their lengths differed, the shorter would be a proper initial segment of the longer, and a formula, contradicting (a). So they have the same length, and being initial segments of the same string, \( \varphi = \varphi' \). The next symbol is then \( \circ \) on one side and \( \circ' \) on the other, so \( \circ = \circ' \); what remains is \( \psi) = \psi') \), and removing the last symbol gives \( \psi = \psi' \).

**Marking scheme.** (10 points)

- 1: reduces (a) to non-empty segments (the empty string is not a formula).
- 2: sets up a structural induction with the property "no proper non-empty initial segment is a formula", with the atom and \( \bot \) case.
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

::: {#exr-structural-induction-c4}
[C4: Challenge: Inside the folded proofs]

*These parts are about the proofs in the second-reading folds of this section; read the folds first.*

::: {.enumerate options="label=(\alph*)"}
1. In the proof of @thm-structural-induction, on what is the strong induction performed?
2. Where in the proof of @thm-structural-recursion is @thm-unique-readability used, and why is it not needed for uniqueness?
3. In the fold "Sets built from a base", prove part (i).
:::
:::

::: {.solution}
*(a)* On the position \( i \) of an entry in a formation sequence \( \chi_1, \dots, \chi_m \) of the given formula, with the property "if \( 1 \le i \le m \), then \( \chi_i \) has \( P \)". Not on the height, which at that point is not yet known to be well defined.

*(b)* In the inductive step, to define \( h(\chi) \) for a formula \( \chi \) of length \( n + 1 \): unique readability says which clause applies and to which parts, so the clauses give exactly one value. That two functions obeying the clauses agree needs no unique readability: by @thm-structural-induction, if \( f \) and \( f' \) both obey the clauses, they agree at atoms and \( \bot \); and if they agree at \( \varphi \) (and \( \psi \)), then at \( \neg\varphi \) both equal \( g_\neg(\varphi, f(\varphi)) \), and at \( (\varphi \circ \psi) \) both equal \( g_\circ(\varphi, \psi, f(\varphi), f(\psi)) \), whichever way the string may be split.

*(c)* Let \( C \) be a closed collection, \( \chi \) a formula, and \( \chi_1, \dots, \chi_m \) a formation sequence with \( \chi_m = \chi \). We prove, by @thm-strong-induction on \( i \), the property "if \( 1 \le i \le m \), then \( \chi_i \in C \)". Let \( i \in \nN \) and suppose the property for every \( k < i \). If \( i = 0 \) or \( i > m \), it holds vacuously. Otherwise: an atom or \( \bot \) is in \( C \); if \( \chi_i = \neg\chi_j \) with \( j < i \), then \( \chi_j \in C \) by hypothesis, so \( \chi_i \in C \); if \( \chi_i = (\chi_j \circ \chi_l) \) with \( j, l < i \), then \( \chi_j, \chi_l \in C \), so \( \chi_i \in C \). By @thm-strong-induction the property holds for every \( i \), and at \( i = m \) it gives \( \chi \in C \). Since every formula is the last entry of some formation sequence, every formula is in \( C \).

**Marking scheme.** (6 points)

- 2: (a).
- 2: (b).
- 2: (c): 1 for the strong induction set up on positions, 1 for the three cases.
:::

::: {#exr-structural-induction-c5}
[C5: Challenge: formulas without parentheses]

Write connectives in front of their parts and drop all parentheses. The **Polish formulas** are given by the clauses: every atom and \( \bot \) is a Polish formula; if \( \varphi \) is one, so is \( \mathsf{N}\varphi \); if \( \varphi \) and \( \psi \) are, so are \( \mathsf{K}\varphi\psi \), \( \mathsf{A}\varphi\psi \), \( \mathsf{C}\varphi\psi \) and \( \mathsf{E}\varphi\psi \) (for \( \wedge, \vee, \to, \leftrightarrow \)); and nothing else is. Give each symbol a **weight**: \( +1 \) for an atom or \( \bot \), \( 0 \) for \( \mathsf{N} \), \( -1 \) for each of \( \mathsf{K}, \mathsf{A}, \mathsf{C}, \mathsf{E} \). The weight \( w(u) \) of a string \( u \) is the sum of the weights of its symbols.

::: {.enumerate options="label=(\alph*)"}
1. Write \( ((p \wedge \neg q) \to p) \) and \( \neg(p \vee (q \leftrightarrow r)) \) as Polish formulas.
2. Prove that every Polish formula has weight \( 1 \), and that every proper initial segment of it (the empty one included) has weight at most \( 0 \).
3. Deduce that if \( \mathsf{K}\varphi\psi \) and \( \mathsf{K}\varphi'\psi' \) are the same string, for Polish formulas \( \varphi, \psi, \varphi', \psi' \), then \( \varphi = \varphi' \) and \( \psi = \psi' \).
4. Read \( \mathsf{C}\mathsf{A}pq\mathsf{N}r \) by the count, and write it in ordinary notation.
:::
:::

::: {.solution}
[Hint 1]

(b) is a structural induction over the Polish clauses, set up as in the proof of @thm-structural-induction, with a strengthened property, as in @lem-parenthesis-count.
:::

::: {.solution}
[Hint 2]

(c): if \( \varphi \ne \varphi' \), one of them is a proper initial segment of the other.
:::

::: {.solution}
*(a)* \( \mathsf{C}\mathsf{K}p\mathsf{N}qp \) and \( \mathsf{N}\mathsf{A}p\mathsf{E}qr \).

*(b)* By induction over the clauses, the property being "weight \( 1 \), and every proper initial segment has weight \( \le 0 \)".

*Atom or \( \bot \).* Weight \( 1 \); its only proper initial segment is the empty string, of weight \( 0 \).

*\( \mathsf{N}\varphi \).* Weight \( 0 + 1 = 1 \). A proper initial segment is empty (weight \( 0 \)), or \( \mathsf{N} \) followed by a proper initial segment \( u \) of \( \varphi \) (weight \( 0 + w(u) \le 0 \)).

*\( \mathsf{K}\varphi\psi \)* (and likewise \( \mathsf{A}, \mathsf{C}, \mathsf{E} \)). Weight \( -1 + 1 + 1 = 1 \). A proper initial segment is of one of four kinds: empty (weight \( 0 \)); \( \mathsf{K} \) followed by an initial segment \( u \) of \( \varphi \) other than \( \varphi \) itself (weight \( -1 + w(u) \le -1 \)); \( \mathsf{K}\varphi \) (weight \( -1 + 1 = 0 \)); or \( \mathsf{K}\varphi \) followed by a proper non-empty initial segment \( u \) of \( \psi \) (weight \( 0 + w(u) \le 0 \)).

*(c)* Both \( \varphi \) and \( \varphi' \) begin at the second symbol. If they differ, the shorter is an initial segment of the longer (both are initial segments of the string after \( \mathsf{K} \)), a proper one, and non-empty, since every Polish formula has a symbol. By (b) the shorter has weight \( 1 \), and as a proper initial segment of the longer it has weight \( \le 0 \): impossible. So \( \varphi = \varphi' \), and \( \psi \), \( \psi' \) are both what follows \( \mathsf{K}\varphi \): equal.

*(d)* Read from the symbol after \( \mathsf{C} \): the running weight is \( -1 \) after \( \mathsf{A} \), \( 0 \) after \( p \), and first reaches \( 1 \) after \( q \). By (b), a Polish formula ends exactly where its running weight first reaches \( 1 \), so the first part of \( \mathsf{C} \) is \( \mathsf{A}pq \) and the second is \( \mathsf{N}r \). (From the first symbol the running weight is \( -1, -2, -1, 0, 0, 1 \), reaching \( 1 \) only at the end.) In ordinary notation: \( ((p \vee q) \to \neg r) \).

**Marking scheme.** (10 points)

- 2: (a).
- 4: (b), with the induction set up over the clauses and all three kinds of non-empty proper initial segment of \( \mathsf{K}\varphi\psi \).
- 3: (c), with the non-emptiness of the shorter part named.
- 1: (d).

Fatal errors (0 for the step): in (b), proving only "weight \( 1 \)" (then (c) has nothing to use: the strengthening is the point); in (c), assuming the two parts have equal length.
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
def-height (claim): "the" parse tree, hence the height, is well defined | thm-unique-readability (this section), proved just before
thm-structural-induction (claim): (the check-mark figure) the formation sequence p, q, neg q, (p and neg q), ((p and neg q) -> p) and the sources of each entry | the build-up figure of F1.3 §01, same sequence and arrows
thm-structural-induction (claim): (fold "Sets built from a base") collection, closed collection, smallest | everyday sense; F2.1 (promised, STATUS row "smallest closed set")
lem-parenthesis-count (claim): (the hook) the string p and q or r with two readings takes values T and F at p = F, q = F, r = T | the readings of "and" and "or" of Chapter 1, as computed again by the truth tables of F1.3 §04; motivation only, used in no proof; checked by verify/ch04/lem-parenthesis-count.py
lem-parenthesis-count (claim): depth profiles of ((p and q) or r) (figure) and (p and (q or r)) (Quick check); the depth of a symbol is the excess of the initial segment before it | inline counting, from the definition of excess; checked by verify/ch04/lem-parenthesis-count.py
thm-structural-recursion (claim): (the non-example) adding one alone reaches every positive integer; g(2) gets 1 and 0; h(2) gets 3 and 2 (Quick check) | ax-induction (started at 1); inline arithmetic; checked by verify/ch04/thm-structural-recursion.py
exr-structural-induction-a1 (solution): (e) g(n) = n obeys g(1) = 1, g(n+1) = g(n) + 1, g(2n) = 2g(n) | inline arithmetic; checked by verify/ch04/thm-structural-recursion.py
exr-structural-induction-a2 (solution): depths, excess 3, heights 4 and 4, the subformula list, b = 2, the length 6 of (p and neg q), the clash at g(4) | inline counting; checked by verify/ch04/exr-structural-induction-a2.py
exr-structural-induction-b3 (solution): m is an involution and keeps the height; m((p -> (q and neg r))) = ((neg r and q) -> p) | thm-structural-induction, thm-structural-recursion (this section); checked by verify/ch04/exr-structural-induction-b3.py
exr-structural-induction-c4 (solution): (c) strong induction on the position in a formation sequence | thm-strong-induction (F1.3 §02); thm-structural-induction's proof pattern (this section)
exr-structural-induction-c5 (solution): induction over the Polish clauses | thm-structural-induction's proof pattern, cited (this section); the Polish clauses are the item's own definition; checked by verify/ch04/exr-structural-induction-c5.py
-->
