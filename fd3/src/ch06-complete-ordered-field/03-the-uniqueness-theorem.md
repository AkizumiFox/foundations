# Two Complete Ordered Fields, One Isomorphism

Section 6.2 measured an element of an Archimedean ordered field \( F \) by the rationals below it and used the measurement to build a map into a complete ordered field \( L \): by @thm-cof-embedding-into-complete there is **exactly one** order-preserving field map \( \varphi \colon F \to L \), and it keeps the rationals below each element, \( \nQ_L(\varphi(x)) = \nQ_F(x) \) (property \( (\star) \) of that theorem). This section takes both fields complete. Then maps run in both directions, and the word "exactly" turns them into inverses of each other without a single computation. The result is the theorem the chapter is named for: any two complete ordered fields are copies of each other, by one isomorphism and no other. The section ends with automorphisms: the only map of a complete ordered field to itself that respects sums, products and \( 1 \) is the identity, even when the map is asked neither to respect the order nor to be onto.

Throughout, "order-preserving field map" has the meaning of @def-cof-order-preserving-map: a map \( \chi \colon F \to L \) between ordered fields with \( \chi(a + b) = \chi(a) + \chi(b) \), \( \chi(ab) = \chi(a) \chi(b) \), \( \chi(1) = 1 \), and \( a < b \Rightarrow \chi(a) < \chi(b) \) for all \( a, b \in F \). Such a map also **reflects** order: if \( \chi(a) < \chi(b) \), then \( a < b \), since \( a = b \) would give \( \chi(a) = \chi(b) \) and \( b < a \) would give \( \chi(b) < \chi(a) \), both excluded by trichotomy (O1) in \( L \).

## The uniqueness theorem

Section 6.2 gave us, for complete \( F \) and \( L \), a map \( \varphi \colon F \to L \). It did not say that \( \varphi \) is onto. A map can preserve everything in sight and still miss most of its target: the map \( \iota_{\nR} \colon \nQ \to \nR \) preserves sums, products and order (@thm-rationals-embed-ordered-field), and the real number \( r \) of @exm-sqrt2-class, whose square is \( 2 \), is not in its image. What rules this out when the source is complete as well?

::: {#thm-cof-uniqueness}
[Uniqueness of the Complete Ordered Field]

Let \( F \) and \( L \) be complete ordered fields (@def-complete-ordered-field). Then there is **exactly one** order-preserving field isomorphism \( F \to L \) (@def-cof-order-preserving-map). It is the map \( \varphi \) of @thm-cof-embedding-into-complete.
:::

::: {.idea}
Section 6.2 runs in both directions. Since \( F \) is complete, it is Archimedean (@thm-cof-complete-archimedean), so it is a legal source; since \( L \) is complete, it is a legal target. That gives \( \varphi \colon F \to L \). Swapping the roles gives \( \psi \colon L \to F \).

To show that \( \psi \) undoes \( \varphi \), we could try to compute \( \psi(\varphi(x)) \) from the two suprema. We do not have to. The composite \( \psi \circ \varphi \colon F \to F \) is again an order-preserving field map, and so is the identity of \( F \). The uniqueness clause of @thm-cof-embedding-into-complete, applied with \( F \) as source **and** as target, says there is only one such map. So the two are equal. **Uniqueness gives inverses.**

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

The answer to the prompt: three of the four conditions are one line each, because each of \( \varphi \), \( \psi \) satisfies it and the condition passes through a composite. The order condition is the same, in two steps: \( a < b \) gives \( \varphi(a) < \varphi(b) \), which is a strict inequality in \( L \), the kind of hypothesis \( \psi \) accepts. Nothing harder is hiding there. The weight of the proof sits in the uniqueness clause, which the proof uses three times: once for \( \psi \circ \varphi \), once for \( \varphi \circ \psi \), and once for \( \chi \).

The proof never evaluates \( \psi(\varphi(x)) \). A direct proof that \( \varphi \) is onto exists: given \( y \in L \), take the supremum in \( F \) of the rationals below \( y \), and check that \( \varphi \) sends it to \( y \). It needs the measuring argument of Section 6.2 once more, now from \( L \) back to \( F \). The route above gets the same conclusion from a sentence about how many maps there are.

::: {.check}
Why could the proof not simply **define** \( \psi \coloneqq \varphi^{-1} \), instead of building \( \psi \) from @thm-cof-embedding-into-complete?
:::

::: {.solution}
The inverse \( \varphi^{-1} \colon L \to F \) exists only if \( \varphi \) is bijective (@fd2:thm-bijection-iff-inverse), and bijectivity is what the theorem is trying to prove. Section 6.2 gives \( \varphi \) as an injective map (it is strictly increasing), with no claim that it is onto. The map \( \psi \) is built independently of \( \varphi \), and only afterwards shown to be its inverse.
:::

Each hypothesis has a job. Completeness of \( L \) makes \( L \) a target, so that \( \varphi \) exists. Completeness of \( F \) makes \( F \) a target, so that \( \psi \) exists. The uniqueness clause with \( F \) on both sides is cited as stated, for a complete target, but by the remark after its proof in Section 6.2 it needs only that \( F \) is Archimedean. Completeness of each field also gives the Archimedean property that makes it a source. Drop the completeness of \( F \), and the conclusion fails: \( \nQ \) is Archimedean, \( \iota_{\nR} \colon \nQ \to \nR \) is the only order-preserving field map (@thm-cof-embedding-into-complete), and it is not onto, as the opening of this section noted.

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
- \( \nQ \not\cong \nR \). An order-preserving field isomorphism \( \chi \colon \nQ \to \nR \) would satisfy \( \chi = \chi \circ \iota_{\nQ} = \iota_{\nR} \) (@prp-cof-map-fixes-rationals with \( F = \nQ \), and \( \iota_{\nQ} = \id_{\nQ} \) by the uniqueness clause of @thm-rationals-embed-ordered-field, since \( \id_{\nQ} \) preserves sums and products and fixes \( 1 \)). But \( \iota_{\nR} \) is not onto: the element \( r \) of @exm-sqrt2-class has \( r^2 = 2 \) and is not \( \iota_{\nR}(q) \) for any \( q \in \nQ \).

**Non-example by minimal change.** Drop "order-preserving" and keep the rest: a bijection that respects sums, products and \( 1 \). Such a map can send a positive element to a negative one; the warning below names one. So the order condition is a genuine extra demand, and \( \cong \) in this book always includes it.

::: {#cor-cof-isomorphic-to-cauchy-reals}
[Every Complete Ordered Field Is a Copy of the Reals]

Let \( F \) be a complete ordered field, and let \( \nR \) be the field of Chapter 5. Then \( F \cong \nR \): there is **exactly one** order-preserving field isomorphism \( F \to \nR \).
:::

::: {.proof}
By @thm-reals-complete-ordered-field, \( \nR \) is a complete ordered field. Apply @thm-cof-uniqueness with \( L = \nR \).
:::

So "the real numbers" names one ordered field up to a unique relabeling. Informally, a statement about a complete ordered field that speaks only of its sums, products and order is true in \( F \) exactly when it is true in \( \nR \), since the isomorphism carries one situation to the other. Section 6.5 explains this pattern and why we do not state it as a theorem; nothing here depends on it.

::: {.remark}
On any set \( \mathcal S \) of ordered fields, \( \cong \) is an equivalence relation (@fd2:def-equivalence-relation): it is reflexive, symmetric and transitive. No proof in this section uses its symmetry or transitivity; the remark records that the word "isomorphic" behaves as the word "equal" suggests. Section 6.5 uses the symmetric clause: the inverse of the isomorphism of @thm-cof-uniqueness is again one.
:::

::: {.second-reading title="Why isomorphism is an equivalence relation"}
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

Let \( M \) be a complete ordered field; Chapter 7 builds one whose elements are sets of rationals. Let \( \varphi \colon \nR \to M \) be the isomorphism of @thm-cof-uniqueness, and \( r \) the real number of @exm-sqrt2-class, with \( r > 0 \) and \( r^2 = 2 \). Find \( \varphi(r) \) in terms of \( M \) alone, and describe the set \( \nQ_M(\varphi(r)) \).
:::

::: {.solution}
*The image of \( r \).* Since \( \varphi \) is multiplicative and fixes the rationals (@prp-cof-map-fixes-rationals), \( \varphi(r)^2 = \varphi(r^2) = \varphi(\iota_{\nR}(2)) = \iota_M(2) \). Since \( \varphi \) is strictly increasing and \( r > 0 \), \( \varphi(r) > \varphi(0) = 0 \). By @prp-cof-square-roots in the complete field \( M \), there is exactly one \( b \ge 0 \) in \( M \) with \( b^2 = \iota_M(2) \). So \( \varphi(r) \) is that \( b \): the square root of \( 2 \) in \( M \), however \( M \) was built.

*The rationals below it.* By \( (\star) \) of @thm-cof-embedding-into-complete, \( \nQ_M(\varphi(r)) = \nQ_{\nR}(r) \). By @exm-cof-rationals-below-sqrt2 this is the set of rationals \( q \) with \( q < 0 \), or with \( q \ge 0 \) and \( q^2 < 2 \). The same set of rationals sits below \( \sqrt 2 \) in both models.

In Chapter 7 a real number **is** a set of rationals: non-empty, not all of \( \nQ \), closed downward, and with no largest element. The set \( \nQ_F(x) \) of an element of an Archimedean ordered field has each of these four properties (the first two by the Archimedean property, the third by transitivity of \( < \), the fourth by density, @thm-rationals-dense-ordered-field), and the isomorphism of that chapter, from \( \nR \) to the cuts, sends each \( x \in \nR \) to the set \( \nQ_{\nR}(x) \). So the Dedekind cut is the rationals-below set of Section 6.1, made into the definition of a number.
:::

::: {.warning}
"Isomorphic" without "order-preserving" is a weaker statement in general. Section 6.4 shows that the ordered field \( \nQ(\sqrt 2) \) has a bijection onto itself that respects sums and products and sends the positive element \( \sqrt 2 \) to the negative element \( -\sqrt 2 \). For complete ordered fields the two notions coincide: the last subsection shows that a map out of a complete ordered field that respects sums, products and \( 1 \) is automatically order-preserving.
:::

## Automorphisms

An isomorphism from a field to itself is a symmetry of the field: a relabeling of its elements that leaves the arithmetic unchanged. The field \( \nQ(\sqrt 2) \) of the warning above has a symmetry that exchanges \( \sqrt 2 \) and \( -\sqrt 2 \). The uniqueness theorem rules out such a symmetry in a complete ordered field as long as it respects the order; the theorem at the end of this subsection rules it out altogether.

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
The natural first attempt is to copy @cor-cof-order-automorphism-identity, and it stops at once: that proof needs \( \sigma \) to be strictly increasing, and nothing in the hypotheses mentions \( < \). A second attempt computes directly: \( \sigma \) fixes every rational (@prp-cof-map-fixes-rationals, which needs no order hypothesis), and one would like to squeeze \( \sigma(x) \) between rationals close to \( x \). But to squeeze, we must know that \( q < x \) gives \( \sigma(q) < \sigma(x) \), which is the order condition again.

So the order condition has to be **recovered** from the arithmetic. In a complete ordered field, positivity has a description in terms of multiplication alone: an element is positive exactly when it is a non-zero square (@prp-cof-square-roots gives the square root). A map that respects products sends squares to squares, and squares in an ordered field are never negative. Then additivity turns "positives go to positives" into "\( \sigma \) is strictly increasing", and the uniqueness clause of @thm-cof-embedding-into-complete finishes, as in the corollary's proof (which never uses bijectivity).

Plan: ① positive to positive, through a square root; ② strictly increasing, through differences; ③ the uniqueness clause.

*Before reading on: which line of the proof below fails for the field \( \nQ(\sqrt 2) \) of the warning above?*
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

The answer to the prompt: the line that fails in \( \nQ(\sqrt 2) \) is the first line of Step 1, "there is \( b \) with \( b^2 = a \)". In \( \nQ(\sqrt 2) \) the positive element \( \sqrt 2 \) has no square root. Section 6.4 proves this, proves that \( \nQ(\sqrt 2) \) is Archimedean, and shows that the symmetry exchanging \( \pm \sqrt 2 \) sends \( \sqrt 2 \) to a negative element. Every later line of Steps 1 and 2 works in any ordered field. Step 3 uses completeness, as the next paragraph explains.

Completeness entered twice. It supplied square roots in Step 1, and it supplied the Archimedean property, through @thm-cof-complete-archimedean, for the uniqueness clause in Step 3. Step 3 also cites completeness of \( F \) as the target of @thm-cof-embedding-into-complete, but by the remark after that proof in Section 6.2 the uniqueness clause needs only an Archimedean target, so this is the same use again. Neither use can be dropped on its own. In \( \nQ(\sqrt 2) \) only the square roots are missing, and it has a symmetry that is not the identity. In the other direction, an ordered field in which every positive element is a square need not be Archimedean, and then an order-preserving automorphism can move elements; we do not construct such a field here.

::: {.remark}
Steps 1 and 2 used two things only: square roots of positive elements in the **source**, and the rule "non-zero squares are positive" in the **target**. If \( F \) is a complete ordered field, \( L \) is any ordered field, and \( \chi \colon F \to L \) satisfies \( \chi(a + b) = \chi(a) + \chi(b) \), \( \chi(ab) = \chi(a) \chi(b) \) and \( \chi(1) = 1 \), then \( \chi \) is strictly increasing, that is, an order-preserving field map. In particular, for complete ordered fields \( F \) and \( L \), every bijection \( F \to L \) that respects sums, products and \( 1 \) is the isomorphism of @thm-cof-uniqueness.
:::

::: {.check}
Let \( \sigma \colon \nR \to \nR \) respect sums and products, with \( \sigma(1) = 1 \), and let \( r \) be the real number of @exm-sqrt2-class (\( r > 0 \), \( r^2 = 2 \)). Without quoting @thm-cof-field-automorphism-identity, show that \( \sigma(r) = r \).
:::

::: {.solution}
\( \sigma(r)^2 = \sigma(r^2) = \sigma(2) = 2 \), since \( \sigma \) fixes the rationals (@prp-cof-map-fixes-rationals). By @prp-cof-square-roots there is \( s \ge 0 \) with \( s^2 = r \), and \( s \ne 0 \) since \( r \ne 0 \). So \( s \) has an inverse, and \( \sigma(s) \sigma(s^{-1}) = \sigma(s s^{-1}) = \sigma(1) = 1 \), which forces \( \sigma(s) \ne 0 \). Hence \( \sigma(r) = \sigma(s)^2 > 0 \) by @prp-ordered-ring-rules (e). So \( \sigma(r) \) and \( r \) are both non-negative square roots of \( 2 \), and the uniqueness part of @prp-cof-square-roots gives \( \sigma(r) = r \).
:::

## Exercises

### A. Check your understanding

::: {#exr-the-uniqueness-theorem-a1}
[A1]

Parts (a)–(c) are about the proof of @thm-cof-uniqueness, parts (d)–(f) about the proof of @thm-cof-field-automorphism-identity.

::: {.enumerate options="label=(\alph*)"}
1. Where is the completeness of \( F \) used? Name every place.
2. Why is \( \psi \circ \varphi \) order-preserving?
3. Suppose \( F \) is only assumed to be an Archimedean ordered field, and \( L \) is complete. Which step of the proof fails first?
4. Where is completeness of \( F \) used in the proof of @thm-cof-field-automorphism-identity?
5. Why is \( \sigma(b) \ne 0 \) in Step 1?
6. Why does \( \sigma \) fix every rational, although no order hypothesis is made?
:::
:::

::: {.solution}
(a) In two ways. First, through @thm-cof-complete-archimedean, completeness makes \( F \) Archimedean, so \( F \) is a legal **source** for @thm-cof-embedding-into-complete: for \( \varphi \colon F \to L \), and for the uniqueness clause applied to maps \( F \to F \) such as \( \psi \circ \varphi \). Second, it makes \( F \) a legal **target**, so that \( \psi \colon L \to F \) exists. The uniqueness clause for \( \psi \circ \varphi \) is cited with target \( F \), so as stated it asks for \( F \) complete; but by the remark after its proof in Section 6.2 only the Archimedean property of \( F \) is used there, and the first use already supplies it (as in (d)).

(b) If \( a < b \), then \( \varphi(a) < \varphi(b) \) because \( \varphi \) is strictly increasing, and this strict inequality in \( L \) is a hypothesis \( \psi \) accepts, so \( \psi(\varphi(a)) < \psi(\varphi(b)) \). A composite of strictly increasing maps is strictly increasing.

(c) The construction of \( \psi \colon L \to F \): @thm-cof-embedding-into-complete needs a complete target, and \( F \) is not one. (The map \( \varphi \) still exists.) The conclusion fails too: for \( F = \nQ \) and \( L = \nR \), the only order-preserving field map is \( \iota_{\nR} \), which is not onto.

(d) Twice in substance. In Step 1, @prp-cof-square-roots needs \( F \) complete to give the square root \( b \) of \( a > 0 \), and that is how \( \sigma(a) > 0 \) is proved. In Step 3, @thm-cof-complete-archimedean makes \( F \) Archimedean, which the uniqueness clause of @thm-cof-embedding-into-complete needs of its target (the clause separates elements by rationals in the target, here \( F \), @lem-cof-rationals-separate). Step 3 also cites the completeness of \( F \), because that theorem is stated for a complete target; by the remark after its proof in Section 6.2, the uniqueness clause needs only an Archimedean target, so this is the same use again. Square roots alone would not do: in a non-Archimedean ordered field in which every positive element is a square, Steps 1 and 2 still make \( \sigma \) order-preserving, but \( \sigma \) need not be the identity. (We give no example.)

(e) \( b \ne 0 \) has an inverse, and \( \sigma(b) \sigma(b^{-1}) = \sigma(1) = 1 \). If \( \sigma(b) \) were \( 0 \), the left side would be \( 0 \), and \( 0 \ne 1 \) in a field.

(f) By @prp-cof-map-fixes-rationals, whose hypotheses are additivity, multiplicativity and \( \sigma(1) = 1 \) only: the composite \( \sigma \circ \iota_F \colon \nQ \to F \) respects sums and products and fixes \( 1 \), so it is \( \iota_F \) by the uniqueness clause of @thm-rationals-embed-ordered-field. Order plays no part.
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

<!-- dependency ledger
thm-cof-uniqueness (proof): a composite of additive, multiplicative, unit-preserving, strictly increasing maps is one; id_F is one | inline
thm-cof-uniqueness (proof): an order-preserving field map reflects order | trichotomy (O1) of def-ordered-ring-and-field; inline in the opening frame
thm-cof-uniqueness (claim): the uniqueness clause with F on both sides needs only that F is Archimedean (also exr-the-uniqueness-theorem-a1 (a)) | remark after the proof of thm-cof-embedding-into-complete (Section 6.2), cited by prose pointer; nothing depends on it
thm-cof-uniqueness (claim): the image of iota_R misses r with r^2 = 2 | exm-sqrt2-class (r != q for every q in Q), cited
cor-cof-isomorphic-to-cauchy-reals (claim): iota_Q = id_Q | uniqueness clause of thm-rationals-embed-ordered-field, cited inline
cor-cof-isomorphic-to-cauchy-reals (claim): cong is an equivalence relation; injectivity of chi gives additivity of chi^{-1} | inline (second-reading fold)
exm-cof-two-models (example): the four properties of a Dedekind cut, and the isomorphism of Chapter 7 sends x to Q_F(x) | prose pointer to F3.3 (optional); nothing depends on it
exm-cof-two-models (example): Q_F(x) is non-empty, not all of Q, closed downward, with no largest element (F Archimedean) | def-archimedean-ordered-field, thm-rationals-dense-ordered-field; inline
thm-cof-field-automorphism-identity (proof): sigma(0) = 0 and sigma(-c) = -sigma(c) from additivity | inline; uniqueness of negatives prp-ring-algebra (a)
thm-cof-field-automorphism-identity (proof): 0 != 1 in a field | def-commutative-ring-and-field (field: 1 != 0), cited
thm-cof-field-automorphism-identity (claim): Q(sqrt 2) is Archimedean, sqrt 2 is not a square in it, and the conjugation exchanging ±sqrt 2 sends sqrt 2 to a negative element | prose pointer to Section 6.4; nothing depends on it
thm-cof-field-automorphism-identity (proof): the uniqueness clause of thm-cof-embedding-into-complete needs only an Archimedean target | remark after the proof of thm-cof-embedding-into-complete (Section 6.2), cited by prose pointer
thm-cof-field-automorphism-identity (claim): an ordered field in which every positive element is a square need not be Archimedean, and such a field can have an order-preserving automorphism other than the identity | not proved here; marked so in the text ('we do not construct such a field here'); nothing depends on it
cor-cof-isomorphic-to-cauchy-reals (claim): a statement in +, ·, < has the same truth value in F and R | marked informal, not stated as a theorem; prose pointer to Section 6.5 (sec-axioms-or-model); nothing depends on it
exr-the-uniqueness-theorem-b2 (solution): a <= s gives phi(a) <= phi(s) | strict increase or equality; inline
exr-the-uniqueness-theorem-b2 (solution): in Q(t), 1 - 1/t is an upper bound of {1 - 1/n} below 1 | exm-rational-function-field (0 < 1/t < 1/(n·1); school polynomial algebra, flagged there); counterexample only, nothing depends on it
exr-the-uniqueness-theorem-b2 (solution): iota_R keeps every supremum that exists in Q | inline parenthetical; density thm-rationals-dense-ordered-field in the Archimedean R (thm-constructed-reals-archimedean); nothing depends on it
exr-the-uniqueness-theorem-c2 (solution): counterexample x = 0, y = 2, q = 1 | verify/ch06/exr-the-uniqueness-theorem-c2.py
exr-the-uniqueness-theorem-c2 (solution): sup(A + B) = sup A + sup B in a complete ordered field | not proved in this book; named only as the gap; nothing depends on it
-->
