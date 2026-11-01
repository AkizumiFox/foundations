# Roots and Rational Powers

*Number Systems*, Chapter 6 found \( \sqrt a \) as the supremum of the numbers whose square stays below \( a \) (@fd3:prp-cof-square-roots). The same construction gives every \( n \)-th root, and the binomial-type estimates of this chapter make it work for every exponent. Roots then give powers with rational exponents, \( a^{m/n} \), once we check that the value does not depend on how the fraction \( \frac{m}{n} \) is written. These are the "real powers" of the chapter title as far as this chapter goes: rational exponents of positive reals. Chapter 8 extends them to every real exponent. The section ends with two estimates that make the limits \( \sqrt[n]{a} \to 1 \) and \( \sqrt[n]{n} \to 1 \) routine.

## n-th roots

For \( n = 2 \), *Number Systems: From \(\nN\) to \(\nR\)*, Chapter 6 built the square root by the move **construct a point as a supremum** (@fd3:prp-cof-square-roots), and an exercise there ran the same move for cube roots (@fd3:exr-measuring-by-rationals-b2). For a general exponent the move is the same; only the estimate for \( (s + h)^n \) needs a new tool, and @lem-difference-of-powers supplies it. Here \( n \cdot 1_{\nR} \) is written \( n \), and powers in \( \nR \) are those of @prp-power-laws-commutative-ring with \( R = \nR \), the same recursion as @fd3:def-naturals-in-ordered-field (b).

::: {#lem-reals-nth-root}
[Real n-th Roots]

Let \( n \in \nN \) with \( n \ge 1 \).

::: {.enumerate options="label=(\alph*)"}
1. If \( s, t \in \nR \) and \( 0 \le s < t \), then \( s^n < t^n \).
2. For every \( a \in \nR \) with \( a \ge 0 \) there is **exactly one** \( b \in \nR \) with \( b \ge 0 \) and \( b^n = a \). We write \( \sqrt[n]{a} \coloneqq b \). For \( n = 2 \) it is the square root \( \sqrt a \) of @fd3:prp-cof-square-roots.
:::
:::

::: {.idea}
Part (a) is the factorization \( t^n - s^n = (t - s)(t^{n-1} + t^{n-2}s + \dots + s^{n-1}) \): both factors are positive. For (b), let \( s \) be the supremum of the set \( S \) of non-negative \( y \) with \( y^n \le a \), and rule out \( s^n < a \) and \( s^n > a \).

If \( s^n < a \), we want \( h > 0 \) with \( (s + h)^n \le a \). Working backwards: for \( 0 < h \le 1 \), the same factorization writes \( (s + h)^n - s^n \) as \( h \) times a sum of \( n \) terms, each at most \( (s + 1)^{n-1} \). So \( (s + h)^n - s^n \le h \cdot n(s + 1)^{n-1} \), and it is enough that this be at most half the room \( a - s^n \). That gives \( h \coloneqq \min\{1, (a - s^n)/(2n(s + 1)^{n-1})\} \).

If \( s^n > a \), we want \( h > 0 \) with \( (s - h)^n \ge a \) still, which makes \( s - h \) a smaller upper bound. Now \( s^n - (s - h)^n \le h \cdot n s^{n-1} \), and it is enough that this equal the excess \( s^n - a \). That gives \( h \coloneqq (s^n - a)/(n s^{n-1}) \).

*Before reading on: where is completeness used, and why must \( h \le 1 \) in the first case?*
:::

::: {.proof}
Three facts are used throughout: a power of a non-negative real number is non-negative and a power of a positive one is positive (induction on the exponent with @fd3:prp-ordered-ring-rules (c)); if \( 0 \le y \le 1 \) then \( y^k \le y \) for every \( k \ge 1 \), while if \( y \ge 1 \) then \( y^k \ge y \) (induction: \( y^{k+1} = y^k y \), and @fd3:prp-ordered-ring-rules (c) or equality); and if \( 0 \le x \le x' \) and \( 0 \le y \le y' \), then \( xy \le x'y \le x'y' \) (@fd3:prp-ordered-ring-rules (c) twice, or equality).

(a) By @lem-difference-of-powers in the commutative ring \( \nR \),
\[
t^n - s^n = (t - s) \sum_{k=0}^{n-1} t^k s^{n-1-k} .
\]
Every term of the sum is \( \ge 0 \), and the term with \( k = n - 1 \) is \( t^{n-1} > 0 \), since \( t > s \ge 0 \). So the sum is \( \ge t^{n-1} > 0 \). Also \( t - s > 0 \). Hence \( t^n - s^n > 0 \) (@fd3:prp-ordered-ring-rules (c)).

(b) *Uniqueness.* If \( b, c \ge 0 \) and \( b \ne c \), say \( b < c \), then \( b^n < c^n \) by (a); so at most one non-negative \( b \) has \( b^n = a \).

*Existence.* If \( a = 0 \), then \( b \coloneqq 0 \) works, since \( 0^n = 0^{n-1} \cdot 0 = 0 \). Let \( a > 0 \), and let
\[
S \coloneqq \{ y \in \nR : y \ge 0 \text{ and } y^n \le a \} .
\]
Put \( m \coloneqq \min\{1, a\} > 0 \). Since \( 0 < m \le 1 \), \( m^n \le m \le a \), so \( m \in S \). Put \( M \coloneqq \max\{1, a\} \). If \( y > M \), then \( y > 1 \), so \( y^n \ge y > M \ge a \) and \( y \notin S \); hence \( M \) is an upper bound of \( S \). Since \( \nR \) is a complete ordered field (@fd3:thm-reals-complete-ordered-field, @fd3:def-complete-ordered-field), \( S \) has a supremum; let \( s \coloneqq \sup S \). Then \( s \ge m > 0 \).

*Case \( s^n < a \).* Let
\[
h \coloneqq \min\Bigl\{ 1, \frac{a - s^n}{2n(s + 1)^{n-1}} \Bigr\} .
\]
It depends only on \( a \), \( n \) and \( s \), and \( h > 0 \), since \( a - s^n > 0 \) and \( 2n(s + 1)^{n-1} > 0 \). By @lem-difference-of-powers,
\[
(s + h)^n - s^n = h \sum_{k=0}^{n-1} (s + h)^k s^{n-1-k} .
\]
Since \( 0 \le s < s + h \le s + 1 \), each term satisfies \( (s + h)^k s^{n-1-k} \le (s + 1)^k (s + 1)^{n-1-k} = (s + 1)^{n-1} \), by (a) (or equality), the third fact, and @prp-power-laws-commutative-ring (a). A sum of \( n \) terms, each at most \( (s + 1)^{n-1} \), is at most \( n (s + 1)^{n-1} \). Hence
\[
(s + h)^n \le s^n + h \cdot n(s + 1)^{n-1} \le s^n + \frac{a - s^n}{2} < a .
\]
So \( s + h \in S \), and \( s + h > s \), against \( s \) being an upper bound of \( S \).

*Case \( s^n > a \).* Let
\[
h \coloneqq \frac{s^n - a}{n s^{n-1}} ,
\]
which depends only on \( a \), \( n \) and \( s \), and is positive. Since \( a > 0 \), we have \( s^n - a < s^n \le n s^n \), so \( h < s^n/(n s^{n-1}) = s/n \le s \); thus \( 0 < s - h < s \). By @lem-difference-of-powers and the same bound, with \( 0 < s - h < s \), each of the \( n \) terms of \( \sum_{k=0}^{n-1} s^k (s - h)^{n-1-k} \) is at most \( s^{n-1} \), so
\[
s^n - (s - h)^n \le h \cdot n s^{n-1} = s^n - a ,
\]
that is, \( (s - h)^n \ge a \). Now let \( y \in S \). If \( y > s - h \), then (a) gives \( y^n > (s - h)^n \ge a \), against \( y \in S \). So \( y \le s - h \), and \( s - h \) is an upper bound of \( S \) smaller than \( s \), against \( s \) being the **least** upper bound.

Both cases are impossible, so \( s^n = a \) by trichotomy, and \( b \coloneqq s \ge 0 \) works.

For \( n = 2 \), the number \( \sqrt[2]{a} \) is non-negative and squares to \( a \), so it is \( \sqrt a \), by the uniqueness in @fd3:prp-cof-square-roots.
:::

The constants were found backwards in the Idea and placed first in the proof, and each depends on \( a \), \( n \) and \( s \) only. Completeness was used once, to produce \( s \). For \( a > 0 \) the root is positive, since \( 0^n = 0 \ne a \). For instance \( \sqrt[3]{8} = 2 \) and \( \sqrt[4]{4} = \sqrt 2 \), since \( 2^3 = 8 \) and \( (\sqrt 2)^4 = \bigl((\sqrt 2)^2\bigr)^2 = 4 \), and both are non-negative. The symbol \( \sqrt[n]{a} \) is used only for **non-negative real** \( a \); Chapter 3 shows why it could not mean "the" \( n \)-th root of a complex number.

The last example already used the working principle of this section. To identify a root, we do not compute it: we take a candidate, check that it is non-negative, and check that its \( n \)-th power is \( a \). Uniqueness in part (b) does the rest. Every rule for roots follows this way from a rule for powers.

::: {#lem-root-rules}
[Rules for n-th Roots]

Let \( n, m \ge 1 \) be integers and \( a, b \in \nR \) with \( a, b \ge 0 \).

::: {.enumerate options="label=(\alph*)"}
1. \( \sqrt[n]{ab} = \sqrt[n]{a} \, \sqrt[n]{b} \).
2. \( \sqrt[n]{a^m} = \bigl( \sqrt[n]{a} \bigr)^m \).
3. \( \sqrt[m]{\sqrt[n]{a}} = \sqrt[mn]{a} \).
4. If \( a < b \), then \( \sqrt[n]{a} < \sqrt[n]{b} \).
:::
:::

::: {.idea}
Each of (a)–(c) says that some non-negative number is a certain root. So we raise the right side to the relevant power, compute with the laws of powers, and let the uniqueness in @lem-reals-nth-root (b) identify it. This is the move by which @fd3:lem-field-fraction-rules identified inverses: name the defining property, check it, invoke uniqueness. Part (d) runs part (a) of the lemma backwards.
:::

::: {.proof}
Write \( x \coloneqq \sqrt[n]{a} \) and \( y \coloneqq \sqrt[n]{b} \), so \( x, y \ge 0 \), \( x^n = a \) and \( y^n = b \). Powers and products of non-negative reals are non-negative (@fd3:prp-ordered-ring-rules (c), by induction for powers).

(a) The number \( xy \) is \( \ge 0 \), and \( (xy)^n = x^n y^n = ab \) by @prp-power-laws-commutative-ring (c). By the uniqueness in @lem-reals-nth-root (b), \( xy = \sqrt[n]{ab} \).

(b) The number \( x^m \) is \( \ge 0 \), and by @prp-power-laws-commutative-ring (b), used twice with \( mn = nm \),
\[
(x^m)^n = x^{mn} = (x^n)^m = a^m .
\]
By uniqueness, \( x^m = \sqrt[n]{a^m} \).

(c) Let \( z \coloneqq \sqrt[m]{x} \), so \( z \ge 0 \) and \( z^m = x \). By @prp-power-laws-commutative-ring (b), \( z^{mn} = (z^m)^n = x^n = a \). By uniqueness with the exponent \( mn \ge 1 \), \( z = \sqrt[mn]{a} \).

(d) Let \( a < b \), and suppose \( y \le x \). If \( y = x \), then \( b = y^n = x^n = a \). If \( y < x \), then \( b = y^n < x^n = a \) by @lem-reals-nth-root (a), since \( 0 \le y \). Both contradict \( a < b \). So \( x < y \).
:::

Part (d) and @lem-reals-nth-root (a) together say that for non-negative reals, \( a < b \) holds **if and only if** \( \sqrt[n]{a} < \sqrt[n]{b} \): taking an \( n \)-th root and raising to the \( n \)-th power both preserve strict order. That two-way comparison is how roots are compared without computing them, as in @exm-rational-power-computations below.

::: {.check}
Simplify \( \sqrt[3]{\sqrt{64}} \) in two ways.
:::

::: {.solution}
By @lem-root-rules (c) with \( m = 3 \), \( n = 2 \), it is \( \sqrt[6]{64} = 2 \), since \( 2 \ge 0 \) and \( 2^6 = 64 \). Directly, \( \sqrt{64} = 8 \) (as \( 8 \ge 0 \) and \( 8^2 = 64 \)), and \( \sqrt[3]{8} = 2 \).
:::

## Integer powers

A rational exponent \( \frac{m}{n} \) may have a negative numerator, so before we can define \( a^{m/n} \) we need \( a^m \) for negative integers \( m \). There is only one sensible choice. If the law \( a^{m+k} = a^m a^k \) is to survive, then \( a^{-k} a^k = a^0 = 1 \), so \( a^{-k} \) has to be the inverse of \( a^k \). The definition makes this so, and it works in every field, which Chapter 3 will use in \( \nC \).

::: {#def-integer-power}
[Integer Powers]

Let \( F \) be a field, \( a \in F \) with \( a \ne 0 \), and \( n \in \nN \). Put
\[
a^{-n} \coloneqq \bigl( a^{-1} \bigr)^n ,
\]
where the right side is the power of @prp-power-laws-commutative-ring.
:::

Only \( n = 0 \) could clash with the earlier meaning: \( -0 = 0 \), and both readings give \( 1 \), since \( a^0 = 1 = (a^{-1})^0 \). For \( n \ge 1 \) the integer \( -n \) is not in \( \nN \), so the definition gives a new symbol a meaning and changes no old one. At \( n = 1 \) it reads \( a^{-1} = (a^{-1})^1 \): the new power and the old inverse agree. The base must be non-zero, since \( 0 \) has no inverse. For instance, in \( \nR \), \( 2^{-3} = \bigl(\frac12\bigr)^3 = \frac18 \).

::: {#prp-integer-power-laws}
[Laws of Integer Powers]

Let \( F \) be a field, let \( a, b \in F \) with \( a \ne 0 \) and \( b \ne 0 \), and let \( m, n \in \nZ \).

::: {.enumerate options="label=(\alph*)"}
1. \( a^{m+n} = a^m a^n \).
2. \( (a^m)^n = a^{mn} \).
3. \( (ab)^n = a^n b^n \).
4. \( a^n \ne 0 \) and \( a^{-n} = (a^n)^{-1} \).
5. If \( F \) is an ordered field and \( a > 0 \), then \( a^n > 0 \).
6. If \( F \) is an ordered field, \( a > 1 \) and \( m < n \), then \( a^m < a^n \).
:::
:::

::: {.idea}
Each law is known for exponents in \( \nN \) (@prp-power-laws-commutative-ring). A negative exponent is a natural one applied to \( a^{-1} \), and \( (a^{-1})^k = (a^k)^{-1} \) lets us move the inverse wherever it is needed. So each law splits into sign cases, and each case reduces to \( \nN \).
:::

The cases are routine and are written out in the fold below. One case shows the pattern: (a) with \( m \ge 0 > n \). Write \( n = -k \) with \( k \ge 1 \), and recall (d) for natural exponents, \( (a^{-1})^k = (a^k)^{-1} \), which the fold proves first. If \( m \ge k \), then \( a^m = a^{m-k} a^k \) by @prp-power-laws-commutative-ring (a), so
\[
a^m a^{-k} = a^{m-k} \, a^k (a^k)^{-1} = a^{m-k} = a^{m+n} .
\]
If \( m < k \), then \( a^{-k} = (a^{-1})^{m} (a^{-1})^{k-m} \), again by @prp-power-laws-commutative-ring (a), and \( a^m (a^{-1})^m = (a a^{-1})^m = 1 \) by part (c) of that result, so
\[
a^m a^{-k} = (a a^{-1})^m \, (a^{-1})^{k-m} = (a^{-1})^{k-m} = a^{-(k-m)} = a^{m+n} .
\]

::: {.second-reading title="The sign cases for integer powers"}
::: {.proof}
Throughout, exponents written \( j, k, \ell \) are in \( \nN \), and laws "for \( \nN \)" are @prp-power-laws-commutative-ring. Note \( 1^k = 1 \) for every \( k \) (induction: \( 1^{k+1} = 1^k \cdot 1 \)).

(d) *Natural exponents.* For \( k \in \nN \), \( a^k \ne 0 \) by part (d) for \( \nN \), and \( a^k (a^{-1})^k = (a a^{-1})^k = 1^k = 1 \) by part (c) for \( \nN \). By @fd3:lem-field-fraction-rules (a), \( a^{-k} = (a^{-1})^k = (a^k)^{-1} \), and it is non-zero, since its product with \( a^k \) is \( 1 \ne 0 \). *Negative exponents.* For \( n = -k \) with \( k \ge 1 \), \( a^n = (a^k)^{-1} \ne 0 \), and \( (a^n)^{-1} = ((a^k)^{-1})^{-1} = a^k = a^{-n} \) by @fd3:lem-field-fraction-rules (a). So (d) holds for every \( n \in \nZ \). In particular, for every \( n \in \nZ \),
\[
a^{-n} = \bigl( a^{-1} \bigr)^{n} , \tag{$\ast$}
\]
by the definition for \( n \ge 0 \), and for \( n = -k < 0 \) because both sides equal \( a^k \): the right side is \( ((a^{-1})^{-1})^k = a^k \).

(a) *Both \( m, n \ge 0 \):* part (a) for \( \nN \). *Both negative,* \( m = -j \), \( n = -k \): by the definition and part (a) for \( \nN \) applied to \( a^{-1} \),
\[
a^{m+n} = (a^{-1})^{j+k} = (a^{-1})^j (a^{-1})^k = a^m a^n .
\]
*Mixed signs:* the case \( m \ge 0 > n \) is the computation on the main line; the case \( m < 0 \le n \) is the same with \( m \) and \( n \) exchanged, since \( F \) is commutative.

(b) *\( n = k \ge 0 \).* If \( m \ge 0 \), this is part (b) for \( \nN \). If \( m = -j < 0 \), then \( (a^m)^k = ((a^{-1})^j)^k = (a^{-1})^{jk} = a^{-jk} = a^{mk} \), by part (b) for \( \nN \) applied to \( a^{-1} \). *\( n = -k < 0 \).* Since \( a^m \ne 0 \) by (d), the definition and (d) give \( (a^m)^{-k} = ((a^m)^{-1})^k = (a^{-m})^k \), and the case just proved, with exponents \( -m \in \nZ \) and \( k \ge 0 \), gives \( (a^{-m})^k = a^{-mk} = a^{mn} \).

(c) *\( n = k \ge 0 \):* part (c) for \( \nN \). *\( n = -k < 0 \):* \( ab \ne 0 \) and \( (ab)^{-1} = a^{-1} b^{-1} \) (@fd3:lem-field-fraction-rules (a)), so
\[
(ab)^{-k} = (a^{-1} b^{-1})^k = (a^{-1})^k (b^{-1})^k = a^{-k} b^{-k} .
\]

(e) For \( k \in \nN \), \( a^k > 0 \) by induction: \( a^0 = 1 > 0 \), and if \( a^k > 0 \), then \( a^{k+1} = a^k a > 0 \cdot a = 0 \) by @fd3:prp-ordered-ring-rules (c). (This is the proof of @fd2:prp-power-laws (e), which works in any ordered field.) For \( n = -k < 0 \), \( a^{-1} > 0 \) by @fd3:prp-reciprocal-order (a), so \( a^n = (a^{-1})^k > 0 \) by the case just proved.

(f) First, \( a^\ell > 1 \) for every \( \ell \ge 1 \), by induction: \( a^1 = a > 1 \), and if \( a^\ell > 1 \), then \( a^{\ell+1} = a^\ell a > 1 \cdot a = a > 1 \), by @fd3:prp-ordered-ring-rules (c) with the positive factor \( a \). Now let \( m < n \), and put \( \ell \coloneqq n - m \ge 1 \). By (a), \( a^n = a^m a^\ell \), and \( a^m > 0 \) by (e). Multiplying \( a^\ell > 1 \) by \( a^m > 0 \) (@fd3:prp-ordered-ring-rules (c)) gives \( a^n > a^m \).
:::
:::

::: {.check}
Compute \( 2^{-3} \cdot 4^{2} \) and \( \bigl(\frac23\bigr)^{-2} \) in \( \nR \).
:::

::: {.solution}
\( 2^{-3} = \bigl(\frac12\bigr)^3 = \frac18 \) and \( 4^2 = 16 \), so the product is \( \frac{16}{8} = 2 \). (Alternatively, \( 4^2 = (2^2)^2 = 2^4 \) and \( 2^{-3} 2^4 = 2^1 \) by @prp-integer-power-laws (b), (a).) And \( \bigl(\frac23\bigr)^{-2} = \bigl(\frac32\bigr)^2 = \frac94 \), since the inverse of \( \frac23 \) is \( \frac32 \).
:::

## Rational powers

Which number should \( 8^{2/3} \) be? Reading the exponent as "square of the cube root" gives \( (\sqrt[3]{8})^2 = 2^2 = 4 \). But \( \frac23 = \frac46 \), and reading \( \frac46 \) the same way gives \( (\sqrt[6]{8})^4 \). That is \( 4 \) again, as it must be if the notation is to mean anything: its sixth power is \( 8^4 = 4096 = 4^6 \). A definition that picks one way of writing the exponent is a definition by representatives, and it is only a definition if every representative gives the same value.

*A rational power is a power of a root, and it does not matter which fraction names the exponent.*

::: {#def-rational-power}
[Rational Powers]

Let \( a \in \nR \) with \( a > 0 \), and let \( r \in \nQ \). Write \( r = \frac{m}{n} \) with \( m \in \nZ \) and \( n \in \nZ_{>0} \), and put
\[
a^r \coloneqq \bigl( \sqrt[n]{a} \bigr)^m .
\]
:::

In words: take the \( n \)-th root of the base, which is positive since \( a > 0 \), and raise it to the integer power \( m \) of @def-integer-power. The base is **strictly** positive, so that negative \( m \) is allowed; the warning below shows that negative bases cannot be admitted at all.

The definition chose one fraction for \( r \), and every rational number has infinitely many. So there is something to check before \( a^r \) means anything.

::: {#prp-rational-power-well-defined}
[Rational Powers Are Well Defined]

Let \( a \in \nR \) with \( a > 0 \). If \( m, p \in \nZ \) and \( n, q \in \nZ_{>0} \) satisfy \( \frac{m}{n} = \frac{p}{q} \), then
\[
\bigl( \sqrt[n]{a} \bigr)^m = \bigl( \sqrt[q]{a} \bigr)^p .
\]
For \( r = m \in \nZ \), the number \( a^r \) is the integer power \( a^m \) of @def-integer-power, and for \( r = \frac1n \) it is \( \sqrt[n]{a} \).
:::

*Try it first (ten minutes): show \( (\sqrt[2]{a})^1 = (\sqrt[4]{a})^2 \), then say what the general proof must compare.*

::: {.idea}
The attempt runs into the fact that we cannot compute either root, so we cannot compare them directly. In the trial case, squaring the right side gives \( ((\sqrt[4]{a})^2)^2 = a \), so it is the non-negative number with square \( a \): uniqueness of square roots identifies it. In general, raise both candidates to the power \( nq \), which clears both roots: the left side becomes \( a^{mq} \) and the right side \( a^{pn} \), and \( mq = pn \) is what \( \frac{m}{n} = \frac{p}{q} \) means. Two positive numbers with the same \( nq \)-th power are equal by @lem-reals-nth-root (b). This is the method of @fd2:exm-method-well-definedness: two representatives, their relation unwound, equal outputs.
:::

::: {.proof}
Let \( u \coloneqq (\sqrt[n]{a})^m \) and \( v \coloneqq (\sqrt[q]{a})^p \). The roots are positive since \( a > 0 \), so \( u, v > 0 \) by @prp-integer-power-laws (e). By @prp-integer-power-laws (b), used twice with \( m \cdot nq = n \cdot mq \),
\[
u^{nq} = \bigl( \sqrt[n]{a} \bigr)^{mnq} = \Bigl( \bigl( \sqrt[n]{a} \bigr)^{n} \Bigr)^{mq} = a^{mq} ,
\]
and in the same way \( v^{nq} = \bigl( (\sqrt[q]{a})^{q} \bigr)^{pn} = a^{pn} \). Multiplying \( \frac{m}{n} = \frac{p}{q} \) by \( nq \) gives \( mq = pn \). Hence \( u^{nq} = v^{nq} \), with \( nq \ge 1 \), and the uniqueness in @lem-reals-nth-root (b) with exponent \( nq \) gives \( u = v \).

For \( r = m \in \nZ \), use the representative \( \frac{m}{1} \): \( \sqrt[1]{a} = a \), since \( a \ge 0 \) and \( a^1 = a \), so \( a^r = a^m \). For \( r = \frac1n \), use \( \frac{1}{n} \): \( a^r = (\sqrt[n]{a})^1 = \sqrt[n]{a} \).
:::

So \( a^r \) depends on \( r \) alone, and the two special cases say that the new notation extends the old: \( a^{3} \), \( a^{-2} \) and \( a^{1/n} = \sqrt[n]{a} \) all mean what they meant before.

::: {.warning}
Negative bases do not have rational powers. The real number \( -2 \) has cube \( -8 \), so one might want \( (-8)^{1/3} = -2 \). But \( \frac13 = \frac26 \), and read through \( \frac26 \) the power would be the square of a sixth root of \( -8 \), and no real number has sixth power \( -8 \), since an even power is \( \ge 0 \). Reading \( \frac26 \) as "sixth root of the square" gives \( ((-8)^2)^{1/6} = 64^{1/6} = 2 \), positive. No value is independent of the representative, which is why @def-rational-power asks for \( a > 0 \).
:::

With well-definedness in hand, the laws come almost for free. Any two rational exponents can be written over one denominator, and then everything is a statement about integer powers of a single root.

::: {#prp-rational-power-laws}
[Laws of Rational Powers]

Let \( a, b \in \nR \) with \( a > 0 \) and \( b > 0 \), and let \( r, s \in \nQ \).

::: {.enumerate options="label=(\alph*)"}
1. \( a^{r+s} = a^r a^s \).
2. \( (a^r)^s = a^{rs} \).
3. \( (ab)^r = a^r b^r \).
4. \( a^r > 0 \).
5. If \( a > 1 \) and \( r < s \), then \( a^r < a^s \).
6. If \( a < b \) and \( r > 0 \), then \( a^r < b^r \).
:::
:::

::: {.idea}
Write \( r = \frac{m}{n} \) and \( s = \frac{p}{n} \) over a common denominator \( n > 0 \); @prp-rational-power-well-defined allows any representative. Then \( a^r = c^m \) and \( a^s = c^p \) with \( c \coloneqq \sqrt[n]{a} \), and each law becomes a law of integer powers of \( c \) (@prp-integer-power-laws).
:::

::: {.proof}
Write \( r = \frac{m'}{n'} \) and \( s = \frac{p'}{q'} \) with \( n', q' > 0 \), and put \( n \coloneqq n'q' > 0 \), \( m \coloneqq m'q' \), \( p \coloneqq p'n' \). Then \( r = \frac{m}{n} \) and \( s = \frac{p}{n} \). Let \( c \coloneqq \sqrt[n]{a} > 0 \). By @prp-rational-power-well-defined, \( a^r = c^m \) and \( a^s = c^p \). We prove (a) and (e); the other parts are proved in the fold below.

(a) Since \( r + s = \frac{m + p}{n} \), @prp-rational-power-well-defined and @prp-integer-power-laws (a) give \( a^{r+s} = c^{m+p} = c^m c^p = a^r a^s \).

(e) Let \( a > 1 \). Then \( c > 1 \): otherwise \( c \le 1 \), and either \( c = 1 \) and \( a = 1^n = 1 \), or \( 0 < c < 1 \) and \( a = c^n < 1^n = 1 \) by @lem-reals-nth-root (a); both contradict \( a > 1 \). From \( r < s \), multiplying by \( n > 0 \), we get \( m < p \). By @prp-integer-power-laws (f), \( a^r = c^m < c^p = a^s \).
:::

::: {.second-reading title="Proofs of (b), (c), (d), (f)"}
::: {.proof}
Keep \( r = \frac{m}{n} \), \( c = \sqrt[n]{a} \) as above.

(d) \( a^r = c^m > 0 \) by @prp-integer-power-laws (e), since \( c > 0 \).

(b) Here it is convenient to write \( s = \frac{p}{q} \) with its own denominator \( q > 0 \). Let \( w \coloneqq a^r > 0 \) (by (d)), \( u \coloneqq w^s = (a^r)^s \) and \( v \coloneqq a^{rs} \), where \( rs = \frac{mp}{nq} \). Both \( u \) and \( v \) are positive by (d). By the definition and @prp-integer-power-laws (b), \( w^n = (c^m)^n = (c^n)^m = a^m \), and
\[
u^q = \Bigl( \bigl( \sqrt[q]{w} \bigr)^p \Bigr)^q = \Bigl( \bigl( \sqrt[q]{w} \bigr)^q \Bigr)^p = w^p .
\]
Hence, again by @prp-integer-power-laws (b),
\[
u^{nq} = (u^q)^n = (w^p)^n = (w^n)^p = (a^m)^p = a^{mp} .
\]
Also \( v = (\sqrt[nq]{a})^{mp} \), so \( v^{nq} = \bigl( (\sqrt[nq]{a})^{nq} \bigr)^{mp} = a^{mp} \). So \( u^{nq} = v^{nq} \), and the uniqueness in @lem-reals-nth-root (b) with exponent \( nq \) gives \( u = v \). This covers \( m \le 0 \) and \( p \le 0 \) as well, because only integer-power laws were used.

(c) By @lem-root-rules (a), \( \sqrt[n]{ab} = \sqrt[n]{a} \, \sqrt[n]{b} \), and both factors are positive. By @prp-integer-power-laws (c),
\[
(ab)^r = \bigl( \sqrt[n]{a} \, \sqrt[n]{b} \bigr)^m = \bigl( \sqrt[n]{a} \bigr)^m \bigl( \sqrt[n]{b} \bigr)^m = a^r b^r .
\]

(f) Let \( a < b \) and \( r > 0 \). Since \( r = \frac{m}{n} > 0 \) and \( n > 0 \), \( m \ge 1 \). Let \( d \coloneqq \sqrt[n]{b} \). By @lem-root-rules (d), \( 0 < c < d \), and by @lem-reals-nth-root (a) with the exponent \( m \ge 1 \), \( a^r = c^m < d^m = b^r \).
:::
:::

Part (e) needs \( a > 1 \): for \( a = 1 \) every power is \( 1 \), and for \( 0 < a < 1 \) the order reverses, as Exercise C1 shows. Part (f) needs \( r > 0 \): for \( r = 0 \) both sides are \( 1 \).

::: {#exm-rational-power-computations}
[Rational powers by hand]

Compute \( 27^{2/3} \cdot 9^{-1/2} \) and \( \bigl(\frac{16}{81}\bigr)^{-3/4} \). Which is larger, \( 2^{1/2} \) or \( 3^{1/3} \)?
:::

::: {.solution}
Since \( 3 \ge 0 \) and \( 3^3 = 27 \), \( \sqrt[3]{27} = 3 \), so \( 27^{2/3} = 3^2 = 9 \). Since \( \sqrt{9} = 3 \), \( 9^{-1/2} = 3^{-1} = \frac13 \). The product is \( 9 \cdot \frac13 = 3 \).

Since \( \frac23 \ge 0 \) and \( \bigl(\frac23\bigr)^4 = \frac{16}{81} \), \( \sqrt[4]{16/81} = \frac23 \). So \( \bigl(\frac{16}{81}\bigr)^{-3/4} = \bigl(\frac23\bigr)^{-3} = \bigl(\frac32\bigr)^3 = \frac{27}{8} \).

For the comparison, raise both to the sixth power, which clears both roots: by @prp-rational-power-laws (b), \( (2^{1/2})^6 = 2^3 = 8 \) and \( (3^{1/3})^6 = 3^2 = 9 \). Both numbers are positive. If \( 2^{1/2} \ge 3^{1/3} \), then \( 8 \ge 9 \) by @lem-reals-nth-root (a) (or equality), which is false. So \( 2^{1/2} < 3^{1/3} \).
:::

## Means and estimates with roots

Section 1.3 proved the inequality between the means in the form \( a_1 \cdots a_n \le A^n \), without roots, because none were available. With \( n \)-th roots it takes its familiar shape.

::: {#cor-am-gm-roots}
[Geometric Mean Below Arithmetic Mean]

Let \( n \ge 1 \) be an integer and let \( a_1, \dots, a_n \in \nR \) with \( a_k \ge 0 \) for every \( k \). Then
\[
\sqrt[n]{a_1 a_2 \cdots a_n} \le \frac{1}{n} \sum_{k=1}^{n} a_k ,
\]
with equality **if and only if** \( a_1 = a_2 = \dots = a_n \).
:::

::: {.idea}
This is @thm-am-gm with an \( n \)-th root taken on both sides (@exm-method-am-gm bounds the product; the root turns the bound on \( G^n \) into one on \( G \)). Taking roots preserves order by @lem-root-rules (d).
:::

::: {.proof}
Let \( A \coloneqq \frac1n \sum a_k \ge 0 \) and \( G \coloneqq \sqrt[n]{a_1 \cdots a_n} \ge 0 \). By @thm-am-gm (a), \( G^n = a_1 \cdots a_n \le A^n \). If \( G > A \), then \( G^n > A^n \) by @lem-reals-nth-root (a), since \( A \ge 0 \); so \( G \le A \). If \( G = A \), then \( a_1 \cdots a_n = A^n \), and @thm-am-gm (b) gives \( a_1 = \dots = a_n \). Conversely, if all \( a_k \) are equal, then \( a_1 \cdots a_n = A^n \) by @thm-am-gm (b), so \( G = \sqrt[n]{A^n} = A \) by uniqueness, as \( A \ge 0 \).
:::

The last results of this chapter turn roots into estimates. How close to \( 1 \) is \( \sqrt[n]{a} \) for large \( n \)? Write the root as \( 1 + x \) with \( x \ge 0 \). Then \( a = (1 + x)^n \), and a power of \( 1 + x \) is exactly what @exm-method-power-lower-bound bounds from below by one term. A lower bound on \( (1 + x)^n \) is an upper bound on \( x \).

::: {#prp-root-estimates}
[Two Root Estimates]

::: {.enumerate options="label=(\alph*)"}
1. If \( a \in \nR \), \( a \ge 1 \) and \( n \ge 1 \) is an integer, then \( 1 \le \sqrt[n]{a} \le 1 + \dfrac{a - 1}{n} \).
2. If \( n \ge 2 \) is an integer, then \( 1 \le \sqrt[n]{n} \le 1 + \sqrt{\dfrac{2}{n - 1}} \).
:::
:::

::: {.idea}
The method of @exm-method-power-lower-bound, read for a root: write the root as \( 1 + x \), keep one term of \( (1 + x)^n \), solve for \( x \). For (a), Bernoulli's term \( nx \) suffices, because the left side \( a \) is fixed. For (b) the left side is \( n \), which grows, so the linear term gives only \( x \le \frac{n-1}{n} \); the quadratic term \( \binom{n}{2} x^2 \) is needed.
:::

::: {.proof}
In both parts let \( y \) be the number in question, \( y \coloneqq \sqrt[n]{a} \) or \( y \coloneqq \sqrt[n]{n} \), and let \( x \coloneqq y - 1 \). Since \( \sqrt[n]{1} = 1 \) (as \( 1 \ge 0 \) and \( 1^n = 1 \)), @lem-root-rules (d) gives \( y \ge 1 \) whenever the radicand is \( \ge 1 \), with equality if it is \( 1 \). So \( x \ge 0 \), which is the left inequality in both parts.

(a) By @fd2:thm-bernoulli (with \( x \ge 0 \ge -1 \)), \( a = (1 + x)^n \ge 1 + nx \). So \( nx \le a - 1 \), and dividing by \( n > 0 \), \( x \le \frac{a - 1}{n} \).

(b) By @cor-binomial-real (b) with \( k = 2 \le n \), and \( \binom{n}{2} = \frac{n(n-1)}{2} \) (@prp-binomial-factorial (c)),
\[
n = (1 + x)^n \ge \frac{n(n - 1)}{2} x^2 .
\]
Dividing by \( \frac{n(n-1)}{2} > 0 \) gives \( x^2 \le \frac{2}{n - 1} \). Let \( w \coloneqq \sqrt{2/(n - 1)} \ge 0 \). If \( x > w \), then \( x^2 > w^2 = \frac{2}{n-1} \) by @fd3:prp-ordered-ring-rules (g), since \( x, w \ge 0 \); so \( x \le w \).
:::

Both bounds are explicit for every \( n \), so a threshold for any tolerance can be read off. The limit statements follow at once by @fd3:exm-method-limit-from-definition.

::: {#exm-root-limits}
[Roots tend to one]

Show that \( \sqrt[n]{a} \to 1 \) for every real \( a \ge 1 \), and that \( \sqrt[n]{n} \to 1 \).
:::

::: {.solution}
*First limit.* By @prp-root-estimates (a), \( \abs{\sqrt[n]{a} - 1} = \sqrt[n]{a} - 1 \le \frac{a - 1}{n} \) for \( n \ge 1 \). If \( a = 1 \), the sequence is constant. If \( a > 1 \), let \( \varepsilon > 0 \), choose an integer \( N > (a - 1)/\varepsilon \), so \( N \ge 1 \); for \( n \ge N \), \( \abs{\sqrt[n]{a} - 1} \le \frac{a-1}{n} \le \frac{a-1}{N} < \varepsilon \).

*Second limit.* By @prp-root-estimates (b), \( \abs{\sqrt[n]{n} - 1} \le \sqrt{2/(n - 1)} \) for \( n \ge 2 \). Let \( \varepsilon > 0 \) and choose an integer \( N > 1 + 2/\varepsilon^2 \); then \( N \ge 2 \), and \( N \) depends on \( \varepsilon \) only. For \( n \ge N \), \( n - 1 > 2/\varepsilon^2 > 0 \), so \( \frac{2}{n - 1} < \varepsilon^2 \) (@fd3:prp-reciprocal-order (b)), and since square roots preserve strict order between non-negative numbers (@lem-root-rules (d) with \( n = 2 \)), \( \sqrt{2/(n-1)} < \sqrt{\varepsilon^2} = \varepsilon \). Hence \( \abs{\sqrt[n]{n} - 1} < \varepsilon \).
:::

::: {.check}
Find an \( N \) with \( \sqrt[n]{5} < 1.01 \) for every \( n \ge N \).
:::

::: {.solution}
By @prp-root-estimates (a) with \( a = 5 \), \( \sqrt[n]{5} \le 1 + \frac4n \). And \( 1 + \frac4n < 1.01 \) exactly when \( \frac4n < \frac{1}{100} \), that is, \( n > 400 \). So \( N = 401 \) works. (The bound is generous: already \( \sqrt[162]{5} < 1.01 \). The definition asks for some threshold, not the least.)
:::

::: {.remark}
[Looking ahead]

Chapter 8 defines \( a^x \) for every real \( x \) through the exponential function and checks that it agrees with the \( a^r \) of this section; the analysis volumes construct the exponential itself.
:::

## Exercises

### A. Check your understanding

::: {#exr-roots-and-rational-powers-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Where does the proof of @lem-reals-nth-root use that \( \nR \) is complete?
2. Why is \( h \le 1 \) imposed in the case \( s^n < a \) of that proof?
3. Run the first steps of the existence proof for \( n = 3 \), \( a = 8 \): what are \( m \), \( M \) and \( s \)?
4. Compute \( 8^{-2/3} \).
5. True or false: \( (a^r)^s = a^{rs} \) for all real \( a > 0 \) and all \( r, s \in \nQ \).
:::
:::

::: {.solution}
(a) Once: to produce \( s \coloneqq \sup S \), from a non-empty set bounded above. Nothing else in the proof needs it.

(b) So that \( s + h \le s + 1 \). Then each of the \( n \) terms \( (s + h)^k s^{n-1-k} \) is at most \( (s + 1)^{n-1} \), a bound that does not involve \( h \), and \( h \) can be solved for. Without \( h \le 1 \) the terms would grow with \( h \).

(c) \( m = \min\{1, 8\} = 1 \), \( M = \max\{1, 8\} = 8 \), and \( s = \sup\{ y \ge 0 : y^3 \le 8 \} = 2 \): the proof shows \( s^3 = 8 \), and \( 2 \) is the non-negative number with cube \( 8 \).

(d) \( \sqrt[3]{8} = 2 \), so \( 8^{-2/3} = 2^{-2} = \frac14 \).

(e) True: @prp-rational-power-laws (b).
:::

### B. Practice

::: {#exr-roots-and-rational-powers-b1}
[B1: Simplify]

Simplify, for real \( a, b > 0 \):

::: {.enumerate options="label=(\alph*)"}
1. \( 32^{3/5} \);
2. \( \bigl( a^{1/2} b^{-1/3} \bigr)^6 \);
3. \( \dfrac{4^{3/2}}{8^{2/3}} \).
:::
:::

::: {.solution}
(a) \( \sqrt[5]{32} = 2 \), since \( 2^5 = 32 \); so \( 32^{3/5} = 2^3 = 8 \).

(b) By @prp-rational-power-laws (c) and (b), \( (a^{1/2} b^{-1/3})^6 = (a^{1/2})^6 (b^{-1/3})^6 = a^{3} b^{-2} \).

(c) \( 4^{3/2} = (\sqrt 4)^3 = 2^3 = 8 \) and \( 8^{2/3} = (\sqrt[3]{8})^2 = 2^2 = 4 \), so the quotient is \( \frac84 = 2 \).
:::

::: {#exr-roots-and-rational-powers-b2}
[B2: Compare without a calculator]

Put \( 3^{1/3} \), \( 2^{1/2} \) and \( 5^{1/5} \) in increasing order. Justify your answer.
:::

::: {.solution}
Raise all three to the power \( 30 \), a common multiple of \( 3 \), \( 2 \), \( 5 \). By @prp-rational-power-laws (b),
\[
(3^{1/3})^{30} = 3^{10} = 59049 , \quad (2^{1/2})^{30} = 2^{15} = 32768 , \quad (5^{1/5})^{30} = 5^{6} = 15625 .
\]
All three numbers are positive, and for positive \( x, y \), \( x^{30} < y^{30} \) forces \( x < y \): otherwise \( y \le x \) and \( y^{30} \le x^{30} \) by @lem-reals-nth-root (a) (or equality). Hence \( 5^{1/5} < 2^{1/2} < 3^{1/3} \).
:::

::: {#exr-roots-and-rational-powers-b3}
[B3: An explicit N]

Find an \( N \) such that \( \sqrt[n]{n} < 1.1 \) for every \( n \ge N \).
:::

::: {.solution}
By @prp-root-estimates (b), \( \sqrt[n]{n} \le 1 + \sqrt{2/(n - 1)} \) for \( n \ge 2 \), so it suffices that \( \sqrt{2/(n - 1)} < 0.1 \). Both sides are non-negative, so (by @lem-reals-nth-root (a) and @lem-root-rules (d) with exponent \( 2 \)) this holds exactly when \( \frac{2}{n - 1} < 0.01 \), that is, when \( n - 1 > 200 \). So \( N = 202 \) works: for \( n \ge 202 \), \( \sqrt[n]{n} \le 1 + \sqrt{2/(n-1)} < 1.1 \).
:::

### C. Going deeper

::: {#exr-roots-and-rational-powers-c1}
[C1: Exit check: powers of a base below one]

Let \( a \in \nR \) with \( 0 < a < 1 \), and let \( r, s \in \nQ \). Prove:

::: {.enumerate options="label=(\roman*)"}
1. if \( r < s \), then \( a^r > a^s \);
2. if \( r > 0 \), then \( a^r < 1 \).
:::
:::

::: {.solution}
Put \( b \coloneqq \frac1a \). Since \( 0 < a < 1 \), @fd3:prp-reciprocal-order (b) gives \( b > \frac11 = 1 \). For every \( t \in \nQ \), \( 1^t = 1 \): with \( t = \frac{m}{n} \), \( \sqrt[n]{1} = 1 \) by uniqueness (as \( 1 \ge 0 \) and \( 1^n = 1 \)), and \( 1^m = 1 \) for every \( m \in \nZ \) by @prp-integer-power-laws (d). So, by @prp-rational-power-laws (c),
\[
a^t b^t = (ab)^t = 1^t = 1 ,
\]
and \( a^t = (b^t)^{-1} \) for every \( t \in \nQ \).

(i) Let \( r < s \). By @prp-rational-power-laws (e), applied to the base \( b > 1 \), \( b^r < b^s \), and both are positive by part (d). Reciprocals reverse the order between positive numbers (@fd3:prp-reciprocal-order (b)), so
\[
a^r = (b^r)^{-1} > (b^s)^{-1} = a^s .
\]

(ii) Let \( r > 0 \). By (i) with the exponents \( 0 < r \), \( a^r < a^0 \), and \( a^0 = 1 \), since by @prp-rational-power-well-defined \( a^0 \) is the integer power \( a^0 = 1 \).

**Marking scheme.** (10 points)
- 2: \( b = \frac1a > 1 \), with the reason.
- 3: \( a^t = (b^t)^{-1} \), from (c) of the laws and \( 1^t = 1 \).
- 2: the law (e) applied to the base \( b \), not to \( a \).
- 2: the reversal of order under reciprocals, with positivity from (d).
- 1: (ii) from (i), with \( a^0 = 1 \).
Fatal error (0 for the step): applying (e) to a base \( a < 1 \).
:::

::: {#exr-roots-and-rational-powers-c2}
[C2: The compound sequence is bounded]

Show that \( \bigl( 1 + \frac1n \bigr)^n < 3 \) for every integer \( n \ge 1 \).
:::

::: {.solution}
[Hint 1]

Expand by the binomial theorem and compare the term \( \binom{n}{k} \frac{1}{n^k} \) with \( \frac{1}{k!} \).
:::

::: {.solution}
[Hint 2]

By @prp-binomial-factorial (c), \( \binom{n}{k} \dfrac{1}{n^k} = \dfrac{1}{k!} \displaystyle\prod_{j=0}^{k-1} \frac{n - j}{n} \).
:::

::: {.solution}
Let \( n \ge 1 \). By @thm-binomial-commutative-ring with \( x = \frac1n \), \( y = 1 \),
\[
\Bigl( 1 + \frac1n \Bigr)^n = \sum_{k=0}^{n} \binom{n}{k} \frac{1}{n^k} .
\]
The term \( k = 0 \) is \( 1 \). Let \( 1 \le k \le n \). By @prp-binomial-factorial (c), \( \binom{n}{k} k! = \prod_{j=0}^{k-1} (n - j) \), and \( n^k = \prod_{j=0}^{k-1} n \), so
\[
\binom{n}{k} \frac{1}{n^k} = \frac{1}{k!} \prod_{j=0}^{k-1} \frac{n - j}{n} .
\]
For \( 0 \le j \le k - 1 \le n - 1 \), the factor \( \frac{n - j}{n} \) lies in \( (0, 1] \), so the product lies in \( (0, 1] \) (@fd3:prp-ordered-field-halves (d), by induction on the number of factors). Hence the term is at most \( \frac{1}{k!} \), and \( \frac{1}{k!} \le \frac{1}{2^{k-1}} \) by @exm-geometric-comparison. Comparing termwise (@prp-sum-order (a)) and summing the geometric series (@fd2:prp-geometric-sum with \( r = \frac12 \)),
\[
\Bigl( 1 + \frac1n \Bigr)^n \le 1 + \sum_{k=1}^{n} \Bigl( \frac12 \Bigr)^{k-1} = 1 + 2\Bigl( 1 - \frac{1}{2^n} \Bigr) = 3 - \frac{2}{2^n} < 3 ,
\]
where the last step uses \( \frac{2}{2^n} > 0 \).

Together with @exm-am-gm-compound, which showed that the sequence increases, this says the compound sequence is increasing and bounded above by \( 3 \).

**Marking scheme.** (10 points)
- 3: the binomial expansion, with each term written in the factorial form.
- 3: the termwise bound \( \binom{n}{k} n^{-k} \le \frac{1}{k!} \le \frac{1}{2^{k-1}} \), with the factors \( \frac{n-j}{n} \) shown to lie in \( (0, 1] \).
- 2: the geometric sum evaluated correctly.
- 2: the strict inequality \( < 3 \), with its reason.
Fatal error (0 for the step): bounding \( \binom{n}{k} n^{-k} \) by \( \frac{1}{k!} \) without the factor-by-factor reason, or summing the geometric series to infinity.
:::

### R. Review

::: {#exr-roots-and-rational-powers-r1}
[R1]

Compute \( \displaystyle\sum_{k=1}^{n} \frac{1}{\sqrt{k} + \sqrt{k + 1}} \) for \( n \ge 1 \).
:::

::: {.solution}
The tool is telescoping (@exm-method-telescoping). Since \( (\sqrt{k+1} - \sqrt k)(\sqrt{k+1} + \sqrt k) = (k + 1) - k = 1 \), and \( \sqrt k + \sqrt{k+1} \ge 1 > 0 \),
\[
\frac{1}{\sqrt k + \sqrt{k + 1}} = \sqrt{k + 1} - \sqrt k .
\]
With \( b_j \coloneqq \sqrt{j + 1} \) and \( j = k - 1 \), @thm-telescoping (a) gives
\[
\sum_{k=1}^{n} \bigl( \sqrt{k + 1} - \sqrt k \bigr) = \sum_{j=0}^{n-1} (b_{j+1} - b_j) = b_n - b_0 = \sqrt{n + 1} - 1 .
\]
:::

::: {#exr-roots-and-rational-powers-r2}
[R2]

Compute \( \displaystyle\sum_{k=0}^{n} \binom{n}{k} (-2)^k \) for \( n \in \nN \).
:::

::: {.solution}
By the binomial theorem (@thm-binomial-commutative-ring) in \( \nR \) with \( x = -2 \) and \( y = 1 \), the sum is \( (-2 + 1)^n = (-1)^n \).
:::

::: {#exr-roots-and-rational-powers-r3}
[R3]

Prove that \( \dfrac{n + \sqrt n}{n^2 + 1} \to 0 \).
:::

::: {.solution}
The tools are keeping the dominant term (@exm-method-dominant-term) and the limit method (@fd3:exm-method-limit-from-definition). For \( n \ge 1 \), \( n \le n^2 \), so \( \sqrt n \le \sqrt{n^2} = n \) by @lem-root-rules (d) (or equality), where \( \sqrt{n^2} = n \) by uniqueness since \( n \ge 0 \). Hence the numerator is at most \( 2n \), and the denominator is at least \( n^2 > 0 \), so
\[
0 < \frac{n + \sqrt n}{n^2 + 1} \le \frac{2n}{n^2} = \frac{2}{n} \qquad (n \ge 1) .
\]
Let \( \varepsilon > 0 \) and choose an integer \( N > 2/\varepsilon \); then \( N \ge 1 \), and for \( n \ge N \) the distance to \( 0 \) is at most \( 2/n \le 2/N < \varepsilon \).

The look-alike tool, the quotient rule for limits, does not apply to the fraction as written: neither the numerator nor the denominator converges.
:::

<!-- dependency ledger
lem-reals-nth-root (proof): powers of non-negative (positive) reals are non-negative (positive); 0 <= y <= 1 gives y^k <= y, y >= 1 gives y^k >= y; products of ordered non-negatives | induction with @fd3:prp-ordered-ring-rules (c), stated inline (moved verbatim)
lem-reals-nth-root (proof): min{1, a} and max{1, a} exist; trichotomy | @fd3:prp-ordered-field-halves (a) (total order), standard
lem-root-rules (proof): products and powers of non-negative reals are non-negative | @fd3:prp-ordered-ring-rules (c), induction, inline
prp-integer-power-laws (proof): 1^k = 1 for k in N | inline induction
prp-integer-power-laws (proof): a^{-1} != 0 and (a^{-1})^{-1} = a | @fd3:lem-field-fraction-rules (a)
prp-rational-power-well-defined (proof): m/n = p/q with n, q > 0 implies mq = pn | multiplication by nq in the field Q (inside R), inline
prp-rational-power-laws (proof): r < s and n > 0 imply nr < ns; r > 0 with n > 0 implies m >= 1 | @fd3:prp-ordered-ring-rules (c), and m an integer > 0
prp-rational-power-laws (proof): common denominator m'q'/(n'q') = m'/n' | @fd3:lem-field-fraction-rules (b), inline
cor-am-gm-roots (proof): A >= 0 and the product of the a_k is >= 0 | sums and products of non-negatives, @prp-sum-order (b) and @fd3:prp-ordered-ring-rules (c)
prp-root-estimates (proof): dividing an inequality by a positive number; 1^n = 1 | @fd3:prp-ordered-ring-rules (c) with @fd3:prp-reciprocal-order (a); inline
exm-root-limits (solution): an integer N > C exists for every real C | R Archimedean, @fd3:thm-cof-complete-archimedean, as recalled in Section 1.4
exm-rational-power-computations (solution): 2^4 = 16, 3^4 = 81, 2^3 = 8 < 9 = 3^2 | arithmetic; verify/ch01/exm-rational-power-computations.py
exr-roots-and-rational-powers-b2 (solution): 3^10 = 59049, 2^15 = 32768, 5^6 = 15625 | arithmetic; verify/ch01/exr-roots-and-rational-powers-b2.py
exr-roots-and-rational-powers-c1 (solution): 1^m = 1 for m in Z | 1^k = 1 by induction and (d) of prp-integer-power-laws for negative m, inline
exr-roots-and-rational-powers-c2 (solution): binom(n,k)/n^k as (1/k!) times a product of (n-j)/n; a product of factors in (0, 1] lies in (0, 1] | @fd3:lem-field-fraction-rules (b); induction with @fd3:prp-ordered-field-halves (d), inline
exr-roots-and-rational-powers-r1 (solution): (sqrt(k+1) - sqrt k)(sqrt(k+1) + sqrt k) = 1 | ring algebra (@fd3:prp-ring-algebra) and (sqrt x)^2 = x, inline
exr-roots-and-rational-powers-r3 (solution): n^2 + 1 >= n^2 > 0 and inversion | @fd3:prp-ordered-field-halves (c), (d), as in Section 1.4
-->
