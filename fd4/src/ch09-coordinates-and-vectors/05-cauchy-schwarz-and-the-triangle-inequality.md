# Cauchy–Schwarz and the Triangle Inequality

Section 9.4 gave \( \nR^n \) a length and a distance and proved every basic property of the distance except one: that a detour through a third point is never shorter than the direct route. This section proves it. Everything rests on one inequality between the dot product and the lengths, the Cauchy–Schwarz inequality. The method that proves it is called **normalizing**: shrink or stretch both vectors to length \( 1 \), prove the inequality there, and scale back.

## Two earlier proofs, and why neither transfers

The triangle inequality has been proved before in this series in two settings, for real numbers and for complex numbers. Each proof used a tool that \( \nR^n \) lacks.

**In \( \nR \).** *Number Systems: From \(\nN\) to \(\nR\)*, Section 4.1, trapped each number between \( \pm \) its absolute value, \( -\abs{x} \le x \le \abs{x} \), and added the two traps. That is how it proved the triangle inequality for absolute values, @fd3:prp-absolute-value-ordered-field (c)–(e). The trap compares \( x \) with the number \( \abs{x} \). For a vector \( x \in \nR^n \) with \( n \ge 2 \), "\( x \le \norm{x} \)" compares a vector with a number, and \( \nR^n \) has been given no order at all.

**In \( \nC = \nR^2 \).** Section 3.3 expanded \( \abs{z + w}^2 \) and met the cross term \( 2\operatorname{Re}(z\conj{w}) \), which it bounded by \( \abs{z\conj{w}} = \abs{z}\abs{w} \) (@thm-complex-triangle-inequality). By @prp-plane-is-complex-plane, \( \operatorname{Re}(z\conj{w}) = \inner{z}{w} \) and \( \abs{z} = \norm{z} \), so the key step was
\[
\inner{z}{w} \le \norm{z} \, \norm{w} ,
\]
proved with the multiplication of \( \nC \): the product \( z\conj{w} \) and the rule \( \abs{z\conj{w}} = \abs{z}\abs{w} \). For \( n \ge 3 \) this book defines no such multiplication on \( \nR^n \).

The expansion itself does survive. Section 9.4 compared lengths by comparing their squares (@exm-method-expand-the-square). Expanding both squares by @eq-expand-norm-squared gives
\[
\norm{x + y}^2 = \norm{x}^2 + 2\inner{x}{y} + \norm{y}^2 , \qquad
\bigl( \norm{x} + \norm{y} \bigr)^2 = \norm{x}^2 + 2\norm{x}\,\norm{y} + \norm{y}^2 .
\]
Everything matches except the cross terms. So the triangle inequality in \( \nR^n \) rests on one inequality, \( \inner{x}{y} \le \norm{x}\,\norm{y} \), and that inequality now needs a proof that uses only the laws of the dot product.

**An attempt that stalls.** Work coordinatewise: \( x_k y_k \le \abs{x_k}\,\abs{y_k} \) for each \( k \), and \( \abs{x_k} \le \norm{x} \), \( \abs{y_k} \le \norm{y} \) by @prp-norm-coordinate-bounds (a). Adding the \( n \) bounds gives
\[
\inner{x}{y} \le \sum_{k=1}^{n} \abs{x_k}\,\abs{y_k} \le n \, \norm{x} \, \norm{y} ,
\]
which is off by the factor \( n \). Try \( x = y = (1, \dots, 1) \): then \( \inner{x}{y} = n \) and \( \norm{x}\,\norm{y} = n \), so the inequality we want holds with equality, while the attempt only gives \( n \le n^2 \). Each bound \( \abs{x_k} \le \norm{x} \) is sharp only when all of \( x \) sits in coordinate \( k \). For \( x \ne 0 \) and \( n \ge 2 \), the \( n \) bounds cannot all be sharp at once. A coordinate-by-coordinate bound loses the geometry. The proof below uses the length of a whole vector instead.

## The Cauchy–Schwarz inequality

Start with two vectors of \( \nR^2 \), \( x = (3, 4) \) and \( y = (4, 3) \). Their dot product is \( \inner{x}{y} = 12 + 12 = 24 \), and both have length \( 5 \), so \( \norm{x}\,\norm{y} = 25 \). The dot product is a little smaller than the product of the lengths. Now take \( y = 2x = (6, 8) \) instead. Then \( \inner{x}{y} = 18 + 32 = 50 \) and \( \norm{x}\,\norm{y} = 5 \cdot 10 = 50 \): the two are equal. The theorem says that the dot product never exceeds the product of the lengths, and that equality up to sign happens exactly for parallel vectors.

Equality can hold with either sign, and the sign tells which way \( y \) points along \( x \).

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

The attempt gives \( 0 \le \norm{u - v}^2 = 1 - 2\inner{u}{v} + 1 \), so \( \inner{u}{v} \le 1 \). That is one half of the goal for unit vectors, and nothing yet about general \( x, y \). For general vectors the same expansion gives only \( 2\inner{x}{y} \le \norm{x}^2 + \norm{y}^2 \). Its right side equals \( 2\norm{x}\,\norm{y} \) only when \( \norm{x} = \norm{y} \). So we make the lengths equal, to \( 1 \), and pay for it by scaling back.

| We know | We want |
|---|---|
| \( x, y \in \nR^n \) | \( \abs{\inner{x}{y}} \le \norm{x}\,\norm{y} \) |
| \( x, y \ne 0 \) (if one is \( 0 \), both sides are \( 0 \)); \( u \coloneqq x/\norm{x} \), \( v \coloneqq y/\norm{y} \) are unit vectors | \( \abs{\inner{u}{v}} \le 1 \), because both sides of the old goal are \( \norm{x}\,\norm{y} \) times those of the new one |
| \( \norm{u - v}^2 = 2 - 2\inner{u}{v} \ge 0 \) | \( -1 \le \inner{u}{v} \le 1 \); the upper half is done |
| \( \norm{u + v}^2 = 2 + 2\inner{u}{v} \ge 0 \) | the lower half is done: the gap closes |

The passage to unit vectors is allowed because the statement is **homogeneous**: replacing \( x \) by \( ax \) with \( a > 0 \) multiplies both sides by \( a \), and likewise for \( y \). For the equality cases, ask when \( \norm{u - v}^2 \) or \( \norm{u + v}^2 \) is \( 0 \).

*Before reading on: where is \( x \ne 0 \) used, and why are both expansions needed?*
:::

::: {.proof}
Let \( x, y \in \nR^n \).

(a) If \( x = 0 \) or \( y = 0 \), then \( \inner{x}{y} = 0 \), because a dot product with the zero vector is \( 0 \). Also \( \norm{x}\,\norm{y} = 0 \), since \( \norm{0} = 0 \). So (a) reads \( 0 \le 0 \).

Let \( x \ne 0 \) and \( y \ne 0 \). Then \( \norm{x} > 0 \) and \( \norm{y} > 0 \), because only the zero vector has length \( 0 \) (@prp-norm-basic-rn (a)). So \( u \coloneqq (1/\norm{x})\,x \) and \( v \coloneqq (1/\norm{y})\,y \) are unit vectors, and \( x = \norm{x}\,u \), \( y = \norm{y}\,v \). Pulling the two scalars out of the dot product gives
\[
\inner{x}{y} = \norm{x}\,\norm{y} \, \inner{u}{v} .
\]{#eq-cauchy-schwarz-normalized}
Expanding by @eq-expand-norm-squared, with \( \norm{u}^2 = \norm{v}^2 = 1 \),
\[
\begin{aligned}
0 &\le \norm{u - v}^2 = \norm{u}^2 - 2\inner{u}{v} + \norm{v}^2 = 2 - 2\inner{u}{v} , \\
0 &\le \norm{u + v}^2 = 2 + 2\inner{u}{v} .
\end{aligned}
\]
Add \( 2\inner{u}{v} \) to the first line and \( -2 \) to the second, and multiply both by \( \tfrac12 > 0 \). This gives \( -1 \le \inner{u}{v} \le 1 \), that is, \( \abs{\inner{u}{v}} \le 1 \). Now multiply by \( \norm{x}\,\norm{y} > 0 \). By @eq-cauchy-schwarz-normalized and the rule \( \abs{ab} = \abs{a}\,\abs{b} \),
\[
\abs{\inner{x}{y}} = \norm{x}\,\norm{y}\,\abs{\inner{u}{v}} \le \norm{x}\,\norm{y} .
\]

(c) \( (\Leftarrow) \) If \( x = 0 \), both sides are \( 0 \). If \( y = cx \) with \( c \ge 0 \), then \( \inner{x}{y} = c\inner{x}{x} = c\norm{x}^2 \). Also \( \norm{x}\,\norm{cx} = \abs{c}\,\norm{x}^2 = c\norm{x}^2 \), because \( c \ge 0 \).

\( (\Rightarrow) \) If \( x = 0 \) we are done, and if \( y = 0 \), then \( y = 0x \) with \( c = 0 \). Otherwise \( x, y \ne 0 \). With \( u, v \) as in (a), @eq-cauchy-schwarz-normalized gives \( \norm{x}\,\norm{y}\,\inner{u}{v} = \norm{x}\,\norm{y} \). Cancelling the non-zero factor \( \norm{x}\,\norm{y} \) gives \( \inner{u}{v} = 1 \). Then \( \norm{u - v}^2 = 2 - 2 = 0 \), so \( \norm{u - v} = 0 \), and \( u = v \) because only the zero vector has length \( 0 \). Hence \( y = \norm{y}\,u = c x \) with \( c \coloneqq \norm{y}/\norm{x} > 0 \).

(c′) Replacing \( y \) by \( -y \) changes the sign of the dot product but not the length: \( \inner{x}{-y} = -\inner{x}{y} \) and \( \norm{-y} = \norm{y} \). So \( \inner{x}{y} = -\norm{x}\,\norm{y} \) holds if and only if \( \inner{x}{-y} = \norm{x}\,\norm{-y} \). By (c) applied to \( x \) and \( -y \), this holds if and only if \( x = 0 \) or \( -y = cx \) with \( c \ge 0 \). That is, \( y = (-c)x \) with \( -c \le 0 \).

(b) Since \( \norm{x}\,\norm{y} \ge 0 \), the definition of the absolute value gives \( \abs{\inner{x}{y}} = \norm{x}\,\norm{y} \) if and only if \( \inner{x}{y} = \pm\norm{x}\,\norm{y} \). By (c) and (c′) this holds if and only if \( x = 0 \) or \( y = cx \) for some real \( c \). That is exactly the statement that \( x \) and \( y \) are parallel. Indeed, \( 0 \) is parallel to every vector, and for \( x \ne 0 \), \( y \) is parallel to \( x \) if and only if \( y = cx \) for some \( c \). Section 9.2 noted this right after defining parallel vectors (@def-parallel-rn). This proves the theorem.

::: {.uses}
@prp-dot-product-laws-rn (a), (b), (e) (symmetry, scalars, zero vector); @prp-norm-basic-rn (a)–(c) (length zero, scaling, squares); @def-unit-vector-rn; @prp-vector-space-laws-rn (e), (f), (i) (scalar rules, signs); @fd3:prp-ordered-ring-rules (b), (c), (e) (adding, multiplying, squares); @fd3:prp-absolute-value-ordered-field (b), (d) (products, two-sided bounds); @fd3:def-absolute-value-ordered-field.
:::
:::

For \( n = 1 \) the theorem says little: \( \abs{xy} = \abs{x}\,\abs{y} \) always, and any two reals are parallel. The content is in \( n \ge 2 \), where most pairs of vectors are not parallel and the inequality is strict for them.

::: {.check}
For \( x = (1, 2, 2) \) and \( y = (2, 0, 1) \), compute both sides of (a). Is the inequality strict, and does (b) predict the answer?
:::

::: {.solution}
\( \inner{x}{y} = 2 + 0 + 2 = 4 \), \( \norm{x} = 3 \) and \( \norm{y} = \sqrt 5 \). Since \( 4^2 = 16 < 45 = (3\sqrt5)^2 \) and both numbers are non-negative, \( 4 < 3\sqrt5 \): strict. Yes: \( y = cx \) would need \( c = 2 \) from the first coordinate and \( c = 0 \) from the second. And \( x = cy \) is impossible since \( y_2 = 0 \ne 2 = x_2 \). So \( x \), \( y \) are not parallel and (b) forbids equality.
:::

Squaring (a) gives the form used for sums of real numbers. For example, with \( (1, 2, 3) \) and \( (4, 5, 6) \) the sum of products is \( 4 + 10 + 18 = 32 \), and the sums of squares are \( 14 \) and \( 77 \). The squared form reads \( 32^2 = 1024 \le 14 \cdot 77 = 1078 \).

::: {#cor-cauchy-schwarz-sums}
[Cauchy–Schwarz Inequality for Sums]

Let \( n \ge 1 \) and \( x_1, \dots, x_n, y_1, \dots, y_n \in \nR \). Then
\[
\Bigl( \sum_{k=1}^{n} x_k y_k \Bigr)^2 \le \Bigl( \sum_{k=1}^{n} x_k^2 \Bigr) \Bigl( \sum_{k=1}^{n} y_k^2 \Bigr) ,
\]
with equality if and only if \( (x_1, \dots, x_n) \) and \( (y_1, \dots, y_n) \) are parallel vectors of \( \nR^n \).
:::

::: {.proof}
Let \( x \coloneqq (x_1, \dots, x_n) \) and \( y \coloneqq (y_1, \dots, y_n) \). The three sums are \( \inner{x}{y} \), \( \norm{x}^2 \) and \( \norm{y}^2 \). By @thm-cauchy-schwarz-rn (a), \( 0 \le \abs{\inner{x}{y}} \le \norm{x}\,\norm{y} \). Squaring keeps an inequality between non-negative numbers, so \( \abs{\inner{x}{y}}^2 \le \norm{x}^2 \norm{y}^2 \). And \( \abs{\inner{x}{y}}^2 = \inner{x}{y}^2 \). Two non-negative reals with equal squares are equal (comparing squares, Section 9.4). So equality holds exactly when \( \abs{\inner{x}{y}} = \norm{x}\,\norm{y} \), that is, by @thm-cauchy-schwarz-rn (b), when \( x \) and \( y \) are parallel.

::: {.uses}
@def-dot-product-rn; @prp-norm-basic-rn (c) (length squared); @fd3:prp-ordered-field-halves (d) (multiplying inequalities); @fd3:prp-absolute-value-ordered-field (b) (\( \abs{t}^2 = t^2 \)).
:::
:::

In the example above the inequality is strict, because the two triples are not parallel. Exercise C2 below proves it a second way, from Lagrange's identity. For \( n = 2 \) that identity reads \( (ac + bd)^2 + (ad - bc)^2 = (a^2 + b^2)(c^2 + d^2) \). Chapter 3 mentioned this case as a second route in the solution of its chapter check, Exercise C1 of Section 3.3 (@exr-triangle-inequality-c1).

## The method: normalize

The proof of @thm-cauchy-schwarz-rn did its work for unit vectors and then scaled back. This way of proving is called normalizing.

::: {#exm-method-normalize}
[Method: normalize]

**How it goes.** Suppose a statement about \( x \) and \( y \) is **homogeneous**: replacing \( x \) by \( ax \) with \( a > 0 \) multiplies both sides by the same positive factor, and likewise for \( y \). Then:

1. Settle \( x = 0 \) and \( y = 0 \) separately.
2. For \( x, y \ne 0 \), put \( u \coloneqq x/\norm{x} \) and \( v \coloneqq y/\norm{y} \), and prove the statement for the unit vectors \( u \), \( v \).
3. Scale back, multiplying by the positive factor.

**When to use it.** Inequalities between \( \inner{x}{y} \) and products of lengths; statements about directions rather than sizes.

**Common mistakes.** Normalizing the zero vector is impossible: it has no direction, and \( x/\norm{x} \) would divide by \( 0 \). Scaling by a negative factor breaks the method, since \( x \mapsto -x \) changes the sign of \( \inner{x}{y} \) but not of \( \norm{x}\,\norm{y} \). A statement that is not homogeneous cannot be normalized. For example, \( \norm{u + v} \le 2 \) holds for all unit \( u, v \). By Cauchy–Schwarz, \( \norm{u + v}^2 = 2 + 2\inner{u}{v} \le 2 + 2\norm{u}\,\norm{v} = 4 \), and comparing squares of non-negative numbers gives \( \norm{u + v} \le 2 \). And yet \( \norm{x + y} \le 2 \) fails for \( x = y = 2e_1 \), where \( \norm{x + y} = 4 \).
:::

The proof of @thm-cauchy-schwarz-rn is the first worked example. It settles the zero case, proves the bound for unit vectors by expanding \( \norm{u \mp v}^2 \), and scales back by multiplying by \( \norm{x}\,\norm{y} \). Part (b) below is a second.

::: {#exm-cauchy-schwarz-applications}
[Two uses of Cauchy–Schwarz]

(a) Show that \( (a + b + c)^2 \le 3(a^2 + b^2 + c^2) \) for all real \( a, b, c \), with equality if and only if \( a = b = c \).

(b) Find the largest value of \( 2x_1 + 3x_2 - x_3 \) over all unit vectors \( x \in \nR^3 \), and every unit vector where it is attained.
:::

::: {.solution}
(a) Apply @cor-cauchy-schwarz-sums to \( (a, b, c) \) and \( w \coloneqq (1, 1, 1) \). The left side is \( (a + b + c)^2 \) and the right side is \( (a^2 + b^2 + c^2) \cdot 3 \). Equality holds if and only if \( (a, b, c) \) is parallel to \( w \). Since \( w \ne 0 \), this means \( (a, b, c) = tw \) for some \( t \), that is, \( a = b = c \).

(b) Let \( p \coloneqq (2, 3, -1) \), so the expression is \( \inner{p}{x} \) and \( \norm{p} = \sqrt{14} \). The statement \( \inner{p}{x} \le \sqrt{14}\,\norm{x} \) is homogeneous in \( x \). So by normalizing it is enough to look at unit \( x \), which is what the question does. For unit \( x \), using \( t \le \abs{t} \) and then @thm-cauchy-schwarz-rn (a),
\[
\inner{p}{x} \le \abs{\inner{p}{x}} \le \norm{p}\,\norm{x} = \sqrt{14} .
\]
The value \( \sqrt{14} \) is attained at \( x_0 \coloneqq p/\sqrt{14} \), a unit vector, since \( \inner{p}{x_0} = 14/\sqrt{14} = \sqrt{14} \) (because \( \sqrt{14} \cdot \sqrt{14} = 14 \)). Conversely, suppose \( \inner{p}{x} = \sqrt{14} = \norm{p}\,\norm{x} \). Since \( p \ne 0 \), @thm-cauchy-schwarz-rn (c), with \( p \) in the first place, gives \( x = cp \) with \( c \ge 0 \). Then \( 1 = \norm{x} = c\sqrt{14} \), so \( c = 1/\sqrt{14} \) and \( x = x_0 \). The largest value is \( \sqrt{14} \), attained only at \( (2, 3, -1)/\sqrt{14} \). For \( x = 0 \) both sides of \( \inner{p}{x} \le \sqrt{14}\,\norm{x} \) are \( 0 \). Scaling back the other \( x \), \( 2x_1 + 3x_2 - x_3 \le \sqrt{14}\,\norm{x} \) for every \( x \in \nR^3 \).

::: {.uses}
@def-parallel-rn and the remark after it (parallel to \( w \ne 0 \)); @fd3:prp-absolute-value-ordered-field (c) (\( t \le \abs{t} \)).
:::
:::

## The triangle inequality

With the cross term under control, the expansion at the start of the section finishes the job. For instance, \( x = (3, 4) \) and \( y = (4, 3) \) give \( x + y = (7, 7) \), and \( \norm{x + y}^2 = 98 < 100 = (\norm{x} + \norm{y})^2 \).

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
(a) Expand the square, then use \( \inner{x}{y} \le \abs{\inner{x}{y}} \) and @thm-cauchy-schwarz-rn (a), adding the inequalities:
\[
\begin{aligned}
\norm{x + y}^2 &= \norm{x}^2 + 2\inner{x}{y} + \norm{y}^2 \\
&\le \norm{x}^2 + 2\abs{\inner{x}{y}} + \norm{y}^2 \\
&\le \norm{x}^2 + 2\norm{x}\,\norm{y} + \norm{y}^2 = \bigl( \norm{x} + \norm{y} \bigr)^2 .
\end{aligned}
\]
Both \( \norm{x + y} \) and \( \norm{x} + \norm{y} \) are non-negative, so comparing squares (Section 9.4) gives \( \norm{x + y} \le \norm{x} + \norm{y} \). For the same reason the two lengths are equal if and only if their squares are. Comparing the first and last expressions of the display, this means \( 2\inner{x}{y} = 2\norm{x}\,\norm{y} \). By @thm-cauchy-schwarz-rn (c), this holds if and only if \( x = 0 \) or \( y = cx \) with \( c \ge 0 \).

(b) The argument is the one Section 3.3 used for complex numbers (@cor-complex-triangle-variants (a)), with \( \norm{\cdot} \) in place of \( \abs{\cdot} \). Apply (a) to \( x = (x - y) + y \). This gives \( \norm{x} - \norm{y} \le \norm{x - y} \). Exchanging \( x \) and \( y \) gives \( \norm{y} - \norm{x} \le \norm{y - x} \). Also \( \norm{y - x} = \norm{x - y} \), since \( y - x = (-1)(x - y) \). The two bounds together say \( -\norm{x - y} \le \norm{x} - \norm{y} \le \norm{x - y} \), which is (b).

(c) By @prp-vector-space-laws-rn, \( x - z = (x - y) + (y - z) \). So by (a) and the definition of distance,
\[
d(x, z) = \norm{(x - y) + (y - z)} \le \norm{x - y} + \norm{y - z} = d(x, y) + d(y, z) .
\]
This proves the theorem.

::: {.uses}
@eq-expand-norm-squared; @fd3:prp-absolute-value-ordered-field (c), (d) (\( t \le \abs{t} \), two-sided bounds); @fd3:prp-ordered-ring-rules (b) (adding inequalities); @prp-norm-basic-rn (b) with \( c = -1 \); @def-distance-rn.
:::
:::

The equality case of (a) uses @thm-cauchy-schwarz-rn (c), not (b). The first inequality of the display is an equality only when \( \inner{x}{y} \ge 0 \). So a negative \( \inner{x}{y} \) with \( \abs{\inner{x}{y}} = \norm{x}\,\norm{y} \) still leaves a gap.

::: {.warning}
"Equality in Cauchy–Schwarz holds for parallel vectors, and the triangle inequality comes from Cauchy–Schwarz, so parallel vectors give \( \norm{x + y} = \norm{x} + \norm{y} \)." The conclusion is false. For \( x = e_1 \) and \( y = -e_1 \), which are parallel, \( \norm{x + y} = 0 \) and \( \norm{x} + \norm{y} = 2 \). The argument forgets the step \( \inner{x}{y} \le \abs{\inner{x}{y}} \), which is strict whenever \( \inner{x}{y} < 0 \).
:::

For \( n = 2 \), (a) is the triangle inequality of Section 3.3 (@thm-complex-triangle-inequality), now proved by a route with no complex multiplication. The translation between the two is @prp-plane-is-complex-plane (c). Chapter 3 found its equality case in a different form: \( z\conj{w} \) is a non-negative real (@exr-triangle-inequality-b1). Section 9.6 returns to the comparison in a review exercise.

::: {.check}
Let \( x = (1, -2, 3) \) and \( y = -2x \). Is \( \abs{\inner{x}{y}} = \norm{x}\,\norm{y} \)? Is \( \norm{x + y} = \norm{x} + \norm{y} \)?
:::

::: {.solution}
\( \inner{x}{y} = -2 \cdot 14 = -28 \) and \( \norm{x}\,\norm{y} = \sqrt{14} \cdot 2\sqrt{14} = 28 \): yes, as (b) of @thm-cauchy-schwarz-rn predicts for parallel vectors. But \( x + y = -x \), so \( \norm{x + y} = \sqrt{14} \), while \( \norm{x} + \norm{y} = 3\sqrt{14} \): no, since \( y = cx \) with \( c = -2 < 0 \).
:::

## Sums of many vectors

Adding one vector at a time extends (a) to any finite number of terms. For instance, in \( \nR^3 \), \( e_1 + e_2 + e_3 = (1, 1, 1) \) has length \( \sqrt 3 \), while the three lengths add up to \( 3 \), and \( \sqrt 3 \le 3 \) because \( 3 \le 9 \).

::: {#cor-triangle-finite-sums-rn}
[Triangle Inequality for Finite Sums]

For every \( m \in \nN \) and all \( v_1, \dots, v_m \in \nR^n \),
\[
\Bigl\| \sum_{j=1}^{m} v_j \Bigr\| \le \sum_{j=1}^{m} \norm{v_j} .
\]
:::

::: {.proof}
We use induction on \( m \ge 0 \). The sums are defined by recursion, as in @lem-vector-sums-coordinatewise. For \( m = 0 \) both sides are \( 0 \). Suppose the inequality holds for \( m \). Split off the last term by the recursion, apply @thm-triangle-inequality-rn (a), and then add \( \norm{v_{m+1}} \) to both sides of the inequality for \( m \):
\[
\Bigl\| \sum_{j=1}^{m+1} v_j \Bigr\| \le \Bigl\| \sum_{j=1}^{m} v_j \Bigr\| + \norm{v_{m+1}} \le \sum_{j=1}^{m+1} \norm{v_j} .
\]

::: {.uses}
@fd2:thm-induction; @prp-norm-basic-rn (a) (\( \norm{0} = 0 \)); @fd3:prp-ordered-ring-rules (b) (adding inequalities).
:::
:::

Length and the sum of the absolute values of the coordinates are comparable, with constants \( 1 \) and \( \sqrt n \). For \( x = (3, 4) \), the length is \( 5 \) and the sum is \( 7 \). Indeed \( 5 \le 7 \), and \( 7 \le \sqrt 2 \cdot 5 \) because \( 49 \le 50 \).

::: {#cor-norm-sum-bound}
[Length against the Sum of the Coordinates]

For every \( x \in \nR^n \),
\[
\norm{x} \le \sum_{k=1}^{n} \abs{x_k} \le \sqrt{n}\,\norm{x} .
\]
:::

::: {.proof}
By @prp-standard-basis-expansion, \( x = \sum_k x_k e_k \). So @cor-triangle-finite-sums-rn gives \( \norm{x} \le \sum_k \norm{x_k e_k} = \sum_k \abs{x_k} \), since \( \norm{x_k e_k} = \abs{x_k} \). For the second inequality let \( a \coloneqq (\abs{x_1}, \dots, \abs{x_n}) \) and \( w \coloneqq (1, \dots, 1) \). Then \( \inner{a}{w} = \sum_k \abs{x_k} \) and \( \norm{w} = \sqrt n \). Also \( \norm{a} = \norm{x} \): both are non-negative with the same square \( \sum_k x_k^2 \), and a non-negative square root is unique (@fd3:prp-cof-square-roots). Using \( t \le \abs{t} \) and then @thm-cauchy-schwarz-rn (a),
\[
\sum_k \abs{x_k} \le \abs{\inner{a}{w}} \le \norm{a}\,\norm{w} = \sqrt n \, \norm{x} .
\]

::: {.uses}
@prp-norm-basic-rn (b), (e) (\( \norm{x_k e_k} = \abs{x_k} \)); @fd3:prp-absolute-value-ordered-field (b), (c) (\( \abs{t}^2 = t^2 \), \( t \le \abs{t} \)).
:::
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
4. In the scratch work, what goes wrong with the expansion of \( \norm{u - v}^2 \) if \( u \) is not a unit vector?
5. Give the idea of the proof in two sentences.
:::
:::

::: {.solution}
(a) To form \( u = x/\norm{x} \), which needs \( \norm{x} \ne 0 \), that is, \( x \ne 0 \) (@prp-norm-basic-rn (a)). The zero case is settled separately.

(b) \( \norm{u - v}^2 = 2 - 2\inner{u}{v} \ge 0 \) gives \( \inner{u}{v} \le 1 \); \( \norm{u + v}^2 = 2 + 2\inner{u}{v} \ge 0 \) gives \( \inner{u}{v} \ge -1 \).

(c) \( \norm{x} = \norm{y} = 5 \), \( u = (\tfrac35, \tfrac45) \), \( v = (\tfrac45, \tfrac35) \), \( \inner{u}{v} = \tfrac{24}{25} \), and \( \norm{u - v}^2 = \tfrac1{25} + \tfrac1{25} = \tfrac{2}{25} = 2 - \tfrac{48}{25} \). Scaling back, \( \inner{x}{y} = 25 \cdot \tfrac{24}{25} = 24 \le 25 \).

(d) The expansion becomes \( \norm{u - v}^2 = \norm{u}^2 - 2\inner{u}{v} + \norm{v}^2 \), not \( 2 - 2\inner{u}{v} \). It only gives \( \inner{u}{v} \le \tfrac12(\norm{u}^2 + \norm{v}^2) \), which exceeds \( \norm{u}\,\norm{v} \) unless \( \norm{u} = \norm{v} \), since \( \tfrac12(a^2 + b^2) - ab = \tfrac12(a - b)^2 > 0 \) for real \( a \ne b \).

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
An admissible order is (iv), (viii), (i), (vi), (v), (iii). Line (iv) must precede (viii), and (viii) must precede (i). Line (i) must precede (vi), which repeats (iv), (viii), (i) with the letters exchanged. Line (v) may stand anywhere before (iii). Line (iii) comes last, since it uses (i), (vi) and (v).

Line (vii) fails: (a) applied to \( x \) and \( -y \) gives \( \norm{x - y} \le \norm{x} + \norm{-y} = \norm{x} + \norm{y} \), with a plus sign. The claim itself is false: at \( y = -x \ne 0 \) it reads \( 2\norm{x} \le 0 \). Line (ii) is false for every \( y \ne 0 \): by @prp-norm-basic-rn (b), \( \norm{-y} = \abs{-1}\,\norm{y} = \norm{y} > 0 > -\norm{y} \).
:::

::: {#exr-cauchy-schwarz-and-the-triangle-inequality-b2}
[B2]

Prove that \( \norm{x - y} = \norm{x + y} \) if and only if \( x \perp y \). You may start from the two expansions
\[
\norm{x + y}^2 = \norm{x}^2 + 2\inner{x}{y} + \norm{y}^2 , \qquad \norm{x - y}^2 = \norm{x}^2 - 2\inner{x}{y} + \norm{y}^2 .
\]
*Name the method, then use it.*
:::

::: {.solution}
The method is to expand the square (@exm-method-expand-the-square). Both lengths are non-negative, so they are equal if and only if their squares are (comparing squares, Section 9.4). Subtracting the two expansions gives \( \norm{x + y}^2 - \norm{x - y}^2 = 4\inner{x}{y} \), which is @prp-polarization-rn (a) multiplied by \( 4 \). This is \( 0 \) if and only if \( \inner{x}{y} = 0 \). Indeed, if \( 4\inner{x}{y} = 0 \), then \( 4 = 0 \) or \( \inner{x}{y} = 0 \) (@fd3:lem-field-fraction-rules (d)), and \( 4 \ne 0 \) since \( 4 > 0 \) in the ordered field \( \nR \). By the definition of orthogonal vectors, \( \inner{x}{y} = 0 \) holds if and only if \( x \perp y \).

::: {.uses}
@prp-polarization-rn (a); @def-orthogonal-rn.
:::
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
(a) Apply @cor-cauchy-schwarz-sums to \( x \) and \( w \coloneqq (1, \dots, 1) \), with \( \sum_k 1^2 = n \). Equality holds if and only if \( x \) is parallel to \( w \ne 0 \), that is, \( x = tw \) for some \( t \): all \( x_k \) are equal.

(b) Let \( p \coloneqq (1, 2, 2) \), so \( \norm{p} = 3 \) and the condition is \( \inner{p}{x} = 9 \). By @thm-cauchy-schwarz-rn (a), \( 9 = \inner{p}{x} \le \abs{\inner{p}{x}} \le \norm{p}\,\norm{x} = 3\norm{x} \). So \( \norm{x} \ge 3 \), and squaring gives \( \norm{x}^2 \ge 9 \). If \( \norm{x}^2 = 9 \), then \( \norm{x} = 3 \) and \( \inner{p}{x} = 9 = \norm{p}\,\norm{x} \). Since \( p \ne 0 \), @thm-cauchy-schwarz-rn (c) gives \( x = cp \) with \( c \ge 0 \), and the condition gives \( 9c = 9 \), so \( x = (1, 2, 2) \). This point satisfies the condition, \( 1 + 4 + 4 = 9 \), and \( \norm{(1, 2, 2)}^2 = 9 \). The smallest value is \( 9 \), attained only at \( (1, 2, 2) \).

::: {.uses}
@def-parallel-rn and the remark after it (parallel to \( w \ne 0 \)); @fd3:prp-absolute-value-ordered-field (c) (\( t \le \abs{t} \)); @fd3:prp-ordered-field-halves (d) (squaring keeps \( \le \)).
:::
:::

### C. Going deeper

::: {#exr-cauchy-schwarz-and-the-triangle-inequality-c1}
[C1: Chapter check: Cauchy–Schwarz]

Use only the definitions of the dot product and the length and the results of Sections 9.2–9.4. Prove that for all \( x, y \in \nR^n \): (a) \( \abs{\inner{x}{y}} \le \norm{x}\,\norm{y} \); (b) equality holds if and only if \( x \) and \( y \) are parallel.
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
(a) If \( x = 0 \) or \( y = 0 \), both sides are \( 0 \). Otherwise \( \norm{x}, \norm{y} > 0 \). Let \( u \coloneqq x/\norm{x} \) and \( v \coloneqq y/\norm{y} \): these are unit vectors with \( \inner{x}{y} = \norm{x}\,\norm{y}\,\inner{u}{v} \). From \( 0 \le \norm{u \mp v}^2 = 2 \mp 2\inner{u}{v} \) we get \( -1 \le \inner{u}{v} \le 1 \), so \( \abs{\inner{u}{v}} \le 1 \). Multiplying by \( \norm{x}\,\norm{y} > 0 \) gives (a).

(b) If \( x = 0 \) or \( y = 0 \), the two vectors are parallel and both sides of (a) are \( 0 \). Let \( x, y \ne 0 \). If equality holds, then \( \inner{u}{v} = \pm 1 \), so \( \norm{u \mp v}^2 = 0 \). Hence \( v = \pm u \) and \( y = \pm(\norm{y}/\norm{x})\,x \): parallel. Conversely, if they are parallel, then \( y = cx \) for some \( c \) (remark after @def-parallel-rn), and \( \abs{\inner{x}{cx}} = \abs{c}\,\norm{x}^2 = \norm{x}\,\norm{cx} \).

**What a complete answer needs.** (10 points)
- 1: settles \( x = 0 \) or \( y = 0 \).
- 2: reduces the general case to one it can bound, saying why the reduction is legitimate; for unit vectors: the statement is homogeneous and the factor \( \norm{x}\,\norm{y} \) is positive.
- 3: proves \( \abs{\inner{u}{v}} \le 1 \) for unit vectors, by any correct route.
- 1: scales back to (a).
- 3: proves the equality case in both directions, zero vectors included.

A proof through Lagrange's identity (C2) scores on the same points. It gets 1 for the zero cases, which are automatic there. It gets 2 + 3 + 1 for proving the identity, reading off \( \inner{x}{y}^2 \le \norm{x}^2\norm{y}^2 \) and taking roots. It gets 3 for "all \( x_j y_k - x_k y_j = 0 \) if and only if parallel".

A proof that normalizes nothing, expanding \( \norm{x - t_0 y}^2 \ge 0 \) with \( t_0 \coloneqq \inner{x}{y}/\norm{y}^2 \), also scores on the same points. It gets 1 for \( y = 0 \), 2 for setting up \( t_0 \) using \( y \ne 0 \), 3 for the inequality on squares, 1 for taking roots, and 3 for the equality case through \( \norm{x - t_0 y} = 0 \).

Slips that lose the step: dividing by \( \norm{x} \) without \( x \ne 0 \); proving only \( \inner{x}{y} \le \norm{x}\,\norm{y} \) and claiming the absolute value; omitting the converse of (b).
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

Each term \( (x_j y_k - x_k y_j)^2 \) is a square, so it is \( \ge 0 \). So each inner sum is \( \ge 0 \), and then so is the double sum (@prp-sum-order (b)). Hence \( C^2 \le AB \), which is @cor-cauchy-schwarz-sums. Equality holds if and only if the double sum is \( 0 \). Apply @prp-sum-order (e) to the outer sum and then to each inner sum. So equality holds if and only if every term is \( 0 \), that is, \( x_j y_k = x_k y_j \) for all \( j, k \).

It remains to match this with "parallel". If \( y = cx \), each \( x_j y_k - x_k y_j = c(x_j x_k - x_k x_j) = 0 \); if \( x = cy \), likewise \( c(y_j y_k - y_k y_j) = 0 \). Conversely, suppose all \( x_j y_k = x_k y_j \). If \( x = 0 \), \( x \) is parallel to \( y \). Otherwise choose \( m \) with \( x_m \ne 0 \) and let \( c \coloneqq y_m / x_m \). For every \( k \), \( x_m y_k = x_k y_m \) gives \( y_k = c x_k \), so \( y = cx \).

For \( n = 2 \) the terms with \( j = k \) vanish and the other two are both \( (x_1 y_2 - x_2 y_1)^2 \), so the identity is \( AB - C^2 = (x_1 y_2 - x_2 y_1)^2 \).

::: {.uses}
@fd3:prp-ordered-ring-rules (e) (squares are non-negative).
:::
:::

<!-- dependency ledger
thm-cauchy-schwarz-rn (claim): instance before the statement, <(3,4),(4,3)> = 24, ||(3,4)|| = ||(4,3)|| = 5; <(3,4),(6,8)> = 50 = 5 * 10 | inline arithmetic; verify/ch09/thm-cauchy-schwarz-rn.py
thm-cauchy-schwarz-rn (proof): from 0 <= 2 - 2t infer t <= 1, from 0 <= 2 + 2t infer -1 <= t (add, then multiply by 1/2 > 0) | fd3:prp-ordered-ring-rules (b), (c), cited in the Uses line
thm-cauchy-schwarz-rn (proof): |t| = r with r >= 0 iff t = r or t = -r | fd3:def-absolute-value-ordered-field, by cases, cited in the Uses line
thm-cauchy-schwarz-rn (proof): cancelling the non-zero factor ||x|| ||y|| | multiplicative inverse in the field R, fd3:def-commutative-ring-and-field
thm-cauchy-schwarz-rn (proof): a real s >= 0 with s^2 = 0 is 0 | fd3:prp-ordered-ring-rules (e), cited in the Uses line
thm-cauchy-schwarz-rn (proof): dot product with 0, scalars out of the dot product, unit vectors, x = ||x|| u, |ab| = |a||b|, -1 <= t <= 1 iff |t| <= 1, -y = (-1)y and -(cx) = (-c)x | prp-dot-product-laws-rn (a), (b), (e); prp-norm-basic-rn (a)-(c); def-unit-vector-rn; prp-vector-space-laws-rn (e), (f), (i); fd3:prp-absolute-value-ordered-field (b), (d); moved from the prose to the Uses line, still cited
thm-cauchy-schwarz-rn (proof): for x != 0, y parallel to x iff y = tx; 0 parallel to everything | Section 9.2, the two paragraphs after def-parallel-rn (unlabelled; cited as "Section 9.2 noted this right after defining parallel vectors (@def-parallel-rn)")
cor-cauchy-schwarz-sums (claim): instance before the statement, 4 + 10 + 18 = 32, 1 + 4 + 9 = 14, 16 + 25 + 36 = 77 | inline arithmetic; verify/ch09/cor-cauchy-schwarz-sums.py
cor-cauchy-schwarz-sums (proof): the sums are <x,y>, ||x||^2, ||y||^2; squaring non-negative inequalities; |t|^2 = t^2 | def-dot-product-rn, prp-norm-basic-rn (c), fd3:prp-ordered-field-halves (d), fd3:prp-absolute-value-ordered-field (b); cited in the Uses line
cor-cauchy-schwarz-sums (proof): non-negative reals with equal squares are equal | comparing squares, Section 9.4 (recalled from Section 3.3; fd3:prp-ordered-ring-rules (g))
exm-cauchy-schwarz-applications (solution): parallel to w != 0 iff a multiple of w; t <= |t| | remark after def-parallel-rn, fd3:prp-absolute-value-ordered-field (c); cited in the Uses line
thm-triangle-inequality-rn (claim): instance before the statement, x + y = (7,7), ||x+y||^2 = 98 < 100 = (5 + 5)^2 | inline arithmetic; verify/ch09/thm-triangle-inequality-rn.py
thm-triangle-inequality-rn (proof): expansion, t <= |t|, adding inequalities, ||y - x|| = ||x - y||, two-sided bound, distance | eq-expand-norm-squared, fd3:prp-absolute-value-ordered-field (c), (d), fd3:prp-ordered-ring-rules (b), prp-norm-basic-rn (b), def-distance-rn; cited in the Uses line
thm-triangle-inequality-rn (proof): comparing squares of non-negative reals (weak and equality forms) | Section 9.4 recall of Section 3.3 (unlabelled)
thm-triangle-inequality-rn (proof): (b) by transfer of the proof of cor-complex-triangle-variants (a) | cor-complex-triangle-variants, cited; every step written out with its reason
cor-triangle-finite-sums-rn (proof): sum of vectors by recursion, empty sum 0 | lem-vector-sums-coordinatewise, cited
cor-triangle-finite-sums-rn (claim): instance before the statement, e1 + e2 + e3 = (1,1,1), ||(1,1,1)||^2 = 3 <= 9 = 3^2 | inline arithmetic; verify/ch09/cor-triangle-finite-sums-rn.py
cor-triangle-finite-sums-rn (proof): induction; ||0|| = 0; adding inequalities | fd2:thm-induction, prp-norm-basic-rn (a), fd3:prp-ordered-ring-rules (b); cited in the Uses line
cor-norm-sum-bound (claim): instance before the statement, x = (3,4): ||x|| = 5, |3| + |4| = 7, 5 <= 7, 7^2 = 49 <= 50 = 2 * 5^2 | inline arithmetic; verify/ch09/cor-norm-sum-bound.py
cor-norm-sum-bound (proof): ||x_k e_k|| = |x_k|; |t|^2 = t^2; t <= |t| | prp-norm-basic-rn (b), (e), fd3:prp-absolute-value-ordered-field (b), (c); cited in the Uses line
cor-norm-sum-bound (proof): <w, w> = n for w = (1, ..., 1), so ||w|| = sqrt n | a sum of n ones is n, by the recursion of fd2:def-sum-product
cor-cauchy-schwarz-sums (claim): 32^2 = 1024 <= 14 * 77 = 1078 | inline arithmetic; verify/ch09/cor-cauchy-schwarz-sums.py
exm-cauchy-schwarz-applications (solution): ||(2, 3, -1)||^2 = 14; 14/sqrt 14 = sqrt 14 | inline arithmetic; verify/ch09/exm-cauchy-schwarz-applications.py
exr-cauchy-schwarz-and-the-triangle-inequality-b2 (solution): comparing squares (equality form) | Section 9.4 recall of Section 3.3 (unlabelled)
exr-cauchy-schwarz-and-the-triangle-inequality-b2 (solution): definition of orthogonal | def-orthogonal-rn, cited in the Uses line
exr-cauchy-schwarz-and-the-triangle-inequality-b2 (solution): ||x+y||^2 - ||x-y||^2 = 4<x,y> | prp-polarization-rn (a) (Section 9.4), cited inline and in the Uses line
exr-cauchy-schwarz-and-the-triangle-inequality-b2 (solution): 4 > 0, so 4 != 0 | 1 > 0 and adding positives, fd3:prp-ordered-ring-rules; zero-product rule fd3:lem-field-fraction-rules (d), cited inline
exm-method-normalize (claim): ||u + v|| <= 2 for unit u, v | eq-expand-norm-squared, thm-cauchy-schwarz-rn (a) (earlier on the page), comparing squares, Section 9.4 (unlabelled)
exr-cauchy-schwarz-and-the-triangle-inequality-a1 (solution): (a^2 + b^2)/2 - ab = (a - b)^2/2 > 0 for a != b | stated inline; ring arithmetic and fd3:prp-ordered-ring-rules (e)
exr-cauchy-schwarz-and-the-triangle-inequality-b4 (solution): parallel to w != 0 iff a multiple of w; t <= |t|; squaring keeps <= | remark after def-parallel-rn, fd3:prp-absolute-value-ordered-field (c), fd3:prp-ordered-field-halves (d); cited in the Uses line
exr-cauchy-schwarz-and-the-triangle-inequality-c2 (solution): sums from k = 1 read as sums from 0 for lem-ring-finite-sums, prp-double-sum, prp-sum-order | the reindexing line of the chapter's prerequisite ledger (k = m form of fd2:def-sum-product)
exr-cauchy-schwarz-and-the-triangle-inequality-c2 (solution): a sum of non-negative terms is >= 0 | prp-sum-order (b) with m = -1 (the empty sum is 0), cited as prp-sum-order (b)
exr-cauchy-schwarz-and-the-triangle-inequality-c2 (solution): squares are non-negative | fd3:prp-ordered-ring-rules (e), cited in the Uses line
-->
