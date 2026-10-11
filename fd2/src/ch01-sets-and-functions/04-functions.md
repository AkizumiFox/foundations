# Functions, Composition, Injections and Surjections

Section 6.3 made "the pairs a description picks out" into a set: a relation from \( A \) to \( B \) is a subset of \( A \times B \). Among its examples, the graph of squaring relates each real number to exactly one number, and the unit circle relates \( 0 \) to two numbers and \( 2 \) to none. This section gives the first kind its name, **function**, and builds the rest on it: we restrict functions, use them to make families, sequences and the set \( Y^X \) precise, compose them, and ask the two questions that the rest of the chapter turns on: does a function send different inputs to different outputs, and does it reach every point of its target?

## What is a function?

Everyone has used functions since school, and the everyday definition is "a rule that assigns to each input one output". Look at the word "rule". The rules \( x \mapsto x^2 \) and \( x \mapsto (x + 1)^2 - 2x - 1 \) are different: one squares, the other adds, squares, subtracts, and subtracts again. Yet on every real number they give the same answer, and nobody would call them different functions. Other functions have no rule at all that one could write down. A table of measured temperatures, one per day, assigns to each day one number, and no formula produces it.

So the rule is not what matters. What matters is **which output goes with which input**: the set of input–output pairs. That set is a relation, and Section 6.3 said exactly when two relations are the same, namely when they contain the same pairs. So we forget the rule and keep the pairs. One more piece of data is needed, the set in which the outputs are **declared** to lie; the reason is given after the definition.

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
where, as with the bounded quantifiers of @def-bounded-quantifier, \( \exists! \, y \in Y \ \psi \) abbreviates \( \exists! \, y \, (y \in Y \wedge \psi) \).
:::

The whole definition is the quantifier pattern \( \forall \exists! \). By @def-unique-existence, "\( \exists! \, y \)" is an existence claim and a uniqueness claim, and by @prp-unique-existence-use the uniqueness claim may be stated without reference to the witness; so the condition on the graph is two clauses:

- **(Fn1)** (existence) for every \( x \in X \) there is **at least one** \( y \in Y \) with \( (x, y) \in G \): every input has an output;
- **(Fn2)** (uniqueness) for every \( x \in X \) and all \( y, y' \in Y \), if \( (x, y) \in G \) and \( (x, y') \in G \), then \( y = y' \): no input has two outputs.

In words: the graph is a set of input–output pairs, with inputs from \( X \) and outputs from \( Y \); (Fn1) says no input is left without an output, and (Fn2) says no input is given two. The codomain \( Y \) is where outputs are allowed to lie. It need not consist of outputs: \( x \mapsto x^2 \) can be declared as a function from \( \nR \) to \( \nR \), although no output is negative. The set of outputs that actually occur is the **range** of \( f \),
\[
\{ y \in Y : \exists x \in X \ \ f(x) = y \} ,
\]
which Section 6.6 will call the image of \( X \) and write \( f(X) \). The domain needs no slot of its own in the pair \( (G, Y) \): by (Fn1) every \( x \in X \) occurs as a first coordinate in \( G \), and since \( G \subseteq X \times Y \), nothing else does. So the graph determines the domain.

**The notation \( f(x) \) is well defined.** Writing "**the** \( y \) with \( (x, y) \in f \)" is legitimate only if there is one, and only one. Clause (Fn1) supplies one, and clause (Fn2) says that any two are equal; together they license the article "the". This gives the equivalence that every argument with functions uses:
\[
(x, y) \in f \iff y = f(x) \qquad (x \in X, \ y \in Y). \tag{$\ast\ast$}
\]
For \( (\Leftarrow) \): \( (x, f(x)) \in f \) by the choice of \( f(x) \), and if \( y = f(x) \) then \( (x, y) \in f \) by substituting equals (\( \rulename{=E} \), @def-rules-equality). For \( (\Rightarrow) \): both \( (x, y) \) and \( (x, f(x)) \) lie in \( f \), so \( y = f(x) \) by (Fn2). Two consequences follow at once. Equal inputs give equal outputs: if \( x_1 = x_2 \), then \( f(x_1) = f(x_2) \). And every value lies in the codomain: \( f(x) \in Y \) for every \( x \in X \).

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

(d) The graph is \( \bigl(A \times \{1\}\bigr) \cup \bigl((X \setminus A) \times \{0\}\bigr) \). For (Fn1), let \( x \in X \). By excluded middle (@prp-excluded-middle), \( x \in A \) or \( x \notin A \); in the first case \( (x, 1) \) is in the graph, in the second \( x \in X \setminus A \) and \( (x, 0) \) is. For (Fn2), the two cases cannot both hold, so \( x \) never receives both \( 0 \) and \( 1 \), and each case gives only one pair with first coordinate \( x \). The range is \( \{0, 1\} \) if \( A \) has an element and \( X \setminus A \) has an element; it is \( \{0\} \) if \( A = \emptyset \) and \( X \) has an element, \( \{1\} \) if \( A = X \) and \( X \) has an element, and \( \emptyset \) if \( X = \emptyset \). This is the first function of the chapter whose existence clause needs excluded middle: the definition by cases is a function only because every \( x \) falls into one of the cases.
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

(b) No. Clause (Fn1) holds: every rational number is \( p/q \) for some \( p \in \nZ \) and \( q \in \nZ_{>0} \). But (Fn2) fails, because a rational number has many ways of being written as a fraction. Since \( \tfrac{1}{2} = \tfrac{2}{4} \), both \( (\tfrac12, 1) \) and \( (\tfrac12, 2) \) lie in \( N \), and \( 1 \ne 2 \). The "rule" gives an output that depends on **how the input is written**, not on the input. A function may not do that, since its value is attached to the input itself. This is why definitions of the form "write \( x \) as …, then send it to …" must be checked for **well-definedness**, a check that returns in Chapter 7 for functions defined on classes. Here the repair is to fix the way of writing: let \( q_0 \) be the least \( q \in \nZ_{>0} \) with \( rq \in \nZ \) (such \( q \) exist, by the first sentence, so there is a least one by well-ordering, proved in Chapter 7; a least element is unique), and send \( r \) to \( r q_0 \). This is a function.
:::

**Why this definition.** Each clause has a job, and dropping one lets in the failures of @exm-not-a-function. Without (Fn1), a "function" could be undefined at some inputs, like \( 1/x \) at \( 0 \); then \( f(x) \) would not name anything, and statements "for every \( x \in X \)" about \( f(x) \) would lose their meaning. Without (Fn2), \( f(x) \) would not name **one** thing, and \( f(\tfrac12) \) in part (b) would be both \( 1 \) and \( 2 \). The graph replaces the rule because two rules can describe one function, and sets are compared by their elements.

Why is the codomain part of the data? A relation is a set, so if a function were only its graph, two functions with the same graph would be equal (@def-set-equality), whatever target was declared. The graph of \( x \mapsto x^2 \) as a function \( [0, \infty) \to \nR \) is the same set as its graph as a function \( [0, \infty) \to [0, \infty) \). But these should be different functions, because the second reaches every point of its target and the first does not: this is the property called surjectivity below, and an example later in this section shows it changing with the codomain. Recording the codomain in the pair \( (G, Y) \) keeps the two apart. Many books take the same convention, some without saying so.

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

(b) Equal. Same domain and codomain, and for every real \( x \), \( \sqrt{x^2} = \abs{x} \): the number \( \abs{x} \) is nonnegative and its square is \( x^2 \), and \( \sqrt{x^2} \) is by definition the nonnegative number with square \( x^2 \), which is unique by @thm-squares-order.

(c) Not equal. They have the same domain, the same values, and even the same graph; but their codomains \( \nR \) and \( [0, \infty) \) are different sets (\( -1 \) is in one and not the other), so by @prp-function-equality \( s_1 \ne s_2 \).
:::

**Restriction.** A function can be cut down to a smaller domain. For \( f \colon X \to Y \) and \( A \subseteq X \), the **restriction** of \( f \) to \( A \) is the function
\[
f|_A \colon A \to Y, \qquad f|_A(a) \coloneqq f(a) ,
\]
whose graph is \( G \cap (A \times Y) \): the pairs of \( f \) whose input lies in \( A \). The squaring function \( \nR \to \nR \) restricted to \( [0, \infty) \) is \( s_1 \) of part (c). The bar in \( f|_A \) is one of the uses of a vertical bar that the book's colon-for-set-builder convention keeps free.

## Families, sequences, and the set of all functions

Section 6.2 used families of sets \( (A_i)_{i \in I} \) and described them informally, as "a set \( A_i \) for each index \( i \in I \)". We can now say exactly what a family is, once its members are known to lie in some set. A **family of subsets of \( X \) indexed by \( I \)** is a function \( I \to \powerset{X} \), \( i \mapsto A_i \), with the power set \( \powerset{X} \) as the codomain the definition asks for. More generally, if \( S \) is a set whose elements are sets, a family of members of \( S \) indexed by \( I \) is a function \( I \to S \). A codomain must be named, because there is no set of all sets (@thm-russell). The value of a family at \( i \) is written \( A_i \) rather than \( A(i) \), and the family is written \( (A_i)_{i \in I} \), in parentheses because it is indexed. A family is not the same thing as its set of values \( \{ A_i : i \in I \} \): the family \( (A_i)_{i \in \{1, 2\}} \) with \( A_1 = A_2 = \{0\} \) has two indices and one value.

In the same way, a **sequence** of real numbers \( (a_n)_{n \ge 1} \) is a function \( \nZ_{>0} \to \nR \), \( n \mapsto a_n \), with the value at \( n \) written \( a_n \). The sequence \( (1/n) \) is the function \( n \mapsto 1/n \), and its set of values is \( \{ 1/n : n \ge 1 \} \). Sequences are the main object of Part I.

Finally, all functions from \( X \) to \( Y \) form a set, written
\[
Y^X \coloneqq \{ f \in \powerset{X \times Y} \times \{Y\} : f \text{ is a function from } X \text{ to } Y \} .
\]
It is a set by the working rules of Section 6.1: every function \( X \to Y \) is a pair \( (G, Y) \) with \( G \in \powerset{X \times Y} \), so \( Y^X \) is the subset of \( \powerset{X \times Y} \times \{Y\} \) cut out by the condition of @def-function, and this product is a set by (W2), (W4), and (W5), so \( Y^X \) is a set by specification (W1). The letters are in this order because, for finite sets, \( Y^X \) has \( m^n \) elements when \( Y \) has \( m \) and \( X \) has \( n \), as the next example suggests; counting is Chapter 8's business. The set \( \{0, 1\}^{\nN} \) of all sequences of zeros and ones, indexed from \( 0 \), plays a leading role in Chapter 8.

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

The correspondence at the end of the example, between subsets of \( X \) and functions \( X \to \{0, 1\} \), holds for every set \( X \): send \( f \) to \( \{ x \in X : f(x) = 1 \} \) and \( A \) to \( \ind_A \). So counting the subsets of a finite set and counting the functions from it to \( \{0, 1\} \) are one problem, which Chapter 8 solves.

The empty set gives the degenerate cases, and they are worth settling now, since they are the test cases of many later statements.

::: {#prp-empty-function}
[Functions and the Empty Set]

(a) For every set \( Y \) there is exactly one function from \( \emptyset \) to \( Y \): the pair \( (\emptyset, Y) \), called the **empty function**.

(b) If \( X \) is nonempty (it has an element), there is no function from \( X \) to \( \emptyset \).
:::

::: {.proof}
(a) *Existence.* The empty relation satisfies \( \emptyset \subseteq \emptyset \times Y \), since \( \emptyset \) is a subset of every set (Section 6.1). The condition of @def-function reads "for every \( x \), if \( x \in \emptyset \), then there is exactly one \( y \in Y \) with \( (x, y) \in \emptyset \)". For each \( x \) the hypothesis \( x \in \emptyset \) is false, so the implication holds (@prp-vacuous-implication). So \( (\emptyset, Y) \) is a function from \( \emptyset \) to \( Y \).

*Uniqueness.* Let \( (G, Y) \) be any function from \( \emptyset \) to \( Y \). Its graph satisfies \( G \subseteq \emptyset \times Y = \emptyset \), by the mirror-image \( \emptyset \) law of @prp-product-set-laws. So an element of \( G \) would be an element of \( \emptyset \); \( G \) has no elements, and \( G = \emptyset \) by @prp-empty-set-unique. Hence \( (G, Y) = (\emptyset, Y) \).

(b) Let \( x_0 \in X \), and suppose \( f \colon X \to \emptyset \) were a function. By (Fn1) there would be \( y \in \emptyset \) with \( (x_0, y) \in f \); but \( \emptyset \) has no elements. So there is no such function \( [\rulename{\neg I}] \).
:::

In the notation \( Y^X \): the set \( Y^{\emptyset} \) has exactly one element for every \( Y \), including \( Y = \emptyset \); and \( \emptyset^X = \emptyset \) whenever \( X \) is nonempty. The empty function \( \emptyset \to Y \) returns in Section 6.5 as the witness that a hypothesis there cannot be dropped.

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

Composition can also fail to be defined in one order only. For \( f \colon \{1, 2\} \to \nR \) and \( g \colon \nR \to \nR \), the composite \( g \circ f \colon \{1, 2\} \to \nR \) is defined, and \( f \circ g \) is not: \( g \)'s outputs are real numbers, and \( f \) accepts only \( 1 \) and \( 2 \).

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

::: {.check}
For \( f, g \colon \nR \to \nR \), \( f(x) = x^2 \) and \( g(x) = x - 3 \), compute \( (g \circ f)(2) \) and \( (f \circ g)(2) \).
:::

::: {.solution}
\( (g \circ f)(2) = g(4) = 1 \) and \( (f \circ g)(2) = f(-1) = 1 \). The values agree at this point, but the functions are different: at \( x = 0 \), \( (g \circ f)(0) = -3 \) and \( (f \circ g)(0) = 9 \). Agreement at one point proves nothing about equality; disagreement at one point proves inequality.
:::

## Injective, surjective, bijective

Two questions can be asked of any function \( f \colon X \to Y \), and much of mathematics turns on them. First: can we recover the input from the output, or can two different inputs give the same output? Second: is every point of the codomain an output? The first question is about how \( f \) treats \( X \); the second is about how it covers \( Y \).

### Injective functions

*An injective function never sends two different inputs to the same output.*

::: {#def-injective}
[Injective]

A function \( f \colon X \to Y \) is **injective** (an **injection**, or **one-to-one**) if, **for all** \( x_1, x_2 \in X \), \( f(x_1) = f(x_2) \) implies \( x_1 = x_2 \). In symbols:
\[
\forall x_1 \in X \ \ \forall x_2 \in X \ \ \bigl( f(x_1) = f(x_2) \to x_1 = x_2 \bigr) .
\]
:::

In words: if two inputs give the same output, they were the same input. By @prp-contrapositive, the definition gives the **contrapositive form**
\[
\forall x_1 \in X \ \ \forall x_2 \in X \ \ \bigl( x_1 \ne x_2 \to f(x_1) \ne f(x_2) \bigr) :
\]
different inputs give different outputs. The two forms are equivalent; the way back, from the contrapositive form to the definition, is @prp-contrapositive-converse, which uses \( \rulename{RAA} \). A proof of injectivity usually uses the form of the definition, because an equation \( f(x_1) = f(x_2) \) is something to compute with, while an inequation \( x_1 \ne x_2 \) is not.

The negation is found by the laws of Chapter 4 for negating bounded quantifiers and implications: "\( f \) is **not** injective" is
\[
\exists x_1 \in X \ \ \exists x_2 \in X \ \ \bigl( f(x_1) = f(x_2) \wedge x_1 \ne x_2 \bigr) .
\]
So a failure of injectivity is shown by **two witnesses**: two different inputs with the same output.

### Surjective functions

*A surjective function reaches every point of its codomain.*

::: {#def-surjective}
[Surjective]

A function \( f \colon X \to Y \) is **surjective** (a **surjection**, or **onto**) if, **for every** \( y \in Y \), **there exists** \( x \in X \) with \( f(x) = y \). In symbols:
\[
\forall y \in Y \ \ \exists x \in X \ \ f(x) = y .
\]
:::

In words: every point of the codomain is an output; equivalently, the range of \( f \) is all of \( Y \). An \( x \) with \( f(x) = y \) is called a **preimage** of \( y \). The definition does not ask for the preimage to be unique. Negating as before, "\( f \) is **not** surjective" is
\[
\exists y \in Y \ \ \forall x \in X \ \ f(x) \ne y ,
\]
so a failure of surjectivity is shown by **one witness**: a point of the codomain that no input reaches.

Surjectivity depends on the codomain, which is why @def-function records it: \( s_1 \) and \( s_2 \) of @exm-equal-functions have the same graph, and we shall see that \( s_2 \) is surjective and \( s_1 \) is not.

::: {.warning}
Surjectivity cannot be checked by trying some \( y \). The function \( f \colon \nR \to \nR \), \( f(x) = x^2 + x \), reaches \( 0 = f(0) \), \( 2 = f(1) \), \( 6 = f(2) \), and \( 12 = f(3) \), and a reader who tries these may believe it reaches everything. It does not reach \( -1 \): \( x^2 + x = -1 \) would mean \( x^2 + x + 1 = 0 \), but \( x^2 + x + 1 = (x + \tfrac12)^2 + \tfrac34 > 0 \) for every real \( x \). Concluding "for every \( y \)" from a few instances is entry (N1) of the catalogue in Chapter 5.
:::

### Bijective functions

::: {#def-bijective}
[Bijective]

A function is **bijective** (a **bijection**) if it is both injective and surjective.
:::

A bijection is a function in which every point of the codomain is reached **exactly once**: for every \( y \in Y \) there is exactly one \( x \in X \) with \( f(x) = y \). This is the \( \exists! \) of @def-function again, now read from the codomain side, and its two halves are the two properties. Existence of such an \( x \), for every \( y \), is surjectivity. Uniqueness is injectivity: if \( f(x_1) = y = f(x_2) \), injectivity gives \( x_1 = x_2 \); and conversely, if every \( y \) has at most one preimage, then \( f(x_1) = f(x_2) \) makes \( x_1 \) and \( x_2 \) two preimages of the same point \( y \coloneqq f(x_1) \), so \( x_1 = x_2 \).

### Worked examples

Proofs of these properties have a fixed shape, read off the definitions.

- To prove \( f \) **injective**: "Let \( x_1, x_2 \in X \) with \( f(x_1) = f(x_2) \)." Compute until you reach \( x_1 = x_2 \).
- To prove \( f \) **surjective**: "Let \( y \in Y \)." Then produce an \( x \), **say what it is**, check that it lies in \( X \), and check that \( f(x) = y \). The \( x \) is usually found by solving \( f(x) = y \) for \( x \) on scrap paper; the proof then states the solution first and checks it, as every existence proof does.
- To prove \( f \) **not injective**: name \( x_1 \ne x_2 \) with \( f(x_1) = f(x_2) \). **Not surjective**: name \( y \in Y \) and show that \( f(x) = y \) has no solution \( x \in X \).

::: {#exm-injective-surjective-first}
[Deciding injective and surjective]

For each function below, decide with proof whether it is injective and whether it is surjective.

(a) \( f \colon \nR \to \nR \), \( f(x) = 3x - 5 \).

(b) \( g \colon \nZ \to \nZ \), \( g(n) = 3n \).

(c) \( h \colon \{1, 2, 3\} \to \{a, b\} \), with \( h(1) = a \), \( h(2) = b \), \( h(3) = a \).

(d) \( k \colon \{1, 2\} \to \{a, b, c\} \), with \( k(1) = a \), \( k(2) = c \).
:::

::: {.solution}
(a) *Injective.* Let \( x_1, x_2 \in \nR \) with \( 3x_1 - 5 = 3x_2 - 5 \). Adding \( 5 \) and dividing by \( 3 \) gives \( x_1 = x_2 \).

*Surjective.* On scrap paper, \( 3x - 5 = y \) gives \( x = (y + 5)/3 \). Now the proof: let \( y \in \nR \), and put \( x \coloneqq (y + 5)/3 \). Then \( x \in \nR \), and \( f(x) = 3 \cdot \frac{y + 5}{3} - 5 = y \). So \( f \) is bijective.

(b) *Injective.* Let \( n_1, n_2 \in \nZ \) with \( 3n_1 = 3n_2 \). Dividing by \( 3 \) gives \( n_1 = n_2 \).

*Not surjective.* The witness is \( 1 \in \nZ \). If \( n \ge 1 \), then \( 3n \ge 3 \); if \( n \le 0 \), then \( 3n \le 0 \). So \( 3n \ne 1 \) for every integer \( n \), and \( 1 \) has no preimage. (Solving \( 3n = 1 \) gives \( n = \tfrac13 \), which is not in the domain \( \nZ \): the same formula on \( \nQ \) would be surjective.)

(c) *Not injective:* \( h(1) = a = h(3) \) and \( 1 \ne 3 \). *Surjective:* the codomain has two points, and \( a = h(1) \), \( b = h(2) \). For a finite codomain, checking every point **is** a proof: the instances are all the cases.

(d) *Injective:* the two inputs have the different outputs \( a \ne c \), and there are no other pairs of different inputs to check. *Not surjective:* \( b \) is not an output, since the only outputs are \( k(1) = a \) and \( k(2) = c \).
:::

Parts (c) and (d) show two more things. A function from a three-element set to a two-element set cannot be injective, and one from a two-element set to a three-element set cannot be surjective: there are too many inputs in the first case and too few in the second. Chapter 8 proves facts of this kind in general, starting from the pigeonhole principle. And the finite pictures are worth drawing: two columns of dots, with an arrow from each input to its output. Injective means no dot on the right receives two arrows; surjective means every dot on the right receives at least one.

The key example of the section is one formula read as three different functions.

::: {#exm-square-three-ways}
[Squaring, three ways]

For each of the three functions, settle both questions: injective or not, surjective or not.

(a) \( q_1 \colon \nR \to \nR \), \( q_1(x) = x^2 \).

(b) \( q_2 \colon [0, \infty) \to \nR \), \( q_2(x) = x^2 \).

(c) \( q_3 \colon [0, \infty) \to [0, \infty) \), \( q_3(x) = x^2 \).
:::

::: {.solution}
(a) *Not injective:* \( q_1(1) = 1 = q_1(-1) \) and \( 1 \ne -1 \). *Not surjective:* the witness is \( -1 \in \nR \), since \( x^2 \ge 0 > -1 \) for every real \( x \). So \( q_1 \) is neither.

(b) *Injective.* Let \( x_1, x_2 \ge 0 \) with \( x_1^2 = x_2^2 \). Then \( x_1^2 \le x_2^2 \), so \( x_1 \le x_2 \) by @thm-squares-order, which applies since both numbers are nonnegative; and likewise \( x_2 \le x_1 \). Hence \( x_1 = x_2 \). *Not surjective:* the witness \( -1 \) still works, for the same reason.

(c) *Injective*, by the same proof as in (b): injectivity concerns only the domain and the values, and these are the same as for \( q_2 \). *Surjective.* Let \( y \in [0, \infty) \). A nonnegative real number has a nonnegative square root, so put \( x \coloneqq \sqrt{y} \). Then \( x \in [0, \infty) \) and \( q_3(x) = (\sqrt{y})^2 = y \). So \( q_3 \) is bijective.

The same rule gives three different functions. Shrinking the domain from \( \nR \) to \( [0, \infty) \) removed the two witnesses \( \pm 1 \) against injectivity. Shrinking the codomain to \( [0, \infty) \) removed the witness \( -1 \) against surjectivity. The graphs of \( q_2 \) and \( q_3 \) are the same set; only the declared codomain differs, and surjectivity changes with it.
:::

::: {.warning}
Injectivity is not the defining property of a function read backwards. Every function satisfies "if \( x_1 = x_2 \), then \( f(x_1) = f(x_2) \)": equal inputs give equal outputs, which is part of \( f(x) \) being well defined. Injectivity is the **converse**, "if \( f(x_1) = f(x_2) \), then \( x_1 = x_2 \)". A "proof" of injectivity that starts from \( x_1 = x_2 \) and reaches \( f(x_1) = f(x_2) \) has proved the wrong implication, entry (N5) of Chapter 5's catalogue, and it "proves" \( q_1 \) injective, which is false.
:::

::: {.check}
Is \( n \mapsto n + 1 \) surjective as a function \( \nN \to \nN \)? As a function \( \nZ \to \nZ \)?
:::

::: {.solution}
On \( \nN \): no. The witness is \( 0 \), since \( n + 1 \ge 1 \) for every \( n \in \nN \), so \( n + 1 = 0 \) has no solution in \( \nN \). On \( \nZ \): yes. For \( m \in \nZ \), the integer \( m - 1 \) satisfies \( (m - 1) + 1 = m \). Both functions are injective, since \( n_1 + 1 = n_2 + 1 \) gives \( n_1 = n_2 \).
:::

## Composites of injections and surjections

Both properties survive composition. This is the first theorem about functions whose proof uses the definitions and nothing else, and it shows the two proof shapes of the last subsection working together.

::: {#thm-composition-injective-surjective}
[Composites of Injections and Surjections]

Let \( f \colon X \to Y \) and \( g \colon Y \to Z \) be functions.

(a) If \( f \) and \( g \) are injective, then \( g \circ f \) is injective.

(b) If \( f \) and \( g \) are surjective, then \( g \circ f \) is surjective.

(c) If \( f \) and \( g \) are bijective, then \( g \circ f \) is bijective.
:::

::: {.idea}
For (a), start from equal outputs of \( g \circ f \). They are equal outputs of \( g \), at the points \( f(x_1) \) and \( f(x_2) \); peel off \( g \) by its injectivity, then \( f \) by its. For (b), work backwards along the chain \( X \to Y \to Z \): to reach \( z \in Z \), first find a point of \( Y \) that \( g \) sends to \( z \), then a point of \( X \) that \( f \) sends there. Part (c) is (a) and (b) together.
:::

::: {.proof}
(a) Let \( x_1, x_2 \in X \) with \( (g \circ f)(x_1) = (g \circ f)(x_2) \), that is, \( g(f(x_1)) = g(f(x_2)) \) by @def-composition. The points \( f(x_1) \) and \( f(x_2) \) lie in \( Y \), and \( g \) is injective, so \( f(x_1) = f(x_2) \) [\( \rulename{\forall E} \), \( \rulename{{\to}E} \): injectivity of \( g \) at \( f(x_1), f(x_2) \)]. Since \( f \) is injective, \( x_1 = x_2 \) [\( \rulename{\forall E} \), \( \rulename{{\to}E} \): injectivity of \( f \) at \( x_1, x_2 \)]. So \( g \circ f \) is injective.

(b) Let \( z \in Z \). Since \( g \) is surjective, there is \( y \in Y \) with \( g(y) = z \) [\( \rulename{\exists E} \): the name \( y \) is fresh]. Since \( f \) is surjective, there is \( x \in X \) with \( f(x) = y \) [\( \rulename{\exists E} \): \( x \) is fresh]. Then
\[
(g \circ f)(x) = g(f(x)) = g(y) = z ,
\]
so \( z \) has the preimage \( x \) under \( g \circ f \) [\( \rulename{\exists I} \), witness \( x \)]. Since \( z \in Z \) was arbitrary, \( g \circ f \) is surjective.

(c) If \( f \) and \( g \) are bijective, they are injective and surjective, so \( g \circ f \) is injective by (a) and surjective by (b), that is, bijective.
:::

Part (a) is short enough to see whole at level 0 of Chapter 5 (Section 5.3), a full derivation. Here is its derivation, with the quantifiers bounded and handled by the bounded rules (@prp-bounded-quantifier-rules), and \( (g \circ f)(u) \) already unwound to \( g(f(u)) \) by @def-composition. Premises 1 and 2 are the injectivity of \( f \) and of \( g \); premise 3 says that \( f \) maps \( X \) into \( Y \), which the prose used in the clause "the points \( f(x_1) \) and \( f(x_2) \) lie in \( Y \)".

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall u \in X\, \forall v \in X\, (f(u) = f(v) \to u = v)}
  \hypo {2} {\forall u \in Y\, \forall v \in Y\, (g(u) = g(v) \to u = v)}
  \hypo {3} {\forall u \in X\, f(u) \in Y}
  \open[x_1]
  \hypo {4} {x_1 \in X}
  \open[x_2]
  \hypo {5} {x_2 \in X}
  \open
  \hypo {6} {g(f(x_1)) = g(f(x_2))}
  \have {7} {f(x_1) \in Y} \Ae{3,4}
  \have {8} {f(x_2) \in Y} \Ae{3,5}
  \have {9} {\forall v \in Y\, (g(f(x_1)) = g(v) \to f(x_1) = v)} \Ae{2,7}
  \have {10} {g(f(x_1)) = g(f(x_2)) \to f(x_1) = f(x_2)} \Ae{9,8}
  \have {11} {f(x_1) = f(x_2)} \ie{10,6}
  \have {12} {\forall v \in X\, (f(x_1) = f(v) \to x_1 = v)} \Ae{1,4}
  \have {13} {f(x_1) = f(x_2) \to x_1 = x_2} \Ae{12,5}
  \have {14} {x_1 = x_2} \ie{13,11}
  \close
  \have {15} {g(f(x_1)) = g(f(x_2)) \to x_1 = x_2} \ii{6-14}
  \close
  \have {16} {\forall v \in X\, (g(f(x_1)) = g(f(v)) \to x_1 = v)} \Ai{5-15}
  \close
  \have {17} {\forall u \in X\, \forall v \in X\, (g(f(u)) = g(f(v)) \to u = v)} \Ai{4-16}
\end{nd}$
\end{center}
```

Compare it with the prose of (a). "Let \( x_1, x_2 \in X \)" opens the two flagged boxes of lines 4 and 5, and "with \( g(f(x_1)) = g(f(x_2)) \)" is the assumption of line 6. The first tagged sentence is lines 7–11, and the second is lines 12–14. The closing "so \( g \circ f \) is injective" stands for lines 15–17, the closing lines of \( \rulename{{\to}I} \) and of the two \( \rulename{\forall I} \)'s; by the convention of Chapter 5 on silent steps, the prose may state their result without naming them. The two tags in the prose mark the only steps where a hypothesis is used, and that is what the proof is about.

**Each hypothesis is needed.** In (a), dropping the injectivity of \( g \) breaks the conclusion: with \( f = \id_{\nR} \) and \( g = q_1 \), squaring on \( \nR \), the composite \( g \circ f = q_1 \) is not injective, although \( f \) is. Dropping the injectivity of \( f \) instead, with \( f = q_1 \) and \( g = \id_{\nR} \), gives the same composite. In (b), with \( f = \id_{\nR} \) and \( g = q_1 \), the composite \( q_1 \) is not surjective, although \( f \) is; with \( f = q_1 \) and \( g = \id_{\nR} \), again \( g \circ f = q_1 \) is not surjective, although \( g \) is.

The converses are more interesting, and they are the exercises of this section. An injective composite \( g \circ f \) forces \( f \) to be injective and says nothing of the kind about \( g \) (exit check C1). A surjective composite forces \( g \) to be surjective, and \( f \) may miss points (B2). Section 6.5 builds on these facts: a function \( f \) with a function \( g \) such that \( g \circ f = \id_X \) is forced to be injective.

## Exercises

### A. Check your understanding

::: {#exr-functions-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define "\( f \colon X \to Y \) is injective" in symbols, and write its negation in symbols.
2. Is the empty function \( \emptyset \to \{1\} \) injective? Is it surjective? Justify your answers.
3. Which of these relations on \( \{1, 2, 3\} \) are graphs of functions \( \{1, 2, 3\} \to \{1, 2, 3\} \)? For each that is not, name the clause of the definition that fails.
   \( R_1 = \{ (1, 2), (2, 2), (3, 1) \} \), \( R_2 = \{ (1, 1), (2, 3) \} \), \( R_3 = \{ (1, 1), (1, 2), (2, 2), (3, 3) \} \).
4. How many functions \( \{1, 2\} \to \{a, b, c\} \) are there, and how many of them are injective? Answer by listing.
:::
:::

::: {.solution}
(a) \( f \) is injective: \( \forall x_1 \in X \ \forall x_2 \in X \ \bigl( f(x_1) = f(x_2) \to x_1 = x_2 \bigr) \) (@def-injective). Its negation: \( \exists x_1 \in X \ \exists x_2 \in X \ \bigl( f(x_1) = f(x_2) \wedge x_1 \ne x_2 \bigr) \). The bounds stay as they are, and the negated implication becomes "hypothesis and not conclusion", by the negation laws of Chapter 4.

(b) Injective: yes. The condition "for all \( x_1, x_2 \in \emptyset \), …" holds vacuously, since there are no \( x_1 \in \emptyset \) (@prp-vacuous-implication). Surjective: no. The witness is \( 1 \): there is no \( x \in \emptyset \) at all, so none with value \( 1 \).

(c) \( R_1 \) is a function (\( 1 \mapsto 2 \), \( 2 \mapsto 2 \), \( 3 \mapsto 1 \)). \( R_2 \) is not: clause (Fn1) fails at \( 3 \), which has no output. \( R_3 \) is not: clause (Fn2) fails at \( 1 \), which has the two outputs \( 1 \) and \( 2 \).

(d) A function \( f \colon \{1, 2\} \to \{a, b, c\} \) is determined by the pair of values \( (f(1), f(2)) \) (@prp-function-equality), and each value can be any of the three letters. Listing the pairs:
\[
\begin{aligned}
&(a, a), \ (a, b), \ (a, c), \\
&(b, a), \ (b, b), \ (b, c), \\
&(c, a), \ (c, b), \ (c, c).
\end{aligned}
\]
There are \( 9 \) functions. A function on \( \{1, 2\} \) is injective exactly when \( f(1) \ne f(2) \), since \( 1 \) and \( 2 \) are the only two different inputs. Removing the three pairs with equal entries, on the diagonal of the list, leaves \( 6 \) injective functions.
:::

### B. Practice

::: {#exr-functions-b1}
[B1: Five functions]

Determine which of the following are injective, which are surjective, and which are not functions at all. Justify your answers.

::: {.enumerate options="label=(\alph*)"}
1. \( \nZ \to \nZ \), \( n \mapsto 2n \).
2. \( \nN \times \nN \to \nN \), \( (m, n) \mapsto m + n \).
3. \( \nR \to \nR \), \( x \mapsto x^3 \).
4. \( \nR \to (-1, 1) \), \( x \mapsto x / (1 + \abs{x}) \).
5. \( \nZ_{>0} \to \nZ_{>0} \), \( n \mapsto n + (-1)^n \).
:::
:::

::: {.solution}
(a) *Injective:* \( 2n_1 = 2n_2 \) gives \( n_1 = n_2 \). *Not surjective:* the witness is \( 1 \), which is odd, while every \( 2n \) is even, and no integer is both even and odd.

(b) *Not injective:* \( (1, 2) \ne (2, 1) \) (@def-ordered-pair), and both are sent to \( 3 \). *Surjective:* for \( k \in \nN \), the pair \( (0, k) \) lies in \( \nN \times \nN \) and is sent to \( k \).

(c) *Injective.* Let \( x_1^3 = x_2^3 \). Then
\[
0 = x_1^3 - x_2^3 = (x_1 - x_2)\bigl(x_1^2 + x_1 x_2 + x_2^2\bigr),
\qquad
x_1^2 + x_1 x_2 + x_2^2 = \bigl(x_1 + \tfrac12 x_2\bigr)^2 + \tfrac34 x_2^2 .
\]
If \( x_1 \ne x_2 \), the second factor is positive: if \( x_2 \ne 0 \), then \( \tfrac34 x_2^2 > 0 \); if \( x_2 = 0 \), it equals \( x_1^2 > 0 \), because \( x_1 \ne 0 \). Then the product is nonzero, a contradiction. So \( x_1 = x_2 \). *Surjective:* for \( y \in \nR \), every real number has a real cube root, and \( x \coloneqq \sqrt[3]{y} \) satisfies \( x^3 = y \). So the function is bijective.

(d) *A function:* for every \( x \), \( 1 + \abs{x} > 0 \), and \( \abs{x / (1 + \abs{x})} = \abs{x}/(1 + \abs{x}) < 1 \), so the value lies in \( (-1, 1) \). *Injective.* Suppose \( y = x/(1 + \abs{x}) \); we solve for \( x \). Taking absolute values, \( \abs{y} = \abs{x}/(1 + \abs{x}) \), so \( \abs{y}(1 + \abs{x}) = \abs{x} \), that is, \( \abs{x}(1 - \abs{y}) = \abs{y} \); since \( \abs{y} < 1 \) (shown above), \( 1 - \abs{y} > 0 \), and \( \abs{x} = \abs{y}/(1 - \abs{y}) \), and then \( 1 + \abs{x} = 1/(1 - \abs{y}) \). Hence
\[
x = y\,(1 + \abs{x}) = \frac{y}{1 - \abs{y}} .
\]
So \( x \) is determined by \( y \): two inputs with the same output \( y \) are both equal to \( y/(1 - \abs{y}) \), hence equal. *Surjective.* Let \( y \in (-1, 1) \) and put \( x \coloneqq y/(1 - \abs{y}) \), a real number since \( 1 - \abs{y} > 0 \). Then \( \abs{x} = \abs{y}/(1 - \abs{y}) \), so \( 1 + \abs{x} = 1/(1 - \abs{y}) \), and
\[
\frac{x}{1 + \abs{x}} = \frac{y}{1 - \abs{y}} \cdot (1 - \abs{y}) = y .
\]
So the function is bijective. (For example, \( x = 1 \mapsto \tfrac12 \) and \( y = \tfrac12 \) comes back to \( x = \tfrac{1/2}{1/2} = 1 \).)

(e) *Not a function* \( \nZ_{>0} \to \nZ_{>0} \): at \( n = 1 \) the formula gives \( 1 + (-1) = 0 \), and \( 0 \notin \nZ_{>0} \), so (Fn1) fails at \( 1 \). This is the planted failure: the question whether it is injective or surjective does not arise. (On \( \nN = \{0, 1, 2, \dots\} \) the same formula is a function, and a bijection: it swaps \( 0 \leftrightarrow 1 \), \( 2 \leftrightarrow 3 \), and so on.)
:::

::: {#exr-functions-b2}
[B2: Put the proof in order]

Let \( f \colon X \to Y \) and \( g \colon Y \to Z \) be functions. The following lines contain a proof that **if \( g \circ f \) is surjective, then \( g \) is surjective**, shuffled, together with two lines that do not belong. Write the six correct lines in an order that makes a proof, and say why each of the other two lines fails.

(i) Then \( g(y) = g(f(x)) = (g \circ f)(x) = z \), by @def-composition.

(ii) Let \( y \in Y \).

(iii) Since \( g \circ f \) is surjective, there is \( x \in X \) with \( (g \circ f)(x) = z \).

(iv) Since \( z \) was arbitrary, \( g \) is surjective.

(v) Let \( y \coloneqq f(x) \), an element of \( Y \).

(vi) Since \( f \) is surjective, \( y = f(x) \) for some \( x \in X \).

(vii) Let \( z \in Z \).

(viii) So \( z \) has a preimage under \( g \), namely \( y \).
:::

::: {.solution}
The order is (vii), (iii), (v), (i), (viii), (iv):

> Let \( z \in Z \). Since \( g \circ f \) is surjective, there is \( x \in X \) with \( (g \circ f)(x) = z \). Let \( y \coloneqq f(x) \), an element of \( Y \). Then \( g(y) = g(f(x)) = (g \circ f)(x) = z \), by @def-composition. So \( z \) has a preimage under \( g \), namely \( y \). Since \( z \) was arbitrary, \( g \) is surjective.

No other order is admissible. Each line uses the one before it: (iii) needs the \( z \) of (vii); (v) needs the \( x \) of (iii); (i) needs the \( y \) of (v); (viii) is the \( \rulename{\exists I} \) that (i) makes possible; and (iv) closes the \( \rulename{\forall I} \) opened by (vii).

The distractor (ii) opens with an arbitrary element of the wrong set. The goal "\( g \) is surjective" is \( \forall z \in Z \ \exists y \in Y \ g(y) = z \), so the proof must take an arbitrary \( z \in Z \); the \( y \) is the witness to be found, not something given. The distractor (vi) uses a hypothesis the statement does not have: nothing says \( f \) is surjective, and the claim holds without it. For example, with \( f \colon \{1\} \to \{1, 2\} \), \( f(1) = 1 \), and \( g \colon \{1, 2\} \to \{1\} \) constant, \( g \circ f \) and \( g \) are surjective and \( f \) is not.
:::

::: {#exr-functions-b3}
[B3: Examples on the natural numbers]

Give an example of a function \( \nN \to \nN \) that is surjective and not injective, and one that is injective and not surjective. Check each property.
:::

::: {.solution}
*Surjective, not injective.* Let \( s(0) \coloneqq 0 \) and \( s(n) \coloneqq n - 1 \) for \( n \ge 1 \); for \( n \ge 1 \), \( n - 1 \in \nN \), so \( s \colon \nN \to \nN \) is a function. It is surjective: for \( m \in \nN \), \( m + 1 \ge 1 \), so \( s(m + 1) = m \). It is not injective: \( s(0) = 0 = s(1) \) and \( 0 \ne 1 \).

*Injective, not surjective.* Let \( t(n) \coloneqq n + 1 \). It is injective: \( n_1 + 1 = n_2 + 1 \) gives \( n_1 = n_2 \). It is not surjective: \( 0 \) is not an output, since \( n + 1 \ge 1 \).

Many other answers are correct. An answer to the first part must have: every value in \( \nN \) (so it is a function into \( \nN \)); at least one value taken at two different inputs, with the two inputs named; and every \( m \in \nN \) reached, with a preimage given as a formula in \( m \), since checking some \( m \) is not enough. An answer to the second part must have: values in \( \nN \); a proof that equal outputs come from equal inputs; and one named natural number that is never reached, with the reason.
:::

### C. Going deeper

::: {#exr-functions-c1}
[C1: Exit check: composites]

Let \( f \colon X \to Y \) and \( g \colon Y \to Z \) be functions.

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( g \circ f \) is injective, then \( f \) is injective.
2. Give an example in which \( g \circ f \) is injective and \( g \) is not injective, and check both claims.
:::
:::

::: {.solution}
(a) Suppose \( g \circ f \) is injective. Let \( x_1, x_2 \in X \) with \( f(x_1) = f(x_2) \); we must show \( x_1 = x_2 \). Applying \( g \) to both sides gives \( g(f(x_1)) = g(f(x_2)) \), because a function gives equal outputs at equal inputs. By @def-composition, this says \( (g \circ f)(x_1) = (g \circ f)(x_2) \). Since \( g \circ f \) is injective, \( x_1 = x_2 \). So \( f \) is injective.

(b) Let \( X = \{1\} \), \( Y = \{1, 2\} \), \( Z = \{1\} \); let \( f(1) = 1 \), and let \( g \colon \{1, 2\} \to \{1\} \) be the constant function \( g(1) = g(2) = 1 \). Then \( g \circ f \colon \{1\} \to \{1\} \) is injective, because its domain has only one element: if \( x_1, x_2 \in \{1\} \), then \( x_1 = 1 = x_2 \). And \( g \) is not injective: \( g(1) = g(2) \) with \( 1 \ne 2 \).

**Marking scheme.** (10 points)
- 2: fixes arbitrary \( x_1, x_2 \in X \) with \( f(x_1) = f(x_2) \) and states the goal \( x_1 = x_2 \).
- 2: applies \( g \) to both sides, with the reason that a function gives equal outputs at equal inputs.
- 3: rewrites the result as an equation of values of \( g \circ f \) and invokes the injectivity of \( g \circ f \).
- 3: an example with explicit sets and functions, and both claims checked: \( g \circ f \) injective, and two different points with the same value under \( g \).

Fatal errors (0 for the step): assuming \( g \) is injective; starting from \( x_1 = x_2 \) and deriving \( f(x_1) = f(x_2) \) (the converse, entry (N5) of Chapter 5's catalogue); an example in which \( g \circ f \) is not defined because the codomain of \( f \) is not the domain of \( g \).
A proof by contrapositive (from \( x_1 \ne x_2 \), \( g \circ f \) injective gives \( g(f(x_1)) \ne g(f(x_2)) \), hence \( f(x_1) \ne f(x_2) \), since equal values of \( f \) would give equal values of \( g \)) earns full marks: 2 points for fixing \( x_1 \ne x_2 \) and the goal, 3 for the use of the injectivity of \( g \circ f \), and 2 for the step from \( g(f(x_1)) \ne g(f(x_2)) \) to \( f(x_1) \ne f(x_2) \).
:::

::: {#exr-functions-c2}
[C2: When the composite is a bijection]

Let \( f \colon X \to Y \) and \( g \colon Y \to Z \) be functions.

::: {.enumerate options="label=(\alph*)"}
1. Deduce from @exr-functions-c1 and @exr-functions-b2 that if \( g \circ f \) is bijective, then \( f \) is injective and \( g \) is surjective.
2. Give an example in which \( g \circ f \) is bijective and neither \( f \) nor \( g \) is bijective.
:::
:::

::: {.solution}
(a) Suppose \( g \circ f \) is bijective. Then \( g \circ f \) is injective, so \( f \) is injective by part (a) of @exr-functions-c1. And \( g \circ f \) is surjective, so \( g \) is surjective by the proof put in order in @exr-functions-b2.

(b) Take the functions of @exr-functions-c1 (b): \( f \colon \{1\} \to \{1, 2\} \), \( f(1) = 1 \), and \( g \colon \{1, 2\} \to \{1\} \), \( g(1) = g(2) = 1 \). Then \( g \circ f \colon \{1\} \to \{1\} \) sends \( 1 \) to \( 1 \), so \( g \circ f = \id_{\{1\}} \) by @prp-function-equality, which is bijective. But \( f \) is not surjective, since \( 2 \) is not an output; and \( g \) is not injective, since \( g(1) = g(2) \). So neither is bijective. Part (a) is sharp: it gives exactly the half of each property that survives, and this example shows that the other halves can fail together.
:::

<!-- dependency ledger
def-function (claim): bounded exists-unique, exists! y in Y psi, abbreviates exists! y (y in Y and psi) | notation, by analogy with def-bounded-quantifier (cited); NOTATION bounded-quantifier row
def-function (claim): exists-unique splits into existence (Fn1) and uniqueness (Fn2) | def-unique-existence, prp-unique-existence-use (cited)
def-function (claim): (**) uses substituting equals (=E) | def-rules-equality (cited)
def-function (claim): squares of reals are non-negative; 1/x undefined at 0 | school fact (Part 0 convention); proved in Ch 11
exm-first-functions (example): (x, y) in X x {c} gives y = c | def-cartesian-product ((*) of Section 6.3), cited by section
exm-first-functions (example): x in A or x not in A | prp-excluded-middle (cited)
exm-not-a-function (example): no real square is negative; square roots of non-negative reals exist | school fact (Part 0 convention); proved in Ch 11
exm-not-a-function (example): every rational is p/q with p in Z, q in Z_{>0}; 1/2 = 2/4 | school facts (Part 0 convention)
exm-not-a-function (example): a non-empty set of positive integers has a least element (the q0 of the repair); a least element is unique | well-ordering, ch07 (promised; prose pointer; STATUS row "Ch 6 §01, §02, §03, §04 → Ch 7"); uniqueness: two least elements are each <= the other, so equal (order facts, Part 0 convention; proved in Ch 11)
exm-equal-functions (example): (x + 1)^2 - 2x - 1 = x^2; |x| >= 0 and |x|^2 = x^2; sqrt(x^2) is the non-negative square root | school algebra (Part 0 convention); uniqueness by thm-squares-order (cited)
prp-function-equality (proof): domain = set of first coordinates of the graph | inline, in the paraphrase of def-function
def-composition (claim): f(x) in Y, so g(f(x)) is defined and in Z | inline, from (**) in def-function's paraphrase
exm-composition-order (example): 2x + 2 != 2x + 1 | arithmetic
prp-empty-function (proof): empty set is a subset of every set | Section 6.1, prose after prp-empty-set-unique (vacuous implication, cited there)
def-surjective (claim): (the warning after it) x^2 + x + 1 = (x + 1/2)^2 + 3/4 > 0; values 0, 2, 6, 12 | school algebra (Part 0 convention); computation inline
def-injective (claim): negation of bounded quantifiers and of an implication | ch04 (promised): prp-bounded-quantifier-negation, prp-negated-implication, prose pointer
exm-injective-surjective-first (example): dividing by 3; n >= 1 gives 3n >= 3, n <= 0 gives 3n <= 0 | school algebra and order facts (Part 0 convention); proved in Ch 11 (order) and Ch 7 (integers)
exm-injective-surjective-first (claim): a function from a 3-element set to a 2-element set is not injective, etc. | ch08 (prose pointer, pigeonhole); only the two specific cases (c), (d) are proved, by listing; nothing depends on the general claim
exm-function-set-small (claim): Y^X has m^n elements for finite sets; subsets of X correspond to functions X -> {0, 1} | ch08 (prose pointer; the count is Ch 8's exercise on B^A); the correspondence is stated with its two maps, and nothing depends on either
exm-square-three-ways (example): x^2 >= 0 > -1; existence of sqrt(y) for y >= 0 | school fact (Part 0 convention); proved in Ch 11
thm-composition-injective-surjective (proof): f(x1), f(x2) in Y | (**) in def-function's paraphrase (every value lies in the codomain)
thm-composition-injective-surjective (proof): forall-E, exists-E, exists-I, forall-I in the prose tags | ch04 (promised): quantifier rules (Sections 4.3-4.6), prose pointer; the bounded forms in the derivation are prp-bounded-quantifier-rules (cited)
thm-composition-injective-surjective (claim): level 0 = full derivation | ch05 (promised): def-levels-of-proof (prose pointer, Section 5.3)
thm-composition-injective-surjective (claim): closing lines of ->I and forall-I may be silent | ch05 (promised): def-silent-steps, prose pointer
exr-functions-b1 (solution): parity (1 is odd, 2n even, not both) | school fact as in Ch 1-2; ch07 (promised; STATUS row "every integer is even or odd, and not both")
exr-functions-b1 (solution): x1^3 - x2^3 factorization; real cube roots exist; |x| algebra for x/(1+|x|) | school algebra (Part 0 convention); cube roots proved in Ch 11 (thm-nth-root with a sign change)
exr-functions-b1 (solution): 0 in N and 0 + k = k | school arithmetic of N; ch07 (promised; STATUS row "ℕ closed under + and ·", Ch 11)
def-function (claim): m + n in N for m, n in N (addition N x N -> N, the example after the definition; also exr-functions-b1 (b)) | ch07 (promised; STATUS row "ℕ closed under + and ·", Ch 11)
exr-functions-b1 (solution): in (e), (-1)^n is defined, and is 1 for even n and -1 for odd n | ch07 (promised; STATUS rows "definition by recursion (powers)", Ch 11, and "every integer is even or odd, and not both", Ch 1)
def-surjective (example): the Quick check on n -> n + 1 uses n + 1 in N and n + 1 >= 1 for n in N; m - 1 in Z for m in Z | ch07 (promised; STATUS rows "ℕ closed under + and ·" and "nothing between n and n + 1", Ch 11, and "ℤ closed under +, − and ·", Ch 11)
exr-functions-b3 (solution): n >= 1 gives n - 1 in N; n + 1 >= 1 for n in N | ch07 (promised; STATUS row "n >= 1 => n - 1 in N")
exr-functions-a1 (solution): negation laws | ch04 (promised): prp-bounded-quantifier-negation, prp-negated-implication, prose pointer
-->
