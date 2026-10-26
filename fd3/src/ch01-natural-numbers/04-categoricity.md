# All Peano Systems Are Alike

Section 1.1 fixed one Peano system and called it \( (\nN, 0, \mathrm{S}) \). It is not the only one. The natural numbers of *Sets and Functions*, Chapter 3, sitting inside the familiar real numbers, form another; the numbers from \( 1 \) on, \( (\nN \setminus \{0\}, 1, \mathrm{S}) \), form a third; and *Axiomatic Set Theory* builds a fourth out of sets alone (Section 1.5 describes how). So a question is left: does the choice matter? This section answers no. Any two Peano systems are copies of each other, by exactly one matching, and that matching also carries \( + \), \( \cdot \) and \( < \) across. Then it says how the later chapters read what *Logic and Proof*, Chapter 4, and *Sets and Functions*, Chapters 3 and 4 proved about natural numbers.

## Two Peano systems, and what "alike" should mean

Here is a second Peano system, inside \( \nN \) itself: \( (\nN \setminus \{0\}, 1, \mathrm{S}) \), the natural numbers from \( 1 \) on, with the same successor. Exercise C1 of Section 1.1 asked for the check; here it is, in three lines.

- \( \mathrm{S} \) maps \( \nN \setminus \{0\} \) into itself, since \( \mathrm{S}(n) \ne 0 \) by (P3) for \( \nN \).
- (P3) holds with \( e = 1 \): if \( \mathrm{S}(n) = 1 = \mathrm{S}(0) \), then \( n = 0 \) by (P4) for \( \nN \), and \( 0 \notin \nN \setminus \{0\} \). (P4) holds because \( \mathrm{S} \) is injective on all of \( \nN \).
- (P5) holds: if \( A \subseteq \nN \setminus \{0\} \) contains \( 1 \) and is closed under \( \mathrm{S} \), then \( \{0\} \cup A \) contains \( 0 \) and is closed under \( \mathrm{S} \) (as \( \mathrm{S}(0) = 1 \in A \)), so it is \( \nN \) by @thm-omega-induction (a), and \( A = \nN \setminus \{0\} \).

Its starting point is \( 1 \), not \( 0 \), yet it counts the same way: \( n \mapsto \mathrm{S}(n) \) pairs \( 0, 1, 2, \dots \) with \( 1, 2, 3, \dots \), sends start to start, and turns one step into one step.

That is the right meaning of "alike". For Peano systems \( (M, e, s) \) and \( (M', e', s') \), call a bijection \( \psi \colon M \to M' \) an **isomorphism** if
\[
\psi(e) = e' \quad \text{and} \quad \psi\bigl(s(x)\bigr) = s'\bigl(\psi(x)\bigr) \ \text{ for every } x \in M .
\]
In words: \( \psi \) renames the elements, sends start to start, and stepping then renaming is the same as renaming then stepping.

::: {.warning}
Being equinumerous is not enough. The bijection \( \tau \colon \nN \to \nN \) that exchanges \( 1 \) and \( 2 \) and fixes every other number satisfies \( \tau(0) = 0 \), but \( \tau(\mathrm{S}(0)) = \tau(1) = 2 \), while \( \mathrm{S}(\tau(0)) = \mathrm{S}(0) = 1 \). So \( \tau \) is a bijection from a Peano system to itself that is **not** an isomorphism: it does not respect the successor. Categoricity, below, is a statement about isomorphisms, and it says much more than "same size".
:::

## The categoricity theorem

The theorem says that every Peano system is an isomorphic copy of \( \nN \), and so any two are copies of each other, in only one way.

::: {#thm-peano-categoricity}
[Categoricity of the Peano Axioms]

Let \( (M, e, s) \) be a Peano system.

::: {.enumerate options="label=(\alph*)"}
1. There is **exactly one** function \( \varphi \colon \nN \to M \) with \( \varphi(0) = e \) and \( \varphi(\mathrm{S}(n)) = s(\varphi(n)) \) for every \( n \in \nN \).
2. This \( \varphi \) is a bijection.
3. For any two Peano systems \( (M, e, s) \) and \( (M', e', s') \) there is **exactly one** bijection \( \psi \colon M \to M' \) with \( \psi(e) = e' \) and \( \psi(s(x)) = s'(\psi(x)) \) for every \( x \in M \).
:::
:::

*Try it first (ten minutes): given a Peano system \( (M, e, s) \), which map \( \nN \to M \) would you build, with which theorem, and how would you show that it is onto?*

::: {.idea}
[Scratch work]

The attempt meets three obstacles, one for each part.

① **Which map.** It is forced: \( 0 \) must go to \( e \), then \( 1 \) to \( s(e) \), then \( 2 \) to \( s(s(e)) \), and so on. But "and so on" is not a definition. @thm-omega-recursion turns it into one, with \( X = M \), starting value \( e \) and step \( x \mapsto s(x) \); it gives existence and uniqueness at once.

② **Onto.** We know nothing about the elements of \( M \) one by one, so we cannot show "each \( x \in M \) is \( s(\dots s(e)) \)" directly. What we have is (P5) for \( M \), which speaks about subsets. So look at the image of \( \varphi \): it contains \( e \) and is closed under \( s \), and (P5) does the rest, by @exm-method-closed-subset.

③ **One-to-one.** Prove "\( \varphi(m) = \varphi(n) \Rightarrow m = n \)" by induction on \( n \). If \( m \) is fixed before the induction, the hypothesis at \( n \) speaks about that one \( m \), while the step needs it at the predecessor of \( m \). So "for every \( m \)" goes inside the property. The base and the step then use (P3) and (P4) for \( M \): a successor is never \( e \), and equal successors have equal predecessors.

For (c), compose: go back from \( M \) to \( \nN \) along \( \varphi^{-1} \), then forward to \( M' \) along \( \varphi' \).

| Givens | Goal |
|---|---|
| \( (M, e, s) \) a Peano system | \( \varphi \colon \nN \to M \), \( \varphi(0) = e \), \( \varphi(\mathrm{S}(n)) = s(\varphi(n)) \), bijective |
| @thm-omega-recursion with \( X = M \), \( a = e \), \( g(n, x) = s(x) \) | (a): such a \( \varphi \) exists, and only one |
| the image \( \varphi(\nN) \) contains \( e \) and is closed under \( s \) | onto, by (P5) for \( M \) |
| \( Q(n) \): for every \( m \), \( \varphi(m) = \varphi(n) \Rightarrow m = n \) | one-to-one: base by (P3), step by (P4) for \( M \) |

*Before reading on: which axiom of \( M \) gives surjectivity, and which give injectivity?*
:::

::: {.proof}
*(a)* Let \( g \colon \nN \times M \to M \) be \( g(n, x) \coloneqq s(x) \), a function because \( s \) is. By @thm-omega-recursion with \( X = M \) and \( a = e \), there is exactly one \( \varphi \colon \nN \to M \) with \( \varphi(0) = e \) and \( \varphi(\mathrm{S}(n)) = g(n, \varphi(n)) = s(\varphi(n)) \) for every \( n \in \nN \).

*(b), onto.* Let \( B \coloneqq \varphi(\nN) \subseteq M \), the image of \( \nN \) under \( \varphi \) (@fd2:def-image). Then \( e = \varphi(0) \in B \). If \( x \in B \), say \( x = \varphi(n) \) with \( n \in \nN \), then \( \mathrm{S}(n) \in \nN \), since \( \mathrm{S} \) maps \( \nN \) into \( \nN \), and \( s(x) = s(\varphi(n)) = \varphi(\mathrm{S}(n)) \in B \). So \( B \) contains \( e \) and is closed under \( s \), and (P5) for \( M \) gives \( B = M \). Hence \( \varphi \) is surjective (@fd2:def-surjective).

*(b), one-to-one.* Let \( Q(n) \) be "for every \( m \in \nN \), if \( \varphi(m) = \varphi(n) \), then \( m = n \)". We prove \( Q(n) \) for every \( n \in \nN \) by @thm-omega-induction (b).

*Base case.* Let \( m \in \nN \) with \( \varphi(m) = \varphi(0) = e \). Suppose \( m \ne 0 \). Then \( m = \mathrm{S}(k) \) for some \( k \in \nN \) (@prp-peano-predecessor (a)), and \( \varphi(m) = s(\varphi(k)) \ne e \) by (P3) for \( M \), a contradiction. So \( m = 0 \).

*Inductive step.* Let \( n \in \nN \) with \( Q(n) \), and let \( m \in \nN \) with \( \varphi(m) = \varphi(\mathrm{S}(n)) = s(\varphi(n)) \). If \( m = 0 \), then \( s(\varphi(n)) = \varphi(0) = e \), against (P3) for \( M \). So \( m \ne 0 \), and \( m = \mathrm{S}(k) \) for some \( k \in \nN \) (@prp-peano-predecessor (a)). Then \( s(\varphi(k)) = \varphi(m) = s(\varphi(n)) \), so \( \varphi(k) = \varphi(n) \) by (P4) for \( M \), and \( k = n \) by \( Q(n) \), applied to \( k \) in the place of \( m \). Hence \( m = \mathrm{S}(k) = \mathrm{S}(n) \), which is \( Q(\mathrm{S}(n)) \).

So \( \varphi \) is injective (@fd2:def-injective), and with the first half it is a bijection (@fd2:def-bijective).

*(c)* Let \( \varphi \colon \nN \to M \) and \( \varphi' \colon \nN \to M' \) be the maps of (a) for the two systems; both are bijections by (b). By @fd2:thm-bijection-iff-inverse, \( \varphi \) has an inverse \( \varphi^{-1} \colon M \to \nN \), and we set \( \psi \coloneqq \varphi' \circ \varphi^{-1} \) (@fd2:def-composition). The two equations \( \varphi \circ \varphi^{-1} = \id_M \) and \( \varphi^{-1} \circ \varphi = \id_\nN \) of @fd2:def-inverse-function also say that \( \varphi \) is an inverse of \( \varphi^{-1} \), so \( \varphi^{-1} \) is a bijection by @fd2:thm-bijection-iff-inverse. Hence \( \psi \) is a bijection as a composite of bijections (@fd2:thm-composition-injective-surjective (c)).

*\( \psi \) has the two properties.* Since \( \varphi(0) = e \), we have \( \varphi^{-1}(e) = 0 \), so \( \psi(e) = \varphi'(0) = e' \). Let \( x \in M \) and \( n \coloneqq \varphi^{-1}(x) \), so \( x = \varphi(n) \). Then \( s(x) = \varphi(\mathrm{S}(n)) \), so \( \varphi^{-1}(s(x)) = \mathrm{S}(n) \), and
\[
\psi\bigl(s(x)\bigr) = \varphi'\bigl(\mathrm{S}(n)\bigr) = s'\bigl(\varphi'(n)\bigr) = s'\bigl(\psi(x)\bigr) .
\]

*Uniqueness.* Let \( \chi \colon M \to M' \) be **any** function with \( \chi(e) = e' \) and \( \chi(s(x)) = s'(\chi(x)) \) for every \( x \in M \). Then \( \chi \circ \varphi \colon \nN \to M' \) satisfies \( (\chi \circ \varphi)(0) = \chi(e) = e' \) and
\[
(\chi \circ \varphi)\bigl(\mathrm{S}(n)\bigr) = \chi\bigl(s(\varphi(n))\bigr) = s'\bigl((\chi \circ \varphi)(n)\bigr)
\]
for every \( n \in \nN \). By the uniqueness in (a), for the system \( M' \), \( \chi \circ \varphi = \varphi' \). So for every \( x \in M \), \( \chi(x) = \chi(\varphi(\varphi^{-1}(x))) = \varphi'(\varphi^{-1}(x)) = \psi(x) \), and \( \chi = \psi \) by @fd2:prp-function-equality. This proves the theorem.
:::

The proof used one pattern three times: a map out of \( \nN \) came from the recursion theorem, two maps out of \( \nN \) were shown equal by the uniqueness half of that theorem, and every property of the map came from an induction or from (P5). It deserves a name.

::: {#exm-method-build-by-recursion}
[Method: build by recursion, compare by induction]

**Template.** (1) To make a map out of \( \nN \), give its value at \( 0 \) and say how the value at \( \mathrm{S}(n) \) comes from the value at \( n \); @thm-omega-recursion builds the map, and only one. (2) To show two maps out of \( \nN \) equal, check that both satisfy the same two equations, and cite the uniqueness. (3) To prove a property of the map (onto, one-to-one, preserving an operation), induct on \( n \), or apply (P5) to its image.

**When to use it.** Maps between Peano systems; operations defined by recursion; recognizing a formula as the map a recursion defines.

**The usual failure.** "And so on" in place of the theorem, entry (N13) of @fd1:exm-not-allowed-catalogue. Citing uniqueness when the equations differ (another start or another step). Fixing \( m \) outside \( Q(n) \), as ③ of the scratch work warned.
:::

The uniqueness in (c) is stronger than stated: no function at all, bijective or not, other than \( \psi \) respects \( e \) and \( s \).

::: {.check}
Functions \( f, g \colon \nN \to \nN \) satisfy \( f(0) = g(0) = 3 \), \( f(n + 1) = f(n) + 2 \) and \( g(n + 1) = g(n) + 2 \) for every \( n \). Which step of @exm-method-build-by-recursion gives \( f = g \)? What is \( f(2) \)?
:::

::: {.solution}
Step (2): both satisfy the equations of @thm-omega-recursion with \( X = \nN \), \( a = 3 \) and step \( h(n, x) = x + 2 \), so they are equal by its uniqueness. From the equations, \( f(1) = 3 + 2 = 5 \) and \( f(2) = 5 + 2 = 7 \).
:::

Step (2) also finds the map of the theorem without computing it. For the Peano system \( (\nN \setminus \{0\}, 1, \mathrm{S}) \) of the first subsection, the map \( n \mapsto \mathrm{S}(n) \) sends \( \nN \) into \( \nN \setminus \{0\} \) by (P3), sends \( 0 \) to \( \mathrm{S}(0) = 1 \), the starting point, and its value \( \mathrm{S}(\mathrm{S}(n)) \) at \( \mathrm{S}(n) \) is the step \( s = \mathrm{S} \) applied to its value \( \mathrm{S}(n) \) at \( n \). By the uniqueness in @thm-peano-categoricity (a), \( \varphi(n) = \mathrm{S}(n) = n + 1 \) (@def-omega-arithmetic (c)). In particular \( \varphi(3) = 4 \); step by step, \( \varphi(0) = 1 \), \( \varphi(1) = \mathrm{S}(1) = 2 \), \( \varphi(2) = 3 \), \( \varphi(3) = 4 \).

::: {.second-reading title="Each axiom has a job"}
Each axiom of \( M \) has a job in (b), and the structures of @exm-peano-axioms-independent show each job failing. These are not Peano systems, so the theorem does not apply to them. But for each of them @thm-omega-recursion, with \( X = M \), \( a = e \) and \( g(n, x) = s(x) \) exactly as in the proof of (a), still gives exactly one \( \varphi \colon \nN \to M \) with \( \varphi(0) = e \) and \( \varphi(\mathrm{S}(n)) = s(\varphi(n)) \).

- In structure (i), \( M = \{0\} \) with \( s(0) = 0 \), which fails (P3) only, \( \varphi \) is the constant map \( 0 \), not injective: \( \varphi(1) = s(\varphi(0)) = 0 = \varphi(0) \).
- In structure (ii), \( M = \{0, 1\} \) with \( s(0) = s(1) = 1 \), which fails (P4) only, \( \varphi(1) = \varphi(2) = 1 \), again not injective.
- In the two copies of \( \nN \), structure (iii), which fail (P5) only, \( \varphi \) is \( n \mapsto (n, a) \) (step (2) of the box: this map sends \( 0 \) to \( e = (0, a) \) and \( (\mathrm{S}(n), a) = s(n, a) \)). It is injective by @fd2:def-ordered-pair, and it misses \( (0, b) \), so it is not onto.
:::

Exercise C2 asks the reverse question for the structure of @exr-peano-properties-c2: is there a map from it to \( \nN \) that respects the two structures?

::: {.check}
Let \( \psi \) be an isomorphism \( (\nN, 0, \mathrm{S}) \to (\nN, 0, \mathrm{S}) \). What is \( \psi(3) \)?
:::

::: {.solution}
\( \psi(3) = 3 \). The identity \( \id_\nN \) is such an isomorphism, and by @thm-peano-categoricity (c) it is the only one, so \( \psi = \id_\nN \).
:::

## Arithmetic and order travel along the isomorphism

An isomorphism matches \( e \) and \( s \). Addition and multiplication on \( \nN \) were built from \( 0 \) and \( \mathrm{S} \) alone, by recursion (@def-omega-arithmetic), and \( < \) can be described by \( + \) (@prp-omega-order-arithmetic (a)). So we expect the matching to carry them across, as long as the other system has operations defined by the same equations.

::: {#prp-isomorphism-preserves-arithmetic}
[Isomorphisms Preserve Arithmetic and Order]

Let \( (M, e, s) \) be a Peano system, and let \( \oplus, \otimes \colon M \times M \to M \) be functions such that, for all \( x, y \in M \),
\[
\begin{aligned}
x \oplus e &= x, & x \oplus s(y) &= s(x \oplus y), \\
x \otimes e &= e, & x \otimes s(y) &= (x \otimes y) \oplus x .
\end{aligned}
\]
Let \( \varphi \colon \nN \to M \) be the bijection of @thm-peano-categoricity. Then for all \( m, n \in \nN \):

::: {.enumerate options="label=(\alph*)"}
1. \( \varphi(m + n) = \varphi(m) \oplus \varphi(n) \);
2. \( \varphi(m n) = \varphi(m) \otimes \varphi(n) \);
3. \( m < n \) if and only if \( \varphi(n) = \varphi(m) \oplus z \) for some \( z \in M \) with \( z \ne e \).
:::
:::

::: {.idea}
For (a) and (b), this is step (3) of @exm-method-build-by-recursion: fix \( m \) and induct on \( n \), the variable the recursions run on. Each side obeys the same two equations, the base from \( 0 \) and the step from \( \mathrm{S} \), and \( \varphi \) turns one set of equations into the other. For (c), translate @prp-omega-order-arithmetic (a), "\( m < n \) iff \( n = m + j \) with \( j \ne 0 \)", through (a), using that \( \varphi \) is a bijection with \( \varphi(0) = e \).
:::

::: {.proof}
*(a)* Fix \( m \in \nN \); we induct on \( n \) (@thm-omega-induction (b)). *Base case:* \( \varphi(m + 0) = \varphi(m) = \varphi(m) \oplus e = \varphi(m) \oplus \varphi(0) \), by @def-omega-arithmetic (a) and the first equation for \( \oplus \). *Step:* if \( \varphi(m + n) = \varphi(m) \oplus \varphi(n) \), then
\[
\begin{aligned}
\varphi\bigl(m + \mathrm{S}(n)\bigr) &= \varphi\bigl(\mathrm{S}(m + n)\bigr) = s\bigl(\varphi(m + n)\bigr) \\
&= s\bigl(\varphi(m) \oplus \varphi(n)\bigr) = \varphi(m) \oplus s\bigl(\varphi(n)\bigr) = \varphi(m) \oplus \varphi\bigl(\mathrm{S}(n)\bigr) ,
\end{aligned}
\]
by @def-omega-arithmetic (a), the equation of \( \varphi \), the hypothesis, the second equation for \( \oplus \), and the equation of \( \varphi \) again.

*(b)* Fix \( m \in \nN \) and induct on \( n \). *Base case:* \( \varphi(m \cdot 0) = \varphi(0) = e = \varphi(m) \otimes e = \varphi(m) \otimes \varphi(0) \), by @def-omega-arithmetic (b) and the first equation for \( \otimes \). *Step:* if \( \varphi(mn) = \varphi(m) \otimes \varphi(n) \), then
\[
\begin{aligned}
\varphi\bigl(m \cdot \mathrm{S}(n)\bigr) &= \varphi(mn + m) = \varphi(mn) \oplus \varphi(m) \\
&= \bigl(\varphi(m) \otimes \varphi(n)\bigr) \oplus \varphi(m) = \varphi(m) \otimes s\bigl(\varphi(n)\bigr) = \varphi(m) \otimes \varphi\bigl(\mathrm{S}(n)\bigr) ,
\end{aligned}
\]
by @def-omega-arithmetic (b), part (a) just proved, the hypothesis, the second equation for \( \otimes \), and the equation of \( \varphi \).

*(c)* By @prp-omega-order-arithmetic (a), \( m < n \) if and only if \( n = m + j \) for some \( j \in \nN \) with \( j \ne 0 \).

\( (\Rightarrow) \) Let \( n = m + j \) with \( j \ne 0 \). By (a), \( \varphi(n) = \varphi(m) \oplus \varphi(j) \). Put \( z \coloneqq \varphi(j) \). Since \( \varphi \) is injective (@thm-peano-categoricity (b)), \( j \ne 0 \) gives \( z \ne \varphi(0) = e \).

\( (\Leftarrow) \) Let \( z \in M \) with \( z \ne e \) and \( \varphi(n) = \varphi(m) \oplus z \). Since \( \varphi \) is onto (@thm-peano-categoricity (b)), \( z = \varphi(j) \) for some \( j \in \nN \), and \( j \ne 0 \) because \( \varphi(0) = e \ne z \). By (a), \( \varphi(n) = \varphi(m) \oplus \varphi(j) = \varphi(m + j) \), so \( n = m + j \) by injectivity. Hence \( m < n \). This proves the proposition.
:::

So once a Peano system carries an addition and a multiplication obeying the recursive equations, \( \varphi \) is an isomorphism for them too, and the order defined from \( \oplus \) as in (c) is carried along as well. Nothing about \( \oplus \) and \( \otimes \) was assumed beyond the four equations.

::: {.check}
For \( (\nN \setminus \{0\}, 1, \mathrm{S}) \) and its map \( \varphi(n) = n + 1 \): \( \varphi(2 + 3) = 6 \), but \( \varphi(2) + \varphi(3) = 3 + 4 = 7 \). Does this contradict @prp-isomorphism-preserves-arithmetic (a)?
:::

::: {.solution}
No. The proposition uses the \( \oplus \) of the target system, not the \( + \) of \( \nN \). That system carries one: \( x \oplus y \coloneqq x + j \) where \( y = \mathrm{S}(j) \) (@prp-peano-predecessor (a)) satisfies \( x \oplus 1 = x \) and \( x \oplus \mathrm{S}(y) = \mathrm{S}(x \oplus y) \) by @def-omega-arithmetic (a). From these equations, \( 3 \oplus 1 = 3 \), \( 3 \oplus 2 = \mathrm{S}(3 \oplus 1) = 4 \), \( 3 \oplus 3 = 5 \) and \( 3 \oplus 4 = 6 \). So \( \varphi(2) \oplus \varphi(3) = 3 \oplus 4 = 6 = \varphi(5) \), as the proposition says.
:::

## Identifying the two sets of natural numbers

Now apply all this to the natural numbers of *Sets and Functions*, Chapter 3. To keep them apart from \( \nN \), write \( \nN_{\nR} \) for them. Two different things are true. Clause (a) below is about \( \nN_{\nR} \), a subset of the familiar real numbers: it is a Peano system, so it is a copy of \( \nN \), and the proof uses the school arithmetic of \( \nR \). Clauses (b) and (c) are about \( \nN \) alone: the principles that *Logic and Proof*, Chapter 4, and *Sets and Functions*, Chapter 3 assumed (induction, recursion, and the arithmetic of @fd2:lem-naturals-arithmetic) are theorems about \( \nN \), proved from @ax-natural-numbers.

::: {#cor-omega-identification}
[Our ℕ and the ℕ of Sets and Functions]

::: {.enumerate options="label=(\alph*)"}
1. **About \( \nN_{\nR} \).** Write \( \nN_{\nR} \subseteq \nR \) for the set of natural numbers as *Sets and Functions*, Section 3.1 describes it, with (\( \nN \)0), (\( \nN \)S) and @fd1:ax-induction. With \( e \coloneqq 0 \) and \( s(n) \coloneqq n + 1 \), it is a Peano system. There is exactly one bijection \( \varphi \colon \nN \to \nN_{\nR} \) with \( \varphi(0) = 0 \) and \( \varphi(\mathrm{S}(n)) = \varphi(n) + 1 \) for every \( n \in \nN \). For all \( m, n \in \nN \) it satisfies
\[
\varphi(m + n) = \varphi(m) + \varphi(n), \qquad \varphi(mn) = \varphi(m)\varphi(n),
\]
and \( m < n \) if and only if \( \varphi(m) < \varphi(n) \); and it sends each numeral of \( \nN \) to the natural number of the same name.
2. **About \( \nN \), proved from @ax-natural-numbers.** The statements of @fd1:ax-induction and @fd2:thm-recursion, read on \( \nN \) with \( n + 1 \coloneqq \mathrm{S}(n) \), are @thm-omega-induction (b) and @thm-omega-recursion. Induction from a base \( b \in \nN \) (@fd2:thm-induction with \( n_0 = b \)) is @prp-omega-order-arithmetic (g).
3. Each clause of @fd2:lem-naturals-arithmetic holds on \( \nN \), with \( n - m \), for \( m \le n \), read as the unique \( j \in \nN \) with \( n = m + j \) of @prp-omega-order-arithmetic (a).
:::
:::

::: {.idea}
For (a), check (P3)–(P5) for \( \nN_{\nR} \) with the tools of *Sets and Functions*, Section 3.1, and the equations of @prp-isomorphism-preserves-arithmetic with school arithmetic; then @thm-peano-categoricity and that proposition do the rest. Parts (b) and (c) are a matter of reading statements side by side and pointing to the label that proves each one on \( \nN \).

*Before reading on: which clause do the later chapters actually use, when they build \( \nZ \), \( \nQ \) and \( \nR \)?*
:::

::: {.proof}
*(a)* The map \( s \) sends \( \nN_{\nR} \) into \( \nN_{\nR} \) by (\( \nN \)S). (P3): for \( n \in \nN_{\nR} \), \( n \ge 0 \) by @fd2:lem-naturals-arithmetic (a), so \( n + 1 \ge 1 > 0 \) and \( n + 1 \ne 0 \). (P4): \( m + 1 = n + 1 \) gives \( m = n \), by subtracting \( 1 \) in \( \nR \). (P5): a subset of \( \nN_{\nR} \) that contains \( 0 \) and is closed under \( n \mapsto n + 1 \) is \( \nN_{\nR} \); this is the set form of @fd1:ax-induction, the remark at the start of *Sets and Functions*, Section 3.1. So \( (\nN_{\nR}, 0, s) \) is a Peano system (@def-peano-system), and @thm-peano-categoricity (a), (b) give exactly one \( \varphi \) as stated, and it is a bijection.

For the operations, take \( \oplus \) and \( \otimes \) to be the addition and multiplication of \( \nN_{\nR} \); they are functions \( \nN_{\nR} \times \nN_{\nR} \to \nN_{\nR} \) by @fd2:lem-naturals-arithmetic (b). The four equations of @prp-isomorphism-preserves-arithmetic read \( x + 0 = x \), \( x + (y + 1) = (x + y) + 1 \), \( x \cdot 0 = 0 \) and \( x(y + 1) = xy + x \), which hold in \( \nR \). That proposition gives \( \varphi(m + n) = \varphi(m) + \varphi(n) \) and \( \varphi(mn) = \varphi(m)\varphi(n) \).

For the order we first show: for \( x, y \in \nN_{\nR} \), \( x < y \) if and only if \( y = x + z \) for some \( z \in \nN_{\nR} \) with \( z \ne 0 \). If \( x < y \), then \( z \coloneqq y - x \in \nN_{\nR} \) by @fd2:lem-naturals-arithmetic (d), and \( z \ne 0 \) since \( y \ne x \). Conversely, \( z \ne 0 \) gives \( z \ge 1 > 0 \) by @fd2:lem-naturals-arithmetic (a), so \( y = x + z > x \). Now @prp-isomorphism-preserves-arithmetic (c), with \( e = 0 \), says that \( m < n \) if and only if \( \varphi(n) = \varphi(m) + z \) for some \( z \in \nN_{\nR} \) with \( z \ne 0 \), that is, if and only if \( \varphi(m) < \varphi(n) \).

Finally, \( \varphi(0) = 0 \), and each numeral of \( \nN \) is the successor of the one before (@def-omega-arithmetic (c)), so \( \varphi(1) = \varphi(\mathrm{S}(0)) = 0 + 1 = 1 \), \( \varphi(2) = \varphi(\mathrm{S}(1)) = 1 + 1 = 2 \), and so on, one step for each numeral written.

*(b)* By @def-omega-arithmetic (c), \( n + 1 = \mathrm{S}(n) \) for every \( n \in \nN \). So, read on \( \nN \), the statement of @fd1:ax-induction becomes @thm-omega-induction (b), and the statement of @fd2:thm-recursion is word for word @thm-omega-recursion. Induction from a base \( b \in \nN \) is @prp-omega-order-arithmetic (g).

*(c)* We take the clauses of @fd2:lem-naturals-arithmetic in turn, for \( m, n \in \nN \).

- (a) "\( n \ge 0 \); if \( n \ne 0 \), then \( n \ge 1 \)" is @thm-omega-order (d).
- (b) "\( m + n \in \nN \) and \( mn \in \nN \)" holds because \( + \) and \( \cdot \) are functions \( \nN \times \nN \to \nN \) (@def-omega-arithmetic).
- (c) If \( n \ne 0 \), then \( 1 \le n \) by @thm-omega-order (d), so \( n = 1 + j \) for exactly one \( j \in \nN \) by @prp-omega-order-arithmetic (a); this \( j \) is \( n - 1 \), and it lies in \( \nN \).
- (d) If \( m \le n \), then \( n - m \in \nN \) by @prp-omega-order-arithmetic (a).
- (e) No \( k \in \nN \) has \( n < k < \mathrm{S}(n) \), by @thm-omega-order (b). For the second form, let \( m < n \). By trichotomy (@thm-omega-order (a)), \( \mathrm{S}(m) < n \), \( \mathrm{S}(m) = n \) or \( n < \mathrm{S}(m) \). The last gives \( n \le m \) by @thm-omega-order (b), and then \( n \le m < n \) gives \( n < n \) by transitivity, which (a) of that theorem rules out. So \( m + 1 = \mathrm{S}(m) \le n \).

This proves the corollary.
:::

Clause (a) is the honest sense in which the choice of Peano system does not matter: \( \nN \) and \( \nN_{\nR} \) are copies of each other by a unique isomorphism, which also matches \( + \), \( \cdot \) and \( < \). But (a) is a theorem about \( \nN_{\nR} \), and its proof used the school arithmetic of \( \nR \) (in (P3), (P4), the four equations, the step describing \( < \) by \( + \), and the numerals). The answer to the prompt is therefore (b), with (c): when a later chapter applies induction or recursion to \( \nN \), it uses a theorem proved here from @ax-natural-numbers, and \( \nR \) never enters.

::: {.warning}
**The isomorphism carries \( 0 \), the successor, \( + \), \( \cdot \) and \( < \), nothing else.** In \( \nN_{\nR} \), \( 3 - 5 \) and \( 3/5 \) are real numbers; in \( \nN \) neither exists until Chapters 2 and 3 build them. In the construction from sets of Section 1.5, \( 2 \in 3 \) is true; in \( \nN_{\nR} \) it means nothing. No later theorem asks such questions.
:::

## How later chapters cite *Logic and Proof* and *Sets and Functions*

In the rest of this volume, \( \nN \) is the Peano system of @ax-natural-numbers, with the \( 0 \), \( + \), \( \cdot \) and \( < \) of this chapter. The later chapters build \( \nZ \), \( \nQ \) and \( \nR \) from it, and they cite results of *Logic and Proof*, Chapter 4, and *Sets and Functions*, Chapters 3 and 4 about natural numbers. Those proofs used the arithmetic of the real numbers freely (*Sets and Functions*, Chapter 3 takes the arithmetic and order of \( \nR \) as school facts, and @fd2:thm-binary-sequences-uncountable, for example, uses \( 1 - b \)), so they cannot be moved to \( \nN \) word for word. The **citing rule** is this: each fact about natural numbers such a proof uses is read through its counterpart proved in this chapter, namely @cor-omega-identification (b) and (c) for induction, recursion and @fd2:lem-naturals-arithmetic, @thm-omega-well-ordering for @fd2:thm-well-ordering, @thm-omega-arithmetic-laws, @thm-omega-order and @prp-omega-order-arithmetic for the rest of school arithmetic and order (closure, cancellation, trichotomy, \( n - m \) for \( m \le n \)), and @prp-omega-powers-parity for powers and parity. Read this way, the results that later chapters cite fall into three groups, which later chapters refer to by number: (i) results that run on \( \nN \) through the citing rule, the facts about finite and countable sets, citable anywhere; (ii) results that also need @prp-omega-powers-parity and the cancellation of @prp-omega-order-arithmetic (b), (f), citable only in review exercises; (iii) templates used later over an ordered field. The fold lists each group in full.

::: {.second-reading title="The three groups in full"}
(i) **Results that run on \( \nN \) through the citing rule above.** These are @fd2:prp-finite-max (for its \( \nN \) side, which is @fd2:thm-induction with base \( 1 \) and @fd2:lem-naturals-arithmetic (e)), @fd2:def-finite, @fd2:def-infinite, @fd2:cor-pigeonhole-finite-sets, @fd2:thm-finite-no-proper-copy, @fd2:lem-subsets-of-naturals, @fd2:thm-countable-characterizations, @fd2:prp-countable-subset, @fd2:prp-countable-image and @fd2:thm-binary-sequences-uncountable (where \( \{0, 1\}^{\nN} \) is indexed by \( \nN \), and \( 1 - b \) on \( \{0, 1\} \) is read by @prp-omega-order-arithmetic (a)), and @fd2:exr-finite-sets-c2 (a), cited later only from an exercise solution (its \( \nN \) side is an induction on \( m \), read by @cor-omega-identification (b), \( mn \in \nN \), read by @cor-omega-identification (c), and \( 0 = 0 \cdot n \) and \( mn + n = (m + 1)n \), read by @thm-omega-arithmetic-laws (e)). Running a result on \( \nN \) includes the results its proof cites: @fd2:thm-pigeonhole, @fd2:prp-disjoint-union-count, @fd2:prp-subset-finite, @fd2:cor-finite-size-unique, @fd2:cor-remove-point and the count "\( \{0, \dots, x\} \) has \( x + 1 \) elements" in the examples after @fd2:def-finite run through the same citing rule, and they belong to group (i) themselves. A later chapter may cite the results of group (i) anywhere.

(ii) **Results that use school facts, and need @prp-omega-powers-parity on \( \nN \).** These are @fd2:thm-product-countable (powers by @fd2:def-power and @fd2:prp-power-laws (a), (d), (e) over the school \( \nR \), parity through @fd2:thm-division-algorithm on the school \( \nZ \), and cancellation in \( \nR \)), @fd2:prp-union-two-countable (parity through @fd2:thm-division-algorithm), and through them @fd2:cor-product-countable (a). On \( \nN \), the powers are read as @prp-omega-powers-parity (a)–(c), the parity claim as its (d), and cancellation as @prp-omega-order-arithmetic (b), (f); with that, each of these proofs runs on \( \nN \). A later chapter may cite them only in a review (R) exercise; anywhere else, a construction that needs one of them proves it on \( \nN \) first. Part (b) of @fd2:cor-product-countable is not in this group and is not checked on \( \nN \) here: *Sets and Functions*, Chapter 4 treats its list \( A_1, \dots, A_k \) as a family in the everyday sense of @fd2:def-indexed-family, with no set holding it, and such families are left to *Axiomatic Set Theory*. A later chapter that needs (b) proves it on \( \nN \) first. @fd2:thm-integers-rationals-countable is a statement about the school \( \nZ \) and \( \nQ \), and is never applied to \( \nN \).

(iii) **Templates.** @fd2:def-sum-product and @fd2:prp-power-laws are used later only as patterns, with the school \( \nR \) replaced by an ordered field \( F \). Their \( \nN \) side is read through the citing rule above, and their field side is proved again from the axioms of \( F \). The parts that need \( \nZ \) (@fd2:prp-power-laws (d) for an integer base, and the general index of @fd2:def-sum-product, which uses @fd2:prp-integers-closed) are not part of the pattern.
:::

So everything that *Logic and Proof*, Chapter 4, and *Sets and Functions*, Chapter 3 assumed about natural numbers (that \( 0 \) is one, that \( n + 1 \) is one whenever \( n \) is, induction, recursion, and the arithmetic of @fd2:lem-naturals-arithmetic) is now proved from the one assumption @ax-natural-numbers. Section 1.5 says where a Peano system comes from, and Chapter 2 builds \( \nZ \) from \( \nN \), with pairs and classes of pairs.

## Exercises

### A. Check your understanding

::: {#exr-categoricity-a1}
[A1]

These questions are about the proof of @thm-peano-categoricity.

::: {.enumerate options="label=(\alph*)"}
1. Where in the proof is (P5) for \( M \) used, and where are (P3) and (P4) for \( M \) used?
2. Where is (P4) for \( \nN \) used? (It is not visible in the proof itself.)
3. Run \( \varphi \) of part (a) for the system \( (\nN \setminus \{0\}, 1, \mathrm{S}) \) on \( 0 \), \( 1 \) and \( 2 \), from the two equations alone.
4. State the idea of the proof of (a) and (b) in two sentences.
:::
:::

::: {.solution}
(a) (P5) for \( M \) is used once, for surjectivity: the image \( \varphi(\nN) \) contains \( e \) and is closed under \( s \), so it is \( M \). (P3) for \( M \) is used for injectivity, in the base case (\( \varphi(\mathrm{S}(k)) = s(\varphi(k)) \ne e \), so only \( m = 0 \) has \( \varphi(m) = e \)) and at the start of the inductive step (to exclude \( m = 0 \)). (P4) for \( M \) is used in the inductive step, to pass from \( s(\varphi(k)) = s(\varphi(n)) \) to \( \varphi(k) = \varphi(n) \).

(b) Inside @thm-omega-recursion: in its claim's step, a pair stepping to first coordinate \( \mathrm{S}(n) \) has first coordinate \( n \), by (P4) for \( \nN \).

(c) \( \varphi(0) = 1 \); \( \varphi(1) = \varphi(\mathrm{S}(0)) = \mathrm{S}(\varphi(0)) = \mathrm{S}(1) = 2 \); \( \varphi(2) = \varphi(\mathrm{S}(1)) = \mathrm{S}(2) = 3 \).

(d) The map is forced at \( 0 \) and at each successor, so the recursion theorem builds it and makes it unique. It is onto because its image contains \( e \) and is closed under \( s \), so (P5) for \( M \) applies; it is one-to-one by an induction whose base and step are (P3) and (P4) for \( M \).
:::

### B. Practice

::: {#exr-categoricity-b1}
[B1: The even numbers]

Let \( E \coloneqq \{ 2n : n \in \nN \} \), with \( e \coloneqq 0 \) and \( s(x) \coloneqq x + 2 \) for \( x \in E \). Show that \( (E, 0, s) \) is a Peano system, and that the map \( \varphi \) of @thm-peano-categoricity is \( \varphi(n) = 2n \).
:::

::: {.solution}
Here \( E = \{ x \in \nN : x = 2n \text{ for some } n \in \nN \} \). By @def-omega-arithmetic (b), \( 2 \cdot \mathrm{S}(n) = 2n + 2 \) for every \( n \in \nN \). So \( s \) maps \( E \) into \( E \): \( s(2n) = 2n + 2 = 2 \cdot \mathrm{S}(n) \in E \).

(P3): \( 2n + 2 = 2n + \mathrm{S}(1) = \mathrm{S}(2n + 1) \) by @def-omega-arithmetic (a), and a successor is never \( 0 \) ((P3) for \( \nN \)). (P4): if \( x + 2 = y + 2 \), then \( x = y \) by @prp-omega-order-arithmetic (b). (P5): let \( A \subseteq E \) with \( 0 \in A \) and \( x + 2 \in A \) for every \( x \in A \). Let \( B \coloneqq \{ n \in \nN : 2n \in A \} \). Then \( 0 \in B \), since \( 2 \cdot 0 = 0 \in A \); and if \( n \in B \), then \( 2 \cdot \mathrm{S}(n) = 2n + 2 \in A \), so \( \mathrm{S}(n) \in B \). By @thm-omega-induction (a), \( B = \nN \), so every \( 2n \) lies in \( A \), and \( A = E \).

The map \( n \mapsto 2n \) from \( \nN \) to \( E \) sends \( 0 \) to \( 2 \cdot 0 = 0 = e \), and \( 2 \cdot \mathrm{S}(n) = 2n + 2 = s(2n) \). By the uniqueness in @thm-peano-categoricity (a), it is \( \varphi \). In particular, by (b) of that theorem, \( n \mapsto 2n \) is a bijection \( \nN \to E \).
:::

::: {#exr-categoricity-b2}
[B2: The identification at work]

Let \( \varphi \colon \nN \to \nN_{\nR} \) be the bijection of @cor-omega-identification (a).

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \varphi(3) \) step by step from the two equations of \( \varphi \).
2. Compute \( \varphi(2 \cdot 3) \) in two ways: from (a) of the corollary, and by unwinding \( 2 \cdot 3 \) in \( \nN \) to a numeral first.
:::
:::

::: {.solution}
(a) Using \( \varphi(0) = 0 \) and \( \varphi(\mathrm{S}(n)) = \varphi(n) + 1 \), with \( 3 = \mathrm{S}(2) \), \( 2 = \mathrm{S}(1) \), \( 1 = \mathrm{S}(0) \) (@def-omega-arithmetic (c)):
\[
\varphi(3) = \varphi(2) + 1 = \bigl(\varphi(1) + 1\bigr) + 1 = \bigl((0 + 1) + 1\bigr) + 1 = 3 .
\]

(b) By the corollary, \( \varphi(2 \cdot 3) = \varphi(2)\varphi(3) = 2 \cdot 3 = 6 \) in \( \nN_{\nR} \), where \( \varphi(2) = 2 \) as in (a). In \( \nN \), \( 2 \cdot 3 = 2 \cdot 2 + 2 = (2 \cdot 1 + 2) + 2 = ((2 \cdot 0 + 2) + 2) + 2 = 6 \), by @def-omega-arithmetic (b) three times and then \( 2 \cdot 0 = 0 \), \( 0 + 2 = 2 \), \( 2 + 2 = 4 \), \( 4 + 2 = 6 \) from the equations for \( + \). Then \( \varphi(6) = 6 \) by six steps as in (a). The two answers agree, as the corollary says they must.
:::

::: {#exr-categoricity-b3}
[B3: Prove or disprove]

Prove each true statement by @exm-method-build-by-recursion, and refute each false one with a counterexample.

::: {.enumerate options="label=(\alph*)"}
1. Exactly one function \( f \colon \nN \to \nN \) has \( f(0) = 1 \) and \( f(n + 1) = 2 f(n) \) for every \( n \).
2. Exactly one function \( f \colon \nN \to \nN \) has \( f(0) = 0 \) and \( f(n + 1) = f(n) + 2n + 1 \) for every \( n \), and it is \( f(n) = n \cdot n \).
3. Some injective function \( f \colon \nN \to \nN \) has \( f(n + 1) = f(n) \) for every \( n \).
4. If \( f, g \colon \nN \to \nN \) satisfy \( f(0) = g(0) \), \( f(n + 1) = f(n) + n \) and \( g(n + 1) = g(n) + n \) for every \( n \), then \( f = g \).
5. Every bijection \( \psi \colon \nN \to \nN \) with \( \psi(0) = 0 \) is an isomorphism \( (\nN, 0, \mathrm{S}) \to (\nN, 0, \mathrm{S}) \).
:::
:::

::: {.solution}
(a) **True.** Step (1) of the box: @thm-omega-recursion with \( X = \nN \), \( a = 1 \) and \( g(n, x) = 2x \) gives exactly one such \( f \).

(b) **True.** @thm-omega-recursion with \( X = \nN \), \( a = 0 \) and \( g(n, x) = x + 2n + 1 \) gives exactly one such \( f \). The map \( n \mapsto n \cdot n \) satisfies both equations: \( 0 \cdot 0 = 0 \), and
\[
\begin{aligned}
(n + 1)(n + 1) &= (n + 1) n + (n + 1) = (n \cdot n + n) + (n + 1) \\
&= \bigl(n \cdot n + (n + n)\bigr) + 1 = (n \cdot n + 2n) + 1 ,
\end{aligned}
\]
by @def-omega-arithmetic (b), @thm-omega-arithmetic-laws (e), associativity (c) three times, and \( 2n = (1 + 1)n = 1 \cdot n + n = n + n \) by (e). So it is \( f \), by step (2) of the box.

(c) **False.** For any such \( f \), \( f(1) = f(0) \) with \( 1 \ne 0 \), so \( f \) is not injective.

(d) **True.** Both satisfy the equations of @thm-omega-recursion with \( X = \nN \), \( a = f(0) \) and step \( h(n, x) = x + n \); by its uniqueness (step (2) of the box), \( f = g \).

(e) **False.** The bijection \( \tau \) of the first warning exchanges \( 1 \) and \( 2 \) and has \( \tau(0) = 0 \), but \( \tau(\mathrm{S}(0)) = 2 \ne 1 = \mathrm{S}(\tau(0)) \).
:::

### C. Going deeper

::: {#exr-categoricity-c1}
[C1: Writing out categoricity]

Without looking at the text, prove part (b) of @thm-peano-categoricity: for a Peano system \( (M, e, s) \), the map \( \varphi \colon \nN \to M \) with \( \varphi(0) = e \) and \( \varphi(\mathrm{S}(n)) = s(\varphi(n)) \) is a bijection.
:::

::: {.solution}
[Hint 1]

For surjectivity, use (P5) for \( M \) on a set built from \( \varphi \). For injectivity, induct on \( n \); decide first where "for every \( m \)" goes.
:::

::: {.solution}
[Hint 2]

The induction for injectivity starts: "Let \( Q(n) \) be: for every \( m \in \nN \), \( \varphi(m) = \varphi(n) \) implies \( m = n \)."
:::

::: {.solution}
*Onto.* The image \( B \coloneqq \varphi(\nN) \) (@fd2:def-image) contains \( e = \varphi(0) \), and \( x = \varphi(n) \in B \) gives \( s(x) = \varphi(\mathrm{S}(n)) \in B \). By (P5) for \( M \), \( B = M \).

*One-to-one.* By @thm-omega-induction (b) we prove, for every \( n \), \( Q(n) \): "for every \( m \in \nN \), \( \varphi(m) = \varphi(n) \) implies \( m = n \)". For \( Q(0) \), let \( \varphi(m) = e \); an \( m \ne 0 \) is \( \mathrm{S}(k) \) (@prp-peano-predecessor (a)), with \( \varphi(m) = s(\varphi(k)) \ne e \) by (P3) for \( M \); so \( m = 0 \). For the step, assume \( Q(n) \) and \( \varphi(m) = s(\varphi(n)) \). Then \( m \ne 0 \), as \( e \) is not a value of \( s \) (P3 for \( M \)); so \( m = \mathrm{S}(k) \), and \( s(\varphi(k)) = s(\varphi(n)) \) gives \( \varphi(k) = \varphi(n) \) by (P4) for \( M \), hence \( k = n \) by \( Q(n) \) used at \( k \), and \( m = \mathrm{S}(n) \). So \( \varphi \) is injective, and a bijection.

**Marking scheme.** (10 points)
- 3: surjectivity: shows the image of \( \varphi \) contains \( e \) and is closed under \( s \), and cites (P5) for \( M \).
- 2: sets up an induction (on either variable, or by least counterexample) whose hypothesis is strong enough to use at the predecessor, e.g. \( Q(n) \) with "for every \( m \)" inside, or the difference \( j \ne 0 \) fixed and induction on \( m \).
- 2: base case, via \( m = \mathrm{S}(k) \) for \( m \ne 0 \) and (P3) for \( M \).
- 3: inductive step, using (P3) for \( M \) to get \( m \ne 0 \), (P4) for \( M \) to cancel \( s \), and the induction hypothesis at the predecessor \( k \).
Fatal errors (0 for the part concerned): an induction whose hypothesis is then applied at a value it does not cover (typically: \( m \) fixed outside \( Q \), then used at \( k \)); using injectivity of \( \varphi \) to prove injectivity; using (P3), (P4) or (P5) **for \( \nN \)** where the axiom for \( M \) is needed. A proof of injectivity by @thm-omega-well-ordering (a least \( n \) with some \( m \ne n \), \( \varphi(m) = \varphi(n) \)) earns the same 7 points, mapped to base, step and hypothesis in the same way. So does the fixed-difference route (reducing to \( \varphi(m + j) \ne \varphi(m) \) for \( j \ne 0 \) by @thm-omega-order (a) and @prp-omega-order-arithmetic (a), and inducting on \( m \)): its base uses (P3) for \( M \), its step (P4) for \( M \) and the hypothesis at \( m \), and the points are mapped in the same way.
:::

::: {#exr-categoricity-c2}
[C2: Without induction, no recursion]

Let \( (M, e, s) \) be the structure of @exr-peano-properties-c2: \( M = \nN \times \{a, b, c\} \), \( e = (0, a) \), \( s(n, a) = (\mathrm{S}(n), a) \), \( s(n, b) = (\mathrm{S}(n), b) \), \( s(0, c) = (0, b) \) and \( s(\mathrm{S}(k), c) = (k, c) \). Show that there is **no** function \( f \colon M \to \nN \) with \( f(e) = 0 \) and \( f(s(x)) = \mathrm{S}(f(x)) \) for every \( x \in M \). Which Peano axiom, missing in \( M \), is responsible?
:::

::: {.solution}
Suppose such an \( f \) exists. For every \( k \in \nN \), \( s(\mathrm{S}(k), c) = (k, c) \), so
\[
f\bigl((k, c)\bigr) = \mathrm{S}\Bigl(f\bigl((\mathrm{S}(k), c)\bigr)\Bigr) .
\]
Let \( T \coloneqq \{ f((k, c)) : k \in \nN \} \subseteq \nN \); it is non-empty, since it contains \( f((0, c)) \). By @thm-omega-well-ordering, \( T \) has a least element \( t = f((k_0, c)) \). But \( u \coloneqq f((\mathrm{S}(k_0), c)) \in T \), and \( t = \mathrm{S}(u) = u + 1 \), so \( u < t \) (@prp-omega-order-arithmetic (a)). This contradicts the leastness of \( t \), since \( t \le u \) and \( u < t \) would give \( u < u \) (@thm-omega-order (a)). So no such \( f \) exists. (The condition \( f(e) = 0 \) was not even used: no map at all turns \( s \) into \( \mathrm{S} \).)

\( M \) satisfies (P3) and (P4) and fails only (P5) (@exr-peano-properties-c2 (b), (d)). So (P5) is what makes the recursion theorem possible: the downward chain \( (0, c), (1, c), (2, c), \dots \), each element the successor of the next, would need values in \( \nN \) that decrease forever.
:::

<!-- dependency ledger
thm-peano-categoricity (claim): (opening subsection) (N \ {0}, 1, S) is a Peano system | inline (three lines; exr-peano-properties-c1 asks the same, not relied on)
thm-peano-categoricity (proof): every m in N is 0 or not 0 (case split before prp-peano-predecessor (a)) | classical case split (excluded middle), standing in F1-F2
thm-peano-categoricity (proof): g(n, x) = s(x) is a function N x M -> M | inline (s is a function; fd2 def-function, def-cartesian-product)
thm-peano-categoricity (proof): S(n) in N for n in N | def-peano-system (s maps M into M), for N by ax-natural-numbers
thm-peano-categoricity (proof): phi(0) = e gives phi^{-1}(e) = 0, and x = phi(phi^{-1}(x)) | def-inverse-function, through thm-bijection-iff-inverse (cited)
thm-peano-categoricity (proof): phi^{-1} is a bijection (phi is an inverse of it) | def-inverse-function, thm-bijection-iff-inverse (cited)
thm-peano-categoricity (claim): (Quick check after exm-method-build-by-recursion) f(1) = 5, f(2) = 7 | def-omega-arithmetic (a), (c): 3 + 2 = 5, 5 + 2 = 7; verify/ch01/thm-peano-categoricity.py
thm-peano-categoricity (example): (worked example after the Quick check) n -> S(n) maps N into N \ {0}; phi(n) = n + 1; phi(3) = 4 | (P3) for N; uniqueness in (a); def-omega-arithmetic (c) (cited); verify/ch01/thm-peano-categoricity.py
thm-peano-categoricity (claim): (list after the worked example) phi(1) = phi(0) in {0}; phi(1) = phi(2) = 1 in {0, 1} | inline (two steps of the recursion each); verify/ch01/thm-peano-categoricity.py
thm-peano-categoricity (claim): (list) two copies of N: phi(n) = (n, a), injective, (0, b) not of that form | step (2) of exm-method-build-by-recursion (uniqueness in thm-omega-recursion); fd2 def-ordered-pair with a != b (cited); verify/ch01/thm-peano-categoricity.py
thm-peano-categoricity (claim): (Quick check) id_N is an isomorphism (N, 0, S) -> (N, 0, S) | inline (id_N(0) = 0, id_N(S(n)) = S(id_N(n)))
prp-isomorphism-preserves-arithmetic (claim): (Quick check) in (N \ {0}, 1, S): 3 (+) 1 = 3, 3 (+) 2 = 4, 3 (+) 3 = 5, 3 (+) 4 = 6 = phi(5); phi(2) + phi(3) = 7 | inline from the equations for (+); verify/ch01/prp-isomorphism-preserves-arithmetic.py
cor-omega-identification (proof): real arithmetic for (a): subtracting 1 (P4); n + 1 >= 1 > 0; x + 0 = x, x + (y + 1) = (x + y) + 1, x 0 = 0, x(y + 1) = xy + x; y = x + z > x for z > 0; 0 + 1 = 1 and k + 1 is the next numeral (numerals) | school fact (fd2's standing description of N, F2.2 §01), used only in (a)
cor-omega-identification (proof): (P5) for N_R | the remark at the start of F2.2 §01 (unlabeled; set form of ax-induction, cited)
cor-omega-identification (proof): n <= m < n gives n < n, in (c)(e) | thm-omega-order (a) (transitivity, irreflexivity), cited
cor-omega-identification (claim): (warning) 3 - 5 and 3/5 do not exist in N; 2 in 3 holds in the construction of F3.1 §05 | prp-omega-order-arithmetic (a) (n - m only for m <= n); prose pointer to F3.1 §05 (no @ref; nothing depends on it)
cor-omega-identification (claim): (citing rule, fold group (ii)) cor-product-countable (b) is not checked on N here: F2.3 treats its list as an informal family with no ambient set, left to Axiomatic Set Theory | stated; nothing depends on it
cor-omega-identification (claim): (citing rule, groups (i)-(iii)) which fd2 facts about N each listed proof uses | meta-claim of blueprint ch09.md section 07 (carried into recut-ch01.md §3.4 item 7), checked label by label at S2; S8 re-verifies
cor-omega-identification (claim): (citing rule, group (i)) exr-finite-sets-c2 (a) and cor-remove-point run on N: induction on m, mn in N, 0 = 0 n, mn + n = (m + 1)n; cor-remove-point through prp-subset-finite, prp-disjoint-union-count, cor-finite-size-unique and k + 1 = n + 1 => k = n | checked against the proofs of exr-finite-sets-c2 (a) and cor-remove-point in F2.3 §01 (cor-omega-identification (b), (c); thm-omega-arithmetic-laws (e); cancellation by prp-omega-order-arithmetic (b))
exr-categoricity-b1 (solution): 2 = S(1), so 2n + 2 = S(2n + 1) | def-omega-arithmetic (a), (c), cited; verify/ch01/exr-categoricity-b1.py
exr-categoricity-b2 (solution): 2 * 3 = 6, 0 + 2 = 2, 2 + 2 = 4, 4 + 2 = 6 from the defining equations; 2 * 3 = 6 in N_R | inline; school fact in N_R; verify/ch01/exr-categoricity-b2.py
exr-categoricity-b3 (solution): (n + 1)(n + 1) = n n + 2n + 1 and 2n = n + n | def-omega-arithmetic (b), thm-omega-arithmetic-laws (c), (e), cited; verify/ch01/exr-categoricity-b3.py
exr-categoricity-b3 (solution): (c) 1 != 0 | (P3) for N (1 = S(0))
exr-categoricity-c2 (solution): t = S(u) = u + 1 | def-omega-arithmetic (c)
exr-categoricity-c2 (solution): T is a set | fd2 def-set-builder (image of k -> f((k, c)) inside N)
-->
