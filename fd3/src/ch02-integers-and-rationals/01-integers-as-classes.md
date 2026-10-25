# The Integers as Classes of Pairs

Chapter 1 built the natural numbers as the set \( \omega \), with its \( 0 \), \( + \), \( \cdot \) and \( < \), and proved the laws of arithmetic, the order and well-ordering from the axioms for sets. From this chapter on, \( \nN \) **means** that set (@cor-omega-identification and the citing rule of Section 1.7). In \( \nN \) the equation \( 5 + x = 3 \) has no solution: \( 5 \le 5 + x \) for every \( x \in \nN \) by @prp-omega-order-arithmetic (a), while \( 3 < 5 \) by the same result, as \( 5 = 3 + 2 \) with \( 2 \ne 0 \). So \( 5 + x = 3 \) would give \( 5 \le 3 < 5 \), hence \( 5 < 5 \), which @thm-omega-order (a) rules out. This section builds a larger set \( \nZ \), out of \( \nN \) alone, with the one tool of *Sets, Relations, and Cardinality*, Section 4.2: the quotient of a set by an equivalence relation.

## What we use about the natural numbers

Every fact about \( \nN \) in this section and the next is one of the following results of Chapter 1, and each is cited where a proof uses it. The defining equation \( n + 0 = n \) and the evaluation of numeral sums and comparisons such as \( 2 + 3 = 5 \) and \( 0 \ne 2 \) rest on @def-omega-arithmetic and @thm-omega-order and are not cited each time.

- **Defining equations** (@def-omega-arithmetic): \( n + 0 = n \), \( m + \mathrm{S}(n) = \mathrm{S}(m + n) \) and \( n \cdot 0 = 0 \), and the numerals \( 0 \coloneqq \emptyset \), \( 1 \), \( 2 \), …, with \( n + 1 = \mathrm{S}(n) \).
- **Laws of arithmetic** (@thm-omega-arithmetic-laws): \( + \) and \( \cdot \) are commutative and associative, \( \cdot \) distributes over \( + \), and \( 0 + n = n \), \( 1 \cdot n = n \), \( 0 \cdot n = 0 \).
- **Cancellation** (@prp-omega-order-arithmetic (b), (f)): \( m + k = n + k \) gives \( m = n \); and \( mk = nk \) with \( k \ne 0 \) gives \( m = n \).
- **Order** (@thm-omega-order (a)): \( < \) is a strict total order, so for all \( m, n \) **exactly one** of \( m < n \), \( m = n \), \( n < m \) holds, and \( < \) is transitive and irreflexive.
- **Order and addition** (@prp-omega-order-arithmetic (a)): \( m \le n \) if and only if \( n = m + j \) for some \( j \in \nN \); and \( m < n \) if and only if \( n = m + j \) for some \( j \ne 0 \). Adding preserves \( < \) (@prp-omega-order-arithmetic (c)).
- **Small facts and well-ordering**: \( 0 < 1 \) (@thm-omega-order (d)); no \( k \) satisfies \( n < k < \mathrm{S}(n) \) (@thm-omega-order (b)); every non-empty subset of \( \nN \) has a least element (@thm-omega-well-ordering).

That is the whole list for now. Nothing about the integers or the rationals of school enters a proof: from here on they are the sets this chapter builds, and their familiar properties become theorems.

## A naive attempt

The school picture of an integer is "a natural number with a sign": \( +3 \), \( -2 \), \( 0 \). It is tempting to take that literally and let an integer be a pair \( (s, n) \) with a sign \( s \in \{0, 1\} \) (read \( 0 \) as "plus" and \( 1 \) as "minus") and a size \( n \in \nN \). Two things go wrong at once.

First, zero gets two names, \( (0, 0) \) and \( (1, 0) \): a "plus zero" and a "minus zero". Either both stay, and every theorem must treat them as the same, or one is banned, and every definition must check that it never produces the banned one.

Second, addition needs cases. Adding \( +m \) and \( -n \) should give \( +(m - n) \) when \( n \le m \) and \( -(n - m) \) when \( m < n \), where \( m - n \) is the subtraction of @prp-omega-order-arithmetic (a), defined on \( \nN \) only when \( n \le m \). There are four sign patterns for a sum, and two of them split again by the order of the sizes. A proof that addition is associative would split by the signs of all three terms and then by the order of their sizes, and every case would subtract in \( \nN \) in its own direction.

The trouble in both is the same: the definition **performs** a subtraction that \( \nN \) can only do one way round. The construction below never performs it. It records the subtraction as a pair, and lets an equivalence relation decide when two recorded subtractions should count as equal.

## Pairs that record a difference

Think of a pair \( (a, b) \in \nN \times \nN \) as a note saying "\( a \) minus \( b \)", to be computed later or never. The note \( (3, 5) \) is legitimate even though \( 3 - 5 \) is not a natural number. Many notes say the same thing: \( (3, 5) \), \( (0, 2) \) and \( (10, 12) \) all describe "two less than nothing", which school calls \( -2 \).

When do two notes \( (a, b) \) and \( (c, d) \) describe the same thing? School would write \( a - b = c - d \), and then add \( b + d \) to both sides to get \( a + d = b + c \). That last equation is the one we keep, because it uses only addition, which \( \nN \) has for all inputs. The computation with minus signs is a **heuristic**, borrowed from school to find the definition; the definition does not depend on it.

*An integer is a difference you have not computed yet.*

::: {#def-integers-as-classes}
[The Integers]

For \( (a, b), (c, d) \in \nN \times \nN \), let
\[
(a, b) \sim (c, d) \iff a + d = b + c .
\]
The set of **integers** is the quotient set
\[
\nZ \coloneqq (\nN \times \nN)/{\sim}
\]
of @fd2:def-quotient-set, and an **integer** is an element of \( \nZ \). The class of the pair \( (a, b) \) is written \( [(a, b)] \):
\[
[(a, b)] = \{ (c, d) \in \nN \times \nN : (c, d) \sim (a, b) \} .
\]
:::

In words: two pairs are related when their **cross sums** agree, the first coordinate of each added to the second coordinate of the other. The relation is a subset of \( (\nN \times \nN) \times (\nN \times \nN) \), described by a property (@fd2:def-relation, @fd2:def-cartesian-product). An integer is one whole class: the set of all pairs that record the same difference. The notation \( [(a, b)] \) is the class notation \( [x] \) of @fd2:def-equivalence-class with \( x = (a, b) \); no new bracket is introduced.

**Well-definedness.** @fd2:def-quotient-set is stated for an **equivalence relation**. Until \( \sim \) is shown to be one, the definition of \( \nZ \) is a plan, not a definition. The next proposition supplies the missing check, and it is placed directly after the definition for that reason.

**An integer is a set of pairs.** It is not a natural number with a sign, and it is not a pair. *Sets, Relations, and Cardinality*, Chapter 1 adopted the convention that a pair is not a number (after @fd2:def-ordered-pair), and on \( \omega \) that became a theorem, @prp-pair-not-natural. The same care is needed here: \( [(0, 2)] \) is the set \( \{ (0, 2), (1, 3), (2, 4), \dots \} \), and the school \( -2 \) is what those pairs have in common. The construction takes "what they have in common" to be **the set of them**.

::: {#prp-integer-pairs-equivalence}
[The Relation Behind the Integers]

The relation \( \sim \) of @def-integers-as-classes is an equivalence relation on \( \nN \times \nN \) (@fd2:def-equivalence-relation).
:::

::: {.idea}
Reflexivity and symmetry are rearrangements of one equation, by commutativity. Transitivity has two hypotheses, \( a + d = b + c \) and \( c + f = d + e \), and a goal \( a + f = b + e \) in which \( c \) and \( d \) do not appear. In school one would subtract them. In \( \nN \) we add the two equations, so that \( c + d \) appears on both sides, and then remove it by cancellation.

*Before reading on: which line uses cancellation in \( \nN \), and why is it more direct than subtracting \( c + d \)?*
:::

::: {.proof}
We check (Eq1)–(Eq3) of @fd2:def-equivalence-relation. Let \( (a, b), (c, d), (e, f) \in \nN \times \nN \).

(Eq1) \( a + b = b + a \) by commutativity (@thm-omega-arithmetic-laws (b)), so \( (a, b) \sim (a, b) \).

(Eq2) Suppose \( (a, b) \sim (c, d) \), that is, \( a + d = b + c \). By commutativity, \( c + b = b + c = a + d = d + a \), and \( c + b = d + a \) says \( (c, d) \sim (a, b) \).

(Eq3) Suppose \( (a, b) \sim (c, d) \) and \( (c, d) \sim (e, f) \), that is,
\[
a + d = b + c \quad \text{and} \quad c + f = d + e .
\]
Adding the two equations gives \( (a + d) + (c + f) = (b + c) + (d + e) \). By associativity and commutativity (@thm-omega-arithmetic-laws (b), (c)), the left side is \( (a + f) + (c + d) \) and the right side is \( (b + e) + (c + d) \), so
\[
(a + f) + (c + d) = (b + e) + (c + d) .
\]
By cancellation (@prp-omega-order-arithmetic (b)) with \( k = c + d \), \( a + f = b + e \). That is \( (a, b) \sim (e, f) \).

This proves that \( \sim \) is an equivalence relation.
:::

The answer to the prompt is the last line of (Eq3). It is tempting to "subtract \( c + d \) from both sides" at the end. In \( \nN \) the difference \( n - m \) of @prp-omega-order-arithmetic (a) exists only when \( m \le n \). Here it does exist, since \( c + d \le (a + f) + (c + d) \) and \( c + d \le (b + e) + (c + d) \) by the same result and commutativity, but only after that check; and reading off \( ((a + f) + (c + d)) - (c + d) = a + f \) uses the uniqueness in (a), which is itself proved by cancellation. Cancellation removes \( c + d \) directly, and it holds for all \( k \), with no size check.

So \( \nZ = (\nN \times \nN)/{\sim} \) is now defined, and by @fd2:thm-classes-partition its elements partition \( \nN \times \nN \): every pair lies in exactly one integer, and \( [(a, b)] = [(c, d)] \) if and only if \( a + d = b + c \).

## Pictures of classes

The quarter plane \( \nN \times \nN \) is a grid of lattice points, and the classes are easy to see in it.

::: {#exm-integer-pair-classes}
[Three classes, listed and drawn]

List the elements \( (x, y) \) with \( x \le 4 \) of each of the classes \( [(3, 5)] \), \( [(0, 0)] \) and \( [(4, 1)] \), and describe each class as a set of lattice points.
:::

::: {.solution}
*The class \( [(3, 5)] \).* A pair \( (x, y) \) lies in it when \( x + 5 = y + 3 \). This holds if and only if \( y = x + 2 \). Indeed, if \( y = x + 2 \), then \( y + 3 = x + (2 + 3) = x + 5 \) by associativity (@thm-omega-arithmetic-laws (c)). Conversely, \( x + 5 = (x + 2) + 3 \), so \( x + 5 = y + 3 \) gives \( (x + 2) + 3 = y + 3 \), and cancellation (@prp-omega-order-arithmetic (b)) gives \( y = x + 2 \). So
\[
[(3, 5)] = \{ (x, x + 2) : x \in \nN \} ,
\]
and the elements with \( x \le 4 \) are \( (0, 2) \), \( (1, 3) \), \( (2, 4) \), \( (3, 5) \), \( (4, 6) \).

*The class \( [(0, 0)] \).* Here the condition is \( x + 0 = y + 0 \), that is, \( x = y \), since \( n + 0 = n \) (@def-omega-arithmetic (a)). So \( [(0, 0)] = \{ (x, x) : x \in \nN \} \), the diagonal, and the elements with \( x \le 4 \) are \( (0, 0) \), \( (1, 1) \), \( (2, 2) \), \( (3, 3) \), \( (4, 4) \).

*The class \( [(4, 1)] \).* The condition \( x + 1 = y + 4 \) holds if and only if \( x = y + 3 \), by the same two steps as for \( [(3, 5)] \). So \( [(4, 1)] = \{ (y + 3, y) : y \in \nN \} \). Its elements with \( x \le 4 \) are \( (3, 0) \) and \( (4, 1) \) only: \( x = y + 3 = 3 + y \) (@thm-omega-arithmetic-laws (b)) gives \( 3 \le x \) (@prp-omega-order-arithmetic (a)); with \( x \le 4 = \mathrm{S}(3) \), \( x \) is \( 3 \) or \( 4 \), since no natural number lies strictly between \( 3 \) and \( \mathrm{S}(3) \) (@thm-omega-order (b)); and then \( y + 3 = 3 = 0 + 3 \) or \( y + 3 = 4 = 1 + 3 \), so \( y \) is \( 0 \) or \( 1 \) by cancellation (@prp-omega-order-arithmetic (b)).

Each of these three classes is the set of lattice points on one diagonal line \( y = x + k \) or \( x = y + k \) of the quarter plane, starting on an axis and running up and to the right.
:::

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.62, every node/.style={font=\small}]
  \draw[->] (-0.3,0) -- (7.0,0) node[right] {$x$};
  \draw[->] (0,-0.3) -- (0,7.0) node[above] {$y$};
  \foreach \i in {0,...,6} {
    \node[below] at (\i,-0.25) {$\i$};
    \node[left] at (-0.25,\i) {$\i$};
    \foreach \j in {0,...,6} {
      \fill[gray!60] (\i,\j) circle (1.4pt);
    }
  }
  \draw[thick] (0,2) -- (4.6,6.6);
  \foreach \i in {0,...,4} { \filldraw (\i,\i+2) circle (2.6pt); }
  \node[above left] at (2.2,4.6) {$[(3,5)]$};
  \draw[thick, dashed] (0,0) -- (6.6,6.6);
  \foreach \i in {0,...,6} { \draw[fill=white] (\i,\i) circle (2.6pt); }
  \node[right] at (6.6,6.4) {$[(0,0)]$};
  \draw[thick, dotted] (3,0) -- (6.6,3.6);
  \foreach \j in {0,...,3} { \filldraw (\j+2.89,\j-0.11) rectangle (\j+3.11,\j+0.11); }
  \node[right] at (6.6,3.6) {$[(4,1)]$};
\end{tikzpicture}
\end{center}
```

The picture shows the three classes as three diagonals: \( [(3, 5)] \) solid with filled dots, \( [(0, 0)] \) dashed with open dots, \( [(4, 1)] \) dotted with squares. Every pair lies in exactly one class (@fd2:thm-classes-partition), so no two of these diagonals share a lattice point; after the normal form below we see that every class is a diagonal of this kind, so every lattice point lies on exactly one of them. The class \( [(0, 0)] \) is the degenerate case: it is the integer zero, and it is the only class whose line passes through the origin.

**A non-example by minimal change.** Replace the sums in the definition by products: on \( \nN \times \nN \), let \( (a, b) \approx (c, d) \) mean \( ad = bc \). This is still reflexive (\( ab = ba \)) and symmetric (\( ad = bc \) gives \( cb = da \)), both by commutativity of \( \cdot \) (@thm-omega-arithmetic-laws (f)). It is **not** transitive:
\[
(1, 1) \approx (0, 0), \qquad (0, 0) \approx (2, 1), \qquad \text{but} \qquad (1, 1) \not\approx (2, 1) ,
\]
since \( 1 \cdot 0 = 1 \cdot 0 \), \( 0 \cdot 1 = 0 \cdot 2 \) and \( 1 \cdot 1 \ne 1 \cdot 2 \). The clause that fails is (Eq3), and the line of the proof above that has no counterpart is cancellation. Additive cancellation holds for every \( k \); multiplicative cancellation (@prp-omega-order-arithmetic (f)) needs \( k \ne 0 \), and the pair \( (0, 0) \) supplies a middle factor that is \( 0 \). When Section 2.4 builds fractions with this product relation, it excludes zero second coordinates for exactly this reason.

## Why this definition

**Why cross sums.** "\( a - b = c - d \)" cannot be the definition, because \( a - b \) is defined in \( \nN \) only when \( b \le a \). The cross-sum equation \( a + d = b + c \) says the same thing whenever both differences exist, and it makes sense for every two pairs.

**Why whole classes.** Each class has a simplest pair, one with a coordinate \( 0 \), as the next proposition shows. One could define \( \nZ \) as the set of these simplest pairs instead. But then the sum of \( (3, 0) \) and \( (0, 5) \) would have to be brought back to a simplest pair, \( (0, 2) \), by a subtraction in \( \nN \) in the right direction: the case analysis of the naive attempt returns. With classes, any representatives may be combined, and the equivalence relation absorbs the bookkeeping. The price is the check of the next section: a definition through representatives must not depend on which ones were used.

**The degenerate class and the name.** The class of \( (0, 0) \) is the diagonal; it will be the zero of \( \nZ \). The word "integer" is Latin for "whole" or "untouched", a number not broken into fractions; Section 2.4 builds those.

The first result about the new set says that each class has exactly one simplest name.

::: {#prp-integer-normal-form}
[Normal Form of an Integer]

::: {.enumerate options="label=(\alph*)"}
1. Every class \( [(a, b)] \in \nZ \) contains **exactly one** pair of the form \( (n, 0) \) or \( (0, n) \) with \( n \in \nN \) (the pair \( (0, 0) \) has both forms and counts once). Precisely, for each \( (a, b) \in \nN \times \nN \) **exactly one** of the following holds:
   - \( a = b + k \) for some \( k \ne 0 \), and then \( [(a, b)] = [(k, 0)] \);
   - \( a = b \), and then \( [(a, b)] = [(0, 0)] \);
   - \( b = a + k \) for some \( k \ne 0 \), and then \( [(a, b)] = [(0, k)] \).
2. For all \( m, n \in \nN \): if \( [(m, 0)] = [(n, 0)] \), then \( m = n \); and if \( [(0, m)] = [(0, n)] \), then \( m = n \).
:::
:::

::: {.idea}
The three cases are the three cases of trichotomy for \( a \) and \( b \), and @prp-omega-order-arithmetic (a) turns each inequality into an equation with a non-zero \( k \). In each case one line of arithmetic shows that \( (a, b) \) is related to the simplest pair. For "exactly one pair", two simplest pairs of the same form are handled by (b), so we prove (b) first. Two of opposite forms, \( (k, 0) \) and \( (0, l) \) with \( k, l \ne 0 \), would need \( k + l = 0 \), which the order forbids.
:::

::: {.proof}
*(b)* Suppose \( [(m, 0)] = [(n, 0)] \). By @fd2:thm-classes-partition (b), \( (m, 0) \sim (n, 0) \), that is, \( m + 0 = 0 + n \). Since \( m + 0 = m \) (@def-omega-arithmetic (a)) and \( 0 + n = n \) (@thm-omega-arithmetic-laws (a)), \( m = n \). Likewise \( [(0, m)] = [(0, n)] \) gives \( 0 + n = m + 0 \), so \( n = m \).

*(a), the three cases.* Let \( (a, b) \in \nN \times \nN \). By @thm-omega-order (a), exactly one of \( b < a \), \( a = b \), \( a < b \) holds. By @prp-omega-order-arithmetic (a), \( b < a \) holds if and only if \( a = b + k \) for some \( k \ne 0 \), and \( a < b \) if and only if \( b = a + k \) for some \( k \ne 0 \). So exactly one of the three listed conditions holds. In each case the stated equality of classes follows from @fd2:thm-classes-partition (b), once the two pairs are shown to be related:

- if \( a = b + k \), then \( a + 0 = a = b + k \) (@def-omega-arithmetic (a)), so \( (a, b) \sim (k, 0) \);
- if \( a = b \), then \( a + 0 = b + 0 \), so \( (a, b) \sim (0, 0) \);
- if \( b = a + k \), then \( a + k = b = b + 0 \) (@def-omega-arithmetic (a)), so \( (a, b) \sim (0, k) \).

In particular every class contains a pair of the form \( (n, 0) \) or \( (0, n) \).

*(a), only one such pair.* Let \( C \) be a class containing two such pairs \( p \) and \( p' \). Since both lie in \( C \), \( [p] = C = [p'] \) by @fd2:thm-classes-partition (b). If \( p = (m, 0) \) and \( p' = (n, 0) \), then \( m = n \) by (b), so \( p = p' \); likewise if both have the form \( (0, \cdot) \). This covers every case in which one of the pairs is \( (0, 0) \), since \( (0, 0) \) has both forms. There remains \( p = (k, 0) \) and \( p' = (0, l) \) with \( k \ne 0 \) and \( l \ne 0 \). Then \( p \sim p' \) says \( k + l = 0 + 0 = 0 \). Since \( l \ne 0 \), @prp-omega-order-arithmetic (a) gives \( k < 0 \); and since \( k = 0 + k \) (@thm-omega-arithmetic-laws (a)) with \( k \ne 0 \), it also gives \( 0 < k \). By transitivity \( k < k \), which @thm-omega-order (a) rules out. So this case cannot occur, and the pair is unique.
:::

So every integer has a **normal form**: it is \( [(n, 0)] \) for a unique \( n \in \nN \), or \( [(0, n)] \) for a unique \( n \in \nN \) with \( n \ne 0 \). In the picture, every class is a diagonal: \( (x, y) \sim (n, 0) \) means \( x + 0 = y + n \), that is, \( x = y + n \), and \( (x, y) \sim (0, n) \) means \( x + n = y + 0 \), that is, \( y = x + n \) (@def-omega-arithmetic (a)), so
\[
[(n, 0)] = \{ (y + n, y) : y \in \nN \} \quad \text{and} \quad [(0, n)] = \{ (x, x + n) : x \in \nN \} .
\]
The normal form is where the class's diagonal meets an axis. The next section reads \( [(n, 0)] \) as the natural number \( n \) and \( [(0, n)] \) as its negative; this is how the description of *Sets, Relations, and Cardinality*, Section 2.1, "an integer is a natural number or the negative of one", becomes a theorem about the constructed \( \nZ \).

::: {.warning}
A property of a class must not be read off **one** representative. "The integer \( [(a, b)] \) is small when \( a \le 3 \)" sounds like a property of integers and is not one: \( [(3, 3)] = [(5, 5)] \), the first pair has \( a = 3 \le 3 \), and the second has \( a = 5 \). The class is "small" or not according to the name we happened to use. The property "\( [(a, b)] \) is positive when \( b < a \)" looks the same and happens to be safe: if \( (a, b) \sim (a', b') \) and \( b < a \), then \( b' < a' \). That needs a proof, and Section 2.3 gives it before it calls any integer positive.
:::

::: {.check}
Is \( (2, 7) \sim (10, 15) \)? Is \( (2, 7) \sim (15, 10) \)?
:::

::: {.solution}
Yes: the cross sums are \( 2 + 15 = 17 \) and \( 7 + 10 = 17 \). No: the cross sums are \( 2 + 10 = 12 \) and \( 7 + 15 = 22 \), and \( 12 \ne 22 \). In school terms, \( (2, 7) \) and \( (10, 15) \) both record "five less", while \( (15, 10) \) records "five more". The normal forms agree: \( 7 = 2 + 5 \) and \( 15 = 10 + 5 \), so \( [(2, 7)] = [(0, 5)] = [(10, 15)] \), while \( [(15, 10)] = [(5, 0)] \), a different class by @prp-integer-normal-form (a).
:::

The set \( \nZ \) exists, and each element has a simplest name. It has no arithmetic yet. The next section defines the sum and product of two integers by formulas on representatives, and the warning above is the question it must answer for each formula.

## Exercises

### A. Check your understanding

::: {#exr-integers-as-classes-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the relation \( \sim \) and the set \( \nZ \) of @def-integers-as-classes in symbols.
2. Which pairs with a coordinate equal to \( 0 \) lie in \( [(6, 9)] \)?
3. Why does the proof of @prp-integer-pairs-equivalence cancel \( c + d \) rather than subtract it?
4. True or false, with a reason: \( [(1, 1)] = [(5, 5)] \).
:::
:::

::: {.solution}
(a) For \( (a, b), (c, d) \in \nN \times \nN \): \( (a, b) \sim (c, d) \iff a + d = b + c \); and \( \nZ \coloneqq (\nN \times \nN)/{\sim} = \{ [(a, b)] : (a, b) \in \nN \times \nN \} \).

(b) Only \( (0, 3) \). A pair \( (x, 0) \) in the class would need \( x + 9 = 0 + 6 = 6 \) (@thm-omega-arithmetic-laws (a)); but \( 9 \le x + 9 \) by @prp-omega-order-arithmetic (a) (with @thm-omega-arithmetic-laws (b) to write \( x + 9 = 9 + x \)), and \( 6 < 9 \), so \( x + 9 = 6 \) would give \( 9 \le 6 < 9 \), and then \( 9 < 9 \), which @thm-omega-order (a) excludes. A pair \( (0, y) \) needs \( 0 + 9 = y + 6 \), that is, \( 3 + 6 = y + 6 \), so \( y = 3 \) by cancellation (@prp-omega-order-arithmetic (b)). This agrees with @prp-integer-normal-form (a): \( 9 = 6 + 3 \), so \( [(6, 9)] = [(0, 3)] \), and the class has exactly one pair with a coordinate \( 0 \).

(c) Subtraction in \( \nN \) is defined only when the number subtracted is at most the other (@prp-omega-order-arithmetic (a)). Here \( c + d \) is at most both sides, so subtracting would be possible, but only after that check, and reading off the differences uses the uniqueness in (a), which is itself proved by cancellation. Cancellation (@prp-omega-order-arithmetic (b)) holds for every \( k \in \nN \) with no check, so the proof uses it directly.

(d) True. \( (1, 1) \sim (5, 5) \) because \( 1 + 5 = 1 + 5 \), so the classes are equal by @fd2:thm-classes-partition (b). Both are the zero class \( [(0, 0)] \).
:::

### B. Practice

::: {#exr-integers-as-classes-b1}
[B1: Three look-alike relations]

On \( \nN \times \nN \), determine which of the following relations are equivalence relations. For each one, decide which of (Eq1)–(Eq3) hold. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( (a, b) \approx_1 (c, d) \) if and only if \( a + c = b + d \).
2. \( (a, b) \approx_2 (c, d) \) if and only if \( a + 2d = 2b + c \).
3. \( (a, b) \approx_3 (c, d) \) if and only if \( a + d \le b + c \).
:::
:::

::: {.solution}
(a) **Symmetric, but neither reflexive nor transitive.** Symmetric: \( a + c = b + d \) gives \( c + a = d + b \) by commutativity (@thm-omega-arithmetic-laws (b)). Not reflexive: \( (0, 1) \approx_1 (0, 1) \) would need \( 0 + 0 = 1 + 1 \), that is, \( 0 = 2 \), which is false. Not transitive: \( (0, 1) \approx_1 (1, 0) \) since \( 0 + 1 = 1 + 0 \), and \( (1, 0) \approx_1 (0, 1) \) since \( 1 + 0 = 0 + 1 \); transitivity would give \( (0, 1) \approx_1 (0, 1) \), which we just saw is false. Notice that **every** pair is related to something, since \( (a, b) \approx_1 (b, a) \) by commutativity. A symmetric relation in which every element is related to something still need not be reflexive: "\( x \) related to \( y \), so \( y \) related to \( x \), so \( x \) related to \( x \)" uses transitivity, and that is what fails here.

(b) **An equivalence relation.** (Eq1) \( a + 2b = 2b + a \). (Eq2) \( a + 2d = 2b + c \) gives \( c + 2b = 2d + a \), by commutativity. (Eq3) Suppose \( a + 2d = 2b + c \) and \( c + 2f = 2d + e \). Adding, and rearranging by @thm-omega-arithmetic-laws (b), (c),
\[
(a + 2f) + (2d + c) = (2b + e) + (2d + c) ,
\]
and cancellation (@prp-omega-order-arithmetic (b)) gives \( a + 2f = 2b + e \). In school terms the pair \( (a, b) \) records \( a - 2b \), and the relation says \( a - 2b = c - 2d \).

(c) **Reflexive and transitive, not symmetric.** (Eq1) \( a + b \le b + a \), since the two sides are equal. (Eq3) First, for \( x, y, u, v \in \nN \), \( x \le y \) and \( u \le v \) give \( x + u \le y + v \): by @prp-omega-order-arithmetic (a), \( y = x + i \) and \( v = u + j \) for some \( i, j \in \nN \), so \( y + v = (x + u) + (i + j) \) by @thm-omega-arithmetic-laws (b), (c), and (a) again gives \( x + u \le y + v \). Now let \( a + d \le b + c \) and \( c + f \le d + e \). Adding and rearranging,
\[
(a + f) + (c + d) \le (b + e) + (c + d) .
\]
If \( b + e < a + f \), then \( (b + e) + (c + d) < (a + f) + (c + d) \) by @prp-omega-order-arithmetic (c), contradicting the display by trichotomy (@thm-omega-order (a)). So \( a + f \le b + e \), by trichotomy again. Not symmetric: \( (0, 1) \approx_3 (0, 0) \) since \( 0 + 0 \le 1 + 0 \), that is, \( 0 \le 1 \); but \( (0, 0) \approx_3 (0, 1) \) would need \( 0 + 1 \le 0 + 0 \), that is, \( 1 \le 0 \), which is false since \( 0 < 1 \) (@thm-omega-order (d)).
:::

::: {#exr-integers-as-classes-b2}
[B2: A class in set-builder form]

Let \( (a, b) \in \nN \times \nN \). Describe the class \( [(a, b)] \) by a set-builder expression, in the two cases \( b \le a \) and \( a \le b \). Hence describe \( [(7, 2)] \) and \( [(2, 7)] \).
:::

::: {.solution}
*Case \( b \le a \).* Write \( a = b + k \) with \( k \in \nN \) (@prp-omega-order-arithmetic (a)). We claim
\[
[(a, b)] = \{ (y + k, y) : y \in \nN \} .
\]
A pair \( (x, y) \) lies in \( [(a, b)] \) when \( x + b = y + a \), that is, \( x + b = (y + k) + b \) by @thm-omega-arithmetic-laws (c), (b). By cancellation (@prp-omega-order-arithmetic (b)) this holds if and only if \( x = y + k \); the converse direction is substitution. So the elements of the class are exactly the pairs \( (y + k, y) \), \( y \in \nN \).

*Case \( a \le b \).* Write \( b = a + k \) (@prp-omega-order-arithmetic (a)). In the same way, \( (x, y) \sim (a, b) \) means \( x + (a + k) = y + a \), which by rearranging and canceling \( a \) holds if and only if \( y = x + k \). So \( [(a, b)] = \{ (x, x + k) : x \in \nN \} \).

The two descriptions agree when \( a = b \) (then \( k = 0 \)), as they must. For the examples, \( 7 = 2 + 5 \), so \( [(7, 2)] = \{ (y + 5, y) : y \in \nN \} \), and \( [(2, 7)] = \{ (x, x + 5) : x \in \nN \} \).
:::

### C. Going deeper

::: {#exr-integers-as-classes-c1}
[C1: Exit check: the relation that builds \( \nZ \)]

Let \( \sim \) be the relation of @def-integers-as-classes on \( \nN \times \nN \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \sim \) is an equivalence relation.
2. Prove that if \( (a, b) \sim (a', b') \) and \( (c, d) \sim (c', d') \), then \( (a + c, b + d) \sim (a' + c', b' + d') \).
3. Say in one sentence what (b) means for a rule that adds two integers by adding representatives coordinatewise.
:::

Name the property of \( \nN \) behind each step.
:::

::: {.solution}
(a) This is @prp-integer-pairs-equivalence; here is the proof once more. Reflexive: \( a + b = b + a \) by commutativity. Symmetric: if \( a + d = b + c \), then \( c + b = d + a \) by commutativity. Transitive: let \( a + d = b + c \) and \( c + f = d + e \). Adding the two equations and rearranging by associativity and commutativity gives \( (a + f) + (c + d) = (b + e) + (c + d) \), and cancellation of \( c + d \) (@prp-omega-order-arithmetic (b)) gives \( a + f = b + e \).

(b) The hypotheses are \( a + b' = b + a' \) and \( c + d' = d + c' \). Adding them,
\[
(a + b') + (c + d') = (b + a') + (d + c') .
\]
By associativity and commutativity (@thm-omega-arithmetic-laws (b), (c)), the left side is \( (a + c) + (b' + d') \) and the right side is \( (b + d) + (a' + c') \). So
\[
(a + c) + (b' + d') = (b + d) + (a' + c') ,
\]
which is the cross-sum equation for \( (a + c, b + d) \sim (a' + c', b' + d') \).

(c) The class of \( (a + c, b + d) \) does not depend on which representatives of \( [(a, b)] \) and \( [(c, d)] \) were used, so "add representatives coordinatewise, then take the class" is **well defined**: it assigns exactly one integer to each pair of integers.

**Marking scheme.** (10 points)

- 2: reflexive and symmetric, each citing commutativity of \( + \) in \( \nN \).
- 3: transitivity: combines the two hypotheses into one equation with a common summand on both sides (by adding them, or by substituting one into the other) and removes that summand by **cancellation** in \( \nN \), named as such.
- 2: in (b), combines the two hypotheses (by adding them, or by substituting both into a rearranged sum).
- 2: in (b), rearranges by associativity and commutativity to the cross-sum equation for the two sums.
- 1: (c) concludes that the coordinatewise sum is well defined on classes.

A proof of (b) that changes one argument at a time (first \( (a, b) \) to \( (a', b') \) with \( (c, d) \) fixed, then the other) and joins the two by transitivity earns the four points of (b) if each step is justified. Fatal errors (0 for the step): subtracting in \( \nN \) (for instance "subtract \( d \) from both sides") without showing that the difference exists; proving only reflexivity and symmetry and calling the relation an equivalence relation.
:::

<!-- dependency ledger
def-integers-as-classes (claim): 5 + x = 3 has no solution in N: 5 <= 5 + x, 3 < 5 (5 = 3 + 2), and 5 <= 3 < 5 gives 5 < 5 | prp-omega-order-arithmetic (a), thm-omega-order (a) (both cited in the opening)
def-integers-as-classes (claim): (heuristic) a - b = c - d iff a + d = b + c in school arithmetic | school arithmetic, labelled a heuristic in the text; no proof uses it
def-integers-as-classes (claim): (naive attempt) the case structure of signed addition | informal motivation; no proof uses it
prp-integer-pairs-equivalence (proof): adding two equations: x = y and u = v give x + u = y + v | substitution of equals, def-rules-equality (F1.4 §07), used silently
prp-integer-pairs-equivalence (proof): rearranging four terms (a + d) + (c + f) = (a + f) + (c + d) | thm-omega-arithmetic-laws (b), (c) (cited); verify/ch02/prp-integer-pairs-equivalence.py
exm-integer-pair-classes (solution): (x + 2) + 3 = x + 5; 2 + 3 = 5 and similar numeral sums | thm-omega-arithmetic-laws (c) (cited) and numeral arithmetic by def-omega-arithmetic (as in the F3.1 §05 Quick check); verify/ch02/exm-integer-pair-classes.py
exm-integer-pair-classes (solution): 3 <= x <= 4 = S(3) gives x in {3, 4}; y + 3 in {0 + 3, 1 + 3} gives y in {0, 1} | thm-omega-arithmetic-laws (b), prp-omega-order-arithmetic (a), (b), thm-omega-order (b) (cited)
exm-integer-pair-classes (claim): (picture) no two diagonals share a lattice point | thm-classes-partition (cited); that every class is a diagonal is shown after prp-integer-normal-form
prp-integer-normal-form (claim): (picture) [(n, 0)] = {(y + n, y)} and [(0, n)] = {(x, x + n)}, so every class is a diagonal | prp-integer-normal-form (a), def-omega-arithmetic (a) (cited)
def-integers-as-classes (claim): (non-example) 1*0 = 1*0, 0*1 = 0*2, 1*1 != 1*2 | numeral arithmetic by def-omega-arithmetic, thm-omega-arithmetic-laws (e); verify/ch02/def-integers-as-classes.py
def-integers-as-classes (claim): (check) cross sums 17 = 17, 12 != 22; 7 = 2 + 5, 15 = 10 + 5 | numeral arithmetic by def-omega-arithmetic; distinct numerals are distinct (thm-omega-order (a)); verify/ch02/def-integers-as-classes.py
prp-integer-normal-form (claim): (warning) b < a and (a, b) ~ (a', b') give b' < a' | F3.2 §03 (prose pointer, paid by def-integer-order; nothing here depends on it)
exr-integers-as-classes-a1 (solution): 6 < 9; 9 = 3 + 6 | numeral arithmetic and order on omega; verify/ch02/exr-integers-as-classes-a1.py
exr-integers-as-classes-b1 (solution): 0 != 2, 1 != 2 (distinct numerals) | thm-omega-order (a) (0 < 2 gives 0 != 2), covered by the numeral-comparison exemption in the intro; verify/ch02/exr-integers-as-classes-b1.py
exr-integers-as-classes-b1 (solution): rearrangements in (b), (c) | thm-omega-arithmetic-laws (b), (c) (cited); verify/ch02/exr-integers-as-classes-b1.py
exr-integers-as-classes-c1 (solution): rearrangement in (b) | thm-omega-arithmetic-laws (b), (c) (cited); verify/ch02/exr-integers-as-classes-c1.py
-->
