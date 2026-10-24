# Terms, Formulas, Free Variables and Substitution

Section 5.1 read quantified sentences by eye. That is enough to understand them, and not enough to reason with them: every quantifier rule of Sections 5.3 to 5.5, and the rule for using an equation in Section 5.7, has the form "put the term \( t \) in for the variable \( x \) in \( \varphi \)", written \( \varphi[t/x] \), and a rule has to say exactly which symbols change. This section makes the language of Section 5.1 exact, in the way Section 4.1 made the propositional language exact, says exactly what \( \varphi[t/x] \) does, and names the one way it goes wrong, **capture**.

## Which letters are holes

Three sentences, over the domain \( \nN \):

- "\( x > 2 \)" is not a statement. It is the open sentence of item (e) of @exm-statements, true for some values of \( x \) and false for others.
- "\( \forall x\, (x^2 \ge 0) \)" is a statement, and a true one. The letter \( x \) still appears, but the quantifier has closed its hole: the sentence does not ask which \( x \) we mean.
- "\( \forall x\, (x \ge y) \)" is neither true nor false as it stands. It is true when \( y \) is \( 0 \) (every natural number is at least \( 0 \)) and false when \( y \) is \( 1 \) (the number \( 0 \) is not at least \( 1 \)). It is an open sentence **in \( y \)**, although it begins with a quantifier.

So the question "is this a statement?" is not answered by looking for quantifiers. It is answered by asking which letters are still holes. In the third sentence \( x \) is closed by \( \forall x \) and \( y \) is open. The open letters will be called **free**, and the closed ones **bound**.

Here is why the difference matters for reasoning. Over \( \nN \), the sentence
\[
\exists y\, (y \ne x)
\]
is an open sentence in \( x \), and it is true for every \( x \): given \( x \), the number \( y = x + 1 \) differs from it. Now suppose that we want to say the same thing about a particular number named by another letter, and we put \( y \) in for \( x \) without thinking. The result is
\[
\exists y\, (y \ne y),
\]
"some number differs from itself", which is false. Nothing about numbers went wrong. The \( y \) that we put in landed inside the scope of \( \exists y \), and the quantifier took hold of it: the new \( y \) was meant to name a number from outside, and it has become the quantifier's own placeholder. This is **capture**.

Capture is the one trap of substitution, and the rules of Sections 5.3 to 5.7 substitute at almost every step. So we need exact answers to three questions: what the expressions are that can be put in; which occurrences of \( x \) get replaced; and when putting \( t \) in for \( x \) is safe.

## Terms and formulas

The first things to build are the names of objects.

*A term is a name of an object, built from variables and constants by function symbols.*

::: {#def-term}
[Term]

The **terms** are the strings given by the following clauses.

::: {.enumerate options="label=(Tm\arabic*)"}
1. Every variable is a term, and every constant symbol is a term.
2. If \( f \) is a function symbol of arity \( n \) and \( t_1, \dots, t_n \) are terms, then \( f(t_1, \dots, t_n) \) is a term.
3. **Nothing else** is a term: a string is a term **only if** it is the last entry of a finite list of strings in which every entry is a variable, a constant symbol, or \( f(s_1, \dots, s_n) \) for some function symbol \( f \) of arity \( n \) and **earlier** entries \( s_1, \dots, s_n \).
:::
:::

In words: variables and constants are terms, a function symbol applied to as many terms as it has places is a term, and nothing else is.

A **variable of** a term \( t \) is a variable that occurs in \( t \). A term with no variables, such as \( 2 \) or \( f(c) \), names one fixed object once the symbols are interpreted; a term with variables, such as \( x + 1 \), names an object only once its variables have values.

**Shorthand.** We write terms in the familiar way: \( x + y \) for \( +(x, y) \), \( x^2 \), \( \abs{x} \), \( a_n \) for \( a(n) \) (a sequence is a function symbol, as Section 5.1 said). School conventions about grouping say which term is meant.

Here are terms, simplest first.

- \( x \) and \( 2 \): by (Tm1). The degenerate terms, built in no steps; every argument about all terms has to handle them.
- \( x + 1 \), officially \( +(x, 1) \): by (Tm2) from the terms \( x \) and \( 1 \).
- \( f(f(c)) \): by (Tm2) twice, from \( c \), for a one-place \( f \). Its only building blocks are constants, so it has no variables.
- \( \abs{a_n - L} \), officially \( \abs{\cdot}\bigl( -(a(n), L) \bigr) \), with the two-place minus: by (Tm2) three times, from the variables \( n \) and \( L \). Its variables are \( n \) and \( L \). The letter \( a \) is a function symbol, not a variable.

::: {.second-reading title="The symbols of the language, strings that are not terms, and two more shorthand rules"}
Section 4.1 described the propositional language by its alphabet and its formation rules. The language of predicate logic has more symbols, of more kinds.

- **Variables:** \( x, y, z, u \), with subscripts \( x_0, x_1, y_0, \dots \), and in analysis also \( \varepsilon, \delta, N, n, k, L \). There are infinitely many, so that a fresh one is always available. Each is one symbol.
- **Constant symbols**, such as \( 0 \), \( 1 \), \( 2 \), \( a \), \( b \), \( c \). (A letter may be a constant in one language and a function symbol in another: in a language with a sequence, \( a \) is the sequence's one-place function symbol, as below, and not a constant.)
- **Function symbols**, each with a number of places \( n \ge 1 \), its **arity**: \( f \) and \( g \), the arithmetic symbols \( + \), \( \cdot \) and \( - \) (two places), and \( - \) in front of a number, halving \( \cdot/2 \), squaring and \( \abs{\cdot} \) (one place). The one-place and the two-place minus are different symbols written alike; the number of terms they are applied to shows which is meant.
- **Predicate symbols**, each with an arity \( n \ge 1 \): \( P, Q, R, S \), \( < \), \( \le \), \( > \), \( \ge \), \( \mathrm{Prime} \), and \( \in A \) for a fixed set \( A \) (one place, as in Section 5.1).
- **Equality** \( = \), which every language has.
- The constant \( \bot \), the connectives \( \neg, \wedge, \vee, \to, \leftrightarrow \) of Chapter 4, and the **quantifier symbols** \( \forall \) and \( \exists \).
- Parentheses \( ( \), \( ) \), and the comma.

Which constant, function, and predicate symbols are available depends on the subject. For the argument of Section 5.1 we need the constant \( 2 \) and the one-place predicate symbols \( P \) and \( S \). For arithmetic we need \( 0 \), \( 1 \), \( + \), \( \cdot \), and \( < \). Every formula uses only finitely many symbols, and we never need to fix the whole list in advance.

Strings that are **not** terms, each by one clause:

- \( x < 1 \) is not a term. It does not name an object; it says something about one. It is built with a predicate symbol, and (Tm2) uses only function symbols. It will be a formula.
- \( f(x, y) \), for a one-place \( f \), is not a term: (Tm2) applies \( f \) to exactly one term.

Terms can be drawn as trees, exactly as formulas were in Section 4.1: a variable or a constant is a single node, and \( f(t_1, \dots, t_n) \) is a node labeled \( f \) with the trees of \( t_1, \dots, t_n \) below it, in order. And a term can be read in only one way. The proof is the proof of unique readability for formulas in Section 4.3 (@thm-unique-readability), with the parentheses and commas of (Tm2) doing the work that the parentheses of (F3) did there. We do not repeat it.

**Shorthand rules 1 and 3.**

**Rule 1.** Two-place predicate symbols such as \( <, \le \) are written between their terms: \( x < y \) is shorthand for \( <(x, y) \). The one-place symbol \( \in A \) is written after its term: \( t \in A \) is shorthand for \( (\in A)(t) \). (When sets are themselves objects of the domain, \( \in \) is a two-place predicate symbol and \( x \in A \) is \( \in(x, A) \); in this chapter \( A \) is a fixed set, except in one example of Section 5.7 where sets are the objects, so we treat \( \in A \) as one-place.) We write \( t_1 \ne t_2 \) for \( \neg(t_1 = t_2) \).
**Rule 3.** The bounded quantifiers of @def-bounded-quantifier, \( \forall x \in A \; \varphi \) and the rest, stand for the formulas given there.
:::

Next, the statements and open sentences. Atomic formulas say something about terms; everything else is built from them by connectives and quantifiers.

*A first-order formula is built from predicates applied to terms, by the connectives and the two quantifiers.*

::: {#def-first-order-formula}
[First-Order Formula]

The **formulas** (of predicate logic, or **first-order formulas**) are the strings given by the following clauses.

::: {.enumerate options="label=(Fm\arabic*)"}
1. **Atomic formulas.** If \( R \) is a predicate symbol of arity \( n \) and \( t_1, \dots, t_n \) are terms, then \( R(t_1, \dots, t_n) \) is a formula. If \( t_1 \) and \( t_2 \) are terms, then \( t_1 = t_2 \) is a formula. And \( \bot \) is a formula.
2. If \( \varphi \) is a formula, then \( \neg\varphi \) is a formula.
3. If \( \varphi \) and \( \psi \) are formulas, then \( (\varphi \wedge \psi) \), \( (\varphi \vee \psi) \), \( (\varphi \to \psi) \), and \( (\varphi \leftrightarrow \psi) \) are formulas.
4. If \( \varphi \) is a formula and \( x \) is a **variable**, then \( \forall x\, \varphi \) and \( \exists x\, \varphi \) are formulas.
5. **Nothing else** is a formula: a string is a formula only if it is the last entry of a finite list in which every entry is an atomic formula, or is built by (Fm2), (Fm3) or (Fm4) from **earlier** entries.
:::
:::

- *(Fm1)*: the atomic formulas, a predicate symbol with its terms, or an equation, or \( \bot \), take the place of Chapter 4's atoms.
- *(Fm2)*, *(Fm3)*: the connectives, as before.
- *(Fm4)*: puts \( \forall x \) or \( \exists x \), with a **variable** \( x \), in front of a formula, without parentheses, as \( \neg \) is.

Structural induction and recursion (@thm-structural-induction, @thm-structural-recursion) carry over to terms and first-order formulas, with the atomic formulas as base case and one new building step for each quantifier (the fold below says how).

::: {.second-reading title="Induction and recursion on formulas"}
The base case covers every **atomic** formula (and \( \bot \)), and there are two new building steps, from \( \varphi \) to \( \forall x\, \varphi \) and to \( \exists x\, \varphi \), for every variable \( x \), each with one part, like the step to \( \neg\varphi \). So, to prove that every formula has a property, prove it for the atomic formulas and \( \bot \), and prove that it passes from \( \varphi \) to \( \neg\varphi \), \( \forall x\, \varphi \), and \( \exists x\, \varphi \), and from \( \varphi, \psi \) to \( (\varphi \circ \psi) \). To define a function on formulas, give one clause for each of these cases. The proofs in Section 4.3 go through word for word with the new cases added, and unique readability holds for the same reason; we use all three without repeating them. The same two principles hold for terms, with (Tm1) as the base case and (Tm2) as the one building step.
:::

**Shorthand.** The conventions of Section 4.1 for dropping parentheses stay, with three additions. Rules 1 and 3 (predicate symbols written between their terms, as in \( x < y \); bounded quantifiers as abbreviations) are in the fold on the symbols of the language, above; rule 2 matters in every section:

**Rule 2. A quantifier binds as tightly as \( \neg \)**: it applies to the smallest formula that follows it. So \( \forall x\, P(x) \to Q(c) \) stands for \( (\forall x\, P(x) \to Q(c)) \), an implication whose hypothesis is \( \forall x\, P(x) \). For the quantifier to govern the whole implication, write \( \forall x\, (P(x) \to Q(x)) \), where the parentheses are the official ones around the implication.

Rule 2 matters in every rule section. The formula \( \forall x\, P(x) \to Q(c) \) has main connective \( \to \), while \( \forall x\, (P(x) \to Q(x)) \) has main symbol \( \forall x \). The rule for using a "for every" (Section 5.3) applies only to the second.

**Parse trees.** A parse tree for a first-order formula is drawn as in Section 4.1, with one new kind of node: a **quantifier node**, labeled \( \forall x \) or \( \exists x \), with the tree of the formula it governs as its only subtree. The leaves are atomic formulas (or \( \bot \)); their terms have trees of their own, which we do not draw. Here is the tree of \( \forall x\, \bigl( P(x) \to \exists y\, R(x, y) \bigr) \).

\begin{center}
\begin{tikzpicture}[level distance=10mm, sibling distance=22mm, every node/.style={font=\normalsize}]
  \node {$\forall x$}
    child { node {$\to$}
      child { node {$P(x)$} }
      child { node {$\exists y$}
        child { node {$R(x, y)$} }
      }
    };
\end{tikzpicture}
\end{center}

The root is the quantifier node \( \forall x \), so the formula's main symbol is \( \forall x \). Below it is the implication, with the atomic formula \( P(x) \) on the left and the quantifier node \( \exists y \) on the right, which governs the atomic formula \( R(x, y) \).

::: {.check}
Draw the parse tree of \( \forall x\, P(x) \to \exists y\, \forall x\, R(x, y) \), written in shorthand. What is its main symbol?
:::

::: {.solution}
By shorthand rule 2, each quantifier applies to the smallest formula after it, so the official formula is \( (\forall x\, P(x) \to \exists y\, \forall x\, R(x, y)) \) and its main symbol is \( \to \). The root is \( \to \). Its left subtree is the node \( \forall x \) above the leaf \( P(x) \). Its right subtree is the node \( \exists y \), below it the node \( \forall x \), and below that the leaf \( R(x, y) \). The two \( \forall x \) nodes are on different branches.
:::

## Free and bound: drawing the arrows

The parse tree shows which quantifier governs which part of a formula. That is exactly what decides whether a letter is a hole. Draw an arrow from each occurrence of a variable to the nearest quantifier on that variable above it in the parse tree. An occurrence with an arrow is bound; one with none is a hole still open.

```{=latex}
\begin{center}
\begin{tikzpicture}[every node/.style={inner xsep=0pt, inner ysep=2pt, outer sep=0pt, font=\normalsize}]
  \node[anchor=base] (s1) at (0,0) {$P($};
  \node[base right=0pt of s1] (x1) {$x$};
  \node[base right=0pt of x1] (s2) {$) \wedge {}$};
  \node[base right=0pt of s2] (qx) {$\forall x$};
  \node[base right=0pt of qx] (s3) {$\,(Q($};
  \node[base right=0pt of s3] (x2) {$x$};
  \node[base right=0pt of x2] (s4) {$) \to {}$};
  \node[base right=0pt of s4] (qy) {$\exists y$};
  \node[base right=0pt of qy] (s5) {$\,R($};
  \node[base right=0pt of s5] (x3) {$x$};
  \node[base right=0pt of x3] (s6) {$,\,$};
  \node[base right=0pt of s6] (y1) {$y$};
  \node[base right=0pt of y1] (s7) {$))$};
  \draw[->] (x2.north) .. controls +(0,0.6) and +(0,0.6) .. ([xshift=1pt]qx.north);
  \draw[->] (x3.north) .. controls +(0,1.3) and +(0,1.3) .. ([xshift=-1pt]qx.north);
  \draw[->] (y1.north) .. controls +(0,0.6) and +(0,0.6) .. (qy.north);
  \draw ([yshift=-1pt]x1.south west) -- ([yshift=-1pt]x1.south east);
  \node[below=4pt of x1, font=\small] {free};
\end{tikzpicture}
\end{center}
```

**Figure B.** Each bound occurrence points to its quantifier. The first \( x \) points nowhere: it is free.

*An occurrence of a variable is bound if a quantifier on that variable stands above it in the parse tree; otherwise it is free.*

::: {#def-free-variable}
[Free and Bound Variables]

Let \( \varphi \) be a formula and \( x \) a variable. An **occurrence** of \( x \) in \( \varphi \) is an appearance of \( x \) inside one of the terms of an atomic formula of \( \varphi \). (The \( x \) written just after a quantifier symbol, as in \( \forall x \), is part of the quantifier node and is not an occurrence.)

- An occurrence of \( x \) is **bound** if the path from its leaf up to the root of the parse tree passes through a quantifier node \( \forall x \) or \( \exists x \), with the **same** variable \( x \). The lowest such node **binds** the occurrence.
- An occurrence that is not bound is **free**.
- The **scope** of a quantifier node is the part of the tree below it: the formula it governs.
- The variable \( x \) is a **free variable of** \( \varphi \), or is **free in** \( \varphi \), if at least one occurrence of \( x \) in \( \varphi \) is free.
:::

A variable **appears in** \( \varphi \) if it is written anywhere in \( \varphi \): inside a term, or just after a quantifier symbol. Every freshness condition of this chapter is stated with "appear"; in practice, a fresh letter is one written nowhere yet.

::: {#def-sentence}
[Sentence]

A **sentence** is a formula with no free variables.
:::

A sentence is what Chapter 1 called a statement, once the domain and the symbols are fixed: every hole is closed, so it is true or false. A formula with free variables is an open sentence, true or false only once values are given to its free variables.

Examples. The domain is irrelevant to all of them: being free or bound is a matter of the string, not of what it means.

- \( \forall x\, (x \ge y) \): the occurrence of \( x \) is bound by \( \forall x \); the occurrence of \( y \) has no quantifier on \( y \) above it, so it is free. The free variables are \( y \) alone. Not a sentence.
- \( P(x) \wedge \forall x\, Q(x) \): the occurrence of \( x \) in \( P(x) \) is **free** (no quantifier stands above it: the \( \forall x \) governs only \( Q(x) \)), and the occurrence in \( Q(x) \) is bound. So \( x \) is a free variable of this formula, and it is not a sentence.
- \( \forall x\, \exists x\, P(x) \): the occurrence of \( x \) has two quantifiers on \( x \) above it, and the lower one, \( \exists x \), binds it. The outer \( \forall x \) binds nothing. A sentence.

::: {.second-reading title="Occurrences, 'appear', and the recursive description of 'free'"}
In words: an occurrence of \( x \) is bound when it lies in the scope of a quantifier on \( x \); quantifiers on other variables do not bind it. If several quantifiers on \( x \) stand above it, the nearest one, the lowest in the tree, is the one that binds it. A free occurrence is a hole still open. A variable is free in a formula if it has **at least one** free occurrence, even if it has bound occurrences too.

So \( y \) appears in \( \forall y\, P(x) \), although it has no occurrence there. A variable that does not appear in \( \varphi \) has no occurrence in \( \varphi \), and no quantifier of \( \varphi \) is on it; that is why the freshness conditions use "appear".

Three more examples:

- \( \bot \) and \( P(c) \) are sentences: they contain no variables at all. So is \( \forall x\, P(c) \). These are the degenerate cases.
- \( \forall x\, (x^2 \ge 1) \): the single occurrence of \( x \) lies below the node \( \forall x \), so it is bound. A sentence.
- \( \forall x\, \bigl( P(x) \to \exists y\, R(x, y) \bigr) \), the parse tree drawn above: both occurrences of \( x \) are bound by the root; the occurrence of \( y \) in \( R(x, y) \) is bound by \( \exists y \). A sentence.

**The recursive description.** In proofs about all formulas we need "\( x \) is free in \( \varphi \)" in the form that structural induction can use, one case per clause of @def-first-order-formula.

- \( x \) is free in an atomic formula exactly when \( x \) occurs in one of its terms; \( x \) is never free in \( \bot \).
- \( x \) is free in \( \neg\varphi \) exactly when \( x \) is free in \( \varphi \).
- \( x \) is free in \( (\varphi \circ \psi) \) exactly when \( x \) is free in \( \varphi \) or in \( \psi \).
- \( x \) is free in \( \forall y\, \varphi \), and in \( \exists y\, \varphi \), exactly when \( x \) is a different variable from \( y \) **and** \( x \) is free in \( \varphi \).

Each line is read off the tree. In an atomic formula there are no quantifier nodes, so every occurrence is free. The tree of \( \neg\varphi \) or \( (\varphi \circ \psi) \) adds a root that is not a quantifier node, so it binds nothing. The tree of \( \forall y\, \varphi \) adds the root \( \forall y \) on top of the tree of \( \varphi \): an occurrence of \( x \) inside \( \varphi \) keeps its path, with one more node at the top, so it is free in \( \forall y\, \varphi \) exactly when it was free in \( \varphi \) and the new node is not a quantifier on \( x \), that is, when \( x \) and \( y \) are different variables.
:::

::: {.second-reading title="The free variables of a limit statement"}
::: {#exm-free-and-bound-limit}
[The free variables of a limit statement]

With the conventions of Section 5.1 (domain \( \nR \), the sequence as a function symbol \( a \)), "the sequence \( (a_n) \) converges to \( L \)" is the formula
\[
\forall \varepsilon > 0 \; \exists N \in \nN \; \forall n \in \nN \;
\bigl( n \ge N \to \abs{a_n - L} < \varepsilon \bigr).
\]
Write it without bounded quantifiers, and find its free variables. Is it a sentence?
:::

::: {.solution}
Unfolding the three bounded quantifiers by @def-bounded-quantifier (\( \to \) under each \( \forall \), \( \wedge \) under the \( \exists \)) gives
\[
\begin{aligned}
& \forall \varepsilon \, \Bigl( \varepsilon > 0 \to \exists N \, \bigl( N \in \nN \wedge {} \\
& \qquad \forall n \, \bigl( n \in \nN \to ( n \ge N \to \abs{a_n - L} < \varepsilon ) \bigr) \bigr) \Bigr) .
\end{aligned}
\]
The variables that occur are \( \varepsilon \), \( N \), \( n \), and \( L \). Check each.

- Every occurrence of \( \varepsilon \) lies below the root \( \forall \varepsilon \): bound.
- Every occurrence of \( N \) lies below \( \exists N \): bound.
- Every occurrence of \( n \) (in \( n \in \nN \), in \( n \ge N \), and in the term \( a_n \)) lies below \( \forall n \): bound.
- The occurrence of \( L \) has no quantifier on \( L \) above it: free.

So \( L \) is the only free variable, and the formula is **not** a sentence. It is an open sentence in \( L \), as it should be: until \( L \) is given a value, "\( (a_n) \) converges to \( L \)" is neither true nor false, and which values make it true depends on the sequence (for \( a_n = 1/(n+1) \) the value \( L = 0 \) does and \( L = 1 \) does not; for \( a_n = (-1)^n \) no value does). Putting \( \exists L \) in front gives the sentence "\( (a_n) \) converges".

The other symbols in it are not variables, and "free" and "bound" do not apply to them. The letter \( a \) is a function symbol; the formula is certainly about the sequence \( a \), but \( a \) is fixed by the language, like \( + \), and cannot be quantified in this logic. The symbol \( \in \nN \) is a one-place predicate symbol, \( 0 \) is a constant, and \( > \), \( \ge \), \( < \), \( - \) and \( \abs{\cdot} \) are predicate and function symbols of the language.
:::
:::

::: {.warning}
The same letter can occur free and bound in one formula. In \( P(x) \wedge \forall x\, Q(x) \), the first \( x \) is a hole and the second is the quantifier's placeholder, and the two have nothing to do with each other. This is legal, and it is a trap for the reader: a proof that "uses \( x \)" from such a formula has to say which \( x \) it means. The book avoids it by renaming the bound variable (the last part of this section explains how): \( P(x) \wedge \forall z\, Q(z) \) says the same thing, and the question does not arise.
:::

::: {.check}
Is \( x \) free in \( \forall y\, (x < y) \to \exists x\, (x = 0) \)? At which occurrences?
:::

::: {.solution}
Yes. By shorthand rule 2 the formula is \( (\forall y\, (x < y) \to \exists x\, (x = 0)) \). The occurrence of \( x \) in \( x < y \) lies below \( \forall y \) only, which is a quantifier on \( y \), so it is **free**. The occurrence of \( x \) in \( x = 0 \) lies below \( \exists x \), so it is bound. One free occurrence is enough: \( x \) is a free variable of the formula. The variable \( y \), by contrast, is not free: its only occurrence lies below \( \forall y \).
:::

## Substitution, by example first

We now come to the operation that every quantifier rule uses. The rule of Section 5.3 will take the premise \( \forall x\, (P(x) \to S(x)) \) of Section 5.1's argument and produce \( P(2) \to S(2) \): it strips the quantifier and puts \( 2 \) in for \( x \). The rule of Section 5.5 goes the other way. Both need to say exactly what "put \( 2 \) in for \( x \)" does. The answer has one principle: only the **free** occurrences are replaced, because only they are holes. A bound occurrence belongs to its quantifier, and the quantifier is not asking for a value.

*\( \varphi[t/x] \) is \( \varphi \) with \( t \) put in for every free occurrence of \( x \), and nothing else changed.*

::: {#exm-computing-substitutions}
[Four substitutions]

Compute each substitution by the rule in the slogan above.

::: {.enumerate options="label=(\alph*)"}
1. \( \bigl( P(x) \to S(x) \bigr)[2/x] \).
2. \( \bigl( x < y \wedge \forall x\, (x \ge 0) \bigr)[(y + 1)/x] \).
3. \( \bigl( \forall y\, R(x, y) \bigr)[f(z)/x] \).
4. \( \bigl( \forall x\, P(x) \bigr)[c/x] \).
:::
:::

::: {.solution}
*(a)* The implication passes the substitution to both sides, and in each atomic formula the term \( x \) becomes \( 2 \): the result is \( P(2) \to S(2) \). This is the step that Section 5.3's rule makes in the argument of Section 5.1.

*(b)* The conjunction passes it to both parts. In \( x < y \) the \( x \) becomes \( y + 1 \), giving \( y + 1 < y \). In \( \forall x\, (x \ge 0) \) the quantifier is on \( x \), so the substitution stops. The result is
\[
y + 1 < y \ \wedge \ \forall x\, (x \ge 0) .
\]
Only the free occurrence of \( x \) changed. The bound one, in \( x \ge 0 \), was the quantifier's placeholder, and replacing it would have turned the sentence "every \( x \) is at least \( 0 \)" into a claim about \( y + 1 \).

*(c)* The quantifier is on \( y \), a variable different from \( x \), so it passes the substitution on: the result is \( \forall y\, R(f(z), y) \).

*(d)* The quantifier is on \( x \), so nothing changes: the result is \( \forall x\, P(x) \). There was no free \( x \) to replace.
:::

Here are the clauses those computations followed.

::: {#def-substitution}
[Substitution of a Term for a Variable]

Let \( t \) be a term and \( x \) a variable. For a term \( s \), the term \( s[t/x] \) is \( s \) with every occurrence of \( x \) replaced by \( t \); by recursion on terms,
\[
\begin{aligned}
x[t/x] &= t, \qquad y[t/x] = y \ \text{ for a variable } y \ne x, \qquad c[t/x] = c, \\
f(s_1, \dots, s_n)[t/x] &= f\bigl( s_1[t/x], \dots, s_n[t/x] \bigr).
\end{aligned}
\]
For a formula \( \varphi \), the formula \( \varphi[t/x] \), read "\( \varphi \) with \( t \) for \( x \)", is defined by recursion on \( \varphi \):
\[
\begin{aligned}
R(s_1, \dots, s_n)[t/x] &= R\bigl( s_1[t/x], \dots, s_n[t/x] \bigr), \\
(s_1 = s_2)[t/x] &= \bigl( s_1[t/x] = s_2[t/x] \bigr), \qquad \bot[t/x] = \bot, \\
(\neg\varphi)[t/x] &= \neg\bigl( \varphi[t/x] \bigr), \\
(\varphi \circ \psi)[t/x] &= \bigl( \varphi[t/x] \circ \psi[t/x] \bigr), \\
(\forall x\, \varphi)[t/x] &= \forall x\, \varphi, \\
(\forall y\, \varphi)[t/x] &= \forall y\, \bigl( \varphi[t/x] \bigr) \ \text{ for a variable } y \ne x,
\end{aligned}
\]
and the last two lines likewise with \( \exists \) in place of \( \forall \).
:::

A compound term is written in parentheses: \( \varphi[(y + 1)/x] \) puts \( y + 1 \) in for \( x \).

Two facts follow from the definition at once, and both are used again and again.

First, **\( \varphi[x/x] = \varphi \)**: putting \( x \) in for itself changes nothing. In each clause the replaced symbol is \( x \) again.

Second, and more useful: **if \( x \) is not free in \( \varphi \), then \( \varphi[t/x] = \varphi \)**, for every term \( t \). Example (d) was one instance. Later sections use it; its proof, a structural induction, is in the fold below.

::: {.second-reading title="The clauses in words, why the definition defines, and the claim proved"}
In words, clause by clause: in a term, every \( x \) is replaced, since a term has no quantifiers. In an atomic formula, the replacement happens inside its terms. The connectives pass the substitution to their parts. A quantifier on \( x \) **stops** it: below \( \forall x \) there is no free occurrence of \( x \) to replace. A quantifier on another variable \( y \) passes it on.

**Well defined.** The clauses give one value for each case of @def-first-order-formula, so structural recursion (carried over as above) says that they define exactly one formula \( \varphi[t/x] \) for each \( \varphi \). And the result is a formula: each clause builds its value by the clauses of @def-term and @def-first-order-formula from values already known to be terms and formulas.

This is a different operation from the substitution \( \sigma \) of Section 4.5 (the one in @lem-substitution). There, formulas were put in for **atoms**, at every occurrence. Here a **term** is put in for a **variable**, and bound occurrences are left alone.

::: {.claim}
Let \( x \) be a variable and \( t \) a term. For every formula \( \varphi \): if \( x \) is not free in \( \varphi \), then \( \varphi[t/x] = \varphi \).
:::

::: {.idea}
Substitution changes only free occurrences of \( x \), and there are none. Formally, structural induction on \( \varphi \), using the recursive description of "free" case by case. The only case with any content is a quantifier on a variable other than \( x \), where the substitution is passed on, and the induction hypothesis applies because \( x \) is still not free inside.
:::

::: {.proof}
For terms first: if \( x \) does not occur in a term \( s \), then \( s[t/x] = s \), by induction on \( s \) (a variable other than \( x \) and a constant are unchanged by the clauses, and \( f(s_1, \dots, s_n)[t/x] = f(s_1, \dots, s_n) \) when each \( s_i[t/x] = s_i \)). Now we prove the claim by structural induction on \( \varphi \).

*Atomic formulas and \( \bot \).* If \( x \) is not free in \( R(s_1, \dots, s_n) \), then \( x \) occurs in none of the \( s_i \) (the recursive description), so each \( s_i[t/x] = s_i \), and the clause for atomic formulas returns \( R(s_1, \dots, s_n) \). The same holds for \( s_1 = s_2 \), and \( \bot[t/x] = \bot \).

*Connectives.* If \( x \) is not free in \( \neg\varphi \), it is not free in \( \varphi \), so \( (\neg\varphi)[t/x] = \neg(\varphi[t/x]) = \neg\varphi \) by the induction hypothesis. If \( x \) is not free in \( (\varphi \circ \psi) \), it is free in neither part, and the same argument applies to both.

*Quantifiers.* Consider \( \forall y\, \varphi \). If \( y \) is \( x \), then \( (\forall x\, \varphi)[t/x] = \forall x\, \varphi \) by the definition, whatever \( \varphi \) is. If \( y \) is a different variable and \( x \) is not free in \( \forall y\, \varphi \), then \( x \) is not free in \( \varphi \) (the recursive description), so \( (\forall y\, \varphi)[t/x] = \forall y\, (\varphi[t/x]) = \forall y\, \varphi \) by the induction hypothesis. The case of \( \exists y\, \varphi \) is the same.

This proves the claim for every formula \( \varphi \).
:::
:::

**One substitution at a time.** \( \varphi[t/x] \) replaces one variable. Two substitutions in a row are made one after the other, and the second acts on the result of the first. So \( R(x, y)[y/x] \) is \( R(y, y) \), and then \( [x/y] \) turns it into \( R(x, x) \), not into the swapped \( R(y, x) \): the first step has already lost track of which \( y \) was which. To swap two variables, go through a letter that appears nowhere: \( [z/x] \), \( [x/y] \), \( [y/z] \) give \( R(z, y) \), \( R(z, x) \), \( R(y, x) \).

::: {.check}
Compute \( \bigl( (P(x) \wedge Q(y))[y/x] \bigr)[x/y] \). Which formula would swapping \( x \) and \( y \) give?
:::

::: {.solution}
The first step gives \( P(y) \wedge Q(y) \), and the second \( P(x) \wedge Q(x) \). The swap is \( P(y) \wedge Q(x) \), reached by \( [z/x] \), \( [x/y] \), \( [y/z] \) with a new letter \( z \).
:::

## Capture, and the practical rule

The definition of substitution never refuses. Given any \( \varphi \), \( t \) and \( x \), it returns a formula. Sometimes that formula does not say what we meant.

Take \( \varphi = \exists y\, (y \ne x) \), the example at the start of the section, and \( t = y \). The quantifier \( \exists y \) is on a variable different from \( x \), so the definition passes the substitution through, and
\[
\bigl( \exists y\, (y \ne x) \bigr)[y/x] = \exists y\, (y \ne y) .
\]
The definition was followed correctly. The meaning is wrong. The formula \( \exists y\, (y \ne x) \) says something about the number \( x \): some number differs from it, which over \( \nN \) is true whatever \( x \) is. We wanted to say the same thing about the number \( y \), and we got "some number differs from itself", which is false. The \( y \) we put in was supposed to name a number from outside, and it landed in the scope of \( \exists y \) and was **captured**.

Compare a substitution that is safe. Over \( \nR \), \( \forall z\, (x < z) \) says that \( x \) is smaller than every number (false, as it happens, for every \( x \); but what matters is what it says). Put \( y + 1 \) in for \( x \): the quantifier \( \forall z \) passes the substitution on, and
\[
\bigl( \forall z\, (x < z) \bigr)[(y + 1)/x] = \forall z\, (y + 1 < z),
\]
which says exactly that \( y + 1 \) is smaller than every number. Nothing was captured, because the term \( y + 1 \) does not contain \( z \), the only variable quantified above the occurrence of \( x \).

The difference between the safe case and the unsafe one is exactly this: whether a variable of \( t \) is quantified somewhere above a free occurrence of \( x \).

*A term is free for \( x \) when putting it in for \( x \) lets none of its variables be captured.*

::: {#def-free-for}
[Free For]

Let \( t \) be a term, \( x \) a variable, and \( \varphi \) a formula. The term \( t \) is **free for** \( x \) in \( \varphi \) if **no** free occurrence of \( x \) in \( \varphi \) lies in the scope of a quantifier \( \forall y \) or \( \exists y \) such that \( y \) is a variable of \( t \).
:::

In words: look at each place where \( t \) will go, that is, at each free occurrence of \( x \). Look at the quantifiers above it in the tree. If none of them is on a variable of \( t \), the substitution is safe there. The term is free for \( x \) when it is safe at every such place. Informally: **no variable of \( t \) becomes bound** when \( t \) is put in.

Four special cases, each immediate from the definition, cover most uses.

- A term with **no variables** (\( 2 \), \( c \), \( f(c) \)) is free for every variable in every formula: there is no \( y \) to capture.
- The variable \( x \) is free for \( x \) in every formula. A free occurrence of \( x \) never lies in the scope of a quantifier on \( x \); if it did, it would be bound.
- A variable \( z \) that does **not appear** in \( \varphi \) is free for every variable in \( \varphi \): no quantifier of \( \varphi \) is on \( z \).
- If \( x \) is **not free** in \( \varphi \), every term is free for \( x \) in \( \varphi \): there are no free occurrences to check. (And then \( \varphi[t/x] = \varphi \) by the claim above.)

In our examples: \( y \) is **not** free for \( x \) in \( \exists y\, (y \ne x) \), because the free occurrence of \( x \) lies in the scope of \( \exists y \) and \( y \) is a variable of the term \( y \). Likewise \( y + 1 \) is not free for \( x \) in \( \exists y\, (y > x) \). And \( y + 1 \) **is** free for \( x \) in \( \forall z\, (x < z) \): the only quantifier above the free occurrence of \( x \) is on \( z \), which is not a variable of \( y + 1 \).

"Free for" is the precise condition under which \( \varphi[t/x] \) says about \( t \) what \( \varphi \) says about \( x \). The rules \( \forall\text{E} \) (Section 5.3), \( \exists\text{I} \) (Section 5.5) and \( =\text{E} \) (Section 5.7) carry it as a side condition.

::: {.second-reading title="A second capture, the recursive description of 'free for', and why it asks no more than it needs"}
Here is a second example, with a compound term. Over \( \nR \), \( \exists y\, (y > x) \) is true for every \( x \): there is a number larger than \( x \). Put \( y + 1 \) in for \( x \):
\[
\bigl( \exists y\, (y > x) \bigr)[(y + 1)/x] = \exists y\, (y > y + 1) .
\]
The result says that some number is larger than its own successor, which is false. It should have said that some number is larger than \( y + 1 \), which is true.

**The recursive description.** For induction proofs, "free for" can be read off case by case, like "free":

- \( t \) is free for \( x \) in every atomic formula and in \( \bot \);
- \( t \) is free for \( x \) in \( \neg\varphi \) exactly when it is free for \( x \) in \( \varphi \), and in \( (\varphi \circ \psi) \) exactly when it is free for \( x \) in both \( \varphi \) and \( \psi \);
- \( t \) is free for \( x \) in \( \forall y\, \varphi \) (and in \( \exists y\, \varphi \)) exactly when **either** \( x \) is not free in \( \forall y\, \varphi \), **or** \( y \) is not a variable of \( t \) and \( t \) is free for \( x \) in \( \varphi \).

The first two lines hold because an atomic formula has no quantifiers and a connective node is not a quantifier. For the third: if \( x \) is not free in \( \forall y\, \varphi \), there is nothing to check. If it is free, then \( y \) is a different variable and the free occurrences of \( x \) in \( \forall y\, \varphi \) are those in \( \varphi \); each lies in the scope of the new root \( \forall y \) and of the quantifiers inside \( \varphi \) above it. The root is harmless exactly when \( y \) is not a variable of \( t \), and the quantifiers inside are harmless exactly when \( t \) is free for \( x \) in \( \varphi \).

Section 5.3 shows the capture example of this section turning a true premise into a false conclusion when the side condition is ignored. The definition asks for no more than it needs: a variable of \( t \) may be quantified elsewhere in \( \varphi \), as long as no free occurrence of \( x \) lies in its scope. For instance, \( y \) is free for \( x \) in \( P(x) \wedge \exists y\, Q(y) \), and the result \( P(y) \wedge \exists y\, Q(y) \) says of \( y \) what the original said of \( x \).
:::

**Before you substitute.** Look at each free occurrence of \( x \) and at the quantifiers above it. If none of them is on a letter of \( t \), go ahead. If one is, rename that quantifier's letter to a brand-new letter first (next subsection), and then substitute. Nothing else can go wrong.

::: {.check}
Is \( y \) free for \( x \) in \( \exists y\, (x < y) \wedge P(y) \)? Is \( x + 1 \)?
:::

::: {.solution}
By shorthand rule 2 the formula is \( (\exists y\, (x < y) \wedge P(y)) \). The term \( y \) is not free for \( x \): the free \( x \) of \( x < y \) lies under \( \exists y \), and \( y \) is a letter of the term. Rename first, \( \exists z\, (x < z) \wedge P(y) \), and then substitute to get \( \exists z\, (y < z) \wedge P(y) \). The term \( x + 1 \) is free for \( x \): the only quantifier above the free \( x \) is on \( y \), which is not a letter of \( x + 1 \).
:::

::: {.warning}
Capture changes meaning, and it gives no warning: the definition of \( \varphi[t/x] \) returns a formula either way. Over \( \nR \), \( \exists y\, (y > x) \) is true for every \( x \), and \( (\exists y\, (y > x))[(y + 1)/x] \) is \( \exists y\, (y > y + 1) \), which is false. Before putting \( t \) in for \( x \), check that no variable of \( t \) is quantified above a free occurrence of \( x \).
:::

::: {.check}
Is \( y + 1 \) free for \( x \) in \( \forall z\, (x < z) \)? Is it free for \( x \) in \( \forall y\, (x < y) \)? Compute both substitutions and say what each result claims.
:::

::: {.solution}
In \( \forall z\, (x < z) \): yes. The only quantifier above the occurrence of \( x \) is on \( z \), and \( z \) is not a variable of \( y + 1 \). The result is \( \forall z\, (y + 1 < z) \), "\( y + 1 \) is smaller than every number", which is what the original said about \( x \).

In \( \forall y\, (x < y) \): no. The occurrence of \( x \) lies in the scope of \( \forall y \), and \( y \) is a variable of \( y + 1 \). The definition gives \( \forall y\, (y + 1 < y) \): "every number is larger than its own successor". That is a sentence about no particular number at all, and a false one; the original said something about \( x \), and the result should have said the same about \( y + 1 \). The \( y \) of \( y + 1 \) was captured.
:::

## Renaming bound variables

What should we do when \( t \) is not free for \( x \) in \( \varphi \)? A bound variable is a placeholder, and the name of a placeholder does not matter. "Some number differs from \( x \)" can be written \( \exists y\, (y \ne x) \) or \( \exists z\, (z \ne x) \), just as \( \int_0^1 s^2 \, ds \) and \( \int_0^1 u^2 \, du \) are the same integral. So the way out is: **rename the bound variable first, then substitute.**

**Renaming.** Let \( \varphi \) be a formula and \( y, z \) variables, with \( z \) **not appearing** in \( \varphi \). The formula \( \forall z\, \varphi[z/y] \) is obtained from \( \forall y\, \varphi \) by **renaming** the bound variable \( y \) to \( z \); likewise \( \exists z\, \varphi[z/y] \) from \( \exists y\, \varphi \). The same may be done to a quantifier anywhere inside a larger formula.

In words: change the variable after the quantifier, and change the occurrences it binds, to a letter that appears nowhere in the formula. The condition that \( z \) does not appear in \( \varphi \) does two jobs. It makes \( z \) free for \( y \) in \( \varphi \) (the third special case above), so no new \( z \) is captured by a quantifier inside \( \varphi \). And it ensures that no free \( z \) already in \( \varphi \) is captured by the new quantifier \( \forall z \). Without it, renaming can change the meaning: \( \forall y\, (y \ge z) \) says something about \( z \) (over \( \nN \), that \( z = 0 \)), and "renaming" \( y \) to \( z \) would give \( \forall z\, (z \ge z) \), a sentence that is simply true.

Renaming a bound letter is treated as never changing what a formula says; Sections 5.4 and 5.6 derive it at the front of a formula, and the fold says where the rest stands.

::: {.second-reading title="The status of renaming"}
**Its status.** Renaming is not a rule of the calculus, and we have not proved that it keeps meaning. Here is where it stands. For a renaming at the front of a formula, \( \forall y\, \varphi \) and \( \forall z\, \varphi[z/y] \) can each be derived from the other in three lines, once the rules of Section 5.4 are available; that section does it, and Section 5.6 does the same for \( \exists \). A renaming **inside** a larger formula we take as a convention of this book: formulas that differ only by renaming bound variables are treated as saying the same thing. Its justification in terms of meaning is the one the Looking-ahead box at the end of this section points to.
:::

**The recipe.** To put \( t \) in for \( x \) in \( \varphi \) when \( t \) is not free for \( x \): rename each quantifier of \( \varphi \) that is on a variable of \( t \) and has a free occurrence of \( x \) in its scope, each to a different variable that appears neither in \( \varphi \) nor in \( t \) (each such step is a renaming in the sense above); then substitute. After the renaming, \( t \) is free for \( x \).

- \( \exists y\, (y \ne x) \) with \( y \) for \( x \): rename \( y \) to \( z \), giving \( \exists z\, (z \ne x) \); then substitute, giving \( \exists z\, (z \ne y) \), "some number differs from \( y \)". True over \( \nN \) for every \( y \), as intended.
- \( \exists y\, (y > x) \) with \( y + 1 \) for \( x \): rename to \( \exists z\, (z > x) \); substitute, giving \( \exists z\, (z > y + 1) \). True over \( \nR \), as intended.

Which fresh letter we choose does not matter: two choices give formulas that differ only by a renaming. From now on, whenever a rule writes \( \varphi[t/x] \), it will require \( t \) to be free for \( x \) in \( \varphi \), and if we want a \( t \) that is not, we rename first.

## How substitution looks in a mathematical proof

Mathematicians substitute constantly and never write \( [t/x] \). Two examples show the operation, and its trap, in their natural habitat.

**"Apply the hypothesis with \( \varepsilon/2 \) in place of \( \varepsilon \)."** Suppose we know that \( (a_n) \) converges to \( L \), and we have fixed an \( \varepsilon > 0 \) for some other purpose. A proof says: "applying the hypothesis with \( \varepsilon/2 \), there is an \( N \in \nN \) with \( \abs{a_n - L} < \varepsilon/2 \) for all \( n \ge N \)". The hypothesis is \( \forall \varepsilon\, \varphi \), with
\[
\varphi \ = \ \Bigl( \varepsilon > 0 \to \exists N \in \nN \; \forall n \in \nN \;
\bigl( n \ge N \to \abs{a_n - L} < \varepsilon \bigr) \Bigr),
\]
and the proof uses the instance \( \varphi[t/\varepsilon] \) with the term \( t = \varepsilon/2 \):
\[
\varepsilon/2 > 0 \to \exists N \in \nN \; \forall n \in \nN \;
\bigl( n \ge N \to \abs{a_n - L} < \varepsilon/2 \bigr).
\]
The term \( \varepsilon/2 \) contains the variable \( \varepsilon \): the fixed \( \varepsilon \) of the proof, not the bound one of the hypothesis. It is free for \( \varepsilon \) in \( \varphi \), because the only quantifiers above the free occurrences of \( \varepsilon \) in \( \varphi \) are on \( N \) and \( n \). Section 5.3's rule makes this step, and "\( \varepsilon/2 > 0 \)" then comes from \( \varepsilon > 0 \) by arithmetic.

**"Take \( N = n \)."** Now suppose the proof has chosen \( N \), so it knows
\[
\psi \ = \ \forall n \in \nN \; \bigl( n \ge N \to \abs{a_n - L} < \varepsilon \bigr),
\]
with \( N \) free. A tempting step is to "apply this with \( n \) in place of \( N \)". No rule allows this: \( N \) has been chosen, not quantified, so no term may be put in for it. Writing the step out shows how badly it goes wrong, because \( n \) is not even free for \( N \) in \( \psi \): the occurrence of \( N \) lies in the scope of \( \forall n \). The substitution produces
\[
\forall n \in \nN \; \bigl( n \ge n \to \abs{a_n - L} < \varepsilon \bigr),
\]
which says that **every** term of the sequence is within \( \varepsilon \) of \( L \), a far stronger claim that does not follow. In words, the error is to let the threshold \( N \) be "the \( n \) we are looking at", when \( n \) is the placeholder of "for all \( n \ge N \)". A proof that needs a statement about a particular index names it with a new letter, say \( m \ge N \), and substitutes \( m \), which is free for \( n \).

::: {.second-reading title="Induction, as a formula"}
**Induction, as a formula.** The display after @ax-induction in Section 4.2 used a property \( P(n) \). With substitution it can be written for any formula \( \varphi \) in which the variable \( n \) is free, as the formula
\[
\Bigl( \varphi[0/n] \ \wedge \ \forall n \in \nN \, \bigl( \varphi \to \varphi[(n + 1)/n] \bigr) \Bigr)
\ \to \ \forall n \in \nN \; \varphi ,
\]
where \( \varphi[0/n] \) plays the part of \( P(0) \) and \( \varphi[(n + 1)/n] \) the part of \( P(n + 1) \). The term \( n + 1 \) is free for \( n \) in \( \varphi \): its only variable is \( n \), and a free occurrence of \( n \) never lies in the scope of a quantifier on \( n \). This is how the principle of induction reads in the language of this chapter; its status (a basic property of \( \nN \)) is unchanged.
:::

::: {.second-reading title="Partial terms"}
Mathematics writes \( 1/x \) and \( \lim a_n \), which name nothing for some values: \( x = 0 \), or a sequence with no limit. In the language of this chapter every term names an object, because every function symbol is defined everywhere on the domain. Mathematics keeps partial operations out of trouble with hypotheses: \( 1/x \) is written only under \( x \ne 0 \), as in \( \forall x\, (x \ne 0 \to x \cdot (1/x) = 1) \), where the value at \( 0 \) is never used; and "the limit" is written only after it has been proved that there is exactly one (Section 5.8). Some logics allow terms that name nothing; this book does not need them.
:::

::: {.remark}
[Looking ahead]

Chapter 7 proves, in an optional section, that renaming a bound letter never changes the meaning of a formula.
:::

## Exercises

### A. Check your understanding

::: {#exr-terms-formulas-substitution-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. For each formula, mark each occurrence of each variable as free or bound, list the free variables, and say whether it is a sentence: (i) \( \forall x\, (P(x) \to Q(y)) \); (ii) \( \exists x\, \forall y\, R(x, y) \); (iii) \( \forall x\, (x < y) \wedge \exists y\, (y < x) \); (iv) \( \forall \varepsilon\, \bigl( \varepsilon > 0 \to \exists \delta\, (\delta > 0 \wedge \delta < \varepsilon) \bigr) \).
2. Which of the following are terms, and which are formulas, for one-place \( f \), two-place \( g \) and two-place predicate \( R \)? (i) \( g(f(x), c) \); (ii) \( R(f(x), c) \); (iii) \( f(R(x, c)) \); (iv) \( \forall c\, R(c, c) \).
3. True or false, with a reason: if \( t \) is a variable, then \( t \) is free for \( x \) in every formula.
4. True or false, with a reason: \( \bigl( \forall x\, P(x) \wedge Q(x) \bigr)[c/x] \) is \( \forall x\, P(x) \wedge Q(c) \).
:::
:::

::: {.solution}
*(a)* (i) The single occurrence of \( x \), in \( P(x) \), is bound by \( \forall x \) (the \( x \) after \( \forall \) belongs to the quantifier node and is not an occurrence); the occurrence of \( y \) in \( Q(y) \) is free (no quantifier on \( y \)). Free variables: \( y \). Not a sentence.

(ii) The occurrence of \( x \) is bound by \( \exists x \), that of \( y \) by \( \forall y \). No free variables: a sentence.

(iii) By shorthand rule 2 this is \( (\forall x\, (x < y) \wedge \exists y\, (y < x)) \). In the left part, \( x \) is bound by \( \forall x \) and \( y \) is free. In the right part, \( y \) is bound by \( \exists y \) and \( x \) is free (the \( \forall x \) governs only the left part). Free variables: \( x \) and \( y \), each with one free and one bound occurrence. Not a sentence.

(iv) Every occurrence of \( \varepsilon \) lies below \( \forall \varepsilon \), and both occurrences of \( \delta \) lie below \( \exists \delta \); \( 0 \) is a constant. A sentence.

*(b)* (i) A term, by (Tm2) twice. (ii) A formula, atomic by (Fm1): the predicate \( R \) applied to the terms \( f(x) \) and \( c \). (iii) Neither: \( R(x, c) \) is a formula, not a term, and (Tm2) applies \( f \) only to a term. (iv) Neither: (Fm4) puts a **variable** after \( \forall \), and \( c \) is a constant symbol.

*(c)* False. The variable \( y \) is not free for \( x \) in \( \exists y\, (y \ne x) \), since the free occurrence of \( x \) lies in the scope of \( \exists y \). (A variable \( t \) **is** free for \( x \) when \( t \) is \( x \) itself, or when \( t \) does not appear in the formula.)

*(d)* True. The formula is \( (\forall x\, P(x) \wedge Q(x)) \) by shorthand rule 2. The \( \wedge \) passes the substitution to both parts; \( \forall x\, P(x) \) is unchanged because its quantifier is on \( x \), and \( Q(x) \) becomes \( Q(c) \).
:::

::: {#exr-terms-formulas-substitution-a2}
[A2: Drill]

Answer each part in a line or two.

::: {.enumerate options="label=(\alph*)"}
1. In \( \forall y\, (x < y) \wedge \exists x\, (x = y) \), which occurrences are free, and what are the free variables?
2. Is \( \forall x\, \exists y\, (x + y = 0) \) a sentence?
3. Someone writes \( \forall x\, P(x) \to Q(x) \) for "every \( P \) is a \( Q \)". Which occurrence of \( x \) is free, and what is the repair?
4. Repair \( \forall \varepsilon > 0\; \exists \delta > 0\; (\abs{x - a} < \delta \to \abs{f(x) - f(a)} < \varepsilon) \), meant as "\( f \) is continuous at \( a \)", with \( a \) a variable here (not a constant symbol), so that \( a \) is its only free variable.
5. Compute \( \bigl( x \le y \wedge \exists y\, (y < x) \bigr)[3/x] \).
6. Compute \( \bigl( \forall x\, (x \ge y) \bigr)[0/y] \).
7. Compute \( \bigl( \forall x\, P(x) \to P(x) \bigr)[c/x] \).
8. Compute \( \bigl( (x + y = y + x)[y/x] \bigr)[x/y] \). Is the result the formula with \( x \) and \( y \) swapped?
9. Compute \( \bigl( P(x, y)[f(y)/x] \bigr)[c/y] \).
10. Is \( x \) free for \( y \) in \( \exists x\, (x > y) \)?
11. Is \( z + 1 \) free for \( y \) in \( \exists x\, (x > y) \)? Compute.
12. Put \( x \) in for \( y \) in \( \exists x\, (x > y) \), renaming first.
:::
:::

::: {.solution}
(a) The \( x \) of \( x < y \) and the \( y \) of \( x = y \) are free; the \( y \) of \( x < y \) is bound by \( \forall y \) and the \( x \) of \( x = y \) by \( \exists x \). Free variables: \( x \), \( y \).

(b) Yes: every occurrence is bound.

(c) By shorthand rule 2 the \( \forall x \) governs only \( P(x) \), so the formula is \( (\forall x\, P(x)) \to Q(x) \) and the \( x \) of \( Q(x) \) is free. Repair: \( \forall x\, (P(x) \to Q(x)) \).

(d) As written, \( x \) is free, so the formula speaks of one fixed \( x \). Repair: \( \forall \varepsilon > 0\; \exists \delta > 0\; \forall x\, (\abs{x - a} < \delta \to \abs{f(x) - f(a)} < \varepsilon) \); \( f \) is a function symbol, not a variable.

(e) \( 3 \le y \wedge \exists y\, (y < 3) \).

(f) \( \forall x\, (x \ge 0) \).

(g) \( \forall x\, P(x) \to P(c) \) (shorthand rule 2: the \( \forall x \) governs only the first \( P(x) \)).

(h) \( y + y = y + y \), then \( x + x = x + x \). No: the swap is \( y + x = x + y \).

(i) \( P(f(y), y) \), then \( P(f(c), c) \): the second substitution also reaches the \( y \) inside the term put in by the first.

(j) No: the free \( y \) lies in the scope of \( \exists x \), and \( x \) is the variable of the term.

(k) Yes: \( \exists x\, (x > z + 1) \).

(l) Rename \( x \) to \( z \): \( \exists z\, (z > y) \); then \( \exists z\, (z > x) \).
:::

### B. Practice

::: {#exr-terms-formulas-substitution-b1}
[B1: Computing substitutions]

Compute each substitution. Where the term is not free for the variable, say which quantifier would capture it, rename first, and then substitute.

::: {.enumerate options="label=(\alph*)"}
1. \( \bigl( P(x) \wedge R(x, y) \bigr)[f(y)/x] \).
2. \( \bigl( \forall x\, R(x, y) \to P(x) \bigr)[c/x] \).
3. \( \bigl( \forall y\, (x < y) \bigr)[(y + 1)/x] \).
4. \( \bigl( \exists x\, (x = 2 \cdot y) \bigr)[x/y] \).
5. \( \bigl( \exists y\, (y > x) \wedge Q(y) \bigr)[(x + 1)/y] \).
:::
:::

::: {.solution}
*(a)* No quantifiers, so \( f(y) \) is free for \( x \). Every occurrence of \( x \) is replaced: \( P(f(y)) \wedge R(f(y), y) \). The \( y \) inside \( f(y) \) and the \( y \) already in \( R(x, y) \) now stand side by side; with no quantifier around, both are the same free \( y \), as intended.

*(b)* By shorthand rule 2 the formula is \( (\forall x\, R(x, y) \to P(x)) \). The constant \( c \) has no variables, so it is free for \( x \). The left part is unchanged (quantifier on \( x \)); the free \( x \) in \( P(x) \) becomes \( c \): \( \forall x\, R(x, y) \to P(c) \).

*(c)* Not free for: the free occurrence of \( x \) lies in the scope of \( \forall y \), and \( y \) is a variable of \( y + 1 \). Rename \( y \) to \( z \), which appears nowhere: \( \forall z\, (x < z) \). Then substitute: \( \forall z\, (y + 1 < z) \). (Without renaming, the definition would give \( \forall y\, (y + 1 < y) \), which says nothing about \( y + 1 \).)

*(d)* Not free for: the free occurrence of \( y \) lies in the scope of \( \exists x \), and the term is \( x \). Rename \( x \) to \( z \): \( \exists z\, (z = 2 \cdot y) \), "\( y \) doubled is something", then substitute: \( \exists z\, (z = 2 \cdot x) \). (Without renaming, the result would be \( \exists x\, (x = 2 \cdot x) \), "some number is its own double", a claim about no particular number.)

*(e)* By shorthand rule 2 the formula is \( (\exists y\, (y > x) \wedge Q(y)) \). The occurrence of \( y \) in \( y > x \) is bound, and the one in \( Q(y) \) is free and not in the scope of any quantifier; so \( x + 1 \) is free for \( y \) (the \( \exists y \) above the bound \( y \) is irrelevant, since that occurrence is not replaced). The result is \( \exists y\, (y > x) \wedge Q(x + 1) \).
:::

::: {#exr-terms-formulas-substitution-b2}
[B2: The set of free variables]

For a term \( t \), let \( \mathrm{Var}(t) \) be the set of variables of \( t \), and for a formula \( \varphi \), let \( \mathrm{FV}(\varphi) \) be the set of its free variables. (Here \( \cup \) is the union of two sets, \( \setminus \) removes elements, and \( \emptyset \) is the empty set, all in the everyday sense.)

::: {.enumerate options="label=(\alph*)"}
1. Write down clauses that define \( \mathrm{Var}(t) \) by recursion on terms and \( \mathrm{FV}(\varphi) \) by recursion on formulas, one clause for each case of @def-term and of @def-first-order-formula.
2. Use your clauses to compute \( \mathrm{FV} \) of \( \forall x\, (x < y) \wedge \exists y\, (y < x) \) and of \( \forall x\, \exists y\, (x + y = z) \), showing each step.
:::
:::

::: {.solution}
*(a)* For terms:
\[
\begin{aligned}
\mathrm{Var}(x) &= \{x\} \ \text{ for a variable } x, \qquad \mathrm{Var}(c) = \emptyset, \\
\mathrm{Var}\bigl( f(t_1, \dots, t_n) \bigr) &= \mathrm{Var}(t_1) \cup \dots \cup \mathrm{Var}(t_n).
\end{aligned}
\]
For formulas:
\[
\begin{aligned}
\mathrm{FV}\bigl( R(t_1, \dots, t_n) \bigr) &= \mathrm{Var}(t_1) \cup \dots \cup \mathrm{Var}(t_n), \\
\mathrm{FV}(t_1 = t_2) &= \mathrm{Var}(t_1) \cup \mathrm{Var}(t_2), \qquad \mathrm{FV}(\bot) = \emptyset, \\
\mathrm{FV}(\neg\varphi) &= \mathrm{FV}(\varphi), \qquad
\mathrm{FV}\bigl( (\varphi \circ \psi) \bigr) = \mathrm{FV}(\varphi) \cup \mathrm{FV}(\psi), \\
\mathrm{FV}(\forall x\, \varphi) &= \mathrm{FV}(\exists x\, \varphi) = \mathrm{FV}(\varphi) \setminus \{x\}.
\end{aligned}
\]
These are the four lines of the recursive description of "free" (in the fold after the examples of free and bound occurrences), rewritten as sets: \( x \in \mathrm{FV}(\varphi) \) exactly when \( x \) is free in \( \varphi \). By structural recursion (carried over to terms and to first-order formulas), each set of clauses defines exactly one function.

*(b)* First formula. \( \mathrm{FV}(x < y) = \{x, y\} \), so \( \mathrm{FV}(\forall x\, (x < y)) = \{x, y\} \setminus \{x\} = \{y\} \). \( \mathrm{FV}(y < x) = \{x, y\} \), so \( \mathrm{FV}(\exists y\, (y < x)) = \{x\} \). The conjunction gives \( \{y\} \cup \{x\} = \{x, y\} \), which agrees with A1(a)(iii).

Second formula. \( \mathrm{FV}(x + y = z) = \mathrm{Var}(x + y) \cup \mathrm{Var}(z) = \{x, y, z\} \). Then \( \mathrm{FV}(\exists y\, (x + y = z)) = \{x, z\} \), and \( \mathrm{FV}(\forall x\, \exists y\, (x + y = z)) = \{z\} \). So the formula is an open sentence in \( z \) alone (over \( \nR \) it is true for every \( z \): given \( x \), take \( y = z - x \)).
:::

::: {#exr-terms-formulas-substitution-b3}
[B3: Swapping two letters]

Let \( \varphi = \exists z\, \bigl( R(x, z) \wedge R(z, y) \bigr) \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( (\varphi[y/x])[x/y] \), and say whether it is \( \varphi \) with \( x \) and \( y \) swapped.
2. Swap \( x \) and \( y \) in \( \varphi \) with three substitutions through a letter \( u \) that appears nowhere, checking at each step that the term is free for the variable.
3. Why would \( z \) not do as the go-between?
:::
:::

::: {.solution}
*(a)* \( \varphi[y/x] = \exists z\, (R(y, z) \wedge R(z, y)) \), and then \( [x/y] \) gives \( \exists z\, (R(x, z) \wedge R(z, x)) \). The swap is \( \exists z\, (R(y, z) \wedge R(z, x)) \), a different formula, and it says something different: over \( \nN \) with \( R \) read as \( < \) and \( x, y \) naming \( 2, 0 \), the swap is true (\( z = 1 \)), while the computed formula, "some \( z \) is above \( 2 \) and below \( 2 \)", is false.

*(b)* \( \varphi[u/x] = \exists z\, (R(u, z) \wedge R(z, y)) \); then \( [x/y] \) gives \( \exists z\, (R(u, z) \wedge R(z, x)) \); then \( [y/u] \) gives \( \exists z\, (R(y, z) \wedge R(z, x)) \), the swap. At each step the only quantifier above the replaced occurrence is \( \exists z \), and the term (\( u \), \( x \), \( y \)) is not \( z \), so it is free.

*(c)* \( z \) is not free for \( x \) in \( \varphi \): the \( x \) of \( R(x, z) \) lies inside \( \exists z \), so \( \varphi[z/x] \) would be captured and say \( \exists z\, (R(z, z) \wedge R(z, y)) \). The go-between must appear nowhere in \( \varphi \), bound letters included ("appear", in "Free and bound: drawing the arrows").

Worked examples of these types: "One substitution at a time"; the practical rule "Before you substitute".

**Marking scheme.** (10 points)

- 3: (a), both steps computed and the swap written, with the difference shown (by the strings, or by one reading in which they differ).
- 4: (b), the three substitutions in the right order, each result correct, and the free-for check stated once for each step.
- 3: (c), capture named, with the captured formula written.

Fatal error (0 for the part): treating \( [y/x] \) and \( [x/y] \) as happening at the same time.
:::

### C. Going deeper

::: {#exr-terms-formulas-substitution-c1}
[C1: Challenge: What substitution does to the free variables]

Let \( \varphi \) be a formula, \( x \) a variable and \( t \) a term, with \( t \) free for \( x \) in \( \varphi \), and with \( x \) free in \( \varphi \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that the free variables of \( \varphi[t/x] \) are the free variables of \( \varphi \) other than \( x \), together with the variables of \( t \):
\[
\mathrm{FV}(\varphi[t/x]) = \bigl( \mathrm{FV}(\varphi) \setminus \{x\} \bigr) \cup \mathrm{Var}(t),
\]
with the notation of B2. Prove it in the following form, by structural induction on \( \varphi \): for every \( \varphi \) in which \( t \) is free for \( x \), *if \( x \in \mathrm{FV}(\varphi) \), then \( \mathrm{FV}(\varphi[t/x]) = (\mathrm{FV}(\varphi) \setminus \{x\}) \cup \mathrm{Var}(t) \); if \( x \notin \mathrm{FV}(\varphi) \), then \( \varphi[t/x] = \varphi \).* The term version, the atomic case and the connective cases are done below; prove the case of \( \forall y\, \varphi \) (the case of \( \exists y\, \varphi \) is the same).
2. Show, with the capture example \( \exists y\, (y > x) \), \( t = y + 1 \), that the conclusion can fail when \( t \) is not free for \( x \). Show also, with an example of your own, that it can fail when \( x \) is not free in \( \varphi \).
:::

**Given for (a).** *Terms.* Let \( s \) be a term in which \( x \) occurs. Then \( \mathrm{Var}(s[t/x]) = (\mathrm{Var}(s) \setminus \{x\}) \cup \mathrm{Var}(t) \). By induction on \( s \): if \( s \) is the variable \( x \), then \( s[t/x] = t \) and both sides are \( \mathrm{Var}(t) \). (A constant, or a variable other than \( x \), does not contain \( x \).) If \( s = f(s_1, \dots, s_n) \), then \( s[t/x] = f(s_1[t/x], \dots, s_n[t/x]) \); for each \( s_i \) containing \( x \), the induction hypothesis gives \( \mathrm{Var}(s_i[t/x]) = (\mathrm{Var}(s_i) \setminus \{x\}) \cup \mathrm{Var}(t) \), and for each \( s_i \) not containing \( x \), \( s_i[t/x] = s_i \) (as in the proof of the claim in the text). At least one \( s_i \) contains \( x \), so the union over \( i \) is \( (\mathrm{Var}(s) \setminus \{x\}) \cup \mathrm{Var}(t) \).

*Formulas.* We prove, by structural induction on \( \varphi \), the statement \( S(\varphi) \): *if \( t \) is free for \( x \) in \( \varphi \), then \( \mathrm{FV}(\varphi[t/x]) = (\mathrm{FV}(\varphi) \setminus \{x\}) \cup \mathrm{Var}(t) \) when \( x \in \mathrm{FV}(\varphi) \), and \( \varphi[t/x] = \varphi \) when \( x \notin \mathrm{FV}(\varphi) \).* The second half is the claim proved in the text, for every \( \varphi \); so in each case below we assume \( x \in \mathrm{FV}(\varphi) \) and prove the equation. Write \( E(\chi) \) for the set \( (\mathrm{FV}(\chi) \setminus \{x\}) \cup \mathrm{Var}(t) \).

*Atomic.* Let \( \varphi = R(s_1, \dots, s_n) \) with \( x \) occurring in some \( s_i \). By the clause for atomic formulas, \( \mathrm{FV}(\varphi[t/x]) \) is the union over \( i \) of the sets \( \mathrm{Var}(s_i[t/x]) \). Exactly as in the term case for \( f(s_1, \dots, s_n) \) (the result for terms for each \( s_i \) containing \( x \), \( s_i[t/x] = s_i \) for the others, and at least one \( s_i \) containing \( x \)), this union is \( E(\varphi) \). The same for \( s_1 = s_2 \). (\( \bot \) has no free variables.)

*Negation.* \( \mathrm{FV}((\neg\varphi)[t/x]) = \mathrm{FV}(\varphi[t/x]) = E(\varphi) = E(\neg\varphi) \), by the induction hypothesis (\( t \) is free for \( x \) in \( \varphi \), and \( x \) is free in \( \varphi \)).

*Binary connective.* Let \( x \) be free in \( (\varphi \circ \psi) \); then \( t \) is free for \( x \) in both parts, and \( x \) is free in at least one. If it is free in both, the induction hypothesis gives \( E(\varphi) \cup E(\psi) = E((\varphi \circ \psi)) \). If it is free in \( \varphi \) only, then \( \psi[t/x] = \psi \), and \( E(\varphi) \cup \mathrm{FV}(\psi) = E((\varphi \circ \psi)) \), because \( x \notin \mathrm{FV}(\psi) \). Symmetrically if it is free in \( \psi \) only.
:::

::: {.solution}
[Hint 1]

When \( x \) is free in \( \forall y\, \varphi \), what does "free for" tell you about \( y \) and \( t \)?
:::

::: {.solution}
[Hint 2]

Start from \( \mathrm{FV}((\forall y\, \varphi)[t/x]) = \mathrm{FV}(\varphi[t/x]) \setminus \{y\} \) and apply the induction hypothesis to \( \varphi \). Then see where removing \( y \) from the resulting set needs something about \( y \) and \( \mathrm{Var}(t) \).
:::

::: {.solution}
*(a)* The term version and the atomic, negation and connective cases are given in the statement. It remains to treat the quantifiers.

*Quantifier.* If \( x \) is not free in \( \forall y\, \varphi \), then \( (\forall y\, \varphi)[t/x] = \forall y\, \varphi \) by the claim of the text. Now let \( x \) be free in \( \forall y\, \varphi \). Then \( y \) is not \( x \) and \( x \) is free in \( \varphi \); and since \( t \) is free for \( x \) in \( \forall y\, \varphi \) while \( x \) is free there, \( y \notin \mathrm{Var}(t) \) and \( t \) is free for \( x \) in \( \varphi \) (the recursive description of "free for"). So
\[
\begin{aligned}
\mathrm{FV}\bigl( (\forall y\, \varphi)[t/x] \bigr)
&= \mathrm{FV}\bigl( \varphi[t/x] \bigr) \setminus \{y\}
= \bigl( (\mathrm{FV}(\varphi) \setminus \{x\}) \cup \mathrm{Var}(t) \bigr) \setminus \{y\} \\
&= \bigl( \mathrm{FV}(\varphi) \setminus \{x, y\} \bigr) \cup \mathrm{Var}(t)
= E(\forall y\, \varphi),
\end{aligned}
\]
where the third equality uses \( y \notin \mathrm{Var}(t) \), and the last uses \( \mathrm{FV}(\forall y\, \varphi) = \mathrm{FV}(\varphi) \setminus \{y\} \). The case of \( \exists y \) is the same.

This proves \( S(\varphi) \) for every formula, and (a) is its first half.

*(b)* With \( \varphi = \exists y\, (y > x) \) and \( t = y + 1 \): \( \mathrm{FV}(\varphi) = \{x\} \), so the equation would give \( \mathrm{FV}(\varphi[t/x]) = \{y\} \). But \( \varphi[t/x] = \exists y\, (y > y + 1) \), whose set of free variables is \( \emptyset \). The \( y \) of the term was captured, so it is not free in the result; the quantifier case of the proof fails because \( y \in \mathrm{Var}(t) \).

For the second hypothesis, take \( \varphi = P(z) \) and \( t = y \). Then \( x \) is not free in \( \varphi \), and \( t \) is free for \( x \) (there are no quantifiers). Now \( \varphi[t/x] = P(z) \), with free variables \( \{z\} \), while the equation would give \( \{z\} \cup \{y\} = \{y, z\} \). Without a free \( x \), nothing is put in, so the variables of \( t \) do not appear.

**Marking scheme.** (10 points)

- 3: the quantifier case reduced to \( \mathrm{FV}(\varphi[t/x]) \setminus \{y\} \) by the definitions.
- 3: the use of "free for" to get \( y \notin \mathrm{Var}(t) \) and \( t \) free for \( x \) in \( \varphi \), naming where it is used.
- 1: the case "\( x \) not free in \( \forall y\, \varphi \)" handled by the claim of the text.
- 3: both counterexamples of (b), each checked by computing both sides.

Fatal errors (0 for the step): using the equation \( \mathrm{FV}(\chi[t/x]) = (\mathrm{FV}(\chi) \setminus \{x\}) \cup \mathrm{Var}(t) \) for a part \( \chi \) in which \( x \) is not free (it fails there; see the second example in (b)); removing \( y \) from \( \mathrm{Var}(t) \) without justification.
:::

::: {#exr-terms-formulas-substitution-c2}
[C2: Renaming is not swapping]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \forall x\, \exists y\, (x < y) \) and \( \forall y\, \exists x\, (y < x) \) are the same sentence up to renaming bound variables: give a sequence of renamings, each allowed by the condition of the text, leading from the first to the second.
2. Show that \( \forall x\, \exists y\, (x < y) \) and \( \exists y\, \forall x\, (x < y) \) are **not** the same up to renaming. *Hint: what does a renaming leave unchanged?*
:::
:::

::: {.solution}
*(a)* A renaming needs a variable that does not appear in the formula, so the two letters cannot be exchanged in one step; go through a third letter \( z \).

1. In \( \forall x\, \exists y\, (x < y) \), rename the bound \( x \) to \( z \), which does not appear: \( \forall z\, \exists y\, (z < y) \).
2. Rename the bound \( y \) to \( x \), which no longer appears: \( \forall z\, \exists x\, (z < x) \).
3. Rename the bound \( z \) to \( y \), which no longer appears: \( \forall y\, \exists x\, (y < x) \).

Each step renames one quantifier and the occurrences it binds, to a letter absent from the formula at that moment. The result is the second sentence. (Over \( \nN \) both say "there is no largest natural number", in two spellings.)

*(b)* A renaming changes only which **letters** are used. It does not change the parse tree's shape, which quantifier symbol (\( \forall \) or \( \exists \)) sits at which node, or which quantifier node binds which occurrence. In \( \forall x\, \exists y\, (x < y) \) the root is a \( \forall \) node; in \( \exists y\, \forall x\, (x < y) \) the root is an \( \exists \) node. No sequence of renamings turns a \( \forall \) node into an \( \exists \) node, so no sequence of renamings leads from one sentence to the other.

The two sentences also say different things: over \( \nN \), the first is true (take \( y = x + 1 \)) and the second false (for any \( y \), take \( x = y \)). This is @exm-quantifier-order-sum again. Renaming changes the **names** of the placeholders; swapping changes the **order** in which they are chosen, and the order is what carries the meaning.
:::

<!-- dependency ledger
def-term (claim): unique readability for terms (fold F4.2-a) | pattern of thm-unique-readability (F1.3 §03); proof carries over, not repeated, stated as such in the text
def-first-order-formula (claim): structural induction, structural recursion and unique readability for first-order formulas and for terms, with atomic formulas as base case and the quantifier clauses as one-part building steps (main-line sentence; details in fold F4.2-b) | pattern of thm-structural-induction, thm-structural-recursion, thm-unique-readability (F1.3 §03); proofs carry over word for word, not repeated, stated as such in the text
def-free-variable (claim): the recursive description of "x is free in phi" (fold F4.2-c) | inline (read off the parse tree, argued in the text)
def-free-variable (example): Figure B: the x of P(x) free; the x's of Q(x), R(x, y) bound by forall x; the y bound by exists y | inline (read off def-free-variable)
def-substitution (claim): the recursion clauses define exactly one formula phi[t/x], and it is a formula (fold F4.2-e) | structural recursion carried over (see above); inline
def-substitution (claim): phi[x/x] = phi | inline (clause by clause; one sentence in the text)
def-substitution (proof): the claim "x not free in phi implies phi[t/x] = phi", including its term version (fold F4.2-e) | inline (structural induction, proved in the text)
def-substitution (example): "One substitution at a time": R(x, y)[y/x] = R(y, y), then [x/y] gives R(x, x); the swap through z; its Quick check | def-substitution, cited; checked by verify/ch05/exr-terms-formulas-substitution-a2.py
def-free-for (claim): the four special cases and the recursive description of "free for" (fold F4.2-f) | inline (from the definition, argued in the text)
def-free-for (example): the practical rule's Quick check: y is not free for x in exists y (x < y) and P(y); x + 1 is | inline (def-free-for); checked by verify/ch05/exr-terms-formulas-substitution-a2.py
terms-formulas-substitution-renaming (claim): renaming a bound variable keeps meaning | NOT proved here: front renaming derived in F1.4 §04 (forall) and F1.4 §06 (exists); inside a formula a stated convention; its semantic justification is the optional F1.6 §03 (cor-renaming-bound-variables), named only in the Looking-ahead box; nothing in this section depends on it except the recipe, which is stated as a convention
exm-free-and-bound-limit (example): a sequence is a function symbol a; membership in N a one-place predicate | conventions of F1.4 §01 (def-bounded-quantifier and "Mixing kinds of number"), recalled
terms-formulas-substitution-proofs (example): epsilon > 0 gives epsilon/2 > 0 | school arithmetic
terms-formulas-substitution-proofs (example): the induction display for a formula phi (fold F4.2-h) | restates ax-induction (cited); "free for" checked inline
terms-formulas-substitution-partial (claim): fold F5.2-i: every function symbol of this chapter's language is total on the domain; "the limit" only after exactly one is proved | the domain convention of this chapter, stated in the fold; "Section 5.8" an in-chapter pointer; nothing depends on the fold
exr-terms-formulas-substitution-a2 (solution): occurrences and repairs (a)-(d); computations (e)-(i); free for and renaming (j)-(l) | def-free-variable, def-substitution, def-free-for and the recipe, all in this section; checked by verify/ch05/exr-terms-formulas-substitution-a2.py
exr-terms-formulas-substitution-b2 (solution): structural recursion defines Var and FV | carried over (see above)
exr-terms-formulas-substitution-b2 (solution): over R, forall x exists y (x + y = z) holds with y = z - x | school arithmetic
exr-terms-formulas-substitution-b3 (solution): the two computations of (a) and (b), free-for at each step, capture by z in (c); over N with R as <, x = 2, y = 0: the swap true (z = 1), the computed formula false | def-substitution, def-free-for (this section); school order; checked by verify/ch05/exr-terms-formulas-substitution-b3.py
exr-terms-formulas-substitution-c1 (solution): term version by induction on terms; formula version by structural induction; uses the claim phi[t/x] = phi and the recursive descriptions of "free" and "free for" | inline; the claim and the descriptions are in the folds of this section
exr-terms-formulas-substitution-c2 (solution): renamings preserve the tree shape and the quantifier symbols at each node | inline (a renaming changes only the letters of one quantifier node and the occurrences it binds)
exr-terms-formulas-substitution-c2 (solution): over N, forall x exists y (x < y) true, exists y forall x (x < y) false | exm-quantifier-order-sum pattern; school arithmetic (x + 1 > x)
-->
