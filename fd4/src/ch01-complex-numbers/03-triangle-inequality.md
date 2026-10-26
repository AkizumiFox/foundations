# The Triangle Inequality

The modulus of Section 1.2 measures a complex number by a real one. Picture \( z = a + bi \) as the point \( (a, b) \) of the plane: by Pythagoras, \( \abs{z} = \sqrt{a^2 + b^2} \) is its distance from the origin, and \( \abs{z - w} \) is the distance between the points \( z \) and \( w \). In a triangle, one side is never longer than the other two together. This section proves the algebraic form of that fact, \( \abs{z + w} \le \abs{z} + \abs{w} \), from the definitions alone. The picture motivates it; no step of the proof uses it.

## Why the old proof does not transfer

For an ordered field, *Number Systems: From \(\nN\) to \(\nR\)*, Chapter 4 proved \( \abs{x + y} \le \abs{x} + \abs{y} \) by trapping (@fd3:prp-absolute-value-ordered-field (e)). Each of \( x \) and \( y \) lies between \( \pm \) its absolute value, \( -\abs{x} \le x \le \abs{x} \) (part (c) there); adding the two traps traps \( x + y \) between \( \pm(\abs{x} + \abs{y}) \), and part (d) reads that as the inequality.

That route needs \( x \le \abs{x} \): a comparison between \( x \) itself and a number. For a complex \( z \), "\( z \le \abs{z} \)" compares a complex number with a real one, and \( \nC \) has been given no order in which to make the comparison. Section 1.4 shows that no order compatible with the arithmetic of \( \nC \) exists (@prp-complex-not-orderable). So the proof must compare **real** numbers only.

Two kinds of real number are at hand. Moduli are real, and so are real parts. The device that connects them to the arithmetic of \( \nC \) is the identity \( \abs{u}^2 = u\conj{u} \) of @thm-conjugate-properties (c). A modulus is a square root, and square roots do not add well; its square is a product, and products expand. So we will compare squares and then come back.

**Comparing squares.** Coming back from squares to the numbers needs one rule about the real numbers. Let \( p, q \in \nR \) with \( p \ge 0 \) and \( q \ge 0 \). Then
\[
p \le q \iff p^2 \le q^2 , \qquad\qquad p = q \iff p^2 = q^2 ,
\]
and likewise with \( < \) on both sides. The strict form is @fd3:prp-ordered-ring-rules (g). For the first equivalence: if \( p < q \), then \( p^2 < q^2 \) by (g), and if \( p = q \) the squares agree. Conversely, if \( p^2 \le q^2 \) and yet \( q < p \), then (g) gives \( q^2 < p^2 \), which contradicts \( p^2 \le q^2 \) by trichotomy (O1); so \( p \le q \). The second equivalence follows from the first, applied in both directions, and trichotomy. In words: *for non-negative reals, squaring neither creates nor destroys a comparison.* Both hypotheses \( p \ge 0 \) and \( q \ge 0 \) matter: \( (-2)^2 > 1^2 \), and yet \( -2 < 1 \).

## The real part is at most the modulus

The single estimate the proof needs is that a real part never exceeds the modulus. It comes with two companions, which say that the modulus and the "taxicab size" \( \abs{\operatorname{Re} u} + \abs{\operatorname{Im} u} \) are comparable.

::: {#lem-real-part-at-most-modulus}
[Real and Imaginary Parts against the Modulus]

For every \( u \in \nC \),
\[
\abs{\operatorname{Re} u} \le \abs{u} , \qquad \abs{\operatorname{Im} u} \le \abs{u} , \qquad \abs{u} \le \abs{\operatorname{Re} u} + \abs{\operatorname{Im} u} .
\]
In particular \( \operatorname{Re} u \le \abs{u} \).
:::

Here \( \abs{\operatorname{Re} u} \) is the absolute value of a real number. By @prp-modulus-of-real it is the same whether it is read as the absolute value of the ordered field \( \nR \) from *Number Systems: From \(\nN\) to \(\nR\)*, Chapter 4 (@fd3:def-absolute-value-ordered-field) or as the modulus of a complex number that happens to be real, so the lemma has only one reading.

::: {.idea}
Every quantity in the lemma is a non-negative real, so compare squares. The square of \( \abs{u} \) is \( x^2 + y^2 \), and the squares of \( \abs{x} \) and \( \abs{y} \) are \( x^2 \) and \( y^2 \), each at most the sum; the square of \( \abs{x} + \abs{y} \) is the sum plus the non-negative cross term \( 2\abs{x}\abs{y} \).
:::

::: {.proof}
Write \( u = x + yi \) with \( x, y \in \nR \). By @def-conjugate-modulus and the defining property of the square root (@fd3:prp-cof-square-roots), \( \abs{u} \ge 0 \) and \( \abs{u}^2 = x^2 + y^2 \).

Since \( y^2 \ge 0 \) (@fd3:prp-ordered-ring-rules (e) if \( y \ne 0 \); \( 0^2 = 0 \) otherwise), adding \( x^2 \) gives \( x^2 \le x^2 + y^2 \) by @fd3:prp-ordered-ring-rules (b). Also \( \abs{x}^2 = x^2 \) and \( \abs{x} \ge 0 \) (@fd3:prp-absolute-value-ordered-field (a), (b)). Hence \( \abs{x}^2 \le \abs{u}^2 \), with both \( \abs{x} \) and \( \abs{u} \) non-negative, and comparing squares gives \( \abs{x} \le \abs{u} \). The same argument with the roles of \( x \) and \( y \) exchanged gives \( \abs{y} \le \abs{u} \). Then \( \operatorname{Re} u = x \le \abs{x} \) by @fd3:prp-absolute-value-ordered-field (c), so \( \operatorname{Re} u \le \abs{u} \).

For the last inequality, expand with @fd3:prp-ring-algebra (d):
\[
\begin{aligned}
\bigl( \abs{x} + \abs{y} \bigr)^2 &= \abs{x}^2 + 2 \abs{x} \abs{y} + \abs{y}^2 \\
&= x^2 + y^2 + 2 \abs{x} \abs{y} \ge x^2 + y^2 = \abs{u}^2 ,
\end{aligned}
\]
where the inequality holds because \( \abs{x}\abs{y} \ge 0 \) as a product of non-negative reals, so \( 2 \abs{x}\abs{y} \ge 0 \), and @fd3:prp-ordered-ring-rules (b) adds it. Both \( \abs{x} + \abs{y} \) and \( \abs{u} \) are non-negative, so comparing squares gives \( \abs{u} \le \abs{x} + \abs{y} \). This proves the lemma.
:::

For \( u = 3 - 4i \) the three inequalities read \( 3 \le 5 \), \( 4 \le 5 \) and \( 5 \le 7 \). For \( u = 2 \) they read \( 2 \le 2 \), \( 0 \le 2 \) and \( 2 \le 2 \): a real \( u \) makes the first and third equalities. The inequality \( \operatorname{Re} u \le \abs{u} \) is strict for \( u = -1 \), where it reads \( -1 \le 1 \); the absolute value inside the first inequality is what makes it sharp for real \( u \) of either sign.

::: {.check}
Find a non-zero \( u \in \nC \) with \( \operatorname{Re} u = 0 \). What do the three inequalities of @lem-real-part-at-most-modulus say for it?
:::

::: {.solution}
For example \( u = 2i \), with \( \operatorname{Re} u = 0 \), \( \operatorname{Im} u = 2 \) and \( \abs{u} = \sqrt{0 + 4} = 2 \). The inequalities read \( 0 \le 2 \), \( 2 \le 2 \) and \( 2 \le 0 + 2 \). Any \( u = yi \) with \( y \ne 0 \) works the same way: \( \abs{u} = \abs{y} \), so the second and third inequalities are equalities.
:::

## The triangle inequality

We can now state the theorem. Its proof is the first full run of the move this chapter is built around.

::: {#thm-complex-triangle-inequality}
[Triangle Inequality for Complex Numbers]

For all \( z, w \in \nC \),
\[
\abs{z + w} \le \abs{z} + \abs{w} .
\]
:::

*Try it first (ten minutes): show \( \abs{z + w}^2 \le (\abs{z} + \abs{w})^2 \) by expanding both sides with \( \abs{u}^2 = u \conj{u} \), and note which term you cannot yet bound.*

::: {.idea}
Expanding the left side with \( \abs{u}^2 = u\conj{u} \) and conjugation of sums gives \( \abs{z}^2 + z\conj{w} + \conj{z}w + \abs{w}^2 \); the right side is \( \abs{z}^2 + 2\abs{z}\abs{w} + \abs{w}^2 \). Everything matches except the cross term \( z\conj{w} + \conj{z}w \), and an attempt usually stops there: it looks like a complex number, and complex numbers cannot be compared with \( 2\abs{z}\abs{w} \). The way out is to notice that \( \conj{z} w \) is the conjugate of \( z \conj{w} \), so the cross term is \( u + \conj{u} = 2 \operatorname{Re} u \) with \( u = z\conj{w} \): a **real** number after all. A real part is at most the modulus, and \( \abs{z\conj{w}} = \abs{z}\abs{w} \). Squares compare, so the moduli do.

*Before reading on: where is \( \operatorname{Re} u \le \abs{u} \) used, and why may we compare squares?*
:::

::: {.proof}
Let \( z, w \in \nC \). By @thm-conjugate-properties (c), then (a), then @prp-complex-arithmetic-laws (c) together with (a) and (b) (distributivity, commutativity, associativity),
\[
\begin{aligned}
\abs{z + w}^2 &= (z + w)\,\conj{(z + w)} = (z + w)(\conj{z} + \conj{w}) \\
&= z\conj{z} + z\conj{w} + \conj{z}w + w\conj{w} .
\end{aligned}
\]
By @thm-conjugate-properties (b) and (a), \( \conj{z\conj{w}} = \conj{z}\,\conj{\conj{w}} = \conj{z} w \). So with \( u \coloneqq z\conj{w} \), the two middle terms are \( u + \conj{u} = 2 \operatorname{Re} u \), by @thm-conjugate-properties (c). Using (c) once more for \( z\conj{z} \) and \( w\conj{w} \),
\[
\abs{z + w}^2 = \abs{z}^2 + 2 \operatorname{Re}(z\conj{w}) + \abs{w}^2 .
\]
Every term here is real, and sums and products of real numbers are the same in \( \nC \) as in \( \nR \) (@prp-reals-embed-complex), so the inequalities below take place in the ordered field \( \nR \). By @lem-real-part-at-most-modulus, \( \operatorname{Re}(z\conj{w}) \le \abs{z\conj{w}} \), and by @thm-conjugate-properties (d), \( \abs{z\conj{w}} = \abs{z}\,\abs{\conj{w}} = \abs{z}\,\abs{w} \). Adding this inequality to itself (\( 2a = (1 + 1)a = a + a \) by distributivity) and then adding \( \abs{z}^2 + \abs{w}^2 \) (@fd3:prp-ordered-ring-rules (b) twice), and expanding the square with @fd3:prp-ring-algebra (d),
\[
\abs{z + w}^2 \le \abs{z}^2 + 2\abs{z}\abs{w} + \abs{w}^2 = \bigl( \abs{z} + \abs{w} \bigr)^2 .
\]
Both \( \abs{z + w} \) and \( \abs{z} + \abs{w} \) are non-negative real numbers, so comparing squares gives \( \abs{z + w} \le \abs{z} + \abs{w} \). This proves the triangle inequality.
:::

The proof answers its prompt in two lines. \( \operatorname{Re} u \le \abs{u} \) is used once, to bound the cross term \( 2\operatorname{Re}(z\conj{w}) \) by \( 2\abs{z\conj{w}} \). Comparing squares is legitimate because the two quantities being compared, \( \abs{z + w} \) and \( \abs{z} + \abs{w} \), are both non-negative; without that, a smaller square would say nothing about the numbers.

This route has a name in this chapter: **square the modulus**. *The modulus is a square root, and square roots are hard to handle; its square \( \abs{u}^2 = u\conj{u} \) is a product, so square, expand with conjugates, bound or compare the real numbers you get, and take the non-negative square root back.* Section 1.2 used the same move once already, for \( \abs{zw} = \abs{z}\abs{w} \) (@thm-conjugate-properties (d)). The linear algebra volumes take the same route, square, expand, bound the cross term, for the length of a vector in an inner product space.

::: {.warning}
The square of the modulus is \( u\conj{u} \), not \( u^2 \). Expanding \( \abs{z + w}^2 \) as \( (z + w)^2 = z^2 + 2zw + w^2 \) gives nonsense: for \( z = w = i \), \( (z + w)^2 = (2i)^2 = -4 \), while \( \abs{z + w}^2 = \abs{2i}^2 = 4 \). The cross term of the correct expansion is \( z\conj{w} + \conj{z}w \), and only that form is real.
:::

::: {.remark}
The inequality can be strict: for \( z = 1 \) and \( w = -1 \), the left side is \( \abs{0} = 0 \) and the right side is \( 2 \). For real \( z, w \), every modulus in the statement is the absolute value of *Number Systems: From \(\nN\) to \(\nR\)*, Chapter 4 (@prp-modulus-of-real), and the theorem is @fd3:prp-absolute-value-ordered-field (e), reached by a different route.
:::

::: {.check}
Compute \( \abs{3 + 4i} + \abs{-3 + 4i} \) and \( \abs{(3 + 4i) + (-3 + 4i)} \), and check them against the triangle inequality.
:::

::: {.solution}
\( \abs{3 + 4i} = \sqrt{9 + 16} = 5 \) and \( \abs{-3 + 4i} = \sqrt{9 + 16} = 5 \), so the right side is \( 10 \). The sum is \( 8i \), and \( \abs{8i} = \sqrt{0 + 64} = 8 \). Indeed \( 8 \le 10 \). In the picture, the two points and \( 8i \) are three corners of a parallelogram with the origin as the fourth, and the diagonal \( 8 \) is shorter than the two sides \( 5 + 5 \).
:::

## Three variants

Three consequences are used often enough to be stated once: a lower bound for the modulus of a difference, the inequality for any finite number of terms, and a lower bound for the modulus of a sum.

::: {#cor-complex-triangle-variants}
[Variants of the Triangle Inequality]

Let \( z, w \in \nC \).

::: {.enumerate options="label=(\alph*)"}
1. *(Reverse triangle inequality.)* \( \bigl| \abs{z} - \abs{w} \bigr| \le \abs{z - w} \).
2. For every \( n \in \nN \) with \( n \ge 1 \) and all \( z_1, \dots, z_n \in \nC \), \( \displaystyle \Bigl| \sum_{k=1}^{n} z_k \Bigr| \le \sum_{k=1}^{n} \abs{z_k} \).
3. \( \abs{z} - \abs{w} \le \abs{z + w} \).
:::
:::

In (a), the outer bars are the absolute value of the real number \( \abs{z} - \abs{w} \). In words: (a) says that two points at distance \( \abs{z - w} \) from each other have distances from the origin that differ by at most that much; (b) says that a path of \( n \) steps is at least as long as the straight line from start to end; (c) says that adding \( w \) can lower the modulus by at most \( \abs{w} \).

::: {.idea}
For (a), split \( z \) as \( (z - w) + w \) and apply the theorem; that bounds \( \abs{z} - \abs{w} \) from above, and swapping \( z \) and \( w \) bounds it from below. For (b), add one term at a time. For (c), apply (a) to \( z \) and \( -w \).
:::

::: {.proof}
(a) Since \( z = (z - w) + w \), @thm-complex-triangle-inequality gives \( \abs{z} \le \abs{z - w} + \abs{w} \), so \( \abs{z} - \abs{w} \le \abs{z - w} \). Exchanging \( z \) and \( w \) gives \( \abs{w} - \abs{z} \le \abs{w - z} \). Moreover \( w - z = (-1)(z - w) \), so by @thm-conjugate-properties (d), \( \abs{w - z} = \abs{-1}\,\abs{z - w} = \abs{z - w} \), where \( \abs{-1} = 1 \) by @prp-modulus-of-real. Let \( t \coloneqq \abs{z} - \abs{w} \in \nR \). We have shown \( t \le \abs{z - w} \) and \( -t \le \abs{z - w} \), that is, \( -\abs{z - w} \le t \le \abs{z - w} \): if \( -t < \abs{z - w} \), then \( -\abs{z - w} < -(-t) = t \) by @fd3:prp-ordered-ring-rules (a) and @fd3:prp-ring-algebra (a), and if \( -t = \abs{z - w} \), then \( -\abs{z - w} = -(-t) = t \). By @fd3:prp-absolute-value-ordered-field (d), \( \abs{t} \le \abs{z - w} \).

(b) By induction on \( n \ge 1 \) (@fd1:ax-induction, through @fd3:cor-omega-identification (b), applied to the statement for \( n = m + 1 \), \( m \in \nN \)), with the sums defined by appending the last term, as for real sums (@fd2:def-sum-product). For \( n = 1 \), both sides are \( \abs{z_1} \). Suppose the inequality holds for \( n \), and let \( z_1, \dots, z_{n+1} \in \nC \). Then
\[
\begin{aligned}
\Bigl| \sum_{k=1}^{n+1} z_k \Bigr| &= \Bigl| \sum_{k=1}^{n} z_k + z_{n+1} \Bigr| \le \Bigl| \sum_{k=1}^{n} z_k \Bigr| + \abs{z_{n+1}} \\
&\le \sum_{k=1}^{n} \abs{z_k} + \abs{z_{n+1}} = \sum_{k=1}^{n+1} \abs{z_k} ,
\end{aligned}
\]
by @thm-complex-triangle-inequality, then the induction hypothesis with @fd3:prp-ordered-ring-rules (b).

(c) Apply (a) to \( z \) and \( -w \). Since \( z - (-w) = z + w \) (@fd3:prp-ring-algebra (a)) and \( \abs{-w} = \abs{-1}\abs{w} = \abs{w} \) as in (a), it reads \( \bigl| \abs{z} - \abs{w} \bigr| \le \abs{z + w} \). By @fd3:prp-absolute-value-ordered-field (c), \( \abs{z} - \abs{w} \le \bigl| \abs{z} - \abs{w} \bigr| \). This proves the corollary.
:::

Part (b) with \( n = 2 \) is the theorem itself, so the corollary contains it. *Algebraic Preliminaries*, Chapter 5 uses (b) and (c) to show that a polynomial expression of degree at least \( 1 \) is large in modulus when \( \abs{z} \) is large, a step towards the Fundamental Theorem of Algebra.

::: {.check}
Take \( z = 5 \) and \( w = 3i \). Compute both sides of (a) and of (c).
:::

::: {.solution}
\( \abs{z} = 5 \) and \( \abs{w} = 3 \), so \( \abs{z} - \abs{w} = 2 \). For (a): \( \abs{z - w} = \abs{5 - 3i} = \sqrt{34} \), and \( 2 \le \sqrt{34} \) because \( 2^2 = 4 \le 34 \) (comparing squares). For (c): \( \abs{z + w} = \abs{5 + 3i} = \sqrt{34} \) too, and again \( 2 \le \sqrt{34} \). Both bounds are far from sharp here; (a) is an equality when \( w = 0 \), for instance.
:::

## Exercises

### A. Check your understanding

::: {#exr-triangle-inequality-a1}
[A1]

These questions are about the proof of @thm-complex-triangle-inequality.

::: {.enumerate options="label=(\alph*)"}
1. Where in the proof is \( \operatorname{Re} u \le \abs{u} \) used, and for which \( u \)?
2. Why may the proof pass from \( \abs{z + w}^2 \le (\abs{z} + \abs{w})^2 \) back to \( \abs{z + w} \le \abs{z} + \abs{w} \)?
3. Run the proof on \( z = 3 \) and \( w = 4i \): compute the cross term \( 2\operatorname{Re}(z\conj{w}) \), then both sides of the squared inequality.
4. State the idea of the proof in two sentences.
5. True or false: \( \abs{z + w} = \abs{z} + \abs{w} \) for all \( z, w \in \nC \). Justify your answer.
:::
:::

::: {.solution}
(a) Once, to bound the cross term: with \( u = z\conj{w} \), \( 2\operatorname{Re}(z\conj{w}) \le 2\abs{z\conj{w}} \).

(b) Both \( \abs{z + w} \) and \( \abs{z} + \abs{w} \) are non-negative reals, and for non-negative reals \( p \le q \) if and only if \( p^2 \le q^2 \) (comparing squares, from @fd3:prp-ordered-ring-rules (g) and trichotomy).

(c) \( \conj{w} = -4i \), so \( z\conj{w} = 3 \cdot (-4i) = -12i \), with real part \( 0 \): the cross term is \( 0 \). Then \( \abs{z + w}^2 = 9 + 0 + 16 = 25 \) and \( (\abs{z} + \abs{w})^2 = (3 + 4)^2 = 49 \), and \( 25 \le 49 \). So \( \abs{3 + 4i} = 5 \le 7 \).

(d) Square both sides and expand with \( \abs{u}^2 = u\conj{u} \): everything matches except the cross term, which is \( 2\operatorname{Re}(z\conj{w}) \). A real part is at most the modulus, and \( \abs{z\conj{w}} = \abs{z}\abs{w} \), so the squares compare, and so do the non-negative moduli.

(e) False. For \( z = 1 \) and \( w = -1 \), \( \abs{z + w} = 0 \), but \( \abs{z} + \abs{w} = 2 \).
:::

### B. Practice

::: {#exr-triangle-inequality-b1}
[B1: The equality case]

Let \( z, w \in \nC \). Prove that \( \abs{z + w} = \abs{z} + \abs{w} \) if and only if \( z\conj{w} \) is a non-negative real number, that is, \( \operatorname{Im}(z\conj{w}) = 0 \) and \( \operatorname{Re}(z\conj{w}) \ge 0 \).

*Hint: trace the proof of the triangle inequality and ask where an inequality could be strict.*
:::

::: {.solution}
Let \( u \coloneqq z\conj{w} = x + yi \) with \( x, y \in \nR \). By the proof of @thm-complex-triangle-inequality,
\[
\begin{aligned}
\abs{z + w}^2 &= \abs{z}^2 + 2x + \abs{w}^2 , \\
\bigl( \abs{z} + \abs{w} \bigr)^2 &= \abs{z}^2 + 2\abs{u} + \abs{w}^2 ,
\end{aligned}
\]
the second because \( \abs{z}\abs{w} = \abs{u} \) (@thm-conjugate-properties (d)). Both moduli are non-negative, so (comparing squares) \( \abs{z + w} = \abs{z} + \abs{w} \) holds if and only if the squares are equal, that is, if and only if \( 2x = 2\abs{u} \), that is, \( x = \abs{u} \).

It remains to show that \( x = \abs{u} \) holds exactly when \( y = 0 \) and \( x \ge 0 \). If \( x = \abs{u} \), then \( x \ge 0 \), and squaring gives \( x^2 = x^2 + y^2 \), so \( y^2 = 0 \) and \( y = 0 \) (@fd3:prp-ordered-ring-rules (e): a non-zero square is positive). Conversely, if \( y = 0 \) and \( x \ge 0 \), then \( \abs{u} = \sqrt{x^2} = x \), since \( x \ge 0 \) and \( x^2 = x^2 \) (uniqueness in @fd3:prp-cof-square-roots). Hence \( \abs{z + w} = \abs{z} + \abs{w} \) if and only if \( z\conj{w} \) is a non-negative real number.

For instance \( z = 1 + i \), \( w = 2 + 2i \): \( z\conj{w} = (1 + i)(2 - 2i) = 4 \ge 0 \), and indeed \( \abs{3 + 3i} = \sqrt{18} = 3\sqrt 2 = \sqrt 2 + 2\sqrt 2 = \abs{1 + i} + \abs{2 + 2i} \). In the picture: equality holds exactly when one of \( z, w \) is \( 0 \) or they point in the same direction from the origin. The linear algebra volumes prove the version for \( n \) terms.
:::

::: {#exr-triangle-inequality-b2}
[B2: A distance that does not change]

Let \( z \in \nC \) with \( \abs{z} = 1 \). Prove that \( \abs{z - w} = \abs{1 - \conj{z}w} \) for every \( w \in \nC \). The first two steps are done:
\[
\begin{aligned}
\abs{z - w}^2 &= \abs{z}^2 - z\conj{w} - \conj{z}w + \abs{w}^2 , \\
\abs{1 - \conj{z}w}^2 &= 1 - z\conj{w} - \conj{z}w + \abs{z}^2\abs{w}^2 ,
\end{aligned}
\]
both by expanding \( u\conj{u} \) with @thm-conjugate-properties. *Name the move, then complete it.*
:::

::: {.solution}
The move is **square the modulus**: compare the squares, which are algebra, and take the non-negative square roots back.

Substitute \( \abs{z}^2 = 1 \) into both lines. The first becomes \( 1 - z\conj{w} - \conj{z}w + \abs{w}^2 \), and so does the second, since \( \abs{z}^2\abs{w}^2 = \abs{w}^2 \). So \( \abs{z - w}^2 = \abs{1 - \conj{z}w}^2 \). Both \( \abs{z - w} \) and \( \abs{1 - \conj{z}w} \) are non-negative, and non-negative reals with equal squares are equal (comparing squares). Hence \( \abs{z - w} = \abs{1 - \conj{z}w} \).

(For the record, the given lines. Conjugation respects differences: \( \conj{-v} = \conj{(-1)v} = \conj{-1}\,\conj{v} = -\conj{v} \) by @thm-conjugate-properties (b), @prp-modulus-of-real and @fd3:prp-ring-algebra (c), so with (a), \( \conj{u - v} = \conj{u} - \conj{v} \); and \( \conj{1} = 1 \) by @prp-modulus-of-real. Then \( (z - w)(\conj{z} - \conj{w}) = z\conj{z} - z\conj{w} - w\conj{z} + w\conj{w} \), and \( \conj{1 - \conj{z}w} = 1 - z\conj{w} \), so \( (1 - \conj{z}w)(1 - z\conj{w}) = 1 - z\conj{w} - \conj{z}w + (z\conj{z})(w\conj{w}) \).)
:::

::: {#exr-triangle-inequality-b3}
[B3]

Prove that \( \abs{z} \le \abs{\operatorname{Re} z} + \abs{\operatorname{Im} z} \le \sqrt 2 \, \abs{z} \) for every \( z \in \nC \), and, for each of the two inequalities, find a non-zero \( z \) for which it is an equality.
:::

::: {.solution}
The first inequality is the last part of @lem-real-part-at-most-modulus. For the second, write \( z = x + yi \). Both sides are non-negative (\( \sqrt 2 \ge 0 \) by @fd3:prp-cof-square-roots), so it suffices to compare squares. The right side squared is \( (\sqrt 2)^2 \abs{z}^2 = 2(x^2 + y^2) \), and the left side squared is \( x^2 + 2\abs{x}\abs{y} + y^2 \), using \( \abs{x}^2 = x^2 \) (@fd3:prp-absolute-value-ordered-field (b)). Their difference is
\[
\begin{aligned}
2(x^2 + y^2) - \bigl( x^2 + 2\abs{x}\abs{y} + y^2 \bigr) &= \abs{x}^2 - 2\abs{x}\abs{y} + \abs{y}^2 \\
&= \bigl( \abs{x} - \abs{y} \bigr)^2 \ge 0 ,
\end{aligned}
\]
a square in the ordered field \( \nR \) (@fd3:prp-ordered-ring-rules (e)). So \( (\abs{x} + \abs{y})^2 \le 2\abs{z}^2 \), and \( \abs{x} + \abs{y} \le \sqrt 2\,\abs{z} \).

Equality: \( z = 1 \) gives \( 1 = 1 + 0 \) in the first; \( z = 1 + i \) gives \( 1 + 1 = 2 = \sqrt 2 \cdot \sqrt 2 \) in the second.
:::

### C. Going deeper

::: {#exr-triangle-inequality-c1}
[C1: Exit check: the triangle inequality]

State and prove the triangle inequality for complex numbers. Your proof must include a proof that \( \operatorname{Re} u \le \abs{u} \) for every \( u \in \nC \).
:::

::: {.solution}
*Statement.* For all \( z, w \in \nC \), \( \abs{z + w} \le \abs{z} + \abs{w} \).

*The estimate.* Let \( u = x + yi \) with \( x, y \in \nR \). Then \( \abs{u}^2 = x^2 + y^2 \ge x^2 = \abs{x}^2 \), since \( y^2 \ge 0 \). Both \( \abs{x} \) and \( \abs{u} \) are non-negative, so \( \abs{x} \le \abs{u} \) by comparing squares (@fd3:prp-ordered-ring-rules (g) with trichotomy). Hence \( \operatorname{Re} u = x \le \abs{x} \le \abs{u} \) (@fd3:prp-absolute-value-ordered-field (c)).

*The inequality.* Let \( z, w \in \nC \). By @thm-conjugate-properties (a)–(c),
\[
\begin{aligned}
\abs{z + w}^2 &= (z + w)(\conj{z} + \conj{w}) = \abs{z}^2 + \bigl( z\conj{w} + \conj{z\conj{w}} \bigr) + \abs{w}^2 \\
&= \abs{z}^2 + 2\operatorname{Re}(z\conj{w}) + \abs{w}^2 .
\end{aligned}
\]
By the estimate and @thm-conjugate-properties (d), \( 2\operatorname{Re}(z\conj{w}) \le 2\abs{z\conj{w}} = 2\abs{z}\abs{w} \). Hence \( \abs{z + w}^2 \le (\abs{z} + \abs{w})^2 \). Both \( \abs{z + w} \) and \( \abs{z} + \abs{w} \) are non-negative, so comparing squares gives \( \abs{z + w} \le \abs{z} + \abs{w} \).

**Marking scheme.** (10 points)
- 2: proves \( \operatorname{Re} u \le \abs{u} \), with a reason for passing from squares to moduli.
- 3: expands \( \abs{z + w}^2 \) with conjugates and identifies the cross term as \( 2\operatorname{Re}(z\conj{w}) \), a real number.
- 2: bounds the cross term by \( 2\abs{z}\abs{w} \), citing \( \abs{z\conj{w}} = \abs{z}\abs{w} \).
- 1: concludes \( \abs{z + w}^2 \le (\abs{z} + \abs{w})^2 \).
- 2: takes square roots, justified by the non-negativity of both sides.
A second route, with coordinates \( z = a + bi \), \( w = c + di \): expanding \( (a + c)^2 + (b + d)^2 \) and isolating the cross term \( 2(ac + bd) \) earns the 3 points of the second line; proving \( ac + bd \le \abs{z}\abs{w} \), for instance from \( (ac + bd)^2 \le (a^2 + b^2)(c^2 + d^2) \), which follows from \( (ad - bc)^2 \ge 0 \), earns the 2 points of the third line if proved, not if quoted; the last two lines are marked as above. The 2 points for \( \operatorname{Re} u \le \abs{u} \) are still owed on that route, since the problem asks for it.
Fatal errors (0 for the step): writing \( z \le \abs{z} \) or any inequality between non-real complex numbers; dropping the conjugate, as in \( \abs{u}^2 = u^2 \).
:::

::: {#exr-triangle-inequality-c2}
[C2: Inside the unit disc]

Let \( z, w \in \nC \) with \( \abs{z} < 1 \) and \( \abs{w} < 1 \). Prove that \( \abs{z - w} < \abs{1 - \conj{z}w} \). Here is the start of a proof: square both sides and expand. *Name the move, then complete it.*
:::

::: {.solution}
The move is **square the modulus**. Both sides are non-negative, so it is enough to show \( \abs{z - w}^2 < \abs{1 - \conj{z}w}^2 \) (comparing squares, strict form: @fd3:prp-ordered-ring-rules (g)). Expanding each as \( u\conj{u} \), exactly as in @exr-triangle-inequality-b2,
\[
\begin{aligned}
\abs{z - w}^2 &= \abs{z}^2 - z\conj{w} - \conj{z}w + \abs{w}^2 , \\
\abs{1 - \conj{z}w}^2 &= 1 - z\conj{w} - \conj{z}w + \abs{z}^2\abs{w}^2 .
\end{aligned}
\]
The non-real terms cancel in the difference:
\[
\begin{aligned}
\abs{1 - \conj{z}w}^2 - \abs{z - w}^2 &= 1 - \abs{z}^2 - \abs{w}^2 + \abs{z}^2\abs{w}^2 \\
&= \bigl( 1 - \abs{z}^2 \bigr)\bigl( 1 - \abs{w}^2 \bigr) .
\end{aligned}
\]
Since \( 0 \le \abs{z} < 1 \), comparing squares gives \( \abs{z}^2 < 1^2 = 1 \), so \( 1 - \abs{z}^2 > 0 \); likewise \( 1 - \abs{w}^2 > 0 \). A product of two positive reals is positive ((O4)). So the difference is positive, \( \abs{z - w}^2 < \abs{1 - \conj{z}w}^2 \), and \( \abs{z - w} < \abs{1 - \conj{z}w} \).

In particular \( 1 - \conj{z}w \ne 0 \). Since \( \abs{1 - \conj{z}w} = \abs{1 - z\conj{w}} \) (a modulus is unchanged by conjugation, @thm-conjugate-properties (d)), the inequality says that \( \abs{z - w}/\abs{1 - \conj{w}z} < 1 \) for all \( z, w \) in the open unit disc: the map \( z \mapsto (z - w)/(1 - \conj{w}z) \) sends the open unit disc into itself, a fact complex analysis builds on.

**Marking scheme.** (10 points)
- 2: reduces to the squared inequality, with the non-negativity of both sides as the reason.
- 3: expands both squares with conjugates.
- 3: factors the difference as \( (1 - \abs{z}^2)(1 - \abs{w}^2) \).
- 2: shows both factors positive, from \( \abs{z}, \abs{w} < 1 \), and concludes strictly.
Fatal errors (0 for the step): expanding \( \abs{z - w}^2 \) as \( (z - w)^2 \); comparing \( z\conj{w} \) with a real number.
:::

<!-- dependency ledger
thm-complex-triangle-inequality (claim): |z - w| is the distance between the points z and w of the plane, by Pythagoras | picture only; no proof uses it
lem-real-part-at-most-modulus (claim): comparing squares, for p, q >= 0 in R, p <= q iff p^2 <= q^2, and p = q iff p^2 = q^2 | fd3:prp-ordered-ring-rules (g) with (O1) of fd3:def-ordered-ring-and-field; inline
lem-real-part-at-most-modulus (proof): |u|^2 = x^2 + y^2 and |u| >= 0 for u = x + yi | def-conjugate-modulus with fd3:prp-cof-square-roots (the root squares back)
lem-real-part-at-most-modulus (proof): a product of non-negative reals is non-negative; 2 > 0 in R | (O4) of fd3:def-ordered-ring-and-field, fd3:prp-ring-algebra (b) for a zero factor; fd3:prp-ordered-ring-rules (b), (e); inline
thm-complex-triangle-inequality (proof): Re of a complex number and |z|, |w| are reals, and sums and products of reals agree in C and R, so the displayed inequalities are in the ordered field R | fd3:thm-reals-complete-ordered-field (R is an ordered field); prp-reals-embed-complex, cited
thm-complex-triangle-inequality (proof): doubling Re(z conj w) <= |z||w| as a + a, 2a = (1 + 1)a = a + a | fd3:prp-ordered-ring-rules (b); distributivity (F9) in R; inline
thm-complex-triangle-inequality (proof): (z + w)(conj z + conj w) expands into four terms | prp-complex-arithmetic-laws (a)-(c) (distributivity, commutativity, associativity), cited
thm-complex-triangle-inequality (claim): pointer to the linear algebra volumes (inner product spaces, same route) | prose comparison; nothing depends on it
cor-complex-triangle-variants (proof): w - z = (-1)(z - w); z - (-w) = z + w | fd3:prp-ring-algebra (a), (c) in the commutative ring C (prp-complex-arithmetic-laws)
cor-complex-triangle-variants (proof): from -t <= |z - w| to -|z - w| <= t, both cases | fd3:prp-ordered-ring-rules (a) with -(-t) = t, fd3:prp-ring-algebra (a), cited
cor-complex-triangle-variants (proof): finite sums in C by appending the last term; induction from n = 1 | fd2:def-sum-product used as a template (its recursion uses only fd2:thm-recursion and the operations of C); fd1:ax-induction through fd3:cor-omega-identification (b), on m = n - 1
cor-complex-triangle-variants (claim): *Algebraic Preliminaries*, Chapter 5 uses (b) and (c) for polynomial growth | prose pointer (F5.5, lem-complex-polynomial-growth); nothing depends on it
cor-complex-triangle-variants (example): quick check values |5 - 3i| = |5 + 3i| = sqrt 34, 2 <= sqrt 34 | inline; verify/ch01/cor-complex-triangle-variants.py
thm-complex-triangle-inequality (example): quick check |3 + 4i| + |-3 + 4i| = 10, |8i| = 8; warning (2i)^2 = -4, |2i|^2 = 4 | inline; verify/ch01/thm-complex-triangle-inequality.py
lem-real-part-at-most-modulus (example): values for 3 - 4i, 2, -1, 2i | inline; verify/ch01/lem-real-part-at-most-modulus.py
exr-triangle-inequality-a1 (solution): cross term 0, 25 <= 49 for z = 3, w = 4i | verify/ch01/exr-triangle-inequality-a1.py
exr-triangle-inequality-b1 (solution): x = |u| iff y = 0 and x >= 0; (1 + i)(2 - 2i) = 4, |3 + 3i| = 3 sqrt 2 | fd3:prp-ordered-ring-rules (e), fd3:prp-cof-square-roots, cited; verify/ch01/exr-triangle-inequality-b1.py
exr-triangle-inequality-b1 (solution): pointer to the n-term equality case in the linear algebra volumes | prose comparison; nothing depends on it
exr-triangle-inequality-b2 (solution): the two expansions; conj(u - v) = conj u - conj v; conj(1) = 1; conj(1 - conj(z) w) = 1 - z conj(w) | thm-conjugate-properties (a)-(c), prp-modulus-of-real, fd3:prp-ring-algebra (c) in C, cited; verify/ch01/exr-triangle-inequality-b2.py
exr-triangle-inequality-b3 (solution): (sqrt 2)^2 = 2, sqrt 2 >= 0; 2(x^2 + y^2) - (|x| + |y|)^2 = (|x| - |y|)^2 | fd3:prp-cof-square-roots; inline; verify/ch01/exr-triangle-inequality-b3.py
exr-triangle-inequality-c2 (solution): 1 - |z|^2 - |w|^2 + |z|^2|w|^2 = (1 - |z|^2)(1 - |w|^2) | inline; verify/ch01/exr-triangle-inequality-c2.py
exr-triangle-inequality-c2 (solution): the disc map remark | prose only; nothing depends on it
-->
