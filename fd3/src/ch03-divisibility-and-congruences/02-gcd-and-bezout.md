# The Greatest Common Divisor, Bézout, and the Euclidean Algorithm

Section 3.1 gave the constructed integers a relation \( a \mid b \) and a division with remainder (@thm-integers-division-remainder). This section asks what two integers have in common. Here is a concrete version. A machine accepts only coins worth \( 12 \) and \( 42 \) units, and gives change in the same coins. Which amounts can be paid exactly? Paying \( x \) coins of the first kind and \( y \) of the second, with negative numbers for coins received as change, pays \( 12x + 42y \). So \( 42 - 3 \cdot 12 = 6 \) can be paid, and hence every multiple of \( 6 \); and since \( 6 \) divides both \( 12 \) and \( 42 \), nothing else can. Why \( 6 \), and why exactly the multiples of \( 6 \)? The answer is a theorem about every pair of integers, and its proof is the main move of this chapter.

## Integer combinations

The amounts \( 12x + 42y \) form a set that deserves a name.

::: {#def-integer-linear-combinations}
[Integer Combinations]

Let \( a, b, n \in \nZ \). The set of **integer combinations** of \( a \) and \( b \) is
\[
a\nZ + b\nZ \coloneqq \{ ax + by : x, y \in \nZ \} ,
\]
and the set of **multiples** of \( n \) is \( n\nZ \coloneqq \{ kn : k \in \nZ \} \).
:::

So \( n\nZ \) is the set of \( m \in \nZ \) with \( n \mid m \) (@fd2:def-divides), and \( a\nZ + b\nZ \) is written as one symbol: it is defined directly, not as a sum of two sets. Three closure properties hold for every \( a, b \in \nZ \). For \( x, y, x', y', m \in \nZ \), the ring laws of @thm-integers-commutative-ring and @prp-ring-algebra (c) give
\[
\begin{aligned}
(ax + by) + (ax' + by') &= a(x + x') + b(y + y'), \\
-(ax + by) &= a(-x) + b(-y), \\
m(ax + by) &= a(mx) + b(my),
\end{aligned}
\]
so \( a\nZ + b\nZ \) is closed under \( + \), under \( - \), and under multiplication by **any** integer. It contains \( 0 = a \cdot 0 + b \cdot 0 \), \( a = a \cdot 1 + b \cdot 0 \) and \( b = a \cdot 0 + b \cdot 1 \). Taking \( b = 0 \) gives \( n\nZ + 0\nZ = \{ nx + 0y \} = \{ xn : x \in \nZ \} = n\nZ \), by @prp-ring-algebra (b) and (F6); so \( n\nZ \) has the same three properties.

Examples:

- \( 12\nZ + 42\nZ \) contains \( 12 \), \( 42 \), \( 30 = 42 - 12 \) and \( 6 = 12 \cdot (-3) + 42 \cdot 1 \), so it contains every multiple of \( 6 \), by the third closure property.
- \( 2\nZ + 3\nZ = \nZ \): it contains \( 1 = 2 \cdot (-1) + 3 \cdot 1 \), and with it \( m \cdot 1 = m \) for every \( m \in \nZ \).
- The degenerate case: \( 0\nZ + 0\nZ = \{0\} \) (the case \( n = 0 \) above, since \( 0\nZ = \{ k \cdot 0 : k \in \nZ \} = \{0\} \) by @prp-ring-algebra (b)). It is the only case in which \( a\nZ + b\nZ \) has no positive element (if \( a \ne 0 \), one of \( a \), \( -a \) is a positive element, by @prp-divisibility-rules-integers (h); likewise for \( b \)), and the theorem below must exclude it.

*Non-example by minimal change.* Allow only paying, with no change given: \( \{ 12x + 42y : x, y \in \nN \} \). It contains \( 12 \) and \( 42 \) and is closed under \( + \), but not under \( - \): it contains no negative integer, since \( x, y \ge 0 \) give \( 12x + 42y \ge 0 \). Nor does it contain \( 6 \): a non-zero element has \( x \ge 1 \) or \( y \ge 1 \), so it is at least \( 12 \). The coefficients must range over all of \( \nZ \).

## The greatest common divisor

An integer \( d \) is a **common divisor** of \( a \) and \( b \) if \( d \mid a \) and \( d \mid b \). Every pair has the common divisor \( 1 \) (@prp-divisibility-rules-integers (a)). For the coins, \( 6 \) is a common divisor of \( 12 \) and \( 42 \), and the question was why it is the one that matters.

*The greatest common divisor is the largest integer that divides both.*

::: {#def-integer-gcd}
[Greatest Common Divisor]

Let \( a, b \in \nZ \). If \( (a, b) \ne (0, 0) \), the **greatest common divisor** \( \gcd(a, b) \) is the greatest element, for \( \le \), of the set of common divisors of \( a \) and \( b \). We set \( \gcd(0, 0) \coloneqq 0 \).
:::

In words: among all integers dividing both \( a \) and \( b \), take the largest. The definition says "the greatest element", so it owes us a proof that there is one.

*Well-definedness.* Let \( (a, b) \ne (0, 0) \), and let \( D \) be the set of common divisors of \( a \) and \( b \). It is non-empty, since \( 1 \in D \). Say \( a \ne 0 \) (otherwise \( b \ne 0 \), and the same argument runs with \( b \)). By @prp-divisibility-rules-integers (h), one of \( a \), \( -a \) is positive; call it \( c \). Every \( d \in D \) satisfies \( d \le c \): if \( d > 0 \), then \( d \mid c \) by @prp-divisibility-rules-integers (d), and \( d \le c \) by @prp-divisibility-rules-integers (e); if \( d \le 0 \), then \( d \le 0 < c \). So \( D \) is bounded above, and by @prp-integer-least-element it has a greatest element. Since \( 1 \in D \), that element is at least \( 1 \). Hence **\( \gcd(a, b) \ge 1 \) whenever \( (a, b) \ne (0, 0) \)**, and \( \gcd(a, b) = \gcd(b, a) \), since the condition "\( d \mid a \) and \( d \mid b \)" is symmetric in \( a \) and \( b \).

Examples:

- \( \gcd(4, 6) = 2 \). A positive common divisor \( d \) satisfies \( d \le 4 \), by @prp-divisibility-rules-integers (e), and \( d \ge 1 \), so \( d \in \{1, 2, 3, 4\} \) by discreteness (@thm-integers-ordered-ring (c)), as in the small-primes remark of Section 3.1. Now \( 4 \nmid 6 \) and \( 3 \nmid 4 \), because \( 6 = 1 \cdot 4 + 2 \) and \( 4 = 1 \cdot 3 + 1 \) have non-zero remainders (the divisibility test after @thm-integers-division-remainder), while \( 2 \) divides both. So the greatest common divisor is \( 2 \).
- \( \gcd(-5, 5) = 5 \): the common divisors of \( -5 \) and \( 5 \) are the divisors of \( 5 \) (@prp-divisibility-rules-integers (d) and @prp-ring-algebra (a)), and the greatest is \( 5 \), by @prp-divisibility-rules-integers (e).
- \( \gcd(1, b) = 1 \) for every \( b \in \nZ \): a common divisor \( d \) divides \( 1 \), so \( d = \pm 1 \) (@prp-divisibility-rules-integers (g)), and the greater is \( 1 \).

*Why the convention for \( (0, 0) \).* Every integer divides \( 0 \), so \( 0 \) and \( 0 \) have no greatest common divisor for \( \le \), and some value has to be chosen. The value \( 0 \) is the one that keeps clauses (c) and (e) of the theorem below true for \( (0, 0) \), as the remark after it shows. It also matches @fd2:exm-divisibility-lcm of *Sets, Relations, and Cardinality*, Section 2.6, where \( 0 \) is the top of \( (\nN, \mid) \), divisible by everything.

Listing divisors one by one, as in the first example, is slow. The Euclidean algorithm below replaces the list by one division per step, and Bézout's theorem is what makes it work.

## Bézout's theorem

Here is the answer to the coin question for every pair of integers: the payable amounts are exactly the multiples of the greatest common divisor, and the greatest common divisor is itself payable.

::: {#thm-integers-bezout}
[Bézout's Theorem]

Let \( a, b \in \nZ \), not both \( 0 \), and let \( S \coloneqq (a\nZ + b\nZ) \cap \nZ_{>0} \).

::: {.enumerate options="label=(\alph*)"}
1. \( S \) has a least element \( d \), and \( d = ax_0 + by_0 \) for some \( x_0, y_0 \in \nZ \).
2. \( d \mid a \) and \( d \mid b \).
3. Every common divisor of \( a \) and \( b \) divides \( d \).
4. \( d = \gcd(a, b) \). In particular, \( \gcd(a, b) = ax + by \) for some \( x, y \in \nZ \).
5. \( a\nZ + b\nZ = d\nZ \).
:::
:::

*Try it first (ten minutes): for \( a = 12 \) and \( b = 42 \), list the positive numbers \( 12x + 42y \) you can reach. Which is the least, and why should the least one divide \( 12 \)?*

::: {.idea}
The obvious plan starts from the greatest common divisor and tries to write it as \( ax + by \). It stalls: the definition of \( \gcd(a, b) \) says nothing about combinations, so there is nothing to build \( x \) and \( y \) from. The attempt on \( 12 \) and \( 42 \) suggests starting at the other end. The positive combinations \( 12, 42, 30, 18, 6, \dots \) have a least element, and it was found as a combination. Why should it divide \( 12 \)? Divide \( 12 \) by it. The remainder is \( 12 \) minus a multiple of a combination, so it is again a combination, and it is smaller than the least positive one. So it cannot be positive: it is \( 0 \). Once the least positive combination \( d \) is known to divide \( a \) and \( b \), the rest is bookkeeping: every common divisor divides the combination \( d \), so none exceeds it.

*Before reading on: where is the minimality of \( d \) used, and where its positivity?*
:::

::: {.proof}
(a) Suppose \( a \ne 0 \); if \( a = 0 \), then \( b \ne 0 \), and the argument is the same with \( b \) in place of \( a \). Both \( a = a \cdot 1 + b \cdot 0 \) and \( -a = a \cdot (-1) + b \cdot 0 \) lie in \( a\nZ + b\nZ \), and by @prp-divisibility-rules-integers (h) one of them is positive. So \( S \ne \emptyset \). Every element of \( S \) is positive, so \( 0 \) is a lower bound, and by @prp-integer-least-element \( S \) has a least element \( d \). Since \( d \in a\nZ + b\nZ \), there are \( x_0, y_0 \in \nZ \) with \( d = ax_0 + by_0 \).

(b) Since \( d \in \nZ_{>0} \), @thm-integers-division-remainder (a) gives \( q, r \in \nZ \) with \( a = qd + r \) and \( 0 \le r < d \). Then
\[
r = a - qd = a - q(ax_0 + by_0) = a(1 - qx_0) + b(-qy_0) ,
\]
so \( r \in a\nZ + b\nZ \). If \( r > 0 \), then \( r \in S \) and \( r < d \), contradicting the minimality of \( d \). Hence \( r = 0 \), and \( a = qd \), that is, \( d \mid a \). Dividing \( b \) by \( d \) in the same way gives \( d \mid b \).

(c) Let \( c \mid a \) and \( c \mid b \). By @prp-divisibility-rules-integers (c), \( c \mid ax_0 + by_0 = d \).

(d) By (b), \( d \) is a common divisor of \( a \) and \( b \). Let \( c \) be any common divisor. If \( c > 0 \), then \( c \mid d \) by (c), and \( c \le d \) by @prp-divisibility-rules-integers (e), since \( d > 0 \). If \( c \le 0 \), then \( c \le 0 < d \). So \( d \) is the greatest common divisor: \( d = \gcd(a, b) \) by @def-integer-gcd, and \( \gcd(a, b) = ax_0 + by_0 \).

(e) \( (\supseteq) \) Let \( k \in \nZ \). Then \( kd = k(ax_0 + by_0) = a(kx_0) + b(ky_0) \in a\nZ + b\nZ \). \( (\subseteq) \) Let \( x, y \in \nZ \). By (b), \( d \mid a \) and \( d \mid b \), so \( d \mid ax + by \) by @prp-divisibility-rules-integers (c), that is, \( ax + by \in d\nZ \). This proves the theorem.
:::

The answer to the prompt: the minimality of \( d \) is used once, in (b), to force the remainder \( r \) to be \( 0 \). The positivity of \( d \) is used twice: to divide by \( d \) at all (@thm-integers-division-remainder needs a positive divisor), and in (d), where \( c \le d \) for positive \( c \) comes from @prp-divisibility-rules-integers (e) and for the other \( c \) from \( 0 < d \). (The step \( r \in S \) uses the positivity of \( r \), not of \( d \), which is why the case \( r = 0 \) is split off.)

The proof of (b) is the move this chapter is built on, and we give it a name: **least positive element, then divide**. Take the least positive element \( d \) of a set closed under integer combinations; divide any element of the set by \( d \); the remainder lies in the set and is smaller than \( d \), so it is \( 0 \). Section 3.3 uses the move again for common multiples, and Section 3.4 for sets closed under subtraction.

For the coins, the theorem says: the payable amounts form \( 12\nZ + 42\nZ = d\nZ \), where \( d \) is the least positive payable amount, and \( d = \gcd(12, 42) \). The Try-it-first list finds \( d = 6 = 12 \cdot (-3) + 42 \cdot 1 \).

::: {.remark}
Clause (c) says that \( \gcd(a, b) \) is greatest also for divisibility, not only for \( \le \). For \( a, b \in \nN \), not both \( 0 \), it is the infimum of \( \{a, b\} \) in \( (\nN, \mid) \) (@fd2:def-order-supremum): it divides both, and every \( c \in \nN \) dividing both divides it. This is the mirror image of @fd2:exm-divisibility-lcm, where the supremum is the least common multiple. For general \( a, b \in \nZ \), let \( a' \) be the one of \( a \), \( -a \) that lies in \( \nN \), and likewise \( b' \) (@prp-divisibility-rules-integers (h), with \( a' = 0 \) if \( a = 0 \)). Since \( a \) and \( -a \) have the same divisors (@prp-divisibility-rules-integers (d) and @prp-ring-algebra (a)), \( \gcd(a, b) = \gcd(a', b') \). With the convention \( \gcd(0, 0) = 0 \), clauses (c) and (e) also hold for \( (0, 0) \) when \( d \) is read as \( 0 \): every integer divides \( 0 \), and \( 0\nZ + 0\nZ = \{0\} = 0\nZ \). So \( 0 \), the top of \( (\nN, \mid) \), is also the infimum of \( \{0, 0\} = \{0\} \).
:::

Pairs whose greatest common divisor is \( 1 \) get a name of their own.

::: {#def-coprime-integers}
[Coprime Integers]

Integers \( a, b \in \nZ \) are **coprime** if \( \gcd(a, b) = 1 \).
:::

For instance, \( 2 \) and \( 3 \) are coprime, and so are \( 1 \) and any \( b \); but \( 4 \) and \( 6 \) are not, since \( \gcd(4, 6) = 2 \), and neither are \( 0 \) and \( 0 \), since \( \gcd(0, 0) = 0 \). For coprime integers, (d) of the theorem produces \( 1 \) as a combination, and conversely:

::: {#cor-coprime-iff-combination}
[Coprime Means 1 Is a Combination]

Let \( a, b \in \nZ \). Then \( a \) and \( b \) are coprime if and only if \( ax + by = 1 \) for some \( x, y \in \nZ \).
:::

::: {.proof}
\( (\Rightarrow) \) If \( \gcd(a, b) = 1 \), then \( (a, b) \ne (0, 0) \), since \( \gcd(0, 0) = 0 \ne 1 \), and @thm-integers-bezout (d) gives \( x, y \in \nZ \) with \( ax + by = \gcd(a, b) = 1 \).

\( (\Leftarrow) \) Let \( ax + by = 1 \). Then \( (a, b) \ne (0, 0) \), since otherwise \( ax + by = 0 \ne 1 \). So \( g \coloneqq \gcd(a, b) \ge 1 \), and \( g \) divides \( a \) and \( b \), hence divides \( ax + by = 1 \) by @prp-divisibility-rules-integers (c). By @prp-divisibility-rules-integers (g), \( g = 1 \) or \( g = -1 \), and \( g \ge 1 \) rules out \( -1 \). So \( \gcd(a, b) = 1 \).
:::

The direction \( (\Leftarrow) \) is how coprimality is usually proved: exhibit one combination equal to \( 1 \). Thus \( 2 \cdot (-1) + 3 \cdot 1 = 1 \) shows again that \( 2 \) and \( 3 \) are coprime, with no list of divisors.

## The Euclidean algorithm

Bézout's theorem says that \( \gcd(a, b) \) is a combination of \( a \) and \( b \), but its proof finds it as a least element, which is no way to compute it. Computing needs a step that makes the numbers smaller without changing the set of combinations. Division with remainder is that step.

::: {#lem-gcd-remainder-step}
[One Step of the Euclidean Algorithm]

Let \( a \in \nZ \) and \( b \in \nZ_{>0} \), and let \( a = qb + r \) with \( q, r \in \nZ \). Then \( a\nZ + b\nZ = b\nZ + r\nZ \), and hence \( \gcd(a, b) = \gcd(b, r) \).
:::

::: {.proof}
\( (\subseteq) \) For \( x, y \in \nZ \), \( ax + by = (qb + r)x + by = b(qx + y) + rx \in b\nZ + r\nZ \). \( (\supseteq) \) For \( x, y \in \nZ \), \( bx + ry = bx + (a - qb)y = ay + b(x - qy) \in a\nZ + b\nZ \). So the two sets are equal. Neither pair is \( (0, 0) \), since \( b \ne 0 \). By @thm-integers-bezout (a) and (d), \( \gcd(a, b) \) is the least element of \( (a\nZ + b\nZ) \cap \nZ_{>0} \), and \( \gcd(b, r) \) is the least element of \( (b\nZ + r\nZ) \cap \nZ_{>0} \), the same set. So \( \gcd(a, b) = \gcd(b, r) \).
:::

The lemma does not need \( r \) to be the remainder; any \( q \) will do. Choosing the remainder makes the new pair smaller, and repeating the step gives a sequence. To define "repeat" without "and so on", we use the recursion theorem.

::: {#thm-euclidean-algorithm-integers}
[The Euclidean Algorithm]

Let \( a \in \nZ \) and \( b \in \nZ_{>0} \). Define \( (x_k, y_k) \in \nZ \times \nN \) for \( k \in \nN \) by \( (x_0, y_0) \coloneqq (a, b) \) and
\[
(x_{k+1}, y_{k+1}) \coloneqq
\begin{cases}
(y_k, r_k) & \text{if } y_k > 0, \\
(x_k, y_k) & \text{if } y_k = 0,
\end{cases}
\]
where, when \( y_k > 0 \), \( r_k \) is the remainder of \( x_k \) on division by \( y_k \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( x_k\nZ + y_k\nZ = a\nZ + b\nZ \) for every \( k \in \nN \);
2. there is a least \( K \in \nN \) with \( y_K = 0 \); moreover \( K \ge 1 \), and \( y_{k+1} < y_k \) for every \( k < K \);
3. \( x_K = \gcd(a, b) \).
:::
:::

The sequence is well defined. Let \( G \colon \nZ \times \nN \to \nZ \times \nN \) send \( (x, y) \) to \( (y, r) \), where \( r \) is the remainder of \( x \) on division by \( y \), if \( y > 0 \), and to \( (x, y) \) if \( y = 0 \). This is a function: the remainder exists and is unique by @thm-integers-division-remainder (a), and it lies in \( \nN \) because \( r \ge 0 \) (@thm-integers-ordered-ring (b)). The recursion theorem (@fd2:thm-recursion, read on \( \nN = \omega \) as @thm-omega-recursion by @cor-omega-identification (b)), with \( X = \nZ \times \nN \), starting value \( (a, b) \) and step \( (k, (x, y)) \mapsto G(x, y) \), gives exactly one sequence with the two displayed properties.

::: {.idea}
Part (a) is @lem-gcd-remainder-step, once per step, carried along by induction. For (b), the second entries are natural numbers that drop at each step while they are positive, and a set of natural numbers has a least element, which cannot be positive. For (c), at the first index \( K \) with \( y_K = 0 \), the invariant (a) reads \( a\nZ + b\nZ = x_K\nZ \), and Bézout's theorem identifies the gcd as the least positive element of this set.
:::

::: {.proof}
(a) We use @fd1:ax-induction (through @cor-omega-identification (b)) on \( k \), for \( P(k) \): "\( x_k\nZ + y_k\nZ = a\nZ + b\nZ \)". The base case \( P(0) \) holds since \( (x_0, y_0) = (a, b) \). Suppose \( P(k) \). If \( y_k > 0 \), then \( x_k = q_k y_k + r_k \) for some \( q_k \in \nZ \), and @lem-gcd-remainder-step with \( x_k \), \( y_k \) in place of \( a \), \( b \) gives
\[
x_{k+1}\nZ + y_{k+1}\nZ = y_k\nZ + r_k\nZ = x_k\nZ + y_k\nZ = a\nZ + b\nZ .
\]
If \( y_k = 0 \), then \( (x_{k+1}, y_{k+1}) = (x_k, y_k) \), and \( P(k + 1) \) is \( P(k) \).

(b) The set \( Y \coloneqq \{ y_k : k \in \nN \} \subseteq \nN \) is non-empty and has the lower bound \( 0 \), so it has a least element \( y_m \) (@prp-integer-least-element). If \( y_m > 0 \), then \( y_{m+1} = r_m < y_m \) by the definition of the step and @thm-integers-division-remainder (a), contradicting the choice of \( y_m \). So \( y_m = 0 \), and the set \( \{ k \in \nN : y_k = 0 \} \) is non-empty, with lower bound \( 0 \). Let \( K \) be its least element (@prp-integer-least-element). Then \( K \ne 0 \), since \( y_0 = b > 0 \); so \( K \ge 1 \). For \( k < K \), \( y_k \ne 0 \) by the choice of \( K \), so \( y_k > 0 \) (as \( y_k \in \nN \), @thm-integers-ordered-ring (b)), and \( y_{k+1} = r_k < y_k \).

(c) Since \( K \ge 1 \), \( K - 1 \in \nN \) and \( K - 1 < K \), so \( y_{K-1} > 0 \) by (b), and the definition of the step gives \( x_K = y_{K-1} > 0 \). By (a) with \( k = K \), and since \( y_K = 0 \),
\[
a\nZ + b\nZ = x_K\nZ + 0\nZ = x_K\nZ .
\]
The least positive element of \( x_K\nZ \) is \( x_K \): it lies in the set (\( x_K = 1 \cdot x_K \)), and every positive element \( m x_K \) is divisible by \( x_K \), so \( x_K \le m x_K \) by @prp-divisibility-rules-integers (e). Since \( b > 0 \), \( (a, b) \ne (0, 0) \), and by @thm-integers-bezout (a) and (d), the least element of \( (a\nZ + b\nZ) \cap \nZ_{>0} \) is \( \gcd(a, b) \). Hence \( x_K = \gcd(a, b) \).
:::

In practice the sequence is written as a chain of divisions, each dividing the previous divisor by the previous remainder, until a remainder is \( 0 \); then \( x_K = y_{K-1} \), the last non-zero second entry, is the gcd. If \( K \ge 2 \), it is the last non-zero remainder \( r_{K-2} \); if \( K = 1 \), it is \( b \), and then \( b \mid a \). Exercise B3 shows that at most \( b \) divisions are needed.

To find coefficients \( x, y \) with \( \gcd(a, b) = ax + by \), we run the identity of @lem-gcd-remainder-step backwards.

::: {.algorithm}
**Back-substitution.** Write out the divisions \( x_k = q_k y_k + r_k \) for \( k = 0, \dots, K - 1 \), so that \( x_{k+1} = y_k \) and \( y_{k+1} = r_k \). Start from \( \gcd(a, b) = x_K = 1 \cdot x_K + 0 \cdot y_K \), a combination of the last pair. Then, for \( k = K - 1, K - 2, \dots, 0 \) in turn, rewrite a combination \( u x_{k+1} + v y_{k+1} = u y_k + v r_k \) of the pair with index \( k + 1 \) as one of the pair with index \( k \), by substituting \( r_k = x_k - q_k y_k \):
\[
u y_k + v (x_k - q_k y_k) = v x_k + (u - q_k v) y_k ,
\]
the identity in the proof of @lem-gcd-remainder-step. After \( k = 0 \), the combination is one of \( x_0 = a \) and \( y_0 = b \). Multiply it out to check it. (By hand, the step \( k = K - 1 \) changes nothing, since \( r_{K-1} = 0 \); so one starts from the last division with a non-zero remainder, as in the example below.)
:::

The procedure only computes; nothing rests on it. That some \( x, y \) exist is @thm-integers-bezout (d), and the final multiplication checks the particular \( x, y \) found.

::: {#exm-euclidean-algorithm-run}
[Two runs of the algorithm]

Compute \( \gcd(252, 198) \) and \( \gcd(-35, 15) \), and write each as a combination of the two numbers.
:::

::: {.solution}
*The pair \( (252, 198) \).* The chain of divisions is
\[
\begin{aligned}
252 &= 1 \cdot 198 + 54, \\
198 &= 3 \cdot 54 + 36, \\
54 &= 1 \cdot 36 + 18, \\
36 &= 2 \cdot 18 + 0 .
\end{aligned}
\]
In the notation of the theorem, \( (x_k, y_k) \) runs through \( (252, 198) \), \( (198, 54) \), \( (54, 36) \), \( (36, 18) \), \( (18, 0) \), so \( K = 4 \) and \( \gcd(252, 198) = x_4 = 18 \). Back-substitution, from the third division up:
\[
\begin{aligned}
18 &= 54 - 1 \cdot 36 = 54 - (198 - 3 \cdot 54) = 4 \cdot 54 - 198 \\
&= 4 \cdot (252 - 198) - 198 = 4 \cdot 252 - 5 \cdot 198 .
\end{aligned}
\]
Check: \( 4 \cdot 252 = 1008 \), \( 5 \cdot 198 = 990 \), and \( 1008 - 990 = 18 \).

*The pair \( (-35, 15) \).* The first entry may be negative; only the second must be positive. The remainder of \( -35 \) on division by \( 15 \) is \( 10 \), not \( -5 \):
\[
\begin{aligned}
-35 &= (-3) \cdot 15 + 10, \\
15 &= 1 \cdot 10 + 5, \\
10 &= 2 \cdot 5 + 0 .
\end{aligned}
\]
So \( \gcd(-35, 15) = 5 \), and
\[
5 = 15 - 10 = 15 - \bigl( -35 + 3 \cdot 15 \bigr) = (-1) \cdot (-35) + (-2) \cdot 15 .
\]
Check: \( (-1) \cdot (-35) = 35 \), \( (-2) \cdot 15 = -30 \), and \( 35 - 30 = 5 \).
:::

::: {.warning}
Bézout coefficients are **not** unique. From \( 18 = 4 \cdot 252 - 5 \cdot 198 \) and \( 11 \cdot 252 = 2772 = 14 \cdot 198 \),
\[
18 = (4 - 11) \cdot 252 + (-5 + 14) \cdot 198 = (-7) \cdot 252 + 9 \cdot 198 .
\]
So "the" coefficients of \( \gcd(a, b) \) means nothing by itself; when a computation needs particular ones, they are those produced by back-substitution, and any other pair works as well.
:::

::: {.check}
Compute \( \gcd(0, -6) \) and \( \gcd(84, 35) \).
:::

::: {.solution}
\( \gcd(0, -6) = 6 \). Every integer divides \( 0 \), so the common divisors of \( 0 \) and \( -6 \) are the divisors of \( -6 \), which are those of \( 6 \) (@prp-divisibility-rules-integers (d) and @prp-ring-algebra (a)). The positive ones are at most \( 6 \) (@prp-divisibility-rules-integers (e)), and \( 6 \) is one of them. (The theorem does not apply directly to \( (0, -6) \), since its second entry is negative; it does apply to \( (0, 6) \), with the one division \( 0 = 0 \cdot 6 + 0 \).)

\( \gcd(84, 35) = 7 \), by the chain \( 84 = 2 \cdot 35 + 14 \), \( 35 = 2 \cdot 14 + 7 \), \( 14 = 2 \cdot 7 + 0 \).
:::

## Exercises

### A. Check your understanding

::: {#exr-gcd-and-bezout-a1}
[A1]

These questions are about the proof of @thm-integers-bezout.

::: {.enumerate options="label=(\alph*)"}
1. Where is the minimality of \( d \) used?
2. Run the proof on \( (a, b) = (12, 42) \): find \( d \), \( x_0 \), \( y_0 \), and the divisions of (b).
3. Which step fails for \( (a, b) = (0, 0) \)?
4. State the idea of the proof in two sentences.
:::
:::

::: {.solution}
(a) Once, in (b): the remainder \( r \) of \( a \) on division by \( d \) is a combination of \( a \) and \( b \), and if it were positive it would be an element of \( S \) smaller than \( d \). Minimality forces \( r = 0 \).

(b) The set \( S \) contains \( 6 = 12 \cdot (-3) + 42 \cdot 1 \). Every element of \( 12\nZ + 42\nZ \) is divisible by \( 6 \), since \( 6 \mid 12 \) and \( 6 \mid 42 \) (@prp-divisibility-rules-integers (c)), so every element of \( S \) is at least \( 6 \) (@prp-divisibility-rules-integers (e)). Hence \( d = 6 \), with \( x_0 = -3 \) and \( y_0 = 1 \). The divisions of (b) are \( 12 = 2 \cdot 6 + 0 \) and \( 42 = 7 \cdot 6 + 0 \): both remainders are \( 0 \), as the proof predicts.

(c) Step (a): \( 0\nZ + 0\nZ = \{0\} \), so \( S = \emptyset \), and @prp-integer-least-element does not apply. There is no \( d \) to divide by.

(d) Take the least positive integer combination \( d \) of \( a \) and \( b \). Dividing \( a \) (or \( b \)) by \( d \) leaves a remainder that is again a combination and smaller than \( d \), so it is \( 0 \); thus \( d \) is a common divisor, and since every common divisor divides the combination \( d \), it is the greatest.
:::

### B. Practice

::: {#exr-gcd-and-bezout-b1}
[B1]

Run the Euclidean algorithm on \( (1001, 357) \), and use back-substitution to write \( \gcd(1001, 357) \) as \( 1001x + 357y \) with \( x, y \in \nZ \).
:::

::: {.solution}
The chain of divisions is
\[
\begin{aligned}
1001 &= 2 \cdot 357 + 287, \\
357 &= 1 \cdot 287 + 70, \\
287 &= 4 \cdot 70 + 7, \\
70 &= 10 \cdot 7 + 0 ,
\end{aligned}
\]
so \( \gcd(1001, 357) = 7 \) by @thm-euclidean-algorithm-integers (c). Back-substitution:
\[
\begin{aligned}
7 &= 287 - 4 \cdot 70 = 287 - 4 \cdot (357 - 287) = 5 \cdot 287 - 4 \cdot 357 \\
&= 5 \cdot (1001 - 2 \cdot 357) - 4 \cdot 357 = 5 \cdot 1001 - 14 \cdot 357 .
\end{aligned}
\]
Check: \( 5 \cdot 1001 = 5005 \), \( 14 \cdot 357 = 4998 \), and \( 5005 - 4998 = 7 \). Hence \( x = 5 \), \( y = -14 \) works.
:::

::: {#exr-gcd-and-bezout-b2}
[B2]

Let \( a, b \in \nZ \). Prove that \( \gcd(a, b) = \gcd(-a, b) \), and that \( \gcd(a, 0) = a \) if \( a \in \nZ_{>0} \).
:::

::: {.solution}
*First claim.* If \( (a, b) = (0, 0) \), then also \( (-a, b) = (0, 0) \), and both sides are \( 0 \) by convention. Otherwise \( (-a, b) \ne (0, 0) \) as well, since \( -a = 0 \) would give \( a = -(-a) = -0 = 0 \) (@prp-ring-algebra (a); \( -0 = 0 \) because \( 0 + 0 = 0 \) and the inverse is unique). By @prp-divisibility-rules-integers (d), \( c \mid a \) implies \( c \mid -a \), and \( c \mid -a \) implies \( c \mid -(-a) = a \) (@prp-ring-algebra (a)). So \( a \) and \( -a \) have the same divisors, the pairs \( (a, b) \) and \( (-a, b) \) have the same common divisors, and the greatest is the same (@def-integer-gcd).

*Second claim.* Let \( a > 0 \). Every integer divides \( 0 \) (@prp-divisibility-rules-integers (a)), so the common divisors of \( a \) and \( 0 \) are the divisors of \( a \). Among them is \( a \) itself. A positive divisor \( c \) satisfies \( c \le a \) by @prp-divisibility-rules-integers (e), and a non-positive one satisfies \( c \le 0 < a \). So \( a \) is the greatest, and \( \gcd(a, 0) = a \).
:::

::: {#exr-gcd-and-bezout-b3}
[B3: The algorithm stops quickly]

In the notation of @thm-euclidean-algorithm-integers, prove that \( y_k \le b - k \) for every \( k \in \nN \) with \( k \le K \). Deduce that \( K \le b \): the algorithm stops after at most \( b \) divisions.
:::

::: {.solution}
We use @fd1:ax-induction (through @cor-omega-identification (b)) on \( k \), for \( P(k) \): "if \( k \le K \), then \( y_k \le b - k \)". The base case \( P(0) \) is \( y_0 = b = b - 0 \). Suppose \( P(k) \), and let \( k + 1 \le K \). Then \( k < K \), so \( k \le K \) and \( P(k) \) gives \( y_k \le b - k \). By @thm-euclidean-algorithm-integers (b), \( y_{k+1} < y_k \), so \( y_{k+1} + 1 \le y_k \) by discreteness (@thm-integers-ordered-ring (c)), that is, \( y_{k+1} \le y_k - 1 \). Hence \( y_{k+1} \le b - k - 1 = b - (k + 1) \), which is \( P(k + 1) \).

With \( k = K \): \( 0 = y_K \le b - K \), so \( K \le b \). Each index \( k < K \) is one division, so there are \( K \le b \) of them.
:::

### C. Going deeper

::: {#exr-gcd-and-bezout-c1}
[C1: Exit check: Bézout]

Let \( a, b \in \nZ \), not both \( 0 \), and let \( S \coloneqq (a\nZ + b\nZ) \cap \nZ_{>0} \). Prove that \( S \) has a least element \( d \); that \( d \mid a \) and \( d \mid b \); that every common divisor of \( a \) and \( b \) divides \( d \); and that \( d = \gcd(a, b) \).
:::

::: {.solution}
*\( S \) has a least element.* Say \( a \ne 0 \) (otherwise exchange the roles of \( a \) and \( b \)). Both \( a = a \cdot 1 + b \cdot 0 \) and \( -a = a \cdot (-1) + b \cdot 0 \) are combinations of \( a \) and \( b \), and one of them is positive (@prp-divisibility-rules-integers (h)); so \( S \ne \emptyset \). It is bounded below by \( 0 \), so it has a least element \( d \) (@prp-integer-least-element), and \( d = ax_0 + by_0 \) for some \( x_0, y_0 \in \nZ \).

*\( d \) divides \( a \) and \( b \).* Divide \( a \) by \( d > 0 \) (@thm-integers-division-remainder (a)): \( a = qd + r \) with \( 0 \le r < d \). Then \( r = a(1 - qx_0) + b(-qy_0) \) is a combination of \( a \) and \( b \). If \( r > 0 \), then \( r \in S \) and \( r < d \), against the minimality of \( d \). So \( r = 0 \) and \( d \mid a \). The same argument with \( b \) gives \( d \mid b \).

*Common divisors divide \( d \).* If \( c \mid a \) and \( c \mid b \), then \( c \mid ax_0 + by_0 = d \) (@prp-divisibility-rules-integers (c)).

*\( d \) is the gcd.* \( d \) is a common divisor. A common divisor \( c > 0 \) divides \( d > 0 \), so \( c \le d \) (@prp-divisibility-rules-integers (e)); a common divisor \( c \le 0 \) satisfies \( c < d \). So \( d \) is the greatest common divisor (@def-integer-gcd).

**Marking scheme.** (10 points)
- 2: shows \( S \ne \emptyset \), with a reason that covers \( a < 0 \) or \( b < 0 \) (for instance, one of \( a \), \( -a \) is a positive combination).
- 1: obtains the least element by a cited well-ordering result for sets of integers bounded below.
- 3: divides \( a \) by \( d \) and writes the remainder as a combination of \( a \) and \( b \).
- 2: uses the minimality of \( d \) to force the remainder to be \( 0 \), for \( a \) and for \( b \).
- 2: shows every common divisor divides \( d \), and deduces that \( d \) is the greatest (with the case of non-positive divisors).
Fatal errors (0 for the step): assuming that the gcd is a combination of \( a \) and \( b \) (circular); citing @thm-euclidean-algorithm-integers (c) or the gcd clause of @lem-gcd-remainder-step (both are proved from @thm-integers-bezout, so this is circular); "\( d \) divides \( a \) because \( d \) is the least positive combination", with no division step. A second route goes through the Euclidean algorithm, with back-substitution, by induction on the number of steps. Citing @thm-euclidean-algorithm-integers (a), (b) and the equality \( a\nZ + b\nZ = b\nZ + r\nZ \) of @lem-gcd-remainder-step is allowed; if the invariant used is "the common divisors are unchanged", it must be proved directly from \( r = a - qb \). The invariant earns the 3 points for the division, and termination earns the 2 points for minimality. The answer must still identify the gcd with the least element \( d \) of \( S \) (\( d \le \gcd(a, b) \) since \( \gcd(a, b) \in S \); \( \gcd(a, b) \mid d \) since the gcd divides every combination). The rest is marked as written.
:::

::: {#exr-gcd-and-bezout-c2}
[C2: Scaling the gcd]

Let \( a, b \in \nZ \) and \( k \in \nZ_{>0} \). Prove that \( \gcd(ka, kb) = k \gcd(a, b) \).
:::

::: {.solution}
[Hint 1]

Use the description of \( a\nZ + b\nZ \) in @thm-integers-bezout (e), and the description of the gcd as a least element in (a) and (d).
:::

::: {.solution}
[Hint 2]

If \( (a, b) \ne (0, 0) \) and \( d \coloneqq \gcd(a, b) \), first show \( (ka)\nZ + (kb)\nZ = (kd)\nZ \).
:::

::: {.solution}
If \( (a, b) = (0, 0) \), then \( (ka, kb) = (0, 0) \) by @prp-ring-algebra (b), and both sides are \( 0 \): \( \gcd(0, 0) = 0 = k \cdot 0 \).

Otherwise let \( d \coloneqq \gcd(a, b) \), so \( d \ge 1 \). Say \( a \ne 0 \) (otherwise \( b \ne 0 \); exchange the roles of \( a \) and \( b \)); then \( ka \ne 0 \), since \( k \ne 0 \) and \( \nZ \) has no zero divisors (@prp-ordered-ring-rules (f)). So \( (ka, kb) \ne (0, 0) \), and @thm-integers-bezout applies to both pairs.

*The combinations.* For \( x, y \in \nZ \), \( (ka)x + (kb)y = k(ax + by) \). As \( x, y \) range over \( \nZ \), \( ax + by \) ranges over \( a\nZ + b\nZ = d\nZ \) (@thm-integers-bezout (e)), so
\[
(ka)\nZ + (kb)\nZ = \{ k(md) : m \in \nZ \} = \{ m(kd) : m \in \nZ \} = (kd)\nZ .
\]

*The least positive element.* \( kd > 0 \) by (O4), and \( kd = 1 \cdot kd \in (kd)\nZ \). Every positive element \( m(kd) \) of \( (kd)\nZ \) is divisible by \( kd \), so \( kd \le m(kd) \) by @prp-divisibility-rules-integers (e). So \( kd \) is the least element of \( \bigl( (ka)\nZ + (kb)\nZ \bigr) \cap \nZ_{>0} \), and by @thm-integers-bezout (a) and (d), \( \gcd(ka, kb) = kd = k \gcd(a, b) \).

For instance, \( \gcd(12, 42) = 6 \gcd(2, 7) = 6 \), since \( 2 \) and \( 7 \) are coprime (\( 2 \cdot (-3) + 7 \cdot 1 = 1 \), @cor-coprime-iff-combination).

**Marking scheme.** (10 points)
- 2: treats \( (a, b) = (0, 0) \) by the convention, and checks \( (ka, kb) \ne (0, 0) \) otherwise, with a reason (no zero divisors).
- 4: shows \( (ka)\nZ + (kb)\nZ = (kd)\nZ \), citing @thm-integers-bezout (e) for \( (a, b) \).
- 2: shows that \( kd \) is the least positive element of \( (kd)\nZ \).
- 2: concludes \( \gcd(ka, kb) = kd \) through @thm-integers-bezout (a), (d) for \( (ka, kb) \).
Fatal errors (0 for the step): asserting that every common divisor of \( ka \) and \( kb \) is \( k \) times a common divisor of \( a \) and \( b \) (false: \( 1 \) divides \( 6 = 3 \cdot 2 \) and \( 9 = 3 \cdot 3 \), and \( 1 \) is not \( 3 \) times an integer); using prime factorizations, which this section does not have. A second route, showing \( k d \) is a common divisor and every common divisor \( c \) divides \( kd \) because \( c \mid (ka)x_0 + (kb)y_0 = kd \), earns the same total: 2 for treating \( (a, b) = (0, 0) \) by the convention and checking \( (ka, kb) \ne (0, 0) \) otherwise (no zero divisors); 3 for showing \( kd \) is a common divisor and a combination (\( kd = (ka)x_0 + (kb)y_0 \) with \( ax_0 + by_0 = d \) from @thm-integers-bezout); 3 for every common divisor dividing \( kd \); 2 for concluding \( kd \) is the greatest (\( kd > 0 \), rule (e) for positive divisors, and the non-positive divisors) via @def-integer-gcd.
:::

<!-- dependency ledger
def-integer-linear-combinations (claim): the three closure identities | ring laws of Z (thm-integers-commutative-ring) and prp-ring-algebra (c), cited
def-integer-linear-combinations (example): 6 = 12 * (-3) + 42 * 1, 30 = 42 - 12, 1 = 2 * (-1) + 3 * 1; non-zero N-combinations of 12, 42 are >= 12 | verify/ch03/def-integer-linear-combinations.py
def-integer-linear-combinations (claim): n Z + 0 Z = n Z | prp-ring-algebra (b), (F6), cited
def-integer-linear-combinations (example): 0 Z + 0 Z = {0} | case n = 0 of n Z + 0 Z = n Z; 0 Z = {0} by prp-ring-algebra (b), cited
def-integer-gcd (claim): (well-definedness) the argument with b in place of a when a = 0 | symmetric repeat of the argument given
def-integer-gcd (example): 6 = 1 * 4 + 2, 4 = 1 * 3 + 1, and 2 | 4, 2 | 6 | numerals (01-division-with-remainder opening paragraph); verify/ch03/def-integer-gcd.py
def-integer-gcd (example): a positive d <= 4 lies in {1, 2, 3, 4} | discreteness, thm-integers-ordered-ring (c), cited
def-integer-gcd (example): a and -a have the same divisors (gcd(-5, 5), gcd(0, -6)) | prp-divisibility-rules-integers (d), prp-ring-algebra (a), cited
def-integer-gcd (claim): the convention gcd(0, 0) = 0 matches fd2 exm-divisibility-lcm (0 the top of (N, |)) | fd2 F2.2 §06 exm-divisibility-lcm (cited)
thm-integers-bezout (proof): the case a = 0 is the same with b in place of a | symmetric repeat (a Z + b Z is symmetric in a, b by (F1))
thm-integers-bezout (proof): r = a - q(a x0 + b y0) = a(1 - q x0) + b(-q y0) | ring laws of Z, thm-integers-commutative-ring; prp-ring-algebra (c)
thm-integers-bezout (claim): the coin hook, 42 - 3 * 12 = 6 and the Try-it-first list | verify/ch03/thm-integers-bezout.py
thm-integers-bezout (claim): Section 3.3 uses the move for common multiples, Section 3.4 for sets closed under subtraction | blueprint ch03.md, §03 B2 and §04 C2 (faded triple); prose pointers within the chapter, nothing depends on them
thm-integers-bezout (claim): (remark) gcd is the infimum in (N, |); a' in N with a' = 0 if a = 0 | fd2 def-order-supremum (cited), prp-divisibility-rules-integers (h), (d), prp-ring-algebra (a) (cited)
cor-coprime-iff-combination (proof): g >= 1 rules out g = -1 | -1 < 0 < 1, prp-ordered-ring-rules (a), (e)
lem-gcd-remainder-step (proof): (qb + r)x + by = b(qx + y) + rx and bx + (a - qb)y = ay + b(x - qy) | ring laws of Z, thm-integers-commutative-ring
thm-euclidean-algorithm-integers (claim): the step G is a function Z x N -> Z x N; recursion theorem read on omega | thm-integers-division-remainder (a), thm-integers-ordered-ring (b), fd2 thm-recursion via thm-omega-recursion and cor-omega-identification (b), cited in the paragraph after the statement
thm-euclidean-algorithm-integers (proof): x_K Z + 0 Z = x_K Z | def-integer-linear-combinations (the paragraph after it, n Z + 0 Z = n Z)
thm-euclidean-algorithm-integers (proof): K - 1 in N and K - 1 < K for K >= 1 | omega arithmetic (cor-omega-identification (c), fd2 lem-naturals-arithmetic subtraction), with thm-integers-ordered-ring (a)
thm-euclidean-algorithm-integers (claim): (paragraph after the proof) last non-zero remainder is r_{K-2} when K >= 2; b | a when K = 1 | definition of the step, inline
exm-euclidean-algorithm-run (example): every division and back-substitution line; the warning's 11 * 252 = 14 * 198 = 2772; the Quick check | verify/ch03/exm-euclidean-algorithm-run.py
exr-gcd-and-bezout-a1 (solution): 6 = 12 * (-3) + 42 * 1, 12 = 2 * 6, 42 = 7 * 6 | verify/ch03/exr-gcd-and-bezout-a1.py
exr-gcd-and-bezout-b1 (solution): the chain for (1001, 357) and 7 = 5 * 1001 - 14 * 357 | verify/ch03/exr-gcd-and-bezout-b1.py
exr-gcd-and-bezout-b3 (solution): b - k - 1 = b - (k + 1); 0 <= b - K gives K <= b | ring laws of Z; prp-ordered-ring-rules (a)
exr-gcd-and-bezout-c2 (solution): (ka)x + (kb)y = k(ax + by); k(md) = m(kd) | ring laws of Z
exr-gcd-and-bezout-c2 (solution): gcd(12, 42) = 6 gcd(2, 7) instance | verify/ch03/exr-gcd-and-bezout-c2.py
-->
