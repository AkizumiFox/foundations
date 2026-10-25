# Ordered Pairs and Products

Sections 1.2 and 1.3 built sets and combined them: a set is fixed by its elements, and \( \cup \), \( \cap \), \( \setminus \) are \( \vee \), \( \wedge \), \( \wedge\neg \) read through membership. None of this can yet say "the point \( (1, 2) \) of the plane", "\( 3 \) is less than \( 5 \)", or "\( y \) is the square of \( x \)". Each of these is about two objects **in a given order**, and a set forgets order. This section adds one new kind of object, the ordered pair (with its longer versions, the \( n \)-tuples), and then uses it twice: to build the product \( A \times B \) of two sets, and to say what a relation between two sets is. The next section needs exactly this much: a function will be given by a relation of a special kind, its graph, together with a declared target set.

## Order matters: ordered pairs

A set remembers which objects are its elements and nothing else. By extensionality (@def-set-equality), \( \{1, 2\} = \{2, 1\} \), since both sets have the elements \( 1 \) and \( 2 \); and \( \{1, 1\} = \{1\} \), since both have the element \( 1 \) and nothing else. For a set that is exactly right. For a point of the plane it is exactly wrong. The point \( (1, 2) \) lies one unit to the right of the vertical axis and two units above the horizontal one; the point \( (2, 1) \) lies elsewhere. And the point \( (1, 1) \) on the diagonal is a perfectly good point, with the same number in both places.

So we need an object built from two objects \( a \) and \( b \) that remembers **which came first**, and that still has two places when \( a = b \). What we need to know about such an object is one fact: when two of them are equal.

*An ordered pair is equal to another exactly when they agree in the first place and in the second place.*

::: {#def-ordered-pair}
[Ordered pair]

For any objects \( a \) and \( b \) there is an object \( (a, b) \), the **ordered pair** of \( a \) and \( b \); we call \( a \) its **first coordinate** and \( b \) its **second coordinate**. Ordered pairs have the **characteristic property**: for all \( a, b, c, d \),
\[
(a, b) = (c, d) \iff a = c \text{ and } b = d .
\]
:::

In words: to decide whether two pairs are equal, compare first coordinates with first coordinates and second with second; nothing else matters, and both comparisons must succeed. The direction \( (\Leftarrow) \) is nothing new: equal inputs give equal pairs, as for any construction (\( \rulename{=E} \), @fd1:def-rules-equality). The direction \( (\Rightarrow) \) is the content. It says that from the pair we can read off its coordinates, each in its place.

We do not say here **what** the object \( (a, b) \) is. Besides the characteristic property, we use one working convention: pairs and \( n \)-tuples are a different kind of object from numbers, just as sets are (Section 1.2), so **a pair is not a number**; and tuples of different lengths are different kinds of object, so a triple is not a pair. Nothing else about pairs is used in this chapter. *Number Systems: From \(\nN\) to \(\nR\)*, Chapter 1 shows that a pair with this property can be built from sets alone, so that nothing new has to be assumed. Until then, the existence of pairs with this property is taken as given, alongside the working rules (W1)–(W6) of Section 1.2.

**A convention about parentheses.** The symbol \( (a, b) \) now has two meanings. For real numbers \( a < b \) it is also the open interval \( \{ x \in \nR : a < x < b \} \). The book keeps both, and context decides, as it does in every analysis text. In "\( (0, 1) \) contains \( \tfrac{1}{2} \)" it is an interval. In "the point \( (0, 1) \) lies on the unit circle" it is a pair. Where both readings are near each other, the text says which is meant. This convention is stated once, here.

::: {#exm-pair-equations}
[Solving an equation between pairs]

Find all real numbers \( x \) and \( y \) with \( (x + y, x - y) = (3, 1) \). Then decide whether \( (1, 2) = (2, 1) \) and whether \( (1, 1) = (1, 1) \).
:::

::: {.solution}
*Uniqueness.* By the characteristic property, \( (x + y, x - y) = (3, 1) \) holds if and only if
\[
x + y = 3 \quad \text{and} \quad x - y = 1 .
\]
Adding the two equations gives \( 2x = 4 \), so \( x = 2 \); subtracting them gives \( 2y = 2 \), so \( y = 1 \). *Existence.* Conversely, \( x = 2 \) and \( y = 1 \) give \( (x + y, x - y) = (3, 1) \). So there is exactly one solution, \( x = 2 \), \( y = 1 \).

The pairs \( (1, 2) \) and \( (2, 1) \) are **not** equal. If they were, the characteristic property would give \( 1 = 2 \) for the first coordinates. So \( (1, 2) \ne (2, 1) \), by \( \rulename{\neg I} \). The same test on \( (1, 1) \) and \( (1, 1) \) passes in both places, so they are equal; and \( (1, 1) \) has two places, although both hold the same number.
:::

The first part is typical. One equation between pairs is **two** equations between coordinates, and this is how pairs are used: an equation of pairs is split by the characteristic property, and the coordinates are compared one at a time.

The solution also has a shape worth naming. "Exactly one solution" was two claims, proved separately: any solution must be \( (2, 1) \), and \( (2, 1) \) is a solution. Claims of this kind come with every "the" in a definition, so the shape gets a box.

::: {#exm-method-uniqueness}
[Method: existence and uniqueness]

**Template.** "There is exactly one \( x \) with \( P(x) \)" is two claims (@fd1:def-unique-existence, @fd1:prp-unique-existence-use). For *existence*, name a candidate \( x_0 \) and check \( P(x_0) \), or obtain one from a given "there exists". For *uniqueness*, take \( x \) and \( x' \) with \( P(x) \) and \( P(x') \), two names about which nothing else is assumed, and prove \( x = x' \); or show that every \( x \) with \( P(x) \) equals \( x_0 \).

**When to use it.** Whenever a definition says "the": the coordinates of a pair, the value \( f(x) \), the empty set (@prp-empty-set-unique), an inverse.

**The usual failure.** Proving only one half: a uniqueness proof with no candidate, or a candidate never shown to be the only one. Also checking \( P(x_0) \) twice and calling it uniqueness, and naming "the" object before either half is proved (entry (N14) of @fd1:exm-not-allowed-catalogue).
:::

::: {.check}
Is there exactly one real \( x \) with \( (x^2, x^3) = (4, -8) \)? Is there exactly one with \( (x^2, x) = (4, 3) \)?
:::

::: {.solution}
Yes for the first: \( x^3 = -8 \) forces \( x = -2 \) (uniqueness), and \( (-2)^2 = 4 \) (existence). No for the second: \( x = 3 \) is forced, but \( 3^2 = 9 \ne 4 \), so there is no such \( x \) at all. Uniqueness held and existence failed.
:::

**Nonexample by minimal change.** Replace the parentheses by braces. The set \( \{1, 2\} \) has the same two numbers as the pair \( (1, 2) \), but the characteristic property fails for sets: \( \{1, 2\} = \{2, 1\} \), and yet \( 1 \ne 2 \). What survives is membership: \( 1 \) and \( 2 \) are both in \( \{1, 2\} \). What is lost is order, the one thing the pair was made to keep.

**Why this definition.** Only \( (\Rightarrow) \) carries content. Without it, the pair could forget its coordinates, as \( \{1, 2\} \) forgets which number came first. The direction \( (\Leftarrow) \) could be dropped from the definition without loss: \( \rulename{=E} \) already gives it for \( (a, b) \), as for any construction. It is stated so that the property reads as a single test for equality of pairs.

**Longer lists.** The same idea gives ordered triples \( (a, b, c) \), and more generally ordered **\( n \)-tuples** \( (x_1, \dots, x_n) \) for \( n \in \nN \), \( n \ge 2 \). Like pairs, \( n \)-tuples are taken as given, and the \( n \)-tuples with all coordinates in a set form a set, by the working rule (W5) of Section 1.2. Two \( n \)-tuples are equal if and only if they agree in every place: \( (x_1, \dots, x_n) = (y_1, \dots, y_n) \) means \( x_k = y_k \) for every \( k \in \{1, \dots, n\} \). A triple is a new kind of object, not a pair whose first coordinate is a pair (by the convention stated after @def-ordered-pair). The pairs \( ((1, 2), 3) \) and \( (1, (2, 3)) \) carry the same three numbers in the same order, and it is tempting to call both "the triple \( (1, 2, 3) \)"; that is an identification made by convention, and exercise A1 asks whether the two pairs are equal.

::: {.check}
For which real numbers \( t \) is \( (t^2, t) = (1, -1) \)? For which is \( \{t^2, t\} = \{1, -1\} \)?
:::

::: {.solution}
The pair equation holds if and only if \( t^2 = 1 \) and \( t = -1 \), so exactly for \( t = -1 \). The set equation holds for \( t = -1 \) too, since \( \{1, -1\} = \{1, -1\} \). It holds for no other \( t \): the element \( -1 \) of the right side must be \( t^2 \) or \( t \), and \( t^2 \ge 0 \), so \( t = -1 \). Here the sets agree exactly where the pairs do, but that is luck. The pair equation \( (t, 1) = (1, t) \) holds only for \( t = 1 \), while the set equation \( \{t, 1\} = \{1, t\} \) holds for every \( t \).
:::

## Cartesian products

With pairs in hand, the plane is the set of all pairs of real numbers. More generally, from any two sets we can collect all pairs whose first coordinate comes from the first set and whose second comes from the second. Taking such a collection is the working rule (W5) of Section 1.2: it is a set.

::: {#def-cartesian-product}
[Cartesian product]

Let \( A \) and \( B \) be sets. Their **Cartesian product** is the set
\[
A \times B \coloneqq \{ (a, b) : a \in A, \ b \in B \}
\]
of all ordered pairs with first coordinate in \( A \) and second coordinate in \( B \). Written out, an object \( p \) is an element of \( A \times B \) if and only if
\[
\exists a \in A \ \exists b \in B \ \ p = (a, b) .
\]
For a set \( X \) we write \( X^2 \coloneqq X \times X \), and, for \( n \in \nN \) with \( n \ge 2 \), \( X^n \) is the set of all \( n \)-tuples \( (x_1, \dots, x_n) \) with every \( x_k \in X \).
:::

In words: an element of \( A \times B \) is **a pair**, and **there exist** coordinates, one in \( A \) and one in \( B \), from which it is made. The membership condition hides two existential quantifiers, so using it means naming the coordinates, by \( \rulename{\exists E} \) (@fd1:prp-bounded-quantifier-rules), and then matching them against any other naming by the characteristic property of pairs. That two-step move is the basic move for products; \( (\ast) \) below packages it.

For a pair the condition simplifies, and we use the simpler form constantly:
\[
(x, y) \in A \times B \iff x \in A \text{ and } y \in B . \tag{$\ast$}
\]
Here is why. If \( x \in A \) and \( y \in B \), then \( x \) and \( y \) themselves are coordinates of the required kind, and \( (x, y) \in A \times B \) by \( \rulename{\exists I} \). Conversely, let \( (x, y) \in A \times B \). Then there are \( a \in A \) and \( b \in B \) with \( (x, y) = (a, b) \) [\( \rulename{\exists E} \)], and the characteristic property (@def-ordered-pair) gives \( x = a \) and \( y = b \). So \( x \in A \) and \( y \in B \). The characteristic property is used exactly once, in the direction \( (\Rightarrow) \); without it, \( (x, y) \) might equal \( (a, b) \) with the coordinates swapped or lost, and nothing could be concluded.

We write \( (\ast) \) for this equivalence in the rest of the section. It is the reason a product is easy to work with: membership of a pair in a product is checked one coordinate at a time.

The membership condition says that an element of \( A \times B \) is made from **some** pair of coordinates. Can it be made from two different ones? The method of @exm-method-uniqueness answers this, and the answer is what lets us speak of "the first coordinate" of an element of a product.

::: {#exm-coordinates-unique}
[The coordinates of an element of a product]

Let \( p \in A \times B \). Show that there is exactly one \( a \) and exactly one \( b \) such that \( a \in A \), \( b \in B \) and \( p = (a, b) \).
:::

::: {.idea}
[Scratch work]

Existence should come straight from the definition, since membership in \( A \times B \) **is** an existence statement. For uniqueness, take two namings of \( p \) and ask what connects them. Only \( p \) itself does, so the two pairs are equal, and an equation between pairs is exactly what @def-ordered-pair splits. As givens and goal:

| Givens | Goal |
|---|---|
| \( p \in A \times B \) | some \( a \in A \), \( b \in B \) with \( p = (a, b) \); any two such agree |
| \( p = (a, b) \), \( a \in A \), \( b \in B \) (\( \rulename{\exists E} \) twice, @def-cartesian-product) | existence: done |
| \( p = (a, b) \) and \( p = (a', b') \) | \( a = a' \), \( b = b' \): the gap is \( (a, b) = (a', b') \) (\( \rulename{=E} \)), then @def-ordered-pair |

The last row is the gap. Once \( (a, b) = (a', b') \) is written down, the characteristic property closes it in one step.
:::

::: {.solution}
*Existence.* By @def-cartesian-product there are \( a \in A \) and \( b \in B \) with \( p = (a, b) \). *Uniqueness.* If also \( p = (a', b') \) with \( a' \in A \), \( b' \in B \), then \( (a, b) = p = (a', b') \), so \( a = a' \) and \( b = b' \) by the characteristic property (@def-ordered-pair).
:::

This licenses "**the** first coordinate of \( p \)", and so the assignment \( p \mapsto \) its first coordinate, which the next section will call a function.

::: {.check}
Which half of the solution used @def-cartesian-product, and which used @def-ordered-pair?
:::

::: {.solution}
Existence used @def-cartesian-product: membership in the product hands over the coordinates. Uniqueness used @def-ordered-pair: the characteristic property matches two namings of the same pair.
:::

**Set-builders with a pair pattern.** We write \( \{ (x, y) \in A \times B : P(x, y) \} \) for \( \{ p \in A \times B : \text{there are } x, y \text{ with } p = (x, y) \text{ and } P(x, y) \} \), a set-builder in the sense of @def-set-builder. By \( (\ast) \) and the characteristic property, \( (x, y) \) belongs to it if and only if \( x \in A \), \( y \in B \) and \( P(x, y) \). The notation \( \{ (a, b) : a \in A, \ b \in B \} \) in @def-cartesian-product is different: it names no ambient set, so it is not a set-builder. It is notation for the set that (W5) provides, and the displayed membership condition is its definition.

::: {#exm-small-products}
[Products, small and large]

(a) Let \( a, b, c \) be three different objects, none of them a number. List \( \{1, 2\} \times \{a, b, c\} \) and \( \{a, b, c\} \times \{1, 2\} \).

(b) Describe \( \nR^2 \) and \( [0, 1] \times [0, 1] \) as sets of points of the plane.

(c) What is \( \{1, 2\} \times \emptyset \)?
:::

::: {.solution}
(a) Each of the \( 2 \) first coordinates is paired with each of the \( 3 \) second coordinates:
\[
\{1, 2\} \times \{a, b, c\} = \{ (1, a), (1, b), (1, c), (2, a), (2, b), (2, c) \},
\]
six pairs, all different by the characteristic property, since \( 1 \ne 2 \) and \( a, b, c \) are different. Swapping the factors gives the six pairs \( (a, 1), (a, 2), (b, 1), (b, 2), (c, 1), (c, 2) \). No pair of the first list is in the second: every pair in the first list has a number as its first coordinate, and every pair in the second list has one of \( a, b, c \) there, none of which is a number; so by the characteristic property no pair of one list equals a pair of the other.

(b) \( \nR^2 = \nR \times \nR \) is the set of all pairs \( (x, y) \) of real numbers: the plane, with \( x \) the horizontal and \( y \) the vertical coordinate. By \( (\ast) \), \( (x, y) \in [0, 1] \times [0, 1] \) if and only if \( 0 \le x \le 1 \) and \( 0 \le y \le 1 \): the closed unit square, with its four sides.

(c) It is empty. An element \( p \) would be \( (a, b) \) with \( b \in \emptyset \), and \( \emptyset \) has no elements. So \( \{1, 2\} \times \emptyset \) has no elements, and a set with no elements is \( \emptyset \) (@prp-empty-set-unique).
:::

Part (c) is the degenerate case, and it matters: a product is empty as soon as **one** factor is. The general statement is part of the next proposition.

::: {.check}
List \( \{0, 1\} \times \{0, 1, 2\} \). Is \( (1, 1) \in \{1\} \times \emptyset \)?
:::

::: {.solution}
\( \{0, 1\} \times \{0, 1, 2\} = \{ (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2) \} \), six pairs. And \( (1, 1) \notin \{1\} \times \emptyset \): by \( (\ast) \) it would need \( 1 \in \emptyset \). In fact \( \{1\} \times \emptyset \) has no elements at all, as in part (c) of the example.
:::

::: {.warning}
The product is not commutative: \( A \times B \) and \( B \times A \) are in general different sets. For \( A = \{1\} \) and \( B = \{2\} \), \( A \times B = \{(1, 2)\} \) and \( B \times A = \{(2, 1)\} \), and \( (1, 2) \ne (2, 1) \) by @exm-pair-equations. The two products have "the same size", but they do not have the same elements. (They are equal when \( A = B \), and when one of the sets is empty. Exercise C2 finds exactly when even the inclusion \( A \times B \subseteq B \times A \) holds.)
:::

## Products and the set operations

Section 1.3 showed that \( \cup \), \( \cap \), and \( \setminus \) obey the laws of \( \vee \), \( \wedge \), and \( \wedge \neg \). The product interacts with them just as simply, one factor at a time. We use these laws for regions of the plane (exercise B1) and for functions out of the empty set (Section 2.1), so we state them all.

::: {#prp-product-set-laws}
[Products and Set Operations]

For all sets \( A \), \( B \), \( C \):
\[
\begin{aligned}
A \times (B \cup C) &= (A \times B) \cup (A \times C), \\
A \times (B \cap C) &= (A \times B) \cap (A \times C), \\
A \times (B \setminus C) &= (A \times B) \setminus (A \times C), \\
A \times \emptyset &= \emptyset,
\end{aligned}
\]
and the mirror-image laws, with the varying factor on the left:
\[
\begin{aligned}
(B \cup C) \times A &= (B \times A) \cup (C \times A), \\
(B \cap C) \times A &= (B \times A) \cap (C \times A), \\
(B \setminus C) \times A &= (B \times A) \setminus (C \times A), \\
\emptyset \times A &= \emptyset .
\end{aligned}
\]
:::

::: {.idea}
As in @exm-method-element-chasing, we take an element of one side and unwind; here every element is a pair, so its coordinates are named first, by \( \rulename{\exists E} \), and membership is then tested one coordinate at a time, by \( (\ast) \). The first coordinate lies in \( A \) on both sides; the second lies in \( B \cup C \) on one side and in "\( B \) or \( C \)" on the other, which is the same condition by @def-set-operations. Each law is a law of Section 1.3 in the second coordinate, with the first coordinate carried along unchanged.
:::

::: {.proof}
*The \( \cup \) law.* We prove two inclusions and conclude by @prp-subset-antisymmetric.

\( (\subseteq) \) Let \( p \in A \times (B \cup C) \). By @def-cartesian-product there are \( a \in A \) and \( d \in B \cup C \) with \( p = (a, d) \) [\( \rulename{\exists E} \) (@fd1:prp-bounded-quantifier-rules), with fresh names \( a \), \( d \)]. By @def-set-operations, \( d \in B \) or \( d \in C \), and we argue by cases. If \( d \in B \), then \( p = (a, d) \in A \times B \) by \( (\ast) \), so \( p \in (A \times B) \cup (A \times C) \). If \( d \in C \), then likewise \( p \in A \times C \subseteq (A \times B) \cup (A \times C) \). In either case \( p \in (A \times B) \cup (A \times C) \).

\( (\supseteq) \) Let \( p \in (A \times B) \cup (A \times C) \). Then \( p \in A \times B \) or \( p \in A \times C \). If \( p \in A \times B \), there are \( a \in A \) and \( b \in B \) with \( p = (a, b) \) [\( \rulename{\exists E} \)]; since \( b \in B \subseteq B \cup C \), \( (\ast) \) gives \( p \in A \times (B \cup C) \). If \( p \in A \times C \), the same argument with \( C \) in place of \( B \) gives \( p \in A \times (B \cup C) \).

*The \( \cap \) law.* Let \( p \in A \times (B \cap C) \), so \( p = (a, d) \) with \( a \in A \) and \( d \in B \cap C \). Then \( d \in B \) and \( d \in C \), and \( (\ast) \) gives \( p \in A \times B \) and \( p \in A \times C \). Conversely, let \( p \in (A \times B) \cap (A \times C) \). Since \( p \in A \times B \), \( p = (a, b) \) with \( a \in A \) and \( b \in B \). Since also \( (a, b) = p \in A \times C \), \( (\ast) \) gives \( b \in C \). So \( b \in B \cap C \), and \( p = (a, b) \in A \times (B \cap C) \).

*The \( \setminus \) law.* Let \( p \in A \times (B \setminus C) \), so \( p = (a, d) \) with \( a \in A \), \( d \in B \), and \( d \notin C \). Then \( p \in A \times B \) by \( (\ast) \). If \( p \) were in \( A \times C \), then \( (\ast) \) would give \( d \in C \), which is false; so \( p \notin A \times C \), and \( p \in (A \times B) \setminus (A \times C) \). Conversely, let \( p \in (A \times B) \setminus (A \times C) \). Then \( p = (a, b) \) with \( a \in A \) and \( b \in B \), and \( p \notin A \times C \). If \( b \) were in \( C \), then \( (\ast) \) would give \( p = (a, b) \in A \times C \), which is false; so \( b \notin C \). Hence \( b \in B \setminus C \) and \( p \in A \times (B \setminus C) \).

*The \( \emptyset \) law.* An element of \( A \times \emptyset \) would be a pair \( (a, b) \) with \( b \in \emptyset \), and there is no such \( b \). So \( A \times \emptyset \) has no elements, and it equals \( \emptyset \) by @prp-empty-set-unique.

*The mirror-image laws.* The same four arguments, with the roles of the two coordinates exchanged throughout, prove them: the varying set now sits in the first coordinate, and \( (\ast) \) is applied to it there. This proves the proposition.
:::

The proofs of the \( \setminus \) law do not use excluded middle: both "\( \notin \)" conclusions are reached by assuming membership and deriving a contradiction, which is \( \rulename{\neg I} \). Only the first law was written with every \( \rulename{\exists E} \) marked; from here on, "\( p = (a, b) \) with \( a \in A \) and \( b \in B \)" is understood to name fresh coordinates.

A proof about products usually runs like the one above: take an element, write it as a pair with named coordinates, and work coordinatewise. Here is the pattern on concrete sets.

::: {#exm-product-of-intervals}
[Two rectangles]

Show that \( ([0, 2] \times [0, 1]) \cap ([1, 3] \times [0, 2]) = [1, 2] \times [0, 1] \).
:::

::: {.solution}
Draw the two rectangles first: the first is \( 2 \) wide and \( 1 \) high, with its lower left corner at the origin; the second is \( 2 \) wide and \( 2 \) high, with its lower left corner at \( (1, 0) \). They overlap in the rectangle over \( [1, 2] \) of height \( 1 \). Now the proof, by two inclusions.

\( (\subseteq) \) Let \( p \) be in the intersection. Since \( p \in [0, 2] \times [0, 1] \), \( p = (x, y) \) with \( 0 \le x \le 2 \) and \( 0 \le y \le 1 \). Since also \( (x, y) = p \in [1, 3] \times [0, 2] \), \( (\ast) \) gives \( 1 \le x \le 3 \) and \( 0 \le y \le 2 \). Together, \( 1 \le x \le 2 \) and \( 0 \le y \le 1 \), so \( p = (x, y) \in [1, 2] \times [0, 1] \) by \( (\ast) \).

\( (\supseteq) \) Let \( p \in [1, 2] \times [0, 1] \), so \( p = (x, y) \) with \( 1 \le x \le 2 \) and \( 0 \le y \le 1 \). Then \( 0 \le x \le 2 \), so \( p \in [0, 2] \times [0, 1] \); and \( 1 \le x \le 3 \), \( 0 \le y \le 2 \), so \( p \in [1, 3] \times [0, 2] \). Hence \( p \) is in the intersection.

By @prp-subset-antisymmetric, the two sets are equal. The picture found the answer; the element-chase proved it.
:::

The degenerate law of the proposition deserves a second look, because it is easy to misuse.

::: {.remark}
Combining the two \( \emptyset \) laws with one more step gives the full description of an empty product: \( A \times B = \emptyset \) **if and only if** \( A = \emptyset \) or \( B = \emptyset \). The direction \( (\Leftarrow) \) is the pair of \( \emptyset \) laws. For \( (\Rightarrow) \), suppose \( A \times B = \emptyset \). If \( A \) has an element \( a \) and \( B \) has an element \( b \), then \( (a, b) \in A \times B = \emptyset \), which is impossible. So it is not the case that both sets have an element; by excluded middle (@fd1:prp-excluded-middle) applied to "\( A \) has an element", either \( A \) has none, and then \( A = \emptyset \) by @prp-empty-set-unique, or \( A \) has one, and then \( B \) has none, so \( B = \emptyset \).
:::

::: {.warning}
"\( A \times B = \emptyset \), so \( A = \emptyset \)" misses a case. The product \( \{1, 2\} \times \emptyset \) is empty, and \( \{1, 2\} \) is not. The correct conclusion is the disjunction "\( A = \emptyset \) or \( B = \emptyset \)" of the remark, and an argument that continues from it must treat both cases. Dropping one is the missing case of the catalogue in *Logic and Proof*, Chapter 8, entry (N7): a \( \rulename{\vee E} \) with one of its boxes left out.
:::

## Relations

"Is less than", "divides", "is the square of", "lies on the unit circle with": each of these connects an object of one set with an object of another, or of the same set. Each can be described by a rule, a formula, or a sentence. But two different descriptions can pick out exactly the same connections: "\( x < y \)" and "\( y - x > 0 \)" are different sentences about real numbers, and they hold for exactly the same pairs \( (x, y) \). In mathematics we want these to count as the **same** relation.

The way to make them the same is to forget the description and keep what it picks out: the set of pairs \( (x, y) \) for which it holds. Two descriptions that pick out the same pairs then give the same set, by extensionality.

*A relation is the set of pairs it relates.*

::: {#def-relation}
[Relation]

Let \( A \) and \( B \) be sets. A **relation from \( A \) to \( B \)** is a subset \( R \subseteq A \times B \). For \( a \in A \) and \( b \in B \) we write \( a \mathrel{R} b \), read "\( a \) is \( R \)-related to \( b \)", to mean \( (a, b) \in R \). A **relation on \( A \)** is a relation from \( A \) to \( A \), that is, a subset of \( A^2 \).

The **domain** of \( R \) is the set of first coordinates that occur, \( \{ a \in A : \exists b \in B \ \ a \mathrel{R} b \} \), and its **range** is the set of second coordinates that occur, \( \{ b \in B : \exists a \in A \ \ a \mathrel{R} b \} \). Turning every pair of \( R \) around gives a relation from \( B \) to \( A \), the **inverse relation**
\[
R^{-1} \coloneqq \{ (b, a) \in B \times A : (a, b) \in R \} .
\]
:::

In words: a relation **is** a set, namely a set of pairs whose coordinates come from the two given sets. The notation \( a \mathrel{R} b \) is only a way of writing "\( (a, b) \in R \)" that reads like "\( a < b \)". The domain collects the elements of \( A \) that are related to **at least one** element of \( B \); the range collects those of \( B \) that something is related to. The inverse relation turns each pair around: \( b \mathrel{R^{-1}} a \) exactly when \( a \mathrel{R} b \).

Two relations are equal exactly when they relate the same pairs, since relations are sets (@def-set-equality). So the relation "\( x < y \)" on \( \nR \) and the relation "\( y - x > 0 \)" on \( \nR \) are one relation, as we wanted. That is the whole reason for the definition: a relation is determined by **what** it relates, not by **how** it is described.

::: {#exm-relations-as-sets}
[Relations as sets of pairs]

Write each relation as a set, and find its domain and range.

(a) The relation \( < \) on \( \{1, 2, 3\} \).

(b) Divisibility on \( \{1, \dots, 6\} \): \( a \mathrel{D} b \) when \( a \mid b \).

(c) The unit circle, as a relation on \( \nR \).

(d) The graph of squaring, as a relation on \( \nR \).

(e) The two extreme relations from \( A \) to \( B \): \( \emptyset \) and \( A \times B \).
:::

::: {.solution}
(a) The pairs \( (a, b) \) of elements of \( \{1, 2, 3\} \) with \( a < b \) are
\[
L \coloneqq \{ (1, 2), (1, 3), (2, 3) \} ,
\]
three of the nine elements of \( \{1, 2, 3\}^2 \). Its domain is \( \{1, 2\} \), since nothing in the set is larger than \( 3 \); its range is \( \{2, 3\} \), since nothing is smaller than \( 1 \).

(b) Write \( a \mid b \) when \( b = ak \) for some integer \( k \). For each first coordinate \( a \), the second coordinates \( b \in \{1, \dots, 6\} \) with \( a \mid b \) are the multiples of \( a \) up to \( 6 \):

| \( a \) | the \( b \in \{1, \dots, 6\} \) with \( a \mid b \) |
|---|---|
| \( 1 \) | \( 1, 2, 3, 4, 5, 6 \) |
| \( 2 \) | \( 2, 4, 6 \) |
| \( 3 \) | \( 3, 6 \) |
| \( 4 \) | \( 4 \) |
| \( 5 \) | \( 5 \) |
| \( 6 \) | \( 6 \) |

So \( D \) has \( 6 + 3 + 2 + 1 + 1 + 1 = 14 \) elements, the pairs \( (a, b) \) read off the rows. Its domain and range are both all of \( \{1, \dots, 6\} \), because every \( a \) divides itself: \( (a, a) \in D \).

(c) The unit circle is
\[
S \coloneqq \{ (x, y) \in \nR^2 : x^2 + y^2 = 1 \} ,
\]
a relation on \( \nR \); for instance \( 0 \mathrel{S} 1 \), \( 0 \mathrel{S} (-1) \), and \( 1 \mathrel{S} 0 \). Its domain is \( [-1, 1] \). If \( x \mathrel{S} y \), then \( x^2 = 1 - y^2 \le 1 \), so \( -1 \le x \le 1 \). Conversely, for \( -1 \le x \le 1 \) the number \( 1 - x^2 \) is nonnegative and so has a square root \( y = \sqrt{1 - x^2} \), which satisfies \( x^2 + y^2 = 1 \). By the symmetry of the equation, the range is \( [-1, 1] \) too.

(d) The graph of squaring is \( Q \coloneqq \{ (x, y) \in \nR^2 : y = x^2 \} \). Its domain is all of \( \nR \): every \( x \) is related to \( x^2 \). Its range is \( [0, \infty) \): a square is nonnegative, and every \( y \ge 0 \) is the square of \( \sqrt{y} \).

(e) Both are subsets of \( A \times B \), so both are relations. The **empty relation** \( \emptyset \) relates nothing, and its domain and range are empty. The **full relation** \( A \times B \) relates everything to everything. If \( A \) and \( B \) both have elements, its domain is \( A \) and its range is \( B \).
:::

The circle and the graph of squaring look alike, both being curves in the plane, but they differ in a way that the next section makes precise. In \( Q \) every \( x \) is related to **exactly one** \( y \). In \( S \) the number \( 0 \) is related to two numbers, \( 1 \) and \( -1 \), and the number \( 2 \) to none. A relation of the first kind will be the graph of a function.

::: {.check}
Write the inverse relation \( L^{-1} \) of part (a) as a set. Which familiar relation on \( \{1, 2, 3\} \) is it?
:::

::: {.solution}
Turning each pair of \( L \) around gives \( L^{-1} = \{ (2, 1), (3, 1), (3, 2) \} \): the pairs \( (b, a) \) with \( b > a \). So \( L^{-1} \) is the relation \( > \) on \( \{1, 2, 3\} \). Its domain \( \{2, 3\} \) is the range of \( L \), and its range \( \{1, 2\} \) is the domain of \( L \).
:::

**Nonexample by minimal change.** The set \( \{ (1, 2), (2, 3), 3 \} \) looks like the relation "is one less than" on \( \{1, 2, 3\} \), with one pair damaged. It is not a relation on \( \{1, 2, 3\} \): the element \( 3 \) is a number, not a pair (the convention after @def-ordered-pair), so the set is not a subset of \( \{1, 2, 3\}^2 \). Remove the \( 3 \), or replace it by the pair \( (3, 4) \) and enlarge the second set to \( \{1, 2, 3, 4\} \), and it becomes a relation. The clause that failed is "\( R \subseteq A \times B \)": every element of a relation must be a pair with coordinates in the right sets.

**Why this definition.** A relation could be defined as a rule, a sentence, or a formula. Each of those raises the question of when two rules are "the same", and that question has no good answer: "\( x < y \)" and "\( y - x > 0 \)" are different sentences. The definition as a set answers it by extensionality. The price is small: a relation may be any set of pairs whatever, such as \( \{ (1, 3), (2, 2) \} \) on \( \{1, 2, 3\} \), and the definition never asks for a rule that produces it. That is a gain, not a loss: in analysis we meet relations and functions that no formula describes.

::: {.warning}
A relation "from \( A \) to \( B \)" has its direction built in: \( R \subseteq A \times B \), and the first coordinate comes from \( A \). The relation \( L \) of part (a) contains \( (1, 2) \) and not \( (2, 1) \). Reading a relation backwards, "since \( 1 \mathrel{L} 2 \), also \( 2 \mathrel{L} 1 \)", treats it as a symmetric relation; relations with that property, and other properties such as transitivity, are studied in Chapter 5. Relating \( b \) to \( a \) is the job of the inverse relation \( R^{-1} \), a different set.
:::

This definition is all the next section needs. The graph of a function from \( X \) to \( Y \) will be a relation from \( X \) to \( Y \) in which every element of \( X \) is related to exactly one element of \( Y \); the function is that graph together with the declared codomain \( Y \). The graph \( Q \) qualifies and the circle \( S \) does not. The properties that make a relation an order or an equivalence (reflexive, symmetric, antisymmetric, transitive) are the subject of Chapter 5.

## Exercises

### A. Check your understanding

::: {#exr-products-and-relations-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define \( A \times B \) in symbols, with its membership condition written out using quantifiers.
2. Is \( ((1, 2), 3) = (1, (2, 3)) \)? Justify your answer.
3. Write the inverse of the relation \( < \) on \( \{1, 2, 3\} \) as a set of pairs.
4. Is \( \emptyset \) a relation on every set \( A \)? Justify your answer.
:::
:::

::: {.solution}
(a) \( A \times B = \{ (a, b) : a \in A, \ b \in B \} \); that is, \( p \in A \times B \) if and only if \( \exists a \in A \ \exists b \in B \ \ p = (a, b) \) (@def-cartesian-product).

(b) No. Both are ordered pairs, so by the characteristic property (@def-ordered-pair) they are equal if and only if their first coordinates are equal and their second coordinates are equal. The first coordinates are the pair \( (1, 2) \) and the number \( 1 \). A pair is not a number, by the working convention stated after @def-ordered-pair (*Number Systems: From \(\nN\) to \(\nR\)*, Chapter 1, which builds both from sets, bears it out). So the first coordinates differ, and the pairs are not equal. Calling both "the triple \( (1, 2, 3) \)" is an identification made by convention, not an equality.

(c) \( \{ (2, 1), (3, 1), (3, 2) \} \), which is the relation \( > \) on \( \{1, 2, 3\} \).

(d) Yes. A relation on \( A \) is a subset of \( A \times A \), and \( \emptyset \subseteq A \times A \): the condition "\( x \in \emptyset \to x \in A \times A \)" holds for every \( x \), because its hypothesis is false (@fd1:prp-vacuous-implication, @def-subset).
:::

### B. Practice

::: {#exr-products-and-relations-b1}
[B1: An L-shaped region]

Let \( E \coloneqq ([0, 1] \times [0, 2]) \cup ([1, 2] \times [0, 1]) \). Describe \( E \) as a region of the plane. Then use @prp-product-set-laws to write \( E \) as \( ([0, 2] \times [0, 1]) \cup (P \times Q) \) for intervals \( P \) and \( Q \), and prove the equality.
:::

::: {.solution}
The first rectangle is \( 1 \) wide and \( 2 \) high, standing on the origin; the second is \( 1 \) wide and \( 1 \) high, standing on \( [1, 2] \). Together they form an "L": a bottom strip \( [0, 2] \times [0, 1] \) of width \( 2 \), with a square \( [0, 1] \times [1, 2] \) on top of its left half. So we expect \( P = [0, 1] \) and \( Q = [1, 2] \).

Now the proof. Since \( [0, 2] = [0, 1] \cup [1, 2] \), the first law of @prp-product-set-laws gives
\[
[0, 1] \times [0, 2] = ([0, 1] \times [0, 1]) \cup ([0, 1] \times [1, 2]) ,
\]
and the mirror-image \( \cup \) law gives
\[
[0, 2] \times [0, 1] = ([0, 1] \times [0, 1]) \cup ([1, 2] \times [0, 1]) .
\]
Substituting the first equation into the definition of \( E \) and regrouping the unions (\( \cup \) is commutative and associative by @thm-set-algebra),
\[
\begin{aligned}
E &= ([0, 1] \times [0, 1]) \cup ([0, 1] \times [1, 2]) \cup ([1, 2] \times [0, 1]) \\
  &= ([0, 2] \times [0, 1]) \cup ([0, 1] \times [1, 2]),
\end{aligned}
\]
where the second line uses the mirror-image equation. So \( P = [0, 1] \) and \( Q = [1, 2] \). (The equality \( [0, 2] = [0, 1] \cup [1, 2] \) is an order fact: \( 0 \le x \le 2 \) holds exactly when \( 0 \le x \le 1 \) or \( 1 \le x \le 2 \).)
:::

::: {#exr-products-and-relations-b2}
[B2: The intersection law, written with two pairs]

Here is a proof of the inclusion \( (\supseteq) \) of \( A \times (B \cap C) = (A \times B) \cap (A \times C) \) that works from the definition of the product and the characteristic property directly, without the shortcut \( (\ast) \). Its last sentence is blank. *Name the move, then complete it.*

> Let \( p \in (A \times B) \cap (A \times C) \). Since \( p \in A \times B \), there are \( a \in A \) and \( b \in B \) with \( p = (a, b) \). Since \( p \in A \times C \), there are \( a' \in A \) and \( c \in C \) with \( p = (a', c) \); the names \( a' \) and \( c \) are new, because nothing says that this second pair of coordinates is the first one again. Hence \( (a, b) = (a', c) \). \( \underline{\hspace{8em}} \)
:::

::: {.solution}
The move is the second half of the section's move, the characteristic property of pairs (@def-ordered-pair) in the direction \( (\Rightarrow) \). An equation between pairs splits into equations between coordinates.

The completed last sentence: *By the characteristic property, \( a = a' \) and \( b = c \); so \( b \in B \) and \( b = c \in C \), hence \( b \in B \cap C \), and \( p = (a, b) \in A \times (B \cap C) \).*

The names \( a' \) and \( c \) had to be fresh (a second \( \rulename{\exists E} \) may not reuse the names of the first), and the characteristic property is what shows, afterwards, that the two namings name the same coordinates. The proof of @prp-product-set-laws took the same step through \( (\ast) \), which packages exactly this use of the characteristic property.
:::

::: {#exr-products-and-relations-b3}
[B3: Two products crossed]

Prove that \( (A \times B) \cap (B \times A) = (A \cap B) \times (A \cap B) \) for all sets \( A \) and \( B \).
:::

::: {.solution}
We prove two inclusions and conclude by @prp-subset-antisymmetric.

\( (\subseteq) \) Let \( p \in (A \times B) \cap (B \times A) \). Since \( p \in A \times B \), \( p = (x, y) \) with \( x \in A \) and \( y \in B \). Since also \( (x, y) = p \in B \times A \), \( (\ast) \) gives \( x \in B \) and \( y \in A \). So \( x \in A \cap B \) and \( y \in A \cap B \), and \( p = (x, y) \in (A \cap B) \times (A \cap B) \) by \( (\ast) \).

\( (\supseteq) \) Let \( p \in (A \cap B) \times (A \cap B) \), so \( p = (x, y) \) with \( x, y \in A \cap B \). Then \( x \in A \) and \( y \in B \), so \( p \in A \times B \); and \( x \in B \) and \( y \in A \), so \( p \in B \times A \). Hence \( p \in (A \times B) \cap (B \times A) \).
:::

::: {#exr-products-and-relations-b4}
[B4: Prove or disprove]

Prove each true statement by the method of @exm-method-uniqueness, or the section's element arguments, and refute each false one with a concrete counterexample.

::: {.enumerate options="label=(\alph*)"}
1. For all real \( a \) and \( b \) there is exactly one pair \( (x, y) \) of real numbers with \( (3x - y, x + 2y) = (a, b) \).
2. For every real \( a \) there is exactly one pair \( (x, y) \) of real numbers with \( (x^2, y) = (a, 0) \).
3. For all sets \( A \), \( B \), \( C \): if \( A \times B = A \times C \), then \( B = C \).
4. For all sets \( A \), \( B \), \( C \) such that \( A \) has an element: if \( A \times B = A \times C \), then \( B = C \).
5. There is exactly one set \( E \) with \( E \times E = \emptyset \).
:::
:::

::: {.solution}
(a) **True.** *Uniqueness.* Let \( (x, y) \) be a solution. By the characteristic property (@def-ordered-pair), \( 3x - y = a \) and \( x + 2y = b \). The first equation gives \( y = 3x - a \), and then \( x + 2(3x - a) = b \), so \( 7x = 2a + b \). Hence \( x = (2a + b)/7 \) and \( y = 3x - a = (3b - a)/7 \). *Existence.* For these values,
\[
3 \cdot \frac{2a + b}{7} - \frac{3b - a}{7} = \frac{7a}{7} = a, \qquad \frac{2a + b}{7} + 2 \cdot \frac{3b - a}{7} = \frac{7b}{7} = b ,
\]
so \( (3x - y, x + 2y) = (a, b) \).

(b) **False.** For \( a = 1 \), both \( (1, 0) \) and \( (-1, 0) \) qualify, since \( 1^2 = (-1)^2 = 1 \), and they are different pairs because \( 1 \ne -1 \). (For \( a = -1 \) there is no pair at all; one failing \( a \) is enough.)

(c) **False.** Take \( A = \emptyset \), \( B = \{1\} \), \( C = \{2\} \). Both products are \( \emptyset \) by @prp-product-set-laws, so \( A \times B = A \times C \), but \( B \ne C \).

(d) **True.** Let \( a \) be an element of \( A \), and suppose \( A \times B = A \times C \). For \( b \in B \), \( (a, b) \in A \times B = A \times C \) by \( (\ast) \), so \( b \in C \) by \( (\ast) \) again. Hence \( B \subseteq C \), and the other inclusion is the same argument with \( B \) and \( C \) exchanged. So \( B = C \) by @prp-subset-antisymmetric. Part (c) shows where the element \( a \) was needed.

(e) **True.** *Existence.* \( \emptyset \times \emptyset = \emptyset \), by the \( \emptyset \) law of @prp-product-set-laws. *Uniqueness.* Let \( E \times E = \emptyset \). If \( e \in E \), then \( (e, e) \in E \times E = \emptyset \) by \( (\ast) \), which is impossible; so \( E \) has no elements, and \( E = \emptyset \) by @prp-empty-set-unique.
:::

### C. Going deeper

::: {#exr-products-and-relations-c1}
[C1: The square of a union]

::: {.enumerate options="label=(\alph*)"}
1. Determine whether \( (A \cup B) \times (A \cup B) = (A \times A) \cup (B \times B) \) for all sets \( A \) and \( B \). Justify your answer.
2. Prove the inclusion \( (A \times A) \cup (B \times B) \subseteq (A \cup B) \times (A \cup B) \).
3. Prove, from @prp-product-set-laws, that
\[
(A \cup B) \times (A \cup B) = (A \times A) \cup (A \times B) \cup (B \times A) \cup (B \times B) .
\]
:::
:::

::: {.solution}
(a) No. Take \( A = \{1\} \) and \( B = \{2\} \). Then \( (1, 2) \in \{1, 2\} \times \{1, 2\} = (A \cup B) \times (A \cup B) \). But \( (A \times A) \cup (B \times B) = \{ (1, 1), (2, 2) \} \), and \( (1, 2) \) is neither \( (1, 1) \) nor \( (2, 2) \), since in each case the second (or first) coordinates differ. So the two sets are different.

(b) Let \( p \in (A \times A) \cup (B \times B) \). If \( p \in A \times A \), then \( p = (x, y) \) with \( x, y \in A \); so \( x, y \in A \cup B \), and \( p \in (A \cup B) \times (A \cup B) \) by \( (\ast) \). If \( p \in B \times B \), the same argument with \( B \) in place of \( A \) applies. In either case \( p \in (A \cup B) \times (A \cup B) \).

(c) The mirror-image \( \cup \) law, with \( A \cup B \) as the fixed factor on the right, gives
\[
(A \cup B) \times (A \cup B) = \bigl(A \times (A \cup B)\bigr) \cup \bigl(B \times (A \cup B)\bigr) .
\]
The first \( \cup \) law, applied to each of the two products, gives
\[
A \times (A \cup B) = (A \times A) \cup (A \times B), \qquad B \times (A \cup B) = (B \times A) \cup (B \times B) .
\]
Substituting, and using that \( \cup \) is associative (@thm-set-algebra), so that no brackets are needed, gives the formula. Part (a)'s counterexample is the term \( A \times B \) at work: \( (1, 2) \in A \times B \).
:::

::: {#exr-products-and-relations-c2}
[C2: When one inclusion forces equality]

Let \( A \) and \( B \) be sets. Prove that \( A \times B \subseteq B \times A \) if and only if \( A = B \) or \( A = \emptyset \) or \( B = \emptyset \).
:::

::: {.solution}
[Hint 1]

For \( (\Rightarrow) \), the empty cases are easy, so assume both sets have elements. To show \( A \subseteq B \), you need to test an element \( a \in A \); put it into a pair that is sure to lie in \( A \times B \).
:::

::: {.solution}
[Hint 2]

Fix \( b_0 \in B \). For \( a \in A \), the pair \( (a, b_0) \) lies in \( A \times B \).
:::

::: {.solution}
\( (\Leftarrow) \) If \( A = B \), then \( A \times B = B \times A \), and in particular \( A \times B \subseteq B \times A \). If \( A = \emptyset \), then \( A \times B = \emptyset \) by @prp-product-set-laws, and \( \emptyset \) is a subset of every set. If \( B = \emptyset \), likewise \( A \times B = A \times \emptyset = \emptyset \).

\( (\Rightarrow) \) Suppose \( A \times B \subseteq B \times A \). By excluded middle (@fd1:prp-excluded-middle), each of \( A \) and \( B \) either has an element or has none, and a set with no elements is \( \emptyset \) (@prp-empty-set-unique). If \( A = \emptyset \) or \( B = \emptyset \), we are done. In the remaining case both have elements: fix \( a_0 \in A \) and \( b_0 \in B \) (\( \rulename{\exists E} \) twice, with fresh names).

*\( A \subseteq B \).* Let \( a \in A \). Then \( (a, b_0) \in A \times B \) by \( (\ast) \), so \( (a, b_0) \in B \times A \) by the hypothesis. By \( (\ast) \) again, \( a \in B \) (and \( b_0 \in A \)).

*\( B \subseteq A \).* Let \( b \in B \). Then \( (a_0, b) \in A \times B \subseteq B \times A \), and \( (\ast) \) gives \( b \in A \) (and \( a_0 \in B \)).

By @prp-subset-antisymmetric, \( A = B \). This proves the equivalence.

Both witnesses are needed. With \( B = \emptyset \) there is no \( b_0 \), and indeed then \( A \times B \subseteq B \times A \) holds for every \( A \), including \( A \ne B \): the inclusion \( \{1\} \times \emptyset \subseteq \emptyset \times \{1\} \) is \( \emptyset \subseteq \emptyset \).

**Marking scheme.** (10 points)
- 2: \( (\Leftarrow) \): all three cases, including that an empty factor makes \( A \times B \) empty and hence a subset of anything.
- 2: \( (\Rightarrow) \): splits off the empty cases and, in the remaining case, names witnesses \( a_0 \in A \) and \( b_0 \in B \).
- 2: \( A \subseteq B \), through a pair \( (a, b_0) \) with an arbitrary \( a \in A \).
- 2: \( B \subseteq A \), through a pair \( (a_0, b) \) with an arbitrary \( b \in B \).
- 2: uses the characteristic property (directly or through \( (\ast) \)) to read the coordinates off a pair of \( B \times A \), and concludes \( A = B \) by two inclusions.

Fatal errors (0 for the step): testing inclusion on particular elements only (entry (N1) of *Logic and Proof*, Chapter 8's catalogue); using \( b_0 \) without having shown that \( B \) has an element; concluding \( A = B \) from \( A \times B = B \times A \) "by canceling" without an element argument.
A proof of \( (\Rightarrow) \) by contraposition (assume \( A \ne B \) and both nonempty, and exhibit a pair of \( A \times B \) outside \( B \times A \)) earns full marks if it finds the pair: 2 points for the witnesses and 4 for the pair and the check that it is outside \( B \times A \), in place of the two inclusions.
:::

### R. Review

::: {#exr-images-and-preimages-r1}
[R1]

Here is a derivation of "if \( A \subseteq B \), then \( \powerset{A} \subseteq \powerset{B} \)". The steps "by def." unwind or rewind @def-subset and @def-power-set.

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {A \subseteq B}
  \have {2} {\forall x (x \in A \to x \in B)} \by{def.}{1}
  \open[S_0]
  \open
  \hypo {3} {S_0 \in \powerset{A}}
  \have {4} {S_0 \subseteq A} \by{def.}{3}
  \have {5} {\forall x (x \in S_0 \to x \in A)} \by{def.}{4}
  \open[x_0]
  \open
  \hypo {6} {x_0 \in S_0}
  \have {7} {x_0 \in S_0 \to x_0 \in A} \Ae{5}
  \have {8} {x_0 \in A} \ie{7,6}
  \have {9} {x_0 \in A \to x_0 \in B} \Ae{2}
  \have {10} {x_0 \in B} \ie{9,8}
  \close
  \have {11} {x_0 \in S_0 \to x_0 \in B} \ii{6-10}
  \close
  \have {12} {\forall x (x \in S_0 \to x \in B)} \Ai{6-11}
  \have {13} {S_0 \subseteq B} \by{def.}{12}
  \have {14} {S_0 \in \powerset{B}} \by{def.}{13}
  \close
  \have {15} {S_0 \in \powerset{A} \to S_0 \in \powerset{B}} \ii{3-14}
  \close
  \have {16} {\forall S (S \in \powerset{A} \to S \in \powerset{B})} \Ai{3-15}
  \have {17} {\powerset{A} \subseteq \powerset{B}} \by{def.}{16}
  \close
  \have {18} {A \subseteq B \to \powerset{A} \subseteq \powerset{B}} \ii{1-17}
\end{nd}$
\end{center}
```

Write the proof as plain prose, the way a mathematician would. Then say which sentence of your proof carries each of the five boxes.
:::

::: {.solution}
*Proof.* Suppose \( A \subseteq B \). Let \( S \in \powerset{A} \), so \( S \subseteq A \). Let \( x \in S \). Then \( x \in A \), since \( S \subseteq A \), and so \( x \in B \), since \( A \subseteq B \). Hence \( S \subseteq B \), that is, \( S \in \powerset{B} \). This proves \( \powerset{A} \subseteq \powerset{B} \).

*The boxes.* "Suppose \( A \subseteq B \)" opens the \( \rulename{{\to}I} \) box \( \lines{1}{17} \); its closing line 18 is the silent frame of the whole proof. "Let \( S \in \powerset{A} \)" opens two boxes at once: the \( \rulename{\forall I} \) box for \( S_0 \) and the \( \rulename{{\to}I} \) box \( \lines{3}{14} \) inside it. "Let \( x \in S \)" likewise opens the \( \rulename{\forall I} \) box for \( x_0 \) and the \( \rulename{{\to}I} \) box \( \lines{6}{10} \). "Hence \( S \subseteq B \)" closes the two inner boxes (lines 11 and 12) and rewinds the definition (line 13). "This proves \( \powerset{A} \subseteq \powerset{B} \)" closes the \( S \) boxes (lines 15, 16) and rewinds (line 17).

This is the passage from level 0 to level 3 of @fd1:def-levels-of-proof (*Logic and Proof*, Section 8.3): each "let" carries a \( \rulename{\forall I} \) box together with the \( \rulename{{\to}I} \) box of a subset statement, the \( \rulename{\forall E} \) and \( \rulename{{\to}E} \) lines 7–10 become the two "since" clauses, the unwinding lines 2 and 5 go silent, line 4 becomes a "so" and line 14 a "that is", and the rewinding lines 13 and 17 are the two conclusions the prose states.

Lines 5–13, with line 2, are the proof of @prp-subset-transitive, done again inside this one. A level-3 proof that may cite it is shorter: if \( S \subseteq A \), then \( S \subseteq B \) by @prp-subset-transitive, so \( S \in \powerset{B} \).
:::

::: {#exr-images-and-preimages-r2}
[R2]

Decide whether \( A \setminus (B \setminus C) = (A \setminus B) \setminus C \) for all sets \( A, B, C \), by a table of the eight possible memberships of a point \( x \) in \( A \), \( B \), \( C \). If the two sides can differ, turn a row where they differ into a counterexample.
:::

::: {.solution}
Write \( P \), \( Q \), \( R \) for the statements \( x \in A \), \( x \in B \), \( x \in C \). By @def-set-operations, \( x \in A \setminus (B \setminus C) \) is \( P \wedge \neg(Q \wedge \neg R) \), and \( x \in (A \setminus B) \setminus C \) is \( (P \wedge \neg Q) \wedge \neg R \). The table:
\[
\begin{array}{ccc|cc}
P & Q & R & P \wedge \neg (Q \wedge \neg R) & (P \wedge \neg Q) \wedge \neg R \\
\hline
\mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{F} \\
\mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} \\
\mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} \\
\mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} \\
\mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} \\
\end{array}
\]
The columns differ in the first and third rows. Take the first row: put the point \( 1 \) in exactly the sets whose statement is true, all three, so \( A = B = C = \{1\} \). Then \( B \setminus C = \emptyset \), so \( A \setminus (B \setminus C) = \{1\} \); and \( A \setminus B = \emptyset \), so \( (A \setminus B) \setminus C = \emptyset \). The two sides differ, so the identity is false. (The third row gives \( A = C = \{1\} \), \( B = \emptyset \), with the same two answers.)

Why a table suffices: each side's membership condition is a formula in \( P \), \( Q \), \( R \), and a row with the two columns different gives sets directly, which are then checked by computing both sides, as above. The truth tables of *Logic and Proof*, Chapter 4 add one more thing: by @fd1:cor-refuting-row, the first row shows that the sequent \( P \wedge \neg(Q \wedge \neg R) \vdash (P \wedge \neg Q) \wedge \neg R \) is not derivable, so the propositional rules cannot carry a point of the left side into the right side.
:::

::: {#exr-images-and-preimages-r3}
[R3]

Derive \( (P \wedge \neg Q) \to R \vdash P \to (Q \vee R) \). Then read the derivation as a proof that for sets \( A, B, C \), if \( A \setminus B \subseteq C \), then \( A \subseteq B \cup C \). Which step is classical?
:::

::: {.solution}
The goal is an implication, so open a box on \( P \) with goal \( Q \vee R \). The premise can fire only on \( P \wedge \neg Q \), which needs \( \neg Q \), and nothing gives \( \neg Q \) outright. So split on \( Q \vee \neg Q \), by excluded middle (@fd1:prp-excluded-middle): in the case \( Q \) the goal is immediate, and in the case \( \neg Q \) the premise gives \( R \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge \neg Q) \to R}
  \open
  \hypo {2} {P}
  \have {3} {Q \vee \neg Q} \lem{}
  \open
  \hypo {4} {Q}
  \have {5} {Q \vee R} \oi{4}
  \close
  \open
  \hypo {6} {\neg Q}
  \have {7} {P \wedge \neg Q} \ai{2,6}
  \have {8} {R} \ie{1,7}
  \have {9} {Q \vee R} \oi{8}
  \close
  \have {10} {Q \vee R} \oe{3,4-5,6-9}
  \close
  \have {11} {P \to (Q \vee R)} \ii{2-10}
\end{nd}$
\end{center}
```

*As sets.* Suppose \( A \setminus B \subseteq C \), and let \( x \in A \). Take \( P \), \( Q \), \( R \) to be \( x \in A \), \( x \in B \), \( x \in C \). By @def-subset and @def-set-operations, the hypothesis at this \( x \) is \( (P \wedge \neg Q) \to R \), and the goal \( x \in B \cup C \) is \( Q \vee R \). The derivation, used as a derived rule (@fd1:def-derived-rule), gives \( P \to (Q \vee R) \), and with \( P \) it gives \( x \in B \cup C \). In prose: either \( x \in B \), and then \( x \in B \cup C \); or \( x \notin B \), and then \( x \in A \setminus B \subseteq C \), so \( x \in C \subseteq B \cup C \). Since \( x \) was arbitrary, \( A \subseteq B \cup C \).

The classical step is line 3, the case split "\( x \in B \) or \( x \notin B \)" by excluded middle, which is derived with \( \rulename{RAA} \) (@fd1:def-rule-raa).
:::

::: {#exr-images-and-preimages-r4}
[R4]

Show that there is no set that contains every singleton \( \{x\} \) as an element.
:::

::: {.solution}
Suppose \( S \) were such a set. Let \( T \coloneqq \{ s \in S : s \text{ is a singleton} \} \), a set by specification (@def-set-builder); its elements are sets, since \( S \) may also contain numbers, and those are excluded. Consider the union \( \bigcup T \) of the sets in \( T \) (@def-family-union-intersection, the form \( \bigcup \sS \) for a set \( \sS \) whose elements are sets). For every set \( x \), the singleton \( \{x\} \) lies in \( S \), hence in \( T \), and \( x \in \{x\} \); so \( x \in \bigcup T \). Thus \( \bigcup T \) is a set of which every set is an element, and @thm-russell says there is no such set. This contradiction shows that no such \( S \) exists.

*The tool, and the look-alike.* The tool is Russell's theorem, @thm-russell, applied not to \( S \) but to \( \bigcup T \). Applied to \( S \) directly, it says only that \( \{ z \in S : z \notin z \} \notin S \), and that does not contradict anything: \( S \) was supposed to contain singletons, not that set. The move that makes it work is the union, which turns "contains the singleton of every set" into "contains every set". A direct diagonal construction inside \( S \) also works, but it repeats the proof of @thm-russell instead of using it.
:::

<!-- dependency ledger
def-ordered-pair (claim): pairs can be built from sets (Kuratowski) | F3.1 (prose pointer); nothing depends on it
def-ordered-pair (claim): (<=) of the characteristic property is =E (substitution of equals) | def-rules-equality (cited)
def-ordered-pair (claim): (the paragraph after it) working convention: a pair is not a number, and a triple is not a pair | working convention stated in the text after def-ordered-pair, parallel to F2.1 §02's "numbers are not sets"; F3.1 (prose pointer)
def-cartesian-product (claim): A x B is a set; X^n is a set | working rule (W5) of F2.1 §02 (cited in prose; it covers pairs and n-tuples)
def-cartesian-product (claim): (*) uses exists-I and exists-E on "exists a in A exists b in B p = (a, b)" | prp-bounded-quantifier-rules (cited)
def-cartesian-product (claim): (*) uses =E to pass from x = a, a in A to x in A (and likewise y) | def-rules-equality (cited after def-ordered-pair)
def-cartesian-product (claim): (the pair-pattern set-builder paragraph) membership in {(x, y) in A x B : P(x, y)}, via (*), the characteristic property and =E | def-set-builder (cited); def-rules-equality (cited after def-ordered-pair)
exm-pair-equations (example): solving x + y = 3, x - y = 1 by adding and subtracting | school algebra
exm-pair-equations (solution): (the quick check after "Longer lists") t^2 >= 0 for real t | school fact (F1-F2 convention); proved in AN1.1
exm-small-products (example): an element of the empty set does not exist | def-empty-set
exm-small-products (example): (a) a, b, c are pairwise different and none of them is 1 or 2 | hypothesis stated in part (a) ("three different objects, none of them a number"); the six pairs are distinct and the two lists disjoint by def-ordered-pair (characteristic property)
prp-product-set-laws (proof): exists-E with fresh names; case split on d in B or d in C | prp-bounded-quantifier-rules (cited) for exists-E; F1.1 or-E (def-set-operations unwinds the union)
prp-product-set-laws (proof): substituting equals (=E): from p = (a, d) and (a, d) in A x B infer p in A x B, and likewise in the intersection and set-difference cases | def-rules-equality (cited after def-ordered-pair)
prp-product-set-laws (claim): (the warning after the remark) catalogue entry (N7), missing case | F1.5 (promised; prose pointer "the catalogue in *Logic and Proof*, Chapter 8, entry (N7)")
prp-product-set-laws (proof): the not-in conclusions by not-I | F1.2 (def-rules-negation), named in the prose after the proof
exm-product-of-intervals (example): order facts 0 <= x <= 2 and 1 <= x <= 3 give 1 <= x <= 2, etc. | school fact (F1-F2 convention); proved in AN1.1
prp-product-set-laws (claim): (the remark after exm-product-of-intervals) "not both sets have an element" plus excluded middle gives A empty or B empty | prp-excluded-middle (cited); prp-empty-set-unique (cited)
exm-relations-as-sets (example): 1 <= a <= 6 divisors, the count 14 | arithmetic, by listing
exm-relations-as-sets (example): x^2 = 1 - y^2 <= 1 gives -1 <= x <= 1; square roots of non-negative reals exist; squares are non-negative | school fact (F1-F2 convention); proved in AN1.1
exr-products-and-relations-a1 (solution): a pair is not a number | working convention stated in the text after def-ordered-pair (cited); F3.1 (prose pointer)
def-relation (claim): (the nonexample after exm-relations-as-sets) the number 3 is not a pair | working convention stated in the text after def-ordered-pair (cited)
def-relation (claim): (the warning and the paragraph before the exercises) symmetric, transitive, reflexive, antisymmetric relations; orders and equivalences | F2.5 (promised; prose pointer "studied in Chapter 5", "the subject of Chapter 5"); nothing here depends on it
exr-products-and-relations-b1 (solution): [0, 2] = [0, 1] u [1, 2] | school order fact (F1-F2 convention); proved in AN1.1
exr-products-and-relations-c1 (solution): (1, 2) is neither (1, 1) nor (2, 2) | def-ordered-pair (characteristic property), as stated
exr-products-and-relations-c2 (solution): a set either has an element or has none | prp-excluded-middle (cited); a set with no element is the empty set by prp-empty-set-unique (cited)
exr-products-and-relations-c2 (solution): (the marking scheme) catalogue entry (N1) | F1.5 (promised; prose pointer "*Logic and Proof*, Chapter 8's catalogue")
exm-method-uniqueness (claim): the quick check after it, x^3 = -8 forces x = -2; 3^2 = 9 | school fact (F1-F2 convention: a real number has exactly one real cube root); proved in AN1.1
exm-coordinates-unique (solution): from p = (a, b) and p = (a', b') infer (a, b) = (a', b') | def-rules-equality (cited after def-ordered-pair)
exr-products-and-relations-b4 (solution): (a) solving the linear system and the check by exact arithmetic; (b) 1^2 = (-1)^2 = 1 and 1 != -1 | school algebra
exr-products-and-relations-b4 (solution): (d), (e) membership of (a, b) and (e, e) via (*) | (*), proved in the text after def-cartesian-product
exr-images-and-preimages-r1 (solution): levels of proof | def-levels-of-proof (cited)
exr-images-and-preimages-r1 (solution): forall-I / forall-E rules and the flagged S_0 and x_0 boxes (derivation lines 7, 9, 12, 16, read in the solution's box-by-box account) | F1.4 (paid): def-rules-universal; uncited here; the rules are named with their *Logic and Proof*, Chapter 5 source in F2.1 §02 after def-subset, and index.md "What you need" names *Logic and Proof*, Chapters 5 and 6
exr-images-and-preimages-r1 (solution): the closing remark, S ⊆ A and A ⊆ B give S ⊆ B | prp-subset-transitive (F2.1 §02, cited)
exr-images-and-preimages-r4 (solution): every set x is an element of {x}; "is a singleton" is a property usable in specification | def-set-builder (F2.1 §02, listing)
-->
