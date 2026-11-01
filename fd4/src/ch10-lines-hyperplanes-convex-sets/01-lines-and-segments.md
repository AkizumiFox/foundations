# Lines and Segments

In the plane a line is the set of solutions of one equation \( ax + by = c \). In \( \nR^3 \) one equation gives too much. The set \( \{ x \in \nR^3 : x_1 + x_2 + x_3 = 1 \} \) contains \( (1, 0, 0) \), \( (0, 1, 0) \) and \( (0, 0, 1) \), and these three points lie on no common line, as we check below. A line is thinner: a point moving along it is fixed by a single number. So this section describes lines by one parameter, not by equations. It then cuts out the part of a line between two points, the segment, and shows that "between" can be said with distances alone.

## Lines

Chapter 9 gave every vector \( v \) of \( \nR^n \) its multiples \( tv \), and the multiples of a non-zero \( v \) form the line through the origin in the direction of \( v \) (Section 9.6). A line that misses the origin is the same picture moved: start at a point \( p \) and add the multiples of \( v \).

*A line is a starting point plus all multiples of one non-zero direction.*

::: {#def-line-rn}
[Lines in \( \nR^n \)]

Let \( p, v \in \nR^n \) with \( v \ne 0 \). We write
\[
p + \nR v \coloneqq \{ p + tv : t \in \nR \} .
\]
A subset \( L \subseteq \nR^n \) is a **line** if \( L = p + \nR v \) for **some** \( p \in \nR^n \) and **some** \( v \ne 0 \). The map \( t \mapsto p + tv \) from \( \nR \) to \( L \) is a **parametrization** of \( L \), with **base point** \( p \) and **direction** \( v \); the number \( t \) is the **parameter** of the point \( p + tv \).
:::

In words: a line is any set of this form, and the pair \( (p, v) \) is a way of naming it, not part of it. The condition \( v \ne 0 \) is the one that bites. Without it, \( p + \nR 0 = \{p\} \), a single point. The sums and multiples are those of @def-vector-operations-rn.

For example, \( (1, 0, 0) + \nR(-1, 1, 0) \) is the set of points \( (1 - t, t, 0) \). Its points with parameters \( 0 \) and \( 1 \) are \( (1, 0, 0) \) and \( (0, 1, 0) \), and every point of it has third coordinate \( 0 \).

:::: {.check}
Decide each, using only the definition.

::: {.enumerate options="label=(\alph*)"}
1. Is a one-point set \( \{p\} \subseteq \nR^n \) a line?
2. Is \( \nR \) itself a line in \( \nR^1 = \nR \)?
3. Is \( (3, 5, 7) \) on the line \( (1, 1, 1) + \nR(1, 2, 3) \)?
4. Can one point of \( p + \nR v \) have two different parameters?
:::
::::

::: {.solution}
Part (d) first. If \( p + tv = p + uv \), then \( (t - u)v = 0 \), so \( \abs{t - u} \, \norm{v} = \norm{(t - u)v} = 0 \) by @prp-norm-basic-rn (b). Since \( v \ne 0 \), \( \norm{v} > 0 \) (@prp-norm-basic-rn (a)), and so \( \abs{t - u} = 0 \), that is, \( t = u \). So no: distinct parameters give distinct points.

(a) No. By (d), the points \( p + 0v \) and \( p + 1v \) of a line are different, so a line has at least two points. (b) Yes: \( \nR = 0 + \nR \cdot 1 \), with direction \( 1 \ne 0 \). (c) Yes: \( (1, 1, 1) + 2(1, 2, 3) = (3, 5, 7) \), so its parameter is \( t = 2 \).
:::

So for a fixed parametrization each point of the line has **exactly one** parameter. We use this without further comment.

A line has many names. \( (1, 0, 0) + \nR(-1, 1, 0) \) is also \( (0, 1, 0) + \nR(2, -2, 0) \): the base point may be any point of the line, and the direction may be scaled. The next result says that this is all the freedom there is.

::: {#prp-line-parametrizations}
[When Two Parametrizations Give the Same Line]

Let \( p, p' \in \nR^n \) and \( v, v' \in \nR^n \setminus \{0\} \). Then \( p + \nR v = p' + \nR v' \) if and only if \( p' \in p + \nR v \) and \( v' = \lambda v \) for some real \( \lambda \ne 0 \).
:::

::: {.idea}
For \( (\Rightarrow) \), two points of the second line, \( p' \) and \( p' + v' \), must lie on the first; subtracting their parametrizations exposes \( v' \) as a multiple of \( v \). For \( (\Leftarrow) \), rewrite a point of each line in the other's parametrization.
:::

::: {.proof}
\( (\Leftarrow) \) Let \( p' = p + sv \) and \( v' = \lambda v \) with \( \lambda \ne 0 \). For every \( t \in \nR \),
\[
p' + tv' = p + (s + t\lambda) v \in p + \nR v .
\]
Conversely, for every \( t \),
\[
p + tv = p' + \frac{t - s}{\lambda} \, v' \in p' + \nR v' ,
\]
since the right side is \( p + sv + (t - s)v \); the division is allowed because \( \lambda \ne 0 \). The two inclusions give equality.

\( (\Rightarrow) \) The points \( p' \) and \( p' + v' \) (parameters \( 0 \) and \( 1 \)) lie on \( p' + \nR v' = p + \nR v \). So \( p' = p + sv \) and \( p' + v' = p + uv \) for some \( s, u \in \nR \); in particular \( p' \in p + \nR v \). Subtracting, \( v' = (u - s)v \). If \( u - s \) were \( 0 \), then \( v' = 0v = 0 \), against the hypothesis \( v' \ne 0 \). So \( \lambda \coloneqq u - s \) is non-zero, as claimed.

::: {.uses}
@prp-vector-space-laws-rn (e), (h) (regrouping multiples), (i) (\( 0v = 0 \)).
:::
:::

The direction of a line is fixed only up to a non-zero factor, and the base point can be any of its points. Through two different points there is exactly one line.

::: {#prp-line-through-two-points}
[Two Points Determine a Line]

Let \( p, q \in \nR^n \) with \( p \ne q \). Then \( p + \nR(q - p) \) is a line containing \( p \) and \( q \), and it is the only line containing both.
:::

::: {.proof}
Since \( p \ne q \), the direction \( q - p \) is non-zero, so \( p + \nR(q - p) \) is a line; its points with parameters \( 0 \) and \( 1 \) are \( p \) and \( q \). Let \( r + \nR v \) be any line containing \( p \) and \( q \), say \( p = r + sv \) and \( q = r + uv \). Then \( q - p = (u - s)v \), and \( u \ne s \) because \( q \ne p \). So \( p \in r + \nR v \) and \( q - p = \lambda v \) with \( \lambda \coloneqq u - s \ne 0 \), and @prp-line-parametrizations gives \( r + \nR v = p + \nR(q - p) \).

::: {.uses}
@prp-vector-space-laws-rn (vector algebra).
:::
:::

::: {#def-collinear}
[Collinear Points]

Points of \( \nR^n \) are **collinear** if **one** line contains them all.
:::

By @prp-line-through-two-points, any two points are collinear. Three need not be. The only line through \( (1, 0, 0) \) and \( (0, 1, 0) \) is \( (1, 0, 0) + \nR(-1, 1, 0) \), whose points all have third coordinate \( 0 \); so \( (0, 0, 1) \) is not on it, and the three points of the opening are not collinear. In particular the solution set of \( x_1 + x_2 + x_3 = 1 \), which contains all three, is not a line.

## Meeting points

Exercise B2 proves that two lines in the plane whose directions are not multiples of each other meet in exactly one point. In space this fails. Two lines of \( \nR^3 \) are **skew** if they have no common point and neither direction is a multiple of the other. (If \( v' = \lambda v \) with \( v' \ne 0 \), then \( \lambda \ne 0 \) and \( v = \lambda^{-1} v' \), so "neither" is the same as "the first is not a multiple of the second".)

::: {#exm-two-lines-in-space}
[Two Lines in Space]

Let
\[
\begin{aligned}
L_1 &= (1, 0, 1) + \nR(1, 1, 0) , \\
L_2 &= (0, 2, 0) + \nR(1, 0, 1) , \\
L_3 &= (2, 1, 1) + \nR(0, 1, 1) .
\end{aligned}
\]
Do \( L_1 \) and \( L_2 \) meet? Do \( L_1 \) and \( L_3 \)?
:::

::: {.idea}
[Scratch work]

A common point of \( L_1 \) and \( L_2 \) is a point that has **some** parameter on \( L_1 \) and **some** parameter on \( L_2 \). Nothing says the two parameters are equal: the point with parameter \( 1 \) on one line may have parameter \( 5 \) on the other. So we need two letters, \( s \) for \( L_1 \) and \( t \) for \( L_2 \).

| We know | We want |
|---|---|
| \( x \in L_1 \): \( x = (1 + s, s, 1) \) for some \( s \) | is there such an \( x \)? |
| \( x \in L_2 \): \( x = (t, 2, t) \) for some \( t \) | find \( s, t \) with \( (1 + s, s, 1) = (t, 2, t) \) |
| equal triples: one equation per coordinate | \( 1 + s = t \), \( s = 2 \), \( 1 = t \): solve, then check all three |

We solve two of the equations and test the third.
:::

::: {.solution}
The points of \( L_1 \) are \( (1 + s, s, 1) \) and those of \( L_2 \) are \( (t, 2, t) \). They are equal if and only if
\[
1 + s = t , \qquad s = 2 , \qquad 1 = t .
\]
The second and third equations force \( s = 2 \) and \( t = 1 \), and then the first reads \( 3 = 1 \), which is false. So \( L_1 \cap L_2 = \emptyset \). The directions are not multiples: \( (1, 1, 0) = \lambda(1, 0, 1) \) would need \( \lambda = 1 \) from the first coordinate and \( \lambda = 0 \) from the third. So \( L_1 \) and \( L_2 \) are skew.

The points of \( L_3 \) are \( (2, 1 + u, 1 + u) \). Equality with \( (1 + s, s, 1) \) means
\[
1 + s = 2 , \qquad s = 1 + u , \qquad 1 = 1 + u .
\]
The third equation gives \( u = 0 \), the second then gives \( s = 1 \), and the first holds: \( 1 + 1 = 2 \). So \( L_1 \) and \( L_3 \) meet, at \( (1 + 1, 1, 1) = (2, 1, 1) \), the base point of \( L_3 \).
:::

Keep the pair \( L_1, L_2 \) in mind. Two lines in space can fail to meet although their directions are not multiples of each other. Exercise B2 shows that this cannot happen in the plane. The method used twice in the example is worth stating on its own.

::: {#exm-method-parametrize}
[Method: parametrize and solve]

**How it goes.** Give each line or segment its own parameter, with a different letter for each. Write "the point lies on both" as one equation per coordinate. Solve some of the equations, then check **every** equation with the values found. For a segment, also check that the parameter lies in \( [0, 1] \).

**When to use it.** Deciding whether a point lies on a line, a segment or a ray. Finding where two lines meet, or showing that they do not. Later, finding where a line meets a sphere or a hyperplane.

**Common mistakes.** Using one letter for both parameters looks only for a point reached "at the same time" on both lines, and so misses most meeting points. Solving two equations and forgetting to test the rest can produce a meeting point that does not exist.
:::

## Segments

The part of a line between two of its points is used constantly in analysis: a function is examined along it, or a set is asked to contain it. Starting at \( p \) and moving towards \( q \), the points \( p + t(q - p) \) with \( t \) from \( 0 \) to \( 1 \) run from \( p \) to \( q \).

*A segment is the part of the line from one point to another.*

::: {#def-segment-rn}
[Segment]

Let \( p, q \in \nR^n \). The **segment** from \( p \) to \( q \) is
\[
[p, q] \coloneqq \{ (1 - t)p + tq : t \in [0, 1] \} .
\]
Its **midpoint** is \( \frac12 (p + q) \), the point with \( t = \frac12 \).
:::

Three remarks. First, \( (1 - t)p + tq = p + t(q - p) \), so for \( p \ne q \) the segment is the part of the line \( p + \nR(q - p) \) with parameters in \( [0, 1] \). Second, \( [p, q] = [q, p] \): the point with \( t \) in the first is the point with \( 1 - t \) in the second, and \( t \in [0, 1] \) if and only if \( 1 - t \in [0, 1] \). Third, \( [p, p] = \{p\} \), since \( (1 - t)p + tp = p \). This one-point segment is allowed, and it is not a line. The midpoint is the point of Chapter 9 (@exm-midpoints-and-parallelograms), equally displaced from both ends.

**Segments and intervals.** The bracket \( [p, q] \) also names a closed interval of \( \nR \). For \( n = 1 \) the two readings agree when \( p \le q \). Every \( (1 - t)p + tq = p + t(q - p) \) with \( t \in [0, 1] \) lies between \( p \) and \( q \). For \( p < q \), every \( y \) with \( p \le y \le q \) has this form, with \( t \coloneqq (y - p)/(q - p) \). For \( p > q \), the segment \( [p, q] \) is the interval \( [q, p] \), while the interval \( [p, q] \) is empty. In this chapter \( [p, q] \) is a segment whenever \( p \) and \( q \) have been declared as points of \( \nR^n \).

A segment contains, with any two of its points, the segment between them. This is the first instance of the property that Section 10.3 names.

::: {#lem-subsegment}
[A Segment Contains Its Subsegments]

Let \( p, q \in \nR^n \). If \( x, y \in [p, q] \), then \( [x, y] \subseteq [p, q] \).
:::

::: {.idea}
Write \( x \) and \( y \) with their parameters on \( [p, q] \). A point of \( [x, y] \) then has a parameter on \( [p, q] \) that is an average of the two, and an average of two numbers in \( [0, 1] \) stays in \( [0, 1] \).
:::

::: {.proof}
Let \( x = p + s(q - p) \) and \( y = p + u(q - p) \) with \( s, u \in [0, 1] \), and let \( t \in [0, 1] \). Then
\[
(1 - t)x + ty = p + \bigl( (1 - t)s + tu \bigr)(q - p) .
\]
The numbers \( 1 - t \), \( t \), \( s \), \( u \) are all \( \ge 0 \), and \( s, u \le 1 \). Multiplying \( 0 \le s \le 1 \) by \( 1 - t \ge 0 \) keeps both inequalities, so \( 0 \le (1 - t)s \le (1 - t) \cdot 1 \). In the same way \( 0 \le tu \le t \cdot 1 \). Adding the two gives \( 0 \le (1 - t)s + tu \le (1 - t) + t = 1 \). So \( (1 - t)x + ty \in [p, q] \).

::: {.uses}
@prp-vector-space-laws-rn (the displayed identity); @fd3:prp-ordered-field-halves (d) (multiply by a number \( \ge 0 \)); @fd3:prp-ordered-ring-rules (b) (add inequalities).
:::
:::

::: {.check}
Is \( (2, 0, 1) \) on the segment \( [(1, -1, 2), (3, 0, 0)] \)?
:::

::: {.solution}
No. A point of the segment is \( (1, -1, 2) + t(2, 1, -2) \) with \( t \in [0, 1] \). For \( (2, 0, 1) \) this asks for \( (1, 1, -1) = t(2, 1, -2) \). The first coordinate forces \( t = \frac12 \), the second forces \( t = 1 \). No \( t \) works, so the point is not even on the line through the two ends.
:::

## Between by distances

For any three points the triangle inequality gives \( \norm{p - q} \le \norm{p - x} + \norm{x - q} \): the detour through \( x \) is never shorter. A picture suggests that the detour costs nothing exactly when \( x \) lies on the segment \( [p, q] \). Chapter 9 found exactly when the triangle inequality is an equality: \( \norm{u + w} = \norm{u} + \norm{w} \) holds if and only if \( u = 0 \) or \( w = cu \) for some real \( c \ge 0 \) (@thm-triangle-inequality-rn (a)). That is all we need.

::: {#thm-betweenness}
[Points Between Two Points]

Let \( p, q, x \in \nR^n \). Then
\[
x \in [p, q] \iff \norm{p - x} + \norm{x - q} = \norm{p - q} .
\]
Moreover, if \( x = (1 - t)p + tq \) with \( t \in [0, 1] \), then
\[
\norm{p - x} = t \norm{p - q} , \qquad \norm{x - q} = (1 - t) \norm{p - q} .
\]
:::

::: {.idea}
[Scratch work]

The direction \( (\Rightarrow) \) is a computation: the two pieces of the segment are multiples of \( q - p \) by \( t \) and \( 1 - t \). For \( (\Leftarrow) \) we have an equality and want a parameter. Name the two displacements, \( u \coloneqq x - p \) and \( w \coloneqq q - x \), so that \( u + w = q - p \), and plan with a table.

| We know | We want |
|---|---|
| \( \norm{p - x} + \norm{x - q} = \norm{p - q} \) | \( x = p + t(q - p) \) for some \( t \in [0, 1] \) |
| \( \norm{u} + \norm{w} = \norm{u + w} \), as \( \norm{-v} = \norm{v} \) | the same |
| \( u = 0 \), **or** \( w = cu \) with \( c \ge 0 \) (Chapter 9) | case \( u = 0 \): \( x = p \), \( t = 0 \) |
| \( w = cu \), so \( q - p = (1 + c)u \) | \( u = \frac{1}{1 + c}(q - p) \): \( t = \frac{1}{1 + c} \in (0, 1] \) |

The third row is the equality case of the triangle inequality. It turns one equation between numbers into a relation between vectors. The rest is solving for \( u \).
:::

::: {.proof}
\( (\Rightarrow) \) and the moreover clause. Let \( x = (1 - t)p + tq \) with \( t \in [0, 1] \). Then \( x - p = t(q - p) \) and \( q - x = (1 - t)(q - p) \). Since \( t \ge 0 \) and \( 1 - t \ge 0 \), the rule \( \norm{cv} = \abs{c} \, \norm{v} \) of @prp-norm-basic-rn (b) gives
\[
\norm{p - x} = \norm{x - p} = t \norm{q - p} , \qquad \norm{x - q} = (1 - t) \norm{q - p} .
\]
Here \( \norm{p - x} = \norm{x - p} \) and \( \norm{q - x} = \norm{x - q} \) are the same rule with \( c = -1 \). Also \( \norm{q - p} = \norm{p - q} \). This is the moreover clause, and adding the two equations gives \( \norm{p - x} + \norm{x - q} = (t + 1 - t) \norm{p - q} = \norm{p - q} \).

\( (\Leftarrow) \) Let \( u \coloneqq x - p \) and \( w \coloneqq q - x \), so that \( u + w = q - p \). Since \( \norm{-v} = \norm{v} \) for every \( v \), the hypothesis reads \( \norm{u} + \norm{w} = \norm{u + w} \). By @thm-triangle-inequality-rn (a), \( u = 0 \) or \( w = cu \) for some real \( c \ge 0 \).

*Case \( u = 0 \).* Then \( x = p = (1 - 0)p + 0q \in [p, q] \).

*Case \( w = cu \) with \( c \ge 0 \).* Then \( q - p = u + cu = (1 + c)u \). Since \( 1 + c \ge 1 > 0 \), the number \( t \coloneqq 1/(1 + c) \) exists and \( t > 0 \). Taking reciprocals of the positive numbers in \( 1 \le 1 + c \) reverses the inequality, so \( t \le 1 \). Multiplying by \( t \) gives \( u = t(q - p) \). So \( x = p + u = p + t(q - p) = (1 - t)p + tq \) with \( t \in [0, 1] \). This proves the theorem.

::: {.uses}
@prp-vector-space-laws-rn (vector algebra); @prp-norm-basic-rn (b) (\( \norm{cv} = \abs{c} \, \norm{v} \)); @fd3:prp-ordered-field-halves (c) (reciprocals reverse \( \le \)).
:::
:::

Where is \( c \ge 0 \) used? It makes \( 1 + c \) positive, so that \( t \) exists and lies in \( [0, 1] \). A negative multiplier would be a point of the line outside the segment, and the equality case rules it out.

The right side of the theorem mentions only distances, no sums of vectors and no parameters. That is the form of "between" that survives when \( \nR^n \) is replaced by any set with a distance, as in *Real Numbers, Metric Spaces, and Derivatives*. It is also why a map that preserves distances sends segments to segments, a fact proved in *Affine and Projective Geometry*.

::: {#exm-method-equality-case}
[Method: use the equality case]

**How it goes.** A known inequality \( A \le B \) is given, or proved, to hold with \( A = B \). Recall its **exact** equality condition. Typically it reads "one vector is a non-negative multiple of the other, or is zero". Write that condition with a named multiplier. Then solve for what you want, keeping every case of the condition.

**When to use it.** A sum of distances equals a distance. Cauchy–Schwarz holds with equality. A question asks for all extreme cases of an inequality.

**Common mistakes.** Dropping the sign condition loses the point: \( c \ge 0 \) is exactly what separates \( [p, q] \) from the rest of the line through \( p \) and \( q \). Forgetting the case \( u = 0 \) leaves a gap, because in that case no multiplier exists.
:::

The moreover clause of the theorem also tells us where on the segment a point sits: its distance from \( p \) fixes it.

::: {#cor-point-pinned-on-segment}
[A Point Is Pinned by Its Distances to the Ends]

Let \( p, q \in \nR^n \) and let \( s, r \ge 0 \) with \( s + r = \norm{p - q} \). Then exactly one \( x \in \nR^n \) satisfies \( \norm{p - x} = s \) and \( \norm{x - q} = r \). If \( p \ne q \), it is
\[
x = p + \frac{s}{\norm{p - q}} (q - p) ;
\]
if \( p = q \), it is \( p \).
:::

::: {.proof}
Let \( p \ne q \), so \( \norm{p - q} > 0 \) (@prp-norm-basic-rn (a)), and put \( t \coloneqq s/\norm{p - q} \). From \( 0 \le s \le s + r = \norm{p - q} \), dividing by the positive number \( \norm{p - q} \) gives \( 0 \le t \le 1 \). So the point \( x \coloneqq p + t(q - p) = (1 - t)p + tq \) lies on \( [p, q] \). By the moreover clause of @thm-betweenness, \( \norm{p - x} = t\norm{p - q} = s \) and \( \norm{x - q} = (1 - t)\norm{p - q} = \norm{p - q} - s = r \).

Now let \( y \) be any point with \( \norm{p - y} = s \) and \( \norm{y - q} = r \). Then \( \norm{p - y} + \norm{y - q} = \norm{p - q} \), so \( y \in [p, q] \) by @thm-betweenness, say \( y = (1 - t')p + t'q \) with \( t' \in [0, 1] \). The moreover clause gives \( s = t' \norm{p - q} \), so \( t' = t \) and \( y = x \). The case \( p = q \), where the formula would divide by \( 0 \), is treated next.
:::

::: {.second-reading title="The case p = q"}
If \( p = q \), then \( s + r = 0 \) with \( s, r \ge 0 \). If \( s > 0 \), then \( s + r > 0 \) by @fd3:prp-ordered-ring-rules (b), which is impossible; so \( s = 0 \), and then \( r = 0 \). A point with \( \norm{p - x} = 0 \) is \( p \) itself (@prp-norm-basic-rn (a)), and \( p \) does have both distances equal to \( 0 \). So \( p \) is the only such point. The formula of the main case cannot be used here: it divides by \( \norm{p - q} = 0 \).
:::

::: {.check}
Show that the midpoint of \( [p, q] \) is the only point of \( \nR^n \) at distance \( \frac12 \norm{p - q} \) from both \( p \) and \( q \).
:::

::: {.solution}
Take \( s = r = \frac12 \norm{p - q} \). Both are \( \ge 0 \) and \( s + r = \norm{p - q} \), so by @cor-point-pinned-on-segment exactly one point has these two distances. The midpoint, with \( t = \frac12 \), has them, by the moreover clause of @thm-betweenness. So it is that one point.
:::

Being the midpoint takes two equations, one for each distance. Keeping only "equally far from both ends" loses the point.

::: {.warning}
**Equal distances do not make a midpoint.** Let \( p = (-1, 0) \), \( q = (1, 0) \) and \( x = (0, 1) \). Then \( \norm{p - x} = \norm{(-1, -1)} = \sqrt 2 \) and \( \norm{x - q} = \norm{(-1, 1)} = \sqrt 2 \), so \( x \) is equally far from \( p \) and \( q \). But \( x \notin [p, q] \): every point \( (1 - t)p + tq \) has second coordinate \( 0 \). The sum \( 2\sqrt 2 \) is not \( \norm{p - q} = 2 \). Section 10.2 finds all points equally far from \( p \) and \( q \).
:::

## Exercises

### A. Check your understanding

:::: {#exr-lines-and-segments-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Parametrize the line through \( (1, -1, 2) \) and \( (3, 0, 0) \). Is \( (5, 1, -2) \) on it?
2. Find the midpoint of the segment between these two points.
:::
::::

::: {.solution}
(a) By @prp-line-through-two-points, the line is \( (1, -1, 2) + \nR(2, 1, -2) \), since \( (3, 0, 0) - (1, -1, 2) = (2, 1, -2) \). For \( t = 2 \), \( (1, -1, 2) + 2(2, 1, -2) = (5, 1, -2) \), so yes, with parameter \( 2 \).

(b) \( \frac12 \bigl( (1, -1, 2) + (3, 0, 0) \bigr) = \frac12 (4, -1, 2) = (2, -\frac12, 1) \).
:::

:::: {#exr-lines-and-segments-a2}
[A2]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( (1, 2) \), \( (3, 5) \) and \( (7, 11) \) are collinear, and find the one that lies between the other two.
2. In the proof of @thm-betweenness, direction \( (\Leftarrow) \), where is \( c \ge 0 \) used? Take \( p = 0 \), \( q = (1, 0) \) and \( x = (2, 0) \), a point of the line through \( p \) and \( q \). Which hypothesis of the theorem fails, and what does the equality case of the triangle inequality say about \( u = x - p \) and \( w = q - x \)?
:::
::::

::: {.solution}
(a) Put \( p = (1, 2) \) and \( v = (2, 3) \). Then \( (3, 5) = p + 1v \) and \( (7, 11) = p + 3v \), since \( (6, 9) = 3(2, 3) \). So all three lie on \( p + \nR v \), with parameters \( 0 \), \( 1 \), \( 3 \). The middle one is between the others: \( (3, 5) = (1, 2) + \frac13 \bigl( (7, 11) - (1, 2) \bigr) \), so \( (3, 5) \in [(1, 2), (7, 11)] \) with \( t = \frac13 \).

(b) It is used to see that \( 1 + c > 0 \), so that \( t = 1/(1 + c) \) is defined and lies in \( (0, 1] \). For \( x = (2, 0) \): \( \norm{p - x} + \norm{x - q} = 2 + 1 = 3 \ne 1 = \norm{p - q} \), so the hypothesis of \( (\Leftarrow) \) fails. Here \( u = (2, 0) \) and \( w = (-1, 0) = -\frac12 u \): \( w \) is a multiple of \( u \), but the multiplier is negative. The equality case of @thm-triangle-inequality-rn (a) needs \( c \ge 0 \), so it does not apply, in agreement with the strict inequality \( 1 < 3 \).
:::

### B. Practice

::: {#exr-lines-and-segments-b1}
[B1, used later]

Let \( p, v \in \nR^n \) with \( v \ne 0 \), and let \( a < b \) be real numbers. Prove that \( p + tv \in [p + av, p + bv] \) if and only if \( a \le t \le b \).
:::

::: {.solution}
\( (\Leftarrow) \) Let \( a \le t \le b \) and \( s \coloneqq (t - a)/(b - a) \), allowed since \( b - a > 0 \). From \( 0 \le t - a \le b - a \), dividing by \( b - a > 0 \) gives \( s \in [0, 1] \). Then
\[
(1 - s)(p + av) + s(p + bv) = p + \bigl( a + s(b - a) \bigr) v = p + tv ,
\]
so \( p + tv \in [p + av, p + bv] \).

\( (\Rightarrow) \) Let \( p + tv = (1 - s)(p + av) + s(p + bv) \) with \( s \in [0, 1] \). The right side is \( p + (a + s(b - a))v \). A point of \( p + \nR v \) has only one parameter, as shown after @def-line-rn, so \( t = a + s(b - a) \). Since \( 0 \le s(b - a) \le b - a \) (@fd3:prp-ordered-field-halves (d)), adding \( a \) gives \( a \le t \le b \).
:::

:::: {#exr-lines-and-segments-b2}
[B2, used later]

Let \( v, v' \in \nR^2 \) be non-zero.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( v' \) is a multiple of \( v \) if and only if \( v_1 v'_2 - v_2 v'_1 = 0 \).
2. Suppose \( v' \) is not a multiple of \( v \). Prove that for all \( p, p' \in \nR^2 \) the lines \( p + \nR v \) and \( p' + \nR v' \) meet in exactly one point.
:::
::::

::: {.solution}
(a) \( (\Rightarrow) \) If \( v' = \lambda v \), then \( v_1 v'_2 - v_2 v'_1 = v_1 \lambda v_2 - v_2 \lambda v_1 = 0 \).

\( (\Leftarrow) \) Let \( v_1 v'_2 = v_2 v'_1 \). If \( v_1 \ne 0 \), put \( \lambda \coloneqq v'_1/v_1 \). Then \( \lambda v_1 = v'_1 \) and \( \lambda v_2 = v'_1 v_2 / v_1 = v_1 v'_2 / v_1 = v'_2 \), so \( v' = \lambda v \). If \( v_1 = 0 \), then \( v_2 \ne 0 \) because \( v \ne 0 \), and the hypothesis reads \( 0 = v_2 v'_1 \), so \( v'_1 = 0 \) (no zero divisors, @fd3:prp-ordered-ring-rules (f)). Put \( \lambda \coloneqq v'_2/v_2 \): then \( \lambda v_1 = 0 = v'_1 \) and \( \lambda v_2 = v'_2 \).

(b) By @exm-method-parametrize, with \( s \) on the first line and \( t \) on the second. Let \( d \coloneqq p' - p \). Then \( p + sv = p' + tv' \) if and only if
\[
s v_1 - t v'_1 = d_1 , \qquad s v_2 - t v'_2 = d_2 .
\]
Let \( D \coloneqq v_1 v'_2 - v_2 v'_1 \), which is non-zero by (a). Multiplying the first equation by \( v'_2 \), the second by \( v'_1 \), and subtracting eliminates \( t \); multiplying by \( v_2 \) and \( v_1 \) and subtracting eliminates \( s \). Any solution therefore satisfies
\[
sD = d_1 v'_2 - d_2 v'_1 , \qquad tD = d_1 v_2 - d_2 v_1 .
\]
Since \( D \ne 0 \), there is at most one pair \( (s, t) \), namely \( s = (d_1 v'_2 - d_2 v'_1)/D \) and \( t = (d_1 v_2 - d_2 v_1)/D \). Substituting, \( s v_1 - t v'_1 = d_1 (v_1 v'_2 - v_2 v'_1)/D = d_1 \), and likewise \( s v_2 - t v'_2 = d_2 \); so this pair is a solution. Each line has one parameter per point, so exactly one point is common to both.
:::

::: {#exr-lines-and-segments-b3}
[B3]

Show that the lines \( \nR(1, 0, 0) \) and \( (0, 1, 0) + \nR(0, 0, 1) \) of \( \nR^3 \) are skew.
:::

::: {.solution}
By @exm-method-parametrize: the points of the lines are \( (s, 0, 0) \) and \( (0, 1, t) \). Their second coordinates are \( 0 \) and \( 1 \), so no point is on both. The directions are not multiples: \( (1, 0, 0) = \lambda(0, 0, 1) \) fails in the first coordinate, whatever \( \lambda \) is. So the lines are skew.
:::

:::: {#exr-lines-and-segments-b4}
[B4: Prove or disprove]

Prove or disprove each statement, for points \( p, q, x \in \nR^n \) and directions \( v, w \ne 0 \).

::: {.enumerate options="label=(\alph*)"}
1. If \( \norm{p - x} = \norm{x - q} = \frac12 \norm{p - q} \), then \( x = \frac12 (p + q) \).
2. If \( \norm{p - x} = \norm{x - q} \), then \( x \in [p, q] \).
3. Any three points of \( \nR^2 \) are collinear.
4. If \( p + \nR v = p + \nR w \), then \( v = w \).
5. Two lines with two distinct common points are equal.
:::
::::

::: {.solution}
(a) **True.** This is the check that follows @cor-point-pinned-on-segment.

(b) **False.** Equal distances do not make a midpoint: take \( p = (-1, 0) \), \( q = (1, 0) \), \( x = (0, 1) \), as in the warning at the end of the section.

(c) **False.** By @prp-line-through-two-points, the only line through \( (0, 0) \) and \( (1, 0) \) is \( \nR(1, 0) \), whose points have second coordinate \( 0 \); so \( (0, 1) \) is not on it.

(d) **False.** \( p + \nR v = p + \nR(2v) \) by @prp-line-parametrizations with \( \lambda = 2 \), but \( 2v \ne v \), since \( 2v - v = v \ne 0 \).

(e) **True.** If both lines contain \( a \ne b \), both equal the line \( a + \nR(b - a) \) by @prp-line-through-two-points.
:::

### C. Going deeper

::: {#exr-lines-and-segments-c1}
[C1: Chapter check: one point in the middle]

Prove that of three distinct collinear points of \( \nR^n \), exactly one lies on the segment between the other two.
:::

::: {.solution}
Let the three points lie on the line \( p + \nR v \), \( v \ne 0 \). Each has one parameter, and distinct points have distinct parameters, since equal parameters give equal points. Since \( \le \) is a total order (@fd3:prp-ordered-ring-rules (i)), three distinct reals can be listed in increasing order. So we can name the points \( x_i = p + t_i v \) with \( t_1 < t_2 < t_3 \).

*Existence.* By @exr-lines-and-segments-b1 with \( a = t_1 \), \( b = t_3 \) and \( t = t_2 \), \( x_2 \in [x_1, x_3] \).

*Uniqueness.* Suppose \( x_1 \in [x_2, x_3] \). By @exr-lines-and-segments-b1 with \( a = t_2 < b = t_3 \), this gives \( t_2 \le t_1 \), against \( t_1 < t_2 \). Suppose \( x_3 \in [x_1, x_2] \). The same exercise with \( a = t_1 < b = t_2 \) gives \( t_3 \le t_2 \), against \( t_2 < t_3 \). So \( x_2 \) is the only one of the three between the other two.

**What a complete answer needs.** (10 points)
- 2: puts the three points on one parametrization, with distinct parameters, and says why they are distinct.
- 2: orders the parameters.
- 2: shows that the point with the middle parameter is between the others (by B1 or directly).
- 2: uses that a point has only one parameter on the line, at the step where B1's \( (\Rightarrow) \) or its replacement needs it.
- 2: excludes each of the two outer points.

A route through @thm-betweenness (comparing \( \norm{x_1 - x_3} = (t_3 - t_1)\norm{v} \) with the sums of the other distances) earns the same points step for step.

Slips that lose the step (0 points for it): using one parameter for a point on two different parametrizations; excluding only one of the outer points.
:::

<!-- dependency ledger
def-line-rn (example): (1,0,0) + t(-1,1,0) = (1 - t, t, 0) | def-vector-operations-rn (cited); verify/ch10/def-line-rn.py
def-line-rn (claim): Quick check (d): p + tv = p + uv gives (t - u)v = 0 | prp-vector-space-laws-rn (additive cancellation and (h)); inline
def-line-rn (claim): Quick check (a)-(c): 0 + R*1 = R; (1,1,1) + 2(1,2,3) = (3,5,7) | verify/ch10/def-line-rn.py
def-line-rn (claim): each point of a line has exactly one parameter, used without comment after the Quick check | proved in the Quick check's solution (d) on the page; inline
prp-line-parametrizations (proof): p + sv + (t - s)v = p + tv; division by lambda != 0; u - s = 0 gives v' = 0 | prp-vector-space-laws-rn (e), (h), (i) (cited, Uses line); field axioms of R (fd3:def-commutative-ring-and-field)
prp-line-through-two-points (proof): q - p != 0 when p != q; u != s because q != p | vector algebra in R^n (prp-vector-space-laws-rn, cited, Uses line); inline
def-collinear (claim): (1,0,0), (0,1,0), (0,0,1) not collinear; they satisfy x1 + x2 + x3 = 1 | prp-line-through-two-points (cited); verify/ch10/def-line-rn.py
def-collinear (claim): skew: v' = lambda v with v' != 0 forces lambda != 0, and v = lambda^{-1} v' | prp-vector-space-laws-rn (i), (e), (f); inline
exm-two-lines-in-space (solution): the two systems and their solutions; meeting point (2,1,1); directions not multiples | verify/ch10/exm-two-lines-in-space.py
def-segment-rn (claim): [p,q] = [q,p] via t <-> 1 - t; [p,p] = {p}; (1 - t)p + tq = p + t(q - p) | prp-vector-space-laws-rn; inline
def-segment-rn (claim): segments and intervals for n = 1: p + t(q - p) between p and q for t in [0,1]; t = (y - p)/(q - p) | fd3:prp-ordered-field-halves (d), fd3:prp-ordered-ring-rules (b), (c); inline (remark only, nothing depends on it)
lem-subsegment (proof): (1 - t)x + ty = p + ((1 - t)s + tu)(q - p) | prp-vector-space-laws-rn (cited, Uses line); verify/ch10/lem-subsegment.py (identity, exact)
lem-subsegment (proof): 0 <= (1 - t)s <= 1 - t, 0 <= tu <= t, adding | fd3:prp-ordered-field-halves (d), fd3:prp-ordered-ring-rules (b) (cited, Uses line)
lem-subsegment (claim): Quick check: (1,1,-1) not a multiple of (2,1,-2) | verify/ch10/lem-subsegment.py
thm-betweenness (proof): t >= 0 and 1 - t >= 0 for t in [0,1]; |t| = t for t >= 0; x - p = t(q - p) | fd3:def-absolute-value-ordered-field; fd3:prp-ordered-ring-rules (a); prp-vector-space-laws-rn and prp-norm-basic-rn (b) (cited, Uses line)
thm-betweenness (proof): 1 + c >= 1 > 0 for c >= 0; 1/(1 + c) > 0 | fd3:prp-ordered-ring-rules (b), (e); positive reciprocal (fd3:prp-reciprocal-order); fd3:prp-ordered-field-halves (c) (cited, Uses line) for t <= 1
thm-betweenness (claim): aftermath pointers to Real Numbers, Metric Spaces, and Derivatives (AN1) and Affine and Projective Geometry (GEO) | prose pointers by title (blueprint thread 1); nothing depends on them
cor-point-pinned-on-segment (proof): 0 <= s <= s + r; dividing by ||p - q|| > 0 keeps <= | fd3:prp-ordered-ring-rules (b), (c) with a positive reciprocal (fd3:prp-reciprocal-order); inline
cor-point-pinned-on-segment (proof): s = t' ||p - q|| with ||p - q|| > 0 gives t' = s/||p - q|| | field: cancel a non-zero factor (fd3:lem-field-fraction-rules); inline
cor-point-pinned-on-segment (proof): fold, s + r = 0 with s, r >= 0 forces s = r = 0 | fd3:prp-ordered-ring-rules (b) (cited), total order (i); inline
thm-betweenness (claim): warning, ||(-1,-1)|| = ||(-1,1)|| = sqrt 2; 2 sqrt 2 != 2 | verify/ch10/thm-betweenness.py
exr-lines-and-segments-a1 (solution): direction (2,1,-2), t = 2, midpoint (2, -1/2, 1) | verify/ch10/exr-lines-and-segments-a1.py
exr-lines-and-segments-a2 (solution): parameters 0, 1, 3; t = 1/3; distances 2, 1, 1; w = -u/2 | verify/ch10/exr-lines-and-segments-a2.py
exr-lines-and-segments-b1 (solution): 0 <= t - a <= b - a, division by b - a > 0; affine identity | fd3:prp-ordered-ring-rules (b), (c); verify/ch10/exr-lines-and-segments-b1.py
exr-lines-and-segments-b2 (solution): elimination formulas and back-substitution | verify/ch10/exr-lines-and-segments-b2.py (symbolic)
exr-lines-and-segments-b3 (solution): coordinates compared | verify/ch10/exr-lines-and-segments-b3.py
exr-lines-and-segments-c1 (solution): three distinct reals can be listed in increasing order | fd3:prp-ordered-ring-rules (i) (cited); inline
-->
