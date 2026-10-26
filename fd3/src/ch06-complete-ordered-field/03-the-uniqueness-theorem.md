# Two Complete Ordered Fields, One Isomorphism

Section 6.2 built, from an Archimedean ordered field \( F \) into a complete one \( L \), **exactly one** order-preserving field map \( \varphi \), and it keeps the rationals below each element: \( \nQ_L(\varphi(x)) = \nQ_F(x) \) (property \( (\star) \) of @thm-cof-embedding-into-complete). This section takes both fields complete. Then maps run both ways, and the word "exactly" makes them inverse to each other. So any two complete ordered fields are copies of each other, by one isomorphism; the only symmetry of a complete ordered field is the identity; and every first-order statement about sums, products and order has the same truth value in all of them. The section ends with what this means for the two ways to begin analysis.

## The uniqueness theorem

Section 6.2 gave us, for complete \( F \) and \( L \), a map \( \varphi \colon F \to L \). It did not say that \( \varphi \) is onto. A map can preserve everything in sight and still miss most of its target: the map \( \iota_{\nR} \colon \nQ \to \nR \) preserves sums, products and order (@thm-rationals-embed-ordered-field), and the real number \( r \) of @exm-sqrt2-class, whose square is \( 2 \), is not in its image. What rules this out when the source is complete as well?

::: {#thm-cof-uniqueness}
[Uniqueness of the Complete Ordered Field]

Let \( F \) and \( L \) be complete ordered fields (@def-complete-ordered-field). Then there is **exactly one** order-preserving field isomorphism \( F \to L \) (@def-cof-order-preserving-map). It is the map \( \varphi \) of @thm-cof-embedding-into-complete.
:::

::: {.idea}
Section 6.2 runs in both directions. Since \( F \) is complete, it is Archimedean (@thm-cof-complete-archimedean), so it is a legal source; since \( L \) is complete, it is a legal target. That gives \( \varphi \colon F \to L \). Swapping the roles gives \( \psi \colon L \to F \).

To show that \( \psi \) undoes \( \varphi \), we could try to compute \( \psi(\varphi(x)) \) from the two suprema. We do not have to. The composite \( \psi \circ \varphi \colon F \to F \) is again an order-preserving field map, and so is the identity of \( F \). The uniqueness clause of @thm-cof-embedding-into-complete, applied with \( F \) as source **and** as target, says there is only one such map. So the two are equal. **Uniqueness gives inverses.** (This is the pattern of @fd2:exm-method-uniqueness: two objects with the same defining property are equal.)

*Before reading on: self-explain why \( \psi \circ \varphi \) is order-preserving. Which of the four conditions of @def-cof-order-preserving-map needs more than one line?*
:::

::: {.proof}
Let \( F \) and \( L \) be complete ordered fields. By @thm-cof-complete-archimedean, each of them is Archimedean.

*The two maps.* Since \( F \) is Archimedean and \( L \) is complete, @thm-cof-embedding-into-complete gives an order-preserving field map \( \varphi \colon F \to L \). Since \( L \) is Archimedean and \( F \) is complete, the same theorem, with the roles of the two fields exchanged, gives an order-preserving field map \( \psi \colon L \to F \).

*The composite \( \psi \circ \varphi \) is an order-preserving field map \( F \to F \).* For \( a, b \in F \), additivity of \( \varphi \) and then of \( \psi \) gives
\[
\psi(\varphi(a + b)) = \psi(\varphi(a) + \varphi(b)) = \psi(\varphi(a)) + \psi(\varphi(b)) ,
\]
and the same two steps with products give \( \psi(\varphi(ab)) = \psi(\varphi(a)) \, \psi(\varphi(b)) \). Also \( \psi(\varphi(1)) = \psi(1) = 1 \). If \( a < b \), then \( \varphi(a) < \varphi(b) \), since \( \varphi \) is strictly increasing, and then \( \psi(\varphi(a)) < \psi(\varphi(b)) \), since \( \psi \) is.

*The composite is the identity.* The identity map \( \id_F \) is an order-preserving field map \( F \to F \): each of the four conditions reads \( u = u \) or \( a < b \Rightarrow a < b \). Now apply @thm-cof-embedding-into-complete with source \( F \), which is Archimedean, and target \( F \), which is complete: there is **exactly one** order-preserving field map \( F \to F \). Both \( \psi \circ \varphi \) and \( \id_F \) are such maps, so \( \psi \circ \varphi = \id_F \).

Exchanging the roles of \( F \) and \( L \), the same argument gives \( \varphi \circ \psi = \id_L \).

*Existence.* So \( \psi \) is a two-sided inverse of \( \varphi \), and \( \varphi \) is bijective by @fd2:thm-bijection-iff-inverse. Hence \( \varphi \) is an order-preserving field isomorphism \( F \to L \).

*Uniqueness.* Let \( \chi \colon F \to L \) be any order-preserving field isomorphism. Forgetting that it is bijective, \( \chi \) is an order-preserving field map \( F \to L \), and by the uniqueness clause of @thm-cof-embedding-into-complete there is only one such map. Hence \( \chi = \varphi \). This proves the theorem.
:::

The answer to the prompt: each of the four conditions passes through a composite in one line, the order condition in two (\( a < b \) gives \( \varphi(a) < \varphi(b) \), which \( \psi \) accepts). The weight of the proof sits in the uniqueness clause, used three times: for \( \psi \circ \varphi \), for \( \varphi \circ \psi \), and for \( \chi \).

A direct proof that \( \varphi \) is onto, computing a supremum in \( F \), is Exercise C2 of Section 6.2.

::: {.check}
Why could the proof not simply **define** \( \psi \coloneqq \varphi^{-1} \), instead of building \( \psi \) from @thm-cof-embedding-into-complete?
:::

::: {.solution}
The inverse \( \varphi^{-1} \colon L \to F \) exists only if \( \varphi \) is bijective (@fd2:thm-bijection-iff-inverse), and bijectivity is what the theorem is trying to prove. Section 6.2 gives \( \varphi \) as an injective map (it is strictly increasing), with no claim that it is onto. The map \( \psi \) is built independently of \( \varphi \), and only afterwards shown to be its inverse.
:::

Each hypothesis has a job. Completeness of \( L \) makes it a target, so \( \varphi \) exists; completeness of \( F \) makes it a target, so \( \psi \) exists; and completeness of each gives the Archimedean property that makes it a source. Drop the completeness of \( F \), and the conclusion fails: for \( F = \nQ \), \( L = \nR \), the only order-preserving field map is \( \iota_{\nR} \), which is not onto.

## One real line

The theorem says that two complete ordered fields have the same shape, with a unique dictionary between them. We want a short way to write the first half of that sentence.

*Two ordered fields are the same up to relabeling when an order-preserving bijection respects the arithmetic.*

For ordered fields \( F \) and \( L \), write
\[
F \cong L
\]
when there is **an** order-preserving field isomorphism \( F \to L \) (@def-cof-order-preserving-map). Read it "\( F \) is isomorphic to \( L \)", with "as ordered fields" understood.

**Examples.**

- \( \nR \cong \nR \), by \( \id_{\nR} \). Any ordered field is isomorphic to itself in the same way.
- \( F \cong \nR \) for every complete ordered field \( F \), where \( \nR \) is the field of Chapter 5. This is the corollary below.
- \( \nQ \not\cong \nR \). An isomorphism \( \chi \colon \nQ \to \nR \) would fix the rationals (@prp-cof-map-fixes-rationals, with \( \iota_{\nQ} = \id_{\nQ} \) by the uniqueness clause of @thm-rationals-embed-ordered-field), so \( \chi = \iota_{\nR} \), and \( \iota_{\nR} \) is not onto (@exm-sqrt2-class).

::: {#cor-cof-isomorphic-to-cauchy-reals}
[Every Complete Ordered Field Is a Copy of the Reals]

Let \( F \) be a complete ordered field, and let \( \nR \) be the field of Chapter 5. Then \( F \cong \nR \): there is **exactly one** order-preserving field isomorphism \( F \to \nR \).
:::

::: {.proof}
By @thm-reals-complete-ordered-field, \( \nR \) is a complete ordered field. Apply @thm-cof-uniqueness with \( L = \nR \).
:::

So "the real numbers" names one ordered field up to a unique relabeling. A statement about sums, products and order is then true in \( F \) exactly when it is true in \( \nR \); the subsection *What the isomorphism carries* below makes this precise for first-order statements and shows it at work on limits.

::: {.second-reading title="Why isomorphism is an equivalence relation"}
On any set \( \mathcal S \) of ordered fields, \( \cong \) is an equivalence relation (@fd2:def-equivalence-relation): it is reflexive, symmetric and transitive. No proof in this subsection uses its symmetry or transitivity; this paragraph records that the word "isomorphic" behaves as the word "equal" suggests. The symmetric clause is used below: the inverse of the isomorphism of @thm-cof-uniqueness is again one.

*Reflexive.* \( \id_F \) is an order-preserving field isomorphism \( F \to F \).

*Symmetric.* Let \( \chi \colon F \to L \) be an order-preserving field isomorphism, and let \( \chi^{-1} \colon L \to F \) be its two-sided inverse (@fd2:thm-bijection-iff-inverse); it is bijective by the same theorem. For \( u, v \in L \), additivity of \( \chi \) gives
\[
\chi\bigl( \chi^{-1}(u) + \chi^{-1}(v) \bigr) = \chi(\chi^{-1}(u)) + \chi(\chi^{-1}(v)) = u + v = \chi\bigl( \chi^{-1}(u + v) \bigr) ,
\]
and since \( \chi \) is injective, \( \chi^{-1}(u + v) = \chi^{-1}(u) + \chi^{-1}(v) \). The same lines with products give \( \chi^{-1}(uv) = \chi^{-1}(u) \chi^{-1}(v) \), and \( \chi(1) = 1 \) gives \( \chi^{-1}(1) = 1 \). Finally, let \( u < v \). Then \( \chi(\chi^{-1}(u)) < \chi(\chi^{-1}(v)) \), and since \( \chi \) reflects order, \( \chi^{-1}(u) < \chi^{-1}(v) \).

*Transitive.* If \( \chi \colon F \to L \) and \( \chi' \colon L \to M \) are order-preserving field isomorphisms, then \( \chi' \circ \chi \) is bijective (@fd2:thm-composition-injective-surjective), and it is an order-preserving field map by the computation in the proof of @thm-cof-uniqueness for \( \psi \circ \varphi \), which used nothing but the four conditions for each factor.
:::

::: {#exm-cof-two-models}
[Two Models, One Square Root of Two]

Let \( M \) be any complete ordered field (for instance the one *Axiomatic Set Theory* builds, whose elements are sets of rationals). Let \( \varphi \colon \nR \to M \) be the isomorphism of @thm-cof-uniqueness and \( r \) the real number of @exm-sqrt2-class (\( r > 0 \), \( r^2 = 2 \)). Find \( \varphi(r) \) in terms of \( M \) alone, and describe \( \nQ_M(\varphi(r)) \).
:::

::: {.solution}
*The image of \( r \).* Since \( \varphi \) is multiplicative and fixes the rationals (@prp-cof-map-fixes-rationals), \( \varphi(r)^2 = \varphi(r^2) = \varphi(\iota_{\nR}(2)) = \iota_M(2) \). Since \( \varphi \) is strictly increasing and \( r > 0 \), \( \varphi(r) > \varphi(0) = 0 \) (\( \varphi \) fixes the rational \( 0 \), @prp-cof-map-fixes-rationals). By @prp-cof-square-roots in the complete field \( M \), there is exactly one \( b \ge 0 \) in \( M \) with \( b^2 = \iota_M(2) \). So \( \varphi(r) \) is that \( b \): the square root of \( 2 \) in \( M \), however \( M \) was built.

*The rationals below it.* By \( (\star) \) of @thm-cof-embedding-into-complete, \( \nQ_M(\varphi(r)) = \nQ_{\nR}(r) \). By @exm-cof-rationals-below-sqrt2 this is the set of rationals \( q \) with \( q < 0 \), or with \( q \ge 0 \) and \( q^2 < 2 \). The same set of rationals sits below \( \sqrt 2 \) in both models.

The set \( \nQ_F(x) \) of an element \( x \) of an Archimedean ordered field \( F \) always has four properties. It is non-empty: some \( n \in \nN \) has \( -x < n \cdot 1_F \), so \( -n \in \nQ_F(x) \). It is not all of \( \nQ \): some \( m \) has \( x < m \cdot 1_F \), so \( m \notin \nQ_F(x) \). It is closed downward (Section 6.1). It has no largest element: for \( q \in \nQ_F(x) \), density (@thm-rationals-dense-ordered-field) gives \( p \in \nQ \) with \( \iota_F(q) < \iota_F(p) < x \). A set of rationals with these four properties is called a **Dedekind cut**. *Axiomatic Set Theory*, Chapter 1 takes the cuts themselves as the real numbers, proves that they form a complete ordered field, and shows that there the rationals below a cut \( c \) are exactly the elements of \( c \). By @thm-cof-uniqueness that field is one more copy of \( \nR \); by \( (\star) \) the copy of a real number \( y \) has the same rationals below it as \( y \), so the copy of \( y \) is the cut \( \nQ_{\nR}(y) \).
:::

## Automorphisms

An isomorphism from a field to itself is a symmetry: a relabeling that leaves the arithmetic unchanged. The uniqueness theorem rules out every symmetry of a complete ordered field that respects the order; the theorem after it rules out every symmetry.

::: {#cor-cof-order-automorphism-identity}
[A Complete Ordered Field Has Only the Trivial Order Automorphism]

Let \( F \) be a complete ordered field. The only order-preserving field automorphism of \( F \) is \( \id_F \). In particular, this holds for the field \( \nR \) of Chapter 5.
:::

::: {.proof}
\( F \) is Archimedean by @thm-cof-complete-archimedean and complete by hypothesis, so by @thm-cof-embedding-into-complete with source and target \( F \) there is exactly one order-preserving field map \( F \to F \). The identity is one, and every order-preserving field automorphism is one. So every such automorphism is \( \id_F \). For \( \nR \), use @thm-reals-complete-ordered-field.
:::

The corollary assumes that the map respects the order. Can a map that only respects the arithmetic move anything?

::: {#thm-cof-field-automorphism-identity}
[Field Maps of a Complete Ordered Field to Itself]

Let \( F \) be a complete ordered field, and let \( \sigma \colon F \to F \) satisfy, for all \( a, b \in F \),
\[
\sigma(a + b) = \sigma(a) + \sigma(b) , \qquad \sigma(ab) = \sigma(a) \sigma(b) , \qquad \sigma(1) = 1 .
\]
Then \( \sigma = \id_F \). No order condition and no bijectivity is assumed.
:::

*Try it first (ten minutes): why must such a \( \sigma \) send positive elements to positive elements? Look for a description of "positive" that uses only multiplication.*

::: {.idea}
The order condition has to be **recovered** from the arithmetic. In a complete ordered field, positivity has a description in terms of multiplication alone: an element is positive exactly when it is a non-zero square (@prp-cof-square-roots gives the square root). A map that respects products sends squares to squares, and squares in an ordered field are never negative. Then additivity turns "positives go to positives" into "\( \sigma \) is strictly increasing", and the uniqueness clause of @thm-cof-embedding-into-complete finishes, as in the corollary's proof (which never uses bijectivity).

Plan: ① positive to positive, through a square root; ② strictly increasing, through differences; ③ the uniqueness clause.

*Before reading on: which line of the proof below needs completeness, and which would work in any ordered field?*
:::

::: {.proof}
**Step 1: \( \sigma \) sends positive elements to positive elements.** Let \( a \in F \) with \( a > 0 \). By @prp-cof-square-roots there is \( b \in F \) with \( b \ge 0 \) and \( b^2 = a \). Then \( b \ne 0 \), since \( 0^2 = 0 \ne a \) (@prp-ring-algebra (b)). So \( b \) has an inverse \( b^{-1} \), and
\[
\sigma(b) \, \sigma(b^{-1}) = \sigma(b b^{-1}) = \sigma(1) = 1 .
\]
If \( \sigma(b) = 0 \), the left side would be \( 0 \) (@prp-ring-algebra (b)), and \( 0 \ne 1 \) in the field \( F \) (@def-commutative-ring-and-field). Hence \( \sigma(b) \ne 0 \), and
\[
\sigma(a) = \sigma(b b) = \sigma(b)^2 > 0
\]
by @prp-ordered-ring-rules (e): a non-zero square is positive.

**Step 2: \( \sigma \) is strictly increasing.** First, \( \sigma(-c) = -\sigma(c) \) for every \( c \in F \): additivity gives \( \sigma(c) + \sigma(-c) = \sigma(c + (-c)) = \sigma(0) \), and \( \sigma(0) = \sigma(0 + 0) = \sigma(0) + \sigma(0) \) gives \( \sigma(0) = 0 \); so \( \sigma(-c) \) is the negative of \( \sigma(c) \) (@prp-ring-algebra (a)). Now let \( x < y \) in \( F \). Then \( y - x > 0 \) (@prp-ordered-ring-rules (a)), so by Step 1
\[
\sigma(y) - \sigma(x) = \sigma(y) + \sigma(-x) = \sigma(y - x) > 0 ,
\]
and \( \sigma(x) < \sigma(y) \) by @prp-ordered-ring-rules (a).

**Step 3: \( \sigma = \id_F \).** By Step 2 and the hypotheses, \( \sigma \) is an order-preserving field map \( F \to F \) (@def-cof-order-preserving-map). The field \( F \) is Archimedean by @thm-cof-complete-archimedean, and complete by hypothesis. By the uniqueness clause of @thm-cof-embedding-into-complete, with source and target \( F \), there is exactly one order-preserving field map \( F \to F \); the identity is one. Hence \( \sigma = \id_F \).
:::

The answer to the prompt: only the first line of Step 1, "there is \( b \) with \( b^2 = a \)", and Step 3 need completeness; every other line of Steps 1 and 2 works in any ordered field.

Completeness entered twice: it supplied square roots in Step 1, and, through @thm-cof-complete-archimedean, the Archimedean property that the uniqueness clause in Step 3 needs (by the remark after its proof in Section 6.2, an Archimedean target suffices there).

::: {.remark}
**What each hypothesis buys.** Without the order condition, a bijection that respects sums, products and \( 1 \) can reverse signs: *Algebraic Preliminaries*, Chapter 2 meets \( \nQ(\sqrt 2) \), an Archimedean field that is not complete, which has one exchanging \( \sqrt 2 \) and \( -\sqrt 2 \). The theorem above shows that this cannot happen in a complete ordered field. Without the Archimedean property, an order-preserving automorphism can move elements: in \( \nQ(t) \) of @exm-rational-function-field, \( t \mapsto t + 1 \) keeps degrees and leading coefficients (school polynomial algebra, as flagged there). And \( \nQ \) has only the identity (Exercise B1), although it is not complete: there is nothing besides rationals to move.
:::

::: {.second-reading title="Maps that ignore the order"}
Steps 1 and 2 used two things only: square roots of positive elements in the **source**, and the rule "non-zero squares are positive" in the **target**. If \( F \) is a complete ordered field, \( L \) is any ordered field, and \( \chi \colon F \to L \) satisfies \( \chi(a + b) = \chi(a) + \chi(b) \), \( \chi(ab) = \chi(a) \chi(b) \) and \( \chi(1) = 1 \), then \( \chi \) is strictly increasing, that is, an order-preserving field map. In particular, for complete ordered fields \( F \) and \( L \), every bijection \( F \to L \) that respects sums, products and \( 1 \) is the isomorphism of @thm-cof-uniqueness.
:::

## What the isomorphism carries

Throughout this subsection \( F \) and \( L \) are complete ordered fields and \( \varphi \colon F \to L \) is the isomorphism of @thm-cof-uniqueness. The definition gives sums, products, \( 1 \) and order; five more facts follow in a line each. Within this subsection, (T1)–(T5) name them.

::: {.enumerate options="label=(T\arabic*)"}
1. \( \varphi(0) = 0 \), \( \varphi(-x) = -\varphi(x) \), \( \varphi(x - y) = \varphi(x) - \varphi(y) \), and \( \varphi(x^{-1}) = \varphi(x)^{-1} \) for \( x \ne 0 \). Indeed \( \varphi(0) = \varphi(0 + 0) = \varphi(0) + \varphi(0) \), and adding \( -\varphi(0) \) gives \( \varphi(0) = 0 \); then \( \varphi(x) + \varphi(-x) = \varphi(0) = 0 \); and \( \varphi(x)\varphi(x^{-1}) = \varphi(1) = 1 \).
2. \( x < y \) **if and only if** \( \varphi(x) < \varphi(y) \): the forward direction is the definition, and the backward one is the reflection of order shown just after @def-cof-order-preserving-map. With (T1), \( x > 0 \) if and only if \( \varphi(x) > 0 \).
3. \( \varphi(\abs{x}) = \abs{\varphi(x)} \). If \( x \ge 0 \), then \( \varphi(x) \ge 0 \) by (T2), and both sides are \( \varphi(x) \). If \( x < 0 \), then \( \varphi(x) < 0 \), and both sides are \( \varphi(-x) = -\varphi(x) \) (@def-absolute-value-ordered-field, (T1)).
4. \( \varphi(\iota_F(q)) = \iota_L(q) \) for every \( q \in \nQ \) (@prp-cof-map-fixes-rationals): each rational goes to the same rational.
5. The inverse \( \varphi^{-1} \colon L \to F \) is again an order-preserving field isomorphism (the fold after @cor-cof-isomorphic-to-cauchy-reals). So everything said about \( \varphi \) holds for \( \varphi^{-1} \) too.
:::

The map acts on larger objects through their elements: a subset \( A \) goes to \( \varphi(A) \), a sequence \( (a_n) \) to \( (\varphi(a_n)) \), a function \( f \) to \( \varphi \circ f \circ \varphi^{-1} \), and every such object of \( L \) comes from exactly one of \( F \).

*An isomorphism is a renaming: it changes what the elements are called and keeps every relation between them.*

Here is the renaming at work on a statement with three quantifiers.

::: {#exm-cof-limits-carried-across}
[Limits Are Carried Across]

Let \( (a_n) \) be a sequence in \( F \) and \( a \in F \). Show that \( a_n \to a \) in \( F \) (@def-sequence-limit-ordered-field) if and only if \( \varphi(a_n) \to \varphi(a) \) in \( L \).
:::

::: {.solution}
For (\( \Rightarrow \)), let \( \varepsilon \in L_{>0} \), and put \( \varepsilon' \coloneqq \varphi^{-1}(\varepsilon) \). Then \( \varepsilon' > 0 \) by (T2), since \( \varphi(\varepsilon') = \varepsilon > 0 \). Since \( a_n \to a \), there is \( N \in \nN \), depending on \( \varepsilon' \) and so on \( \varepsilon \), with \( \abs{a_n - a} < \varepsilon' \) for every \( n \ge N \). For such \( n \), by (T1), (T3) and (T2),
\[
\abs{\varphi(a_n) - \varphi(a)} = \varphi\bigl(\abs{a_n - a}\bigr) < \varphi(\varepsilon') = \varepsilon .
\]
So \( \varphi(a_n) \to \varphi(a) \). For (\( \Leftarrow \)), apply (\( \Rightarrow \)) to \( \varphi^{-1} \), which is allowed by (T5).
:::

The step that needs \( \varphi \) to be **onto** is the first: the tolerance \( \varepsilon \) lives in \( L \), and the hypothesis speaks of tolerances in \( F \). For a map that is not onto the transfer can fail: the Newton sequence has no limit in \( \nQ \) (@thm-sqrt2-cauchy-no-rational-limit), while its copy under \( \iota_{\nR} \) converges in \( \nR \) (Exercise B3 of Section 5.4).

The example is one case of a general fact. The ordered field \( F \), with \( + \), \( \cdot \), \( 0 \), \( 1 \) and \( < \), is a structure in the sense of *Logic and Proof*, Chapter 7, and \( \varphi \) is an isomorphism of structures: a bijection that respects every symbol. By @fd1:thm-isomorphism-invariance, every first-order sentence in these symbols (@fd1:def-first-order-formula) is true in \( F \) exactly when it is true in \( L \). Statements that also quantify over subsets, sequences or functions are not first-order sentences of this kind; for those, the renaming above is checked case by case, as in the example: one renaming per object, and onto for each quantifier. We do not state a general theorem for them.

::: {.check}
Let \( F \), \( L \) and \( \varphi \) be as above, and suppose some \( x \in F \) satisfies \( x^3 = x + 1 \). Show that some \( y \in L \) satisfies \( y^3 = y + 1 \).
:::

::: {.solution}
Take \( y \coloneqq \varphi(x) \). By @def-naturals-in-ordered-field (b), \( x^3 = ((1 \cdot x) x) x \), and \( \varphi \) respects \( 1 \) and products, so \( \varphi(x^3) = \varphi(x)^3 \). Hence \( y^3 = \varphi(x^3) = \varphi(x + 1) = \varphi(x) + \varphi(1) = y + 1 \).
:::

The renaming keeps relations between elements. It does not keep what the elements are made of.

::: {#exm-cof-zero-empty-set}
[A Complete Ordered Field Whose Zero Is the Empty Set]

Find a complete ordered field whose zero element is \( \emptyset \).
:::

::: {.solution}
In the Cauchy model the zero is \( [(0)_n] \), a class that contains the constant sequence, so it is not \( \emptyset \). Let \( X \coloneqq (\nR \setminus \{0_{\nR}\}) \cup \{\emptyset\} \) and \( \beta \colon \nR \to X \), \( \beta(0_{\nR}) \coloneqq \emptyset \), \( \beta(x) \coloneqq x \) otherwise. Every element of \( \nR \) is a class \( [a] \), which contains \( a \) and so is not empty; hence \( \emptyset \notin \nR \), and \( \beta \) is a bijection. Copy the structure of \( \nR \) to \( X \) along \( \beta \):
\[
\begin{aligned}
u \oplus v &\coloneqq \beta\bigl(\beta^{-1}(u) + \beta^{-1}(v)\bigr) , \\
u \odot v &\coloneqq \beta\bigl(\beta^{-1}(u) \, \beta^{-1}(v)\bigr) ,
\end{aligned}
\]
and \( u \prec v \) if and only if \( \beta^{-1}(u) < \beta^{-1}(v) \). Then \( X \) is a complete ordered field, \( \beta \) is an isomorphism, and the zero of \( X \) is \( \beta(0_{\nR}) = \emptyset \). So the statement "the zero element is the empty set" is false in \( \nR \) and true in \( X \), although the two are isomorphic. The statement is about what an element is made of, and no renaming can be expected to keep that.
:::

::: {.second-reading title="Why the copied structure is a complete ordered field"}
With \( u = \beta(a) \) and \( v = \beta(b) \), the definitions read \( \beta(a + b) = \beta(a) \oplus \beta(b) \), \( \beta(ab) = \beta(a) \odot \beta(b) \), and \( a < b \) if and only if \( \beta(a) \prec \beta(b) \). Each axiom for \( X \), rewritten in this way, becomes the same axiom for \( \nR \): for (F1), \( u \oplus v = \beta(a + b) = \beta(b + a) = v \oplus u \); the zero and one of \( X \) are \( \beta(0) \) and \( \beta(1) \), and \( \beta(1) \ne \beta(0) \) because \( \beta \) is injective and \( 1 \ne 0 \) in \( \nR \); (F2)–(F9) and (O1)–(O4) go the same way. For completeness, let \( B \subseteq X \) be non-empty and bounded above by \( w \). Then \( \beta^{-1}(B) \) is non-empty and bounded above by \( \beta^{-1}(w) \), so it has a supremum \( s \) in \( \nR \), and \( \beta(s) \) is a supremum of \( B \), because \( \beta \) and \( \beta^{-1} \) both preserve the order by the definition of \( \prec \).
:::

::: {.warning}
**Isomorphic is not equal.** The isomorphism links two models; it does not make them one set, and it does not make \( \nQ \) a subset of \( \nR \). In the Cauchy model the rational number \( 2 \) is a class of pairs of integers (@def-rationals-as-classes), while the real number \( 2 \) is \( \kappa(2) = [(2)_n] \), a class of sequences (@def-rational-embedding); they are different sets, and, as Section 5.2 noted after @def-reals-cauchy-classes, the rational \( 2 \) is not an element of \( \nR \). "\( \nQ \subseteq \nR \)" is shorthand for the embedding \( \iota_{\nR} \), the one copy of \( \nQ \) that @thm-rationals-embed-ordered-field provides, and every isomorphism respects that copy by (T4).
:::

So "which construction is \( \nR \)?" has no mathematical content: every construction gives a complete ordered field, any two are linked by exactly one isomorphism, and that isomorphism decides every first-order question in \( + \), \( \cdot \), \( < \) (and, case by case, statements about subsets, sequences and functions) in the same way in both. Questions such as "is \( \sqrt 2 \) a set of rationals?" depend on the model, and analysis never asks them.

## Assume the axioms or build a model

**(A) Assume the axioms.** Declare that \( \nR \) is a set with an addition, a multiplication and a relation \( < \) satisfying the field axioms (F1)–(F9) and \( 1 \ne 0 \) of @def-commutative-ring-and-field, the order axioms (O1)–(O4) of @def-ordered-ring-and-field, and completeness, @def-complete-ordered-field: every non-empty subset that is bounded above has a supremum. Then prove theorems from these axioms and nothing else. *Analysis on the Real Line*, Chapter 1 begins this way. It assumes an ordered field containing \( \nQ \) in which the least upper bound axiom holds, and every theorem of that volume about real numbers is proved from this assumption, with the logic and set theory of the earlier volumes.

**(B) Build a model.** Start from sets and construct the objects one by one. This volume did that from a Peano system \( \nN \), whose existence Section 1.5 explains and *Axiomatic Set Theory* proves from the axioms of set theory: the integers and the rationals as classes of pairs (Chapters 2 and 3), and the real numbers as classes of Cauchy sequences of rationals (Chapter 5). The result is a complete ordered field (@thm-reals-complete-ordered-field); once \( \nN \) is given, no property of the result was assumed.

Route (A) is shorter, and it is the route of most analysis courses. On its own, though, it leaves two questions open.

::: {.enumerate options="label=(Q\arabic*)"}
1. *Is there a complete ordered field at all?* A list of axioms can be contradictory: a list of demands that nothing meets. Theorems proved from a contradictory list would all be worthless.
2. *If there are several, which one is \( \nR \)?* Route (A) says "let \( \nR \) be **a** complete ordered field". The article matters.
:::

Route (B) answers (Q1). The Cauchy model of Chapter 5 is a complete ordered field, built inside set theory, from a Peano system. So if a contradiction could be derived from the axioms of a complete ordered field, the same derivation, run in the Cauchy model, would be a contradiction about one particular set built in that set theory. In short, the axioms are consistent if the axioms of set theory are, with a Peano system among the sets (*Axiomatic Set Theory* states the axioms as ZF and builds one). That is the most a construction can give: it moves the question of consistency from the axioms of \( \nR \) to the axioms of set theory.

Route (B) alone does not answer (Q2): a builder who uses Dedekind cuts gets a different set. The answer to (Q2) is @thm-cof-uniqueness, and the previous subsection explained why it is the right answer: one structure, not a family that agrees only on what the axioms prove.

**Theorems need no uniqueness; truth does.** A statement **proved** from the ordered-field axioms holds in every ordered field, but the axioms alone leave statements open: "some \( x \) has \( x \cdot x = 1 + 1 \)" is false in \( \nQ \) (@thm-no-rational-square-two) and true in \( \nR \) (@prp-cof-square-roots), and "some \( y \) lies above every \( n \cdot 1 \)" is false in \( \nR \) (@thm-cof-complete-archimedean) and true in \( \nQ(t) \) (@exm-rational-function-field). For complete ordered fields no such disagreement can occur, whether or not anybody has a proof.

The analysis volume uses route (A). The table matches each of its assumptions with the place where this series supplies or justifies it.

| Assumed in *Analysis on the Real Line*, Chapter 1 | Supplied or justified here |
|---|---|
| \( \nR \) is an ordered field, axioms (F1)–(F9), (O1)–(O4) | the axioms: @def-commutative-ring-and-field, @def-ordered-ring-and-field, in the same numbering (in *Analysis on the Real Line*, (F7) includes \( 1 \ne 0 \); here it is a separate clause of the field definition); a model: @thm-reals-ordered-field |
| \( \nR \) contains \( \nQ \) | every ordered field contains exactly one copy of \( \nQ \): @thm-rationals-embed-ordered-field; isomorphisms respect it: @prp-cof-map-fixes-rationals |
| the least upper bound axiom | the property: @def-complete-ordered-field; a model: @thm-reals-complete-ordered-field |
| "the" real numbers | any two models are isomorphic, by exactly one isomorphism: @thm-cof-uniqueness, @cor-cof-isomorphic-to-cauchy-reals |
| logic and set theory | *Logic and Proof*, *Sets and Functions*; ℕ in Chapter 1 of this volume (Section 1.5 for where it comes from) |

Some results are proved in both volumes, from different starting points. *Analysis on the Real Line*, Chapter 1 proves from its axioms that \( \nN \) is not bounded above, that \( \nQ \) is dense in \( \nR \), and that positive numbers have square roots. Here the same three facts were proved for an arbitrary complete ordered field: @thm-cof-complete-archimedean, @thm-rationals-dense-ordered-field (which needs Archimedes, supplied by the first) and @prp-cof-square-roots. The two volumes start from different places, and neither volume's proofs cite the other's.

This ends the volume. *Analysis on the Real Line* begins from route (A), and this chapter is why that beginning names one structure.

## Exercises

### A. Check your understanding

::: {#exr-the-uniqueness-theorem-a1}
[A1]

Parts (a)–(c) are about the proof of @thm-cof-uniqueness, parts (d)–(g) about @thm-cof-field-automorphism-identity.

::: {.enumerate options="label=(\alph*)"}
1. Where is the completeness of \( F \) used? Name every place.
2. Why is \( \psi \circ \varphi \) order-preserving?
3. Suppose \( F \) is only assumed to be an Archimedean ordered field, and \( L \) is complete. Which step of the proof fails first?
4. Where is completeness of \( F \) used in the proof of @thm-cof-field-automorphism-identity?
5. Why is \( \sigma(b) \ne 0 \) in Step 1?
6. Why does \( \sigma \) fix every rational, although no order hypothesis is made?
7. Let \( \sigma \colon \nR \to \nR \) respect sums and products, with \( \sigma(1) = 1 \), and let \( r \) be the real number of @exm-sqrt2-class (\( r > 0 \), \( r^2 = 2 \)). Without quoting @thm-cof-field-automorphism-identity, show that \( \sigma(r) = r \).
:::
:::

::: {.solution}
(a) In two ways. First, through @thm-cof-complete-archimedean, completeness makes \( F \) Archimedean, so \( F \) is a legal **source** for @thm-cof-embedding-into-complete: for \( \varphi \colon F \to L \), and for the uniqueness clause applied to maps \( F \to F \) such as \( \psi \circ \varphi \). Second, it makes \( F \) a legal **target**, so that \( \psi \colon L \to F \) exists. The uniqueness clause for \( \psi \circ \varphi \) is cited with target \( F \), so as stated it asks for \( F \) complete; but by the remark after its proof in Section 6.2 only the Archimedean property of \( F \) is used there, and the first use already supplies it (as in (d)).

(b) If \( a < b \), then \( \varphi(a) < \varphi(b) \) because \( \varphi \) is strictly increasing, and this strict inequality in \( L \) is a hypothesis \( \psi \) accepts, so \( \psi(\varphi(a)) < \psi(\varphi(b)) \). A composite of strictly increasing maps is strictly increasing.

(c) The construction of \( \psi \colon L \to F \): @thm-cof-embedding-into-complete needs a complete target, and \( F \) is not one. (The map \( \varphi \) still exists.) The conclusion fails too: for \( F = \nQ \) and \( L = \nR \), the only order-preserving field map is \( \iota_{\nR} \), which is not onto.

(d) Twice in substance. In Step 1, @prp-cof-square-roots needs \( F \) complete to give the square root \( b \) of \( a > 0 \), and that is how \( \sigma(a) > 0 \) is proved. In Step 3, @thm-cof-complete-archimedean makes \( F \) Archimedean, which the uniqueness clause of @thm-cof-embedding-into-complete needs of its target (the clause separates elements by rationals in the target, here \( F \), @lem-cof-rationals-separate). Step 3 also cites the completeness of \( F \), because that theorem is stated for a complete target; by the remark after its proof in Section 6.2, the uniqueness clause needs only an Archimedean target, so this is the same use again.

(e) \( b \ne 0 \) has an inverse, and \( \sigma(b) \sigma(b^{-1}) = \sigma(1) = 1 \). If \( \sigma(b) \) were \( 0 \), the left side would be \( 0 \), and \( 0 \ne 1 \) in a field.

(f) By @prp-cof-map-fixes-rationals, whose hypotheses are additivity, multiplicativity and \( \sigma(1) = 1 \) only: the composite \( \sigma \circ \iota_F \colon \nQ \to F \) respects sums and products and fixes \( 1 \), so it is \( \iota_F \) by the uniqueness clause of @thm-rationals-embed-ordered-field. Order plays no part.

(g) \( \sigma(r)^2 = \sigma(r^2) = \sigma(2) = 2 \), since \( \sigma \) fixes the rationals (@prp-cof-map-fixes-rationals). By @prp-cof-square-roots there is \( s \ge 0 \) with \( s^2 = r \), and \( s \ne 0 \) since \( r \ne 0 \). So \( s \) has an inverse, and \( \sigma(s) \sigma(s^{-1}) = \sigma(s s^{-1}) = \sigma(1) = 1 \), which forces \( \sigma(s) \ne 0 \). Hence \( \sigma(r) = \sigma(s)^2 > 0 \) by @prp-ordered-ring-rules (e). So \( \sigma(r) \) and \( r \) are both non-negative square roots of \( 2 \), and the uniqueness part of @prp-cof-square-roots gives \( \sigma(r) = r \).
:::

::: {#exr-axioms-or-model-a1}
[A2]

Throughout, \( F \) and \( L \) are complete ordered fields and \( \varphi \colon F \to L \) is the order-preserving field isomorphism.

::: {.enumerate options="label=(\alph*)"}
1. For each statement, decide whether its truth could depend on which complete ordered field is taken as \( \nR \), and justify your answer: (i) \( \sqrt 2 + \sqrt 3 > 3 \); (ii) the zero element is the empty set; (iii) \( \nR \) is uncountable.
2. Which step of @exm-cof-limits-carried-across uses that \( \varphi \) is onto?
3. Why does a model of the axioms, built inside set theory, show that the axioms of a complete ordered field cannot contradict each other unless that set theory does?
:::
:::

::: {.solution}
(a) (i) No. Write \( b \) and \( c \) for the non-negative square roots of \( 2 \) and \( 3 \) in \( F \), which exist and are unique by @prp-cof-square-roots. Then \( \varphi(b) \ge 0 \) by (T2) and \( \varphi(b)^2 = \varphi(b^2) = \varphi(2) = 2 \) by (T4), so \( \varphi(b) \) is the non-negative square root of \( 2 \) in \( L \), by the uniqueness in @prp-cof-square-roots; likewise for \( c \). By (T2) and (T4), \( b + c > 3 \) if and only if \( \varphi(b) + \varphi(c) > 3 \). (The statement is in fact true: both sides are positive, \( (b + c)^2 = 5 + 2bc \), and \( bc \) is the non-negative square root of \( 6 \), so \( 5 + 2bc > 9 \) if and only if \( bc > 2 \), if and only if \( 6 > 4 \), by @prp-ordered-ring-rules (g).)

(ii) Yes. It is false in the Cauchy model and true in the field \( X \) of @exm-cof-zero-empty-set, and the two are isomorphic. The statement is about what an element is made of, which no renaming keeps.

(iii) No. A set is countable exactly when it injects into \( \nN \) (@fd2:thm-countable-characterizations). If \( L \) were countable, an injection \( g \colon L \to \nN \) composed with the bijection \( \varphi \) would give an injection \( g \circ \varphi \colon F \to \nN \); and symmetrically with \( \varphi^{-1} \). So \( F \) is countable exactly when \( L \) is.

(b) The first: the tolerance \( \varepsilon \) is given in \( L \), and the hypothesis \( a_n \to a \) speaks only about tolerances in \( F \). Surjectivity provides \( \varepsilon' = \varphi^{-1}(\varepsilon) \in F \).

(c) A contradiction derived from the axioms could be run in the model, where it would become a contradiction about one set built in the set theory; so the set theory would be inconsistent. In this volume the model is the Cauchy model (@thm-reals-complete-ordered-field) and the set theory is the one *Sets and Functions* uses informally and *Axiomatic Set Theory* states as the ZF axioms, in which it builds the Peano system \( \nN \) that Chapter 1 assumes.
:::

### B. Practice

::: {#exr-the-uniqueness-theorem-b1}
[B1]

Prove that the only order-preserving field map \( \nQ \to \nQ \) is the identity, using @prp-cof-map-fixes-rationals and @thm-rationals-embed-ordered-field but not Section 6.2. Does your proof use the order condition?
:::

::: {.solution}
Let \( \chi \colon \nQ \to \nQ \) be an order-preserving field map. It respects sums and products and fixes \( 1 \), so @prp-cof-map-fixes-rationals with \( F = L = \nQ \) gives \( \chi \circ \iota_{\nQ} = \iota_{\nQ} \). The identity \( \id_{\nQ} \) respects sums and products and fixes \( 1 \), so by the uniqueness clause of @thm-rationals-embed-ordered-field, \( \iota_{\nQ} = \id_{\nQ} \). Hence \( \chi = \chi \circ \id_{\nQ} = \id_{\nQ} \).

The order condition was never used: every map \( \nQ \to \nQ \) that respects sums and products and fixes \( 1 \) is the identity. In \( \nQ \) there is nothing besides rationals to move.
:::

::: {#exr-the-uniqueness-theorem-b2}
[B2]

Let \( F \) and \( L \) be complete ordered fields, and \( \varphi \colon F \to L \) the isomorphism of @thm-cof-uniqueness. Let \( A \subseteq F \) be non-empty and bounded above. Prove that \( \varphi(A) \coloneqq \{ \varphi(a) : a \in A \} \) has a supremum in \( L \) and that \( \varphi(\sup A) = \sup \varphi(A) \) (@fd2:def-order-supremum).
:::

::: {.solution}
Since \( F \) is complete, \( s \coloneqq \sup A \) exists. We show that \( \varphi(s) \) satisfies (S1) and (S2) for \( \varphi(A) \) in \( L \); then it is the supremum.

*(S1).* Let \( a \in A \). Then \( a \le s \), so \( \varphi(a) \le \varphi(s) \): equal if \( a = s \), and smaller if \( a < s \), since \( \varphi \) is strictly increasing.

*(S2).* Let \( u \in L \) be an upper bound of \( \varphi(A) \). Since \( \varphi \) is bijective, \( u = \varphi(v) \) for some \( v \in F \). For \( a \in A \), \( \varphi(a) \le \varphi(v) \), so \( a \le v \): if \( v < a \), then \( \varphi(v) < \varphi(a) \), against (O1). So \( v \) is an upper bound of \( A \), hence \( s \le v \) by (S2) for \( A \), and \( \varphi(s) \le \varphi(v) = u \).

So \( \varphi(s) = \sup \varphi(A) \). The proof used that \( \varphi \) is onto (in (S2)) and that \( \varphi \) reflects order; for an order-preserving field map that is not onto, the image of a supremum can fail to be the supremum of the image, because the image may have new upper bounds that are not images. For example, take \( \iota_{\nQ(t)} \colon \nQ \to \nQ(t) \) of @exm-rational-function-field and \( A = \{ 1 - 1/n : n \in \nZ_{>0} \} \). Then \( \sup A = 1 \) in \( \nQ \), but \( 1 - 1/t \) is an upper bound of the image that lies below \( 1 \), since \( 0 < 1/t < 1/(n \cdot 1) \) for every \( n \ge 1 \). (For \( \iota_{\nR} \) this cannot happen: \( \nQ \) is dense in the Archimedean field \( \nR \), so \( \iota_{\nR} \) keeps every supremum that exists in \( \nQ \).)
:::

::: {#exr-axioms-or-model-b2}
[B3]

Let \( F \) and \( L \) be complete ordered fields, \( \varphi \colon F \to L \) the isomorphism of @thm-cof-uniqueness, and \( (a_n) \) a sequence in \( F \). Prove that \( (a_n) \) is a Cauchy sequence in \( F \) (@def-cauchy-sequence-ordered-field) if and only if \( (\varphi(a_n)) \) is a Cauchy sequence in \( L \).
:::

::: {.solution}
(\( \Rightarrow \)) Let \( \varepsilon \in L_{>0} \), and put \( \varepsilon' \coloneqq \varphi^{-1}(\varepsilon) \). Since \( \varphi(\varepsilon') = \varepsilon > 0 = \varphi(0) \), and \( \varphi \) reflects order, \( \varepsilon' > 0 \). Since \( (a_n) \) is Cauchy, there is \( N \in \nN \), depending on \( \varepsilon \), with \( \abs{a_m - a_n} < \varepsilon' \) for all \( m, n \ge N \). For such \( m, n \),
\[
\abs{\varphi(a_m) - \varphi(a_n)} = \varphi\bigl(\abs{a_m - a_n}\bigr) < \varphi(\varepsilon') = \varepsilon ,
\]
by (T1), (T3) and (T2). So \( (\varphi(a_n)) \) is Cauchy in \( L \).

(\( \Leftarrow \)) The inverse \( \varphi^{-1} \) is an order-preserving field isomorphism \( L \to F \) (T5), so the same argument with the roles of \( F \) and \( L \) exchanged shows that \( (\varphi^{-1}(\varphi(a_n))) = (a_n) \) is Cauchy in \( F \).
:::

### C. Going deeper

::: {#exr-the-uniqueness-theorem-c1}
[C1: Exit check: field maps of a complete ordered field]

Let \( F \) be a complete ordered field and \( \sigma \colon F \to F \) a map that respects sums and products and has \( \sigma(1) = 1 \). Using only @prp-cof-square-roots, @prp-cof-map-fixes-rationals, @lem-cof-rationals-separate, @thm-cof-complete-archimedean and @thm-cof-embedding-into-complete (and the rules of an ordered field), prove that \( \sigma = \id_F \). Write the proof without looking at the one in this section.
:::

::: {.solution}
*\( \sigma \) fixes \( 0 \) and negatives.* \( \sigma(0) = \sigma(0 + 0) = \sigma(0) + \sigma(0) \), so \( \sigma(0) = 0 \); then \( \sigma(c) + \sigma(-c) = \sigma(0) = 0 \), so \( \sigma(-c) = -\sigma(c) \).

*Positive to positive.* Let \( a > 0 \). By @prp-cof-square-roots, \( a = b^2 \) for some \( b \ge 0 \), and \( b \ne 0 \) since \( a \ne 0 \). Then \( \sigma(b) \sigma(b^{-1}) = \sigma(1) = 1 \ne 0 \), so \( \sigma(b) \ne 0 \), and \( \sigma(a) = \sigma(b)^2 > 0 \) because non-zero squares are positive.

*Strictly increasing.* If \( x < y \), then \( y - x > 0 \), so \( \sigma(y) - \sigma(x) = \sigma(y - x) > 0 \).

*Conclusion.* \( \sigma \) is an order-preserving field map \( F \to F \). By @thm-cof-complete-archimedean, \( F \) is Archimedean; it is complete. @thm-cof-embedding-into-complete with source and target \( F \) gives exactly one order-preserving field map \( F \to F \), and \( \id_F \) is one. So \( \sigma = \id_F \).

(Alternatively, the last paragraph can be done by hand: \( \sigma \) fixes the rationals by @prp-cof-map-fixes-rationals, and a strictly increasing map that fixes the rationals keeps \( \nQ_F(x) \); since \( F \) is Archimedean, \( \nQ_F(\sigma(x)) = \nQ_F(x) \) gives \( \sigma(x) = x \) by @lem-cof-rationals-separate.)

**Marking scheme.** (10 points)
- 2: \( \sigma(0) = 0 \) and \( \sigma(-c) = -\sigma(c) \) from additivity (on the by-hand route, also that \( \sigma \) fixes the rationals, with a reason that uses no order hypothesis).
- 3: \( a > 0 \Rightarrow \sigma(a) > 0 \) through a square root of \( a \), **including** the proof that \( \sigma(b) \ne 0 \).
- 2: strict increase from additivity, through \( \sigma(y) - \sigma(x) = \sigma(y - x) \).
- 3: concludes \( \sigma = \id_F \) by the uniqueness clause, or directly by comparing the rationals below \( x \) and below \( \sigma(x) \), and in either case says that \( F \) is Archimedean by @thm-cof-complete-archimedean.
Fatal errors (0 for the step): assuming \( \sigma \) order-preserving; using the uniqueness clause or the rationals-below comparison without saying why \( F \) is Archimedean; taking a square root of a negative element; dividing by \( \sigma(b) \) without showing \( \sigma(b) \ne 0 \).
:::

::: {#exr-the-uniqueness-theorem-c2}
[C2: Find the error]

Here is an argument that the map \( \varphi \colon F \to L \) of @thm-cof-embedding-into-complete is additive. For subsets \( A, B \subseteq \nQ \), write \( A + B \coloneqq \{ a + b : a \in A, b \in B \} \).

> (1) Let \( x, y \in F \) and \( q \in \nQ_F(x + y) \).
>
> (2) Then \( q/2 < x \) and \( q/2 < y \).
>
> (3) So \( q = q/2 + q/2 \in \nQ_F(x) + \nQ_F(y) \).
>
> (4) Conversely, if \( r < x \) and \( s < y \), then \( r + s < x + y \); so \( \nQ_F(x) + \nQ_F(y) \subseteq \nQ_F(x + y) \).
>
> (5) Hence \( \nQ_F(x + y) = \nQ_F(x) + \nQ_F(y) \).
>
> (6) Taking suprema in \( L \), \( \varphi(x + y) = \varphi(x) + \varphi(y) \).

Is the conclusion true? Name the first line that fails, give a counterexample **to that line**, and name a second gap. Then repair the argument with results of Section 6.2.
:::

::: {.solution}
*The conclusion is true:* \( \varphi \) is additive by @thm-cof-embedding-into-complete. The argument does not prove it.

*The first illegal line is (2).* From \( q < x + y \) it does not follow that \( q/2 < x \). Counterexample to the step, in \( F = \nQ \): \( x = 0 \), \( y = 2 \), \( q = 1 \). Then \( q = 1 < 2 = x + y \), but \( q/2 = 1/2 \) is not below \( x = 0 \). The line would be right if \( x = y \); it splits \( q \) evenly while \( x + y \) may be split unevenly.

*The second gap is (6).* It uses, without saying so, that the supremum of a sum set is the sum of the suprema: \( \sup_L \iota_L(A + B) = \sup_L \iota_L(A) + \sup_L \iota_L(B) \). That is true in a complete ordered field, but this book has not proved it, and the route of Section 6.2 was chosen to avoid it.

*Repair.* Line (5) is in fact true, for another reason: by @lem-cof-below-sum in the Archimedean field \( F \), \( q < x + y \) if and only if there is \( r \in \nQ \) with \( r < x \) and \( q - r < y \); then \( q = r + (q - r) \) with \( r \in \nQ_F(x) \) and \( q - r \in \nQ_F(y) \). So replace (2) and (3) by @lem-cof-below-sum, which chooses the split \( r \) to fit \( x \) and \( y \). Replace (6) by the rationals-below argument: by \( (\star) \), \( \nQ_L(\varphi(x + y)) = \nQ_F(x + y) \) and \( \nQ_L(\varphi(x)) = \nQ_F(x) \), \( \nQ_L(\varphi(y)) = \nQ_F(y) \); by @lem-cof-below-sum in \( L \) (Archimedean by @thm-cof-complete-archimedean), \( \nQ_L(\varphi(x) + \varphi(y)) = \nQ_L(\varphi(x)) + \nQ_L(\varphi(y)) \). So \( \varphi(x + y) \) and \( \varphi(x) + \varphi(y) \) have the same rationals below them, and they are equal by @lem-cof-rationals-separate in \( L \).

**Marking scheme.** (10 points)
- 3: names line (2) as the first failure and says what it would need (an even split of \( q \), which \( x + y \) does not guarantee).
- 1: names line (6) as a second gap, because it assumes the sum-of-suprema rule.
- 3: a counterexample to the step itself (values of \( x, y, q \) with \( q < x + y \) and \( q/2 \not< x \)), not to the conclusion.
- 3: a correct repair through @lem-cof-below-sum and the rationals below, with \( (\star) \) and @lem-cof-rationals-separate in \( L \); or a proof of the sum-of-suprema rule, if the reader supplies one.
Fatal errors (0 for the item): declaring the conclusion false.
:::

::: {#exr-the-uniqueness-theorem-c3}
[C3: Bounded increasing sequences]

(a) Let \( F \) be a complete ordered field and \( (a_n) \) a sequence in \( F \) with \( a_n \le a_{n+1} \) for every \( n \), whose set of terms \( S \coloneqq \{ a_n : n \in \nN \} \) is bounded above. The following steps prove that \( a_n \to \sup S \) (@def-sequence-limit-ordered-field).

::: {.enumerate options="label=(\arabic*)"}
1. \( S \) is non-empty and bounded above, so \( s \coloneqq \sup S \) exists.
2. Let \( \varepsilon \in F_{>0} \). Find \( N \in \nN \) with \( a_N > s - \varepsilon \).
3. *Name the move, then complete it:* show \( \abs{a_n - s} < \varepsilon \) for every \( n \ge N \), and conclude.
:::

(b) Show that in \( \nQ \) the conclusion fails: the sequence \( (-x_n) \), with \( (x_n) \) the Newton sequence, is increasing and bounded above and has no limit in \( \nQ \).
:::

::: {.solution}
The move is **construct a point as a supremum** (@exm-method-point-as-supremum): the limit is built as \( \sup S \); (S1) puts every term below it, and leastness, in (2), puts a term above \( s - \varepsilon \).

(a) (2) Since \( s - \varepsilon < s \) and \( s \) is the least upper bound, \( s - \varepsilon \) is not an upper bound of \( S \), so \( a_N > s - \varepsilon \) for some \( N \in \nN \).

(3) Let \( n \ge N \). By induction on \( i \) (@thm-omega-induction), \( a_N \le a_{N+i} \), and \( n = N + i \) for some \( i \) (@prp-omega-order-arithmetic (a)); so \( a_N \le a_n \). Also \( a_n \le s \) by (S1). Hence \( s - \varepsilon < a_N \le a_n \le s < s + \varepsilon \), and \( \abs{a_n - s} < \varepsilon \) (@prp-absolute-value-ordered-field (d)). Since \( \varepsilon \) was arbitrary and \( N \) depends only on \( \varepsilon \), \( a_n \to s \).

(b) By @thm-sqrt2-cauchy-no-rational-limit, \( x_m \le x_n \) for \( m \ge n \) and \( x_n > 1 \); so \( -x_n \le -x_m \) for \( m \ge n \) (increasing) and \( -x_n < -1 \) (bounded above). If \( -x_n \to L \) in \( \nQ \), then \( x_n \to -L \) (@thm-limit-laws-ordered-field (b), with \( c = -1 \)), against the same theorem.

**Marking scheme.** (10 points)
- 2: names the move (construct a point as a supremum) and says that every term lies below \( s \) by (S1) while step (2) uses leastness (S2).
- 2: step (2): \( s - \varepsilon \) is not an upper bound, so some \( a_N \) exceeds it.
- 2: proves \( a_N \le a_n \) for \( n \ge N \) (induction, or monotonicity stated with a reason).
- 2: the squeeze \( s - \varepsilon < a_n \le s \) and the absolute value.
- 2: (b) increasing, bounded above, and no limit, through the limit law.
Fatal errors (0 for the step): assuming \( s \in S \); choosing \( N \) after \( n \).
:::

### R. Review

::: {#exr-the-uniqueness-theorem-r1}
[R1]

Let \( q_n \coloneqq (n + 1)/(n + 2) \in \nQ \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( (q_n) \) is a Cauchy sequence of rationals and that \( [(q_n)] = 1 \) in \( \nR \).
2. Every \( q_n \) is less than \( 1 \). What inequality between \( [(q_n)] \) and \( 1 \) does a termwise comparison give, and why can it not give a strict one?
:::
:::

::: {.solution}
(a) \( q_n \to 1 \) in \( \nQ \) (@exm-first-sequences-ordered-field (c)); a convergent sequence is Cauchy (@prp-convergent-cauchy-ordered-field), so \( (q_n) \in \sC \) (@def-rational-cauchy-sequences). Since \( \abs{(q_n - 1) - 0} = \abs{q_n - 1} \), the statement \( q_n \to 1 \) says exactly that \( (q_n - 1)_n \) is null. So \( (q_n) \sim (1)_n \) (@def-cauchy-equivalent), and \( [(q_n)] = [(1)_n] = 1 \) (@def-rational-embedding).

(b) @lem-termwise-order gives \( [(q_n)] \le [(1)_n] = 1 \). A strict inequality is impossible, since (a) gives equality: strict termwise inequalities survive to classes only as \( \le \), as they survive to limits (@prp-limit-preserves-order-ordered-field).
:::

::: {#exr-the-uniqueness-theorem-r2}
[R2]

Which of the following rules define a function \( \nQ \to \nQ \), where \( \nQ = (\nZ \times \nZ_{>0})/{\sim} \)?

::: {.enumerate options="label=(\alph*)"}
1. \( [(p, q)] \mapsto [(p^2, q^2)] \);
2. \( [(p, q)] \mapsto [(p + q, q)] \);
3. \( [(p, q)] \mapsto [(p + 1, q)] \).
:::

For each that does, name the function in familiar terms.
:::

::: {.solution}
Recall \( (p, q) \sim (r, s) \) iff \( ps = rq \) (@prp-rational-pairs-equivalence; the method is @fd2:exm-method-well-definedness).

(a) Yes, it is \( x \mapsto x^2 \): \( q^2 > 0 \), and \( ps = rq \) gives \( p^2 s^2 = r^2 q^2 \).

(b) Yes, \( x \mapsto x + 1 \): \( (p + q)s = ps + qs = rq + qs = (r + s)q \).

(c) No: \( (1, 2) \sim (2, 4) \), but \( (2, 2) \not\sim (3, 4) \), since \( 2 \cdot 4 = 8 \ne 6 = 3 \cdot 2 \).
:::

::: {#exr-the-uniqueness-theorem-r3}
[R3]

Let \( F \) be a complete ordered field.

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \iota_F(\nQ) \) is countable.
2. Let \( \sqrt 2 \in F \) be as in @prp-cof-square-roots. Show that \( \sqrt 2 \notin \iota_F(\nQ) \).
3. Let \( x < y \) in \( F \). Show that some element of \( F \setminus \iota_F(\nQ) \) lies strictly between \( x \) and \( y \).
:::
:::

::: {.solution}
(a) The set \( \nQ \) built in Chapter 3 is countable; that is review exercise R2 of Section 3.3 (the countability results of *Sets and Functions*, Chapter 4, applied to \( \nZ = (\nN \times \nN)/{\sim} \) and \( \nQ \); @fd2:thm-integers-rationals-countable is about the school rationals and is not used). \( \iota_F(\nQ) \) is the image of \( \nQ \) under \( \iota_F \), so it is countable (@fd2:prp-countable-image).

(b) If \( \sqrt 2 = \iota_F(p) \), then \( \iota_F(p^2) = \iota_F(p)^2 = 2 \cdot 1_F = \iota_F(2) \) (@thm-rationals-embed-ordered-field), and \( \iota_F \) is injective, so \( p^2 = 2 \), against @thm-no-rational-square-two.

(c) \( F \) is Archimedean (@thm-cof-complete-archimedean). By density (@thm-rationals-dense-ordered-field) take \( q \in \nQ \) with \( x < \iota_F(q) < y \), and by @prp-archimedean-reciprocal take \( N \in \nZ_{>0} \) with \( 1/(N \cdot 1_F) < (y - \iota_F(q))/\sqrt 2 \); here \( \sqrt 2 > 0 \), since \( \sqrt 2 \ge 0 \) and \( \sqrt 2 \ne 0 \). Put \( z \coloneqq \iota_F(q) + \sqrt 2/(N \cdot 1_F) \); then \( \iota_F(q) < z < y \). If \( z = \iota_F(p) \) with \( p \in \nQ \), then
\[
\sqrt 2 = (N \cdot 1_F)\bigl(\iota_F(p) - \iota_F(q)\bigr) = \iota_F\bigl(N(p - q)\bigr) ,
\]
against (b). So the rational elements of \( F \) are countably many, and between any two elements of \( F \) lies one that is not rational.
:::

<!-- dependency ledger
thm-cof-uniqueness (proof): a composite of additive, multiplicative, unit-preserving, strictly increasing maps is one; id_F is one | inline
thm-cof-uniqueness (proof): an order-preserving field map reflects order | shown after def-cof-order-preserving-map (Section 6.1), (O1)
thm-cof-uniqueness (claim): the uniqueness clause with F on both sides needs only that F is Archimedean (also exr-the-uniqueness-theorem-a1 (a), (d)) | remark after the proof of thm-cof-embedding-into-complete (Section 6.2), cited by prose pointer; nothing depends on it
thm-cof-uniqueness (claim): the image of iota_R misses r with r^2 = 2 | exm-sqrt2-class (r != q for every q in Q), cited
thm-cof-uniqueness (claim): a direct proof that phi is onto | exr-measuring-by-rationals-c2 (b), prose pointer only; nothing depends on it
cor-cof-isomorphic-to-cauchy-reals (claim): iota_Q = id_Q | uniqueness clause of thm-rationals-embed-ordered-field, cited inline
cor-cof-isomorphic-to-cauchy-reals (claim): cong is an equivalence relation; injectivity of chi gives additivity of chi^{-1} | inline (second-reading fold)
exm-cof-two-models (example): Q_F(x) non-empty and not all of Q (Archimedean property applied to -x and x, iota_F(-n) = -n 1_F), closed downward (Section 6.1, transitivity of <), no largest element (density) | def-archimedean-ordered-field, thm-rationals-dense-ordered-field; inline
exm-cof-two-models (solution): phi(0) = 0 | prp-cof-map-fixes-rationals, cited
exm-cof-two-models (example): Dedekind cuts as the real numbers of Axiomatic Set Theory, a complete ordered field in which the rationals below a cut c are the elements of c; the copy of y is Q_R(y) | prose pointer to Axiomatic Set Theory, Chapter 1 (STATUS promise ST.1, thm-dedekind-same-reals (c)) for the cut model; then (star) of thm-cof-embedding-into-complete for the isomorphism of thm-cof-uniqueness; nothing depends on it
thm-cof-field-automorphism-identity (proof): sigma(0) = 0 and sigma(-c) = -sigma(c) from additivity | inline; uniqueness of negatives prp-ring-algebra (a)
thm-cof-field-automorphism-identity (proof): 0 != 1 in a field | def-commutative-ring-and-field (field: 1 != 0), cited
thm-cof-field-automorphism-identity (proof): the uniqueness clause of thm-cof-embedding-into-complete needs only an Archimedean target | remark after the proof of thm-cof-embedding-into-complete (Section 6.2), cited by prose pointer
thm-cof-field-automorphism-identity (claim): Q(sqrt 2) is Archimedean, not complete, and has a field automorphism exchanging sqrt 2 and -sqrt 2 | prose pointer to Algebraic Preliminaries, Chapter 2 (remark 'What each hypothesis buys'); nothing depends on it
thm-cof-field-automorphism-identity (claim): t -> t + 1 is an order-preserving automorphism of Q(t) other than the identity (keeps degrees and leading coefficients) | exm-rational-function-field (school polynomial algebra, flagged there); remark only, nothing depends on it
thm-cof-field-automorphism-identity (claim): Q has only the identity as a map respecting +, ·, 1 | exr-the-uniqueness-theorem-b1, remark pointer only; nothing depends on it
sec-the-uniqueness-theorem (claim): (T1)-(T5) for the isomorphism phi | inline, from def-cof-order-preserving-map, def-absolute-value-ordered-field, prp-cof-map-fixes-rationals, the fold after cor-cof-isomorphic-to-cauchy-reals (cited)
sec-the-uniqueness-theorem (claim): subsets, sequences, functions of L each come from exactly one of F | phi bijective; inline
exm-cof-limits-carried-across (example): epsilon' = phi^{-1}(epsilon) > 0; |phi(a_n) - phi(a)| = phi(|a_n - a|) | (T1)-(T3), (T5); inline
exm-cof-limits-carried-across (claim): the copy of the Newton sequence under iota_R converges in R | Exercise B3 of Section 5.4 (exr-rationals-inside-the-reals-b3, the proof of the retired thm-terms-converge-to-class), remark pointer; nothing depends on it
sec-the-uniqueness-theorem (claim): an order-preserving field isomorphism is an isomorphism of the structure (F; +, ·, 0, 1, <) in the sense of fd1:def-isomorphism-of-structures | constants by (T1) and chi(1) = 1, functions by definition, the relation in both directions by (T2); inline
sec-the-uniqueness-theorem (claim): statements quantifying over subsets, sequences, functions are carried across case by case | not stated as a theorem; instance proved (exm-cof-limits-carried-across); nothing depends on it
exm-cof-zero-empty-set (example): emptyset not in the Cauchy R (every class contains its representative); beta is a bijection | inline, def-reals-cauchy-classes
exm-cof-zero-empty-set (example): transport of structure along a bijection beta gives a complete ordered field and beta is an isomorphism | inline (second-reading fold)
sec-the-uniqueness-theorem (claim): Analysis on the Real Line, Chapter 1 assumes an ordered field containing Q with the least upper bound axiom, and proves N unbounded, Q dense, square roots; an1 does not cite fd3 | an1 Chapter 1 (prose pointer, read in an1/src/ch01-least-upper-bound/03, 05, 06); nothing depends on it
sec-the-uniqueness-theorem (claim): consistency of the complete-ordered-field axioms relative to set theory with a Peano system | thm-reals-complete-ordered-field (cited); informal meta-argument in prose; existence of N from ZF is in Axiomatic Set Theory (prose pointer) and Section 1.5 (explained, not proved); nothing depends on it
sec-the-uniqueness-theorem (claim): a statement proved from the ordered-field axioms holds in every ordered field | inline (a proof from the axioms runs in any model; for first-order statements fd1:thm-first-order-soundness); nothing depends on it
sec-the-uniqueness-theorem (claim): the four truth values: x·x = 1 + 1 false in Q, true in R; some y above every n·1 false in R, true in Q(t) | thm-no-rational-square-two, prp-cof-square-roots, thm-cof-complete-archimedean, exm-rational-function-field (school polynomial algebra, flagged there), cited
exr-the-uniqueness-theorem-a1 (solution): (g) sigma(2) = 2 and the square root of r | prp-cof-map-fixes-rationals, prp-cof-square-roots, prp-ordered-ring-rules (e), cited
exr-axioms-or-model-a1 (solution): (b + c)^2 = 5 + 2bc, bc = sqrt 6, 5 + 2 sqrt 6 > 9 iff 6 > 4 | inline; verify/ch06/exr-axioms-or-model-a1.py
exr-axioms-or-model-a1 (solution): composite of an injection and a bijection is an injection | fd2:thm-composition-injective-surjective (a); inline
exr-axioms-or-model-a1 (solution): (ii) uses only exm-cof-zero-empty-set and the zero of the Cauchy model | exm-cof-zero-empty-set, cited
exr-the-uniqueness-theorem-b2 (solution): a <= s gives phi(a) <= phi(s) | strict increase or equality; inline
exr-the-uniqueness-theorem-b2 (solution): in Q(t), 1 - 1/t is an upper bound of {1 - 1/n} below 1 | exm-rational-function-field (0 < 1/t < 1/(n·1); school polynomial algebra, flagged there); counterexample only, nothing depends on it
exr-the-uniqueness-theorem-b2 (solution): iota_R keeps every supremum that exists in Q | inline parenthetical; density thm-rationals-dense-ordered-field in the Archimedean R (thm-constructed-reals-archimedean); nothing depends on it
exr-axioms-or-model-b2 (solution): (T1)-(T3), (T5) as in exm-cof-limits-carried-across | inline in this section
exr-the-uniqueness-theorem-c2 (solution): counterexample x = 0, y = 2, q = 1 | verify/ch06/exr-the-uniqueness-theorem-c2.py
exr-the-uniqueness-theorem-c2 (solution): sup(A + B) = sup A + sup B in a complete ordered field | not proved in this book; named only as the gap; nothing depends on it
exr-the-uniqueness-theorem-c3 (solution): (2) s - eps not an upper bound, so a_N > s - eps | leastness (S2) of the supremum; inline
exr-the-uniqueness-theorem-c3 (solution): a_N <= a_{N+i} by induction on i; n = N + i | thm-omega-induction, prp-omega-order-arithmetic (a), cited; verify/ch06/exr-the-uniqueness-theorem-c3.py
exr-the-uniqueness-theorem-c3 (solution): s - eps < a_n <= s gives |a_n - s| < eps | prp-absolute-value-ordered-field (d), cited
exr-the-uniqueness-theorem-c3 (solution): (b) -x_n increasing, < -1; no limit via c = -1 | thm-sqrt2-cauchy-no-rational-limit, thm-limit-laws-ordered-field (b), cited; verify/ch06/exr-the-uniqueness-theorem-c3.py
exr-the-uniqueness-theorem-r1 (solution): q_n - 1 = -1/(n + 2); (q_n - 1) null | exm-first-sequences-ordered-field (c); verify/ch06/exr-the-uniqueness-theorem-r1.py
exr-the-uniqueness-theorem-r2 (solution): (a), (b) respect ~; (c) fails at (1, 2) ~ (2, 4), 8 != 6 | prp-rational-pairs-equivalence; verify/ch06/exr-the-uniqueness-theorem-r2.py
exr-the-uniqueness-theorem-r3 (solution): (a) constructed Q countable; image under iota_F countable | exr-gaps-in-the-rationals-r2 (prose pointer); fd2:prp-countable-image (citing rule group (i))
exr-the-uniqueness-theorem-r3 (solution): iota_F injective and preserves sums, products; iota_F(N(p - q)) = (N 1_F)(iota_F(p) - iota_F(q)) | thm-rationals-embed-ordered-field, cited; verify/ch06/exr-the-uniqueness-theorem-r3.py
exr-the-uniqueness-theorem-r3 (solution): sqrt 2 > 0; iota_F(q) < z < y | prp-cof-square-roots (b >= 0, b^2 = 2 != 0), prp-archimedean-reciprocal, prp-reciprocal-order; inline; verify/ch06/exr-the-uniqueness-theorem-r3.py
-->
