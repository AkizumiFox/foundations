# Irreducible Polynomials and Unique Factorization

Over every field, \( x^4 - 1 = (x - 1)(x + 1)(x^2 + 1) \). Over \( \nQ \) the last factor cannot be split further; over \( \nF_5 \) it can, and \( x^4 - 1 \) becomes a product of four factors of degree \( 1 \); over \( \nF_2 \) all of them coincide, and \( x^4 - 1 = (x + 1)^4 \). So the "primes" of \( F[x] \) depend on the field \( F \). Once \( F \) is fixed, though, every polynomial of positive degree splits into such primes in essentially one way, as every positive integer does in *Number Systems: From \(\nN\) to \(\nR\)*, Section 3.3, and for the same reason: a prime that divides a product divides one of the factors.

Sections 4.1 and 4.2 supplied the tools: division with remainder (@thm-polynomial-division-remainder), the monic greatest common divisor and its Bézout identity (@thm-polynomial-bezout). This section spends them. Throughout, \( F \) is a field, and \( F[x] \) is a commutative ring with no zero divisors (@thm-polynomial-ring-laws (a), @cor-polynomial-no-zero-divisors); degrees of products add (@thm-degree-of-product (b)), and the units of \( F[x] \) are the non-zero constants (@prp-polynomial-divisibility-rules (e)).

## Irreducible polynomials

In \( \nZ \), a prime is a number \( p \ge 2 \) whose only positive divisors are \( 1 \) and \( p \). Two features of that definition need adjusting for polynomials. "Positive" has no meaning in \( F[x] \), and its job there was to ignore the units \( \pm 1 \); in \( F[x] \) the units are the non-zero constants, so we ignore those. And "\( p \ge 2 \)" kept the units themselves from counting as primes; in \( F[x] \) the condition becomes "degree at least \( 1 \)".

*An irreducible polynomial is one that cannot be split into two factors of smaller degree.*

::: {#def-irreducible-over-field}
[Irreducible Polynomial]

Let \( F \) be a field and \( p \in F[x] \). The polynomial \( p \) is **irreducible over \( F \)** if \( \deg p \ge 1 \) and, **whenever** \( p = gh \) with \( g, h \in F[x] \), **one** of \( g \), \( h \) is a constant. A polynomial of degree at least \( 1 \) that is not irreducible over \( F \) is **reducible over \( F \)**.
:::

In words: the first clause rules out \( 0 \) and the non-zero constants; the second says that every way of writing \( p \) as a product uses a constant factor. That constant is never \( 0 \), since \( p \ne 0 \). So \( p \) is reducible exactly when \( p = gh \) with \( \deg g \ge 1 \) and \( \deg h \ge 1 \); then \( \deg g + \deg h = \deg p \) (@thm-degree-of-product (b)), so both factors have degree **strictly** less than \( \deg p \).

**Examples.**

- Every polynomial of degree \( 1 \) is irreducible. If \( p = gh \) with \( \deg p = 1 \), the degrees of \( g \) and \( h \) are natural numbers adding up to \( 1 \), so one of them is \( 0 \).
- \( x^2 + x = x(x + 1) \) and \( x^3 = x \cdot x^2 \) are reducible over every field: each is a product of two factors of degree at least \( 1 \).
- \( x^2 + 1 \) is reducible over \( \nF_2 \), where \( (x + 1)^2 = x^2 + 2x + 1 = x^2 + 1 \) because \( 2 = 0 \). Over \( \nQ \) it is irreducible, as the next proposition shows. The polynomial is the same; the field changed, and with it the answer. This is why the definition says "over \( F \)".
- If \( p \) is irreducible and \( a \in F \) is non-zero, then \( ap \) is irreducible. First, \( \deg(ap) = \deg p \ge 1 \) (@thm-degree-of-product (b)), and a factorization \( ap = gh \) gives \( p = (a^{-1}g)h \), so \( a^{-1}g \) or \( h \) is a constant, and then so is \( g \) or \( h \). Associates of irreducibles are irreducible.

::: {.second-reading title="The degenerate cases: constants"}
The constants are kept out by the first clause, and each for a reason. Without it, the polynomial \( 0 \) would pass the second clause, since every factorization \( 0 = gh \) has \( g = 0 \) or \( h = 0 \) (@cor-polynomial-no-zero-divisors), a constant. But every polynomial divides \( 0 \) (@prp-polynomial-divisibility-rules (a)), so \( 0 \) behaves like the integer \( 0 \), not like a prime. A non-zero constant \( a \) is a unit: it divides everything, and every factorization \( a = gh \) has two constant factors, since the degrees add up to \( 0 \). If units counted as irreducible, every factorization could be padded with as many of them as we like, just as \( (1, 2, 2, 3, 5) \) would pad the factorization of \( 60 \) if \( 1 \) were prime. The clause \( \deg p \ge 1 \) plays the part of the integer condition \( p \ge 2 \).
:::

For polynomials of degree \( 2 \) and \( 3 \), irreducibility can be decided by looking for roots.

::: {#prp-irreducible-low-degree}
[Irreducibility in Low Degree]

Let \( F \) be a field and \( p \in F[x] \).

::: {.enumerate options="label=(\alph*)"}
1. If \( \deg p \ge 2 \) and \( p \) has a root in \( F \), then \( p \) is reducible over \( F \).
2. If \( \deg p \in \{2, 3\} \), then \( p \) is irreducible over \( F \) **if and only if** \( p \) has no root in \( F \).
:::
:::

::: {.proof}
*(a)* Let \( c \in F \) be a root of \( p \). By @thm-polynomial-remainder-factor (b), \( p = (x - c)q \) for some \( q \in F[x] \). Then \( \deg q = \deg p - 1 \ge 1 \) by @thm-degree-of-product (b), and \( \deg(x - c) = 1 \), so neither factor is a constant and \( p \) is reducible.

*(b)* \( (\Rightarrow) \) is (a), read contrapositively. \( (\Leftarrow) \) Suppose \( p \) is reducible, so \( p = gh \) with \( \deg g, \deg h \ge 1 \) and \( \deg g + \deg h = \deg p \in \{2, 3\} \). Two natural numbers, each at least \( 1 \), with sum \( 2 \) or \( 3 \): one of them is \( 1 \). So \( p \) has a factor of degree \( 1 \), and @thm-polynomial-remainder-factor (c) gives a root of \( p \) in \( F \).
:::

For \( x^2 + 1 \) over \( \nQ \): for every \( c \in \nQ \), \( c^2 \ge 0 \) (@fd3:prp-ordered-ring-rules (e), with \( 0^2 = 0 \)), so \( c^2 + 1 \ge 1 > 0 \) by (b) and (e) of the same proposition. There is no rational root, and (b) makes \( x^2 + 1 \) irreducible over \( \nQ \). The same lines work in every ordered field, so \( x^2 + 1 \) is irreducible over \( \nR \) as well.

::: {.warning}
**"No root" does not mean "irreducible" in degree \( 4 \) and above.** For \( c \in \nQ \), \( c^4 = (c^2)^2 \ge 0 \), so \( c^4 + 4 \ge 4 > 0 \) (@fd3:prp-ordered-ring-rules (h)): the polynomial \( x^4 + 4 \) has no rational root. Yet
\[
x^4 + 4 = (x^2 + 2x + 2)(x^2 - 2x + 2) ,
\]
as expanding the right side shows: the terms in \( x^3 \), \( x^2 \) and \( x \) cancel. Proposition @prp-irreducible-low-degree (b) is about degrees \( 2 \) and \( 3 \) only, where every splitting must contain a factor of degree \( 1 \); in degree \( 4 \) a splitting may be \( 2 + 2 \), with no factor of degree \( 1 \) and so no root.
:::

::: {.check}
Is \( 2x^2 + 4 \) irreducible over \( \nQ \)? Is \( x^2 + 2 \) irreducible over \( \nF_3 \)?
:::

::: {.solution}
Over \( \nQ \), yes: \( 2x^2 + 4 = 2(x^2 + 2) \), and \( x^2 + 2 \) has no rational root (\( c^2 + 2 \ge 2 > 0 \), @fd3:prp-ordered-ring-rules (e), (h)), so it is irreducible by @prp-irreducible-low-degree (b), and so is its associate \( 2x^2 + 4 \). The factor \( 2 \) is a constant, so \( 2 \cdot (x^2 + 2) \) is not a splitting into non-constants. Over \( \nF_3 \), no: \( 1^2 + 2 = 3 = 0 \), so \( 1 \) is a root, and indeed \( x^2 + 2 = x^2 - 1 = (x - 1)(x + 1) \) in \( \nF_3 \).
:::

## Euclid's lemma for polynomials

The definition of an irreducible \( p \) speaks about the factors **of** \( p \). Unique factorization needs a statement about the polynomials that \( p \) **divides**. As in \( \nZ \), the bridge is the Bézout identity, and the move is the one of *Number Systems: From \(\nN\) to \(\nR\)*, Section 3.3: **multiply the Bézout identity**.

::: {#thm-polynomial-euclid-lemma}
[Euclid's Lemma for Polynomials]

Let \( F \) be a field and \( f, g, h \in F[x] \). If \( f \mid gh \) and \( \gcd(f, g) = 1 \), then \( f \mid h \).
:::

::: {.proof}
Since \( \gcd(f, g) = 1 \), @cor-polynomial-coprime-iff-combination gives \( a, b \in F[x] \) with \( af + bg = 1 \). Multiplying by \( h \),
\[
h = h(af + bg) = (ah)f + b(gh) .
\]
Now \( f \mid f \) and \( f \mid gh \), so \( f \) divides the combination \( (ah)f + b(gh) \) (@prp-polynomial-divisibility-rules (c)). Hence \( f \mid h \).
:::

The hypothesis \( \gcd(f, g) = 1 \) is needed. In \( \nQ[x] \), \( x^2 \mid x \cdot x \), but \( x^2 \nmid x \), since a divisor of a non-zero polynomial has degree at most its degree (@prp-polynomial-divisibility-rules (d)); here \( \gcd(x^2, x) = x \).

For an irreducible \( p \), the coprimality comes almost free, exactly as it did for a prime number.

::: {#cor-irreducible-divides-product}
[An Irreducible Dividing a Product]

Let \( F \) be a field and \( p \in F[x] \) irreducible over \( F \).

::: {.enumerate options="label=(\alph*)"}
1. For every \( f \in F[x] \): \( p \mid f \) or \( \gcd(p, f) = 1 \).
2. For all \( g, h \in F[x] \): if \( p \mid gh \), then \( p \mid g \) or \( p \mid h \).
3. If \( (q_1, \dots, q_l) \) is a list of polynomials in \( F[x] \), with \( l \in \nN \), and \( p \mid q_1 q_2 \cdots q_l \), then \( l \ge 1 \) and \( p \mid q_j \) for some \( j \in \{1, \dots, l\} \).
4. If \( p \) and \( q \) are monic and irreducible over \( F \) and \( p \mid q \), then \( p = q \).
:::
:::

Here \( q_1 q_2 \cdots q_l \), also written \( \prod_{j=1}^{l} q_j \), is the product of a finite list in the commutative ring \( F[x] \), given by the recursion of @fd2:def-sum-product as @lem-finite-sums-and-powers (a) reads it: the empty product is \( 1 \), and \( \prod_{j=1}^{l+1} q_j = \bigl(\prod_{j=1}^{l} q_j\bigr) q_{l+1} \).

::: {.idea}
For (a), the gcd of \( p \) and \( f \) is a monic divisor of \( p \), and an irreducible \( p \) has only two kinds of divisors: constants and associates of itself. Part (b) is Euclid's lemma in the coprime case of (a). For (c), peel the last factor off the product and apply (b); induction on the length does the rest. For (d), the cofactor of \( p \) in \( q \) must be a constant, and comparing leading coefficients makes it \( 1 \).
:::

::: {.proof}
*(a)* Since \( p \ne 0 \), the gcd \( d \coloneqq \gcd(p, f) \) is monic (@def-polynomial-gcd, @thm-polynomial-bezout (c)). It divides \( p \): write \( p = du \) with \( u \in F[x] \). As \( p \) is irreducible, \( d \) or \( u \) is a constant. If \( d \) is a constant, it is a monic constant, so \( d = 1 \). If \( u \) is a constant, then \( u \ne 0 \) (as \( p \ne 0 \)) and \( d = u^{-1}p \); since \( d \mid f \), \( f = dk = p(u^{-1}k) \) for some \( k \in F[x] \), so \( p \mid f \).

*(b)* Let \( p \mid gh \). By (a), \( p \mid g \) or \( \gcd(p, g) = 1 \), and in the second case @thm-polynomial-euclid-lemma gives \( p \mid h \).

*(c)* By @fd1:ax-induction (on \( \nN = \omega \), @fd3:cor-omega-identification (b)) we prove, for every \( l \in \nN \), the statement \( P(l) \): "for every list \( (q_1, \dots, q_l) \) in \( F[x] \) with \( p \mid \prod_{j=1}^{l} q_j \), we have \( l \ge 1 \) and \( p \mid q_j \) for some \( j \le l \)".

*Base case \( P(0) \).* The empty product is \( 1 \), and \( p \nmid 1 \): otherwise \( \deg p \le \deg 1 = 0 \) by @prp-polynomial-divisibility-rules (d), against \( \deg p \ge 1 \). So the hypothesis of \( P(0) \) never holds, and \( P(0) \) is true.

*Step.* Assume \( P(l) \), and let \( p \mid \prod_{j=1}^{l+1} q_j = \bigl(\prod_{j=1}^{l} q_j\bigr) q_{l+1} \). By (b), \( p \) divides the first factor or \( p \mid q_{l+1} \). In the first case \( P(l) \) gives \( j \le l \) with \( p \mid q_j \); in the second, take \( j = l + 1 \). Either way \( l + 1 \ge 1 \), and \( P(l + 1) \) holds.

*(d)* Write \( q = pu \) with \( u \in F[x] \). As \( q \) is irreducible, \( p \) or \( u \) is a constant, and \( p \) is not, since \( \deg p \ge 1 \). So \( u \) is a non-zero constant, and comparing leading coefficients (@thm-degree-of-product (b)) gives \( 1 = 1 \cdot u \). Hence \( u = 1 \) and \( p = q \).
:::

Part (b) fails for reducible polynomials: \( x^2 \mid x \cdot x \) with \( x^2 \nmid x \). Part (d) needs "monic": \( x \) and \( 2x \) are irreducible over \( \nQ \), and each divides the other.

The same multiplication of a Bézout identity combines two coprime divisors.

::: {#prp-polynomial-coprime-divisors-product}
[Coprime Divisors of a Polynomial]

Let \( F \) be a field and \( m, n, h \in F[x] \) with \( m \mid h \), \( n \mid h \) and \( \gcd(m, n) = 1 \). Then \( mn \mid h \).
:::

::: {.proof}
Write \( h = mk \) with \( k \in F[x] \). Then \( n \mid mk \), and \( \gcd(n, m) = \gcd(m, n) = 1 \), since the clauses of @def-polynomial-gcd do not depend on the order of the two polynomials. By @thm-polynomial-euclid-lemma, \( n \mid k \); say \( k = nt \). Then \( h = m(nt) = (mn)t \), so \( mn \mid h \).
:::

Without coprimality the conclusion fails: \( x \mid x \) twice over, yet \( x \cdot x = x^2 \nmid x \).

::: {.check}
In \( \nF_2[x] \), the polynomial \( x^2 + 1 \) divides \( (x + 1)(x + 1) \), but divides neither factor. Does this contradict @cor-irreducible-divides-product (b)?
:::

::: {.solution}
No. In \( \nF_2[x] \), \( (x + 1)(x + 1) = x^2 + 1 \), so \( x^2 + 1 \) is reducible over \( \nF_2 \), and the corollary says nothing about it. (It divides neither factor because each factor has degree \( 1 < 2 \), @prp-polynomial-divisibility-rules (d).)
:::

## Factors that cannot be split further

The existence half of unique factorization needs a supply of irreducibles: every polynomial of positive degree must have an irreducible factor. In \( \nZ \), the least divisor at least \( 2 \) was prime (@fd3:lem-least-divisor-prime). For polynomials, size becomes degree, and the "least divisor" becomes a monic divisor of least positive degree.

::: {#lem-polynomial-irreducible-factor}
[An Irreducible Factor Exists]

Let \( F \) be a field and \( f \in F[x] \) with \( \deg f \ge 1 \). Then \( f \) has a **monic** irreducible divisor in \( F[x] \).
:::

::: {.idea}
Among the monic divisors of positive degree, take one of least degree. A splitting of it into two non-constants would produce a monic divisor of smaller positive degree.
:::

::: {.proof}
Let \( c \) be the leading coefficient of \( f \), and let
\[
D \coloneqq \{ \deg d : d \in F[x] \text{ monic}, \ \deg d \ge 1, \ d \mid f \} \subseteq \nN .
\]
The monic associate \( c^{-1}f \) has degree \( \deg f \ge 1 \) and divides \( f = c \cdot (c^{-1}f) \), so \( D \) is non-empty. By @fd2:thm-well-ordering (on \( \nN = \omega \) it is @fd3:thm-omega-well-ordering), \( D \) has a least element \( n_0 \); let \( p \) be a monic divisor of \( f \) of degree \( n_0 \). Then \( \deg p = n_0 \ge 1 \).

Suppose \( p = gh \) with \( \deg g \ge 1 \) and \( \deg h \ge 1 \). Then \( \deg g = n_0 - \deg h < n_0 \) (@thm-degree-of-product (b)). Let \( g_1 \) be the monic associate of \( g \), so \( g = \operatorname{lc}(g)\, g_1 \) and \( \deg g_1 = \deg g \). Then \( g_1 \mid g \), \( g \mid p \) and \( p \mid f \), so \( g_1 \mid f \) (@prp-polynomial-divisibility-rules (b)), and \( \deg g_1 \in D \) is smaller than \( n_0 \), against the choice of \( n_0 \). So every factorization \( p = gh \) has a constant factor, and \( p \) is irreducible.
:::

This is @fd3:lem-least-divisor-prime with degree in place of size; the twin is compared with, not used.

## Unique factorization

**Two facts about products of lists.** The proof below handles lists of polynomials, and it uses two facts about their products, both proved by induction on the length from the recursion of the product. Let \( (q_1, \dots, q_l) \) be a list in \( F[x] \), with \( l \in \nN \).

::: {.enumerate options="label=(L\arabic*)"}
1. If every \( q_j \) is non-zero, then \( \prod_{j=1}^{l} q_j \ne 0 \), and its degree is \( \sum_{j=1}^{l} \deg q_j \). If every \( q_j \) is monic, so is the product.
2. If \( l \ge 1 \) and \( j \in \{1, \dots, l\} \), let \( (q'_1, \dots, q'_{l-1}) \) be the list with the entry \( j \) removed: \( q'_t \coloneqq q_t \) for \( t < j \) and \( q'_t \coloneqq q_{t+1} \) for \( j \le t \le l - 1 \). Then \( \prod_{t=1}^{l} q_t = \bigl(\prod_{t=1}^{l-1} q'_t\bigr) q_j \). In particular every entry of a list divides its product.
:::

The names (L1), (L2) are used throughout this chapter.

::: {.second-reading title="Proofs of (L1) and (L2)"}
*(L1).* Induction on \( l \). For \( l = 0 \) the product is \( 1 \), which is monic of degree \( 0 \), the empty sum. If the claim holds for \( l \), then \( \prod_{j=1}^{l+1} q_j = \bigl(\prod_{j=1}^{l} q_j\bigr) q_{l+1} \) is a product of two non-zero polynomials, so it is non-zero with degree \( \sum_{j=1}^{l} \deg q_j + \deg q_{l+1} \) and leading coefficient the product of the two leading coefficients (@thm-degree-of-product (b)); that is \( 1 \cdot 1 = 1 \) when both factors are monic.

*(L2).* Induction on \( l \ge 1 \), for all \( j \le l \) at once. For \( l = 1 \), \( j = 1 \), the shortened list is empty and both sides are \( q_1 \). Suppose the claim holds for lists of length \( l \), and let \( (q_1, \dots, q_{l+1}) \) and \( j \le l + 1 \) be given. If \( j = l + 1 \), the shortened list is \( (q_1, \dots, q_l) \) and the claim is the recursion itself. If \( j \le l \), the claim for the list \( (q_1, \dots, q_l) \) and the same \( j \) gives \( \prod_{t=1}^{l} q_t = \bigl(\prod_{t=1}^{l-1} r_t\bigr) q_j \), where \( (r_1, \dots, r_{l-1}) \) is \( (q_1, \dots, q_l) \) with entry \( j \) removed. The list \( (q'_1, \dots, q'_l) \) obtained from \( (q_1, \dots, q_{l+1}) \) has the first \( l - 1 \) entries \( r_1, \dots, r_{l-1} \) and the last entry \( q'_l = q_{l+1} \). So, by the recursion twice and commutativity and associativity in \( F[x] \),
\[
\begin{aligned}
\prod_{t=1}^{l+1} q_t &= \Bigl(\prod_{t=1}^{l-1} r_t\Bigr) q_j \, q_{l+1} \\
&= \Bigl(\Bigl(\prod_{t=1}^{l-1} r_t\Bigr) q_{l+1}\Bigr) q_j = \Bigl(\prod_{t=1}^{l} q'_t\Bigr) q_j .
\end{aligned}
\]
The last clause of (L2) follows: \( q_j \) divides \( \bigl(\prod_{t} q'_t\bigr) q_j \).
:::

Everything is now in place.

::: {#thm-polynomial-unique-factorization}
[Unique Factorization of Polynomials]

Let \( F \) be a field and \( f \in F[x] \) with \( \deg f \ge 1 \) and leading coefficient \( c \).

::: {.enumerate options="label=(\alph*)"}
1. **Existence.** There are \( k \ge 1 \) and monic polynomials \( p_1, \dots, p_k \), irreducible over \( F \), with \( f = c \, p_1 p_2 \cdots p_k \).
2. **Uniqueness.** If also \( f = c' q_1 q_2 \cdots q_l \) with \( c' \in F \), \( l \in \nN \) and monic polynomials \( q_1, \dots, q_l \) irreducible over \( F \), then \( c' = c \), \( l = k \), and there is a bijection \( \sigma \colon \{1, \dots, k\} \to \{1, \dots, l\} \) (@fd2:def-bijective) with \( q_{\sigma(i)} = p_i \) for every \( i \).
:::
:::

In words: every polynomial of positive degree is its leading coefficient times a product of monic irreducibles, and the leading coefficient and the irreducibles, counted with repetition, are determined by \( f \); only their order is free. The bijection \( \sigma \) says "the same list, possibly in another order": it matches each \( p_i \) with an equal \( q_{\sigma(i)} \), and each \( q \) is used exactly once.

::: {.idea}
*Existence.* Split off one monic irreducible factor (@lem-polynomial-irreducible-factor); the cofactor has smaller degree, so strong induction on the degree factors it.

*Uniqueness.* Divide by the leading coefficient, so that both products are equal products of monic irreducibles. The last factor \( p_{k+1} \) of one list divides the other product, so by Euclid's lemma (in the form @cor-irreducible-divides-product (c)) it divides one of the \( q_j \), and, both being monic and irreducible, it **equals** it. Cancel it from both sides and use induction on the length.

*Before reading on: where is Euclid's lemma used, and why does "monic" turn "\( p_{k+1} \) is a constant times \( q_j \)" into "\( p_{k+1} = q_j \)"?*
:::

::: {.proof}
*Existence.* We prove, by @fd1:thm-strong-induction on \( n \in \nN \) (read on \( \omega \): its proof uses only @fd1:ax-induction and @fd3:thm-omega-order (a), (b), (d), as in Section 2.1), the statement \( E(n) \): "every **monic** \( g \in F[x] \) of degree \( n \ge 1 \) is a product \( p_1 \cdots p_k \) of a list of monic irreducibles, \( k \ge 1 \)". For \( n = 0 \) there is nothing to prove. Let \( n \ge 1 \), assume \( E(m) \) for every \( m < n \), and let \( g \) be monic of degree \( n \). By @lem-polynomial-irreducible-factor, \( g = pu \) with \( p \) monic and irreducible, and \( u \in F[x] \). Comparing leading coefficients (@thm-degree-of-product (b)), \( 1 = 1 \cdot \operatorname{lc}(u) \), so \( u \) is monic, and \( \deg u = n - \deg p < n \). If \( \deg u = 0 \), then \( u = 1 \) and \( g = p \) is a list of length \( 1 \). Otherwise \( E(\deg u) \) gives \( u = p_1 \cdots p_r \) with monic irreducibles \( p_i \), and the list \( (p_1, \dots, p_r, p) \) has, by the recursion, the product \( \bigl(\prod_{i=1}^{r} p_i\bigr) p = up = g \). This proves \( E(n) \).

Now let \( f \) be as in the theorem. Its monic associate \( c^{-1}f \) has degree \( \deg f \ge 1 \), so \( c^{-1}f = p_1 \cdots p_k \) by \( E(\deg f) \), and \( f = c \, p_1 \cdots p_k \).

*Uniqueness.* By (L1), \( q_1 \cdots q_l \) is monic. As \( f \ne 0 \), \( c' \ne 0 \), and comparing leading coefficients in \( f = c' q_1 \cdots q_l \) (@thm-degree-of-product (b)) gives \( c = c' \cdot 1 = c' \). Multiplying both expressions for \( f \) by \( c^{-1} \),
\[
p_1 p_2 \cdots p_k = q_1 q_2 \cdots q_l .
\]
It remains to prove, by @fd1:ax-induction on \( k \in \nN \), the statement \( U(k) \): "for every \( l \in \nN \), if \( (p_1, \dots, p_k) \) and \( (q_1, \dots, q_l) \) are lists of monic irreducibles with \( \prod_{i=1}^{k} p_i = \prod_{j=1}^{l} q_j \), then \( l = k \) and there is a bijection \( \sigma \colon \{1, \dots, k\} \to \{1, \dots, l\} \) with \( q_{\sigma(i)} = p_i \) for every \( i \le k \)".

*Base case \( U(0) \).* The empty product is \( 1 \), of degree \( 0 \). By (L1), \( \prod_{j=1}^{l} q_j \) has degree \( \sum_{j} \deg q_j \ge l \), since each \( \deg q_j \ge 1 \). So \( l = 0 \), and the empty function \( \emptyset \to \emptyset \) is the required bijection.

*Step.* Assume \( U(k) \), and let \( (p_1, \dots, p_{k+1}) \) and \( (q_1, \dots, q_l) \) be lists of monic irreducibles with the same product \( N \). By the recursion, \( N = \bigl(\prod_{i=1}^{k} p_i\bigr) p_{k+1} \), so \( p_{k+1} \mid N = \prod_{j=1}^{l} q_j \). By @cor-irreducible-divides-product (c), \( l \ge 1 \) and \( p_{k+1} \mid q_j \) for some \( j \le l \); by @cor-irreducible-divides-product (d), \( p_{k+1} = q_j \). Let \( (q'_1, \dots, q'_{l-1}) \) be the \( q \)-list with entry \( j \) removed. By (L2),
\[
\Bigl(\prod_{i=1}^{k} p_i\Bigr) p_{k+1} = N = \Bigl(\prod_{t=1}^{l-1} q'_t\Bigr) q_j = \Bigl(\prod_{t=1}^{l-1} q'_t\Bigr) p_{k+1} .
\]
Since \( p_{k+1} \ne 0 \), we may cancel it (@cor-polynomial-no-zero-divisors (b)): \( \prod_{i=1}^{k} p_i = \prod_{t=1}^{l-1} q'_t \). The list \( (q'_1, \dots, q'_{l-1}) \) consists of monic irreducibles, so \( U(k) \), applied with \( l - 1 \in \nN \), gives \( l - 1 = k \) and a bijection \( \sigma' \colon \{1, \dots, k\} \to \{1, \dots, l - 1\} \) with \( q'_{\sigma'(i)} = p_i \).

Let \( \tau \colon \{1, \dots, l - 1\} \to \{1, \dots, l\} \setminus \{j\} \) be \( \tau(t) \coloneqq t \) for \( t < j \) and \( \tau(t) \coloneqq t + 1 \) for \( t \ge j \). It is a bijection (its inverse sends \( s < j \) to \( s \) and \( s > j \) to \( s - 1 \)), and \( q'_t = q_{\tau(t)} \) by the definition of \( q' \). Define \( \sigma \colon \{1, \dots, k + 1\} \to \{1, \dots, l\} \) by \( \sigma(i) \coloneqq \tau(\sigma'(i)) \) for \( i \le k \) and \( \sigma(k + 1) \coloneqq j \). On \( \{1, \dots, k\} \), \( \sigma \) is a bijection onto \( \{1, \dots, l\} \setminus \{j\} \), a composite of two bijections; and it sends \( k + 1 \) to the one remaining point \( j \). So \( \sigma \) is injective and surjective, a bijection. Finally \( q_{\sigma(i)} = q_{\tau(\sigma'(i))} = q'_{\sigma'(i)} = p_i \) for \( i \le k \), and \( q_{\sigma(k+1)} = q_j = p_{k+1} \); and \( l = k + 1 \). This proves \( U(k + 1) \), and the theorem.
:::

The answer to the prompt. Euclid's lemma enters at one line, "\( p_{k+1} \mid q_j \) for some \( j \)": that is @cor-irreducible-divides-product (c), whose step is (b), which is @thm-polynomial-euclid-lemma in the coprime case. "Monic" enters twice. Irreducibility of \( q_j \) only gives \( q_j = p_{k+1} u \) with \( u \) a non-zero constant; both being monic forces \( u = 1 \) (part (d)), and without that the cancellation would leave a stray constant \( u \) on one side. And the leading coefficients \( c, c' \) can be compared only because the products of monic lists are monic.

::: {.remark}
In \( \nZ \), *Number Systems: From \(\nN\) to \(\nR\)*, Section 3.3 stated uniqueness for **non-decreasing** lists of primes (@fd3:thm-fundamental-arithmetic), so that two factorizations of the same number are literally equal. Polynomials have no natural order to sort by, so here "the same up to order" is said with a bijection of indices.
:::

::: {#exm-factor-x4-minus-one-fields}
[The Factorizations of \( x^4 - 1 \)]

Factor \( x^4 - 1 \) into monic irreducibles over \( \nQ \), over \( \nR \), over \( \nF_3 \), over \( \nF_5 \) and over \( \nF_2 \).
:::

::: {.solution}
Over every field, \( (x - 1)(x + 1) = x^2 - 1 \) and \( (x^2 - 1)(x^2 + 1) = x^4 - 1 \), by expanding, so
\[
x^4 - 1 = (x - 1)(x + 1)(x^2 + 1) .
\]
The two factors of degree \( 1 \) are irreducible. Everything depends on \( x^2 + 1 \), which by @prp-irreducible-low-degree (b) is irreducible exactly when it has no root in the field.

- **\( \nQ \) and \( \nR \).** No root, since \( c^2 + 1 \ge 1 > 0 \) in an ordered field (after @prp-irreducible-low-degree). So \( (x - 1, x + 1, x^2 + 1) \) is the factorization, with leading coefficient \( 1 \).
- **\( \nF_3 \).** The values of \( x^2 + 1 \) at \( 0, 1, 2 \) are \( 1, 2, 5 = 2 \): no root. The factorization is \( (x - 1, x + 1, x^2 + 1) \) again, with \( x + 1 = x - 2 \).
- **\( \nF_5 \).** Here \( 2^2 + 1 = 5 = 0 \), and indeed \( (x - 2)(x - 3) = x^2 - 5x + 6 = x^2 + 1 \) in \( \nF_5 \). So \( x^4 - 1 = (x - 1)(x - 2)(x - 3)(x - 4) \), using \( x + 1 = x - 4 \): four factors of degree \( 1 \).
- **\( \nF_2 \).** Here \( -1 = 1 \), so \( x - 1 = x + 1 \), and \( x^2 + 1 = (x + 1)^2 \) (the example after @def-irreducible-over-field). So \( x^4 - 1 = (x + 1)^4 \): one irreducible, four times.

By @thm-polynomial-unique-factorization, each of these lists is the only one up to order.
:::

::: {.check}
Is \( x^2 + x + 1 \) irreducible over \( \nF_2 \)? Over \( \nF_3 \)?
:::

::: {.solution}
Over \( \nF_2 \), its values at \( 0 \) and \( 1 \) are \( 1 \) and \( 3 = 1 \): no root, so it is irreducible (@prp-irreducible-low-degree (b)). Over \( \nF_3 \), \( 1 + 1 + 1 = 3 = 0 \), so \( 1 \) is a root and it is reducible; indeed \( (x - 1)^2 = x^2 - 2x + 1 = x^2 + x + 1 \) in \( \nF_3 \).
:::

## Rational roots

Over \( \nQ \), the low-degree test of @prp-irreducible-low-degree asks for rational roots, and there are infinitely many rationals to try. For a polynomial with integer coefficients and non-zero constant term the candidates can be listed (a zero constant term is dealt with by factoring out a power of \( x \), below). The proof is about integers, not polynomials: here, unlike in the rest of this section, integer results of *Number Systems: From \(\nN\) to \(\nR\)*, Chapter 3 (Euclid's lemma, lowest terms) are steps of the proof and not only compared with.

::: {#thm-rational-root-test}
[Rational Root Test]

Let \( n \ge 1 \), let \( a_0, a_1, \dots, a_n \in \nZ \) with \( a_n \ne 0 \), and let \( f \coloneqq \sum_{i=0}^{n} a_i x^i \in \nQ[x] \). If \( u \in \nZ \), \( v \in \nZ_{>0} \), \( \gcd(u, v) = 1 \) and \( f(u/v) = 0 \), then \( u \mid a_0 \) and \( v \mid a_n \) in \( \nZ \).
:::

::: {.idea}
Clear denominators: \( v^n f(u/v) = 0 \) is an equation in \( \nZ \) in which every term but one is a multiple of \( u \), and every term but another is a multiple of \( v \). Then Euclid's lemma for integers strips the powers of \( v \) from \( a_0 v^n \), one at a time.
:::

::: {.proof}
Multiply \( f(u/v) = 0 \) by \( v^n \). For \( i \le n \), \( (u/v)^i v^i = u^i \) and \( v^n = v^{n-i} v^i \) (@lem-finite-sums-and-powers (c), in the commutative ring \( \nQ \)), so
\[
a_n u^n + a_{n-1} u^{n-1} v + \dots + a_1 u v^{n-1} + a_0 v^n = 0 ,
\]
an equation between integers. Every term except the last contains the factor \( u \), and every term except the first contains the factor \( v \) (as \( n \ge 1 \)). So
\[
a_0 v^n = -u \sum_{i=1}^{n} a_i u^{i-1} v^{n-i} , \qquad a_n u^n = -v \sum_{i=0}^{n-1} a_i u^i v^{n-1-i} ,
\]
and \( u \mid a_0 v^n \), \( v \mid a_n u^n \) in \( \nZ \).

We show \( u \mid a_0 v^{n-j} \) for every \( j \le n \), by @fd1:ax-induction on \( j \). The case \( j = 0 \) is the line above. If \( u \mid a_0 v^{n-j} \) with \( j < n \), then \( a_0 v^{n-j} = v \cdot (a_0 v^{n-j-1}) \), and \( \gcd(u, v) = 1 \), so @fd3:thm-euclid-lemma-integers gives \( u \mid a_0 v^{n-(j+1)} \). At \( j = n \): \( u \mid a_0 \). The same induction with the roles of \( u \) and \( v \) exchanged (and \( \gcd(v, u) = \gcd(u, v) = 1 \)) turns \( v \mid a_n u^n \) into \( v \mid a_n \).
:::

Every rational root has such a form: by @fd3:prp-rationals-lowest-terms, each \( r \in \nQ \) is \( u/v \) with \( u \in \nZ \), \( v \in \nZ_{>0} \) and \( \gcd(u, v) = 1 \). So, when \( a_0 \ne 0 \), the rational roots of \( f \) are among the finitely many fractions \( u/v \) with \( u \mid a_0 \) and \( v \) a positive divisor of \( a_n \): a divisor \( u \) of \( a_0 \ne 0 \) has \( -|a_0| \le u \le |a_0| \), by @fd3:prp-divisibility-rules-integers (d), (e), and likewise \( 1 \le v \le |a_n| \). If \( a_0 = 0 \), then \( 0 \) is a root; let \( k \) be the least index with \( a_k \ne 0 \) (so \( k \le n \)). Then \( f = x^k g \) with \( g \coloneqq \sum_{i=0}^{n-k} a_{i+k} x^i \), which has integer coefficients and constant term \( a_k \ne 0 \), and the non-zero rational roots of \( f \) are those of \( g \), since \( f(r) = r^k g(r) \) (@thm-evaluation-respects-operations) and \( \nQ \) has no zero divisors; apply the test to \( g \) when \( \deg g \ge 1 \), and when \( \deg g = 0 \), \( g \) has no root. The test lists candidates; it does not say which of them are roots.

::: {#exm-cubic-no-rational-root}
[A Cubic with No Rational Root]

Show that \( 3x^3 + x^2 - 2 \) is irreducible over \( \nQ \).
:::

::: {.solution}
By @thm-rational-root-test, a rational root \( u/v \) in lowest terms has \( u \mid -2 \) and \( v \) a positive divisor of \( 3 \). The divisors of \( -2 \) are \( \pm 1, \pm 2 \), and the positive divisors of \( 3 \) are \( 1, 3 \) (a positive divisor of \( 3 \) is at most \( 3 \), @fd3:prp-divisibility-rules-integers (e), and \( 3 = 1 \cdot 2 + 1 \)). So the candidates are \( \pm 1, \pm 2, \pm 1/3, \pm 2/3 \). The values of \( f \coloneqq 3x^3 + x^2 - 2 \) at them are

| \( c \) | \( 1 \) | \( -1 \) | \( 2 \) | \( -2 \) | \( 1/3 \) | \( -1/3 \) | \( 2/3 \) | \( -2/3 \) |
|---|---|---|---|---|---|---|---|---|
| \( f(c) \) | \( 2 \) | \( -4 \) | \( 26 \) | \( -22 \) | \( -16/9 \) | \( -2 \) | \( -2/3 \) | \( -22/9 \) |

For instance \( f(2/3) = 3 \cdot \tfrac{8}{27} + \tfrac{4}{9} - 2 = \tfrac{8}{9} + \tfrac{4}{9} - 2 = -\tfrac{2}{3} \). None is \( 0 \), so \( f \) has no rational root, and as \( \deg f = 3 \), @prp-irreducible-low-degree (b) makes \( f \) irreducible over \( \nQ \).
:::

::: {.check}
Which rational numbers can be roots of \( 2x^2 + 3x - 2 \)? Which are?
:::

::: {.solution}
The candidates are \( u/v \) with \( u \mid -2 \) and \( v \in \{1, 2\} \): \( \pm 1, \pm 2, \pm 1/2 \). Evaluating, the roots are \( 1/2 \) and \( -2 \); indeed \( 2x^2 + 3x - 2 = (2x - 1)(x + 2) \).
:::

::: {.remark}
[Looking ahead]

Two sharper tests for irreducibility over \( \nQ \), Gauss's lemma and Eisenstein's criterion, belong to a later algebra volume of the series; nothing in this volume uses them.
:::

## Exercises

### A. Check your understanding

::: {#exr-irreducible-factorization-a1}
[A1]

These questions are about the uniqueness half of the proof of @thm-polynomial-unique-factorization.

::: {.enumerate options="label=(\alph*)"}
1. Which line of the proof uses Euclid's lemma, and through which result?
2. Where is "monic" used?
3. In \( \nF_5[x] \), run the induction step on the two lists \( (p_1, p_2, p_3, p_4) = (x - 1, x - 2, x - 3, x - 4) \) and \( (q_1, q_2, q_3, q_4) = (x - 4, x - 3, x - 2, x - 1) \). Which \( j \) matches \( p_4 \)? What is the bijection \( \sigma \) at the end?
4. Why must the empty list be allowed?
5. Give the idea of the uniqueness proof in two sentences.
:::
:::

::: {.solution}
(a) The line "\( p_{k+1} \mid q_j \) for some \( j \le l \)". It cites @cor-irreducible-divides-product (c), proved by induction from (b), which is @thm-polynomial-euclid-lemma applied when \( \gcd(p, g) = 1 \).

(b) In \( p_{k+1} = q_j \): from \( p_{k+1} \mid q_j \) and irreducibility of \( q_j \) we only get \( q_j = u \, p_{k+1} \) with \( u \) a non-zero constant, and comparing the leading coefficients \( 1 = u \) needs both monic (@cor-irreducible-divides-product (d)). Also in \( c' = c \): the products of the monic lists are monic by (L1).

(c) \( p_4 = x - 4 \) divides \( q_1 q_2 q_3 q_4 \); the only \( q_j \) it divides is \( q_1 = x - 4 \), so \( j = 1 \) and \( \sigma(4) = 1 \). The shortened list is \( (q'_1, q'_2, q'_3) = (x - 3, x - 2, x - 1) \), and \( \tau(t) = t + 1 \). The step for \( k = 2 \) matches \( p_3 = x - 3 \) with \( q'_1 \), and so on down. Unwinding, \( \sigma(i) = 5 - i \): \( q_{5-i} = x - i = p_i \) for \( i = 1, 2, 3, 4 \).

(d) The induction on \( k \) starts at \( k = 0 \), and \( U(0) \) is about the empty list, whose product is \( 1 \); each step removes one entry, so the empty list is where every chain of steps ends.

(e) The last irreducible of one factorization divides the other product, so by Euclid's lemma it divides, and so equals, one of the other's irreducibles. Cancel it from both sides and apply the induction hypothesis to the two shorter lists.
:::

### B. Practice

::: {#exr-irreducible-factorization-b1}
[B1: Determine which]

Determine whether each polynomial is irreducible over the given field. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( x^2 + 2 \) over \( \nQ \), over \( \nF_2 \), over \( \nF_3 \).
2. \( x^3 + x + 1 \) over \( \nF_2 \) and over \( \nF_3 \).
3. \( x^4 + 4 \) over \( \nQ \).
4. \( 3x^3 + x^2 - 2 \), with its coefficients read in \( \nF_2 \).
:::
:::

::: {.solution}
(a) Over \( \nQ \): irreducible, since \( c^2 + 2 \ge 2 > 0 \) for \( c \in \nQ \) (@fd3:prp-ordered-ring-rules (e), (h)), so there is no root, and the degree is \( 2 \) (@prp-irreducible-low-degree (b)). Over \( \nF_2 \): \( 2 = 0 \), so the polynomial is \( x^2 = x \cdot x \), reducible. Over \( \nF_3 \): \( 2 = -1 \), so it is \( x^2 - 1 = (x - 1)(x + 1) \), reducible.

(b) Over \( \nF_2 \): the values at \( 0 \) and \( 1 \) are \( 1 \) and \( 3 = 1 \); no root, degree \( 3 \), irreducible. Over \( \nF_3 \): the value at \( 1 \) is \( 3 = 0 \), so it is reducible (@prp-irreducible-low-degree (a)); indeed \( x^3 + x + 1 = (x - 1)(x^2 + x + 2) \) in \( \nF_3 \).

(c) Reducible: \( x^4 + 4 = (x^2 + 2x + 2)(x^2 - 2x + 2) \) (the warning after @prp-irreducible-low-degree), although it has no rational root.

(d) In \( \nF_2 \), \( 3 = 1 \) and \( -2 = 0 \), so the polynomial is \( x^3 + x^2 = x^2(x + 1) \). It has the root \( 0 \) and degree \( 3 \), so it is reducible.
:::

::: {#exr-irreducible-factorization-b2}
[B2: The polynomials vanishing at the square root of two]

Let \( s \in \nR \) be the non-negative square root of \( 2 \) (@fd3:prp-cof-square-roots, in the complete ordered field \( \nR \)), and let
\[
J \coloneqq \{ f \in \nQ[x] : f(s) = 0 \} ,
\]
where \( f(s) \) is computed in \( \nR \), reading \( \nQ[x] \subseteq \nR[x] \) coefficientwise. Prove that \( J = \langle x^2 - 2 \rangle \).

The beginning and the end of a proof are given.

> \( J \) is an ideal of \( \nQ[x] \), since evaluation at \( s \) respects sums and products (@thm-evaluation-respects-operations). It contains \( x^2 - 2 \), and \( 1 \notin J \). Let \( d \) be a monic element of least degree in \( J \). Let \( f \in J \), and divide: \( f = qd + r \) with \( \deg r < \deg d \) (@thm-polynomial-division-remainder).
>
> *[Blank.]*
>
> So \( J = \langle d \rangle \). Then \( d \mid x^2 - 2 \), and \( \deg d \ge 2 \): \( \deg d = 0 \) would make \( d = 1 \in J \), and \( \deg d = 1 \) would give \( d = x + a \) with \( a \in \nQ \) and \( s = -a \), a rational number whose square is \( 2 \), against @fd3:thm-no-rational-square-two. Hence \( d = x^2 - 2 \).

*Name the move, then complete it.*
:::

::: {.solution}
The move is **least degree, then divide**: in a set closed under the right operations, a remainder on division by an element of least degree lies in the set and has smaller degree, so it is \( 0 \).

Completion of the blank: \( r = f - qd \), and \( f, d \in J \), so \( r \in J \) because \( J \) is an ideal (it absorbs the multiple \( qd \) and is closed under differences). A non-zero \( r \) would be a non-zero element of \( J \) of degree less than \( \deg d \); its monic associate would lie in \( J \) too and have the same degree, against the choice of \( d \). So \( r = 0 \), and \( f = qd \in \langle d \rangle \). Conversely every multiple of \( d \) lies in \( J \). This is the argument of @thm-polynomial-ideals-principal, run on \( J \).

For the end: \( d \mid x^2 - 2 \) because \( x^2 - 2 \in J = \langle d \rangle \). So \( \deg d \le 2 \) (@prp-polynomial-divisibility-rules (d)), and with \( \deg d \ge 2 \), \( x^2 - 2 = d u \) with \( u \) a constant; both being monic, \( u = 1 \). In the language of this section, \( x^2 - 2 \) is irreducible over \( \nQ \): it has degree \( 2 \) and no rational root, since a root \( c \) would satisfy \( c^2 = 2 \), against @fd3:thm-no-rational-square-two (@prp-irreducible-low-degree (b)). Every rational polynomial vanishing at \( s \) is a multiple of it.
:::

::: {#exr-irreducible-factorization-b3}
[B3: The small irreducibles over the two-element field]

List all irreducible polynomials of degree at most \( 3 \) over \( \nF_2 \), and prove that the list is complete.
:::

::: {.solution}
Over \( \nF_2 \) the only non-zero constant is \( 1 \), so every non-zero polynomial is monic and associates are equal. There are \( 2 + 4 + 8 = 14 \) polynomials of degree \( 1 \), \( 2 \) or \( 3 \): the coefficient of the top power is \( 1 \), and each lower coefficient is \( 0 \) or \( 1 \).

- **Degree 1:** \( x \) and \( x + 1 \), both irreducible (the first example after @def-irreducible-over-field).
- **Degrees 2 and 3:** by @prp-irreducible-low-degree (b), irreducible exactly when there is no root. The value at \( 0 \) is the constant term, and the value at \( 1 \) is the sum of the coefficients, which is \( 0 \) in \( \nF_2 \) exactly when the number of non-zero coefficients is even. So the irreducible ones have constant term \( 1 \) and an odd number of non-zero coefficients.

In degree \( 2 \), the candidates with constant term \( 1 \) are \( x^2 + 1 \) (two non-zero coefficients) and \( x^2 + x + 1 \) (three); only \( x^2 + x + 1 \) is irreducible. In degree \( 3 \) they are \( x^3 + 1 \), \( x^3 + x + 1 \), \( x^3 + x^2 + 1 \), \( x^3 + x^2 + x + 1 \), with two, three, three and four non-zero coefficients; so \( x^3 + x + 1 \) and \( x^3 + x^2 + 1 \) are irreducible. The complete list is
\[
x, \quad x + 1, \quad x^2 + x + 1, \quad x^3 + x + 1, \quad x^3 + x^2 + 1 .
\]
:::

### C. Going deeper

::: {#exr-irreducible-factorization-c1}
[C1: Exit check: unique factorization]

Prove the uniqueness half of @thm-polynomial-unique-factorization: if \( c \, p_1 \cdots p_k = c' q_1 \cdots q_l \) with \( c, c' \in F \) non-zero and all \( p_i \), \( q_j \) monic irreducible over the field \( F \), then \( c = c' \), \( l = k \), and the two lists agree up to a bijection of indices. You may cite Euclid's lemma (@thm-polynomial-euclid-lemma) and @cor-irreducible-divides-product.
:::

::: {.solution}
The uniqueness part of the proof of @thm-polynomial-unique-factorization is a complete answer. Its steps, in order: the products of the monic lists are monic (L1), so comparing leading coefficients gives \( c = c' \), and dividing by \( c \) leaves equal products; induction on \( k \), with the statement quantified over every length \( l \) of the other list; base case \( k = 0 \), where a non-empty list of monic irreducibles has a product of degree at least \( 1 \); in the step, \( p_{k+1} \) divides the other product, so it divides some \( q_j \) by @cor-irreducible-divides-product (c), and equals it by (d); remove \( q_j \) from its list (L2) and cancel \( p_{k+1} \ne 0 \) (@cor-polynomial-no-zero-divisors (b)); the induction hypothesis on the shortened lists gives \( l - 1 = k \) and a bijection, extended by \( k + 1 \mapsto j \).

**Marking scheme.** (10 points)
- 1: compares leading coefficients to get \( c = c' \), with a reason that a product of monic polynomials is monic.
- 2: sets up an induction on the length of one list (or a least counterexample), with the statement quantified over all lengths of the other list, and proves the base case by a degree argument.
- 3: shows that an irreducible of one list divides the other product and **equals** one of its factors, citing Euclid's lemma for several factors **and** "monic irreducible divides monic irreducible implies equal".
- 1: justifies the cancellation by the absence of zero divisors in \( F[x] \).
- 3: applies the induction hypothesis to the shortened lists, with the removal of the matched entry stated, and extends the bijection.
Fatal errors (0 for the step): using the uniqueness for a polynomial of smaller degree without an induction set up; concluding \( p_{k+1} = q_j \) from \( p_{k+1} \mid q_j \) without using that both are monic and irreducible. A proof by strong induction on \( \deg f \) maps to the same points: its set-up and the degree-\( 0 \) case take the 2 points of the induction, and "the cofactor has a unique factorization" takes the last 3.
:::

::: {#exr-irreducible-factorization-c2}
[C2: Find the error]

Here is a statement and an argument for it.

> **Claim.** \( x^4 + 1 \) is irreducible over \( \nQ \).
>
> **Argument.** (1) By @thm-rational-root-test, a rational root of \( x^4 + 1 \) is \( u/v \) with \( u \mid 1 \) and \( v \mid 1 \), so the only candidates are \( 1 \) and \( -1 \). (2) Both give the value \( 1 + 1 = 2 \ne 0 \), so \( x^4 + 1 \) has no rational root. (3) By @prp-irreducible-low-degree, a polynomial without roots is irreducible. (4) Hence \( x^4 + 1 \) is irreducible over \( \nQ \).

Is the claim true? Does the argument prove it? If not, name the line that fails, explain why, give a counterexample to the step, and repair the proof.
:::

::: {.solution}
The claim is **true**; the argument does **not** prove it.

Lines (1) and (2) are correct. The failing line is (3). @prp-irreducible-low-degree (b) is stated for polynomials of degree \( 2 \) or \( 3 \), and \( x^4 + 1 \) has degree \( 4 \): the line applies a result outside its hypotheses, a "fact" that is not available, entry (N9) of @fd1:exm-not-allowed-catalogue. A counterexample to the step: \( x^4 + 4 \) has no rational root and is reducible (the warning after @prp-irreducible-low-degree).

*Repair.* Suppose \( x^4 + 1 = gh \) with \( \deg g, \deg h \ge 1 \). The leading coefficients multiply to \( 1 \), so replacing \( g \), \( h \) by their monic associates we may take both monic. The degrees add up to \( 4 \). If one of them is \( 1 \), that factor has a root in \( \nQ \) (@thm-polynomial-remainder-factor (c)), against lines (1)–(2). So both have degree \( 2 \): \( g = x^2 + ax + b \), \( h = x^2 + cx + d \) with \( a, b, c, d \in \nQ \). Comparing coefficients in
\[
(x^2 + ax + b)(x^2 + cx + d) = x^4 + (a + c)x^3 + (b + d + ac)x^2 + (ad + bc)x + bd
\]
with \( x^4 + 1 \) gives \( c = -a \), \( b + d - a^2 = 0 \), \( a(d - b) = 0 \) and \( bd = 1 \). Since \( \nQ \) has no zero divisors (@thm-field-basic-properties (f)), \( a = 0 \) or \( d = b \).

- If \( a = 0 \): \( d = -b \) and \( -b^2 = 1 \), impossible since \( b^2 \ge 0 > -1 \) (@fd3:prp-ordered-ring-rules (e)).
- If \( d = b \): \( b^2 = 1 \), so \( b = \pm 1 \) (@cor-field-squares-equal), and \( a^2 = 2b = \pm 2 \). Now \( a^2 = 2 \) is impossible by @fd3:thm-no-rational-square-two, and \( a^2 = -2 < 0 \) is impossible since squares are non-negative.

So no splitting exists, and \( x^4 + 1 \) is irreducible over \( \nQ \).
:::

::: {#exr-irreducible-factorization-c3}
[C3: Infinitely many irreducibles]

::: {.enumerate options="label=(\alph*)"}
1. Let \( F \) be a field. Prove that no finite list contains every monic irreducible polynomial of \( F[x] \): for every list \( (p_1, \dots, p_k) \) of monic irreducibles, \( k \in \nN \), some monic irreducible is not an entry of it.
2. Let \( p \) be prime. Prove that there are exactly \( p^n \) monic polynomials of degree \( n \) in \( \nF_p[x] \), for each \( n \in \nN \), and deduce that \( \nF_p[x] \) has monic irreducibles of arbitrarily large degree.
:::
:::

::: {.solution}
[Hint 1]

For (a), copy the integer argument: consider \( p_1 \cdots p_k + 1 \). For (b), a monic polynomial of degree \( n \) is determined by its \( n \) lower coefficients.
:::

::: {.solution}
[Hint 2]

For (a): by (L1) the product has degree at least \( 1 \) when \( k \ge 1 \), so \( N \coloneqq p_1 \cdots p_k + 1 \) has a monic irreducible factor (@lem-polynomial-irreducible-factor).
:::

::: {.solution}
*(a)* If \( k = 0 \), the polynomial \( x \) is monic and irreducible and not an entry. Let \( k \ge 1 \) and \( P \coloneqq p_1 \cdots p_k \). By (L1), \( P \) is monic of degree \( \sum_i \deg p_i \ge 1 \). Then \( N \coloneqq P + 1 \) has \( \deg N = \deg P \ge 1 \) (@thm-degree-of-sum, the degrees of \( P \) and \( 1 \) differ), so \( N \) has a monic irreducible divisor \( q \) (@lem-polynomial-irreducible-factor). If \( q = p_i \) for some \( i \), then \( q \mid P \) by (L2), and \( q \mid N - P = 1 \) (@prp-polynomial-divisibility-rules (c)), so \( \deg q \le 0 \) (@prp-polynomial-divisibility-rules (d)), against \( \deg q \ge 1 \). So \( q \) is a monic irreducible that is not an entry of the list.

*(b)* A monic polynomial of degree \( n \) has \( n \) lower coefficients \( a_0, \dots, a_{n-1} \in \nF_p \), and by @def-polynomial (equality coefficientwise) the map sending it to \( (a_0, \dots, a_{n-1}) \) is a bijection onto the set \( T_n \) of such tuples; its inverse puts \( 1 \) in position \( n \) and zeros above. We show \( \card{T_n} = p^n \) by @fd1:ax-induction on \( n \). \( T_0 \) has one element, the empty tuple, and \( p^0 = 1 \). The tuples of length \( n + 1 \) split by their last entry into \( p \) pairwise disjoint sets, one for each element of \( \nF_p \), which has \( p \) elements (@def-field-fp); each is in bijection with \( T_n \) (drop the last entry). Applying @fd2:prp-disjoint-union-count \( p - 1 \) times (an induction on the number of pieces), \( \card{T_{n+1}} = p \cdot p^n = p^{n+1} \).

So for each \( M \in \nN \), the monic polynomials of degree at most \( M \) form a finite set: a union of the finitely many finite sets for \( n = 0, \dots, M \), pairwise disjoint, again by @fd2:prp-disjoint-union-count. Suppose every monic irreducible of \( \nF_p[x] \) had degree at most \( M \). Then they would form a subset of a finite set, hence a finite set (@fd2:prp-subset-finite), and a bijection \( \{1, \dots, k\} \to \) that set (@fd2:def-finite) would be a list containing every monic irreducible, against (a). So for every \( M \) there is a monic irreducible of degree greater than \( M \).

**Marking scheme.** (10 points)
- 2: (a) builds a polynomial \( N \) of degree \( \ge 1 \) that is \( 1 \) more than a multiple of \( p_1 \cdots p_k \) (e.g. \( p_1 \cdots p_k + 1 \), or \( x \, p_1 \cdots p_k + 1 \)), and shows \( \deg N \ge 1 \) for every \( k \), \( k = 0 \) included (or treats \( k = 0 \) separately).
- 3: (a) takes a monic irreducible factor \( q \) of \( N \) and shows \( q \) is no \( p_i \), since it would divide \( 1 \).
- 3: (b) counts the monic polynomials of degree \( n \) through their coefficient tuples, with an induction or a cited counting result.
- 2: (b) concludes by contradiction with (a): a bound on the degrees would make the irreducibles a finite set, hence a list.
Fatal errors (0 for the step): claiming that \( N \) itself is irreducible; taking "the product of all monic irreducibles" without a finite list.
:::

::: {#exr-irreducible-factorization-c4}
[C4: Greatest common divisor and least common multiple]

Let \( f, g \in F[x] \) be monic, \( d \coloneqq \gcd(f, g) \), and write \( f = d f_1 \), \( g = d g_1 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \gcd(f_1, g_1) = 1 \).
2. Prove that \( L \coloneqq d f_1 g_1 \) is a monic common multiple of \( f \) and \( g \) that divides every common multiple of \( f \) and \( g \), and that \( d \cdot L = fg \).
3. In \( \nQ[x] \), let \( f = g = 2x \) (not monic). The gcd is \( x \), and the monic common multiple dividing every common multiple is \( x \). Show that \( \gcd(f, g) \cdot x \ne fg \).
:::
:::

::: {.solution}
*(a)* Since \( f \ne 0 \), \( d \) is monic, so \( d \ne 0 \). By @thm-polynomial-bezout (d), \( d = af + bg \) for some \( a, b \in F[x] \), so \( d \cdot 1 = d(af_1 + bg_1) \). Canceling \( d \) (@cor-polynomial-no-zero-divisors (b)), \( af_1 + bg_1 = 1 \), and \( \gcd(f_1, g_1) = 1 \) by @cor-polynomial-coprime-iff-combination.

*(b)* Comparing leading coefficients in \( f = d f_1 \) (@thm-degree-of-product (b)) gives \( \operatorname{lc}(f_1) = 1 \); likewise \( g_1 \) is monic, so \( L \) is monic (L1). It is a common multiple: \( L = f g_1 = g f_1 \). Let \( h \) be a common multiple, \( h = fk = g m \) with \( k, m \in F[x] \). Then \( d f_1 k = d g_1 m \), and canceling \( d \), \( f_1 k = g_1 m \). So \( g_1 \mid f_1 k \), and \( \gcd(g_1, f_1) = 1 \) by (a), hence \( g_1 \mid k \) by @thm-polynomial-euclid-lemma; say \( k = g_1 t \). Then \( h = d f_1 g_1 t = L t \), and \( L \mid h \). Finally \( d \cdot L = (d f_1)(d g_1) = fg \).

*(c)* \( \gcd(2x, 2x) = x \) by @def-polynomial-gcd: \( x \) is monic and divides \( 2x \), and every common divisor \( h \) of \( 2x \) and \( 2x \) divides \( 2^{-1}(2x) = x \) (@prp-polynomial-divisibility-rules (b)). Next, \( x \) is monic and a common multiple of \( f = g = 2x \), since \( 2^{-1}(2x) = x \). It divides every common multiple \( h \): \( x \mid 2x \) and \( 2x \mid h \), so \( x \mid h \) by @prp-polynomial-divisibility-rules (b). Any other monic \( L' \) with these two properties satisfies \( x \mid L' \) and \( L' \mid x \), so \( L' = x \) by @prp-polynomial-divisibility-rules (f). But \( x \cdot x = x^2 \ne 4x^2 = fg \), since \( 1 \ne 4 \) in \( \nQ \). The identity of (b) needs \( f \) and \( g \) monic. For non-zero \( f \), \( g \), the monic associates \( \operatorname{lc}(f)^{-1} f \) and \( \operatorname{lc}(g)^{-1} g \) have the same common divisors and the same common multiples as \( f \) and \( g \), since each divides the other; so (b) applied to them gives \( d \cdot L = \operatorname{lc}(f)^{-1} \operatorname{lc}(g)^{-1} fg \).
:::

<!-- dependency ledger
def-irreducible-over-field (claim): reducible iff p = gh with both degrees >= 1, both < deg p; a constant factor of p != 0 is non-zero | thm-degree-of-product (b) (cited); prp-ring-algebra (b) (0 * h = 0), used silently
def-irreducible-over-field (example): (x + 1)^2 = x^2 + 2x + 1 = x^2 + 1 in F_2 | ring arithmetic, 2 = 0 in F_2 (def-field-fp); verify/ch04/exm-factor-x4-minus-one-fields.py
def-irreducible-over-field (claim): (fold) padding factorizations with units; (1, 2, 2, 3, 5) for 60 | comparison with fd3 F3.5 Section 3.3 (prose only), nothing depends on it
prp-irreducible-low-degree (proof): two natural numbers >= 1 with sum 2 or 3, one of them is 1 | arithmetic of N (fd3 cor-omega-identification), used silently
prp-irreducible-low-degree (claim): c^2 + 1 >= 1 > 0 in an ordered field; Q and R are ordered fields | fd3:prp-ordered-ring-rules (b), (e) (cited); Q ordered field fd3:thm-rationals-ordered-field, R by fd3:thm-reals-complete-ordered-field; used without @ref in prose
prp-irreducible-low-degree (claim): (warning) c^4 + 4 >= 4 > 0; (x^2 + 2x + 2)(x^2 - 2x + 2) = x^4 + 4 | fd3:prp-ordered-ring-rules (e) (c^4 = (c^2)^2), (h) (4 * 1 > 0) (cited), expansion; verify/ch04/prp-irreducible-low-degree.py
prp-irreducible-low-degree (claim): (check) 2x^2 + 4 = 2(x^2 + 2); c^2 + 2 >= 2 > 0; 1 is a root of x^2 + 2 in F_3; x^2 - 1 = (x - 1)(x + 1) | fd3:prp-ordered-ring-rules (e), (h) (cited); ring arithmetic in F_3 (def-field-fp); verify/ch04/prp-irreducible-low-degree.py
thm-polynomial-euclid-lemma (claim): (aftermath) gcd(x^2, x) = x | def-polynomial-gcd: x is a monic common divisor, every common divisor divides x; one line, inline
cor-irreducible-divides-product (claim): products of lists in F[x] | fd2:def-sum-product used as a pattern through lem-finite-sums-and-powers (a) with R = F[x] (cited); blueprint ledger line (sums, products, powers)
cor-irreducible-divides-product (proof): a monic constant is 1 | def-degree (monic: lc = 1), used silently
prp-polynomial-coprime-divisors-product (proof): gcd(n, m) = gcd(m, n) | def-polynomial-gcd, its clauses are symmetric (said in the proof)
lem-polynomial-irreducible-factor (proof): the monic associate g_1 of g, g = lc(g) g_1, deg g_1 = deg g | prp-polynomial-divisibility-rules (f) (unique monic associate), thm-degree-of-product (b); used silently
thm-polynomial-unique-factorization (claim): (L1), (L2) about products of lists | inline (second-reading fold "Proofs of (L1) and (L2)"), by induction from the recursion; (F5), (F6) in F[x] (thm-polynomial-ring-laws (a))
thm-polynomial-unique-factorization (claim): (L1) degree of a product is the sum of degrees (finite sums in N) | fd2:def-sum-product as a template on N (through fd3:cor-omega-identification); thm-degree-of-product (b)
thm-polynomial-unique-factorization (proof): deg u = n - deg p < n since deg p >= 1 | arithmetic of N (fd3:cor-omega-identification (c)), used silently
thm-polynomial-unique-factorization (proof): sum of l terms each >= 1 is >= l | induction on l, arithmetic of N; used silently
thm-polynomial-unique-factorization (proof): tau is a bijection; sigma assembled from a bijection onto {1..l} minus {j} and k+1 -> j is a bijection | fd2:def-bijective (cited), checked in the proof
thm-polynomial-unique-factorization (proof): the empty function is a bijection between empty sets | fd2:def-finite, first example (the empty function); used silently
exm-factor-x4-minus-one-fields (example): expansions; values of x^2 + 1 on F_3; (x - 2)(x - 3) = x^2 + 1 in F_5; x + 1 = x - 4 in F_5; (x + 1)^4 = x^4 + 1 in F_2 | ring arithmetic mod p (def-field-fp); verify/ch04/exm-factor-x4-minus-one-fields.py
exm-factor-x4-minus-one-fields (claim): (check) x^2 + x + 1 values in F_2; (x - 1)^2 = x^2 + x + 1 in F_3 | arithmetic mod p; verify/ch04/exm-factor-x4-minus-one-fields.py
thm-rational-root-test (proof): Z inside Q, f(u/v) computed in Q, integers closed under + and * | fd3 F3.2 (prp-integers-embed-rationals), blueprint ledger line (Q in R in C); used silently
thm-rational-root-test (proof): rearranging the multiplied equation into a_0 v^n = -u(...), a_n u^n = -v(...) | ring axioms (F5)-(F9) in Z and Q, lem-finite-sums-and-powers (b) (Sigma2) for factoring u, v out of a finite sum; used silently
thm-rational-root-test (proof): gcd(v, u) = gcd(u, v) | fd3:def-integer-gcd (symmetric), used silently
exm-cubic-no-rational-root (example): divisors of -2 are +-1, +-2; positive divisors of 3 are 1, 3; the eight values | fd3:prp-divisibility-rules-integers (e) (cited); arithmetic in Q; verify/ch04/exm-cubic-no-rational-root.py
exm-cubic-no-rational-root (claim): (check) candidates and roots of 2x^2 + 3x - 2; (2x - 1)(x + 2) | arithmetic in Q; verify/ch04/exm-cubic-no-rational-root.py
exr-irreducible-factorization-a1 (solution): the run on (x - 1, ..., x - 4) in F_5; sigma(i) = 5 - i | the proof of thm-polynomial-unique-factorization; x - i divides x - j in F_5 only for i = j (cor-irreducible-divides-product (d)); verify/ch04/exr-irreducible-factorization-a1.py
exr-irreducible-factorization-b1 (solution): values over F_2, F_3; x^3 + x + 1 = (x - 1)(x^2 + x + 2) in F_3; c^2 + 2 >= 2 > 0 | arithmetic mod p; fd3:prp-ordered-ring-rules (e), (h) (cited); verify/ch04/exr-irreducible-factorization-b1.py
exr-irreducible-factorization-b2 (claim): (problem text) s = sqrt 2 in R; Q[x] inside R[x]; evaluation in R | fd3:prp-cof-square-roots (cited), R complete ordered field fd3:thm-reals-complete-ordered-field; blueprint ledger line (Q in R in C)
exr-irreducible-factorization-b2 (solution): J is an ideal of Q[x] (absorbs multiples, closed under differences) | fd3:def-ideal-commutative-ring with thm-evaluation-respects-operations, given in the problem; nothing in the text rests on this exercise
exr-irreducible-factorization-b3 (solution): 14 polynomials; f(1) = sum of coefficients; the list | thm-evaluation-respects-operations; counting by inspection; verify/ch04/exr-irreducible-factorization-b3.py
exr-irreducible-factorization-c2 (solution): coefficients of (x^2 + ax + b)(x^2 + cx + d); case analysis | expansion; a(d - b) = 0 gives a = 0 or d = b by thm-field-basic-properties (f); cor-field-squares-equal, fd3:thm-no-rational-square-two, fd3:prp-ordered-ring-rules (e) (cited); verify/ch04/exr-irreducible-factorization-c2.py
exr-irreducible-factorization-c3 (solution): F_p has p elements; tuples of length n + 1 split by last entry; finite union of finite sets is finite; subset of a finite set is finite | def-field-fp, fd2:prp-disjoint-union-count, fd2:prp-subset-finite, fd2:def-finite (cited); verify/ch04/exr-irreducible-factorization-c3.py
exr-irreducible-factorization-c4 (solution): lc(f) = lc(d) lc(f_1) gives f_1 monic | thm-degree-of-product (b) (cited)
exr-irreducible-factorization-c4 (solution): (c) gcd(2x, 2x) = x; x is the monic common multiple dividing every common multiple; d L = lc(f)^{-1} lc(g)^{-1} fg via monic associates | def-polynomial-gcd, prp-polynomial-divisibility-rules (b), (f) (cited)
def-irreducible-over-field (example): deg(ap) = deg p for a != 0 | thm-degree-of-product (b) (cited)
thm-rational-root-test (claim): (aftermath) finitely many candidates when a_0 != 0; f = x^k g when a_0 = 0 | fd3:prp-divisibility-rules-integers (d), (e), thm-evaluation-respects-operations (cited); f = x^k g by comparing coefficients (def-polynomial), Q has no zero divisors (thm-field-basic-properties (f)), used silently; |u| <= |a_0| from (d), (e) via absolute value, used silently
exr-irreducible-factorization-b2 (solution): x^2 - 2 has no rational root | fd3:thm-no-rational-square-two, prp-irreducible-low-degree (b) (cited)
-->
