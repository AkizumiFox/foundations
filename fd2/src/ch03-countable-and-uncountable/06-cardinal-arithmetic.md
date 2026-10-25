# Cardinal Arithmetic

Section 2.5 counted finite sets, and Section 2.3 proved the laws of powers \( m^{n+k} = m^n m^k \) and \( (m^n)^k = m^{nk} \) by induction (@prp-power-laws). For finite sets these numbers count functions: \( Y^X \) has \( m^n \) elements when \( Y \) has \( m \) and \( X \) has \( n \) (Section 1.5, before @exm-function-set-small). This section asks what is left of that arithmetic when the sets are infinite and all we have are bijections.

## The plane and the line

A square has two dimensions and a segment has one. Surely the plane \( \nR \times \nR \) has more points than the line? The injection \( x \mapsto (x, 0) \) gives \( \card{\nR} \le \card{\nR \times \nR} \), and it seems that the other half of the plane should be left over.

A second question. Is \( \nN^{\nN} \), the set of sequences of natural numbers, bigger than \( \nR \)? A real number in \( [0, 1) \) is only a sequence of digits below \( 10 \), while a sequence in \( \nN^{\nN} \) may use any natural number at every place, so \( \nN^{\nN} \) looks bigger.

Guess both answers before reading on. The plane is a product, \( \nN^{\nN} \) is a power, and the line will turn out to be a power too: a power of \( 2 \).

## Adding sizes: disjoint unions

For finite sets that do not meet, Section 2.5 added sizes by taking the union (@prp-disjoint-union-count). So define the sum of two sets as their union? With \( A = B = \{0\} \) we want two elements, and \( A \cup B = \{0\} \) has one. The union counts the shared element once. The cure is to tag every element with the name of the set it came from, so that the two copies cannot overlap.

*A disjoint union keeps a labeled copy of each set, so nothing is counted twice.*

::: {#def-disjoint-union}
[Disjoint Union]

Let \( A \) and \( B \) be sets. Their **disjoint union** is
\[
A \sqcup B \coloneqq (A \times \{0\}) \cup (B \times \{1\}) .
\]
The maps \( \iota_A \colon A \to A \sqcup B \), \( \iota_A(a) \coloneqq (a, 0) \), and \( \iota_B \colon B \to A \sqcup B \), \( \iota_B(b) \coloneqq (b, 1) \), are the **inclusions**.
:::

In words: every element of \( A \sqcup B \) is \( (a, 0) \) with \( a \in A \) or \( (b, 1) \) with \( b \in B \), and **not both**, since \( (a, 0) = (b, 1) \) would give \( 0 = 1 \) by the characteristic property of pairs (@def-ordered-pair). By the same property each inclusion is injective, the two images are disjoint, and together they make up \( A \sqcup B \). So a function on \( A \sqcup B \) may be defined by giving its values on the two tagged parts separately: these are the two cases that cannot overlap, as in the proof of @prp-union-two-countable.

::: {#exm-two-copies-of-naturals}
[Two copies of ℕ]

Show that \( \card{\nN \sqcup \nN} = \card{\nN} \).
:::

::: {.solution}
This is the merging of two lists from the proof of @prp-union-two-countable, now as a bijection. Let \( e(n, 0) \coloneqq 2n \) and \( e(n, 1) \coloneqq 2n + 1 \), for \( n \in \nN \); by the unwinding above this defines \( e \colon \nN \sqcup \nN \to \nN \). For the decoder, let \( d(m) \coloneqq (q, r) \), where \( m = 2q + r \) with \( q \in \nN \) and \( r \in \{0, 1\} \); the pair exists and is unique by the claim in that proof, and \( (q, r) \in \nN \sqcup \nN \). Then \( d(e(n, r)) = (n, r) \) by the uniqueness, and \( e(d(m)) = 2q + r = m \). By @thm-bijection-iff-inverse, \( e \) is a bijection.

This is the first encoding of the section: \( e \) writes a pair as one number, and \( d \) reads it back. The method box comes with the next one.
:::

::: {.check}
(a) With \( a \ne b \), list the elements of \( \{a, b\} \sqcup \{a\} \) and of \( \{a, b\} \cup \{a\} \). (b) What is \( \emptyset \sqcup B \)? (c) If \( A \cap B = \emptyset \), give a bijection \( A \cup B \to A \sqcup B \).
:::

::: {.solution}
(a) \( \{a, b\} \sqcup \{a\} = \{ (a, 0), (b, 0), (a, 1) \} \), three elements; \( \{a, b\} \cup \{a\} = \{a, b\} \), two. (b) \( \emptyset \sqcup B = B \times \{1\} \), since \( \emptyset \times \{0\} = \emptyset \); and \( b \mapsto (b, 1) \) is a bijection \( B \to \emptyset \sqcup B \). (c) Send \( x \) to \( (x, 0) \) if \( x \in A \) and to \( (x, 1) \) if \( x \in B \). The cases do not overlap, since \( A \cap B = \emptyset \), so this is a function. Its inverse sends \( (a, 0) \mapsto a \) and \( (b, 1) \mapsto b \).
:::

::: {.warning}
**No subtraction.** For numbers, \( m + k = n + k \) gives \( m = n \). For sets, \( \card{\{0\} \sqcup \nN} = \card{\emptyset \sqcup \nN} \) although \( \card{\{0\}} \ne \card{\emptyset} \) (Exercise B4 (a)). Every law below is proved by a bijection, never borrowed from the numbers.
:::

## Multiplying, raising to powers, and comparing

Products \( A \times B \) (@def-cartesian-product) and sets of functions \( Y^X \) (Section 1.5) are the other two operations. If \( A \) has \( m \) elements and \( B \) has \( n \), then \( A \times B \) has \( mn \) elements and \( B^A \) has \( n^m \), as Exercise C2 of Section 2.5 counts. The base is written on the line and the exponent is the domain: \( Y^X \) is the set of functions **from** \( X \) **to** \( Y \).

Before any law, we check that the three operations see only sizes.

::: {#prp-card-operations-well-defined}
[Sums, Products and Powers Respect Size]

Let \( A, A', B, B' \) be sets with \( \card{A} = \card{A'} \) and \( \card{B} = \card{B'} \). Then

::: {.enumerate options="label=(\alph*)"}
1. \( \card{A \sqcup B} = \card{A' \sqcup B'} \);
2. \( \card{A \times B} = \card{A' \times B'} \);
3. \( \card{A^B} = \card{A'^{B'}} \).
:::
:::

::: {.idea}
Carry each element across along the bijections: on each tagged part for (a), on each coordinate for (b), and for (c) by composing a function with the bijections on both sides. The inverses carry everything back.
:::

::: {.proof}
Let \( \alpha \colon A \to A' \) and \( \beta \colon B \to B' \) be bijections, with two-sided inverses \( \alpha^{-1} \) and \( \beta^{-1} \) (@thm-bijection-iff-inverse).

(a) Send \( (a, 0) \mapsto (\alpha(a), 0) \) and \( (b, 1) \mapsto (\beta(b), 1) \); this is a function by the two-part rule after @def-disjoint-union. The same rule with \( \alpha^{-1} \) and \( \beta^{-1} \) undoes it on each part, so it is a two-sided inverse.

(b) Send \( (a, b) \mapsto (\alpha(a), \beta(b)) \). The map \( (a', b') \mapsto (\alpha^{-1}(a'), \beta^{-1}(b')) \) is a two-sided inverse, by @def-ordered-pair.

(c) For \( f \in A^B \), the composite \( \alpha \circ f \circ \beta^{-1} \) is a function \( B' \to A' \). Let \( \Theta(f) \coloneqq \alpha \circ f \circ \beta^{-1} \) and \( \Lambda(g) \coloneqq \alpha^{-1} \circ g \circ \beta \) for \( g \in A'^{B'} \). By @prp-composition-associative and \( \alpha^{-1} \circ \alpha = \id_A \), \( \beta^{-1} \circ \beta = \id_B \),
\[
\Lambda(\Theta(f)) = (\alpha^{-1} \circ \alpha) \circ f \circ (\beta^{-1} \circ \beta) = f ,
\]
and \( \Theta(\Lambda(g)) = g \) in the same way. In each part, @thm-bijection-iff-inverse gives a bijection.
:::

::: {.remark}
The proposition lets us replace either set by an equinumerous one without changing the size of the result. An answer computed from representatives must not depend on which representatives we used. Compare "send \( p/q \) to \( p \)" in Section 1.5 (@exm-not-a-function), which fails exactly this test.
:::

The comparison \( \le \) of @def-card-le is respected as well, with one exception.

::: {#prp-card-operations-monotone}
[Monotonicity]

Let \( A, A', B, B' \) be sets with \( \card{A} \le \card{A'} \) and \( \card{B} \le \card{B'} \). Then

::: {.enumerate options="label=(\alph*)"}
1. \( \card{A \sqcup B} \le \card{A' \sqcup B'} \);
2. \( \card{A \times B} \le \card{A' \times B'} \);
3. if \( A' \ne \emptyset \), then \( \card{A^B} \le \card{A'^{B'}} \).
:::
:::

::: {.idea}
Carry the injections across, as in the previous proof. For powers, a function on \( B \) must be extended to all of \( B' \), and the extension needs a value to put on the points that \( B \) does not reach.
:::

::: {.proof}
Let \( u \colon A \to A' \) and \( v \colon B \to B' \) be injections. (a), (b): the maps of the previous proof with \( u \), \( v \) in place of \( \alpha \), \( \beta \) are injective, by @def-ordered-pair.

(c) Fix \( a_0 \in A' \). For \( f \in A^B \) define \( F(f) \colon B' \to A' \) by
\[
F(f)(b') \coloneqq
\begin{cases}
u(f(b)) & \text{if } b' = v(b) \text{ for some } b \in B , \\
a_0 & \text{if } b' \notin v(B) .
\end{cases}
\]
In the first case \( b \) is unique, since \( v \) is injective, so \( F(f) \) is a function. If \( F(f) = F(g) \), then for every \( b \in B \),
\[
u(f(b)) = F(f)(v(b)) = F(g)(v(b)) = u(g(b)) ,
\]
so \( f(b) = g(b) \), since \( u \) is injective. Hence \( f = g \) (@prp-function-equality), and \( F \) is an injection \( A^B \to A'^{B'} \).
:::

**A non-example by minimal change.** Drop "\( A' \ne \emptyset \)" from (c), and take \( A = A' = \emptyset \), \( B = \emptyset \), \( B' = \{0\} \). Then \( \card{B} \le \card{B'} \), but \( \emptyset^{\emptyset} \) has one element, the empty function (@prp-empty-function), while \( \emptyset^{\{0\}} = \emptyset \); there is no injection from a one-element set into \( \emptyset \). The proof used \( a_0 \) exactly once, and here there is no \( a_0 \). (If \( A' = \emptyset \), then \( A = \emptyset \) too, since a function into \( \emptyset \) has empty domain.)

::: {.check}
Where does the proof of (c) use that \( v \) is injective? Where does it use that \( u \) is injective?
:::

::: {.solution}
Injectivity of \( v \) makes \( F(f) \) a function: the point \( b \) with \( v(b) = b' \) must be unique. Injectivity of \( u \) makes \( F \) injective: \( u(f(b)) = u(g(b)) \) must give \( f(b) = g(b) \).
:::

## Encoding: the diagonals of ℕ × ℕ

Section 3.1 showed \( \nN \times \nN \) countable by an injection. At the scratch work for @thm-product-countable it set aside the list along the diagonals, because writing a formula for the position of \( (m, n) \) and checking that every position is used takes real work. The Quick check before 3.4's Looking-ahead remark got \( \card{\nN \times \nN} = \card{\nN} \) from @thm-schroder-bernstein without ever seeing a bijection. Here is the work, done.

For \( s \in \nN \), the **triangular number** \( \tau_s \coloneqq \sum_{i=1}^{s} i \) (@def-sum-product) has \( \tau_0 = 0 \) and \( \tau_{s+1} = \tau_s + s + 1 \). It counts the points on the diagonals \( m + n = 0, 1, \dots, s - 1 \), which hold \( 1, 2, \dots, s \) points.

::: {#exm-pairing-bijection}
[The diagonal pairing of ℕ × ℕ with ℕ]

Show that \( \pi(m, n) \coloneqq \tau_{m+n} + n \) is a bijection \( \nN \times \nN \to \nN \).
:::

::: {.idea}
[Scratch work]

What must the code record? Which diagonal the point is on, \( s = m + n \), and its place on that diagonal, \( n \in \{0, \dots, s\} \); from \( s \) and \( n \) we read back \( m = s - n \). The diagonals before diagonal \( s \) hold \( 1 + 2 + \dots + s = \tau_s \) points, so the code counts them and adds the place. Small values: diagonal \( 0 \) gives \( 0 \); diagonal \( 1 \) gives \( 1, 2 \); diagonal \( 2 \) gives \( 3, 4, 5 \). The decoder must find, for each \( k \), the diagonal it falls on.

| Givens | Goal |
|---|---|
| \( (m, n) \in \nN \times \nN \) | \( \pi(m, n) \in \nN \) |
| \( k \in \nN \) | exactly one \( (m, n) \) with \( \tau_{m+n} + n = k \) |
| gap | every \( k \in \nN \) is \( \tau_s + n \) with \( s, n \in \nN \), \( n \le s \), in exactly one way |

Existence by induction on \( k \): stepping from \( k \) to \( k + 1 \) moves one place along the diagonal, or, at its end, to the start of the next one. Uniqueness: diagonal \( s \) fills the block \( \tau_s, \dots, \tau_s + s \), just below \( \tau_{s+1} \), so different diagonals give different numbers.
:::

::: {.solution}
::: {.claim}
For every \( k \in \nN \) there are \( s, n \in \nN \) with \( n \le s \) and \( k = \tau_s + n \), and the pair \( (s, n) \) is unique.
:::

::: {.proof}
*Existence*, by @thm-induction from \( 0 \). First, \( 0 = \tau_0 + 0 \). Suppose \( k = \tau_s + n \) with \( n \le s \). If \( n < s \), then \( k + 1 = \tau_s + (n + 1) \) with \( n + 1 \le s \). If \( n = s \), then \( k + 1 = \tau_s + s + 1 = \tau_{s+1} + 0 \).

*Uniqueness.* First, \( \tau_{j+1} = \tau_j + j + 1 > \tau_j \) for every \( j \), so if \( s < s' \), then \( \tau_{s+1} \le \tau_{s'} \), by @thm-induction on \( s' \) from \( s + 1 \). Now let \( \tau_s + n = \tau_{s'} + n' \) with \( n \le s \) and \( n' \le s' \), and suppose \( s \ne s' \); by symmetry \( s < s' \). Then
\[
\tau_s + n \le \tau_s + s < \tau_{s+1} \le \tau_{s'} \le \tau_{s'} + n' ,
\]
a contradiction. So \( s = s' \), and then \( n = n' \).
:::

*The bijection.* \( \pi(m, n) \in \nN \), since \( \tau_{m+n} \in \nN \) (@lem-naturals-arithmetic (b)). For \( k \in \nN \), write \( k = \tau_s + n \) by the claim and set \( \delta(k) \coloneqq (s - n, n) \), where \( s - n \in \nN \) because \( n \le s \) (@lem-naturals-arithmetic (d)); the uniqueness in the claim makes \( \delta \) a function. Then \( \pi(\delta(k)) = \tau_{(s - n) + n} + n = \tau_s + n = k \). And \( \delta(\pi(m, n)) = (m, n) \), by the uniqueness applied to \( k = \tau_{m+n} + n \), where \( s = m + n \ge n \). By @thm-bijection-iff-inverse, \( \pi \) is a bijection.

A table of the first values: \( \pi(0, 0) = 0 \), \( \pi(1, 0) = 1 \), \( \pi(0, 1) = 2 \), \( \pi(2, 0) = 3 \), \( \pi(1, 1) = 4 \), \( \pi(0, 2) = 5 \). Decoding \( 11 \): \( \tau_4 = 10 \le 11 < 15 = \tau_5 \), so \( 11 = \tau_4 + 1 \) and \( \delta(11) = (3, 1) \).
:::

::: {#exm-method-encode}
[Method: build a bijection by encoding and decoding]

**Template.** (1) Say what an element of the source must record for nothing to be lost. (2) Choose a code: a rule sending each element to an element of the target, and check that it lands there. (3) Write the decoder: a rule reading an element of the source back from each element of the target, and check that it is a function, with exactly one answer for each input. (4) Check both round trips and cite @thm-bijection-iff-inverse.

**When to use it.** The two sets carry the same information arranged differently: two numbers in one, a pair of sequences in one sequence, a function of two variables as a function with function values.

**The usual failure.** Checking one round trip only: \( \delta \circ \pi = \id \) alone shows only that \( \pi \) is injective (@thm-left-inverse-iff-injective). A decoder that is not a function, with two readings of one code or none (the interleaving of decimals, later in this section). If the decoder works on part of the target only, keep the injection and use @exm-method-injections-both-ways.
:::

::: {.warning}
An injective code is not yet a bijection. The code \( 2^m 3^n \) of @thm-product-countable is injective, but \( 5 \) is not a value, and no decoder is defined at \( 5 \). Step (3) of the method, a decoder defined on the **whole** target, is what makes \( \pi \) a bijection.
:::

::: {.check}
Compute \( \pi(3, 2) \) and \( \delta(47) \).
:::

::: {.solution}
\( \pi(3, 2) = \tau_5 + 2 = 15 + 2 = 17 \). For \( 47 \): \( \tau_9 = 45 \le 47 < 55 = \tau_{10} \), so \( 47 = \tau_9 + 2 \), and \( \delta(47) = (9 - 2, 2) = (7, 2) \). Check: \( \pi(7, 2) = \tau_9 + 2 = 47 \).
:::

## The laws of exponents, for all sets

For numbers, \( m^{n+k} = m^n m^k \) and \( (m^n)^k = m^{nk} \). Read through the sets these numbers count, each law says that two sets of functions are the same size, and for sets we must find the bijection.

::: {#thm-cardinal-laws}
[Laws of Cardinal Arithmetic]

For all sets \( A, B, C, X, Y, Z \):

::: {.enumerate options="label=(\alph*)"}
1. \( \card{A \sqcup B} = \card{B \sqcup A} \), \( \card{(A \sqcup B) \sqcup C} = \card{A \sqcup (B \sqcup C)} \), \( \card{A \times B} = \card{B \times A} \) and \( \card{(A \times B) \times C} = \card{A \times (B \times C)} \);
2. \( \card{A \times (B \sqcup C)} = \card{(A \times B) \sqcup (A \times C)} \);
3. \( X^{\emptyset} \) has exactly one element, and \( \card{X^{\{0\}}} = \card{X} \);
4. \( \card{X^{Y \sqcup Z}} = \card{X^Y \times X^Z} \);
5. \( \card{(X \times Y)^Z} = \card{X^Z \times Y^Z} \);
6. \( \card{(X^Y)^Z} = \card{X^{Y \times Z}} \).
:::
:::

::: {.idea}
[Scratch work]

For (d): what is an element of each side? On the left, a function \( h \) defined on the tagged copies of \( Y \) and \( Z \). On the right, a pair \( (f, g) \) with \( f \colon Y \to X \) and \( g \colon Z \to X \). A function on two disjoint pieces is the same thing as a function on each piece. So cut \( h \) into its two pieces by composing with the inclusions, and glue a pair back together piece by piece.

| Givens | Goal |
|---|---|
| \( h \in X^{Y \sqcup Z} \) | an element of \( X^Y \times X^Z \): \( (h \circ \iota_Y, h \circ \iota_Z) \) |
| \( (f, g) \in X^Y \times X^Z \) | one \( h \) with \( h \circ \iota_Y = f \) and \( h \circ \iota_Z = g \) |
| gap | \( h(y, 0) \coloneqq f(y) \), \( h(z, 1) \coloneqq g(z) \) is a function: the parts do not overlap (after @def-disjoint-union) |
:::

::: {.proof}
(d) Let \( \Phi(h) \coloneqq (h \circ \iota_Y, h \circ \iota_Z) \) for \( h \in X^{Y \sqcup Z} \). For \( (f, g) \in X^Y \times X^Z \), let \( \Psi(f, g) \) be the function \( h \colon Y \sqcup Z \to X \) with
\[
h(y, 0) \coloneqq f(y), \qquad h(z, 1) \coloneqq g(z) \qquad (y \in Y, \ z \in Z) .
\]
This is a function, because every element of \( Y \sqcup Z \) has exactly one of the two forms. Then \( \Phi(\Psi(f, g)) = (f, g) \): for \( y \in Y \), \( h(\iota_Y(y)) = h(y, 0) = f(y) \), so \( h \circ \iota_Y = f \) by @prp-function-equality, and likewise \( h \circ \iota_Z = g \); the pairs are equal by @def-ordered-pair. And \( \Psi(\Phi(h)) = h \): the two functions agree at every \( (y, 0) \) and every \( (z, 1) \), which are all the points of \( Y \sqcup Z \), so they are equal by @prp-function-equality. By @thm-bijection-iff-inverse, \( \Phi \) is a bijection.

(f) For \( g \in (X^Y)^Z \), each \( g(z) \) is a function \( Y \to X \). Let \( \Phi(g) \colon Y \times Z \to X \), \( \Phi(g)(y, z) \coloneqq g(z)(y) \). For \( h \in X^{Y \times Z} \) and \( z \in Z \), the rule \( y \mapsto h(y, z) \) is an element of \( X^Y \); let \( \Psi(h) \colon Z \to X^Y \) send \( z \) to it. Then
\[
\Phi(\Psi(h))(y, z) = \Psi(h)(z)(y) = h(y, z)
\]
for all \( (y, z) \), so \( \Phi(\Psi(h)) = h \). And \( \Psi(\Phi(g))(z) \) is the function \( y \mapsto g(z)(y) \), which is \( g(z) \); so \( \Psi(\Phi(g)) = g \). Here @prp-function-equality is used twice: first for functions on \( Y \), then for functions on \( Z \). By @thm-bijection-iff-inverse, \( \Phi \) is a bijection.

The remaining parts are proved by the same kind of regrouping; the maps are in the fold below.
:::

::: {.second-reading title="The other laws"}
Each map below has the stated inverse, and each round trip is one line of @prp-function-equality and @def-ordered-pair. As a sample, the associativity of \( \sqcup \) has three cases, one for each form of element; on \( ((b, 1), 0) \) the map gives \( ((b, 0), 1) \), and the inverse, reading the tag \( 1 \) outside and the tag \( 0 \) inside, returns \( ((b, 1), 0) \).

(a) \( A \sqcup B \to B \sqcup A \): \( (a, 0) \mapsto (a, 1) \), \( (b, 1) \mapsto (b, 0) \); it is its own inverse, with the roles of \( A \) and \( B \) exchanged. \( (A \sqcup B) \sqcup C \to A \sqcup (B \sqcup C) \): \( ((a, 0), 0) \mapsto (a, 0) \), \( ((b, 1), 0) \mapsto ((b, 0), 1) \), \( (c, 1) \mapsto ((c, 1), 1) \); the three forms of the source do not overlap, and the inverse reads the three forms of the target back. \( A \times B \to B \times A \): \( (a, b) \mapsto (b, a) \). \( (A \times B) \times C \to A \times (B \times C) \): \( ((a, b), c) \mapsto (a, (b, c)) \), with inverse \( (a, (b, c)) \mapsto ((a, b), c) \).

(b) \( A \times (B \sqcup C) \to (A \times B) \sqcup (A \times C) \): \( (a, (b, 0)) \mapsto ((a, b), 0) \) and \( (a, (c, 1)) \mapsto ((a, c), 1) \); the inverse moves the tag back inside.

(c) \( X^{\emptyset} = \{ (\emptyset, X) \} \), the empty function, by @prp-empty-function (a). The map \( f \mapsto f(0) \) is a bijection \( X^{\{0\}} \to X \), with inverse sending \( x \) to the function \( 0 \mapsto x \).

(e) Let \( p_1(x, y) \coloneqq x \) and \( p_2(x, y) \coloneqq y \) on \( X \times Y \). The map \( h \mapsto (p_1 \circ h, p_2 \circ h) \) from \( (X \times Y)^Z \) to \( X^Z \times Y^Z \) has the inverse \( (f, g) \mapsto \bigl(z \mapsto (f(z), g(z))\bigr) \).
:::

Law (f) is called **currying**: a function of two variables becomes a function whose values are functions. For finite sets with \( m \), \( n \) and \( k \) elements, the theorem gives back \( m^{n+k} = m^n m^k \) and \( (m^n)^k = m^{nk} \) with no induction in sight; the induction has moved into the counting of Section 2.5. Nothing in the proof used finiteness.

::: {#exm-method-laws-by-bijection}
[Method: prove a law of sizes by a bijection of sets]

**Template.** (1) Write out what an element of each side is: a tagged element, a pair, a function, a function with function values. (2) Find the map that only regroups: compose with the inclusions, pair the coordinates, or curry. (3) Write the reverse regrouping. (4) Check both round trips with @prp-function-equality and @def-ordered-pair, and cite @thm-bijection-iff-inverse.

**When to use it.** A law familiar from numbers, such as \( m^{n+k} = m^n m^k \), is claimed for sets of any size; or a size is to be computed by rewriting a set step by step.

**The usual failure.** Computing with symbols, as in "\( \card{X}^{\card{Y} + \card{Z}} = \card{X}^{\card{Y}} \card{X}^{\card{Z}} \)", when no number \( \card{X} \) exists and the step is the law itself: (N9) of @fd1:exm-not-allowed-catalogue. Dropping the tags: with \( \cup \) in place of \( \sqcup \) the law fails (Exercise B4 (b)).
:::

::: {.check}
Let \( X = \{0, 1\} \), \( Y = \{a\} \) and \( Z = \{b, c\} \). How many elements has each side of (d)? Let \( h(a, 0) = 1 \), \( h(b, 1) = 0 \), \( h(c, 1) = 1 \). What is \( \Phi(h) \)?
:::

::: {.solution}
\( Y \sqcup Z = \{ (a, 0), (b, 1), (c, 1) \} \) has three elements, and a function from it to \( \{0, 1\} \) is fixed by three values, each \( 0 \) or \( 1 \): \( 2 \cdot 2 \cdot 2 = 8 \) functions. On the right, \( X^Y \) has \( 2 \) elements and \( X^Z \) has \( 4 \), so the product has \( 2 \cdot 4 = 8 \). And \( \Phi(h) = (f, g) \) with \( f(a) = 1 \), \( g(b) = 0 \), \( g(c) = 1 \).
:::

## Subsets are 0–1 functions

Section 1.5 stated, for every set, that subsets and 0–1 functions match, and gave both maps: send \( f \) to \( \{ x : f(x) = 1 \} \) and \( A \) to \( \ind_A \). Here are the two round trips, which make \( 2 \) a base like any other.

::: {#thm-power-set-two-power}
[Subsets and 0–1 Functions]

For every set \( X \), the map \( A \mapsto \ind_A \) is a bijection \( \powerset{X} \to \{0, 1\}^X \), with inverse \( f \mapsto \{ x \in X : f(x) = 1 \} \). In particular \( \card{\powerset{X}} = \card{\{0, 1\}^X} \).
:::

::: {.proof}
For \( A \subseteq X \), \( \ind_A \in \{0, 1\}^X \) (@exm-first-functions (d)), and \( \{ x \in X : \ind_A(x) = 1 \} = A \) by the definition of \( \ind_A \). For \( f \in \{0, 1\}^X \), let \( S \coloneqq \{ x \in X : f(x) = 1 \} \). For \( x \in S \), \( \ind_S(x) = 1 = f(x) \). For \( x \in X \setminus S \), \( f(x) \ne 1 \), so \( f(x) = 0 = \ind_S(x) \). So \( \ind_S = f \) (@prp-function-equality). By @thm-bijection-iff-inverse, \( A \mapsto \ind_A \) is a bijection.
:::

Section 2.5 (the fold after @prp-power-set-count), Section 3.3 (after @cor-powerset-naturals-uncountable) and Section 3.4 (the Quick check after @prp-card-le-surjection) quoted this correspondence; it is now a theorem to cite.

::: {#cor-cantor-two-power}
[No Set Is the Size of Its 0–1 Functions]

For every set \( X \), \( \card{X} < \card{\{0, 1\}^X} \).
:::

::: {.idea}
One injection is easy; for strictness, move a bijection over to \( \powerset{X} \) with the theorem just proved, where Cantor's theorem forbids it.
:::

::: {.proof}
The map \( x \mapsto \ind_{\{x\}} \) is injective, since \( \ind_{\{x\}} \) takes the value \( 1 \) at \( x \) only; so \( \card{X} \le \card{\{0, 1\}^X} \). A bijection \( X \to \{0, 1\}^X \), followed by the inverse of the bijection of @thm-power-set-two-power, would be a bijection \( X \to \powerset{X} \) (@thm-composition-injective-surjective (c)), in particular a surjection, against @thm-cantor.
:::

So \( \nN \), \( \{0, 1\}^{\nN} \), \( \{0, 1\}^{\{0, 1\}^{\nN}} \), … grow strictly at each step, and there is no largest size.

## No set of all sets, once more

Section 3.3 (consequence (i) after @thm-cantor) saw that Russell's argument is Cantor's, with the rule \( f(x) = x \) and \( R_A \) in the role of \( D \). What is new here is a proof **by sizes** of the last clause of @thm-russell: there is no set of which every set is an element.

Suppose \( U \) were such a set. Every subset of \( U \) is a set, hence an element of \( U \), so \( \powerset{U} \subseteq U \). Define \( f \colon U \to \powerset{U} \) by \( f(u) \coloneqq u \) if \( u \in \powerset{U} \), and \( f(u) \coloneqq \emptyset \) otherwise. It is onto: each \( S \in \powerset{U} \) lies in \( U \), and \( f(S) = S \). This contradicts @thm-cantor.

Cantor's set for this \( f \), \( D = \{ u \in U : u \notin f(u) \} \), agrees with \( R_U = \{ u \in U : u \notin u \} \) on \( \powerset{U} \), and contains every \( u \in U \setminus \powerset{U} \), since \( u \notin \emptyset \). The unrestricted collection \( \{ x : x \notin x \} \) is never formed.

## The size of the line

The hook asked about \( \nR \times \nR \); first \( \nR \) itself. A real number in \( [0, 1) \) is a digit sequence, a function \( \nZ_{>0} \to \{0, \dots, 9\} \). So \( \nR \) should be a power, and that power should be a power of \( 2 \).

::: {#thm-reals-power-set-naturals}
[The Line Is a Power of Two]

\( \card{\nR} = \card{\{0, 1\}^{\nN}} = \card{\powerset{\nN}} \).
:::

::: {.idea}
Injections both ways (@exm-method-injections-both-ways). Into the 0–1 sequences, the digits are encoded and the laws do the bookkeeping. Out of them, a 0–1 sequence is read as decimal digits \( 0 \) and \( 1 \), which contain no \( 9 \).
:::

::: {.proof}
Let \( T \coloneqq \{0, 1, \dots, 9\} \) and \( D \coloneqq T^{\nZ_{>0}} \), the set of digit sequences (@def-decimal-expansion).

*\( \card{[0, 1)} \le \card{D} \).* This is the step of the proof of @thm-reals-uncountable-decimal. Send \( x \) to its expansion not ending in all \( 9 \)s: one exists by (D1), and only one by (D3), so the rule is a function and no choice is made. It is injective, since a digit sequence is an expansion of only one number, by (D2).

*\( \card{D} \le \card{\{0, 1\}^{\nN}} \).* The map \( n \mapsto n + 1 \) is a bijection \( \nN \to \nZ_{>0} \), so \( \card{D} = \card{T^{\nN}} \) (@prp-card-operations-well-defined (c)). The map \( t \mapsto \ind_{\{t\}} \) injects \( T \) into \( \{0, 1\}^T \), so \( \card{T^{\nN}} \le \card{(\{0, 1\}^T)^{\nN}} \) (@prp-card-operations-monotone (c), as \( \{0, 1\}^T \ne \emptyset \)), and this is \( \card{\{0, 1\}^{T \times \nN}} \) by @thm-cardinal-laws (f). A pair \( (t, n) \) is recorded by one number, by the method of @exm-method-encode: the code \( (t, n) \mapsto 10n + t \) is a bijection \( T \times \nN \to \nN \), whose decoder takes quotient and remainder on division by \( 10 \) (@thm-division-algorithm, with the quotient in \( \nN \) as in the claim in the proof of @prp-union-two-countable). So \( \card{\{0, 1\}^{T \times \nN}} = \card{\{0, 1\}^{\nN}} \) (@prp-card-operations-well-defined (c)). Composing the maps gives an injection \( D \to \{0, 1\}^{\nN} \) (@thm-composition-injective-surjective (a)).

*\( \card{\{0, 1\}^{\nN}} \le \card{[0, 1)} \).* For \( b \in \{0, 1\}^{\nN} \), let \( e_{k+1} \coloneqq b(k) \) for \( k \in \nN \): a digit sequence with digits \( 0 \) and \( 1 \) only. By (D2) it is an expansion of exactly one \( y_b \in [0, 1] \), and \( y_b \le t_1 + \frac{1}{10} \le \frac{2}{10} \) by @def-decimal-expansion at \( n = 1 \), so \( y_b \in [0, 1) \). If \( b \ne b' \), the two digit sequences differ. If also \( y_b = y_{b'} \), they would be two different expansions of one number, and by (D3) one of them would end in all \( 9 \)s; but neither contains a \( 9 \). So \( y_b \ne y_{b'} \), and \( b \mapsto y_b \) is injective.

*Conclusion.* By @prp-card-le-preorder (b) and @thm-schroder-bernstein, \( \card{[0, 1)} = \card{\{0, 1\}^{\nN}} \). By @exm-reals-open-interval, \( \card{[0, 1)} = \card{\nR} \), and by @thm-power-set-two-power, \( \card{\{0, 1\}^{\nN}} = \card{\powerset{\nN}} \). Chaining with @prp-equinumerous-properties proves the theorem.
:::

The first step is the one of Exercise C1 of Section 3.4. What is new is the middle step, where the laws replace that exercise's hand-built code \( 10k + d_k \), and the last, where the digits \( 0 \) and \( 1 \) suffice because (D3) needs only that no \( 9 \) appears. Neither step needed binary expansions of real numbers.

::: {.remark}
[Notation in other books]

Many books treat sizes as objects, called **cardinal numbers**, and write \( \aleph_0 \) for the size of \( \nN \) and \( 2^{\aleph_0} \), or \( \mathfrak c \), for the size of \( \nR \). Making a size into an object needs more set theory than this book uses (Section 2.5, the fold after @prp-equinumerous-properties). Here "\( \card{A} = 2^{\aleph_0} \)" can be read only as shorthand for \( \card{A} = \card{\{0, 1\}^{\nN}} \). Whether some subset of \( \nR \) is strictly bigger than \( \nN \) and strictly smaller than \( \nR \) is the **continuum hypothesis**; it is known to be neither provable nor refutable from the usual axioms of set theory, if those axioms are consistent.
:::

::: {.check}
Which step of the proof of @thm-reals-power-set-naturals uses the axiom of choice?
:::

::: {.solution}
None. The expansion of \( x \) is picked by a rule ("the one not ending in all \( 9 \)s"), every other map is a formula, and @thm-schroder-bernstein was proved without choice (Section 3.4).
:::

## Back to the plane

::: {#exm-interleaving-decimals}
[Interleaving digits]

The natural map \( [0, 1) \times [0, 1) \to [0, 1) \) interleaves digits. If \( x = 0.a_1 a_2 \ldots \) and \( y = 0.b_1 b_2 \ldots \), with the expansions not ending in all \( 9 \)s, let
\[
F(x, y) \coloneqq 0.a_1 b_1 a_2 b_2 \ldots ;
\]
the inverse splits the digits of \( z \) into the odd and the even places. Is \( F \) a bijection?
:::

::: {.solution}
*\( F \) is a function into \( [0, 1) \).* The expansions of \( x \) and \( y \) are fixed by the rule, as in the last proof. Let \( c \) be the interleaved sequence: \( c_{2k-1} \coloneqq a_k \), \( c_{2k} \coloneqq b_k \). It has infinitely many places that are not \( 9 \) (those of \( a \)), so it does not end in all \( 9 \)s, and by (D2) it is an expansion of exactly one \( z \in [0, 1] \). To see \( z < 1 \), let \( n \) be the first place with \( c_n \le 8 \) (@thm-well-ordering). Every earlier digit is \( 9 \), so by @prp-geometric-sum
\[
t_n \le \bigl(1 - 10^{-(n-1)}\bigr) + 8 \cdot 10^{-n} = 1 - 2 \cdot 10^{-n} ,
\]
and \( z \le t_n + 10^{-n} \le 1 - 10^{-n} < 1 \).

*\( F \) is injective.* If \( F(x, y) = F(x', y') = z \), both interleaved sequences are expansions of \( z \) and neither ends in all \( 9 \)s, so by (D3) they are equal. Then \( a = a' \) and \( b = b' \), and \( x = x' \), \( y = y' \) by (D2).

*\( F \) is not onto.* Take \( z = \frac{1}{11} = 0.090909\ldots \). The truncations at even places are \( t_{2j} = \frac{9}{99} (1 - 100^{-j}) = \frac{1}{11} - \frac{1}{11} 100^{-j} \) (@prp-geometric-sum with \( r = \frac{1}{100} \)), and the inequalities of @def-decimal-expansion hold at every place. This expansion has no tail of \( 0 \)s and no tail of \( 9 \)s, so by (D3) it is the only expansion of \( \frac{1}{11} \). A preimage \( (x, y) \) would need \( b = 9, 9, 9, \dots \); but \( b \) was the expansion of \( y \) not ending in all \( 9 \)s.

The splitting "inverse" named "the \( y \in [0, 1) \) whose expansion is \( 999\ldots \)" without checking that such a \( y \) exists: that is (N14) of @fd1:exm-not-allowed-catalogue. So the direct route gives an injection and no bijection. The injection is enough (@exm-method-injections-both-ways), and the laws give a bijection with no digit-fiddling.
:::

::: {#thm-plane-equinumerous-line}
[The Plane Is the Size of the Line]

\( \card{\nR \times \nR} = \card{\nR} \).
:::

::: {.idea}
By the method of @exm-method-laws-by-bijection: replace \( \nR \) by \( \{0, 1\}^{\nN} \) and rewrite the plane step by step.
:::

::: {.proof}
By @thm-reals-power-set-naturals and @prp-card-operations-well-defined (b), \( \card{\nR \times \nR} = \card{\{0, 1\}^{\nN} \times \{0, 1\}^{\nN}} \). By @thm-cardinal-laws (d), this is \( \card{\{0, 1\}^{\nN \sqcup \nN}} \). By @exm-two-copies-of-naturals and @prp-card-operations-well-defined (c), this is \( \card{\{0, 1\}^{\nN}} \), which is \( \card{\nR} \) by @thm-reals-power-set-naturals. Chaining with @prp-equinumerous-properties proves the theorem.
:::

Read through the maps, the composite on 0–1 sequences sends \( (a, b) \) to the sequence with \( a(n) \) at place \( 2n \) and \( b(n) \) at place \( 2n + 1 \): the interleaving of Exercise B3 of Section 3.4. The trouble with decimals has gone because 0–1 sequences, unlike numbers, have no double expansions. That price is paid once, in the proof of @thm-reals-power-set-naturals.

::: {#thm-baire-space-reals}
[Sequences of Natural Numbers]

\( \card{\nN^{\nN}} = \card{\nR} \).
:::

::: {.idea}
By the method of @exm-method-laws-by-bijection, with injections both ways: a 0–1 sequence is already a sequence of natural numbers, and a natural number is recorded by a 0–1 sequence.
:::

::: {.proof}
Send \( b \in \{0, 1\}^{\nN} \) to the same rule with codomain \( \nN \). This map is injective: two sequences with the same image have the same value at every point, so they are equal (@prp-function-equality). In the other direction, \( n \mapsto \ind_{\{n\}} \) is an injection \( \nN \to \{0, 1\}^{\nN} \), so \( \card{\nN^{\nN}} \le \card{(\{0, 1\}^{\nN})^{\nN}} \) (@prp-card-operations-monotone (c)). This is \( \card{\{0, 1\}^{\nN \times \nN}} \) (@thm-cardinal-laws (f)), and that is \( \card{\{0, 1\}^{\nN}} \) by @exm-pairing-bijection and @prp-card-operations-well-defined (c). By @prp-card-le-preorder (b) and @thm-schroder-bernstein, \( \card{\nN^{\nN}} = \card{\{0, 1\}^{\nN}} \), which is \( \card{\nR} \) by @thm-reals-power-set-naturals.
:::

Exercise B4 (d) of Section 3.4 reached the same equality through graphs and \( \powerset{\nN \times \nN} \).

::: {#cor-real-sequences}
[Sequences of Real Numbers]

\( \card{\nR^{\nN}} = \card{\nR} \).
:::

::: {.proof}
In one chain,
\[
\begin{aligned}
\card{\nR^{\nN}} &= \card{(\{0, 1\}^{\nN})^{\nN}} = \card{\{0, 1\}^{\nN \times \nN}} \\
&= \card{\{0, 1\}^{\nN}} = \card{\nR} ,
\end{aligned}
\]
by @prp-card-operations-well-defined (c) with @thm-reals-power-set-naturals, then @thm-cardinal-laws (f), then @exm-pairing-bijection with @prp-card-operations-well-defined (c), and @thm-reals-power-set-naturals again, chained by @prp-equinumerous-properties. No appeal to @thm-schroder-bernstein is needed.
:::

So both guesses of the hook were wrong. The plane is no bigger than the line, and \( \nN^{\nN} \) is no bigger either. For every infinite set \( X \) it is in fact true that \( \card{X \times X} = \card{X} \) and \( \card{X \sqcup X} = \card{X} \); in general these cannot be proved without the axiom of choice (the first is equivalent to it), and this book does not prove them.

::: {.check}
Show that \( \card{\nR^{\nN} \times \nR} = \card{\nR} \).
:::

::: {.solution}
By @cor-real-sequences and @prp-card-operations-well-defined (b), \( \card{\nR^{\nN} \times \nR} = \card{\nR \times \nR} \), which is \( \card{\nR} \) by @thm-plane-equinumerous-line; chain with @prp-equinumerous-properties.
:::

::: {.remark}
[Looking ahead]

Respecting size, @prp-card-operations-well-defined, is an instance of a requirement that Section 4.2 names: a rule stated through representatives must give the same answer for all of them. There it is called well-definedness, and it is what makes functions on quotient sets possible.
:::

## Exercises

### A. Check your understanding

::: {#exr-cardinal-arithmetic-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. True or false, for every set \( A \): \( \card{\emptyset \sqcup A} = \card{A} \); \( \emptyset \times A = \emptyset \); \( A^{\emptyset} \) has exactly one element; \( \emptyset^A = \emptyset \).
2. Under the bijection of @thm-cardinal-laws (f) with \( X = Y = \{0, 1\} \) and \( Z = \{0\} \), which element of \( (X^Y)^Z \) corresponds to \( h(y, z) \coloneqq y \)?
3. Give an injection \( \nR \sqcup \nN \to \nR \).
4. The proof of @thm-reals-power-set-naturals reads a 0–1 sequence as decimal digits \( 0 \) and \( 1 \). Which other pairs of digits would serve as well, by the same appeal to (D3)? Why does the pair \( 0 \) and \( 9 \) not follow from (D3) alone?
:::
:::

::: {.solution}
(a) True: \( \emptyset \sqcup A = A \times \{1\} \), and \( (a, 1) \mapsto a \) is a bijection onto \( A \). True: no pair has a first coordinate in \( \emptyset \). True, by @prp-empty-function (a). False: for \( A = \emptyset \), \( \emptyset^{\emptyset} \) has one element, the empty function; the claim holds for every non-empty \( A \), by @prp-empty-function (b).

(b) The \( g \) with \( g(0) = \id_{\{0, 1\}} \), since \( g(0)(y) = h(y, 0) = y \) for both \( y \in \{0, 1\} \).

(c) Send \( (x, 0) \mapsto x/(1 + \abs{x}) \), which lies in \( (-1, 1) \) (@exm-reals-open-interval), and \( (n, 1) \mapsto n + 1 \ge 1 \). Each part is injective (the first is a bijection onto \( (-1, 1) \), the second cancels the \( 1 \)), and the values of the two parts are disjoint, so the map is injective.

(d) Any pair that misses \( 9 \) works unchanged: a sequence with no \( 9 \)s cannot end in all \( 9 \)s, so (D3) rules out two different expansions of one number, and the first digit is at most \( 8 \), so \( y_b \le \frac{8}{10} + \frac{1}{10} < 1 \). Any pair that misses \( 0 \) gives an injection too, since a sequence with no \( 0 \)s cannot end in all \( 0 \)s; but if the pair contains \( 9 \), the sequence of all \( 9 \)s goes to \( 1 \), so the target must be widened to \( [0, 1] \), which @exm-reals-open-interval also covers. (The digits \( 1 \) and \( 2 \), used in Exercise C1 of Section 3.4, miss both.) With the digits \( 0 \) and \( 9 \), one sequence could end in all \( 9 \)s and another in all \( 0 \)s, which is exactly the situation (D3) allows; so (D3) alone does not decide whether \( b \mapsto y_b \) is injective, and a further computation at the first differing place would be needed.
:::

### B. Practice

::: {#exr-cardinal-arithmetic-b1}
[B1: Encodings]

Prove each equality by an explicit bijection and its inverse.

::: {.enumerate options="label=(\alph*)"}
1. \( \card{\nN \times \{0, 1, 2\}} = \card{\nN} \).
2. \( \card{\{0, 1\}^{\nN}} = \card{\{0, 1, 2, 3\}^{\nN}} \).
3. \( \card{\nN \times \nN \times \nN} = \card{\nN} \), using the pairing \( \pi \) of @exm-pairing-bijection twice, with an explicit decoder.
:::
:::

::: {.solution}
(a) Send \( (n, r) \mapsto 3n + r \). The inverse sends \( m \) to \( (q, r) \), the quotient and remainder of \( m \) on division by \( 3 \) (@thm-division-algorithm, with \( q \in \nN \) as in the claim in the proof of @prp-union-two-countable). Both round trips follow from the uniqueness in the division algorithm.

(b) For \( c \in \{0, 1\}^{\nN} \) let \( \Phi(c)(n) \coloneqq 2c(2n) + c(2n + 1) \in \{0, 1, 2, 3\} \). For the inverse, given \( d \in \{0, 1, 2, 3\}^{\nN} \), write \( d(n) = 2q_n + r_n \) with \( q_n, r_n \in \{0, 1\} \) (division by \( 2 \), unique), and set \( c(2n) \coloneqq q_n \), \( c(2n + 1) \coloneqq r_n \). This defines \( c \) on all of \( \nN \), since each \( m \in \nN \) is \( 2n \) or \( 2n + 1 \) for exactly one \( n \). The round trips follow from the two uniqueness statements and @prp-function-equality.

(c) Let \( E(m, n, k) \coloneqq \pi(\pi(m, n), k) \). The decoder sends \( k' \) to \( (m, n, k) \), where \( \delta(k') = (j, k) \) and \( \delta(j) = (m, n) \). The round trips follow from \( \delta \circ \pi = \id \) and \( \pi \circ \delta = \id \), each used twice, together with the characteristic property of triples (the paragraph after the proof of @cor-product-countable). For example, \( E(1, 0, 1) = \pi(\pi(1, 0), 1) = \pi(1, 1) = 4 \).
:::

::: {#exr-cardinal-arithmetic-b2}
[B2: More laws]

By the method of @exm-method-laws-by-bijection, prove for all sets \( A, B, X \):

::: {.enumerate options="label=(\alph*)"}
1. \( \card{\powerset{A \sqcup B}} = \card{\powerset{A} \times \powerset{B}} \);
2. \( \card{X^{\{0, 1\}}} = \card{X \times X} \).
:::
:::

::: {.solution}
(a) Directly: send \( S \mapsto (\{ a \in A : (a, 0) \in S \}, \{ b \in B : (b, 1) \in S \}) \), with inverse \( (S_1, S_2) \mapsto (S_1 \times \{0\}) \cup (S_2 \times \{1\}) \). The round trips hold because every element of \( A \sqcup B \) is \( (a, 0) \) or \( (b, 1) \), and not both (after @def-disjoint-union). Or by laws: \( \card{\powerset{A \sqcup B}} = \card{\{0, 1\}^{A \sqcup B}} \) by @thm-power-set-two-power, which is \( \card{\{0, 1\}^A \times \{0, 1\}^B} \) by @thm-cardinal-laws (d), which is \( \card{\powerset{A} \times \powerset{B}} \) by @thm-power-set-two-power twice with @prp-card-operations-well-defined (b).

(b) Send \( f \mapsto (f(0), f(1)) \), with inverse sending \( (x, x') \) to the function \( 0 \mapsto x \), \( 1 \mapsto x' \). Or from (c) and (d) of @thm-cardinal-laws, since \( \{0, 1\} \) is the same size as \( \{0\} \sqcup \{0\} \), by \( 0 \mapsto (0, 0) \), \( 1 \mapsto (0, 1) \).
:::

::: {#exr-cardinal-arithmetic-b3}
[B3: Sets the size of the line, used later]

Prove:

::: {.enumerate options="label=(\alph*)"}
1. \( \card{\nN \times \nR} = \card{\nR} \);
2. \( \card{\nR \sqcup \nR} = \card{\nR} \);
3. \( \card{\nR^k} = \card{\nR} \) for every integer \( k \ge 2 \).
:::
:::

::: {.solution}
(a) \( x \mapsto (0, x) \) injects \( \nR \) into \( \nN \times \nR \). In the other direction, \( \nN \times \nR \subseteq \nR \times \nR \), so the inclusion followed by a bijection \( \nR \times \nR \to \nR \) (@thm-plane-equinumerous-line) is an injection \( \nN \times \nR \to \nR \). Apply @thm-schroder-bernstein.

(b) Unwinding @def-disjoint-union, \( \nR \sqcup \nR = (\nR \times \{0\}) \cup (\nR \times \{1\}) = \nR \times \{0, 1\} \), a subset of \( \nR \times \nR \); so it injects into \( \nR \) as in (a). And \( x \mapsto (x, 0) \) injects \( \nR \) into \( \nR \sqcup \nR \). Apply @thm-schroder-bernstein.

(c) By @thm-induction with \( n_0 = 2 \). The base case \( k = 2 \) is @thm-plane-equinumerous-line. Step: the map \( ((x_1, \dots, x_k), x_{k+1}) \mapsto (x_1, \dots, x_{k+1}) \) is a bijection \( \nR^k \times \nR \to \nR^{k+1} \), by the characteristic property of tuples (the paragraph after the proof of @cor-product-countable). So
\[
\card{\nR^{k+1}} = \card{\nR^k \times \nR} = \card{\nR \times \nR} = \card{\nR} ,
\]
by the hypothesis with @prp-card-operations-well-defined (b), then @thm-plane-equinumerous-line, chained by @prp-equinumerous-properties. (The book has no \( 1 \)-tuples and defines \( X^k \) for \( k \ge 2 \) only, so the induction starts at \( 2 \).)
:::

::: {#exr-cardinal-arithmetic-b4}
[B4: Prove or disprove]

Prove each true statement and refute each false one with a counterexample. Here \( A, B, C, X, Y, Y', Z \) are sets.

::: {.enumerate options="label=(\alph*)"}
1. If \( \card{A \sqcup C} = \card{B \sqcup C} \), then \( \card{A} = \card{B} \).
2. \( \card{X^{Y \cup Z}} = \card{X^Y \times X^Z} \).
3. If \( \card{Y} \le \card{Y'} \), then \( \card{X^Y} \le \card{X^{Y'}} \).
4. \( \card{\nN^{\{0, 1\}}} = \card{\{0, 1\}^{\nN}} \).
5. If \( \card{A} < \card{B} \) and \( C \ne \emptyset \), then \( \card{A \times C} < \card{B \times C} \).
6. There is a set \( X \) with \( \card{\{0, 1\}^X} \le \card{X} \).
:::
:::

::: {.solution}
(a) False. Take \( A = \{0\} \), \( B = \emptyset \), \( C = \nN \). The map \( (0, 0) \mapsto 0 \), \( (n, 1) \mapsto n + 1 \) is a bijection \( \{0\} \sqcup \nN \to \nN \), with inverse \( 0 \mapsto (0, 0) \) and \( m \mapsto (m - 1, 1) \) for \( m \ge 1 \) (@lem-naturals-arithmetic (c)). And \( (n, 1) \mapsto n \) is a bijection \( \emptyset \sqcup \nN = \nN \times \{1\} \to \nN \). So both sides are the size of \( \nN \), while \( \card{\{0\}} \ne \card{\emptyset} \).

(b) False. Take \( X = \{0, 1\} \) and \( Y = Z = \{0\} \). Then \( Y \cup Z = \{0\} \), and \( X^{Y \cup Z} \) has \( 2 \) elements, while \( X^Y \times X^Z \) has \( 2 \cdot 2 = 4 \). Finite sets with different numbers of elements are not equinumerous (@cor-finite-size-unique). The statement is true when \( Y \cap Z = \emptyset \), by Quick check 1 (c) and @thm-cardinal-laws (d).

(c) False. Take \( X = \emptyset \), \( Y = \emptyset \), \( Y' = \{0\} \): this is the non-example after @prp-card-operations-monotone. It is true when \( X \ne \emptyset \), by @prp-card-operations-monotone (c).

(d) False. The map \( f \mapsto (f(0), f(1)) \) is a bijection \( \nN^{\{0, 1\}} \to \nN \times \nN \), with inverse sending \( (m, n) \) to the function \( 0 \mapsto m \), \( 1 \mapsto n \). Since \( \nN \times \nN \) is countable (@thm-product-countable), there is an injection \( \nN \times \nN \to \nN \) (@thm-countable-characterizations), and so an injection \( \nN^{\{0, 1\}} \to \nN \) (@thm-composition-injective-surjective (a)). If \( \nN^{\{0, 1\}} \) were the same size as \( \{0, 1\}^{\nN} \), composing would inject \( \{0, 1\}^{\nN} \) into \( \nN \), making it countable (@thm-countable-characterizations), against @thm-binary-sequences-uncountable. Base and exponent do not commute.

(e) False. Take \( A = \{0\} \), \( B = \{0, 1\} \), \( C = \nN \); then \( \card{A} < \card{B} \) (@cor-finite-size-unique for "no bijection"). But \( \card{\{0\} \times \nN} = \card{\nN} \), by \( (0, n) \mapsto n \), and \( \card{\{0, 1\} \times \nN} = \card{\nN} \): the map \( (r, n) \mapsto (n, r) \) is a bijection \( \{0, 1\} \times \nN \to \nN \sqcup \nN \), and @exm-two-copies-of-naturals finishes.

(f) False. For every \( X \), \( x \mapsto \ind_{\{x\}} \) gives \( \card{X} \le \card{\{0, 1\}^X} \), so \( \card{\{0, 1\}^X} \le \card{X} \) would give \( \card{X} = \card{\{0, 1\}^X} \) by @thm-schroder-bernstein, against @cor-cantor-two-power.
:::

### C. Going deeper

::: {#exr-cardinal-arithmetic-c1}
[C1: Functions from the line to the line]

Prove that \( \card{\nR^{\nR}} = \card{\powerset{\nR}} \). Deduce that there is no surjection \( \nR \to \nR^{\nR} \).
:::

::: {.solution}
[Hint 1]

Replace the base \( \nR \) by \( \{0, 1\}^{\nN} \), then curry.
:::

::: {.solution}
[Hint 2]

You will need \( \card{\nN \times \nR} = \card{\nR} \).
:::

::: {.solution}
Let \( \beta \colon \nR \to \{0, 1\}^{\nN} \) be a bijection (@thm-reals-power-set-naturals). Then
\[
\begin{aligned}
\card{\nR^{\nR}} &= \card{(\{0, 1\}^{\nN})^{\nR}} = \card{\{0, 1\}^{\nN \times \nR}} \\
&= \card{\{0, 1\}^{\nR}} = \card{\powerset{\nR}} ,
\end{aligned}
\]
by @prp-card-operations-well-defined (c) with \( \beta \) and \( \id_{\nR} \); then @thm-cardinal-laws (f) with \( Y = \nN \), \( Z = \nR \); then @exr-cardinal-arithmetic-b3 (a) with @prp-card-operations-well-defined (c), now in the exponent; then @thm-power-set-two-power; chained by @prp-equinumerous-properties.

For the second part, let \( \Theta \colon \nR^{\nR} \to \powerset{\nR} \) be a bijection. If \( s \colon \nR \to \nR^{\nR} \) were onto, then \( \Theta \circ s \colon \nR \to \powerset{\nR} \) would be onto (@thm-composition-injective-surjective (b)), against @thm-cantor. So there are more functions \( \nR \to \nR \) than real numbers.

**Marking scheme.** (10 points)
- 2: replaces the base \( \nR \) by \( \{0, 1\}^{\nN} \), citing the bijection and @prp-card-operations-well-defined (c).
- 3: applies currying in the right direction: \( (X^Y)^Z \) with \( Y = \nN \), \( Z = \nR \), to reach \( \{0, 1\}^{\nN \times \nR} \).
- 2: uses \( \card{\nN \times \nR} = \card{\nR} \) together with respecting size in the exponent.
- 1: passes from \( \{0, 1\}^{\nR} \) to \( \powerset{\nR} \).
- 2: rules out a surjection by composing with the bijection and citing @thm-cantor.
Fatal errors (0 for the step): computing with symbols as if sizes were numbers ("\( \mathfrak c^{\mathfrak c} = 2^{\aleph_0 \mathfrak c} \)") with no bijection behind each step.
:::

::: {#exr-cardinal-arithmetic-c2}
[C2: Find the error]

Claim: \( \{0, 1\}^{\nN} \) is countable.

> *Proof.* Send \( b \) to the natural number \( N(b) \coloneqq \sum_k b(k) 2^k \). Different sequences have different binary digits, so \( N \) is injective, and an injection into \( \nN \) makes a set countable (@thm-countable-characterizations).

Is the conclusion true? Where does the argument fail? What does it prove?
:::

::: {.solution}
*The conclusion is false*: \( \{0, 1\}^{\nN} \) is uncountable (@thm-binary-sequences-uncountable).

*The error is in the first line.* \( N(b) \) is named before it is shown to exist: (N14) of @fd1:exm-not-allowed-catalogue. The sum is infinite whenever \( b \) has infinitely many \( 1 \)s, and Section 2.3 defines only finite sums (@def-sum-product); no natural number is "\( 1 + 2 + 4 + \cdots \)". The all-\( 1 \) sequence is a witness: it has no value under \( N \).

*What survives.* On the sequences that are eventually \( 0 \), the sum is finite (\( \sum_{k < K} b(k) 2^k \) for any \( K \) past the last \( 1 \)), and \( N \) is defined there. It is injective once the uniqueness of binary digits is proved, which Exercise R1 below does not do (R1 gives existence only). The countability of that set follows anyway, with no binary digits: changing the codomain from \( \{0, 1\} \) to \( \nN \) injects it into the set of eventually zero functions \( \nN \to \nN \) of @exr-infinite-sets-r4, at the end of this section, which is countable; compose with an injection of that set into \( \nN \) (@thm-countable-characterizations, @thm-composition-injective-surjective (a)).

**Marking scheme.** (10 points)
- 2: says the conclusion is false, citing @thm-binary-sequences-uncountable.
- 3: names the failing step, an infinite sum named as a natural number, with (N14).
- 2: gives a witness, such as the all-\( 1 \) sequence.
- 2: says what the argument does prove: the eventually zero sequences form a countable set.
- 1: flags that the injectivity of \( N \) on them needs the uniqueness of binary digits, which is not proved.
Fatal errors (0 for the step): calling the conclusion true; locating the error in "an injection into \( \nN \) makes a set countable", which is correct.
:::

::: {#exr-cardinal-arithmetic-c3}
[C3: Rearrangements of ℕ]

Let \( B \) be the set of bijections \( \nN \to \nN \). Exercise C2 of Section 3.3 showed that \( B \) is uncountable. Prove that it has exactly the size of \( \nR \): \( \card{B} = \card{\nR} \).
:::

::: {.solution}
*Up.* Every bijection \( \nN \to \nN \) is a function \( \nN \to \nN \), so \( B \subseteq \nN^{\nN} \), and the inclusion followed by a bijection \( \nN^{\nN} \to \nR \) (@thm-baire-space-reals) is an injection \( B \to \nR \).

*Down.* For \( b \in \{0, 1\}^{\nN} \), let \( \sigma_b \colon \nN \to \nN \) swap \( 2n \) and \( 2n + 1 \) when \( b(n) = 1 \), and fix them when \( b(n) = 0 \); this is a function, since each \( m \in \nN \) is \( 2n \) or \( 2n + 1 \) for exactly one \( n \). It is its own inverse, so \( \sigma_b \in B \) (@thm-bijection-iff-inverse). The map \( b \mapsto \sigma_b \) is injective, since \( b(n) = 1 \) exactly when \( \sigma_b(2n) = 2n + 1 \). This is the construction of @exr-diagonal-arguments-c2.

By @thm-schroder-bernstein, \( \card{B} = \card{\{0, 1\}^{\nN}} \), and this is \( \card{\nR} \) by @thm-reals-power-set-naturals.

**Marking scheme.** (10 points)
- 3: shows \( \card{B} \le \card{\nR} \), through \( B \subseteq \nN^{\nN} \) and @thm-baire-space-reals.
- 3: defines \( \sigma_b \) and shows that it is a bijection of \( \nN \).
- 2: shows that \( b \mapsto \sigma_b \) is injective, by reading \( b(n) \) off \( \sigma_b(2n) \).
- 2: concludes by @thm-schroder-bernstein and @thm-reals-power-set-naturals.
Fatal errors (0 for the step): concluding \( \card{B} = \card{\nR} \) from "\( B \) is uncountable and \( B \subseteq \nN^{\nN} \)" alone, with no injection from a set the size of \( \nR \) into \( B \).
:::

### R. Review

::: {#exr-infinite-sets-r1}
[R1]

Prove that every integer \( n \ge 1 \) is a sum of distinct powers of \( 2 \): there are an integer \( r \ge 1 \) and natural numbers \( k_1 > k_2 > \dots > k_r \) with \( n = 2^{k_1} + 2^{k_2} + \dots + 2^{k_r} \).
:::

::: {.solution}
We use @thm-strong-induction-from-base with \( n_0 = 1 \). Let \( n \ge 1 \), and suppose every integer \( m \) with \( 1 \le m < n \) is such a sum.

*The largest power of \( 2 \) not above \( n \).* The set \( T \coloneqq \{ k \in \nN : 2^k > n \} \) is non-empty, since \( 2^n \ge 1 + n > n \) by @thm-bernoulli with \( x = 1 \). By @thm-well-ordering it has a least element \( m \) (the method of @exm-method-least-element). Since \( 2^0 = 1 \le n \), \( 0 \notin T \), so \( m \ge 1 \), and \( K \coloneqq m - 1 \in \nN \) (@lem-naturals-arithmetic (c)). As \( K < m \), \( K \notin T \); so
\[
2^K \le n < 2^{K+1} .
\]
*The step.* Let \( s \coloneqq n - 2^K \), so \( 0 \le s < 2^{K+1} - 2^K = 2^K \). If \( s = 0 \), then \( n = 2^K \), a sum with \( r = 1 \). If \( s \ge 1 \), then \( s < n \), because \( 2^K \ge 1 \). By the hypothesis, \( s = 2^{k_1} + \dots + 2^{k_r} \) with \( k_1 > \dots > k_r \). Each \( 2^{k_i} \le s < 2^K \), so \( k_i < K \) (if \( k_i \ge K \), then \( 2^{k_i} \ge 2^K \) by @prp-power-laws (e)). Hence
\[
n = 2^K + 2^{k_1} + \dots + 2^{k_r}, \qquad K > k_1 > \dots > k_r ,
\]
a sum of distinct powers of \( 2 \). By @thm-strong-induction-from-base, every \( n \ge 1 \) is such a sum. For example \( 13 = 2^3 + 2^2 + 2^0 \).

The base \( 1 \) is the right one: \( 0 \) is not a sum of one or more powers of \( 2 \), since each power is positive.
:::

::: {#exr-infinite-sets-r2}
[R2]

Show that \( \forall x\, \exists y\, R(x, y) \nvdash \exists y\, \forall x\, R(x, y) \) by a counter-model whose domain is \( \nN \). Say in words what the two sentences say when \( R(x, y) \) is read as "\( x < y \)".
:::

::: {.solution}
Let \( \fM \) have domain \( \nN \) and \( R^{\fM} \coloneqq \{ (d, e) \in \nN \times \nN : d < e \} \). Both formulas are sentences, so no assignment matters.

*The premise is true.* \( \forall x\, \exists y\, (x < y) \) says "every natural number has a larger one". For each \( d \in \nN \), \( e \coloneqq d + 1 \in \nN \) has \( d < e \).

*The conclusion is false.* \( \exists y\, \forall x\, (x < y) \) says "some natural number is larger than every natural number". For any \( e \in \nN \), the choice \( d \coloneqq e \) gives \( d < e \) false, so no \( e \) works.

So \( \fM \) is a counter-model, and \( \forall x\, \exists y\, R(x, y) \not\models \exists y\, \forall x\, R(x, y) \). By the soundness statement of *Logic and Proof*, Section 7.2 (the subsection "From counter-models to non-derivability"), a counter-model shows non-derivability: \( \forall x\, \exists y\, R(x, y) \nvdash \exists y\, \forall x\, R(x, y) \).

This is the converse of @fd1:prp-exists-forall-swap with the variables renamed and the two places of \( R \) exchanged (read \( R(x, y) \) as \( R(y, x) \)), and the counter-model is the one of @fd1:exm-counter-model-swap: there the domain was \( \nZ \) and \( R \) was read as \( > \); with the roles of the variables exchanged, \( R \) read as \( < \) and the domain cut down to \( \nN \), the same witnesses work, as checked above. In the premise the larger number \( y \) is chosen after \( x \) and depends on it; the conclusion asks for one \( y \) in advance.
:::

::: {#exr-infinite-sets-r3}
[R3]

For an integer \( n \ge 1 \), how many truth functions with \( n \) inputs are there? Prove your answer.
:::

::: {.solution}
There are \( 2^{2^n} \). A truth function with \( n \) inputs (@fd1:def-truth-function) assigns a truth value to each row \( (a_1, \dots, a_n) \); read a row as the function \( i \mapsto a_i \) on \( \{1, \dots, n\} \), and let \( L \) be the set of rows.

*There are \( 2^n \) rows.* The map sending a row to \( \{ i \in \{1, \dots, n\} : a_i = \mathrm{T} \} \) is a bijection \( L \to \powerset{\{1, \dots, n\}} \) (injective and surjective by @exm-method-injectivity and @exm-method-surjectivity): a row is determined by the places where it is \( \mathrm{T} \), and every set of places arises: given \( A \subseteq \{1, \dots, n\} \), the row with \( a_i = \mathrm{T} \) for \( i \in A \) and \( a_i = \mathrm{F} \) otherwise maps to \( A \), and two rows with the same \( \mathrm{T} \)-places agree at every \( i \), since each \( a_i \) is \( \mathrm{T} \) or \( \mathrm{F} \). Since \( \{1, \dots, n\} \) has \( n \) elements, @prp-power-set-count gives \( 2^n \) subsets, so \( L \) has \( 2^n \) elements (compose the bijections).

*There are \( 2^{2^n} \) truth functions.* In the same way, a truth function \( f \) is determined by the set \( \{ \rho \in L : f(\rho) = \mathrm{T} \} \subseteq L \), and every subset of \( L \) arises (the same two checks, with \( f \mapsto \{ \rho : f(\rho) = \mathrm{T} \} \) in place of the row map); so the truth functions are in bijection with \( \powerset{L} \), which has \( 2^{2^n} \) elements by @prp-power-set-count again. For \( n = 1, 2, 3 \) this gives \( 4, 16, 256 \).
:::

::: {#exr-infinite-sets-r4}
[R4]

A function \( f \colon \nN \to \nN \) is **eventually zero** if there is \( N \in \nN \) with \( f(n) = 0 \) for every \( n \ge N \). Is the set of eventually zero functions countable?
:::

::: {.solution}
*Yes.* The tool is a **countable union of countable sets**. For \( N \in \nN \) let \( Z_N \) be the set of \( f \colon \nN \to \nN \) with \( f(n) = 0 \) for every \( n \ge N \); the set of eventually zero functions is \( Z \coloneqq \bigcup_{N \in \nN} Z_N \). Each \( Z_N \) is countable:

- \( Z_0 \) has one element, the zero function, so it is countable.
- For \( N = 1 \), \( f \mapsto f(0) \) is a bijection \( Z_1 \to \nN \): a function in \( Z_1 \) is determined by its value at \( 0 \), and every value occurs.
- For \( N \ge 2 \), \( f \mapsto (f(0), \dots, f(N - 1)) \) is a bijection \( Z_N \to \nN \times \dots \times \nN \) (\( N \) factors), by the same reasoning and the characteristic property of tuples; the product is countable by @cor-product-countable, and so is \( Z_N \) (compose a surjection \( \nN \to \nN \times \dots \times \nN \) with the inverse bijection, @prp-countable-image).

By @thm-countable-union, \( Z \) is countable. (That theorem uses @ax-choice; here it could be avoided, since each \( Z_N \) comes with an explicit listing, but the question did not ask for that.)

*Why the look-alike fails.* A diagonal argument, as in @thm-binary-sequences-uncountable, builds from a list \( f_0, f_1, \dots \) of eventually zero functions the function \( g(n) \coloneqq f_n(n) + 1 \). It differs from every \( f_n \), but \( g(n) \ge 1 \) for every \( n \), so \( g \) is **not** eventually zero: it is not in \( Z \), and nothing is contradicted. A diagonal argument proves uncountability only when the diagonal object stays inside the set; this is the usual failure named in @exm-method-diagonal.
:::

<!-- dependency ledger
def-disjoint-union (claim): every element is (a, 0) or (b, 1), not both; inclusions injective with disjoint images | def-ordered-pair (cited); inline
exm-two-copies-of-naturals (solution): m = 2q + r uniquely, q in N, r in {0, 1} | the claim in the proof of prp-union-two-countable (cited)
prp-card-operations-well-defined (proof): (a) the two-part rule is a function; inverses undo it partwise | inline (unwinding after def-disjoint-union)
prp-card-operations-monotone (claim): (non-example) if A' is empty then A is empty, an injection into the empty set has empty domain | prp-empty-function (b), used silently
exm-pairing-bijection (solution): tau_(s+1) = tau_s + s + 1, tau_0 = 0, tau_s in N | def-sum-product (cited); lem-naturals-arithmetic (b) by induction on s, used silently
exm-pairing-bijection (solution): order and cancellation in N (tau_s + n <= tau_s + s < tau_(s+1); n = n' from tau_s + n = tau_s + n') | arithmetic and order of N (lem-naturals-arithmetic, school arithmetic of N)
exm-pairing-bijection (solution): the values pi(0,0)..pi(0,2), delta(11) = (3, 1); Quick check 3: pi(3,2) = 17, delta(47) = (7, 2) | verify/ch03/exm-pairing-bijection.py
thm-cardinal-laws (proof): a function on Y u Z may be defined on the two tagged parts separately | inline (unwinding after def-disjoint-union)
thm-cardinal-laws (claim): (fold) the maps of (a), (b), (c), (e) and their inverses | inline; prp-function-equality, def-ordered-pair (cited); verify/ch03/thm-cardinal-laws.py (finite instances)
thm-cardinal-laws (claim): (Quick check 4) 8 = 8 | inline count by listing values; verify/ch03/thm-cardinal-laws.py
thm-cardinal-laws (claim): (aftermath) the finite case gives back m^(n+k) = m^n m^k, (m^n)^k = m^(nk) | Section 2.5 counts (exr-finite-sets-c2, prose only; nothing depends on it)
thm-power-set-two-power (proof): f(x) is 0 or 1, so f(x) != 1 gives f(x) = 0 | the codomain {0, 1}
cor-cantor-two-power (proof): ind_{x} = ind_{y} gives x = y | inline (value 1 at x only)
thm-reals-power-set-naturals (proof): the expansion of x not ending in all 9s exists and is unique; one digit sequence names one number; y_b exists; two different expansions of one number, one ends in 9s | school facts (D1), (D2), (D3), stated in F2.3 §03 (def-decimal-expansion)
thm-reals-power-set-naturals (proof): (t, n) -> 10n + t bijection T x N -> N, decoder by division by 10 with quotient in N | thm-division-algorithm (cited), as in the claim in the proof of prp-union-two-countable; verify/ch03/exr-comparing-cardinalities-c1.py checks the same decoding
thm-reals-power-set-naturals (proof): y_b <= t_1 + 1/10 <= 2/10 | def-decimal-expansion (cited) at n = 1
thm-reals-power-set-naturals (claim): (remark) the continuum hypothesis is independent of the usual axioms, if consistent | set theory, stated without proof; nothing depends on it
exm-interleaving-decimals (solution): t_n <= (1 - 10^-(n-1)) + 8 * 10^-n; termwise comparison of finite sums | prp-geometric-sum (cited); induction on n via def-sum-product and the order of R; verify/ch03/exm-interleaving-decimals.py
exm-interleaving-decimals (solution): 0.090909... is an expansion of 1/11; t_(2j) = (1/11)(1 - 100^-j) | prp-geometric-sum (cited); verify/ch03/exm-interleaving-decimals.py
thm-plane-equinumerous-line (claim): (aftermath) the composite map is the interleaving of 3.4 B3 | inline (composite of Psi of thm-cardinal-laws (d) with the map of prp-card-operations-well-defined (c) along e)
cor-real-sequences (claim): (closing) |X x X| = |X| for all infinite X is equivalent to choice; |X u X| = |X| not provable without choice | set theory, stated without proof; nothing depends on it
exr-cardinal-arithmetic-a1 (solution): (d) first digit <= 8 gives y_b < 1 | def-decimal-expansion at n = 1
exr-cardinal-arithmetic-b1 (solution): division by 3 and by 2 with quotient in N; E(1, 0, 1) = 4 | thm-division-algorithm (cited); verify/ch03/exr-cardinal-arithmetic-b1.py
exr-cardinal-arithmetic-b4 (solution): finite counts 2 vs 4, 1 vs 0 functions; maps of (a) | inline listing; cor-finite-size-unique (cited); verify/ch03/exr-cardinal-arithmetic-b4.py
exr-cardinal-arithmetic-c2 (solution): eventually zero 0-1 sequences inject into R4's set by changing the codomain | exr-infinite-sets-r4 (an exercise, cited by an exercise)
exr-cardinal-arithmetic-c3 (solution): sigma_b is its own inverse; m = 2n or 2n + 1 uniquely | inline; exr-diagonal-arguments-c2 (an exercise, cited by an exercise); thm-division-algorithm as in prp-union-two-countable
exr-infinite-sets-r1 (solution): 2^(K+1) - 2^K = 2^K; 2^K >= 1 (a positive natural number) | def-power, prp-power-laws (d), (e), lem-naturals-arithmetic (a), used silently; verify/ch03/exr-infinite-sets-r1.py
exr-infinite-sets-r2 (solution): soundness for predicate logic (counter-model gives non-derivability) | F1.6 §02, subsection #from-counter-models-to-non-derivability (statement; proof in optional F1.6 §03); prose pointer, unlabelled statement
exr-infinite-sets-r3 (solution): row <-> set of T-places and truth function <-> set of T-rows are bijections; equinumerous with an n-element set has n elements | inline; prp-equinumerous-properties via composition; verify/ch03/exr-infinite-sets-r3.py
exr-infinite-sets-r4 (solution): Z_N -> N x ... x N (N factors) bijection, N >= 2 | characteristic property of tuples (F2.1 §04, def-ordered-pair)
-->
