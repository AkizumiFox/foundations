# Convex Sets and Hulls

Much of analysis moves from one point to another along a segment. Here are three examples.

- The mean value theorem compares \( f(q) \) with \( f(p) \) by walking from \( p \) to \( q \).
- A set is connected, in the simplest case, because any two of its points can be joined inside it.
- Cauchy's theorem in complex analysis is first proved on regions where every segment between two points stays inside.

Each of these arguments needs the segment \( [p, q] \) of @def-segment-rn to lie in the set where the work is done. This section names the sets for which that holds for every pair of points, shows that balls, lines, segments, hyperplanes and half-spaces are among them, and describes the smallest such set containing a given one.

Before the definition, test the property on a few sets of the plane.

::: {.check}
Which of these subsets of \( \nR^2 \) contain the segment between any two of their points?

- the disc \( \{x : \norm{x} \le 1\} \);
- the ring \( \{x : 1 \le \norm{x} \le 2\} \);
- the line \( \nR(1, 1) \);
- the two-point set \( \{(0, 0), (1, 0)\} \);
- the empty set;
- the union of the two coordinate axes.
:::

::: {.solution}
The disc: yes; this section proves it for every ball. The ring: no; \( (3/2, 0) \) and \( (-3/2, 0) \) lie in it, and the midpoint \( (0, 0) \) of the segment between them has norm \( 0 < 1 \). The line: yes, since \( (1 - t)(s, s) + t(u, u) = (v, v) \) with \( v \coloneqq (1 - t)s + tu \). The two points: no; the midpoint \( (1/2, 0) \) is neither of them. The empty set: yes, since there are no two points to test. The axes: no; \( (1, 0) \) and \( (0, 1) \) lie on them, and the midpoint \( (1/2, 1/2) \) lies on neither axis.
:::

## Convex sets and balls

The property tested above deserves a name.

*A set is convex when it never makes you leave it to walk straight from one of its points to another.* In other words, the segment between any two of its points lies inside it.

::: {#def-convex-set-rn}
[Convex Set]

A subset \( C \subseteq \nR^n \) is **convex** if \( [p, q] \subseteq C \) **for all** \( p, q \in C \).
:::

In words: whenever \( p \) and \( q \) are in \( C \), so is \( (1 - t)p + tq \) **for every** \( t \in [0, 1] \) (@def-segment-rn). The quantifier over \( t \) covers the whole interval \( [0, 1] \), not just the midpoint \( t = 1/2 \). This matters: the rational points of the plane, at the end of this subsection, contain every midpoint and still do not form a convex set. The empty set is convex, since the condition has no instance to check. So is every one-point set \( \{p\} \), since \( [p, p] = \{p\} \). The ring and the axes tested above are not convex: in each, one pair of points already has a midpoint outside.

The sets of analysis on which estimates hold are balls. The words "open" and "closed" below are names for now. *Real Numbers, Metric Spaces, and Derivatives* explains them and defines balls for any distance.

For instance, in \( \nR^2 \) take the points at distance less than \( 1 \) from \( (1, 0) \). The point \( (1/2, 0) \) is one of them, at distance \( 1/2 \). The point \( (1, 1) \) is not, since its distance is exactly \( 1 \); it lies on the circle around the disc.

::: {#def-ball-rn}
[Open and Closed Balls]

Let \( c \in \nR^n \) and \( r > 0 \). The **open ball** and the **closed ball** of center \( c \) and radius \( r \) are
\[
B(c, r) \coloneqq \{ x \in \nR^n : \norm{x - c} < r \} , \qquad \overline{B}(c, r) \coloneqq \{ x \in \nR^n : \norm{x - c} \le r \} .
\]
:::

For \( n = 1 \), \( \norm{x - c} = \abs{x - c} \) (@prp-norm-basic-rn (d)). So \( B(c, r) \) is the interval \( (c - r, c + r) \), and \( \overline{B}(c, r) \) is \( [c - r, c + r] \) (@fd3:prp-absolute-value-ordered-field (d)). For \( n = 2 \) they are discs without and with their circle \( S(c, r) \) (@def-sphere-rn).

::: {#prp-balls-convex}
[Balls Are Convex]

For every \( c \in \nR^n \) and \( r > 0 \), the balls \( B(c, r) \) and \( \overline{B}(c, r) \) are convex.
:::

::: {.idea}
[Scratch work]

Unwind the goal. The definition of convexity says what to fix: two points of the ball and a parameter \( t \in [0, 1] \).

| We know | We want |
|---|---|
| \( \norm{p - c} < r \), \( \norm{q - c} < r \), \( t \in [0, 1] \) | \( \norm{(1 - t)p + tq - c} < r \) |
| the same; and \( c = (1 - t)c + tc \) | \( \norm{(1 - t)(p - c) + t(q - c)} < r \) |
| the triangle inequality and \( \norm{sx} = \abs{s}\norm{x} \) | each of the two pieces is at most its weight times \( r \); the gap closes, since \( (1 - t)r + tr = r \) |

The second row is the whole trick. The center is split with the same weights as the point. Then the vector inside the norm becomes a weighted sum of two vectors whose lengths we know.
:::

::: {.proof}
Let \( p, q \in B(c, r) \) and \( t \in [0, 1] \). By the laws of the vector operations, \( (1 - t)p + tq - c = (1 - t)(p - c) + t(q - c) \). Since \( 1 - t \ge 0 \) and \( t \ge 0 \), the triangle inequality (@thm-triangle-inequality-rn (a)) gives
\[
\norm{(1 - t)p + tq - c} \le (1 - t)\norm{p - c} + t\norm{q - c} .
\]
If \( t = 0 \) or \( t = 1 \), the point \( (1 - t)p + tq \) is \( p \) or \( q \), which lies in \( B(c, r) \). If \( 0 < t < 1 \), both weights are positive. Multiplying by a positive number keeps a strict inequality, so \( (1 - t)\norm{p - c} < (1 - t)r \) and \( t\norm{q - c} < tr \). Adding these bounds the right side by \( (1 - t)r + tr = r \). Hence \( (1 - t)p + tq \in B(c, r) \), and \( B(c, r) \) is convex.

For \( \overline{B}(c, r) \) the same display holds. Since all four factors are non-negative, \( (1 - t)\norm{p - c} \le (1 - t)r \) and \( t\norm{q - c} \le tr \). Adding gives \( \norm{(1 - t)p + tq - c} \le r \). This proves the proposition.

::: {.uses}
@prp-vector-space-laws-rn, @prp-norm-basic-rn (b): rearrangements, \( \norm{sx} = \abs{s}\norm{x} \); @fd3:prp-ordered-ring-rules (b), (c): adding, multiplying by positives; @fd3:prp-ordered-field-halves (d): multiplying non-negative inequalities.
:::
:::

A ball is convex; its boundary is not.

::: {.check}
Is the sphere \( S(0, 1) \subseteq \nR^2 \) convex?
:::

::: {.solution}
No. The points \( (1, 0) \) and \( (-1, 0) \) lie on it, and the midpoint \( (0, 0) \) of the segment between them has norm \( 0 \ne 1 \). Exercise B3 shows that no point strictly inside a segment between two different points of a sphere lies on the sphere.
:::

The proof of @prp-balls-convex is the pattern for almost every convexity proof in this book.

::: {#exm-method-two-point-test}
[Method: the two-point test]

**How it goes.** To prove that \( C \) is convex:

1. Take \( p, q \in C \) and \( t \in [0, 1] \).
2. Write down the condition that \( p \) and \( q \) satisfy.
3. Split the vector, or the expression, belonging to \( (1 - t)p + tq \) as \( (1 - t)(\dots) + t(\dots) \). Use the same weights on every term, including the center or the constant.
4. Conclude by the triangle inequality, or by linearity, using \( 1 - t \ge 0 \) and \( t \ge 0 \).

**When to use it.** Proving that a set is convex straight from the definition: balls, half-spaces, sets cut out by inequalities.

**Common mistakes.** Checking only the midpoint, \( t = 1/2 \), is not enough: the set \( \nQ^2 \) below passes that check and is not convex. Allowing \( t \) outside \( [0, 1] \) is also wrong, since then a weight is negative and the inequalities reverse.
:::

::: {.warning}
**Midpoints are not enough.** The set \( \nQ^2 \) of points of \( \nR^2 \) with rational coordinates contains the midpoint \( \bigl( (a + c)/2, (b + d)/2 \bigr) \) of any two of its points \( (a, b) \), \( (c, d) \). Yet it is not convex. The field \( \nR \) is a complete ordered field (@fd3:thm-reals-complete-ordered-field). So the real number \( \sqrt 2 \) exists (@fd3:prp-cof-square-roots). Since \( 1 < 2 < 4 \), comparing squares of non-negative numbers gives \( 1 < \sqrt 2 < 2 \) (@fd3:prp-ordered-ring-rules (g)). So \( t \coloneqq \sqrt 2 / 2 \) lies in \( [0, 1] \). Then \( (\sqrt 2 / 2, 0) = (1 - t)(0, 0) + t(1, 0) \) is a point of \( [(0, 0), (1, 0)] \). It is not in \( \nQ^2 \): if \( t \in \nQ \), then \( \sqrt 2 = 2t \in \nQ \), against @fd3:thm-no-rational-square-two.
:::

## Examples and operations

The sets of Sections 10.1 and 10.2 are convex, and each passes the two-point test in one line.

::: {#prp-convex-examples}
[Lines, Segments, Hyperplanes and Half-Spaces Are Convex]

Each of the following is a convex subset of \( \nR^n \):

- every line (@def-line-rn);
- every segment (@def-segment-rn);
- every hyperplane \( H_{a,c} \) and each of its four half-spaces (@def-hyperplane-rn).
:::

::: {.idea}
Use the two-point test of @exm-method-two-point-test, with linearity in place of the triangle inequality. The weights \( 1 - t \) and \( t \) pass through the parameter of a line and through the dot product with \( a \).
:::

::: {.proof}
Let \( t \in [0, 1] \).

*Lines.* For two points \( p + sv \) and \( p + uv \) of \( p + \nR v \), the laws of the vector operations give \( (1 - t)(p + sv) + t(p + uv) = p + \bigl( (1 - t)s + tu \bigr)v \), a point of \( p + \nR v \).

*Segments.* If \( x, y \in [p, q] \), then \( [x, y] \subseteq [p, q] \) by @lem-subsegment; that is the definition of convexity for \( [p, q] \).

*Hyperplanes and half-spaces.* For \( x, y \in \nR^n \), linearity of the dot product (@prp-dot-product-laws-rn (b)) gives
\[
c - \inner{a}{(1 - t)x + ty} = (1 - t)\bigl( c - \inner{a}{x} \bigr) + t\bigl( c - \inner{a}{y} \bigr) .
\]
If \( x, y \in H_{a,c} \), the right side is \( 0 \), so \( (1 - t)x + ty \in H_{a,c} \). If \( \inner{a}{x} \le c \) and \( \inner{a}{y} \le c \), both brackets are \( \ge 0 \), and so are both weights. A product of two non-negative numbers is \( \ge 0 \), and so is a sum of two such products; so the right side is \( \ge 0 \). If both brackets are \( > 0 \), the right side is \( > 0 \). Indeed, one weight is positive, so its term is a product of two positive numbers and is positive, and the other term is \( \ge 0 \). This settles \( \{ \inner{a}{x} \le c \} \) and \( \{ \inner{a}{x} < c \} \). The half-spaces with \( \ge \) and \( > \) are those with \( \le \) and \( < \) for the normal \( -a \) and the constant \( -c \), since multiplying by \( -1 \) reverses an inequality. Also \( -a \ne 0 \).

::: {.uses}
@prp-vector-space-laws-rn (vector rearrangements); @fd3:prp-ordered-field-halves (d): products of non-negatives; @fd3:prp-ordered-ring-rules (a), (b), (c): negation, sums, positive products.
:::
:::

New convex sets come from old ones by intersecting, translating and scaling, but not by joining.

::: {#prp-convex-operations}
[Operations on Convex Sets]

::: {.enumerate options="label=(\alph*)"}
1. If \( (C_i)_{i \in I} \) is a family of convex subsets of \( \nR^n \), then \( \bigcap_{i \in I} C_i \) is convex.
2. If \( C \subseteq \nR^n \) is convex, \( b \in \nR^n \) and \( \lambda \in \nR \), then \( b + C \coloneqq \{ b + x : x \in C \} \) and \( \lambda C \coloneqq \{ \lambda x : x \in C \} \) are convex.
3. A union of two convex sets need not be convex: for \( p \ne q \), the sets \( \{p\} \) and \( \{q\} \) are convex and \( \{p\} \cup \{q\} \) is not.
:::
:::

::: {.idea}
Each part checks one segment at a time. A segment that lies in every \( C_i \) lies in their intersection, and translating or scaling moves a segment onto a segment.
:::

::: {.proof}
(a) The intersection is taken in \( \nR^n \), as *Sets and Functions* defined the intersection of a family (@fd2:def-family-union-intersection (b)). For \( I = \emptyset \) it is \( \nR^n \), which is convex. Let \( p, q \in \bigcap_{i} C_i \). For each \( i \), \( p, q \in C_i \) and \( C_i \) is convex, so \( [p, q] \subseteq C_i \). Hence \( [p, q] \subseteq \bigcap_i C_i \).

(b) For \( x, y \in C \) and \( t \in [0, 1] \), the laws of @prp-vector-space-laws-rn give
\[
(1 - t)(b + x) + t(b + y) = b + \bigl( (1 - t)x + ty \bigr) , \qquad (1 - t)\lambda x + t\lambda y = \lambda\bigl( (1 - t)x + ty \bigr) ,
\]
and \( (1 - t)x + ty \in C \).

(c) \( [p, p] = \{p\} \), so a one-point set is convex. The midpoint \( m = (p + q)/2 \) of \( [p, q] \) is neither \( p \) nor \( q \): \( m = p \) would give \( q = p \), and likewise for \( q \).
:::

::: {.check}
Show that the triangle \( T \coloneqq \{ x \in \nR^2 : x_1 \ge 0, \ x_2 \ge 0, \ x_1 + x_2 \le 1 \} \) is convex.
:::

::: {.solution}
\( T \) is the intersection of the three closed half-spaces \( \{ \inner{(-1, 0)}{x} \le 0 \} \), \( \{ \inner{(0, -1)}{x} \le 0 \} \) and \( \{ \inner{(1, 1)}{x} \le 1 \} \), each convex by @prp-convex-examples. By @prp-convex-operations (a), \( T \) is convex.
:::

## Convex combinations and the hull

A point of a segment is a sum of two points with non-negative weights adding up to \( 1 \). Allowing more than two points gives the general form. For example, the weights \( \tfrac12, \tfrac14, \tfrac14 \) are non-negative and add up to \( 1 \). On the points \( (0, 0) \), \( (4, 0) \), \( (0, 4) \) they give \( \tfrac12(0, 0) + \tfrac14(4, 0) + \tfrac14(0, 4) = (1, 1) \).

::: {#def-convex-combination-rn}
[Convex Combination]

Let \( k \ge 1 \) and \( p_1, \dots, p_k \in \nR^n \). A **convex combination** of \( p_1, \dots, p_k \) is a point
\[
\lambda_1 p_1 + \dots + \lambda_k p_k = \sum_{i=1}^{k} \lambda_i p_i \quad \text{with every } \lambda_i \ge 0 \text{ and } \sum_{i=1}^{k} \lambda_i = 1 .
\]
The numbers \( \lambda_i \) are its **weights**.
:::

For \( k = 1 \) the only convex combination of \( p_1 \) is \( p_1 \) itself. For \( k = 2 \), the weights are \( 1 - t \) and \( t \) with \( t \in [0, 1] \), and the convex combinations of \( p_1, p_2 \) form \( [p_1, p_2] \). The points need not be distinct.

A convex set is defined by a condition on two points. It controls combinations of any number of points.

::: {#thm-convex-contains-combinations}
[Convex Sets Contain Their Convex Combinations]

Let \( C \subseteq \nR^n \) be convex. Then every convex combination of finitely many points of \( C \) lies in \( C \).
:::

::: {.idea}
**Peel off the last point.** Convexity speaks about two points at a time, so split one point off. Of \( k + 1 \) weighted points, keep the last one. Rescale the first \( k \) weights so that they add up to \( 1 \) again. By induction, the first \( k \) points then give one point \( y \) of \( C \), and the whole combination is a point of the segment \( [y, p_{k+1}] \). The rescaling divides by \( 1 - \lambda_{k+1} \), so the case \( \lambda_{k+1} = 1 \) is set aside.
:::

::: {.proof}
For \( k \ge 1 \), let \( P(k) \) be the statement: for all \( p_1, \dots, p_k \in C \), every convex combination of \( p_1, \dots, p_k \) lies in \( C \). We prove \( P(k) \) for every \( k \ge 1 \) by induction from the base \( 1 \) (@fd2:thm-induction).

*Base case.* A convex combination of one point \( p_1 \in C \) has \( \lambda_1 = 1 \), so it is \( p_1 \in C \).

*Inductive step.* Let \( k \ge 1 \) and assume \( P(k) \). Let \( p_1, \dots, p_{k+1} \in C \) and let \( x = \sum_{i=1}^{k+1} \lambda_i p_i \) be a convex combination of them. The case \( \lambda_{k+1} = 1 \), in which all the other weights are \( 0 \), is handled just after this proof. Suppose \( \lambda_{k+1} \ne 1 \). The weights \( \lambda_1, \dots, \lambda_k \) are non-negative, so \( \sum_{i=1}^{k} \lambda_i \ge 0 \) (@prp-sum-order (a)), and \( \sum_{i=1}^{k} \lambda_i = 1 - \lambda_{k+1} \) by the recursion for sums. Hence \( s \coloneqq 1 - \lambda_{k+1} \) satisfies \( s \ge 0 \) and \( s \ne 0 \), so \( s > 0 \), and \( \lambda_{k+1} = 1 - s \in [0, 1] \). The numbers \( \lambda_i / s \), for \( i \le k \), are non-negative and add up to \( s/s = 1 \), since the constant \( 1/s \) comes out of the sum. So
\[
y \coloneqq \sum_{i=1}^{k} \frac{\lambda_i}{s} \, p_i
\]
is a convex combination of \( p_1, \dots, p_k \), and \( y \in C \) by \( P(k) \). By the recursion for sums, and by taking the constant \( s \) out of the sum in each coordinate,
\[
x = \sum_{i=1}^{k} \lambda_i p_i + \lambda_{k+1} p_{k+1} = s\,y + \lambda_{k+1} p_{k+1} = (1 - \lambda_{k+1})\,y + \lambda_{k+1}\,p_{k+1} ,
\]
a point of \( [y, p_{k+1}] \). Since \( y, p_{k+1} \in C \) and \( C \) is convex, \( x \in C \). This proves \( P(k + 1) \), and the theorem follows.

::: {.uses}
@lem-ring-finite-sums (b): constants come out; @lem-vector-sums-coordinatewise (a): vector sums by coordinates.
:::
:::

::: {.second-reading title="When the last weight is 1"}
If \( \lambda_{k+1} = 1 \), then \( \sum_{i=1}^{k} \lambda_i = 0 \) with every \( \lambda_i \ge 0 \), so every \( \lambda_i \) with \( i \le k \) is \( 0 \) (@prp-sum-order (e)). Then \( 0\,p_i = 0 \) (@prp-vector-space-laws-rn (i)), and \( x = 1\,p_{k+1} = p_{k+1} \in C \). This completes the inductive step.
:::

Among all convex sets containing a given set \( S \), there is a smallest one. It is built the way *Sets and Functions* built the smallest closed set (@fd2:prp-smallest-closed-set): intersect all candidates. For the two points \( (0, 0) \) and \( (1, 0) \), every convex set containing both contains the segment between them. That segment is itself convex, so it is the smallest convex set containing the two points.

::: {#def-convex-hull-rn}
[Convex Hull]

Let \( S \subseteq \nR^n \). The **convex hull** of \( S \) is
\[
\operatorname{conv} S \coloneqq \bigcap \{ C \subseteq \nR^n : C \text{ is convex and } S \subseteq C \} .
\]
:::

The family being intersected is **non-empty**, since \( \nR^n \) is convex and contains \( S \). So \( \operatorname{conv} S \) is a subset of \( \nR^n \), and it has three properties:

- it is convex, by @prp-convex-operations (a);
- it contains \( S \), since every member of the family does;
- it lies inside every convex set that contains \( S \), since it is the intersection of all of them.

In short, \( \operatorname{conv} S \) is the **smallest** convex set containing \( S \). For example, \( \operatorname{conv}\{p, q\} = [p, q] \). Indeed, the segment is convex (@prp-convex-examples) and contains \( p \) and \( q \), and every convex set containing \( p \) and \( q \) contains \( [p, q] \).

The definition says what the hull is, but not how to find its points. The next theorem does.

::: {#thm-convex-hull-combinations-rn}
[The Convex Hull Is the Set of Convex Combinations]

Let \( S \subseteq \nR^n \), and let \( K \) be the set of all convex combinations of finitely many points of \( S \). Then \( \operatorname{conv} S = K \).
:::

*Try it first (ten minutes): for three points \( p, q, r \) of the plane, describe \( \operatorname{conv}\{p, q, r\} \) without the word "intersection".*

::: {.idea}
The first guess is the three sides, \( [p, q] \cup [q, r] \cup [r, p] \). It contains \( p, q, r \), but it is not convex. For \( p = (0, 0) \), \( q = (2, 0) \), \( r = (0, 2) \), the points \( (1, 0) \in [p, q] \) and \( (0, 1) \in [r, p] \) have midpoint \( (1/2, 1/2) \), which lies on none of the three sides. So the hull must also contain every segment \( [x, r] \) with \( x \in [p, q] \). A point of such a segment is \( (1 - t)\bigl( (1 - s)p + sq \bigr) + tr \): a convex combination of \( p, q, r \). That suggests the theorem, and suggests its two halves:

① every convex combination of points of \( S \) lies in \( \operatorname{conv} S \), which is @thm-convex-contains-combinations applied to the convex set \( \operatorname{conv} S \);

② the set \( K \) is itself convex and contains \( S \), so the smallest such set lies inside it. For ②, two convex combinations are mixed by writing their two lists of points one after the other.
:::

::: {.proof}
\( (\supseteq) \) The set \( \operatorname{conv} S \) is convex and contains \( S \), as shown just after @def-convex-hull-rn. By @thm-convex-contains-combinations, it contains every convex combination of finitely many of its points, in particular of points of \( S \). So \( K \subseteq \operatorname{conv} S \).

\( (\subseteq) \) First, \( S \subseteq K \): each \( p \in S \) is the convex combination \( 1\,p \). Next, \( K \) is convex. Let \( x = \sum_{i=1}^{k} \lambda_i p_i \) and \( y = \sum_{j=1}^{m} \mu_j q_j \) be in \( K \), with \( p_i, q_j \in S \), and let \( t \in [0, 1] \). Join the two lists: let \( r_i \coloneqq p_i \) and \( \nu_i \coloneqq (1 - t)\lambda_i \) for \( 1 \le i \le k \), and \( r_{k+j} \coloneqq q_j \) and \( \nu_{k+j} \coloneqq t\mu_j \) for \( 1 \le j \le m \). Each \( \nu_i \) is a product of two non-negative numbers, so \( \nu_i \ge 0 \). Split the sum over the joined list into its two parts, and take the constants out of the two sums. This gives
\[
\sum_{i=1}^{k+m} \nu_i = (1 - t)\sum_{i=1}^{k} \lambda_i + t\sum_{j=1}^{m} \mu_j = (1 - t) + t = 1 .
\]
The same two rules, applied in each coordinate, give
\[
\sum_{i=1}^{k+m} \nu_i r_i = (1 - t)\sum_{i=1}^{k} \lambda_i p_i + t\sum_{j=1}^{m} \mu_j q_j = (1 - t)x + ty .
\]
So \( (1 - t)x + ty \) is a convex combination of the points \( r_1, \dots, r_{k+m} \) of \( S \), and lies in \( K \). Thus \( K \) is a convex set containing \( S \). Since \( \operatorname{conv} S \) lies inside every such set, \( \operatorname{conv} S \subseteq K \). This proves \( \operatorname{conv} S = K \).

::: {.uses}
@prp-sum-reindex (b): splitting a sum; @lem-ring-finite-sums (b): constants come out; @lem-vector-sums-coordinatewise (a): vector sums by coordinates.
:::
:::

The theorem turns membership in a hull, a statement about all convex sets at once, into a search for weights.

::: {#exm-triangle-as-hull}
[A Triangle as a Hull]

Let \( p_1, p_2, p_3 \in \nR^2 \). (a) Show that \( \operatorname{conv}\{p_1, p_2, p_3\} \) is the set \( T \) of points \( \lambda_1 p_1 + \lambda_2 p_2 + \lambda_3 p_3 \) with \( \lambda_i \ge 0 \) and \( \lambda_1 + \lambda_2 + \lambda_3 = 1 \): the filled triangle with corners \( p_1, p_2, p_3 \). (b) For \( p_1 = (0, 0) \), \( p_2 = (3, 0) \), \( p_3 = (0, 3) \), decide whether \( (1, 1) \) and \( (2, 2) \) lie in the hull.
:::

::: {.solution}
(a) \( T \subseteq \operatorname{conv}\{p_1, p_2, p_3\} \) by @thm-convex-hull-combinations-rn. For the other inclusion it is enough that \( T \) is convex, since it contains \( p_1 \) (weights \( 1, 0, 0 \)), \( p_2 \) and \( p_3 \). For two points of \( T \) with weights \( \lambda_i \) and \( \mu_i \), and \( t \in [0, 1] \),
\[
(1 - t)\sum_{i=1}^{3} \lambda_i p_i + t\sum_{i=1}^{3} \mu_i p_i = \sum_{i=1}^{3} \bigl( (1 - t)\lambda_i + t\mu_i \bigr) p_i ,
\]
and the new weights are non-negative and add up to \( (1 - t) + t = 1 \). This is the proof of @thm-convex-hull-combinations-rn with the two lists kept equal instead of joined.

(b) The weights \( \lambda_1 = \lambda_2 = \lambda_3 = 1/3 \) give \( \tfrac13(0, 0) + \tfrac13(3, 0) + \tfrac13(0, 3) = (1, 1) \), so \( (1, 1) \) is in the hull. For \( (2, 2) \): any weights with \( \lambda_1(0, 0) + \lambda_2(3, 0) + \lambda_3(0, 3) = (2, 2) \) have \( 3\lambda_2 = 2 \) and \( 3\lambda_3 = 2 \), so \( \lambda_2 + \lambda_3 = 4/3 \) and \( \lambda_1 = 1 - 4/3 < 0 \). No admissible weights exist, and \( (2, 2) \) is not in the hull. In this example the hull is \( \{ x_1 \ge 0, \ x_2 \ge 0, \ x_1 + x_2 \le 3 \} \). It is three times the triangle \( \{ x_1 \ge 0, \ x_2 \ge 0, \ x_1 + x_2 \le 1 \} \) shown convex earlier, and \( (2, 2) \) breaks the third inequality.
:::

## Star-shaped sets

Some arguments need segments only from one fixed point, not between every pair of points. For instance, the union of the two axes of \( \nR^2 \) is not convex. Yet every segment from \( (0, 0) \) to one of its points stays inside it.

::: {#def-star-shaped}
[Star-Shaped Set]

A set \( S \subseteq \nR^n \) is **star-shaped about** a point \( c \in S \) if \( [c, x] \subseteq S \) **for every** \( x \in S \). It is **star-shaped** if it is star-shaped about **some** point of \( S \).
:::

A non-empty convex set is star-shaped about **each** of its points: that is the definition of convexity with \( p = c \). The converse fails.

::: {#exm-star-not-convex}
[The Axes: Star-Shaped, Not Convex]

Let \( A \coloneqq \nR(1, 0) \cup \nR(0, 1) \subseteq \nR^2 \), the union of the two axes. Show that \( A \) is star-shaped about \( 0 \), is not convex, and is not star-shaped about \( (1, 0) \).
:::

::: {.solution}
For \( x = (s, 0) \in A \) and \( t \in [0, 1] \), \( (1 - t)\,0 + t(s, 0) = (ts, 0) \in A \); points of the other axis are handled the same way. So \( A \) is star-shaped about \( 0 \). The points \( (1, 0) \) and \( (0, 1) \) lie in \( A \), and the midpoint \( (1/2, 1/2) \) of the segment between them has both coordinates non-zero, so it lies on neither axis. This shows at once that \( A \) is not convex and that \( [(1, 0), (0, 1)] \not\subseteq A \), so \( A \) is not star-shaped about \( (1, 0) \).
:::

Convex and star-shaped sets return throughout the series. *Real Numbers, Metric Spaces, and Derivatives* uses segments inside convex sets for the mean value theorem in several variables. *Complex Analysis* proves Cauchy's theorem first on convex and star-shaped regions. *Analysis on Manifolds* proves the Poincaré lemma on star-shaped sets.

## Exercises

### A. Check your understanding

::: {#exr-convex-sets-and-hulls-a1}
[A1]

Decide which of these subsets of \( \nR^2 \) are convex. Justify each answer that is "no" with two points.

::: {.enumerate options="label=(\alph*)"}
1. \( \{ (x, y) : y \ge x^2 \} \).
2. \( \{ (x, y) : y \le x^2 \} \).
3. \( \nZ^2 \).
4. \( \{ x : 1 \le \norm{x} \le 2 \} \).
:::
:::

::: {.solution}
(a) Convex; Exercise B1 proves it with the two-point test.

(b) Not convex: \( (1, 1) \) and \( (-1, 1) \) lie in the set (\( 1 \le 1 \)), and their midpoint \( (0, 1) \) does not, since \( 1 > 0 = 0^2 \).

(c) Not convex: \( (0, 0), (1, 0) \in \nZ^2 \), and the midpoint \( (1/2, 0) \notin \nZ^2 \).

(d) Not convex: \( (3/2, 0) \) and \( (-3/2, 0) \) lie in the ring, and the midpoint \( (0, 0) \) has norm \( 0 < 1 \).
:::

::: {#exr-convex-sets-and-hulls-a2}
[A2]

::: {.enumerate options="label=(\alph*)"}
1. Is \( (1, 2) \) in \( \operatorname{conv}\{(0, 0), (3, 0), (0, 3)\} \)?
2. Consider the proof of @thm-convex-hull-combinations-rn. Which of its two inclusions uses @thm-convex-contains-combinations, and what does it apply that theorem to? Why is the family of convex sets containing \( S \), in @def-convex-hull-rn, non-empty?
:::
:::

::: {.solution}
(a) Yes: \( 0\,(0, 0) + \tfrac13(3, 0) + \tfrac23(0, 3) = (1, 2) \), with non-negative weights adding up to \( 1 \).

(b) The inclusion \( K \subseteq \operatorname{conv} S \). It applies the theorem to the convex set \( \operatorname{conv} S \), which contains \( S \), so it contains every convex combination of points of \( S \). The family contains \( \nR^n \), which is convex and contains \( S \).
:::

### B. Practice

::: {#exr-convex-sets-and-hulls-b1}
[B1]

Prove that \( P \coloneqq \{ (x, y) \in \nR^2 : y \ge x^2 \} \) is convex.
:::

::: {.solution}
We use the two-point test (@exm-method-two-point-test). Let \( (a, b), (c, d) \in P \), so \( b \ge a^2 \) and \( d \ge c^2 \), and let \( t \in [0, 1] \). The point \( (1 - t)(a, b) + t(c, d) \) has coordinates \( (1 - t)a + tc \) and \( (1 - t)b + td \). Since \( 1 - t \ge 0 \) and \( t \ge 0 \), multiplying keeps the two inequalities, and adding them gives
\[
(1 - t)b + td \ge (1 - t)a^2 + tc^2 .
\]
Expanding the square,
\[
(1 - t)a^2 + tc^2 - \bigl( (1 - t)a + tc \bigr)^2 = t(1 - t)(a - c)^2 ,
\]
since \( (1 - t) - (1 - t)^2 = t(1 - t) = t - t^2 \). The right side is \( \ge 0 \): \( t(1 - t) \ge 0 \) and \( (a - c)^2 \ge 0 \) (@fd3:prp-ordered-ring-rules (e)). Hence \( (1 - t)b + td \ge \bigl( (1 - t)a + tc \bigr)^2 \), and the point lies in \( P \).

::: {.uses}
@fd3:prp-ordered-field-halves (d): multiplying non-negative inequalities; @fd3:prp-ordered-ring-rules (b): adding inequalities.
:::
:::

::: {#exr-convex-sets-and-hulls-b2}
[B2]

For \( C, D \subseteq \nR^n \), let \( C + D \coloneqq \{ x + y : x \in C, \ y \in D \} \). Prove that if \( C \) and \( D \) are convex, so is \( C + D \).
:::

::: {.solution}
Let \( x + y \) and \( x' + y' \) be points of \( C + D \), with \( x, x' \in C \) and \( y, y' \in D \), and let \( t \in [0, 1] \). By the laws of @prp-vector-space-laws-rn,
\[
(1 - t)(x + y) + t(x' + y') = \bigl( (1 - t)x + tx' \bigr) + \bigl( (1 - t)y + ty' \bigr) .
\]
The first bracket lies in \( C \) and the second in \( D \), by convexity. So the point lies in \( C + D \).
:::

::: {#exr-convex-sets-and-hulls-b3}
[B3]

Let \( c \in \nR^n \), \( r > 0 \), and let \( p \ne q \) be points of the sphere \( S(c, r) \). Prove that \( \norm{(1 - t)p + tq - c} < r \) for every \( t \) with \( 0 < t < 1 \).
:::

::: {.solution}
We use the equality case, as in @exm-method-equality-case. Let \( u \coloneqq (1 - t)(p - c) \) and \( w \coloneqq t(q - c) \), so \( (1 - t)p + tq - c = u + w \) (@prp-vector-space-laws-rn). By @prp-norm-basic-rn (b), \( \norm{u} = (1 - t)r \) and \( \norm{w} = tr \). So the triangle inequality gives \( \norm{u + w} \le (1 - t)r + tr = r \).

Suppose \( \norm{u + w} = r = \norm{u} + \norm{w} \). Here \( u \ne 0 \), since \( \norm{u} = (1 - t)r > 0 \). By the equality case of @thm-triangle-inequality-rn (a), \( w = \lambda u \) for some \( \lambda \ge 0 \), that is, \( t(q - c) = \lambda(1 - t)(p - c) \). Dividing by \( t > 0 \), \( q - c = \mu(p - c) \) with \( \mu \coloneqq \lambda(1 - t)/t \ge 0 \). Taking norms, \( r = \mu r \), so \( \mu = 1 \) and \( q = p \), a contradiction. Hence \( \norm{u + w} < r \).

The result depends on the equality case of the triangle inequality, which belongs to the Euclidean norm. Measure distances in \( \nR^2 \) instead by \( \max(\abs{x_1 - y_1}, \abs{x_2 - y_2}) \): the "unit ball" about \( 0 \) is the square \( \{ \max(\abs{x_1}, \abs{x_2}) \le 1 \} \), and its edge contains the whole segment \( [(1, -1), (1, 1)] \), so the analogue of this exercise fails. So does the analogue of @thm-betweenness: the point \( (1, 1) \) is at distance \( 1 \) from \( (0, 0) \) and from \( (2, 0) \), and \( 1 + 1 = 2 \) is the distance between them, yet \( (1, 1) \) is not on the segment \( [(0, 0), (2, 0)] \). *Real Numbers, Metric Spaces, and Derivatives* returns to this distance.
:::

::: {#exr-convex-sets-and-hulls-b4}
[B4: Prove or disprove]

Prove each statement or give a counterexample. Throughout, \( C \), \( S \), \( T \) are subsets of \( \nR^n \).

::: {.enumerate options="label=(\alph*)"}
1. The union of two convex sets is convex.
2. The complement \( \nR^2 \setminus C \) of a convex set \( C \subseteq \nR^2 \) is convex.
3. \( \operatorname{conv}(S \cup T) = \operatorname{conv} S \cup \operatorname{conv} T \).
4. For \( p, q \in \nR^n \), the set \( \{ x : \norm{x - p} \le \norm{x - q} \} \) is convex.
5. If \( C \) is convex and \( \lambda, \mu \ge 0 \), then \( \lambda C + \mu C = (\lambda + \mu)C \) (notation of Exercise B2 and @prp-convex-operations (b)).
:::
:::

::: {.solution}
(a) **False.** @prp-convex-operations (c): \( \{p\} \cup \{q\} \) with \( p \ne q \).

(b) **False.** \( C = \overline{B}(0, 1) \) is convex (@prp-balls-convex). The points \( (2, 0) \) and \( (-2, 0) \) lie outside it, and their midpoint \( (0, 0) \) lies in it.

(c) **False.** Take \( S = \{p\} \), \( T = \{q\} \) with \( p \ne q \). Then \( \operatorname{conv} S = \{p\} \) and \( \operatorname{conv} T = \{q\} \), since one-point sets are convex; but \( \operatorname{conv}(S \cup T) = [p, q] \) (the example after @def-convex-hull-rn) contains the midpoint, which is neither \( p \) nor \( q \).

(d) **True.** If \( p = q \), the set is \( \nR^n \). If \( p \ne q \), let \( c \coloneqq (\norm{q}^2 - \norm{p}^2)/2 \). By @prp-perpendicular-bisector, \( \norm{x - p} < \norm{x - q} \) if and only if \( \inner{q - p}{x} < c \), and \( \norm{x - p} = \norm{x - q} \) if and only if \( \inner{q - p}{x} = c \). Since \( \le \) means "\( < \) or \( = \)" (@fd3:prp-ordered-ring-rules (i)), the set is the closed half-space \( \{ \inner{q - p}{x} \le c \} \). It is convex by @prp-convex-examples.

(e) **True.** \( (\supseteq) \) For \( x \in C \), \( (\lambda + \mu)x = \lambda x + \mu x \in \lambda C + \mu C \) (@prp-vector-space-laws-rn (h)). \( (\subseteq) \) Let \( \lambda x + \mu y \in \lambda C + \mu C \), with \( x, y \in C \). If \( \lambda + \mu > 0 \), let \( s \coloneqq \mu/(\lambda + \mu) \in [0, 1] \); then
\[
\lambda x + \mu y = (\lambda + \mu)\bigl( (1 - s)x + sy \bigr) ,
\]
and \( (1 - s)x + sy \in C \) by convexity. If \( \lambda = \mu = 0 \), both sides are \( \{0\} \) when \( C \ne \emptyset \) and \( \emptyset \) when \( C = \emptyset \). Convexity is needed: for \( C = \{0, e_1\} \subseteq \nR^n \) and \( \lambda = \mu = 1 \), the point \( e_1 = 0 + e_1 \) lies in \( C + C \) but not in \( 2C = \{0, 2e_1\} \).
:::

### C. Going deeper

::: {#exr-convex-sets-and-hulls-c1}
[C1: Chapter check: convex subsets of the line]

Let \( C \subseteq \nR \) be non-empty and convex. Let \( \alpha \coloneqq \inf C \) if \( C \) is bounded below, and \( \alpha \coloneqq -\infty \) otherwise; let \( \beta \coloneqq \sup C \) if \( C \) is bounded above, and \( \beta \coloneqq +\infty \) otherwise. Prove that every real \( x \) with \( \alpha < x < \beta \) lies in \( C \), and that every \( c \in C \) satisfies \( \alpha \le c \le \beta \). (So \( C \) is an interval with ends \( \alpha \) and \( \beta \), each end included or not.)
:::

::: {.solution}
[Hint 1]

For \( x \) strictly between \( \alpha \) and \( \beta \), look for two points of \( C \), one on each side of \( x \).
:::

::: {.solution}
[Hint 2]

If \( C \) is bounded below, then \( x > \inf C \), so \( x \) is not a lower bound of \( C \); hence there is \( a \in C \) with \( a < x \).
:::

::: {.solution}
*The supremum and the infimum.* If \( C \) is bounded above, \( \sup C \) exists, since \( C \) is non-empty and \( \nR \) is complete (@fd3:thm-reals-complete-ordered-field). If \( C \) is bounded below, by \( \ell \) say, then \( -C \coloneqq \{ -c : c \in C \} \) is non-empty and bounded above by \( -\ell \), so \( \sigma \coloneqq \sup(-C) \) exists. Then \( -\sigma \) is a lower bound of \( C \) (from \( -c \le \sigma \)), and for every lower bound \( \ell' \) of \( C \), \( -\ell' \) is an upper bound of \( -C \), so \( \sigma \le -\ell' \) and \( \ell' \le -\sigma \) (@fd3:prp-ordered-ring-rules (a)). So \( -\sigma \) is the greatest lower bound: \( \inf C = -\sup(-C) \) exists.

*Two points around \( x \).* Let \( \alpha < x < \beta \). If \( C \) is bounded below, \( x > \inf C \), so \( x \) is not a lower bound of \( C \); if \( C \) is not bounded below, no real number is a lower bound. Either way there is \( a \in C \) with \( a < x \) (@fd3:prp-ordered-ring-rules (i)). In the same way, \( x \) is not an upper bound of \( C \), and there is \( b \in C \) with \( x < b \).

*The segment is the interval.* For \( n = 1 \), \( (1 - t)a + tb = a + t(b - a) \). Let \( t \coloneqq (x - a)/(b - a) \), which is defined since \( b - a > 0 \). It lies in \( (0, 1) \): \( 0 < x - a < b - a \), and multiplying by \( 1/(b - a) > 0 \) keeps both inequalities (@fd3:prp-ordered-ring-rules (c)). With this \( t \), we get \( (1 - t)a + tb = x \). So \( x \in [a, b] \subseteq C \), by convexity.

*Conclusion.* Every \( x \) with \( \alpha < x < \beta \) lies in \( C \). For \( c \in C \), \( \alpha \le c \) because \( \inf C \) is a lower bound (or \( \alpha = -\infty \)), and \( c \le \beta \) likewise. So \( C \) is one of the intervals \( (\alpha, \beta) \), \( [\alpha, \beta) \), \( (\alpha, \beta] \), \( [\alpha, \beta] \), where an infinite end is never included.

**What a complete answer needs.** (10 points)
- 3: handles the ends: \( \sup C \) by completeness when bounded above, \( \inf C \) obtained (for instance as \( -\sup(-C) \)) when bounded below, and the unbounded cases.
- 3: finds \( a, b \in C \) with \( a < x < b \), from "\( x \) is not a lower (upper) bound".
- 2: shows \( x \in [a, b] \) by an explicit \( t \in [0, 1] \), or by the remark of Section 10.1 that a segment of \( \nR \) is an interval.
- 2: concludes both inclusions.
**Slips that lose the step** (0 for the step): using \( \inf C \) or \( \sup C \) without boundedness; assuming that \( C \) contains its supremum or infimum.

::: {.uses}
@fd3:def-complete-ordered-field (bounded sets have suprema).
:::
:::

### R. Review

::: {#exr-convex-sets-and-hulls-r1}
[R1]

Let \( Q \coloneqq \{ x \in \nR^n : \abs{x_k} \le 1 \text{ for every } k \} \). Show that \( Q \) is convex and that \( \overline{B}(0, 1) \subseteq Q \subseteq \overline{B}(0, \sqrt n) \).
:::

::: {.solution}
By @fd3:prp-absolute-value-ordered-field (d), \( \abs{x_k} \le 1 \) if and only if \( -1 \le x_k \le 1 \), that is, \( x_k \le 1 \) and \( -x_k \le 1 \). Since \( x_k = \inner{e_k}{x} \) and \( -x_k = \inner{-e_k}{x} \) (@prp-dot-product-laws-rn (a), (b), (d)), \( Q \) is the intersection of the \( 2n \) closed half-spaces \( \{ \inner{e_k}{x} \le 1 \} \) and \( \{ \inner{-e_k}{x} \le 1 \} \), whose normals \( \pm e_k \) are non-zero. Each is convex by @prp-convex-examples. So \( Q \), their intersection, is convex by @prp-convex-operations (a).

If \( \norm{x} \le 1 \), then \( \abs{x_k} \le \norm{x} \le 1 \) for every \( k \) (@prp-norm-coordinate-bounds (a)), so \( x \in Q \). If \( x \in Q \), then \( M \coloneqq \max_k \abs{x_k} \le 1 \), so \( \norm{x} \le \sqrt n \, M \le \sqrt n \) (@prp-norm-coordinate-bounds (b)), and \( x \in \overline{B}(0, \sqrt n) \). These two inclusions, a ball inside a box inside a larger ball, are the ones *Real Numbers, Metric Spaces, and Derivatives* uses to compare balls and boxes.
:::

::: {#exr-convex-sets-and-hulls-r2}
[R2]

Identify the polynomial \( a + bx + cx^2 \in \nR[x] \) with the point \( (a, b, c) \in \nR^3 \). Show that the set \( P \) of such polynomials \( f \) with \( f(t) \ge 0 \) for every \( t \in [0, 1] \) is a convex subset of \( \nR^3 \).
:::

::: {.solution}
Fix \( t \in [0, 1] \). Evaluation respects sums and products, sends a constant to itself and \( x \) to \( t \) (@thm-evaluation-respects-operations). So for \( f = a + bx + cx^2 \), by the definition of the dot product,
\[
f(t) = a + bt + ct^2 = \inner{(1, t, t^2)}{(a, b, c)} .
\]
So \( P_t \coloneqq \{ f : f(t) \ge 0 \} \) is the closed half-space \( \{ \inner{(1, t, t^2)}{y} \ge 0 \} \) of \( \nR^3 \). Its normal \( (1, t, t^2) \) is non-zero, since its first coordinate is \( 1 \). So \( P_t \) is convex by @prp-convex-examples. Then \( P = \bigcap_{t \in [0, 1]} P_t \) is convex by @prp-convex-operations (a).

The two-point test also works directly: \( (1 - s)f(t) + sg(t) \ge 0 \) for \( s \in [0, 1] \), and by the displayed formula this is the value at \( t \) of the polynomial whose coefficient triple is \( (1 - s)(a, b, c) + s(a', b', c') \).

::: {.uses}
@def-dot-product-rn (the dot product).
:::
:::

::: {#exr-convex-sets-and-hulls-r3}
[R3]

Let \( c \in \nC \), \( r > 0 \) and \( u \in \nT \). Show that \( D \coloneqq \{ z \in \nC : \abs{z - c} < r \} \) is convex as a subset of \( \nR^2 \), and that \( z \mapsto uz \) maps \( D \) onto \( \{ w \in \nC : \abs{w - uc} < r \} \).
:::

::: {.solution}
Reading \( \nC \) as \( \nR^2 \), \( \abs{z - c} = \norm{z - c} \) (@prp-plane-is-complex-plane (a), (c)). So \( D = B(c, r) \), which is convex by @prp-balls-convex.

For \( z \in D \), \( \abs{uz - uc} = \abs{u}\,\abs{z - c} = \abs{z - c} < r \) by @thm-conjugate-properties (d) and \( \abs{u} = 1 \); so \( uz \) lies in the second disc. Onto: let \( \abs{w - uc} < r \) and put \( z \coloneqq \conj{u} w \). Since \( \conj{u} = u^{-1} \) (@prp-unit-circle (a)), \( uz = w \). Also \( \conj{u}\,u\,c = c \), and \( \abs{\conj{u}} = \abs{u} = 1 \) by @thm-conjugate-properties (d). Hence
\[
\abs{z - c} = \abs{\conj{u}(w - uc)} = \abs{\conj{u}}\,\abs{w - uc} = \abs{w - uc} < r ,
\]
and \( z \in D \). Multiplying the plane by a unit complex number turns it about \( 0 \), and *Complex Analysis* opens with this picture.
:::

<!-- dependency ledger
def-ball-rn (claim): for n = 1 the balls are the intervals (c - r, c + r), [c - r, c + r] | prp-norm-basic-rn (d), fd3:prp-absolute-value-ordered-field (d), cited
prp-balls-convex (proof): |t| = t and |1 - t| = 1 - t for t in [0, 1] | fd3:def-absolute-value-ordered-field (unlabelled use)
prp-convex-examples (proof): a product of two non-negative reals is >= 0; of two positive reals is > 0 | fd3:prp-ordered-field-halves (d), fd3:prp-ordered-ring-rules (c), cited (Uses line)
prp-convex-examples (proof): the two half-spaces with >=, > are those with <=, < for -a, -c | fd3:prp-ordered-ring-rules (a) with prp-dot-product-laws-rn (b), cited (Uses line)
prp-convex-operations (proof): (p + q)/2 = p implies q = p | prp-vector-space-laws-rn, inline
thm-convex-contains-combinations (proof): sum_{i<=k+1} = sum_{i<=k} + last term; sums of reals indexed from 1 read as fd4 ch01 sums from 0 by shifting the index | fd2:def-sum-product (recursion and shifting line, NOTATION row)
thm-convex-contains-combinations (proof): s >= 0 and s != 0 give s > 0 | fd3:prp-ordered-ring-rules (i) (totality)
thm-convex-hull-combinations-rn (proof): sum_{i=k+1}^{k+m} a_i = sum_{j=1}^{m} a_{k+j} (index shift) | fd2:def-sum-product (shifting line, NOTATION row)
thm-convex-hull-combinations-rn (proof): the sums over the joined list as sums of vectors are taken coordinatewise | lem-vector-sums-coordinatewise (a), cited (Uses line)
exm-triangle-as-hull (solution): (1 - t) sum lambda_i p_i + t sum mu_i p_i = sum ((1 - t) lambda_i + t mu_i) p_i for three terms | prp-vector-space-laws-rn, inline; verify/ch10/exm-triangle-as-hull.py
exr-convex-sets-and-hulls-b1 (solution): (1 - t)a^2 + tc^2 - ((1 - t)a + tc)^2 = t(1 - t)(a - c)^2 | inline expansion; verify/ch10/exr-convex-sets-and-hulls-b1.py
exr-convex-sets-and-hulls-b3 (solution): from r = mu r with r > 0, mu = 1 | field cancellation, fd3 (cited in ch09 ledger as fd3:def-commutative-ring-and-field)
exr-convex-sets-and-hulls-b4 (solution): (e) mu/(lambda + mu) in [0, 1]; identity lambda x + mu y = (lambda + mu)((1 - s)x + s y) | inline; verify/ch10/exr-convex-sets-and-hulls-b4.py
exr-convex-sets-and-hulls-c1 (solution): 1/(b - a) > 0 for b - a > 0 | inline: otherwise 1 = (b - a) * 1/(b - a) <= 0 by fd3:prp-ordered-ring-rules (c), (e) (1 > 0)
exr-convex-sets-and-hulls-c1 (solution): x > inf C implies x is not a lower bound (inf is the greatest lower bound) | fd2:def-order-supremum (dual, unlabelled use)
exr-convex-sets-and-hulls-r2 (solution): the identification a + bx + cx^2 <-> (a, b, c); a constant times x^k evaluated at t is a t^k | thm-evaluation-respects-operations, cited
exr-convex-sets-and-hulls-r3 (solution): |u| = 1 for u in T | definition of T, ch03 s05 (unlabelled display)
-->
