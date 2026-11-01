# Cauchy–Schwarz and the Triangle Inequality

Section 9.4 gave \( \nR^n \) a length and a distance and proved every basic property of the distance except one: that a detour through a third point is never shorter than the direct route. This section proves it. The work goes into a single inequality between the dot product and the lengths, the Cauchy–Schwarz inequality, and the method that proves it, **normalize**, is the chapter's third named move.

## Two earlier proofs, and why neither transfers

The triangle inequality has been proved twice before in this series. Each proof used a tool that \( \nR^n \) lacks.

**In \( \nR \).** *Number Systems: From \(\nN\) to \(\nR\)*, Section 4.1 trapped each number between \( \pm \) its absolute value, \( -\abs{x} \le x \le \abs{x} \), and added the two traps (@fd3:prp-absolute-value-ordered-field (c)–(e)). The trap compares \( x \) with the number \( \abs{x} \). For a vector \( x \in \nR^n \) with \( n \ge 2 \), "\( x \le \norm{x} \)" compares a vector with a number, and \( \nR^n \) has been given no order at all.

**In \( \nC = \nR^2 \).** Section 3.3 expanded \( \abs{z + w}^2 \) and met the cross term \( 2\operatorname{Re}(z\conj{w}) \), which it bounded by \( \abs{z\conj{w}} = \abs{z}\abs{w} \) (@thm-complex-triangle-inequality). By @prp-plane-is-complex-plane, \( \operatorname{Re}(z\conj{w}) = \inner{z}{w} \) and \( \abs{z} = \norm{z} \), so the key step was
\[
\inner{z}{w} \le \norm{z} \, \norm{w} ,
\]
proved with the multiplication of \( \nC \): the product \( z\conj{w} \) and the rule \( \abs{z\conj{w}} = \abs{z}\abs{w} \). For \( n \ge 3 \) this book defines no such multiplication on \( \nR^n \).

The expansion itself does survive. By the method of @exm-method-expand-the-square, compare squares, expanding with @eq-expand-norm-squared:
\[
\norm{x + y}^2 = \norm{x}^2 + 2\inner{x}{y} + \norm{y}^2 , \qquad
\bigl( \norm{x} + \norm{y} \bigr)^2 = \norm{x}^2 + 2\norm{x}\,\norm{y} + \norm{y}^2 .
\]
Everything matches except the cross terms. So the triangle inequality in \( \nR^n \) rests on one inequality, \( \inner{x}{y} \le \norm{x}\,\norm{y} \), and that inequality now needs a proof that uses only the laws of the dot product.

**An attempt that stalls.** Work coordinatewise: \( x_k y_k \le \abs{x_k}\,\abs{y_k} \) for each \( k \), and \( \abs{x_k} \le \norm{x} \), \( \abs{y_k} \le \norm{y} \) by @prp-norm-coordinate-bounds (a). Adding the \( n \) bounds gives
\[
\inner{x}{y} \le \sum_{k=1}^{n} \abs{x_k}\,\abs{y_k} \le n \, \norm{x} \, \norm{y} ,
\]
which is off by the factor \( n \). Try \( x = y = (1, \dots, 1) \): then \( \inner{x}{y} = n \) and \( \norm{x}\,\norm{y} = n \), so the inequality we want holds with equality, while the attempt only gives \( n \le n^2 \). Each bound \( \abs{x_k} \le \norm{x} \) is sharp only when all of \( x \) sits in coordinate \( k \), and the \( n \) bounds cannot all be sharp at once. A coordinate-by-coordinate bound loses the geometry. The proof below uses the length of a whole vector instead.

## The Cauchy–Schwarz inequality

We state the inequality together with its equality cases. Part (c′) is the mirror image of (c); Section 9.6 needs it for angles.

::: {#thm-cauchy-schwarz-rn}
[Cauchy–Schwarz Inequality]

Let \( n \ge 1 \) and \( x, y \in \nR^n \).

(a) \( \abs{\inner{x}{y}} \le \norm{x}\,\norm{y} \).

(b) \( \abs{\inner{x}{y}} = \norm{x}\,\norm{y} \) if and only if \( x \) and \( y \) are parallel.

(c) \( \inner{x}{y} = \norm{x}\,\norm{y} \) if and only if \( x = 0 \) or \( y = cx \) for some real \( c \ge 0 \).

(c′) \( \inner{x}{y} = -\norm{x}\,\norm{y} \) if and only if \( x = 0 \) or \( y = cx \) for some real \( c \le 0 \).
:::

*Try it first (ten minutes): for unit vectors \( u, v \), expand \( \norm{u - v}^2 \ge 0 \). What does it say about \( \inner{u}{v} \)? What else could you expand?*

::: {.idea}
[Scratch work]

The attempt gives \( 0 \le \norm{u - v}^2 = 1 - 2\inner{u}{v} + 1 \), so \( \inner{u}{v} \le 1 \): one half of the goal for unit vectors, and nothing yet about general \( x, y \). For general vectors the same expansion gives only \( 2\inner{x}{y} \le \norm{x}^2 + \norm{y}^2 \), whose right side equals \( 2\norm{x}\,\norm{y} \) only when \( \norm{x} = \norm{y} \). So we make the lengths equal, to \( 1 \), and pay for it by scaling back.

| Givens | Goal |
|---|---|
| \( x, y \in \nR^n \) | \( \abs{\inner{x}{y}} \le \norm{x}\,\norm{y} \) |
| \( x, y \ne 0 \) (if one is \( 0 \), both sides are \( 0 \)); \( u \coloneqq x/\norm{x} \), \( v \coloneqq y/\norm{y} \) are unit vectors | \( \abs{\inner{u}{v}} \le 1 \), because both sides of the old goal are \( \norm{x}\,\norm{y} \) times those of the new one |
| \( \norm{u - v}^2 = 2 - 2\inner{u}{v} \ge 0 \) | \( -1 \le \inner{u}{v} \le 1 \); the upper half is done |
| \( \norm{u + v}^2 = 2 + 2\inner{u}{v} \ge 0 \) | the lower half is done: the gap closes |

The second row is allowed because the statement is **homogeneous**: replacing \( x \) by \( ax \) with \( a > 0 \) multiplies both sides by \( a \), and likewise for \( y \). For the equality cases, ask when \( \norm{u - v}^2 \) or \( \norm{u + v}^2 \) is \( 0 \).

*Before reading on: where is \( x \ne 0 \) used, and why are both expansions needed?*
:::

::: {.proof}
Let \( x, y \in \nR^n \).

(a) If \( x = 0 \) or \( y = 0 \), then \( \inner{x}{y} = 0 \) by @prp-dot-product-laws-rn (e), with (a) there when \( x = 0 \), and \( \norm{x}\,\norm{y} = 0 \) since \( \norm{0} = 0 \) (@prp-norm-basic-rn (a)); so (a) reads \( 0 \le 0 \).

Let \( x \ne 0 \) and \( y \ne 0 \). Then \( \norm{x} > 0 \) and \( \norm{y} > 0 \) by @prp-norm-basic-rn (a), so \( u \coloneqq (1/\norm{x})\,x \) and \( v \coloneqq (1/\norm{y})\,y \) are unit vectors (@def-unit-vector-rn), and \( x = \norm{x}\,u \), \( y = \norm{y}\,v \) by @prp-vector-space-laws-rn (e), (f). By @prp-dot-product-laws-rn (a), (b),
\[
\inner{x}{y} = \norm{x}\,\norm{y} \, \inner{u}{v} .
\]{#eq-cauchy-schwarz-normalized}
By @eq-expand-norm-squared and @prp-norm-basic-rn (c),
\[
\begin{aligned}
0 &\le \norm{u - v}^2 = \norm{u}^2 - 2\inner{u}{v} + \norm{v}^2 = 2 - 2\inner{u}{v} , \\
0 &\le \norm{u + v}^2 = 2 + 2\inner{u}{v} .
\end{aligned}
\]
Adding \( 2\inner{u}{v} \), resp. \( -2 \), and multiplying by \( \tfrac12 > 0 \) (@fd3:prp-ordered-ring-rules (b), (c)) gives \( -1 \le \inner{u}{v} \le 1 \), that is, \( \abs{\inner{u}{v}} \le 1 \) (@fd3:prp-absolute-value-ordered-field (d)). Multiplying by \( \norm{x}\,\norm{y} > 0 \) and using @eq-cauchy-schwarz-normalized with \( \abs{ab} = \abs{a}\,\abs{b} \) (@fd3:prp-absolute-value-ordered-field (b)), \( \abs{\inner{x}{y}} = \norm{x}\,\norm{y}\,\abs{\inner{u}{v}} \le \norm{x}\,\norm{y} \).

(c) \( (\Leftarrow) \) If \( x = 0 \), both sides are \( 0 \). If \( y = cx \) with \( c \ge 0 \), then \( \inner{x}{y} = c\inner{x}{x} = c\norm{x}^2 \), and \( \norm{x}\,\norm{cx} = \abs{c}\,\norm{x}^2 = c\norm{x}^2 \) by @prp-norm-basic-rn (b), (c).

\( (\Rightarrow) \) If \( x = 0 \) we are done, and if \( y = 0 \), then \( y = 0x \) with \( c = 0 \). Otherwise \( x, y \ne 0 \), and with \( u, v \) as in (a), @eq-cauchy-schwarz-normalized gives \( \norm{x}\,\norm{y}\,\inner{u}{v} = \norm{x}\,\norm{y} \), so \( \inner{u}{v} = 1 \) after cancelling the non-zero factor. Then \( \norm{u - v}^2 = 2 - 2 = 0 \), so \( \norm{u - v} = 0 \) (@fd3:prp-ordered-ring-rules (e)) and \( u = v \) (@prp-norm-basic-rn (a)). Hence \( y = \norm{y}\,u = c x \) with \( c \coloneqq \norm{y}/\norm{x} > 0 \).

(c′) By @prp-dot-product-laws-rn (b) and @prp-norm-basic-rn (b) with \( c = -1 \), \( \inner{x}{-y} = -\inner{x}{y} \) and \( \norm{-y} = \norm{y} \). So \( \inner{x}{y} = -\norm{x}\,\norm{y} \) holds if and only if \( \inner{x}{-y} = \norm{x}\,\norm{-y} \). By (c) applied to \( x \) and \( -y \), this holds if and only if \( x = 0 \) or \( -y = cx \) with \( c \ge 0 \), that is, \( y = (-c)x \) with \( -c \le 0 \).

(b) Since \( \norm{x}\,\norm{y} \ge 0 \), the definition of the absolute value (@fd3:def-absolute-value-ordered-field) gives \( \abs{\inner{x}{y}} = \norm{x}\,\norm{y} \) if and only if \( \inner{x}{y} = \pm\norm{x}\,\norm{y} \). By (c) and (c′) this holds if and only if \( x = 0 \) or \( y = cx \) for some real \( c \). By the remark after @def-parallel-rn, that is exactly the statement that \( x \) and \( y \) are parallel: \( 0 \) is parallel to every vector, and for \( x \ne 0 \), \( y \) is parallel to \( x \) if and only if \( y = cx \) for some \( c \). This proves the theorem.
:::

For \( n = 1 \) the theorem says little: \( \abs{xy} = \abs{x}\,\abs{y} \) always, and any two reals are parallel. The content is in \( n \ge 2 \), where most pairs of vectors are not parallel and the inequality is strict for them.

::: {.check}
For \( x = (1, 2, 2) \) and \( y = (2, 0, 1) \), compute both sides of (a). Is the inequality strict, and does (b) predict the answer?
:::

::: {.solution}
\( \inner{x}{y} = 2 + 0 + 2 = 4 \), \( \norm{x} = 3 \) and \( \norm{y} = \sqrt 5 \). Since \( 4^2 = 16 < 45 = (3\sqrt5)^2 \) and both numbers are non-negative, \( 4 < 3\sqrt5 \): strict. Yes: \( y = cx \) would need \( c = 2 \) from the first coordinate and \( c = 0 \) from the second, and \( x = cy \) is impossible since \( y_2 = 0 \ne 2 = x_2 \); so \( x \), \( y \) are not parallel and (b) forbids equality.
:::

Squaring (a) gives the form used for sums of real numbers.

::: {#cor-cauchy-schwarz-sums}
[Cauchy–Schwarz Inequality for Sums]

Let \( n \ge 1 \) and \( x_1, \dots, x_n, y_1, \dots, y_n \in \nR \). Then
\[
\Bigl( \sum_{k=1}^{n} x_k y_k \Bigr)^2 \le \Bigl( \sum_{k=1}^{n} x_k^2 \Bigr) \Bigl( \sum_{k=1}^{n} y_k^2 \Bigr) ,
\]
with equality if and only if \( (x_1, \dots, x_n) \) and \( (y_1, \dots, y_n) \) are parallel vectors of \( \nR^n \).
:::

::: {.proof}
Let \( x \coloneqq (x_1, \dots, x_n) \) and \( y \coloneqq (y_1, \dots, y_n) \). The three sums are \( \inner{x}{y} \), \( \norm{x}^2 \) and \( \norm{y}^2 \) (@def-dot-product-rn, @prp-norm-basic-rn (c)). By @thm-cauchy-schwarz-rn (a), \( 0 \le \abs{\inner{x}{y}} \le \norm{x}\,\norm{y} \), so @fd3:prp-ordered-field-halves (d) gives \( \abs{\inner{x}{y}}^2 \le \norm{x}^2 \norm{y}^2 \), and \( \abs{\inner{x}{y}}^2 = \inner{x}{y}^2 \) by @fd3:prp-absolute-value-ordered-field (b). Two non-negative reals with equal squares are equal (comparing squares, Section 9.4), so equality holds exactly when \( \abs{\inner{x}{y}} = \norm{x}\,\norm{y} \), that is, by @thm-cauchy-schwarz-rn (b), when \( x \) and \( y \) are parallel.
:::

For example, with \( (1, 2, 3) \) and \( (4, 5, 6) \) the corollary reads \( 32^2 = 1024 \le 14 \cdot 77 = 1078 \), strict because the two triples are not parallel. This is the form in which the analysis volumes quote the inequality. Exercise C2 below proves it a second way, from Lagrange's identity. For \( n = 2 \) that identity reads \( (ac + bd)^2 + (ad - bc)^2 = (a^2 + b^2)(c^2 + d^2) \), the identity behind the second route in the marking scheme of Chapter 3's exit check @exr-triangle-inequality-c1.

## The method: normalize

The proof of @thm-cauchy-schwarz-rn did its work for unit vectors and then scaled back. That move has a name.

::: {#exm-method-normalize}
[Method: normalize]

**Template.** Suppose a statement about \( x \) and \( y \) is **homogeneous**: replacing \( x \) by \( ax \) with \( a > 0 \) multiplies both sides by the same positive factor, and likewise for \( y \). Then (1) settle \( x = 0 \) and \( y = 0 \) separately; (2) for \( x, y \ne 0 \), put \( u \coloneqq x/\norm{x} \) and \( v \coloneqq y/\norm{y} \) and prove the statement for the unit vectors \( u \), \( v \); (3) scale back, multiplying by the positive factor.

**When to use it.** Inequalities between \( \inner{x}{y} \) and products of lengths; statements about directions rather than sizes.

**The usual failures.** Normalizing \( 0 \), which has no direction (\( x/\norm{x} \) divides by \( 0 \)). Scaling by a negative factor: \( x \mapsto -x \) changes the sign of \( \inner{x}{y} \) but not of \( \norm{x}\,\norm{y} \). A statement that is not homogeneous: \( \norm{u + v} \le 2 \) holds for all unit \( u, v \), and yet \( \norm{x + y} \le 2 \) fails for \( x = y = 2e_1 \).
:::

The proof of @thm-cauchy-schwarz-rn is the first worked example: steps (1), (2) and (3) are its zero case, its expansions of \( \norm{u \mp v}^2 \), and the multiplication by \( \norm{x}\,\norm{y} \). Here is a second.

::: {#exm-cauchy-schwarz-applications}
[Two uses of Cauchy–Schwarz]

(a) Show that \( (a + b + c)^2 \le 3(a^2 + b^2 + c^2) \) for all real \( a, b, c \), with equality if and only if \( a = b = c \).

(b) Find the largest value of \( 2x_1 + 3x_2 - x_3 \) over all unit vectors \( x \in \nR^3 \), and every unit vector where it is attained.
:::

::: {.solution}
(a) Apply @cor-cauchy-schwarz-sums to \( (a, b, c) \) and \( w \coloneqq (1, 1, 1) \): the left side is \( (a + b + c)^2 \) and the right side is \( (a^2 + b^2 + c^2) \cdot 3 \). Equality holds if and only if \( (a, b, c) \) is parallel to \( w \). Since \( w \ne 0 \), the remark after @def-parallel-rn turns this into \( (a, b, c) = tw \) for some \( t \), that is, \( a = b = c \).

(b) Let \( p \coloneqq (2, 3, -1) \), so the expression is \( \inner{p}{x} \) and \( \norm{p} = \sqrt{14} \). The statement \( \inner{p}{x} \le \sqrt{14}\,\norm{x} \) is homogeneous in \( x \), so by normalizing it is enough to look at unit \( x \), which is what the question does. For unit \( x \), @thm-cauchy-schwarz-rn (a) and @fd3:prp-absolute-value-ordered-field (c) give
\[
\inner{p}{x} \le \abs{\inner{p}{x}} \le \norm{p}\,\norm{x} = \sqrt{14} .
\]
The value \( \sqrt{14} \) is attained at \( x_0 \coloneqq p/\sqrt{14} \), a unit vector, since \( \inner{p}{x_0} = 14/\sqrt{14} = \sqrt{14} \) (because \( \sqrt{14} \cdot \sqrt{14} = 14 \)). Conversely, if \( \inner{p}{x} = \sqrt{14} = \norm{p}\,\norm{x} \), then @thm-cauchy-schwarz-rn (c), with \( p \ne 0 \) in the first place, gives \( x = cp \) with \( c \ge 0 \); then \( 1 = \norm{x} = c\sqrt{14} \), so \( c = 1/\sqrt{14} \) and \( x = x_0 \). The largest value is \( \sqrt{14} \), attained only at \( (2, 3, -1)/\sqrt{14} \). Scaling back, \( 2x_1 + 3x_2 - x_3 \le \sqrt{14}\,\norm{x} \) for every \( x \in \nR^3 \).
:::

## The triangle inequality

With the cross term under control, the expansion at the start of the section finishes the job.

::: {#thm-triangle-inequality-rn}
[Triangle Inequality for Vectors]

Let \( x, y, z \in \nR^n \).

::: {.enumerate options="label=(\alph*)"}
1. \( \norm{x + y} \le \norm{x} + \norm{y} \), with equality if and only if \( x = 0 \) or \( y = cx \) for some real \( c \ge 0 \).
2. \( \bigl| \norm{x} - \norm{y} \bigr| \le \norm{x - y} \).
3. \( d(x, z) \le d(x, y) + d(y, z) \).
:::
:::

::: {.idea}
As in @exm-method-expand-the-square: compare squares, expand, and bound the cross term \( 2\inner{x}{y} \) by \( 2\norm{x}\,\norm{y} \), now with Cauchy–Schwarz. Parts (b) and (c) are (a) applied to well-chosen vectors.

*Before reading on: which equality case of @thm-cauchy-schwarz-rn does the equality case of (a) use, and why not (b)?*
:::

::: {.proof}
(a) By @eq-expand-norm-squared, @fd3:prp-absolute-value-ordered-field (c) and @thm-cauchy-schwarz-rn (a), with @fd3:prp-ordered-ring-rules (b) to add the inequalities,
\[
\begin{aligned}
\norm{x + y}^2 &= \norm{x}^2 + 2\inner{x}{y} + \norm{y}^2 \\
&\le \norm{x}^2 + 2\abs{\inner{x}{y}} + \norm{y}^2 \\
&\le \norm{x}^2 + 2\norm{x}\,\norm{y} + \norm{y}^2 = \bigl( \norm{x} + \norm{y} \bigr)^2 .
\end{aligned}
\]
Both \( \norm{x + y} \) and \( \norm{x} + \norm{y} \) are non-negative, so comparing squares (Section 9.4) gives \( \norm{x + y} \le \norm{x} + \norm{y} \). For the same reason the two lengths are equal if and only if their squares are, that is, comparing the first and last expressions of the display, if and only if \( 2\inner{x}{y} = 2\norm{x}\,\norm{y} \). By @thm-cauchy-schwarz-rn (c), this holds if and only if \( x = 0 \) or \( y = cx \) with \( c \ge 0 \).

(b) This follows from (a) exactly as @cor-complex-triangle-variants (a) followed from @thm-complex-triangle-inequality, with \( \norm{\cdot} \) in place of \( \abs{\cdot} \): (a) applied to \( x = (x - y) + y \) gives \( \norm{x} - \norm{y} \le \norm{x - y} \); exchanging \( x \) and \( y \) gives \( \norm{y} - \norm{x} \le \norm{y - x} \); \( \norm{y - x} = \norm{x - y} \) by @prp-norm-basic-rn (b) with \( c = -1 \); and @fd3:prp-absolute-value-ordered-field (d) combines the two bounds.

(c) By @prp-vector-space-laws-rn, \( x - z = (x - y) + (y - z) \), so by (a) and @def-distance-rn, \( d(x, z) = \norm{(x - y) + (y - z)} \le \norm{x - y} + \norm{y - z} = d(x, y) + d(y, z) \). This proves the theorem.
:::

The equality case of (a) uses @thm-cauchy-schwarz-rn (c), not (b): the first inequality of the display is an equality only when \( \inner{x}{y} \ge 0 \), so a negative \( \inner{x}{y} \) with \( \abs{\inner{x}{y}} = \norm{x}\,\norm{y} \) still leaves a gap.

::: {.warning}
"Equality in Cauchy–Schwarz holds for parallel vectors, and the triangle inequality comes from Cauchy–Schwarz, so parallel vectors give \( \norm{x + y} = \norm{x} + \norm{y} \)." The conclusion is false. For \( x = e_1 \) and \( y = -e_1 \), which are parallel, \( \norm{x + y} = 0 \) and \( \norm{x} + \norm{y} = 2 \). The argument forgets the step \( \inner{x}{y} \le \abs{\inner{x}{y}} \), which is strict whenever \( \inner{x}{y} < 0 \).
:::

For \( n = 2 \), @prp-plane-is-complex-plane (c) turns (a) into @thm-complex-triangle-inequality, proved here by a route with no complex multiplication. Chapter 3 found its equality case in a different form, \( z\conj{w} \) a non-negative real (@exr-triangle-inequality-b1); Section 9.6 returns to the comparison in a review exercise.

::: {.check}
Let \( x = (1, -2, 3) \) and \( y = -2x \). Is \( \abs{\inner{x}{y}} = \norm{x}\,\norm{y} \)? Is \( \norm{x + y} = \norm{x} + \norm{y} \)?
:::

::: {.solution}
\( \inner{x}{y} = -2 \cdot 14 = -28 \) and \( \norm{x}\,\norm{y} = \sqrt{14} \cdot 2\sqrt{14} = 28 \): yes, as (b) of @thm-cauchy-schwarz-rn predicts for parallel vectors. But \( x + y = -x \), so \( \norm{x + y} = \sqrt{14} \), while \( \norm{x} + \norm{y} = 3\sqrt{14} \): no, since \( y = cx \) with \( c = -2 < 0 \).
:::

## Sums of many vectors

Adding one vector at a time extends (a) to any finite number of terms.

::: {#cor-triangle-finite-sums-rn}
[Triangle Inequality for Finite Sums]

For every \( m \in \nN \) and all \( v_1, \dots, v_m \in \nR^n \),
\[
\Bigl\| \sum_{j=1}^{m} v_j \Bigr\| \le \sum_{j=1}^{m} \norm{v_j} .
\]
:::

::: {.proof}
By induction on \( m \ge 0 \) (@fd2:thm-induction), with the sums defined as in @lem-vector-sums-coordinatewise. For \( m = 0 \) both sides are \( 0 \). If the inequality holds for \( m \), then by the recursion, @thm-triangle-inequality-rn (a) and @fd3:prp-ordered-ring-rules (b),
\[
\Bigl\| \sum_{j=1}^{m+1} v_j \Bigr\| \le \Bigl\| \sum_{j=1}^{m} v_j \Bigr\| + \norm{v_{m+1}} \le \sum_{j=1}^{m+1} \norm{v_j} .
\]
:::

Length and the sum of the absolute values of the coordinates are comparable, with constants \( 1 \) and \( \sqrt n \).

::: {#cor-norm-sum-bound}
[Length against the Sum of the Coordinates]

For every \( x \in \nR^n \),
\[
\norm{x} \le \sum_{k=1}^{n} \abs{x_k} \le \sqrt{n}\,\norm{x} .
\]
:::

::: {.proof}
By @prp-standard-basis-expansion, \( x = \sum_k x_k e_k \), so @cor-triangle-finite-sums-rn and @prp-norm-basic-rn (b), (e) give \( \norm{x} \le \sum_k \norm{x_k e_k} = \sum_k \abs{x_k} \). For the second inequality let \( a \coloneqq (\abs{x_1}, \dots, \abs{x_n}) \) and \( w \coloneqq (1, \dots, 1) \). Then \( \inner{a}{w} = \sum_k \abs{x_k} \), \( \norm{w} = \sqrt n \), and \( \norm{a} = \norm{x} \), because both are non-negative with the same square \( \sum_k x_k^2 \) (@fd3:prp-absolute-value-ordered-field (b), uniqueness in @fd3:prp-cof-square-roots). By @fd3:prp-absolute-value-ordered-field (c) and @thm-cauchy-schwarz-rn (a), \( \sum_k \abs{x_k} \le \abs{\inner{a}{w}} \le \norm{a}\,\norm{w} = \sqrt n \, \norm{x} \).
:::

For \( n = 2 \) the first inequality is the last one of @lem-real-part-at-most-modulus. Both are sharp: \( x = e_1 \) gives equality on the left, and \( x = (1, \dots, 1) \) on the right.

## Exercises

### A. Check your understanding

::: {#exr-cauchy-schwarz-and-the-triangle-inequality-a1}
[A1]

These questions are about the proof of @thm-cauchy-schwarz-rn.

::: {.enumerate options="label=(\alph*)"}
1. Where is \( x \ne 0 \) used?
2. Which expansion gives which half of \( -1 \le \inner{u}{v} \le 1 \)?
3. Run the proof on \( x = (3, 4) \), \( y = (4, 3) \): compute \( u \), \( v \), \( \inner{u}{v} \) and \( \norm{u - v}^2 \).
4. What fails in the third row of the Givens/Goal table if \( u \) is not a unit vector?
5. Give the idea of the proof in two sentences.
:::
:::

::: {.solution}
(a) To form \( u = x/\norm{x} \), which needs \( \norm{x} \ne 0 \), that is, \( x \ne 0 \) (@prp-norm-basic-rn (a)); the zero case is settled separately.

(b) \( \norm{u - v}^2 = 2 - 2\inner{u}{v} \ge 0 \) gives \( \inner{u}{v} \le 1 \); \( \norm{u + v}^2 = 2 + 2\inner{u}{v} \ge 0 \) gives \( \inner{u}{v} \ge -1 \).

(c) \( \norm{x} = \norm{y} = 5 \), \( u = (\tfrac35, \tfrac45) \), \( v = (\tfrac45, \tfrac35) \), \( \inner{u}{v} = \tfrac{24}{25} \), and \( \norm{u - v}^2 = \tfrac1{25} + \tfrac1{25} = \tfrac{2}{25} = 2 - \tfrac{48}{25} \). Scaling back, \( \inner{x}{y} = 25 \cdot \tfrac{24}{25} = 24 \le 25 \).

(d) The expansion becomes \( \norm{u - v}^2 = \norm{u}^2 - 2\inner{u}{v} + \norm{v}^2 \), not \( 2 - 2\inner{u}{v} \), and it only gives \( \inner{u}{v} \le \tfrac12(\norm{u}^2 + \norm{v}^2) \), which exceeds \( \norm{u}\,\norm{v} \) unless \( \norm{u} = \norm{v} \).

(e) The inequality is homogeneous, so after disposing of zero vectors it is enough to prove \( \abs{\inner{u}{v}} \le 1 \) for unit vectors. That follows from \( \norm{u \mp v}^2 = 2 \mp 2\inner{u}{v} \ge 0 \).
:::

### B. Practice

::: {#exr-cauchy-schwarz-and-the-triangle-inequality-b1}
[B1: Proof ordering]

The eight lines below are shuffled. Six of them, in a suitable order, prove @thm-triangle-inequality-rn (b) from (a); the other two belong in no proof. Write an admissible order without rereading the proof above, and say why each of the two other lines fails.

(i) So \( \norm{x} - \norm{y} \le \norm{x - y} \).

(ii) \( \norm{-y} = -\norm{y} \).

(iii) So \( -\norm{x - y} \le \norm{x} - \norm{y} \le \norm{x - y} \), and @fd3:prp-absolute-value-ordered-field (d) gives \( \bigl| \norm{x} - \norm{y} \bigr| \le \norm{x - y} \).

(iv) \( x = (x - y) + y \).

(v) \( \norm{y - x} = \norm{x - y} \), by @prp-norm-basic-rn (b) with \( c = -1 \).

(vi) The same with \( x \) and \( y \) exchanged: \( \norm{y} - \norm{x} \le \norm{y - x} \).

(vii) \( \norm{x - y} \le \norm{x} - \norm{y} \), by (a) applied to \( x \) and \( -y \).

(viii) So \( \norm{x} \le \norm{x - y} + \norm{y} \), by (a).
:::

::: {.solution}
An admissible order is (iv), (viii), (i), (vi), (v), (iii). Line (iv) must precede (viii), (viii) precede (i), and (i) precede (vi), which repeats (iv), (viii), (i) with the letters exchanged; (v) may stand anywhere before (iii), and (iii) comes last, since it uses (i), (vi) and (v).

Line (vii) fails: (a) applied to \( x \) and \( -y \) gives \( \norm{x - y} \le \norm{x} + \norm{-y} = \norm{x} + \norm{y} \), with a plus sign. The claim itself is false: at \( y = -x \ne 0 \) it reads \( 2\norm{x} \le 0 \). Line (ii) is false for every \( y \ne 0 \): by @prp-norm-basic-rn (b), \( \norm{-y} = \abs{-1}\,\norm{y} = \norm{y} > 0 > -\norm{y} \).
:::

::: {#exr-cauchy-schwarz-and-the-triangle-inequality-b2}
[B2]

Prove that \( \norm{x - y} = \norm{x + y} \) if and only if \( x \perp y \). You may start from the two expansions
\[
\norm{x + y}^2 = \norm{x}^2 + 2\inner{x}{y} + \norm{y}^2 , \qquad \norm{x - y}^2 = \norm{x}^2 - 2\inner{x}{y} + \norm{y}^2 .
\]
*Name the move, then complete it.*
:::

::: {.solution}
The move is to expand the square (@exm-method-expand-the-square). Both lengths are non-negative, so they are equal if and only if their squares are (comparing squares, Section 9.4). Subtracting the two expansions, \( \norm{x + y}^2 - \norm{x - y}^2 = 4\inner{x}{y} \). This is \( 0 \) if and only if \( \inner{x}{y} = 0 \) (as \( 4 \ne 0 \) in \( \nR \), @fd3:lem-field-fraction-rules (d)), that is, if and only if \( x \perp y \) (@def-orthogonal-rn).
:::

::: {#exr-cauchy-schwarz-and-the-triangle-inequality-b3}
[B3: Prove or disprove]

For each statement about all \( x, y \in \nR^n \) (or all unit vectors \( u, v \)), prove it or give a counterexample.

::: {.enumerate options="label=(\alph*)"}
1. \( \inner{x}{y} \le \tfrac12 \bigl( \norm{x}^2 + \norm{y}^2 \bigr) \).
2. \( \norm{x + y} \ge \norm{x} \).
3. Unit vectors \( u, v \) with \( \inner{u}{v} = 1 \) are equal.
4. Equality \( \abs{\inner{x}{y}} = \norm{x}\,\norm{y} \) holds only when \( x = y \).
5. \( \inner{x}{y} \le \tfrac12 \norm{x}\,\norm{y} \).
:::
:::

::: {.solution}
(a) **True.** \( 0 \le \norm{x - y}^2 = \norm{x}^2 - 2\inner{x}{y} + \norm{y}^2 \); add \( 2\inner{x}{y} \) and halve.

(b) **False.** For \( x = e_1 \), \( y = -e_1 \): \( \norm{x + y} = 0 < 1 = \norm{x} \).

(c) **True.** \( \norm{u - v}^2 = 2 - 2 \cdot 1 = 0 \), so \( u - v = 0 \) by @prp-norm-basic-rn (a).

(d) **False.** For \( x = e_1 \), \( y = 2e_1 \): \( \abs{\inner{x}{y}} = 2 = 1 \cdot 2 \), and \( x \ne y \).

(e) **False.** For \( x = y = e_1 \) it reads \( 1 \le \tfrac12 \). The statement is homogeneous, so normalizing is legitimate here: it reduces the claim to "\( \inner{u}{v} \le \tfrac12 \) for unit \( u, v \)", which fails at \( u = v \).
:::

::: {#exr-cauchy-schwarz-and-the-triangle-inequality-b4}
[B4]

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \bigl( \sum_{k=1}^{n} x_k \bigr)^2 \le n \sum_{k=1}^{n} x_k^2 \) for real \( x_1, \dots, x_n \), with equality if and only if all \( x_k \) are equal.
2. Find the smallest value of \( \norm{x}^2 \) over all \( x \in \nR^3 \) with \( x_1 + 2x_2 + 2x_3 = 9 \), and every \( x \) where it is attained.
:::
:::

::: {.solution}
(a) Apply @cor-cauchy-schwarz-sums to \( x \) and \( w \coloneqq (1, \dots, 1) \), with \( \sum_k 1^2 = n \). Equality holds if and only if \( x \) is parallel to \( w \ne 0 \), that is (remark after @def-parallel-rn), \( x = tw \) for some \( t \): all \( x_k \) are equal.

(b) Let \( p \coloneqq (1, 2, 2) \), so \( \norm{p} = 3 \) and the condition is \( \inner{p}{x} = 9 \). By @thm-cauchy-schwarz-rn (a), \( 9 \le \norm{p}\,\norm{x} = 3\norm{x} \), so \( \norm{x} \ge 3 \) and \( \norm{x}^2 \ge 9 \) (@fd3:prp-ordered-field-halves (d)). If \( \norm{x}^2 = 9 \), then \( \norm{x} = 3 \) and \( \inner{p}{x} = 9 = \norm{p}\,\norm{x} \), so \( x = cp \) with \( c \ge 0 \) by @thm-cauchy-schwarz-rn (c); the condition gives \( 9c = 9 \), so \( x = (1, 2, 2) \). This point satisfies the condition, \( 1 + 4 + 4 = 9 \), and \( \norm{(1, 2, 2)}^2 = 9 \). The smallest value is \( 9 \), attained only at \( (1, 2, 2) \).
:::

### C. Going deeper

::: {#exr-cauchy-schwarz-and-the-triangle-inequality-c1}
[C1: Exit check: Cauchy–Schwarz]

Prove, from the definitions of the dot product and the length and the results of Sections 9.2–9.4, that for all \( x, y \in \nR^n \): (a) \( \abs{\inner{x}{y}} \le \norm{x}\,\norm{y} \); (b) equality holds if and only if \( x \) and \( y \) are parallel.
:::

::: {.solution}
[Hint 1]

Dispose of the zero cases, then scale both vectors to length \( 1 \).
:::

::: {.solution}
[Hint 2]

For unit \( u, v \), expand \( \norm{u - v}^2 \) and \( \norm{u + v}^2 \).
:::

::: {.solution}
(a) If \( x = 0 \) or \( y = 0 \), both sides are \( 0 \). Otherwise \( \norm{x}, \norm{y} > 0 \); let \( u \coloneqq x/\norm{x} \), \( v \coloneqq y/\norm{y} \), unit vectors with \( \inner{x}{y} = \norm{x}\,\norm{y}\,\inner{u}{v} \). From \( 0 \le \norm{u \mp v}^2 = 2 \mp 2\inner{u}{v} \) we get \( -1 \le \inner{u}{v} \le 1 \), so \( \abs{\inner{u}{v}} \le 1 \); multiplying by \( \norm{x}\,\norm{y} > 0 \) gives (a).

(b) If \( x = 0 \) or \( y = 0 \), the two vectors are parallel and both sides of (a) are \( 0 \). Let \( x, y \ne 0 \). If equality holds, then \( \inner{u}{v} = \pm 1 \), so \( \norm{u \mp v}^2 = 0 \), hence \( v = \pm u \) and \( y = \pm(\norm{y}/\norm{x})\,x \): parallel. Conversely, if they are parallel, then \( y = cx \) for some \( c \) (remark after @def-parallel-rn), and \( \abs{\inner{x}{cx}} = \abs{c}\,\norm{x}^2 = \norm{x}\,\norm{cx} \).

**Marking scheme.** (10 points)
- 1: settles \( x = 0 \) or \( y = 0 \).
- 2: reduces to unit vectors, saying why: the statement is homogeneous and the factor \( \norm{x}\,\norm{y} \) is positive.
- 3: proves \( \abs{\inner{u}{v}} \le 1 \) for unit vectors, by any correct route.
- 1: scales back to (a).
- 3: proves the equality case in both directions, zero vectors included.
A second route through Lagrange's identity (C2) maps onto the same points: 1 for the zero cases (there automatic), 2 + 3 + 1 for proving the identity and reading off \( \inner{x}{y}^2 \le \norm{x}^2\norm{y}^2 \) and taking roots, 3 for "all \( x_j y_k - x_k y_j = 0 \) if and only if parallel".
Fatal errors (0 for the step): dividing by \( \norm{x} \) without \( x \ne 0 \); proving only \( \inner{x}{y} \le \norm{x}\,\norm{y} \) and claiming the absolute value; omitting the converse of (b).
:::

::: {#exr-cauchy-schwarz-and-the-triangle-inequality-c2}
[C2: Lagrange's identity]

Let \( x, y \in \nR^n \). Prove that
\[
\Bigl( \sum_{k=1}^{n} x_k^2 \Bigr) \Bigl( \sum_{k=1}^{n} y_k^2 \Bigr) - \Bigl( \sum_{k=1}^{n} x_k y_k \Bigr)^2 = \frac12 \sum_{j=1}^{n} \sum_{k=1}^{n} (x_j y_k - x_k y_j)^2 ,
\]
and deduce @cor-cauchy-schwarz-sums with its equality case: equality holds if and only if \( x_j y_k = x_k y_j \) for all \( j, k \), if and only if \( x \) and \( y \) are parallel.
:::

::: {.solution}
[Hint 1]

Expand the square inside the double sum and use the product form of @prp-double-sum three times.
:::

::: {.solution}
[Hint 2]

For "parallel": if \( x = 0 \) it is clear; otherwise pick \( m \) with \( x_m \ne 0 \) and set \( c \coloneqq y_m / x_m \).
:::

::: {.solution}
Write \( A \coloneqq \sum_k x_k^2 \), \( B \coloneqq \sum_k y_k^2 \), \( C \coloneqq \sum_k x_k y_k \). Expanding each term,
\[
(x_j y_k - x_k y_j)^2 = x_j^2 y_k^2 - 2 (x_j y_j)(x_k y_k) + x_k^2 y_j^2 .
\]
Sum over \( j \) and \( k \), splitting termwise (@lem-ring-finite-sums (a), (b)). By the product form of @prp-double-sum, \( \sum_j \sum_k x_j^2 y_k^2 = AB \), \( \sum_j \sum_k x_k^2 y_j^2 = BA \) and \( \sum_j \sum_k (x_j y_j)(x_k y_k) = C^2 \). The double sum is \( 2AB - 2C^2 \), and halving proves the identity.

Each term \( (x_j y_k - x_k y_j)^2 \) is \( \ge 0 \) (@fd3:prp-ordered-ring-rules (e)), so each inner sum and then the double sum is \( \ge 0 \) (@prp-sum-order (b)). Hence \( C^2 \le AB \), which is @cor-cauchy-schwarz-sums. Equality holds if and only if the double sum is \( 0 \), that is, by @prp-sum-order (e) applied to the outer sum and then to each inner sum, if and only if every term is \( 0 \), that is, \( x_j y_k = x_k y_j \) for all \( j, k \).

It remains to match this with "parallel". If \( y = cx \), each \( x_j y_k - x_k y_j = c(x_j x_k - x_k x_j) = 0 \); if \( x = cy \), likewise \( c(y_j y_k - y_k y_j) = 0 \). Conversely, suppose all \( x_j y_k = x_k y_j \). If \( x = 0 \), \( x \) is parallel to \( y \). Otherwise choose \( m \) with \( x_m \ne 0 \) and let \( c \coloneqq y_m / x_m \); for every \( k \), \( x_m y_k = x_k y_m \) gives \( y_k = c x_k \), so \( y = cx \).

For \( n = 2 \) the terms with \( j = k \) vanish and the other two are both \( (x_1 y_2 - x_2 y_1)^2 \), so the identity is \( AB - C^2 = (x_1 y_2 - x_2 y_1)^2 \).
:::

<!-- dependency ledger
thm-cauchy-schwarz-rn (proof): from 0 <= 2 - 2t infer t <= 1, from 0 <= 2 + 2t infer -1 <= t (add, then multiply by 1/2 > 0) | fd3:prp-ordered-ring-rules (b), (c), cited
thm-cauchy-schwarz-rn (proof): |t| = r with r >= 0 iff t = r or t = -r | fd3:def-absolute-value-ordered-field, by cases, cited
thm-cauchy-schwarz-rn (proof): cancelling the non-zero factor ||x|| ||y|| | multiplicative inverse in the field R, fd3:def-commutative-ring-and-field
thm-cauchy-schwarz-rn (proof): a real s >= 0 with s^2 = 0 is 0 | fd3:prp-ordered-ring-rules (e), cited
thm-cauchy-schwarz-rn (proof): for x != 0, y parallel to x iff y = tx; 0 parallel to everything | Section 9.2, the two paragraphs after def-parallel-rn (unlabelled; cited as "the remark after @def-parallel-rn")
cor-cauchy-schwarz-sums (proof): non-negative reals with equal squares are equal | comparing squares, Section 9.4 (recalled from Section 3.3; fd3:prp-ordered-ring-rules (g))
thm-triangle-inequality-rn (proof): comparing squares of non-negative reals (weak and equality forms) | Section 9.4 recall of Section 3.3 (unlabelled)
thm-triangle-inequality-rn (proof): (b) by transfer of the proof of cor-complex-triangle-variants (a) | cor-complex-triangle-variants, cited; every step written out with its reason
cor-triangle-finite-sums-rn (proof): sum of vectors by recursion, empty sum 0 | lem-vector-sums-coordinatewise, cited
cor-norm-sum-bound (proof): <w, w> = n for w = (1, ..., 1), so ||w|| = sqrt n | a sum of n ones is n, by the recursion of fd2:def-sum-product
cor-cauchy-schwarz-sums (claim): 32^2 = 1024 <= 14 * 77 = 1078 | inline arithmetic; verify/ch09/cor-cauchy-schwarz-sums.py
exm-cauchy-schwarz-applications (solution): ||(2, 3, -1)||^2 = 14; 14/sqrt 14 = sqrt 14 | inline arithmetic; verify/ch09/exm-cauchy-schwarz-applications.py
exr-cauchy-schwarz-and-the-triangle-inequality-b2 (solution): comparing squares (equality form) | Section 9.4 recall of Section 3.3 (unlabelled)
exr-cauchy-schwarz-and-the-triangle-inequality-c2 (solution): sums from k = 1 read as sums from 0 for lem-ring-finite-sums, prp-double-sum, prp-sum-order | the reindexing line of the chapter's prerequisite ledger (k = m form of fd2:def-sum-product)
exr-cauchy-schwarz-and-the-triangle-inequality-c2 (solution): a sum of non-negative terms is >= 0 | prp-sum-order (b) with m = -1 (the empty sum is 0), cited as prp-sum-order (b)
-->
