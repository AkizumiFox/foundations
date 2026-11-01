# Floor, Distance to the Integers, and Step Functions

*Number Systems: From \(\nN\) to \(\nR\)* gave every element of an Archimedean field an integer part (@fd3:prp-integer-part-ordered-field). Here the integer part becomes a function on all of \( \nR \), one that jumps at every integer. From it we build the distance to the nearest integer and the step functions. Section 8.6 builds its strange functions from these pieces.

## The floor and the ceiling

Nobody needs a definition to round \( 3.7 \) down to \( 3 \). The integer \( 3 \) is the one with \( 3 \le 3.7 < 3 + 1 \). Rounding up gives \( 4 \), and the part left over, \( 3.7 - 3 = 0.7 \), lies between \( 0 \) and \( 1 \).

For a number such as \( \sqrt 2 + \sqrt 3 \), with no decimal expansion handed to us, we need to know that the answer exists and is unique. Both facts are already proved:

- \( \nR \) is a complete ordered field (@fd3:thm-reals-complete-ordered-field);
- a complete ordered field is Archimedean (@fd3:thm-cof-complete-archimedean);
- in an Archimedean field every element lies in exactly one interval \( [m, m + 1) \) with \( m \in \nZ \) (@fd3:prp-integer-part-ordered-field).

Throughout, integers are read inside \( \nR \), as in *Number Systems*. The embedding \( \iota_{\nR} \) respects sums, products and order and reflects order (@fd3:thm-rationals-embed-ordered-field). So a sum, product or comparison of integers means the same in \( \nZ \) and in \( \nR \).

*The floor of \( x \) is the integer you reach by stepping down from \( x \) to the nearest integer at or below it.*

::: {#def-floor-ceiling}
[Floor, Ceiling, Fractional Part]

Let \( x \in \nR \). The **floor** of \( x \), written \( \floor{x} \), is **the** unique \( m \in \nZ \) with
\[
m \le x < m + 1 .
\]
The **ceiling** of \( x \) is \( \ceil{x} \coloneqq -\floor{-x} \). The number \( x - \floor{x} \) is the **fractional part** of \( x \); it lies in \( [0, 1) \).
:::

Existence and uniqueness are @fd3:prp-integer-part-ordered-field for \( F = \nR \). So \( x \mapsto \floor{x} \) is a function \( \nR \to \nR \) with values in \( \nZ \), a real function in the sense of @def-real-function. The fractional part lies in \( [0, 1) \) because subtracting \( \floor{x} \) from \( m \le x < m + 1 \) gives \( 0 \le x - \floor{x} < 1 \). For a rational \( x \) the floor is the integer part of @fd3:prp-rational-integer-part. *Sets and Functions* used the floor map as a school fact (@fd2:exm-maps-from-calculus (b)). Now it rests on a proof.

**Examples.** \( \floor{3.7} = 3 \), since \( 3 \le 3.7 < 4 \). \( \floor{5} = 5 \), since \( 5 \le 5 < 6 \): at an integer the floor is the integer itself. \( \floor{-0.2} = -1 \), since \( -1 \le -0.2 < 0 \). \( \ceil{3.7} = -\floor{-3.7} = -(-4) = 4 \).

The graph of the floor is a staircase: on each \( [m, m + 1) \) a horizontal segment at height \( m \), with a filled dot at its left end and a hollow dot at its right end.

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.8]
  \draw[->] (-2.6,0) -- (3.6,0) node[right] {$x$};
  \draw[->] (0,-2.6) -- (0,2.6) node[above] {$y$};
  \foreach \m in {-2,-1,0,1,2} {
    \draw[thick] (\m,\m) -- (\m+0.93,\m);
    \fill (\m,\m) circle (2pt);
    \draw (\m+1,\m) circle (2pt);
  }
  \foreach \t in {-2,-1,1,2,3} \draw (\t,0.08) -- (\t,-0.08) node[below] {\scriptsize $\t$};
  \draw[dashed] (-2.5,-2.5) -- (2.5,2.5);
\end{tikzpicture}
\end{center}
```

The figure shows the graph of \( \floor{x} \) on \( [-2, 3) \), with the dashed line \( y = x \): the staircase never rises above the line and never falls a full unit below it, which is rule (a) below.

::: {.warning}
The floor is not "drop the decimals". For \( x = -2.5 \), dropping the decimals gives \( -2 \), but \( -2 \le -2.5 \) is false; the integer with \( m \le -2.5 < m + 1 \) is \( m = -3 \). For negative non-integers the floor is one below the truncation.
:::

::: {.check}
Compute \( \floor{-7/2} \), \( \ceil{-7/2} \) and \( \floor{7/2} + \floor{-7/2} \).
:::

::: {.solution}
\( -4 \le -7/2 < -3 \), so \( \floor{-7/2} = -4 \). Next, \( 3 \le 7/2 < 4 \) gives \( \floor{7/2} = 3 \), so \( \ceil{-7/2} = -\floor{7/2} = -3 \). Finally \( \floor{7/2} + \floor{-7/2} = 3 - 4 = -1 \), not \( 0 \): the floor does not commute with negation.
:::

Each of these floors was found the same way: name a candidate integer and verify the two inequalities. That is the whole method for floors.

::: {#exm-method-floor-inequality}
[Method: pin the floor by its inequality]

**How it goes.** To show \( \floor{A} = m \) for a real expression \( A \), use one of two forms.

- *First form.* Check that \( m \) is an integer and that \( m \le A < m + 1 \). Uniqueness in @def-floor-ceiling does the rest.
- *Second form.* Check that \( m \) is an integer and that **every** \( j \in \nZ \) satisfies \( j \le A \iff j \le m \). This form rests on rule (g) of @prp-floor-rules, which turns \( j \le A \) into a statement about \( \floor{A} \).

| We know | We want |
|---|---|
| an expression \( A \); a candidate integer \( m \) | \( m \le A < m + 1 \) (first form), or \( \forall j \in \nZ \colon j \le A \iff j \le m \) (second form) |

**When to use it.** Every identity with a floor on one side. The first form suits a candidate given by a formula; the second suits an \( A \) built from floors and divisions, where each step of the argument is an equivalence.

**Common mistakes.** One mistake is to drop the decimals, as in the warning above. Another is to forget that \( m \) must be an integer. For example, \( x - \tfrac12 \le x < (x - \tfrac12) + 1 \) holds for every real \( x \), yet \( x - \tfrac12 \) is \( \floor{x} \) only when it is an integer.
:::

Here are the rules for the floor that later chapters use. Most of them are one application of the method; rule (g) is discreteness of \( \nZ \).

::: {#prp-floor-rules}
[Rules for the Floor]

Let \( x, y \in \nR \), \( n \in \nZ \) and \( k \in \nZ_{>0} \).

::: {.enumerate options="label=(\alph*)"}
1. \( x - 1 < \floor{x} \le x \), and \( \floor{x} = x \) if and only if \( x \in \nZ \).
2. \( \floor{x + n} = \floor{x} + n \).
3. The floor is increasing: if \( x \le y \), then \( \floor{x} \le \floor{y} \).
4. \( \floor{x} + \floor{y} \le \floor{x + y} \le \floor{x} + \floor{y} + 1 \).
5. \( \floor{-x} = -\floor{x} \) if \( x \in \nZ \), and \( \floor{-x} = -\floor{x} - 1 \) if \( x \notin \nZ \).
6. \( \ceil{x} \) is the unique \( m \in \nZ \) with \( m - 1 < x \le m \).
7. For every \( j \in \nZ \): \( j \le x \iff j \le \floor{x} \).
8. \( \floor{\floor{x}/k} = \floor{x/k} \).
:::
:::

::: {.idea}
Parts (a), (b), (d), (e) and (f) use the first form of @exm-method-floor-inequality: write down the candidate and check two inequalities. Part (g) is discreteness of \( \nZ \): no integer lies strictly between \( \floor{x} \) and \( \floor{x} + 1 \). Part (c) is (g) applied once, and (h) needs a separate argument.
:::

::: {.proof}
Write \( m \coloneqq \floor{x} \), so \( m \in \nZ \) and \( m \le x < m + 1 \).

(a) The inequality \( m \le x \) is half of the definition, and subtracting \( 1 \) from \( x < m + 1 \) gives \( x - 1 < m \). If \( x \in \nZ \), the integer \( x \) satisfies \( x \le x < x + 1 \), so \( \floor{x} = x \) by the first form. Conversely, if \( \floor{x} = x \), then \( x \) is an integer, because \( \floor{x} \) is.

(b) The number \( m + n \) is an integer, and adding \( n \) to \( m \le x < m + 1 \) gives \( m + n \le x + n < (m + n) + 1 \). By the first form, \( \floor{x + n} = m + n \).

(d) Let \( l \coloneqq \floor{y} \), and write \( s \coloneqq x - m \) and \( t \coloneqq y - l \), both in \( [0, 1) \). Then \( x + y = (m + l) + (s + t) \) with \( 0 \le s + t < 2 \). *Case \( s + t < 1 \).* Then \( m + l \le x + y < (m + l) + 1 \), so \( \floor{x + y} = m + l \) by the first form. *Case \( s + t \ge 1 \).* Then \( m + l + 1 \le x + y < (m + l + 1) + 1 \), so \( \floor{x + y} = m + l + 1 \). In both cases \( m + l \le \floor{x + y} \le m + l + 1 \).

(e) If \( x \in \nZ \), then \( -x \in \nZ \), and (a) gives \( \floor{-x} = -x = -\floor{x} \). If \( x \notin \nZ \), then \( m \ne x \) by (a), so \( m < x < m + 1 \). Negating reverses both inequalities (@fd3:prp-ordered-ring-rules (a)): \( -m - 1 < -x < -m \). So the integer \( -m - 1 \) satisfies \( -m - 1 \le -x < (-m - 1) + 1 \), and \( \floor{-x} = -m - 1 \) by the first form.

(f) Let \( k' \coloneqq \floor{-x} \), so \( k' \le -x < k' + 1 \). Negating gives \( -k' - 1 < x \le -k' \), that is, \( \ceil{x} = -k' \) satisfies \( \ceil{x} - 1 < x \le \ceil{x} \). If also \( m' \in \nZ \) satisfies \( m' - 1 < x \le m' \), then negating gives \( -m' \le -x < -m' + 1 \), so \( -m' = \floor{-x} = k' \) by the definition of the floor, and \( m' = \ceil{x} \).

(g) Let \( j \in \nZ \). \( (\Leftarrow) \) If \( j \le m \), then \( j \le m \le x \). \( (\Rightarrow) \) We prove the contrapositive. If \( j \le m \) fails, then \( m < j \), by totality of the order. Discreteness of \( \nZ \) (@fd3:thm-integers-ordered-ring (c)) then gives \( m + 1 \le j \). Then \( x < m + 1 \le j \), so \( j \le x \) fails.

(c) Let \( x \le y \). Then \( \floor{x} \le x \le y \) by (a), and \( \floor{x} \in \nZ \), so (g) for \( y \), with \( j = \floor{x} \), gives \( \floor{x} \le \floor{y} \). Hence the floor is increasing on \( \nR \) (@def-monotone-function).

::: {.uses}
@fd3:prp-ordered-ring-rules (b) (adding to an inequality); @fd3:prp-ordered-field-halves (a) (totality).
:::
:::

Rule (g) justifies the second form of the method. Suppose \( m \in \nZ \) and every \( j \in \nZ \) satisfies \( j \le A \iff j \le m \). By (g), every \( j \in \nZ \) then satisfies \( j \le \floor{A} \iff j \le m \). The choice \( j = m \) gives \( m \le \floor{A} \), and the choice \( j = \floor{A} \) gives \( \floor{A} \le m \). So \( m = \floor{A} \).

Part (h) is the rule behind dividing in stages: \( \floor{\floor{17/3}/2} = \floor{5/2} = 2 = \floor{17/6} \).

::: {.idea}
[Scratch work]

Start with the first form, candidate \( m \coloneqq \floor{x/k} \).

| We know | We want |
|---|---|
| \( x \in \nR \), \( k \in \nZ_{>0} \); \( m \le x/k < m + 1 \) | \( m \le \floor{x}/k < m + 1 \) |
| \( \floor{x} \le x \), \( k > 0 \) | upper half: \( \floor{x}/k \le x/k < m + 1 \); done |
| \( m \le x/k \), that is, \( mk \le x \) | lower half: \( mk \le \floor{x} \) |
| \( mk \in \nZ \) | rule (g) turns \( mk \le x \) into \( mk \le \floor{x} \) |

Both halves go through. But the lower half is just rule (g) again, and every step is an equivalence. The second form writes it as one chain, with no candidate to guess.
:::

::: {.proof}
(h) Let \( j \in \nZ \). Multiplying by \( k > 0 \) and by \( 1/k > 0 \) preserves \( \le \), and \( jk \in \nZ \). Hence
\[
\begin{aligned}
j \le \frac{\floor{x}}{k}
&\iff jk \le \floor{x}
\iff jk \le x \\
&\iff j \le \frac{x}{k}
\iff j \le \floor{x/k} ,
\end{aligned}
\]
where the second and the last equivalence are (g), applied to \( x \) with the integer \( jk \) and to \( x/k \) with \( j \). So the integer \( \floor{x/k} \) satisfies the second form for \( A = \floor{x}/k \), and \( \floor{\floor{x}/k} = \floor{x/k} \).

::: {.uses}
@fd3:prp-ordered-ring-rules (c) (multiplying by a positive); @fd3:prp-reciprocal-order (a) (\( 1/k > 0 \)).
:::
:::

Applied to \( x/k \) and \( l \in \nZ_{>0} \), it gives \( \floor{\floor{x/k}/l} = \floor{x/(kl)} \).

::: {.check}
Compute \( \floor{\floor{7.5}/2} \) and \( \floor{7.5/2} \).
:::

::: {.solution}
\( \floor{7.5} = 7 \), and \( \floor{7/2} = 3 \) since \( 3 \le 3.5 < 4 \). On the other side \( 7.5/2 = 3.75 \) and \( \floor{3.75} = 3 \). The two agree, as (h) says with \( k = 2 \).
:::

## Distance to the nearest integer

The fractional part \( x - \floor{x} \) measures how far \( x \) sits above the integer below it. Often we want the distance to **any** integer: \( 0.9 \) is far above \( 0 \) but close to \( 1 \). That is a distance to a set, so we define it as an infimum and then show that it is attained.

*The distance from \( x \) to \( \nZ \) is how far \( x \) must move to land on an integer.*

::: {#def-distance-to-integer}
[Distance to the Integers]

For \( x \in \nR \), the **distance from \( x \) to \( \nZ \)** is
\[
\dist(x, \nZ) \coloneqq \inf \{ \abs{x - n} : n \in \nZ \} .
\]
:::

The set is non-empty (take \( n = 0 \)) and bounded below by \( 0 \), so the infimum exists (@prp-real-infimum).

::: {#prp-distance-to-integer}
[Distance to the Integers]

Let \( x, y \in \nR \), \( m \coloneqq \floor{x} \) and \( t \coloneqq x - m \).

::: {.enumerate options="label=(\alph*)"}
1. \( \dist(x, \nZ) = \min\{ t, 1 - t \} \), and it is a minimum: \( \dist(x, \nZ) = \abs{x - n} \) for \( n = m \) or \( n = m + 1 \), and \( \abs{x - n} \ge \dist(x, \nZ) \) for every \( n \in \nZ \).
2. \( 0 \le \dist(x, \nZ) \le \tfrac12 \); \( \dist(x, \nZ) = 0 \) if and only if \( x \in \nZ \); \( \dist(x, \nZ) = \tfrac12 \) if and only if \( x - \tfrac12 \in \nZ \).
3. \( \dist(x + 1, \nZ) = \dist(x, \nZ) \) and \( \dist(-x, \nZ) = \dist(x, \nZ) \).
4. \( \dist(x, \nZ) \le \abs{x} \); \( \dist(x + y, \nZ) \le \dist(x, \nZ) + \dist(y, \nZ) \); and \( \abs{\dist(x, \nZ) - \dist(y, \nZ)} \le \abs{x - y} \).
:::
:::

::: {.idea}
Every integer is at most \( m \) or at least \( m + 1 \), so the nearest integer is \( m \) or \( m + 1 \), at distance \( t \) or \( 1 - t \). Parts (b)–(d) follow, using a nearest integer as a witness.
:::

::: {.proof}
(a) We have \( 0 \le t < 1 \). Let \( n \in \nZ \). If \( n \le m \), then \( n \le m \le x \), so \( \abs{x - n} = x - n \ge x - m = t \). Otherwise \( m < n \), so \( m + 1 \le n \) by discreteness (@fd3:thm-integers-ordered-ring (c)), and \( n > x \), so \( \abs{x - n} = n - x \ge m + 1 - x = 1 - t \). In both cases \( \abs{x - n} \ge \min\{t, 1 - t\} \). The value \( \min\{t, 1 - t\} \) is itself in the set: \( \abs{x - m} = t \) and \( \abs{x - (m + 1)} = 1 - t \). A lower bound of a set that belongs to the set is its infimum, and its minimum.

(b) By (a), \( \dist(x, \nZ) \ge 0 \). The two numbers \( t \) and \( 1 - t \) add up to \( 1 \), so the smaller is at most \( \tfrac12 \). Since \( 1 - t > 0 \), the minimum is \( 0 \) exactly when \( t = 0 \), that is, when \( \floor{x} = x \), that is, when \( x \in \nZ \) (@prp-floor-rules (a)). The minimum is \( \tfrac12 \) exactly when \( t \ge \tfrac12 \) and \( 1 - t \ge \tfrac12 \), that is, when \( t = \tfrac12 \); then \( x - \tfrac12 = m \in \nZ \). Conversely, if \( x - \tfrac12 = k \in \nZ \), then \( k \le x < k + 1 \), so \( m = k \) and \( t = \tfrac12 \).

(c) For every \( n \in \nZ \), \( \abs{(x + 1) - n} = \abs{x - (n - 1)} \) and \( \abs{-x - n} = \abs{x - (-n)} \). As \( n \) runs through \( \nZ \), so do \( n - 1 \) and \( -n \). So the three sets in the definitions of \( \dist(x + 1, \nZ) \), \( \dist(-x, \nZ) \) and \( \dist(x, \nZ) \) are equal, and so are their infima.

(d) The first inequality is the term \( n = 0 \) of the set. For the others, use (a) to choose \( k, l \in \nZ \) with \( \abs{x - k} = \dist(x, \nZ) \) and \( \abs{y - l} = \dist(y, \nZ) \). By the triangle inequality (@fd3:prp-absolute-value-ordered-field (e)),
\[
\dist(x + y, \nZ) \le \abs{(x + y) - (k + l)} \le \abs{x - k} + \abs{y - l} ,
\]
which is subadditivity. Similarly \( \dist(x, \nZ) \le \abs{x - l} \le \abs{x - y} + \abs{y - l} = \abs{x - y} + \dist(y, \nZ) \). Exchanging \( x \) and \( y \) gives \( \dist(y, \nZ) - \dist(x, \nZ) \le \abs{x - y} \), and the two bounds together are \( \abs{\dist(x, \nZ) - \dist(y, \nZ)} \le \abs{x - y} \).

::: {.uses}
@fd3:prp-absolute-value-ordered-field (b) (\( \abs{-x} = \abs{x} \)), (d) (\( \abs{x} \le r \) as two bounds).
:::
:::

The graph is a row of tents: it rises with slope \( 1 \) from \( 0 \) at each integer to \( \tfrac12 \) at each half-integer, and falls back with slope \( -1 \).

```{=latex}
\begin{center}
\begin{tikzpicture}[xscale=1.4, yscale=2.4]
  \draw[->] (-2.3,0) -- (2.4,0) node[right] {$x$};
  \draw[->] (0,-0.1) -- (0,0.8) node[above] {$y$};
  \draw[thick] (-2,0) -- (-1.5,0.5) -- (-1,0) -- (-0.5,0.5) -- (0,0)
               -- (0.5,0.5) -- (1,0) -- (1.5,0.5) -- (2,0);
  \foreach \t in {-2,-1,1,2} \draw (\t,0.03) -- (\t,-0.03) node[below] {\scriptsize $\t$};
  \draw (0.03,0.5) -- (-0.03,0.5) node[left] {\scriptsize $\tfrac12$};
\end{tikzpicture}
\end{center}
```

The figure shows \( \dist(x, \nZ) \) on \( [-2, 2] \). The last inequality of (d) says that no tent is steeper than slope \( 1 \): moving \( x \) by \( h \) changes the height by at most \( \abs{h} \).

Rule (c) says that shifting by \( 1 \) changes nothing. For instance, \( \dist(0.3, \nZ) \), \( \dist(1.3, \nZ) \) and \( \dist(-0.7, \nZ) \) are all \( 0.3 \). Functions with such a shift have a name.

::: {#def-periodic-function}
[Periodic Function]

Let \( f \colon D \to \nR \) with \( D \subseteq \nR \), and let \( p \in \nR \) with \( p \ne 0 \). The number \( p \) is a **period** of \( f \) if, **for every** \( x \in D \), both \( x + p \) and \( x - p \) lie in \( D \) and \( f(x + p) = f(x) \). The function \( f \) is **periodic** if it has a period.
:::

The periods of \( f \) are closed under negation and under non-zero sums. Let \( p, q \) be periods and \( x \in D \). The domain condition for \( -p \) is the one for \( p \). With \( z \coloneqq x - p \in D \), we get \( f(x - p) = f(z) = f(z + p) = f(x) \). If \( p + q \ne 0 \), then \( x \pm (p + q) \in D \) in two steps, and \( f(x + p + q) = f(x + q) = f(x) \). By induction on \( k \ge 1 \) (@fd2:thm-induction), \( kp \) is a period, since \( kp + p = (k + 1)p \ne 0 \); by negation so is \( -kp \). So if \( 1 \) is a period, every non-zero integer is one.

**Examples.** The fractional part \( x \mapsto x - \floor{x} \) on \( \nR \) has period \( 1 \), by @prp-floor-rules (b) with \( n = 1 \): \( (x + 1) - \floor{x + 1} = x - \floor{x} \). The distance \( x \mapsto \dist(x, \nZ) \) has period \( 1 \), by @prp-distance-to-integer (c). A constant function on \( \nR \) has every \( p \ne 0 \) as a period. The identity on \( \nR \) has none, since \( x + p \ne x \).

::: {.check}
Is \( \tfrac12 \) a period of \( x \mapsto \dist(x, \nZ) \)?
:::

::: {.solution}
No. A period \( \tfrac12 \) would give \( \dist(0 + \tfrac12, \nZ) = \dist(0, \nZ) \). But \( \dist(0, \nZ) = 0 \), since \( 0 \in \nZ \), while \( \dist(\tfrac12, \nZ) = \tfrac12 \) by @prp-distance-to-integer (b), since \( \tfrac12 - \tfrac12 = 0 \in \nZ \).
:::

## Step functions

On a bounded interval the floor changes value only finitely often. On \( [0, 3] \) it is \( 0 \) on \( (0, 1) \), \( 1 \) on \( (1, 2) \) and \( 2 \) on \( (2, 3) \). It jumps at \( 1 \), \( 2 \) and \( 3 \), and is constant in between. Functions of this shape are the simplest after the constants.

*A step function is constant between finitely many cut points, and may take any values at the cut points.*

::: {#def-step-function}
[Step Function]

Let \( a, b \in \nR \) with \( a < b \). A function \( \varphi \colon [a, b] \to \nR \) is a **step function** if **there exist** \( n \in \nZ_{>0} \) and points
\[
a = x_0 < x_1 < \dots < x_n = b
\]
such that, **for each** \( i \in \{1, \dots, n\} \), \( \varphi \) is constant on the open interval \( (x_{i-1}, x_i) \). The points \( x_0, \dots, x_n \) form a **partition** of \( [a, b] \) **adapted** to \( \varphi \), and the intervals \( (x_{i-1}, x_i) \) are its **open pieces**.
:::

In words: finitely many cut points, constant on each open piece, and nothing required at the cut points themselves. Adding cut points keeps a partition adapted, since a constant function stays constant on a smaller interval; so an adapted partition is never unique.

**Examples.** A constant function on \( [a, b] \) is a step function, with the partition \( a, b \). So is \( \ind_{[0, 1/2]} \) on \( [0, 1] \) (@fd2:def-indicator), with the partition \( 0, \tfrac12, 1 \): it is \( 1 \) on \( (0, \tfrac12) \) and \( 0 \) on \( (\tfrac12, 1) \), and its value \( 1 \) at the cut point \( \tfrac12 \) is allowed.

The floor on any \( [a, b] \) is a step function. The integers \( j \) with \( a < j < b \) satisfy \( \floor{a} < j \le \floor{b} \), by rules (a) and (g) of @prp-floor-rules. So they form a subset of the finite set \( \{ \floor{a} + 1, \dots, \floor{b} \} \) (@fd2:def-finite). A subset of a finite set is finite (@fd2:prp-subset-finite), so there are finitely many such \( j \). Take as cut points \( a \), \( b \) and these integers, in increasing order. On an open piece \( (x_{i-1}, x_i) \), let \( u < v \) be two of its points. Then \( \floor{v} \le v < x_i \), and \( \floor{v} \le u \): otherwise the integer \( \floor{v} \) would lie in \( (u, v] \), inside the open piece, where no integer is. So \( \floor{v} \le \floor{u} \) by @prp-floor-rules (g), and \( \floor{u} \le \floor{v} \) by (c). The floor is constant on the piece.

**Non-example.** The identity \( x \mapsto x \) on \( [0, 1] \) is not a step function. Every partition has a first open piece \( (x_0, x_1) \) with \( x_0 < x_1 \), and the identity takes two different values on it, at \( x_0 + \tfrac13 (x_1 - x_0) \) and \( x_0 + \tfrac23 (x_1 - x_0) \). The clause that fails is "constant on each open piece".

::: {.check}
Which of these functions on \( [0, 1] \) are step functions: \( \ind_{[0, 1/2]} \); the indicator of \( \{ 1/n : n \in \nZ_{>0} \} \)?
:::

::: {.solution}
The first is, with the partition \( 0, \tfrac12, 1 \), as in the examples. The second is not. Take any partition \( 0 = x_0 < x_1 < \dots < x_n = 1 \). By @fd3:prp-archimedean-reciprocal there is \( n' \in \nZ_{>0} \) with \( 1/n' < x_1 \). The point \( 1/n' \) lies in the first open piece \( (0, x_1) \), and the indicator is \( 1 \) there. The midpoint \( c \) of \( 1/(n' + 1) \) and \( 1/n' \) also lies in \( (0, x_1) \). It is not of the form \( 1/k \), since larger denominators give smaller reciprocals (@fd3:prp-reciprocal-order (b)). For \( k \le n' \), \( 1/k \ge 1/n' > c \), and for \( k \ge n' + 1 \), \( 1/k \le 1/(n' + 1) < c \). So the indicator is \( 0 \) at \( c \), and it is not constant on \( (0, x_1) \).
:::

Combining two step functions point by point gives a step function again. The only work is to find one partition that serves both. For instance, \( \ind_{[0, 1/2]} + \ind_{[0, 1/3]} \) on \( [0, 1] \) needs the merged cut points \( 0, \tfrac13, \tfrac12, 1 \); neither partition alone is adapted to it.

::: {#prp-step-function-algebra}
[Step Functions Are Closed Under the Operations]

Let \( \varphi, \psi \colon [a, b] \to \nR \) be step functions and \( c \in \nR \). Then \( \varphi + \psi \), \( \varphi \psi \), \( c\varphi \), \( \max(\varphi, \psi) \) and \( \abs{\varphi} \) (@def-function-algebra) are step functions.
:::

::: {.idea}
Merge the two partitions. Every open piece of the merged partition sits inside an open piece of each old one, so both \( \varphi \) and \( \psi \) are constant there, and so is anything computed from their values point by point.
:::

::: {.proof}
Let \( P \) and \( Q \) be the sets of cut points of partitions adapted to \( \varphi \) and to \( \psi \), and let \( R \coloneqq P \cup Q \). Then \( R \) is finite, contains \( a \) and \( b \), and lies in \( [a, b] \). So listing it in increasing order gives a partition \( a = r_0 < r_1 < \dots < r_N = b \). Each open piece \( (r_{i-1}, r_i) \) lies inside an open piece of \( P \) and inside an open piece of \( Q \), because no point of \( P \) or \( Q \) lies strictly between consecutive points of \( R \). So \( \varphi \) takes one value \( \alpha \) and \( \psi \) one value \( \beta \) on \( (r_{i-1}, r_i) \). The five functions take the values \( \alpha + \beta \), \( \alpha\beta \), \( c\alpha \), \( \max(\alpha, \beta) \) and \( \abs{\alpha} \) there. Hence each is constant on every open piece of \( R \), and \( R \) is adapted to all five.
:::

::: {.second-reading title="Merging two partitions"}
*\( R \) is finite and can be listed.* \( P \) and \( Q \) are finite. Since \( Q \setminus P \subseteq Q \), it is finite (@fd2:prp-subset-finite). Then \( R = P \cup (Q \setminus P) \) is a disjoint union of finite sets, finite by @fd2:prp-disjoint-union-count. Repeatedly removing the minimum (@fd2:prp-finite-max) lists it in increasing order.

*Each piece of \( R \) lies in a piece of \( P \).* Let \( r < r' \) be consecutive in \( R \). Let \( p \) be the largest point of \( P \) with \( p \le r \) and \( p' \) the least with \( p' \ge r' \); both exist, since \( a, b \in P \) and \( P \) is finite. No point \( q \) of \( P \) lies in \( (p, p') \). If \( q \le r \), it would be a point of \( P \) at most \( r \) and larger than \( p \). If \( q \ge r' \), it would be a point of \( P \) at least \( r' \) and smaller than \( p' \). If \( r < q < r' \), it would be a point of \( R \) between the consecutive points \( r \) and \( r' \). So \( p, p' \) are consecutive in \( P \), and \( (r, r') \subseteq (p, p') \). The same holds for \( Q \).
:::

::: {.remark}
[Looking ahead]

*Integration, Series, and Function Spaces* builds a function that is continuous everywhere and differentiable nowhere by adding up the tents \( \dist(2^k x, \nZ)/2^k \), each a smaller copy of the graph above.
:::

## Exercises

### A. Check your understanding

::: {#exr-floor-and-step-functions-a1}
[A1]

Compute:

::: {.enumerate options="label=(\alph*)"}
1. \( \floor{-0.01} \);
2. \( \ceil{2} \);
3. \( \floor{2.999} + \ceil{-2.999} \);
4. \( \dist(-2.7, \nZ) \);
5. \( \dist(13/4, \nZ) \).
:::
:::

::: {.solution}
(a) \( -1 \le -0.01 < 0 \), so \( \floor{-0.01} = -1 \).

(b) \( \ceil{2} = -\floor{-2} = -(-2) = 2 \), since \( -2 \in \nZ \) (@prp-floor-rules (a)).

(c) \( 2 \le 2.999 < 3 \), so \( \floor{2.999} = 2 \), and \( \ceil{-2.999} = -\floor{2.999} = -2 \). The sum is \( 0 \).

(d) \( \floor{-2.7} = -3 \), so \( t = -2.7 - (-3) = 0.3 \), and \( \dist(-2.7, \nZ) = \min\{0.3, 0.7\} = 0.3 \) (@prp-distance-to-integer (a)). The nearest integer is \( -3 \).

(e) \( \floor{13/4} = 3 \), so \( t = 1/4 \), and \( \dist(13/4, \nZ) = \min\{1/4, 3/4\} = 1/4 \).
:::

::: {#exr-floor-and-step-functions-a2}
[A2]

True or false for all real \( x \), \( y \)? Give a reason or a counterexample.

::: {.enumerate options="label=(\alph*)"}
1. \( \floor{2x} = 2\floor{x} \).
2. \( \floor{x}\floor{y} \le \floor{xy} \).
3. \( \dist(2x, \nZ) \le 2 \dist(x, \nZ) \).
:::
:::

::: {.solution}
(a) False: for \( x = \tfrac12 \), \( \floor{1} = 1 \) but \( 2\floor{\tfrac12} = 0 \).

(b) False: for \( x = y = -\tfrac12 \), \( \floor{x}\floor{y} = (-1)(-1) = 1 \), but \( \floor{xy} = \floor{\tfrac14} = 0 \).

(c) True: subadditivity in @prp-distance-to-integer (d), with \( y = x \), gives \( \dist(x + x, \nZ) \le \dist(x, \nZ) + \dist(x, \nZ) \).
:::

### B. Practice

::: {#exr-floor-and-step-functions-b1}
[B1: Prove or disprove]

Prove each true statement for all real \( x \), and refute each false one with a counterexample. In (c), prove it for all \( x \ge 0 \).

::: {.enumerate options="label=(\alph*)"}
1. \( \floor{2x} = \floor{x} + \floor{x + \tfrac12} \).
2. \( \ceil{x} - \floor{x} = 1 \).
3. \( \floor{\sqrt{\floor{x}}} = \floor{\sqrt{x}} \) for \( x \ge 0 \).
4. \( \floor{x} + \floor{-x} = 0 \).
:::
:::

::: {.solution}
(a) True. Let \( m \coloneqq \floor{x} \) and \( t \coloneqq x - m \in [0, 1) \). *Case \( t < \tfrac12 \).* Then \( 2x = 2m + 2t \) with \( 0 \le 2t < 1 \), so \( 2m \le 2x < 2m + 1 \) and \( \floor{2x} = 2m \). Also \( x + \tfrac12 = m + (t + \tfrac12) \) with \( \tfrac12 \le t + \tfrac12 < 1 \), so \( \floor{x + \tfrac12} = m \). Both sides are \( 2m \). *Case \( t \ge \tfrac12 \).* Then \( 1 \le 2t < 2 \), so \( \floor{2x} = 2m + 1 \). Also \( 1 \le t + \tfrac12 < \tfrac32 \), so \( \floor{x + \tfrac12} = m + 1 \). Both sides are \( 2m + 1 \). Each floor was found by the first form of @exm-method-floor-inequality.

(b) False: for \( x = 0 \), \( \ceil{0} - \floor{0} = 0 \). (For \( x \notin \nZ \) it is true, by @prp-floor-rules (e).)

(c) True, by the second form. Since \( 0 \le x \), \( 0 \le \floor{x} \) by @prp-floor-rules (g), so both square roots exist. First, for \( u, v \ge 0 \): \( u \le \sqrt v \iff u^2 \le v \). Indeed, if \( u \le \sqrt v \), then \( u^2 \le (\sqrt v)^2 = v \) by @lem-reals-nth-root (a) with \( n = 2 \), with equality when \( u = \sqrt v \). If \( u > \sqrt v \), then \( u^2 > v \) by the same part. Now let \( j \in \nZ \). If \( j \ge 0 \),
\[
j \le \sqrt{\floor{x}} \iff j^2 \le \floor{x} \iff j^2 \le x \iff j \le \sqrt x ,
\]
the middle step by @prp-floor-rules (g), since \( j^2 \in \nZ \). If \( j < 0 \), then \( j \) lies below both square roots, which are \( \ge 0 \), so both sides hold. Rule (g) rewrites \( j \le \sqrt x \) as \( j \le \floor{\sqrt x} \). So every \( j \in \nZ \) satisfies \( j \le \sqrt{\floor{x}} \iff j \le \floor{\sqrt x} \), and the second form gives \( \floor{\sqrt{\floor{x}}} = \floor{\sqrt x} \).

(d) False: for \( x = \tfrac12 \), \( \floor{\tfrac12} + \floor{-\tfrac12} = 0 + (-1) = -1 \). It holds exactly for \( x \in \nZ \), by @prp-floor-rules (e).
:::

::: {#exr-floor-and-step-functions-b2}
[B2: Counting multiples]

Let \( N, k \in \nZ_{>0} \). Prove that the number of multiples of \( k \) in \( \{1, \dots, N\} \) is \( \floor{N/k} \).
:::

::: {.solution}
The multiples of \( k \) are the numbers \( jk \) with \( j \in \nZ \). Since \( k > 0 \), \( jk \ge 1 \) holds exactly when \( j \ge 1 \): for \( j \ge 1 \), \( jk \ge k \ge 1 \), and for \( j \le 0 \), \( jk \le 0 \). Also
\[
jk \le N \iff j \le N/k \iff j \le \floor{N/k} .
\]
The first step multiplies or divides by \( k > 0 \), which keeps the direction of \( \le \). The second step is rule (g) of @prp-floor-rules. So the multiples of \( k \) in \( \{1, \dots, N\} \) are exactly \( jk \) with \( j \in \{1, \dots, \floor{N/k}\} \); here \( \floor{N/k} \ge 0 \), since \( N/k > 0 \), and the set is empty when \( \floor{N/k} = 0 \). The map \( j \mapsto jk \) from \( \{1, \dots, \floor{N/k}\} \) onto this set is injective, since \( jk = j'k \) and \( k \ne 0 \) give \( j = j' \). So it is a bijection, and the set has \( \floor{N/k} \) elements (@fd2:def-finite). This number of elements is unique (@fd2:cor-finite-size-unique).

::: {.uses}
@fd3:prp-ordered-ring-rules (c) (multiplying by a positive); @fd3:prp-reciprocal-order (a) (\( 1/k > 0 \)).
:::
:::

::: {#exr-floor-and-step-functions-b3}
[B3]

Show that \( \varphi(x) \coloneqq \floor{2x} - 2\floor{x} \) is a step function on \( [0, 2] \), and give an adapted partition and the values on its open pieces.
:::

::: {.solution}
Take the partition \( 0, \tfrac12, 1, \tfrac32, 2 \). On each open piece both floors are constant, by the first form of @exm-method-floor-inequality:

- on \( (0, \tfrac12) \): \( 2x \in (0, 1) \) and \( x \in (0, 1) \), so \( \varphi = 0 - 0 = 0 \);
- on \( (\tfrac12, 1) \): \( 2x \in (1, 2) \), \( x \in (0, 1) \), so \( \varphi = 1 - 0 = 1 \);
- on \( (1, \tfrac32) \): \( 2x \in (2, 3) \), \( x \in (1, 2) \), so \( \varphi = 2 - 2 = 0 \);
- on \( (\tfrac32, 2) \): \( 2x \in (3, 4) \), \( x \in (1, 2) \), so \( \varphi = 3 - 2 = 1 \).

So \( \varphi \) is constant on each open piece, as @def-step-function requires. At the cut points, \( \varphi(0) = 0 \), \( \varphi(\tfrac12) = 1 \), \( \varphi(1) = 0 \), \( \varphi(\tfrac32) = 1 \), \( \varphi(2) = 0 \).
:::

### C. Going deeper

::: {#exr-floor-and-step-functions-c1}
[C1: A sum of floors]

Let \( n \in \nZ_{>0} \). Prove that for every \( x \in \nR \),
\[
\sum_{k=0}^{n-1} \floor{x + \frac{k}{n}} = \floor{nx} .
\]
:::

::: {.solution}
[Hint 1]

Compare the left side at \( x \) and at \( x + 1/n \): which terms survive the shift?
:::

::: {.solution}
[Hint 2]

Let \( F(x) \) be the left side minus the right side. Show that \( 1/n \) is a period of \( F \) and that \( F = 0 \) on \( [0, 1/n) \).
:::

::: {.solution}
Let \( F(x) \coloneqq \sum_{k=0}^{n-1} \floor{x + k/n} - \floor{nx} \) for \( x \in \nR \).

*Step 1: \( 1/n \) is a period of \( F \).* Shifting the index gives
\[
\sum_{k=0}^{n-1} \floor{x + \tfrac{k+1}{n}} = \sum_{k=1}^{n-1} \floor{x + \tfrac{k}{n}} + \floor{x + 1} ,
\]
and \( \floor{x + 1} = \floor{x} + 1 \) by rule (b) of @prp-floor-rules. Since \( \floor{x} \) is the term \( k = 0 \) of the sum at \( x \), the left side of the identity grows by exactly \( 1 \) from \( x \) to \( x + 1/n \). So does the right side: \( \floor{n(x + 1/n)} = \floor{nx + 1} = \floor{nx} + 1 \). Hence \( F(x + 1/n) = F(x) \) for every \( x \), and \( 1/n \) is a period of \( F \) on \( \nR \) (@def-periodic-function).

*Step 2: \( F = 0 \) on \( [0, 1/n) \).* For \( 0 \le x < 1/n \) and \( 0 \le k \le n - 1 \), \( 0 \le x + k/n < 1/n + (n - 1)/n = 1 \), so each \( \floor{x + k/n} = 0 \). Also \( 0 \le nx < 1 \), so \( \floor{nx} = 0 \).

*Step 3: every \( x \).* Let \( j \coloneqq \floor{nx} \) and \( y \coloneqq x - j/n \). From \( j \le nx < j + 1 \), dividing by \( n \), \( 0 \le y < 1/n \). If \( j \ne 0 \), then \( j/n \) is a period of \( F \), since integer multiples of a period are periods; so \( F(x) = F(y + j/n) = F(y) = 0 \). If \( j = 0 \), then \( x = y \) and \( F(x) = 0 \) by Step 2. This proves the identity.

::: {.uses}
@fd2:def-sum-product (shifting the index).
:::

**What a complete answer needs.** (10 points)

- 3: shows that both sides increase by exactly \( 1 \) under \( x \mapsto x + 1/n \), naming @prp-floor-rules (b) for each side.
- 2: checks that both sides vanish on \( [0, 1/n) \), with the bound \( x + (n - 1)/n < 1 \).
- 3: reduces an arbitrary \( x \) to \( [0, 1/n) \) by a multiple \( j/n \) of the period, with \( j = \floor{nx} \) (or another integer chosen so that the remainder lands in \( [0, 1/n) \)).
- 2: uses that integer multiples of a period (including negative ones) are periods, or iterates the shift in both directions.

A direct count also earns full marks. Write \( t = x - \floor{x} \). The terms with \( t + k/n \ge 1 \) equal \( \floor{x} + 1 \), and the others equal \( \floor{x} \). Such a proof earns the 3, 2, 3 and 2 points for, in order: the count, each term's inequality, \( \floor{nx} \), and the comparison.

Slips that lose the step (0 points for it): shifting only forward, although \( x < 0 \) needs a backward shift; treating \( \floor{x + 1} \) as \( \floor{x} \).
:::

::: {#exr-floor-and-step-functions-c2}
[C2: Multiplying the distance]

Let \( n \in \nZ_{>0} \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \dist(nx, \nZ) \le n \dist(x, \nZ) \) for every \( x \in \nR \).
2. Prove that equality holds whenever \( \dist(x, \nZ) \le 1/(2n) \).
3. Find \( x \) with strict inequality for \( n = 2 \).
:::

*Hint: if \( \abs{y - k} \le \tfrac12 \) for an integer \( k \), then \( \dist(y, \nZ) = \abs{y - k} \).*
:::

::: {.solution}
(a) By induction on \( n \ge 1 \) (@fd2:thm-induction, with base \( 1 \)). For \( n = 1 \) both sides are \( \dist(x, \nZ) \). If \( \dist(nx, \nZ) \le n \dist(x, \nZ) \), then subadditivity (@prp-distance-to-integer (d)) gives
\[
\dist((n + 1)x, \nZ) \le \dist(nx, \nZ) + \dist(x, \nZ) \le (n + 1)\dist(x, \nZ) .
\]

(b) First the hint. Let \( \abs{y - k} \le \tfrac12 \) with \( k \in \nZ \), and let \( j \in \nZ \) with \( j \ne k \). Then \( \abs{j - k} \ge 1 \) by discreteness (@fd3:thm-integers-ordered-ring (c)). The reverse triangle inequality (@fd3:prp-absolute-value-ordered-field (f)) gives
\[
\abs{y - j} \ge \abs{j - k} - \abs{y - k} \ge 1 - \tfrac12 = \tfrac12 \ge \abs{y - k} .
\]
So \( \abs{y - k} \) is the least of the numbers \( \abs{y - j} \), \( j \in \nZ \), and equals \( \dist(y, \nZ) \).

Now let \( \dist(x, \nZ) \le 1/(2n) \). By @prp-distance-to-integer (a) there is \( k \in \nZ \) with \( \abs{x - k} = \dist(x, \nZ) \); put \( t \coloneqq x - k \). Then \( nx = nk + nt \) with \( nk \in \nZ \) and \( \abs{nx - nk} = n\abs{t} \le \tfrac12 \). By the hint, \( \dist(nx, \nZ) = n\abs{t} = n \dist(x, \nZ) \).

::: {.uses}
@fd3:prp-absolute-value-ordered-field (b) (\( \abs{nt} = n\abs{t} \), as \( n > 0 \)).
:::

(c) \( x = \tfrac12 \): \( \dist(1, \nZ) = 0 < 1 = 2 \dist(\tfrac12, \nZ) \). Here \( \dist(x, \nZ) = \tfrac12 > \tfrac14 = 1/(2n) \), so (b) does not apply. Exercise A2 (c) gave the inequality only; (b) adds where it is an equality.
:::

<!-- dependency ledger
def-floor-ceiling (example): integer arithmetic and comparisons agree in Z and in R (embedding) | fd3:thm-rationals-embed-ordered-field, recalled in prose
prp-floor-rules (proof): Z is closed under +, -, and products of integers are integers | fd3:thm-integers-ordered-ring (ring), standard
def-floor-ceiling (example): products of integers agree in Z and in R (embedding) | fd3:thm-rationals-embed-ordered-field, recalled in prose
prp-distance-to-integer (proof): a lower bound of a set that belongs to the set is its infimum and its minimum | fd2:def-order-supremum (dual), inline
prp-distance-to-integer (proof): n -> n - 1 and n -> -n are bijections of Z | inline (ring laws of Z)
def-periodic-function (claim): closure of periods under negation and non-zero sums; integer multiples by induction on k | inline, fd2:thm-induction
def-step-function (example): an integer in (u, v] with x_{i-1} < u < v < x_i lies in the open piece | inline (order)
def-step-function (example): {m+1,...,M} has M-m elements via j -> m+j | inline
def-step-function (example): listing a finite set of reals increasingly | fd2:prp-finite-max
prp-step-function-algebra (proof): the merged partition lies in pieces of P and Q | inline, in the fold
exr-floor-and-step-functions-b2 (solution): jk >= 1 iff j >= 1 for k in Z_{>0} | fd3:thm-integers-ordered-ring (c), inline
exr-floor-and-step-functions-c2 (solution): |nt| = n|t| | fd3:prp-absolute-value-ordered-field (b), Uses line
exr-floor-and-step-functions-c1 (solution): index shift in a finite sum | fd2:def-sum-product, Uses line
-->
