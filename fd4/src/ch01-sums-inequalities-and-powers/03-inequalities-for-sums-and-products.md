# Inequalities for Sums and Products

Bernoulli's inequality (@fd2:thm-bernoulli) compares a power with a linear function: \( (1 + x)^n \ge 1 + nx \) whenever \( x \ge -1 \). Estimates in analysis keep needing comparisons of this kind, and they usually need a little more than the plain statement gives. This section first sharpens Bernoulli's inequality to a strict one. It then extends the inequality from a power of one factor to a product of different factors. Finally it uses Bernoulli's inequality to prove the inequality between the arithmetic and the geometric mean. That last inequality is the tool for bounding a product by a power. The inequality of Cauchy and Schwarz, which bounds a sum of products, waits for vectors in Chapter 9.

## Bernoulli's inequality, sharpened and extended

The proof of @fd2:thm-bernoulli multiplied out \( (1 + nx)(1 + x) = 1 + (n + 1)x + nx^2 \) and threw away the term \( nx^2 \) because it is non-negative. When \( x \ne 0 \) and \( n \ge 1 \), that term is positive, and something is lost by throwing it away. For example, at \( x = \frac12 \) and \( n = 2 \), the power is \( \bigl(\frac32\bigr)^2 = \frac94 \), while \( 1 + 2 \cdot \frac12 = 2 \). Keeping the term gives a strict inequality.

::: {#lem-bernoulli-strict}
[Strict Bernoulli Inequality]

Let \( x \in \nR \) with \( x \ge -1 \) and \( x \ne 0 \). Then \( (1 + x)^n > 1 + nx \) for every integer \( n \ge 2 \).
:::

::: {.idea}
The induction of @fd2:thm-bernoulli runs again from the base \( n = 2 \). The term it discarded, \( nx^2 \), is now strictly positive, and that is where the strictness comes from.
:::

::: {.proof}
We use @fd2:thm-induction with base \( 2 \). For \( n = 2 \),
\[
(1 + x)^2 = 1 + 2x + x^2 > 1 + 2x ,
\]
because \( x^2 > 0 \) for \( x \ne 0 \): the square of a nonzero number is positive.

Let \( n \ge 2 \) and suppose \( (1 + x)^n > 1 + nx \). Since \( x \ge -1 \), we have \( 1 + x \ge 0 \). Multiplying an inequality by a non-negative number keeps its direction, though perhaps not its strictness. If \( 1 + x > 0 \), multiplying by it keeps the inequality strict. If \( 1 + x = 0 \), both sides become \( 0 \). So
\[
\begin{aligned}
(1 + x)^{n+1} &= (1 + x)^n (1 + x) \ge (1 + nx)(1 + x) \\
&= 1 + (n + 1)x + nx^2 > 1 + (n + 1)x ,
\end{aligned}
\]
where the last step holds because \( n > 0 \) and \( x^2 > 0 \), so \( nx^2 > 0 \). The strictness of the conclusion comes from this last step, not from the hypothesis. This proves the lemma for every \( n \ge 2 \).

::: {.uses}
@fd3:prp-ordered-ring-rules (c), (e), (h): signs of products and squares. @fd3:prp-ring-algebra (b): times zero is zero.
:::
:::

At \( x = -1 \) the lemma says \( 0 > 1 - n \), which is true for \( n \ge 2 \): the endpoint is allowed, and the proof used it only through \( 1 + x \ge 0 \).

::: {.check}
Why does the lemma exclude \( x = 0 \) and \( n = 1 \)?
:::

::: {.solution}
Both give equality, so a strict inequality would be false. For \( x = 0 \): \( (1 + 0)^n = 1 = 1 + n \cdot 0 \). For \( n = 1 \): \( (1 + x)^1 = 1 + x = 1 + 1 \cdot x \). (For \( n = 0 \) both sides are \( 1 \) as well.)
:::

Put \( x = -a \) with \( 0 \le a \le 1 \). Bernoulli's inequality becomes \( (1 - a)^n \ge 1 - na \): a product of \( n \) equal factors just below \( 1 \) is at least \( 1 \) minus the total of what each factor misses. The same holds when the factors differ. For example, \( (1 - 0.1)(1 - 0.2) = 0.72 \), which is at least \( 1 - (0.1 + 0.2) = 0.7 \).

::: {#prp-weierstrass-product}
[Products of Factors Below One]

Let \( n \in \nN \) and \( a_1, \dots, a_n \in \nR \) with \( 0 \le a_k \le 1 \) for every \( k \). Then
\[
\prod_{k=1}^{n} (1 - a_k) \ge 1 - \sum_{k=1}^{n} a_k .
\]
:::

::: {.idea}
Induct on \( n \), as for Bernoulli: multiply the hypothesis by the next factor \( 1 - a_{n+1} \), which is non-negative, and throw away the cross term \( s\, a_{n+1} \), which is non-negative too.
:::

::: {.proof}
We induct on \( n \in \nN \) (@fd1:ax-induction). For \( n = 0 \) the product is empty and the sum is empty, so the claim reads \( 1 \ge 1 - 0 \).

Suppose the claim holds for \( n \), and let \( a_1, \dots, a_{n+1} \in [0, 1] \). Write \( s \coloneqq \sum_{k=1}^{n} a_k \). Every \( a_k \ge 0 \), so \( s \) is at least the sum of \( n \) zeros, that is, \( s \ge 0 \). Since \( a_{n+1} \le 1 \), the factor \( 1 - a_{n+1} \) is non-negative. Multiplying the hypothesis \( \prod_{k=1}^{n} (1 - a_k) \ge 1 - s \) by it keeps the direction: by @fd3:prp-ordered-ring-rules (c) if the factor is positive, and both sides become \( 0 \) if it is \( 0 \). Splitting off the last factor of the product, we get
\[
\begin{aligned}
\prod_{k=1}^{n+1} (1 - a_k) &\ge (1 - s)(1 - a_{n+1}) = 1 - s - a_{n+1} + s\, a_{n+1} \\
&\ge 1 - (s + a_{n+1}) = 1 - \sum_{k=1}^{n+1} a_k ,
\end{aligned}
\]
where the second inequality drops \( s\, a_{n+1} \ge 0 \), a product of two non-negative numbers. This is the claim for \( n + 1 \).

::: {.uses}
@prp-sum-order (a): sums respect order. @fd3:prp-ordered-ring-rules (c): multiplying by a positive. @fd3:prp-ring-algebra (b): times zero is zero. @fd2:def-sum-product: empty and last factor.
:::
:::

With all \( a_k \) equal to \( a \), the proposition is Bernoulli's inequality at \( x = -a \). It is useful when the \( a_k \) are small and their sum is under control, for then the product stays close to \( 1 \). The analysis volumes use it to study infinite products, products of infinitely many factors \( 1 - a_k \).

::: {.check}
Bound \( 0.99 \cdot 0.98 \cdot 0.97 \cdot 0.96 \) from below by the proposition.
:::

::: {.solution}
Take \( a_1 = 0.01 \), \( a_2 = 0.02 \), \( a_3 = 0.03 \), \( a_4 = 0.04 \), all in \( [0, 1] \). Their sum is \( 0.10 \), so the product is at least \( 1 - 0.10 = 0.90 \). Multiplying out gives about \( 0.9035 \), so the bound loses very little.
:::

## The arithmetic and geometric means

A rectangle with perimeter \( 4 \) has sides \( a \) and \( b \) with \( a + b = 2 \). Its area \( ab \) is at most \( 1 \), the area of the square with the same perimeter. In general, for real \( a, b \),
\[
\Bigl(\frac{a + b}{2}\Bigr)^2 - ab = \frac{a^2 + 2ab + b^2 - 4ab}{4} = \Bigl(\frac{a - b}{2}\Bigr)^2 \ge 0 ,
\]
so \( ab \le \bigl(\frac{a + b}{2}\bigr)^2 \), with equality exactly when \( a = b \). A product of two numbers is at most the square of their average.

For three numbers we would like \( abc \le \bigl(\frac{a + b + c}{3}\bigr)^3 \), and for \( n \) numbers the analogous statement. A single square no longer does the job: the difference of the two sides is not a square of anything simple. Still, it holds in examples: the numbers \( 1, 2, 6 \) have average \( 3 \), and \( 1 \cdot 2 \cdot 6 = 12 \le 27 = 3^3 \). We need a proof that handles every \( n \) at once.

*A product is at most the matching power of the average.* In plain words: if \( n \) numbers are non-negative, their product is at most their average raised to the power \( n \).

::: {#thm-am-gm}
[Arithmetic and Geometric Means]

Let \( n \ge 1 \) be an integer, let \( a_1, \dots, a_n \in \nR \) with \( a_k \ge 0 \) for **every** \( k \), and let \( A \coloneqq \frac{1}{n} \sum_{k=1}^{n} a_k \).

::: {.enumerate options="label=(\alph*)"}
1. \( a_1 a_2 \cdots a_n \le A^n \).
2. Equality holds in (a) **if and only if** \( a_1 = a_2 = \dots = a_n \).
:::
:::

The number \( A \) is the **arithmetic mean** of \( a_1, \dots, a_n \). The **geometric mean** is the non-negative number whose \( n \)-th power is the product \( a_1 \cdots a_n \). Once \( n \)-th roots are available (Section 1.5), (a) says that the geometric mean is at most the arithmetic mean.

*Try it first (ten minutes): prove (a) for \( n = 3 \), or explain what goes wrong when you add a third number to the case \( n = 2 \).*

::: {.idea}
[Scratch work]

The natural attempt is induction on \( n \). Write \( A_m \coloneqq \frac{1}{m} \sum_{k=1}^{m} a_k \) for the mean of the first \( m \) numbers, and suppose \( a_1 \cdots a_n \le A_n^n \). Multiplying by \( a_{n+1} \ge 0 \) gives \( a_1 \cdots a_{n+1} \le A_n^n\, a_{n+1} \). To finish we would need
\[
A_n^n\, a_{n+1} \le A_{n+1}^{n+1} ,
\]
a comparison between means of different lengths. This is where the attempt stalls: nothing in the hypothesis speaks about \( A_{n+1} \).

Suppose for now that every \( a_k > 0 \), so that \( A_n > 0 \), and divide the missing inequality by \( A_n^{n+1} \). It becomes
\[
\Bigl(\frac{A_{n+1}}{A_n}\Bigr)^{n+1} \ge \frac{a_{n+1}}{A_n} ,
\]
a power on the left and something linear on the right: the shape of Bernoulli's inequality. So set \( x \coloneqq \frac{A_{n+1}}{A_n} - 1 \), which makes the left side \( (1 + x)^{n+1} \). Since \( (n + 1)A_{n+1} = nA_n + a_{n+1} \),
\[
(n + 1)x = \frac{(n + 1)A_{n+1} - (n + 1)A_n}{A_n} = \frac{a_{n+1} - A_n}{A_n} ,
\]
so \( 1 + (n + 1)x = \frac{a_{n+1}}{A_n} \), exactly the right side. Bernoulli closes the gap.

| We know | We want |
|---|---|
| every \( a_k > 0 \); \( a_1 \cdots a_n \le A_n^n \) | \( a_1 \cdots a_{n+1} \le A_{n+1}^{n+1} \) |
| multiply by \( a_{n+1} > 0 \): \( a_1 \cdots a_{n+1} \le A_n^n\, a_{n+1} \) | enough: \( A_n^n\, a_{n+1} \le A_{n+1}^{n+1} \) |
| \( x \coloneqq A_{n+1}/A_n - 1 > -1 \); Bernoulli with exponent \( n + 1 \) | \( (1 + x)^{n+1} \ge 1 + (n + 1)x = a_{n+1}/A_n \): the gap closes |

Zeros are handled first and separately: a zero factor makes the product \( 0 \).

*Before reading on: where will \( x > -1 \) be needed, and why is it true?*
:::

::: {.proof}
(a) If \( a_j = 0 \) for some \( j \), the product \( a_1 \cdots a_n \) is \( 0 \). Also \( A \ge 0 \), since the sum of the \( a_k \) is non-negative and \( \frac1n > 0 \). So \( A^n \ge 0 \). If \( A > 0 \), this holds because every power of a positive number is positive. If \( A = 0 \), it holds because \( 0^n = 0 \) for \( n \ge 1 \). Hence \( a_1 \cdots a_n = 0 \le A^n \).

It remains to treat lists of positive numbers. For \( m \ge 1 \) let \( A_m \coloneqq \frac{1}{m} \sum_{k=1}^{m} a_k \). We prove by induction from base \( 1 \) (@fd2:thm-induction) that \( a_1 \cdots a_n \le A_n^n \) for every integer \( n \ge 1 \) and **all** positive \( a_1, \dots, a_n \). For \( n = 1 \), \( a_1 = A_1 \).

Let \( n \ge 1 \), suppose the claim for \( n \), and let \( a_1, \dots, a_{n+1} > 0 \). Then \( A_n > 0 \) and \( A_{n+1} > 0 \), as means of positive numbers. Put \( x \coloneqq A_{n+1}/A_n - 1 \). Then \( 1 + x = A_{n+1}/A_n > 0 \), so \( x > -1 \), and from \( (n + 1)A_{n+1} = nA_n + a_{n+1} \) we get \( 1 + (n + 1)x = a_{n+1}/A_n \). By @fd2:thm-bernoulli with exponent \( n + 1 \),
\[
\Bigl(\frac{A_{n+1}}{A_n}\Bigr)^{n+1} \ge \frac{a_{n+1}}{A_n} .
\]
Multiply both sides by \( A_n^{n+1} \), which is positive because \( A_n > 0 \). Multiplying by a positive number keeps the inequality: a strict inequality stays strict, and an equality stays an equality. The power laws give \( \bigl(A_{n+1}/A_n\bigr)^{n+1} A_n^{n+1} = A_{n+1}^{n+1} \) and \( A_n^{n+1} \cdot a_{n+1}/A_n = A_n^n\, a_{n+1} \). So the inequality becomes \( A_{n+1}^{n+1} \ge A_n^n\, a_{n+1} \). Multiplying the induction hypothesis by \( a_{n+1} > 0 \) gives the other half, and together
\[
a_1 \cdots a_n\, a_{n+1} \le A_n^n\, a_{n+1} \le A_{n+1}^{n+1} .
\]
This is the claim for \( n + 1 \), and (a) is proved.

(b) \( (\Leftarrow) \) If every \( a_k \) equals \( a \), then \( A = \frac1n (na) = a \), and both sides of (a) are \( a^n \).

\( (\Rightarrow) \) We prove the contrapositive: if the \( a_k \) are not all equal, then \( a_1 \cdots a_n < A^n \). With a zero among them this is immediate. For positive numbers, the induction of (a) runs again, with the strict Bernoulli inequality (@lem-bernoulli-strict) in place of Bernoulli's inequality. In the step, either the first \( n \) numbers are not all equal, so the induction hypothesis is strict, or they are all equal to \( A_n \), the new number differs from \( A_n \), and the strict Bernoulli inequality applies.

::: {.uses}
@prp-sum-order (a): sums respect order. @fd2:prp-power-laws (e): powers of positives. @fd3:prp-ordered-ring-rules (c), (h): multiplying by a positive; \( m > 0 \). @fd3:prp-reciprocal-order (a): \( \frac1m > 0 \). @prp-power-laws-commutative-ring (a), (c): power laws.
:::
:::

::: {.second-reading title="The equality case of the means"}
Suppose \( a_1, \dots, a_n \ge 0 \) are not all equal; we show \( a_1 \cdots a_n < A^n \).

If some \( a_j = 0 \), then some \( a_i \ne 0 \), since the numbers are not all equal; so \( a_i > 0 \). The sum of the \( a_k \) is then positive, because one term is positive and none is negative. So \( A > 0 \), and \( A^n > 0 = a_1 \cdots a_n \).

If every \( a_k > 0 \), we use induction from base \( 2 \) (@fd2:thm-induction). The claim for \( n \ge 2 \) is: for all positive \( a_1, \dots, a_n \) that are not all equal, \( a_1 \cdots a_n < A_n^n \). (For \( n = 1 \) there is nothing to prove: one number is always "all equal".) For \( n = 2 \), \( a_1 \ne a_2 \), and the computation before the theorem gives \( A_2^2 - a_1 a_2 = \bigl(\frac{a_1 - a_2}{2}\bigr)^2 > 0 \), since the square of a nonzero number is positive.

Let \( n \ge 2 \), suppose the claim for \( n \), and let \( a_1, \dots, a_{n+1} > 0 \) be not all equal. The proof of (a) gave the chain
\[
a_1 \cdots a_n\, a_{n+1} \le A_n^n\, a_{n+1} \le A_{n+1}^{n+1} ,
\]
and it is enough to make one of its two inequalities strict.

*Case 1: \( a_1, \dots, a_n \) are not all equal.* By the induction hypothesis \( a_1 \cdots a_n < A_n^n \), and multiplying by \( a_{n+1} > 0 \) keeps it strict. The left inequality is strict.

*Case 2: \( a_1 = \dots = a_n \).* Then each of them equals \( A_n \), so \( a_{n+1} \ne A_n \), since otherwise all \( n + 1 \) numbers would be equal. Hence \( (n + 1)x = (a_{n+1} - A_n)/A_n \ne 0 \), so \( x \ne 0 \); also \( x > -1 \) and \( n + 1 \ge 2 \). So @lem-bernoulli-strict gives \( (1 + x)^{n+1} > 1 + (n + 1)x \), and multiplying by \( A_n^{n+1} > 0 \) as in (a) makes the right inequality strict.

In both cases \( a_1 \cdots a_{n+1} < A_{n+1}^{n+1} \), which is the claim for \( n + 1 \).

::: {.uses}
@prp-sum-order (a): sums respect order. @fd2:prp-power-laws (e): powers of positives. @fd3:prp-ordered-ring-rules (c), (e): signs of products and squares.
:::
:::

The one real step of the proof is the right inequality of the displayed chain, and that step is Bernoulli's inequality after the substitution found in the scratch work. The left inequality is only the induction hypothesis multiplied by \( a_{n+1} \).

::: {#exm-method-am-gm}
[Method: bound a product by a power]

**How it goes.** To bound a product of non-negative factors from above, arrange the factors so that their sum is known, or at least bounded. Then apply @thm-am-gm: the product is at most the \( n \)-th power of their mean. For a strict inequality, check that the factors are not all equal.

**When to use it.** Products such as \( n! \), \( x(1 - x) \) or \( \bigl(1 + \frac1n\bigr)^n \); and any problem that asks for the largest product under a condition on the sum.

**Common mistakes.** One mistake is to apply the theorem to factors that may be negative, where it is false. Another is to choose factors whose sum is not under control. That gives a bound that grows faster than the product.
:::

The first example bounds a factorial. Its factors \( 1, 2, \dots, n \) have a sum we know.

::: {#exm-am-gm-factorial}
[A bound for n factorial]

Show that \( n! \le \bigl(\frac{n + 1}{2}\bigr)^n \) for every integer \( n \ge 1 \), with equality only for \( n = 1 \).
:::

::: {.solution}
Apply @thm-am-gm to the \( n \) numbers \( 1, 2, \dots, n \), all non-negative. Their sum is \( \frac{n(n + 1)}{2} \) (@fd2:prp-sum-first-n), so their mean is \( \frac{n + 1}{2} \), and part (a) gives \( n! = 1 \cdot 2 \cdots n \le \bigl(\frac{n + 1}{2}\bigr)^n \).

By part (b), equality holds exactly when the factors \( 1, \dots, n \) are all equal. For \( n = 1 \) there is one factor, and indeed \( 1! = 1 = 1^1 \). For \( n \ge 2 \) the factors \( 1 \) and \( 2 \) differ, so the inequality is strict; at \( n = 2 \) it reads \( 2 < \frac94 \).
:::

The bound is crude, but it beats the obvious one, \( n! \le n^n \), by a lot: for \( n \ge 2 \), \( \frac{n + 1}{2n} \le \frac34 \), so \( \bigl(\frac{n + 1}{2}\bigr)^n \le \bigl(\frac34\bigr)^n n^n \).

The second example chooses the factors with more care. The sequence \( \bigl(1 + \frac1n\bigr)^n \) begins \( 2, \frac94, \frac{64}{27}, \dots \), and it seems to increase. Its terms are powers, and a power is a product of equal factors; the trick is to add one more factor that brings the length up to \( n + 1 \).

::: {#exm-am-gm-compound}
[The compound-interest sequence increases]

Show that \( \bigl(1 + \frac1n\bigr)^n < \bigl(1 + \frac{1}{n + 1}\bigr)^{n+1} \) for every integer \( n \ge 1 \).
:::

::: {.solution}
Apply @thm-am-gm to the \( n + 1 \) positive numbers
\[
\underbrace{1 + \tfrac1n, \; \dots, \; 1 + \tfrac1n}_{n \text{ times}}, \; 1 .
\]
Their product is \( \bigl(1 + \frac1n\bigr)^n \cdot 1 \). Their sum is \( n\bigl(1 + \frac1n\bigr) + 1 = n + 2 \), so their mean is \( \frac{n + 2}{n + 1} = 1 + \frac{1}{n + 1} \). They are not all equal, since \( 1 + \frac1n \ne 1 \). So part (b) makes part (a) strict:
\[
\Bigl(1 + \frac1n\Bigr)^n < \Bigl(1 + \frac{1}{n + 1}\Bigr)^{n+1} .
\]
:::

The extra factor \( 1 \) changes the product not at all and raises the length by one. That is what makes the mean of length \( n + 1 \) come out as the next term. The sequence is increasing; the exercises of Section 1.5 show that it is bounded above by \( 3 \), and *Analysis on the Real Line*, Chapter 4 proves that it converges.

::: {.warning}
The theorem needs every \( a_k \ge 0 \). For the three numbers \( -1, -1, 1 \), the product is \( 1 \), the mean is \( -\frac13 \), and \( A^3 = -\frac{1}{27} < 1 \). An even number of negative factors can make the product large while the mean stays small.
:::

::: {.check}
Which numbers does the method use to show that \( x(2 - x) \le 1 \) for \( 0 \le x \le 2 \)? When is the inequality an equality?
:::

::: {.solution}
The two numbers \( x \) and \( 2 - x \), both non-negative on \( [0, 2] \). Their sum is \( 2 \) and their mean \( 1 \), so \( x(2 - x) \le 1^2 = 1 \). Equality holds exactly when \( x = 2 - x \), that is, at \( x = 1 \).
:::

::: {.remark}
[Looking ahead]

Chapter 9 proves the Cauchy–Schwarz inequality, which bounds a sum of products \( \sum a_k b_k \) by the sums of squares.
:::

## Exercises

### A. Check your understanding

::: {#exr-inequalities-for-sums-and-products-a1}
[A1]

These parts are about the proof of @thm-am-gm.

::: {.enumerate options="label=(\alph*)"}
1. In the induction step, what is \( x \), and which fact gives \( x > -1 \)?
2. Which step uses that every \( a_k > 0 \), and not just \( a_k \ge 0 \)?
3. Run the step from \( n = 1 \) to \( n = 2 \) with \( a_1 = 1 \) and \( a_2 = 4 \): compute \( A_1 \), \( A_2 \) and \( x \), and the three members of the chain \( a_1 a_2 \le A_1 a_2 \le A_2^2 \).
4. True or false: \( abc \le \bigl(\frac{a + b + c}{3}\bigr)^3 \) for all real \( a, b, c \).
:::
:::

::: {.solution}
(a) \( x = A_{n+1}/A_n - 1 \). Then \( 1 + x = A_{n+1}/A_n \), a quotient of two positive numbers, since \( A_{n+1} \) and \( A_n \) are means of positive numbers. So \( 1 + x > 0 \), that is, \( x > -1 \), which is the hypothesis of Bernoulli's inequality.

(b) The definition of \( x \) divides by \( A_n \), which needs \( A_n \ne 0 \). With zeros allowed, \( A_n \) could be \( 0 \) (take \( a_1 = \dots = a_n = 0 \)). That is why lists with a zero were handled first, by a separate argument.

(c) \( A_1 = 1 \), \( A_2 = \frac52 \), \( x = \frac52 - 1 = \frac32 \). The chain reads \( a_1 a_2 = 4 \le A_1 a_2 = 4 \le A_2^2 = \frac{25}{4} \). The left inequality is an equality here, since the hypothesis \( a_1 \le A_1 \) is one; Bernoulli gives \( \bigl(\frac52\bigr)^2 \ge 1 + 2 \cdot \frac32 = 4 = a_2/A_1 \).

(d) False. For \( a = b = -1 \), \( c = 1 \): \( abc = 1 \), while \( \bigl(-\frac13\bigr)^3 = -\frac1{27} \). The theorem needs non-negative numbers.
:::

### B. Practice

::: {#exr-inequalities-for-sums-and-products-b1}
[B1: Apply the means]

Let \( a, b, c > 0 \). Prove that \( (a + b)(b + c)(c + a) \ge 8abc \).
:::

::: {.solution}
By @thm-am-gm with \( n = 2 \), \( ab \le \bigl(\frac{a + b}{2}\bigr)^2 \), that is, \( 4ab \le (a + b)^2 \). In the same way \( 4bc \le (b + c)^2 \) and \( 4ca \le (c + a)^2 \). All six sides are non-negative, so multiplying the three inequalities (@fd3:prp-ordered-field-halves (d), twice) gives
\[
64\, a^2 b^2 c^2 \le (a + b)^2 (b + c)^2 (c + a)^2 ,
\]
that is, \( (8abc)^2 \le P^2 \) with \( P \coloneqq (a + b)(b + c)(c + a) \). Both \( 8abc \) and \( P \) are positive. If \( P < 8abc \), then \( P^2 < (8abc)^2 \) by @fd3:prp-ordered-ring-rules (g), a contradiction. Hence \( P \ge 8abc \).
:::

::: {#exr-inequalities-for-sums-and-products-b2}
[B2: Prove or disprove]

Prove or disprove each statement.

::: {.enumerate options="label=(\alph*)"}
1. \( \dfrac{x}{y} + \dfrac{y}{x} \ge 2 \) for all real \( x, y > 0 \).
2. \( \prod_{k=1}^{n} (1 - a_k) \le 1 - \sum_{k=1}^{n} a_k \) for every \( n \in \nN \) and all \( a_1, \dots, a_n \in [0, 1] \).
3. \( (1 + x)^3 \ge 1 + 3x + 3x^2 \) for every real \( x \ge -1 \).
4. \( abcd \le \bigl(\frac{a + b + c + d}{4}\bigr)^4 \) for all real \( a, b, c, d \ge 0 \).
:::
:::

::: {.solution}
(a) True. Both \( x/y \) and \( y/x \) are positive and their product is \( 1 \), so @thm-am-gm with \( n = 2 \) gives \( 1 \le u^2 \) for \( u \coloneqq \frac{x/y + y/x}{2} > 0 \). If \( u < 1 \), then \( u^2 < 1 \) by @fd3:prp-ordered-ring-rules (g), a contradiction; so \( u \ge 1 \), that is, \( x/y + y/x \ge 2 \). Directly: \( \frac{x}{y} + \frac{y}{x} - 2 = \frac{x^2 + y^2 - 2xy}{xy} = \frac{(x - y)^2}{xy} \ge 0 \), a square divided by a positive number.

(b) False. Take \( n = 2 \) and \( a_1 = a_2 = \frac12 \): the product is \( \frac14 \), the right side is \( 1 - 1 = 0 \), and \( \frac14 > 0 \). (@prp-weierstrass-product gives the opposite inequality.)

(c) False. Take \( x = -1 \): the left side is \( 0 \), the right side is \( 1 - 3 + 3 = 1 \). In general \( (1 + x)^3 = 1 + 3x + 3x^2 + x^3 \), so the claim holds exactly when \( x^3 \ge 0 \), that is, for \( x \ge 0 \).

(d) True: this is @thm-am-gm (a) with \( n = 4 \).
:::

::: {#exr-inequalities-for-sums-and-products-b3}
[B3: A product near one]

Show that \( \prod_{k=1}^{10} \Bigl(1 - \dfrac{k}{100}\Bigr) \ge 0.45 \).
:::

::: {.solution}
Put \( a_k \coloneqq \frac{k}{100} \) for \( 1 \le k \le 10 \); each lies in \( [0, 1] \). By @fd2:prp-sum-first-n, \( \sum_{k=1}^{10} k = 55 \), so \( \sum_{k=1}^{10} a_k = \frac{55}{100} \). By @prp-weierstrass-product the product is at least \( 1 - 0.55 = 0.45 \).
:::

### C. Going deeper

::: {#exr-inequalities-for-sums-and-products-c1}
[C1: Find the error]

Here is an argument for part (a) of @thm-am-gm when all \( a_k > 0 \). Write \( A_m \) for the mean of \( a_1, \dots, a_m \).

> We induct on \( n \). For \( n = 1 \), \( a_1 = A_1 \). Suppose \( a_1 \cdots a_n \le A_n^n \) for all positive \( a_1, \dots, a_n \), and let \( a_1, \dots, a_{n+1} > 0 \). Multiplying the hypothesis by \( a_{n+1} > 0 \) gives \( a_1 \cdots a_{n+1} \le A_n^n\, a_{n+1} \). Adding a number to a list never lowers its mean, so \( A_n \le A_{n+1} \); and the new number is at most the new mean, so \( a_{n+1} \le A_{n+1} \). Hence \( A_n^n\, a_{n+1} \le A_{n+1}^n A_{n+1} = A_{n+1}^{n+1} \), and \( a_1 \cdots a_{n+1} \le A_{n+1}^{n+1} \).

Is the conclusion true? Does the argument prove it? If not, name the line that fails and give a counterexample to that line.
:::

::: {.solution}
The conclusion is true: it is @thm-am-gm (a). The argument does not prove it.

The base case and the multiplication by \( a_{n+1} \) are correct. The line that fails is the claim that \( A_n \le A_{n+1} \) and \( a_{n+1} \le A_{n+1} \). Each half is false in general:

- for \( a = (2, 1) \): \( A_1 = 2 > A_2 = \frac32 \), so adding a number can lower the mean;
- for \( a = (1, 2) \): \( a_2 = 2 > A_2 = \frac32 \), so the new number can exceed the new mean.

In fact the two halves can hold together only in the dull case. Since \( (n + 1)A_{n+1} = nA_n + a_{n+1} \), the new mean lies between \( A_n \) and \( a_{n+1} \), so if both are at most \( A_{n+1} \), then \( A_n = a_{n+1} = A_{n+1} \). These are counterexamples to the step, not to the claim, which has none. The proof of @thm-am-gm closes the same gap with Bernoulli's inequality.

**What a complete answer needs.** (10 points)

- 3: says that the conclusion is true (citing @thm-am-gm or equivalent) and that the argument nevertheless fails.
- 3: names either half of the line "\( A_n \le A_{n+1} \) and \( a_{n+1} \le A_{n+1} \)" (or the whole line) as the failing step, without blaming the base case or the multiplication by \( a_{n+1} \).
- 4: gives a concrete list on which that line fails (one list for either half earns the points).

Slips that lose the step (0 for the step): calling the conclusion false; offering a "counterexample" to the conclusion; blaming the multiplication by \( a_{n+1} \).
:::

<!-- dependency ledger
lem-bernoulli-strict (proof): multiplying an inequality by 0 gives 0 on both sides | fd3:prp-ring-algebra (b), cited in the Uses line
lem-bernoulli-strict (proof): n > 0 in R for an integer n >= 2 | fd3:prp-ordered-ring-rules (h), cited in the Uses line
prp-weierstrass-product (proof): a product of two non-negative reals is non-negative | fd3:prp-ordered-ring-rules (c) and (O4), with the zero case fd3:prp-ring-algebra (b), cited in the Uses line
prp-weierstrass-product (proof): the empty product is 1 and the empty sum 0 | fd2:def-sum-product
thm-am-gm (proof): 1/m > 0 for an integer m >= 1 | fd3:prp-ordered-ring-rules (h) with fd3:prp-reciprocal-order (a), cited in the Uses line
thm-am-gm (proof): a finite product with a zero factor is 0 | induction on fd2:def-sum-product with fd3:prp-ring-algebra (b)
thm-am-gm (proof): 0^n = 0 for n >= 1 | fd2:def-power, one step
thm-am-gm (proof): (n+1)A_{n+1} = nA_n + a_{n+1} | fd2:def-sum-product and the definition of A_m
thm-am-gm (proof): (A_{n+1}/A_n)^{n+1} A_n^{n+1} = A_{n+1}^{n+1} and A_n^{n+1} a_{n+1}/A_n = A_n^n a_{n+1} | prp-power-laws-commutative-ring (a), (c), fd3:lem-field-fraction-rules
thm-am-gm (proof): the sum of n copies of a is na | the constant-sum induction written out in exm-odd-sum-reversal (1.1)
thm-am-gm (proof): x^2 > 0 for x != 0 | fd3:prp-ordered-ring-rules (e), cited in the Uses line
exm-am-gm-compound (solution): n(1 + 1/n) + 1 = n + 2, a sum of n equal terms | constant sum as above; fd3:lem-field-fraction-rules
exr-inequalities-for-sums-and-products-b1 (solution): 8abc > 0 and P > 0 as products of positives | (O4) of fd3:def-ordered-ring-and-field
exr-inequalities-for-sums-and-products-b2 (solution): (1 + x)^3 = 1 + 3x + 3x^2 + x^3 | school expansion (fd3:prp-ring-algebra)
-->
