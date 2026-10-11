# Order and Well-Ordering of the Natural Numbers

Chapter 7 compared natural numbers with the order of the real line, and proved that every non-empty set of natural numbers has a least element (@thm-well-ordering) from that order and induction. In \( \omega \) there is no real line to borrow from. But the von Neumann numerals carry their order inside them: \( 3 = \{0, 1, 2\} \) is the set of the numbers before it. This section takes "is an element of" as the order, proves that it is a strict total order and a well-ordering, ties it to the arithmetic of the previous section, and then collects three groups of facts about \( \omega \): powers and parity, \( n \)-tuples, and lists of variable length.

## Less than is "element of"

The numerals of @exm-von-neumann-numerals were built so that each one collects all the earlier ones: \( 1 = \{0\} \), \( 2 = \{0, 1\} \), \( 4 = \{0, 1, 2, 3\} \). So "\( m \) comes before \( n \)" can be read off the sets themselves, without any new structure.

*\( m \) is less than \( n \) when \( m \) is one of the elements of \( n \).*

::: {#def-omega-order}
[Order on \( \omega \)]

For \( m, n \in \omega \), we write \( m < n \) if \( m \in n \), and \( m \le n \) if \( m < n \) or \( m = n \). As usual, \( n > m \) means \( m < n \), and \( n \ge m \) means \( m \le n \).
:::

In words: \( m < n \) is membership, read as an order. For example \( 2 < 4 \), because \( 2 \in \{0, 1, 2, 3\} \); \( 0 < n \) for every \( n \ne 0 \), by @lem-omega-transitive (e); and no \( m \) satisfies \( m < 0 \), because \( 0 = \emptyset \) has no elements. A minimal change gives a non-example: \( 4 < 2 \) fails, since \( 4 \) is not one of \( 0, 1 \). The relation \( \le \) is "\( \in \) or \( = \)"; exercise B1 shows that on \( \omega \) it is also \( \subseteq \).

Nothing in the definition says that \( < \) behaves like an order. For arbitrary sets, membership does not: it can fail to be transitive, as the warning below shows. That it is a strict total order on \( \omega \) is the first theorem of this section, and the induction theorem does the work.

::: {#thm-omega-order}
[Order on \( \omega \)]

::: {.enumerate options="label=(\alph*)"}
1. \( < \) is a strict total order on \( \omega \): for all \( k, m, n \in \omega \), never \( n < n \); if \( k < m \) and \( m < n \), then \( k < n \); and **exactly one** of \( m < n \), \( m = n \), \( n < m \) holds.
2. For \( m, n \in \omega \), \( m < \mathrm{S}(n) \) if and only if \( m \le n \). Hence no \( k \in \omega \) satisfies \( n < k < \mathrm{S}(n) \).
3. Every \( n \in \omega \) is the set of the natural numbers less than it: \( n = \{ m \in \omega : m < n \} \). Hence \( \{0, \dots, n\} \coloneqq \{ k \in \omega : k \le n \} \) equals \( \mathrm{S}(n) \).
4. \( 0 \le n \) for every \( n \in \omega \); if \( n \ne 0 \), then \( 1 \le n \); and \( 0 < 1 \).
5. For \( n \in \omega \), \( \{1, \dots, n\} \coloneqq \{ k \in \omega : 1 \le k \le n \} \) equals \( \mathrm{S}(n) \setminus \{0\} \).
:::
:::

::: {.idea}
Irreflexivity and transitivity are facts already proved about the sets in \( \omega \): no \( n \) is an element of itself, and every \( n \) is a transitive set (@lem-omega-transitive). The real content is trichotomy. We prove "for every \( m \): \( m \in n \), \( m = n \) or \( n \in m \)" by induction on \( n \), keeping \( m \) universally quantified inside the property. In the step, the awkward case is \( n \in m \): we must place \( \mathrm{S}(n) \) relative to \( m \). A separate induction shows that the successor preserves \( \in \), and that settles it. The rest unwinds the definition of \( \mathrm{S}(n) \).
:::

::: {.proof}
(a) *Irreflexive:* \( n \notin n \) by @lem-omega-transitive (c). *Transitive:* if \( k \in m \) and \( m \in n \), then \( m \subseteq n \) because \( n \) is a transitive set (@lem-omega-transitive (a)), so \( k \in n \).

::: {.claim}
For all \( m, n \in \omega \): if \( m \in n \), then \( \mathrm{S}(m) \in \mathrm{S}(n) \).
:::

::: {.proofofclaim}
We use @thm-omega-induction (b) on \( n \), for the property "for every \( m \in \omega \), if \( m \in n \), then \( \mathrm{S}(m) \in \mathrm{S}(n) \)". For \( n = 0 \) it holds vacuously, since no \( m \) lies in \( 0 = \emptyset \). Suppose it holds for \( n \), and let \( m \in \mathrm{S}(n) = n \cup \{n\} \). If \( m \in n \), then \( \mathrm{S}(m) \in \mathrm{S}(n) \) by the hypothesis, and \( \mathrm{S}(n) \subseteq \mathrm{S}(\mathrm{S}(n)) \), so \( \mathrm{S}(m) \in \mathrm{S}(\mathrm{S}(n)) \). If \( m = n \), then \( \mathrm{S}(m) = \mathrm{S}(n) \in \mathrm{S}(\mathrm{S}(n)) \). So the property holds for \( \mathrm{S}(n) \).
:::

*Trichotomy, at least one.* We use @thm-omega-induction (b) on \( n \), for the property \( T(n) \): "for every \( m \in \omega \), \( m \in n \) or \( m = n \) or \( n \in m \)".

*Base case.* Let \( m \in \omega \). Then \( m = 0 \) or \( 0 \in m \), by @lem-omega-transitive (e). So \( T(0) \) holds.

*Inductive step.* Suppose \( T(n) \), and let \( m \in \omega \). By \( T(n) \) there are three cases. If \( m \in n \) or \( m = n \), then \( m \in n \cup \{n\} = \mathrm{S}(n) \). If \( n \in m \), then \( \mathrm{S}(n) \in \mathrm{S}(m) = m \cup \{m\} \) by the claim, so \( \mathrm{S}(n) \in m \) or \( \mathrm{S}(n) = m \). In every case \( m \in \mathrm{S}(n) \), \( m = \mathrm{S}(n) \) or \( \mathrm{S}(n) \in m \), which is \( T(\mathrm{S}(n)) \).

*Trichotomy, at most one.* If \( m \in n \) and \( m = n \), then \( n \in n \); if \( m = n \) and \( n \in m \), then \( n \in n \); if \( m \in n \) and \( n \in m \), then \( m \in m \) by transitivity. Each contradicts irreflexivity.

(b) By @def-set-successor, \( m \in \mathrm{S}(n) = n \cup \{n\} \) if and only if \( m \in n \) or \( m = n \), that is, \( m \le n \). Now suppose \( n < k \) and \( k < \mathrm{S}(n) \). Then \( k \le n \), so \( k = n \), giving \( n < n \), or \( k < n \), giving \( n < n \) by transitivity. Both contradict irreflexivity.

(c) \( (\supseteq) \): if \( m \in \omega \) and \( m < n \), then \( m \in n \) by definition. \( (\subseteq) \): if \( m \in n \), then \( m \in \omega \), because \( \omega \) is a transitive set (@lem-omega-transitive (b)), and \( m < n \). Applying this to \( \mathrm{S}(n) \), which lies in \( \omega \) by (P2) of @thm-omega-peano, and using (b), \( \mathrm{S}(n) = \{ k \in \omega : k < \mathrm{S}(n) \} = \{ k \in \omega : k \le n \} \).

(d) By @lem-omega-transitive (e), \( n = 0 \) or \( 0 \in n \); that is, \( 0 \le n \). Let \( n \ne 0 \). By @lem-omega-transitive (d), \( n = \mathrm{S}(k) \) for some \( k \in \omega \), and \( 0 \le k \). If \( k = 0 \), then \( n = \mathrm{S}(0) = 1 \). If \( 0 < k \), then \( 1 = \mathrm{S}(0) < \mathrm{S}(k) = n \) by the claim. So \( 1 \le n \). Finally \( 0 \in \{0\} = \mathrm{S}(0) = 1 \), so \( 0 < 1 \).

(e) Let \( k \in \mathrm{S}(n) \setminus \{0\} \). Then \( k \in \omega \) (as in (c)), \( k \le n \) by (b), and \( 1 \le k \) by (d), since \( k \ne 0 \). Conversely, let \( k \in \omega \) with \( 1 \le k \le n \). Then \( k \in \mathrm{S}(n) \) by (b). And \( k \ne 0 \): otherwise \( 1 \le 0 \), but \( 1 \ne 0 \) by (P3) of @thm-omega-peano and \( 1 \notin 0 = \emptyset \). This proves the theorem.
:::

So the notation of Chapter 7, \( \{0, \dots, n\} \) and \( \{1, \dots, n\} \), keeps its meaning on \( \omega \), and the two sets are \( \mathrm{S}(n) \) and \( \mathrm{S}(n) \setminus \{0\} \); in particular \( \{1, \dots, 0\} = \emptyset \). In the "plus one" notation of @def-omega-arithmetic, (b) says that \( n + 1 \) is the next number after \( n \), and (d) with @cor-omega-successor-cancellation gives \( 1 \le k + 1 \) for every \( k \in \omega \), since \( k + 1 \ne 0 \).

::: {.warning}
**On arbitrary sets, \( \in \) is not transitive.** \( \emptyset \in \{\emptyset\} \) and \( \{\emptyset\} \in \{\{\emptyset\}\} \), but \( \emptyset \notin \{\{\emptyset\}\} \), whose only element is \( \{\emptyset\} \ne \emptyset \). The conclusion "\( k \in m \) and \( m \in n \) give \( k \in n \)" is false in general; on \( \omega \) it holds by a theorem, @lem-omega-transitive (a): the elements of \( \omega \) are transitive sets. Membership by itself does not give it.
:::

## Well-ordering

In Chapter 7, @thm-well-ordering was derived from @ax-induction, which there was an axiom. On \( \omega \), induction is a theorem (@thm-omega-induction), so well-ordering becomes one too. The proof here takes a different route from Chapter 7's strong induction, and the order of \( \omega \) as membership makes it short.

::: {#thm-omega-well-ordering}
[Well-Ordering of \( \omega \)]

Every **non-empty** subset \( A \subseteq \omega \) has a least element: an \( a \in A \) with \( a \le x \) for every \( x \in A \). The least element is unique.
:::

::: {.idea}
Suppose \( A \) has no least element. Then we can show, by induction, that no natural number \( n \) contains an element of \( A \): \( n \cap A = \emptyset \). Passing from \( n \) to \( \mathrm{S}(n) = n \cup \{n\} \) adds only the element \( n \), and if \( n \) were in \( A \) while nothing below it is, \( n \) would be least. But \( \mathrm{S}(a) \) contains \( a \), so no \( a \) can lie in \( A \), and \( A \) is empty.
:::

::: {.proof}
Let \( A \subseteq \omega \) be non-empty, and suppose, for a contradiction, that \( A \) has no least element. Let
\[
B \coloneqq \{ n \in \omega : n \cap A = \emptyset \} ,
\]
a set by (Z6) of @ax-zf-fragment. We show that \( B \) is inductive in the sense of @thm-omega-induction (a). First, \( 0 \in B \), since \( 0 = \emptyset \). Next, let \( n \in B \). Then
\[
\mathrm{S}(n) \cap A = (n \cap A) \cup (\{n\} \cap A) = \{n\} \cap A .
\]
Suppose \( n \in A \). Let \( x \in A \). Then \( x \notin n \), because \( n \cap A = \emptyset \); that is, \( x < n \) fails, so \( x = n \) or \( n < x \) by trichotomy (@thm-omega-order (a)), and \( n \le x \). Hence \( n \) is a least element of \( A \), contrary to our supposition. So \( n \notin A \), \( \mathrm{S}(n) \cap A = \emptyset \), and \( \mathrm{S}(n) \in B \). By @thm-omega-induction (a), \( B = \omega \).

Since \( A \) is non-empty, there is some \( a \in A \). Then \( \mathrm{S}(a) \in \omega = B \), so \( \mathrm{S}(a) \cap A = \emptyset \); but \( a \in \mathrm{S}(a) \cap A \). This contradiction shows, by RAA (@def-rule-raa), that \( A \) has a least element.

*Uniqueness.* If \( a \) and \( a' \) are least elements, then \( a \le a' \) and \( a' \le a \). If \( a \ne a' \), these give \( a < a' \) and \( a' < a \), so \( a < a \) by transitivity, contradicting irreflexivity (@thm-omega-order (a)). So \( a = a' \).
:::

The proof concludes an existence statement from a contradiction, so its last step is RAA, not \( \rulename{\neg I} \): what is refuted is "\( A \) has no least element", and the double negation is removed classically. The statement is that of @thm-well-ordering, read on \( \omega \); there the proof went through strong induction on \( \nN \subseteq \nR \), here through the inductive set \( B \).

Both hypotheses are needed. The empty set is a subset of \( \omega \) with no least element, since a least element must be an element of the set. The hypothesis \( A \subseteq \omega \) is needed too. Read with the order of @def-omega-order, "\( \in \) or \( = \)", the non-empty set \( \{0, \{1\}\} = \{\emptyset, \{\{\emptyset\}\}\} \) has no least element: neither \( \emptyset \in \{\{\emptyset\}\} \) (the only element of \( \{\{\emptyset\}\} \) is \( \{\emptyset\} \ne \emptyset \)) nor \( \{\{\emptyset\}\} \in \emptyset \) holds, and the two elements are different, so neither is \( \le \) the other. Outside \( \omega \), membership need not even compare two sets (compare the warning above). For sets of numbers, the warning after @thm-well-ordering gives \( \nZ \) and the positive rationals.

::: {.check}
Is \( 3 < 5 \)? What is the \( j \in \omega \) with \( 5 = 2 + j \)?
:::

::: {.solution}
Yes: \( 3 \in \mathrm{S}(3) = 4 \) and \( 4 \subseteq 4 \cup \{4\} = 5 \), so \( 3 \in 5 \); by @thm-omega-order (c), \( 5 = \{0, 1, 2, 3, 4\} \). For the second question, \( j = 3 \): by @def-omega-arithmetic (a), \( 2 + 3 = \mathrm{S}(2 + 2) = \mathrm{S}(4) = 5 \), using \( 2 + 2 = 4 \) from the Quick check of the previous section. By (a) of the next proposition, \( 3 \) is the only such \( j \).
:::

## Order and arithmetic

The order was defined by membership and the arithmetic by recursion. They are tied together by clause (a) of the next proposition: \( m \le n \) exactly when \( n \) is reached from \( m \) by adding something. Clauses (c), (e), (f) and (g) follow from it, with cancellation (b), the laws of @thm-omega-arithmetic-laws and trichotomy, together with (d) for (e) and (f) and an induction for (g); (d) itself needs only that a nonzero natural number is a successor and that a successor is never \( 0 \).

::: {#prp-omega-order-arithmetic}
[Order and Arithmetic on \( \omega \)]

For all \( k, m, n, b \in \omega \):

::: {.enumerate options="label=(\alph*)"}
1. \( m \le n \) if and only if \( n = m + j \) for some \( j \in \omega \); this \( j \) is then unique, and is written \( n - m \). Moreover \( m < n \) if and only if \( n = m + j \) for some \( j \ne 0 \).
2. If \( m + k = n + k \), then \( m = n \).
3. If \( m < n \), then \( m + k < n + k \).
4. If \( mn = 0 \), then \( m = 0 \) or \( n = 0 \).
5. If \( m < n \) and \( k \ne 0 \), then \( mk < nk \).
6. If \( mk = nk \) and \( k \ne 0 \), then \( m = n \).
7. *(Induction from \( b \).)* Let \( P(n) \) be a property of natural numbers. If \( P(b) \) holds and, for every \( n \in \omega \) with \( n \ge b \), \( P(n) \) implies \( P(n + 1) \), then \( P(n) \) holds for every \( n \in \omega \) with \( n \ge b \).
:::
:::

::: {.idea}
Cancellation (b) needs no order: induct on \( k \) and peel off one successor at a time with @cor-omega-successor-cancellation. For (a), "\( m \le m + j \)" is an induction on \( j \), and the converse is an induction on \( n \) whose step uses that nothing lies between \( n \) and \( n + 1 \). Then (c), (e) and (f) translate an inequality \( m < n \) into an equation \( n = m + j \) with \( j \ne 0 \), compute, and translate back; (d) writes \( m \) and \( n \) as successors and uses that a successor is never \( 0 \). Finally (g) shifts the start of an induction from \( 0 \) to \( b \).
:::

::: {.proof}
All inductions are by @thm-omega-induction (b), and "Law (x)" refers to clause (x) of @thm-omega-arithmetic-laws. We prove (b) first, since (a) uses it.

(b) Induct on \( k \) for "for all \( m, n \): \( m + k = n + k \Rightarrow m = n \)". For \( k = 0 \), \( m + 0 = m \) and \( n + 0 = n \). If the statement holds for \( k \) and \( m + (k + 1) = n + (k + 1) \), then \( (m + k) + 1 = (n + k) + 1 \) by @def-omega-arithmetic (a), so \( m + k = n + k \) by @cor-omega-successor-cancellation, and \( m = n \) by the hypothesis.

(a) \( (\Leftarrow) \) Fix \( m \) and induct on \( j \) for "\( m \le m + j \)". For \( j = 0 \), \( m + 0 = m \). If \( m \le m + j \), then, since \( m + j < \mathrm{S}(m + j) \) by @thm-omega-order (b), transitivity (or substitution, if \( m = m + j \)) gives
\[
m < \mathrm{S}(m + j) = m + (j + 1) ,
\]
the equality by @def-omega-arithmetic (a). So \( m \le m + (j + 1) \).

\( (\Rightarrow) \) Induct on \( n \) for "for every \( m \le n \) there is \( j \in \omega \) with \( n = m + j \)". For \( n = 0 \): \( m < 0 \) is impossible, since \( 0 = \emptyset \), so \( m = 0 \), and \( 0 = 0 + 0 \). Suppose the statement holds for \( n \), and let \( m \le n + 1 \). If \( m = n + 1 \), take \( j = 0 \). Otherwise \( m < n + 1 = \mathrm{S}(n) \), so \( m \le n \) by @thm-omega-order (b); by the hypothesis \( n = m + j \) for some \( j \), and then \( n + 1 = (m + j) + 1 = m + (j + 1) \) by @def-omega-arithmetic (a).

*Uniqueness.* If \( m + j = m + j' \), then \( j + m = j' + m \) by Law (b), so \( j = j' \) by (b) of this proposition.

*The strict case.* If \( n = m + j \), then \( j = 0 \) if and only if \( n = m \): if \( j = 0 \), then \( n = m + 0 = m \); if \( n = m \), then \( m + j = m = m + 0 \), so \( j = 0 \) by uniqueness. Since \( m < n \) holds exactly when \( m \le n \) and \( m \ne n \) (by @def-omega-order and irreflexivity, @thm-omega-order (a)), \( m < n \) holds if and only if \( n = m + j \) with \( j \ne 0 \).

(c) Let \( m < n \), so \( n = m + j \) with \( j \ne 0 \) by (a). Then
\[
n + k = (m + j) + k = m + (k + j) = (m + k) + j
\]
by Laws (c), (b) and (c). Since \( j \ne 0 \), (a) gives \( m + k < n + k \).

(d) Let \( mn = 0 \) and \( n \ne 0 \); we show \( m = 0 \). By @lem-omega-transitive (d), \( n = j + 1 \) for some \( j \in \omega \), so \( 0 = mn = mj + m \) by @def-omega-arithmetic (b). If \( m \ne 0 \), then \( m = i + 1 \) for some \( i \in \omega \), and
\[
0 = mj + (i + 1) = (mj + i) + 1 ,
\]
by @def-omega-arithmetic (a), which contradicts @cor-omega-successor-cancellation. So \( m = 0 \).

(e) Let \( m < n \) and \( k \ne 0 \). By (a), \( n = m + j \) with \( j \ne 0 \), so \( nk = (m + j)k = mk + jk \) by Law (d). By (d), \( jk \ne 0 \), since \( j \ne 0 \) and \( k \ne 0 \). By (a), \( mk < nk \).

(f) Let \( mk = nk \) and \( k \ne 0 \). If \( m < n \), then \( mk < nk \) by (e), contradicting \( mk = nk \) and irreflexivity; likewise if \( n < m \). By trichotomy, \( m = n \).

(g) Let \( Q(i) \) be "\( P(b + i) \)", for \( i \in \omega \). \( Q(0) \) is \( P(b + 0) = P(b) \). If \( Q(i) \) holds, then \( b + i \ge b \) by (a), so the hypothesis gives \( P((b + i) + 1) \); and \( (b + i) + 1 = b + (i + 1) \) by @def-omega-arithmetic (a), so \( Q(i + 1) \) holds. By @thm-omega-induction (b), \( Q(i) \) holds for every \( i \in \omega \). Finally, if \( n \ge b \), then \( n = b + i \) for some \( i \) by (a), and \( P(n) \) is \( Q(i) \).
:::

Clause (a) is how subtraction appears on \( \omega \): \( n - m \) is defined only when \( m \le n \), as the unique \( j \) with \( m + j = n \). For example \( 5 - 2 = 3 \), by the Quick check above, and \( n - 0 = n \). Clause (g) is the "induction from a base" that Chapter 7 used as @thm-induction, now proved on \( \omega \).

## Powers and parity

Chapter 8 counted with powers \( 2^m 3^n \) and with even and odd numbers, and took both from the real numbers and the integers. Here are the facts it used, proved on \( \omega \). They are recorded for the citing rule at the end of this chapter, which says how Chapter 8's counting arguments read on \( \omega \).

For \( b \in \omega \), the powers \( b^n \) (\( n \in \omega \)) are defined by @thm-omega-recursion with \( X = \omega \), \( a = 1 \) and \( g(n, x) = x \cdot b \):
\[
b^0 \coloneqq 1, \qquad b^{n+1} \coloneqq b^n \cdot b .
\]
These are the two equations of @def-power, now on \( \omega \); so \( b^1 = 1 \cdot b = b \) by @thm-omega-arithmetic-laws (e).

::: {#prp-omega-powers-parity}
[Powers and Parity on \( \omega \)]

For all \( b, m, n \in \omega \):

::: {.enumerate options="label=(\alph*)"}
1. \( b^{m+n} = b^m \cdot b^n \);
2. if \( b \ne 0 \), then \( b^n \ne 0 \);
3. if \( b > 1 \) and \( m < n \), then \( b^m < b^n \);
4. there is exactly one pair \( (q, r) \) with \( q \in \omega \), \( r \in \{0, 1\} \) and \( n = 2q + r \). In particular, no \( n \in \omega \) is both of the form \( 2q \) and of the form \( 2q' + 1 \).
:::
:::

::: {.idea}
(a) and (b) are inductions on \( n \) following the definition of \( b^n \). For (c), first \( b^j > 1 \) for \( j \ge 1 \), by induction from \( 1 \); then write \( n = m + j \) and use (a). For (d), existence is an induction (a number is even or odd, and adding one swaps the two), and uniqueness reduces, after canceling, to "\( r = 2j + r' \) with \( j \ge 1 \)", which makes \( r \ge 2 \).
:::

::: {.proof}
"Law (x)" refers to @thm-omega-arithmetic-laws, and "Order (x)" to @prp-omega-order-arithmetic.

(a) Fix \( m \) and induct on \( n \) (@thm-omega-induction (b)). For \( n = 0 \): \( b^{m+0} = b^m = b^m \cdot 1 = b^m b^0 \), by Law (e). If \( b^{m+n} = b^m b^n \), then
\[
b^{m+(n+1)} = b^{(m+n)+1} = b^{m+n} b = (b^m b^n) b = b^m (b^n b) = b^m b^{n+1} ,
\]
by @def-omega-arithmetic (a), the definition of powers, the hypothesis, Law (g), and the definition again.

(b) Let \( b \ne 0 \); induct on \( n \). \( b^0 = 1 \ne 0 \) by @cor-omega-successor-cancellation (\( 1 = 0 + 1 \)). If \( b^n \ne 0 \), then \( b^{n+1} = b^n b \ne 0 \) by Order (d).

(c) Let \( b > 1 \). Then \( b > 0 \), by \( 0 < 1 \) (@thm-omega-order (d)) and transitivity, so \( b \ne 0 \). First, \( b^j > 1 \) for every \( j \ge 1 \), by Order (g) with base \( 1 \): \( b^1 = b > 1 \); and if \( b^j > 1 \), then
\[
b^{j+1} = b^j b > 1 \cdot b = b > 1
\]
by Order (e) (with \( b \ne 0 \)), Law (e) and transitivity. Now let \( m < n \). By Order (a), \( n = m + j \) with \( j \ne 0 \), so \( j \ge 1 \) by @thm-omega-order (d), and \( b^j > 1 \). By (b), \( b^m \ne 0 \). Then, by Order (e), Law (e), Law (f) and (a),
\[
b^m = 1 \cdot b^m < b^j b^m = b^m b^j = b^{m+j} = b^n .
\]

(d) *Existence,* by @thm-omega-induction (b). For \( n = 0 \): \( 0 = 2 \cdot 0 + 0 \). Suppose \( n = 2q + r \) with \( r \in \{0, 1\} \). If \( r = 0 \), then \( n = 2q \) and \( n + 1 = 2q + 1 \). If \( r = 1 \), then
\[
n + 1 = (2q + 1) + 1 = 2q + 2 = 2q + 2 \cdot 1 = 2(q + 1) = 2(q + 1) + 0 ,
\]
by Law (c) and \( 1 + 1 = 2 \) (after @def-omega-arithmetic), Law (e), and Law (d).

*Uniqueness.* Let \( 2q + r = 2q' + r' \) with \( r, r' \in \{0, 1\} \). Suppose first that \( q < q' \). By Order (a), \( q' = q + j \) with \( j \ne 0 \), so
\[
2q + r = 2(q + j) + r' = 2q + (2j + r')
\]
by Laws (d) and (c), and canceling \( 2q \) (Order (b), after Law (b)) gives \( r = 2j + r' \). Since \( j \ge 1 \) (@thm-omega-order (d)), Order (a) gives \( j = 1 + i \) for some \( i \in \omega \), and \( 2j + r' = (2 + 2i) + r' = 2 + (2i + r') \) by Laws (d), (e) and (c). So \( r = 2 + (2i + r') \ge 2 \) by Order (a). But \( r = 0 \) or \( r = 1 \), and both are \( < 2 = \mathrm{S}(1) \) by @thm-omega-order (b); this contradicts trichotomy. So \( q < q' \) is impossible, and \( q' < q \) is impossible by the same argument with the roles exchanged. By trichotomy \( q = q' \), and then \( r = r' \) by Order (b) (after Law (b)). The pairs \( (q, r) \) and \( (q', r') \) are therefore equal (@thm-kuratowski-pair).

If \( n = 2q = 2q + 0 \) and \( n = 2q' + 1 \), the pairs \( (q, 0) \) and \( (q', 1) \) would both represent \( n \), and they differ since \( 0 \ne 1 \); so no \( n \) is of both forms.
:::

Any other definition of powers on \( \omega \) by the same two equations, \( c(0) = 1 \) and \( c(n + 1) = c(n) \cdot b \), gives these powers, by the uniqueness half of @thm-omega-recursion. No proof in this chapter uses the proposition; it is here for the citing rule.

## Tuples and lists as sets

Chapter 6 used \( n \)-tuples \( (x_1, \dots, x_n) \) with \( n \) a variable, as working rule (W5), and stated working rule (W2) for lists (Section 6.1); Chapters 7 and 8 write \( \{x_1, \dots, x_n\} \) with \( n \) a variable. With pairs built from sets (@thm-kuratowski-pair) and with \( \{1, \dots, n\} = \mathrm{S}(n) \setminus \{0\} \) (@thm-omega-order (e)), we can now say what they are. An \( n \)-tuple, for \( n \ge 3 \), is a list of entries labeled by \( 1, \dots, n \), and a function on \( \{1, \dots, n\} \) is exactly that.

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
is a set: the image \( x(\{1, \dots, n\}) \) of @def-image.
5. For \( n \ge 3 \), no \( n \)-tuple is an element of \( \omega \).
:::
:::

The tuple is the graph alone, without the codomain \( X \), so the same list of entries is the same tuple in every set that contains them.

Since a natural number is also a set, an exponent \( n \in \omega \) could be read in more than one way. In \( X^n \) the exponent is always read as a number: \( X^n \) is the set of \( n \)-tuples of (a), not Chapter 6's set \( Y^X \) (Section 6.4) taken with \( Y = X \) and with the set \( n \) as exponent, whose elements are pairs (graph, codomain) with graphs on \( n = \{0, \dots, n - 1\} \). And \( X^n \) is written only for a declared set of entries \( X \), never for \( X \in \omega \); for \( b \in \omega \), \( b^n \) is always the power defined above. For example, the power \( 2^2 \) is \( 4 = \{0, 1, 2, 3\} \), while \( 2 \times 2 \) is a set of four pairs.

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

(b) For \( n = 2 \) this is @thm-kuratowski-pair. For \( n \ge 3 \), let \( G \) and \( G' \) be the graphs of \( x \) and \( y \). If \( x_k = y_k \) for every \( k \), then each element \( (k, x_k) \) of \( G \) is \( (k, y_k) \in G' \), and vice versa, so \( G = G' \) by (Z1). Conversely, if \( G = G' \), then \( (k, x_k) \in G' \) for each \( k \), so \( x_k = y_k \) by (Fn2) of @def-function for \( y \).

(c) An \( n \)-tuple contains the three pairs \( (1, x_1) \), \( (2, x_2) \), \( (3, x_3) \), which are distinct by @thm-kuratowski-pair, since their first coordinates are. Every element of a pair \( (a, b) = \{\{a\}, \{a, b\}\} \) is \( \{a\} \) or \( \{a, b\} \). If a pair contained three distinct elements \( u, v, w \), then \( u \) and \( v \), being different, would be \( \{a\} \) and \( \{a, b\} \) in some order, and \( w \), being one of these two, would equal \( u \) or \( v \). So a pair has no three distinct elements, and an \( n \)-tuple is not a pair.

Let \( 3 \le n < n' \). The \( n' \)-tuple contains a pair with first coordinate \( n' \), since \( 1 \le n' \le n' \) (@thm-omega-order (d), with \( n' \ne 0 \)). Every element of the \( n \)-tuple is a pair \( (k, x_k) \) with \( k \le n \), and \( k = n' \) would give \( n' \le n \), which trichotomy rules out since \( n < n' \). By @thm-kuratowski-pair, no element of the \( n \)-tuple has first coordinate \( n' \), so the two sets differ. The case \( n' < n \) is the same with the roles exchanged.

(d) Let \( n \in \omega \) and \( x \colon \{1, \dots, n\} \to X \). The set \( \{x_1, \dots, x_n\} \) is cut out of \( X \) by a condition, so it is a set by (Z6) of @ax-zf-fragment; by @def-image it is \( x(\{1, \dots, n\}) \). For \( n = 0 \) it is \( \emptyset \), since \( \{1, \dots, 0\} = \emptyset \).

(e) An \( n \)-tuple \( t \) contains \( (1, x_1) \), so \( t \ne \emptyset = 0 \). Each element of \( t \) is a pair \( (k, x_k) = \{\{k\}, \{k, x_k\}\} \), which has the element \( \{k\} \), so no element of \( t \) is \( \emptyset \). Every \( m \in \omega \) with \( m \ne 0 \) has \( 0 = \emptyset \) as an element (@lem-omega-transitive (e)). So \( t \) is neither \( 0 \) nor any other element of \( \omega \).
:::

Clause (d) is the second half of working rule (W2): Chapter 7's @prp-finite-max and Chapter 8's @def-finite speak of \( \{x_1, \dots, x_n\} \) for a variable \( n \), and this is the set they mean. Clauses (a) and (b) are working rule (W5) for \( n \)-tuples. Clause (c) bears out Chapter 6's convention that a triple is not a pair, and (e), with @prp-pair-not-natural for \( n = 2 \), that no pair or \( n \)-tuple is a natural number.

## Exercises

### A. Check your understanding

::: {#exr-order-on-omega-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. List the elements of \( \{ k \in \omega : k \le 3 \} \). Which natural number is this set?
2. True or false: for \( m, n \in \omega \), \( m < n \) implies \( m \subseteq n \). Justify your answer.
3. Find the least element of \( \{ n \in \omega : n \cdot n > 10 \} \), and say why it is least.
4. Which clause of @thm-omega-order says that the notation \( \{0, \dots, n\} \) of Chapter 7 still means what it meant there, and what set is it on \( \omega \)?
:::
:::

::: {.solution}
(a) \( 0, 1, 2, 3 \). By @thm-omega-order (c), the set is \( \mathrm{S}(3) = 4 \).

(b) True. If \( m < n \), then \( m \in n \), and \( n \) is a transitive set (@lem-omega-transitive (a)), so \( m \subseteq n \).

(c) The least element is \( 4 \). From the defining equations, \( 0 \cdot 0 = 0 \), \( 1 \cdot 1 = 1 \), \( 2 \cdot 2 = 4 \), \( 3 \cdot 3 = 9 \) and \( 4 \cdot 4 = 16 \); and \( 16 > 10 \), since \( 10 \in 16 = \{0, 1, \dots, 15\} \), while \( 0, 1, 4, 9 \) are all \( < 10 \), since each is an element of \( 10 = \{0, 1, \dots, 9\} \) (both by @thm-omega-order (c)). So \( 4 \) lies in the set. If \( x \) lies in the set and \( x < 4 \), then \( x \in 4 = \{0, 1, 2, 3\} \), and \( x \cdot x \in \{0, 1, 4, 9\} \), so \( x \cdot x < 10 \), and \( x \cdot x > 10 \) fails by trichotomy. Hence \( x < 4 \) is impossible, and \( 4 \le x \) by trichotomy. The set is non-empty, so @thm-omega-well-ordering promised a least element; this is it.

(d) Clause (c): \( \{0, \dots, n\} \coloneqq \{ k \in \omega : k \le n \} \) is \( \mathrm{S}(n) \). (Clause (e) does the same for \( \{1, \dots, n\} = \mathrm{S}(n) \setminus \{0\} \).)
:::

### B. Practice

::: {#exr-order-on-omega-b1}
[B1: Order as inclusion]

Prove that for all \( m, n \in \omega \), \( m \le n \) if and only if \( m \subseteq n \).
:::

::: {.solution}
\( (\Rightarrow) \) If \( m = n \), then \( m \subseteq n \). If \( m < n \), then \( m \in n \), and \( m \subseteq n \) because \( n \) is a transitive set (@lem-omega-transitive (a)).

\( (\Leftarrow) \) Let \( m \subseteq n \), and suppose \( m \le n \) fails. By trichotomy (@thm-omega-order (a)), \( n < m \), that is, \( n \in m \). Then \( n \in m \subseteq n \), so \( n \in n \), contradicting @lem-omega-transitive (c). Hence \( m \le n \).

So on \( \omega \), "\( \le \)" can be read as "\( \subseteq \)", just as "\( < \)" is "\( \in \)". For arbitrary sets the two readings come apart: \( \{1\} \subseteq \{0, 1\} = 2 \), but \( \{1\} \) is not a natural number at all: \( 0 \in 1 \in \{1\} \) while \( 0 \notin \{1\} \) (its only element is \( 1 \ne 0 \)), so \( \{1\} \) is not a transitive set, as every natural number is (@lem-omega-transitive (a)).
:::

::: {#exr-order-on-omega-b2}
[B2: A product is at least its factor]

Prove that for all \( m, n \in \omega \) with \( n \ge 1 \), \( m \le mn \). Show by an example that the hypothesis \( n \ge 1 \) is needed.
:::

::: {.solution}
Since \( 1 \le n \), @prp-omega-order-arithmetic (a) gives \( n = 1 + j \) for some \( j \in \omega \). Then
\[
mn = m(1 + j) = m \cdot 1 + mj = m + mj ,
\]
by @thm-omega-arithmetic-laws (d) and (e). By @prp-omega-order-arithmetic (a) again, \( m \le m + mj = mn \).

The hypothesis is needed: for \( m = 1 \) and \( n = 0 \), \( mn = 0 \), and \( 1 \le 0 \) is false, since \( 0 < 1 \) (@thm-omega-order (d)) and trichotomy.
:::

### C. Going deeper

::: {#exr-order-on-omega-c1}
[C1: Strong induction on ω]

Let \( P(n) \) be a property of natural numbers. Suppose that, for every \( n \in \omega \), if \( P(k) \) holds for every \( k \in \omega \) with \( k < n \), then \( P(n) \) holds. Prove that \( P(n) \) holds for every \( n \in \omega \).
:::

::: {.solution}
[Hint 1]

Consider the set of natural numbers at which \( P \) fails.
:::

::: {.solution}
[Hint 2]

If that set is non-empty, @thm-omega-well-ordering gives it a least element \( a \). What do you know about \( P(k) \) for \( k < a \)?
:::

::: {.solution}
Let \( A \coloneqq \{ n \in \omega : P(n) \text{ fails} \} \), a set by (Z6) of @ax-zf-fragment, and suppose, for a contradiction, that \( A \ne \emptyset \). By @thm-omega-well-ordering, \( A \) has a least element \( a \). Let \( k \in \omega \) with \( k < a \). If \( k \in A \), then \( a \le k \), and with \( k < a \) this gives \( k < k \) (by transitivity, or directly if \( a = k \)), contradicting irreflexivity (@thm-omega-order (a)). So \( k \notin A \), that is, \( P(k) \) holds. This holds for every \( k < a \), so the hypothesis gives \( P(a) \), contradicting \( a \in A \). Hence \( A = \emptyset \), and \( P(n) \) holds for every \( n \in \omega \).

This is the statement of @thm-strong-induction, read on \( \omega \). There it was derived from @ax-induction directly; here the route goes through well-ordering, which was itself proved from @thm-omega-induction. As there, the hypothesis at \( n = 0 \) is vacuous (no \( k < 0 \)), so it hands us \( P(0) \) outright.

**Marking scheme.** (10 points)
- 2: considers the set of failures (or argues by contradiction from a failure) and makes it a set.
- 3: applies @thm-omega-well-ordering, with the set non-empty, to obtain a least failure \( a \).
- 3: shows \( P(k) \) for every \( k < a \), using that \( a \) is least and the order facts.
- 2: applies the hypothesis at \( a \) and reaches the contradiction.
Fatal errors (0 for the step): citing @thm-strong-induction (a statement about Chapter 3's \( \nN \), not proved on \( \omega \)) instead of proving the result; taking a least element of a set not shown to be non-empty. A route by @thm-omega-induction (b) on "\( P(k) \) for every \( k < n \)" earns the same points: 2 for the property, 3 for the base (vacuous) and the use of @thm-omega-order (b) in the step, 3 for the step, 2 for deducing \( P(n) \) from the property at \( n + 1 \).
:::

::: {#exr-order-on-omega-c2}
[C2: Find the error]

Here is an attempted proof that any two natural numbers are comparable. Is the conclusion true? Is the proof correct? If not, give the first line that fails, the rule it breaks, and a counterexample to the step.

> **Claim.** For all \( m, n \in \omega \): \( m \in n \), \( m = n \) or \( n \in m \).
>
> (1) We use @thm-omega-induction (b) on \( n \), for the property "for every \( m \in \omega \): \( m \in n \), \( m = n \) or \( n \in m \)". (2) For \( n = 0 \): every \( m \) is \( 0 \) or contains \( 0 \), by @lem-omega-transitive (e). (3) Suppose the property holds for \( n \), and let \( m \in \omega \). (4) If \( m \in n \) or \( m = n \), then \( m \in n \cup \{n\} = \mathrm{S}(n) \). (5) If \( n \in m \), then \( \mathrm{S}(n) \le m \), because nothing lies strictly between \( n \) and \( \mathrm{S}(n) \): no \( k \in \omega \) has \( n \in k \in \mathrm{S}(n) \). (6) In every case \( m \in \mathrm{S}(n) \), \( m = \mathrm{S}(n) \) or \( \mathrm{S}(n) \in m \), which is the property for \( \mathrm{S}(n) \). (7) By @thm-omega-induction (b), the claim holds.
:::

::: {.solution}
The conclusion is **true**: it is trichotomy, @thm-omega-order (a). The proof is **not** correct.

*The failing line is (5).* Its reason, "nothing lies strictly between \( n \) and \( \mathrm{S}(n) \)", is true (it follows from irreflexivity and transitivity, as in @thm-omega-order (b)), but it does not give \( \mathrm{S}(n) \le m \). To pass from "\( m \) is not strictly between \( n \) and \( \mathrm{S}(n) \)" to "\( \mathrm{S}(n) \in m \) or \( \mathrm{S}(n) = m \)", one must know that if neither holds, then \( m \in \mathrm{S}(n) \). That is trichotomy for \( \mathrm{S}(n) \) and \( m \): an instance of the claim being proved, at a number the induction has not reached. So the stated reason gives (5) only by assuming the goal (circular). Without that, (5) asserts the general fact "\( n \in m \Rightarrow \mathrm{S}(n) \le m \)", which is true but not yet proved. Either way, line (5) rests on an unavailable fact: entry (N9) of @exm-not-allowed-catalogue.

*Counterexample to the step.* The inference "\( x \in y \) and nothing lies strictly between \( x \) and \( x \cup \{x\} \), so \( x \cup \{x\} \in y \) or \( x \cup \{x\} = y \)" fails for sets in general. Take \( x = \emptyset \) and \( y = \{\emptyset, \{\{\emptyset\}\}\} \). Then \( x \in y \), and nothing lies strictly between \( x \) and \( x \cup \{x\} = \{\emptyset\} \) (the only element of \( \{\emptyset\} \) is \( \emptyset \), and \( \emptyset \notin \emptyset \)). But \( \{\emptyset\} \notin y \), since \( \{\emptyset\} \ne \emptyset \) and \( \{\emptyset\} \ne \{\{\emptyset\}\} \); and \( \{\emptyset\} \ne y \), since \( \{\{\emptyset\}\} \in y \) is not an element of \( \{\emptyset\} \). So the step needs something about \( \omega \) beyond "nothing in between".

*Repair.* Replace (5) by the claim inside the proof of @thm-omega-order: for all \( m, n \in \omega \), \( m \in n \) implies \( \mathrm{S}(m) \in \mathrm{S}(n) \), proved by its own induction. Then \( n \in m \) gives \( \mathrm{S}(n) \in \mathrm{S}(m) = m \cup \{m\} \), so \( \mathrm{S}(n) \in m \) or \( \mathrm{S}(n) = m \). Lines (1)–(4), (6) and (7) are correct.

**Marking scheme.** (10 points)
- 2: says that the conclusion is true and that the proof is not correct.
- 3: names line (5) as the failing line and explains why its reason does not give \( \mathrm{S}(n) \le m \) (it needs trichotomy for \( \mathrm{S}(n) \) and \( m \), or the unproved fact \( n \in m \Rightarrow \mathrm{S}(n) \le m \)).
- 2: classifies the error as (N9): a line resting on an unavailable fact, either the goal itself (circular) or an unproved general fact.
- 2: gives a counterexample to the step on arbitrary sets (any \( x \in y \) with \( x \cup \{x\} \) neither in nor equal to \( y \)).
- 1: gives the repair through "\( m \in n \Rightarrow \mathrm{S}(m) \in \mathrm{S}(n) \)".
Fatal errors (0 for the step): declaring the conclusion false; blaming line (2) or (4), which are correct.
:::

<!-- dependency ledger
thm-omega-order (proof): S(n) subset of S(S(n)); m in n u {n} iff m in n or m = n | def-set-successor (cited), prp-zf-basic-sets (c)
thm-omega-order (proof): 1 notin 0 since 0 = emptyset has no elements | def-omega / exm-von-neumann-numerals (0 := emptyset)
thm-omega-well-ordering (proof): S(n) cap A = (n cap A) u ({n} cap A) | set algebra, Ch 6 Section 6.2 (distributive law, no label used); inline
thm-omega-well-ordering (proof): RAA on an existential goal | def-rule-raa (cited)
prp-omega-order-arithmetic (proof): substitution of equals inside sums and products | equality rules of Ch 4 (=E)
prp-omega-order-arithmetic (proof): n + 1 = S(n) | def-omega-arithmetic (the paragraph after it; cited)
prp-omega-powers-parity (claim): powers b^n on omega defined by recursion before the statement | thm-omega-recursion (cited)
prp-omega-powers-parity (proof): 1 + 1 = 2, 2 = S(1) | def-omega-arithmetic (the paragraph after it; cited)
prp-omega-powers-parity (proof): two pairs with different second coordinates differ | thm-kuratowski-pair (cited)
prp-tuples-as-sets (proof): 1 < 2 < 3 and 3 <= n for n >= 3 | thm-omega-order (a), (b) (cited)
prp-tuples-as-sets (proof): first coordinates of a set of pairs; a pair (k, y) has the element {k} | def-kuratowski-pair (cited)
exr-order-on-omega-a1 (solution): 0*0 = 0, 1*1 = 1, 2*2 = 4, 3*3 = 9, 4*4 = 16; numerals up to 16 | def-omega-arithmetic (computed from the equations; the Quick check of Section 05 for 2*2)
exr-order-on-omega-a1 (solution): 0, 1, 4, 9 < 10 and 16 > 10 | thm-omega-order (b), (c) (successive numerals)
exr-order-on-omega-c1 (solution): comparison with thm-strong-induction | Ch 3 (prose comparison only)
-->
