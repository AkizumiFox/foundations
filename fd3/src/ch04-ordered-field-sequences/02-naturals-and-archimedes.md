# The Rationals inside an Ordered Field; the Archimedean Property

In an ordered field \( F \) we can form \( 1 \), \( 1 + 1 \), \( 1 + 1 + 1 \), and so on. They look like the natural numbers \( 1, 2, 3, \dots \), but they are elements of \( F \), and two questions need answers before the next section can use them as thresholds. Do they behave like natural numbers, adding, multiplying and comparing as \( \nN \) does? And does every element of \( F \) lie below one of them? For \( \nQ \), Section 2.5 answered the second question with yes (@thm-rationals-archimedean). This section answers the first for every ordered field, and goes further: a whole copy of \( \nQ \) sits inside \( F \), in exactly one way. The second question has the answer no in general. Fields where the answer is yes are called **Archimedean**, and in them every element has an integer part and the rationals are dense.

## The natural numbers in an ordered field

Section 2.3 defined, in any commutative ring \( R \) and for any \( a \in R \), the multiples \( n \cdot a \) for \( n \in \nN \) (just before @prp-ordered-ring-rules): \( 0 \cdot a = 0 \) and \( (n + 1) \cdot a = n \cdot a + a \). With \( a = 1 \) they are the elements \( 0, 1, 1 + 1, \dots \) of the opening paragraph. We give them a name, together with powers, which this chapter needs for estimates such as \( 2^k \ge k + 1 \).

::: {#def-naturals-in-ordered-field}
[Natural Numbers and Powers in an Ordered Field]

Let \( F \) be an ordered field, with unit element \( 1_F \).

::: {.enumerate options="label=(\alph*)"}
1. For \( n \in \nN \), \( n \cdot 1_F \in F \) is the multiple of \( 1_F \) of Section 2.3: the map \( \nN \to F \), \( n \mapsto n \cdot 1_F \), is the unique function with
\[
0 \cdot 1_F = 0 , \qquad (n + 1) \cdot 1_F = n \cdot 1_F + 1_F \quad \text{for every } n \in \nN .
\]
2. For \( x \in F \), the **powers** \( x^k \) (\( k \in \nN \)) are given by @fd2:thm-recursion, read on \( \nN = \omega \) through @cor-omega-identification (b), with \( X = F \), starting value \( 1_F \) and step \( (k, y) \mapsto y x \):
\[
x^0 \coloneqq 1_F , \qquad x^{k+1} \coloneqq x^k x \quad \text{for every } k \in \nN .
\]
:::
:::

The subscript in \( 1_F \) is there because two fields will often be in play, \( F \) and \( \nQ \), each with its own \( 1 \); where only one field is in play the subscript is dropped. For natural numbers \( n, k \), the power \( n^k \in \nN \) is the one of Section 1.6, defined (just before @prp-omega-powers-parity) by the same recursion with \( X = \nN \): \( n^0 = 1 \) and \( n^{k+1} = n^k n \). So \( 2^k \) may mean a natural number or an element of \( F \); part (c) of the next proposition says the two readings match.

**Examples.** \( 1 \cdot 1_F = 0 \cdot 1_F + 1_F = 0 + 1_F = 1_F \), and \( 2 \cdot 1_F = 1_F + 1_F \), the element written \( 2 \) in Section 4.1. Also \( x^1 = 1_F x = x \) and \( x^2 = x x \), which is the square of @prp-ring-algebra (d). The degenerate case: \( 0 \cdot 1_F = 0 \), and \( 0^0 = 1_F \) by the first equation, a convention the recursion imposes and nothing below questions.

**A non-example by minimal change.** Keep the field axioms and drop the order. In the two-element field of @exm-finite-ring-not-orderable, the same recursion gives \( 2 \cdot 1 = 1 + 1 = 0 = 0 \cdot 1 \). So the map \( n \mapsto n \cdot 1 \) is not injective there, and the elements \( 0 \cdot 1, 1 \cdot 1, 2 \cdot 1, \dots \) are not a copy of \( \nN \). The next proposition shows that the order axioms are exactly what prevents this.

::: {#prp-naturals-in-ordered-field}
[The Natural Numbers inside an Ordered Field]

Let \( F \) be an ordered field, and let \( m, n, k \in \nN \).

::: {.enumerate options="label=(\alph*)"}
1. \( (m + n) \cdot 1_F = m \cdot 1_F + n \cdot 1_F \) and \( (mn) \cdot 1_F = (m \cdot 1_F)(n \cdot 1_F) \).
2. If \( m < n \), then \( m \cdot 1_F < n \cdot 1_F \). Hence \( n \mapsto n \cdot 1_F \) is injective, and \( n \cdot 1_F \ge 1_F \) whenever \( n \ge 1 \).
3. \( (n^k) \cdot 1_F = (n \cdot 1_F)^k \). In particular \( (2^k) \cdot 1_F = (2 \cdot 1_F)^k \), the \( k \)-th power in \( F \) of \( 2 = 1 + 1 \).
4. In \( \nQ \), \( n \cdot 1_{\nQ} = j(\iota(n)) \), the image of \( n \) under the embeddings @prp-naturals-embed-integers and @prp-integers-embed-rationals. With the identifications \( \nN \subseteq \nZ \subseteq \nQ \), this says \( n \cdot 1_{\nQ} = n \).
:::
:::

::: {.idea}
Each part is an induction that follows the recursion defining the left side. The product law in (a) is the only one with content: multiplying by \( n + 1 \) is multiplying by \( n \) and adding one more copy, and the sum law and distributivity turn that into the same step on the right. Part (d) compares two functions on \( \nN \) that satisfy the same recursion, and the uniqueness half of the recursion theorem makes them equal.
:::

::: {.proof}
(a) The sum law is @prp-ordered-ring-rules (h) with \( R = F \) and \( a = 1_F \). For the product law, fix \( m \) and use @fd1:ax-induction (through @cor-omega-identification (b)) on \( n \), for \( P(n) \): "\( (mn) \cdot 1_F = (m \cdot 1_F)(n \cdot 1_F) \)". *Base:* \( m \cdot 0 = 0 \) by @def-omega-arithmetic (b), so the left side is \( 0 \cdot 1_F = 0 \), and the right side is \( (m \cdot 1_F) \cdot 0 = 0 \) by @prp-ring-algebra (b). *Step:* assume \( P(n) \). By @def-omega-arithmetic (b) and (c), \( m(n + 1) = mn + m \). Hence
\[
\begin{aligned}
\bigl(m(n + 1)\bigr) \cdot 1_F &= (mn) \cdot 1_F + m \cdot 1_F = (m \cdot 1_F)(n \cdot 1_F) + (m \cdot 1_F) 1_F \\
&= (m \cdot 1_F)(n \cdot 1_F + 1_F) = (m \cdot 1_F)\bigl((n + 1) \cdot 1_F\bigr) ,
\end{aligned}
\]
by the sum law, \( P(n) \) with (F7), (F9), and the recursion of (a) in @def-naturals-in-ordered-field. So \( P(n + 1) \) holds, and \( P(n) \) holds for every \( n \).

(b) Since \( 1_F \ne 0 \) in a field, @prp-ordered-ring-rules (h) gives \( m \cdot 1_F < n \cdot 1_F \) whenever \( m < n \). If \( m \ne n \), then \( m < n \) or \( n < m \) by trichotomy in \( \nN \) (@thm-omega-order (a)), so \( m \cdot 1_F \ne n \cdot 1_F \) by (O1): the map is injective. Finally \( 1 \cdot 1_F = 1_F \) (the examples above), and for \( n > 1 \), \( 1_F = 1 \cdot 1_F < n \cdot 1_F \); so \( n \cdot 1_F \ge 1_F \) for every \( n \ge 1 \).

(c) Fix \( n \) and induct on \( k \). *Base:* \( n^0 = 1 \), so \( (n^0) \cdot 1_F = 1 \cdot 1_F = 1_F = (n \cdot 1_F)^0 \). *Step:* if \( (n^k) \cdot 1_F = (n \cdot 1_F)^k \), then, since \( n^{k+1} = n^k n \),
\[
(n^{k+1}) \cdot 1_F = \bigl((n^k) \cdot 1_F\bigr)(n \cdot 1_F) = (n \cdot 1_F)^k (n \cdot 1_F) = (n \cdot 1_F)^{k+1} ,
\]
by the product law of (a), the hypothesis, and @def-naturals-in-ordered-field (b). The special case is \( n = 2 \), with \( 2 \cdot 1_F = 1_F + 1_F \).

(d) Let \( f(n) \coloneqq j(\iota(n)) \in \nQ \). The zero and one of \( \nZ \) are \( \iota(0) \) and \( \iota(1) \) (@thm-integers-commutative-ring), and \( j \) sends them to the zero and one of \( \nQ \) (@prp-integers-embed-rationals). So \( f(0) = 0 \), and, since \( \iota \) and \( j \) preserve sums (@prp-naturals-embed-integers (a), @prp-integers-embed-rationals),
\[
f(n + 1) = j\bigl(\iota(n) + \iota(1)\bigr) = j(\iota(n)) + j(\iota(1)) = f(n) + 1_{\nQ} .
\]
So \( f \) and \( n \mapsto n \cdot 1_{\nQ} \) both satisfy the recursion of @def-naturals-in-ordered-field (a) with \( F = \nQ \), and by the uniqueness in @fd2:thm-recursion (through @cor-omega-identification (b)) they are equal. This proves the proposition.
:::

So the order axioms do what the non-example above lacked: by (b), the elements \( n \cdot 1_F \) are all different and increase with \( n \), and by (a) they add and multiply as natural numbers do. In \( \nQ \), (d) says that nothing new has happened: \( n \cdot 1_{\nQ} \) is \( n \). When only one field is in play, we will sometimes write \( n \) for \( n \cdot 1_F \) in a general ordered field too; the statements of this section keep \( n \cdot 1_F \), because there the difference between \( n \in \nN \) and its image in \( F \) is the point.

## A copy of the rationals in every ordered field

The copy of \( \nN \) extends. Negatives exist in \( F \), so the integers have images too, and inverses of non-zero elements exist, so fractions have images. The next theorem says that the result is a copy of \( \nQ \), compatible with \( + \), \( \cdot \) and \( < \), and that there is no other way to place \( \nQ \) inside \( F \). Later chapters of this volume use this map to compare an arbitrary ordered field with the rationals.

*Every ordered field contains a copy of \( \nQ \), and only one.*

::: {#thm-rationals-embed-ordered-field}
[The Rationals Embed in Every Ordered Field]

Let \( F \) be an ordered field. There is **exactly one** map \( \iota_F \colon \nQ \to F \) such that, for all \( x, y \in \nQ \),
\[
\begin{gathered}
\iota_F(1) = 1_F , \\
\iota_F(x + y) = \iota_F(x) + \iota_F(y) , \qquad \iota_F(xy) = \iota_F(x)\, \iota_F(y) .
\end{gathered}
\]
It satisfies \( \iota_F(n) = n \cdot 1_F \) for every \( n \in \nN \). It is injective and **strictly increasing** (\( x < y \) implies \( \iota_F(x) < \iota_F(y) \)), and it **reflects order**: \( \iota_F(x) < \iota_F(y) \) implies \( x < y \).
:::

::: {.idea}
Uniqueness tells us how to build \( \iota_F \). A map respecting \( 1 \) and \( + \) must send \( n = 1 + \dots + 1 \) to \( n \cdot 1_F \); respecting negatives, it must send \( -n \) to \( -(n \cdot 1_F) \); and respecting products, it must send \( p/q \) to \( (p \cdot 1_F)(q \cdot 1_F)^{-1} \). So we take that formula as the definition, and the work is to check it. **Step roadmap.** ① Extend \( n \mapsto n \cdot 1_F \) to \( \nZ \) and check that it respects \( + \), \( \cdot \) and negation. ② Define \( \iota_F \) on fractions and check that the value does not depend on the fraction chosen. ③ Check \( + \) and \( \cdot \) with the fraction rules. ④ Check the order. ⑤ Uniqueness: run the opening argument as a proof.
:::

::: {.proof}
**Step 1: the integers.** By @prp-naturals-embed-integers (c), read through the identification \( \nN \subseteq \nZ \), every \( m \in \nZ \) is \( n \) or \( -n \) for some \( n \in \nN \). Define
\[
m \cdot 1_F \coloneqq
\begin{cases}
n \cdot 1_F & \text{if } m = n \text{ with } n \in \nN , \\
-(n \cdot 1_F) & \text{if } m = -n \text{ with } n \in \nN .
\end{cases}
\]
This is well defined. Within one case, \( n \) is determined by \( m \): directly in the first case, and in the second because \( -n = -n' \) gives \( n = n' \) by @prp-ring-algebra (a). The cases overlap only at \( 0 \): if \( n = -n' \) with \( n, n' \in \nN \), then \( n + n' = 0 \), and \( n, n' \ge 0 \) (@thm-integers-ordered-ring (b)); if \( n' > 0 \), then \( n + n' > n + 0 \ge 0 \) by @prp-ordered-ring-rules (b), against \( n + n' = 0 \), so \( n' = 0 \) and then \( n = 0 \). At \( m = 0 \) both cases give \( 0 \), since \( -0 = 0 \).

We check three rules, for \( m, m' \in \nZ \).

*Negation:* \( (-m) \cdot 1_F = -(m \cdot 1_F) \). If \( m = n \in \nN \), this is the second case of the definition. If \( m = -n \), then \( -m = n \) by @prp-ring-algebra (a), and \( (-m) \cdot 1_F = n \cdot 1_F = -\bigl(-(n \cdot 1_F)\bigr) = -(m \cdot 1_F) \).

*Sums:* \( (m + m') \cdot 1_F = m \cdot 1_F + m' \cdot 1_F \). If \( m, m' \in \nN \), this is @prp-naturals-in-ordered-field (a). We write out the mixed case \( m = n \), \( m' = -n' \) with \( n, n' \in \nN \). If \( n' \le n \), then \( n = n' + k \) for some \( k \in \nN \) (@prp-omega-order-arithmetic (a)), so \( m + m' = (n' + k) - n' = k \) in \( \nZ \), and
\[
\begin{aligned}
m \cdot 1_F + m' \cdot 1_F &= (n' + k) \cdot 1_F - n' \cdot 1_F \\
&= n' \cdot 1_F + k \cdot 1_F - n' \cdot 1_F = k \cdot 1_F ,
\end{aligned}
\]
by @prp-naturals-in-ordered-field (a). If \( n < n' \), then \( n' = n + k \), \( m + m' = -k \), and the same computation gives \( n \cdot 1_F - (n + k) \cdot 1_F = -(k \cdot 1_F) = (-k) \cdot 1_F \). The case \( m = -n \), \( m' = n' \) follows by (F1). If \( m = -n \) and \( m' = -n' \), then \( m + m' = -(n + n') \), and \( -\bigl((n + n') \cdot 1_F\bigr) = -(n \cdot 1_F) - (n' \cdot 1_F) \), by the sum law and uniqueness of negatives.

*Products:* \( (m m') \cdot 1_F = (m \cdot 1_F)(m' \cdot 1_F) \). If \( m, m' \in \nN \), this is @prp-naturals-in-ordered-field (a). We write out \( m = -n \), \( m' = n' \): then \( mm' = -(nn') \) by @prp-ring-algebra (c), so
\[
\begin{aligned}
(mm') \cdot 1_F &= -\bigl((nn') \cdot 1_F\bigr) = -\bigl((n \cdot 1_F)(n' \cdot 1_F)\bigr) \\
&= \bigl(-(n \cdot 1_F)\bigr)(n' \cdot 1_F) = (m \cdot 1_F)(m' \cdot 1_F) ,
\end{aligned}
\]
by negation, @prp-naturals-in-ordered-field (a), and @prp-ring-algebra (c) in \( F \). The two remaining sign patterns are the same with signs: \( (-n)(-n') = nn' \) in \( \nZ \) and \( \bigl(-(n \cdot 1_F)\bigr)\bigl(-(n' \cdot 1_F)\bigr) = (n \cdot 1_F)(n' \cdot 1_F) \) in \( F \), both by @prp-ring-algebra (c), and \( m = n \), \( m' = -n' \) follows from the case written out by (F6).

**Step 2: the definition on \( \nQ \).** By @prp-integers-embed-rationals (b), every \( x \in \nQ \) is \( p/q \) for some \( p \in \nZ \) and \( q \in \nZ_{>0} \). Since \( q \in \nZ_{>0} \), that is, \( q \in \nN \) and \( q \ne 0 \), we have \( q \ge 1 \) (@thm-omega-order (d)), and @prp-naturals-in-ordered-field (b) gives \( q \cdot 1_F \ge 1_F > 0 \), so \( q \cdot 1_F \ne 0 \). Define
\[
\iota_F\Bigl(\frac{p}{q}\Bigr) \coloneqq (p \cdot 1_F)(q \cdot 1_F)^{-1} = \frac{p \cdot 1_F}{q \cdot 1_F} .
\]
The value does not depend on the fraction chosen: if \( p/q = r/s \) with \( r \in \nZ \) and \( s \in \nZ_{>0} \), then \( ps = rq \) (@prp-integers-embed-rationals (b)), so \( (p \cdot 1_F)(s \cdot 1_F) = (r \cdot 1_F)(q \cdot 1_F) \) by the product rule of Step 1. Multiplying both sides by \( (q \cdot 1_F)^{-1} (s \cdot 1_F)^{-1} \) and using (F5), (F6), (F8) gives \( (p \cdot 1_F)(q \cdot 1_F)^{-1} = (r \cdot 1_F)(s \cdot 1_F)^{-1} \). So \( \iota_F \) is a function \( \nQ \to F \). For \( m \in \nZ \), \( m = m/1 \), so \( \iota_F(m) = (m \cdot 1_F)(1_F)^{-1} = m \cdot 1_F \); in particular \( \iota_F(n) = n \cdot 1_F \) for \( n \in \nN \), and \( \iota_F(1) = 1_F \).

**Step 3: sums and products.** Let \( x = p/q \) and \( y = r/s \) as in Step 2. In the field \( \nQ \), @lem-field-fraction-rules (b) gives
\[
x + y = \frac{ps + rq}{qs} , \qquad xy = \frac{pr}{qs} ,
\]
with \( qs \in \nZ_{>0} \) by (O4) in \( \nZ \). By the definition, Step 1, and @lem-field-fraction-rules (b) in \( F \),
\[
\begin{aligned}
\iota_F(x + y) &= \frac{(p \cdot 1_F)(s \cdot 1_F) + (r \cdot 1_F)(q \cdot 1_F)}{(q \cdot 1_F)(s \cdot 1_F)} \\
&= \frac{p \cdot 1_F}{q \cdot 1_F} + \frac{r \cdot 1_F}{s \cdot 1_F} = \iota_F(x) + \iota_F(y) ,
\end{aligned}
\]
and in the same way \( \iota_F(xy) = \dfrac{(p \cdot 1_F)(r \cdot 1_F)}{(q \cdot 1_F)(s \cdot 1_F)} = \iota_F(x)\, \iota_F(y) \).

**Step 4: order.** Let \( x < y \) in \( \nQ \). Then \( y - x > 0 \), and writing \( y - x = p/q \) with \( q \in \nZ_{>0} \), the comparison formula (@thm-rationals-ordered-field (a)) gives \( p > 0 \), so \( p \in \nZ_{>0} \) (@thm-integers-ordered-ring (b)). By @prp-naturals-in-ordered-field (b), \( p \cdot 1_F > 0 \) and \( q \cdot 1_F > 0 \); by @prp-reciprocal-order (a) and (O4), \( \iota_F(y - x) > 0 \). By Step 3, \( \iota_F(y) = \iota_F(x) + \iota_F(y - x) > \iota_F(x) \), using (O3). So \( \iota_F \) is strictly increasing. If \( x \ne y \), then \( x < y \) or \( y < x \), and the images differ by (O1): \( \iota_F \) is injective. If \( \iota_F(x) < \iota_F(y) \), then neither \( x = y \) nor \( y < x \) can hold, since they would give \( \iota_F(x) = \iota_F(y) \) or \( \iota_F(y) < \iota_F(x) \), against (O1); so \( x < y \) by trichotomy.

**Step 5: uniqueness.** Let \( \psi \colon \nQ \to F \) satisfy the three equations of the statement. Then \( \psi(0) = \psi(0 + 0) = \psi(0) + \psi(0) \), and adding \( -\psi(0) \) gives \( \psi(0) = 0 \). By @fd1:ax-induction (through @cor-omega-identification (b)), \( \psi(n) = n \cdot 1_F \) for every \( n \in \nN \): the base is \( \psi(0) = 0 = 0 \cdot 1_F \), and \( \psi(n + 1) = \psi(n) + \psi(1) = n \cdot 1_F + 1_F = (n + 1) \cdot 1_F \). For \( x \in \nQ \), \( \psi(x) + \psi(-x) = \psi(0) = 0 \), so \( \psi(-x) = -\psi(x) \) by @prp-ring-algebra (a); hence \( \psi(m) = m \cdot 1_F \) for every \( m \in \nZ \). For \( q \in \nZ_{>0} \), \( \psi(q)\, \psi(q^{-1}) = \psi(1) = 1_F \), so \( \psi(q^{-1}) = (q \cdot 1_F)^{-1} \) by @lem-field-fraction-rules (a). Finally \( p/q = p q^{-1} \) (@prp-integers-embed-rationals (a)), so
\[
\psi\Bigl(\frac{p}{q}\Bigr) = \psi(p)\, \psi(q^{-1}) = (p \cdot 1_F)(q \cdot 1_F)^{-1} = \iota_F\Bigl(\frac{p}{q}\Bigr) .
\]
So \( \psi = \iota_F \). This proves the theorem.
:::

For \( F = \nQ \), the identity map of \( \nQ \) satisfies the three equations, so by uniqueness \( \iota_{\nQ} \) is the identity. In general \( \iota_F \) is the map of Step 2, and it carries \( \nQ \) onto a copy inside \( F \) that adds, multiplies and compares as \( \nQ \) does. So "\( \nQ \subseteq F \)" is an honest abuse of notation, as \( \nN \subseteq \nZ \subseteq \nQ \) was in Chapter 2, and where only one field is in play we write \( q \) for \( \iota_F(q) \). The statements below keep \( \iota_F \) visible.

::: {.remark}
Uniqueness has a consequence that later chapters of this volume use when comparing two ordered fields. Let \( L \) be another ordered field and \( \chi \colon F \to L \) a map with \( \chi(1_F) = 1_L \) that respects \( + \) and \( \cdot \). Then \( \chi \circ \iota_F \colon \nQ \to L \) satisfies the three equations of the theorem, so \( \chi \circ \iota_F = \iota_L \): such a map fixes the rationals.
:::

## The Archimedean property

Section 2.5 proved that every rational lies below a natural number (@thm-rationals-archimedean). By @prp-naturals-in-ordered-field (d), that theorem says: for every \( x \in \nQ \) there is \( n \in \nN \) with \( x < n \cdot 1_{\nQ} \). This statement makes sense in any ordered field, and it deserves a name, because it can fail.

*No element of the field lies above all the natural numbers.*

::: {#def-archimedean-ordered-field}
[Archimedean Ordered Field]

An ordered field \( F \) is **Archimedean** if **for every** \( x \in F \) **there is** \( n \in \nN \) with \( x < n \cdot 1_F \). In symbols,
\[
\forall x \in F \ \ \exists n \in \nN \ \ x < n \cdot 1_F .
\]
:::

In words: whatever element of \( F \) we pick, some natural number, read in \( F \), lies strictly above it. The \( n \) may depend on \( x \); it is chosen after \( x \).

**Examples.** \( \nQ \) is Archimedean: this is @thm-rationals-archimedean, by @prp-naturals-in-ordered-field (d). The constructed real numbers of the next chapter are Archimedean too (proved there). A non-example, \( \nQ(t) \), comes at the end of this section: there the element \( t \) lies above every \( n \cdot 1 \).

**Why the name.** Archimedes used, as an axiom about lengths, that a smaller length laid off often enough exceeds any larger one. That is Exercise B1: in an Archimedean field, for \( y > 0 \) and any \( x \), some multiple \( (n \cdot 1_F) y \) exceeds \( x \). The definition is the case \( y = 1_F \).

The form in which the next section uses the property is about reciprocals, as in @cor-rationals-archimedean-epsilon, now in an arbitrary field.

::: {#prp-archimedean-reciprocal}
[Small Reciprocals in an Archimedean Field]

In an Archimedean ordered field \( F \), **for every** \( \varepsilon \in F_{>0} \) **there is** \( N \in \nZ_{>0} \) such that \( 1/(n \cdot 1_F) < \varepsilon \) **for every** \( n \in \nN \) with \( n \ge N \). In symbols,
\[
\forall \varepsilon \in F_{>0} \ \ \exists N \in \nZ_{>0} \ \ \forall n \in \nN \ \ \Bigl( n \ge N \Rightarrow \frac{1}{n \cdot 1_F} < \varepsilon \Bigr) .
\]
:::

::: {.proof}
Let \( \varepsilon \in F_{>0} \). Then \( 1/\varepsilon > 0 \) by @prp-reciprocal-order (a). By @def-archimedean-ordered-field there is \( N \in \nN \) with \( 1/\varepsilon < N \cdot 1_F \); it depends on \( \varepsilon \). Then \( N \ne 0 \), since \( 0 \cdot 1_F = 0 < 1/\varepsilon \), so \( N \in \nZ_{>0} \). Let \( n \ge N \). Then \( n \cdot 1_F \ge N \cdot 1_F \) (@prp-naturals-in-ordered-field (b), or equality), so \( 0 < 1/\varepsilon < n \cdot 1_F \), and @prp-reciprocal-order (b) gives
\[
\frac{1}{n \cdot 1_F} < \frac{1}{1/\varepsilon} = \varepsilon ,
\]
where \( 1/(1/\varepsilon) = (\varepsilon^{-1})^{-1} = \varepsilon \) by @lem-field-fraction-rules (a).
:::

The order of the quantifiers is as in Section 2.5: \( \varepsilon \) first, then \( N \), depending on \( \varepsilon \), and then **every** \( n \ge N \) at once. That last clause is what Section 4.3 will call "eventually".

::: {.check}
Find \( n \in \nN \) with \( n > 355/113 \) in \( \nQ \). Then find the least \( n \in \nZ_{>0} \) with \( 1/n < 7/500 \).
:::

::: {.solution}
By the comparison formula (@thm-rationals-ordered-field (a)), \( 355/113 < n/1 \) if and only if \( 355 < 113 n \). Since \( 113 \cdot 3 = 339 < 355 \) and \( 113 \cdot 4 = 452 > 355 \), \( n = 4 \) works (and is the least such \( n \)).

For \( n \in \nZ_{>0} \), \( 1/n < 7/500 \) if and only if \( 500 < 7n \). Since \( 7 \cdot 71 = 497 < 500 \) and \( 7 \cdot 72 = 504 > 500 \), the least such \( n \) is \( 72 \); every \( n \ge 72 \) works too, as @prp-archimedean-reciprocal promises.
:::

## Integer part and density

In \( \nQ \), the Archimedean property gave every rational an integer part (@prp-rational-integer-part). The proof used only Archimedes, applied to \( x \) and to \( -x \), and the least-element property of \( \nZ \). So it runs in any Archimedean field, with \( \iota_F \) carrying the integers into \( F \).

::: {#prp-integer-part-ordered-field}
[Integer Part in an Archimedean Field]

Suppose that the ordered field \( F \) is Archimedean. Then for every \( x \in F \) there is **exactly one** \( m \in \nZ \) with
\[
\iota_F(m) \le x < \iota_F(m + 1) .
\]
:::

::: {.idea}
The integer just above \( x \) should be the least integer \( k \) with \( x < \iota_F(k) \). Archimedes applied to \( x \) shows that such \( k \) exist; applied to \( -x \), it bounds them below, so @prp-integer-least-element supplies a least one. The comparisons happen in \( F \), and \( \iota_F \) reflecting order (@thm-rationals-embed-ordered-field) carries them back to \( \nZ \).
:::

::: {.proof}
Let \( x \in F \) and \( S \coloneqq \{ k \in \nZ : x < \iota_F(k) \} \). By @def-archimedean-ordered-field there is \( n \in \nN \) with \( x < n \cdot 1_F = \iota_F(n) \) (@thm-rationals-embed-ordered-field), so \( n \in S \) and \( S \ne \emptyset \). Applied to \( -x \), it gives \( n' \in \nN \) with \( -x < \iota_F(n') \), that is, \( \iota_F(-n') = -\iota_F(n') < x \) (@prp-ordered-ring-rules (a); \( \iota_F \) respects negatives, as in Step 5 of the proof of @thm-rationals-embed-ordered-field). For \( k \in S \), \( \iota_F(-n') < x < \iota_F(k) \), so \( -n' < k \) because \( \iota_F \) reflects order. Thus \( -n' \) is a lower bound of \( S \), and by @prp-integer-least-element \( S \) has a least element \( l \). Let \( m \coloneqq l - 1 \), so \( l = m + 1 \).

*Existence.* \( x < \iota_F(m + 1) \), since \( l \in S \). And \( m \notin S \), since \( m < l \) and \( l \) is least. So \( x < \iota_F(m) \) fails, and \( \iota_F(m) \le x \) by totality (@prp-ordered-field-halves (a)).

*Uniqueness.* Let \( m, m' \in \nZ \) both satisfy the condition, and suppose \( m < m' \). By discreteness (@thm-integers-ordered-ring (c)), \( m + 1 \le m' \), so \( \iota_F(m + 1) \le \iota_F(m') \) (@thm-rationals-embed-ordered-field). Then
\[
x < \iota_F(m + 1) \le \iota_F(m') \le x ,
\]
so \( x < x \), against (O1). By symmetry \( m' < m \) is impossible, so \( m = m' \).
:::

For \( F = \nQ \), \( \iota_{\nQ} \) is the identity and this is @prp-rational-integer-part. The constructed real numbers of the next chapter will use it with \( F \) the new field, where \( m \) is an integer approximant of a number not yet known to be anything else.

Between two rationals there is always a third, their midpoint (Section 2.5). In an Archimedean field more is true: between any two elements, however close, lies a **rational**.

::: {#thm-rationals-dense-ordered-field}
[The Rationals Are Dense in an Archimedean Field]

In an Archimedean ordered field \( F \), for all \( x, y \in F \) with \( x < y \) there is \( q \in \nQ \) with \( x < \iota_F(q) < y \).
:::

::: {.idea}
Look for \( q \) with denominator \( n \): we need an integer \( k \) with \( n x < k < n y \), after scaling by \( n \). Integers are spaced \( 1 \) apart, so such a \( k \) exists once the scaled gap \( n(y - x) \) exceeds \( 1 \); that is where Archimedes enters, through @prp-archimedean-reciprocal. The integer to take is the one just above \( n x \), which the integer part supplies.
:::

::: {.proof}
Since \( y - x > 0 \), @prp-archimedean-reciprocal gives \( n \in \nZ_{>0} \) with \( 1/(n \cdot 1_F) < y - x \). Let \( c \coloneqq n \cdot 1_F \), which is positive (@prp-naturals-in-ordered-field (b)). Multiplying by \( c \) (@prp-ordered-ring-rules (c)) gives \( 1_F < c(y - x) = c y - c x \), by (F9) and @prp-ring-algebra (c); adding \( c x \) by (O3), \( c x + 1_F < c y \). Let \( m \) be the integer part of \( c x \) (@prp-integer-part-ordered-field), so that \( \iota_F(m) \le c x < \iota_F(m + 1) \). Then
\[
c x < \iota_F(m + 1) = \iota_F(m) + 1_F \le c x + 1_F < c y ,
\]
by @thm-rationals-embed-ordered-field and @prp-ordered-ring-rules (b). Multiplying by \( c^{-1} > 0 \) (@prp-reciprocal-order (a), @prp-ordered-ring-rules (c)) gives \( x < \iota_F(m + 1) c^{-1} < y \). Let \( q \coloneqq (m + 1)/n \in \nQ \). Since \( c = \iota_F(n) \) and \( \iota_F \) respects products, \( \iota_F(q)\, c = \iota_F(m + 1) \), so \( \iota_F(q) = \iota_F(m + 1) c^{-1} \), and \( x < \iota_F(q) < y \).
:::

Applied again, the theorem shows that an interval of an Archimedean field contains infinitely many rationals (Exercise C1). Chapters 5 and 6 use the theorem with \( F \) a field of real numbers, to approximate every real number by rationals.

## A field that is not Archimedean

Section 2.5 proved the Archimedean property of \( \nQ \) from the construction of \( \nQ \): every rational is a quotient of integers. Nothing in (F1)–(F9) and (O1)–(O4) forces it. The standard witness uses polynomials, which this volume has not built; *Algebraic Preliminaries*, Chapter 4 builds them as formal polynomials. We use the school algebra of polynomials in this one example, and say so. No proof of a numbered result in this chapter cites it; it serves only as a counterexample, in prose, warnings and exercises.

::: {#exm-rational-function-field}
[A Non-Archimedean Ordered Field]

Let \( \nQ(t) \) be the set of quotients \( p/q \) of polynomials \( p, q \) in an indeterminate \( t \) with rational coefficients, \( q \ne 0 \), where \( p/q = r/s \) means \( ps = rq \), with the usual sum and product of fractions. Call \( p/q \) **positive** if the leading coefficients of \( p \) and \( q \) have the same sign. With this positive set, \( \nQ(t) \) is an ordered field; we state this and do not verify it. Show that \( t > n \cdot 1 \) for every \( n \in \nN \), so that \( \nQ(t) \) is **not** Archimedean, and that \( 0 < 1/t < 1/(n \cdot 1) \) for every \( n \ge 1 \).
:::

::: {.solution}
In \( \nQ(t) \) the element \( n \cdot 1 \) is the constant polynomial \( n \), by the recursion of @def-naturals-in-ordered-field (a) and the addition of constants. The difference \( t - n \cdot 1 = (t - n)/1 \) has numerator \( t - n \), with leading coefficient \( 1 \), and denominator \( 1 \), with leading coefficient \( 1 \). The signs agree, so \( t - n \cdot 1 \) is positive, that is, \( n \cdot 1 < t \) (@prp-order-from-positives). This holds for every \( n \in \nN \), so \( x = t \) has no \( n \) with \( x < n \cdot 1 \): \( \nQ(t) \) is not Archimedean.

Next, \( 1/t \) has numerator \( 1 \) and denominator \( t \), both with leading coefficient \( 1 \), so \( 1/t > 0 \). For \( n \ge 1 \), @lem-field-fraction-rules (c) gives
\[
\frac{1}{n \cdot 1} - \frac{1}{t} = \frac{t - n}{n t} ,
\]
whose numerator has leading coefficient \( 1 \) and whose denominator \( n t \) has leading coefficient \( n > 0 \). So the difference is positive, and \( 1/t < 1/(n \cdot 1) \).
:::

::: {.warning}
The Archimedean property does not follow from the ordered-field axioms: \( \nQ(t) \) satisfies (F1)–(F9) and (O1)–(O4) and fails it. So in a general ordered field the move "take \( \varepsilon = 1/n \)" does not reach every \( \varepsilon \): in \( \nQ(t) \), the tolerance \( \varepsilon = 1/t \) is below every \( 1/n \). Each later use of "\( 1/n \) eventually drops below \( \varepsilon \)" must name the Archimedean property.
:::

The density theorem fails in \( \nQ(t) \) too, so its hypothesis is needed. There \( 0 < 1/t \), and no rational lies strictly between them. Suppose \( q \in \nQ \) had \( 0 < \iota(q) < 1/t \), with \( \iota \) the embedding of @thm-rationals-embed-ordered-field for \( \nQ(t) \). Then \( q > 0 \), because \( \iota \) reflects order. By @prp-reciprocal-order (b) and @lem-field-fraction-rules (a), \( t = 1/(1/t) < 1/\iota(q) = \iota(1/q) \). By @thm-rationals-archimedean, \( 1/q < n \) for some \( n \in \nN \), so \( \iota(1/q) < \iota(n) = n \cdot 1 \), and \( t < n \cdot 1 \), against the example.

## Exercises

### A. Check your understanding

::: {#exr-naturals-and-archimedes-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Write "\( F \) is **not** Archimedean" in symbols, moving the negation inside by @fd1:prp-quantifier-negation.
2. Give two different elements of \( \nQ(t) \) (@exm-rational-function-field) that lie above every \( n \cdot 1 \).
3. In an ordered field, can \( n \cdot 1_F = 0 \) for some \( n \ge 1 \)? Give a reason.
4. What is \( \iota_{\nQ} \)? Which part of @thm-rationals-embed-ordered-field tells you?
:::
:::

::: {.solution}
(a) The definition is \( \forall x \in F \ \exists n \in \nN \ \ x < n \cdot 1_F \). By @fd1:prp-quantifier-negation, in its bounded form @fd1:prp-bounded-quantifier-negation, applied twice, its negation is \( \exists x \in F \ \forall n \in \nN \ \ \neg (x < n \cdot 1_F) \), and by totality (@prp-ordered-field-halves (a)) \( \neg (x < n \cdot 1_F) \) is \( n \cdot 1_F \le x \):
\[
\exists x \in F \ \ \forall n \in \nN \ \ n \cdot 1_F \le x .
\]

(b) \( t \), as in @exm-rational-function-field, and \( t + 1 \), since \( t + 1 > t > n \cdot 1 \). Also \( t^2 \): \( t^2 - n \cdot 1 = (t^2 - n)/1 \) has leading coefficients \( 1 \) and \( 1 \).

(c) No. By @prp-naturals-in-ordered-field (b), \( n \cdot 1_F \ge 1_F > 0 \) for \( n \ge 1 \). (The two-element field of @exm-finite-ring-not-orderable has \( 2 \cdot 1 = 0 \), and it cannot be ordered.)

(d) The identity map of \( \nQ \): it satisfies \( \mathrm{id}(1) = 1 \) and respects \( + \) and \( \cdot \), and the theorem says **exactly one** map does.
:::

### B. Practice

::: {#exr-naturals-and-archimedes-b1}
[B1: Archimedes' form]

Suppose the ordered field \( F \) is Archimedean, and take \( x \in F \) and \( y \in F_{>0} \). Prove that there is \( n \in \nN \) with \( (n \cdot 1_F)\, y > x \).
:::

::: {.solution}
Since \( y > 0 \), \( y^{-1} > 0 \) (@prp-reciprocal-order (a)). By @def-archimedean-ordered-field applied to \( x/y \), there is \( n \in \nN \) with \( x/y < n \cdot 1_F \). Multiplying by \( y > 0 \) (@prp-ordered-ring-rules (c)) gives \( (x y^{-1}) y < (n \cdot 1_F) y \), and \( (x y^{-1}) y = x (y^{-1} y) = x \) by (F5), (F6), (F8). Hence \( (n \cdot 1_F) y > x \).
:::

::: {#exr-naturals-and-archimedes-b2}
[B2: Smaller than every reciprocal]

::: {.enumerate options="label=(\alph*)"}
1. Let \( F \) be Archimedean, and let \( x \in F \) satisfy \( 0 \le x < 1/(n \cdot 1_F) \) for every \( n \in \nN \) with \( n \ge 1 \). Prove that \( x = 0 \).
2. Give an element \( x \ne 0 \) of \( \nQ(t) \) (@exm-rational-function-field) with this property.
:::
:::

::: {.solution}
(a) Suppose, for \( \rulename{\neg I} \) (@fd1:def-rules-negation), that \( x \ne 0 \). Then \( x > 0 \), since \( x \ge 0 \). By @prp-archimedean-reciprocal with \( \varepsilon \coloneqq x \), there is \( N \in \nZ_{>0} \) with \( 1/(N \cdot 1_F) < x \). The hypothesis with \( n = N \ge 1 \) gives \( x < 1/(N \cdot 1_F) \). By (O2), \( x < x \), against (O1). So \( x = 0 \).

(b) \( x = 1/t \): by @exm-rational-function-field, \( 0 < 1/t < 1/(n \cdot 1) \) for every \( n \ge 1 \), and \( 1/t \ne 0 \). So part (a) fails without the Archimedean hypothesis.
:::

::: {#exr-naturals-and-archimedes-b3}
[B3: Rationals with a power of two as denominator]

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( 2^k \ge k + 1 \) in \( \nQ \) for every \( k \in \nN \).
2. Let \( a, b \in \nQ \) with \( a < b \). Prove that there are \( m \in \nZ \) and \( k \in \nN \) with \( a < (m + 1)/2^k < b \).
3. Carry out the construction of (b) for \( a = 1/3 \), \( b = 1/2 \), taking \( k \) least with \( 1/(k + 1) < b - a \).
:::

*Hint: follow the proof of @thm-rationals-dense-ordered-field, with \( 2^k \) in place of \( n \).*
:::

::: {.solution}
(a) Read \( 2^k \) as \( (2^k) \cdot 1_{\nQ} = (2 \cdot 1_{\nQ})^k \) (@prp-naturals-in-ordered-field (c), (d)). We use @fd1:ax-induction (through @cor-omega-identification (b)) on \( k \) for \( P(k) \): "\( (2^k) \cdot 1_{\nQ} \ge (k + 1) \cdot 1_{\nQ} \)". *Base:* \( 2^0 = 1 = 0 + 1 \), so both sides are \( 1 \cdot 1_{\nQ} \). *Step:* assume \( P(k) \). Then
\[
\begin{aligned}
(2^{k+1}) \cdot 1_{\nQ} &= \bigl((2^k) \cdot 1_{\nQ}\bigr)(2 \cdot 1_{\nQ}) \ge \bigl((k + 1) \cdot 1_{\nQ}\bigr)(2 \cdot 1_{\nQ}) \\
&= (2k + 2) \cdot 1_{\nQ} \ge (k + 2) \cdot 1_{\nQ} ,
\end{aligned}
\]
by @prp-naturals-in-ordered-field (a) and \( 2^{k+1} = 2^k \cdot 2 \); then @prp-ordered-field-halves (d), all factors being non-negative by @prp-naturals-in-ordered-field (b); then (a) again with \( (k + 1) 2 = 2k + 2 \) (@thm-omega-arithmetic-laws); and finally @prp-naturals-in-ordered-field (b), since \( k + 2 \le 2k + 2 \). This is \( P(k + 1) \).

(b) By @prp-archimedean-reciprocal with \( F = \nQ \) and \( \varepsilon \coloneqq b - a > 0 \), there is \( k \in \nN \) with \( 1/(k + 1) < b - a \) (take \( k + 1 \ge N \)). By (a) and @prp-ordered-field-halves (c), \( 1/2^k \le 1/(k + 1) < b - a \). Let \( m \coloneqq \floor{2^k a} \) (@prp-rational-integer-part), so that \( m \le 2^k a < m + 1 \). Then \( 2^k a < m + 1 \le 2^k a + 1 \), so
\[
a < \frac{m + 1}{2^k} \le a + \frac{1}{2^k} < b ,
\]
dividing by \( 2^k > 0 \) (@prp-ordered-ring-rules (c), @prp-reciprocal-order (a)) and using \( 1/2^k < b - a \) with (O3).

(c) \( b - a = 1/6 \). For \( k \in \nN \), \( 1/(k + 1) < 1/6 \) if and only if \( 6 < k + 1 \), so the least \( k \) is \( 6 \), with \( 2^6 = 64 \). Then \( 2^6 a = 64/3 \), and \( \floor{64/3} = 21 \), since \( 21 \cdot 3 = 63 \le 64 < 66 = 22 \cdot 3 \). So \( (m + 1)/2^k = 22/64 = 11/32 \). Check: \( 1/3 < 11/32 \) since \( 32 < 33 \), and \( 11/32 < 1/2 \) since \( 22 < 32 \). (The bound \( 1/2^k \le 1/(k + 1) \) is far from sharp: \( k = 3 \) already gives \( 3/8 \).)
:::

### C. Going deeper

::: {#exr-naturals-and-archimedes-c1}
[C1: Many rationals, and rational approximation]

Throughout, \( F \) is an Archimedean ordered field.

::: {.enumerate options="label=(\alph*)"}
1. Let \( x < y \) in \( F \). Prove that the set \( S \coloneqq \{ q \in \nQ : x < \iota_F(q) < y \} \) is infinite (@fd2:def-infinite).
2. Let \( x \in F \) and \( n \in \nZ_{>0} \). Prove that there is \( q \in \nQ \) with \( \iota_F(q) \le x < \iota_F(q + 1/n) \).
:::
:::

::: {.solution}
[Hint 1]

For (a), apply @thm-rationals-dense-ordered-field twice; for (b), apply @prp-integer-part-ordered-field to a multiple of \( x \).
:::

::: {.solution}
[Hint 2]

For (a): let \( r, s \in \nQ \) with \( x < \iota_F(r) < \iota_F(s) < y \); it is enough to find infinitely many rationals strictly between \( r \) and \( s \). For (b): let \( m \) be the integer part of \( (n \cdot 1_F) x \).
:::

::: {.solution}
(a) By @thm-rationals-dense-ordered-field there is \( s \in \nQ \) with \( x < \iota_F(s) < y \), and, applied to \( x < \iota_F(s) \), there is \( r \in \nQ \) with \( x < \iota_F(r) < \iota_F(s) \). Then \( r < s \), since \( \iota_F \) reflects order (@thm-rationals-embed-ordered-field). For \( k \in \nZ_{>0} \), let
\[
s_k \coloneqq r + \frac{s - r}{k + 1} \in \nQ .
\]
Since \( k + 1 > 1 > 0 \), \( 0 < 1/(k + 1) < 1 \) (@prp-reciprocal-order), so \( 0 < (s - r)/(k + 1) < s - r \) (@prp-ordered-ring-rules (c)), and \( r < s_k < s \) by (O3). As \( \iota_F \) is strictly increasing, \( x < \iota_F(r) < \iota_F(s_k) < \iota_F(s) < y \), so \( s_k \in S \). If \( k < l \), then \( 1/(l + 1) < 1/(k + 1) \) (@prp-reciprocal-order (b), @prp-naturals-in-ordered-field (b)), so \( s_l < s_k \): the map \( k \mapsto s_k \) is injective. Suppose \( S \) were finite, with \( m \) elements for some \( m \in \nN \) (@fd2:def-finite). The map \( \{1, \dots, m + 1\} \to S \), \( k \mapsto s_k \), would be injective, against @fd2:cor-pigeonhole-finite-sets (a). So \( S \) is infinite.

(b) Let \( c \coloneqq n \cdot 1_F > 0 \) and let \( m \) be the integer part of \( c x \) (@prp-integer-part-ordered-field): \( \iota_F(m) \le c x < \iota_F(m + 1) \). Multiplying by \( c^{-1} > 0 \) (@prp-ordered-ring-rules (c), with equality allowed on the left) gives \( \iota_F(m) c^{-1} \le x < \iota_F(m + 1) c^{-1} \). Let \( q \coloneqq m/n \). Since \( c = \iota_F(n) \) and \( \iota_F \) respects products, \( \iota_F(m) c^{-1} = \iota_F(m/n) = \iota_F(q) \) and \( \iota_F(m + 1) c^{-1} = \iota_F\bigl((m + 1)/n\bigr) = \iota_F(q + 1/n) \), using \( (m + 1)/n = m/n + 1/n \) (@lem-field-fraction-rules (b) in \( \nQ \)). So \( \iota_F(q) \le x < \iota_F(q + 1/n) \).

**Marking scheme.** (10 points)
- 2: (a) obtains two rationals \( r < s \) inside the interval, by density twice, with \( r < s \) justified (order reflected).
- 2: (a) exhibits infinitely many distinct rationals between \( r \) and \( s \) (any explicit injective family, or an induction producing one more each time), each checked to lie strictly between.
- 2: (a) concludes that \( S \) is infinite from an injection, citing a finiteness result (pigeonhole or subsets of finite sets).
- 2: (b) applies the integer part to \( (n \cdot 1_F) x \).
- 2: (b) divides by \( n \cdot 1_F > 0 \) and identifies the bounds as \( \iota_F(q) \), \( \iota_F(q + 1/n) \).
Fatal errors (0 for the step): using density in an arbitrary ordered field (the Archimedean hypothesis must be named); "infinitely many because the construction never stops" with no injection and no finiteness result; dividing by \( n \cdot 1_F \) without its sign.
:::

::: {#exr-naturals-and-archimedes-c2}
[C2: Where the proof for the rationals breaks]

In \( \nQ(t) \) (@exm-rational-function-field):

::: {.enumerate options="label=(\alph*)"}
1. Show that the set \( \{ n \cdot 1 : n \in \nN \} \) is bounded above.
2. The proof of @thm-rationals-archimedean shows that every rational lies below a natural number. Which step of that proof has no analogue for the element \( t \) of \( \nQ(t) \)? Prove that it has none.
:::
:::

::: {.solution}
(a) By @exm-rational-function-field, \( n \cdot 1 < t \) for every \( n \in \nN \), so \( t \) is an upper bound.

(b) The first step: "write \( x = p/q \) with \( p \in \nZ \) and \( q \in \nZ_{>0} \)". The rest of the proof (the case split on the sign of \( p \), discreteness of \( \nZ \), the comparison formula) works for any element of the form \( \iota(p)/\iota(q) \) of an ordered field, with \( \iota = \iota_{\nQ(t)} \). But \( t \) is not of this form. Indeed, \( \iota(p)/\iota(q) = \iota(p/q) \) by @thm-rationals-embed-ordered-field; if \( t = \iota(r) \) with \( r \in \nQ \), then @thm-rationals-archimedean gives \( n \in \nN \) with \( r < n \), so \( t = \iota(r) < \iota(n) = n \cdot 1 \), against (a). So \( t \) is not the image of any rational, and the proof has nothing to start from.

**Marking scheme.** (10 points)
- 3: (a) exhibits an upper bound and justifies it from the positive set of \( \nQ(t) \).
- 3: (b) names the representation \( x = p/q \) with integers \( p, q \) as the step that fails.
- 4: (b) proves that \( t \) is not \( \iota(r) \) for any rational \( r \), using the Archimedean property of \( \nQ \) and that \( \iota \) is strictly increasing.
Fatal errors (0 for the step): naming the comparison formula or discreteness as the failing step (both hold for images of rationals); asserting that \( t \) "is not a fraction" without proof.
:::

::: {#exr-naturals-and-archimedes-c3}
[C3: The order of the rationals is the only one]

Prove that the usual order of \( \nQ \) (@def-rational-order) is the only relation \( < \) on \( \nQ \) that makes \( \nQ \), with its usual operations, an ordered field.
:::

::: {.solution}
[Hint 1]

Which elements must be positive in any such order? Start with \( 1 \), then \( n \cdot 1 \), then \( p/q \).
:::

::: {.solution}
[Hint 2]

By @prp-order-from-positives, an order on a commutative ring is determined by its set of positive elements. Let \( P \) be the positive set of an order \( \prec \) making \( \nQ \) an ordered field; show \( P = \nQ_{>0} \).
:::

::: {.solution}
Let \( \prec \) be a relation making \( \nQ \) an ordered field, and \( P \coloneqq \{ x \in \nQ : 0 \prec x \} \). By @prp-order-from-positives, \( P \) satisfies (P1) and (P2), and \( x \prec y \) holds if and only if \( y - x \in P \). The usual order has positive set \( \nQ_{>0} \) (@thm-rationals-ordered-field) and is described by \( \nQ_{>0} \) in the same way. So it suffices to prove \( P = \nQ_{>0} \).

The multiples \( n \cdot 1_{\nQ} \) are defined by the recursion of @def-naturals-in-ordered-field (a), which uses only addition, so they do not depend on the order; by @prp-naturals-in-ordered-field (d), \( n \cdot 1_{\nQ} = n \). Applying @prp-ordered-ring-rules (h) to the ordered field \( (\nQ, \prec) \), in which \( 1 \ne 0 \), gives \( 0 \prec n \) for every \( n \in \nZ_{>0} \): so \( \nZ_{>0} \subseteq P \).

Let \( x \in \nQ_{>0} \). Then \( x = p/q \) with \( p, q \in \nZ_{>0} \) (@prp-integers-embed-rationals (b) and the comparison formula, @thm-rationals-ordered-field (a)), so \( x = p \cdot q^{-1} \). Here \( p, q \in P \), so \( q^{-1} \in P \) by @prp-reciprocal-order (a) applied in \( (\nQ, \prec) \), and \( x \in P \) by (P1). Hence \( \nQ_{>0} \subseteq P \).

Conversely, let \( x \in P \). Then \( x \ne 0 \) by (P2). If \( x \notin \nQ_{>0} \), then \( x < 0 \) in the usual order, so \( -x \in \nQ_{>0} \subseteq P \); but then both \( x \) and \( -x \) lie in \( P \), against (P2). So \( x \in \nQ_{>0} \), and \( P = \nQ_{>0} \). Hence \( \prec \) is the usual order.

**Marking scheme.** (10 points)
- 2: reduces the claim to the positive sets, citing @prp-order-from-positives.
- 2: shows every positive integer is positive for the new order, noting that \( n \cdot 1 \) does not depend on the order.
- 3: shows every usual-positive \( p/q \) is in \( P \), via inverses and products.
- 3: shows \( P \subseteq \nQ_{>0} \) by (P2).
Fatal errors (0 for the step): assuming \( 1 \succ 0 \) without \( 1 \ne 0 \) or a rule; using the usual order's comparison formula to compare elements in the new order.
:::

<!-- dependency ledger
def-naturals-in-ordered-field (claim): N-powers n^k are F3.1's (recursion before prp-omega-powers-parity) | F3.1 §06 (defined there, unlabeled; pointed to via prp-omega-powers-parity)
def-naturals-in-ordered-field (example): 0 + 1_F = 1_F | def-commutative-ring-and-field (F1), (F3)
prp-naturals-in-ordered-field (proof): n + 1 = S(n) and m S(n) = mn + m on omega | def-omega-arithmetic (b), (c) (cited)
prp-naturals-in-ordered-field (proof): the zero and one of Q are j(0), j(1) | prp-integers-embed-rationals (j(0) = 0, j(1) = 1; cited)
thm-rationals-embed-ordered-field (proof): naturals are distinct as integers (identification) | prp-naturals-embed-integers (a), injective (cited)
thm-rationals-embed-ordered-field (proof): (n' + k) - n' = k in Z; -(n + n') = (-n) + (-n') | prp-naturals-embed-integers (a) (iota preserves +), prp-ring-algebra (a) (uniqueness of negatives); inline
thm-rationals-embed-ordered-field (proof): Z_{>0} is a subset of N, and q >= 1 for q in Z_{>0} | thm-integers-ordered-ring (b), (c) (cited at Step 2 via prp-naturals-in-ordered-field (b); identification)
thm-rationals-embed-ordered-field (proof): q s in Z_{>0} for q, s in Z_{>0} | (O4) in Z with thm-integers-ordered-ring (b)
thm-rationals-embed-ordered-field (proof): p/q = j(p)/j(q), so lem-field-fraction-rules applies in Q | prp-integers-embed-rationals (a) (cited in Step 5)
prp-integer-part-ordered-field (proof): iota_F(-n') = -iota_F(n') | thm-rationals-embed-ordered-field, Step 5 argument (psi(-x) = -psi(x)), pointed to in the proof
prp-integer-part-ordered-field (proof): l - 1 < l in Z | (O3) with 0 < 1 (prp-ordered-ring-rules (e)); inline
thm-rationals-dense-ordered-field (proof): iota_F(m + 1) = iota_F(m) + 1_F | thm-rationals-embed-ordered-field (additive, iota_F(1) = 1_F)
thm-rationals-dense-ordered-field (claim): Chapters 5 and 6 use it with F a field of real numbers | prose pointer (F3.10, F3.4); nothing here depends on it
def-archimedean-ordered-field (claim): the constructed reals of the next chapter are Archimedean | prose pointer (F3.10); nothing here depends on it
exm-rational-function-field (example): school polynomial algebra (degree, leading coefficient, leading coefficient of a product), Q(t) is an ordered field with the stated positive set, n.1 is the constant polynomial n | school fact; formal polynomials in F4.4 (flagged in the text; nothing in a proof depends on it)
exm-rational-function-field (claim): density fails in Q(t) (paragraph after the warning) | school facts of the example (as above); otherwise cited
exr-naturals-and-archimedes-a1 (solution): t + 1 > t, t^2 - n has leading coefficient 1 | (O3) with 1 > 0; school polynomial algebra (as for the example)
exr-naturals-and-archimedes-b3 (solution): (k + 1) 2 = 2k + 2 and k + 2 <= 2k + 2 in N | thm-omega-arithmetic-laws (cited), prp-omega-order-arithmetic (a)
exr-naturals-and-archimedes-b3 (solution): 1/6, 64/3, floor 21, 11/32 and the comparisons | verify/ch04/exr-naturals-and-archimedes-b3.py
exr-naturals-and-archimedes-c1 (solution): {1, ..., m + 1} has m + 1 elements | fd2 def-finite (identity bijection), run on omega by cor-omega-identification
exr-naturals-and-archimedes-c2 (solution): the rest of the proof of thm-rationals-archimedean works for images iota(p)/iota(q) | inline claim (the proof uses only the representation, discreteness of Z and the comparison formula, as F3.2 remarks after it)
exr-naturals-and-archimedes-c3 (solution): n.1 is defined by + alone, independent of the order | def-naturals-in-ordered-field (a) (cited)
def-archimedean-ordered-field (solution): the Quick check, 355 < 452, 339 < 355, 497 < 500 < 504 | verify/ch04/def-archimedean-ordered-field.py
-->
