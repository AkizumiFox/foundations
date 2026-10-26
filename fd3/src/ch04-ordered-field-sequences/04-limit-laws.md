# The Algebra and Order of Limits

So far every limit has been found by hand: we computed the distance from \( a_n \) to the candidate limit and bounded it, as in @exm-first-sequences-ordered-field and @exm-limit-from-definition. This section proves the rules that make most such work unnecessary. Sums, multiples, products and quotients of convergent sequences converge to the sum, multiple, product and quotient of the limits; limits respect \( \le \); and a sequence trapped between two sequences with a common limit has that limit too. Everything holds in an arbitrary ordered field \( F \). No result of this section uses the Archimedean property; only the examples in \( \nQ \) do, through @exm-first-sequences-ordered-field (b) or the non-example after @def-bounded-sequence-ordered-field.

Throughout, \( F \) is an ordered field and \( F_{>0} \) its set of positive elements, as in Section 4.3.

## Two tools

The first tool says that a small factor wins against a factor that merely stays bounded.

::: {#prp-null-times-bounded-ordered-field}
[Null Times Bounded Is Null]

Let \( (a_n) \) be a null sequence in \( F \), and let \( (b_n) \) be a sequence with \( \abs{b_n} \le M \) for every \( n \), where \( M \in F_{>0} \). Then \( (a_n b_n) \) is null.
:::

::: {.proof}
Let \( \varepsilon \in F_{>0} \). Then \( \varepsilon/M \in F_{>0} \) (@prp-reciprocal-order (a) and (O4)). Since \( (a_n) \) is null, there is \( N \) with \( \abs{a_n} < \varepsilon/M \) for every \( n \ge N \). For such \( n \), by @prp-absolute-value-ordered-field (b),
\[
\abs{a_n b_n - 0} = \abs{a_n} \abs{b_n} \le \abs{a_n} M < \frac{\varepsilon}{M} \, M = \varepsilon ,
\]
where the first inequality multiplies \( \abs{b_n} \le M \) by \( \abs{a_n} \ge 0 \) (@prp-ordered-field-halves (d)), and the second multiplies \( \abs{a_n} < \varepsilon/M \) by \( M > 0 \).
:::

For instance, \( \bigl( (-1)^n/(n + 1) \bigr) \) is null in \( \nQ \): it is \( 1/(n + 1) \), null by @exm-first-sequences-ordered-field (b), times \( (-1)^n \), bounded by \( 1 \). The bound \( M \) is fixed before \( \varepsilon \) and enters the tolerance \( \varepsilon/M \). That is the pattern of the product law below.

The second tool is the fact behind every division by \( b_n \): if \( b_n \to b \ne 0 \), the terms eventually stay away from \( 0 \), by a margin we can name.

::: {#lem-limit-bounded-away-ordered-field}
[Terms Near a Non-zero Limit]

Let \( b_n \to b \) in \( F \) with \( b \ne 0 \). Then there is \( N_0 \in \nN \) with \( \abs{b_n} > \abs{b}/2 \) for every \( n \ge N_0 \). If \( b > 0 \), then moreover \( b_n > b/2 \) for every \( n \ge N_0 \).
:::

::: {.proof}
Since \( b \ne 0 \), \( \abs{b} > 0 \) (@prp-absolute-value-ordered-field (a)), so \( \varepsilon \coloneqq \abs{b}/2 \in F_{>0} \) (@prp-ordered-field-halves (b)). Choose \( N_0 \) (depending on \( (b_n) \) and \( b \)) with \( \abs{b_n - b} < \abs{b}/2 \) for every \( n \ge N_0 \). For such \( n \), the reverse triangle inequality (@prp-absolute-value-ordered-field (f)), together with \( x \le \abs{x} \) and \( \abs{-x} = \abs{x} \) (parts (c), (b)), gives
\[
\abs{b} - \abs{b_n} \le \bigl\lvert \abs{b} - \abs{b_n} \bigr\rvert \le \abs{b - b_n} = \abs{b_n - b} < \frac{\abs{b}}{2} ,
\]
so \( \abs{b_n} > \abs{b} - \abs{b}/2 = \abs{b}/2 \), adding \( \abs{b_n} - \abs{b}/2 \) to both sides (@prp-ordered-ring-rules (b)). If \( b > 0 \), then \( \abs{b} = b \), and @prp-absolute-value-ordered-field (d) turns \( \abs{b_n - b} < b/2 \) into \( b - b/2 < b_n \), that is, \( b_n > b/2 \).
:::

In particular \( b_n \ne 0 \) for every \( n \ge N_0 \), since \( \abs{b_n} > \abs{b}/2 > 0 \). The lemma needs \( b \ne 0 \). In \( \nQ \), \( b_n \coloneqq (1 + (-1)^n)/(n + 1) \) tends to \( 0 \) (the warning in Section 4.3), yet \( b_n = 0 \) at every odd \( n \), so for \( b = 0 \) no \( N_0 \) has \( \abs{b_n} > \abs{b}/2 = 0 \) for every \( n \ge N_0 \).

## The limit laws

::: {#thm-limit-laws-ordered-field}
[Limit Laws]

Let \( a_n \to a \) and \( b_n \to b \) in \( F \), and let \( c \in F \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( a_n + b_n \to a + b \);
2. \( c a_n \to c a \); in particular \( -a_n \to -a \) and \( a_n - b_n \to a - b \);
3. \( a_n b_n \to a b \);
4. if \( b \ne 0 \) and \( b_n \ne 0 \) for every \( n \), then \( a_n / b_n \to a / b \).
:::
:::

::: {.idea}
Each part keeps the shape of @exm-method-limit-from-definition (estimate the distance, then choose the threshold and write forwards), but the threshold comes from the hypotheses \( a_n \to a \), \( b_n \to b \) instead of from Archimedes, and the estimate bounds the distance by \( \abs{a_n - a} \), \( \abs{b_n - b} \) through split \( \varepsilon \) or bound-then-shrink. Work backwards from each target distance. For (a), \( \abs{(a_n + b_n) - (a + b)} \le \abs{a_n - a} + \abs{b_n - b} \): a sum of two terms, each of which we can make small, so we give each half the tolerance. For (c), write
\[
a_n b_n - ab = a_n (b_n - b) + b (a_n - a) .
\]
The factors \( b_n - b \) and \( a_n - a \) can be made small, but \( a_n \) cannot. It is, however, bounded (@prp-convergent-bounded-ordered-field), so we replace \( \abs{a_n} \) by a bound \( M \) and ask \( \abs{b_n - b} \) to be smaller than \( \varepsilon/(2M) \). For (d), it is enough to treat \( 1/b_n \) and then use (c). *Before reading on: why must \( M \) be fixed before \( \varepsilon \)?*
:::

::: {.proof}
(a) Let \( \varepsilon \in F_{>0} \). Then \( \varepsilon/2 \in F_{>0} \) (@prp-ordered-field-halves (b)). Since \( a_n \to a \), choose \( N_1 \) (depending on \( \varepsilon \)) with \( \abs{a_n - a} < \varepsilon/2 \) for every \( n \ge N_1 \); since \( b_n \to b \), choose \( N_2 \) with \( \abs{b_n - b} < \varepsilon/2 \) for every \( n \ge N_2 \). Let \( N \coloneqq \max\{N_1, N_2\} \). For \( n \ge N \), both estimates hold, and the triangle inequality (@prp-absolute-value-ordered-field (e)) gives
\[
\begin{aligned}
\abs{(a_n + b_n) - (a + b)} &= \abs{(a_n - a) + (b_n - b)} \\
&\le \abs{a_n - a} + \abs{b_n - b} < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon .
\end{aligned}
\]

(b) If \( c = 0 \), then \( c a_n = 0 = c a \) for every \( n \) (@prp-ring-algebra (b)), a constant sequence, which converges to \( 0 \) (@exm-first-sequences-ordered-field (a)). Let \( c \ne 0 \), so \( \abs{c} > 0 \) (@prp-absolute-value-ordered-field (a)), and let \( \varepsilon \in F_{>0} \). Then \( \varepsilon/\abs{c} \in F_{>0} \) (@prp-reciprocal-order (a) and (O4)). Choose \( N \) with \( \abs{a_n - a} < \varepsilon/\abs{c} \) for every \( n \ge N \). For such \( n \), by distributivity and @prp-absolute-value-ordered-field (b),
\[
\abs{c a_n - c a} = \abs{c (a_n - a)} = \abs{c} \abs{a_n - a} < \abs{c} \, \frac{\varepsilon}{\abs{c}} = \varepsilon ,
\]
multiplying by \( \abs{c} > 0 \) (@prp-ordered-ring-rules (c)). With \( c = -1 \), and \( (-1) x = -x \) (@prp-ring-algebra (c)), this gives \( -a_n \to -a \). Then (a), applied to \( (a_n) \) and \( (-b_n) \), gives \( a_n - b_n = a_n + (-b_n) \to a + (-b) = a - b \).

(c) By @prp-convergent-bounded-ordered-field there is \( M \in F_{>0} \) with \( \abs{a_n} \le M \) for every \( n \in \nN \). We fix this \( M \) now; it depends on the sequence \( (a_n) \) only. Now let \( \varepsilon \in F_{>0} \). Since \( M > 0 \) and \( \abs{b} + 1 \ge 1 > 0 \), the tolerances \( \varepsilon/(2M) \) and \( \varepsilon/(2(\abs{b} + 1)) \) are positive. Since \( b_n \to b \), choose \( N_1 \) with \( \abs{b_n - b} < \varepsilon/(2M) \) for every \( n \ge N_1 \). Since \( a_n \to a \), choose \( N_2 \) with \( \abs{a_n - a} < \varepsilon/(2(\abs{b} + 1)) \) for every \( n \ge N_2 \). Both depend only on \( \varepsilon \), \( M \) and \( b \). Let \( N \coloneqq \max\{N_1, N_2\} \), and let \( n \ge N \). Using the identity of the Idea, the triangle inequality and the product rule (@prp-absolute-value-ordered-field (e), (b)),
\[
\begin{aligned}
\abs{a_n b_n - ab} &\le \abs{a_n} \abs{b_n - b} + \abs{b} \abs{a_n - a} \\
&\le M \abs{b_n - b} + (\abs{b} + 1) \abs{a_n - a} \\
&< M \, \frac{\varepsilon}{2M} + (\abs{b} + 1) \, \frac{\varepsilon}{2(\abs{b} + 1)} = \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon .
\end{aligned}
\]
The second line uses @prp-ordered-field-halves (d), all factors being non-negative; the third multiplies the two estimates by the positive elements \( M \) and \( \abs{b} + 1 \). So \( a_n b_n \to ab \).

(d) First we show \( 1/b_n \to 1/b \). By @lem-limit-bounded-away-ordered-field there is \( N_0 \) with \( \abs{b_n} > \abs{b}/2 \) for every \( n \ge N_0 \). For such \( n \), @lem-field-fraction-rules (c) and @prp-absolute-value-ordered-field (b) give
\[
\Bigl\lvert \frac{1}{b_n} - \frac{1}{b} \Bigr\rvert = \Bigl\lvert \frac{b - b_n}{b_n b} \Bigr\rvert = \frac{\abs{b_n - b}}{\abs{b_n} \abs{b}} .
\]
Multiplying \( \abs{b_n} > \abs{b}/2 \) by \( \abs{b} > 0 \) gives \( \abs{b_n}\abs{b} > \abs{b}^2/2 > 0 \), so \( 1/(\abs{b_n}\abs{b}) < 2/\abs{b}^2 \) (@prp-reciprocal-order (b)). Multiplying by \( \abs{b_n - b} \ge 0 \),
\[
\Bigl\lvert \frac{1}{b_n} - \frac{1}{b} \Bigr\rvert \le \frac{2}{\abs{b}^2} \, \abs{b_n - b} \qquad (n \ge N_0) .
\]
Now let \( \varepsilon \in F_{>0} \). Then \( \varepsilon \abs{b}^2/2 \in F_{>0} \); choose \( N_1 \) with \( \abs{b_n - b} < \varepsilon \abs{b}^2/2 \) for every \( n \ge N_1 \), and let \( N \coloneqq \max\{N_0, N_1\} \). For \( n \ge N \), the last display and multiplication of \( \abs{b_n - b} < \varepsilon \abs{b}^2/2 \) by \( 2/\abs{b}^2 > 0 \) gives \( \abs{1/b_n - 1/b} < (2/\abs{b}^2)(\varepsilon \abs{b}^2/2) = \varepsilon \). So \( 1/b_n \to 1/b \). Finally \( a_n/b_n = a_n \cdot (1/b_n) \), and (c) gives \( a_n/b_n \to a \cdot (1/b) = a/b \). This proves the theorem.
:::

The answer to the prompt: the tolerance \( \varepsilon/(2M) \) contains \( M \), so \( M \) must exist before that tolerance is written down. And \( M \) must not depend on \( n \): it has to bound \( \abs{a_n} \) for **every** \( n \ge N \) at once, including indices not yet chosen. That is why it comes from @prp-convergent-bounded-ordered-field, a single bound for the whole sequence, and not from "\( \abs{a_n} \) is some element of \( F \)". The \( + 1 \) in \( \abs{b} + 1 \) is there because \( b \) may be \( 0 \), and \( \varepsilon/(2\abs{b}) \) would then mean nothing.

Part (a) is the move we call **split \( \varepsilon \)**: to make a sum of \( k \) small terms smaller than \( \varepsilon \), give each term the tolerance \( \varepsilon/k \), and combine the finitely many thresholds by a maximum. Part (c) is **bound, then shrink**: replace the factor you cannot control by a bound fixed in advance, then make the other factor small.

::: {.second-reading title="The product law from the two tools"}
Alternatively, (c) follows from the earlier tools without new estimates. By @prp-limit-null-shift-ordered-field, \( (b_n - b) \) and \( (a_n - a) \) are null; \( a_n (b_n - b) \) is null by @prp-null-times-bounded-ordered-field, with the bound \( M \); \( b (a_n - a) \) is null by (b); so their sum \( a_n b_n - ab \) is null by (a), and @prp-limit-null-shift-ordered-field again gives \( a_n b_n \to ab \). The bound \( M \) is still fixed first: it is the hypothesis of @prp-null-times-bounded-ordered-field.
:::

In (d), the hypothesis "\( b_n \ne 0 \) for every \( n \)" is there only so that \( a_n / b_n \) is defined for every \( n \). By @lem-limit-bounded-away-ordered-field, \( b_n \ne 0 \) holds eventually anyway once \( b \ne 0 \). If some early \( b_n \) vanish, the quotient is a sequence from some \( N_0 \) on, and @prp-tail-change-ordered-field (b) applies the law to the shifted sequences \( (a_{n+N_0}) \) and \( (b_{n+N_0}) \).

::: {.warning}
Part (d) needs \( b \ne 0 \), even when every \( b_n \ne 0 \). In \( \nQ \), \( a_n = 1/(n + 1) \) and \( b_n = 1/(n + 1)^2 \) are both null (the first by @exm-first-sequences-ordered-field (b), the second by (c), since \( b_n = a_n a_n \)), with every \( b_n \ne 0 \), and \( a_n / b_n = n + 1 \). Since \( n + 1 > n \), the sequence \( (n + 1) \) is not bounded (the non-example after @def-bounded-sequence-ordered-field), and so has no limit (@prp-convergent-bounded-ordered-field). The "law" \( \lim (a_n/b_n) = 0/0 \) names nothing.
:::

::: {.check}
Find \( \lim (3n^2 - n)/(n^2 + 5) \) in \( \nQ \), citing a law, or another result, for each step.
:::

::: {.solution}
The limit is \( 3 \). Let \( u_0 \coloneqq 0 \) and \( u_n \coloneqq 1/n \) for \( n \ge 1 \). The shifted sequence \( (u_{n+1})_n = (1/(n + 1))_n \) is null (@exm-first-sequences-ordered-field (b); this is where Archimedes enters), so \( (u_n) \) is null by @prp-tail-change-ordered-field (b). By @thm-limit-laws-ordered-field: \( 3 - u_n \to 3 - 0 = 3 \) (the constant \( 3 \) converges to \( 3 \) by @exm-first-sequences-ordered-field (a); then (b) and (a)); \( u_n^2 \to 0 \) ((c)); \( 1 + 5u_n^2 \to 1 \) ((b), (a)). Every \( 1 + 5u_n^2 \ge 1 > 0 \): \( u_n^2 \ge 0 \) (@prp-ordered-ring-rules (e) if \( u_n \ne 0 \), and \( u_0^2 = 0 \)), so \( 5u_n^2 \ge 0 \) (@prp-ordered-field-halves (d)), and \( 1 + 5u_n^2 \ge 1 \) by @prp-ordered-ring-rules (b). Also the limit \( 1 \ne 0 \), so (d) gives
\[
c_n \coloneqq \frac{3 - u_n}{1 + 5u_n^2} \to \frac{3}{1} = 3 .
\]
For \( n \ge 1 \), multiplying numerator and denominator by \( n^2 \) shows \( c_n = (3n^2 - n)/(n^2 + 5) \). The two sequences agree from \( N_0 = 1 \) on (at \( n = 0 \) they differ: \( 3 \) versus \( 0 \)), so @prp-tail-change-ordered-field (a) gives the limit \( 3 \).
:::

## Limits and order

Inequalities between terms pass to the limits, provided we accept that a strict inequality may become an equality.

::: {#prp-limit-preserves-order-ordered-field}
[Limits Preserve Weak Inequalities]

Let \( a_n \to a \) and \( b_n \to b \) in \( F \), and let \( N_0 \in \nN \).

::: {.enumerate options="label=(\alph*)"}
1. If \( a_n \le b_n \) for every \( n \ge N_0 \), then \( a \le b \).
2. In particular, for \( c \in F \): if \( a_n \le c \) for every \( n \ge N_0 \), then \( a \le c \); and if \( a_n \ge c \) for every \( n \ge N_0 \), then \( a \ge c \).
3. *(Squeeze.)* Let \( (c_n) \) be a sequence in \( F \). If \( a = b \) and \( a_n \le c_n \le b_n \) for every \( n \ge N_0 \), then \( c_n \to a \).
:::
:::

::: {.idea}
For (a), suppose instead that \( b < a \). The midpoint \( (a + b)/2 \) separates them, and from some index on \( a_n \) lies above it and \( b_n \) below it, contradicting \( a_n \le b_n \). The tolerance that achieves this is half the gap, \( (a - b)/2 \). For (c), from some index on \( a_n \) and \( b_n \) both lie in the window \( (a - \varepsilon, a + \varepsilon) \), and \( c_n \) is trapped between them.
:::

::: {.proof}
(a) Suppose, for a contradiction, that \( b < a \). Let
\[
\varepsilon \coloneqq \frac{a - b}{2} ,
\]
which lies in \( F_{>0} \) by @prp-ordered-ring-rules (a) and @prp-ordered-field-halves (b). Choose \( N_1 \) (depending on \( \varepsilon \)) with \( \abs{a_n - a} < \varepsilon \) for every \( n \ge N_1 \), and \( N_2 \) with \( \abs{b_n - b} < \varepsilon \) for every \( n \ge N_2 \). Let \( n \coloneqq \max\{N_0, N_1, N_2\} \). By @prp-absolute-value-ordered-field (d), at this \( n \),
\[
a_n > a - \varepsilon = \frac{a + b}{2} = b + \varepsilon > b_n .
\]
This contradicts \( a_n \le b_n \), which holds because \( n \ge N_0 \). So \( b < a \) is false, and \( a \le b \) by trichotomy (O1).

(b) A constant sequence \( c \) converges to \( c \) (@exm-first-sequences-ordered-field (a)). Apply (a) to \( (a_n) \) and the constant sequence \( c \) for the first claim, and to the constant sequence \( c \) and \( (a_n) \) for the second.

(c) Let \( \varepsilon \in F_{>0} \). Choose \( N_1 \) with \( \abs{a_n - a} < \varepsilon \) for \( n \ge N_1 \) and \( N_2 \) with \( \abs{b_n - a} < \varepsilon \) for \( n \ge N_2 \) (recall \( b = a \)), and let \( N \coloneqq \max\{N_0, N_1, N_2\} \). For \( n \ge N \), @prp-absolute-value-ordered-field (d) gives
\[
a - \varepsilon < a_n \le c_n \le b_n < a + \varepsilon ,
\]
so \( \abs{c_n - a} < \varepsilon \) by the same part (d). Hence \( c_n \to a \).
:::

The two midpoint equalities in (a) are field algebra: \( a - (a - b)/2 = (2a - a + b)/2 = (a + b)/2 \), and likewise \( b + (a - b)/2 = (a + b)/2 \). Chapter 5 uses the squeeze (c) repeatedly, mostly with \( F = \nQ \) to show that a sequence is null. In the squeeze (c), the middle sequence is not assumed to converge: its convergence is the conclusion.

::: {.warning}
Strict inequalities do not pass to the limit. In \( \nQ \), \( 1/(n + 1) > 0 \) for every \( n \), and the limit is \( 0 \), not positive (@exm-first-sequences-ordered-field (b)). From \( a_n < b_n \) for every \( n \), (a) gives only \( a \le b \).
:::

::: {.check}
Let \( a_n \to a \) in \( F \) with \( \abs{a_n} \le 3 \) for every \( n \). Show \( \abs{a} \le 3 \).
:::

::: {.solution}
By @prp-absolute-value-ordered-field (d), \( -3 \le a_n \le 3 \) for every \( n \). Part (b) of @prp-limit-preserves-order-ordered-field, used twice, gives \( -3 \le a \le 3 \), and (d) again gives \( \abs{a} \le 3 \).
:::

## Exercises

### A. Check your understanding

::: {#exr-limit-laws-a1}
[A1]

These questions are about the proof of the product law, @thm-limit-laws-ordered-field (c).

::: {.enumerate options="label=(\alph*)"}
1. Why is \( M \) fixed before \( \varepsilon \), and what does it depend on?
2. Which hypothesis supplies \( N_1 \), which supplies \( N_2 \), and which supplies \( M \)?
3. Why does the proof use \( \abs{b} + 1 \) rather than \( \abs{b} \)?
4. State the idea of the proof in two sentences.
5. Run the proof in \( \nQ \) on \( a_n = 1 + 1/(n + 1) \), \( b_n = 2 \) and \( \varepsilon = 1/10 \): give a valid \( M \), the least \( N_1 \), the least \( N_2 \), and \( N \).
:::
:::

::: {.solution}
(a) The tolerance \( \varepsilon/(2M) \) is built from \( M \), so \( M \) must be available first. It depends only on the sequence \( (a_n) \): it bounds \( \abs{a_n} \) for every \( n \), independently of \( \varepsilon \) and of \( n \). A "bound" depending on \( n \) would be useless, since the tolerance for \( \abs{b_n - b} \) must be named before \( n \) is.

(b) \( N_1 \) comes from \( b_n \to b \), applied with the tolerance \( \varepsilon/(2M) \); \( N_2 \) from \( a_n \to a \), with the tolerance \( \varepsilon/(2(\abs{b} + 1)) \); \( M \) also from \( a_n \to a \), through @prp-convergent-bounded-ordered-field.

(c) \( b \) may be \( 0 \), and then \( \varepsilon/(2\abs{b}) \) is undefined. Since \( \abs{b} + 1 \ge 1 > 0 \), the tolerance \( \varepsilon/(2(\abs{b} + 1)) \) always exists, and \( \abs{b} \le \abs{b} + 1 \) keeps the estimate valid.

(d) Write \( a_n b_n - ab = a_n(b_n - b) + b(a_n - a) \), so that each term has a factor tending to \( 0 \). The other factor of the first term is not small, but it is bounded by a constant \( M \) fixed in advance, so making \( \abs{b_n - b} < \varepsilon/(2M) \) and \( \abs{a_n - a} < \varepsilon/(2(\abs{b} + 1)) \) makes each term smaller than \( \varepsilon/2 \).

(e) Here \( a = 1 \) and \( b = 2 \). Since \( 0 < 1/(n + 1) \le 1 \), \( \abs{a_n} \le 2 \) for every \( n \), so \( M = 2 \) is valid. Then \( \varepsilon/(2M) = 1/40 \), and \( \abs{b_n - b} = 0 < 1/40 \) for every \( n \): the least \( N_1 \) is \( 0 \). Next \( \varepsilon/(2(\abs{b} + 1)) = (1/10)/6 = 1/60 \), and \( \abs{a_n - a} = 1/(n + 1) < 1/60 \) if and only if \( n + 1 > 60 \), that is, \( n \ge 60 \): the least \( N_2 \) is \( 60 \). So \( N = \max\{0, 60\} = 60 \). Check at \( n = 60 \): \( a_{60} b_{60} - ab = 2(1 + 1/61) - 2 = 2/61 < 1/10 \).
:::

### B. Practice

::: {#exr-limit-laws-b1}
[B1]

Find the following limits in \( \nQ \) by the limit laws, naming the result used at each step.

::: {.enumerate options="label=(\alph*)"}
1. \( \dfrac{n + 2}{3n + 1} \).
2. \( \dfrac{n^2 + 1}{(n + 1)^2} \).
3. \( \Bigl( \dfrac{1}{n + 1} - 2 \Bigr) \Bigl( 3 + \dfrac{(-1)^n}{n + 1} \Bigr) \).
:::

*Hint: write each term through \( u_n \coloneqq 1/(n + 1) \).*
:::

::: {.solution}
Let \( u_n \coloneqq 1/(n + 1) \), so \( u_n \to 0 \) (@exm-first-sequences-ordered-field (b)), and constant sequences converge to their value (part (a) of that example). All laws cited are parts of @thm-limit-laws-ordered-field.

(a) With \( m \coloneqq n + 1 \ge 1 \): \( (n + 2)/(3n + 1) = (m + 1)/(3m - 2) = (1 + u_n)/(3 - 2u_n) \), dividing numerator and denominator by \( m \). Now \( 1 + u_n \to 1 \) by (a), and \( 3 - 2u_n \to 3 \) by (b) and (a). Since \( 0 < u_n \le 1 \), \( 3 - 2u_n \ge 1 > 0 \) for every \( n \), and the limit \( 3 \ne 0 \), so (d) gives the limit \( 1/3 \).

(b) With \( m = n + 1 \): \( (n^2 + 1)/(n + 1)^2 = ((m - 1)^2 + 1)/m^2 = 1 - 2u_n + 2u_n^2 \). By (c), \( u_n^2 \to 0 \); by (b) and (a), \( 1 - 2u_n + 2u_n^2 \to 1 - 0 + 0 = 1 \). No quotient law is needed.

(c) \( u_n - 2 \to -2 \) by (b) and (a). The sequence \( (-1)^n u_n \) is null by @prp-null-times-bounded-ordered-field, since \( u_n \) is null and \( \abs{(-1)^n} = 1 \) (@exm-first-sequences-ordered-field (d)); so \( 3 + (-1)^n u_n \to 3 \) by (a). By (c), the product tends to \( (-2) \cdot 3 = -6 \).

In each part Archimedes enters once, through \( u_n \to 0 \); every other step is a law valid in any ordered field.
:::

::: {#exr-limit-laws-b2}
[B2: Put the proof in order]

Here are lines of the proof of @prp-limit-preserves-order-ordered-field (a), shuffled, together with two lines that do not belong. Recall the hypotheses: \( a_n \to a \), \( b_n \to b \), and \( a_n \le b_n \) for every \( n \ge N_0 \). Write the seven lines of a correct proof in a correct order, say which other orders are also admissible, and say why each of the other two lines fails.

::: {.enumerate options="label=(\roman*)"}
1. Let \( n \coloneqq \max\{N_0, N_1, N_2\} \).
2. Let \( \varepsilon \coloneqq a - b \), which lies in \( F_{>0} \).
3. Choose \( N_2 \) with \( \abs{b_n - b} < \varepsilon \) for every \( n \ge N_2 \).
4. Suppose, for a contradiction, that \( b < a \).
5. This contradicts \( a_n \le b_n \); so \( b < a \) is false, and \( a \le b \) by trichotomy.
6. Let \( \varepsilon \coloneqq (a - b)/2 \), which lies in \( F_{>0} \) by @prp-ordered-field-halves.
7. Let \( n \coloneqq N_1 \).
8. Then \( a_n > a - \varepsilon = (a + b)/2 = b + \varepsilon > b_n \).
9. Choose \( N_1 \) with \( \abs{a_n - a} < \varepsilon \) for every \( n \ge N_1 \).
:::
:::

::: {.solution}
An admissible order is
\[
\text{(iv)}, \ \text{(vi)}, \ \text{(ix)}, \ \text{(iii)}, \ \text{(i)}, \ \text{(viii)}, \ \text{(v)} .
\]
The only other admissible order exchanges (ix) and (iii), which use only \( \varepsilon \) and one hypothesis each. Nothing else moves: (vi) uses the assumption \( b < a \) of (iv) to make \( \varepsilon \) positive; (ix) and (iii) use \( \varepsilon \); (i) uses \( N_1 \) and \( N_2 \); (viii) uses the two estimates at this \( n \), and needs \( n \ge N_1 \) and \( n \ge N_2 \); (v) uses (viii) and \( n \ge N_0 \), and closes the assumption of (iv).

*Line (ii) is an \( \varepsilon \) of the wrong size.* It is positive, but with it (viii) becomes \( a_n > a - (a - b) = b \) and \( b_n < b + (a - b) = a \), and "\( a_n > b \) and \( b_n < a \)" is no contradiction with \( a_n \le b_n \): for instance \( a_n = b_n = (a + b)/2 \) satisfies all three at once. The two windows of half-width \( a - b \) around \( a \) and \( b \) overlap; half-width \( (a - b)/2 \) makes them touch only at the midpoint, which neither open window contains.

*Line (vii) chooses an index that depends on the wrong thing.* With \( n \coloneqq N_1 \), the estimate for \( a_n \) holds, but nothing makes \( n \ge N_2 \) or \( n \ge N_0 \): the estimate for \( b_n \) and the hypothesis \( a_n \le b_n \) may both fail at this \( n \). The index must lie beyond **all three** thresholds, which the maximum in (i) ensures.
:::

::: {#exr-limit-laws-b3}
[B3: Close to a convergent sequence]

Let \( a_n \to a \) in \( F \), and let \( (b_n) \) be a sequence in \( F \) such that \( (b_n - a_n) \) is null. Prove that \( b_n \to a \). Here is the start of a proof.

> Let \( \varepsilon \in F_{>0} \). Then \( \varepsilon/2 \in F_{>0} \). Since \( a_n \to a \), choose \( N_1 \) with \( \abs{a_n - a} < \varepsilon/2 \) for every \( n \ge N_1 \). Since \( (b_n - a_n) \) is null, choose \( N_2 \) with \( \abs{b_n - a_n} < \varepsilon/2 \) for every \( n \ge N_2 \). Let \( N \coloneqq \max\{N_1, N_2\} \).
>
> ...

*Name the move, then complete it.*
:::

::: {.solution}
The move is **split \( \varepsilon \)**, with two terms: each gets \( \varepsilon/2 \), and the two thresholds are combined by a maximum.

*Completion.* Let \( n \ge N \). Then \( n \ge N_1 \) and \( n \ge N_2 \), and the three-point triangle inequality (@prp-absolute-value-ordered-field (e)) gives
\[
\abs{b_n - a} \le \abs{b_n - a_n} + \abs{a_n - a} < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon .
\]
Since \( \varepsilon \in F_{>0} \) was arbitrary, \( b_n \to a \). (The same result also follows from the laws: \( b_n = (b_n - a_n) + a_n \to 0 + a \) by @thm-limit-laws-ordered-field (a). The exercise is the law's proof, run once more.)
:::

### C. Going deeper

::: {#exr-limit-laws-c1}
[C1: Exit check: the product law]

Prove, from @def-sequence-limit-ordered-field, that if \( a_n \to a \) and \( b_n \to b \) in an ordered field \( F \), then \( a_n b_n \to ab \). You may use that convergent sequences are bounded (@prp-convergent-bounded-ordered-field), the rules for the absolute value (@prp-absolute-value-ordered-field), @prp-limit-null-shift-ordered-field and @prp-null-times-bounded-ordered-field, but not @thm-limit-laws-ordered-field.
:::

::: {.solution}
By @prp-convergent-bounded-ordered-field there is \( M \in F_{>0} \) with \( \abs{a_n} \le M \) for every \( n \in \nN \). It depends only on \( (a_n) \), and we fix it before any tolerance is named.

Let \( \varepsilon \in F_{>0} \). Since \( \abs{b} + 1 \ge 1 > 0 \), both \( \varepsilon/(2M) \) and \( \varepsilon/(2(\abs{b} + 1)) \) lie in \( F_{>0} \). By \( b_n \to b \) there is \( N_1 \) with \( \abs{b_n - b} < \varepsilon/(2M) \) for every \( n \ge N_1 \); by \( a_n \to a \) there is \( N_2 \) with \( \abs{a_n - a} < \varepsilon/(2(\abs{b} + 1)) \) for every \( n \ge N_2 \). These depend only on \( \varepsilon \), \( M \) and \( b \). Let \( N \coloneqq \max\{N_1, N_2\} \).

Let \( n \ge N \). Since
\[
a_n b_n - ab = a_n (b_n - b) + b (a_n - a) ,
\]
the triangle inequality and \( \abs{xy} = \abs{x}\abs{y} \) give
\[
\begin{aligned}
\abs{a_n b_n - ab} &\le \abs{a_n}\abs{b_n - b} + \abs{b}\abs{a_n - a} \\
&\le M \abs{b_n - b} + (\abs{b} + 1)\abs{a_n - a} \\
&< \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon ,
\end{aligned}
\]
where the second line uses \( 0 \le \abs{a_n} \le M \) and \( 0 \le \abs{b} \le \abs{b} + 1 \) (@prp-ordered-field-halves (d)), and the third multiplies the two estimates by \( M > 0 \) and \( \abs{b} + 1 > 0 \). So for every \( \varepsilon \in F_{>0} \) there is \( N \in \nN \) with \( \abs{a_n b_n - ab} < \varepsilon \) for every \( n \ge N \): \( a_n b_n \to ab \).

**Marking scheme.** (10 points)
- 2: fixes a bound \( M \in F_{>0} \) for \( (\abs{a_n}) \), justified (convergent sequences are bounded), before \( \varepsilon \).
- 2: writes \( a_n b_n - ab \) as a sum of two terms, each with a factor tending to \( 0 \).
- 3: chooses \( N_1 \), \( N_2 \) depending only on \( \varepsilon \), \( M \) and \( b \), with the case \( b = 0 \) handled, and \( N \) as their maximum.
- 2: carries out the estimate with the triangle inequality and the product rule for \( \abs{\cdot} \).
- 1: concludes with the quantifiers in the order \( \forall \varepsilon \, \exists N \, \forall n \ge N \).
Fatal errors (0 for the step): a threshold or tolerance that depends on \( n \); the bound "\( \abs{a_n} \le \abs{a} + 1 \) for every \( n \)" without the finite part for \( n < N \); dividing by \( \abs{b} \) without \( b \ne 0 \). A route through @prp-null-times-bounded-ordered-field earns the same points, provided the sum of two null sequences is proved from the definition. Citing @thm-limit-laws-ordered-field for the sum or for \( b(a_n - a) \) gets 0 for that step. A three-term route (\( a_n b_n - ab = (a_n - a)(b_n - b) + a(b_n - b) + b(a_n - a) \), with a tolerance such as \( \delta = \min\{1, \varepsilon/(1 + \abs{a} + \abs{b})\} \) chosen from \( \varepsilon \), \( a \) and \( b \) only) earns the same points: decomposition 2; the choice of \( \delta \), independent of \( n \) and with \( \delta \le 1 \) controlling the product term (in place of the bound \( M \)), 2; a threshold \( N \) for both sequences at tolerance \( \delta \) (the case \( a = 0 \) or \( b = 0 \) covered by the \( 1 \) in the denominator) 3; the estimate 2; conclusion 1.
:::

::: {#exr-limit-laws-c2}
[C2: Non-negative terms and reciprocals]

Let \( a_n \to a \) in \( F \), with \( a_n \ge 0 \) for every \( n \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( a \ge 0 \).
2. Suppose moreover \( a > 0 \). Prove that there is \( N_0 \in \nN \) with \( a_n > 0 \) for every \( n \ge N_0 \), and that the sequence \( (1/a_{n+N_0})_{n \in \nN} \) converges to \( 1/a \).
3. Give an example in \( \nQ \) where \( a_n > 0 \) for every \( n \) and \( (1/a_n) \) does not converge.
:::
:::

::: {.solution}
[Hint 1]

For (a), compare with a constant sequence. For (b), which result keeps terms away from a non-zero limit?
:::

::: {.solution}
[Hint 2]

For (b), start: "By @lem-limit-bounded-away-ordered-field, since \( a > 0 \), there is \( N_0 \) with \( a_n > a/2 \) for every \( n \ge N_0 \)."
:::

::: {.solution}
(a) Since \( a_n \ge 0 \) for every \( n \ge 0 \), @prp-limit-preserves-order-ordered-field (b) with \( c = 0 \) gives \( a \ge 0 \).

(b) Since \( a > 0 \), @lem-limit-bounded-away-ordered-field gives \( N_0 \) with \( a_n > a/2 > 0 \) for every \( n \ge N_0 \). The shifted sequence \( (a_{n+N_0})_n \) converges to \( a \) by @prp-tail-change-ordered-field (b), and each of its terms is non-zero. By @thm-limit-laws-ordered-field (d), applied to the constant sequence \( 1 \) and to \( (a_{n+N_0})_n \), whose limit \( a \) is non-zero, \( 1/a_{n+N_0} \to 1/a \).

(c) \( a_n = 1/(n + 1) \): every term is positive, and \( 1/a_n = n + 1 \) is not bounded in \( \nQ \): for any \( M \in \nQ_{>0} \), the non-example after @def-bounded-sequence-ordered-field gives \( n \) with \( M < n < n + 1 = \abs{1/a_n} \). So it does not converge (@prp-convergent-bounded-ordered-field). The hypothesis \( a > 0 \) of (b) fails here: \( a = 0 \).

**Marking scheme.** (10 points)
- 3: (a), by comparison with the constant sequence \( 0 \) (or by contradiction with \( \varepsilon = -a/2 \)).
- 3: (b), an index \( N_0 \) beyond which \( a_n \) is bounded away from \( 0 \), from \( a > 0 \).
- 2: (b), \( 1/a_{n+N_0} \to 1/a \), either by the quotient law (@thm-limit-laws-ordered-field (d)) applied to the shift, with its convergence to \( a \) and \( a \ne 0 \) checked, or directly from \( \abs{1/a_{n+N_0} - 1/a} \le (2/a^2)\abs{a_{n+N_0} - a} \), which uses \( a_{n+N_0} > a/2 \).
- 2: (c), an example with the failure of convergence justified.
Fatal errors (0 for the step): concluding \( a > 0 \) in (a) from \( a_n > 0 \); applying the quotient law without checking that the limit is non-zero.
:::

<!-- dependency ledger
prp-null-times-bounded-ordered-field (proof): eps/M > 0 and (eps/M) M = eps | prp-reciprocal-order (a), (O4); (F5), (F8) of def-commutative-ring-and-field
prp-null-times-bounded-ordered-field (example): (-1)^n bounded by 1 | exm-first-sequences-ordered-field (d), whose solution shows |(-1)^n| = 1
lem-limit-bounded-away-ordered-field (proof): |b| - |b|/2 = |b|/2 | prp-ordered-field-halves (b)
lem-limit-bounded-away-ordered-field (example): (1 + (-1)^n)/(n + 1) is null in Q and 0 at odd n | the warning after exm-first-sequences-ordered-field in §03 (0 <= b_n <= 2/(n+1)), with exm-first-sequences-ordered-field (b) (Archimedes)
thm-limit-laws-ordered-field (proof): (also the Idea) a_n b_n - ab = a_n (b_n - b) + b (a_n - a) | ring algebra, def-commutative-ring-and-field (F1)-(F9), prp-ring-algebra (c); verify/ch04/thm-limit-laws-ordered-field.py
thm-limit-laws-ordered-field (proof): c a_n - c a = c (a_n - a) and (-1) x = -x | (F9), prp-ring-algebra (c)
thm-limit-laws-ordered-field (proof): |c| (eps/|c|) = eps | (F5), (F8) of def-commutative-ring-and-field; lem-field-fraction-rules
thm-limit-laws-ordered-field (proof): M (eps/(2M)) = eps/2, (|b| + 1) (eps/(2(|b| + 1))) = eps/2 | lem-field-fraction-rules (a), (b); verify/ch04/thm-limit-laws-ordered-field.py
thm-limit-laws-ordered-field (proof): |b| >= 0 gives |b| + 1 >= 1 > 0 | prp-absolute-value-ordered-field (a), prp-ordered-ring-rules (b), (e)
thm-limit-laws-ordered-field (proof): 1/(|b|^2/2) = 2/|b|^2 and (2/|b|^2)(eps |b|^2/2) = eps; |b|^2 > 0 | lem-field-fraction-rules (a), (b); prp-ordered-ring-rules (e); verify/ch04/thm-limit-laws-ordered-field.py
thm-limit-laws-ordered-field (proof): a_n/b_n = a_n (1/b_n) and a (1/b) = a/b | def-commutative-ring-and-field (a/b := a b^{-1}), (F7)
thm-limit-laws-ordered-field (proof): multiplying the inequality 1/(|b_n||b|) < 2/|b|^2 by |b_n - b| >= 0 gives <= | prp-ordered-ring-rules (c), with equality when b_n = b
thm-limit-laws-ordered-field (claim): (the Quick check's solution) (3n^2 - n)/(n^2 + 5) = (3 - 1/n)/(1 + 5/n^2) for n >= 1; values at n = 0 | field algebra; verify/ch04/thm-limit-laws-ordered-field.py
thm-limit-laws-ordered-field (claim): (the warning after it) (1/(n+1))/(1/(n+1)^2) = n + 1 | lem-field-fraction-rules (a), (b); verify/ch04/thm-limit-laws-ordered-field.py
prp-limit-preserves-order-ordered-field (proof): a - (a - b)/2 = (a + b)/2 = b + (a - b)/2 | field algebra, displayed after the proof; verify/ch04/prp-limit-preserves-order-ordered-field.py
prp-limit-preserves-order-ordered-field (proof): not(b < a) gives a <= b | (O1) of def-ordered-ring-and-field, as cited
thm-limit-laws-ordered-field (proof): max of two or three thresholds in N | thm-omega-order (a), one comparison at a time; the same in prp-limit-preserves-order-ordered-field (proof)
prp-limit-preserves-order-ordered-field (solution): the Quick check |a| <= 3 | prp-absolute-value-ordered-field (d), prp-limit-preserves-order-ordered-field (b); inline
exr-limit-laws-a1 (solution): M = 2, least N1 = 0, least N2 = 60, N = 60, and 2/61 < 1/10 | verify/ch04/exr-limit-laws-a1.py
exr-limit-laws-b1 (solution): the three rewritings through u_n = 1/(n + 1) and the limits 1/3, 1, -6 | verify/ch04/exr-limit-laws-b1.py
exr-limit-laws-b1 (solution): 0 < u_n <= 1 | prp-reciprocal-order (b) with 1 <= n + 1 (prp-naturals-in-ordered-field (b))
exr-limit-laws-b2 (solution): a_n = b_n = (a + b)/2 defeats distractor (ii) | verify/ch04/exr-limit-laws-b2.py
exr-limit-laws-c2 (solution): n + 1 is unbounded in Q, using n < n + 1 | Archimedes, the non-example after def-bounded-sequence-ordered-field (§03); prp-ordered-ring-rules (h)
exr-limit-laws-c1 (solution): (marking scheme, three-term route) a_n b_n - ab = (a_n - a)(b_n - b) + a(b_n - b) + b(a_n - a), and delta^2 + |a| delta + |b| delta <= delta(1 + |a| + |b|) <= eps for delta <= 1 | ring algebra, (F1)-(F9); prp-ordered-field-halves (d)
-->
