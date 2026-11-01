# Adding Points and Scaling Them

Section 9.1 made \( \nR^n \) a set of lists of reals. A set alone has no geometry: nothing in it says how to move from one point to another, or what it means to go twice as far in the same direction. Two operations supply this. A **displacement** is added to a point, coordinate by coordinate, and a displacement is **scaled** by stretching every coordinate by the same factor. Both are already familiar in the plane: the sum of @def-complex-numbers adds two points of \( \nC = \nR^2 \) coordinate by coordinate.

This section defines the two operations on \( \nR^n \) and proves their laws. Every law turns out to be a law of \( \nR \), used once in each coordinate. That observation is the section's method, **work coordinatewise**. The method has a failure case, and the failure case is part of it: a statement such as "\( x \ne 0 \)" is not a statement about every coordinate.

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
The degenerate scalar is \( c = 0 \): \( 0x = (0 \cdot x_1, \dots, 0 \cdot x_n) = 0 \) for every \( x \), by @fd3:prp-ring-algebra (b), so scaling by \( 0 \) collapses every vector to the origin.

**In the plane.** On \( \nR^2 = \nC \) the sum is the sum of @def-complex-numbers, and the scalar multiple \( c(a, b) = (ca, cb) \) is the complex product \( (c, 0)(a, b) \), that is, the product of \( (a, b) \) with the real number \( c \) as identified in @prp-reals-embed-complex. So nothing new happens for \( n = 2 \); what is new is that every \( n \) works the same way.

## The method: work coordinatewise

We want the usual rules of algebra for these operations: brackets may be expanded, sums rearranged, scalars collected. None of this is promised by the definition; each rule must be proved. The first one shows how every proof in this section goes.

::: {.idea}
[Scratch work]

Take the law \( c(x + y) = cx + cy \), and plan it backwards from the goal.

| Givens | Goal |
|---|---|
| \( x, y \in \nR^n \), \( c \in \nR \) | \( c(x + y) = cx + cy \) |
| the same; two points are equal when they agree in every place (@def-real-n-space) | \( \bigl(c(x + y)\bigr)_k = (cx + cy)_k \) **for every** \( k \in \{1, \dots, n\} \) |
| fix \( k \); unwind both sides with @def-vector-operations-rn | \( c(x_k + y_k) = c x_k + c y_k \), an equation in \( \nR \) |
| the gap: an equation between real numbers | closed by distributivity (F9) in \( \nR \) |

The second row is where the method lives: one equation in \( \nR^n \) became \( n \) equations in \( \nR \), and each of them is a field law.
:::

The table found the proof backwards; written forwards, it is short. Let \( k \in \{1, \dots, n\} \). Then \( \bigl(c(x + y)\bigr)_k = c(x_k + y_k) = c x_k + c y_k = (cx + cy)_k \), by @def-vector-operations-rn twice and (F9) of @fd3:def-commutative-ring-and-field. Since \( k \) was arbitrary, the two vectors agree in every place, so they are equal by @def-real-n-space.

::: {#exm-method-coordinatewise}
[Method: work coordinatewise]

**Template.** To prove an equation between vectors of \( \nR^n \): (1) fix an arbitrary \( k \in \{1, \dots, n\} \); (2) compute the \( k \)-th coordinate of each side from the definitions; (3) prove the resulting equation in \( \nR \), naming the field law used; (4) conclude, since \( k \) was arbitrary, that the vectors agree in every place and so are equal.

**When to use it.** Equations built from \( + \), scalar multiples, coordinates and finite sums of vectors. Every law of @prp-vector-space-laws-rn below except (j) is one application.

**The usual failure.** A condition that is not "for every \( k \)". The statement \( x \ne 0 \) means that **some** coordinate \( x_k \) is non-zero, not that every coordinate is; and "\( x \) and \( y \) are parallel", defined below, asks for one scalar shared by all coordinates, so it is not a separate condition in each coordinate. In these cases the method still helps, but only after the condition has been unwound into a statement about one chosen coordinate.

**Worked examples.** Law (g), planned in the table above, and law (j), where the failure case appears; both are in the proof below.
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
Let \( k \in \{1, \dots, n\} \). In (a)–(i) we compute the \( k \)-th coordinate of each side with @def-vector-operations-rn; the two coordinates agree by the field law of \( \nR \) named in brackets (@fd3:def-commutative-ring-and-field, @fd3:prp-ring-algebra). Since \( k \) is arbitrary, the two sides are equal by @def-real-n-space.

- (a) \( (x_k + y_k) + z_k = x_k + (y_k + z_k) \) [(F2)]. (b) \( x_k + y_k = y_k + x_k \) [(F1)]. (c) \( x_k + 0 = x_k \) [(F3)].
- (d) \( (-x)_k = (-1)x_k = -x_k \) [@fd3:prp-ring-algebra (c) with (F7)], so \( (x + (-x))_k = x_k + (-x_k) = 0 \) [(F4)].
- (e) \( c(d x_k) = (cd) x_k \) [(F5)]. (f) \( 1 \cdot x_k = x_k \) [(F6), (F7)].
- (g) \( c(x_k + y_k) = c x_k + c y_k \) [(F9)], as in the table above.
- (h) \( (c + d)x_k = c x_k + d x_k \) [(F6), (F9)].
- (i) \( 0 \cdot x_k = 0 \) and \( c \cdot 0 = 0 \) [@fd3:prp-ring-algebra (b), with (F6)]. For the last equations, \( (-c)x_k \), \( (-1)(c x_k) \) and \( c\bigl((-1)x_k\bigr) \) are all equal to \( -(c x_k) \) [@fd3:prp-ring-algebra (c), with (F7)]; these are the \( k \)-th coordinates of \( (-c)x \), \( -(cx) \) and \( c(-x) \).

(j) Suppose \( cx = 0 \). If \( x = 0 \), the conclusion holds. Otherwise \( x \ne 0 \), so \( x \) and \( (0, \dots, 0) \) differ in **some** place (@def-real-n-space): there is one index \( k \) with \( x_k \ne 0 \). The \( k \)-th coordinate of \( cx = 0 \) gives \( c x_k = 0 \). Since \( \nR \) has no zero divisors (@fd3:lem-field-fraction-rules (d)), \( c = 0 \) or \( x_k = 0 \), and the second is false. Hence \( c = 0 \). This proves the proposition.
:::

The proof of (j) is the only one that does not use every coordinate. It uses exactly one, the index \( k \) that "\( x \ne 0 \)" provides, and the other coordinates of \( x \) may be zero. That is the failure case of the method box, handled correctly.

::: {.remark}
The proof used only the field laws of \( \nR \), never its order or its completeness. So the same definitions and the same proof work verbatim for \( n \)-tuples over **any** field \( F \) (@def-field), for instance over \( \nC \) or over the field with two elements. The linear-algebra volumes turn the situation around: they take (a)–(h) as the axioms of a vector space, and \( \nR^n \) becomes their first example.
:::

From now on we compute with vectors as with numbers, expanding brackets and collecting terms, and cite @prp-vector-space-laws-rn only where a step is not visible. For example, \( x + y = x + z \) gives \( y = z \): add \( -x \) to both sides and use (a)–(d).

## Sums of several vectors

A vector is assembled from its coordinates, and to say this as an equation we need sums of more than two vectors. They are defined exactly as finite sums of reals are, by recursion (@fd2:thm-recursion) with \( \nR^n \) as the set of values, on the template of @fd2:def-sum-product: for vectors \( v_1, \dots, v_m \in \nR^n \),
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
by the recursion for vector sums and @def-vector-operations-rn, then the hypothesis, then the recursion of @fd2:def-sum-product.

(b) Fix \( k \). By (a) and @def-vector-operations-rn, the \( k \)-th coordinate of the left side is \( \sum_j \bigl(c_j (v_j)_k + d_j (w_j)_k\bigr) \). By @lem-ring-finite-sums (a), read for sums indexed from \( 1 \), this is \( \sum_j c_j (v_j)_k + \sum_j d_j (w_j)_k \), which is the \( k \)-th coordinate of the right side, by (a) applied to each sum and @def-vector-operations-rn. Since \( k \) is arbitrary, the two sides are equal.
:::

A sum indexed from \( 1 \) is a sum indexed from \( 0 \) after a shift: \( \sum_{j=1}^{m} a_j = \sum_{j=0}^{m-1} a_{j+1} \), which is the general form of @fd2:def-sum-product with lower index \( 0 \). So every part of @lem-ring-finite-sums, stated for sums from \( 0 \), applies to sums from \( 1 \).
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

For \( n = 3 \): \( e_1 = (1, 0, 0) \), \( e_2 = (0, 1, 0) \), \( e_3 = (0, 0, 1) \). For \( n = 1 \) there is one standard vector, \( e_1 = 1 \). The linear-algebra volumes call the list \( e_1, \dots, e_n \) the standard basis of \( \nR^n \); here we need only the following fact.

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
Let \( c_1, \dots, c_n \in \nR \) and \( j \in \{1, \dots, n\} \). By @lem-vector-sums-coordinatewise (a) and @def-vector-operations-rn,
\[
\Bigl( \sum_{k=1}^{n} c_k e_k \Bigr)_j = \sum_{k=1}^{n} c_k (e_k)_j .
\]
For \( k \ne j \) the term is \( c_k \cdot 0 = 0 \) (@fd3:prp-ring-algebra (b)), and for \( k = j \) it is \( c_j \cdot 1 = c_j \) (F7). A sum with one possibly non-zero term equals that term (@lem-ring-finite-sums (d), read for sums indexed from \( 1 \)), so the \( j \)-th coordinate is \( c_j \). Since \( j \) is arbitrary,
\[
\sum_{k=1}^{n} c_k e_k = (c_1, \dots, c_n) .
\]{#eq-standard-expansion}
Taking \( c_k \coloneqq x_k \) gives \( \sum_k x_k e_k = x \). If \( \sum_k c_k e_k = x \), then @eq-standard-expansion gives \( (c_1, \dots, c_n) = x \), so \( c_k = x_k \) for every \( k \) by @def-real-n-space. This proves the proposition.
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

**Parallel to a non-zero vector.** When \( x \ne 0 \) the two clauses merge, and we use this form from now on: *for \( x \ne 0 \), \( y \) is parallel to \( x \) if and only if \( y = tx \) for some \( t \in \nR \).*

\( (\Leftarrow) \) This is the first clause of @def-parallel-rn. \( (\Rightarrow) \) If \( y = cx \), take \( t \coloneqq c \). If \( x = cy \), then \( c \ne 0 \), since \( c = 0 \) would give \( x = 0 \cdot y = 0 \) by @prp-vector-space-laws-rn (i). So \( c^{-1} \) exists, and \( y = 1y = (c^{-1} c) y = c^{-1}(cy) = c^{-1} x \), by (f) and (e) of @prp-vector-space-laws-rn; take \( t \coloneqq c^{-1} \).

Parallelism is not coordinatewise: \( y = tx \) asks for **one** \( t \) that works in every coordinate at once. To test it, find \( t \) from one coordinate where \( x_k \ne 0 \), then check the others.

::: {.check}
Is \( (2, 4, -6) \) parallel to \( (-1, -2, 3) \)? Is \( (1, 2) \) parallel to \( (2, 3) \)?
:::

::: {.solution}
Yes: \( (2, 4, -6) = -2 \cdot (-1, -2, 3) \). No: \( (1, 2) \ne 0 \), so by the form for a non-zero vector \( (2, 3) \) would have to be \( t(1, 2) \); the first coordinate forces \( t = 2 \), the second \( t = 3/2 \). (Testing the other way, \( (1, 2) = s(2, 3) \) would need \( s = 1/2 \) and \( s = 2/3 \).)
:::

::: {#exm-midpoints-and-parallelograms}
[Midpoints and Parallelograms]

(a) For \( a, b \in \nR^n \), let \( m \coloneqq \tfrac{1}{2}(a + b) \). Show that \( m - a = b - m \), and compute \( m \) for \( a = (1, 4) \), \( b = (5, -2) \).

(b) Four points \( a, b, c, d \) satisfy \( b - a = c - d \) exactly when \( \tfrac{1}{2}(a + c) = \tfrac{1}{2}(b + d) \). Check both conditions for \( a = (0, 0) \), \( b = (3, 1) \), \( c = (4, 3) \), \( d = (1, 2) \).
:::

::: {.solution}
(a) Work coordinatewise. For each \( k \),
\[
m_k - a_k = \tfrac{1}{2}(a_k + b_k) - a_k = \tfrac{1}{2}(b_k - a_k) = b_k - \tfrac{1}{2}(a_k + b_k) = b_k - m_k ,
\]
by the field laws of \( \nR \) and \( \tfrac{1}{2} + \tfrac{1}{2} = 1 \). So the displacement from \( a \) to \( m \) equals the displacement from \( m \) to \( b \): \( m \) is the **midpoint** of \( a \) and \( b \). For \( a = (1, 4) \) and \( b = (5, -2) \), \( a + b = (6, 2) \) and \( m = (3, 1) \); indeed \( m - a = (2, -3) = b - m \).

(b) Here \( b - a = (3, 1) \) and \( c - d = (3, 1) \), so the first condition holds. Also \( a + c = (4, 3) = b + d \), so \( \tfrac{1}{2}(a + c) = (2, \tfrac{3}{2}) = \tfrac{1}{2}(b + d) \). Read with pictures, \( b - a = c - d \) says that the sides from \( a \) to \( b \) and from \( d \) to \( c \) are the same displacement, as in a parallelogram \( abcd \), and the second condition says that the diagonals from \( a \) to \( c \) and from \( b \) to \( d \) share their midpoint. The picture only suggests the equivalence; Exercise B2 (b) proves it from the laws.
:::

## Exercises

### A. Check your understanding

:::: {#exr-vector-operations-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Compute \( 2(1, 0, -1) - 3(0, 1, 1) + (1, 1, 1) \) and write it in the form \( \sum_k c_k e_k \).
2. \( x = y \).
3. \( x \ne y \).
4. \( x + y = 0 \).
5. \( x \) is parallel to \( e_1 \).
:::

In (b)–(e), \( x, y \in \nR^n \) with \( n \ge 2 \). Decide whether the condition is a condition "for every \( k \)" on the coordinates, and if it is not, say what it asks.
::::

::: {.solution}
(a) \( (2, 0, -2) - (0, 3, 3) + (1, 1, 1) = (3, -2, -4) = 3e_1 - 2e_2 - 4e_3 \), by @prp-standard-basis-expansion.

(b) Yes: \( x_k = y_k \) for every \( k \) (@def-real-n-space).

(c) No: it means \( x_k \ne y_k \) for **some** \( k \).

(d) Yes: \( x_k + y_k = 0 \) for every \( k \).

(e) Yes, once rewritten. Since \( e_1 \ne 0 \), the form for a non-zero vector after @def-parallel-rn says that \( x \) is parallel to \( e_1 \) if and only if \( x = te_1 \) for some \( t \). That holds if and only if \( x_k = 0 \) for every \( k \ge 2 \): if \( x = te_1 \), then \( x_k = t \cdot 0 = 0 \) for \( k \ge 2 \); conversely, if those coordinates vanish, then \( x = x_1 e_1 \) by @eq-standard-expansion. The original wording, with its "some \( c \)", is not of this kind; the rewritten one is.
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

(c) **True.** From \( cx = dx \), adding \( -(dx) = (-d)x \) gives \( (c - d)x = 0 \), by (h) and (i) of @prp-vector-space-laws-rn. Since \( x \ne 0 \), (j) gives \( c - d = 0 \), so \( c = d \).

(d) **False.** Take \( x = e_1 \), \( y = 0 \), \( z = e_2 \). The zero vector is parallel to every vector, so the hypotheses hold. But \( e_2 = te_1 \) fails for every \( t \) (second coordinates \( 1 \ne t \cdot 0 \)), so \( e_2 \) is not parallel to \( e_1 \), by the form for a non-zero vector after @def-parallel-rn, since \( e_1 \ne 0 \). The zero vector is the culprit: for non-zero \( y \), that form gives \( x = sy \) and \( z = ty \), and then \( x \) and \( z \) are parallel (if \( t \ne 0 \), \( x = (st^{-1})z \); if \( t = 0 \), \( z = 0 = 0x \)). In \( \nR^1 \) the statement is true, since any two reals are parallel; that is why \( n \ge 2 \) is assumed.

(e) **True.** Since \( x \ne 0 \), the form for a non-zero vector gives \( y = cx \) for some \( c \). If \( c = 0 \), then \( y = 0x = 0 \), against \( y \ne 0 \). So \( c \ne 0 \).
:::

:::: {#exr-vector-operations-b2}
[B2]

::: {.enumerate options="label=(\alph*)"}
1. Find every \( t \in \nR \) for which \( (1, t, 2) \) is parallel to \( (2, 6, 4) \).
2. Prove part (b) of @exm-midpoints-and-parallelograms for all \( a, b, c, d \in \nR^n \): \( b - a = c - d \) if and only if \( \tfrac{1}{2}(a + c) = \tfrac{1}{2}(b + d) \). Name the laws of @prp-vector-space-laws-rn you use.
:::
::::

::: {.solution}
(a) The vector \( (1, t, 2) \) is non-zero, as its first coordinate is \( 1 \). By the form for a non-zero vector after @def-parallel-rn, the two are parallel if and only if \( (2, 6, 4) = s(1, t, 2) \) for some \( s \). The first coordinate forces \( s = 2 \); then the third reads \( 4 = 2 \cdot 2 \), true, and the second reads \( 6 = 2t \), so \( t = 3 \). Conversely, \( (2, 6, 4) = 2(1, 3, 2) \). So \( t = 3 \) is the only value.

(b) \( (\Rightarrow) \) Suppose \( b - a = c - d \). Add \( a + d \) to both sides. By (a)–(d), the left side becomes \( b + d \) and the right side \( a + c \): for instance \( (b - a) + (a + d) = b + \bigl((-a) + a\bigr) + d = b + 0 + d = b + d \), regrouping by (a), reordering by (b), then (d) and (c). So \( a + c = b + d \), and multiplying by \( \tfrac{1}{2} \) gives \( \tfrac{1}{2}(a + c) = \tfrac{1}{2}(b + d) \).

\( (\Leftarrow) \) Suppose \( \tfrac{1}{2}(a + c) = \tfrac{1}{2}(b + d) \). Multiply by \( 2 \): by (e) and (f), \( 2\bigl(\tfrac{1}{2}(a + c)\bigr) = (2 \cdot \tfrac{1}{2})(a + c) = 1(a + c) = a + c \), and likewise on the right, so \( a + c = b + d \). Add \( -a - d \) to both sides; by (a)–(d) as above, \( c - d = b - a \).
:::

### C. Going deeper

:::: {#exr-vector-operations-c1}
[C1: Exit check: two vectors that are not parallel]

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

**Marking scheme.** (10 points)

- 2: sets up \( (\Rightarrow) \): assumes not parallel and \( sx + ty = 0 \), with the goal \( s = t = 0 \).
- 3: case \( s \ne 0 \): solves for \( x \) as a scalar multiple of \( y \), dividing only after \( s \ne 0 \) is assumed, and reaches a contradiction with the definition.
- 2: case \( s = 0 \): obtains \( ty = 0 \), **justifies** \( y \ne 0 \), and concludes \( t = 0 \) by (j).
- 2: \( (\Leftarrow) \) by contrapositive (or contradiction), producing \( (s, t) \ne (0, 0) \) in **both** clauses of the definition.
- 1: concludes the equivalence.

Fatal errors (0 for the step): dividing by \( s \) without checking \( s \ne 0 \); treating only the clause \( y = cx \) of @def-parallel-rn; concluding \( t = 0 \) from \( ty = 0 \) without \( y \ne 0 \).
:::

<!-- dependency ledger
def-vector-operations-rn (claim): n-tuples, equality in every place; n = 1 read as 1-tuples | def-real-n-space (cited), F2.1 §04 "Longer lists"
def-vector-operations-rn (example): (1,0,-1) + (2,5,3) = (3,5,2); 2x - y = (0,-5,-5) | numeral arithmetic in R; verify/ch09/def-vector-operations-rn.py
def-vector-operations-rn (claim): a_k + (b_k + (-a_k)) = b_k | field laws of R (fd3:def-commutative-ring-and-field), (F2), (F4), (F3)
prp-vector-space-laws-rn (proof): (-1)a = -a in R | fd3:prp-ring-algebra (c) with (F7) (cited)
exm-method-coordinatewise (claim): x + y = x + z gives y = z (closing paragraph after the remark) | prp-vector-space-laws-rn (a)-(d) (cited)
lem-vector-sums-coordinatewise (claim): finitely many vectors v_1..v_m fed to the recursion theorem (which takes a sequence) | finite-lists convention, as in lem-ring-finite-sums's "finite-lists remark"
lem-vector-sums-coordinatewise (proof): Σ_{j=1}^m a_j = Σ_{j=0}^{m-1} a_{j+1}, so lem-ring-finite-sums (from 0) applies to sums from 1; Ch4's sum from 0 agrees with fd2's def-sum-product at lower index 0 | fd2:def-sum-product (general form, cited in the fold); ledgered re-indexing line of the blueprint
prp-standard-basis-expansion (proof): lem-ring-finite-sums (d) applied to the re-indexed sum (terms extended by 0 beyond n) | lem-ring-finite-sums (d) (cited), re-indexing line above
def-parallel-rn (claim): the form for a non-zero x | proved inline
exm-midpoints-and-parallelograms (solution): 1/2 + 1/2 = 1; m = (3,1); midpoints (2, 3/2) | field laws of R (fd3:def-commutative-ring-and-field); verify/ch09/exm-midpoints-and-parallelograms.py
def-parallel-rn (claim): (hook) (3,-6) = -3(-1,2); (quick check) factor -2; t = 2 vs 3/2; s = 1/2 vs 2/3 | numeral arithmetic; verify/ch09/def-parallel-rn.py
exr-vector-operations-a1 (solution): (3, -2, -4) | numeral arithmetic; verify/ch09/exr-vector-operations-a1.py
exr-vector-operations-b1 (solution): counterexample values; (a) adding -x_k in R | field laws of R; verify/ch09/exr-vector-operations-b1.py
exr-vector-operations-b2 (solution): t = 3, s = 2 | numeral arithmetic; verify/ch09/exr-vector-operations-b2.py
-->
