# What Completeness Gives at Once

Chapter 5 ended with one complete ordered field, the classes of Cauchy sequences of rationals (@thm-reals-complete-ordered-field). *Axiomatic Set Theory* builds another from Dedekind cuts, and *Analysis on the Real Line* simply assumes that one exists. This chapter asks whether these are the same field. Before that question can be asked we need a precise meaning for "the same": a map between ordered fields that respects everything. This section fixes that meaning, and then collects what completeness gives at once: the Archimedean property, a way to tell elements apart by the rationals below them, and square roots.

**Standing setting.** Throughout the chapter, \( F \) and \( L \) are ordered fields (@def-ordered-ring-and-field), so \( \le \) is a total order on each (@prp-ordered-field-halves (a)) and upper bounds and suprema in the sense of *Sets and Functions*, Section 5.3 apply to their subsets (@fd2:def-order-bounds, @fd2:def-order-supremum). "Complete" is always the property of @def-complete-ordered-field: every non-empty subset that is bounded above has a supremum. We do not redefine it.

Each ordered field \( F \) carries its own copy of \( \nQ \): the map \( \iota_F \colon \nQ \to F \) of @thm-rationals-embed-ordered-field, the only map with \( \iota_F(1) = 1_F \) that preserves sums and products. It is injective, strictly increasing and reflects order, and \( \iota_F(n) = n \cdot 1_F \) for \( n \in \nN \). For the constructed reals, \( \iota_{\nR} \) is the map \( \kappa \) of Chapter 5 (@thm-rational-embedding (d)). When only one field is in play, a proof may write \( q \) for \( \iota_F(q) \), as Chapter 4 did; statements keep \( \iota_F \) visible, and so does every argument that moves between two fields.

## Maps that respect everything

To say that two ordered fields are "the same", we want a dictionary between them: a map that turns sums into sums, products into products, \( 1 \) into \( 1 \), and smaller into smaller. An isomorphism of Peano systems in Chapter 1 (@thm-peano-categoricity) was such a dictionary for \( 0 \) and the successor; here the structure is larger.

*A map that respects addition, multiplication, the unit and the order.*

::: {#def-cof-order-preserving-map}
[Order-Preserving Field Map]

Let \( F \) and \( L \) be ordered fields. A map \( \chi \colon F \to L \) is an **order-preserving field map** if, **for all** \( a, b \in F \),
\[
\chi(a + b) = \chi(a) + \chi(b) , \qquad \chi(ab) = \chi(a)\, \chi(b) , \qquad \chi(1_F) = 1_L ,
\]
and \( a < b \) implies \( \chi(a) < \chi(b) \). An **order-preserving field isomorphism** is an order-preserving field map that is **bijective** (@fd2:def-bijective). An **order-preserving field automorphism** of \( F \) is an order-preserving field isomorphism \( F \to F \).
:::

In words: the first two equations say that computing in \( F \) and then translating gives the same answer as translating and then computing in \( L \); the third pins down the unit; the last says that \( \chi \) is **strictly** increasing.

Two consequences come free. A strictly increasing map is injective: if \( a \ne b \), then \( a < b \) or \( b < a \) by (O1), and the images differ in the same way. And it **reflects order**: if \( \chi(a) < \chi(b) \), then \( a < b \). For \( a = b \) would give \( \chi(a) = \chi(b) \), and \( b < a \) would give \( \chi(b) < \chi(a) \); both contradict \( \chi(a) < \chi(b) \) by (O1), so only \( a < b \) is left. So an order-preserving field map satisfies \( a < b \iff \chi(a) < \chi(b) \).

**Examples.**

*The identity.* \( \id_F \) satisfies all four clauses trivially; it is an order-preserving field automorphism of \( F \).

*The copy of the rationals.* For every ordered field \( F \), \( \iota_F \colon \nQ \to F \) is an order-preserving field map, by @thm-rationals-embed-ordered-field. It is injective and usually not surjective: \( \iota_{\nR} = \kappa \) misses the class \( r \) of the Newton sequence, which is not \( \kappa(q) \) for any rational \( q \) (@exm-sqrt2-class).

*Doubling.* On \( \nQ \), \( \chi(x) \coloneqq 2x \) preserves sums and is strictly increasing, but \( \chi(1) = 2 \ne 1 \), and \( \chi(1 \cdot 1) = 2 \ne 4 = \chi(1)\chi(1) \). It is not a field map: the clauses about multiplication and the unit fail, the additive ones survive.

::: {.second-reading title="A degenerate case"}
The zero map \( \chi(a) \coloneqq 0_L \) preserves sums and products, since \( 0 + 0 = 0 \) and \( 0 \cdot 0 = 0 \). It fails the unit clause, because \( 1_L \ne 0_L \) in a field, and it fails strict increase. In @def-cof-order-preserving-map the unit clause in fact follows from the other three: additivity gives \( \chi(0) = \chi(0) + \chi(0) \), so \( \chi(0) = 0 \); strict increase then gives \( \chi(1) > \chi(0) = 0 \); and \( \chi(1) = \chi(1)^2 \) with \( \chi(1) \ne 0 \) forces \( \chi(1) = 1 \). It is stated anyway because @prp-cof-map-fixes-rationals, @thm-cof-field-automorphism-identity and the remark after its proof assume sums, products and the unit but no order. Without the unit hypothesis, the zero map would be a counterexample to each of them.
:::

**Why this definition.** Preserving sums, products and the unit is what makes \( \chi \) a dictionary for the field operations; strict increase makes it a dictionary for the order. *Algebraic Preliminaries*, Chapter 2 shows a map of \( \nQ(\sqrt 2) \) to itself that respects sums, products and the unit but sends a positive element to a negative one, so the order clause does not follow from the others in general. Section 6.3 shows that for complete ordered fields it does.

::: {.check}
Which clauses of @def-cof-order-preserving-map does the map \( \chi \colon \nQ \to \nQ \), \( \chi(x) \coloneqq -x \), satisfy?
:::

::: {.solution}
Only the sum clause: \( -(a + b) = (-a) + (-b) \). The unit clause fails, \( \chi(1) = -1 \ne 1 \), and so does the product clause, since \( \chi(1 \cdot 1) = -1 \) while \( \chi(1)\chi(1) = (-1)(-1) = 1 \); and the order is reversed, \( 0 < 1 \) but \( \chi(1) = -1 < 0 = \chi(0) \).
:::

The first result about these maps needs no order hypothesis at all. A map that preserves sums, products and the unit cannot move a rational number.

::: {#prp-cof-map-fixes-rationals}
[Field Maps Fix the Rationals]

Let \( F \) and \( L \) be ordered fields, and let \( \chi \colon F \to L \) satisfy \( \chi(a + b) = \chi(a) + \chi(b) \), \( \chi(ab) = \chi(a)\chi(b) \) for all \( a, b \in F \), and \( \chi(1_F) = 1_L \). Then
\[
\chi \circ \iota_F = \iota_L , \qquad \text{that is,} \qquad \chi\bigl(\iota_F(q)\bigr) = \iota_L(q) \quad \text{for every } q \in \nQ .
\]
:::

::: {.proof}
The composite \( \chi \circ \iota_F \colon \nQ \to L \) sends \( 1 \) to \( \chi(1_F) = 1_L \), and for \( x, y \in \nQ \),
\[
\chi\bigl(\iota_F(x + y)\bigr) = \chi\bigl(\iota_F(x) + \iota_F(y)\bigr) = \chi\bigl(\iota_F(x)\bigr) + \chi\bigl(\iota_F(y)\bigr) ,
\]
by @thm-rationals-embed-ordered-field for \( F \) and the hypothesis on \( \chi \); products are the same with \( \cdot \) in place of \( + \). So \( \chi \circ \iota_F \) has the three properties that, by the uniqueness clause of @thm-rationals-embed-ordered-field for \( L \), only \( \iota_L \) has. Hence \( \chi \circ \iota_F = \iota_L \).
:::

This is the remark after @thm-rationals-embed-ordered-field, now with a label. Read with the identifications \( q = \iota_F(q) \) and \( q = \iota_L(q) \), it says \( \chi(q) = q \): such a map **fixes the rationals**. If \( \chi \) is also order-preserving, more follows. For \( q \in \nQ \) and \( x \in F \), \( \iota_F(q) < x \) holds if and only if \( \chi(\iota_F(q)) < \chi(x) \), that is, if and only if \( \iota_L(q) < \chi(x) \). The rationals below \( x \) in \( F \) are exactly the rationals below \( \chi(x) \) in \( L \). That observation drives the whole chapter.

## A complete ordered field is Archimedean

Chapter 4 called \( F \) Archimedean if every element lies below some \( n \cdot 1_F \) (@def-archimedean-ordered-field), and showed that this can fail: in \( \nQ(t) \) the element \( t \) lies above every \( n \cdot 1 \) (@exm-rational-function-field). Chapter 5 proved it for the constructed \( \nR \) (@thm-constructed-reals-archimedean) on the way to completeness. For the supremum form of completeness, no assumption is needed: it implies the Archimedean property. We write \( \iota_F(\nN) \coloneqq \{ \iota_F(n) : n \in \nN \} = \{ n \cdot 1_F : n \in \nN \} \).

::: {#thm-cof-complete-archimedean}
[A Complete Ordered Field Is Archimedean]

Let \( F \) be a complete ordered field. Then \( F \) is Archimedean (@def-archimedean-ordered-field).
:::

::: {.idea}
If some element bounded \( \iota_F(\nN) \) above, completeness would give a **least** upper bound \( s \). Step down by \( 1 \): \( s - 1 \) is not an upper bound, so some \( n \cdot 1_F \) is above it, and one more step, \( (n + 1) \cdot 1_F \), is above \( s \). The set \( \iota_F(\nN) \) is closed under adding \( 1 \), so it cannot have a least upper bound, and hence no upper bound at all.
:::

::: {.proof}
Suppose that \( \iota_F(\nN) \) is bounded above. It is non-empty, since \( 0 \cdot 1_F \in \iota_F(\nN) \), so by completeness it has a supremum \( s \). Since \( s - 1_F < s \), the element \( s - 1_F \) is not an upper bound of \( \iota_F(\nN) \): some \( n \in \nN \) has \( n \cdot 1_F > s - 1_F \) (@fd1:prp-bounded-quantifier-negation (a), with totality, @prp-ordered-field-halves (a)). Then \( (n + 1) \cdot 1_F = n \cdot 1_F + 1_F > s \) (@def-naturals-in-ordered-field (a) and (O3)), and \( (n + 1) \cdot 1_F \in \iota_F(\nN) \), against \( s \) being an upper bound. So \( \iota_F(\nN) \) is not bounded above: for each \( x \in F \), \( x \) is not an upper bound, and as before some \( n \in \nN \) has \( x < n \cdot 1_F \). Hence \( F \) is Archimedean (@def-archimedean-ordered-field).
:::

Both hypotheses of completeness were used: "non-empty" through \( 0 \cdot 1_F \), "bounded above" through the existence of \( s \). The converse fails: \( \nQ \) is Archimedean (@thm-rationals-archimedean) and not complete (@thm-rationals-gap-sqrt2). And dropping completeness can lose the conclusion: \( \nQ(t) \) is an ordered field that is not Archimedean.

The proof never claimed that \( s \) is an element of \( \iota_F(\nN) \); a supremum need not belong to its set. Exercise C2 shows how tempting that claim is.

::: {.check}
In a complete ordered field \( F \), is \( \iota_F(\nZ) \) bounded below?
:::

::: {.solution}
No. If \( b \le \iota_F(k) \) for every \( k \in \nZ \), then \( -b \ge \iota_F(n) = n \cdot 1_F \) for every \( n \in \nN \), taking \( k = -n \); so \( -b \) bounds \( \iota_F(\nN) \) above, against @thm-cof-complete-archimedean.
:::

::: {.warning}
Completeness here is about **subsets**, not sequences. In this chapter "complete" is the supremum property of @def-complete-ordered-field, and the theorem above shows that it brings the Archimedean property with it. Do not replace it by Cauchy-completeness in the proofs below: a Cauchy-complete ordered field need not be Archimedean, a fact this book does not prove and *Analysis on the Real Line*, Chapter 11 returns to.
:::

Every complete ordered field therefore has the consequences of the Archimedean property that Chapter 4 proved. The one we use most is density (@thm-rationals-dense-ordered-field): in an Archimedean ordered field \( F \), for all \( x < y \) there is \( q \in \nQ \) with \( x < \iota_F(q) < y \). We cite it, not reprove it; Section 6.2 uses it in two fields at once.

Here is the Archimedean property at work on a specific supremum. The pattern has two halves: check the candidate is an upper bound, then show that anything smaller is not one.

::: {#exm-cof-sup-one-minus-reciprocals}
[A Supremum Computed by Archimedes]

Let \( F \) be a complete ordered field. Show that \( \sup\{ \iota_F(1 - 1/n) : n \in \nZ_{>0} \} = 1_F \).
:::

::: {.solution}
Let \( A \coloneqq \{ \iota_F(1 - 1/n) : n \in \nZ_{>0} \} \).

*Upper bound.* For \( n \in \nZ_{>0} \), \( 1/n > 0 \) in \( \nQ \), so \( 1 - 1/n < 1 \), and \( \iota_F(1 - 1/n) < \iota_F(1) = 1_F \) because \( \iota_F \) is strictly increasing (@thm-rationals-embed-ordered-field). So \( 1_F \) is an upper bound of \( A \).

*Least.* Let \( b \) be an upper bound of \( A \) and suppose \( b < 1_F \). By @thm-cof-complete-archimedean and @prp-archimedean-reciprocal (with \( \varepsilon \coloneqq 1_F - b \)) some \( N \in \nZ_{>0} \) has \( 1/(N \cdot 1_F) < 1_F - b \). Since \( \iota_F \) preserves sums and products, hence inverses (@lem-field-fraction-rules (a)), and \( \iota_F(N) = N \cdot 1_F \),
\[
\iota_F(1 - 1/N) = 1_F - \frac{1}{N \cdot 1_F} > b :
\]
an element of \( A \) above \( b \), which is impossible. So every upper bound is \( \ge 1_F \), and \( 1_F = \sup A \) (@fd2:def-order-supremum).
:::

The supremum \( 1_F \) is not an element of \( A \): every element is strictly below it. Completeness entered only through the Archimedean property; in an ordered field that is Archimedean but not complete, such as \( \nQ \) (@thm-rationals-archimedean), the same two halves give the same answer. Exercises B1 and B2 follow this pattern.

## The rationals below an element

How can we tell two elements of a field apart? In an Archimedean field, by a rational between them. That suggests recording, for each element, which rationals lie below it.

*An element is measured by the rationals below it.*

::: {#def-cof-rationals-below}
[The Rationals below an Element]

Let \( F \) be an ordered field and \( x \in F \). The **rationals below \( x \)** form the set
\[
\nQ_F(x) \coloneqq \{ q \in \nQ : \iota_F(q) < x \} \subseteq \nQ .
\]
:::

In words: \( \nQ_F(x) \) is a set of **rational numbers**, not of elements of \( F \); a rational \( q \) belongs to it when its copy \( \iota_F(q) \) lies **strictly** below \( x \).

Two properties hold in every ordered field and are used without comment. The set is **closed downward**: if \( q \in \nQ_F(x) \) and \( p < q \), then \( \iota_F(p) < \iota_F(q) < x \), so \( p \in \nQ_F(x) \). And if \( x \le y \), then \( \nQ_F(x) \subseteq \nQ_F(y) \), by transitivity.

**Examples.**

*A rational element.* For \( r \in \nQ \), \( \nQ_F(\iota_F(r)) = \{ q \in \nQ : q < r \} \). Indeed \( \iota_F(q) < \iota_F(r) \) holds if and only if \( q < r \), because \( \iota_F \) is strictly increasing and reflects order. In particular \( r \notin \nQ_F(\iota_F(r)) \): the inequality is strict.

::: {#exm-cof-rationals-below-sqrt2}
[The Rationals below the Square Root of Two]

Let \( r \in \nR \) be the class of the Newton sequence, so that \( r > 0 \) and \( r^2 = 2 \) (@exm-sqrt2-class). Show that
\[
\nQ_{\nR}(r) = \{ q \in \nQ : q < 0 \} \cup \{ q \in \nQ : q \ge 0 \text{ and } q^2 < 2 \} .
\]
:::

::: {.solution}
Negative rationals lie below \( r > 0 \); for \( q \ge 0 \), compare squares.

::: {.second-reading title="The computation"}
Let \( q \in \nQ \), and recall \( \iota_{\nR} = \kappa \) (@thm-rational-embedding (d)). If \( q < 0 \), then \( \kappa(q) < \kappa(0) = 0 < r \), so \( q \in \nQ_{\nR}(r) \). Let \( q \ge 0 \), so \( \kappa(q) \ge 0 \). Since also \( r > 0 \), @prp-ordered-ring-rules (g) in \( \nR \) gives
\[
\kappa(q) < r \iff \kappa(q)^2 < r^2 = 2 .
\]
Now \( \kappa(q)^2 = \kappa(q^2) \) and \( 2 = \kappa(2) \) (@thm-rational-embedding (a)), and \( \kappa(q^2) < \kappa(2) \) if and only if \( q^2 < 2 \) (@thm-rational-embedding (b)). So for \( q \ge 0 \), \( q \in \nQ_{\nR}(r) \) if and only if \( q^2 < 2 \). Together the two cases give the displayed set.
:::
:::

The set of Section 3.3, \( \{ x \in \nQ : x^2 < 2 \} \) (@thm-rationals-gap-sqrt2), is **not** \( \nQ_{\nR}(r) \): it omits \( -2 \), whose square is \( 4 \). That set is not closed downward, and a rationals-below set always is.

::: {.check}
Let \( F \) be an ordered field and \( x \coloneqq \iota_F(3/2) \). Describe \( \nQ_F(x) \), and say whether \( 3/2 \in \nQ_F(x) \).
:::

::: {.solution}
By the first example, \( \nQ_F(x) = \{ q \in \nQ : q < 3/2 \} \). It does not contain \( 3/2 \), since \( \iota_F(3/2) < \iota_F(3/2) \) is false by (O1).
:::

The point of the definition is that in an Archimedean field, these sets lose no information.

::: {#lem-cof-rationals-separate}
[Rationals Separate]

Let \( F \) be an Archimedean ordered field, and let \( x, y \in F \). Then
\[
x \le y \iff \nQ_F(x) \subseteq \nQ_F(y) .
\]
Consequently \( x = y \iff \nQ_F(x) = \nQ_F(y) \).
:::

::: {.proof}
\( (\Rightarrow) \) This is the second property after @def-cof-rationals-below: if \( \iota_F(q) < x \) and \( x \le y \), then \( \iota_F(q) < y \).

\( (\Leftarrow) \) We prove the contrapositive (@fd1:prp-contrapositive). Suppose that \( x \le y \) fails. Then \( y < x \) by totality (@prp-ordered-field-halves (a)). By @thm-rationals-dense-ordered-field there is \( q \in \nQ \) with \( y < \iota_F(q) < x \). Then \( q \in \nQ_F(x) \), and \( q \notin \nQ_F(y) \), since \( \iota_F(q) < y \) and \( y < \iota_F(q) \) cannot both hold (O1). So \( \nQ_F(x) \not\subseteq \nQ_F(y) \).

For the consequence: \( x = y \) holds if and only if \( x \le y \) and \( y \le x \), by antisymmetry of the total order \( \le \); by the equivalence just proved, that is \( \nQ_F(x) \subseteq \nQ_F(y) \) and \( \nQ_F(y) \subseteq \nQ_F(x) \), that is, \( \nQ_F(x) = \nQ_F(y) \).
:::

This is the first named move of the chapter, **rationals separate**: to prove two elements of an Archimedean field equal, show that the same rationals lie below each. A rational strictly between them would otherwise exist. Section 6.2 uses it in four of the seven steps of its main proof (Steps 3, 5, 6 and 7), each time to prove that two elements of the complete field are equal.

::: {.second-reading title="Without Archimedes the sets cannot tell elements apart"}
The direction \( (\Rightarrow) \) and the remark that equal elements have equal sets hold in every ordered field. The direction \( (\Leftarrow) \) needs density, and density needs Archimedes. In the non-Archimedean field \( \nQ(t) \) of @exm-rational-function-field (school polynomial algebra, as flagged there; nothing below depends on it), every rational \( q \) satisfies \( q < n \) for some \( n \in \nN \) (@thm-rationals-archimedean), and \( n \cdot 1 < t \), so \( \iota_{\nQ(t)}(q) < t < t + 1 \). Hence \( \nQ_{\nQ(t)}(t) = \nQ = \nQ_{\nQ(t)}(t + 1) \), although \( t \ne t + 1 \). Both elements lie above all of the rationals, and the rationals cannot see the difference.
:::

## Constructing a point as a supremum

Some elements cannot be written down in advance. In \( \nQ \) the equation \( x^2 = 2 \) has no solution (@thm-no-rational-square-two); in a complete ordered field we expect one, but no formula names it. What we can name is the set of elements that should lie **below** it. Completeness turns that set into an element, its supremum, and the work is to prove that this element does what we want. We do it in full for square roots, extract the method, and run it again to find an element between two sets.

::: {#prp-cof-square-roots}
[Square Roots in a Complete Ordered Field]

Let \( F \) be a complete ordered field and \( a \in F \) with \( a \ge 0 \). Then there is **exactly one** \( b \in F \) with \( b \ge 0 \) and \( b^2 = a \).
:::

::: {.idea}
[Scratch work]

The square root of \( a > 0 \) should be the top of \( S \coloneqq \{ y \ge 0 : y^2 < a \} \). Two jobs before taking a supremum: \( S \ne \emptyset \) (\( 0 \in S \)) and an upper bound (\( a + 1 \): a larger \( y \) has \( y^2 > y > a \)). Put \( s \coloneqq \sup S \). The goal \( s^2 = a \) is an equation, so we refute the two strict cases.

| Givens | Goal |
|---|---|
| \( F \) complete, \( a > 0 \); \( S = \{ y \ge 0 : y^2 < a \} \) non-empty, bounded by \( a + 1 \) | some \( b \ge 0 \) with \( b^2 = a \) |
| \( s = \sup S \), \( s \ge 0 \) | \( s^2 = a \): rule out \( s^2 < a \) and \( s^2 > a \) |
| case \( s^2 < a \) | an element of \( S \) **above** \( s \), against (S1): \( s + h \) with \( (s + h)^2 < a \) |
| case \( s^2 > a \) | an upper bound of \( S \) **below** \( s \), against (S2): \( s - h > 0 \) with \( (s - h)^2 \ge a \) |

If \( s^2 < a \), there is room above \( s \): we look for \( h > 0 \) with \( (s + h)^2 < a \), which puts \( s + h \) in \( S \) above its supremum. Working backwards, for \( 0 < h \le 1 \) we have \( h^2 \le h \), so
\[
(s + h)^2 = s^2 + 2sh + h^2 \le s^2 + h(2s + 1) ,
\]
and it is enough that \( h(2s + 1) \) be at most half the room \( a - s^2 \). So \( h \coloneqq \min\{1, (a - s^2)/(2(2s + 1))\} \).

If \( s^2 > a \), then \( s \) overshoots: we look for \( h > 0 \) with \( (s - h)^2 \ge a \) still, which makes \( s - h \) a smaller upper bound. Since \( (s - h)^2 \ge s^2 - 2sh \), it is enough that \( 2sh = s^2 - a \), so \( h \coloneqq (s^2 - a)/(2s) \).

Both \( h \) depend on \( s \) and \( a \) only; the proof fixes them first and checks forwards.
:::

::: {.proof}
*Existence.* If \( a = 0 \), then \( b \coloneqq 0 \) works. Let \( a > 0 \), and let
\[
S \coloneqq \{ y \in F : y \ge 0 \text{ and } y^2 < a \} .
\]
Then \( 0 \in S \), since \( 0^2 = 0 < a \). And \( a + 1 \) is an upper bound of \( S \): if \( y > a + 1 \), then \( y > 1 > 0 \), so \( y^2 = y \cdot y > y \cdot 1 = y > a \) (@prp-ordered-ring-rules (c)), and \( y \notin S \); so every \( y \in S \) satisfies \( y \le a + 1 \) by totality. Since \( F \) is complete, let \( s \coloneqq \sup S \). Since \( 0 \in S \), \( s \ge 0 \).

*Case \( s^2 < a \).* Let \( h \coloneqq \min\{1, (a - s^2)/(2(2s + 1))\} \). It is defined and positive, since \( 2s + 1 \ge 1 > 0 \) and \( a - s^2 > 0 \) (@prp-reciprocal-order (a), (O4)). Since \( 0 < h \le 1 \), \( h^2 \le h \) (@prp-ordered-ring-rules (c)), so
\[
\begin{aligned}
(s + h)^2 &= s^2 + 2sh + h^2 \le s^2 + h(2s + 1) \\
&\le s^2 + \frac{a - s^2}{2} < a ,
\end{aligned}
\]
where the second inequality uses \( h \le (a - s^2)/(2(2s + 1)) \) and \( 2s + 1 > 0 \), and the last uses \( (a - s^2)/2 < a - s^2 \) (@prp-ordered-field-halves (b)). So \( s + h \ge 0 \) lies in \( S \), and \( s + h > s \), against \( s \) being an upper bound of \( S \).

*Case \( s^2 > a \).* Then \( s \ne 0 \), since \( 0^2 = 0 < a \); so \( s > 0 \). Let \( h \coloneqq (s^2 - a)/(2s) \). It is positive, since \( s^2 - a > 0 \) and \( 2s > 0 \) (@prp-reciprocal-order (a), (O4)). Then \( s - h = (s^2 + a)/(2s) > 0 \) by the same reasons, since \( s^2 + a > 0 \); and
\[
(s - h)^2 = s^2 - 2sh + h^2 = s^2 - (s^2 - a) + h^2 = a + h^2 > a .
\]
We claim that \( s - h \) is an upper bound of \( S \). Let \( y > s - h \). Then \( y > 0 \), and @prp-ordered-ring-rules (g) gives \( y^2 > (s - h)^2 > a \), so \( y \notin S \). Hence every element of \( S \) is \( \le s - h \). But \( s - h < s \), against \( s \) being the **least** upper bound.

Both cases are impossible, so \( s^2 = a \) by trichotomy (O1), and \( b \coloneqq s \ge 0 \) works.

*Uniqueness.* Let \( b, c \ge 0 \) with \( b^2 = c^2 = a \). Then \( (b - c)(b + c) = b^2 - c^2 = 0 \), so \( b = c \) or \( b + c = 0 \) (@prp-ordered-ring-rules (f)). If \( b + c = 0 \), then \( b = -c \le 0 \le b \), so \( b = 0 \) and \( c = -b = 0 \). In either case \( b = c \).
:::

For \( a \ge 0 \) in a complete ordered field we write \( \sqrt a \) for this \( b \). In the constructed reals, the class \( r \) of @exm-sqrt2-class has \( r > 0 \) and \( r^2 = 2 \), so \( r = \sqrt 2 \) by the uniqueness clause, and @exm-cof-rationals-below-sqrt2 describes \( \nQ_{\nR}(\sqrt 2) \).

Completeness was used once, to produce \( s \); the rest is ordered-field arithmetic. Without completeness the statement fails: \( 2 \) has no square root in \( \nQ \), and *Algebraic Preliminaries*, Chapter 2 meets \( \nQ(\sqrt 2) \), an Archimedean field that still lacks square roots.

::: {#exm-method-point-as-supremum}
[Method: construct a point as a supremum]

**Template.** To produce an element with a property \( P \) in a complete ordered field: (1) choose a set \( S \) of elements that should lie below it; (2) check that \( S \) is non-empty and bounded above; (3) let \( s \coloneqq \sup S \); (4) prove \( P(s) \). An inequality \( y \le s \) for \( y \in S \) is (S1). An inequality \( s \le u \) follows once \( u \) is shown to be an upper bound of \( S \) (S2). An equation is proved by refuting both strict cases: one by an element of \( S \) above \( s \), the other by an upper bound of \( S \) below \( s \).

**When to use it.** When the element has no formula but the elements below it can be described: a square root, an element between two sets, the value \( \varphi(x) \) in Section 6.2, the limit of a bounded increasing sequence (Exercise C3 of Section 6.3). It is @fd2:exm-method-construct-and-verify with the construction step done by completeness.

**The usual failure.** Taking the supremum before checking (2); assuming \( s \in S \); choosing \( h \) that depends on something other than \( s \) and the data.
:::

::: {#exm-cof-separating-element}
[An Element Between Two Sets]

Let \( F \) be a complete ordered field, and let \( A, B \subseteq F \) be non-empty with \( a \le b \) for every \( a \in A \) and \( b \in B \).

::: {.enumerate options="label=(\alph*)"}
1. Show that some \( c \in F \) has \( a \le c \le b \) for every \( a \in A \) and \( b \in B \).
2. Show that if, in addition, for every \( \varepsilon > 0 \) there are \( a \in A \) and \( b \in B \) with \( b - a < \varepsilon \), then \( c \) is the only such element.
:::
:::

::: {.solution}
(a) *Choose \( S \).* The element should lie above all of \( A \): take \( S \coloneqq A \), non-empty. *An upper bound.* Fix \( b_0 \in B \); every \( a \in A \) has \( a \le b_0 \). *Take the supremum* \( c \coloneqq \sup A \). Then \( a \le c \) for \( a \in A \) by (S1), and for \( b \in B \), \( b \) is an upper bound of \( A \) by hypothesis, so \( c \le b \) by (S2).

::: {.second-reading title="Only one such element"}
**(b)** Let \( c' \) be another such element, and suppose \( c \ne c' \). Take \( \varepsilon \coloneqq \abs{c - c'} > 0 \) and \( a \in A \), \( b \in B \) with \( b - a < \varepsilon \). Both \( c \) and \( c' \) lie between \( a \) and \( b \), so \( -(b - a) \le c - c' \le b - a \), and \( \abs{c - c'} \le b - a < \varepsilon \) (@prp-absolute-value-ordered-field (d)): a contradiction.
:::
:::

No equation had to be refuted case by case here: (S1) and (S2) gave the two inequalities directly. Section 6.3 meets the same picture again: a real number sits between the rationals below it and those above it.

::: {.check}
In \( \nQ \), let \( A \coloneqq \{ p \in \nQ : p^2 < 2 \} \) and \( B \coloneqq \{ p \in \nQ : p > 0,\ p^2 > 2 \} \). Every element of \( A \) is below every element of \( B \). Is there a rational \( c \) with \( a \le c \le b \) for all \( a \in A \), \( b \in B \)?
:::

::: {.solution}
No. Such a \( c \) is an upper bound of \( A \). Every rational upper bound \( u \) of \( A \) lies in \( B \): \( u \ge 1 > 0 \) since \( 1 \in A \); \( u^2 \ne 2 \) (@thm-no-rational-square-two); and \( u^2 < 2 \) would make \( u \) the largest element of \( A \), hence a supremum of \( A \) in \( \nQ \). So \( c \le u \) for every upper bound \( u \), and \( c \) would be a supremum of \( A \) in \( \nQ \), against @thm-rationals-gap-sqrt2 (a). The example needs completeness.
:::

## Exercises

### A. Check your understanding

::: {#exr-completeness-and-archimedes-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. True or false, with a reason: in **every** ordered field \( F \), if \( \nQ_F(x) \ne \nQ_F(y) \) then \( x \ne y \). Is the converse true in every ordered field?
2. Write "\( F \) is Archimedean" in symbols, and state its negation with the quantifiers moved to the front (@fd1:prp-quantifier-negation).
3. The eight lines (i)–(viii) below are about a complete ordered field \( F \); six of them, in a suitable order, prove @thm-cof-complete-archimedean. Write an admissible order, and say why each of the other two lines is wrong.
:::

::: {.enumerate options="label=(\roman*)"}
1. Then \( \iota_F(n + 1) = \iota_F(n) + 1 > s \), and \( n + 1 \in \nN \).
2. For every \( n \in \nN \), \( \iota_F(n) > s - 1 \).
3. The set \( \iota_F(\nN) \) is non-empty (\( 0 \in \nN \)), so \( s \coloneqq \sup \iota_F(\nN) \) exists.
4. This contradicts that \( s \) is an upper bound of \( \iota_F(\nN) \).
5. Suppose that \( \iota_F(\nN) \) is bounded above.
6. So \( \iota_F(n) > s - 1 \) for some \( n \in \nN \).
7. So \( s \in \iota_F(\nN) \), say \( s = \iota_F(m) \).
8. Since \( s - 1 < s \), the element \( s - 1 \) is not an upper bound of \( \iota_F(\nN) \).
:::
:::

::: {.solution}
(a) True. It is the contrapositive (@fd1:prp-contrapositive) of "if \( x = y \) then \( \nQ_F(x) = \nQ_F(y) \)", which holds because equal elements have the same rationals below them. The converse, "if \( x \ne y \) then \( \nQ_F(x) \ne \nQ_F(y) \)", is the direction \( (\Leftarrow) \) of @lem-cof-rationals-separate, and it needs the Archimedean property: in \( \nQ(t) \), \( t \ne t + 1 \) and both have every rational below them (the second-reading note after @lem-cof-rationals-separate).

(b) \( \forall x \in F \ \exists n \in \nN \ \ x < n \cdot 1_F \). Negation: \( \exists x \in F \ \forall n \in \nN \ \ n \cdot 1_F \le x \), using \( \neg(x < y) \iff y \le x \) (totality and (O1)). In words: some element lies above or at every \( n \cdot 1_F \).

(c) (v), (iii), (viii), (vi), (i), (iv). No other order is admissible: each line uses the one before it ((iii) needs the bound of (v) for the supremum to exist, (viii) needs \( s \), (vi) unpacks (viii), (i) uses the \( n \) of (vi), and (iv) is the contradiction with (i)). The contradiction in (iv) refutes (v), so \( \iota_F(\nN) \) is not bounded above; unpacked with the negation laws, as at the end of the proof of @thm-cof-complete-archimedean, that is the statement of (b).

Line (vii) is wrong: a supremum need not belong to the set (in every ordered field, the set of negative elements has supremum \( 0 \), which is not negative: the first example after @def-complete-ordered-field). Line (ii) has the wrong quantifier: "\( s - 1 \) is not an upper bound" gives **some** \( n \) with \( \iota_F(n) > s - 1 \), by @fd1:prp-bounded-quantifier-negation, not every \( n \) (and for \( n = 0 \) it may be false).
:::

### B. Practice

::: {#exr-completeness-and-archimedes-b1}
[B1]

Let \( F \) be a complete ordered field. Prove that \( \inf\{ \iota_F(1/n) : n \in \nZ_{>0} \} = 0 \).
:::

::: {.solution}
Let \( T \coloneqq \{ \iota_F(1/n) : n \in \nZ_{>0} \} \). For \( n \in \nZ_{>0} \), \( 1/n > 0 \) in \( \nQ \), so \( \iota_F(1/n) > 0 \): \( 0 \) is a lower bound of \( T \).

Let \( c \) be a lower bound of \( T \), and suppose, for contradiction, that \( c > 0 \). By @thm-cof-complete-archimedean, \( F \) is Archimedean, so @prp-archimedean-reciprocal (with \( \varepsilon \coloneqq c \), applied at \( n = N \)) gives \( N \in \nZ_{>0} \) with \( 1/(N \cdot 1_F) < c \). Since \( \iota_F \) preserves products and \( \iota_F(N) = N \cdot 1_F \), we have \( \iota_F(1/N) \cdot (N \cdot 1_F) = \iota_F(1) = 1_F \), so \( \iota_F(1/N) = 1/(N \cdot 1_F) \) by uniqueness of inverses (@lem-field-fraction-rules (a)). So the element \( \iota_F(1/N) \) of \( T \) lies below \( c \), against \( c \) being a lower bound. Hence every lower bound \( c \) satisfies \( c \le 0 \), and \( 0 \) is the greatest lower bound (@fd2:def-order-supremum).
:::

::: {#exr-completeness-and-archimedes-b2}
[B2]

Let \( F \) be an Archimedean ordered field and \( x \in F \). Prove that the set \( \iota_F(\nQ_F(x)) = \{ \iota_F(q) : q \in \nQ_F(x) \} \) has supremum \( x \) in \( F \).
:::

::: {.solution}
*Upper bound.* Every element \( \iota_F(q) \) of the set satisfies \( \iota_F(q) < x \) by the definition of \( \nQ_F(x) \).

*Least.* Let \( u \) be an upper bound, and suppose \( u < x \). By @thm-rationals-dense-ordered-field there is \( q \in \nQ \) with \( u < \iota_F(q) < x \). Then \( q \in \nQ_F(x) \), so \( \iota_F(q) \) is in the set and exceeds \( u \), against \( u \) being an upper bound. So \( x \le u \) by totality, for every upper bound \( u \). Hence \( x = \sup \iota_F(\nQ_F(x)) \).

No completeness was used: the supremum exists because we exhibited it.
:::

::: {#exr-completeness-and-archimedes-b3}
[B3: Prove or disprove]

Prove each true statement and refute each false one. Throughout, \( F \) is a complete ordered field and rationals stand for their copies \( \iota_F(q) \).

::: {.enumerate options="label=(\alph*)"}
1. Every \( a > 0 \) in \( F \) has exactly two elements \( b \) with \( b^2 = a \).
2. In every Archimedean ordered field, every element \( a \ge 0 \) has a square root.
3. If \( S \subseteq F \) is non-empty and bounded above, then \( \sup S \in S \).
4. For every \( a > 0 \) in \( F \) there is \( x > 0 \) with \( x^2 + x = a \).
5. If \( S \subseteq F \) is non-empty, \( c \in F \), and \( y < c \) for every \( y \in S \), then \( \sup S < c \).
:::
:::

::: {.solution}
(a) **True.** Let \( r \coloneqq \sqrt a \) (@prp-cof-square-roots). Then \( r \ne 0 \), since \( a \ne 0 \); so \( r > 0 > -r \) and \( r \ne -r \), and both square to \( a \). Conversely, let \( b^2 = a \). If \( b \ge 0 \), then \( b = r \) by the uniqueness clause. If \( b < 0 \), then \( -b > 0 \) and \( (-b)^2 = b^2 = a \), so \( -b = r \) and \( b = -r \). So the two elements are \( r \) and \( -r \).

(b) **False.** \( \nQ \) is Archimedean (@thm-rationals-archimedean), and \( 2 \) has no square root in it (@thm-no-rational-square-two).

(c) **False.** \( S \coloneqq \{ 1 - 1/n : n \in \nZ_{>0} \} \) has supremum \( 1 \) (@exm-cof-sup-one-minus-reciprocals), and \( 1 \notin S \), since every element is strictly below \( 1 \).

(d) **True.** Complete the square: \( x^2 + x = (x + 1/2)^2 - 1/4 \). So put \( x \coloneqq \sqrt{a + 1/4} - 1/2 \), which exists because \( a + 1/4 > 0 \). Then \( x^2 + x = (a + 1/4) - 1/4 = a \). And \( x > 0 \): \( a + 1/4 > 1/4 = (1/2)^2 \), and both \( \sqrt{a + 1/4} \) and \( 1/2 \) are non-negative, so \( \sqrt{a + 1/4} > 1/2 \) by @prp-ordered-ring-rules (g).

(e) **False.** Take \( S \) as in (c) and \( c \coloneqq 1 \): every element of \( S \) is below \( 1 \), and \( \sup S = 1 \). The true statement is \( \sup S \le c \), by (S2), since \( c \) is an upper bound of \( S \).
:::

### C. Going deeper

::: {#exr-completeness-and-archimedes-c1}
[C1: An Archimedean field is no larger than the subsets of the rationals]

Let \( F \) be an Archimedean ordered field. Prove that the map \( F \to \powerset{\nQ} \), \( x \mapsto \nQ_F(x) \), is injective. What does this say about the size of \( F \)?
:::

::: {.solution}
Let \( x, y \in F \) with \( \nQ_F(x) = \nQ_F(y) \). By @lem-cof-rationals-separate, \( x = y \). So the map is injective (@fd2:def-injective).

An injection \( F \to \powerset{\nQ} \) says that \( F \) has at most as many elements as \( \powerset{\nQ} \), in the sense of *Sets and Functions*, Chapter 4. In particular every Archimedean ordered field, and so (by @thm-cof-complete-archimedean) every complete ordered field, is no larger than the set of all sets of rationals. The non-Archimedean field \( \nQ(t) \) shows that the hypothesis is needed for injectivity: \( t \) and \( t + 1 \) have the same image.
:::

::: {#exr-completeness-and-archimedes-c2}
[C2: Find the error]

Here is a "proof" that a complete ordered field \( F \) is Archimedean.

> Suppose that \( \iota_F(\nN) \) is bounded above, and let \( s \) be its supremum. Since \( s \) is the least upper bound of \( \iota_F(\nN) \), it is the largest element of \( \iota_F(\nN) \), so \( s = \iota_F(m) \) for some \( m \in \nN \). But \( \iota_F(m + 1) > s \), a contradiction.

Is the conclusion true? Find the line that fails, give a counterexample to that line, and repair the proof.
:::

::: {.solution}
The conclusion is true: it is @thm-cof-complete-archimedean.

The illegal step is "the least upper bound of a set is its largest element". A supremum is an upper bound that lies below every other upper bound (@fd2:def-order-supremum); nothing says it belongs to the set. Counterexample to the step: in the constructed \( \nR \), \( A \coloneqq \{ 1 - 1/n : n \in \nZ_{>0} \} \) has supremum \( 1 \), and \( 1 \notin A \). Indeed every element is \( < 1 \); and if \( b < 1 \), Archimedes in \( \nR \) (@thm-constructed-reals-archimedean, with @prp-archimedean-reciprocal) gives \( n \in \nZ_{>0} \) with \( 1/n < 1 - b \), so \( 1 - 1/n > b \) and \( b \) is not an upper bound. So the step fails for this set, though the theorem's conclusion is not affected.

Repair: replace the second and third sentences by the argument of the proof of @thm-cof-complete-archimedean. Since \( s - 1 < s \), \( s - 1 \) is not an upper bound, so \( \iota_F(n) > s - 1 \) for some \( n \); then \( \iota_F(n + 1) = \iota_F(n) + 1 > s \), against \( s \) being an upper bound. The repair uses that \( s \) is **least** only through "\( s - 1 \) is not an upper bound", which hands us an element of the set just below \( s \), not \( s \) itself.

**Marking scheme.** (10 points)
- 3: says the conclusion is true, with the reason (the theorem).
- 3: names the line "the supremum is the largest element" and says which property of suprema it wrongly assumes.
- 2: a counterexample **to that step**: a set whose supremum is not an element of it, with the supremum verified.
- 2: a correct repair that uses that \( s \) is **least**, without assuming \( s \) lies in the set: for example, \( s - 1 \) is not an upper bound, so some \( \iota_F(n) > s - 1 \) and then \( \iota_F(n + 1) > s \); or, equivalently, if \( \iota_F(n + 1) \le s \) for all \( n \) then \( s - 1 \) is a smaller upper bound (the case \( n = 0 \) uses \( 1 \le s \)).
Fatal errors (0 for the step): declaring the conclusion false; a counterexample to the theorem rather than to the step.
:::

<!-- dependency ledger
def-cof-order-preserving-map (claim): strictly increasing implies injective and order-reflecting | (O1) of def-ordered-ring-and-field; inline
def-cof-order-preserving-map (example): x -> 2x and x -> -x on Q fail the unit and product clauses | arithmetic in Q; inline
def-cof-order-preserving-map (claim): the zero map preserves + and . but not 1; 1_L != 0_L in a field | def-commutative-ring-and-field (1 != 0); inline
def-cof-order-preserving-map (claim): the unit clause follows from additivity, multiplicativity and strict increase (chi(0) = 0, chi(1) > 0, chi(1) = chi(1)^2) | field cancellation (lem-field-fraction-rules (d)); inline, fold only
def-cof-order-preserving-map (claim): pointers to Algebraic Preliminaries, Chapter 2 (conjugation of Q(sqrt 2)) and to Section 6.3 | prose pointers; nothing depends on them
thm-cof-complete-archimedean (proof): "not an upper bound" gives n with n * 1_F > s - 1, and n * 1_F > x for each x once iota_F(N) is not bounded above | totality (prp-ordered-field-halves (a)), fd1:prp-bounded-quantifier-negation (a); inline
thm-cof-complete-archimedean (proof): s - 1 < s; (s - 1) + 1 = s | (O3), field arithmetic; inline
exm-cof-sup-one-minus-reciprocals (solution): iota_F(1 - 1/n) < 1_F; iota_F(1/N) = 1/(N * 1_F); iota_F(1 - 1/N) = 1_F - 1/(N * 1_F) | thm-rationals-embed-ordered-field (sums, products, strictly increasing, iota_F(n) = n * 1_F), lem-field-fraction-rules (a); inline
exm-cof-sup-one-minus-reciprocals (solution): some 1/(N * 1_F) < 1_F - b for b < 1_F; then 1_F - 1/(N * 1_F) > b | thm-cof-complete-archimedean, prp-archimedean-reciprocal, (O3), totality (prp-ordered-field-halves (a)), fd2:def-order-supremum
thm-cof-complete-archimedean (solution): iota_F(Z) is not bounded below (k = -n gives -b >= n * 1_F) | thm-cof-complete-archimedean, prp-ordered-ring-rules (a); inline
exm-cof-sup-one-minus-reciprocals (claim): the same answer holds in any Archimedean field such as Q | the solution uses completeness only through thm-cof-complete-archimedean; thm-rationals-archimedean; remark, nothing depends on it
thm-cof-complete-archimedean (claim): Q(t) is not Archimedean | exm-rational-function-field (school polynomial algebra, flagged there); counterexample only
thm-cof-complete-archimedean (claim): Cauchy-complete need not imply Archimedean | stated without proof (AN1.11 returns to it); nothing depends on it
def-cof-rationals-below (claim): closed downward; x <= y gives inclusion | iota_F strictly increasing (thm-rationals-embed-ordered-field), transitivity (O2); inline
exm-cof-rationals-below-sqrt2 (solution): kappa(q) >= 0 for q >= 0; kappa(0) = 0 | thm-rational-embedding (a), (b)
lem-cof-rationals-separate (proof): antisymmetry of <= | prp-ordered-field-halves (a) (total order)
lem-cof-rationals-separate (claim): Q_{Q(t)}(t) = Q = Q_{Q(t)}(t + 1) | exm-rational-function-field (school polynomial algebra, flagged; fold, counterexample only), thm-rationals-archimedean
prp-cof-square-roots (proof): (s + h)^2 <= s^2 + h(2s + 1) for 0 < h <= 1, s >= 0; (s - h)^2 = a + h^2 for h = (s^2 - a)/(2s); s - h = (s^2 + a)/(2s); a + 1 bounds S | field arithmetic, prp-ordered-ring-rules (b), (c); inline; verify/ch06/prp-cof-square-roots.py
prp-cof-square-roots (proof): h <= 1 and h > 0 give h^2 <= h; y > 1 gives y^2 > y | prp-ordered-ring-rules (c); inline
prp-cof-square-roots (proof): h = (s^2 - a)/(2s) > 0 and s - h = (s^2 + a)/(2s) > 0 | prp-reciprocal-order (a), (O4); inline
prp-cof-square-roots (proof): b = -c <= 0 <= b forces b = 0 | prp-ordered-ring-rules (a), antisymmetry; inline
prp-cof-square-roots (claim): Q(sqrt 2) is Archimedean and lacks square roots | Algebraic Preliminaries, Chapter 2; prose pointer, nothing depends on it
exm-method-point-as-supremum (claim): the template covers square roots, exm-cof-separating-element, the map of Section 6.2 and Exercise C3 of Section 6.3 | prose pointers to later sections of this chapter; fd2:exm-method-construct-and-verify; nothing depends on them
exm-cof-separating-element (solution): sup A exists and a <= sup A <= b | def-complete-ordered-field, fd2:def-order-supremum (S1), (S2); inline
exm-cof-separating-element (solution): a <= c, c' <= b gives |c - c'| <= b - a | prp-ordered-ring-rules (a), (b), prp-absolute-value-ordered-field (d); inline; verify/ch06/exm-cof-separating-element.py
exm-cof-separating-element (solution): every rational upper bound of {p^2 < 2} lies in {p > 0, p^2 > 2}; a separating rational would be sup A in Q | thm-no-rational-square-two, thm-rationals-gap-sqrt2 (a), fd2:def-order-supremum; inline
exr-completeness-and-archimedes-a1 (solution): admissible order (v)(iii)(viii)(vi)(i)(iv) | inline
exr-completeness-and-archimedes-a1 (solution): sup of the negative elements is 0 | first example after def-complete-ordered-field
exr-completeness-and-archimedes-b1 (solution): iota_F(1/n) = 1/(n * 1_F) | thm-rationals-embed-ordered-field (products, iota_F(n) = n * 1_F), lem-field-fraction-rules (a); inline
exr-completeness-and-archimedes-b1 (solution): some 1/(N * 1_F) < c for c > 0 | thm-cof-complete-archimedean, prp-archimedean-reciprocal
exr-completeness-and-archimedes-b3 (solution): (a) r != -r, both square to a, b < 0 gives -b = r | prp-cof-square-roots (uniqueness), prp-ordered-ring-rules (e); verify/ch06/exr-completeness-and-archimedes-b3.py
exr-completeness-and-archimedes-b3 (solution): (b) Q Archimedean without sqrt 2 | thm-rationals-archimedean, thm-no-rational-square-two
exr-completeness-and-archimedes-b3 (solution): (c), (e) sup{1 - 1/n} = 1 not attained; sup S <= c | exm-cof-sup-one-minus-reciprocals, fd2:def-order-supremum (S2)
exr-completeness-and-archimedes-b3 (solution): (d) (x + 1/2)^2 - 1/4 = x^2 + x; sqrt(a + 1/4) > 1/2 | field arithmetic, prp-cof-square-roots, prp-ordered-ring-rules (g); verify/ch06/exr-completeness-and-archimedes-b3.py
exr-completeness-and-archimedes-c1 (solution): an injection F -> P(Q) means |F| <= |P(Q)| | fd2 Chapter 4 (prose only, no proof uses it)
exr-completeness-and-archimedes-c2 (solution): sup{1 - 1/n : n >= 1} = 1 in R, not attained | thm-constructed-reals-archimedean, prp-archimedean-reciprocal; inline
-->
