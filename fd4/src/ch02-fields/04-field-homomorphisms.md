# Field Homomorphisms

Section 2.3 looked at fields inside fields. This section looks at maps between fields. Two such maps have appeared already. Complex conjugation \( z \mapsto \conj{z} \) turns sums into sums and products into products (@thm-conjugate-properties (a), (b)), and so does \( a + b\sqrt 2 \mapsto a - b\sqrt 2 \) on \( \nQ(\sqrt 2) \) (@fd3:exm-cof-sqrt2-conjugation). A map that respects both operations carries every equation that holds in one field to an equation in the other. That single observation decides where such a map can send an element, shows that it never collapses two elements, and rules out most maps between most pairs of fields.

Throughout, \( F \) and \( L \) are fields, and \( n \cdot a \) for \( n \in \nN \) is the multiple of *Number Systems: From \(\nN\) to \(\nR\)*, Section 2.3 ("Multiples"): \( 0 \cdot a \coloneqq 0 \), \( (n + 1) \cdot a \coloneqq n \cdot a + a \). Powers in a field are defined by the same recursion with products: \( a^0 \coloneqq 1 \) and \( a^{n+1} \coloneqq a^n a \) for \( n \in \nN \), as @fd2:def-power does for real numbers; the power laws \( a^{m+n} = a^m a^n \), \( (a^m)^n = a^{mn} \) and \( (ab)^n = a^n b^n \) of @fd2:prp-power-laws have proofs that use only (F1)–(F7), (F9) and induction, and hold in every field with the same proofs.

## Maps that respect both operations

*A homomorphism is a map that respects addition, multiplication and the number one.*

::: {#def-field-homomorphism}
[Field Homomorphism]

Let \( F \) and \( L \) be fields. A **homomorphism** (of fields) \( \varphi \colon F \to L \) is a function such that, **for all** \( a, b \in F \),
\[
\varphi(a + b) = \varphi(a) + \varphi(b) , \qquad \varphi(ab) = \varphi(a)\varphi(b) , \qquad \varphi(1) = 1 .
\]
A **bijective** (@fd2:def-bijective) homomorphism is an **isomorphism**; \( F \) and \( L \) are **isomorphic**, written \( F \cong L \), if there is an isomorphism \( F \to L \). An isomorphism \( F \to F \) is an **automorphism** of \( F \).
:::

In words: the first clause says that adding and then mapping gives the same as mapping and then adding; the second says the same for multiplying; the third pins down the image of \( 1 \), where \( 1 \) on the left is \( 1_F \) and on the right \( 1_L \). An isomorphism is a homomorphism that is also a one-to-one correspondence of elements, so \( F \) and \( L \) are then "the same field with the elements renamed".

**Examples.**

- The **identity** \( \id_F \colon F \to F \) is an automorphism.
- **Conjugation** \( z \mapsto \conj{z} \) on \( \nC \) is a homomorphism by @thm-conjugate-properties (a), (b), since \( \conj{1} = 1 \); @exm-complex-conjugation-automorphism below shows that it is an automorphism.
- **The conjugation of \( \nQ(\sqrt 2) \)**, \( \sigma(a + b\sqrt 2) \coloneqq a - b\sqrt 2 \), is an automorphism (@fd3:exm-cof-sqrt2-conjugation).

**Why the clause \( \varphi(1) = 1 \).** The **zero map** \( a \mapsto 0 \) satisfies the first two clauses, since \( 0 = 0 + 0 \) and \( 0 = 0 \cdot 0 \), and it carries no information about \( F \) at all. The third clause excludes it, and the next proposition shows that the third clause is exactly what forces a homomorphism to remember every element.

::: {.remark}
The order-preserving field maps of *Number Systems: From \(\nN\) to \(\nR\)*, Section 6.1 (@fd3:def-cof-order-preserving-map), are the homomorphisms between ordered fields that also preserve \( < \). From here on, \( F \cong L \) means isomorphic as fields, in the sense above; the relation of that chapter, an isomorphism that also preserves the order, is said in words, "isomorphic as ordered fields". The two differ: the conjugation \( \sigma \) of \( \nQ(\sqrt 2) \) is an automorphism of the field, and it is not order-preserving, since \( 0 < \sqrt 2 \) while \( \sigma(\sqrt 2) = -\sqrt 2 < 0 = \sigma(0) \).
:::

## What a homomorphism must do

To find where a homomorphism sends an element, we take an equation that the element satisfies and apply \( \varphi \) to both sides. The equation in \( L \) that comes out often has only one solution.

::: {#prp-field-homomorphism-properties}
[Properties of Field Homomorphisms]

Let \( \varphi \colon F \to L \) be a homomorphism of fields, and let \( a, b \in F \).

::: {.enumerate options="label=(\alph*)"}
1. \( \varphi(0) = 0 \), \( \varphi(-a) = -\varphi(a) \) and \( \varphi(a - b) = \varphi(a) - \varphi(b) \).
2. If \( a \ne 0 \), then \( \varphi(a) \ne 0 \) and \( \varphi(a^{-1}) = \varphi(a)^{-1} \).
3. \( \varphi \) is **injective**.
4. The image \( \varphi(F) \) is a subfield of \( L \), and \( \varphi \), with codomain \( \varphi(F) \), is an isomorphism \( F \to \varphi(F) \).
5. If \( \psi \colon L \to M \) is a homomorphism of fields, then \( \psi \circ \varphi \colon F \to M \) is a homomorphism. If \( \varphi \) is an isomorphism, its inverse function \( \varphi^{-1} \colon L \to F \) is an isomorphism. The identity \( \id_F \) is an automorphism.
6. \( \varphi(n \cdot a) = n \cdot \varphi(a) \) and \( \varphi(a^n) = \varphi(a)^n \) for every \( n \in \nN \).
:::
:::

::: {.idea}
For (a) and (b) the equations to push through \( \varphi \) are \( 0 + 0 = 0 \), \( a + (-a) = 0 \) and \( aa^{-1} = 1 \); in \( L \) the results are equations with a unique solution, by cancellation and the uniqueness of negatives and inverses. For (c): a homomorphism cannot send a non-zero element to \( 0 \), because a non-zero element has an inverse, and then \( \varphi(a)\varphi(a^{-1}) = \varphi(1) = 1 \ne 0 \). Injectivity is that fact applied to \( a - b \). The rest is bookkeeping with (a)–(c), and induction for (f).

*Before reading on: in the proof of (c), where is \( \varphi(1) = 1 \) used, and which map satisfies the other two clauses of @def-field-homomorphism but is not injective?*
:::

::: {.proof}
(a) Since \( 0 + 0 = 0 \) in \( F \),
\[
\varphi(0) + \varphi(0) = \varphi(0 + 0) = \varphi(0) = \varphi(0) + 0 ,
\]
and additive cancellation in \( L \) (@thm-field-basic-properties (b)) gives \( \varphi(0) = 0 \). Next, \( a + (-a) = 0 \) gives \( \varphi(a) + \varphi(-a) = \varphi(a + (-a)) = \varphi(0) = 0 \), so \( \varphi(-a) \) is a negative of \( \varphi(a) \), and \( \varphi(-a) = -\varphi(a) \) by the uniqueness of negatives (@thm-field-basic-properties (c)). Finally, \( \varphi(a - b) = \varphi(a + (-b)) = \varphi(a) + \varphi(-b) = \varphi(a) - \varphi(b) \).

(b) Let \( a \ne 0 \). Since \( aa^{-1} = 1 \),
\[
\varphi(a)\varphi(a^{-1}) = \varphi(aa^{-1}) = \varphi(1) = 1 .
\]
If \( \varphi(a) = 0 \), the left side would be \( 0 \cdot \varphi(a^{-1}) = 0 \) (@thm-field-basic-properties (d)), and the display would read \( 0 = 1 \), against (F7) in \( L \). So \( \varphi(a) \ne 0 \), and the display says that \( \varphi(a^{-1}) \) is an inverse of \( \varphi(a) \); by the uniqueness of inverses (@thm-field-basic-properties (c)), \( \varphi(a^{-1}) = \varphi(a)^{-1} \).

(c) Let \( \varphi(a) = \varphi(b) \). By (a), \( \varphi(a - b) = \varphi(a) - \varphi(b) = 0 \). By (b), read contrapositively, an element whose image is \( 0 \) is \( 0 \); so \( a - b = 0 \), and \( a = b \) (add \( b \) to both sides, with (F2), (F1), (F4) and (F3)). So \( \varphi \) is injective.

(d) We use @prp-subfield-test (c) for \( \varphi(F) \subseteq L \). First, \( 1 = \varphi(1) \in \varphi(F) \). Next, two elements of \( \varphi(F) \) are \( \varphi(a) \), \( \varphi(b) \) with \( a, b \in F \) (@fd2:def-image), and \( \varphi(a) - \varphi(b) = \varphi(a - b) \in \varphi(F) \) by (a). If moreover \( \varphi(b) \ne 0 \), then \( b \ne 0 \), since \( \varphi(0) = 0 \); so by (b), \( \varphi(a)\varphi(b)^{-1} = \varphi(a)\varphi(b^{-1}) = \varphi(ab^{-1}) \in \varphi(F) \). Hence \( \varphi(F) \) is a subfield of \( L \), a field with the operations of \( L \) (@prp-subfield-test (a)). The map \( \varphi \colon F \to \varphi(F) \) still satisfies the three clauses, since the operations of \( \varphi(F) \) are those of \( L \) and its one is \( 1_L \); it is surjective by the definition of the image, and injective by (c). So it is an isomorphism.

(e) For the composite, \( (\psi \circ \varphi)(a + b) = \psi(\varphi(a) + \varphi(b)) = \psi(\varphi(a)) + \psi(\varphi(b)) \), likewise for products, and \( \psi(\varphi(1)) = \psi(1) = 1 \) (@fd2:def-composition). Now let \( \varphi \) be an isomorphism, with inverse function \( \varphi^{-1} \colon L \to F \) (@fd2:def-inverse-function, which exists by @fd2:thm-bijection-iff-inverse). For \( x, y \in L \),
\[
\varphi\bigl(\varphi^{-1}(x) + \varphi^{-1}(y)\bigr) = \varphi(\varphi^{-1}(x)) + \varphi(\varphi^{-1}(y)) = x + y = \varphi\bigl(\varphi^{-1}(x + y)\bigr) ,
\]
so \( \varphi^{-1}(x) + \varphi^{-1}(y) = \varphi^{-1}(x + y) \), because \( \varphi \) is injective. The same computation with products gives \( \varphi^{-1}(x)\varphi^{-1}(y) = \varphi^{-1}(xy) \). And \( \varphi(1) = 1 \) gives \( \varphi^{-1}(1) = 1 \). The function \( \varphi^{-1} \) is bijective, with inverse \( \varphi \) (@fd2:thm-bijection-iff-inverse); so it is an isomorphism. The identity satisfies the three clauses trivially and is bijective.

(f) By induction on \( n \) (@fd1:ax-induction, read on \( \nN = \omega \) through @fd3:cor-omega-identification). For \( n = 0 \): \( \varphi(0 \cdot a) = \varphi(0) = 0 = 0 \cdot \varphi(a) \) by (a), and \( \varphi(a^0) = \varphi(1) = 1 = \varphi(a)^0 \). If the two formulas hold for \( n \), then
\[
\begin{aligned}
\varphi((n + 1) \cdot a) &= \varphi(n \cdot a + a) = n \cdot \varphi(a) + \varphi(a) = (n + 1) \cdot \varphi(a) , \\
\varphi(a^{n+1}) &= \varphi(a^n a) = \varphi(a)^n \varphi(a) = \varphi(a)^{n+1} .
\end{aligned}
\]
This proves the proposition.
:::

The answer to the prompt. In (c), \( \varphi(1) = 1 \) enters through (b): the display \( \varphi(a)\varphi(a^{-1}) = 1 \) is what makes \( \varphi(a) = 0 \) impossible. The zero map \( F \to L \) satisfies the two other clauses, sends every element to \( 0 \), and is not injective. A map that respected sums and products but sent \( 1 \) to \( 0 \) would be the zero map: \( \varphi(a) = \varphi(a \cdot 1) = \varphi(a)\varphi(1) = \varphi(a) \cdot 0 = 0 \), by (F7), the product clause, \( \varphi(1) = 0 \), and @thm-field-basic-properties (d) with (F6) in \( L \).

We call the move of this proof **push the equation through \( \varphi \)**: to learn \( \varphi(x) \), apply \( \varphi \) to an equation that \( x \) satisfies, and solve the resulting equation in \( L \). By (c) and (d), a homomorphism \( F \to L \) is the same thing as a copy of \( F \) inside \( L \): \( F \cong \varphi(F) \), a subfield of \( L \). By (e) and @fd2:thm-composition-injective-surjective (c), composing isomorphisms gives isomorphisms, so \( \cong \) is reflexive, symmetric and transitive on any set of fields.

::: {.warning}
A bijection that respects addition alone is not an isomorphism. The map \( f \colon \nQ \to \nQ \), \( f(x) \coloneqq 2x \), is bijective (its inverse is \( x \mapsto x/2 \)) and satisfies \( f(a + b) = f(a) + f(b) \), by (F9). But \( f(1 \cdot 1) = 2 \), while \( f(1)f(1) = 4 \); and \( f(1) = 2 \ne 1 \). All three clauses of @def-field-homomorphism must be checked.
:::

::: {.check}
Is \( a \mapsto -a \) a homomorphism \( \nQ \to \nQ \)?
:::

::: {.solution}
No. It sends \( 1 \) to \( -1 \), and \( -1 \ne 1 \) in \( \nQ \): if \( -1 = 1 \), then \( 1 + 1 = 1 + (-1) = 0 \), while \( 1 + 1 = 2 \cdot 1 > 0 \) in the ordered field \( \nQ \) (@fd3:prp-ordered-ring-rules (h), @fd3:thm-rationals-ordered-field). (In \( \nF_2 \), where \( -1 = 1 \), the same map is the identity.) It also fails the product clause: \( 1 \cdot 1 = 1 \) is sent to \( -1 \), while the product of the images is \( (-1)(-1) = 1 \) (@fd3:prp-ring-algebra (c)). It does respect sums, by @fd3:prp-ring-algebra (c) and (F9): \( -(a + b) = (-1)(a + b) = -a + (-b) \).
:::

## Examples, and pairs of fields with no map between them

::: {#exm-complex-conjugation-automorphism}
[Conjugation and Other Automorphisms]

::: {.enumerate options="label=(\roman*)"}
1. Show that conjugation \( z \mapsto \conj{z} \) is an automorphism of \( \nC \), that it is not the identity, and that \( \conj{z} = z \) if and only if \( z \in \nR \).
2. Let \( K \) be a subfield of \( L \). Show that the inclusion \( K \to L \), \( x \mapsto x \), is a homomorphism, and that it is not surjective when \( K \ne L \).
3. Recall why \( a + b\sqrt 2 \mapsto a - b\sqrt 2 \) is an automorphism of \( \nQ(\sqrt 2) \).
4. Which automorphisms does \( \nR \) have?
:::
:::

::: {.solution}
(i) By @thm-conjugate-properties (a), (b), \( \conj{z + w} = \conj{z} + \conj{w} \) and \( \conj{zw} = \conj{z}\,\conj{w} \); and \( \conj{1} = \conj{1 + 0i} = 1 - 0i = 1 \) (@def-conjugate-modulus). So conjugation is a homomorphism. By @thm-conjugate-properties (a), \( \conj{\conj{z}} = z \), so conjugation is its own inverse, hence bijective (@fd2:thm-bijection-iff-inverse): an automorphism. It is not the identity: \( \conj{i} = -i \), and \( -i \ne i \), since \( i - (-i) = 2i = (0, 2) \ne (0, 0) \).

For the fixed elements, let \( z = a + bi \) with \( a, b \in \nR \). Then \( \conj{z} = a - bi \) (@def-conjugate-modulus), and comparing parts (@def-complex-numbers), \( \conj{z} = z \) if and only if \( -b = b \), that is \( 2b = 0 \), that is \( b = 0 \) (as \( 2 = 2 \cdot 1 > 0 \) in the ordered field \( \nR \), @fd3:thm-reals-ordered-field, @fd3:prp-ordered-ring-rules (h), so \( 2 \ne 0 \), and by @thm-field-basic-properties (f)). And \( b = 0 \) says \( z = a + 0i = a \in \nR \) (@prp-reals-embed-complex). This fact is not among the parts of @thm-conjugate-properties; the two lines above prove it.

(ii) The operations of \( K \) are those of \( L \), and \( 1_K = 1_L \) (@prp-subfield-test (a)). So \( x \mapsto x \) satisfies the three clauses. If \( K \ne L \), some element of \( L \) is not in \( K \), and it is not a value of the inclusion.

(iii) This is @fd3:exm-cof-sqrt2-conjugation, recalled and not proved again: unique representation makes the formula a function, the product formula of @exm-q-sqrt2-field with \( -b \), \( -d \) in place of \( b \), \( d \) shows that products go to products, and the map is its own inverse.

(iv) Only the identity. *Number Systems: From \(\nN\) to \(\nR\)*, Chapter 6, proved that a map \( \sigma \colon \nR \to \nR \) with \( \sigma(a + b) = \sigma(a) + \sigma(b) \), \( \sigma(ab) = \sigma(a)\sigma(b) \) and \( \sigma(1) = 1 \), that is, a homomorphism \( \nR \to \nR \), is the identity, with no order condition assumed (@fd3:thm-cof-field-automorphism-identity, with \( \nR \) complete by @fd3:thm-reals-complete-ordered-field). So \( \nC \) has a symmetry and \( \nR \) has none. Section 2.5 shows that \( \nQ \) and every \( \nF_p \) have no automorphism other than the identity either.
:::

Pushing an equation through \( \varphi \) also proves that no homomorphism exists: an equation that holds in \( F \) and has no counterpart in \( L \) leaves \( \varphi \) nowhere to go.

::: {#exm-field-homomorphism-obstructions}
[Pairs of Fields with No Homomorphism]

Show that there is no homomorphism (i) \( \nC \to \nR \); (ii) \( \nF_2 \to \nQ \); (iii) \( \nQ \to \nF_p \), for any prime \( p \). (iv) Which clause of @def-field-homomorphism does the zero map \( \nQ \to \nQ \) fail?
:::

::: {.solution}
(i) Suppose \( \varphi \colon \nC \to \nR \) is a homomorphism. In \( \nC \), \( i^2 = -1 \). Pushing this through \( \varphi \),
\[
\varphi(i)^2 = \varphi(i^2) = \varphi(-1) = -\varphi(1) = -1 ,
\]
by (f) and (a) of @prp-field-homomorphism-properties. But \( \nR \) is an ordered field (@fd3:thm-reals-ordered-field), in which every square is \( \ge 0 \) and \( 1 > 0 \), so \( -1 < 0 \) (@fd3:prp-ordered-ring-rules (e), (a)). So \( \varphi(i)^2 = -1 \) is impossible.

(ii) Suppose \( \varphi \colon \nF_2 \to \nQ \) is a homomorphism. In \( \nF_2 \), \( 1 + 1 = 0 \) (@exm-finite-fields). Pushing it through \( \varphi \), \( 1 + 1 = \varphi(1) + \varphi(1) = \varphi(1 + 1) = \varphi(0) = 0 \) in \( \nQ \), by (a). But \( 1 + 1 = 2 \cdot 1 > 0 \) in the ordered field \( \nQ \) (@fd3:prp-ordered-ring-rules (h), @fd3:thm-rationals-ordered-field). So no such \( \varphi \) exists.

(iii) Suppose \( \varphi \colon \nQ \to \nF_p \) is a homomorphism. In \( \nF_p \), \( p \cdot 1 = 0 \) (@fd3:thm-integers-mod-n-ring (d)). By @prp-field-homomorphism-properties (f), \( \varphi(p \cdot 1) = p \cdot \varphi(1) = p \cdot 1 = 0 = \varphi(0) \), and \( \varphi \) is injective by (c), so \( p \cdot 1 = 0 \) in \( \nQ \). But \( p \cdot 1 > 0 \) in \( \nQ \), as in (ii), since \( p \ge 1 \). So no such \( \varphi \) exists.

(iv) The zero map \( a \mapsto 0 \) respects sums and products, since \( 0 + 0 = 0 \) and \( 0 \cdot 0 = 0 \), and it sends \( 1 \) to \( 0 \ne 1 \). So it fails only \( \varphi(1) = 1 \), and is not a homomorphism.

Section 2.5 explains (ii) and (iii) at once: both pairs of fields differ in the number of copies of \( 1 \) that add up to \( 0 \).
:::

## Exercises

### A. Check your understanding

::: {#exr-field-homomorphisms-a1}
[A1]

These parts are about @prp-field-homomorphism-properties, mainly its part (c).

::: {.enumerate options="label=(\alph*)"}
1. Where in the proof of (c) is the clause \( \varphi(1) = 1 \) used?
2. Let \( \zeta \colon \nQ \to \nQ \) be the zero map. Which clause of @def-field-homomorphism fails? Which of the conclusions (a)–(f) fail for \( \zeta \)?
3. Run the proof of (c) with conjugation on \( \nC \) and the elements \( a = 1 + i \), \( b = 1 - i \): compute \( a - b \), its image, and conclude.
4. State the idea of the proof of (c) in two sentences.
:::
:::

::: {.solution}
(a) In (b), which (c) cites: \( \varphi(a)\varphi(a^{-1}) = \varphi(aa^{-1}) = \varphi(1) = 1 \), and \( 1 \ne 0 \), so \( \varphi(a) \ne 0 \) for \( a \ne 0 \).

(b) The clause \( \zeta(1) = 1 \) fails: \( \zeta(1) = 0 \). Conclusion (a) holds (\( \zeta(0) = 0 = -0 \)). Conclusion (b) fails: \( 1 \ne 0 \) and \( \zeta(1) = 0 \). Conclusion (c) fails: \( \zeta(1) = \zeta(2) \). Conclusion (d) fails: the image \( \{0\} \) does not contain \( 1 \), so it is not a subfield. Conclusion (f) holds for multiples (both sides are \( 0 \)) and fails for powers at \( n = 0 \): \( \zeta(a^0) = \zeta(1) = 0 \), while \( \zeta(a)^0 = 1 \). Conclusion (e) fails in its first clause: for a homomorphism \( \psi \colon \nQ \to M \) (for example \( \psi = \id_{\nQ} \)), \( \psi \circ \zeta \) is the zero map, since \( \psi(0) = 0 \) by (a) for \( \psi \), and the zero map sends \( 1 \) to \( 0 \), so it is not a homomorphism. The clause about inverses holds vacuously, since \( \zeta \) is not bijective, and the clause about \( \id_F \) does not involve \( \zeta \).

(c) \( a - b = 2i \ne 0 \). Its image is \( \conj{2i} = -2i \ne 0 \), as (b) predicts; so \( \conj{a} - \conj{b} = \conj{a - b} \ne 0 \), and \( \conj{a} \ne \conj{b} \). Indeed \( \conj{a} = 1 - i \) and \( \conj{b} = 1 + i \).

(d) A non-zero element has an inverse, so its image times another image is \( \varphi(1) = 1 \ne 0 \); hence a homomorphism sends no non-zero element to \( 0 \). Applied to a difference \( a - b \), this says that different elements have different images.
:::

### B. Practice

::: {#exr-field-homomorphisms-b1}
[B1: Images of quotients]

Let \( \varphi \colon F \to L \) be a homomorphism, and let \( a, b \in F \) with \( b \ne 0 \). Prove that \( \varphi(a/b) = \varphi(a)/\varphi(b) \). Here is the start of a proof. *Name the move, then complete it.*

"Since \( a = (a/b) \cdot b \), applying \( \varphi \) gives \( \varphi(a) = \varphi(a/b)\,\varphi(b) \). …"
:::

::: {.solution}
*The move* is **push the equation through \( \varphi \)**: the equation \( a = (a/b)b \), which holds since \( (ab^{-1})b = a(b^{-1}b) = a \) by (F5), (F6), (F8) and (F7), is carried to \( L \) and solved there.

*Completion.* Since \( b \ne 0 \), \( \varphi(b) \ne 0 \) by @prp-field-homomorphism-properties (b), so \( \varphi(b)^{-1} \) exists. Multiplying \( \varphi(a) = \varphi(a/b)\varphi(b) \) by \( \varphi(b)^{-1} \), with (F5), (F8) and (F7),
\[
\varphi(a)\varphi(b)^{-1} = \varphi(a/b)\,\varphi(b)\varphi(b)^{-1} = \varphi(a/b) .
\]
That is, \( \varphi(a/b) = \varphi(a)/\varphi(b) \).
:::

::: {#exr-field-homomorphisms-b2}
[B2: The automorphisms of the rational complex numbers]

Show that \( \nQ(i) \) (@exm-subfields-gaussian) has exactly two automorphisms: the identity and conjugation \( a + bi \mapsto a - bi \). Here is the first half of a proof. *Name the move, then complete it.*

"Let \( \sigma \) be an automorphism of \( \nQ(i) \). It fixes every rational: \( \sigma(n) = \sigma(n \cdot 1) = n \cdot \sigma(1) = n \) for \( n \in \nN \) by @prp-field-homomorphism-properties (f), \( \sigma(-n) = -\sigma(n) = -n \) by (a), and \( \sigma(m/n) = \sigma(m)/\sigma(n) = m/n \) for \( m \in \nZ \), \( n \in \nZ_{>0} \), by @exr-field-homomorphisms-b1. Moreover \( i^2 = -1 \). …"
:::

::: {.solution}
*The move* is **push the equation through \( \sigma \)**, applied to \( i^2 = -1 \).

*Completion.* Every rational is \( m/n \) with \( m \in \nZ \), \( n \in \nZ_{>0} \) (@fd3:prp-integers-embed-rationals (b)), so \( \sigma(q) = q \) for every \( q \in \nQ \). Applying \( \sigma \) to \( i^2 = -1 \),
\[
\sigma(i)^2 = \sigma(i^2) = \sigma(-1) = -1 = i^2 .
\]
By @cor-field-squares-equal in the field \( \nQ(i) \), \( \sigma(i) = i \) or \( \sigma(i) = -i \). For \( a, b \in \nQ \), \( \sigma(a + bi) = \sigma(a) + \sigma(b)\sigma(i) = a + b\,\sigma(i) \). So either \( \sigma(a + bi) = a + bi \) for all \( a, b \), and \( \sigma \) is the identity, or \( \sigma(a + bi) = a - bi \) for all \( a, b \), and \( \sigma \) is conjugation. There are at most these two.

Both occur. The identity is an automorphism (@prp-field-homomorphism-properties (e)). Conjugation sends \( a + bi \) to \( a + (-b)i \in \nQ(i) \), so it maps \( \nQ(i) \) into itself; it respects sums and products and sends \( 1 \) to \( 1 \) because conjugation on \( \nC \) does (@exm-complex-conjugation-automorphism (i)) and the operations of \( \nQ(i) \) are those of \( \nC \); and it is its own inverse on \( \nQ(i) \), hence bijective. The two are different maps, since conjugation sends \( i \in \nQ(i) \) to \( -i \ne i \) (@exm-complex-conjugation-automorphism (i)). So \( \nQ(i) \) has exactly two automorphisms.
:::

::: {#exr-field-homomorphisms-b3}
[B3]

Let \( F \) be the field of @exr-field-axioms-b3 (a): the set \( \nQ \) with the usual sum and the product \( a \odot b \coloneqq 2ab \). Show that \( f \colon F \to \nQ \), \( f(x) \coloneqq 2x \), is an isomorphism of fields, so \( F \cong \nQ \). Compare with the warning of this section.
:::

::: {.solution}
The one of \( F \) is \( 1/2 \): \( a \odot \tfrac12 = 2a \cdot \tfrac12 = a \). We check the three clauses, with \( \nQ \)'s usual product on the right. Sums: \( f(a + b) = 2a + 2b = f(a) + f(b) \), by (F9). Products: \( f(a \odot b) = 2(2ab) = (2a)(2b) = f(a)f(b) \), by (F5) and (F6). One: \( f(1/2) = 1 \). The map is bijective, with inverse \( x \mapsto x/2 \): \( 2(x/2) = x \) and \( (2x)/2 = x \) (@fd2:thm-bijection-iff-inverse). So \( f \) is an isomorphism.

The warning used the same formula \( x \mapsto 2x \) as a map \( \nQ \to \nQ \), with the usual product on **both** sides, and it is not a homomorphism there. Whether a map is a homomorphism depends on the operations of the source as well as on the formula: on \( F \), the product \( \odot \) contains the factor \( 2 \) that the formula needs.
:::

::: {#exr-field-homomorphisms-b4}
[B4: The fixed field]

Let \( \sigma \) be an automorphism of a field \( F \). Show that its **fixed set** \( \{ a \in F : \sigma(a) = a \} \) is a subfield of \( F \). Find the fixed set of conjugation on \( \nC \) and of conjugation on \( \nQ(\sqrt 2) \).
:::

::: {.solution}
Write \( K \) for the fixed set, and use @prp-subfield-test (c). \( \sigma(1) = 1 \), so \( 1 \in K \). For \( a, b \in K \), \( \sigma(a - b) = \sigma(a) - \sigma(b) = a - b \) by @prp-field-homomorphism-properties (a), so \( a - b \in K \). If moreover \( b \ne 0 \), then \( \sigma(ab^{-1}) = \sigma(a)\sigma(b)^{-1} = ab^{-1} \) by (b), so \( ab^{-1} \in K \). Hence \( K \) is a subfield. (Only the homomorphism property was used.)

For conjugation on \( \nC \), \( K = \nR \), by @exm-complex-conjugation-automorphism (i).

For conjugation on \( \nQ(\sqrt 2) \), \( a - b\sqrt 2 = a + b\sqrt 2 \) holds if and only if \( 2b\sqrt 2 = 0 \), that is, \( b = 0 \): in the ordered field \( \nR \), \( 2 = 2 \cdot 1 > 0 \) (@fd3:prp-ordered-ring-rules (h), @fd3:thm-reals-ordered-field), so \( 2 \ne 0 \), and \( \sqrt 2 \ne 0 \) (since \( 0^2 = 0 \ne 2 \)), and a product of non-zero elements is non-zero (@thm-field-basic-properties (f)). So \( K = \{ a + 0\sqrt 2 : a \in \nQ \} = \nQ \).
:::

### C. Going deeper

::: {#exr-field-homomorphisms-c1}
[C1: Isomorphic fields have the same square roots of minus one]

(a) Let \( F \cong L \). Prove that \( F \) has an element \( x \) with \( x^2 = -1 \) if and only if \( L \) has one.

(b) Deduce that \( \nQ(i) \not\cong \nQ(\sqrt 2) \) and that \( \nC \not\cong \nR \).
:::

::: {.solution}
(a) Let \( \varphi \colon F \to L \) be an isomorphism. If \( x \in F \) has \( x^2 = -1 \), then by @prp-field-homomorphism-properties (f) and (a),
\[
\varphi(x)^2 = \varphi(x^2) = \varphi(-1) = -\varphi(1) = -1 ,
\]
so \( \varphi(x) \in L \) is such an element. Conversely, \( \varphi^{-1} \colon L \to F \) is an isomorphism (@prp-field-homomorphism-properties (e)), and the same computation carries an element \( y \in L \) with \( y^2 = -1 \) to \( \varphi^{-1}(y) \in F \) with \( \varphi^{-1}(y)^2 = -1 \).

(b) In \( \nQ(i) \), \( i^2 = -1 \). In \( \nQ(\sqrt 2) \subseteq \nR \), every \( y \) has \( y^2 \ge 0 > -1 \), since \( \nR \) is an ordered field (@fd3:thm-reals-ordered-field, @fd3:prp-ordered-ring-rules (e), (a)); so \( \nQ(\sqrt 2) \) has no such element, and by (a), \( \nQ(i) \not\cong \nQ(\sqrt 2) \). Likewise \( i \in \nC \) and no element of \( \nR \) squares to \( -1 \), so \( \nC \not\cong \nR \).

The same argument works for any statement written with \( + \), \( \cdot \), \( 0 \), \( 1 \) and elements: an isomorphism carries it in both directions. (For \( \nC \) and \( \nR \), @exm-field-homomorphism-obstructions (i) shows more: there is no homomorphism \( \nC \to \nR \) at all.)

**Marking scheme.** (10 points)
- 3: pushes \( x^2 = -1 \) through \( \varphi \), with \( \varphi(-1) = -1 \) justified (by (a) and \( \varphi(1) = 1 \)).
- 3: the converse, by either route: through \( \varphi^{-1} \), with the fact that it is an isomorphism (or a homomorphism) justified (@prp-field-homomorphism-properties (e)); or directly, writing \( y = \varphi(x) \) by surjectivity, getting \( \varphi(x^2) = \varphi(-1) \), and concluding \( x^2 = -1 \) by injectivity.
- 2: no element of \( \nQ(\sqrt 2) \) (or of \( \nR \)) squares to \( -1 \), from the order of \( \nR \).
- 2: both conclusions of (b) drawn from (a).
Fatal errors (0 for the step): treating \( \nQ(\sqrt 2) \not\cong \nQ(i) \) as evident because the sets "look different"; using \( \varphi(-1) = -1 \) without (a).
:::

::: {#exr-field-homomorphisms-c2}
[C2: Find the error]

Here is an argument. Is its conclusion true? Does the argument prove it? If not, name the line that fails and why.

"Every homomorphism \( \varphi \colon \nQ \to \nQ \) is the identity. (1) By definition, \( \varphi(1) = 1 \), and \( \varphi \) respects sums. (2) For \( x \in \nQ \), \( \varphi(x) = \varphi(x \cdot 1) = x\,\varphi(1) \). (3) Hence \( \varphi(x) = x \cdot 1 = x \)."
:::

::: {.solution}
The conclusion is **true**: the repair below proves it, and Section 2.5 proves it again by another route. The argument does not prove it.

*Line (2) fails*, at the second equality. "\( \varphi(x \cdot 1) = x\,\varphi(1) \)" pulls the factor \( x \) out of \( \varphi \), as if \( \varphi \) were compatible with multiplication by a scalar \( x \); that is not a clause of @def-field-homomorphism, and nothing proved so far supplies it. So the line cites a general "fact" that is not available, entry (N9) of @fd1:exm-not-allowed-catalogue. The clause that is available, multiplicativity, gives only \( \varphi(x \cdot 1) = \varphi(x)\varphi(1) = \varphi(x) \), which proves nothing.

*Counterexample to the step* (in its general form, "a homomorphism satisfies \( \varphi(x \cdot 1) = x\,\varphi(1) \)"): conjugation on \( \nC \) has \( \conj{i \cdot 1} = -i \), while \( i \cdot \conj{1} = i \).

*Repair.* For \( n \in \nN \), \( \varphi(n \cdot 1) = n \cdot \varphi(1) = n \cdot 1 \) by @prp-field-homomorphism-properties (f), and \( n \cdot 1 = n \) in \( \nQ \); so \( \varphi(n) = n \). For \( n \in \nN \), \( \varphi(-n) = -\varphi(n) = -n \) by (a), so \( \varphi(m) = m \) for every \( m \in \nZ \) (@fd3:prp-naturals-embed-integers (c)). Every rational is \( m/n \) with \( m \in \nZ \), \( n \in \nZ_{>0} \) (@fd3:prp-integers-embed-rationals (b)), and \( \varphi(m/n) = \varphi(m)/\varphi(n) = m/n \) by @exr-field-homomorphisms-b1. So \( \varphi = \id_{\nQ} \).
:::

<!-- dependency ledger
prp-field-homomorphism-properties (proof): powers a^n in a field and the power laws | fd2:def-power and fd2:prp-power-laws as templates with F in place of the school R (fd2:thm-recursion read on omega); proofs use only (F1)-(F7), (F9) and induction; stated in the section's opening paragraph
prp-field-homomorphism-properties (proof): multiples n.a in a commutative ring | F3.2 Section 2.3 "Multiples" (cited by position, recalled in the opening paragraph)
prp-field-homomorphism-properties (proof): a - b = 0 implies a = b | (F1), (F2), (F3), (F4), named inline
prp-field-homomorphism-properties (claim): composite of bijections is bijective (transitivity of isomorphism) | fd2:thm-composition-injective-surjective (c), cited
prp-field-homomorphism-properties (claim): x.0 = 0 in L (a map sending 1 to 0 is zero) | thm-field-basic-properties (d) with (F6), cited
def-field-homomorphism (claim): (check) -1 != 1 in Q | fd3:prp-ordered-ring-rules (h), fd3:thm-rationals-ordered-field, cited
prp-field-homomorphism-properties (proof): the image of phi is the set of values | fd2:def-image, cited
def-field-homomorphism (claim): conjugation of Q(sqrt 2) is not order-preserving, sqrt 2 > 0 | fd3:exm-cof-sqrt2-conjugation (soft citation of F3.4, remark only)
exm-complex-conjugation-automorphism (solution): i - (-i) = 2i = (0, 2) != (0, 0); 2 != 0 in R; 2b = 0 implies b = 0 | def-complex-numbers (F4.1, see edge; example only); 2 = 2.1 > 0, fd3:prp-ordered-ring-rules (h), fd3:thm-reals-ordered-field; thm-field-basic-properties (f)
exm-complex-conjugation-automorphism (solution): R is a complete ordered field (hypothesis of fd3:thm-cof-field-automorphism-identity) | fd3:thm-reals-complete-ordered-field, cited
exm-complex-conjugation-automorphism (solution): the product formula of Q(sqrt 2) with -b, -d gives sigma(xy) = sigma(x) sigma(y) | exm-q-sqrt2-field; recalled from fd3:exm-cof-sqrt2-conjugation
exm-field-homomorphism-obstructions (solution): 1 + 1 = 2.1 > 0 and p.1 > 0 in Q | fd3:prp-ordered-ring-rules (h), fd3:thm-rationals-ordered-field, cited
exr-field-homomorphisms-b2 (solution): n.1 = n in Q(i) for n in N (rationals inside C) | n.1 = n in Q (F3.2: j and the identifications preserve +), and Q a subfield of C (exm-subfields-gaussian (iii)); the given first half of the exercise uses it
exr-field-homomorphisms-c2 (solution): n.1 = n in Q for n in N | F3.2 Section 2.3 "Multiples" remark (n.a = na in Z) with fd3:prp-integers-embed-rationals (j preserves sums), by induction
exr-field-homomorphisms-b4 (solution): 2 != 0 and sqrt 2 != 0 in R | 2 = 2.1 > 0, fd3:prp-ordered-ring-rules (h), fd3:thm-reals-ordered-field; sqrt 2 != 0 inline (0^2 = 0 != 2)
exr-field-homomorphisms-b3 (solution): (Q, +, odot) is a field with one 1/2 | exr-field-axioms-b3 (a), an exercise cited by an exercise solution only
exr-field-homomorphisms-a1 (solution): conj(2i) = -2i; conj(1 + i) = 1 - i | def-conjugate-modulus (F4.1, see edge; exercise only); verify/ch02/exr-field-homomorphisms-a1.py
prp-field-homomorphism-properties (claim): the warning's f(1.1) = 2 != 4 = f(1)f(1); B3's f(a odot b) = f(a)f(b), f(1/2) = 1 | inline; verify/ch02/exr-field-homomorphisms-a1.py, verify/ch02/exr-field-homomorphisms-b3.py
-->
