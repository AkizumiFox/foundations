# Length and Distance

Section 9.3 attached a number to a pair of vectors, the dot product. Taken with itself, it gives \( \inner{x}{x} = x_1^2 + \dots + x_n^2 \), the square of the length that Pythagoras assigns to \( x \) in the plane. This section takes its square root and calls it the length of \( x \), defines the distance between two points, and checks that for \( n = 2 \) both agree with the modulus of Chapter 3. Lengths are awkward, since each is the root of a sum, while their squares are polynomials in the coordinates. So the section's method is to move to squares, compute there, and come back. It ends by comparing the length of \( x \) with the sizes of its coordinates, the comparison that analysis in several variables uses most often.

## Length

In the plane, the point \( x = (x_1, x_2) \) is the far corner of a right triangle with legs \( \abs{x_1} \) and \( \abs{x_2} \). By Pythagoras its distance from the origin is \( \sqrt{x_1^2 + x_2^2} \). For \( x = (3, 4) \) the legs are \( 3 \) and \( 4 \), and the distance is \( \sqrt{9 + 16} = 5 \). Chapter 3 gave this number a name, the modulus \( \abs{x_1 + x_2 i} \) (@def-conjugate-modulus). In space the same picture, used twice, gives \( \sqrt{x_1^2 + x_2^2 + x_3^2} \). The pictures stop at three coordinates, but the formula does not, and the expression under the root is the dot product \( \inner{x}{x} \). The pictures are motivation only. What we need from them is one property: a length is zero only for the point at the origin.

::: {.check}
Is there a vector \( x \ne 0 \) in some \( \nR^n \) with \( \inner{x}{x} = 0 \)?
:::

::: {.solution}
No. By @prp-dot-product-laws-rn (c), \( \inner{x}{x} = \sum_k x_k^2 \ge 0 \), with equality only for \( x = 0 \). A nonzero \( x \) has some \( x_k \ne 0 \), and that one term already makes the sum positive.
:::

So \( \inner{x}{x} \) is never negative. Every non-negative element of a complete ordered field has exactly one non-negative square root (@fd3:prp-cof-square-roots). The field \( \nR \) is complete (@fd3:thm-reals-complete-ordered-field), so the root of \( \inner{x}{x} \) exists. This is where the completeness of \( \nR \) enters the chapter.

*Length is the root of the dot product of a vector with itself.* We take this root as the length of \( x \).

::: {#def-norm-rn}
[Norm]

Let \( x \in \nR^n \). The **norm** (or **length**) of \( x \) is the real number
\[
\norm{x} \coloneqq \sqrt{\inner{x}{x}} = \sqrt{x_1^2 + \dots + x_n^2} ,
\]
the non-negative square root of @fd3:prp-cof-square-roots.
:::

For example, \( \norm{(3, 4)} = \sqrt{9 + 16} = \sqrt{25} = 5 \), because \( 5 \ge 0 \) and \( 5^2 = 25 \). The uniqueness clause of @fd3:prp-cof-square-roots identifies the root by these two properties. Each norm computed below can be checked the same way: the claimed root is \( \ge 0 \) and its square is the given number. The norm is well defined, since \( \inner{x}{x} \ge 0 \) by @prp-dot-product-laws-rn (c).

Two facts about roots carry most of the proofs in this section. The first is the uniqueness clause just used: *if \( s \ge 0 \) and \( s^2 = t \), then \( s = \sqrt t \).* The second is the rule of **comparing squares** from Section 3.3, a consequence of @fd3:prp-ordered-ring-rules (g) together with trichotomy: for real \( p, q \ge 0 \),
\[
p \le q \iff p^2 \le q^2 , \qquad p = q \iff p^2 = q^2 ,
\]
and likewise with \( < \) on both sides. The hypothesis \( p \ge 0 \) matters: \( -2 \le 1 \), but \( (-2)^2 > 1^2 \). Swapping the roles shows that \( q \ge 0 \) matters too.

::: {#prp-norm-basic-rn}
[Basic Properties of the Norm]

Let \( x \in \nR^n \) and \( c \in \nR \).

::: {.enumerate options="label=(\alph*)"}
1. \( \norm{x} \ge 0 \), and \( \norm{x} = 0 \) if and only if \( x = 0 \).
2. \( \norm{cx} = \abs{c} \, \norm{x} \).
3. \( \norm{x}^2 = \inner{x}{x} \).
4. For \( n = 1 \), \( \norm{x} = \abs{x} \).
5. \( \norm{e_k} = 1 \) for every \( k \).
6. If \( x \ne 0 \), the vectors \( u \) with \( \norm{u} = 1 \) that are parallel to \( x \) are exactly \( \frac{1}{\norm{x}} \, x \) and \( -\frac{1}{\norm{x}} \, x \).
:::
:::

::: {.idea}
Each part is a statement about a root, so it is checked on squares: compute the square with the dot-product laws of Section 9.3, then identify the root by its sign and its square.
:::

::: {.proof}
(c) This is the defining property of the root: \( (\sqrt t)^2 = t \).

(a) A square root is non-negative by definition. If \( x = 0 \), then \( \inner{x}{x} = 0 \), and \( \sqrt 0 = 0 \) by uniqueness, as \( 0 \ge 0 \) and \( 0^2 = 0 \). Conversely, if \( \norm{x} = 0 \), then \( \inner{x}{x} = \norm{x}^2 = 0 \) by (c), so \( x = 0 \) by @prp-dot-product-laws-rn (c).

(b) A scalar comes out of each slot of the dot product. Then (c) turns the dot products back into squared norms:
\[
\norm{cx}^2 = \inner{cx}{cx} = c^2 \inner{x}{x} = c^2 \norm{x}^2 .
\]
The number \( \abs{c} \, \norm{x} \) is \( \ge 0 \), as a product of two non-negative numbers: \( \abs{c} \ge 0 \), and \( \norm{x} \ge 0 \) by (a) above. Its square is \( \abs{c}^2 \norm{x}^2 = c^2 \norm{x}^2 \). So \( \norm{cx} \) and \( \abs{c} \, \norm{x} \) are non-negative with the same square, and they are equal by comparing squares.

(d) For \( n = 1 \), \( \inner{x}{x} = x^2 \) (@def-dot-product-rn), so \( \norm{x} = \sqrt{x^2} \). As in @prp-modulus-of-real, \( \abs{x} \ge 0 \) and \( \abs{x}^2 = x^2 \), so \( \abs{x} = \sqrt{x^2} \) by uniqueness.

(e) \( \inner{e_k}{e_k} = 1 \) by @prp-dot-product-laws-rn (d), and \( \sqrt 1 = 1 \) since \( 1 \ge 0 \) and \( 1^2 = 1 \).

(f) Let \( x \ne 0 \), so \( \norm{x} > 0 \) by (a), and put \( t_0 \coloneqq \frac{1}{\norm{x}} \). The vectors \( \pm t_0 x \) are parallel to \( x \) (@def-parallel-rn), and by (b) their norms are \( \abs{\pm t_0} \, \norm{x} = t_0 \norm{x} = 1 \). Conversely, let \( \norm{u} = 1 \) with \( u \) parallel to \( x \). Since \( x \ne 0 \), a vector parallel to \( x \) is a multiple of \( x \) (Section 9.2, after @def-parallel-rn), so \( u = tx \) for some \( t \in \nR \). Then \( 1 = \norm{tx} = \abs{t} \, \norm{x} \) by (b), so \( \abs{t} = t_0 \). Since \( \abs{t} \) is \( t \) or \( -t \), we get \( t = t_0 \) or \( t = -t_0 \). This proves the proposition.

::: {.uses}
@prp-dot-product-laws-rn (e), (b): the zero vector, scalars come out. @fd3:prp-absolute-value-ordered-field (a), (b): \( \abs{c} \ge 0 \), \( \abs{c}^2 = c^2 \). @fd3:prp-reciprocal-order: \( 1/p > 0 \) for \( p > 0 \). @fd3:def-absolute-value-ordered-field: \( \abs{t} \) is \( \pm t \).
:::
:::

Part (b) says that stretching a vector by \( c \) stretches its length by \( \abs{c} \); the absolute value is needed, since \( \norm{-x} = \norm{x} \). Part (d) says that on \( \nR^1 = \nR \) the norm is the old absolute value, so the double bars extend the single ones and nothing clashes.

Dividing a nonzero vector by its norm gives a vector of length \( 1 \). For example, \( (3, 4) \) has norm \( 5 \), and by (b) the vector \( \frac15 (3, 4) = (3/5, 4/5) \) has norm \( \frac15 \cdot 5 = 1 \).

::: {#def-unit-vector-rn}
[Unit Vector]

A **unit vector** is a vector \( u \in \nR^n \) with \( \norm{u} = 1 \). For \( x \ne 0 \) we write \( \dfrac{x}{\norm{x}} \coloneqq \dfrac{1}{\norm{x}} \, x \), and call it the **unit vector in the direction of \( x \)**.
:::

The division is allowed because \( \norm{x} \ne 0 \) for \( x \ne 0 \), by part (a) of @prp-norm-basic-rn. Part (b) shows that \( x / \norm{x} \) is a unit vector. By part (f), the only other unit vector parallel to \( x \) is \( -x / \norm{x} \). Replacing \( x \) by \( x / \norm{x} \) is called **normalizing** \( x \). For example, \( (3, 4)/5 = (3/5, 4/5) \) is the unit vector in the direction of \( (3, 4) \), and the standard vectors \( e_k \) are unit vectors by (e).

::: {.check}
Compute \( \norm{(1, 2, 2)} \). Is \( (3/5, 0, 4/5) \) a unit vector?
:::

::: {.solution}
\( \norm{(1, 2, 2)} = \sqrt{1 + 4 + 4} = \sqrt 9 = 3 \), since \( 3 \ge 0 \) and \( 3^2 = 9 \). And \( \inner{(3/5, 0, 4/5)}{(3/5, 0, 4/5)} = 9/25 + 0 + 16/25 = 1 \), so the norm is \( \sqrt 1 = 1 \): yes.
:::

::: {.warning}
The length of a vector is **not** the sum of the sizes of its coordinates. \( \norm{(1, 1)} = \sqrt 2 \), not \( \abs{1} + \abs{1} = 2 \); since \( (1, 1) = e_1 + e_2 \), this also shows \( \norm{e_1 + e_2} = \sqrt 2 \ne 2 = \norm{e_1} + \norm{e_2} \). (Here \( \sqrt 2 \ne 2 \) because \( 2^2 = 4 \ne 2 \).) The norm respects scalar multiples, by @prp-norm-basic-rn (b), but not sums.
:::

## Distance

The distance between two points should be the length of the displacement from one to the other, \( y - x \) in the language of Section 9.2. We use \( x - y \); it has the same length, by part (b) below.

::: {#def-distance-rn}
[Distance]

For \( x, y \in \nR^n \), the **distance** from \( x \) to \( y \) is \( d(x, y) \coloneqq \norm{x - y} \).
:::

For example, \( d\bigl((1, 2), (4, 6)\bigr) = \norm{(-3, -4)} = 5 \). For \( n = 1 \), \( d(x, y) = \abs{x - y} \) by @prp-norm-basic-rn (d). That is the distance on the line of *Number Systems: From \(\nN\) to \(\nR\)*, Chapter 4 (@fd3:def-absolute-value-ordered-field).

::: {#prp-distance-basic-rn}
[Basic Properties of the Distance]

For all \( x, y, z \in \nR^n \) and \( c \in \nR \):

::: {.enumerate options="label=(\alph*)"}
1. \( d(x, y) \ge 0 \), and \( d(x, y) = 0 \) if and only if \( x = y \);
2. \( d(x, y) = d(y, x) \);
3. \( d(x + z, y + z) = d(x, y) \);
4. \( d(cx, cy) = \abs{c} \, d(x, y) \).
:::
:::

::: {.proof}
Each part rests on a vector identity that is checked coordinatewise (@exm-method-coordinatewise). (a) This is @prp-norm-basic-rn (a), since \( x - y = 0 \) if and only if \( x = y \). (b) \( y - x = (-1)(x - y) \), so @prp-norm-basic-rn (b) with \( \abs{-1} = 1 \) gives \( \norm{y - x} = \norm{x - y} \). (c) \( (x + z) - (y + z) = x - y \). (d) \( cx - cy = c(x - y) \), then @prp-norm-basic-rn (b).
:::

Part (c) says that sliding both points by the same vector does not change their distance; (d) says that scaling the picture by \( c \) scales distances by \( \abs{c} \). The property that matters most is missing from the list: the triangle inequality \( d(x, z) \le d(x, y) + d(y, z) \). It is the one property of distance that needs an idea, and Section 9.5 supplies it.

## The plane is the complex plane

Chapter 3 defined \( \nC \) as the set \( \nR^2 \) (@def-complex-numbers) and measured its elements with the modulus. This chapter has now put a second structure on the same set. The two fit together exactly.

::: {#prp-plane-is-complex-plane}
[The Plane and the Complex Numbers]

Let \( z = (a, b) \) and \( w = (c, d) \) be elements of \( \nR^2 = \nC \), and let \( t \in \nR \).

::: {.enumerate options="label=(\alph*)"}
1. The sum \( z + w \) is the same in \( \nR^2 \) and in \( \nC \), and so is the difference \( z - w \). The scalar multiple \( tz \) equals the complex product \( (t, 0)\, z \), that is, the product in \( \nC \) of the real number \( t \) with \( z \) (@prp-reals-embed-complex).
2. \( \inner{z}{w} = \operatorname{Re}(z \conj{w}) \).
3. \( \norm{z} = \abs{z} \), and so \( d(z, w) = \abs{z - w} \).
:::
:::

::: {.idea}
Every part compares two formulas in the coordinates \( a, b, c, d \). Write both sides out by the definitions of Chapter 3 and of this chapter, and read off that they agree.
:::

::: {.proof}
(a) Both sums are \( (a + c, b + d) \) by the two definitions. By the multiplication rule of @def-complex-numbers, \( (t, 0)(a, b) = (ta - 0 \cdot b, \; tb + 0 \cdot a) = (ta, tb) \), which is \( tz \). In particular \( (-1)w = (-c, -d) \), and \( (c, d) + (-c, -d) = (0, 0) \), so \( (-c, -d) \) is the negative of \( w \) in \( \nC \) as well; hence both differences are \( (a - c, b - d) \).

(b) The conjugate of \( w \) is \( \conj{w} = (c, -d) \) (@def-conjugate-modulus). By the multiplication rule,
\[
z \conj{w} = \bigl(ac - b(-d), \; a(-d) + bc\bigr) = (ac + bd, \; bc - ad) .
\]
Its real part is \( ac + bd = \inner{z}{w} \) (@def-dot-product-rn).

(c) Both are \( \sqrt{a^2 + b^2} \), by the definitions of the norm and of the modulus. Then \( d(z, w) = \norm{z - w} = \abs{z - w} \) by (a).

::: {.uses}
@def-vector-operations-rn: the sum in \( \nR^2 \). @def-complex-numbers: sum and product in \( \nC \). @def-norm-rn. @def-conjugate-modulus: the modulus.
:::
:::

So every result of this chapter about \( \nR^n \), read at \( n = 2 \), is a result about \( \nC \). The order of the factors in (b) does not matter: \( \operatorname{Re}(z \conj{w}) = \operatorname{Re}(\conj{z} w) \), since the two products are conjugate (@thm-conjugate-properties (a), (b)). The coordinate bound (a) at the end of this section is, for \( n = 2 \), the first two inequalities of @lem-real-part-at-most-modulus. In the other direction, the multiplication of \( \nC \) has no counterpart in \( \nR^n \) for general \( n \) in this chapter; Section 9.5 explains why that matters.

## Comparing lengths through their squares

Norms do not expand: \( \norm{x + y} \) is the root of a sum, and nothing splits it. Squared norms do, because \( \norm{v}^2 = \inner{v}{v} \) and the dot product is linear in each slot. The first example is the theorem of Pythagoras, with "right angle" read as "dot product zero" (@def-orthogonal-rn). For instance, \( \inner{(3, 0)}{(0, 4)} = 0 \), and indeed \( \norm{(3, 0) + (0, 4)}^2 = \norm{(3, 4)}^2 = 25 = 9 + 16 \).

::: {#prp-pythagoras-rn}
[Theorem of Pythagoras]

Let \( x, y \in \nR^n \). Then
\[
\norm{x + y}^2 = \norm{x}^2 + \norm{y}^2 \iff x \perp y ,
\]
and the same holds with \( x - y \) in place of \( x + y \).
:::

::: {.idea}
[Scratch work]

We want an equivalence between a statement about norms and a statement about a dot product. Norms cannot be expanded. So first we rewrite every squared norm as a dot product, and then we expand.

| We know | We want |
|---|---|
| \( x, y \in \nR^n \) | \( \norm{x + y}^2 = \norm{x}^2 + \norm{y}^2 \iff \inner{x}{y} = 0 \) |
| \( \norm{v}^2 = \inner{v}{v} \) (@prp-norm-basic-rn (c)) | \( \inner{x + y}{x + y} = \inner{x}{x} + \inner{y}{y} \iff \inner{x}{y} = 0 \) |
| linearity and symmetry (@prp-dot-product-laws-rn (a), (b)) | \( \inner{x}{x} + 2\inner{x}{y} + \inner{y}{y} = \inner{x}{x} + \inner{y}{y} \iff \inner{x}{y} = 0 \) |
| cancel \( \inner{x}{x} + \inner{y}{y} \); \( 2 \ne 0 \) | \( 2\inner{x}{y} = 0 \iff \inner{x}{y} = 0 \), which is true |

The case \( x - y \) is the same table with \( -2\inner{x}{y} \) in the third row.
:::

::: {.proof}
Section 9.3 expanded \( \inner{x \pm y}{x \pm y} = \inner{x}{x} \pm 2\inner{x}{y} + \inner{y}{y} \) by linearity and symmetry, just after @prp-dot-product-laws-rn. By @prp-norm-basic-rn (c), these read
\[
\norm{x \pm y}^2 = \norm{x}^2 \pm 2\inner{x}{y} + \norm{y}^2 .
\]{#eq-expand-norm-squared}
So \( \norm{x \pm y}^2 = \norm{x}^2 + \norm{y}^2 \) holds if and only if \( \pm 2\inner{x}{y} = 0 \). This holds if and only if \( \inner{x}{y} = 0 \), since \( 2 \ne 0 \) in \( \nR \) and \( \nR \) has no zero divisors (@fd3:lem-field-fraction-rules (d)). By @def-orthogonal-rn, \( \inner{x}{y} = 0 \) says \( x \perp y \).

::: {.uses}
The expansion of \( \inner{x \pm y}{x \pm y} \) after @prp-dot-product-laws-rn (Section 9.3); @prp-norm-basic-rn (c).
:::
:::

The proof never mentions an angle or a triangle. Pythagoras' theorem is now an identity about squares of norms, with a dot product as the error term. The identity @eq-expand-norm-squared is behind the proofs of the parallelogram law and of polarization below, so the way of working deserves a name.

::: {#exm-method-expand-the-square}
[Method: expand the square]

**How it goes.** To prove an identity or an inequality between norms:

1. If lengths are compared, compare their squares instead. This is allowed because both sides are \( \ge 0 \).
2. Write each squared norm as a dot product, \( \norm{v}^2 = \inner{v}{v} \).
3. Expand by linearity and symmetry, as in @eq-expand-norm-squared.
4. Compare the expansions. Then return from squares to lengths by comparing squares.

**When to use it.** Identities and inequalities among the norms of sums, differences and multiples of vectors; conditions such as \( d(x, a) = d(x, b) \).

**Common mistakes.** A common mistake is to drop the cross term \( 2\inner{x}{y} \), which turns every expansion into Pythagoras. Another is to square a side that may be negative, such as \( \norm{x} - \norm{y} \); comparing squares does not apply there.
:::

The second worked example is the law of the parallelogram. In the plane, the parallelogram spanned by \( x \) and \( y \) has diagonals \( x + y \) and \( x - y \). The law says that the squares of the two diagonals add up to the squares of the four sides. For \( x = (2, 0) \) and \( y = (1, 1) \), the diagonals are \( (3, 1) \) and \( (1, -1) \), and \( 10 + 2 = 12 = 2 \cdot 4 + 2 \cdot 2 \).

::: {#prp-parallelogram-law-rn}
[Parallelogram Law]

For all \( x, y \in \nR^n \),
\[
\norm{x + y}^2 + \norm{x - y}^2 = 2\norm{x}^2 + 2\norm{y}^2 .
\]
:::

::: {.proof}
We expand the squares, as in @exm-method-expand-the-square. No lengths are compared, only squares, so we never pass to roots. Each side is a sum of dot products: \( \norm{x \pm y}^2 = \inner{x \pm y}{x \pm y} \) by @prp-norm-basic-rn (c). The identity @eq-expand-norm-squared expands both:
\[
\begin{aligned}
\norm{x + y}^2 &= \norm{x}^2 + 2\inner{x}{y} + \norm{y}^2 , \\
\norm{x - y}^2 &= \norm{x}^2 - 2\inner{x}{y} + \norm{y}^2 .
\end{aligned}
\]
Now add the two lines: the cross terms \( 2\inner{x}{y} \) and \( -2\inner{x}{y} \) cancel, and what is left is \( 2\norm{x}^2 + 2\norm{y}^2 \). This proves the law.
:::

Subtracting the two lines instead of adding them makes the norms cancel and keeps the cross term. That gives the dot product back from lengths.

::: {#prp-polarization-rn}
[Polarization]

For all \( x, y \in \nR^n \):

::: {.enumerate options="label=(\alph*)"}
1. \( \inner{x}{y} = \frac14 \bigl( \norm{x + y}^2 - \norm{x - y}^2 \bigr) \);
2. \( 2\inner{x}{y} = \norm{x}^2 + \norm{y}^2 - \norm{x - y}^2 \).
:::
:::

::: {.proof}
(a) Subtract the second expansion in the proof of @prp-parallelogram-law-rn from the first: \( \norm{x + y}^2 - \norm{x - y}^2 = 4\inner{x}{y} \); divide by \( 4 \ne 0 \). (b) Solve the second expansion, \( \norm{x - y}^2 = \norm{x}^2 - 2\inner{x}{y} + \norm{y}^2 \), for \( 2\inner{x}{y} \).
:::

Polarization says that lengths determine dot products: whoever knows every distance knows every dot product. For instance, let \( f \colon \nR^n \to \nR^n \) preserve distances, \( d(f(x), f(y)) = d(x, y) \) for all \( x, y \), and suppose \( f(0) = 0 \). Then \( \norm{f(x)} = d(f(x), f(0)) = d(x, 0) = \norm{x} \), and (b) gives \( \inner{f(x)}{f(y)} = \inner{x}{y} \). Which maps behave like this is a question for the linear algebra volumes.

## Length against coordinates

Analysis in several variables keeps changing between two ways of saying that \( x \) is small: \( \norm{x} \) is small, or every coordinate \( x_k \) is small. The two are equivalent, with constants that depend only on \( n \). For example, for \( x = (1, -2, 2) \) the largest size of a coordinate is \( 2 \), and \( \norm{x} = \sqrt 9 = 3 \). So \( 2 \le 3 \le 2\sqrt 3 \), where the second inequality holds since \( 3^2 = 9 \le 12 = (2\sqrt 3)^2 \). In general, let \( M \coloneqq \max\{ \abs{x_1}, \dots, \abs{x_n} \} \), the largest size of a coordinate; the maximum exists and is one of the listed numbers (@fd2:prp-finite-max).

::: {#prp-norm-coordinate-bounds}
[Norm against Coordinates]

Let \( x \in \nR^n \) and \( M \coloneqq \max\{ \abs{x_1}, \dots, \abs{x_n} \} \).

::: {.enumerate options="label=(\alph*)"}
1. \( \abs{x_k} \le \norm{x} \) for every \( k \); hence \( M \le \norm{x} \).
2. \( \norm{x} \le \sqrt n \, M \).
:::
:::

::: {.idea}
The square \( \norm{x}^2 = x_1^2 + \dots + x_n^2 \) is a sum of \( n \) non-negative terms. Keeping one term and dropping the rest makes it smaller, which gives (a); replacing every term by the largest one makes it larger, which gives (b). In both parts we work with squares and come back by comparing squares.
:::

::: {.proof}
By @prp-norm-basic-rn (c), \( \norm{x}^2 = \inner{x}{x} = \sum_{j=1}^{n} x_j^2 \). Every term \( x_j^2 \) is \( \ge 0 \), since a square is never negative.

(a) Fix \( k \). A sum of non-negative terms is at least each of its terms (@prp-sum-order (b)), so \( x_k^2 \le \sum_{j=1}^{n} x_j^2 = \norm{x}^2 \). Since \( x_k^2 = \abs{x_k}^2 \), this reads \( \abs{x_k}^2 \le \norm{x}^2 \). Both \( \abs{x_k} \) and \( \norm{x} \) are \( \ge 0 \), so comparing squares gives \( \abs{x_k} \le \norm{x} \). The maximum \( M \) is one of the numbers \( \abs{x_k} \), so \( M \le \norm{x} \).

(b) For every \( j \), \( 0 \le \abs{x_j} \le M \), so \( \abs{x_j} \abs{x_j} \le M M \) by @fd3:prp-ordered-field-halves (d), that is, \( x_j^2 \le M^2 \). A sum of \( n \) terms, each at most \( M^2 \), is at most \( n M^2 \) (@prp-sum-order (c)), so \( \norm{x}^2 \le n M^2 \). The number \( \sqrt n \, M \) is \( \ge 0 \), and its square is \( (\sqrt n)^2 M^2 = n M^2 \). So \( \norm{x}^2 \le (\sqrt n \, M)^2 \), and comparing squares gives \( \norm{x} \le \sqrt n \, M \).

::: {.uses}
@prp-dot-product-laws-rn (c): \( \inner{x}{x} \) as a sum. @fd3:prp-ordered-ring-rules (e): squares are \( \ge 0 \). @fd3:prp-absolute-value-ordered-field (b): \( \abs{a}^2 = a^2 \).
:::
:::

Neither constant can be improved. For \( x = e_1 \), \( M = \norm{x} = 1 \), so (a) is an equality. For \( x = (1, \dots, 1) \), \( M = 1 \) and \( \norm{x} = \sqrt{1 + \dots + 1} = \sqrt n \), so (b) is an equality. For \( n = 1 \) both parts say \( \norm{x} = \abs{x} \).

The proposition is used mostly in the following form, about the points near a given point \( a \). Recall that \( \abs{x_k - a_k} < r \) says \( a_k - r < x_k < a_k + r \) (@fd3:prp-absolute-value-ordered-field (d)). So "\( \abs{x_k - a_k} < r \) for every \( k \)" says that \( x \) lies in the open box \( (a_1 - r, a_1 + r) \times \dots \times (a_n - r, a_n + r) \) of @def-box-rn, centered at \( a \).

::: {#cor-balls-and-boxes-rn}
[Balls and Boxes]

Let \( a \in \nR^n \) and \( r > 0 \), and let \( x \in \nR^n \).

::: {.enumerate options="label=(\alph*)"}
1. If \( \norm{x - a} < r \), then \( \abs{x_k - a_k} < r \) for every \( k \).
2. If \( \abs{x_k - a_k} < r / \sqrt n \) for every \( k \), then \( \norm{x - a} < r \).
:::
:::

::: {.proof}
The \( k \)-th coordinate of \( x - a \) is \( x_k - a_k \). (a) By @prp-norm-coordinate-bounds (a) for \( x - a \), \( \abs{x_k - a_k} \le \norm{x - a} < r \). (b) Let \( M \coloneqq \max_k \abs{x_k - a_k} \). It is one of the numbers \( \abs{x_k - a_k} \), so \( M < r/\sqrt n \). We have \( \sqrt n > 0 \), since \( \sqrt n \ge 0 \) and \( \sqrt n \ne 0 \), as \( 0^2 \ne n \). So multiplying by \( \sqrt n \) keeps the strict inequality (@fd3:prp-ordered-ring-rules (c)). Then @prp-norm-coordinate-bounds (b) for \( x - a \) gives \( \norm{x - a} \le \sqrt n \, M < r \).
:::

In words: take the set of points at distance less than \( r \) from \( a \), a disc in the plane. It sits inside the open square of half-side \( r \) centered at \( a \). It contains the smaller open square of half-side \( r / \sqrt 2 \), whose corners lie on the boundary circle. In \( \nR^n \) the same holds with boxes, and the inner box shrinks as \( n \) grows. The analysis volumes use the corollary to pass between "close in distance" and "close in every coordinate", so that a limit in \( \nR^n \) can be taken one coordinate at a time.

## Exercises

### A. Check your understanding

:::: {#exr-length-and-distance-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \norm{(2, -3, 6)} \) and the unit vector in the direction of \( (2, -3, 6) \).
2. Compute \( d\bigl((1, -1, 0), (3, 1, 1)\bigr) \).
3. For \( x = (2, -1, 2, 0) \), compute \( M \), \( \norm{x} \) and \( \sqrt n \, M \), and check both bounds of @prp-norm-coordinate-bounds.
4. Where does the proof of @prp-norm-coordinate-bounds use that every term \( x_j^2 \) is \( \ge 0 \)?
5. Why does @cor-balls-and-boxes-rn (b) assume \( \abs{x_k - a_k} < r/\sqrt n \) and not \( \abs{x_k - a_k} < r \)? Answer with an example for \( n \ge 2 \).
6. State the idea of the proof of @prp-norm-coordinate-bounds (b) in two sentences.
:::
::::

::: {.solution}
(a) \( \norm{(2, -3, 6)} = \sqrt{4 + 9 + 36} = \sqrt{49} = 7 \), since \( 7 \ge 0 \) and \( 7^2 = 49 \). The unit vector is \( (2, -3, 6)/7 = (2/7, -3/7, 6/7) \).

(b) The difference is \( (1, -1, 0) - (3, 1, 1) = (-2, -2, -1) \), so the distance is \( \sqrt{4 + 4 + 1} = \sqrt 9 = 3 \).

(c) \( M = \max\{2, 1, 2, 0\} = 2 \), \( \norm{x} = \sqrt{4 + 1 + 4 + 0} = 3 \), and \( \sqrt 4 \cdot 2 = 4 \). Indeed \( 2 \le 3 \le 4 \).

(d) In (a), to drop all terms except \( x_k^2 \): the sum is at least one of its terms only because the other terms are non-negative (@prp-sum-order (b)). Part (b) does not need it.

(e) With \( r \) in place of \( r/\sqrt n \), the statement is false for every \( n \ge 2 \). Since \( \sqrt n > 1 \), we have \( r/\sqrt n < r \), so we can choose \( c \) with \( r/\sqrt n \le c < r \); for \( n \ge 4 \), \( c = r/2 \) is such a choice, since then \( \sqrt n \ge 2 \). Let \( x \coloneqq a + c(1, \dots, 1) \). Then \( \abs{x_k - a_k} = c < r \) for every \( k \), but \( \norm{x - a} = c\sqrt n \ge r \) by @prp-norm-basic-rn (b), since \( \norm{(1, \dots, 1)} = \sqrt n \). For \( n = 1 \), \( \sqrt 1 = 1 \) and the two versions agree.

(f) The square \( \norm{x}^2 \) is a sum of \( n \) squares, each at most \( M^2 \), so it is at most \( n M^2 \). Both \( \norm{x} \) and \( \sqrt n \, M \) are non-negative, so the inequality between their squares gives the inequality between the numbers.
:::

### B. Practice

:::: {#exr-length-and-distance-b1}
[B1: Prove or disprove]

Prove or disprove each statement for all \( x, y \in \nR^n \), \( n \ge 2 \).

::: {.enumerate options="label=(\alph*)"}
1. If \( \norm{x} = \norm{y} \), then \( x = y \) or \( x = -y \).
2. If \( \norm{x} = \norm{y} \), then \( x + y \perp x - y \).
3. If \( x \perp y \), then \( \norm{x - y} = \norm{x + y} \).
4. \( \norm{x + y}^2 \le 2\norm{x}^2 + 2\norm{y}^2 \).
5. If \( x \perp y \), then \( d(x, 0) + d(0, y) = d(x, y) \).
:::
::::

::: {.solution}
(a) **False.** Take \( x = e_1 \) and \( y = e_2 \). Both have norm \( 1 \) (@prp-norm-basic-rn (e)), but \( e_1 \ne e_2 \) and \( e_1 \ne -e_2 \) (compare first coordinates: \( 1 \ne 0 \)).

(b) **True.** By linearity and symmetry (@prp-dot-product-laws-rn (a), (b)), \( \inner{x + y}{x - y} = \inner{x}{x} - \inner{x}{y} + \inner{y}{x} - \inner{y}{y} = \norm{x}^2 - \norm{y}^2 \), which is \( 0 \) when \( \norm{x} = \norm{y} \).

(c) **True.** By @prp-pythagoras-rn, used for \( x + y \) and for \( x - y \), both \( \norm{x + y}^2 \) and \( \norm{x - y}^2 \) equal \( \norm{x}^2 + \norm{y}^2 \). The two norms are non-negative with equal squares, so they are equal by comparing squares.

(d) **True.** By @prp-parallelogram-law-rn, \( \norm{x + y}^2 = 2\norm{x}^2 + 2\norm{y}^2 - \norm{x - y}^2 \), and \( \norm{x - y}^2 \ge 0 \).

(e) **False.** Take \( x = e_1 \), \( y = e_2 \), which are orthogonal (@prp-dot-product-laws-rn (d)). Then \( d(x, 0) + d(0, y) = 1 + 1 = 2 \), but \( d(x, y) = \norm{e_1 - e_2} = \norm{(1, -1, 0, \dots, 0)} = \sqrt 2 \ne 2 \).
:::

::: {#exr-length-and-distance-b2}
[B2]

Let \( a = (1, 2) \), \( b = (4, 6) \) and \( c = (-3, 5) \). Show that \( b - a \perp c - a \), and check the theorem of Pythagoras for the triangle with corners \( a \), \( b \), \( c \) by computing the three squared side lengths.
:::

::: {.solution}
\( b - a = (3, 4) \) and \( c - a = (-4, 3) \), and \( \inner{(3, 4)}{(-4, 3)} = -12 + 12 = 0 \). The squared sides are \( \norm{b - a}^2 = 9 + 16 = 25 \), \( \norm{c - a}^2 = 16 + 9 = 25 \), and, since \( (b - a) - (c - a) = b - c = (7, 1) \), \( \norm{b - c}^2 = 49 + 1 = 50 \). Indeed \( 25 + 25 = 50 \), as @prp-pythagoras-rn (with \( x - y \), \( x = b - a \), \( y = c - a \)) predicts. The two legs have length \( 5 \), and the third side has length \( \sqrt{50} = 5\sqrt 2 \).
:::

::: {#exr-length-and-distance-b3}
[B3]

Let \( a, b \in \nR^n \) with \( a \ne b \). Prove that a point \( x \in \nR^n \) satisfies \( d(x, a) = d(x, b) \) if and only if
\[
\inner{x}{b - a} = \tfrac12 \bigl( \norm{b}^2 - \norm{a}^2 \bigr) ,
\]
and check that the midpoint \( \frac12 (a + b) \) satisfies this equation.

*Hint: which method compares two lengths?*
:::

::: {.solution}
We expand the squares (@exm-method-expand-the-square). Both distances are non-negative, so by comparing squares \( d(x, a) = d(x, b) \) if and only if \( \norm{x - a}^2 = \norm{x - b}^2 \). By @eq-expand-norm-squared,
\[
\norm{x - a}^2 = \norm{x}^2 - 2\inner{x}{a} + \norm{a}^2 , \qquad \norm{x - b}^2 = \norm{x}^2 - 2\inner{x}{b} + \norm{b}^2 .
\]
Cancelling \( \norm{x}^2 \), the two are equal if and only if \( 2\inner{x}{b} - 2\inner{x}{a} = \norm{b}^2 - \norm{a}^2 \), that is, by linearity, \( 2\inner{x}{b - a} = \norm{b}^2 - \norm{a}^2 \). Divide by \( 2 \).

For \( x = \frac12 (a + b) \): by linearity and symmetry, \( \inner{a + b}{b - a} = \norm{b}^2 - \inner{a}{b} + \inner{a}{b} - \norm{a}^2 = \norm{b}^2 - \norm{a}^2 \), so \( \inner{\frac12 (a + b)}{b - a} = \frac12 (\norm{b}^2 - \norm{a}^2) \).

The hypothesis \( a \ne b \) is not used in the equivalence, which holds for \( a = b \) too (both sides then hold for every \( x \)). It makes the vector \( b - a \) nonzero, so that the equation is a genuine condition on \( x \); Chapter 10 calls such a set a hyperplane, and this one is the perpendicular bisector of \( a \) and \( b \).

::: {.uses}
@prp-dot-product-laws-rn: linearity and symmetry.
:::
:::

### C. Going deeper

::: {#exr-length-and-distance-c1}
[C1: Find the error]

The conclusion of the following argument is true. Is the argument correct? If not, name the line that fails, say why, and repair it.

"*Claim.* For every \( x \in \nR^n \) and every \( k \), \( \abs{x_k} \le \norm{x} \).

*Proof.* (1) The other terms of \( \norm{x}^2 = \sum_j x_j^2 \) are non-negative, so \( \norm{x}^2 \ge x_k^2 \). (2) Taking non-negative square roots, which preserves \( \le \), we get \( \norm{x} \ge \sqrt{x_k^2} \). (3) Since \( \sqrt{a^2} = a \) for every real \( a \), this gives \( \norm{x} \ge x_k \). (4) Applying this to \( -x \), whose norm is \( \norm{x} \), gives \( \norm{x} \ge -x_k \). (5) So \( \norm{x} \ge \abs{x_k} \)."
:::

::: {.solution}
The conclusion is true: it is @prp-norm-coordinate-bounds (a). The argument is not correct. The one bad line is (3). It cites the "fact" \( \sqrt{a^2} = a \) for every real \( a \), which is false. Citing a false general fact is never allowed; it is (N9) in the list of *Logic and Proof* (@fd1:exm-not-allowed-catalogue). A counterexample to the step: for \( a = -3 \), \( \sqrt{(-3)^2} = \sqrt 9 = 3 \ne -3 \). The correct fact is \( \sqrt{a^2} = \abs{a} \), by @prp-norm-basic-rn (d).

The other lines are correct:

- Line (1) is @prp-sum-order (b).
- Line (2) is comparing squares, since \( \norm{x} \) and \( \sqrt{x_k^2} \) are non-negative with squares \( \norm{x}^2 \ge x_k^2 \).
- Line (4) uses \( \norm{-x} = \norm{x} \) (@prp-norm-basic-rn (b)).
- Line (5) holds because \( \abs{x_k} \) is \( x_k \) or \( -x_k \).

Even line (3) can be saved. The true inequality \( \sqrt{a^2} \ge a \) holds, as \( \sqrt{a^2} = \abs{a} \ge a \) (@fd3:prp-absolute-value-ordered-field (c)). With it, lines (3)–(5) prove the claim. So the argument reaches a true conclusion, and only one of its lines needs a different justification. A correct conclusion does not make every line correct.

*Repair.* Replace (3) by "\( \sqrt{x_k^2} = \abs{x_k} \) (@prp-norm-basic-rn (d))"; then (2) gives \( \norm{x} \ge \abs{x_k} \) at once, and lines (4) and (5) become unnecessary.

::: {.uses}
@prp-modulus-of-real: the same fact, in Chapter 3.
:::
:::

<!-- dependency ledger
def-norm-rn (claim): sqrt 25 = 5, sqrt 9 = 3, sqrt 1 = 1, sqrt 49 = 7, sqrt 0 = 0 by uniqueness | fd3:prp-cof-square-roots (cited); arithmetic in R; verify/ch09/def-norm-rn.py
def-norm-rn (claim): comparing squares: for p, q >= 0, p <= q iff p^2 <= q^2, p = q iff p^2 = q^2, and with < | fd3:prp-ordered-ring-rules (g), (i) (cited); the unlabelled paragraph "Comparing squares" of Section 3.3 (fd4 ch03 §03; prose pointer)
def-norm-rn (claim): (-2)^2 > 1^2 although -2 < 1 | arithmetic; inline
def-norm-rn (claim): the Quick check before it: a nonzero x has some x_k != 0 | tuple equality (F2.1 §04 "Longer lists", ledgered in ch09 §01); inline
prp-norm-basic-rn (proof): <cx, cx> = c^2 <x, x>, using (b) of prp-dot-product-laws-rn in each slot | prp-dot-product-laws-rn (b) (cited); fd3:prp-ring-algebra for c * c = c^2
prp-norm-basic-rn (proof): |c| ||x|| >= 0 as a product of non-negatives | (O4) of fd3:def-ordered-ring-and-field and fd3:prp-ring-algebra (b) (zero factor); used silently as in fd4 ch03 §02
prp-norm-basic-rn (proof): |t| is t or -t; |-t0| = t0 for t0 > 0 | fd3:def-absolute-value-ordered-field (cited); fd3:prp-absolute-value-ordered-field (b)
prp-norm-basic-rn (proof): 1/||x|| exists and is > 0 for ||x|| > 0 | fd3:prp-reciprocal-order (positive reciprocal); field axiom (F8)
def-unit-vector-rn (claim): instance before it: (1/5)(3, 4) = (3/5, 4/5) has norm (1/5) * 5 = 1 | prp-norm-basic-rn (b) (on the page); verify/ch09/def-norm-rn.py
def-unit-vector-rn (claim): (3, 4)/5 = (3/5, 4/5); (3/5, 0, 4/5) has norm 1 | verify/ch09/def-norm-rn.py
def-unit-vector-rn (claim): warning: ||(1, 1)|| = sqrt 2 != 2 = ||e1|| + ||e2|| since 2^2 = 4 != 2 | arithmetic; verify/ch09/def-norm-rn.py
def-distance-rn (claim): d((1,2),(4,6)) = 5 | verify/ch09/def-norm-rn.py
prp-distance-basic-rn (proof): x - y = 0 iff x = y; (x + z) - (y + z) = x - y; y - x = (-1)(x - y); cx - cy = c(x - y) | coordinatewise by exm-method-coordinatewise (cited) with field laws of R; inline
prp-plane-is-complex-plane (proof): (t,0)(a,b) = (ta, tb); (c,d) + (-c,-d) = (0,0) so (-c,-d) is the negative in C; z conj(w) = (ac + bd, bc - ad) | def-complex-numbers multiplication rule (cited); negatives unique in the ring C (fd3:prp-ring-algebra (a), via prp-complex-arithmetic-laws); verify/ch09/prp-plane-is-complex-plane.py
prp-plane-is-complex-plane (claim): Re(z conj w) = Re(conj z w), the products being conjugate | thm-conjugate-properties (a), (b) (cited); Re conj u = Re u from def-conjugate-modulus (prose after it in ch03 §02)
prp-plane-is-complex-plane (claim): bound (a) of prp-norm-coordinate-bounds at n = 2 is lem-real-part-at-most-modulus's first two inequalities; pointer to Section 9.5 | comparison, nothing depends on it; prose pointer within the chapter
prp-pythagoras-rn (claim): instance before it: <(3,0),(0,4)> = 0 and ||(3,4)||^2 = 25 = 9 + 16 | arithmetic; verify/ch09/def-norm-rn.py
prp-pythagoras-rn (proof): 2 != 0 in R; cancelling a common summand | fd3:prp-ordered-ring-rules (h) (2 = 2 * 1 > 0); fd3:lem-field-fraction-rules (d) (cited); additive cancellation in a ring (fd3:prp-ring-algebra)
prp-pythagoras-rn (proof): <x +- y, x +- y> expansions | cited from the paragraph after prp-dot-product-laws-rn (Section 9.3), no longer re-derived; prp-norm-basic-rn (c)
prp-parallelogram-law-rn (claim): instance before it: x = (2,0), y = (1,1): diagonals (3,1), (1,-1), 10 + 2 = 12 = 2*4 + 2*2 | arithmetic; verify/ch09/def-norm-rn.py
prp-polarization-rn (proof): dividing by 4 != 0 | fd3:prp-ordered-ring-rules (h); field (F8)
prp-polarization-rn (claim): a distance-preserving map fixing 0 preserves norms and dot products; pointer to the linear algebra volumes | prp-polarization-rn (b) (on the page); prose pointer, nothing depends on it
prp-norm-coordinate-bounds (claim): instance before it: x = (1,-2,2): largest coordinate size 2, ||x|| = sqrt 9 = 3, 3 <= 2 sqrt 3 since 9 <= 12 | arithmetic; uniqueness of roots and comparing squares (as in def-norm-rn); verify/ch09/prp-norm-coordinate-bounds.py
prp-norm-coordinate-bounds (proof): x_j^2 >= 0 | fd3:prp-ordered-ring-rules (e) and 0^2 = 0 (fd3:prp-ring-algebra (b)) (cited)
prp-norm-coordinate-bounds (proof): prp-sum-order (b), (c) are stated for sums over 0 <= k <= n; our sums run over 1 <= j <= n | reindexing: sum_{j=1}^{n} a_j is sum_{k=0}^{n-1} a_{k+1}, the k = m form of fd2:def-sum-product (template line, as in ch09 §02/§03); (c) then gives n M^2 for n terms
prp-norm-coordinate-bounds (proof): the maximum M exists and is one of the |x_k| | fd2:prp-finite-max (cited) with the definition of maximum (F2.2)
prp-norm-coordinate-bounds (proof): (sqrt n M)^2 = (sqrt n)^2 M^2 = n M^2; sqrt n M >= 0 | commutativity in R; definition of sqrt (fd3:prp-cof-square-roots); product of non-negatives as above
prp-norm-coordinate-bounds (claim): sharpness: e1 gives M = ||x|| = 1; (1, ..., 1) gives ||x|| = sqrt n = sqrt n M | prp-norm-basic-rn (e); arithmetic; verify/ch09/prp-norm-coordinate-bounds.py
cor-balls-and-boxes-rn (proof): sqrt n > 0 (0^2 = 0 != n for n >= 1) | fd3:prp-cof-square-roots; n * 1 > 0 by fd3:prp-ordered-ring-rules (h); inline
cor-balls-and-boxes-rn (claim): |x_k - a_k| < r iff a_k - r < x_k < a_k + r | fd3:prp-absolute-value-ordered-field (d) (cited) with (O3)
cor-balls-and-boxes-rn (claim): disc between squares of half-side r and r/sqrt 2, corners on the circle; pointer to the analysis volumes | the corollary itself at n = 2 (corners: ||(r/sqrt2, r/sqrt2)|| = r, verify/ch09/prp-norm-coordinate-bounds.py); prose pointer, nothing depends on it
exr-length-and-distance-a1 (solution): 7; (2/7, -3/7, 6/7); 3; M = 2, ||x|| = 3, 4; c in [r/sqrt n, r), c = r/2 for n >= 4, c sqrt n >= r | verify/ch09/exr-length-and-distance-a1.py
exr-length-and-distance-a1 (solution): sqrt n > 1 for n >= 2 | comparing squares (1^2 = 1 < n); inline
exr-length-and-distance-b1 (solution): counterexamples e1, e2; d(e1, e2) = sqrt 2 | verify/ch09/exr-length-and-distance-b1.py
exr-length-and-distance-b2 (solution): (3,4) . (-4,3) = 0; 25, 25, 50 | verify/ch09/exr-length-and-distance-b2.py
exr-length-and-distance-b3 (solution): the expansion identity and the midpoint identity | eq-expand-norm-squared, prp-dot-product-laws-rn (cited); verify/ch09/exr-length-and-distance-b3.py
exr-length-and-distance-b3 (solution): pointer to Chapter 10 (hyperplane, perpendicular bisector) | prose pointer (merged-ch10-f49.md, 10.2: def-hyperplane-rn, prp-perpendicular-bisector); nothing depends on it
exr-length-and-distance-c1 (solution): sqrt 9 = 3 != -3; |a| >= a | verify/ch09/exr-length-and-distance-c1.py; fd3:prp-absolute-value-ordered-field (c) (cited)
-->
