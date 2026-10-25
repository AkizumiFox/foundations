# Parked: Chapter 6 reserve exercises

<!-- Parked from fd2 (blueprint fd2/authoring/blueprints/ch06-axiom-of-choice.md §3 "Parked", layout-six-chapters.md, approved 2026-10-26). Not part of any book's src; nothing builds or scans it.
Old sections: fd2 at 09cf1f1, ch06-axiom-of-choice/01-countable-unions-and-choice.md (old 3.2, 3.5 material) and 02-chains-and-zorn.md, 03-using-zorn.md (old 6.1, 6.2)
Labels: exr-infinite-sets-a1, exr-infinite-sets-b1, exr-infinite-sets-b3, exr-infinite-sets-c1, exr-countable-unions-and-choice-b3, exr-chains-and-zorn-a1, exr-chains-and-zorn-b3, exr-using-zorn-b1, exr-using-zorn-b3, exr-using-zorn-r3
Intended home: none; reserve exercises
Text copied verbatim from 09cf1f1 at the fd2 wrap-up, 2026-10-26; ledger items in ../ledger-parked.yaml (parked_file: ch06-exercises.md); sidecars in verify/ch06/.
-->

<!-- from 01-countable-unions-and-choice.md -->
::: {#exr-infinite-sets-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Where does the proof of @thm-infinite-countable-subset use @ax-choice? Why is one \( \rulename{\exists E} \) per step not enough?
2. True or false, with a reason: every infinite subset of \( \nR \) contains a countably infinite subset; every uncountable set contains an uncountable proper subset.
3. Write down the bijection \( X \to X \setminus \{x_0\} \) of the proof of @thm-infinite-iff-proper-subset for \( X = \nZ \) and \( x_n = n \) for \( n \in \nN \).
4. For \( X = \nN \), is choice needed to find a countably infinite subset?
:::
:::

::: {.solution}
(a) At the line "By @ax-choice there is a function \( c \) with \( c(S) \in S \) for every non-empty \( S \subseteq X \)." One \( \rulename{\exists E} \) names one element of one non-empty set; that would give \( x_0 \), then \( x_1 \), and any finite number of steps. But @thm-recursion needs the step as a **function** \( g \), defined once for every stage \( F \) at once, before the sequence exists. Defining \( g \) means picking an element of \( X \setminus F \) for every such \( F \) simultaneously, and that is what the axiom provides.

(b) Both are true. The first is @thm-infinite-countable-subset applied to the infinite subset. For the second, let \( X \) be uncountable; then \( X \ne \emptyset \), and for \( x \in X \), \( X \setminus \{x\} \) is an uncountable proper subset, by the Quick check after the warning above.

(c) \( h(n) = n + 1 \) for \( n \in \nN \), and \( h(k) = k \) for \( k < 0 \). It maps \( \nZ \) onto \( \nZ \setminus \{0\} \): a positive \( m \) is \( h(m - 1) \), and a negative \( k \) is \( h(k) \).

(d) No. \( \nN \) itself is countably infinite, via \( \id_{\nN} \). (More generally, an infinite \( X \subseteq \nN \) can be listed in increasing order by @lem-subsets-of-naturals, a rule.)
:::

<!-- from 01-countable-unions-and-choice.md -->
::: {#exr-infinite-sets-b1}
[B1: Removing finitely many points]

Let \( X \) be infinite and let \( F \subseteq X \) be finite. Prove that \( \card{X \setminus F} = \card{X} \).
:::

::: {.solution}
First, \( X \setminus F \) is infinite: otherwise \( X = (X \setminus F) \cup F \) would be a union of two disjoint finite sets, finite by @prp-disjoint-union-count.

By @thm-infinite-countable-subset applied to \( X \setminus F \) (this uses @ax-choice), there is an injection \( n \mapsto s_n \) from \( \nN \) to \( X \setminus F \); let \( S \coloneqq \{ s_n : n \in \nN \} \). Let \( F \) have \( k \) elements, and let \( \varphi \colon \{1, \dots, k\} \to F \) be a bijection (@def-finite). No two of \( X \setminus (F \cup S) \), \( F \) and \( S \) meet, and together they make up \( X \); and \( X \setminus F \) is the union of the disjoint sets \( X \setminus (F \cup S) \) and \( S \). Define \( h \colon X \to X \setminus F \) by
\[
h(x) \coloneqq
\begin{cases}
x & \text{if } x \notin F \cup S, \\
s_{i-1} & \text{if } x = \varphi(i), \ i \in \{1, \dots, k\}, \\
s_{n+k} & \text{if } x = s_n, \ n \in \nN .
\end{cases}
\]
Each \( x \) falls under one case, with one \( i \) or one \( n \), since \( \varphi \) and \( n \mapsto s_n \) are injective. The second case sends \( F \) bijectively onto \( \{s_0, \dots, s_{k-1}\} \), and the third sends \( S \) bijectively onto \( \{ s_m : m \ge k \} \); these two image sets are disjoint and together make up \( S \). The first case is the identity on \( X \setminus (F \cup S) \). So \( h \) is a bijection, and \( \card{X \setminus F} = \card{X} \). (For \( k = 0 \), \( F = \emptyset \) and \( h \) is the identity.)
:::

<!-- from 01-countable-unions-and-choice.md -->
::: {#exr-infinite-sets-b3}
[B3: A big hole]

Give an example of an infinite set \( X \) and a proper subset \( Y \subsetneq X \) with \( \card{Y} = \card{X} \) and \( X \setminus Y \) infinite. Check each property, and list the properties any answer must have.
:::

::: {.solution}
*An answer must have:* (1) \( Y \subseteq X \); (2) \( Y \ne X \); (3) a bijection \( X \to Y \), or injections both ways; (4) \( X \) infinite; (5) \( X \setminus Y \) infinite. (The hole \( X \setminus Y \) in the proof of @thm-infinite-iff-proper-subset was the single point \( x_0 \); this asks for more.)

*Example:* \( X = \nN \), \( Y = 2\nN \). (1), (2): \( 2\nN \subseteq \nN \) and \( 1 \notin 2\nN \). (3): \( n \mapsto 2n \) is a bijection \( \nN \to 2\nN \) (@exm-hilbert-hotel). (4): \( \nN \) is infinite (@exm-hilbert-hotel). (5): \( X \setminus Y \) is the set of odd numbers (every \( m \in \nN \) is even or odd, not both, by @thm-division-algorithm), and \( n \mapsto 2n + 1 \) is a bijection from \( \nN \) onto it; if it were finite, \( \nN \) would be finite too (compose with a bijection from \( \{1, \dots, k\} \), @thm-composition-injective-surjective), which it is not.

Another correct answer: \( X = \nR \), \( Y = (0, \infty) \). (1), (2): \( (0, \infty) \subseteq \nR \) and \( 0 \notin (0, \infty) \). (3): @exm-reals-open-interval. (4), (5): \( n \mapsto -n \) is a bijection from \( \nN \) onto \( \{ -n : n \in \nN \} \), so this set is infinite, as in (5) above. It lies inside \( X \setminus Y = (-\infty, 0] \subseteq \nR \), so by @prp-subset-finite neither \( (-\infty, 0] \) nor \( \nR \) is finite.
:::

<!-- from 01-countable-unions-and-choice.md -->
::: {#exr-infinite-sets-c1}
[C1: Increasing functions]

A function \( f \colon \nN \to \nN \) is **strictly increasing** if \( f(m) < f(n) \) whenever \( m < n \). Let \( I \) be the set of strictly increasing functions \( \nN \to \nN \). Prove that \( I \) is uncountable.

Below, the proof is started; the second half is blank. *Name the move, then complete it.*

> Let \( n \mapsto f_n \) be any function from \( \nN \) to \( I \). By @thm-recursion, applied with the set \( \nN \), the starting value \( f_0(0) + 1 \) and the function \( (n, x) \mapsto \max\{ x, f_{n+1}(n + 1) \} + 1 \) from \( \nN \times \nN \) to \( \nN \) (a step that depends on \( n \)), there is a function \( g \colon \nN \to \nN \) with
> \[
> g(0) = f_0(0) + 1, \qquad g(n + 1) = \max\{ g(n), f_{n+1}(n + 1) \} + 1 .
> \]
> \( \underline{\hspace{8em}} \)
:::

::: {.solution}
[Hint 1]

Two things must be shown about \( g \): that it lies in \( I \), and that it differs from each \( f_n \) somewhere. Where?
:::

::: {.solution}
[Hint 2]

The second half begins: "For every \( n \in \nN \), \( g(n + 1) \ge g(n) + 1 > g(n) \)."
:::

::: {.solution}
The move is **the diagonal**: given any list, build an object that differs from the \( n \)-th entry at the \( n \)-th place. Here the object must also stay inside \( I \), which is why \( g(n + 1) \) is pushed above \( g(n) \) as well as above \( f_{n+1}(n + 1) \).

*Completion.* For every \( n \in \nN \), \( g(n + 1) = \max\{ g(n), f_{n+1}(n + 1) \} + 1 \ge g(n) + 1 > g(n) \). From this, \( g(m) < g(n) \) whenever \( m < n \), by induction on \( n \) (@thm-induction with base \( m + 1 \)): \( g(m) < g(m + 1) \), and \( g(m) < g(n) < g(n + 1) \). So \( g \in I \).

Next, \( g(n) > f_n(n) \) for every \( n \in \nN \): for \( n = 0 \), \( g(0) = f_0(0) + 1 \); for \( n = k + 1 \), \( g(k + 1) \ge f_{k+1}(k + 1) + 1 \). So \( g(n) \ne f_n(n) \), and hence \( g \ne f_n \), for every \( n \in \nN \). So \( g \in I \) is not a value of \( n \mapsto f_n \), and no function \( \nN \to I \) is onto. Since \( I \ne \emptyset \) (it contains \( \id_{\nN} \)), \( I \) is not countable.

**Marking scheme.** (10 points)
- 1: names the diagonal move.
- 4: shows \( g \) is strictly increasing: 2 for the step \( g(n) < g(n + 1) \) for every \( n \), and 2 for the passage to all \( m < n \).
- 3: shows \( g(n) > f_n(n) \) for every \( n \), treating \( n = 0 \) and \( n = k + 1 \) separately, and concludes \( g \ne f_n \).
- 2: concludes that no function \( \nN \to I \) is onto and, noting \( I \ne \emptyset \) (\( \id_{\nN} \in I \)), that \( I \) is not countable.
Fatal errors (0 for the part concerned): taking \( g(n) < g(n + 1) \) alone as strict increase, with no passage to all \( m < n \); inferring \( g \ne f_n \) without exhibiting a point where they differ, or exhibiting one only for \( n \ge 1 \).

The max in \( g \) is needed: the plain diagonal \( g(n) \coloneqq f_n(n) + 1 \) need not be strictly increasing (for \( f_0(n) = 5 + n \) and \( f_1(n) = n \), it gives \( g(0) = 6 > g(1) = 2 \)).
:::

<!-- from 01-countable-unions-and-choice.md -->
::: {#exr-countable-unions-and-choice-b3}
[B3]

A **rational point** of the plane is a point of \( \nQ \times \nQ \). Prove that the set of lines in the plane that pass through two different rational points is countable. Does your proof use @ax-choice?
:::

::: {.solution}
Let \( D \coloneqq \{ (p, q) \in (\nQ \times \nQ) \times (\nQ \times \nQ) : p \ne q \} \). The set \( \nQ \times \nQ \) is countable by @thm-integers-rationals-countable and @cor-product-countable; so is its product with itself, again by @cor-product-countable, and so is the subset \( D \) (@prp-countable-subset). For \( (p, q) \in D \), let \( \mathrm{line}(p, q) \) be the line through \( p \) and \( q \), as a subset of \( \nR^2 \): \( \mathrm{line}(p, q) \coloneqq \{ p + t(q - p) : t \in \nR \} \). Two different points lie on exactly one line (school geometry), so the lines in question form the image \( \mathrm{line}(D) \), countable by @prp-countable-image. The map \( \mathrm{line} \) is a formula, so no choice is used.
:::

<!-- from 02-chains-and-zorn.md -->
::: {#exr-chains-and-zorn-a1}
[A1]

These questions are about the proof of @thm-choice-from-zorn.

::: {.enumerate options="label=(\alph*)"}
1. Where is "\( A_i \ne \emptyset \)" used, and which step fails without it?
2. Why does the chain step need @lem-chain-union only for \( n = 2 \)?
3. Run the proof on \( I = \{1, 2\} \), \( A_1 = \{0\} \), \( A_2 = \{5, 6\} \): list \( P \), name its maximal elements, and decide whether \( P \) has a greatest element.
4. Which of the two hypotheses of @thm-zorn does the empty partially ordered set satisfy?
:::
:::

::: {.solution}
(a) In the last step: \( x_0 \in A_{i_0} \) exists only because \( A_{i_0} \ne \emptyset \). Without it, \( M \) could miss \( i_0 \) and still be maximal, and indeed no choice function exists if some \( A_i \) is empty.

(b) Condition (C1) mentions one pair and (C2) mentions two; no condition defining \( P \) mentions more.

(c) \( U = \{0, 5, 6\} \), and
\[
P = \bigl\{ \emptyset, \{(1, 0)\}, \{(2, 5)\}, \{(2, 6)\}, \{(1, 0), (2, 5)\}, \{(1, 0), (2, 6)\} \bigr\}.
\]
The maximal elements are the last two, each the graph of a choice function. There is no greatest element: the two maximal elements are incomparable, and a greatest element would be maximal (@prp-greatest-maximal (a)), so it would be one of them and contain the other.

(d) The chain hypothesis, vacuously; not non-emptiness.
:::

<!-- from 02-chains-and-zorn.md -->
::: {#exr-chains-and-zorn-b3}
[B3: A small poset of partial injections]

Let \( A = \{1, 2\} \) and \( B = \{b\} \). List the relations \( G \subseteq A \times B \) in which each element of \( A \) and each element of \( B \) occurs in at most one pair, ordered by \( \subseteq \). Name the maximal elements. For each, is every element of \( A \) paired? Every element of \( B \)?
:::

::: {.solution}
They are \( \emptyset \), \( \{(1, b)\} \) and \( \{(2, b)\} \); the only other subset of \( A \times B \), \( \{(1, b), (2, b)\} \), fails because \( b \) occurs twice. The maximal elements are \( \{(1, b)\} \) and \( \{(2, b)\} \). Neither pairs every element of \( A \); each pairs every element of \( B \), and read backwards it is an injection \( B \to A \). (Section 6.3 shows that this always happens: a maximal partial injection uses up one side.)
:::

<!-- from 02-chains-and-zorn.md -->
::: {#exr-using-zorn-b1}
[B1: Name the move, then complete it]

Let \( R \) be a relation from \( A \) to \( B \) whose domain is \( A \) (@def-relation). Prove that there is a function \( f \colon A \to B \) whose graph is contained in \( R \).

Below, the proof is started; the second half is blank. *Name the move, then complete it.*

> Let \( P \) be the set of \( G \subseteq R \) such that each \( a \in A \) occurs in at most one pair of \( G \), ordered by \( \subseteq \). Then \( \emptyset \in P \).
> \( \underline{\hspace{8em}} \)
> Hence the graph of \( f \) is contained in \( R \).
:::

::: {.solution}
The move is the maximality template, @exm-method-maximality; steps (2) to (4) remain.

*Completion.* Let \( \sC \subseteq P \) be a non-empty chain. Its union lies in \( R \), and two pairs of the union lie in one member of \( \sC \) (@lem-chain-union (b)), so an element of \( A \) occurs in at most one pair of the union. The union is in \( P \) and is an upper bound of \( \sC \). By @thm-zorn, \( P \) has a maximal element \( M \). Suppose some \( a_0 \in A \) occurs in no pair of \( M \). Since \( a_0 \) is in the domain of \( R \), there is \( b_0 \) with \( (a_0, b_0) \in R \) (one use of \( \rulename{\exists E} \)). Then \( M \cup \{ (a_0, b_0) \} \subseteq R \), \( a_0 \) occurs in it once, and it is strictly larger than \( M \): a contradiction with maximality. So each \( a \in A \) occurs in exactly one pair of \( M \), and \( M \) is the graph of a function \( f \colon A \to B \) (@def-function), with \( M \subseteq R \).
:::

<!-- from 02-chains-and-zorn.md -->
::: {#exr-using-zorn-b3}
[B3: A total order on the plane]

On \( \nR^2 \), let \( (x_1, x_2) \le_p (y_1, y_2) \) mean \( x_1 \le y_1 \) and \( x_2 \le y_2 \); and let \( (x_1, x_2) \le_l (y_1, y_2) \) mean \( x_1 < y_1 \), or \( x_1 = y_1 \) and \( x_2 \le y_2 \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \le_p \) is a partial order and not total.
2. Show that \( \le_l \) is a total order containing \( \le_p \).
:::
:::

::: {.solution}
(a) (PO1), (PO2) and (PO3) for \( \le_p \) hold coordinate by coordinate, from the same properties of \( \le \) on \( \nR \); for (PO2), \( x_1 = y_1 \) and \( x_2 = y_2 \) give equal pairs. The points \( (0, 1) \) and \( (1, 0) \) are incomparable: \( 0 \le 1 \) but \( 1 \not\le 0 \) in the second coordinate, and the reverse in the first.

(b) That \( \le_l \) is a total order is the argument of Section 5.3, Exercises A1 (d) and C1 (a), with \( \nR \) in place of \( \nN \): it uses only trichotomy and transitivity of \( \le \). Containment: if \( x_1 \le y_1 \) and \( x_2 \le y_2 \), then either \( x_1 < y_1 \), or \( x_1 = y_1 \) and \( x_2 \le y_2 \); in both cases \( (x_1, x_2) \le_l (y_1, y_2) \).
:::

<!-- from 02-chains-and-zorn.md -->
::: {#exr-using-zorn-r3}
[R3: The basis theorem, read as a template]

This item is optional and goes with the optional subsection. A set of vectors is linearly independent when no finite non-trivial combination of its vectors is \( 0 \).

::: {.enumerate options="label=(\alph*)"}
1. Which of the template's four steps uses that independence is tested on finitely many vectors at a time?
2. Why would the template fail for the property "\( S \) is a finite independent set"?
3. A maximal element of a partial order need not be greatest. What does this say about bases?
:::
:::

::: {.solution}
(a) Step (2), the chains: a dependence among vectors of the union of a chain involves finitely many vectors, all in one member (@lem-chain-union (b)), and that member is independent.

(b) The union of a chain of finite sets need not be finite (the second warning of Section 6.2), so step (2) fails: the union need not be a partial object.

(c) This is the point of @exm-maximal-not-greatest. Maximal independent sets need not contain one another, so a vector space can have many bases, none of them greatest. In \( \nR^2 \), \( \{ (1, 0), (1, 1) \} \) and \( \{ (2, 0), (0, 3) \} \) are both bases, and neither contains the other.
:::

<!-- dependency ledger
exr-infinite-sets-a1 (solution): the Quick check after the warning (X \ {x} uncountable) | inline in the section (Quick check solution), not an exercise
exr-infinite-sets-b1 (solution): disjoint pieces, piecewise bijection is a bijection | inline
exr-infinite-sets-b3 (solution): a set equinumerous with a finite set is finite | inline (compose the bijections, thm-composition-injective-surjective, cited)
exr-infinite-sets-b3 (solution): (0, infinity) is an interval with more than one point; n -> -n a bijection N -> {-n : n in N}, so it is infinite; a superset of it is infinite | exm-reals-open-interval (cited); inline, as in the first answer; prp-subset-finite (cited)
exr-infinite-sets-c1 (solution): max{a, b} of two naturals exists and is >= each | prp-finite-max (F2.2 §03), used silently in the given half
exr-infinite-sets-c1 (solution): counterexample to the plain diagonal: f_0(n) = 5 + n, f_1(n) = n give g(0) = 6, g(1) = 2 | verify/ch06/exr-infinite-sets-c1.py
exr-countable-unions-and-choice-b3 (solution): two points lie on exactly one line | school geometry
exr-chains-and-zorn-a1 (solution): the enumeration of P for I = {1, 2} | finite check
exr-chains-and-zorn-b3 (solution): the three relations and the maximal ones | finite check
exr-using-zorn-b3 (solution): lexicographic order total | Section 5.3 Exercises A1 (d), C1 (a) (cited), with R for N; R order (school fact)
exr-using-zorn-r3 (solution): bases of R^2 | linear algebra (optional item; prose only; nothing depends on it)
-->
