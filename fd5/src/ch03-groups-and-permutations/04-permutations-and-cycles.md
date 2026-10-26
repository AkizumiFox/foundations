# Permutations and Cycle Notation

Shuffle three cards, then shuffle them again. Two shuffles in a row are a shuffle, every shuffle can be undone, and the order of the two shuffles matters. This is the group of bijections of a finite set (@exm-groups (c)), and it is the one group of this chapter studied in detail, because every determinant in linear algebra is built from it. This section gives it a compact notation, cycle notation, learns to multiply in it, counts its elements, and proves that every permutation breaks into independent loops: **follow the orbit, then peel it off**.

## Permutations and two-line notation

Section 3.1 showed that the bijections of a set form a group under composition. On the set \( \{1, \dots, n\} \) they are the rearrangements of \( n \) objects, and they get a name of their own.

*A permutation is a rearrangement: a bijection of a set to itself.*

::: {#def-symmetric-group}
[Permutations and the Symmetric Group]

Let \( X \) be a set. A **permutation** of \( X \) is a bijection \( X \to X \). The permutations of \( X \), with the operation \( \sigma\tau \coloneqq \sigma \circ \tau \), form the group \( S_X \) of @exm-groups (c). For \( n \in \nN \), the **symmetric group** is
\[
S_n \coloneqq S_{\{1, \dots, n\}} ,
\]
where \( \{1, \dots, n\} \) is empty for \( n = 0 \). The **support** of \( \sigma \in S_X \) is the set of points it moves,
\[
\supp \sigma \coloneqq \{ x \in X : \sigma(x) \ne x \} .
\]
:::

In words: \( S_X \) is not a new group. It is the group of bijections of \( X \), with the product written as juxtaposition. Its identity is \( \id_X \), written \( \id \) when \( X \) is clear, and the inverse of \( \sigma \) is the inverse function \( \sigma^{-1} \) (@fd2:def-inverse-function). The support of \( \id \) is empty, and the support is empty only for \( \id \): if \( \sigma(x) = x \) for every \( x \), then \( \sigma = \id_X \) (@fd2:prp-function-equality).

**The product is read right to left.** In \( S_X \) the product \( \sigma\tau \) is the composite \( \sigma \circ \tau \): **first apply \( \tau \), then \( \sigma \)**, exactly as \( g \circ f \) applies \( f \) first (@fd2:def-composition). So \( (\sigma\tau)(x) = \sigma(\tau(x)) \), and a longer product \( \sigma_1\sigma_2 \cdots \sigma_r \) applies \( \sigma_r \) first and \( \sigma_1 \) last.

**Two-line notation.** A permutation \( \sigma \in S_n \) is given by its values, and we write them under the points:
\[
\sigma = \begin{pmatrix} 1 & 2 & \cdots & n \\ \sigma(1) & \sigma(2) & \cdots & \sigma(n) \end{pmatrix} .
\]
This array is a **table** of values, not a matrix. For example, \( \begin{pmatrix} 1 & 2 & 3 & 4 \\ 3 & 1 & 2 & 4 \end{pmatrix} \in S_4 \) sends \( 1 \mapsto 3 \), \( 2 \mapsto 1 \), \( 3 \mapsto 2 \) and fixes \( 4 \); its support is \( \{1, 2, 3\} \). The bottom row of a permutation lists each of \( 1, \dots, n \) exactly once: once at least, because \( \sigma \) is surjective, and at most once, because it is injective.

**The smallest symmetric groups.** \( S_0 \) has one element, the empty function \( \emptyset \to \emptyset \) (@fd2:prp-empty-function (a)), which is a bijection because there is nothing to check; it is the trivial group. \( S_1 \) has one element, \( \id \), since the only function \( \{1\} \to \{1\} \) sends \( 1 \mapsto 1 \). \( S_2 \) has two elements, \( \id \) and the permutation swapping \( 1 \) and \( 2 \): a bijection of \( \{1, 2\} \) either fixes \( 1 \), and then also \( 2 \), or sends \( 1 \mapsto 2 \), and then \( 2 \mapsto 1 \). These degenerate cases are where inductions on \( n \) start, here and in Section 3.5.

## Cycles

Two-line notation lists every value, even the values of points that do not move. Most permutations met in practice move a few points around a loop and leave the rest alone, and a notation that records only the loop is shorter and shows more.

*A cycle moves a list of distinct points one step along the list, the last back to the first, and fixes everything else.*

::: {#def-cycle}
[Cycle, Transposition]

Let \( n \in \nN \) and \( k \ge 2 \), and let \( i_1, \dots, i_k \in \{1, \dots, n\} \) be **distinct**. The **\( k \)-cycle** \( (i_1\ i_2\ \cdots\ i_k) \in S_n \) is the permutation \( \gamma \) with
\[
\gamma(i_j) \coloneqq i_{j+1} \ \text{ for } 1 \le j < k , \qquad \gamma(i_k) \coloneqq i_1 ,
\]
and \( \gamma(x) \coloneqq x \) for every \( x \in \{1, \dots, n\} \) not among \( i_1, \dots, i_k \). A \( 2 \)-cycle \( (i\ j) \) is a **transposition**. Two cycles are **disjoint** if their supports are disjoint.
:::

In words: \( i_1 \mapsto i_2 \mapsto \cdots \mapsto i_k \mapsto i_1 \), and the points off the list stay put. A transposition \( (i\ j) \) swaps \( i \) and \( j \).

*Well-definedness.* Because the entries are distinct, each point of \( \{1, \dots, n\} \) receives exactly one value from the rule, so \( \gamma \) is a function. It is a bijection: the cycle \( (i_k\ \cdots\ i_2\ i_1) \), the list read backwards, undoes it point by point (\( i_{j+1} \mapsto i_j \) and \( i_1 \mapsto i_k \), and the other points are fixed by both), so it is a two-sided inverse and @fd2:thm-bijection-iff-inverse applies. Hence
\[
(i_1\ i_2\ \cdots\ i_k)^{-1} = (i_k\ \cdots\ i_2\ i_1) .
\]
Every entry is moved, since \( i_{j+1} \ne i_j \) and \( i_1 \ne i_k \) by distinctness and \( k \ge 2 \); so \( \supp (i_1\ \cdots\ i_k) = \{ i_1, \dots, i_k \} \). A transposition is its own inverse: \( (i\ j)(i\ j) = \id \).

**Examples.** In \( S_4 \), \( (1\ 2\ 3) \) sends \( 1 \mapsto 2 \), \( 2 \mapsto 3 \), \( 3 \mapsto 1 \) and fixes \( 4 \); in two-line notation it is \( \begin{pmatrix} 1 & 2 & 3 & 4 \\ 2 & 3 & 1 & 4 \end{pmatrix} \). The same cycle may be written starting at any of its entries: \( (1\ 2\ 3) = (2\ 3\ 1) = (3\ 1\ 2) \), since all three describe the loop \( 1 \mapsto 2 \mapsto 3 \mapsto 1 \). But \( (1\ 3\ 2) \) is a different permutation: it sends \( 1 \mapsto 3 \). The cycles \( (1\ 2) \) and \( (3\ 4) \) are disjoint; \( (1\ 2) \) and \( (2\ 3) \) are not.

::: {.second-reading title="Why a cycle has at least two entries"}
**The identity is not a cycle.** The definition asks for \( k \ge 2 \): a "\( 1 \)-cycle" \( (i) \) would be the identity, and so would every one of them, so the notation would not be telling us anything. The identity is instead the empty product of cycles (@def-group-list-product), and that is how it will appear in the decomposition theorem below.
:::

::: {.check}
Which of these are equal in \( S_4 \): \( (2\ 4\ 1) \), \( (1\ 2\ 4) \), \( (1\ 4\ 2) \)? Write the one that differs in two-line notation.
:::

::: {.solution}
\( (2\ 4\ 1) \) is the loop \( 2 \mapsto 4 \mapsto 1 \mapsto 2 \), and \( (1\ 2\ 4) \) is the same loop started at \( 1 \): both send \( 1 \mapsto 2 \), \( 2 \mapsto 4 \), \( 4 \mapsto 1 \) and fix \( 3 \). So they are equal. \( (1\ 4\ 2) \) runs the loop backwards: it sends \( 1 \mapsto 4 \), \( 4 \mapsto 2 \), \( 2 \mapsto 1 \), so it differs from the other two at \( 1 \). In two-line notation it is \( \begin{pmatrix} 1 & 2 & 3 & 4 \\ 4 & 1 & 3 & 2 \end{pmatrix} \); it is the inverse of the other two.
:::

Products of cycles are computed by following each point through the factors, **from right to left**.

::: {#exm-cycle-notation}
[Computing with Cycles]

In \( S_3 \), compute \( (1\ 3)(1\ 2) \) and \( (1\ 2)(1\ 3) \). In \( S_5 \), write
\[
\sigma = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 3 & 5 & 1 & 2 & 4 \end{pmatrix}
\]
as a product of cycles.
:::

::: {.solution}
For \( (1\ 3)(1\ 2) \), follow each point through \( (1\ 2) \) first, then \( (1\ 3) \): \( 1 \mapsto 2 \mapsto 2 \), \( 2 \mapsto 1 \mapsto 3 \), \( 3 \mapsto 3 \mapsto 1 \). So \( (1\ 3)(1\ 2) = (1\ 2\ 3) \). For \( (1\ 2)(1\ 3) \): \( 1 \mapsto 3 \mapsto 3 \), \( 3 \mapsto 1 \mapsto 2 \), \( 2 \mapsto 2 \mapsto 1 \). So \( (1\ 2)(1\ 3) = (1\ 3\ 2) \). The two products differ, so \( S_3 \) is not abelian. For every \( n \ge 3 \), the same two transpositions lie in \( S_n \), the same computation applies at \( 1, 2, 3 \), and both products fix every point \( \ge 4 \); so \( S_n \) is not abelian for every \( n \ge 3 \).

For \( \sigma \), start at \( 1 \) and follow: \( 1 \mapsto 3 \mapsto 1 \), a loop \( (1\ 3) \). The smallest point not yet used is \( 2 \): \( 2 \mapsto 5 \mapsto 4 \mapsto 2 \), a loop \( (2\ 5\ 4) \). Every point is now used, so \( \sigma = (1\ 3)(2\ 5\ 4) \). To check, follow each point through \( (2\ 5\ 4) \) first, then \( (1\ 3) \): \( 1 \mapsto 1 \mapsto 3 \), \( 2 \mapsto 5 \mapsto 5 \), \( 3 \mapsto 3 \mapsto 1 \), \( 4 \mapsto 2 \mapsto 2 \), \( 5 \mapsto 4 \mapsto 4 \), which is the bottom row \( 3, 5, 1, 2, 4 \). The two cycles move disjoint sets of points, and the product in the other order, \( (2\ 5\ 4)(1\ 3) \), is also \( \sigma \), as the same check shows.
:::

::: {.second-reading title="The small symmetric groups are abelian"}
For \( S_n \) with \( n \le 2 \) the situation is different: \( S_0 \), \( S_1 \) and \( S_2 \) have at most two elements, and any two of their elements commute, since one of them is \( \id \) or both are equal. So \( S_n \) is abelian exactly when \( n \le 2 \).
:::

::: {.warning}
**Mind the order.** \( \sigma\tau \) applies \( \tau \) first, as \( g \circ f \) applies \( f \) first. Reading a product of cycles from left to right gives a wrong answer: read that way, \( (1\ 3)(1\ 2) \) would send \( 1 \mapsto 3 \mapsto 3 \), \( 3 \mapsto 1 \mapsto 2 \), \( 2 \mapsto 2 \mapsto 1 \), that is, "\( (1\ 3\ 2) \)"; but the example computed \( (1\ 3)(1\ 2) = (1\ 2\ 3) \). The left-to-right reading computes the product in the other order.
:::

Section 3.1 noted that the power law \( (gh)^n = g^n h^n \) of @prp-group-power-laws (d) needs \( gh = hg \). In \( S_3 \) it fails without that hypothesis.

::: {.warning}
\( (\sigma\tau)^2 = \sigma^2\tau^2 \) is false in general. Take \( \sigma = (1\ 2) \) and \( \tau = (1\ 3) \). By the example, \( \sigma\tau = (1\ 3\ 2) \), and \( (1\ 3\ 2)(1\ 3\ 2) \) sends \( 1 \mapsto 3 \mapsto 2 \), \( 2 \mapsto 1 \mapsto 3 \), \( 3 \mapsto 2 \mapsto 1 \), so \( (\sigma\tau)^2 = (1\ 2\ 3) \). But transpositions are their own inverses, so \( \sigma^2\tau^2 = \id \cdot \id = \id \). Here \( \sigma\tau \ne \tau\sigma \), and the law fails.
:::

::: {.check}
Compute \( (1\ 2\ 3)(1\ 2) \) in \( S_3 \).
:::

::: {.solution}
Apply \( (1\ 2) \) first: \( 1 \mapsto 2 \mapsto 3 \), \( 2 \mapsto 1 \mapsto 2 \), \( 3 \mapsto 3 \mapsto 1 \). So \( 1 \) and \( 3 \) are swapped and \( 2 \) is fixed: \( (1\ 2\ 3)(1\ 2) = (1\ 3) \).
:::

## Counting permutations

How many permutations does \( S_n \) have? There are \( n \) choices for \( \sigma(1) \), then \( n - 1 \) for \( \sigma(2) \), and so on, which suggests \( n! \). We make this precise by induction on \( n \), and the induction needs one structural fact: the permutations of \( \{1, \dots, n + 1\} \) that fix the last point are, in effect, the permutations of \( \{1, \dots, n\} \). Section 3.5 uses the same fact for a different induction.

::: {#lem-permutations-fixing-last-point}
[Permutations Fixing the Last Point]

Let \( n \in \nN \), and let \( S' \coloneqq \{ \sigma \in S_{n+1} : \sigma(n + 1) = n + 1 \} \), a subgroup of \( S_{n+1} \).

::: {.enumerate options="label=(\alph*)"}
1. For \( \sigma \in S' \), the restriction \( \sigma' \) of \( \sigma \) to \( \{1, \dots, n\} \), with codomain \( \{1, \dots, n\} \), is a permutation of \( \{1, \dots, n\} \).
2. The map \( S' \to S_n \), \( \sigma \mapsto \sigma' \), is an isomorphism. Its inverse sends \( \rho \in S_n \) to its **extension** \( \bar\rho \in S' \), defined by \( \bar\rho(i) \coloneqq \rho(i) \) for \( i \le n \) and \( \bar\rho(n + 1) \coloneqq n + 1 \).
:::
:::

That \( S' \) is a subgroup is @exm-subgroups (e), with \( X = \{1, \dots, n + 1\} \) and the chosen point \( n + 1 \).

::: {.idea}
A permutation fixing \( n + 1 \) cannot send any other point to \( n + 1 \), since that value is taken; so it maps \( \{1, \dots, n\} \) into itself. It also reaches every point there, because whatever reaches \( j \le n \) cannot be \( n + 1 \). Restricting and extending undo each other, and restriction respects composition.
:::

::: {.proof}
(a) Let \( \sigma \in S' \) and \( i \in \{1, \dots, n\} \). If \( \sigma(i) = n + 1 = \sigma(n + 1) \), then \( i = n + 1 \) by injectivity, which is false; so \( \sigma(i) \in \{1, \dots, n\} \), and \( \sigma' \colon \{1, \dots, n\} \to \{1, \dots, n\} \), \( \sigma'(i) \coloneqq \sigma(i) \), is a function. It is injective because \( \sigma \) is. It is surjective: for \( j \in \{1, \dots, n\} \) there is \( i \in \{1, \dots, n + 1\} \) with \( \sigma(i) = j \), since \( \sigma \) is surjective, and \( i \ne n + 1 \), since \( \sigma(n + 1) = n + 1 \ne j \). So \( \sigma' \in S_n \).

(b) Write \( R(\sigma) \coloneqq \sigma' \) and \( E(\rho) \coloneqq \bar\rho \).

*\( E \) maps into \( S' \).* The extension \( \bar\rho \) is a function on \( \{1, \dots, n + 1\} \) with values in that set, and \( \overline{\rho^{-1}} \) undoes it point by point: for \( i \le n \), \( \overline{\rho^{-1}}(\bar\rho(i)) = \rho^{-1}(\rho(i)) = i \), and both fix \( n + 1 \); the other composite is the same with \( \rho \) and \( \rho^{-1} \) exchanged. So \( \bar\rho \) is a bijection (@fd2:thm-bijection-iff-inverse) fixing \( n + 1 \).

*\( R \) and \( E \) are mutually inverse.* For \( \sigma \in S' \), \( \overline{\sigma'} \) agrees with \( \sigma \) at every \( i \le n \) and at \( n + 1 \), so \( E(R(\sigma)) = \sigma \) (@fd2:prp-function-equality). For \( \rho \in S_n \), \( (\bar\rho)' \) agrees with \( \rho \) at every \( i \le n \), so \( R(E(\rho)) = \rho \). Hence \( R \) is a bijection with inverse \( E \) (@fd2:def-inverse-function, @fd2:thm-bijection-iff-inverse).

*\( R \) is a homomorphism.* Let \( \sigma, \tau \in S' \) and \( i \le n \). By (a), \( \tau(i) \le n \), so
\[
(\sigma\tau)'(i) = \sigma(\tau(i)) = \sigma'(\tau'(i)) = (\sigma'\tau')(i) .
\]
So \( (\sigma\tau)' = \sigma'\tau' \), and \( R \) is an isomorphism. Its inverse \( E \) is an isomorphism by @prp-homomorphism-composition-inverse (b). This proves the lemma.
:::

So inside \( S_{n+1} \) sits a copy of \( S_n \), the permutations that leave the last point alone. The factorial \( n! \) is that of @fd2:def-sum-product, read in \( \nN \): \( 0! = 1 \) and \( (n + 1)! = n! \, (n + 1) \).

::: {#prp-symmetric-group-order}
[The Symmetric Group Has n! Elements]

For every \( n \in \nN \), \( S_n \) is finite and has \( n! \) elements: \( \card{S_n} = n! \).
:::

::: {.idea}
Sort the permutations of \( \{1, \dots, n + 1\} \) by where they send the last point. Those sending it to \( n + 1 \) are a copy of \( S_n \), by the lemma. Those sending it to \( k \le n \) are matched with the first kind by composing with the swap \( (k\ \ n{+}1) \). So there are \( n + 1 \) classes of \( n! \) permutations each.
:::

::: {.proof}
We use induction on \( n \) (@fd1:ax-induction). For \( n = 0 \), \( S_0 \) has exactly one element, the empty function (@fd2:prp-empty-function (a)), and \( 0! = 1 \).

Suppose \( S_n \) has \( n! \) elements. For \( k \in \{1, \dots, n + 1\} \) let
\[
A_k \coloneqq \{ \sigma \in S_{n+1} : \sigma(n + 1) = k \} .
\]
Every \( \sigma \in S_{n+1} \) lies in exactly one \( A_k \), namely for \( k = \sigma(n + 1) \). So the sets \( A_1, \dots, A_{n+1} \) are pairwise disjoint and their union is \( S_{n+1} \).

*The class \( A_{n+1} \).* \( A_{n+1} \) is the subgroup \( S' \) of @lem-permutations-fixing-last-point. By the induction hypothesis there is a bijection \( \{1, \dots, n!\} \to S_n \) (@fd2:def-finite); composing it with the bijection \( S_n \to S' \) of the lemma gives a bijection \( \{1, \dots, n!\} \to A_{n+1} \) (@fd2:thm-composition-injective-surjective (c)). So \( A_{n+1} \) has \( n! \) elements.

*The classes \( A_k \), \( k \le n \).* Let \( \tau \coloneqq (k\ \ n{+}1) \), a transposition with \( \tau\tau = \id \). If \( \sigma \in A_k \), then \( (\tau\sigma)(n + 1) = \tau(k) = n + 1 \), so \( \tau\sigma \in A_{n+1} \); if \( \rho \in A_{n+1} \), then \( (\tau\rho)(n + 1) = \tau(n + 1) = k \), so \( \tau\rho \in A_k \). The maps \( A_k \to A_{n+1} \), \( \sigma \mapsto \tau\sigma \), and \( A_{n+1} \to A_k \), \( \rho \mapsto \tau\rho \), are mutually inverse, since \( \tau(\tau\sigma) = (\tau\tau)\sigma = \sigma \) by (G1), \( \tau\tau = \id \) and (G2), and likewise for \( \rho \). So \( \sigma \mapsto \tau\sigma \) is a bijection \( A_k \to A_{n+1} \) (@fd2:thm-bijection-iff-inverse), and composing as before, \( A_k \) has \( n! \) elements.

*Adding up.* We prove, by @fd2:thm-induction with base \( 1 \) (read on \( \omega \) by @fd3:cor-omega-identification (b)), the statement \( P(j) \): "if \( j \le n + 1 \), the union \( A_1 \cup \dots \cup A_j \) has \( j \, n! \) elements". For \( j = 1 \) this is the count of \( A_1 \), and the step adds the \( n! \) elements of \( A_{j+1} \), disjoint from \( A_1 \cup \dots \cup A_j \), by @fd2:prp-disjoint-union-count, with \( j \, n! + n! = (j + 1) \, n! \). For \( j = n + 1 \), \( S_{n+1} \) has \( (n + 1) \, n! = (n + 1)! \) elements. This completes the induction and proves the proposition.
:::

So \( S_3 \) has \( 6 \) elements, \( S_4 \) has \( 24 \), and \( S_{10} \) already has \( 3628800 \). For \( S_3 \) all six can be listed: \( \id \), the three transpositions \( (1\ 2) \), \( (1\ 3) \), \( (2\ 3) \), and the two \( 3 \)-cycles \( (1\ 2\ 3) \), \( (1\ 3\ 2) \). These are six different permutations, so by the proposition they are all of \( S_3 \): a proper subset of a \( 6 \)-element set has fewer elements (@fd2:prp-subset-finite, @fd2:cor-finite-size-unique).

## Disjoint cycles and the decomposition theorem

In @exm-cycle-notation, \( \sigma \) came apart into the loops \( (1\ 3) \) and \( (2\ 5\ 4) \), which move disjoint sets of points, and the order of the two factors did not matter. Both observations hold in general. We start with the second: permutations moving disjoint sets of points do not interfere with each other.

::: {#prp-disjoint-cycles-commute}
[Disjoint Permutations Commute]

Let \( n \in \nN \) and \( \sigma, \tau \in S_n \) with \( \supp \sigma \cap \supp \tau = \emptyset \). Then \( \sigma\tau = \tau\sigma \). Moreover, every permutation \( \sigma \) maps \( \supp \sigma \) onto itself: \( \sigma(\supp \sigma) = \supp \sigma \).
:::

In particular, disjoint cycles commute.

::: {.idea}
A point moved by \( \sigma \) is fixed by \( \tau \), and so is its image under \( \sigma \), because \( \sigma \) keeps its moved points among its moved points. So on \( \supp \sigma \) only \( \sigma \) acts, on \( \supp \tau \) only \( \tau \), and elsewhere neither: the order of application cannot matter.
:::

::: {.proof}
*\( \sigma \) maps its support onto itself.* Let \( i \in \supp \sigma \). If \( \sigma(i) \notin \supp \sigma \), then \( \sigma(\sigma(i)) = \sigma(i) \), and injectivity gives \( \sigma(i) = i \), against \( i \in \supp \sigma \). So \( \sigma(\supp \sigma) \subseteq \supp \sigma \). Conversely, let \( j \in \supp \sigma \) and \( i \coloneqq \sigma^{-1}(j) \). If \( i \notin \supp \sigma \), then \( j = \sigma(i) = i \notin \supp \sigma \), a contradiction; so \( i \in \supp \sigma \) and \( j = \sigma(i) \in \sigma(\supp \sigma) \). Hence \( \sigma(\supp \sigma) = \supp \sigma \).

*Commuting.* Let \( i \in \{1, \dots, n\} \). There are three cases, since \( i \) lies in at most one of the disjoint supports.

*Case 1: \( i \in \supp \sigma \).* Then \( i \notin \supp \tau \), so \( \tau(i) = i \). Also \( \sigma(i) \in \supp \sigma \) by the first part, so \( \sigma(i) \notin \supp \tau \) and \( \tau(\sigma(i)) = \sigma(i) \). Hence \( (\sigma\tau)(i) = \sigma(i) = (\tau\sigma)(i) \).

*Case 2: \( i \in \supp \tau \).* The same argument with \( \sigma \) and \( \tau \) exchanged gives \( (\tau\sigma)(i) = \tau(i) = (\sigma\tau)(i) \).

*Case 3: \( i \) lies in neither support.* Then \( \sigma(i) = i = \tau(i) \), and both products send \( i \) to \( i \).

So \( \sigma\tau \) and \( \tau\sigma \) agree at every point, and \( \sigma\tau = \tau\sigma \) (@fd2:prp-function-equality). This proves the proposition.
:::

The hypothesis "disjoint" cannot be dropped: \( (1\ 2) \) and \( (1\ 3) \) share the point \( 1 \), and @exm-cycle-notation shows that they do not commute. Exercise C1 looks at the dropped hypothesis more closely.

Now the main theorem. To break a permutation into loops, start at a point it moves and follow it until it comes back. The loop found is a cycle; remove it, and fewer points are moved, so induction finishes the job.

::: {#thm-disjoint-cycle-decomposition}
[Disjoint Cycle Decomposition]

Let \( n \in \nN \). Every \( \sigma \in S_n \) is a product \( \sigma = \gamma_1 \gamma_2 \cdots \gamma_s \), \( s \in \nN \), of pairwise disjoint cycles, each with support contained in \( \supp \sigma \). For \( \sigma = \id \) the product is empty (\( s = 0 \)).
:::

The clause about supports is part of the statement because the induction needs it: it is what makes the new cycle disjoint from the old ones. The theorem says nothing about uniqueness; that the decomposition is unique up to the order of the factors is proved in *Groups*, the chapter "Symmetric Groups and the Sign of a Permutation".

::: {.idea}
Induction on the number \( m \) of points that \( \sigma \) moves. ① Pick a moved point \( i \) and follow its orbit \( i, \sigma(i), \sigma^2(i), \dots \). There are only \( n \) points, so the orbit repeats, and it repeats first at \( i \) itself. ② The points before the return form a cycle \( \gamma \) on which \( \sigma \) acts exactly as \( \gamma \) does. ③ Peel it off: \( \rho \coloneqq \gamma^{-1}\sigma \) fixes the orbit and everything \( \sigma \) fixes, so it moves fewer points, and the induction hypothesis decomposes it. Then \( \sigma = \gamma\rho \).

*Before reading on: why must the orbit of \( i \) return to \( i \) itself, and not to some later point?*
:::

::: {.proof}
We use strong induction (@fd1:thm-strong-induction) on \( m \in \nN \), for the statement: every \( \sigma \in S_n \) whose support has \( m \) elements is a product of pairwise disjoint cycles with supports in \( \supp \sigma \). Every support is a subset of \( \{1, \dots, n\} \), which has \( n \) elements, so it is finite (@fd2:prp-subset-finite), and every \( \sigma \) is covered by the statement for some \( m \).

Let \( \sigma \in S_n \), let \( \supp \sigma \) have \( m \) elements, and suppose the statement holds for every smaller number. If \( m = 0 \), then \( \supp \sigma = \emptyset \), so \( \sigma = \id \), the empty product (@def-group-list-product). Let \( m \ge 1 \) and choose \( i \in \supp \sigma \).

*Follow the orbit.* Powers are taken in the group \( S_n \) (@def-group-integer-power). The map \( \{0, 1, \dots, n\} \to \{1, \dots, n\} \), \( c \mapsto \sigma^c(i) \), goes from a set of \( n + 1 \) elements to a set of \( n \) elements, so it is not injective (@fd2:cor-pigeonhole-finite-sets (a)): \( \sigma^a(i) = \sigma^b(i) \) for some \( 0 \le a < b \le n \). Apply \( \sigma^{-a} \) to both sides. By @prp-group-power-laws (a), \( \sigma^{-a}\sigma^a = \sigma^0 = \id \) and \( \sigma^{-a}\sigma^b = \sigma^{b-a} \), so
\[
i = \sigma^{b-a}(i) , \qquad b - a \ge 1 .
\]
So the set of \( c \in \nZ_{>0} \) with \( \sigma^c(i) = i \) is non-empty and bounded below by \( 0 \), and it has a least element \( r \) (@fd3:prp-integer-least-element). Since \( \sigma(i) \ne i \), \( r \ge 2 \).

The points \( i, \sigma(i), \dots, \sigma^{r-1}(i) \) are distinct. Indeed, if \( \sigma^c(i) = \sigma^d(i) \) with \( 0 \le c < d \le r - 1 \), the argument just given yields \( \sigma^{d-c}(i) = i \) with \( 0 < d - c < r \), against the minimality of \( r \). Let
\[
O \coloneqq \{ \sigma^c(i) : 0 \le c \le r - 1 \} , \qquad \gamma \coloneqq \bigl(i\ \ \sigma(i)\ \cdots\ \sigma^{r-1}(i)\bigr) ,
\]
an \( r \)-cycle (@def-cycle) with \( \supp \gamma = O \).

*\( \sigma \) acts on \( O \) as \( \gamma \) does.* For \( 0 \le c < r - 1 \), \( \gamma(\sigma^c(i)) = \sigma^{c+1}(i) = \sigma(\sigma^c(i)) \), where \( \sigma^{c+1} = \sigma\sigma^c \) by @prp-group-power-laws (a). For \( c = r - 1 \), \( \gamma(\sigma^{r-1}(i)) = i = \sigma^r(i) = \sigma(\sigma^{r-1}(i)) \). So \( \sigma(x) = \gamma(x) \) for every \( x \in O \). In particular \( \sigma \) moves every point of \( O \), since \( \gamma \) does, and \( O \subseteq \supp \sigma \).

*Peel it off.* Let \( \rho \coloneqq \gamma^{-1}\sigma \). For \( x \in O \), \( \rho(x) = \gamma^{-1}(\sigma(x)) = \gamma^{-1}(\gamma(x)) = x \). For \( x \notin \supp \sigma \), we have \( x \notin O \), so \( \gamma(x) = x \) and hence \( \gamma^{-1}(x) = x \); then \( \rho(x) = \gamma^{-1}(x) = x \). So \( \rho \) fixes every point of \( O \) and every point outside \( \supp \sigma \):
\[
\supp \rho \subseteq \supp \sigma \setminus O .
\]
Since \( i \in O \), the set \( \supp \sigma \setminus O \) is a proper subset of \( \supp \sigma \), so it has fewer than \( m \) elements, and so does its subset \( \supp \rho \) (@fd2:prp-subset-finite, twice). By the induction hypothesis, \( \rho = \gamma_1 \cdots \gamma_s \) with pairwise disjoint cycles \( \gamma_j \) and \( \supp \gamma_j \subseteq \supp \rho \subseteq \supp \sigma \setminus O \). Each \( \gamma_j \) is therefore disjoint from \( \gamma \), whose support is \( O \).

Finally, \( \gamma\rho = \gamma\gamma^{-1}\sigma = \sigma \), so by @prp-group-list-product-laws (a)
\[
\sigma = \gamma\gamma_1 \cdots \gamma_s ,
\]
a product of pairwise disjoint cycles, with \( \supp \gamma = O \subseteq \supp \sigma \) and \( \supp \gamma_j \subseteq \supp \sigma \). This completes the induction and proves the theorem.
:::

*The answer to the prompt.* The orbit returns to \( i \) itself because \( \sigma \) is injective; in the proof, that is the step "apply \( \sigma^{-a} \)". If the first repetition were \( \sigma^b(i) = \sigma^a(i) \) with \( a \ge 1 \), applying \( \sigma^{-1} \) would give the earlier repetition \( \sigma^{b-1}(i) = \sigma^{a-1}(i) \). For a function that is not injective this fails: \( f \colon \{1, 2\} \to \{1, 2\} \) with \( f(1) = f(2) = 2 \) has the orbit \( 1, 2, 2, 2, \dots \), which never comes back to \( 1 \).

The proof is an algorithm. Here it is run on one permutation.

**A worked run.** Let \( \sigma \in S_6 \) send \( 1 \mapsto 4 \), \( 2 \mapsto 6 \), \( 3 \mapsto 3 \), \( 4 \mapsto 1 \), \( 5 \mapsto 2 \), \( 6 \mapsto 5 \). Its support is \( \{1, 2, 4, 5, 6\} \). Start at \( 1 \): \( 1 \mapsto 4 \mapsto 1 \), so \( r = 2 \) and \( \gamma = (1\ 4) \). Peel it off: \( \rho = (1\ 4)^{-1}\sigma = (1\ 4)\sigma \) fixes \( 1 \) and \( 4 \) and agrees with \( \sigma \) elsewhere, with support \( \{2, 5, 6\} \). Start again at \( 2 \): \( 2 \mapsto 6 \mapsto 5 \mapsto 2 \), so \( r = 3 \) and the next cycle is \( (2\ 6\ 5) \). Peeling it off leaves the identity, and the point \( 3 \), fixed by \( \sigma \), never enters. So
\[
\sigma = (1\ 4)(2\ 6\ 5) .
\]

::: {.check}
Decompose \( \begin{pmatrix} 1 & 2 & 3 & 4 & 5 & 6 \\ 3 & 6 & 5 & 4 & 1 & 2 \end{pmatrix} \in S_6 \) into disjoint cycles.
:::

::: {.solution}
Start at \( 1 \): \( 1 \mapsto 3 \mapsto 5 \mapsto 1 \), the cycle \( (1\ 3\ 5) \). The next moved point is \( 2 \): \( 2 \mapsto 6 \mapsto 2 \), the cycle \( (2\ 6) \). The point \( 4 \) is fixed. So the permutation is \( (1\ 3\ 5)(2\ 6) \), and by @prp-disjoint-cycles-commute also \( (2\ 6)(1\ 3\ 5) \).
:::

By @prp-disjoint-cycles-commute, two neighboring factors of a disjoint cycle decomposition may be exchanged; for instance \( (1\ 3\ 5)(2\ 6) = (2\ 6)(1\ 3\ 5) \). The next section breaks each cycle further, into transpositions.

## Exercises

### A. Check your understanding

::: {#exr-permutations-and-cycles-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Compute \( (1\ 2\ 3\ 4)(2\ 4) \) and \( (2\ 4)(1\ 2\ 3\ 4) \) in \( S_4 \), as products of disjoint cycles.
2. Find the inverse of \( (1\ 5\ 2\ 7) \) in \( S_7 \), written as a cycle starting at \( 1 \).
3. Run the proof of @thm-disjoint-cycle-decomposition on
\[
\sigma = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 2 & 5 & 4 & 3 & 1 \end{pmatrix} \in S_5 ,
\]
starting at \( i = 1 \): give the orbit of \( 1 \), the number \( r \), the cycle \( \gamma \), and \( \rho = \gamma^{-1}\sigma \); then finish the run. Which step of the proof uses that \( \sigma \) is injective?
4. Compute \( \bigl((1\ 2)(2\ 3)\bigr)^2 \) and \( (1\ 2)^2(2\ 3)^2 \) in \( S_3 \).
:::
:::

::: {.solution}
(a) For \( (1\ 2\ 3\ 4)(2\ 4) \), apply \( (2\ 4) \) first: \( 1 \mapsto 1 \mapsto 2 \), \( 2 \mapsto 4 \mapsto 1 \), \( 3 \mapsto 3 \mapsto 4 \), \( 4 \mapsto 2 \mapsto 3 \). So the product is \( (1\ 2)(3\ 4) \). For \( (2\ 4)(1\ 2\ 3\ 4) \), apply \( (1\ 2\ 3\ 4) \) first: \( 1 \mapsto 2 \mapsto 4 \), \( 4 \mapsto 1 \mapsto 1 \), \( 2 \mapsto 3 \mapsto 3 \), \( 3 \mapsto 4 \mapsto 2 \). So the product is \( (1\ 4)(2\ 3) \). The two orders give different permutations.

(b) By the inverse formula after @def-cycle, \( (1\ 5\ 2\ 7)^{-1} = (7\ 2\ 5\ 1) \), which, started at \( 1 \), is \( (1\ 7\ 2\ 5) \).

(c) The orbit of \( 1 \) is \( 1 \mapsto 2 \mapsto 5 \mapsto 1 \), so \( r = 3 \) and \( \gamma = (1\ 2\ 5) \), with \( \gamma^{-1} = (5\ 2\ 1) = (1\ 5\ 2) \). Then \( \rho = \gamma^{-1}\sigma \) sends \( 1 \mapsto 2 \mapsto 1 \), \( 2 \mapsto 5 \mapsto 2 \), \( 5 \mapsto 1 \mapsto 5 \), \( 3 \mapsto 4 \mapsto 4 \), \( 4 \mapsto 3 \mapsto 3 \): \( \rho = (3\ 4) \). Running the proof on \( \rho \), starting at \( 3 \): \( 3 \mapsto 4 \mapsto 3 \), so the cycle is \( (3\ 4) \), and peeling it off leaves \( \id \). Hence \( \sigma = (1\ 2\ 5)(3\ 4) \). Injectivity is used where the orbit is shown to return to \( i \) itself: the step that applies \( \sigma^{-a} \) to \( \sigma^a(i) = \sigma^b(i) \).

(d) \( (1\ 2)(2\ 3) \): \( 1 \mapsto 1 \mapsto 2 \), \( 2 \mapsto 3 \mapsto 3 \), \( 3 \mapsto 2 \mapsto 1 \), so it is \( (1\ 2\ 3) \), and its square sends \( 1 \mapsto 2 \mapsto 3 \), \( 3 \mapsto 1 \mapsto 2 \), \( 2 \mapsto 3 \mapsto 1 \): \( \bigl((1\ 2)(2\ 3)\bigr)^2 = (1\ 3\ 2) \). On the other hand \( (1\ 2)^2(2\ 3)^2 = \id \), since transpositions are their own inverses. A second instance of the warning on \( (\sigma\tau)^2 \).
:::

### B. Practice

::: {#exr-permutations-and-cycles-b1}
[B1: The table of \( S_3 \)]

List the six elements of \( S_3 \) in cycle notation and write out the table whose entry in row \( x \) and column \( y \) is \( xy \). Hence find all \( x \in S_3 \) with \( x^2 = \id \), and all \( x \) that commute with every element of \( S_3 \).
:::

::: {.solution}
By the list after @prp-symmetric-group-order, the elements are \( \id, (1\ 2), (1\ 3), (2\ 3), (1\ 2\ 3), (1\ 3\ 2) \). Computing each product right to left, as in @exm-cycle-notation, the entry in row \( x \), column \( y \) is \( xy \):

| \( xy \) | \( \id \) | \( (1\ 2) \) | \( (1\ 3) \) | \( (2\ 3) \) | \( (1\ 2\ 3) \) | \( (1\ 3\ 2) \) |
|---|---|---|---|---|---|---|
| \( \id \) | \( \id \) | \( (1\ 2) \) | \( (1\ 3) \) | \( (2\ 3) \) | \( (1\ 2\ 3) \) | \( (1\ 3\ 2) \) |
| \( (1\ 2) \) | \( (1\ 2) \) | \( \id \) | \( (1\ 3\ 2) \) | \( (1\ 2\ 3) \) | \( (2\ 3) \) | \( (1\ 3) \) |
| \( (1\ 3) \) | \( (1\ 3) \) | \( (1\ 2\ 3) \) | \( \id \) | \( (1\ 3\ 2) \) | \( (1\ 2) \) | \( (2\ 3) \) |
| \( (2\ 3) \) | \( (2\ 3) \) | \( (1\ 3\ 2) \) | \( (1\ 2\ 3) \) | \( \id \) | \( (1\ 3) \) | \( (1\ 2) \) |
| \( (1\ 2\ 3) \) | \( (1\ 2\ 3) \) | \( (1\ 3) \) | \( (2\ 3) \) | \( (1\ 2) \) | \( (1\ 3\ 2) \) | \( \id \) |
| \( (1\ 3\ 2) \) | \( (1\ 3\ 2) \) | \( (2\ 3) \) | \( (1\ 2) \) | \( (1\ 3) \) | \( \id \) | \( (1\ 2\ 3) \) |

For example, the entry in row \( (1\ 2) \), column \( (2\ 3) \) is \( (1\ 2)(2\ 3) \): \( 1 \mapsto 1 \mapsto 2 \), \( 2 \mapsto 3 \mapsto 3 \), \( 3 \mapsto 2 \mapsto 1 \), which is \( (1\ 2\ 3) \).

Reading the diagonal, \( x^2 = \id \) exactly for \( x = \id, (1\ 2), (1\ 3), (2\ 3) \). An element \( x \) commutes with every element exactly when row \( x \) equals column \( x \). This holds for \( \id \). It fails for every other element: \( (1\ 2)(1\ 3) = (1\ 3\ 2) \ne (1\ 2\ 3) = (1\ 3)(1\ 2) \) handles \( (1\ 2) \) and \( (1\ 3) \); \( (2\ 3)(1\ 2) = (1\ 3\ 2) \ne (1\ 2\ 3) = (1\ 2)(2\ 3) \) handles \( (2\ 3) \); and \( (1\ 2\ 3)(1\ 2) = (1\ 3) \ne (2\ 3) = (1\ 2)(1\ 2\ 3) \) handles \( (1\ 2\ 3) \), while \( (1\ 3\ 2)(1\ 2) = (2\ 3) \ne (1\ 3) = (1\ 2)(1\ 3\ 2) \) handles \( (1\ 3\ 2) \). Hence only \( \id \) commutes with everything.
:::

::: {#exr-permutations-and-cycles-b2}
[B2: Counting cycles]

Let \( n \in \nN \) and \( 2 \le k \le n \). Show that \( S_n \) contains exactly
\[
\frac{n!}{(n - k)! \, k}
\]
\( k \)-cycles. Check the formula for \( n = 4 \) by listing the cycles of \( S_4 \).
:::

::: {.solution}
We use one counting fact: *if a finite set is the union of \( N \) pairwise disjoint subsets with \( q \) elements each, it has \( Nq \) elements.* This is @fd2:prp-disjoint-union-count applied \( N - 1 \) times, by induction on \( N \), as in the proof of @prp-symmetric-group-order.

*Lists.* Let \( T_k \) be the set of lists \( (i_1, \dots, i_k) \) of **distinct** elements of \( \{1, \dots, n\} \). Then \( T_k \) has \( n(n - 1) \cdots (n - k + 1) \) elements, by induction on \( k \): \( T_0 \) has one element, the empty list, and \( T_{j+1} \) is the disjoint union, over the lists \( t \in T_j \), of the sets of lists extending \( t \) by a point \( x \) of the complement \( C \) of its entry set \( E \). Here \( E \) has \( j \) elements, since the entries are distinct, so \( j + \card{C} = n \) (@fd2:prp-subset-finite, @fd2:prp-disjoint-union-count, @fd2:cor-finite-size-unique) and \( C \) has \( n - j \) elements. By the counting fact, \( T_{j+1} \) has \( (n - j) \) times as many elements as \( T_j \). Since \( n(n - 1) \cdots (n - k + 1) \cdot (n - k)! = n! \), this number is \( n!/(n - k)! \).

*Lists to cycles.* Each list in \( T_k \) defines the \( k \)-cycle \( (i_1\ \cdots\ i_k) \), and every \( k \)-cycle arises this way. Two lists give the same cycle exactly when one is a rotation of the other. Indeed, rotations give the same cycle (the remark after @def-cycle). Conversely, if \( (i_1\ \cdots\ i_k) = (j_1\ \cdots\ j_k) = \gamma \), then \( j_1 \) lies in the support \( \{i_1, \dots, i_k\} \), say \( j_1 = i_c \), and then \( j_2 = \gamma(j_1) = i_{c+1} \), and so on around the loop: the second list is the first rotated to start at \( i_c \). The \( k \) rotations of a list are \( k \) different lists, since their first entries differ. So the lists fall into pairwise disjoint classes of \( k \) elements, one class per \( k \)-cycle, and by the counting fact, with \( N_k \) the number of \( k \)-cycles,
\[
k \, N_k = \frac{n!}{(n - k)!} .
\]
Dividing by \( k \) gives the formula.

*Check, \( n = 4 \).* Transpositions: \( 4!/(2! \cdot 2) = 6 \), namely \( (1\ 2), (1\ 3), (1\ 4), (2\ 3), (2\ 4), (3\ 4) \). \( 3 \)-cycles: \( 4!/(1! \cdot 3) = 8 \), two for each of the four sets of three points: \( (1\ 2\ 3), (1\ 3\ 2), (1\ 2\ 4), (1\ 4\ 2), (1\ 3\ 4), (1\ 4\ 3), (2\ 3\ 4), (2\ 4\ 3) \). \( 4 \)-cycles: \( 4!/(0! \cdot 4) = 6 \), starting at \( 1 \) with the other three points in any of their \( 3! = 6 \) orders: \( (1\ 2\ 3\ 4), (1\ 2\ 4\ 3), (1\ 3\ 2\ 4), (1\ 3\ 4\ 2), (1\ 4\ 2\ 3), (1\ 4\ 3\ 2) \).
:::

::: {#exr-permutations-and-cycles-b3}
[B3: The rotations of a square]

Label the corners of a square \( 1, 2, 3, 4 \) in order around it. The quarter turn moves each label to the next corner, which is the permutation \( \rho = (1\ 2\ 3\ 4) \in S_4 \) (@exm-groups (e)).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \rho^2 \) and \( \rho^3 \) as products of disjoint cycles, and show \( \rho^4 = \id \).
2. Show that \( \langle \rho \rangle = \{ \id, \rho, \rho^2, \rho^3 \} \).
3. Show that \( [k] \mapsto \rho^k \) is a well-defined isomorphism \( (\nZ/4\nZ, +) \to \langle \rho \rangle \).
:::
:::

::: {.solution}
(a) \( \rho^2 = \rho\rho \) sends \( 1 \mapsto 2 \mapsto 3 \), \( 3 \mapsto 4 \mapsto 1 \), \( 2 \mapsto 3 \mapsto 4 \), \( 4 \mapsto 1 \mapsto 2 \): \( \rho^2 = (1\ 3)(2\ 4) \). Then \( \rho^3 = \rho^2\rho \) sends \( 1 \mapsto 2 \mapsto 4 \), \( 4 \mapsto 1 \mapsto 3 \), \( 3 \mapsto 4 \mapsto 2 \), \( 2 \mapsto 3 \mapsto 1 \): \( \rho^3 = (1\ 4\ 3\ 2) \). Finally \( \rho^4 = \rho^3\rho \) sends \( 1 \mapsto 2 \mapsto 1 \), \( 2 \mapsto 3 \mapsto 2 \), \( 3 \mapsto 4 \mapsto 3 \), \( 4 \mapsto 1 \mapsto 4 \): \( \rho^4 = \id \).

(b) By @def-subgroup-generated-by-element, \( \langle \rho \rangle = \{ \rho^k : k \in \nZ \} \). For \( k \in \nZ \), divide by \( 4 \): \( k = 4q + r \) with \( 0 \le r < 4 \) (@fd3:thm-integers-division-remainder (a)). By @prp-group-power-laws (a) and (c),
\[
\rho^k = (\rho^4)^q \rho^r = \id^q \rho^r = \rho^r ,
\]
where \( \id^q = (\rho^0)^q = \rho^{0} = \id \), again by (c). So every \( \rho^k \) is one of \( \rho^0 = \id, \rho, \rho^2, \rho^3 \), and all four lie in \( \langle \rho \rangle \).

(c) *Well defined.* If \( [k] = [k'] \) in \( \nZ/4\nZ \), then \( k' - k \in 4\nZ \) (@def-integers-mod-n-ring), so \( k' = k + 4q \) for some \( q \in \nZ \), and \( \rho^{k'} = \rho^k (\rho^4)^q = \rho^k \) as in (b). *Homomorphism.* \( [k] + [l] = [k + l] \mapsto \rho^{k + l} = \rho^k\rho^l \) by @prp-group-power-laws (a). *Bijective.* The four distinct classes \( [0], [1], [2], [3] \), which are all of \( \nZ/4\nZ \) (@thm-integers-mod-n-ring (b)), go to \( \id, \rho, \rho^2, \rho^3 \), which are four different permutations by (a) (they differ at the point \( 1 \): \( 1, 2, 3, 4 \)) and are all of \( \langle \rho \rangle \) by (b). So the map is a bijection, hence an isomorphism, and the four rotations of the square form a copy of \( \nZ/4\nZ \), as Section 3.1 announced.
:::

### C. Going deeper

::: {#exr-permutations-and-cycles-c1}
[C1: Dropping "disjoint"]

@prp-disjoint-cycles-commute assumes that the supports are disjoint.

::: {.enumerate options="label=(\alph*)"}
1. Find two transpositions that share exactly one point and do not commute.
2. Find two cycles in \( S_3 \) with the **same** support that do commute.
3. In the proof of @prp-disjoint-cycles-commute, which step fails for the pair of (a)?
:::
:::

::: {.solution}
(a) \( (1\ 2) \) and \( (2\ 3) \) share only the point \( 2 \). By the table of Exercise B1, \( (1\ 2)(2\ 3) = (1\ 2\ 3) \) and \( (2\ 3)(1\ 2) = (1\ 3\ 2) \), which differ (at \( 1 \): \( 2 \) versus \( 3 \)).

(b) \( (1\ 2\ 3) \) and \( (1\ 3\ 2) \) both have support \( \{1, 2, 3\} \). They are inverse to each other (the inverse formula after @def-cycle), so both products are \( \id \): \( (1\ 2\ 3)(1\ 3\ 2) = \id = (1\ 3\ 2)(1\ 2\ 3) \). More generally every permutation commutes with its inverse and with its own powers (@prp-group-power-laws (a)). So disjointness is sufficient for commuting, not necessary.

(c) Case 1 at the point \( i = 1 \in \supp (1\ 2) \): the proof needs \( \sigma(i) = 2 \notin \supp \tau \), so that \( \tau \) fixes it. Here \( \tau = (2\ 3) \) moves \( 2 \), so \( (\tau\sigma)(1) = \tau(2) = 3 \), while \( (\sigma\tau)(1) = \sigma(1) = 2 \).
:::

::: {#exr-permutations-and-cycles-c2}
[C2: Powers of disjoint cycles]

::: {.enumerate options="label=(\alph*)"}
1. Let \( \sigma = (i_1\ \cdots\ i_k) \in S_n \) be a \( k \)-cycle and \( m \in \nZ_{>0} \). Prove that \( \sigma^m = \id \) if and only if \( k \mid m \).
2. Let \( \sigma \) be a \( k \)-cycle and \( \tau \) an \( l \)-cycle in \( S_n \), disjoint. Prove that, for every \( m \in \nZ_{>0} \), \( (\sigma\tau)^m = \id \) if and only if \( k \mid m \) and \( l \mid m \).
3. Deduce that the least \( m \ge 1 \) with \( (\sigma\tau)^m = \id \) is the least positive common multiple of \( k \) and \( l \).
4. Find the least \( m \ge 1 \) with \( \bigl((1\ 2)(3\ 4\ 5)\bigr)^m = \id \) in \( S_5 \).
:::
:::

::: {.solution}
[Hint 1]

For (b): a power of \( \tau \) fixes every point that \( \tau \) fixes.
:::

::: {.solution}
[Hint 2]

Converse of (b): evaluate \( \sigma^m\tau^m = \id \) at a point of \( \supp \sigma \).
:::

::: {.solution}
(a) Read the indices of the entries modulo \( k \): for \( j \in \nZ \) let \( i_j \coloneqq i_t \), where \( t \in \{1, \dots, k\} \) and \( j \equiv t \pmod{k} \). Write \( j - 1 = kq + s \) with \( 0 \le s < k \) (@fd3:thm-integers-division-remainder (a)) and take \( t \coloneqq s + 1 \); \( t \) is unique because \( s \) is. Then \( \sigma(i_j) = i_{j+1} \) for every \( j \), which is @def-cycle. By induction on \( m \in \nN \) (@fd1:ax-induction), \( \sigma^m(i_j) = i_{j+m} \) for every \( j \): for \( m = 0 \) both sides are \( i_j \), and \( \sigma^{m+1}(i_j) = \sigma(\sigma^m(i_j)) = \sigma(i_{j+m}) = i_{j+m+1} \), using \( \sigma^{m+1} = \sigma\sigma^m \) (@prp-group-power-laws (a)). Every point off the cycle is fixed by \( \sigma \), hence by \( \sigma^m \). So \( \sigma^m = \id \) if and only if \( i_{j+m} = i_j \) for every \( j \). Since the entries \( i_1, \dots, i_k \) are distinct, \( i_{j+m} = i_j \) holds exactly when \( j + m \equiv j \pmod{k} \), that is, when \( k \mid m \).

(b) The supports are disjoint, so \( \sigma\tau = \tau\sigma \) (@prp-disjoint-cycles-commute), and \( (\sigma\tau)^m = \sigma^m\tau^m \) by @prp-group-power-laws (d). If \( k \mid m \) and \( l \mid m \), then \( \sigma^m = \tau^m = \id \) by (a), so \( (\sigma\tau)^m = \id \). Conversely, suppose \( \sigma^m\tau^m = \id \). Let \( x \in \supp \sigma \). Then \( x \notin \supp \tau \), so \( \tau(x) = x \), and by induction on \( m \) (@fd1:ax-induction) \( \tau^m(x) = x \) (Hint 1). Hence \( \sigma^m(x) = \sigma^m(\tau^m(x)) = x \). Also \( \sigma^m \) fixes every \( x \notin \supp \sigma \), since \( \sigma \) does. So \( \sigma^m = \id \), and then \( \tau^m = \sigma^m\tau^m = \id \). By (a), \( k \mid m \) and \( l \mid m \).

(c) By (b), the \( m \ge 1 \) with \( (\sigma\tau)^m = \id \) are exactly the positive common multiples of \( k \) and \( l \). This set contains \( kl \), and so it has a least element (@fd3:prp-integer-least-element), the least positive common multiple of \( k \) and \( l \). By @exr-subgroups-c3, the common multiples of \( k \) and \( l \) are exactly the multiples of that number.

(d) \( (1\ 2) \) and \( (3\ 4\ 5) \) are disjoint, of lengths \( 2 \) and \( 3 \). The positive common multiples of \( 2 \) and \( 3 \) start \( 6, 12, \dots \) (a common multiple of \( 2 \) is even, and \( 3 \nmid 2, 4 \)), so the least \( m \) is \( 6 \).

**Marking scheme.** (10 points)
- 3: (a) the formula \( \sigma^m(i_j) = i_{j+m} \) with indices modulo \( k \), proved by induction, and the points off the cycle fixed.
- 1: (a) from distinctness of the entries to \( k \mid m \), in both directions.
- 2: (b) commuting from disjointness, cited, and \( (\sigma\tau)^m = \sigma^m\tau^m \) with the reason.
- 3: (b) the converse: from \( \sigma^m\tau^m = \id \), uses disjointness of the supports to get \( \sigma^m = \id \) and \( \tau^m = \id \).
- 1: (c) and (d), the least element named.

Second route: \( \sigma^m = \tau^{-m} \), with \( \supp \sigma^m \subseteq \supp \sigma \) and \( \supp \tau^{-m} \subseteq \supp \tau \), and these are disjoint, so both are \( \id \); this earns the same 3 points if both inclusions are justified.

Fatal errors (0 for the step): \( (\sigma\tau)^m = \sigma^m\tau^m \) without using that the cycles commute; "\( \sigma^m\tau^m = \id \) so \( \sigma^m = \tau^{-m} \), hence both are \( \id \)" with no use of disjointness.
:::

<!-- dependency ledger
def-symmetric-group (claim): supp sigma empty only for id | fd2:prp-function-equality, cited
def-symmetric-group (claim): the bottom row lists each point once | fd2:def-injective, fd2:def-surjective (sigma bijective); inline
def-symmetric-group (claim): S_0, S_1, S_2 have 1, 1, 2 elements | fd2:prp-empty-function (a); inline case analysis
def-cycle (claim): the cycle is a function and a bijection with inverse (i_k ... i_1); supp = {i_1, ..., i_k}; (i j)(i j) = id | distinctness of the entries, fd2:thm-bijection-iff-inverse, cited; inline
def-cycle (claim): (check after it) (2 4 1) = (1 2 4) != (1 4 2), two-line form 4 1 3 2 | inline pointwise check; verify/ch03/def-cycle.py
exm-cycle-notation (example): (1 3)(1 2) = (1 2 3), (1 2)(1 3) = (1 3 2), sigma = (1 3)(2 5 4) = (2 5 4)(1 3); S_n not abelian for n >= 3 | inline pointwise computation; verify/ch03/exm-cycle-notation.py
exm-cycle-notation (claim): (paragraph after it) S_n abelian exactly when n <= 2 | S_0, S_1, S_2 listed in the paragraph after def-symmetric-group; inline
exm-cycle-notation (claim): (warnings) left-to-right reading gives (1 3 2); (1 3 2)^2 = (1 2 3); sigma^2 tau^2 = id | inline; verify/ch03/exm-cycle-notation.py
exm-cycle-notation (claim): (check after the warnings) (1 2 3)(1 2) = (1 3) | verify/ch03/exm-cycle-notation.py
lem-permutations-fixing-last-point (proof): restriction of a function with codomain cut down | fd2 Section 1.4, "Restriction" paragraph (no label), with fd2:def-function; inline; verify/ch03/lem-permutations-fixing-last-point.py (n <= 4)
prp-disjoint-cycles-commute (proof): three cases | inline; verify/ch03/prp-disjoint-cycles-commute.py (exhaustive in S_5)
prp-symmetric-group-order (proof): n! read in N, 0! = 1, (n + 1)! = n!(n + 1); j n! + n! = (j + 1) n!; (n + 1) n! = (n + 1)! | fd2:def-sum-product (factorial) read on omega by F3.1's citing rule; arithmetic of N (fd3 thm-omega-arithmetic-laws); inline
prp-symmetric-group-order (proof): induction on n, and on j from base 1; fd2 finite-set results | fd1:ax-induction; fd2:thm-induction via fd3:cor-omega-identification (b); fd2:def-finite, fd2:prp-disjoint-union-count, read on omega (F3.1 citing rule, group (i)), cited
prp-symmetric-group-order (proof): tau(tau sigma) = (tau tau)sigma = sigma, tau tau = id | (G1), (G2) of def-group; tau tau = id for a swap, a pointwise check (fd2:prp-function-equality), used silently
prp-symmetric-group-order (claim): (aftermath) 3! = 6, 4! = 24, 10! = 3628800; the six elements of S_3 are distinct | inline arithmetic; verify/ch03/prp-symmetric-group-order.py
prp-symmetric-group-order (claim): (aftermath) six distinct elements are all of S_3 | fd2:prp-subset-finite, fd2:cor-finite-size-unique, cited
thm-disjoint-cycle-decomposition (proof): strong induction on card supp sigma; supports finite; pigeonhole; least element | fd1:thm-strong-induction, fd2:prp-subset-finite, fd2:cor-pigeonhole-finite-sets (a) (group (i) of F3.1's citing rule), fd3:prp-integer-least-element, cited
thm-disjoint-cycle-decomposition (proof): {0, 1, ..., n} has n + 1 elements | the count after fd2:def-finite, group (i) of F3.1's citing rule
thm-disjoint-cycle-decomposition (claim): (worked run) sigma = (1 4)(2 6 5) in S_6 | verify/ch03/thm-disjoint-cycle-decomposition.py
thm-disjoint-cycle-decomposition (claim): (check after the run) (1 3 5)(2 6) | verify/ch03/thm-disjoint-cycle-decomposition.py
thm-disjoint-cycle-decomposition (claim): uniqueness up to order | Groups (AL1.3), prose pointer, nothing depends on it
exr-permutations-and-cycles-a1 (solution): (a)-(d) products, inverse, run giving (1 2 5)(3 4) | verify/ch03/exr-permutations-and-cycles-a1.py
exr-permutations-and-cycles-b1 (solution): the table of S_3, squares, center | verify/ch03/exr-permutations-and-cycles-b1.py
exr-permutations-and-cycles-b2 (solution): counting fact (union of N disjoint q-sets has Nq elements); card T_k = n!/(n - k)!; number of k-cycles; n = 4: 6, 8, 6 | fd2:prp-disjoint-union-count with induction on N, read on omega; inline; verify/ch03/exr-permutations-and-cycles-b2.py (n <= 6)
exr-permutations-and-cycles-b2 (solution): complement of j entries has n - j points | fd2:prp-subset-finite, fd2:prp-disjoint-union-count, fd2:cor-finite-size-unique, cited
exr-permutations-and-cycles-b3 (solution): rho^2 = (1 3)(2 4), rho^3 = (1 4 3 2), rho^4 = id; k = 4q + r | fd3:thm-integers-division-remainder (a), prp-group-power-laws (a), (c), cited; verify/ch03/exr-permutations-and-cycles-b3.py
exr-permutations-and-cycles-b3 (solution): (c) k' = k + 4q; Z/4Z = {[0], ..., [3]} | def-integers-mod-n-ring, thm-integers-mod-n-ring (b), cited
exr-permutations-and-cycles-c1 (solution): (1 2)(2 3) != (2 3)(1 2); (1 2 3)(1 3 2) = id | exercise B1's table (an exercise cited from an exercise solution); verify/ch03/exr-permutations-and-cycles-c1.py
exr-permutations-and-cycles-c2 (solution): indices modulo k (t = s + 1, s the remainder of j - 1); congruence mod k; k | m iff j + m = j mod k; tau^m fixes the points tau fixes | fd3:thm-integers-division-remainder (a), fd2:def-congruence, fd1:ax-induction; inline; verify/ch03/exr-permutations-and-cycles-c2.py
exr-permutations-and-cycles-c2 (solution): common multiples of k and l are the multiples of the least one | exr-subgroups-c3, an exercise cited from an exercise solution (STYLE, section 6); not needed for (c) itself
-->
