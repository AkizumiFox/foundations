# Division with Remainder

*Number Systems: From \( \nN \) to \( \nR \)*, Section 4.1 divided \( -17 \) by \( 5 \) and kept the remainder \( 3 \): a quotient times the divisor, plus something **smaller** than the divisor. Chapter 4 built the ring \( F[x] \) of polynomials over a field and gave every non-zero polynomial a degree. For polynomials, "smaller" will mean "of smaller degree". For instance, in \( \nQ[x] \),
\[
x^4 + 2x^3 - x + 3 = (x^2 + x)(x^2 + x - 1) + 3 ,
\]
and the leftover \( 3 \) has degree \( 0 \), below the degree \( 2 \) of \( x^2 + x - 1 \). Three questions are open. Why can one always go on until the degree drops below that of the divisor? Why is the answer unique? And where does it matter that the coefficients lie in a **field**? This section answers all three, and then uses the answer to connect a root of a polynomial with a factor of degree \( 1 \).

Throughout the chapter, \( F \) is a field (@def-field), and \( F[x] \) is the ring of polynomials over \( F \) (@def-polynomial-ring), a commutative ring by @thm-polynomial-ring-laws (a). A field is an integral domain (@exm-integral-domains), so the results of Chapter 4 stated for integral domains apply to \( F[x] \). We use the degree \( \deg p \) and the leading coefficient \( \operatorname{lc}(p) \) of @def-degree, with \( \deg 0 = -\infty \), and the conventions \( -\infty < n \) and \( -\infty + n = -\infty \) for \( n \in \nN \) that come with it. A constant \( a \in F \) is identified with the polynomial \( a x^0 \) (@thm-polynomial-ring-laws (b)), and \( (ap)_k = a p_k \) for a constant \( a \) (@thm-polynomial-ring-laws (d)). Numerals in \( F \) are multiples of \( 1 \): \( 2 \coloneqq 1 + 1 \), \( 3 \coloneqq 2 + 1 \), and so on, so that \( 2 = 0 \) in \( \nF_2 \) and \( 3 = 0 \) in \( \nF_3 \) (@def-field-fp).

## Divisibility over a field

In \( \nZ \), "\( a \) divides \( b \)" asked whether \( b \) is some integer times \( a \). The same question makes sense in any commutative ring, and in \( F[x] \) it is the question this chapter is built on. The one new feature is that the answer can depend on the field.

*A polynomial \( g \) divides \( f \) when \( f \) is \( g \) times some polynomial over the same field.*

::: {#def-polynomial-divides}
[Divisibility of Polynomials]

Let \( F \) be a field and \( f, g \in F[x] \).

::: {.enumerate options="label=(\alph*)"}
1. \( g \) **divides \( f \) over \( F \)**, written \( g \mid f \), if **there exists** \( h \in F[x] \) with \( f = gh \). Then \( g \) is a **divisor** (or **factor**) of \( f \), and \( f \) is a **multiple** of \( g \). We write \( g \nmid f \) when \( g \) does not divide \( f \).
2. \( f \) and \( g \) are **associates** if \( f = cg \) for some **non-zero** constant \( c \in F \).
:::
:::

In words: (a) asks for a cofactor \( h \), and the cofactor must have its coefficients in \( F \); (b) says that two polynomials are associates when they differ by a non-zero constant factor. When two fields are in play, "\( g \mid f \) in \( F[x] \)" names the field.

Four instances, chosen so that the same symbols give different answers:

- \( x - 1 \mid x^2 - 1 \) in \( \nQ[x] \), since \( x^2 - 1 = (x - 1)(x + 1) \).
- \( 2x - 2 \mid x^2 - 1 \) in \( \nQ[x] \), since \( x^2 - 1 = (2x - 2)\bigl(\tfrac12 x + \tfrac12\bigr) \). The polynomials \( x - 1 \) and \( 2x - 2 = 2(x - 1) \) are associates, and the cofactor \( \tfrac12 x + \tfrac12 \) needs the inverse of \( 2 \).
- \( x + 1 \mid x^2 + 1 \) in \( \nF_2[x] \), since \( (x + 1)^2 = x^2 + 2x + 1 = x^2 + 1 \) there: \( 2 = 0 \) in \( \nF_2 \).
- \( x + 1 \nmid x^2 + 1 \) in \( \nQ[x] \). Suppose \( x^2 + 1 = (x + 1)h \) with \( h \in \nQ[x] \). Evaluating at \( -1 \) respects sums and products (@thm-evaluation-respects-operations), so \( (-1)^2 + 1 = (-1 + 1) \cdot h(-1) \), that is, \( 2 = 0 \cdot h(-1) = 0 \) in \( \nQ \), which is false.

*Non-example by minimal change.* The last two lines use the same symbols, \( x + 1 \) and \( x^2 + 1 \). Only the field changed, from \( \nF_2 \) to \( \nQ \), and with it the value of \( 2 \): the evaluation argument gives \( 2 = 0 \), which is true in \( \nF_2 \) and false in \( \nQ \). So "\( g \mid f \)" is a statement about \( g \), \( f \) **and** \( F \), which is why the definition says "over \( F \)".

*Degenerate cases.* Every \( g \) divides \( 0 \), since \( 0 = g \cdot 0 \). The zero polynomial divides only \( 0 \). And a non-zero constant \( c \) divides every \( f \), since \( f = c(c^{-1}f) \); this is (F8), inverses of non-zero elements, at work in general (the cofactor of \( 2x - 2 \) above was one instance), and it means that non-zero constants are as invisible to divisibility as \( \pm 1 \) were in \( \nZ \).

::: {.check}
In \( \nF_3[x] \), does \( x + 1 \) divide \( x^2 + 1 \)? Evaluate at \( -1 = 2 \).
:::

::: {.solution}
No. If \( x^2 + 1 = (x + 1)h \), evaluating at \( 2 \) (@thm-evaluation-respects-operations) gives \( 2^2 + 1 = (2 + 1)h(2) \), that is, \( 5 = 0 \cdot h(2) = 0 \). In \( \nF_3 \), \( 5 = 2 \ne 0 \). So \( x + 1 \nmid x^2 + 1 \) in \( \nF_3[x] \).
:::

The rules below are the ones the chapter uses. Parts (a)–(d) are identities in the commutative ring \( F[x] \), plus the inverse of a non-zero constant (F8) for the last clause of (a) and one degree count; parts (e) and (f) say exactly what "invisible" means.

::: {#prp-polynomial-divisibility-rules}
[Rules for Divisibility of Polynomials]

Let \( F \) be a field and \( f, g, h \in F[x] \).

::: {.enumerate options="label=(\alph*)"}
1. \( g \mid 0 \). \( 0 \mid f \) if and only if \( f = 0 \). Every non-zero constant divides every polynomial.
2. If \( f \mid g \) and \( g \mid h \), then \( f \mid h \).
3. If \( h \mid f \) and \( h \mid g \), then \( h \mid af + bg \) for **all** \( a, b \in F[x] \).
4. If \( g \mid f \) and \( f \ne 0 \), then \( \deg g \le \deg f \).
5. The units of \( F[x] \) (@def-ring-unit) are exactly the non-zero constants.
6. \( f \mid g \) and \( g \mid f \) if and only if \( f \) and \( g \) are associates (this includes \( f = g = 0 \)). Every non-zero \( f \) has **exactly one** monic associate, namely \( \operatorname{lc}(f)^{-1} f \). Two monic polynomials that divide each other are equal.
:::
:::

::: {.idea}
Parts (a)–(c) are rearrangements of equations \( f = gh \) by the ring laws, except that the last clause of (a) also uses \( c^{-1} \), from (F8). Part (d) is the degree of a product: a non-zero multiple of \( g \) has degree \( \deg g \) plus something in \( \nN \). Part (e) is Chapter 4's description of the units of \( R[x] \), read with \( R = F \). For (f), mutual divisibility gives \( f = f \cdot uv \), and canceling \( f \) makes \( u \) a unit, which (e) identifies as a non-zero constant.
:::

::: {.proof}
We use the ring laws of \( F[x] \) (@thm-polynomial-ring-laws (a)) and @fd3:prp-ring-algebra without further mention.

(a) \( 0 = g \cdot 0 \), so \( g \mid 0 \). If \( 0 \mid f \), then \( f = 0 \cdot k = 0 \) for some \( k \); conversely \( 0 \mid 0 \) by the first claim. If \( c \in F \) is a non-zero constant, then \( c^{-1} \) exists by (F8) of @def-field, and \( f = (c c^{-1}) f = c (c^{-1} f) \), so \( c \mid f \).

(b) Let \( g = fu \) and \( h = gv \). Then \( h = (fu)v = f(uv) \), so \( f \mid h \).

(c) Let \( f = hu \) and \( g = hv \). Then \( af + bg = a(hu) + b(hv) = h(au + bv) \), so \( h \mid af + bg \).

(d) Let \( f = gu \) with \( u \in F[x] \). Since \( f \ne 0 \), neither \( g \) nor \( u \) is \( 0 \). The field \( F \) has no zero divisors (@thm-field-basic-properties (f)), so @thm-degree-of-product (b) gives \( \deg f = \deg g + \deg u \). Here \( \deg u \in \nN \), so \( \deg g \le \deg f \).

(e) By @prp-polynomial-units, applied to the integral domain \( F \) (@exm-integral-domains), the units of \( F[x] \) are the constants that are units of \( F \). In a field every non-zero \( a \) is a unit, by (F8), and \( 0 \) is not, since \( 0 \cdot v = 0 \ne 1 \) for every \( v \) (@thm-field-basic-properties (d) and (F7) of @def-field). So the units of \( F[x] \) are the non-zero constants.

(f) \( (\Leftarrow) \) Let \( f = cg \) with \( c \ne 0 \) a constant. Then \( g \mid f \), and \( g = c^{-1} f \), so \( f \mid g \).

\( (\Rightarrow) \) Let \( f \mid g \) and \( g \mid f \). If \( f = 0 \), then \( 0 \mid g \), so \( g = 0 \) by (a), and \( f = 1 \cdot g \). Otherwise write \( g = fu \) and \( f = gv \). Then \( f = fuv \), so \( f(1 - uv) = 0 \). Since \( f \ne 0 \), @cor-polynomial-no-zero-divisors (a) gives \( 1 - uv = 0 \), that is, \( uv = 1 \). So \( v \) is a unit of \( F[x] \), hence a non-zero constant by (e), and \( f = vg \): \( f \) and \( g \) are associates.

*The monic associate.* Let \( f \ne 0 \) and \( a \coloneqq \operatorname{lc}(f) \ne 0 \). The polynomial \( a^{-1} f \) has the coefficients \( a^{-1} f_k \) (@thm-polynomial-ring-laws (d)). These vanish exactly where the \( f_k \) do, since \( a^{-1} \ne 0 \) (as \( a \cdot 0 = 0 \ne 1 = a a^{-1} \), by @thm-field-basic-properties (d), (F7), (F8)) and \( F \) has no zero divisors, so \( \deg(a^{-1} f) = \deg f \) and \( \operatorname{lc}(a^{-1} f) = a^{-1} a = 1 \). If also \( cf \) is monic for a constant \( c \ne 0 \), the same computation gives \( \operatorname{lc}(cf) = ca = 1 \), so \( c = a^{-1} \) (uniqueness of inverses, @thm-field-basic-properties (c)). So \( a^{-1} f \) is the only monic associate of \( f \).

*Monic and mutually dividing.* Let \( f, g \) be monic with \( f \mid g \) and \( g \mid f \). By what we proved, \( f = cg \) with a non-zero constant \( c \), and comparing leading coefficients, \( 1 = \operatorname{lc}(f) = c \operatorname{lc}(g) = c \). So \( f = g \). This proves the proposition.
:::

Parts (e) and (f) are the polynomial form of a fact about \( \nZ \): in @fd3:prp-divisibility-rules-integers (f) and (g), the units of \( \nZ \) were \( \pm 1 \), and two **positive** integers that divide each other are equal. In \( F[x] \) the units are the non-zero constants, and the role of "positive" is played by "monic": among the associates of a non-zero polynomial, exactly one is monic. So whenever a polynomial is to be singled out from its associates, it is made monic.

The hypothesis \( f \ne 0 \) in (d) cannot be dropped: \( x^5 \mid 0 \), and \( \deg x^5 = 5 > -\infty = \deg 0 \).

::: {.check}
In \( \nQ[x] \), list the associates of \( 3x + 6 \) that have integer coefficients and leading coefficient between \( -3 \) and \( 3 \). Which one is monic?
:::

::: {.solution}
The associates are \( c(3x + 6) \) with \( c \in \nQ \), \( c \ne 0 \); the leading coefficient is \( 3c \). Leading coefficients \( \pm 1, \pm 2, \pm 3 \) give \( \pm(x + 2) \), \( \pm(2x + 4) \), \( \pm(3x + 6) \), all with integer coefficients. The monic one is \( x + 2 = \tfrac13 (3x + 6) \).
:::

## Division with remainder

Now the theorem. The tool is the one *Number Systems: From \( \nN \) to \( \nR \)*, Section 4.1 used for integers, with degree in place of size: among all \( f - hg \), take one of **least degree**, and show that its degree is below \( \deg g \).

::: {#thm-polynomial-division-remainder}
[Division with Remainder in \( F[x] \)]

Let \( F \) be a field, and let \( f, g \in F[x] \) with \( g \ne 0 \).

::: {.enumerate options="label=(\alph*)"}
1. There are **unique** \( q, r \in F[x] \) with
\[
f = qg + r \quad \text{and} \quad \deg r < \deg g .
\]
2. \( g \mid f \) if and only if \( r = 0 \).
:::

The polynomials \( q \) and \( r \) are the **quotient** and the **remainder** of \( f \) on division by \( g \).
:::

Since \( \deg 0 = -\infty < \deg g \), the remainder \( r = 0 \) is allowed.

::: {.idea}
Look at all polynomials \( f - hg \), \( h \in F[x] \). If \( 0 \) is among them, \( f \) is a multiple of \( g \) and we are done. Otherwise their degrees are natural numbers, and well-ordering gives one, \( r \), of least degree \( n \). If \( n \ge \deg g \), we can kill the leading term of \( r \) by subtracting a constant times a power of \( x \) times \( g \): the constant is \( \operatorname{lc}(r) \operatorname{lc}(g)^{-1} \), and that inverse is where the field is needed. The result is again of the form \( f - hg \) and has smaller degree, against the choice of \( r \). Uniqueness: two answers give \( (q - q')g = r' - r \), and a non-zero multiple of \( g \) cannot have degree below \( \deg g \). We call this move **compare degrees**.
:::

::: {.proof}
(a) *Existence.* Let \( m \coloneqq \deg g \in \nN \) and \( b \coloneqq \operatorname{lc}(g) \ne 0 \), and let
\[
S \coloneqq \{ f - hg : h \in F[x] \} .
\]
If \( 0 \in S \), say \( 0 = f - qg \), then \( r \coloneqq 0 \) and this \( q \) satisfy \( f = qg + r \) and \( \deg r = -\infty < m \).

Suppose \( 0 \notin S \). Then every element of \( S \) has a degree in \( \nN \), and \( D \coloneqq \{ \deg s : s \in S \} \subseteq \nN \) is non-empty, since \( f = f - 0 \cdot g \in S \). By the well-ordering of \( \nN \) (@fd2:thm-well-ordering; on \( \nN = \omega \) it is @fd3:thm-omega-well-ordering), \( D \) has a least element \( n \). Choose \( q \in F[x] \) with \( r \coloneqq f - qg \) of degree \( n \), and let \( a \coloneqq \operatorname{lc}(r) \ne 0 \).

Suppose \( n \ge m \). Let \( t \coloneqq (ab^{-1}) x^{n-m} \), a monomial with \( n - m \in \nN \) and non-zero coefficient \( ab^{-1} \): \( b^{-1} \ne 0 \), since \( b \cdot 0 = 0 \ne 1 = b b^{-1} \) (@thm-field-basic-properties (d), (F7), (F8)), so \( ab^{-1} \ne 0 \) by @thm-field-basic-properties (f). Then \( \deg t = n - m \) and \( \operatorname{lc}(t) = ab^{-1} \), so by @thm-degree-of-product (b), \( tg \) has degree \( (n - m) + m = n \) and leading coefficient \( ab^{-1} b = a \). Let
\[
r_1 \coloneqq r - tg = f - (q + t) g ,
\]
an element of \( S \). By @thm-degree-of-sum (with \( \deg(-p) = \deg p \) for every \( p \), since \( (-p)_k = -p_k \)), \( \deg r_1 \le \max(\deg r, \deg tg) = n \), and the coefficient of \( x^n \) in \( r_1 \) is \( a - a = 0 \). So \( \deg r_1 < n \) (or \( r_1 = 0 \)). But \( r_1 \ne 0 \), since \( 0 \notin S \), and then \( \deg r_1 \in D \) is smaller than the least element \( n \) of \( D \). This contradiction shows \( n < m \). So \( f = qg + r \) with \( \deg r < \deg g \).

*Uniqueness.* Let \( f = qg + r = q'g + r' \) with \( \deg r < m \) and \( \deg r' < m \). Then
\[
(q - q')g = r' - r ,
\]
and \( \deg(r' - r) \le \max(\deg r', \deg r) < m \) by @thm-degree-of-sum (using \( \deg(-r) = \deg r \) as above). If \( q \ne q' \), then @thm-degree-of-product (b) gives \( \deg\bigl((q - q')g\bigr) = \deg(q - q') + m \ge m \), a contradiction. So \( q = q' \), hence \( r' - r = 0 \cdot g = 0 \) and \( r = r' \).

(b) \( (\Leftarrow) \) If \( r = 0 \), then \( f = qg \), so \( g \mid f \). \( (\Rightarrow) \) If \( f = hg \), then \( f = hg + 0 \) with \( \deg 0 < \deg g \) is a division with remainder; by the uniqueness in (a), \( r = 0 \). This proves the theorem.
:::

The field is used in two places. The first is the inverse \( b^{-1} \) of the leading coefficient of \( g \), which builds the monomial \( t \). The second is the degree of a product, in \( \deg(tg) = n \) and in the uniqueness: @thm-degree-of-product (b) needs the product of the leading coefficients to be non-zero, and a field has no zero divisors. The hypothesis \( g \ne 0 \) is needed as well: for \( g = 0 \) no \( r \) has \( \deg r < -\infty \).

The existence proof is also a procedure. Each pass replaces \( r \) by \( r - tg \), which removes the leading term of \( r \), and the degree drops by at least one. Starting from \( f \), at most \( \deg f - \deg g + 1 \) passes are needed when \( \deg f \ge \deg g \), and none when \( \deg f < \deg g \): then \( q = 0 \) and \( r = f \). This is the long division of school algebra, now with a proof that it stops and that its answer is the only one. Chapter 4 did not divide polynomials with remainder, so this is where the volume first does it. Its integer twin is @fd3:thm-integers-division-remainder, whose least-element proof the one above follows.

::: {#exm-polynomial-long-division}
[Long division in two fields]

(i) In \( \nQ[x] \), divide \( f = 2x^4 - 3x^3 + x^2 + 4x - 1 \) by \( g = 2x^2 - x + 3 \).

(ii) In \( \nF_3[x] \), divide \( f = x^4 + x + 2 \) by \( g = 2x^2 + 1 \).
:::

::: {.solution}
(i) Here \( \operatorname{lc}(g) = 2 \), with inverse \( \tfrac12 \). Each pass subtracts \( t g \), where \( t \) is the leading term of the current remainder divided by \( 2x^2 \):
\[
\begin{aligned}
f - x^2 g &= -2x^3 - 2x^2 + 4x - 1, \\
(-2x^3 - 2x^2 + 4x - 1) - (-x) g &= -3x^2 + 7x - 1, \\
(-3x^2 + 7x - 1) - \bigl(-\tfrac32\bigr) g &= \tfrac{11}{2} x + \tfrac72 .
\end{aligned}
\]
The last line has degree \( 1 < 2 \), so we stop. Adding up the \( t \)'s,
\[
2x^4 - 3x^3 + x^2 + 4x - 1 = \bigl(x^2 - x - \tfrac32\bigr)(2x^2 - x + 3) + \tfrac{11}{2} x + \tfrac72 .
\]
Check: \( \bigl(x^2 - x - \tfrac32\bigr)(2x^2 - x + 3) = 2x^4 - 3x^3 + x^2 - \tfrac32 x - \tfrac92 \), and adding \( \tfrac{11}{2} x + \tfrac72 \) gives \( f \).

(ii) In \( \nF_3 \), \( 2 \cdot 2 = 4 = 1 \), so \( \operatorname{lc}(g)^{-1} = 2^{-1} = 2 \). The first \( t \) is \( 1 \cdot 2 \cdot x^2 = 2x^2 \), and \( 2x^2 \cdot g = 4x^4 + 2x^2 = x^4 + 2x^2 \). The second \( t \) is \( 2 \), and \( 2g = 4x^2 + 2 = x^2 + 2 \):
\[
\begin{aligned}
f - 2x^2 g &= -2x^2 + x + 2 = x^2 + x + 2, \\
(x^2 + x + 2) - 2g &= x .
\end{aligned}
\]
So \( x^4 + x + 2 = (2x^2 + 2)(2x^2 + 1) + x \) in \( \nF_3[x] \). Check: \( (2x^2 + 2)(2x^2 + 1) = 4x^4 + 6x^2 + 2 = x^4 + 2 \) in \( \nF_3 \), and adding \( x \) gives \( f \).
:::

::: {.check}
Find two different pairs \( (q, r) \) with \( x^2 = q(x^2 + 1) + r \) in \( \nQ[x] \) and \( \deg r \le 2 \). Which condition in part (a) of the theorem does the second one fail?
:::

::: {.solution}
\( (q, r) = (1, -1) \): \( 1 \cdot (x^2 + 1) - 1 = x^2 \), with \( \deg(-1) = 0 < 2 \). And \( (q, r) = (0, x^2) \): \( 0 \cdot (x^2 + 1) + x^2 = x^2 \), with \( \deg r = 2 \). The second fails \( \deg r < \deg g = 2 \). Uniqueness holds only among remainders of degree **strictly** below that of the divisor; \( (1, -1) \) is the quotient and remainder.
:::

::: {.warning}
Division with remainder needs the leading coefficient of the divisor to be invertible. Take the polynomials in \( \nQ[x] \) all of whose coefficients lie in \( \nZ \), and try to divide \( x^2 \) by \( 2x \) **among them**: \( x^2 = q \cdot 2x + r \) with \( \deg r < 1 \). Comparing the coefficients of \( x^2 \) gives \( 1 = 2q_1 \) (@lem-monomial-product (a)), and no integer \( q_1 \) satisfies it, since \( 1 \) is odd (@fd3:cor-integers-even-odd (a)). In \( \nQ[x] \) there is no problem: \( x^2 = \tfrac12 x \cdot 2x + 0 \). Exercise C1 shows that integer coefficients are kept when the divisor is monic.
:::

## Roots and factors of degree one

Division by a polynomial of degree \( 1 \) has a remainder of degree at most \( 0 \), that is, a constant. Which constant? Evaluate: the divisor \( x - c \) vanishes at \( c \), so the quotient term disappears and the remainder is read off. We call this move **evaluate at a root**.

::: {#thm-polynomial-remainder-factor}
[Remainder Theorem and Factor Theorem]

Let \( F \) be a field, \( f \in F[x] \) and \( c \in F \).

::: {.enumerate options="label=(\alph*)"}
1. The remainder of \( f \) on division by \( x - c \) is the constant \( f(c) \).
2. \( c \) is a root of \( f \) if and only if \( x - c \mid f \).
3. \( f \) has a factor of degree \( 1 \) in \( F[x] \) if and only if \( f \) has a root in \( F \).
:::
:::

::: {.idea}
Divide by \( x - c \) and evaluate at \( c \): the term with the quotient vanishes, and what is left is the remainder. Part (b) is then the divisibility test of @thm-polynomial-division-remainder (b), and for (c) a factor \( ax + b \) of degree \( 1 \) is made monic, which turns it into some \( x - c \).
:::

::: {.proof}
(a) The polynomial \( x - c \) is non-zero, of degree \( 1 \) and monic. By @thm-polynomial-division-remainder (a), \( f = q \cdot (x - c) + r \) with \( \deg r < 1 \), so \( r \) is a constant (possibly \( 0 \)). Evaluation at \( c \) respects sums and products, sends \( x \) to \( c \) and a constant to itself (@thm-evaluation-respects-operations), so
\[
f(c) = q(c) \cdot (c - c) + r = q(c) \cdot 0 + r = r .
\]

(b) By (a), \( f = q \cdot (x - c) + f(c) \) is the division of \( f \) by \( x - c \). By @thm-polynomial-division-remainder (b), \( x - c \mid f \) if and only if this remainder is \( 0 \), that is, \( f(c) = 0 \).

(c) \( (\Leftarrow) \) If \( f(c) = 0 \), then \( x - c \mid f \) by (b), and \( x - c \) has degree \( 1 \). \( (\Rightarrow) \) Let \( ax + b \mid f \) with \( a, b \in F \), \( a \ne 0 \). Then \( ax + b = a\bigl(x - (-a^{-1}b)\bigr) \), so \( x - (-a^{-1}b) \mid ax + b \), and by @prp-polynomial-divisibility-rules (b), \( x - (-a^{-1}b) \mid f \). By (b), \( -a^{-1}b \) is a root of \( f \).
:::

Part (b) is the **factor theorem**, and it turns a question about values (is \( f(c) = 0 \)?) into a question about divisibility. Part (c) turns the search for factors of degree \( 1 \) into a search for roots.

::: {#exm-polynomial-remainders-without-dividing}
[Remainders without dividing]

(a) In \( \nQ[x] \), find the remainder of \( f = x^5 - 3x^3 + 2x + 7 \) on division by \( x - 2 \).

(b) In \( \nQ[x] \), find the remainder of \( x^5 \) on division by \( x^2 - x \).
:::

::: {.solution}
(a) By @thm-polynomial-remainder-factor (a), the remainder is
\[
f(2) = 32 - 24 + 4 + 7 = 19 .
\]

(b) The divisor \( x^2 - x \) has degree \( 2 \), so the remainder has degree at most \( 1 \): \( x^5 = q \cdot (x^2 - x) + ax + b \) with \( a, b \in \nQ \) (@thm-polynomial-division-remainder (a)). The divisor vanishes at \( 0 \) and at \( 1 \). Evaluating at both (@thm-evaluation-respects-operations),
\[
0 = q(0) \cdot 0 + b, \qquad 1 = q(1) \cdot 0 + a + b ,
\]
so \( b = 0 \) and \( a = 1 \). The remainder is \( x \). Check: \( x^5 - x = (x^2 - x)(x^3 + x^2 + x + 1) \).
:::

::: {.check}
Without dividing, decide whether \( x + 1 \) divides \( x^7 + 1 \) in \( \nQ[x] \), and whether \( x - 1 \) does.
:::

::: {.solution}
\( x + 1 = x - (-1) \), and \( (-1)^7 + 1 = -1 + 1 = 0 \), so \( x + 1 \mid x^7 + 1 \) by @thm-polynomial-remainder-factor (b). For \( x - 1 \), the remainder is \( 1^7 + 1 = 2 \ne 0 \) in \( \nQ \), so \( x - 1 \nmid x^7 + 1 \). (Over \( \nF_2 \), \( 2 = 0 \) and both divide.)
:::

::: {.remark}
[Looking ahead]

Section 5.5 builds, for any finite list of distinct points of \( F \), the polynomial of least degree that takes prescribed values there. Exercise C2 below is the case of two points: the remainder of \( f \) on division by \( (x - a)(x - b) \).
:::

## Exercises

### A. Check your understanding

::: {#exr-polynomial-division-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State @thm-polynomial-division-remainder with every hypothesis.
2. Name the two places in its proof where "\( F \) is a field" is used.
3. Let \( f \in F[x] \), and let \( c \in F \) be a non-zero constant. What are the quotient and the remainder of \( f \) on division by \( c \)?
4. True or false, with a reason: for \( f, g \in \nQ[x] \), if \( f \mid g \) and \( g \mid f \), then \( f = g \). The same question in \( \nF_2[x] \).
:::
:::

::: {.solution}
(a) Let \( F \) be a field and \( f, g \in F[x] \) with \( g \ne 0 \). Then there are unique \( q, r \in F[x] \) with \( f = qg + r \) and \( \deg r < \deg g \); and \( g \mid f \) if and only if \( r = 0 \).

(b) The inverse \( \operatorname{lc}(g)^{-1} \), which builds the monomial \( t = \operatorname{lc}(r)\operatorname{lc}(g)^{-1} x^{n-m} \); and the absence of zero divisors in \( F \), through @thm-degree-of-product (b), which gives \( \deg(tg) = n \) and, in the uniqueness, \( \deg\bigl((q - q')g\bigr) \ge \deg g \).

(c) \( q = c^{-1} f \) and \( r = 0 \): indeed \( f = (c^{-1} f) c + 0 \), and \( \deg 0 = -\infty < 0 = \deg c \). By uniqueness this is the division.

(d) In \( \nQ[x] \): false. \( x \mid 2x \) and \( 2x \mid x \) (\( x = \tfrac12 \cdot 2x \)), but \( x \ne 2x \). By @prp-polynomial-divisibility-rules (f), mutual divisibility only makes \( f \) and \( g \) associates. In \( \nF_2[x] \): true. By (f), \( f = cg \) with \( c \) a non-zero constant, and the only non-zero element of \( \nF_2 \) is \( 1 \); so \( f = g \).
:::

### B. Practice

::: {#exr-polynomial-division-b1}
[B1: Two long divisions]

::: {.enumerate options="label=(\alph*)"}
1. In \( \nQ[x] \), divide \( x^4 - 3x^3 + 2x - 5 \) by \( 3x^2 - 1 \).
2. In \( \nF_5[x] \), divide \( x^4 + 2x^3 + 3x + 1 \) by \( 2x^2 + 3 \), and decide whether \( 2x^2 + 3 \) divides \( x^4 + 2x^3 + 3x + 1 \) in \( \nF_5[x] \).
:::
:::

::: {.solution}
(a) \( \operatorname{lc}(3x^2 - 1)^{-1} = \tfrac13 \). The passes subtract \( \tfrac13 x^2 \), \( -x \) and \( \tfrac19 \) times the divisor:
\[
\begin{aligned}
(x^4 - 3x^3 + 2x - 5) - \tfrac13 x^2 (3x^2 - 1) &= -3x^3 + \tfrac13 x^2 + 2x - 5, \\
(-3x^3 + \tfrac13 x^2 + 2x - 5) + x(3x^2 - 1) &= \tfrac13 x^2 + x - 5, \\
(\tfrac13 x^2 + x - 5) - \tfrac19 (3x^2 - 1) &= x - \tfrac{44}{9} .
\end{aligned}
\]
So the quotient is \( \tfrac13 x^2 - x + \tfrac19 \) and the remainder is \( x - \tfrac{44}{9} \), of degree \( 1 < 2 \). Check: \( (3x^2 - 1)\bigl(\tfrac13 x^2 - x + \tfrac19\bigr) = x^4 - 3x^3 + x - \tfrac19 \), and adding \( x - \tfrac{44}{9} \) gives \( x^4 - 3x^3 + 2x - 5 \).

(b) In \( \nF_5 \), \( 2 \cdot 3 = 6 = 1 \), so \( 2^{-1} = 3 \). The passes subtract \( 3x^2 \), \( x \) and \( 3 \) times the divisor, with \( 3x^2(2x^2 + 3) = x^4 + 4x^2 \), \( x(2x^2 + 3) = 2x^3 + 3x \) and \( 3(2x^2 + 3) = x^2 + 4 \):
\[
\begin{aligned}
(x^4 + 2x^3 + 3x + 1) - (x^4 + 4x^2) &= 2x^3 + x^2 + 3x + 1, \\
(2x^3 + x^2 + 3x + 1) - (2x^3 + 3x) &= x^2 + 1, \\
(x^2 + 1) - (x^2 + 4) &= 2 ,
\end{aligned}
\]
using \( -4 = 1 \) and \( -3 = 2 \) in \( \nF_5 \). So the quotient is \( 3x^2 + x + 3 \) and the remainder is the constant \( 2 \). Since \( 2 \ne 0 \) in \( \nF_5 \), @thm-polynomial-division-remainder (b) gives \( 2x^2 + 3 \nmid x^4 + 2x^3 + 3x + 1 \) in \( \nF_5[x] \).
:::

::: {#exr-polynomial-division-b2}
[B2: A factor of a difference of powers]

Let \( F \) be a field, \( c \in F \) and \( n \in \nZ_{>0} \). Deduce from @fd4:lem-difference-of-powers that
\[
x^n - c^n = (x - c) \sum_{j=0}^{n-1} c^j x^{n-1-j} ,
\]
and hence that \( x - c \mid x^n - c^n \). Then give a second proof of the divisibility with @thm-polynomial-remainder-factor.
:::

::: {.solution}
\( F[x] \) is a commutative ring (@thm-polynomial-ring-laws (a)), so @fd4:lem-difference-of-powers applies in it. Take \( z = c \) and \( w = x \):
\[
c^n - x^n = (c - x) \sum_{j=0}^{n-1} c^j x^{n-1-j} .
\]
Negate both sides: \( -(c^n - x^n) = x^n - c^n \) and \( -\bigl((c - x) s\bigr) = (x - c) s \) for every \( s \in F[x] \) (@fd3:prp-ring-algebra (a), (c)). This is the displayed identity, and it shows \( x - c \mid x^n - c^n \). Taking \( z = c \), \( w = x \) rather than \( z = x \), \( w = c \) gives the sum in the stated order, with no re-indexing.

*Second proof.* By @thm-polynomial-ring-laws (c), \( x^n \) is the monomial \( 1 x^n \), whose value at \( c \) is \( 1 \cdot c^n = c^n \) (@def-polynomial-evaluation, the monomial example after it). So the value of \( x^n - c^n \) at \( c \) is \( c^n - c^n = 0 \) (@thm-evaluation-respects-operations, for the sum and the constant \( -c^n \)), so \( c \) is a root and \( x - c \mid x^n - c^n \) by @thm-polynomial-remainder-factor (b). This proof gives the divisibility at once but not the quotient.
:::

::: {#exr-polynomial-division-b3}
[B3: One remainder over every field]

Let \( F \) be any field. Show that the remainder of \( x^{100} \) on division by \( x^2 - 1 \) in \( F[x] \) is \( 1 \). Then explain why, over \( \nQ \), evaluating at the roots \( 1 \) and \( -1 \) also finds it, and why that method alone does not settle the question over \( \nF_2 \).
:::

::: {.solution}
By @fd4:lem-difference-of-powers in \( F[x] \) with \( z = x^2 \), \( w = 1 \) and \( n = 50 \), since \( (x^2)^k = x^{2k} \) and \( 1^k = 1 \) (@lem-finite-sums-and-powers (c)),
\[
(x^2 - 1) \sum_{j=0}^{49} x^{2j} = x^{100} - 1 .
\]
So \( x^{100} = \bigl(\sum_{j=0}^{49} x^{2j}\bigr)(x^2 - 1) + 1 \), and \( \deg 1 = 0 < 2 = \deg(x^2 - 1) \). By the uniqueness in @thm-polynomial-division-remainder (a), the remainder is \( 1 \), over every field.

*Over \( \nQ \) by evaluation.* Write \( x^{100} = q(x^2 - 1) + ax + b \). Evaluating at \( 1 \) and \( -1 \) gives \( 1 = a + b \) and \( 1 = -a + b \); subtracting, \( 2a = 0 \), so \( a = 0 \) since \( 2 \ne 0 \) in \( \nQ \); then \( b = 1 \).

*Over \( \nF_2 \).* There \( -1 = 1 \), so the two roots coincide and evaluation gives the single equation \( 1 = a + b \). It does not determine \( a \) and \( b \) (both \( (0, 1) \) and \( (1, 0) \) satisfy it), so the uniqueness argument above is needed.
:::

### C. Going deeper

::: {#exr-polynomial-division-c1}
[C1: Monic divisors keep integer coefficients]

Call \( p \in \nQ[x] \) an **integer polynomial** if every coefficient of \( p \) lies in \( \nZ \).

::: {.enumerate options="label=(\alph*)"}
1. Let \( f, g \) be integer polynomials with \( g \) monic. Prove that the quotient and the remainder of \( f \) on division by \( g \) in \( \nQ[x] \) are integer polynomials.
2. Prove the same if \( \operatorname{lc}(g) = -1 \).
3. Explain why the least-degree argument of @thm-polynomial-division-remainder still works when \( S \) is replaced by \( \{ f - hg : h \text{ an integer polynomial} \} \), for \( g \) monic.
:::
:::

::: {.solution}
[Hint 1]

Rerun the existence proof of @thm-polynomial-division-remainder, but only with integer polynomials \( h \).
:::

::: {.solution}
[Hint 2]

Let \( S_\nZ \coloneqq \{ f - hg : h \text{ an integer polynomial} \} \). If \( 0 \notin S_\nZ \), take \( r = f - qg \in S_\nZ \) of least degree \( n \) (@fd2:thm-well-ordering) and suppose \( n \ge \deg g \).
:::

::: {.solution}
Sums, negatives and products of integer polynomials are integer polynomials: their coefficients are sums of products of coefficients (@def-polynomial-ring), and \( \nZ \) is closed under \( + \), \( - \), \( \cdot \).

(c) and (a). Let \( m \coloneqq \deg g \) and
\[
S_\nZ \coloneqq \{ f - hg : h \text{ an integer polynomial} \} \subseteq \nQ[x] ,
\]
whose elements are integer polynomials. Run the existence proof with \( S_\nZ \) in place of \( S \). If \( 0 \in S_\nZ \), then \( f = qg \) with \( q \) an integer polynomial and \( r = 0 \). Otherwise take \( r = f - qg \in S_\nZ \) of least degree \( n \) (@fd2:thm-well-ordering), and suppose \( n \ge m \). With \( a \coloneqq \operatorname{lc}(r) \in \nZ \) and \( b = 1 \), the monomial \( t = a x^{n-m} \) is an integer polynomial, so \( r - tg = f - (q + t)g \in S_\nZ \), and it has degree \( < n \) or is \( 0 \), exactly as in the proof. Both contradict the choice of \( r \). So \( \deg r < m \), and \( f = qg + r \) with \( q, r \) integer polynomials. This is a division with remainder in \( \nQ[x] \), so by uniqueness (@thm-polynomial-division-remainder (a)) these \( q \), \( r \) are **the** quotient and remainder. The argument works because the step \( r \mapsto r - tg \) never leaves \( S_\nZ \): it needs \( b^{-1} \in \nZ \), and \( b = 1 \) gives \( b^{-1} = 1 \). That answers (c).

(b) If \( \operatorname{lc}(g) = -1 \), then \( b^{-1} = -1 \in \nZ \), and the same proof runs with \( t = -a x^{n-m} \). (Alternatively, divide \( f \) by the monic \( -g \): \( f = q(-g) + r = (-q)g + r \).)
:::

::: {#exr-polynomial-division-c2}
[C2: The remainder modulo a quadratic with known roots]

Let \( F \) be a field, \( f \in F[x] \) and \( a, b \in F \).

::: {.enumerate options="label=(\alph*)"}
1. If \( a \ne b \), prove that the remainder of \( f \) on division by \( (x - a)(x - b) \) is
\[
f(a) (a - b)^{-1} (x - b) + f(b) (b - a)^{-1} (x - a) .
\]
2. If \( a = b \), write \( f = (x - a)h + f(a) \) (@thm-polynomial-remainder-factor (a)) and prove that the remainder of \( f \) on division by \( (x - a)^2 \) is \( h(a)(x - a) + f(a) \).
3. Hence find the remainder of \( x^{100} \) on division by \( x^2 - 3x + 2 \) in \( \nQ[x] \).
:::
:::

::: {.solution}
[Hint 1]

The remainder has degree at most \( 1 \). Which values does it take at \( a \) and at \( b \)?
:::

::: {.solution}
[Hint 2]

Write \( f = q(x - a)(x - b) + r \) with \( \deg r \le 1 \), and let \( s \) be the displayed polynomial.
:::

::: {.solution}
(a) The divisor \( (x - a)(x - b) \) is monic of degree \( 2 \) (@thm-degree-of-product (b)), so @thm-polynomial-division-remainder (a) gives \( f = q (x - a)(x - b) + r \) with \( \deg r \le 1 \). Evaluating at \( a \) and at \( b \) (@thm-evaluation-respects-operations) kills the first term: \( r(a) = f(a) \) and \( r(b) = f(b) \). Let \( s \) be the displayed polynomial; it has degree at most \( 1 \), and \( s(a) = f(a) \cdot 1 + f(b) \cdot 0 = f(a) \), \( s(b) = f(b) \). So \( r - s \) has degree at most \( 1 \) and the two roots \( a \ne b \). If \( r - s \ne 0 \), then \( x - a \mid r - s \) (@thm-polynomial-remainder-factor (b)), say \( r - s = (x - a)k \), and \( \deg k \le 0 \) by @thm-degree-of-product (b), so \( k \) is a constant; evaluating at \( b \) gives \( 0 = (b - a) k \), so \( k = 0 \) because \( b - a \ne 0 \), and then \( r - s = 0 \) after all. Hence \( r = s \).

(b) Divide \( h \) by \( x - a \): \( h = (x - a)h_2 + h(a) \) (@thm-polynomial-remainder-factor (a)). Then
\[
f = (x - a)^2 h_2 + h(a)(x - a) + f(a) ,
\]
and \( h(a)(x - a) + f(a) \) has degree at most \( 1 < 2 \). By uniqueness, it is the remainder.

(c) \( x^2 - 3x + 2 = (x - 1)(x - 2) \). By (a) with \( a = 1 \), \( b = 2 \), \( f(1) = 1 \) and \( f(2) = 2^{100} \), the remainder is
\[
1 \cdot (-1)^{-1} (x - 2) + 2^{100} \cdot 1^{-1} (x - 1) = (2^{100} - 1)x + (2 - 2^{100}) .
\]
:::

<!-- dependency ledger
def-polynomial-divides (claim): (opening frame of the section) numerals 2 = 1 + 1, 3 = 2 + 1 in a field, so 2 = 0 in F_2 and 3 = 0 in F_3 | def-field-fp (residues mod p); multiples n * 1 of lem-integer-multiples (F5.2)
def-polynomial-divides (example): (x - 1)(x + 1) = x^2 - 1, (2x - 2)(x/2 + 1/2) = x^2 - 1, (x + 1)^2 = x^2 + 2x + 1 | ring laws of F[x] (thm-polynomial-ring-laws (a)), computed; verify/ch05/def-polynomial-divides.py
def-polynomial-divides (example): 2 != 0 in Q | thm-rationals-field (fd3), 1 + 1 > 0 in the ordered field Q
def-polynomial-divides (claim): (degenerate cases) 0 = g * 0, f = c (c^{-1} f) | fd3:prp-ring-algebra (b), (F8) of def-field; written out again in prp-polynomial-divisibility-rules (a)
prp-polynomial-divisibility-rules (proof): (f) coefficients of a^{-1} f vanish exactly where those of f do | thm-field-basic-properties (f) (no zero divisors), with thm-polynomial-ring-laws (d)
prp-polynomial-divisibility-rules (proof): (f) a^{-1} != 0 for a != 0 | a * 0 = 0 != 1 = a a^{-1}: thm-field-basic-properties (d), (F7), (F8); same argument for b^{-1} in thm-polynomial-division-remainder (proof)
prp-polynomial-divisibility-rules (proof): (d) deg u in N for u != 0, so deg g <= deg g + deg u | def-degree; order of N
prp-polynomial-divisibility-rules (proof): (f) comparing leading coefficients of f = c g | thm-polynomial-ring-laws (d) (coefficients of a constant multiple)
thm-polynomial-division-remainder (proof): n - m in N for m <= n, and (n - m) + m = n | fd3:cor-omega-identification (c) (fd2 lem-naturals-arithmetic on omega)
thm-polynomial-division-remainder (proof): deg t = n - m and lc(t) = a b^{-1} for the monomial t | def-polynomial (monomial), def-degree
thm-polynomial-division-remainder (proof): coefficient of x^n in r - tg is a - a = 0 | coefficientwise subtraction, def-polynomial-ring
thm-polynomial-division-remainder (proof): deg(-r) = deg r | (-r)_k = -r_k (def-polynomial-ring) and -a = 0 iff a = 0
thm-polynomial-division-remainder (claim): (paragraph after the proof) at most deg f - deg g + 1 passes | each pass lowers the degree by at least 1 (the proof), counted in N; nothing depends on it
thm-polynomial-division-remainder (claim): Chapter 4 states no division with remainder | F5.4 blueprint (ch04.md, Promises "-> F5.5"), meta-claim about Chapter 4
exm-polynomial-long-division (example): the passes and the checks, over Q and F_3 | verify/ch05/exm-polynomial-long-division.py
exm-polynomial-long-division (claim): (the warning after the Quick check that follows it) x^2 = (x/2)(2x); 2 q_1 = 1 has no solution in Z | computed; ring laws of Q[x]
thm-polynomial-remainder-factor (proof): x - c has degree 1 and is monic; deg r < 1 means r constant | def-degree
thm-polynomial-remainder-factor (proof): (c) ax + b = a(x - (-a^{-1} b)) | ring laws of F[x], (F8)
exm-polynomial-remainders-without-dividing (example): f(2) = 19; x^5 - x = (x^2 - x)(x^3 + x^2 + x + 1) | verify/ch05/exm-polynomial-remainders-without-dividing.py
exm-polynomial-remainders-without-dividing (claim): (the Quick check after it) (-1)^7 + 1 = 0, 1^7 + 1 = 2 | computed in Q and F_2
exr-polynomial-division-b1 (solution): the passes over Q and F_5 | verify/ch05/exr-polynomial-division-b1.py
exr-polynomial-division-b2 (solution): c^n - x^n = (c - x) sum_{j=0}^{n-1} c^j x^{n-1-j}, then negated | lem-difference-of-powers (F4.1) with z = c, w = x in the commutative ring F[x] (thm-polynomial-ring-laws (a)); fd3:prp-ring-algebra (a), (c)
exr-polynomial-division-b2 (solution): (second proof) value of x^n at c is c^n | thm-polynomial-ring-laws (c) (x^n = 1 x^n); def-polynomial-evaluation (monomial example)
exr-polynomial-division-b3 (solution): (x^2 - 1) sum_{j=0}^{49} x^{2j} = x^{100} - 1 | lem-difference-of-powers (F4.1) with z = x^2, w = 1, n = 50; lem-finite-sums-and-powers (c) ((x^2)^k = x^{2k}, 1^k = 1); verify/ch05/exr-polynomial-division-b3.py
exr-polynomial-division-c1 (solution): Z closed under +, -, *; coefficients of sums and products are sums of products | fd3:thm-integers-commutative-ring; def-polynomial-ring
exr-polynomial-division-c2 (solution): x^2 - 3x + 2 = (x - 1)(x - 2); the remainder (2^100 - 1)x + (2 - 2^100) | verify/ch05/exr-polynomial-division-c2.py
-->
