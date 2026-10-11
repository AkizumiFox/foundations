# Comparing Sizes: the Schröder–Bernstein Theorem

We have \( (0, 1) \subseteq [0, 1] \subseteq \nR \). Are the three sets the same size? Section 8.1 made "same size" mean "there is a bijection", and for these sets a bijection is fiddly to write down: \( [0, 1] \) has two endpoints that \( (0, 1) \) lacks, and \( \nR \) is unbounded. An **injection**, on the other hand, is easy in both directions: the inclusion goes one way, and squeezing \( [0, 1] \) into the middle of \( (0, 1) \) goes the other. This section turns injections into a way of comparing sizes, and proves the theorem that makes the comparison useful: injections both ways give a bijection.

## Comparing sizes with injections

An injection \( A \to B \) places a copy of \( A \) inside \( B \): distinct elements of \( A \) go to distinct elements of \( B \), so \( B \) has room for all of \( A \). For finite sets this is the pigeonhole principle read the other way round (@cor-pigeonhole-finite-sets). It deserves a name for all sets.

*\( A \) is at most as big as \( B \) when \( A \) fits into \( B \) without collisions.*

::: {#def-card-le}
[Comparing Sizes]

Let \( A \) and \( B \) be sets. We write \( \card{A} \le \card{B} \), and say that **\( A \) is at most as big as \( B \)**, if **there exists** an injection \( A \to B \). We write \( \card{A} < \card{B} \), and say that **\( A \) is strictly smaller than \( B \)**, if \( \card{A} \le \card{B} \) and **not** \( \card{A} = \card{B} \): there is an injection \( A \to B \), and there is **no** bijection \( A \to B \).
:::

In words: "\( \le \)" asks for one injection, of our choosing. "\( < \)" asks for an injection **and** rules out every bijection, which is a statement about all functions \( A \to B \) at once. As with \( \card{A} = \card{B} \) in Section 8.1 (@def-equinumerous), the symbols \( \card{A} \le \card{B} \) and \( \card{A} < \card{B} \) are **relations between the sets** \( A \) and \( B \). No object \( \card{A} \) is defined for an infinite set, and nothing here compares two numbers.

**Examples.**

- *Subsets.* If \( A \subseteq B \), the inclusion \( a \mapsto a \) is an injection \( A \to B \), so \( \card{A} \le \card{B} \). In particular \( \card{(0, 1)} \le \card{[0, 1]} \le \card{\nR} \).
- *The degenerate case.* For every set \( B \), \( \card{\emptyset} \le \card{B} \): the empty function \( \emptyset \to B \) (@prp-empty-function (a)) is injective, vacuously, since there are no \( x_1, x_2 \in \emptyset \) to test.
- *Finite sets.* Let \( A \) have \( m \) elements and \( B \) have \( n \) elements (@def-finite). Then \( \card{A} \le \card{B} \) exactly when \( m \le n \). If \( m \le n \), take bijections \( \varphi \colon \{1, \dots, m\} \to A \) and \( \psi \colon \{1, \dots, n\} \to B \); the inclusion \( \iota \colon \{1, \dots, m\} \to \{1, \dots, n\} \) is injective, so \( \psi \circ \iota \circ \varphi^{-1} \colon A \to B \) is injective by @thm-composition-injective-surjective (a), \( \varphi^{-1} \) being a bijection (@thm-bijection-iff-inverse). If \( m > n \), there is no injection \( A \to B \) by @cor-pigeonhole-finite-sets (a). So the relation agrees with the count of elements, which is why it is allowed to borrow the symbol \( \le \).
- *Countable sets.* By @thm-countable-characterizations, (i) \( \iff \) (ii), a set \( A \) is countable if and only if \( \card{A} \le \card{\nN} \). "Countable" means "at most as big as \( \nN \)".
- *Power sets.* For every set \( X \), \( \card{X} < \card{\powerset{X}} \). The map \( x \mapsto \{x\} \) is an injection \( X \to \powerset{X} \), since \( \{x_1\} = \{x_2\} \) gives \( x_1 \in \{x_2\} \), so \( x_1 = x_2 \). And there is no bijection \( X \to \powerset{X} \), because by @thm-cantor there is not even a surjection. In particular \( \card{\nN} < \card{\powerset{\nN}} \).

**Non-example by minimal change.** Replace "injection" by "function" in the definition. Then any set would be "at most as big as" any non-empty set, by a constant map: \( \nR \to \{0\} \) would put \( \nR \) below a one-element set. The clause that carries the meaning is "no two elements collide".

::: {.warning}
\( \card{A} < \card{B} \) does **not** mean "there is an injection \( A \to B \) that is not a bijection". The map \( n \mapsto n + 1 \) is an injection \( \nN \to \nN \) that misses \( 0 \), and yet \( \card{\nN} = \card{\nN} \). For infinite sets one injection that fails to be onto proves nothing about strictness; \( \card{A} < \card{B} \) needs **every** map \( A \to B \) to fail to be a bijection, which is why Cantor's theorem, a statement about every \( f \colon X \to \powerset{X} \), is the source of our strict inequalities.
:::

The relation behaves like an order in two of the three ways. The third is the content of this section's theorem.

::: {#prp-card-le-preorder}
[Comparing Sizes Is Reflexive and Transitive]

For all sets \( A \), \( B \), \( C \):

::: {.enumerate options="label=(\alph*)"}
1. \( \card{A} \le \card{A} \);
2. if \( \card{A} \le \card{B} \) and \( \card{B} \le \card{C} \), then \( \card{A} \le \card{C} \).
:::
:::

::: {.proof}
(a) The identity \( \id_A \) is injective, since \( \id_A(x_1) = \id_A(x_2) \) says \( x_1 = x_2 \).

(b) Let \( f \colon A \to B \) and \( g \colon B \to C \) be injections. Then \( g \circ f \colon A \to C \) is injective by @thm-composition-injective-surjective (a). This proves the proposition.
:::

As with equinumerosity (Section 8.1, after @prp-equinumerous-properties), we do not call this a partial order: there is no set of all sets for it to be a relation on (@thm-russell). And antisymmetry, the clause (PO2) of @def-partial-order, would say "if \( \card{A} \le \card{B} \) and \( \card{B} \le \card{A} \), then \( A = B \)", which is false: \( \card{\nN} \le \card{2\nN} \) and \( \card{2\nN} \le \card{\nN} \), while \( 2\nN \ne \nN \). The right replacement for "\( A = B \)" is "\( \card{A} = \card{B} \)". That is the Schröder–Bernstein Theorem below.

Before it, one more way to read \( \le \). A countable set was defined by a surjection from \( \nN \), and @thm-countable-characterizations turned that into an injection into \( \nN \). The same exchange works for all sets, with one exception and one price.

::: {#prp-card-le-surjection}
[Injections and Surjections]

Let \( A \) and \( B \) be sets with \( A \ne \emptyset \). Then \( \card{A} \le \card{B} \) if and only if there is a surjection \( B \to A \).
:::

::: {.proof}
\( (\Rightarrow) \) Let \( f \colon A \to B \) be an injection. Since \( A \ne \emptyset \), @thm-left-inverse-iff-injective (b) gives a left inverse \( g \colon B \to A \), so \( g \circ f = \id_A \). This says that \( f \) is a right inverse of \( g \) (@def-left-right-inverse), so \( g \) is surjective by @prp-right-inverse-surjective.

\( (\Leftarrow) \) Let \( g \colon B \to A \) be a surjection. By @thm-surjection-right-inverse, \( g \) has a right inverse \( h \colon A \to B \), so \( g \circ h = \id_A \); **this step uses @ax-choice**, through @thm-surjection-right-inverse. Then \( g \) is a left inverse of \( h \), so \( h \) is injective by @thm-left-inverse-iff-injective (a). Hence \( \card{A} \le \card{B} \). This proves the proposition.
:::

The hypothesis \( A \ne \emptyset \) is needed for \( (\Rightarrow) \) only. For \( A = \emptyset \) and \( B = \{b\} \), the empty function is an injection \( \emptyset \to \{b\} \), but there is no function \( \{b\} \to \emptyset \) at all (@prp-empty-function (b)), let alone a surjection. The proof shows where the hypothesis enters: a left inverse \( g \colon B \to A \) must send \( b \) somewhere in \( A \). The choice in \( (\Leftarrow) \) is genuine in general, but not for \( B = \nN \): a surjection from \( \nN \) has least preimages, a rule, which is how @thm-countable-characterizations went from (i) to (ii) without the axiom.

::: {.check}
Is \( \card{\{0, 1\}^{\nN}} \le \card{\powerset{\nN}} \)? Give an injection, and say whether your answer needed @prp-card-le-surjection.
:::

::: {.solution}
Yes. Send a sequence \( a \in \{0, 1\}^{\nN} \) to the set \( \{ n \in \nN : a(n) = 1 \} \). If two sequences give the same set, they take the value \( 1 \) at the same places, and so the value \( 0 \) at the same places too; hence they are equal (@prp-function-equality), and the map is injective. No appeal to @prp-card-le-surjection is needed: the definition asks for an injection, and we wrote one down. (The map is in fact a bijection, with inverse \( S \mapsto \ind_S \); this is the correspondence of Section 6.4, recalled after @cor-powerset-naturals-uncountable.)
:::

## The Schröder–Bernstein Theorem

Here is the replacement for antisymmetry. To show two sets are the same size, it is enough to fit each into the other.

::: {#thm-schroder-bernstein}
[Schröder–Bernstein Theorem]

Let \( A \) and \( B \) be sets. If \( \card{A} \le \card{B} \) and \( \card{B} \le \card{A} \), then \( \card{A} = \card{B} \).
:::

::: {.idea}
Let \( f \colon A \to B \) and \( g \colon B \to A \) be the two injections. We want a bijection \( h \colon A \to B \), and at each \( a \in A \) there are two candidates: go forward, \( h(a) = f(a) \), or go back along \( g \): let \( h(a) \) be the unique \( b \) with \( g(b) = a \). Going back is possible only for \( a \in g(B) \). So a point of \( A \) **not hit by \( g \)** must be sent forward by \( f \). Then the point \( f(a) \in B \) is used up, and \( g(f(a)) \) must not go back to it, or \( h \) would collide; so \( g(f(a)) \) must also be sent forward, and then \( g(f(g(f(a)))) \), and so on along the chain. Everything reached this way goes forward; everything else goes back.

**Step roadmap.**

① Build the set \( C \subseteq A \) of points that are forced forward: \( C_0 \coloneqq A \setminus g(B) \), \( C_{n+1} \coloneqq g(f(C_n)) \), \( C \coloneqq \bigcup_{n \in \nN} C_n \).

② Define \( h(a) \coloneqq f(a) \) on \( C \), and let \( h(a) \) be the unique \( b \) with \( g(b) = a \) off \( C \).

③ Show \( h \) is injective; the only case with content is one point of each kind.

④ Show \( h \) is onto: for \( b \in B \), look at \( g(b) \) and ask whether it lies in \( C \).

*Before reading on: in step ④, why is \( g(b) \notin C_0 \), and what does that buy?*
:::

::: {.proof}
Let \( f \colon A \to B \) and \( g \colon B \to A \) be injections.

**Step 1.** By @thm-recursion, applied with the set \( \powerset{A} \), the starting value \( A \setminus g(B) \in \powerset{A} \) and the function \( (n, S) \mapsto g(f(S)) \) from \( \nN \times \powerset{A} \) to \( \powerset{A} \), there are sets \( C_n \subseteq A \), for \( n \in \nN \), with
\[
C_0 = A \setminus g(B), \qquad C_{n+1} = g\bigl(f(C_n)\bigr) \ \text{ for every } n \in \nN .
\]
Here \( f(C_n) \subseteq B \) and \( g(f(C_n)) \subseteq A \) are images (@def-image). Let \( C \coloneqq \bigcup_{n \in \nN} C_n \subseteq A \) (@def-family-union-intersection). Two facts about \( C \) will be used.

(F1) If \( a \in C \), then \( g(f(a)) \in C \). Indeed \( a \in C_n \) for some \( n \in \nN \); then \( f(a) \in f(C_n) \), so \( g(f(a)) \in g(f(C_n)) = C_{n+1} \subseteq C \).

(F2) If \( a \in A \setminus C \), there is **exactly one** \( b \in B \) with \( g(b) = a \). It exists because \( a \notin C_0 = A \setminus g(B) \) and \( a \in A \), so \( a \in g(B) \). It is unique because \( g \) is injective.

**Step 2.** Define \( h \colon A \to B \) by
\[
h(a) \coloneqq
\begin{cases}
f(a) & \text{if } a \in C, \\
\text{the unique } b \in B \text{ with } g(b) = a & \text{if } a \notin C .
\end{cases}
\]
Each \( a \in A \) falls under exactly one case, and in each case the value exists and is unique (in the second case by (F2)), so \( h \) is a function. Note that \( g(h(a)) = a \) whenever \( a \notin C \).

**Step 3.**

::: {.claim}
\( h \) is injective.
:::

::: {.proofofclaim}
Let \( a, a' \in A \) with \( h(a) = h(a') \).

*Case 1: \( a, a' \in C \).* Then \( f(a) = f(a') \), and \( a = a' \) because \( f \) is injective.

*Case 2: \( a, a' \notin C \).* Then \( a = g(h(a)) = g(h(a')) = a' \).

*Case 3: \( a \in C \) and \( a' \notin C \).* Then \( h(a') = h(a) = f(a) \), so \( a' = g(h(a')) = g(f(a)) \). By (F1), \( g(f(a)) \in C \), so \( a' \in C \), a contradiction. So this case does not occur.

The case \( a \notin C \), \( a' \in C \) is Case 3 with the roles of \( a \) and \( a' \) swapped. Hence \( a = a' \) in every case that occurs.
:::

**Step 4.**

::: {.claim}
\( h \) is surjective.
:::

::: {.proofofclaim}
Let \( b \in B \), and consider \( g(b) \in A \).

*Case 1: \( g(b) \notin C \).* Then \( h(g(b)) \) is the unique element of \( B \) whose image under \( g \) is \( g(b) \), and \( b \) is such an element. So \( h(g(b)) = b \).

*Case 2: \( g(b) \in C \).* Then \( g(b) \in C_n \) for some \( n \in \nN \). Since \( g(b) \in g(B) \), we have \( g(b) \notin A \setminus g(B) = C_0 \), so \( n \ne 0 \). By @lem-naturals-arithmetic (c), \( k \coloneqq n - 1 \in \nN \), and \( g(b) \in C_{k+1} = g(f(C_k)) \). By @def-image there is \( b' \in f(C_k) \) with \( g(b') = g(b) \), and then \( a \in C_k \) with \( f(a) = b' \). As \( g \) is injective, \( b = b' = f(a) \). Since \( a \in C_k \subseteq C \), \( h(a) = f(a) = b \).

In both cases \( b \) is a value of \( h \).
:::

By the two claims, \( h \colon A \to B \) is a bijection, so \( \card{A} = \card{B} \). This proves the theorem.
:::

The answer to the prompt: \( g(b) \) is a value of \( g \), and \( C_0 \) consists exactly of the points of \( A \) that are **not** values of \( g \). That is what pushes the index \( n \) of Case 2 up to at least \( 1 \), so that \( g(b) \) has a predecessor \( a \in C_{n-1} \) in its chain, and \( b \) is reached by \( f \) from that predecessor.

Every value of \( h \) is given by a rule, so the proof makes **no use of @ax-choice**: Step 1 is a recursion with an explicit step, and Step 2 picks the unique preimage, where there is nothing to choose. The case split "\( a \in C \) or \( a \notin C \)" is an instance of excluded middle, the classical step discussed in Section 5.7; nothing in the proof decides which case holds for a given \( a \), and nothing needs to.

Each hypothesis is used. Without the injection \( g \), the conclusion fails: \( \nN \to \powerset{\nN} \), \( n \mapsto \{n\} \), is an injection, and \( \card{\nN} \ne \card{\powerset{\nN}} \) by @thm-cantor. In the proof, injectivity of \( f \) is used once, in Case 1 of Step 3, and injectivity of \( g \) twice, in (F2) and in Case 2 of Step 4.

::: {.remark}
The theorem needs both \( \card{A} \le \card{B} \) and \( \card{B} \le \card{A} \); are any two sets comparable, that is, is it true that \( \card{A} \le \card{B} \) or \( \card{B} \le \card{A} \) for all \( A \) and \( B \)? The answer is yes, but the proof needs Zorn's lemma, a principle equivalent to @ax-choice; a later chapter devoted to Zorn's lemma states it, and the companion volume on set theory proves it from the axiom. This chapter does not prove comparability, and nothing in it needs it.
:::

## Intervals of real numbers

The theorem's first use is the question of the opening frame.

::: {#exm-closed-open-interval}
[The closed and the open unit interval]

Show that \( \card{[0, 1]} = \card{(0, 1)} \): first with @thm-schroder-bernstein, then by writing down a bijection.
:::

::: {.solution}
*With the theorem.* The inclusion \( (0, 1) \to [0, 1] \) is an injection. In the other direction let \( u(x) \coloneqq x/2 + 1/4 \) for \( x \in [0, 1] \). If \( 0 \le x \le 1 \), then \( 1/4 \le u(x) \le 3/4 \), so \( u(x) \in (0, 1) \), and \( u \) is a function \( [0, 1] \to (0, 1) \). It is injective: \( x/2 + 1/4 = y/2 + 1/4 \) gives \( x = y \). By @thm-schroder-bernstein, \( \card{[0, 1]} = \card{(0, 1)} \).

*A bijection.* The two extra points \( 0 \) and \( 1 \) are absorbed by a Hilbert's hotel (@exm-hilbert-hotel) run on the points \( 1, \frac12, \frac13, \dots \). Define \( \varphi \colon [0, 1] \to (0, 1) \) by
\[
\varphi(x) \coloneqq
\begin{cases}
\frac12 & \text{if } x = 0, \\
\frac{1}{n + 2} & \text{if } x = \frac1n \text{ for some } n \in \nZ_{>0}, \\
x & \text{otherwise.}
\end{cases}
\]
The cases do not overlap, since \( \frac1n \ne 0 \), and in the second case \( n = 1/x \) is determined by \( x \); so \( \varphi \) is a function, with values in \( (0, 1) \) because \( 0 < \frac{1}{n + 2} \le \frac13 \). Let \( H \coloneqq \{0\} \cup \{ \frac1n : n \in \nZ_{>0} \} = \{0, 1, \frac12, \frac13, \dots\} \) and \( H' \coloneqq \{ \frac1m : m \in \nZ_{>0}, \ m \ge 2 \} = \{\frac12, \frac13, \frac14, \dots\} \). Then \( \varphi \) maps \( H \) onto \( H' \): \( 0 \mapsto \frac12 \), and \( \frac1n \mapsto \frac{1}{n + 2} \) runs through \( \frac13, \frac14, \dots \). It is injective on \( H \), since \( \frac{1}{n + 2} = \frac{1}{n' + 2} \) forces \( n = n' \), and \( \frac{1}{n + 2} \le \frac13 < \frac12 \). Off \( H \) it is the identity of \( [0, 1] \setminus H = (0, 1) \setminus H' \). Since
\[
[0, 1] = H \cup \bigl([0, 1] \setminus H\bigr), \qquad (0, 1) = H' \cup \bigl((0, 1) \setminus H'\bigr),
\]
both unions disjoint, \( \varphi \) is a bijection, and \( \card{[0, 1]} = \card{(0, 1)} \). For instance \( \varphi(1) = \frac13 \), \( \varphi(\frac12) = \frac14 \), \( \varphi(\frac34) = \frac34 \).

The first route took two lines and the second took a paragraph. That is the point of the theorem: we never had to find \( \varphi \).
:::

The second interval computation turns an unbounded set into a bounded one.

::: {#exm-reals-open-interval}
[The real line and its intervals]

Show that \( x \mapsto x/(1 + \abs{x}) \) is a bijection \( \nR \to (-1, 1) \). Deduce that every open interval \( (c, d) \) with \( c < d \) is equinumerous with \( \nR \), and then that every interval with more than one point is.
:::

::: {.solution}
*The bijection.* Let \( s(x) \coloneqq x/(1 + \abs{x}) \) for \( x \in \nR \); the denominator is at least \( 1 \), so \( s(x) \) is defined, and \( \abs{s(x)} = \abs{x}/(1 + \abs{x}) < 1 \), so \( s(x) \in (-1, 1) \). For \( y \in (-1, 1) \) let \( t(y) \coloneqq y/(1 - \abs{y}) \); here \( 1 - \abs{y} > 0 \). We check that \( t \) is a two-sided inverse. For \( x \in \nR \), \( \abs{s(x)} = \abs{x}/(1 + \abs{x}) \), so
\[
1 - \abs{s(x)} = \frac{1}{1 + \abs{x}} , \qquad t(s(x)) = \frac{x}{1 + \abs{x}} \cdot (1 + \abs{x}) = x .
\]
For \( y \in (-1, 1) \), \( \abs{t(y)} = \abs{y}/(1 - \abs{y}) \), so
\[
1 + \abs{t(y)} = \frac{1}{1 - \abs{y}} , \qquad s(t(y)) = \frac{y}{1 - \abs{y}} \cdot (1 - \abs{y}) = y .
\]
By @thm-bijection-iff-inverse, \( s \) is a bijection \( \nR \to (-1, 1) \). For example \( s(1) = \frac12 \) and \( s(-3) = -\frac34 \).

*Open intervals.* The map \( y \mapsto (y + 1)/2 \) is a bijection \( (-1, 1) \to (0, 1) \), with inverse \( u \mapsto 2u - 1 \). For \( c < d \), the map \( u \mapsto c + (d - c)u \) is a bijection \( (0, 1) \to (c, d) \), with inverse \( v \mapsto (v - c)/(d - c) \), since \( d - c > 0 \). Composing the three bijections (@thm-composition-injective-surjective (c)) gives a bijection \( \nR \to (c, d) \), so \( \card{(c, d)} = \card{\nR} \).

*Every interval with more than one point.* Let \( I \) be an interval (bounded or not, with or without its endpoints) containing two points \( c < d \). An interval contains every number between two of its points, so \( (c, d) \subseteq I \subseteq \nR \). The inclusion is an injection \( (c, d) \to I \). In the other direction, let \( \beta \colon \nR \to (c, d) \) be the bijection just built; then \( \beta \) restricted to \( I \) is an injection \( I \to (c, d) \). By @thm-schroder-bernstein, \( \card{I} = \card{(c, d)} \), and \( \card{(c, d)} = \card{\nR} \), so \( \card{I} = \card{\nR} \) by @prp-equinumerous-properties. This covers \( [0, 1] \), \( [0, 1) \), \( (0, \infty) \), \( [5, \infty) \) and \( \nR \) itself at once.
:::

In particular every interval with more than one point is uncountable: it is equinumerous with \( \nR \), which is uncountable by @thm-reals-uncountable-decimal, and a set equinumerous with a countable set is countable (compose a surjection from \( \nN \) with the bijection, @prp-countable-image).

::: {.warning}
Injections both ways do not make either injection a bijection. On \( \nN \), \( n \mapsto 2n \) is an injection \( \nN \to \nN \) in both directions, and it is not onto: \( 1 \) is never a value. @thm-schroder-bernstein builds a **new** map \( h \) out of \( f \) and \( g \); it says nothing about \( f \) or \( g \) themselves. In @exm-closed-open-interval, \( u(x) = x/2 + 1/4 \) misses \( \frac{9}{10} \in (0, 1) \), and the bijection is a different map.
:::

::: {.check}
Give an injection \( \nN \to \nN \times \nN \) and an injection \( \nN \times \nN \to \nN \). What does @thm-schroder-bernstein conclude?
:::

::: {.solution}
\( n \mapsto (n, 1) \) is injective, by the characteristic property of pairs (@def-ordered-pair). \( (m, n) \mapsto 2^m 3^n \) is injective, as shown in the proof of @thm-product-countable. So \( \card{\nN} = \card{\nN \times \nN} \), and \( \nN \times \nN \) is countably infinite (@def-countably-infinite). Section 8.2 showed only that \( \nN \times \nN \) is countable; the theorem gives a bijection with \( \nN \) directly, with no listing at all.
:::

## Exercises

### A. Check your understanding

::: {#exr-comparing-cardinalities-a1}
[A1]

These parts are about the proof of @thm-schroder-bernstein.

::: {.enumerate options="label=(\alph*)"}
1. In Step 4, Case 2, why is \( g(b) \notin C_0 \), and what would go wrong without it?
2. Run the construction for \( A = B = \nN \) and \( f(n) = g(n) = 2n \). Compute \( C_0 \), \( C_1 \) and \( C \), and the values \( h(0), h(1), h(2), h(3), h(4) \).
3. Where is the injectivity of \( f \) used?
4. Give the idea of the proof in two sentences.
:::
:::

::: {.solution}
(a) \( C_0 = A \setminus g(B) \) consists of the points that are not values of \( g \), and \( g(b) \) is a value of \( g \). Without it the index \( n \) with \( g(b) \in C_n \) could be \( 0 \), and then there would be no \( C_{n-1} \) to find a predecessor \( a \) in, so no \( a \in C \) with \( f(a) = b \).

(b) \( g(\nN) = 2\nN \), so \( C_0 = \nN \setminus 2\nN \) is the set of odd numbers. \( C_1 = g(f(C_0)) = \{ 4q : q \text{ odd} \} = \{4, 12, 20, \dots\} \). In general \( C_{n+1} = \{ 4c : c \in C_n \} \), so \( C_n = \{ 4^n q : q \text{ odd} \} \) by induction on \( n \), and \( C \) is the set of numbers \( 4^k q \) with \( k \in \nN \) and \( q \) odd. Now:

- \( 0 \notin C \), since \( 4^k q \ne 0 \) for odd \( q \) (\( 4^k > 0 \) and \( q \ge 1 \)). So \( h(0) \) is the \( b \) with \( 2b = 0 \): \( h(0) = 0 \), a fixed point.
- \( 1 \in C_0 \), so \( h(1) = f(1) = 2 \).
- \( 2 \notin C \): for \( k = 0 \), \( 2 \) is not odd; for \( k \ge 1 \), \( 4^k q \ge 4 > 2 \). So \( h(2) \) is the \( b \) with \( 2b = 2 \): \( h(2) = 1 \).
- \( 3 \in C_0 \), so \( h(3) = 6 \).
- \( 4 = 4^1 \cdot 1 \in C_1 \), so \( h(4) = f(4) = 8 \).

(c) In Step 3, Case 1: from \( f(a) = f(a') \) with \( a, a' \in C \) it concludes \( a = a' \).

(d) Points of \( A \) that \( g \) does not reach must be sent forward by \( f \), and so must everything reached from them by repeating \( g \circ f \); this is the set \( C \). Every other point of \( A \) is a value of \( g \) and is sent back to its unique preimage, and the two halves fit together into a bijection.
:::

### B. Practice

::: {#exr-comparing-cardinalities-b1}
[B1: Injections both ways]

Prove each of the following by giving an injection in each direction and applying @thm-schroder-bernstein.

::: {.enumerate options="label=(\alph*)"}
1. \( \card{[0, 1]} = \card{\nR} \).
2. \( \card{\nN} = \card{\nN \times \nZ} \).
3. \( \card{(0, 1) \cup (2, 3)} = \card{(0, 1)} \).
:::
:::

::: {.solution}
(a) The inclusion \( [0, 1] \to \nR \) is injective. In the other direction, \( x \mapsto \bigl(x/(1 + \abs{x}) + 1\bigr)/2 \) is a bijection \( \nR \to (0, 1) \) by @exm-reals-open-interval, so it is an injection \( \nR \to [0, 1] \), as \( (0, 1) \subseteq [0, 1] \).

(b) \( n \mapsto (n, 0) \) is an injection \( \nN \to \nN \times \nZ \), by the characteristic property of pairs (@def-ordered-pair). In the other direction, let \( j \colon \nZ \to \nN \) be \( j(k) \coloneqq 2k \) for \( k \ge 0 \) and \( j(k) \coloneqq -2k - 1 \) for \( k < 0 \). Its values are in \( \nN \), even for \( k \ge 0 \) and odd for \( k < 0 \); since no natural number is both even and odd (@thm-division-algorithm, uniqueness), \( j(k) = j(k') \) forces \( k \) and \( k' \) to have the same sign, and then \( k = k' \). So \( j \) is injective, and so is \( (m, k) \mapsto (m, j(k)) \). Following it by the injection \( (m, n) \mapsto 2^m 3^n \) from the proof of @thm-product-countable gives an injection \( \nN \times \nZ \to \nN \) (@thm-composition-injective-surjective (a)).

(c) The inclusion \( (0, 1) \to (0, 1) \cup (2, 3) \) is injective. The map \( x \mapsto x/4 \) is injective and sends \( (0, 1) \cup (2, 3) \) into \( (0, \frac14) \cup (\frac12, \frac34) \subseteq (0, 1) \).

Hence, by @thm-schroder-bernstein, the three equalities hold.
:::

::: {#exr-comparing-cardinalities-b2}
[B2: A proper subset of the same size]

Give an example of sets \( A \subsetneq B \subseteq \nR \) with \( \card{A} = \card{B} \), such that \( A \) is uncountable and \( B \setminus A \) is uncountable. Check each property, and list the properties any answer must have.
:::

::: {.solution}
*An answer must have:* (1) \( A \subseteq B \subseteq \nR \); (2) \( A \ne B \); (3) a bijection \( A \to B \), or injections both ways; (4) \( A \) uncountable; (5) \( B \setminus A \) uncountable. (Then \( B \) is uncountable too, since it contains \( A \), by @prp-countable-subset.)

*Example:* \( A = (0, 1) \), \( B = (0, 3) \). (1) and (2): \( (0, 1) \subseteq (0, 3) \) and \( 2 \in B \setminus A \). (3): \( x \mapsto 3x \) is a bijection \( (0, 1) \to (0, 3) \), with inverse \( y \mapsto y/3 \). (4) and (5): \( A \) and \( B \setminus A = [1, 3) \) are intervals with more than one point, hence equinumerous with \( \nR \) by @exm-reals-open-interval, hence uncountable, as shown after it.

Another correct answer: \( A = (0, 1) \), \( B = \nR \), with \( B \setminus A \supseteq (1, 2) \) uncountable. Any answer can be checked against (1)–(5).
:::

::: {#exr-comparing-cardinalities-b3}
[B3: Interleaving two sequences]

Prove that \( \card{\{0, 1\}^{\nN} \times \{0, 1\}^{\nN}} = \card{\{0, 1\}^{\nN}} \) by an explicit bijection.

*Hint: put one sequence in the even places and the other in the odd places.*
:::

::: {.solution}
Every \( m \in \nN \) is \( 2n \) or \( 2n + 1 \) for exactly one \( n \in \nN \), and not both (@thm-division-algorithm with divisor \( 2 \), the quotient in \( \nN \), as in the proof of @prp-union-two-countable). So for \( a, b \in \{0, 1\}^{\nN} \) we may define \( c = \Phi(a, b) \in \{0, 1\}^{\nN} \) by
\[
c(2n) \coloneqq a(n), \qquad c(2n + 1) \coloneqq b(n) \qquad (n \in \nN).
\]
Define \( \Psi \colon \{0, 1\}^{\nN} \to \{0, 1\}^{\nN} \times \{0, 1\}^{\nN} \) by \( \Psi(c) \coloneqq (a, b) \) with \( a(n) \coloneqq c(2n) \) and \( b(n) \coloneqq c(2n + 1) \). Then \( \Psi(\Phi(a, b)) = (a, b) \): its coordinates \( n \mapsto c(2n) = a(n) \) and \( n \mapsto c(2n + 1) = b(n) \) are \( a \) and \( b \) by @prp-function-equality, so the pairs are equal (@def-ordered-pair). And \( \Phi(\Psi(c)) \) agrees with \( c \) at every even place \( 2n \) and every odd place \( 2n + 1 \), which are all the places, so \( \Phi(\Psi(c)) = c \) (@prp-function-equality). By @thm-bijection-iff-inverse, \( \Phi \) is a bijection.
:::

### C. Going deeper

::: {#exr-comparing-cardinalities-c1}
[C1: The real line and the subsets of \( \nN \)]

Prove that \( \card{\nR} = \card{\powerset{\nN}} \), using the decimal facts (D1)–(D3) of Section 8.4.

::: {.enumerate options="label=(\alph*)"}
1. For \( x \in [0, 1) \) let \( d_1 d_2 \ldots \) be its decimal expansion that does not end in all \( 9 \)s, and let \( E(x) \coloneqq \{ 10k + d_k : k \in \nZ_{>0} \} \). Show that \( E \) is a well-defined injection \( [0, 1) \to \powerset{\nN} \).
2. For \( S \subseteq \nN \) let \( y_S \) be the number with decimal expansion \( 0.e_1 e_2 e_3 \ldots \), where \( e_{k+1} \coloneqq 1 \) if \( k \in S \) and \( e_{k+1} \coloneqq 2 \) if \( k \notin S \), for \( k \in \nN \). Show that \( S \mapsto y_S \) is a well-defined injection \( \powerset{\nN} \to [0, 1) \).
3. Conclude.
:::
:::

::: {.solution}
[Hint 1]

The tools are the decimal facts (D1)–(D3), and @thm-division-algorithm with divisor \( 10 \) for reading digits back out of \( E(x) \).
:::

::: {.solution}
[Hint 2]

Begin (a) with: "By (D1), \( x \) has an expansion that does not end in all \( 9 \)s, and by (D3) it has only one."
:::

::: {.solution}
(a) *Well defined.* By (D1), \( x \) has an expansion not ending in all \( 9 \)s. It has only one: if two different expansions of \( x \) both failed to end in all \( 9 \)s, (D3) would make one of them end in all \( 9 \)s. So \( d_1 d_2 \ldots \) is determined by \( x \), and \( E(x) \subseteq \nN \) because \( 10k + d_k \in \nN \).

*Injective.* By @thm-division-algorithm with divisor \( 10 \), the number \( 10j + d_j \), with \( 0 \le d_j \le 9 \), has quotient \( j \) and remainder \( d_j \), and these are unique. So for each \( k \ge 1 \), the only element of \( E(x) \) with quotient \( k \) is \( 10k + d_k \), and \( E(x) \) determines every digit \( d_k \). If \( E(x) = E(x') \), then \( x \) and \( x' \) have the same expansion \( d_1 d_2 \ldots \), and by the uniqueness half of (D2) a digit sequence is an expansion of exactly one number; so \( x = x' \).

(b) *Well defined.* By (D2), the digit sequence \( e_1 e_2 \ldots \) is an expansion of exactly one \( y_S \in [0, 1] \). With \( t_1 = e_1/10 \) as in @def-decimal-expansion, \( y_S \le t_1 + \frac{1}{10} \le \frac{2}{10} + \frac{1}{10} = \frac{3}{10} \), so \( y_S \in [0, 1) \).

*Injective.* Let \( S \ne S' \), say \( k \in S \setminus S' \) or \( k \in S' \setminus S \). Then the two digit sequences differ at place \( k + 1 \). Neither contains a \( 0 \) or a \( 9 \), so neither ends in all \( 9 \)s or in all \( 0 \)s. If \( y_S = y_{S'} \), the number would have two different expansions, and by (D3) one would end in all \( 9 \)s, which is false. So \( y_S \ne y_{S'} \). The index shift \( e_{k+1} \) is there so that whether \( 0 \in S \) is recorded too, in the first digit.

(c) By (a), (b) and @thm-schroder-bernstein, \( \card{[0, 1)} = \card{\powerset{\nN}} \). By @exm-reals-open-interval, \( [0, 1) \), an interval with more than one point, has \( \card{[0, 1)} = \card{\nR} \). By @prp-equinumerous-properties, \( \card{\nR} = \card{\powerset{\nN}} \).

**Marking scheme.** (10 points)
- 2: shows the expansion in (a) is unique, citing (D1) and (D3), so \( E \) is a function.
- 2: shows \( E \) is injective: the set determines each digit, and one digit sequence names one number (D2).
- 2: shows \( y_S \) exists, is unique and lies in \( [0, 1) \).
- 2: shows \( S \mapsto y_S \) is injective, using that the digits avoid \( 0 \) and \( 9 \) and (D3).
- 2: applies @thm-schroder-bernstein and passes from \( [0, 1) \) to \( \nR \) with a cited bijection or injections both ways.
Fatal errors (0 for the step): treating "the expansion of \( x \)" as unique without (D1) and (D3); concluding \( y_S \ne y_{S'} \) from different digit sequences without ruling out the \( 0.4999\ldots = 0.5 \) case.
:::

::: {#exr-comparing-cardinalities-c2}
[C2: Find the error]

Here is a proof that \( \card{[0, 1]} = \card{(0, 1)} \).

> *Proof.* (1) Let \( u \colon [0, 1] \to (0, 1) \), \( u(x) \coloneqq x/2 + 1/4 \). For \( 0 \le x \le 1 \) we have \( 1/4 \le u(x) \le 3/4 \), so \( u \) does map into \( (0, 1) \). (2) If \( u(x) = u(y) \), then \( x/2 = y/2 \), so \( x = y \); hence \( u \) is injective. (3) The inclusion \( \iota \colon (0, 1) \to [0, 1] \) is injective. (4) So there are injections in both directions between \( [0, 1] \) and \( (0, 1) \). (5) Therefore \( u \) is a bijection, and \( \card{[0, 1]} = \card{(0, 1)} \).

Is the conclusion true? Does the argument prove it? If not, name the line that fails, say why, and give a counterexample to the step it takes.
:::

::: {.solution}
*The conclusion is true*: @exm-closed-open-interval proves it twice.

*The argument does not prove it.* Lines (1)–(4) are correct. Line (5) fails: it infers that a particular injection is a bijection from the existence of injections both ways. The step cites a general "fact", that injections both ways make a given injection a bijection. That fact is neither proved nor a school fact, and it is false, so the line cites nothing: entry (N9) of @exm-not-allowed-catalogue. And \( u \) is in fact not onto: \( \frac{9}{10} \in (0, 1) \) is not a value, since every value lies in \( [\frac14, \frac34] \).

*Counterexample to the step.* Take \( A = B = \nN \) and \( f = g = (n \mapsto 2n) \). These are injections both ways, and the step would conclude that \( n \mapsto 2n \) is a bijection \( \nN \to \nN \); but \( 1 \) is not a value.

*Repair.* Replace line (5) by: "By @thm-schroder-bernstein, \( \card{[0, 1]} = \card{(0, 1)} \)." The theorem produces a bijection, but a different one, built from both \( u \) and \( \iota \).
:::

<!-- dependency ledger
def-card-le (example): finite case, the inclusion {1..m} into {1..n} for m <= n | {1, ..., n} notation (NOTATION; Ch 7 Section 7.1); order of N
def-card-le (example): {x1} = {x2} gives x1 = x2 | def-set-equality (Ch 6 Section 6.1), used silently
prp-card-le-preorder (claim): (after it) 2N is not N, n -> 2n injective | arithmetic (1 is not even: thm-division-algorithm uniqueness)
thm-schroder-bernstein (proof): case split a in C or a not in C | excluded middle (Ch 5 Section 5.7, prose pointer; classical logic of Ch 2)
thm-schroder-bernstein (proof): g(f(S)) is a subset of A for S subset of A, so (n, S) -> g(f(S)) is a function N x P(A) -> P(A) | def-image (cited), def-power-set (Ch 6 Section 6.2), used silently
thm-schroder-bernstein (claim): (remark) any two sets are comparable, via Zorn's lemma; Zorn stated in F2.4, proved from choice in ST.4 | F2.4, ST.4 (prose pointers; nothing depends on them)
exm-closed-open-interval (solution): 1/4 <= x/2 + 1/4 <= 3/4; 1/n distinct for distinct n; 0 < 1/(n+2) <= 1/3 < 1/2 | R arithmetic and order, school fact; verify/ch08/exm-closed-open-interval.py
exm-closed-open-interval (solution): [0,1] \ H = (0,1) \ H' | inline (0 and 1 = 1/1 lie in H; H \ {0, 1} = H')
exm-reals-open-interval (solution): algebra of |x|/(1 + |x|) and its inverse; |y/(1-|y|)| = |y|/(1-|y|) | R arithmetic with absolute values, school fact (Ch 6 Section 6.5 B3 does the same computation, not cited); verify/ch08/exm-reals-open-interval.py
exm-reals-open-interval (solution): an interval contains every number between two of its points | school fact about intervals (each kind by its defining inequalities)
exm-reals-open-interval (claim): (after it) a set equinumerous with a countable set is countable | inline (prp-countable-image with the bijection; empty case trivial)
exr-comparing-cardinalities-a1 (solution): C_n = {4^n q : q odd} by induction; 4^k q != 0 and >= 4 for k >= 1 | inline induction; prp-power-laws (e); verify/ch08/exr-comparing-cardinalities-a1.py
exr-comparing-cardinalities-b1 (solution): j(k) = 2k / -2k-1 lands in N and is injective | thm-division-algorithm (cited), prp-integers-closed (b), used silently
exr-comparing-cardinalities-b1 (solution): x/4 maps (0,1) u (2,3) into (0,1/4) u (1/2,3/4) | R arithmetic, school fact
exr-comparing-cardinalities-b2 (solution): x -> 3x bijection (0,1) -> (0,3) | R arithmetic, school fact
exr-comparing-cardinalities-c1 (solution): uses (D1), (D2), (D3) | school facts (D1)-(D3), stated in Section 8.4 (def-decimal-expansion)
exr-comparing-cardinalities-c1 (solution): y_S <= t_1 + 1/10 <= 3/10 | def-decimal-expansion (cited) with n = 1; verify/ch08/exr-comparing-cardinalities-c1.py
exr-comparing-cardinalities-c2 (solution): 9/10 not in [1/4, 3/4] | R order, school fact
-->
