# Ordered Pairs, Products and Relations

Sections 6.1 and 6.2 built sets and combined them: a set is fixed by its elements, and \( \cup \), \( \cap \), \( \setminus \) are \( \vee \), \( \wedge \), \( \wedge\neg \) read through membership. None of this can yet say "the point \( (1, 2) \) of the plane", "\( 3 \) is less than \( 5 \)", or "\( y \) is the square of \( x \)". Each of these is about two objects **in a given order**, and a set forgets order. This section adds one new kind of object, the ordered pair (with its longer versions, the \( n \)-tuples), and then uses it twice: to build the product \( A \times B \) of two sets, and to say what a relation between two sets is. The next section needs exactly this much: a function will be given by a relation of a special kind, its graph, together with a declared target set.

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

In words: to decide whether two pairs are equal, compare first coordinates with first coordinates and second with second; nothing else matters, and both comparisons must succeed. The direction \( (\Leftarrow) \) is nothing new: equal inputs give equal pairs, as for any construction (\( \rulename{=E} \), @def-rules-equality). The direction \( (\Rightarrow) \) is the content. It says that from the pair we can read off its coordinates, each in its place.

We do not say here **what** the object \( (a, b) \) is. Besides the characteristic property, we use one working convention: pairs and \( n \)-tuples are a different kind of object from numbers, just as sets are (Section 6.1), so **a pair is not a number**; and tuples of different lengths are different kinds of object, so a triple is not a pair. Nothing else about pairs is used in this chapter. The optional Chapter 9 shows that a pair with this property can be built from sets alone, so that nothing new has to be assumed. Until then, the existence of pairs with this property is taken as given, alongside the working rules (W1)–(W6) of Section 6.1.

**A convention about parentheses.** The symbol \( (a, b) \) now has two meanings. For real numbers \( a < b \) it is also the open interval \( \{ x \in \nR : a < x < b \} \). The book keeps both, and context decides, as it does in every analysis text. In "\( (0, 1) \) contains \( \tfrac{1}{2} \)" it is an interval. In "the point \( (0, 1) \) lies on the unit circle" it is a pair. Where both readings are near each other, the text says which is meant. This convention is stated once, here.

::: {#exm-pair-equations}
[Solving an equation between pairs]

Find all real numbers \( x \) and \( y \) with \( (x + y, x - y) = (3, 1) \). Then decide whether \( (1, 2) = (2, 1) \) and whether \( (1, 1) = (1, 1) \).
:::

::: {.solution}
By the characteristic property, \( (x + y, x - y) = (3, 1) \) holds if and only if
\[
x + y = 3 \quad \text{and} \quad x - y = 1 .
\]
Adding the two equations gives \( 2x = 4 \), so \( x = 2 \); subtracting them gives \( 2y = 2 \), so \( y = 1 \). Conversely, \( x = 2 \) and \( y = 1 \) give \( (x + y, x - y) = (3, 1) \). So there is exactly one solution, \( x = 2 \), \( y = 1 \).

The pairs \( (1, 2) \) and \( (2, 1) \) are **not** equal. If they were, the characteristic property would give \( 1 = 2 \) for the first coordinates. So \( (1, 2) \ne (2, 1) \), by \( \rulename{\neg I} \). The same test on \( (1, 1) \) and \( (1, 1) \) passes in both places, so they are equal; and \( (1, 1) \) has two places, although both hold the same number.
:::

The first part is typical. One equation between pairs is **two** equations between coordinates, and this is how pairs are used: an equation of pairs is split by the characteristic property, and the coordinates are compared one at a time.

**Nonexample by minimal change.** Replace the parentheses by braces. The set \( \{1, 2\} \) has the same two numbers as the pair \( (1, 2) \), but the characteristic property fails for sets: \( \{1, 2\} = \{2, 1\} \), and yet \( 1 \ne 2 \). What survives is membership: \( 1 \) and \( 2 \) are both in \( \{1, 2\} \). What is lost is order, the one thing the pair was made to keep.

**Why this definition.** Only \( (\Rightarrow) \) carries content. Without it, the pair could forget its coordinates, as \( \{1, 2\} \) forgets which number came first. The direction \( (\Leftarrow) \) could be dropped from the definition without loss: \( \rulename{=E} \) already gives it for \( (a, b) \), as for any construction. It is stated so that the property reads as a single test for equality of pairs.

**Longer lists.** The same idea gives ordered triples \( (a, b, c) \), and more generally ordered **\( n \)-tuples** \( (x_1, \dots, x_n) \) for \( n \in \nN \), \( n \ge 2 \). Like pairs, \( n \)-tuples are taken as given, and the \( n \)-tuples with all coordinates in a set form a set, by the working rule (W5) of Section 6.1. Two \( n \)-tuples are equal if and only if they agree in every place: \( (x_1, \dots, x_n) = (y_1, \dots, y_n) \) means \( x_k = y_k \) for every \( k \in \{1, \dots, n\} \). A triple is a new kind of object, not a pair whose first coordinate is a pair (by the convention stated after @def-ordered-pair). The pairs \( ((1, 2), 3) \) and \( (1, (2, 3)) \) carry the same three numbers in the same order, and it is tempting to call both "the triple \( (1, 2, 3) \)"; that is an identification made by convention, and exercise A1 asks whether the two pairs are equal.

::: {.check}
For which real numbers \( t \) is \( (t^2, t) = (1, -1) \)? For which is \( \{t^2, t\} = \{1, -1\} \)?
:::

::: {.solution}
The pair equation holds if and only if \( t^2 = 1 \) and \( t = -1 \), so exactly for \( t = -1 \). The set equation holds for \( t = -1 \) too, since \( \{1, -1\} = \{1, -1\} \). It holds for no other \( t \): the element \( -1 \) of the right side must be \( t^2 \) or \( t \), and \( t^2 \ge 0 \), so \( t = -1 \). Here the sets agree exactly where the pairs do, but that is luck. The pair equation \( (t, 1) = (1, t) \) holds only for \( t = 1 \), while the set equation \( \{t, 1\} = \{1, t\} \) holds for every \( t \).
:::

## Cartesian products

With pairs in hand, the plane is the set of all pairs of real numbers. More generally, from any two sets we can collect all pairs whose first coordinate comes from the first set and whose second comes from the second. Taking such a collection is the working rule (W5) of Section 6.1: it is a set.

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

In words: an element of \( A \times B \) is **a pair**, and **there exist** coordinates, one in \( A \) and one in \( B \), from which it is made. The membership condition hides two existential quantifiers, so using it means naming the coordinates, by \( \rulename{\exists E} \) (@prp-bounded-quantifier-rules), and then matching them against any other naming by the characteristic property of pairs. That two-step move is the one move of this section; \( (\ast) \) below packages it.

For a pair the condition simplifies, and we use the simpler form constantly:
\[
(x, y) \in A \times B \iff x \in A \text{ and } y \in B . \tag{$\ast$}
\]
Here is why. If \( x \in A \) and \( y \in B \), then \( x \) and \( y \) themselves are coordinates of the required kind, and \( (x, y) \in A \times B \) by \( \rulename{\exists I} \). Conversely, let \( (x, y) \in A \times B \). Then there are \( a \in A \) and \( b \in B \) with \( (x, y) = (a, b) \) [\( \rulename{\exists E} \)], and the characteristic property (@def-ordered-pair) gives \( x = a \) and \( y = b \). So \( x \in A \) and \( y \in B \). The characteristic property is used exactly once, in the direction \( (\Rightarrow) \); without it, \( (x, y) \) might equal \( (a, b) \) with the coordinates swapped or lost, and nothing could be concluded.

We write \( (\ast) \) for this equivalence in the rest of the section. It is the reason a product is easy to work with: membership of a pair in a product is checked one coordinate at a time.

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

Section 6.2 showed that \( \cup \), \( \cap \), and \( \setminus \) obey the laws of \( \vee \), \( \wedge \), and \( \wedge \neg \). The product interacts with them just as simply, one factor at a time. We use these laws for regions of the plane (exercise B1) and for functions out of the empty set (Section 6.4), so we state them all.

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
Every element of each side is a pair, so we name its coordinates by \( \rulename{\exists E} \) and then test membership one coordinate at a time, by \( (\ast) \). The first coordinate lies in \( A \) on both sides; the second lies in \( B \cup C \) on one side and in "\( B \) or \( C \)" on the other, which is the same condition by @def-set-operations. Each law is a law of Section 6.2 in the second coordinate, with the first coordinate carried along unchanged.
:::

::: {.proof}
*The \( \cup \) law.* We prove two inclusions and conclude by @prp-subset-antisymmetric.

\( (\subseteq) \) Let \( p \in A \times (B \cup C) \). By @def-cartesian-product there are \( a \in A \) and \( d \in B \cup C \) with \( p = (a, d) \) [\( \rulename{\exists E} \) (@prp-bounded-quantifier-rules), with fresh names \( a \), \( d \)]. By @def-set-operations, \( d \in B \) or \( d \in C \), and we argue by cases. If \( d \in B \), then \( p = (a, d) \in A \times B \) by \( (\ast) \), so \( p \in (A \times B) \cup (A \times C) \). If \( d \in C \), then likewise \( p \in A \times C \subseteq (A \times B) \cup (A \times C) \). In either case \( p \in (A \times B) \cup (A \times C) \).

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
Combining the two \( \emptyset \) laws with one more step gives the full description of an empty product: \( A \times B = \emptyset \) **if and only if** \( A = \emptyset \) or \( B = \emptyset \). The direction \( (\Leftarrow) \) is the pair of \( \emptyset \) laws. For \( (\Rightarrow) \), suppose \( A \times B = \emptyset \). If \( A \) has an element \( a \) and \( B \) has an element \( b \), then \( (a, b) \in A \times B = \emptyset \), which is impossible. So it is not the case that both sets have an element; by excluded middle (@prp-excluded-middle) applied to "\( A \) has an element", either \( A \) has none, and then \( A = \emptyset \) by @prp-empty-set-unique, or \( A \) has one, and then \( B \) has none, so \( B = \emptyset \).
:::

::: {.warning}
"\( A \times B = \emptyset \), so \( A = \emptyset \)" misses a case. The product \( \{1, 2\} \times \emptyset \) is empty, and \( \{1, 2\} \) is not. The correct conclusion is the disjunction "\( A = \emptyset \) or \( B = \emptyset \)" of the remark, and an argument that continues from it must treat both cases. Dropping one is the missing case of the catalogue in Chapter 5, entry (N7): a \( \rulename{\vee E} \) with one of its boxes left out.
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
A relation "from \( A \) to \( B \)" has its direction built in: \( R \subseteq A \times B \), and the first coordinate comes from \( A \). The relation \( L \) of part (a) contains \( (1, 2) \) and not \( (2, 1) \). Reading a relation backwards, "since \( 1 \mathrel{L} 2 \), also \( 2 \mathrel{L} 1 \)", treats it as a symmetric relation; relations with that property, and other properties such as transitivity, are studied in Chapter 7. Relating \( b \) to \( a \) is the job of the inverse relation \( R^{-1} \), a different set.
:::

This definition is all the next section needs. The graph of a function from \( X \) to \( Y \) will be a relation from \( X \) to \( Y \) in which every element of \( X \) is related to exactly one element of \( Y \); the function is that graph together with the declared codomain \( Y \). The graph \( Q \) qualifies and the circle \( S \) does not. The properties that make a relation an order or an equivalence (reflexive, symmetric, antisymmetric, transitive) are the subject of Chapter 7.

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

(b) No. Both are ordered pairs, so by the characteristic property (@def-ordered-pair) they are equal if and only if their first coordinates are equal and their second coordinates are equal. The first coordinates are the pair \( (1, 2) \) and the number \( 1 \). A pair is not a number, by the working convention stated after @def-ordered-pair (the optional Chapter 9, which builds both from sets, bears it out). So the first coordinates differ, and the pairs are not equal. Calling both "the triple \( (1, 2, 3) \)" is an identification made by convention, not an equality.

(c) \( \{ (2, 1), (3, 1), (3, 2) \} \), which is the relation \( > \) on \( \{1, 2, 3\} \).

(d) Yes. A relation on \( A \) is a subset of \( A \times A \), and \( \emptyset \subseteq A \times A \): the condition "\( x \in \emptyset \to x \in A \times A \)" holds for every \( x \), because its hypothesis is false (@prp-vacuous-implication, @def-subset).
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

\( (\Rightarrow) \) Suppose \( A \times B \subseteq B \times A \). By excluded middle (@prp-excluded-middle), each of \( A \) and \( B \) either has an element or has none, and a set with no elements is \( \emptyset \) (@prp-empty-set-unique). If \( A = \emptyset \) or \( B = \emptyset \), we are done. In the remaining case both have elements: fix \( a_0 \in A \) and \( b_0 \in B \) (\( \rulename{\exists E} \) twice, with fresh names).

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

Fatal errors (0 for the step): testing inclusion on particular elements only (entry (N1) of Chapter 5's catalogue); using \( b_0 \) without having shown that \( B \) has an element; concluding \( A = B \) from \( A \times B = B \times A \) "by canceling" without an element argument.
A proof of \( (\Rightarrow) \) by contraposition (assume \( A \ne B \) and both nonempty, and exhibit a pair of \( A \times B \) outside \( B \times A \)) earns full marks if it finds the pair: 2 points for the witnesses and 4 for the pair and the check that it is outside \( B \times A \), in place of the two inclusions.
:::

<!-- dependency ledger
def-ordered-pair (claim): pairs can be built from sets (Kuratowski) | optional Ch 9 (prose pointer); nothing depends on it
def-ordered-pair (claim): (<=) of the characteristic property is =E (substitution of equals) | def-rules-equality (cited)
def-ordered-pair (claim): (the paragraph after it) working convention: a pair is not a number, and a triple is not a pair | working convention stated in the text after def-ordered-pair, parallel to Section 6.1's "numbers are not sets"; optional Ch 9 (prose pointer)
def-cartesian-product (claim): A x B is a set; X^n is a set | working rule (W5) of Section 6.1 (cited in prose; it covers pairs and n-tuples)
def-cartesian-product (claim): (*) uses exists-I and exists-E on "exists a in A exists b in B p = (a, b)" | prp-bounded-quantifier-rules (cited)
def-cartesian-product (claim): (*) uses =E to pass from x = a, a in A to x in A (and likewise y) | def-rules-equality (cited after def-ordered-pair)
def-cartesian-product (claim): (the pair-pattern set-builder paragraph) membership in {(x, y) in A x B : P(x, y)}, via (*), the characteristic property and =E | def-set-builder (cited); def-rules-equality (cited after def-ordered-pair)
exm-pair-equations (example): solving x + y = 3, x - y = 1 by adding and subtracting | school algebra
exm-pair-equations (solution): (the quick check after it) t^2 >= 0 for real t | school fact (Part 0 convention); proved in Ch 11
exm-small-products (example): an element of the empty set does not exist | def-empty-set
exm-small-products (example): (a) a, b, c are pairwise different and none of them is 1 or 2 | hypothesis stated in part (a) ("three different objects, none of them a number"); the six pairs are distinct and the two lists disjoint by def-ordered-pair (characteristic property)
prp-product-set-laws (proof): exists-E with fresh names; case split on d in B or d in C | prp-bounded-quantifier-rules (cited) for exists-E; Ch 1 or-E (def-set-operations unwinds the union)
prp-product-set-laws (proof): substituting equals (=E): from p = (a, d) and (a, d) in A x B infer p in A x B, and likewise in the intersection and set-difference cases | def-rules-equality (cited after def-ordered-pair)
prp-product-set-laws (claim): (the warning after the remark) catalogue entry (N7), missing case | ch05 (promised; prose pointer "the catalogue in Chapter 5, entry (N7)")
prp-product-set-laws (proof): the not-in conclusions by not-I | Ch 2 (def-rules-negation), named in the prose after the proof
exm-product-of-intervals (example): order facts 0 <= x <= 2 and 1 <= x <= 3 give 1 <= x <= 2, etc. | school fact (Part 0 convention); proved in Ch 11
prp-product-set-laws (claim): (the remark after exm-product-of-intervals) "not both sets have an element" plus excluded middle gives A empty or B empty | prp-excluded-middle (cited); prp-empty-set-unique (cited)
exm-relations-as-sets (example): 1 <= a <= 6 divisors, the count 14 | arithmetic, by listing
exm-relations-as-sets (example): x^2 = 1 - y^2 <= 1 gives -1 <= x <= 1; square roots of non-negative reals exist; squares are non-negative | school fact (Part 0 convention); proved in Ch 11
exr-products-and-relations-a1 (solution): a pair is not a number | working convention stated in the text after def-ordered-pair (cited); optional Ch 9 (prose pointer)
def-relation (claim): (the nonexample after exm-relations-as-sets) the number 3 is not a pair | working convention stated in the text after def-ordered-pair (cited)
def-relation (claim): (the warning and the paragraph before the exercises) symmetric, transitive, reflexive, antisymmetric relations; orders and equivalences | ch07 (promised; prose pointer "studied in Chapter 7", "the subject of Chapter 7"); nothing here depends on it
exr-products-and-relations-b1 (solution): [0, 2] = [0, 1] u [1, 2] | school order fact (Part 0 convention); proved in Ch 11
exr-products-and-relations-c1 (solution): (1, 2) is neither (1, 1) nor (2, 2) | def-ordered-pair (characteristic property), as stated
exr-products-and-relations-c2 (solution): a set either has an element or has none | prp-excluded-middle (cited); a set with no element is the empty set by prp-empty-set-unique (cited)
exr-products-and-relations-c2 (solution): (the marking scheme) catalogue entry (N1) | ch05 (promised; prose pointer "Chapter 5's catalogue")
-->
