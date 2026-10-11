# The Rationals Inside the Cuts, and a Complete Ordered Field

This section is part of the optional Chapter 7, and nothing outside the chapter depends on it. Section 7.4 finished the arithmetic: by @thm-cuts-ordered-field the cuts form an ordered field \( \nR_{\mathrm D} \), with zero \( D_0 \) and one \( D_1 \). Three questions are left before \( \nR_{\mathrm D} \) can be called a model of the real numbers. Do the rational cuts \( D_q \) form a faithful copy of \( \nQ \), with the arithmetic of \( \nQ \)? Is the new field complete? And does the cut \( \sigma \) of @exm-cut-sqrt2, built to sit at the gap of \( \nQ \), really square to \( D_2 \)? This section answers all three with yes. On the Cauchy road, Section 5.4 asked the first question about the map \( \kappa \) (@thm-rational-embedding), and Sections 5.5 and 5.6 together answered the second; here the second answer is already in hand, from Section 7.2.

## A copy of the rationals

Every ordered field \( F \) contains a copy of \( \nQ \): by @thm-rationals-embed-ordered-field there is exactly one map \( \iota_F \colon \nQ \to F \) that sends \( 1 \) to \( 1_F \) and respects sums and products, and it is strictly increasing. For \( F = \nR_{\mathrm D} \) we have a candidate in hand, the map \( q \mapsto D_q \) of @def-rational-cut. It sends \( 1 \) to \( D_1 \), the one of the field. The theorem below checks the rest: sums and positive products by computing with sets, negatives and the other signs by the field rules; and the uniqueness clause then says the candidate is \( \iota_{\nR_{\mathrm D}} \).

::: {#thm-rationals-embed-cuts}
[The Rationals Inside the Cuts]

The map \( \nQ \to \nR_{\mathrm D} \), \( q \mapsto D_q \), is injective, and for all \( p, q \in \nQ \):

::: {.enumerate options="label=(\alph*)"}
1. \( p < q \) if and only if \( D_p < D_q \);
2. \( D_p + D_q = D_{p+q} \);
3. \( -D_q = D_{-q} \);
4. \( D_p D_q = D_{pq} \);
5. \( D_1 \) is the one of the ordered field \( \nR_{\mathrm D} \) of @thm-cuts-ordered-field.
:::

Consequently \( D_q = \iota_{\nR_{\mathrm D}}(q) \) for every \( q \in \nQ \), where \( \iota_{\nR_{\mathrm D}} \) is the map of @thm-rationals-embed-ordered-field.
:::

::: {.idea}
The identity (b), and (d) for positive \( p, q \), are equalities of sets of rationals, so each has two halves. The \( \subseteq \) halves are closure: if \( r < p \) and \( s < q \), then \( r + s < p + q \). The \( \supseteq \) halves must **split** a given rational \( x < p + q \) as a sum of something below \( p \) and something below \( q \), and the obvious split \( x = p + (x - p) \) fails, because \( p \notin D_p \). So we take a little off both summands: half the gap \( p + q - x \) from each. For products we do the same with a factor instead of a summand. Signs other than "both positive" are reduced to that case, the chapter's named move of reducing to the positive case (Section 7.4); since \( \nR_{\mathrm D} \) is already known to be a field, the ring rules for signs do the reduction.
:::

::: {.proof}
Throughout, \( \nR_{\mathrm D} \) is an ordered field (@thm-cuts-ordered-field), so the rules of @prp-ordered-ring-rules hold in it as well as in \( \nQ \).

*(a)* If \( p < q \), then \( p \in D_q \), so \( D_p \subsetneq D_q \) by @prp-rational-in-cut (a) applied to the cut \( D_q \); that is, \( D_p < D_q \) (@def-cut-order). Conversely, if \( D_p \subsetneq D_q \), then @prp-rational-in-cut (a), applied to the cut \( D_q \) and the rational \( p \), gives \( p \in D_q \), that is, \( p < q \).

*Injectivity.* If \( p \ne q \), then \( p < q \) or \( q < p \) by trichotomy (O1) in \( \nQ \), and (a) gives \( D_p \ne D_q \) in either case.

*(b)* \( (\subseteq) \) An element of \( D_p + D_q \) is \( r + s \) with \( r < p \) and \( s < q \) (@def-cut-sum), and \( r + s < p + q \) by @prp-ordered-ring-rules (b). \( (\supseteq) \) Let \( x \in \nQ \) with \( x < p + q \), and put
\[
\delta \coloneqq \frac{p + q - x}{2} > 0 .
\]
Then \( p - \delta < p \) and \( q - \delta < q \), so \( p - \delta \in D_p \) and \( q - \delta \in D_q \), and \( (p - \delta) + (q - \delta) = p + q - 2\delta = x \). Hence \( x \in D_p + D_q \).

*(c)* By (b), \( D_q + D_{-q} = D_{q + (-q)} = D_0 \). By @thm-cut-additive-inverse, also \( D_q + (-D_q) = D_0 \). The negative of an element of the commutative ring \( \nR_{\mathrm D} \) is unique (@prp-ring-algebra (a)), so \( -D_q = D_{-q} \).

*(d), both positive.* Let \( p > 0 \) and \( q > 0 \). By (a), \( D_p > D_0 \) and \( D_q > D_0 \), so the product is that of @def-cut-product-positive:
\[
D_p D_q = \{ x \in \nQ : x \le rs \text{ for some } r \in D_p, \ s \in D_q \text{ with } r > 0, \ s > 0 \} .
\]
\( (\subseteq) \) If \( 0 < r < p \) and \( 0 < s < q \), then \( rs < ps < pq \) by @prp-ordered-ring-rules (c), used twice. So \( x \le rs \) gives \( x < pq \).

\( (\supseteq) \) Let \( x < pq \). If \( x \le 0 \), take \( r \coloneqq p/2 \) and \( s \coloneqq q/2 \): they are positive, lie in \( D_p \) and \( D_q \), and \( x \le 0 < rs \). If \( 0 < x < pq \), put
\[
\lambda \coloneqq \frac{1}{2} \Bigl( 1 + \frac{x}{pq} \Bigr) , \qquad r \coloneqq \lambda p , \qquad s \coloneqq \frac{x}{\lambda p} .
\]
Since \( 0 < x/(pq) < 1 \), the midpoint \( \lambda \) satisfies \( x/(pq) < \lambda < 1 \). Hence \( 0 < r < p \); and \( s > 0 \), with \( s < q \) because this is equivalent, after multiplying by \( \lambda p > 0 \), to \( x < \lambda pq \), that is, to \( x/(pq) < \lambda \). So \( r \in D_p \), \( s \in D_q \), both are positive, and \( rs = x \). Hence \( x \in D_p D_q \).

*(d), the other signs.* If \( p = 0 \) or \( q = 0 \), then one factor is \( D_0 \), so \( D_p D_q = D_0 \) by @def-cut-product, and \( D_{pq} = D_0 \). For negative entries, (c) gives \( D_p = -D_{-p} \) for every \( p \), since \( -(-\alpha) = \alpha \) (@prp-ring-algebra (a)). If \( p < 0 < q \), then by the sign rule \( (-a)b = -(ab) \) of @prp-ring-algebra (c) in \( \nR_{\mathrm D} \) (in the cut model it is part of @lem-cut-sign-rules) and the positive case,
\[
D_p D_q = (-D_{-p}) D_q = -(D_{-p} D_q) = -D_{-pq} = D_{pq} ,
\]
the last step by (c). The case \( q < 0 < p \) follows by commutativity of the product. If \( p < 0 \) and \( q < 0 \), then the rule \( (-a)(-b) = ab \) of @prp-ring-algebra (c) and the positive case give
\[
D_p D_q = (-D_{-p})(-D_{-q}) = D_{-p} D_{-q} = D_{(-p)(-q)} = D_{pq} .
\]

*(e)* This is part of @thm-cuts-ordered-field.

*The consequence.* By (e), (b) and (d), the map \( q \mapsto D_q \) sends \( 1 \) to the one of \( \nR_{\mathrm D} \) and respects sums and products. By the uniqueness clause of @thm-rationals-embed-ordered-field, applied to the ordered field \( F = \nR_{\mathrm D} \), it is \( \iota_{\nR_{\mathrm D}} \). This proves the theorem.
:::

So the rationals live inside \( \nR_{\mathrm D} \) as the rational cuts, with their order and arithmetic unchanged. From now on, a computation with rational cuts may be done in \( \nQ \) and carried over: \( D_{1/2} + D_{1/3} = D_{5/6} \), \( D_{-2} D_3 = D_{-6} \), \( D_2^{-1} = D_{1/2} \). The last one holds because \( D_2 D_{1/2} = D_1 \) by (d), and in a field the inverse is the only element with that property (@lem-field-fraction-rules (a)).

::: {.check}
In the \( (\supseteq) \) half of (b), why not write \( x = p + (x - p) \)? It has \( x - p < q \).
:::

::: {.solution}
Because \( p \notin D_p \): the cut \( D_p \) consists of the rationals **strictly** below \( p \). The split must take something from \( p \) as well, and \( \delta > 0 \) is that something. The flawed proof of Exercise C2 of Section 7.3 falls into the same trap, with \( 0 \notin D_0 \).
:::

On the Cauchy road the same theorem was @thm-rational-embedding, and its proof was a computation with constant sequences. There the sum of two constant sequences is the constant sequence of the sum, termwise. Here the sum of two rational cuts is not obviously a rational cut, and the \( \supseteq \) half needs the room that \( \delta \) provides.

::: {#prp-cut-union-of-rationals .optional}
[A Cut Is the Union of the Rational Cuts Below It]

For every cut \( \alpha \),
\[
\alpha = \bigcup \{ D_q : q \in \alpha \} = \sup \{ D_q : q \in \alpha \} .
\]
:::

::: {.proof}
\( (\supseteq) \) If \( q \in \alpha \) and \( r < q \), then \( r \in \alpha \) by (C2) of @def-dedekind-cut; so \( D_q \subseteq \alpha \). \( (\subseteq) \) If \( p \in \alpha \), then (C3) gives \( p' \in \alpha \) with \( p' > p \), and \( p \in D_{p'} \). This proves the first equality. The set \( \{ D_q : q \in \alpha \} \) is non-empty, since \( \alpha \ne \emptyset \), and bounded above by \( \alpha \), by the \( \supseteq \) half; so by @thm-dedekind-lub its supremum is its union.
:::

The proposition is the cut model's way of saying that every real number is approached from below by rationals. Nothing later in the chapter uses it.

## Between two cuts there is a rational cut

In \( \nQ \) between two rationals lies a third, their midpoint. In an Archimedean field, @thm-rationals-dense-ordered-field puts a rational between any two elements. For \( \nR_{\mathrm D} \) we prove the corresponding statement directly from the cut conditions. We do not yet know that \( \nR_{\mathrm D} \) is Archimedean, and the direct proof is shorter anyway.

::: {#thm-cut-rationals-dense}
[The Rational Cuts Are Dense]

Let \( \alpha \) and \( \beta \) be cuts with \( \alpha < \beta \). Then there is \( q \in \nQ \) with \( \alpha < D_q < \beta \).
:::

*Try it first (ten minutes): given cuts \( \alpha < \beta \), which rational would you put between them, and why is one point of \( \beta \setminus \alpha \) not quite enough?*

::: {.idea}
Since \( \alpha \subsetneq \beta \), there is a rational \( p \) in \( \beta \) but not in \( \alpha \), and the natural guess is \( q = p \). By @prp-rational-in-cut, \( p \notin \alpha \) gives \( \alpha \subseteq D_p \) (part (b)), and \( p \in \beta \) gives \( D_p \subsetneq \beta \) (part (a)). So \( \alpha \le D_p < \beta \). The first inequality need not be strict: for \( \alpha = D_1 \), \( \beta = D_2 \) and \( p = 1 \), the guess gives \( D_p = \alpha \). The cure is to move up once more **inside** \( \beta \): condition (C3) of \( \beta \) gives \( p' \in \beta \) above \( p \), and \( D_{p'} \) is strictly above \( D_p \), so strictly above \( \alpha \), and still strictly below \( \beta \).
:::

::: {.proof}
Since \( \alpha \subsetneq \beta \) (@def-cut-order), there is \( p \in \beta \) with \( p \notin \alpha \). By (C3) of @def-dedekind-cut for \( \beta \), there is \( p' \in \beta \) with \( p' > p \). Then:

- \( \alpha \subseteq D_p \), by @prp-rational-in-cut (b), since \( p \notin \alpha \);
- \( D_p \subsetneq D_{p'} \), by @thm-rationals-embed-cuts (a), since \( p < p' \);
- \( D_{p'} \subsetneq \beta \), by @prp-rational-in-cut (a), since \( p' \in \beta \).

Hence \( \alpha \subsetneq D_{p'} \subsetneq \beta \), that is, \( \alpha < D_{p'} < \beta \). Take \( q \coloneqq p' \).
:::

Each hypothesis has a job. "\( \alpha < \beta \)" supplies \( p \), and the strictness is needed: for \( \alpha = \beta \) there is nothing strictly between. Condition (C3), used for \( \beta \), supplies the second step up; without it, \( D_1 \) and the set \( \{ r \in \nQ : r \le 1 \} \) would be two "cuts", the first strictly inside the second, with no \( D_q \) strictly between them: \( D_1 \subsetneq D_q \) forces \( q > 1 \), and then \( D_q \) contains \( (1 + q)/2 > 1 \), which the second set lacks.

::: {.warning}
"Dense" does not mean that every cut is rational. The rational cuts are dense, and still \( \sigma \) of @exm-cut-sqrt2 is not one of them, as @prp-cut-sqrt2-square below proves. Density says only that between two cuts there is a rational cut, never that a cut **is** one.
:::

::: {.check}
Name a rational \( q \) with \( \sigma < D_q < D_{3/2} \), and check both inequalities.
:::

::: {.solution}
Take \( q = 29/20 \). Then \( q > 0 \) and \( q^2 = 841/400 > 800/400 = 2 \), so \( q \notin \sigma \), and @prp-rational-in-cut (b) gives \( \sigma \subseteq D_q \). The inclusion is strict: \( 10/7 > 0 \) and \( (10/7)^2 = 100/49 > 98/49 = 2 \), so \( 10/7 \notin \sigma \), while \( 10/7 < 29/20 \) (\( 200/140 < 203/140 \)), so \( 10/7 \in D_q \). Hence \( \sigma < D_q \). And \( 29/20 < 30/20 = 3/2 \), so \( D_q < D_{3/2} \) by @thm-rationals-embed-cuts (a). The rational \( q = 10/7 \) works the same way, with \( 17/12 \) as the witness of strictness: \( (17/12)^2 = 289/144 > 2 \) and \( 17/12 < 10/7 \) (\( 119/84 < 120/84 \)).
:::

## Archimedes in the cuts

An ordered field is Archimedean (@def-archimedean-ordered-field) if no element lies above every \( n \cdot 1_F \), \( n \in \nN \). In \( \nR_{\mathrm D} \), \( n \cdot 1 = \iota_{\nR_{\mathrm D}}(n) = D_n \), by @thm-rationals-embed-ordered-field and @thm-rationals-embed-cuts. A cut is bounded inside \( \nQ \) by any rational it misses, and \( \nQ \) is Archimedean, so the property comes almost for free.

::: {#prp-cuts-archimedean .optional}
[The Cuts Are Archimedean]

For every cut \( \alpha \) there is \( n \in \nN \) with \( \alpha < D_n \). Hence \( \nR_{\mathrm D} \) is an Archimedean ordered field.
:::

::: {.proof}
By (C1) of @def-dedekind-cut there is \( b \in \nQ \) with \( b \notin \alpha \), and @prp-rational-in-cut (b) gives \( \alpha \subseteq D_b \). By @thm-rationals-archimedean there is \( n \in \nN \) with \( b < n \), so \( D_b < D_n \) by @thm-rationals-embed-cuts (a). Hence \( \alpha < D_n = n \cdot 1_{\nR_{\mathrm D}} \), which is @def-archimedean-ordered-field for \( \nR_{\mathrm D} \).
:::

## The square root of two

The cut \( \sigma \coloneqq \{ p \in \nQ : p \le 0 \text{ or } p^2 < 2 \} \) of @exm-cut-sqrt2 was introduced as "the rationals below \( \sqrt 2 \)". Now that cuts can be multiplied, that description becomes a theorem: \( \sigma \sigma = D_2 \). The proof is the chapter's multiplicative form of **walk up by \( \varepsilon \)**, @lem-cut-multiplicative-step: step up by a factor \( \mu > 1 \) until you leave \( \sigma \).

::: {#prp-cut-sqrt2-square}
[The Cut of the Square Root of Two]

The cut \( \sigma \) of @exm-cut-sqrt2 satisfies \( \sigma > D_0 \) and \( \sigma \sigma = D_2 \). Consequently \( \sigma \ne D_q \) for every \( q \in \nQ \).
:::

::: {.idea}
The \( \subseteq \) half is a bound: two positive elements of \( \sigma \) have squares below \( 2 \), so their product has square below \( 4 \). The \( \supseteq \) half must write a given \( x < 2 \) as a product \( rs \) of positive elements of \( \sigma \). Small \( x \) are easy: \( x \le 1 \cdot 1 \). For \( 1 \le x < 2 \) we want \( r \in \sigma \) with \( r^2 > x \), since then \( s \coloneqq x/r \) is smaller than \( r \) and so lies in \( \sigma \). Such an \( r \) is found by walking up by a factor: if \( r \in \sigma \) and \( \mu r \notin \sigma \), then \( r^2 \ge 2/\mu^2 \), and this exceeds \( x \) as soon as \( \mu^2 < 2/x \). So we need a rational \( \mu > 1 \) with \( \mu^2 < 2/x \), written down without square roots.
:::

::: {.proof}
*\( \sigma > D_0 \).* Every \( p < 0 \) has \( p \le 0 \), so \( D_0 \subseteq \sigma \); and \( 0 \in \sigma \setminus D_0 \). Hence \( D_0 \subsetneq \sigma \). So \( \sigma \sigma \) is the product of @def-cut-product-positive.

*\( (\subseteq) \)* Let \( x \in \sigma \sigma \), so \( x \le rs \) with \( r, s \in \sigma \), \( r > 0 \), \( s > 0 \). Since \( r > 0 \) and \( r \in \sigma \), \( r^2 < 2 \); likewise \( s^2 < 2 \). By @prp-ordered-ring-rules (c), used twice, \( (rs)^2 = r^2 s^2 < 2 s^2 < 4 = 2^2 \). Since \( rs \ge 0 \) and \( 2 \ge 0 \), @prp-ordered-ring-rules (g) gives \( rs < 2 \). So \( x < 2 \) and \( x \in D_2 \).

*\( (\supseteq) \), small \( x \).* Let \( x < 1 \). Then \( 1 \in \sigma \), since \( 1^2 = 1 < 2 \), and \( x \le 1 \cdot 1 \) with \( r = s = 1 \) positive. So \( x \in \sigma \sigma \). This covers every \( x \le 0 \) as well.

*\( (\supseteq) \), \( 1 \le x < 2 \).* Put
\[
t \coloneqq \frac{2}{x} - 1 , \qquad \mu \coloneqq 1 + \frac{t}{3} .
\]
Since \( 1 \le x < 2 \), we have \( 1 < 2/x \le 2 \), so \( 0 < t \le 1 \) and \( \mu > 1 \). Moreover \( t^2/9 < t/3 \), because this is equivalent to \( t < 3 \). Hence
\[
\mu^2 = 1 + \frac{2t}{3} + \frac{t^2}{9} < 1 + \frac{2t}{3} + \frac{t}{3} = 1 + t = \frac{2}{x} .
\]
Since \( \sigma > D_0 \) and \( \mu > 1 \), @lem-cut-multiplicative-step gives \( r \in \sigma \) with \( r > 0 \) and \( \mu r \notin \sigma \). As \( \mu r > 0 \) and \( \mu r \notin \sigma \), the definition of \( \sigma \) gives \( (\mu r)^2 \ge 2 \), so
\[
r^2 \ge \frac{2}{\mu^2} > x ,
\]
the second inequality because \( \mu^2 < 2/x \). Put \( s \coloneqq x/r \). Then \( s > 0 \), and \( s < r \) because \( x < r^2 \). Since \( r \in \sigma \), (C2) of @def-dedekind-cut gives \( s \in \sigma \). Finally \( rs = x \), so \( x \in \sigma \sigma \).

So \( \sigma \sigma = D_2 \).

*The consequence.* Suppose \( \sigma = D_q \) for some \( q \in \nQ \). Then \( D_0 < D_q \), so \( q > 0 \) by @thm-rationals-embed-cuts (a). By @thm-rationals-embed-cuts (d), \( D_{q^2} = D_q D_q = \sigma \sigma = D_2 \), and by injectivity \( q^2 = 2 \). This contradicts @thm-no-rational-square-two. Hence \( \sigma \ne D_q \) for every \( q \in \nQ \).
:::

The constant \( \mu \) depends on \( x \) only, and it is chosen before \( r \): the lemma is applied to the fixed factor \( \mu \), and it returns \( r \). For \( x = 3/2 \), for instance, \( t = 1/3 \) and \( \mu = 10/9 \), with \( \mu^2 = 100/81 < 108/81 = 4/3 = 2/x \). Exercise C1 of Section 7.1 proved \( \sigma \ne D_q \) directly from the definition; the proof above gets it as a by-product of \( \sigma \sigma = D_2 \) and needs no step below a rational \( q \) with \( q^2 > 2 \).

::: {.check}
Why does the case \( 1 \le x < 2 \) need @lem-cut-multiplicative-step, while the case \( x < 1 \) does not? Where in the \( (\supseteq) \) half is the hypothesis \( x < 2 \) used?
:::

::: {.solution}
For \( x < 1 \) the fixed element \( 1 \in \sigma \) already gives \( x \le 1 \cdot 1 \). For \( x \ge 1 \) no fixed pair works for all \( x \): we need \( r \in \sigma \) with \( r^2 > x \), and how close to the gap \( r \) must be depends on how close \( x \) is to \( 2 \). The hypothesis \( x < 2 \) is used to get \( 2/x > 1 \), so \( t > 0 \) and \( \mu > 1 \), which the lemma requires.
:::

## A complete ordered field

The last question has the shortest answer. Completeness in the sense of @def-complete-ordered-field asks that every non-empty subset bounded above have a supremum for the order \( \le \) of the field. In \( \nR_{\mathrm D} \), that order is inclusion (@def-cut-order), and @thm-dedekind-lub found the supremum: the union.

::: {#thm-cuts-complete-field}
[The Cuts Form a Complete Ordered Field]

\( \nR_{\mathrm D} \), with the sum of @def-cut-sum, the product of @def-cut-product and the order of @def-cut-order, is a complete ordered field (@def-complete-ordered-field).
:::

::: {.proof}
By @thm-cuts-ordered-field, \( \nR_{\mathrm D} \) is an ordered field. Its relation \( \le \) ("\( < \) or \( = \)", @def-ordered-ring-and-field) is "\( \subsetneq \) or \( = \)", that is, \( \subseteq \), the order of @def-cut-order. Let \( A \subseteq \nR_{\mathrm D} \) be non-empty and bounded above for this order. By @thm-dedekind-lub, \( \bigcup A \) is a cut and is the supremum of \( A \) in \( (\nR_{\mathrm D}, \le) \). So every non-empty subset bounded above has a supremum, and \( \nR_{\mathrm D} \) is complete.
:::

That is the whole proof, and it is the point of the chapter's comparison. On the Cauchy road, Section 5.5 proved that every Cauchy sequence of real numbers converges, and Section 5.6 then needed bisection and the Archimedean property to reach suprema (@thm-cauchy-archimedean-lub). On the Dedekind road the supremum is a union, and all the work went into the arithmetic of Sections 7.3 and 7.4.

With this theorem, @thm-cof-complete-archimedean gives a second proof of @prp-cuts-archimedean: every complete ordered field is Archimedean. By @thm-cof-uniqueness, \( \nR_{\mathrm D} \) is therefore a copy of the field \( \nR \) of Chapter 5, by exactly one order-preserving field isomorphism. Section 7.6 writes that isomorphism down.

## Exercises

### A. Check your understanding

::: {#exr-rationals-inside-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Which result shows that the map \( q \mapsto D_q \) is the map \( \iota_{\nR_{\mathrm D}} \) of @thm-rationals-embed-ordered-field, and which property of \( \iota_{\nR_{\mathrm D}} \) does that argument use?
2. True or false, with a reason from the cut conditions: every cut is a union of rational cuts.
3. In the proof of @thm-cut-rationals-dense, the rational \( p \in \beta \setminus \alpha \) was not used directly. Give cuts \( \alpha < \beta \) and a rational \( p \in \beta \setminus \alpha \) with \( D_p = \alpha \).
4. True or false: if \( \alpha \) is a cut and \( \alpha \ne D_q \) for every \( q \in \nQ \), then \( \alpha \alpha \ne D_r \) for every \( r \in \nQ \).
:::
:::

::: {.solution}
(a) @thm-rationals-embed-cuts. Parts (b), (d) and (e) say that \( q \mapsto D_q \) respects sums and products and sends \( 1 \) to the one of \( \nR_{\mathrm D} \); the **uniqueness** clause of @thm-rationals-embed-ordered-field says only one map \( \nQ \to \nR_{\mathrm D} \) does that, namely \( \iota_{\nR_{\mathrm D}} \).

(b) True. Let \( \alpha \) be a cut. For \( q \in \alpha \), (C2) gives \( D_q \subseteq \alpha \), so the union of the \( D_q \) with \( q \in \alpha \) is contained in \( \alpha \). Conversely, for \( q \in \alpha \), (C3) gives \( q' \in \alpha \) with \( q' > q \), and then \( q \in D_{q'} \). So \( \alpha \) is the union of the rational cuts \( D_q \), \( q \in \alpha \). (This is the optional proposition on unions of rational cuts in this section; the argument above does not need it.)

(c) \( \alpha = D_1 \), \( \beta = D_2 \), \( p = 1 \): then \( 1 \in D_2 \), \( 1 \notin D_1 \), and \( D_p = D_1 = \alpha \). So \( D_p \) is not strictly above \( \alpha \), and the proof moves up to \( p' \in \beta \) with \( p' > p \).

(d) False. \( \sigma \) is not rational (@prp-cut-sqrt2-square), and \( \sigma \sigma = D_2 \) is.
:::

### B. Practice

::: {#exr-rationals-inside-b1}
[B1]

Let \( p, q \in \nQ \) with \( p < 0 < q \). Prove that \( D_p D_q = D_{pq} \) directly from the case distinction of @def-cut-product, using the positive case of @thm-rationals-embed-cuts (d) and part (c), but not the ring rules for signs (@prp-ring-algebra (c), @lem-cut-sign-rules).
:::

::: {.solution}
By @thm-rationals-embed-cuts (a), \( D_p < D_0 < D_q \). So neither factor is \( D_0 \), the signs differ, and @def-cut-product gives
\[
D_p D_q = -\bigl( \abs{D_p} \abs{D_q} \bigr) .
\]
Since \( D_q \ge D_0 \), \( \abs{D_q} = D_q \). Since \( D_p < D_0 \), \( \abs{D_p} = -D_p \), and \( -D_p = D_{-p} \) by @thm-rationals-embed-cuts (c). Now \( -p > 0 \) and \( q > 0 \), so the positive case of (d) gives \( D_{-p} D_q = D_{(-p)q} = D_{-pq} \). Hence \( D_p D_q = -D_{-pq} = D_{pq} \), the last step by (c) again.
:::

::: {#exr-rationals-inside-b2}
[B2]

Let \( \rho \coloneqq \{ p \in \nQ : p \le 0 \text{ or } p^2 < 3 \} \). Exercise B2 of Section 7.1 shows that \( \rho \) is a cut (there the set is written with \( p < 0 \); since \( 0^2 < 3 \), it is the same set). Prove that \( \rho > D_0 \) and \( \rho \rho = D_3 \).

*Hint: follow @prp-cut-sqrt2-square, and check that the same \( \mu \) still works when \( 2/x \) is replaced by \( 3/x \).*
:::

::: {.solution}
*\( \rho > D_0 \).* \( D_0 \subseteq \rho \), since \( p < 0 \) gives \( p \le 0 \), and \( 0 \in \rho \setminus D_0 \).

*\( (\subseteq) \)* If \( x \le rs \) with \( r, s \in \rho \) positive, then \( r^2 < 3 \) and \( s^2 < 3 \), so \( (rs)^2 = r^2 s^2 < 3 s^2 < 9 = 3^2 \) by @prp-ordered-ring-rules (c), and \( rs < 3 \) by @prp-ordered-ring-rules (g), since \( rs, 3 \ge 0 \). So \( x < 3 \).

*\( (\supseteq) \)* Let \( x < 3 \). If \( x < 1 \), then \( x \le 1 \cdot 1 \) with \( 1 \in \rho \). Let \( 1 \le x < 3 \), and put \( t \coloneqq 3/x - 1 \) and \( \mu \coloneqq 1 + t/3 \). Then \( 1 < 3/x \le 3 \), so \( 0 < t \le 2 \) and \( \mu > 1 \). Since \( t < 3 \), \( t^2/9 < t/3 \), and
\[
\mu^2 = 1 + \frac{2t}{3} + \frac{t^2}{9} < 1 + t = \frac{3}{x} .
\]
By @lem-cut-multiplicative-step (\( \rho > D_0 \), \( \mu > 1 \)) there is \( r \in \rho \), \( r > 0 \), with \( \mu r \notin \rho \). Then \( (\mu r)^2 \ge 3 \), so \( r^2 \ge 3/\mu^2 > x \). Put \( s \coloneqq x/r \): then \( 0 < s < r \), so \( s \in \rho \) by (C2), and \( rs = x \). So \( x \in \rho\rho \).

Hence \( \rho \rho = D_3 \).

The only change from \( \sigma \) is the range of \( t \): now \( t \) can be as large as \( 2 \), and the inequality \( t^2/9 < t/3 \) still holds, because it needs only \( t < 3 \).
:::

### C. Going deeper

::: {#exr-rationals-inside-c1}
[C1: An irrational cut in every gap]

Prove that between any two cuts \( \alpha < \beta \) lies a cut that is not rational: there is a cut \( \gamma \) with \( \alpha < \gamma < \beta \) and \( \gamma \ne D_r \) for every \( r \in \nQ \).
:::

::: {.solution}
[Hint 1]

Build an irrational cut between \( D_0 \) and \( D_1 \) from \( \sigma \), then move it with rational coefficients.
:::

::: {.solution}
[Hint 2]

By @thm-cut-rationals-dense, used twice, there are rationals \( q, q' \) with \( \alpha < D_q < D_{q'} < \beta \).
:::

::: {.solution}
*Two rationals.* By @thm-cut-rationals-dense there is \( q \in \nQ \) with \( \alpha < D_q < \beta \); applied again to \( D_q < \beta \), it gives \( q' \) with \( D_q < D_{q'} < \beta \). By @thm-rationals-embed-cuts (a), \( q < q' \).

*An irrational cut between \( D_0 \) and \( D_1 \).* Since \( 1^2 < 2 \), \( 1 \in \sigma \), so \( D_1 < \sigma \) (@prp-rational-in-cut (a)). Since \( 3/2 > 0 \) and \( (3/2)^2 = 9/4 > 2 \), \( 3/2 \notin \sigma \), so \( \sigma \subseteq D_{3/2} \) (@prp-rational-in-cut (b)), and \( D_{3/2} < D_2 \) (@thm-rationals-embed-cuts (a)). Hence \( D_1 < \sigma < D_2 \). Adding \( -D_1 = D_{-1} \) (translation in the ordered field \( \nR_{\mathrm D} \), @thm-cuts-ordered-field, and @thm-rationals-embed-cuts (b), (c)) gives \( D_0 < \sigma - D_1 < D_1 \).

*The cut.* Put \( \gamma \coloneqq D_q + D_{q' - q} (\sigma - D_1) \). Since \( q' > q \), \( D_{q' - q} > D_0 \) by @thm-rationals-embed-cuts (a), and multiplying by it preserves strict inequalities (@prp-ordered-ring-rules (c) in \( \nR_{\mathrm D} \)), so
\[
D_0 < D_{q' - q} (\sigma - D_1) < D_{q' - q} D_1 = D_{q' - q} .
\]
Adding \( D_q \) gives \( D_q < \gamma < D_q + D_{q' - q} = D_{q'} \). Hence \( \alpha < D_q < \gamma < D_{q'} < \beta \).

*\( \gamma \) is not rational.* Suppose \( \gamma = D_r \). In the field \( \nR_{\mathrm D} \), \( D_{q' - q} \ne D_0 \) has the inverse \( D_{1/(q' - q)} \) (by (d), \( D_{q'-q} D_{1/(q'-q)} = D_1 \)). Solving for \( \sigma \),
\[
\sigma = D_1 + D_{1/(q' - q)} (D_r - D_q) = D_{1 + (r - q)/(q' - q)} ,
\]
by @thm-rationals-embed-cuts (b), (c), (d). This contradicts @prp-cut-sqrt2-square. So \( \gamma \) is not rational.

**Marking scheme.** (10 points)
- 2: two rationals \( q < q' \) with \( \alpha < D_q < D_{q'} < \beta \), from density used twice.
- 3: a non-rational cut strictly between \( D_0 \) and \( D_1 \) (or between any two rational cuts), with both inequalities proved.
- 3: the affine image lies strictly between \( D_q \) and \( D_{q'} \), using the order rules of the ordered field \( \nR_{\mathrm D} \) with a positive factor.
- 2: the image is not rational, because rational cuts are closed under the field operations (@thm-rationals-embed-cuts).
Fatal errors (0 for the step): treating \( \sigma \) as a number "\( \sqrt 2 \)" with decimal digits; claiming \( \sigma - D_1 < D_1 \) without a rational bound such as \( 3/2 \notin \sigma \).
:::

::: {#exr-rationals-inside-c2}
[C2: A cube root of two]

Let \( \tau \coloneqq \{ p \in \nQ : p \le 0 \text{ or } p^3 < 2 \} \). We show that \( \tau \) is a cut with \( \tau > D_0 \) and that \( \tau\tau\tau = D_2 \). Everything below is proved in full except the last case, which is left to you.

*Monotone cubing.* For rationals \( 0 \le a < b \), \( b^3 - a^3 = (b - a)(b^2 + ab + a^2) > 0 \), since \( b - a > 0 \), \( b^2 > 0 \) (@prp-ordered-ring-rules (e)), \( ab \ge 0 \), \( a^2 \ge 0 \), and a product of positives is positive (@prp-ordered-ring-rules (c)). Only non-negative \( a, b \) are needed, because of the clause "\( p \le 0 \) or".

*\( \tau \) is a cut and \( \tau > D_0 \).* (C1) \( 0 \in \tau \), and \( 2 \notin \tau \) since \( 2^3 = 8 \ge 2 \). (C2) Let \( q < p \in \tau \). If \( q \le 0 \), then \( q \in \tau \). If \( 0 < q < p \), then \( p > 0 \), so \( p^3 < 2 \), and monotone cubing gives \( q^3 < p^3 < 2 \). (C3) If \( p \le 0 \), then \( 1 \in \tau \) is larger. If \( p > 0 \) and \( p^3 < 2 \), put \( d \coloneqq 2 - p^3 \), so \( 0 < d \le 2 \), and
\[
h \coloneqq \frac{d}{3p^2 + 3p + 2} .
\]
Then \( 0 < h < 1 \), because \( d \le 2 < 3p^2 + 3p + 2 \). So \( h^2 < h \) and \( h^3 < h \), and since \( p > 0 \),
\[
\begin{aligned}
(p + h)^3 &= p^3 + 3p^2 h + 3p h^2 + h^3 \\
&< p^3 + h (3p^2 + 3p + 1) \\
&< p^3 + h (3p^2 + 3p + 2) = p^3 + d = 2 ,
\end{aligned}
\]
so \( p + h \in \tau \) and \( p + h > p \). Finally \( D_0 \subseteq \tau \) and \( 1 \in \tau \setminus D_0 \), so \( \tau > D_0 \).

*The \( \subseteq \) half of \( \tau\tau\tau = D_2 \).* Since \( \tau > D_0 \), the proof of @prp-cut-product-positive (c), with \( \alpha = \beta = \gamma = \tau \), shows that \( (\tau\tau)\tau = \tau(\tau\tau) \) (so we write \( \tau\tau\tau \)) is the set of \( x \in \nQ \) with \( x \le rst \) for some positive \( r, s, t \in \tau \). For such \( r, s, t \), let \( m \) be the largest. Then \( rst \le m^3 < 2 \), by @prp-ordered-ring-rules (c) and monotone cubing. So \( \tau\tau\tau \subseteq D_2 \).

*The \( \supseteq \) half, easy cases.* Let \( x < 1 \). Then \( 1 \in \tau \) (\( 1^3 < 2 \)) and \( x \le 1 \cdot 1 \cdot 1 \), so \( x \in \tau\tau\tau \). This covers \( x \le 0 \) and \( 0 < x < 1 \) together.

*The \( \supseteq \) half, the case \( 1 \le x < 2 \).* Let \( 1 \le x < 2 \). Find \( r \in \tau \), \( r > 0 \), with \( r^3 > x \), and then write \( x \) as a product of three positive elements of \( \tau \).

*Name the move, then complete it.*
:::

::: {.solution}
*The move* is **walk up by \( \varepsilon \)** in its multiplicative form, @lem-cut-multiplicative-step: step up by a fixed factor \( \mu > 1 \) until you leave \( \tau \), and choose \( \mu \) so small that the last step inside is already beyond what we need.

*The factor.* We need \( \mu > 1 \) with \( \mu^3 < 2/x \). Put \( t \coloneqq 2/x - 1 \), so \( 0 < t \le 1 \), and \( \mu \coloneqq 1 + t/7 \). Since \( 0 < t \le 1 \), \( t^2 \le t \) and \( t^3 \le t \), so
\[
\begin{aligned}
\mu^3 &= 1 + \frac{3t}{7} + \frac{3t^2}{49} + \frac{t^3}{343} \\
&\le 1 + t \Bigl( \frac{147 + 21 + 1}{343} \Bigr) = 1 + \frac{169}{343} t < 1 + t = \frac{2}{x} .
\end{aligned}
\]

*The step.* Since \( \tau > D_0 \) and \( \mu > 1 \), @lem-cut-multiplicative-step gives \( r \in \tau \) with \( r > 0 \) and \( \mu r \notin \tau \). As \( \mu r > 0 \), this means \( (\mu r)^3 \ge 2 \), so \( r^3 \ge 2/\mu^3 > x \).

*The product.* Put \( u \coloneqq x/r^2 \). Then \( u > 0 \), and \( u < r \) because \( x < r^3 \); so \( u \in \tau \) by (C2). Now \( x = r \cdot r \cdot u \) with \( r, r, u \) positive elements of \( \tau \), so \( x \in \tau\tau\tau \).

Hence \( \tau\tau\tau = D_2 \): the cut \( \tau \) is a cube root of \( D_2 \) in \( \nR_{\mathrm D} \). The factor \( 1/7 \) is one convenient choice; any \( \mu = 1 + ct \) with \( 3c + 3c^2 + c^3 < 1 \) works by the same estimate, and \( c = 1/3 \), which served for \( \sigma \), does not: for \( x = 1 \) it gives \( \mu = 4/3 \) and \( \mu^3 = 64/27 > 2 \).
:::

<!-- dependency ledger
sec-rationals-inside (claim): Q is an ordered field; arithmetic and order of rationals throughout (midpoints, halving, multiplying inequalities by positives) | ℚ ordered field, F3.2 (thm-rationals-ordered-field, prp-ordered-ring-rules), cited where a step turns on it
thm-rationals-embed-cuts (proof): uniqueness of negatives, -(-a) = a, and the sign rules (-a)b = -(ab), (-a)(-b) = ab, used in the field R_D | prp-ring-algebra (a), (c) with thm-cuts-ordered-field, cited
thm-rationals-embed-cuts (proof): x/(pq) < lambda < 1 for the midpoint lambda of x/(pq) and 1 | inline; verify/ch07/thm-rationals-embed-cuts.py
thm-rationals-embed-cuts (example): D_2^{-1} = D_{1/2} from D_2 D_{1/2} = D_1 | lem-field-fraction-rules (a) with thm-cuts-ordered-field, cited
thm-cut-rationals-dense (claim): {r : r <= 1} and D_1 have no D_q strictly between them | inline (every q with D_1 < D_q has q > 1); illustration only
thm-cut-rationals-dense (solution): 29/20 squared is 841/400 > 2; 10/7 in D_{29/20} but not in sigma; 10/7 also works, with witness 17/12 | verify/ch07/thm-cut-rationals-dense.py
prp-cuts-archimedean (proof): n · 1 in R_D equals D_n | thm-rationals-embed-ordered-field (iota_F(n) = n · 1_F) with thm-rationals-embed-cuts, cited in the lead-in
prp-cut-sqrt2-square (proof): mu^2 < 2/x for t = 2/x - 1 in (0, 1], mu = 1 + t/3; the example x = 3/2 | inline; verify/ch07/prp-cut-sqrt2-square.py
prp-cut-sqrt2-square (proof): r^2 >= 2/mu^2 from (mu r)^2 >= 2 | ℚ ordered field, F3.2 (prp-ordered-ring-rules (c), dividing by mu^2 > 0)
thm-cuts-complete-field (claim): Section 5.5 proves Cauchy completeness and Section 5.6 reaches suprema by bisection | thm-constructed-reals-cauchy-complete, thm-cauchy-archimedean-lub; comparison only
thm-cuts-complete-field (claim): R_D is a copy of Chapter 5's R by exactly one isomorphism | thm-cof-uniqueness with thm-reals-complete-ordered-field; prose, proved in Section 7.6 (thm-dedekind-same-reals)
exr-rationals-inside-b2 (solution): rho is a cut | Exercise B2 of Section 7.1 (an earlier exercise, granted in the problem)
exr-rationals-inside-b2 (solution): mu^2 < 3/x for t in (0, 2] | verify/ch07/exr-rationals-inside-b2.py
exr-rationals-inside-c1 (solution): order rules (translation, multiplying by a positive) in the ordered field R_D | thm-cuts-ordered-field with prp-ordered-ring-rules, cited
exr-rationals-inside-c1 (solution): (3/2)^2 = 9/4 > 2; the affine solve for sigma | verify/ch07/exr-rationals-inside-c1.py
exr-rationals-inside-c2 (solution): the (C3) estimate for tau and mu^3 < 2/x with mu = 1 + t/7, coefficient 169/343 | verify/ch07/exr-rationals-inside-c2.py
exr-rationals-inside-c2 (claim): tau tau tau = {x : x <= rst, r, s, t in tau positive} | prp-cut-product-positive (c), the set T in its proof, cited
exr-rationals-inside-c2 (solution): rst <= m^3 for positive r, s, t with largest m | prp-ordered-ring-rules (c), cited in the problem
-->
