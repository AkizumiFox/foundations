# Countable Sets

Section 8.1 made "the same size" exact and settled the finite sets. It also showed that \( \nN \) is infinite, because it is equinumerous with its proper subset \( 2\nN \) (@exm-hilbert-hotel). The next question is which sets can be put into a list indexed by \( \nN \). Chapter 11 already uses the word for these sets, **countable**, in its proof that the real numbers cannot be listed. This section defines it, proves three equivalent forms of it, shows that countable sets are closed under subsets, images, unions of two sets and finite products, and lists the integers and the rationals.

## Lists

Can we list the rational numbers as \( q_0, q_1, q_2, \dots \) so that every rational number appears somewhere? Density makes it look impossible. Between any two rationals \( p < q \) lies a third, \( (p + q)/2 \), so no rational has a next one, and a list in increasing order cannot even get from \( q_0 \) to \( q_1 \). And yet a list need not be in increasing order. It only has to reach every element at some finite position. The rationals can be listed in that sense, and so can many sets that look larger than \( \nN \).

A list indexed by \( \nN \) is a function on \( \nN \), its \( n \)-th entry being the value at \( n \). Reaching every element is surjectivity.

*Countable means listable, repetitions allowed.*

::: {#def-countable}
[Countable Set]

A set \( A \) is **countable** if \( A = \emptyset \) or **there exists** a surjection \( f \colon \nN \to A \). In the second case
\[
A = f(\nN) = \{ f(0), f(1), f(2), \dots \} ,
\]
that is, the elements of \( A \) can be listed as \( x_0, x_1, x_2, \dots \), with \( x_n \coloneqq f(n) \), repetitions allowed. A set that is not countable is **uncountable**. In symbols, \( A \) is countable if and only if
\[
A = \emptyset \ \vee \ \exists f \in A^{\nN} \ \ \forall a \in A \ \ \exists n \in \nN \ \ f(n) = a .
\]
:::

In words: a non-empty set is countable when some list \( x_0, x_1, x_2, \dots \) reaches every one of its elements, each at a **finite** position \( n \in \nN \). The list may repeat an element as often as it likes, and it need not follow any order. The first clause is there because there is no function at all from \( \nN \) to \( \emptyset \) (@prp-empty-function (b)), so the second clause can never hold for the empty set; without the first clause, \( \emptyset \) would be uncountable. For a non-empty set the definition says that it is the image of some function from \( \nN \), which is how Chapter 11 states it.

Examples, starting from the smallest:

- \( \emptyset \) is countable, by the first clause.
- A non-empty finite set is countable. For three different objects \( a, b, c \), the list \( a, b, c, c, c, \dots \), that is \( f(0) \coloneqq a \), \( f(1) \coloneqq b \) and \( f(n) \coloneqq c \) for \( n \ge 2 \), is a surjection \( \nN \to \{a, b, c\} \). Repetitions pad a short list out to the length of \( \nN \).
- \( \nN \) is countable: \( \id_{\nN} \) is a surjection.
- The set of squares \( \{ n^2 : n \in \nN \} \) is countable: it is the image of \( \nN \) under \( n \mapsto n^2 \), and a function is a surjection onto its image (Section 8.1, "Shrinking the codomain"). In the same way \( 2\nN \) is countable.

**A non-example by a minimal change.** The list \( n \mapsto 2n \) is a list of \( 2\nN \). Read it as a list of \( \nN \), keeping the rule and changing only the target set, and it fails: the clause "for every \( a \in \nN \) there is an \( n \) with \( 2n = a \)" fails at \( a = 1 \). This shows that **this** list misses \( 1 \), not that \( \nN \) is uncountable; one map proves nothing about all maps (the warning after the non-example in Section 8.1). Sets that are genuinely uncountable appear in Section 8.4.

**Why repetitions are allowed.** Two reasons. First, finite sets are then countable with no special case: pad the list by repeating an element, as above. Second, the closure proofs below become short. A function applied to a list gives a list of the image, which may have repetitions even if the first list had none; interleaving lists of two overlapping sets repeats their common elements. If repetitions were forbidden, every such proof would need a step that deletes them. The definition puts that work in one place, the theorem on three ways to say countable below, and does it once.

Sometimes we need the stronger statement that a set has exactly the size of \( \nN \).

::: {#def-countably-infinite}
[Countably Infinite Set]

A set \( A \) is **countably infinite** if \( \card{A} = \card{\nN} \), that is, if there is a bijection \( A \to \nN \) (equivalently, by @prp-equinumerous-properties (b), a bijection \( \nN \to A \)).
:::

So \( \nN \), \( 2\nN \) and \( \nZ_{>0} \) are countably infinite (Section 8.1), and a countably infinite set is countable, since a bijection is a surjection.

::: {.warning}
In this book "countable" **includes** the finite sets and \( \emptyset \). Some books use "countable" to mean "countably infinite" and say "at most countable" for our "countable". Before quoting a theorem about countable sets from elsewhere, check which convention it uses. Here, \( \{0, 1\} \) is countable and is not countably infinite.
:::

## Subsets of the natural numbers

Every countable set will turn out to be finite or countably infinite, with nothing in between. The heart of that is a fact about subsets of \( \nN \): an infinite one can be listed in increasing order without gaps.

::: {#lem-subsets-of-naturals}
[Subsets of the Natural Numbers]

Every subset \( S \subseteq \nN \) is finite or countably infinite.
:::

::: {.idea}
If \( S \) is infinite, list it in increasing order: \( s_0 \) is the least element of \( S \), and \( s_{n+1} \) is the least element of \( S \) above \( s_n \). Well-ordering supplies each least element, provided the set is non-empty, and it is non-empty because \( S \) has elements beyond any bound, being infinite. Recursion turns the rule into a function. The list misses nothing: if \( t \in S \) were skipped, it would lie strictly between two consecutive entries \( s_{n-1} < t < s_n \), and then \( s_n \) would not be the least element of \( S \) above \( s_{n-1} \).
:::

::: {.proof}
If \( S \) is finite there is nothing to prove, so let \( S \) be infinite. In particular \( S \ne \emptyset \).

*Every \( x \in \nN \) has an element of \( S \) above it.* Let \( x \in \nN \), and suppose that no \( s \in S \) has \( s > x \). Then \( S \subseteq \{0, \dots, x\} \), a set with \( x + 1 \) elements (the third example after @def-finite), so \( S \) is finite by @prp-subset-finite, a contradiction. Hence \( T_x \coloneqq \{ s \in S : s > x \} \) is non-empty, and by @thm-well-ordering it has a least element.

*The list.* Define \( g \colon \nN \times \nN \to \nN \) by \( g(n, x) \coloneqq \min T_x \); by the previous paragraph this is defined for every \( x \in \nN \). By @thm-recursion, with \( X \coloneqq \nN \) and \( a \coloneqq \min S \) (which exists by @thm-well-ordering), there is a function \( n \mapsto s_n \) from \( \nN \) to \( \nN \) with
\[
s_0 = \min S , \qquad s_{n+1} = \min \{ s \in S : s > s_n \} \quad (n \in \nN) .
\]
Every \( s_n \) lies in \( S \): \( s_0 \in S \), and \( s_{n+1} \in T_{s_n} \subseteq S \).

*Increasing.* By construction \( s_{n+1} > s_n \) for every \( n \). Hence \( s_m < s_n \) whenever \( m < n \), by induction on \( n \): there is no \( m < 0 \) (@lem-naturals-arithmetic (a)), and if \( m < n + 1 \), then \( m \le n \) (@lem-naturals-arithmetic (e)), so \( s_m \le s_n < s_{n+1} \), using the hypothesis when \( m < n \). In particular \( n \mapsto s_n \) is injective, since \( m \ne n \) gives \( m < n \) or \( n < m \). Also \( s_n \ge n \) for every \( n \): \( s_0 \ge 0 \) (@lem-naturals-arithmetic (a)), and if \( s_n \ge n \), then \( s_{n+1} > s_n \ge n \), so \( s_{n+1} \ge n + 1 \) (@lem-naturals-arithmetic (e)).

*Onto \( S \).* Let \( t \in S \). The set \( \{ n \in \nN : s_n \ge t \} \) is non-empty, since \( s_t \ge t \), so it has a least element \( n \) by @thm-well-ordering. If \( n = 0 \), then \( s_0 = \min S \le t \) and \( s_0 \ge t \), so \( s_0 = t \). If \( n \ne 0 \), then \( n - 1 \in \nN \) (@lem-naturals-arithmetic (c)), and \( s_{n-1} < t \) by the minimality of \( n \). So \( t \in T_{s_{n-1}} \), and \( s_n = \min T_{s_{n-1}} \le t \). With \( s_n \ge t \) this gives \( s_n = t \).

So \( n \mapsto s_n \), with codomain \( S \), is a bijection \( \nN \to S \), and \( S \) is countably infinite.
:::

## Three ways to say countable

Being countable (empty or listable by \( \nN \)), having an injection into \( \nN \), and being finite or the size of \( \nN \) all describe the same sets. Having the three forms side by side is what makes countability easy to prove: we may use whichever is cheapest for the set in hand.

::: {#thm-countable-characterizations}
[Characterizations of Countable Sets]

For every set \( A \), the following are equivalent.

::: {.enumerate options="label=(\roman*)"}
1. \( A \) is countable.
2. There is an injection \( A \to \nN \).
3. \( A \) is finite or countably infinite.
:::
:::

::: {.idea}
From a list to an injection: send each element to the **first** position at which it appears. From an injection to (iii): the injection makes \( A \) equinumerous with a subset of \( \nN \), and @lem-subsets-of-naturals sorts those. From (iii) back to a list: pad a finite list by repetition, as in the examples above.
:::

::: {.proof}
(i) \( \Rightarrow \) (ii). If \( A = \emptyset \), the empty function \( \emptyset \to \nN \) is injective, vacuously. Otherwise let \( g \colon \nN \to A \) be a surjection. For \( a \in A \), the preimage \( g^{-1}(\{a\}) \subseteq \nN \) is non-empty, since \( g \) is onto, so it has a least element by @thm-well-ordering. Define \( h \colon A \to \nN \) by
\[
h(a) \coloneqq \min g^{-1}(\{a\}) .
\]
Then \( g(h(a)) = a \) for every \( a \in A \), that is, \( g \circ h = \id_A \), so \( h \) is injective by @thm-left-inverse-iff-injective (a).

(ii) \( \Rightarrow \) (iii). Let \( h \colon A \to \nN \) be injective. With its codomain shrunk to \( h(A) \), it is a bijection \( A \to h(A) \) (Section 8.1), so \( \card{A} = \card{h(A)} \). By @lem-subsets-of-naturals, \( h(A) \subseteq \nN \) is finite or countably infinite. If \( h(A) \) has \( n \) elements, there is a bijection \( \{1, \dots, n\} \to h(A) \), and following it by the inverse of \( A \to h(A) \) gives a bijection \( \{1, \dots, n\} \to A \) (@prp-equinumerous-properties (b) for the inverse, @thm-composition-injective-surjective (c)); so \( A \) has \( n \) elements. If \( \card{h(A)} = \card{\nN} \), then \( \card{A} = \card{\nN} \) by @prp-equinumerous-properties (c).

(iii) \( \Rightarrow \) (i). If \( A \) is countably infinite, a bijection \( \nN \to A \) is a surjection. Let \( A \) be finite with \( n \) elements. If \( n = 0 \), then \( A = \emptyset \), which is countable. If \( n \ge 1 \), let \( \varphi \colon \{1, \dots, n\} \to A \) be a bijection and define \( f \colon \nN \to A \) by
\[
f(k) \coloneqq
\begin{cases}
\varphi(k) & \text{if } 1 \le k \le n , \\
\varphi(1) & \text{if } k = 0 \text{ or } k > n .
\end{cases}
\]
Every \( a \in A \) is \( \varphi(k) = f(k) \) for some \( k \in \{1, \dots, n\} \), so \( f \) is a surjection. This proves the theorem.
:::

The step (i) \( \Rightarrow \) (ii) picks one element \( h(a) \) of \( g^{-1}(\{a\}) \) for **every** \( a \in A \) at once, and it needs no new principle for that, because there is a rule that names the element: the least one. That works because the preimages are subsets of \( \nN \), which is well-ordered. Section 8.3 meets a step that looks the same and has no such rule, and it is the point at which the book adds the axiom of choice.

In practice, (ii) is often the cheapest test. An injection into \( \nN \) only has to keep different elements apart, while a surjection has to reach every element, and (iii) asks for a bijection, which must do both.

## Closure properties

Three closure properties follow at once, each from the form of countability that suits it.

::: {#prp-countable-subset}
[Subsets of Countable Sets]

Every subset of a countable set is countable.
:::

::: {.proof}
Let \( B \) be countable and \( A \subseteq B \). By @thm-countable-characterizations, (i) \( \Rightarrow \) (ii), there is an injection \( h \colon B \to \nN \). Its restriction \( h|_A \colon A \to \nN \) is injective, since it has the same values. By (ii) \( \Rightarrow \) (i), \( A \) is countable.
:::

::: {#prp-countable-image}
[Images of Countable Sets]

Let \( A \) be countable and \( f \colon A \to B \) a function. Then \( f(A) \) is countable. In particular, if \( f \) is surjective, then \( B \) is countable.
:::

::: {.proof}
If \( A = \emptyset \), then \( f(A) = \emptyset \), which is countable. Otherwise let \( g \colon \nN \to A \) be a surjection. The function \( f \) with codomain \( f(A) \) is surjective (Section 8.1), so its composite with \( g \) is a surjection \( \nN \to f(A) \) by @thm-composition-injective-surjective (b). If \( f \) is surjective, then \( f(A) = B \).
:::

For unions we interleave two lists, taking the entries of the first list at the even positions and those of the second at the odd positions. That needs the fact that every natural number is even or odd, in exactly one way.

::: {#prp-union-two-countable}
[Union of Two Countable Sets]

If \( A \) and \( B \) are countable, then \( A \cup B \) is countable.
:::

::: {.idea}
Two lists \( a_0, a_1, \dots \) and \( b_0, b_1, \dots \) merge into one, \( a_0, b_0, a_1, b_1, \dots \): the entry at position \( 2q \) comes from the first list and the entry at position \( 2q + 1 \) from the second. For this to define a function, every position must be even or odd, and not both.
:::

::: {.proof}
If \( A = \emptyset \), then \( A \cup B = B \), and if \( B = \emptyset \), then \( A \cup B = A \); both are countable. So let \( g \colon \nN \to A \) and \( h \colon \nN \to B \) be surjections.

::: {.claim}
Every \( a \in \nN \) can be written as \( a = 2q + r \) with \( q \in \nN \) and \( r \in \{0, 1\} \), and the pair \( (q, r) \) is unique. In particular, no natural number is both of the form \( 2q \) and of the form \( 2q' + 1 \) with \( q, q' \in \nN \).
:::

::: {.proof}
By @thm-division-algorithm with divisor \( 2 \), there are unique integers \( q, r \) with \( a = 2q + r \) and \( 0 \le r < 2 \). Then \( r \in \nN \) by @prp-integers-closed (b), and \( r \le 1 \) by @lem-naturals-arithmetic (e), so \( r \in \{0, 1\} \). If \( q < 0 \), then \( q + 1 \le 0 \) by the discreteness clause @prp-integers-closed (c), so \( q \le -1 \) and \( a = 2q + r \le -2 + 1 < 0 \), which contradicts \( a \ge 0 \) (@lem-naturals-arithmetic (a)). So \( q \ge 0 \), and \( q \in \nN \) by @prp-integers-closed (b). Uniqueness among pairs with \( q \in \nN \) follows from uniqueness among all integer pairs. The last sentence is the uniqueness of \( r \).
:::

Define \( k \colon \nN \to A \cup B \) by
\[
k(2q) \coloneqq g(q) , \qquad k(2q + 1) \coloneqq h(q) \qquad (q \in \nN) .
\]
By the claim, each \( a \in \nN \) falls under exactly one of the two clauses, with exactly one \( q \), so \( k \) is a function. It is onto: an element of \( A \) is \( g(q) = k(2q) \) for some \( q \), and an element of \( B \) is \( h(q) = k(2q + 1) \) for some \( q \), where \( 2q \) and \( 2q + 1 \) lie in \( \nN \) by @lem-naturals-arithmetic (b). So \( A \cup B \) is countable.
:::

If \( A \) and \( B \) overlap, the interleaved list repeats their common elements, and the definition does not mind. By induction on the number of sets, a union of finitely many countable sets is countable. A union of **infinitely** many is a different matter, and Section 8.3 is about it.

## Pairs of natural numbers

The set \( \nN \times \nN \) looks two-dimensional, and a first attempt to list it shows where the difficulty lies.

::: {#exm-rows-first-listing}
[Listing the rows one after another]

Arrange \( \nN \times \nN \) in rows, the \( m \)-th row being \( (m, 0), (m, 1), (m, 2), \dots \). Consider the "list"
\[
(0, 0), (0, 1), (0, 2), \dots , \ \text{then} \ (1, 0), (1, 1), \dots , \ \text{then} \ (2, 0), \dots
\]
Is it a surjection \( \nN \to \nN \times \nN \)?
:::

::: {.solution}
No. A list indexed by \( \nN \) gives each entry a position \( n \in \nN \). Here position \( n \) holds \( (0, n) \), for every \( n \in \nN \): that already defines a function \( f(n) \coloneqq (0, n) \) on all of \( \nN \). No position is left for \( (1, 0) \): there is no \( n \in \nN \) with \( f(n) = (1, 0) \), since the first coordinate of every value is \( 0 \). The word "then" asks for positions after all the natural numbers, and there are none. So the claim that this is a list of \( \nN \times \nN \) is false. It is a list of the first row only.
:::

::: {.warning}
A list must give every entry a **finite** position. "First all of row \( 0 \), then all of row \( 1 \)" never reaches row \( 1 \), because row \( 0 \) uses up every position. The same mistake hides in any listing that runs through an infinite block before starting the next one.
:::

The conclusion that \( \nN \times \nN \) is countable is nevertheless true.

::: {#thm-product-countable}
[The Plane of Natural Numbers Is Countable]

The map \( p \colon \nN \times \nN \to \nN \), \( p(m, n) \coloneqq 2^m 3^n \), is injective. Hence \( \nN \times \nN \) is countable.
:::

*Try it first (ten minutes): list \( \nN \times \nN \), or inject it into \( \nN \). Which is less work to write down and check?*

::: {.idea}
The rows-first list fails, as we saw. A list that works runs along the diagonals \( m + n = 0, 1, 2, \dots \), each of which is finite; but writing a formula for the position of \( (m, n) \) and checking that every position is used takes real work. By @thm-countable-characterizations it is enough to **inject** \( \nN \times \nN \) into \( \nN \), and an injection only has to be a code from which \( m \) and \( n \) can be read back. In \( 2^m 3^n \), the power of \( 2 \) records \( m \) and the power of \( 3 \) records \( n \). To read them back we do not cite unique factorization into primes, which we have not proved. Parity does the job: cancel the smaller power of \( 2 \); if any factor \( 2 \) is left on one side, that side is even and the other is odd.
:::

::: {.proof}
First, \( p(m, n) \in \nN \) by @prp-power-laws (d) and @lem-naturals-arithmetic (b). Next, every power \( 3^k \) with \( k \in \nN \) is odd, that is, \( 3^k = 2j + 1 \) for some \( j \in \nN \): by @ax-induction, \( 3^0 = 1 = 2 \cdot 0 + 1 \), and if \( 3^k = 2j + 1 \), then \( 3^{k+1} = 3^k \cdot 3 = 2(3j + 1) + 1 \) (@def-power).

Let \( (m, n), (m', n') \in \nN \times \nN \) with \( 2^m 3^n = 2^{m'} 3^{n'} \). Suppose \( m \ne m' \). The hypothesis is symmetric in the two pairs, so we may assume \( m > m' \). Then \( m - m' \in \nN \) and \( m - m' \ge 1 \) (@lem-naturals-arithmetic (d), (e)), and \( 2^m = 2^{m'} 2^{m - m'} \) by @prp-power-laws (a). Canceling \( 2^{m'} \), which is positive by @prp-power-laws (e), gives
\[
2^{m - m'} 3^n = 3^{n'} .
\]
The left side is even: \( 2^{m - m'} = 2^{m - m' - 1} \cdot 2 \) by @def-power, where \( m - m' - 1 \in \nN \) by @lem-naturals-arithmetic (c), so the left side is \( 2 \) times the natural number \( 2^{m - m' - 1} 3^n \). The right side is odd, as shown above. No natural number is both even and odd, by the uniqueness of the remainder in @thm-division-algorithm with divisor \( 2 \) (the claim in the proof of @prp-union-two-countable). This contradiction shows \( m = m' \).

Canceling \( 2^m \) now gives \( 3^n = 3^{n'} \). By @prp-power-laws (e) with \( u = 3 > 1 \), \( n < n' \) would give \( 3^n < 3^{n'} \), and \( n' < n \) would give \( 3^{n'} < 3^n \); so \( n = n' \). Hence \( (m, n) = (m', n') \), and \( p \) is injective. By @thm-countable-characterizations, (ii) \( \Rightarrow \) (i), \( \nN \times \nN \) is countable.
:::

Alternatively, one can list \( \nN \times \nN \) along its diagonals: first the one pair with \( m + n = 0 \), then the two pairs with \( m + n = 1 \), then the three with \( m + n = 2 \), and so on. Each diagonal is finite, so every pair is reached after finitely many steps, and the list never stalls on an infinite block. Some readers find this picture more convincing than the code \( 2^m 3^n \). The injection is shorter to write out and to check, which is why the proof uses it.

The theorem passes to products of any countable sets. Chapter 6 defines \( X^n \) for one set \( X \); for several sets we first say what the product is. For an integer \( k \ge 2 \) and sets \( A_1, \dots, A_k \), let \( U \coloneqq \bigcup_{i \in \{1, \dots, k\}} A_i \) and
\[
A_1 \times \dots \times A_k \coloneqq \{ x \in U^k : x = (x_1, \dots, x_k) \text{ with } x_i \in A_i \text{ for every } i \} ,
\]
the \( k \)-tuples whose \( i \)-th coordinate lies in \( A_i \). It is a set by (W3), (W5) and (W1) of Section 6.1. For \( k = 2 \) it is \( A_1 \times A_2 \) of @def-cartesian-product, a pair being a \( 2 \)-tuple, and if every \( A_i \) is the same set \( X \), it is \( X^k \).

::: {#cor-product-countable}
[Products of Countable Sets]

::: {.enumerate options="label=(\alph*)"}
1. If \( A \) and \( B \) are countable, then \( A \times B \) is countable.
2. Let \( k \ge 2 \) be an integer. If \( A_1, \dots, A_k \) are countable, then \( A_1 \times \dots \times A_k \) is countable.
:::
:::

::: {.idea}
For two factors, injections \( A \to \nN \) and \( B \to \nN \) turn \( A \times B \) into a subset of \( \nN \times \nN \), and the code \( 2^m 3^n \) does the rest. More factors are added one at a time: a \( (k + 1) \)-tuple is a \( k \)-tuple followed by one more coordinate.
:::

::: {.proof}
*(a)* By @thm-countable-characterizations, (i) \( \Rightarrow \) (ii), there are injections \( i \colon A \to \nN \) and \( j \colon B \to \nN \). The map \( A \times B \to \nN \times \nN \), \( (a, b) \mapsto (i(a), j(b)) \), is injective: if \( (i(a), j(b)) = (i(a'), j(b')) \), then \( i(a) = i(a') \) and \( j(b) = j(b') \) by @def-ordered-pair, so \( a = a' \) and \( b = b' \). Following it by the injection \( p \) of @thm-product-countable gives an injection \( A \times B \to \nN \) (@thm-composition-injective-surjective (a)), and (ii) \( \Rightarrow \) (i) concludes. No case split is needed: if \( A = \emptyset \) or \( B = \emptyset \), then \( A \times B = \emptyset \) (@prp-product-set-laws), so the map \( (a, b) \mapsto (i(a), j(b)) \) and its composite with \( p \) are empty functions (@prp-empty-function (a)), which are injective vacuously.

*(b)* We use @thm-induction with \( n_0 = 2 \) on the statement "for all countable sets \( A_1, \dots, A_k \), the set \( A_1 \times \dots \times A_k \) is countable". *Base case \( k = 2 \).* This is (a). *Step.* Let \( k \ge 2 \), suppose the statement for \( k \), and let \( A_1, \dots, A_{k+1} \) be countable. The map
\[
\bigl( (a_1, \dots, a_k), a_{k+1} \bigr) \mapsto (a_1, \dots, a_{k+1})
\]
is a function, since a \( k \)-tuple determines its coordinates (Section 6.3), and it sends \( (A_1 \times \dots \times A_k) \times A_{k+1} \) onto \( A_1 \times \dots \times A_{k+1} \): a \( (k + 1) \)-tuple with \( x_i \in A_i \) is the image of \( ((x_1, \dots, x_k), x_{k+1}) \). By the hypothesis, \( A_1 \times \dots \times A_k \) is countable, so the domain is countable by (a), and the \( (k + 1) \)-fold product is countable by @prp-countable-image. By @thm-induction the statement holds for every \( k \ge 2 \).
:::

The map in the step is in fact a bijection, by the characteristic property of tuples (Section 6.3). The proof uses that property only to see that the map is well defined, and of the map it uses only that it is onto; injectivity is never needed. Tuples of different lengths are different objects, and the book has no \( 1 \)-tuples, so the corollary starts at \( k = 2 \); a single countable set needs no corollary.

::: {.check}
Let \( L \) be the set of the \( 26 \) letters a–z. Is the set of all strings of exactly \( 5 \) letters, that is \( L^5 \), countable? Which results do you use?
:::

::: {.solution}
Yes. The set \( L \) is finite, so it is countable by @thm-countable-characterizations, (iii) \( \Rightarrow \) (i). The strings of length \( 5 \) are the \( 5 \)-tuples of letters, \( L^5 = L \times L \times L \times L \times L \), which is countable by @cor-product-countable (b) with \( k = 5 \). (It is in fact finite, with \( 26^5 \) elements: the map in the step of the proof of @cor-product-countable (b) is a bijection \( L^k \times L \to L^{k+1} \) (the remark above), so Exercise C2 (a) of Section 8.1, applied for \( k = 2, 3, 4 \) after \( L^2 = L \times L \), counts it. Countability needs less than the count.)
:::

All strings of every finite length together form the union of the sets \( L^k \) over \( k \), a union of infinitely many countable sets. Section 8.3 takes up such unions.

## The integers and the rationals

Here is the answer to the question that opened the section. Recall from Section 7.1 that \( \nZ \coloneqq \nN \cup \{ -n : n \in \nN \} \), \( \nZ_{>0} \coloneqq \{ n \in \nN : n \ne 0 \} \) and \( \nQ \coloneqq \{ m/n : m \in \nZ, \ n \in \nZ_{>0} \} \).

::: {#thm-integers-rationals-countable}
[The Integers and the Rationals Are Countable]

\( \nN \), \( \nZ \) and \( \nQ \) are countable. Each of them is countably infinite.
:::

::: {.idea}
For \( \nZ \), interleave the non-negative and the negative integers, as in @prp-union-two-countable, but with explicit lists, so that the result is a bijection: \( 0, -1, 1, -2, 2, -3, \dots \). For \( \nQ \), do not try to list the fractions directly. Every rational is \( m/n \) for some pair \( (m, n) \in \nZ \times \nZ_{>0} \), and that set of pairs is countable, so \( \nQ \) is the image of a countable set.
:::

::: {.proof}
*\( \nN \).* The identity \( \id_{\nN} \) is a bijection \( \nN \to \nN \).

*\( \nZ \).* By the claim in the proof of @prp-union-two-countable, every \( n \in \nN \) is \( 2k \) or \( 2k + 1 \) for exactly one \( k \in \nN \), and not both. So we may define \( z \colon \nN \to \nZ \) by
\[
z(2k) \coloneqq k , \qquad z(2k + 1) \coloneqq -(k + 1) \qquad (k \in \nN) ,
\]
which begins \( z(0) = 0 \), \( z(1) = -1 \), \( z(2) = 1 \), \( z(3) = -2 \), \( z(4) = 2 \). It is injective: \( z(2k) = k \ge 0 \), while \( z(2k + 1) = -(k + 1) \le -1 < 0 \) (@lem-naturals-arithmetic (a)), so an even and an odd input never share a value; and \( k = k' \) or \( -(k + 1) = -(k' + 1) \) gives \( k = k' \). It is surjective: let \( m \in \nZ \). If \( m \in \nN \), then \( m = z(2m) \). Otherwise \( m = -n \) with \( n \in \nN \), and \( n \ne 0 \), since \( -0 = 0 \in \nN \); so \( n - 1 \in \nN \) by @lem-naturals-arithmetic (c), and \( m = -((n - 1) + 1) = z(2(n - 1) + 1) \). So \( z \) is a bijection.

*\( \nQ \).* The set \( \nZ_{>0} \subseteq \nN \) is countable by @prp-countable-subset, and \( \nZ \) is countable, so \( \nZ \times \nZ_{>0} \) is countable by @cor-product-countable (a). The map \( (m, n) \mapsto m/n \) from \( \nZ \times \nZ_{>0} \) to \( \nQ \) is defined, since \( n \ge 1 \) is not \( 0 \), and it is surjective by the definition of \( \nQ \). By @prp-countable-image, \( \nQ \) is countable. It is infinite: \( \nN \subseteq \nQ \), since \( n = n/1 \), and \( \nN \) is infinite (@exm-hilbert-hotel), so \( \nQ \) is not finite by @prp-subset-finite. By @thm-countable-characterizations, (i) \( \Rightarrow \) (iii), \( \nQ \) is countably infinite.
:::

The list of \( \nQ \) that the proof produces repeats every rational infinitely often: \( 1/1 \), \( 2/2 \), \( 3/3 \), … are all \( 1 \). The definition allows it, and that is what made the proof three lines. No line of the proof, or of the results it cites, uses the axiom of choice of Section 8.3: each surjection or injection it relies on is either given by a formula or named by a single \( \rulename{\exists E} \), and the only selections made for many elements at once are least elements (@thm-well-ordering). That \( \nQ \) can be listed is the fact Chapter 11 quotes when it compares \( \nQ \) with \( \nR \): the rationals, dense as they are, can be listed, while Chapter 11 shows that the reals cannot.

## Exercises

### A. Check your understanding

::: {#exr-countable-sets-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define "\( A \) is countable", and say why the empty set is mentioned separately in the definition.
2. True or false, with a reason: every infinite subset of \( \nQ \) is countably infinite; every countable set is finite or equinumerous with \( \nN \).
3. Which of the three forms (i)–(iii) of @thm-countable-characterizations is quickest to check for \( \{ n^2 : n \in \nN \} \), and why?
4. Where does the proof of (i) \( \Rightarrow \) (ii) in @thm-countable-characterizations use @thm-well-ordering, and to which set is it applied?
:::
:::

::: {.solution}
(a) \( A \) is countable if \( A = \emptyset \) or there is a surjection \( \nN \to A \) (@def-countable). The empty set is mentioned separately because there is no function \( \nN \to \emptyset \) at all (@prp-empty-function (b)), so the surjection clause never holds for \( \emptyset \).

(b) Both are true. An infinite \( A \subseteq \nQ \) is countable by @prp-countable-subset and @thm-integers-rationals-countable; by @thm-countable-characterizations, (i) \( \Rightarrow \) (iii), it is finite or countably infinite, and it is not finite. The second statement is (i) \( \Rightarrow \) (iii) itself, with "countably infinite" unfolded by @def-countably-infinite.

(c) Form (i): the set is given as the image of \( \nN \) under \( n \mapsto n^2 \), and a function is a surjection onto its image, so nothing is left to check. Form (ii) is almost as quick: the inclusion into \( \nN \) is injective. Form (iii) needs a bijection with \( \nN \), which costs a proof that \( n \mapsto n^2 \) is injective on \( \nN \).

(d) In defining \( h(a) \coloneqq \min g^{-1}(\{a\}) \): well-ordering is applied to the preimage \( g^{-1}(\{a\}) \subseteq \nN \), which is non-empty because \( g \) is onto. It gives every \( a \) a definite position, the first one at which \( a \) appears in the list, so no choice is needed.
:::

### B. Practice

::: {#exr-countable-sets-b1}
[B1]

Prove that each of the following sets is countable.

::: {.enumerate options="label=(\alph*)"}
1. \( 2\nN \times \nZ \).
2. \( \{ (m, n) \in \nN \times \nN : m < n \} \).
3. \( \nQ \times \nQ \), the points of the plane with rational coordinates.
4. The set of open intervals with rational endpoints, that is, of the sets \( \{ x \in \nR : a < x < b \} \) with \( a, b \in \nQ \) and \( a < b \).
:::
:::

::: {.solution}
(a) \( 2\nN \subseteq \nN \) is countable by @prp-countable-subset, and \( \nZ \) is countable by @thm-integers-rationals-countable; so \( 2\nN \times \nZ \) is countable by @cor-product-countable (a).

(b) It is a subset of \( \nN \times \nN \), which is countable by @thm-product-countable, so it is countable by @prp-countable-subset.

(c) \( \nQ \) is countable (@thm-integers-rationals-countable), so \( \nQ \times \nQ \) is countable by @cor-product-countable (a).

(d) Let \( D \coloneqq \{ (a, b) \in \nQ \times \nQ : a < b \} \), countable by (c) and @prp-countable-subset. Define \( J \colon D \to \powerset{\nR} \) by \( J(a, b) \coloneqq \{ x \in \nR : a < x < b \} \). The set of intervals in question is the image \( J(D) \), so it is countable by @prp-countable-image. (Here \( (a, b) \in D \) is an ordered pair, and the interval it names is written in set-builder notation, so the two readings of "\( (a, b) \)" never meet.)
:::

::: {#exr-countable-sets-b2}
[B2: Putting a proof in order]

The lines (i)–(ix) below include the seven lines of a proof that \( 2^m 3^n = 2^{m'} 3^{n'} \) implies \( m = m' \) and \( n = n' \), for \( m, n, m', n' \in \nN \), shuffled, together with two lines that do not belong. Write the seven lines in an order that makes a correct proof, and say why each of the other two lines fails.

::: {.enumerate options="label=(\roman*)"}
1. The left side is even, because \( m - m' \ge 1 \) by the supposition; the right side is odd; no natural number is both (@thm-division-algorithm, uniqueness of the remainder for divisor \( 2 \)). This is a contradiction.
2. Suppose \( 2^m 3^n = 2^{m'} 3^{n'} \).
3. The left side is odd and the right side is even, a contradiction.
4. Canceling \( 2^m \) gives \( 3^n = 3^{n'} \).
5. Suppose \( m \ne m' \); by symmetry, say \( m > m' \).
6. Since \( k \mapsto 3^k \) is strictly increasing on \( \nN \), \( n = n' \).
7. Since \( 2 \) and \( 3 \) are prime, unique factorization gives \( m = m' \) and \( n = n' \).
8. Canceling \( 2^{m'} \) gives \( 2^{m - m'} 3^n = 3^{n'} \).
9. So \( m = m' \).
:::
:::

::: {.solution}
The order is (ii), (v), (viii), (i), (ix), (iv), (vi). No other order is admissible. Line (ii) introduces the four numbers and the equation. Lines (v), (viii) and (i) are one proof by contradiction: (v) opens it, (viii) uses the supposition \( m > m' \) to cancel, and (i) closes it with a contradiction, so (ix), its conclusion, must come right after (i). Line (iv) cancels \( 2^m \) on both sides, which needs \( m = m' \), so it follows (ix); and (vi) uses the equation of (iv).

Line (iii) reverses the parities. The left side \( 2^{m - m'} 3^n \) has a factor \( 2 \) because \( m - m' \ge 1 \), so it is even; the right side \( 3^{n'} \) is odd. A line asserting the opposite is false: for \( m = 1 \), \( m' = 0 \), \( n = n' = 0 \), the left side is \( 2 \) and the right side is \( 1 \).

Line (vii) would end the proof at once, but it cites unique factorization into primes, which the book has neither proved nor taken as a school fact: Section 7.2 sets it aside as a fact it does not prove or use (after @def-prime), and the idea before @thm-product-countable declines to cite it. So (vii) cites a line that is not available, (N9) of @exm-not-allowed-catalogue. The theorem is true, and the conclusion of (vii) is true; the error is in the citation, which is exactly why the proof in the text goes through parity instead.
:::

::: {#exr-countable-sets-b3}
[B3: A surjection by formula]

Give an explicit surjection \( \nN \to \nN \times \{0, 1\} \) and prove that it is one. List the properties that any correct answer must have, so that a different answer can be checked against them.
:::

::: {.solution}
By the claim in the proof of @prp-union-two-countable, every \( a \in \nN \) is \( 2q + r \) for exactly one pair \( (q, r) \) with \( q \in \nN \) and \( r \in \{0, 1\} \). Define \( s \colon \nN \to \nN \times \{0, 1\} \) by \( s(2q + r) \coloneqq (q, r) \): so \( s(0) = (0, 0) \), \( s(1) = (0, 1) \), \( s(2) = (1, 0) \), \( s(3) = (1, 1) \). The uniqueness of the pair makes \( s \) a function. It is surjective: given \( (q, r) \in \nN \times \{0, 1\} \), the number \( a \coloneqq 2q + r \) lies in \( \nN \) (@lem-naturals-arithmetic (b)), and \( s(a) = (q, r) \). (It is even a bijection, by the uniqueness of the pair.)

A correct answer must:

- assign to **every** \( a \in \nN \) exactly one value, so that it is a function on all of \( \nN \);
- take its values in \( \nN \times \{0, 1\} \);
- reach every pair \( (q, 0) \) **and** every pair \( (q, 1) \), for every \( q \in \nN \), each at a finite position.

For instance \( s'(2q) \coloneqq (q, 1) \), \( s'(2q + 1) \coloneqq (q, 0) \) also qualifies. The rows-first attempt \( a \mapsto (a, 0) \), "then" the pairs \( (q, 1) \), fails the third property (@exm-rows-first-listing).
:::

### C. Going deeper

::: {#exr-countable-sets-c1}
[C1: Finite subsets of the natural numbers]

Let \( \sF \) be the set of all finite subsets of \( \nN \). Prove that \( \sF \) is countable, without using any result about unions of infinitely many sets.
:::

::: {.solution}
[Hint 1]

Inject \( \sF \) into \( \nN \) by sending \( F \) to \( S_N(F) \coloneqq \sum_{k=0}^{N} \ind_F(k) \, 2^k \), for any \( N \) with \( F \subseteq \{0, \dots, N\} \) (the value does not depend on \( N \)): the number whose binary digits are the indicator of \( F \).
:::

::: {.solution}
[Hint 2]

To prove injectivity, let \( m \) be the largest element at which two different sets \( F \ne G \) differ (the largest element of \( (F \setminus G) \cup (G \setminus F) \), a non-empty finite subset of \( \nN \)). The terms above \( m \) are the same for \( F \) and \( G \). Then use \( \sum_{k=0}^{m-1} 2^k = 2^m - 1 < 2^m \).
:::

::: {.solution}
The set \( \sF \subseteq \powerset{\nN} \) exists by specification. We build an injection \( \sigma \colon \sF \to \nN \) in four steps. For \( N \in \nN \) and \( F \subseteq \{0, \dots, N\} \) let
\[
S_N(F) \coloneqq \sum_{k=0}^{N} \ind_F(k) \, 2^k ,
\]
a finite sum as in @def-sum-product (indexed from \( 0 \)), where \( \ind_F \colon \nN \to \{0, 1\} \) is the indicator function of \( F \). Each term is \( 0 \) or \( 2^k \), and \( 2^k \in \nN \) by @prp-power-laws (d). So \( S_N(F) \in \nN \), by induction on \( N \) through the recursive clause of @def-sum-product, using @lem-naturals-arithmetic (b) at each step.

*Step 1: a bound.* Each term is at most \( 2^k \), so
\[
0 \le S_N(F) \le \sum_{k=0}^{N} 2^k = 2^{N+1} - 1 ,
\]
by @prp-geometric-sum with \( r = 2 \) (shifting the index by one).

*Step 2: one more term.* Splitting off the last term (Section 7.3), for \( F \subseteq \{0, \dots, N + 1\} \),
\[
S_{N+1}(F) = S_N\bigl(F \cap \{0, \dots, N\}\bigr) + \ind_F(N + 1) \, 2^{N+1} .
\]
In particular, if \( F \subseteq \{0, \dots, N\} \), then \( S_{N+1}(F) = S_N(F) \). By induction on \( N' \ge N \), \( S_{N'}(F) = S_N(F) \) for every \( N' \ge N \): the value does not depend on which bound \( N \) we use.

*Step 3: injective for a fixed \( N \).* We prove by @ax-induction on \( N \): if \( F, G \subseteq \{0, \dots, N\} \) and \( S_N(F) = S_N(G) \), then \( F = G \). For \( N = 0 \), \( F \) and \( G \) are \( \emptyset \) or \( \{0\} \), with values \( 0 \) and \( 1 \). For the step, let \( F, G \subseteq \{0, \dots, N + 1\} \) with \( S_{N+1}(F) = S_{N+1}(G) \), and write \( F' \coloneqq F \cap \{0, \dots, N\} \), \( G' \coloneqq G \cap \{0, \dots, N\} \). If \( N + 1 \in F \) and \( N + 1 \notin G \), then Steps 2 and 1 give
\[
S_{N+1}(F) \ge 2^{N+1} > 2^{N+1} - 1 \ge S_N(G') = S_{N+1}(G) ,
\]
a contradiction; the case \( N + 1 \in G \setminus F \) is the same with \( F \) and \( G \) exchanged. So \( N + 1 \) lies in both or in neither, the last terms in Step 2 agree, and \( S_N(F') = S_N(G') \). By the hypothesis, \( F' = G' \). Since \( \{0, \dots, N + 1\} = \{0, \dots, N\} \cup \{N + 1\} \), it follows that \( F = G \).

*Step 4: the injection.* Every \( F \in \sF \) lies in some \( \{0, \dots, N\} \): if \( F = \emptyset \), take \( N = 0 \); otherwise \( F \) is a non-empty finite set of real numbers, so it has a maximum \( M \in F \subseteq \nN \) (@prp-finite-max, as in the remark at the end of Section 8.1), and \( F \subseteq \{0, \dots, M\} \). Define \( \sigma(F) \coloneqq S_N(F) \) for any such \( N \); by Step 2 this does not depend on \( N \). If \( \sigma(F) = \sigma(G) \), take \( N \) at least as large as a bound for \( F \) and a bound for \( G \); then \( S_N(F) = S_N(G) \), and Step 3 gives \( F = G \). So \( \sigma \) is injective, and \( \sF \) is countable by @thm-countable-characterizations, (ii) \( \Rightarrow \) (i).

For example \( \sigma(\emptyset) = 0 \) (the empty set contributes no terms), \( \sigma(\{0, 2\}) = 1 + 4 = 5 \) and \( \sigma(\{1, 3\}) = 2 + 8 = 10 \): \( \sigma(F) \) is the number whose binary numeral has a \( 1 \) exactly in the places listed in \( F \). Step 3 is the uniqueness of binary numerals, and Step 4 uses no principle of choice: every value is given by a formula.

**Marking scheme.** (10 points)
- 2: defines a map from the finite subsets to \( \nN \) explicitly, including the value at \( \emptyset \), and checks that its values are natural numbers.
- 2: makes the map well defined, either by a bound-independent definition (as in Step 2) or by summing over the elements of \( F \) listed in increasing order.
- 4: proves injectivity, either by comparing the terms at the largest element at which \( F \) and \( G \) differ, using \( \sum_{k=0}^{m-1} 2^k < 2^m \), or by an induction on the bound as in Step 3, or by an equivalent proved uniqueness argument for binary numerals.
- 2: concludes with @thm-countable-characterizations, (ii) \( \Rightarrow \) (i).
- Route by surjection: an explicit map \( \nN \to \sF \) that reads off binary digits (for example, \( D(n) \) is the set of \( k \le n \) for which the quotient of \( n \) by \( 2^k \) in @thm-division-algorithm is odd) earns the same points: 2 for defining the map, 2 for checking that each value is a finite subset of \( \nN \), 4 for a proof that every \( F \in \sF \) is a value, and 2 for concluding by @def-countable.
Fatal errors (0 for the step): writing \( \sF \) as the union over \( n \) of the sets of \( n \)-element subsets and citing a result on countable unions (the task excludes it); asserting injectivity, or surjectivity on the second route, "by uniqueness of binary expansions" with no proof.
:::

::: {#exr-countable-sets-c2}
[C2: Find the error]

Here is a "proof" that every subset of a countable set is countable.

> Let \( B \) be countable and \( A \subseteq B \). (1) If \( A = \emptyset \), then \( A \) is countable by definition. (2) Otherwise \( B \ne \emptyset \), so there is a surjection \( g \colon \nN \to B \). (3) Define \( h \colon \nN \to A \) by \( h(n) \coloneqq g(n) \). (4) Let \( a \in A \). Then \( a \in B \), so \( a = g(n) \) for some \( n \in \nN \), and \( h(n) = a \). (5) Hence \( h \) is a surjection onto \( A \), and \( A \) is countable.

Is the conclusion true? Does the argument prove it? If not, name the line that fails, the rule it breaks, and give a counterexample **to that line**. Then repair the proof.
:::

::: {.solution}
The conclusion is true: it is @prp-countable-subset. The argument does not prove it.

Line (3) fails. It does not define a function from \( \nN \) to \( A \): @def-function requires, for **every** \( n \in \nN \), exactly one value **in \( A \)**, and when \( g(n) \notin A \) the formula offers no value in \( A \) at all. Counterexample to line (3): \( B = \nN \), \( g = \id_{\nN} \), \( A = \{1\} \). Then "\( h(2) = g(2) = 2 \)", and \( 2 \notin A \), so \( h \) is not a function into \( A \). Lines (1), (2) and (4) are correct, and (5) would follow if \( h \) were a function \( \nN \to A \).

*Repair.* In the case \( A \ne \emptyset \), fix one element \( a_0 \in A \) (one \( \rulename{\exists E} \)) and define
\[
h(n) \coloneqq
\begin{cases}
g(n) & \text{if } g(n) \in A , \\
a_0 & \text{if } g(n) \notin A .
\end{cases}
\]
Now \( h \) is a function \( \nN \to A \), and line (4) shows that it is onto: for \( a \in A \), some \( n \) has \( g(n) = a \in A \), and then \( h(n) = g(n) = a \). The repaired proof uses that \( A \) is non-empty, which line (1) had already split off; the flawed line ignored the elements of \( B \setminus A \), and the default value \( a_0 \) is where they go. The proof in the text avoids the issue by restricting an **injection** instead, since a restriction of a function is always a function.

**Marking scheme.** (10 points)
- 2: says the conclusion is true, citing @prp-countable-subset or an equivalent proof.
- 3: names line (3) and the broken requirement: a function into \( A \) needs a value in \( A \) at every \( n \) (@def-function).
- 2: gives a concrete instance of the failure of line (3), with a specific \( n \) whose value leaves \( A \).
- 3: repairs the proof with a default value in \( A \) (or by restricting an injection), and checks surjectivity.
Fatal errors (0 for the step): calling the conclusion false; blaming line (4) or (5); a "counterexample" that shows a subset that is not countable.
:::

<!-- dependency ledger
def-countable (claim): between rationals p < q lies (p + q)/2, a rational | Q arithmetic and order, school fact; axioms in Ch 11
def-countable (example): n -> n^2 and n -> 2n map N into N | lem-naturals-arithmetic (b) (cited elsewhere in the section)
lem-subsets-of-naturals (proof): trichotomy; s_m <= s_n < s_(n+1) | R order, school fact
thm-countable-characterizations (proof): a set with 0 elements is empty | Section 8.1, examples after def-finite (inline there)
prp-countable-subset (proof): a restriction of an injective function is injective | restriction, Section 6.4 (no label)
prp-union-two-countable (claim): 2q + r <= -2 + 1 < 0 for q <= -1, r <= 1 | R arithmetic and order, school fact
prp-union-two-countable (claim): "finitely many countable sets" by induction on the number of sets | inline sentence after the proof; nothing depends on it
thm-product-countable (proof): 3^k * 3 = 6j + 3 = 2(3j + 1) + 1; canceling a positive factor | R arithmetic, school fact
thm-product-countable (proof): trichotomy on N | R order, school fact
cor-product-countable (proof): k-tuples are determined by their coordinates; a (k+1)-tuple is the image of ((x_1, ..., x_k), x_(k+1)) | Section 6.3, n-tuples and their characteristic property (prose, no label)
cor-product-countable (claim): A_1 x ... x A_k is a set | (W1), (W3), (W5) of Section 6.1 (working rules, no label)
thm-integers-rationals-countable (proof): definitions of Z, Z_{>0}, Q | Section 7.1 (definitions in prose, no label)
thm-integers-rationals-countable (proof): -0 = 0; -(k + 1) <= -1 < 0; n = n/1 | R arithmetic and order, school fact
exr-countable-sets-b1 (solution): the interval {x in R : a < x < b} is a subset of R, so J maps into P(R) | def-power-set (Section 6.2)
exr-countable-sets-b2 (solution): 2^1 3^0 = 2, 2^0 3^0 = 1 | arithmetic, by hand
exr-countable-sets-c1 (solution): sum of terms each at most 2^k is at most the sum of the 2^k; splitting off the last term of a finite sum; shifting the index | R order, school fact; Section 7.3 (prose after def-sum-product, no label)
exr-countable-sets-c1 (solution): indicator function 1_F | Section 6.4 (example in prose)
exr-countable-sets-c1 (solution): a non-empty finite subset of N is {x_1, ..., x_n} | remark at the end of Section 8.1 (no label)
-->
