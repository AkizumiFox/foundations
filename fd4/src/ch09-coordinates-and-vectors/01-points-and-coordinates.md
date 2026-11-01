# Points and Coordinates

In school the plane comes first as a picture, a sheet with two axes drawn on it, and pairs of numbers are labels attached to its points afterwards. Analysis turns this around. A point **is** its list of coordinates, and every statement about points, lines, lengths or angles is a statement about real numbers. Chapter 3 has already done this once: there a complex number was by definition a pair of reals, and the plane of complex numbers was the set \( \nR^2 \). This section does the same for lists of any length. It defines \( \nR^n \), describes subsets of it by conditions on coordinates, and introduces the simplest such subsets, the boxes.

**Standing setting.** Throughout the chapter, \( \nR \) is the complete ordered field of *Number Systems: From \(\nN\) to \(\nR\)*, Chapter 5 (@fd3:thm-reals-complete-ordered-field). Every rule proved there for ordered fields holds in \( \nR \), and no proof below looks inside a real number. The letters \( n \) and \( m \) stand for natural numbers with \( n, m \ge 1 \), and \( k \) and \( j \) for indices in \( \{1, \dots, n\} \), unless we say otherwise.

## A point is its list of coordinates

Coordinates entered geometry so that a curve could become an equation and a construction a computation; a proof about the plane then needs the laws of \( \nR \) and nothing else. We take that step for every number of coordinates.

For example, the pair \( (3, -1) \) is a point of the plane, with first coordinate \( 3 \) and second coordinate \( -1 \). The triple \( (2, 0, 5) \) is a point of space. A list of four reals, such as \( (1, -2, 0, 3) \), is just as good a point, though we can no longer draw it. In each case the point is nothing but the list.

*A point is its list of coordinates.*

::: {#def-real-n-space}
[The Space \( \nR^n \)]

Let \( n \in \nN \) with \( n \ge 2 \). The set \( \nR^n \) is the set of **all** \( n \)-tuples
\[
x = (x_1, \dots, x_n) \qquad \text{with } x_k \in \nR \text{ for every } k \in \{1, \dots, n\} ;
\]
it is the set \( X^n \) of @fd2:def-cartesian-product with \( X = \nR \). The real number \( x_k \) is the **\( k \)-th coordinate** of \( x \). For \( n = 1 \) we **define** \( \nR^1 \coloneqq \nR \), and read a real number \( x \) as a list of length one whose first coordinate is \( x_1 \coloneqq x \). The elements of \( \nR^n \) are called **points** or **vectors**; the two words mean the same thing.
:::

In words: a point of \( \nR^n \) is an ordered list of \( n \) real numbers, and nothing more. Two points are equal **if and only if** they agree in **every** place:
\[
x = y \iff x_k = y_k \text{ for every } k \in \{1, \dots, n\} .
\]
*Sets and Functions* defined this equality of \( n \)-tuples (@fd2:def-ordered-pair). For \( n = 1 \) it says only that \( x_1 = y_1 \). So one equation between points of \( \nR^n \) is \( n \) equations between real numbers. For \( n = 2 \) the definition gives \( \nR^2 = \nR \times \nR \). This is also the underlying set of the complex numbers: \( \nC \coloneqq \nR^2 \) in @def-complex-numbers. A complex number and a point of the plane are the same object; Section 9.4 compares what the two readings do with it.

The case \( n = 1 \) is a **convention**, not a theorem. *Sets and Functions* defines tuples only of length at least \( 2 \), and a real number is not a tuple. We declare \( \nR^1 \) to be \( \nR \) so that every statement "for all \( n \ge 1 \)" in this chapter includes the line, with \( x_1 \) meaning \( x \) itself.

**Examples.** The point \( (1, -2, 0, 3) \) lies in \( \nR^4 \); its third coordinate is \( 0 \). The point \( (0, 0, 0) \) lies in \( \nR^3 \). It is not the real number \( 0 \): it is a triple, and *Sets and Functions* agreed that a tuple is never a number (@fd2:def-ordered-pair). And the smallest case: \( \nR^1 \) is the line \( \nR \), where a point has one coordinate, and the equality rule above reads \( x = y \).

**A list is not a set.** Replace the list by a set. The set \( \{1, 2\} \) holds the same two numbers as the point \( (1, 2) \), but it forgets their order, \( \{1, 2\} = \{2, 1\} \), and it forgets repetitions, \( \{1, 1\} = \{1\} \). The points \( (1, 2) \), \( (2, 1) \) and \( (1, 1) \) are three different points of \( \nR^2 \). What a coordinate system needs is exactly what sets lose: which number sits in which place.

**Why this definition.** A point defined as "a position in the plane" cannot be reasoned about: there is no rule for positions, only pictures of them. A point defined as a list of reals carries all the rules of the field \( \nR \) with it, one coordinate at a time. The price is that every geometric word now needs a definition in coordinates. The rest of this chapter supplies these definitions, each by a formula in the coordinates:

- the sum of two points (Section 9.2);
- the dot product (Section 9.3);
- length and distance (Section 9.4);
- the cosine of an angle (Section 9.6).

::: {.remark}
The familiar model of the plane, with an origin, a unit of length and two perpendicular axes, is how we draw a point of \( \nR^2 \) and choose what to prove. It is motivation only. In this chapter a picture is never a reason: every claim is proved from the definitions and the laws of \( \nR \).
:::

::: {.warning}
Order and nesting matter. The points \( (1, 2) \) and \( (2, 1) \) of \( \nR^2 \) are different, and the point \( (1, 2) \) is not the set \( \{1, 2\} \). Nor is \( \nR^2 \times \nR \) literally \( \nR^3 \). Its elements are pairs \( ((x_1, x_2), x_3) \) whose first entry is itself a pair. The elements of \( \nR^3 \) are triples, and a triple is not a pair (*Sets and Functions*, Section 1.4).
:::

::: {.second-reading title="Gluing two lists into one"}
Although \( \nR^m \times \nR^n \) and \( \nR^{m+n} \) are different sets, nothing is lost in passing between them. Let \( g \colon \nR^m \times \nR^n \to \nR^{m+n} \) glue two lists,
\[
g\bigl((x_1, \dots, x_m), (y_1, \dots, y_n)\bigr) \coloneqq (x_1, \dots, x_m, y_1, \dots, y_n) ,
\]
with a real number read as a list of length one when \( m = 1 \) or \( n = 1 \). Then \( g \) is a bijection (@fd2:def-bijective). It is injective. Suppose two pairs have the same image. The images agree in all \( m + n \) places, so the first lists agree in every place and so do the second lists. The two pairs are therefore equal by @fd2:def-ordered-pair. It is surjective: a list \( (z_1, \dots, z_{m+n}) \) is the image of the pair \( \bigl((z_1, \dots, z_m), (z_{m+1}, \dots, z_{m+n})\bigr) \). We use this identification only in words, as in "a point of \( \nR^3 \) is a point of the plane together with a height".
:::

::: {.check}
Which of \( (0, 0, 0) \), \( (1, 2) \) and \( ((1, 2), 3) \) lie in \( \nR^3 \)? How many points has \( \{0, 1\}^3 \)?
:::

::: {.solution}
Only \( (0, 0, 0) \). The point \( (1, 2) \) is a pair, a list of length two. The object \( ((1, 2), 3) \) is also a pair, whose first entry is the pair \( (1, 2) \); it lies in \( \nR^2 \times \nR \), and a pair is not a triple.

The set \( \{0, 1\}^3 \) has **eight** points: each of the three coordinates is \( 0 \) or \( 1 \), and the choices are independent, so there are \( 2 \cdot 2 \cdot 2 = 8 \) lists. Written out, they are \( (0, 0, 0) \), \( (0, 0, 1) \), \( (0, 1, 0) \), \( (0, 1, 1) \), \( (1, 0, 0) \), \( (1, 0, 1) \), \( (1, 1, 0) \) and \( (1, 1, 1) \).
:::

## Sets described by conditions

With points as lists, a subset of \( \nR^n \) is described by a condition on coordinates: the set of all \( x \in \nR^n \) whose coordinates satisfy it. Deciding whether a given point belongs is then a computation with real numbers. Here are the subsets of the plane that return most often.

::: {#exm-subsets-of-the-plane}
[Subsets of the Plane by Conditions]

For each of the following subsets of \( \nR^2 \), name one point that lies in it and one that does not, and check both against the condition.

::: {.enumerate options="label=(\alph*)"}
1. The **first axis** \( A \coloneqq \{ x \in \nR^2 : x_2 = 0 \} \).
2. The **closed first quadrant** \( Q \coloneqq \{ x \in \nR^2 : x_1 \ge 0 \text{ and } x_2 \ge 0 \} \).
3. The **diagonal** \( D \coloneqq \{ x \in \nR^2 : x_1 = x_2 \} \).
4. The graph \( G \coloneqq \{ (t, t^2) : t \in \nR \} \) of the squaring function.
5. The set \( E \coloneqq \{ x \in \nR^2 : x_1^2 + x_2^2 \le 1 \} \).
:::
:::

::: {.solution}
(a) The point \( (5, 0) \) is in \( A \), since its second coordinate is \( 0 \). The point \( (0, 5) \) is not, since \( 5 \ne 0 \).

(b) The point \( (0, 3) \) is in \( Q \): \( 0 \ge 0 \) and \( 3 \ge 0 \). "Closed" means the axes are included. The point \( (-1, 2) \) is not in \( Q \), since \( -1 \ge 0 \) fails; one failed condition is enough, because the two conditions are joined by "and". Compare the condition \( x_1 x_2 \ge 0 \), a single condition that looks similar: the point \( (-1, -1) \) satisfies it, as \( (-1)(-1) = 1 \ge 0 \), but \( (-1, -1) \notin Q \). So \( \{ x : x_1 x_2 \ge 0 \} \) is a larger set than \( Q \): it contains the closed third quadrant as well.

(c) The point \( (-2, -2) \) is in \( D \), and \( (1, 2) \) is not, since \( 1 \ne 2 \).

(d) Here the set is described by listing its points, one for each real \( t \), rather than by a condition. It has a description by a condition too: \( G = \{ x \in \nR^2 : x_2 = x_1^2 \} \). Indeed \( (t, t^2) \) satisfies \( x_2 = x_1^2 \); and if \( x_2 = x_1^2 \), then \( x = (t, t^2) \) with \( t \coloneqq x_1 \). So \( (3, 9) \in G \), while \( (9, 3) \notin G \), because \( 3 \ne 81 = 9^2 \). Section 8.1 treats the graph of any real function in the same way.

(e) The point \( (3/5, 4/5) \) is in \( E \): \( 9/25 + 16/25 = 1 \le 1 \). The point \( (1, 1) \) is not: \( 1 + 1 = 2 > 1 \). In the picture \( E \) is a disk, but the picture is not the definition; Section 9.4 rewrites the condition as "the length of \( x \) is at most \( 1 \)", once length has been defined.
:::

## Boxes

Some conditions treat the coordinates **separately**: one condition on \( x_1 \), one on \( x_2 \), and so on, with no condition linking two coordinates. The quadrant \( Q \) of @exm-subsets-of-the-plane is of this kind; the diagonal \( D \) is not, since \( x_1 = x_2 \) ties the two coordinates together. The simplest separate conditions bound each coordinate between two numbers. On the line that gives a closed interval \( [a, b] \), and in the plane a rectangle \( [a_1, b_1] \times [a_2, b_2] \) with sides parallel to the axes. Later work in analysis traps points inside such sets in \( \nR^n \), so we give them names.

For example, take \( a = (0, 1) \) and \( b = (2, 3) \). The points \( x \) of \( \nR^2 \) with \( 0 \le x_1 \le 2 \) and \( 1 \le x_2 \le 3 \) form the rectangle \( [0, 2] \times [1, 3] \), with corners \( (0, 1) \) and \( (2, 3) \). The point \( (1, 2) \) lies in it. The point \( (3, 2) \) does not, since its first coordinate \( 3 \) is larger than \( 2 \).

::: {#def-box-rn}
[Boxes]

Let \( a, b \in \nR^n \) with \( a_k \le b_k \) for **every** \( k \). The **closed box** with corners \( a \) and \( b \) is
\[
[a_1, b_1] \times \dots \times [a_n, b_n] \coloneqq \{ x \in \nR^n : a_k \le x_k \le b_k \text{ for every } k \} .
\]
If \( a_k < b_k \) for every \( k \), the **open box** with corners \( a \) and \( b \) is
\[
(a_1, b_1) \times \dots \times (a_n, b_n) \coloneqq \{ x \in \nR^n : a_k < x_k < b_k \text{ for every } k \} .
\]
:::

The notation is the product of sets from *Sets and Functions*, Section 4.2, applied to intervals. A point lies in the box exactly when its \( k \)-th coordinate lies in the \( k \)-th interval, for every \( k \). In the open box each \( (a_k, b_k) \) is an interval, not a pair. *Sets and Functions*, Section 1.4 lets context decide between the two readings of \( (a, b) \). Inside a product of this kind it always means the interval.

**Examples.** For \( n = 1 \) a closed box is a closed interval \( [a_1, b_1] \) and an open box an open interval. For \( n = 2 \) the closed box \( [0, 1] \times [0, 1] \) is the unit square. In \( \nR^3 \), the closed box \( [-1, 1] \times [0, 1] \times [2, 2] \) is flat: its third interval is \( [2, 2] = \{2\} \), so every point of it has third coordinate \( 2 \). The definition allows this, since it asks only \( a_3 \le b_3 \). At the extreme, \( a = b \) gives a box with exactly one point, \( a \) itself.

Every box is **non-empty**, and we can name a point in it. The corner \( a \) lies in the closed box, since \( a_k \le a_k \le b_k \) for every \( k \); so does \( b \). The open box contains the center \( c \) with \( c_k \coloneqq (a_k + b_k)/2 \), because \( a_k < b_k \) gives \( a_k < (a_k + b_k)/2 < b_k \) (@fd3:prp-ordered-field-halves (b)). This is why the definition demands \( a_k \le b_k \), and \( a_k < b_k \) for the open box. Without it, \( \{ x \in \nR^2 : 1 \le x_1 \le 0 \} \) would be "a box", an empty one, and its "corners" would mean nothing. Exercise C1 shows that with the condition in place, a closed box determines its corners.

**A set that is not a box.** Let one bound depend on another coordinate:
\[
T \coloneqq \{ x \in \nR^2 : 0 \le x_2 \le x_1 \le 1 \} ,
\]
a triangle in the picture. Each coordinate still lies in \( [0, 1] \), but the bound \( x_2 \le x_1 \) links the two. That one change makes \( T \) no box. Suppose \( T = [p_1, q_1] \times [p_2, q_2] \). The points \( (0, 0) \) and \( (1, 1) \) lie in \( T \), so \( p_1 \le 0 \), \( p_2 \le 0 \), \( 0 \le q_1 \) and \( 1 \le q_2 \). Then \( (0, 1) \) satisfies \( p_1 \le 0 \le q_1 \) and \( p_2 \le 1 \le q_2 \), so it lies in the box. But \( (0, 1) \notin T \), since \( 1 \le 0 \) fails. To show a set is not a box, read bounds off points of the set, then build a point the box must contain.

## Exercises

### A. Check your understanding

:::: {#exr-points-and-coordinates-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Find all \( s, t \in \nR \) with \( (s + t, \; s - t) = (4, 2) \).
2. Is \( (1, 1/2) \) in \( [0, 1] \times [1/2, 1] \)? Is \( (1/2, 0) \)?
3. Describe the set \( \{ x \in \nR^2 : x_1 = x_2 \text{ and } x_1 + x_2 = 1 \} \).
4. Is \( (0, 2) \) in the open box \( (0, 1) \times (1, 3) \)?
5. Write the closed box with corners \( (-1, 0, 2) \) and \( (1, 1, 2) \), and count its points whose coordinates are all integers.
:::
::::

::: {.solution}
(a) By the equality of pairs, \( s + t = 4 \) and \( s - t = 2 \). Adding gives \( 2s = 6 \), so \( s = 3 \); then \( t = 1 \). Conversely \( (3 + 1, \; 3 - 1) = (4, 2) \). So \( s = 3 \), \( t = 1 \) is the only solution.

(b) Yes: \( 0 \le 1 \le 1 \) and \( 1/2 \le 1/2 \le 1 \). No: the second coordinate \( 0 \) fails \( 1/2 \le 0 \).

(c) A point in the set has \( x_1 = x_2 \), so \( 2x_1 = 1 \) and \( x_1 = x_2 = 1/2 \). Conversely \( (1/2, 1/2) \) satisfies both conditions. The set is \( \{ (1/2, 1/2) \} \), a single point.

(d) No. The first coordinate would need \( 0 < 0 < 1 \), and \( 0 < 0 \) is false. The second coordinate passes (\( 1 < 2 < 3 \)), but every coordinate must pass.

(e) The corners satisfy \( -1 \le 1 \), \( 0 \le 1 \) and \( 2 \le 2 \), so the box is \( [-1, 1] \times [0, 1] \times [2, 2] \). A point of it with integer coordinates has \( x_1 \in \{-1, 0, 1\} \), \( x_2 \in \{0, 1\} \) and \( x_3 = 2 \), and every such choice gives one. So there are \( 3 \cdot 2 \cdot 1 = 6 \) of them.
:::

### B. Practice

::: {#exr-points-and-coordinates-b1}
[B1: When one box contains another]

Let \( P = [a_1, b_1] \times \dots \times [a_n, b_n] \) and \( Q = [c_1, d_1] \times \dots \times [c_n, d_n] \) be closed boxes in \( \nR^n \). Prove that \( P \subseteq Q \) if and only if \( c_k \le a_k \) and \( b_k \le d_k \) for every \( k \).
:::

::: {.solution}
\( (\Leftarrow) \) Let \( x \in P \) and fix \( k \). Then \( c_k \le a_k \le x_k \le b_k \le d_k \), so \( c_k \le x_k \le d_k \) by transitivity. As \( k \) was arbitrary, \( x \in Q \). Hence \( P \subseteq Q \).

\( (\Rightarrow) \) Suppose \( P \subseteq Q \). The corner \( a \) lies in \( P \), because \( a_k \le a_k \le b_k \) for every \( k \), so \( a \in Q \): reading coordinate \( k \), \( c_k \le a_k \). Likewise \( b \in P \), so \( b \in Q \) and \( b_k \le d_k \). This holds for every \( k \).

The hypothesis \( a_k \le b_k \) of @def-box-rn was used in \( (\Rightarrow) \), to put the corners in \( P \). Without it the claim fails: the "box" \( \{ x \in \nR : 1 \le x \le 0 \} \) is empty, so it lies in every \( Q \), including \( Q = [5, 6] \), although \( 5 \le 1 \) is false.
:::

::: {#exr-points-and-coordinates-b2}
[B2: Intersections and unions of boxes]

Let \( P = [a_1, b_1] \times \dots \times [a_n, b_n] \) and \( Q = [c_1, d_1] \times \dots \times [c_n, d_n] \) be closed boxes in \( \nR^n \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( P \cap Q = \{ x \in \nR^n : \max\{a_k, c_k\} \le x_k \le \min\{b_k, d_k\} \text{ for every } k \} \). Deduce that \( P \cap Q \) is a closed box if \( \max\{a_k, c_k\} \le \min\{b_k, d_k\} \) for every \( k \), and is empty otherwise.
2. Prove that \( [0, 1] \times [0, 1] \cup [2, 3] \times [0, 1] \) is not a closed box.
:::
:::

::: {.solution}
(a) Fix \( k \) and a real \( t \). Since \( \le \) is a total order on \( \nR \) (@fd3:prp-ordered-ring-rules (i)), \( \max\{a_k, c_k\} \) is one of \( a_k \), \( c_k \) and is \( \ge \) both, so \( a_k \le t \) and \( c_k \le t \) hold together exactly when \( \max\{a_k, c_k\} \le t \). In the same way \( t \le b_k \) and \( t \le d_k \) hold together exactly when \( t \le \min\{b_k, d_k\} \). Now \( x \in P \cap Q \) means \( a_k \le x_k \le b_k \) and \( c_k \le x_k \le d_k \) for every \( k \), which by the two equivalences, with \( t = x_k \), is the displayed condition.

If \( \max\{a_k, c_k\} \le \min\{b_k, d_k\} \) for every \( k \), the displayed set is the closed box with corners \( (\max\{a_k, c_k\})_k \) and \( (\min\{b_k, d_k\})_k \), as @def-box-rn requires. If \( \max\{a_k, c_k\} > \min\{b_k, d_k\} \) for some \( k \), no real \( x_k \) satisfies \( \max\{a_k, c_k\} \le x_k \le \min\{b_k, d_k\} \), by transitivity, so \( P \cap Q = \varnothing \).

(b) Call the union \( U \) and suppose \( U = [p_1, q_1] \times [p_2, q_2] \). The points \( (0, 0) \) and \( (3, 0) \) lie in \( U \), so \( p_1 \le 0 \) and \( 3 \le q_1 \), and \( p_2 \le 0 \le q_2 \). Then \( (3/2, 0) \) lies in the box, since \( p_1 \le 0 \le 3/2 \le 3 \le q_1 \) and \( p_2 \le 0 \le q_2 \). But \( (3/2, 0) \) lies in neither square: \( 3/2 > 1 \) and \( 3/2 < 2 \). So \( (3/2, 0) \notin U \), a contradiction. Hence \( U \) is not a closed box. The argument is the one used above to show that the triangle \( T \) is not a box.
:::

### C. Going deeper

::: {#exr-points-and-coordinates-c1}
[C1: A box determines its corners]

Let \( P = [a_1, b_1] \times \dots \times [a_n, b_n] \) and \( Q = [c_1, d_1] \times \dots \times [c_n, d_n] \) be closed boxes in \( \nR^n \). Prove that if \( P = Q \), then \( a_k = c_k \) and \( b_k = d_k \) for every \( k \).
:::

::: {.solution}
[Hint 1]

Use Exercise B1, twice.
:::

::: {.solution}
[Hint 2]

From \( P \subseteq Q \) and \( Q \subseteq P \), write down four inequalities for each \( k \).
:::

::: {.solution}
Suppose \( P = Q \) and fix \( k \). Since \( P \subseteq Q \), Exercise B1 gives \( c_k \le a_k \) and \( b_k \le d_k \). Since \( Q \subseteq P \), the same exercise with the roles of the boxes exchanged gives \( a_k \le c_k \) and \( d_k \le b_k \). The order of \( \nR \) is antisymmetric, being a total order (@fd3:prp-ordered-ring-rules (i)), so \( a_k = c_k \) and \( b_k = d_k \). As \( k \) was arbitrary, this proves the claim.

So a closed box, as a set, determines the numbers \( a_k \) and \( b_k \). This is what makes "the box \( [a_1, b_1] \times \dots \times [a_n, b_n] \)" an unambiguous name, and "the corners of a box" meaningful. Exercise B1 needed \( a_k \le b_k \) and \( c_k \le d_k \), and so does this result: the empty sets \( \{ x \in \nR : 1 \le x \le 0 \} \) and \( \{ x \in \nR : 5 \le x \le 2 \} \) are equal, with different "corners".

**What a complete answer needs.** (10 points)
- 2: fixes \( k \) and states the goal \( a_k = c_k \), \( b_k = d_k \).
- 3: obtains \( c_k \le a_k \) and \( b_k \le d_k \) from \( P \subseteq Q \) (by B1, or directly from the corners \( a, b \in P \)).
- 3: obtains the reverse inequalities from \( Q \subseteq P \).
- 2: concludes by antisymmetry, for every \( k \).
Slips that lose the step: using one inclusion only; reading the corners off the notation without proof (that is the claim).
:::

<!-- dependency ledger
def-real-n-space (claim): equality of n-tuples is equality in every place; n-tuples defined for n >= 2 only | fd2 F2.1 section 04, paragraph "Longer lists" after fd2:def-ordered-pair (cited)
def-real-n-space (claim): a tuple is not a number; a triple is not a pair | fd2 F2.1 section 04, the working convention after fd2:def-ordered-pair (cited)
def-real-n-space (claim): R^1 := R is a convention, x_1 := x | inline (definition)
def-real-n-space (claim): Sections 9.2, 9.3, 9.4, 9.6 define sum, dot product, length/distance, cosine of an angle by formulas in coordinates | prose pointer, this chapter's blueprint (merged-ch09-f48.md, section 3); nothing depends on it
def-real-n-space (claim): Section 9.4 compares the two readings of R^2 = C | prose pointer to prp-plane-is-complex-plane (section 04); nothing depends on it
def-real-n-space (claim): second-reading fold, gluing map R^m x R^n -> R^{m+n} is a bijection | inline, from fd2:def-ordered-pair and equality of n-tuples (fd2 F2.1 section 04)
def-real-n-space (solution): Quick check, {0,1}^3 has 2*2*2 = 8 points | listed in full in the solution; verify/ch09/def-real-n-space.py
exm-subsets-of-the-plane (solution): (-1)(-1) = 1, 3 != 81, 9/25 + 16/25 = 1, 1 + 1 = 2 > 1 | arithmetic in R (fd3:prp-ring-algebra (c), fd3:prp-ordered-ring-rules); verify/ch09/exm-subsets-of-the-plane.py
exm-subsets-of-the-plane (solution): pointer to Section 8.1 (graphs of real functions, merged-ch08-f47.md def-real-function) and Section 9.4 (length) | prose pointers; nothing depends on them
def-box-rn (example): instance [0,2] x [1,3] with corners (0,1), (2,3); (1,2) in it, (3,2) not | inline; order of R
def-box-rn (claim): product notation [a_1, b_1] x ... x [a_n, b_n] read coordinatewise | fd2 Section 4.2 product A_1 x ... x A_k (before fd2:cor-product-countable; NOTATION row); for n = 1 the interval itself
def-box-rn (claim): intervals [a, b], (a, b) and the pair/interval reading of (a, b) | NOTATION row "intervals"; fd2 F2.1 section 04 convention
def-box-rn (claim): a_k <= a_k <= b_k (reflexivity) | fd3:prp-ordered-ring-rules (i) (total order); used silently
def-box-rn (claim): a_k < (a_k + b_k)/2 < b_k | fd3:prp-ordered-field-halves (b) (cited)
def-box-rn (example): non-example T: (0,1) in the box, not in T | inline; order of R
exr-points-and-coordinates-a1 (solution): all values of (a)-(e), the count 3*2*1 = 6 | verify/ch09/exr-points-and-coordinates-a1.py
exr-points-and-coordinates-b1 (solution): transitivity of <= | fd3:prp-ordered-ring-rules (i); used silently
exr-points-and-coordinates-b2 (solution): max{a, c}, min{b, d} of two reals and their characterization | fd3:prp-ordered-ring-rules (i) (total order); inline
exr-points-and-coordinates-b2 (solution): (3/2, 0) in the box, not in either square | verify/ch09/exr-points-and-coordinates-b2.py
exr-points-and-coordinates-c1 (solution): antisymmetry of <= | fd3:prp-ordered-ring-rules (i) (cited)
exr-points-and-coordinates-c1 (solution): uses exr-points-and-coordinates-b1 | exercise citing an earlier exercise (allowed, STYLE section 6)
-->
