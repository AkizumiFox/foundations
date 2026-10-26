# Working in an Ordered Field

<!-- S3: style revision per S1 change list (layout-proposal.md §3, 4.1, pipeline S): delete B2; cite each rule letter once per idea. -->

Section 2.3 proved the rules for inequalities from the order axioms, and Section 3.2 added the one rule that needs division: reciprocals reverse order. A limit argument asks for a few more. It halves a tolerance, so it needs \( 0 < \varepsilon/2 < \varepsilon \); it subtracts fractions, so it needs \( 1/b - 1/d = (d - b)/(bd) \); and above all it measures how far apart two numbers are, so it needs the absolute value and the triangle inequality. Each of these is a few lines from the rules we have. This section proves them once, in an arbitrary ordered field, and the rest of the chapter uses them on nearly every page.

## The standing setup

Throughout this chapter, \( F \) is an **ordered field** (@def-ordered-ring-and-field): a field with a relation \( < \) satisfying (O1)–(O4). The rationals are one, by @thm-rationals-ordered-field, and for most of the chapter they are the one that matters: the next chapter applies these results first with \( F = \nQ \), to build the real numbers from Cauchy sequences of rationals, and then again with \( F = \nR \), once \( \nR \) is shown to be an ordered field. We state results for a general \( F \) because the proofs never use anything about \( \nQ \) beyond (F1)–(F9) and (O1)–(O4), and saying so on the page makes it checkable.

We use the results of Sections 2.3 and 3.2 by their letters, without restating them: the algebra of a commutative ring (@prp-ring-algebra), the rules for inequalities (@prp-ordered-ring-rules (a)–(i)), and the reversal of order by reciprocals (@prp-reciprocal-order). In a field \( 1 \ne 0 \), so @prp-ordered-ring-rules (e) gives \( 1 > 0 \) in every ordered field. We write
\[
F_{>0} \coloneqq \{ x \in F : x > 0 \} , \qquad F_{\ge 0} \coloneqq \{ x \in F : x \ge 0 \} ,
\]
so that \( \nQ_{>0} \) of Section 3.2 is the case \( F = \nQ \). Recall that \( a/b \coloneqq a b^{-1} \) for \( b \ne 0 \), so \( 1/b = b^{-1} \), and that \( 2 \coloneqq 1 + 1 \) and \( x^2 \coloneqq x x \) (@prp-ring-algebra (d)).

## Fractions

School algebra adds fractions by cross-multiplying and subtracts reciprocals by a common denominator. Both are identities in any field, and the second is how we will compare \( 1/b_n \) with \( 1/b \) in Section 4.4. The only point needing care is that a product of non-zero elements is non-zero, so that \( bd \) may stand in a denominator.

::: {#lem-field-fraction-rules}
[Fraction Rules in a Field]

Let \( F \) be a field (@def-commutative-ring-and-field), and let \( a, b, c, d \in F \) with \( b \ne 0 \) and \( d \ne 0 \).

::: {.enumerate options="label=(\alph*)"}
1. \( b^{-1} \) is the **only** element \( y \) with \( b y = 1 \), and \( (b^{-1})^{-1} = b \). Moreover \( bd \ne 0 \) and \( (bd)^{-1} = b^{-1} d^{-1} \).
2. \( \dfrac{a}{b} + \dfrac{c}{d} = \dfrac{ad + bc}{bd} \) and \( \dfrac{a}{b} \cdot \dfrac{c}{d} = \dfrac{ac}{bd} \).
3. \( \dfrac{1}{b} - \dfrac{1}{d} = \dfrac{d - b}{bd} \).
4. For **all** \( x, y \in F \): if \( xy = 0 \), then \( x = 0 \) or \( y = 0 \).
:::
:::

::: {.idea}
Everything rests on one move from Section 2.3: to identify an element, show it satisfies the **defining equation** of the element you want and let uniqueness finish. The product \( b^{-1} d^{-1} \) satisfies the defining equation of \( (bd)^{-1} \); once \( bd \) is known to be a legal denominator, (b) and (c) are bookkeeping with (F5), (F6) and (F9).
:::

::: {.proof}
(a) Suppose \( by = 1 \). Then
\[
y = 1 \cdot y = (b^{-1} b) y = b^{-1} (b y) = b^{-1} \cdot 1 = b^{-1} ,
\]
by (F7), (F8) with (F6), (F5), the hypothesis, and (F7); this is the uniqueness argument of @prp-ring-algebra (a), run with multiplication. Next, \( b^{-1} \ne 0 \): otherwise \( 1 = b b^{-1} = b \cdot 0 = 0 \) by @prp-ring-algebra (b), against \( 1 \ne 0 \). So \( (b^{-1})^{-1} \) exists, and since \( b^{-1} b = b b^{-1} = 1 \) by (F6), the element \( b \) satisfies its defining equation; uniqueness gives \( (b^{-1})^{-1} = b \). Now, by (F5) and (F6),
\[
(bd)(b^{-1} d^{-1}) = (b b^{-1})(d d^{-1}) = 1 \cdot 1 = 1 .
\]
If \( bd = 0 \), the left side would be \( 0 \cdot (b^{-1} d^{-1}) = 0 \) by @prp-ring-algebra (b) and (F6), so \( 1 = 0 \), which is false in a field. Hence \( bd \ne 0 \), and the display says that \( b^{-1} d^{-1} \) satisfies the defining equation of \( (bd)^{-1} \); by uniqueness, \( (bd)^{-1} = b^{-1} d^{-1} \).

(b) By (a), \( bd \ne 0 \), so both right-hand sides are defined. For the product, by (F5), (F6) and (a),
\[
\begin{aligned}
\frac{a}{b} \cdot \frac{c}{d} &= (a b^{-1})(c d^{-1}) = (ac)(b^{-1} d^{-1}) \\
&= (ac)(bd)^{-1} = \frac{ac}{bd} .
\end{aligned}
\]
For the sum, first \( \dfrac{ad}{bd} = (ad)(b^{-1} d^{-1}) = (a b^{-1})(d d^{-1}) = \dfrac{a}{b} \), and likewise \( \dfrac{bc}{bd} = \dfrac{c}{d} \). Then (F9) with (F6) gives
\[
\begin{aligned}
\frac{a}{b} + \frac{c}{d} &= (ad)(bd)^{-1} + (bc)(bd)^{-1} \\
&= (ad + bc)(bd)^{-1} = \frac{ad + bc}{bd} .
\end{aligned}
\]

(c) Apply the sum rule of (b) with \( a = 1 \) and \( c = -1 \). Since \( (-1) d^{-1} = -(d^{-1}) \) by @prp-ring-algebra (c), the left side is \( 1/b + (-1)/d = 1/b - 1/d \), and the numerator on the right is \( 1 \cdot d + b(-1) = d - b \), again by @prp-ring-algebra (c).

(d) Let \( xy = 0 \), and suppose \( x \ne 0 \). Then \( y = 1 \cdot y = (x^{-1} x) y = x^{-1} (xy) = x^{-1} \cdot 0 = 0 \), by (F7), (F8), (F5) and @prp-ring-algebra (b). So \( x = 0 \) or \( y = 0 \). This proves the lemma.
:::

In an ordered field, (d) is also @prp-ordered-ring-rules (f). The point of (d) here is that it needs **no** order: a field has no zero divisors. The commutative ring of integers modulo \( 6 \), in the warning after @def-commutative-ring-and-field, has them (\( [2][3] = [0] \) with \( [2] \ne [0] \ne [3] \)), so by (d) it is not a field.

## Halving and comparing

The commonest move in a limit proof is to give each of two terms half the tolerance. That needs \( \varepsilon/2 \) to be positive, smaller than \( \varepsilon \), and to add up to \( \varepsilon \) with itself. The next proposition collects these facts with two comparisons we will need as often.

::: {#prp-ordered-field-halves}
[Halves and Comparisons in an Ordered Field]

Let \( F \) be an ordered field.

::: {.enumerate options="label=(\alph*)"}
1. \( \le \) is a total order on \( F \) (@fd2:def-partial-order), and its strict part is \( < \).
2. \( 2 \coloneqq 1 + 1 > 0 \). For every \( \varepsilon \in F_{>0} \),
\[
0 < \frac{\varepsilon}{2} < \varepsilon \qquad \text{and} \qquad \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon .
\]
For all \( a, b \in F \) with \( a < b \), \( a < \dfrac{a + b}{2} < b \).
3. For \( a, b \in F_{>0} \): if \( a \le b \), then \( \dfrac{1}{b} \le \dfrac{1}{a} \).
4. For \( a, b, c, d \in F \): if \( 0 \le a \le b \) and \( 0 \le c \le d \), then \( ac \le bd \).
:::
:::

::: {.idea}
Nothing new happens: each part is one or two of the rules of Sections 2.3 and 3.2 in sequence. The only care needed is with \( \le \), which hides an "or": each non-strict hypothesis splits into an equality case and a strict case, and the strict rules apply only to the second.
:::

::: {.proof}
(a) This is @prp-ordered-ring-rules (i).

(b) Since \( 1 > 0 \), (O3) gives \( 2 = 1 + 1 > 0 + 1 = 1 \), and \( 2 > 0 \) by (O2). So \( 2 \ne 0 \), and \( 2^{-1} > 0 \) by @prp-reciprocal-order (a). For \( \varepsilon > 0 \), \( \varepsilon/2 = \varepsilon \cdot 2^{-1} > 0 \) by (O4). By (F9) and (F7),
\[
\begin{aligned}
\frac{\varepsilon}{2} + \frac{\varepsilon}{2} &= \varepsilon \cdot 2^{-1} \cdot 1 + \varepsilon \cdot 2^{-1} \cdot 1 \\
&= (\varepsilon \cdot 2^{-1})(1 + 1) = \varepsilon (2^{-1} \cdot 2) = \varepsilon ,
\end{aligned}
\]
the third equality by (F5) and (F6). Adding \( \varepsilon/2 \) to \( 0 < \varepsilon/2 \) by (O3) gives \( \varepsilon/2 < \varepsilon/2 + \varepsilon/2 = \varepsilon \). For the midpoint, let \( a < b \). By (O3), \( a + a < a + b \) and \( a + b < b + b \), and \( a + a = a(1 + 1) = 2a \), \( b + b = 2b \) by (F7), (F9), (F6). Multiplying by \( 2^{-1} > 0 \) (@prp-ordered-ring-rules (c)) gives \( a < (a + b)/2 < b \), since \( (2a) 2^{-1} = a (2 \cdot 2^{-1}) = a \).

(c) If \( a = b \), then \( 1/b = 1/a \). Otherwise \( 0 < a < b \), and \( 1/b < 1/a \) by @prp-reciprocal-order (b). In both cases \( 1/b \le 1/a \).

(d) First, \( ac \le bc \): if \( a = b \) or \( c = 0 \), the two sides are equal (for \( c = 0 \) both are \( 0 \) by @prp-ring-algebra (b)); otherwise \( a < b \) and \( c > 0 \), and \( ac < bc \) by @prp-ordered-ring-rules (c). Next, \( bc \le bd \), by the same argument with the roles of the factors exchanged by (F6): \( c \le d \), and \( b \ge 0 \) since \( 0 \le a \le b \) (transitivity, part (a)). By transitivity of \( \le \) (part (a)), \( ac \le bd \).
:::

Part (b) is used whenever a proof splits a tolerance: the sum of two quantities, each below \( \varepsilon/2 \), is below \( \varepsilon \), by @prp-ordered-ring-rules (b). The midpoint is the same fact read for two points: between any two elements of \( F \) lies a third. Part (d) is how a product of two small, or two bounded, quantities is estimated.

::: {.warning}
The non-negativity in (d) cannot be dropped. In \( \nQ \), take \( a = c = -2 \) and \( b = d = 0 \): then \( a \le b \) and \( c \le d \), but \( ac = 4 \) and \( bd = 0 \), and \( 4 \le 0 \) is false. Section 2.3 gave a strict version of the same trap (the warning after @prp-ordered-ring-rules). Before multiplying two inequalities, check that both sides are non-negative.
:::

## Absolute value

To say that \( x \) is close to \( a \), we want one element of \( F \) measuring the gap between them, whichever of the two is larger. In school this is \( \abs{x - a} \), and \( \abs{x} \) is sometimes written \( \sqrt{x^2} \). That formula needs a square-root function, and an ordered field has none in general: no rational squares to \( 2 \) (@thm-no-rational-square-two). The square \( x^2 \) does have the two square roots \( x \) and \( -x \), and picking the non-negative one is already a definition by cases. So we define the absolute value by cases, using only the order.

*The absolute value of \( x \) is \( x \) with its sign made non-negative.*

::: {#def-absolute-value-ordered-field}
[Absolute Value in an Ordered Field]

Let \( F \) be an ordered field. For \( x \in F \), the **absolute value** of \( x \) is
\[
\abs{x} \coloneqq
\begin{cases}
x & \text{if } x \ge 0 , \\
-x & \text{if } x < 0 .
\end{cases}
\]
For \( x, y \in F \), the element \( \abs{x - y} \) is the **distance** from \( x \) to \( y \).
:::

The two cases do not overlap and cover \( F \), by trichotomy (O1), so \( \abs{x} \) is a well-defined element of \( F \). The map \( x \mapsto \abs{x} \) is a function \( F \to F \).

**Examples.** In \( \nQ \), \( \abs{3/4} = 3/4 \) and \( \abs{-3/4} = 3/4 \), the second because \( -3/4 < 0 \) (@thm-rationals-ordered-field (a): \( (-3) \cdot 1 < 0 \cdot 4 \)) and \( -(-3/4) = 3/4 \) (@prp-ring-algebra (a)). The distance from \( 1/3 \) to \( 1/2 \) is \( \abs{1/3 - 1/2} = \abs{-1/6} = 1/6 \). The degenerate case is \( \abs{0} = 0 \), from the first clause. Part (a) below shows that \( 0 \) is the only element with absolute value \( 0 \), so the distance from \( x \) to \( y \) is \( 0 \) exactly when \( x = y \).

**A non-example by minimal change.** Replace the definition by \( x \mapsto x^2 \). This map is also non-negative, zero only at \( 0 \), and multiplicative, so it passes (a) and the product rule of (b) below. It fails the triangle inequality (e): in \( \nQ \), with \( x = y = 1 \), the "size" of \( x + y \) would be \( 2^2 = 4 \), while the sizes of \( x \) and \( y \) add up to \( 1 + 1 = 2 \). A measure of size must not grow faster than its argument, and that is the clause the square breaks.

::: {#prp-absolute-value-ordered-field}
[Rules for the Absolute Value]

Let \( F \) be an ordered field, and let \( x, y, z, r \in F \).

::: {.enumerate options="label=(\alph*)"}
1. \( \abs{x} \ge 0 \), and \( \abs{x} = 0 \) if and only if \( x = 0 \).
2. \( \abs{-x} = \abs{x} \), \( \abs{xy} = \abs{x} \abs{y} \) and \( \abs{x}^2 = x^2 \); if \( x \ne 0 \), then \( \abs{1/x} = 1/\abs{x} \).
3. \( -\abs{x} \le x \le \abs{x} \).
4. \( \abs{x} \le r \) if and only if \( -r \le x \le r \); and \( \abs{x} < r \) if and only if \( -r < x < r \).
5. *(Triangle inequality.)* \( \abs{x + y} \le \abs{x} + \abs{y} \), and \( \abs{x - z} \le \abs{x - y} + \abs{y - z} \).
6. *(Reverse triangle inequality.)* \( \bigl| \abs{x} - \abs{y} \bigr| \le \abs{x - y} \).
:::
:::

::: {.idea}
Parts (a)–(d) are case checks on the sign of \( x \) (and of \( y \)). The triangle inequality then needs **no** cases: by (c), \( x \) and \( y \) are each trapped between \( \pm \) their absolute values; adding the two traps traps \( x + y \) between \( \pm (\abs{x} + \abs{y}) \), and (d) reads that as the inequality. The reverse triangle inequality is the triangle inequality applied to \( x = (x - y) + y \) and to \( y = (y - x) + x \).
:::

::: {.proof}
(a) If \( x \ge 0 \), then \( \abs{x} = x \ge 0 \). If \( x < 0 \), then \( \abs{x} = -x > 0 \) by @prp-ordered-ring-rules (a), since \( -0 = 0 \). So \( \abs{x} \ge 0 \) always, and \( \abs{x} = 0 \) only in the first case with \( x = 0 \); conversely \( \abs{0} = 0 \).

(b) *Negation.* If \( x > 0 \), then \( -x < 0 \) (@prp-ordered-ring-rules (a)), so \( \abs{-x} = -(-x) = x = \abs{x} \) (@prp-ring-algebra (a)). If \( x = 0 \), both sides are \( 0 \). If \( x < 0 \), then \( -x > 0 \), so \( \abs{-x} = -x = \abs{x} \).

*Product.* If \( x \ge 0 \) and \( y \ge 0 \), then \( xy \ge 0 \) (by (O4), or @prp-ring-algebra (b) if a factor is \( 0 \)), so \( \abs{xy} = xy = \abs{x}\abs{y} \). If \( x \ge 0 \) and \( y < 0 \), then \( -y > 0 \), and \( x(-y) = -(xy) \) by @prp-ring-algebra (c), so \( \abs{x}\abs{y} = x(-y) = -(xy) \); and \( -(xy) \ge 0 \) by the first case, so \( xy \le 0 \) and \( \abs{xy} = -(xy) \) (if \( xy = 0 \), both readings give \( 0 \)). The case \( x < 0 \le y \) is the same with the roles exchanged. If \( x < 0 \) and \( y < 0 \), then \( xy = (-x)(-y) > 0 \) by @prp-ring-algebra (c) and (O4), so \( \abs{xy} = xy = (-x)(-y) = \abs{x}\abs{y} \).

*Square.* \( \abs{x}^2 \) is \( x x \) or \( (-x)(-x) \), and both are \( x^2 \) by @prp-ring-algebra (c).

*Reciprocal.* Let \( x \ne 0 \). By the product rule, \( \abs{x} \, \abs{1/x} = \abs{x \cdot x^{-1}} = \abs{1} = 1 \), and \( \abs{x} \ne 0 \) by (a). So \( \abs{1/x} \) satisfies the defining equation of \( \abs{x}^{-1} \), and @lem-field-fraction-rules (a) gives \( \abs{1/x} = 1/\abs{x} \).

(c) If \( x \ge 0 \), then \( -\abs{x} = -x \le 0 \le x = \abs{x} \), using @prp-ordered-ring-rules (a) for \( -x \le 0 \). If \( x < 0 \), then \( -\abs{x} = -(-x) = x \), and \( x < 0 < -x = \abs{x} \). In both cases \( -\abs{x} \le x \le \abs{x} \), by transitivity (@prp-ordered-ring-rules (i)).

(d) \( (\Rightarrow) \) Let \( \abs{x} \le r \). By (c), \( x \le \abs{x} \le r \). By (c) and (b) applied to \( -x \), \( -x \le \abs{-x} = \abs{x} \le r \), and negating reverses the inequality (@prp-ordered-ring-rules (a), or equality), so \( -r \le x \). \( (\Leftarrow) \) Let \( -r \le x \le r \). If \( x \ge 0 \), then \( \abs{x} = x \le r \). If \( x < 0 \), then \( \abs{x} = -x \le r \), by negating \( -r \le x \). The strict version is the same argument with \( < \) in place of \( \le \) at the steps that involve \( r \): for instance \( x \le \abs{x} < r \) gives \( x < r \) by @prp-ordered-ring-rules (i).

(e) By (c), \( -\abs{x} \le x \le \abs{x} \) and \( -\abs{y} \le y \le \abs{y} \). Adding (@prp-ordered-ring-rules (b)),
\[
-\bigl(\abs{x} + \abs{y}\bigr) \le x + y \le \abs{x} + \abs{y} ,
\]
where \( (-\abs{x}) + (-\abs{y}) = -(\abs{x} + \abs{y}) \) by uniqueness of negatives (@prp-ring-algebra (a)). By (d) with \( r \coloneqq \abs{x} + \abs{y} \), \( \abs{x + y} \le \abs{x} + \abs{y} \). For the second form, apply the first to \( x - z = (x - y) + (y - z) \).

(f) By (e), \( \abs{x} = \abs{(x - y) + y} \le \abs{x - y} + \abs{y} \), so \( \abs{x} - \abs{y} \le \abs{x - y} \) by (O3). Exchanging \( x \) and \( y \), and using \( \abs{y - x} = \abs{-(x - y)} = \abs{x - y} \) from (b), gives \( \abs{y} - \abs{x} \le \abs{x - y} \). So \( -\abs{x - y} \le -(\abs{y} - \abs{x}) \) by @prp-ordered-ring-rules (a) (or equality), and \( -(\abs{y} - \abs{x}) = \abs{x} - \abs{y} \) by uniqueness of negatives (@prp-ring-algebra (a)), since \( (\abs{y} - \abs{x}) + (\abs{x} - \abs{y}) = 0 \); that is, \( -\abs{x - y} \le \abs{x} - \abs{y} \). By (d), \( \bigl| \abs{x} - \abs{y} \bigr| \le \abs{x - y} \). This proves the proposition.
:::

The form of (d) that the rest of the chapter uses is about a distance. Apply the strict half of (d) to \( x - a \) with \( r = \varepsilon \), and add \( a \) throughout by (O3); the step is reversible, since adding \( -a \) (by (O3) again) goes back, and \( (x - a) + a = x \):
\[
\abs{x - a} < \varepsilon \iff a - \varepsilon < x < a + \varepsilon .
\]
In words: \( x \) lies within \( \varepsilon \) of \( a \) exactly when it lies strictly between \( a - \varepsilon \) and \( a + \varepsilon \). In Section 4.3 the role of \( x \) is played by the terms \( a_n \) of a sequence and \( a \) is a candidate limit.

**Example.** In \( \nQ \), which \( x \) satisfy \( \abs{x - 1/2} < 1/4 \)? By the display above, exactly those with \( 1/2 - 1/4 < x < 1/2 + 1/4 \), that is, \( 1/4 < x < 3/4 \). So \( 2/3 \) qualifies (\( 1 \cdot 3 = 3 < 8 = 2 \cdot 4 \) and \( 2 \cdot 4 = 8 < 9 = 3 \cdot 3 \), by the comparison formula of @thm-rationals-ordered-field (a)) and \( 3/4 \) does not: the inequality is strict, and \( \abs{3/4 - 1/2} = 1/4 \).

::: {.check}
Is \( \abs{a} - \abs{b} \le \abs{a - b} \) for all \( a, b \in F \)? Is \( \abs{a - b} \le \abs{a} - \abs{b} \) for all \( a, b \in F \)?
:::

::: {.solution}
The first: yes. By (f) and (c), \( \abs{a} - \abs{b} \le \bigl| \abs{a} - \abs{b} \bigr| \le \abs{a - b} \). The second: no. In \( \nQ \), take \( a = 0 \) and \( b = 1 \): then \( \abs{a - b} = \abs{-1} = 1 \), while \( \abs{a} - \abs{b} = -1 \), and \( 1 \le -1 \) is false.
:::

The triangle inequality is the tool of the whole chapter. In its second form it says that a detour through a third point \( y \) cannot shorten the way from \( x \) to \( z \). Run backwards, it turns two small distances, from \( x \) to \( y \) and from \( y \) to \( z \), into one small distance from \( x \) to \( z \). That is the move of almost every proof in Sections 4.3–4.5.

::: {.remark}
The same two-case formula appears in *Logic and Proof*, Chapter 1, for the school numbers, and in *Analysis on the Real Line*, Chapter 1, for \( \nR \). Here it is defined, and its rules are proved, for an arbitrary ordered field, from (F1)–(F9) and (O1)–(O4) alone.
:::

## Exercises

### A. Check your understanding

::: {#exr-rules-and-absolute-value-a1}
[A1]

Let \( F \) be an ordered field.

::: {.enumerate options="label=(\alph*)"}
1. Here is a proof that \( 0 < 1/2 < 1 \) in \( F \): (1) \( 1 > 0 \); (2) \( 2 = 1 + 1 > 1 > 0 \); (3) \( 0 < 1/2 < 1/1 = 1 \). Name the rule behind each of the three steps.
2. True or false in every ordered field: "if \( a < b \), then \( a^2 < b^2 \)". Give a reason, or a counterexample in \( \nQ \).
3. True or false in every ordered field: "if \( \abs{a} < \abs{b} \), then \( a < b \)". Give a reason, or a counterexample in \( \nQ \).
4. True or false in every ordered field: "\( x^2 + 1 > 0 \) for every \( x \)". Give a reason, or a counterexample in \( \nQ \).
:::
:::

::: {.solution}
(a) (1) @prp-ordered-ring-rules (e), since \( 1 \ne 0 \) in a field. (2) \( 1 + 1 > 0 + 1 = 1 \) by (O3) (or @prp-ordered-ring-rules (b), strict), then \( 2 > 0 \) by (O2). (3) @prp-reciprocal-order (b), applied to \( 0 < 1 < 2 \); and \( 1/1 = 1 \cdot 1^{-1} = 1 \), since \( 1 \) is its own inverse (\( 1 \cdot 1 = 1 \), and @lem-field-fraction-rules (a)).

(b) False. In \( \nQ \), \( -2 < 1 \), but \( (-2)^2 = 4 > 1 = 1^2 \). The true statement needs \( a, b \ge 0 \): @prp-ordered-ring-rules (g).

(c) False. In \( \nQ \), \( a = 1 \) and \( b = -2 \) give \( \abs{a} = 1 < 2 = \abs{b} \), but \( a = 1 > -2 = b \).

(d) True. By @prp-ordered-ring-rules (e), \( x^2 > 0 \) if \( x \ne 0 \), and \( x^2 = 0 \) if \( x = 0 \) (@prp-ring-algebra (b)); so \( x^2 \ge 0 \). Also \( 1 > 0 \). Hence \( x^2 + 1 > 0 + 0 = 0 \) by @prp-ordered-ring-rules (b), strict in the second summand.
:::

### B. Practice

::: {#exr-rules-and-absolute-value-b1}
[B1: Two companions of (c) and (d)]

Let \( F \) be an ordered field.

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( 0 \le a < b \) and \( 0 < c \le d \), then \( ac < bd \).
2. Prove that for \( a, b \in F_{>0} \), \( a \le b \) **if and only if** \( 1/b \le 1/a \).
:::

Name the rule behind each step.
:::

::: {.solution}
(a) Since \( 0 \le a < b \), \( b > 0 \) by @prp-ordered-ring-rules (i). First, \( ac < bc \): \( a < b \) and \( c > 0 \), so @prp-ordered-ring-rules (c) applies. Next, \( bc \le bd \): if \( c = d \) the two sides are equal; otherwise \( c < d \) and \( b > 0 \), so \( cb < db \) by @prp-ordered-ring-rules (c), that is, \( bc < bd \) by (F6). Combining \( ac < bc \le bd \) by @prp-ordered-ring-rules (i) gives \( ac < bd \).

(b) \( (\Rightarrow) \) is @prp-ordered-field-halves (c). \( (\Leftarrow) \) Let \( 1/b \le 1/a \). Both are positive, by @prp-reciprocal-order (a). Applying @prp-ordered-field-halves (c) to the positive elements \( 1/b \le 1/a \) gives \( 1/(1/a) \le 1/(1/b) \), and \( 1/(1/a) = (a^{-1})^{-1} = a \), \( 1/(1/b) = b \) by @lem-field-fraction-rules (a). So \( a \le b \).
:::

::: {#exr-rules-and-absolute-value-b2}
[B2: Solving an inequality]

In an ordered field \( F \), find all \( x \) with \( \abs{2x - 3} < 5 \), naming the rule behind each step. Here \( 3 \), \( 5 \), \( 8 \) and so on denote the multiples \( 3 \cdot 1 \), \( 5 \cdot 1 \), \( 8 \cdot 1 \), … of Section 2.3 (defined before @prp-ordered-ring-rules), and \( 2 = 1 + 1 = 2 \cdot 1 \).
:::

::: {.solution}
We use the sum law of @prp-ordered-ring-rules (h), \( (m + k) \cdot 1 = m \cdot 1 + k \cdot 1 \); in particular \( 5 + 3 = 8 \), \( 2 + 3 = 5 \) and \( 4 + 4 = 8 \) hold in \( F \) because they hold in \( \nN \).

By @prp-absolute-value-ordered-field (d), strict form, \( \abs{2x - 3} < 5 \) if and only if
\[
-5 < 2x - 3 < 5 .
\]
Adding \( 3 \) throughout is reversible (add \( -3 \) to go back), so by (O3) this holds if and only if \( -5 + 3 < 2x < 5 + 3 \). Here \( 5 + 3 = 8 \), and \( -5 + 3 = -(2 + 3) + 3 = -2 \), using \( -(2 + 3) = (-2) + (-3) \) (uniqueness of negatives, @prp-ring-algebra (a)). So the condition is \( -2 < 2x < 8 \).

Multiplying by \( 1/2 > 0 \) (@prp-ordered-field-halves (b)) is reversible too (multiply by \( 2 > 0 \) to go back), so by @prp-ordered-ring-rules (c) the condition is equivalent to \( (-2)/2 < x < 8/2 \). Now \( 2/2 = 1 \), so \( (-2)/2 = -(2/2) = -1 \) by @prp-ring-algebra (c). And \( 8 = 4 + 4 = 4(1 + 1) \) by (F7) and (F9), the field product of the elements \( 4 \) and \( 2 \), so \( 8/2 = 4 (2/2) = 4 \) by (F5). Hence
\[
\abs{2x - 3} < 5 \iff -1 < x < 4 .
\]
Check at an endpoint: \( x = 4 \) gives \( \abs{8 - 3} = 5 \), not \( < 5 \), as the strict inequality predicts.
:::

::: {#exr-rules-and-absolute-value-b3}
[B3: Two more triangle inequalities]

Prove that for all \( a, b, c \) in an ordered field,

::: {.enumerate options="label=(\alph*)"}
1. \( \abs{a + b + c} \le \abs{a} + \abs{b} + \abs{c} \);
2. \( \bigl| \abs{a} - \abs{b} \bigr| \le \abs{a + b} \).
:::
:::

::: {.solution}
(a) By @prp-absolute-value-ordered-field (e) twice, \( \abs{(a + b) + c} \le \abs{a + b} + \abs{c} \le (\abs{a} + \abs{b}) + \abs{c} \), the second step by adding \( \abs{c} \) to \( \abs{a + b} \le \abs{a} + \abs{b} \) (@prp-ordered-ring-rules (b)). Conclude by transitivity (@prp-ordered-ring-rules (i)).

(b) Apply @prp-absolute-value-ordered-field (f) to \( a \) and \( -b \): \( \bigl| \abs{a} - \abs{-b} \bigr| \le \abs{a - (-b)} \). By @prp-absolute-value-ordered-field (b), \( \abs{-b} = \abs{b} \), and \( a - (-b) = a + b \) by @prp-ring-algebra (a). This is the claim.
:::

### C. Going deeper

::: {#exr-rules-and-absolute-value-c1}
[C1: A field that cannot be ordered]

::: {.enumerate options="label=(\alph*)"}
1. Prove that in an ordered field no \( x \) satisfies \( x^2 = -1 \).
2. Deduce that if a field contains an element \( i \) with \( i^2 = -1 \), then no relation \( < \) makes it an ordered field.
:::
:::

::: {.solution}
[Hint 1]

Which sign does a square have, and which sign does \( -1 \) have?
:::

::: {.solution}
[Hint 2]

Show first that \( x^2 \ge 0 \) for every \( x \), splitting on whether \( x = 0 \).
:::

::: {.solution}
(a) Let \( F \) be an ordered field and \( x \in F \). If \( x = 0 \), then \( x^2 = 0 \) (@prp-ring-algebra (b)); if \( x \ne 0 \), then \( x^2 > 0 \) (@prp-ordered-ring-rules (e)). So \( x^2 \ge 0 \). On the other hand \( 1 > 0 \) (@prp-ordered-ring-rules (e), as \( 1 \ne 0 \) in a field), so \( -1 < 0 \) by @prp-ordered-ring-rules (a). If \( x^2 = -1 \), then \( 0 \le x^2 = -1 < 0 \), so \( 0 < 0 \) by @prp-ordered-ring-rules (i), against (O1).

(b) If some relation \( < \) made the field an ordered field, then (a), applied to that ordered field, would forbid \( i^2 = -1 \). So no such relation exists.

The complex numbers of *Analytic Preliminaries*, Chapter 1 contain such an \( i \), so they form a field that cannot be ordered. Compare @exm-finite-ring-not-orderable, where the obstacle was \( 1 + 1 = 0 \); here it is that \( -1 \) is a square.

**Marking scheme.** (10 points)
- 4: shows \( x^2 \ge 0 \) for every \( x \) (cases \( x = 0 \), \( x \ne 0 \)), or rules out \( x = 0 \) for the \( x \) with \( x^2 = -1 \) and then shows \( x^2 > 0 \), giving the rule for each step.
- 2: shows \( -1 < 0 \) from \( 1 > 0 \) (justified by \( 1 \ne 0 \) and @prp-ordered-ring-rules (e), or by citing the standing remark of Section 4.1) and from negation reversing order.
- 2: derives the contradiction with trichotomy (O1) or irreflexivity.
- 2: (b) states that any order would make (a) apply, so none exists.
Fatal errors (0 for the step): asserting \( x^2 > 0 \) for all \( x \) (false at \( 0 \)) and then using strictness; asserting \( 1 > 0 \) with no justification (accept \( 1 \ne 0 \) with @prp-ordered-ring-rules (e), or the standing remark of Section 4.1); using properties of \( \nR \) or of \( \sqrt{\ } \).
:::

::: {#exr-rules-and-absolute-value-c2}
[C2: Maximum and minimum through the absolute value]

For \( a, b \) in an ordered field \( F \), let \( \max\{a, b\} \) be \( b \) if \( a \le b \) and \( a \) otherwise, and \( \min\{a, b\} \) be \( a \) if \( a \le b \) and \( b \) otherwise.

::: {.enumerate options="label=(\alph*)"}
1. Prove that
\[
\max\{a, b\} = \frac{a + b + \abs{a - b}}{2} , \qquad \min\{a, b\} = \frac{a + b - \abs{a - b}}{2} .
\]
2. Deduce that \( \abs{x} = \max\{x, -x\} \) for every \( x \in F \).
:::
:::

::: {.solution}
(a) *Case \( a \le b \).* Then \( a - b \le 0 \) (@prp-ordered-ring-rules (a), or equality), so \( \abs{a - b} = b - a \): by the second clause of @def-absolute-value-ordered-field if \( a - b < 0 \), and because both sides are \( 0 \) if \( a = b \). Hence
\[
\frac{a + b + \abs{a - b}}{2} = \frac{a + b + b - a}{2} = \frac{2b}{2} = b = \max\{a, b\} ,
\]
and likewise \( \dfrac{a + b - (b - a)}{2} = \dfrac{2a}{2} = a = \min\{a, b\} \), using \( b + b = 2b \) and \( (2b) 2^{-1} = b \) as in the proof of @prp-ordered-field-halves (b).

*Case \( b < a \).* Then \( a - b > 0 \), so \( \abs{a - b} = a - b \), and the two formulas give \( (2a)/2 = a = \max\{a, b\} \) and \( (2b)/2 = b = \min\{a, b\} \).

(b) By (a) with \( a = x \) and \( b = -x \): \( \max\{x, -x\} = \bigl(x + (-x) + \abs{2x}\bigr)/2 = \abs{2x}/2 \). By @prp-absolute-value-ordered-field (b), \( \abs{2x} = \abs{2}\abs{x} = 2\abs{x} \), since \( 2 > 0 \). So \( \max\{x, -x\} = \abs{x} \).
:::

<!-- dependency ledger
lem-field-fraction-rules (proof): (F5)-(F9) and 1 != 0 in a field, used by clause name | def-commutative-ring-and-field (cited in the statement)
lem-field-fraction-rules (claim): the integers modulo 6 have zero divisors [2][3] = [0] | F3.2 warning after def-commutative-ring-and-field (cited; illustration only, nothing depends on it)
prp-ordered-field-halves (proof): (2a) 2^{-1} = a(2 2^{-1}) = a | def-commutative-ring-and-field (F5), (F6), (F8); inline
prp-ordered-field-halves (claim): the strict version of the warning is F3.2's warning after prp-ordered-ring-rules | F3.2 §03 (pointer, not used)
prp-absolute-value-ordered-field (proof): -0 = 0 | F3.2 proof of prp-order-from-positives (one line there: 0 + 0 = 0); inline
prp-absolute-value-ordered-field (proof): (-a) + (-b) = -(a + b) | prp-ring-algebra (a) (cited; uniqueness of negatives)
prp-absolute-value-ordered-field (proof): -(b - a) = a - b (used in (f) for |y - x| = |-(x - y)|), (c - b) + (b - a) = c - a (used in (e) for x - z = (x - y) + (y - z)), and (x - y) + y = x (used in (f) and in the display after the proof) | F3.2 proof of prp-order-from-positives (first display and the line after it, by (F1)-(F4) and prp-ring-algebra (a)); inline
def-absolute-value-ordered-field (example): x - y = 0 iff x = y | F3.2 proof of prp-order-from-positives (one line there: (F4) and (b - a) + a = b); inline
prp-absolute-value-ordered-field (proof): 1 is its own inverse, |1| = 1 | (F7) and def-absolute-value-ordered-field with 1 > 0; inline
prp-absolute-value-ordered-field (claim): the display |x - a| < eps iff a - eps < x < a + eps: adding a throughout an equivalence is reversible | def-ordered-ring-and-field (O3), applied with a and with -a
def-absolute-value-ordered-field (example): 1/3 - 1/2 = -1/6, 1/2 - 1/4 = 1/4, 1/2 + 1/4 = 3/4 in Q | def-rational-operations; verify/ch04/def-absolute-value-ordered-field.py
def-absolute-value-ordered-field (claim): remark: same absolute value as F1.1 (school) and AN1.1 (R) | prose pointers; nothing depends on them
exr-rules-and-absolute-value-a1 (solution): numerals (-2)^2 = 4 in Q | prp-ring-algebra (c); verify/ch04/exr-rules-and-absolute-value-a1.py
exr-rules-and-absolute-value-b2 (solution): 5 + 3 = 8, 2 + 3 = 5, 4 + 4 = 8 in N, carried to F by the sum law | thm-omega-arithmetic-laws, def-omega-arithmetic (numerals; F3.1), with prp-ordered-ring-rules (h) (cited); verify/ch04/exr-rules-and-absolute-value-b2.py
exr-rules-and-absolute-value-c1 (solution): the complex numbers contain i with i^2 = -1 | fd4 Chapter 1 (prose pointer; nothing depends on it)
-->
