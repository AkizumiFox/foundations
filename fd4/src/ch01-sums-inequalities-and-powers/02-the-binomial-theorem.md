# The Binomial Theorem

One polynomial does more work in this volume than any other: \( (1 + x)^n \). In analysis it bounds powers from below, and Section 1.4 makes \( r^n \) large by keeping a single term of its expansion. In algebra it is the source of Fermat's little theorem, which Chapter 4 proves by expanding \( (x + y)^p \) in a field with \( p \) elements. Both uses need the same theorem, so this section proves it once, in every commutative ring. The coefficients are defined by Pascal's rule and never by division, which keeps the theorem valid in rings where \( p! \) is \( 0 \). The school formula with factorials comes afterwards, as an identity between natural numbers that may then be read in \( \nR \).

## Binomial coefficients

In \( (x + y)^n \), each product \( x^k y^{n-k} \) appears a certain number of times, and that number is the binomial coefficient. We define it by Pascal's rule, which is how the coefficients arise when \( (x + y)^n \) is multiplied by \( x + y \), and we never divide.

::: {#def-binomial-coefficients}
[Binomial Coefficients]

The **binomial coefficients** \( \binom{n}{k} \in \nN \), for \( n, k \in \nN \), are defined by recursion on \( n \) (@fd2:thm-recursion, with \( X \) the set of functions \( \nN \to \nN \)):
\[
\begin{aligned}
\binom{0}{0} &\coloneqq 1 , & \binom{0}{k} &\coloneqq 0 \quad (k \ge 1) , \\
\binom{n + 1}{0} &\coloneqq 1 , & \binom{n + 1}{k + 1} &\coloneqq \binom{n}{k} + \binom{n}{k + 1} \quad (k \in \nN) .
\end{aligned}
\]
:::

In words: row \( n + 1 \) starts with \( 1 \), and each later entry is the sum of the two entries of row \( n \) above it (**Pascal's rule**). Each row is a whole function \( \nN \to \nN \), so the recursion has values for every \( k \), and a coefficient is a natural number, never a quotient.

Three facts follow by one induction on \( n \) each.

- \( \binom{n}{k} = 0 \) for \( k > n \). For \( n = 0 \) this is the definition. If it holds for \( n \) and \( k > n + 1 \), write \( k = j + 1 \) with \( j > n \); then \( \binom{n+1}{j+1} = \binom{n}{j} + \binom{n}{j+1} = 0 + 0 \).
- \( \binom{n}{n} = 1 \). Indeed \( \binom{0}{0} = 1 \), and \( \binom{n+1}{n+1} = \binom{n}{n} + \binom{n}{n+1} = 1 + 0 \) by the first fact.
- \( \binom{n}{1} = n \). Indeed \( \binom{0}{1} = 0 \), and \( \binom{n+1}{1} = \binom{n}{0} + \binom{n}{1} = 1 + n \).

The rows \( n = 0, \dots, 6 \), with the zeros for \( k > n \) shown:

| \( n \) | \( k = 0 \) | \( 1 \) | \( 2 \) | \( 3 \) | \( 4 \) | \( 5 \) | \( 6 \) |
|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| 2 | 1 | 2 | 1 | 0 | 0 | 0 | 0 |
| 3 | 1 | 3 | 3 | 1 | 0 | 0 | 0 |
| 4 | 1 | 4 | 6 | 4 | 1 | 0 | 0 |
| 5 | 1 | 5 | 10 | 10 | 5 | 1 | 0 |
| 6 | 1 | 6 | 15 | 20 | 15 | 6 | 1 |

The identity we need relates row \( n + 1 \) to row \( n \) by a factor. It is what makes a prime divide the middle coefficients of row \( p \).

::: {#prp-binomial-absorption}
[Absorption Identity]

For all \( n, k \in \nN \),
\[
(k + 1) \binom{n + 1}{k + 1} = (n + 1) \binom{n}{k} .
\]
:::

::: {.idea}
The definition is a recursion on \( n \), so we induct on \( n \), proving the statement for **all** \( k \) at once; the step then needs the hypothesis at two values of \( k \). In the step, expand the left side by Pascal's rule, split the factor \( k + 2 \) as \( (k + 1) + 1 \) in front of one of the two terms, apply the hypothesis twice, and recombine with Pascal's rule. For \( n = 2 \), \( k = 0 \) it reads \( 1 \cdot 3 = 3 \cdot 1 \); for \( n = 3 \), \( k = 1 \), \( 2 \cdot 6 = 4 \cdot 3 \).
:::

::: {.proof}
We prove by induction on \( n \) (@fd1:ax-induction) the statement "for every \( k \in \nN \), \( (k + 1)\binom{n+1}{k+1} = (n + 1)\binom{n}{k} \)".

*Base \( n = 0 \).* For \( k = 0 \): \( 1 \cdot \binom{1}{1} = 1 = 1 \cdot \binom{0}{0} \). For \( k \ge 1 \): \( \binom{1}{k+1} = 0 \) since \( k + 1 > 1 \), and \( \binom{0}{k} = 0 \); both sides are \( 0 \).

*Step.* Suppose the statement holds for \( n \). For \( k = 0 \), the claim for \( n + 1 \) reads \( \binom{n+2}{1} = (n + 2)\binom{n+1}{0} \), and both sides are \( n + 2 \) by the facts above. For \( k = j + 1 \) with \( j \in \nN \), Pascal's rule gives
\[
\begin{aligned}
(j + 2)\binom{n+2}{j+2} &= (j + 2)\binom{n+1}{j+1} + (j + 2)\binom{n+1}{j+2} \\
&= (j + 1)\binom{n+1}{j+1} + \binom{n+1}{j+1} + (j + 2)\binom{n+1}{j+2} \\
&= (n + 1)\binom{n}{j} + \binom{n+1}{j+1} + (n + 1)\binom{n}{j+1} \\
&= (n + 1)\binom{n+1}{j+1} + \binom{n+1}{j+1} = (n + 2)\binom{n+1}{j+1} ,
\end{aligned}
\]
where the third line uses the hypothesis at \( k = j \) and at \( k = j + 1 \), and the fourth line Pascal's rule again. This is the claim for \( n + 1 \) at \( k = j + 1 \). This proves the proposition.
:::

## Binomial coefficients and factorials

School defines \( \binom{n}{k} \) as \( \frac{n!}{k!\,(n-k)!} \), with the factorial \( n! = \prod_{k=1}^{n} k \) of @fd2:def-sum-product. The recursive definition and the school formula agree, and absorption is what shows it. We prove the agreement as an identity between natural numbers, with no division in it, and divide only at the end, in \( \nR \).

::: {#prp-binomial-factorial}
[Binomial Coefficients and Factorials]

Let \( n, k \in \nN \) with \( k \le n \).

::: {.enumerate options="label=(\alph*)"}
1. \( \binom{n}{k} \, k! \, (n - k)! = n! \).
2. \( \binom{n}{k} = \binom{n}{n-k} \).
3. \( \binom{n}{k} \, k! = \prod_{j=0}^{k-1} (n - j) \).
:::

Hence, in \( \nR \), \( \binom{n}{k} = \dfrac{n!}{k!\,(n - k)!} \).
:::

*In words:* the table above is the table of the school formula, it is symmetric about the middle of each row, and \( \binom{n}{k} \, k! \) is the product of the \( k \) numbers \( n, n - 1, \dots, n - k + 1 \).

::: {.idea}
Induct on \( n \), for all \( k \le n \) at once, as in the absorption identity. In the step, write \( (j + 1)! = j! \, (j + 1) \); absorption trades the factor \( j + 1 \) and the row \( n + 1 \) for a factor \( n + 1 \) and the row \( n \), and the hypothesis turns what is left into \( n! \). Parts (b) and (c) then compare two products equal to \( n! \) and cancel a common factor, which is legal in \( \nZ \) because a product of non-zero integers is non-zero.
:::

::: {.proof}
We prove (a) by induction on \( n \) (@fd1:ax-induction), for every \( k \le n \) at once. For \( n = 0 \) the only \( k \) is \( 0 \), and \( \binom{0}{0} \, 0! \, 0! = 1 = 0! \).

Suppose (a) holds for \( n \), and let \( k \le n + 1 \). If \( k = 0 \), the left side is \( 1 \cdot 1 \cdot (n + 1)! \). Otherwise \( k = j + 1 \) with \( j \le n \), and \( (n + 1) - k = n - j \). By the factorial recursion \( (j + 1)! = j! \, (j + 1) \), then @prp-binomial-absorption, then the hypothesis at \( j \),
\[
\begin{aligned}
\binom{n+1}{j+1} \, (j + 1)! \, (n - j)! &= \Bigl[ (j + 1) \binom{n+1}{j+1} \Bigr] \, j! \, (n - j)! \\
&= (n + 1) \, \Bigl[ \binom{n}{j} \, j! \, (n - j)! \Bigr] = (n + 1) \, n! ,
\end{aligned}
\]
and \( (n + 1) \, n! = (n + 1)! \) by the factorial recursion. This proves (a) for \( n + 1 \). Parts (b) and (c) are proved in the fold below.

For the formula in \( \nR \), read each natural number \( m \) as the real number \( m \cdot 1 \) (@fd3:def-naturals-in-ordered-field). By @fd3:prp-naturals-in-ordered-field (a), the products in (a) are the same products in \( \nR \), and by (b) there, \( k! \, (n - k)! \ge 1 > 0 \). Dividing (a) by this positive real gives the formula. This proves the proposition.
:::

::: {.second-reading title="Proofs of (b) and (c): cancelling in the integers"}
**Proof of (b).** Let \( c \coloneqq k! \, (n - k)! \), a positive integer, so \( c \ne 0 \). By (a) at \( k \), \( \binom{n}{k} c = n! \). Since \( n - k \le n \) and \( n - (n - k) = k \), (a) at \( n - k \) gives \( \binom{n}{n-k} (n - k)! \, k! = n! \), that is, \( \binom{n}{n-k} c = n! \). Subtracting in \( \nZ \), \( \bigl( \binom{n}{k} - \binom{n}{n-k} \bigr) c = 0 \). Since \( \nZ \) is an ordered commutative ring (@fd3:thm-integers-ordered-ring) and \( c \ne 0 \), @fd3:prp-ordered-ring-rules (f) gives \( \binom{n}{k} - \binom{n}{n-k} = 0 \).

**Proof of (c).** First, \( n! = (n - k)! \prod_{j=0}^{k-1} (n - j) \) for every \( k \le n \), by induction on \( k \). For \( k = 0 \) the product is empty, equal to \( 1 \), and both sides are \( n! \). If the claim holds for \( k \) and \( k + 1 \le n \), then \( n - k \ge 1 \), so the factorial recursion gives \( (n - k)! = (n - k - 1)! \, (n - k) \), and the product recursion appends the factor \( j = k \):
\[
n! = (n - k - 1)! \, (n - k) \prod_{j=0}^{k-1} (n - j) = \bigl( n - (k + 1) \bigr)! \prod_{j=0}^{k} (n - j) .
\]
Now (a) and this claim give \( \binom{n}{k} \, k! \, (n - k)! = (n - k)! \prod_{j=0}^{k-1} (n - j) \). The factor \( (n - k)! \) is a positive integer, so it cancels as \( c \) did in (b). This proves (c).
:::

The formula is a fact about natural numbers, and in \( \nR \) the division by \( k! \, (n - k)! \) is legal because the divisor is a positive real. In the field with \( p \) elements of Chapter 4, \( p! \) is \( 0 \), and so is \( k! \, (n - k)! \) as soon as \( k \ge p \); there the formula cannot even be written, and the definition by Pascal's rule is the one that survives.

## The binomial theorem

Expanding \( (x + y)^n \) multiplies out \( n \) factors \( x + y \) and collects the products \( x^k y^{n-k} \). In a commutative ring this collecting is legitimate, and the counts are the binomial coefficients, acting as natural multiples.

::: {#thm-binomial-commutative-ring}
[The Binomial Theorem in a Commutative Ring]

Let \( R \) be a commutative ring, \( x, y \in R \) and \( n \in \nN \). Then
\[
(x + y)^n = \sum_{k=0}^{n} \binom{n}{k} \cdot \bigl( x^k y^{n-k} \bigr) .
\]
:::

Here \( \binom{n}{k} \cdot z \) is the natural multiple of @lem-natural-multiples (in \( \nR \), the product \( \binom{n}{k} z \)), and \( n - k \in \nN \) since \( k \le n \).

::: {.idea}
Induct on \( n \), with \( (x + y)^{n+1} = (x + y)^n x + (x + y)^n y \). Multiplying the sum for \( (x + y)^n \) by \( x \) raises every power of \( x \) by one, which shifts the coefficients one place to the right; multiplying by \( y \) leaves them in place. Adding the two rows entry by entry is exactly Pascal's rule. The work is in lining the two sums up over the same range \( k = 0, \dots, n + 1 \): the shifted sum gets a zero first term, and the other one a zero last term.

*Self-explain why \( w_{n+1} = 0 \).*
:::

::: {.proof}
Induction on \( n \) (@fd1:ax-induction). For \( n = 0 \), \( (x + y)^0 = 1 \) and the right side is \( \binom{0}{0} \cdot (x^0 y^0) = 1 \cdot (1 \cdot 1) = 1 \).

Suppose the formula holds for \( n \), and put \( t_k \coloneqq \binom{n}{k} \cdot (x^k y^{n-k}) \) for \( 0 \le k \le n \). By the power recursion, (F9) and @lem-ring-finite-sums (b) with (F6),
\[
(x + y)^{n+1} = (x + y)^n x + (x + y)^n y = \sum_{k=0}^{n} t_k x + \sum_{k=0}^{n} t_k y .
\]
By the rule \( (m \cdot a) b = m \cdot (ab) \) of @lem-natural-multiples (c), with (F5), (F6) and the power recursion,
\[
t_k x = \binom{n}{k} \cdot \bigl( x^{k+1} y^{n-k} \bigr) , \qquad t_k y = \binom{n}{k} \cdot \bigl( x^k y^{n+1-k} \bigr) .
\]
For \( 0 \le k \le n + 1 \) let \( z_k \coloneqq x^k y^{n+1-k} \), and define
\[
u_0 \coloneqq 0 , \quad u_k \coloneqq \binom{n}{k - 1} \cdot z_k \ (1 \le k \le n + 1) , \qquad w_k \coloneqq \binom{n}{k} \cdot z_k \ (0 \le k \le n + 1) .
\]
Then \( t_k x = u_{k+1} \) and \( t_k y = w_k \) for \( 0 \le k \le n \), and \( w_{n+1} = 0 \cdot z_{n+1} = 0 \), since \( \binom{n}{n+1} = 0 \). By @lem-ring-finite-sums (f) and \( u_0 = 0 \), and by splitting off the last term \( w_{n+1} = 0 \),
\[
\sum_{k=0}^{n} t_k x = \sum_{k=0}^{n+1} u_k , \qquad \sum_{k=0}^{n} t_k y = \sum_{k=0}^{n+1} w_k .
\]
So \( (x + y)^{n+1} = \sum_{k=0}^{n+1} (u_k + w_k) \) by @lem-ring-finite-sums (a). Finally, \( u_0 + w_0 = 0 + 1 \cdot z_0 = \binom{n+1}{0} \cdot z_0 \), and for \( k = j + 1 \) with \( 0 \le j \le n \), the sum rule @lem-natural-multiples (a) (that is, @fd3:prp-ordered-ring-rules (h), whose proof uses no order) and Pascal's rule give
\[
u_k + w_k = \binom{n}{j} \cdot z_k + \binom{n}{j + 1} \cdot z_k = \binom{n + 1}{j + 1} \cdot z_k = \binom{n + 1}{k} \cdot z_k .
\]
Hence \( (x + y)^{n+1} = \sum_{k=0}^{n+1} \binom{n+1}{k} \cdot (x^k y^{n+1-k}) \), which is the formula for \( n + 1 \). This proves the theorem.
:::

The proof used (F6) at every regrouping of \( x^k y^{n-k} x \), and the theorem needs it: the linear-algebra volumes meet matrices, whose multiplication is not commutative, and there the expansion holds only for pairs that commute. For \( R = \nZ \) the theorem is the familiar expansion, since there \( m \cdot z = mz \) (@lem-natural-multiples (e)). The same holds in \( \nR \), where \( m \cdot 1 \) is the real number \( m \), and this is the reading the next examples and the rest of the section use.

::: {.second-reading title="Non-example by minimal change: drop (F6)"}
Keep every clause of a commutative ring except (F6), together with the distributive law on the other side, \( (a + b)c = ac + bc \), which (F6) used to supply. Then the theorem fails already at \( n = 2 \). Expanding by the two distributive laws gives \( (x + y)^2 = x^2 + xy + yx + y^2 \), and the theorem's middle term \( 2 \cdot (xy) = xy + xy \) agrees with \( xy + yx \) exactly when \( yx = xy \). The \( 2 \times 2 \) real matrices
\[
X = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} , \qquad Y = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}
\]
live in a system with all of these laws under the usual matrix operations, and here \( X^2 = Y^2 = 0 \), while \( (X + Y)^2 \) is the identity matrix and \( 2 \cdot (XY) \) has entries \( 2, 0, 0, 0 \). Everything else in the proof survives: Pascal's rule, the sum rules and the bookkeeping with \( u_k \) and \( w_k \). Only the regrouping \( x^k y^{n-k} x = x^{k+1} y^{n-k} \) breaks, and this is why the statement asks for a commutative ring.
:::

::: {#exm-binomial-expansions}
[Three expansions]

(a) Expand \( (a + b)^4 \) in \( \nZ \). (b) Expand \( (x - 1)^5 \) in \( \nR \). (c) Compute \( 11^4 \) from row \( 4 \) of the table.
:::

::: {.solution}
(a) The theorem with \( n = 4 \) and row \( 4 \), \( 1, 4, 6, 4, 1 \), gives, from \( k = 4 \) down to \( k = 0 \),
\[
(a + b)^4 = a^4 + 4a^3 b + 6a^2 b^2 + 4ab^3 + b^4 .
\]

(b) Take \( y = -1 \) in the theorem. The term with index \( k \) is \( \binom{5}{k} x^k (-1)^{5-k} \), and \( (-1)^{5-k} \) is \( -1 \) for \( k = 4, 2, 0 \) and \( 1 \) for \( k = 5, 3, 1 \), since \( (-1)^2 = 1 \) and @fd2:prp-power-laws (a), (b) give \( (-1)^{2i} = 1 \) and \( (-1)^{2i+1} = -1 \). With row \( 5 \), \( 1, 5, 10, 10, 5, 1 \),
\[
(x - 1)^5 = x^5 - 5x^4 + 10x^3 - 10x^2 + 5x - 1 .
\]

(c) Write \( 11 = 10 + 1 \) and take \( x = 10 \), \( y = 1 \):
\[
11^4 = 10^4 + 4 \cdot 10^3 + 6 \cdot 10^2 + 4 \cdot 10 + 1 = 10000 + 4000 + 600 + 40 + 1 = 14641 .
\]
The digits of \( 14641 \) are row \( 4 \), because every coefficient of that row is below \( 10 \) and no carrying occurs.
:::

::: {.check}
Write row \( 7 \) from row \( 6 \) by Pascal's rule, and check \( \binom{7}{3} \) by the formula of @prp-binomial-factorial.
:::

::: {.solution}
Row \( 6 \) is \( 1, 6, 15, 20, 15, 6, 1 \), so row \( 7 \) is \( 1, 7, 21, 35, 35, 21, 7, 1 \) (for instance \( \binom{7}{3} = \binom{6}{2} + \binom{6}{3} = 15 + 20 \)). By the formula, \( \binom{7}{3} = \frac{7!}{3! \, 4!} = \frac{5040}{6 \cdot 24} = \frac{5040}{144} = 35 \).
:::

::: {.warning}
The rule \( (x + y)^n = x^n + y^n \) is false in \( \nR \) for every \( n \ge 2 \): with \( x = y = 1 \) it would give \( 2^n = 2 \), while \( 2^n > 2^1 = 2 \) for \( n \ge 2 \) (@fd2:prp-power-laws (e)); at \( n = 2 \), \( (1 + 1)^2 = 4 \ne 2 \). The theorem says what is missing: the middle terms \( \binom{n}{k} x^k y^{n-k} \) with \( 0 < k < n \). Chapter 4 finds the rings in which those middle terms all vanish for \( n = p \), a prime.
:::

## Consequences in the real numbers

In \( \nR \) the theorem gives exact sums of binomial coefficients, and, for \( x \ge 0 \), lower bounds for \( (1 + x)^n \): every term of the expansion is then non-negative, and a sum of non-negative terms is at least any part of it. These lower bounds are what Section 1.4 needs.

::: {#cor-binomial-real}
[Binomial Sums and Lower Bounds]

Let \( n \in \nN \).

::: {.enumerate options="label=(\alph*)"}
1. \( \sum_{k=0}^{n} \binom{n}{k} = 2^n \), and \( \sum_{k=0}^{n} (-1)^k \binom{n}{k} = 0 \) if \( n \ge 1 \).
2. If \( x \in \nR \), \( x \ge 0 \) and \( k \le n \), then \( (1 + x)^n \ge \binom{n}{k} x^k \).
3. If \( x \in \nR \), \( x \ge 0 \) and \( n \ge 2 \), then \( (1 + x)^n \ge 1 + nx + \frac{n(n-1)}{2} x^2 \).
:::
:::

::: {.proof}
We apply @thm-binomial-commutative-ring in \( R = \nR \).

(a) With \( x = y = 1 \), every \( x^k y^{n-k} \) is \( 1 \), since \( 1^m = 1 \) for every \( m \), so \( 2^n = (1 + 1)^n = \sum_{k=0}^{n} \binom{n}{k} \). With \( x = -1 \) and \( y = 1 \), \( (-1 + 1)^n = 0^n \), and for \( n \ge 1 \), \( 0^n = 0^{n-1} \cdot 0 = 0 \). So \( 0 = \sum_{k=0}^{n} (-1)^k \binom{n}{k} \).

(b), (c) With \( y = 1 \), \( (x + 1)^n = \sum_{j=0}^{n} \binom{n}{j} x^j \). For \( x \ge 0 \) each term is \( \ge 0 \): \( \binom{n}{j} \ge 0 \) is a natural number, and \( x^j \ge 0 \) (for \( x > 0 \) by @fd2:prp-power-laws (e); for \( x = 0 \), \( x^j \) is \( 1 \) or \( 0 \)), so the product is \( \ge 0 \) by @fd3:prp-ordered-field-halves (d). By @prp-sum-order (b), the sum is at least its single term \( j = k \), which is (b). By the same part with \( m = 2 \le n \), it is at least the sum of its terms \( j = 0, 1, 2 \), which is \( 1 + \binom{n}{1} x + \binom{n}{2} x^2 \). Finally \( \binom{n}{1} = n \) by the third fact after @def-binomial-coefficients, and \( \binom{n}{2} \cdot 2 = n(n - 1) \) by @prp-binomial-factorial (c) with \( k = 2 \), so \( \binom{n}{2} = \frac{n(n-1)}{2} \). This proves (c).
:::

Keeping only the first two terms (@prp-sum-order (b) with \( m = 1 \), for \( n \ge 1 \)) gives \( (1 + x)^n \ge 1 + nx \) for \( x \ge 0 \), which is @fd2:thm-bernoulli on that range. Bernoulli's inequality also covers \( -1 \le x < 0 \), and the expansion cannot reach that range: for \( x < 0 \) the terms \( \binom{n}{j} x^j \) alternate in sign, and dropping some of them may raise the sum instead of lowering it.

::: {.check}
With \( n = 5 \) and \( x = 2 \), which \( k \) gives the best lower bound for \( 3^5 \) from (b)?
:::

::: {.solution}
The bound is \( \binom{5}{k} 2^k \), which for \( k = 0, 1, \dots, 5 \) is \( 1, 10, 40, 80, 80, 32 \). The best choices are \( k = 3 \) and \( k = 4 \), both giving \( 3^5 = 243 \ge 80 \). A single term loses a lot; Section 1.4 only ever needs a bound that grows fast enough, not a sharp one.
:::

::: {#exm-binomial-bound}
[Powers of two beat n squared]

Show that \( 2^n \ge \frac{n(n-1)}{2} \), and hence \( \frac{n}{2^n} \le \frac{2}{n - 1} \), for every integer \( n \ge 2 \).
:::

::: {.solution}
Let \( n \ge 2 \). By @cor-binomial-real (b) with \( x = 1 \) and \( k = 2 \le n \), \( 2^n = (1 + 1)^n \ge \binom{n}{2} = \frac{n(n-1)}{2} \). Both sides are positive (\( n(n - 1) \ge 2 \)), so @fd3:prp-ordered-field-halves (c) inverts the inequality: \( \frac{1}{2^n} \le \frac{2}{n(n-1)} \). Multiplying by \( n > 0 \) gives \( \frac{n}{2^n} \le \frac{2}{n - 1} \). For instance, at \( n = 5 \): \( \frac{5}{32} \le \frac{2}{4} \).

The right side \( \frac{2}{n - 1} \) can be made as small as we like by taking \( n \) large, and Section 1.4 turns this into the limit \( n/2^n \to 0 \).
:::

## Exercises

### A. Check your understanding

::: {#exr-binomial-theorem-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. In the proof of @thm-binomial-commutative-ring, why is \( u_0 \coloneqq 0 \) put in, and where is it used?
2. Where does the proof use (F6)?
3. Run the induction step from \( n = 1 \) to \( n = 2 \): list \( u_0, u_1, u_2 \) and \( w_0, w_1, w_2 \), and add them.
4. True or false: \( \binom{n}{k} = \binom{n}{n-k} \) for all \( n, k \in \nN \) with \( k \le n \). Give the reason.
:::
:::

::: {.solution}
(a) The sum \( \sum_{k=0}^{n} t_k x \) is \( u_1 + \dots + u_{n+1} \), which starts at index \( 1 \). Putting in \( u_0 = 0 \) turns it into \( \sum_{k=0}^{n+1} u_k \) by @lem-ring-finite-sums (f) (split off the first term, which is \( 0 \)). That is a sum over the same range \( 0 \le k \le n + 1 \) as \( \sum w_k \), so the two can be added termwise by @lem-ring-finite-sums (a).

(b) In computing \( t_k x \): the product \( (x^k y^{n-k}) x \) becomes \( x^{k+1} y^{n-k} \) only after \( x \) is moved past \( y^{n-k} \), which is (F6). It is also used to bring the factor \( x \) (and \( y \)) to the left of the sum, where @lem-ring-finite-sums (b) has it. The first use is the one the theorem cannot do without: for matrices that do not commute, \( (x + y)^2 = x^2 + xy + yx + y^2 \), and \( xy + yx \ne 2 \cdot xy \).

(c) For \( n = 1 \), \( z_k = x^k y^{2-k} \). Then \( u_0 = 0 \), \( u_1 = \binom{1}{0} \cdot z_1 = xy \), \( u_2 = \binom{1}{1} \cdot z_2 = x^2 \); and \( w_0 = \binom{1}{0} \cdot z_0 = y^2 \), \( w_1 = \binom{1}{1} \cdot z_1 = xy \), \( w_2 = \binom{1}{2} \cdot z_2 = 0 \). The sum is \( y^2 + 2 \cdot (xy) + x^2 \), with coefficients \( 1, 2, 1 \), row \( 2 \).

(d) True, by @prp-binomial-factorial (b). Each row of the table reads the same from both ends.
:::

### B. Practice

::: {#exr-binomial-theorem-b1}
[B1: Expansions]

(a) Write \( (2x - 1)^5 \), for \( x \in \nR \), as a sum of six terms. What multiplies \( x^3 \)? (b) Compute \( \sum_{k=0}^{n} \binom{n}{k} 3^k \) for \( n \in \nN \).
:::

::: {.solution}
(a) By @thm-binomial-commutative-ring with \( 2x \) in place of \( x \) and \( y = -1 \), and \( (2x)^k = 2^k x^k \) (@fd2:prp-power-laws (c)),
\[
(2x - 1)^5 = \sum_{k=0}^{5} \binom{5}{k} 2^k (-1)^{5-k} x^k .
\]
The term with \( k = 3 \) is \( \binom{5}{3} \cdot 8 \cdot (-1)^2 \, x^3 = 80 x^3 \), so \( 80 \) multiplies \( x^3 \).

(b) By the theorem with \( x = 3 \) and \( y = 1 \), the sum is \( (3 + 1)^n = 4^n \). Check \( n = 2 \): \( 1 + 2 \cdot 3 + 9 = 16 \).
:::

::: {#exr-binomial-theorem-b2}
[B2: An absorbed sum]

Show that \( \sum_{k=1}^{n} k \binom{n}{k} = n \, 2^{n-1} \) for every integer \( n \ge 1 \).

*Hint: absorption.*
:::

::: {.solution}
Let \( n \ge 1 \). Shift the index by \( k = j + 1 \) (@fd2:def-sum-product): the sum is \( \sum_{j=0}^{n-1} (j + 1) \binom{n}{j+1} \). By @prp-binomial-absorption with \( n - 1 \in \nN \) in place of \( n \), \( (j + 1) \binom{(n-1)+1}{j+1} = n \binom{n-1}{j} \). So, by @lem-ring-finite-sums (b) and @cor-binomial-real (a) for \( n - 1 \),
\[
\sum_{k=1}^{n} k \binom{n}{k} = \sum_{j=0}^{n-1} n \binom{n-1}{j} = n \sum_{j=0}^{n-1} \binom{n-1}{j} = n \, 2^{n-1} .
\]
Check \( n = 3 \): \( 1 \cdot 3 + 2 \cdot 3 + 3 \cdot 1 = 12 = 3 \cdot 4 \).
:::

::: {#exr-binomial-theorem-b3}
[B3: A numerical lower bound]

Show that \( (1.01)^{10} \ge 1.1045 \) without multiplying out the power.
:::

::: {.solution}
Apply @cor-binomial-real (c) with \( x = 0.01 \ge 0 \) and \( n = 10 \ge 2 \): \( \frac{n(n-1)}{2} = 45 \), and
\[
(1.01)^{10} \ge 1 + 10 \cdot 0.01 + 45 \cdot 0.0001 = 1 + 0.1 + 0.0045 = 1.1045 .
\]
:::

### C. Going deeper

::: {#exr-binomial-theorem-c1}
[C1: Exit check: absorption twice]

Prove that \( \sum_{k=0}^{n} k(k - 1) \binom{n}{k} = n(n - 1) \, 2^{n-2} \) for every integer \( n \ge 2 \).
:::

::: {.solution}
Let \( n \ge 2 \), and write \( a_k \coloneqq k(k - 1) \binom{n}{k} \). The terms \( a_0 \) and \( a_1 \) are \( 0 \), so by @prp-sum-reindex (b) with \( m = 1 \),
\[
\sum_{k=0}^{n} a_k = (a_0 + a_1) + \sum_{k=2}^{n} a_k = \sum_{k=2}^{n} a_k .
\]
Let \( 2 \le k \le n \). By @prp-binomial-absorption with \( n - 1 \) in place of \( n \) and \( k - 1 \) in place of \( k \) (both in \( \nN \), as \( n, k \ge 1 \)), \( k \binom{n}{k} = n \binom{n-1}{k-1} \). Applied again with \( n - 2 \) and \( k - 2 \) (in \( \nN \), as \( n, k \ge 2 \)), \( (k - 1) \binom{n-1}{k-1} = (n - 1) \binom{n-2}{k-2} \). Hence
\[
a_k = (k - 1) \cdot k \binom{n}{k} = n \, (k - 1) \binom{n-1}{k-1} = n(n - 1) \binom{n-2}{k-2} .
\]
Shifting the index by \( j = k - 2 \) (@fd2:def-sum-product) and using @lem-ring-finite-sums (b) and @cor-binomial-real (a) for \( n - 2 \),
\[
\sum_{k=2}^{n} a_k = n(n - 1) \sum_{j=0}^{n-2} \binom{n-2}{j} = n(n - 1) \, 2^{n-2} .
\]
Check \( n = 3 \): \( a_2 + a_3 = 2 \cdot 3 + 6 \cdot 1 = 12 = 6 \cdot 2 \).

**Marking scheme.** (10 points)
- 2: the terms \( k = 0, 1 \) are shown to be \( 0 \) and split off, with the splitting rule cited.
- 3: the first absorption, \( k \binom{n}{k} = n \binom{n-1}{k-1} \), with its range \( k \ge 1 \) stated.
- 3: the second absorption, \( (k - 1) \binom{n-1}{k-1} = (n - 1) \binom{n-2}{k-2} \), with its range \( k \ge 2 \), \( n \ge 2 \) stated.
- 2: the index shift and the row sum @cor-binomial-real (a) for \( n - 2 \).
A route through @prp-binomial-factorial (c) earns the absorption points for the equivalent identity \( k(k - 1) \binom{n}{k} = n(n - 1) \binom{n-2}{k-2} \), proved for \( k \ge 2 \). Fatal error (0 for the step): applying absorption at \( k = 0 \), where it would need \( \binom{n-1}{-1} \).
:::

<!-- dependency ledger
def-binomial-coefficients (claim): the three facts C(n, k) = 0 for k > n, C(n, n) = 1, C(n, 1) = n; table rows 0-6 | inline inductions; verify/ch01/def-binomial-coefficients.py
prp-binomial-absorption (proof): arithmetic in N (distributivity, (j + 2) = (j + 1) + 1) | arithmetic of omega, fd3:cor-omega-identification (c); fd2:lem-naturals-arithmetic read on omega
prp-binomial-absorption (idea): 1 * 3 = 3 * 1; 2 * 6 = 4 * 3 | verify/ch01/prp-binomial-absorption.py
prp-binomial-factorial (proof): factorial recursion (n + 1)! = n! (n + 1); empty product 1 | fd2:def-sum-product (product recursion, n! as a product)
prp-binomial-factorial (proof): n! is a positive integer for every n in N | fd2:thm-primes-infinite, proof Step 1 (inline induction), with fd2:prp-integers-closed (b)
prp-binomial-factorial (proof): (n + 1) - (j + 1) = n - j; n - (n - k) = k; arithmetic and commutativity in N and Z | arithmetic of omega, fd3:cor-omega-identification (c); fd3:thm-integers-ordered-ring
prp-binomial-factorial (proof): a product of positive integers is a positive integer | fd2:prp-integers-closed (a), (b)
thm-binomial-commutative-ring (proof): x^k x = x^{k+1}, y^{n-k} y = y^{n+1-k}, (n + 1) - (k + 1) = n - k | power recursion (prp-power-laws-commutative-ring, Section 1.1); arithmetic of omega, fd3:cor-omega-identification (c)
thm-binomial-commutative-ring (proof): 1 . a = a and 0 . a = 0 for natural multiples | recursion for n . a (fd3 Section 2.4, "Multiples"), inline
thm-binomial-commutative-ring (claim): matrix multiplication is not commutative, the expansion needs commuting pairs | linear-algebra volumes, prose comparison only; nothing depends on it
thm-binomial-commutative-ring (example): (fold) 2x2 matrices X, Y: X^2 = Y^2 = 0, (X + Y)^2 = I, 2XY = diag(2, 0); matrix rings satisfy (F1)-(F5), (F7), (F9) | linear-algebra volumes (school matrix arithmetic), fold only, nothing depends on it; verify/ch01/thm-binomial-commutative-ring.py
thm-binomial-commutative-ring (claim): in Z and R, m . z = mz since m . 1 = m | NOTATION n . a row (fd3 Section 2.4); fd3:def-naturals-in-ordered-field
exm-binomial-expansions (example): (-1)^{2i} = 1, (-1)^{2i+1} = -1; rows 4 and 5; 11^4 = 14641 | fd2:prp-power-laws (a), (b) with (-1)^2 = 1 (fd3:prp-ring-algebra (c)); verify/ch01/exm-binomial-expansions.py
prp-binomial-factorial (claim): (check) row 7; 7! = 5040, 3! 4! = 144, 5040 / 144 = 35 | verify/ch01/prp-binomial-factorial.py
cor-binomial-real (proof): 1^m = 1; 0^n = 0 for n >= 1 | power recursion, inline induction; fd3:prp-ring-algebra (b)
cor-binomial-real (proof): 0^j is 1 (j = 0) or 0 (j >= 1) | power recursion, inline
cor-binomial-real (claim): (check) C(5, k) 2^k = 1, 10, 40, 80, 80, 32; 3^5 = 243 | verify/ch01/cor-binomial-real.py
cor-binomial-real (claim): for x < 0 the terms C(n, j) x^j alternate in sign | sign of x^j by fd2:prp-power-laws (a), (b) and fd3:prp-ordered-ring-rules (c), (d); prose remark, nothing depends on it
exm-binomial-bound (solution): n(n - 1) >= 2 for n >= 2; 5/32 <= 2/4 | arithmetic of N read in R (fd3:prp-naturals-in-ordered-field (a), (b)); verify/ch01/exm-binomial-bound.py
exr-binomial-theorem-a1 (solution): run of the step n = 1 to n = 2; (x + y)^2 = x^2 + xy + yx + y^2 for matrices | verify/ch01/exr-binomial-theorem-a1.py; matrices: linear-algebra volumes, prose only
exr-binomial-theorem-b1 (solution): (2x)^k = 2^k x^k; x^3 coefficient 80; n = 2 check 16 | fd2:prp-power-laws (c); verify/ch01/exr-binomial-theorem-b1.py
exr-binomial-theorem-b2 (solution): shift of index k = j + 1 | fd2:def-sum-product (general bounds); verify/ch01/exr-binomial-theorem-b2.py
exr-binomial-theorem-b3 (solution): 1 + 0.1 + 0.0045 = 1.1045; C(10, 2) = 45 | verify/ch01/exr-binomial-theorem-b3.py
exr-binomial-theorem-c1 (solution): shift of index j = k - 2; n = 3 check 12 | fd2:def-sum-product (general bounds); verify/ch01/exr-binomial-theorem-c1.py
-->
