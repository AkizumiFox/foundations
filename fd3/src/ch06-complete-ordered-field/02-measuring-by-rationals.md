# Building the Map from the Rationals Below

Section 6.1 gave every element \( x \) of an ordered field \( F \) a record, the set \( \nQ_F(x) \) of rationals below it, and showed that in an Archimedean field the record determines the element (@lem-cof-rationals-separate). This section turns the record into a map. Given an Archimedean field \( F \) and a complete field \( L \), we send \( x \in F \) to the element of \( L \) with the same record. The result is the main theorem of the chapter in its one-sided form: there is exactly one order-preserving field map \( F \to L \). Section 6.3 applies it twice, in both directions, to compare two complete ordered fields.

Two fields are in play throughout, so every proof here keeps \( \iota_F \) and \( \iota_L \) visible. Only the two lemmas, each about one field, write \( q \) for \( \iota_F(q) \).

## What the map must be

Suppose \( \varphi \colon F \to L \) is an order-preserving field map (@def-cof-order-preserving-map). By @prp-cof-map-fixes-rationals it fixes the rationals, \( \varphi(\iota_F(q)) = \iota_L(q) \), and it preserves and reflects order. So for \( q \in \nQ \) and \( x \in F \),
\[
\iota_F(q) < x \iff \varphi\bigl(\iota_F(q)\bigr) < \varphi(x) \iff \iota_L(q) < \varphi(x) .
\]
In the notation of Section 6.1: \( \nQ_L(\varphi(x)) = \nQ_F(x) \). *The image of \( x \) has exactly the rationals below it that \( x \) has.*

That already shows there can be at most one such map when \( L \) is Archimedean: two candidates for \( \varphi(x) \) would have the same rationals below them, and rationals separate. For existence, we need an element of \( L \) with a prescribed set of rationals below it. When \( L \) is complete there is a natural candidate: the least element of \( L \) that lies above all the copies \( \iota_L(q) \), \( q \in \nQ_F(x) \), that is, their supremum.

The check that this candidate respects sums and products goes through the record, not through suprema. For that we need to know how the rationals below \( a + b \) and below \( ab \) are made from those below \( a \) and \( b \).

::: {.check}
Let \( \varphi \colon \nQ \to L \) be an order-preserving field map into an ordered field \( L \). Which rationals lie below \( \varphi(1/2) \)?
:::

::: {.solution}
Those \( q < 1/2 \): \( \varphi(1/2) = \iota_L(1/2) \) (@prp-cof-map-fixes-rationals with \( \iota_{\nQ} = \id_{\nQ} \)), and \( \iota_L \) preserves and reflects order.
:::

## Sums and products, measured by rationals

A rational \( q \) lies below \( a + b \) exactly when it splits into a rational below \( a \) and a rational below \( b \).

::: {#lem-cof-below-sum}
[Rationals below a Sum]

Let \( F \) be an Archimedean ordered field, \( a, b \in F \) and \( q \in \nQ \). Then \( \iota_F(q) < a + b \) if and only if there is \( r \in \nQ \) with
\[
\iota_F(r) < a \qquad \text{and} \qquad \iota_F(q - r) < b .
\]
In other words, \( q \in \nQ_F(a + b) \iff \exists r \in \nQ \ \bigl( r \in \nQ_F(a) \wedge q - r \in \nQ_F(b) \bigr) \).
:::

::: {.idea}
One direction is addition of inequalities. For the other, split \( q \) as \( r + (q - r) \) with \( r \) a rational just below \( a \): we need \( r \) in the gap between \( q - b \) and \( a \), which is non-empty exactly because \( q < a + b \), and density supplies it.
:::

::: {.proof}
We write \( q \) for \( \iota_F(q) \); since \( \iota_F \) preserves sums, it preserves differences, so \( \iota_F(q - r) = q - r \) in \( F \).

\( (\Leftarrow) \) If \( r < a \) and \( q - r < b \), then \( q = r + (q - r) < a + b \) by @prp-ordered-ring-rules (b).

\( (\Rightarrow) \) Let \( q < a + b \). Then \( q - b < a \) (@prp-ordered-ring-rules (a)). By @thm-rationals-dense-ordered-field there is \( r \in \nQ \) with \( q - b < r < a \). Then \( r < a \), and \( q - r < b \) by the same rule.
:::

For products the same idea works for positive elements and positive rationals, with \( q/r \) in place of \( q - r \).

::: {#lem-cof-below-product}
[Rationals below a Product]

Let \( F \) be an Archimedean ordered field, \( a, b \in F \) with \( a > 0 \) and \( b > 0 \), and \( q \in \nQ \) with \( q > 0 \). Then \( \iota_F(q) < ab \) if and only if there is \( r \in \nQ \) with
\[
r > 0 , \qquad \iota_F(r) < a \qquad \text{and} \qquad \iota_F(q/r) < b .
\]
For \( q \le 0 \), \( \iota_F(q) < ab \) holds always.
:::

*In words: below a product of positives, a positive rational splits as a product of a rational below each factor.* Exercise B1 asks for the proof; the fold below has it.

::: {.second-reading title="The proof of the product lemma (try Exercise B1 first)"}
::: {.idea}
As for sums, with division in place of subtraction: split \( q \) as \( r \cdot (q/r) \) with \( r \) a rational in the gap between \( q/b \) and \( a \), a gap of positive elements.
:::

::: {.proof}
We write \( q \) for \( \iota_F(q) \); since \( \iota_F \) preserves products and \( \iota_F(r) \ne 0 \) for \( r \ne 0 \), it preserves quotients, so \( \iota_F(q/r) = q/r \) in \( F \).

If \( q \le 0 \), then \( q \le 0 < ab \) by (O4). Let \( q > 0 \).

\( (\Leftarrow) \) Let \( r > 0 \) with \( r < a \) and \( q/r < b \). Since \( q/r > 0 \) (@prp-reciprocal-order (a), (O4)), @prp-ordered-ring-rules (c) gives \( q = r \cdot (q/r) < a \cdot (q/r) \); since \( a > 0 \), it gives \( a \cdot (q/r) < ab \). So \( q < ab \).

\( (\Rightarrow) \) Let \( q < ab \). Multiplying by \( b^{-1} > 0 \) (by the same two rules) gives \( q/b < a \), and \( q/b > 0 \) by (O4). By @thm-rationals-dense-ordered-field there is \( r \in \nQ \) with \( q/b < r < a \). Then \( r > q/b > 0 \), so \( r > 0 \) in \( \nQ \), since \( \iota_F \) reflects order. Multiplying \( q/b < r \) by \( b > 0 \) gives \( q < rb \), and multiplying by \( r^{-1} > 0 \) gives \( q/r < b \).
:::
:::

::: {.check}
In \( F = \nQ \), with \( a \coloneqq 3/4 \), \( b \coloneqq 1/2 \) and \( q \coloneqq 1 \), find a rational \( r \) as in @lem-cof-below-sum. Which rationals \( r \) work?
:::

::: {.solution}
We need \( r < 3/4 \) and \( 1 - r < 1/2 \), that is, \( 1/2 < r < 3/4 \). For example \( r = 2/3 \): then \( 1 - 2/3 = 1/3 < 1/2 \). Exactly the rationals of the open gap between \( q - b = 1/2 \) and \( a = 3/4 \) work, as the proof predicts.
:::

## The map into a complete field

Here is the theorem. Its proof is the first key proof of the chapter.

::: {#thm-cof-embedding-into-complete}
[Embedding an Archimedean Field in a Complete One]

Let \( F \) be an Archimedean ordered field and \( L \) a complete ordered field. Then there is **exactly one** order-preserving field map \( \varphi \colon F \to L \). It is given by
\[
\varphi(x) \coloneqq \sup\nolimits_L \, \{ \iota_L(q) : q \in \nQ_F(x) \} \qquad (x \in F) ,
\]
the supremum taken in \( L \), and it satisfies
\[
\nQ_L\bigl(\varphi(x)\bigr) = \nQ_F(x) \qquad \text{for every } x \in F . \tag{$\star$}
\]
:::

*Try it first (ten minutes): if \( \varphi \) exists and fixes \( \nQ \), which element of \( L \) must \( \varphi(x) \) be?*

::: {.idea}
The natural first attempt defines \( \varphi \) on the copy of \( \nQ \), by \( \varphi(\iota_F(q)) \coloneqq \iota_L(q) \), and then tries to "extend". It stalls at once: an element \( x \in F \) that is not a rational has no formula, and nothing in \( F \) names it. What we do know, from the previous subsection, is its record: \( \varphi(x) \) must have exactly the rationals \( \nQ_F(x) \) below it. So we **construct a point as a supremum** (@exm-method-point-as-supremum): \( \varphi(x) \) is the least upper bound in \( L \) of the copies of those rationals, and \( (\star) \) says the construction has the right record. After that, sums, products and uniqueness are checked the same way: compute the record of both sides (for sums and products by the two lemmas) and let rationals separate in \( L \). Monotonicity needs only one rational between \( x \) and \( y \).

① \( \varphi(x) \) exists; ② \( (\star) \); ③ \( \varphi \) fixes the rationals; ④ \( \varphi \) is strictly increasing; ⑤ sums; ⑥ products and the unit; ⑦ uniqueness. *Before reading on: where is completeness of \( L \) used, and where the Archimedean property of \( F \)?*
:::

::: {.proof}
By @thm-cof-complete-archimedean, \( L \) is Archimedean. The rules of an ordered field are used without comment. So @thm-rationals-dense-ordered-field, @lem-cof-rationals-separate, @lem-cof-below-sum and @lem-cof-below-product apply in \( L \) as well as in \( F \). For \( x \in F \) write \( A_x \coloneqq \{ \iota_L(q) : q \in \nQ_F(x) \} \subseteq L \).

**Step 1: \( \varphi(x) \) is defined.** Let \( x \in F \). Since \( F \) is Archimedean, there is \( n \in \nN \) with \( -x < n \cdot 1_F \), so \( \iota_F(-n) = -(n \cdot 1_F) < x \), and \( -n \in \nQ_F(x) \): the set \( A_x \) is non-empty. Applied to \( x \), the Archimedean property gives \( m \in \nN \) with \( x < m \cdot 1_F = \iota_F(m) \). For \( q \in \nQ_F(x) \), \( \iota_F(q) < x < \iota_F(m) \), so \( q < m \) because \( \iota_F \) reflects order, and \( \iota_L(q) < \iota_L(m) \). So \( \iota_L(m) \) is an upper bound of \( A_x \). Since \( L \) is complete, \( A_x \) has a supremum in \( L \), and it is unique; \( \varphi(x) \) is that supremum. So \( \varphi \colon F \to L \) is a function.

**Step 2: \( (\star) \).** Let \( x \in F \) and \( q \in \nQ \).

\( (\subseteq) \) Let \( q \in \nQ_F(x) \). By density in \( F \) there is \( r \in \nQ \) with \( \iota_F(q) < \iota_F(r) < x \). Then \( r \in \nQ_F(x) \), so \( \iota_L(r) \in A_x \) and \( \iota_L(r) \le \varphi(x) \), since \( \varphi(x) \) is an upper bound. Also \( q < r \) (reflection in \( F \)), so \( \iota_L(q) < \iota_L(r) \le \varphi(x) \), and \( q \in \nQ_L(\varphi(x)) \).

\( (\supseteq) \) Let \( \iota_L(q) < \varphi(x) \). Since \( \varphi(x) \) is the **least** upper bound of \( A_x \), \( \iota_L(q) \) is not an upper bound, so there is \( r \in \nQ_F(x) \) with \( \iota_L(q) < \iota_L(r) \) (totality). Then \( q < r \) (reflection in \( L \)), so \( \iota_F(q) < \iota_F(r) < x \), and \( q \in \nQ_F(x) \).

**Step 3: \( \varphi \) fixes the rationals.** Let \( r \in \nQ \). By \( (\star) \) and the first example after @def-cof-rationals-below, used in \( F \) and in \( L \),
\[
\nQ_L\bigl(\varphi(\iota_F(r))\bigr) = \nQ_F\bigl(\iota_F(r)\bigr) = \{ q \in \nQ : q < r \} = \nQ_L\bigl(\iota_L(r)\bigr) .
\]
By @lem-cof-rationals-separate in \( L \), \( \varphi(\iota_F(r)) = \iota_L(r) \). In particular \( \varphi(0_F) = 0_L \) and \( \varphi(1_F) = 1_L \).

**Step 4: \( \varphi \) is strictly increasing.** Let \( x < y \) in \( F \). By density in \( F \) there is \( r \in \nQ \) with \( x < \iota_F(r) < y \). Then \( r \notin \nQ_F(x) \) (by (O1)), so \( r \notin \nQ_L(\varphi(x)) \) by \( (\star) \), and \( \varphi(x) \le \iota_L(r) \) by totality. And \( r \in \nQ_F(y) = \nQ_L(\varphi(y)) \), so \( \iota_L(r) < \varphi(y) \). Hence \( \varphi(x) \le \iota_L(r) < \varphi(y) \).

**Step 5: sums.** Let \( x, y \in F \) and \( q \in \nQ \). Then
\[
\begin{aligned}
q \in \nQ_L\bigl(\varphi(x + y)\bigr)
&\iff q \in \nQ_F(x + y) \\
&\iff \exists r \in \nQ \ \bigl( r \in \nQ_F(x) \wedge q - r \in \nQ_F(y) \bigr) \\
&\iff \exists r \in \nQ \ \bigl( r \in \nQ_L(\varphi(x)) \wedge q - r \in \nQ_L(\varphi(y)) \bigr) \\
&\iff q \in \nQ_L\bigl(\varphi(x) + \varphi(y)\bigr) ,
\end{aligned}
\]
by \( (\star) \), @lem-cof-below-sum in \( F \), \( (\star) \) twice, and @lem-cof-below-sum in \( L \). By @lem-cof-rationals-separate in \( L \), \( \varphi(x + y) = \varphi(x) + \varphi(y) \).

**Step 6: products and the unit.** First let \( x > 0 \) and \( y > 0 \). By Steps 3 and 4, \( \varphi(x) > \varphi(0_F) = 0_L \) and \( \varphi(y) > 0_L \); and \( xy > 0 \), \( \varphi(x)\varphi(y) > 0 \) by (O4). Let \( q \in \nQ \). If \( q \le 0 \), then \( q \in \nQ_F(xy) = \nQ_L(\varphi(xy)) \), and \( q \in \nQ_L(\varphi(x)\varphi(y)) \), by the last clause of @lem-cof-below-product in \( F \) and in \( L \). If \( q > 0 \), then
\[
\begin{aligned}
q \in \nQ_L\bigl(\varphi(xy)\bigr)
&\iff q \in \nQ_F(xy) \\
&\iff \exists r \in \nQ_{>0} \ \bigl( r \in \nQ_F(x) \wedge q/r \in \nQ_F(y) \bigr) \\
&\iff \exists r \in \nQ_{>0} \ \bigl( r \in \nQ_L(\varphi(x)) \wedge q/r \in \nQ_L(\varphi(y)) \bigr) \\
&\iff q \in \nQ_L\bigl(\varphi(x)\varphi(y)\bigr) ,
\end{aligned}
\]
by \( (\star) \), @lem-cof-below-product in \( F \), \( (\star) \) twice, and @lem-cof-below-product in \( L \) (with \( \varphi(x), \varphi(y) > 0 \)). By @lem-cof-rationals-separate in \( L \), \( \varphi(xy) = \varphi(x)\varphi(y) \) for \( x, y > 0 \).

Now the signs. By Steps 5 and 3, \( \varphi(x) + \varphi(-x) = \varphi(0_F) = 0_L \), so \( \varphi(-x) = -\varphi(x) \). If \( x = 0 \) or \( y = 0 \), both sides of \( \varphi(xy) = \varphi(x)\varphi(y) \) are \( 0_L \) (Step 3). If \( x < 0 < y \), then \( -x > 0 \) and \( xy = -\bigl((-x)y\bigr) \), so
\[
\varphi(xy) = -\varphi\bigl((-x)y\bigr) = -\bigl(\varphi(-x)\varphi(y)\bigr) = -\bigl(-\varphi(x)\bigr)\varphi(y) = \varphi(x)\varphi(y) .
\]
The case \( x > 0 > y \) follows by commutativity, and if \( x, y < 0 \), then \( xy = (-x)(-y) \) and \( \varphi(xy) = \bigl(-\varphi(x)\bigr)\bigl(-\varphi(y)\bigr) = \varphi(x)\varphi(y) \). Finally \( \varphi(1_F) = 1_L \) by Step 3. With Steps 4 and 5, \( \varphi \) is an order-preserving field map.

**Step 7: uniqueness.** Let \( \chi \colon F \to L \) be any order-preserving field map, and let \( x \in F \), \( q \in \nQ \). By @prp-cof-map-fixes-rationals, \( \chi(\iota_F(q)) = \iota_L(q) \). If \( \iota_F(q) < x \), then \( \iota_L(q) = \chi(\iota_F(q)) < \chi(x) \). If \( \iota_L(q) < \chi(x) \), that is, \( \chi(\iota_F(q)) < \chi(x) \), then \( \iota_F(q) < x \), because \( \chi \) reflects order (the remark after @def-cof-order-preserving-map). So
\[
\nQ_L\bigl(\chi(x)\bigr) = \nQ_F(x) = \nQ_L\bigl(\varphi(x)\bigr) ,
\]
the second equality by \( (\star) \). By @lem-cof-rationals-separate in \( L \), \( \chi(x) = \varphi(x) \). Since \( x \) was arbitrary, \( \chi = \varphi \). This proves the theorem.
:::

The answer to the prompt. Completeness of \( L \) is used in Step 1, where the supremum must exist, and in Step 2 \( (\supseteq) \), where its leastness turns "below \( \varphi(x) \)" into "below some \( \iota_L(r) \)". The Archimedean property of \( F \) is used in Step 1 for the bounds \( -n \) and \( m \), in Steps 2 and 4 through density in \( F \), and in Steps 5 and 6 through the two lemmas applied in \( F \). Completeness of \( L \) is used a third time, indirectly: it makes \( L \) Archimedean (@thm-cof-complete-archimedean), which Steps 3, 5, 6 and 7 need for rationals to separate in \( L \) and for the lemmas in \( L \).

::: {.remark}
Step 7 is the whole of "uniqueness". Its idea, comparing the rationals below two candidate values, needs only that \( L \) is Archimedean, not that it is complete: Exercise C1 runs it for any two order-preserving field maps \( F \to L \), with no appeal to \( (\star) \). Section 6.3 leans on the uniqueness clause throughout: to show that the maps between two complete fields are inverse to each other, that the isomorphism they give is the only one, and that a complete ordered field has no order-preserving field automorphism other than the identity.
:::

::: {.remark}
Neither hypothesis can be dropped from the existence half. *Without completeness of \( L \):* take \( F = \nR \), which is Archimedean (@thm-constructed-reals-archimedean), and \( L = \nQ \). An order-preserving field map \( \varphi \colon \nR \to \nQ \) would fix \( 2 \) (@prp-cof-map-fixes-rationals), so for \( \sqrt 2 \in \nR \) (Section 6.1), \( \varphi(\sqrt 2)^2 = \varphi((\sqrt 2)^2) = \varphi(2) = 2 \) in \( \nQ \), against @thm-no-rational-square-two. *Without the Archimedean property of \( F \):* take \( F = \nQ(t) \) of @exm-rational-function-field and any complete \( L \). An order-preserving field map \( \varphi \) would fix each \( n \cdot 1 \) and be strictly increasing, so \( n \cdot 1_L = \varphi(n \cdot 1) < \varphi(t) \) for every \( n \in \nN \), against the Archimedean property of \( L \) (@thm-cof-complete-archimedean).
:::

::: {.warning}
The supremum in the definition of \( \varphi \) is taken **in \( L \)**, of the copies \( \iota_L(q) \). In \( \nQ \) it may not exist: \( \nQ_{\nR}(\sqrt 2) \) has the same upper bounds in \( \nQ \) as \( \{ p \in \nQ : p^2 < 2 \} \), which has no least one (@thm-rationals-gap-sqrt2). In \( F \) it always exists and is \( x \) itself (Exercise B2 of Section 6.1): an element of the wrong field.
:::

::: {.check}
Take \( L \coloneqq F \), a complete ordered field. Which map \( F \to F \) does @thm-cof-embedding-into-complete produce, and why, without computing a single supremum?
:::

::: {.solution}
The identity. The theorem says there is exactly one order-preserving field map \( F \to F \) (\( F \) is Archimedean by @thm-cof-complete-archimedean), and \( \id_F \) is one (the first example after @def-cof-order-preserving-map). So \( \varphi = \id_F \). This is the argument Section 6.3 builds on.
:::

## Exercises

### A. Check your understanding

::: {#exr-measuring-by-rationals-a1}
[A1]

These questions are about the proof of @thm-cof-embedding-into-complete.

::: {.enumerate options="label=(\alph*)"}
1. Which steps use that \( L \) is complete, and which that \( F \) is Archimedean? Which steps use that \( L \) is Archimedean, and where does that come from?
2. Run the definition of \( \varphi \) with \( F = \nQ \) and \( L = \nR \), the constructed reals. What is \( \varphi \)?
3. State the idea of the proof in two sentences.
4. Why may Step 1 not define \( \varphi(x) \) as a supremum taken in \( F \)?
:::
:::

::: {.solution}
(a) \( L \) complete: Step 1 (the supremum exists) and Step 2 \( (\supseteq) \) (its leastness). \( F \) Archimedean: Step 1 (the bounds \( -n \), \( m \)), Steps 2 and 4 (density in \( F \)), and Steps 5 and 6 (@lem-cof-below-sum and @lem-cof-below-product applied in \( F \)). \( L \) Archimedean: Steps 3, 5, 6 and 7, through @lem-cof-rationals-separate in \( L \) and the two lemmas in \( L \). It comes from the completeness of \( L \), by @thm-cof-complete-archimedean.

(b) \( \varphi = \iota_{\nR} = \kappa \). By Step 3, \( \varphi(\iota_{\nQ}(r)) = \iota_{\nR}(r) \) for every \( r \in \nQ \), and \( \iota_{\nQ} \) is the identity (Chapter 4, after @thm-rationals-embed-ordered-field). So \( \varphi(r) = \iota_{\nR}(r) \), which is \( \kappa(r) \) by @thm-rational-embedding (d). Concretely, \( \varphi(r) \) is the supremum in \( \nR \) of \( \{ \kappa(q) : q < r \} \), and that supremum is \( \kappa(r) \).

(c) An order-preserving map that fixes the rationals must send \( x \) to an element with the same rationals below it, and in a complete \( L \) the supremum of their copies is such an element. Every field identity for \( \varphi \) is then checked by comparing the rationals below the two sides, which the sum and product lemmas compute, and rationals separate in \( L \).

(d) In \( F \) the supremum of \( \iota_F(\nQ_F(x)) \) always exists, since \( F \) is Archimedean, and it is \( x \) itself (Exercise B2 of Section 6.1): an element of \( F \), not of \( L \). So it does not give a map into \( L \). The supremum must be of the copies \( \iota_L(q) \), taken in \( L \).
:::

### B. Practice

::: {#exr-measuring-by-rationals-b1}
[B1]

Prove @lem-cof-below-product: let \( F \) be an Archimedean ordered field, \( a, b \in F \) with \( a, b > 0 \), and \( q \in \nQ \) with \( q > 0 \); show that \( \iota_F(q) < ab \) if and only if some rational \( r > 0 \) has \( \iota_F(r) < a \) and \( \iota_F(q/r) < b \). Show also that \( \iota_F(q) < ab \) for every rational \( q \le 0 \).

*Hint: imitate the proof of @lem-cof-below-sum, with division in place of subtraction.*
:::

::: {.solution}
Write \( q \) for \( \iota_F(q) \). Since \( \iota_F \) preserves products, \( \iota_F(r)\,\iota_F(r^{-1}) = \iota_F(1) = 1 \) for \( r \ne 0 \), so \( \iota_F(r^{-1}) = \iota_F(r)^{-1} \) (@lem-field-fraction-rules (a)) and \( \iota_F(q/r) = q/r \) in \( F \).

If \( q \le 0 \), then \( q \le 0 < ab \) by (O4).

Let \( q > 0 \). \( (\Leftarrow) \) Let \( r > 0 \), \( r < a \), \( q/r < b \). Then \( q/r > 0 \) (@prp-reciprocal-order (a), (O4)), so @prp-ordered-ring-rules (c) gives \( q = r(q/r) < a(q/r) \), and, as \( a > 0 \), \( a(q/r) < ab \). Hence \( q < ab \).

\( (\Rightarrow) \) Let \( q < ab \). Since \( b^{-1} > 0 \), @prp-ordered-ring-rules (c) gives \( q/b < a \), and \( q/b > 0 \). By @thm-rationals-dense-ordered-field there is \( r \in \nQ \) with \( q/b < \iota_F(r) < a \). Then \( \iota_F(r) > 0 = \iota_F(0) \), so \( r > 0 \) since \( \iota_F \) reflects order. From \( q/b < r \) and \( b > 0 \), \( q < rb \); multiplying by \( r^{-1} > 0 \), \( q/r < b \). This \( r \) is as required.
:::

::: {#exr-measuring-by-rationals-b2}
[B2: Cube roots]

Let \( F \) be a complete ordered field and \( a \in F \) with \( a > 0 \). Let \( S \coloneqq \{ y \in F : y \ge 0 \text{ and } y^3 < a \} \). The following steps prove that some \( s \in F \) has \( s^3 = a \).

::: {.enumerate options="label=(\arabic*)"}
1. \( S \) is non-empty (\( 0 \in S \)) and bounded above by \( 1 + a \): if \( y > 1 + a \), then \( y > 1 \), so \( y^3 > y > a \). Let \( s \coloneqq \sup S \). Then \( s > 0 \), since \( m \coloneqq \min\{1, a/2\} \) has \( 0 < m \le 1 \), so \( m^3 \le m \le a/2 < a \), and \( m \in S \).
2. For \( y, z \in F \), \( z^3 - y^3 = (z - y)(z^2 + zy + y^2) \) and \( z^2 + zy + y^2 = (z + y/2)^2 + (3/4)y^2 \), which is \( > 0 \) unless \( y = z = 0 \) (if \( y \ne 0 \), then \( (3/4)y^2 > 0 \) by @prp-ordered-ring-rules (e), (c) and the square is \( \ge 0 \), so the sum is positive by (b); if \( y = 0 \) and \( z \ne 0 \), the expression is \( z^2 > 0 \) by (e)). Hence \( y < z \iff y^3 < z^3 \), for all \( y, z \in F \).
3. The case \( s^3 < a \) is impossible. Let \( h \coloneqq \min\{1, (a - s^3)/(2(3s^2 + 3s + 1))\} > 0 \). Since \( 0 < h \le 1 \) and \( s \ge 0 \), \( (s + h)^3 = s^3 + 3s^2h + 3sh^2 + h^3 \le s^3 + h(3s^2 + 3s + 1) \le s^3 + (a - s^3)/2 < a \), so \( s + h \in S \), against \( s \) being an upper bound.
4. The case \( s^3 > a \) is impossible. *Name the move, then complete it.*
5. Hence \( s^3 = a \).
:::

Then explain how to get a cube root of \( a = 0 \) and of \( a < 0 \), and why every \( a \in F \) has **exactly one** cube root.
:::

::: {.solution}
The move is **construct a point as a supremum**: \( s \) is built as \( \sup S \), and each of the two wrong cases of trichotomy is refuted by exhibiting a point that contradicts one clause of the supremum. In step (3) it was an element of \( S \) above \( s \), against (S1). In step (4) it is an upper bound below \( s \), against (S2).

(4) Suppose \( s^3 > a \). Let \( h \coloneqq (s^3 - a)/(3s^2) \); it is positive, since \( s > 0 \) by (1). Also \( h < s \): this says \( s^3 - a < 3s^3 \), which holds because \( a > 0 \) and \( 2s^3 > 0 \). So \( s - h > 0 \), and
\[
(s - h)^3 - a = (s^3 - a) - 3s^2h + 3sh^2 - h^3 = h^2(3s - h) > 0 ,
\]
since \( 3s^2 h = s^3 - a \), \( h^2 > 0 \) and \( 3s - h > 2s > 0 \). Let \( y > s - h \). By (2), \( y^3 > (s - h)^3 > a \), so \( y \notin S \). Hence every element of \( S \) is \( \le s - h \), and \( s - h \) is an upper bound of \( S \) smaller than \( s \), against \( s \) being the least upper bound.

(5) Steps (3) and (4) leave only \( s^3 = a \), by trichotomy (O1).

For \( a = 0 \), \( 0^3 = 0 \). For \( a < 0 \), \( -a > 0 \) has a cube root \( c \) by the above, and \( (-c)^3 = -c^3 = a \) (@prp-ring-algebra (c)). Uniqueness: if \( b^3 = c^3 \), then neither \( b < c \) nor \( c < b \) can hold, since by (2) either would make the cubes differ; so \( b = c \). So every element of a complete ordered field has exactly one cube root.
:::

### C. Going deeper

::: {#exr-measuring-by-rationals-c1}
[C1: Exit check: at most one map into an Archimedean field]

Let \( F \) and \( L \) be Archimedean ordered fields, and let \( \chi_1, \chi_2 \colon F \to L \) be order-preserving field maps. Prove that \( \chi_1 = \chi_2 \).
:::

::: {.solution}
[Hint 1]

Compare the rationals below \( \chi_1(x) \) and below \( \chi_2(x) \).
:::

::: {.solution}
[Hint 2]

By @prp-cof-map-fixes-rationals, \( \chi_i(\iota_F(q)) = \iota_L(q) \) for \( i = 1, 2 \) and every \( q \in \nQ \).
:::

::: {.solution}
Let \( x \in F \) and \( i \in \{1, 2\} \). By @prp-cof-map-fixes-rationals (which needs no order hypothesis), \( \chi_i(\iota_F(q)) = \iota_L(q) \) for every \( q \in \nQ \). Since \( \chi_i \) is strictly increasing and reflects order (the remark after @def-cof-order-preserving-map),
\[
\iota_F(q) < x \iff \chi_i\bigl(\iota_F(q)\bigr) < \chi_i(x) \iff \iota_L(q) < \chi_i(x) .
\]
So \( \nQ_L(\chi_1(x)) = \nQ_F(x) = \nQ_L(\chi_2(x)) \). Since \( L \) is Archimedean, @lem-cof-rationals-separate gives \( \chi_1(x) = \chi_2(x) \). As \( x \) was arbitrary, \( \chi_1 = \chi_2 \). (This is Step 7 of @thm-cof-embedding-into-complete with \( \chi_2 \) in place of \( \varphi \); completeness of \( L \) is not needed, and neither is the Archimedean property of \( F \).)

*Why \( L \) must be Archimedean (remark, not proved here).* The last step separates \( \chi_1(x) \) from \( \chi_2(x) \) by a rational strictly between them, which is density of \( \iota_L(\nQ) \) in \( L \), and density needs Archimedes (@thm-rationals-dense-ordered-field). In the non-Archimedean field \( \nQ(t) \) of @exm-rational-function-field, the elements \( 1/t \) and \( 2/t \) are different and have the same rationals below them, namely all \( q \le 0 \): a positive rational \( q \) has \( q > 1/n \) in \( \nQ \) for some \( n \in \nZ_{>0} \) (@thm-rationals-archimedean), so \( \iota_{\nQ(t)}(q) > \iota_{\nQ(t)}(1/n) = 1/(n \cdot 1) > 2/t \), because \( t > 2n \cdot 1 \) (@exm-rational-function-field). So the separating step fails in such a field.

**Marking scheme.** (10 points)
- 2: each \( \chi_i \) fixes \( \nQ \), with the reason (@prp-cof-map-fixes-rationals, or directly: induction for \( \nN \), then negatives and quotients).
- 3: links the rationals below \( x \) to those below \( \chi_i(x) \), using that \( \chi_i \) fixes \( \nQ \) and reflects order. Either gives the full equivalence \( \iota_F(q) < x \iff \iota_L(q) < \chi_i(x) \), or, for the squeeze route of the next item, applies reflection by \( \chi_1 \) and \( \chi_2 \) to a rational strictly between \( \chi_1(x) \) and \( \chi_2(x) \).
- 3: concludes \( \chi_1(x) = \chi_2(x) \) by rationals separating, or by a rational strictly between the two, invoking the Archimedean property **of \( L \)**.
- 2: states the conclusion for every \( x \in F \).
Fatal errors (0 for the step): using density in \( L \) without a hypothesis that gives it; assuming \( \chi_i \) surjective.
:::

::: {#exr-measuring-by-rationals-c2}
[C2: Dense image, and when the map is onto]

Let \( F \) be an Archimedean ordered field, \( L \) a complete ordered field, and \( \varphi \colon F \to L \) the map of @thm-cof-embedding-into-complete.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \varphi(F) \) is dense in \( L \): for all \( u < v \) in \( L \) there is \( x \in F \) with \( u < \varphi(x) < v \).
2. Prove that if \( F \) is complete, then \( \varphi \) is surjective.
3. Prove that if \( \varphi \) is surjective, then \( F \) is complete.
:::
:::

::: {.solution}
[Hint 1]

For (b), given \( y \in L \), look at the set \( S \coloneqq \nQ_L(y) \) and its copy \( \iota_F(S) \) in \( F \).
:::

::: {.solution}
[Hint 2]

For (b): \( \iota_F(S) \) is non-empty and bounded above in \( F \); let \( x \coloneqq \sup_F \iota_F(S) \), and show \( \nQ_F(x) = S \).
:::

::: {.solution}
By @thm-cof-complete-archimedean, \( L \) is Archimedean.

(a) Let \( u < v \) in \( L \). By @thm-rationals-dense-ordered-field in \( L \) there is \( q \in \nQ \) with \( u < \iota_L(q) < v \). By Step 3 of the proof of @thm-cof-embedding-into-complete, \( \iota_L(q) = \varphi(\iota_F(q)) \), so \( x \coloneqq \iota_F(q) \) works.

(b) Let \( F \) be complete and \( y \in L \). Let \( S \coloneqq \nQ_L(y) \). Since \( L \) is Archimedean, there are \( n, m \in \nN \) with \( -y < \iota_L(n) \) and \( y < \iota_L(m) \). So \( -n \in S \), and every \( q \in S \) has \( \iota_L(q) < y < \iota_L(m) \), hence \( q < m \) and \( \iota_F(q) < \iota_F(m) \). So \( \iota_F(S) \) is non-empty and bounded above in \( F \), and \( x \coloneqq \sup_F \iota_F(S) \) exists.

We show \( \nQ_F(x) = S \). \( (\supseteq) \) Let \( q \in S \). By density in \( L \) there is \( r \in \nQ \) with \( \iota_L(q) < \iota_L(r) < y \); then \( r \in S \) and \( q < r \), so \( \iota_F(q) < \iota_F(r) \le x \). \( (\subseteq) \) Let \( \iota_F(q) < x \). Then \( \iota_F(q) \) is not an upper bound of \( \iota_F(S) \), so \( \iota_F(q) < \iota_F(r) \) for some \( r \in S \); hence \( q < r \) and \( \iota_L(q) < \iota_L(r) < y \), so \( q \in S \).

By \( (\star) \), \( \nQ_L(\varphi(x)) = \nQ_F(x) = S = \nQ_L(y) \), so \( \varphi(x) = y \) by @lem-cof-rationals-separate in \( L \).

(c) Let \( \varphi \) be surjective. It is injective (strictly increasing), so bijective, with an inverse \( \varphi^{-1} \colon L \to F \) (@fd2:thm-bijection-iff-inverse). Let \( A \subseteq F \) be non-empty with an upper bound \( b \). Then \( \varphi(A) \) is non-empty and bounded above by \( \varphi(b) \), since \( a \le b \) gives \( \varphi(a) \le \varphi(b) \). As \( L \) is complete, \( s \coloneqq \sup \varphi(A) \) exists; let \( c \coloneqq \varphi^{-1}(s) \). *Upper bound:* for \( a \in A \), \( \varphi(a) \le s = \varphi(c) \), so \( a \le c \), because \( \varphi \) reflects order (and is injective, for the case of equality). *Least:* if \( u \) is an upper bound of \( A \), then \( \varphi(u) \) is an upper bound of \( \varphi(A) \), so \( \varphi(c) = s \le \varphi(u) \), and \( c \le u \) as before. So \( c = \sup A \) (@fd2:def-order-supremum), and \( F \) is complete.

So \( \varphi \) is an order-preserving field isomorphism exactly when \( F \) is complete. Section 6.3 reaches the "if" direction by a different route, which computes no supremum at all.

**Marking scheme.** (10 points)
- 2: (a) \( L \) is Archimedean (@thm-cof-complete-archimedean), so some \( \iota_L(q) \) lies strictly between \( u \) and \( v \), and \( \iota_L(q) = \varphi(\iota_F(q)) \) (Step 3).
- 2: (b) \( \iota_F(S) \) is non-empty and bounded above in \( F \) (Archimedes in \( L \), transferred through \( \iota_F \)), so \( x = \sup_F \iota_F(S) \) exists by completeness of \( F \).
- 2: (b) \( \nQ_F(x) = S \), both inclusions; \( (\supseteq) \) uses density in \( L \).
- 1: (b) \( \nQ_L(\varphi(x)) = \nQ_F(x) = \nQ_L(y) \) by \( (\star) \), hence \( \varphi(x) = y \) by @lem-cof-rationals-separate in \( L \).
- 3: (c) for non-empty \( A \subseteq F \) bounded above by \( b \), \( \varphi(A) \) is bounded above by \( \varphi(b) \), and \( \varphi^{-1}(\sup \varphi(A)) \) is an upper bound of \( A \) and the least one, both using that \( \varphi \) reflects order and is bijective.
Fatal errors (0 for the step): using density of \( \iota_L(\nQ) \) in \( L \) without the Archimedean property of \( L \); in (b), taking a supremum in \( F \) before checking that the set is non-empty and bounded above; in (c), assuming \( \varphi^{-1} \) preserves order without justification.
:::

<!-- dependency ledger
prp-cof-map-fixes-rationals (solution): quick check in Section 6.2, Q_L(phi(1/2)) = {q < 1/2} for phi: Q -> L | prp-cof-map-fixes-rationals, iota_Q = id_Q and iota_L preserves and reflects order (thm-rationals-embed-ordered-field and the paragraph after it); inline
lem-cof-below-sum (proof): iota_F preserves differences | thm-rationals-embed-ordered-field (sums), prp-ring-algebra (a) (uniqueness of negatives); inline
lem-cof-below-product (proof): iota_F preserves quotients | thm-rationals-embed-ordered-field (products), lem-field-fraction-rules (a); inline
lem-cof-below-sum (solution): quick check, 1/2 < r < 3/4, r = 2/3 | verify/ch06/lem-cof-below-sum.py
thm-cof-embedding-into-complete (proof): a set has at most one supremum | def-complete-ordered-field (well-definedness paragraph)
thm-cof-embedding-into-complete (proof): "not an upper bound" gives an element above; neg(a < b) iff b <= a | fd1:prp-bounded-quantifier-negation, totality (prp-ordered-field-halves (a)); inline
thm-cof-embedding-into-complete (proof): Q_F(iota_F(r)) = {q < r} | the first example after def-cof-rationals-below (Section 6.1)
thm-cof-embedding-into-complete (proof): Step 1, iota_F(-n) = -(n*1_F); -(-x) = x | thm-rationals-embed-ordered-field (sums, iota_F(n) = n*1_F), prp-ring-algebra (a) (uniqueness of negatives, -(-a) = a); inline
thm-cof-embedding-into-complete (proof): phi(-x) = -phi(x) | prp-ring-algebra (a)
thm-cof-embedding-into-complete (proof): x = 0 or y = 0 gives both sides 0_L | Step 3 (phi(0_F) = 0_L), prp-ring-algebra (b), (F6)
thm-cof-embedding-into-complete (proof): x < 0 gives -x > 0 | prp-ordered-ring-rules (a), -0 = 0 (prp-ring-algebra (a))
thm-cof-embedding-into-complete (proof): x < 0 < y gives xy = -((-x)y); (-a)(-b) = ab | prp-ring-algebra (c)
thm-cof-embedding-into-complete (proof): chi reflects order | the remark after def-cof-order-preserving-map (Section 6.1)
thm-cof-embedding-into-complete (proof): maps with equal values at every point are equal | fd2:def-function (equality of functions); inline
thm-cof-embedding-into-complete (claim): remark, existence fails for F = R, L = Q and for F = Q(t), L complete | thm-constructed-reals-archimedean, prp-cof-map-fixes-rationals, exm-sqrt2-class, thm-no-rational-square-two, exm-rational-function-field, thm-rationals-embed-ordered-field (iota_L(n) = n*1_L), thm-cof-complete-archimedean; remark only, nothing depends on it
thm-cof-embedding-into-complete (claim): warning, Q_R(sqrt 2) and A = {p in Q : p^2 < 2} have the same upper bounds in Q (A is contained in Q_R(sqrt 2), whose other elements are negative, below 0 in A) | exm-cof-rationals-below-sqrt2, thm-rationals-gap-sqrt2 (a); inline
thm-cof-embedding-into-complete (claim): warning, sup in F of iota_F(Q_F(x)) exists and is x | exr-completeness-and-archimedes-b2 (pointer only; the two-line proof is x an upper bound plus thm-rationals-dense-ordered-field and totality, prp-ordered-field-halves (a)); nothing depends on it
thm-cof-embedding-into-complete (solution): quick check, L = F gives the identity | thm-cof-complete-archimedean and the uniqueness clause; inline
exr-measuring-by-rationals-a1 (solution): iota_Q is the identity | Chapter 4, paragraph after thm-rationals-embed-ordered-field
exr-measuring-by-rationals-a1 (solution): sup of Q_F(x)'s copies in F is x | exr-completeness-and-archimedes-b2 (an exercise, cited only in this solution)
exr-measuring-by-rationals-b2 (claim): (z + y/2)^2 + (3/4)y^2 > 0 unless y = z = 0 | prp-ordered-ring-rules (e), (c), (b); inline
exr-measuring-by-rationals-b2 (solution): z^3 - y^3 factorization; (z + y/2)^2 + (3/4)y^2; (s + h)^3 bound; (s - h)^3 - a = h^2(3s - h) for h = (s^3 - a)/(3s^2); h < s; m = min{1, a/2} in S | inline; verify/ch06/exr-measuring-by-rationals-b2.py
exr-measuring-by-rationals-c1 (solution): in Q(t), 1/t and 2/t have the same rationals below them (q <= 0) | exm-rational-function-field (school polynomial algebra, flagged there), thm-rationals-archimedean, prp-reciprocal-order (b); remark only, nothing depends on it
exr-measuring-by-rationals-c2 (solution): Step 3 of the proof of thm-cof-embedding-into-complete | cited by name (a step of an earlier proof in this section)
-->
