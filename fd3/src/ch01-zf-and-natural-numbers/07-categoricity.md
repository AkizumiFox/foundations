# All Peano Systems Are Alike

Section 9.4 proved that \( (\omega, 0, \mathrm{S}) \) is a Peano system (@thm-omega-peano, @def-peano-system), and Sections 9.5 and 9.6 built \( + \), \( \cdot \) and \( < \) on it. One question is left. Chapter 7 worked with a set \( \nN \) inside the familiar real numbers, and this chapter has built a quite different set \( \omega \) out of \( \emptyset \). In what sense are they the same? This section answers: any two Peano systems are copies of each other, by exactly one matching, which also carries \( + \), \( \cdot \) and \( < \) across. Then it says what the later chapters may take from Chapters 3 and 7 when they write \( \nN \) for \( \omega \).

## Two Peano systems, and what "alike" should mean

Here is a second Peano system, inside \( \omega \) itself: \( (\omega \setminus \{0\}, 1, \mathrm{S}) \), the natural numbers from \( 1 \) on, with the same successor. Exercise C1 of Section 9.4 asked you to check it; the check is three lines.

- \( \mathrm{S} \) maps \( \omega \setminus \{0\} \) into itself, since \( \mathrm{S}(n) \ne 0 \) by @thm-omega-peano (P3).
- (P3) holds with \( e = 1 \): if \( \mathrm{S}(n) = 1 = \mathrm{S}(0) \), then \( n = 0 \) by (P4) of @thm-omega-peano, and \( 0 \notin \omega \setminus \{0\} \). (P4) holds because \( \mathrm{S} \) is injective on all of \( \omega \).
- (P5) holds: if \( A \subseteq \omega \setminus \{0\} \) contains \( 1 \) and is closed under \( \mathrm{S} \), then \( \{0\} \cup A \) contains \( 0 \) and is closed under \( \mathrm{S} \) (as \( \mathrm{S}(0) = 1 \in A \)), so it is \( \omega \) by @thm-omega-induction (a), and \( A = \omega \setminus \{0\} \).

Its starting point is \( 1 \), not \( \emptyset \), yet it counts the same way: \( n \mapsto \mathrm{S}(n) \) pairs \( 0, 1, 2, \dots \) with \( 1, 2, 3, \dots \), sends start to start, and turns one step into one step.

That is the right meaning of "alike". For Peano systems \( (M, e, s) \) and \( (M', e', s') \), call a bijection \( \psi \colon M \to M' \) an **isomorphism** if
\[
\psi(e) = e' \quad \text{and} \quad \psi\bigl(s(x)\bigr) = s'\bigl(\psi(x)\bigr) \ \text{ for every } x \in M .
\]
In words: \( \psi \) renames the elements, sends the starting point to the starting point, and it does not matter whether we first step and then rename, or first rename and then step.

::: {.warning}
Being equinumerous is not enough. The bijection \( \tau \colon \omega \to \omega \) that exchanges \( 1 \) and \( 2 \) and fixes every other number satisfies \( \tau(0) = 0 \), but \( \tau(\mathrm{S}(0)) = \tau(1) = 2 \), while \( \mathrm{S}(\tau(0)) = \mathrm{S}(0) = 1 \). So \( \tau \) is a bijection from a Peano system to itself that is **not** an isomorphism: it does not respect the successor. Categoricity, below, is a statement about isomorphisms, and it says much more than "same size".
:::

## The categoricity theorem

The theorem says that every Peano system is an isomorphic copy of \( \omega \), and so any two are copies of each other, in only one way.

::: {#thm-peano-categoricity}
[Categoricity of the Peano Axioms]

Let \( (M, e, s) \) be a Peano system.

::: {.enumerate options="label=(\alph*)"}
1. There is **exactly one** function \( \varphi \colon \omega \to M \) with \( \varphi(0) = e \) and \( \varphi(\mathrm{S}(n)) = s(\varphi(n)) \) for every \( n \in \omega \).
2. This \( \varphi \) is a bijection.
3. For any two Peano systems \( (M, e, s) \) and \( (M', e', s') \) there is **exactly one** bijection \( \psi \colon M \to M' \) with \( \psi(e) = e' \) and \( \psi(s(x)) = s'(\psi(x)) \) for every \( x \in M \).
:::
:::

*Try it first (ten minutes): given a Peano system \( (M, e, s) \), which map \( \omega \to M \) would you build, with which theorem, and how would you show that it is onto?*

::: {.idea}
The attempt meets three obstacles, one for each part.

① **Which map.** It is forced: \( 0 \) must go to \( e \), then \( 1 \) to \( s(e) \), then \( 2 \) to \( s(s(e)) \), and so on. But "and so on" is not a definition. @thm-omega-recursion turns it into one, with \( X = M \), starting value \( e \) and step \( x \mapsto s(x) \); it gives existence and uniqueness at once.

② **Onto.** We know nothing about the elements of \( M \) one by one, so we cannot show "each \( x \in M \) is \( s(\dots s(e)) \)" directly. What we have is (P5) for \( M \), which speaks about subsets. So look at the image of \( \varphi \): it contains \( e \) and is closed under \( s \), and (P5) does the rest.

③ **One-to-one.** Prove "\( \varphi(m) = \varphi(n) \Rightarrow m = n \)" by induction on \( n \). If \( m \) is fixed before the induction, the hypothesis at \( n \) speaks about that one \( m \), while the step needs it at the predecessor of \( m \). So "for every \( m \)" goes inside the property. The base and the step then use (P3) and (P4) for \( M \): a successor is never \( e \), and equal successors have equal predecessors.

For (c), compose: go back from \( M \) to \( \omega \) along \( \varphi^{-1} \), then forward to \( M' \) along \( \varphi' \).

*Before reading on: which axiom of \( M \) gives surjectivity, and which give injectivity?*
:::

::: {.proof}
*(a)* Let \( g \colon \omega \times M \to M \) be \( g(n, x) \coloneqq s(x) \); its graph \( \{ ((n, x), y) \in (\omega \times M) \times M : y = s(x) \} \) is a set by (Z6) inside the product of @prp-cartesian-product-exists, and each \( (n, x) \) has exactly one partner \( s(x) \) because \( s \) is a function. By @thm-omega-recursion with \( X = M \) and \( a = e \), there is exactly one \( \varphi \colon \omega \to M \) with \( \varphi(0) = e \) and \( \varphi(\mathrm{S}(n)) = g(n, \varphi(n)) = s(\varphi(n)) \) for every \( n \in \omega \).

*(b), onto.* Let \( B \coloneqq \varphi(\omega) \subseteq M \), the image of \( \omega \) under \( \varphi \) (@def-image). Then \( e = \varphi(0) \in B \). If \( x \in B \), say \( x = \varphi(n) \) with \( n \in \omega \), then \( \mathrm{S}(n) \in \omega \) by @thm-omega-peano (P2), and \( s(x) = s(\varphi(n)) = \varphi(\mathrm{S}(n)) \in B \). So \( B \) contains \( e \) and is closed under \( s \), and (P5) for \( M \) gives \( B = M \). Hence \( \varphi \) is surjective (@def-surjective).

*(b), one-to-one.* Let \( Q(n) \) be "for every \( m \in \omega \), if \( \varphi(m) = \varphi(n) \), then \( m = n \)". We prove \( Q(n) \) for every \( n \in \omega \) by @thm-omega-induction (b).

*Base case.* Let \( m \in \omega \) with \( \varphi(m) = \varphi(0) = e \). Suppose \( m \ne 0 \). Then \( m = \mathrm{S}(k) \) for some \( k \in \omega \) (@lem-omega-transitive (d)), and \( \varphi(m) = s(\varphi(k)) \ne e \) by (P3) for \( M \), a contradiction. So \( m = 0 \).

*Inductive step.* Let \( n \in \omega \) with \( Q(n) \), and let \( m \in \omega \) with \( \varphi(m) = \varphi(\mathrm{S}(n)) = s(\varphi(n)) \). If \( m = 0 \), then \( s(\varphi(n)) = \varphi(0) = e \), against (P3) for \( M \). So \( m \ne 0 \), and \( m = \mathrm{S}(k) \) for some \( k \in \omega \) (@lem-omega-transitive (d)). Then \( s(\varphi(k)) = \varphi(m) = s(\varphi(n)) \), so \( \varphi(k) = \varphi(n) \) by (P4) for \( M \), and \( k = n \) by \( Q(n) \), applied to \( k \) in the place of \( m \). Hence \( m = \mathrm{S}(k) = \mathrm{S}(n) \), which is \( Q(\mathrm{S}(n)) \).

So \( \varphi \) is injective (@def-injective), and with the first half it is a bijection (@def-bijective).

*(c)* Let \( \varphi \colon \omega \to M \) and \( \varphi' \colon \omega \to M' \) be the maps of (a) for the two systems; both are bijections by (b). By @thm-bijection-iff-inverse, \( \varphi \) has an inverse \( \varphi^{-1} \colon M \to \omega \), and we set \( \psi \coloneqq \varphi' \circ \varphi^{-1} \) (@def-composition). The two equations \( \varphi \circ \varphi^{-1} = \id_M \) and \( \varphi^{-1} \circ \varphi = \id_\omega \) of @def-inverse-function also say that \( \varphi \) is an inverse of \( \varphi^{-1} \), so \( \varphi^{-1} \) is a bijection by @thm-bijection-iff-inverse. Hence \( \psi \) is a bijection as a composite of bijections (@thm-composition-injective-surjective (c)).

*\( \psi \) has the two properties.* Since \( \varphi(0) = e \), we have \( \varphi^{-1}(e) = 0 \), so \( \psi(e) = \varphi'(0) = e' \). Let \( x \in M \) and \( n \coloneqq \varphi^{-1}(x) \), so \( x = \varphi(n) \). Then \( s(x) = \varphi(\mathrm{S}(n)) \), so \( \varphi^{-1}(s(x)) = \mathrm{S}(n) \), and
\[
\psi\bigl(s(x)\bigr) = \varphi'\bigl(\mathrm{S}(n)\bigr) = s'\bigl(\varphi'(n)\bigr) = s'\bigl(\psi(x)\bigr) .
\]

*Uniqueness.* Let \( \chi \colon M \to M' \) be **any** function with \( \chi(e) = e' \) and \( \chi(s(x)) = s'(\chi(x)) \) for every \( x \in M \). Then \( \chi \circ \varphi \colon \omega \to M' \) satisfies \( (\chi \circ \varphi)(0) = \chi(e) = e' \) and
\[
(\chi \circ \varphi)\bigl(\mathrm{S}(n)\bigr) = \chi\bigl(s(\varphi(n))\bigr) = s'\bigl((\chi \circ \varphi)(n)\bigr)
\]
for every \( n \in \omega \). By the uniqueness in (a), for the system \( M' \), \( \chi \circ \varphi = \varphi' \). So for every \( x \in M \), \( \chi(x) = \chi(\varphi(\varphi^{-1}(x))) = \varphi'(\varphi^{-1}(x)) = \psi(x) \), and \( \chi = \psi \) by @prp-function-equality. This proves the theorem.
:::

The proof is the third named move of the chapter, **build by recursion, compare by induction**: the map out of \( \omega \) came from the recursion theorem, and every fact about it (onto, one-to-one) came from an induction or from (P5). The uniqueness in (c) is stronger than stated: no function at all, bijective or not, other than \( \psi \) respects \( e \) and \( s \).

Each axiom of \( M \) has a job in (b), and the structures of @exm-peano-axioms-independent show each job failing. These are not Peano systems, so the theorem does not apply to them. But for each of them @thm-omega-recursion, with \( X = M \), \( a = e \) and \( g(n, x) = s(x) \) exactly as in the proof of (a), still gives exactly one \( \varphi \colon \omega \to M \) with \( \varphi(0) = e \) and \( \varphi(\mathrm{S}(n)) = s(\varphi(n)) \).

- In structure (i), \( M = \{0\} \) with \( s(0) = 0 \), which fails (P3) only, \( \varphi \) is the constant map \( 0 \), not injective: \( \varphi(1) = s(\varphi(0)) = 0 = \varphi(0) \).
- In structure (ii), \( M = \{0, 1\} \) with \( s(0) = s(1) = 1 \), which fails (P4) only, \( \varphi(1) = \varphi(2) = 1 \), again not injective.
- In the natural numbers beside a two-sided chain, structure (iii), which fails (P5) only, \( \varphi \) is \( n \mapsto (n, 0) \) (remark below), which is injective by @thm-kuratowski-pair, but not onto, as the remark below shows.

::: {.remark}
**What induction buys.** In structure (iii) of @exm-peano-axioms-independent, the natural numbers beside a two-sided chain (a copy of \( \omega \) next to a copy of \( \nZ \)), \( M = \omega \times 3 \) with \( e = (0, 0) \), the map \( \varphi \) still exists, by @thm-omega-recursion as above. It is \( \varphi(n) = (n, 0) \), by the uniqueness half of @thm-omega-recursion: \( n \mapsto (n, 0) \) sends \( 0 \) to \( e \) and satisfies the recursion, as \( s(n, 0) = (\mathrm{S}(n), 0) \). Its image \( \omega \times \{0\} \) misses \( (0, 1) \), so \( \varphi \) is not onto. Exercise C2 asks the reverse question: is there a map \( M \to \omega \) that respects the two structures?
:::

::: {.check}
For the Peano system \( (\omega \setminus \{0\}, 1, \mathrm{S}) \) of the first subsection, what is the map \( \varphi \) of @thm-peano-categoricity (a)? What is \( \varphi(3) \)?
:::

::: {.solution}
\( \varphi(n) = \mathrm{S}(n) = n + 1 \). Indeed \( n \mapsto \mathrm{S}(n) \) maps \( \omega \) into \( \omega \setminus \{0\} \) by (P3), sends \( 0 \) to \( \mathrm{S}(0) = 1 \), and satisfies \( \mathrm{S}(\mathrm{S}(n)) = \mathrm{S}(\varphi(n)) \); by the uniqueness in (a), it is \( \varphi \). So \( \varphi(3) = \mathrm{S}(3) = 4 \). Step by step: \( \varphi(0) = 1 \), \( \varphi(1) = \mathrm{S}(1) = 2 \), \( \varphi(2) = 3 \), \( \varphi(3) = 4 \).
:::

## Arithmetic and order travel along the isomorphism

An isomorphism matches \( e \) and \( s \). Addition and multiplication on \( \omega \) were built from \( 0 \) and \( \mathrm{S} \) alone, by recursion (@def-omega-arithmetic), and \( < \) can be described by \( + \) (@prp-omega-order-arithmetic (a)). So we expect the matching to carry them across, as long as the other system has operations defined by the same equations.

::: {#prp-isomorphism-preserves-arithmetic}
[Isomorphisms Preserve Arithmetic and Order]

Let \( (M, e, s) \) be a Peano system, and let \( \oplus, \otimes \colon M \times M \to M \) be functions such that, for all \( x, y \in M \),
\[
\begin{aligned}
x \oplus e &= x, & x \oplus s(y) &= s(x \oplus y), \\
x \otimes e &= e, & x \otimes s(y) &= (x \otimes y) \oplus x .
\end{aligned}
\]
Let \( \varphi \colon \omega \to M \) be the bijection of @thm-peano-categoricity. Then for all \( m, n \in \omega \):

::: {.enumerate options="label=(\alph*)"}
1. \( \varphi(m + n) = \varphi(m) \oplus \varphi(n) \);
2. \( \varphi(m n) = \varphi(m) \otimes \varphi(n) \);
3. \( m < n \) if and only if \( \varphi(n) = \varphi(m) \oplus z \) for some \( z \in M \) with \( z \ne e \).
:::
:::

::: {.idea}
For (a) and (b), fix \( m \) and induct on \( n \), the variable the recursions run on: each side obeys the same two equations, the base from \( 0 \) and the step from \( \mathrm{S} \), and \( \varphi \) turns one set of equations into the other. For (c), translate @prp-omega-order-arithmetic (a), "\( m < n \) iff \( n = m + j \) with \( j \ne 0 \)", through (a), using that \( \varphi \) is a bijection with \( \varphi(0) = e \).
:::

::: {.proof}
*(a)* Fix \( m \in \omega \); we induct on \( n \) (@thm-omega-induction (b)). *Base case:* \( \varphi(m + 0) = \varphi(m) = \varphi(m) \oplus e = \varphi(m) \oplus \varphi(0) \), by @def-omega-arithmetic (a) and the first equation for \( \oplus \). *Step:* if \( \varphi(m + n) = \varphi(m) \oplus \varphi(n) \), then
\[
\begin{aligned}
\varphi\bigl(m + \mathrm{S}(n)\bigr) &= \varphi\bigl(\mathrm{S}(m + n)\bigr) = s\bigl(\varphi(m + n)\bigr) \\
&= s\bigl(\varphi(m) \oplus \varphi(n)\bigr) = \varphi(m) \oplus s\bigl(\varphi(n)\bigr) = \varphi(m) \oplus \varphi\bigl(\mathrm{S}(n)\bigr) ,
\end{aligned}
\]
by @def-omega-arithmetic (a), the equation of \( \varphi \), the hypothesis, the second equation for \( \oplus \), and the equation of \( \varphi \) again.

*(b)* Fix \( m \in \omega \) and induct on \( n \). *Base case:* \( \varphi(m \cdot 0) = \varphi(0) = e = \varphi(m) \otimes e = \varphi(m) \otimes \varphi(0) \), by @def-omega-arithmetic (b) and the first equation for \( \otimes \). *Step:* if \( \varphi(mn) = \varphi(m) \otimes \varphi(n) \), then
\[
\begin{aligned}
\varphi\bigl(m \cdot \mathrm{S}(n)\bigr) &= \varphi(mn + m) = \varphi(mn) \oplus \varphi(m) \\
&= \bigl(\varphi(m) \otimes \varphi(n)\bigr) \oplus \varphi(m) = \varphi(m) \otimes s\bigl(\varphi(n)\bigr) = \varphi(m) \otimes \varphi\bigl(\mathrm{S}(n)\bigr) ,
\end{aligned}
\]
by @def-omega-arithmetic (b), part (a) just proved, the hypothesis, the second equation for \( \otimes \), and the equation of \( \varphi \).

*(c)* By @prp-omega-order-arithmetic (a), \( m < n \) if and only if \( n = m + j \) for some \( j \in \omega \) with \( j \ne 0 \).

\( (\Rightarrow) \) Let \( n = m + j \) with \( j \ne 0 \). By (a), \( \varphi(n) = \varphi(m) \oplus \varphi(j) \). Put \( z \coloneqq \varphi(j) \). Since \( \varphi \) is injective (@thm-peano-categoricity (b)), \( j \ne 0 \) gives \( z \ne \varphi(0) = e \).

\( (\Leftarrow) \) Let \( z \in M \) with \( z \ne e \) and \( \varphi(n) = \varphi(m) \oplus z \). Since \( \varphi \) is onto (@thm-peano-categoricity (b)), \( z = \varphi(j) \) for some \( j \in \omega \), and \( j \ne 0 \) because \( \varphi(0) = e \ne z \). By (a), \( \varphi(n) = \varphi(m) \oplus \varphi(j) = \varphi(m + j) \), so \( n = m + j \) by injectivity. Hence \( m < n \). This proves the proposition.
:::

So once a Peano system carries an addition and a multiplication obeying the recursive equations, \( \varphi \) is an isomorphism for them too, and the order defined from \( \oplus \) as in (c) is carried along as well. Nothing about \( \oplus \) and \( \otimes \) was assumed beyond the four equations.

## Identifying the two sets of natural numbers

Now apply all this to the set \( \nN \) of Chapter 7. Two different things are true, and it matters which one the later chapters lean on. One is a statement about Chapter 7's \( \nN \), a subset of the familiar real numbers: it is a Peano system, so it is a copy of \( \omega \). The other is a statement about \( \omega \) alone: the principles Chapters 3 and 7 assumed or proved for \( \nN \) are theorems about \( \omega \), proved from the axioms (Z1)–(Z7).

::: {#cor-omega-identification}
[ω Is the Natural Numbers]

::: {.enumerate options="label=(\alph*)"}
1. **About Chapter 7's \( \nN \).** Let \( \nN \subseteq \nR \) be the set of natural numbers as Section 7.1 describes it, with (\( \nN \)0), (\( \nN \)S) and @ax-induction. With \( e \coloneqq 0 \) and \( s(n) \coloneqq n + 1 \), it is a Peano system. There is exactly one bijection \( \varphi \colon \omega \to \nN \) with \( \varphi(0) = 0 \) and \( \varphi(\mathrm{S}(n)) = \varphi(n) + 1 \) for every \( n \in \omega \). For all \( m, n \in \omega \) it satisfies
\[
\varphi(m + n) = \varphi(m) + \varphi(n), \qquad \varphi(mn) = \varphi(m)\varphi(n),
\]
and \( m < n \) if and only if \( \varphi(m) < \varphi(n) \); and it sends each numeral of \( \omega \) to the natural number of the same name.
2. **About \( \omega \), proved from (Z1)–(Z7).** The statements of @ax-induction and @thm-recursion, read with \( \nN \coloneqq \omega \) and \( n + 1 \coloneqq \mathrm{S}(n) \), are @thm-omega-induction (b) and @thm-omega-recursion. Induction started at a base \( b \in \omega \) (the form of @thm-induction with base \( n_0 = b \)) is @prp-omega-order-arithmetic (g).
3. Each clause of @lem-naturals-arithmetic holds on \( \omega \), with \( n - m \), for \( m \le n \), read as the unique \( j \in \omega \) with \( n = m + j \) of @prp-omega-order-arithmetic (a).
:::
:::

::: {.idea}
For (a), check (P3)–(P5) for Chapter 7's \( \nN \) with the tools of Section 7.1, and the equations of @prp-isomorphism-preserves-arithmetic with school arithmetic; then @thm-peano-categoricity and that proposition do the rest. Parts (b) and (c) are a matter of reading statements side by side and pointing to the label that proves each one on \( \omega \).

*Before reading on: which clause do the later chapters actually use, when they build \( \nZ \), \( \nQ \) and \( \nR \)?*
:::

::: {.proof}
*(a)* The map \( s \) sends \( \nN \) into \( \nN \) by (\( \nN \)S). (P3): for \( n \in \nN \), \( n \ge 0 \) by @lem-naturals-arithmetic (a), so \( n + 1 \ge 1 > 0 \) and \( n + 1 \ne 0 \). (P4): \( m + 1 = n + 1 \) gives \( m = n \), by subtracting \( 1 \) in \( \nR \). (P5): a subset of \( \nN \) that contains \( 0 \) and is closed under \( n \mapsto n + 1 \) is \( \nN \); this is the set form of @ax-induction, the remark at the start of Section 7.1. So \( (\nN, 0, s) \) is a Peano system (@def-peano-system), and @thm-peano-categoricity (a), (b) give exactly one \( \varphi \) as stated, and it is a bijection.

For the operations, take \( \oplus \) and \( \otimes \) to be the addition and multiplication of \( \nN \); they are functions \( \nN \times \nN \to \nN \) by @lem-naturals-arithmetic (b). The four equations of @prp-isomorphism-preserves-arithmetic read \( x + 0 = x \), \( x + (y + 1) = (x + y) + 1 \), \( x \cdot 0 = 0 \) and \( x(y + 1) = xy + x \), which hold in \( \nR \). That proposition gives \( \varphi(m + n) = \varphi(m) + \varphi(n) \) and \( \varphi(mn) = \varphi(m)\varphi(n) \).

For the order we first show: for \( x, y \in \nN \), \( x < y \) if and only if \( y = x + z \) for some \( z \in \nN \) with \( z \ne 0 \). If \( x < y \), then \( z \coloneqq y - x \in \nN \) by @lem-naturals-arithmetic (d), and \( z \ne 0 \) since \( y \ne x \). Conversely, \( z \ne 0 \) gives \( z \ge 1 > 0 \) by @lem-naturals-arithmetic (a), so \( y = x + z > x \). Now @prp-isomorphism-preserves-arithmetic (c), with \( e = 0 \), says that \( m < n \) if and only if \( \varphi(n) = \varphi(m) + z \) for some \( z \in \nN \) with \( z \ne 0 \), that is, if and only if \( \varphi(m) < \varphi(n) \).

Finally, \( \varphi(0) = 0 \), and each numeral of \( \omega \) is the successor of the one before (@def-omega-arithmetic (c)), so \( \varphi(1) = \varphi(\mathrm{S}(0)) = 0 + 1 = 1 \), \( \varphi(2) = \varphi(\mathrm{S}(1)) = 1 + 1 = 2 \), and so on, one step for each numeral written.

*(b)* By the two equations of @def-omega-arithmetic (a), \( n + 1 = n + \mathrm{S}(0) = \mathrm{S}(n + 0) = \mathrm{S}(n) \) for every \( n \in \omega \) (Section 9.5, "the successor is plus one"). With \( \nN \coloneqq \omega \), the statement of @ax-induction becomes @thm-omega-induction (b), and the statement of @thm-recursion is word for word @thm-omega-recursion. Induction from a base \( b \in \omega \) is @prp-omega-order-arithmetic (g).

*(c)* We take the clauses of @lem-naturals-arithmetic in turn, for \( m, n \in \omega \).

- (a) "\( n \ge 0 \); if \( n \ne 0 \), then \( n \ge 1 \)" is @thm-omega-order (d).
- (b) "\( m + n \in \omega \) and \( mn \in \omega \)" holds because \( + \) and \( \cdot \) are functions \( \omega \times \omega \to \omega \) (@def-omega-arithmetic).
- (c) If \( n \ne 0 \), then \( 1 \le n \) by @thm-omega-order (d), so \( n = 1 + j \) for exactly one \( j \in \omega \) by @prp-omega-order-arithmetic (a); this \( j \) is \( n - 1 \), and it lies in \( \omega \).
- (d) If \( m \le n \), then \( n - m \in \omega \) by @prp-omega-order-arithmetic (a).
- (e) No \( k \in \omega \) has \( n < k < \mathrm{S}(n) \), by @thm-omega-order (b). For the second form, let \( m < n \). By trichotomy (@thm-omega-order (a)), \( \mathrm{S}(m) < n \), \( \mathrm{S}(m) = n \) or \( n < \mathrm{S}(m) \). The last gives \( n \le m \) by @thm-omega-order (b), and then \( n \le m < n \) gives \( n < n \) by transitivity, which (a) of that theorem rules out. So \( m + 1 = \mathrm{S}(m) \le n \).

This proves the corollary.
:::

Clause (a) is the honest sense in which "\( \omega \) **is** \( \nN \)": the two are copies of each other by a unique isomorphism, which also matches \( + \), \( \cdot \) and \( < \). But (a) is a theorem about Chapter 7's \( \nN \), and its proof used the school arithmetic of \( \nR \) (in (P3), (P4), the four equations, the step describing \( < \) by \( + \), and the numerals). The answer to the prompt is therefore (b), with (c): when a later chapter applies induction or recursion to \( \omega \), it uses a theorem proved here from the axioms for sets, and nothing about the school real numbers enters.

::: {.warning}
The isomorphism carries \( 0 \), successor, \( + \), \( \cdot \) and \( < \), and nothing else. In \( \omega \), \( 0 \in 5 \) and \( 2 \subseteq 3 \) are true, because natural numbers here are sets (@exm-von-neumann-numerals). In Chapter 7's picture numbers are not sets, and "\( 0 \in 5 \)" has no meaning there. Such statements are facts about one particular construction, and no theorem of the later chapters asks them.
:::

## How later chapters cite Chapters 3 and 7

In the rest of this volume, \( \nN \) **means** \( \omega \), with the \( 0 \), \( + \), \( \cdot \) and \( < \) of this chapter. The later chapters build \( \nZ \), \( \nQ \) and finally \( \nR \) from it, and they cite results of Chapters 3, 7 and 8 about \( \nN \). This subsection says how such a citation is to be read, so that the construction of \( \nR \) never rests on the school \( \nR \) it is meant to replace.

The proofs in Chapters 7 and 8 use the arithmetic of the real numbers freely: Chapter 7's "What you need" paragraph takes the arithmetic and order of \( \nR \) as school facts, Section 7.1 says so for itself in "the rule for this section", and Chapter 8's proofs do the same (@thm-binary-sequences-uncountable, for example, uses \( 1 - b \)). So they do **not** rest only on (\( \nN \)0), (\( \nN \)S), @ax-induction, @thm-recursion and @lem-naturals-arithmetic, and "they hold unchanged on \( \omega \)" would be false. What is true is a **dictionary**: each fact about \( \nN \) those proofs use has a counterpart proved on \( \omega \) here.

| used for \( \nN \) in Chapters 3, 7, 8 | read on \( \omega \) as |
|---|---|
| @ax-induction; @thm-recursion | @cor-omega-identification (b): @thm-omega-induction (b); @thm-omega-recursion |
| @thm-induction with a base \( n_0 = b \in \nN \), induction from a base | @prp-omega-order-arithmetic (g) |
| @thm-well-ordering | @thm-omega-well-ordering |
| @lem-naturals-arithmetic | @cor-omega-identification (c) |
| other school arithmetic and order of natural numbers: closure under \( + \), \( \cdot \); cancellation; trichotomy; \( n - m \) for \( m \le n \); "subtract \( 1 \) from \( m > n + 1 \)" | @thm-omega-arithmetic-laws, @thm-omega-order, @prp-omega-order-arithmetic |
| powers \( b^n \) of a natural number, @def-power, @prp-power-laws (a), (d), (e) | @prp-omega-powers-parity (a)–(c); closure of \( \omega \) under powers is the definition there |
| "no natural number is both even and odd" | @prp-omega-powers-parity (d) |

With the dictionary, the results of Chapters 7 and 8 that later chapters cite fall into three groups.

(i) **Results that run on \( \omega \) through the dictionary.** These are @prp-finite-max (for its \( \nN \) side, which is @thm-induction with base \( 1 \) and @lem-naturals-arithmetic (e)), @def-finite, @def-infinite, @cor-pigeonhole-finite-sets, @thm-finite-no-proper-copy, @lem-subsets-of-naturals, @thm-countable-characterizations, @prp-countable-subset, @prp-countable-image and @thm-binary-sequences-uncountable (where \( \{0, 1\}^{\nN} \) is indexed by \( \omega \), and \( 1 - b \) on \( \{0, 1\} \) is read by @prp-omega-order-arithmetic (a)), and @exr-finite-sets-c2 (a), cited later only from an exercise solution (its \( \nN \) side is an induction on \( m \), read by @cor-omega-identification (b), \( mn \in \nN \), read by @cor-omega-identification (c), and \( 0 = 0 \cdot n \) and \( mn + n = (m + 1)n \), read by @thm-omega-arithmetic-laws (e)). Running a result on \( \omega \) includes the results its proof cites: @thm-pigeonhole, @prp-disjoint-union-count, @prp-subset-finite, @cor-finite-size-unique, @cor-remove-point and the count "\( \{0, \dots, x\} \) has \( x + 1 \) elements" in the examples after @def-finite run through the same dictionary, and they belong to group (i) themselves. A later chapter may cite the results of group (i) anywhere.

(ii) **Results that use school facts, and need @prp-omega-powers-parity on \( \omega \).** These are @thm-product-countable (powers by @def-power and @prp-power-laws (a), (d), (e) over the school \( \nR \), parity through @thm-division-algorithm on the school \( \nZ \), and cancellation in \( \nR \)), @prp-union-two-countable (parity through @thm-division-algorithm), and through them @cor-product-countable (a). On \( \omega \), the powers are read as @prp-omega-powers-parity (a)–(c), the parity claim as its (d), and cancellation as @prp-omega-order-arithmetic (b), (f); with that, each of these proofs runs on \( \omega \). A later chapter may cite them only in a review (R) exercise; anywhere else, a construction that needs one of them proves it on \( \omega \) first. Part (b) of @cor-product-countable is not in this group and is not checked on \( \omega \) here: Chapter 8 treats its list \( A_1, \dots, A_k \) as a family in the everyday sense of @def-indexed-family, with no set holding it, and Section 9.2 left such families to the axiom of Replacement. A list given as a function on \( \{1, \dots, k\} \), with graph \( G \), does have an ambient set: each \( A_i \) lies in \( \bigcup \bigcup G \) by (Z4), so the union of the \( A_i \) exists by (Z4) and (Z6), and the proof of (b) can then be run on \( \omega \), with its base case (a) read as above and its @thm-induction from base \( 2 \) read by @prp-omega-order-arithmetic (g). A later chapter that needs (b) proves it on \( \omega \) first, in that form. @thm-integers-rationals-countable is a statement about the school \( \nZ \) and \( \nQ \), and is never applied to \( \omega \).

(iii) **Templates.** @def-sum-product and @prp-power-laws are used later only as patterns, with the school \( \nR \) replaced by an ordered field \( F \). Their \( \nN \) side is read through the dictionary, and their field side is proved again from the axioms of \( F \). The parts that need \( \nZ \) (@prp-power-laws (d) for an integer base, and the general index of @def-sum-product, which uses @prp-integers-closed) are not part of the pattern.

Finally, the axiom of choice. Apart from Chapter 7's \( \nN \subseteq \nR \) and its school operations, which @cor-omega-identification (a) takes as given, every set in Sections 9.1–9.7 is produced by one of (Z1)–(Z7). Every function is produced by @thm-omega-recursion, by (Z6) applied to a graph described by a property (as \( g \) was in the proof of @thm-peano-categoricity (a)), or by Chapter 6's inverses and composites of such functions. Nothing is chosen from infinitely many sets, and @ax-choice is used nowhere in this chapter; it is mentioned only to say where it lives.

So everything that Chapters 3 and 7 assumed about \( \nN \) (that \( 0 \) is a natural number, that \( n + 1 \) is one whenever \( n \) is, induction, recursion, and the arithmetic of @lem-naturals-arithmetic) is now proved, from seven axioms about sets. The set-theory volume returns to those axioms and adds the rest of the system. Chapter 10 builds \( \nZ \) and \( \nQ \) from \( \omega \) by the same kind of construction as here: pairs, and classes of pairs.

## Exercises

### A. Check your understanding

::: {#exr-categoricity-a1}
[A1]

These questions are about the proof of @thm-peano-categoricity.

::: {.enumerate options="label=(\alph*)"}
1. Where in the proof is (P5) for \( M \) used, and where are (P3) and (P4) for \( M \) used?
2. Where is (P4) for \( \omega \) used? (It is not visible in the proof itself.)
3. Run \( \varphi \) of part (a) for the system \( (\omega \setminus \{0\}, 1, \mathrm{S}) \) on \( 0 \), \( 1 \) and \( 2 \), from the two equations alone.
4. State the idea of the proof of (a) and (b) in two sentences.
:::
:::

::: {.solution}
(a) (P5) for \( M \) is used once, for surjectivity: the image \( \varphi(\omega) \) contains \( e \) and is closed under \( s \), so it is \( M \). (P3) for \( M \) is used for injectivity, in the base case (\( \varphi(\mathrm{S}(k)) = s(\varphi(k)) \ne e \), so only \( m = 0 \) has \( \varphi(m) = e \)) and at the start of the inductive step (to exclude \( m = 0 \)). (P4) for \( M \) is used in the inductive step, to pass from \( s(\varphi(k)) = s(\varphi(n)) \) to \( \varphi(k) = \varphi(n) \).

(b) Inside part (a), through @thm-omega-recursion: its proof extends a partial solution by one new pair at \( \mathrm{S}(n) \), and (P4) for \( \omega \) makes \( \mathrm{S}(n) \) the successor of \( n \) only, so the equation at \( \mathrm{S}(n) \) asks for \( g(n, h(n)) \) and nothing else.

(c) \( \varphi(0) = 1 \); \( \varphi(1) = \varphi(\mathrm{S}(0)) = \mathrm{S}(\varphi(0)) = \mathrm{S}(1) = 2 \); \( \varphi(2) = \varphi(\mathrm{S}(1)) = \mathrm{S}(2) = 3 \).

(d) The map is forced at \( 0 \) and at each successor, so the recursion theorem builds it and makes it unique. It is onto because its image contains \( e \) and is closed under \( s \), so (P5) for \( M \) applies; it is one-to-one by an induction whose base and step are (P3) and (P4) for \( M \).
:::

### B. Practice

::: {#exr-categoricity-b1}
[B1: The even numbers]

Let \( E \coloneqq \{ 2n : n \in \omega \} \), with \( e \coloneqq 0 \) and \( s(x) \coloneqq x + 2 \) for \( x \in E \). Show that \( (E, 0, s) \) is a Peano system, and that the map \( \varphi \) of @thm-peano-categoricity is \( \varphi(n) = 2n \).
:::

::: {.solution}
\( E \) is a set by (Z6) inside \( \omega \): it is \( \{ x \in \omega : x = 2n \text{ for some } n \in \omega \} \). By @def-omega-arithmetic (b), \( 2 \cdot \mathrm{S}(n) = 2n + 2 \) for every \( n \in \omega \). So \( s \) maps \( E \) into \( E \): \( s(2n) = 2n + 2 = 2 \cdot \mathrm{S}(n) \in E \).

(P3): \( 2n + 2 = 2n + \mathrm{S}(1) = \mathrm{S}(2n + 1) \) by @def-omega-arithmetic (a), and a successor is never \( 0 \) (@thm-omega-peano (P3)). (P4): if \( x + 2 = y + 2 \), then \( x = y \) by @prp-omega-order-arithmetic (b). (P5): let \( A \subseteq E \) with \( 0 \in A \) and \( x + 2 \in A \) for every \( x \in A \). Let \( B \coloneqq \{ n \in \omega : 2n \in A \} \). Then \( 0 \in B \), since \( 2 \cdot 0 = 0 \in A \); and if \( n \in B \), then \( 2 \cdot \mathrm{S}(n) = 2n + 2 \in A \), so \( \mathrm{S}(n) \in B \). By @thm-omega-induction (a), \( B = \omega \), so every \( 2n \) lies in \( A \), and \( A = E \).

The map \( n \mapsto 2n \) from \( \omega \) to \( E \) sends \( 0 \) to \( 2 \cdot 0 = 0 = e \), and \( 2 \cdot \mathrm{S}(n) = 2n + 2 = s(2n) \). By the uniqueness in @thm-peano-categoricity (a), it is \( \varphi \). In particular, by (b) of that theorem, \( n \mapsto 2n \) is a bijection \( \omega \to E \).
:::

::: {#exr-categoricity-b2}
[B2: The identification at work]

Let \( \varphi \colon \omega \to \nN \) be the bijection of @cor-omega-identification (a).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \varphi(3) \) step by step from the two equations of \( \varphi \).
2. Compute \( \varphi(2 \cdot 3) \) in two ways: from (a) of the corollary, and by unwinding \( 2 \cdot 3 \) in \( \omega \) to a numeral first.
:::
:::

::: {.solution}
(a) Using \( \varphi(0) = 0 \) and \( \varphi(\mathrm{S}(n)) = \varphi(n) + 1 \), with \( 3 = \mathrm{S}(2) \), \( 2 = \mathrm{S}(1) \), \( 1 = \mathrm{S}(0) \) (@def-omega-arithmetic (c)):
\[
\varphi(3) = \varphi(2) + 1 = \bigl(\varphi(1) + 1\bigr) + 1 = \bigl((0 + 1) + 1\bigr) + 1 = 3 .
\]

(b) By the corollary, \( \varphi(2 \cdot 3) = \varphi(2)\varphi(3) = 2 \cdot 3 = 6 \) in \( \nN \), where \( \varphi(2) = 2 \) as in (a). In \( \omega \), \( 2 \cdot 3 = 2 \cdot 2 + 2 = (2 \cdot 1 + 2) + 2 = ((2 \cdot 0 + 2) + 2) + 2 = 6 \), by @def-omega-arithmetic (b) three times and then \( 2 \cdot 0 = 0 \), \( 0 + 2 = 2 \), \( 2 + 2 = 4 \), \( 4 + 2 = 6 \) from the equations for \( + \). Then \( \varphi(6) = 6 \) by six steps as in (a). The two answers agree, as the corollary says they must.
:::

### C. Going deeper

::: {#exr-categoricity-c1}
[C1: Writing out categoricity]

Without looking at the text, prove part (b) of @thm-peano-categoricity: for a Peano system \( (M, e, s) \), the map \( \varphi \colon \omega \to M \) with \( \varphi(0) = e \) and \( \varphi(\mathrm{S}(n)) = s(\varphi(n)) \) is a bijection.
:::

::: {.solution}
[Hint 1]

For surjectivity, use (P5) for \( M \) on a set built from \( \varphi \). For injectivity, induct on \( n \); decide first where "for every \( m \)" goes.
:::

::: {.solution}
[Hint 2]

The induction for injectivity starts: "Let \( Q(n) \) be: for every \( m \in \omega \), \( \varphi(m) = \varphi(n) \) implies \( m = n \)."
:::

::: {.solution}
*Onto.* The image \( B \coloneqq \varphi(\omega) \) (@def-image) contains \( e = \varphi(0) \), and \( x = \varphi(n) \in B \) gives \( s(x) = \varphi(\mathrm{S}(n)) \in B \). By (P5) for \( M \), \( B = M \).

*One-to-one.* By @thm-omega-induction (b) we prove, for every \( n \), \( Q(n) \): "for every \( m \in \omega \), \( \varphi(m) = \varphi(n) \) implies \( m = n \)". For \( Q(0) \), let \( \varphi(m) = e \); an \( m \ne 0 \) is \( \mathrm{S}(k) \) (@lem-omega-transitive (d)), with \( \varphi(m) = s(\varphi(k)) \ne e \) by (P3) for \( M \); so \( m = 0 \). For the step, assume \( Q(n) \) and \( \varphi(m) = s(\varphi(n)) \). Then \( m \ne 0 \), as \( e \) is not a value of \( s \) (P3 for \( M \)); so \( m = \mathrm{S}(k) \), and \( s(\varphi(k)) = s(\varphi(n)) \) gives \( \varphi(k) = \varphi(n) \) by (P4) for \( M \), hence \( k = n \) by \( Q(n) \) used at \( k \), and \( m = \mathrm{S}(n) \). So \( \varphi \) is injective, and a bijection.

**Marking scheme.** (10 points)
- 3: surjectivity: shows the image of \( \varphi \) contains \( e \) and is closed under \( s \), and cites (P5) for \( M \).
- 2: sets up an induction (on either variable, or by least counterexample) whose hypothesis is strong enough to use at the predecessor, e.g. \( Q(n) \) with "for every \( m \)" inside, or the difference \( j \ne 0 \) fixed and induction on \( m \).
- 2: base case, via \( m = \mathrm{S}(k) \) for \( m \ne 0 \) and (P3) for \( M \).
- 3: inductive step, using (P3) for \( M \) to get \( m \ne 0 \), (P4) for \( M \) to cancel \( s \), and the induction hypothesis at the predecessor \( k \).
Fatal errors (0 for the part concerned): an induction whose hypothesis is then applied at a value it does not cover (typically: \( m \) fixed outside \( Q \), then used at \( k \)); using injectivity of \( \varphi \) to prove injectivity; using (P3), (P4) or (P5) **for \( \omega \)** where the axiom for \( M \) is needed. A proof of injectivity by @thm-omega-well-ordering (a least \( n \) with some \( m \ne n \), \( \varphi(m) = \varphi(n) \)) earns the same 7 points, mapped to base, step and hypothesis in the same way. So does the fixed-difference route (reducing to \( \varphi(m + j) \ne \varphi(m) \) for \( j \ne 0 \) by @thm-omega-order (a) and @prp-omega-order-arithmetic (a), and inducting on \( m \)): its base uses (P3) for \( M \), its step (P4) for \( M \) and the hypothesis at \( m \), and the points are mapped in the same way.
:::

::: {#exr-categoricity-c2}
[C2: Without induction, no recursion]

Let \( (M, e, s) \) be structure (iii) of @exm-peano-axioms-independent, the natural numbers beside a two-sided chain: \( M = \omega \times 3 \), \( e = (0, 0) \), \( s(n, 0) = (\mathrm{S}(n), 0) \), \( s(n, 1) = (\mathrm{S}(n), 1) \), \( s(0, 2) = (0, 1) \) and \( s(\mathrm{S}(k), 2) = (k, 2) \). Show that there is **no** function \( f \colon M \to \omega \) with \( f(e) = 0 \) and \( f(s(x)) = \mathrm{S}(f(x)) \) for every \( x \in M \). Which Peano axiom, missing in \( M \), is responsible?
:::

::: {.solution}
Suppose such an \( f \) exists. For every \( k \in \omega \), \( s(\mathrm{S}(k), 2) = (k, 2) \), so
\[
f\bigl((k, 2)\bigr) = \mathrm{S}\Bigl(f\bigl((\mathrm{S}(k), 2)\bigr)\Bigr) .
\]
Let \( T \coloneqq \{ f((k, 2)) : k \in \omega \} \subseteq \omega \), a set by (Z6) inside \( \omega \); it is non-empty, since it contains \( f((0, 2)) \). By @thm-omega-well-ordering, \( T \) has a least element \( t = f((k_0, 2)) \). But \( u \coloneqq f((\mathrm{S}(k_0), 2)) \in T \), and \( t = \mathrm{S}(u) \), so \( u \in \mathrm{S}(u) = t \), that is, \( u < t \) (@def-omega-order). This contradicts the leastness of \( t \), since \( t \le u \) and \( u < t \) would give \( u < u \) (@thm-omega-order (a)). So no such \( f \) exists. (The condition \( f(e) = 0 \) was not even used: no map at all turns \( s \) into \( \mathrm{S} \).)

\( M \) satisfies (P3) and (P4) and fails only (P5) (@exm-peano-axioms-independent). So (P5) is what makes the recursion theorem possible: the downward chain \( (0, 2), (1, 2), (2, 2), \dots \), each element the successor of the next, would need values in \( \omega \) that decrease forever.
:::

### R. Review

::: {#exr-categoricity-r1}
[R1]

Prove that \( \omega \) is infinite.
:::

::: {.solution}
We read @def-infinite and @thm-finite-no-proper-copy on \( \omega \), through the dictionary of this section (group (i)). Consider \( \mathrm{S} \) with codomain \( \omega \setminus \{0\} \); its values lie there by @thm-omega-peano (P3). It is injective by (P4) of that theorem, and onto \( \omega \setminus \{0\} \) by @lem-omega-transitive (d): every \( n \ne 0 \) is \( \mathrm{S}(k) \) for some \( k \in \omega \). So it is a bijection \( \omega \to \omega \setminus \{0\} \). The set \( \omega \setminus \{0\} \) is a proper subset of \( \omega \), since \( 0 \in \omega \) and \( 0 \notin \omega \setminus \{0\} \). By @thm-finite-no-proper-copy, a finite set is not equinumerous with any proper subset; so \( \omega \) is not finite, that is, it is infinite (@def-infinite). This is the Quick check after @exm-hilbert-hotel (every guest moves up one room), built from (P3) and (P4).
:::

::: {#exr-categoricity-r2}
[R2]

Show that the successor function \( \mathrm{S} \colon \omega \to \omega \) has a left inverse and no right inverse. Write a left inverse down explicitly. Is it the only one?
:::

::: {.solution}
*No right inverse.* A function with a right inverse is surjective (@prp-right-inverse-surjective), and \( \mathrm{S} \) is not: \( 0 \) is not a value, by @thm-omega-peano (P3).

*A left inverse.* Let \( L \colon \omega \to \omega \) have the graph
\[
G \coloneqq \bigl\{ (n, k) \in \omega \times \omega : (n = 0 \text{ and } k = 0) \text{ or } n = \mathrm{S}(k) \bigr\},
\]
a set by (Z6). Each \( n \in \omega \) has exactly one partner. If \( n = 0 \), the partner \( k = 0 \) works, and no \( k \) has \( 0 = \mathrm{S}(k) \), by (P3). If \( n \ne 0 \), then \( n = \mathrm{S}(k) \) for some \( k \) (@lem-omega-transitive (d)), and only one, by (P4). So \( L \) is a function (@def-function) with \( L(0) = 0 \) and \( L(\mathrm{S}(k)) = k \). Hence \( L(\mathrm{S}(n)) = n \) for every \( n \in \omega \), that is, \( L \circ \mathrm{S} = \id_\omega \): \( L \) is a left inverse of \( \mathrm{S} \) (@def-left-right-inverse (a)). This matches @thm-left-inverse-iff-injective: \( \mathrm{S} \) is injective and \( \omega \ne \emptyset \).

*Not unique.* The value of a left inverse at \( 0 \) is never used, since \( 0 \) is not of the form \( \mathrm{S}(n) \); setting \( L'(0) \coloneqq 5 \) and \( L'(\mathrm{S}(k)) \coloneqq k \) gives another left inverse.
:::

::: {#exr-categoricity-r3}
[R3]

Let \( M = \{0, 1\} \), \( e = 0 \) and \( s(0) = s(1) = 1 \). Show that there is no function \( f \colon M \to \omega \) with \( f(0) = 0 \) and \( f(s(x)) = \mathrm{S}(f(x)) \) for every \( x \in M \). Which of the Peano axioms play the part, for definitions on \( \omega \), that a theorem about reading formulas plays for definitions on formulas?
:::

::: {.solution}
Suppose \( f \) exists. Taking \( x = 1 \), \( f(1) = f(s(1)) = \mathrm{S}(f(1)) \). But no \( n \in \omega \) has \( n = \mathrm{S}(n) \): \( n \in \mathrm{S}(n) \) (@def-set-successor), so \( n = \mathrm{S}(n) \) would give \( n \in n \), against @lem-omega-transitive (c). So no such \( f \) exists. (Taking \( x = 0 \) instead gives \( f(1) = \mathrm{S}(0) = 1 \), so the two equations at the input \( 1 \) also contradict each other.)

The trouble is that \( 1 \) is built in two ways, as \( s(0) \) and as \( s(1) \), and the two ways ask for different values. In Chapter 3, @thm-structural-recursion defines functions on formulas, and what makes it work is @thm-unique-readability: each compound formula is built from its parts in exactly one way. On \( \omega \) the same job is done by (P3) and (P4): \( 0 \) is not a successor, so its value is not asked for twice, and a successor is the successor of exactly one number, so the equation at \( \mathrm{S}(n) \) asks for one thing. The structure \( M \) fails (P4), since \( s(0) = s(1) \), though it satisfies (P5).
:::

::: {#exr-categoricity-r4}
[R4]

For \( n \in \omega \), compute \( \bigcup \mathrm{S}(n) \) and \( \bigcup n \). Then find a set \( x \) with \( \bigcup \mathrm{S}(x) \ne x \).
:::

::: {.solution}
*A formula for every set.* For any set \( x \), \( \bigcup \mathrm{S}(x) = \bigcup (x \cup \{x\}) = \bigcup x \cup x \): an element of a member of \( x \cup \{x\} \) is an element of a member of \( x \), or an element of \( x \) itself.

*For \( n \in \omega \).* The tool is transitivity. By @lem-omega-transitive (a), \( n \) is transitive, so every element of a member of \( n \) is a member of \( n \), that is, \( \bigcup n \subseteq n \). Hence \( \bigcup \mathrm{S}(n) = \bigcup n \cup n = n \). For \( \bigcup n \) itself: \( \bigcup 0 = \bigcup \emptyset = \emptyset = 0 \); and if \( n \ne 0 \), then \( n = \mathrm{S}(k) \) (@lem-omega-transitive (d)), and \( \bigcup n = \bigcup \mathrm{S}(k) = k \) by what we just proved. So \( \bigcup \) undoes the successor: it is the "predecessor" on \( \omega \), with \( 0 \) sent to \( 0 \).

*A set where it fails.* Let \( x \coloneqq \{1\} = \{\{\emptyset\}\} \). Then \( \bigcup x = 1 = \{\emptyset\} \), and \( \bigcup \mathrm{S}(x) = \{\emptyset\} \cup \{\{\emptyset\}\} = \{0, 1\} = 2 \). This is not \( x \): \( 0 = \emptyset \in 2 \), but \( \emptyset \notin x \), since the only element of \( x \) is \( \{\emptyset\} \ne \emptyset \).

*Why the identity alone is not enough.* The look-alike tool is the identity \( \bigcup \mathrm{S}(x) = \bigcup x \cup x \), which holds for every set. On its own it does not give \( x \): it gives \( \bigcup \mathrm{S}(x) = x \) **exactly** when \( \bigcup x \subseteq x \), that is, when \( x \) is transitive (@def-transitive-set), and \( \{1\} \), which is not transitive, is a witness that this can fail. Nor is an induction on \( n \) a route that avoids transitivity: its step \( \bigcup \mathrm{S}(\mathrm{S}(n)) = \bigcup \mathrm{S}(n) \cup \mathrm{S}(n) = n \cup \mathrm{S}(n) = \mathrm{S}(n) \) proves \( \bigcup \mathrm{S}(n) = n \), which is equivalent to transitivity of \( n \), so it proves @lem-omega-transitive (a) again along the way.
:::

<!-- dependency ledger
thm-peano-categoricity (claim): (opening subsection) (omega \ {0}, 1, S) is a Peano system | inline (three lines; exr-peano-properties-c1 asks the same, not relied on)
thm-peano-categoricity (proof): every m in omega is 0 or not 0 (case split before lem-omega-transitive (d)) | classical case split (excluded middle), standing in Part 0
thm-peano-categoricity (proof): phi(0) = e gives phi^{-1}(e) = 0, and x = phi(phi^{-1}(x)) | def-inverse-function, through thm-bijection-iff-inverse (cited)
thm-peano-categoricity (proof): phi^{-1} is a bijection (phi is an inverse of it) | def-inverse-function, thm-bijection-iff-inverse (cited)
thm-peano-categoricity (claim): (list after the proof) phi(1) = phi(0) in {0}; phi(1) = phi(2) in {0, 1} | inline (two steps of the recursion each); verify/ch09/thm-peano-categoricity.py
thm-peano-categoricity (claim): (list after the proof and remark) phi exists and is unique for structures (i)-(iii); phi(n) = (n, 0) in omega x 3 is injective, and (0, 1) is not of that form | thm-omega-recursion (cited; existence and uniqueness, the theorem itself not applying); thm-kuratowski-pair (cited) for injectivity; thm-kuratowski-pair with 0 != 1 (thm-omega-peano (P3)); verify/ch09/thm-peano-categoricity.py
cor-omega-identification (proof): real arithmetic for (a): subtracting 1 (P4); n + 1 >= 1 > 0; x + 0 = x, x + (y + 1) = (x + y) + 1, x 0 = 0, x(y + 1) = xy + x; y = x + z > x for z > 0; 0 + 1 = 1 and k + 1 is the next numeral (numerals) | school fact (fd2's standing description of N, Section 7.1), used only in (a)
cor-omega-identification (proof): (P5) for Chapter 7's N | the remark at the start of Section 7.1 (unlabeled; set form of ax-induction, cited)
cor-omega-identification (proof): n <= m < n gives n < n, in (c)(e) | thm-omega-order (a) (transitivity, irreflexivity), cited
cor-omega-identification (claim): (citing rule, group (ii)) cor-product-countable (b) is not checked on omega here: Chapter 8 treats its list as an informal family with no ambient set (Replacement, the set-theory volume); a list given as a function G has its entries in the union of the union of G by (Z4), and its union by (Z4), (Z6) | stated; nothing depends on it
cor-omega-identification (claim): (citing rule, groups (i)-(iii)) which fd2 facts about N each listed proof uses | meta-claim of blueprint ch09.md, section 07, checked label by label at S2; S8 re-verifies
cor-omega-identification (claim): (citing rule, group (i)) exr-finite-sets-c2 (a) and cor-remove-point run on omega: induction on m, mn in N, 0 = 0 n, mn + n = (m + 1)n; cor-remove-point through prp-subset-finite, prp-disjoint-union-count, cor-finite-size-unique and k + 1 = n + 1 => k = n | checked here against the proofs of exr-finite-sets-c2 (a) and cor-remove-point in Section 8.1 (cor-omega-identification (b), (c); thm-omega-arithmetic-laws (e); cancellation by prp-omega-order-arithmetic (b)); not in the frozen blueprint, blueprint sync deferred
cor-omega-identification (claim): (choice paragraph) apart from Chapter 7's N in (a), every set from (Z1)-(Z7), every function from thm-omega-recursion, (Z6), or Chapter 6's inverses and composites of these; ax-choice unused | meta-claim about Sections 9.1-9.7 (blueprint "Choice audit"); S8 checks the other sections
exr-categoricity-b1 (solution): 2 = S(1), so 2n + 2 = S(2n + 1) | def-omega-arithmetic (a), (c), cited; verify/ch09/exr-categoricity-b1.py
exr-categoricity-b2 (solution): 2 * 3 = 6, 0 + 2 = 2, 2 + 2 = 4, 4 + 2 = 6 from the defining equations; 2 * 3 = 6 in Chapter 7's N | inline; school fact in N; verify/ch09/exr-categoricity-b2.py
exr-categoricity-c2 (solution): u in S(u) | def-set-successor
exr-categoricity-r1 (solution): def-infinite and thm-finite-no-proper-copy read on omega | the dictionary of this section, group (i)
exr-categoricity-r3 (solution): n in S(n) | def-set-successor (cited)
exr-categoricity-r4 (solution): union of (x u {x}) = (union x) u x; union of the empty set is empty | inline, from (Z4) and (Z1); verify/ch09/exr-categoricity-r4.py
exr-categoricity-r4 (solution): {emptyset} != emptyset | def-empty-set (emptyset is in {emptyset})
-->
