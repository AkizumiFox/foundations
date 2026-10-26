# Ordered Rings and the Rules for Inequalities

Section 2.3 made \( \nZ \) a commutative ring and proved the rules for equations from (F1)–(F9). Inequalities need the same treatment. In school, \( -3 < -2 \) is read off a number line; here there is no line, only classes of pairs. This section lists four order axioms, shows that an order is the same thing as a set of positive elements, orders \( \nZ \), and derives the rules for inequalities in every ordered ring. Each rule will come from one observation: \( a < b \) is a statement about the single element \( b - a \).

## Ordered rings

The integers carry an order tied to the operations: adding the same number to both sides keeps an inequality, and a product of positives is positive. We want every rule for inequalities to follow from a short list of axioms, as for equations. The list is the order axioms (O1)–(O4) of *Analysis on the Real Line*, Chapter 1, with "field" relaxed to "commutative ring".

*An ordered ring is a ring with a strict order that adding respects, in which a product of positives is positive.*

::: {#def-ordered-ring-and-field}
[Ordered Ring, Ordered Field]

An **ordered commutative ring** is a commutative ring \( R \) (@def-commutative-ring-and-field) together with a relation \( < \) on \( R \) such that, **for all** \( a, b, c \in R \):

::: {.enumerate options="label=(O\arabic*)"}
1. (trichotomy) **exactly one** of \( a < b \), \( a = b \), \( b < a \) holds;
2. (transitivity) if \( a < b \) and \( b < c \), then \( a < c \);
3. (addition) if \( a < b \), then \( a + c < b + c \);
4. (multiplication) if \( 0 < a \) and \( 0 < b \), then \( 0 < ab \).
:::

An **ordered field** is a field that is an ordered commutative ring. We write \( b > a \) for \( a < b \), and \( a \le b \) for "\( a < b \) or \( a = b \)" (likewise \( b \ge a \)). An element \( a \) is **positive** if \( a > 0 \), **negative** if \( a < 0 \), and **non-negative** if \( a \ge 0 \).
:::

In words: any two elements compare in exactly one way, so \( a < a \) never holds; comparisons chain; we may add the same element to both sides; and (O4), the only clause about multiplication, speaks only of **positive** elements.

The degenerate case: the zero ring \( \{0\} \) with the **empty** relation is an ordered commutative ring. Only the middle option of (O1) holds, and (O2)–(O4) are vacuous. There \( 1 = 0 \), so any rule concluding \( 1 > 0 \) must assume \( 1 \ne 0 \).

Checking (O1)–(O4) directly means handling pairs of elements. It is easier to say which elements are positive and let \( a < b \) mean that \( b - a \) is positive. The next proposition says which "positive sets" give an order, and that every order arises so. We call the move **order from a positive set**.

::: {#prp-order-from-positives}
[Order from a Positive Set]

Let \( R \) be a commutative ring and \( P \subseteq R \) a subset such that:

::: {.enumerate options="label=(P\arabic*)"}
1. if \( a, b \in P \), then \( a + b \in P \) and \( ab \in P \);
2. **for every** \( a \in R \), **exactly one** of \( a \in P \), \( a = 0 \), \( -a \in P \) holds.
:::

Define \( a < b \) to mean \( b - a \in P \). Then \( (R, <) \) is an ordered commutative ring (@def-ordered-ring-and-field), and \( P = \{ a \in R : a > 0 \} \).

Conversely, if \( (R, <) \) is an ordered commutative ring, then \( P \coloneqq \{ a \in R : a > 0 \} \) satisfies (P1) and (P2), and for all \( a, b \in R \), \( a < b \) holds if and only if \( b - a \in P \).
:::

The labels (P1), (P2) are local; they are not the clauses of a partition (*Sets and Functions*, Section 5.2) or Peano's axioms (Chapter 1).

::: {.idea}
Each order axiom is a statement about one difference. (O1) is (P2) applied to \( b - a \), since \( -(b - a) = a - b \). (O2) is closure under sums, since \( (c - b) + (b - a) = c - a \). (O3) holds since \( (b + c) - (a + c) = b - a \). (O4) is closure under products. The algebra is uniqueness of negatives.
:::

::: {.proof}
We first record three identities in \( R \), for \( a, b, c \in R \):
\[
\begin{gathered}
-(b - a) = a - b , \qquad (c - b) + (b - a) = c - a , \\
(b + c) - (a + c) = b - a .
\end{gathered}
\]
For the first, \( (b - a) + (a - b) = (b + (-b)) + ((-a) + a) = 0 \) by (F1), (F2), (F4), and @prp-ring-algebra (a) gives the identity. The second is regrouping by (F1)–(F4). For the third, \( (a + c) + ((-a) + (-c)) = 0 \) likewise, so \( -(a + c) = (-a) + (-c) \) by @prp-ring-algebra (a), and the \( c \)'s cancel. Also \( -0 = 0 \) (as \( 0 + 0 = 0 \)), so \( a - 0 = a \); and \( b - a = 0 \) if and only if \( b = a \): one direction is (F4), and \( b - a = 0 \) gives \( b = (b - a) + a = 0 + a = a \).

Now let \( P \) satisfy (P1), (P2), and let \( a < b \) mean \( b - a \in P \).

(O1) Apply (P2) to \( b - a \): exactly one of \( b - a \in P \), \( b - a = 0 \), \( -(b - a) \in P \) holds. By the facts above, these say \( a < b \), \( a = b \) and \( a - b \in P \), that is, \( b < a \). So exactly one of the three holds.

(O2) If \( b - a \in P \) and \( c - b \in P \), then \( c - a = (c - b) + (b - a) \in P \) by (P1).

(O3) If \( b - a \in P \), then \( (b + c) - (a + c) = b - a \in P \).

(O4) Since \( a - 0 = a \), we have \( 0 < a \) if and only if \( a \in P \). So \( 0 < a \) and \( 0 < b \) give \( a, b \in P \), hence \( ab \in P \) by (P1), that is, \( 0 < ab \). The same equivalence says \( P = \{ a \in R : a > 0 \} \).

Conversely, let \( (R, <) \) be an ordered commutative ring and \( P \coloneqq \{ a : a > 0 \} \). If \( a < b \), then \( a + (-a) < b + (-a) \) by (O3), that is, \( 0 < b - a \). If \( 0 < b - a \), then \( 0 + a < (b - a) + a = b \) by (O3), that is, \( a < b \). This is the last claim. For (P1), let \( a, b > 0 \). Then \( 0 + b < a + b \) by (O3), so \( 0 < b < a + b \) and \( a + b > 0 \) by (O2); and \( ab > 0 \) by (O4). For (P2), let \( a \in R \). By (O1) exactly one of \( 0 < a \), \( a = 0 \), \( a < 0 \) holds, and by the last claim \( a < 0 \) holds exactly when \( 0 - a = -a \) is in \( P \). This proves the proposition.
:::

So an order on a commutative ring is the same thing as a positive set. For \( \nZ \), the natural one is the classes \( [(a, b)] \) with \( b < a \). Section 2.1 warned that "\( b < a \)" is a statement about **one** representative; we now check that it is a statement about the class.

## The order of the integers

::: {#def-integer-order}
[Order on the Integers]

Let \( S \coloneqq \{ (a, b) \in \nN \times \nN : b < a \} \), and
\[
P_{\nZ} \coloneqq \{ [(a, b)] : (a, b) \in S \} \subseteq \nZ .
\]
For \( x, y \in \nZ \), define \( x < y \) to mean \( y - x \in P_{\nZ} \).
:::

**Well-definedness.** By @thm-well-defined-on-classes (c), with \( X = \nN \times \nN \), it suffices that \( (a, b) \sim (a', b') \) and \( b < a \) imply \( b' < a' \). Write \( a = b + k \) with \( k \ne 0 \) (@prp-omega-order-arithmetic (a)). Then \( a + b' = b + a' \) reads \( (b' + k) + b = a' + b \) (@thm-omega-arithmetic-laws (b), (c)), and canceling \( b \) (@prp-omega-order-arithmetic (b)) gives \( a' = b' + k \), so \( b' < a' \). Hence, for **every** pair,
\[
[(a, b)] \in P_{\nZ} \iff b < a .
\]
So "positive" may be tested on any representative, as Section 2.1's warning required.

**Examples.** \( [(5, 2)] \in P_{\nZ} \), since \( 2 < 5 \); this is the integer \( 3 \). \( [(2, 5)] \notin P_{\nZ} \) and \( [(4, 4)] \notin P_{\nZ} \), since neither \( 5 < 2 \) nor \( 4 < 4 \). To compare \( x = [(3, 5)] \) and \( y = [(4, 1)] \): \( y - x = [(4, 1)] + [(5, 3)] = [(9, 4)] \), and \( 4 < 9 \), so \( x < y \), as "\( -2 < 3 \)" leads us to expect. The degenerate pair \( (0, 0) \) is not in \( S \), so \( 0 \notin P_{\nZ} \): zero is not positive.

::: {.check}
Is \( [(7, 10)] < [(2, 4)] \)?
:::

::: {.solution}
Compute \( [(2, 4)] - [(7, 10)] = [(2, 4)] + [(10, 7)] = [(12, 11)] \) by @def-integer-operations. Since \( 11 < 12 \), the difference lies in \( P_{\nZ} \), so yes: \( [(7, 10)] < [(2, 4)] \), which is \( -3 < -2 \).
:::

Recall from Section 2.2 that \( \nZ_{>0} \coloneqq \{ n \in \nN : n \ne 0 \} \), a set of natural numbers, inside \( \nZ \) through the identification \( n = \iota(n) \). The next theorem shows that it is exactly the set of positive integers.

::: {#thm-integers-ordered-ring}
[The Integers Form an Ordered Ring]

\( \nZ \), with the operations of @def-integer-operations and the relation \( < \) of @def-integer-order, is an ordered commutative ring, and its positive elements are exactly \( P_{\nZ} \). Moreover:

::: {.enumerate options="label=(\alph*)"}
1. for \( m, n \in \nN \), \( \iota(m) < \iota(n) \) if and only if \( m < n \);
2. \( \nN = \{ x \in \nZ : x \ge 0 \} \), and \( \nZ_{>0} = \{ x \in \nZ : x > 0 \} \);
3. (**discreteness**) there is no \( k \in \nZ \) with \( 0 < k < 1 \); hence, for \( m, n \in \nZ \) with \( m < n \), \( m + 1 \le n \).
:::
:::

::: {.idea}
By @prp-order-from-positives it is enough to check (P1) and (P2) for \( P_{\nZ} \), each a fact about \( \nN \), reached by reducing to the level below (@exm-method-reduce-to-level-below). For products, write \( a = b + k \), \( c = d + l \): the product's two coordinates differ by exactly \( kl \ne 0 \). (P2) is trichotomy in \( \nN \). Parts (a)–(c) follow from the positive classes being the \( [(k, 0)] \) with \( k \ne 0 \).
:::

::: {.proof}
By @thm-integers-commutative-ring, \( \nZ \) is a commutative ring. We check (P1) and (P2) of @prp-order-from-positives for \( P = P_{\nZ} \), using the criterion \( [(a, b)] \in P_{\nZ} \iff b < a \).

(P1), sums. Let \( x = [(a, b)] \) and \( y = [(c, d)] \) with \( b < a \) and \( d < c \). Then \( x + y = [(a + c, b + d)] \), and
\[
b + d < a + d < a + c
\]
by @prp-omega-order-arithmetic (c) twice (with commutativity), so \( b + d < a + c \) by transitivity (@thm-omega-order (a)). Hence \( x + y \in P_{\nZ} \).

(P1), products. With the same \( x, y \), write \( a = b + k \) and \( c = d + l \) with \( k, l \ne 0 \) (@prp-omega-order-arithmetic (a)). Then \( xy = [(ac + bd, ad + bc)] \), and expanding by @thm-omega-arithmetic-laws,
\[
\begin{aligned}
ac + bd &= (b + k)(d + l) + bd = bd + bl + kd + kl + bd , \\
ad + bc &= (b + k)d + b(d + l) = bd + kd + bd + bl .
\end{aligned}
\]
So \( ac + bd = (ad + bc) + kl \). Since \( k \ne 0 \) and \( l \ne 0 \), \( kl \ne 0 \) by @prp-omega-order-arithmetic (d), and therefore \( ad + bc < ac + bd \) by @prp-omega-order-arithmetic (a). Hence \( xy \in P_{\nZ} \).

(P2). Let \( x = [(a, b)] \). Then \( x \in P_{\nZ} \) if and only if \( b < a \). Next, \( x = [(0, 0)] \) if and only if \( (a, b) \sim (0, 0) \) (@fd2:thm-classes-partition (b)), that is, \( a + 0 = b + 0 \), that is, \( a = b \). Finally, \( -x = [(b, a)] \in P_{\nZ} \) if and only if \( a < b \). By trichotomy in \( \nN \) (@thm-omega-order (a)), exactly one of \( b < a \), \( a = b \), \( a < b \) holds. So exactly one of \( x \in P_{\nZ} \), \( x = 0 \), \( -x \in P_{\nZ} \) holds.

By @prp-order-from-positives, \( (\nZ, <) \) is an ordered commutative ring with positive set \( P_{\nZ} \).

(a) By @def-integer-operations, \( \iota(n) - \iota(m) = [(n, 0)] + [(0, m)] = [(n, m)] \), which lies in \( P_{\nZ} \) if and only if \( m < n \).

(b) If \( x = [(a, b)] > 0 \), then \( a = b + k \) with \( k \ne 0 \) (@prp-omega-order-arithmetic (a)), and \( x = [(k, 0)] = \iota(k) \) by @prp-integer-normal-form (a). Conversely, for \( k \ne 0 \), \( \iota(k) = [(k, 0)] \) is positive since \( 0 < k \) (@thm-omega-order (d)). So the positive integers are the \( \iota(k) \) with \( k \in \nZ_{>0} \); adding \( 0 = \iota(0) \) gives the first equation.

(c) If \( 0 < k \), then \( k = \iota(m) \) with \( m \ne 0 \) by (b), so \( 1 \le m \) (@thm-omega-order (d)) and \( 1 \le k \) by (a); then \( k < 1 \) would give \( 1 < 1 \) by (O2), or contradict (O1) directly. Now let \( m < n \). Then \( n - m > 0 \) (@prp-order-from-positives), so \( n - m \ge 1 \), and adding \( m \) by (O3) gives \( n \ge 1 + m \). This proves the theorem.
:::

With the identification of Section 2.2, (a) says that the order of \( \nZ \) **extends** the order of \( \nN \).

**Two non-examples by minimal change**, each breaking exactly one order axiom:

- Replace \( < \) by \( \le \). (O2)–(O4) still hold, by the axioms for \( < \) and the cases of equality (for (O4), \( ab = 0 \) when a factor is \( 0 \), by @prp-ring-algebra (b)). But (O1) fails at \( a = b = 0 \): both "\( 0 \le 0 \)" and "\( 0 = 0 \)" hold. The axioms describe a **strict** order.
- Reverse the order: \( a \prec b \) means \( b < a \). (O1)–(O3) hold, by the same axioms for \( < \). But (O4) fails: \( 0 \prec -1 \), since \( 0 - (-1) = 1 = [(1, 0)] \in P_{\nZ} \) (@prp-ring-algebra (a)), and \( (-1)(-1) = 1 \) (@prp-ring-algebra (c)), yet \( 0 \prec 1 \) is false, since \( 0 - 1 = [(0, 1)] \notin P_{\nZ} \). So (O4) fixes which way round the order goes.

## Rules for inequalities

The rules below hold in every ordered commutative ring: in \( \nZ \) now, and in \( \nQ \) once Section 3.2 orders it. One of them needs multiples first.

**Multiples.** Let \( R \) be a commutative ring and \( a \in R \). By @fd2:thm-recursion, read on \( \nN \) through @cor-omega-identification (b), with \( X = R \), starting value \( 0 \) and step \( (n, y) \mapsto y + a \), there is exactly one function \( \nN \to R \), written \( n \mapsto n \cdot a \), with
\[
0 \cdot a = 0 , \qquad (n + 1) \cdot a = n \cdot a + a \quad \text{for every } n \in \nN .
\]
So \( 1 \cdot a = a \) and \( 2 \cdot a = a + a \). From here to the end of the section, a dot with a natural number on its left means this multiple, and the product of two elements of \( R \) is written by juxtaposition, \( ab \). When \( R = \nZ \), the two readings agree, by @fd1:ax-induction (through @cor-omega-identification (b)): \( 0 \cdot a = 0 = 0a \) by @prp-ring-algebra (b) and (F6), and \( n \cdot a = na \) gives \( (n + 1) \cdot a = na + a = (n + 1)a \), since \( (n + 1)a = a(n + 1) = an + a = na + a \) by (F6), then (F9) with (F7), then (F6) (the sum \( n + 1 \) is the same in \( \nN \) and \( \nZ \) by @prp-naturals-embed-integers (a)).

::: {#prp-ordered-ring-rules}
[Rules for Inequalities in an Ordered Ring]

Let \( R \) be an ordered commutative ring, and let \( a, b, c, d \in R \).

::: {.enumerate options="label=(\alph*)"}
1. \( a < b \) if and only if \( b - a > 0 \), if and only if \( -b < -a \).
2. If \( a \le b \) and \( c \le d \), then \( a + c \le b + d \), and the conclusion is strict if one of the hypotheses is strict.
3. If \( a < b \) and \( c > 0 \), then \( ac < bc \).
4. If \( a < b \) and \( c < 0 \), then \( ac > bc \).
5. If \( a \ne 0 \), then \( a^2 > 0 \). If \( 1 \ne 0 \), then \( 1 > 0 \).
6. If \( ab = 0 \), then \( a = 0 \) or \( b = 0 \).
7. If \( a \ge 0 \) and \( b \ge 0 \), then \( a < b \) if and only if \( a^2 < b^2 \).
8. For every \( m, k \in \nN \), \( (m + k) \cdot a = m \cdot a + k \cdot a \). If \( 1 \ne 0 \), then \( n \cdot 1 > 0 \) for every \( n \in \nN \) with \( n \ge 1 \), and \( m \cdot 1 < n \cdot 1 \) whenever \( m, n \in \nN \) and \( m < n \).
9. \( \le \) is a total order on \( R \) (@fd2:def-partial-order), and its strict part is \( < \).
:::
:::

::: {.idea}
[Scratch work]

Every part is a comparison, and by @prp-order-from-positives a comparison \( a < b \) is the statement \( b - a > 0 \). Positive elements are closed under \( + \) and \( \cdot \). So the plan is always: write the goal as one difference, and build it from given positive elements. For (c):

| Givens | Goal |
|---|---|
| \( a < b \), \( c > 0 \) | \( ac < bc \) |
| \( b - a > 0 \), \( c > 0 \) (@prp-order-from-positives) | \( bc - ac > 0 \) |
| \( (b - a)c > 0 \) by (O4) | \( bc - ac = (b - a)c \)? |
| (F9), (F6), @prp-ring-algebra (c) | yes: the gap closes |

Part (d) is (c) with \( -c \) in place of \( c \); (e) and (f) apply (O4) to whichever of \( a \), \( -a \) is positive. We prove (i) first, since (b) and (g) use it.
:::

::: {.proof}
(i) Reflexivity is \( a = a \). Antisymmetry: \( a \le b \), \( b \le a \) and \( a \ne b \) give \( a < b < a \), so \( a < a \) by (O2), against (O1). Transitivity: if \( a \le b \le c \), either an equality holds and we substitute, or \( a < c \) by (O2); and \( a < c \) whenever one step is strict. Totality is (O1). Strict part: \( a < b \) implies \( a \ne b \) by (O1), and \( a \le b \), \( a \ne b \) give \( a < b \).

(a) The first equivalence is the last claim of @prp-order-from-positives. For the second, \( (-a) - (-b) = (-a) + b = b - a \) by @prp-ring-algebra (a) and (F1), so \( -b < -a \) also says \( b - a > 0 \).

(b) By (O3) (or equality) and (F1), \( a + c \le b + c \le b + d \); conclude by (i).

(c) By (a), \( b - a > 0 \). By (O4), \( (b - a)c > 0 \). By (F9), (F6) and @prp-ring-algebra (c), \( (b - a)c = bc + (-a)c = bc - ac \). So \( bc - ac > 0 \), and \( ac < bc \) by (a).

(d) By (a), \( c < 0 \) gives \( 0 - c = -c > 0 \). By (c) applied with \( -c \), \( a(-c) < b(-c) \), that is, \( -(ac) < -(bc) \) by @prp-ring-algebra (c), and then \( bc < ac \) by (a) together with \( -(-x) = x \).

(e) If \( a > 0 \), then \( a^2 = aa > 0 \) by (O4). If \( a < 0 \), then \( -a > 0 \) as in (d), and \( a^2 = (-a)(-a) > 0 \) by @prp-ring-algebra (c) and (O4). By (O1) one of the two cases occurs when \( a \ne 0 \). If \( 1 \ne 0 \), then \( 1 = 1^2 > 0 \).

(f) Contrapositive: let \( a, b \ne 0 \). By (O1) and (a), some \( a' \in \{ a, -a \} \) and \( b' \in \{ b, -b \} \) are positive, so \( a'b' > 0 \) by (O4). By @prp-ring-algebra (c), \( a'b' \) is \( ab \) or \( -(ab) \); if \( ab = 0 \), both are \( 0 \), against (O1). So \( ab \ne 0 \).

(g) Let \( a, b \ge 0 \). (\( \Rightarrow \)) If \( a < b \), then \( b > 0 \) by (i), and (c) gives \( ab < b^2 \). Also \( a^2 \le ab \): by (c) if \( a > 0 \), and by @prp-ring-algebra (b) if \( a = 0 \). So \( a^2 < b^2 \) by (i). (\( \Leftarrow \)) If \( a^2 < b^2 \) but not \( a < b \), then \( b = a \) or \( b < a \) by (O1), giving \( a^2 = b^2 \) or, by (\( \Rightarrow \)), \( b^2 < a^2 \); both contradict (O1).

(h) Fix \( m \in \nN \). We prove the sum law by @fd1:ax-induction on \( k \) (through @cor-omega-identification (b)), for \( P(k) \): "\( (m + k) \cdot a = m \cdot a + k \cdot a \)". The base case is \( (m + 0) \cdot a = m \cdot a + 0 \cdot a \), by @def-omega-arithmetic (a), (F3) and \( 0 \cdot a = 0 \). For the step, \( P(k) \) gives \( (m + (k + 1)) \cdot a = (m + k) \cdot a + a = (m \cdot a + k \cdot a) + a = m \cdot a + (k + 1) \cdot a \), by associativity in \( \nN \) (@thm-omega-arithmetic-laws (c)) with the definition of multiples, \( P(k) \), and (F2) with the definition of multiples again.

Now let \( 1 \ne 0 \). By @fd1:ax-induction on \( n \), for \( Q(n) \): "\( (n + 1) \cdot 1 > 0 \)": the base is \( 1 \cdot 1 = 0 + 1 = 1 > 0 \) by (e), and the step is \( (n + 2) \cdot 1 = (n + 1) \cdot 1 + 1 > 0 \) by (b) and (e). Every \( n \ge 1 \) in \( \nN \) is \( j + 1 \) for some \( j \) (@prp-omega-order-arithmetic (a)), so \( n \cdot 1 > 0 \). Finally, if \( m < n \), then \( n = m + k \) with \( k \ne 0 \) (@prp-omega-order-arithmetic (a)), so \( k \ge 1 \) (@thm-omega-order (d)), and by the sum law and (b),
\[
n \cdot 1 = m \cdot 1 + k \cdot 1 > m \cdot 1 + 0 = m \cdot 1 .
\]
This proves the proposition.
:::

The school rules for inequalities between integers are now theorems about \( \nZ \). The hypothesis \( 1 \ne 0 \) in (e) and (h) cannot be dropped: in the zero ring with the empty order, neither \( 1 > 0 \) nor \( 1 \cdot 1 > 0 \) holds.

::: {#exm-method-one-positive-element}
[Method: turn the comparison into one positive element]

**Template.** To prove an inequality in an ordered ring: (1) rewrite the goal \( u < v \) as \( v - u > 0 \) (@prp-order-from-positives); (2) express \( v - u \) by the ring laws as a sum or product of elements known to be positive (or non-negative); (3) conclude by closure, (P1), or by @prp-ordered-ring-rules (b), (c); (4) translate back.

**When to use it.** Any rule for inequalities; comparisons in \( \nZ \) and, later, in every ordered field.

**The usual failure.** Multiplying by an element whose sign is unknown; treating \( \le \) as \( < \) in (O4); using a picture of the number line as a reason.
:::

::: {.warning}
(O4) and (c) are about multiplying by something **positive**. The tempting rule "if \( a < b \) and \( c < d \), then \( ac < bd \)" is false in \( \nZ \): \( -3 < -1 \) and \( -3 < -1 \), yet \( (-3)(-3) = 9 \) and \( (-1)(-1) = 1 \), and \( 9 > 1 \).
:::

With both smaller sides non-negative, the method gives a correct rule.

::: {#exm-product-of-inequalities}
[Multiplying two inequalities]

Let \( R \) be an ordered commutative ring, and let \( a, b, c, d \in R \) with \( 0 \le a < b \) and \( 0 \le c < d \). Prove that \( ac < bd \).
:::

::: {.solution}
By the method, the goal is \( bd - ac > 0 \). Write the difference through elements of known sign:
\[
bd - ac = b(d - c) + (b - a)c .
\]
Indeed, \( b(d - c) = bd - bc \) and \( (b - a)c = bc - ac \), by (F9), (F6) and @prp-ring-algebra (c); adding, the terms \( -bc \) and \( bc \) cancel by (F1), (F2), (F4) and (F3), leaving \( bd - ac \).

Now the signs. From \( 0 \le a \) and \( a < b \) we get \( 0 < b \) (@prp-ordered-ring-rules (i)), and \( d - c > 0 \) since \( c < d \) (@prp-ordered-ring-rules (a)). So \( b(d - c) > 0 \) by (O4). Likewise \( b - a > 0 \). If \( c > 0 \), then \( (b - a)c > 0 \) by (O4); if \( c = 0 \), then \( (b - a)c = 0 \) by @prp-ring-algebra (b). Either way \( (b - a)c \ge 0 \).

A positive element plus a non-negative one is positive: by @prp-ordered-ring-rules (b), with the strict hypothesis \( 0 < b(d - c) \), we get \( 0 = 0 + 0 < b(d - c) + (b - a)c = bd - ac \), where \( 0 + 0 = 0 \) is (F3). By @prp-ordered-ring-rules (a), \( ac < bd \).
:::

The hypotheses \( a \ge 0 \) and \( c \ge 0 \) are exactly what make the two summands non-negative; the warning shows what goes wrong without them.

::: {.check}
Which positive element shows that \( a < b \) gives \( a + a < b + b \)?
:::

::: {.solution}
The element \( b - a \), taken twice: \( (b + b) - (a + a) = (b - a) + (b - a) \) by the ring laws (regrouping by (F1), (F2), with \( -(a + a) = (-a) + (-a) \) as in the proof of @prp-order-from-positives). It is a sum of two positive elements, so it is positive by (P1), and \( a + a < b + b \) by @prp-ordered-ring-rules (a).
:::

::: {.check}
Is \( \nZ \) a field?
:::

::: {.solution}
No: \( 1 + 1 \) is non-zero (it is \( > 1 > 0 \)) and has no inverse. Suppose \( (1 + 1)x = 1 \). Since \( (1 + 1)x = x(1 + 1) = x + x \) by (F6), (F9) and (F7), this says \( x + x = 1 \). If \( x \le 0 \), then \( x + x \le 0 < 1 \) by @prp-ordered-ring-rules (b), (e). If \( x > 0 \), then \( x \ge 1 \) by discreteness (@thm-integers-ordered-ring (c)), so \( x + x \ge 1 + 1 > 1 \) by @prp-ordered-ring-rules (b), (e). Both contradict \( x + x = 1 \) by (O1).
:::

## Least elements, and a ring that cannot be ordered

The natural numbers are well ordered (@thm-omega-well-ordering); the integers are not, since \( x - 1 < x \) for every \( x \). But a set of integers bounded below can be shifted into \( \nN \).

::: {#prp-integer-least-element}
[Least and Greatest Elements of Sets of Integers]

Let \( S \subseteq \nZ \) be **non-empty**. If \( S \) has a lower bound \( b \in \nZ \) (that is, \( b \le s \) for every \( s \in S \)), then \( S \) has a least element. If \( S \) has an upper bound \( c \in \nZ \), then \( S \) has a greatest element.
:::

::: {.idea}
This is @fd2:cor-well-ordering-integers on the constructed \( \nZ \), by the same shift into \( \nN \), with @thm-omega-well-ordering in place of @fd2:thm-well-ordering.
:::

::: {.proof}
Let \( b \) be a lower bound and \( T \coloneqq \{ s - b : s \in S \} \), a non-empty set. For \( s \in S \), \( s \ge b \) gives \( s - b \ge 0 \) by (O3), so \( T \subseteq \{ x \in \nZ : x \ge 0 \} = \nN \) by @thm-integers-ordered-ring (b). By @thm-omega-well-ordering, \( T \) has an element \( m \) with \( m \le t \) for every \( t \in T \), in the order of \( \nN \) and so in that of \( \nZ \) (@thm-integers-ordered-ring (a)). Then \( m = s_0 - b \) for some \( s_0 \in S \), so \( m + b = s_0 \in S \); and for \( s \in S \), \( s - b \ge m \) gives \( s \ge m + b \) by (O3). So \( m + b \) is least in \( S \).

If \( c \) is an upper bound, then \( -S \coloneqq \{ -s : s \in S \} \) has the lower bound \( -c \) (@prp-ordered-ring-rules (a)), so by the first part it has a least element, which is \( -s_1 \) for some \( s_1 \in S \), by the definition of \( -S \). For \( s \in S \), \( -s_1 \le -s \) gives \( s \le s_1 \), by @prp-ordered-ring-rules (a), or by \( -(-s) = s \) (@prp-ring-algebra (a)) when \( -s_1 = -s \). So \( s_1 \) is greatest in \( S \). This proves the proposition.
:::

Both hypotheses are needed: \( \nZ \) has no least element, and neither has \( \emptyset \), which every integer bounds. The rules of @prp-ordered-ring-rules also show that some rings carry no order at all.

::: {#exm-finite-ring-not-orderable}
[A field with two elements that cannot be ordered]

Let \( R \coloneqq \{0, 1\} \), two distinct elements, with addition and multiplication given by the tables
\[
\begin{array}{c|cc}
{+} & 0 & 1 \\ \hline
0 & 0 & 1 \\
1 & 1 & 0
\end{array}
\qquad\qquad
\begin{array}{c|cc}
\cdot & 0 & 1 \\ \hline
0 & 0 & 0 \\
1 & 0 & 1
\end{array}
\]
Check that \( R \) satisfies (F1)–(F9), so that it is a field, and show that no relation \( < \) on \( R \) makes it an ordered commutative ring.
:::

::: {.solution}
*The axioms.* (F1), (F6): both tables are symmetric. (F3), (F7): the row of \( 0 \) in the first table and of \( 1 \) in the second repeat the headings. (F4): \( -0 = 0 \) and \( -1 = 1 \), since \( 1 + 1 = 0 \). (F8): \( 1 \) has inverse \( 1 \), since the second table gives the product of \( 1 \) and \( 1 \) as \( 1 \). And \( 1 \ne 0 \).

The three laws with three variables can be checked over the eight triples \( (a, b, c) \), or by cases. From the tables, \( 0x = 0 \) and \( 1x = x \), and \( x + y = 1 \) exactly when exactly one of \( x, y \) is \( 1 \). (F2): both sides are \( 1 \) exactly when an odd number of \( a, b, c \) (one or three) are \( 1 \). (F5): both sides are \( 1 \) exactly when \( a = b = c = 1 \). (F9): if \( a = 0 \), both sides are \( 0 \); if \( a = 1 \), both sides are \( b + c \). So \( R \) is a field.

*No order.* If \( < \) made \( R \) an ordered commutative ring, then, as \( 1 \ne 0 \), @prp-ordered-ring-rules (h) would give \( 2 \cdot 1 > 0 \). But \( 2 \cdot 1 = 1 \cdot 1 + 1 = (0 + 1) + 1 = 0 \) by the definition of multiples, and \( 0 > 0 \) is forbidden by (O1).
:::

The argument uses only \( 1 \ne 0 \) and \( n \cdot 1 = 0 \) for some \( n \ge 1 \). So **no commutative ring with \( 1 \ne 0 \) in which \( n \cdot 1 = 0 \) for some \( n \in \nN \), \( n \ge 1 \), can be ordered**. The integers modulo \( n \ge 2 \) of *Sets and Functions*, Section 5.2 are such rings (their ring laws taken for granted, as in the warning after @def-commutative-ring-and-field), since \( n \cdot [1] = [n] = [0] \); *Algebraic Preliminaries*, Chapter 1 rebuilds them on the constructed \( \nZ \).

## Exercises

### A. Check your understanding

::: {#exr-ordered-rings-a1}
[A1]

Let \( R \) be an ordered commutative ring.

::: {.enumerate options="label=(\alph*)"}
1. Here is a proof that if \( a < 0 < b \), then \( ab < a^2 + b^2 \). Name the axiom, rule or result that justifies each of the five steps. (1) \( ab < 0b \). (2) \( 0b = 0 \). (3) \( a^2 > 0 \) and \( b^2 > 0 \). (4) \( a^2 + b^2 > 0 + 0 = 0 \). (5) \( ab < a^2 + b^2 \).
2. True or false: "\( R \) has no zero divisors." Give a reason.
3. True or false: "\( 1 > 0 \) in every ordered commutative ring." Give a reason.
4. Use the method of @exm-method-one-positive-element to show: if \( a < b \) and \( c \le 0 \), then \( ac \ge bc \).
:::
:::

::: {.solution}
(a) (1) @prp-ordered-ring-rules (c), with \( a < 0 \) and \( b > 0 \). (2) @prp-ring-algebra (b) and (F6). (3) @prp-ordered-ring-rules (e), as \( a, b \ne 0 \) by (O1). (4) @prp-ordered-ring-rules (b), strict, and (F3). (5) (O2).

(b) True, by @prp-ordered-ring-rules (f); a general commutative ring may have zero divisors (the warning after @def-commutative-ring-and-field).

(c) False: in the zero ring with the empty relation, \( 1 = 0 \). It is true when \( 1 \ne 0 \) (@prp-ordered-ring-rules (e)).

(d) By the method, compute the difference \( ac - bc \). By (F9), (F6) and @prp-ring-algebra (c), \( ac - bc = (a - b)c \); and \( a - b = -(b - a) \) (the first identity in the proof of @prp-order-from-positives), so \( (a - b)c = (-(b - a))c = (b - a)(-c) \) by @prp-ring-algebra (c). Here \( b - a > 0 \) by @prp-ordered-ring-rules (a). If \( c < 0 \), then \( -c > 0 \) (@prp-ordered-ring-rules (a), as \( 0 - c = -c \)), and the product is \( > 0 \) by (O4). If \( c = 0 \), then \( -c = 0 \) and the product is \( 0 \) by @prp-ring-algebra (b). So \( ac - bc \ge 0 \): either \( bc < ac \) by @prp-ordered-ring-rules (a), or \( ac - bc = 0 \), that is, \( ac = bc \). In both cases \( bc \le ac \), that is, \( ac \ge bc \).
:::

### B. Practice

::: {#exr-ordered-rings-b2}
[B1: The wrong positive set]

Let \( P' \coloneqq \{ [(a, b)] : a < b \} \subseteq \nZ \). Show that membership in \( P' \) does not depend on the representative, that \( P' \) satisfies (P2) of @prp-order-from-positives, and that it does not satisfy (P1). Which part of (P1) fails?
:::

::: {.solution}
*Independence of representatives.* If \( (a, b) \sim (a', b') \) and \( b = a + k \) with \( k \ne 0 \), then \( b' + a = a + b' = b + a' = (a + k) + a' = (a' + k) + a \) (@thm-omega-arithmetic-laws (b), (c)), so \( b' = a' + k \) by cancellation (@prp-omega-order-arithmetic (b)), and \( a' < b' \) by @prp-omega-order-arithmetic (a). By @thm-well-defined-on-classes (c), \( [(a, b)] \in P' \) if and only if \( a < b \).

*(P2).* For \( x = [(a, b)] \): \( x \in P' \) iff \( a < b \); \( x = 0 \) iff \( a = b \) (as in the proof of @thm-integers-ordered-ring); \( -x \in P' \) iff \( b < a \). By trichotomy in \( \nN \) (@thm-omega-order (a)), exactly one holds.

*(P1) fails for products.* \( [(0, 1)] \in P' \), but, by @def-integer-operations with \( a = c = 0 \) and \( b = d = 1 \) in \( [(ac + bd, \ ad + bc)] \),
\[
[(0, 1)][(0, 1)] = [(1, 0)] ,
\]
and \( [(1, 0)] \notin P' \), since \( 1 < 0 \) is false. The sum half of (P1) holds, as in the proof of @thm-integers-ordered-ring. So \( P' \), the negative integers, fails only closure under products; it would define the reversed order, which breaks exactly (O4).
:::

::: {#exr-ordered-rings-b3}
[B2: Prove or disprove]

Prove or disprove.

::: {.enumerate options="label=(\alph*)"}
1. In every ordered commutative ring, \( a < b \) implies \( a^2 < b^2 \).
2. In every ordered commutative ring with \( 1 \ne 0 \), \( a^2 + 1 > 0 \).
3. In \( \nZ \), if \( x > 0 \) and \( xy = x \), then \( y = 1 \).
4. In every ordered commutative ring, \( a < b \) and \( c < d \) imply \( a - d < b - c \).
5. In \( \nZ \), \( x < y \) implies \( x + 1 < y \).
:::
:::

::: {.solution}
(a) **False.** In \( \nZ \), \( -3 < 1 \), but \( (-3)^2 = 9 \) and \( 1^2 = 1 \), and \( 9 > 1 \). The true version needs \( a \ge 0 \) (@prp-ordered-ring-rules (g)).

(b) **True.** First, \( a^2 \ge 0 \): if \( a = 0 \), then \( a^2 = 0 \cdot 0 = 0 \) by @prp-ring-algebra (b); otherwise \( a^2 > 0 \) by @prp-ordered-ring-rules (e). Next, \( 1 > 0 \) by @prp-ordered-ring-rules (e), since \( 1 \ne 0 \). By @prp-ordered-ring-rules (b), with the strict hypothesis \( 0 < 1 \), \( 0 = 0 + 0 < a^2 + 1 \), using (F3).

(c) **True.** By (F9), (F7) and @prp-ring-algebra (c), \( x(y - 1) = xy + x(-1) = xy - x \), and \( xy - x = x - x = 0 \) by the hypothesis and (F4). Since \( x > 0 \), \( x \ne 0 \) by (O1). So \( y - 1 = 0 \) by @prp-ordered-ring-rules (f), and \( y = (y - 1) + 1 = 1 \) by (F1)–(F4).

(d) **True.** From \( c < d \), @prp-ordered-ring-rules (a) gives \( -d < -c \). Adding this to \( a < b \) by @prp-ordered-ring-rules (b), strict, gives \( a + (-d) < b + (-c) \), that is, \( a - d < b - c \).

(e) **False.** Take \( x = 0 \) and \( y = 1 \): then \( x < y \) (@prp-ordered-ring-rules (e), as \( 1 \ne 0 \) in \( \nZ \) by @thm-integers-commutative-ring), but \( x + 1 = 1 \), and \( 1 < 1 \) is ruled out by (O1). Discreteness gives only \( x + 1 \le y \) (@thm-integers-ordered-ring (c)).
:::

### C. Going deeper

::: {#exr-ordered-rings-c1}
[C1: Ordered rings with \( 1 \ne 0 \) are infinite]

::: {.enumerate options="label=(\alph*)"}
1. Prove the sum law of @prp-ordered-ring-rules (h) in full: for every ordered commutative ring \( R \), every \( a \in R \) and all \( m, k \in \nN \), \( (m + k) \cdot a = m \cdot a + k \cdot a \). State the property you induct on and justify every equality.
2. Deduce that every ordered commutative ring with \( 1 \ne 0 \) is infinite (@fd2:def-infinite).
3. The set \( \{0, 1, 2\} \) with addition and multiplication "modulo \( 3 \)", given by the tables below, is a commutative ring with \( 1 \ne 0 \) (you may take this for granted). Show that it cannot be ordered.
:::

\[
\begin{array}{c|ccc}
{+} & 0 & 1 & 2 \\ \hline
0 & 0 & 1 & 2 \\
1 & 1 & 2 & 0 \\
2 & 2 & 0 & 1
\end{array}
\qquad\qquad
\begin{array}{c|ccc}
\cdot & 0 & 1 & 2 \\ \hline
0 & 0 & 0 & 0 \\
1 & 0 & 1 & 2 \\
2 & 0 & 2 & 1
\end{array}
\]
:::

::: {.solution}
[Hint 1]

For (b): what does (h) say about \( k \mapsto k \cdot 1 \)?
:::

::: {.solution}
[Hint 2]

Suppose \( R \) has \( m \) elements; consider \( k \mapsto k \cdot 1 \) on \( \{1, \dots, m + 1\} \).
:::

::: {.solution}
(a) Fix \( R \), \( a \in R \), \( m \in \nN \), and use @fd1:ax-induction (through @cor-omega-identification (b)) on \( k \), for \( P(k) \): "\( (m + k) \cdot a = m \cdot a + k \cdot a \)". *Base:* \( (m + 0) \cdot a = m \cdot a = m \cdot a + 0 = m \cdot a + 0 \cdot a \), by @def-omega-arithmetic (a), (F3) and \( 0 \cdot a = 0 \). *Step:* assume \( P(k) \). Then
\[
\begin{aligned}
(m + (k + 1)) \cdot a &= ((m + k) + 1) \cdot a = (m + k) \cdot a + a \\
&= (m \cdot a + k \cdot a) + a = m \cdot a + (k \cdot a + a) \\
&= m \cdot a + (k + 1) \cdot a ,
\end{aligned}
\]
by associativity in \( \nN \) (@thm-omega-arithmetic-laws (c)), the recursion for multiples, \( P(k) \), (F2), and the recursion again. So \( P(k + 1) \) holds, and \( P(k) \) holds for every \( k \).

(b) Let \( 1 \ne 0 \) in \( R \), and suppose \( R \) has \( m \) elements for some \( m \in \nN \) (@fd2:def-finite). Let \( f \colon \{1, \dots, m + 1\} \to R \), \( f(k) \coloneqq k \cdot 1 \). If \( k < l \), then \( k \cdot 1 < l \cdot 1 \) by @prp-ordered-ring-rules (h), so \( k \cdot 1 \ne l \cdot 1 \) by (O1): \( f \) is injective. But \( \{1, \dots, m + 1\} \) has \( m + 1 > m \) elements (by its identity map), so @fd2:cor-pigeonhole-finite-sets (a) forbids an injection into \( R \). This contradiction shows that \( R \) is infinite (@fd2:def-infinite).

(c) By the definition of multiples and the tables, \( 1 \cdot 1 = 0 + 1 = 1 \), \( 2 \cdot 1 = 1 + 1 = 2 \) and \( 3 \cdot 1 = 2 + 1 = 0 \). An order would give \( 3 \cdot 1 > 0 \) by @prp-ordered-ring-rules (h), since \( 1 \ne 0 \), that is, \( 0 > 0 \), against (O1). (Alternatively, (b) applies to this finite ring.)

**Marking scheme.** (10 points)
- 1: (a) states the induction property with \( m \) and \( a \) fixed and \( k \) the induction variable.
- 2: (a) base case, citing \( m + 0 = m \), \( 0 \cdot a = 0 \) and (F3).
- 2: (a) inductive step, with associativity in \( \nN \), the recursion, the hypothesis and (F2) each named.
- 2: (b) shows that \( k \mapsto k \cdot 1 \) is injective, citing (h) and (O1).
- 2: (b) derives the contradiction from @fd2:cor-pigeonhole-finite-sets (a) with \( m + 1 > m \) elements (or any correct count).
- 1: (c) computes \( 3 \cdot 1 = 0 \) and concludes.
Fatal errors (0 for the step): inducting on \( m \) and \( k \) at once without fixing one; using \( 1 > 0 \) without \( 1 \ne 0 \); in (b), "the multiples are all different, so there are infinitely many" with no finiteness result cited (@fd2:cor-pigeonhole-finite-sets, @fd2:prp-subset-finite with \( \nN \) infinite, or equivalent). A route for (b) composing the inverse of a bijection \( \{1, \dots, m\} \to R \) with \( f \) earns the same 4 points. So does a route that shows \( k \mapsto k \cdot 1 \) is an injection \( \nN \to R \) (2 points, as above), so that its image is an infinite subset of \( R \), and concludes with @fd2:prp-subset-finite (2 points).
:::

<!-- dependency ledger
def-ordered-ring-and-field (claim): prose pointer before the definition, (O1)-(O4) match the ordered fields of AN1.1 (with "field" relaxed to "commutative ring") | AN1.1 (prose pointer; nothing here depends on it)
exm-finite-ring-not-orderable (claim): the remark after it, that the integers modulo n >= 2 form a commutative ring with [1] != [0] and n.[1] = [n] = [0] | ring laws as for the modulo-6 example (not proved here, marked in the text); [1] != [0] since n does not divide 1; k.[1] = [k] by induction on the recursion for multiples; illustration only; F5.1 (*Algebraic Preliminaries*, Chapter 1) rebuilds it on the constructed Z
prp-ordered-ring-rules (solution): the Quick check "Is Z a field?" uses (1 + 1)x = x + x | def-commutative-ring-and-field (F6), (F9), (F7) (cited inline)
prp-order-from-positives (proof): -(b - a) = a - b, (c - b) + (b - a) = c - a, -(a + c) = (-a) + (-c), -0 = 0 | inline (from prp-ring-algebra (a))
thm-integers-ordered-ring (proof): (a, b) ~ (0, 0) iff a = b | def-integers-as-classes with def-omega-arithmetic (a) (cited)
prp-ordered-ring-rules (proof): the multiples n.a exist and are unique | thm-recursion via cor-omega-identification (b) (cited before the statement)
prp-ordered-ring-rules (proof): a natural number n >= 1 is j + 1 for some j | prp-omega-order-arithmetic (a) (cited), with 1 + j = j + 1 by thm-omega-arithmetic-laws (b)
prp-integer-least-element (proof): T = {s - b : s in S} is a set | image of S under s |-> s - b (F2.1, def-image); not cited by label
prp-integer-least-element (proof): -S = {-s : s in S} is a set | image of S under s |-> -s (F2.1, def-image); not cited by label
exm-finite-ring-not-orderable (solution): (F2), (F5), (F9) for the two-element tables | inline case argument from the tables (0x = 0, 1x = x, x + y = 1 iff exactly one of x, y is 1)
exr-ordered-rings-c1 (solution): {1, ..., m + 1} has m + 1 elements | def-finite (identity bijection; inline)
exm-product-of-inequalities (solution): bd - ac = b(d - c) + (b - a)c | inline from (F1)-(F4), (F6), (F9) and prp-ring-algebra (c) (cited)
prp-ordered-ring-rules (solution): the Quick check after exm-product-of-inequalities, (b + b) - (a + a) = (b - a) + (b - a) | inline regrouping by (F1), (F2), with -(a + a) = (-a) + (-a) from prp-ring-algebra (a) as in the proof of prp-order-from-positives (cited)
exr-ordered-rings-a1 (solution): (d) a - b = -(b - a) | the first identity in the proof of prp-order-from-positives (cited)
exr-ordered-rings-b3 (solution): (a) in Z, -3 < 1, (-3)^2 = 9, 1^2 = 1, 1 < 9 | prp-ring-algebra (c) ((-3)(-3) = 3 . 3), def-integer-operations on representatives (numeral products in N), thm-integers-ordered-ring (a) for the comparisons; numerals as in the warning
exr-ordered-rings-b3 (solution): (c) y = (y - 1) + 1 | regrouping by (F1)-(F4) (cited)
-->
