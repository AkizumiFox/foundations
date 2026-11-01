# Hyperplanes and Nearest Points

Section 10.1 described a line by a parametrization, one free parameter. In the plane a line is also the solution set of one equation \( a_1 x_1 + a_2 x_2 = c \). This section takes one linear equation \( \inner{a}{x} = c \) in any \( \nR^n \) and names its solution set, a hyperplane. Distances to a hyperplane, and to a line, then have exact formulas. The tool throughout is the expansion of Chapter 9: a condition on distances becomes, after squaring and expanding, a linear condition on \( x \).

## Hyperplanes

Chapter 9 met equations of this kind twice. The vectors orthogonal to a fixed \( a \) are the solutions of \( \inner{a}{x} = 0 \) (@def-orthogonal-rn). The points equidistant from two given points satisfy an equation \( \inner{x}{b - a} = \text{constant} \) (@exr-length-and-distance-b3). In \( \nR^2 \) such a set is a line. In \( \nR^3 \) it is not: the opening of Section 10.1 found three points of \( \{ x_1 + x_2 + x_3 = 1 \} \) on no common line. The solution set of one equation deserves its own name.

Here is a small case. Take \( a = (1, 1, 1) \) and \( c = 1 \) in \( \nR^3 \), so the equation is \( x_1 + x_2 + x_3 = 1 \). The points \( (1, 0, 0) \), \( (0, 1, 0) \) and \( (0, 0, 1) \) satisfy it. The point \( 0 \) gives \( 0 < 1 \), and the point \( (1, 1, 1) \) gives \( 3 > 1 \). So these two points lie on opposite sides of the solution set.

*A hyperplane is the set where one non-zero linear expression takes one value.*

::: {#def-hyperplane-rn}
[Hyperplane]

Let \( a \in \nR^n \) with \( a \ne 0 \), and let \( c \in \nR \). The set
\[
H_{a,c} \coloneqq \{ x \in \nR^n : \inner{a}{x} = c \}
\]
is a **hyperplane**, and \( a \) is **a normal vector** of it. The sets \( \{ x : \inner{a}{x} \le c \} \) and \( \{ x : \inner{a}{x} \ge c \} \) are the two **closed half-spaces** of \( H_{a,c} \); with \( < \) and \( > \) **strictly**, they are the two **open half-spaces**, or the two **sides** of \( H_{a,c} \).
:::

In words: one vector \( a \), which must be **non-zero**, and one number \( c \) give one equation, and the hyperplane is everything that satisfies it. A subset of \( \nR^n \) is a hyperplane if it equals \( H_{a,c} \) for **some** such pair.

A hyperplane is never empty. The point
\[
p_0 \coloneqq \frac{c}{\norm{a}^2} \, a
\]
is defined, since \( \norm{a}^2 > 0 \) by @prp-norm-basic-rn (a), (c). It lies on the hyperplane: \( \inner{a}{p_0} = (c/\norm{a}^2)\norm{a}^2 = c \) by linearity (@prp-dot-product-laws-rn (b)). By linearity again, \( \inner{a}{x} - c = \inner{a}{x - p_0} \), so
\[
x \in H_{a,c} \iff x - p_0 \perp a .
\]
The hyperplane is the set of points reached from \( p_0 \) by a step orthogonal to \( a \).

**Examples.**

- **\( n = 1 \).** For \( a \ne 0 \) in \( \nR \), \( H_{a,c} = \{ c/a \} \): a hyperplane of the line is one point. Its sides are the two open rays.
- **\( n = 2 \).** \( H_{(1,1),1} \) is the line \( x_1 + x_2 = 1 \). We will see shortly that every hyperplane of \( \nR^2 \) is a line.
- **Coordinate hyperplanes.** \( H_{e_k, 0} = \{ x : x_k = 0 \} \) by @prp-dot-product-laws-rn (d). In \( \nR^3 \), \( H_{e_3, 0} \) is the plane of the first two axes.

**What goes wrong when \( a = 0 \).** Change \( a = (1, 1) \) to \( a = (0, 0) \). Then \( \inner{0}{x} = 0 \) for every \( x \) (@prp-dot-product-laws-rn (e)), so \( \{ x : \inner{0}{x} = c \} \) is \( \nR^n \) when \( c = 0 \) and empty when \( c \ne 0 \). Neither looks like the sets above, and the formula for \( p_0 \) would divide by \( 0 \). The clause \( a \ne 0 \) is what fails.

**Why "a" normal and not "the" normal.** The equations \( x_1 + x_2 = 1 \) and \( 2x_1 + 2x_2 = 2 \) have the same solutions. So one hyperplane has many pairs \( (a, c) \), and the next result says exactly how many.

::: {#prp-hyperplane-normals}
[The Normals of a Hyperplane]

Let \( a, a' \in \nR^n \) be non-zero and \( c, c' \in \nR \). Then \( H_{a,c} = H_{a',c'} \) if and only if \( (a', c') = (\lambda a, \lambda c) \) for some real \( \lambda \ne 0 \).
:::

::: {.idea}
The direction \( (\Leftarrow) \) multiplies an equation by \( \lambda \). For \( (\Rightarrow) \), the equation \( \inner{a'}{x} = c' \) must hold at every \( p_0 + w \) with \( w \perp a \), so \( a' \) is orthogonal to everything orthogonal to \( a \). Subtracting the projection (@exm-method-subtract-the-projection) produces a vector orthogonal to \( a \) from \( a' \) itself, and that vector must be \( 0 \).
:::

::: {.proof}
\( (\Leftarrow) \) If \( a' = \lambda a \) and \( c' = \lambda c \) with \( \lambda \ne 0 \), then \( \inner{a'}{x} = \lambda\inner{a}{x} \) by linearity, and \( \lambda\inner{a}{x} = \lambda c \) holds if and only if \( \inner{a}{x} = c \), multiplying by \( \lambda \) or by \( 1/\lambda \).

\( (\Rightarrow) \) Suppose \( H_{a,c} = H_{a',c'} \), and let \( p_0 = (c/\norm{a}^2) a \). For every \( w \perp a \), the point \( p_0 + w \) lies in \( H_{a,c} \), hence in \( H_{a',c'} \): \( \inner{a'}{p_0 + w} = c' \). Taking \( w = 0 \) gives \( \inner{a'}{p_0} = c' \), and subtracting, \( \inner{a'}{w} = 0 \) for every \( w \perp a \).

Let \( \mu \coloneqq \inner{a'}{a}/\norm{a}^2 \) and \( w \coloneqq a' - \mu a = a' - \operatorname{proj}_a a' \). By @thm-projection-closest-point (a), \( w \perp a \), so \( \inner{a'}{w} = 0 \). Hence, by linearity,
\[
\norm{w}^2 = \inner{a' - \mu a}{w} = \inner{a'}{w} - \mu \inner{a}{w} = 0 - 0 = 0 ,
\]
and \( w = 0 \), since only the zero vector has norm \( 0 \). So \( a' = \mu a \). Since \( a' \ne 0 \), \( \mu \ne 0 \). Finally \( c' = \inner{a'}{p_0} = \mu \inner{a}{p_0} = \mu c \). This proves the claim with \( \lambda = \mu \).

::: {.uses}
@prp-dot-product-laws-rn (b): linearity; @prp-norm-basic-rn (a): norm zero only at 0.
:::
:::

::: {.warning}
**A hyperplane has many normal vectors, and \( a = 0 \) gives none.** \( H_{(1,1),1} = H_{(2,2),2} = H_{(-1,-1),-1} \). "The normal" of a hyperplane means "a normal": it is fixed only up to a non-zero factor (@prp-hyperplane-normals). So a formula that uses a normal, such as the distance and nearest-point formulas below, is only meaningful if it gives the same answer for \( (\lambda a, \lambda c) \) as for \( (a, c) \). We check that it does. And \( a = 0 \) is excluded on purpose: \( \{ x : \inner{0}{x} = c \} \) is \( \emptyset \) or \( \nR^n \), and neither is a hyperplane. Indeed, every \( H_{a,c} \) contains \( p_0 \) and misses \( p_0 + a \), where the value is \( c + \norm{a}^2 \ne c \).
:::

In the plane, hyperplanes and lines are the same sets, and each description converts into the other by swapping two coordinates and changing one sign.

::: {#exm-lines-in-the-plane}
[Lines of the Plane Are Its Hyperplanes]

Work in \( \nR^2 \).

::: {.enumerate options="label=(\alph*)"}
1. For \( a \ne 0 \), \( H_{a,c} = p_0 + \nR(-a_2, a_1) \), where \( p_0 = (c/\norm{a}^2) a \).
2. For \( v \ne 0 \) and any \( p \), \( p + \nR v = H_{a,c} \) with \( a \coloneqq (-v_2, v_1) \) and \( c \coloneqq \inner{a}{p} \).
:::
:::

::: {.solution}
(a) Since \( a \ne 0 \), also \( (-a_2, a_1) \ne 0 \), so the right side is a line (@def-line-rn). \( (\supseteq) \) \( \inner{a}{(-a_2, a_1)} = -a_1 a_2 + a_2 a_1 = 0 \), so \( \inner{a}{p_0 + t(-a_2, a_1)} = c + 0 = c \). \( (\subseteq) \) Let \( x \in H_{a,c} \) and \( w \coloneqq x - p_0 \). Then \( a_1 w_1 + a_2 w_2 = 0 \). Put \( t \coloneqq (a_1 w_2 - a_2 w_1)/\norm{a}^2 \). Using \( a_2 w_2 = -a_1 w_1 \) and \( a_1 w_1 = -a_2 w_2 \),
\[
\begin{aligned}
-t a_2 &= \frac{a_2^2 w_1 - a_1 (a_2 w_2)}{\norm{a}^2} = \frac{(a_2^2 + a_1^2) w_1}{\norm{a}^2} = w_1 , \\
t a_1 &= \frac{a_1^2 w_2 - a_2 (a_1 w_1)}{\norm{a}^2} = \frac{(a_1^2 + a_2^2) w_2}{\norm{a}^2} = w_2 .
\end{aligned}
\]
So \( x = p_0 + t(-a_2, a_1) \).

(b) \( a = (-v_2, v_1) \ne 0 \) since \( v \ne 0 \), and \( \inner{a}{v} = -v_2 v_1 + v_1 v_2 = 0 \). So \( \inner{a}{p + tv} = \inner{a}{p} = c \): the line lies in \( H_{a,c} \). By (a), \( H_{a,c} = p_0 + \nR(-a_2, a_1) = p_0 + \nR(-v) \). As \( p \in H_{a,c} \), \( p = p_0 - sv \) for some \( s \), so \( p_0 = p + sv \in p + \nR v \); and \( -v = (-1)v \). By @prp-line-parametrizations, \( p_0 + \nR(-v) = p + \nR v \).
:::

So in \( \nR^2 \) the two descriptions are interchangeable: a direction \( v \) gives the normal \( (-v_2, v_1) \), and a normal \( a \) gives the direction \( (-a_2, a_1) \). In \( \nR^3 \) this fails. The hyperplane \( H_{(1,1,1),1} \) contains \( (1, 0, 0) \), \( (0, 1, 0) \) and \( (0, 0, 1) \), and the opening of Section 10.1 showed that no line contains all three. **A hyperplane of \( \nR^3 \) is not a line.**

::: {.check}
Write the line through \( (1, 3) \) and \( (4, -1) \) as an equation \( a_1 x_1 + a_2 x_2 = c \).
:::

::: {.solution}
A direction is \( v = (4, -1) - (1, 3) = (3, -4) \). By @exm-lines-in-the-plane (b), a normal is \( (4, 3) \) and \( c = 4 \cdot 1 + 3 \cdot 3 = 13 \). So the line is \( 4x_1 + 3x_2 = 13 \). Check at the second point: \( 16 - 3 = 13 \).

::: {.uses}
@prp-line-through-two-points: direction \( q - p \).
:::
:::

## Equidistant points

At the end of Section 10.1 we found a point at equal distances from \( p \) and \( q \) that is not their midpoint, and asked for all such points. Chapter 9 found their equation in @exr-length-and-distance-b3. Here that set is named as a hyperplane. Its two sides are the points nearer to \( p \) and the points nearer to \( q \).

A small case first. In \( \nR^2 \), take \( p = (0, 0) \) and \( q = (2, 0) \). A point \( x \) is equally far from both exactly when \( x_1^2 + x_2^2 = (x_1 - 2)^2 + x_2^2 \), that is, when \( 4x_1 = 4 \), or \( x_1 = 1 \). This is a line through the midpoint \( (1, 0) \). The points with \( x_1 < 1 \) are nearer to \( p \).

::: {#prp-perpendicular-bisector}
[The Perpendicular Bisector]

Let \( p, q \in \nR^n \) with \( p \ne q \), and let \( c \coloneqq \frac12 \bigl( \norm{q}^2 - \norm{p}^2 \bigr) \). Then
\[
\{ x \in \nR^n : \norm{x - p} = \norm{x - q} \} = H_{q - p, \, c} ,
\]
a hyperplane that contains the midpoint \( \frac12 (p + q) \). Moreover, \( \norm{x - p} < \norm{x - q} \) if and only if \( \inner{q - p}{x} < c \).
:::

This hyperplane is the **perpendicular bisector** of \( p \) and \( q \).

::: {.idea}
Expand the square (@exm-method-expand-the-square): compare squares instead of norms. The two squared norms both contain \( \norm{x}^2 \), which cancels, and what is left of their difference is linear in \( x \).
:::

::: {.proof}
For non-negative reals \( s, u \), we have \( s < u \) if and only if \( s^2 < u^2 \). Since the order of \( \nR \) is total, also \( s = u \) if and only if \( s^2 = u^2 \). Norms are non-negative, so both claims may be checked on squares. By @eq-expand-norm-squared and linearity,
\[
\begin{aligned}
\norm{x - p}^2 - \norm{x - q}^2
&= \bigl( \norm{x}^2 - 2\inner{x}{p} + \norm{p}^2 \bigr) - \bigl( \norm{x}^2 - 2\inner{x}{q} + \norm{q}^2 \bigr) \\
&= 2\inner{q - p}{x} - 2c .
\end{aligned}
\]
So \( \norm{x - p}^2 = \norm{x - q}^2 \) if and only if \( \inner{q - p}{x} = c \), and \( \norm{x - p}^2 < \norm{x - q}^2 \) if and only if \( \inner{q - p}{x} < c \). Since \( p \ne q \), \( q - p \ne 0 \), so \( H_{q - p, c} \) is a hyperplane. For the midpoint, linearity and symmetry give \( \inner{q - p}{p + q} = \norm{q}^2 - \norm{p}^2 \), so \( \inner{q - p}{\frac12 (p + q)} = c \).

::: {.uses}
@fd3:prp-ordered-ring-rules (g), (i): squares keep order, order is total; @prp-norm-basic-rn (a): norms are non-negative.
:::
:::

The open half-space \( \inner{q - p}{x} < c \) is the side of the bisector that contains \( p \): the points strictly nearer to \( p \) than to \( q \). The midpoint is the only point of the segment \( [p, q] \) on the bisector. Indeed, for a point of \( [p, q] \) the two distances add up to \( \norm{p - q} \), by @thm-betweenness. If they are also equal, the point is the midpoint (@cor-point-pinned-on-segment). For \( n \ge 2 \), though, the bisector has many other points.

::: {.check}
Find the points of \( \nR^2 \) equidistant from \( (0, 0) \) and \( (2, 4) \).
:::

::: {.solution}
Here \( q - p = (2, 4) \) and \( c = \frac12 (20 - 0) = 10 \), so the set is \( 2x_1 + 4x_2 = 10 \), that is, \( x_1 + 2x_2 = 5 \) (the same hyperplane, by @prp-hyperplane-normals with \( \lambda = \frac12 \)). The midpoint \( (1, 2) \) satisfies it: \( 1 + 4 = 5 \).
:::

## Nearest points

Chapter 9 found the point of a line **through the origin** nearest to a given point (@thm-projection-closest-point). A general line \( p + \nR v \) is the line \( \nR v \) slid by \( p \), and distances do not change under sliding (@prp-distance-basic-rn (c)). So the answer carries over: slide \( x \) by \( -p \), project, slide back.

For example, take the horizontal line \( (0, 1) + \nR(1, 0) \) in \( \nR^2 \) and the point \( x = (3, 5) \). The point of the line nearest to \( x \) is \( (3, 1) \), straight below \( x \), at distance \( 4 \). The step from it to \( x \) is \( (0, 4) \), orthogonal to the direction \( (1, 0) \).

::: {#prp-nearest-point-on-line}
[The Nearest Point on a Line]

Let \( L = p + \nR v \) with \( v \ne 0 \), let \( x \in \nR^n \), and put
\[
t_0 \coloneqq \frac{\inner{x - p}{v}}{\norm{v}^2} , \qquad m \coloneqq p + t_0 v .
\]
Then \( x - m \perp v \), and for every \( t \in \nR \),
\[
\norm{x - (p + tv)}^2 = \norm{x - m}^2 + (t - t_0)^2 \norm{v}^2 .
\]
Hence \( m \) is the **unique** point of \( L \) nearest to \( x \).
:::

::: {.proof}
Apply @thm-projection-closest-point to the vectors \( x - p \) and \( v \ne 0 \). Its number is \( t_0 \), and \( x - m = (x - p) - t_0 v \). Part (a) gives \( x - m \perp v \). Part (b), since \( x - (p + tv) = (x - p) - tv \), gives the identity, and with it \( \norm{x - (p + tv)} \ge \norm{x - m} \), with equality if and only if \( t = t_0 \), that is, if and only if \( p + tv = m \).
:::

Since \( m \) is described as the nearest point, it depends only on \( L \) and \( x \), not on the parametrization used to compute it. The number \( \norm{x - m} \) is the **distance from \( x \) to \( L \)**. For \( p = 0 \) this is the computation of @exm-distance-to-a-line-through-the-origin.

For a hyperplane the roles turn around. On a line we search along the direction \( v \) and the error is orthogonal to \( v \). On a hyperplane the error should be **parallel** to the normal \( a \): from \( x \), move along \( a \) until the equation \( \inner{a}{x} = c \) holds.

For example, take \( x_1 + x_2 = 2 \) in \( \nR^2 \), so \( a = (1, 1) \), and the point \( x = (3, 3) \). Moving to \( x - s(1, 1) \) changes the value \( x_1 + x_2 = 6 \) by \( -2s \). The value is \( 2 \) when \( s = 2 \), at the point \( (1, 1) \). Its distance from \( x \) is \( \norm{(2, 2)} = 2\sqrt 2 \).

::: {#prp-nearest-point-on-hyperplane}
[Distance to a Hyperplane]

Let \( a \ne 0 \), \( c \in \nR \) and \( x \in \nR^n \), and put
\[
x^* \coloneqq x - \frac{\inner{a}{x} - c}{\norm{a}^2} \, a .
\]
Then \( x^* \in H_{a,c} \), and for every \( y \in H_{a,c} \),
\[
\norm{x - y}^2 = \norm{x - x^*}^2 + \norm{x^* - y}^2 .
\]
Hence \( x^* \) is the **unique** point of \( H_{a,c} \) nearest to \( x \), and the distance from \( x \) to \( H_{a,c} \) is
\[
\norm{x - x^*} = \frac{\abs{\inner{a}{x} - c}}{\norm{a}} .
\]
:::

::: {.proof}
Write \( s \coloneqq (\inner{a}{x} - c)/\norm{a}^2 \), so \( x^* = x - sa \). By linearity, \( \inner{a}{x^*} = \inner{a}{x} - s\norm{a}^2 = c \), so \( x^* \in H_{a,c} \). Let \( y \in H_{a,c} \). Then \( x - y = (x - x^*) + (x^* - y) \), where \( x - x^* = sa \) and \( \inner{a}{x^* - y} = c - c = 0 \). Hence \( \inner{x - x^*}{x^* - y} = s \cdot 0 = 0 \), and Pythagoras (@prp-pythagoras-rn) gives the identity. The identity shows \( \norm{x - y}^2 \ge \norm{x - x^*}^2 \). Equality holds if and only if \( \norm{x^* - y} = 0 \), that is, \( y = x^* \). Comparing squares of non-negative numbers, as in the proof of @prp-perpendicular-bisector, gives the same for the norms. Finally, since \( \norm{sa} = \abs{s} \, \norm{a} \),
\[
\norm{x - x^*} = \abs{s} \, \norm{a} = \frac{\abs{\inner{a}{x} - c}}{\norm{a}^2} \, \norm{a} = \frac{\abs{\inner{a}{x} - c}}{\norm{a}} ,
\]
using \( \abs{u/w} = \abs{u}/w \) for \( w > 0 \).

::: {.uses}
@prp-norm-basic-rn (a), (b): norm zero only at 0, \( \norm{sa} = \abs{s}\norm{a} \); @fd3:prp-absolute-value-ordered-field (b): \( \abs{u/w} = \abs{u}/\abs{w} \).
:::
:::

The formula does not depend on which normal is used. Replacing \( (a, c) \) by \( (\lambda a, \lambda c) \) multiplies the numerator \( \abs{\inner{a}{x} - c} \) by \( \abs{\lambda} \) and the denominator \( \norm{a} \) by \( \abs{\lambda} \); in \( x^* \) the coefficient is multiplied by \( \lambda/\lambda^2 \) and the vector by \( \lambda \). Nothing changes. The sign of \( \inner{a}{x} - c \), which the absolute value discards, says on which side of the hyperplane \( x \) lies.

::: {.check}
Find the distance from \( (1, 2, 3) \) to the hyperplane \( x_1 + x_2 + x_3 = 0 \), and the nearest point.
:::

::: {.solution}
Here \( a = (1, 1, 1) \), \( c = 0 \), \( \inner{a}{x} - c = 6 \) and \( \norm{a}^2 = 3 \). So \( x^* = (1, 2, 3) - 2(1, 1, 1) = (-1, 0, 1) \), which satisfies \( -1 + 0 + 1 = 0 \), and the distance is \( 6/\sqrt 3 = 2\sqrt 3 \) (as \( (2\sqrt 3)^2 = 12 = 36/3 \)).
:::

## Spheres meet lines; segments cross hyperplanes

A sphere is the set of points at one fixed distance from a center. In the plane, the points at distance \( 1 \) from the origin form the unit circle \( x_1^2 + x_2^2 = 1 \). On the number line, the points at distance \( r \) from \( c \) are the two points \( c \pm r \).

::: {#def-sphere-rn}
[Sphere]

For \( c \in \nR^n \) and a real \( r > 0 \), the **sphere** with center \( c \) and radius \( r \) is \( S(c, r) \coloneqq \{ x \in \nR^n : \norm{x - c} = r \} \). In \( \nR^2 \) a sphere is called a **circle**.
:::

So the unit circle is \( S(0, 1) \) in \( \nR^2 \).

How many points can a line share with a sphere? Try the unit circle and the horizontal line \( x_2 = h \). A common point has \( x_1^2 = 1 - h^2 \). So there are two common points if \( \abs{h} < 1 \), one if \( \abs{h} = 1 \), and none if \( \abs{h} > 1 \). Here \( \abs{h} \) is the distance from the center to the line. In general, too, the answer depends only on that distance.

::: {#prp-line-meets-sphere}
[A Line Meets a Sphere]

Let \( L = p + \nR v \) with \( v \ne 0 \), let \( c \in \nR^n \) and \( r > 0 \), and let \( m = p + t_0 v \) be the point of \( L \) nearest to \( c \) and \( d \coloneqq \norm{c - m} \) its distance (@prp-nearest-point-on-line). Then \( L \cap S(c, r) \) is

::: {.enumerate options="label=(\alph*)"}
1. empty if \( d > r \);
2. \( \{ m \} \) if \( d = r \);
3. the two points \( p + \bigl( t_0 \pm \sqrt{r^2 - d^2}/\norm{v} \bigr) v \) if \( d < r \).
:::
:::

::: {.idea}
Parametrize (@exm-method-parametrize): the point \( p + tv \) lies on the sphere exactly when one equation in \( t \) holds. The identity of @prp-nearest-point-on-line makes that equation a square equal to a number, \( (t - t_0)^2 = k \), and the sign of \( k \) decides everything.
:::

::: {.proof}
Apply @prp-nearest-point-on-line to the point \( c \). Since \( \norm{y - c} = \norm{c - y} \) for every \( y \), its identity reads
\[
\norm{(p + tv) - c}^2 = d^2 + (t - t_0)^2 \norm{v}^2 \quad \text{for every } t \in \nR .
\]
Both \( \norm{(p + tv) - c} \) and \( r \) are non-negative, so we may compare squares, as in the proof of @prp-perpendicular-bisector. Thus \( p + tv \in S(c, r) \) if and only if
\[
(t - t_0)^2 = k , \qquad k \coloneqq \frac{r^2 - d^2}{\norm{v}^2} .
\]
Since \( d, r \ge 0 \), @fd3:prp-ordered-ring-rules (g) and totality give: \( k < 0 \) if \( d > r \), \( k = 0 \) if \( d = r \), \( k > 0 \) if \( d < r \).

(a) A square is never negative (@fd3:prp-ordered-ring-rules (e)), so for \( k < 0 \) no \( t \) works.

(b) For \( k = 0 \), \( (t - t_0)^2 = 0 \) forces \( t = t_0 \) (@fd3:prp-ordered-ring-rules (f)), and the only common point is \( m \).

(c) For \( k > 0 \), let \( \rho \coloneqq \sqrt k \), the non-negative real whose square is \( k \) (@fd3:prp-cof-square-roots). Then \( \rho > 0 \), since \( \rho \ge 0 \) and \( \rho^2 = k \ne 0 \). The equation \( (t - t_0)^2 = \rho^2 \) says \( (t - t_0 - \rho)(t - t_0 + \rho) = 0 \). So \( t = t_0 + \rho \) or \( t = t_0 - \rho \) (@fd3:prp-ordered-ring-rules (f)), and both work. They differ, as \( \rho > 0 \). Distinct parameters give distinct points: \( p + tv = p + uv \) gives \( \abs{t - u}\,\norm{v} = 0 \), so \( t = u \). Finally \( \rho = \sqrt{r^2 - d^2}/\norm{v} \), since the right side is non-negative and its square is \( k \). Here we use that the non-negative square root is unique.

::: {.uses}
@prp-distance-basic-rn (b): distance is symmetric. @fd3:thm-reals-complete-ordered-field: square roots exist in \( \nR \). @fd3:prp-cof-square-roots: the root is unique. @prp-norm-basic-rn (b): \( \norm{sv} = \abs{s}\norm{v} \).
:::
:::

When \( d = r \) the line is **tangent** to the sphere at \( m \). Exercise B3 shows that the tangent lines at a point \( m \) of the sphere are exactly the lines through \( m \) whose direction is orthogonal to \( m - c \).

The last result of the section is about segments. If \( p \) and \( q \) are on opposite sides of a hyperplane, the segment between them must cross it, and it crosses exactly once. For example, \( p = (0, 0) \) and \( q = (4, 0) \) lie on opposite sides of the line \( x_1 = 1 \). The point \( (1 - t)p + tq = (4t, 0) \) is on the line only for \( t = 1/4 \), at \( (1, 0) \).

::: {#prp-segment-crosses-hyperplane}
[A Segment Crosses a Hyperplane Once]

Let \( a \ne 0 \), \( c \in \nR \), and let \( p, q \in \nR^n \) with \( \inner{a}{p} < c < \inner{a}{q} \). Then \( [p, q] \) meets \( H_{a,c} \) in exactly one point, namely \( (1 - t_1)p + t_1 q \) with
\[
t_1 \coloneqq \frac{c - \inner{a}{p}}{\inner{a}{q} - \inner{a}{p}} \in (0, 1) .
\]
:::

::: {.proof}
Write \( \alpha \coloneqq \inner{a}{p} \) and \( \beta \coloneqq \inner{a}{q} \), so \( \alpha < c < \beta \). Every point of \( [p, q] \) is \( (1 - t)p + tq \) with \( t \in [0, 1] \) (@def-segment-rn), and by linearity
\[
\inner{a}{(1 - t)p + tq} = \alpha + t(\beta - \alpha) .
\]
This equals \( c \) if and only if \( t(\beta - \alpha) = c - \alpha \), and since \( \beta - \alpha > 0 \), if and only if \( t = t_1 \). Moreover \( 0 < c - \alpha < \beta - \alpha \), so \( 0 < t_1 < 1 \). Hence the point with parameter \( t_1 \) lies on \( [p, q] \) and on \( H_{a,c} \), and every common point has parameter \( t_1 \), so it is that point.
:::

Along the segment, the value of \( \inner{a}{x} \) grows from \( \alpha \) to \( \beta \) at a constant rate in \( t \), so it passes the level \( c \) once. When \( p \) and \( q \) are on the **same** side, the segment does not reach \( H_{a,c} \) at all. Exercise B4 (d) asks you to prove this. Section 10.3 calls a set **convex** if it contains the segment between any two of its points.

## Exercises

### A. Check your understanding

::: {#exr-hyperplanes-and-nearest-points-a1}
[A1]

Consider the hyperplane \( 2x_1 - x_2 + 2x_3 = 6 \) in \( \nR^3 \).

::: {.enumerate options="label=(\alph*)"}
1. Give a normal vector, and a second normal vector different from the first.
2. Find the distance from \( 0 \) to the hyperplane.
3. Find the point of the hyperplane nearest to \( 0 \).
:::
:::

::: {.solution}
(a) \( a = (2, -1, 2) \); for example \( -a = (-2, 1, -2) \), with the equation \( -2x_1 + x_2 - 2x_3 = -6 \) (@prp-hyperplane-normals).

(b) \( \norm{a} = \sqrt{4 + 1 + 4} = 3 \), so by @prp-nearest-point-on-hyperplane the distance is \( \abs{0 - 6}/3 = 2 \).

(c) \( x^* = 0 - \frac{0 - 6}{9} a = \frac23 (2, -1, 2) = (4/3, -2/3, 4/3) \). Check: \( 8/3 + 2/3 + 8/3 = 6 \), and \( \norm{x^*} = \frac23 \cdot 3 = 2 \).
:::

::: {#exr-hyperplanes-and-nearest-points-a2}
[A2]

Are \( 0 \) and \( (3, 0, 1) \) on the same side of the hyperplane \( 2x_1 - x_2 + 2x_3 = 6 \)? If not, where does the segment between them cross it?
:::

::: {.solution}
\( \inner{a}{0} = 0 < 6 \) and \( \inner{a}{(3, 0, 1)} = 6 + 0 + 2 = 8 > 6 \): opposite sides. By @prp-segment-crosses-hyperplane, \( t_1 = (6 - 0)/(8 - 0) = 3/4 \), and the crossing point is \( \frac34 (3, 0, 1) = (9/4, 0, 3/4) \). Check: \( 9/2 + 3/2 = 6 \).
:::

### B. Practice

::: {#exr-hyperplanes-and-nearest-points-b1}
[B1]

Find the point of the line \( (1, 0, 0) + \nR(1, 1, 1) \) nearest to \( (0, 3, 0) \), and the distance between them.
:::

::: {.solution}
By @prp-nearest-point-on-line with \( p = (1, 0, 0) \), \( v = (1, 1, 1) \), \( x = (0, 3, 0) \): \( x - p = (-1, 3, 0) \), \( \inner{x - p}{v} = 2 \), \( \norm{v}^2 = 3 \), so \( t_0 = 2/3 \) and \( m = (5/3, 2/3, 2/3) \). Then \( x - m = (-5/3, 7/3, -2/3) \), orthogonal to \( v \) as it should be (\( -5 + 7 - 2 = 0 \)), and
\[
\norm{x - m}^2 = \frac{25 + 49 + 4}{9} = \frac{26}{3} .
\]
Hence the distance is \( \sqrt{26/3} \).
:::

::: {#exr-hyperplanes-and-nearest-points-b2}
[B2]

Find the points where the line \( \nR(1, 2, 2) \) meets the sphere \( S((3, 0, 0), 3) \).
:::

::: {.solution}
Parametrize (@exm-method-parametrize): \( t(1, 2, 2) - (3, 0, 0) = (t - 3, 2t, 2t) \), whose squared norm is \( (t - 3)^2 + 8t^2 = 9t^2 - 6t + 9 \). Both norms being non-negative, the point is on the sphere if and only if \( 9t^2 - 6t + 9 = 9 \), that is, \( 3t(3t - 2) = 0 \), so \( t = 0 \) or \( t = 2/3 \). The points are \( 0 \) and \( (2/3, 4/3, 4/3) \).

The same answer from @prp-line-meets-sphere: \( t_0 = \inner{(3, 0, 0)}{(1, 2, 2)}/9 = 1/3 \), \( m = (1/3, 2/3, 2/3) \), \( d^2 = \norm{(8/3, -2/3, -2/3)}^2 = 72/9 = 8 < 9 \), so there are two points, at \( t = 1/3 \pm \sqrt{9 - 8}/3 \).
:::

::: {#exr-hyperplanes-and-nearest-points-b3}
[B3]

Let \( m \in S(c, r) \) and \( v \ne 0 \). Prove that the line \( m + \nR v \) meets \( S(c, r) \) only at \( m \) if and only if \( \inner{m - c}{v} = 0 \).
:::

::: {.solution}
Expand the square (@eq-expand-norm-squared), and use \( \norm{tv} = \abs{t}\,\norm{v} \) and \( \norm{m - c} = r \):
\[
\norm{(m + tv) - c}^2 = r^2 + 2t\inner{m - c}{v} + t^2 \norm{v}^2 .
\]
Comparing squares of non-negative numbers, \( m + tv \in S(c, r) \) if and only if this equals \( r^2 \), that is, \( t \bigl( 2\inner{m - c}{v} + t\norm{v}^2 \bigr) = 0 \), that is, \( t = 0 \) or \( t = t' \coloneqq -2\inner{m - c}{v}/\norm{v}^2 \). Distinct parameters give distinct points (as in the proof of @prp-line-meets-sphere), so \( m \) (at \( t = 0 \)) is the only common point if and only if \( t' = 0 \), if and only if \( \inner{m - c}{v} = 0 \). Hence the tangent lines at \( m \) are those whose direction is orthogonal to the radius \( m - c \).

::: {.uses}
@prp-norm-basic-rn (b): \( \norm{tv} = \abs{t}\norm{v} \).
:::
:::

::: {#exr-hyperplanes-and-nearest-points-b4}
[B4: Prove or disprove]

Throughout, \( a \ne 0 \).

::: {.enumerate options="label=(\alph*)"}
1. If \( c \ne c' \), then \( H_{a,c} \cap H_{a,c'} = \emptyset \).
2. Any two distinct hyperplanes of \( \nR^3 \) have a common point.
3. For \( n \ge 2 \) and \( p \ne q \) in \( \nR^n \), the only point equidistant from \( p \) and \( q \) is their midpoint.
4. If \( \inner{a}{p} < c \) and \( \inner{a}{q} < c \), then \( [p, q] \) does not meet \( H_{a,c} \).
5. The distance from \( 0 \) to \( H_{a,c} \) is \( \abs{c} \).
:::
:::

::: {.solution}
(a) **True.** A common point \( x \) would give \( c = \inner{a}{x} = c' \).

(b) **False.** \( H_{e_1, 0} = \{ x_1 = 0 \} \) and \( H_{e_1, 1} = \{ x_1 = 1 \} \) are disjoint by (a), so no point is common to both; they are distinct since both are non-empty.

(c) **False.** For \( p = (-1, 0) \) and \( q = (1, 0) \), @prp-perpendicular-bisector gives the set \( H_{(2, 0), 0} = \{ x_1 = 0 \} \), which contains \( (0, y) \) for every \( y \), not only the midpoint \( (0, 0) \).

(d) **True.** For \( t \in [0, 1] \), \( \inner{a}{(1 - t)p + tq} = (1 - t)\inner{a}{p} + t\inner{a}{q} \). Each of \( (1 - t)\inner{a}{p} \le (1 - t)c \) and \( t\inner{a}{q} \le tc \) holds, and the one whose weight is positive is strict (one of \( t \), \( 1 - t \) is positive); adding (@fd3:prp-ordered-ring-rules (b)), the value is \( < c \). So no point of \( [p, q] \) satisfies \( \inner{a}{x} = c \).

(e) **False.** For \( a = (2, 0) \) and \( c = 2 \), the hyperplane is \( \{ x_1 = 1 \} \), at distance \( \abs{0 - 2}/\norm{a} = 1 \ne 2 \) from \( 0 \) (@prp-nearest-point-on-hyperplane). The correct value is \( \abs{c}/\norm{a} \).
:::

### C. Going deeper

::: {#exr-hyperplanes-and-nearest-points-c1}
[C1: Chapter check: the circle through three points]

Prove that three non-collinear points \( p, q, r \) of \( \nR^2 \) lie on exactly one circle. Find it for \( (0, 0) \), \( (4, 0) \), \( (0, 2) \).
:::

::: {.solution}
[Hint 1]

Where must the center of such a circle lie, relative to \( p \) and \( q \)? Relative to \( q \) and \( r \)?
:::

::: {.solution}
[Hint 2]

A center \( z \) satisfies \( \norm{z - p} = \norm{z - q} \) and \( \norm{z - q} = \norm{z - r} \); by @prp-perpendicular-bisector, \( z \) lies on two lines of \( \nR^2 \). When do two lines of the plane meet in exactly one point?
:::

::: {.solution}
The three points are distinct: if two coincided, the line through the two distinct ones among them (or any line through the point, if all three coincide) would contain all three.

*Reduction.* \( S(z, \rho) \) contains \( p, q, r \) if and only if \( \norm{z - p} = \norm{z - q} = \norm{z - r} = \rho \). By @prp-perpendicular-bisector this puts \( z \) on \( B_1 \coloneqq H_{q - p, c_1} \) and on \( B_2 \coloneqq H_{r - q, c_2} \), with \( c_1, c_2 \) as there.

*The normals are not multiples.* If \( r - q = \lambda(q - p) \), then \( r = p + (1 + \lambda)(q - p) \) lies on the line \( p + \nR(q - p) \), which contains \( p \) and \( q \) too, against non-collinearity. So, by @exr-lines-and-segments-b2 (a), with \( a \coloneqq q - p \ne 0 \) and \( a' \coloneqq r - q \ne 0 \), \( D \coloneqq a_1 a'_2 - a_2 a'_1 \ne 0 \).

*The bisectors meet once.* By @exm-lines-in-the-plane (a), \( B_1 \) and \( B_2 \) are lines with directions \( (-a_2, a_1) \) and \( (-a'_2, a'_1) \). For these two directions, the expression of @exr-lines-and-segments-b2 (a) is \( (-a_2) a'_1 - a_1 (-a'_2) = D \ne 0 \). So neither direction is a multiple of the other. By part (b) of the same exercise, the lines meet in exactly one point \( z \).

*Existence.* \( z \in B_1 \cap B_2 \) gives \( \norm{z - p} = \norm{z - q} = \norm{z - r} \); call this number \( \rho \). Then \( \rho > 0 \): \( \rho = 0 \) would give \( z = p = q \). So \( p, q, r \in S(z, \rho) \).

*Uniqueness.* If \( p, q, r \in S(z', \rho') \), then \( z' \in B_1 \cap B_2 = \{ z \} \) by the reduction, and \( \rho' = \norm{z - p} = \rho \).

*The example.* \( B_1 \): \( q - p = (4, 0) \), \( c_1 = \frac12 (16 - 0) = 8 \), so \( 4x_1 = 8 \), \( x_1 = 2 \). \( B_2 \): \( r - q = (-4, 2) \), \( c_2 = \frac12 (4 - 16) = -6 \), so \( -4x_1 + 2x_2 = -6 \), and with \( x_1 = 2 \), \( x_2 = 1 \). The center is \( (2, 1) \), and \( \rho = \norm{(2, 1)} = \sqrt 5 \); indeed \( \norm{(2, 1) - (4, 0)}^2 = 4 + 1 \) and \( \norm{(2, 1) - (0, 2)}^2 = 4 + 1 \).

**What a complete answer needs.** (10 points)

- 2: reduces "\( p, q, r \) on \( S(z, \rho) \)" to "\( z \) on both perpendicular bisectors", citing the bisector result.
- 2: shows the normals \( q - p \), \( r - q \) are not multiples, from non-collinearity, and carries this to the directions of the two lines.
- 2: concludes the two lines meet in exactly one point, by the two-line criterion of Section 10.1 or by solving the two equations directly with \( D \ne 0 \).
- 2: existence: the common point is equidistant from all three, with \( \rho > 0 \).
- 2: uniqueness of the center and hence of the radius.

A route that solves the two bisector equations as a linear system in \( z \), with \( D \ne 0 \) shown, earns the middle three items at once (6 points).

**Slips that lose the step.** Each of these earns 0 for its step: assuming the bisectors meet without using non-collinearity; checking only the example; forgetting that the radius must be positive.
:::

<!-- dependency ledger
def-hyperplane-rn (claim): c/||a||^2 is defined since ||a||^2 > 0 | prp-norm-basic-rn (a), (c) (cited): ||a||^2 >= 0 and != 0, so > 0
def-hyperplane-rn (example): for n = 1, ax = c iff x = c/a (a != 0) | field arithmetic in R (fd3 field axioms), inline
prp-hyperplane-normals (proof): lambda u = lambda c iff u = c for lambda != 0 | multiply by 1/lambda (field axioms of R), inline
prp-hyperplane-normals (proof): mu != 0 since a' = mu a and a' != 0 | 0 * a = 0 (prp-vector-space-laws-rn), inline
exm-lines-in-the-plane (solution): (-a2, a1) != 0 iff a != 0 | coordinatewise, inline
prp-perpendicular-bisector (proof): s = u iff s^2 = u^2 for s, u >= 0 | fd3:prp-ordered-ring-rules (g) with totality (i) (cited, Uses line), as in Ch9's "comparing squares" (Section 3.3 prose)
prp-nearest-point-on-hyperplane (proof): |u / w| = |u| / w for w > 0 | fd3:prp-absolute-value-ordered-field (b) (cited, Uses line) with |w| = w for w > 0
prp-line-meets-sphere (proof): k < 0, = 0, > 0 according as d > r, d = r, d < r | fd3:prp-ordered-ring-rules (g), (i) (cited) and division by ||v||^2 > 0 (fd3:prp-ordered-ring-rules (c))
prp-line-meets-sphere (proof): (s - rho)(s + rho) = s^2 - rho^2 | commutative ring algebra in R, inline
prp-line-meets-sphere (proof): sqrt(r^2 - d^2)/||v|| has square k | fd3:lem-field-fraction-rules (b), inline
prp-segment-crosses-hyperplane (proof): 0 < c - alpha < beta - alpha gives 0 < t1 < 1 | fd3:prp-ordered-ring-rules (c) with 1/(beta - alpha) > 0, inline
exr-hyperplanes-and-nearest-points-b4 (solution): one of t, 1 - t is positive for t in [0, 1] | fd3:prp-ordered-ring-rules (i), inline
exr-hyperplanes-and-nearest-points-c1 (solution): two lines with non-parallel directions meet once | exr-lines-and-segments-b2 (cited; exercise cited from an exercise)
-->
