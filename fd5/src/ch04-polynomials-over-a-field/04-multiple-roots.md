# Roots, Multiplicity, and the Formal Derivative

Over \( \nQ \), the polynomial \( x^4 - 2x^3 + 2x - 1 \) vanishes at \( 1 \) and at \( -1 \), and nowhere else. Yet it has degree \( 4 \), and \( 1 \) behaves like three roots at once: \( x^4 - 2x^3 + 2x - 1 = (x - 1)^3(x + 1) \). This section counts roots properly. It proves that a non-zero polynomial of degree \( n \) has at most \( n \) roots, that a polynomial over an infinite field is determined by its values, and what it means for a root to be repeated; then it shows how to see a repeated root without factoring, through the formal derivative of Section 3.5.

Here the integers have no twin. Section 4.3 followed *Number Systems: From \(\nN\) to \(\nR\)*, Section 3.3 step by step, but an integer cannot be evaluated at a point. The main new tool is one fact from Section 4.1, the factor theorem (@thm-polynomial-remainder-factor): \( c \) is a root of \( f \) if and only if \( x - c \mid f \). Throughout, \( F \) is a field.

## Counting roots

A root of \( f \) gives a factor of degree \( 1 \). Several distinct roots give several factors, and degrees add, so there cannot be too many of them.

::: {#thm-polynomial-root-count}
[Counting Roots]

Let \( F \) be a field, \( f \in F[x] \), \( k \ge 1 \), and let \( c_1, \dots, c_k \in F \) be **distinct** roots of \( f \). Then
\[
(x - c_1)(x - c_2) \cdots (x - c_k) \mid f .
\]
If \( f \ne 0 \), then \( k \le \deg f \). In particular, a non-zero polynomial of degree \( n \) has at most \( n \) distinct roots in \( F \).
:::

::: {.idea}
Peel the roots off one at a time. If \( f = (x - c_1) \cdots (x - c_{k-1}) \, h \), then the next root \( c_k \) must be a root of \( h \): at \( c_k \) the product of the factors \( c_k - c_i \) is non-zero, because the roots are distinct and a field has no zero divisors. Then the factor theorem splits \( x - c_k \) off \( h \). Counting degrees at the end gives \( k \le \deg f \).
:::

::: {.proof}
For \( k \ge 1 \) let \( P_k \coloneqq \prod_{i=1}^{k} (x - c_i) \), the product of a list in \( F[x] \) (the recursion of Section 4.3, after @cor-irreducible-divides-product). We prove "\( P_k \mid f \) for all distinct roots \( c_1, \dots, c_k \) of \( f \)" by @fd1:ax-induction on \( k \ge 1 \) (on \( \omega \), @fd3:cor-omega-identification (b)).

For \( k = 1 \), \( P_1 = x - c_1 \), and \( x - c_1 \mid f \) by @thm-polynomial-remainder-factor (b).

Suppose the claim holds for \( k \), and let \( c_1, \dots, c_{k+1} \) be distinct roots of \( f \). By the claim for \( c_1, \dots, c_k \), \( f = P_k h \) for some \( h \in F[x] \). Evaluating at \( c_{k+1} \) (@thm-evaluation-respects-operations, applied factor by factor along the recursion),
\[
0 = f(c_{k+1}) = (c_{k+1} - c_1)(c_{k+1} - c_2) \cdots (c_{k+1} - c_k) \, h(c_{k+1}) .
\]
Each \( c_{k+1} - c_i \) with \( i \le k \) is non-zero, since the roots are distinct, and a product of non-zero elements of a field is non-zero (@thm-field-basic-properties (g), by induction on the number of factors). So \( h(c_{k+1}) = 0 \) by @thm-field-basic-properties (f). By @thm-polynomial-remainder-factor (b), \( h = (x - c_{k+1}) h_1 \) for some \( h_1 \in F[x] \), and by the recursion
\[
f = P_k (x - c_{k+1}) h_1 = P_{k+1} h_1 .
\]
So \( P_{k+1} \mid f \).

Now let \( f \ne 0 \) and write \( f = P_k h_1 \). Then \( h_1 \ne 0 \), \( P_k \) is monic of degree \( k \) by (L1) of Section 4.3, and \( \deg f = k + \deg h_1 \ge k \) by @thm-degree-of-product (b).
:::

Both hypotheses have a job: "distinct" in the factors \( c_{k+1} - c_i \ne 0 \), and "field" in the step "a product of non-zero elements is non-zero".

::: {.second-reading title="Dropping a hypothesis"}
Without "distinct": \( 1, 1 \) is a list of two roots of \( x - 1 \), but \( (x - 1)^2 \nmid x - 1 \), by degrees (@prp-polynomial-divisibility-rules (d)). Without "field": over the ring \( \nZ/8\nZ \), which has zero divisors, the polynomial \( x^2 - 1 \) of degree \( 2 \) has the four roots \( 1, 3, 5, 7 \), since \( 3^2 - 1 = 8 \), \( 5^2 - 1 = 24 \) and \( 7^2 - 1 = 48 \) are multiples of \( 8 \); there \( (3 - 1)(3 + 1) = 8 = 0 \) with both factors non-zero.
:::

::: {.check}
Can a polynomial over \( \nQ \) of degree \( 3 \) vanish at \( 1, 2, 3 \) and \( 4 \)? Can a polynomial of degree at most \( 3 \)?
:::

::: {.solution}
Not one of degree \( 3 \): it is non-zero, so it has at most \( 3 \) distinct roots (@thm-polynomial-root-count). A polynomial of degree at most \( 3 \) can, but only the zero polynomial, whose degree is \( -\infty \le 3 \).
:::

## Values determine the polynomial

Section 3.4 insisted that a polynomial is not a function: over \( \nF_2 \), \( x^2 + x \) and \( 0 \) have the same values (@exm-polynomial-vs-function-f2). Its warning promised that over a field such as \( \nQ \) the values do determine the polynomial. Counting roots pays that promise.

::: {#thm-polynomial-identity-from-values}
[Polynomials Determined by Values]

Let \( F \) be a field and \( f, g \in F[x] \).

::: {.enumerate options="label=(\alph*)"}
1. Let \( n \in \nN \). If \( \deg f \le n \), \( \deg g \le n \), and \( f(c_i) = g(c_i) \) for \( n + 1 \) distinct elements \( c_0, \dots, c_n \in F \), then \( f = g \).
2. If \( F \) is infinite and \( f(c) = g(c) \) for **every** \( c \in F \), then \( f = g \).
:::
:::

::: {.idea}
Two polynomials that agree at a point differ by a polynomial with a root there. If they agree at more points than their degree allows, the difference has too many roots, so it is \( 0 \). An infinite field has as many points as we need.
:::

::: {.proof}
*(a)* By @thm-degree-of-sum, \( \deg(f - g) \le \max(\deg f, \deg g) \le n \) (the degree of \( -g \) is that of \( g \)). By @thm-evaluation-respects-operations, \( (f - g)(c_i) = f(c_i) - g(c_i) = 0 \), so \( c_0, \dots, c_n \) are \( n + 1 \) distinct roots of \( f - g \). If \( f - g \ne 0 \), @thm-polynomial-root-count gives \( n + 1 \le \deg(f - g) \le n \), which is false. So \( f - g = 0 \).

*(b)* We first find enough distinct elements.

::: {.claim}
An infinite set \( S \) contains, for every \( m \in \nN \), a list of \( m \) distinct elements: an injective function \( \{1, \dots, m\} \to S \).

::: {.proof}
By @fd1:ax-induction on \( m \). For \( m = 0 \) the empty function works. Suppose \( s_1, \dots, s_m \) are distinct elements of \( S \). The set \( A \coloneqq \{s_1, \dots, s_m\} \) has \( m \) elements, through the bijection \( i \mapsto s_i \), so it is finite (@fd2:def-finite). Since \( S \) is infinite (@fd2:def-infinite), \( A \ne S \), and as \( A \subseteq S \), **there is** \( s \in S \) with \( s \notin A \). Then \( s_1, \dots, s_m, s \) are \( m + 1 \) distinct elements of \( S \).
:::
:::

The claim is proved by induction on a statement of the form "there exists a list", and each step takes one element from a non-empty set, once; no sequence of choices is made, so no axiom of choice is used. Now let \( n \coloneqq \max(\deg f, \deg g, 0) \in \nN \). The claim with \( S = F \) and \( m = n + 1 \) gives \( n + 1 \) distinct elements of \( F \), at which \( f \) and \( g \) agree, and (a) gives \( f = g \).
:::

Over \( \nQ \), \( \nR \) and \( \nC \), which are infinite, equality of polynomials and equality of polynomial functions are therefore the same thing. Two polynomials with integer coefficients that agree at every integer are equal too: read them in \( \nQ[x] \), and apply (a) at \( n + 1 \) distinct integers. Part (a) says more, and it says it over every field: \( n + 1 \) values fix a polynomial of degree at most \( n \). A line is fixed by two points, a parabola by three.

::: {.warning}
**Over a finite field, (b) fails.** For a prime \( p \), every \( c \in \nF_p \) satisfies \( c^p = c \) (@thm-fermat-little (a)), so the polynomial \( x^p - x \), which is **not** \( 0 \) (its coefficient of \( x^p \) is \( 1 \)), vanishes at every element of \( \nF_p \). For \( p = 2 \): \( 0^2 - 0 = 0 \) and \( 1^2 - 1 = 0 \), which is @exm-polynomial-vs-function-f2. For \( p = 3 \): the values at \( 0, 1, 2 \) are \( 0 \), \( 0 \) and \( 8 - 2 = 6 = 0 \). There is no conflict with (a): a polynomial of degree \( p \) needs \( p + 1 \) points, and \( \nF_p \) has only \( p \).
:::

::: {#exm-polynomial-function-finite-field}
[Polynomial Functions over a Finite Field]

(a) Show that \( x^3 + 2x \) and \( 0 \) have the same values on \( \nF_3 \), and factor \( x^3 + 2x \) in \( \nF_3[x] \).

(b) Let \( p \) be prime. Show that, in \( \nF_p[x] \),
\[
x^p - x = \prod_{c=0}^{p-1} (x - c) = x(x - 1)(x - 2) \cdots (x - (p - 1)) .
\]
:::

::: {.solution}
(a) In \( \nF_3 \), \( 2 = -1 \), so \( x^3 + 2x = x^3 - x \). Its values at \( 0, 1, 2 \) are \( 0 \), \( 1 - 1 = 0 \) and \( 8 - 2 = 6 = 0 \): the same as those of \( 0 \), although \( x^3 - x \ne 0 \). So \( 0, 1, 2 \) are three distinct roots, and by @thm-polynomial-root-count, \( x(x - 1)(x - 2) \mid x^3 - x \). Both are monic of degree \( 3 \), so the cofactor has degree \( 0 \) and, comparing leading coefficients, is \( 1 \):
\[
x^3 + 2x = x(x - 1)(x - 2) \quad \text{in } \nF_3[x] .
\]
Expanding confirms it: \( x(x - 1)(x - 2) = x^3 - 3x^2 + 2x = x^3 + 2x \), since \( 3 = 0 \).

(b) The elements \( 0, 1, \dots, p - 1 \) of \( \nF_p \) are distinct (@def-field-fp), and each is a root of \( x^p - x \) by the warning. By @thm-polynomial-root-count, the product \( P \) of the \( x - c \) divides \( x^p - x \); \( P \) is monic of degree \( p \) by (L1) of Section 4.3, and so is \( x^p - x \), because \( p \ge 2 > 1 \). As in (a), \( x^p - x = P \cdot u \) with \( \deg u = 0 \), and comparing leading coefficients gives \( u = 1 \).
:::

## Re-centering at a point

To study a polynomial near a point \( c \), it helps to write it in powers of \( x - c \) instead of powers of \( x \). For \( x^2 \) and \( c = 1 \): \( x^2 = 1 + 2(x - 1) + (x - 1)^2 \). Such an expansion always exists and is unique, and it is found by dividing by \( x - c \) repeatedly.

::: {#thm-polynomial-taylor-shift}
[Expansion in Powers of \( x - c \)]

Let \( F \) be a field, \( f \in F[x] \) with \( \deg f = n \ge 0 \), and \( c \in F \).

::: {.enumerate options="label=(\alph*)"}
1. There are **unique** \( b_0, b_1, \dots, b_n \in F \) with
\[
f = \sum_{j=0}^{n} b_j (x - c)^j .
\]
2. \( b_0 = f(c) \), and \( b_n \) is the leading coefficient of \( f \).
3. For every \( h \in F \), \( f(c + h) = \sum_{j=0}^{n} b_j h^j \).
:::
:::

By @thm-degree-of-product (b) and induction on \( j \), each \( (x - c)^j \) is monic of degree \( j \); so a sum \( \sum_{j=0}^{J} d_j (x - c)^j \) with \( d_J \ne 0 \) has degree **exactly** \( J \): the term \( d_J (x - c)^J \) has degree \( J \), every other non-zero term has smaller degree, and @thm-degree-of-sum (with equality when the degrees differ, applied one term at a time) does the rest. The uniqueness half of (a) below uses this fact; part (b) uses its first clause, that \( (x - c)^n \) is monic of degree \( n \).

::: {.idea}
Divide \( f \) by \( x - c \): the remainder is the constant \( f(c) \), and the quotient has degree one less. Expand the quotient the same way, by induction, and multiply back by \( x - c \). For uniqueness, compare degrees: a non-trivial combination of the powers \( (x - c)^j \) has the degree of its highest term, so it is not \( 0 \).
:::

::: {.proof}
*(a), existence.* By @fd1:ax-induction on \( n \), for every \( f \) of degree \( n \). If \( n = 0 \), \( f \) is a non-zero constant \( b_0 = b_0 (x - c)^0 \). Let \( \deg f = n + 1 \). By @thm-polynomial-division-remainder and @thm-polynomial-remainder-factor (a), \( f = (x - c) q + f(c) \) with \( q \in F[x] \). Since \( \deg f \ge 1 > \deg f(c) \), @thm-degree-of-sum gives \( \deg((x - c) q) = n + 1 \), so \( q \ne 0 \) and \( \deg q = n \) (@thm-degree-of-product (b)). By the induction hypothesis, \( q = \sum_{j=0}^{n} d_j (x - c)^j \). Then
\[
f = f(c) + \sum_{j=0}^{n} d_j (x - c)^{j+1} = \sum_{j=0}^{n+1} b_j (x - c)^j ,
\]
with \( b_0 \coloneqq f(c) \) and \( b_{j+1} \coloneqq d_j \), by the distributive law for finite sums (@lem-finite-sums-and-powers (b), (Σ2)) and a shift of the summation index.

*(a), uniqueness.* If \( \sum_{j=0}^{n} b_j (x - c)^j = \sum_{j=0}^{n} b'_j (x - c)^j \), then \( \sum_{j=0}^{n} (b_j - b'_j)(x - c)^j = 0 \) (@lem-finite-sums-and-powers (b), (Σ1), (Σ4)). If some \( b_j - b'_j \) were non-zero, the largest such \( j \) would be the degree of this sum, by the fact before the Idea; but the sum is \( 0 \). So \( b_j = b'_j \) for every \( j \).

*(b)* Evaluate at \( c \) (@thm-evaluation-respects-operations): \( (c - c)^0 = 1 \) and \( (c - c)^j = 0 \) for \( j \ge 1 \), so \( f(c) = b_0 \). The terms with \( j < n \) have degree less than \( n \), and \( b_n (x - c)^n \) has coefficient \( b_n \) at \( x^n \), since \( (x - c)^n \) is monic of degree \( n \); so the coefficient of \( x^n \) in \( f \), its leading coefficient, is \( b_n \).

*(c)* Evaluate at \( c + h \): \( (x - c) \) takes the value \( h \) there, and @thm-evaluation-respects-operations carries sums, products and powers through.
:::

The coefficients \( b_j \) are computed by the existence proof: divide by \( x - c \), keep the remainder as \( b_0 \), divide the quotient by \( x - c \), keep the remainder as \( b_1 \), and so on until the quotient is a constant, which is \( b_n \). The next example runs this.

::: {.check}
Expand \( x^3 \) in powers of \( x - 1 \) over \( \nQ \).
:::

::: {.solution}
\( x^3 = (x - 1)(x^2 + x + 1) + 1 \), \( x^2 + x + 1 = (x - 1)(x + 2) + 3 \), \( x + 2 = (x - 1) \cdot 1 + 3 \). So \( b_0 = 1 \), \( b_1 = 3 \), \( b_2 = 3 \), \( b_3 = 1 \):
\[
x^3 = 1 + 3(x - 1) + 3(x - 1)^2 + (x - 1)^3 .
\]
:::

## Multiplicity

The hook's polynomial \( (x - 1)^3(x + 1) \) is divisible by \( (x - 1)^3 \) and not by \( (x - 1)^4 \). That exponent is what "three roots at once" means.

*The multiplicity of a root counts how many factors \( x - c \) can be split off.*

::: {#def-polynomial-root-multiplicity}
[Multiplicity of a Root]

Let \( F \) be a field, \( f \in F[x] \) **non-zero**, and \( c \in F \). The **multiplicity** of \( c \) in \( f \), written \( \operatorname{mult}_c(f) \), is the **largest** \( m \in \nN \) with \( (x - c)^m \mid f \). The root \( c \) is **simple** if \( \operatorname{mult}_c(f) = 1 \) and **multiple** if \( \operatorname{mult}_c(f) \ge 2 \).
:::

In words: keep dividing \( f \) by \( x - c \) while the division comes out exact; the number of exact divisions is the multiplicity.

*Well defined.* The set \( M \coloneqq \{ m \in \nN : (x - c)^m \mid f \} \) contains \( 0 \), since \( (x - c)^0 = 1 \) divides \( f \). For \( m \in M \), \( m = \deg (x - c)^m \le \deg f \) (@prp-polynomial-divisibility-rules (d)), so \( M \) is bounded above, and it has a greatest element (@fd3:prp-integer-least-element, with \( \nN \subseteq \nZ \)). By the factor theorem (@thm-polynomial-remainder-factor (b)), \( 1 \in M \) exactly when \( f(c) = 0 \), so
\[
\operatorname{mult}_c(f) = 0 \iff f(c) \ne 0 .
\]
For the direction from right to left: if \( f(c) \ne 0 \), no \( m \ge 1 \) lies in \( M \) either, since \( (x - c)^m = (x - c)^{m-1} (x - c) \) (@lem-finite-sums-and-powers (c)), so \( (x - c)^m \mid f \) would give \( x - c \mid f \) (@prp-polynomial-divisibility-rules (b)), that is, \( 1 \in M \). Hence \( M = \{0\} \). A multiplicity \( 0 \) means "not a root". The zero polynomial is excluded because every power of \( x - c \) divides it, and \( M \) would have no greatest element.

**Examples.** In \( \nQ[x] \), \( \operatorname{mult}_1((x - 1)^2) = 2 \): \( (x - 1)^2 \) divides itself, and \( (x - 1)^3 \) does not, by degrees. \( \operatorname{mult}_0(x^2 + x) = 1 \): the value at \( 0 \) is \( 0 \), and \( x^2 \) does not divide \( x^2 + x \), since division with remainder gives \( x^2 + x = x^2 \cdot 1 + x \) with remainder \( x \ne 0 \). And \( \operatorname{mult}_2(x^2 + x) = 0 \), since the value at \( 2 \) is \( 6 \ne 0 \).

The definition asks for a largest exponent, which is awkward to check directly. The next lemma replaces it by a single evaluation.

::: {#lem-polynomial-multiplicity-cofactor}
[Multiplicity through the Cofactor]

Let \( F \) be a field, \( f \in F[x] \) non-zero, \( c \in F \) and \( m \in \nN \).

::: {.enumerate options="label=(\alph*)"}
1. \( \operatorname{mult}_c(f) = m \) **if and only if** \( f = (x - c)^m g \) for some \( g \in F[x] \) with \( g(c) \ne 0 \).
2. Such a \( g \) is unique.
3. If \( f = \sum_{j=0}^{n} b_j (x - c)^j \) is the expansion of @thm-polynomial-taylor-shift, then \( \operatorname{mult}_c(f) \) is the **least** \( j \) with \( b_j \ne 0 \).
:::
:::

::: {.idea}
If the cofactor \( g \) vanished at \( c \), one more factor \( x - c \) would split off; if one more factor split off, cancellation would make \( g \) vanish at \( c \). For (c), the expansion displays the cofactor directly.
:::

::: {.proof}
*(a)* \( (\Rightarrow) \) Let \( m = \operatorname{mult}_c(f) \), so \( f = (x - c)^m g \) for some \( g \). If \( g(c) = 0 \), then \( g = (x - c) g_1 \) (@thm-polynomial-remainder-factor (b)) and \( (x - c)^{m+1} \mid f \), against the maximality of \( m \). So \( g(c) \ne 0 \).

\( (\Leftarrow) \) Let \( f = (x - c)^m g \) with \( g(c) \ne 0 \); then \( m \in M \). Suppose some \( m' > m \) were in \( M \). Then \( (x - c)^{m+1} \) divides \( (x - c)^{m'} \), hence \( f \): say \( f = (x - c)^{m+1} k = (x - c)^m \bigl((x - c) k\bigr) \). Canceling \( (x - c)^m \ne 0 \) (@cor-polynomial-no-zero-divisors (b)) gives \( g = (x - c) k \), so \( g(c) = 0 \), a contradiction. So \( m \) is the largest element of \( M \).

*(b)* If \( (x - c)^m g = (x - c)^m g' \), cancel \( (x - c)^m \ne 0 \).

*(c)* The coefficient \( b_n \) is the leading coefficient of \( f \), so it is non-zero, and the set of \( j \) with \( b_j \ne 0 \) has a least element \( J \) (@fd2:thm-well-ordering). The terms with \( j < J \) vanish, so, taking the factor \( (x - c)^J \) out of the remaining terms,
\[
f = (x - c)^J g , \qquad g \coloneqq \sum_{i=0}^{n-J} b_{J+i} (x - c)^i .
\]
Evaluating at \( c \), as in @thm-polynomial-taylor-shift (b), \( g(c) = b_J \ne 0 \). By (a), \( \operatorname{mult}_c(f) = J \).
:::

The factor \( g \) is the **cofactor** of \( c \) in \( f \). Multiplicities of a product add, because cofactors multiply.

::: {#prp-polynomial-multiplicity-product}
[Multiplicity of a Product]

Let \( F \) be a field, \( f, g \in F[x] \) non-zero and \( c \in F \). Then \( \operatorname{mult}_c(fg) = \operatorname{mult}_c(f) + \operatorname{mult}_c(g) \).
:::

::: {.proof}
Let \( m \coloneqq \operatorname{mult}_c(f) \) and \( n \coloneqq \operatorname{mult}_c(g) \). By @lem-polynomial-multiplicity-cofactor (a), \( f = (x - c)^m u \) and \( g = (x - c)^n v \) with \( u(c) \ne 0 \) and \( v(c) \ne 0 \). Then \( fg = (x - c)^{m+n} uv \) (@lem-finite-sums-and-powers (c), commutativity of \( F[x] \)), \( fg \ne 0 \) (@cor-polynomial-no-zero-divisors (a); a field is an integral domain), and \( (uv)(c) = u(c) v(c) \ne 0 \) (@thm-evaluation-respects-operations, @thm-field-basic-properties (f)). By @lem-polynomial-multiplicity-cofactor (a) again, \( \operatorname{mult}_c(fg) = m + n \).
:::

::: {.check}
Over \( \nQ \), find \( \operatorname{mult}_0(x^5 + x^3) \) and \( \operatorname{mult}_2(x^3 - 4x) \).
:::

::: {.solution}
\( x^5 + x^3 = x^3 (x^2 + 1) \), and the cofactor \( x^2 + 1 \) has value \( 1 \ne 0 \) at \( 0 \), so \( \operatorname{mult}_0 = 3 \) by @lem-polynomial-multiplicity-cofactor (a). \( x^3 - 4x = (x - 2) \cdot x(x + 2) \), with cofactor value \( 2 \cdot 4 = 8 \ne 0 \) at \( 2 \), so \( \operatorname{mult}_2 = 1 \): a simple root.
:::

All roots can now be split off at once. The roots of a non-zero \( f \) form a finite set: otherwise the claim in the proof of @thm-polynomial-identity-from-values (b), applied to the set of roots, would give \( \deg f + 1 \) distinct roots, against @thm-polynomial-root-count. So they can be listed without repetition.

::: {#thm-polynomial-roots-with-multiplicity}
[Splitting Off All Roots]

Let \( F \) be a field and \( f \in F[x] \) non-zero. Let \( c_1, \dots, c_k \in F \), \( k \in \nN \), be the distinct roots of \( f \) in \( F \) (every root of \( f \) in \( F \) is one of them), and \( m_i \coloneqq \operatorname{mult}_{c_i}(f) \). Then
\[
f = (x - c_1)^{m_1} (x - c_2)^{m_2} \cdots (x - c_k)^{m_k} \, g
\]
for some \( g \in F[x] \) with **no** root in \( F \), and \( m_1 + m_2 + \dots + m_k \le \deg f \).
:::

::: {.idea}
Split off the full power of one root with @lem-polynomial-multiplicity-cofactor. The cofactor keeps every other root, with the same multiplicity, because the power just removed does not vanish there; induction on the number of roots does the rest.
:::

::: {.proof}
By @fd1:ax-induction on \( k \), we prove: for every non-zero \( f \) and every list \( c_1, \dots, c_k \) of distinct elements of \( F \) whose entries are exactly the roots of \( f \) in \( F \), the displayed factorization holds with \( g \) rootless. For \( k = 0 \), \( f \) has no root, and \( g \coloneqq f \) works with the empty product \( 1 \).

Assume the statement for \( k \), and let the roots of \( f \) be exactly the distinct \( c_1, \dots, c_{k+1} \). By @lem-polynomial-multiplicity-cofactor (a), \( f = (x - c_{k+1})^{m_{k+1}} g_1 \) with \( g_1(c_{k+1}) \ne 0 \); then \( g_1 \ne 0 \).

The roots of \( g_1 \) are exactly \( c_1, \dots, c_k \). A root \( c \) of \( g_1 \) is a root of \( f \) (@thm-evaluation-respects-operations), and \( c \ne c_{k+1} \), so \( c = c_i \) with \( i \le k \). Conversely, for \( i \le k \), the polynomial \( (x - c_{k+1})^{m_{k+1}} \) has the value \( (c_i - c_{k+1})^{m_{k+1}} \ne 0 \) at \( c_i \) (a power of a non-zero element of a field, @thm-field-basic-properties (g)), so its multiplicity at \( c_i \) is \( 0 \), and @prp-polynomial-multiplicity-product gives
\[
\operatorname{mult}_{c_i}(g_1) = m_i - 0 = m_i \ge 1 .
\]
So \( c_i \) is a root of \( g_1 \), with the same multiplicity as in \( f \).

The statement for \( k \), applied to \( g_1 \) and \( c_1, \dots, c_k \), gives \( g_1 = \prod_{i=1}^{k} (x - c_i)^{m_i} \, g \) with \( g \) rootless. Hence, by commutativity and associativity and the recursion of the product,
\[
f = \Bigl( \prod_{i=1}^{k} (x - c_i)^{m_i} \Bigr) (x - c_{k+1})^{m_{k+1}} \, g = \Bigl( \prod_{i=1}^{k+1} (x - c_i)^{m_i} \Bigr) g .
\]
For the degree, the product is monic of degree \( \sum_i m_i \) by (L1) of Section 4.3, and \( g \ne 0 \), so \( \deg f = \sum_i m_i + \deg g \ge \sum_i m_i \) (@thm-degree-of-product (b)).
:::

So the multiplicities add up to at most \( \deg f \): counted with multiplicity, a non-zero polynomial of degree \( n \) still has at most \( n \) roots. The case where nothing is left over has a name.

::: {#def-splits-over-field}
[Splitting over a Field]

Let \( F \) be a field and \( f \in F[x] \) non-zero of degree \( n \). The polynomial \( f \) **splits over \( F \)** if
\[
f = a (x - a_1)(x - a_2) \cdots (x - a_n)
\]
for some \( a, a_1, \dots, a_n \in F \), repetitions among the \( a_i \) allowed. For \( n = 0 \) this says that \( f = a \) is a non-zero constant.
:::

If \( f \) splits, the multiplicities of its roots add up to **exactly** \( n \): the rootless factor \( g \) of @thm-polynomial-roots-with-multiplicity is then a constant.

::: {.second-reading title="Why nothing is left over"}
In the factorization of @thm-polynomial-roots-with-multiplicity, suppose the rootless \( g \) had degree at least \( 1 \); it would have a monic irreducible factor \( q \) (@lem-polynomial-irreducible-factor), say \( g = q h \). Since \( g \mid f \), also \( q \mid f \) (@prp-polynomial-divisibility-rules (b)). As \( f \ne 0 \), \( a \ne 0 \), and \( q \) divides \( a^{-1} f = (x - a_1)(x - a_2) \cdots (x - a_n) \) (@prp-polynomial-divisibility-rules (c)). By @cor-irreducible-divides-product (c), \( n \ge 1 \) and \( q \mid x - a_i \) for some \( i \). Each \( x - a_i \) is monic and, having degree \( 1 \), irreducible (Section 4.3), so @cor-irreducible-divides-product (d) gives \( q = x - a_i \). Then \( g(a_i) = q(a_i) h(a_i) = 0 \) (@thm-evaluation-respects-operations), against \( g \) rootless. Hence \( g \) is a constant, non-zero as \( f \ne 0 \), and \( \deg f = \sum_i m_i \) (@thm-degree-of-product (b)).
:::

For example, \( x^2 - 2 \) does not split over \( \nQ \): a splitting \( a(x - a_1)(x - a_2) \) would make \( a_1 \) a rational root, and \( a_1^2 = 2 \) is impossible (@fd3:thm-no-rational-square-two). Over \( \nR \) it splits, as \( (x - s)(x + s) \) with \( s \) the non-negative square root of \( 2 \) (@fd3:prp-cof-square-roots).

::: {#exm-polynomial-multiplicity-run}
[Multiplicities by Repeated Division]

Find the roots of \( f \coloneqq x^4 - 2x^3 + 2x - 1 \in \nQ[x] \) with their multiplicities, and expand \( f \) in powers of \( x - 1 \).
:::

::: {.solution}
The value at \( 1 \) is \( 1 - 2 + 2 - 1 = 0 \), so divide by \( x - 1 \), and keep dividing while the remainder is \( 0 \):
\[
\begin{aligned}
x^4 - 2x^3 + 2x - 1 &= (x - 1)(x^3 - x^2 - x + 1) + 0 , \\
x^3 - x^2 - x + 1 &= (x - 1)(x^2 - 1) + 0 , \\
x^2 - 1 &= (x - 1)(x + 1) + 0 , \\
x + 1 &= (x - 1) \cdot 1 + 2 .
\end{aligned}
\]
So \( f = (x - 1)^3 (x + 1) \), and the cofactor \( x + 1 \) has the value \( 2 \ne 0 \) at \( 1 \): \( \operatorname{mult}_1(f) = 3 \) by @lem-polynomial-multiplicity-cofactor (a). At \( -1 \), the cofactor of \( x + 1 \) is \( (x - 1)^3 \), with value \( (-2)^3 = -8 \ne 0 \), so \( \operatorname{mult}_{-1}(f) = 1 \). There are no other roots: \( f(c) = (c - 1)^3 (c + 1) = 0 \) forces \( c = 1 \) or \( c = -1 \) (@thm-field-basic-properties (f)). The multiplicities add up to \( 4 = \deg f \), and \( f \) splits over \( \nQ \), with \( a = 1 \) and \( (a_1, a_2, a_3, a_4) = (1, 1, 1, -1) \).

The remainders \( 0, 0, 0, 2 \) and the last quotient \( 1 \) are the coefficients \( b_0, \dots, b_4 \) of @thm-polynomial-taylor-shift at \( c = 1 \), by its existence proof:
\[
f = 2(x - 1)^3 + (x - 1)^4 ,
\]
and the least \( j \) with \( b_j \ne 0 \) is \( 3 \), the multiplicity, as @lem-polynomial-multiplicity-cofactor (c) says. Expanding \( (x - 1)^3 \bigl((x - 1) + 2\bigr) \) confirms the expansion.
:::

## Repeated roots and the derivative

Finding multiplicities by division needs the root first. The formal derivative detects repeated roots, and repeated factors, without knowing them. Section 3.5 defined it with no limits: for \( f = \sum_k f_k x^k \),
\[
f' \coloneqq \sum_{k \ge 1} (k \cdot f_k) x^{k-1}
\]
(@def-formal-derivative), where \( k \cdot f_k \) is the \( k \)-th multiple and \( k \cdot 1 \) may be \( 0 \) in \( F \). It obeys the rules of calculus (@thm-formal-derivative-rules): it is additive with \( (af)' = af' \) for a constant \( a \); the product rule \( (fg)' = f'g + fg' \) holds; and \( (g^m)' = (m \cdot 1) g^{m-1} g' \), in particular \( \bigl((x - c)^m\bigr)' = (m \cdot 1)(x - c)^{m-1} \) for \( m \ge 1 \). In characteristic \( 0 \), \( f' = 0 \) only for constant \( f \), and \( \deg f' = \deg f - 1 \) when \( \deg f \ge 1 \) (@prp-formal-derivative-zero (a)); in characteristic \( p \) a non-constant polynomial can have derivative \( 0 \): over \( \nF_2 \), \( (x^2)' = (2 \cdot 1) x = 0 \).

At a double root the graph of a real polynomial touches the axis, with slope \( 0 \). The formal version of that picture needs no graph and no slope.

::: {#thm-polynomial-repeated-root-test}
[Repeated Roots and the Derivative]

Let \( F \) be a field, \( f \in F[x] \) non-zero and \( c \in F \).

::: {.enumerate options="label=(\alph*)"}
1. \( c \) is a multiple root of \( f \) **if and only if** \( f(c) = 0 \) and \( f'(c) = 0 \).
2. If \( \operatorname{mult}_c(f) = m \ge 1 \) and \( m \cdot 1 \ne 0 \) in \( F \), then \( f' \ne 0 \) and \( \operatorname{mult}_c(f') = m - 1 \).
:::
:::

::: {.idea}
Write \( f = (x - c)^m g \) with \( g(c) \ne 0 \) and differentiate by the product rule. Both terms contain \( (x - c)^{m-1} \), so \( f' = (x - c)^{m-1} B \) with a bracket \( B \) whose value at \( c \) is \( (m \cdot 1) g(c) \). Everything follows from looking at \( m \) and at that value.
:::

::: {.proof}
Let \( m \coloneqq \operatorname{mult}_c(f) \). If \( m = 0 \), then \( f(c) \ne 0 \), so both sides of (a) are false, and (b) does not apply. Let \( m \ge 1 \), and write \( f = (x - c)^m g \) with \( g(c) \ne 0 \) (@lem-polynomial-multiplicity-cofactor (a)). By @thm-formal-derivative-rules,
\[
\begin{aligned}
f' &= (m \cdot 1)(x - c)^{m-1} g + (x - c)^m g' \\
&= (x - c)^{m-1} B , \qquad B \coloneqq (m \cdot 1) g + (x - c) g' .
\end{aligned}
\]
At \( c \), \( B(c) = (m \cdot 1) g(c) \) (@thm-evaluation-respects-operations).

*(a)* Here \( f(c) = 0 \). If \( m \ge 2 \), then \( m - 1 \ge 1 \) and \( f'(c) = 0^{m-1} B(c) = 0 \). If \( m = 1 \), then \( f' = B \) and \( f'(c) = (1 \cdot 1) g(c) = g(c) \ne 0 \). So \( f'(c) = 0 \) exactly when \( m \ge 2 \), that is, when \( c \) is a multiple root.

*(b)* If \( m \cdot 1 \ne 0 \), then \( B(c) = (m \cdot 1) g(c) \ne 0 \) by @thm-field-basic-properties (f). So \( B \ne 0 \), hence \( f' \ne 0 \) (@cor-polynomial-no-zero-divisors), and @lem-polynomial-multiplicity-cofactor (a) applied to \( f' = (x - c)^{m-1} B \) gives \( \operatorname{mult}_c(f') = m - 1 \).
:::

The hypothesis \( m \cdot 1 \ne 0 \) in (b) is needed. Over \( \nF_3 \), \( f = x^3 \) has \( \operatorname{mult}_0(f) = 3 \), but \( f' = (3 \cdot 1) x^2 = 0 \), whose multiplicity is not even defined. Part (a) holds over every field.

::: {.remark}
**The polynomial \( x^p - x \) has only simple roots.** Over \( \nF_p \), \( (x^p - x)' = (p \cdot 1) x^{p-1} - 1 \) by @thm-formal-derivative-rules, and this is \( -1 \), since \( p \cdot 1 = 0 \) in \( \nF_p \) (@exm-characteristics: \( \operatorname{char} \nF_p = p \)). The derivative \( -1 \) vanishes nowhere, so by (a) no root of \( x^p - x \) is multiple. By @exm-polynomial-function-finite-field (b), every \( c \in \nF_p \) is a root, and each is simple: \( x^p - x \) is the product of the \( p \) distinct factors \( x - c \). This is the fact that Section 3.5's warning set aside.
:::

The same computation, with an irreducible factor in place of \( x - c \), detects repeated factors through a gcd, which the Euclidean algorithm of Section 4.2 computes without factoring anything.

::: {#cor-polynomial-squarefree-gcd}
[Repeated Factors and the Greatest Common Divisor]

Let \( F \) be a field and \( f \in F[x] \) with \( \deg f \ge 1 \).

::: {.enumerate options="label=(\alph*)"}
1. If \( p \in F[x] \) is irreducible and \( p^2 \mid f \), then \( p \mid \gcd(f, f') \). So if \( \gcd(f, f') = 1 \), no irreducible divides \( f \) twice, and \( f \) has no multiple root in \( F \).
2. If \( F \) has characteristic \( 0 \) (@def-characteristic) and \( \gcd(f, f') \ne 1 \), then \( p^2 \mid f \) for some irreducible \( p \).
:::
:::

::: {.idea}
For (a), differentiate \( p^2 g \): every term keeps a factor \( p \). For (b), take an irreducible \( p \) dividing both \( f \) and \( f' \). If \( p \) divided \( f \) only once, \( f = pg \), then \( p \) would divide \( f' - pg' = p'g \), and hence \( p' \), which in characteristic \( 0 \) is non-zero of smaller degree.
:::

::: {.proof}
*(a)* Write \( f = p^2 g \). By @thm-formal-derivative-rules,
\[
f' = (2 \cdot 1) p p' g + p^2 g' = p \bigl( (2 \cdot 1) p' g + p g' \bigr) ,
\]
so \( p \) divides both \( f \) and \( f' \), and hence divides \( \gcd(f, f') \) (@thm-polynomial-bezout (b); \( f \ne 0 \)). If \( \gcd(f, f') = 1 \), this would give \( p \mid 1 \), impossible since \( \deg p \ge 1 \) (@prp-polynomial-divisibility-rules (d)). A multiple root \( c \) would give \( (x - c)^2 \mid f \) with \( x - c \) irreducible.

*(b)* Let \( d \coloneqq \gcd(f, f') \). It is monic (\( f \ne 0 \)) and \( d \ne 1 \), so \( \deg d \ge 1 \), and \( d \) has a monic irreducible divisor \( p \) (@lem-polynomial-irreducible-factor). Then \( p \mid f \) and \( p \mid f' \) (@prp-polynomial-divisibility-rules (b)). As for multiplicities, the set of \( m \in \nN \) with \( p^m \mid f \) contains \( 0 \) and \( 1 \) and is bounded by \( \deg f \) (\( m \le m \deg p = \deg p^m \)); let \( m \ge 1 \) be its greatest element and write \( f = p^m g \). Then \( p \nmid g \), since otherwise \( p^{m+1} \mid f \).

Suppose \( m = 1 \). Then \( f' = p' g + p g' \), and \( p \) divides \( f' \) and \( p g' \), so \( p \mid f' - p g' = p' g \) (@prp-polynomial-divisibility-rules (c)). By @cor-irreducible-divides-product (b), \( p \mid p' \) or \( p \mid g \), and \( p \nmid g \). But \( F \) has characteristic \( 0 \) and \( \deg p \ge 1 \), so \( p' \ne 0 \) and \( \deg p' = \deg p - 1 < \deg p \) (@prp-formal-derivative-zero (a)); then \( p \nmid p' \) by @prp-polynomial-divisibility-rules (d). This contradiction shows \( m \ge 2 \), and \( p^2 \mid f \).
:::

Characteristic \( 0 \) is used once, at \( \deg p' = \deg p - 1 \). Over \( \nQ \), a polynomial \( f \) therefore has a repeated irreducible factor exactly when \( \gcd(f, f') \ne 1 \), and that question is answered by the Euclidean algorithm (@thm-euclidean-algorithm-polynomials) with no factoring at all.

::: {.check}
Is \( 1 \) a multiple root of \( x^3 - 3x + 2 \in \nQ[x] \)?
:::

::: {.solution}
Yes. \( f(1) = 1 - 3 + 2 = 0 \), \( f' = 3x^2 - 3 \) and \( f'(1) = 0 \), so @thm-polynomial-repeated-root-test (a) applies. Indeed \( x^3 - 3x + 2 = (x - 1)^2 (x + 2) \).
:::

## Exercises

### A. Check your understanding

::: {#exr-multiple-roots-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Find \( \operatorname{mult}_1 \) and \( \operatorname{mult}_{-1} \) of \( x^4 - 2x^3 + 2x - 1 \in \nQ[x] \).
2. In \( \nF_3[x] \), let \( f = x^3 \). Is \( 0 \) a multiple root by the test of @thm-polynomial-repeated-root-test (a)? Does part (b) apply?
3. True or false: a polynomial over \( \nQ \) of degree at most \( 2 \) that vanishes at \( 1, 2, 3 \) is the zero polynomial.
4. True or false: a polynomial over \( \nF_2 \) that vanishes at every element of \( \nF_2 \) is the zero polynomial.
:::
:::

::: {.solution}
(a) \( 3 \) and \( 1 \) (@exm-polynomial-multiplicity-run).

(b) Yes: \( f(0) = 0 \) and \( f' = (3 \cdot 1) x^2 = 0 \), so \( f'(0) = 0 \), and \( 0 \) is a multiple root (its multiplicity is \( 3 \)). Part (b) does not apply: \( m = 3 \) and \( 3 \cdot 1 = 0 \) in \( \nF_3 \); indeed \( f' = 0 \), and its multiplicity is not \( 2 \), it is not defined.

(c) True: a non-zero polynomial of degree at most \( 2 \) has at most \( 2 \) distinct roots (@thm-polynomial-root-count), or @thm-polynomial-identity-from-values (a) with \( n = 2 \) and \( g = 0 \).

(d) False: \( x^2 + x \ne 0 \) vanishes at \( 0 \) and \( 1 \) (@exm-polynomial-vs-function-f2). Part (b) of @thm-polynomial-identity-from-values needs an infinite field.
:::

### B. Practice

::: {#exr-multiple-roots-b1}
[B1: Put the proof in order]

The following lines contain a proof of the divisibility part of @thm-polynomial-root-count, shuffled, together with two lines that do not belong. Write the seven correct lines in an order that makes a proof, say which other orders are also admissible, and say why each of the other two lines fails.

(i) We use induction on \( k \); for \( k = 1 \), \( x - c_1 \mid f \) by the factor theorem.

(ii) Assume the claim for every list of \( k - 1 \) distinct roots, and let \( c_1, \dots, c_k \) be distinct roots of \( f \).

(iii) Write \( f = (x - c_1) \cdots (x - c_{k-1}) \, h \).

(iv) Evaluate at \( c_k \): \( 0 = (c_k - c_1) \cdots (c_k - c_{k-1}) \, h(c_k) \).

(v) Each \( c_k - c_i \), \( i < k \), is non-zero, since the roots are distinct.

(v′) Each \( c_k - c_i \), \( i < k \), is non-zero, since \( c_k \ne 0 \).

(vi) A product of non-zero elements of a field is non-zero, so \( h(c_k) = 0 \).

(vi′) \( h(c_k) = 0 \), because \( f(c_k) = 0 \).

(vii) By the factor theorem, \( h = (x - c_k) h_1 \), so \( f = (x - c_1) \cdots (x - c_k) \, h_1 \).
:::

::: {.solution}
An admissible order is (i), (ii), (iii), (iv), (v), (vi), (vii):

> We use induction on \( k \); for \( k = 1 \), \( x - c_1 \mid f \) by the factor theorem. Assume the claim for every list of \( k - 1 \) distinct roots, and let \( c_1, \dots, c_k \) be distinct roots of \( f \). Write \( f = (x - c_1) \cdots (x - c_{k-1}) h \). Evaluate at \( c_k \): \( 0 = (c_k - c_1) \cdots (c_k - c_{k-1}) h(c_k) \). Each \( c_k - c_i \), \( i < k \), is non-zero, since the roots are distinct. A product of non-zero elements of a field is non-zero, so \( h(c_k) = 0 \). By the factor theorem, \( h = (x - c_k) h_1 \), so \( f = (x - c_1) \cdots (x - c_k) h_1 \).

Lines (i) and (ii) set up the induction and come first, in that order; (iii) uses the hypothesis of (ii). Line (v) uses only the distinctness from (ii), so it may come anywhere after (ii) and before (vi); in particular (iv) and (v) may be exchanged, and (v) may even precede (iii). Line (vi) needs both (iv) and (v), and (vii) needs (vi) and (iii). So the admissible orders are: (i), (ii), then (iii), (iv), (v) with (iv) after (iii) and (v) anywhere among them, then (vi), (vii).

The distractor (v′) gives a wrong reason: \( c_k = 0 \) is allowed, and \( c_k \ne 0 \) says nothing about \( c_k - c_i \). The distractor (vi′) skips the cancellation: \( f(c_k) = 0 \) only says that the product in (iv) is \( 0 \), and passing to \( h(c_k) = 0 \) needs both (v) and the absence of zero divisors. Over a ring with zero divisors the step fails: over \( \nZ/8\nZ \), \( x^2 - 1 = (x - 1)(x + 1) \) has the root \( 3 \), yet neither factor vanishes at \( 3 \).
:::

::: {#exr-multiple-roots-b2}
[B2: Expansions at a point]

::: {.enumerate options="label=(\alph*)"}
1. Expand \( x^3 - 2x + 5 \in \nQ[x] \) in powers of \( x - 1 \).
2. Find \( \operatorname{mult}_{-2}(x^3 - 3x + 2) \) from the first two coefficients of an expansion in powers of \( x + 2 \).
:::
:::

::: {.solution}
(a) Divide by \( x - 1 \) three times:
\[
\begin{aligned}
x^3 - 2x + 5 &= (x - 1)(x^2 + x - 1) + 4 , \\
x^2 + x - 1 &= (x - 1)(x + 2) + 1 , \\
x + 2 &= (x - 1) \cdot 1 + 3 .
\end{aligned}
\]
By the existence proof of @thm-polynomial-taylor-shift, \( x^3 - 2x + 5 = 4 + (x - 1) + 3(x - 1)^2 + (x - 1)^3 \). Expanding the right side gives back \( x^3 - 2x + 5 \).

(b) Here \( c = -2 \) and \( x - c = x + 2 \). First \( x^3 - 3x + 2 = (x + 2)(x^2 - 2x + 1) + 0 \), so \( b_0 = 0 \); then \( x^2 - 2x + 1 = (x + 2)(x - 4) + 9 \), so \( b_1 = 9 \ne 0 \). By @lem-polynomial-multiplicity-cofactor (c), \( \operatorname{mult}_{-2} = 1 \): \( -2 \) is a simple root.
:::

::: {#exr-multiple-roots-b3}
[B3: Functions on a finite field]

Let \( p \) be prime and \( f, g \in \nF_p[x] \). Prove that \( f(c) = g(c) \) for every \( c \in \nF_p \) if and only if \( x^p - x \mid f - g \). Then find a polynomial of degree less than \( 5 \) with the same values on \( \nF_5 \) as \( x^7 + x \).
:::

::: {.solution}
\( (\Leftarrow) \) If \( f - g = (x^p - x) h \), then for \( c \in \nF_p \), \( f(c) - g(c) = (c^p - c) h(c) = 0 \), since \( c^p = c \) (@thm-fermat-little (a)).

\( (\Rightarrow) \) If \( f \) and \( g \) agree on \( \nF_p \), then \( 0, 1, \dots, p - 1 \) are \( p \) distinct roots of \( f - g \), so \( \prod_{c=0}^{p-1} (x - c) \mid f - g \) by @thm-polynomial-root-count, and that product is \( x^p - x \) (@exm-polynomial-function-finite-field (b)).

For \( p = 5 \): \( x^7 = x^2 \cdot x^5 \), and \( x^7 - x^3 = x^2 (x^5 - x) \), so \( (x^7 + x) - (x^3 + x) = x^2 (x^5 - x) \) is a multiple of \( x^5 - x \). By the first part, \( x^3 + x \) has the same values as \( x^7 + x \) on \( \nF_5 \), and its degree is \( 3 < 5 \).
:::

### C. Going deeper

::: {#exr-multiple-roots-c1}
[C1: The coefficients as derivatives]

Let \( F \) be a field of characteristic \( 0 \), \( f \in F[x] \) of degree \( n \ge 0 \), \( c \in F \), and \( f = \sum_{j=0}^{n} b_j (x - c)^j \) as in @thm-polynomial-taylor-shift. Prove that
\[
b_j = \frac{f^{(j)}(c)}{j! \cdot 1} \qquad (0 \le j \le n) ,
\]
where \( f^{(j)} \) is the \( j \)-th formal derivative (@def-formal-derivative). Check the formula on the expansion of Exercise B2 (a) at \( j = 2 \).
:::

::: {.solution}
[Hint 1]

Compute the \( j \)-th derivative of \( (x - c)^i \) first.
:::

::: {.solution}
[Hint 2]

By induction on \( j \), \( \bigl((x - c)^i\bigr)^{(j)} = \bigl( (i(i - 1) \cdots (i - j + 1)) \cdot 1 \bigr) (x - c)^{i-j} \) for \( j \le i \), and \( 0 \) for \( j > i \).
:::

::: {.solution}
*The derivatives of the powers.* We prove the formula of Hint 2 by @fd1:ax-induction on \( j \), for all \( i \). For \( j = 0 \) the coefficient is the empty product \( 1 \). Suppose it holds for \( j \). If \( j + 1 \le i \), then \( i - j \ge 1 \) and, by @thm-formal-derivative-rules (a) and (c),
\[
\bigl((x - c)^i\bigr)^{(j+1)} = \bigl( (i \cdots (i - j + 1)) \cdot 1 \bigr) \bigl( (i - j) \cdot 1 \bigr) (x - c)^{i-j-1} ,
\]
and \( (u \cdot 1)(v \cdot 1) = (uv) \cdot 1 \) (@lem-integer-multiples (b)) gives the coefficient \( (i \cdots (i - j)) \cdot 1 \). If \( j + 1 = i + 1 \), the \( i \)-th derivative is the constant \( (i! \cdot 1) \), whose derivative is \( 0 \); and the derivative of \( 0 \) is \( 0 \) for larger \( j \).

*The coefficients.* Since the derivative is additive with \( (af)' = af' \) for constants \( a \) (@thm-formal-derivative-rules (a)), so is the \( j \)-th derivative (induction on \( j \)), and
\[
f^{(j)} = \sum_{i=j}^{n} b_i \bigl( (i \cdots (i - j + 1)) \cdot 1 \bigr) (x - c)^{i-j} .
\]
At \( x = c \), every term with \( i > j \) vanishes, and the term \( i = j \) is \( b_j (j! \cdot 1) \). So \( f^{(j)}(c) = (j! \cdot 1) b_j \). In characteristic \( 0 \), \( j! \cdot 1 \ne 0 \) (@def-characteristic, as \( j! \ge 1 \)), and dividing gives the formula.

*Check.* For \( f = x^3 - 2x + 5 \), \( f'' = 6x \) and \( f''(1) = 6 \), so \( b_2 = 6/2 = 3 \), as in Exercise B2 (a).
:::

::: {#exr-multiple-roots-c2}
[C2: Repeated factors through the gcd]

::: {.enumerate options="label=(\alph*)"}
1. Using only \( \gcd(f, f') \), decide whether \( f \coloneqq x^4 - 2x^3 + 2x - 1 \in \nQ[x] \) has a repeated irreducible factor.
2. Over \( \nF_2 \), let \( f \coloneqq x^4 + 1 \). Compute \( f' \) and \( \gcd(f, f') \), and explain why part (b) of @cor-polynomial-squarefree-gcd does not apply.
:::
:::

::: {.solution}
(a) \( f' = 4x^3 - 6x^2 + 2 \). The Euclidean algorithm (@thm-euclidean-algorithm-polynomials):
\[
\begin{aligned}
f &= \Bigl( \tfrac{1}{4} x - \tfrac{1}{8} \Bigr) f' - \tfrac{3}{4} (x^2 - 2x + 1) , \\
f' &= \Bigl( -\tfrac{3}{4} (x^2 - 2x + 1) \Bigr) \Bigl( -\tfrac{8}{3} (2x + 1) \Bigr) + 0 .
\end{aligned}
\]
The last non-zero remainder is \( -\tfrac{3}{4}(x^2 - 2x + 1) \), so \( \gcd(f, f') = x^2 - 2x + 1 \ne 1 \). As \( \nQ \) has characteristic \( 0 \), @cor-polynomial-squarefree-gcd (b) says that \( f \) has a repeated irreducible factor. (Indeed \( f = (x - 1)^3 (x + 1) \), @exm-polynomial-multiplicity-run.)

(b) \( f' = (4 \cdot 1) x^3 = 0 \) in \( \nF_2 \). Then \( \langle f, 0 \rangle = \langle f \rangle \), whose monic generator is \( f \) itself, so \( \gcd(f, f') = f = x^4 + 1 \ne 1 \) (@thm-polynomial-bezout (c)). Part (b) of the corollary assumes characteristic \( 0 \), and \( \nF_2 \) has characteristic \( 2 \) (@def-characteristic: \( 1 \ne 0 \), \( 2 \cdot 1 = 0 \)). Its proof uses that hypothesis at \( \deg p' = \deg p - 1 \), which fails in characteristic \( 2 \): \( (x^2 + 1)' = 0 \). Here the conclusion happens to hold anyway, since \( x^4 + 1 = (x + 1)^4 \) in \( \nF_2 \), but it is not given by the corollary; the gcd \( f \) records only that \( f' = 0 \).
:::

<!-- dependency ledger
thm-polynomial-root-count (proof): products of lists in F[x] by the recursion; P_k monic of degree k | (L1) of Section 4.3 (03-irreducible-factorization, "Two facts about products of lists"), cited by name; lem-finite-sums-and-powers (a)
thm-polynomial-root-count (proof): evaluation of a product of a list is the product of the values | thm-evaluation-respects-operations, induction on the length along the recursion, stated in the proof
thm-polynomial-root-count (proof): a product of a list of non-zero field elements is non-zero | thm-field-basic-properties (g), induction on the number of factors, stated in the proof
thm-polynomial-root-count (claim): (aftermath) x^2 - 1 has the roots 1, 3, 5, 7 in Z/8Z; (3 - 1)(3 + 1) = 8 | arithmetic mod 8 (fd3 thm-integers-mod-n-ring); verify/ch04/thm-polynomial-root-count.py
thm-polynomial-identity-from-values (proof): deg(-g) = deg g | def-degree (coefficients of -g are -g_k, nonzero iff g_k nonzero), used silently
thm-polynomial-identity-from-values (proof): max(deg f, deg g, 0) in N | def-degree conventions (-infinity < n), used silently
thm-polynomial-identity-from-values (claim): (aftermath) Q, R, C are infinite | N infinite (fd2:exm-hilbert-hotel), N inside Q inside R inside C through the embeddings (fd3:prp-naturals-embed-integers, fd3:prp-integers-embed-rationals, fd3:thm-rational-embedding, prp-reals-embed-complex), a set with an infinite subset is infinite (fd2:prp-subset-finite, contrapositive), used silently
thm-polynomial-identity-from-values (claim): (aftermath) integer polynomials read in Q[x] | Z inside Q (fd3:prp-integers-embed-rationals) coefficientwise: equality in Q[x] gives equality in Z[x], and values at integers are unchanged; the integers 0, ..., n are n + 1 distinct points, used silently
thm-polynomial-identity-from-values (claim): no choice used in the inner induction | one existential instantiation per step of an induction on an existential statement (fd1 F1.4 rules, prose only)
thm-polynomial-identity-from-values (claim): (warning) values of x^3 - x on F_3; 0^2 - 0, 1^2 - 1 in F_2 | arithmetic mod p; verify/ch04/exm-polynomial-function-finite-field.py
exm-polynomial-function-finite-field (example): (a) values and factorization over F_3; (b) x^p - x = prod (x - c) for p <= 7 | arithmetic mod p; verify/ch04/exm-polynomial-function-finite-field.py
exm-polynomial-function-finite-field (example): x^p - x monic of degree p since p >= 2 | thm-degree-of-sum (degrees p and 1 differ), used silently
thm-polynomial-taylor-shift (claim): (x - c)^j monic of degree j; a sum with d_J != 0 as top term has degree J | thm-degree-of-product (b), thm-degree-of-sum (cited), induction stated in the text
thm-polynomial-taylor-shift (proof): (x - c) sum d_j (x - c)^j = sum d_j (x - c)^{j+1}; index shift sum_{j=0}^{n} u_{j+1} + u_0 = sum_{j=0}^{n+1} u_j | lem-finite-sums-and-powers (b) (Sigma2) (cited), (c) power law; index shift by induction on n from the recursion of fd2:def-sum-product (template), used silently
thm-polynomial-taylor-shift (proof): 0^j = 0 for j >= 1 | lem-finite-sums-and-powers (c) and fd3:prp-ring-algebra (b), used silently
thm-polynomial-taylor-shift (claim): (check) expansion of x^3 at 1: 1, 3, 3, 1 | division; verify/ch04/thm-polynomial-taylor-shift.py
def-polynomial-root-multiplicity (claim): N inside Z; a bounded non-empty set has a greatest element | fd3:prp-integer-least-element (cited), fd3 prp-naturals-embed-integers, used silently
def-polynomial-root-multiplicity (claim): deg (x - c)^m = m | thm-degree-of-product (b), as in thm-polynomial-taylor-shift's lead-in
def-polynomial-root-multiplicity (claim): f(c) != 0 gives M = {0}: (x - c)^m = (x - c)^{m-1}(x - c) | lem-finite-sums-and-powers (c), prp-polynomial-divisibility-rules (b) (cited)
def-polynomial-root-multiplicity (example): mult_0(x^2 + x) = 1 via x^2 + x = x^2 * 1 + x, remainder x != 0 | thm-polynomial-division-remainder (uniqueness of the remainder), used silently; verify/ch04/lem-polynomial-multiplicity-cofactor.py
def-polynomial-root-multiplicity (example): mult_1((x - 1)^2) = 2; mult_0(x^2 + x) = 1; value 6 at 2 | arithmetic in Q; verify/ch04/lem-polynomial-multiplicity-cofactor.py
lem-polynomial-multiplicity-cofactor (proof): (x - c)^{m+1} divides (x - c)^{m'} for m' > m | power law lem-finite-sums-and-powers (c), used silently
lem-polynomial-multiplicity-cofactor (proof): (c) taking (x - c)^J out of sum_{j >= J} b_j (x - c)^j, index shift | lem-finite-sums-and-powers (b), (c); index shift as in thm-polynomial-taylor-shift, used silently
prp-polynomial-multiplicity-product (proof): fg = (x - c)^m (x - c)^n uv = (x - c)^{m+n} uv; fg != 0 | lem-finite-sums-and-powers (c), commutativity of F[x], cor-polynomial-no-zero-divisors (a) (cited); a field is an integral domain (fd3 field definition), used silently
lem-polynomial-multiplicity-cofactor (claim): (check) x^5 + x^3 = x^3(x^2 + 1), x^3 - 4x = (x - 2) x (x + 2), cofactor value 8 | arithmetic in Q; verify/ch04/lem-polynomial-multiplicity-cofactor.py
thm-polynomial-roots-with-multiplicity (claim): the roots of f != 0 form a finite set, listable without repetition | the claim inside thm-polynomial-identity-from-values (b) with thm-polynomial-root-count, stated in the lead-in; fd2:def-finite
thm-polynomial-roots-with-multiplicity (proof): the product of the list ((x - c_i)^{m_i}) is monic of degree sum m_i | (L1) of Section 4.3 with deg (x - c)^m = m; cited by name
thm-polynomial-roots-with-multiplicity (proof): mult_{c_i}(g_1) = m_i - 0 | prp-polynomial-multiplicity-product (cited); subtraction in N, used silently
def-splits-over-field (claim): multiplicities of a split polynomial add up to n | second-reading fold after the definition: lem-polynomial-irreducible-factor, prp-polynomial-divisibility-rules (b), (c), cor-irreducible-divides-product (c), (d), thm-evaluation-respects-operations, thm-degree-of-product (b) (cited); x - a_i irreducible (degree 1, example after def-irreducible-over-field, Section 4.3), cited by section; a^{-1} a (x - a_1)...(x - a_n) = (x - a_1)...(x - a_n) by associativity, used silently
def-splits-over-field (example): x^2 - 2 splits over R as (x - s)(x + s) | fd3:prp-cof-square-roots in R (complete ordered field, fd3:thm-reals-complete-ordered-field), (x - s)(x + s) = x^2 - s^2; Q in R ledger line of the blueprint
exm-polynomial-multiplicity-run (example): the four divisions; (-2)^3 = -8; f = 2(x - 1)^3 + (x - 1)^4 | arithmetic in Q; verify/ch04/exm-polynomial-multiplicity-run.py
thm-polynomial-repeated-root-test (proof): (1 * 1) g(c) = g(c); 0^{m-1} = 0 for m >= 2 | lem-integer-multiples (c) (1 * a = a), lem-finite-sums-and-powers (c); used silently
thm-polynomial-repeated-root-test (claim): (aftermath) x^3 in F_3, f' = (3 * 1) x^2 = 0 | def-formal-derivative, arithmetic mod 3; verify/ch04/thm-polynomial-repeated-root-test.py
thm-polynomial-repeated-root-test (claim): (remark) (x^p - x)' = (p * 1) x^{p-1} - 1 = -1; p * 1 = 0 in F_p | thm-formal-derivative-rules (cited); x' = 1 (def-formal-derivative); p * 1 = 0 in F_p (exm-characteristics, char F_p = p; F5.2); verify/ch04/thm-polynomial-repeated-root-test.py
cor-polynomial-squarefree-gcd (proof): the set {m : p^m | f} has a greatest element; m <= m deg p = deg p^m | as for def-polynomial-root-multiplicity: fd3:prp-integer-least-element; thm-degree-of-product (b) by induction on m; prp-polynomial-divisibility-rules (d)
cor-polynomial-squarefree-gcd (proof): x - c is irreducible (degree 1) | example after def-irreducible-over-field (Section 4.3), used silently
cor-polynomial-squarefree-gcd (claim): (check) f(1) = 0, f'(1) = 0, (x - 1)^2 (x + 2) = x^3 - 3x + 2 | arithmetic in Q; verify/ch04/cor-polynomial-squarefree-gcd.py
exr-multiple-roots-b1 (solution): admissible orders; Z/8Z root 3 of (x - 1)(x + 1) | the solution's own analysis; arithmetic mod 8
exr-multiple-roots-b2 (solution): the divisions at 1 and at -2 | arithmetic in Q; verify/ch04/exr-multiple-roots-b2.py
exr-multiple-roots-b3 (solution): x^7 - x^3 = x^2 (x^5 - x) | ring arithmetic; verify/ch04/exr-multiple-roots-b3.py
exr-multiple-roots-c1 (solution): j-th derivative additive; j! * 1 != 0 in characteristic 0; the empty product 1 | thm-formal-derivative-rules (a), lem-integer-multiples (b) (cited); def-characteristic (j! >= 1 a positive integer); fd2:def-sum-product for j! (template); f'' = 6x, f''(1) = 6; verify/ch04/exr-multiple-roots-c1.py
exr-multiple-roots-c2 (solution): Euclidean run for f, f'; gcd = x^2 - 2x + 1; (x + 1)^4 = x^4 + 1 in F_2 | arithmetic in Q and F_2; verify/ch04/exr-multiple-roots-c2.py
-->
