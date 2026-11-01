# The Dot Product

Section 9.2 gave \( \nR^n \) two operations, adding points and scaling them, and both produce points. Nothing so far measures anything: there is no length, no distance and no right angle. This section introduces one more operation, which takes two points and returns a **number**, and proves the rules it obeys. Length, distance and angle are built from it in the rest of the chapter.

## A product that is a number

Start with the plane. By Pythagoras, the point \( (x_1, x_2) \) lies at distance \( \sqrt{x_1^2 + x_2^2} \) from the origin, and Chapter 3 gave this number a name: it is the modulus \( \abs{x_1 + x_2 i} \) of @def-conjugate-modulus. Pythagoras is the motivation here, not a reason; nothing below rests on a picture.

Look at the expression under the root. It is a sum of products of coordinates, each coordinate multiplied by itself:
\[
x_1^2 + x_2^2 = x_1 x_1 + x_2 x_2 .
\]
Take this apart for two points: keep the first factor of each product from \( x \) and take the second from another point \( y \). The result \( x_1 y_1 + x_2 y_2 \) still makes sense, in \( \nR^n \) for every \( n \), and it is a real number, not a point. The squared length is the special case \( y = x \).

*Multiply coordinate by coordinate, then add.*

::: {#def-dot-product-rn}
[Dot Product]

Let \( n \ge 1 \). The **dot product** of \( x = (x_1, \dots, x_n) \) and \( y = (y_1, \dots, y_n) \) in \( \nR^n \) is the real number
\[
\inner{x}{y} \coloneqq \sum_{k=1}^{n} x_k y_k = x_1 y_1 + \dots + x_n y_n .
\]
:::

In words: pair the coordinates place by place, multiply each pair in \( \nR \), and add the \( n \) products. The two inputs must lie in the **same** \( \nR^n \); for \( x \in \nR^2 \) and \( y \in \nR^3 \) the dot product is not defined. Many books write \( x \cdot y \); this book always writes \( \inner{x}{y} \), with two slots and a comma, so that the product of two points is never confused with the scalar multiple \( cx \) of Section 9.2. The sum is the finite sum of @fd2:def-sum-product; nothing needs checking for well-definedness, since the coordinates of \( x \) and \( y \) are determined by the points (@def-real-n-space).

**Examples.**

*In the plane.* \( \inner{(1, 2)}{(3, 4)} = 1 \cdot 3 + 2 \cdot 4 = 11 \), and \( \inner{(3, 4)}{(3, 4)} = 9 + 16 = 25 \), the square of the modulus \( \abs{3 + 4i} = 5 \) of Chapter 3.

*Signs.* \( \inner{(1, 2)}{(-2, 1)} = -2 + 2 = 0 \), and \( \inner{(1, 0)}{(-1, 0)} = -1 \). The dot product can be zero or negative even when neither point is \( 0 \).

*The degenerate case \( n = 1 \).* A sum with one term is that term (\( \sum_{k=1}^{1} a_k = 0 + a_1 = a_1 \)), so for \( x, y \in \nR = \nR^1 \) the dot product is the ordinary product: \( \inner{x}{y} = xy \). This is why the definition deserves the name *product*. It also explains why the dot product of a point with itself can only be \( \ge 0 \): on the line it is \( x^2 \).

**A non-example by minimal change.** On \( \nR^2 \), try \( [x, y] \coloneqq x_1 y_1 - x_2 y_2 \), with one sign changed. It is still symmetric and still respects sums and scalar multiples in each slot, so it passes parts (a) and (b) of the next proposition. Part (c) fails: \( [e_2, e_2] = -1 < 0 \), and \( [(1, 1), (1, 1)] = 0 \) although \( (1, 1) \ne 0 \). So this bracket cannot be the square of a length. The plus signs of the definition are what make \( \inner{x}{x} \) a sum of squares.

**Why this definition.** Two features are deliberate. First, the output is a number. A product returning a point, such as the coordinatewise product \( (x_1 y_1, \dots, x_n y_n) \), would not measure anything, and Section 9.2's warning already set products of points aside: in this chapter \( (1, 2)(3, 4) \) has no meaning. Second, the dot product of a point with itself is \( \sum_k x_k^2 \), the expression under Pythagoras' root. That is exactly what Section 9.4 needs to define length.

## The laws of the dot product

Every law below reduces, term by term, to a law of \( \nR \). The tool for collecting the terms afterwards is the set of sum rules @lem-ring-finite-sums, with the comparison rules @prp-sum-order of Chapter 1 for the order facts.

Those rules are stated for sums indexed from \( 0 \), while ours run from \( 1 \) to \( n \). Shifting the index (the remark after @fd2:def-sum-product, with \( p = -1 \)) gives
\[
\sum_{k=1}^{n} a_k = \sum_{k=0}^{n-1} a_{k+1} ,
\]
and \( n - 1 \in \nN \) because \( n \ge 1 \). So each rule holds for sums from \( 1 \) to \( n \) as well, and we apply it in that form without repeating the shift.

The proposition lists the laws in the order in which later sections use them.

::: {#prp-dot-product-laws-rn}
[Laws of the Dot Product]

Let \( n \ge 1 \), let \( x, y, z \in \nR^n \) and \( c \in \nR \), and let \( e_1, \dots, e_n \) be the standard vectors (@def-standard-basis-rn).

::: {.enumerate options="label=(\alph*)"}
1. *(Symmetry.)* \( \inner{x}{y} = \inner{y}{x} \).
2. *(Linearity in each slot.)* \( \inner{x + y}{z} = \inner{x}{z} + \inner{y}{z} \) and \( \inner{cx}{z} = c\inner{x}{z} \); and likewise in the second slot, \( \inner{z}{x + y} = \inner{z}{x} + \inner{z}{y} \) and \( \inner{z}{cx} = c\inner{z}{x} \).
3. *(Positivity.)* \( \inner{x}{x} = \sum_{k=1}^{n} x_k^2 \ge 0 \), and \( \inner{x}{x} = 0 \) **if and only if** \( x = 0 \).
4. *(Standard vectors.)* \( \inner{x}{e_k} = x_k \) for every \( k \), and \( \inner{e_j}{e_k} = 1 \) if \( j = k \), \( \inner{e_j}{e_k} = 0 \) if \( j \ne k \).
5. *(Zero.)* \( \inner{x}{0} = \inner{0}{x} = 0 \).
:::
:::

::: {.idea}
This is the move of @exm-method-coordinatewise, one level up: write out each side as a sum over \( k \), apply the law of \( \nR \) to the \( k \)-th term, and let the sum rules collect the terms. Part (c) is the one law with content: a sum of squares in \( \nR \) is \( \ge 0 \) and vanishes only when every square does.
:::

::: {.proof}
Throughout, \( \inner{x}{y} = \sum_{k=1}^{n} x_k y_k \) by @def-dot-product-rn, and the coordinates of \( x + y \) and \( cx \) are \( x_k + y_k \) and \( c x_k \) (@def-vector-operations-rn).

(a) Each term satisfies \( x_k y_k = y_k x_k \) by (F5) of @fd3:def-commutative-ring-and-field, so the two sums have the same terms and are equal.

(b) For sums, (F9) with (F5) gives \( (x_k + y_k) z_k = x_k z_k + y_k z_k \) for each \( k \), so
\[
\inner{x + y}{z} = \sum_{k=1}^{n} (x_k z_k + y_k z_k) = \sum_{k=1}^{n} x_k z_k + \sum_{k=1}^{n} y_k z_k ,
\]
by @lem-ring-finite-sums (a). For scalars, \( (c x_k) z_k = c (x_k z_k) \) by (F6), and \( \sum_k c (x_k z_k) = c \sum_k x_k z_k \) by @lem-ring-finite-sums (b). The second-slot rules follow from the first-slot rules and (a): \( \inner{z}{x + y} = \inner{x + y}{z} = \inner{x}{z} + \inner{y}{z} = \inner{z}{x} + \inner{z}{y} \), and in the same way \( \inner{z}{cx} = c\inner{z}{x} \).

(e) By @prp-vector-space-laws-rn (i), \( 0 = 0 \cdot 0 \), the scalar \( 0 \) times the zero vector. So (b) gives \( \inner{0}{x} = \inner{0 \cdot 0}{x} = 0 \cdot \inner{0}{x} = 0 \), using \( a \cdot 0 = 0 \) in \( \nR \) (@fd3:prp-ring-algebra (b)); and \( \inner{x}{0} = \inner{0}{x} \) by (a). We prove (e) before (c), which uses it.

(c) Here \( x_k y_k \) with \( y = x \) is \( x_k x_k = x_k^2 \), which gives the formula. Each term is \( \ge 0 \): if \( x_k \ne 0 \), then \( x_k^2 > 0 \) by @fd3:prp-ordered-ring-rules (e); if \( x_k = 0 \), then \( x_k^2 = 0 \) by @fd3:prp-ring-algebra (b). A sum of non-negative terms is non-negative (@prp-sum-order (b) with \( m = -1 \), the empty sum being \( 0 \)), so \( \inner{x}{x} \ge 0 \).

\( (\Leftarrow) \) If \( x = 0 \), then \( \inner{x}{x} = \inner{0}{0} = 0 \) by (e).

\( (\Rightarrow) \) Suppose \( \inner{x}{x} = 0 \). This is a sum of non-negative terms equal to \( 0 \), so every term is \( 0 \) (@prp-sum-order (e)): \( x_k x_k = 0 \) for each \( k \). Then \( x_k = 0 \) by @fd3:prp-ordered-ring-rules (f). Since every coordinate of \( x \) is \( 0 \), \( x = 0 \) (equality of tuples, @def-real-n-space).

(d) Fix \( k \). The \( j \)-th coordinate of \( e_k \) is \( 1 \) if \( j = k \) and \( 0 \) otherwise (@def-standard-basis-rn). So the terms of \( \inner{x}{e_k} = \sum_{j=1}^{n} x_j (e_k)_j \) are \( x_j \cdot 0 = 0 \) for \( j \ne k \) and \( x_k \cdot 1 = x_k \) for \( j = k \). A sum with one non-zero term is that term (@lem-ring-finite-sums (d)), so \( \inner{x}{e_k} = x_k \). Taking \( x = e_j \) gives \( \inner{e_j}{e_k} = (e_j)_k \), which is \( 1 \) if \( j = k \) and \( 0 \) otherwise. This proves the proposition.
:::

Part (d) says that the dot product with \( e_k \) **reads off** the \( k \)-th coordinate; we use it whenever a coordinate has to be recovered from dot products. Part (c) is what will make length meaningful in Section 9.4: \( \inner{x}{x} \) has a square root, and only the zero vector has length \( 0 \).

One consequence of (a) and (b) is used constantly from the next section on: a dot product of sums can be multiplied out like a product of numbers. For \( x, y \in \nR^n \),
\[
\begin{aligned}
\inner{x + y}{x + y} &= \inner{x}{x + y} + \inner{y}{x + y} \\
&= \inner{x}{x} + \inner{x}{y} + \inner{y}{x} + \inner{y}{y} \\
&= \inner{x}{x} + 2\inner{x}{y} + \inner{y}{y} .
\end{aligned}
\]
The first line is linearity in the first slot, the second is linearity in the second slot, and the third is symmetry, \( \inner{y}{x} = \inner{x}{y} \), with \( a + a = 2a \) in \( \nR \). Replacing \( y \) by \( -y = (-1)y \) changes the middle term only: by (b), \( \inner{x}{-y} = -\inner{x}{y} \) and \( \inner{-y}{-y} = (-1)^2 \inner{y}{y} = \inner{y}{y} \), so
\[
\inner{x - y}{x - y} = \inner{x}{x} - 2\inner{x}{y} + \inner{y}{y} .
\]
These two expansions are the dot-product form of \( (a \pm b)^2 = a^2 \pm 2ab + b^2 \) (@fd3:prp-ring-algebra (d)), and the middle term \( 2\inner{x}{y} \) is the one that matters.

## Orthogonal vectors

The expansion just displayed says when the plane's Pythagorean relation holds for the triangle with sides \( x \), \( y \) and \( x + y \): the dot product of \( x + y \) with itself is the sum \( \inner{x}{x} + \inner{y}{y} \) **exactly when** \( 2\inner{x}{y} = 0 \), that is, when \( \inner{x}{y} = 0 \) (as \( 2 \ne 0 \) in \( \nR \)). In the plane we see the same thing: the points \( (1, 2) \) and \( (-2, 1) \) look perpendicular, since the second is the first turned a quarter turn about the origin, and their dot product is \( -2 + 2 = 0 \). So "dot product zero" is the condition that does the job of a right angle, and it makes sense in every \( \nR^n \), where there is no picture to consult.

*Two vectors are orthogonal when their dot product is zero.*

::: {#def-orthogonal-rn}
[Orthogonal Vectors]

Let \( n \ge 1 \). Vectors \( x, y \in \nR^n \) are **orthogonal**, written \( x \perp y \), if \( \inner{x}{y} = 0 \).
:::

In words: one number, the dot product, must vanish. The relation is symmetric, \( x \perp y \) if and only if \( y \perp x \), by @prp-dot-product-laws-rn (a), so "\( x \) and \( y \) are orthogonal" is unambiguous. "Perpendicular" is another word for it; we keep "orthogonal" because it is the word the linear algebra volumes use.

**Examples.**

*Standard vectors.* \( e_j \perp e_k \) whenever \( j \ne k \), by @prp-dot-product-laws-rn (d).

*In \( \nR^3 \).* \( (1, 1, 0) \perp (1, -1, 5) \), since \( 1 - 1 + 0 = 0 \). The third coordinate of the second vector is irrelevant because the first vector's third coordinate is \( 0 \).

*The degenerate case.* \( 0 \perp x \) for **every** \( x \), by @prp-dot-product-laws-rn (e). This matters: the zero vector is orthogonal to everything, including itself, so "orthogonal" does not mean "pointing in different directions". And \( 0 \) is the **only** vector orthogonal to itself: \( x \perp x \) means \( \inner{x}{x} = 0 \), which forces \( x = 0 \) by @prp-dot-product-laws-rn (c).

**Non-example by minimal change.** Change \( (-2, 1) \) to \( (-2, 2) \): then \( \inner{(1, 2)}{(-2, 2)} = -2 + 4 = 2 \ne 0 \), so \( (1, 2) \) and \( (-2, 2) \) are not orthogonal. The single clause \( \inner{x}{y} = 0 \) fails, by \( 2 \).

**Why this definition.** We could have defined a right angle by a picture, or by the Pythagorean relation itself. The dot product is better: it is one equation, linear in each vector, so orthogonality to a fixed \( a \) is the solution set of \( \inner{a}{x} = 0 \), an equation in the coordinates of \( x \). Chapter 10 builds its hyperplanes from equations of exactly this form.

The test below turns orthogonality into a tool for proving vectors **equal**. A vector orthogonal to everything is zero, and two vectors with the same dot products are the same vector.

::: {#prp-orthogonal-test-rn}
[The Orthogonality Test]

Let \( n \ge 1 \) and \( x, y \in \nR^n \).

::: {.enumerate options="label=(\alph*)"}
1. If \( \inner{x}{z} = 0 \) for **every** \( z \in \nR^n \), then \( x = 0 \).
2. The following are equivalent: (i) \( x = y \); (ii) \( \inner{x}{z} = \inner{y}{z} \) for every \( z \in \nR^n \); (iii) \( \inner{x}{e_k} = \inner{y}{e_k} \) for every \( k \in \{1, \dots, n\} \).
:::
:::

::: {.proof}
(a) The hypothesis holds for every \( z \), in particular for \( z = x \). So \( \inner{x}{x} = 0 \), and \( x = 0 \) by @prp-dot-product-laws-rn (c).

(b) (i) \( \Rightarrow \) (ii): equal vectors have equal dot products with every \( z \). (ii) \( \Rightarrow \) (iii): take \( z = e_k \). (iii) \( \Rightarrow \) (i): by @prp-dot-product-laws-rn (d), (iii) says \( x_k = y_k \) for every \( k \), and tuples that agree in every place are equal (@def-real-n-space).
:::

The hypothesis of (a) is a "for every \( z \)" statement, and the proof uses it once, at the one vector that settles the question. Choosing \( z = e_1 \) instead would give only \( x_1 = 0 \); C1 below examines that mistake.

::: {#exm-dot-products-computed}
[Dot products and orthogonality computed]

(a) Compute \( \inner{(1, 2, -1)}{(3, 0, 4)} \). (b) Show that \( (1, 1, 1, 1) \perp (1, -1, 1, -1) \) in \( \nR^4 \). (c) Find all \( x \in \nR^2 \) with \( x \perp (1, 1) \). (d) In \( \nR^3 \), when is \( x \perp e_3 \)?
:::

::: {.solution}
(a) \( 1 \cdot 3 + 2 \cdot 0 + (-1) \cdot 4 = 3 + 0 - 4 = -1 \).

(b) \( 1 - 1 + 1 - 1 = 0 \), so the two vectors are orthogonal. Neither is \( 0 \), and no coordinate of either is \( 0 \): orthogonality comes from cancellation between terms, not from zero entries.

(c) \( x \perp (1, 1) \) means \( x_1 + x_2 = 0 \). We show that the solutions are exactly the vectors \( t(1, -1) \) with \( t \in \nR \). \( (\subseteq) \) If \( x_1 + x_2 = 0 \), then \( x_2 = -x_1 \), so \( x = (x_1, -x_1) = x_1 (1, -1) \); take \( t = x_1 \). \( (\supseteq) \) \( \inner{t(1, -1)}{(1, 1)} = t(1 - 1) = 0 \) by @prp-dot-product-laws-rn (b). So the vectors orthogonal to \( (1, 1) \) are the multiples of \( (1, -1) \), and only those.

(d) By @prp-dot-product-laws-rn (d), \( \inner{x}{e_3} = x_3 \). So \( x \perp e_3 \) if and only if \( x_3 = 0 \): the vectors orthogonal to \( e_3 \) are those of the form \( (x_1, x_2, 0) \).
:::

In part (c) the vectors orthogonal to the non-zero vector \( (1, 1) \) are the multiples of one vector. In \( \nR^n \), the solutions of one equation \( \inner{a}{x} = c \) with \( a \ne 0 \) are what Chapter 10 calls a hyperplane.

::: {.warning}
The dot product does not obey every law of multiplication in \( \nR \). **There is no cancellation:** \( \inner{e_1}{e_2} = \inner{e_1}{2e_2} = 0 \), yet \( e_2 \ne 2e_2 \). **There is no associativity:** \( \inner{x}{y} z \) and \( \inner{y}{z} x \) are both defined, but for \( x = y = e_1 \) and \( z = e_2 \) the first is \( 1 \cdot e_2 = e_2 \) and the second is \( 0 \cdot e_1 = 0 \). And **\( \inner{x}{y} = 0 \) does not force a zero factor:** \( e_1 \) and \( e_2 \) are both non-zero. What does hold is @prp-orthogonal-test-rn: cancellation is allowed when the equation holds for **every** \( z \).
:::

::: {.check}
Is \( (2, -1, 3) \perp (1, 5, 1) \)? What is \( \inner{x}{x} \) for \( x = (1, -2, 0, 3) \)?
:::

::: {.solution}
Yes: \( 2 - 5 + 3 = 0 \). And \( \inner{x}{x} = 1 + 4 + 0 + 9 = 14 \), a sum of squares, as @prp-dot-product-laws-rn (c) says it must be.
:::

## Exercises

### A. Check your understanding

:::: {#exr-dot-product-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \inner{(1, -2, 0, 3)}{(4, 1, 7, -1)} \).
2. True or false for all \( x, y \in \nR^n \), with a reason: \( \inner{2x}{2y} = 2\inner{x}{y} \).
3. True or false for all \( x \in \nR^n \), with a reason: if \( \inner{x}{x} = 0 \), then \( x = 0 \).
4. True or false for all \( x, y \in \nR^n \), with a reason: if \( \inner{x}{y} = 0 \), then \( x = 0 \) or \( y = 0 \).
:::
::::

::: {.solution}
(a) \( 4 - 2 + 0 - 3 = -1 \).

(b) False. By @prp-dot-product-laws-rn (b) in each slot, \( \inner{2x}{2y} = 2\inner{x}{2y} = 4\inner{x}{y} \). For \( x = y = e_1 \) the left side is \( 4 \) and \( 2\inner{x}{y} = 2 \).

(c) True: this is the "only if" half of @prp-dot-product-laws-rn (c).

(d) False when \( n \ge 2 \): \( \inner{e_1}{e_2} = 0 \), and neither vector is \( 0 \). (For \( n = 1 \) the statement is true, since \( \inner{x}{y} = xy \) and \( \nR \) has no zero divisors.)
:::

### B. Practice

::: {#exr-dot-product-b1}
[B1: Orthogonal to two vectors]

Find all \( x \in \nR^3 \) that are orthogonal to both \( (1, 1, 0) \) and \( (0, 1, 1) \).
:::

::: {.solution}
The conditions are \( x_1 + x_2 = 0 \) and \( x_2 + x_3 = 0 \). We show that the solutions are exactly the vectors \( t(1, -1, 1) \), \( t \in \nR \).

\( (\subseteq) \) If both hold, put \( t \coloneqq x_1 \). Then \( x_2 = -x_1 = -t \) and \( x_3 = -x_2 = t \), so \( x = (t, -t, t) = t(1, -1, 1) \).

\( (\supseteq) \) By @prp-dot-product-laws-rn (b), \( \inner{t(1, -1, 1)}{(1, 1, 0)} = t(1 - 1 + 0) = 0 \) and \( \inner{t(1, -1, 1)}{(0, 1, 1)} = t(0 - 1 + 1) = 0 \).

Hence the vectors orthogonal to both are the multiples of \( (1, -1, 1) \).
:::

::: {#exr-dot-product-b2}
[B2: The difference of squares]

Prove that \( \inner{x - y}{x + y} = \inner{x}{x} - \inner{y}{y} \) for all \( x, y \in \nR^n \), naming the law used at each step. Deduce that \( \inner{x}{x} = \inner{y}{y} \) if and only if \( x - y \perp x + y \).
:::

::: {.solution}
Write \( x - y = x + (-1)y \) (@def-vector-operations-rn). By linearity in the first slot (@prp-dot-product-laws-rn (b)),
\[
\inner{x - y}{x + y} = \inner{x}{x + y} - \inner{y}{x + y} .
\]
By linearity in the second slot, this is
\[
\inner{x}{x} + \inner{x}{y} - \inner{y}{x} - \inner{y}{y} .
\]
By symmetry (@prp-dot-product-laws-rn (a)), \( \inner{y}{x} = \inner{x}{y} \), so the two middle terms cancel in \( \nR \), leaving \( \inner{x}{x} - \inner{y}{y} \).

For the deduction: \( x - y \perp x + y \) means \( \inner{x - y}{x + y} = 0 \) (@def-orthogonal-rn), which by the identity means \( \inner{x}{x} - \inner{y}{y} = 0 \), that is, \( \inner{x}{x} = \inner{y}{y} \). Each step is an equivalence, so both directions hold.

In the plane this says that the diagonals \( x + y \) and \( x - y \) of the parallelogram on \( x \) and \( y \) are orthogonal exactly when the two sides have equal "squared length".
:::

::: {#exr-dot-product-b3}
[B3: Solving one linear equation]

Let \( a \in \nR^n \) with \( a \ne 0 \), and let \( r \in \nR \). Show that \( x \coloneqq \dfrac{r}{\inner{a}{a}}\, a \) satisfies \( \inner{a}{x} = r \), and that it is the only solution of \( \inner{a}{x} = r \) that is parallel to \( a \).
:::

::: {.solution}
*The division is allowed.* Since \( a \ne 0 \), \( \inner{a}{a} \ne 0 \) by @prp-dot-product-laws-rn (c), and \( \inner{a}{a} \ge 0 \), so \( \inner{a}{a} > 0 \).

*Existence.* By linearity in the second slot, \( \inner{a}{x} = \dfrac{r}{\inner{a}{a}} \inner{a}{a} = r \).

*Uniqueness among vectors parallel to \( a \).* Let \( w \) be parallel to \( a \) with \( \inner{a}{w} = r \). Since \( a \ne 0 \), \( w = ta \) for some \( t \in \nR \) (the remark after @def-parallel-rn). Then \( r = \inner{a}{ta} = t\inner{a}{a} \), so \( t = r/\inner{a}{a} \) and \( w = x \).

For \( n \ge 2 \) there are other solutions, not parallel to \( a \). Choose \( k \) with \( a_k \ne 0 \) and \( j \ne k \), and let \( v \coloneqq a_k e_j - a_j e_k \). Then \( \inner{a}{v} = a_k a_j - a_j a_k = 0 \) by @prp-dot-product-laws-rn (b), (d), and \( v \ne 0 \) because its \( j \)-th coordinate is \( a_k \ne 0 \). So \( \inner{a}{x + v} = r + 0 = r \). If \( x + v \) were parallel to \( a \), it would equal \( x \) by uniqueness, giving \( v = 0 \). For example, with \( a = (1, 1) \) and \( r = 2 \): \( x = (1, 1) \), and \( (2, 0) \) is another solution.
:::

### C. Going deeper

::: {#exr-dot-product-c1}
[C1: Find the error]

Here is an argument.

> **Claim.** Let \( x \in \nR^n \). If \( \inner{x}{z} = 0 \) for every \( z \in \nR^n \), then \( x = 0 \).
>
> **Proof.** Take \( z = e_1 \). Then \( 0 = \inner{x}{e_1} = x_1 \). Hence \( x = 0 \).

Is the claim true? Does the argument prove it? If not, name the line that fails and what is wrong with it, and repair the argument.
:::

::: {.solution}
*The conclusion is true*: it is @prp-orthogonal-test-rn (a).

*The argument does not prove it.* The first two lines are correct: \( z = e_1 \) is a legal instance of the hypothesis, and \( \inner{x}{e_1} = x_1 \) by @prp-dot-product-laws-rn (d). The failing line is "Hence \( x = 0 \)". To show \( x = 0 \) we must show \( x_k = 0 \) for **every** \( k \), and the argument checks one coordinate and concludes for all of them. That is (N1) of @fd1:exm-not-allowed-catalogue: verifying instances and concluding "for all".

*A counterexample to the step* (not to the claim, which is true): in \( \nR^2 \), the vector \( x = e_2 = (0, 1) \) has \( x_1 = 0 \), yet \( x \ne 0 \). So "\( x_1 = 0 \), hence \( x = 0 \)" leads from a true line to a false one.

*Repair.* Either take \( z = x \): then \( \inner{x}{x} = 0 \), and \( x = 0 \) by @prp-dot-product-laws-rn (c). Or take \( z = e_k \) for **each** \( k \in \{1, \dots, n\} \), which gives \( x_k = 0 \) for every \( k \), and conclude by equality of tuples.

For \( n = 1 \) the step happens to be valid, since \( x_1 \) is the only coordinate; the argument is wrong because it is written for every \( n \).
:::

<!-- dependency ledger
def-dot-product-rn (claim): hook: distance in the plane is sqrt(x_1^2 + x_2^2) by Pythagoras | motivation only, flagged in the text as not a reason; modulus from def-conjugate-modulus (cited)
def-dot-product-rn (example): <(1,2),(3,4)> = 11, <(3,4),(3,4)> = 25 = |3 + 4i|^2, <(1,2),(-2,1)> = 0, <(1,0),(-1,0)> = -1 | arithmetic; verify/ch09/def-dot-product-rn.py
def-dot-product-rn (example): a sum with one term is that term, sum_{k=1}^{1} a_k = 0 + a_1 = a_1 | fd2:def-sum-product (cited), (F3)
def-dot-product-rn (claim): the bracket x_1y_1 - x_2y_2 is symmetric and linear in each slot; [e_2, e_2] = -1, [(1,1),(1,1)] = 0 | inline by the field laws; verify/ch09/def-dot-product-rn.py
prp-dot-product-laws-rn (proof): sum rules for sums indexed 1..n via the shift sum_{k=1}^{n} a_k = sum_{k=0}^{n-1} a_{k+1} (n - 1 in N since n >= 1) | fd2:def-sum-product, remark "Shifting the index" with p = -1 (cited); applied to lem-ring-finite-sums and prp-sum-order
prp-dot-product-laws-rn (proof): prp-sum-order (b) with m = -1 and (e): a sum of non-negative terms is >= 0, and = 0 only if every term is 0 | ch01 (promised): merged-ch01-f46.md, prp-sum-order (b), (e) (answers this chapter's request lem-nonnegative-sum-zero)
prp-dot-product-laws-rn (proof): lem-ring-finite-sums (a), (b), (d) | cited; now in fd4/src/ch04-fields/06-frobenius-and-fermat.md, moving to Chapter 1 under merged-ch01-f46.md (label unchanged)
prp-dot-product-laws-rn (proof): coordinates of e_k: (e_k)_j = 1 if j = k, 0 otherwise | def-standard-basis-rn (cited; ch09 §02)
prp-dot-product-laws-rn (proof): 0 = 0 * 0 (scalar zero times zero vector) | prp-vector-space-laws-rn (i) (cited; ch09 §02)
prp-dot-product-laws-rn (proof): x_j * 0 = 0, x_k * 1 = x_k in R | fd3:prp-ring-algebra (b), (F7) of fd3:def-commutative-ring-and-field
prp-dot-product-laws-rn (claim): expansion of <x +- y, x +- y>; a + a = 2a; (-1)^2 = 1 | prp-dot-product-laws-rn (a), (b) (cited); fd3:prp-ring-algebra (c), (F9) with 2 = 1 + 1; inline
def-orthogonal-rn (claim): 2 != 0 in R, so 2t = 0 iff t = 0 | fd3:prp-ordered-ring-rules (h) (2 = 2 * 1 > 0) and (f); inline
def-orthogonal-rn (claim): (1,2), (-2,1) "look perpendicular" (quarter turn) | motivation only, no proof uses it
def-orthogonal-rn (example): (1,1,0) . (1,-1,5) = 0; (1,2) . (-2,2) = 2 | arithmetic; verify/ch09/def-orthogonal-rn.py
def-orthogonal-rn (claim): pointer to Chapter 10 (hyperplanes from equations <a, x> = c) | prose pointer; nothing depends on it
exm-dot-products-computed (solution): -1; 0; x perp (1,1) iff x = t(1,-1); x perp e_3 iff x_3 = 0 | verify/ch09/exm-dot-products-computed.py
exm-dot-products-computed (claim): pointer to Chapter 10 (orthogonal complement of one vector as one equation) | prose pointer; nothing depends on it
exm-dot-products-computed (example): the Quick check after the warning: (2,-1,3) . (1,5,1) = 0; <x, x> = 14 for (1,-2,0,3) | verify/ch09/exm-dot-products-computed.py
exm-dot-products-computed (example): warning: <e1,e1> e2 = e2, <e1,e2> e1 = 0 | prp-dot-product-laws-rn (d), prp-vector-space-laws-rn (i) (cited); inline
exr-dot-product-a1 (solution): -1; <2x, 2y> = 4<x, y>; n = 1 case: R has no zero divisors | verify/ch09/exr-dot-product-a1.py; fd3:prp-ordered-ring-rules (f)
exr-dot-product-b1 (solution): x = t(1,-1,1) | verify/ch09/exr-dot-product-b1.py
exr-dot-product-b3 (solution): a vector parallel to a != 0 is ta | the remark after def-parallel-rn (ch09 §02, stated and proved in the text there)
exr-dot-product-b3 (solution): v = a_k e_j - a_j e_k has <a, v> = 0, v != 0; example a = (1,1), r = 2: x = (1,1), (2,0) | verify/ch09/exr-dot-product-b3.py
exr-dot-product-c1 (solution): (N1) | fd1:exm-not-allowed-catalogue (cited)
-->
