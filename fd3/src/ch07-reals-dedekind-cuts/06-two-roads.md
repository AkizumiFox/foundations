# The Two Roads Give the Same Real Numbers

This section is part of the optional Chapter 7, and nothing outside the chapter depends on it. We now have two complete ordered fields. Chapter 5 built one from classes of Cauchy sequences of rationals (@thm-reals-complete-ordered-field), and Section 7.5 built another from cuts (@thm-cuts-complete-field). Their elements have nothing in common: a class of sequences is not a set of rationals. Chapter 6 proved that any two complete ordered fields are linked by exactly one order-preserving field isomorphism (@thm-cof-uniqueness). This section applies that theorem to the two models, computes the isomorphism explicitly, and compares what each road had to pay for.

## Two models on one page

With both models in view, one letter \( \nR \) is not enough. In this section only, \( \nR_{\mathrm C} \) denotes the field \( \nR \) of Chapter 5, the quotient set \( \sC/{\sim} \) of @def-reals-cauchy-classes, and \( \nR_{\mathrm D} \) the field of cuts of @def-dedekind-cut. Each contains its own copy of \( \nQ \), given by the map of @thm-rationals-embed-ordered-field. In \( \nR_{\mathrm D} \) that copy is \( q \mapsto D_q \) (@thm-rationals-embed-cuts). In \( \nR_{\mathrm C} \) we write
\[
\iota \coloneqq \iota_{\nR_{\mathrm C}} \colon \nQ \to \nR_{\mathrm C} ,
\]
which is the map \( \kappa(q) = [(q)_n] \) of @def-rational-embedding, by @thm-rational-embedding (d). From the identification in Section 5.4 on, Chapter 5 wrote \( q \) for \( \kappa(q) \). Here we keep \( \iota \) visible, since a bare \( q \) could now mean an element of either field.

Recall from Section 6.1 the rationals below an element \( x \) of an ordered field \( F \) (@def-cof-rationals-below):
\[
\nQ_F(x) \coloneqq \{ q \in \nQ : \iota_F(q) < x \} .
\]
Section 6.1 remarked that this set is closed downward. In \( \nR_{\mathrm D} \), the rationals below a cut \( \alpha \) are \( \{ q : D_q < \alpha \} \), and @prp-rational-in-cut (a) says that this set is \( \alpha \) itself. So in the cut model **every element is its own set of rationals below**. The theorem below says what the isomorphism does with this.

## The isomorphism

The uniqueness theorem gives the existence and uniqueness of an isomorphism, but says nothing about what it does to a given element. For these two models, what it does can be written down.

::: {#thm-dedekind-same-reals}
[The Two Constructions Give the Same Reals]

Let \( \nR_{\mathrm C} \) be the field of Chapter 5, \( \nR_{\mathrm D} \) the field of cuts, and \( \iota = \iota_{\nR_{\mathrm C}} \).

::: {.enumerate options="label=(\alph*)"}
1. There is **exactly one** order-preserving field isomorphism \( \Psi \colon \nR_{\mathrm C} \to \nR_{\mathrm D} \) (@def-cof-order-preserving-map).
2. \( \Psi(\iota(q)) = D_q \) for every \( q \in \nQ \).
3. For every \( x \in \nR_{\mathrm C} \),
\[
\Psi(x) = \nQ_{\nR_{\mathrm C}}(x) = \{ q \in \nQ : \iota(q) < x \} .
\]
:::
:::

::: {.idea}
Part (a) is Chapter 6's theorem, once both fields are known to be complete; that work is already done. Part (b) says that \( \Psi \) carries each copy of \( \nQ \) to the other. Chapter 6 showed that every map respecting sums, products and \( 1 \) fixes the rationals (@prp-cof-map-fixes-rationals). Here "fixes" means \( \Psi \circ \iota_{\nR_{\mathrm C}} = \iota_{\nR_{\mathrm D}} \), and we know \( \iota_{\nR_{\mathrm D}} \). Part (c) is then a chain of three equivalences. A rational \( q \) lies in the cut \( \Psi(x) \) exactly when \( D_q \) lies below it. By (b), \( D_q \) is \( \Psi(\iota(q)) \). And \( \Psi \) compares elements the way \( \nR_{\mathrm C} \) does.

*Before reading on: where is the uniqueness in @thm-cof-uniqueness used, and where only existence?*
:::

::: {.proof}
*(a)* \( \nR_{\mathrm C} \) is a complete ordered field by @thm-reals-complete-ordered-field, and \( \nR_{\mathrm D} \) is one by @thm-cuts-complete-field. By @thm-cof-uniqueness, with \( F = \nR_{\mathrm C} \) and \( L = \nR_{\mathrm D} \), there is exactly one order-preserving field isomorphism \( \Psi \colon \nR_{\mathrm C} \to \nR_{\mathrm D} \).

*(b)* \( \Psi \) respects sums and products and sends \( 1 \) to \( 1 \) (@def-cof-order-preserving-map). By @prp-cof-map-fixes-rationals, \( \Psi \circ \iota_{\nR_{\mathrm C}} = \iota_{\nR_{\mathrm D}} \). By @thm-rationals-embed-cuts, \( \iota_{\nR_{\mathrm D}}(q) = D_q \) for every \( q \in \nQ \). Hence \( \Psi(\iota(q)) = D_q \).

*(c)* First, \( \Psi \) reflects order: if \( \Psi(u) < \Psi(v) \), then \( u < v \). Indeed, \( u = v \) would give \( \Psi(u) = \Psi(v) \), and \( v < u \) would give \( \Psi(v) < \Psi(u) \), and trichotomy (O1) in \( \nR_{\mathrm D} \) excludes both; so \( u < v \) by (O1) in \( \nR_{\mathrm C} \). Together with strict increase, \( u < v \iff \Psi(u) < \Psi(v) \).

Now let \( x \in \nR_{\mathrm C} \) and \( q \in \nQ \). The value \( \Psi(x) \) is a cut, so
\[
q \in \Psi(x) \iff D_q < \Psi(x) \iff \Psi(\iota(q)) < \Psi(x) \iff \iota(q) < x .
\]
The first equivalence is @prp-rational-in-cut (a), \( q \in \alpha \iff D_q \subsetneq \alpha \), read with \( \subsetneq \) as \( < \) (@def-cut-order). The second is (b). The third holds because \( \Psi \) preserves and reflects \( < \). The last condition says \( q \in \nQ_{\nR_{\mathrm C}}(x) \) (@def-cof-rationals-below). Since \( \Psi(x) \) and \( \nQ_{\nR_{\mathrm C}}(x) \) are subsets of \( \nQ \) with the same elements, they are equal. This proves the theorem.
:::

The answer to the prompt: uniqueness is used only for the words "exactly one" in (a). Parts (b) and (c) use nothing about \( \Psi \) except that it respects sums, products and \( 1 \), and is strictly increasing. So any order-preserving field map \( \nR_{\mathrm C} \to \nR_{\mathrm D} \) would satisfy (c), and (c) determines the map. That gives a second proof of the uniqueness in (a), by computation. The existence in (a) is the part that computation does not give cheaply. A direct proof would show that \( x \mapsto \nQ_{\nR_{\mathrm C}}(x) \) lands in the cuts, is onto, is strictly increasing (hence injective), sends \( 1 \) to \( D_1 \), and respects sums and products. The first two are Exercises C2(a) and C2(b), each a few lines. Strict increase is @lem-cof-rationals-separate, since \( \nR_{\mathrm C} \) is Archimedean (@thm-cof-complete-archimedean), and \( \nQ_{\nR_{\mathrm C}}(\iota(1)) = D_1 \) holds by the definitions. Sums are @lem-cof-below-sum read in \( \nR_{\mathrm C} \) (Exercise B1). The product, with its sign cases, is the work Chapter 6 did once for all complete ordered fields.

Part (c) can also be read off Chapter 6's construction. By property \( (\star) \) of @thm-cof-embedding-into-complete, \( \nQ_{\nR_{\mathrm D}}(\Psi(x)) = \nQ_{\nR_{\mathrm C}}(x) \), and \( \nQ_{\nR_{\mathrm D}}(\alpha) = \alpha \) for every cut, as we saw above. The proof given here avoids \( (\star) \) and uses only that \( \Psi \) fixes the rationals.

So part (c) says: *the cut attached to a Cauchy real is the set of rationals below it.* Dedekind's definition is what the Cauchy model sees when it looks at one of its elements through the rationals. The map also runs the other way. Its inverse \( \Psi^{-1} \colon \nR_{\mathrm D} \to \nR_{\mathrm C} \) is again an order-preserving field isomorphism (the second-reading fold after @cor-cof-isomorphic-to-cauchy-reals checks this for any isomorphism). So by the uniqueness clause of @thm-cof-embedding-into-complete, applied with \( F = \nR_{\mathrm D} \), which is Archimedean by @thm-cof-complete-archimedean, and \( L = \nR_{\mathrm C} \), it is the map of that theorem:
\[
\begin{aligned}
\Psi^{-1}(\alpha) &= \sup\nolimits_{\nR_{\mathrm C}} \{ \iota(q) : q \in \nQ_{\nR_{\mathrm D}}(\alpha) \} \\
&= \sup\nolimits_{\nR_{\mathrm C}} \{ \iota(q) : q \in \alpha \} .
\end{aligned}
\]
A cut is sent to the least upper bound, in the Cauchy model, of its own rationals. Exercise C2 below proves the same correspondence directly in any complete ordered field \( F \): there \( x \mapsto \nQ_F(x) \) is onto the cuts, with inverse \( \alpha \mapsto \sup\nolimits_F \{ \iota_F(q) : q \in \alpha \} \). For an Archimedean \( F \), C2 also shows that this map is onto exactly when \( F \) is complete.

::: {.check}
What is \( \Psi(\iota(-3/4)) \)? Is \( \Psi \) determined by its values on the elements \( \iota(q) \), \( q \in \nQ \)?
:::

::: {.solution}
By (b), \( \Psi(\iota(-3/4)) = D_{-3/4} = \{ r \in \nQ : r < -3/4 \} \); by (c) this is also \( \{ q : \iota(q) < \iota(-3/4) \} \), the same set, since \( \iota \) preserves and reflects order. Yes: by (c), \( \Psi(x) \) is the set of \( q \) with \( \iota(q) < x \), which is determined by how \( x \) compares with the elements \( \iota(q) \). The order of \( \nR_{\mathrm C} \), together with the values \( \Psi(\iota(q)) = D_q \), decides everything.
:::

::: {.warning}
"The same real numbers" means **isomorphic as ordered fields, by a unique isomorphism**. It does not mean that the two sets have the same elements. The cut \( \sigma \) contains the rational \( 0 \); the element of \( \nR_{\mathrm C} \) that corresponds to it is a class of sequences, and its elements are functions \( \nN \to \nQ \), not rationals. Informally, the isomorphism carries every statement about sums, products and order in one field to the same statement in the other, so no such statement can tell the two fields apart; Section 6.5 explains this pattern and why it is not stated as a theorem.
:::

## The square root of two, twice

Chapter 5 found a square root of \( 2 \) as the class of the Newton sequence (@exm-sqrt2-class). Chapter 7 found one as the cut \( \sigma \) (@prp-cut-sqrt2-square). The isomorphism should match them.

::: {#exm-two-roads-sqrt2 .optional}
[The Two Square Roots of Two]

Let \( x \in \nR_{\mathrm C} \) with \( x > 0 \) and \( x^2 = \iota(2) \); for instance the class \( r \) of the Newton sequence (@exm-sqrt2-class), which has \( r > 0 \) and \( r^2 = \kappa(2) = \iota(2) \) (@thm-rational-embedding (d)). Show that \( \Psi(x) = \sigma \).
:::

::: {.solution}
Since \( \Psi \) is multiplicative, \( \Psi(x)^2 = \Psi(x^2) = \Psi(\iota(2)) = D_2 \), by @thm-dedekind-same-reals (b). By @prp-cut-sqrt2-square, \( \sigma \sigma = D_2 \) as well. Both are positive: \( \Psi(x) > \Psi(\iota(0)) = D_0 \), since \( x > 0 = \iota(0) \) and \( \Psi \) is strictly increasing, and \( \sigma > D_0 \) by @prp-cut-sqrt2-square.

Positive square roots are unique in an ordered field. If \( u, v > 0 \) and \( u \ne v \), say \( u < v \), then \( u^2 < v^2 \) by @prp-ordered-ring-rules (g). Applied in \( \nR_{\mathrm D} \) to \( u = \Psi(x) \) and \( v = \sigma \), which have the same square \( D_2 \), this gives \( \Psi(x) = \sigma \).

For the Newton class there is a second route through (c): \( \Psi(r) = \nQ_{\nR_{\mathrm C}}(r) \), and @exm-cof-rationals-below-sqrt2 computed this set as the rationals \( q < 0 \) together with those \( q \ge 0 \) with \( q^2 < 2 \). That is \( \sigma \), written differently.
:::

Exercise C1 below runs the correspondence backwards: from any cut \( \alpha \) it builds a Cauchy sequence of rationals whose class \( \Psi \) sends to \( \alpha \). Applied to \( \alpha = \sigma \), it produces a positive element of \( \nR_{\mathrm C} \) with square \( \iota(2) \). As a **source** for such an element, though, that route would assume what the example illustrates, so the example takes \( x \) from Chapter 5.

## What each road pays for

Both constructions start from \( \nQ \) and end at a complete ordered field, and by @thm-dedekind-same-reals they end at the same one. They spend their effort in different places.

| | Cauchy sequences (Chapter 5) | Dedekind cuts (Chapter 7) |
|---|---|---|
| an element is | a class of Cauchy sequences of rationals (@def-reals-cauchy-classes) | a set of rationals with (C1)–(C3) (@def-dedekind-cut) |
| equality | equality of classes; every operation and the order must be shown independent of representatives (@thm-reals-operations-well-defined, @prp-positivity-well-defined) | equality of sets; nothing to check |
| sum and product | termwise on representatives (@def-reals-operations) | the sum is the set sum (@def-cut-sum); the negative needs a margin (@def-cut-negative); the product is defined for positive cuts, then by signs (@def-cut-product) |
| inverses | through the sign theorem for Cauchy sequences (@thm-reals-field) | a margin again, by "walk up" (@def-cut-reciprocal, @thm-cut-reciprocal) |
| order | positive classes, eventually above a fixed rational margin (@def-positive-cauchy-sequence) | inclusion (@def-cut-order), total by @thm-cut-order-total |
| completeness | every Cauchy sequence converges (Section 5.5), then bisection (@thm-cauchy-archimedean-lub) | a union (@thm-dedekind-lub) |
| generalizes to | the completion of a metric space | the completion of an ordered set |

Read down the columns. The Cauchy road gets its arithmetic cheaply, termwise, and pays at both ends: every definition must be checked against a change of representative, the order needs a margin, and completeness takes two sections. The Dedekind road gets order and completeness almost free, because a cut is a set and inclusion is already an order, and pays in the middle: negatives need a margin, and multiplication needs a detour through positive cuts and signs.

The last row looks beyond this volume. The Cauchy construction works for any metric space, with sequences whose terms get close: *Metric and Topological Spaces*, Chapter 2 builds the completion of a metric space that way. The Dedekind construction has an analogue for any ordered set, in which a cut is a set of elements that equals the set of lower bounds of its upper bounds; the result is called the Dedekind–MacNeille completion, and no volume of this series develops it. Each road leads somewhere the other does not.

::: {.second-reading title="History"}
Richard Dedekind published the construction by cuts in 1872, in *Stetigkeit und irrationale Zahlen*; he says there that the idea came to him in 1858, while preparing lectures on the differential calculus. Charles Méray had built the irrational numbers from convergent sequences of rationals in 1869, and Georg Cantor and Eduard Heine gave constructions from fundamental sequences, our Cauchy sequences, in 1872. Karl Weierstrass had presented his own construction of the real numbers in his Berlin lectures of the 1860s. The two roads of this volume were thus laid out within a few years of each other.
:::

## Exercises

### A. Check your understanding

::: {#exr-two-roads-a1}
[A1]

These questions are about the proof of @thm-dedekind-same-reals.

::: {.enumerate options="label=(\alph*)"}
1. Name the earlier results the proof uses, and say for which of (a), (b), (c) each is used.
2. Run part (c) for \( x = \iota(1/2) \): which rationals lie in \( \Psi(x) \)? Check your answer against (b).
3. State the idea of the proof in two sentences.
4. Which step of (c) uses that \( \Psi \) reflects order, and which uses that \( \Psi(x) \) is a cut?
:::
:::

::: {.solution}
(a) For (a): @thm-reals-complete-ordered-field and @thm-cuts-complete-field (both fields are complete), and @thm-cof-uniqueness. For (b): @prp-cof-map-fixes-rationals, and @thm-rationals-embed-cuts for \( \iota_{\nR_{\mathrm D}}(q) = D_q \). For (c): @prp-rational-in-cut (a), part (b) of the theorem, and trichotomy (O1) of @def-ordered-ring-and-field in both fields, to see that \( \Psi \) reflects order.

(b) \( q \in \Psi(\iota(1/2)) \iff \iota(q) < \iota(1/2) \iff q < 1/2 \), since \( \iota \) is strictly increasing and reflects order (@thm-rationals-embed-ordered-field). So \( \Psi(\iota(1/2)) = \{ q \in \nQ : q < 1/2 \} = D_{1/2} \), which is what (b) says.

(c) Both fields are complete, so Chapter 6 supplies exactly one isomorphism, and like every map that respects sums, products and \( 1 \), it carries the copy of \( \nQ \) in one field to the copy in the other. Since a cut consists of the rationals \( q \) with \( D_q \) below it, the isomorphism sends \( x \) to the set of rationals below \( x \).

(d) The third equivalence, \( \Psi(\iota(q)) < \Psi(x) \Rightarrow \iota(q) < x \), uses that \( \Psi \) reflects order; the reverse implication uses strict increase. The first equivalence, \( q \in \Psi(x) \iff D_q < \Psi(x) \), is @prp-rational-in-cut, which holds only for cuts.
:::

### B. Practice

::: {#exr-two-roads-b1}
[B1]

Let \( x, y \in \nR_{\mathrm C} \).

::: {.enumerate options="label=(\alph*)"}
1. Deduce from @lem-cof-below-sum, without using \( \Psi \), that \( \nQ_{\nR_{\mathrm C}}(x + y) = \nQ_{\nR_{\mathrm C}}(x) + \nQ_{\nR_{\mathrm C}}(y) \), where the right side is the set sum of @def-cut-sum. Say why the lemma applies to \( \nR_{\mathrm C} \).
2. Explain how (a), read through @thm-dedekind-same-reals (c), is the statement \( \Psi(x + y) = \Psi(x) + \Psi(y) \).
:::
:::

::: {.solution}
Write \( \nQ(z) \) for \( \nQ_{\nR_{\mathrm C}}(z) \).

(a) The field \( \nR_{\mathrm C} \) is Archimedean (@thm-constructed-reals-archimedean), so @lem-cof-below-sum applies with \( F = \nR_{\mathrm C} \), \( a = x \) and \( b = y \): for every \( q \in \nQ \),
\[
q \in \nQ(x + y) \iff \exists r \in \nQ \ \bigl( r \in \nQ(x) \wedge q - r \in \nQ(y) \bigr) .
\]
\( (\subseteq) \) If \( q \in \nQ(x + y) \), take \( r \) as on the right; then \( q = r + (q - r) \) with \( r \in \nQ(x) \) and \( q - r \in \nQ(y) \), so \( q \in \nQ(x) + \nQ(y) \).

\( (\supseteq) \) If \( q = r + s \) with \( r \in \nQ(x) \) and \( s \in \nQ(y) \), then \( q - r = s \in \nQ(y) \), so the right side holds with this \( r \), and \( q \in \nQ(x + y) \).

(b) By @thm-dedekind-same-reals (c), \( \nQ(x + y) = \Psi(x + y) \), \( \nQ(x) = \Psi(x) \) and \( \nQ(y) = \Psi(y) \), and the set sum of two cuts is their sum in \( \nR_{\mathrm D} \) (@def-cut-sum). So (a) says \( \Psi(x + y) = \Psi(x) + \Psi(y) \). We knew this already, since \( \Psi \) is additive; (a) is @lem-cof-below-sum read in \( \nR_{\mathrm C} \) as a statement about cuts.
:::

### C. Going deeper

::: {#exr-two-roads-c1}
[C1: From a cut to a Cauchy sequence]

Let \( \alpha \) be a cut. For \( n \in \nN \) let \( 2^{-n} \coloneqq \bigl( (2 \cdot 1_{\nQ})^n \bigr)^{-1} \) (@def-naturals-in-ordered-field). Fix \( a \in \alpha \), and for each \( n \) let \( k_n \) be the **least** \( k \in \nN \) with \( a + k \, 2^{-n} \notin \alpha \), and \( a_n \coloneqq a + (k_n - 1) \, 2^{-n} \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( k_n \) exists and \( k_n \ge 1 \), and that \( a_n \in \alpha \) and \( a_n + 2^{-n} \notin \alpha \).
2. Show that \( (a_n) \) is a Cauchy sequence of rationals (@def-rational-cauchy-sequences).
3. Show that \( \Psi([(a_n)]) = \alpha \).
:::
:::

::: {.solution}
[Hint 1]

For (b), compare \( a_n \) with \( a_m + 2^{-m} \): one is in \( \alpha \) and the other is not. For (c), use @thm-dedekind-same-reals (c), so that you only need to decide when \( \iota(q) < [(a_n)] \).
:::

::: {.solution}
[Hint 2]

For (c), if \( q \in \alpha \), take \( q' \in \alpha \) with \( q' > q \), and show that \( a_n > (q + q')/2 \) for all large \( n \).
:::

::: {.solution}
Write \( \varepsilon_n \coloneqq 2^{-n} \). By @lem-power-two-bound with \( F = \nQ \), \( (2 \cdot 1_{\nQ})^n \ge n + 1 > 0 \), so \( \varepsilon_n > 0 \).

*A threshold for \( \varepsilon_n \).* Let \( \varepsilon \in \nQ \), \( \varepsilon > 0 \). By @thm-rationals-archimedean there is \( N \in \nN \) with \( N > 1/\varepsilon \), that is, \( N \varepsilon > 1 \). For \( n \ge N \), @lem-power-two-bound gives \( (2 \cdot 1_{\nQ})^n \varepsilon \ge (n + 1)\varepsilon > N \varepsilon > 1 \), so \( \varepsilon_n < \varepsilon \). Call this \( (\dagger) \): for every rational \( \varepsilon > 0 \) there is \( N \) with \( \varepsilon_n < \varepsilon \) for all \( n \ge N \).

(a) The set \( S_n \coloneqq \{ k \in \nN : a + k \varepsilon_n \notin \alpha \} \) is non-empty. Indeed, take \( b \notin \alpha \) (C1); by @thm-rationals-archimedean there is \( m \in \nN \) with \( m > (b - a)/\varepsilon_n \), so \( a + m \varepsilon_n > b \), and \( a + m \varepsilon_n \notin \alpha \) because the complement of a cut is closed upward (@lem-cut-separation). This is the first step of the proof of @lem-cut-step. So \( S_n \) is a non-empty set of integers (\( \nN \subseteq \nZ \), @thm-integers-ordered-ring (b)), and \( 0 \) is a lower bound of it; by @prp-integer-least-element it has a least element \( k_n \). Since \( a + 0 \cdot \varepsilon_n = a \in \alpha \), \( k_n \ne 0 \), so \( k_n \ge 1 \) (@thm-integers-ordered-ring (c)) and \( k_n - 1 \in \nN \). By minimality \( k_n - 1 \notin S_n \), so \( a_n \in \alpha \); and \( a_n + \varepsilon_n = a + k_n \varepsilon_n \notin \alpha \). Each \( a_n \) is defined by a rule from the fixed \( a \), so no choice principle is involved.

(b) For any \( m, n \in \nN \): \( a_n \in \alpha \) and \( a_m + \varepsilon_m \notin \alpha \), so \( a_n < a_m + \varepsilon_m \) by @lem-cut-separation; symmetrically, \( a_m < a_n + \varepsilon_n \). Given a rational \( \varepsilon > 0 \), take \( N \) from \( (\dagger) \). For \( m, n \ge N \),
\[
-\varepsilon < -\varepsilon_m < a_m - a_n < \varepsilon_n < \varepsilon ,
\]
so \( \abs{a_m - a_n} < \varepsilon \) (@prp-absolute-value-ordered-field (d)). Hence \( (a_n) \in \sC \).

(c) Let \( x \coloneqq [(a_n)] \in \nR_{\mathrm C} \). By @thm-dedekind-same-reals (c), \( \Psi(x) = \{ q \in \nQ : \iota(q) < x \} \), and \( \iota = \kappa \) (@thm-rational-embedding (d)). So it suffices to show \( \kappa(q) < x \iff q \in \alpha \) for every \( q \in \nQ \).

*If \( q \in \alpha \).* By (C3) there is \( q' \in \alpha \) with \( q' > q \). For every \( n \), \( q' \in \alpha \) and \( a_n + \varepsilon_n \notin \alpha \) give \( q' < a_n + \varepsilon_n \) (@lem-cut-separation). Apply \( (\dagger) \) with \( \varepsilon \coloneqq (q' - q)/2 \): for \( n \ge N \),
\[
a_n > q' - \varepsilon_n > q' - \frac{q' - q}{2} = \frac{q + q'}{2} .
\]
By @lem-termwise-order, applied to the constant sequence with value \( (q + q')/2 \) and to \( (a_n) \), \( \kappa\bigl( (q + q')/2 \bigr) \le x \). Since \( q < (q + q')/2 \), @thm-rational-embedding (b) gives \( \kappa(q) < \kappa\bigl( (q + q')/2 \bigr) \le x \).

*If \( q \notin \alpha \).* For every \( n \), \( a_n \in \alpha \) gives \( a_n < q \) (@lem-cut-separation). By @lem-termwise-order, \( x \le \kappa(q) \), so \( \kappa(q) < x \) is false by (O1).

Hence \( \Psi(x) = \alpha \). The argument used neither monotonicity of \( (a_n) \) nor any law of exponents in \( \nQ \): only the inequality of @lem-power-two-bound.

**Marking scheme.** (10 points)
- 2: (a), with the least-element principle and the reason \( k_n \ge 1 \).
- 3: (b), from the two separation inequalities and a threshold \( N \) for \( 2^{-n} \) with a stated reason.
- 3: (c) for \( q \in \alpha \): the strict gap \( q' > q \) from (C3), then a correct passage to \( \kappa(q) < x \), either by @lem-termwise-order (which gives only \( \le \)) against the midpoint \( (q + q')/2 \) followed by @thm-rational-embedding (b), or directly by showing that \( (a_n - q)_n \), a representative of \( x - \kappa(q) \), is eventually \( \ge \) the fixed margin \( (q' - q)/2 \) (@def-positive-cauchy-sequence). Either route earns all 3 points.
- 2: (c) for \( q \notin \alpha \).
Fatal errors (0 for the step): concluding \( \kappa(q) < x \) from \( q < a_n \) for all \( n \) (termwise \( < \) gives only \( \le \) between classes); choosing \( N \) after \( m, n \).
:::

::: {#exr-two-roads-c2}
[C2: Exit check: the rationals below, as a cut]

Let \( F \) be an Archimedean ordered field (@def-archimedean-ordered-field). Prove:

::: {.enumerate options="label=(\alph*)"}
1. \( \nQ_F(x) \) is a cut for every \( x \in F \);
2. the map \( \nQ_F \colon F \to \nR_{\mathrm D} \), \( x \mapsto \nQ_F(x) \), is onto if and only if \( F \) is complete (@def-complete-ordered-field).
:::

You may use @lem-cof-rationals-separate: \( x \le y \iff \nQ_F(x) \subseteq \nQ_F(y) \), so the map is injective.
:::

::: {.solution}
Throughout, \( \iota_F \) is strictly increasing and reflects order (@thm-rationals-embed-ordered-field).

(a) *(C1).* By @def-archimedean-ordered-field there is \( n \in \nN \) with \( x < n \cdot 1_F = \iota_F(n) \); then \( \iota_F(n) < x \) fails by (O1), so \( n \notin \nQ_F(x) \), and \( \nQ_F(x) \ne \nQ \). Applied to \( -x \), the same property gives \( m \in \nN \) with \( -x < \iota_F(m) \), so \( \iota_F(-m) = -\iota_F(m) < x \) (@prp-ordered-ring-rules (a)), and \( -m \in \nQ_F(x) \ne \emptyset \).

*(C2).* If \( q \in \nQ_F(x) \) and \( p < q \), then \( \iota_F(p) < \iota_F(q) < x \), so \( p \in \nQ_F(x) \).

*(C3).* If \( q \in \nQ_F(x) \), then \( \iota_F(q) < x \), and @thm-rationals-dense-ordered-field gives \( q' \in \nQ \) with \( \iota_F(q) < \iota_F(q') < x \). Then \( q' > q \), since \( \iota_F \) reflects order, and \( q' \in \nQ_F(x) \).

(b) \( (\Leftarrow) \) Let \( F \) be complete and \( \alpha \) a cut. Put \( S \coloneqq \{ \iota_F(q) : q \in \alpha \} \). It is non-empty, since \( \alpha \ne \emptyset \). Take \( b \notin \alpha \) (C1); every \( q \in \alpha \) has \( q < b \) (@lem-cut-separation), so \( \iota_F(b) \) is an upper bound of \( S \). By completeness \( s \coloneqq \sup S \) exists. We show \( \nQ_F(s) = \alpha \).

If \( q \in \alpha \), (C3) gives \( q' \in \alpha \) with \( q' > q \), and \( \iota_F(q) < \iota_F(q') \le s \). So \( q \in \nQ_F(s) \).

If \( q \notin \alpha \), every \( p \in \alpha \) has \( p < q \) (@lem-cut-separation), so \( \iota_F(q) \) is an upper bound of \( S \), and \( s \le \iota_F(q) \) because \( s \) is the least one. So \( \iota_F(q) < s \) fails, and \( q \notin \nQ_F(s) \).

Hence \( \nQ_F(s) = \alpha \), and the map is onto.

\( (\Rightarrow) \) Let the map be onto. By (a) and @lem-cof-rationals-separate, it is a bijection \( F \to \nR_{\mathrm D} \) with \( x \le y \iff \nQ_F(x) \subseteq \nQ_F(y) \). Let \( A \subseteq F \) be non-empty and bounded above by \( u \). The set \( \{ \nQ_F(a) : a \in A \} \) of cuts is non-empty and bounded above by \( \nQ_F(u) \), so it has a supremum \( \gamma \) in \( (\nR_{\mathrm D}, \subseteq) \) (@thm-dedekind-lub). Since the map is onto, \( \gamma = \nQ_F(s) \) for some \( s \in F \). For \( a \in A \), \( \nQ_F(a) \subseteq \nQ_F(s) \), so \( a \le s \): \( s \) is an upper bound of \( A \). If \( v \) is any upper bound of \( A \), then \( \nQ_F(v) \) is an upper bound of the set of cuts, so \( \nQ_F(s) = \gamma \subseteq \nQ_F(v) \), and \( s \le v \). Hence \( s = \sup A \), and \( F \) is complete.

For \( F = \nR_{\mathrm C} \), (b) gives a second proof that \( x \mapsto \nQ_{\nR_{\mathrm C}}(x) \), the map \( \Psi \) of @thm-dedekind-same-reals (c), is onto.

**Marking scheme.** (10 points)
- 2: (a) (C1), with the Archimedean property used for **both** halves (a rational outside, and a rational inside).
- 1: (a) (C2) by transitivity, and (C3) by density.
- 1: (b) \( (\Leftarrow) \): states the candidate \( s = \sup \iota_F(\alpha) \) and why it exists (non-empty, bounded above by \( \iota_F(b) \), \( b \notin \alpha \)).
- 2: \( \alpha \subseteq \nQ_F(s) \), using (C3) of \( \alpha \) to get the strict inequality.
- 2: \( \nQ_F(s) \subseteq \alpha \), from "\( \iota_F(q) \) is an upper bound".
- 2: \( (\Rightarrow) \) through the order isomorphism onto \( (\nR_{\mathrm D}, \subseteq) \) and @thm-dedekind-lub.
Fatal errors (0 for the step): using \( \iota_F(q) \le x \) in place of \( \iota_F(q) < x \) (the set then has a largest element when \( x = \iota_F(r) \)); concluding \( q \in \nQ_F(s) \) from \( \iota_F(q) \le s \).
:::

### R. Review

::: {#exr-two-roads-r1}
[R1]

Let \( f \colon \nR_{\mathrm D} \to \nR_{\mathrm D} \) satisfy \( \alpha \le \beta \Rightarrow f(\alpha) \le f(\beta) \) for all cuts \( \alpha, \beta \), and \( f(D_q) = D_q \) for every \( q \in \nQ \). Prove that \( f(\alpha) = \alpha \) for every cut \( \alpha \).
:::

::: {.solution}
Let \( \alpha \) be a cut, and suppose \( f(\alpha) \ne \alpha \). By @thm-cut-order-total, \( \alpha < f(\alpha) \) or \( f(\alpha) < \alpha \).

If \( \alpha < f(\alpha) \), @thm-cut-rationals-dense gives \( q \in \nQ \) with \( \alpha < D_q < f(\alpha) \). Since \( \alpha \le D_q \), the hypothesis gives \( f(\alpha) \le f(D_q) = D_q \), so \( f(\alpha) \le D_q < f(\alpha) \), which is impossible. If \( f(\alpha) < \alpha \), a rational cut with \( f(\alpha) < D_q < \alpha \) gives \( D_q = f(D_q) \le f(\alpha) < D_q \) in the same way. Hence \( f(\alpha) = \alpha \).

This is the method of Chapter 6: elements of an Archimedean field are separated by rationals (@lem-cof-rationals-separate), so a map that fixes the rationals and respects order can move nothing. Neither sums nor products were needed.
:::

::: {#exr-two-roads-r2}
[R2]

Let \( F \) be an ordered field, \( x \in F \), and \( (q_n) \) a sequence of rationals with \( \iota_F(q_n) \to x \) in \( F \). Show that \( (q_n) \) is a Cauchy sequence in \( \nQ \), and that for every \( q \in \nQ \) with \( \iota_F(q) < x \) there is \( N \in \nN \) with \( q_n > q \) for all \( n \ge N \).
:::

::: {.solution}
*Cauchy in \( \nQ \).* The sequence \( (\iota_F(q_n)) \) converges in \( F \), so it is a Cauchy sequence in \( F \) (@prp-convergent-cauchy-ordered-field). Let \( \varepsilon \in \nQ \), \( \varepsilon > 0 \). Then \( \iota_F(\varepsilon) > \iota_F(0) = 0 \), so @def-cauchy-sequence-ordered-field with the tolerance \( \iota_F(\varepsilon) \) gives \( N \) with \( \abs{\iota_F(q_m) - \iota_F(q_n)} < \iota_F(\varepsilon) \) for all \( m, n \ge N \). By @prp-absolute-value-ordered-field (d) and additivity of \( \iota_F \),
\[
\iota_F(-\varepsilon) < \iota_F(q_m - q_n) < \iota_F(\varepsilon) ,
\]
and since \( \iota_F \) reflects order (@thm-rationals-embed-ordered-field), \( -\varepsilon < q_m - q_n < \varepsilon \), that is, \( \abs{q_m - q_n} < \varepsilon \). So \( (q_n) \) is Cauchy in \( \nQ \) (@def-cauchy-sequence-ordered-field with \( F = \nQ \)).

*Eventually above \( q \).* Let \( \iota_F(q) < x \), and put \( \delta \coloneqq x - \iota_F(q) > 0 \). By @def-sequence-limit-ordered-field there is \( N \) with \( \abs{\iota_F(q_n) - x} < \delta \) for \( n \ge N \), so \( \iota_F(q_n) > x - \delta = \iota_F(q) \), and \( q_n > q \) because \( \iota_F \) reflects order.

Both parts are from Chapter 4. The second says that every rational \( q \) with \( \iota_F(q) < x \), that is, every element of the set \( \nQ_F(x) \) of Exercise C2, lies below all but finitely many \( q_n \). No Archimedean hypothesis was needed.
:::

::: {#exr-two-roads-r3}
[R3]

Prove that \( \card{\nR_{\mathrm D}} \le \card{\powerset{\nN}} \), and that the set \( \{ D_q : q \in \nQ \} \) of rational cuts is countable and is not all of \( \nR_{\mathrm D} \).
:::

::: {.solution}
*\( \nQ \) is countable.* This is @exr-gaps-in-the-rationals-r2: \( \nZ \) is the image of the countable set \( \nN \times \nN \) under \( a \mapsto [a] \), and \( \nQ \) is the image of the countable set \( \nZ \times \nZ_{>0} \) under \( (p, q) \mapsto [(p, q)] \), by @fd2:thm-product-countable, @fd2:prp-countable-subset, @fd2:cor-product-countable (a) and @fd2:prp-countable-image, read on \( \nN = \omega \) through Section 1.7. (It is the argument of @fd2:thm-integers-rationals-countable, run for the constructed \( \nQ \); that theorem itself is about another \( \nQ \) and is not used.)

*An injection into \( \powerset{\nN} \).* By @fd2:thm-countable-characterizations, (i) \( \Rightarrow \) (ii), there is an injection \( i \colon \nQ \to \nN \). Every cut is a subset of \( \nQ \), so \( \alpha \mapsto i(\alpha) = \{ i(q) : q \in \alpha \} \) maps \( \nR_{\mathrm D} \) into \( \powerset{\nN} \). It is injective: if \( i(\alpha) = i(\beta) \) and \( q \in \alpha \), then \( i(q) = i(q') \) for some \( q' \in \beta \), so \( q = q' \in \beta \) since \( i \) is injective; thus \( \alpha \subseteq \beta \), and symmetrically \( \beta \subseteq \alpha \). By @fd2:def-card-le, \( \card{\nR_{\mathrm D}} \le \card{\powerset{\nN}} \).

*The rational cuts.* \( \{ D_q : q \in \nQ \} \) is the image of the countable set \( \nQ \) under \( q \mapsto D_q \), so it is countable (@fd2:prp-countable-image). It is not all of \( \nR_{\mathrm D} \): \( \sigma \) is not a rational cut (@prp-cut-sqrt2-square).

Much more is true: \( \nR_{\mathrm D} \) is in bijection with \( \nR_{\mathrm C} \) (@thm-dedekind-same-reals), which @exr-the-least-upper-bound-property-r3 showed to be uncountable. So \( \nR_{\mathrm D} \) is uncountable, while its rational cuts are countable.
:::

::: {#exr-two-roads-r4}
[R4]

Is the set \( \{ \alpha \in \nR_{\mathrm D} : \alpha \ne D_q \text{ for every } q \in \nQ \} \) of irrational cuts closed under addition? Justify your answer.
:::

::: {.solution}
No. The tool is the additive inverse of a cut (@thm-cut-additive-inverse) together with the arithmetic of rational cuts (@thm-rationals-embed-cuts).

The cut \( \sigma \) is irrational (@prp-cut-sqrt2-square). So is \( -\sigma \): if \( -\sigma = D_q \), then \( \sigma = -(-\sigma) = -D_q = D_{-q} \) (@prp-ring-algebra (a) in the field \( \nR_{\mathrm D} \), and @thm-rationals-embed-cuts (c)), which is impossible. But \( \sigma + (-\sigma) = D_0 \) (@thm-cut-additive-inverse), a rational cut. So two irrational cuts can have a rational sum.

The school slogan "irrational plus irrational is irrational" is false, and its opposite is no rule either: \( \sigma + \sigma \) is irrational. Indeed \( \sigma + \sigma = (D_1 + D_1)\sigma = D_2 \sigma \) by distributivity, and if \( D_2 \sigma = D_r \), then \( \sigma = D_{1/2} D_r = D_{r/2} \) by @thm-rationals-embed-cuts (d), which is impossible. Whether a sum of irrational cuts is rational depends on the summands, not on a rule; a proof has to look at them.
:::

<!-- dependency ledger
sec-two-roads (claim): Chapter 5 writes q for kappa(q) from the identification in Section 5.4 on | identification remark of F3.10 §04 (NOTATION, kappa row); recalled in prose
sec-two-roads (claim): Q_F(x) is closed downward | stated in Section 6.1 after def-cof-rationals-below; recalled in prose
thm-dedekind-same-reals (proof): an order-preserving field map reflects order | inline, from trichotomy (O1) of def-ordered-ring-and-field (as in the opening of Section 6.3)
thm-dedekind-same-reals (claim): the inverse of an order-preserving field isomorphism is one | the second-reading fold after cor-cof-isomorphic-to-cauchy-reals (Section 6.3), pointed to in prose
sec-two-roads (claim): x -> Q_{R_C}(x) is strictly increasing and sends 1 to D_1 | lem-cof-rationals-separate with thm-cof-complete-archimedean (cited); def-cof-rationals-below with def-rational-cut for Q(iota(1)) = D_1; remark after the proof, nothing depends on it
thm-dedekind-same-reals (claim): Q_{R_D}(alpha) = alpha for every cut | prp-rational-in-cut with def-cut-order, inline in "Two models on one page"
sec-two-roads (claim): a statement in +, *, < has the same truth value in R_C and R_D | Section 6.5, explained by pattern, not stated as a theorem; nothing depends on it
exm-two-roads-sqrt2 (solution): Psi(iota(0)) = D_0 | thm-dedekind-same-reals (b) with q = 0
sec-two-roads (claim): comparison table cells (where each road pays) | the labels cited in each cell; Section 5.5 is thm-constructed-reals-cauchy-complete
sec-two-roads (claim): the Dedekind-MacNeille completion of an ordered set | not proved here; named only, no volume of the series develops it; nothing depends on it
sec-two-roads (claim): history (Dedekind 1872 and 1858, Meray 1869, Cantor and Heine 1872, Weierstrass's Berlin lectures of the 1860s) | historical remark in a second-reading fold; dates as in F3.10 §06's history fold, checked against Bloch §1.8 at S2
exr-two-roads-c1 (solution): N epsilon > 1 and (2 . 1_Q)^n >= n + 1 give 2^{-n} < epsilon; the constant sequence of a rational is in the set C | lem-power-two-bound, thm-rationals-archimedean (cited); constant sequences Cauchy as in def-rational-embedding; verify/ch07/exr-two-roads-c1.py
exr-two-roads-c1 (solution): S_n is non-empty | inline, by thm-rationals-archimedean and lem-cut-separation (the first step of lem-cut-step's proof)
exr-two-roads-c2 (solution): iota_F(-m) = -iota_F(m) | additivity of iota_F (thm-rationals-embed-ordered-field)
exr-two-roads-r3 (claim): R_C is uncountable | exr-the-least-upper-bound-property-r3 (an earlier exercise, cited); a remark after the solution, nothing depends on it
exr-two-roads-r4 (solution): sigma + sigma = (D_1 + D_1) sigma = D_2 sigma | distributivity and D_1 the unit (thm-cuts-ordered-field), D_1 + D_1 = D_2 (thm-rationals-embed-cuts (b))
-->
