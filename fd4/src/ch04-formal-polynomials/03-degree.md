# Degree, Leading Coefficients, and Integral Domains

Section 4.2 made \( R[x] \) a commutative ring for every commutative ring \( R \) (@thm-polynomial-ring-laws). This section attaches to each non-zero polynomial its **degree**, the position of its last non-zero coefficient, and asks the school question: is the degree of a product the sum of the degrees? Over \( \nZ \) it is. Over \( \nZ/6\nZ \) it is not, and the reason is a single product of two elements of \( R \). Sorting out which rings behave like \( \nZ \) leads to the integral domains, and to the two facts later chapters use most: a polynomial ring over an integral domain has no zero divisors, and its units are the units of \( R \).

Throughout, \( R \) is a commutative ring (@fd3:def-commutative-ring-and-field), and polynomials are coefficient sequences (@def-polynomial), with the sum and product of @def-polynomial-ring.

## Degree and leading coefficient

Here is the computation that drives the section. Multiply \( p = 2x + 1 \) by \( q = 3x^2 + x \) by the product formula of @def-polynomial-ring, once in \( \nZ[x] \) and once in \( (\nZ/6\nZ)[x] \). The coefficients of \( p \) are \( 1, 2, 0, 0, \dots \) and those of \( q \) are \( 0, 1, 3, 0, \dots \), so
\[
\begin{aligned}
(pq)_0 &= p_0 q_0 = 0, \\
(pq)_1 &= p_0 q_1 + p_1 q_0 = 1, \\
(pq)_2 &= p_0 q_2 + p_1 q_1 + p_2 q_0 = 3 + 2 = 5, \\
(pq)_3 &= p_0 q_3 + p_1 q_2 + p_2 q_1 + p_3 q_0 = 2 \cdot 3 = 6,
\end{aligned}
\]
and \( (pq)_k = 0 \) for \( k \ge 4 \). Over \( \nZ \) the product is \( 6x^3 + 5x^2 + x \), with its last non-zero coefficient in position \( 3 = 1 + 2 \). Over \( \nZ/6\nZ \) the same sums are read modulo \( 6 \): \( (pq)_3 = [6] = [0] \), and the product is \( [5]x^2 + x \), whose last non-zero coefficient sits in position \( 2 \). The top coefficient of the product was \( 2 \cdot 3 \), the product of the top coefficients of the factors, and in \( \nZ/6\nZ \) that product is \( [0] \) (@fd3:exm-integers-mod-six).

To state any of this we need a name for "the position of the last non-zero coefficient". A non-zero polynomial has one, because only finitely many of its coefficients are non-zero.

*The degree of a polynomial is the position of its last non-zero coefficient; the leading coefficient is the coefficient sitting there.*

::: {#def-degree}
[Degree, Leading Coefficient, Monic]

Let \( R \) be a commutative ring and \( p \in R[x] \).

::: {.enumerate options="label=(\alph*)"}
1. If \( p \ne 0 \), the **degree** \( \deg p \) is the **largest** \( n \in \nN \) with \( p_n \ne 0 \). The **leading coefficient** of \( p \) is \( \operatorname{lc}(p) \coloneqq p_{\deg p} \), and \( p \) is **monic** if \( \operatorname{lc}(p) = 1 \).
2. The zero polynomial has degree \( \deg 0 \coloneqq -\infty \), and **no** leading coefficient.
:::

Here \( -\infty \) is a symbol not in \( \nN \), with the conventions \( -\infty < n \) and \( -\infty + n = n + (-\infty) = -\infty \) for every \( n \in \nN \), and \( -\infty + (-\infty) = -\infty \).
:::

In words: (a) looks along the coefficient sequence and stops at the last place where it is non-zero; that place is the degree, and the entry there is the leading coefficient. A polynomial is monic when that entry is \( 1 \). Clause (b) gives the zero polynomial, which has no non-zero coefficient at all, a degree below every natural number.

*Well-definedness.* Let \( p \ne 0 \), and let \( N \) be admissible for \( p \): \( p_k = 0 \) for every \( k > N \) (@def-polynomial). The set \( S \coloneqq \{ n \in \nN : p_n \ne 0 \} \) is non-empty, since \( p \) is not the zero sequence, and every element of \( S \) is at most \( N \). Read in \( \nZ \supseteq \nN \) (@fd3:prp-naturals-embed-integers), \( S \) is a non-empty set of integers bounded above, so it has a greatest element (@fd3:prp-integer-least-element). That element is \( \deg p \). Two facts come with it, and every proof below uses them:
\[
p_{\deg p} \ne 0 , \qquad p_k = 0 \ \text{ for every } k > \deg p .
\]
The second says that \( \deg p \) is itself admissible for \( p \), and the least admissible \( N \): any smaller \( N \) would leave the non-zero coefficient \( p_{\deg p} \) beyond it.

**Examples.**

- In \( \nQ[x] \), \( \deg(3x^2 - x + 2) = 2 \) with leading coefficient \( 3 \); \( x^2 + 1 \) is monic of degree \( 2 \). The monomial \( a x^n \) with \( a \ne 0 \) has degree \( n \) and leading coefficient \( a \).
- A non-zero constant \( a = a x^0 \) has degree \( 0 \). The constant \( 0 \) has degree \( -\infty \), not \( 0 \): degree \( 0 \) means "a constant, and not the zero one".
- Degree depends on the ring. The integer polynomial \( 6x^3 + 5x^2 + x \) has degree \( 3 \) in \( \nZ[x] \); its coefficients read in \( \nZ/6\nZ \) give \( [5]x^2 + x \), of degree \( 2 \). Read in \( \nZ/5\nZ \) they give \( x^3 + x \) (\( [6] = [1] \), \( [5] = [0] \)), monic of degree \( 3 \).
- **The degenerate ring.** If \( 1 = 0 \) in \( R \), then every \( a \in R \) is \( a = a \cdot 1 = a \cdot 0 = 0 \) (@fd3:prp-ring-algebra (b)), so \( R = \{0\} \), and the only polynomial over \( R \) is the zero sequence. Every polynomial over the zero ring has degree \( -\infty \), and no polynomial over it is monic. This is why "monic" will never need the hypothesis \( 1 \ne 0 \): a monic polynomial is non-zero, so its ring has \( 1 = \operatorname{lc}(p) \ne 0 \).

**Non-example by minimal change.** The sequence \( (1, 1, 1, \dots) \) has no degree: the set \( S \) of its non-zero positions is all of \( \nN \), which has no greatest element. It fails exactly the clause "only finitely many" of @def-polynomial, which is what made \( S \) bounded above.

::: {.second-reading title="Why the degree of the zero polynomial is minus infinity"}
Any value given to \( \deg 0 \) is a convention, and the choice is made so that the rule "degrees add under products" survives the zero polynomial. For every \( q \), \( 0 \cdot q = 0 \), so the rule asks for \( \deg 0 = \deg 0 + \deg q \). If \( \deg 0 \) were an integer \( d \), then in any ring with \( 1 \ne 0 \) the case \( q = x \), of degree \( 1 \), would give \( d = d + 1 \). No integer works; a symbol \( -\infty \) with \( -\infty + n = -\infty \) does. The order \( -\infty < n \) then lets "\( \deg p \le n \)" include the zero polynomial, which is what the sets \( R[x]_{\le n} \) at the end of this section need.
:::

::: {.warning}
The leading coefficient is the coefficient of the **highest** power, not the first one written. In \( 2 + x - 5x^3 \in \nQ[x] \), the leading coefficient is \( -5 \), and the polynomial is not monic although its \( x \) has coefficient \( 1 \). And the zero polynomial has no leading coefficient at all: "\( \operatorname{lc}(p) \)" silently assumes \( p \ne 0 \).
:::

## The degree of a sum

A sum cannot raise the degree, because adding coefficients position by position creates no non-zero coefficient beyond the last non-zero ones of the summands.

::: {#thm-degree-of-sum}
[Degree of a Sum]

Let \( R \) be a commutative ring and \( p, q \in R[x] \). Then
\[
\deg(p + q) \le \max(\deg p, \deg q) ,
\]
with **equality** when \( \deg p \ne \deg q \).
:::

::: {.idea}
Beyond the larger of the two degrees both summands have only zero coefficients, so the sum does too. When one degree is strictly larger, the other summand contributes \( 0 \) at that top position, and the top coefficient survives.
:::

::: {.proof}
Let \( M \coloneqq \max(\deg p, \deg q) \). If \( M = -\infty \), then \( p = q = 0 \), so \( p + q = 0 \) and both sides are \( -\infty \). Otherwise \( M \in \nN \), and for \( k > M \) we have \( k > \deg p \) and \( k > \deg q \), so \( p_k = 0 \) and \( q_k = 0 \) (by the two facts after @def-degree when the polynomial is non-zero, and trivially when it is \( 0 \)). Hence \( (p + q)_k = p_k + q_k = 0 + 0 = 0 \) for every \( k > M \), by @def-polynomial-ring and (F3). So either \( p + q = 0 \), with degree \( -\infty < M \), or \( p + q \ne 0 \) and its last non-zero coefficient is at a position \( \le M \). In both cases \( \deg(p + q) \le M \).

Now let \( \deg p \ne \deg q \); by symmetry \( \deg q < \deg p \), so \( p \ne 0 \) and \( M = \deg p \). Then \( q_M = 0 \), and
\[
(p + q)_M = p_M + q_M = p_M + 0 = p_M \ne 0 ,
\]
so \( p + q \ne 0 \) and \( \deg(p + q) \ge M \). With the first part, \( \deg(p + q) = M \).
:::

::: {.remark}
The inequality is strict exactly when \( \deg p = \deg q = M \in \nN \) and the leading coefficients cancel, \( p_M + q_M = 0 \): for example \( (x^2 + x) + (-x^2 + 1) = x + 1 \), of degree \( 1 < 2 \), and \( x + (-x) = 0 \), of degree \( -\infty < 1 \).
:::

## The degree of a product

The opening computation suggests how a product behaves at the top. In \( (pq)_k = \sum_{i=0}^{k} p_i q_{k-i} \), a term can be non-zero only if \( i \le \deg p \) **and** \( k - i \le \deg q \); for \( k = \deg p + \deg q \) that leaves exactly one term. We call this move **look at the top coefficient**.

::: {#thm-degree-of-product}
[Degree of a Product]

Let \( R \) be a commutative ring, let \( p, q \in R[x] \) be non-zero, and let \( m \coloneqq \deg p \), \( n \coloneqq \deg q \).

::: {.enumerate options="label=(\alph*)"}
1. \( (pq)_k = 0 \) for every \( k > m + n \), and \( (pq)_{m+n} = \operatorname{lc}(p) \operatorname{lc}(q) \). Hence \( \deg(pq) \le \deg p + \deg q \) for **all** \( p, q \in R[x] \), zero or not; and if \( p = 0 \) or \( q = 0 \), then \( pq = 0 \) and \( \deg(pq) = -\infty = \deg p + \deg q \).
2. \( \deg(pq) = m + n \) **if and only if** \( \operatorname{lc}(p) \operatorname{lc}(q) \ne 0 \), and then \( \operatorname{lc}(pq) = \operatorname{lc}(p) \operatorname{lc}(q) \). This holds in particular
    - when \( R \) has **no zero divisors** (\( ab = 0 \) implies \( a = 0 \) or \( b = 0 \)), for example when \( R \) is a field (@thm-field-basic-properties (f)); together with the last clause of (a), \( \deg(pq) = \deg p + \deg q \) then holds for **all** \( p, q \in R[x] \), zero or not;
    - when \( \operatorname{lc}(p) \) is a unit of \( R \) (@fd3:def-ring-unit), in particular when \( p \) is monic.
:::
:::

In words: (a) says that the product has nothing above position \( m + n \), and that what sits at \( m + n \) is the product of the two leading coefficients, in every commutative ring; (b) says that the degree formula holds precisely when that one product is non-zero, and names two common situations where it is.

::: {.idea}
The top of a product comes from the tops of the factors alone. Above \( m + n \) every term \( p_i q_{k-i} \) has a factor beyond the top of \( p \) or beyond the top of \( q \); at \( m + n \) exactly one term escapes, \( p_m q_n \). So the only question is whether \( p_m q_n \) can be \( 0 \), and that is a question about \( R \), not about polynomials.

*Before reading on: which line needs \( R \) to have no zero divisors, and which works in every ring?*
:::

::: {.proof}
*(a)* Let \( k \ge m + n \) and \( 0 \le i \le k \), and consider the term \( p_i q_{k-i} \) of \( (pq)_k \) (@def-polynomial-ring). If \( i > m \), then \( p_i = 0 \). If \( i \le m \), then \( k - i \ge k - m \ge n \), and \( k - i > n \) (so \( q_{k-i} = 0 \)) unless \( k = m + n \) and \( i = m \). So every term with \( i \ne m \), or with \( k > m + n \), has a factor \( 0 \), and is \( 0 \) by @fd3:prp-ring-algebra (b) with (F6).

For \( k > m + n \), all terms of \( (pq)_k \) are \( 0 \), so \( (pq)_k = 0 \) by (Σ3) of @lem-finite-sums-and-powers (b) (with \( j = 0 \)). For \( k = m + n \), every term with \( i \ne m \) is \( 0 \), and \( m \le m + n \), so (Σ3) with \( j = m \) leaves
\[
(pq)_{m+n} = p_m q_n = \operatorname{lc}(p) \operatorname{lc}(q) .
\]

For the inequality, let \( p, q \in R[x] \) be arbitrary. If \( p = 0 \), every coefficient of \( pq \) is a sum of terms \( 0 \cdot q_{k-i} = 0 \) (@fd3:prp-ring-algebra (b), (F6)), so \( pq = 0 \), and both sides of the inequality are \( -\infty \) by the conventions of @def-degree, which is also the last clause of (a); likewise if \( q = 0 \). If \( p, q \ne 0 \) and \( pq = 0 \), the left side is \( -\infty < m + n \). Otherwise \( pq \ne 0 \), and since \( (pq)_k = 0 \) for every \( k > m + n \), its last non-zero coefficient is at a position \( \le m + n \): \( \deg(pq) \le m + n \).

*(b)* By (a), \( m + n \) is admissible for \( pq \), and \( (pq)_{m+n} = \operatorname{lc}(p) \operatorname{lc}(q) \). If this element is non-zero, then \( pq \ne 0 \), its last non-zero coefficient is at \( m + n \), and so \( \deg(pq) = m + n \) and \( \operatorname{lc}(pq) = (pq)_{m+n} = \operatorname{lc}(p) \operatorname{lc}(q) \). If it is \( 0 \), then \( (pq)_k = 0 \) for every \( k \ge m + n \), so \( \deg(pq) < m + n \).

For the two situations: \( p_m \ne 0 \) and \( q_n \ne 0 \) by @def-degree, so if \( R \) has no zero divisors, \( p_m q_n \ne 0 \). If \( u \coloneqq p_m \) is a unit and \( u q_n = 0 \), then \( q_n = (u^{-1} u) q_n = u^{-1}(u q_n) = u^{-1} \cdot 0 = 0 \), by (F6), (F7), (F5) and @fd3:prp-ring-algebra (b), against \( q_n \ne 0 \); so \( p_m q_n \ne 0 \). A monic \( p \) has \( p_m = 1 \), a unit since \( 1 \cdot 1 = 1 \). This proves the theorem.
:::

The answer to the prompt. Part (a), including the inequality, uses only (F1)–(F7), (F9), @fd3:prp-ring-algebra (b), (Σ3) of @lem-finite-sums-and-powers (b) and the conventions of @def-degree, all valid in every commutative ring: it holds over \( \nZ/6\nZ \) as over \( \nQ \). Part (b) as an equivalence also holds in every ring. "No zero divisors" enters in one line, the first sentence of the last paragraph, and only to decide that \( p_m q_n \ne 0 \); the unit hypothesis is a second, different way to decide the same thing.

::: {.warning}
**The degree formula is not automatic.** In \( (\nZ/6\nZ)[x] \), the opening computation gives
\[
([2]x + [1])([3]x^2 + x) = [5]x^2 + x ,
\]
a product of polynomials of degrees \( 1 \) and \( 2 \) that has degree \( 2 \), not \( 3 \). The coefficient \( (pq)_3 \) is \( \operatorname{lc}(p)\operatorname{lc}(q) = [2][3] = [6] = [0] \) (@fd3:exm-integers-mod-six). Part (a) of @thm-degree-of-product holds here; the hypothesis of (b) fails.
:::

::: {.check}
Let \( p, q \in \nQ[x] \) with \( \deg p = 3 \) and \( \deg q = 2 \). What are \( \deg(pq) \), \( \deg(p + q) \) and \( \deg(p^2) \), where \( p^2 \coloneqq pp \)? Can you say what \( \deg(p - x^3) \) is?
:::

::: {.solution}
\( \deg(pq) = 5 \) and \( \deg(p^2) = 6 \), by @thm-degree-of-product (b): \( \nQ \) is a field (@fd3:thm-rationals-field), so it has no zero divisors. \( \deg(p + q) = 3 \), by the equality case of @thm-degree-of-sum, since \( 3 \ne 2 \). The degree of \( p - x^3 \) is not determined: it is \( 3 \) if \( \operatorname{lc}(p) \ne 1 \), at most \( 2 \) if \( p \) is monic, and \( -\infty \) if \( p = x^3 \). The difference has coefficient \( \operatorname{lc}(p) - 1 \) at position \( 3 \), and that coefficient decides.
:::

## Integral domains

@thm-degree-of-product (b) asks for one property of \( R \): a product of two non-zero elements is non-zero. The integers have it, every field has it, \( \nZ/6\nZ \) lacks it. A ring that has it, and is not the zero ring, gets a name.

*An integral domain is a commutative ring in which a product is zero only when a factor is zero.*

::: {#def-integral-domain}
[Integral Domain]

An **integral domain** is a commutative ring \( R \) with \( 1 \ne 0 \) and **no zero divisors**: **for all** \( a, b \in R \), if \( ab = 0 \), then \( a = 0 \) or \( b = 0 \).
:::

In words: the zero ring is excluded, and the rule "a product vanishes only if a factor vanishes", the rule used to solve \( (x - 1)(x - 2) = 0 \) at school, holds in \( R \). Equivalently, by contraposition: the product of two non-zero elements is non-zero.

::: {#exm-integral-domains}
[Which Rings Are Integral Domains]

Decide which of the following are integral domains: \( \nZ \); a field, and in particular \( \nQ \) and \( \nZ/p\nZ \) for a prime \( p \); \( \nZ/n\nZ \) for \( n \ge 2 \) not prime (@fd2:def-prime); \( \nZ/1\nZ \); and \( \nZ \times \nZ \) with componentwise operations, \( (a, b) + (c, d) \coloneqq (a + c, b + d) \) and \( (a, b)(c, d) \coloneqq (ac, bd) \).
:::

::: {.solution}
*\( \nZ \): yes.* It is a commutative ring with \( 1 \ne 0 \) (@fd3:thm-integers-commutative-ring), and an ordered commutative ring (@fd3:thm-integers-ordered-ring), so \( ab = 0 \) implies \( a = 0 \) or \( b = 0 \) by @fd3:prp-ordered-ring-rules (f).

*A field: yes.* A field has \( 1 \ne 0 \) (@def-field) and no zero divisors (@thm-field-basic-properties (f)). So \( \nQ \) (@fd3:thm-rationals-field) and \( \nZ/p\nZ \) for \( p \) prime (@fd3:thm-integers-mod-prime-field) are integral domains.

*\( \nZ/n\nZ \) for \( n \ge 2 \) not prime: no.* By @fd2:def-prime, \( n \) has a positive divisor \( r \notin \{1, n\} \); write \( n = rs \). As in the proof of @fd3:thm-integers-mod-prime-field (\( \Rightarrow \)), \( 1 < r < n \) and \( 0 < s < n \). Then \( [r] \ne [0] \): otherwise \( n \mid r \) with \( n, r > 0 \), and @fd3:prp-divisibility-rules-integers (e) would give \( n \le r \), against \( r < n \). Likewise \( [s] \ne [0] \). But \( [r][s] = [rs] = [n] = [0] \), by the multiplication of @fd3:def-integers-mod-n-ring (@fd3:thm-quotient-ring-by-ideal (b)).

*\( \nZ/1\nZ \): no.* It has \( [1] = [0] \) (@fd3:thm-integers-mod-n-ring (c)); it is the zero ring.

*\( \nZ \times \nZ \): no.* Each ring axiom holds componentwise, because it holds in each coordinate in \( \nZ \), with zero \( (0, 0) \) and one \( (1, 1) \ne (0, 0) \). But \( (1, 0)(0, 1) = (1 \cdot 0, 0 \cdot 1) = (0, 0) \), with both factors non-zero.

Putting the second and third answers together with @fd3:thm-integers-mod-prime-field: for \( n \ge 2 \), \( \nZ/n\nZ \) is an integral domain if and only if it is a field, if and only if \( n \) is prime.
:::

Now the payoff. Over an integral domain the degree formula holds without exception, and the polynomial ring inherits the property it was built from.

::: {#cor-polynomial-no-zero-divisors}
[Polynomial Rings over Integral Domains]

Let \( R \) be a commutative ring.

::: {.enumerate options="label=(\alph*)"}
1. If \( R \) is an integral domain, \( p, q \in R[x] \) and \( pq = 0 \), then \( p = 0 \) or \( q = 0 \). So \( R[x] \) is an integral domain.
2. (Cancellation) If \( R \) is an integral domain, \( p, q, r \in R[x] \), \( pq = pr \) and \( p \ne 0 \), then \( q = r \).
3. Conversely, if \( R[x] \) is an integral domain, then so is \( R \).
:::
:::

::: {.proof}
*(a)* Let \( p \ne 0 \) and \( q \ne 0 \). Since \( R \) has no zero divisors, @thm-degree-of-product (b) gives \( \deg(pq) = \deg p + \deg q \in \nN \), so \( \deg(pq) \ne -\infty \) and \( pq \ne 0 \). By contraposition, \( pq = 0 \) implies \( p = 0 \) or \( q = 0 \). Moreover \( R[x] \) is a commutative ring (@thm-polynomial-ring-laws (a)), and \( 1 \ne 0 \) in \( R[x] \) because \( 1 \ne 0 \) in \( R \) (@thm-polynomial-ring-laws (b)). So \( R[x] \) is an integral domain.

*(b)* By (F9) of \( R[x] \) and @fd3:prp-ring-algebra (c), \( p(q - r) = pq - pr = 0 \). By (a) and \( p \ne 0 \), \( q - r = 0 \), so \( q = r \) (add \( r \) to both sides, with (F2), (F1), (F4), (F3)).

*(c)* The map \( a \mapsto a x^0 \) from \( R \) to \( R[x] \) is injective and preserves sums, products and \( 1 \) (@thm-polynomial-ring-laws (b)). If \( 1 = 0 \) in \( R \), then the one of \( R[x] \), which is \( 1 x^0 \), equals \( 0 x^0 \), the zero polynomial, against \( 1 \ne 0 \) in \( R[x] \). If \( ab = 0 \) in \( R \), then \( (a x^0)(b x^0) = (ab) x^0 = 0 x^0 \) is the zero polynomial, so \( a x^0 = 0 x^0 \) or \( b x^0 = 0 x^0 \), and by injectivity \( a = 0 \) or \( b = 0 \).
:::

With \( R = \nQ \), @def-degree, @thm-degree-of-product (b) and part (a) are the polynomial algebra that the ordered field \( \nQ(t) \) of @fd3:exm-rational-function-field took on school credit: the degree and the leading coefficient of a polynomial, the rule \( \operatorname{lc}(pq) = \operatorname{lc}(p)\operatorname{lc}(q) \), and the absence of zero divisors in \( \nQ[t] \) (the letter \( t \) there plays the part of our \( x \)). Building fractions \( p/q \) of polynomials is a further step, which this volume does not take.

The cancellation law (b) is what makes it legitimate to "divide both sides by \( p \)" in an identity of polynomials over \( \nZ \), \( \nQ \) or \( \nF_p \). Over \( \nZ/6\nZ \) it fails: \( [2] \cdot [3]x = [0] = [2] \cdot [0] \) with \( [2] \ne [0] \) and \( [3]x \ne [0] \).

## Units of a polynomial ring

The degree also tells us which polynomials can be inverted. If \( pq = 1 \) and degrees add, then \( \deg p + \deg q = 0 \), so both are constants.

::: {#prp-polynomial-units}
[Units of a Polynomial Ring]

Let \( R \) be an integral domain. Then the units of \( R[x] \) are exactly the constants \( a \) with \( a \in R^{\times} \) (@fd3:def-ring-unit): identifying \( a \) with \( a x^0 \), \( (R[x])^{\times} = R^{\times} \).
:::

::: {.proof}
Let \( p \) be a unit of \( R[x] \), with \( pq = 1 \). Since \( 1 \ne 0 \) in \( R[x] \) (@cor-polynomial-no-zero-divisors (a)) and \( 0 \cdot q = 0 \) (@fd3:prp-ring-algebra (b) in the commutative ring \( R[x] \), @thm-polynomial-ring-laws (a)), we have \( p \ne 0 \), and likewise \( q \ne 0 \). By @thm-degree-of-product (b), \( \deg p + \deg q = \deg 1 = 0 \). Two natural numbers with sum \( 0 \) are both \( 0 \), so \( \deg p = \deg q = 0 \): \( p = a x^0 \) and \( q = b x^0 \) with \( a = p_0 \), \( b = q_0 \in R \) (\( 0 \) is admissible for \( p \) and \( q \) by the facts after @def-degree, so @prp-polynomial-sum-of-monomials with \( N = 0 \) applies). Then \( (ab) x^0 = (a x^0)(b x^0) = 1 x^0 \) (@thm-polynomial-ring-laws (b)), so \( ab = 1 \) by injectivity of \( a \mapsto a x^0 \), and \( a \in R^{\times} \).

Conversely, if \( a \in R^{\times} \) with \( ab = 1 \), then \( (a x^0)(b x^0) = (ab) x^0 = 1 x^0 \), so the constant \( a \) is a unit of \( R[x] \).
:::

For a field \( F \), \( F^{\times} \) consists of the non-zero elements (by (F8), and \( 0 \) is not a unit since \( 0 \cdot b = 0 \ne 1 \) by @fd3:prp-ring-algebra (b) and (F6)). So the units of \( F[x] \) are the non-zero constants. Over \( \nZ \), an integral domain (@exm-integral-domains), the units of \( \nZ[x] \) are the constants \( 1 \) and \( -1 \), since \( \nZ^{\times} = \{1, -1\} \) (the examples after @fd3:def-ring-unit): \( 2 \) is a unit of \( \nQ[x] \) and not of \( \nZ[x] \).

::: {.warning}
**Without "integral domain", non-constant units exist.** In \( (\nZ/4\nZ)[x] \),
\[
(1 + [2]x)^2 = 1 + [4]x + [4]x^2 = 1 ,
\]
by the product formula: the coefficients are \( 1 \cdot 1 \), \( 1 \cdot [2] + [2] \cdot 1 \) and \( [2][2] \). So \( 1 + [2]x \) is a unit of degree \( 1 \), its own inverse. The proof above breaks at @thm-degree-of-product (b): \( \operatorname{lc}(p)\operatorname{lc}(p) = [2][2] = [0] \), so degrees do not add.
:::

## Polynomials of bounded degree

Many later arguments fix a bound on the degree: interpolation through \( n + 1 \) points looks for a polynomial of degree at most \( n \), and the linear-algebra companion treats such polynomials as a vector space. Two sets get names.

::: {#def-polynomials-bounded-degree}
[Polynomials of Degree at Most n]

Let \( R \) be a commutative ring and \( n \in \nN \). The set of **polynomials of degree at most \( n \)** is
\[
R[x]_{\le n} \coloneqq \{ p \in R[x] : \deg p \le n \} .
\]
:::

There are two ways to describe this set, and it is worth seeing that they agree. A polynomial has \( \deg p \le n \) exactly when \( p_k = 0 \) for every \( k > n \): for \( p \ne 0 \) by the two facts after @def-degree, and for \( p = 0 \) both hold. By @prp-polynomial-sum-of-monomials, such a \( p \) is the sum \( p_0 + p_1 x + \dots + p_n x^n \) of its first \( n + 1 \) monomials, and every such sum, with \( a_0, \dots, a_n \in R \) arbitrary, has its coefficients beyond \( n \) equal to \( 0 \). So
\[
R[x]_{\le n} = \{ a_0 + a_1 x + \dots + a_n x^n : a_0, \dots, a_n \in R \} .
\]
The first description is about degrees; the second is the one used for computing. Some of the \( a_i \), including \( a_n \), may be \( 0 \), and \( 0 \in R[x]_{\le n} \) (all \( a_i = 0 \); \( -\infty \le n \)).

The set is closed under the operations that do not raise the degree. If \( p, q \in R[x]_{\le n} \), then \( p + q \in R[x]_{\le n} \) by @thm-degree-of-sum; \( -p \in R[x]_{\le n} \), since \( (-p)_k = -p_k = -0 = 0 \) for \( k > n \); and \( ap \in R[x]_{\le n} \) for every constant \( a \), since \( (ap)_k = a p_k = a \cdot 0 = 0 \) for \( k > n \) (@thm-polynomial-ring-laws (d), @fd3:prp-ring-algebra (b)). It is not closed under products: \( x^n \cdot x \notin R[x]_{\le n} \) when \( 1 \ne 0 \).

::: {#exm-elements-of-rx-leq-2}
[Membership in Polynomials of Bounded Degree]

Which of \( 3x^2 - 2x + 1 \), \( 5x + 7 \), \( -4 \), \( 0 \) and \( x^3 - x^3 + x \) lie in \( \nQ[x]_{\le 2} \)? Which lie in \( \nQ[x]_{\le 0} \)?
:::

::: {.solution}
The degrees are \( 2 \), \( 1 \), \( 0 \), \( -\infty \) and \( 1 \): the last expression is the polynomial \( x \), since its coefficient in position \( 3 \) is \( 1 + (-1) = 0 \). An expression containing \( x^3 \) can still have degree below \( 3 \); the degree belongs to the polynomial, not to the way it is written. So all five lie in \( \nQ[x]_{\le 2} \), and exactly \( -4 \) and \( 0 \) lie in \( \nQ[x]_{\le 0} \), the set of constants.
:::

::: {#def-polynomials-exact-degree}
[Polynomials of Degree Exactly n]

Let \( R \) be a commutative ring and \( n \in \nN \). The set of **polynomials of degree exactly \( n \)** is \( R[x]_{= n} \coloneqq \{ p \in R[x] : \deg p = n \} \).
:::

The second description also counts these sets over a finite ring. Over \( \nF_3 = \nZ/3\nZ \), whose elements are \( 0, 1, 2 \) (@fd3:thm-integers-mod-n-ring (b)), \( \nF_3[x]_{\le 1} \) consists of the polynomials \( a_0 + a_1 x \), and distinct pairs \( (a_0, a_1) \) give distinct polynomials, since \( a_0 \) and \( a_1 \) are the coefficients (@prp-polynomial-sum-of-monomials). So it has \( 3 \cdot 3 = 9 \) elements, one for each pair. Those in \( \nF_3[x]_{= 1} \) are the ones with \( a_1 \ne 0 \): \( x, x + 1, x + 2, 2x, 2x + 1, 2x + 2 \), that is \( 3 \cdot 2 = 6 \) of them. The remaining \( 3 \) are the constants \( 0, 1, 2 \).

::: {#exm-comparing-notations}
[Comparing the Two Sets]

Decide whether each of \( x^2 + 1 \), \( 3x - 2 \) and \( 0 \) lies in \( \nQ[x]_{\le 2} \) and in \( \nQ[x]_{= 2} \). Then express \( R[x]_{\le n} \) through \( R[x]_{= n} \) and \( R[x]_{\le n-1} \) for \( n \ge 1 \), and decide whether \( \nQ[x]_{= 2} \) is closed under addition.
:::

::: {.solution}
\( x^2 + 1 \) has degree \( 2 \), so it lies in both sets. \( 3x - 2 \) has degree \( 1 \): it lies in \( \nQ[x]_{\le 2} \) but not in \( \nQ[x]_{= 2} \). The zero polynomial has degree \( -\infty \): it lies in \( \nQ[x]_{\le 2} \) and not in \( \nQ[x]_{= 2} \).

For \( n \ge 1 \), a polynomial of degree at most \( n \) has degree exactly \( n \) or degree at most \( n - 1 \), and not both, so
\[
R[x]_{\le n} = R[x]_{= n} \cup R[x]_{\le n-1} , \qquad R[x]_{= n} \cap R[x]_{\le n-1} = \emptyset .
\]

\( \nQ[x]_{= 2} \) is **not** closed under addition: \( x^2 + x \) and \( -x^2 + 1 \) both have degree \( 2 \), and their sum \( x + 1 \) has degree \( 1 \). It does not contain \( 0 \) either. In the linear-algebra companion, the first of the two sets is a subspace of the space of polynomials and the second is not, for exactly these two reasons.
:::

## Exercises

### A. Check your understanding

::: {#exr-degree-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. In the proof of @thm-degree-of-product, where is the hypothesis "\( R \) has no zero divisors" used?
2. Run the proof of @thm-degree-of-product (a) on \( p = 2x + 1 \) and \( q = 3x^2 + x \), once over \( \nZ \) and once over \( \nZ/6\nZ \): what is \( m + n \), and which element is \( (pq)_{m+n} \)?
3. True or false: \( \deg(p + q) = \max(\deg p, \deg q) \) for all \( p, q \in \nQ[x] \). Justify your answer.
4. Give the idea of the proof of @thm-degree-of-product in two sentences.
5. For which \( n \ge 2 \) is \( (\nZ/n\nZ)[x] \) an integral domain?
:::
:::

::: {.solution}
(a) Only in (b), to conclude that \( \operatorname{lc}(p)\operatorname{lc}(q) \ne 0 \) from \( \operatorname{lc}(p) \ne 0 \) and \( \operatorname{lc}(q) \ne 0 \). Part (a), the vanishing above \( m + n \) and the value at \( m + n \), holds in every commutative ring.

(b) \( m = 1 \), \( n = 2 \), \( m + n = 3 \), and \( (pq)_3 = p_1 q_2 = 2 \cdot 3 \): over \( \nZ \) this is \( 6 \ne 0 \), so \( \deg(pq) = 3 \); over \( \nZ/6\nZ \) it is \( [6] = [0] \), so \( \deg(pq) < 3 \) (in fact \( 2 \), by the warning after the theorem).

(c) False: \( p = x \), \( q = -x \) give \( p + q = 0 \), of degree \( -\infty \), while \( \max(\deg p, \deg q) = 1 \). Equality is only guaranteed when \( \deg p \ne \deg q \) (@thm-degree-of-sum).

(d) In the \( k \)-th coefficient of \( pq \) with \( k \ge m + n \), every term but \( p_m q_n \) has a factor beyond the top of \( p \) or of \( q \), hence vanishes. So the product's top is the product of the tops, and the degree formula holds exactly when that one product in \( R \) is non-zero.

(e) Exactly for \( n \) prime. If \( n \) is prime, \( \nZ/n\nZ \) is an integral domain (@exm-integral-domains), so \( (\nZ/n\nZ)[x] \) is one by @cor-polynomial-no-zero-divisors (a). If \( n \) is not prime, \( \nZ/n\nZ \) is not an integral domain (@exm-integral-domains), so \( (\nZ/n\nZ)[x] \) is not one by @cor-polynomial-no-zero-divisors (c).
:::

### B. Practice

::: {#exr-degree-b1}
[B1: Put the proof in order]

Below are eight lines. Six of them, in a suitable order, form a proof of @cor-polynomial-no-zero-divisors (a), "if \( R \) is an integral domain and \( pq = 0 \) in \( R[x] \), then \( p = 0 \) or \( q = 0 \)"; two are distractors. Write an admissible order, say which other orders are admissible, and say why each distractor fails.

::: {.enumerate options="label=(\roman*)"}
1. \( R \) has no zero divisors, so \( p_m q_n \ne 0 \).
2. By contraposition, \( pq = 0 \) implies \( p = 0 \) or \( q = 0 \).
3. Let \( m \coloneqq \deg p \) and \( n \coloneqq \deg q \), so \( p_m \ne 0 \) and \( q_n \ne 0 \).
4. \( (pq)_{m+n} = \sum_{i=0}^{m+n} p_i q_{m+n-i} \), and this is non-zero because each of its terms is non-zero.
5. Hence \( pq \) has a non-zero coefficient, so \( pq \ne 0 \).
6. Suppose \( p \ne 0 \) and \( q \ne 0 \).
7. By @thm-degree-of-product (a), \( (pq)_{m+n} = p_m q_n \).
8. \( p_m q_n \ne 0 \) because \( R \) is a commutative ring.
:::
:::

::: {.solution}
An admissible order is (vi), (iii), (vii), (i), (v), (ii). Line (vi) must come first: it introduces the assumptions that \( m \) and \( n \) need (the degree of the zero polynomial is \( -\infty \), not a position). Line (iii) must come before (vii) and (i), which use \( m \), \( n \), \( p_m \), \( q_n \). Lines (vii) and (i) do not use each other, so they may come in either order; both must precede (v), which combines them. Line (ii) closes the contrapositive and comes last. So the admissible orders are exactly
\[
\begin{aligned}
&\text{(vi), (iii), (vii), (i), (v), (ii)} \quad \text{and} \\
&\text{(vi), (iii), (i), (vii), (v), (ii)} .
\end{aligned}
\]

Line (iv) fails twice: the terms \( p_i q_{m+n-i} \) with \( i \ne m \) are \( 0 \), not non-zero, and even a sum of non-zero terms can be \( 0 \) (\( 1 + (-1) = 0 \)). Line (viii) gives a false reason: in the commutative ring \( \nZ/6\nZ \), \( [2] \ne [0] \) and \( [3] \ne [0] \) but \( [2][3] = [0] \). The hypothesis that does the work is "no zero divisors", which is line (i).
:::

::: {#exr-degree-b2}
[B2: Units in polynomial rings]

::: {.enumerate options="label=(\alph*)"}
1. Show that for **every** commutative ring \( R \), each unit of \( R \) is a unit of \( R[x] \): \( R^{\times} \subseteq (R[x])^{\times} \).
2. Find the inverse of \( 1 + [3]x \) in \( (\nZ/9\nZ)[x] \).
3. Show that \( 1 + [2]x + [2]x^2 \) is a unit of \( (\nZ/4\nZ)[x] \).
:::

*Hint: in (b), what is \( [3]^2 \) in \( \nZ/9\nZ \)?*
:::

::: {.solution}
(a) The second paragraph of the proof of @prp-polynomial-units uses nothing about \( R \) beyond @thm-polynomial-ring-laws (b): if \( ab = 1 \) in \( R \), then \( (a x^0)(b x^0) = (ab) x^0 = 1 x^0 \), which is the one of \( R[x] \).

(b) By the product formula, \( (1 + [3]x)(1 - [3]x) \) has coefficients \( 1 \), \( [3] - [3] = [0] \) and \( -[3][3] = -[9] = [0] \), so it equals \( 1 \). Since \( -[3] = [6] \), the inverse is \( 1 + [6]x \). (It is unique by @fd3:def-ring-unit.)

(c) Let \( p \coloneqq 1 + [2]x + [2]x^2 \), with coefficients \( 1, [2], [2] \). The coefficients of \( p^2 = pp \) are, by the product formula,
\[
\begin{aligned}
(p^2)_0 &= 1, & (p^2)_1 &= [2] + [2] = [4], \\
(p^2)_2 &= [2] + [4] + [2] = [8], & (p^2)_3 &= [4] + [4] = [8],
\end{aligned}
\]
and \( (p^2)_4 = [2][2] = [4] \). In \( \nZ/4\nZ \), \( [4] = [8] = [0] \), so \( p^2 = 1 \), and \( p \) is a unit, its own inverse. Again \( \nZ/4\nZ \) is not an integral domain, and @prp-polynomial-units does not apply.
:::

::: {#exr-degree-b3}
[B3: Counting polynomials over a finite field]

Let \( p \) be a prime and \( n \in \nN \). How many elements do \( \nF_p[x]_{\le n} \) and \( \nF_p[x]_{= n} \) have?

*Hint: @exr-polynomials-as-sequences-b1.*
:::

::: {.solution}
Since \( \nF_p = \nZ/p\nZ \) has the \( p \) elements \( 0, 1, \dots, p - 1 \) (@fd3:thm-integers-mod-n-ring (b)), the non-zero elements \( 1, \dots, p - 1 \) form a set with \( p - 1 \) elements.

*At most \( n \).* By the description after @def-polynomials-bounded-degree, \( \nF_p[x]_{\le n} \) is the set of polynomials \( q \) with \( q_k = 0 \) for every \( k > n \). By @exr-polynomials-as-sequences-b1 with \( N = n \), \( q \mapsto (q_0, \dots, q_n) \) is a bijection from this set onto \( \nF_p^{\,n+1} \) (for \( n = 0 \), with \( \nF_p^{\,1} \) read as \( \nF_p \), as there). A tuple \( (a_0, \dots, a_n) \) is the same as the function \( \{1, \dots, n + 1\} \to \nF_p \), \( i \mapsto a_{i-1} \), so by @fd2:exr-finite-sets-c2 (b) there are \( p^{n+1} \) of them. So \( \nF_p[x]_{\le n} \) has \( p^{n+1} \) elements.

*Exactly \( n \).* The same bijection maps \( \nF_p[x]_{= n} \) onto the tuples \( (a_0, \dots, a_n) \) with \( a_n \ne 0 \): such a tuple is a pair of an arbitrary \( (a_0, \dots, a_{n-1}) \), \( p^n \) choices as before, and a non-zero \( a_n \), \( p - 1 \) choices. By @fd2:exr-finite-sets-c2 (a), there are \( (p - 1)p^n \) of them. (For \( n = 0 \) these are the \( p - 1 \) non-zero constants, and \( (p - 1)p^0 = p - 1 \).) For example, over \( \nF_2 \) there are \( 2^3 = 8 \) polynomials of degree at most \( 2 \) and \( 1 \cdot 2^2 = 4 \) of degree exactly \( 2 \).
:::

### C. Going deeper

::: {#exr-degree-c1}
[C1: Exit check: polynomial rings over integral domains]

Let \( R \) be a commutative ring. Prove @thm-degree-of-product (a) and (b) (for (b), the equivalence, the leading coefficient, and the case of no zero divisors), and then prove @cor-polynomial-no-zero-divisors (a) and (c).
:::

::: {.solution}
*Degree of a product.* Let \( p, q \ne 0 \), \( m = \deg p \), \( n = \deg q \), so \( p_m \ne 0 \), \( q_n \ne 0 \), and \( p_i = 0 \) for \( i > m \), \( q_j = 0 \) for \( j > n \). Let \( k \ge m + n \) and \( 0 \le i \le k \). If \( i > m \), then \( p_i = 0 \). If \( i \le m \), then \( k - i \ge n \), with equality only when \( k = m + n \) and \( i = m \); otherwise \( q_{k-i} = 0 \). So for \( k > m + n \) every term \( p_i q_{k-i} \) of \( (pq)_k \) is \( 0 \) (@fd3:prp-ring-algebra (b) with (F6)), and \( (pq)_k = 0 \); for \( k = m + n \), every term with \( i \ne m \) is \( 0 \), and the sum is \( p_m q_n \) by (Σ3) of @lem-finite-sums-and-powers. Hence \( \deg(pq) \le m + n \) when \( pq \ne 0 \), and trivially when \( pq = 0 \); if \( p = 0 \) or \( q = 0 \), then \( pq = 0 \) and both sides are \( -\infty \).

If \( p_m q_n \ne 0 \), then \( pq \) has a non-zero coefficient at \( m + n \) and none beyond, so \( \deg(pq) = m + n \) and \( \operatorname{lc}(pq) = p_m q_n \). If \( p_m q_n = 0 \), all coefficients from \( m + n \) on vanish, and \( \deg(pq) < m + n \).

*No zero divisors.* Let \( R \) be an integral domain and \( p, q \ne 0 \). Then \( p_m q_n \ne 0 \), since \( R \) has no zero divisors, so \( pq \) has a non-zero coefficient and \( pq \ne 0 \). Contraposition gives (a); with \( R[x] \) a commutative ring (@thm-polynomial-ring-laws (a)) and \( 1 x^0 \ne 0 x^0 \) because \( 1 \ne 0 \) in \( R \), \( R[x] \) is an integral domain.

*The converse.* Let \( R[x] \) be an integral domain. If \( 1 = 0 \) in \( R \), the one \( 1 x^0 \) of \( R[x] \) is the zero polynomial, a contradiction. If \( ab = 0 \) in \( R \), then \( (a x^0)(b x^0) = (ab) x^0 = 0 \) (@lem-monomial-product (b)), so one factor is the zero polynomial, and its only possibly non-zero coefficient, \( a \) or \( b \), is \( 0 \).

**Marking scheme.** (10 points)

- 3: shows that every coefficient of \( pq \) above \( m + n \) vanishes, treating both cases \( i > m \) and \( i \le m \) of the index argument, and the case \( p = 0 \) or \( q = 0 \) of the inequality.
- 2: shows that \( (pq)_{m+n} = \operatorname{lc}(p)\operatorname{lc}(q) \), with the other terms of that coefficient shown to be \( 0 \).
- 1: derives \( \deg(pq) = \deg p + \deg q \) and \( \operatorname{lc}(pq) = \operatorname{lc}(p)\operatorname{lc}(q) \) from \( \operatorname{lc}(p)\operatorname{lc}(q) \ne 0 \), and that this holds when \( R \) has no zero divisors.
- 1: shows the converse direction of the equivalence: \( \operatorname{lc}(p)\operatorname{lc}(q) = 0 \) gives \( \deg(pq) < m + n \).
- 2: concludes that \( R[x] \) has no zero divisors and \( 1 \ne 0 \) in \( R[x] \).
- 1: proves the converse through the constants.

Fatal errors (0 for the step): "the leading term of \( pq \) is \( \operatorname{lc}(p)\operatorname{lc}(q)x^{m+n} \)" without showing that the other terms of the \( (m + n) \)-th coefficient vanish; using \( \deg(pq) = \deg p + \deg q \) in an arbitrary commutative ring. A proof through the **lowest** non-zero coefficients (as in the repair of @exr-degree-c2) earns the same points for (a) of the corollary, with the index argument mirrored.
:::

::: {#exr-degree-c2}
[C2: Find the error]

Here is an argument.

> **Claim.** If \( R \) is an integral domain, then \( R[x] \) has no zero divisors.
>
> **Proof.** Let \( p, q \in R[x] \) be non-zero. (1) Then \( p_0 \ne 0 \) and \( q_0 \ne 0 \). (2) The constant term of \( pq \) is \( (pq)_0 = p_0 q_0 \). (3) Since \( R \) has no zero divisors, \( p_0 q_0 \ne 0 \). (4) So \( pq \ne 0 \).

Is the claim true? Does the argument prove it? If not, name the first line that fails, say why, give a counterexample to that step, and repair the proof.
:::

::: {.solution}
The claim is true: it is @cor-polynomial-no-zero-divisors (a). The argument does not prove it.

*The failing line is (1).* A non-zero polynomial may have constant term \( 0 \): \( p = x \) is non-zero, with \( p_0 = 0 \). That is a counterexample to the step from "\( p \ne 0 \)" to "\( p_0 \ne 0 \)". The step generalizes from the constants, where it is true, to all polynomials, where no result supports it: it cites a general "fact" that is neither proved nor true, entry (N9) of @fd1:exm-not-allowed-catalogue. Lines (2), (3) and (4) are correct: (2) is the product formula at \( k = 0 \), and (3), (4) follow once (1) is granted.

*Two repairs.* The book's repair looks at the **top** coefficients: with \( m = \deg p \), \( n = \deg q \), @thm-degree-of-product (a) gives \( (pq)_{m+n} = p_m q_n \ne 0 \).

The argument can also be repaired at the **bottom**. Let \( i_0 \) and \( j_0 \) be the least indices with \( p_{i_0} \ne 0 \) and \( q_{j_0} \ne 0 \); they exist because the sets of non-zero positions are non-empty subsets of \( \nN \) (@fd3:prp-integer-least-element, bounded below by \( 0 \)). In \( (pq)_{i_0 + j_0} = \sum_{i=0}^{i_0+j_0} p_i q_{i_0+j_0-i} \), a term with \( i < i_0 \) has \( p_i = 0 \), and a term with \( i > i_0 \) has \( i_0 + j_0 - i < j_0 \), so \( q_{i_0+j_0-i} = 0 \). By (Σ3), \( (pq)_{i_0+j_0} = p_{i_0} q_{j_0} \), which is non-zero since \( R \) has no zero divisors. So \( pq \ne 0 \). This is the index argument of @thm-degree-of-product, mirrored.
:::

<!-- dependency ledger
def-degree (claim): (opening, warning) ([2]x + [1])([3]x^2 + x) = [5]x^2 + x; 6x^3 + 5x^2 + x over Z; coefficients 0, 1, 5, 6 | def-polynomial-ring (cited), arithmetic in Z and Z/6Z (fd3:exm-integers-mod-six cited); verify/ch04/def-degree.py
def-degree (claim): degree exists: S non-empty, bounded above by an admissible N, greatest element | fd3:prp-naturals-embed-integers, fd3:prp-integer-least-element (cited)
def-degree (example): 6x^3 + 5x^2 + x read in Z/5Z is x^3 + x | [6] = [1], [5] = [0] in Z/5Z (fd3:def-integers-mod-n-ring, numerals; numeral convention of exm-elements-of-rx, cited); verify/ch04/def-degree.py
def-degree (example): if 1 = 0 then R = {0} | fd3:prp-ring-algebra (b) (cited), (F7)
def-degree (claim): (why -infty) 0 . q = 0 for every q | fd3:prp-ring-algebra (b) applied coefficientwise, as in the proof of thm-degree-of-product (a)
thm-degree-of-sum (proof): k > M implies k > deg p and k > deg q; max on N u {-infty} | order of N (fd3:thm-omega-order) with the conventions of def-degree
thm-degree-of-product (proof): index arithmetic: k >= m + n, i <= m gives k - i >= n, with equality only if k = m + n and i = m; k - i in N for i <= k | N in Z (fd3:prp-naturals-embed-integers), fd3:thm-omega-arithmetic-laws, fd3:thm-omega-order, ordered-ring rules fd3:prp-ordered-ring-rules (b) in Z
thm-degree-of-product (proof): a sum all of whose terms are 0 is 0 | (Sigma3) of lem-finite-sums-and-powers (b) with j = 0 (cited)
thm-degree-of-product (proof): unit times non-zero is non-zero | fd3:def-ring-unit (cited) with (F5)-(F7), fd3:prp-ring-algebra (b), written out in the proof
thm-degree-of-product (claim): (answer to prompt) part (a) uses only (F1)-(F7), (F9), prp-ring-algebra (b), (Sigma3) of lem-finite-sums-and-powers (b), the conventions of def-degree; "no zero divisors" only in the first sentence of the last paragraph of (b) | meta-claim about the proof on the page; checkable line by line
exm-integral-domains (solution): Z x Z componentwise is a commutative ring | each axiom componentwise from fd3:thm-integers-commutative-ring; stated, one line, as the blueprint allows
exm-integral-domains (solution): n >= 2 not prime gives n = rs with 1 < r < n, 0 < s < n | fd2:def-prime (cited), then as in the proof of fd3:thm-integers-mod-prime-field (=>) (cited); [r][s] = [rs] by fd3:thm-quotient-ring-by-ideal (b) through fd3:def-integers-mod-n-ring (cited)
cor-polynomial-no-zero-divisors (proof): q - r = 0 gives q = r; p(q - r) = pq - pr | (F1)-(F4), (F9), fd3:prp-ring-algebra (c) (cited)
cor-polynomial-no-zero-divisors (claim): R = Q is the polynomial algebra behind fd3:exm-rational-function-field | pays STATUS row F3.9 §02 (polynomial half); prose
cor-polynomial-no-zero-divisors (claim): [2] . [3]x = [0] in (Z/6Z)[x] | def-polynomial-ring with thm-polynomial-ring-laws (d); [6] = [0]; verify/ch04/def-degree.py
prp-polynomial-units (proof): two natural numbers with sum 0 are both 0 | fd3:thm-omega-arithmetic-laws / fd3:thm-omega-order (m <= m + n), used silently
prp-polynomial-units (proof): deg p = 0 gives p = p_0 x^0; 0 . q = 0 in R[x] | prp-polynomial-sum-of-monomials with N = 0 and the facts after def-degree (cited); fd3:prp-ring-algebra (b) in R[x] via thm-polynomial-ring-laws (a) (cited)
prp-polynomial-units (claim): units of Z[x] are 1, -1; 0 is not a unit of a field | Z an integral domain (exm-integral-domains, cited), Z^x = {1, -1} (examples after fd3:def-ring-unit, cited); 0 . b = 0 by fd3:prp-ring-algebra (b), (F6) (cited)
prp-polynomial-units (claim): (warning) (1 + [2]x)^2 = 1 + [4]x + [4]x^2 = 1 in (Z/4Z)[x] | product formula; verify/ch04/prp-polynomial-units.py
def-polynomials-bounded-degree (claim): -0 = 0 | fd3:prp-ring-algebra (a) (uniqueness of negatives, 0 + 0 = 0), used silently
def-polynomials-exact-degree (example): F_3[x]_{<=1} has 3 . 3 = 9 elements, F_3[x]_{=1} has 3 . 2 = 6, 3 constants | fd3:thm-integers-mod-n-ring (b), prp-polynomial-sum-of-monomials (cited); counted by listing; verify/ch04/exr-degree-b3.py
def-polynomials-bounded-degree (claim): interpolation through n + 1 points; the linear-algebra companion treats R[x]_{<=n} as a vector space | prose motivation; interpolation is F4.5's (blueprint ch05.md), no chapter named; nothing depends on it
exm-comparing-notations (claim): in the linear-algebra companion one set is a subspace, the other not | companion (LA1.1), prose pointer; nothing depends on it
exr-degree-a1 (solution): (b) (pq)_3 = 6 resp. [0] | verify/ch04/def-degree.py
exr-degree-b2 (solution): (1 + [3]x)(1 - [3]x) = 1 in Z/9Z; -[3] = [6]; (1 + [2]x + [2]x^2)^2 coefficients 1, [4], [8], [8], [4] | product formula; verify/ch04/exr-degree-b2.py
exr-degree-b3 (solution): n-tuples are functions {1, ..., n+1} -> F_p; counts p^(n+1), (p - 1)p^n; {1, ..., p - 1} has p - 1 elements; n = 0 reads F_p^1 as F_p (convention of exr-polynomials-as-sequences-b1) | fd2:exr-finite-sets-c2 (a), (b) (cited; an exercise citing an earlier exercise), exr-polynomials-as-sequences-b1 (cited), fd3:thm-integers-mod-n-ring (b) restricted to {1, ..., p - 1} (used silently); verify/ch04/exr-degree-b3.py
exr-degree-c2 (solution): least non-zero positions exist | fd3:prp-integer-least-element (cited)
-->
