# Projection onto a Line and the Cosine of an Angle

Section 9.5 bounded the dot product by lengths, \( \abs{\inner{x}{y}} \le \norm{x}\norm{y} \). This section asks a new question: given a point \( x \) and a line through the origin, which point of the line is nearest to \( x \)? The answer splits \( x \) into a piece along the line and a piece orthogonal to it. Divided by lengths, the same split gives a number between \( -1 \) and \( 1 \) that measures how far two directions agree, the cosine of the angle between them.

## The nearest point on a line through the origin

Fix \( y \in \nR^n \) with \( y \ne 0 \). The multiples \( ty \), for \( t \in \nR \), form the **line through the origin in the direction of \( y \)**. Take a point \( x \in \nR^n \). Among all \( ty \), which one is nearest to \( x \)? In the plane a picture answers: drop a perpendicular from \( x \) to the line, and its foot is the nearest point. In \( \nR^5 \) there is no picture, but the picture suggests a guess to test.

Try a concrete case first. Let \( x = (3, 1) \) and \( y = (1, 1) \). The squared distance from \( x \) to \( ty \) is
\[
\norm{x - ty}^2 = (3 - t)^2 + (1 - t)^2 = 2t^2 - 8t + 10 = 2(t - 2)^2 + 2 .
\]
The last form shows the answer at once: the squared distance is at least \( 2 \), and it equals \( 2 \) only at \( t = 2 \). So the nearest point is \( 2y = (2, 2) \), and the distance is \( \sqrt 2 \). Now look at the error: \( x - 2y = (1, -1) \), and \( \inner{(1, -1)}{(1, 1)} = 0 \). The error is orthogonal to the line, as the picture promised.

Completing the square worked but hid the reason. In any \( \nR^n \) we guess that the error is orthogonal and check the guess with Pythagoras.

::: {.idea}
[Scratch work]

We plan the search with a table.

| We know | We want |
|---|---|
| \( x, y \in \nR^n \), \( y \ne 0 \) | find \( t \) with \( \norm{x - ty} \le \norm{x - sy} \) for **every** \( s \in \nR \) |
| guess: the error is perpendicular, \( \inner{x - ty}{y} = 0 \) | solve \( \inner{x}{y} - t\norm{y}^2 = 0 \): \( t_0 = \inner{x}{y}/\norm{y}^2 \), allowed since \( \norm{y}^2 \ne 0 \) |
| \( x - t_0 y \perp y \) | compare \( x - sy \) with \( x - t_0 y \) for an arbitrary \( s \) |
| \( x - sy = (x - t_0 y) + (t_0 - s)y \), two orthogonal pieces | Pythagoras: \( \norm{x - sy}^2 = \norm{x - t_0 y}^2 + (t_0 - s)^2\norm{y}^2 \) |

The last row closes the gap: the extra term \( (t_0 - s)^2\norm{y}^2 \) is never negative, so no \( s \) beats \( t_0 \). The picture supplied only the guess; Pythagoras supplies the proof.
:::

The number \( t_0 = \inner{x}{y}/\norm{y}^2 \) and the point \( t_0 y \) come back in this section and in Chapter 10, so they get a name.

::: {#def-projection-rn}
[Projection onto a Line]

Let \( x, y \in \nR^n \) with \( y \ne 0 \). The **projection of \( x \) onto \( y \)** is the vector
\[
\operatorname{proj}_y x \coloneqq \frac{\inner{x}{y}}{\norm{y}^2} \, y .
\]
:::

*The projection is the multiple of \( y \) that leaves an error orthogonal to \( y \).*

In words: \( \operatorname{proj}_y x \) is a **vector**, a scalar multiple of \( y \). The scalar is the number \( \inner{x}{y} \) divided by the **square** of the length of \( y \). Recall that \( \norm{y}^2 = \inner{y}{y} \) (@prp-norm-basic-rn (c)). This number is positive exactly when \( y \ne 0 \) (@prp-dot-product-laws-rn (c)).

**Examples.**

- **A unit vector.** If \( \norm{u} = 1 \), the denominator is \( 1 \), and \( \operatorname{proj}_u x = \inner{x}{u}\,u \).
- **A standard vector.** The vector \( e_k \) is a unit vector (@prp-norm-basic-rn (e)). For \( u = e_k \) this gives \( \operatorname{proj}_{e_k} x = \inner{x}{e_k} e_k = x_k e_k \), by @prp-dot-product-laws-rn (d). Projecting onto the \( k \)-th axis keeps the \( k \)-th coordinate and sets the others to \( 0 \). For \( x = (3, -1, 2) \) and \( k = 3 \), it gives \( (0, 0, 2) \).
- **The opening example.** For \( x = (3, 1) \) and \( y = (1, 1) \), \( \inner{x}{y} = 4 \) and \( \norm{y}^2 = 2 \), so \( \operatorname{proj}_y x = 2y = (2, 2) \), the point found above.
- **Two extreme cases.** If \( x \perp y \), the coefficient is \( 0 \), and \( \operatorname{proj}_y x = 0 \): the nearest point of the line to a point orthogonal to it is the origin. At the other extreme, if \( x = cy \) then \( \operatorname{proj}_y x = (c\norm{y}^2/\norm{y}^2) y = x \): a point already on the line is its own projection.

**When \( y = 0 \).** Keep \( x = (3, 1) \) and change \( y = (1, 1) \) to \( y = (0, 0) \). The formula now divides by \( \norm{y}^2 = 0 \), so it defines nothing. The question does not survive either: every \( ty \) is \( 0 \), so all of them are at the same distance \( \norm{x} \) from \( x \), and "the" nearest point is no longer a single \( t \). This is why the definition requires \( y \ne 0 \).

**Why this definition.** Dividing by \( \norm{y} \) instead of \( \norm{y}^2 \) would give \( 2\sqrt 2 \,(1, 1) \ne (2, 2) \) for \( y = (1, 1) \) and \( x = (3, 1) \), and its error is not orthogonal to \( y \). The square makes the answer independent of the length of \( y \), as Exercise B2 (c) shows: the projection depends on the line, not on the vector chosen to name it.

::: {.check}
Compute \( \operatorname{proj}_{(1, 0)} (2, 3) \) and \( \operatorname{proj}_{(2, 0)} (2, 3) \). Are they equal?
:::

::: {.solution}
For \( y = (1, 0) \): \( \inner{(2, 3)}{(1, 0)} = 2 \) and \( \norm{y}^2 = 1 \), so the projection is \( 2(1, 0) = (2, 0) \). For \( y = (2, 0) \): \( \inner{(2, 3)}{(2, 0)} = 4 \) and \( \norm{y}^2 = 4 \), so it is \( 1 \cdot (2, 0) = (2, 0) \). They are equal, because \( (1, 0) \) and \( (2, 0) \) name the same line.
:::

The scratch work above is a proof method.

::: {#exm-method-subtract-the-projection}
[Method: subtract the projection]

**How it goes.** Given \( x \) and \( y \ne 0 \), write
\[
x = p + (x - p) , \qquad p \coloneqq \operatorname{proj}_y x .
\]
The piece \( x - p \) is orthogonal to \( y \), hence to every multiple of \( y \). So Pythagoras (@prp-pythagoras-rn) splits the length of any vector of the form \( (x - p) + cy \): its square is \( \norm{x - p}^2 + c^2\norm{y}^2 \).

**When to use it.** Distances from a point to a line through the origin; inequalities between \( \inner{x}{y} \) and lengths; any problem where a vector should be split into "along \( y \)" and "orthogonal to \( y \)".

**Common mistakes.** It is easy to forget that \( y \ne 0 \) is needed before anything is divided. It is also easy to project onto the wrong vector: \( \operatorname{proj}_y x \) and \( \operatorname{proj}_x y \) are different in general, as Exercise B2 (e) shows. Finally, dividing by \( \norm{y} \) instead of \( \norm{y}^2 \) leaves an error that is not orthogonal to \( y \).

The closest-point theorem below is proved this way, and @exm-distance-to-a-line-through-the-origin uses it on numbers.
:::

The theorem turns the scratch work into a proof, and adds an exact identity for the cost of a wrong choice of \( t \).

::: {#thm-projection-closest-point}
[The Projection Is the Closest Point]

Let \( x, y \in \nR^n \) with \( y \ne 0 \), let \( t_0 \coloneqq \inner{x}{y}/\norm{y}^2 \), and let \( p \coloneqq t_0 y = \operatorname{proj}_y x \).

::: {.enumerate options="label=(\alph*)"}
1. \( x - p \perp y \), and \( t_0 \) is the **only** \( t \in \nR \) with \( x - ty \perp y \).
2. **For every** \( t \in \nR \),
\[
\norm{x - ty}^2 = \norm{x - p}^2 + (t - t_0)^2 \norm{y}^2 .
\]
Hence \( \norm{x - ty} \ge \norm{x - p} \), with equality **if and only if** \( t = t_0 \).
3. \( \norm{x}^2 = \norm{p}^2 + \norm{x - p}^2 \), and \( \norm{p} = \abs{\inner{x}{y}}/\norm{y} \).
:::
:::

*Try it first (ten minutes): for \( x = (3, 1) \) and \( y = (1, 1) \) we minimized \( \norm{x - ty}^2 \) by completing the square in \( t \). Do the same for general \( x \) and \( y \ne 0 \): expand \( \norm{x - ty}^2 \) as a quadratic in \( t \) and complete the square.*

::: {.idea}
The attempt succeeds. Expanding gives \( \norm{y}^2 t^2 - 2\inner{x}{y} t + \norm{x}^2 \), and completing the square gives (b) with \( \norm{x}^2 - \inner{x}{y}^2/\norm{y}^2 \) as the constant term. What it does not show is **why** the minimum sits at \( t_0 \), or what the constant term means. The scratch work answers both, as in @exm-method-subtract-the-projection: the error at \( t_0 \) is orthogonal to \( y \), and Pythagoras turns the split \( x - ty = (x - p) + (t_0 - t)y \) into the identity. The constant term is then \( \norm{x - p}^2 \), the squared distance to the line.

*Before reading on: in (a), why is \( t_0 \) the only such \( t \)? Which hypothesis does that use?*
:::

::: {.proof}
Since \( y \ne 0 \), \( \norm{y}^2 = \inner{y}{y} > 0 \). In particular \( \norm{y}^2 \ne 0 \), so \( t_0 \) is defined.

(a) Let \( t \in \nR \). By linearity in the first slot,
\[
\inner{x - ty}{y} = \inner{x}{y} - t\inner{y}{y} = \inner{x}{y} - t\norm{y}^2 .
\]
This is \( 0 \) if and only if \( t\norm{y}^2 = \inner{x}{y} \). Since \( \norm{y}^2 \ne 0 \), this holds if and only if \( t = t_0 \). So \( x - t_0 y = x - p \) is orthogonal to \( y \), and no other \( t \) has this property.

(b) Let \( t \in \nR \). By the vector space laws,
\[
x - ty = (x - p) + (t_0 - t) y .
\]
By (a) and linearity, \( \inner{x - p}{(t_0 - t)y} = (t_0 - t)\inner{x - p}{y} = 0 \), so the two pieces are orthogonal. Pythagoras (@prp-pythagoras-rn) and the rule \( \norm{cv} = \abs{c}\,\norm{v} \) give
\[
\norm{x - ty}^2 = \norm{x - p}^2 + \abs{t_0 - t}^2 \norm{y}^2 = \norm{x - p}^2 + (t - t_0)^2 \norm{y}^2 ,
\]
where \( \abs{t_0 - t}^2 = (t_0 - t)^2 = (t - t_0)^2 \). The last term is a product of two non-negative reals, so it is \( \ge 0 \). Hence \( \norm{x - ty}^2 \ge \norm{x - p}^2 \). The last term is \( 0 \) if and only if \( (t - t_0)^2 = 0 \), because \( \norm{y}^2 \ne 0 \) and a field has no zero divisors. That is, it is \( 0 \) if and only if \( t = t_0 \), since a non-zero real has a positive square. Both lengths are non-negative, and for non-negative numbers comparing squares compares the numbers. So \( \norm{x - ty} \ge \norm{x - p} \), with equality exactly when the squares are equal, that is, when \( t = t_0 \).

(c) Take \( t = 0 \) in (b): \( \norm{x}^2 = \norm{x - p}^2 + t_0^2 \norm{y}^2 \). Since \( p = t_0 y \), \( \norm{p} = \abs{t_0}\,\norm{y} \), so \( \norm{p}^2 = t_0^2\norm{y}^2 \), which gives the first claim. For the second, \( \abs{t_0} = \abs{\inner{x}{y}}/\norm{y}^2 \), since \( \norm{y}^2 > 0 \). Hence \( \norm{p} = \abs{\inner{x}{y}}\,\norm{y}/\norm{y}^2 = \abs{\inner{x}{y}}/\norm{y} \). This proves the theorem.

::: {.uses}
@prp-norm-basic-rn (a)–(c) (rules for lengths); @prp-dot-product-laws-rn (b), (c) (linearity, positivity); @def-orthogonal-rn, @prp-vector-space-laws-rn, @exm-method-expand-the-square (comparing squares). @fd3:prp-absolute-value-ordered-field (b) (products, squares); @fd3:prp-ordered-ring-rules (b), (e) (sums, non-zero squares); @fd3:lem-field-fraction-rules (d) (no zero divisors).
:::
:::

Why is \( t_0 \) the only such \( t \)? By (a), \( x - ty \perp y \) is the linear equation \( t\norm{y}^2 = \inner{x}{y} \), with exactly one solution because \( \norm{y}^2 \ne 0 \). Without \( y \ne 0 \) the theorem fails: for \( y = 0 \) every \( t \) gives the same distance \( \norm{x} \), so the nearest point is not unique in \( t \).

Part (b) says more than "\( p \) is nearest": it measures exactly what a wrong \( t \) costs.

**Alternatively.** Part (c) says \( \norm{p} \le \norm{x} \), that is, \( \inner{x}{y}^2/\norm{y}^2 \le \norm{x}^2 \). Multiplying by \( \norm{y}^2 > 0 \) gives \( \inner{x}{y}^2 \le \norm{x}^2\norm{y}^2 \). That is the Cauchy–Schwarz inequality (@thm-cauchy-schwarz-rn (a)) again, by a second route. More is true: (c) gives
\[
\norm{x}^2\norm{y}^2 - \inner{x}{y}^2 = \norm{y}^2 \, \norm{x - p}^2 ,
\]
so the gap between the two sides of Cauchy–Schwarz is a squared distance, scaled by \( \norm{y}^2 \). Equality holds exactly when \( x = p \), that is, when \( x \) lies on the line through \( y \). Exercise C1 of Section 9.5 (@exr-cauchy-schwarz-and-the-triangle-inequality-c1) turns this route into a complete second proof of Cauchy–Schwarz with its equality case.

::: {#exm-distance-to-a-line-through-the-origin}
[Distance to a line through the origin]

Find the point of the line \( \{ ty : t \in \nR \} \) nearest to \( x \), and the distance from \( x \) to the line:

::: {.enumerate options="label=(\alph*)"}
1. \( x = (3, 1) \), \( y = (1, 1) \);
2. \( x = (1, 2, 3) \), \( y = (1, 1, 1) \); also write \( \norm{x - ty}^2 \) for every \( t \).
:::
:::

::: {.solution}
We subtract the projection, as in @exm-method-subtract-the-projection, and use the theorem just proved.

(a) \( \inner{x}{y} = 3 + 1 = 4 \) and \( \norm{y}^2 = 2 \), so \( t_0 = 2 \) and \( p = (2, 2) \). Then \( x - p = (1, -1) \), and indeed \( \inner{(1, -1)}{(1, 1)} = 0 \). The distance is \( \norm{x - p} = \sqrt{1 + 1} = \sqrt 2 \), as the completed square at the start of the section found.

(b) \( \inner{x}{y} = 1 + 2 + 3 = 6 \) and \( \norm{y}^2 = 3 \), so \( t_0 = 2 \) and \( p = (2, 2, 2) \). Then \( x - p = (-1, 0, 1) \); its dot product with \( (1, 1, 1) \) is \( -1 + 0 + 1 = 0 \), and \( \norm{x - p}^2 = 2 \). By the theorem's (b), for every \( t \),
\[
\norm{x - ty}^2 = 2 + 3(t - 2)^2 .
\]
So the nearest point is \( (2, 2, 2) \) and the distance is \( \sqrt 2 \). As a check, at \( t = 0 \) the formula gives \( 2 + 12 = 14 = 1 + 4 + 9 = \norm{x}^2 \).

Lines that do not pass through the origin need one more step, a translation; Chapter 10 takes them up.

::: {.uses}
@thm-projection-closest-point.
:::
:::

::: {.warning}
\( \operatorname{proj}_y x \) is a **vector**; \( \inner{x}{y}/\norm{y} \) is a **number**. The two are easily confused, because the number is, up to sign, the length of the vector (@thm-projection-closest-point (c)). They also behave differently when \( y \) is rescaled. For \( x = (3, 1) \): with \( y = (1, 1) \) the number is \( 4/\sqrt 2 = 2\sqrt 2 \), and with \( y = (-1, -1) \) it is \( -2\sqrt 2 \), while the projection is \( (2, 2) \) both times.
:::

## The cosine of an angle

The projection splits \( x \) into a piece along \( y \) and a piece orthogonal to it. In the plane picture, \( x \), \( p \) and the origin are the corners of a right triangle, and school trigonometry would call \( \norm{p}/\norm{x} \) the cosine of the angle at the origin, "adjacent over hypotenuse". With the sign of \( t_0 \) kept, so that the cosine is negative when \( p \) points away from \( y \), that ratio is
\[
\frac{t_0 \norm{y}}{\norm{x}} = \frac{\inner{x}{y}}{\norm{y}^2} \cdot \frac{\norm{y}}{\norm{x}} = \frac{\inner{x}{y}}{\norm{x}\,\norm{y}} .
\]
The picture is motivation only. The expression on the right is defined in any \( \nR^n \) as soon as \( x \ne 0 \) and \( y \ne 0 \), and Cauchy–Schwarz already tells us it lies between \( -1 \) and \( 1 \). Before naming it, compute it on a few cases where the answer is guessable.

::: {.check}
Let \( x = (1, 1, 0) \). Compute \( \inner{x}{y}/(\norm{x}\norm{y}) \) for \( y = x \), for \( y = -x \), and for \( y = (1, -1, 0) \).
:::

::: {.solution}
\( \norm{x} = \sqrt 2 \). For \( y = x \): \( \inner{x}{x} = 2 \), so the ratio is \( 2/(\sqrt 2 \sqrt 2) = 1 \). For \( y = -x \): \( \inner{x}{-x} = -2 \) and \( \norm{-x} = \sqrt 2 \), so the ratio is \( -1 \). For \( y = (1, -1, 0) \): \( \inner{x}{y} = 1 - 1 + 0 = 0 \), so the ratio is \( 0 \). Same direction gives \( 1 \), opposite directions give \( -1 \), and orthogonal vectors give \( 0 \), as the school cosine of \( 0 \), of a straight angle and of a right angle would.
:::

::: {#def-angle-cosine-rn}
[Cosine of the Angle between Two Vectors]

Let \( x, y \in \nR^n \) with \( x \ne 0 \) **and** \( y \ne 0 \). The **cosine of the angle** between \( x \) and \( y \) is the real number
\[
\cos\angle(x, y) \coloneqq \frac{\inner{x}{y}}{\norm{x}\,\norm{y}} .
\]
:::

*The cosine of the angle is the dot product of the two directions.*

In words: divide the dot product by both lengths. The symbol \( \cos\angle(x, y) \) is read as **one** symbol, a function of the pair \( (x, y) \). It is **not** the function \( \cos \) applied to a number \( \angle(x, y) \): this chapter defines no angle \( \angle(x, y) \) at all, and \( \angle \) alone means nothing here.

**Well-definedness.** Both lengths are positive, because \( x \ne 0 \) and \( y \ne 0 \) (@prp-norm-basic-rn (a)), so the quotient exists. Its value lies in \( [-1, 1] \). Indeed, Cauchy–Schwarz (@thm-cauchy-schwarz-rn (a)) gives \( \abs{\inner{x}{y}} \le \norm{x}\norm{y} \). Dividing by \( \norm{x}\norm{y} > 0 \) gives \( \abs{\cos\angle(x, y)} \le 1 \), that is, \( -1 \le \cos\angle(x, y) \le 1 \), by the rule for absolute values in an ordered field (*Number Systems: From \( \nN \) to \( \nR \)*, @fd3:prp-absolute-value-ordered-field (d)). Without Cauchy–Schwarz, we would not know that this number lies between \( -1 \) and \( 1 \), as a cosine should.

The computation before the definition gives the first examples: \( \cos\angle(x, x) = 1 \), \( \cos\angle(x, -x) = -1 \), and \( \cos\angle(x, y) = 0 \) for orthogonal non-zero \( x, y \).

**When one vector is zero.** Keep \( x = (1, 1, 0) \) and replace \( y \) by \( 0 \). The dot product is still \( 0 \), but the quotient \( 0/0 \) is not defined. The zero vector has no direction, and this is why the definition requires \( y \ne 0 \). In particular, "\( \cos\angle(x, y) = 0 \)" and "\( x \perp y \)" are not the same statement: the second allows a zero vector, the first does not.

**Why this definition.** Dividing by **both** lengths makes the number see only directions, as part (b) below shows. Dividing by one length, or by none, would let the size of \( x \) or \( y \) change the answer.

The properties below are what the name promises.

::: {#prp-angle-cosine-properties}
[Properties of the Cosine of an Angle]

Let \( x, y \in \nR^n \) be non-zero.

::: {.enumerate options="label=(\alph*)"}
1. \( \cos\angle(x, y) = \cos\angle(y, x) \), and \( \cos\angle(x, y) = \bigl\langle x/\norm{x}, \, y/\norm{y} \bigr\rangle \).
2. For all \( a, b \in \nR \) with \( ab \ne 0 \): \( \cos\angle(ax, by) = \cos\angle(x, y) \) if \( ab > 0 \), and \( \cos\angle(ax, by) = -\cos\angle(x, y) \) if \( ab < 0 \).
3. \( \cos\angle(x, y) = 1 \) if and only if \( y = cx \) for some \( c > 0 \); \( \cos\angle(x, y) = -1 \) if and only if \( y = cx \) for some \( c < 0 \); and \( \cos\angle(x, y) = 0 \) if and only if \( x \perp y \).
4. *(Law of cosines.)* \( \norm{x - y}^2 = \norm{x}^2 + \norm{y}^2 - 2\norm{x}\,\norm{y}\cos\angle(x, y) \).
:::
:::

::: {.idea}
Part (a) is the method of normalizing (@exm-method-normalize) in reverse: the cosine is the dot product of the unit vectors \( x/\norm{x} \) and \( y/\norm{y} \). Rescaling \( x \) or \( y \) by a non-zero factor changes the unit vector at most by a sign, which is (b). Part (c) is the equality case of Cauchy–Schwarz, and (d) is one expansion of a square.
:::

::: {.proof}
(a) The first claim is the symmetry of the dot product. By linearity in each slot, \( \inner{x/\norm{x}}{y/\norm{y}} = \inner{x}{y}/(\norm{x}\norm{y}) \).

(b) Here \( ax \ne 0 \) and \( by \ne 0 \) (@prp-vector-space-laws-rn (j)), so the left side is defined. By linearity and the rule \( \norm{cv} = \abs{c}\,\norm{v} \),
\[
\cos\angle(ax, by) = \frac{ab\inner{x}{y}}{\abs{a}\norm{x}\,\abs{b}\norm{y}} = \frac{ab}{\abs{ab}}\cos\angle(x, y) ,
\]
using \( \abs{a}\abs{b} = \abs{ab} \). If \( ab > 0 \) then \( \abs{ab} = ab \) and the factor is \( 1 \). If \( ab < 0 \) then \( \abs{ab} = -ab \) and the factor is \( -1 \).

(c) Multiplying by \( \norm{x}\norm{y} > 0 \), \( \cos\angle(x, y) = 1 \) if and only if \( \inner{x}{y} = \norm{x}\norm{y} \). By the equality case of Cauchy–Schwarz (@thm-cauchy-schwarz-rn (c)), this holds if and only if \( x = 0 \) or \( y = cx \) with \( c \ge 0 \). Since \( x \ne 0 \), it holds if and only if \( y = cx \) with \( c \ge 0 \). Also \( c \ne 0 \) because \( y \ne 0 \), so \( c > 0 \). The case \( -1 \) is the same argument with \( \inner{x}{y} = -\norm{x}\norm{y} \) and part (c′) of the same theorem, which gives \( c \le 0 \), hence \( c < 0 \). Finally \( \cos\angle(x, y) = 0 \) if and only if \( \inner{x}{y} = 0 \), that is, \( x \perp y \).

(d) Expand the square (@exm-method-expand-the-square): \( \norm{x - y}^2 = \norm{x}^2 - 2\inner{x}{y} + \norm{y}^2 \), and \( \inner{x}{y} = \norm{x}\norm{y}\cos\angle(x, y) \) by the definition.

::: {.uses}
@prp-dot-product-laws-rn (a), (b) (symmetry, linearity); @prp-norm-basic-rn (b) (length of a multiple); @def-orthogonal-rn. @fd3:prp-absolute-value-ordered-field (b) (\( \abs{a}\abs{b} = \abs{ab} \)).
:::
:::

Part (d) is the law of cosines of school trigonometry, now with no triangle and no angle in it: the "angle" is replaced by its cosine, and the cosine by a quotient of dot products. When \( x \perp y \) it is Pythagoras again. Part (b) says that the cosine depends only on the two lines through \( x \) and \( y \), and on whether each vector points along its line or against it.

::: {#exm-angles-computed}
[Cosines of angles]

Compute:

::: {.enumerate options="label=(\alph*)"}
1. \( \cos\angle((1, 0), (1, 1)) \);
2. \( \cos\angle((1, 2, 2), (2, -1, 2)) \);
3. three cosines in the unit cube \( [0, 1]^3 \), with a corner at the origin. First, between the body diagonal \( (1, 1, 1) \) and the edge \( e_1 \). Second, between the two body diagonals \( (1, 1, 1) \) and \( (1, 1, -1) \); the second runs from the corner \( (0, 0, 1) \) to the corner \( (1, 1, 0) \). Third, between the body diagonal and the face diagonal \( (1, 1, 0) \).
:::
:::

::: {.solution}
(a) The dot product is \( 1 \), and the lengths are \( 1 \) and \( \sqrt 2 \), so the cosine is \( 1/\sqrt 2 \).

(b) The dot product is \( 2 - 2 + 4 = 4 \), and both lengths are \( \sqrt{1 + 4 + 4} = 3 \), so the cosine is \( 4/9 \).

(c) \( \norm{(1, 1, 1)} = \sqrt 3 \). Against \( e_1 \): the dot product is \( 1 \) (@prp-dot-product-laws-rn (d)), so the cosine is \( 1/\sqrt 3 \). Between the body diagonals: the dot product is \( 1 + 1 - 1 = 1 \), and both lengths are \( \sqrt 3 \), so the cosine is \( 1/3 \). Against the face diagonal: the dot product is \( 2 \) and \( \norm{(1, 1, 0)} = \sqrt 2 \), so the cosine is \( 2/(\sqrt 3\sqrt 2) = 2/\sqrt 6 = \sqrt 6/3 \).

Each answer is a cosine and nothing more. We do not convert any of them into an angle, because that needs the function \( \cos \) itself.

::: {.uses}
@lem-root-rules (a) (root of a product).
:::
:::

::: {.check}
What is \( \cos\angle((1, 1), (-1, -1)) \)? Answer first with @prp-angle-cosine-properties, then by computing.
:::

::: {.solution}
\( (-1, -1) = c(1, 1) \) with \( c = -1 < 0 \), so the cosine is \( -1 \) by (c). Computing: the dot product is \( -2 \), and both lengths are \( \sqrt 2 \), so the cosine is \( -2/2 = -1 \).
:::

::: {.remark}
[Looking ahead: the angle itself]

An angle \( \theta \) with \( \cos\theta = \cos\angle(x, y) \) needs the function \( \cos \), which this book only borrows through five facts (@ax-cosine-sine). Those facts give such a \( \theta \) for any \( n \). Let \( c = \cos\angle(x, y) \). Then \( c^2 \le 1 \), so the point \( \bigl(c, \sqrt{1 - c^2}\bigr) \) has squared coordinates adding up to \( 1 \). Every such point is \( (\cos\theta, \sin\theta) \) for some \( \theta \), (T4). No proof in this chapter uses \( \theta \). For \( n = 2 \) and non-zero \( z, w \in \nC \), the number \( \conj{z}w/(\abs{z}\abs{w}) \) has modulus \( 1 \), so its polar form is \( \cos\theta + i\sin\theta \) (@prp-polar-form). Here \( \cos\theta = \cos\angle(z, w) \), by @prp-plane-is-complex-plane. The sign of \( \sin\theta \) records which way one turns from \( z \) to \( w \), and \( \cos\angle \) cannot see it. Next, Chapter 10 uses the projection to find nearest points on lines and on hyperplanes.
:::

## Exercises

### A. Check your understanding

::: {#exr-projection-and-angle-a1}
[A1]

These questions are about @thm-projection-closest-point and its proof.

::: {.enumerate options="label=(\alph*)"}
1. Why does the theorem assume \( y \ne 0 \)? What goes wrong for \( y = 0 \)?
2. Where in the proof of (b) is \( x - p \perp y \) used?
3. Check the identity of (b) for \( x = (1, 2, 3) \), \( y = (1, 1, 1) \), at \( t = 0 \) and at \( t = 1 \).
4. Compute \( \operatorname{proj}_{(1, 2, 2)} (3, 0, 0) \), and check that the error is orthogonal to \( (1, 2, 2) \).
5. State the idea of the proof of (b) in two sentences.
:::
:::

::: {.solution}
(a) The definition of \( t_0 \) divides by \( \norm{y}^2 \), which is \( 0 \) exactly when \( y = 0 \). For \( y = 0 \) the statement also fails: every \( ty \) is \( 0 \), so \( \norm{x - ty} = \norm{x} \) for **every** \( t \), and the minimizing \( t \) is not unique.

(b) In applying Pythagoras to \( x - ty = (x - p) + (t_0 - t)y \): Pythagoras needs the two pieces orthogonal, and \( \inner{x - p}{(t_0 - t)y} = (t_0 - t)\inner{x - p}{y} = 0 \) uses (a). In the terms of @exm-method-expand-the-square, it makes the cross term zero.

(c) Here \( t_0 = 2 \), \( p = (2, 2, 2) \), \( \norm{x - p}^2 = 2 \) and \( \norm{y}^2 = 3 \). At \( t = 0 \): \( \norm{x}^2 = 1 + 4 + 9 = 14 \) and \( 2 + (0 - 2)^2 \cdot 3 = 14 \). At \( t = 1 \): \( \norm{x - y}^2 = \norm{(0, 1, 2)}^2 = 5 \) and \( 2 + (1 - 2)^2 \cdot 3 = 5 \).

(d) \( \inner{(3, 0, 0)}{(1, 2, 2)} = 3 \) and \( \norm{(1, 2, 2)}^2 = 9 \), so the projection is \( \tfrac13 (1, 2, 2) = (1/3, 2/3, 2/3) \). The error is \( (8/3, -2/3, -2/3) \), and its dot product with \( (1, 2, 2) \) is \( 8/3 - 4/3 - 4/3 = 0 \).

(e) Choose \( t_0 \) so that the error \( x - t_0 y \) is orthogonal to \( y \). Then any other \( x - ty \) is that error plus a multiple of \( y \), and Pythagoras shows the extra multiple can only add length.
:::

### B. Practice

::: {#exr-projection-and-angle-b1}
[B1: The median identity]

Let \( x, y, z \in \nR^n \) and \( m \coloneqq \tfrac12 (x + y) \). Prove that
\[
\norm{x - z}^2 + \norm{y - z}^2 = \tfrac12 \norm{x - y}^2 + 2\norm{z - m}^2 .
\]
You are given the first half:
\[
x - z = (x - m) + (m - z) , \qquad y - z = -(x - m) + (m - z) ,
\]
where the second holds because \( y - m = \tfrac12(y - x) = -(x - m) \).

*Say which method this is, then complete it.*
:::

::: {.solution}
The method is **expand the square** (@exm-method-expand-the-square). Write \( a \coloneqq x - m \) and \( b \coloneqq m - z \). Then
\[
\begin{aligned}
\norm{x - z}^2 &= \norm{a + b}^2 = \norm{a}^2 + 2\inner{a}{b} + \norm{b}^2 , \\
\norm{y - z}^2 &= \norm{-a + b}^2 = \norm{a}^2 - 2\inner{a}{b} + \norm{b}^2 ,
\end{aligned}
\]
using \( \norm{-a} = \norm{a} \) (@prp-norm-basic-rn (b)) and linearity for \( \inner{-a}{b} = -\inner{a}{b} \). Adding, the cross terms cancel: the sum is \( 2\norm{a}^2 + 2\norm{b}^2 \). Finally \( a = x - m = \tfrac12(x - y) \), so \( 2\norm{a}^2 = 2 \cdot \tfrac14 \norm{x - y}^2 = \tfrac12\norm{x - y}^2 \) by @prp-norm-basic-rn (b), and \( \norm{b} = \norm{z - m} \). This proves the identity. It is the parallelogram law (@prp-parallelogram-law-rn) applied to \( a \) and \( b \), read as a statement about a triangle \( x, y, z \) and the midpoint \( m \) of one side.
:::

::: {#exr-projection-and-angle-b2}
[B2: Prove or disprove]

Let \( x, y, z \in \nR^n \) with \( y \ne 0 \). Prove or disprove each statement.

::: {.enumerate options="label=(\alph*)"}
1. \( \operatorname{proj}_y (\operatorname{proj}_y x) = \operatorname{proj}_y x \).
2. \( \operatorname{proj}_y (x + z) = \operatorname{proj}_y x + \operatorname{proj}_y z \).
3. \( \operatorname{proj}_{cy} x = \operatorname{proj}_y x \) for every \( c \in \nR \) with \( c \ne 0 \).
4. \( \norm{\operatorname{proj}_y x} \le \norm{x} \).
5. \( \operatorname{proj}_y x = \operatorname{proj}_x y \) for all non-zero \( x, y \).
6. If \( x \perp y \), then \( \operatorname{proj}_y x = 0 \).
:::
:::

::: {.solution}
Write \( t_0 = \inner{x}{y}/\norm{y}^2 \).

(a) **True.** \( \operatorname{proj}_y x = t_0 y \), and \( \operatorname{proj}_y (t_0 y) = (\inner{t_0 y}{y}/\norm{y}^2)\,y = (t_0\norm{y}^2/\norm{y}^2)\,y = t_0 y \), by linearity. A point on the line is its own projection.

(b) **True.** By linearity, \( \inner{x + z}{y} = \inner{x}{y} + \inner{z}{y} \); divide by \( \norm{y}^2 \) and multiply by \( y \), using the distributive law (h) of @prp-vector-space-laws-rn.

(c) **True.** \( cy \ne 0 \) because \( c \ne 0 \) and \( y \ne 0 \) (@prp-vector-space-laws-rn (j)). Then \( \inner{x}{cy} = c\inner{x}{y} \) and \( \norm{cy}^2 = c^2\norm{y}^2 \), so
\[
\operatorname{proj}_{cy} x = \frac{c\inner{x}{y}}{c^2\norm{y}^2}\, cy = \frac{c^2\inner{x}{y}}{c^2\norm{y}^2}\, y = \operatorname{proj}_y x .
\]

(d) **True.** By @thm-projection-closest-point (c), \( \norm{x}^2 = \norm{p}^2 + \norm{x - p}^2 \ge \norm{p}^2 \), and both lengths are non-negative, so \( \norm{p} \le \norm{x} \).

(e) **False.** Take \( x = (1, 0) \) and \( y = (1, 1) \). Then \( \operatorname{proj}_y x = \tfrac12 (1, 1) = (1/2, 1/2) \), while \( \operatorname{proj}_x y = 1 \cdot (1, 0) = (1, 0) \). The first lies on the line of \( y \), the second on the line of \( x \).

(f) **True.** \( x \perp y \) means \( \inner{x}{y} = 0 \), so \( t_0 = 0 \) and \( \operatorname{proj}_y x = 0y = 0 \) (@prp-vector-space-laws-rn (i)).
:::

::: {#exr-projection-and-angle-b3}
[B3]

::: {.enumerate options="label=(\alph*)"}
1. Find the point of the line \( \{ t(2, 1, -2) : t \in \nR \} \) nearest to \( (1, 1, 1) \), and the distance from \( (1, 1, 1) \) to the line.
2. Let \( v, y \in \nR^n \) with \( y \ne 0 \). Show that there are at most two real numbers \( t \) with \( \norm{v + ty} = 1 \).
:::
:::

::: {.solution}
(a) With \( x = (1, 1, 1) \) and \( y = (2, 1, -2) \): \( \inner{x}{y} = 2 + 1 - 2 = 1 \) and \( \norm{y}^2 = 4 + 1 + 4 = 9 \), so \( t_0 = 1/9 \), and the nearest point is \( p = (2/9, 1/9, -2/9) \) (@thm-projection-closest-point (b)). By (c) of the theorem,
\[
\norm{x - p}^2 = \norm{x}^2 - \norm{p}^2 = 3 - \frac{1}{9} = \frac{26}{9} ,
\]
since \( \norm{p}^2 = \inner{x}{y}^2/\norm{y}^2 = 1/9 \). The distance is \( \sqrt{26}/3 \). As a check, \( x - p = (7/9, 8/9, 11/9) \), with \( (49 + 64 + 121)/81 = 234/81 = 26/9 \), and \( \inner{x - p}{y} = (14 + 8 - 22)/9 = 0 \).

(b) Suppose \( \norm{v + ty} = 1 \). Squaring and expanding (@exm-method-expand-the-square),
\[
\norm{y}^2 t^2 + 2\inner{v}{y}\, t + \norm{v}^2 - 1 = 0 .
\]
Consider the polynomial \( f \coloneqq \norm{y}^2 x^2 + 2\inner{v}{y}\, x + (\norm{v}^2 - 1) \) in \( \nR[x] \), with the indeterminate \( x \) of Chapters 6 and 7. Its coefficient of \( x^2 \) is \( \norm{y}^2 \ne 0 \), since \( y \ne 0 \), so \( f \ne 0 \) and \( \deg f = 2 \) (@def-degree). By @thm-evaluation-respects-operations, the value \( f(t) \) is the left side of the display, so every \( t \) with \( \norm{v + ty} = 1 \) is a root of \( f \) in \( \nR \). By @thm-polynomial-root-count, \( f \) has at most \( 2 \) distinct roots. Hence there are at most two such \( t \). (Geometrically: a line meets a sphere of radius \( 1 \) in at most two points.)
:::

### C. Going deeper

::: {#exr-projection-and-angle-c1}
[C1: Chapter check: the projection theorem]

Let \( x, y \in \nR^n \) with \( y \ne 0 \). Prove that exactly one \( t \in \nR \) minimizes \( \norm{x - ty} \), that this \( t \) is \( t_0 = \inner{x}{y}/\norm{y}^2 \), and that \( x - t_0 y \perp y \). Write the proof from the definitions and the results of Sections 9.2–9.4, without quoting @thm-projection-closest-point.
:::

::: {.solution}
[Hint 1]

Look for the \( t \) that makes the error \( x - ty \) orthogonal to \( y \).
:::

::: {.solution}
[Hint 2]

For an arbitrary \( t \), compare \( x - ty \) with \( x - t_0 y \): what is their difference?
:::

::: {.solution}
Since \( y \ne 0 \), \( \norm{y}^2 = \inner{y}{y} > 0 \), so \( t_0 \) is defined. By linearity,
\[
\inner{x - t_0 y}{y} = \inner{x}{y} - t_0\norm{y}^2 = \inner{x}{y} - \inner{x}{y} = 0 ,
\]
so \( x - t_0 y \perp y \). Let \( t \in \nR \). Then \( x - ty = (x - t_0 y) + (t_0 - t)y \), and \( \inner{x - t_0 y}{(t_0 - t)y} = (t_0 - t) \cdot 0 = 0 \). By Pythagoras and the rule \( \norm{cv} = \abs{c}\,\norm{v} \),
\[
\norm{x - ty}^2 = \norm{x - t_0 y}^2 + (t - t_0)^2\norm{y}^2 .
\]
The last term is \( \ge 0 \), and it is \( 0 \) only if \( t = t_0 \), because \( \norm{y}^2 > 0 \) and a square of a non-zero real is positive. So \( \norm{x - ty}^2 \ge \norm{x - t_0 y}^2 \) for every \( t \), with equality only at \( t = t_0 \). Lengths are non-negative, so the same holds for the lengths themselves. Hence \( t_0 \) minimizes \( \norm{x - ty} \), and every \( t \ne t_0 \) gives a strictly larger value, so the minimizer is unique.

Completing the square in \( t \) is an acceptable second route for the identity: \( \norm{x - ty}^2 = \norm{y}^2 t^2 - 2\inner{x}{y}t + \norm{x}^2 = \norm{y}^2(t - t_0)^2 + \norm{x}^2 - \inner{x}{y}^2/\norm{y}^2 \). It receives the points for the identity, minimality and uniqueness; the orthogonality must still be checked separately.

**What a complete answer needs.** (10 points)

- 2: finds \( t_0 \) from the orthogonality condition (or states it), and justifies dividing by \( \norm{y}^2 \) through \( y \ne 0 \).
- 2: verifies \( x - t_0 y \perp y \).
- 3: proves the identity \( \norm{x - ty}^2 = \norm{x - t_0 y}^2 + (t - t_0)^2\norm{y}^2 \) for **every** \( t \) (by Pythagoras or by completing the square).
- 2: deduces minimality and uniqueness, using \( \norm{y}^2 > 0 \) for the strict inequality when \( t \ne t_0 \).
- 1: concludes, passing from squares to lengths with non-negativity.

**Slips that lose the step** (0 for the step):

- a division by \( \norm{y}^2 \) with no mention of \( y \ne 0 \);
- derivatives, which are not available in this book;
- "the vertex of a parabola is the minimum" without the identity that proves it.

::: {.uses}
@prp-dot-product-laws-rn (b), (c) (linearity, positivity); @prp-vector-space-laws-rn; @prp-pythagoras-rn; @prp-norm-basic-rn (b) (length of a multiple). @fd3:prp-ordered-ring-rules (e), (g) (non-zero squares, comparing squares).
:::
:::

::: {#exr-projection-and-angle-c2}
[C2: The distance to a line in the plane]

Let \( x, y \in \nR^n \) with \( y \ne 0 \), and \( p = \operatorname{proj}_y x \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that
\[
\norm{y}^2\,\norm{x - p}^2 = \frac12 \sum_{j=1}^{n} \sum_{k=1}^{n} (x_j y_k - x_k y_j)^2 .
\]
2. Deduce that for \( n = 2 \) the distance from \( x \) to the line \( \{ ty : t \in \nR \} \) is \( \abs{x_1 y_2 - x_2 y_1}/\norm{y} \).
:::
:::

::: {.solution}
[Hint 1]

Both sides of (a) are equal to the same third expression, which involves only \( \norm{x} \), \( \norm{y} \) and \( \inner{x}{y} \).
:::

::: {.solution}
[Hint 2]

For (a), start from \( \norm{x - p}^2 = \norm{x}^2 - \norm{p}^2 \) and multiply by \( \norm{y}^2 \). For (b), list the four terms of the double sum when \( n = 2 \).
:::

::: {.solution}
(a) By @thm-projection-closest-point (c), \( \norm{x - p}^2 = \norm{x}^2 - \norm{p}^2 = \norm{x}^2 - \inner{x}{y}^2/\norm{y}^2 \). Multiplying by \( \norm{y}^2 \),
\[
\norm{y}^2\,\norm{x - p}^2 = \norm{x}^2\norm{y}^2 - \inner{x}{y}^2 .
\]
By Lagrange's identity (@exr-cauchy-schwarz-and-the-triangle-inequality-c2), the right side is \( \tfrac12 \sum_j \sum_k (x_j y_k - x_k y_j)^2 \), since \( \norm{x}^2 = \sum_k x_k^2 \), \( \norm{y}^2 = \sum_k y_k^2 \) and \( \inner{x}{y} = \sum_k x_k y_k \).

(b) For \( n = 2 \), the terms with \( j = k \) are \( (x_j y_j - x_j y_j)^2 = 0 \). The terms with \( (j, k) = (1, 2) \) and \( (2, 1) \) are \( (x_1y_2 - x_2y_1)^2 \) and \( (x_2y_1 - x_1y_2)^2 \), which are equal. So the right side of (a) is \( \tfrac12 \cdot 2(x_1y_2 - x_2y_1)^2 = (x_1y_2 - x_2y_1)^2 \). By @thm-projection-closest-point (b), the distance from \( x \) to the line is \( \norm{x - p} \). Taking non-negative square roots gives \( \norm{y}\,\norm{x - p} = \abs{x_1y_2 - x_2y_1} \), since \( \sqrt{a^2} = \abs{a} \) and the root of a product is the product of the roots. Dividing by \( \norm{y} > 0 \) gives the claim. For \( x = (3, 1) \) and \( y = (1, 1) \) it gives \( \abs{3 - 1}/\sqrt 2 = \sqrt 2 \), as in @exm-distance-to-a-line-through-the-origin.

The number \( \abs{x_1y_2 - x_2y_1} \) is the base \( \norm{y} \) times the height \( \norm{x - p} \): in the picture, the area of the parallelogram spanned by \( x \) and \( y \). Area is not defined in this book; later volumes meet this number again as a determinant.

::: {.uses}
@thm-projection-closest-point (b); @prp-modulus-of-real (\( \sqrt{a^2} = \abs{a} \)); @lem-root-rules (a) (root of a product).
:::
:::

### R. Review

::: {#exr-projection-and-angle-r1}
[R1]

Let \( x, y \in \nR^n \) with \( y \ne 0 \), let \( t_0 = \inner{x}{y}/\norm{y}^2 \), let \( p \coloneqq t_0 y \), and let \( g(t) \coloneqq \norm{x - ty} \) for \( t \in \nR \). Prove that \( g \) is strictly increasing on \( [t_0, \infty) \).
:::

::: {.solution}
Let \( t_0 \le s < t \). By @thm-projection-closest-point (b), \( g(t)^2 = \norm{x - p}^2 + (t - t_0)^2\norm{y}^2 \), and likewise for \( s \). Factoring out \( t - s \) (@exm-method-factor-difference) gives
\[
\begin{aligned}
g(t)^2 - g(s)^2 &= \bigl( (t - t_0)^2 - (s - t_0)^2 \bigr) \norm{y}^2 \\
&= (t - s)(t + s - 2t_0)\,\norm{y}^2 .
\end{aligned}
\]
Here \( t - s > 0 \) and \( \norm{y}^2 > 0 \). Also \( t + s - 2t_0 = (t - t_0) + (s - t_0) > 0 \), since \( t - t_0 > 0 \) and \( s - t_0 \ge 0 \). The sum is strict because one summand is. So \( g(s)^2 < g(t)^2 \). Both \( g(s) \) and \( g(t) \) are non-negative, so \( g(s) < g(t) \). This is the definition of strictly increasing on \( [t_0, \infty) \) (@def-monotone-function). By the same factorization, \( g \) is strictly decreasing on \( (-\infty, t_0] \).

::: {.uses}
@fd3:prp-ordered-ring-rules (b), (g) (strict sums, comparing squares).
:::
:::

::: {#exr-projection-and-angle-r2}
[R2]

Fix \( a \in \nR^n \), and define \( \varphi \colon \nR^n \to \nR \) by \( \varphi(x) \coloneqq \inner{a}{x} \). Show that \( \varphi \) is a homomorphism from \( (\nR^n, +) \) to \( (\nR, +) \), find its kernel, and decide for which \( a \) and \( n \) it is injective.
:::

::: {.solution}
The brackets here are the dot product of @def-dot-product-rn, not a subgroup generated by an element.

\( (\nR^n, +) \) is a group (@def-group). Associativity, the identity \( 0 \) and the inverse \( -x \) are laws (a), (c) and (d) of @prp-vector-space-laws-rn, and law (b) makes it abelian. So is \( (\nR, +) \). By linearity of the dot product, \( \varphi(x + y) = \inner{a}{x + y} = \inner{a}{x} + \inner{a}{y} = \varphi(x) + \varphi(y) \), so \( \varphi \) is a homomorphism (@def-group-homomorphism). Its kernel is \( \{ x : \inner{a}{x} = 0 \} = \{ x : x \perp a \} \).

If \( a = 0 \), the kernel is all of \( \nR^n \). Let \( a \ne 0 \). If \( n = 1 \), \( \varphi(x) = ax \), and \( ax = 0 \) forces \( x = 0 \); the kernel is \( \{0\} \). If \( n \ge 2 \), the kernel contains a non-zero vector: if \( a_1 \ne 0 \), take \( v = a_2 e_1 - a_1 e_2 \), with \( \inner{a}{v} = a_1a_2 - a_2a_1 = 0 \) and second coordinate \( -a_1 \ne 0 \); if \( a_1 = 0 \), take \( e_1 \), with \( \inner{a}{e_1} = a_1 = 0 \). By @prp-homomorphism-injective-iff-kernel-trivial, \( \varphi \) is injective if and only if \( n = 1 \) and \( a \ne 0 \).

::: {.uses}
@prp-dot-product-laws-rn (b) (linearity).
:::
:::

::: {#exr-projection-and-angle-r3}
[R3]

Let \( z, w \in \nC \) with \( z \ne 0 \). Prove that \( z\conj{w} \) is a non-negative real number if and only if \( w = cz \) for some real \( c \ge 0 \).
:::

::: {.solution}
\( (\Leftarrow) \) If \( w = cz \) with \( c \in \nR \), \( c \ge 0 \), then \( \conj{c} = c \), because the imaginary part of \( c \) is \( 0 \). So by @thm-conjugate-properties (b) and (c), \( z\conj{w} = z\,\conj{c}\,\conj{z} = c\abs{z}^2 \), a non-negative real.

\( (\Rightarrow) \) Let \( z\conj{w} = r \) with \( r \in \nR \), \( r \ge 0 \). By @thm-conjugate-properties (a) and (b), \( w\conj{z} = \conj{z\conj{w}} = \conj{r} = r \). Since \( z \ne 0 \), \( \abs{z}^2 = z\conj{z} \ne 0 \) (@thm-conjugate-properties (c), (e)), so
\[
w = \frac{w\conj{z}}{z\conj{z}}\, z = \frac{r}{\abs{z}^2}\, z .
\]
With \( c \coloneqq r/\abs{z}^2 \), a non-negative real, \( w = cz \). The product of the real number \( c = (c, 0) \) with \( z \) in \( \nC \) is the scalar multiple \( cz \) in \( \nR^2 \), by @prp-plane-is-complex-plane (a).

Chapter 3 found the first condition as the equality case of \( \abs{z + w} \le \abs{z} + \abs{w} \) (@exr-triangle-inequality-b1). Then @thm-triangle-inequality-rn (a) found the second, "\( z = 0 \) or \( w = cz \) with \( c \ge 0 \)", for \( n = 2 \). For \( z \ne 0 \) this exercise shows the two conditions agree, and for \( z = 0 \) both hold. So the two chapters' equality cases are one statement.

::: {.uses}
@def-conjugate-modulus (conjugate of a real).
:::
:::

::: {#exr-projection-and-angle-r4}
[R4]

Find all \( x \in \nR^n \) with \( \displaystyle\sum_{k=1}^n x_k = n \) and \( \displaystyle\sum_{k=1}^n x_k^2 = n \).
:::

::: {.solution}
The only solution is \( x = (1, 1, \dots, 1) \). It works, since both sums are \( n \). Let \( w \coloneqq (1, 1, \dots, 1) \in \nR^n \), so \( \norm{w} = \sqrt n \). The two conditions say \( \inner{w}{x} = n \) and \( \norm{x} = \sqrt n \). By Cauchy–Schwarz (@thm-cauchy-schwarz-rn (a)),
\[
n = \inner{w}{x} \le \norm{w}\,\norm{x} = \sqrt n \sqrt n = n ,
\]
so equality holds: \( \inner{w}{x} = \norm{w}\norm{x} \). By @thm-cauchy-schwarz-rn (c), \( w = 0 \) or \( x = cw \) with \( c \ge 0 \); since \( w \ne 0 \), \( x = cw \). Then \( \sum x_k = nc = n \), so \( c = 1 \) and \( x = w \).

A second route expands a square (@exm-method-expand-the-square): \( \norm{x - w}^2 = \norm{x}^2 - 2\inner{x}{w} + \norm{w}^2 = n - 2n + n = 0 \). So \( x = w \), because only the zero vector has length \( 0 \) (@prp-norm-basic-rn (a)).

The tool is Cauchy–Schwarz with its equality case, because each condition mixes all the coordinates. The look-alike tool, working coordinatewise (@exm-method-coordinatewise), finds nothing to hold on to: neither condition says anything about a single \( x_k \).
:::

<!-- dependency ledger
thm-projection-closest-point (proof): for p, q >= 0, p <= q iff p^2 <= q^2, and p = q iff p^2 = q^2 | fd3:prp-ordered-ring-rules (g) with trichotomy, as written out in prose in Section 3.3 ("Comparing squares") and as step (1) of exm-method-expand-the-square (cited, Uses line)
thm-projection-closest-point (proof): a^2 = 0 iff a = 0 | fd3:prp-ordered-ring-rules (e) (cited, Uses line); fd3:lem-field-fraction-rules (d) (cited, Uses line)
thm-projection-closest-point (proof): a product of non-negative reals is non-negative | fd3:prp-ordered-ring-rules (c), and the zero case
thm-projection-closest-point (proof): x - ty = (x - p) + (t0 - t)y | prp-vector-space-laws-rn (cited as a whole, Uses line)
thm-projection-closest-point (claim): (Alternatively) multiplying an inequality by ||y||^2 > 0; equality iff x = p (the parallel-vector details are left to exr-cauchy-schwarz-and-the-triangle-inequality-c1) | fd3:prp-ordered-ring-rules (c); thm-projection-closest-point (c); def-parallel-rn remark (Section 9.2) used in Section 9.5 C1
def-projection-rn (example): ||e_k|| = 1 | prp-norm-basic-rn (e) (cited)
def-projection-rn (claim): ||y||^2 > 0 iff y != 0 | prp-dot-product-laws-rn (c), prp-norm-basic-rn (c) (cited)
def-projection-rn (example): (3, 1) with y = (1, 1) under division by ||y||: 4 - 4 sqrt 2 != 0 | verify/ch09/def-projection-rn.py
def-angle-cosine-rn (claim): |c| <= 1 after dividing |<x, y>| <= ||x|| ||y|| by a positive number | fd3:prp-ordered-ring-rules (c) and fd3:prp-absolute-value-ordered-field (b), (d)
prp-angle-cosine-properties (proof): |ab| = ab for ab > 0, -ab for ab < 0 | fd3:def-absolute-value-ordered-field
prp-angle-cosine-properties (proof): part (c') of thm-cauchy-schwarz-rn | Section 9.5 (labelled part of thm-cauchy-schwarz-rn; letter as delivered there)
exm-angles-computed (solution): sqrt 3 sqrt 2 = sqrt 6, 2/sqrt 6 = sqrt 6/3 | lem-root-rules (a) (cited, Uses line); verify/ch09/exm-angles-computed.py
def-angle-cosine-rn (claim): (Looking ahead box) conj(z) w/(|z||w|) has modulus 1; its real part is <z, w>/(|z||w|) | thm-conjugate-properties (d), prp-plane-is-complex-plane (b) with Re of a conjugate; Re(u/r) = Re(u)/r for real r > 0 by def-complex-numbers; prose only, nothing depends on it
def-angle-cosine-rn (claim): (Looking ahead box) polar angle determined up to 2 pi Z | prp-polar-form (b) (cited)
def-angle-cosine-rn (claim): (Looking ahead box) theta with cos theta = c exists for any n: c^2 = |c|^2 <= 1 from |c| <= 1 (well-definedness), sqrt(1 - c^2) exists as 1 - c^2 >= 0, and c^2 + (1 - c^2) = 1, so (T4) applies | def-angle-cosine-rn (|c| <= 1, claim above), fd3:prp-cof-square-roots, fd3:prp-ordered-ring-rules (c), ax-cosine-sine (T4); prose only, nothing depends on it
exr-projection-and-angle-b3 (solution): ||v + ty|| = 1 implies ||v + ty||^2 = 1 | squaring an equation
exr-projection-and-angle-b3 (solution): coefficient form of f gives deg f = 2 | def-degree (cited); def-polynomial-ring
thm-projection-closest-point (proof): norm-basic (a)-(c), dot-product-laws (b), (c), def-orthogonal-rn, fd3:prp-absolute-value-ordered-field (b) | moved from prose to the Uses line (cited)
prp-angle-cosine-properties (proof): dot-product-laws (a), (b), norm-basic (b), fd3:prp-absolute-value-ordered-field (b), def-orthogonal-rn | moved from prose to the Uses line (cited)
exr-projection-and-angle-c1 (solution): dot-product-laws (b), (c), prp-vector-space-laws-rn, prp-pythagoras-rn, norm-basic (b), fd3:prp-ordered-ring-rules (e), (g) | moved from prose to the Uses line (cited)
exr-projection-and-angle-r2 (solution): dot-product-laws (b) | moved from prose to the Uses line (cited)
exm-distance-to-a-line-through-the-origin (solution): thm-projection-closest-point | moved from prose to the Uses line (cited)
exr-projection-and-angle-c2 (solution): sqrt(ab) = sqrt a sqrt b for a, b >= 0 | lem-root-rules (a) (cited)
exr-projection-and-angle-c2 (solution): Lagrange's identity | exr-cauchy-schwarz-and-the-triangle-inequality-c2 (cited; exercise cited by an exercise, STYLE §6)
exr-projection-and-angle-r1 (solution): exm-method-factor-difference and def-monotone-function | ch08 (cited)
exr-projection-and-angle-r2 (solution): n = 1: ax = 0 with a != 0 forces x = 0 | fd3:lem-field-fraction-rules (d)
exr-projection-and-angle-r3 (solution): conj(c) = c for real c; z conj(z) = |z|^2 != 0 for z != 0, division in C | def-conjugate-modulus (cited, Uses line), thm-conjugate-properties (c), (e) (cited); C is a field (Chapter 3)
exr-projection-and-angle-r4 (solution): ||w|| = sqrt n for w = (1, ..., 1); sqrt n sqrt n = n | def-norm-rn; fd3:prp-cof-square-roots
-->
