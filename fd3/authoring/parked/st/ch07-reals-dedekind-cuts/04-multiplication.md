# Parked: old Chapter 7, Dedekind Cuts, 04-multiplication.md

<!-- Parked from fd3 (fd3/authoring/design/layout-proposal.md §4, approved 2026-10-26). Not part of any book's src; nothing builds or scans it.
Old section: fd3 7.4 (src/ch07-reals-dedekind-cuts/04-multiplication.md)
Labels: def-cut-product-positive, prp-cut-product-positive, lem-cut-multiplicative-step, lem-cut-distributive-positive, def-cut-product, lem-cut-sign-rules, lem-cut-distributive, def-cut-reciprocal, thm-cut-reciprocal, thm-cuts-ordered-field, exr-multiplication-a1, exr-multiplication-b1, exr-multiplication-b2, exr-multiplication-b3, exr-multiplication-c1
Intended home: ST.1 (cuts carved from P(ℚ) by (Z5)/(Z6); next to the Dedekind–MacNeille remark)
-->

# Multiplication

Like every section of this chapter, this one is optional: nothing outside Chapter 7 depends on it. Section 7.3 made the cuts an ordered group under addition (@thm-cut-ordered-group). This section adds a product and finishes the field axioms. On the Cauchy road of Chapter 5, multiplication was termwise and cost little; on this road it is the hard part. The set of all products of elements is useless, so we define the product of two **positive** cuts first, prove the laws there, and then extend to all cuts by signs, once, through one lemma (@lem-cut-sign-rules). The reciprocal needs the walk up by ε again, in a multiplicative form. The section ends with the theorem that the cuts form an ordered field.

As in Section 7.3, letters \( p, q, r, s, t, x \) stand for rationals, and the rules of the ordered field \( \nQ \) (@thm-rationals-ordered-field, @prp-ordered-ring-rules, @prp-reciprocal-order) are used for them without comment.

## Why not the set of products

For sums, the set of all sums worked. The analogous set for products,
\[
\{ pq : p \in \alpha , \ q \in \beta \} ,
\]
fails in two different ways.

*It can be everything.* Suppose \( 0 \in \alpha \) and \( 0 \in \beta \), as for \( \alpha = \beta = D_1 \). Then both cuts contain every negative rational (C2), and \( \alpha \) contains some \( a > 0 \) (C3). Every rational is a product: for \( x > 0 \), \( x = (-1)(-x) \) with \( -1 \in \alpha \), \( -x \in \beta \); \( 0 = 0 \cdot 0 \); and for \( x < 0 \), \( x = a \cdot (x/a) \) with \( x/a < 0 \), so \( x/a \in \beta \). So the set is \( \nQ \), which fails (C1). The culprit is that negatives times negatives are unbounded above.

*It can be upside down.* For \( \alpha = \beta = D_{-1} \), every product \( pq \) with \( p, q < -1 \) is \( (-p)(-q) > 1 \), and every \( x > 1 \) is such a product: \( x = p q \) with \( p \coloneqq -(1 + x)/2 < -1 \) and \( q \coloneqq -2x/(1 + x) < -1 \). So the set is \( \{ x \in \nQ : x > 1 \} \). It contains \( 2 \) but not \( 0 < 2 \), so it fails (C2): it is closed upward.

Both failures come from negative elements, and every cut has them. For a cut \( \alpha > D_0 \), the positive elements carry all the information, since the others are exactly the rationals \( p \le 0 \): by @prp-rational-in-cut, \( \alpha > D_0 \) means \( 0 \in \alpha \), so every \( p \le 0 \) is in \( \alpha \) by (C2), and \( \alpha \) has a positive element by (C3). So for positive cuts we multiply positive elements only, then put back everything below.

::: {.warning}
The product of two cuts is **not** the set of products of their elements, even for positive cuts: \( D_1 \) and \( D_1 \) give \( \nQ \), as shown above. Every proof in this section works with the definitions below, never with that set.
:::

## Positive cuts

::: {#def-cut-product-positive}
[Product of Positive Cuts]

Let \( \alpha \) and \( \beta \) be cuts with \( \alpha > D_0 \) and \( \beta > D_0 \) (equivalently, \( 0 \in \alpha \) and \( 0 \in \beta \), by @prp-rational-in-cut). Their **product** is
\[
\begin{aligned}
\alpha\beta \coloneqq \{ p \in \nQ : {}& p \le rs \text{ for some } r \in \alpha \text{ and } s \in \beta \\
& \text{with } r > 0 \text{ and } s > 0 \} .
\end{aligned}
\]
:::

In words: take the products of **positive** elements, and then every rational at or below one of them. The second step is what makes \( \alpha\beta \) closed downward; it also puts every \( p \le 0 \) in \( \alpha\beta \), since positive \( r \in \alpha \) and \( s \in \beta \) exist and \( p \le 0 < rs \). For instance, in \( D_2 D_3 \) every product \( rs \) of positive \( r < 2 \), \( s < 3 \) is below \( 6 \), so \( D_2 D_3 \subseteq D_6 \); Exercise B1 proves equality.

::: {.check}
Let \( \alpha, \beta > D_0 \). Suppose the definition said "\( p = rs \)" instead of "\( p \le rs \)". Which set would it give, and which cut condition would that set fail?
:::

::: {.solution}
It would give the set of products \( rs \) of positive elements, a set of positive rationals. It is non-empty, but it fails (C2): it contains a positive \( rs \) and not \( 0 < rs \).
:::

::: {#prp-cut-product-positive}
[Positive Cuts under Multiplication]

Let \( \alpha \), \( \beta \), \( \gamma \) be cuts with \( \alpha, \beta, \gamma > D_0 \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \alpha\beta \) is a cut, and \( \alpha\beta > D_0 \);
2. \( \alpha\beta = \beta\alpha \);
3. \( (\alpha\beta)\gamma = \alpha(\beta\gamma) \);
4. \( \alpha D_1 = \alpha \).
:::
:::

::: {.idea}
Each cut condition for \( \alpha\beta \) is inherited from \( \alpha \) or \( \beta \), as for sums: an outside point of each factor bounds the products, and moving up in \( \alpha \) moves the product up. The laws (b) and (c) are (F6) and (F5) of \( \nQ \), applied to positive elements. For (d), multiplying by an element of \( D_1 \) pushes down, so one inclusion is (C2); the other writes \( p \) as a larger element of \( \alpha \) times a factor below \( 1 \).
:::

::: {.proof}
Throughout, \( \alpha \), \( \beta \), \( \gamma \) contain \( 0 \) and a positive element (by @prp-rational-in-cut and (C3)), and every element outside one of them is positive (@lem-cut-separation, against \( 0 \)).

(a) (C1): \( 0 \in \alpha\beta \), as noted after the definition. By (C1) there are \( a \notin \alpha \) and \( b \notin \beta \); then \( a, b > 0 \). For positive \( r \in \alpha \), \( s \in \beta \), separation gives \( r < a \) and \( s < b \), so \( rs < as < ab \) by @prp-ordered-ring-rules (c), since \( s > 0 \) and \( a > 0 \). So every \( p \in \alpha\beta \) has \( p \le rs < ab \) for suitable \( r, s \), and \( ab \notin \alpha\beta \). (C2): if \( p \le rs \) and \( q < p \), then \( q \le rs \), with the same \( r, s \). (C3): let \( p \in \alpha\beta \), with \( p \le rs \) for positive \( r \in \alpha \), \( s \in \beta \). By (C3) for \( \alpha \) there is \( r' \in \alpha \) with \( r' > r \); then \( r' > 0 \), so \( r's \in \alpha\beta \), and \( r's > rs \ge p \) by @prp-ordered-ring-rules (c). So \( \alpha\beta \) is a cut, and since \( 0 \in \alpha\beta \), \( \alpha\beta > D_0 \) by @prp-rational-in-cut.

(b) The condition "\( p \le rs \) for some positive \( r \in \alpha \), \( s \in \beta \)" is the same as "\( p \le sr \) for some positive \( s \in \beta \), \( r \in \alpha \)", by (F6) in \( \nQ \). So the two sets are equal.

(c) Let \( T \) be the set of rationals \( p \) with \( p \le rst \) for some positive \( r \in \alpha \), \( s \in \beta \), \( t \in \gamma \). We show \( (\alpha\beta)\gamma = T \). \( (\subseteq) \) Let \( p \le ut \) with \( u \in \alpha\beta \), \( t \in \gamma \) positive. Then \( u \le rs \) for some positive \( r \in \alpha \), \( s \in \beta \), and \( ut \le (rs)t \) since \( t > 0 \); so \( p \le rst \) and \( p \in T \). \( (\supseteq) \) If \( p \le (rs)t \) with \( r, s, t \) as in \( T \), then \( u \coloneqq rs \) is positive and in \( \alpha\beta \) (as \( rs \le rs \)), so \( p \in (\alpha\beta)\gamma \). The same argument, grouping \( r(st) \), gives \( \alpha(\beta\gamma) = T \), using (F5) in \( \nQ \).

(d) \( (\subseteq) \) Let \( p \le rs \) with positive \( r \in \alpha \) and \( s \in D_1 \), so \( 0 < s < 1 \). Then \( rs < r \), so \( p < r \) and \( p \in \alpha \) by (C2). \( (\supseteq) \) Let \( p \in \alpha \). If \( p \le 0 \), then \( p \in \alpha D_1 \) as noted after the definition. If \( p > 0 \), take \( p' \in \alpha \) with \( p' > p \) by (C3). Then \( 0 < p/p' < 1 \), so \( p/p' \in D_1 \) is positive, and \( p = p' \cdot (p/p') \in \alpha D_1 \).
:::

The proof of (d) used (C3) in the same place as the proof that \( \alpha + D_0 = \alpha \) (@prp-cut-sum-zero): to reach \( p \) from inside, one needs an element of \( \alpha \) strictly above it.

The reciprocal will need, as the negative did, a point inside a cut and a point outside that are close. For products "close" means "close in ratio", and the walk up by ε gives that too.

::: {#lem-cut-multiplicative-step}
[The Walk Up, Multiplicatively]

Let \( \alpha \) be a cut with \( \alpha > D_0 \), and let \( \mu \in \nQ \) with \( \mu > 1 \). Then there is \( r \in \alpha \) with \( r > 0 \) and \( \mu r \notin \alpha \).
:::

::: {.idea}
Walk up from a positive point \( a \) in steps of \( \varepsilon \coloneqq (\mu - 1)a \). The last point \( r \) inside is at least \( a \), so the step \( \varepsilon \) is at most \( (\mu - 1)r \), and \( \mu r = r + (\mu - 1)r \) is at least the first point outside.
:::

::: {.proof}
By @prp-rational-in-cut, \( 0 \in \alpha \), and by (C3) there is \( a \in \alpha \) with \( a > 0 \); fix one \( \bigl[ \rulename{\exists E} \bigr] \) (@fd1:def-rules-existential). Let \( \varepsilon \coloneqq (\mu - 1)a \); it is positive, as a product of positives. By @lem-cut-step there is \( n \in \nN \) with \( r \coloneqq a + n\varepsilon \in \alpha \) and \( r + \varepsilon \notin \alpha \). Since \( n\varepsilon \ge 0 \), \( r \ge a > 0 \). Then
\[
\mu r - (r + \varepsilon) = (\mu - 1) r - (\mu - 1) a = (\mu - 1)(r - a) \ge 0 ,
\]
so \( \mu r \ge r + \varepsilon \). As \( r + \varepsilon \notin \alpha \) and the outside of a cut is closed upward (@lem-cut-separation), \( \mu r \notin \alpha \).
:::

The last law for positive cuts is distributivity. The sum \( \beta + \gamma \) of two positive cuts contains \( 0 = 0 + 0 \), since \( 0 \in \beta \) and \( 0 \in \gamma \), so it is positive (both steps by @prp-rational-in-cut (a)), and \( \alpha(\beta + \gamma) \) is defined.

::: {#lem-cut-distributive-positive}
[Distributivity for Positive Cuts]

For all cuts \( \alpha, \beta, \gamma > D_0 \), \( \alpha(\beta + \gamma) = \alpha\beta + \alpha\gamma \).
:::

::: {.idea}
An element of \( \beta + \gamma \) is a sum \( s + t \), and \( r(s + t) = rs + rt \). The only snag is that \( s \) or \( t \) may be negative, and the definition of \( \alpha\beta \) wants positive factors; raising them to positive elements only increases \( r(s + t) \), which is harmless because both sides are closed downward. For the other inclusion, two different first factors \( r_1 \), \( r_2 \) are replaced by the larger.
:::

::: {.proof}
Let \( \alpha, \beta, \gamma > D_0 \). By @thm-cut-sum and @prp-cut-product-positive (a), both sides are cuts.

\( (\subseteq) \) Let \( p \in \alpha(\beta + \gamma) \): \( p \le ru \) for some positive \( r \in \alpha \) and positive \( u \in \beta + \gamma \), and \( u = s + t \) with \( s \in \beta \), \( t \in \gamma \). Let \( \tilde s \coloneqq s \) if \( s > 0 \), and otherwise let \( \tilde s \) be a positive element of \( \beta \) (one exists by (C3), since \( 0 \in \beta \)). Then \( \tilde s \in \beta \), \( \tilde s > 0 \) and \( \tilde s \ge s \). Choose \( \tilde t \in \gamma \) in the same way. Since \( r > 0 \),
\[
p \le r(s + t) = rs + rt \le r\tilde s + r\tilde t ,
\]
and \( r\tilde s \in \alpha\beta \), \( r\tilde t \in \alpha\gamma \). So \( r\tilde s + r\tilde t \in \alpha\beta + \alpha\gamma \), and \( p \) is in that cut, being equal to this element or below it (C2).

\( (\supseteq) \) Let \( x \in \alpha\beta \) and \( y \in \alpha\gamma \): \( x \le r_1 s \) and \( y \le r_2 t \) with positive \( r_1, r_2 \in \alpha \), \( s \in \beta \), \( t \in \gamma \). Let \( r \coloneqq \max\{ r_1, r_2 \} \), one of \( r_1, r_2 \), so \( r \in \alpha \) and \( r > 0 \). Then
\[
x + y \le r_1 s + r_2 t \le rs + rt = r(s + t) ,
\]
and \( s + t \in \beta + \gamma \) is positive. So \( x + y \in \alpha(\beta + \gamma) \).
:::

## Signs

Every cut is positive, zero or negative (@thm-cut-order-total), and a negative cut has a positive negative (@thm-cut-ordered-group (f)). So the product of positive cuts determines all others, as in school: multiply the sizes and fix the sign.

::: {#def-cut-product}
[Absolute Value, Sign and Product of Cuts]

For a cut \( \alpha \), its **absolute value** and **sign** are
\[
\abs{\alpha} \coloneqq
\begin{cases}
\alpha & \text{if } \alpha \ge D_0 , \\
-\alpha & \text{if } \alpha < D_0 ,
\end{cases}
\qquad
\sgn \alpha \coloneqq
\begin{cases}
1 & \text{if } \alpha > D_0 , \\
0 & \text{if } \alpha = D_0 , \\
-1 & \text{if } \alpha < D_0 .
\end{cases}
\]
For cuts \( \alpha \) and \( \beta \), their **product** is
\[
\alpha\beta \coloneqq
\begin{cases}
D_0 & \text{if } \alpha = D_0 \text{ or } \beta = D_0 , \\
\abs{\alpha}\abs{\beta} & \text{if } \sgn \alpha = \sgn \beta \ne 0 , \\
-\bigl( \abs{\alpha}\abs{\beta} \bigr) & \text{if } \sgn \alpha \ne \sgn \beta \text{ and neither is } 0 ,
\end{cases}
\]
where \( \abs{\alpha}\abs{\beta} \) is the product of positive cuts of @def-cut-product-positive.
:::

The cases do not overlap and cover every cut and every pair, by @thm-cut-order-total. For \( \alpha \ne D_0 \), \( \abs{\alpha} > D_0 \) (@thm-cut-ordered-group (f)), so in the last two cases \( \abs{\alpha}\abs{\beta} \) is defined, and it is a cut (@prp-cut-product-positive (a)). So \( \alpha\beta \) is a cut in every case: \( D_0 \), a product of positive cuts, or the negative of one (@def-cut-negative, with the check after it). The product is a function \( \nR_{\mathrm D} \times \nR_{\mathrm D} \to \nR_{\mathrm D} \). The new product agrees with the old one where both are defined: for \( \alpha, \beta > D_0 \) the signs agree, \( \abs{\alpha} = \alpha \), \( \abs{\beta} = \beta \), and the second case returns \( \alpha\beta \) of @def-cut-product-positive. So writing \( \alpha\beta \) for both is safe. The degenerate cases: \( \abs{D_0} = D_0 \), \( \sgn D_0 = 0 \), and \( \alpha D_0 = D_0 \alpha = D_0 \) for every cut \( \alpha \). Two small examples. Since \( -1 < 0 \), \( D_{-1} < D_0 \) (Section 7.2, "Two translations"), so \( \sgn D_{-1} = -1 \) and \( \abs{D_{-1}} = -D_{-1} = D_1 \), because \( p \in -D_{-1} \) exactly when \( -p - r \ge -1 \) for some \( r > 0 \), that is, when \( p < 1 \); and so \( D_{-1}D_{-1} = D_1 D_1 = D_1 \), by @prp-cut-product-positive (d).

::: {.warning}
The absolute value \( \abs{\alpha} \) is defined here before we know that \( \nR_{\mathrm D} \) is an ordered field. Once @thm-cuts-ordered-field below has shown that it is, \( \abs{\alpha} \) is the absolute value of that ordered field in the sense of @def-absolute-value-ordered-field, by the same formula, so the two readings never disagree. Before that theorem, no rule of @prp-absolute-value-ordered-field may be used for cuts; the rules we need are proved in the next lemma.
:::

The next lemma is where the reduction to positive cuts pays off. That reduction is the last of the chapter's named moves.

*Reduce to the positive case: define and prove for positive cuts, then extend to all cuts by signs once, through one lemma, never axiom by axiom.*

The lemma is proved once, by the definition's cases, and the later sign laws (distributivity, the reciprocal of a negative cut, the field axioms in @thm-cuts-ordered-field) cite it instead of repeating the case analysis.

::: {#lem-cut-sign-rules}
[Sign Rules for Cuts]

For all cuts \( \alpha \), \( \beta \), \( \gamma \):

::: {.enumerate options="label=(\alph*)"}
1. \( \alpha = \sgn(\alpha)\abs{\alpha} \), reading \( 1 \cdot \xi \coloneqq \xi \), \( 0 \cdot \xi \coloneqq D_0 \) and \( (-1) \cdot \xi \coloneqq -\xi \); so two cuts with the same sign and the same absolute value are equal;
2. \( \abs{\alpha\beta} = \abs{\alpha}\abs{\beta} \) and \( \sgn(\alpha\beta) = \sgn\alpha \, \sgn\beta \);
3. \( \abs{-\alpha} = \abs{\alpha} \) and \( \sgn(-\alpha) = -\sgn\alpha \);
4. \( (-\alpha)\beta = -(\alpha\beta) = \alpha(-\beta) \);
5. \( \alpha\beta = \beta\alpha \);
6. \( (\alpha\beta)\gamma = \alpha(\beta\gamma) \);
7. \( \alpha D_1 = \alpha \).
:::
:::

*In words: a cut is its sign times its size; sizes multiply as positive cuts do, and signs multiply as the integers \( -1, 0, 1 \) do.*

::: {.idea}
Clause (a) says a cut is determined by two pieces of data, its sign and its absolute value. Clauses (b) and (c) compute both pieces for a product and a negative. After that, each of (d)–(g) is an equation between two cuts whose signs and absolute values are visibly equal: the signs by arithmetic in \( \{ -1, 0, 1 \} \), the absolute values by @prp-cut-product-positive once a factor \( D_0 \) is set aside. No axiom is checked over the sign combinations.
:::

::: {.proof}
We use @thm-cut-ordered-group (e), (f) freely: \( -(-\xi) = \xi \), \( -D_0 = D_0 \), and \( \xi > D_0 \iff -\xi < D_0 \).

(a) If \( \alpha > D_0 \), then \( \sgn(\alpha)\abs{\alpha} = 1 \cdot \alpha = \alpha \). If \( \alpha = D_0 \), it is \( 0 \cdot D_0 = D_0 \). If \( \alpha < D_0 \), it is \( (-1) \cdot (-\alpha) = -(-\alpha) = \alpha \). So two cuts with equal signs and equal absolute values are both equal to \( \sgn(\alpha)\abs{\alpha} \).

(b) If \( \alpha = D_0 \) or \( \beta = D_0 \), then \( \alpha\beta = D_0 \), so \( \abs{\alpha\beta} = D_0 \) and \( \sgn(\alpha\beta) = 0 \); and \( \abs{\alpha}\abs{\beta} = D_0 \), since one factor is \( \abs{D_0} = D_0 \), and \( \sgn\alpha \, \sgn\beta = 0 \). Otherwise let \( \pi \coloneqq \abs{\alpha}\abs{\beta} \), a product of positive cuts, so \( \pi > D_0 \) by @prp-cut-product-positive (a). If the signs agree, \( \alpha\beta = \pi \), with absolute value \( \pi \) and sign \( 1 = \sgn\alpha \, \sgn\beta \). If they differ, \( \alpha\beta = -\pi < D_0 \), with absolute value \( -(-\pi) = \pi \) and sign \( -1 = \sgn\alpha \, \sgn\beta \).

(c) If \( \alpha > D_0 \), then \( -\alpha < D_0 \), so \( \abs{-\alpha} = -(-\alpha) = \alpha = \abs{\alpha} \), and the signs are \( -1 \) and \( 1 \). If \( \alpha = D_0 \), then \( -\alpha = D_0 \). If \( \alpha < D_0 \), then \( -\alpha > D_0 \), so \( \abs{-\alpha} = -\alpha = \abs{\alpha} \), and the signs are \( 1 \) and \( -1 \).

(d) By (b) and (c), \( (-\alpha)\beta \) has absolute value \( \abs{-\alpha}\abs{\beta} = \abs{\alpha}\abs{\beta} \) and sign \( -\sgn\alpha \, \sgn\beta \). By (c) and (b), \( -(\alpha\beta) \) has absolute value \( \abs{\alpha\beta} = \abs{\alpha}\abs{\beta} \) and sign \( -\sgn(\alpha\beta) = -\sgn\alpha \, \sgn\beta \). By (a) they are equal. The same computation, with \( \beta \) negated instead of \( \alpha \), gives \( \alpha(-\beta) = -(\alpha\beta) \).

(e) The signs of \( \alpha\beta \) and \( \beta\alpha \) are \( \sgn\alpha \, \sgn\beta = \sgn\beta \, \sgn\alpha \). Their absolute values are \( \abs{\alpha}\abs{\beta} \) and \( \abs{\beta}\abs{\alpha} \), by (b): both are \( D_0 \) if \( \alpha \) or \( \beta \) is \( D_0 \), and otherwise they are equal by @prp-cut-product-positive (b). By (a), \( \alpha\beta = \beta\alpha \).

(f) By (b), twice, the absolute values of the two sides are \( \bigl( \abs{\alpha}\abs{\beta} \bigr)\abs{\gamma} \) and \( \abs{\alpha}\bigl( \abs{\beta}\abs{\gamma} \bigr) \). If one of \( \alpha, \beta, \gamma \) is \( D_0 \), both are \( D_0 \), since a product with a factor \( D_0 \) is \( D_0 \); otherwise they are equal by @prp-cut-product-positive (c). The signs are \( (\sgn\alpha \, \sgn\beta)\sgn\gamma = \sgn\alpha \, (\sgn\beta \, \sgn\gamma) \). By (a), the two sides are equal.

(g) \( D_1 > D_0 \), since \( 0 \in D_1 \) (@prp-rational-in-cut), so \( \abs{D_1} = D_1 \) and \( \sgn D_1 = 1 \). By (b), \( \alpha D_1 \) has sign \( \sgn\alpha \) and absolute value \( \abs{\alpha}D_1 \), which is \( D_0 = \abs{\alpha} \) if \( \alpha = D_0 \), and \( \abs{\alpha} \) by @prp-cut-product-positive (d) otherwise. By (a), \( \alpha D_1 = \alpha \).
:::

::: {.check}
Compute \( D_{-2} \cdot D_3 \) through the cases of @def-cut-product. Which case applies, and what are \( \abs{D_{-2}} \) and \( \sgn D_{-2} \)? Express the product through \( D_2 D_3 \).
:::

::: {.solution}
Since \( 0 \notin D_{-2} \), \( D_{-2} > D_0 \) fails (@prp-rational-in-cut), and \( D_{-2} \ne D_0 \) (as \( -1 \in D_0 \setminus D_{-2} \)); so \( D_{-2} < D_0 \) and \( \sgn D_{-2} = -1 \), while \( \sgn D_3 = 1 \) (\( 0 \in D_3 \)). The signs differ, so the third case applies: \( D_{-2} D_3 = -\bigl( \abs{D_{-2}} \, \abs{D_3} \bigr) \). Here \( \abs{D_{-2}} = -D_{-2} = D_2 \), since \( p \in -D_{-2} \) exactly when \( -p - r \ge -2 \) for some \( r > 0 \), that is, when \( p < 2 \); and \( \abs{D_3} = D_3 \). So \( D_{-2} D_3 = -(D_2 D_3) \). Since \( D_2 D_3 = D_6 \) (Exercise B1) and \( -D_6 = D_{-6} \) (by the same computation), the product is \( D_{-6} \), as \( (-2) \cdot 3 = -6 \) suggests. Section 7.5 proves \( D_p D_q = D_{pq} \) for all rationals.
:::

Distributivity for all cuts is the one law where the reduction to positive cuts needs an idea, because \( \beta + \gamma \) may have a sign different from both \( \beta \) and \( \gamma \). The device is to move the negative summand to the other side, where it becomes positive.

::: {#lem-cut-distributive}
[Distributivity for All Cuts]

For all cuts \( \alpha \), \( \beta \), \( \gamma \), \( \alpha(\beta + \gamma) = \alpha\beta + \alpha\gamma \).
:::

::: {.idea}
Fix \( \alpha > D_0 \) and write \( f(\xi) \coloneqq \alpha\xi \). We know two things about \( f \): it is additive on cuts \( > D_0 \) (@lem-cut-distributive-positive), and trivially when one summand is \( D_0 \), and it commutes with negation (@lem-cut-sign-rules (d)). If \( \beta \) and \( \gamma \) have the same sign, negate both if necessary. If \( \beta \ge D_0 \ge \gamma \), one of \( \beta \) and \( -\gamma \) is a sum of two cuts \( \ge D_0 \): \( \beta = (\beta + \gamma) + (-\gamma) \) when \( \beta + \gamma \ge D_0 \), and \( -\gamma = \bigl( -(\beta + \gamma) \bigr) + \beta \) otherwise. Apply additivity to that sum and solve for \( f(\beta + \gamma) \). For \( \alpha < D_0 \), pull the sign out of \( \alpha \).

*Before reading on: which case uses that \( -\gamma \ge D_0 \)?*
:::

::: {.proof}
Throughout we use @thm-cut-ordered-group and @lem-cut-sign-rules (d) as in the Idea. If \( \alpha = D_0 \), both sides are \( D_0 \) (@def-cut-product, @prp-cut-sum-zero).

Let \( \alpha > D_0 \) and \( f(\xi) \coloneqq \alpha\xi \) for every cut \( \xi \). Two facts:

- (A) \( f(\xi + \eta) = f(\xi) + f(\eta) \) whenever \( \xi, \eta \ge D_0 \). If \( \xi, \eta > D_0 \), this is @lem-cut-distributive-positive. If \( \xi = D_0 \), both sides are \( f(\eta) \), since \( f(D_0) = D_0 \) and \( D_0 + \eta = \eta \); likewise if \( \eta = D_0 \).
- (N) \( f(-\xi) = -f(\xi) \) for every cut \( \xi \), by @lem-cut-sign-rules (d).

By totality (@thm-cut-order-total), each of \( \beta \) and \( \gamma \) is \( \ge D_0 \) or \( \le D_0 \), so one of the following cases applies.

*Case 1: \( \beta, \gamma \ge D_0 \).* This is (A).

*Case 2: \( \beta, \gamma \le D_0 \).* Then \( -\beta, -\gamma \ge D_0 \) (@thm-cut-ordered-group (f)), and \( -(\beta + \gamma) = (-\beta) + (-\gamma) \) (@thm-cut-ordered-group (e)). By (N), (A) and (N),
\[
\begin{aligned}
f(\beta + \gamma) &= -f\bigl( (-\beta) + (-\gamma) \bigr) = -\bigl( f(-\beta) + f(-\gamma) \bigr) \\
&= -\bigl( (-f(\beta)) + (-f(\gamma)) \bigr) = f(\beta) + f(\gamma) ,
\end{aligned}
\]
where the last step is @thm-cut-ordered-group (e) twice.

*Case 3: \( \beta \ge D_0 \ge \gamma \) and \( \beta + \gamma \ge D_0 \).* Then \( \beta = (\beta + \gamma) + (-\gamma) \), with both summands \( \ge D_0 \). By (A) and (N), \( f(\beta) = f(\beta + \gamma) + f(-\gamma) = f(\beta + \gamma) + (-f(\gamma)) \). Adding \( f(\gamma) \) to both sides gives \( f(\beta) + f(\gamma) = f(\beta + \gamma) \).

*Case 4: \( \beta \ge D_0 \ge \gamma \) and \( \beta + \gamma < D_0 \).* Then \( -\gamma = \bigl( -(\beta + \gamma) \bigr) + \beta \), since \( -(\beta + \gamma) + \beta = (-\beta) + (-\gamma) + \beta = -\gamma \); both summands are \( \ge D_0 \). By (N) and (A), \( -f(\gamma) = -f(\beta + \gamma) + f(\beta) \). Adding \( f(\beta + \gamma) + f(\gamma) \) to both sides gives \( f(\beta + \gamma) = f(\beta) + f(\gamma) \).

*Case 5: \( \gamma \ge D_0 \ge \beta \).* Exchange \( \beta \) and \( \gamma \) in Cases 3 and 4; both sides of the claim are symmetric in \( \beta \) and \( \gamma \) (@thm-cut-ordered-group (a)).

This proves the lemma for \( \alpha > D_0 \). Let \( \alpha < D_0 \). Then \( -\alpha > D_0 \), and by @lem-cut-sign-rules (d), \( \alpha\xi = -\bigl( (-\alpha)\xi \bigr) \) for every cut \( \xi \). So, by the case just proved (applied to \( -\alpha \)),
\[
\begin{aligned}
\alpha(\beta + \gamma) &= -\bigl( (-\alpha)(\beta + \gamma) \bigr) = -\bigl( (-\alpha)\beta + (-\alpha)\gamma \bigr) \\
&= \bigl( -\bigl( (-\alpha)\beta \bigr) \bigr) + \bigl( -\bigl( (-\alpha)\gamma \bigr) \bigr) = \alpha\beta + \alpha\gamma ,
\end{aligned}
\]
where the third equality is @thm-cut-ordered-group (e).
:::

The answer to the prompt. Case 3 uses \( -\gamma \ge D_0 \) to apply (A) to \( (\beta + \gamma) + (-\gamma) \), and Case 2 uses it, with \( -\beta \ge D_0 \), to apply (A) to \( (-\beta) + (-\gamma) \). Case 4 does not: there \( -\gamma \) is the sum, and the summands are \( -(\beta + \gamma) \) and \( \beta \).

## Reciprocals

For the reciprocal we repeat the idea of the negative, with division in place of subtraction. For \( \alpha > D_0 \), the reciprocal should consist of the rationals \( p \le 0 \) together with the positive rationals below \( 1/q \) for some rational \( q \) outside \( \alpha \). The analogue of the margin is a **strict** inequality.

*The reciprocal of a positive cut: the non-positive rationals, and the positive rationals strictly below the reciprocal of some point outside.*

::: {#def-cut-reciprocal}
[Reciprocal of a Cut]

Let \( \alpha \) be a cut. If \( \alpha > D_0 \), its **reciprocal** is the set
\[
\begin{aligned}
\alpha^{-1} \coloneqq {}& \{ p \in \nQ : p \le 0 \} \\
{}\cup{}& \{ p \in \nQ : p > 0 \text{ and } pq < 1 \text{ for some } q \in \nQ \setminus \alpha \} .
\end{aligned}
\]
If \( \alpha < D_0 \), its reciprocal is \( \alpha^{-1} \coloneqq -\bigl( (-\alpha)^{-1} \bigr) \). The cut \( D_0 \) has no reciprocal. The quantifier in the set for \( \alpha > D_0 \) is **some**: one point \( q \) outside \( \alpha \) suffices, and it may depend on \( p \).
:::

Every \( q \notin \alpha \) is positive when \( \alpha > D_0 \) (@lem-cut-separation against \( 0 \in \alpha \)), so for \( p > 0 \) the condition \( pq < 1 \) says \( p < 1/q \). For \( \alpha < D_0 \), the cut \( -\alpha \) is positive (@thm-cut-ordered-group (f)), so the definition for \( \alpha < D_0 \) refers to the one for \( \alpha > D_0 \).

**Example.** \( D_2^{-1} = D_{1/2} \). The outside of \( D_2 \) is \( \{ q : q \ge 2 \} \). A positive \( p < 1/2 \) is in \( D_2^{-1} \), with \( q = 2 \): \( 2p < 1 \). A positive \( p \ge 1/2 \) is not, since every \( q \ge 2 \) gives \( pq \ge 1 \). With the non-positive rationals, \( D_2^{-1} = \{ p : p < 1/2 \} \).

**A non-example by minimal change.** Replace "\( pq < 1 \)" by "\( pq \le 1 \)". For \( D_2 \) the set becomes \( \{ p : p \le 1/2 \} \), which has a largest element. This is the multiplicative mirror of @exm-naive-negative, and Exercise C1 shows that, as there, it fails exactly for the rational cuts.

::: {#thm-cut-reciprocal}
[Reciprocals of Cuts]

Let \( \alpha \) be a cut with \( \alpha \ne D_0 \). Then \( \alpha^{-1} \) is a cut, \( \alpha^{-1} > D_0 \) if \( \alpha > D_0 \), \( \alpha^{-1} < D_0 \) if \( \alpha < D_0 \), and
\[
\alpha \alpha^{-1} = D_1 .
\]
:::

::: {.idea}
For \( \alpha > D_0 \), the cut conditions are checked as for the negative; the strict inequality \( pq < 1 \) leaves room above \( p \), as the margin did. The inclusion \( \alpha\alpha^{-1} \subseteq D_1 \) is separation: \( r < q \) for \( r \in \alpha \), \( q \notin \alpha \), so \( rs < qs < 1 \).

For \( \supseteq \), work backwards. Given \( 0 < p < 1 \), we want positive \( r \in \alpha \) and \( s \in \alpha^{-1} \) with \( rs = p \). So \( s = p/r \), and "\( s \in \alpha^{-1} \)" asks for some \( q \notin \alpha \) with \( (p/r) q < 1 \), that is, \( q < r/p \). So we need **a point \( r \) inside and a point outside below \( r/p \)**: a point inside and a point outside whose **ratio** is less than \( 1/p \). The multiplicative walk (@lem-cut-multiplicative-step) supplies the ratio \( \mu \), and \( \mu \) must be chosen strictly between \( 1 \) and \( 1/p \), for the same reason that \( \varepsilon \) was \( -s/2 \) and not \( -s \): we take the midpoint \( \mu \coloneqq (1 + 1/p)/2 \). For \( \alpha < D_0 \), the sign rules move everything to \( -\alpha \).
:::

Exercise B2 asks for the last step of the proof; the fold below has the proof in full.

::: {.second-reading title="The proof of the reciprocal theorem (try Exercise B2 first)"}
::: {.proof}
*Let \( \alpha > D_0 \).* Then \( 0 \in \alpha \) (@prp-rational-in-cut), so every \( q \notin \alpha \) is positive (@lem-cut-separation), and \( \alpha \) has a positive element (C3).

(C1) \( 0 \in \alpha^{-1} \). Let \( a \in \alpha \) with \( a > 0 \). Then \( 1/a \notin \alpha^{-1} \): it is positive, and every \( q \notin \alpha \) has \( q > a \) (@lem-cut-separation), so \( (1/a) q > (1/a) a = 1 \).

(C2) Let \( p \in \alpha^{-1} \) and \( p' < p \). If \( p' \le 0 \), then \( p' \in \alpha^{-1} \). Otherwise \( 0 < p' < p \), so \( p > 0 \) and \( pq < 1 \) for some \( q \notin \alpha \); as \( q > 0 \), \( p'q < pq < 1 \), and \( p' \in \alpha^{-1} \) with the same \( q \).

(C3) Let \( p \in \alpha^{-1} \). If \( p \le 0 \), take any \( q \notin \alpha \) (C1); then \( 1/(2q) > 0 \ge p \), and \( \bigl( 1/(2q) \bigr) q = 1/2 < 1 \), so \( 1/(2q) \in \alpha^{-1} \). If \( p > 0 \) with \( pq < 1 \), \( q \notin \alpha \), then \( p < 1/q \); the midpoint \( p'' \coloneqq (p + 1/q)/2 \) has \( p < p'' < 1/q \) (@prp-ordered-field-halves (b)), so \( p'' > 0 \) and \( p'' q < 1 \), and \( p'' \in \alpha^{-1} \).

So \( \alpha^{-1} \) is a cut, and \( \alpha^{-1} > D_0 \) because \( 0 \in \alpha^{-1} \) (@prp-rational-in-cut). The product \( \alpha\alpha^{-1} \) is therefore given by @def-cut-product-positive.

\( (\subseteq) \) Let \( x \in \alpha\alpha^{-1} \): \( x \le rs \) with positive \( r \in \alpha \) and \( s \in \alpha^{-1} \), and \( sq < 1 \) for some \( q \notin \alpha \). By @lem-cut-separation, \( r < q \), so \( rs < qs < 1 \) since \( s > 0 \). Hence \( x < 1 \) and \( x \in D_1 \).

\( (\supseteq) \) Let \( p \in D_1 \), so \( p < 1 \). If \( p \le 0 \), then \( p \in \alpha\alpha^{-1} \), since positive elements of \( \alpha \) and of \( \alpha^{-1} \) exist and their product is above \( p \). Let \( 0 < p < 1 \), and put
\[
\mu \coloneqq \frac{1}{2} \Bigl( 1 + \frac{1}{p} \Bigr) ;
\]
it depends only on \( p \). Since \( 1/p > 1 \) (@prp-reciprocal-order (b)), \( \mu \) is the midpoint of \( 1 < 1/p \), so \( 1 < \mu < 1/p \). By @lem-cut-multiplicative-step there is \( r \in \alpha \) with \( r > 0 \) and \( \mu r \notin \alpha \); fix one \( \bigl[ \rulename{\exists E} \bigr] \). Put \( s \coloneqq p/r > 0 \). Then
\[
s \cdot (\mu r) = p\mu < p \cdot \frac{1}{p} = 1 ,
\]
and \( \mu r \notin \alpha \), so \( s \in \alpha^{-1} \) \( \bigl[ \rulename{\exists I} \bigr] \) (@fd1:def-rule-existential-introduction), with witness \( q \coloneqq \mu r \). Since \( p = rs \le rs \), \( p \in \alpha\alpha^{-1} \) \( \bigl[ \rulename{\exists I} \bigr] \). As \( p \) was arbitrary, \( D_1 \subseteq \alpha\alpha^{-1} \) \( \bigl[ \rulename{\forall I} \bigr] \) (@fd1:def-rules-universal).

*Let \( \alpha < D_0 \).* Then \( -\alpha > D_0 \), so by the first part \( \beta \coloneqq (-\alpha)^{-1} \) is a cut with \( \beta > D_0 \) and \( (-\alpha)\beta = D_1 \). Then \( \alpha^{-1} = -\beta \) is a cut (@def-cut-negative), and \( -\beta < D_0 \) (@thm-cut-ordered-group (f)). By @lem-cut-sign-rules (d), used twice,
\[
\alpha\alpha^{-1} = \alpha(-\beta) = -(\alpha\beta) = (-\alpha)\beta = D_1 .
\]
:::
:::

The walk up by ε has now produced both inverses: the additive one through @lem-cut-step directly, the multiplicative one through its multiplicative form. No other law of this section constructs a point by walking up.

## The cuts form an ordered field

::: {#thm-cuts-ordered-field}
[The Cuts Form an Ordered Field]

With the addition of @def-cut-sum, the multiplication of @def-cut-product and the order of @def-cut-order, \( \nR_{\mathrm D} \) is an ordered field (@def-ordered-ring-and-field), with zero \( D_0 \) and one \( D_1 \).
:::

::: {.proof}
Let \( \alpha, \beta, \gamma \) be cuts. Both operations map \( \nR_{\mathrm D} \times \nR_{\mathrm D} \) into \( \nR_{\mathrm D} \): sums by @thm-cut-sum, products as noted after @def-cut-product. The table names, for each clause of @def-commutative-ring-and-field and @def-ordered-ring-and-field, the line that proves it.

| Clause | Statement for cuts | Proved by |
|---|---|---|
| (F1), (F2) | \( + \) commutative, associative | @thm-cut-sum |
| (F3) | \( \alpha + D_0 = \alpha \) | @prp-cut-sum-zero |
| (F4) | \( \alpha + (-\alpha) = D_0 \) | @thm-cut-additive-inverse |
| (F5) | \( (\alpha\beta)\gamma = \alpha(\beta\gamma) \) | @lem-cut-sign-rules (f) |
| (F6) | \( \alpha\beta = \beta\alpha \) | @lem-cut-sign-rules (e) |
| (F7) | \( \alpha D_1 = \alpha \) | @lem-cut-sign-rules (g) |
| (F8) | \( \alpha\alpha^{-1} = D_1 \) for \( \alpha \ne D_0 \) | @thm-cut-reciprocal |
| (F9) | \( \alpha(\beta + \gamma) = \alpha\beta + \alpha\gamma \) | @lem-cut-distributive |
| \( 1 \ne 0 \) | \( D_1 \ne D_0 \) | \( 0 \in D_1 \setminus D_0 \) |
| (O1) | exactly one of \( \alpha < \beta \), \( \alpha = \beta \), \( \beta < \alpha \) | @thm-cut-order-total |
| (O2) | \( \alpha < \beta < \gamma \Rightarrow \alpha < \gamma \) | below |
| (O3) | \( \alpha < \beta \Rightarrow \alpha + \gamma < \beta + \gamma \) | @thm-cut-ordered-group (d) |
| (O4) | \( D_0 < \alpha, \beta \Rightarrow D_0 < \alpha\beta \) | @prp-cut-product-positive (a) |

For (O2): if \( \alpha \subsetneq \beta \subsetneq \gamma \), then \( \alpha \subseteq \gamma \) (@fd2:prp-subset-transitive), and \( \alpha = \gamma \) would give \( \beta \subseteq \gamma = \alpha \subseteq \beta \), so \( \alpha = \beta \) (@fd2:prp-subset-antisymmetric), against \( \alpha < \beta \). For (O4): for \( \alpha, \beta > D_0 \) the product of @def-cut-product is that of @def-cut-product-positive, as noted after the definition. Every clause is covered, so \( \nR_{\mathrm D} \) is an ordered field.
:::

Nothing in the table is left to an exercise. Two rows are proved by walking up: (F4), through @lem-cut-step, and (F8), through @lem-cut-multiplicative-step. Several others, such as (O3), (F5)–(F7) and (F9), lean on (F4) through the cancellation law and \( -(-\alpha) = \alpha \) of @thm-cut-ordered-group (e). The order rows cost almost nothing, because the order is inclusion; on the Cauchy road of Chapter 5 the order took a section of its own. Section 7.5 puts \( \nQ \) inside \( \nR_{\mathrm D} \) and adds completeness, and Section 7.6 compares the result with Chapter 5's field.

## Exercises

### A. Check your understanding

::: {#exr-multiplication-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Why is the set \( \{ pq : p \in \alpha, \ q \in \beta \} \) useless as a product for \( \alpha = \beta = D_1 \)?
2. In the table of the proof of @thm-cuts-ordered-field, which rows are proved by a lemma that walks up through a cut, @lem-cut-step or @lem-cut-multiplicative-step? Which further rows depend on such a row?
3. Compute \( \abs{D_{-1}} \), \( \sgn D_{-1} \), \( \abs{D_{1/2}} \), \( \sgn D_{1/2} \) and \( D_{-1} D_{1/2} \) from the definitions.
4. True or false: if \( \alpha > D_0 \), then \( \alpha^{-1} \) contains every negative rational. Give a reason.
:::
:::

::: {.solution}
(a) It is all of \( \nQ \), so it fails (C1): \( x > 0 \) is \( (-1)(-x) \), \( 0 = 0 \cdot 0 \), and \( x < 0 \) is \( (1/2)(2x) \), with every factor in \( D_1 \).

(b) (F4), the additive inverse: @thm-cut-additive-inverse uses @lem-cut-step. (F8), the multiplicative inverse: @thm-cut-reciprocal uses @lem-cut-multiplicative-step, whose proof uses @lem-cut-step. Further rows depend on (F4): the strict form of (O3) uses cancellation, and (F5)–(F7) and (F9) use @lem-cut-sign-rules and @lem-cut-distributive, which use \( -(-\alpha) = \alpha \), cancellation, or both (@thm-cut-ordered-group (e)), all proved from \( \alpha + (-\alpha) = D_0 \). The rows (F1)–(F3), \( 1 \ne 0 \), (O1), (O2) and (O4) use neither lemma.

(c) \( D_{-1} < D_0 \): \( D_{-1} > D_0 \) fails since \( 0 \notin D_{-1} \), and \( D_{-1} \ne D_0 \) since \( -1/2 \in D_0 \setminus D_{-1} \). So \( \sgn D_{-1} = -1 \) and \( \abs{D_{-1}} = -D_{-1} = D_1 \) (@exr-addition-b1 with \( q = -1 \)). Since \( 0 \in D_{1/2} \), \( D_{1/2} > D_0 \), so \( \sgn D_{1/2} = 1 \) and \( \abs{D_{1/2}} = D_{1/2} \). The signs differ, so
\[
D_{-1} D_{1/2} = -\bigl( D_1 D_{1/2} \bigr) = -\bigl( D_{1/2} D_1 \bigr) = -D_{1/2} = D_{-1/2} ,
\]
by @prp-cut-product-positive (b) and (d), and @exr-addition-b1 with \( q = 1/2 \).

(d) True: by @def-cut-reciprocal, \( \alpha^{-1} \) contains every \( p \le 0 \), with no condition.
:::

### B. Practice

::: {#exr-multiplication-b1}
[B1]

Prove from @def-cut-product-positive that \( D_2 D_3 = D_6 \).

*Hint: for \( 0 < x < 6 \), scale \( 2 \) and \( 3 \) down by suitable factors.*
:::

::: {.solution}
\( D_2, D_3 > D_0 \), since \( 0 \in D_2 \) and \( 0 \in D_3 \).

\( (\subseteq) \) Let \( p \le rs \) with \( 0 < r < 2 \), \( 0 < s < 3 \). Then \( rs < 2s < 6 \) (@prp-ordered-ring-rules (c), twice), so \( p < 6 \).

\( (\supseteq) \) Let \( x < 6 \). If \( x \le 0 \), then \( x \le 1 \cdot 1 \) with \( 1 \in D_2 \) and \( 1 \in D_3 \). Let \( 0 < x < 6 \), and put
\[
\lambda \coloneqq \frac{1}{2} \Bigl( 1 + \frac{x}{6} \Bigr) , \qquad r \coloneqq 2\lambda , \qquad s \coloneqq \frac{x}{2\lambda} .
\]
Since \( 0 < x/6 < 1 \), \( \lambda \) is the midpoint of \( x/6 < 1 \), so \( x/6 < \lambda < 1 \). Hence \( 0 < r < 2 \), so \( r \in D_2 \). Also \( s > 0 \), and \( s < 3 \) because \( x < 6\lambda \); so \( s \in D_3 \). Finally \( rs = x \), so \( x \in D_2 D_3 \). Hence \( D_2 D_3 = D_6 \).
:::

::: {#exr-multiplication-b2}
[B2: The last step of the reciprocal]

Let \( \alpha \) be a cut with \( \alpha > D_0 \), and let \( p \in \nQ \) with \( 0 < p < 1 \). We show that \( p \in \alpha\alpha^{-1} \).

::: {.enumerate options="label=(\arabic*)"}
1. Let \( \mu \coloneqq (1 + 1/p)/2 \). Since \( 1/p > 1 \), \( \mu \) is the midpoint of \( 1 \) and \( 1/p \), so \( 1 < \mu < 1/p \).
2. By @lem-cut-multiplicative-step there is \( r \in \alpha \) with \( r > 0 \) and \( \mu r \notin \alpha \).
3. Hence \( p \in \alpha\alpha^{-1} \).
:::

*Name the move, then complete it:* write out step (3).
:::

::: {.solution}
The move is the **walk up by ε**, in its multiplicative form: step (2) walks up through \( \alpha \) until the next point is outside, which gives a point inside and a point outside whose ratio is \( \mu \), less than \( 1/p \).

(3) Put \( s \coloneqq p/r \); it is positive. Then
\[
s \cdot (\mu r) = p\mu < p \cdot \frac{1}{p} = 1 ,
\]
using \( \mu < 1/p \) and \( p > 0 \). Since \( \mu r \notin \alpha \), the rational \( q \coloneqq \mu r \) witnesses \( s \in \alpha^{-1} \) (@def-cut-reciprocal). Now \( r \in \alpha \) and \( s \in \alpha^{-1} \) are positive and \( p = rs \le rs \), so \( p \in \alpha\alpha^{-1} \) by @def-cut-product-positive.

Why \( \mu \) and not \( 1/p \) itself: with \( \mu = 1/p \), step (2) gives \( r \) with \( r/p \notin \alpha \), and \( s = p/r \) would need some \( q \notin \alpha \) with \( (p/r) q < 1 \), that is, \( q < r/p \). The point \( r/p \) itself does not qualify, and there may be no smaller one outside. The strict room between \( \mu \) and \( 1/p \) plays the part of the margin.
:::

::: {#exr-multiplication-b3}
[B3]

Prove that \( (-\alpha)(-\beta) = \alpha\beta \) for all cuts \( \alpha \) and \( \beta \).
:::

::: {.solution}
By @lem-cut-sign-rules (d), applied first with \( -\alpha \) in front and then to \( \alpha(-\beta) \),
\[
(-\alpha)(-\beta) = -\bigl( \alpha(-\beta) \bigr) = -\bigl( -(\alpha\beta) \bigr) = \alpha\beta ,
\]
where the last step is \( -(-\xi) = \xi \) (@thm-cut-ordered-group (e)) with \( \xi = \alpha\beta \).
:::

### C. Going deeper

::: {#exr-multiplication-c1}
[C1: The reciprocal without strictness]

For a cut \( \alpha > D_0 \), let
\[
\begin{aligned}
\rho(\alpha) \coloneqq {}& \{ p \in \nQ : p \le 0 \} \\
{}\cup{}& \{ p \in \nQ : p > 0 \text{ and } pq \le 1 \text{ for some } q \in \nQ \setminus \alpha \} .
\end{aligned}
\]
Prove that \( \rho(\alpha) \) is a cut if and only if \( \alpha \) is not a rational cut, that is, \( \alpha \ne D_a \) for every \( a \in \nQ \).
:::

::: {.solution}
[Hint 1]

Compute \( \rho(D_a) \) first. Which element of the outside of \( D_a \) does all the work?
:::

::: {.solution}
[Hint 2]

If \( \alpha \) is not rational, the outside \( \nQ \setminus \alpha \) has no least element: a least element \( m \) would force \( \alpha = D_m \).
:::

::: {.solution}
Let \( \alpha > D_0 \). Then \( 0 \in \alpha \), every \( q \notin \alpha \) is positive (@lem-cut-separation), and \( \alpha \) has a positive element.

*If \( \alpha = D_a \), then \( \rho(\alpha) \) is not a cut.* Here \( a > 0 \), since \( 0 \in D_a \), and the outside is \( \{ q : q \ge a \} \). For \( p > 0 \): if \( pq \le 1 \) with \( q \ge a \), then \( pa \le pq \le 1 \); conversely \( pa \le 1 \) gives the witness \( q = a \). So \( \rho(D_a) = \{ p : p \le 0 \} \cup \{ p > 0 : p \le 1/a \} = \{ p : p \le 1/a \} \). It has the largest element \( 1/a \), so (C3) fails.

*If \( \alpha \) is not rational, then \( \rho(\alpha) \) is a cut.* First, \( \nQ \setminus \alpha \) has no least element. Suppose \( m \) were one. Every \( r < m \) is then in \( \alpha \) (otherwise \( r \) is a smaller element of the outside), and every \( r \in \alpha \) has \( r < m \) (@lem-cut-separation). So \( \alpha = D_m \), against the hypothesis.

(C1) \( 0 \in \rho(\alpha) \). For a positive \( a \in \alpha \), \( 1/a \notin \rho(\alpha) \): every \( q \notin \alpha \) has \( q > a \), so \( (1/a) q > 1 \).

(C2) As for \( \alpha^{-1} \): if \( 0 < p' < p \) and \( pq \le 1 \) with \( q > 0 \), then \( p'q < pq \le 1 \); and every \( p' \le 0 \) is in \( \rho(\alpha) \).

(C3) If \( p \le 0 \), then for any \( q \notin \alpha \), \( 1/(2q) \) is in \( \rho(\alpha) \) and larger. Let \( p > 0 \) with \( pq \le 1 \), \( q \notin \alpha \). Since \( q \) is not least in the outside, there is \( q' \notin \alpha \) with \( q' < q \); then \( q' > 0 \) and \( pq' < pq \le 1 \), so \( p < 1/q' \). The midpoint \( p'' \coloneqq (p + 1/q')/2 \) has \( p < p'' < 1/q' \), so \( p'' q' < 1 \), and \( p'' \in \rho(\alpha) \) is larger than \( p \).

So \( \rho(\alpha) \) is a cut exactly when \( \alpha \) is not rational. For such \( \alpha \), \( \rho(\alpha) = \alpha^{-1} \): the argument for (C3) shows that \( pq \le 1 \) with \( q \notin \alpha \) gives \( pq' < 1 \) with \( q' \notin \alpha \), and the converse is immediate. As with the negatives of the outside in Section 7.3, the non-strict recipe works for the cut \( \sigma \) of @exm-cut-sqrt2, which is not a rational cut (Exercise C1 of Section 7.1), and fails on the simplest cuts; the strict inequality in @def-cut-reciprocal is the multiplicative margin.

**Marking scheme.** (10 points)
- 3: shows that \( \rho(D_a) \) has the largest element \( 1/a \) (\( 1/a \in \rho(D_a) \) and every element is \( \le 1/a \); the full equality \( \rho(D_a) = \{ p : p \le 1/a \} \) also earns this), and names (C3) as the failing condition.
- 2: proves that the outside of a non-rational cut has no least element.
- 1: (C1) and (C2) for \( \rho(\alpha) \).
- 3: (C3) for \( \rho(\alpha) \), using a smaller outside point \( q' \) to make the inequality strict.
- 1: states the equivalence with both directions.
Second route: showing \( \rho(\alpha) = \alpha^{-1} \) for non-rational \( \alpha \) (\( \subseteq \) by a smaller outside point \( q' \) making \( pq' < 1 \), \( \supseteq \) since \( < \) implies \( \le \)) and citing @thm-cut-reciprocal earns the 1 point for (C1) and (C2) and the 3 points for (C3). The 2 points for the no-least-element step still require that step.
Fatal errors (0 for the step): assuming \( q > 0 \) without separation against \( 0 \in \alpha \); "a smaller outside point exists" asserted for every cut.
:::

<!-- dependency ledger
prp-cut-product-positive (proof): rational arithmetic and order, (F1)-(F9), (O1)-(O4), prp-ordered-ring-rules, prp-reciprocal-order for rationals | Q ordered field, F3.2 (thm-rationals-ordered-field, recalled in the opening frame)
def-cut-product-positive (claim): lead-in, the set of products is Q when 0 in alpha, beta; x = (-1)(-x), x = a (x/a) | inline; verify/ch07/def-cut-product-positive.py
def-cut-product-positive (claim): lead-in, for D_{-1} the set of products is {x > 1}; p = -(1 + x)/2, q = -2x/(1 + x) | inline; verify/ch07/def-cut-product-positive.py
def-cut-product-positive (claim): a cut alpha > D_0 contains all p <= 0 and a positive element | prp-rational-in-cut, (C2), (C3); inline
lem-cut-multiplicative-step (proof): mu r - (r + eps) = (mu - 1)(r - a) | inline; verify/ch07/lem-cut-multiplicative-step.py
lem-cut-distributive-positive (proof): max{r1, r2} is one of r1, r2 | totality of the order of Q (prp-ordered-ring-rules (i)); inline
def-cut-product (claim): alpha beta is a cut in every case (product a function R_D x R_D -> R_D) | prp-cut-product-positive (a), def-cut-negative (the check that -alpha is a cut), def-rational-cut (D_0)
def-cut-product (claim): D_{-1} < D_0 from -1 < 0; |D_{-1}| = -D_{-1} = D_1 | §02 two translations (p < q iff D_p < D_q); inline (one line, from def-cut-negative)
lem-cut-distributive-positive (claim): beta + gamma > D_0 for beta, gamma > D_0 | prp-rational-in-cut (a), twice
def-cut-product (solution): quick check, D_{-2} D_3 = -(D_2 D_3) = D_{-6} | inline; D_2 D_3 = D_6 is exr-multiplication-b1 (cited only in this solution); |D_{-2}| = D_2 and -D_6 = D_{-6} inline from def-cut-negative
lem-cut-sign-rules (proof): integer arithmetic in {-1, 0, 1} (commutativity, associativity, -(ab) = (-a)b) | Z ordered ring, F3.2 (thm-integers-ordered-ring); inline
lem-cut-distributive (proof): -(beta + gamma) + beta = -gamma; adding a cut to both sides of an equation | thm-cut-ordered-group (a), (c), (e); inline
def-cut-reciprocal (example): D_2^{-1} = D_{1/2} | inline; verify/ch07/thm-cut-reciprocal.py
thm-cut-reciprocal (proof): 1 < mu < 1/p for mu = (1 + 1/p)/2; p mu < 1; (p + 1/q)/2 in (p, 1/q) | prp-ordered-field-halves (b), prp-reciprocal-order (b); verify/ch07/thm-cut-reciprocal.py
thm-cuts-ordered-field (proof): the product of def-cut-product agrees with def-cut-product-positive on positive cuts | the paragraph after def-cut-product
thm-cuts-ordered-field (proof): + and . map R_D x R_D into R_D | thm-cut-sum; the paragraph after def-cut-product
exr-multiplication-a1 (solution): |D_{-1}| = D_1, -D_{1/2} = D_{-1/2} | exr-addition-b1 (an exercise, cited only in this solution)
exr-multiplication-b1 (solution): lambda = (1 + x/6)/2, r = 2 lambda, s = x/(2 lambda) | inline; verify/ch07/exr-multiplication-b1.py
exr-multiplication-b2 (solution): s mu r = p mu < 1 | inline; verify/ch07/thm-cut-reciprocal.py
exr-multiplication-c1 (solution): rho(D_a) = {p <= 1/a}; outside of a non-rational cut has no least element | inline; verify/ch07/exr-multiplication-c1.py
exr-multiplication-c1 (solution): sigma is not rational, so rho(sigma) = sigma^{-1} | exr-cuts-c1 (an exercise, cited only in this solution)
-->
