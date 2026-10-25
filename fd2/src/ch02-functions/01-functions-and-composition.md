# Functions and Composition

Chapter 1 made sets, pairs and relations precise. A relation from \( A \) to \( B \) is a subset of \( A \times B \) (@def-relation), and among the examples of Section 1.4 the graph of squaring relates each real number to exactly one number, while the unit circle relates \( 0 \) to two numbers and \( 2 \) to none. This chapter is about the first kind of relation. This section gives it its name, **function**, says when two functions are equal, uses functions to make families, sequences and the set \( Y^X \) precise, and composes them. The rest of the chapter asks what a function does to its inputs and to its codomain (Section 2.2), builds functions from pieces (Section 2.3), undoes them (Section 2.4), and applies them to whole sets (Section 2.5).

## What is a function?

Everyone has used functions since school, and the everyday definition is "a rule that assigns to each input one output". Look at the word "rule". The rules \( x \mapsto x^2 \) and \( x \mapsto (x + 1)^2 - 2x - 1 \) are different: one squares, the other adds, squares, subtracts, and subtracts again. Yet on every real number they give the same answer, and nobody would call them different functions. Other functions have no rule at all that one could write down. A table of measured temperatures, one per day, assigns to each day one number, and no formula produces it.

So the rule is not what matters. What matters is **which output goes with which input**: the set of input–output pairs. That set is a relation, and Section 1.4 said exactly when two relations are the same, namely when they contain the same pairs. So we forget the rule and keep the pairs. One more piece of data is needed, the set in which the outputs are **declared** to lie; the reason is given after the definition.

*A function is its graph, with a declared target.*

::: {#def-function}
[Function]

Let \( X \) and \( Y \) be sets. A **function from \( X \) to \( Y \)**, written \( f \colon X \to Y \), is given by a relation \( G \subseteq X \times Y \), the **graph** of \( f \), such that
\[
\text{for every } x \in X \text{ there is exactly one } y \in Y \text{ with } (x, y) \in G ,
\]
together with the set \( Y \), the **codomain** of \( f \). Formally, \( f \) is the pair \( (G, Y) \). The set \( X \) is the **domain** of \( f \). For \( x \in X \), the unique \( y \) with \( (x, y) \in G \) is written \( f(x) \), the **value** of \( f \) at \( x \). We write \( (x, y) \in f \) for \( (x, y) \in G \), and \( x \mapsto f(x) \) for the whole function when its domain and codomain are clear.

In symbols, the condition on the graph is
\[
\forall x \in X \ \ \exists! \, y \in Y \ \ (x, y) \in G ,
\]
where, as with the bounded quantifiers of @fd1:def-bounded-quantifier, \( \exists! \, y \in Y \ \psi \) abbreviates \( \exists! \, y \, (y \in Y \wedge \psi) \).
:::

The whole definition is the quantifier pattern \( \forall \exists! \). By @fd1:def-unique-existence, "\( \exists! \, y \)" is an existence claim and a uniqueness claim, and by @fd1:prp-unique-existence-use the uniqueness claim may be stated without reference to the witness; so the condition on the graph is two clauses:

- **(Fn1)** (existence) for every \( x \in X \) there is **at least one** \( y \in Y \) with \( (x, y) \in G \): every input has an output;
- **(Fn2)** (uniqueness) for every \( x \in X \) and all \( y, y' \in Y \), if \( (x, y) \in G \) and \( (x, y') \in G \), then \( y = y' \): no input has two outputs.

In words: the graph is a set of input–output pairs, with inputs from \( X \) and outputs from \( Y \); (Fn1) says no input is left without an output, and (Fn2) says no input is given two. The codomain \( Y \) is where outputs are allowed to lie. It need not consist of outputs: \( x \mapsto x^2 \) can be declared as a function from \( \nR \) to \( \nR \), although no output is negative. The set of outputs that actually occur is the **range** of \( f \),
\[
\{ y \in Y : \exists x \in X \ \ f(x) = y \} ,
\]
which Section 2.5 will call the image of \( X \) and write \( f(X) \). The domain needs no slot of its own in the pair \( (G, Y) \): by (Fn1) every \( x \in X \) occurs as a first coordinate in \( G \), and since \( G \subseteq X \times Y \), nothing else does. So the graph determines the domain.

**The notation \( f(x) \) is well defined.** Writing "**the** \( y \) with \( (x, y) \in f \)" is legitimate only if there is one, and only one. Clause (Fn1) supplies one, and clause (Fn2) says that any two are equal; together they license the article "the". This gives the equivalence that every argument with functions uses:
\[
(x, y) \in f \iff y = f(x) \qquad (x \in X, \ y \in Y). \tag{$\ast\ast$}
\]
For \( (\Leftarrow) \): \( (x, f(x)) \in f \) by the choice of \( f(x) \), and if \( y = f(x) \) then \( (x, y) \in f \) by substituting equals (\( \rulename{=E} \), @fd1:def-rules-equality). For \( (\Rightarrow) \): both \( (x, y) \) and \( (x, f(x)) \) lie in \( f \), so \( y = f(x) \) by (Fn2). Two consequences follow at once. Equal inputs give equal outputs: if \( x_1 = x_2 \), then \( f(x_1) = f(x_2) \). And every value lies in the codomain: \( f(x) \in Y \) for every \( x \in X \).

**Functions given by formulas.** Most functions in this book are introduced by a formula: "let \( f \colon \nR \to \nR \), \( f(x) = x^2 \)". This means the function whose graph is \( \{ (x, y) \in \nR^2 : y = x^2 \} \). Clause (Fn2) holds for any such graph: if \( y = x^2 \) and \( y' = x^2 \), then \( y = y' \). So for a formula only (Fn1) needs checking, and it says: for each \( x \) in the domain, the formula **makes sense** and its value **lies in the codomain**. For \( x^2 \) on \( \nR \) both are clear. For "\( f \colon \nR \to \nR \), \( f(x) = 1/x \)" the formula makes no sense at \( x = 0 \), and (Fn1) fails there; for "\( f \colon \nR \to [0, \infty) \), \( f(x) = x^2 \)" the value must be checked to lie in \( [0, \infty) \), which it does, since squares are nonnegative.

A function whose domain is a product \( A \times B \) is a **function of two variables**. Its inputs are pairs, and we write \( f(a, b) \) rather than \( f((a, b)) \). Addition \( (m, n) \mapsto m + n \) from \( \nN \times \nN \) to \( \nN \) is an example.

::: {#exm-first-functions}
[First functions]

Check (Fn1) and (Fn2), and find the range, for each of the following.

(a) \( f \colon \{1, 2, 3\} \to \{a, b\} \) with graph \( \{ (1, a), (2, b), (3, a) \} \).

(b) The **identity function** \( \id_X \colon X \to X \), \( \id_X(x) = x \), for a set \( X \).

(c) A **constant function** \( X \to Y \), \( x \mapsto c \), for a fixed \( c \in Y \).

(d) The **indicator function** \( \ind_A \colon X \to \{0, 1\} \) of a subset \( A \subseteq X \):
\[
\ind_A(x) = \begin{cases} 1 & \text{if } x \in A, \\ 0 & \text{if } x \in X \setminus A. \end{cases}
\]
:::

::: {.solution}
(a) The graph is a subset of \( \{1, 2, 3\} \times \{a, b\} \). Each of \( 1 \), \( 2 \), \( 3 \) occurs as a first coordinate (Fn1), and each occurs exactly once, so no input has two outputs (Fn2). So \( f \) is a function, with \( f(1) = a \), \( f(2) = b \), \( f(3) = a \). Its range is \( \{a, b\} \), the whole codomain. A function on a small finite set is often given this way, by listing its values; no formula is needed.

(b) The graph is the **diagonal** \( \{ (x, x) : x \in X \} \). For each \( x \), the pair \( (x, x) \) is in it (Fn1); and if \( (x, y) \) is in it, then \( (x, y) = (z, z) \) for some \( z \in X \), and the characteristic property (@def-ordered-pair) gives \( x = z = y \) (Fn2). The range is \( X \).

(c) The graph is \( X \times \{c\} \). For each \( x \in X \), \( (x, c) \) is in it (Fn1); if \( (x, y) \) is in it, then \( y \in \{c\} \) by the membership test \( (\ast) \) for pairs in a product (@def-cartesian-product), so \( y = c \) (Fn2). If \( X \) has an element, the range is \( \{c\} \). If \( X = \emptyset \), the range is \( \emptyset \).

(d) The graph is \( \bigl(A \times \{1\}\bigr) \cup \bigl((X \setminus A) \times \{0\}\bigr) \). For (Fn1), let \( x \in X \). By excluded middle (@fd1:prp-excluded-middle), \( x \in A \) or \( x \notin A \); in the first case \( (x, 1) \) is in the graph, in the second \( x \in X \setminus A \) and \( (x, 0) \) is. For (Fn2), the two cases cannot both hold, so \( x \) never receives both \( 0 \) and \( 1 \), and each case gives only one pair with first coordinate \( x \). The range is \( \{0, 1\} \) if \( A \) has an element and \( X \setminus A \) has an element; it is \( \{0\} \) if \( A = \emptyset \) and \( X \) has an element, \( \{1\} \) if \( A = X \) and \( X \) has an element, and \( \emptyset \) if \( X = \emptyset \). This is the first function of the chapter whose existence clause needs excluded middle: the definition by cases is a function only because every \( x \) falls into one of the cases.
:::

The next example collects relations that fail to be functions. Each failure is one clause, and it pays to say which.

::: {#exm-not-a-function}
[Relations that are not functions]

(a) Is the unit circle \( S = \{ (x, y) \in \nR^2 : x^2 + y^2 = 1 \} \) the graph of a function \( \nR \to \nR \)?

(b) "Send a fraction \( p/q \) to its numerator \( p \)." Is this a function from \( \nQ \) to \( \nZ \)? As a relation it is
\[
N \coloneqq \{ (r, p) \in \nQ \times \nZ : \exists q \in \nZ_{>0} \ \ r = p/q \} .
\]
:::

::: {.solution}
(a) No, and both clauses fail, at different points. Clause (Fn2) fails at \( x = 0 \): both \( (0, 1) \) and \( (0, -1) \) lie in \( S \), and \( 1 \ne -1 \). Clause (Fn1) fails at \( x = 2 \): a pair \( (2, y) \in S \) would need \( y^2 = 1 - 4 = -3 \), and no real square is negative. Restricting the inputs to \( [-1, 1] \) repairs (Fn1) but not (Fn2); keeping only the upper half, \( y \ge 0 \), repairs (Fn2) as well, and gives the function \( [-1, 1] \to \nR \), \( x \mapsto \sqrt{1 - x^2} \).

(b) No. Clause (Fn1) holds: every rational number is \( p/q \) for some \( p \in \nZ \) and \( q \in \nZ_{>0} \). But (Fn2) fails, because a rational number has many ways of being written as a fraction. Since \( \tfrac{1}{2} = \tfrac{2}{4} \), both \( (\tfrac12, 1) \) and \( (\tfrac12, 2) \) lie in \( N \), and \( 1 \ne 2 \). The "rule" gives an output that depends on **how the input is written**, not on the input. A function may not do that, since its value is attached to the input itself. This is why definitions of the form "write \( x \) as …, then send it to …" must be checked for **well-definedness**, a check that returns in Chapter 5 for functions defined on classes. Here the repair is to fix the way of writing: let \( q_0 \) be the least \( q \in \nZ_{>0} \) with \( rq \in \nZ \) (such \( q \) exist, by the first sentence, so there is a least one by well-ordering, proved in Chapter 3; a least element is unique), and send \( r \) to \( r q_0 \). This is a function.
:::

::: {.second-reading title="Why each clause, and why a codomain"}
**Why this definition.** Each clause has a job, and dropping one lets in the failures of @exm-not-a-function. Without (Fn1), a "function" could be undefined at some inputs, like \( 1/x \) at \( 0 \); then \( f(x) \) would not name anything, and statements "for every \( x \in X \)" about \( f(x) \) would lose their meaning. Without (Fn2), \( f(x) \) would not name **one** thing, and \( f(\tfrac12) \) in part (b) would be both \( 1 \) and \( 2 \). The graph replaces the rule because two rules can describe one function, and sets are compared by their elements.

Why is the codomain part of the data? A relation is a set, so if a function were only its graph, two functions with the same graph would be equal (@def-set-equality), whatever target was declared. The graph of \( x \mapsto x^2 \) as a function \( [0, \infty) \to \nR \) is the same set as its graph as a function \( [0, \infty) \to [0, \infty) \). But these should be different functions, because the second reaches every point of its target and the first does not: this is the property called surjectivity in Section 2.2, and @exm-square-three-ways there shows it changing with the codomain. Recording the codomain in the pair \( (G, Y) \) keeps the two apart. Many books take the same convention, some without saying so.
:::

::: {.warning}
A formula is not yet a function. "The function \( 1/x \)" names no function until a domain and a codomain are given, and the domain must be chosen so that (Fn1) holds: \( x \mapsto 1/x \) is a function \( \nR \setminus \{0\} \to \nR \), and there is no function \( \nR \to \nR \) given by this formula. Likewise \( \sqrt{x} \) makes sense on \( [0, \infty) \) and not on \( \nR \). When you meet "let \( f(x) = \dots \)", ask first where \( x \) lives and where \( f(x) \) is meant to lie.
:::

::: {.check}
Which of these relations on \( \{1, 2, 3\} \) are graphs of functions \( \{1, 2, 3\} \to \{1, 2, 3\} \): \( \{ (1, 2), (2, 2), (3, 2) \} \), \( \{ (1, 1), (2, 2) \} \), \( \{ (1, 3), (2, 1), (3, 2), (2, 3) \} \)? For each that is not, name the clause that fails.
:::

::: {.solution}
The first is a function: the constant function with value \( 2 \). The second fails (Fn1) at \( 3 \), which has no output. The third fails (Fn2) at \( 2 \), which has the two outputs \( 1 \) and \( 3 \).
:::

## When are two functions equal?

A function is a pair \( (G, Y) \), so two functions are equal when their graphs are equal and their codomains are equal. In practice we compare functions by their values, and the next result says that this is the same test.

::: {#prp-function-equality}
[Equality of Functions]

Let \( f \colon X \to Y \) and \( g \colon X' \to Y' \) be functions. Then \( f = g \) if and only if \( X = X' \), \( Y = Y' \), and \( f(x) = g(x) \) for every \( x \in X \).
:::

::: {.idea}
Write \( f = (G, Y) \) and \( g = (G', Y') \). The characteristic property of pairs splits \( f = g \) into "same graph" and "same codomain". Two graphs are equal when they have the same elements, and by \( (\ast\ast) \) an element of a graph is a pair \( (x, f(x)) \); so "same graph" is "same inputs, same outputs".
:::

::: {.proof}
Write \( f = (G, Y) \) and \( g = (G', Y') \), as in @def-function.

\( (\Rightarrow) \) Suppose \( f = g \). By the characteristic property of pairs (@def-ordered-pair), \( G = G' \) and \( Y = Y' \). The domain is determined by the graph, as the set of first coordinates of its elements, so \( X = X' \). Let \( x \in X \). By \( (\ast\ast) \), \( (x, f(x)) \in G = G' \), so \( (x, f(x)) \in g \), and \( (\ast\ast) \) for \( g \) gives \( f(x) = g(x) \).

\( (\Leftarrow) \) Suppose \( X = X' \), \( Y = Y' \), and \( f(x) = g(x) \) for every \( x \in X \). We show \( G \subseteq G' \). Let \( p \in G \). Since \( G \subseteq X \times Y \), \( p = (x, y) \) with \( x \in X \) and \( y \in Y \). By \( (\ast\ast) \), \( y = f(x) \), so \( y = g(x) \) by the hypothesis, and then \( p = (x, y) \in G' \) by \( (\ast\ast) \) for \( g \). The same argument with \( f \) and \( g \) exchanged gives \( G' \subseteq G \), so \( G = G' \) by @prp-subset-antisymmetric. Since also \( Y = Y' \), the characteristic property gives \( (G, Y) = (G', Y') \), that is, \( f = g \).
:::

So to show two functions equal, check three things: the same domain, the same codomain, and the same value at an arbitrary point. To show them different, one witness suffices: a point where the values differ, or a difference in domain or codomain.

::: {#exm-equal-functions}
[Equal and unequal functions]

Decide which of these functions are equal.

(a) \( f, g \colon \nR \to \nR \), \( f(x) = (x + 1)^2 - 2x - 1 \) and \( g(x) = x^2 \).

(b) \( h, k \colon \nR \to \nR \), \( h(x) = \abs{x} \) and \( k(x) = \sqrt{x^2} \).

(c) \( s_1 \colon [0, \infty) \to \nR \) and \( s_2 \colon [0, \infty) \to [0, \infty) \), both given by \( x \mapsto x^2 \).
:::

::: {.solution}
(a) Equal. The domains are both \( \nR \) and the codomains both \( \nR \). For every real \( x \), \( (x + 1)^2 - 2x - 1 = x^2 + 2x + 1 - 2x - 1 = x^2 \). By @prp-function-equality, \( f = g \): two rules, one function.

(b) Equal. Same domain and codomain, and for every real \( x \), \( \sqrt{x^2} = \abs{x} \): the number \( \abs{x} \) is nonnegative and its square is \( x^2 \), and \( \sqrt{x^2} \) is by definition the nonnegative number with square \( x^2 \), which is unique by @fd1:thm-squares-order.

(c) Not equal. They have the same domain, the same values, and even the same graph; but their codomains \( \nR \) and \( [0, \infty) \) are different sets (\( -1 \) is in one and not the other), so by @prp-function-equality \( s_1 \ne s_2 \).
:::

**Restriction.** A function can be cut down to a smaller domain. For \( f \colon X \to Y \) and \( A \subseteq X \), the **restriction** of \( f \) to \( A \) is the function
\[
f|_A \colon A \to Y, \qquad f|_A(a) \coloneqq f(a) ,
\]
whose graph is \( G \cap (A \times Y) \): the pairs of \( f \) whose input lies in \( A \). The squaring function \( \nR \to \nR \) restricted to \( [0, \infty) \) is \( s_1 \) of part (c). The bar in \( f|_A \) is one of the uses of a vertical bar that the book's colon-for-set-builder convention keeps free.

## Families, sequences, and the set of all functions

Section 1.3 used families of sets \( (A_i)_{i \in I} \) and described them informally, as "a set \( A_i \) for each index \( i \in I \)". We can now say exactly what a family is, once its members are known to lie in some set. A **family of subsets of \( X \) indexed by \( I \)** is a function \( I \to \powerset{X} \), \( i \mapsto A_i \), with the power set \( \powerset{X} \) as the codomain the definition asks for. More generally, if \( S \) is a set whose elements are sets, a family of members of \( S \) indexed by \( I \) is a function \( I \to S \). A codomain must be named, because there is no set of all sets (@thm-russell). The value of a family at \( i \) is written \( A_i \) rather than \( A(i) \), and the family is written \( (A_i)_{i \in I} \), in parentheses because it is indexed. A family is not the same thing as its set of values \( \{ A_i : i \in I \} \): the family \( (A_i)_{i \in \{1, 2\}} \) with \( A_1 = A_2 = \{0\} \) has two indices and one value.

In the same way, a **sequence** of real numbers \( (a_n)_{n \ge 1} \) is a function \( \nZ_{>0} \to \nR \), \( n \mapsto a_n \), with the value at \( n \) written \( a_n \). The sequence \( (1/n) \) is the function \( n \mapsto 1/n \), and its set of values is \( \{ 1/n : n \ge 1 \} \). Sequences are the main object of *Analysis on the Real Line*.

Finally, all functions from \( X \) to \( Y \) form a set, written
\[
Y^X \coloneqq \{ f \in \powerset{X \times Y} \times \{Y\} : f \text{ is a function from } X \text{ to } Y \} .
\]

::: {.second-reading title="Where $Y^X$ comes from"}
It is a set by the working rules of Section 1.2: every function \( X \to Y \) is a pair \( (G, Y) \) with \( G \in \powerset{X \times Y} \), so \( Y^X \) is the subset of \( \powerset{X \times Y} \times \{Y\} \) cut out by the condition of @def-function, and this product is a set by (W2), (W4), and (W5), so \( Y^X \) is a set by specification (W1).
:::

The letters are in this order because, for finite sets, \( Y^X \) has \( m^n \) elements when \( Y \) has \( m \) and \( X \) has \( n \), as the next example suggests; counting is the business of Section 4.1. The set \( \{0, 1\}^{\nN} \) of all sequences of zeros and ones, indexed from \( 0 \), plays a leading role in Chapter 4.

::: {#exm-function-set-small}
[All functions between two small sets]

List the elements of \( \{0, 1\}^{\{1, 2\}} \), and say which are indicator functions of subsets of \( \{1, 2\} \).
:::

::: {.solution}
A function \( f \colon \{1, 2\} \to \{0, 1\} \) is determined by its two values \( f(1) \) and \( f(2) \) (@prp-function-equality), and each may be \( 0 \) or \( 1 \). So there are four:

| \( f(1) \) | \( f(2) \) | graph | indicator of |
|---|---|---|---|
| \( 0 \) | \( 0 \) | \( \{ (1, 0), (2, 0) \} \) | \( \emptyset \) |
| \( 0 \) | \( 1 \) | \( \{ (1, 0), (2, 1) \} \) | \( \{2\} \) |
| \( 1 \) | \( 0 \) | \( \{ (1, 1), (2, 0) \} \) | \( \{1\} \) |
| \( 1 \) | \( 1 \) | \( \{ (1, 1), (2, 1) \} \) | \( \{1, 2\} \) |

Every one of them is an indicator function: \( f = \ind_A \) for \( A = \{ x \in \{1, 2\} : f(x) = 1 \} \). The four subsets of \( \{1, 2\} \) and the four functions correspond one to one.
:::

The correspondence at the end of the example, between subsets of \( X \) and functions \( X \to \{0, 1\} \), holds for every set \( X \): send \( f \) to \( \{ x \in X : f(x) = 1 \} \) and \( A \) to \( \ind_A \). So counting the subsets of a finite set and counting the functions from it to \( \{0, 1\} \) are one problem, which Section 4.1 solves.

**A game with five strings.** A string of five symbols \( 0 \) or \( 1 \), such as \( 01101 \), is a function \( \{1, \dots, 5\} \to \{0, 1\} \): its value at \( k \) is its \( k \)-th symbol. One player lists five strings, say \( 00000 \), \( 11111 \), \( 01010 \), \( 10101 \), \( 00111 \); the other must write a string not on the list. Searching all \( 32 \) always works, but is there a rule that builds a missing string from **any** list of five in five steps? Try one. Chapter 4 comes back to this game.

::: {.check}
Which string is the indicator function of \( \{1, 4\} \subseteq \{1, \dots, 5\} \)? What is the value at \( 2 \) of the string \( 01100 \)?
:::

::: {.solution}
The indicator of \( \{1, 4\} \) has value \( 1 \) at \( 1 \) and \( 4 \) and value \( 0 \) elsewhere, so it is the string \( 10010 \). The value of \( 01100 \) at \( 2 \) is its second symbol, \( 1 \).
:::

The empty set gives the degenerate cases, and they are worth settling now, since they are the test cases of many later statements.

::: {#prp-empty-function}
[Functions and the Empty Set]

(a) For every set \( Y \) there is exactly one function from \( \emptyset \) to \( Y \): the pair \( (\emptyset, Y) \), called the **empty function**.

(b) If \( X \) is nonempty (it has an element), there is no function from \( X \) to \( \emptyset \).
:::

::: {.second-reading title="The empty function, proved"}
::: {.proof}
(a) *Existence.* The empty relation satisfies \( \emptyset \subseteq \emptyset \times Y \), since \( \emptyset \) is a subset of every set (Section 1.2). The condition of @def-function reads "for every \( x \), if \( x \in \emptyset \), then there is exactly one \( y \in Y \) with \( (x, y) \in \emptyset \)". For each \( x \) the hypothesis \( x \in \emptyset \) is false, so the implication holds (@fd1:prp-vacuous-implication). So \( (\emptyset, Y) \) is a function from \( \emptyset \) to \( Y \).

*Uniqueness.* Let \( (G, Y) \) be any function from \( \emptyset \) to \( Y \). Its graph satisfies \( G \subseteq \emptyset \times Y = \emptyset \), by the mirror-image \( \emptyset \) law of @prp-product-set-laws. So an element of \( G \) would be an element of \( \emptyset \); \( G \) has no elements, and \( G = \emptyset \) by @prp-empty-set-unique. Hence \( (G, Y) = (\emptyset, Y) \).

(b) Let \( x_0 \in X \), and suppose \( f \colon X \to \emptyset \) were a function. By (Fn1) there would be \( y \in \emptyset \) with \( (x_0, y) \in f \); but \( \emptyset \) has no elements. So there is no such function \( [\rulename{\neg I}] \).
:::

In the notation \( Y^X \): the set \( Y^{\emptyset} \) has exactly one element for every \( Y \), including \( Y = \emptyset \); and \( \emptyset^X = \emptyset \) whenever \( X \) is nonempty. The empty function \( \emptyset \to Y \) returns in Section 2.4 as the witness that a hypothesis there cannot be dropped.
:::

::: {.check}
How many elements do \( \{0, 1\}^{\emptyset} \) and \( \emptyset^{\{0\}} \) have?
:::

::: {.solution}
The set \( \{0, 1\}^{\emptyset} \) has exactly one element, the empty function \( (\emptyset, \{0, 1\}) \), by @prp-empty-function (a). The set \( \emptyset^{\{0\}} \) has none, by @prp-empty-function (b), since \( \{0\} \) has the element \( 0 \).
:::

## Composition

Two functions can be applied one after the other when the outputs of the first are inputs of the second. Temperature in degrees Celsius, as a function of the day, followed by the conversion to degrees Fahrenheit, gives temperature in Fahrenheit as a function of the day.

::: {#def-composition}
[Composition]

Let \( f \colon X \to Y \) and \( g \colon Y \to Z \) be functions, the codomain of \( f \) being the domain of \( g \). Their **composite** is the function
\[
g \circ f \colon X \to Z, \qquad (g \circ f)(x) \coloneqq g(f(x)) ,
\]
read "\( g \) after \( f \)".
:::

This is a function by the remark on formulas: for \( x \in X \), the value \( f(x) \) lies in \( Y \), the domain of \( g \), so \( g(f(x)) \) makes sense, and it lies in \( Z \). Its graph is \( \{ (x, z) \in X \times Z : z = g(f(x)) \} \). The order of the letters is the order of the formula \( g(f(x)) \), which is the **reverse** of the order in which the functions act: \( f \) acts first.

::: {#exm-composition-order}
[The order of composition matters]

Let \( f, g \colon \nR \to \nR \), \( f(x) = x + 1 \) and \( g(x) = 2x \). Compute \( g \circ f \) and \( f \circ g \), and decide whether they are equal.
:::

::: {.solution}
By @def-composition, \( (g \circ f)(x) = g(x + 1) = 2x + 2 \) and \( (f \circ g)(x) = f(2x) = 2x + 1 \). At \( x = 0 \) the values are \( 2 \) and \( 1 \), so by @prp-function-equality \( g \circ f \ne f \circ g \). In words: "add one, then double" is not "double, then add one". (In fact the two composites differ at every \( x \), since \( 2x + 2 \ne 2x + 1 \); one point already suffices.)
:::

The next example composes two functions that look as if they cancel each other, and finds that they do so in one order only.

::: {#exm-root-and-square}
[Square root after squaring, and squaring after square root]

Let \( q \colon \nR \to [0, \infty) \), \( q(x) = x^2 \), and \( r \colon [0, \infty) \to \nR \), \( r(t) = \sqrt{t} \). Which of \( r \circ q \) and \( q \circ r \) are defined? Compute them, and compare each with an identity function.
:::

::: {.solution}
*The composite \( r \circ q \).* It is defined, since the codomain \( [0, \infty) \) of \( q \) is the domain of \( r \) (@def-composition). It is a function \( \nR \to \nR \) with
\[
(r \circ q)(x) = \sqrt{x^2} = \abs{x} ,
\]
by @exm-equal-functions (b). It is not \( \id_{\nR} \): its value at \( -1 \) is \( 1 \), and \( \id_{\nR}(-1) = -1 \).

*The composite \( q \circ r \).* It is defined as well, since the codomain \( \nR \) of \( r \) is the domain of \( q \). It is a function \( [0, \infty) \to [0, \infty) \) with
\[
(q \circ r)(t) = \bigl(\sqrt{t}\bigr)^2 = t \qquad (t \ge 0) ,
\]
because \( \sqrt{t} \) is by definition a number whose square is \( t \). The functions \( q \circ r \) and \( \id_{[0, \infty)} \) have the same domain, the same codomain and the same value at every point, so \( q \circ r = \id_{[0, \infty)} \) by @prp-function-equality.

So one order gives an identity function and the other does not. Applying \( r \) and then \( q \) returns every input; applying \( q \) and then \( r \) loses the sign. So \( q \) undoes \( r \), but \( r \) does not undo \( q \).
:::

::: {.second-reading title="Composites defined in one order only"}
Composition can also fail to be defined in one order only. For \( f \colon \{1, 2\} \to \nR \) and \( g \colon \nR \to \nR \), the composite \( g \circ f \colon \{1, 2\} \to \nR \) is defined, and \( f \circ g \) is not: \( g \)'s outputs are real numbers, and \( f \) accepts only \( 1 \) and \( 2 \).
:::

Composition is not commutative, but it is associative, and the identity functions do nothing.

::: {#prp-composition-associative}
[Composition Is Associative]

Let \( f \colon X \to Y \), \( g \colon Y \to Z \), and \( h \colon Z \to W \) be functions. Then
\[
h \circ (g \circ f) = (h \circ g) \circ f ,
\]
and \( f \circ \id_X = f = \id_Y \circ f \).
:::

::: {.proof}
Both sides of the first equation are functions from \( X \) to \( W \), by @def-composition. For \( x \in X \), applying @def-composition twice on each side gives
\[
\bigl(h \circ (g \circ f)\bigr)(x) = h\bigl((g \circ f)(x)\bigr) = h(g(f(x))) = (h \circ g)(f(x)) = \bigl((h \circ g) \circ f\bigr)(x) .
\]
So the two functions agree at every point, and they are equal by @prp-function-equality. Likewise \( f \circ \id_X \) and \( \id_Y \circ f \) are functions from \( X \) to \( Y \) with values \( f(\id_X(x)) = f(x) \) and \( \id_Y(f(x)) = f(x) \), so both equal \( f \).
:::

Because of associativity, we write \( h \circ g \circ f \) without brackets: every way of bracketing gives the same function, \( x \mapsto h(g(f(x))) \).

The identity functions play for composition the part that the number \( 1 \) plays for multiplication: by the second statement of @prp-composition-associative, composing with an identity changes nothing. The analogy stops at division. A number \( a \ne 0 \) can be cancelled from \( ab = ac \); a function \( f \) can be cancelled from \( f \circ g = f \circ h \) only under a condition on \( f \). And in @exm-root-and-square, \( q \circ r = \id_{[0, \infty)} \) although \( r \circ q \ne \id_{\nR} \): one composite of two functions can be an identity while the other is not.

::: {.check}
Find \( h \colon \nR \to \nR \) with \( h \circ g = f \), for \( f(x) = 2x + 3 \) and \( g(x) = x + 1 \).
:::

::: {.solution}
The function \( g \) turns \( x \) into \( y = x + 1 \), and \( x \) is recovered as \( y - 1 \). So put \( h(y) \coloneqq 2(y - 1) + 3 = 2y + 1 \). Check: \( h(g(x)) = 2(x + 1) + 1 = 2x + 3 = f(x) \) for every \( x \), so \( h \circ g = f \) by @prp-function-equality.
:::

::: {.check}
For \( f, g \colon \nR \to \nR \), \( f(x) = x^2 \) and \( g(x) = x - 3 \), compute \( (g \circ f)(2) \) and \( (f \circ g)(2) \).
:::

::: {.solution}
\( (g \circ f)(2) = g(4) = 1 \) and \( (f \circ g)(2) = f(-1) = 1 \). The values agree at this point, but the functions are different: at \( x = 0 \), \( (g \circ f)(0) = -3 \) and \( (f \circ g)(0) = 9 \). Agreement at one point proves nothing about equality; disagreement at one point proves inequality.
:::

## Exercises

### A. Check your understanding

::: {#exr-functions-and-composition-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Let \( X = \{1, 2, 3\} \) and let \( f \colon X \to X \) be given by \( f(1) = 2 \), \( f(2) = 3 \), \( f(3) = 3 \). Write the graph of \( f \), and list the values of \( f \circ f \) and \( f \circ f \circ f \).
2. Which of the formulas \( 1/(x^2 + 1) \), \( \sqrt{x - 1} \), \( 1/(x^2 - 1) \) define a function \( \nR \to \nR \)? For each that does not, name a point where (Fn1) fails.
3. Are \( f, g \colon \nZ \to \nZ \), \( f(n) = n^2 - n \) and \( g(n) = n(n - 1) \), equal? Are \( h, k \colon \{0, 1\} \to \nZ \), \( h(x) = x^2 \) and \( k(x) = x \), equal?
4. How many elements do \( \{0\}^{\{1, 2, 3\}} \) and \( \emptyset^{\{1\}} \) have? Name them.
:::
:::

::: {.solution}
(a) The graph is \( \{ (1, 2), (2, 3), (3, 3) \} \). For \( f \circ f \): \( f(f(1)) = f(2) = 3 \), \( f(f(2)) = f(3) = 3 \), \( f(f(3)) = f(3) = 3 \), so \( f \circ f \) sends every point to \( 3 \). Then \( f \circ f \circ f = f \circ (f \circ f) \) sends every point to \( f(3) = 3 \): it is the constant function with value \( 3 \), and equal to \( f \circ f \).

(b) The formula \( 1/(x^2 + 1) \) defines a function \( \nR \to \nR \): \( x^2 + 1 \ge 1 \), so the denominator is never \( 0 \). The formula \( \sqrt{x - 1} \) does not: at \( x = 0 \) it asks for \( \sqrt{-1} \), and no real number has square \( -1 \) (it fails at every \( x < 1 \)). The formula \( 1/(x^2 - 1) \) does not: it fails at \( 1 \) and at \( -1 \), where the denominator is \( 0 \).

(c) Yes: both have domain and codomain \( \nZ \), and \( n^2 - n = n(n - 1) \) for every integer \( n \), so \( f = g \) by @prp-function-equality. Yes again: \( h(0) = 0 = k(0) \) and \( h(1) = 1 = k(1) \), so \( h \) and \( k \) agree at both points of their common domain; two rules, one function.

(d) The set \( \{0\}^{\{1, 2, 3\}} \) has exactly one element, the constant function with value \( 0 \) (@exm-first-functions (c)). A function \( \{1, 2, 3\} \to \{0\} \) must send each of \( 1 \), \( 2 \), \( 3 \) to \( 0 \), so any two such functions agree at every point and are equal by @prp-function-equality. The set \( \emptyset^{\{1\}} \) has no element: a function \( \{1\} \to \emptyset \) would need a value at \( 1 \) (@prp-empty-function (b)).
:::

### B. Practice

::: {#exr-functions-and-composition-b1}
[B1: Composites of real functions]

Let \( f, g \colon \nR \to \nR \), \( f(x) = x^2 + 1 \) and \( g(x) = 2x - 3 \).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( g \circ f \) and \( f \circ g \).
2. Find every \( x \in \nR \) with \( (g \circ f)(x) = (f \circ g)(x) \).
3. Find a function \( h \colon \nR \to \nR \) with \( h \circ g = f \), and check it.
:::
:::

::: {.solution}
(a) By @def-composition, \( (g \circ f)(x) = 2(x^2 + 1) - 3 = 2x^2 - 1 \) and \( (f \circ g)(x) = (2x - 3)^2 + 1 = 4x^2 - 12x + 10 \).

(b) The equation \( 2x^2 - 1 = 4x^2 - 12x + 10 \) is equivalent to \( 2x^2 - 12x + 11 = 0 \). Its discriminant is \( 144 - 88 = 56 = 4 \cdot 14 \), so by the quadratic formula
\[
x = \frac{12 \pm 2\sqrt{14}}{4} = 3 \pm \tfrac12 \sqrt{14} .
\]
These two numbers are the only points where the composites agree.

(c) The function \( g \) turns \( x \) into \( y = 2x - 3 \), and \( x \) is recovered as \( (y + 3)/2 \). So put
\[
h(y) \coloneqq \Bigl(\frac{y + 3}{2}\Bigr)^2 + 1 = \frac{y^2 + 6y + 13}{4} .
\]
*Check:* for every \( x \in \nR \),
\[
h(g(x)) = \Bigl(\frac{(2x - 3) + 3}{2}\Bigr)^2 + 1 = x^2 + 1 = f(x) ,
\]
and \( h \circ g \) and \( f \) both go from \( \nR \) to \( \nR \), so \( h \circ g = f \) by @prp-function-equality.
:::

::: {#exr-functions-and-composition-b2}
[B2: A map of the plane]

Let \( s \colon \nR^2 \to \nR^2 \), \( s(x, y) = (x + y, x - y) \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( (s \circ s)(x, y) = (2x, 2y) \) for all \( x, y \in \nR \).
2. Find a function \( t \colon \nR^2 \to \nR^2 \) with \( t \circ s = \id_{\nR^2} \), and check that also \( s \circ t = \id_{\nR^2} \). (Hint: solve \( u = x + y \), \( v = x - y \) for \( x \) and \( y \).)
:::
:::

::: {.solution}
(a) \( (s \circ s)(x, y) = s(x + y, x - y) = \bigl((x + y) + (x - y), (x + y) - (x - y)\bigr) = (2x, 2y) \).

(b) Part (a) suggests halving after applying \( s \). Put
\[
t(u, v) \coloneqq \Bigl(\frac{u + v}{2}, \frac{u - v}{2}\Bigr) .
\]
Then \( t(s(x, y)) = t(x + y, x - y) = (2x/2, 2y/2) = (x, y) \), and
\[
s(t(u, v)) = \Bigl(\frac{u + v}{2} + \frac{u - v}{2}, \frac{u + v}{2} - \frac{u - v}{2}\Bigr) = (u, v) .
\]
Each computation compares two pairs coordinate by coordinate (@def-ordered-pair). All four functions go from \( \nR^2 \) to \( \nR^2 \), so \( t \circ s = \id_{\nR^2} \) and \( s \circ t = \id_{\nR^2} \) by @prp-function-equality.
:::

::: {#exr-functions-and-composition-b3}
[B3: Families and their values]

::: {.enumerate options="label=(\alph*)"}
1. Write the family \( A_n = [-1/n, 1/n] \), \( n \in \nZ_{>0} \), as a function, naming a codomain.
2. Give two different families \( (A_i)_{i \in \nN} \) and \( (B_i)_{i \in \nN} \) of subsets of \( \nN \) with the same set of values \( \{ \emptyset, \nN \} \).
3. Is \( i \mapsto \{i\} \) a function \( \nN \to \powerset{\nN} \)? A function \( \nN \to \nN \)?
:::
:::

::: {.solution}
(a) The function \( \nZ_{>0} \to \powerset{\nR} \), \( n \mapsto [-1/n, 1/n] \). Each value is a subset of \( \nR \), so it lies in \( \powerset{\nR} \).

(b) Let \( A_i = \emptyset \) for even \( i \) and \( A_i = \nN \) for odd \( i \). Every \( i \in \nN \) is even or odd, and not both (@thm-even-or-odd), so each \( i \) receives exactly one value and (Fn1), (Fn2) hold. Let \( B_0 = \emptyset \) and \( B_i = \nN \) for \( i \ge 1 \). Both families have the set of values \( \{ \emptyset, \nN \} \). They differ at the index \( 2 \): \( A_2 = \emptyset \) and \( B_2 = \nN \). So they are different functions (@prp-function-equality) with the same values.

(c) Yes: for each \( i \in \nN \), \( \{i\} \subseteq \nN \), so \( \{i\} \in \powerset{\nN} \). No: \( \{i\} \notin \nN \), since the elements of \( \nN \) are numbers and no number is a set (the working convention of Section 1.2). So (Fn1) fails for the codomain \( \nN \): the only candidate value at \( i \) does not lie in it.
:::

### C. Going deeper

::: {#exr-functions-and-composition-c1}
[C1: Functions equal to their own square]

In this exercise, a function \( f \colon X \to X \) with \( f \circ f = f \) is called **idempotent**.

::: {.enumerate options="label=(\alph*)"}
1. Let \( f \colon X \to X \) be idempotent. Show that \( f(y) = y \) for every \( y \) in the range of \( f \).
2. Show that \( x \mapsto \abs{x} \) on \( \nR \) is idempotent, and that \( x \mapsto -x \) is not.
3. Find all idempotent functions \( \{1, 2\} \to \{1, 2\} \).
:::
:::

::: {.solution}
(a) Let \( y \) be in the range of \( f \): \( y = f(x) \) for some \( x \in X \). Then
\[
f(y) = f(f(x)) = (f \circ f)(x) = f(x) = y .
\]

(b) For every real \( x \), \( \abs{x} \ge 0 \), so \( \bigl\lvert \abs{x} \bigr\rvert = \abs{x} \); the two functions \( x \mapsto \bigl\lvert \abs{x} \bigr\rvert \) and \( x \mapsto \abs{x} \) agree everywhere and are equal by @prp-function-equality. For \( m(x) = -x \): \( m(m(1)) = -(-1) = 1 \), while \( m(1) = -1 \), so \( m \circ m \ne m \).

(c) A function \( \{1, 2\} \to \{1, 2\} \) is determined by its two values (@prp-function-equality), so there are four: the identity, the constant function with value \( 1 \), the constant function with value \( 2 \), and the swap \( \sigma \) with \( \sigma(1) = 2 \), \( \sigma(2) = 1 \). The identity is idempotent by @prp-composition-associative. A constant function \( c \) with value \( a \) gives \( c(c(x)) = c(a) = a = c(x) \). The swap is not: \( \sigma(\sigma(1)) = \sigma(2) = 1 \), and \( \sigma(1) = 2 \). So there are three idempotent functions.
:::

::: {#exr-functions-and-composition-c2}
[C2: Find the error]

"*Claim:* if \( f, g \colon \nR \to \nR \) and \( g \circ f = f \circ g \), then \( f = g \). *Proof:* Let \( x \in \nR \). Then \( g(f(x)) = f(g(x)) \). Cancelling the outer functions on both sides, \( f(x) = g(x) \). So \( f = g \)."

Find the first wrong step, and show that the claim is false.
:::

::: {.solution}
The first two steps are correct: \( g(f(x)) = f(g(x)) \) is the hypothesis \( g \circ f = f \circ g \) at the point \( x \). The wrong step is "cancelling the outer functions". The two sides apply **different** outer functions, \( g \) on the left and \( f \) on the right, and nothing licenses passing from an equation \( g(a) = f(b) \) to \( a = b \).

The claim is false. Let \( f(x) = x + 1 \) and \( g(x) = x + 2 \). Then \( (g \circ f)(x) = (x + 1) + 2 = x + 3 \) and \( (f \circ g)(x) = (x + 2) + 1 = x + 3 \), so \( g \circ f = f \circ g \) by @prp-function-equality. But \( f(0) = 1 \ne 2 = g(0) \), so \( f \ne g \).

**Marking scheme.** (10 points)
- 3: locates the step "cancelling the outer functions" as the first wrong one.
- 3: says why it fails: the outer functions on the two sides are different, so from \( g(a) = f(b) \) one cannot conclude \( a = b \).
- 4: a counterexample with both claims checked: the two composites are equal, and \( f \) and \( g \) differ at a named point.

Fatal errors (0 for the step): blaming the step \( g(f(x)) = f(g(x)) \); a counterexample in which \( f \circ g \ne g \circ f \).
:::

<!-- dependency ledger
def-function (claim): (second-reading fold) x -> x^2 onto [0, infinity) reaches every point of its target, into R does not | forward pointer to exm-square-three-ways (F2.6 §02, cited in a fold); nothing depends on it
def-function (claim): bounded exists-unique, exists! y in Y psi, abbreviates exists! y (y in Y and psi) | notation, by analogy with def-bounded-quantifier (cited); NOTATION bounded-quantifier row
def-function (claim): exists-unique splits into existence (Fn1) and uniqueness (Fn2) | def-unique-existence, prp-unique-existence-use (cited)
def-function (claim): (**) uses substituting equals (=E) | def-rules-equality (cited)
def-function (claim): squares of reals are non-negative; 1/x undefined at 0 | school fact (F1-F2 convention); proved in AN1.1
exm-first-functions (example): (x, y) in X x {c} gives y = c | def-cartesian-product ((*) of F2.1 §04), cited by section
exm-first-functions (example): x in A or x not in A | prp-excluded-middle (cited)
exm-not-a-function (example): no real square is negative; square roots of non-negative reals exist | school fact (F1-F2 convention); proved in AN1.1
exm-not-a-function (example): every rational is p/q with p in Z, q in Z_{>0}; 1/2 = 2/4 | school facts (F1-F2 convention)
exm-not-a-function (example): a non-empty set of positive integers has a least element (the q0 of the repair); a least element is unique | well-ordering, F2.2 (promised; prose pointer; STATUS row "F2.1 §02, §03, F2.6 §01 → F2.2"); uniqueness: two least elements are each <= the other, so equal (order facts, F1-F2 convention; proved in AN1.1)
exm-equal-functions (example): (x + 1)^2 - 2x - 1 = x^2; |x| >= 0 and |x|^2 = x^2; sqrt(x^2) is the non-negative square root | school algebra (F1-F2 convention); uniqueness by thm-squares-order (cited)
prp-function-equality (proof): domain = set of first coordinates of the graph | inline, in the paraphrase of def-function
def-composition (claim): f(x) in Y, so g(f(x)) is defined and in Z | inline, from (**) in def-function's paraphrase
exm-composition-order (example): 2x + 2 != 2x + 1 | arithmetic
exm-composition-order (claim): the Quick check on h with h o g = f: y - 1 recovers x from y = x + 1; 2(x + 1) + 1 = 2x + 3 | school algebra (F1-F2 convention)
prp-empty-function (proof): empty set is a subset of every set | F2.1 §02, prose after prp-empty-set-unique (vacuous implication, cited there)
exm-function-set-small (claim): Y^X has m^n elements for finite sets; subsets of X correspond to functions X -> {0, 1} | F2.3 §01 (prose pointers "the business of Section 4.1", "which Section 4.1 solves"); the correspondence is stated with its two maps, and nothing depends on either
def-function (claim): m + n in N for m, n in N (addition N x N -> N, the example after the definition) | F2.2 (promised; STATUS row "F2.1 §02, §03, F2.6 §01 → F2.2", lem-naturals-arithmetic (b))
exm-not-a-function (claim): well-definedness returns for functions defined on classes | F2.5 (prose pointer "Chapter 5"); nothing depends on it
exm-function-set-small (claim): (the five-string game) there are 32 strings of five symbols 0 or 1; Chapter 4 returns to the game | 2^5 = 32 by listing (the count in general is F2.3 §01's); F2.3 (promised; prose pointer "Chapter 4 comes back to this game"); nothing depends on it
exm-root-and-square (example): sqrt(x^2) = |x| | exm-equal-functions (b) (cited)
exm-root-and-square (example): (sqrt t)^2 = t for t >= 0; sqrt t >= 0 exists | school fact (F1-F2 convention); proved in AN1.1
exr-functions-and-composition-a1 (solution): x^2 + 1 >= 1; no real square is negative; n^2 - n = n(n - 1) | school algebra (F1-F2 convention)
exr-functions-and-composition-b1 (solution): expansions; quadratic formula, discriminant 56 = 4 * 14 | school algebra (F1-F2 convention)
exr-functions-and-composition-b2 (solution): coordinate arithmetic | school algebra (F1-F2 convention)
exr-functions-and-composition-b3 (solution): the elements of N are numbers, not sets | F2.1 §02 working convention ("numbers are not sets"), cited by section
exr-functions-and-composition-c1 (solution): |x| >= 0, so ||x|| = |x| | school fact (F1-F2 convention)
exr-functions-and-composition-c2 (solution): (x + 1) + 2 = x + 3 = (x + 2) + 1 | arithmetic
-->
