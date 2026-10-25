# Conjugate, Modulus, and Division

Section 1.1 built \( \nC \) and showed that it is a commutative ring with \( 1 \ne 0 \) (@prp-complex-arithmetic-laws). One field axiom is still missing: (F8), which asks for an inverse of every non-zero element. To divide by \( 3 + 4i \), we want a number to multiply by that lands in the real numbers, where division is familiar. The product \( (a + bi)(a - bi) = a^2 + b^2 \) of @exm-complex-arithmetic shows which number does the job. This section gives its two ingredients names, the conjugate and the modulus, proves the rules they obey, and concludes that \( \nC \) is a field.

## Conjugate and modulus

A complex number \( z = a + bi \) is a point \( (a, b) \) of the plane. Two pieces of plane geometry turn out to be algebra in disguise: the mirror image of \( z \) in the horizontal axis, and the distance of \( z \) from \( 0 \). The mirror image changes the sign of \( b \). The distance, by Pythagoras, is the square root of \( a^2 + b^2 \), the very number that appeared in @exm-complex-arithmetic. Square roots of non-negative real numbers exist and are unique in every complete ordered field (@fd3:prp-cof-square-roots), so we may use them in \( \nR \): for \( x \in \nR \) with \( x \ge 0 \), \( \sqrt{x} \) is the **unique** \( y \in \nR \) with \( y \ge 0 \) and \( y^2 = x \).

*Conjugating reflects a point in the real axis; the modulus is its distance from the origin.*

::: {#def-conjugate-modulus}
[Conjugate and Modulus]

Let \( z = a + bi \in \nC \) with \( a, b \in \nR \). The **complex conjugate** of \( z \) is
\[
\conj{z} \coloneqq a - bi .
\]
The **modulus** (or absolute value) of \( z \) is the real number
\[
\abs{z} \coloneqq \sqrt{a^2 + b^2} ,
\]
the **non-negative** square root of @fd3:prp-cof-square-roots in \( \nR \).
:::

In words: the conjugate keeps the real part and flips the sign of the imaginary part, \( \operatorname{Re} \conj{z} = \operatorname{Re} z \) and \( \operatorname{Im} \conj{z} = -\operatorname{Im} z \). The modulus is a **real** number, never negative, and its square is \( a^2 + b^2 = (\operatorname{Re} z)^2 + (\operatorname{Im} z)^2 \).

**Well-definedness.** Since \( z \) determines \( a \) and \( b \) (compare real and imaginary parts, Section 1.1), the right-hand sides depend only on \( z \). The square root exists because its argument is non-negative: \( a^2 \ge 0 \) and \( b^2 \ge 0 \) (@fd3:prp-ordered-ring-rules (e), with \( 0^2 = 0 \) when the number is \( 0 \)), so \( a^2 + b^2 \ge 0 \) (@fd3:prp-ordered-ring-rules (b)). And \( \nR \) is complete (@fd3:thm-reals-complete-ordered-field), which is the hypothesis of @fd3:prp-cof-square-roots. This is where the completeness of \( \nR \) enters the chapter. Over \( \nQ \) alone the definition would break down at once: \( \abs{1 + i} \) would have to be a rational number whose square is \( 2 \), and there is none (@fd3:thm-no-rational-square-two).

**Examples.**

*A point with integer distance.* For \( z = 3 + 4i \): \( \conj{z} = 3 - 4i \), and \( \abs{z} = \sqrt{9 + 16} = \sqrt{25} = 5 \). The last step is the uniqueness clause of @fd3:prp-cof-square-roots: \( 5 \ge 0 \) and \( 5^2 = 25 \), so \( 5 \) is **the** non-negative square root of \( 25 \).

*The unit \( i \).* \( \conj{i} = \conj{0 + 1i} = 0 - 1i = -i \), and \( \abs{i} = \sqrt{0 + 1} = 1 \), since \( 1 \ge 0 \) and \( 1^2 = 1 \).

*The degenerate case \( z = 0 \).* \( \conj{0} = 0 \) and \( \abs{0} = \sqrt{0} = 0 \). We show below that \( 0 \) is the **only** complex number with modulus \( 0 \); that one fact is what makes division possible.

*A real number.* For \( a \in \nR \), \( \conj{a} = a \) and \( \abs{a} = \sqrt{a^2} \). The symbol \( \abs{a} \) already had a meaning for real \( a \): the absolute value of an ordered field (@fd3:def-absolute-value-ordered-field). The next proposition shows the two meanings agree, so the notation does not clash.

::: {#prp-modulus-of-real}
[The Modulus Extends the Absolute Value]

Let \( a \in \nR \subseteq \nC \). Then \( \conj{a} = a \), and the modulus \( \sqrt{a^2 + 0^2} \) of \( a \) equals the absolute value of \( a \) in the ordered field \( \nR \) (@fd3:def-absolute-value-ordered-field).
:::

::: {.proof}
Write \( a = a + 0i \). Then \( \conj{a} = a - 0i = a \), since \( 0 \cdot i = i \cdot 0 = 0 \) by (F6) and @fd3:prp-ring-algebra (b), and \( -0 = 0 \) because \( 0 + 0 = 0 \) and negatives are unique (@fd3:prp-ring-algebra (a)), all in the commutative ring \( \nC \). The modulus of \( a \) is \( \sqrt{a^2 + 0^2} = \sqrt{a^2} \), the unique non-negative real number whose square is \( a^2 \). The absolute value \( \abs{a} \) of the ordered field \( \nR \) is non-negative and satisfies \( \abs{a}^2 = a^2 \) (@fd3:prp-absolute-value-ordered-field (a), (b)). By the uniqueness clause of @fd3:prp-cof-square-roots, the two are equal.
:::

So the modulus **extends** the absolute value: on \( \nR \subseteq \nC \) it is the old \( \abs{\cdot} \), and every result about \( \abs{x} \) for real \( x \) stays true with the new reading. For instance \( \abs{-3} = 3 \), whichever definition we use.

::: {.check}
Find \( \conj{z} \) and \( \abs{z} \) for \( z = -2i \) and for \( z = 1 - i \). For which of the two is \( \conj{z} = z \)?
:::

::: {.solution}
For \( z = -2i = 0 + (-2)i \): \( \conj{z} = 0 - (-2)i = 2i \) and \( \abs{z} = \sqrt{0 + 4} = 2 \), since \( 2 \ge 0 \) and \( 2^2 = 4 \). For \( z = 1 - i \): \( \conj{z} = 1 + i \) and \( \abs{z} = \sqrt{1 + 1} = \sqrt{2} \). In neither case is \( \conj{z} = z \): comparing imaginary parts, \( \conj{z} = z \) needs \( \operatorname{Im} z = -\operatorname{Im} z \), that is \( \operatorname{Im} z = 0 \), and both numbers have non-zero imaginary part.
:::

**Why this definition.** The square root is what makes the modulus a length. Without it, the simpler quantity \( N(z) \coloneqq a^2 + b^2 \) would do some of the same jobs: it is \( z \conj{z} \), and it vanishes only at \( 0 \). But on real numbers it is \( N(a) = a^2 \), not \( \abs{a} \), so it does not extend the absolute value: \( N(2) = 4 \). And it is not a sensible distance: \( N(1 + 1) = 4 \), while \( N(1) + N(1) = 2 \), so the "side" from \( 0 \) to \( 2 \) would be longer than the two sides through \( 1 \). The modulus keeps the convenient algebra of \( N \), since \( \abs{z}^2 = N(z) \), and adds the right size. Section 1.3 exploits exactly this square.

::: {.warning}
The modulus squared is \( z \conj{z} \), **not** \( z z \). In general \( \abs{z}^2 \ne z^2 \): for \( z = i \), \( \abs{i}^2 = 1 \) but \( i^2 = -1 \). The two agree only when \( z \) is real. For \( z = a + bi \), \( z^2 = (a^2 - b^2) + 2abi \) and \( \abs{z}^2 = a^2 + b^2 \); if they are equal, comparing real parts gives \( a^2 - b^2 = a^2 + b^2 \), so \( 2b^2 = 0 \). Since \( 2 > 0 \) in \( \nR \) (@fd3:prp-ordered-ring-rules (h)), \( 2 \ne 0 \), so \( b^2 = 0 \) by part (f), and \( b = 0 \) by part (e). Conversely, for real \( z = a \), \( \abs{a}^2 = a^2 + 0^2 = a^2 \).
:::

## Rules for conjugate and modulus

The following rules are used constantly, in this chapter and much later for complex inner products. They say that conjugation respects both operations, and that the modulus respects products.

::: {#thm-conjugate-properties}
[Properties of Conjugation and Modulus]

For all \( z, w \in \nC \):

::: {.enumerate options="label=(\alph*)"}
1. \( \conj{z + w} = \conj{z} + \conj{w} \) and \( \conj{\conj{z}} = z \);
2. \( \conj{zw} = \conj{z} \, \conj{w} \);
3. \( z \conj{z} = \abs{z}^2 \) and \( z + \conj{z} = 2 \operatorname{Re} z \);
4. \( \abs{zw} = \abs{z} \, \abs{w} \) and \( \abs{\conj{z}} = \abs{z} \);
5. \( \abs{z} = 0 \) if and only if \( z = 0 \).
:::
:::

::: {.idea}
Parts (a)–(c) and (e) are direct computations with real and imaginary parts. For (d), expanding \( \abs{zw} \) directly is legitimate but messy, since a square root of a long sum appears. It is cleaner to square: by (c) a squared modulus is a product with a conjugate, and (b) lets the conjugate split across the product. Two non-negative real numbers with the same square are equal, and that brings us back from squares to moduli.
:::

::: {.proof}
Let \( z = a + bi \) and \( w = c + di \) with \( a, b, c, d \in \nR \).

(a) We have \( \conj{z + w} = (a + c) - (b + d)i = (a - bi) + (c - di) = \conj{z} + \conj{w} \), since \( -(b + d) = (-b) + (-d) \): \( (b + d) + \bigl((-b) + (-d)\bigr) = 0 \), and negatives are unique (@fd3:prp-ring-algebra (a) in \( \nR \)). And \( \conj{z} = a + (-b)i \), so \( \conj{\conj{z}} = a - (-b)i = a + bi = z \), by @fd3:prp-ring-algebra (a) in \( \nR \).

(b) Since \( zw = (ac - bd) + (ad + bc)i \), we get \( \conj{zw} = (ac - bd) - (ad + bc)i \). On the other hand, by @def-complex-numbers and @fd3:prp-ring-algebra (c) in \( \nR \),
\[
\begin{aligned}
\conj{z} \, \conj{w}
&= \bigl(a + (-b)i\bigr)\bigl(c + (-d)i\bigr) \\
&= \bigl(ac - (-b)(-d)\bigr) + \bigl(a(-d) + (-b)c\bigr)i \\
&= (ac - bd) - (ad + bc)i .
\end{aligned}
\]

(c) By @exm-complex-arithmetic, \( z \conj{z} = a^2 + b^2 \), and \( a^2 + b^2 = \abs{z}^2 \) because \( \abs{z} \) is a square root of \( a^2 + b^2 \). Also \( z + \conj{z} = (a + a) + (b - b)i = 2a = 2 \operatorname{Re} z \).

(d) By (c), then (b), then @prp-complex-arithmetic-laws to regroup and reorder the four factors,
\[
\abs{zw}^2 = (zw)\,\conj{zw} = z w \conj{z} \, \conj{w} = (z \conj{z})(w \conj{w}) = \abs{z}^2 \abs{w}^2 .
\]
In \( \nR \), \( \abs{z}^2 \abs{w}^2 = \bigl(\abs{z} \abs{w}\bigr)^2 \) (@prp-power-laws-commutative-ring (c)), and \( \abs{z} \abs{w} \ge 0 \): it is \( 0 \) if one factor is \( 0 \) (@fd3:prp-ring-algebra (b)), and positive otherwise, since a product of two positive elements of an ordered field is positive ((O4) of @fd3:def-ordered-ring-and-field). So \( \abs{zw} \) and \( \abs{z}\abs{w} \) are both non-negative real numbers whose square is \( \abs{z}^2 \abs{w}^2 \). By the uniqueness clause of @fd3:prp-cof-square-roots they are equal. Finally \( \abs{\conj{z}} = \sqrt{a^2 + (-b)^2} = \sqrt{a^2 + b^2} = \abs{z} \), since \( (-b)^2 = b^2 \) (@fd3:prp-ring-algebra (c)).

(e) If \( z = 0 \), then \( \abs{z} = \sqrt{0} = 0 \). Conversely, let \( \abs{z} = 0 \), so \( a^2 + b^2 = \abs{z}^2 = 0 \). If \( a \ne 0 \), then \( a^2 > 0 \) (@fd3:prp-ordered-ring-rules (e)) and \( b^2 \ge 0 \), so \( a^2 + b^2 > 0 \) (@fd3:prp-ordered-ring-rules (b)), a contradiction; hence \( a = 0 \). Then \( b^2 = 0 \), and the same rule gives \( b = 0 \). So \( z = 0 \). This proves the theorem.
:::

The proof of (d) is our first use of a move that runs through the whole chapter: a statement about a modulus \( \abs{u} \) becomes a statement about \( \abs{u}^2 = u \conj{u} \), which is algebra; we compute there, and come back by taking non-negative square roots. Section 1.3 names it, *square the modulus*, and uses it to prove the triangle inequality.

Two remarks on what the theorem says. First, (a) and (b) say that conjugation respects sums and products, and it fixes \( 1 \). Not every reflection does: the reflection in the vertical axis, \( z \mapsto -\conj{z} \), respects sums, but it sends \( 1 \) to \( -1 \), and \( 1 \cdot 1 = 1 \) to \( -1 \), while the product of the images is \( (-1)(-1) = 1 \). Second, (d) says that the size of a product is the product of the sizes. In the plane picture, multiplying by \( w \) stretches every length by \( \abs{w} \); Section 1.5 completes this picture with angles.

## Division

The first payoff is division. If \( z \ne 0 \), then \( \abs{z} \ne 0 \) by (e), so \( \abs{z}^2 \) is a **strictly** positive real number, and we may divide by it in \( \nR \).

::: {#prp-complex-inverse}
[Inverse of a Complex Number]

Let \( z \in \nC \) with \( z \ne 0 \). Then
\[
w \coloneqq \frac{1}{\abs{z}^2} \, \conj{z}
\]
satisfies \( zw = 1 \). We write \( z^{-1} \) or \( \dfrac{1}{z} \) for this \( w \).
:::

::: {.proof}
Since \( z \ne 0 \), \( \abs{z} \ne 0 \) by @thm-conjugate-properties (e), so \( \abs{z}^2 > 0 \) by @fd3:prp-ordered-ring-rules (e). In particular \( \abs{z}^2 \ne 0 \), so it has an inverse \( 1/\abs{z}^2 \) in the field \( \nR \). By @prp-complex-arithmetic-laws and @thm-conjugate-properties (c),
\[
zw = \frac{1}{\abs{z}^2} \, (z \conj{z}) = \frac{1}{\abs{z}^2} \, \abs{z}^2 = 1 ,
\]
where the last product is computed in \( \nR \), which gives the same result as in \( \nC \) (@prp-reals-embed-complex). This proves the proposition.
:::

The hypothesis \( z \ne 0 \) is used exactly once, to make \( \abs{z}^2 \) non-zero, so that \( 1/\abs{z}^2 \) exists. For \( z = 0 \) there is nothing to rescue: \( 0 \cdot w = 0 \ne 1 \) for every \( w \) (@fd3:prp-ring-algebra (b)). The proposition gives one inverse; that it is the only one is a fact about all fields, which we can cite as soon as we know that \( \nC \) is one.

::: {#thm-complex-numbers-field}
[The Complex Numbers Form a Field]

The set \( \nC \), with the operations of @def-complex-numbers, is a field in the sense of @fd3:def-commutative-ring-and-field. Moreover \( \nR \subseteq \nC \) (@prp-reals-embed-complex) is closed under the field operations of \( \nC \): for \( a, c \in \nR \), the sum \( a + c \), the product \( ac \), the negative \( -a \) and, if \( a \ne 0 \), the inverse \( a^{-1} \), computed in \( \nC \), are the real numbers computed in \( \nR \).
:::

::: {.proof}
By @prp-complex-arithmetic-laws and the remark after it, \( \nC \) satisfies (F1)–(F7) and (F9), and \( 1 \ne 0 \) in \( \nC \). By @prp-complex-inverse, every non-zero \( z \in \nC \) has an element \( z^{-1} \) with \( z z^{-1} = 1 \), which is (F8). So \( \nC \) is a field.

For \( a, c \in \nR \), the sum and product are those of \( \nR \) by @prp-reals-embed-complex. The real negative \( -a \) satisfies \( a + (-a) = 0 \) in \( \nR \), hence in \( \nC \), so it is the negative of \( a \) in \( \nC \), by uniqueness of negatives (@fd3:prp-ring-algebra (a)). If \( a \ne 0 \), the real inverse \( a^{-1} \) satisfies \( a a^{-1} = 1 \) in \( \nR \), hence in \( \nC \); and \( a \ne 0 \) in \( \nC \), since \( \iota \) is injective. So \( a^{-1} \) is the inverse of \( a \) in \( \nC \), by uniqueness of inverses in the field \( \nC \) (@fd3:lem-field-fraction-rules (a)).
:::

Everything proved for an arbitrary field now holds in \( \nC \), without a new proof. From @fd3:lem-field-fraction-rules: the inverse \( z^{-1} \) is the **only** \( y \) with \( zy = 1 \), and \( (zw)^{-1} = z^{-1} w^{-1} \) for non-zero \( z, w \); fractions \( z/w \coloneqq z w^{-1} \) add and multiply by the usual rules; and \( \nC \) has **no zero divisors**: \( zw = 0 \) forces \( z = 0 \) or \( w = 0 \). By @prp-power-laws-commutative-ring (d), \( z^n \ne 0 \) whenever \( z \ne 0 \). These are the facts that the rest of the chapter uses when it cancels a non-zero factor.

::: {.remark}
*Algebraic Preliminaries*, Chapter 1 collects fields as a notion with many examples, finite and infinite. This theorem is the one it cites for \( \nC \), and \( \nR \subseteq \nC \), with the closure just proved, is one of its examples of one field inside another.
:::

In practice, a quotient is computed by "multiplying top and bottom by the conjugate". For \( w \ne 0 \), @prp-complex-inverse gives
\[
\frac{z}{w} = z w^{-1} = \frac{z \conj{w}}{\abs{w}^2} ,
\]
which is the fraction \( z/w \) multiplied by \( \conj{w}/\conj{w} = 1 \) (here \( \conj{w} \ne 0 \), since \( \abs{\conj{w}} = \abs{w} \ne 0 \) by @thm-conjugate-properties (d), (e)) and simplified with the product rule for fractions (@fd3:lem-field-fraction-rules (b)): the new denominator \( w \conj{w} = \abs{w}^2 \) is real.

::: {#exm-complex-division}
[Dividing Complex Numbers]

Write \( \dfrac{1}{3 + 4i} \) and \( \dfrac{5 + i}{1 - i} \) in the form \( a + bi \) with \( a, b \in \nR \).
:::

::: {.solution}
For the first, \( \abs{3 + 4i}^2 = 25 \) and \( \conj{3 + 4i} = 3 - 4i \), so by @prp-complex-inverse
\[
\frac{1}{3 + 4i} = \frac{3 - 4i}{25} = \frac{3}{25} - \frac{4}{25} i .
\]
Check: \( (3 + 4i)(3 - 4i) = 9 + 16 = 25 \), so the product with \( 3 + 4i \) is \( 25/25 = 1 \).

For the second, \( \abs{1 - i}^2 = 2 \) and \( \conj{1 - i} = 1 + i \), so
\[
\frac{5 + i}{1 - i} = \frac{(5 + i)(1 + i)}{2} = \frac{5 + 5i + i + i^2}{2} = \frac{4 + 6i}{2} = 2 + 3i .
\]
This agrees with \( (2 + 3i)(1 - i) = 5 + i \) from @exm-complex-arithmetic: since \( 1 - i \ne 0 \), the quotient is the **only** \( u \) with \( u(1 - i) = 5 + i \). Indeed, if \( u(1 - i) = 5 + i \), then \( u = u \cdot 1 = u\bigl((1 - i)(1 - i)^{-1}\bigr) = \bigl(u(1 - i)\bigr)(1 - i)^{-1} = (5 + i)(1 - i)^{-1} \), by (F7), (F8) and (F5) in the field \( \nC \) (@thm-complex-numbers-field).
:::

::: {.check}
Compute \( \abs{(1 + i)(1 - i)} \) in two ways: by multiplying first, and by @thm-conjugate-properties (d). Then compute \( 1/i \).
:::

::: {.solution}
Multiplying first, \( (1 + i)(1 - i) = 1 + 1 = 2 \), so the modulus is \( \abs{2} = 2 \). By (d), it is \( \abs{1 + i}\,\abs{1 - i} = \sqrt{2} \cdot \sqrt{2} = 2 \), since \( \sqrt{2}\sqrt{2} = (\sqrt 2)^2 = 2 \). And \( 1/i = \conj{i}/\abs{i}^2 = -i/1 = -i \); check: \( i(-i) = -i^2 = 1 \).
:::

## Exercises

### A. Check your understanding

:::: {#exr-conjugate-and-modulus-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define the complex conjugate \( \conj{z} \) and the modulus \( \abs{z} \) of \( z = a + bi \), where \( a, b \in \nR \). Which earlier result guarantees that \( \abs{z} \) exists?
2. True or false, with a reason: \( z \conj{z} \) is a non-negative real number for every \( z \in \nC \).
3. Where exactly is the hypothesis \( z \ne 0 \) used in the proof of @prp-complex-inverse?
4. Write \( 1/(1 + 2i) \) in the form \( a + bi \) with \( a, b \in \nR \).
:::
::::

::: {.solution}
(a) \( \conj{z} \coloneqq a - bi \) and \( \abs{z} \coloneqq \sqrt{a^2 + b^2} \), the non-negative square root. It exists by @fd3:prp-cof-square-roots, since \( \nR \) is a complete ordered field and \( a^2 + b^2 \ge 0 \).

(b) True. By @thm-conjugate-properties (c), \( z \conj{z} = \abs{z}^2 \), the square of a real number, and squares of real numbers are non-negative (@fd3:prp-ordered-ring-rules (e) when \( \abs{z} \ne 0 \), and \( 0^2 = 0 \) by @fd3:prp-ring-algebra (b) when \( \abs{z} = 0 \)).

(c) It gives \( \abs{z} \ne 0 \) by @thm-conjugate-properties (e), hence \( \abs{z}^2 > 0 \), so that \( 1/\abs{z}^2 \) exists in \( \nR \). Nowhere else.

(d) \( \abs{1 + 2i}^2 = 1 + 4 = 5 \) and \( \conj{1 + 2i} = 1 - 2i \), so \( 1/(1 + 2i) = (1 - 2i)/5 = \frac{1}{5} - \frac{2}{5} i \). Check: \( (1 + 2i)(1 - 2i) = 5 \).
:::

### B. Practice

:::: {#exr-conjugate-and-modulus-b1}
[B1: Arithmetic]

Write each of the following in the form \( a + bi \) with \( a, b \in \nR \), or as a real number where indicated.

::: {.enumerate options="label=(\alph*)"}
1. \( (3 - 2i)(4 + i) \).
2. \( \dfrac{1 + 2i}{2 - i} \).
3. \( \abs{(3 + 4i)(5 - 12i)} \), without expanding the product.
4. \( \operatorname{Re}\dfrac{1}{1 + i} \) and \( \operatorname{Im}\dfrac{1}{1 + i} \).
:::
::::

::: {.solution}
(a) \( (3 - 2i)(4 + i) = 12 + 3i - 8i - 2i^2 = 14 - 5i \).

(b) By @prp-complex-inverse, multiply by \( \conj{2 - i} = 2 + i \) and divide by \( \abs{2 - i}^2 = 5 \):
\[
\frac{1 + 2i}{2 - i} = \frac{(1 + 2i)(2 + i)}{5} = \frac{2 + i + 4i + 2i^2}{5} = \frac{5i}{5} = i .
\]
Check: \( i(2 - i) = 2i - i^2 = 1 + 2i \).

(c) By @thm-conjugate-properties (d), \( \abs{(3 + 4i)(5 - 12i)} = \abs{3 + 4i}\,\abs{5 - 12i} = 5 \cdot 13 = 65 \), since \( \abs{5 - 12i} = \sqrt{25 + 144} = \sqrt{169} = 13 \) (\( 13 \ge 0 \) and \( 13^2 = 169 \)).

(d) \( \dfrac{1}{1 + i} = \dfrac{1 - i}{2} = \dfrac{1}{2} - \dfrac{1}{2} i \), so the real part is \( 1/2 \) and the imaginary part is \( -1/2 \).
:::

:::: {#exr-conjugate-and-modulus-b2}
[B2]

Let \( z \in \nC \). Prove:

::: {.enumerate options="label=(\alph*)"}
1. \( \operatorname{Re} z = \dfrac{z + \conj{z}}{2} \) and \( \operatorname{Im} z = \dfrac{z - \conj{z}}{2i} \);
2. \( z \in \nR \) if and only if \( \conj{z} = z \);
3. \( \operatorname{Re} z = 0 \) if and only if \( \conj{z} = -z \).
:::
::::

::: {.solution}
Write \( z = a + bi \) with \( a, b \in \nR \).

(a) By @thm-conjugate-properties (c), \( z + \conj{z} = 2a \), and \( 2 \ne 0 \), so \( (z + \conj{z})/2 = a = \operatorname{Re} z \). Also \( z - \conj{z} = (a - a) + (b + b)i = 2bi \), and \( 2i \ne 0 \), so \( (z - \conj{z})/(2i) = \bigl(b(2i)\bigr)(2i)^{-1} = b\bigl((2i)(2i)^{-1}\bigr) = b = \operatorname{Im} z \), using \( 2bi = b \cdot (2i) \) and (F5), (F8), (F7) in the field \( \nC \) (@thm-complex-numbers-field).

(b) \( \conj{z} = z \) means \( a - bi = a + bi \), which by comparing imaginary parts holds if and only if \( -b = b \), that is \( 2b = 0 \), that is \( b = 0 \) (as \( 2 \ne 0 \) in \( \nR \)). And \( b = 0 \) means \( z = a \in \nR \).

(c) \( \conj{z} = -z \) means \( a - bi = -a - bi \), which by comparing parts holds if and only if \( a = -a \) (the imaginary parts agree), that is \( 2a = 0 \), that is \( a = 0 \) (as in (b)).
:::

::: {#exr-conjugate-and-modulus-b3}
[B3]

Let \( z, w \in \nC \) with \( w \ne 0 \). Prove that \( \conj{z/w} = \conj{z}/\conj{w} \) and \( \abs{z/w} = \abs{z}/\abs{w} \).

*Hint: start from \( w \cdot (z/w) = z \).*
:::

::: {.solution}
Let \( q \coloneqq z/w = z w^{-1} \), so \( wq = z \). By @thm-conjugate-properties (b), \( \conj{w}\,\conj{q} = \conj{z} \). Here \( \conj{w} \ne 0 \): \( \abs{\conj{w}} = \abs{w} \ne 0 \) by @thm-conjugate-properties (d), (e). Multiplying by \( \conj{w}^{-1} \) gives \( \conj{q} = \conj{z}/\conj{w} \).

Likewise, by @thm-conjugate-properties (d), \( \abs{w}\,\abs{q} = \abs{z} \), with \( \abs{w} \ne 0 \) by (e). Dividing by \( \abs{w} \) in \( \nR \) gives \( \abs{q} = \abs{z}/\abs{w} \).
:::

### C. Going deeper

::: {#exr-conjugate-and-modulus-c1}
[C1: Exit check: the complex numbers form a field]

Prove @thm-conjugate-properties (b) and (d) and @prp-complex-inverse, and conclude that \( \nC \) satisfies (F8). You may use @def-complex-numbers, @prp-complex-arithmetic-laws, @prp-reals-embed-complex, @thm-conjugate-properties (c) and (e), and the rules of the ordered field \( \nR \), including @fd3:prp-cof-square-roots.
:::

::: {.solution}
*(b).* Let \( z = a + bi \), \( w = c + di \). Then \( zw = (ac - bd) + (ad + bc)i \), so \( \conj{zw} = (ac - bd) - (ad + bc)i \). And \( \conj{z}\,\conj{w} = (a - bi)(c - di) = \bigl(ac - (-b)(-d)\bigr) + \bigl(-ad - bc\bigr)i = (ac - bd) - (ad + bc)i \). The two agree.

*(d).* By (c), (b), and commutativity and associativity of multiplication (@prp-complex-arithmetic-laws (a), (b)),
\[
\abs{zw}^2 = (zw)\conj{zw} = (zw)(\conj{z}\,\conj{w}) = (z\conj{z})(w\conj{w}) = \abs{z}^2\abs{w}^2 = \bigl(\abs{z}\abs{w}\bigr)^2 .
\]
Both \( \abs{zw} \) and \( \abs{z}\abs{w} \) are non-negative (\( \abs{z}\abs{w} \) is \( 0 \) if a factor is \( 0 \), by @fd3:prp-ring-algebra (b), and positive by (O4) of @fd3:def-ordered-ring-and-field otherwise), so both are the non-negative square root of \( \abs{z}^2 \abs{w}^2 \), and they are equal by the uniqueness clause of @fd3:prp-cof-square-roots. Also \( \abs{\conj{z}} = \sqrt{a^2 + (-b)^2} = \sqrt{a^2 + b^2} = \abs{z} \).

*Inverse.* Let \( z \ne 0 \). By (e), \( \abs{z} \ne 0 \), so \( \abs{z}^2 > 0 \) (@fd3:prp-ordered-ring-rules (e)), and \( r \coloneqq 1/\abs{z}^2 \) exists in \( \nR \). With \( w \coloneqq r \conj{z} \), @prp-complex-arithmetic-laws and (c) give \( zw = r(z\conj{z}) = r\abs{z}^2 = 1 \), where the last product is computed in \( \nR \), which agrees with the product in \( \nC \) (@prp-reals-embed-complex).

*(F8).* Every non-zero \( z \in \nC \) has an element \( w \) with \( zw = 1 \), which is (F8) of @fd3:def-commutative-ring-and-field.

**Marking scheme.** (10 points)
- 2: (b) by expanding both sides in real and imaginary parts and comparing.
- 3: (d) via \( \abs{zw}^2 = (zw)\conj{zw} \) and (b), with commutativity named for the reordering.
- 1: equal non-negative squares give equal numbers, with a reason (uniqueness of the non-negative square root, or @fd3:prp-ordered-ring-rules (g) with trichotomy).
- 2: \( \abs{z}^2 > 0 \) for \( z \ne 0 \), with a reason.
- 2: \( zw = 1 \) for \( w = (1/\abs{z}^2)\conj{z} \), and the conclusion stated as (F8).
Fatal errors (0 for the step): dividing by \( z \) or by \( \abs{z} \) before showing it is non-zero; "\( \abs{zw} = \abs{z}\abs{w} \) because the modulus is a length and multiplication scales lengths" (circular: the scaling picture is a consequence of (d)). A second route to (d), expanding \( (ac - bd)^2 + (ad + bc)^2 = (a^2 + b^2)(c^2 + d^2) \) and then taking square roots, earns the 3 points of the (d) step in full.
:::

:::: {#exr-conjugate-and-modulus-c2}
[C2: Gaussian rationals]

Let \( \nQ(i) \coloneqq \{ a + bi : a, b \in \nQ \} \subseteq \nC \), where \( \nQ \subseteq \nR \) as in *Number Systems: From \(\nN\) to \(\nR\)*, Chapter 5 (@fd3:thm-reals-complete-ordered-field). Prove that \( \nQ(i) \) is closed under addition, negatives, multiplication, inverses of non-zero elements, and conjugation.
::::

::: {.solution}
Under the identification of \( q \) with \( \kappa(q) \), \( \kappa \) sends sums, products, negatives and inverses of non-zero rationals to the same operations in \( \nR \) (@fd3:thm-rational-embedding (a), (c)), so the copy of \( \nQ \) in \( \nR \) is closed under \( + \), \( \cdot \), negatives and inverses of non-zero elements.

Let \( z = a + bi \) and \( w = c + di \) with \( a, b, c, d \in \nQ \). Then \( z + w = (a + c) + (b + d)i \), \( -z = (-a) + (-b)i \) and \( zw = (ac - bd) + (ad + bc)i \) have rational parts, and so does \( \conj{z} = a + (-b)i \). If \( z \ne 0 \), then \( a^2 + b^2 = \abs{z}^2 \ne 0 \) by @thm-conjugate-properties (e), and \( a^2 + b^2 \in \nQ \). By @prp-complex-inverse,
\[
z^{-1} = \frac{a}{a^2 + b^2} + \frac{-b}{a^2 + b^2}\, i ,
\]
whose parts are quotients of rational numbers by a non-zero rational number, hence rational. So all five operations stay in \( \nQ(i) \). For example, \( (1 + 2i)^{-1} = \frac15 - \frac25 i \in \nQ(i) \).

*Algebraic Preliminaries*, Chapter 1 calls a subset of a field a subfield when it contains \( 0 \) and \( 1 \) and has these closure properties. \( \nQ(i) \) contains \( 0 = 0 + 0i \) and \( 1 = 1 + 0i \), and it is one of the examples there.

**Marking scheme.** (10 points)
- 2: the copy of \( \nQ \) in \( \nR \) is closed under \( + \), \( \cdot \), negatives and inverses of non-zero elements, with a reason (@fd3:thm-rational-embedding (a), (c)).
- 2: \( z + w \), \( -z \) and \( \conj{z} \) have rational real and imaginary parts.
- 2: \( zw = (ac - bd) + (ad + bc)i \) has rational parts.
- 3: for \( z \ne 0 \), \( a^2 + b^2 \) is non-zero (@thm-conjugate-properties (e)) and rational, and the formula of @prp-complex-inverse then gives rational parts.
- 1: the conclusion that all five operations stay in \( \nQ(i) \).
Fatal errors (0 for the step): dividing by \( a^2 + b^2 \) without first using \( z \ne 0 \) to show it is non-zero; assuming without a reason that \( \nQ \subseteq \nR \) is closed under the operations.
:::

<!-- dependency ledger
def-conjugate-modulus (claim): the modulus depends only on z | prp-reals-embed-complex (compare parts); inline
def-conjugate-modulus (claim): a^2 + b^2 >= 0 (0^2 = 0 in the zero case) | fd3:prp-ordered-ring-rules (e), (b) (cited); fd3:prp-ring-algebra (b) for 0^2 = 0, used silently
def-conjugate-modulus (example): sqrt 25 = 5, sqrt 1 = 1, sqrt 0 = 0, sqrt 169 = 13 by uniqueness | fd3:prp-cof-square-roots (cited); arithmetic in R; verify/ch01/def-conjugate-modulus.py
def-conjugate-modulus (claim): over Q, |1 + i| would be a rational square root of 2 | fd3:thm-no-rational-square-two (cited)
def-conjugate-modulus (claim): N(z) = a^2 + b^2: N(2) = 4, N(1+1) = 4 > N(1) + N(1) = 2 | arithmetic; inline
prp-modulus-of-real (proof): 0 * i = i * 0 = 0 and -0 = 0 in C | (F6), fd3:prp-ring-algebra (a), (b) in the commutative ring C (prp-complex-arithmetic-laws and the remark after it) (cited)
def-conjugate-modulus (claim): warning: |z|^2 = z^2 only for real z: comparing real parts, 2b^2 = 0 => b = 0 | fd3:prp-ordered-ring-rules (e), (f), (h) (cited); inline
thm-conjugate-properties (proof): -(b + d) = (-b) + (-d); -(-b) = b; (-b)(-d) = bd; a(-d) + (-b)c = -(ad + bc); (-b)^2 = b^2 in R | fd3:prp-ring-algebra (a), (c) (cited)
thm-conjugate-properties (proof): (sqrt x)^2 = x | fd3:prp-cof-square-roots (definition of sqrt); inline
thm-conjugate-properties (proof): |z||w| >= 0 | (O4) of fd3:def-ordered-ring-and-field and fd3:prp-ring-algebra (b) (cited)
thm-conjugate-properties (claim): z -> -conj z sends 1 to -1 and 1*1 to -1 | arithmetic; inline
thm-conjugate-properties (claim): pointers to Section 1.3 (square the modulus, triangle inequality) and Section 1.5 (angles) | prose pointers within the chapter; nothing depends on them
prp-complex-inverse (proof): the product 1/|z|^2 * |z|^2 = 1 computed in R equals that in C | prp-reals-embed-complex (cited)
thm-complex-numbers-field (claim): pointer to *Algebraic Preliminaries*, Chapter 1 (fields; R inside C as one example of a subfield) | prose pointer; nothing depends on it
exm-complex-division (solution): 1/(3 + 4i) = 3/25 - (4/25)i; (5 + i)/(1 - i) = 2 + 3i | verify/ch01/exm-complex-division.py
exm-complex-division (example): z/w = z conj(w) / |w|^2 | prp-complex-inverse, fd3:lem-field-fraction-rules (b) (cited); conj w != 0 by thm-conjugate-properties (d), (e) (cited)
exm-complex-division (solution): the quotient is the only u with u(1 - i) = 5 + i | (F5), (F7), (F8) in C via thm-complex-numbers-field (cited); inline
prp-modulus-of-real (claim): the Quick check after it: -2i and 1 - i have conjugates 2i, 1 + i and moduli 2, sqrt 2 | verify/ch01/def-conjugate-modulus.py
exm-complex-division (example): the Quick check after it: |(1+i)(1-i)| = 2, sqrt2 * sqrt2 = 2, 1/i = -i | verify/ch01/exm-complex-division.py
exr-conjugate-and-modulus-a1 (solution): 1/(1 + 2i) = 1/5 - (2/5)i | verify/ch01/exr-conjugate-and-modulus-a1.py
exr-conjugate-and-modulus-b1 (solution): 14 - 5i; i; 65 (|5 - 12i| = 13); 1/2, -1/2 | verify/ch01/exr-conjugate-and-modulus-b1.py
exr-conjugate-and-modulus-b2 (solution): 2 != 0 in R and 2i != 0 in C; 2bi = b(2i); (b(2i))(2i)^{-1} = b | fd3:prp-ordered-ring-rules (h) (2 = 2 * 1 > 0); prp-complex-arithmetic-laws; (F5), (F7), (F8) via thm-complex-numbers-field; inline
exr-conjugate-and-modulus-c1 (solution): (ac - bd)^2 + (ad + bc)^2 = (a^2 + b^2)(c^2 + d^2) (second route, in the marking scheme) | verify/ch01/thm-conjugate-properties.py
exr-conjugate-and-modulus-c2 (solution): Q closed in R under +, *, negatives, inverses | fd3:thm-rational-embedding (a), (c) (cited); identification q = kappa(q) of F3.10 (prose)
exr-conjugate-and-modulus-a1 (solution): squares of reals are >= 0 | fd3:prp-ordered-ring-rules (e), fd3:prp-ring-algebra (b) (cited)
exr-conjugate-and-modulus-c1 (solution): |z||w| >= 0; r|z|^2 = 1 in R equals that in C | (O4) of fd3:def-ordered-ring-and-field, fd3:prp-ring-algebra (b), prp-reals-embed-complex (cited)
exr-conjugate-and-modulus-c2 (solution): pointer to *Algebraic Preliminaries*, Chapter 1 (subfields) | prose pointer; nothing depends on it
-->
