# The Exponential, the Logarithm, and Real Powers

Chapter 1 gave every non-negative real number its \( n \)-th roots (@lem-reals-nth-root) and every positive real number its rational powers (@def-rational-power), so a power with a rational exponent such as \( 2^{3/2} = (\sqrt 2)^3 \) already has a meaning. A power such as \( 2^{\sqrt 2} \) does not, and no root will give it one. This section borrows three facts about a single function, the exponential, and derives everything else from them: the logarithm, real powers and their laws, and how fast the exponential grows. Its main theorem shows that two of the three facts already determine the function completely.

## Powers that roots cannot reach

A power \( a^{m/n} \) with \( a > 0 \) is the \( n \)-th root of \( a^m \). The exponent \( \sqrt 2 \) is not of the form \( m/n \): if \( \sqrt 2 = m/n \) with \( m, n \in \nZ \), then \( m/n \) would be a rational number whose square is \( 2 \), which @fd3:thm-no-rational-square-two rules out in \( \nQ \), and the rationals sit inside \( \nR \) with the same arithmetic (@fd3:thm-rationals-embed-ordered-field). So \( 2^{\sqrt 2} \) is not a root of anything we know.

The naive answer, "the limit of \( 2^q \) as rational \( q \) approach \( \sqrt 2 \)", needs limits of functions, which this volume does not have. Our route goes through one function, the exponential, and one rule, \( a^x \coloneqq \exp(x \log a) \). Constructing the exponential needs power series, so we borrow it: three facts, and everything else is proved.

## What this volume borrows about the exponential

The exponential should turn sums into products, and near \( 0 \) it should look like \( 1 + x \). *Analysis on the Real Line*, Chapter 10 constructs it as a power series and proves the facts below. Its \( \nR \) is a complete ordered field, so by @fd3:thm-cof-uniqueness it is our \( \nR \), up to the one order-preserving field isomorphism, and the function carries over along it.

::: {#ax-exponential}
[What This Volume Borrows about the Exponential]

There is a function \( \exp \colon \nR \to \nR \) with the following properties. They are **assumed here and proved in *Analysis on the Real Line*, Chapter 10**.

::: {.enumerate options="label=(E\arabic*)"}
1. \( \exp(x + y) = \exp x \cdot \exp y \) **for all** \( x, y \in \nR \).
2. \( \exp x \ge 1 + x \) **for every** \( x \in \nR \).
3. **For every** \( y \in \nR \) with \( y > 0 \) **there is** \( x \in \nR \) with \( \exp x = y \).
:::
:::

In words: (E1) turns addition of arguments into multiplication of values; (E2) puts the graph of \( \exp \) on or above the line \( y = 1 + x \); (E3) says that every positive real number is a value.

This box is where the chapter borrows, as Chapter 3's box (@ax-cosine-sine) borrowed cosine and sine. Nothing in Sections 8.1–8.4, and nothing in this section above the box, uses it. From here on we use these three facts about \( \exp \) and **no others**, and each proof that uses one names it. The first two carry most of the weight; (E3) is what makes the logarithm defined on all of \( (0, \infty) \).

Neither of the first two facts follows from the other. The constant function \( 1 \) satisfies (E1), since \( 1 = 1 \cdot 1 \), but not (E2): at \( x = 1 \) it would need \( 1 \ge 2 \). The function \( x \mapsto 1 + x \) satisfies (E2) with equality, but not (E1): at \( x = y = 1 \) it gives \( 3 \), while \( (1 + 1)(1 + 1) = 4 \).

::: {.warning}
The box says nothing about continuity or derivatives. That \( \exp \) is continuous, and equal to its own derivative, is true; but it is not in the box, and no proof in this volume may quote it. Nor is \( e^x \) a notation yet: until real powers are defined and shown to agree with \( \exp \), we write \( \exp x \), never \( e^x \).
:::

## First consequences

Negative integer exponents appear as soon as we divide. For a real \( u \ne 0 \) and \( n \in \nZ_{>0} \) we write \( u^{-n} \coloneqq 1/u^n \), alongside the powers \( u^n \), \( n \in \nN \), of @fd2:def-power; then \( u^{-n} = (1/u)^n \) by @fd2:prp-power-laws (c) with \( v = 1/u \), since \( u^n (1/u)^n = (u \cdot 1/u)^n = 1 \). We also write \( \exp(t)^n \) for \( (\exp t)^n \).

The first proposition collects what (E1) and (E2) say at once.

::: {#prp-exp-first-consequences}
[First Consequences of the Box]

::: {.enumerate options="label=(\alph*)"}
1. \( \exp 0 = 1 \).
2. \( \exp x > 0 \) and \( \exp(-x) = 1/\exp x \) for every \( x \in \nR \).
3. \( \exp \) is strictly increasing on \( \nR \).
4. \( \exp x \le 1/(1 - x) \) for every \( x \in \nR \) with \( x < 1 \).
5. \( \exp(nx) = (\exp x)^n \) for every \( x \in \nR \) and every \( n \in \nZ \).
:::
:::

::: {.idea}
Part (a) is (E1) at \( x = y = 0 \), with (E2) to rule out \( \exp 0 = 0 \). Part (b) writes \( \exp x \) as a square, \( \exp(x/2)^2 \). Part (c) is the move of @exm-method-factor-difference in multiplicative form: (E1) factors the difference \( \exp y - \exp x \) as \( \exp x \cdot (\exp(y - x) - 1) \), and (E2) signs the bracket. Part (d) is (E2) at \( -x \), turned upside down.
:::

::: {.proof}
(a) By (E1), \( \exp 0 = \exp(0 + 0) = (\exp 0)^2 \), so \( \exp 0 \cdot (\exp 0 - 1) = 0 \). By (E2), \( \exp 0 \ge 1 + 0 = 1 \), so \( \exp 0 \ne 0 \), and @fd3:lem-field-fraction-rules (d) gives \( \exp 0 - 1 = 0 \).

(b) By (E1) and (a), \( \exp x \cdot \exp(-x) = \exp 0 = 1 \). Hence \( \exp x \ne 0 \), and \( \exp(-x) = 1/\exp x \) by the uniqueness of inverses (@fd3:lem-field-fraction-rules (a)). By (E1), \( \exp x = \exp(x/2 + x/2) = (\exp(x/2))^2 \), which is \( \ge 0 \) by @fd3:prp-ordered-ring-rules (e). A non-zero element that is \( \ge 0 \) is \( > 0 \).

(c) Let \( x < y \). By (E1), \( \exp y = \exp x \cdot \exp(y - x) \), so
\[
\exp y - \exp x = \exp x \cdot \bigl( \exp(y - x) - 1 \bigr) \ge \exp x \cdot (y - x) > 0 ,
\]
where the first inequality is (E2) at \( y - x \), multiplied by \( \exp x > 0 \) from (b) (@fd3:prp-ordered-ring-rules (c), or equality), and the last step is (O4): \( \exp x > 0 \) and \( y - x > 0 \).

(d) Let \( x < 1 \). By (E2) at \( -x \), \( \exp(-x) \ge 1 - x > 0 \). Both numbers are positive, so @fd3:prp-ordered-field-halves (c) gives \( 1/\exp(-x) \le 1/(1 - x) \), and \( 1/\exp(-x) = \exp x \) by (b) applied to \( -x \).

(e) For \( n \in \nN \) we induct (@fd1:ax-induction). For \( n = 0 \), \( \exp(0 \cdot x) = \exp 0 = 1 = (\exp x)^0 \) by (a). If \( \exp(nx) = (\exp x)^n \), then by (E1)
\[
\exp((n + 1)x) = \exp(nx + x) = \exp(nx) \exp x = (\exp x)^n \exp x = (\exp x)^{n+1} .
\]
For \( n \in \nZ_{>0} \), (b) and the case just proved give \( \exp(-nx) = 1/\exp(nx) = 1/(\exp x)^n = (\exp x)^{-n} \).
:::

(E3) appears nowhere in this proof, so every part of @prp-exp-first-consequences holds for **any** function satisfying (E1) and (E2). The main theorem below depends on that.

::: {.check}
Which facts of the box does each of the following use: \( \exp 0 = 1 \); \( \exp \) is strictly increasing; the inverse of \( \exp \) is defined at every point of \( (0, \infty) \)?
:::

::: {.solution}
\( \exp 0 = 1 \) uses (E1) and (E2), by the proof of (a). Strict increase uses (E1) and (E2), through (b) and (c). The inverse being defined on all of \( (0, \infty) \) needs every positive number to be a value, which is (E3); that the inverse is a function at all is (c), so (E1) and (E2) enter too.
:::

## Squeeze, then close the gap by Archimedes

The main theorem computes \( \exp x \) as a supremum. To show \( L = \sup S \), @fd2:def-order-supremum asks that \( L \) be an upper bound and that no smaller number be one. The second half often comes from members of \( S \) approaching \( L \) at a known rate.

::: {#exm-method-archimedes-squeeze}
[Method: squeeze, then close the gap by Archimedes]

**Template.** To prove \( \sup S = L \) for a set \( S \subseteq \nR \):

1. show that every \( s \in S \) satisfies \( s \le L \);
2. find a constant \( C > 0 \), **fixed before \( n \) is chosen**, and an \( N_0 \in \nZ_{>0} \) such that for every integer \( n \ge N_0 \) some \( s_n \in S \) satisfies \( s_n \ge L - C/n \);
3. given \( L' < L \), put \( \varepsilon \coloneqq (L - L')/C > 0 \); by @fd3:prp-archimedean-reciprocal there is \( N \) with \( 1/n < \varepsilon \) for all \( n \ge N \); for \( n \ge \max\{N, N_0\} \) we get \( s_n \ge L - C/n > L - C\varepsilon = L' \).

So no \( L' < L \) is an upper bound, and \( L \) is the least upper bound.

**When to use it.** A supremum has been guessed, and the members of \( S \) come with an index \( n \) and an error estimate of the form \( C/n \).

**The usual failures.** A "constant" \( C \) that depends on \( n \) (with \( C = n \) the estimate \( s_n \ge L - 1 \) says nothing about small gaps); and \( C = 0 \), which leaves \( \varepsilon \) undefined. If the estimate seems to come with \( C = 0 \), enlarge \( C \): a lower bound \( L - C/n \) stays true when \( C \) grows.

| Givens | Goal |
|---|---|
| every \( s \in S \) has \( s \le L \); for \( n \ge N_0 \) some \( s_n \in S \) has \( s_n \ge L - C/n \), with \( C > 0 \) fixed in advance | no \( L' < L \) is an upper bound of \( S \) |
| \( L' < L \); \( \varepsilon \coloneqq (L - L')/C > 0 \); \( 1/n < \varepsilon \) for \( n \ge N \) | some \( s \in S \) with \( s > L' \): take \( s_n \), \( n \ge \max\{N, N_0\} \) |
:::

The real numbers are Archimedean (@fd3:thm-reals-complete-ordered-field with @fd3:thm-cof-complete-archimedean), so step 3 is available in \( \nR \).

## Two facts determine the exponential

For a fixed \( x \), the numbers \( (1 + x/n)^n \) are built from \( x \) by arithmetic alone. The theorem says that they squeeze \( \exp x \) from below, and that their supremum is \( \exp x \).

::: {#thm-exp-unique}
[The Exponential Is Determined by (E1) and (E2)]

Let \( x \in \nR \), and let
\[
S_x \coloneqq \Bigl\{ \Bigl(1 + \frac{x}{n}\Bigr)^{n} : n \in \nZ_{>0},\ n > \abs{x} \Bigr\} .
\]
Then \( S_x \) is non-empty and bounded above, and \( \exp x = \sup S_x \). Consequently, if \( E \colon \nR \to \nR \) is any function satisfying (E1) and (E2) with \( E \) in place of \( \exp \), then \( E = \exp \).
:::

::: {.idea}
[Scratch work]

We want two bounds on \( (1 + x/n)^n \): above by \( \exp x \), and below by \( \exp x \) minus something of size \( C/n \).

*Upper.* (E2) at \( x/n \) gives \( \exp(x/n) \ge 1 + x/n \). Raising both sides to the \( n \)-th power gives \( \exp(x/n)^n \ge (1 + x/n)^n \), and \( \exp(x/n)^n = \exp x \) by @prp-exp-first-consequences (e). But raising an inequality to a power is legal only between non-negative numbers (@lem-reals-nth-root (a)): at \( x = -3 \), \( n = 2 \), the base \( 1 + x/n = -1/2 \) is negative. So we ask for \( n > \abs{x} \), which makes \( 1 + x/n > 0 \).

*Lower.* (d) of the same proposition at \( x/n \) gives \( \exp(x/n) \le 1/(1 - x/n) \), legal when \( x/n < 1 \), so \( \exp x \le (1 - x/n)^{-n} \). To compare this with \( (1 + x/n)^n \), multiply and divide by \( (1 - x/n)^n \):
\[
\Bigl(1 + \frac{x}{n}\Bigr)^{n} = \Bigl(1 - \frac{x^2}{n^2}\Bigr)^{n} \Bigl(1 - \frac{x}{n}\Bigr)^{-n} .
\]
The middle factor is close to \( 1 \): Bernoulli's inequality gives \( (1 - x^2/n^2)^n \ge 1 - x^2/n \). That is the \( C/n \) we need.

| Givens | Goal |
|---|---|
| (E1), (E2); @prp-exp-first-consequences; \( n > \abs{x} \) | \( (1 + x/n)^n \le \exp x \) and \( (1 + x/n)^n \ge \exp x - C/n \), \( C > 0 \) not depending on \( n \) |
| \( 1 \pm x/n > 0 \); \( \exp x \le (1 - x/n)^{-n} \) | \( (1 - x^2/n^2)^n \ge 1 - (\text{const})/n \): Bernoulli |

Then @exm-method-archimedes-squeeze finishes, with \( C \coloneqq (x^2 + 1)\exp x \); the \( +1 \) keeps \( C > 0 \) at \( x = 0 \).

*Before reading on: why must \( n \) exceed \( \abs{x} \)? Find every place it is used.*
:::

::: {.proof}
Fix \( x \in \nR \). By the Archimedean property there is \( N_0 \in \nZ_{>0} \) with \( N_0 > \abs{x} \), so \( S_x \ne \varnothing \). Let \( n \in \nZ_{>0} \) with \( n > \abs{x} \). Then \( \abs{x/n} < 1 \), so \( 1 + x/n > 0 \) and \( 1 - x/n > 0 \) (@fd3:prp-absolute-value-ordered-field (d)).

*Upper bound.* By (E2) at \( x/n \), \( 0 < 1 + x/n \le \exp(x/n) \). By @lem-reals-nth-root (a) (or equality), \( (1 + x/n)^n \le \exp(x/n)^n \), and \( \exp(x/n)^n = \exp(n \cdot x/n) = \exp x \) by @prp-exp-first-consequences (e). So \( \exp x \) is an upper bound of \( S_x \), and \( \sup S_x \) exists.

*Lower estimate.* Since \( x/n < 1 \), @prp-exp-first-consequences (d) gives \( \exp(x/n) \le 1/(1 - x/n) \); both sides are positive, so by @lem-reals-nth-root (a) and part (e),
\[
\exp x = \exp(x/n)^n \le \Bigl(1 - \frac{x}{n}\Bigr)^{-n} .
\]
By @fd2:prp-power-laws (c), \( (1 + x/n)^n = (1 - x^2/n^2)^n (1 - x/n)^{-n} \), and \( (1 - x^2/n^2)^n > 0 \) since \( 1 - x^2/n^2 = (1 + x/n)(1 - x/n) > 0 \). Multiplying the display by it, and then applying Bernoulli's inequality (@fd2:thm-bernoulli) to \( -x^2/n^2 \ge -1 \) with \( \exp x > 0 \),
\[
\begin{aligned}
\Bigl(1 + \frac{x}{n}\Bigr)^{n} &\ge \Bigl(1 - \frac{x^2}{n^2}\Bigr)^{n} \exp x \ge \Bigl(1 - \frac{x^2}{n}\Bigr) \exp x \\
&\ge \exp x - \frac{(x^2 + 1) \exp x}{n} .
\end{aligned}
\]

*Conclusion.* Put \( C \coloneqq (x^2 + 1)\exp x \). It depends on \( x \) only, and \( C > 0 \) by @prp-exp-first-consequences (b). For every integer \( n \ge N_0 \) the member \( s_n \coloneqq (1 + x/n)^n \) of \( S_x \) satisfies \( s_n \ge \exp x - C/n \). By @exm-method-archimedes-squeeze, \( \sup S_x = \exp x \).

*Uniqueness.* Let \( E \) satisfy (E1) and (E2). The proof of @prp-exp-first-consequences used only (E1), (E2) and field and order rules, so its conclusions hold for \( E \); and the argument above used only those conclusions, (E2), and facts about \( \nR \). So \( E(x) = \sup S_x = \exp x \) for every \( x \in \nR \). By @fd2:prp-function-equality, \( E = \exp \).
:::

The set \( S_x \) never mentions \( \exp \), so the theorem is a formula: \( \exp x \) is pinned between computable numbers, as the next definition shows at \( x = 1 \). And the box borrows a function that is already determined.

## The number e

::: {#def-euler-number}
[Euler's Number]

\( e \coloneqq \exp 1 \).
:::

By the proof of @thm-exp-unique at \( x = 1 \), for every integer \( n \ge 2 \),
\[
\Bigl(1 + \frac1n\Bigr)^{n} \le e \le \Bigl(1 - \frac1n\Bigr)^{-n} .
\]
At \( n = 2 \) this reads \( 9/4 \le e \le 4 \), so \( e > 2 \). Exercise B1 below squeezes harder.

Now we can say what fails without (E2), beyond the two functions after the box. The function \( F(x) \coloneqq \exp(2x) \) satisfies (E1), since \( F(x + y) = \exp(2x)\exp(2y) \), and (E3), since \( \exp t = y \) gives \( F(t/2) = y \). It is not \( \exp \): \( F(1) = \exp 2 = e^2 \ne e \) because \( e > 1 \). So, by @thm-exp-unique, it must fail (E2), and it does at \( x = -1/2 \): \( F(-1/2) = \exp(-1) = 1/e < 1/2 = 1 + (-1/2) \), as \( e > 2 \). Without (E2), (E1) and (E3) leave the speed of the function free.

## The logarithm

By @prp-exp-first-consequences (b) and (c), \( \exp \) is a strictly increasing map from \( \nR \) into \( (0, \infty) \), and (E3) says that every point of \( (0, \infty) \) is a value. So \( \exp \colon \nR \to (0, \infty) \) is a bijection.

*The logarithm undoes the exponential.*

::: {#def-logarithm}
[The Logarithm]

The **logarithm** \( \log \colon (0, \infty) \to \nR \) is the inverse of the bijection \( \exp \colon \nR \to (0, \infty) \): for \( y > 0 \), \( \log y \) is the **unique** \( x \in \nR \) with \( \exp x = y \).
:::

In words: existence of \( x \) is (E3), uniqueness is the injectivity of a strictly increasing map (@fd2:prp-strictly-monotone-injective). So \( \exp(\log y) = y \) for every \( y > 0 \) and \( \log(\exp x) = x \) for every \( x \in \nR \). By @thm-monotone-inverse, \( \log \) is strictly increasing, and its graph is the graph of \( \exp \) with the coordinates swapped, that is, reflected in the line \( y = x \). We write \( \log \) and never \( \ln \).

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.9]
    \draw[->] (-2.6,0) -- (4.3,0) node[right] {$x$};
    \draw[->] (0,-2.6) -- (0,4.3) node[above] {$y$};
    \draw[dashed] (-2.4,-2.4) -- (4,4) node[above right] {$y = x$};
    \draw[thick, domain=-2.5:1.4, smooth, samples=60] plot (\x, {exp(\x)}) node[above] {$\exp$};
    \draw[thick, domain=0.083:4, smooth, samples=80] plot (\x, {ln(\x)}) node[right] {$\log$};
    \draw (-2.4,-1.4) -- (2,3) node[right] {$y = 1 + x$};
    \fill (0,1) circle (1.5pt) node[left] {$1$};
    \fill (1,0) circle (1.5pt) node[below] {$1$};
\end{tikzpicture}
\end{center}
```

The picture shows \( \exp \) above the line \( y = 1 + x \), touching it at \( (0, 1) \), and \( \log \) as its mirror image in \( y = x \), through \( (1, 0) \). It illustrates; no proof below reads anything off it.

::: {.check}
What are \( \log(\exp 2) \) and \( \log(1/e) \)?
:::

::: {.solution}
\( \log(\exp 2) = 2 \), since \( \log \) undoes \( \exp \). And \( \exp(-1) = 1/\exp 1 = 1/e \) by @prp-exp-first-consequences (b), so \( \log(1/e) = -1 \).
:::

Every rule for \( \log \) is a rule for \( \exp \) read backwards: apply \( \exp \) to both sides and use that \( \exp \) is injective.

::: {#prp-log-rules}
[Rules for the Logarithm]

Let \( x, y \in \nR \) with \( x, y > 0 \).

::: {.enumerate options="label=(\alph*)"}
1. \( \log 1 = 0 \) and \( \log e = 1 \).
2. \( \log(xy) = \log x + \log y \) and \( \log(1/x) = -\log x \).
3. \( 1 - 1/x \le \log x \le x - 1 \), and each inequality is an equality only at \( x = 1 \).
:::
:::

::: {.idea}
For (a) and (b), compute \( \exp \) of each side. For (c), (E2) at \( t = \log x \) gives \( x \ge 1 + \log x \), and at \( t = \log(1/x) \) it gives the other half. Strictness needs \( \exp t > 1 + t \) for \( t \ne 0 \), which the box does not state; we get it by writing \( \exp t \) as a square, \( \exp(t/2)^2 \ge (1 + t/2)^2 = 1 + t + t^2/4 \), legal while \( 1 + t/2 \ge 0 \).
:::

::: {.proof}
(a) \( \exp 0 = 1 \) by @prp-exp-first-consequences (a), and \( \exp 1 = e \) by @def-euler-number; apply @def-logarithm.

(b) By (E1), \( \exp(\log x + \log y) = \exp(\log x)\exp(\log y) = xy \), so \( \log(xy) = \log x + \log y \) by @def-logarithm. Then \( \log x + \log(1/x) = \log 1 = 0 \) by (a).

(c) First, \( \exp t > 1 + t \) for every \( t \ne 0 \). *Case \( t \ge -2 \).* Then \( 1 + t/2 \ge 0 \) and \( \exp(t/2) \ge 1 + t/2 \) by (E2), so by (E1) and @lem-reals-nth-root (a) (or equality),
\[
\exp t = \exp(t/2)^2 \ge \Bigl(1 + \frac t2\Bigr)^{2} = 1 + t + \frac{t^2}{4} > 1 + t ,
\]
the last step because \( t^2 > 0 \) (@fd3:prp-ordered-ring-rules (e)). *Case \( t < -2 \).* Then \( 1 + t < -1 < 0 < \exp t \) by @prp-exp-first-consequences (b).

Now (E2) at \( t = \log x \) gives \( x = \exp(\log x) \ge 1 + \log x \), that is, \( \log x \le x - 1 \); by the strict inequality just proved, it is strict when \( \log x \ne 0 \), that is, when \( x \ne 1 \). By (b), (E2) at \( t = \log(1/x) = -\log x \) gives \( 1/x \ge 1 - \log x \), that is, \( \log x \ge 1 - 1/x \), again strict when \( x \ne 1 \). At \( x = 1 \) all three numbers are \( 0 \).
:::

Part (c) gives numbers: \( 1/2 < \log 2 < 1 \), for example.

## Real powers

*A real power is the exponential of a multiple of a logarithm.*

::: {#def-real-power}
[Real Powers]

Let \( a, x \in \nR \).

- If \( a > 0 \), then \( a^x \coloneqq \exp(x \log a) \).
- If \( a = 0 \) and \( x > 0 \), then \( 0^x \coloneqq 0 \).

No other pair \( (a, x) \) is given a value by this definition; in particular there are **no** real powers of a negative base.
:::

In words: to raise \( a \) to the power \( x \), take the logarithm, multiply by \( x \), and exponentiate. By @def-logarithm, \( \log(a^x) = x \log a \) for \( a > 0 \); this is the definition read through \( \log \), not a theorem.

The symbol \( a^x \) was already in use for \( x \in \nN \) (@fd2:def-power), and Chapter 1 gave \( \sqrt[n]{a} \) and \( a^{m/n} \). The next proposition shows that the new definition agrees with both wherever they overlap, so no symbol now has two meanings.

::: {.second-reading title="Base zero and negative bases"}
**Base zero.** For \( x = n \in \nZ_{>0} \) both definitions give \( 0^n = 0 \). For \( x = 0 \), @def-real-power says nothing, and \( 0^0 \) keeps the value \( 1 \) that @fd2:def-power gives it as a natural-number power. For \( x < 0 \), \( 0^x \) would have to be \( 1/0^{-x} = 1/0 \), so it is left undefined.

**Negative bases.** \( \log a \) is defined only for \( a > 0 \), so the formula \( \exp(x \log a) \) cannot start. One could set \( (-8)^{1/3} \coloneqq -2 \), but the rule \( (a^x)^y = a^{xy} \) would then break: with \( x = 2 \) and \( y = 1/6 \) it would give \( (-8)^{1/3} = ((-8)^2)^{1/6} = 64^{1/6} = 2 \), not \( -2 \). The real cube root of a negative number is a separate object, \( \sqrt[3]{-8} = -2 \) of @exm-odd-roots, and it keeps its own symbol.
:::

::: {.check}
Does @def-real-power give \( 0^0 \) a value? Is \( (1/2)^{-1} = 2 \)?
:::

::: {.solution}
No: base \( 0 \) is covered only for \( x > 0 \). (The symbol \( 0^0 \) keeps its natural-number value \( 1 \) from @fd2:def-power, which this definition does not touch.) Yes: \( (1/2)^{-1} = \exp(-\log(1/2)) = \exp(\log 2) = 2 \), since \( -\log(1/2) = \log 2 \) by @prp-log-rules (b).
:::

::: {#prp-real-power-consistent}
[Real Powers Agree with Roots and Integer Powers]

Let \( a \in \nR \) with \( a > 0 \).

::: {.enumerate options="label=(\alph*)"}
1. For \( m \in \nZ \) and \( n \in \nZ_{>0} \), \( a^{m/n} = \sqrt[n]{a^m} \), where \( a^m \) is the power of @fd2:def-power for \( m \ge 0 \) and \( 1/a^{-m} \) for \( m < 0 \).
2. In particular, for \( n = 1 \), the real power \( a^m \) is the integer power \( a^m \).
3. \( e^x = \exp x \) for every \( x \in \nR \).
:::
:::

::: {.idea}
Show that \( a^{m/n} \) is a non-negative number whose \( n \)-th power is \( a^m \); the uniqueness of roots does the rest.
:::

::: {.proof}
(a) By @def-real-power and @prp-exp-first-consequences (b), \( b \coloneqq a^{m/n} = \exp((m/n) \log a) > 0 \). By @prp-exp-first-consequences (e), used twice,
\[
b^n = \exp\Bigl(n \cdot \frac mn \log a\Bigr) = \exp(m \log a) = \bigl(\exp(\log a)\bigr)^m = a^m ,
\]
with \( a^m \) read as in the statement (part (e) covers \( m < 0 \) with the convention \( u^{-k} = 1/u^k \)). So \( b \ge 0 \) and \( b^n = a^m \), where \( a^m > 0 \). By the uniqueness in @lem-reals-nth-root (b), \( b = \sqrt[n]{a^m} \).

(b) At \( n = 1 \), \( \sqrt[1]{a^m} \) is the unique \( b \ge 0 \) with \( b^1 = a^m \), which is \( a^m \) itself.

(c) By @prp-log-rules (a), \( e^x = \exp(x \log e) = \exp(x \cdot 1) = \exp x \).
:::

From now on \( e^x \) and \( \exp x \) are the same thing, and we use whichever reads better.

::: {.check}
Is \( 4^{1/2} = 2 \)? Answer from @prp-real-power-consistent.
:::

::: {.solution}
Yes. By (a) with \( m = 1 \), \( n = 2 \), \( 4^{1/2} = \sqrt{4^1} \), the unique non-negative real number whose square is \( 4 \). Since \( 2 \ge 0 \) and \( 2^2 = 4 \), that number is \( 2 \).
:::

The laws of exponents now come in one line each, because each is a law of \( \exp \) or of \( \log \) in disguise.

::: {#prp-real-power-laws}
[Laws of Real Powers]

Let \( a, b, x, y \in \nR \) with \( a, b > 0 \).

::: {.enumerate options="label=(\alph*)"}
1. \( a^{x + y} = a^x a^y \) and \( a^{-x} = 1/a^x \).
2. \( (a^x)^y = a^{xy} \).
3. \( (ab)^x = a^x b^x \).
4. \( a^x > 0 \).
5. As a function of \( x \) on \( \nR \): \( x \mapsto a^x \) is strictly increasing if \( a > 1 \), strictly decreasing if \( a < 1 \), and constant \( 1 \) if \( a = 1 \).
6. As a function of \( a \) on \( (0, \infty) \): \( a \mapsto a^x \) is strictly increasing if \( x > 0 \) and strictly decreasing if \( x < 0 \).
:::
:::

::: {.idea}
Write each power as \( \exp \) of a product and use (E1), the log rules, and the monotonicity of \( \exp \) and \( \log \).
:::

::: {.proof}
(a) \( a^{x+y} = \exp(x \log a + y \log a) = a^x a^y \) by (E1); \( a^{-x} = \exp(-x \log a) = 1/a^x \) by @prp-exp-first-consequences (b).

(b) \( a^x > 0 \) by (d), and \( \log(a^x) = x \log a \), so \( (a^x)^y = \exp(y x \log a) = a^{xy} \).

(c) \( (ab)^x = \exp(x \log a + x \log b) = a^x b^x \), by @prp-log-rules (b) and (E1).

(d) This is @prp-exp-first-consequences (b).

(e) If \( a > 1 \), then \( \log a > \log 1 = 0 \), since \( \log \) is strictly increasing, so \( x \mapsto x \log a \) is strictly increasing (@fd3:prp-ordered-ring-rules (c)); composing with the strictly increasing \( \exp \) gives a strictly increasing function (@prp-monotone-algebra (e)). If \( a < 1 \), then \( \log a < 0 \), \( x \mapsto x \log a \) is strictly decreasing (@fd3:prp-ordered-ring-rules (d)), and the composite is strictly decreasing by the same rule. If \( a = 1 \), \( a^x = \exp 0 = 1 \).

(f) Let \( 0 < a < b \). Then \( \log a < \log b \). If \( x > 0 \), then \( x \log a < x \log b \), and \( \exp \) keeps the order; if \( x < 0 \), the order is reversed and \( \exp \) keeps the reversed order.
:::

::: {.check}
Is \( 2^{\sqrt 2} > 2 \)? Is \( (\sqrt 2)^{\sqrt 2} < 2 \)?
:::

::: {.solution}
Yes to both. Since \( 1^2 = 1 < 2 = (\sqrt 2)^2 \), we have \( \sqrt 2 > 1 \) (@fd3:prp-ordered-ring-rules (g)), and \( x \mapsto 2^x \) is strictly increasing by @prp-real-power-laws (e); so \( 2^{\sqrt 2} > 2^1 = 2 \). For the second, \( \sqrt 2 = 2^{1/2} \) by @prp-real-power-consistent (a), so by @prp-real-power-laws (b), \( (\sqrt 2)^{\sqrt 2} = 2^{\sqrt 2/2} \). Since \( (\sqrt 2)^2 = 2 < 4 = 2^2 \), \( \sqrt 2 < 2 \), so \( \sqrt 2/2 < 1 \) and \( 2^{\sqrt 2/2} < 2^1 = 2 \).
:::

## The exponential outruns every power

How fast does \( \exp x \) grow? (E2) gives only \( \exp x \ge 1 + x \), which a linear function matches. Raising (E2) to a power, as in the proof of @thm-exp-unique, does much better.

::: {#prp-exp-beats-powers}
[The Exponential Beats Every Power]

::: {.enumerate options="label=(\alph*)"}
1. For every \( x > 0 \) and every \( k \in \nN \), \( \exp x > \bigl(x/(k + 1)\bigr)^{k+1} \). Hence, for every \( M > 0 \), \( \exp x > M x^k \) for all \( x > M (k + 1)^{k+1} \).
2. For every \( x > 0 \) and every \( m \in \nZ_{>0} \), \( \log x < m x^{1/m} \). Hence, for every \( \varepsilon > 0 \), \( \log x < \varepsilon x \) for all \( x > 4/\varepsilon^2 \).
:::
:::

::: {.idea}
For (a), split \( x \) into \( k + 1 \) equal parts and apply (E2) to each: \( \exp x = \exp(x/(k + 1))^{k+1} \ge (1 + x/(k + 1))^{k+1} \), and dropping the \( 1 \) costs only strictness. For (b), apply \( \log t \le t - 1 \) not at \( x \) but at \( x^{1/m} \), which is much smaller.
:::

::: {.proof}
(a) Let \( x > 0 \), \( k \in \nN \), \( t \coloneqq x/(k + 1) > 0 \). By (E2), \( \exp t \ge 1 + t > t \ge 0 \), so by @prp-exp-first-consequences (e) and @lem-reals-nth-root (a),
\[
\exp x = (\exp t)^{k+1} > t^{k+1} = \frac{x^{k+1}}{(k + 1)^{k+1}} = x^k \cdot \frac{x}{(k + 1)^{k+1}} .
\]
If \( M > 0 \) and \( x > M(k + 1)^{k+1} \), then \( x > 0 \), \( x^k > 0 \) and \( x/(k + 1)^{k+1} > M \), so the right side exceeds \( M x^k \).

(b) Let \( x > 0 \) and \( m \in \nZ_{>0} \). By @def-real-power, \( \log(x^{1/m}) = (1/m) \log x \), so by @prp-log-rules (c) at \( x^{1/m} > 0 \),
\[
\log x = m \log(x^{1/m}) \le m (x^{1/m} - 1) < m x^{1/m} .
\]
Now let \( \varepsilon > 0 \) and \( x > 4/\varepsilon^2 \), and take \( m = 2 \), where \( x^{1/2} = \sqrt x \) by @prp-real-power-consistent (a). Since \( \sqrt x \ge 0 \) and \( (\sqrt x)^2 = x > (2/\varepsilon)^2 \), @fd3:prp-ordered-ring-rules (g) gives \( \sqrt x > 2/\varepsilon \), so \( 2 < \varepsilon \sqrt x \) and \( 2\sqrt x < \varepsilon \sqrt x \sqrt x = \varepsilon x \). Hence \( \log x < 2\sqrt x < \varepsilon x \).
:::

The thresholds are explicit: \( \exp x > 1000\, x^2 \) once \( x > 1000 \cdot 27 = 27{,}000 \), and \( \log x < x/100 \) once \( x > 40{,}000 \). They are far from the best, and need not be good: they need to exist, depending on \( M \), \( k \) or \( \varepsilon \) only, never on \( x \).

## Exercises

### A. Check your understanding

::: {#exr-exponential-and-logarithm-a1}
[A1]

These questions are about the proof of @thm-exp-unique.

::: {.enumerate options="label=(\alph*)"}
1. Which of (E1), (E2), (E3) does the proof use, including through @prp-exp-first-consequences?
2. Where does Bernoulli's inequality enter, and at which real number is it applied?
3. Write out the two bounds on \( e \) that the proof gives at \( x = 1 \), \( n = 2 \).
4. Take \( x = -3 \) and \( n = 2 \). Which step of the upper-bound argument fails? Is its conclusion \( (1 + x/n)^n \le \exp x \) still true for this pair?
:::
:::

::: {.solution}
(a) Only (E1) and (E2). The proof of @prp-exp-first-consequences uses (E1), (E2) and field and order rules; the proof of the theorem adds (E2) at \( x/n \). (E3) is not used, which is why the uniqueness sentence asks only for (E1) and (E2).

(b) In the lower estimate, to bound \( (1 - x^2/n^2)^n \) below by \( 1 - x^2/n \). It is applied at \( -x^2/n^2 \), which is \( \ge -1 \) because \( n > \abs{x} \).

(c) \( (1 + 1/2)^2 = 9/4 \le e \le (1 - 1/2)^{-2} = 4 \).

(d) Here \( n = 2 < 3 = \abs{x} \), and \( 1 + x/n = -1/2 < 0 \). The step "raise \( 1 + x/n \le \exp(x/n) \) to the \( n \)-th power" fails: @lem-reals-nth-root (a) needs a non-negative smaller side. The conclusion fails too: \( (-1/2)^2 = 1/4 \), while \( \exp(-3) = 1/\exp 3 < 1/4 \), because \( \exp 3 > 1 + 3 = 4 \) (strictly, by the first step of the proof of @prp-log-rules (c)).
:::

::: {#exr-exponential-and-logarithm-a2}
[A2]

True or false? Give a reason or a counterexample.

::: {.enumerate options="label=(\alph*)"}
1. \( \exp(2x) = (\exp x)^2 \) for every \( x \in \nR \).
2. \( \log(x + y) = \log x + \log y \) for all \( x, y > 0 \).
3. @def-real-power defines \( (-8)^{1/3} \).
4. \( a^x b^y = (ab)^{x + y} \) for all \( a, b > 0 \) and \( x, y \in \nR \).
:::
:::

::: {.solution}
(a) True, by (E1) with \( y = x \) (or @prp-exp-first-consequences (e) with \( n = 2 \)).

(b) False. At \( x = y = 1 \) the left side is \( \log 2 \) and the right side is \( 0 \); but \( \log 2 > \log 1 = 0 \), since \( \log \) is strictly increasing.

(c) False: the base \( -8 \) is negative, and @def-real-power gives no real powers of a negative base. The real number \( \sqrt[3]{-8} = -2 \) is the odd root of @exm-odd-roots, a different symbol.

(d) False. With \( a = 1 \), \( b = 2 \), \( x = 1 \), \( y = 0 \): the left side is \( 1^1 \cdot 2^0 = 1 \), the right side \( 2^1 = 2 \) (values by @prp-real-power-consistent (b)).
:::

### B. Practice

::: {#exr-exponential-and-logarithm-b1}
[B1]

Prove that \( 2.5 < e < 3 \).

*Hint: one value of \( n \) in the bounds after @def-euler-number does both.*
:::

::: {.solution}
Take \( n = 6 \). The lower bound gives
\[
e \ge \Bigl(\frac76\Bigr)^{6} = \frac{117649}{46656} > \frac52 ,
\]
because \( 2 \cdot 117649 = 235298 > 233280 = 5 \cdot 46656 \). The upper bound gives
\[
e \le \Bigl(1 - \frac16\Bigr)^{-6} = \Bigl(\frac65\Bigr)^{6} = \frac{46656}{15625} < 3 ,
\]
because \( 46656 < 46875 = 3 \cdot 15625 \). Hence \( 2.5 < e < 3 \). (Smaller \( n \) is not enough: at \( n = 5 \) the upper bound is \( (5/4)^5 = 3125/1024 > 3 \).)
:::

::: {#exr-exponential-and-logarithm-b2}
[B2: Prove or disprove]

Prove each true statement and give a counterexample to each false one.

::: {.enumerate options="label=(\alph*)"}
1. \( \exp x \ge 1 + x + x^2/2 \) for every \( x \ge 0 \).
2. \( \log x \le x/e \) for every \( x > 0 \).
3. If \( 0 < a \le b \), then \( a^x \le b^x \) for every \( x \in \nR \).
4. There is a polynomial function \( p \) on \( \nR \) (@def-polynomial-rational-function) with \( p(x) = \exp x \) for every \( x \in \nR \).
:::
:::

::: {.solution}
(a) **True.** Let \( x \ge 0 \) and \( n \in \nZ_{>0} \) with \( n > x \). By the binomial theorem in the commutative ring \( \nR \) (@thm-binomial-commutative-ring), \( (1 + x/n)^n \) is a sum of non-negative terms, among them \( 1 \), \( n \cdot x/n = x \) and \( \binom n2 x^2/n^2 = (1 - 1/n) x^2/2 \). Dropping the others,
\[
\exp x \ge \Bigl(1 + \frac xn\Bigr)^{n} \ge 1 + x + \frac{x^2}{2} - \frac{x^2}{2n} ,
\]
where the first inequality is the upper-bound half of @thm-exp-unique. Suppose \( \delta \coloneqq 1 + x + x^2/2 - \exp x > 0 \). Then \( x \ne 0 \) (at \( x = 0 \), \( \delta = 0 \)), and the display gives \( x^2/(2n) \ge \delta \) for every \( n > x \). By @fd3:prp-archimedean-reciprocal there is \( n > x \) with \( 1/n < 2\delta/x^2 \), a contradiction. So \( \delta \le 0 \).

(b) **True.** By @prp-log-rules (b), (a) and (c), \( \log x = \log(e \cdot x/e) = 1 + \log(x/e) \le 1 + (x/e - 1) = x/e \).

(c) **False.** Take \( a = 1 \), \( b = 2 \), \( x = -1 \): \( 1^{-1} = 1 > 1/2 = 2^{-1} \). The statement holds for \( x \ge 0 \) (@prp-real-power-laws (f), with equality at \( x = 0 \)) and reverses for \( x < 0 \).

(d) **False.** Suppose \( p(x) = \sum_{i=0}^{d} a_i x^i = \exp x \) for all \( x \). Put \( S \coloneqq \sum_{i<d} \abs{a_i} \) and \( M \coloneqq S + \abs{a_d} + 1 \ge 1 \). For \( x \ge 1 \) we have \( x^i \le x^d \) for \( i \le d \) (@fd2:prp-power-laws (e), or equality), so by the triangle inequality (@fd3:prp-absolute-value-ordered-field (e)) \( \abs{p(x)} \le (S + \abs{a_d}) x^d < M x^d \). By @prp-exp-beats-powers (a) with \( k = d \), any \( x > M(d + 1)^{d+1} \), which is \( \ge 1 \), has \( \exp x > M x^d > \abs{p(x)} \ge p(x) \), a contradiction.
:::

::: {#exr-exponential-and-logarithm-b3}
[B3: Put the proof in order]

Here are lines of the lower estimate in the proof of @thm-exp-unique, shuffled, with two lines that do not belong. Write an order of the correct lines that makes a proof, and say why each distractor fails.

::: {.enumerate options="label=(\roman*)"}
1. Fix \( x \in \nR \) and an integer \( n > \abs{x} \).
2. Then \( 1 + x/n > 0 \) and \( 1 - x/n > 0 \).
3. By @prp-exp-first-consequences (d), \( \exp(x/n) \le 1/(1 - x/n) \), so \( \exp x \le (1 - x/n)^{-n} \).
4. \( (1 + x/n)^n = (1 - x^2/n^2)^n (1 - x/n)^{-n} \).
5. So \( (1 + x/n)^n \ge (1 - x^2/n^2)^n \exp x \).
6. Bernoulli's inequality at \( -x^2/n^2 \ge -1 \) gives \( (1 - x^2/n^2)^n \ge 1 - x^2/n \).
7. Hence \( (1 + x/n)^n \ge \exp x - x^2 \exp x / n \).
8. (D1) By (E2), \( \exp x \ge 1 + x \), so \( (1 + x/n)^n \ge 1 + x \).
9. (D2) Bernoulli's inequality at \( x^2/n^2 \) gives \( (1 - x^2/n^2)^n \ge 1 + x^2/n \).
:::
:::

::: {.solution}
Each line may come only after the lines it uses: (ii) uses (i); (iii) uses (ii) (it needs \( x/n < 1 \) and positive sides); (iv) uses (ii) (it divides by \( 1 - x/n \ne 0 \)); (v) uses (iii) and (iv); (vi) uses only (i) (it needs \( x^2/n^2 \le 1 \)); (vii) uses (v) and (vi). **Every order respecting these constraints is accepted.** One is (i), (ii), (iii), (iv), (v), (vi), (vii); another is (i), (vi), (ii), (iv), (iii), (v), (vii).

(D1) bounds the wrong thing: the goal is a lower bound by \( \exp x - C/n \), and \( 1 + x \) is not one. (Its "so" is also unjustified: \( (1 + x/n)^n \ge 1 + x \) is Bernoulli's inequality, not a consequence of \( \exp x \ge 1 + x \).) (D2) has the wrong sign: Bernoulli's inequality at \( u = -x^2/n^2 \) gives \( 1 + nu = 1 - x^2/n \), and the claimed bound is false, since for \( x \ne 0 \) the left side is \( < 1 \) and the right side \( > 1 \).
:::

### C. Going deeper

::: {#exr-exponential-and-logarithm-c1}
[C1: Find the error]

Here is a proof that \( \exp \) is strictly increasing: "Let \( x < y \). By (E1), \( \exp y - \exp x = \exp(y - x) \), and by (E2), \( \exp(y - x) \ge 1 + (y - x) > 0 \). So \( \exp y > \exp x \)." Is the conclusion true? Does the argument prove it? Name the line that fails, and show that it fails with numbers.
:::

::: {.solution}
The conclusion is true: it is @prp-exp-first-consequences (c). The argument does not prove it. The first equality is false: (E1) gives the **quotient** \( \exp y / \exp x = \exp(y - x) \), not the difference. At \( x = 0 \), \( y = 1 \): \( \exp 1 - \exp 0 = e - 1 \), while \( \exp(1 - 0) = e \), and \( e - 1 \ne e \). The correct line is \( \exp y - \exp x = \exp x \cdot (\exp(y - x) - 1) \), after which the rest of the argument, with \( \exp x > 0 \), goes through.
:::

::: {#exr-exponential-and-logarithm-c2}
[C2: Exit check: the logarithm is slower than every root]

::: {.enumerate options="label=(\alph*)"}
1. Prove that for every \( \varepsilon > 0 \) there is \( X \) such that \( \log x < \varepsilon x \) for every \( x > X \).
2. Let \( m \in \nZ_{>0} \). Prove that for every \( \varepsilon > 0 \) there is \( X \) such that \( \log x < \varepsilon x^{1/m} \) for every \( x > X \).
:::
:::

::: {.solution}
[Hint 1]

For (a), compare \( \log x \) with a root of \( x \), using the box fact through @prp-log-rules (c).
:::

::: {.solution}
[Hint 2]

For (b), put \( y \coloneqq x^{1/m} \) and apply (a) to \( y \) with a smaller \( \varepsilon \).
:::

::: {.solution}
(a) Let \( \varepsilon > 0 \) and \( X \coloneqq 4/\varepsilon^2 \); it depends on \( \varepsilon \) only. For \( x > X \), @prp-exp-beats-powers (b) gives \( \log x < 2 \sqrt x < \varepsilon x \): the first inequality is \( \log x \le m(x^{1/m} - 1) \) at \( m = 2 \), which comes from \( \log t \le t - 1 \) (@prp-log-rules (c), itself (E2) read through \( \log \)); the second holds because \( \sqrt x > 2/\varepsilon \).

(b) Let \( \varepsilon > 0 \). Put \( Y \coloneqq 4m^2/\varepsilon^2 \), the threshold of (a) for \( \varepsilon/m \), and \( X \coloneqq Y^m \); both depend on \( \varepsilon \) and \( m \) only. Let \( x > X \) and \( y \coloneqq x^{1/m} > 0 \). Since \( a \mapsto a^{1/m} \) is strictly increasing on \( (0, \infty) \) (@prp-real-power-laws (f)), \( y > X^{1/m} = (Y^m)^{1/m} = Y \) (@prp-real-power-laws (b)). By (a) applied to \( y \) and \( \varepsilon/m \), \( \log y < (\varepsilon/m) y \). By @prp-real-power-laws (b) and @prp-real-power-consistent (b), \( y^m = x^{(1/m) m} = x \), and by @def-real-power, \( \log x = \log(y^m) = m \log y \), so \( \log x < \varepsilon y = \varepsilon x^{1/m} \).

**Marking scheme.** (10 points)

- 3: a bound \( \log x \le c\sqrt x \) (or \( \le c\, x^{1/k} \)) with the box fact or log rule it comes from named.
- 3: an explicit \( X \) depending on \( \varepsilon \) only, and a check that \( x > X \) gives \( \log x < \varepsilon x \).
- 2: the substitution \( y = x^{1/m} \) in (b), with the monotonicity of \( a \mapsto a^{1/m} \) cited to pass from \( x > X \) to \( y > Y \).
- 2: the quantifiers in the order \( \varepsilon \), then \( X \), then every \( x > X \).

A route through @prp-exp-beats-powers (a) (put \( x = \exp t \)) earns the same points step for step. Fatal errors (0 for the step): \( X \) chosen depending on \( x \); any use of derivatives, l'Hôpital's rule or limits of functions.
:::

<!-- dependency ledger
sec-exponential-and-logarithm (claim): sqrt 2 is not m/n with m, n in Z | fd3:thm-no-rational-square-two transported by fd3:thm-rationals-embed-ordered-field (cited in prose)
sec-exponential-and-logarithm (claim): constant 1 satisfies (E1) not (E2); 1 + x satisfies (E2) not (E1) (3 vs 4) | inline arithmetic
sec-exponential-and-logarithm (claim): Nothing in Sections 8.1-8.4, and nothing in this section above the box, uses ax-exponential | blueprint merged-ch08-f47.md ("What this chapter borrows"); checkable by grep for ax-exponential, exp, log, e in 8.1-8.4
sec-exponential-and-logarithm (claim): exp is continuous and its own derivative (warning, not used) | AN1.10 (where the box is paid); nothing depends on it
ax-exponential (claim): paid in AN1.10 (named in the box); its R is ours by fd3:thm-cof-uniqueness | AN1.10 (borrow)
sec-exponential-and-logarithm (claim): u^(-n) := 1/u^n for u != 0, n >= 1; u^(-n) = (1/u)^n | inline, fd2:prp-power-laws (c)
prp-exp-first-consequences (proof): a non-zero element >= 0 is > 0; x/2 + x/2 = x | fd3:prp-ordered-field-halves (a), (b)
prp-exp-first-consequences (proof): (O4) product of positives is positive | fd3 ordered-field axiom (O4)
exm-method-archimedes-squeeze (proof): L upper bound and no smaller upper bound => L = sup S | fd2:def-order-supremum
thm-exp-unique (proof): exists N0 in Z>0 with N0 > |x| (Archimedean property of R) | fd3:thm-reals-complete-ordered-field, fd3:thm-cof-complete-archimedean (cited before the theorem)
thm-exp-unique (proof): 0 <= s <= t => s^n <= t^n (the "or equality" case of lem-reals-nth-root (a)) | lem-reals-nth-root (a) plus equality
thm-exp-unique (proof): (1 + x/n)(1 - x/n) = 1 - x^2/n^2; 1 - x^2/n >= 1 - (x^2 + 1)/n | inline field arithmetic
thm-exp-unique (proof): uniqueness: the proof of prp-exp-first-consequences uses only (E1), (E2) | inline (meta-claim checkable on the page: the proof of prp-exp-first-consequences names (E1), (E2) only)
def-euler-number (claim): (1 + 1/n)^n <= e <= (1 - 1/n)^(-n), n >= 2; 9/4, 4 at n = 2 | thm-exp-unique proof; verify/ch08/def-euler-number.py
sec-exponential-and-logarithm (claim): exp(2x) satisfies (E1), (E3), fails (E2) at -1/2; e^2 != e since e > 1 | inline; def-euler-number bounds (e >= 9/4)
def-logarithm (claim): exp: R -> (0, inf) bijective; inverse strictly increasing; graph reflection | thm-monotone-inverse (8.2), fd2:prp-strictly-monotone-injective
prp-log-rules (proof): (1 + t/2)^2 = 1 + t + t^2/4 | inline arithmetic
sec-exponential-and-logarithm (claim): 1/2 < log 2 < 1 | prp-log-rules (c) at x = 2; verify/ch08/prp-log-rules.py
prp-real-power-laws (proof): composite of strictly increasing / decreasing maps | prp-monotone-algebra (e) (8.2)
prp-real-power-laws (proof): log strictly increasing, log 1 = 0 | def-logarithm, prp-log-rules (a)
prp-exp-beats-powers (proof): t^(k+1) = x^(k+1)/(k+1)^(k+1) | fd2:prp-power-laws (c)
sec-exponential-and-logarithm (claim): thresholds 27,000 for exp x > 1000 x^2 and 40,000 for log x < x/100 | verify/ch08/prp-exp-beats-powers.py
exr-exponential-and-logarithm-a1 (solution): exp 3 > 4 strictly | proof of prp-log-rules (c), first step
exr-exponential-and-logarithm-b1 (solution): (7/6)^6 = 117649/46656, (6/5)^6 = 46656/15625, (5/4)^5 = 3125/1024 and comparisons | verify/ch08/exr-exponential-and-logarithm-b1.py
exr-exponential-and-logarithm-b2 (solution): binomial terms of (1 + x/n)^n are >= 0 for x >= 0; C(n,2)/n^2 = (1 - 1/n)/2 | thm-binomial-commutative-ring; verify/ch08/exr-exponential-and-logarithm-b2.py
exr-exponential-and-logarithm-b2 (solution): x^i <= x^d for x >= 1, i <= d | fd2:prp-power-laws (e)
exr-exponential-and-logarithm-b2 (solution): triangle inequality for a finite sum; |a_i x^i| = |a_i| x^i for x >= 1 | fd3:prp-absolute-value-ordered-field (e) with induction on the number of terms (inline)
exr-exponential-and-logarithm-b2 (solution): p(x) = sum a_i x^i as the value of the polynomial function | def-polynomial-rational-function (8.1), def-polynomial-evaluation
exr-exponential-and-logarithm-b3 (solution): partial order of lines and distractor (D2) sign | inline
exr-exponential-and-logarithm-c2 (solution): x = y^m from y = x^(1/m) | prp-real-power-laws (b), prp-real-power-consistent (b)
-->
