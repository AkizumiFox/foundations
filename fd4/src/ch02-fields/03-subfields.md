# Subfields

The fields met so far sit inside one another. \( \nQ \subseteq \nR \subseteq \nC \), and each is a field with the sum and product of the next: \( \nQ \) inside \( \nR \) through the identification of *Number Systems: From \(\nN\) to \(\nR\)*, Section 5.4 (@fd3:def-rational-embedding), and \( \nR \) inside \( \nC \) through @prp-reals-embed-complex. Between \( \nQ \) and \( \nR \) lies the set \( \nQ(\sqrt 2) \) of numbers \( a + b\sqrt 2 \) with \( a, b \) rational. Sums and products of two such numbers are again of that form, but is \( 1/(1 + 2\sqrt 2) \)? This section gives a short test that settles such questions once, and it finds, inside every field, a smallest field.

Throughout, \( a - b \coloneqq a + (-b) \) and \( a/b \coloneqq ab^{-1} \) for \( b \ne 0 \), as in @def-field, and the rules of @thm-field-basic-properties are used freely, each cited by its letter.

## Fields inside fields

A subset \( K \) of a field \( L \) inherits two operations, but only in a weak sense: \( a + b \) and \( ab \) are defined for \( a, b \in K \), as elements of \( L \). For \( K \) to be a field with these operations, the sum and the product must land in \( K \), and the elements that the axioms (F3), (F4), (F7) and (F8) ask for must be found in \( K \). The natural guess is that nothing else needs checking.

*A subfield is a subset that a field's own arithmetic never leaves.*

::: {#def-subfield}
[Subfield]

Let \( L \) be a field. A **subfield** of \( L \) is a subset \( K \subseteq L \) such that

- \( 0 \in K \) and \( 1 \in K \);
- \( K \) is **closed under sums and products**: \( a + b \in K \) and \( ab \in K \) **for all** \( a, b \in K \);
- \( K \) is **closed under negatives**: \( -a \in K \) **for every** \( a \in K \);
- \( K \) is **closed under inverses**: \( a^{-1} \in K \) **for every non-zero** \( a \in K \).

Here \( 0 \), \( 1 \), \( + \), \( \cdot \), \( -a \) and \( a^{-1} \) are those of \( L \).
:::

In words: the first clause asks for the two special elements of \( L \); the second says that the operations of \( L \) do not leave \( K \); the last two say that the negatives and inverses which \( L \) provides already lie in \( K \).

**Examples.**

- **\( L \) itself** is a subfield of \( L \). It is the largest one, and the degenerate case: every clause holds because \( K = L \).
- **\( \nQ \) in \( \nR \).** Under the identification of a rational \( q \) with \( \kappa(q) \in \nR \), the embedding \( \kappa \) sends \( 0 \), \( 1 \), sums, products, negatives and inverses of rationals to the same things in \( \nR \) (@fd3:thm-rational-embedding (a), (c)). So all four clauses hold, and \( \nQ \) is a subfield of \( \nR \).
- **\( \nR \) in \( \nC \).** Chapter 1 checked the four clauses for the copy of \( \nR \) in \( \nC \). The zero \( 0 = (0, 0) \) and the one \( 1 = (1, 0) \) of \( \nC \) (@prp-complex-arithmetic-laws (d)) are the real numbers \( 0 \) and \( 1 \) under the identification \( a = (a, 0) \) that follows @prp-reals-embed-complex, and @thm-complex-numbers-field gives closure under sums, products, negatives and inverses. So \( \nR \) is a subfield of \( \nC \), and so is \( \nQ \), since a subfield of a subfield is a subfield: each clause of the inner one is a statement about the operations of the outer field.

**Non-examples.**

- \( \{0\} \subseteq \nQ \) is closed under sums, products, negatives and inverses (the last vacuously), and does not contain \( 1 \), since \( 1 \ne 0 \) in a field.
- \( \nN \subseteq \nQ \) contains \( 0 \) and \( 1 \) and is closed under sums and products, but not under negatives, since \( -1 \notin \nN \), nor under inverses, since \( 2^{-1} = 1/2 \notin \nN \) (as for \( \nZ \) below).
- \( \nZ \subseteq \nQ \) satisfies every clause except closure under inverses: \( 2^{-1} = 1/2 \notin \nZ \), since \( 2x = 1 \) has no solution \( x \in \nZ \) (@fd3:cor-integers-even-odd (a)).

These are the non-examples (i)–(iii) of @exm-field-nonexamples, now seen from inside \( \nQ \) (the fourth, \( \nZ/6\nZ \), is not a subset of \( \nQ \)): each fails as a subfield exactly where it failed as a field.

## The subfield test

The guess above is right, and it comes with a converse and a shortcut. The converse says that a subset closed under the operations which happens to be a field cannot have its own zero or one: they must be those of \( L \). The shortcut, part (c), reduces the four clauses to three checks.

::: {#prp-subfield-test}
[The Subfield Test]

Let \( L \) be a field and \( K \subseteq L \).

::: {.enumerate options="label=(\alph*)"}
1. If \( K \) is a subfield of \( L \), then \( K \), with the restrictions of \( + \) and \( \cdot \) to \( K \times K \), is a field (@def-field). Its zero is \( 0_L \), its one is \( 1_L \), and the negative and the inverse of an element of \( K \) are those of \( L \).
2. Conversely, suppose that \( a + b \in K \) and \( ab \in K \) for all \( a, b \in K \), and that \( K \) with the restricted operations is a field. Then \( K \) is a subfield of \( L \): its zero \( 0_K \) is \( 0_L \), its one \( 1_K \) is \( 1_L \), and its negatives and inverses are those of \( L \).
3. \( K \) is a subfield of \( L \) **if and only if** \( 1 \in K \), \( a - b \in K \) for all \( a, b \in K \), and \( ab^{-1} \in K \) for all \( a, b \in K \) with \( b \ne 0 \).
:::
:::

::: {.idea}
(a) The axioms (F1), (F2), (F5), (F6) and (F9) are identities that hold **for all** elements of \( L \), so in particular for all elements of \( K \); nothing about \( K \) needs checking. The other axioms ask for elements, \( 0 \), \( -a \), \( 1 \), \( a^{-1} \), and the four clauses of @def-subfield put them in \( K \). We call this move **test inside the big field**: the identities come free, and only closure and the special elements cost anything.

(b) runs the other way. An equation true in \( K \) is an equation in \( L \), where cancellation and the uniqueness of negatives and inverses are available; so \( 0_K \) and \( 1_K \) are forced to be \( 0_L \) and \( 1_L \).

(c) builds \( 0 \), \( -b \), \( b^{-1} \), \( a + b \) and \( ab \) out of \( 1 \) and the two operations "subtract" and "divide".

*Before reading on: in (b), where is it used that \( L \) is a field, and not just a commutative ring?*
:::

::: {.proof}
(a) Since \( K \) is closed under sums and products, \( + \) and \( \cdot \) restrict to functions \( K \times K \to K \). Axioms (F1), (F2), (F5), (F6) and (F9) hold for all elements of \( L \), hence for all elements of \( K \). (F3): \( 0 \in K \), and \( a + 0 = a \) for \( a \in K \). (F4): for \( a \in K \), \( -a \in K \) by closure under negatives, and \( a + (-a) = 0 \). (F7): \( 1 \in K \), \( a \cdot 1 = a \) for \( a \in K \), and \( 1 \ne 0 \) because this holds in \( L \). (F8): for non-zero \( a \in K \), \( a^{-1} \in K \) by closure under inverses, and \( aa^{-1} = 1 \). So \( K \) is a field, and \( 0_L \), \( 1_L \), \( -a \), \( a^{-1} \) witness its axioms; by the uniqueness of these elements in the field \( K \) (@thm-field-basic-properties (a), (c), applied in \( K \)), they are its zero, its one, its negatives and its inverses.

(b) Write \( 0_K \), \( 1_K \) for the zero and one of the field \( K \). In \( K \), \( 0_K + 0_K = 0_K \) by (F3); in \( L \), \( 0_K + 0_L = 0_K \). So \( 0_K + 0_K = 0_K + 0_L \) in \( L \), and additive cancellation in \( L \) (@thm-field-basic-properties (b)) gives \( 0_K = 0_L \). Next, \( 1_K \cdot 1_K = 1_K \) by (F7) in \( K \), and \( 1_K \cdot 1_L = 1_K \) by (F7) in \( L \). Since \( 1_K \ne 0_K = 0_L \), multiplicative cancellation in \( L \) (@thm-field-basic-properties (b)) gives \( 1_K = 1_L \). Now let \( a \in K \), and let \( x \in K \) be its negative in \( K \): \( a + x = 0_K = 0_L \), so \( x = -a \) by the uniqueness of negatives in \( L \) (@thm-field-basic-properties (c)). Likewise, if \( a \ne 0_K \), that is \( a \ne 0_L \), its inverse \( y \in K \) satisfies \( ay = 1_K = 1_L \), so \( y = a^{-1} \) by the uniqueness of inverses in \( L \). Hence \( 0_L, 1_L \in K \), \( K \) is closed under the negatives and inverses of \( L \), and with the hypothesis on sums and products, \( K \) is a subfield.

(c) \( (\Rightarrow) \) \( 1 \in K \) by definition. For \( a, b \in K \), \( -b \in K \), so \( a - b = a + (-b) \in K \), by closure under negatives and sums. For \( b \ne 0 \), \( b^{-1} \in K \), so \( ab^{-1} \in K \), by closure under inverses and products.

\( (\Leftarrow) \) First, \( 0 = 1 - 1 \in K \), since \( 1 + (-1) = 0 \) by (F4). For \( b \in K \), \( -b = 0 + (-b) = 0 - b \in K \), by (F1) and (F3). For non-zero \( b \in K \), \( b^{-1} = 1 \cdot b^{-1} \in K \), by (F6) and (F7). For \( a, b \in K \), \( -b \in K \) and \( -(-b) = b \) (@fd3:prp-ring-algebra (a)), so \( a + b = a - (-b) \in K \). For the product, let \( a, b \in K \). If \( b = 0 \), then \( ab = 0 \in K \) by @thm-field-basic-properties (d) and (F6). If \( b \ne 0 \), then \( b^{-1} \in K \), and \( b^{-1} \ne 0 \), since \( bb^{-1} = 1 \ne 0 \) while \( b \cdot 0 = 0 \); so \( a(b^{-1})^{-1} \in K \), and \( (b^{-1})^{-1} = b \) (@thm-field-basic-properties (g)) gives \( ab \in K \). So \( K \) contains \( 0 \) and \( 1 \) and is closed under sums, products, negatives and inverses: it is a subfield.
:::

The answer to the prompt. Part (b) uses that \( L \) is a field in the step \( 1_K \cdot 1_K = 1_K \cdot 1_L \Rightarrow 1_K = 1_L \): canceling the factor \( 1_K \) means multiplying by its inverse in \( L \), which exists because \( 1_K \ne 0 \) and (F8) holds in \( L \). The additive step uses only negatives, which every commutative ring has. The warning below shows the multiplicative step failing in a ring.

So to show that a subset is a field, we rarely check nine axioms: we check (c), three closure statements, and (a) does the rest.

::: {.warning}
A subset of a ring can be a field with **another** one. In the ring \( \nZ/6\nZ \), the subset \( \{[0], [3]\} \) is closed under \( + \) and \( \cdot \): \( [3] + [3] = [6] = [0] \) and \( [3][3] = [9] = [3] \). With these operations it is a field with two elements, a copy of \( \nF_2 \), but its one is \( [3] \), not \( [1] \). Part (b) has no counterpart here: \( [3][3] = [3][1] \), and \( [3] \) cannot be canceled, since \( \nZ/6\nZ \) is not a field.
:::

Likewise, a field structure with **other operations** does not make a subset a subfield: the set \( \{0, 1\} \subseteq \nQ \) with the tables of \( \nF_2 \) is a field, but it is not a subfield of \( \nQ \), because the sum of \( \nQ \) gives \( 1 + 1 = 2 \notin \{0, 1\} \).

## Square roots of two and of minus one

The question of the opening is now one application of the test. Recall that \( \nR \) is a complete ordered field (@fd3:thm-reals-complete-ordered-field), so by @fd3:prp-cof-square-roots there is exactly one \( r \in \nR \) with \( r \ge 0 \) and \( r^2 = 2 \), and \( \sqrt 2 \coloneqq r \). The set \( \nQ(\sqrt 2) \) is that of @fd3:def-cof-sqrt2-field.

::: {#exm-q-sqrt2-field}
[The Field Generated by the Square Root of Two]

Show that \( \nQ(\sqrt 2) \coloneqq \{ a + b\sqrt 2 : a, b \in \nQ \} \subseteq \nR \) is a field, namely a subfield of \( \nR \), and find the inverse of \( 1 + 2\sqrt 2 \).
:::

::: {.solution}
We check the three conditions of @prp-subfield-test (c). All computations are in the field \( \nR \), with \( (\sqrt 2)^2 = 2 \), and they expand brackets by (F5), (F6), (F9) and @fd3:prp-ring-algebra (c).

*One.* \( 1 = 1 + 0\sqrt 2 \in \nQ(\sqrt 2) \).

*Differences.* For \( a, b, c, d \in \nQ \), \( (a + b\sqrt 2) - (c + d\sqrt 2) = (a - c) + (b - d)\sqrt 2 \), and \( a - c, b - d \in \nQ \).

*Products, used below.* \( (a + b\sqrt 2)(c + d\sqrt 2) = (ac + 2bd) + (ad + bc)\sqrt 2 \), again in \( \nQ(\sqrt 2) \).

*Inverses.* Let \( y = c + d\sqrt 2 \ne 0 \), with \( c, d \in \nQ \). First, the **conjugate** \( c - d\sqrt 2 \) is not \( 0 \). If \( d \ne 0 \) and \( c - d\sqrt 2 = 0 \), then \( \sqrt 2 = c/d \in \nQ \), and \( (c/d)^2 = 2 \), against @fd3:thm-no-rational-square-two. If \( d = 0 \), then \( c - d\sqrt 2 = c = y \ne 0 \). Now
\[
N \coloneqq (c + d\sqrt 2)(c - d\sqrt 2) = c^2 - 2d^2 ,
\]
a rational number, and \( N \ne 0 \) by @thm-field-basic-properties (f) in \( \nR \), both factors being non-zero. Put \( y' \coloneqq c/N - (d/N)\sqrt 2 \in \nQ(\sqrt 2) \). Then \( y y' = (c + d\sqrt 2)(c - d\sqrt 2) N^{-1} = N N^{-1} = 1 \), so \( y' = y^{-1} \) by the uniqueness of inverses (@thm-field-basic-properties (c)). Finally, for \( x \in \nQ(\sqrt 2) \), \( xy^{-1} \in \nQ(\sqrt 2) \) by the product formula.

By @prp-subfield-test (c), \( \nQ(\sqrt 2) \) is a subfield of \( \nR \), and by (a) it is a field.

*The inverse of \( 1 + 2\sqrt 2 \).* Here \( c = 1 \), \( d = 2 \) and \( N = 1 - 8 = -7 \), so
\[
(1 + 2\sqrt 2)^{-1} = -\frac{1}{7} + \frac{2}{7}\sqrt 2 = \frac{-1 + 2\sqrt 2}{7} .
\]
Check: \( (1 + 2\sqrt 2)(-1 + 2\sqrt 2) = -1 + 2\sqrt 2 - 2\sqrt 2 + 8 = 7 \).
:::

The move "multiply by the conjugate" is the one that inverted complex numbers in @prp-complex-inverse. *Number Systems: From \(\nN\) to \(\nR\)*, Section 6.4, proved the same facts about \( \nQ(\sqrt 2) \) as part of an ordered field (@fd3:prp-cof-sqrt2-field-archimedean), and showed that it does not contain a square root of \( 3 \) (@fd3:prp-cof-sqrt2-field-incomplete).

::: {.check}
Is \( \{ a + b\sqrt 2 : a, b \in \nZ \} \) a subfield of \( \nR \)?
:::

::: {.solution}
No. It contains \( 2 = 2 + 0\sqrt 2 \), but not \( 2^{-1} = 1/2 \). If \( a + b\sqrt 2 = 1/2 \) with \( a, b \in \nZ \) and \( b \ne 0 \), then \( \sqrt 2 = (1/2 - a)/b \) would be rational, against @fd3:thm-no-rational-square-two; and if \( b = 0 \), then \( a = 1/2 \notin \nZ \). So it is not closed under inverses. It satisfies the other three clauses, exactly as \( \nZ \subseteq \nQ \) does.
:::

The same test works inside \( \nC \), where \( i^2 = -1 \) plays the part of \( (\sqrt 2)^2 = 2 \), and \( \nQ \subseteq \nR \subseteq \nC \) as above.

::: {#exm-subfields-gaussian}
[Rational and Integer Complex Numbers]

Let \( \nQ(i) \coloneqq \{ a + bi : a, b \in \nQ \} \) and \( \nZ[i] \coloneqq \{ a + bi : a, b \in \nZ \} \), subsets of \( \nC \).

::: {.enumerate options="label=(\roman*)"}
1. Show that \( \nQ(i) \) is a subfield of \( \nC \).
2. Show that \( \nZ[i] \) contains \( 0 \) and \( 1 \) and is closed under differences and products, but is not a subfield of \( \nC \).
3. Summarize the subfields of \( \nC \) met so far.
:::
:::

::: {.solution}
Real and imaginary parts are compared as in @def-complex-numbers: \( a + bi = c + di \) with \( a, b, c, d \in \nR \) holds exactly when \( a = c \) and \( b = d \).

(i) We use @prp-subfield-test (c). \( 1 = 1 + 0i \in \nQ(i) \). Differences: \( (a + bi) - (c + di) = (a - c) + (b - d)i \). Products: \( (a + bi)(c + di) = (ac - bd) + (ad + bc)i \), from \( i^2 = -1 \). Inverses: let \( y = c + di \ne 0 \) with \( c, d \in \nQ \); then \( (c, d) \ne (0, 0) \). The rational number \( M \coloneqq c^2 + d^2 \) is positive: \( \nQ \) is an ordered field (@fd3:thm-rationals-ordered-field), a non-zero square is positive (@fd3:prp-ordered-ring-rules (e)) and \( 0^2 = 0 \cdot 0 = 0 \) (@fd3:prp-ring-algebra (b)), so every square is non-negative, and a sum of a positive and a non-negative element is positive (@fd3:prp-ordered-ring-rules (b)). So \( M \ne 0 \). Since \( (c + di)(c - di) = c^2 + d^2 = M \), the element \( y' \coloneqq c/M - (d/M)i \in \nQ(i) \) satisfies \( yy' = MM^{-1} = 1 \), so \( y^{-1} = y' \in \nQ(i) \) (@thm-field-basic-properties (c)), and then \( xy^{-1} \in \nQ(i) \) for \( x \in \nQ(i) \) by the product formula. So \( \nQ(i) \) is a subfield of \( \nC \).

(ii) \( 0 = 0 + 0i \) and \( 1 = 1 + 0i \) lie in \( \nZ[i] \), and the difference and product formulas of (i), with integer \( a, b, c, d \), give integer parts. But \( 2 \in \nZ[i] \) has no inverse in \( \nZ[i] \). Suppose \( u = a + bi \in \nZ[i] \) had \( 2u = 1 \). Then \( u = 2^{-1} = 1/2 \) in \( \nC \), by the uniqueness of inverses (@thm-field-basic-properties (c)) and because the inverse of \( 2 \) in \( \nC \) is the real number \( 1/2 \) (@thm-complex-numbers-field), so \( a + bi = 1/2 + 0i \), and comparing real parts gives \( a = 1/2 \notin \nZ \). So \( \nZ[i] \) is not closed under inverses.

(iii) \( \nQ \), \( \nQ(i) \), \( \nR \) and \( \nC \) are subfields of \( \nC \), and \( \nQ(\sqrt 2) \) is a subfield of \( \nR \), hence of \( \nC \):
\[
\nQ \subseteq \nQ(\sqrt 2) \subseteq \nR \subseteq \nC , \qquad \nQ \subseteq \nQ(i) \subseteq \nC .
\]
For \( \nR \) in \( \nC \) there is a second way to see it: by @prp-reals-embed-complex the copy \( \iota(\nR) \) of \( \nR \) in \( \nC \) is closed under \( + \) and \( \cdot \), since \( \iota(a) + \iota(c) = \iota(a + c) \) and \( \iota(a)\iota(c) = \iota(ac) \). It is a field with these operations. Every element of \( \iota(\nR) \) is \( \iota(a) \) for some \( a \in \nR \), so each identity among the axioms carries over from \( \nR \) through these two equations; for instance \( \iota(a)(\iota(c) + \iota(e)) = \iota(a(c + e)) = \iota(ac + ae) = \iota(a)\iota(c) + \iota(a)\iota(e) \). In the same way \( \iota(0) \), \( \iota(-a) \), \( \iota(1) \) and, for \( a \ne 0 \), \( \iota(a^{-1}) \) serve as the zero, the negatives, the one and the inverses; and \( \iota(1) \ne \iota(0) \), and \( \iota(a) \ne \iota(0) \) exactly when \( a \ne 0 \), because \( \iota \) is injective. @prp-subfield-test (b) then says that it is a subfield, with the zero and one of \( \nC \).
:::

## The smallest subfield

Subfields can be intersected, and that gives, for any set \( S \) of elements, a smallest field containing them.

::: {#prp-subfield-intersection}
[Intersections of Subfields]

Let \( L \) be a field.

::: {.enumerate options="label=(\alph*)"}
1. If \( \sK \) is a **non-empty** set of subfields of \( L \), then \( \bigcap \sK \) is a subfield of \( L \).
2. For every subset \( S \subseteq L \) there is a **smallest** subfield of \( L \) containing \( S \): a subfield \( K_S \) with \( S \subseteq K_S \), contained in every subfield of \( L \) that contains \( S \). It is \( K_S = \bigcap \sK_S \), where \( \sK_S \) is the set of subfields of \( L \) that contain \( S \).
:::
:::

::: {.proof}
(a) The intersection \( \bigcap \sK = \{ x \in L : x \in K \text{ for every } K \in \sK \} \) is defined because \( \sK \) is a non-empty set of subsets of \( L \) (@fd2:def-family-union-intersection). We check @prp-subfield-test (c). Every \( K \in \sK \) contains \( 1 \), so \( 1 \in \bigcap \sK \). If \( a, b \in \bigcap \sK \), then \( a, b \in K \) for every \( K \in \sK \), so \( a - b \in K \) for every \( K \in \sK \), by (c) applied to \( K \); hence \( a - b \in \bigcap \sK \). In the same way, \( ab^{-1} \in \bigcap \sK \) when \( b \ne 0 \).

(b) \( \sK_S \) is a set, by Separation (Z6) from the power set of \( L \), which exists by (Z5) (@fd3:ax-zf-fragment). It is non-empty, since \( L \in \sK_S \). By (a), \( K_S \coloneqq \bigcap \sK_S \) is a subfield of \( L \). Every \( K \in \sK_S \) contains \( S \), so \( S \subseteq K_S \). And if \( K \) is a subfield containing \( S \), then \( K \in \sK_S \), so \( K_S \subseteq K \). Two smallest subfields containing \( S \) would each contain the other, so \( K_S \) is the only one.
:::

The case \( S = \emptyset \) asks for no element at all, and gives a subfield contained in every subfield. It has a name.

::: {#def-prime-subfield}
[Prime Subfield]

The **prime subfield** of a field \( L \) is the smallest subfield of \( L \), that is, \( K_{\emptyset} \) of @prp-subfield-intersection (b): the intersection of the set of **all** subfields of \( L \).
:::

In words: the prime subfield is what every subfield of \( L \) contains. Section 2.5 identifies it in every field, as a copy of \( \nQ \) or of exactly one \( \nF_p \). One case can be settled now: the prime subfield of \( \nF_p \) is \( \nF_p \) itself, because \( \nF_p \) has no other subfield. Indeed, let \( K \) be a subfield of \( \nF_p \). It contains \( 1 \) and is closed under \( + \), so it contains every multiple \( k \cdot 1 \) with \( k \in \nN \), the multiples of *Number Systems: From \(\nN\) to \(\nR\)*, Section 2.3 ("Multiples"): \( 0 \cdot 1 = 0 \in K \), and if \( k \cdot 1 \in K \), then \( (k + 1) \cdot 1 = k \cdot 1 + 1 \in K \), so induction (@fd1:ax-induction) covers every \( k \). In \( \nZ/p\nZ \), \( k \cdot [1] = [k] \) (@fd3:thm-integers-mod-n-ring (d)), and every element is \( [k] \) for some \( k \in \{0, \dots, p - 1\} \) (@fd3:thm-integers-mod-n-ring (b)). So \( K = \nF_p \).

The smallest subfield containing a given element is often easy to name. Exercise B2 shows that \( \nQ(\sqrt 2) \) is the smallest subfield of \( \nR \) containing \( \sqrt 2 \); the reason to expect it is that a subfield containing \( \sqrt 2 \) contains \( 1 \), hence every rational, and is closed under the sums and products that build \( a + b\sqrt 2 \).

## Exercises

### A. Check your understanding

::: {#exr-subfields-a1}
[A1]

These parts are about @prp-subfield-test (b).

::: {.enumerate options="label=(\alph*)"}
1. Why must the one of a field \( K \subseteq L \), closed under the operations of the field \( L \), be \( 1_L \)? Name the step of the proof.
2. Run the proof of (b) on \( K = \{[0], [3]\} \) inside the ring \( \nZ/6\nZ \) (the warning). Which steps go through, and which step fails?
3. In @exm-q-sqrt2-field, is the commutativity (F6) of \( \nQ(\sqrt 2) \) checked, or inherited? From where?
4. State the idea of the subfield test, parts (a) and (b), in two sentences.
:::
:::

::: {.solution}
(a) In \( L \), \( 1_K \cdot 1_K = 1_K = 1_K \cdot 1_L \), and \( 1_K \ne 0_K = 0_L \); multiplicative cancellation in \( L \) (@thm-field-basic-properties (b)) removes the factor \( 1_K \) and gives \( 1_K = 1_L \).

(b) The zero step goes through: \( [0] \) is the zero of both, and \( [0] + [0] = [0] + [0] \) cancels in any commutative ring. The negative step also goes through (\( [3] + [3] = [0] \), so \( -[3] = [3] \) in both). The one step fails: \( [3][3] = [3] = [3][1] \), but \( [3] \) has no inverse in \( \nZ/6\nZ \) (\( [3][x] \in \{[0], [3]\} \) for every \( x \)), so it cannot be canceled, and indeed \( [3] \ne [1] \). The inverse step then has nothing to say.

(c) Inherited. (F6) holds for all elements of \( \nR \) (@fd3:thm-reals-field), hence for all elements of the subset \( \nQ(\sqrt 2) \); @prp-subfield-test (a) records this. The solution of the example checks only the three conditions of (c).

(d) The identities among the field axioms hold for all elements of the big field, hence for the elements of any subset, so only closure and the special elements \( 0, 1, -a, a^{-1} \) need checking. Conversely, the zero and one of a field sitting inside \( L \) with \( L \)'s operations are forced, by cancellation in \( L \), to be those of \( L \).
:::

### B. Practice

::: {#exr-subfields-b1}
[B1: Putting a proof in order]

Here are the lines of the proof of @prp-subfield-test (c) \( (\Leftarrow) \), shuffled, together with two lines that do not belong. Put the correct lines in an admissible order, say which other orders are admissible, and say what is wrong with each of the other two lines.

::: {.enumerate options="label=(\roman*)"}
1. Assume \( 1 \in K \), \( a - b \in K \) for all \( a, b \in K \), and \( ab^{-1} \in K \) for all \( a, b \in K \) with \( b \ne 0 \).
2. \( 0 = 1 - 1 \in K \).
3. For \( b \in K \), \( -b = 0 - b \in K \).
4. For non-zero \( b \in K \), \( b^{-1} = 1 \cdot b^{-1} \in K \).
5. For \( a, b \in K \), \( a + b = a - (-b) \in K \).
6. For \( a, b \in K \): if \( b \ne 0 \), then \( b^{-1} \in K \) and \( b^{-1} \ne 0 \) (as \( bb^{-1} = 1 \ne 0 = b \cdot 0 \)), so \( ab = a(b^{-1})^{-1} \in K \); if \( b = 0 \), \( ab = 0 \in K \).
7. So \( K \) is a subfield of \( L \).
:::

The two extra lines: "(ii′) \( 0 \in K \), since \( 0 = bb^{-1} \) for any \( b \in K \)", and "(vi′) \( ab \in K \), because \( K \) is closed under multiplication".
:::

::: {.solution}
An admissible order is (i), (ii), (iii), (iv), (v), (vi), (vii). The constraints are what each line uses: (i) comes first and (vii) last; (ii) comes before (iii), which uses \( 0 \in K \), and before (vi), whose case \( b = 0 \) uses \( 0 \in K \); (iii) comes before (v), which uses \( -b \in K \); (iv) comes before (vi), which uses \( b^{-1} \in K \) (line (vi) itself checks \( b^{-1} \ne 0 \) before applying (i) to it). Any order respecting these is admissible; for instance (i), (ii), (iv), (iii), (vi), (v), (vii).

(ii′) is false: \( bb^{-1} = 1 \), not \( 0 \), and \( b^{-1} \) exists only for \( b \ne 0 \).

(vi′) is circular: closure under products is part of what the proof must establish, so the line cites the goal. This is entry (N9) of @fd1:exm-not-allowed-catalogue.
:::

::: {#exr-subfields-b2}
[B2]

Show that \( \nQ(\sqrt 2) \) is the smallest subfield of \( \nR \) containing \( \sqrt 2 \), in the sense of @prp-subfield-intersection (b).
:::

::: {.solution}
Let \( K \) be a subfield of \( \nR \) with \( \sqrt 2 \in K \). Since \( 1 \in K \) and \( K \) is closed under \( + \), \( n \cdot 1 \in K \) for every \( n \in \nN \), by induction (@fd1:ax-induction) as for \( \nF_p \) above; and in \( \nR \), \( n \cdot 1 = n \) (@fd3:thm-rational-embedding (d), under the identification). Then \( -n \in K \) by closure under negatives, so every integer lies in \( K \) (every integer is \( n \) or \( -n \) with \( n \in \nN \), @fd3:prp-naturals-embed-integers (c)). For \( m \in \nZ \) and \( n \in \nZ_{>0} \), \( n \ne 0 \), so \( m/n = mn^{-1} \in K \) by closure under inverses and products; and every rational is of this form (@fd3:prp-integers-embed-rationals (b)). So \( \nQ \subseteq K \), and then \( a + b\sqrt 2 \in K \) for all \( a, b \in \nQ \), by closure under sums and products. Hence \( \nQ(\sqrt 2) \subseteq K \).

Conversely, \( \nQ(\sqrt 2) \) is a subfield of \( \nR \) (@exm-q-sqrt2-field) containing \( \sqrt 2 = 0 + 1\sqrt 2 \). So it is the smallest such subfield.
:::

::: {#exr-subfields-b3}
[B3]

Inside \( \nC \) (with \( \nR \subseteq \nC \)), show that \( \nQ(\sqrt 2) \cap \nQ(i) = \nQ \).
:::

::: {.solution}
\( (\supseteq) \) A rational \( a \) is \( a + 0\sqrt 2 \) and \( a + 0i \).

\( (\subseteq) \) Let \( x = a + b\sqrt 2 = c + di \) with \( a, b, c, d \in \nQ \). The number \( a + b\sqrt 2 \) is real, so its imaginary part is \( 0 \); the imaginary part of \( c + di \) is \( d \). Comparing parts (@def-complex-numbers), \( d = 0 \) and \( a + b\sqrt 2 = c \). If \( b \ne 0 \), then \( \sqrt 2 = (c - a)/b \in \nQ \), against @fd3:thm-no-rational-square-two. So \( b = 0 \), and \( x = a \in \nQ \).

By @prp-subfield-intersection (a), this also shows again that \( \nQ \) is a subfield of \( \nC \).
:::

::: {#exr-subfields-b4}
[B4]

Let \( \sqrt 3 \) be the non-negative real number with square \( 3 \) (@fd3:prp-cof-square-roots), and \( \nQ(\sqrt 3) \coloneqq \{ a + b\sqrt 3 : a, b \in \nQ \} \subseteq \nR \). Show that \( \nQ(\sqrt 3) \) is a subfield of \( \nR \), and that \( \sqrt 2 + \sqrt 3 \notin \nQ(\sqrt 2) \cup \nQ(\sqrt 3) \). Hence deduce that the union of two subfields need not be a subfield.

*Hint: the claim stated with @fd3:prp-cof-sqrt2-field-incomplete says which integers are not squares of rationals.*
:::

::: {.solution}
The claim stated with @fd3:prp-cof-sqrt2-field-incomplete says: if \( n, k \in \nN \) and \( k^2 < n < (k + 1)^2 \), no rational squares to \( n \). We use it for \( (n, k) = (3, 1) \) and \( (6, 2) \), since \( 1 < 3 < 4 \) and \( 4 < 6 < 9 \).

*\( \nQ(\sqrt 3) \) is a subfield.* Exactly as in @exm-q-sqrt2-field, with \( 3 \) in place of \( 2 \): the product is \( (a + b\sqrt 3)(c + d\sqrt 3) = (ac + 3bd) + (ad + bc)\sqrt 3 \); for \( y = c + d\sqrt 3 \ne 0 \), the conjugate \( c - d\sqrt 3 \) is non-zero (if \( d \ne 0 \), it would make \( \sqrt 3 = c/d \) rational, against the claim with \( (3, 1) \)), \( N \coloneqq c^2 - 3d^2 \ne 0 \), and \( y^{-1} = c/N - (d/N)\sqrt 3 \).

*Not in \( \nQ(\sqrt 2) \).* If \( \sqrt 2 + \sqrt 3 \in \nQ(\sqrt 2) \), then \( \sqrt 3 = (\sqrt 2 + \sqrt 3) - \sqrt 2 \in \nQ(\sqrt 2) \), a square root of \( 3 \) in \( \nQ(\sqrt 2) \), against @fd3:prp-cof-sqrt2-field-incomplete.

*Not in \( \nQ(\sqrt 3) \).* If it were, then \( \sqrt 2 = (\sqrt 2 + \sqrt 3) - \sqrt 3 \in \nQ(\sqrt 3) \), say \( \sqrt 2 = a + b\sqrt 3 \) with \( a, b \in \nQ \). Squaring,
\[
2 = (a^2 + 3b^2) + 2ab\sqrt 3 , \quad\text{that is,}\quad (a^2 + 3b^2 - 2) + 2ab\sqrt 3 = 0 .
\]
If \( ab \ne 0 \), then \( \sqrt 3 = (2 - a^2 - 3b^2)/(2ab) \in \nQ \), against the claim with \( (3, 1) \). So \( ab = 0 \), and then \( a^2 + 3b^2 = 2 \). If \( b = 0 \), then \( a^2 = 2 \), against @fd3:thm-no-rational-square-two. If \( a = 0 \), then \( 3b^2 = 2 \), so \( (3b)^2 = 6 \), against the claim with \( (6, 2) \).

*The union.* \( \sqrt 2 \in \nQ(\sqrt 2) \) and \( \sqrt 3 \in \nQ(\sqrt 3) \), but their sum is in neither. So \( \nQ(\sqrt 2) \cup \nQ(\sqrt 3) \) is not closed under sums, and is not a subfield of \( \nR \), although both pieces are.
:::

### C. Going deeper

::: {#exr-subfields-c1}
[C1: A finite subset closed under the operations]

Let \( L \) be a field and \( K \subseteq L \) a **finite** subset with \( 1 \in K \), closed under \( + \) and \( \cdot \). Show that \( 0 \in K \), that \( K \) is closed under negatives and under inverses of non-zero elements, and hence that \( K \) is a subfield of \( L \). Then show that the hypothesis "finite" cannot be dropped.
:::

::: {.solution}
[Hint 1]

For \( b \in K \), which maps \( K \to K \) can you build from \( b \) and the two operations?
:::

::: {.solution}
[Hint 2]

The maps \( x \mapsto x + b \) and \( x \mapsto bx \) go from \( K \) to \( K \). Why are they injective, and what does finiteness then give?
:::

::: {.solution}
*A finite set has no injection onto a proper part.* Let \( f \colon K \to K \) be injective. If \( f \) were not surjective, its image \( f(K) \) (@fd2:def-image) would be a proper subset of \( K \), and \( f \), with codomain \( f(K) \), would be a bijection \( K \to f(K) \), against @fd2:thm-finite-no-proper-copy. So every injective map \( K \to K \) is surjective.

*Zero.* Let \( t \colon K \to K \), \( t(x) \coloneqq x + 1 \), a map into \( K \) because \( K \) is closed under \( + \) and \( 1 \in K \). It is injective: \( x + 1 = x' + 1 \) gives \( 1 + x = 1 + x' \) by (F1), so \( x = x' \) by additive cancellation in \( L \) (@thm-field-basic-properties (b)). So it is surjective, and some \( x \in K \) has \( x + 1 = 1 = 0 + 1 \), so \( 1 + x = 1 + 0 \) by (F1); canceling, \( x = 0 \). So \( 0 \in K \).

*Negatives.* Let \( b \in K \). The map \( x \mapsto x + b \) is injective in the same way, hence surjective, and \( 0 \in K \) is a value: \( x + b = 0 \) for some \( x \in K \). By the uniqueness of negatives in \( L \), \( x = -b \).

*Inverses.* Let \( b \in K \), \( b \ne 0 \). The map \( x \mapsto bx \) goes from \( K \) to \( K \) and is injective by multiplicative cancellation in \( L \), which uses \( b \ne 0 \). So it is surjective, \( bx = 1 \) for some \( x \in K \), and \( x = b^{-1} \) by the uniqueness of inverses in \( L \).

So \( K \) is a subfield. Note that \( K \ne \emptyset \) need not be assumed: \( 1 \in K \).

*Finiteness is needed.* \( \nN \subseteq \nQ \) contains \( 1 \) and is closed under \( + \) and \( \cdot \), and \( -1 \notin \nN \). The argument breaks at "injective, hence surjective": \( x \mapsto x + 1 \) is injective on \( \nN \), and \( 0 \) is not a value.

**Marking scheme.** (10 points)
- 2: a finiteness argument with its reason: an injective map from a finite set to itself is surjective (@fd2:thm-finite-no-proper-copy, or a count), or pigeonhole on a sequence in \( K \) (@fd2:thm-pigeonhole).
- 2: \( 0 \in K \), from a translation map and cancellation, or from a repetition \( m \cdot 1 = n \cdot 1 \) with \( m < n \) and cancellation in \( L \), **before** \( 0 \) is used.
- 2: negatives, from surjectivity of \( x \mapsto x + b \) and uniqueness of negatives in \( L \), or from a repetition \( i \cdot b = j \cdot b \) with \( i < j \), giving \( -b = (j - i - 1) \cdot b \).
- 2: inverses, with the cancellation by \( b \) justified by \( b \ne 0 \) (injectivity of \( x \mapsto bx \), or \( b^i = b^j \) with \( i < j \) giving \( b^{j - i} = 1 \) and \( b^{-1} = b^{j - i - 1} \)).
- 2: a witness that finiteness is needed (\( \nN \subseteq \nQ \), or \( \nZ \subseteq \nQ \) for inverses).
Fatal errors (0 for the step): using \( 0 \in K \) or \( -b \in K \) to build the translation before proving it; "injective, hence surjective" (or pigeonhole) without finiteness.
:::

::: {#exr-subfields-c2}
[C2: Find the error]

Here is an argument. Is its conclusion true? Does the argument prove it? If not, name the line that fails and why.

"\( \nQ(\sqrt 2) \) is closed under inverses. (1) Let \( a + b\sqrt 2 \in \nQ(\sqrt 2) \) be non-zero. (2) Then
\[
(a + b\sqrt 2)^{-1} = \frac{1}{a} + \frac{1}{b\sqrt 2} = \frac{1}{a} + \frac{1}{2b}\sqrt 2 .
\]
(3) Both coefficients are rational, so the inverse lies in \( \nQ(\sqrt 2) \)."
:::

::: {.solution}
The conclusion is **true** (@exm-q-sqrt2-field). The argument does not prove it.

*Line (2) fails.* Its first equality uses the general "fact" \( 1/(x + y) = 1/x + 1/y \), which is neither proved nor true; so the line cites nothing, entry (N9) of @fd1:exm-not-allowed-catalogue. It also divides by \( a \) and by \( b \), either of which may be \( 0 \) (for \( \sqrt 2 = 0 + 1\sqrt 2 \), \( a = 0 \)). The second equality, \( 1/(b\sqrt 2) = (1/(2b))\sqrt 2 \), is correct for \( b \ne 0 \).

*Counterexample to the step.* \( x = y = 1 \) in \( \nQ \): \( 1/(1 + 1) = 1/2 \), while \( 1/1 + 1/1 = 2 \). In the case at hand, \( a = b = 1 \): the formula gives \( 1 + \tfrac12\sqrt 2 \), and \( (1 + \sqrt 2)(1 + \tfrac12\sqrt 2) = 2 + \tfrac32\sqrt 2 \ne 1 \); the true inverse is \( -1 + \sqrt 2 \).

*Repair.* Multiply by the conjugate, as in @exm-q-sqrt2-field: \( (a + b\sqrt 2)^{-1} = (a - b\sqrt 2)/(a^2 - 2b^2) \).
:::

<!-- dependency ledger
def-subfield (example): Q is a subfield of R under the identification q = kappa(q) | fd3:thm-rational-embedding (a), (c), cited (soft citation of F3.10, examples only)
def-subfield (example): a subfield of a subfield is a subfield | inline (each clause is about the outer field's operations)
def-subfield (example): 2x = 1 has no integer solution | fd3:cor-integers-even-odd (a), cited
prp-subfield-test (proof): 1 + (-1) = 0, 0 + (-b) = -b, 1 * b^{-1} = b^{-1} | (F1), (F3), (F4), (F6), (F7) of def-field, named inline
exm-q-sqrt2-field (solution): sqrt 2 exists in R; R complete | fd3:thm-reals-complete-ordered-field, fd3:prp-cof-square-roots, cited (soft citation of F3.4/F3.10, example only)
exm-q-sqrt2-field (solution): product formula, (c + d sqrt 2)(c - d sqrt 2) = c^2 - 2d^2, N = -7, inverse (-1 + 2 sqrt 2)/7 | inline expansion with fd3:prp-ring-algebra (c); verify/ch02/exm-q-sqrt2-field.py
exm-q-sqrt2-field (solution): rational arithmetic computed in Q agrees with that in R | fd3:thm-rational-embedding (a), (c) (identification), as recalled in the def-subfield examples
exm-subfields-gaussian (solution): every square in Q is non-negative | fd3:prp-ordered-ring-rules (e), fd3:prp-ring-algebra (b), cited
exm-subfields-gaussian (solution): the inverse of 2 in C is the real 1/2; zero and one of C are the real 0, 1 | thm-complex-numbers-field, prp-complex-arithmetic-laws (d), prp-reals-embed-complex (identification), cited
exm-subfields-gaussian (solution): product formula in C from i^2 = -1; (c + di)(c - di) = c^2 + d^2 | def-complex-numbers, prp-reals-embed-complex (F4.1, see edge; example only); verify/ch02/exm-subfields-gaussian.py
exm-subfields-gaussian (solution): the copy of R in C is a field because it is the image of R under an injective map preserving + and . | prp-reals-embed-complex; inline transport of the axioms, written out
prp-subfield-intersection (proof): the set of subfields containing S exists | fd3:ax-zf-fragment (Z5), (Z6), cited
def-prime-subfield (claim): every subfield of F_p contains k.1 for k in N | fd1:ax-induction read on omega (fd3:cor-omega-identification); multiples of F3.2 Section 2.3 "Multiples", recalled in prose
exr-subfields-b2 (solution): n.1 = n in R for n in N | fd3:thm-rational-embedding (d) with the identification of N inside Q inside R
exr-subfields-b4 (solution): 1 < 3 < 4, 4 < 6 < 9; (a + b sqrt 3)^2 = a^2 + 3b^2 + 2ab sqrt 3 | inline; verify/ch02/exr-subfields-b4.py
exr-subfields-b4 (solution): no rational squares to 3 or 6 | the claim stated with fd3:prp-cof-sqrt2-field-incomplete, cited (soft citation of F3.4, exercise solution)
exr-subfields-c1 (solution): an injective map K -> K of a finite set is surjective | inline from fd2:thm-finite-no-proper-copy and fd2:def-image
exr-subfields-c2 (solution): (1 + sqrt 2)(1 + sqrt 2 / 2) = 2 + 3 sqrt 2 / 2; inverse of 1 + sqrt 2 is -1 + sqrt 2 | verify/ch02/exr-subfields-c2.py
exr-subfields-a1 (solution): [3][x] lies in {[0], [3]} for every x in Z/6Z | inline (six products); verify/ch02/exr-subfields-a1.py
-->
