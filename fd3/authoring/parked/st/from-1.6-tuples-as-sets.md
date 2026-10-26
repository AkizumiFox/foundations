# Parked: from old Section 1.6, tuples and lists as sets

<!-- Parked from fd3 (fd3/authoring/design/layout-proposal.md §4, approved 2026-10-26). Not part of any book's src; nothing builds or scans it.
Old section: fd3 1.6 Order and Well-Ordering of the Natural Numbers (part) (06-order-on-omega.md)
Labels: prp-tuples-as-sets
Intended home: ST.1 (tuples and lists coded as sets)
-->

## Tuples and lists as sets

*Sets and Functions*, Chapter 1 used \( n \)-tuples \( (x_1, \dots, x_n) \) with \( n \) a variable, as working rule (W5), and stated working rule (W2) for lists (*Sets and Functions*, Section 1.2); *Sets and Functions*, Chapters 3 and 4 write \( \{x_1, \dots, x_n\} \) with \( n \) a variable. With pairs built from sets (@thm-kuratowski-pair) and with \( \{1, \dots, n\} = \mathrm{S}(n) \setminus \{0\} \) (@thm-omega-order (e)), we can now say what they are. An \( n \)-tuple, for \( n \ge 3 \), is a list of entries labeled by \( 1, \dots, n \), and a function on \( \{1, \dots, n\} \) is exactly that.

::: {#prp-tuples-as-sets}
[Tuples and Lists as Sets]

Let \( X \) be a set. For \( n = 2 \), an **\( n \)-tuple in \( X \)** is a pair \( (x_1, x_2) \) with \( x_1, x_2 \in X \) (@def-kuratowski-pair), and \( X^2 \coloneqq X \times X \). For \( n \in \omega \) with \( n \ge 3 \), an **\( n \)-tuple in \( X \)** is the graph \( G \) of a function \( x \colon \{1, \dots, n\} \to X \); with \( x_k \coloneqq x(k) \) it is written
\[
(x_1, \dots, x_n) \coloneqq \bigl\{ (k, x_k) : k \in \{1, \dots, n\} \bigr\} = G .
\]

::: {.enumerate options="label=(\alph*)"}
1. For \( n \ge 2 \), there is exactly one set \( X^n \) whose elements are exactly the \( n \)-tuples in \( X \); for \( n = 2 \) it is \( X \times X \).
2. For \( n \ge 2 \), two \( n \)-tuples \( (x_1, \dots, x_n) \) and \( (y_1, \dots, y_n) \) in \( X \) are equal if and only if \( x_k = y_k \) for every \( k \in \{1, \dots, n\} \).
3. For \( n \ge 3 \), no \( n \)-tuple is a pair; and for \( n, n' \ge 3 \) with \( n \ne n' \), no \( n \)-tuple is an \( n' \)-tuple.
4. For every \( n \in \omega \) (\( n = 0, 1 \) allowed) and every function \( x \colon \{1, \dots, n\} \to X \), the list
\[
\{x_1, \dots, x_n\} \coloneqq \bigl\{ y \in X : y = x_k \text{ for some } k \in \{1, \dots, n\} \bigr\}
\]
is a set: the image \( x(\{1, \dots, n\}) \) of @fd2:def-image.
5. For \( n \ge 3 \), no \( n \)-tuple is an element of \( \omega \).
:::
:::

The tuple is the graph alone, without the codomain \( X \), so the same list of entries is the same tuple in every set that contains them.

Since a natural number is also a set, an exponent \( n \in \omega \) could be read in more than one way. In \( X^n \) the exponent is always read as a number: \( X^n \) is the set of \( n \)-tuples of (a), not the set \( Y^X \) of *Sets and Functions*, Section 2.1 taken with \( Y = X \) and with the set \( n \) as exponent, whose elements are pairs (graph, codomain) with graphs on \( n = \{0, \dots, n - 1\} \). And \( X^n \) is written only for a declared set of entries \( X \), never for \( X \in \omega \); for \( b \in \omega \), \( b^n \) is always the power defined above. For example, the power \( 2^2 \) is \( 4 = \{0, 1, 2, 3\} \), while \( 2 \times 2 \) is a set of four pairs.

::: {.idea}
Each clause unwinds a definition. Sets come from (Z5) and (Z6); equality of tuples is equality of graphs, which is agreement of values. For (c) and (e), look at the elements: an \( n \)-tuple with \( n \ge 3 \) has at least three elements, all of them pairs, while a pair has at most two elements and every non-zero natural number has the element \( \emptyset \), which is not a pair.
:::

::: {.proof}
In (a)–(c) and (e), \( n \ge 3 \) unless \( n = 2 \) is named. First, \( \{1, \dots, n\} \) is a set, by (Z6) of @ax-zf-fragment inside \( \omega \), and \( 1, 2, 3 \) are distinct elements of it: \( 1 < 2 < 3 \) by @thm-omega-order (b) (\( 2 = \mathrm{S}(1) \), \( 3 = \mathrm{S}(2) \)), so the three are distinct by irreflexivity and transitivity (@thm-omega-order (a)); \( 1 \le 1, 2, 3 \), and each of them is \( \le 3 \le n \), so they lie in \( \{1, \dots, n\} \).

(a) In each case the set is unique by (Z1), since two sets with the same elements are equal. For \( n = 2 \), \( X \times X \) is a set by @prp-cartesian-product-exists, and its elements are exactly the pairs \( (x_1, x_2) \) with \( x_1, x_2 \in X \). For \( n \ge 3 \), every \( n \)-tuple is a subset of \( \{1, \dots, n\} \times X \), so the set
\[
\bigl\{ G \in \powerset{\{1, \dots, n\} \times X} : (G, X) \text{ is a function } \{1, \dots, n\} \to X \bigr\}
\]
exists by @prp-cartesian-product-exists and (Z5), (Z6) of @ax-zf-fragment, and its elements are exactly the \( n \)-tuples in \( X \). This is \( X^n \).

(b) For \( n = 2 \) this is @thm-kuratowski-pair. For \( n \ge 3 \), let \( G \) and \( G' \) be the graphs of \( x \) and \( y \). If \( x_k = y_k \) for every \( k \), then each element \( (k, x_k) \) of \( G \) is \( (k, y_k) \in G' \), and vice versa, so \( G = G' \) by (Z1). Conversely, if \( G = G' \), then \( (k, x_k) \in G' \) for each \( k \), so \( x_k = y_k \) by (Fn2) of @fd2:def-function for \( y \).

(c) An \( n \)-tuple contains the three pairs \( (1, x_1) \), \( (2, x_2) \), \( (3, x_3) \), which are distinct by @thm-kuratowski-pair, since their first coordinates are. Every element of a pair \( (a, b) = \{\{a\}, \{a, b\}\} \) is \( \{a\} \) or \( \{a, b\} \). If a pair contained three distinct elements \( u, v, w \), then \( u \) and \( v \), being different, would be \( \{a\} \) and \( \{a, b\} \) in some order, and \( w \), being one of these two, would equal \( u \) or \( v \). So a pair has no three distinct elements, and an \( n \)-tuple is not a pair.

Let \( 3 \le n < n' \). The \( n' \)-tuple contains a pair with first coordinate \( n' \), since \( 1 \le n' \le n' \) (@thm-omega-order (d), with \( n' \ne 0 \)). Every element of the \( n \)-tuple is a pair \( (k, x_k) \) with \( k \le n \), and \( k = n' \) would give \( n' \le n \), which trichotomy rules out since \( n < n' \). By @thm-kuratowski-pair, no element of the \( n \)-tuple has first coordinate \( n' \), so the two sets differ. The case \( n' < n \) is the same with the roles exchanged.

(d) Let \( n \in \omega \) and \( x \colon \{1, \dots, n\} \to X \). The set \( \{x_1, \dots, x_n\} \) is cut out of \( X \) by a condition, so it is a set by (Z6) of @ax-zf-fragment; by @fd2:def-image it is \( x(\{1, \dots, n\}) \). For \( n = 0 \) it is \( \emptyset \), since \( \{1, \dots, 0\} = \emptyset \).

(e) An \( n \)-tuple \( t \) contains \( (1, x_1) \), so \( t \ne \emptyset = 0 \). Each element of \( t \) is a pair \( (k, x_k) = \{\{k\}, \{k, x_k\}\} \), which has the element \( \{k\} \), so no element of \( t \) is \( \emptyset \). Every \( m \in \omega \) with \( m \ne 0 \) has \( 0 = \emptyset \) as an element (@lem-omega-transitive (e)). So \( t \) is neither \( 0 \) nor any other element of \( \omega \).
:::

Clause (d) is the second half of working rule (W2): @fd2:prp-finite-max and @fd2:def-finite in *Sets and Functions*, Chapters 3 and 4, speak of \( \{x_1, \dots, x_n\} \) for a variable \( n \), and this is the set they mean. Clauses (a) and (b) are working rule (W5) for \( n \)-tuples. Clause (c) bears out the convention of *Sets and Functions*, Chapter 1, that a triple is not a pair, and (e), with @prp-pair-not-natural for \( n = 2 \), that no pair or \( n \)-tuple is a natural number.

<!-- dependency ledger
prp-tuples-as-sets (proof): 1 < 2 < 3 and 3 <= n for n >= 3 | thm-omega-order (a), (b) (cited)
prp-tuples-as-sets (proof): first coordinates of a set of pairs; a pair (k, y) has the element {k} | def-kuratowski-pair (cited)
-->
