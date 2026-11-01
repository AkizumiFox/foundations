# Estimates for Limits

*Number Systems*, Chapter 4 defined what \( a_n \to a \) means in an ordered field (@fd3:def-sequence-limit-ordered-field) and proved the limit laws. It also gave a method for proving a limit from the definition (@fd3:exm-method-limit-from-definition). The method bounds the distance by \( C/(n + 1) \) for \( n \ge n_0 \), by enlarging numerators and shrinking denominators, and then takes \( N \coloneqq \max\{N', n_0\} \). This section does not teach that method again. It adds two ways to find the bound when the expression is less tame: keep the dominant term of a quotient, and bound a power from below by one term of the binomial theorem. *Analysis on the Real Line* uses all three.

Throughout, sequences are sequences in \( \nR \), a complete ordered field (@fd3:thm-reals-complete-ordered-field), and \( n \) stands for \( n \cdot 1 \), as in *Number Systems*. Where a formula such as \( 1/n \) needs \( n \ge 1 \), the sequence starts at \( n = 1 \). Such a sequence is the shift by one of a sequence indexed from \( 0 \), and a shift changes no limit (@fd3:prp-tail-change-ordered-field (b)).

## The method, recalled

The method of @fd3:exm-method-limit-from-definition has four steps.

::: {.enumerate options="label=(\arabic*)"}
1. Bring the distance \( \abs{a_n - a} \) to one fraction.
2. Bound it, for every \( n \ge n_0 \), by a constant \( C \) over \( n + 1 \).
3. Choose a threshold \( N' \) for that bound, and let \( N \coloneqq \max\{N', n_0\} \).
4. Write the proof forwards: \( \varepsilon \) first, then \( N \), then an arbitrary \( n \ge N \).
:::

In \( \nR \) two remarks simplify the work. First, step (3) always succeeds. \( \nR \) is complete, hence Archimedean (@fd3:thm-cof-complete-archimedean). So @fd3:prp-archimedean-reciprocal applies to it.

Second, a bound \( C/n \) for \( n \ge 1 \) serves as well as \( C/(n + 1) \). Since \( \nR \) is Archimedean, there is an integer \( N' > C/\varepsilon \). Then \( 1/N' < \varepsilon/C \), because reciprocals reverse the order of positive numbers (@fd3:prp-reciprocal-order (b)). So \( C/n \le C/N' < \varepsilon \) for every \( n \ge N' \), because a larger denominator gives a smaller quotient (@fd3:prp-ordered-field-halves (c)).

::: {#exm-first-estimate}
[A first estimate in \( \nR \)]

Show that \( a_n \coloneqq \dfrac{n + 3}{2n^2 - 1} \to 0 \) in \( \nR \).
:::

::: {.solution}
The numbers (1)–(4) are the four steps of the method.

(1) For \( n \ge 1 \), \( 2n^2 - 1 \ge 1 > 0 \) and \( n + 3 > 0 \), so the distance \( \abs{a_n - 0} \) is \( a_n \) itself.

(2) Let \( n \ge 3 \). Then \( n + 3 \le n + n = 2n \). Also \( n^2 \ge 1 \), so \( 2n^2 - 1 = n^2 + (n^2 - 1) \ge n^2 > 0 \). A larger denominator gives a smaller quotient, so \( 1/(2n^2 - 1) \le 1/n^2 \). Multiplying these two inequalities between non-negative numbers,
\[
0 < a_n \le 2n \cdot \frac{1}{n^2} = \frac{2}{n} \qquad (n \ge 3) .
\]
So \( n_0 = 3 \) and \( C = 2 \).

(3) Let \( \varepsilon > 0 \). Choose an integer \( N' > 2/\varepsilon \) and let \( N \coloneqq \max\{3, N'\} \). It depends on \( \varepsilon \) only.

(4) Let \( n \ge N \). Then \( n \ge 3 \), so the bound of (2) applies, and \( 2/n \le 2/N \) since \( n \ge N \):
\[
\abs{a_n - 0} = a_n \le \frac{2}{n} \le \frac{2}{N} < \varepsilon ,
\]
where the last step uses \( N \ge N' > 2/\varepsilon \). Hence \( a_n \to 0 \).

::: {.uses}
@fd3:prp-ordered-field-halves (c) (larger denominator, smaller quotient), (d) (multiplying inequalities).
:::
:::

Both bounds in step (2) needed a range. The bound \( n + 3 \le 2n \) fails at \( n = 2 \). The bound \( 2n^2 - 1 \ge n^2 \) holds from \( n = 1 \) on. Here the ranges were found at sight. When the terms do not simplify so readily, two techniques find them: keeping the dominant term, and bounding a power from below.

## Keeping the dominant term

Take \( \dfrac{2n^2 + 3n}{n^2 - 5} \). For large \( n \) the terms \( 2n^2 \) and \( n^2 \) swamp the others, and the quotient should be close to \( 2 \). To bound a quotient from above we need its numerator from above and its denominator from below. Enlarging a numerator is easy. Shrinking a denominator that contains a subtraction is where care is needed, because \( n^2 - 5 \) is negative for small \( n \).

::: {#exm-method-dominant-term}
[Method: keep the dominant term]

**How it goes.** In a quotient of sums, keep the term that grows fastest and absorb the others into it. From some \( n_0 \) on, a lower-order term is at most a fixed fraction of the dominant term. For example, \( 5 \le \frac12 n^2 \) once \( n \ge 4 \), so \( n^2 - 5 \ge \frac12 n^2 \) there. Then the quotient is bounded by a quotient of single powers. This is step (2) of the method of @fd3:exm-method-limit-from-definition, with \( n_0 \) the largest of the ranges used.

**When to use it.** Rational expressions in \( n \), possibly with \( \sqrt{n} \).

**Common mistakes.** Subtracting in the denominator without stating a range. For instance, \( n^2 - 5 \ge \frac12 n^2 \) is false for \( n \le 3 \).
:::

::: {#exm-dominant-term}
[A limit that is not zero]

Show that \( a_n \coloneqq \dfrac{2n^2 + 3n}{n^2 - 5} \to 2 \).
:::

::: {.solution}
(1) No natural number has square \( 5 \), so every \( a_n \) is defined. For \( n \ge 3 \), \( n^2 \ge 9 > 5 \), and
\[
a_n - 2 = \frac{2n^2 + 3n - 2(n^2 - 5)}{n^2 - 5} = \frac{3n + 10}{n^2 - 5} > 0 ,
\]
so the distance is \( \abs{a_n - 2} = \dfrac{3n + 10}{n^2 - 5} \).

(2) Keep the dominant terms, \( 3n \) on top and \( n^2 \) below. Let \( n \ge 4 \). Then \( 3n \ge 12 \ge 10 \), so \( 3n + 10 \le 6n \). And \( \frac12 n^2 \ge \frac12 \cdot 16 = 8 \ge 5 \), so \( n^2 - 5 \ge \frac12 n^2 > 0 \). Inverting the second, which reverses it, and multiplying by the first,
\[
\abs{a_n - 2} \le 6n \cdot \frac{2}{n^2} = \frac{12}{n} \qquad (n \ge 4) .
\]

(3) Let \( \varepsilon > 0 \). Choose an integer \( N' > 12/\varepsilon \) and let \( N \coloneqq \max\{4, N'\} \).

(4) For \( n \ge N \): \( \abs{a_n - 2} \le 12/n \le 12/N < \varepsilon \). Hence \( a_n \to 2 \).

::: {.uses}
@fd3:prp-ordered-field-halves (c) (larger denominator, smaller quotient), (d) (multiplying inequalities).
:::
:::

The candidate limit \( 2 \) is the ratio of the leading coefficients. Reading off the dominant terms is how the limit is guessed, and the method is how the guess is proved. The range \( n \ge 4 \) came from two requirements, \( 3n \ge 10 \) and \( \frac12 n^2 \ge 5 \), and the larger of their thresholds serves both.

::: {.check}
For which \( n \in \nN \) is \( n^2 - 7n \ge \frac12 n^2 \)?
:::

::: {.solution}
The inequality says \( \frac12 n^2 \ge 7n \), that is, \( n \bigl( \frac12 n - 7 \bigr) \ge 0 \). For \( n = 0 \) it holds with equality. For \( n \ge 1 \) the factor \( n \) is positive, so it holds exactly when \( \frac12 n \ge 7 \), that is, \( n \ge 14 \). So the inequality holds for \( n = 0 \) and for every \( n \ge 14 \), and fails for \( 1 \le n \le 13 \). A proof that uses \( n^2 - 7n \ge \frac12 n^2 \) takes \( n_0 = 14 \).
:::

## Powers

Every bound so far came from dropping or absorbing terms of a sum. A power \( r^n \) has only one term, and there is nothing to drop. Bernoulli's inequality and the binomial theorem turn it into a sum, and a sum can be bounded below by any one of its non-negative terms.

The first case is the geometric sequence. For \( \abs{r} \ge 1 \) the terms \( r^n \) do not shrink, and for \( \abs{r} < 1 \) they should tend to \( 0 \). Take \( r = \frac12 \) first. Then \( (\frac12)^n = 1/2^n \), and Bernoulli's inequality gives \( 2^n = (1 + 1)^n \ge 1 + n > n \). So \( (\frac12)^n < 1/n \) for every \( n \ge 1 \), a bound of the form \( C/n \) with \( C = 1 \). The proposition below does the same for every \( r \) with \( 0 < \abs{r} < 1 \), by writing \( 1/\abs{r} \) as \( 1 + h \).

::: {#prp-power-null}
[Geometric Sequences Tend to Zero]

Let \( r \in \nR \) with \( \abs{r} < 1 \).

::: {.enumerate options="label=(\alph*)"}
1. If \( r \ne 0 \) and \( h \coloneqq \dfrac{1}{\abs{r}} - 1 \), then \( h > 0 \) and \( \abs{r}^n < \dfrac{1}{nh} \) for every integer \( n \ge 1 \).
2. \( r^n \to 0 \).
:::
:::

::: {.idea}
[Scratch work]

The goal, from @fd3:def-sequence-limit-ordered-field, is \( \abs{r^n - 0} = \abs{r}^n < \varepsilon \) for every \( n \) beyond some \( N \). Solving \( \abs{r}^n < \varepsilon \) for \( n \) would need a logarithm, which we do not have yet. So we follow step (2) of the method and look for a simpler bound of the form \( C/n \).

The trouble is that \( \abs{r}^n \) is a small number. The tools we have, Bernoulli's inequality and the binomial theorem, bound powers of numbers **above** \( 1 \) from **below**. So we turn small into large: we write \( \abs{r} \) as the reciprocal of a number above \( 1 \),
\[
\abs{r} = \frac{1}{1 + h} , \qquad h \coloneqq \frac{1}{\abs{r}} - 1 > 0 ,
\]
so that \( \abs{r}^n = 1/(1 + h)^n \). Now \( \abs{r}^n \) is small as soon as \( (1 + h)^n \) is large, and a lower bound \( (1 + h)^n \ge Cn \) is enough. Bernoulli's inequality supplies one at once: \( (1 + h)^n \ge 1 + nh > nh \).

| We know | We want |
|---|---|
| \( 0 < \abs{r} < 1 \) | \( \abs{r}^n \) below every \( \varepsilon > 0 \) for large \( n \) |
| \( h \coloneqq \frac{1}{\abs{r}} - 1 > 0 \), so \( \abs{r}^n = \frac{1}{(1 + h)^n} \) | enough: \( (1 + h)^n \) bounded below by \( Cn \) |
| @fd2:thm-bernoulli: \( (1 + h)^n \ge 1 + nh > nh \) | \( \abs{r}^n < \frac{1}{nh} \): step (2) of the method with \( C = \frac{1}{h} \); the gap is closed |

The proof follows these rows from top to bottom. It then finishes with steps (3) and (4) of the method, using the bound \( 1/(nh) \).
:::

::: {.proof}
(a) Let \( r \ne 0 \). Then \( 0 < \abs{r} < 1 \), since the absolute value of a non-zero number is positive. Reciprocals reverse the order of positive numbers, so \( 1/\abs{r} > 1/1 = 1 \), that is, \( h > 0 \). By the choice of \( h \), \( 1 + h = 1/\abs{r} \), so \( \abs{r} = 1/(1 + h) \) and \( \abs{r}^n = 1/(1 + h)^n \). Since \( h \ge -1 \), Bernoulli's inequality (@fd2:thm-bernoulli) gives
\[
(1 + h)^n \ge 1 + nh > nh .
\]
For \( n \ge 1 \), \( nh > 0 \) as a product of positive numbers. So \( 0 < nh < (1 + h)^n \), and taking reciprocals reverses the inequality: \( \abs{r}^n = 1/(1 + h)^n < 1/(nh) \).

(b) If \( r = 0 \), then \( r^n = r^{n-1} \cdot 0 = 0 \) for every \( n \ge 1 \), so \( \abs{r^n - 0} = 0 < \varepsilon \) for every \( \varepsilon > 0 \) and every \( n \ge 1 \). Let \( r \ne 0 \) and \( \varepsilon > 0 \), and let \( h \) be as in (a). Then \( h\varepsilon > 0 \). Since \( \nR \) is Archimedean, @fd3:prp-archimedean-reciprocal gives \( N \in \nZ_{>0} \) with \( 1/n < h\varepsilon \) for every \( n \ge N \). This \( N \) depends on \( \varepsilon \) and on \( r \), through \( h \). Let \( n \ge N \). Then \( n \ge 1 \), and \( \abs{r^n} = \abs{r}^n \) by induction on \( n \), since \( \abs{xy} = \abs{x} \abs{y} \). By (a),
\[
\abs{r^n - 0} = \abs{r}^n < \frac{1}{nh} < \frac{h\varepsilon}{h} = \varepsilon .
\]
This proves \( r^n \to 0 \).

::: {.uses}
@fd3:prp-absolute-value-ordered-field (a) (\( \abs{r} > 0 \) for \( r \ne 0 \)), (b) (\( \abs{xy} = \abs{x} \abs{y} \)); @fd3:prp-reciprocal-order (b) (reciprocals reverse \( < \)). @fd2:prp-power-laws (\( (1/x)^n = 1/x^n \)); @fd3:def-naturals-in-ordered-field (b) (\( x^n = x^{n-1} x \)); @fd3:prp-ordered-ring-rules (products of positives).
:::
:::

Part (a) is the useful half. It gives an explicit bound, valid for every \( n \ge 1 \), from which a threshold can be read off for any tolerance.

::: {.check}
From @prp-power-null (a), find an \( N \) with \( (0.9)^n < 0.01 \) for every \( n \ge N \).
:::

::: {.solution}
Here \( r = 0.9 = \frac{9}{10} \), so \( h = \frac{10}{9} - 1 = \frac{1}{9} \) and \( (0.9)^n < \dfrac{1}{n/9} = \dfrac{9}{n} \) for \( n \ge 1 \). Now \( \frac{9}{n} \le \frac{1}{100} \) exactly when \( n \ge 900 \). So \( N = 900 \) works: for \( n \ge 900 \), \( (0.9)^n < 9/n \le 0.01 \). The bound is wasteful, since already \( (0.9)^{44} < 0.01 \). That costs nothing: the definition asks for **some** threshold, not the least.
:::

The same three steps handle a power in a denominator under any numerator: write the base as \( 1 + h \), keep one term of the expansion, and invert.

::: {#exm-method-power-lower-bound}
[Method: bound a power from below]

**How it goes.** To make a quotient small when its denominator contains \( r^n \) with \( r > 1 \):

::: {.enumerate options="label=(\arabic*)"}
1. Write \( r = 1 + h \) with \( h > 0 \).
2. Keep one term of the expansion: \( (1 + h)^n \ge nh \) by Bernoulli's inequality, or \( (1 + h)^n \ge \binom{n}{k} h^k \) by @cor-binomial-real (b). Take \( k \) one more than the power of \( n \) on top.
3. Bound \( \binom{n}{k} \) below by \( c\,n^k \) for \( n \ge n_0 \).
4. Invert, and finish with the method of @fd3:exm-method-limit-from-definition.
:::

**When to use it.** Quotients \( n^p / r^n \). Powers \( \abs{r}^n \) with \( \abs{r} < 1 \), through \( 1/\abs{r} = 1 + h \). The \( n \)-th roots of Section 1.5.

**Common mistakes.** One mistake is to choose \( k \) too small: then the bound does not tend to \( 0 \). Another is to use the binomial bound with \( h < 0 \).
:::

In @exm-binomial-bound the base was \( 2 \), and \( k = 2 \) gave \( n/2^n \le 2/(n - 1) \) for \( n \ge 2 \). The same steps work for every base \( r > 1 \). The numerator is \( n \), to the first power, so \( k = 2 \).

::: {#prp-linear-over-power-null}
[Powers Beat n]

Let \( r > 1 \) and \( h \coloneqq r - 1 \). Then \( \dfrac{n}{r^n} \le \dfrac{4}{nh^2} \) for every integer \( n \ge 2 \), and \( \dfrac{n}{r^n} \to 0 \).
:::

::: {.idea}
Follow @exm-method-power-lower-bound step by step. Write \( r = 1 + h \). Keep the term \( k = 2 \), which is of order \( n^2 \). Bound \( n(n - 1) \) below by \( \frac12 n^2 \). Invert, multiply by \( n \), and finish the limit with \( C = 4/h^2 \).
:::

::: {.proof}
Let \( n \ge 2 \). Since \( r > 1 \), \( h > 0 \). By @cor-binomial-real (b) with \( x = h \) and \( k = 2 \le n \), and since \( \binom{n}{2} \cdot 2 = n(n - 1) \),
\[
r^n = (1 + h)^n \ge \binom{n}{2} h^2 = \frac{n(n - 1)}{2} h^2 .
\]
Since \( n \ge 2 \), \( \frac{n}{2} \ge 1 \), so \( n - 1 \ge \frac{n}{2} \ge 0 \). Multiplying the inequalities \( 0 \le \frac{n}{2} \le n - 1 \) and \( 0 \le n \le n \), between non-negative numbers, gives \( n(n - 1) \ge \frac{n^2}{2} \). Hence \( r^n \ge \frac{n^2 h^2}{4} > 0 \). Inverting, which reverses the inequality, and multiplying by \( n > 0 \),
\[
\frac{n}{r^n} \le n \cdot \frac{4}{n^2 h^2} = \frac{4}{nh^2} .
\]
For the limit, \( n/r^n > 0 \), so the distance to \( 0 \) is \( n/r^n \le C/n \) for \( n \ge 2 \), with \( C \coloneqq 4/h^2 \). Let \( \varepsilon > 0 \), choose an integer \( N' > C/\varepsilon \), and let \( N \coloneqq \max\{2, N'\} \). It depends on \( \varepsilon \) and \( r \). For \( n \ge N \), \( \abs{n/r^n - 0} \le C/n \le C/N < \varepsilon \). So \( n/r^n \to 0 \).

::: {.uses}
@prp-binomial-factorial (c) (\( \binom{n}{2} \cdot 2 = n(n - 1) \)); @fd3:prp-ordered-field-halves (c) (larger denominator, smaller quotient), (d) (multiplying inequalities).
:::
:::

With \( k = 1 \), that is, Bernoulli's inequality, the same steps give only \( n/r^n < n/(nh) = 1/h \). That bound does not tend to \( 0 \). The choice of \( k \) is the whole difference.

A comparison with a power can also run the other way: a sequence that is hard to handle directly is bounded by a geometric one, and @prp-power-null finishes.

::: {#exm-geometric-comparison}
[Factorials beat powers of two]

Show that \( \dfrac{1}{n!} \le \dfrac{1}{2^{n-1}} < \dfrac{2}{n} \) for every integer \( n \ge 1 \), and hence that \( \dfrac{1}{n!} \to 0 \).
:::

::: {.solution}
*The first inequality.* We show \( n! \ge 2^{n-1} \) for \( n \ge 1 \), by induction on \( n \). For \( n = 1 \): \( 1! = 1 = 2^0 \). Suppose \( n! \ge 2^{n-1} \). Also \( n + 1 \ge 2 \), and both inequalities are between non-negative numbers, so we may multiply them:
\[
(n + 1)! = n! \, (n + 1) \ge 2^{n-1} \cdot 2 = 2^n .
\]
Inverting reverses the inequality, so \( 1/n! \le 1/2^{n-1} \).

*The second inequality.* By @prp-power-null (a) with \( r = \frac12 \), \( h = 2 - 1 = 1 \), we have \( (\frac12)^n < \frac1n \) for \( n \ge 1 \). Since \( 1/2^{n-1} = (\frac12)^{n-1} = 2 \cdot (\frac12)^n \),
\[
\frac{1}{2^{n-1}} = 2 \Bigl( \frac12 \Bigr)^n < \frac{2}{n} .
\]

*The limit.* So \( 0 < 1/n! < 2/n \) for \( n \ge 1 \): a bound \( C/n \) with \( C = 2 \). Given \( \varepsilon > 0 \), take an integer \( N > 2/\varepsilon \). Then \( N \ge 1 \), and for \( n \ge N \), \( \abs{1/n! - 0} < 2/n \le 2/N < \varepsilon \). Hence \( 1/n! \to 0 \).

::: {.uses}
@fd2:def-sum-product (\( (n + 1)! = n! \, (n + 1) \)); @fd3:prp-ordered-field-halves (d) (multiplying inequalities), (c) (larger denominator, smaller quotient); @fd2:prp-power-laws (\( 1/2^{n-1} = 2 (\frac12)^n \)).
:::
:::

::: {.warning}
\( \frac{1}{n^2} \le \varepsilon \) is not \( \frac{1}{n^2} < \varepsilon \). The definition of a limit asks for the strict inequality. A threshold chosen to make the bound **at most** \( \varepsilon \) can miss it. For \( \varepsilon = 1 \), the choice \( N \coloneqq 1/\varepsilon = 1 \) gives, at \( n = N = 1 \), the distance \( \frac{1}{1^2} = 1 \), which is not \( < 1 \). Ask for \( N > C/\varepsilon \), strictly.
:::

::: {.second-reading title="When the one-term bound fails"}
Change one hypothesis of @cor-binomial-real (b): keep \( k = 2 \) and allow \( h < 0 \). At \( h = -1 \), \( n = 2 \) the claim would read \( (1 - 1)^2 \ge \binom{2}{2}(-1)^2 \), that is, \( 0 \ge 1 \), which is false. What breaks is the step that keeps one term of a sum. That step needs every term non-negative, and with \( h < 0 \) the terms \( \binom{n}{j} h^j \) alternate in sign. Bernoulli's inequality survives for \( -1 \le h < 0 \), because its proof is an induction, not a dropped sum. So for \( 0 < \abs{r} < 1 \) the method first passes to \( 1/\abs{r} = 1 + h \) with \( h > 0 \), as the proof of @prp-power-null did. It never expands \( (1 + (r - 1))^n \) directly.
:::

## Exercises

### A. Check your understanding

::: {#exr-estimates-for-limits-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Write the negation of "\( a_n \to 0 \)" with all its quantifiers.
2. In @exm-first-estimate, on what does \( N \) depend? Could it depend on \( n \)?
3. Name the method used: \( \dfrac{n}{n^3 + 7} \le \dfrac{1}{n^2} \) for \( n \ge 1 \).
4. True or false: if \( \abs{a_n} \le \dfrac{5}{n} \) for every \( n \ge 10 \), then \( a_n \to 0 \).
:::
:::

::: {.solution}
(a) \( \exists \varepsilon > 0 \ \ \forall N \in \nN \ \ \exists n \in \nN \ \ \bigl( n \ge N \wedge \abs{a_n} \ge \varepsilon \bigr) \), as in the negation after @fd3:def-sequence-limit-ordered-field with \( a = 0 \).

(b) On \( \varepsilon \) only. It cannot depend on \( n \): \( N \) is chosen before \( n \) is named, and the claim is about **every** \( n \ge N \).

(c) Step (2) of @fd3:exm-method-limit-from-definition: shrink the denominator by dropping the positive term \( 7 \), so \( n^3 + 7 \ge n^3 > 0 \) and \( n/(n^3 + 7) \le n/n^3 = 1/n^2 \).

(d) True. Given \( \varepsilon > 0 \), take an integer \( N' > 5/\varepsilon \) and \( N \coloneqq \max\{10, N'\} \). For \( n \ge N \), \( \abs{a_n - 0} \le 5/n \le 5/N < \varepsilon \).
:::

### B. Practice

::: {#exr-estimates-for-limits-b1}
[B1: Name the method, then complete it]

Show that \( a_n \coloneqq \dfrac{n + 5}{2^n} \to 0 \). Start: write \( 2 = 1 + 1 \). By @cor-binomial-real (b) with \( k = 2 \), \( 2^n \ge \dfrac{n(n - 1)}{2} \ge \dfrac{n^2}{4} \) for \( n \ge 2 \). *Name the method, then complete it.*
:::

::: {.solution}
*The method:* bound the power from below, as in @exm-method-power-lower-bound. The numerator is handled by keeping its dominant term, as in @exm-method-dominant-term.

Let \( n \ge 5 \). Then \( n + 5 \le 2n \). By the start, \( 2^n \ge n^2/4 > 0 \), so \( 1/2^n \le 4/n^2 \). Multiplying,
\[
0 < a_n \le 2n \cdot \frac{4}{n^2} = \frac{8}{n} .
\]
Let \( \varepsilon > 0 \), take an integer \( N' > 8/\varepsilon \) and \( N \coloneqq \max\{5, N'\} \). For \( n \ge N \), \( \abs{a_n - 0} \le 8/n \le 8/N < \varepsilon \). Hence \( a_n \to 0 \).

::: {.uses}
@fd3:prp-ordered-field-halves (c) (larger denominator, smaller quotient), (d) (multiplying inequalities).
:::
:::

::: {#exr-estimates-for-limits-b2}
[B2: Put the proof in order]

The claim is \( a_n \coloneqq \dfrac{2n + 1}{n + 1} \to 2 \). Put the lines below in an order that proves it, and say which line does not belong.

::: {.enumerate options="label=(\roman*)"}
1. Let \( \varepsilon > 0 \).
2. For \( n \ge N \), \( \abs{a_n - 2} = \dfrac{1}{n + 1} < \dfrac{1}{n} \le \dfrac{1}{N} < \varepsilon \).
3. Choose \( N \in \nN \) with \( N > 1/\varepsilon \) and \( N \ge 1 \).
4. Choose \( N \coloneqq n + 1 \).
5. Hence \( a_n \to 2 \).
6. \( \abs{a_n - 2} = \Bigl\lvert \dfrac{2n + 1 - 2n - 2}{n + 1} \Bigr\rvert = \dfrac{1}{n + 1} \) for every \( n \in \nN \).
:::
:::

::: {.solution}
An admissible order is (i), (iii), (vi), (ii), (v). Line (vi) uses nothing chosen, so it may also come first: (vi), (i), (iii), (ii), (v). Line (ii) must come after (iii), since it uses \( N \). It must also come after (vi), since it uses the formula for the distance. In (ii), \( 1/n \le 1/N \) holds because a larger denominator gives a smaller quotient, and \( 1/N < \varepsilon \) follows from \( N > 1/\varepsilon \).

The line that does not belong is (iv): it makes \( N \) depend on \( n \), but \( N \) must be fixed before \( n \) is named, and \( n \) ranges over all numbers \( \ge N \).

::: {.uses}
@fd3:prp-ordered-field-halves (c) (larger denominator, smaller quotient); @fd3:prp-reciprocal-order (b) (reciprocals reverse \( < \)).
:::
:::

::: {#exr-estimates-for-limits-b3}
[B3: Prove or disprove]

Prove each true statement and refute each false one.

::: {.enumerate options="label=(\alph*)"}
1. \( \dfrac{n^2 + 1}{n^3} \to 0 \).
2. \( \dfrac{n}{n + 1} \to 0 \).
3. \( \dfrac{(-1)^n}{n} \to 0 \).
4. For every \( \varepsilon > 0 \), every integer \( n \ge 1/\varepsilon \) has \( \dfrac{1}{n^2} < \varepsilon \).
5. \( \dfrac{2^n}{n!} \to 0 \).
:::
:::

::: {.solution}
(a) **True.** For \( n \ge 1 \), \( n^2 + 1 \le 2n^2 \), so \( 0 < a_n \le 2n^2/n^3 = 2/n \). Given \( \varepsilon > 0 \), take an integer \( N > 2/\varepsilon \). Then \( N \ge 1 \), and for \( n \ge N \), \( \abs{a_n} \le 2/n \le 2/N < \varepsilon \).

(b) **False.** For \( n \ge 1 \), \( 2n \ge n + 1 \), so \( \frac{n}{n + 1} \ge \frac12 \). Take \( \varepsilon \coloneqq \frac12 \). For every \( N \in \nN \), the index \( n \coloneqq \max\{N, 1\} \ge N \) has \( \abs{a_n - 0} \ge \frac12 = \varepsilon \). This is the negation of A1 (a).

(c) **True.** \( \abs{a_n - 0} = \abs{(-1)^n}/n = 1/n \), since \( \abs{xy} = \abs{x} \abs{y} \) and \( \abs{(-1)^n} = 1 \). Given \( \varepsilon \), an integer \( N > 1/\varepsilon \) works, as in (a).

(d) **False.** Take \( \varepsilon = 1 \) and \( n = 1 \ge 1/\varepsilon \). Then \( 1/n^2 = 1 \), which is not \( < 1 \). The non-strict \( 1/n^2 \le \varepsilon \) does not give the strict \( 1/n^2 < \varepsilon \).

(e) **True.** For \( n \ge 3 \), \( n! = 1 \cdot 2 \cdot \prod_{k=3}^{n} k \), so
\[
\frac{2^n}{n!} = \frac{2}{1} \cdot \frac{2}{2} \cdot \prod_{k=3}^{n} \frac{2}{k} \le 2 \cdot 1 \cdot \frac{2}{n} = \frac{4}{n} .
\]
Every factor \( \frac{2}{k} \) with \( 3 \le k < n \) lies in \( (0, 1] \), so their product lies in \( (0, 1] \). The last factor, \( k = n \), is kept. Given \( \varepsilon > 0 \), take an integer \( N' > 4/\varepsilon \) and \( N \coloneqq \max\{3, N'\} \). For \( n \ge N \), \( \abs{a_n} \le 4/n \le 4/N < \varepsilon \).

::: {.uses}
@fd3:prp-absolute-value-ordered-field (b) (\( \abs{xy} = \abs{x} \abs{y} \)); @fd3:exm-first-sequences-ordered-field (d) (\( \abs{(-1)^n} = 1 \)); @fd3:prp-ordered-field-halves (d) (multiplying inequalities).
:::
:::

### C. Going deeper

::: {#exr-estimates-for-limits-c1}
[C1: Chapter check: a rational limit]

Prove from the definition that \( a_n \coloneqq \dfrac{3n^2 - n}{n^2 + 4} \to 3 \).
:::

::: {.solution}
Let \( \varepsilon > 0 \). The goal is an \( N \) with \( \abs{a_n - 3} < \varepsilon \) for every \( n \ge N \).

*The distance.* For every \( n \),
\[
a_n - 3 = \frac{3n^2 - n - 3(n^2 + 4)}{n^2 + 4} = \frac{-(n + 12)}{n^2 + 4} ,
\]
so \( \abs{a_n - 3} = \dfrac{n + 12}{n^2 + 4} \).

*The bound.* Let \( n \ge 1 \). Then \( n + 12 \le n + 12n = 13n \), and \( n^2 + 4 \ge n^2 > 0 \), so \( 1/(n^2 + 4) \le 1/n^2 \). Multiplying, \( \abs{a_n - 3} \le 13n/n^2 = 13/n \).

*The threshold.* Choose an integer \( N > 13/\varepsilon \). Then \( N \ge 1 \), and \( N \) depends on \( \varepsilon \) only. For \( n \ge N \), \( n \ge 1 \), so
\[
\abs{a_n - 3} \le \frac{13}{n} \le \frac{13}{N} < \varepsilon ,
\]
where the middle step holds because \( n \ge N \) and the last because \( N > 13/\varepsilon \). Hence \( a_n \to 3 \).

**What a complete answer needs.** (10 points)

- 2: fixes \( \varepsilon > 0 \) arbitrary and states the goal.
- 3: computes \( \abs{a_n - 3} \) exactly.
- 3: bounds it by \( C/n \) with the range \( n \ge 1 \) stated.
- 2: chooses \( N \) before \( n \), depending only on \( \varepsilon \), and ends the chain with a strict \( < \varepsilon \).

**Slips that lose the step.** Letting \( N \) depend on \( n \). Bounding in the wrong direction, that is, shrinking a numerator or enlarging a denominator.

::: {.uses}
@fd3:prp-ordered-field-halves (c) (larger denominator, smaller quotient), (d) (multiplying inequalities).
:::
:::

::: {#exr-estimates-for-limits-c2}
[C2: Squares over powers]

Let \( r > 1 \) and \( h \coloneqq r - 1 \). Show that \( \dfrac{n^2}{r^n} \to 0 \). Start: by @cor-binomial-real (b) with \( k = 3 \), \( r^n \ge \dfrac{n(n - 1)(n - 2)}{6} h^3 \) for \( n \ge 3 \). *Name the method, then complete it.*
:::

::: {.solution}
[Hint 1]

Bound \( n - 1 \) and \( n - 2 \) below by multiples of \( n \), for \( n \ge 4 \).
:::

::: {.solution}
[Hint 2]

For \( n \ge 4 \): \( n - 1 \ge \frac{3n}{4} \) and \( n - 2 \ge \frac{n}{2} \), so \( r^n \ge \dfrac{n^3 h^3}{16} \).
:::

::: {.solution}
*The method:* bound the power from below, as in @exm-method-power-lower-bound. The start did steps (1) and (2), with \( k = 3 \), one more than the power of \( n \) on top. What remains is steps (3) and (4).

*Step (3).* Let \( n \ge 4 \). Then \( n - 1 \ge \frac{3n}{4} \), since this rearranges to \( \frac{n}{4} \ge 1 \). Also \( n - 2 \ge \frac{n}{2} \), since this rearranges to \( \frac{n}{2} \ge 2 \). Both sides of both inequalities are non-negative. So we may multiply them, with \( 0 \le n \le n \) as the third factor, and get \( n(n - 1)(n - 2) \ge n \cdot \frac{3n}{4} \cdot \frac{n}{2} = \frac{3n^3}{8} \). Hence
\[
r^n \ge \frac{3n^3}{8 \cdot 6} h^3 = \frac{n^3 h^3}{16} > 0 \qquad (n \ge 4) .
\]

*Step (4).* Inverting, which reverses the inequality, and multiplying by \( n^2 > 0 \), we get \( \dfrac{n^2}{r^n} \le \dfrac{16}{nh^3} \) for \( n \ge 4 \). Let \( \varepsilon > 0 \), take an integer \( N' > \dfrac{16}{h^3 \varepsilon} \) and \( N \coloneqq \max\{4, N'\} \). It depends on \( \varepsilon \) and \( r \). For \( n \ge N \),
\[
\Bigl\lvert \frac{n^2}{r^n} - 0 \Bigr\rvert \le \frac{16}{nh^3} \le \frac{16}{Nh^3} < \varepsilon .
\]
Hence \( n^2/r^n \to 0 \).

**What a complete answer needs.** (6 points)

- 2: the linear lower bounds for \( n - 1 \) and \( n - 2 \), with the range \( n \ge 4 \) justified.
- 2: their product, with non-negativity checked, and the inversion, with positivity stated.
- 2: the choice of \( N \), and the strict chain ending in \( < \varepsilon \).

**Slips that lose the step.** Using \( n - 1 \ge \frac{3n}{4} \) or \( n - 2 \ge \frac{n}{2} \) without the range \( n \ge 4 \). Multiplying inequalities without checking that the factors are non-negative.

::: {.uses}
@fd3:prp-ordered-field-halves (d) (multiplying inequalities, twice), (c) (larger denominator, smaller quotient).
:::
:::

<!-- dependency ledger
prp-power-null (proof): |r|^n = 1/(1 + h)^n from |r| = 1/(1 + h), i.e. (1/x)^n = 1/x^n for x != 0 | @fd2:prp-power-laws ((xy)^n = x^n y^n with y = 1/x, and 1^n = 1), in the Uses line
prp-power-null (proof): |r^n| = |r|^n | induction on n with @fd3:prp-absolute-value-ordered-field (b), stated inline in words; source in the Uses line
prp-power-null (proof): 0^n = 0 for n >= 1 | @fd3:def-naturals-in-ordered-field (b) (x^{n} = x^{n-1} x), inline; source in the Uses line
prp-power-null (proof): a product of positive reals is positive (nh > 0) | ordered-field axioms (@fd3:prp-ordered-ring-rules), in the Uses line
exm-geometric-comparison (solution): n! >= 2^{n-1} for n >= 1; (n+1)! = n!(n+1) | inline induction; factorial recursion from @fd2:def-sum-product, in the Uses line
exm-geometric-comparison (solution): 1/2^{n-1} = (1/2)^{n-1} = 2 (1/2)^n | @fd2:prp-power-laws, in the Uses line
exr-estimates-for-limits-b3 (solution): a product of finitely many factors in (0, 1] lies in (0, 1]; |(-1)^n| = 1 | inline induction with @fd3:prp-ordered-field-halves (d); |(-1)^n| = 1 is in @fd3:exm-first-sequences-ordered-field (d); both in the Uses line, with @fd3:prp-absolute-value-ordered-field (b)
exm-first-estimate (solution): an integer N' > C/eps exists (also used in exm-dominant-term, prp-linear-over-power-null, exm-geometric-comparison and the exercise solutions) | @fd3:def-archimedean-ordered-field via @fd3:thm-cof-complete-archimedean, recalled in "The method, recalled"
exm-dominant-term (solution): no natural number has square 5 | 2^2 = 4 < 5 < 9 = 3^2 and monotonicity of squares on N, inline
-->
