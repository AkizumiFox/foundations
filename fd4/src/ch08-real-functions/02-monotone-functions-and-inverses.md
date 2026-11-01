# Monotone Functions and Inverse Functions

Section 8.1 made real functions into objects with a domain and a graph, and combined them. This section asks how a function treats the order of \( \nR \): does a larger input give a larger output? We give the property its definition, a method for proving it, and rules for building monotone functions from others. Then we prove the main result: a strictly monotone function is a bijection onto its image, and its inverse is monotone in the same direction. That gives the \( n \)-th root as a function, for every real input when \( n \) is odd.

## Increasing and decreasing functions

Ask a reader whether \( x \mapsto 1/x \) is decreasing, and the answer is usually yes. On \( \nR \setminus \{0\} \) it is not: \( -1 < 1 \), but \( 1/(-1) = -1 < 1 = 1/1 \), so a larger input gave a larger output. The function decreases on \( (-\infty, 0) \) and on \( (0, \infty) \), and the jump across \( 0 \) spoils the union. So "decreasing" is never a property of a formula alone. It is a property of a function **on a set**, and the definition must name the set.

*A function is increasing on a set when moving right inside the set never moves its value down.*

::: {#def-monotone-function}
[Monotone Function]

Let \( f \colon D \to \nR \) be a real function (@def-real-function) and let \( A \subseteq D \). The function \( f \) is

- **increasing on \( A \)** if, **for all** \( x, y \in A \), \( x < y \) implies \( f(x) \le f(y) \);
- **strictly increasing on \( A \)** if, for all \( x, y \in A \), \( x < y \) implies \( f(x) < f(y) \);
- **decreasing on \( A \)** if, for all \( x, y \in A \), \( x < y \) implies \( f(x) \ge f(y) \);
- **strictly decreasing on \( A \)** if, for all \( x, y \in A \), \( x < y \) implies \( f(x) > f(y) \).

It is **monotone on \( A \)** if it is increasing on \( A \) or decreasing on \( A \), and **strictly monotone on \( A \)** if it is strictly increasing or strictly decreasing on \( A \). Without "on \( A \)", the set is the whole domain \( D \). In symbols, "increasing on \( A \)" is
\[
\forall x \in A \ \ \forall y \in A \ \ \bigl( x < y \to f(x) \le f(y) \bigr) .
\]
:::

In words: we pick two points of \( A \), name the smaller one \( x \), and ask that the values come in the same order (\( \le \) or \( < \)) or in the reverse order (\( \ge \) or \( > \)). Since \( x \le y \) means \( x < y \) or \( x = y \), an increasing function also satisfies \( x \le y \Rightarrow f(x) \le f(y) \), and likewise for the other three kinds.

Negating quantifier by quantifier (@fd1:prp-quantifier-negation), "\( f \) is **not** increasing on \( A \)" is
\[
\exists x \in A \ \ \exists y \in A \ \ \bigl( x < y \wedge f(x) > f(y) \bigr) ,
\]
so a failure is shown by **two witnesses**, as \( -1 \) and \( 1 \) were in the hook.

The identity \( x \mapsto x \) on \( \nR \) is strictly increasing, and so is \( x \mapsto x^3 \): the word agrees with the one of *Sets and Functions*, where that map was proved strictly increasing (@fd2:exm-maps-from-calculus (a)) and every strictly increasing map between subsets of \( \nR \) was shown injective (@fd2:prp-strictly-monotone-injective). We use both without proving them again.

::: {.second-reading title="The two definitions agree; sets with one point"}
*Sets and Functions* called a map \( f \colon A \to B \) between subsets of \( \nR \) strictly increasing when \( x < x' \) implies \( f(x) < f(x') \). Our \( f \colon D \to \nR \) is strictly increasing on \( A \) exactly when its restriction \( f|_A \colon A \to \nR \) (@fd2:def-restriction-extension) is strictly increasing in that sense: both say the same thing about the same pairs of points of \( A \). The codomain plays no part.

The degenerate case: on a set \( A \) with at most one point there is no pair \( x < y \), so every function is strictly increasing and strictly decreasing on \( A \), vacuously. Monotonicity says something only about pairs.
:::

::: {.warning}
Monotone on two sets does not give monotone on their union. The function \( 1/x \) is strictly decreasing on \( (-\infty, 0) \) and on \( (0, \infty) \), yet not decreasing on \( \nR \setminus \{0\} \), by the witnesses \( -1 < 1 \) of the hook. A proof that splits \( A \) into pieces must also compare a point of one piece with a point of the other.
:::

::: {.check}
Is a constant function on \( \nR \) increasing? Is \( 1/x \) decreasing on \( \nR \setminus \{0\} \)? Is the indicator \( \ind_{[0, \infty)} \) (@fd2:def-indicator) increasing on \( \nR \)? For each "yes", say whether "strictly" holds too.
:::

::: {.solution}
A constant is increasing, since \( f(x) = f(y) \) satisfies \( \le \); it is decreasing too, and strictly neither: \( 0 < 1 \) and the values are equal. The function \( 1/x \) is not decreasing on \( \nR \setminus \{0\} \): \( -1 < 1 \) and \( 1/(-1) < 1/1 \). The indicator is increasing: for \( x < y \), if its value at \( x \) is \( 1 \), then \( 0 \le x < y \) and its value at \( y \) is \( 1 \) too. It is not strictly increasing: \( -2 < -1 \) with both values \( 0 \).
:::

## The method: factor out the difference of the inputs

To prove \( f \) strictly increasing on \( A \), we fix \( x < y \) in \( A \) and must show \( f(y) - f(x) > 0 \). The hypothesis is about the difference \( y - x \), which is positive. So the natural plan is to make \( y - x \) appear as a factor of \( f(y) - f(x) \), and then to sign what is left.

::: {#exm-method-factor-difference}
[Method: factor out y − x]

**Template.** "Let \( x, y \in A \) with \( x < y \)." Write
\[
f(y) - f(x) = (y - x) \, Q(x, y)
\]
by algebra on the formula for \( f \). Since \( y - x > 0 \), the sign of \( f(y) - f(x) \) is the sign of \( Q(x, y) \): show \( Q(x, y) > 0 \) for strictly increasing, \( Q(x, y) \ge 0 \) for increasing, and \( < 0 \) or \( \le 0 \) for the decreasing kinds (@fd3:prp-ordered-ring-rules (c), (d)). Differences of powers factor by @lem-difference-of-powers:
\[
y^n - x^n = (y - x) \sum_{k=0}^{n-1} y^k x^{n-1-k} .
\]
Quotients are brought over a common denominator first.

**When to use it.** \( f \) is given by a formula built from \( + \), \( \cdot \) and \( / \), and the claim is that \( f \) is monotone on a set.

**The usual failure.** Concluding "strictly" from \( Q \ge 0 \): a positive number times a non-negative one may be \( 0 \). And using a sign of \( Q \) that holds on part of \( A \) only; then split \( A \) first, and compare across the pieces as the warning above demands.

| Givens | Goal |
|---|---|
| \( x, y \in A \), \( x < y \); the formula for \( f \) | \( f(x) < f(y) \) |
| \( y - x > 0 \) | \( f(y) - f(x) > 0 \) |
| \( f(y) - f(x) = (y - x) \, Q(x, y) \) | \( Q(x, y) > 0 \): the gap the method leaves |
:::

The first worked example is a quotient, where the obvious argument fails.

::: {#exm-mobius-increasing}
[A quotient of two increasing functions]

Let \( g \colon (-2, \infty) \to \nR \), \( g(x) = \dfrac{x - 1}{x + 2} \). Prove that \( g \) is strictly increasing.
:::

::: {.idea}
[Scratch work]

*The naive attempt.* "The numerator \( x - 1 \) increases with \( x \), so the quotient does." The denominator increases too, and a quotient of two increasing positive things can do anything: \( x/x \) is constant. So the naive attempt proves nothing.

*Factor out \( y - x \).* For \( -2 < x < y \), bring the difference over the common denominator \( (x + 2)(y + 2) \), which is positive. The numerator is
\[
\begin{aligned}
&(y - 1)(x + 2) - (x - 1)(y + 2) \\
&\quad = (xy + 2y - x - 2) - (xy + 2x - y - 2) = 3(y - x) .
\end{aligned}
\]
So \( Q(x, y) = 3/\bigl((x + 2)(y + 2)\bigr) \).

| Givens | Goal |
|---|---|
| \( -2 < x < y \) | \( g(y) - g(x) > 0 \) |
| \( g(y) - g(x) = 3(y - x)/\bigl((x + 2)(y + 2)\bigr) \) | \( Q(x, y) = 3/\bigl((x + 2)(y + 2)\bigr) > 0 \) |
| \( x + 2 > 0 \), \( y + 2 > 0 \) | closed: a quotient of positive elements |
:::

::: {.solution}
Let \( x, y \in (-2, \infty) \) with \( x < y \). Then \( x + 2 > 0 \) and \( y + 2 > 0 \), so the denominators are non-zero and, by @fd3:lem-field-fraction-rules,
\[
g(y) - g(x) = \frac{(y - 1)(x + 2) - (x - 1)(y + 2)}{(x + 2)(y + 2)} = \frac{3(y - x)}{(x + 2)(y + 2)} .
\]
The numerator is positive since \( y - x > 0 \), and the denominator is a product of two positive elements, positive by (O4); its reciprocal is positive by @fd3:prp-reciprocal-order (a). Hence \( g(y) - g(x) > 0 \) (@fd3:prp-ordered-ring-rules (a)), and \( g \) is strictly increasing.
:::

The scratch work found the factor \( 3(y - x) \); the proof starts from it and signs each piece once. Nothing in the proof mentions the naive attempt.

The second example needs the split that the method box warns about.

::: {#exm-squash-function}
[The squashing function]

Let \( \sigma \colon \nR \to \nR \), \( \sigma(x) = \dfrac{x}{1 + \abs{x}} \). Prove that \( \sigma \) is strictly increasing on \( \nR \), and find its image.
:::

::: {.idea}
The absolute value has one formula for \( x \ge 0 \) and another for \( x \le 0 \), so the factoring works on each half separately. Two points in the same half are handled by the method; for one point in each half, the signs of the values decide at once, since \( \sigma(x) \) has the sign of \( x \).
:::

::: {.solution}
Since \( 1 + \abs{x} \ge 1 > 0 \), \( \sigma \) is defined on \( \nR \) and \( \sigma(x) \) has the sign of \( x \). Let \( x < y \).

*Case \( 0 \le x < y \).* Here \( \sigma(t) = t/(1 + t) \) at \( t = x, y \), and
\[
\sigma(y) - \sigma(x) = \frac{y(1 + x) - x(1 + y)}{(1 + x)(1 + y)} = \frac{y - x}{(1 + x)(1 + y)} > 0 .
\]

*Case \( x < y \le 0 \).* Here \( \sigma(t) = t/(1 - t) \), and
\[
\sigma(y) - \sigma(x) = \frac{y(1 - x) - x(1 - y)}{(1 - x)(1 - y)} = \frac{y - x}{(1 - x)(1 - y)} > 0 ,
\]
since \( 1 - x \ge 1 \) and \( 1 - y \ge 1 \).

*Case \( x < 0 \le y \).* Then \( \sigma(x) < 0 \le \sigma(y) \).

By trichotomy the three cases cover every pair \( x < y \), so \( \sigma \) is strictly increasing. Its image is \( (-1, 1) \): every value satisfies \( \abs{\sigma(x)} = \abs{x}/(1 + \abs{x}) < 1 \), and every \( v \in (-1, 1) \) is a value, at \( x = v/(1 - \abs{v}) \), which is \( v/(1 - v) \) for \( v \ge 0 \) and \( v/(1 + v) \) for \( v < 0 \). That is the surjectivity proved in *Sets and Functions* by solving backwards (@fd2:exm-fraction-map).
:::

## Building monotone functions from others

The method handles one formula at a time. Most functions are built from simpler ones by the operations of @def-function-algebra, and monotonicity passes through some of them.

::: {#prp-monotone-algebra}
[Rules for Monotone Functions]

Let \( f, g \colon D \to \nR \) and \( A \subseteq D \).

::: {.enumerate options="label=(\alph*)"}
1. If \( f \) and \( g \) are increasing on \( A \), so is \( f + g \); it is strictly increasing if \( f \) or \( g \) is.
2. If \( f \) is increasing on \( A \) and \( c \ge 0 \), then \( cf \) is increasing on \( A \), strictly if \( f \) is and \( c > 0 \); and \( -f \) is decreasing on \( A \), strictly if \( f \) is strictly increasing.
3. If \( f \) and \( g \) are increasing on \( A \) and \( f(x) \ge 0 \), \( g(x) \ge 0 \) for every \( x \in A \), then \( fg \) is increasing on \( A \).
4. If \( f \) is increasing on \( A \) and \( f(x) > 0 \) for every \( x \in A \), then \( 1/f \) is decreasing on \( A \), strictly if \( f \) is strictly increasing.
5. Let \( f \colon D \to \nR \), \( g \colon E \to \nR \), \( A \subseteq D \) and \( B \subseteq E \) with \( f(A) \subseteq B \). If \( f \) is monotone on \( A \) and \( g \) on \( B \), then \( g \circ f \) is monotone on \( A \): increasing if both are increasing or both decreasing, decreasing if one is increasing and the other decreasing; strictly so if both are strictly monotone.
:::
:::

::: {.idea}
Each part fixes \( x < y \) in \( A \), writes down what the hypotheses say about the values at \( x \) and \( y \), and applies one rule for inequalities in an ordered field to them.
:::

::: {.proof}
In each part let \( x, y \in A \) with \( x < y \).

(a) \( f(x) \le f(y) \) and \( g(x) \le g(y) \), so \( f(x) + g(x) \le f(y) + g(y) \), strictly if one of the two is strict (@fd3:prp-ordered-ring-rules (b)).

(b) If \( c = 0 \), \( cf \) is constant. If \( c > 0 \), \( f(x) \le f(y) \) gives \( cf(x) \le cf(y) \) (@fd3:prp-ordered-ring-rules (c), or equality), strictly if \( f(x) < f(y) \). And \( f(x) \le f(y) \) gives \( -f(y) \le -f(x) \), strictly if \( f(x) < f(y) \) (@fd3:prp-ordered-ring-rules (a)).

(c) \( 0 \le f(x) \le f(y) \) and \( 0 \le g(x) \le g(y) \), so \( f(x)g(x) \le f(y)g(y) \) by @fd3:prp-ordered-field-halves (d).

(d) \( 0 < f(x) \le f(y) \), so \( 1/f(y) \le 1/f(x) \) by @fd3:prp-ordered-field-halves (c), strictly if \( f(x) < f(y) \) by @fd3:prp-reciprocal-order (b).

(e) The composite is defined on \( A \), since \( f(A) \subseteq B \subseteq E \) (@def-function-algebra). Let \( f \) and \( g \) be increasing. Then \( f(x) \le f(y) \) with both in \( B \), so \( g(f(x)) \le g(f(y)) \) by the remark after @def-monotone-function. If both are strict, \( f(x) < f(y) \) and then \( g(f(x)) < g(f(y)) \). The other three cases are the same argument with the inequality reversed at each decreasing function: two reversals restore the order, one reverses it.
:::

::: {.warning}
The sign condition in (c) cannot be dropped. The identity \( x \mapsto x \) is increasing on \( \nR \), but its product with itself, \( x \mapsto x^2 \), is not: \( -1 < 0 \) and \( (-1)^2 = 1 > 0 = 0^2 \).
:::

::: {.check}
On \( [0, \infty) \), the functions \( x \mapsto x \) and \( x \mapsto x^2 + 1 \) are increasing and non-negative. Is \( x \mapsto x(x^2 + 1) \) increasing on \( [0, \infty) \), and by which rule?
:::

::: {.solution}
Yes, by (c): both factors are increasing on \( [0, \infty) \) (the second by @lem-reals-nth-root (a) with \( n = 2 \), then rule (a) with a constant), and both are \( \ge 0 \) there.
:::

## Strict monotonicity reflects the order

A strictly increasing function carries \( x < y \) to \( f(x) < f(y) \). For the inverse we need the way back: from \( f(x) < f(y) \) to \( x < y \). Because \( \le \) on \( \nR \) is a total order, the way back is free.

::: {#prp-strictly-monotone-order-reflecting}
[Strictly Monotone Functions Reflect the Order]

Let \( f \colon D \to \nR \), \( A \subseteq D \), and \( x, y \in A \).

::: {.enumerate options="label=(\alph*)"}
1. If \( f \) is strictly increasing on \( A \), then \( x < y \iff f(x) < f(y) \), and \( x \le y \iff f(x) \le f(y) \).
2. If \( f \) is strictly decreasing on \( A \), then \( x < y \iff f(x) > f(y) \), and \( x \le y \iff f(x) \ge f(y) \).
:::
:::

::: {.idea}
The directions \( (\Rightarrow) \) are the definition. For the way back, suppose the conclusion fails; totality turns "not \( x < y \)" into \( y \le x \), and the forward direction then contradicts the hypothesis.
:::

::: {.proof}
(a) The direction \( (\Rightarrow) \) of the first equivalence is @def-monotone-function. For \( (\Rightarrow) \) of the second: if \( x \le y \), then \( x = y \) and \( f(x) = f(y) \), or \( x < y \) and \( f(x) < f(y) \); in both cases \( f(x) \le f(y) \).

\( (\Leftarrow) \) of the first: let \( f(x) < f(y) \), and suppose \( x < y \) fails. Since \( \le \) is a total order with strict part \( < \) (@fd3:prp-ordered-field-halves (a)), \( y \le x \). By \( (\Rightarrow) \) of the second equivalence, \( f(y) \le f(x) \). With \( f(x) < f(y) \) this gives \( f(x) = f(y) \) by antisymmetry, against \( f(x) \ne f(y) \). So \( x < y \).

\( (\Leftarrow) \) of the second: let \( f(x) \le f(y) \), and suppose \( x \le y \) fails. By totality, \( y \le x \) and \( y \ne x \), that is, \( y < x \); so \( f(y) < f(x) \), against \( f(x) \le f(y) \). So \( x \le y \).

(b) By @prp-monotone-algebra (b), \( -f \) is strictly increasing on \( A \), and \( f(x) > f(y) \iff -f(x) < -f(y) \) (@fd3:prp-ordered-ring-rules (a)), and likewise for \( \ge \). Apply (a) to \( -f \).
:::

Taking \( x \le y \) and \( y \le x \) together, the second equivalence gives \( f(x) = f(y) \Rightarrow x = y \) again: injectivity, which *Sets and Functions* proved directly (@fd2:prp-strictly-monotone-injective). What is new is the direction \( (\Leftarrow) \), and it rests on totality alone.

::: {.check}
Which half of @prp-strictly-monotone-order-reflecting (a) uses that \( \le \) is total, and how?
:::

::: {.solution}
The directions \( (\Leftarrow) \). From "not \( x < y \)" totality gives \( y \le x \), hence \( f(y) \le f(x) \), against \( f(x) < f(y) \). In a partial order, "not \( x < y \)" would allow \( x \) and \( y \) to be incomparable, and the argument would stop.
:::

The converse of @fd2:prp-strictly-monotone-injective is false: an injective function need not be monotone.

::: {#exm-injective-not-monotone}
[Injective but not monotone]

Let \( f \colon \nR \to \nR \) swap \( 0 \) and \( 1 \): \( f(0) = 1 \), \( f(1) = 0 \), and \( f(x) = x \) for every other \( x \). Show that \( f \) is injective but monotone on no set containing \( 0 \), \( 1 \) and \( 2 \). Then do the same for \( 1/x \) on \( \nR \setminus \{0\} \) and the set \( \{-1, 1, 2\} \).
:::

::: {.solution}
*The swap.* Checking the three cases of the definition, \( f(f(x)) = x \) for every \( x \), so \( f \) is its own two-sided inverse and is bijective (@fd2:thm-bijection-iff-inverse). It is not increasing: \( 0 < 1 \) and \( f(0) = 1 > 0 = f(1) \). It is not decreasing: \( 1 < 2 \) and \( f(1) = 0 < 2 = f(2) \).

*The reciprocal.* If \( 1/x = 1/y \), then \( x = y \), taking reciprocals. It is not increasing: \( 1 < 2 \) and \( 1 > 1/2 \). It is not decreasing: \( -1 < 1 \) and \( -1 < 1 \), the witnesses of the hook.
:::

## The inverse of a strictly monotone function

By @fd2:thm-bijection-iff-inverse, a function has an inverse exactly when it is a bijection. A strictly increasing \( f \colon A \to \nR \) is injective, but usually not surjective onto \( \nR \): \( \sigma \) of @exm-squash-function misses \( 1 \). Cutting the codomain down to the image repairs that, and the inverse then inherits the order.

::: {#thm-monotone-inverse}
[Inverse of a Strictly Monotone Function]

Let \( A \subseteq \nR \) and let \( f \colon A \to \nR \) be strictly increasing. Then:

::: {.enumerate options="label=(\alph*)"}
1. \( f \), with codomain \( f(A) \), is a bijection \( A \to f(A) \); write \( f^{-1} \colon f(A) \to A \) for its inverse;
2. \( f^{-1} \) is strictly increasing;
3. \( \operatorname{graph} f^{-1} = \{ (y, x) : (x, y) \in \operatorname{graph} f \} \).
:::

The same holds with "strictly decreasing" in place of "strictly increasing", in the hypothesis and in (b).
:::

*Try it first (ten minutes): take \( u < v \) in \( f(A) \). Why should \( f^{-1}(u) < f^{-1}(v) \)?*

::: {.idea}
The direct attempt applies \( f^{-1} \) to \( u < v \), but nothing is known about \( f^{-1} \) yet; that is what we are proving. So name the two preimages, \( x \coloneqq f^{-1}(u) \) and \( y \coloneqq f^{-1}(v) \). Now \( f(x) = u < v = f(y) \), and the question is about \( f \) alone: does \( f(x) < f(y) \) force \( x < y \)? That is the direction \( (\Leftarrow) \) of @prp-strictly-monotone-order-reflecting. The bijection costs nothing: \( f(A) \) is chosen so that every point is reached, and strict monotonicity gives injectivity. The graph is @exm-method-graph-pairs with the move \( (x, y) \mapsto (y, x) \).

*Before reading on: where is the totality of \( \le \) used?*
:::

::: {.proof}
(a) For \( x \in A \), \( f(x) \in f(A) \) by @fd2:def-image, so \( f \) is a function \( A \to f(A) \). It is surjective, since every \( v \in f(A) \) is \( f(a) \) for some \( a \in A \) (@fd2:def-image), and injective by @fd2:prp-strictly-monotone-injective. By @fd2:thm-bijection-iff-inverse it has a two-sided inverse \( f^{-1} \colon f(A) \to A \) (@fd2:def-inverse-function).

(b) Let \( u, v \in f(A) \) with \( u < v \), and let \( x \coloneqq f^{-1}(u) \) and \( y \coloneqq f^{-1}(v) \), points of \( A \). Since \( f \circ f^{-1} = \id_{f(A)} \), \( f(x) = u < v = f(y) \). By @prp-strictly-monotone-order-reflecting (a), \( x < y \), that is, \( f^{-1}(u) < f^{-1}(v) \).

(c) Let \( v, x \in \nR \). If \( (v, x) \in \operatorname{graph} f^{-1} \), then \( v \in f(A) \) and \( x = f^{-1}(v) \in A \), and \( f(x) = f(f^{-1}(v)) = v \); so \( (x, v) \in \operatorname{graph} f \). Conversely, if \( (x, v) \in \operatorname{graph} f \), then \( x \in A \) and \( v = f(x) \in f(A) \), and \( f^{-1}(v) = f^{-1}(f(x)) = x \), since \( f^{-1} \circ f = \id_A \); so \( (v, x) \in \operatorname{graph} f^{-1} \). This proves the theorem for strictly increasing \( f \).
:::

::: {.second-reading title="The decreasing case"}
Let \( f \) be strictly decreasing. Part (a) is proved word for word as above, since @fd2:prp-strictly-monotone-injective covers decreasing maps too, and (c) used only \( f \circ f^{-1} = \id_{f(A)} \) and \( f^{-1} \circ f = \id_A \). For (b), let \( u < v \) in \( f(A) \) and \( x \coloneqq f^{-1}(u) \), \( y \coloneqq f^{-1}(v) \). Then \( f(y) = v > u = f(x) \), and @prp-strictly-monotone-order-reflecting (b), applied to the pair \( y, x \), gives \( y < x \), that is, \( f^{-1}(v) < f^{-1}(u) \). So \( f^{-1} \) is strictly decreasing.
:::

The answer to the prompt: totality was used once, inside @prp-strictly-monotone-order-reflecting, where "not \( x < y \)" became \( y \le x \). Each hypothesis has a job. Without "strictly", (a) fails: a constant on \( [0, 1] \) is increasing and not injective. Without cutting the codomain to \( f(A) \), (a) fails as well: \( \sigma \colon \nR \to \nR \) has no inverse, because nothing goes back from \( 1 \).

Part (c) says that the graph of \( f^{-1} \) is the graph of \( f \) reflected in the line \( y = x \), the inverse relation of *Sets and Functions*. To draw an inverse, draw \( f \) and swap the axes.

::: {.check}
Find the image of \( g \) of @exm-mobius-increasing, and its inverse.
:::

::: {.solution}
Writing \( g(x) = 1 - 3/(x + 2) \) shows that \( g \) takes exactly the values in \( (-\infty, 1) \): as \( x \) runs over \( (-2, \infty) \), \( x + 2 \) runs over \( (0, \infty) \), and so does \( 3/(x + 2) \). Solving \( v = (x - 1)/(x + 2) \) gives \( g^{-1}(v) = (1 + 2v)/(1 - v) \) on \( (-\infty, 1) \). Check: with \( x = (1 + 2v)/(1 - v) \), \( x + 2 = 3/(1 - v) > 0 \) and \( x - 1 = 3v/(1 - v) \), so \( g(x) = v \). By @thm-monotone-inverse, \( g^{-1} \) is strictly increasing.
:::

The theorem turns the first half of @lem-reals-nth-root into the statement that roots form a monotone function, and extends roots to negative numbers when the exponent is odd.

::: {#exm-odd-roots}
[Roots as inverse functions]

Let \( n \in \nN \) with \( n \ge 1 \), and let \( p_n \colon \nR \to \nR \), \( p_n(x) = x^n \). Show that the function \( a \mapsto \sqrt[n]{a} \) on \( [0, \infty) \) is strictly increasing, and that for odd \( n \) every real number has exactly one real \( n \)-th root.
:::

::: {.solution}
*On \( [0, \infty) \).* By @lem-reals-nth-root (a), \( p_n \) is strictly increasing on \( [0, \infty) \). Its image is \( [0, \infty) \): a power of a non-negative number is non-negative, and every \( a \ge 0 \) is \( b^n \) for \( b = \sqrt[n]{a} \ge 0 \) (@lem-reals-nth-root (b)). By @thm-monotone-inverse, applied to the restriction of \( p_n \) to \( [0, \infty) \), the inverse \( [0, \infty) \to [0, \infty) \) is strictly increasing, and it sends \( a \) to the unique \( b \ge 0 \) with \( b^n = a \), which is \( \sqrt[n]{a} \).

*Odd \( n \) on \( \nR \).* Let \( n = 2k + 1 \) with \( k \in \nN \). Then \( (-x)^n = \bigl((-x)^2\bigr)^k (-x) = -x^n \) for every real \( x \), by @prp-power-laws-commutative-ring (a), (b) and \( (-x)^2 = x^2 \) (@fd3:prp-ring-algebra (c)). Let \( x < y \). If \( 0 \le x \), then \( x^n < y^n \) by @lem-reals-nth-root (a). If \( y \le 0 \), then \( 0 \le -y < -x \), so \( -y^n = (-y)^n < (-x)^n = -x^n \), and \( x^n < y^n \) (@fd3:prp-ordered-ring-rules (a)). If \( x < 0 < y \), then \( x^n = -(-x)^n < 0 < y^n \), since a power of a positive number is positive. So \( p_n \) is strictly increasing on \( \nR \). Its image is \( \nR \): \( a \ge 0 \) is \( (\sqrt[n]{a})^n \), and \( a < 0 \) is \( \bigl(-\sqrt[n]{-a}\bigr)^n = -(-a) \). By @thm-monotone-inverse, \( p_n \) is a bijection \( \nR \to \nR \) with a strictly increasing inverse. Its value at \( a \) is the **one** real \( s \) with \( s^n = a \); we write it \( \sqrt[n]{a} \), for every real \( a \) when \( n \) is odd. By the formula for the image, \( \sqrt[n]{-a} = -\sqrt[n]{a} \) for \( a \ge 0 \), and so for every real \( a \).
:::

For even \( n \) the second half fails: \( p_2 \) is not injective on \( \nR \), since \( (-1)^2 = 1^2 \), and \( -1 \) is not a value. So \( \sqrt[n]{a} \) for \( a < 0 \) is defined **only for odd** \( n \).

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.4]
  \draw[->] (-1.8,0) -- (1.8,0) node[right] {$x$};
  \draw[->] (0,-1.8) -- (0,1.8) node[above] {$y$};
  \draw[dashed] (-1.6,-1.6) -- (1.6,1.6) node[above right] {$y = x$};
  \draw[thick, domain=-1.17:1.17, samples=60] plot (\x, {\x*\x*\x});
  \node[left] at (1.0,1.55) {$y = x^3$};
  \draw[thick, densely dotted, domain=-1.17:1.17, samples=60] plot ({\x*\x*\x}, \x);
  \node[below] at (1.75,1.05) {$y = \sqrt[3]{x}$};
\end{tikzpicture}
\end{center}
```

*The graphs of \( x \mapsto x^3 \) (solid) and of its inverse \( x \mapsto \sqrt[3]{x} \) (dotted) on \( \nR \), mirror images in the dashed line \( y = x \), as @thm-monotone-inverse (c) says.*

A strictly increasing function on all of \( \nR \) need not have an interval as its image.

::: {#exm-strange-jump}
[A strictly increasing function with a jump]

Let \( H \colon \nR \to \nR \), \( H(x) = x \) for \( x < 0 \) and \( H(x) = x + 1 \) for \( x \ge 0 \). Show that \( H \) is strictly increasing, find its image, and describe \( H^{-1} \).
:::

::: {.solution}
Let \( x < y \). If \( y < 0 \), then \( H(x) = x < y = H(y) \). If \( 0 \le x \), then \( H(x) = x + 1 < y + 1 = H(y) \). If \( x < 0 \le y \), then \( H(x) = x < 0 < 1 \le y + 1 = H(y) \). So \( H \) is strictly increasing.

The image is \( (-\infty, 0) \cup [1, \infty) \): values at \( x < 0 \) are the negative numbers, and values at \( x \ge 0 \) are the numbers \( \ge 1 \). In particular \( 1/2 \) is not a value, though it lies between the values \( H(-1) = -1 \) and \( H(0) = 1 \); the image is not an interval. By @thm-monotone-inverse, \( H^{-1} \colon (-\infty, 0) \cup [1, \infty) \to \nR \), \( H^{-1}(v) = v \) for \( v < 0 \) and \( H^{-1}(v) = v - 1 \) for \( v \ge 1 \), is strictly increasing.
:::

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.8]
  \draw[->] (-3,0) -- (3,0) node[right] {$x$};
  \draw[->] (0,-3) -- (0,3.6) node[above] {$y$};
  \draw[thick] (-2.8,-2.8) -- (-0.07,-0.07);
  \draw (0,0) circle (2.5pt);
  \fill (0,1) circle (2.5pt);
  \draw[thick] (0,1) -- (2.3,3.3);
  \node[left] at (-0.1,1) {$1$};
\end{tikzpicture}
\end{center}
```

*The graph of \( H \): the line \( y = x \) up to the open point \( (0, 0) \), then the line \( y = x + 1 \) from the closed point \( (0, 1) \). The values between \( 0 \) and \( 1 \) are skipped.*

::: {.remark}
[Looking ahead]

*Analysis on the Real Line* proves that a continuous injective function on an interval is strictly monotone. Both words are needed: the swap of @exm-injective-not-monotone lives on an interval but jumps, and \( 1/x \) does not jump but lives on \( \nR \setminus \{0\} \), which is not an interval. The function \( H \) shows that a strictly monotone function may still jump.
:::

## Exercises

### A. Check your understanding

::: {#exr-monotone-functions-and-inverses-a1}
[A1]

These parts are about the proof of @thm-monotone-inverse.

::: {.enumerate options="label=(\alph*)"}
1. Run the proof for \( f(x) = x^2 \) on \( A = [0, 2] \): find \( f(A) \) and \( f^{-1} \), and say what \( x \), \( y \) are in part (b) for \( u = 1 \), \( v = 4 \).
2. Which cited result gives the injectivity in part (a)?
3. Give the idea of the proof of part (b) in two sentences.
:::
:::

::: {.solution}
(a) \( f \) is strictly increasing on \( [0, 2] \) by @lem-reals-nth-root (a). If \( 0 \le x \le 2 \), then \( 0 \le x^2 \le 4 \); and every \( v \in [0, 4] \) is \( (\sqrt v)^2 \) with \( 0 \le \sqrt v \le 2 \), since \( \sqrt v > 2 \) would give \( v > 4 \). So \( f(A) = [0, 4] \), and \( f^{-1} \) is \( \sqrt{\phantom{a}} \) on \( [0, 4] \). For \( u = 1 < 4 = v \): \( x = \sqrt 1 = 1 \), \( y = \sqrt 4 = 2 \), and \( f(1) < f(2) \) gives \( 1 < 2 \).

(b) @fd2:prp-strictly-monotone-injective.

(c) Name the preimages \( x = f^{-1}(u) \), \( y = f^{-1}(v) \), so that \( u < v \) becomes \( f(x) < f(y) \), a statement about \( f \). Strict monotonicity reflects the order, by totality of \( \le \), so \( x < y \).
:::

::: {#exr-monotone-functions-and-inverses-a2}
[A2]

Classify each function as strictly increasing, strictly decreasing, or neither, with a reason: (a) \( x^2 \) on \( [-1, 1] \); (b) \( x^2 \) on \( [0, \infty) \); (c) \( -x^3 \) on \( \nR \); (d) \( 1/x \) on \( (0, \infty) \).
:::

::: {.solution}
(a) Neither: \( -1 < 0 \) with \( 1 > 0 \), so not increasing; \( 0 < 1 \) with \( 0 < 1 \), so not decreasing.

(b) Strictly increasing, by @lem-reals-nth-root (a) with \( n = 2 \).

(c) Strictly decreasing: \( x^3 \) is strictly increasing on \( \nR \) (@fd2:exm-maps-from-calculus (a)), and \( -f \) reverses it (@prp-monotone-algebra (b)).

(d) Strictly decreasing: for \( 0 < x < y \), \( 1/y - 1/x = -(y - x)/(xy) < 0 \), the method with \( Q(x, y) = -1/(xy) < 0 \).
:::

### B. Practice

::: {#exr-monotone-functions-and-inverses-b1}
[B1]

Prove that \( f(x) = x + 1/x \) is strictly increasing on \( [1, \infty) \) and strictly decreasing on \( (0, 1] \).
:::

::: {.solution}
Let \( 0 < x < y \). Over the common denominator \( xy > 0 \),
\[
f(y) - f(x) = (y - x) - \frac{y - x}{xy} = \frac{(y - x)(xy - 1)}{xy} .
\]
So \( Q(x, y) = (xy - 1)/(xy) \), and its sign is the sign of \( xy - 1 \). If \( 1 \le x < y \), then \( xy > x \cdot 1 \ge 1 \) (@fd3:prp-ordered-ring-rules (c)), so \( Q > 0 \) and \( f(x) < f(y) \). If \( 0 < x < y \le 1 \), then \( 0 < xy < 1 \cdot y \le 1 \), so \( Q < 0 \) and \( f(x) > f(y) \).
:::

::: {#exr-monotone-functions-and-inverses-b2}
[B2: Prove or disprove]

Prove each true statement and refute each false one with a counterexample.

::: {.enumerate options="label=(\alph*)"}
1. The composite of two strictly decreasing functions \( \nR \to \nR \) is strictly increasing.
2. If \( f \colon D \to \nR \) is strictly increasing and \( f(x) > 0 \) for all \( x \in D \), then \( 1/f \) is strictly decreasing.
3. The sum of a strictly increasing and a strictly decreasing function on \( \nR \) is monotone.
4. The function \( x \mapsto x^3 - x \) is strictly increasing on \( [1/2, \infty) \).
:::
:::

::: {.solution}
(a) True: @prp-monotone-algebra (e), both strictly decreasing.

(b) True: @prp-monotone-algebra (d).

(c) False. Take \( x^3 \), strictly increasing (@fd2:exm-maps-from-calculus (a)), and \( -x \), strictly decreasing. The sum \( h(x) = x^3 - x \) has \( h(-1) = 0 \), \( h(-1/2) = 3/8 \), \( h(0) = 0 \): it goes up and then down, so it is neither increasing (\( -1/2 < 0 \), \( 3/8 > 0 \)) nor decreasing (\( -1 < -1/2 \), \( 0 < 3/8 \)).

(d) False. The method gives
\[
f(y) - f(x) = (y - x)\bigl(x^2 + xy + y^2 - 1\bigr) ,
\]
and at \( x = 1/2 \), \( y = 3/5 \) the bracket is \( 0.25 + 0.3 + 0.36 - 1 < 0 \). Indeed \( f(1/2) = -3/8 = -375/1000 \) and \( f(3/5) = -48/125 = -384/1000 \), so \( 1/2 < 3/5 \) and \( f(1/2) > f(3/5) \). *Repair:* on \( [1, \infty) \) the statement is true, since \( 1 \le x < y \) gives \( x^2 \ge 1 \), \( xy > 1 \) and \( y^2 > 1 \), so the bracket is \( > 3 - 1 > 0 \).
:::

::: {#exr-monotone-functions-and-inverses-b3}
[B3]

Let \( s \colon \nR \to \nR \), \( s(x) = x\abs{x} \). Prove that \( s \) is strictly increasing, find its image, and write down \( s^{-1} \). Is \( s^{-1} \) increasing?
:::

::: {.solution}
*Strictly increasing,* split as in @exm-squash-function. Let \( x < y \). If \( 0 \le x < y \), then \( s(y) - s(x) = y^2 - x^2 > 0 \) (@lem-reals-nth-root (a)). If \( x < y \le 0 \), then
\[
s(y) - s(x) = -y^2 + x^2 = (x - y)(x + y) > 0 ,
\]
as both factors are negative. If \( x < 0 \le y \), then \( s(x) = -x^2 < 0 \le y^2 = s(y) \).

*Image \( \nR \):* \( v \ge 0 \) is \( s(\sqrt v) \), and \( v < 0 \) is \( s(-\sqrt{-v}) = -(-v) \). So \( s^{-1}(v) = \sqrt v \) for \( v \ge 0 \) and \( s^{-1}(v) = -\sqrt{-v} \) for \( v < 0 \): this is the inverse whose two composites were checked in *Sets and Functions* (@fd2:exm-two-sided-inverses (c)). It is strictly increasing by @thm-monotone-inverse, with no further computation.
:::

### C. Going deeper

::: {#exr-monotone-functions-and-inverses-c1}
[C1: Find the error]

Here is an argument that \( f(x) = x^3 - 3x \) is strictly increasing on \( [1, \infty) \).

(i) Let \( 1 \le x < y \).
(ii) By the method of @exm-method-factor-difference, \( f(y) - f(x) = (y - x)(y^2 + xy + x^2 - 3) \).
(iii) Since \( x \ge 1 \) and \( y \ge 1 \), we get \( y^2 + xy + x^2 \ge 3 \).
(iv) Also \( y - x > 0 \), so \( f(y) - f(x) > 0 \).

Is the conclusion true? Does the argument prove it? Name the line that fails, if any, and repair it.
:::

::: {.solution}
The conclusion is true, but the argument does not prove it. Line (iv) fails: (iii) gives only that the bracket is \( \ge 0 \), and a positive number times a non-negative one is only \( \ge 0 \). A counterexample to the step: \( 1 \cdot 0 = 0 \). This is the usual failure named in @exm-method-factor-difference, strictness concluded from \( Q \ge 0 \).

*Repair.* Line (i) gives more than (iii) uses: \( y > x \ge 1 \), so \( y^2 > 1 \) (@lem-reals-nth-root (a)), while \( x^2 \ge 1 \) and \( xy \ge x \ge 1 \). Hence \( y^2 + xy + x^2 > 3 \), the bracket is \( > 0 \), and (iv) holds.
:::

::: {#exr-monotone-functions-and-inverses-c2}
[C2, used later]

Let \( f \colon \nR \to \nR \) be increasing, with \( f(f(x)) = x \) for every \( x \in \nR \). Prove that \( f = \id_{\nR} \). Then show that "increasing" cannot be dropped.
:::

::: {.solution}
[Hint 1]

Fix \( x \), and split by the sign of \( f(x) - x \).
:::

::: {.solution}
[Hint 2]

Suppose \( f(x) > x \), and apply \( f \) to both sides.
:::

::: {.solution}
Let \( x \in \nR \). By trichotomy, \( f(x) > x \), \( f(x) < x \) or \( f(x) = x \).

If \( x < f(x) \), then, \( f \) being increasing, \( f(x) \le f(f(x)) = x \), against \( x < f(x) \). If \( f(x) < x \), then \( f(f(x)) \le f(x) \), that is, \( x \le f(x) \), against \( f(x) < x \). So \( f(x) = x \) for every \( x \), and \( f = \id_{\nR} \) by @fd2:prp-function-equality.

Without "increasing" the claim fails: \( x \mapsto -x \) satisfies \( -(-x) = x \) for every \( x \), and it is not the identity, since it sends \( 1 \) to \( -1 \).

**Marking scheme.** (10 points)
- 2: fixes an arbitrary \( x \) and splits into the three cases of trichotomy.
- 3: in the case \( f(x) > x \), applies the monotonicity of \( f \) to the inequality between \( x \) and \( f(x) \) and uses \( f(f(x)) = x \) to reach a contradiction.
- 2: handles the case \( f(x) < x \), or says that it is symmetric with the reason.
- 1: concludes \( f = \id_{\nR} \) from equality at every point.
- 2: gives a function with \( f \circ f = \id_{\nR} \), \( f \ne \id_{\nR} \), and checks both properties.

Fatal errors (0 for the step): applying \( f \) to a strict inequality and keeping it strict (\( f \) is only increasing); assuming \( f \) is injective or continuous without proof.
:::

<!-- dependency ledger
def-monotone-function (claim): the negation of "increasing on A"; not (P -> Q) is P and not Q | fd1:prp-quantifier-negation, cited; the propositional law from fd1, inline
def-monotone-function (claim): increasing gives x <= y => f(x) <= f(y) | inline (x <= y means x < y or x = y)
def-monotone-function (example): the indicator of [0, oo) is increasing | fd2:def-indicator, inline case check
exm-method-factor-difference (claim): sign of (y - x)Q is the sign of Q when y - x > 0 | fd3:prp-ordered-ring-rules (c), (d), cited
exm-mobius-increasing (example): (y - 1)(x + 2) - (x - 1)(y + 2) = 3(y - x) | verify/ch08/exm-mobius-increasing.py
exm-mobius-increasing (example): a product of positive elements is positive | (O4), named; fd3:def-ordered-ring-and-field
exm-squash-function (example): the two difference formulas; sigma(v/(1 - |v|)) = v | verify/ch08/exm-squash-function.py; image cited from fd2:exm-fraction-map
exm-squash-function (example): 1/((1 + x)(1 + y)) > 0 when x, y >= 0 | fd3:prp-reciprocal-order (a), (O4); inline
prp-monotone-algebra (proof): increasing gives x <= y => f(x) <= f(y) (used in (e)) | remark after def-monotone-function, inline
prp-strictly-monotone-order-reflecting (proof): f(x) < f(y) and f(y) <= f(x) is impossible | antisymmetry of the total order, fd3:prp-ordered-field-halves (a)
prp-strictly-monotone-order-reflecting (claim): (quick check) in a partial order elements may be incomparable | fd2:def-partial-order, prose only
exm-injective-not-monotone (example): the swap satisfies f(f(x)) = x | inline (three cases)
thm-monotone-inverse (claim): (aftermath) the graph of f^{-1} is the inverse relation | fd2 (Sets and Functions, the inverse relation of a bijection), named in prose; nothing rests on it
thm-monotone-inverse (claim): (quick check) image of g is (-oo, 1); g^{-1}(v) = (1 + 2v)/(1 - v) | verify/ch08/exm-mobius-increasing.py
exm-odd-roots (example): a power of a non-negative (positive) real is non-negative (positive) | the first fact in the proof of lem-reals-nth-root (induction with fd3:prp-ordered-ring-rules (c)), cited
exm-odd-roots (example): (-x)^(2k+1) = ((-x)^2)^k (-x) = -x^(2k+1); (-x)^2 = x^2 | prp-power-laws-commutative-ring (a), (b), fd3:prp-ring-algebra (c), cited; verify/ch08/exm-odd-roots.py
exm-odd-roots (example): every n >= 1 odd is 2k + 1 with k in N | the meaning of "odd" (fd3:cor-integers-even-odd), inline
exm-strange-jump (example): image (-oo, 0) u [1, oo); H^{-1} | inline case check; verify/ch08/exm-strange-jump.py
exr-monotone-functions-and-inverses-a1 (solution): f([0, 2]) = [0, 4] | lem-reals-nth-root (a), (b), fd3:prp-cof-square-roots; inline
exr-monotone-functions-and-inverses-b1 (solution): difference formula (y - x)(xy - 1)/(xy) | verify/ch08/exr-monotone-functions-and-inverses-b1.py
exr-monotone-functions-and-inverses-b2 (solution): h(-1), h(-1/2), h(0); f(1/2) = -3/8, f(3/5) = -48/125; bracket 0.91 | verify/ch08/exr-monotone-functions-and-inverses-b2.py
exr-monotone-functions-and-inverses-b3 (solution): s(-sqrt(-v)) = v; s difference on x < y <= 0 | verify/ch08/exr-monotone-functions-and-inverses-b3.py; inverse checks cited from fd2:exm-two-sided-inverses (c)
exr-monotone-functions-and-inverses-c1 (solution): f(y) - f(x) = (y - x)(y^2 + xy + x^2 - 3) | verify/ch08/exr-monotone-functions-and-inverses-c1.py
exr-monotone-functions-and-inverses-c2 (solution): trichotomy on R | fd3:prp-ordered-field-halves (a), not cited by label in the solution; inline
-->
