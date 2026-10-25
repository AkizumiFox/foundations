# Infinite Sets

Section 3.4 compared sizes with injections. Here we ask where \( \nN \) sits in that comparison. Every infinite set we have met contains a copy of \( \nN \), and it is tempting to say that this must always happen by picking new elements one at a time; this section makes that picking exact. It turns out to need @ax-choice again, this time applied to a family with one set for each non-empty subset of the given set, and it gives two results: \( \nN \) is the smallest infinite size, and a set is infinite exactly when it is the same size as a proper part of itself.

## Every infinite set contains a copy of the natural numbers

The question has a goal theorem: we want to show that an infinite set \( X \) has a countably infinite subset, that is, a subset equinumerous with \( \nN \) (@def-countably-infinite). Equivalently, we want an injection \( \nN \to X \): its image is then such a subset.

::: {#thm-infinite-countable-subset}
[Infinite Sets Contain a Countably Infinite Subset]

Every infinite set \( X \) has a countably infinite subset. Equivalently, there is an injection \( \nN \to X \).
:::

::: {.idea}
The natural attempt picks \( x_0 \in X \), then \( x_1 \in X \setminus \{x_0\} \), then \( x_2 \in X \setminus \{x_0, x_1\} \), and so on. Each pick is possible, because a finite set cannot exhaust the infinite \( X \), and each single pick is one \( \rulename{\exists E} \). But "and so on" is a definition by recursion, and @thm-recursion needs a **function** \( g \) that says, once and for all, which new element to take after any finite stage. That function must pick an element from every non-empty set of the form \( X \setminus F \) at once, with no rule for doing so when \( X \) is arbitrary. So we let @ax-choice supply a choice function \( c \) on all non-empty subsets of \( X \) first, and then the recursion is an ordinary one, with \( c \) as its rule.
:::

::: {.proof}
Let \( X \) be infinite. The family \( (S)_{S \in \powerset{X} \setminus \{\emptyset\}} \), indexed by the non-empty subsets of \( X \) with each index as its own member, consists of non-empty sets, and its union is \( X \): every index is a subset of \( X \), and each \( x \in X \) lies in the index \( \{x\} \). **By @ax-choice** there is a function \( c \colon \powerset{X} \setminus \{\emptyset\} \to X \) with
\[
c(S) \in S \quad \text{for every non-empty } S \subseteq X .
\]
This is the one line of the proof that uses the axiom.

Define \( g \colon \nN \times \powerset{X} \to \powerset{X} \) by \( g(n, F) \coloneqq F \cup \{ c(X \setminus F) \} \) if \( F \ne X \), and \( g(n, F) \coloneqq F \) if \( F = X \). In the first case \( X \setminus F \) is non-empty, so \( c(X \setminus F) \) is defined; so \( g \) is a function. By @thm-recursion, applied with the set \( \powerset{X} \), the starting value \( \emptyset \) and this \( g \), there are sets \( F_n \subseteq X \), for \( n \in \nN \), with \( F_0 = \emptyset \) and \( F_{n+1} = g(n, F_n) \).

We show by induction (@fd1:ax-induction) that **\( F_n \) has exactly \( n \) elements, for every \( n \in \nN \)**. For \( n = 0 \), \( F_0 = \emptyset \) has \( 0 \) elements (@def-finite). Suppose \( F_n \) has \( n \) elements. Then \( F_n \) is finite and \( X \) is not, so \( F_n \ne X \), and \( F_{n+1} = F_n \cup \{ c(X \setminus F_n) \} \) with \( c(X \setminus F_n) \in X \setminus F_n \). This is a union of disjoint sets with \( n \) elements and \( 1 \) element, so \( F_{n+1} \) has \( n + 1 \) elements by @prp-disjoint-union-count.

In particular \( F_n \ne X \) for every \( n \in \nN \), so we may define
\[
x_n \coloneqq c(X \setminus F_n) \in X \setminus F_n , \qquad\text{and then}\qquad F_{n+1} = F_n \cup \{x_n\} .
\]
Hence \( F_n \subseteq F_{n+1} \) for every \( n \), and by induction on \( k \), \( F_m \subseteq F_{m+k} \) for all \( m, k \in \nN \).

Now let \( m, n \in \nN \) with \( m < n \). Then \( x_m \in F_{m+1} \subseteq F_n \), because \( m + 1 \le n \) (@lem-naturals-arithmetic (e)), so \( k \coloneqq n - (m + 1) \in \nN \) (@lem-naturals-arithmetic (d)) and \( F_{m+1} \subseteq F_{(m+1)+k} = F_n \); and \( x_n \notin F_n \). So \( x_m \ne x_n \). Hence \( n \mapsto x_n \) is an injection \( \nN \to X \). Its image \( \{ x_n : n \in \nN \} \subseteq X \) is equinumerous with \( \nN \), since \( n \mapsto x_n \) is a bijection from \( \nN \) onto it. This proves the theorem.
:::

The proof shows where the axiom enters and why one \( \rulename{\exists E} \) per step is not enough: \( \rulename{\exists E} \) names one element for one set, while the recursion needs \( g \) as a single function defined on every stage at once. Each \( F_n \) is then determined by \( c \); the only arbitrary thing is \( c \) itself.

**A non-example by a minimal change.** Run the same construction on the finite set \( X = \{a, b\} \), with \( a \ne b \). The choice function \( c \) and the recursion still make sense, since \( g \) is defined on every \( F \subseteq X \). But \( F_1 = \{ c(X) \} \) has one element, \( F_2 \) adds the other, so \( F_2 = X \), and from then on \( g \) leaves \( F_n \) unchanged. So \( x_2 = c(X \setminus F_2) = c(\emptyset) \) is not defined. The step that fails is "\( F_n \) is finite and \( X \) is not, so \( F_n \ne X \)", exactly where the hypothesis that \( X \) is infinite is used.

::: {.remark}
Compare *Analysis on the Real Line*, Chapter 1's proof that the real numbers cannot be listed. There, a given list is used to build nested closed intervals, and each interval is obtained from the previous one by an explicit rule (keep an outer third that misses the next point of the list), so no choice principle is involved. Here \( X \) is an arbitrary infinite set, and there is no rule available for picking an element of an arbitrary non-empty subset of it; the choice function **is** the rule.
:::

For a particular \( X \) a rule may exist: for \( X \subseteq \nN \), "the least element" is one (@thm-well-ordering), and then the proof needs no axiom. That the theorem cannot be proved in general from the other rules of set formation alone is a result of set theory; we state it without proof, and nothing depends on it.

## Consequences: the smallest infinite size

The theorem says \( \card{\nN} \le \card{X} \) for every infinite \( X \) (@def-card-le). Three consequences follow at once.

- **\( \nN \) is the smallest infinite size.** If \( X \) is infinite and \( \card{X} \le \card{\nN} \), then \( \card{X} = \card{\nN} \), by @thm-schroder-bernstein and the theorem. So no infinite set is strictly smaller than \( \nN \).
- **Countable sets are exactly the sets of size at most \( \card{\nN} \)**, by @thm-countable-characterizations, (i) \( \iff \) (ii). Combining with the first point: a countable set is finite or equinumerous with \( \nN \), which @thm-countable-characterizations (iii) already said.
- **An uncountable set is strictly bigger than \( \nN \).** If \( X \) is uncountable, then \( X \) is infinite (a finite set is countable, by @thm-countable-characterizations), so \( \card{\nN} \le \card{X} \); and \( \card{\nN} = \card{X} \) would make \( X \) countable. So \( \card{\nN} < \card{X} \). For example \( \card{\nN} < \card{\nR} \), since \( \nR \) is uncountable (@thm-reals-uncountable-decimal).

::: {.warning}
"Infinite" and "uncountable" are different words. \( \nQ \) is infinite (it contains \( \nN \), which is infinite by @exm-hilbert-hotel, and a subset of a finite set is finite, by @prp-subset-finite) and countable (@thm-integers-rationals-countable). Likewise "\( X \) contains a copy of \( \nN \)" is not "\( X \) is equinumerous with \( \nN \)": \( \nR \) contains \( \nN \), and \( \card{\nN} < \card{\nR} \) (as above).
:::

::: {.check}
Let \( X \) be uncountable. Is \( X \setminus \{x\} \) uncountable for every \( x \in X \)? Why must \( X \) have an element at all?
:::

::: {.solution}
\( X \ne \emptyset \), because \( \emptyset \) is countable by @def-countable. For \( x \in X \), if \( X \setminus \{x\} \) were countable, then \( X = (X \setminus \{x\}) \cup \{x\} \) would be a union of two countable sets, countable by @prp-union-two-countable. So \( X \setminus \{x\} \) is uncountable.
:::

## Infinite sets are the same size as a proper part

Section 2.5 proved that a finite set is never equinumerous with a proper subset (@thm-finite-no-proper-copy), and @exm-hilbert-hotel showed \( \nN \) doing exactly that. With @thm-infinite-countable-subset, the hotel can be built inside any infinite set: run it on the copy of \( \nN \), and leave everything else alone.

::: {#thm-infinite-iff-proper-subset}
[Infinite Sets and Proper Subsets]

A set \( X \) is infinite if and only if \( \card{X} = \card{Y} \) for some proper subset \( Y \subsetneq X \).
:::

::: {.idea}
One direction is already done: Section 2.5 showed that finite sets have no proper subset of their own size. For the other, take the copy \( x_0, x_1, x_2, \dots \) of \( \nN \) inside \( X \) and move every guest one room up, \( x_n \mapsto x_{n+1} \), as \( n \mapsto n + 1 \) does in the Quick check after @exm-hilbert-hotel. Room \( x_0 \) is vacated, and every point outside the copy stays where it is.
:::

::: {.proof}
\( (\Leftarrow) \) This is the contrapositive of @thm-finite-no-proper-copy: a finite set is not equinumerous with any proper subset, so a set that is equinumerous with one is not finite.

\( (\Rightarrow) \) Let \( X \) be infinite. By @thm-infinite-countable-subset there is an injection \( n \mapsto x_n \) from \( \nN \) to \( X \); let \( S \coloneqq \{ x_n : n \in \nN \} \). Each element of \( S \) is \( x_n \) for exactly one \( n \in \nN \), by injectivity. Define \( h \colon X \to X \setminus \{x_0\} \) by
\[
h(x) \coloneqq
\begin{cases}
x_{n+1} & \text{if } x = x_n \text{ with } n \in \nN, \\
x & \text{if } x \notin S .
\end{cases}
\]
This is a function into \( X \setminus \{x_0\} \): \( x_{n+1} \ne x_0 \) because \( n + 1 \ne 0 \), and an \( x \notin S \) is not \( x_0 \).

*\( h \) is injective.* Two points of \( S \): \( x_{m+1} = x_{n+1} \) gives \( m + 1 = n + 1 \), so \( m = n \). Two points outside \( S \): \( h \) is the identity there. One of each: \( h(x_n) = x_{n+1} \in S \), while \( h(x) = x \notin S \), so the values differ.

*\( h \) is onto \( X \setminus \{x_0\} \).* Let \( y \in X \setminus \{x_0\} \). If \( y \notin S \), then \( y = h(y) \). If \( y \in S \), then \( y = x_m \) with \( m \ne 0 \), so \( n \coloneqq m - 1 \in \nN \) (@lem-naturals-arithmetic (c)) and \( y = x_{n+1} = h(x_n) \).

So \( h \) is a bijection, and \( Y \coloneqq X \setminus \{x_0\} \) is a proper subset of \( X \), as \( x_0 \in X \setminus Y \), with \( \card{X} = \card{Y} \). This proves the theorem.
:::

Together with Section 2.5, this gives a characterization of "infinite" that never mentions \( \nN \) or counting: a set is infinite precisely when some proper part of it is as big as the whole. The finite intuition "a part is smaller than the whole" is exactly the property that separates finite sets from infinite ones. The direction \( (\Rightarrow) \) used @ax-choice, through @thm-infinite-countable-subset; the direction \( (\Leftarrow) \) did not.

::: {.check}
Name a proper subset of \( \nR \) that is equinumerous with \( \nR \), and give a bijection.
:::

::: {.solution}
\( (-1, 1) \), with the bijection \( x \mapsto x/(1 + \abs{x}) \) of @exm-reals-open-interval. (Any interval with more than one point other than \( \nR \) itself works, by the same example.) No choice is needed for \( \nR \): the bijection is a formula.
:::

## Exercises

### A. Check your understanding

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

### B. Practice

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

::: {#exr-infinite-sets-b2}
[B2: Absorbing a countable set]

Let \( X \) be infinite, and let \( C \) be countable with \( C \cap X = \emptyset \). Prove that \( \card{X \cup C} = \card{X} \).

*Hint: absorb \( C \) into a countably infinite subset of \( X \).*
:::

::: {.solution}
By @thm-infinite-countable-subset (using @ax-choice) there is a countably infinite \( S \subseteq X \). The set \( S \cup C \) is countable by @prp-union-two-countable, and infinite, because it contains \( S \) (a subset of a finite set is finite, @prp-subset-finite), which is infinite: if \( \varphi \colon \{1, \dots, k\} \to S \) were a bijection and \( \beta \colon \nN \to S \) is a bijection given by the theorem, then \( \beta^{-1} \circ \varphi \) would be a bijection \( \{1, \dots, k\} \to \nN \) (@prp-equinumerous-properties, @thm-composition-injective-surjective), against @exm-hilbert-hotel. By @thm-countable-characterizations (iii), \( S \cup C \) is countably infinite. So \( \card{S \cup C} = \card{\nN} = \card{S} \), and @prp-equinumerous-properties gives a bijection \( \psi \colon S \cup C \to S \).

Now \( X \cup C \) is the union of the disjoint sets \( X \setminus S \) and \( S \cup C \) (disjoint because \( C \cap X = \emptyset \)), and \( X \) is the union of the disjoint sets \( X \setminus S \) and \( S \). Define \( h \colon X \cup C \to X \) by \( h(x) \coloneqq x \) for \( x \in X \setminus S \) and \( h(x) \coloneqq \psi(x) \) for \( x \in S \cup C \). It is a bijection on each piece, onto the corresponding piece, so it is a bijection, and \( \card{X \cup C} = \card{X} \).
:::

::: {#exr-infinite-sets-b3}
[B3: A big hole]

Give an example of an infinite set \( X \) and a proper subset \( Y \subsetneq X \) with \( \card{Y} = \card{X} \) and \( X \setminus Y \) infinite. Check each property, and list the properties any answer must have.
:::

::: {.solution}
*An answer must have:* (1) \( Y \subseteq X \); (2) \( Y \ne X \); (3) a bijection \( X \to Y \), or injections both ways; (4) \( X \) infinite; (5) \( X \setminus Y \) infinite. (The hole \( X \setminus Y \) in the proof of @thm-infinite-iff-proper-subset was the single point \( x_0 \); this asks for more.)

*Example:* \( X = \nN \), \( Y = 2\nN \). (1), (2): \( 2\nN \subseteq \nN \) and \( 1 \notin 2\nN \). (3): \( n \mapsto 2n \) is a bijection \( \nN \to 2\nN \) (@exm-hilbert-hotel). (4): \( \nN \) is infinite (@exm-hilbert-hotel). (5): \( X \setminus Y \) is the set of odd numbers (every \( m \in \nN \) is even or odd, not both, by @thm-division-algorithm), and \( n \mapsto 2n + 1 \) is a bijection from \( \nN \) onto it; if it were finite, \( \nN \) would be finite too (compose with a bijection from \( \{1, \dots, k\} \), @thm-composition-injective-surjective), which it is not.

Another correct answer: \( X = \nR \), \( Y = (0, \infty) \). (1), (2): \( (0, \infty) \subseteq \nR \) and \( 0 \notin (0, \infty) \). (3): @exm-reals-open-interval. (4), (5): \( n \mapsto -n \) is a bijection from \( \nN \) onto \( \{ -n : n \in \nN \} \), so this set is infinite, as in (5) above. It lies inside \( X \setminus Y = (-\infty, 0] \subseteq \nR \), so by @prp-subset-finite neither \( (-\infty, 0] \) nor \( \nR \) is finite.
:::

### C. Going deeper

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

::: {#exr-infinite-sets-c2}
[C2: The irrationals]

Deduce from @exr-infinite-sets-b2 that \( \card{\nR \setminus \nQ} = \card{\nR} \).
:::

::: {.solution}
The set \( \nR \setminus \nQ \) is uncountable: otherwise \( \nR = (\nR \setminus \nQ) \cup \nQ \) would be a union of two countable sets (@thm-integers-rationals-countable), countable by @prp-union-two-countable, against @thm-reals-uncountable-decimal. An uncountable set is infinite, since finite sets are countable (@thm-countable-characterizations). Now apply @exr-infinite-sets-b2 with \( X \coloneqq \nR \setminus \nQ \) and \( C \coloneqq \nQ \), which is countable and disjoint from \( X \): \( \card{(\nR \setminus \nQ) \cup \nQ} = \card{\nR \setminus \nQ} \), and the left side is \( \card{\nR} \).
:::

<!-- dependency ledger
thm-infinite-countable-subset (proof): the family (S) indexed by P(X) \ {empty}, union equal to X | def-indexed-family, def-family-union-intersection (F2.1 §03), used silently; ax-choice (cited)
thm-infinite-countable-subset (proof): a singleton {x} has 1 element | def-finite (cited): the bijection 1 -> x from {1}
thm-infinite-countable-subset (proof): F_m subset of F_(m+k), induction on k | inline (ax-induction, cited)
thm-infinite-countable-subset (claim): (remark) AN1.1's nested-interval proof uses an explicit rule | AN1.1 §07 (prose pointer; nothing depends on it)
thm-infinite-countable-subset (claim): (prose after the remark) the theorem is not provable without choice | set theory, stated without proof; nothing depends on it
thm-infinite-iff-proper-subset (proof): m + 1 = n + 1 gives m = n; n + 1 != 0 | arithmetic of N (lem-naturals-arithmetic), used silently
exr-infinite-sets-a1 (solution): the Quick check after the warning (X \ {x} uncountable) | inline in the section (Quick check solution), not an exercise
exr-infinite-sets-b1 (solution): disjoint pieces, piecewise bijection is a bijection | inline
exr-infinite-sets-b2 (solution): disjoint pieces, piecewise bijection is a bijection | inline (as in B1)
exr-infinite-sets-b3 (solution): a set equinumerous with a finite set is finite | inline (compose the bijections, thm-composition-injective-surjective, cited)
exr-infinite-sets-b3 (solution): (0, infinity) is an interval with more than one point; n -> -n a bijection N -> {-n : n in N}, so it is infinite; a superset of it is infinite | exm-reals-open-interval (cited); inline, as in the first answer; prp-subset-finite (cited)
exr-infinite-sets-c1 (solution): max{a, b} of two naturals exists and is >= each | prp-finite-max (F2.2 §03), used silently in the given half
exr-infinite-sets-c1 (solution): counterexample to the plain diagonal: f_0(n) = 5 + n, f_1(n) = n give g(0) = 6, g(1) = 2 | verify/ch03/exr-infinite-sets-c1.py
-->
