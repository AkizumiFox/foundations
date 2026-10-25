<!-- Parked from fd2 (fd2/authoring/design/layout-six-chapters.md §2, approved 2026-10-26). Not part of any book's src; nothing builds or scans it.
Old section: fd2 5.3 Binary Operations (src/ch05-building-functions/03-binary-operations.md)
Labels: def-binary-operation, exm-first-operations, def-operation-properties, exm-subtraction-identity, prp-operation-identity-unique, exm-method-two-ways, prp-operation-inverse-unique, exm-two-inverses, prp-operation-inverse-rules, prp-pointwise-operations, prp-composition-operation, prp-operation-on-quotient, exr-binary-operations-a1, exr-binary-operations-b1, exr-binary-operations-b2, exr-binary-operations-b3, exr-binary-operations-b4, exr-binary-operations-c1, exr-binary-operations-c2, exr-binary-operations-c3
Intended home: fd5 Algebraic Preliminaries, a later revision (overlaps fd5 Chapter 2 to be resolved then); no fd5 file cites these labels
-->

# Binary Operations

Sections 5.1 and 5.2 built new functions from old ones by cutting, gluing and factoring. This section looks at functions of a special shape: functions that take two elements of a set and return a third element of the same set, such as \( + \) on \( \nZ \), \( \cup \) on \( \powerset{X} \) and \( \circ \) on the functions from a set to itself. We name the properties such an operation may have, one at a time, and ask what each property buys on its own. The central answers, uniqueness of identities and of inverses, are short proofs by one method, computing a single expression in two ways; the rest are proved by checking candidates. All of them work at once for numbers, for sets, for functions and for the hours of the clock.

## Brackets

Nobody writes brackets in \( 2 + 3 + 4 \): whether we add \( 2 + 3 \) first or \( 3 + 4 \) first, the answer is \( 9 \). Subtraction is different. Reading \( 2 - 3 - 4 \) from the left gives \( (2 - 3) - 4 = -5 \), and from the right gives \( 2 - (3 - 4) = 3 \). Powers behave like subtraction: \( 2^{(3^2)} = 2^9 = 512 \), while \( (2^3)^2 = 8^2 = 64 \). School arithmetic settles this by convention (subtraction from the left, towers of powers from the top), and a convention is needed exactly because the bracketing changes the answer.

The same questions arise far from numbers. For subsets of a set \( X \), is \( (A \cup B) \cup C \) the same set as \( A \cup (B \cup C) \)? For functions from \( X \) to itself, is \( h \circ (g \circ f) \) the same function as \( (h \circ g) \circ f \)? On the clock \( \nZ/12 \) of Section 4.2, is there an hour that changes nothing when added, as \( 0 \) does for integers, and can every hour be undone?

Each of these questions asks whether some rule of arithmetic holds for some way of combining two things into a third. The aim of this section is to separate the rules and to find out what each rule gives on its own. Here is a test question to keep in mind: can a set with an operation have two different elements that both behave like \( 0 \)? For \( + \) on \( \nZ \) the answer seems obvious, but the reason is not; the answer comes in the subsection "One identity, one inverse".

## Operations

The first thing to fix is what counts as a way of combining two things. Two natural candidates fail. Subtraction on \( \nN \) takes the pair \( (2, 3) \in \nN \times \nN \) to \( -1 \), which is not in \( \nN \). Division on \( \nR \) has no value at all at the pair \( (1, 0) \). The first fails because a value leaves the set; the second fails because a pair has no value. A way of combining must give **every** pair a value, and the value must lie **in the set**. Those are the two halves of being a function with domain \( X \times X \) and codomain \( X \) (@def-function).

*An operation on a set combines any two of its elements into a third element of the same set.*

::: {#def-binary-operation}
[Binary Operation]

Let \( X \) be a set. A **binary operation** on \( X \), or an **operation** on \( X \), is a function
\[
\ast \colon X \times X \to X .
\]
Its value at \( (x, y) \) is written \( x \ast y \) rather than \( \ast(x, y) \).

A subset \( A \subseteq X \) is **closed** under \( \ast \) if \( a \ast b \in A \) **for all** \( a, b \in A \).
:::

In words: the definition asks for a function, so each pair \( (x, y) \) of elements of \( X \), in this order, has **exactly one** value, and that value lies in \( X \). The order matters, since \( (x, y) \) and \( (y, x) \) are different pairs and may have different values; \( 2 - 3 \ne 3 - 2 \). The letter \( \ast \) is a name for the operation, like \( f \) for a function. In examples it is replaced by a familiar symbol, \( + \), \( \cdot \), \( \cup \), \( \circ \).

If \( A \) is closed under \( \ast \), then the restriction of \( \ast \) to \( A \times A \), with codomain \( A \), is an operation on \( A \): restriction to a subset of the domain (@def-restriction-extension) gives a function \( A \times A \to X \), and closure says its values lie in \( A \), so \( A \) may serve as the codomain. We keep the symbol \( \ast \) for the restricted operation.

::: {#exm-first-operations}
[Operations]

Decide which of the following are operations on the set named, and which subsets named are closed.

::: {.enumerate options="label=(\alph*)"}
1. \( + \), \( \cdot \) and \( - \) on \( \nZ \); the average \( x \ast y \coloneqq (x + y)/2 \) and \( \max \) on \( \nR \).
2. \( \cup \), \( \cap \) and the symmetric difference \( \triangle \) of Section 5.1 on \( \powerset{X} \).
3. Composition \( \circ \) on \( X^X \), the set of all functions \( X \to X \).
4. \( [a] + [b] \coloneqq [a + b] \) and \( [a][b] \coloneqq [ab] \) on \( \nZ/n \), for \( n \in \nZ_{>0} \).
5. Division \( (x, y) \mapsto x/y \) on \( \nR \setminus \{0\} \); and the subset \( \nZ_{>0} \) of \( \nZ \), under \( + \) and under \( - \).
:::
:::

::: {.solution}
(a) Each rule gives every pair of integers one integer, and every pair of reals one real, so each is an operation. The average is an operation on \( \nR \) but not on \( \nZ \): \( (0 + 1)/2 \notin \nZ \).

(b) For \( A, B \subseteq X \), the sets \( A \cup B \), \( A \cap B \) and \( A \triangle B \) are again subsets of \( X \) (@def-set-operations), so each is an operation on \( \powerset{X} \).

(c) For \( f, g \in X^X \), the composite \( g \circ f \) is a function \( X \to X \) (@def-composition), so \( (g, f) \mapsto g \circ f \) is an operation on \( X^X \).

(d) Both rules read representatives of classes; @prp-congruence-arithmetic proved that they are well defined, that is, that each pair of classes gets exactly one class. So both are operations on \( \nZ/n \).

(e) If \( x, y \ne 0 \), then \( x/y \) is defined and \( x/y \ne 0 \), so division is an operation on \( \nR \setminus \{0\} \). The positive integers are closed under \( + \), since a sum of positive integers is positive. They are not closed under \( - \): \( 1, 2 \in \nZ_{>0} \), and \( 1 - 2 = -1 \notin \nZ_{>0} \).
:::

Part (d) is the reason this section returns to quotients at its end: an operation on classes is a rule on representatives together with a proof of well-definedness. Part (e) shows that a rule that fails on one set may succeed on a smaller one; the pairs that caused trouble for division, those with second entry \( 0 \), have been removed.

::: {.check}
Is \( (A, B) \mapsto A \setminus B \) an operation on \( \powerset{X} \)? Are the even integers closed under \( + \)? The odd integers?
:::

::: {.solution}
Yes: for \( A, B \subseteq X \), \( A \setminus B \subseteq A \subseteq X \), so the value lies in \( \powerset{X} \). Yes: \( 2k + 2l = 2(k + l) \). No: \( 1 \) is odd and \( 1 + 1 = 2 \) is not.
:::

## Properties

The questions of the hook are now questions about an operation \( \ast \) on a set \( X \). Each asks whether an equation holds for every choice of elements, or whether some element has a special behavior.

::: {#def-operation-properties}
[Associative, Commutative, Identity, Inverse]

Let \( \ast \) be an operation on a set \( X \).

::: {.enumerate options="label=(\alph*)"}
1. \( \ast \) is **associative** if \( (x \ast y) \ast z = x \ast (y \ast z) \) **for all** \( x, y, z \in X \).
2. \( \ast \) is **commutative** if \( x \ast y = y \ast x \) **for all** \( x, y \in X \).
3. An element \( e \in X \) is a **left identity** of \( \ast \) if \( e \ast x = x \) **for every** \( x \in X \); a **right identity** if \( x \ast e = x \) **for every** \( x \in X \); and an **identity** if it is both.
4. Suppose \( \ast \) has an identity \( e \), and let \( x \in X \). An element \( y \in X \) is an **inverse** of \( x \) if \( x \ast y = e \) **and** \( y \ast x = e \). The element \( x \) is **invertible** if it has an inverse.
:::
:::

In words: associativity says brackets may be moved; commutativity says the two inputs may be swapped. A left or right identity is an element that changes nothing, from the side named; an identity must change nothing from **both** sides and must do so for **every** element. An inverse of \( x \) undoes \( x \), again from both sides, and it is defined only relative to an identity. Clause (d) says "an inverse", not "the inverse": nothing in the definition says there is only one.

For \( + \) on \( \nZ \), all four hold: \( + \) is associative and commutative, \( 0 \) is an identity, and \( -x \) is an inverse of \( x \). For \( \cdot \) on \( \nZ \), \( 1 \) is an identity, and only \( 1 \) and \( -1 \) are invertible. For \( \cup \) on \( \powerset{X} \), \( \emptyset \) is an identity, since \( \emptyset \cup A = A = A \cup \emptyset \).

Deciding whether an operation has a property is the work of Section 4.1's method for relations (@exm-method-relation-properties): a property that says "for all" is proved by taking arbitrary elements, and a failure needs one witness, checked. For an identity the quantifiers are the other way round, "there is an \( e \) such that for every \( x \)", so a proof names one \( e \) and checks it against every \( x \), and a refutation must show that **every** candidate \( e \) fails at some \( x \).

::: {#exm-subtraction-identity}
[A right identity that is not an identity]

Decide whether subtraction on \( \nZ \) is associative, and find its left and right identities.
:::

::: {.solution}
*Not associative.* The triple \( 2, 3, 4 \) of the hook is a witness: \( (2 - 3) - 4 = -5 \) and \( 2 - (3 - 4) = 3 \).

*A right identity.* For every \( x \in \nZ \), \( x - 0 = x \), so \( 0 \) is a right identity.

*Not a left identity.* \( 0 - 1 = -1 \ne 1 \), so \( 0 \) fails at \( x = 1 \).

*No left identity at all.* Suppose \( e \) is a left identity, so \( e - x = x \) for every \( x \in \nZ \). At \( x = 0 \) this gives \( e = 0 \); at \( x = 1 \) it gives \( e - 1 = 1 \), so \( e = 2 \). Then \( 0 = 2 \), which is false. So no integer is a left identity, and subtraction has no identity.
:::

The refutation of "there is a left identity" did not test candidates one by one. It assumed a left identity \( e \), used the hypothesis "for every \( x \)" at two well-chosen values of \( x \), and reached two incompatible values for \( e \).

::: {.check}
Is the average \( x \ast y \coloneqq (x + y)/2 \) on \( \nR \) associative? Is it commutative? Has it an identity?
:::

::: {.solution}
Not associative: \( (0 \ast 0) \ast 4 = 0 \ast 4 = 2 \), while \( 0 \ast (0 \ast 4) = 0 \ast 2 = 1 \). Commutative: \( (x + y)/2 = (y + x)/2 \). No identity: if \( (e + x)/2 = x \) for every \( x \), then \( e = x \) for every \( x \in \nR \), so \( e = 0 \) and \( e = 1 \), which is false.
:::

::: {.check}
Consider \( \max \) on \( \nN \) and \( \max \) on \( \nZ \). Is each associative? Commutative? Has it an identity?
:::

::: {.solution}
Both are associative, since \( \max(\max(x, y), z) \) and \( \max(x, \max(y, z)) \) are both the largest of \( x, y, z \), and both are commutative. On \( \nN \), \( 0 \) is an identity: \( \max(0, x) = x = \max(x, 0) \) since \( x \ge 0 \). On \( \nZ \) there is none: an identity \( e \) would need \( \max(e, e - 1) = e - 1 \), but \( \max(e, e - 1) = e \). The same rule, on a larger set, loses its identity.
:::

## One identity, one inverse

Back to the test question of the hook. An operation may have several left identities: for \( x \ast y \coloneqq y \) on a set with two elements, every element is a left identity (Exercise A1 (c)). But an element that is an identity from both sides is never shared.

::: {#prp-operation-identity-unique}
[An Identity Is Unique]

Let \( \ast \) be an operation on a set \( X \). If \( e \) is a left identity and \( e' \) is a right identity of \( \ast \), then \( e = e' \). In particular, \( \ast \) has at most one identity.
:::

::: {.idea}
[Scratch work]

Two candidates, so this is the uniqueness half of @exm-method-uniqueness: two names, about which we know only the defining equations, to be shown equal. The givens are equations about products; the goal mentions no product at all. The gap is to find one product that both givens can simplify.

| Givens | Goal |
|---|---|
| \( e \ast x = x \) for every \( x \in X \); \( x \ast e' = x \) for every \( x \in X \) | \( e = e' \) |
| the givens speak about products; the goal about two elements | one product that each given simplifies |
| the product \( e \ast e' \): the first given at \( x = e' \) makes it \( e' \); the second at \( x = e \) makes it \( e \) | \( e = e \ast e' = e' \) |

The last row closes the gap: the product \( e \ast e' \), with one candidate on each side, is the expression both givens can reach.
:::

::: {.proof}
Since \( e' \) is a right identity, the case \( x = e \) of its defining equation gives \( e \ast e' = e \). Since \( e \) is a left identity, the case \( x = e' \) gives \( e \ast e' = e' \). Hence \( e = e \ast e' = e' \).

If \( e \) and \( e' \) are both identities, then \( e \) is a left identity and \( e' \) a right identity, so \( e = e' \). This proves the proposition.
:::

Neither associativity nor commutativity was used: the proof applies two hypotheses once each, to the single product \( e \ast e' \). So the answer to the test question is no, for every operation whatsoever. Because of the proposition, we may speak of **the** identity of \( \ast \) when there is one.

The proof is an instance of a move that runs through this section and the next.

::: {#exm-method-two-ways}
[Method: compute one expression in two ways]

**Template.** To prove \( a = b \) when \( a \) and \( b \) are known only through equations: (1) find one expression \( m \) that the equations about \( a \) reduce to \( a \), and the equations about \( b \) reduce to \( b \); (2) write the chain \( a = \dots = m = \dots = b \), citing a hypothesis at each "\( = \)".

**When to use it.** Uniqueness of identities and of inverses, cancellation, and any goal equating two objects given by equations.

**The usual failure.** Assuming \( a = b \) somewhere in the chain (entry (N9) of @fd1:exm-not-allowed-catalogue); using associativity or commutativity that was not given; a bracket moved silently.
:::

Inverses are the second test of the method. Here associativity is needed, and the proof shows exactly where.

::: {#prp-operation-inverse-unique}
[Inverses Are Unique for an Associative Operation]

Let \( \ast \) be an associative operation on a set \( X \) with identity \( e \), and let \( x \in X \). If \( y \ast x = e \) and \( x \ast z = e \), then \( y = z \). In particular, \( x \) has at most one inverse.
:::

::: {.idea}
As in @exm-method-two-ways. The expression is \( m = (y \ast x) \ast z \), which is also \( y \ast (x \ast z) \) by associativity: bracketed as written it is \( e \ast z = z \), and regrouped it is \( y \ast e = y \). Associativity is exactly the license to read it both ways.
:::

::: {.proof}
Using that \( e \) is an identity, then \( x \ast z = e \), then associativity, then \( y \ast x = e \), and finally that \( e \) is an identity again:
\[
y = y \ast e = y \ast (x \ast z) = (y \ast x) \ast z = e \ast z = z .
\]
If \( y \) and \( z \) are both inverses of \( x \), then in particular \( y \ast x = e \) and \( x \ast z = e \), so \( y = z \). This proves the proposition.
:::

For an associative operation with identity, the inverse of an invertible \( x \) is therefore unique, and we write it \( x^{-1} \). For an operation written \( + \), the inverse is written \( -x \) instead. The proposition is a little stronger than uniqueness: an element \( x \) with some \( y \) such that \( y \ast x = e \) and some \( z \) such that \( x \ast z = e \) has \( y = z \), and then \( y \) is an inverse of \( x \), so \( x \) is invertible. This is the same computation as @prp-inverse-unique for functions, now done for any associative operation.

Without associativity the conclusion can fail, and a three-element table shows it.

::: {#exm-two-inverses}
[Without associativity, two inverses]

Let \( X = \{e, a, b\} \) with three different elements, and define \( \ast \) by the table below: the entry in row \( u \) and column \( v \) is \( u \ast v \).

| \( \ast \) | \( e \) | \( a \) | \( b \) |
|---|---|---|---|
| \( e \) | \( e \) | \( a \) | \( b \) |
| \( a \) | \( a \) | \( e \) | \( e \) |
| \( b \) | \( b \) | \( e \) | \( e \) |

Show that \( \ast \) is a commutative operation with identity \( e \), that \( a \) has two different inverses, and that \( \ast \) is not associative.
:::

::: {.solution}
The table gives each of the nine pairs exactly one value in \( X \), so \( \ast \) is an operation on \( X \). The table is symmetric about its diagonal, which says \( u \ast v = v \ast u \) for all \( u, v \): \( \ast \) is commutative. The row and the column of \( e \) repeat the headings, so \( e \ast u = u = u \ast e \) for every \( u \): \( e \) is the identity.

Since \( a \ast a = e \), the element \( a \) is an inverse of itself; since \( a \ast b = e = b \ast a \), the element \( b \) is another inverse of \( a \), and \( a \ne b \).

Finally, \( (a \ast a) \ast b = e \ast b = b \), while \( a \ast (a \ast b) = a \ast e = a \). These differ, so \( \ast \) is not associative.
:::

The last line is @prp-operation-inverse-unique's chain, run on \( y = a \), \( x = a \), \( z = b \), breaking at the one step that used associativity.

With uniqueness in hand, the rules that school algebra uses for inverses of numbers can be proved for any associative operation. The method for each is the same: name a candidate, check it on both sides, and let uniqueness do the rest.

::: {#prp-operation-inverse-rules}
[Inverses of Products]

Let \( \ast \) be an associative operation on a set \( X \) with identity \( e \).

::: {.enumerate options="label=(\alph*)"}
1. \( e \) is invertible, and \( e^{-1} = e \).
2. If \( x \) is invertible, then so is \( x^{-1} \), and \( (x^{-1})^{-1} = x \).
3. If \( x \) and \( y \) are invertible, then so is \( x \ast y \), and \( (x \ast y)^{-1} = y^{-1} \ast x^{-1} \).
:::
:::

::: {.idea}
Each part names a candidate and checks it, which is the existence half of @exm-method-uniqueness; uniqueness was proved once and for all in @prp-operation-inverse-unique. For (c) the candidate is found by asking what undoes \( x \ast y \): first remove \( y \), then \( x \).
:::

::: {.proof}
In each part we show that the candidate is an inverse by checking both equations of @def-operation-properties (d); then it is **the** inverse by @prp-operation-inverse-unique.

*(a)* \( e \ast e = e \), since \( e \) is an identity, and this one equation is both required equations.

*(b)* The two equations \( x \ast x^{-1} = e \) and \( x^{-1} \ast x = e \), which say that \( x^{-1} \) is an inverse of \( x \), also say that \( x \) is an inverse of \( x^{-1} \).

*(c)* Using associativity twice to regroup, then the defining equation of \( y^{-1} \), the identity, and the defining equation of \( x^{-1} \):
\[
\begin{aligned}
(x \ast y) \ast (y^{-1} \ast x^{-1}) &= x \ast \bigl(y \ast (y^{-1} \ast x^{-1})\bigr) = x \ast \bigl((y \ast y^{-1}) \ast x^{-1}\bigr) \\
&= x \ast (e \ast x^{-1}) = x \ast x^{-1} = e .
\end{aligned}
\]
In the same way, \( (y^{-1} \ast x^{-1}) \ast (x \ast y) = y^{-1} \ast \bigl(x^{-1} \ast (x \ast y)\bigr) = y^{-1} \ast \bigl((x^{-1} \ast x) \ast y\bigr) = y^{-1} \ast (e \ast y) = y^{-1} \ast y = e \). This proves the proposition.
:::

In (c) the order reverses: to undo "first \( x \), then \( y \)", one undoes \( y \) first. The display moved brackets one step at a time; Exercise C1 shows that for four factors every bracketing gives the same element.

::: {.check}
Which elements of \( \powerset{X} \) are invertible under \( \cup \)? Which are invertible under \( \triangle \)?
:::

::: {.solution}
Both operations have identity \( \emptyset \): \( A \cup \emptyset = A \), and \( A \triangle \emptyset = (A \setminus \emptyset) \cup (\emptyset \setminus A) = A \) and \( \emptyset \triangle A = (\emptyset \setminus A) \cup (A \setminus \emptyset) = A \). Under \( \cup \), if \( A \cup B = \emptyset \), then \( A \subseteq A \cup B = \emptyset \), so \( A = \emptyset \): only \( \emptyset \) is invertible. Under \( \triangle \), \( A \triangle A = (A \setminus A) \cup (A \setminus A) = \emptyset \), so every \( A \) is invertible and is its own inverse.
:::

## Operations on functions

An operation on a set \( Y \) gives an operation on every set of functions into \( Y \), by combining values point by point. This is how \( f + g \) and \( f \cdot g \) are defined for real functions, and it carries each property of the operation on \( Y \) over to the functions.

::: {#prp-pointwise-operations}
[Pointwise Operations]

Let \( \ast \) be an operation on a set \( Y \), and let \( X \) be a set. For \( f, g \in Y^X \), define \( f \ast g \colon X \to Y \) by
\[
(f \ast g)(x) \coloneqq f(x) \ast g(x) \qquad (x \in X) .
\]
This is an operation on \( Y^X \), the **pointwise** operation, and:

::: {.enumerate options="label=(\alph*)"}
1. if \( \ast \) is associative, or commutative, on \( Y \), then so is the pointwise operation on \( Y^X \);
2. if \( e \) is an identity of \( \ast \), then the constant function \( c_e \colon X \to Y \), \( x \mapsto e \), is an identity of the pointwise operation;
3. if \( \ast \) is associative with identity \( e \), then \( f \in Y^X \) is invertible if and only if every value \( f(x) \) is invertible in \( Y \), and then the inverse of \( f \) is \( x \mapsto f(x)^{-1} \).
:::
:::

::: {.idea}
An equation between functions is checked value by value (@prp-function-equality), and at the point \( x \) each law for the pointwise operation is the same law for \( \ast \), applied to the values \( f(x) \), \( g(x) \), \( h(x) \).
:::

::: {.proof}
For \( x \in X \), the value \( f(x) \ast g(x) \) is one element of \( Y \), so \( f \ast g \) is a function \( X \to Y \), and \( (f, g) \mapsto f \ast g \) is an operation on \( Y^X \). Each equation below is between functions \( X \to Y \), so by @prp-function-equality it suffices to compare values at an arbitrary \( x \in X \).

*(a)* By the definition, used twice on each side, and associativity in \( Y \),
\[
\bigl((f \ast g) \ast h\bigr)(x) = (f(x) \ast g(x)) \ast h(x) = f(x) \ast (g(x) \ast h(x)) = \bigl(f \ast (g \ast h)\bigr)(x) .
\]
Likewise \( (f \ast g)(x) = f(x) \ast g(x) = g(x) \ast f(x) = (g \ast f)(x) \) when \( \ast \) is commutative.

*(b)* \( (c_e \ast f)(x) = e \ast f(x) = f(x) \) and \( (f \ast c_e)(x) = f(x) \ast e = f(x) \).

*(c)* \( (\Rightarrow) \) Let \( g \) be an inverse of \( f \), so \( f \ast g = c_e = g \ast f \), the identity being \( c_e \) by (b) and @prp-operation-identity-unique. Evaluating at \( x \) gives \( f(x) \ast g(x) = e = g(x) \ast f(x) \), so \( g(x) \) is an inverse of \( f(x) \). \( (\Leftarrow) \) If every \( f(x) \) is invertible, its inverse \( f(x)^{-1} \) is unique (@prp-operation-inverse-unique), so \( g(x) \coloneqq f(x)^{-1} \) defines a function \( g \colon X \to Y \). Then \( (f \ast g)(x) = f(x) \ast f(x)^{-1} = e = c_e(x) \), and likewise \( (g \ast f)(x) = e \), so \( g \) is an inverse of \( f \). The pointwise operation is associative by (a), so this inverse is the only one, by @prp-operation-inverse-unique. This proves the proposition.
:::

Part (c) needs every value to be invertible, not just most of them. On \( \nR^{\nR} \) with pointwise \( \cdot \), the identity is the constant \( c_1 \); the function \( x \mapsto x \) is not invertible, because its value at \( 0 \) has no multiplicative inverse, although every other value has one.

::: {.warning}
[Iterate or product?]

On \( \nR^{\nR} \) the symbol \( f^2 \) could mean two different functions: the pointwise product \( x \mapsto f(x) \cdot f(x) \), or the composite \( f \circ f \). For \( f(x) = x + 1 \) the first is \( x \mapsto (x + 1)^2 \) and the second is \( x \mapsto x + 2 \). In this book \( f^n \) always means the \( n \)-th iterate, \( f \) composed with itself \( n \) times, defined in Section 5.4. A pointwise product is written \( f \cdot g \), and a pointwise power is written out, \( x \mapsto f(x)^n \). For the same reason \( f^{-1} \) standing alone always means the inverse function, while \( f^{-1}(B) \) for a set \( B \) is still the preimage of @def-preimage, defined for every \( f \); the inverse of \( f \) under pointwise \( \cdot \), when it exists, is written \( x \mapsto 1/f(x) \).
:::

Indicators are a first instance. The set \( \{0, 1\} \) is closed under multiplication of numbers, so \( \cdot \) is an operation on \( \{0, 1\} \), and pointwise multiplication is an operation on \( \{0, 1\}^X \). By @prp-indicator-arithmetic (a), \( \ind_A \cdot \ind_B = \ind_{A \cap B} \): on indicators, the pointwise product **is** intersection. The identity of pointwise \( \cdot \) is the constant function \( c_1 \), which is \( \ind_X \), matching \( X \cap A = A \) for \( A \subseteq X \).

The second instance is composition. On \( X^X \), any two functions can be composed in either order, and composition is an operation (@exm-first-operations (c)).

::: {#prp-composition-operation}
[Composition on X^X]

Let \( X \) be a set. Composition \( (g, f) \mapsto g \circ f \) is an associative operation on \( X^X \) with identity \( \id_X \). An element \( f \in X^X \) is invertible under \( \circ \) if and only if \( f \) is bijective, and then its inverse under \( \circ \) is the inverse function \( f^{-1} \). If \( X \) has two different elements, then \( \circ \) is not commutative on \( X^X \).
:::

::: {.proof}
Associativity and \( f \circ \id_X = f = \id_X \circ f \) are @prp-composition-associative, with all four sets equal to \( X \). Under \( \circ \), an inverse of \( f \) in the sense of @def-operation-properties (d) is a \( g \in X^X \) with \( f \circ g = \id_X = g \circ f \), which is exactly a two-sided inverse of \( f \) in the sense of @def-inverse-function. By @thm-bijection-iff-inverse, \( f \) has one if and only if \( f \) is bijective, and it is then the inverse function \( f^{-1} \), which is unique by @prp-inverse-unique.

Now let \( a, b \in X \) with \( a \ne b \), and let \( c_a, c_b \in X^X \) be the constant functions with values \( a \) and \( b \). For every \( x \in X \), \( (c_a \circ c_b)(x) = c_a(b) = a \) and \( (c_b \circ c_a)(x) = c_b(a) = b \). So \( c_a \circ c_b = c_a \) and \( c_b \circ c_a = c_b \), and these differ, since their values at \( a \) differ (@prp-function-equality). This proves the proposition.
:::

So the invertible elements of \( X^X \) under composition are exactly the bijections from \( X \) to itself, the subject of Section 5.4. For them, @prp-operation-inverse-rules (c) says \( (g \circ f)^{-1} = f^{-1} \circ g^{-1} \). That rule appeared as Exercise B2 of Section 1.6 (@exr-inverses-b2); here it is proved once, for every associative operation, and the rule for bijections of a set to itself is one case of it (Exercise B2 of Section 1.6 allows three different sets).

::: {.check}
In \( \nR^{\nR} \), find the inverse of \( f(x) = 2x + 1 \) under composition, and its inverse under pointwise \( + \).
:::

::: {.solution}
Under \( \circ \): \( g(x) = (x - 1)/2 \), since \( f(g(x)) = (x - 1) + 1 = x \) and \( g(f(x)) = (2x + 1 - 1)/2 = x \). Under pointwise \( + \), whose identity is the constant \( c_0 \): \( x \mapsto -2x - 1 \), since \( (2x + 1) + (-2x - 1) = 0 \). The two inverses are different functions; "the inverse" always names its operation.
:::

## Operations on a quotient

The clock adds hours, and Section 4.2 checked that the addition is well defined (@prp-congruence-arithmetic). Every operation that respects an equivalence relation passes to the quotient in the same way, and it takes its properties with it.

::: {#prp-operation-on-quotient}
[Operations on a Quotient]

Let \( \ast \) be an operation on a set \( X \), and let \( \sim \) be an equivalence relation on \( X \) such that, for all \( x, x', y, y' \in X \),
\[
x \sim x' \text{ and } y \sim y' \quad \Longrightarrow \quad x \ast y \sim x' \ast y' .
\]
Then \( [x] \ast [y] \coloneqq [x \ast y] \) is a well-defined operation on \( X/{\sim} \), and the quotient map satisfies \( q(x \ast y) = q(x) \ast q(y) \). Moreover:

::: {.enumerate options="label=(\alph*)"}
1. if \( \ast \) is associative, or commutative, then so is the operation on \( X/{\sim} \);
2. if \( e \) is an identity of \( \ast \), then \( [e] \) is an identity of the operation on \( X/{\sim} \);
3. if \( y \) is an inverse of \( x \), then \( [y] \) is an inverse of \( [x] \).
:::
:::

::: {.idea}
As in @exm-method-factor-through-quotient, the rule computes a value from representatives, so the one thing to check is that the value does not depend on them (@exm-method-well-definedness); here there are two representatives to change, and the hypothesis on \( \sim \) handles both at once. Each law then holds for classes because it holds for representatives, and every class has one.
:::

::: {.proof}
*Well defined.* Every class is \( [x] \) for some \( x \in X \) (@def-quotient-set), so the rule gives every pair of classes a value, and the value \( [x \ast y] \) lies in \( X/{\sim} \). Let \( [x] = [x'] \) and \( [y] = [y'] \). By @thm-classes-partition (b), \( x \sim x' \) and \( y \sim y' \), so \( x \ast y \sim x' \ast y' \) by hypothesis, and \( [x \ast y] = [x' \ast y'] \) by @thm-classes-partition (b) again. So the value does not depend on the representatives, and \( \ast \) is an operation on \( X/{\sim} \). The equation \( q(x \ast y) = [x \ast y] = [x] \ast [y] = q(x) \ast q(y) \) is the definition.

*(a)* Let three classes be given, with representatives \( x, y, z \). Applying the definition twice on each side and associativity in \( X \),
\[
([x] \ast [y]) \ast [z] = [(x \ast y) \ast z] = [x \ast (y \ast z)] = [x] \ast ([y] \ast [z]) .
\]
Likewise \( [x] \ast [y] = [x \ast y] = [y \ast x] = [y] \ast [x] \) when \( \ast \) is commutative.

*(b)* \( [e] \ast [x] = [e \ast x] = [x] \) and \( [x] \ast [e] = [x \ast e] = [x] \), for every class \( [x] \).

*(c)* \( [x] \ast [y] = [x \ast y] = [e] \) and \( [y] \ast [x] = [y \ast x] = [e] \), and \( [e] \) is the identity by (b). This proves the proposition.
:::

The hypothesis on \( \sim \) is the whole content: it says that \( \ast \) does not see the difference between equivalent elements. For \( \nZ \) with congruence modulo \( n \), it is exactly @prp-congruence-arithmetic, for \( + \) and for \( \cdot \). So \( \nZ/n \) inherits from \( \nZ \): addition is associative and commutative with identity \( [0] \), every class \( [a] \) has the inverse \( [-a] \) and we write \( -[a] = [-a] \), and multiplication is associative and commutative with identity \( [1] \). On the clock, \( [9] + [3] = [12] = [0] \), so \( -[9] = [3] \): the hour that undoes nine hours is three hours.

Part (c) goes one way only. The quotient can have inverses that \( X \) lacks: in \( \nZ/3 \), \( [2][2] = [4] = [1] \), so \( [2] \) is invertible under multiplication, while no integer \( y \) has \( 2y = 1 \), since \( 1 \) is odd.

## Exercises

### A. Check your understanding

::: {#exr-binary-operations-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Which of the following are operations: subtraction on \( \nN \); subtraction on \( \nZ \); \( (x, y) \mapsto x/y \) on \( \nR \setminus \{0\} \); \( (x, y) \mapsto x/y \) on \( \nZ \setminus \{0\} \)?
2. Write the table of \( + \) on \( \nZ/3 = \{[0], [1], [2]\} \). Find the identity and the inverse of each class.
3. Let \( X \) be a set with at least two elements, and let \( x \ast y \coloneqq y \). Find all left identities and all right identities of \( \ast \).
4. State the template of the method of computing one expression in two ways, and say which expression it computes in the proof of @prp-operation-inverse-unique.
:::
:::

::: {.solution}
(a) Subtraction on \( \nN \): no, \( 2 - 3 = -1 \notin \nN \). Subtraction on \( \nZ \): yes. Division on \( \nR \setminus \{0\} \): yes, since \( x/y \) is defined and non-zero for \( x, y \ne 0 \). Division on \( \nZ \setminus \{0\} \): no, \( 1/2 \notin \nZ \).

(b) By the rule \( [a] + [b] = [a + b] \), reducing with @prp-integers-mod-n (\( [3] = [0] \), \( [4] = [1] \)):

| \( + \) | \( [0] \) | \( [1] \) | \( [2] \) |
|---|---|---|---|
| \( [0] \) | \( [0] \) | \( [1] \) | \( [2] \) |
| \( [1] \) | \( [1] \) | \( [2] \) | \( [0] \) |
| \( [2] \) | \( [2] \) | \( [0] \) | \( [1] \) |

The row and column of \( [0] \) repeat the headings, so \( [0] \) is the identity. Reading off the entries \( [0] \): \( -[0] = [0] \), \( -[1] = [2] \), \( -[2] = [1] \).

(c) Every \( e \in X \) is a left identity, since \( e \ast y = y \) for every \( y \). No element is a right identity: for \( e \in X \), pick \( x \in X \) with \( x \ne e \) (there is one, since \( X \) has at least two elements); then \( x \ast e = e \ne x \). So left identities need not be unique when there is no right identity; @prp-operation-identity-unique needs one of each.

(d) To prove \( a = b \) for objects known only through equations, find one expression that the equations about \( a \) reduce to \( a \) and those about \( b \) reduce to \( b \), and write \( a = \dots = m = \dots = b \) with a reason at each step (@exm-method-two-ways). In @prp-operation-inverse-unique the expression is \( (y \ast x) \ast z \), which equals \( z \) as written and, regrouped as \( y \ast (x \ast z) \), equals \( y \).
:::

### B. Practice

::: {#exr-binary-operations-b1}
[B1: Deciding properties]

On \( \nR \), let \( x \ast y \coloneqq x + y - xy \). Determine whether \( \ast \) is associative and whether it is commutative, find its identity, and find which elements are invertible, with their inverses. Justify your answer.
:::

::: {.solution}
*Associative.* Expanding both sides,
\[
\begin{aligned}
(x \ast y) \ast z &= (x + y - xy) + z - (x + y - xy)z \\
&= x + y + z - xy - xz - yz + xyz , \\
x \ast (y \ast z) &= x + (y + z - yz) - x(y + z - yz) \\
&= x + y + z - xy - xz - yz + xyz .
\end{aligned}
\]
The two results agree, so \( \ast \) is associative. (Both are unchanged by any rearrangement of \( x, y, z \).)

*Commutative.* \( x + y - xy = y + x - yx \).

*Identity.* \( 0 \ast x = 0 + x - 0 = x \), and \( x \ast 0 = x \) by commutativity; so \( 0 \) is the identity, unique by @prp-operation-identity-unique.

*Inverses.* We need \( y \) with \( x + y - xy = 0 \) (the other side follows by commutativity), that is, \( y(1 - x) = -x \). If \( x \ne 1 \), this has the solution \( y = x/(x - 1) \): indeed \( x + \tfrac{x}{x - 1} - \tfrac{x^2}{x - 1} = \tfrac{x(x - 1) + x - x^2}{x - 1} = 0 \). If \( x = 1 \), then \( 1 \ast y = 1 + y - y = 1 \ne 0 \) for every \( y \), so \( 1 \) has no inverse. So every \( x \ne 1 \) is invertible, with inverse \( x/(x - 1) \) under \( \ast \), and \( 1 \) is not.

*A remark.* \( 1 - x \ast y = (1 - x)(1 - y) \). For \( u, v \in \{0, 1\} \), \( u \ast v = u + v - uv \) is the indicator rule for a union, @prp-indicator-arithmetic (c): \( \ind_{A \cup B}(x) = \ind_A(x) \ast \ind_B(x) \).
:::

::: {#exr-binary-operations-b2}
[B2: Every square is the identity]

Let \( \ast \) be an associative operation on a set \( X \) with identity \( e \), such that \( x \ast x = e \) for every \( x \in X \). Prove that \( \ast \) is commutative. Check the hypothesis for \( \triangle \) on \( \powerset{X} \).
:::

::: {.solution}
Let \( x \in X \). The equation \( x \ast x = e \) says that \( x \) is an inverse of itself, from both sides; by @prp-operation-inverse-unique, \( x^{-1} = x \). Now let \( x, y \in X \). By the hypothesis applied to \( x \ast y \), and by @prp-operation-inverse-rules (c),
\[
x \ast y = (x \ast y)^{-1} = y^{-1} \ast x^{-1} = y \ast x .
\]
For \( \triangle \): it is associative (@exm-symmetric-difference-associative) with identity \( \emptyset \), and \( A \triangle A = \emptyset \) for every \( A \subseteq X \) (the Quick check after @prp-operation-inverse-rules). So \( \triangle \) is commutative, which can also be read off its definition, since \( (A \setminus B) \cup (B \setminus A) \) is symmetric in \( A \) and \( B \).
:::

::: {#exr-binary-operations-b3}
[B3: Two kinds of inverse]

In \( \nR^{\nR} \), find, if they exist, the inverses of \( f(x) = x^3 + 1 \) under composition and under pointwise \( + \), and the inverses of \( g(x) = x^2 \) under composition and under pointwise \( \cdot \). Justify each answer.
:::

::: {.solution}
*\( f \) under \( \circ \).* Let \( h(x) \coloneqq \sqrt[3]{x - 1} \), the real cube root. Then \( f(h(x)) = (x - 1) + 1 = x \) and \( h(f(x)) = \sqrt[3]{x^3} = x \), so \( h \) is the inverse (@prp-composition-operation).

*\( f \) under \( + \).* The identity is \( c_0 \), and \( x \mapsto -x^3 - 1 \) is the inverse: \( (x^3 + 1) + (-x^3 - 1) = 0 \) at every \( x \) (@prp-pointwise-operations (c)).

*\( g \) under \( \circ \).* None: \( g(1) = 1 = g(-1) \), so \( g \) is not injective, hence not bijective, hence not invertible under \( \circ \) by @prp-composition-operation.

*\( g \) under \( \cdot \).* None: the value \( g(0) = 0 \) has no inverse under multiplication of reals (\( 0 \cdot y = 0 \ne 1 \)), so by @prp-pointwise-operations (c) \( g \) is not invertible.
:::

::: {#exr-binary-operations-b4}
[B4: Prove or disprove]

Prove or disprove each statement. Throughout, \( \ast \) is an operation on a set \( X \).

::: {.enumerate options="label=(\alph*)"}
1. Every left identity of \( \ast \) equals every right identity of \( \ast \).
2. \( \ast \) has at most one left identity.
3. If \( \ast \) is associative with identity, \( x \) is invertible and \( x \ast y = x \ast z \), then \( y = z \).
4. If \( \ast \) is associative with identity \( e \) and \( x \ast y = e \), then \( y \ast x = e \).
5. A commutative operation with an identity is associative.
:::
:::

::: {.solution}
(a) True. This is @prp-operation-identity-unique.

(b) False. For \( x \ast y \coloneqq y \) on \( X = \{1, 2\} \), both \( 1 \) and \( 2 \) are left identities, as in Exercise A1 (c).

(c) True, by computing \( (x^{-1} \ast x) \ast y \), regrouped as \( x^{-1} \ast (x \ast y) \), in two ways (@exm-method-two-ways), with associativity at the second and fourth steps:
\[
y = (x^{-1} \ast x) \ast y = x^{-1} \ast (x \ast y) = x^{-1} \ast (x \ast z) = (x^{-1} \ast x) \ast z = z .
\]

(d) False. Take \( X = \nN^{\nN} \) under composition, associative with identity \( \id_{\nN} \) (@prp-composition-operation). Let \( s(n) \coloneqq n + 1 \), and \( p(n) \coloneqq n - 1 \) for \( n \ge 1 \), \( p(0) \coloneqq 0 \): the successor map of Section 1.6 and a left inverse of it. Then \( p \circ s = \id_{\nN} \), since \( p(n + 1) = n \). But \( (s \circ p)(0) = s(0) = 1 \ne 0 \), so \( s \circ p \ne \id_{\nN} \). With \( x = p \) and \( y = s \), \( x \circ y = e \) and \( y \circ x \ne e \).

(e) False. The operation of @exm-two-inverses is commutative with identity \( e \), and not associative.
:::

### C. Going deeper

::: {#exr-binary-operations-c1}
[C1: Four factors]

Let \( \ast \) be an associative operation on a set \( X \), and let \( a, b, c, d \in X \). Writing \( uv \) for \( u \ast v \), show that the five bracketings
\[
((ab)c)d, \quad (a(bc))d, \quad (ab)(cd), \quad a((bc)d), \quad a(b(cd))
\]
are all equal.
:::

::: {.solution}
We show that each equals \( ((ab)c)d \). Each step is one use of associativity, \( (xy)z = x(yz) \), with \( x, y, z \) chosen as stated.

- \( (a(bc))d = ((ab)c)d \): associativity with \( x = a \), \( y = b \), \( z = c \) gives \( a(bc) = (ab)c \), and then both sides are that element times \( d \).
- \( (ab)(cd) = ((ab)c)d \): associativity with \( x = ab \), \( y = c \), \( z = d \).
- \( a((bc)d) = (a(bc))d \): associativity with \( x = a \), \( y = bc \), \( z = d \); and \( (a(bc))d = ((ab)c)d \) by the first item.
- \( a(b(cd)) = (ab)(cd) \): associativity with \( x = a \), \( y = b \), \( z = cd \); and \( (ab)(cd) = ((ab)c)d \) by the second item.

So all five bracketings are equal. That every bracketing of any finite number of factors gives the same element is true as well; its proof is an induction on the number of factors, not carried out here, and this chapter regroups longer composites only by repeated use of the three-factor law.
:::

::: {#exr-binary-operations-c2}
[C2: Find the error]

Let \( \ast \) be an operation on a set \( X \) with identity \( e \). A student argues:

> (1) Let \( y \) and \( z \) be inverses of \( x \). (2) Then \( x \ast y = e \) and \( x \ast z = e \), so \( x \ast y = x \ast z \). (3) Cancelling \( x \) on the left, \( y = z \). (4) Hence an element has at most one inverse.

::: {.enumerate options="label=(\alph*)"}
1. Which line fails, and which hypothesis does it hide?
2. Show that without that hypothesis the step of the failing line is false.
:::
:::

::: {.solution}
(a) Line (3) fails. "Cancelling \( x \)" is the statement of Exercise B4 (c), which holds when \( \ast \) is associative and \( x \) is invertible; its proof regroups \( x^{-1} \ast (x \ast y) \) as \( (x^{-1} \ast x) \ast y \), and that is associativity. The statement here does not assume associativity, so line (3) cites a fact that is not available: entry (N9) of @fd1:exm-not-allowed-catalogue. Lines (1) and (2) are correct, and with associativity added the argument becomes a correct proof of @prp-operation-inverse-unique.

(b) In @exm-two-inverses, which has an identity and is not associative, \( a \ast a = e = a \ast b \), so \( a \ast a = a \ast b \), and yet \( a \ne b \). Cancelling \( a \) on the left is false there, and so is the conclusion (4): \( a \) has the two inverses \( a \) and \( b \).

**Marking scheme.** (10 points)

- 3: names line (3) as the step that fails.
- 3: names associativity as the hidden hypothesis, and says where cancellation uses it.
- 4: gives an operation with identity, not associative, and an **invertible** element \( x \) with \( x \ast y = x \ast z \) and \( y \ne z \) (for instance \( y, z \) two inverses of \( x \)), each equation checked.

A different counterexample to cancellation earns the 4 points if its table is given and the failure of associativity is shown. Fatal errors (0 for the step): naming line (2) or line (4); a counterexample that is associative, or that has no identity, or whose element \( x \) is not invertible.
:::

::: {#exr-binary-operations-c3}
[C3: Transport by a bijection]

Let \( \varphi \colon X \to Y \) be a bijection, and let \( \ast \) be an operation on \( Y \). For \( x, x' \in X \), define
\[
x \star x' \coloneqq \varphi^{-1}\bigl(\varphi(x) \ast \varphi(x')\bigr) .
\]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \star \) is an operation on \( X \) with \( \varphi(x \star x') = \varphi(x) \ast \varphi(x') \) for all \( x, x' \in X \).
2. Show that \( \star \) is associative if and only if \( \ast \) is.
3. Compute \( \star \) for \( X = Y = \nR \), \( \varphi(x) = 1 - x \) and \( \ast = \cdot \).
:::
:::

::: {.solution}
(a) The inverse function \( \varphi^{-1} \colon Y \to X \) exists by @thm-bijection-iff-inverse, so the right-hand side is one element of \( X \) for each pair, and \( \star \) is an operation on \( X \). Applying \( \varphi \) and using \( \varphi \circ \varphi^{-1} = \id_Y \) (@def-inverse-function) gives \( \varphi(x \star x') = \varphi(x) \ast \varphi(x') \).

(b) \( (\Leftarrow) \) Let \( \ast \) be associative and \( x, y, z \in X \). By (a), applied twice on each side,
\[
\varphi\bigl((x \star y) \star z\bigr) = (\varphi(x) \ast \varphi(y)) \ast \varphi(z) = \varphi(x) \ast (\varphi(y) \ast \varphi(z)) = \varphi\bigl(x \star (y \star z)\bigr) ,
\]
and \( \varphi \) is injective, so \( (x \star y) \star z = x \star (y \star z) \). \( (\Rightarrow) \) Let \( \star \) be associative and \( u, v, w \in Y \). Since \( \varphi \) is surjective, \( u = \varphi(x) \), \( v = \varphi(y) \), \( w = \varphi(z) \) for some \( x, y, z \in X \), and the same display read from the outside in gives \( (u \ast v) \ast w = \varphi((x \star y) \star z) = \varphi(x \star (y \star z)) = u \ast (v \ast w) \).

(c) \( \varphi \circ \varphi = \id_{\nR} \), since \( 1 - (1 - x) = x \), so \( \varphi^{-1} = \varphi \) (@def-inverse-function). Hence
\[
x \star x' = 1 - (1 - x)(1 - x') = x + x' - xx' ,
\]
the operation of Exercise B1. Its identity \( 0 = \varphi(1) \) and its one non-invertible element \( 1 = \varphi(0) \) are the images of the identity \( 1 \) and of the non-invertible \( 0 \) of multiplication.
:::

<!-- dependency ledger
exm-first-operations (solution): sums of positive integers are positive; x/y defined and non-zero for non-zero reals; (0 + 1)/2 not an integer | R arithmetic and order, school fact
exm-first-operations (claim): (quick check) A \ B subset of A; 2k + 2l = 2(k + l); 2 is not odd | def-set-operations (cited in the example); def-parity, thm-even-or-odd (F2.1 §01), not cited; arithmetic
def-binary-operation (claim): restricting * to A x A gives a function A x A -> X | def-restriction-extension (cited)
exm-subtraction-identity (solution): (2 - 3) - 4 = -5, 2 - (3 - 4) = 3; e - 1 = 1 gives e = 2; 0 != 2 | arithmetic, school fact
def-operation-properties (claim): + on Z associative, commutative, identity 0, inverse -x; 1 and -1 the only units of Z under multiplication; max of three numbers | R arithmetic and order, school fact (the units claim: |xy| = 1 with x, y non-zero integers forces |x| = |y| = 1, school fact; nothing depends on it)
exm-subtraction-identity (claim): (quick checks after it) average values 2 and 1; max of three numbers; max(e, e - 1) = e | R arithmetic and order, school fact; fd5/authoring/parked/from-fd2/verify/exm-subtraction-identity.py
prp-operation-inverse-rules (claim): (quick check) A union empty = A; A triangle A = empty; A subset of A union B | def-set-operations; the definition of triangle (Section 5.1, inline before prp-indicator-arithmetic); thm-set-algebra
exm-two-inverses (solution): table entries, identity, commutativity, the two inverses, (a*a)*b = b and a*(a*b) = a | inline (read off the table); fd5/authoring/parked/from-fd2/verify/exm-two-inverses.py (all 27 triples)
prp-pointwise-operations (claim): x -> x has value 0 at 0, and 0 has no multiplicative inverse | R arithmetic (0 * y = 0), school fact
prp-pointwise-operations (claim): {0, 1} closed under multiplication; c_1 = ind_X | arithmetic; def-indicator (Section 5.1)
prp-composition-operation (claim): (quick check) inverses of 2x + 1 | R arithmetic, school fact
prp-operation-on-quotient (claim): [9] + [3] = [0]; [2][2] = [1] in Z/3; 2y = 1 has no integer solution since 1 is odd | prp-integers-mod-n (4.2), not cited; thm-even-or-odd (F2.1 §01), not cited; arithmetic
prp-operation-on-quotient (claim): Z/n inherits identity [0], inverse [-a], identity [1]; a + (-a) = 0 | prp-congruence-arithmetic (cited); R arithmetic
exr-binary-operations-a1 (solution): Z/3 addition table; 2 - 3 not in N; 1/2 not in Z | prp-integers-mod-n (cited); arithmetic; fd5/authoring/parked/from-fd2/verify/exr-binary-operations-a1.py
exr-binary-operations-b1 (solution): polynomial expansion; inverse x/(x - 1); 1 - x*y = (1 - x)(1 - y) | R arithmetic (a field), school fact; fd5/authoring/parked/from-fd2/verify/exr-binary-operations-b1.py
exr-binary-operations-b3 (solution): real cube roots exist, cube root of x^3 is x | school fact (NOTATION sqrt[n] row: F2.1 §05-§06 use real cube roots as a school fact); fd5/authoring/parked/from-fd2/verify/exr-binary-operations-b3.py
exr-binary-operations-b3 (solution): 0 * y = 0 != 1 in R | R arithmetic, school fact
exr-binary-operations-b4 (solution): n + 1 >= 1 and p(n + 1) = n; s(0) = 1 | arithmetic; the successor map of Section 1.6 (quick check after exm-left-inverses-small-sets), named in prose, not a reason
prp-pointwise-operations (claim): the warning that f^n means the iterate | F2.6 §04 def-iterate (prose pointer, same chapter; paid)
prp-composition-operation (claim): bijections X to X are the subject of Section 5.4 | F2.6 §04 (prose pointer, same chapter; paid)
exr-binary-operations-c1 (claim): generalized associativity for n factors | not proved here; nothing depends on it (said in the solution); fd5/authoring/parked/from-fd2/verify/exr-binary-operations-c1.py checks the five bracketings on a sample associative operation
exr-binary-operations-c3 (solution): 1 - (1 - x) = x; 1 - (1 - x)(1 - x') = x + x' - xx' | R arithmetic, school fact; fd5/authoring/parked/from-fd2/verify/exr-binary-operations-c3.py
-->
