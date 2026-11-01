# Adding Points and Scaling Them

Section 9.1 made \( \nR^n \) a set of lists of reals. A set alone has no geometry: nothing in it says how to move from one point to another, or what it means to go twice as far in the same direction. Two operations supply this. A **displacement** is added to a point, coordinate by coordinate, and a displacement is **scaled** by stretching every coordinate by the same factor. Both are already familiar in the plane: the sum of @def-complex-numbers adds two points of \( \nC = \nR^2 \) coordinate by coordinate.

This section defines the two operations on \( \nR^n \) and proves their laws. Every equation among the laws turns out to be a law of \( \nR \), used once in each coordinate. That observation is the section's method, **work coordinatewise**. The method has one trap: a statement such as "\( x \ne 0 \)" is not a statement about every coordinate.

## The two operations

Here is the recurring computation that the definitions name. Moving the point \( (1, 4) \) three units along the first axis and one unit down the second gives \( (1 + 3, \; 4 - 1) = (4, 3) \). Doing the same move twice gives \( (1 + 6, \; 4 - 2) = (7, 2) \): the displacement \( (3, -1) \) has been doubled to \( (6, -2) \). In each case one rule is applied, in the same way, to every coordinate.

*Add and scale one coordinate at a time.*

::: {#def-vector-operations-rn}
[Vector Operations in \( \nR^n \)]

Let \( n \ge 1 \). **For all** \( x = (x_1, \dots, x_n) \) and \( y = (y_1, \dots, y_n) \) in \( \nR^n \) and **every** \( c \in \nR \), define
\[
\begin{aligned}
x + y &\coloneqq (x_1 + y_1, \; \dots, \; x_n + y_n) , \\
c x &\coloneqq (c x_1, \; \dots, \; c x_n) .
\end{aligned}
\]
The **zero vector** is \( 0 \coloneqq (0, \dots, 0) \), the **negative** of \( x \) is \( -x \coloneqq (-1)x \), and the **difference** is \( x - y \coloneqq x + (-y) \). The number \( c \) is called a **scalar**, and \( cx \) a **scalar multiple** of \( x \).
:::

In words: the \( k \)-th coordinate of \( x + y \) is \( x_k + y_k \), and the \( k \)-th coordinate of \( cx \) is \( c x_k \). Both right-hand sides are \( n \)-tuples of reals, so the sum is a function \( \nR^n \times \nR^n \to \nR^n \) and scaling is a function \( \nR \times \nR^n \to \nR^n \). There is nothing else to check: by @def-real-n-space a point determines its coordinates, so each formula gives exactly one output. When a vector is given by an expression, we write \( (v)_k \) for its \( k \)-th coordinate; thus \( (x + y)_k = x_k + y_k \) and \( (cx)_k = c x_k \). For \( n = 1 \), with a real \( x \) read as the \( 1 \)-tuple \( (x) \), both operations are the sum and product of \( \nR \).

**Points and vectors.** An element of \( \nR^n \) is called a **point** when we locate something and a **vector** when we add or scale it; the two words name the same objects. The **displacement from \( a \) to \( b \)** is the vector \( b - a \). Adding it to \( a \) gives \( b \): in coordinate \( k \), \( a_k + \bigl(b_k + (-a_k)\bigr) = b_k \) in \( \nR \). A picture of an arrow from \( a \) to \( b \) is a way to think about \( b - a \); it is not a new kind of object, and it never serves as a reason.

**Two examples.** With \( x = (1, 0, -1) \) and \( y = (2, 5, 3) \) in \( \nR^3 \),
\[
x + y = (3, 5, 2) , \qquad 2x - y = (2, 0, -2) + (-2, -5, -3) = (0, -5, -5) .
\]
The extreme scalar is \( c = 0 \). Then \( 0x = (0 \cdot x_1, \dots, 0 \cdot x_n) = 0 \) for every \( x \), by @fd3:prp-ring-algebra (b) and commutativity of multiplication, (F6), so scaling by \( 0 \) collapses every vector to the origin.

**In the plane.** On \( \nR^2 = \nC \) the sum is the sum of complex numbers (@def-complex-numbers). The scalar multiple \( c(a, b) = (ca, cb) \) is the complex product \( (c, 0)(a, b) \). That is, it is the product of \( (a, b) \) with the real number \( c \), read as a complex number (@prp-reals-embed-complex). So nothing new happens for \( n = 2 \); what is new is that every \( n \) works the same way.

## The method: work coordinatewise

We want the usual rules of algebra for these operations: brackets may be expanded, sums rearranged, scalars collected. None of this is promised by the definition; each rule must be proved. The first one shows how every proof in this section goes.

::: {.idea}
[Scratch work]

Take the law \( c(x + y) = cx + cy \). In \( \nR^2 \), with \( c = 2 \), \( x = (1, -3) \) and \( y = (4, 5) \), both sides are \( (10, 4) \): on the left \( 2(5, 2) \), on the right \( (2, -6) + (8, 10) \). To prove the law for all \( x, y, c \), we plan it backwards from what we want.

| We know | We want |
|---|---|
| \( x, y \in \nR^n \), \( c \in \nR \) | \( c(x + y) = cx + cy \) |
| the same; two points are equal when they agree in every place (@def-real-n-space) | \( \bigl(c(x + y)\bigr)_k = (cx + cy)_k \) **for every** \( k \in \{1, \dots, n\} \) |
| fix \( k \); unwind both sides with @def-vector-operations-rn | \( c(x_k + y_k) = c x_k + c y_k \), an equation in \( \nR \) |
| what is left: an equation between real numbers | true by the distributive law \( r(s + t) = rs + rt \) of \( \nR \), (F9) |

The second row is the key step: one equation in \( \nR^n \) became \( n \) equations in \( \nR \), and each of them is a field law.
:::

The table found the proof backwards; written forwards, it is short. Let \( k \in \{1, \dots, n\} \). Then
\[
\bigl(c(x + y)\bigr)_k = c(x_k + y_k) = c x_k + c y_k = (cx + cy)_k .
\]
The outer equalities are @def-vector-operations-rn. The middle one is the distributive law (F9) of a field (@fd3:def-commutative-ring-and-field). Since \( k \) was arbitrary, the two vectors agree in every place, so they are equal by @def-real-n-space.

::: {#exm-method-coordinatewise}
[Method: work coordinatewise]

**How it goes.** To prove an equation between vectors of \( \nR^n \):

1. Fix an arbitrary \( k \in \{1, \dots, n\} \).
2. Compute the \( k \)-th coordinate of each side from the definitions.
3. Prove the resulting equation in \( \nR \), naming the field law used.
4. Since \( k \) was arbitrary, conclude that the vectors agree in every place, so they are equal.

**When to use it.** Equations built from \( + \), scalar multiples, coordinates and finite sums of vectors. Every law of @prp-vector-space-laws-rn below except (j) is one application.

**Common mistakes.** Treating a condition that is not "for every \( k \)" as if it were. The statement \( x \ne 0 \) means that **some** coordinate \( x_k \) is non-zero. It does not mean that every coordinate is non-zero. Similarly, "\( x \) and \( y \) are parallel", defined below, asks for one scalar shared by all coordinates, so it is not a separate condition in each coordinate. In these cases, first unwind the condition into a statement about one chosen coordinate; then the method helps.

**Examples.** Law (g) of the proposition below, planned in the table above, and law (j), where the condition \( x \ne 0 \) has to be unwound.
:::

## The laws of the two operations

::: {#prp-vector-space-laws-rn}
[Laws of the Vector Operations]

For all \( x, y, z \in \nR^n \) and all \( c, d \in \nR \):

::: {.enumerate options="label=(\alph*)"}
1. \( (x + y) + z = x + (y + z) \);
2. \( x + y = y + x \);
3. \( x + 0 = x \);
4. \( x + (-x) = 0 \);
5. \( c(dx) = (cd)x \);
6. \( 1x = x \);
7. \( c(x + y) = cx + cy \);
8. \( (c + d)x = cx + dx \);
9. \( 0x = 0 \), \( c0 = 0 \), and \( (-c)x = -(cx) = c(-x) \);
10. if \( cx = 0 \), then \( c = 0 \) or \( x = 0 \).
:::
:::

::: {.idea}
Parts (a)–(i) are equations, so @exm-method-coordinatewise applies directly: each becomes the matching law of \( \nR \) in coordinate \( k \). Part (j) has the conclusion "\( c = 0 \) or \( x = 0 \)", and "\( x \ne 0 \)" gives only one non-zero coordinate; that one coordinate is enough, because a field has no zero divisors.
:::

::: {.proof}
Let \( k \in \{1, \dots, n\} \). In (a)–(i) we compute the \( k \)-th coordinate of each side with @def-vector-operations-rn. The two coordinates agree by the law of \( \nR \) named in brackets. Since \( k \) is arbitrary, the two sides agree in every place, so they are equal.

- (a) \( (x_k + y_k) + z_k = x_k + (y_k + z_k) \) [addition is associative, (F2)]. (b) \( x_k + y_k = y_k + x_k \) [addition is commutative, (F1)]. (c) \( x_k + 0 = x_k \) [\( 0 \) is neutral for addition, (F3)].
- (d) \( (-x)_k = (-1)x_k = -x_k \) [\( (-1)a = -(1 \cdot a) = -a \), by @fd3:prp-ring-algebra (c) with (F6) and (F7)], so \( (x + (-x))_k = x_k + (-x_k) = 0 \) [negatives, (F4)].
- (e) \( c(d x_k) = (cd) x_k \) [multiplication is associative, (F5)]. (f) \( 1 \cdot x_k = x_k \) [multiplication is commutative, (F6), and \( 1 \) is neutral, (F7)].
- (g) \( c(x_k + y_k) = c x_k + c y_k \) [(F9)], as in the table above.
- (h) \( (c + d)x_k = c x_k + d x_k \) [(F6), (F9)].
- (i) \( 0 \cdot x_k = 0 \) and \( c \cdot 0 = 0 \) [\( a \cdot 0 = 0 \), with (F6)]. For the last equations, \( (-c)x_k \), \( (-1)(c x_k) \) and \( c\bigl((-1)x_k\bigr) \) are all equal to \( -(c x_k) \) [\( (-a)b = a(-b) = -(ab) \), @fd3:prp-ring-algebra (c), and \( (-1)a = -a \) as in (d)]. These are the \( k \)-th coordinates of \( (-c)x \), \( -(cx) \) and \( c(-x) \).

(j) Suppose \( cx = 0 \). If \( x = 0 \), the conclusion holds. Otherwise \( x \ne 0 \), so \( x \) and \( (0, \dots, 0) \) differ in **some** place: there is one index \( k \) with \( x_k \ne 0 \). The \( k \)-th coordinate of \( cx = 0 \) gives \( c x_k = 0 \). Since \( \nR \) has no zero divisors (@fd3:lem-field-fraction-rules (d)), \( c = 0 \) or \( x_k = 0 \), and the second is false. Hence \( c = 0 \). This proves the proposition.

::: {.uses}
@def-real-n-space (equal means equal in every place); @fd3:def-commutative-ring-and-field (the field laws); @fd3:prp-ring-algebra (b) and (c) (\( a \cdot 0 = 0 \) and \( (-a)b = a(-b) = -(ab) \)).
:::
:::

Only the proof of (j) does not use every coordinate. It uses exactly one, the index \( k \) that "\( x \ne 0 \)" provides, and the other coordinates of \( x \) may be zero. This is how a condition that is not "for every \( k \)" is handled: it is first unwound into a statement about one chosen coordinate.

::: {.remark}
The proof used only the field laws of \( \nR \), never its order or its completeness. So the same definitions and the same proof work verbatim for \( n \)-tuples over **any** field \( F \) (@def-field), for instance over \( \nC \) or over the field with two elements.
:::

From now on we compute with vectors as with numbers, expanding brackets and collecting terms. Each such step is one of the laws of @prp-vector-space-laws-rn. For example, \( x + y = x + z \) gives \( y = z \): add \( -x \) to both sides and use (a)–(d).

## Sums of several vectors

A vector is assembled from its coordinates. To say this as an equation we need sums of more than two vectors, such as
\[
(1, 2) + (0, 3) + (4, -1) = (5, 4) ,
\]
where each coordinate of the result is the sum of the matching coordinates: \( 1 + 0 + 4 = 5 \) and \( 2 + 3 - 1 = 4 \). Sums of vectors are defined exactly as finite sums of reals are in *Sets and Functions* (@fd2:def-sum-product). The definition is by recursion, now with \( \nR^n \) as the set of values (@fd2:thm-recursion). For vectors \( v_1, \dots, v_m \in \nR^n \),
\[
\sum_{j=1}^{0} v_j \coloneqq 0 , \qquad \sum_{j=1}^{m+1} v_j \coloneqq \sum_{j=1}^{m} v_j + v_{m+1} .
\]
The empty sum is the zero vector, and the sum of one vector is that vector, by (c) and (b) of @prp-vector-space-laws-rn.

::: {#lem-vector-sums-coordinatewise}
[Sums of Vectors, Coordinatewise]

Let \( m \in \nN \), let \( v_1, \dots, v_m, w_1, \dots, w_m \in \nR^n \), and let \( c_1, \dots, c_m, d_1, \dots, d_m \in \nR \).

::: {.enumerate options="label=(\alph*)"}
1. For every \( k \in \{1, \dots, n\} \), \( \Bigl( \sum_{j=1}^{m} v_j \Bigr)_k = \sum_{j=1}^{m} (v_j)_k \).
2. \( \sum_{j=1}^{m} (c_j v_j + d_j w_j) = \sum_{j=1}^{m} c_j v_j + \sum_{j=1}^{m} d_j w_j \).
:::
:::

In words: the \( k \)-th coordinate of a sum of vectors is the sum of their \( k \)-th coordinates, and sums of vectors may be split termwise. Part (a) is the coordinatewise method for sums of any length, and part (b) is its first use.

For \( m \ge 1 \), a sum indexed from \( 1 \) is a sum indexed from \( 0 \) after a shift: \( \sum_{j=1}^{m} a_j = \sum_{j=0}^{m-1} a_{j+1} \) with \( m - 1 \in \nN \), which is the general form of @fd2:def-sum-product with lower index \( 0 \). So every part of @lem-ring-finite-sums, stated for sums from \( 0 \), applies to non-empty sums from \( 1 \).

::: {.second-reading title="Proof of the lemma"}
::: {.idea}
Part (a) is an induction on the number of terms: the recursion adds one vector at the end, and adding one vector adds one real in each coordinate. Part (b) is then @exm-method-coordinatewise, with (a) supplying the coordinates.
:::

::: {.proof}
(a) Fix \( k \). We use @fd2:thm-induction on \( m \), from the base \( m = 0 \). For \( m = 0 \) both sides are \( 0 \): the empty vector sum is the zero vector, whose \( k \)-th coordinate is \( 0 \), and the empty sum of reals is \( 0 \). Suppose (a) holds for \( m \). Then
\[
\begin{aligned}
\Bigl( \sum_{j=1}^{m+1} v_j \Bigr)_k
&= \Bigl( \sum_{j=1}^{m} v_j \Bigr)_k + (v_{m+1})_k \\
&= \sum_{j=1}^{m} (v_j)_k + (v_{m+1})_k = \sum_{j=1}^{m+1} (v_j)_k ,
\end{aligned}
\]
The first equality is the recursion for vector sums, read in coordinate \( k \). The second is the induction hypothesis. The third is the recursion for sums of reals.

(b) For \( m = 0 \) both sides are the zero vector: the left side is the empty sum, and the right side is \( 0 + 0 = 0 \) by @prp-vector-space-laws-rn (c). Let \( m \ge 1 \), and fix \( k \). By (a), the \( k \)-th coordinate of the left side is \( \sum_j \bigl(c_j (v_j)_k + d_j (w_j)_k\bigr) \). By @lem-ring-finite-sums (a), which holds for non-empty sums indexed from \( 1 \) as well, this is \( \sum_j c_j (v_j)_k + \sum_j d_j (w_j)_k \). By (a) applied to each sum, that is the \( k \)-th coordinate of the right side. Since \( k \) is arbitrary, the two sides are equal.

::: {.uses}
@def-vector-operations-rn (coordinates of sums, multiples); @fd2:def-sum-product (recursion for real sums); @lem-ring-finite-sums (a) (split termwise); @prp-vector-space-laws-rn (c) (\( 0 + 0 = 0 \)); @def-real-n-space (equal in every place).
:::
:::
:::

## The standard vectors

In the plane, \( (3, -2) \) is "three steps along the first axis and two steps back along the second". The steps are one unit long along a single axis, and they deserve names.

::: {#def-standard-basis-rn}
[Standard Vectors]

For \( k \in \{1, \dots, n\} \), the **\( k \)-th standard vector** \( e_k \in \nR^n \) has \( k \)-th coordinate \( 1 \) and every other coordinate \( 0 \):
\[
(e_k)_j \coloneqq \begin{cases} 1 & \text{if } j = k , \\ 0 & \text{if } j \ne k . \end{cases}
\]
:::

For \( n = 3 \): \( e_1 = (1, 0, 0) \), \( e_2 = (0, 1, 0) \), \( e_3 = (0, 0, 1) \). For \( n = 1 \) there is one standard vector, \( e_1 = 1 \). We need one fact about them.

::: {#prp-standard-basis-expansion}
[Expansion in the Standard Vectors]

Every \( x \in \nR^n \) satisfies
\[
x = \sum_{k=1}^{n} x_k e_k ,
\]
and the coefficients are unique: if \( c_1, \dots, c_n \in \nR \) and \( \sum_{k=1}^{n} c_k e_k = x \), then \( c_k = x_k \) for every \( k \).
:::

::: {.idea}
Work coordinatewise, using @lem-vector-sums-coordinatewise for the sum: the \( j \)-th coordinate of \( \sum_k c_k e_k \) is a sum of \( n \) reals in which only the \( k = j \) term can be non-zero.
:::

::: {.proof}
Let \( c_1, \dots, c_n \in \nR \) and \( j \in \{1, \dots, n\} \). By @lem-vector-sums-coordinatewise (a),
\[
\Bigl( \sum_{k=1}^{n} c_k e_k \Bigr)_j = \sum_{k=1}^{n} c_k (e_k)_j .
\]
For \( k \ne j \) the term is \( c_k \cdot 0 = 0 \), and for \( k = j \) it is \( c_j \cdot 1 = c_j \), since \( 1 \) is neutral for multiplication (F7). A sum with one possibly non-zero term equals that term, by @lem-ring-finite-sums (d), shifted to sums indexed from \( 1 \) as after @lem-vector-sums-coordinatewise (here \( n \ge 1 \)). So the \( j \)-th coordinate is \( c_j \). Since \( j \) is arbitrary,
\[
\sum_{k=1}^{n} c_k e_k = (c_1, \dots, c_n) .
\]{#eq-standard-expansion}
Taking \( c_k \coloneqq x_k \) gives \( \sum_k x_k e_k = x \). If \( \sum_k c_k e_k = x \), then @eq-standard-expansion gives \( (c_1, \dots, c_n) = x \), so \( c_k = x_k \) for every \( k \). This proves the proposition.

::: {.uses}
@def-vector-operations-rn (coordinates of \( c_k e_k \)); @fd3:prp-ring-algebra (b) (\( a \cdot 0 = 0 \)); @def-real-n-space (equal points, equal coordinates).
:::
:::

So the coefficients of a vector in the standard vectors are its coordinates, and nothing else. For example, \( (3, -2) = 3e_1 - 2e_2 \) in \( \nR^2 \), and \( (0, 5, 0) = 5e_2 \) in \( \nR^3 \).

::: {.warning}
The vector \( e_1 = (1, 0) \) is **not** the zero vector, although its second coordinate is \( 0 \). "\( x = 0 \)" asks every coordinate to vanish; "\( x \ne 0 \)" asks only that **some** coordinate be non-zero. Reading "\( x \ne 0 \)" as "\( x_k \ne 0 \) for every \( k \)" would make \( e_1 \) a zero vector, and would break the proof of @prp-vector-space-laws-rn (j), which needs one non-zero coordinate and no more.
:::

::: {.remark}
This chapter defines no product of two vectors that is again a vector. The expression \( (1, 2)(3, 4) \) is undefined in \( \nR^n \), even though \( \nR^2 = \nC \) carries the product of Chapter 3; a computation with vectors must not borrow it. The product of Section 9.3 takes two vectors and returns a **number**.
:::

## Parallel vectors

When is one vector a stretched copy of another? For \( (3, -6) \) and \( (-1, 2) \) the answer is yes: \( (3, -6) = -3 \cdot (-1, 2) \). The definition must decide the cases with a zero vector too, and that forces its shape.

::: {#def-parallel-rn}
[Parallel Vectors]

Vectors \( x, y \in \nR^n \) are **parallel** if \( y = cx \) for some \( c \in \nR \) **or** \( x = cy \) for some \( c \in \nR \).
:::

**The zero vector.** The vector \( 0 \) is parallel to every \( x \), since \( 0 = 0x \) by @prp-vector-space-laws-rn (i). The "or" is needed for this. With \( x = 0 \) and \( y = e_1 \), no \( c \) gives \( e_1 = c \cdot 0 \), because \( c \cdot 0 = 0 \ne e_1 \); only the second clause, \( 0 = 0 \cdot e_1 \), makes them parallel. Without the "or", parallelism would not even be symmetric.

**The one-scalar test.** When \( x \ne 0 \) the two clauses merge into one, and we use this form from now on: *for \( x \ne 0 \), \( y \) is parallel to \( x \) if and only if \( y = tx \) for some \( t \in \nR \).*

\( (\Leftarrow) \) This is the first clause of @def-parallel-rn. \( (\Rightarrow) \) If \( y = cx \), take \( t \coloneqq c \). If \( x = cy \), then \( c \ne 0 \), since \( c = 0 \) would give \( x = 0 \cdot y = 0 \) by @prp-vector-space-laws-rn (i). So \( c^{-1} \) exists, and \( y = 1y = (c^{-1} c) y = c^{-1}(cy) = c^{-1} x \), by (f) and (e) of @prp-vector-space-laws-rn; take \( t \coloneqq c^{-1} \).

Parallelism is not coordinatewise: \( y = tx \) asks for **one** \( t \) that works in every coordinate at once. To test it, find \( t \) from one coordinate where \( x_k \ne 0 \), then check the others.

::: {.check}
Is \( (2, 4, -6) \) parallel to \( (-1, -2, 3) \)? Is \( (1, 2) \) parallel to \( (2, 3) \)?
:::

::: {.solution}
Yes: \( (2, 4, -6) = -2 \cdot (-1, -2, 3) \). No: \( (1, 2) \ne 0 \), so by the one-scalar test \( (2, 3) \) would have to be \( t(1, 2) \); the first coordinate forces \( t = 2 \), the second \( t = 3/2 \). (Testing the other way, \( (1, 2) = s(2, 3) \) would need \( s = 1/2 \) and \( s = 2/3 \).)
:::

::: {#exm-midpoints-and-parallelograms}
[Midpoints and Parallelograms]

(a) For \( a, b \in \nR^n \), let \( m \coloneqq \tfrac{1}{2}(a + b) \). Show that \( m - a = b - m \), and compute \( m \) for \( a = (1, 4) \), \( b = (5, -2) \).

(b) For four points \( a, b, c, d \), consider the two conditions \( b - a = c - d \) and \( \tfrac{1}{2}(a + c) = \tfrac{1}{2}(b + d) \). Check both for \( a = (0, 0) \), \( b = (3, 1) \), \( c = (4, 3) \), \( d = (1, 2) \).
:::

::: {.solution}
(a) Work coordinatewise. For each \( k \),
\[
m_k - a_k = \tfrac{1}{2}(a_k + b_k) - a_k = \tfrac{1}{2}(b_k - a_k) = b_k - \tfrac{1}{2}(a_k + b_k) = b_k - m_k ,
\]
by the field laws of \( \nR \) and \( \tfrac{1}{2} + \tfrac{1}{2} = 1 \). So the displacement from \( a \) to \( m \) equals the displacement from \( m \) to \( b \): \( m \) is the **midpoint** of \( a \) and \( b \). For \( a = (1, 4) \) and \( b = (5, -2) \), \( a + b = (6, 2) \) and \( m = (3, 1) \); indeed \( m - a = (2, -3) = b - m \).

(b) Here \( b - a = (3, 1) \) and \( c - d = (3, 1) \), so the first condition holds. Also \( a + c = (4, 3) = b + d \), so \( \tfrac{1}{2}(a + c) = (2, \tfrac{3}{2}) = \tfrac{1}{2}(b + d) \). In a picture, \( b - a = c - d \) says that the sides from \( a \) to \( b \) and from \( d \) to \( c \) are the same displacement, as in a parallelogram \( abcd \). The second condition says that the diagonals from \( a \) to \( c \) and from \( b \) to \( d \) share their midpoint. The picture suggests that the two conditions always hold together. A picture is not a reason; Exercise B2 (b) proves the equivalence from the laws.
:::

## Exercises

### A. Check your understanding

:::: {#exr-vector-operations-a1}
[A1]

In (b)–(e), \( x, y \in \nR^n \) with \( n \ge 2 \). Decide whether the condition is a condition "for every \( k \)" on the coordinates, and if it is not, say what it asks.

::: {.enumerate options="label=(\alph*)"}
1. Compute \( 2(1, 0, -1) - 3(0, 1, 1) + (1, 1, 1) \) and write it in the form \( \sum_k c_k e_k \).
2. \( x = y \).
3. \( x \ne y \).
4. \( x + y = 0 \).
5. \( x \) is parallel to \( e_1 \).
:::
::::

::: {.solution}
(a) \( (2, 0, -2) - (0, 3, 3) + (1, 1, 1) = (3, -2, -4) = 3e_1 - 2e_2 - 4e_3 \), by @prp-standard-basis-expansion.

(b) Yes: \( x_k = y_k \) for every \( k \) (@def-real-n-space).

(c) No: it means \( x_k \ne y_k \) for **some** \( k \).

(d) Yes: \( x_k + y_k = 0 \) for every \( k \).

(e) No, as written: since \( e_1 \ne 0 \), the one-scalar test says that \( x \) is parallel to \( e_1 \) if and only if \( x = te_1 \) for **one** \( t \) shared by all coordinates. Because \( e_1 \) has only one non-zero coordinate, this one condition is equivalent to "\( x_k = 0 \) for every \( k \ge 2 \)", which puts no condition on \( x_1 \): if \( x = te_1 \), then \( x_k = t \cdot 0 = 0 \) for \( k \ge 2 \); conversely, if those coordinates vanish, then \( x = x_1 e_1 \) by @eq-standard-expansion.
:::

### B. Practice

:::: {#exr-vector-operations-b1}
[B1: Prove or disprove]

Let \( n \ge 2 \), \( x, y, z \in \nR^n \) and \( c, d \in \nR \). Prove or disprove.

::: {.enumerate options="label=(\alph*)"}
1. If \( x + y = x + z \), then \( y = z \).
2. If \( cx = cy \), then \( x = y \).
3. If \( cx = dx \) and \( x \ne 0 \), then \( c = d \).
4. If \( x \) is parallel to \( y \) and \( y \) is parallel to \( z \), then \( x \) is parallel to \( z \).
5. If \( x \) and \( y \) are parallel and both non-zero, then \( y = cx \) for some \( c \ne 0 \).
:::
::::

::: {.solution}
(a) **True.** Coordinatewise: \( x_k + y_k = x_k + z_k \) for every \( k \), so \( y_k = z_k \) by adding \( -x_k \) to both sides in \( \nR \). Hence \( y = z \).

(b) **False.** Take \( c = 0 \), \( x = e_1 \), \( y = e_2 \): then \( cx = 0 = cy \) by @prp-vector-space-laws-rn (i), but \( e_1 \ne e_2 \), as their first coordinates are \( 1 \) and \( 0 \). (The statement is true when \( c \ne 0 \): multiply by \( c^{-1} \).)

(c) **True.** From \( cx = dx \), adding \( -(dx) = (-d)x \) gives \( (c - d)x = 0 \), by (d), (h) and (i) of @prp-vector-space-laws-rn. Since \( x \ne 0 \), (j) gives \( c - d = 0 \), so \( c = d \).

(d) **False.** Take \( x = e_1 \), \( y = 0 \), \( z = e_2 \). The zero vector is parallel to every vector, so the hypotheses hold. But \( e_2 = te_1 \) fails for every \( t \) (second coordinates \( 1 \ne t \cdot 0 \)), so \( e_2 \) is not parallel to \( e_1 \), by the one-scalar test, since \( e_1 \ne 0 \). The counterexample needs the zero vector: for non-zero \( y \), the one-scalar test gives \( x = sy \) and \( z = ty \), and then \( x \) and \( z \) are parallel (if \( t \ne 0 \), \( x = (st^{-1})z \); if \( t = 0 \), \( z = 0 = 0x \)). In \( \nR^1 \) the statement is true, since any two reals are parallel; that is why \( n \ge 2 \) is assumed.

(e) **True.** Since \( x \ne 0 \), the one-scalar test gives \( y = cx \) for some \( c \). If \( c = 0 \), then \( y = 0x = 0 \), against \( y \ne 0 \). So \( c \ne 0 \).
:::

:::: {#exr-vector-operations-b2}
[B2]

::: {.enumerate options="label=(\alph*)"}
1. Find every \( t \in \nR \) for which \( (1, t, 2) \) is parallel to \( (2, 6, 4) \).
2. Prove that the two conditions of @exm-midpoints-and-parallelograms (b) agree for all \( a, b, c, d \in \nR^n \): \( b - a = c - d \) if and only if \( \tfrac{1}{2}(a + c) = \tfrac{1}{2}(b + d) \). Name the laws of @prp-vector-space-laws-rn you use.
:::
::::

::: {.solution}
(a) The vector \( (1, t, 2) \) is non-zero, as its first coordinate is \( 1 \). By the one-scalar test, the two are parallel if and only if \( (2, 6, 4) = s(1, t, 2) \) for some \( s \). The first coordinate forces \( s = 2 \); then the third reads \( 4 = 2 \cdot 2 \), true, and the second reads \( 6 = 2t \), so \( t = 3 \). Conversely, \( (2, 6, 4) = 2(1, 3, 2) \). So \( t = 3 \) is the only value.

(b) \( (\Rightarrow) \) Suppose \( b - a = c - d \). Add \( a + d \) to both sides. By (a)–(d), the left side becomes \( b + d \) and the right side \( a + c \): for instance \( (b - a) + (a + d) = b + \bigl((-a) + a\bigr) + d = b + 0 + d = b + d \), regrouping by (a), reordering by (b), then (d) and (c). So \( a + c = b + d \), and multiplying by \( \tfrac{1}{2} \) gives \( \tfrac{1}{2}(a + c) = \tfrac{1}{2}(b + d) \).

\( (\Leftarrow) \) Suppose \( \tfrac{1}{2}(a + c) = \tfrac{1}{2}(b + d) \). Multiply by \( 2 \): by (e) and (f), \( 2\bigl(\tfrac{1}{2}(a + c)\bigr) = (2 \cdot \tfrac{1}{2})(a + c) = 1(a + c) = a + c \), and likewise on the right, so \( a + c = b + d \). Add \( -a - d \) to both sides; by (a)–(d) as above, \( c - d = b - a \).
:::

### C. Going deeper

:::: {#exr-vector-operations-c1}
[C1: Chapter check: two vectors that are not parallel]

Let \( x, y \in \nR^n \). Prove that \( x \) and \( y \) are **not** parallel if and only if, for all \( s, t \in \nR \),
\[
sx + ty = 0 \implies s = t = 0 .
\]
::::

::: {.solution}
[Hint 1]

For \( (\Rightarrow) \), suppose \( s \ne 0 \) and solve \( sx + ty = 0 \) for \( x \).
:::

::: {.solution}
[Hint 2]

For \( (\Leftarrow) \), prove the contrapositive: if \( x \) and \( y \) are parallel, choose \( s \) and \( t \), not both zero, with \( sx + ty = 0 \). There are two clauses in @def-parallel-rn.
:::

::: {.solution}
\( (\Rightarrow) \) Suppose \( x \) and \( y \) are not parallel, and let \( s, t \in \nR \) with \( sx + ty = 0 \). First, \( s = 0 \). Otherwise \( s^{-1} \) exists, and adding \( -(ty) = (-t)y \) to both sides gives \( sx = (-t)y \), so
\[
x = s^{-1}(sx) = s^{-1}\bigl((-t)y\bigr) = (-ts^{-1})y ,
\]
by (f), (e) and (i) of @prp-vector-space-laws-rn. Then \( x = cy \) with \( c = -ts^{-1} \), so \( x \) and \( y \) are parallel, a contradiction. So \( s = 0 \), and the equation becomes \( 0x + ty = 0 \), that is, \( ty = 0 \) by (i) and (c). Next, \( y \ne 0 \): the zero vector is parallel to every vector (\( 0 = 0x \)), and \( y \) is not parallel to \( x \). By @prp-vector-space-laws-rn (j), \( t = 0 \).

\( (\Leftarrow) \) We prove the contrapositive. Suppose \( x \) and \( y \) are parallel. If \( y = cx \), take \( s \coloneqq c \), \( t \coloneqq -1 \): then \( sx + ty = cx - cx = 0 \), yet \( t \ne 0 \). If \( x = cy \), take \( s \coloneqq -1 \), \( t \coloneqq c \): then \( sx + ty = -cy + cy = 0 \), yet \( s \ne 0 \). In both cases the implication fails.

**What a complete answer needs.** (10 points)

- 2: sets up \( (\Rightarrow) \): assumes not parallel and \( sx + ty = 0 \), with the goal \( s = t = 0 \).
- 3: case \( s \ne 0 \): solves for \( x \) as a scalar multiple of \( y \), dividing only after \( s \ne 0 \) is assumed, and reaches a contradiction with the definition.
- 2: case \( s = 0 \): obtains \( ty = 0 \), **justifies** \( y \ne 0 \), and concludes \( t = 0 \) by (j).
- 2: \( (\Leftarrow) \) by contrapositive (or contradiction), producing \( (s, t) \ne (0, 0) \) in **both** clauses of the definition.
- 1: concludes the equivalence.

A contrapositive route for \( (\Rightarrow) \) earns the same 5 points: 3 for the case \( s \ne 0 \), writing \( x \) as a multiple of \( y \); 2 for the case \( s = 0 \), \( t \ne 0 \), deducing \( y = 0 \) from \( ty = 0 \) by (j) and noting that \( 0 \) is parallel to \( x \).

**Slips that lose the step** (0 for the step):

- Dividing by \( s \) without checking that \( s \ne 0 \).
- Treating only the clause \( y = cx \) of @def-parallel-rn and forgetting the clause \( x = cy \).
- Concluding \( t = 0 \) from \( ty = 0 \) without showing that \( y \ne 0 \).
:::

<!-- dependency ledger
def-vector-operations-rn (claim): n-tuples, equality in every place; n = 1 read as 1-tuples | def-real-n-space (cited), F2.1 §04 "Longer lists"
def-vector-operations-rn (example): (1,0,-1) + (2,5,3) = (3,5,2); 2x - y = (0,-5,-5) | numeral arithmetic in R; verify/ch09/def-vector-operations-rn.py
prp-vector-space-laws-rn (example): instance in the scratch work, 2((1,-3)+(4,5)) = (10,4) = (2,-6) + (8,10) | numeral arithmetic; verify/ch09/def-vector-operations-rn.py
lem-vector-sums-coordinatewise (example): (1,2) + (0,3) + (4,-1) = (5,4) | numeral arithmetic; verify/ch09/def-vector-operations-rn.py
prp-vector-space-laws-rn (proof): field laws (F1)-(F9), fd3:prp-ring-algebra (b), (c) ((-a)b = a(-b) = -(ab)), def-real-n-space | Uses line of the proof (moved from prose)
lem-vector-sums-coordinatewise (proof): def-vector-operations-rn, fd2:def-sum-product (recursion), lem-ring-finite-sums (a) (m >= 1), prp-vector-space-laws-rn (c) (case m = 0), def-real-n-space | Uses line of the proof (moved from prose)
prp-standard-basis-expansion (proof): def-vector-operations-rn, fd3:prp-ring-algebra (b), def-real-n-space | Uses line of the proof (moved from prose)
def-vector-operations-rn (claim): a_k + (b_k + (-a_k)) = b_k | field laws of R (fd3:def-commutative-ring-and-field), (F1), (F2), (F4), (F3)
def-vector-operations-rn (claim): 0x = 0 | fd3:prp-ring-algebra (b) with (F6) (cited)
prp-vector-space-laws-rn (proof): (-1)a = -a and (-a)b = a(-b) = -(ab) in R | fd3:prp-ring-algebra (c) with (F6), (F7) (cited)
exm-method-coordinatewise (claim): x + y = x + z gives y = z (closing paragraph after the remark) | prp-vector-space-laws-rn (a)-(d) (cited)
lem-vector-sums-coordinatewise (claim): finitely many vectors v_1..v_m fed to the recursion theorem (which takes a sequence) | finite-lists convention, as in lem-ring-finite-sums's "finite-lists remark"
lem-vector-sums-coordinatewise (claim): for m >= 1, Σ_{j=1}^m a_j = Σ_{j=0}^{m-1} a_{j+1}, so lem-ring-finite-sums (from 0) applies to non-empty sums from 1 (main line, after the lemma); Chapter 1's (lem-ring-finite-sums, F4.6 §01) sum from 0 agrees with fd2's def-sum-product at lower index 0 | fd2:def-sum-product (general form, cited on the main line); ledgered re-indexing line of the blueprint
prp-standard-basis-expansion (proof): lem-ring-finite-sums (d) applied to the re-indexed sum (terms extended by 0 beyond n) | lem-ring-finite-sums (d) (cited), re-indexing line above
def-parallel-rn (claim): the one-scalar test (form for a non-zero x) | proved inline
exm-midpoints-and-parallelograms (solution): 1/2 + 1/2 = 1; m = (3,1); midpoints (2, 3/2) | field laws of R (fd3:def-commutative-ring-and-field); verify/ch09/exm-midpoints-and-parallelograms.py
def-parallel-rn (claim): (hook) (3,-6) = -3(-1,2); (quick check) factor -2; t = 2 vs 3/2; s = 1/2 vs 2/3 | numeral arithmetic; verify/ch09/def-parallel-rn.py
exr-vector-operations-a1 (solution): (3, -2, -4) | numeral arithmetic; verify/ch09/exr-vector-operations-a1.py
exr-vector-operations-b1 (solution): counterexample values; (a) adding -x_k in R | field laws of R; verify/ch09/exr-vector-operations-b1.py
exr-vector-operations-b2 (solution): t = 3, s = 2 | numeral arithmetic; verify/ch09/exr-vector-operations-b2.py
-->
