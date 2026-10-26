# The Recursion Theorem; Addition and Multiplication

The natural numbers now have a zero, a successor map and induction (@thm-omega-induction), and nothing else: no addition, no multiplication. *Sets and Functions*, Section 3.3 had the same need and met it with @fd2:thm-recursion, a theorem that turns two equations into a function. Its proof built partial solutions on the sets \( \{0, \dots, n\} \) and compared them using the order of the real numbers. The natural numbers of @ax-natural-numbers have no order yet; the order is defined in the next section, from the addition of this one. So this section proves the recursion theorem by a construction that needs no order at all: it takes the smallest set of pairs that the two equations force, and shows that this set is the graph of a function. Then it defines addition and multiplication as school does, and proves the laws of arithmetic by one move and its consequences.

## Recursion on ℕ

*A starting value and a rule for the next value determine exactly one function on \( \nN \).*

::: {#thm-omega-recursion}
[Recursion Theorem on \( \nN \)]

Let \( X \) be a set, let \( a \in X \), and let \( g \colon \nN \times X \to X \) be a function. Then there is **exactly one** function \( f \colon \nN \to X \) such that
\[
f(0) = a \quad \text{and} \quad f\bigl(\mathrm{S}(n)\bigr) = g\bigl(n, f(n)\bigr) \ \text{ for every } n \in \nN .
\]
:::

This is the statement of @fd2:thm-recursion, with \( \nN \) the Peano system of @ax-natural-numbers and \( \mathrm{S}(n) \) in place of \( n + 1 \). The set \( \nN \times X \) is the Cartesian product of @fd2:def-cartesian-product. As before, \( a \) is the starting value and \( g \) turns the stage \( n \) and the current value into the next value; the conclusion has an existence half and a uniqueness half.

::: {.idea}
[Scratch work]

Uniqueness will be an induction: two solutions agree at \( 0 \), and the second equation passes agreement from \( n \) to \( \mathrm{S}(n) \). Existence is the hard half. "Define \( f \) by the two equations" names \( f \) on both sides of the second one, so it is not yet a definition. A definition must produce an object, and the object a function is made of is its graph (@fd2:def-function). So ask what the graph must contain. It must contain the pair \( (0, a) \). Whenever it contains a pair \( (n, x) \), meaning \( f(n) = x \), it must also contain \( (\mathrm{S}(n), g(n, x)) \).

That is a description of a closed set: in \( \nN \times X \), take the starting element \( (0, a) \) and the step \( (n, x) \mapsto (\mathrm{S}(n), g(n, x)) \), which maps \( \nN \times X \) into itself because \( g \) takes its values in \( X \). By @fd2:prp-smallest-closed-set there is a smallest closed subset; call it \( R \). It contains exactly what the equations force and nothing more. The question is whether \( R \) is a graph: does each \( n \) have exactly one partner \( x \) with \( (n, x) \in R \)?

| Givens | Goal |
|---|---|
| \( R \) is the smallest closed subset of \( \nN \times X \) | each \( n \) has exactly one \( x \) with \( (n, x) \in R \) |
| induction on \( n \) | base: the only pair at \( 0 \) is \( (0, a) \); step: the only pair at \( \mathrm{S}(n) \) is \( (\mathrm{S}(n), g(n, x_n)) \), where \( x_n \) is the partner of \( n \) |
| an extra pair \( (n, y) \in R \) | \( R \setminus \{(n, y)\} \) is still closed, against "smallest" |

The last row is the gap the proof closes. A smallest closed set has no spare elements: if one pair could be removed without breaking closure, the smaller set would be closed, and \( R \) would lie inside it. Removing a pair is safe only if no step produces it from a pair that stays. That is where (P3) and (P4) enter.

*Before reading on: where is each of them used?*
:::

::: {.proof}
**Step 1 (uniqueness).** Let \( f, f' \colon \nN \to X \) both satisfy the two equations, and let \( P(n) \) be "\( f(n) = f'(n) \)". \( P(0) \) holds, since \( f(0) = a = f'(0) \). If \( P(n) \) holds, then
\[
f\bigl(\mathrm{S}(n)\bigr) = g\bigl(n, f(n)\bigr) = g\bigl(n, f'(n)\bigr) = f'\bigl(\mathrm{S}(n)\bigr) ,
\]
so \( P(\mathrm{S}(n)) \) holds. By @thm-omega-induction (b), \( P(n) \) holds for every \( n \in \nN \). The two functions have the same domain and codomain, so \( f = f' \) by @fd2:prp-function-equality.

**Step 2 (the set of pairs).** Call a subset \( C \subseteq \nN \times X \) *closed* if \( (0, a) \in C \) and \( (\mathrm{S}(n), g(n, x)) \in C \) for every \( (n, x) \in C \). The step sends \( \nN \times X \) into itself, since \( \mathrm{S}(n) \in \nN \) and \( g(n, x) \in X \). By @fd2:prp-smallest-closed-set there is a closed set \( R \subseteq \nN \times X \) that lies inside every closed set.

**Step 3.**

::: {.claim}
For every \( n \in \nN \) there is exactly one \( x \in X \) with \( (n, x) \in R \).
:::

::: {.proofofclaim}
We use @thm-omega-induction (b) on \( n \).

*Base case.* \( (0, a) \in R \), since \( R \) is closed. Suppose \( (0, b) \in R \) with \( b \ne a \), and let \( R' \coloneqq R \setminus \{(0, b)\} \). Then \( (0, a) \in R' \), because \( (0, a) \ne (0, b) \) (@fd2:def-ordered-pair). Let \( (m, x) \in R' \). Then \( (m, x) \in R \), so \( (\mathrm{S}(m), g(m, x)) \in R \); and this pair is not \( (0, b) \), because \( \mathrm{S}(m) \ne 0 \) by (P3). So it lies in \( R' \), and \( R' \) is closed. Hence \( R \subseteq R' \), which is false, since \( (0, b) \in R \) and \( (0, b) \notin R' \). So \( a \) is the only partner of \( 0 \).

*Inductive step.* Let \( n \in \nN \), and suppose \( n \) has exactly one partner \( x_n \) in \( R \). Since \( (n, x_n) \in R \) and \( R \) is closed, \( (\mathrm{S}(n), g(n, x_n)) \in R \). Suppose \( (\mathrm{S}(n), y) \in R \) with \( y \ne g(n, x_n) \), and let \( R' \coloneqq R \setminus \{(\mathrm{S}(n), y)\} \). Then \( (0, a) \in R' \), because \( \mathrm{S}(n) \ne 0 \) by (P3). Let \( (m, x) \in R' \); then \( (\mathrm{S}(m), g(m, x)) \in R \). If this pair were \( (\mathrm{S}(n), y) \), then \( \mathrm{S}(m) = \mathrm{S}(n) \), so \( m = n \) by (P4); then \( (n, x) \in R \), so \( x = x_n \) by the induction hypothesis; and then \( y = g(m, x) = g(n, x_n) \), against the choice of \( y \). So \( (\mathrm{S}(m), g(m, x)) \in R' \), and \( R' \) is closed. As in the base case, \( R \subseteq R' \) is false. So \( g(n, x_n) \) is the only partner of \( \mathrm{S}(n) \), which proves the claim.
:::

**Step 4 (the function).** \( R \) is a subset of \( \nN \times X \) in which each \( n \in \nN \) has exactly one partner, so \( f \coloneqq (R, X) \) is a function \( \nN \to X \) by @fd2:def-function, and \( f(n) \) is the partner of \( n \). Since \( (0, a) \in R \), \( f(0) = a \). For \( n \in \nN \), \( (n, f(n)) \in R \), so closure gives \( (\mathrm{S}(n), g(n, f(n))) \in R \), that is, \( f(\mathrm{S}(n)) = g(n, f(n)) \). This proves existence, and with Step 1, the theorem.
:::

Each Peano axiom has a visible job in the proof. (P3) appears in the base case of Step 3, where no step can produce a pair with first coordinate \( 0 \), and again in its inductive step, where it keeps \( (0, a) \) in \( R' \). (P4) appears in the inductive step: a pair that steps to first coordinate \( \mathrm{S}(n) \) has first coordinate \( n \), where the induction hypothesis applies. (P5) enters through @thm-omega-induction, in Steps 1 and 3. No choice is made: \( R \) is the one smallest closed set, and each partner is the only one. From now on a definition "\( f(0) \coloneqq a \), \( f(\mathrm{S}(n)) \coloneqq g(n, f(n)) \)" on \( \nN \) is legitimate whenever \( a \in X \) and \( g \colon \nN \times X \to X \) is a function, and \( f \) is **defined by recursion**.

::: {.check}
For \( X = \nN \), \( a = 0 \) and \( g(n, x) = \mathrm{S}(\mathrm{S}(x)) \), which pairs of \( R \) have first coordinate \( 0 \), \( 1 \) or \( 2 \)? (Here \( 1 \), \( 2 \), \( 3 \), \( 4 \) stand for \( \mathrm{S}(0) \), \( \mathrm{S}(1) \), \( \mathrm{S}(2) \), \( \mathrm{S}(3) \).)
:::

::: {.solution}
\( (0, 0) \), since \( R \) contains the starting pair; then \( (1, 2) \), since \( g(0, 0) = \mathrm{S}(\mathrm{S}(0)) = 2 \); then \( (2, 4) \), since \( g(1, 2) = \mathrm{S}(\mathrm{S}(2)) = 4 \). There are no others with these first coordinates, by the claim of Step 3.
:::

::: {.check}
In the inductive step of the claim, why does \( R' \coloneqq R \setminus \{(\mathrm{S}(n), y)\} \) still contain \( (0, a) \)? Which axiom is used?
:::

::: {.solution}
(P3): \( \mathrm{S}(n) \ne 0 \), so the removed pair has a different first coordinate from \( (0, a) \) and is not \( (0, a) \) (@fd2:def-ordered-pair).
:::

::: {.warning}
The hypothesis that \( g \) takes its values in \( X \) cannot be dropped. Let \( X = \{0\} \), \( a = 0 \), and \( g(n, x) \coloneqq \mathrm{S}(0) \) for \( n \in \nN \), \( x \in X \), so that \( g \) maps \( \nN \times X \) into \( \nN \) but not into \( X \). Any \( f \colon \nN \to X \) with the two equations would need \( f(\mathrm{S}(0)) = g(0, f(0)) = \mathrm{S}(0) \), and \( \mathrm{S}(0) \notin X \) since \( \mathrm{S}(0) \ne 0 \) by (P3); so no such \( f \) exists. The proof breaks at Step 2: this step does not map \( \nN \times X \) into itself, so @fd2:prp-smallest-closed-set does not apply.
:::

## Addition and multiplication

With the theorem, addition is the old school definition made official. To add \( n \) to \( m \), start at \( m \) and take \( n \) successor steps: \( m + 0 \) is \( m \), and \( m + \mathrm{S}(n) \) is one step further than \( m + n \). Multiplication is repeated addition in the same way.

*Adding \( n \) to \( m \) is taking \( n \) successor steps from \( m \).*

::: {#def-omega-arithmetic}
[Addition and Multiplication on \( \nN \)]

::: {.enumerate options="label=(\alph*)"}
1. For each \( m \in \nN \), let \( A_m \colon \nN \to \nN \) be the function given by @thm-omega-recursion with \( X = \nN \), \( a = m \) and \( g(n, x) = \mathrm{S}(x) \). The **sum** of \( m \) and \( n \) is \( m + n \coloneqq A_m(n) \). Thus, for all \( m, n \in \nN \),
\[
m + 0 = m, \qquad m + \mathrm{S}(n) = \mathrm{S}(m + n) .
\]
2. For each \( m \in \nN \), let \( M_m \colon \nN \to \nN \) be the function given by @thm-omega-recursion with \( X = \nN \), \( a = 0 \) and \( g(n, x) = x + m \). The **product** of \( m \) and \( n \) is \( m \cdot n \coloneqq M_m(n) \), also written \( mn \). Thus, for all \( m, n \in \nN \),
\[
m \cdot 0 = 0, \qquad m \cdot \mathrm{S}(n) = m \cdot n + m .
\]
3. The **numerals** are \( 1 \coloneqq \mathrm{S}(0) \), \( 2 \coloneqq \mathrm{S}(1) \), \( 3 \coloneqq \mathrm{S}(2) \), and so on. For every \( n \in \nN \), \( n + 1 = \mathrm{S}(n) \); in particular \( 1 + 1 = 2 \) and \( k + 2 = (k + 1) + 1 \) for every \( k \in \nN \).
:::
:::

In words: (a) and (b) are the two clauses we would write for a school definition, and the theorem guarantees that they define exactly one function \( A_m \), respectively \( M_m \), for each \( m \). Multiplication binds more tightly than addition, so \( m \cdot n + m \) is \( (m \cdot n) + m \).

**Well-definedness.** Each \( g \) maps \( \nN \times \nN \) into \( \nN \): \( \mathrm{S}(x) \in \nN \) because \( \mathrm{S} \) maps \( \nN \) into \( \nN \), and \( x + m = A_x(m) \in \nN \) because \( A_x \) maps into \( \nN \). So (b) uses (a), and (a) uses nothing but the successor. The sum is then a function \( \nN \times \nN \to \nN \), with graph \( \{ ((m, n), k) \in (\nN \times \nN) \times \nN : k = A_m(n) \} \) (@fd2:def-set-builder): each \( (m, n) \) gets exactly one \( k \), because each \( A_m \) exists and is unique. Likewise for the product.

**The successor is "plus one".** Proof of the last sentence of (c): for every \( n \in \nN \),
\[
n + 1 = n + \mathrm{S}(0) = \mathrm{S}(n + 0) = \mathrm{S}(n) ,
\]
by (c) and the two equations of (a). From now on we write \( n + 1 \) for \( \mathrm{S}(n) \) whenever \( n \in \nN \); the defining equations then read as in school:
\[
\begin{aligned}
m + 0 &= m, & m + (n + 1) &= (m + n) + 1, \\
m \cdot 0 &= 0, & m \cdot (n + 1) &= m \cdot n + m .
\end{aligned}
\]
Two small computations are used repeatedly later: \( 1 + 1 = \mathrm{S}(1) = 2 \), and, for every \( k \in \nN \),
\[
k + 2 = k + \mathrm{S}(1) = \mathrm{S}(k + 1) = (k + 1) + 1 .
\]

A non-example by minimal change: keep \( a = m \) in (a), but replace \( g(n, x) = \mathrm{S}(x) \) by \( g(n, x) = \mathrm{S}(n) \), which ignores the current value. This \( g \) is still a function \( \nN \times \nN \to \nN \), so @thm-omega-recursion gives exactly one \( f \colon \nN \to \nN \) with \( f(0) = m \) and \( f(\mathrm{S}(n)) = \mathrm{S}(n) \). The first equation \( m + 0 = m \) still holds for this "sum", but the second, \( m + \mathrm{S}(n) = \mathrm{S}(m + n) \), fails: with \( m = 2 \), \( f(1) = \mathrm{S}(0) = 1 \), while \( \mathrm{S}(f(0)) = \mathrm{S}(2) = 3 \). So it would give \( 2 + 1 = 1 \), and it is not addition.

The defining equations immediately give the two Peano facts in the "plus one" notation.

::: {#cor-omega-successor-cancellation}
[Successor Cancellation]

For all \( k, l \in \nN \): if \( k + 1 = l + 1 \), then \( k = l \); and \( k + 1 \ne 0 \).
:::

::: {.proof}
By (c) of @def-omega-arithmetic, \( k + 1 = \mathrm{S}(k) \) and \( l + 1 = \mathrm{S}(l) \). So the first claim is (P4) for \( \nN \), and the second is (P3) (@ax-natural-numbers).
:::

::: {.check}
Compute \( 2 + 2 \) and \( 2 \cdot 2 \) from the defining equations alone.
:::

::: {.solution}
By (a) of @def-omega-arithmetic, three times,
\[
2 + 2 = \mathrm{S}(2 + 1) = \mathrm{S}\bigl(\mathrm{S}(2 + 0)\bigr) = \mathrm{S}\bigl(\mathrm{S}(2)\bigr) = \mathrm{S}(3) = 4 .
\]
By (b), twice and then at \( 0 \),
\[
2 \cdot 2 = 2 \cdot 1 + 2 = (2 \cdot 0 + 2) + 2 = (0 + 2) + 2 ,
\]
and \( 0 + 2 = \mathrm{S}(0 + 1) = \mathrm{S}(\mathrm{S}(0 + 0)) = \mathrm{S}(\mathrm{S}(0)) = 2 \). So \( 2 \cdot 2 = 2 + 2 = 4 \).
:::

## The laws of arithmetic

Every law of arithmetic that *Sets and Functions*, Chapter 3 took from the real numbers must now be proved, and the only tools are the four defining equations and induction. The equations are lopsided: they say what happens when the **second** argument goes up by one, and nothing about the first. So in every induction in the proof of @thm-omega-arithmetic-laws we fix all variables but one and induct on the variable that the recursion runs on, the second argument of \( + \) or \( \cdot \).

::: {.idea}
[Scratch work]

Take the first law that school arithmetic uses without a thought: \( 0 + n = n \). The defining equations do not give it. They give \( m + 0 = m \), with the \( 0 \) in the **second** place, and \( 0 + n \) has its \( 0 \) in the first. Which variable to induct on? The equations speak about \( 0 \) and successors in the second place, and in \( 0 + n \) that place is held by \( n \). So induct on \( n \): then the base case is a defining equation, and the step can open \( 0 + (n + 1) \) with the other one.

| Givens | Goal |
|---|---|
| \( m + 0 = m \) and \( m + (n + 1) = (m + n) + 1 \) for all \( m, n \) | \( 0 + n = n \) for every \( n \in \nN \) |
| \( 0 + 0 = 0 \): the first equation with \( m = 0 \) | base closed; step: \( 0 + (n + 1) = n + 1 \) |
| IH: \( 0 + n = n \) | \( 0 + (n + 1) = (0 + n) + 1 = n + 1 \): closed |

The second equation, with \( m = 0 \), opens the term at \( n + 1 \); the hypothesis applies to the inner \( 0 + n \); nothing is left to do. Had we tried to induct with \( 0 \) and \( n \) in the other roles, there would be no equation to open the term with.
:::

The scratch work proves the first half of (a) in the theorem below; the rest of the theorem is proved the same way.

::: {#thm-omega-arithmetic-laws}
[Laws of Arithmetic on \( \nN \)]

For all \( k, m, n \in \nN \):

::: {.enumerate options="label=(\alph*)"}
1. \( 0 + n = n \), and \( (m + 1) + n = (m + n) + 1 \);
2. \( m + n = n + m \);
3. \( (k + m) + n = k + (m + n) \);
4. \( m(n + k) = mn + mk \) and \( (n + k)m = nm + km \);
5. \( 0 \cdot n = 0 \), \( (m + 1) \cdot n = mn + n \), and \( n \cdot 1 = 1 \cdot n = n \);
6. \( mn = nm \);
7. \( (km)n = k(mn) \).
:::
:::

The move of the scratch work is worth naming, because the identities of this section are proved with it.

::: {#exm-method-induct-on-recursion-variable}
[Method: fix the others, induct on the recursion variable]

**Template.** (1) Find the variable the definition is a recursion on: the second argument of \( + \) and \( \cdot \), the exponent of a power \( u^n \) (*Sets and Functions*, Section 3.3; on \( \nN \) in the next section). (2) Fix the other variables. (3) Induct on it: the base is the defining equation at \( 0 \); the step opens the term at \( n + 1 \) by the other equation, applies the hypothesis inside, and closes up. (4) If the variable sits where no equation applies (a first argument), first prove the lemma that moves it.

**When to use it.** Identities between terms built by recursion: laws of \( + \) and \( \cdot \), of powers, of sums.

**The usual failure.** Inducting on a first argument (the warning after the proof); citing a law not yet proved, such as commutativity before (a).
:::

::: {.idea}
Every clause except the second half of (d) and the last part of (e), which follow from earlier clauses directly, is proved by @exm-method-induct-on-recursion-variable, in an order where each uses only earlier ones. Commutativity (b) needs both halves of (a), which move a successor out of the **first** argument, where no defining equation reaches.
:::

::: {.proof}
Each induction is @thm-omega-induction (b), applied to the property stated in the clause, with the other variables fixed. "Def" refers to the equations of @def-omega-arithmetic, "IH" to the induction hypothesis.

*(a)* The first half, \( 0 + n = n \), is the scratch work above: the base is Def with \( m = 0 \), and the step is \( 0 + (n + 1) = (0 + n) + 1 = n + 1 \), by Def and IH. For the second half, fix \( m \in \nN \) and induct on \( n \). *Base case:* \( (m + 1) + 0 = m + 1 = (m + 0) + 1 \), by Def twice. *Inductive step:* if \( (m + 1) + n = (m + n) + 1 \), then
\[
(m + 1) + (n + 1) = \bigl((m + 1) + n\bigr) + 1 = \bigl((m + n) + 1\bigr) + 1 = \bigl(m + (n + 1)\bigr) + 1 ,
\]
by Def, IH, and Def read from right to left inside the outer \( + 1 \).

*(c)* We prove associativity of addition in full. Fix \( k, m \in \nN \), and let \( P(n) \) be "\( (k + m) + n = k + (m + n) \)". *Base case:* by the first equation of (a) of @def-omega-arithmetic, applied twice,
\[
(k + m) + 0 = k + m = k + (m + 0) .
\]
*Inductive step:* suppose \( P(n) \). Then
\[
\begin{aligned}
(k + m) + (n + 1) &= \bigl((k + m) + n\bigr) + 1 = \bigl(k + (m + n)\bigr) + 1 \\
&= k + \bigl((m + n) + 1\bigr) = k + \bigl(m + (n + 1)\bigr) ,
\end{aligned}
\]
where the first equality is Def with first argument \( k + m \), the second is \( P(n) \), the third is Def with first argument \( k \) and second argument \( m + n \), and the fourth is Def with first argument \( m \). So \( P(n + 1) \) holds, and by @thm-omega-induction (b), \( P(n) \) holds for every \( n \in \nN \).

*(b), (d)–(g)* follow by the same move, in the order of the table in the fold below.
:::

::: {.second-reading title="Proofs of (b) and (d)–(g)"}
"Def" refers to the equations of @def-omega-arithmetic, "IH" to the induction hypothesis. The second half of (d) and the last part of (e) are derived from earlier clauses without induction; for the first half of (d) the variable is \( k \), the recursion variable of \( m(n + k) \).

The other clauses follow the same pattern; the table gives, for each, the property inducted on, the base case, the step, and the earlier clauses used. They are proved in the order of the table, so each row uses only (a), (c) and rows above it.

| Clause, variable | Base case | Inductive step (IH at the marked equality) | Uses |
|---|---|---|---|
| (b) \( m + n = n + m \); \( m \) fixed, on \( n \) | \( m + 0 = m = 0 + m \) | \( m + (n + 1) = (m + n) + 1 \overset{\text{IH}}{=} (n + m) + 1 = (n + 1) + m \) | Def; (a), both halves |
| (d) \( m(n + k) = mn + mk \); \( m, n \) fixed, on \( k \) | \( m(n + 0) = mn = mn + 0 = mn + m \cdot 0 \) | \( m(n + (k + 1)) = m((n + k) + 1) = m(n + k) + m \overset{\text{IH}}{=} (mn + mk) + m = mn + (mk + m) = mn + m(k + 1) \) | Def; (c) |
| (e) \( 0 \cdot n = 0 \); on \( n \) | \( 0 \cdot 0 = 0 \) (Def) | \( 0 \cdot (n + 1) = 0 \cdot n + 0 \overset{\text{IH}}{=} 0 + 0 = 0 \) | Def |
| (e) \( (m + 1) n = mn + n \); \( m \) fixed, on \( n \) | \( (m + 1) \cdot 0 = 0 = 0 + 0 = m \cdot 0 + 0 \) | \( (m + 1)(n + 1) = (m + 1)n + (m + 1) \overset{\text{IH}}{=} (mn + n) + (m + 1) = mn + (n + (m + 1)) = mn + ((n + m) + 1) = mn + ((m + n) + 1) = mn + (m + (n + 1)) = (mn + m) + (n + 1) = m(n + 1) + (n + 1) \) | Def; (b), (c) |
| (e) \( n \cdot 1 = n \), \( 1 \cdot n = n \); no induction | | \( n \cdot 1 = n \cdot 0 + n = 0 + n = n \); \( 1 \cdot n = (0 + 1) \cdot n = 0 \cdot n + n = 0 + n = n \) | Def; (a); first two parts of (e) |
| (f) \( mn = nm \); \( m \) fixed, on \( n \) | \( m \cdot 0 = 0 = 0 \cdot m \) | \( m(n + 1) = mn + m \overset{\text{IH}}{=} nm + m = (n + 1)m \) | Def; (e) |
| (d), second half; no induction | | \( (n + k)m = m(n + k) = mn + mk = nm + km \) | (d), first half; (f) |
| (g) \( (km)n = k(mn) \); \( k, m \) fixed, on \( n \) | \( (km) \cdot 0 = 0 = k \cdot 0 = k(m \cdot 0) \) | \( (km)(n + 1) = (km)n + km \overset{\text{IH}}{=} k(mn) + km = k(mn + m) = k(m(n + 1)) \) | Def; (d) |

In the step of (b), the last equality is (a), second half, read from right to left. In the long step of (e), the equalities after IH use, in order, (c), Def, (b), Def, (c), Def. In the last part of (e), \( 1 = 0 + 1 \) is the first half of (a), and \( (0 + 1) \cdot n = 0 \cdot n + n \) is the second part of (e) with \( m = 0 \). In (g), \( k(mn + m) = k(mn) + km \) is the first half of (d). This proves the theorem.
:::

The laws (a)–(g) are the rules of school arithmetic, now proved from @ax-natural-numbers. The next section defines the order from addition and proves its properties with these laws.

::: {.warning}
**Do not assume \( 0 + n = n \).** It is clause (a) of @thm-omega-arithmetic-laws, proved by induction; the defining equation is \( n + 0 = n \). For the same reason, inducting on \( m \) in \( m + n = n + m \) gets stuck: the step would need \( (m + 1) + n \), and the definition says nothing about a sum whose **first** argument is a successor until (a) is proved.
:::

The order of the table is forced by the lopsided definition. Commutativity, which lets us move a successor from the second place to the first, comes only after the two facts in (a) that move it by hand; once it is available, (e) and (f) follow the same way for multiplication.

::: {.check}
Which variable would you induct on to prove \( m(n + k) = mn + mk \), and which earlier law lets the step close?
:::

::: {.solution}
On \( k \), the second argument of \( n + k \) and of \( mk \), where the recursion runs; \( m \) and \( n \) are fixed. The step is
\[
m\bigl(n + (k + 1)\bigr) = m\bigl((n + k) + 1\bigr) = m(n + k) + m = (mn + mk) + m = mn + (mk + m) = mn + m(k + 1) ,
\]
by Def of \( + \), Def of \( \cdot \), IH, associativity (c), and Def of \( \cdot \) again. Law (c) is the one that lets the step close.
:::

## Exercises

### A. Check your understanding

::: {#exr-recursion-and-arithmetic-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. In the proof of @thm-omega-recursion, where are (P3) and (P4) used?
2. Why does the uniqueness half need only an induction, while existence needs the set \( R \)?
3. Name the move, and the variable, for proving \( 0 \cdot n = 0 \).
4. State the idea of the existence proof in two sentences.
:::
:::

::: {.solution}
(a) (P3) is used in the base case of the claim of Step 3: no step produces a pair with first coordinate \( 0 \), since \( \mathrm{S}(m) \ne 0 \), so a second pair \( (0, b) \) could be removed without breaking closure. It is used again in the inductive step, where \( \mathrm{S}(n) \ne 0 \) keeps \( (0, a) \) in \( R' \). (P4) is used in the inductive step: a pair that steps to first coordinate \( \mathrm{S}(n) \) has first coordinate \( n \), where the induction hypothesis applies.

(b) Uniqueness compares two functions that are **given**, value by value, and comparing values at \( n + 1 \) through the values at \( n \) is exactly an induction on \( n \). Existence asks for a function that is not given; induction proves statements and builds nothing. So existence needs an object first, the set \( R \), and induction then proves a statement about it (the claim of Step 3).

(c) Fix the others, induct on the recursion variable (@exm-method-induct-on-recursion-variable). There are no others to fix; the recursion variable of \( 0 \cdot n \) is \( n \). Base: \( 0 \cdot 0 = 0 \) by Def. Step: \( 0 \cdot (n + 1) = 0 \cdot n + 0 = 0 + 0 = 0 \), by Def, the hypothesis, and Def.

(d) The smallest set of pairs closed under the two equations exists. Each \( n \) has exactly one partner in it, because a second partner could be removed without breaking closure, so the set is the graph of the required function.
:::

### B. Practice

::: {#exr-recursion-and-arithmetic-b1}
[B1: Small products]

Compute \( 3 \cdot 2 \) and \( 2 \cdot 3 \) from the defining equations of @def-omega-arithmetic alone, without using @thm-omega-arithmetic-laws. Here \( 5 \coloneqq \mathrm{S}(4) \) and \( 6 \coloneqq \mathrm{S}(5) \).
:::

::: {.solution}
For \( 3 \cdot 2 \), by (b) twice and then at \( 0 \):
\[
3 \cdot 2 = 3 \cdot 1 + 3 = (3 \cdot 0 + 3) + 3 = (0 + 3) + 3 .
\]
By (a), \( 0 + 3 = \mathrm{S}(0 + 2) = \mathrm{S}(\mathrm{S}(0 + 1)) = \mathrm{S}(\mathrm{S}(\mathrm{S}(0 + 0))) = \mathrm{S}(\mathrm{S}(\mathrm{S}(0))) = 3 \). Then
\[
3 + 3 = \mathrm{S}(3 + 2) = \mathrm{S}\bigl(\mathrm{S}(3 + 1)\bigr) = \mathrm{S}\Bigl(\mathrm{S}\bigl(\mathrm{S}(3 + 0)\bigr)\Bigr) = \mathrm{S}(\mathrm{S}(\mathrm{S}(3))) = 6 .
\]
So \( 3 \cdot 2 = 6 \).

For \( 2 \cdot 3 \), by (b), \( 2 \cdot 3 = 2 \cdot 2 + 2 \), and \( 2 \cdot 2 = 4 \) by the Quick check above. Then
\[
4 + 2 = \mathrm{S}(4 + 1) = \mathrm{S}\bigl(\mathrm{S}(4 + 0)\bigr) = \mathrm{S}(\mathrm{S}(4)) = 6 .
\]
So \( 2 \cdot 3 = 6 = 3 \cdot 2 \), as (f) of @thm-omega-arithmetic-laws predicts; but the two computations took different routes, and neither used a law.
:::

::: {#exr-recursion-and-arithmetic-b2}
[B2: Distributivity, last step blank]

Here is the proof of \( m(n + k) = mn + mk \) for all \( m, n, k \in \nN \), with the last step left blank. *Name the move, then complete it.*

> Fix \( m, n \in \nN \) and induct on \( k \). Base case: \( m(n + 0) = mn = mn + 0 = mn + m \cdot 0 \). Inductive step: suppose \( m(n + k) = mn + mk \). Then
> \[
> m\bigl(n + (k + 1)\bigr) = m\bigl((n + k) + 1\bigr) = m(n + k) + m = (mn + mk) + m = \underline{\hspace{6em}} .
> \]

Justify each equality you add.
:::

::: {.solution}
The move is **fix the others, induct on the recursion variable** (@exm-method-induct-on-recursion-variable): in \( m(n + k) \) the recursion of \( + \) runs on \( k \), so \( m \) and \( n \) are fixed and the induction is on \( k \).

The completion is
\[
(mn + mk) + m = mn + (mk + m) = mn + m(k + 1) ,
\]
where the first equality is associativity, (c) of @thm-omega-arithmetic-laws, and the second is the defining equation \( m(k + 1) = mk + m \) of @def-omega-arithmetic (b), read from right to left. This is the statement for \( k + 1 \), so by @thm-omega-induction (b) it holds for every \( k \in \nN \). (This is clause (d) of @thm-omega-arithmetic-laws, already proved; the exercise practices the move.)
:::

::: {#exr-recursion-and-arithmetic-b3}
[B3: Prove or disprove]

Prove each true statement and refute each false one with a counterexample. All letters stand for natural numbers, and you may use @thm-omega-arithmetic-laws.

::: {.enumerate options="label=(\alph*)"}
1. If \( m + n = 0 \), then \( m = n = 0 \).
2. If \( mn = m \), then \( n = 1 \).
3. \( m \cdot (n + 1) = m \cdot n + n \).
4. If \( m + n = m \), then \( n = 0 \).
5. If \( n \cdot n = n \), then \( n = 0 \).
:::
:::

::: {.solution}
(a) **True.** Suppose \( n \ne 0 \). Then \( n = \mathrm{S}(k) = k + 1 \) for some \( k \in \nN \) (@prp-peano-predecessor (a), and (c) of @def-omega-arithmetic), and
\[
m + n = m + (k + 1) = (m + k) + 1 \ne 0
\]
by Def and @cor-omega-successor-cancellation. So \( m + n = 0 \) forces \( n = 0 \), and then \( m = m + 0 = 0 \).

(b) **False.** Take \( m = n = 0 \): \( 0 \cdot 0 = 0 = m \), but \( n = 0 \ne 1 \), since \( 1 = \mathrm{S}(0) \ne 0 \) by (P3).

(c) **False.** This is a look-alike of the defining equation \( m \cdot (n + 1) = m \cdot n + m \) of @def-omega-arithmetic (b), whose last term is \( m \), not \( n \). Take \( m = 0 \), \( n = 1 \): the left side is \( 0 \cdot 2 = 0 \) by law (e), and the right side is \( 0 \cdot 1 + 1 = 0 + 1 = 1 \), and \( 1 \ne 0 \).

(d) **True.** Induct on \( m \) for the property "for every \( n \), if \( m + n = m \), then \( n = 0 \)". *Base:* \( 0 + n = n \) by law (a), so \( 0 + n = 0 \) gives \( n = 0 \). *Step:* suppose the property for \( m \), and let \( (m + 1) + n = m + 1 \). By law (a), \( (m + 1) + n = (m + n) + 1 \), so \( (m + n) + 1 = m + 1 \), and @cor-omega-successor-cancellation gives \( m + n = m \). By the hypothesis, \( n = 0 \).

(e) **False.** Take \( n = 1 \): \( 1 \cdot 1 = 1 \cdot 0 + 1 = 0 + 1 = 1 \), by Def and law (a), but \( 1 \ne 0 \).
:::

### C. Going deeper

::: {#exr-recursion-and-arithmetic-c1}
[C1: Exit check: addition is commutative]

From the two defining equations of addition, \( m + 0 = m \) and \( m + (n + 1) = (m + n) + 1 \), and @thm-omega-induction alone, prove that \( m + n = n + m \) for all \( m, n \in \nN \). Prove every auxiliary fact you need.
:::

::: {.solution}
[Hint 1]

The definition says what happens when the second argument is \( 0 \) or a successor. To use it on \( n + m \), you need to know the same for the first argument: prove two lemmas first.
:::

::: {.solution}
[Hint 2]

Start with the first lemma, \( 0 + n = n \), by induction on \( n \); the base is the first equation with \( m = 0 \). Then find the second lemma, about \( (m + 1) + n \), yourself.
:::

::: {.solution}
All inductions are by @thm-omega-induction (b).

*Lemma 1: \( 0 + n = n \) for every \( n \).* Induct on \( n \). Base: \( 0 + 0 = 0 \), by the first equation. Step: if \( 0 + n = n \), then \( 0 + (n + 1) = (0 + n) + 1 = n + 1 \), by the second equation and the hypothesis.

*Lemma 2: \( (m + 1) + n = (m + n) + 1 \) for all \( m, n \).* Fix \( m \) and induct on \( n \). Base: \( (m + 1) + 0 = m + 1 = (m + 0) + 1 \), by the first equation twice. Step: if \( (m + 1) + n = (m + n) + 1 \), then
\[
(m + 1) + (n + 1) = \bigl((m + 1) + n\bigr) + 1 = \bigl((m + n) + 1\bigr) + 1 = \bigl(m + (n + 1)\bigr) + 1 ,
\]
by the second equation, the hypothesis, and the second equation read from right to left inside the outer \( + 1 \).

*Main induction.* Fix \( m \) and induct on \( n \) for "\( m + n = n + m \)". Base: \( m + 0 = m = 0 + m \), by the first equation and Lemma 1. Step: if \( m + n = n + m \), then
\[
m + (n + 1) = (m + n) + 1 = (n + m) + 1 = (n + 1) + m ,
\]
by the second equation, the hypothesis, and Lemma 2 (with \( n \) in the role of \( m \) and \( m \) in the role of \( n \)), read from right to left. Hence \( m + n = n + m \) for all \( m, n \in \nN \).

**Marking scheme.** (10 points)
- 2: proves \( 0 + n = n \) by induction on \( n \), from the first equation (base) and the second (step).
- 3: proves, by an induction with the other variable fixed, a lemma that moves a successor out of the first argument (the book's \( (m + 1) + n = (m + n) + 1 \), or \( 1 + n = n + 1 \) together with associativity of addition), base and step both justified.
- 2: in the main induction, the base case \( m + 0 = 0 + m \), using the first lemma.
- 2: in the main induction, the step, using the second equation, the hypothesis and that lemma.
- 1: names the variable inducted on in each induction and fixes the other.
Fatal errors (0 for the step): citing commutativity, or any law of @thm-omega-arithmetic-laws, without proving it from the two equations; treating \( 0 + n = n \) as if it were a defining equation. A second route inducts on \( m \) in the main induction with \( n \) fixed; it needs the same two lemmas, and its base and step map to the same 2 + 2 points. A third route proves associativity and \( 1 + n = n + 1 \) (each by induction on \( n \), from the equations and \( 0 + n = n \)) and then closes the step as \( m + (n + 1) = (m + n) + 1 = (n + m) + 1 = n + (m + 1) = n + (1 + m) = (n + 1) + m \); those two lemmas together earn the 3 points.
:::

::: {#exr-recursion-and-arithmetic-c2}
[C2: Associativity of multiplication, last half blank]

Prove that \( (km)n = k(mn) \) for all \( k, m, n \in \nN \). The first half is given; *name the move, then complete it.*

> Fix \( k, m \in \nN \) and induct on \( n \). Base case: \( (km) \cdot 0 = 0 = k \cdot 0 = k(m \cdot 0) \). Inductive step: \( \underline{\hspace{10em}} \)

You may use (a)–(f) of @thm-omega-arithmetic-laws. If you read the fold after its proof, the last row of the table compresses this step into one line; write it out without looking, and give the reason for each equality.
:::

::: {.solution}
The move is **fix the others, induct on the recursion variable**: in \( (km)n \) and \( k(mn) \) the variable \( n \) is the second argument of the outer and the inner product, where the recursion runs, so \( k \) and \( m \) are fixed.

*Inductive step.* Suppose \( (km)n = k(mn) \). Then
\[
\begin{aligned}
(km)(n + 1) &= (km)n + km = k(mn) + km \\
&= k(mn + m) = k\bigl(m(n + 1)\bigr) ,
\end{aligned}
\]
where the first equality is the defining equation of @def-omega-arithmetic (b) with first factor \( km \), the second is the induction hypothesis, the third is (d) of @thm-omega-arithmetic-laws read from right to left (\( k(x + y) = kx + ky \) with \( x = mn \), \( y = m \)), and the fourth is the defining equation with first factor \( m \). By @thm-omega-induction (b), \( (km)n = k(mn) \) for every \( n \), and \( k, m \) were arbitrary.

The base case used the defining equation \( x \cdot 0 = 0 \) three times, with \( x = km \), \( x = k \) and \( x = m \). Commutativity (f) is not needed for this route; a proof that first rewrites \( km \) as \( mk \) would need it.
:::

::: {#exr-recursion-and-arithmetic-c3}
[C3: Doubling]

Show that there is exactly one function \( D \colon \nN \to \nN \) with \( D(0) = 0 \) and \( D(n + 1) = (D(n) + 1) + 1 \) for every \( n \in \nN \), and prove that \( D(n) = n + n \) for every \( n \in \nN \).
:::

::: {.solution}
*Existence and uniqueness.* The function \( g \colon \nN \times \nN \to \nN \), \( g(n, x) \coloneqq \mathrm{S}(\mathrm{S}(x)) = (x + 1) + 1 \), maps into \( \nN \) since \( \mathrm{S} \) maps \( \nN \) into \( \nN \). By @thm-omega-recursion with \( X = \nN \) and \( a = 0 \), there is exactly one \( D \colon \nN \to \nN \) with \( D(0) = 0 \) and \( D(n + 1) = g(n, D(n)) = (D(n) + 1) + 1 \). (Its graph is the set \( R \) of the proof for these data, which contains \( (1, 2) \) and \( (2, 4) \) by the first Quick check after @thm-omega-recursion; so \( D(1) = 2 \) and \( D(2) = 4 \).)

*The formula.* Induct on \( n \) by @thm-omega-induction (b) for "\( D(n) = n + n \)". Base: \( D(0) = 0 = 0 + 0 \), by the defining equation \( m + 0 = m \). Step: suppose \( D(n) = n + n \). Then
\[
\begin{aligned}
(n + 1) + (n + 1) &= \bigl((n + 1) + n\bigr) + 1 = \bigl((n + n) + 1\bigr) + 1 \\
&= \bigl(D(n) + 1\bigr) + 1 = D(n + 1) ,
\end{aligned}
\]
where the first equality is the defining equation of @def-omega-arithmetic (a), the second is (a) of @thm-omega-arithmetic-laws, \( (m + 1) + n = (m + n) + 1 \) with \( m = n \), the third is the hypothesis, and the last is the equation of \( D \). Hence \( D(n) = n + n \) for every \( n \in \nN \).

*Alternatively,* \( n \mapsto n + n \) satisfies the two equations that define \( D \) (the computation above, read without the hypothesis, shows \( (n + 1) + (n + 1) = ((n + n) + 1) + 1 \)), so it is \( D \) by the uniqueness half of @thm-omega-recursion. Either way the double \( n + n \) is \( 2n \) too: \( 2n = n \cdot 2 = n \cdot 1 + n = n + n \) by (f), the defining equation of \( \cdot \), and (e) of @thm-omega-arithmetic-laws.
:::

<!-- dependency ledger
thm-omega-recursion (proof): S maps N into N, so the step (n, x) -> (S(n), g(n, x)) maps N x X into itself | ax-natural-numbers, def-peano-system (data of a Peano system), recalled in prose
thm-omega-recursion (proof): R \ {p} is a subset of R; R subset of R' fails when p in R and p not in R' | def-set-operations (F2.1 §03), working rules of subsets (F2.1 §02)
thm-omega-recursion (proof): a subset of N x X in which each n has exactly one partner, with codomain X, is a function | fd2:def-function (cited)
thm-omega-recursion (proof): (P3), (P4) for N | ax-natural-numbers, def-peano-system (cited by clause name)
def-omega-arithmetic (claim): the graph of + is a set and a function | fd2:def-set-builder (cited), uniqueness half of thm-omega-recursion
def-omega-arithmetic (claim): the numerals 4, 5, 6 as successors | "and so on" in (c); 5, 6 defined where used (B1)
thm-omega-arithmetic-laws (proof): rewriting inside a term with an equation (substitution of equals) | equality rules of F1.4 (=E), used throughout
exr-recursion-and-arithmetic-b3 (solution): 1 != 0 | (P3), since 1 = S(0)
exr-recursion-and-arithmetic-c3 (solution): 2n = n + n | inline, from def-omega-arithmetic and thm-omega-arithmetic-laws (e), (f)
-->
