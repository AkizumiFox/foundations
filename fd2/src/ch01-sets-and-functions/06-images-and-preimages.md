# Images and Preimages

A function \( f \colon X \to Y \) sends points to points. Much of analysis asks what it does to **sets** of points. Where does \( f \) send an interval? Which inputs land in a given set of outputs? The first question is answered by the image \( f(A) \), the second by the preimage \( f^{-1}(B) \), and the two are the subject of this section. They look like mirror images of each other, and they are not: preimages respect every set operation of Section 6.2, while images respect only unions. The reason is one quantifier, and by the end of the section we will be able to point at it.

Throughout, \( f \colon X \to Y \) is a function (@def-function), and the unions and intersections of families are those of @def-family-union-intersection. An intersection of a family of subsets of \( Y \) is taken inside \( Y \); of subsets of \( X \), inside \( X \).

## A question about squares

Let \( f \colon \nR \to \nR \), \( f(x) = x^2 \), and take the two intervals \( A = [-1, 0] \) and \( B = [0, 1] \). Squaring \( A \) gives every number from \( 0 \) to \( 1 \), and so does squaring \( B \). So the set of squares of points of \( A \) and the set of squares of points of \( B \) are both \( [0, 1] \), and the points they share make up \( [0, 1] \).

Now intersect first. The intervals \( A \) and \( B \) share only the point \( 0 \), so \( A \cap B = \{0\} \), and its only square is \( 0 \). Squaring the intersection gives \( \{0\} \); intersecting the squares gives \( [0, 1] \). The order of the two operations matters.

Try the same thing backwards. Instead of pushing sets forwards through \( f \), pull them back: for a set \( C \) of outputs, collect the inputs whose squares lie in \( C \). Take \( C = [0, 1] \) and \( D = [1, 4] \). The inputs with square in \( C \) form \( [-1, 1] \), those with square in \( D \) form \( [-2, -1] \cup [1, 2] \), and the inputs common to both are \( -1 \) and \( 1 \). Intersecting first gives \( C \cap D = \{1\} \), whose inputs are again \( -1 \) and \( 1 \). This time the order does not matter.

Is that an accident of these intervals? No. Pulling back will turn out to respect intersections for every function and all sets, while pushing forwards respects them exactly for the injective functions. To see why, we first need names for the two operations.

## Images and preimages

The two sets in the question above keep recurring: "all the values \( f(a) \) for \( a \) in \( A \)" and "all the inputs \( x \) with \( f(x) \) in \( B \)". The first was already used in Section 6.4 for \( A = X \), where it is the range of \( f \).

*An image hides a "there exists"; a preimage hides nothing.*

::: {#def-image}
[Image]

Let \( f \colon X \to Y \) be a function and \( A \subseteq X \). The **image** of \( A \) under \( f \) is the set
\[
    f(A) \coloneqq \{ y \in Y : \text{there exists } a \in A \text{ with } f(a) = y \}.
\]
We also write it \( \{ f(a) : a \in A \} \). In symbols, for every \( y \),
\[
    y \in f(A) \iff y \in Y \wedge \exists a \in A\ \, f(a) = y .
\]
:::

::: {#def-preimage}
[Preimage]

Let \( f \colon X \to Y \) be a function and \( B \subseteq Y \). The **preimage** of \( B \) under \( f \), also called its **inverse image**, is the set
\[
    f^{-1}(B) \coloneqq \{ x \in X : f(x) \in B \}.
\]
In symbols, for every \( x \), \( x \in f^{-1}(B) \iff x \in X \wedge f(x) \in B \). The preimage is defined for **every** function \( f \), whether or not \( f \) has an inverse.
:::

In Section 6.4 a point \( x \) with \( f(x) = y \) was called a preimage of \( y \); that is, \( x \in f^{-1}(\{y\}) \). So the preimages of a point \( y \) are the elements of the preimage of the set \( \{y\} \).

Read the two definitions clause by clause.

- **The ambient sets.** Both are sets by specification (@def-set-builder): \( f(A) \) is carved out of the codomain \( Y \), and \( f^{-1}(B) \) out of the domain \( X \). So \( f(A) \subseteq Y \) and \( f^{-1}(B) \subseteq X \) always. The shorthand \( \{ f(a) : a \in A \} \) names the same subset of \( Y \); it is a way of writing, not a new rule of set formation.
- **The image.** "\( y \in f(A) \)" says that \( y \) is **hit** by some point of \( A \). The words "there exists" are part of the definition. To **use** a line \( y \in f(A) \), we must name a witness: "let \( a \in A \) with \( f(a) = y \)". That is the rule \( \exists \)E of Chapter 4 (Section 4.6), and the name must be fresh. To **prove** \( y \in f(A) \), we exhibit a witness, by \( \exists \)I (Chapter 4, Section 4.5).
- **The preimage.** "\( x \in f^{-1}(B) \)" says that \( x \) is sent **into** \( B \). There is no quantifier. For \( x \in X \), a line \( x \in f^{-1}(B) \) is used and proved by one substitution: it is exchanged for \( f(x) \in B \), and back.
- **The symbol \( f^{-1} \).** In \( f^{-1}(B) \), the symbol \( f^{-1} \) is not a function that is applied to \( B \). The whole expression \( f^{-1}(B) \) is the name of a set built from \( f \) and \( B \). Section 6.5 used \( f^{-1} \) for the inverse function of a bijection; the remark at the end of this section reconciles the two readings.

The notation \( f(A) \) puts a set where \( f(x) \) puts a point. When the letter in the brackets has been declared a subset of \( X \), the expression is an image; when it has been declared a point, it is a value. As with the pair and the interval of Section 6.3, the declaration decides.

Start with the smallest possible example, where everything can be listed.

::: {#exm-images-finite}
[Images and preimages by listing]

Let \( X = \{1, 2, 3, 4\} \), \( Y = \{0, 1, 2, 5\} \), and let \( f \colon X \to Y \) be given by
\[
    f(1) = 1, \quad f(2) = 2, \quad f(3) = 0, \quad f(4) = 1 .
\]
Find \( f(\{1, 4\}) \), \( f(\{2, 3\}) \), \( f(X) \), and \( f(\emptyset) \); then \( f^{-1}(\{1\}) \), \( f^{-1}(\{0, 2\}) \), \( f^{-1}(\{5\}) \), \( f^{-1}(\emptyset) \), and \( f^{-1}(Y) \).
:::

::: {.solution}
*Images.* A point \( y \) lies in \( f(A) \) when some \( a \in A \) has \( f(a) = y \), so we apply \( f \) to each point of \( A \) and collect the results. \( f(\{1, 4\}) = \{1\} \): both points go to \( 1 \), and a set lists \( 1 \) once. \( f(\{2, 3\}) = \{0, 2\} \). \( f(X) = \{0, 1, 2\} \), the range; \( 5 \) is not in it. \( f(\emptyset) = \emptyset \): a point \( y \) in it would need some \( a \in \emptyset \), and there is none.

*Preimages.* A point \( x \in X \) lies in \( f^{-1}(B) \) when \( f(x) \in B \), so we test each of the four points of \( X \). \( f^{-1}(\{1\}) = \{1, 4\} \). \( f^{-1}(\{0, 2\}) = \{2, 3\} \). \( f^{-1}(\{5\}) = \emptyset \): no point of \( X \) is sent to \( 5 \). \( f^{-1}(\emptyset) = \emptyset \), since \( f(x) \in \emptyset \) never holds. \( f^{-1}(Y) = X \), since \( f(x) \in Y \) holds for every \( x \in X \).
:::

The two computations differ in shape. For the image we ran through the points of \( A \) and **produced** outputs. For the preimage we ran through the points of \( X \) and **tested** each one. That is the "there exists" of the image and the plain condition of the preimage, seen on a four-point set.

The example also contains a non-example by minimal change. The sets \( \{1\} \) and \( \{5\} \) are both one-point subsets of \( Y \). The first has a two-point preimage; change \( 1 \) to \( 5 \) and the preimage becomes empty, because \( 5 \) lies outside the range. The preimage of a non-empty set can be empty. What fails is the existence of a point of \( X \) sent into the set.

Why is the preimage defined for **every** function, when \( f^{-1} \) as a function exists only for bijections? Because the question "which inputs land in \( B \)?" makes sense for any \( f \): its answer may be empty, or contain many points, and neither is a problem for a set. The function \( f^{-1} \) of Section 6.5 asks for more: exactly one input for each output. This is why analysis states its definitions with preimages. "The preimage of every open set is open" makes sense for every function; Chapter 24 uses it to characterize continuity.

::: {.warning}
The preimage \( f^{-1}(B) \) does not presuppose that \( f \) is invertible. For the squaring map on \( \nR \), which has no inverse function, \( f^{-1}(\{4\}) = \{-2, 2\} \) is a perfectly good set. What the symbol does **not** give is a value "\( f^{-1}(4) \)": that would be a point, and there are two candidates.
:::

## Computing images and preimages

With an infinite set, listing is impossible, and the definitions are used as they stand. The image asks us to name witnesses; the preimage asks us to solve an inequality.

::: {#exm-images-of-square}
[Images and preimages of intervals under squaring]

Let \( f \colon \nR \to \nR \), \( f(x) = x^2 \). Prove that

::: {.enumerate options="label=(\alph*)"}
1. \( f([-1, 2]) = [0, 4] \);
2. \( f^{-1}([1, 4]) = [-2, -1] \cup [1, 2] \);
3. \( f^{-1}(\{-1\}) = \emptyset \);
4. \( f^{-1}(f([0, 1])) = [-1, 1] \).
:::
:::

::: {.solution}
We use school facts about real numbers, \( x^2 \ge 0 \) and every \( y \ge 0 \) has a square root \( \sqrt y \ge 0 \), and, by @thm-squares-order, for \( s, t \ge 0 \), \( s \le t \) holds exactly when \( s^2 \le t^2 \).

(a) *Idea.* An image is proved equal to a set by two inclusions. The inclusion \( \subseteq \) uses \( y \in f([-1, 2]) \), so it names a witness. The inclusion \( \supseteq \) proves \( y \in f([-1, 2]) \), so it exhibits one.

\( (\subseteq) \) Let \( y \in f([-1, 2]) \). Then \( y = a^2 \) for some \( a \in [-1, 2] \); name it \( a \). Certainly \( y = a^2 \ge 0 \). If \( a \ge 0 \), then \( 0 \le a \le 2 \), so \( a^2 \le 4 \). If \( a < 0 \), then \( 0 < -a \le 1 \), so \( a^2 = (-a)^2 \le 1 \le 4 \). In either case \( 0 \le y \le 4 \), that is, \( y \in [0, 4] \).

\( (\supseteq) \) Let \( y \in [0, 4] \). Take \( a \coloneqq \sqrt y \). Then \( 0 \le a \le \sqrt 4 = 2 \), so \( a \in [-1, 2] \), and \( f(a) = y \). Hence \( y \in f([-1, 2]) \).

The witness in \( (\supseteq) \) could have been \( -\sqrt y \) for \( y \le 1 \), but not for \( y > 1 \), where \( -\sqrt y < -1 \). One witness per \( y \) is all we need, so we choose the one that always works.

(b) *Idea.* A preimage is a set of solutions of a condition on \( x \). No witness is needed: each line is an equivalence.

For every \( x \in \nR \),
\[
\begin{aligned}
    x \in f^{-1}([1, 4])
    &\iff 1 \le x^2 \le 4
     \iff 1 \le \abs{x} \le 2 \\
    &\iff x \in [-2, -1] \cup [1, 2] .
\end{aligned}
\]
The first step is @def-preimage. The second uses \( x^2 = \abs{x}^2 \) and @thm-squares-order with \( s, t \) among \( 1 \), \( \abs{x} \), \( 2 \). The third splits by the sign of \( x \): for \( x \ge 0 \), \( \abs{x} = x \), and for \( x < 0 \), \( \abs{x} = -x \). So the two sets have the same elements.

(c) For every \( x \in \nR \), \( f(x) = x^2 \ge 0 > -1 \), so \( f(x) \in \{-1\} \) never holds. The preimage is empty, although \( \{-1\} \) is not.

(d) First \( f([0, 1]) = [0, 1] \), by the argument of (a): a square of a number in \( [0, 1] \) lies in \( [0, 1] \), and each \( y \in [0, 1] \) is \( (\sqrt y)^2 \) with \( \sqrt y \in [0, 1] \). Then, as in (b), for every \( x \in \nR \), \( x \in f^{-1}([0, 1]) \iff 0 \le x^2 \le 1 \iff \abs{x} \le 1 \iff x \in [-1, 1] \).
:::

Part (d) is worth a second look. We started with \( [0, 1] \), pushed it forwards and pulled it back, and got the bigger set \( [-1, 1] \). The negative numbers came in because they have the same squares as the positive ones. That is a failure of injectivity, and the subsection "There and back" later in this section proves that it is the only way the round trip can grow a set.

::: {.check}
For \( f(x) = x^2 \) on \( \nR \), find \( f^{-1}(\{4\}) \), \( f^{-1}([-4, -1]) \), and \( f(f^{-1}([-1, 1])) \).
:::

::: {.solution}
\( f^{-1}(\{4\}) = \{-2, 2\} \), the solutions of \( x^2 = 4 \). \( f^{-1}([-4, -1]) = \emptyset \), since \( x^2 \ge 0 > -1 \). For the last, \( f^{-1}([-1, 1]) = \{ x \in \nR : -1 \le x^2 \le 1 \} = [-1, 1] \), and then \( f([-1, 1]) = [0, 1] \), by the argument of @exm-images-of-square (a). So \( f(f^{-1}([-1, 1])) = [0, 1] \), which is smaller than \( [-1, 1] \): the negative numbers are not squares.
:::

## Sets of numbers as images

Chapter 11 works with three ways of making new sets of real numbers from old ones: for \( A, B \subseteq \nR \) and \( c \in \nR \),
\[
    -A \coloneqq \{ -a : a \in A \}, \quad cA \coloneqq \{ ca : a \in A \}, \quad A + B \coloneqq \{ a + b : a \in A,\ b \in B \}.
\]
The first two are images in the sense of @def-image. In the third, two letters vary, and the notation means, as for @def-cartesian-product,
\[
    A + B = \{ y \in \nR : \exists a \in A\ \exists b \in B\ \, y = a + b \}.
\]
Each is an image, and seeing them as images tells us how to prove things about them: an element of \( A + B \) is used by naming two witnesses.

::: {#exm-sets-of-numbers-as-images}
[Reflections, scalings and sums as images]

Let \( A, B \subseteq \nR \) and \( c \in \nR \).

::: {.enumerate options="label=(\alph*)"}
1. Let \( n \colon \nR \to \nR \), \( n(x) = -x \), and \( m_c \colon \nR \to \nR \), \( m_c(x) = cx \). Show that \( -A = n(A) \) and \( cA = m_c(A) \).
2. Let \( s \colon \nR \times \nR \to \nR \), \( s(a, b) = a + b \). Show that \( A + B = s(A \times B) \).
3. Compute \( -[0, 1] \), \( \{1, 2\} + \{10, 20\} \), and \( \{1, 2\} + \{1, 2\} \).
:::
:::

::: {.solution}
(a) By the shorthand of @def-image, \( n(A) = \{ n(a) : a \in A \} = \{ -a : a \in A \} \), which is \( -A \) as written above. In the same way, \( m_c(A) = \{ ca : a \in A \} = cA \). Nothing more is needed: the set-builder \( \{ -a : a \in A \} \) **is** the image, written in the form of @def-image.

(b) Here the domain is the product \( \nR \times \nR \) of Section 6.3, and \( A \times B \subseteq \nR \times \nR \). An element \( p \) of \( A \times B \) is a pair \( (a, b) \) with \( a \in A \) and \( b \in B \) (@def-cartesian-product).

\( (\subseteq) \) Let \( y \in A + B \). Then \( y = a + b \) for some \( a \in A \) and \( b \in B \); name them. The pair \( p \coloneqq (a, b) \) lies in \( A \times B \), and \( s(p) = a + b = y \). So \( y \in s(A \times B) \), with witness \( p \).

\( (\supseteq) \) Let \( y \in s(A \times B) \). Then \( y = s(p) \) for some \( p \in A \times B \); name it \( p \). Since \( p \in A \times B \), \( p = (a, b) \) for some \( a \in A \) and \( b \in B \); name them. Then \( y = s(a, b) = a + b \), so \( y \in A + B \).

Unwinding \( y \in s(A \times B) \) took **two** layers of witnesses: first the pair \( p \) from the image, then its coordinates \( a, b \) from the product.

(c) \( -[0, 1] = [-1, 0] \): if \( y = -a \) with \( 0 \le a \le 1 \), then \( -1 \le y \le 0 \); and if \( -1 \le y \le 0 \), then \( a \coloneqq -y \in [0, 1] \) and \( y = -a \). Next, \( \{1, 2\} + \{10, 20\} \) is the image of the four pairs \( (1, 10) \), \( (1, 20) \), \( (2, 10) \), \( (2, 20) \), so it is \( \{11, 21, 12, 22\} \), with 4 elements. Finally, \( \{1, 2\} + \{1, 2\} \) is the image of \( (1, 1) \), \( (1, 2) \), \( (2, 1) \), \( (2, 2) \), which is \( \{2, 3, 4\} \), with only 3 elements: the pairs \( (1, 2) \) and \( (2, 1) \) have the same image \( 3 \), because \( s \) is not injective.
:::

This pays a debt. Chapter 11 introduces these sets by set-builder, and part (b) shows that even the two-variable form is an image, of \( A \times B \) under \( s \), so @def-image is what all three rest on: an element of \( A + B \) is used by naming two witnesses, as in part (b).

## Preimages respect every operation

Now the promised theorem. The preimage of a union is the union of the preimages, and the same holds for intersections, complements, and differences. No hypothesis on \( f \) is needed.

::: {#thm-preimage-operations}
[Preimages of Set Operations]

Let \( f \colon X \to Y \) be a function.

::: {.enumerate options="label=(\alph*)"}
1. For every family \( (B_i)_{i \in I} \) of subsets of \( Y \),
\( \displaystyle f^{-1}\Bigl(\bigcup_{i \in I} B_i\Bigr) = \bigcup_{i \in I} f^{-1}(B_i) \).
2. For every family \( (B_i)_{i \in I} \) of subsets of \( Y \),
\( \displaystyle f^{-1}\Bigl(\bigcap_{i \in I} B_i\Bigr) = \bigcap_{i \in I} f^{-1}(B_i) \),
the intersection on the left taken in \( Y \) and on the right in \( X \).
3. For every \( B \subseteq Y \), \( f^{-1}(Y \setminus B) = X \setminus f^{-1}(B) \).
4. For all \( B, C \subseteq Y \), \( f^{-1}(B \setminus C) = f^{-1}(B) \setminus f^{-1}(C) \).
:::
:::

::: {.idea}
Unwind each side at a point \( x \in X \). A preimage turns "\( x \) is in the preimage of something" into "\( f(x) \) is in that something". The set operation is then applied to **one** point, \( f(x) \), and on the other side it is applied to one point, \( x \), whose membership in each \( f^{-1}(B_i) \) is again a statement about \( f(x) \). The two sides say the same thing about the same point. No point is ever named as a witness for an image. The only "there exists" is over the index \( i \) in (a), and its witness is handed straight from \( \exists \)E to \( \exists \)I, so no witness can go wrong, and nothing is asked of \( f \).
:::

::: {.proof}
Every set in the four laws is a subset of \( X \): a preimage is one by @def-preimage, a union of subsets of \( X \) is one because each of its elements lies in some \( f^{-1}(B_i) \subseteq X \), an intersection in \( X \) and a difference \( X \setminus \cdot \) are subsets of \( X \) by @def-family-union-intersection and @def-set-operations, and \( f^{-1}(B) \setminus f^{-1}(C) \subseteq f^{-1}(B) \). For two subsets \( S, T \) of \( X \), a point outside \( X \) lies in neither, so by @def-set-equality, \( S = T \) holds as soon as \( x \in S \iff x \in T \) for every \( x \in X \). Let \( x \in X \). In each chain below, the steps labeled (P) are @def-preimage, which applies because \( x \in X \); the others are named.

(a)
\[
\begin{aligned}
    x \in f^{-1}\Bigl(\bigcup_{i \in I} B_i\Bigr)
    &\iff f(x) \in \bigcup_{i \in I} B_i && \text{(P)} \\
    &\iff \exists i \in I,\ f(x) \in B_i && \text{(union)} \\
    &\iff \exists i \in I,\ x \in f^{-1}(B_i) && \text{(P)} \\
    &\iff x \in \bigcup_{i \in I} f^{-1}(B_i) && \text{(union).}
\end{aligned}
\]
The steps marked "union" are @def-family-union-intersection. In the third step, for each fixed \( i \in I \) the statements \( f(x) \in B_i \) and \( x \in f^{-1}(B_i) \) are equivalent, so one holds for some \( i \) exactly when the other does: a witness \( i \) for one is a witness for the other.

(b)
\[
\begin{aligned}
    x \in f^{-1}\Bigl(\bigcap_{i \in I} B_i\Bigr)
    &\iff f(x) \in \bigcap_{i \in I} B_i && \text{(P)} \\
    &\iff \forall i \in I,\ f(x) \in B_i && \text{(intersection)} \\
    &\iff \forall i \in I,\ x \in f^{-1}(B_i) && \text{(P)} \\
    &\iff x \in \bigcap_{i \in I} f^{-1}(B_i) && \text{(intersection).}
\end{aligned}
\]
In the second step, the intersection in \( Y \) is \( \{ y \in Y : \forall i \in I,\ y \in B_i \} \), and the clause \( f(x) \in Y \) holds because \( f \) maps into \( Y \). In the last step, the intersection in \( X \) is \( \{ x' \in X : \forall i \in I,\ x' \in f^{-1}(B_i) \} \), and the clause \( x \in X \) holds by assumption. The third step holds for each \( i \), hence for all \( i \) at once.

(c)
\[
\begin{aligned}
    x \in f^{-1}(Y \setminus B)
    &\iff f(x) \in Y \setminus B && \text{(P)} \\
    &\iff f(x) \notin B && (f(x) \in Y) \\
    &\iff x \notin f^{-1}(B) && \text{(P, negated)} \\
    &\iff x \in X \setminus f^{-1}(B) && (x \in X).
\end{aligned}
\]
The second and fourth steps are @def-set-operations for \( \setminus \), with the clause that is known to hold dropped. The third negates both sides of the equivalence \( x \in f^{-1}(B) \iff f(x) \in B \), as @exm-iff-negations allows.

(d)
\[
\begin{aligned}
    x \in f^{-1}(B \setminus C)
    &\iff f(x) \in B \wedge f(x) \notin C \\
    &\iff x \in f^{-1}(B) \wedge x \notin f^{-1}(C) \\
    &\iff x \in f^{-1}(B) \setminus f^{-1}(C),
\end{aligned}
\]
by (P) and @def-set-operations in the first step, (P) and @exm-iff-negations in the second, and @def-set-operations in the third.

In each chain the equivalences link up, so the first statement is equivalent to the last, for every \( x \in X \). This proves the theorem.
:::

The proof never named a witness for an image (the index \( i \) in (a) is taken by \( \exists \)E and passed unchanged to \( \exists \)I) and never used a property of \( f \) beyond its being a function. That is the whole content of the slogan: a preimage hides nothing. Each law of sets was carried across by the corresponding law of logic, applied to the one point \( f(x) \), exactly as in Section 6.2.

The empty family is covered. When \( I = \emptyset \), the intersection of the empty family in \( Y \) is \( Y \) and in \( X \) is \( X \) (@def-family-union-intersection), and (b) says \( f^{-1}(Y) = X \), which is true. The union of the empty family is \( \emptyset \), and (a) says \( f^{-1}(\emptyset) = \emptyset \), also true. This is the payoff of taking intersections inside a named ambient set: the theorem holds with no exception for \( I = \emptyset \).

Preimages also behave well under composition, with the order reversed. We will need this in Chapter 24, to show that composites of continuous maps are continuous.

::: {#prp-preimage-composition}
[Preimage under a Composite]

Let \( f \colon X \to Y \) and \( g \colon Y \to Z \) be functions, and \( C \subseteq Z \). Then
\[
    (g \circ f)^{-1}(C) = f^{-1}\bigl(g^{-1}(C)\bigr).
\]
:::

::: {.proof}
Both sides are subsets of \( X \) by @def-preimage, so, as in the proof of @thm-preimage-operations, it suffices to compare memberships of each \( x \in X \). For \( x \in X \),
\[
\begin{aligned}
    x \in (g \circ f)^{-1}(C)
    &\iff g(f(x)) \in C
     \iff f(x) \in g^{-1}(C) \\
    &\iff x \in f^{-1}\bigl(g^{-1}(C)\bigr).
\end{aligned}
\]
The first step is @def-preimage for \( g \circ f \) with @def-composition; the second is @def-preimage for \( g \), which applies because \( f(x) \in Y \); the third is @def-preimage for \( f \). This proves the proposition.
:::

To pull a set back through "first \( f \), then \( g \)", pull it back through \( g \) first. This is the same reversal as for the inverse of a composite (Exercise B2 of Section 6.5), and here no function needs an inverse.

## Images respect unions

Now push forwards. For unions the result is the same as for preimages, but the proof is different in kind: it has to name witnesses.

::: {#thm-image-union}
[Image of a Union]

Let \( f \colon X \to Y \) be a function, and let \( (A_i)_{i \in I} \) be a family of subsets of \( X \). Then
\[
    f\Bigl(\bigcup_{i \in I} A_i\Bigr) = \bigcup_{i \in I} f(A_i).
\]
:::

::: {.idea}
Unwind the left side at a point \( y \): there is a point \( a \) in the union with \( f(a) = y \), and being in the union means there is an index \( i \) with \( a \in A_i \). So "there is \( a \), and there is \( i \)". The right side says "there is \( i \), and there is \( a \)". The two differ only in the order of two "there exists", and two existential quantifiers can be exchanged: name both witnesses, then reintroduce them so that the quantifiers come out in the other order.
:::

::: {.proof}
We prove two inclusions. The union \( \bigcup_{i \in I} A_i \) is a subset of \( X \), so its image is defined.

\( (\subseteq) \) Let \( y \in f(\bigcup_{i \in I} A_i) \). By @def-image, \( y \in Y \) and there is \( a \in \bigcup_{i \in I} A_i \) with \( f(a) = y \); name such a point \( a \) \( [\rulename{\exists E}] \). By @def-family-union-intersection, there is \( j \in I \) with \( a \in A_j \); name such an index \( j \) \( [\rulename{\exists E}] \). Now \( a \in A_j \) and \( f(a) = y \), so \( y \in f(A_j) \), with witness \( a \) \( [\rulename{\exists I}] \). Since \( j \in I \), \( y \in \bigcup_{i \in I} f(A_i) \), with witness \( j \) \( [\rulename{\exists I}] \).

\( (\supseteq) \) Let \( y \in \bigcup_{i \in I} f(A_i) \). There is \( j \in I \) with \( y \in f(A_j) \); name it \( j \) \( [\rulename{\exists E}] \). So \( y \in Y \), and there is \( a \in A_j \) with \( f(a) = y \); name it \( a \) \( [\rulename{\exists E}] \). Since \( a \in A_j \) and \( j \in I \), \( a \in \bigcup_{i \in I} A_i \), with witness \( j \) \( [\rulename{\exists I}] \). Since \( f(a) = y \), \( y \in f(\bigcup_{i \in I} A_i) \), with witness \( a \) \( [\rulename{\exists I}] \).

This proves the theorem.
:::

Look at the order of the tags in \( (\subseteq) \): \( \exists \)E for \( a \), \( \exists \)E for \( j \), \( \exists \)I for \( a \), \( \exists \)I for \( j \). The witnesses are reintroduced in the same order they were named. Because \( \exists \)I builds the formula from the inside out, \( a \), which was the outer witness, ends up as the inner one. To rebuild the quantifiers in their old order, the \( \exists \)I steps would have run in reverse, \( \exists \)I for \( j \) before \( \exists \)I for \( a \). That the order is not reversed is the exchange of the two "there exists". The two \( \exists \)E boxes may close at the end because the conclusion \( y \in \bigcup_i f(A_i) \) mentions neither \( a \) nor \( j \): the side condition of \( \exists \)E (Chapter 4, Section 4.6) holds. The case \( I = \emptyset \) needs no separate treatment: both sides are \( f(\emptyset) = \emptyset \) and \( \emptyset \).

## Images and intersections

For unions, images behave. For intersections, the question of the opening showed they do not: \( f(A \cap B) = \{0\} \) and \( f(A) \cap f(B) = [0, 1] \) for the squaring map. One inclusion survives, and the other fails in a way that is instructive, because the failing inclusion has a tempting false proof.

::: {#exm-image-two-witnesses}
[Two witnesses under one name]

Here is a "proof" that \( f(A) \cap f(B) \subseteq f(A \cap B) \) for every function \( f \colon X \to Y \) and all \( A, B \subseteq X \).

> (1) Let \( y \in f(A) \cap f(B) \). (2) Then \( y \in f(A) \), so \( y = f(x) \) for some \( x \in A \). (3) Also \( y \in f(B) \), so \( y = f(x) \) for some \( x \in B \). (4) Hence \( x \in A \) and \( x \in B \), so \( x \in A \cap B \). (5) Therefore \( y = f(x) \in f(A \cap B) \).

Show that the conclusion is false, and find the line that fails.
:::

::: {.solution}
*The conclusion is false.* Take \( f(x) = x^2 \) on \( \nR \), \( A = \{-1\} \), and \( B = \{1\} \). Then \( f(A) = f(B) = \{1\} \), so \( f(A) \cap f(B) = \{1\} \); but \( A \cap B = \emptyset \), so \( f(A \cap B) = \emptyset \), and \( 1 \notin \emptyset \).

*The failing line is (3).* Line (2) is a correct \( \exists \)E: it names a witness \( x \in A \) with \( f(x) = y \). Line (3) performs a second \( \exists \)E, on \( y \in f(B) \), and gives its witness the **same** name \( x \). The rule requires a fresh name (Chapter 4, Section 4.6). The statement "\( y = f(b) \) for some \( b \in B \)" promises some point of \( B \), not the point already named. Reusing the name silently asserts that the two witnesses are equal, and nothing says they are. This is the error "one name for two witnesses", entry (N4) of the catalogue of what is not allowed (Chapter 5, Section 5.6).

*A counterexample to the step.* With the data above and \( y = 1 \): line (2) names \( x = -1 \), the only point of \( A \). The only point of \( B \) with square \( 1 \) is \( 1 \ne -1 \), so line (3), with the name \( x \) meaning the \( x \) of line (2), asserts \( -1 \in B \), which is false. Lines (4) and (5) are correct inferences from what (3) wrongly asserts.
:::

::: {.warning}
When you unwind two images, give the two witnesses two names: "\( y = f(a) \) with \( a \in A \), and \( y = f(b) \) with \( b \in B \)". A single name is a hidden claim that \( a = b \), which is exactly what fails for \( x \mapsto x^2 \) with \( a = -1 \), \( b = 1 \). If the proof needs them equal, it must prove it.
:::

With two names, the proof gets as far as \( f(a) = y = f(b) \) and stops. To conclude \( a = b \) we need exactly the property that injectivity supplies. So the inclusion should hold for injective functions, and only for them.

::: {#thm-image-intersection}
[Image of an Intersection]

Let \( f \colon X \to Y \) be a function.

::: {.enumerate options="label=(\alph*)"}
1. For all \( A, B \subseteq X \), \( f(A \cap B) \subseteq f(A) \cap f(B) \).
2. The equality \( f(A \cap B) = f(A) \cap f(B) \) holds for all \( A, B \subseteq X \) **if and only if** \( f \) is injective.
:::
:::

*Try it first (ten minutes): if \( f \) is injective, why should \( f(A) \cap f(B) \subseteq f(A \cap B) \) hold? Start from "let \( y \in f(A) \cap f(B) \)" and unwind both images, with two names.*

::: {.idea}
The attempt names \( a \in A \) and \( b \in B \) with \( f(a) = y = f(b) \), and then has two points where it needs one in \( A \cap B \). That is the obstacle @exm-image-two-witnesses tried to wish away. Injectivity removes it: \( f(a) = f(b) \) gives \( a = b \), so \( a \) lies in both sets.

For the converse, run the failure backwards. If equality holds for **all** \( A, B \), use it on the smallest sets that could show a failure of injectivity: two one-point sets \( \{x_1\} \) and \( \{x_2\} \) with \( f(x_1) = f(x_2) \).

*Before reading on: which line of the proof of \( (\Leftarrow) \) uses injectivity, and which line of \( (\Rightarrow) \) uses that equality holds for all sets rather than for one pair?*
:::

::: {.proof}
(a) Let \( y \in f(A \cap B) \). By @def-image there is \( c \in A \cap B \) with \( f(c) = y \); name it \( c \). Since \( c \in A \), \( y \in f(A) \), with witness \( c \); since \( c \in B \), \( y \in f(B) \), with witness \( c \). So \( y \in f(A) \cap f(B) \).

(b) \( (\Leftarrow) \) Suppose \( f \) is injective, and let \( A, B \subseteq X \). By (a) it suffices to prove \( f(A) \cap f(B) \subseteq f(A \cap B) \). Let \( y \in f(A) \cap f(B) \). Since \( y \in f(A) \), there is \( a \in A \) with \( f(a) = y \); name it \( a \) \( [\rulename{\exists E}] \). Since \( y \in f(B) \), there is \( b \in B \) with \( f(b) = y \); name it \( b \), a new name \( [\rulename{\exists E}] \). Then \( f(a) = y = f(b) \), so \( a = b \) because \( f \) is injective (@def-injective). Hence \( a \in B \), so \( a \in A \cap B \), and \( y = f(a) \in f(A \cap B) \), with witness \( a \) \( [\rulename{\exists I}] \).

\( (\Rightarrow) \) Suppose \( f(A \cap B) = f(A) \cap f(B) \) for all \( A, B \subseteq X \). Let \( x_1, x_2 \in X \) with \( f(x_1) = f(x_2) \), and apply the hypothesis to \( A \coloneqq \{x_1\} \) and \( B \coloneqq \{x_2\} \). Now \( f(x_1) \in f(A) \), with witness \( x_1 \), and \( f(x_1) = f(x_2) \in f(B) \), with witness \( x_2 \). So \( f(x_1) \in f(A) \cap f(B) = f(A \cap B) \). Hence there is \( c \in \{x_1\} \cap \{x_2\} \) with \( f(c) = f(x_1) \); name it \( c \). Then \( c = x_1 \) and \( c = x_2 \), so \( x_1 = x_2 \). Since \( x_1, x_2 \) were arbitrary, \( f \) is injective. This proves the theorem.
:::

The proof of \( (\Rightarrow) \) is direct: it proves \( x_1 = x_2 \) by pushing the one-point sets through the hypothesis, without supposing \( x_1 \ne x_2 \). Read contrapositively, the same sets give the witness of failure: whenever \( f(x_1) = f(x_2) \) with \( x_1 \ne x_2 \), the sets \( \{x_1\} \) and \( \{x_2\} \) have \( f(\{x_1\} \cap \{x_2\}) = f(\emptyset) = \emptyset \) while \( f(\{x_1\}) \cap f(\{x_2\}) = \{f(x_1)\} \). For the squaring map, \( x_1 = -1 \) and \( x_2 = 1 \) is such a pair, and the intervals \( [-1, 0] \) and \( [0, 1] \) of the opening are a larger failure of the same kind.

Compare with @exm-image-two-witnesses. The false proof and the true one begin identically. The false one reuses a name and thereby assumes \( a = b \); the true one keeps two names and **proves** \( a = b \), from injectivity, on the one line where the hypothesis is used. That line is the whole difference between a theorem and a false statement.

## There and back

What happens when we push a set forwards and pull it back, or the other way round? Part (d) of @exm-images-of-square and the quick check after it gave one answer each for the squaring map: \( f^{-1}(f([0, 1])) = [-1, 1] \) is bigger than \( [0, 1] \), and \( f(f^{-1}([-1, 1])) = [0, 1] \) is smaller than \( [-1, 1] \). In general, the round trip through \( Y \) can only grow a set, and the round trip through \( X \) can only shrink one.

::: {#prp-image-preimage}
[Image and Preimage Round Trips]

Let \( f \colon X \to Y \) be a function.

::: {.enumerate options="label=(\alph*)"}
1. \( A \subseteq f^{-1}(f(A)) \) for every \( A \subseteq X \). Equality holds for all \( A \subseteq X \) if and only if \( f \) is injective.
2. \( f(f^{-1}(B)) = B \cap f(X) \) for every \( B \subseteq Y \); in particular \( f(f^{-1}(B)) \subseteq B \). Equality \( f(f^{-1}(B)) = B \) holds for all \( B \subseteq Y \) if and only if \( f \) is surjective.
:::
:::

::: {.idea}
For (a), a point \( a \in A \) is sent into \( f(A) \), with itself as witness, so it lies in the preimage. A point \( x \) of the preimage has \( f(x) = f(a) \) for some \( a \in A \), and it lies in \( A \) when \( x = a \): that is injectivity again. For (b), a point of \( f(f^{-1}(B)) \) is \( f(x) \) with \( f(x) \in B \): so it lies in \( B \), and it is a value of \( f \). Those two conditions are all there is to it.
:::

::: {.proof}
(a) Let \( A \subseteq X \) and \( a \in A \). Then \( a \in X \), and \( f(a) \in f(A) \), with witness \( a \). So \( a \in f^{-1}(f(A)) \) by @def-preimage. This proves \( A \subseteq f^{-1}(f(A)) \).

\( (\Leftarrow) \) Suppose \( f \) is injective, and let \( x \in f^{-1}(f(A)) \). Then \( x \in X \) and \( f(x) \in f(A) \), so there is \( a \in A \) with \( f(a) = f(x) \); name it \( a \) \( [\rulename{\exists E}] \). Since \( f \) is injective (@def-injective), \( a = x \), so \( x \in A \). With the inclusion already proved, \( A = f^{-1}(f(A)) \) by @prp-subset-antisymmetric.

\( (\Rightarrow) \) Suppose \( A = f^{-1}(f(A)) \) for every \( A \subseteq X \). Let \( x_1, x_2 \in X \) with \( f(x_1) = f(x_2) \). Then \( f(x_2) = f(x_1) \in f(\{x_1\}) \), with witness \( x_1 \), so \( x_2 \in f^{-1}(f(\{x_1\})) \) by @def-preimage. The hypothesis with \( A = \{x_1\} \), a subset of \( X \) because \( x_1 \in X \), gives \( f^{-1}(f(\{x_1\})) = \{x_1\} \), so \( x_2 \in \{x_1\} \). Hence \( x_2 = x_1 \), and \( f \) is injective.

(b) Let \( B \subseteq Y \). \( (\subseteq) \) Let \( y \in f(f^{-1}(B)) \). There is \( x \in f^{-1}(B) \) with \( f(x) = y \); name it \( x \). Then \( x \in X \) and \( f(x) \in B \), so \( y \in B \); and \( y \in f(X) \), with witness \( x \). \( (\supseteq) \) Let \( y \in B \cap f(X) \). Since \( y \in f(X) \), there is \( x \in X \) with \( f(x) = y \); name it \( x \). Then \( f(x) = y \in B \), so \( x \in f^{-1}(B) \), and \( y \in f(f^{-1}(B)) \), with witness \( x \). This proves \( f(f^{-1}(B)) = B \cap f(X) \), and \( B \cap f(X) \subseteq B \).

For the last statement: if \( f \) is surjective (@def-surjective), every \( y \in Y \) lies in \( f(X) \); since \( f(X) \subseteq Y \) by @def-image, \( f(X) = Y \) by @prp-subset-antisymmetric, and \( B \cap f(X) = B \cap Y = B \) for every \( B \subseteq Y \), because \( B \subseteq Y \). Conversely, if \( f(f^{-1}(B)) = B \) for every \( B \subseteq Y \), take \( B = Y \): since \( f^{-1}(Y) = X \), this says \( f(X) = Y \), so every \( y \in Y \) is \( f(x) \) for some \( x \in X \) (@def-image), and \( f \) is surjective (@def-surjective). This proves the proposition.
:::

So the two round trips measure the two failures of Section 6.4. Pushing forwards and pulling back adds to \( A \) the points that share a value with a point of \( A \): nothing is added, for every \( A \), exactly when \( f \) is injective. Pulling back and pushing forwards removes from \( B \) the points that are never hit: nothing is removed, for every \( B \), exactly when \( f \) is surjective.

## Two readings of the inverse symbol

::: {.remark}
The symbol \( f^{-1} \) now has two uses. For **every** function \( f \colon X \to Y \) and every \( B \subseteq Y \), \( f^{-1}(B) \) is the preimage of @def-preimage. For a **bijection** \( f \), \( f^{-1} \colon Y \to X \) is also the inverse function of @def-inverse-function, and then \( f^{-1}(B) \) could also be read as the image of \( B \) under that function. The two readings give the same set. Write \( g \) for the inverse function; both sets are subsets of \( X \). If \( x = g(b) \) with \( b \in B \), then \( f(x) = f(g(b)) = b \in B \), since \( f \circ g = \id_Y \), so \( x \) lies in the preimage. If \( x \in X \) and \( f(x) \in B \), then \( x = g(f(x)) \in g(B) \), since \( g \circ f = \id_X \). So the two readings name the same set, and the notation is never ambiguous. When \( f \) is not a bijection only the first reading exists.
:::

For example, \( a(x) = 3x - 2 \) on \( \nR \) is a bijection with inverse \( a^{-1}(y) = (y + 2)/3 \) (Section 6.5). The preimage \( a^{-1}([1, 4]) \) is \( \{ x \in \nR : 1 \le 3x - 2 \le 4 \} = [1, 2] \), and the image of \( [1, 4] \) under the inverse function is \( \{ (y + 2)/3 : y \in [1, 4] \} = [1, 2] \) as well.

## Exercises

### A. Check your understanding

::: {#exr-images-and-preimages-a1}
[A1]

Parts (a)–(d) are about @thm-preimage-operations and its proof.

::: {.enumerate options="label=(\alph*)"}
1. Suppose we tried to prove the image version of law (b), \( f(\bigcap_{i \in I} A_i) = \bigcap_{i \in I} f(A_i) \), by the same kind of chain. At which step would a witness have to be named, and why does the preimage version need none?
2. Run law (b) on \( f(x) = x^2 \) on \( \nR \), with \( I = \{1, 2\} \), \( B_1 = [0, 4] \), and \( B_2 = [1, 9] \): compute both sides.
3. What are both sides of law (b) when \( I = \emptyset \)?
4. State law (c) in symbols, for \( f \colon X \to Y \) and \( B \subseteq Y \).
5. True or false, with a reason: for every \( A \subseteq X \), \( f(X \cap A) = f(A) \).
:::
:::

::: {.solution}
(a) At the step that unwinds \( y \in \bigcap_i f(A_i) \) into "for every \( i \in I \), \( y \in f(A_i) \)", and then each \( y \in f(A_i) \) into "there is \( a_i \in A_i \) with \( f(a_i) = y \)". The witnesses \( a_i \) may differ from one \( i \) to another, and the left side needs **one** point in every \( A_i \). In the preimage version, the corresponding step is "for every \( i \), \( f(x) \in B_i \)", a statement about the single point \( f(x) \) with no "there exists" in it, so nothing needs naming.

(b) \( B_1 \cap B_2 = [1, 4] \), so the left side is \( f^{-1}([1, 4]) = [-2, -1] \cup [1, 2] \) (@exm-images-of-square (b)). On the right, \( f^{-1}([0, 4]) = [-2, 2] \) and \( f^{-1}([1, 9]) = [-3, -1] \cup [1, 3] \), whose intersection is \( [-2, -1] \cup [1, 2] \). The two sides agree.

(c) Both are \( X \). The left side is \( f^{-1}(Y) = X \), since the empty intersection in \( Y \) is \( Y \); the right side is the empty intersection in \( X \), which is \( X \).

(d) \( f^{-1}(Y \setminus B) = X \setminus f^{-1}(B) \): a point of \( X \) is sent outside \( B \) exactly when it is not in the preimage of \( B \).

(e) True. Since \( A \subseteq X \), \( X \cap A = A \) (each element of \( A \) lies in \( X \)), so the two sides are the image of the same set.
:::

### B. Practice

::: {#exr-images-and-preimages-b1}
[B1: Computing images and preimages]

Compute each set, and prove each equality by two inclusions or by a chain of equivalences.

::: {.enumerate options="label=(\alph*)"}
1. For \( d \colon \nN \times \nN \to \nZ \), \( d(m, n) = m - n \): the image \( d(\{ (m, n) \in \nN \times \nN : m > n \}) \) and the preimage \( d^{-1}(\{0\}) \).
2. For \( \ind_{[0, 1]} \colon \nR \to \{0, 1\} \): the preimages of \( \{1\} \) and \( \{0\} \), and the image of \( [2, 3] \).
3. For \( g \colon \nR \to \nR \), \( g(x) = x^2 - 2x \): the image \( g([0, 3]) \) and the preimages \( g^{-1}(\{0\}) \) and \( g^{-1}([-1, 0]) \).
:::
:::

::: {.solution}
(a) The image is \( \nZ_{>0} \). \( (\subseteq) \) If \( y = m - n \) with \( m > n \), then \( y \) is an integer and \( y > 0 \), so \( y \in \nZ_{>0} \). \( (\supseteq) \) Let \( k \in \nZ_{>0} \). The pair \( (k, 0) \) lies in \( \nN \times \nN \), has \( k > 0 \), and \( d(k, 0) = k \); so \( k \) is in the image. The preimage is \( d^{-1}(\{0\}) = \{ (m, n) \in \nN \times \nN : m = n \} = \{ (n, n) : n \in \nN \} \), since \( m - n = 0 \) exactly when \( m = n \).

(b) By the definition of the indicator (Section 6.4), \( \ind_{[0, 1]}(x) = 1 \) for \( x \in [0, 1] \) and \( 0 \) otherwise. So \( \ind_{[0, 1]}^{-1}(\{1\}) = [0, 1] \) and \( \ind_{[0, 1]}^{-1}(\{0\}) = \nR \setminus [0, 1] \), each a chain of one equivalence. The image \( \ind_{[0, 1]}([2, 3]) = \{0\} \): every point of \( [2, 3] \) lies outside \( [0, 1] \) and is sent to \( 0 \), and \( 0 \) is hit, for instance by \( 2 \).

(c) Write \( g(x) = (x - 1)^2 - 1 \). The image is \( g([0, 3]) = [-1, 3] \). \( (\subseteq) \) If \( 0 \le a \le 3 \), then \( -1 \le a - 1 \le 2 \), so \( \abs{a - 1} \le 2 \), and hence \( 0 \le (a - 1)^2 = \abs{a - 1}^2 \le 4 \) by @thm-squares-order applied to \( \abs{a - 1} \) and \( 2 \), and \( -1 \le g(a) \le 3 \). \( (\supseteq) \) Let \( -1 \le y \le 3 \), and take \( a \coloneqq 1 + \sqrt{y + 1} \). Then \( 0 \le \sqrt{y + 1} \le 2 \), so \( a \in [1, 3] \subseteq [0, 3] \), and \( g(a) = (y + 1) - 1 = y \). For the preimages: \( g(x) = 0 \iff x(x - 2) = 0 \iff x \in \{0, 2\} \), so \( g^{-1}(\{0\}) = \{0, 2\} \); and \( -1 \le g(x) \le 0 \iff 0 \le (x - 1)^2 \le 1 \iff \abs{x - 1} \le 1 \iff x \in [0, 2] \), so \( g^{-1}([-1, 0]) = [0, 2] \).
:::

::: {#exr-images-and-preimages-b2}
[B2: Two laws, element by element]

Let \( f \colon X \to Y \) be a function. Prove each law directly, by two inclusions or by a chain of equivalences at a point, tagging each step that names or exhibits a witness with \( [\rulename{\exists E}] \) or \( [\rulename{\exists I}] \).

::: {.enumerate options="label=(\alph*)"}
1. \( f(A \cup B) = f(A) \cup f(B) \) for \( A, B \subseteq X \). (This is a case of @thm-image-union; prove it without citing it.)
2. \( f^{-1}(C \setminus D) = f^{-1}(C) \setminus f^{-1}(D) \) for \( C, D \subseteq Y \). (This is @thm-preimage-operations (d); prove it without citing it.) Which steps, if any, need a tag?
:::
:::

::: {.solution}
(a) \( (\subseteq) \) Let \( y \in f(A \cup B) \). There is \( c \in A \cup B \) with \( f(c) = y \); name it \( c \) \( [\rulename{\exists E}] \). By @def-set-operations, \( c \in A \) or \( c \in B \). *Case 1:* \( c \in A \). Then \( y \in f(A) \), with witness \( c \) \( [\rulename{\exists I}] \), so \( y \in f(A) \cup f(B) \). *Case 2:* \( c \in B \). Then \( y \in f(B) \), with witness \( c \) \( [\rulename{\exists I}] \), so \( y \in f(A) \cup f(B) \). \( (\supseteq) \) Let \( y \in f(A) \cup f(B) \). *Case 1:* \( y \in f(A) \). There is \( a \in A \) with \( f(a) = y \); name it \( a \) \( [\rulename{\exists E}] \). Then \( a \in A \cup B \), so \( y \in f(A \cup B) \), with witness \( a \) \( [\rulename{\exists I}] \). *Case 2:* \( y \in f(B) \) is the same with \( B \) in place of \( A \). In either case \( y \in f(A \cup B) \).

(b) Both sides are subsets of \( X \). For \( x \in X \): \( x \in f^{-1}(C \setminus D) \) if and only if \( f(x) \in C \setminus D \) (@def-preimage) if and only if \( f(x) \in C \) and \( f(x) \notin D \) (@def-set-operations) if and only if \( x \in f^{-1}(C) \) and \( x \notin f^{-1}(D) \) (@def-preimage, and @exm-iff-negations for the second clause) if and only if \( x \in f^{-1}(C) \setminus f^{-1}(D) \). No step names or exhibits a witness, so no step carries a tag: this is the difference between (a) and (b).
:::

::: {#exr-images-and-preimages-b3}
[B3: The two readings of the inverse]

Let \( f \colon X \to Y \) be a bijection, with inverse function \( f^{-1} \colon Y \to X \), and let \( B \subseteq Y \). Prove that the image of \( B \) under the function \( f^{-1} \) equals the preimage of \( B \) under \( f \). To keep the readings apart, write \( g \coloneqq f^{-1} \) for the inverse function, and prove \( g(B) = \{ x \in X : f(x) \in B \} \). The remark in "Two readings of the inverse symbol" gives the argument in brief; write it out as two inclusions, tagging each step that names or exhibits a witness with \( [\rulename{\exists E}] \) or \( [\rulename{\exists I}] \).
:::

::: {.solution}
\( (\subseteq) \) Let \( x \in g(B) \). There is \( b \in B \) with \( g(b) = x \); name it \( b \) \( [\rulename{\exists E}] \). Then \( x \in X \), and \( f(x) = f(g(b)) = b \in B \), since \( f \circ g = \id_Y \). So \( x \) lies in the preimage.

\( (\supseteq) \) Let \( x \in X \) with \( f(x) \in B \). Then \( g(f(x)) = x \), since \( g \circ f = \id_X \). So \( x \in g(B) \), with witness \( f(x) \in B \) \( [\rulename{\exists I}] \).

Hence \( g(B) \) equals the preimage of \( B \) under \( f \): for a bijection, the two readings of \( f^{-1}(B) \) name the same set. Both equations of @def-inverse-function were used, one in each inclusion.
:::

### C. Going deeper

::: {#exr-images-and-preimages-c1}
[C1: Images and differences]

Let \( f \colon X \to Y \) be a function and \( A, B \subseteq X \).

::: {.enumerate options="label=(\alph*)"}
1. Here are the first lines of a proof that \( f(A) \setminus f(B) \subseteq f(A \setminus B) \). *Name the move, then complete it.*

    > Let \( y \in f(A) \setminus f(B) \). Then \( y \in f(A) \), so there is \( a \in A \) with \( f(a) = y \); name it \( a \) \( [\rulename{\exists E}] \). Also \( y \notin f(B) \).
2. Show that the reverse inclusion can fail, with \( f(x) = x^2 \) on \( \nR \), \( A = \{-1, 1\} \), and \( B = \{1\} \).
3. Prove that \( f(A \setminus B) = f(A) \setminus f(B) \) holds for all \( A, B \subseteq X \) if and only if \( f \) is injective.
:::
:::

::: {.solution}
(a) The move is **element-chasing**: unwind the membership of the hypothesis into its definition, and rewind into the definition of the goal. The goal is \( y \in f(A \setminus B) \), which needs a witness in \( A \setminus B \), and the natural candidate is the \( a \) already named. We know \( a \in A \); we need \( a \notin B \).

Suppose \( a \in B \). Then \( y = f(a) \in f(B) \), with witness \( a \) \( [\rulename{\exists I}] \), which contradicts \( y \notin f(B) \). Hence \( a \notin B \) \( [\rulename{\neg I}] \). So \( a \in A \setminus B \) and \( f(a) = y \), which gives \( y \in f(A \setminus B) \), with witness \( a \) \( [\rulename{\exists I}] \).

(b) \( A \setminus B = \{-1\} \), so \( f(A \setminus B) = \{1\} \). But \( f(A) = \{1\} = f(B) \), so \( f(A) \setminus f(B) = \emptyset \). The point \( 1 \) lies in \( f(A \setminus B) \) and not in \( f(A) \setminus f(B) \).

(c) \( (\Leftarrow) \) Suppose \( f \) is injective. By (a) it suffices to show \( f(A \setminus B) \subseteq f(A) \setminus f(B) \). Let \( y \in f(A \setminus B) \), and name \( a \in A \setminus B \) with \( f(a) = y \). Then \( y \in f(A) \), with witness \( a \). Suppose \( y \in f(B) \), and name \( b \in B \) with \( f(b) = y \). Then \( f(a) = f(b) \), so \( a = b \) by injectivity, and \( a \in B \), contradicting \( a \in A \setminus B \). Hence \( y \notin f(B) \), and \( y \in f(A) \setminus f(B) \).

\( (\Rightarrow) \) Suppose equality holds for all \( A, B \subseteq X \). Let \( x_1, x_2 \in X \) with \( f(x_1) = f(x_2) \), and take \( A \coloneqq \{x_1\} \), \( B \coloneqq \{x_2\} \). Then \( f(A) = \{f(x_1)\} = f(B) \), so \( f(A \setminus B) = f(A) \setminus f(B) = \emptyset \). Suppose \( x_1 \ne x_2 \). Then \( x_1 \in A \setminus B \), so \( f(x_1) \in f(A \setminus B) = \emptyset \), which is impossible. Hence \( x_1 = x_2 \), by \( \rulename{RAA} \) (@def-rule-raa), and \( f \) is injective.

**Marking scheme.** (10 points)

- 3: (a) shows \( a \notin B \) by deriving \( y \in f(B) \) from \( a \in B \), and concludes \( y \in f(A \setminus B) \) with the witness \( a \).
- 2: (b) computes both sides for the given data.
- 3: (c) \( (\Leftarrow) \) names two witnesses, \( a \in A \setminus B \) and \( b \in B \), and uses injectivity to identify them.
- 2: (c) \( (\Rightarrow) \) applies the hypothesis to one-point sets (or any sets that separate \( x_1 \) from \( x_2 \)) and concludes \( x_1 = x_2 \).

Fatal errors (0 for the step): using one name for the witnesses of \( y \in f(A \setminus B) \) and \( y \in f(B) \) (entry (N4) of Chapter 5's catalogue); in \( (\Rightarrow) \), assuming injectivity to compute \( f(A \setminus B) \).
:::

::: {#exr-images-and-preimages-c2}
[C2: Find the error]

A student proves the following claim: *if \( f \colon X \to Y \) is injective and \( A \subseteq X \), then \( f^{-1}(f(A)) \subseteq A \).*

> (1) Let \( x \in f^{-1}(f(A)) \). (2) By the definition of preimage, \( x \in X \) and \( f(x) \in f(A) \). (3) Since \( f(x) \in f(A) \), we have \( x \in A \). (4) Since \( x \) was arbitrary, \( f^{-1}(f(A)) \subseteq A \).

::: {.enumerate options="label=(\alph*)"}
1. Is the claim true?
2. Which line fails, and which rule does it skip?
3. Give a counterexample to the failing step, and repair the proof.
:::
:::

::: {.solution}
(a) The claim is true: it is the \( (\Leftarrow) \) half of @prp-image-preimage (a).

(b) Line (3) fails. The statement \( f(x) \in f(A) \) says only that \( f(a) = f(x) \) for **some** \( a \in A \) (@def-image). To use it, the proof must name that witness by \( \exists \)E, with a fresh name. Line (3) skips the \( \exists \)E and silently takes the witness to be \( x \) itself. The name \( x \) is already in use (line (1) introduced it), so the step breaks the fresh-name condition of \( \exists \)E (Chapter 4, Section 4.6), the condition behind entry (N4) of the catalogue of Chapter 5. The tell is that injectivity, a hypothesis, is never used: an argument that ignores a necessary hypothesis cannot be right.

(c) A counterexample to the step "\( f(x) \in f(A) \), so \( x \in A \)" needs a non-injective function, since for injective ones the conclusion of the step is true. Take \( f(x) = x^2 \) on \( \nR \), \( A = \{1\} \), and \( x = -1 \). Then \( f(x) = 1 \in f(A) \), but \( x \notin A \).

Repair: replace (3) by "Since \( f(x) \in f(A) \), there is \( a \in A \) with \( f(a) = f(x) \); name it \( a \). Since \( f \) is injective, \( a = x \). Hence \( x \in A \)."
:::

::: {#exr-images-and-preimages-c3}
[C3: Exit check: preimages]

::: {.enumerate options="label=(\alph*)"}
1. Let \( f \colon X \to Y \) be a function and \( (B_i)_{i \in I} \) a family of subsets of \( Y \). Prove that \( f^{-1}(\bigcap_{i \in I} B_i) = \bigcap_{i \in I} f^{-1}(B_i) \), the intersections taken in \( Y \) and in \( X \).
2. Give a function \( f \) and sets \( A, B \) with \( f(A \cap B) \ne f(A) \cap f(B) \), computing both sides.
:::
:::

::: {.solution}
(a) We prove two inclusions.

\( (\subseteq) \) Let \( x \in f^{-1}(\bigcap_{i \in I} B_i) \). By @def-preimage, \( x \in X \) and \( f(x) \in \bigcap_{i \in I} B_i \). By @def-family-union-intersection, \( f(x) \in B_i \) for every \( i \in I \). Let \( i \in I \). Then \( f(x) \in B_i \) and \( x \in X \), so \( x \in f^{-1}(B_i) \). Since \( i \) was arbitrary, \( x \) lies in every \( f^{-1}(B_i) \), and since \( x \in X \), \( x \in \bigcap_{i \in I} f^{-1}(B_i) \).

\( (\supseteq) \) Let \( x \in \bigcap_{i \in I} f^{-1}(B_i) \). Then \( x \in X \) and \( x \in f^{-1}(B_i) \) for every \( i \in I \). Let \( i \in I \). Then \( f(x) \in B_i \) by @def-preimage. Since \( i \) was arbitrary, and \( f(x) \in Y \), \( f(x) \in \bigcap_{i \in I} B_i \). So \( x \in f^{-1}(\bigcap_{i \in I} B_i) \).

If \( I = \emptyset \), both sides are \( X \), and the argument above covers this case: the "for every \( i \)" statements hold vacuously.

(b) Let \( f \colon \{1, 2\} \to \{0\} \) be the constant function, \( A = \{1\} \), \( B = \{2\} \). Then \( A \cap B = \emptyset \), so \( f(A \cap B) = \emptyset \). But \( f(A) = \{0\} = f(B) \), so \( f(A) \cap f(B) = \{0\} \ne \emptyset \). (The squaring map with \( A = [-1, 0] \), \( B = [0, 1] \) is another answer: \( \{0\} \) against \( [0, 1] \).)

**Marking scheme.** (10 points)

- 1: announces two inclusions (or a chain of equivalences at a point \( x \in X \)).
- 3: \( (\subseteq) \) unwinds \( x \in f^{-1}(\bigcap B_i) \) to "\( f(x) \in B_i \) for every \( i \)", then rewinds to \( x \in f^{-1}(B_i) \) for an **arbitrary** \( i \).
- 3: \( (\supseteq) \) the reverse chain, with \( i \) arbitrary.
- 1: the ambient sets are named (\( x \in X \), \( f(x) \in Y \)) or the case \( I = \emptyset \) is handled.
- 2: a correct example, with both sides computed.

A single chain of equivalences, each step justified, earns the first seven points. Fatal errors (0 for the step): fixing one \( i \) and concluding for all \( i \) (entry (N1) of Chapter 5's catalogue); stating the example's two sides without checking an element that lies in one and not the other.
:::

### R. Review

::: {#exr-images-and-preimages-r1}
[R1]

Here is a derivation of "if \( A \subseteq B \), then \( \powerset{A} \subseteq \powerset{B} \)". The steps "by def." unwind or rewind @def-subset and @def-power-set.

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {A \subseteq B}
  \have {2} {\forall x (x \in A \to x \in B)} \by{def.}{1}
  \open[S_0]
  \open
  \hypo {3} {S_0 \in \powerset{A}}
  \have {4} {S_0 \subseteq A} \by{def.}{3}
  \have {5} {\forall x (x \in S_0 \to x \in A)} \by{def.}{4}
  \open[x_0]
  \open
  \hypo {6} {x_0 \in S_0}
  \have {7} {x_0 \in S_0 \to x_0 \in A} \Ae{5}
  \have {8} {x_0 \in A} \ie{7,6}
  \have {9} {x_0 \in A \to x_0 \in B} \Ae{2}
  \have {10} {x_0 \in B} \ie{9,8}
  \close
  \have {11} {x_0 \in S_0 \to x_0 \in B} \ii{6-10}
  \close
  \have {12} {\forall x (x \in S_0 \to x \in B)} \Ai{6-11}
  \have {13} {S_0 \subseteq B} \by{def.}{12}
  \have {14} {S_0 \in \powerset{B}} \by{def.}{13}
  \close
  \have {15} {S_0 \in \powerset{A} \to S_0 \in \powerset{B}} \ii{3-14}
  \close
  \have {16} {\forall S (S \in \powerset{A} \to S \in \powerset{B})} \Ai{3-15}
  \have {17} {\powerset{A} \subseteq \powerset{B}} \by{def.}{16}
  \close
  \have {18} {A \subseteq B \to \powerset{A} \subseteq \powerset{B}} \ii{1-17}
\end{nd}$
\end{center}
```

Write the proof as plain prose, the way a mathematician would. Then say which sentence of your proof carries each of the five boxes.
:::

::: {.solution}
*Proof.* Suppose \( A \subseteq B \). Let \( S \in \powerset{A} \), so \( S \subseteq A \). Let \( x \in S \). Then \( x \in A \), since \( S \subseteq A \), and so \( x \in B \), since \( A \subseteq B \). Hence \( S \subseteq B \), that is, \( S \in \powerset{B} \). This proves \( \powerset{A} \subseteq \powerset{B} \).

*The boxes.* "Suppose \( A \subseteq B \)" opens the \( \rulename{{\to}I} \) box \( \lines{1}{17} \); its closing line 18 is the silent frame of the whole proof. "Let \( S \in \powerset{A} \)" opens two boxes at once: the \( \rulename{\forall I} \) box for \( S_0 \) and the \( \rulename{{\to}I} \) box \( \lines{3}{14} \) inside it. "Let \( x \in S \)" likewise opens the \( \rulename{\forall I} \) box for \( x_0 \) and the \( \rulename{{\to}I} \) box \( \lines{6}{10} \). "Hence \( S \subseteq B \)" closes the two inner boxes (lines 11 and 12) and rewinds the definition (line 13). "This proves \( \powerset{A} \subseteq \powerset{B} \)" closes the \( S \) boxes (lines 15, 16) and rewinds (line 17).

This is the passage from level 0 to level 3 of Chapter 5 (Section 5.3): each "let" carries a \( \rulename{\forall I} \) box together with the \( \rulename{{\to}I} \) box of a subset statement, the \( \rulename{\forall E} \) and \( \rulename{{\to}E} \) lines 7–10 become the two "since" clauses, and the unwinding lines 2, 4, 5 and 13, 14, 17 go silent or become a "that is".
:::

::: {#exr-images-and-preimages-r2}
[R2]

Decide whether \( A \setminus (B \setminus C) = (A \setminus B) \setminus C \) for all sets \( A, B, C \), by a table of the eight possible memberships of a point \( x \) in \( A \), \( B \), \( C \). If the two sides can differ, turn a row where they differ into a counterexample.
:::

::: {.solution}
Write \( P \), \( Q \), \( R \) for the statements \( x \in A \), \( x \in B \), \( x \in C \). By @def-set-operations, \( x \in A \setminus (B \setminus C) \) is \( P \wedge \neg(Q \wedge \neg R) \), and \( x \in (A \setminus B) \setminus C \) is \( (P \wedge \neg Q) \wedge \neg R \). The table:
\[
\begin{array}{ccc|cc}
P & Q & R & P \wedge \neg (Q \wedge \neg R) & (P \wedge \neg Q) \wedge \neg R \\
\hline
\mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{F} \\
\mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} \\
\mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} \\
\mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} \\
\mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} \\
\end{array}
\]
The columns differ in the first and third rows. Take the first row: put the point \( 1 \) in exactly the sets whose statement is true, all three, so \( A = B = C = \{1\} \). Then \( B \setminus C = \emptyset \), so \( A \setminus (B \setminus C) = \{1\} \); and \( A \setminus B = \emptyset \), so \( (A \setminus B) \setminus C = \emptyset \). The two sides differ, so the identity is false. (The third row gives \( A = C = \{1\} \), \( B = \emptyset \), with the same two answers.)

Why a table suffices: each side's membership condition is a formula in \( P \), \( Q \), \( R \), and a row with the two columns different gives sets directly, which are then checked by computing both sides, as above. The truth tables of Chapter 3 add one more thing: by @cor-refuting-row, the first row shows that the sequent \( P \wedge \neg(Q \wedge \neg R) \vdash (P \wedge \neg Q) \wedge \neg R \) is not derivable, so the propositional rules cannot carry a point of the left side into the right side.
:::

::: {#exr-images-and-preimages-r3}
[R3]

Derive \( (P \wedge \neg Q) \to R \vdash P \to (Q \vee R) \). Then read the derivation as a proof that for sets \( A, B, C \), if \( A \setminus B \subseteq C \), then \( A \subseteq B \cup C \). Which step is classical?
:::

::: {.solution}
The goal is an implication, so open a box on \( P \) with goal \( Q \vee R \). The premise can fire only on \( P \wedge \neg Q \), which needs \( \neg Q \), and nothing gives \( \neg Q \) outright. So split on \( Q \vee \neg Q \), by excluded middle (@prp-excluded-middle): in the case \( Q \) the goal is immediate, and in the case \( \neg Q \) the premise gives \( R \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge \neg Q) \to R}
  \open
  \hypo {2} {P}
  \have {3} {Q \vee \neg Q} \lem{}
  \open
  \hypo {4} {Q}
  \have {5} {Q \vee R} \oi{4}
  \close
  \open
  \hypo {6} {\neg Q}
  \have {7} {P \wedge \neg Q} \ai{2,6}
  \have {8} {R} \ie{1,7}
  \have {9} {Q \vee R} \oi{8}
  \close
  \have {10} {Q \vee R} \oe{3,4-5,6-9}
  \close
  \have {11} {P \to (Q \vee R)} \ii{2-10}
\end{nd}$
\end{center}
```

*As sets.* Suppose \( A \setminus B \subseteq C \), and let \( x \in A \). Take \( P \), \( Q \), \( R \) to be \( x \in A \), \( x \in B \), \( x \in C \). By @def-subset and @def-set-operations, the hypothesis at this \( x \) is \( (P \wedge \neg Q) \to R \), and the goal \( x \in B \cup C \) is \( Q \vee R \). The derivation, used as a derived rule (@def-derived-rule), gives \( P \to (Q \vee R) \), and with \( P \) it gives \( x \in B \cup C \). In prose: either \( x \in B \), and then \( x \in B \cup C \); or \( x \notin B \), and then \( x \in A \setminus B \subseteq C \), so \( x \in C \subseteq B \cup C \). Since \( x \) was arbitrary, \( A \subseteq B \cup C \).

The classical step is line 3, the case split "\( x \in B \) or \( x \notin B \)" by excluded middle, which is derived with \( \rulename{RAA} \) (@def-rule-raa).
:::

::: {#exr-images-and-preimages-r4}
[R4]

Show that there is no set that contains every singleton \( \{x\} \) as an element.
:::

::: {.solution}
Suppose \( S \) were such a set. Let \( T \coloneqq \{ s \in S : s \text{ is a singleton} \} \), a set by specification (@def-set-builder); its elements are sets, since \( S \) may also contain numbers, and those are excluded. Consider the union \( \bigcup T \) of the sets in \( T \) (@def-family-union-intersection, the form \( \bigcup \sS \) for a set \( \sS \) whose elements are sets). For every set \( x \), the singleton \( \{x\} \) lies in \( S \), hence in \( T \), and \( x \in \{x\} \); so \( x \in \bigcup T \). Thus \( \bigcup T \) is a set of which every set is an element, and @thm-russell says there is no such set. This contradiction shows that no such \( S \) exists.

*The tool, and the look-alike.* The tool is Russell's theorem, @thm-russell, applied not to \( S \) but to \( \bigcup T \). Applied to \( S \) directly, it says only that \( \{ z \in S : z \notin z \} \notin S \), and that does not contradict anything: \( S \) was supposed to contain singletons, not that set. The move that makes it work is the union, which turns "contains the singleton of every set" into "contains every set". A direct diagonal construction inside \( S \) also works, but it repeats the proof of @thm-russell instead of using it.
:::

<!-- dependency ledger
def-image (claim): (opening question) squares of points of [-1, 0] and [0, 1] fill [0, 1]; preimages of [0, 1] and [1, 4] under squaring | school facts (Part 0 convention; square roots proved in Chapter 11); worked in exm-images-of-square
def-image (claim): exists-E with a fresh name; exists-I | ch04 (promised): def-rules-existential, def-rule-existential-introduction (prose pointers, Sections 4.5-4.6)
def-image (claim): f(X) is the range of Section 6.4 | def-function (Section 6.4, prose)
exm-images-finite (example): a set lists a repeated element once | def-set-equality (Section 6.1, prose)
def-preimage (claim): open sets and continuity | ch24 (prose pointer; nothing depends on it)
exm-images-of-square (example): x^2 >= 0; square roots of non-negative reals; x^2 = |x|^2; sign cases for |x| | school facts (Part 0 convention); square roots proved in Chapter 11
exm-images-of-square (example): for s, t >= 0, s <= t iff s^2 <= t^2 (also in exr-images-and-preimages-b1 (c)) | thm-squares-order (ch02, cited)
exm-sets-of-numbers-as-images (example): -A, cA, A + B as Chapter 11 writes them | Chapter 11 (Sections 11.3, 11.4; later chapter, prose pointer)
exm-sets-of-numbers-as-images (example): p in A x B iff p = (a, b) with a in A, b in B | def-cartesian-product (cited)
thm-preimage-operations (proof): two subsets of X are equal iff they have the same elements among points of X | inline, from def-set-equality (cited)
thm-preimage-operations (proof): chaining equivalences (transitivity of iff) | prp-provable-equivalence-basics (ch02), used silently
thm-preimage-operations (proof): replacing equivalent statements under "for some i" / "for every i" | inline sentence in the proof (exists-E then exists-I; forall-E then forall-I); ch04 (promised) for the rules
thm-preimage-operations (proof): negating both sides of an iff | exm-iff-negations (cited)
prp-preimage-composition (claim): composites of continuous maps | ch24 (prose pointer)
prp-preimage-composition (claim): (closing remark) (g o f)^{-1} = f^{-1} o g^{-1} for bijections, as a comparison | exr-inverses-b2 (proved in its solution); no proof, idea or claim of the text rests on it
thm-image-union (proof): exists-E side condition (conclusion free of the witness) | ch04 (promised): def-rules-existential (prose pointer, Section 4.6)
exm-image-two-witnesses (solution): fresh-name condition; catalogue entry (N4) | ch04 (promised) Section 4.6; ch05 (promised): exm-not-allowed-catalogue (prose pointer, Section 5.6)
thm-image-intersection (proof): c in {x_1} gives c = x_1 | def-set-builder / listing (Section 6.1)
prp-image-preimage (proof): A = f^{-1}(f(A)) from two inclusions | prp-subset-antisymmetric (cited)
prp-image-preimage (proof): x_2 in {x_1} gives x_2 = x_1; {x_1} is a subset of X when x_1 in X | def-set-builder / listing (Section 6.1); def-subset (Section 6.1)
prp-image-preimage (proof): f^{-1}(Y) = X | def-preimage (cited), as in exm-images-finite
prp-image-preimage (proof): B cap Y = B for B subset of Y | inline, from def-subset and the definition of intersection (Section 6.2)
thm-image-intersection (proof): substituting equals (=E): a = b and b in B give a in B; c = x_1 and c = x_2 give x_1 = x_2 | def-rules-equality (Section 4.7), used silently
prp-image-preimage (proof): substituting equals (=E): a = x and a in A give x in A | def-rules-equality (Section 4.7), used silently
exr-images-and-preimages-c1 (solution): substituting equals (=E): a = b and b in B give a in B | def-rules-equality (Section 4.7), used silently
prp-image-preimage (claim): (two readings remark and example) a(x) = 3x - 2 and its inverse; interval arithmetic | exm-two-sided-inverses (Section 6.5); school facts
prp-image-preimage (claim): (two readings remark) for a bijection the preimage f^{-1}(B) equals the image of B under the inverse function | inline two-inclusion argument in the remark, from def-inverse-function (cited: g o f = id_X, f o g = id_Y); exr-images-and-preimages-b3 writes it out with tags
exr-images-and-preimages-a1 (solution): numeric preimages under squaring | school facts; exm-images-of-square
exr-images-and-preimages-b1 (solution): m > n in N gives m - n in Z_{>0}; a positive integer is in N; m - n = 0 iff m = n; (x - 1)^2 algebra; -1 <= t <= 2 gives |t| <= 2, and t^2 = |t|^2; sqrt monotone | school facts (Part 0 convention)
exr-images-and-preimages-b1 (solution): the indicator function | Section 6.4 (ind_A defined there)
exr-images-and-preimages-c1 (solution): RAA for x_1 = x_2 | def-rule-raa (cited)
exr-images-and-preimages-c2 (solution): fresh-name condition; catalogue (N4) | ch04 (promised) Section 4.6; ch05 (promised): exm-not-allowed-catalogue (prose pointer)
exr-images-and-preimages-c3 (solution): marking-scheme reference to catalogue (N1) | ch05 (promised): exm-not-allowed-catalogue (prose pointer)
exr-images-and-preimages-r1 (solution): levels of proof | ch05 (promised): def-levels-of-proof (prose pointer, Section 5.3)
exr-images-and-preimages-r1 (solution): forall-I / forall-E rules and flagged boxes | ch04 (promised): def-rules-universal (prose pointer)
exr-images-and-preimages-r4 (solution): every set x is an element of {x}; "is a singleton" is a property usable in specification | def-set-builder (Section 6.1, listing)
-->
