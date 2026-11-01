# A Table of Strange Functions

The later volumes will define continuity, limits of functions and the integral, and each definition will be tested on functions that resist being drawn. This section collects those functions in one place. For each we prove what can be proved with the tools of this chapter: the order, the floor, suprema and finite counting. What needs a limit we only ask, and the questions go into a table at the end.

## Irrationals between any two reals

Most of the functions below treat rational and irrational points differently, so we need both kinds in every interval. The rationals are dense (@fd3:thm-rationals-dense-ordered-field). The irrationals are dense too. *Number Systems* left this as an exercise (@fd3:exr-rationals-inside-the-reals-c2), and we prove it here. A real number is **irrational** if it is not in \( \nQ \).

::: {#lem-irrationals-dense}
[Irrationals Are Dense]

For all \( a, b \in \nR \) with \( a < b \) there is an irrational \( x \) with \( a < x < b \).
:::

::: {.proof}
Let \( a < b \). The real numbers form a complete ordered field (@fd3:thm-reals-complete-ordered-field). So there is \( \sqrt 2 \ge 0 \) with \( (\sqrt 2)^2 = 2 \), and \( \nR \) is Archimedean. Since \( a - \sqrt 2 < b - \sqrt 2 \), the density of the rationals gives \( q \in \nQ \) with \( a - \sqrt 2 < q < b - \sqrt 2 \) (@fd3:thm-rationals-dense-ordered-field). Put \( x \coloneqq q + \sqrt 2 \); then \( a < x < b \).

Suppose \( x \) were rational. Then \( \sqrt 2 = x - q \) would be rational, as a difference of rationals. But \( \sqrt 2 \) is irrational, as Section 8.3 showed from @fd3:thm-no-rational-square-two and the copy of \( \nQ \) inside \( \nR \), a contradiction. Hence \( x \) is irrational.

::: {.uses}
@fd3:prp-cof-square-roots (square roots exist); @fd3:thm-cof-complete-archimedean (\( \nR \) is Archimedean); @fd3:thm-rationals-embed-ordered-field (\( \nQ \) sits inside \( \nR \)).
:::
:::

The argument for irrationality works for every rational \( q \): \( q + \sqrt 2 \) is irrational.

::: {.check}
Why does the proof shift by \( \sqrt 2 \), and not by \( 1/2 \)?
:::

::: {.solution}
For rational \( q \), the number \( q + 1/2 \) is rational, so the shift would land on a rational. The proof needs a shift that turns every rational into an irrational, and an irrational shift does that.
:::

## The Dirichlet function

The simplest function that no pencil can draw is the indicator of the rationals.

::: {#def-dirichlet-function}
[The Dirichlet Function]

The **Dirichlet function** is \( D \coloneqq \ind_{\nQ} \colon \nR \to \nR \) (@fd2:def-indicator): \( D(x) = 1 \) for \( x \in \nQ \), and \( D(x) = 0 \) for \( x \notin \nQ \).
:::

::: {#prp-dirichlet-properties}
[Properties of the Dirichlet Function]

::: {.enumerate options="label=(\alph*)"}
1. A real \( p \ne 0 \) is a period of \( D \) (@def-periodic-function) if and only if \( p \in \nQ \).
2. For all \( a < b \), \( \sup_{(a, b)} D = 1 \) and \( \inf_{(a, b)} D = 0 \), both attained, and \( \sup \{ \abs{D(x) - D(y)} : x, y \in (a, b) \} = 1 \).
3. For all \( a < b \), \( D \) is neither increasing nor decreasing on \( (a, b) \).
:::
:::

::: {.proof}
(a) Let \( p \in \nQ \), \( p \ne 0 \). Since \( \nQ \) is closed under sums and negatives, \( x \in \nQ \) if and only if \( x + p \in \nQ \), so \( D(x + p) = D(x) \) for every \( x \). Let \( p \notin \nQ \). Then \( D(0) = 1 \) and \( D(0 + p) = 0 \), so \( p \) is not a period.

(b) Every value of \( D \) is \( 0 \) or \( 1 \). The interval \( (a, b) \) contains a rational, where \( D \) is \( 1 \) (@fd3:thm-rationals-dense-ordered-field). It also contains an irrational, where \( D \) is \( 0 \) (@lem-irrationals-dense). An upper bound of \( D((a, b)) \) that is itself a value is its supremum, so \( \sup_{(a, b)} D = 1 \) is attained; likewise \( \inf_{(a, b)} D = 0 \). Since \( D \) is bounded on the non-empty set \( (a, b) \), @prp-sup-oscillation gives \( \sup \{ \abs{D(x) - D(y)} : x, y \in (a, b) \} = 1 - 0 = 1 \).

(c) By @lem-irrationals-dense there is an irrational \( t \in (a, b) \). The rationals are dense, so there are rationals \( q_1 \in (a, t) \) and \( q_2 \in (t, b) \). Then \( q_1 < t \) and \( D(q_1) = 1 > 0 = D(t) \), so \( D \) is not increasing on \( (a, b) \). Also \( t < q_2 \) with \( D(t) = 0 < 1 = D(q_2) \), so it is not decreasing.

::: {.uses}
@fd2:def-order-supremum (a bound that is a value); @fd3:thm-rationals-dense-ordered-field (the rationals are dense).
:::
:::

```{=latex}
\begin{center}
\begin{tikzpicture}[x=6cm, y=2cm]
  \draw[->] (-0.05,0) -- (1.1,0) node[right] {$x$};
  \draw[->] (0,-0.1) -- (0,1.3);
  \draw[densely dotted, thick] (0,1) -- (1,1);
  \draw[densely dotted, thick] (0,0.02) -- (1,0.02);
  \node[left] at (0,1) {$1$};
  \node[below] at (1,0) {$1$};
  \node[below left] at (0,0) {$0$};
\end{tikzpicture}
\end{center}
```

*The Dirichlet function on \( [0, 1] \): the rational points sit on the upper dotted line, the irrational points on the lower one, and every stretch of either line contains points of both kinds.*

**Multiplying by \( x \).** Let \( g(x) \coloneqq x D(x) \) on \( \nR \): \( g(x) = x \) on \( \nQ \) and \( 0 \) off \( \nQ \). Then \( \abs{g(x)} \le \abs{x} \) for every \( x \), so near \( 0 \) the values of \( g \) are small. Away from \( 0 \) they are not. Let \( a \ne 0 \) and \( \delta > 0 \). If \( a \in \nQ \), an irrational \( x \) with \( \abs{x - a} < \delta \) (@lem-irrationals-dense) gives \( \abs{g(x) - g(a)} = \abs{a} \). If \( a \notin \nQ \), a rational \( x \) with \( \abs{x - a} < \min\{\delta, \abs{a}/2\} \) gives
\[
\abs{g(x) - g(a)} = \abs{x} \ge \abs{a} - \abs{x - a} > \abs{a}/2 ,
\]
by the triangle inequality (@fd3:prp-absolute-value-ordered-field (e)). So every interval around \( a \ne 0 \), however short, holds points where \( g \) differs from \( g(a) \) by at least \( \abs{a}/2 \).

## Thomae's function

The Dirichlet function gives every rational the same value. Thomae's function gives a rational a value that shrinks with its denominator. For example, it gives \( 1/2 \) the value \( 1/2 \), both \( 1/3 \) and \( 2/3 \) the value \( 1/3 \), and \( 3/4 \) the value \( 1/4 \). At an irrational point it is \( 0 \).

::: {#def-thomae-function}
[Thomae's Function]

For \( x \in \nQ \), let \( x = p/q \) with \( p \in \nZ \), \( q \in \nZ_{>0} \) and \( \gcd(p, q) = 1 \); the pair \( (p, q) \) is unique (@prp-rationals-lowest-terms (a)). **Thomae's function** \( T \colon \nR \to \nR \) is
\[
T(x) \coloneqq \begin{cases} 1/q & \text{if } x = p/q \in \nQ \text{ in lowest terms,} \\ 0 & \text{if } x \notin \nQ . \end{cases}
\]
:::

Since \( 0 = 0/1 \) and \( \gcd(0, 1) = 1 \), \( T(0) = 1 \); likewise \( T(n) = 1 \) for every \( n \in \nZ \). On \( \nQ \), \( 0 < T \le 1 \), since \( q \ge 1 \).

::: {.warning}
The denominator is read **after** cancelling: \( T(2/4) = T(1/2) = 1/2 \), not \( 1/4 \). Without lowest terms, "\( 1/q \) at \( p/q \)" is not a function at all, since \( 1/2 = 2/4 \) would get the two values \( 1/2 \) and \( 1/4 \).
:::

::: {.check}
Compute \( T(3/4) \), \( T(-6/8) \), \( T(0.6) \) and \( T(\sqrt 2/2) \).
:::

::: {.solution}
- \( T(3/4) = 1/4 \).
- \( T(-6/8) = 1/4 \), since \( -6/8 = -3/4 \) and \( \gcd(-3, 4) = 1 \).
- \( T(0.6) = 1/5 \), since \( 0.6 = 3/5 \).
- \( T(\sqrt 2/2) = 0 \), since \( \sqrt 2/2 \) is irrational. Indeed, if \( \sqrt 2/2 = r \in \nQ \), then \( \sqrt 2 = 2r \in \nQ \). But \( \sqrt 2 \) is irrational, as shown in Section 8.3.
:::

Large values of \( T \) are rare. On \( [0, 1] \), the points with \( T(x) \ge 1/3 \) have denominator \( 1 \), \( 2 \) or \( 3 \). They are \( 0 \), \( 1 \), \( 1/2 \), \( 1/3 \) and \( 2/3 \): only five.

::: {#prp-thomae-large-values}
[Thomae's Function Has Few Large Values]

::: {.enumerate options="label=(\alph*)"}
1. \( 1 \) is a period of \( T \).
2. For all real \( a \le b \) and every \( \varepsilon > 0 \), the set \( E \coloneqq \{ x \in [a, b] : T(x) \ge \varepsilon \} \) is finite.
3. For all \( a < b \), the interval \( (a, b) \) contains points with \( T > 0 \) and points with \( T = 0 \).
:::
:::

::: {.idea}
A large value needs a small denominator: \( T(x) \ge \varepsilon \) forces \( q \le 1/\varepsilon \). There are finitely many such \( q \), and for each \( q \) only finitely many multiples of \( 1/q \) lie in \( [a, b] \). The same point appears under several \( q \) (\( 1/2 = 2/4 \)), so we take a union of finite sets rather than add up counts.
:::

::: {.proof}
(a) For \( x \notin \nQ \), also \( x + 1 \notin \nQ \), and both values are \( 0 \). Let \( x = p/q \) in lowest terms. Then \( x + 1 = (p + q)/q \). A positive common divisor of \( p + q \) and \( q \) divides \( (p + q) - q = p \). It divides \( q \) as well, so it is a common divisor of \( p \) and \( q \) and is at most their greatest common divisor \( \gcd(p, q) = 1 \); hence it equals \( 1 \). So \( \gcd(p + q, q) = 1 \) and \( T(x + 1) = 1/q = T(x) \).

(b) Let \( \varepsilon > 0 \) and \( Q \coloneqq \floor{1/\varepsilon} \) (@def-floor-ceiling). For \( q \in \nZ_{>0} \) let
\[
S_q \coloneqq \{ p/q : p \in \nZ,\ \floor{aq} \le p \le \floor{bq} \} .
\]
*\( E \subseteq S_1 \cup \dots \cup S_Q \).* Let \( x \in E \). Then \( T(x) \ge \varepsilon > 0 \), so \( x \in \nQ \); write \( x = p/q \) in lowest terms. From \( 1/q \ge \varepsilon \) we get \( q \le 1/\varepsilon \), so \( q \le Q \) by @prp-floor-rules (g). From \( a \le p/q \le b \) and \( q > 0 \) we get \( aq \le p \le bq \). Hence \( \floor{aq} \le aq \le p \), and \( p \le \floor{bq} \) by @prp-floor-rules (g). So \( x \in S_q \) with \( 1 \le q \le Q \). (If \( Q = 0 \), no \( q \) qualifies and \( E = \emptyset \).)

*Each \( S_q \) is finite.* If \( \floor{aq} > \floor{bq} \), then \( S_q = \emptyset \). Otherwise let \( m \coloneqq \floor{aq} \) and \( k \coloneqq \floor{bq} - m + 1 \). The map \( \{1, \dots, k\} \to S_q \), \( j \mapsto (m + j - 1)/q \), is onto by the definition of \( S_q \), and injective because \( q \ne 0 \). So \( S_q \) has \( k \) elements (@fd2:def-finite).

*A finite union of finite sets is finite.* Let \( A \) and \( B \) be finite sets. Then \( A \cup B \) is the union of the disjoint sets \( A \) and \( B \setminus A \). The second is finite, as a subset of \( B \). So \( A \cup B \) is finite by @fd2:prp-disjoint-union-count. Induction on the number of sets gives \( S_1 \cup \dots \cup S_Q \) finite.

Hence \( E \), a subset of a finite set, is finite by @fd2:prp-subset-finite.

(c) The interval \( (a, b) \) contains a rational, where \( T > 0 \) (@fd3:thm-rationals-dense-ordered-field). It also contains an irrational, where \( T = 0 \) (@lem-irrationals-dense).

::: {.uses}
@prp-floor-rules (a) (the floor is at most the number); @fd2:prp-subset-finite (subsets of finite sets); @fd2:prp-disjoint-union-count (a disjoint union of finite sets is finite); @fd1:ax-induction (induction).
:::
:::

```{=latex}
\begin{center}
\begin{tikzpicture}[x=7cm, y=3cm]
  \draw[->] (-0.05,0) -- (1.1,0) node[right] {$x$};
  \draw[->] (0,-0.05) -- (0,1.2);
  \foreach \x/\y in {0/1, 1/1, 0.5/0.5, 0.3333/0.3333, 0.6667/0.3333,
                     0.25/0.25, 0.75/0.25, 0.2/0.2, 0.4/0.2, 0.6/0.2, 0.8/0.2,
                     0.1667/0.1667, 0.8333/0.1667}
    \fill (\x,\y) circle (0.9pt);
  \draw[densely dotted] (0,0.01) -- (1,0.01);
  \draw[dashed] (0,0.22) -- (1,0.22) node[right] {$\varepsilon$};
  \node[left] at (0,1) {$1$};
  \node[below] at (1,0) {$1$};
\end{tikzpicture}
\end{center}
```

*Thomae's function on \( [0, 1] \), drawn for the denominators \( q \le 6 \): the dot over \( p/q \) has height \( 1/q \), and the irrational points lie on the dotted axis. Only finitely many dots rise above the dashed level \( \varepsilon \).*

## More strange functions

**An involution.** A function \( f \) with \( f \circ f = \id \) is an **involution**. Exercise C2 of Section 8.2 (@exr-monotone-functions-and-inverses-c2) showed that an *increasing* involution of \( \nR \) is the identity. Here is how far that fails without "increasing".

::: {#exm-strange-involution}
[An Involution That Is Monotone Nowhere]

Let \( J \colon \nR \to \nR \), \( J(x) \coloneqq x \) for \( x \in \nQ \) and \( J(x) \coloneqq -x \) for \( x \notin \nQ \). Show that \( J \circ J = \id_{\nR} \), that \( J \) is a bijection, and that \( J \) is monotone on no interval \( (a, b) \) with \( a < b \).
:::

::: {.solution}
For \( x \in \nQ \), \( J(J(x)) = J(x) = x \). For \( x \notin \nQ \), also \( -x \notin \nQ \), so \( J(J(x)) = J(-x) = -(-x) = x \). So \( J \) is its own two-sided inverse, and it is a bijection by @fd2:thm-bijection-iff-inverse.

Let \( a < b \). By @fd3:thm-rationals-dense-ordered-field, used twice, there are rationals \( q_1 < q_2 \) in \( (a, b) \), and \( J(q_1) = q_1 < q_2 = J(q_2) \), so \( J \) is not decreasing there. By @lem-irrationals-dense, used twice, there are irrationals \( t_1 < t_2 \) in \( (a, b) \), and \( J(t_1) = -t_1 > -t_2 = J(t_2) \), so \( J \) is not increasing there.
:::

The map \( x \mapsto -x \) was already a non-identity involution; \( J \) is one that agrees with the identity on a dense set.

**A jump.** The function \( H \) of @exm-strange-jump, \( H(x) = x \) for \( x < 0 \) and \( H(x) = x + 1 \) for \( x \ge 0 \), is strictly increasing on \( \nR \), yet its image \( (-\infty, 0) \cup [1, \infty) \) skips the whole interval \( [0, 1) \).

**A staircase.** The floor function makes a step function out of a straight line.

::: {#exm-strange-staircase}
[A Staircase Along the Diagonal]

Let \( s \colon [0, 1] \to \nR \), \( s(0) \coloneqq 0 \) and \( s(x) \coloneqq 1/\floor{1/x} \) for \( 0 < x \le 1 \). Describe \( s \) on \( (1/(n + 1), 1/n] \) for \( n \in \nZ_{>0} \).
:::

::: {.solution}
For \( 0 < x \le 1 \) we have \( 1/x \ge 1 \), so \( \floor{1/x} \ge 1 \) by @prp-floor-rules (g), and \( s(x) \) is defined. For \( n \in \nZ_{>0} \),
\[
\floor{1/x} = n \iff n \le 1/x < n + 1 \iff \frac{1}{n + 1} < x \le \frac{1}{n} .
\]
The first equivalence is the definition of the floor. The second takes reciprocals of positive numbers, which reverses inequalities (@fd3:prp-reciprocal-order). So \( s = 1/n \) on \( (1/(n + 1), 1/n] \): a step at height \( 1/n \) whose right end lies on the line \( y = x \).

::: {.uses}
@def-floor-ceiling (the floor).
:::
:::

```{=latex}
\begin{center}
\begin{tikzpicture}[x=6cm, y=6cm]
  \draw[->] (-0.05,0) -- (1.1,0) node[right] {$x$};
  \draw[->] (0,-0.05) -- (0,1.1);
  \draw[dashed] (0,0) -- (1,1) node[above right] {$y = x$};
  \foreach \n in {1,...,7} {
    \pgfmathsetmacro{\stlo}{1/(\n+1)}
    \pgfmathsetmacro{\sthi}{1/\n}
    \draw[thick] (\stlo,\sthi) -- (\sthi,\sthi);
    \draw (\stlo,\sthi) circle (0.9pt);
    \fill (\sthi,\sthi) circle (0.9pt);
  }
  \fill (0,0) circle (0.9pt);
  \node[below] at (1,0) {$1$};
  \node[left] at (0,1) {$1$};
\end{tikzpicture}
\end{center}
```

*The staircase \( s \) and the line \( y = x \) (dashed), drawn for \( n \le 7 \): each step starts just above the line and ends on it.*

::: {#prp-staircase-squeeze}
[The Staircase Hugs the Diagonal]

::: {.enumerate options="label=(\alph*)"}
1. \( s \) is increasing on \( [0, 1] \).
2. \( s \) takes infinitely many values.
3. For \( 0 < x \le 1 \), \( 0 \le s(x) - x < 2x^2 \). (At \( x = 0 \) the left side is \( 0 \) and so is the right, so the strict inequality fails there.)
:::
:::

::: {.proof}
(a) Let \( 0 < x < y \le 1 \). Taking reciprocals reverses the inequality, so \( 1/y < 1/x \) (@fd3:prp-reciprocal-order). Then \( \floor{1/y} \le \floor{1/x} \) by @prp-floor-rules (c). Both are at least \( 1 \), so taking reciprocals again gives \( s(x) = 1/\floor{1/x} \le 1/\floor{1/y} = s(y) \). For \( x = 0 < y \), \( s(0) = 0 < s(y) \).

(b) For \( n \in \nZ_{>0} \), \( s(1/n) = 1/\floor{n} = 1/n \) (@prp-floor-rules (a)). Suppose \( s \) took finitely many values. The set \( V \coloneqq \{ 1/n : n \in \nZ_{>0} \} \) consists of some of them, so it would be finite (@fd2:prp-subset-finite). It is non-empty, so it would have a minimum \( 1/N \) (@fd2:prp-finite-max). But \( 1/(N + 1) \in V \) and \( 1/(N + 1) < 1/N \).

(c) Let \( 0 < x \le 1 \) and \( n \coloneqq \floor{1/x} \ge 1 \). By the solution of @exm-strange-staircase, \( 1/(n + 1) < x \le 1/n \), so \( s(x) - x = 1/n - x \ge 0 \), and
\[
\frac{1}{n} - x < \frac{1}{n} - \frac{1}{n + 1} = \frac{1}{n(n + 1)} \le \frac{2}{(n + 1)^2} < 2x^2 .
\]
The middle inequality is \( n + 1 \le 2n \), true for \( n \ge 1 \). The last holds because \( x > 1/(n + 1) > 0 \) gives \( x^2 > 1/(n + 1)^2 \) (@lem-reals-nth-root (a) with exponent \( 2 \)).
:::

So near \( 0 \), \( s(x) \) agrees with \( x \) up to an error below \( 2x^2 \), although \( s \) is constant on each step.

::: {.check}
Is \( s \) a step function on \( [0, 1] \) (@def-step-function)?
:::

::: {.solution}
No. A step function with a partition into \( n \) open pieces takes at most \( 2n + 1 \) values: one on each piece and one at each of the \( n + 1 \) partition points. By @prp-staircase-squeeze (b), \( s \) takes infinitely many values.
:::

**A zigzag.** Replace the floor by the distance to the nearest integer, and the steps become tents.

::: {#exm-strange-zigzag}
[A Zigzag That Never Settles]

Let \( Z \colon \nR \to \nR \), \( Z(0) \coloneqq 0 \) and \( Z(x) \coloneqq \dist(1/x, \nZ) \) for \( x \ne 0 \) (@def-distance-to-integer). Describe \( Z \) on \( [1/(n + 1), 1/n] \) for \( n \in \nZ_{>0} \).
:::

::: {.solution}
For \( x \) in that interval, \( 1/x \in [n, n + 1] \), and
\[
Z(x) = \min\{ 1/x - n,\ n + 1 - 1/x \} :
\]
for \( 1/x < n + 1 \) this is @prp-distance-to-integer (a) with \( \floor{1/x} = n \), and at \( x = 1/(n + 1) \) both sides are \( 0 \). So \( Z = 0 \) at both ends, \( Z = 1/2 \) at \( x = 2/(2n + 1) \), where \( 1/x = n + 1/2 \), and in between \( Z \) climbs from \( 0 \) to \( 1/2 \) and falls back. Each interval \( [1/(n + 1), 1/n] \) carries one full tent, and the tents crowd toward \( 0 \).
:::

```{=latex}
\begin{center}
\begin{tikzpicture}[x=7cm, y=4cm]
  \draw[->] (0,0) -- (1.1,0) node[right] {$x$};
  \draw[->] (0,-0.05) -- (0,0.7);
  \foreach \n in {1,...,5} {
    \pgfmathsetmacro{\zlo}{1/(\n+1)}
    \pgfmathsetmacro{\zmid}{2/(2*\n+1)}
    \pgfmathsetmacro{\zhi}{1/\n}
    \draw[thick, domain=\zlo:\zmid, samples=30, smooth] plot (\x, {\n + 1 - 1/\x});
    \draw[thick, domain=\zmid:\zhi, samples=30, smooth] plot (\x, {1/\x - \n});
  }
  \draw[densely dotted] (0,0.5) -- (1,0.5);
  \node[left] at (0,0.5) {$\tfrac12$};
  \node[below] at (1,0) {$1$};
  \node[below] at (0.1667,0) {$\tfrac16$};
\end{tikzpicture}
\end{center}
```

*The zigzag \( Z \) on \( [1/6, 1] \): five tents, each rising from \( 0 \) to \( 1/2 \) and back, narrower as they approach \( 0 \).*

::: {#prp-zigzag-all-values}
[The Zigzag Takes Every Value Near 0]

::: {.enumerate options="label=(\alph*)"}
1. For every \( \delta > 0 \) and every \( t \in [0, 1/2] \) there is \( x \in (0, \delta) \) with \( Z(x) = t \).
2. For every \( x \in \nR \), \( \abs{x Z(x)} \le \abs{x}/2 \).
:::
:::

::: {.proof}
(a) Let \( \delta > 0 \) and \( t \in [0, 1/2] \). By @fd3:prp-archimedean-reciprocal there is \( n \in \nZ_{>0} \) with \( 1/n < \delta \). Put \( x \coloneqq 1/(n + t) \). Since \( n + t \ge n > 0 \), we have \( 0 < x \le 1/n < \delta \) (@fd3:prp-reciprocal-order). Since \( \dist(\cdot, \nZ) \) has period \( 1 \) (@prp-distance-to-integer (c)), induction on \( n \) gives \( Z(x) = \dist(n + t, \nZ) = \dist(t, \nZ) \). Finally \( \floor{t} = 0 \), as \( 0 \le t < 1 \), so by @prp-distance-to-integer (a), \( \dist(t, \nZ) = \min\{ t, 1 - t \} = t \), because \( t \le 1/2 \le 1 - t \).

(b) For \( x = 0 \) both sides are \( 0 \). For \( x \ne 0 \), \( \abs{x Z(x)} = \abs{x} \dist(1/x, \nZ) \le \abs{x}/2 \) by @prp-distance-to-integer (b).
:::

So on every interval \( (0, \delta) \) the zigzag sweeps through all of \( [0, 1/2] \), while \( x Z(x) \) is pressed between \( -\abs{x}/2 \) and \( \abs{x}/2 \).

**Two functions on a closed interval.** The last two are defined at every point of \( [0, 1] \) and still misbehave.

::: {#exm-strange-unbounded}
[Unbounded on a Closed Interval]

Let \( R \colon [0, 1] \to \nR \), \( R(0) \coloneqq 0 \) and \( R(x) \coloneqq 1/x \) for \( 0 < x \le 1 \). Show that \( R \) is not bounded above on \( [0, 1] \) (@def-bounded-function).
:::

::: {.solution}
Let \( C \in \nR \), and put \( C' \coloneqq \max\{C, 0\} + 1 \ge 1 \) and \( x \coloneqq 1/C' \in (0, 1] \). Then \( R(x) = C' > C \). So no \( C \) is an upper bound of \( R([0, 1]) \).
:::

::: {#exm-strange-sup-missed}
[A Supremum Never Reached]

Let \( M \colon [0, 1] \to \nR \), \( M(x) \coloneqq x \) for \( 0 \le x < 1 \) and \( M(1) \coloneqq 0 \). Show that \( \sup_{[0, 1]} M = 1 \) and that it is not attained.
:::

::: {.solution}
Every value is at most \( 1 \): it is \( x < 1 \) or it is \( 0 \). For \( \varepsilon > 0 \), put \( x \coloneqq \max\{0, 1 - \varepsilon/2\} \in [0, 1) \); then \( M(x) = x \ge 1 - \varepsilon/2 > 1 - \varepsilon \). By @prp-real-sup-approximation, \( \sup_{[0, 1]} M = 1 \). Every value is in fact **strictly** below \( 1 \), so the supremum is not attained.
:::

Both \( R \) and \( M \) are defined everywhere on the closed bounded interval \( [0, 1] \). The table below asks which further hypothesis would rule out both behaviors.

## The table

::: {#exm-strange-functions}
[A Table of Strange Functions]

Each row names a function, recalls its definition, lists what has been proved about it, and asks what the later volumes will answer.

| function | definition | proved here | question for later |
|---|---|---|---|
| \( D \) (@def-dirichlet-function) | \( 1 \) on \( \nQ \), \( 0 \) off \( \nQ \) | periods exactly the non-zero rationals; on every interval sup \( 1 \), inf \( 0 \), monotone nowhere | continuous at any point? integrable on \( [0, 1] \)? |
| \( x D(x) \) | \( x \) on \( \nQ \), \( 0 \) off \( \nQ \) | at most \( \abs{x} \) in size; near each \( a \ne 0 \), points where it differs from its value at \( a \) by at least \( \abs{a}/2 \) | continuous exactly where? |
| \( T \) (@def-thomae-function) | \( 1/q \) at \( p/q \) in lowest terms, \( 0 \) off \( \nQ \) | period \( 1 \); finitely many points of \( [a, b] \) where \( T \ge \varepsilon \); positive and zero points in every interval | continuous exactly where? integrable on \( [0, 1] \)? |
| \( J \) (@exm-strange-involution) | \( x \) on \( \nQ \), \( -x \) off \( \nQ \) | \( J \circ J = \id \); a bijection; monotone on no interval | continuous at any point? |
| \( H \) (@exm-strange-jump) | \( x \) for \( x < 0 \), \( x + 1 \) for \( x \ge 0 \) | strictly increasing; image skips \( [0, 1) \) | which property forces the image of an interval to be an interval? |
| \( s \) (@exm-strange-staircase) | \( 1/\floor{1/x} \) on \( (0, 1] \), \( 0 \) at \( 0 \) | increasing; infinitely many values; \( 0 \le s(x) - x < 2x^2 \) for \( 0 < x \le 1 \) | continuous at \( 0 \)? differentiable at \( 0 \)? integrable? |
| \( Z \), \( x Z(x) \) (@exm-strange-zigzag) | \( \dist(1/x, \nZ) \) for \( x \ne 0 \), \( 0 \) at \( 0 \) | \( Z \) takes every value of \( [0, 1/2] \) on every \( (0, \delta) \); \( \abs{x Z(x)} \le \abs{x}/2 \) | \( Z \) continuous at \( 0 \)? \( x Z(x) \) continuous at \( 0 \)? differentiable there? |
| \( R \) (@exm-strange-unbounded) | \( 1/x \) on \( (0, 1] \), \( 0 \) at \( 0 \) | not bounded above on \( [0, 1] \) | which hypothesis on a function on \( [a, b] \) forces it to be bounded? |
| \( M \) (@exm-strange-sup-missed) | \( x \) on \( [0, 1) \), \( 0 \) at \( 1 \) | sup \( 1 \), not attained | which hypothesis forces the sup to be attained? |
:::

::: {.remark}
[Looking ahead]

The analysis volumes answer these questions. *Real Numbers, Metric Spaces, and Derivatives* settles the continuity and extreme-value questions once it has continuous functions. *Integration, Series, and Function Spaces* settles the integrability questions once it has the integral, and once it has the sine, it replaces \( \dist(1/x, \nZ) \) in the zigzag by the sine. No proof in the main text of this section uses a limit, continuity or a derivative.
:::

## Exercises

### A. Check your understanding

::: {#exr-strange-functions-a1}
[A1]

Find the supremum and infimum of \( D \) on \( (0, 1) \) and of \( T \) on \( [0, 1] \). Which of them are attained, and where?
:::

::: {.solution}
For \( D \) on \( (0, 1) \): supremum \( 1 \), infimum \( 0 \), both attained (@prp-dirichlet-properties (b)), for example at \( 1/2 \) and at the irrational \( \sqrt 2/2 \) (irrational by the Quick check after @def-thomae-function, and \( (\sqrt 2/2)^2 = 1/2 < 1 \) gives \( \sqrt 2/2 < 1 \), and it is positive).

For \( T \) on \( [0, 1] \): every value is at most \( 1 \), since \( q \ge 1 \), and \( T(0) = T(0/1) = 1 \), \( T(1) = T(1/1) = 1 \); so the supremum is \( 1 \), attained at \( 0 \) and \( 1 \). Every value is at least \( 0 \), and \( T(\sqrt 2/2) = 0 \); so the infimum is \( 0 \), attained at every irrational point of \( [0, 1] \).
:::

::: {#exr-strange-functions-a2}
[A2]

Let \( g(x) \coloneqq x D(x) \).

::: {.enumerate options="label=(\alph*)"}
1. Is \( g \) bounded on \( [-5, 5] \)?
2. Is \( g \) monotone on \( (0, 1) \)?
:::
:::

::: {.solution}
(a) Yes: \( \abs{g(x)} \le \abs{x} \le 5 \) for \( x \in [-5, 5] \).

(b) No. The points \( 1/2 < \sqrt 2/2 < 3/4 \) lie in \( (0, 1) \): squaring, \( 1/4 < 1/2 < 9/16 \), and squaring is strictly increasing on \( [0, \infty) \) (@lem-reals-nth-root (a)). The values are \( g(1/2) = 1/2 \), \( g(\sqrt 2/2) = 0 \), \( g(3/4) = 3/4 \). The first pair shows \( g \) is not increasing on \( (0, 1) \), the second that it is not decreasing.
:::

### B. Practice

::: {#exr-strange-functions-b1}
[B1]

Find all \( x \in [0, 1] \) with \( T(x) \ge 1/4 \).
:::

::: {.solution}
\( T(x) \ge 1/4 \) forces \( x \) rational, \( x = p/q \) in lowest terms with \( q \le 4 \) and \( 0 \le p \le q \). Listing \( q = 1, 2, 3, 4 \) and keeping the pairs with \( \gcd(p, q) = 1 \):
\[
0,\ 1,\ \tfrac12,\ \tfrac13,\ \tfrac23,\ \tfrac14,\ \tfrac34 .
\]
Seven points; \( 2/4 \) is not new, since it is \( 1/2 \), with value \( 1/2 \).
:::

::: {#exr-strange-functions-b2}
[B2: Prove or disprove]

::: {.enumerate options="label=(\alph*)"}
1. \( D(x) + D(x + \sqrt 2) \le 1 \) for every \( x \in \nR \).
2. The restriction of \( J \) to \( \nQ \) is increasing.
3. Every bijection \( \nR \to \nR \) is monotone on some interval \( (a, b) \) with \( a < b \).
4. \( T(x + 1) = T(x) \) for every \( x \in \nR \).
:::
:::

::: {.solution}
(a) True. If \( x \) and \( x + \sqrt 2 \) were both rational, so would be their difference \( \sqrt 2 \), which is irrational, as shown in Section 8.3. So at most one of the two values is \( 1 \).

(b) True. On \( \nQ \), \( J \) is the identity, and \( q_1 < q_2 \) gives \( J(q_1) = q_1 < q_2 = J(q_2) \).

(c) False. \( J \) is a bijection that is monotone on no such interval (@exm-strange-involution).

(d) True. This is @prp-thomae-large-values (a).
:::

::: {#exr-strange-functions-b3}
[B3]

Compute \( s(0.4) \), and check the inequality of @prp-staircase-squeeze (c) at \( x = 0.4 \).
:::

::: {.solution}
\( 1/0.4 = 2.5 \) and \( \floor{2.5} = 2 \), so \( s(0.4) = 1/2 \). Then \( s(0.4) - 0.4 = 0.1 \), and \( 2 \cdot 0.4^2 = 0.32 \). Indeed \( 0 \le 0.1 < 0.32 \).
:::

### C. Going deeper

::: {#exr-strange-functions-c1}
[C1: Additive and increasing]

Let \( f \colon \nR \to \nR \) satisfy \( f(x + y) = f(x) + f(y) \) for all \( x, y \), and let \( f \) be increasing. Prove that \( f(x) = cx \) for every \( x \in \nR \), where \( c \coloneqq f(1) \).
:::

::: {.solution}
[Hint 1]

Exercise C1 of Section 8.1 gives \( f \) on \( \nQ \). Trap \( x \) between rationals.
:::

::: {.solution}
[Hint 2]

Suppose \( c > 0 \) and \( f(x) > cx \) for some \( x \). Where can a rational \( q \) sit so that monotonicity and \( f(q) = cq \) collide?
:::

::: {.solution}
By @exr-real-functions-and-graphs-c1 (a) and (c), \( f(0) = 0 \) and \( f(q) = cq \) for every \( q \in \nQ \). Since \( f \) is increasing and \( 0 < 1 \), \( c = f(1) \ge f(0) = 0 \). Fix \( x \in \nR \).

*Case \( c > 0 \).* Suppose \( f(x) > cx \). Then \( x < f(x)/c \), and @fd3:thm-rationals-dense-ordered-field gives \( q \in \nQ \) with \( x < q < f(x)/c \). Then \( f(q) = cq < f(x) \), although \( x < q \) and \( f \) is increasing, so \( f(x) \le f(q) \): a contradiction. Suppose \( f(x) < cx \). Then \( f(x)/c < x \), and a rational \( q \) with \( f(x)/c < q < x \) gives \( f(q) = cq > f(x) \), against \( f(q) \le f(x) \). So \( f(x) = cx \).

*Case \( c = 0 \).* Take rationals \( p < x < q \) (@fd3:thm-rationals-dense-ordered-field, in \( (x - 1, x) \) and \( (x, x + 1) \)). Then \( 0 = f(p) \le f(x) \le f(q) = 0 \), so \( f(x) = 0 = cx \).

Without "increasing", additivity alone does not force \( f(x) = cx \) in general. But an additive function that is not of this form cannot be written down without the axiom of choice. This series builds no such function, and it does not prove that none can be written down without choice.

**What a complete answer needs.** (10 points)
- 2: obtains \( f(q) = cq \) on \( \nQ \) and \( c \ge 0 \), each with its reason.
- 4: for \( c > 0 \), refutes \( f(x) > cx \) with a rational between \( x \) and \( f(x)/c \), using monotonicity in the right direction.
- 2: the symmetric case \( f(x) < cx \).
- 2: the case \( c = 0 \).
Another correct route earns the same points: a two-sided squeeze with rationals \( p < x < q \) closer than \( 1/n \), then Archimedes (2 for \( f = cq \) on \( \nQ \) and \( c \ge 0 \), 4 for \( cp \le f(x) \le cq \), 4 for closing the gap).
Slips that lose the step: dividing by \( c \) without \( c > 0 \); assuming \( f \) continuous or taking a limit of rationals.
:::

::: {#exr-strange-functions-c2}
[C2]

Let \( a < b \) and let \( f \colon [a, b] \to \nR \) be increasing. Prove that \( f \) is bounded and attains its supremum and its infimum on \( [a, b] \). Why does @exm-strange-sup-missed not contradict this?
:::

::: {.solution}
For \( x \in [a, b] \), \( a \le x \le b \), so \( f(a) \le f(x) \le f(b) \) because \( f \) is increasing. So \( f \) is bounded, \( f(b) \) is an upper bound of \( f([a, b]) \) that is itself a value, hence \( \sup_{[a, b]} f = f(b) \) is attained; likewise \( \inf_{[a, b]} f = f(a) \).

The function \( M \) is not increasing on \( [0, 1] \): \( 1/2 < 1 \) but \( M(1/2) = 1/2 > 0 = M(1) \). Its supremum fails to be attained exactly because the value at the right end drops.
:::

### R. Review

::: {#exr-strange-functions-r1}
[R1]

Let \( p \in \nR[x] \), and suppose its polynomial function satisfies \( p(x + 1) = p(x) \) for every \( x \in \nR \). Prove that \( p \) is a constant polynomial.
:::

::: {.solution}
Let \( c \coloneqq p(0) \) and \( r \coloneqq p - c \in \nR[x] \). Evaluation respects differences (@prp-polynomial-function-map (b)), so \( r(x) = p(x) - c \). By induction on \( n \in \nN \), \( r(n) = 0 \): \( r(0) = p(0) - c = 0 \), and \( r(n + 1) = p(n + 1) - c = p(n) - c = r(n) \).

Suppose \( r \ne 0 \), of degree \( d \). Then \( 0, 1, \dots, d \) are \( d + 1 \) distinct roots of \( r \), against @thm-polynomial-root-count, which allows at most \( d \). So \( r = 0 \), and \( p = c \) is constant.
:::

::: {#exr-strange-functions-r2}
[R2]

Prove that the strictly increasing bijections \( \nR \to \nR \) form a subgroup of the group of all bijections \( \nR \to \nR \) under composition. Do the strictly decreasing bijections form one?
:::

::: {.solution}
The bijections of \( \nR \) form a group under \( \circ \) (@exm-groups (c)). Let \( G \) be the set of strictly increasing bijections. We use @thm-subgroup-test.

\( G \ne \emptyset \), since \( \id_{\nR} \in G \). Let \( f, g \in G \). Since \( g \) is strictly increasing and onto, @thm-monotone-inverse (b) gives that \( g^{-1} \colon g(\nR) = \nR \to \nR \) is strictly increasing. It is a bijection by @fd2:thm-bijection-iff-inverse. Then \( f \circ g^{-1} \) is strictly increasing by @prp-monotone-algebra (e). It is bijective by @fd2:thm-composition-injective-surjective (c). So \( f \circ g^{-1} \in G \), and \( G \) is a subgroup.

The strictly decreasing bijections do not form a subgroup. A subgroup contains the identity, and \( \id_{\nR} \) is not strictly decreasing (\( 0 < 1 \), \( \id(0) < \id(1) \)). They are not even closed under composition: \( x \mapsto -x \) composed with itself is \( \id_{\nR} \).
:::

::: {#exr-strange-functions-r3}
[R3]

Let \( x \in \nR \), and let \( a_0 \coloneqq 0 \) and \( a_n \coloneqq \floor{nx}/n \) for \( n \ge 1 \). Prove that \( a_n \to x \).
:::

::: {.solution}
For \( n \ge 1 \), @prp-floor-rules (a) gives \( nx - 1 < \floor{nx} \le nx \); dividing by \( n > 0 \), \( 0 \le x - a_n < 1/n \). Let \( \varepsilon > 0 \). By @fd3:prp-archimedean-reciprocal there is \( N \in \nZ_{>0} \), depending on \( \varepsilon \), with \( 1/n < \varepsilon \) for every \( n \ge N \). For such \( n \), \( n \ge 1 \) and \( \abs{a_n - x} < 1/n < \varepsilon \). So \( a_n \to x \) by @fd3:def-sequence-limit-ordered-field.
:::

::: {#exr-strange-functions-r4}
[R4]

Is there a polynomial \( p \in \nR[x] \) whose polynomial function is \( x \mapsto \abs{x} \) on \( \nR \)?
:::

::: {.solution}
No. Suppose there were. Then \( p \ne 0 \), since \( p(1) = 1 \). Let \( d \coloneqq \max\{\deg p, 1\} \). The polynomials \( p \) and \( x \) both have degree at most \( d \) and agree at the \( d + 1 \) distinct points \( 0, 1, \dots, d \), where \( \abs{x} = x \). By @thm-polynomial-identity-from-values (a), \( p = x \). Then \( p(-1) = -1 \ne 1 = \abs{-1} \), a contradiction.

The tool is that a polynomial is fixed by finitely many values. Two look-alikes fail. Comparing growth gives nothing: \( \abs{x} \) grows like a polynomial of degree \( 1 \). "Since \( \abs{x} \) is even, \( p \) has only even powers" needs the same identity principle to compare \( p(x) \) with \( p(-x) \), and then still needs an argument.
:::

<!-- dependency ledger
lem-irrationals-dense (proof): Q is identified with its copy in R (q written for kappa(q)) | fd3 ch05 §04 identification remark (NOTATION row for \nQ, \nR)
lem-irrationals-dense (proof): sqrt 2 is irrational; Q closed under differences | recalled from 8.3 (Quick check 3 solution, fd3:thm-no-rational-square-two with fd3:thm-rationals-embed-ordered-field); Q is a field (fd3 ch03)
prp-dirichlet-properties (proof): Q is closed under sums and negatives | Q is a field (fd3 ch03)
prp-dirichlet-properties (proof): an upper bound of a set that lies in the set is its supremum (and max) | @fd2:def-order-supremum, Uses line
prp-thomae-large-values (proof): a common divisor of p + q and q divides p | inline (Ch2 divisibility)
prp-thomae-large-values (proof): j -> (m + j - 1)/q is a bijection {1..k} -> S_q | inline
prp-thomae-large-values (proof): q <= 1/eps with q integer gives q <= floor(1/eps) | @prp-floor-rules (g)
prp-zigzag-all-values (proof): period 1 gives dist(n + t, Z) = dist(t, Z) for n in N | inline induction (@fd1:ax-induction)
exm-strange-involution (solution): x irrational implies -x irrational | Q closed under negatives (fd3 ch03)
exr-strange-functions-c1 (solution): f(0) = 0 and f(q) = cq on Q | @exr-real-functions-and-graphs-c1 (an exercise, cited in a solution only)
exr-strange-functions-c2 (solution): an upper bound of a set that lies in the set is its supremum | @fd2:def-order-supremum, inline
exr-strange-functions-r1 (solution): induction on n | @fd1:ax-induction
exr-strange-functions-a1 (solution): sqrt(2)/2 is irrational | Quick check after @def-thomae-function, from sqrt 2 irrational (8.3)
exr-strange-functions-a2 (solution): sqrt(2)/2 is irrational | Quick check after @def-thomae-function, from sqrt 2 irrational (8.3)
-->
