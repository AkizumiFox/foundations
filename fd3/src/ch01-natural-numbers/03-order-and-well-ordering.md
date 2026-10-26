# Order and Well-Ordering of the Natural Numbers

*Sets and Functions*, Chapter 3 ordered the natural numbers by the order of the real line, and proved from that order and induction that every non-empty set of natural numbers has a least element (@fd2:thm-well-ordering). The natural numbers of @ax-natural-numbers lie on no line. They do have addition, though, and addition already says when one number comes before another: \( m \) comes before \( n \) when we can count up from \( m \) to \( n \). This section takes that as the definition of the order, ties it to the arithmetic of the previous section, proves that it is a total order and a well-ordering, and records the facts about powers and parity that later sections cite.

## Counting up from m to n

The first idea is to copy *Sets and Functions*: \( m \le n \) when \( n - m \ge 0 \). On \( \nN \) this says nothing yet. There is no subtraction, and "\( \ge 0 \)" is the very order we are trying to define. What we do have is the sum. In school, \( 2 \le 5 \) because three more steps lead from \( 2 \) to \( 5 \); that statement uses only \( + \).

*\( m \le n \) when \( n \) is reached from \( m \) by adding a natural number.*

::: {#def-omega-order}
[Order on \( \nN \)]

For \( m, n \in \nN \), we write \( m \le n \) if \( n = m + j \) for some \( j \in \nN \), and \( m < n \) if \( m \le n \) and \( m \ne n \). As usual, \( n \ge m \) means \( m \le n \), and \( n > m \) means \( m < n \).
:::

Two examples. First, \( 2 \le 5 \), with \( j = 3 \): by the equations of @def-omega-arithmetic (a),
\[
2 + 3 = \mathrm{S}(2 + 2) = \mathrm{S}\bigl(\mathrm{S}(2 + 1)\bigr) = \mathrm{S}\bigl(\mathrm{S}(\mathrm{S}(2 + 0))\bigr) = \mathrm{S}\bigl(\mathrm{S}(3)\bigr) = 5 .
\]
Second, \( 0 \le n \) for every \( n \in \nN \), since \( n = 0 + n \) by @thm-omega-arithmetic-laws (a).

The definition is short, and so it promises little. Nothing in it says that \( 5 \le 2 \) fails, or that \( \le \) behaves like an order at all. Antisymmetry will need the fact that a sum is \( 0 \) only when both terms are, and totality, that any two numbers are comparable, will need an induction. We first collect what the definition says about sums and products, since those facts are the tools for everything else.

## Order and arithmetic

Cancellation in sums, \( m + k = n + k \Rightarrow m = n \), needs no order at all, and it is what makes the \( j \) of the definition unique. With it, the order clauses (c) and (e) follow one pattern: translate \( m < n \) into an equation \( n = m + j \) with \( j \ne 0 \), compute with the laws of @thm-omega-arithmetic-laws, and translate back; the rest are inductions or successor arguments.

::: {#prp-omega-order-arithmetic}
[Order and Arithmetic on \( \nN \)]

For all \( k, m, n, b \in \nN \):

::: {.enumerate options="label=(\alph*)"}
1. \( m \le n \) if and only if \( n = m + j \) for some \( j \in \nN \); this \( j \) is then unique, and is written \( n - m \). Moreover \( m < n \) if and only if \( n = m + j \) for some \( j \ne 0 \).
2. If \( m + k = n + k \), then \( m = n \).
3. If \( m < n \), then \( m + k < n + k \).
4. If \( mn = 0 \), then \( m = 0 \) or \( n = 0 \).
5. If \( m < n \) and \( k \ne 0 \), then \( mk < nk \).
6. If \( mk = nk \) and \( k \ne 0 \), then \( m = n \).
7. *(Induction from \( b \).)* Let \( P(n) \) be a property of natural numbers. If \( P(b) \) holds and, for every \( n \in \nN \) with \( n \ge b \), \( P(n) \) implies \( P(n + 1) \), then \( P(n) \) holds for every \( n \in \nN \) with \( n \ge b \).
:::
:::

::: {.idea}
Cancellation (b) needs no order: induct on \( k \) and peel off one successor at a time with @cor-omega-successor-cancellation. The equivalence in (a) is the definition, and uniqueness is (b). Then (c) and (e) translate an inequality \( m < n \) into an equation \( n = m + j \) with \( j \ne 0 \), compute, and translate back; (d) writes \( m \) and \( n \) as successors and uses that a successor is never \( 0 \). Clause (f) is proved by induction on \( m \), the first factor, using law (e) to open \( (m + 1)k \) (step (4) of @exm-method-induct-on-recursion-variable). Finally (g) shifts the start of an induction from \( 0 \) to \( b \).
:::

::: {.proof}
All inductions are by @thm-omega-induction (b), and "Law (x)" refers to clause (x) of @thm-omega-arithmetic-laws. We prove (b) first, since (a) uses it.

(b) Induct on \( k \) for "for all \( m, n \): \( m + k = n + k \Rightarrow m = n \)". For \( k = 0 \), \( m + 0 = m \) and \( n + 0 = n \). If the statement holds for \( k \) and \( m + (k + 1) = n + (k + 1) \), then \( (m + k) + 1 = (n + k) + 1 \) by @def-omega-arithmetic (a), so \( m + k = n + k \) by @cor-omega-successor-cancellation, and \( m = n \) by the hypothesis.

(a) The equivalence is @def-omega-order.

*Uniqueness.* If \( m + j = m + j' \), then \( j + m = j' + m \) by Law (b), so \( j = j' \) by (b) of this proposition.

*The strict case.* If \( n = m + j \), then \( j = 0 \) if and only if \( n = m \): if \( j = 0 \), then \( n = m + 0 = m \); if \( n = m \), then \( m + j = m = m + 0 \), so \( j = 0 \) by uniqueness. Since \( m < n \) holds exactly when \( m \le n \) and \( m \ne n \) (by @def-omega-order), \( m < n \) holds if and only if \( n = m + j \) with \( j \ne 0 \).

(c) Let \( m < n \), so \( n = m + j \) with \( j \ne 0 \) by (a). Then
\[
n + k = (m + j) + k = m + (k + j) = (m + k) + j
\]
by Laws (c), (b) and (c). Since \( j \ne 0 \), (a) gives \( m + k < n + k \).

(d) Let \( mn = 0 \) and \( n \ne 0 \); we show \( m = 0 \). By @prp-peano-predecessor (a), \( n = \mathrm{S}(j) = j + 1 \) for some \( j \in \nN \), so \( 0 = mn = mj + m \) by @def-omega-arithmetic (b). If \( m \ne 0 \), then likewise \( m = i + 1 \) for some \( i \in \nN \), and
\[
0 = mj + (i + 1) = (mj + i) + 1 ,
\]
by @def-omega-arithmetic (a), which contradicts @cor-omega-successor-cancellation. So \( m = 0 \).

(e) Let \( m < n \) and \( k \ne 0 \). By (a), \( n = m + j \) with \( j \ne 0 \), so \( nk = (m + j)k = mk + jk \) by Law (d). By (d), \( jk \ne 0 \), since \( j \ne 0 \) and \( k \ne 0 \). By (a), \( mk < nk \).

(f) Fix \( k \ne 0 \), and induct on \( m \) for "for every \( n \in \nN \), \( mk = nk \Rightarrow m = n \)". For \( m = 0 \): if \( 0 \cdot k = nk \), then \( nk = 0 \) by Law (e), so \( n = 0 \) by (d), since \( k \ne 0 \). Suppose the statement holds for \( m \), and let \( (m + 1)k = nk \). By @prp-peano-predecessor (a), \( k = i + 1 \) for some \( i \in \nN \), so
\[
(m + 1)k = mk + k = mk + (i + 1) = (mk + i) + 1 \ne 0
\]
by Law (e), @def-omega-arithmetic (a) and @cor-omega-successor-cancellation. So \( nk \ne 0 \), hence \( n \ne 0 \) (as \( 0 \cdot k = 0 \)), and \( n = n' + 1 \) for some \( n' \in \nN \) (@prp-peano-predecessor (a)). Then \( mk + k = (m + 1)k = nk = n'k + k \) by Law (e), so \( mk = n'k \) by (b), and \( m = n' \) by the hypothesis. Hence \( m + 1 = n \).

(g) Let \( Q(i) \) be "\( P(b + i) \)", for \( i \in \nN \). \( Q(0) \) is \( P(b + 0) = P(b) \). If \( Q(i) \) holds, then \( b + i \ge b \) by (a), so the hypothesis gives \( P((b + i) + 1) \); and \( (b + i) + 1 = b + (i + 1) \) by @def-omega-arithmetic (a), so \( Q(i + 1) \) holds. By @thm-omega-induction (b), \( Q(i) \) holds for every \( i \in \nN \). Finally, if \( n \ge b \), then \( n = b + i \) for some \( i \) by (a), and \( P(n) \) is \( Q(i) \).
:::

Clause (a) is how subtraction appears on \( \nN \): \( n - m \) is defined only when \( m \le n \), as the unique \( j \) with \( m + j = n \). For example \( 5 - 2 = 3 \), by the example after @def-omega-order, and \( n - 0 = n \). Clause (g) is the "induction from a base" that *Sets and Functions*, Chapter 3 used as @fd2:thm-induction, now proved on \( \nN \).

::: {.check}
Show that \( 3 \le 5 \), naming the \( j \). Is \( n \le n + 1 \)? Is \( n + 1 \le n \)?
:::

::: {.solution}
\( 3 + 2 = \mathrm{S}(3 + 1) = \mathrm{S}\bigl(\mathrm{S}(3 + 0)\bigr) = \mathrm{S}\bigl(\mathrm{S}(3)\bigr) = 5 \), so \( 3 \le 5 \) with \( j = 2 \), and \( 5 - 3 = 2 \). Yes, \( n \le n + 1 \), with \( j = 1 \). No: if \( n = (n + 1) + j \), then \( n + 0 = n + (j + 1) \) by @thm-omega-arithmetic-laws (c) and (b), so \( j + 1 = 0 \) by the uniqueness in (a), against @cor-omega-successor-cancellation.
:::

## A total order

The definition of \( \le \) came from arithmetic, so its properties as an order must come from arithmetic too. The next theorem proves them, and then describes the sets \( \{0, \dots, n\} \) and \( \{1, \dots, n\} \) that *Sets and Functions* used everywhere, now as subsets of \( \nN \).

::: {#thm-omega-order}
[Order on \( \nN \)]

::: {.enumerate options="label=(\alph*)"}
1. \( < \) is a strict total order on \( \nN \): for all \( k, m, n \in \nN \), never \( n < n \); if \( k < m \) and \( m < n \), then \( k < n \); and **exactly one** of \( m < n \), \( m = n \), \( n < m \) holds.
2. For \( m, n \in \nN \), \( m < \mathrm{S}(n) \) if and only if \( m \le n \). Hence no \( k \in \nN \) satisfies \( n < k < \mathrm{S}(n) \).
3. For \( n \in \nN \), the set \( \{0, \dots, n\} \coloneqq \{ k \in \nN : k \le n \} \) satisfies \( \{0, \dots, 0\} = \{0\} \) and \( \{0, \dots, \mathrm{S}(n)\} = \{0, \dots, n\} \cup \{\mathrm{S}(n)\} \), with \( \mathrm{S}(n) \notin \{0, \dots, n\} \).
4. \( 0 \le n \) for every \( n \in \nN \); if \( n \ne 0 \), then \( 1 \le n \); and \( 0 < 1 \).
5. For \( n \in \nN \), the set \( \{1, \dots, n\} \coloneqq \{ k \in \nN : 1 \le k \le n \} \) satisfies \( \{1, \dots, 0\} = \emptyset \) and \( \{1, \dots, \mathrm{S}(n)\} = \{1, \dots, n\} \cup \{\mathrm{S}(n)\} \).
:::
:::

::: {.idea}
First \( \le \) is a partial order: reflexive (\( j = 0 \)), transitive (associativity), antisymmetric (cancel, then use that a sum is \( 0 \) only when both terms are). Then it is total, by induction on \( n \) with "for every \( m \)" kept inside the property. The three properties of \( < \) in (a) follow from these four facts, and the rest unwinds (b).
:::

::: {.proof}
"Law (x)" refers to @thm-omega-arithmetic-laws, and "Order (x)" to @prp-omega-order-arithmetic.

*Zero sums.* If \( j + i = 0 \), then \( i = 0 \) and \( j = 0 \). Indeed, if \( i \ne 0 \), then \( i = i' + 1 \) for some \( i' \) (@prp-peano-predecessor (a)), and \( j + i = (j + i') + 1 \ne 0 \) by @def-omega-arithmetic (a) and @cor-omega-successor-cancellation. So \( i = 0 \), and \( j = j + 0 = 0 \).

*\( \le \) is a partial order* (@fd2:def-partial-order). (PO1) \( n = n + 0 \), so \( n \le n \). (PO3) If \( m = k + i \) and \( n = m + j \), then \( n = k + (i + j) \) by Law (c), so \( k \le n \). (PO2) If \( n = m + j \) and \( m = n + i \), then \( m + 0 = m = m + (j + i) \) by Law (c), so \( j + i = 0 \) by the uniqueness in Order (a). By zero sums \( i = 0 \), and \( m = n + 0 = n \).

*\( \le \) is total.* We induct on \( n \) for "for every \( m \in \nN \), \( m \le n \) or \( n \le m \)". For \( n = 0 \): \( 0 \le m \), since \( m = 0 + m \) by Law (a). Suppose the property holds for \( n \), and let \( m \in \nN \). If \( m \le n \), say \( n = m + j \), then \( n + 1 = m + (j + 1) \) by @def-omega-arithmetic (a), so \( m \le n + 1 \). If \( n \le m \), say \( m = n + j \), there are two cases. If \( j = 0 \), then \( m = n \), and \( n + 1 = m + 1 \) gives \( m \le n + 1 \). Otherwise \( j \ne 0 \), so \( j = j' + 1 \) for some \( j' \in \nN \) (@prp-peano-predecessor (a)), and
\[
m = n + (j' + 1) = (n + j') + 1 = (n + 1) + j'
\]
by @def-omega-arithmetic (a) and Law (a), so \( n + 1 \le m \).

(a) *Irreflexive:* \( n < n \) would need \( n \ne n \). *Transitive:* let \( k < m \) and \( m < n \). Then \( k \le n \) by (PO3). If \( k = n \), then \( k \le m \) and \( m \le k \), so \( k = m \) by (PO2), against \( k < m \). So \( k < n \). *Trichotomy:* at least one of the three holds, since by totality \( m \le n \) or \( n \le m \), and each of these is "\( < \) or \( = \)". At most one: \( m < n \) excludes \( m = n \) by definition, and \( m < n \) together with \( n < m \) would give \( m = n \) by (PO2).

(b) \( (\Leftarrow) \) If \( n = m + j \), then \( \mathrm{S}(n) = n + 1 = m + (j + 1) \), and \( j + 1 \ne 0 \), so \( m < \mathrm{S}(n) \) by Order (a). \( (\Rightarrow) \) If \( m < \mathrm{S}(n) \), then by Order (a) and @prp-peano-predecessor (a), \( \mathrm{S}(n) = m + (i + 1) = \mathrm{S}(m + i) \) for some \( i \), so \( n = m + i \) by (P4), and \( m \le n \). Finally, if \( n < k < \mathrm{S}(n) \), then \( k \le n \), so \( k < n \) or \( k = n \), and either contradicts \( n < k \) by trichotomy.

(c) If \( k \le 0 \), then \( 0 = k + j \) for some \( j \), and \( k = 0 \) by zero sums; and \( 0 \le 0 \). So \( \{0, \dots, 0\} = \{0\} \). By (b), \( k \le \mathrm{S}(n) \), that is, \( k < \mathrm{S}(n) \) or \( k = \mathrm{S}(n) \), holds if and only if \( k \le n \) or \( k = \mathrm{S}(n) \); this is the union. Since \( n \le n \), (b) gives \( n < \mathrm{S}(n) \), so \( \mathrm{S}(n) \le n \) fails by trichotomy.

(d) \( 0 \le n \), since \( n = 0 + n \) by Law (a). If \( n \ne 0 \), then \( n = k + 1 \) for some \( k \) (@prp-peano-predecessor (a)), and \( k + 1 = 1 + k \) by Law (b), so \( 1 \le n \). Finally \( 1 = 0 + 1 \) and \( 1 \ne 0 \) (@cor-omega-successor-cancellation), so \( 0 < 1 \) by Order (a).

(e) For \( k \in \nN \), \( 1 \le k \) holds if and only if \( k \ne 0 \): by (d) if \( k \ne 0 \), and \( 1 \le 0 \) fails by (c), since \( 1 \ne 0 \). So \( \{1, \dots, n\} = \{0, \dots, n\} \setminus \{0\} \), and (c) gives \( \{1, \dots, 0\} = \emptyset \) and \( \{1, \dots, \mathrm{S}(n)\} = \{1, \dots, n\} \cup \{\mathrm{S}(n)\} \), as \( \mathrm{S}(n) \ne 0 \) by (P3). This proves the theorem.
:::

So the notation \( \{0, \dots, n\} \) and \( \{1, \dots, n\} \) of *Sets and Functions*, Chapter 3 keeps its meaning on \( \nN \): by (c) and (e) each set grows by exactly one new element at each step, and \( \{1, \dots, 0\} = \emptyset \). In the "plus one" notation of @def-omega-arithmetic, (b) says that \( n + 1 \) is the next number after \( n \).

::: {.check}
Is there a \( k \in \nN \) with \( 4 < k < 5 \)? List \( \{0, \dots, 3\} \) using (c).
:::

::: {.solution}
No: \( 5 = \mathrm{S}(4) \), and (b) says that nothing lies strictly between \( 4 \) and \( \mathrm{S}(4) \). By (c), three times, \( \{0, \dots, 3\} = \{0\} \cup \{1\} \cup \{2\} \cup \{3\} = \{0, 1, 2, 3\} \).
:::

::: {.warning}
**Cancelling a factor needs it to be non-zero.** \( 5 \cdot 0 = 2 \cdot 0 \), yet \( 5 \ne 2 \): clause (f) of @prp-omega-order-arithmetic carries \( k \ne 0 \) for this reason. Clause (e) carries it too, since \( 2 < 5 \) while \( 2 \cdot 0 < 5 \cdot 0 \) fails.
:::

## Well-ordering

In *Sets and Functions*, Chapter 3, @fd2:thm-well-ordering was derived from @fd1:ax-induction, which there was an axiom, by way of strong induction. On \( \nN \), induction is a theorem (@thm-omega-induction), so well-ordering becomes one too. Here a direct induction does it, on the sets \( \{0, \dots, n\} \) of @thm-omega-order (c).

::: {#thm-omega-well-ordering}
[Well-Ordering of \( \nN \)]

Every **non-empty** subset \( A \subseteq \nN \) has a least element: an \( a \in A \) with \( a \le x \) for every \( x \in A \). The least element is unique.
:::

::: {.idea}
Suppose \( A \) has no least element. Walk up through \( 0, 1, 2, \dots \): the first element of \( A \) met on the way would be least. So no element of \( \{0, \dots, n\} \) lies in \( A \), and this is proved by induction on \( n \). Since every \( a \) lies in \( \{0, \dots, a\} \), \( A \) is empty. Compare @fd2:exm-method-least-element, which *uses* a least element; here we produce one.
:::

::: {.proof}
Let \( A \subseteq \nN \) be non-empty, and suppose, for a contradiction, that \( A \) has no least element. We use @thm-omega-induction (b) on \( n \), for the property \( B(n) \): "\( \{0, \dots, n\} \cap A = \emptyset \)".

*Base case.* By @thm-omega-order (c), \( \{0, \dots, 0\} \cap A = \{0\} \cap A \). If \( 0 \in A \), then \( 0 \le x \) for every \( x \in A \) by @thm-omega-order (d), so \( 0 \) is a least element of \( A \), contrary to our supposition. So \( B(0) \) holds.

*Inductive step.* Suppose \( B(n) \). By @thm-omega-order (c),
\[
\{0, \dots, \mathrm{S}(n)\} \cap A = \bigl(\{0, \dots, n\} \cap A\bigr) \cup \bigl(\{\mathrm{S}(n)\} \cap A\bigr) = \{\mathrm{S}(n)\} \cap A .
\]
Suppose \( \mathrm{S}(n) \in A \), and let \( x \in A \). By \( B(n) \), \( x \le n \) fails, so \( x < \mathrm{S}(n) \) fails by @thm-omega-order (b), and \( \mathrm{S}(n) \le x \) by trichotomy (@thm-omega-order (a)). Hence \( \mathrm{S}(n) \) is a least element of \( A \), contrary to our supposition. So \( \mathrm{S}(n) \notin A \), and \( B(\mathrm{S}(n)) \) holds.

By induction, \( B(n) \) holds for every \( n \in \nN \). Since \( A \) is non-empty, there is some \( a \in A \). Then \( a \le a \), so \( a \in \{0, \dots, a\} \cap A \), against \( B(a) \). This contradiction shows, by RAA (@fd1:def-rule-raa), that \( A \) has a least element.

*Uniqueness.* If \( a \) and \( a' \) are least elements, then \( a \le a' \) and \( a' \le a \). If \( a \ne a' \), these give \( a < a' \) and \( a' < a \), so \( a < a \) by transitivity, contradicting irreflexivity (@thm-omega-order (a)). So \( a = a' \).
:::

The proof concludes an existence statement from a contradiction, so its last step is RAA, not \( \rulename{\neg I} \): what is refuted is "\( A \) has no least element". The statement is that of @fd2:thm-well-ordering, read on \( \nN \); there the proof went through strong induction on \( \nN \subseteq \nR \), here through the property \( B(n) \).

Both hypotheses are needed. The empty set is a subset of \( \nN \) with no least element, since a least element must be an element of the set. For sets of numbers that are not subsets of \( \nN \), the warning after @fd2:thm-well-ordering gives \( \nZ \) and the positive rationals.

::: {.check}
What is the least element of \( \{ n \in \nN : n \cdot n > 10 \} \), and why?
:::

::: {.solution}
It is \( 4 \). First, \( 3 \cdot 3 = 9 \), \( 4 \cdot 4 = 16 \), and \( 9 < 10 < 16 \), since \( 10 = 9 + 1 \) and \( 16 = 10 + 6 \). So \( 4 \) lies in the set. Any \( x < 4 \) lies in \( \{0, \dots, 3\} = \{0, 1, 2, 3\} \) (@thm-omega-order (b), (c)), where \( x \cdot x \) is \( 0 \), \( 1 \), \( 4 \) or \( 9 \), so \( x \cdot x \le 9 < 10 \) and \( x \) is not in the set. By trichotomy every element \( x \) of the set has \( 4 \le x \).
:::

## Powers and parity

*Sets and Functions*, Chapter 4 counted with powers \( 2^m 3^n \) and with even and odd numbers, and took both from the real numbers and the integers. Here are the facts it used, proved on \( \nN \). Section 1.4 cites them in its rule for reading *Sets and Functions* on \( \nN \), and Chapter 4 of this volume uses them again.

For \( b \in \nN \), the powers \( b^n \) (\( n \in \nN \)) are defined by @thm-omega-recursion with \( X = \nN \), \( a = 1 \) and \( g(n, x) = x \cdot b \):
\[
b^0 \coloneqq 1, \qquad b^{n+1} \coloneqq b^n \cdot b .
\]
These are the two equations of @fd2:def-power, now on \( \nN \); so \( b^1 = 1 \cdot b = b \) by @thm-omega-arithmetic-laws (e).

::: {.check}
Compute \( 2^3 \) from the two equations.
:::

::: {.solution}
\( 2^0 = 1 \), \( 2^1 = 1 \cdot 2 = 2 \), \( 2^2 = 2 \cdot 2 = 4 \), \( 2^3 = 4 \cdot 2 = 8 \).
:::

::: {#prp-omega-powers-parity}
[Powers and Parity on \( \nN \)]

For all \( b, m, n \in \nN \):

::: {.enumerate options="label=(\alph*)"}
1. \( b^{m+n} = b^m \cdot b^n \);
2. if \( b \ne 0 \), then \( b^n \ne 0 \);
3. if \( b > 1 \) and \( m < n \), then \( b^m < b^n \);
4. there is exactly one pair \( (q, r) \) with \( q \in \nN \), \( r \in \{0, 1\} \) and \( n = 2q + r \). In particular, no \( n \in \nN \) is both of the form \( 2q \) and of the form \( 2q' + 1 \).
:::
:::

::: {.idea}
(a) and (b) are inductions on \( n \) following the definition of \( b^n \), by the recursion-variable method of @exm-method-induct-on-recursion-variable. For (c), first \( b^j > 1 \) for \( j \ge 1 \), by induction from \( 1 \); then write \( n = m + j \) and use (a). For (d), existence is an induction (a number is even or odd, and adding one swaps the two), and uniqueness reduces, after canceling, to "\( r = 2j + r' \) with \( j \ge 1 \)", which makes \( r \ge 2 \).
:::

::: {.second-reading title="Proof of the proposition"}
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
by Law (c) and \( 1 + 1 = 2 \) (@def-omega-arithmetic (c)), Law (e), and Law (d).

*Uniqueness.* Let \( 2q + r = 2q' + r' \) with \( r, r' \in \{0, 1\} \). Suppose first that \( q < q' \). By Order (a), \( q' = q + j \) with \( j \ne 0 \), so
\[
2q + r = 2(q + j) + r' = 2q + (2j + r')
\]
by Laws (d) and (c), and canceling \( 2q \) (Order (b), after Law (b)) gives \( r = 2j + r' \). Since \( j \ge 1 \) (@thm-omega-order (d)), Order (a) gives \( j = 1 + i \) for some \( i \in \nN \), and \( 2j + r' = (2 + 2i) + r' = 2 + (2i + r') \) by Laws (d), (e) and (c). So \( r = 2 + (2i + r') \ge 2 \) by Order (a). But \( r = 0 \) or \( r = 1 \), and both are \( < 2 = \mathrm{S}(1) \) by @thm-omega-order (b); this contradicts trichotomy. So \( q < q' \) is impossible, and \( q' < q \) is impossible by the same argument with the roles exchanged. By trichotomy \( q = q' \), and then \( r = r' \) by Order (b) (after Law (b)). The pairs \( (q, r) \) and \( (q', r') \) are therefore equal (@fd2:def-ordered-pair).

If \( n = 2q = 2q + 0 \) and \( n = 2q' + 1 \), the pairs \( (q, 0) \) and \( (q', 1) \) would both represent \( n \), and they differ since \( 0 \ne 1 \); so no \( n \) is of both forms.
:::
:::

Any other definition of powers on \( \nN \) by the same two equations, \( c(0) = 1 \) and \( c(n + 1) = c(n) \cdot b \), gives these powers, by the uniqueness half of @thm-omega-recursion. Section 1.4 and Chapter 4 of this volume use the proposition.

## Exercises

### A. Check your understanding

::: {#exr-order-on-omega-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. True or false: for \( m, n \in \nN \), \( m < n \) implies \( m + 1 \le n \). Justify your answer.
2. Is \( 5 \le 2 \)? Justify your answer.
3. Which clause of @thm-omega-order says that \( \{0, \dots, n\} \) grows by one element at each step? List \( \{0, \dots, 2\} \) and \( \{1, \dots, 2\} \).
4. Which clause of @prp-omega-order-arithmetic defines \( n - m \)? Compute \( 5 - 2 \).
:::
:::

::: {.solution}
(a) True. By @prp-omega-order-arithmetic (a), \( n = m + j \) with \( j \ne 0 \). By @thm-omega-order (d), \( 1 \le j \), so \( j = 1 + i \) for some \( i \in \nN \), by @prp-omega-order-arithmetic (a) again. Then \( n = m + (1 + i) = (m + 1) + i \) by @thm-omega-arithmetic-laws (c), so \( m + 1 \le n \).

(b) No. \( 5 = 2 + 3 \) with \( 3 \ne 0 \) (the example after @def-omega-order), so \( 2 < 5 \) by @prp-omega-order-arithmetic (a). By trichotomy (@thm-omega-order (a)), neither \( 5 < 2 \) nor \( 5 = 2 \), so \( 5 \le 2 \) fails.

(c) Clause (c). \( \{0, \dots, 2\} = \{0, 1, 2\} \), and \( \{1, \dots, 2\} = \{1, 2\} \) by clause (e).

(d) Clause (a): \( n - m \) is the unique \( j \) with \( n = m + j \). Since \( 5 = 2 + 3 \), \( 5 - 2 = 3 \).
:::

### B. Practice

::: {#exr-order-on-omega-b1}
[B1: Order as inclusion]

Prove that for all \( m, n \in \nN \), \( m \le n \) if and only if \( \{0, \dots, m\} \subseteq \{0, \dots, n\} \), and that \( m < n \) if and only if this inclusion is proper.
:::

::: {.solution}
\( (\Rightarrow) \) Let \( m \le n \), say \( n = m + j \), and let \( k \in \{0, \dots, m\} \), say \( m = k + i \). Then \( n = k + (i + j) \) by @thm-omega-arithmetic-laws (c), so \( k \le n \) and \( k \in \{0, \dots, n\} \).

\( (\Leftarrow) \) Since \( m = m + 0 \), \( m \in \{0, \dots, m\} \subseteq \{0, \dots, n\} \), so \( m \le n \).

*The strict case.* Let \( m < n \). The inclusion holds by the first part, and \( n \in \{0, \dots, n\} \) while \( n \notin \{0, \dots, m\} \), because \( n \le m \) would contradict \( m < n \) by trichotomy (@thm-omega-order (a)). So the inclusion is proper. Conversely, if the inclusion is proper, then \( m \le n \) by the first part, and \( m \ne n \), since \( m = n \) would make the two sets equal. So \( m < n \).
:::

::: {#exr-order-on-omega-b2}
[B2: A product is at least its factor]

Prove that for all \( m, n \in \nN \) with \( n \ge 1 \), \( m \le mn \). Show by an example that the hypothesis \( n \ge 1 \) is needed.
:::

::: {.solution}
Since \( 1 \le n \), @prp-omega-order-arithmetic (a) gives \( n = 1 + j \) for some \( j \in \nN \). Then
\[
mn = m(1 + j) = m \cdot 1 + mj = m + mj ,
\]
by @thm-omega-arithmetic-laws (d) and (e). By @prp-omega-order-arithmetic (a) again, \( m \le m + mj = mn \).

The hypothesis is needed: for \( m = 1 \) and \( n = 0 \), \( mn = 0 \), and \( 1 \le 0 \) is false, since \( 0 < 1 \) (@thm-omega-order (d)) and trichotomy.
:::

### C. Going deeper

::: {#exr-order-on-omega-c1}
[C1: Strong induction on ℕ]

Let \( P(n) \) be a property of natural numbers. Suppose that, for every \( n \in \nN \), if \( P(k) \) holds for every \( k \in \nN \) with \( k < n \), then \( P(n) \) holds. Prove that \( P(n) \) holds for every \( n \in \nN \).
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
Let \( A \coloneqq \{ n \in \nN : P(n) \text{ fails} \} \), a set by @fd2:def-set-builder, and suppose, for a contradiction, that \( A \ne \emptyset \). By @thm-omega-well-ordering, \( A \) has a least element \( a \). Let \( k \in \nN \) with \( k < a \). If \( k \in A \), then \( a \le k \), and with \( k < a \) this gives \( k < k \) (by transitivity, or directly if \( a = k \)), contradicting irreflexivity (@thm-omega-order (a)). So \( k \notin A \), that is, \( P(k) \) holds. This holds for every \( k < a \), so the hypothesis gives \( P(a) \), contradicting \( a \in A \). Hence \( A = \emptyset \), and \( P(n) \) holds for every \( n \in \nN \).

This is the statement of @fd1:thm-strong-induction, read on \( \nN \). There it was derived from @fd1:ax-induction directly; here the route goes through well-ordering, which was itself proved from @thm-omega-induction. The proof is the move of @fd2:exm-method-smallest-counterexample: a least failure, below which everything holds. As in *Logic and Proof*, the hypothesis at \( n = 0 \) is vacuous (no \( k < 0 \), since \( k \le 0 \) forces \( k = 0 \) by @thm-omega-order (c)), so it hands us \( P(0) \) outright.

**Marking scheme.** (10 points)
- 2: considers the set of failures (or argues by contradiction from a failure) and makes it a set.
- 3: applies @thm-omega-well-ordering, with the set non-empty, to obtain a least failure \( a \).
- 3: shows \( P(k) \) for every \( k < a \), using that \( a \) is least and the order facts.
- 2: applies the hypothesis at \( a \) and reaches the contradiction.
Fatal errors (0 for the step): citing @fd1:thm-strong-induction (a statement about the natural numbers of *Logic and Proof*, Chapter 4, not proved from @ax-natural-numbers) instead of proving the result; taking a least element of a set not shown to be non-empty. A route by @thm-omega-induction (b) on "\( P(k) \) for every \( k < n \)" earns the same points: 2 for the property \( Q(n) \): \"\( P(k) \) for every \( k < n \)\"; 2 for the vacuous base (no \( k < 0 \), by @thm-omega-order (c)); 4 for the step (\( P(n) \) from the hypothesis, then \( k < n + 1 \) gives \( k \le n \) by @thm-omega-order (b), so \( k < n \) or \( k = n \)); 2 for deducing \( P(n) \) from \( Q(n + 1) \).
:::

::: {#exr-order-on-omega-c2}
[C2: Find the error]

Here is an attempted proof that any two natural numbers are comparable. The proof is meant to replace the totality step in the proof of @thm-omega-order, so it may cite only results stated before that theorem. Is the conclusion true? Is the proof correct? If not, give the first line that fails, the error, and a counterexample to the step.

> **Claim.** For all \( m, n \in \nN \): \( m \le n \) or \( n \le m \).
>
> (1) Fix \( m \); we use @thm-omega-induction (b) on \( n \), for the property "\( m \le n \) or \( n \le m \)". (2) For \( n = 0 \): \( 0 \le m \), since \( m = 0 + m \). (3) Suppose that \( m \le n \) or \( n \le m \). (4) If \( n = m + j \), then \( n + 1 = m + (j + 1) \), so \( m \le n + 1 \). (5) If \( n \le m \), then \( n + 1 \le m \), because \( n < n + 1 \) and nothing lies strictly between \( n \) and \( n + 1 \). (6) So \( m \le n + 1 \) or \( n + 1 \le m \). (7) By induction, the claim holds.
:::

::: {.solution}
The conclusion is **true**: it is the totality proved inside @thm-omega-order, and it follows from trichotomy, @thm-omega-order (a). The proof is **not** correct.

*The failing line is (5)*, and it fails for two independent reasons.

First, \( n \le m \) includes the case \( n = m \), where the conclusion \( n + 1 \le n \) is false (the Quick check after @prp-omega-order-arithmetic). This is a missing case, entry (N7) of @fd1:exm-not-allowed-catalogue. *Counterexample to the step:* \( m = n = 0 \). The hypothesis of line (3) holds, since \( 0 \le 0 \), and so does \( n \le m \); but \( n + 1 = 1 \le 0 \) is false, since \( 0 < 1 \) (@thm-omega-order (d)).

Second, even when \( n < m \), the stated reason does not give \( n + 1 \le m \) without comparing \( m \) with \( n + 1 \): "nothing lies strictly between \( n \) and \( n + 1 \)" excludes \( n < m < n + 1 \), and one still needs that \( m < n + 1 \), \( m = n + 1 \) or \( n + 1 < m \). That is trichotomy, and @thm-omega-order (b), which the reason quotes, was itself proved from trichotomy, that is, from the claim being proved. So the line rests on a fact not available at that point of the proof of @thm-omega-order: entry (N9).

*Repair.* Replace (5) by two cases. If \( n = m \), then \( m \le n + 1 \), since \( n + 1 = m + 1 \). If \( n < m \), then \( m = n + j \) with \( j \ne 0 \) (@prp-omega-order-arithmetic (a)), so \( j = j' + 1 \) for some \( j' \), and \( m = (n + 1) + j' \) by @def-omega-arithmetic (a) and @thm-omega-arithmetic-laws (a); this uses no comparison. Lines (1)–(4), (6) and (7) are correct; fixing \( m \) is harmless, since the step never needs the property for another \( m \).

**Marking scheme.** (10 points)
- 2: says that the conclusion is true and that the proof is not correct.
- 3: names line (5) as the failing line, with either defect: the case \( n = m \), or the hidden comparison of \( m \) with \( n + 1 \).
- 2: classifies the error as (N7), a missing case, or as (N9), a line resting on an unavailable fact (the claim itself).
- 2: gives a counterexample to the step, such as \( m = n = 0 \) (a case with \( n = m \); the (N9) defect alone has none, since the conclusion of (5) is true when \( n < m \)).
- 1: gives a repair through \( m = n + j \) with \( j \ne 0 \).
Fatal errors (0 for the step): declaring the conclusion false; blaming line (1).
:::

<!-- dependency ledger
def-omega-order (example): 2 + 3 = 5 by unfolding m + S(n) = S(m + n) three times; 3 = S(2), 4 = S(3), 5 = S(4) | def-omega-arithmetic (a), (c) (cited)
prp-omega-order-arithmetic (proof): substitution of equals inside sums and products | equality rules of F1.4 (=E)
prp-omega-order-arithmetic (proof): n + 1 = S(n) | def-omega-arithmetic (c) (cited)
prp-omega-order-arithmetic (proof): (f) 0 * k = 0 | thm-omega-arithmetic-laws (e) (cited as Law (e))
thm-omega-order (proof): S(n) = n + 1, used to write predecessors as k + 1 | def-omega-arithmetic (c) (cited)
thm-omega-order (proof): (b) S(m + i) = m + (i + 1); (P4) for N | def-omega-arithmetic (a); ax-natural-numbers with def-peano-system (P4), named "(P4)" in text
thm-omega-order (proof): (e) S(n) != 0 | ax-natural-numbers with def-peano-system (P3), named "(P3)" in text
thm-omega-well-ordering (proof): {0..S(n)} cap A = ({0..n} cap A) u ({S(n)} cap A) | set algebra, F2.1 (distributive law, no label used); inline
thm-omega-well-ordering (proof): RAA on an existential goal | def-rule-raa (cited)
thm-omega-well-ordering (solution): Quick check: 3*3 = 9, 4*4 = 16, 10 = 9 + 1, 16 = 10 + 6; 0*0, 1*1, 2*2 in {0, 1, 4} | def-omega-arithmetic (computed from the equations)
prp-omega-powers-parity (claim): powers b^n on N defined by recursion before the statement | thm-omega-recursion (cited)
prp-omega-powers-parity (solution): Quick check: 2^3 = 8; 2*2 = 4, 4*2 = 8 | def-omega-arithmetic (computed from the equations)
prp-omega-powers-parity (proof): 1 + 1 = 2, 2 = S(1) | def-omega-arithmetic (c) (cited)
prp-omega-powers-parity (proof): two pairs with different second coordinates differ | fd2:def-ordered-pair (cited)
exr-order-on-omega-a1 (solution): {0..2} = {0, 1, 2} by unfolding thm-omega-order (c) twice | thm-omega-order (c), (e) (cited)
exr-order-on-omega-c1 (solution): comparison with thm-strong-induction | F1.3 (prose comparison only)
exr-order-on-omega-c2 (solution): totality is proved inside thm-omega-order's proof, not stated as a clause | thm-omega-order (a) (trichotomy implies it; cited)
-->
