<!-- Parked from fd2 (fd2/authoring/design/layout-six-chapters.md §2, approved 2026-10-26). Not part of any book's src; nothing builds or scans it.
Old section: fd2 5.4 Permutations and Iteration (src/ch05-building-functions/04-permutations-and-iteration.md)
Labels: def-permutation, prp-permutations-closed, def-iterate, prp-iterate-laws, def-orbit, thm-orbits-partition, prp-orbit-cycle, exm-method-follow-the-orbit, exm-three-pile-shuffle, def-permutation-cycle, thm-permutation-cycles, cor-permutation-power-identity, prp-eventually-periodic, exm-squaring-mod-eleven, exr-permutations-and-iteration-a1, exr-permutations-and-iteration-b1, exr-permutations-and-iteration-b2, exr-permutations-and-iteration-b3, exr-permutations-and-iteration-b4, exr-permutations-and-iteration-c1, exr-permutations-and-iteration-c2, exr-permutations-and-iteration-c3, exr-permutations-and-iteration-r1, exr-permutations-and-iteration-r2, exr-permutations-and-iteration-r3, exr-permutations-and-iteration-r4
Intended home: fd5 Algebraic Preliminaries, a later revision (fd5 Chapter 3 already has def-symmetric-group, def-cycle, thm-disjoint-cycle-decomposition); no fd5 file cites these labels
-->

# Permutations and Iteration

Sections 5.1–5.3 built new functions from old ones: by cutting a domain down, by gluing pieces together, by passing to a quotient, and by combining two functions with an operation. This section does the simplest thing that can be done with a function whose codomain is its own domain: it applies the function again, and again. For a bijection, going forwards and backwards sorts the set into orbits, and on a finite set each orbit is a cycle. We prove that a bijection of a finite set, repeated often enough, gives back the identity, and we say after how many steps. Then we see what is left of this when the map is not a bijection.

## Shuffling twelve cards

Lay twelve cards in a row and number the positions \( 0, 1, \dots, 11 \). Cut the row into three piles of four: positions \( 0 \)–\( 3 \), positions \( 4 \)–\( 7 \), positions \( 8 \)–\( 11 \). Now deal them back: take the first card of each pile in turn, then the second card of each pile, and so on. The new row holds the cards from the old positions
\[
0, \ 4, \ 8, \ 1, \ 5, \ 9, \ 2, \ 6, \ 10, \ 3, \ 7, \ 11 ,
\]
in that order. So the card that was at position \( 4 \) is now at position \( 1 \), and the card that was at position \( 1 \) is now at position \( 3 \).

The card at old position \( i \) moves to the new position \( \sigma(i) \), where
\[
\sigma(i) =
\begin{cases}
3i & \text{if } 0 \le i \le 3, \\
3i - 11 & \text{if } 4 \le i \le 7, \\
3i - 22 & \text{if } 8 \le i \le 11 .
\end{cases}
\]
Check one card from each pile: card \( 2 \) lands at \( 6 \), card \( 5 \) at \( 15 - 11 = 4 \), card \( 10 \) at \( 30 - 22 = 8 \), as the row above says. The three pieces \( \{0, \dots, 3\} \), \( \{4, \dots, 7\} \), \( \{8, \dots, 11\} \) are disjoint and cover the positions, so \( \sigma \) is a gluing with nothing to check on overlaps (@exm-method-gluing).

Now shuffle again by the same rule. After two shuffles the card from position \( i \) is at \( \sigma(\sigma(i)) \). Follow card \( 1 \) through the shuffles: it goes to \( 3 \), then \( 9 \), then \( 27 - 22 = 5 \), then \( 15 - 11 = 4 \), then \( 12 - 11 = 1 \). Card \( 2 \) goes to \( 6 \), \( 7 \), \( 10 \), \( 8 \), and back to \( 2 \). Cards \( 0 \) and \( 11 \) never move. These are \( 1 + 1 + 5 + 5 = 12 \) cards, every card of the deck, and each is back in its place after five shuffles. The deck is in its starting order.

Was that luck? Three questions organize the section. Does **every** shuffle of a finite deck, repeated, bring the deck back? After how many shuffles? And what is left of the answer when the rule is not a shuffle, for instance when it sends two positions to one?

## Permutations and iterates

A shuffle sends every position to a position, sends no two positions to the same one, and fills every position. That is a bijection from the set of positions to itself.

::: {#def-permutation}
[Permutation]

Let \( X \) be a set. A **permutation** of \( X \) is a bijection \( \sigma \colon X \to X \). The set of all permutations of \( X \) is written \( S_X \); it is a subset of \( X^X \), the set of all functions \( X \to X \).
:::

For a finite set, a function \( X \to X \) can be written as a **two-line table**: the elements of \( X \) in the top row, and under each element its image. For instance,
\[
\begin{pmatrix} 1 & 2 & 3 \\ 2 & 3 & 1 \end{pmatrix}
\]
is the function on \( \{1, 2, 3\} \) with \( 1 \mapsto 2 \), \( 2 \mapsto 3 \), \( 3 \mapsto 1 \). It is a table, not a matrix: nothing is multiplied. Such a function is a permutation exactly when its bottom row lists every element of \( X \) once: "every element appears" is surjectivity, and "no element twice" is injectivity. The hook's shuffle is the table with top row \( 0, \dots, 11 \) and bottom row \( 0, 3, 6, 9, 1, 4, 7, 10, 2, 5, 8, 11 \). The two permutations of \( \{1, 2\} \) are the identity and the swap \( 1 \mapsto 2 \), \( 2 \mapsto 1 \).

Section 5.3 made composition an operation on \( X^X \) (@prp-composition-operation). The permutations are closed under it, and they keep everything that operation has.

::: {#prp-permutations-closed}
[Permutations under Composition]

Let \( X \) be a set.

::: {.enumerate options="label=(\alph*)"}
1. If \( \sigma, \tau \in S_X \), then \( \sigma \circ \tau \in S_X \).
2. \( \id_X \in S_X \).
3. If \( \sigma \in S_X \), then \( \sigma^{-1} \in S_X \), and \( \sigma \circ \sigma^{-1} = \id_X = \sigma^{-1} \circ \sigma \).
:::

Hence \( S_X \) is closed under \( \circ \), and \( \circ \) is an associative operation on \( S_X \) with identity \( \id_X \), in which every element \( \sigma \) is invertible, with inverse \( \sigma^{-1} \).
:::

::: {.proof}
(a) is @thm-composition-injective-surjective (c). (b) \( \id_X \circ \id_X = \id_X \), so \( \id_X \) is a two-sided inverse of itself, and it is bijective by @thm-bijection-iff-inverse. (c) Since \( \sigma \) is bijective, it has the inverse \( \sigma^{-1} \) with \( \sigma^{-1} \circ \sigma = \id_X \) and \( \sigma \circ \sigma^{-1} = \id_X \) (@thm-bijection-iff-inverse, @def-inverse-function). Read the other way round, the same two equations say that \( \sigma \) is a two-sided inverse of \( \sigma^{-1} \), so \( \sigma^{-1} \) is bijective by @thm-bijection-iff-inverse.

By (a), \( S_X \) is closed under \( \circ \), so \( \circ \) restricted to \( S_X \times S_X \) is an operation on \( S_X \) (@def-binary-operation). Associativity holds on all of \( X^X \) (@prp-composition-operation), so in particular on \( S_X \); \( \id_X \) lies in \( S_X \) by (b) and is an identity there; and by (c) each \( \sigma \in S_X \) has an inverse \( \sigma^{-1} \) that lies in \( S_X \).
:::

So everything Section 5.3 proved for an associative operation with an identity applies to \( S_X \). For instance, @prp-operation-inverse-rules (c) gives \( (\sigma \circ \tau)^{-1} = \tau^{-1} \circ \sigma^{-1} \): undo the second shuffle first.

Composing a function with itself needs only that its codomain is its domain; bijectivity is not needed. Shuffling twice is \( \sigma \circ \sigma \), and "apply \( f \) a total of \( n \) times" is a definition by recursion.

::: {#def-iterate}
[Iterates]

Let \( X \) be a set and \( f \colon X \to X \). The **iterates** \( f^n \colon X \to X \), for \( n \in \nN \), are defined by
\[
f^0 \coloneqq \id_X , \qquad f^{n+1} \coloneqq f \circ f^n .
\]
For \( \sigma \in S_X \) and \( n \in \nN \), we also set \( \sigma^{-n} \coloneqq (\sigma^{-1})^n \).
:::

The definition is an instance of @thm-recursion, applied to the set \( X^X \) with the starting value \( \id_X \) and the step \( g \colon \nN \times X^X \to X^X \), \( g(n, h) \coloneqq f \circ h \): there is exactly one sequence \( n \mapsto f^n \) in \( X^X \) with these two properties. Unwinding, \( f^1 = f \circ \id_X = f \), \( f^2 = f \circ f \), \( f^3 = f \circ (f \circ f) \), and \( f^n(x) \) is "apply \( f \) to \( x \), \( n \) times". For a permutation the two clauses do not clash: \( \sigma^{-0} = (\sigma^{-1})^0 = \id_X = \sigma^0 \), and \( (\sigma^{-1})^1 = \sigma^{-1} \) is the inverse function. So \( \sigma^k \) has one meaning for every \( k \in \nZ \). As Section 5.3 warned, \( f^n \) is always an iterate in this book, never the pointwise power \( x \mapsto f(x)^n \).

The definition adds one \( f \) at a time, on the left. The first thing to prove is that blocks of \( f \)'s can be moved around as the notation suggests.

::: {#prp-iterate-laws}
[Laws of Iterates]

Let \( X \) be a set, \( f \colon X \to X \), and \( m, n \in \nN \).

::: {.enumerate options="label=(\alph*)"}
1. \( f^{m+n} = f^m \circ f^n \).
2. \( (f^m)^n = f^{mn} \).
3. If \( \sigma \in S_X \), then \( \sigma^k \in S_X \) for every \( k \in \nZ \); \( \sigma^n \circ \sigma^{-n} = \id_X = \sigma^{-n} \circ \sigma^n \); and \( \sigma^{k + l} = \sigma^k \circ \sigma^l \) for all \( k, l \in \nZ \).
:::
:::

::: {.idea}
Each law is an equation between iterates, and the definition only tells us how to peel one \( f \) off the left. So we induct on the exponent that appears first, peel one \( f \), and use the induction hypothesis on what is left. For (c) the new feature is the sign: \( \sigma^{-n} \) undoes \( \sigma^n \), and a mixed sum \( k + l \) is handled by canceling the overlap.
:::

::: {.proof}
(a) Fix \( n \) and induct on \( m \) (@fd1:ax-induction). For \( m = 0 \), \( f^{0+n} = f^n = \id_X \circ f^n = f^0 \circ f^n \) by @prp-composition-associative. Suppose \( f^{m+n} = f^m \circ f^n \). Then, by @def-iterate, the induction hypothesis and @prp-composition-associative,
\[
f^{(m+1)+n} = f \circ f^{m+n} = f \circ (f^m \circ f^n) = (f \circ f^m) \circ f^n = f^{m+1} \circ f^n .
\]

(b) Induct on \( n \). For \( n = 0 \), \( (f^m)^0 = \id_X = f^0 = f^{m \cdot 0} \). If \( (f^m)^n = f^{mn} \), then \( (f^m)^{n+1} = f^m \circ (f^m)^n = f^m \circ f^{mn} = f^{m + mn} \) by (a), and \( m + mn = m(n + 1) \).

(c) First, \( \sigma^n \in S_X \) for \( n \in \nN \), by induction: \( \sigma^0 = \id_X \in S_X \), and \( \sigma^{n+1} = \sigma \circ \sigma^n \in S_X \) by @prp-permutations-closed (a). Since \( \sigma^{-1} \in S_X \) (@prp-permutations-closed (c)), the same induction gives \( \sigma^{-n} = (\sigma^{-1})^n \in S_X \). So \( \sigma^k \in S_X \) for every \( k \in \nZ \).

Next, \( \sigma^n \circ \sigma^{-n} = \id_X \), by induction on \( n \). For \( n = 0 \) both factors are \( \id_X \). If it holds for \( n \), then \( \sigma^{n+1} = \sigma^n \circ \sigma \) by (a) with the exponents \( n \) and \( 1 \), and \( \sigma^{-(n+1)} = \sigma^{-1} \circ \sigma^{-n} \) by @def-iterate, so
\[
\sigma^{n+1} \circ \sigma^{-(n+1)} = \sigma^n \circ (\sigma \circ \sigma^{-1}) \circ \sigma^{-n} = \sigma^n \circ \sigma^{-n} = \id_X ,
\]
by @prp-composition-associative and @prp-permutations-closed (c). The equation \( \sigma^{-n} \circ \sigma^n = \id_X \) is the same induction with the roles of \( \sigma \) and \( \sigma^{-1} \) exchanged.

Finally, \( \sigma^{k+l} = \sigma^k \circ \sigma^l \). When \( k, l \ge 0 \) this is (a). When \( k, l \le 0 \), it is (a) for the map \( \sigma^{-1} \) with the exponents \( -k \) and \( -l \). The cases with \( k \) and \( l \) of opposite signs reduce to these two by canceling, as the second reading below shows.
:::

::: {.second-reading title="The mixed signs in (c)"}
Let \( k \) and \( l \) have opposite signs. All equalities below use @prp-composition-associative, the cases of (c) already proved, and \( \sigma^n \circ \sigma^{-n} = \id_X = \sigma^{-n} \circ \sigma^n \) for \( n \in \nN \).

*Case \( k \ge 0 \), \( l = -b \) with \( b > 0 \).* If \( k \ge b \), then \( \sigma^k = \sigma^{k-b} \circ \sigma^b \) by (a), so \( \sigma^k \circ \sigma^{-b} = \sigma^{k-b} \circ (\sigma^b \circ \sigma^{-b}) = \sigma^{k-b} \). If \( k < b \), then \( \sigma^{-b} = \sigma^{-k} \circ \sigma^{-(b-k)} \) by (a) for \( \sigma^{-1} \), so \( \sigma^k \circ \sigma^{-b} = (\sigma^k \circ \sigma^{-k}) \circ \sigma^{-(b-k)} = \sigma^{k-b} \). In both cases \( \sigma^k \circ \sigma^l = \sigma^{k+l} \).

*Case \( k = -a \) with \( a > 0 \), \( l \ge 0 \).* If \( l \ge a \), then \( \sigma^l = \sigma^a \circ \sigma^{l-a} \) by (a), so \( \sigma^{-a} \circ \sigma^l = (\sigma^{-a} \circ \sigma^a) \circ \sigma^{l-a} = \sigma^{l-a} \). If \( l < a \), then \( \sigma^{-a} = \sigma^{-(a-l)} \circ \sigma^{-l} \) by (a) for \( \sigma^{-1} \), so \( \sigma^{-a} \circ \sigma^l = \sigma^{-(a-l)} \circ (\sigma^{-l} \circ \sigma^l) = \sigma^{l-a} \). Again \( \sigma^k \circ \sigma^l = \sigma^{k+l} \).
:::

In particular \( \sigma^{-n} \) is the inverse of \( \sigma^n \), by the middle clause of (c) and @def-inverse-function: shuffling backwards \( n \) times undoes shuffling forwards \( n \) times.

::: {.check}
For \( f \colon \nR \to \nR \), \( f(x) = x + 3 \), find \( f^n \) and prove your answer.
:::

::: {.solution}
\( f^n(x) = x + 3n \). By induction on \( n \): \( f^0(x) = x = x + 3 \cdot 0 \); and if \( f^n(x) = x + 3n \), then \( f^{n+1}(x) = f(f^n(x)) = (x + 3n) + 3 = x + 3(n + 1) \) by @def-iterate. Here \( f^n \) is not the power \( (x + 3)^n \).
:::

## Orbits

In the hook, the cards fell into sets that move among themselves: \( \{1, 3, 9, 5, 4\} \), \( \{2, 6, 7, 10, 8\} \), \( \{0\} \) and \( \{11\} \). The natural guess for "in the same set" is "one card reaches the other": \( y = f^n(x) \) for some \( n \in \nN \). This relation is reflexive (\( n = 0 \)) and transitive (add the exponents, @prp-iterate-laws (a)). It is not symmetric. For \( f \colon \nN \to \nN \), \( f(n) = n + 1 \), the point \( 0 \) reaches \( 1 = f(0) \), but \( 1 \) never reaches \( 0 \), since \( f^n(1) = 1 + n \ge 1 \). So reachability does not cut a set into pieces. For a permutation the repair is to allow negative exponents: walk backwards as well as forwards.

*The orbit of a point is everywhere a permutation can take it, forwards or backwards.*

::: {#def-orbit}
[Orbit, Forward Orbit, Fixed Point]

Let \( X \) be a set and \( \sigma \in S_X \). For \( x, y \in X \), let \( x \sim_\sigma y \) mean that \( y = \sigma^k(x) \) for **some** \( k \in \nZ \). The **orbit** of \( x \) under \( \sigma \) is
\[
O_\sigma(x) \coloneqq \{ \sigma^k(x) : k \in \nZ \} .
\]
For an arbitrary function \( f \colon X \to X \), the **forward orbit** of \( x \) is \( \{ f^n(x) : n \in \nN \} \). A **fixed point** of \( f \) is an \( x \in X \) with \( f(x) = x \).
:::

In words: the orbit collects every point reached from \( x \) by applying \( \sigma \) or \( \sigma^{-1} \) any number of times; the forward orbit uses \( f \) only, so it makes sense for every self-map. For a permutation, the forward orbit of \( x \) is contained in \( O_\sigma(x) \), since \( \nN \subseteq \nZ \); on a finite set the two are equal, as the next subsection proves. A fixed point is a point the map does not move, the sense in which Section 4.4 called \( 0 \) a fixed point of a bijection. For the hook's shuffle, \( O_\sigma(1) = \{1, 3, 9, 5, 4\} \): since \( \sigma^5(1) = 1 \), the negative powers give nothing new (\( \sigma^{-1}(1) = \sigma^4(1) \), and so on; @prp-orbit-cycle proves this in general), and \( 0 \) and \( 11 \) are the fixed points.

::: {.warning}
Forward orbits need not cut a set into pieces. For \( f(n) = n + 1 \) on \( \nN \), the forward orbit of \( 0 \) is \( \nN \) and that of \( 1 \) is \( \{ n \in \nN : n \ge 1 \} \): they overlap and are not equal. Only orbits of a **permutation**, with \( k \) running over \( \nZ \), are guaranteed to be disjoint or equal.
:::

The guarantee is the next theorem: \( \sim_\sigma \) is an equivalence relation, and the orbits are its classes.

::: {#thm-orbits-partition}
[The Orbits of a Permutation Partition the Set]

Let \( X \) be a set and \( \sigma \in S_X \). Then \( \sim_\sigma \) is an equivalence relation on \( X \), and the class of each \( x \in X \) is \( O_\sigma(x) \). Hence the orbits of \( \sigma \) form a partition of \( X \). Moreover, \( x \) is a fixed point of \( \sigma \) if and only if \( O_\sigma(x) = \{x\} \).
:::

::: {.proof}
We check (Eq1)–(Eq3) of @def-equivalence-relation, using @prp-iterate-laws (c) throughout. (Eq1): \( x = \sigma^0(x) \), so \( x \sim_\sigma x \). (Eq2): if \( y = \sigma^k(x) \), then \( \sigma^{-k}(y) = \sigma^{-k}(\sigma^k(x)) = \sigma^{-k + k}(x) = \sigma^0(x) = x \), so \( y \sim_\sigma x \). (Eq3): if \( y = \sigma^k(x) \) and \( z = \sigma^l(y) \), then \( z = \sigma^l(\sigma^k(x)) = \sigma^{l+k}(x) \) and \( l + k \in \nZ \), so \( x \sim_\sigma z \).

The class of \( x \) is \( \{ y \in X : y \sim_\sigma x \} \) (@def-equivalence-class), which by (Eq2) is \( \{ y \in X : x \sim_\sigma y \} = \{ \sigma^k(x) : k \in \nZ \} = O_\sigma(x) \). By @thm-classes-partition (d), the classes form a partition of \( X \).

If \( O_\sigma(x) = \{x\} \), then \( \sigma(x) = \sigma^1(x) \in O_\sigma(x) \), so \( \sigma(x) = x \). Conversely, let \( \sigma(x) = x \). Then \( \sigma^n(x) = x \) for every \( n \in \nN \), by induction: \( \sigma^{n+1}(x) = \sigma(\sigma^n(x)) = \sigma(x) = x \). Also \( \sigma^{-1}(x) = \sigma^{-1}(\sigma(x)) = x \), so \( x \) is a fixed point of \( \sigma^{-1} \), and the same induction gives \( \sigma^{-n}(x) = (\sigma^{-1})^n(x) = x \). Hence \( \sigma^k(x) = x \) for every \( k \in \nZ \), and \( O_\sigma(x) = \{x\} \).
:::

The theorem answers the hook's first observation: the cards always fall into sets that move among themselves, because the orbits are the classes of an equivalence relation, and each card lies in exactly one class.

::: {.check}
Find the orbits of
\( \sigma = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 3 & 5 & 1 & 2 & 4 \end{pmatrix} \).
:::

::: {.solution}
From \( 1 \): \( 1 \mapsto 3 \mapsto 1 \), so \( O_\sigma(1) = \{1, 3\} \) (going backwards, \( \sigma^{-1}(1) = 3 \), gives nothing new). From \( 2 \): \( 2 \mapsto 5 \mapsto 4 \mapsto 2 \), so \( O_\sigma(2) = \{2, 5, 4\} \). These two orbits are disjoint and cover \( \{1, \dots, 5\} \), as @thm-orbits-partition says they must; \( \sigma \) has no fixed point.
:::

## Following an orbit

In the hook, card \( 1 \) came back after five shuffles and card \( 0 \) after one. On a finite set this always happens, and the first return controls everything else about the orbit.

::: {#prp-orbit-cycle}
[Following an Orbit]

Let \( X \) be a finite set, \( \sigma \in S_X \), and \( x \in X \). Then there is a **least** integer \( k \ge 1 \) with \( \sigma^k(x) = x \). For this \( k \):

::: {.enumerate options="label=(\alph*)"}
1. the points \( x, \sigma(x), \dots, \sigma^{k-1}(x) \) are distinct;
2. \( O_\sigma(x) = \{ x, \sigma(x), \dots, \sigma^{k-1}(x) \} \), so \( O_\sigma(x) \) has exactly \( k \) elements;
3. for every \( m \in \nZ \), \( \sigma^m(x) = x \) if and only if \( k \mid m \).
:::

The number \( k \) is the **length** of the orbit \( O_\sigma(x) \).
:::

::: {.idea}
[Scratch work]

The set is finite and the forward orbit \( x, \sigma(x), \sigma^2(x), \dots \) is an infinite list, so the list must repeat. A repeat is not yet a return to \( x \): we need to cancel the front of it, and that is where injectivity comes in.

| Givens | Goal |
|---|---|
| \( X \) has \( n \) elements; \( \sigma \) bijective | some \( k \ge 1 \) with \( \sigma^k(x) = x \) |
| the \( n + 1 \) points \( \sigma^0(x), \dots, \sigma^n(x) \) | two of them equal: \( m \mapsto \sigma^{m-1}(x) \) on \( \{1, \dots, n + 1\} \) is not injective (@cor-pigeonhole-finite-sets (a)) |
| \( \sigma^i(x) = \sigma^j(x) \) with \( 0 \le i < j \le n \); \( \sigma^j = \sigma^i \circ \sigma^{j-i} \) | cancel \( \sigma^i \), which is injective (@prp-iterate-laws (c)): \( k = j - i \) works |
| a non-empty set of such \( k \) | a least one (@thm-well-ordering) |

Once there is a least return time, (a) is minimality again, and (c) is division with remainder: \( m \) full rounds plus a part of a round.
:::

::: {.proof}
Let \( X \) have \( n \) elements. The set \( \{1, \dots, n + 1\} \) has \( n + 1 \) elements, so the function \( \{1, \dots, n + 1\} \to X \), \( m \mapsto \sigma^{m-1}(x) \), is not injective (@cor-pigeonhole-finite-sets (a)). So there are integers \( 0 \le i < j \le n \) with \( \sigma^i(x) = \sigma^j(x) \). By @prp-iterate-laws (c), \( \sigma^j = \sigma^i \circ \sigma^{j-i} \), so \( \sigma^i(\sigma^{j-i}(x)) = \sigma^i(x) \), and since \( \sigma^i \in S_X \) is injective, \( \sigma^{j-i}(x) = x \). Hence the set \( K \coloneqq \{ k \in \nN : k \ge 1 \text{ and } \sigma^k(x) = x \} \) contains \( j - i \), and by @thm-well-ordering it has a least element \( k \).

(a) Suppose \( \sigma^i(x) = \sigma^j(x) \) with \( 0 \le i < j < k \). As above, \( \sigma^{j-i}(x) = x \), with \( 1 \le j - i < k \), so \( j - i \in K \), against the choice of \( k \). So the \( k \) points are distinct.

(c) First, \( \sigma^{qk}(x) = x \) for every \( q \in \nZ \). For \( q \ge 0 \), by induction on \( q \): \( \sigma^0(x) = x \), and \( \sigma^{(q+1)k}(x) = \sigma^k(\sigma^{qk}(x)) = \sigma^k(x) = x \) by @prp-iterate-laws (c). For \( q < 0 \), \( -q > 0 \), so \( \sigma^{-qk}(x) = x \) by the case just proved, and \( \sigma^{qk}(x) = \sigma^{qk}(\sigma^{-qk}(x)) = \sigma^0(x) = x \). Now let \( m \in \nZ \), and write \( m = qk + r \) with \( q, r \in \nZ \) and \( 0 \le r < k \) (@thm-division-algorithm). Then
\[
\sigma^m(x) = \sigma^r\bigl(\sigma^{qk}(x)\bigr) = \sigma^r(x) .
\]
If \( r = 0 \), this is \( x \). If \( 1 \le r < k \), then \( \sigma^r(x) \ne x \), since otherwise \( r \in K \) and \( r < k \). So \( \sigma^m(x) = x \) if and only if \( r = 0 \). By the uniqueness in @thm-division-algorithm, \( r = 0 \) holds exactly when \( m = q'k \) for some \( q' \in \nZ \), that is, when \( k \mid m \).

(b) The display shows that every point \( \sigma^m(x) \) of the orbit is one of \( \sigma^0(x), \dots, \sigma^{k-1}(x) \); conversely each of these lies in the orbit. By (a), \( \{1, \dots, k\} \to O_\sigma(x) \), \( j \mapsto \sigma^{j-1}(x) \), is injective, and it is onto by what was just shown; so \( O_\sigma(x) \) has \( k \) elements (@def-finite).
:::

Two things to take from the proof. The forward orbit already contains \( x, \sigma(x), \dots, \sigma^{k-1}(x) \), so on a finite set it equals the orbit: walking forwards reaches every point that walking backwards does. And in the existence of a return, the hypothesis "\( \sigma \) is a permutation" was used once, in the cancellation of \( \sigma^i \); the rest of the proof needs negative powers only because the orbit is defined with them. The last subsection shows what goes wrong without it. The argument is a method in its own right.

::: {#exm-method-follow-the-orbit}
[Method: follow an orbit]

**Template.** (1) List the forward orbit \( x, f(x), f^2(x), \dots \). (2) On a finite set of \( n \) elements, two of the first \( n + 1 \) terms are equal (@cor-pigeonhole-finite-sets). (3) Take the first repeat, or the least return time (@thm-well-ordering). (4) Carry the repeat with the map's structure: cancel if the map is injective; push forward with \( f^{l+1} = f \circ f^l \) always.

**When to use it.** Repeated application of one map on a finite set: shuffles, the tick of a clock, maps on \( \nZ/n \).

**The usual failure.** Speaking of "the first repeat" without proving that a repeat exists; canceling a map that is not injective, which forgets the tail before the cycle.
:::

Now the hook, in full.

::: {#exm-three-pile-shuffle}
[The three-pile shuffle]

Let \( \sigma \) be the shuffle of twelve cards in three piles of four. Show that \( \sigma \) is a permutation of \( \{0, \dots, 11\} \), find its orbits and their lengths, and find the least \( N \ge 1 \) with \( \sigma^N = \id \).
:::

::: {.solution}
*A formula.* Write \( i = 4p + r \) with \( 0 \le r < 4 \) (@thm-division-algorithm); for \( 0 \le i \le 11 \), \( p \in \{0, 1, 2\} \) is the pile and \( r \) the place in it. The card is dealt in round \( r \) (counting from \( 0 \)), after the \( p \) cards of that round from the earlier piles, so \( \sigma(i) = 3r + p \); the three cases of the hook are \( p = 0, 1, 2 \).

*A permutation.* Every \( j \in \{0, \dots, 11\} \) is \( 3r + p \) for exactly one pair with \( 0 \le p < 3 \), by @thm-division-algorithm, and then \( 0 \le r \le 3 \), because \( -3 < j - p = 3r \le 11 \). So \( 3r + p \mapsto 4p + r \) is a function \( \{0, \dots, 11\} \to \{0, \dots, 11\} \), and it undoes \( \sigma \) on both sides. By @thm-bijection-iff-inverse, \( \sigma \in S_X \) for \( X = \{0, \dots, 11\} \).

*Arithmetic modulo \( 11 \).* \( 3i - \sigma(i) = 12p + 3r - 3r - p = 11p \), so \( \sigma(i) \equiv 3i \pmod{11} \). For \( i \le 10 \), \( \sigma(i) \ne 11 \), since \( 3r + p = 11 \) forces \( r = 3 \), \( p = 2 \), that is \( i = 11 \). So for \( i \le 10 \), \( 3i = 11p + \sigma(i) \) with \( 0 \le \sigma(i) < 11 \), and \( \sigma(i) \) is the remainder of \( 3i \) on division by \( 11 \) by the uniqueness in @thm-division-algorithm; and \( \sigma(11) = 11 \).

*Orbits.* Follow each orbit (@exm-method-follow-the-orbit), reducing modulo \( 11 \):
\[
\begin{aligned}
&1 \mapsto 3 \mapsto 9 \mapsto 5 \mapsto 4 \mapsto 1 &&(27 \equiv 5, \ 15 \equiv 4, \ 12 \equiv 1), \\
&2 \mapsto 6 \mapsto 7 \mapsto 10 \mapsto 8 \mapsto 2 &&(18 \equiv 7, \ 21 \equiv 10, \ 30 \equiv 8, \ 24 \equiv 2),
\end{aligned}
\]
and \( 0 \), \( 11 \) are fixed. The orbits are \( \{0\} \), \( \{11\} \), \( \{1, 3, 9, 5, 4\} \), \( \{2, 6, 7, 10, 8\} \), of lengths \( 1, 1, 5, 5 \).

*The return.* Each length divides \( 5 \), so \( \sigma^5(x) = x \) for every \( x \) by @prp-orbit-cycle (c), and \( \sigma^5 = \id \) by @prp-function-equality. For \( 1 \le N < 5 \), \( 5 \nmid N \), so \( \sigma^N(1) \ne 1 \) by the same part (c). Hence \( N = 5 \). The arithmetic agrees: \( 3^5 = 243 = 22 \cdot 11 + 1 \), so five shuffles multiply every position below \( 11 \) by \( 1 \) modulo \( 11 \).
:::

::: {.check}
Let \( t \colon \nZ/12 \to \nZ/12 \), \( [a] \mapsto [a + 1] \), be the tick of @exm-clock-maps. What is the length of the orbit of \( [1] \) under \( t \)? And under \( [a] \mapsto [a + 3] \)?
:::

::: {.solution}
By induction, \( t^m([1]) = [1 + m] \) for \( m \in \nN \), and \( [1 + m] = [1] \) exactly when \( 12 \mid m \) (@thm-classes-partition (b), @def-congruence). The least \( m \ge 1 \) is \( 12 \): the orbit is all of \( \nZ/12 \), of length \( 12 \). The map \( [a] \mapsto [a + 3] \) is well defined as the tick is (\( (a + 3) - (a' + 3) = a - a' \)), and is a permutation with inverse \( [a] \mapsto [a - 3] \). From \( [1] \): \( [1], [4], [7], [10], [13] = [1] \). The orbit is \( \{[1], [4], [7], [10]\} \), of length \( 4 \).
:::

## Cycles

The hook's shuffle moves \( 1, 3, 9, 5, 4 \) round in a ring, moves \( 2, 6, 7, 10, 8 \) round in another ring, and leaves everything else alone. A permutation that moves one ring and nothing else deserves a name and a notation.

::: {#def-permutation-cycle}
[Cycle]

Let \( X \) be a set, \( k \ge 2 \), and \( x_1, \dots, x_k \in X \) **distinct**. The **cycle** \( (x_1\ x_2\ \cdots\ x_k) \) is the function \( X \to X \) that sends \( x_j \mapsto x_{j+1} \) for \( 1 \le j < k \), sends \( x_k \mapsto x_1 \), and sends every other point of \( X \) to itself. Two cycles are **disjoint** if their sets of entries are disjoint.
:::

The cycle is defined by gluing (@exm-method-gluing): the pieces \( \{x_1, \dots, x_k\} \) and its complement are disjoint and cover \( X \), so there are no overlaps to check. On the first piece the rule reads the index \( j \) of a point, and distinctness makes that index unique. On the second piece the rule is the identity. A cycle is a permutation: \( (x_k\ \cdots\ x_2\ x_1) \) sends \( x_{j+1} \mapsto x_j \) and \( x_1 \mapsto x_k \), so composing it with \( (x_1\ \cdots\ x_k) \) in either order fixes each \( x_j \), and it fixes each point off the entries since both factors do. By @thm-bijection-iff-inverse the cycle is bijective, with inverse the reversed cycle. The same cycle has \( k \) names: \( (1\ 3\ 9\ 5\ 4) = (3\ 9\ 5\ 4\ 1) \), since both send each entry to the next one round the ring.

The theorem below says that every permutation of a finite set is built from its orbits in this way: one cycle for each orbit with at least two points. Before stating it, note that such orbits are finitely many. Let \( X \) have \( n \) elements via a bijection \( \varphi \colon \{1, \dots, n\} \to X \). Send each orbit \( O \) to the least \( i \) with \( \varphi(i) \in O \) (@thm-well-ordering). Distinct orbits are disjoint (@thm-orbits-partition), so they get distinct indices, and the orbits are in bijection with a subset of \( \{1, \dots, n\} \), which is finite (@prp-subset-finite).

::: {#thm-permutation-cycles}
[Cycle Decomposition]

Let \( X \) be a finite set and \( \sigma \in S_X \). Let \( O_1, \dots, O_r \) be the distinct orbits of \( \sigma \) with at least two elements, choose \( x_i \in O_i \), let \( k_i \) be the number of elements of \( O_i \) (so \( \card{O_i} = k_i \)), and let
\[
\gamma_i \coloneqq \bigl( x_i\ \ \sigma(x_i)\ \ \cdots\ \ \sigma^{k_i - 1}(x_i) \bigr) .
\]
Then \( \gamma_1, \dots, \gamma_r \) are pairwise disjoint cycles, \( \gamma_i \circ \gamma_j = \gamma_j \circ \gamma_i \) for all \( i, j \), and
\[
\sigma = \gamma_1 \circ \gamma_2 \circ \cdots \circ \gamma_r ,
\]
bracketed from the left; if \( r = 0 \), this says \( \sigma = \id_X \).
:::

::: {.idea}
Both sides are functions on \( X \), so we compare values (@prp-function-equality). A point of \( O_i \) is moved by \( \gamma_i \) exactly as \( \sigma \) moves it, and is left alone by every other \( \gamma_j \). So composing the cycles one at a time, the composite agrees with \( \sigma \) on more and more orbits; an induction on the number of cycles composed makes that precise.
:::

::: {.proof}
By @prp-orbit-cycle, \( O_i = \{ x_i, \sigma(x_i), \dots, \sigma^{k_i - 1}(x_i) \} \) and these \( k_i \ge 2 \) points are distinct, so \( \gamma_i \) is a cycle whose set of entries is \( O_i \). Distinct orbits are disjoint (@thm-orbits-partition), so the cycles are pairwise disjoint.

*The key value.* Let \( y \in O_i \), say \( y = \sigma^m(x_i) \) with \( 0 \le m < k_i \). If \( m < k_i - 1 \), then \( \gamma_i(y) = \sigma^{m+1}(x_i) = \sigma(y) \) by @def-iterate. If \( m = k_i - 1 \), then \( \gamma_i(y) = x_i = \sigma^{k_i}(x_i) = \sigma(y) \). So \( \gamma_i(y) = \sigma(y) \) for every \( y \in O_i \); and \( \sigma(y) = \sigma^{m+1}(x_i) \in O_i \). For \( j \ne i \), \( \gamma_j \) fixes every point of \( O_i \), since \( O_i \cap O_j = \emptyset \).

Define \( \delta^{(0)} \coloneqq \id_X \) and \( \delta^{(j)} \coloneqq \delta^{(j-1)} \circ \gamma_j \) for \( 1 \le j \le r \), by recursion (@thm-recursion, with \( \gamma_j \coloneqq \id_X \) for \( j > r \)). So \( \delta^{(r)} \) is the composite of the theorem, bracketed from the left. Let \( U_j \coloneqq O_1 \cup \dots \cup O_j \). We prove by induction on \( j \le r \):
\[
\delta^{(j)}(y) = \sigma(y) \ \text{ for } y \in U_j , \qquad \delta^{(j)}(y) = y \ \text{ for } y \in X \setminus U_j .
\]
For \( j = 0 \), \( U_0 = \emptyset \) and \( \delta^{(0)} = \id_X \). Suppose the claim holds for \( j - 1 \), and let \( y \in X \). If \( y \in O_j \), then \( \gamma_j(y) = \sigma(y) \in O_j \), and \( O_j \) is disjoint from \( U_{j-1} \), so \( \delta^{(j)}(y) = \delta^{(j-1)}(\sigma(y)) = \sigma(y) \). If \( y \notin O_j \), then \( \gamma_j(y) = y \), so \( \delta^{(j)}(y) = \delta^{(j-1)}(y) \); and since \( y \notin O_j \), \( y \in U_j \) exactly when \( y \in U_{j-1} \). In both cases the claim holds for \( j \).

For \( j = r \): a point \( y \) outside \( U_r \) lies in an orbit with fewer than two elements, so \( O_\sigma(y) = \{y\} \) and \( \sigma(y) = y \) (@thm-orbits-partition). Hence \( \delta^{(r)}(y) = \sigma(y) \) for every \( y \in X \), and \( \delta^{(r)} = \sigma \) by @prp-function-equality. That disjoint cycles commute is a check of values at a point of \( O_i \), of \( O_j \), and of neither, which the second reading below carries out.
:::

::: {.second-reading title="Disjoint cycles commute"}
Let \( i \ne j \) and \( y \in X \). If \( y \in O_i \), then \( \gamma_j(y) = y \), so \( \gamma_i(\gamma_j(y)) = \gamma_i(y) = \sigma(y) \); and \( \gamma_i(y) = \sigma(y) \in O_i \) is fixed by \( \gamma_j \), so \( \gamma_j(\gamma_i(y)) = \sigma(y) \). If \( y \in O_j \), the same two lines with \( i \) and \( j \) exchanged give \( \sigma(y) \) on both sides. If \( y \) lies in neither, both cycles fix it, and both composites give \( y \). So \( \gamma_i \circ \gamma_j = \gamma_j \circ \gamma_i \) by @prp-function-equality. For \( i = j \) there is nothing to prove.
:::

From now on we write \( \gamma\delta \) for \( \gamma \circ \delta \), the right factor applied first, the convention of *Algebraic Preliminaries*, Chapter 3. Two examples. The three-pile shuffle of @exm-three-pile-shuffle is
\[
\sigma = (1\ 3\ 9\ 5\ 4)(2\ 6\ 7\ 10\ 8) ,
\]
and the two factors may be written in either order. The tick of @exm-clock-maps has one orbit, all of \( \nZ/12 \), with \( t^m([0]) = [m] \), so it is the single cycle \( ([0]\ [1]\ \cdots\ [11]) \).

The decomposition answers the hook's second question. A permutation of a finite set comes back to the identity, and the orbit lengths say when.

::: {#cor-permutation-power-identity}
[Some Power Is the Identity]

Let \( X \) be a finite set and \( \sigma \in S_X \). For an integer \( N \ge 1 \), \( \sigma^N = \id_X \) if and only if the length of every orbit of \( \sigma \) divides \( N \). There is such an \( N \).
:::

::: {.proof}
By @prp-function-equality, \( \sigma^N = \id_X \) means \( \sigma^N(x) = x \) for every \( x \in X \), and by @prp-orbit-cycle (c) that holds exactly when the length \( k_x \) of \( O_\sigma(x) \) divides \( N \) for every \( x \). This proves the equivalence.

For existence, let \( X \) have \( n \) elements, and let \( \varphi \colon \{1, \dots, n\} \to X \) be a bijection (@def-finite), and let \( N \coloneqq \prod_{i=1}^{n} k_{\varphi(i)} \) (@def-sum-product). Each factor is an integer \( \ge 1 \), so \( N \) is an integer \( \ge 1 \). Write \( P_j \coloneqq \prod_{i=1}^{j} k_{\varphi(i)} \). For a fixed \( i \le n \), \( k_{\varphi(i)} \mid P_j \) for every \( j \) with \( i \le j \le n \), by induction on \( j \): \( P_i = P_{i-1} \, k_{\varphi(i)} \), and \( P_j \mid P_{j+1} = P_j \, k_{\varphi(j+1)} \), so @prp-divides-transitive carries the divisibility from \( P_j \) to \( P_{j+1} \). Hence \( k_x \mid P_n = N \) for every \( x = \varphi(i) \in X \), and \( \sigma^N = \id_X \) by the first part.
:::

The **least** such \( N \) is the least positive common multiple of the orbit lengths: by the corollary, \( N \) works exactly when it is a common multiple of all of them. For two distinct lengths \( a \) and \( b \), that least common multiple is the one found in @exm-divisibility-lcm. For the three-pile shuffle the lengths are \( 1, 1, 5, 5 \), and the answer is \( 5 \), as the hook found by hand.

::: {.check}
Decompose \( [a] \mapsto [5a] \) on \( \nZ/12 \) into disjoint cycles.
:::

::: {.solution}
The map is well defined by @prp-congruence-arithmetic. Applying it twice gives \( [25a] = [a] \), since \( 25 \equiv 1 \pmod{12} \), so it is its own inverse and a permutation. Following orbits: \( [1] \mapsto [5] \mapsto [25] = [1] \); \( [2] \mapsto [10] \mapsto [50] = [2] \); \( [4] \mapsto [20] = [8] \mapsto [40] = [4] \); \( [7] \mapsto [35] = [11] \mapsto [55] = [7] \); and \( [0], [3], [6], [9] \) are fixed (\( 15 \equiv 3 \), \( 30 \equiv 6 \), \( 45 \equiv 9 \)). So the map is \( ([1]\ [5])([2]\ [10])([4]\ [8])([7]\ [11]) \).
:::

## Maps that are not permutations

The last question of the hook: what if the rule sends two positions to one? Then there is no inverse, orbits in the sense of @def-orbit are not defined, and @prp-orbit-cycle's cancellation is not available. Forward orbits still exist, and on a finite set they still repeat. What changes is that the repeat need not involve the starting point.

::: {#prp-eventually-periodic}
[Forward Orbits of a Self-Map of a Finite Set]

Let \( X \) be a set with \( n \) elements, \( f \colon X \to X \), and \( x \in X \). There are integers \( m \ge 0 \) and \( p \ge 1 \) with \( m + p \le n \) such that
\[
f^{l + p}(x) = f^l(x) \quad \text{for every integer } l \ge m .
\]
:::

::: {.idea}
This is @exm-method-follow-the-orbit with step (4) done without canceling: the pigeonhole repeat \( f^i(x) = f^j(x) \) cannot be pulled back to \( x \), but it can be pushed forward, one application of \( f \) at a time.
:::

::: {.proof}
As in the proof of @prp-orbit-cycle, @cor-pigeonhole-finite-sets (a) gives integers \( 0 \le i < j \le n \) with \( f^i(x) = f^j(x) \). Let \( m \coloneqq i \) and \( p \coloneqq j - i \ge 1 \); then \( m + p = j \le n \). We prove \( f^{l+p}(x) = f^l(x) \) by induction on \( l \ge m \) (@thm-induction). For \( l = m \) it is \( f^j(x) = f^i(x) \). If it holds for \( l \), then by @def-iterate
\[
f^{l + 1 + p}(x) = f\bigl(f^{l+p}(x)\bigr) = f\bigl(f^l(x)\bigr) = f^{l+1}(x) .
\]
:::

The forward orbit of \( x \) is thus a **tail** \( x, f(x), \dots, f^{m-1}(x) \) followed by a **cycle** that repeats with period \( p \). For a permutation the tail can be taken empty: \( m = 0 \) and \( p = k \), the length of \( O_\sigma(x) \), work, by @prp-orbit-cycle (c). Without injectivity it need not be.

::: {#exm-squaring-mod-eleven}
[Squaring on an eleven-hour clock]

Let \( s \colon \nZ/11 \to \nZ/11 \), \( s([a]) \coloneqq [a^2] \). Show that \( s \) is well defined, follow the forward orbit of \( [2] \), and find \( m \) and \( p \). Does \( [2] \) ever come back?
:::

::: {.solution}
*Well defined.* If \( a \equiv a' \pmod{11} \), then \( a \cdot a \equiv a' \cdot a' \) by the product clause of @prp-congruence-arithmetic: the rule \( a \mapsto [a^2] \) is constant on classes (@exm-method-factor-through-quotient).

*The orbit.* Squaring and reducing modulo \( 11 \):
\[
[2] \mapsto [4] \mapsto [16] = [5] \mapsto [25] = [3] \mapsto [9] \mapsto [81] = [4] ,
\]
using \( 16 - 11 = 5 \), \( 25 - 22 = 3 \), \( 81 - 77 = 4 \). So \( s^5([2]) = [4] = s^1([2]) \), with \( s^1([2]), \dots, s^4([2]) \) distinct: the tail is \( [2] \), and the cycle is \( [4], [5], [3], [9] \), so \( m = 1 \) and \( p = 4 \).

*No return.* The set \( C = \{[4], [5], [3], [9]\} \) contains \( s([2]) = [4] \), and the computation above shows that \( s \) maps \( C \) into \( C \) (\( [4] \mapsto [5] \mapsto [3] \mapsto [9] \mapsto [4] \)). So by induction on \( l \ge 1 \) (@thm-induction, @def-iterate), every \( s^l([2]) \) with \( l \ge 1 \) lies in \( C \), and none of them is \( [2] \). This is the tail-and-cycle shape that @prp-eventually-periodic predicts. The reason is the failure of injectivity: \( s([2]) = [4] = s([9]) \), with \( [2] \ne [9] \). The point \( [4] \) has two arrows coming in, from \( [2] \) and from \( [9] \); the cycle comes back to \( [4] \) through \( [9] \), and never needs \( [2] \) again.
:::

The example is the usual failure of @exm-method-follow-the-orbit in action: from \( s([2]) = s([9]) \) one may not cancel \( s \) to conclude \( [2] = [9] \).

::: {.check}
Follow the forward orbit of \( [0] \) under \( [a] \mapsto [a^2 + 1] \) on \( \nZ/7 \), and find \( m \) and \( p \).
:::

::: {.solution}
\( [0] \mapsto [1] \mapsto [2] \mapsto [5] \mapsto [26] = [5] \), since \( 26 - 21 = 5 \). The tail is \( [0], [1], [2] \), so \( m = 3 \), and \( [5] \) is a fixed point, so \( p = 1 \).
:::

::: {.remark}
[Looking ahead]

*Algebraic Preliminaries*, Chapter 3 gives a name, group, to a set with an associative operation that has an identity and inverses, as \( \circ \) on \( S_X \) does by @prp-permutations-closed, and studies \( S_X \) among its examples.
:::

## Exercises

### A. Check your understanding

::: {#exr-permutations-and-iteration-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. For \( \sigma = (1\ 4)(2\ 3\ 5) \) on \( \{1, \dots, 5\} \), write the two-line tables of \( \sigma \), \( \sigma^{-1} \) and \( \sigma^2 \).
2. Let \( f \colon \{1, \dots, 5\} \to \{1, \dots, 5\} \) send \( 1 \mapsto 2 \), \( 2 \mapsto 3 \), \( 3 \mapsto 4 \), \( 4 \mapsto 2 \), \( 5 \mapsto 5 \). Find \( m \) and \( p \) as in @prp-eventually-periodic for \( x = 1 \), with \( m \) as small as possible.
3. How many fixed points has the three-pile shuffle of twelve cards?
:::
:::

::: {.solution}
(a) Applying the right factor first, \( \sigma \) sends \( 1 \mapsto 4 \), \( 2 \mapsto 3 \), \( 3 \mapsto 5 \), \( 4 \mapsto 1 \), \( 5 \mapsto 2 \):
\[
\sigma = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 4 & 3 & 5 & 1 & 2 \end{pmatrix}, \quad
\sigma^{-1} = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 4 & 5 & 2 & 1 & 3 \end{pmatrix}, \quad
\sigma^2 = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 1 & 5 & 2 & 4 & 3 \end{pmatrix}.
\]
The table of \( \sigma^{-1} \) is that of \( \sigma \) read from bottom to top; \( \sigma^{-1} = (1\ 4)(2\ 5\ 3) \) and \( \sigma^2 = (2\ 5\ 3) \), since the swap \( (1\ 4) \) applied twice is the identity.

(b) The forward orbit is \( 1, 2, 3, 4, 2, \dots \): \( f^4(1) = 2 = f^1(1) \), with \( f^0(1), \dots, f^3(1) \) distinct. So \( m = 1 \), \( p = 3 \) work. And \( m = 0 \) is impossible: \( f \) maps \( \{2, 3, 4\} \) into itself and \( f(1) = 2 \), so by induction \( f^l(1) \in \{2, 3, 4\} \) for every \( l \ge 1 \), and \( f^p(1) \ne 1 = f^0(1) \) for every \( p \ge 1 \).

(c) Two: positions \( 0 \) and \( 11 \) (@exm-three-pile-shuffle).
:::

### B. Practice

::: {#exr-permutations-and-iteration-b1}
[B1: Doubling on nine hours]

Let \( d \colon \nZ/9 \to \nZ/9 \), \( d([a]) \coloneqq [2a] \). Show that \( d \) is a permutation, decompose it into disjoint cycles, and find the least \( N \ge 1 \) with \( d^N = \id \).
:::

::: {.solution}
\( d \) is well defined by @prp-congruence-arithmetic, and so is \( e([a]) \coloneqq [5a] \). Since \( 10 \equiv 1 \pmod 9 \), \( e(d([a])) = [10a] = [a] \) and \( d(e([a])) = [a] \), so \( d \) is bijective with inverse \( e \) (@thm-bijection-iff-inverse). Following orbits (@exm-method-follow-the-orbit):
\[
[1] \mapsto [2] \mapsto [4] \mapsto [8] \mapsto [16] = [7] \mapsto [14] = [5] \mapsto [10] = [1] ,
\]
\( [3] \mapsto [6] \mapsto [12] = [3] \), and \( [0] \) is fixed. So
\[
d = ([1]\ [2]\ [4]\ [8]\ [7]\ [5])([3]\ [6]) ,
\]
with orbit lengths \( 6, 2, 1 \). By @cor-permutation-power-identity, \( d^N = \id \) exactly when \( 6 \mid N \), \( 2 \mid N \) and \( 1 \mid N \), that is, when \( 6 \mid N \) (since \( 2 \mid 6 \), @prp-divides-transitive). The least such \( N \ge 1 \) is \( 6 \).
:::

::: {#exr-permutations-and-iteration-b2}
[B2: Iterates commute]

Let \( f, g \colon X \to X \). Prove that \( f^{n+1} = f^n \circ f \) for every \( n \in \nN \), and that if \( f \circ g = g \circ f \), then \( f^n \circ g = g \circ f^n \) for every \( n \in \nN \).
:::

::: {.solution}
The first equation is @prp-iterate-laws (a) with the exponents \( n \) and \( 1 \), since \( f^1 = f \). For the second, induct on \( n \). For \( n = 0 \), \( \id_X \circ g = g = g \circ \id_X \) (@prp-composition-associative). If \( f^n \circ g = g \circ f^n \), then, by @def-iterate and @prp-composition-associative,
\[
f^{n+1} \circ g = f \circ (f^n \circ g) = f \circ (g \circ f^n) = (f \circ g) \circ f^n = (g \circ f) \circ f^n = g \circ f^{n+1} .
\]
:::

::: {#exr-permutations-and-iteration-b3}
[B3: Orbits are invariant]

Let \( \sigma \in S_X \) and \( x \in X \). Prove that \( \sigma(O_\sigma(x)) = O_\sigma(x) \).
:::

::: {.solution}
\( (\subseteq) \) A point of \( \sigma(O_\sigma(x)) \) is \( \sigma(\sigma^k(x)) = \sigma^{k+1}(x) \) for some \( k \in \nZ \) (@def-image, @prp-iterate-laws (c)), and \( k + 1 \in \nZ \). \( (\supseteq) \) For \( k \in \nZ \), \( \sigma^k(x) = \sigma(\sigma^{k-1}(x)) \) by @prp-iterate-laws (c), and \( \sigma^{k-1}(x) \in O_\sigma(x) \).
:::

::: {#exr-permutations-and-iteration-b4}
[B4: Prove or disprove]

Prove or disprove each statement.

::: {.enumerate options="label=(\alph*)"}
1. If \( X \) is finite and \( f \colon X \to X \) is injective, then every \( x \in X \) has \( f^k(x) = x \) for some \( k \ge 1 \).
2. If \( f \colon X \to X \) and \( f^N = \id_X \) for some \( N \ge 1 \), then \( f \) is a permutation.
3. Every function from a finite non-empty set to itself has a fixed point.
4. Every orbit of a permutation is finite.
5. If \( X \) is finite and every orbit of \( \sigma \in S_X \) has length \( 1 \) or \( 2 \), then \( \sigma \circ \sigma = \id_X \).
:::
:::

::: {.solution}
(a) True. The proof of @prp-orbit-cycle used only that \( \sigma^i \) is injective. Here \( f^i \) is injective for every \( i \in \nN \), by induction with @thm-composition-injective-surjective (a) (\( f^0 = \id_X \), \( f^{i+1} = f \circ f^i \)). So pigeonhole gives \( f^i(x) = f^j(x) \) with \( i < j \); by @prp-iterate-laws (a), \( f^j = f^i \circ f^{j-i} \), and canceling \( f^i \) gives \( f^{j-i}(x) = x \), with \( j - i \ge 1 \).

(b) True. By @prp-iterate-laws (a), \( f \circ f^{N-1} = f^N = \id_X \) and \( f^{N-1} \circ f = f^{(N-1) + 1} = \id_X \). So \( f^{N-1} \) is a two-sided inverse of \( f \), and \( f \) is bijective by @thm-bijection-iff-inverse.

(c) False. The swap of \( \{0, 1\} \), \( 0 \mapsto 1 \), \( 1 \mapsto 0 \), moves both points.

(d) False. \( \sigma \colon \nZ \to \nZ \), \( \sigma(n) = n + 1 \), is a permutation with inverse \( n \mapsto n - 1 \), and \( \sigma^k(0) = k \) for every \( k \in \nZ \) (induction in each direction), so \( O_\sigma(0) = \nZ \). This is not finite: it contains \( \nN \), which is infinite (@exm-hilbert-hotel, @prp-subset-finite).

(e) True. Each orbit length \( k_x \) divides \( 2 \), so \( \sigma^2(x) = x \) by @prp-orbit-cycle (c), for every \( x \); and \( \sigma^2 = \sigma \circ \sigma \) by @def-iterate. So \( \sigma \circ \sigma = \id_X \) by @prp-function-equality.
:::

### C. Going deeper

::: {#exr-permutations-and-iteration-c1}
[C1: Exit check: fifteen cards]

Fifteen cards lie at positions \( 0, \dots, 14 \). Cut them into three piles of five and deal them back in turn, as in the hook, so that
\[
\sigma(i) =
\begin{cases}
3i & \text{if } 0 \le i \le 4, \\
3i - 14 & \text{if } 5 \le i \le 9, \\
3i - 28 & \text{if } 10 \le i \le 14 .
\end{cases}
\]
Show that \( \sigma \) is a permutation, decompose it into disjoint cycles, and find the least \( N \ge 1 \) with \( \sigma^N = \id \).
:::

::: {.solution}
*A permutation.* The three pieces have images \( \{0, 3, 6, 9, 12\} \), \( \{1, 4, 7, 10, 13\} \) and \( \{2, 5, 8, 11, 14\} \): the positions with remainder \( 0 \), \( 1 \), \( 2 \) on division by \( 3 \). Each piece is injective (\( 3i - c = 3i' - c \) gives \( i = i' \)), and the images are disjoint and cover \( \{0, \dots, 14\} \) by @thm-division-algorithm. So two different cards in one piece land in different places, two cards in different pieces land in different images, and every position is hit: \( \sigma \) is bijective. (This is the cross-piece check of @exm-method-gluing.)

*Arithmetic modulo \( 14 \).* Write \( i = 5p + r \) with \( 0 \le r < 5 \); the card lands at \( \sigma(i) = 3r + p \), and \( 3i - \sigma(i) = 15p - p = 14p \), so \( \sigma(i) \equiv 3i \pmod{14} \). Since \( 3r + p = 14 \) only for \( r = 4 \), \( p = 2 \), that is \( i = 14 \), \( \sigma \) maps \( \{0, \dots, 13\} \) into itself, with \( \sigma(i) \) the remainder of \( 3i \) on division by \( 14 \), and \( \sigma(14) = 14 \). By induction and @prp-congruence-arithmetic, \( \sigma^k(i) \equiv 3^k i \pmod{14} \) for \( i \le 13 \).

*Cycles.* \( 0 \), \( 7 \) (\( 21 \equiv 7 \)) and \( 14 \) are fixed. Following orbits (@exm-method-follow-the-orbit):
\[
\begin{aligned}
&1 \mapsto 3 \mapsto 9 \mapsto 13 \mapsto 11 \mapsto 5 \mapsto 1 &&(27 \equiv 13, \ 39 \equiv 11, \ 33 \equiv 5, \ 15 \equiv 1), \\
&2 \mapsto 6 \mapsto 4 \mapsto 12 \mapsto 8 \mapsto 10 \mapsto 2 &&(18 \equiv 4, \ 36 \equiv 8, \ 24 \equiv 10, \ 30 \equiv 2).
\end{aligned}
\]
These account for \( 3 + 6 + 6 = 15 \) positions, so \( \sigma = (1\ 3\ 9\ 13\ 11\ 5)(2\ 6\ 4\ 12\ 8\ 10) \) by @thm-permutation-cycles.

*The return.* The orbit lengths are \( 1, 1, 1, 6, 6 \). By @cor-permutation-power-identity, \( \sigma^N = \id \) exactly when \( 6 \mid N \); the least \( N \ge 1 \) is \( 6 \). Check: \( 3^6 = 729 = 52 \cdot 14 + 1 \), so six shuffles multiply every position below \( 14 \) by \( 1 \) modulo \( 14 \).

**Marking scheme.** (10 points)
- 2: proves \( \sigma \) bijective, including the check across pieces (or by an explicit inverse).
- 2: reduces \( \sigma \) to multiplication by \( 3 \) modulo \( 14 \) on \( \{0, \dots, 13\} \) with \( 14 \) fixed, or follows the orbits directly from the three formulas.
- 3: finds the two \( 6 \)-cycles and the fixed points \( 0, 7, 14 \), with the arithmetic shown.
- 3: concludes \( N = 6 \) and shows that no smaller \( N \) works, either from the orbit lengths by @cor-permutation-power-identity or directly (\( 3^6 \equiv 1 \pmod{14} \) and \( \sigma^k(1) \ne 1 \) for \( 1 \le k \le 5 \)).
Fatal errors (0 for the step): claiming bijectivity from injectivity of each piece alone; taking \( N \) as the sum, rather than a common multiple, of the orbit lengths.
:::

::: {#exr-permutations-and-iteration-c2}
[C2: Find the error]

Here is a claim and a proof.

*Claim.* For every function \( f \) from a finite set \( X \) to itself and every \( x \in X \), there is \( k \ge 1 \) with \( f^k(x) = x \).

*Proof.* By pigeonhole, \( f^i(x) = f^j(x) \) for some \( i < j \). Apply \( f^{-i} \) to both sides: \( x = f^{j-i}(x) \). Take \( k = j - i \).

Is the claim true? Find the line that fails, say why, and state what the argument does prove.
:::

::: {.solution}
The claim is false. The line that fails is "apply \( f^{-i} \)": \( f^{-i} \) is defined only for a permutation (@def-iterate), and the claim is about every self-map. A counterexample to that step, and to the claim, is @exm-squaring-mod-eleven with \( x = [2] \): \( s^1([2]) = s^5([2]) = [4] \), but no \( s^k([2]) \) with \( k \ge 1 \) is \( [2] \). The correct conclusion from the pigeonhole repeat is @prp-eventually-periodic: after a tail, the forward orbit is periodic. For a permutation, or more generally an injective \( f \) (B4 (a)), the cancellation is legitimate and the claim holds.

**Marking scheme.** (10 points)
- 3: says the claim is false, with a counterexample.
- 4: names the failing line, "apply \( f^{-i} \)", and the reason: \( f \) need not be invertible, or even injective.
- 3: states the correct conclusion (tail then cycle, @prp-eventually-periodic), or the extra hypothesis under which the proof is right.
Fatal errors (0 for the step): accepting the proof because the claim holds for permutations; objecting to the pigeonhole step, which is correct.
:::

::: {#exr-permutations-and-iteration-c3}
[C3: Each point, its own clock]

Let \( X \) be a finite set and \( \sigma \in S_X \). Show that the length of \( O_\sigma(x) \) is the same for all points \( x \) of one orbit. Show also that if \( \sigma \) has exactly two orbits, then the number of elements of \( X \) is the sum of their lengths.
:::

::: {.solution}
Let \( y \in O_\sigma(x) \). Then \( x \sim_\sigma y \), so \( O_\sigma(y) = O_\sigma(x) \) by @thm-orbits-partition and @thm-classes-partition (b). By @prp-orbit-cycle (b), the length of an orbit is its number of elements, so the length at \( y \) is the number of elements of \( O_\sigma(y) = O_\sigma(x) \), which is the length at \( x \).

If \( \sigma \) has exactly two orbits \( O \) and \( O' \), they are disjoint and their union is \( X \) (@thm-orbits-partition, @def-partition). By @prp-orbit-cycle (b), \( O \) and \( O' \) have as many elements as their lengths \( k \) and \( k' \), so \( X = O \cup O' \) has \( k + k' \) elements by @prp-disjoint-union-count.
:::

### R. Review

::: {#exr-permutations-and-iteration-r1}
[R1]

On \( \nR \), let \( x \sim y \) mean \( x - y \in \nZ \). Show that \( [x] \mapsto [2x] \) is a well-defined surjection \( \nR/{\sim} \to \nR/{\sim} \) that is not injective.
:::

::: {.solution}
Here \( \sim \) is the equivalence relation of @exm-reals-mod-integers. Let \( g \colon \nR \to \nR/{\sim} \), \( g(x) \coloneqq [2x] \). If \( x \sim x' \), then \( 2x - 2x' = 2(x - x') \in \nZ \), so \( g \) is constant on classes, and @thm-functions-out-of-quotient (a) gives the function \( [x] \mapsto [2x] \) (@exm-method-factor-through-quotient). It is onto: every class \( [y] \) is the image of \( [y/2] \). It is not injective: \( [0] \mapsto [0] \) and \( [\tfrac12] \mapsto [1] = [0] \), while \( [0] \ne [\tfrac12] \) by @exm-reals-mod-integers. The method is the well-definedness check of Section 5.2 (@exm-method-well-definedness).
:::

::: {#exr-permutations-and-iteration-r2}
[R2]

Let \( \varphi \colon X \to Y \) be a bijection. Show that \( \sigma \mapsto \varphi \circ \sigma \circ \varphi^{-1} \) is a bijection from \( S_X \) to \( S_Y \), and that \( x \) is a fixed point of \( \sigma \) if and only if \( \varphi(x) \) is a fixed point of \( \varphi \circ \sigma \circ \varphi^{-1} \).
:::

::: {.solution}
For \( \sigma \in S_X \), \( \varphi \circ \sigma \circ \varphi^{-1} \colon Y \to Y \) is a composite of bijections (\( \varphi^{-1} \) is bijective by @thm-bijection-iff-inverse, since \( \varphi \) is a two-sided inverse of it, @def-inverse-function), so it lies in \( S_Y \) (@thm-composition-injective-surjective (c)); so the rule is a function \( c \colon S_X \to S_Y \). In the same way \( d(\tau) \coloneqq \varphi^{-1} \circ \tau \circ \varphi \) defines \( d \colon S_Y \to S_X \). By @prp-composition-associative and \( \varphi^{-1} \circ \varphi = \id_X \), \( \varphi \circ \varphi^{-1} = \id_Y \) (@def-inverse-function),
\[
d(c(\sigma)) = \varphi^{-1} \circ \bigl((\varphi \circ \sigma) \circ \varphi^{-1}\bigr) \circ \varphi = \bigl(\varphi^{-1} \circ (\varphi \circ \sigma)\bigr) \circ (\varphi^{-1} \circ \varphi) = \bigl((\varphi^{-1} \circ \varphi) \circ \sigma\bigr) \circ \id_X = \sigma ,
\]
with @prp-composition-associative at each regrouping, and likewise \( c(d(\tau)) = \tau \). So \( c \) has a two-sided inverse and is bijective (@thm-bijection-iff-inverse). For the fixed points,
\[
c(\sigma)(\varphi(x)) = \varphi\bigl(\sigma(\varphi^{-1}(\varphi(x)))\bigr) = \varphi(\sigma(x)) ,
\]
which equals \( \varphi(x) \) if and only if \( \sigma(x) = x \), since \( \varphi \) is injective. The tools are the composites and inverses of Sections 2.5 and 2.6. (Section 4.3's @exr-diagonal-arguments-c2 used bijections of \( \nN \) for a different purpose.)
:::

::: {#exr-permutations-and-iteration-r3}
[R3]

Let \( f \colon \nR \to \nR \), \( f(x) = 2x + 1 \). Prove that \( f^n(x) = 2^n x + 2^n - 1 \) for every \( n \in \nN \) and \( x \in \nR \).
:::

::: {.solution}
By induction on \( n \) (@fd1:ax-induction), with the powers of @def-power. For \( n = 0 \): \( f^0(x) = x = 1 \cdot x + 1 - 1 \). If \( f^n(x) = 2^n x + 2^n - 1 \), then by @def-iterate
\[
f^{n+1}(x) = 2\bigl(2^n x + 2^n - 1\bigr) + 1 = 2^{n+1} x + 2^{n+1} - 1 ,
\]
since \( 2 \cdot 2^n = 2^n \cdot 2 = 2^{n+1} \). The method is the induction of Section 3.2 on a sequence defined by recursion (@thm-recursion).
:::

::: {#exr-permutations-and-iteration-r4}
[R4]

Let \( f \colon X \to Y \), \( A \subseteq X \) and \( B \subseteq Y \). Show that \( (f|_A)^{-1}(B) = A \cap f^{-1}(B) \).
:::

::: {.solution}
For every \( a \), by @def-preimage applied to \( f|_A \colon A \to Y \) and to \( f \), and \( f|_A(a) = f(a) \) for \( a \in A \) (@def-restriction-extension),
\[
a \in (f|_A)^{-1}(B) \iff a \in A \wedge f(a) \in B \iff a \in A \cap f^{-1}(B) ,
\]
where the second step uses \( A \subseteq X \). The two sets have the same elements, so they are equal. This is the element-chasing of Section 2.7 applied to a function built in Section 5.1. The tool is the preimage definition (@def-preimage), tested pointwise. The look-alike tools fail: image rules such as @prp-restriction-properties compare images, not preimages, and \( f(A \cap C) \) can be strictly smaller than \( f(A) \cap f(C) \); and \( (f|_A)^{-1} \) here is a preimage, not an inverse function, which \( f|_A \) need not have.
:::

<!-- dependency ledger
exm-three-pile-shuffle (example): (hook) 3*5 - 11 = 4, 3*10 - 22 = 8; the orbit of 1 and 2 by hand; 1 + 1 + 5 + 5 = 12 | arithmetic; fd5/authoring/parked/from-fd2/verify/exm-three-pile-shuffle.py
def-permutation (claim): a two-line table is a permutation iff its bottom row lists every element once | def-injective, def-surjective (unwound in prose)
def-permutation (claim): bottom row of the three-pile table | arithmetic; fd5/authoring/parked/from-fd2/verify/exm-three-pile-shuffle.py
prp-permutations-closed (claim): (after it) (sigma o tau)^{-1} = tau^{-1} o sigma^{-1} | prp-operation-inverse-rules (c) (cited)
def-iterate (claim): sigma^{-0} = id, (sigma^{-1})^1 = sigma^{-1} | def-iterate, prp-composition-associative (unwound)
prp-iterate-laws (proof): m + mn = m(n + 1); exponents in Z add and subtract as integers | R arithmetic, school fact; prp-integers-closed (a)
prp-iterate-laws (proof): induction on n in N | fd1 ax-induction (cited in (a)), used again in (b), (c)
prp-iterate-laws (claim): (quick check) (x + 3n) + 3 = x + 3(n + 1) | R arithmetic
def-orbit (claim): n + 1 >= 1 for n in N, so 1 never reaches 0 | prp-integers-closed (b), lem-naturals-arithmetic (a): naturals are >= 0
def-orbit (claim): the sense of "fixed point" in Section 4.4 (h(0) = 0) | ch03 §04, prose pointer, nothing depends on it
thm-orbits-partition (claim): (quick check) orbits of the 5-element table | arithmetic; fd5/authoring/parked/from-fd2/verify/thm-orbits-partition.py
prp-orbit-cycle (proof): {1, ..., n + 1} has n + 1 elements | def-finite with the identity bijection
prp-orbit-cycle (proof): (q + 1)k = k + qk; -q > 0 for q < 0 | R arithmetic
prp-orbit-cycle (proof): r = 0 iff k | m, by uniqueness of (q, r) | thm-division-algorithm (cited), def-divides
exm-three-pile-shuffle (solution): division by 4 and by 3 gives the pile/place formula; 3i - sigma(i) = 11p; 3r + p = 11 only for (r, p) = (3, 2); orbits mod 11; 3^5 = 243 = 22*11 + 1 | thm-division-algorithm (cited); arithmetic; fd5/authoring/parked/from-fd2/verify/exm-three-pile-shuffle.py
exm-three-pile-shuffle (solution): the remainder of 3i is the unique r in {0..10} with r = 3i mod 11 | thm-division-algorithm (uniqueness, cited inline)
exm-method-follow-the-orbit (claim): (quick check) t^m([1]) = [1 + m]; [a] -> [a + 3] well defined, inverse [a - 3]; orbit [1],[4],[7],[10] | induction, def-congruence; arithmetic; fd5/authoring/parked/from-fd2/verify/exm-method-follow-the-orbit.py
def-permutation-cycle (claim): a cycle is well defined (distinct entries give a unique index) and the reversed cycle is its inverse | inline, gluing as in exm-method-gluing (5.1 thm-gluing)
thm-permutation-cycles (claim): finitely many orbits (least index map into {1..n}) | thm-well-ordering, thm-orbits-partition, prp-subset-finite (cited); a subset of {1..n} with r elements gives a list O_1..O_r by composing bijections, def-finite
thm-permutation-cycles (proof): recursion for delta^(j) on a finite index range, padded with id for j > r | thm-recursion (cited)
thm-permutation-cycles (claim): (examples) shuffle cycles; tick is a 12-cycle, t^m([0]) = [m] | exm-three-pile-shuffle; induction as in the tick check
cor-permutation-power-identity (proof): a product of integers >= 1 is an integer >= 1 | prp-integers-closed (a), R order, induction on the number of factors
cor-permutation-power-identity (claim): (after it) least N is the least common multiple of the orbit lengths | the corollary itself; exm-divisibility-lcm (cited) for two lengths; for more lengths stated in prose only, nothing depends on it
thm-permutation-cycles (claim): (quick check) [5a] on Z/12; 25 = 1 mod 12; the four 2-cycles and four fixed points | arithmetic; fd5/authoring/parked/from-fd2/verify/thm-permutation-cycles.py
exm-squaring-mod-eleven (solution): 16 - 11 = 5, 25 - 22 = 3, 81 - 77 = 4; s(2) = s(9) | arithmetic; fd5/authoring/parked/from-fd2/verify/exm-squaring-mod-eleven.py
prp-eventually-periodic (claim): (quick check) orbit of [0] under a^2 + 1 on Z/7; 26 - 21 = 5 | arithmetic; fd5/authoring/parked/from-fd2/verify/prp-eventually-periodic.py
prp-permutations-closed (claim): (Looking ahead) groups and S_X in Algebraic Preliminaries Ch 2 | fd5 (prose pointer; nothing here depends on it)
thm-permutation-cycles (claim): juxtaposition gamma delta = gamma o delta, as in Algebraic Preliminaries | notation convention only (NOTATION S_X row)
exr-permutations-and-iteration-a1 (solution): tables of sigma, sigma^{-1}, sigma^2; m = 1, p = 3 | arithmetic; fd5/authoring/parked/from-fd2/verify/exr-permutations-and-iteration-a1.py
exr-permutations-and-iteration-b1 (solution): 10 = 1 mod 9; the doubling orbits mod 9 | prp-congruence-arithmetic (cited); arithmetic; fd5/authoring/parked/from-fd2/verify/exr-permutations-and-iteration-b1.py
exr-permutations-and-iteration-b4 (solution): sigma^k(0) = k for k in Z (n -> n + 1 on Z) | induction in each direction, R arithmetic
exr-permutations-and-iteration-c1 (solution): images of the three pieces by remainder mod 3; 3i - sigma(i) = 14p; orbits mod 14; 3^6 = 729 = 52*14 + 1 | thm-division-algorithm, prp-congruence-arithmetic (cited); arithmetic; fd5/authoring/parked/from-fd2/verify/exr-permutations-and-iteration-c1.py
exr-permutations-and-iteration-c1 (solution): images disjoint and covering, each piece injective, so bijective | exm-method-gluing step (4); def-injective, def-surjective
exr-permutations-and-iteration-r1 (solution): 2(x - x') in Z; 2 * (1/2) = 1 ~ 0; y = 2 (y/2) | prp-integers-closed (a), R arithmetic
exr-permutations-and-iteration-r3 (solution): 2 * 2^n = 2^{n+1}; 2(2^n x + 2^n - 1) + 1 = 2^{n+1} x + 2^{n+1} - 1 | def-power (cited), R arithmetic; fd5/authoring/parked/from-fd2/verify/exr-permutations-and-iteration-r3.py
-->
