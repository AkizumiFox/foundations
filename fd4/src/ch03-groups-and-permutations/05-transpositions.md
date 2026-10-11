# Transpositions Generate the Symmetric Group

Section 3.4 wrote permutations in cycle notation and showed that every permutation breaks into disjoint cycles (@thm-disjoint-cycle-decomposition). One small computation there, \( (1\ 3)(1\ 2) = (1\ 2\ 3) \) in @exm-cycle-notation, says more than it seems to: a 3-cycle is two swaps. This section shows that every permutation of \( \{1, \dots, n\} \), for \( n \ge 2 \), is a product of swaps of two points. The determinant of linear algebra is built on exactly this fact, and so is the sign of a permutation, which later volumes define.

Throughout, \( n \in \nN \), products of permutations are read **right to left** (@def-symmetric-group: \( \sigma\tau = \sigma \circ \tau \) applies \( \tau \) first), and a product \( \tau_1 \tau_2 \cdots \tau_r \) is the product of a list in the group \( S_n \) (@def-group-list-product), so brackets may be dropped (@prp-group-list-product-laws (b)).

## Cycles as products of transpositions

Recall from @def-cycle that a **transposition** is a 2-cycle \( (a\ b) \), with \( a \ne b \): it swaps \( a \) and \( b \) and fixes every other point. Two facts about it are used constantly below.

- \( (a\ b) = (b\ a) \), since both swap \( a \) and \( b \) and fix the rest (@fd2:prp-function-equality).
- A transposition is its own inverse: \( (a\ b)(a\ b) = \id \). Indeed \( a \mapsto b \mapsto a \), \( b \mapsto a \mapsto b \), and every other point is fixed twice. Equivalently, the inverse of \( (a\ b) \) is \( (b\ a) = (a\ b) \) (@def-cycle).

The computation \( (1\ 3)(1\ 2) = (1\ 2\ 3) \) has a pattern: both transpositions contain the first entry \( 1 \) of the cycle, and the one applied **first** is \( (1\ 2) \), which sends \( 1 \) to the next entry. Longer cycles follow the same pattern.

::: {#prp-cycle-product-of-transpositions}
[A Cycle Is a Product of Transpositions]

Let \( k \ge 2 \), and let \( i_1, i_2, \dots, i_k \in \{1, \dots, n\} \) be **distinct**. Then
\[
(i_1\ i_2\ \cdots\ i_k) = (i_1\ i_k)(i_1\ i_{k-1}) \cdots (i_1\ i_2) ,
\]
a product of \( k - 1 \) transpositions.
:::

Read right to left, the factors are \( (i_1\ i_2) \), then \( (i_1\ i_3) \), and so on up to \( (i_1\ i_k) \). For \( k = 4 \): \( (1\ 2\ 3\ 4) = (1\ 4)(1\ 3)(1\ 2) \). Follow \( 2 \): the first factor \( (1\ 2) \) sends it to \( 1 \), the second sends \( 1 \) to \( 3 \), and the third fixes \( 3 \); so \( 2 \mapsto 3 \), as the cycle requires.

::: {.idea}
Induct on the length. To pass from \( (i_1\ \cdots\ i_k) \) to \( (i_1\ \cdots\ i_k\ i_{k+1}) \), the only change is that \( i_k \) must now go to \( i_{k+1} \) instead of back to \( i_1 \), and \( i_{k+1} \) must go to \( i_1 \). One more swap of \( i_1 \) and \( i_{k+1} \), applied **after** the shorter cycle, makes exactly this change.
:::

::: {.proof}
We prove, by @fd2:thm-induction with base \( 2 \) (read on \( \omega \) by @fd3:cor-omega-identification (b)), the statement \( P(k) \): "for every list \( (i_1, \dots, i_k) \) of distinct points of \( \{1, \dots, n\} \), the displayed equation holds".

*Base, \( k = 2 \).* The right-hand side is the list of one factor \( (i_1\ i_2) \), whose product is \( (i_1\ i_2) \) (@def-group-list-product), and this is the left-hand side.

*Step.* Let \( k \ge 2 \), suppose \( P(k) \), and let \( i_1, \dots, i_{k+1} \) be distinct. Put \( \gamma \coloneqq (i_1\ \cdots\ i_k) \) and \( \tau \coloneqq (i_1\ i_{k+1}) \). We claim \( \tau\gamma = (i_1\ \cdots\ i_{k+1}) \), and check it point by point (@fd2:prp-function-equality).

- For \( 1 \le j < k \): \( \gamma(i_j) = i_{j+1} \), which is neither \( i_1 \) (as \( j + 1 \ge 2 \)) nor \( i_{k+1} \) (as \( j + 1 \le k \)), the entries being distinct; so \( \tau \) fixes it: \( \tau\gamma(i_j) = i_{j+1} \).
- \( \gamma(i_k) = i_1 \) and \( \tau(i_1) = i_{k+1} \): so \( \tau\gamma(i_k) = i_{k+1} \).
- \( i_{k+1} \) is not among \( i_1, \dots, i_k \), so \( \gamma \) fixes it, and \( \tau(i_{k+1}) = i_1 \): so \( \tau\gamma(i_{k+1}) = i_1 \).
- Every other point \( x \) is fixed by \( \gamma \) and by \( \tau \).

These are the values of the \( (k+1) \)-cycle (@def-cycle), which proves the claim. By \( P(k) \) and the concatenation law @prp-group-list-product-laws (a), applied to the list \( (\tau) \) and the list \( ((i_1\ i_k), \dots, (i_1\ i_2)) \),
\[
(i_1\ \cdots\ i_{k+1}) = \tau\gamma = (i_1\ i_{k+1})(i_1\ i_k) \cdots (i_1\ i_2) ,
\]
which is \( P(k + 1) \). This proves the proposition.
:::

The proof never used that the cycle starts at its smallest entry, so the formula may be applied to any way of writing the cycle. Writing \( (1\ 2\ 3) \) as \( (2\ 3\ 1) \) gives \( (2\ 1)(2\ 3) = (1\ 2)(2\ 3) \), a second word for the same permutation; we return to this below.

::: {.check}
Write \( (2\ 5\ 3) \) as a product of transpositions, and check your answer point by point.
:::

::: {.solution}
By @prp-cycle-product-of-transpositions with \( i_1 = 2 \), \( i_2 = 5 \), \( i_3 = 3 \): \( (2\ 5\ 3) = (2\ 3)(2\ 5) \). Check, applying \( (2\ 5) \) first: \( 2 \mapsto 5 \mapsto 5 \), \( 5 \mapsto 2 \mapsto 3 \), \( 3 \mapsto 3 \mapsto 2 \), and every other point is fixed. So \( 2 \mapsto 5 \), \( 5 \mapsto 3 \), \( 3 \mapsto 2 \), which is \( (2\ 5\ 3) \).
:::

## Every permutation is a product of transpositions

We say that \( \sigma \in S_n \) is a **product of transpositions** if \( \sigma = \tau_1 \tau_2 \cdots \tau_r \) for some \( r \ge 1 \) and transpositions \( \tau_1, \dots, \tau_r \in S_n \). The words "\( r \ge 1 \)" matter for one permutation only: the identity is always the empty product (@def-group-list-product), but it is a product of **at least one** transposition only when a transposition exists, that is, when \( n \ge 2 \). Then \( \id = (1\ 2)(1\ 2) \). More generally, for a set \( T \subseteq S_n \), \( \sigma \) is a **product of elements of \( T \)** if \( \sigma = t_1 t_2 \cdots t_r \) for some \( r \ge 1 \) and \( t_1, \dots, t_r \in T \), and \( T \) **generates** \( S_n \) if every \( \sigma \in S_n \) is a product of elements of \( T \). The theorem below says that the transpositions generate \( S_n \) for \( n \ge 2 \), and its corollary says the same for the adjacent transpositions.

::: {#thm-transpositions-generate}
[Transpositions Generate \( S_n \)]

Let \( n \ge 2 \). Every \( \sigma \in S_n \) is a product of transpositions.
:::

*Try it first (ten minutes): write \( (1\ 2\ 3\ 4) \) and \( (1\ 3)(2\ 4) \) as products of transpositions. Then let \( \sigma \in S_4 \) with \( \sigma(4) \ne 4 \): which single transposition \( \tau \) makes \( \tau\sigma \) fix \( 4 \)?*

::: {.idea}
The two examples are easy: the first is \( (1\ 4)(1\ 3)(1\ 2) \) by @prp-cycle-product-of-transpositions, and the second is already a product of two transpositions. They suggest a route through @thm-disjoint-cycle-decomposition, and that route works (the remark after the proof). But it hides where the transpositions come from. The second question points to a route that needs no cycles at all: induction on \( n \). What is the smaller object inside a permutation of \( n + 1 \) points? If \( \sigma \) fixes \( n + 1 \), it is really a permutation of \( \{1, \dots, n\} \), and @lem-permutations-fixing-last-point makes that precise. If not, say \( \sigma(n + 1) = k \), one swap repairs it: \( \tau \coloneqq (k\ \ n{+}1) \) sends \( k \) back to \( n + 1 \), so \( \tau\sigma \) fixes \( n + 1 \). Apply the first case to \( \tau\sigma \), then undo the swap. In one phrase: **fix one point, then induct**.

*Before reading on: why does \( \tau\sigma \) fix \( n + 1 \), and why is that the right thing to aim for?*
:::

::: {.proof}
We use @fd2:thm-induction with base \( 2 \) (read on \( \omega \) by @fd3:cor-omega-identification (b)) on \( n \ge 2 \).

*Base, \( n = 2 \).* Let \( \sigma \in S_2 \). If \( \sigma(1) = 1 \), then \( \sigma(2) \ne 1 \) since \( \sigma \) is injective, so \( \sigma(2) = 2 \) and \( \sigma = \id \) (@fd2:prp-function-equality). If \( \sigma(1) = 2 \), then \( \sigma(2) = 1 \) in the same way, and \( \sigma = (1\ 2) \). So \( S_2 = \{ \id, (1\ 2) \} \). Here \( (1\ 2) \) is one transposition and \( \id = (1\ 2)(1\ 2) \) is two.

*Step.* Let \( n \ge 2 \), suppose that every element of \( S_n \) is a product of transpositions, and let \( \sigma \in S_{n+1} \). For \( \rho \in S_n \), write \( \overline{\rho} \in S_{n+1} \) for its extension, \( \overline{\rho}(i) = \rho(i) \) for \( i \le n \) and \( \overline{\rho}(n + 1) = n + 1 \). By @lem-permutations-fixing-last-point, \( \rho \mapsto \overline{\rho} \) is the inverse of the isomorphism \( \sigma \mapsto \sigma' \) from \( S' \coloneqq \{ \sigma \in S_{n+1} : \sigma(n+1) = n + 1 \} \) onto \( S_n \); so it is an isomorphism \( S_n \to S' \) (@prp-homomorphism-composition-inverse (b)), and \( \overline{\rho\pi} = \overline{\rho}\,\overline{\pi} \) for all \( \rho, \pi \in S_n \), the product on the right being taken in \( S' \), that is, in \( S_{n+1} \).

We record two facts about the extension.

1. *It carries list products to list products:* \( \overline{\tau_1 \cdots \tau_r} = \overline{\tau_1} \cdots \overline{\tau_r} \) for every \( r \ge 1 \) and \( \tau_1, \dots, \tau_r \in S_n \). For \( r = 1 \) both sides are \( \overline{\tau_1} \). If it holds for \( r \), then by the recursion of @def-group-list-product and the homomorphism property,
\[
\overline{\tau_1 \cdots \tau_{r+1}} = \overline{(\tau_1 \cdots \tau_r)\tau_{r+1}} = \overline{\tau_1 \cdots \tau_r}\;\overline{\tau_{r+1}} = \overline{\tau_1} \cdots \overline{\tau_{r+1}} ,
\]
so it holds for \( r + 1 \) (@fd2:thm-induction with base \( 1 \)).
2. *It carries transpositions to transpositions:* for distinct \( a, b \le n \), \( \overline{(a\ b)} \) swaps \( a \) and \( b \) and fixes every other point of \( \{1, \dots, n + 1\} \), including \( n + 1 \); so it is the transposition \( (a\ b) \) of \( S_{n+1} \).

*Case 1: \( \sigma(n + 1) = n + 1 \).* Then \( \sigma \in S' \), and its restriction \( \sigma' \) lies in \( S_n \) (@lem-permutations-fixing-last-point). By the induction hypothesis, \( \sigma' = \tau_1 \cdots \tau_r \) with \( r \ge 1 \) and transpositions \( \tau_j \in S_n \). Since the two maps of the lemma are mutually inverse, \( \sigma = \overline{\sigma'} \), and by facts 1 and 2,
\[
\sigma = \overline{\sigma'} = \overline{\tau_1 \cdots \tau_r} = \overline{\tau_1} \cdots \overline{\tau_r} ,
\]
a product of \( r \) transpositions of \( S_{n+1} \).

*Case 2: \( \sigma(n + 1) = k \ne n + 1 \).* Then \( k \in \{1, \dots, n\} \), and \( \tau \coloneqq (k\ \ n{+}1) \) is a transposition of \( S_{n+1} \). Now
\[
(\tau\sigma)(n + 1) = \tau(\sigma(n + 1)) = \tau(k) = n + 1 ,
\]
so Case 1 applies to \( \tau\sigma \): \( \tau\sigma = \tau_1 \cdots \tau_r \) with \( r \ge 1 \) and transpositions \( \tau_j \in S_{n+1} \). Multiply on the left by \( \tau \), using \( \tau\tau = \id \), (G1), (G2) and the concatenation law @prp-group-list-product-laws (a):
\[
\sigma = (\tau\tau)\sigma = \tau(\tau\sigma) = \tau(\tau_1 \cdots \tau_r) = \tau\tau_1 \cdots \tau_r ,
\]
a product of \( r + 1 \) transpositions.

In both cases \( \sigma \) is a product of transpositions. This completes the induction and proves the theorem.
:::

The answer to the prompt. The transposition \( \tau = (k\ \ n{+}1) \) was chosen so that it sends \( k = \sigma(n + 1) \) back to \( n + 1 \); that is the whole computation in Case 2. Fixing \( n + 1 \) is the right aim because it is exactly the hypothesis of @lem-permutations-fixing-last-point: a permutation of \( n + 1 \) points that fixes the last one **is** a permutation of \( n \) points, and only there does the induction hypothesis speak. Case 1 also needs the restriction \( \sigma' \) to be **onto** \( \{1, \dots, n\} \), and the lemma proves this directly from \( \sigma(n + 1) = n + 1 \), with no counting.

::: {.remark}
Alternatively, @thm-disjoint-cycle-decomposition writes \( \sigma = \gamma_1 \cdots \gamma_s \) with disjoint cycles \( \gamma_j \). If \( s = 0 \), then \( \sigma = \id = (1\ 2)(1\ 2) \), using \( n \ge 2 \). Otherwise @prp-cycle-product-of-transpositions writes each \( \gamma_j \) as a product of transpositions, and the concatenation law @prp-group-list-product-laws (a) joins the words. For \( \sigma = (1\ 3)(2\ 5\ 4) \) of @exm-cycle-notation this gives \( (1\ 3)(2\ 4)(2\ 5) \).
:::

## The word is not unique

A product \( \tau_1 \cdots \tau_r \) equal to \( \sigma \) is a **word** for \( \sigma \). A permutation has many words. For the 3-cycle of the opening,
\[
(1\ 2\ 3) = (1\ 3)(1\ 2) = (1\ 2)(2\ 3) = (1\ 3)(1\ 2)(1\ 2)(1\ 2) .
\]
The first word is @exm-cycle-notation. The second is @prp-cycle-product-of-transpositions applied to \( (2\ 3\ 1) \), as above; directly, applying \( (2\ 3) \) first, \( 1 \mapsto 1 \mapsto 2 \), \( 2 \mapsto 3 \mapsto 3 \), \( 3 \mapsto 2 \mapsto 1 \). The third inserts \( (1\ 2)(1\ 2) = \id \) after the first word.

::: {.warning}
"The transpositions of \( \sigma \)" means nothing, and neither does "\( \sigma \) is a product of \( r \) transpositions, so \( r \) is determined by \( \sigma \)". The three words for \( (1\ 2\ 3) \) above have lengths \( 2 \), \( 2 \) and \( 4 \), and the first two consist of different transpositions. A word must also be read **right to left**, like every product of permutations: reversing the word \( (1\ 3)(1\ 2) \) gives \( (1\ 2)(1\ 3) = (1\ 3\ 2) \) (@exm-cycle-notation), a different permutation.
:::

Something does survive. The three lengths \( 2 \), \( 2 \), \( 4 \) above are all even. That every word for a given permutation has a length of the same parity is true, but it is not proved here: it is the theorem on the **sign** of a permutation, proved in the chapter "Determinants" of the linear algebra volume *Determinants and the Structure of Operators* and in the chapter "Symmetric Groups and the Sign of a Permutation" of *Groups*. Nothing in this chapter uses it.

::: {.second-reading title="A minimal change: 3-cycles do not generate"}
Not every kind of cycle generates \( S_n \). Change "transpositions" to "3-cycles" in the theorem, with \( n = 3 \). By @def-cycle, a 3-cycle of \( S_3 \) is \( (i_1\ i_2\ i_3) \) with \( \{i_1, i_2, i_3\} = \{1, 2, 3\} \), and rotating the written cycle shows that there are only two of them: \( (1\ 2\ 3) = (2\ 3\ 1) = (3\ 1\ 2) \) and \( (1\ 3\ 2) = (3\ 2\ 1) = (2\ 1\ 3) \). Let \( H \coloneqq \{ \id, (1\ 2\ 3), (1\ 3\ 2) \} \). Computing right to left as in @exm-cycle-notation,
\[
\begin{aligned}
(1\ 2\ 3)(1\ 2\ 3) &= (1\ 3\ 2) , & (1\ 3\ 2)(1\ 3\ 2) &= (1\ 2\ 3) , \\
(1\ 2\ 3)(1\ 3\ 2) &= \id , & (1\ 3\ 2)(1\ 2\ 3) &= \id ,
\end{aligned}
\]
and \( \id \) times anything is that thing; so \( H \) is closed under products. By induction on the length \( r \ge 1 \), using the recursion of @def-group-list-product, every product of \( r \) 3-cycles lies in \( H \). But \( (1\ 2) \notin H \). So the 3-cycles do **not** generate \( S_3 \), and the theorem depends on the kind of cycle it names.
:::

## Adjacent transpositions

Linear algebra often sorts a list by swapping **neighbors**, positions \( i \) and \( i + 1 \). The transpositions \( (i\ \ i{+}1) \), \( 1 \le i < n \), are the **adjacent** transpositions, and they are enough.

::: {#cor-adjacent-transpositions-generate}
[Adjacent Transpositions Generate \( S_n \)]

Let \( n \ge 2 \). Every \( \sigma \in S_n \) is a product of adjacent transpositions \( (i\ \ i{+}1) \), \( 1 \le i < n \).
:::

::: {.idea}
By @thm-transpositions-generate it is enough to write one transposition \( (i\ j) \), \( i < j \), with adjacent ones. Conjugating by a neighbor swap moves an endpoint one step: \( (i\ \ i{+}1)(i{+}1\ \ j)(i\ \ i{+}1) = (i\ j) \). So the gap \( j - i \) shrinks by one, and an induction on the gap finishes.
:::

::: {.proof}
First let \( 1 \le i < j \le n \) with \( j - i \ge 2 \), and put \( s \coloneqq (i\ \ i{+}1) \), \( t \coloneqq (i{+}1\ \ j) \); here \( i + 1 < j \), so \( t \) is a transposition. We check \( sts = (i\ j) \) point by point, applying the right-hand \( s \) first:
\[
\begin{aligned}
i &\mapsto i + 1 \mapsto j \mapsto j , & j &\mapsto j \mapsto i + 1 \mapsto i , \\
i + 1 &\mapsto i \mapsto i \mapsto i + 1 ,
\end{aligned}
\]
and every other point is fixed by \( s \), \( t \) and \( s \). So
\[
(i\ j) = (i\ \ i{+}1)(i{+}1\ \ j)(i\ \ i{+}1) . \tag{$\ast$}
\]

Next we prove, by @fd2:thm-induction with base \( 1 \) on \( d \), the statement \( Q(d) \): "for every \( i \ge 1 \) with \( i + d \le n \), \( (i\ \ i{+}d) \) is a product of adjacent transpositions". \( Q(1) \) holds, since \( (i\ \ i{+}1) \) is one. Suppose \( Q(d) \), and let \( i + d + 1 \le n \). By \( (\ast) \) with \( j = i + d + 1 \), \( (i\ \ i{+}d{+}1) = (i\ \ i{+}1)(i{+}1\ \ i{+}1{+}d)(i\ \ i{+}1) \), and the middle factor is a product of adjacent transpositions by \( Q(d) \), applied at \( i + 1 \). Joining the three words by @prp-group-list-product-laws (a) gives \( Q(d + 1) \).

Finally let \( \sigma \in S_n \). By @thm-transpositions-generate, \( \sigma = \tau_1 \cdots \tau_r \) with \( r \ge 1 \). Each \( \tau_j \) is \( (a\ b) = (b\ a) \) with \( a \ne b \), so it can be written as \( (i\ \ i{+}d) \) with \( i \) the smaller entry and \( d \ge 1 \) the difference; by \( Q(d) \) it is a product of adjacent transpositions. Joining these \( r \) words by @prp-group-list-product-laws (a) proves the corollary.
:::

The words this proof produces are long. Unwinding \( (\ast) \) twice, \( (1\ 4) = (1\ 2)(2\ 4)(1\ 2) \) and \( (2\ 4) = (2\ 3)(3\ 4)(2\ 3) \), so
\[
(1\ 4) = (1\ 2)(2\ 3)(3\ 4)(2\ 3)(1\ 2) .
\]
The corollary only promises that some word exists; it says nothing about the shortest one.

::: {.check}
Find a second word of adjacent transpositions for \( (1\ 4) \) in \( S_4 \), different from the one above, and check it point by point.
:::

::: {.solution}
Shrink the gap from the other end: \( (1\ 4) = (3\ 4)(1\ 3)(3\ 4) \) and \( (1\ 3) = (2\ 3)(1\ 2)(2\ 3) \), so \( (1\ 4) = (3\ 4)(2\ 3)(1\ 2)(2\ 3)(3\ 4) \). Check, applying the right-most factor first: \( 1 \mapsto 1 \mapsto 1 \mapsto 2 \mapsto 3 \mapsto 4 \); \( 4 \mapsto 3 \mapsto 2 \mapsto 1 \mapsto 1 \mapsto 1 \); \( 2 \mapsto 2 \mapsto 3 \mapsto 3 \mapsto 2 \mapsto 2 \); \( 3 \mapsto 4 \mapsto 4 \mapsto 4 \mapsto 4 \mapsto 3 \). So \( 1 \leftrightarrow 4 \) with \( 2 \), \( 3 \) fixed, which is \( (1\ 4) \). (The first step is the mirror image of \( (\ast) \): \( (i\ j) = (j{-}1\ \ j)(i\ \ j{-}1)(j{-}1\ \ j) \) for \( j - i \ge 2 \), checked in the same way.)
:::

## Exercises

### A. Check your understanding

::: {#exr-transpositions-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Where in @thm-transpositions-generate is the hypothesis \( n \ge 2 \) used? What goes wrong for \( n = 1 \)?
2. Run the proof of @thm-transpositions-generate on \( \sigma \coloneqq (1\ 3\ 4\ 2) \in S_4 \): at each stage name the case, the transposition \( \tau \) chosen, and the permutation passed down to the smaller symmetric group. Write down the word for \( \sigma \) the run produces, and check it.
3. Where does the proof use @lem-permutations-fixing-last-point, and for what?
4. State the idea of the proof in two sentences.
:::
:::

::: {.solution}
(a) In the base case. The induction starts at \( n = 2 \), where \( \id = (1\ 2)(1\ 2) \) needs a transposition to exist. For \( n = 1 \), \( S_1 = \{ \id \} \) has no transposition at all (a transposition needs two distinct points), so \( \id \) is a product of transpositions only as the empty product, which the definition of "product of transpositions" (\( r \ge 1 \)) excludes.

(b) *First stage, in \( S_4 \).* \( \sigma(4) = 2 \ne 4 \): Case 2, with \( k = 2 \) and \( \tau = (2\ 4) \). Then \( \tau\sigma \), applying \( \sigma \) first: \( 1 \mapsto 3 \mapsto 3 \), \( 3 \mapsto 4 \mapsto 2 \), \( 2 \mapsto 1 \mapsto 1 \), \( 4 \mapsto 2 \mapsto 4 \). So \( \tau\sigma = (1\ 3\ 2) \), which fixes \( 4 \), and Case 1 passes its restriction, the permutation \( (1\ 3\ 2) \) of \( \{1, 2, 3\} \), down to \( S_3 \).

*Second stage, in \( S_3 \).* \( \sigma' \coloneqq (1\ 3\ 2) \) has \( \sigma'(3) = 2 \ne 3 \): Case 2 again, with \( \tau' = (2\ 3) \). Then \( \tau'\sigma' \): \( 1 \mapsto 3 \mapsto 2 \), \( 2 \mapsto 1 \mapsto 1 \), \( 3 \mapsto 2 \mapsto 3 \). So \( \tau'\sigma' = (1\ 2) \), which fixes \( 3 \); Case 1 passes \( (1\ 2) \in S_2 \) down.

*Base, in \( S_2 \).* \( (1\ 2) \) is one transposition.

*Back up.* \( \tau'\sigma' = (1\ 2) \) gives \( \sigma' = \tau'(1\ 2) = (2\ 3)(1\ 2) \), and then \( \sigma = \tau(\tau\sigma) = (2\ 4)(2\ 3)(1\ 2) \), each transposition read in \( S_4 \) by fact 2 of the proof. Check, applying \( (1\ 2) \) first: \( 1 \mapsto 2 \mapsto 3 \mapsto 3 \), \( 3 \mapsto 3 \mapsto 2 \mapsto 4 \), \( 4 \mapsto 4 \mapsto 4 \mapsto 2 \), \( 2 \mapsto 1 \mapsto 1 \mapsto 1 \). So \( 1 \mapsto 3 \mapsto 4 \mapsto 2 \mapsto 1 \), which is \( (1\ 3\ 4\ 2) \).

The second route of the remark after the theorem gives another word: by @prp-cycle-product-of-transpositions, \( (1\ 3\ 4\ 2) = (1\ 2)(1\ 4)(1\ 3) \) (check: \( 1 \mapsto 3 \mapsto 3 \mapsto 3 \), \( 3 \mapsto 1 \mapsto 4 \mapsto 4 \), \( 4 \mapsto 4 \mapsto 1 \mapsto 2 \), \( 2 \mapsto 2 \mapsto 2 \mapsto 1 \)). That is a correct word, but it is not the run asked for. Neither is \( (2\ 4)(1\ 2)(1\ 3) \), which applies one Case-2 step and then the cycle formula to \( \tau\sigma = (1\ 3\ 2) \); it is a third valid word.

(c) In two places. In the paragraph opening the Step, part (b) of the lemma says that \( \rho \mapsto \overline{\rho} \) is the inverse of the isomorphism \( \sigma \mapsto \sigma' \) from \( S' \) onto \( S_n \); so, by @prp-homomorphism-composition-inverse (b), the extension is a homomorphism, the product of extensions being taken in \( S_{n+1} \). Fact 1 rests on this. In Case 1, part (a) says that a permutation \( \sigma \) of \( \{1, \dots, n + 1\} \) fixing \( n + 1 \) restricts to a permutation \( \sigma' \) of \( \{1, \dots, n\} \), to which the induction hypothesis applies, and part (b) says that extending \( \sigma' \) back gives \( \sigma \), so that the extension carries the word for \( \sigma' \) to a word for \( \sigma \).

(d) Induct on \( n \): a permutation that fixes the last point is a permutation of one point fewer, so the induction hypothesis writes it as transpositions. A permutation that moves the last point is brought to that case by one transposition, which is then undone.
:::

### B. Practice

::: {#exr-transpositions-b1}
[B1]

Write \( (1\ 2\ 3\ 4\ 5) \) and \( (1\ 5)(2\ 4) \) as products of transpositions, and then as products of adjacent transpositions. Check one of your adjacent words point by point.
:::

::: {.solution}
*Transpositions.* By @prp-cycle-product-of-transpositions, \( (1\ 2\ 3\ 4\ 5) = (1\ 5)(1\ 4)(1\ 3)(1\ 2) \). The permutation \( (1\ 5)(2\ 4) \) is already a product of two transpositions.

*Adjacent transpositions.* A word of neighbor swaps for the 5-cycle can be checked directly:
\[
(1\ 2\ 3\ 4\ 5) = (1\ 2)(2\ 3)(3\ 4)(4\ 5) .
\]
Check, applying \( (4\ 5) \) first: \( 1 \mapsto 1 \mapsto 1 \mapsto 1 \mapsto 2 \); \( 2 \mapsto 2 \mapsto 2 \mapsto 3 \mapsto 3 \); \( 3 \mapsto 3 \mapsto 4 \mapsto 4 \mapsto 4 \); \( 4 \mapsto 5 \mapsto 5 \mapsto 5 \mapsto 5 \); \( 5 \mapsto 4 \mapsto 3 \mapsto 2 \mapsto 1 \). So \( 1 \mapsto 2 \mapsto 3 \mapsto 4 \mapsto 5 \mapsto 1 \), as required.

For \( (1\ 5)(2\ 4) \), use \( (\ast) \) of the corollary's proof repeatedly: \( (1\ 5) = (1\ 2)(2\ 5)(1\ 2) \), \( (2\ 5) = (2\ 3)(3\ 5)(2\ 3) \), \( (3\ 5) = (3\ 4)(4\ 5)(3\ 4) \), and \( (2\ 4) = (2\ 3)(3\ 4)(2\ 3) \). Joining the words (@prp-group-list-product-laws (a)),
\[
\begin{aligned}
(1\ 5)(2\ 4) = {} & (1\ 2)(2\ 3)(3\ 4)(4\ 5)(3\ 4)(2\ 3)(1\ 2) \\
& \cdot (2\ 3)(3\ 4)(2\ 3) ,
\end{aligned}
\]
a word of ten adjacent transpositions.
:::

::: {#exr-transpositions-b2}
[B2]

Let \( n \ge 2 \) and \( \rho \coloneqq (1\ 2\ \cdots\ n) \in S_n \) (for \( n = 2 \), \( \rho = (1\ 2) \)).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \sigma(a\ b)\sigma^{-1} = (\sigma(a)\ \sigma(b)) \) for every \( \sigma \in S_n \) and every transposition \( (a\ b) \in S_n \).
2. Prove that \( \rho^{i-1}(1\ 2)\rho^{-(i-1)} = (i\ \ i{+}1) \) for \( 1 \le i \le n - 1 \).
3. Deduce that every \( \sigma \in S_n \) is a product of factors each equal to \( (1\ 2) \), \( \rho \) or \( \rho^{-1} \).
:::
:::

::: {.solution}
(a) The points \( \sigma(a) \), \( \sigma(b) \) are distinct, since \( \sigma \) is injective, so the right-hand side is a transposition. Check point by point, applying \( \sigma^{-1} \) first. For \( x = \sigma(a) \): \( \sigma^{-1}(x) = a \mapsto b \mapsto \sigma(b) \). For \( x = \sigma(b) \): \( \sigma^{-1}(x) = b \mapsto a \mapsto \sigma(a) \). For any other \( x \): \( \sigma^{-1}(x) \notin \{a, b\} \) (otherwise \( x = \sigma(\sigma^{-1}(x)) \) would be \( \sigma(a) \) or \( \sigma(b) \)), so \( (a\ b) \) fixes it, and \( \sigma(\sigma^{-1}(x)) = x \). These are the values of \( (\sigma(a)\ \sigma(b)) \) (@fd2:prp-function-equality).

(b) First, \( \rho^m(j) = j + m \) whenever \( m \in \nN \), \( j \ge 1 \) and \( j + m \le n \). By induction on \( m \): \( \rho^0 = \id \); and if it holds for \( m \) and \( j + m + 1 \le n \), then \( \rho^{m+1} = \rho^m \rho \) (@def-group-integer-power), so \( \rho^{m+1}(j) = \rho^m(j + 1) = j + 1 + m \), using \( \rho(j) = j + 1 \) for \( j < n \) (@def-cycle). Now let \( 1 \le i \le n - 1 \) and \( \sigma \coloneqq \rho^{i-1} \). Then \( \sigma(1) = i \) and \( \sigma(2) = i + 1 \), since \( 2 + (i - 1) \le n \), and \( \sigma^{-1} = \rho^{-(i-1)} \) by @prp-group-power-laws (b). By (a), \( \rho^{i-1}(1\ 2)\rho^{-(i-1)} = (i\ \ i{+}1) \).

(c) By @cor-adjacent-transpositions-generate, \( \sigma \) is a product of adjacent transpositions. By (b), each \( (i\ \ i{+}1) \) equals \( \rho^{i-1}(1\ 2)\rho^{-(i-1)} \), where \( \rho^{i-1} \) is the product of \( i - 1 \) factors \( \rho \) and \( \rho^{-(i-1)} = (\rho^{-1})^{i-1} \) the product of \( i - 1 \) factors \( \rho^{-1} \) (@def-group-integer-power, @prp-group-power-laws (b)). Joining all these words by @prp-group-list-product-laws (a) writes \( \sigma \) as required.
:::

### C. Going deeper

::: {#exr-transpositions-c1}
[C1: Exit check: transpositions generate]

Let \( n \ge 2 \). State and prove that every \( \sigma \in S_n \) is a product of transpositions.
:::

::: {.solution}
*Statement.* For \( n \ge 2 \), every \( \sigma \in S_n \) is \( \tau_1 \cdots \tau_r \) for some \( r \ge 1 \) and transpositions \( \tau_j \in S_n \) (@thm-transpositions-generate).

*Proof.* Induction on \( n \ge 2 \) (@fd2:thm-induction with base \( 2 \)). For \( n = 2 \), a bijection \( \sigma \) of \( \{1, 2\} \) has \( \sigma(1) = 1 \), and then \( \sigma(2) = 2 \) by injectivity, or \( \sigma(1) = 2 \) and \( \sigma(2) = 1 \); so \( S_2 = \{ \id, (1\ 2) \} \), and \( \id = (1\ 2)(1\ 2) \).

Suppose the statement for \( n \ge 2 \), and let \( \sigma \in S_{n+1} \).

If \( \sigma(n + 1) = n + 1 \), then \( \sigma(i) \ne n + 1 \) for \( i \le n \) by injectivity, so \( \sigma \) restricts to an injective map \( \sigma' \colon \{1, \dots, n\} \to \{1, \dots, n\} \). It is onto: for \( j \le n \), \( j = \sigma(i) \) for some \( i \), and \( i \ne n + 1 \) because \( \sigma(n + 1) = n + 1 \ne j \). So \( \sigma' \in S_n \) (@lem-permutations-fixing-last-point), and \( \sigma' = \tau_1 \cdots \tau_r \) by the hypothesis. Extending each permutation of \( \{1, \dots, n\} \) by \( n + 1 \mapsto n + 1 \) is the inverse of the restriction isomorphism of @lem-permutations-fixing-last-point (b), so it is a homomorphism (@prp-homomorphism-composition-inverse (b)). By induction on \( r \), using the recursion of @def-group-list-product (fact 1 in the proof of @thm-transpositions-generate), it carries this word to the word \( \overline{\tau_1} \cdots \overline{\tau_r} \) in \( S_{n+1} \), each \( \overline{\tau_j} \) the transposition of the same two points; and it carries \( \sigma' \) to \( \sigma \). Hence \( \sigma = \overline{\tau_1} \cdots \overline{\tau_r} \).

If \( \sigma(n + 1) = k \ne n + 1 \), let \( \tau \coloneqq (k\ \ n{+}1) \). Then \( (\tau\sigma)(n + 1) = \tau(k) = n + 1 \), so by the first case \( \tau\sigma = \tau_1 \cdots \tau_r \) with transpositions in \( S_{n+1} \). Since \( \tau\tau = \id \), \( \sigma = \tau(\tau\sigma) = \tau\tau_1 \cdots \tau_r \). This completes the induction.

**Marking scheme.** (10 points)

- 2: sets up induction on \( n \) with base \( n = 2 \), and handles \( S_2 \), including \( \id \) as a product of transpositions.
- 3: Case \( \sigma(n + 1) = n + 1 \): reduces to \( S_n \), with the restriction shown to be a permutation of \( \{1, \dots, n\} \) (surjectivity justified, or @lem-permutations-fixing-last-point cited).
- 3: Case \( \sigma(n + 1) = k \ne n + 1 \): chooses a transposition \( \tau \) with \( \tau\sigma \) fixing \( n + 1 \), and computes \( (\tau\sigma)(n + 1) = n + 1 \).
- 1: undoes \( \tau \), using \( \tau^{-1} = \tau \).
- 1: says why transpositions of \( S_n \), extended, are transpositions of \( S_{n+1} \) and the extended word still equals \( \sigma \).

Fatal errors (0 for the step): using "\( \sigma \) is a product of transpositions in \( S_{n+1} \)" inside its own proof (circular); assuming the cycle decomposition or the cycle formula without citing it as proved.

**Second route (accepted, 10 points).**

- 3: cites @thm-disjoint-cycle-decomposition as proved, writing \( \sigma \) as a product of disjoint cycles.
- 3: writes each cycle as transpositions by @prp-cycle-product-of-transpositions, cited or proved, with the factors in the right (right-to-left) order.
- 2: handles \( \sigma = \id \) as \( (1\ 2)(1\ 2) \), using \( n \ge 2 \).
- 2: joins the words into one product of transpositions (@prp-group-list-product-laws (a)).

**Third route (accepted, 10 points): strong induction on \( \card{\supp \sigma} \)** (finite, as a subset of \( \{1, \dots, n\} \)).

- 2: sets up the induction and handles the base \( \supp \sigma = \emptyset \), that is, \( \sigma = \id = (1\ 2)(1\ 2) \), using \( n \ge 2 \).
- 3: for \( \sigma \ne \id \), picks \( i \) with \( j \coloneqq \sigma(i) \ne i \) and \( \tau \coloneqq (i\ j) \), and shows that \( \tau\sigma \) fixes \( i \) and every point that \( \sigma \) fixes (such a point is neither \( i \) nor \( j \), by injectivity).
- 3: concludes \( \supp(\tau\sigma) \subseteq \supp \sigma \setminus \{i\} \), so the hypothesis applies to \( \tau\sigma \) (or \( \tau\sigma = \id \), and \( \sigma = \tau \)).
- 1: undoes \( \tau \), using \( \tau^{-1} = \tau \).
- 1: joins the words (@prp-group-list-product-laws (a)).
:::

::: {#exr-transpositions-c2}
[C2: Find the error]

Here is an argument.

> **Claim.** Every cycle is a product of transpositions.
>
> **Proof.** (1) Let \( \gamma = (i_1\ i_2\ \cdots\ i_k) \) with \( k \ge 2 \) and distinct entries. (2) The cycle sends \( i_1 \) to \( i_2 \), then \( i_2 \) to \( i_3 \), and so on, up to \( i_k \), which it sends back to \( i_1 \). (3) The swap \( (i_1\ i_2) \) takes \( i_1 \) to \( i_2 \); the swap \( (i_1\ i_3) \) is next; and so on. (4) Hence \( \gamma = (i_1\ i_2)(i_1\ i_3) \cdots (i_1\ i_k) \). (5) So \( \gamma \) is a product of \( k - 1 \) transpositions.

Is the claim true? Does the argument prove it? Name the line that fails and the reason, give a counterexample to the illegal step, and repair the argument.
:::

::: {.solution}
**The claim is true:** it is @prp-cycle-product-of-transpositions. **The argument does not prove it.**

*Line (4) fails*, on the strength of line (3). Line (3) lists the transpositions in the order in which they should **act**, and line (4) writes them left to right in that order. But a product of permutations acts right to left (@def-symmetric-group): in \( (i_1\ i_2)(i_1\ i_3) \cdots (i_1\ i_k) \) the factor \( (i_1\ i_k) \) acts first. The equation of line (4) is an unproved "fact", and a false one: entry (N9) of @fd1:exm-not-allowed-catalogue. Lines (1), (2) and (5) are correct.

*Counterexample to the step.* For \( k = 3 \) and \( \gamma = (1\ 2\ 3) \), line (4) claims \( (1\ 2\ 3) = (1\ 2)(1\ 3) \). But \( (1\ 2)(1\ 3) = (1\ 3\ 2) \) (@exm-cycle-notation), and \( (1\ 3\ 2) \ne (1\ 2\ 3) \), since the first sends \( 1 \) to \( 3 \) and the second sends \( 1 \) to \( 2 \). There is no counterexample to the conclusion.

In fact the product in line (4) is \( \gamma^{-1} \): by @prp-group-list-product-laws (c), the inverse of \( (i_1\ i_k) \cdots (i_1\ i_2) = \gamma \) is the reversed product of the inverses, and each transposition is its own inverse.

*Repair.* Reverse the order of the factors: \( \gamma = (i_1\ i_k)(i_1\ i_{k-1}) \cdots (i_1\ i_2) \), and prove it as in @prp-cycle-product-of-transpositions, by induction on \( k \) with a point-by-point check of \( (i_1\ i_{k+1})(i_1\ \cdots\ i_k) = (i_1\ \cdots\ i_{k+1}) \).

**Marking scheme.** (10 points)

- 2: says the claim is true and the argument does not prove it.
- 3: names line (4) (or lines (3)–(4) together) and the reason: the factors are written in the order they should act, but products act right to left.
- 2: a counterexample to the step, such as \( (1\ 2)(1\ 3) = (1\ 3\ 2) \ne (1\ 2\ 3) \).
- 3: gives a correct formula for \( \gamma \) as a product of transpositions and justifies it. For the reversed product \( (i_1\ i_k) \cdots (i_1\ i_2) \), the induction or a citation of @prp-cycle-product-of-transpositions is enough. For another word, such as \( (i_1\ i_2)(i_2\ i_3) \cdots (i_{k-1}\ i_k) \), the reader must prove it, by induction on \( k \) or by a point-by-point check for general \( k \).

Fatal errors (0 for the step): a counterexample to the conclusion (there is none); a "repair" that keeps line (4)'s product and silently replaces \( \gamma \) by another cycle (such as \( \gamma^{-1} \)).
:::

::: {#exr-transpositions-c3}
[C3]

::: {.enumerate options="label=(\alph*)"}
1. Let \( \sigma \in S_n \) and let \( (i_1\ \cdots\ i_k) \in S_n \) be a cycle. Prove that \( \sigma (i_1\ \cdots\ i_k) \sigma^{-1} = (\sigma(i_1)\ \cdots\ \sigma(i_k)) \).
2. Deduce that any two transpositions of \( S_n \) are conjugate: for transpositions \( \tau, \tau' \) there is \( \pi \in S_n \) with \( \tau' = \pi\tau\pi^{-1} \).
:::
:::

::: {.solution}
(a) Write \( \gamma \coloneqq (i_1\ \cdots\ i_k) \), and read indices so that \( i_{k+1} \) means \( i_1 \). The points \( \sigma(i_1), \dots, \sigma(i_k) \) are distinct, since \( \sigma \) is injective, so the right-hand side is a \( k \)-cycle. For \( x = \sigma(i_j) \): \( \sigma^{-1}(x) = i_j \mapsto i_{j+1} \mapsto \sigma(i_{j+1}) \). For \( x \) not among the \( \sigma(i_j) \): \( \sigma^{-1}(x) \) is not among the \( i_j \), so \( \gamma \) fixes it, and \( \sigma\gamma\sigma^{-1}(x) = x \). These are the values of \( (\sigma(i_1)\ \cdots\ \sigma(i_k)) \).

(b) Here \( n \ge 2 \), since a transposition exists. First, every transposition \( (a\ b) \), written with \( a < b \), is conjugate to \( (1\ 2) \): by (a) it suffices to find \( \pi \) with \( \pi(1) = a \), \( \pi(2) = b \). If \( (a, b) = (1, 2) \), take \( \pi = \id \). If \( a = 1 \) and \( b \ge 3 \), take \( \pi = (2\ b) \). If \( a \ge 2 \), then \( b \ge 3 \); take \( \pi = (1\ a)(2\ b) \): applying \( (2\ b) \) first, \( 1 \mapsto 1 \mapsto a \), and \( 2 \mapsto b \mapsto b \), since \( b \ne 1 \) and \( b \ne a \). Now let \( \tau = \pi(1\ 2)\pi^{-1} \) and \( \tau' = \pi'(1\ 2)\pi'^{-1} \). Then \( (1\ 2) = \pi^{-1}\tau\pi \), and
\[
\tau' = \pi'\pi^{-1}\tau\pi\pi'^{-1} = (\pi'\pi^{-1})\tau(\pi'\pi^{-1})^{-1} ,
\]
by @prp-group-list-product-laws (c) and @thm-group-basic-properties (3). Conjugacy in \( S_n \) is studied in the chapter "Symmetric Groups and the Sign of a Permutation" of *Groups*.

**Marking scheme.** (10 points)

- 2: notes that the \( \sigma(i_j) \) are distinct (\( \sigma \) injective), so the right side of (a) is a \( k \)-cycle.
- 2: checks \( \sigma\gamma\sigma^{-1}(\sigma(i_j)) = \sigma(i_{j+1}) \), including the wrap-around \( j = k \).
- 2: checks that every \( x \) outside \( \{\sigma(i_1), \dots, \sigma(i_k)\} \) is fixed.
- 3: for transpositions \( (a\ b) \), \( (c\ d) \), exhibits a permutation \( \pi \) with \( \{\pi(a), \pi(b)\} = \{c, d\} \), covering every case of overlap between \( \{a, b\} \) and \( \{c, d\} \); directly or through \( (1\ 2) \).
- 1: applies (a) with \( k = 2 \) to conclude \( \tau' = \pi\tau\pi^{-1} \), or composes the two conjugations by \( (1\ 2) \) using \( (\pi'\pi^{-1})^{-1} = \pi\pi'^{-1} \).

Fatal errors (0 for the step): a proof of (a) that only asserts the formula (0 for the three (a) items); \( \pi \) is not a bijection, or is built only for disjoint (or only for overlapping) pairs. Part (b) may use (a) even where (a) was not proved.
:::

### R. Review

::: {#exr-transpositions-r1}
[R1]

Let \( F \) be a field. Show that \( \varphi(k) \coloneqq k \cdot 1_F \) defines a homomorphism \( (\nZ, +) \to (F, +) \), that \( \ker \varphi = m\nZ \) for exactly one \( m \in \nN \), and that this \( m \) is \( 0 \) or a prime.
:::

::: {.solution}
*Homomorphism.* In additive notation, @prp-group-power-laws (a) says \( (k + l) \cdot 1_F = k \cdot 1_F + l \cdot 1_F \) for all \( k, l \in \nZ \), the multiples being those of the group \( (F, +) \) (@def-group-integer-power). That is \( \varphi(k + l) = \varphi(k) + \varphi(l) \). By @prp-group-power-laws (e), for \( k \in \nN \) these group multiples are the multiples of *Number Systems: From \(\nN\) to \(\nR\)*, Section 2.3, which are the multiples of @lem-integer-multiples; that lemma is applied below only to natural numbers.

*Kernel.* \( \ker \varphi \) is a subgroup of \( \nZ \) (@thm-homomorphism-basic-properties (c)), so \( \ker \varphi = m\nZ \) for exactly one \( m \in \nN \) (@thm-subgroups-of-integers): \( m = 0 \) if the kernel is \( \{0\} \), and otherwise \( m \) is its least positive element.

*\( m \) is \( 0 \) or prime.* \( m \ne 1 \): \( 1 \cdot 1_F = 1_F \) (@def-group-integer-power), and \( 1_F \ne 0_F \) in a field (@fd3:def-commutative-ring-and-field), so \( 1 \notin \ker \varphi \). Suppose \( m \ge 2 \) were not prime. By @fd2:def-prime it has a positive divisor \( a \notin \{1, m\} \); write \( m = ab \) with \( b \in \nZ \). Then \( b > 0 \), as \( a, m > 0 \); \( a \le m \) and \( b \le m \) by @fd3:prp-divisibility-rules-integers (e); and \( b \ne m \), since \( b = m \) would give \( a = 1 \) (cancel \( m \ne 0 \) in \( \nZ \)). So \( 0 < a < m \) and \( 0 < b < m \). By @lem-integer-multiples (b),
\[
(a \cdot 1_F)(b \cdot 1_F) = (ab) \cdot 1_F = m \cdot 1_F = 0_F .
\]
But \( a \notin m\nZ \): if \( m \mid a \) with \( a > 0 \), then \( m \le a \) by @fd3:prp-divisibility-rules-integers (e), against \( a < m \). So \( a \cdot 1_F \ne 0_F \), and in the same way \( b \cdot 1_F \ne 0_F \). A field has no zero divisors (@thm-field-basic-properties (f)): a contradiction. So \( m \) is \( 0 \) or prime.

This is a group-theoretic route to Chapter 2's characteristic. The number \( m \) is \( \operatorname{char} F \) (@def-characteristic): if \( m > 0 \) it is the least positive \( n \) with \( n \cdot 1_F = 0_F \), and \( m = 0 \) exactly when there is none. The result is @thm-characteristic-prime, whose proof there runs the same argument without the language of kernels.
:::

::: {#exr-transpositions-r2}
[R2]

Show that \( (\nZ/6\nZ, +) \cong ((\nZ/7\nZ)^{\times}, \cdot) \), and that \( (\nZ/6\nZ, +) \cong \nZ/2\nZ \times \nZ/3\nZ \).
:::

::: {.solution}
*The first isomorphism.* By @fd3:thm-integers-mod-prime-field, \( \nZ/7\nZ \) is a field, so every non-zero class is a unit, while \( [0] \) is not (\( [0][x] = [0] \ne [1] \)). So the units are the six classes \( [1], \dots, [6] \), distinct by @fd3:thm-integers-mod-n-ring (b), and they form a group by @prp-units-form-group. Compute the powers of \( [3] \):
\[
[3]^0, [3]^1, \dots, [3]^5 = [1], [3], [2], [6], [4], [5] ,
\]
from \( 3 \cdot 3 = 9 = 7 + 2 \), \( 2 \cdot 3 = 6 \), \( 6 \cdot 3 = 18 = 14 + 4 \), \( 4 \cdot 3 = 12 = 7 + 5 \), and then \( [3]^6 = [5][3] = [15] = [1] \).

Define \( f([k]) \coloneqq [3]^k \). *Well defined:* if \( [k] = [k'] \) in \( \nZ/6\nZ \), then \( k' = k + 6q \) with \( q \in \nZ \), and by @prp-group-power-laws (a), (c),
\[
[3]^{k'} = [3]^k ([3]^6)^q = [3]^k [1]^q = [3]^k ,
\]
since every power of the identity is the identity (@def-group-integer-power, by induction on \( q \in \nN \), and for \( q < 0 \) because \( [1]^{-1} = [1] \)). *A homomorphism:* \( f([k] + [l]) = f([k + l]) = [3]^{k+l} = [3]^k[3]^l = f([k])f([l]) \), by @prp-group-power-laws (a). *Bijective:* the six classes \( [0], \dots, [5] \) of \( \nZ/6\nZ \) (@fd3:thm-integers-mod-n-ring (b)) go to the six distinct units listed above, which are all of \( (\nZ/7\nZ)^{\times} \). So \( f \) is an isomorphism (@def-group-homomorphism).

*The second isomorphism.* \( 1 = 3 \cdot 1 + 2 \cdot (-1) \), so \( 2 \) and \( 3 \) are coprime (@fd3:cor-coprime-iff-combination). By @exm-group-homomorphisms (e), which rests on @fd3:thm-chinese-remainder-two (b), \( [x]_6 \mapsto ([x]_2, [x]_3) \) is an isomorphism of additive groups \( \nZ/6\nZ \to \nZ/2\nZ \times \nZ/3\nZ \).

The method is that of @exm-isomorphic-small-groups (b), where \( [2] \) played the role of \( [3] \) modulo \( 5 \).
:::

::: {#exr-transpositions-r3}
[R3]

Let \( X \) be a set. Show that the permutations \( \sigma \in S_X \) with \( \supp \sigma \) finite form a subgroup of \( S_X \).
:::

::: {.solution}
Let \( H \coloneqq \{ \sigma \in S_X : \supp \sigma \text{ is finite} \} \). We use @thm-subgroup-test. \( H \ne \emptyset \): \( \supp \id_X = \emptyset \), which has \( 0 \) elements (@fd2:def-finite).

Let \( \sigma, \tau \in H \). If \( x \notin \supp \sigma \cup \supp \tau \), then \( \tau(x) = x \), so \( \tau^{-1}(x) = x \), and \( \sigma(x) = x \); hence \( \sigma\tau^{-1}(x) = x \). So
\[
\supp(\sigma\tau^{-1}) \subseteq \supp \sigma \cup \supp \tau = \supp \sigma \cup (\supp \tau \setminus \supp \sigma) .
\]
The set \( \supp \tau \setminus \supp \sigma \) is finite, as a subset of the finite set \( \supp \tau \) (@fd2:prp-subset-finite); it is disjoint from \( \supp \sigma \), so the union is finite (@fd2:prp-disjoint-union-count); and \( \supp(\sigma\tau^{-1}) \), a subset of it, is finite (@fd2:prp-subset-finite). So \( \sigma\tau^{-1} \in H \), and \( H \) is a subgroup.

For an infinite \( X \) the subgroup can be proper. On \( X = \nZ \), the translation \( \sigma(x) \coloneqq x + 1 \) is a bijection (its inverse is \( x \mapsto x - 1 \)) that moves every point, since \( x + 1 \ne x \). Its support \( \nZ \) is not finite: \( x \mapsto 2x \) is a bijection from \( \nZ \) onto \( 2\nZ \) (injective by cancellation, @fd3:prp-ordered-ring-rules (f)), and \( 2\nZ \ne \nZ \) since \( 1 \notin 2\nZ \) (@fd3:prp-divisibility-rules-integers (g)), which a finite set does not allow (@fd2:thm-finite-no-proper-copy).
:::

::: {#exr-transpositions-r4}
[R4]

Let \( G \) be a finite group with an even number of elements. Prove that some \( g \in G \) with \( g \ne e \) has \( g^2 = e \).
:::

::: {.solution}
The tool is to pair each element with its inverse. Define \( g \sim h \) on \( G \) by \( h \in \{ g, g^{-1} \} \). It is an equivalence relation (@fd2:def-equivalence-relation): reflexive since \( g \in \{g, g^{-1}\} \); symmetric since \( h = g^{-1} \) gives \( g = h^{-1} \) (@thm-group-basic-properties (3)); transitive since \( h \in \{g, g^{-1}\} \) and \( k \in \{h, h^{-1}\} \) give \( k \in \{g, g^{-1}, (g^{-1})^{-1}\} = \{g, g^{-1}\} \). The class of \( g \) is \( \{g, g^{-1}\} \), and the classes partition \( G \) (@fd2:thm-classes-partition).

A class has one element exactly when \( g = g^{-1} \), that is, when \( g^2 = e \): if \( g = g^{-1} \), then \( g^2 = gg^{-1} = e \); if \( g^2 = e \), then \( g \) is an inverse of \( g \), so \( g = g^{-1} \) by uniqueness of inverses (@thm-group-basic-properties (2)). Let \( T \coloneqq \{ g \in G : g^2 = e \} \), the union of the one-element classes, and \( U \coloneqq G \setminus T \), the union of the two-element classes; both are finite, as subsets of \( G \) (@fd2:prp-subset-finite).

*\( \card{U} \) is even.* We show, by @fd1:thm-strong-induction on \( j \), that every subset \( V \subseteq U \) with \( j \) elements that contains \( g^{-1} \) whenever it contains \( g \) has an even number of elements. If \( j = 0 \), this holds. If \( j \ge 1 \), pick \( g \in V \); then \( g^{-1} \in V \) and \( g^{-1} \ne g \) (as \( g \notin T \)), so \( \{g, g^{-1}\} \) has \( 2 \) elements, and \( V' \coloneqq V \setminus \{g, g^{-1}\} \) again contains the inverse of each of its elements: if \( h \in V' \), then \( h^{-1} \in V \), and \( h^{-1} \notin \{g, g^{-1}\} \), since otherwise \( h = (h^{-1})^{-1} \in \{g^{-1}, g\} \) by @thm-group-basic-properties (3). As \( V \) is the disjoint union of \( V' \) and \( \{g, g^{-1}\} \), \( j = \card{V'} + 2 \) (@fd2:prp-disjoint-union-count with @fd2:cor-finite-size-unique), so \( V' \) has \( j - 2 < j \) elements; that number is even by the hypothesis, so \( j \) is even. Apply this to \( V = U \).

*Conclusion.* \( G = T \cup U \) is a disjoint union, so \( \card{G} = \card{T} + \card{U} \) (@fd2:prp-disjoint-union-count). With \( \card{G} \) and \( \card{U} \) even, \( \card{T} = \card{G} - \card{U} \) is even. Since \( e \in T \), \( \card{T} \ge 1 \), so \( \card{T} \ge 2 \): an even number cannot be \( 1 \), as \( 2 \nmid 1 \) (@fd3:prp-divisibility-rules-integers (g)). So \( T \) contains some \( g \ne e \), and \( g^2 = e \).

*Look-alikes.* Lagrange's theorem (the chapter "Cosets and Lagrange's Theorem" of *Groups*) and Cauchy's theorem (the chapter "Group Actions, the Orbit–Stabilizer Theorem, and the Class Equation" of *Groups*) would give this, but neither is available here. "Pick \( g \ne e \) and square it" does not work: in \( (\nZ/6\nZ, +) \), where the condition reads \( 2 \cdot g = [0] \), the element \( g = [1] \) has \( 2 \cdot [1] = [2] \ne [0] \); the element that works there is \( [3] \), and the pairing argument shows that such an element exists without searching for it.
:::

<!-- dependency ledger
prp-cycle-product-of-transpositions (proof): induction from base 2 on k | fd2:thm-induction read on omega by fd3:cor-omega-identification (b), cited
prp-cycle-product-of-transpositions (proof): j + 1 >= 2, j + 1 <= k for 1 <= j < k; i_{k+1} not among i_1..i_k | distinctness hypothesis; order of N, discreteness fd3:thm-integers-ordered-ring (c); inline
prp-cycle-product-of-transpositions (claim): (a b) = (b a); (a b)(a b) = id | def-cycle, fd2:prp-function-equality; inline pointwise check
prp-cycle-product-of-transpositions (example): (1 2 3 4) = (1 4)(1 3)(1 2); rotation (2 3 1) gives (1 2)(2 3); quick check (2 5 3) = (2 3)(2 5) | verify/ch03/prp-cycle-product-of-transpositions.py (k <= 7)
thm-transpositions-generate (proof): base S_2 = {id, (1 2)} by cases on sigma(1) | inline (injectivity, fd2:prp-function-equality); agrees with prp-symmetric-group-order for n = 2, not cited
thm-transpositions-generate (proof): k = sigma(n+1) != n+1 lies in {1..n} | codomain {1..n+1}; inline
thm-transpositions-generate (proof): extension map is a homomorphism | lem-permutations-fixing-last-point (inverse of the restriction isomorphism), prp-homomorphism-composition-inverse (b), cited
thm-transpositions-generate (proof): extension carries list products to list products | inline induction from base 1 (fd2:thm-induction) with def-group-list-product
thm-transpositions-generate (proof): tau tau = id, then sigma = tau(tau sigma) | (G1), (G2) of def-group; the fact stated before prp-cycle-product-of-transpositions; prp-group-list-product-laws (a)
thm-transpositions-generate (claim): (remark) sigma = (1 3)(2 5 4) gives (1 3)(2 4)(2 5) | verify/ch03/thm-transpositions-generate.py
thm-transpositions-generate (claim): (1 2 3) = (1 3)(1 2) = (1 2)(2 3) = (1 3)(1 2)(1 2)(1 2); lengths 2, 2, 4; reversal (1 2)(1 3) = (1 3 2) | exm-cycle-notation; verify/ch03/thm-transpositions-generate.py
thm-transpositions-generate (claim): parity of word lengths is an invariant | NOT proved here; prose pointer to LA2.7 and AL1.3; nothing depends on it
thm-transpositions-generate (claim): (non-example) the two 3-cycles of S_3 and the products in H; (1 2) not in H; closure gives all products of 3-cycles by induction | verify/ch03/thm-transpositions-generate.py; inline induction with def-group-list-product
cor-adjacent-transpositions-generate (proof): s t s = (i j) pointwise | inline; verify/ch03/cor-adjacent-transpositions-generate.py (n <= 5)
cor-adjacent-transpositions-generate (proof): induction from base 1 on the gap d | fd2:thm-induction read on omega, cited
cor-adjacent-transpositions-generate (claim): (1 4) = (1 2)(2 3)(3 4)(2 3)(1 2); quick check (3 4)(2 3)(1 2)(2 3)(3 4) and the mirror formula | verify/ch03/cor-adjacent-transpositions-generate.py
exr-transpositions-a1 (solution): (c) the lemma makes the extension a homomorphism and supplies restriction/extension in Case 1 | lem-permutations-fixing-last-point (a), (b), prp-homomorphism-composition-inverse (b), cited
exr-transpositions-a1 (solution): the run on (1 3 4 2): tau sigma = (1 3 2), tau' sigma' = (1 2), word (2 4)(2 3)(1 2); second-route word (1 2)(1 4)(1 3); third word (2 4)(1 2)(1 3) | verify/ch03/exr-transpositions-a1.py
exr-transpositions-b1 (solution): (1 2 3 4 5) = (1 5)(1 4)(1 3)(1 2) = (1 2)(2 3)(3 4)(4 5); ten-factor word for (1 5)(2 4) | verify/ch03/exr-transpositions-b1.py
exr-transpositions-b2 (solution): rho^m(j) = j + m for j + m <= n | inline induction (def-group-integer-power); verify/ch03/exr-transpositions-b2.py (n <= 6)
exr-transpositions-c1 (solution): restriction is onto; extension respects products and transpositions | inline (as in the proof of thm-transpositions-generate); lem-permutations-fixing-last-point (b), prp-homomorphism-composition-inverse (b), cited; induction on r with def-group-list-product (fact 1 of the proof of thm-transpositions-generate)
exr-transpositions-c2 (solution): (1 2)(1 3) = (1 3 2); the left-to-right product is the inverse cycle | exm-cycle-notation, prp-group-list-product-laws (c); verify/ch03/exr-transpositions-c2.py (k <= 7)
exr-transpositions-c3 (solution): the conjugating permutations id, (2 b), (1 a)(2 b) | inline; verify/ch03/exr-transpositions-c3.py (exhaustive in S_5)
exr-transpositions-r1 (solution): non-prime m >= 2 is ab with 0 < a, b < m | inline from fd2:def-prime, fd3:prp-divisibility-rules-integers (e), cancellation in Z (as in the proof of thm-characteristic-prime)
exr-transpositions-r1 (solution): F3.2 / Chapter 2 multiples agree with group multiples for k in N | prp-group-power-laws (e), cited; lem-integer-multiples (b) used for a, b in N only
exr-transpositions-r2 (solution): powers of [3] mod 7: 1, 3, 2, 6, 4, 5, [3]^6 = [1]; powers of the identity are the identity | inline arithmetic and induction; verify/ch03/exr-transpositions-r2.py
exr-transpositions-r3 (solution): Z is not finite via x -> 2x onto 2Z | fd2:thm-finite-no-proper-copy (group (i) of F3.1's citing rule), fd3:prp-ordered-ring-rules (f), fd3:prp-divisibility-rules-integers (g), cited
exr-transpositions-r3 (solution): fd2 finite-set results read on omega | group (i) of F3.1's citing rule after fd3:cor-omega-identification, cited by label
exr-transpositions-r4 (solution): V' = V minus {g, g^{-1}} is closed under inverses | thm-group-basic-properties (3), inline
exr-transpositions-r4 (solution): j - 2 elements after removing a 2-element set; even minus even is even; card T >= 1 even gives >= 2 | fd2:prp-disjoint-union-count, fd2:cor-finite-size-unique (group (i)); integer arithmetic in fd3:thm-integers-commutative-ring; fd3:prp-divisibility-rules-integers (g); verify/ch03/exr-transpositions-r4.py (small groups)
exr-transpositions-r4 (solution): Lagrange, Cauchy named as unavailable | prose pointers to AL1.4, AL1.6; nothing depends on them
-->
