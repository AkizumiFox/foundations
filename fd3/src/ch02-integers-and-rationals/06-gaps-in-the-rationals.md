# The Gaps in the Rationals

The rationals now have everything Section 10.5 asked of them: they form an ordered field (@thm-rationals-ordered-field), every rational lies below a natural number (@thm-rationals-archimedean), and no two rationals are neighbors, since their midpoint lies between them. Is anything missing? School geometry suggests an answer. The diagonal of a square with side \( 1 \) has a length whose square is \( 2 \), and no fraction seems to measure it. That picture is motivation only. This section proves the two facts behind it from the construction: no rational squares to \( 2 \), and the set of rationals whose square is below \( 2 \) has no least upper bound in \( \nQ \). We also build a sequence of rationals that closes in on the gap from above without ever landing in it. A later chapter of this volume fills the gap.

## No rational squares to two

Throughout, \( x^2 \coloneqq x \cdot x \) and \( 2 \coloneqq 1 + 1 \), with \( 4 = 2 \cdot 2 \) and so on; by the identifications of Sections 10.2 and 10.4 these are the natural numbers of the same names. Their sums and products may be computed in \( \nN \), since the maps \( \iota \) and \( j \) preserve \( + \) and \( \cdot \) (@prp-naturals-embed-integers, @prp-integers-embed-rationals), and so may their comparisons (@thm-integers-ordered-ring (a), @thm-rationals-ordered-field (b)).

Chapter 2 proved that "\( \sqrt 2 \) is irrational" (@thm-sqrt2-irrational), about the school rationals, by parity: an argument about even and odd integers. Parity for the constructed \( \nZ \) is not yet available (a later chapter of this volume develops division with remainder), so we prove the statement for the constructed \( \nQ \) by a different route, one that needs only the order and the least-element property of \( \nZ \).

::: {#thm-no-rational-square-two}
[No Rational Squares to Two]

There is no \( x \in \nQ \) with \( x^2 = 2 \).
:::

::: {.idea}
Work backwards from a supposed square root \( x = p/q \). From \( x^2 = 2 \) we get \( 2 - x = x^2 - x = x(x - 1) \), so
\[
x = \frac{2 - x}{x - 1} = \frac{2 - p/q}{p/q - 1} = \frac{2q - p}{p - q} .
\]
Since \( 1 < x < 2 \) (as \( 1^2 < 2 < 2^2 \)), the new denominator \( p - q \) is positive and smaller than \( q \). So no fraction for \( x \) can have a **least** positive denominator, while @prp-integer-least-element says some fraction must. The written proof checks the descent with integers only: it never divides, and it verifies \( (2q - p)^2 = 2(p - q)^2 \) by expanding. *Before reading on: why is \( q' > 0 \), and why is \( q' < q \)?*
:::

::: {.proof}
Suppose, for a contradiction, that \( x \in \nQ \) and \( x^2 = 2 \). Then \( x \ne 0 \), since \( 0^2 = 0 \) (@prp-ring-algebra (b)) and \( 2 > 0 \). By (O1), \( x > 0 \) or \( x < 0 \); let \( y \coloneqq x \) in the first case and \( y \coloneqq -x \) in the second. Then \( y > 0 \) (@prp-ordered-ring-rules (a)) and \( y^2 = x^2 = 2 \), because \( (-x)(-x) = x x \) (@prp-ring-algebra (c)).

By @prp-integers-embed-rationals (b), \( y = a/b \) with \( a \in \nZ \) and \( b \in \nZ_{>0} \), and \( a > 0 \) by @thm-rationals-ordered-field (a). By @def-rational-operations, \( y^2 = a^2/b^2 \), and \( 2 = 2/1 \), so \( y^2 = 2 \) says \( a^2 \cdot 1 = 2 b^2 \) (@prp-integers-embed-rationals (b)). Hence the set
\[
D \coloneqq \{ q \in \nZ_{>0} : p^2 = 2q^2 \text{ for some } p \in \nZ_{>0} \}
\]
contains \( b \), so it is non-empty, and \( 0 \) is a lower bound of it. By @prp-integer-least-element, \( D \) has a least element \( q \). Choose \( p \in \nZ_{>0} \) with \( p^2 = 2q^2 \).

*\( q < p \).* Suppose \( p \le q \). Since \( p \ge 0 \), @prp-ordered-ring-rules (g) gives \( p^2 \le q^2 \), that is, \( q^2 + q^2 \le q^2 \), and adding \( -q^2 \) (O3) gives \( q^2 \le 0 \). But \( q \ne 0 \), so \( q^2 > 0 \) by @prp-ordered-ring-rules (e). This contradicts (O1), so \( p \le q \) fails, and \( q < p \) by totality (@prp-ordered-ring-rules (i)).

*\( p < 2q \).* Suppose \( 2q \le p \). Since \( 2q \ge 0 \), (g) gives \( (2q)^2 \le p^2 \), that is, \( 2q^2 + 2q^2 = 4q^2 \le 2q^2 \), so \( 2q^2 \le 0 \). But \( 2q^2 > 0 \) by (O4). As before, \( p < 2q \).

*Descent.* Let \( p' \coloneqq 2q - p \) and \( q' \coloneqq p - q \), integers. By @prp-ordered-ring-rules (a), \( p < 2q \) gives \( p' > 0 \), and \( q < p \) gives \( q' > 0 \); so \( p', q' \in \nZ_{>0} \) (@thm-integers-ordered-ring (b)). Adding \( -q \) to \( p < 2q \) (O3) gives \( q' = p - q < q \). Expanding with @prp-ring-algebra (c) and (d),
\[
\begin{aligned}
p'^2 - 2q'^2 &= (4q^2 - 4pq + p^2) - (2p^2 - 4pq + 2q^2) \\
&= 2q^2 - p^2 = 0 .
\end{aligned}
\]
So \( p'^2 = 2q'^2 \) with \( p' \in \nZ_{>0} \), that is, \( q' \in D \). But \( q' < q \), and \( q \) is the least element of \( D \). This contradiction shows that no \( x \in \nQ \) has \( x^2 = 2 \).
:::

The answer to the prompt: \( q' = p - q > 0 \) because \( q < p \), and \( q' < q \) because \( p < 2q \). These are the two inequalities "\( 1 < x < 2 \)" of the Idea, written for integers; the hypotheses \( p^2 = 2q^2 \) and \( q \) least are each used once.

::: {.remark}
The proof assumes \( x^2 = 2 \), reaches a contradiction, and concludes \( \neg(\exists x \in \nQ \; x^2 = 2) \): its last step is \( \rulename{\neg I} \) (@def-rules-negation), not RAA (@def-rule-raa), since what is refuted is the assumption and the conclusion is its negation. The steps "\( q < p \)" and "\( p < 2q \)" refute \( p \le q \) and \( 2q \le p \) and then read the remaining case off trichotomy.
:::

## The set below the gap

Section 7.6 stated, without proof, that the set of positive rationals with square below \( 2 \) has no least upper bound in \( \nQ \), and pointed out that the ambient set decides whether a supremum exists. We now prove it. By @prp-ordered-ring-rules (i) and @thm-rationals-ordered-field, \( \le \) is a total order on \( \nQ \), so \( (\nQ, \le) \) is a partially ordered set and the words of Section 7.6 apply: upper bounds (@def-order-bounds) and a supremum, an upper bound \( s \) with (S1) \( x \le s \) for every \( x \) in the set and (S2) \( s \le u \) for every upper bound \( u \) (@def-order-supremum).

::: {#thm-rationals-gap-sqrt2}
[A Bounded Set of Rationals with No Rational Supremum]

Let
\[
A \coloneqq \{ x \in \nQ : x^2 < 2 \} , \qquad A^+ \coloneqq \{ x \in A : x > 0 \} = \{ x \in \nQ : x > 0, \ x^2 < 2 \} .
\]

::: {.enumerate options="label=(\alph*)"}
1. \( A \) is non-empty and bounded above in \( (\nQ, \le) \), but \( A \) has no supremum in \( \nQ \).
2. \( A \) and \( A^+ \) have the same upper bounds in \( \nQ \). Hence \( A^+ \) is also non-empty and bounded above, and has no supremum in \( \nQ \).
:::
:::

*Try it first (ten minutes): a rational \( s > 0 \) is offered as \( \sup A \). Find a rational that proves the offer wrong, once in the case \( s^2 < 2 \) and once in the case \( s^2 > 2 \).*

::: {.idea}
If \( s^2 < 2 \), we need an element of \( A \) above \( s \). The obvious try is \( s + h \) with \( h > 0 \) small, but \( (s + h)^2 = s^2 + 2sh + h^2 \) has an \( h^2 \) in it, and taming that needs a separate size estimate on \( h \). If \( s^2 > 2 \), we need a smaller upper bound, and a guess \( s - h \) runs into the same algebra.

A cleaner idea finds the new rational in one formula. If \( s^2 > 2 \), then \( 2/s < s \) and \( (2/s)^2 = 4/s^2 < 2 \): the gap lies between \( 2/s \) and \( s \). Their average
\[
t(s) \coloneqq \frac{1}{2}\Bigl( s + \frac{2}{s} \Bigr) = \frac{s^2 + 2}{2s}
\]
is smaller than \( s \), and its square is still above \( 2 \); that is the smaller upper bound. If \( s^2 < 2 \), apply the same trick from the other side: \( t(s) \) overshoots, so \( u(s) \coloneqq 2/t(s) = 4s/(s^2 + 2) \) undershoots, and it lands above \( s \). Each claim is an identity in the field \( \nQ \), checked by clearing denominators. The proof uses @thm-no-rational-square-two exactly once, to rule out the third case \( s^2 = 2 \).
:::

::: {.proof}
(a) *Non-empty:* \( 1^2 = 1 < 2 \), so \( 1 \in A \). *Bounded above:* \( 2 \) is an upper bound. Indeed, let \( x \in A \), and suppose \( x > 2 \). Then \( 0 \le 2 < x \), so \( 4 = 2^2 < x^2 \) by @prp-ordered-ring-rules (g), and \( 2 < 4 \), so \( 2 < x^2 \), against \( x^2 < 2 \) by (O1). So \( x \le 2 \), by totality.

*Two maps.* For \( s \in \nQ_{>0} \), we have \( 2s > 0 \) by (O4), and \( s^2 + 2 > 0 \) by @prp-ordered-ring-rules (e) and (b); both are non-zero. Let
\[
t(s) \coloneqq \frac{s^2 + 2}{2s} , \qquad u(s) \coloneqq \frac{4s}{s^2 + 2} .
\]
Both are rationals, and both are positive, by @prp-reciprocal-order (a) and (O4). They satisfy
\[
\begin{aligned}
t(s)^2 - 2 &= \frac{(s^2 - 2)^2}{4s^2} , & s - t(s) &= \frac{s^2 - 2}{2s} , \\
u(s) - s &= \frac{s(2 - s^2)}{s^2 + 2} , & 2 - u(s)^2 &= \frac{2(s^2 - 2)^2}{(s^2 + 2)^2} .
\end{aligned}
\]{#eq-newton-identities}
Each identity is checked by multiplying both sides by its denominator, which is non-zero, so that the multiplication can be undone with the inverse. For the first, \( 2s \cdot t(s) = s^2 + 2 \), so \( 4s^2 (t(s)^2 - 2) = (s^2 + 2)^2 - 8s^2 = s^4 - 4s^2 + 4 = (s^2 - 2)^2 \). For the second, \( 2s(s - t(s)) = 2s^2 - (s^2 + 2) = s^2 - 2 \). For the third, \( (s^2 + 2)(u(s) - s) = 4s - s^3 - 2s = s(2 - s^2) \). For the fourth, \( (s^2 + 2)^2 (2 - u(s)^2) = 2(s^2 + 2)^2 - 16s^2 = 2(s^2 - 2)^2 \).

*No supremum.* Suppose, for a contradiction, that \( s \in \nQ \) is a supremum of \( A \). By (S1) and \( 1 \in A \), \( s \ge 1 > 0 \), so \( s \in \nQ_{>0} \). By @thm-no-rational-square-two, \( s^2 \ne 2 \), so by (O1), \( s^2 < 2 \) or \( s^2 > 2 \). In both cases \( s^2 - 2 \ne 0 \), so \( (s^2 - 2)^2 > 0 \) by @prp-ordered-ring-rules (e).

*Case 1: \( s^2 < 2 \).* Then \( 2 - s^2 > 0 \), and the third identity of @eq-newton-identities exhibits \( u(s) - s \) as a product of positive elements (with @prp-reciprocal-order (a) for the reciprocal), so \( u(s) > s \). The fourth gives \( 2 - u(s)^2 > 0 \), so \( u(s)^2 < 2 \) and \( u(s) \in A \). So \( A \) has an element \( u(s) > s \), and \( s \) is not an upper bound of \( A \), against (S1).

*Case 2: \( s^2 > 2 \).* The first identity gives \( t(s)^2 - 2 > 0 \), so \( t(s)^2 > 2 \). Then \( t(s) \) is an upper bound of \( A \): if some \( x \in A \) had \( x > t(s) \), then \( 0 < t(s) < x \) would give \( 2 < t(s)^2 < x^2 \) by @prp-ordered-ring-rules (g), against \( x^2 < 2 \); so \( x \le t(s) \) for every \( x \in A \). By (S2), \( s \le t(s) \). But the second identity, with \( s^2 - 2 > 0 \) and \( 2s > 0 \), gives \( s - t(s) > 0 \), that is, \( t(s) < s \). Then \( t(s) < s \le t(s) \), so \( t(s) < t(s) \), against (O1).

Both cases are impossible, so \( A \) has no supremum in \( \nQ \).

(b) Since \( A^+ \subseteq A \), every upper bound of \( A \) is an upper bound of \( A^+ \). Conversely, let \( u \) be an upper bound of \( A^+ \). Since \( 1 > 0 \) and \( 1^2 < 2 \), \( 1 \in A^+ \), so \( u \ge 1 > 0 \). Let \( x \in A \). If \( x > 0 \), then \( x \in A^+ \) and \( x \le u \). Otherwise \( x \le 0 < u \) (@prp-ordered-ring-rules (i)). So \( u \) is an upper bound of \( A \).

Conditions (S1) and (S2) for a set mention only the set of its upper bounds: (S1) says that \( s \) is one, and (S2) that it lies below all of them. So \( s \) is a supremum of \( A^+ \) if and only if it is a supremum of \( A \), and by (a), \( A^+ \) has none. It is non-empty, since \( 1 \in A^+ \), and bounded above, by \( 2 \).
:::

The set \( A^+ \) is the set of Section 7.6, so clause (b) is the statement left unproved there. The two descriptions differ only by the non-positive elements of \( A \), which lie below every upper bound anyway.

::: {.remark}
Chapter 11 proves the same conclusion for \( A^+ \) in \( \nQ \), as part of its motivation for the axioms of the real numbers, and then shows that \( A^+ \) does have a supremum in the real numbers. That is the sense of "gap": a bounded set of rationals whose least upper bound, if it is anywhere, is not a rational.
:::

::: {.warning}
"\( A \) has no supremum in \( \nQ \), so \( A \) is unbounded" mixes up the two conditions a supremum needs. \( A \) is bounded above, by \( 2 \) for instance; what fails is (S2): among the rational upper bounds there is no least one, because every upper bound \( s \) is beaten by the smaller upper bound \( t(s) \).
:::

## A rational sequence aimed at the gap

The map \( t \) does more than refute a candidate. Started at an upper bound, it produces a smaller one, and it can be applied again. Iterating it gives a sequence of rationals that approaches the gap from above.

::: {#exm-newton-rationals-sqrt2}
[A Rational Sequence Aimed at the Gap]

For \( s \in \nQ_{>0} \) let \( t(s) \coloneqq (s^2 + 2)/(2s) \). Define \( x_0 \coloneqq 2 \) and \( x_{n+1} \coloneqq t(x_n) \) for \( n \in \nN \), and let \( e_n \coloneqq x_n^2 - 2 \). Show that this defines a sequence with \( x_n \in \nQ_{>0} \) for every \( n \in \nN \), and that for every \( n \in \nN \):

::: {.enumerate options="label=(\roman*)"}
1. \( e_n > 0 \), that is, \( x_n^2 > 2 \);
2. \( e_{n+1} = e_n^2/(4x_n^2) \le e_n^2/8 \);
3. \( x_n - x_{n+1} = e_n/(2x_n) > 0 \), so \( x_{n+1} < x_n \).
:::

Compute \( x_0, \dots, x_3 \) and \( e_0, \dots, e_3 \).
:::

::: {.solution}
*The sequence.* For \( s \in \nQ_{>0} \), \( s^2 + 2 > 0 \) and \( 2s > 0 \), so \( t(s) \in \nQ_{>0} \) by (O4) and @prp-reciprocal-order (a): \( t \) maps \( \nQ_{>0} \) to \( \nQ_{>0} \). The recursion theorem (@thm-recursion, read on \( \nN = \omega \) as @thm-omega-recursion by @cor-omega-identification (b)), with \( X = \nQ_{>0} \), starting value \( 2 \) and \( g(n, s) \coloneqq t(s) \), gives exactly one function \( n \mapsto x_n \) from \( \nN \) to \( \nQ_{>0} \) with \( x_0 = 2 \) and \( x_{n+1} = t(x_n) \). So every \( x_n \) is a positive rational, with no further argument.

*Two identities.* For \( s \in \nQ_{>0} \), \( 2s \cdot t(s) = s^2 + 2 \). Hence \( 4s^2 (t(s)^2 - 2) = (s^2 + 2)^2 - 8s^2 = (s^2 - 2)^2 \) and \( 2s (s - t(s)) = 2s^2 - s^2 - 2 = s^2 - 2 \). Multiplying by the inverses of \( 4s^2 \ne 0 \) and \( 2s \ne 0 \),
\[
t(s)^2 - 2 = \frac{(s^2 - 2)^2}{4s^2} , \qquad s - t(s) = \frac{s^2 - 2}{2s} .
\]{#eq-newton-step}

*(i).* We use @ax-induction (read on \( \omega \) as @thm-omega-induction (b), by @cor-omega-identification (b)) for \( P(n) \): \( e_n > 0 \). Base \( P(0) \): \( e_0 = 2^2 - 2 = 2 > 0 \). Step: suppose \( e_n > 0 \). By @eq-newton-step with \( s = x_n \),
\[
e_{n+1} = t(x_n)^2 - 2 = \frac{e_n^2}{4x_n^2} .
\]
Here \( e_n^2 > 0 \) by @prp-ordered-ring-rules (e), since \( e_n \ne 0 \), and \( 1/(4x_n^2) > 0 \) by @prp-reciprocal-order (a); so \( e_{n+1} > 0 \) by (O4). This proves (i) for every \( n \).

*(ii).* The equation was just shown, for every \( n \). By (i), \( x_n^2 > 2 \), so \( 4x_n^2 > 4 \cdot 2 = 8 \) by @prp-ordered-ring-rules (c). From \( 0 < 8 < 4x_n^2 \), @prp-reciprocal-order (b) gives \( 1/(4x_n^2) < 1/8 \), and multiplying by \( e_n^2 > 0 \) (@prp-ordered-ring-rules (c)) gives \( e_{n+1} < e_n^2/8 \); in particular \( e_{n+1} \le e_n^2/8 \).

*(iii).* By @eq-newton-step with \( s = x_n \), \( x_n - x_{n+1} = e_n/(2x_n) \), a product of the positive elements \( e_n \) and \( 1/(2x_n) \); so it is positive, and \( x_{n+1} < x_n \) by @prp-ordered-ring-rules (a).

*The first terms.* By the definition of \( t \),
\[
x_1 = \frac{4 + 2}{4} = \frac{3}{2} , \quad
x_2 = \frac{9/4 + 2}{3} = \frac{17}{12} , \quad
x_3 = \frac{289/144 + 2}{17/6} = \frac{577}{408} .
\]
The errors are \( e_0 = 2 \), \( e_1 = 9/4 - 2 = 1/4 \), \( e_2 = 289/144 - 2 = 1/144 \) and \( e_3 = 577^2/408^2 - 2 = 1/166464 \), since \( 577^2 = 332929 = 2 \cdot 166464 + 1 \) and \( 408^2 = 166464 \). As a check on (ii): \( e_1 = 2^2/(4 \cdot 4) = 1/4 \), \( e_2 = (1/16)/9 = 1/144 \), and \( e_3 = (1/144)^2 / (4 \cdot 289/144) = 1/(144 \cdot 1156) = 1/166464 \).
:::

For orientation only (decimals are not part of this volume's toolkit), here are the terms in school decimals:

| \( n \) | \( x_n \) | \( e_n = x_n^2 - 2 \) | \( x_n \), roughly |
|---|---|---|---|
| \( 0 \) | \( 2 \) | \( 2 \) | \( 2 \) |
| \( 1 \) | \( 3/2 \) | \( 1/4 \) | \( 1.5 \) |
| \( 2 \) | \( 17/12 \) | \( 1/144 \) | \( 1.41667 \) |
| \( 3 \) | \( 577/408 \) | \( 1/166464 \) | \( 1.414216 \) |

The terms decrease, every one of them is an upper bound of \( A \) (a positive rational whose square exceeds \( 2 \), as in Case 2 of the proof above), and by (ii) the error is roughly squared at each step: after three steps, \( e_3 = 1/166464 \) is already below \( 1/100000 \). The terms crowd together. Yet no rational \( L \) can be "the number they approach", for if they approached \( L \), their squares would approach \( L^2 \), and the errors \( e_n \) force \( L^2 = 2 \), which @thm-no-rational-square-two forbids. This paragraph is a picture, not a proof: limits in \( \nQ \) have not been defined. A later chapter of this volume defines them, with \( \varepsilon \in \nQ_{>0} \), and proves that this sequence is Cauchy in \( \nQ \) yet has no limit in \( \nQ \), citing (i)–(iii) from this example.

::: {.check}
Is \( 3/2 \) an upper bound of \( A = \{ x \in \nQ : x^2 < 2 \} \)? Is \( 17/12 \)?
:::

::: {.solution}
Both are. Each is positive, and \( (3/2)^2 = 9/4 > 2 \) because \( 9 > 8 \), while \( (17/12)^2 = 289/144 > 2 \) because \( 289 > 288 \) (the comparison formula, @thm-rationals-ordered-field (a)). A positive rational \( b \) with \( b^2 > 2 \) bounds \( A \): if \( x \in A \) had \( x > b \), then \( x^2 > b^2 > 2 \) by @prp-ordered-ring-rules (g), against \( x^2 < 2 \). (These are \( x_1 \) and \( x_2 \) of @exm-newton-rationals-sqrt2, and \( 17/12 = t(3/2) \) is the smaller upper bound that Case 2 of the proof of @thm-rationals-gap-sqrt2 produces from \( s = 3/2 \).)
:::

This chapter built two number systems by one method. From \( \nN \) to \( \nZ \): pairs \( (a, b) \), identified when \( a + d = b + c \), so that subtraction becomes possible. From \( \nZ \) to \( \nQ \): pairs \( (p, q) \) with \( q > 0 \), identified when \( ps = rq \), so that division becomes possible. Each time an operation was defined on representatives and checked to be well defined (@thm-well-defined-on-classes), and each axiom was reduced to the level below. The third step, from \( \nQ \) to the real numbers, takes the same route in a later chapter of this volume: the representatives are sequences of rationals like the one above, identified when their difference tends to \( 0 \), so that the gap found in this section, and every other gap of \( \nQ \), is filled.

## Exercises

### A. Check your understanding

::: {#exr-gaps-in-the-rationals-a1}
[A1]

These questions are about the proof of @thm-rationals-gap-sqrt2.

::: {.enumerate options="label=(\alph*)"}
1. Where is @thm-no-rational-square-two used, and what would go wrong without it?
2. Run the proof on \( s = 3/2 \) and on \( s = 7/5 \): which case applies, which rational does the proof produce, and why does it refute \( s \)?
3. Let \( F \) be an ordered field containing an element \( r > 0 \) with \( r^2 = 2 \), and let \( A_F \coloneqq \{ x \in F : x^2 < 2 \} \). Which step of the proof fails for \( A_F \), and what happens to \( t(r) \) and \( u(r) \)?
4. State the idea of the proof in two sentences.
:::
:::

::: {.solution}
(a) Once, right after a supposed supremum \( s \) is fixed: it excludes \( s^2 = 2 \), so that trichotomy leaves the two cases \( s^2 < 2 \) and \( s^2 > 2 \). Without it there is a third case, in which neither map helps: \( (s^2 - 2)^2 = 0 \), so the identities give \( u(s) = s \) and \( t(s) = s \).

(b) For \( s = 3/2 \): \( s^2 = 9/4 > 2 \) (as \( 9 > 8 \)), so Case 2. The proof produces \( t(3/2) = (9/4 + 2)/3 = 17/12 \), an upper bound of \( A \), since \( (17/12)^2 = 289/144 > 2 \); and \( 17/12 < 3/2 \), since \( 17 \cdot 2 = 34 < 36 = 3 \cdot 12 \). So \( 3/2 \) is not the **least** upper bound. For \( s = 7/5 \): \( s^2 = 49/25 < 2 \) (as \( 49 < 50 \)), so Case 1. The proof produces
\[
u(7/5) = \frac{28/5}{49/25 + 2} = \frac{28/5}{99/25} = \frac{140}{99} ,
\]
which lies in \( A \), since \( 140^2 = 19600 < 19602 = 2 \cdot 99^2 \), and exceeds \( 7/5 \), since \( 140 \cdot 5 = 700 > 693 = 7 \cdot 99 \). So \( 7/5 \) is not an upper bound.

(c) The step "\( s^2 \ne 2 \)": in \( F \) the candidate \( s = r \) satisfies \( r^2 = 2 \), and it falls in neither case. Indeed \( r \) is the supremum of \( A_F \) in \( F \): it is an upper bound (if \( x > r > 0 \), then \( x^2 > 2 \)), and an upper bound \( v < r \) would have \( v > 0 \) (as \( 1 \in A_F \)) and \( v^2 < 2 \), and then \( u(v) \in A_F \) with \( u(v) > v \), as in Case 1. The maps fix \( r \): \( t(r) = (2 + 2)/(2r) = 2/r = r \), since \( r \cdot r = 2 \), and \( u(r) = 4r/4 = r \).

(d) Suppose a rational \( s \) were the supremum; since no rational squares to \( 2 \), either \( s^2 < 2 \) or \( s^2 > 2 \). The explicit rationals \( u(s) \) and \( t(s) \) then give, respectively, an element of the set above \( s \) or an upper bound below \( s \), so \( s \) fails (S1) or (S2).
:::

### B. Practice

::: {#exr-gaps-in-the-rationals-b1}
[B1: Put the proof in order]

Here are lines of a proof of @thm-no-rational-square-two, shuffled, together with two lines that do not belong. Write the lines of a correct proof in a correct order, and say what is wrong with each line you leave out.

(i) Set \( p' \coloneqq 2q - p \) and \( q' \coloneqq p - q \); both are positive integers, by the two inequalities between \( p \) and \( q \).

(ii) Write \( x = p/q \) with \( p, q \in \nZ_{>0} \); then \( p^2 = 2q^2 \).

(iii) Since \( p^2 = 2q^2 \), we have \( p < q \).

(iv) Since \( q' = p - q < q \), this contradicts the choice of \( q \); so no rational squares to \( 2 \).

(v) Suppose \( x \in \nQ \) has \( x^2 = 2 \); replacing \( x \) by \( -x \) if necessary, take \( x > 0 \).

(vi) \( p < 2q \), since \( p \ge 2q \) would give \( p^2 \ge 4q^2 > 2q^2 \).

(vii) Choose such an \( x \) with the least positive value.

(viii) Among all such pairs \( (p, q) \), choose one with \( q \) least.

(ix) Expanding, \( p'^2 - 2q'^2 = 2q^2 - p^2 = 0 \), so \( p'^2 = 2q'^2 \).

(x) \( q < p \), since \( p \le q \) would give \( 2q^2 = p^2 \le q^2 \), that is, \( q^2 \le 0 \).
:::

::: {.solution}
An admissible order is
\[
\text{(v)}, \ \text{(ii)}, \ \text{(viii)}, \ \text{(x)}, \ \text{(vi)}, \ \text{(i)}, \ \text{(ix)}, \ \text{(iv)} .
\]
Lines (x) and (vi) may be exchanged, since neither uses the other. Otherwise the order is forced by what each line uses: (ii) needs the \( x > 0 \) of (v); (x) and (vi) are about the pair fixed in (viii), and if they came before it, the pair might change afterwards; (i) needs both inequalities; (ix) needs the definitions in (i); and (iv) needs \( q' \in \nZ_{>0} \) with \( p'^2 = 2q'^2 \), from (i) and (ix), and \( q' < q \), which comes from (vi).

*Line (vii) fails.* It asks for a least element of a set of positive rationals, and no result provides one: \( \nQ_{>0} \) itself has no least element (the midpoint argument of Section 10.5: \( 0 < x/2 < x \)), and least elements are guaranteed only for non-empty sets of integers bounded below (@prp-integer-least-element). So the line cites a principle that does not exist, entry (N9) of @exm-not-allowed-catalogue. It would not help even if granted: the descent keeps the number \( x \) and shrinks its denominator, \( p'/q' = p/q \), so what must be least is the denominator \( q \), as in (viii).

*Line (iii) fails.* Its conclusion is false: from \( p^2 = 2q^2 \) and \( q > 0 \) we get \( p^2 > q^2 \), hence \( q < p \) by @prp-ordered-ring-rules (g), the opposite of (iii). It also clashes with (x).
:::

::: {#exr-gaps-in-the-rationals-b2}
[B2]

Let \( A \coloneqq \{ x \in \nQ : x^2 < 2 \} \) and \( A^+ \coloneqq \{ x \in \nQ : x > 0, \ x^2 < 2 \} \). Without looking back, prove that \( A \) and \( A^+ \) have the same upper bounds in \( \nQ \), and deduce from @thm-rationals-gap-sqrt2 (a) that \( A^+ \) has no supremum in \( \nQ \).
:::

::: {.solution}
\( (\subseteq) \) for upper bounds: if \( u \) bounds \( A \), it bounds the subset \( A^+ \subseteq A \). Conversely, let \( u \) bound \( A^+ \). Since \( 1 > 0 \) and \( 1^2 = 1 < 2 \), \( 1 \in A^+ \), so \( 1 \le u \) and \( u > 0 \). Let \( x \in A \). If \( x > 0 \), then \( x \in A^+ \), so \( x \le u \). If \( x \le 0 \), then \( x \le 0 < u \). So \( u \) bounds \( A \).

Now suppose \( s \) were a supremum of \( A^+ \). Then \( s \) is an upper bound of \( A^+ \), hence of \( A \) (S1), and \( s \le u \) for every upper bound \( u \) of \( A^+ \), which are exactly the upper bounds of \( A \) (S2). So \( s \) would be a supremum of \( A \), which @thm-rationals-gap-sqrt2 (a) excludes. Hence \( A^+ \) has no supremum in \( \nQ \).
:::

::: {#exr-gaps-in-the-rationals-b3}
[B3]

Compute \( x_4 \) of @exm-newton-rationals-sqrt2, as a fraction of integers, and \( e_4 = x_4^2 - 2 \). Check your value of \( e_4 \) against (ii) of the example. Hence \( x_4 \) is an upper bound of \( \{ x \in \nQ : x^2 < 2 \} \) below \( x_3 \).
:::

::: {.solution}
With \( x_3 = 577/408 \),
\[
x_4 = t(x_3) = \frac{577^2 + 2 \cdot 408^2}{2 \cdot 577 \cdot 408} = \frac{332929 + 332928}{470832} = \frac{665857}{470832} .
\]
Then \( 665857^2 = 443365544449 \) and \( 470832^2 = 221682772224 \), and \( 443365544449 - 2 \cdot 221682772224 = 1 \), so
\[
e_4 = \frac{1}{221682772224} .
\]
By (ii), \( e_4 = e_3^2/(4x_3^2) = 1/(166464 \cdot 4 \cdot 332929) \), and \( 4 \cdot 166464 \cdot 332929 = 221682772224 \), which agrees. Since \( x_4 > 0 \) and \( e_4 > 0 \), \( x_4 \) bounds the set (the argument of the Quick check), and \( x_4 < x_3 \) by (iii).
:::

### C. Going deeper

::: {#exr-gaps-in-the-rationals-c1}
[C1: Exit check: the gap at \( \sqrt 2 \)]

Prove that no rational number squares to \( 2 \), and that the set \( \{ x \in \nQ : x^2 < 2 \} \) has no supremum in \( \nQ \).
:::

::: {.solution}
*No rational squares to \( 2 \).* Suppose \( x \in \nQ \) with \( x^2 = 2 \). Then \( x \ne 0 \), and replacing \( x \) by \( -x \) if needed (\( (-x)^2 = x^2 \)), \( x > 0 \). Write \( x = a/b \) with \( a, b \in \nZ_{>0} \) (@prp-integers-embed-rationals (b), @thm-rationals-ordered-field (a)); then \( a^2 = 2b^2 \). Among all \( q \in \nZ_{>0} \) for which some \( p \in \nZ_{>0} \) has \( p^2 = 2q^2 \), take the least (@prp-integer-least-element; the set contains \( b \) and is bounded below by \( 0 \)), with its \( p \). Then \( q < p \) (else \( p^2 \le q^2 \) by @prp-ordered-ring-rules (g), so \( q^2 \le 0 \), against \( q^2 > 0 \)) and \( p < 2q \) (else \( 4q^2 \le p^2 = 2q^2 \), so \( 2q^2 \le 0 \)). So \( p' \coloneqq 2q - p \) and \( q' \coloneqq p - q \) are positive integers with \( q' < q \), and \( p'^2 - 2q'^2 = 2q^2 - p^2 = 0 \) by expanding. This contradicts the choice of \( q \).

*Bounded above.* \( 2 \) bounds the set \( A \): \( x > 2 \) would give \( x^2 > 4 > 2 \) (@prp-ordered-ring-rules (g)). And \( 1 \in A \).

*No supremum.* Suppose \( s \in \nQ \) is a supremum of \( A \). As \( 1 \in A \), \( s \ge 1 > 0 \), and \( s^2 \ne 2 \) by the first part.

If \( s^2 < 2 \), let \( u \coloneqq 4s/(s^2 + 2) \in \nQ_{>0} \). Clearing denominators, \( u - s = s(2 - s^2)/(s^2 + 2) > 0 \) and \( 2 - u^2 = 2(s^2 - 2)^2/(s^2 + 2)^2 > 0 \). So \( u \in A \) and \( u > s \): \( s \) is not an upper bound.

If \( s^2 > 2 \), let \( t \coloneqq (s^2 + 2)/(2s) \in \nQ_{>0} \). Clearing denominators, \( t^2 - 2 = (s^2 - 2)^2/(4s^2) > 0 \) and \( s - t = (s^2 - 2)/(2s) > 0 \). So \( t^2 > 2 \), and \( t \) bounds \( A \) (an \( x \in A \) with \( x > t > 0 \) would have \( x^2 > t^2 > 2 \)); and \( t < s \). So \( s \) is not the least upper bound.

By trichotomy one of the two cases holds, and each contradicts the choice of \( s \). So \( A \) has no supremum in \( \nQ \).

**Marking scheme.** (10 points)
- 4: no rational squares to \( 2 \): sets up a least denominator, or any other correct route (1); proves the key inequalities \( q < p < 2q \), or the parity step of another route (2); reaches the contradiction (1).
- 1: shows that \( A \) is bounded above, with an explicit upper bound, and non-empty.
- 2: the case \( s^2 < 2 \): an explicit element of \( A \) larger than \( s \), with both properties verified.
- 2: the case \( s^2 > 2 \): an explicit smaller rational, verified to be an upper bound of \( A \).
- 1: concludes by trichotomy, with \( s^2 = 2 \) excluded by the first part.
Fatal errors (0 for the step): assuming that \( \sqrt 2 \) exists (in \( \nQ \) or in a larger field) and comparing \( s \) with it; "\( s^2 < 2 \), so \( s + \varepsilon \in A \) for small \( \varepsilon \)" with no \( \varepsilon \) exhibited and checked. A second route for the first part, by parity (every integer is \( 2m \) or \( 2m + 1 \), with \( m = \floor{a/2} \) from @prp-rational-integer-part, and not both), earns the same 4 points: 1 for the least denominator, 2 for "\( p \) even, then \( q \) even", 1 for the contradiction.
:::

::: {#exr-gaps-in-the-rationals-c2}
[C2: Which integers have a rational square root?]

For which \( n \in \nZ_{>0} \) does the set \( A_n \coloneqq \{ x \in \nQ : x^2 < n \} \) have a supremum in \( \nQ \)? Prove your answer.
:::

::: {.solution}
[Hint 1]

First find \( k \in \nN \) with \( k^2 \le n < (k + 1)^2 \), and treat \( n = k^2 \) on its own. For \( k^2 < n \), adapt both proofs of this section: the descent, and then the two maps.
:::

::: {.solution}
[Hint 2]

Let \( T \coloneqq \{ m \in \nZ : m \ge 0, \ n < m^2 \} \). It contains \( n + 1 \), it is bounded below by \( 0 \), and \( 0 \notin T \); so its least element is \( k + 1 \) for some \( k \in \nN \). In the descent for \( k^2 < n \), try \( q' \coloneqq p - kq \).
:::

::: {.solution}
**Answer:** exactly when \( n = k^2 \) for some \( k \in \nN \), and then the supremum is \( k \).

*Finding \( k \).* Let \( T \coloneqq \{ m \in \nZ : m \ge 0, \ n < m^2 \} \). Since \( n + 1 \ge 1 \), \( (n + 1)^2 \ge n + 1 > n \) (@prp-ordered-ring-rules (c)), so \( n + 1 \in T \); \( 0 \) is a lower bound of \( T \); and \( 0 \notin T \), as \( 0^2 = 0 < n \). By @prp-integer-least-element, \( T \) has a least element \( l \ge 1 \). Let \( k \coloneqq l - 1 \in \nN \). Then \( n < (k + 1)^2 \), and \( k \notin T \) with \( k \ge 0 \) gives \( k^2 \le n \). So either \( n = k^2 \) or \( k^2 < n < (k + 1)^2 \).

*Case \( n = k^2 \).* Here \( k \ge 1 \), since \( n \ge 1 \). We show \( k = \sup A_n \). (S1): if \( x \in A_n \) had \( x > k \), then \( x > k \ge 0 \) would give \( x^2 > k^2 = n \) (@prp-ordered-ring-rules (g)), against \( x^2 < n \); so \( x \le k \). (S2): let \( v \) be an upper bound of \( A_n \), and suppose \( v < k \). Let \( w \coloneqq v \) if \( v \ge 0 \) and \( w \coloneqq 0 \) otherwise; then \( v \le w \) and \( 0 \le w < k \). Let \( c \) be the midpoint of \( w \) and \( k \) (Section 10.5): \( w < c < k \). Then \( c > 0 \) and \( c^2 < k^2 = n \) by (g), so \( c \in A_n \), and \( c > w \ge v \), so \( v \) is not an upper bound. Hence \( k \le v \) for every upper bound \( v \), and \( k \) is the supremum.

*Case \( k^2 < n < (k + 1)^2 \).* Then \( n \ge 2 \), since \( n = 1 = 1^2 \) is the other case; so \( 1 \in A_n \).

(i) *No rational squares to \( n \).* Suppose \( x^2 = n \) with \( x \in \nQ \); as in @thm-no-rational-square-two, we may take \( x > 0 \), and then \( p^2 = nq^2 \) for some \( p, q \in \nZ_{>0} \), with \( q \) least among all such denominators (@prp-integer-least-element). Multiplying \( k^2 < n < (k + 1)^2 \) by \( q^2 > 0 \) gives \( (kq)^2 < p^2 < ((k + 1)q)^2 \), so \( kq < p < (k + 1)q \) by (g). Let
\[
p' \coloneqq nq - kp , \qquad q' \coloneqq p - kq .
\]
Then \( 0 < q' < q \). For \( p' \), expand:
\[
q \cdot p' = nq^2 - kpq = p^2 - kpq = p(p - kq) > 0
\]
by (O4); since \( q > 0 \), \( p' \le 0 \) would give \( q p' \le 0 \) (@prp-ordered-ring-rules (c)), so \( p' > 0 \). (The bounds alone do not give this: for \( n = 5 \), \( k = 2 \), \( q = 10 \), \( p = 28 \), we have \( kq < p < (k + 1)q \), but \( nq - kp = -6 \). It is \( p^2 = nq^2 \) that forces the sign.) Finally, expanding,
\[
p'^2 - n q'^2 = (k^2 - n)(p^2 - nq^2) = 0 ,
\]
so \( q' \) is a smaller admissible denominator, a contradiction.

(ii) *No supremum.* The proof of @thm-rationals-gap-sqrt2 (a) goes through with \( n \) in place of \( 2 \), using (i) where it used @thm-no-rational-square-two. The set \( A_n \) contains \( 1 \) and is bounded above by \( n \) (if \( x > n \ge 1 \), then \( x^2 > n^2 \ge n \)). For \( s \in \nQ_{>0} \), let
\[
t(s) \coloneqq \frac{s^2 + n}{2s} , \qquad u(s) \coloneqq \frac{2ns}{s^2 + n} .
\]
Clearing denominators as before,
\[
\begin{aligned}
t(s)^2 - n &= \frac{(s^2 - n)^2}{4s^2} , & s - t(s) &= \frac{s^2 - n}{2s} , \\
u(s) - s &= \frac{s(n - s^2)}{s^2 + n} , & n - u(s)^2 &= \frac{n(s^2 - n)^2}{(s^2 + n)^2} .
\end{aligned}
\]
A supremum \( s \) would satisfy \( s \ge 1 > 0 \) and \( s^2 \ne n \) by (i). If \( s^2 < n \), then \( u(s) \in A_n \) and \( u(s) > s \); if \( s^2 > n \), then \( t(s) \) is an upper bound of \( A_n \) with \( t(s) < s \). Either way \( s \) is not the supremum.

So \( A_n \) has a supremum in \( \nQ \) exactly when \( n \) is the square of a natural number.

**Marking scheme.** (10 points)
- 2: produces \( k \in \nN \) with \( k^2 \le n < (k + 1)^2 \), from a least element.
- 2: the case \( n = k^2 \): checks (S1) and (S2) for \( k \).
- 3: the case \( k^2 < n \): no rational squares to \( n \), by a descent with a least denominator (or another correct route), including a proof that the new numerator is positive.
- 2: the two maps (or any explicit rationals) and the two cases, as in the proof for \( 2 \).
- 1: states the answer: exactly the squares of natural numbers.
Fatal errors (0 for the step): using a square root of \( n \), or the floor of one, as if it existed; deducing \( nq - kp > 0 \) from \( kq < p < (k + 1)q \) alone.
:::

### R. Review

::: {#exr-gaps-in-the-rationals-r1}
[R1]

Prove, by induction on \( m \), that for all \( m, n \in \nN \): if \( m + n = m \), then \( n = 0 \). Use only the equations of addition (\( m + 0 = m \), \( m + (n + 1) = (m + n) + 1 \), \( 0 + n = n \), \( (m + 1) + n = (m + n) + 1 \)) and the fact that \( k + 1 = l + 1 \) implies \( k = l \). Do not use cancellation or any fact about the order: cancellation gives the claim in one line (\( m + n = m + 0 \)), and it is itself proved from the facts this exercise asks you to use.
:::

::: {.solution}
We use @thm-omega-induction (b) (the form of @ax-induction on \( \omega = \nN \), by @cor-omega-identification (b)) on \( m \), for the property \( P(m) \): "for every \( n \in \nN \), if \( m + n = m \), then \( n = 0 \)". Keeping "for every \( n \)" inside \( P(m) \) lets the step use the hypothesis for the same \( n \).

*Base \( P(0) \).* Let \( 0 + n = 0 \). Since \( 0 + n = n \) (@thm-omega-arithmetic-laws (a)), \( n = 0 \).

*Step.* Assume \( P(m) \), and let \( (m + 1) + n = m + 1 \). By @thm-omega-arithmetic-laws (a), \( (m + 1) + n = (m + n) + 1 \), so \( (m + n) + 1 = m + 1 \). By @cor-omega-successor-cancellation, \( m + n = m \). By \( P(m) \), \( n = 0 \). This proves \( P(m + 1) \).

By induction, \( P(m) \) holds for every \( m \in \nN \).

Cancellation (@prp-omega-order-arithmetic (b)) and the order facts are deliberately not used: each gives a one-line proof, and cancellation is itself proved by peeling off one successor at a time with @cor-omega-successor-cancellation, the move of the step above.
:::

::: {#exr-gaps-in-the-rationals-r2}
[R2]

Show that the set \( \nQ \), as constructed in this chapter, is countable.
:::

::: {.solution}
The tools are the results on countable sets of Chapter 8, read on \( \nN = \omega \) through the dictionary of Section 9.7 (@cor-omega-identification and the table after it).

*\( \nZ \) is countable.* \( \nN \times \nN \) is countable (@thm-product-countable). The map \( a \mapsto [a] \), from \( \nN \times \nN \) to \( \nZ = (\nN \times \nN)/{\sim} \), is surjective, since every class is the class of each of its elements (@def-quotient-set). By @prp-countable-image, \( \nZ \) is countable.

*\( \nZ \times \nZ_{>0} \) is countable.* \( \nZ_{>0} \subseteq \nZ \) is countable by @prp-countable-subset, and the product of two countable sets is countable (@cor-product-countable (a)).

*\( \nQ \) is countable.* The map \( (p, q) \mapsto [(p, q)] \), from \( \nZ \times \nZ_{>0} \) to \( \nQ \), is surjective (@def-quotient-set), so \( \nQ \) is countable by @prp-countable-image.

(Section 9.7 lets a review exercise cite @thm-product-countable and @cor-product-countable, which run on \( \omega \) through @prp-omega-powers-parity.) The conclusion is @thm-integers-rationals-countable for the constructed \( \nQ \); that theorem, about the school rationals, is not used.
:::

::: {#exr-gaps-in-the-rationals-r3}
[R3]

Let \( A \coloneqq \{ x \in \nQ : x^2 < 2 \} \) and \( s \in \nQ \). Write "\( s \) is a supremum of \( A \) in \( \nQ \)" in symbols, with bounded quantifiers. Then write its negation, moving \( \neg \) inward as far as it goes and naming the law used at each step. The proof that \( A \) has no supremum in \( \nQ \) has two cases; which half of the negation does each case establish, and with which witness?
:::

::: {.solution}
By @def-order-supremum, "\( s \) is a supremum of \( A \)" is the conjunction of (S1) and (S2):
\[
\bigl( \forall x \in A \ \ x \le s \bigr) \ \wedge \ \forall v \in \nQ \ \bigl( (\forall x \in A \ \ x \le v) \to s \le v \bigr) .
\]
Its negation is, by @prp-de-morgan (d),
\[
\neg \bigl( \forall x \in A \ \ x \le s \bigr) \ \vee \ \neg \forall v \in \nQ \ \bigl( (\forall x \in A \ \ x \le v) \to s \le v \bigr) .
\]
By @prp-bounded-quantifier-negation (a), the first disjunct becomes \( \exists x \in A \ \neg(x \le s) \), that is, \( \exists x \in A \ \ s < x \) (totality of \( \le \), @prp-ordered-ring-rules (i)). By @prp-bounded-quantifier-negation (a) and then @prp-negated-implication, the second becomes
\[
\exists v \in \nQ \ \bigl( (\forall x \in A \ \ x \le v) \wedge \neg(s \le v) \bigr) ,
\]
that is, there is an upper bound \( v \) of \( A \) with \( v < s \). In words: \( s \) fails to be the supremum when **some element of \( A \) lies above \( s \)**, or **some upper bound lies below \( s \)**.

In the proof of @thm-rationals-gap-sqrt2, Case 1 (\( s^2 < 2 \)) establishes the first disjunct, with witness \( x = u(s) = 4s/(s^2 + 2) \). Case 2 (\( s^2 > 2 \)) establishes the second, with witness \( v = t(s) = (s^2 + 2)/(2s) \). (The proof itself needs no negation law: it derives a contradiction from (S1) in Case 1 and from (S2) in Case 2.)
:::

::: {#exr-gaps-in-the-rationals-r4}
[R4]

Is there a rational number \( x \) with \( x^3 = 2 \), where \( x^3 \coloneqq x^2 \cdot x \)? Prove your answer.
:::

::: {.solution}
**No.** The tool is descent on the denominator, as in @thm-no-rational-square-two, but run with parity, which @prp-rational-integer-part supplies.

*Parity.* For every \( a \in \nZ \) there is \( m \in \nZ \) with \( a = 2m \) or \( a = 2m + 1 \), and not both forms occur. Indeed, let \( m \coloneqq \floor{a/2} \) (@prp-rational-integer-part): \( m \le a/2 < m + 1 \), so \( 2m \le a < 2m + 2 \) (@prp-ordered-ring-rules (c)). The integer \( r \coloneqq a - 2m \) has \( 0 \le r < 2 \); if \( r > 0 \), then \( r \ge 1 \), and if \( r > 1 \), then \( r \ge 2 \), by discreteness (@thm-integers-ordered-ring (c)); so \( r = 0 \) or \( r = 1 \). If \( 2m = 2m' + 1 \), then \( d \coloneqq m - m' \) has \( 2d = 1 \); but \( d \le 0 \) gives \( 2d \le 0 \), and \( d \ge 1 \) gives \( 2d \ge 2 \), and by discreteness one of these holds. Moreover an odd cube is odd:
\[
(2m + 1)^3 = 2(4m^3 + 6m^2 + 3m) + 1 .
\]

*Descent.* Suppose \( x \in \nQ \) and \( x^3 = 2 \). Then \( x > 0 \): \( x = 0 \) gives \( x^3 = 0 \), and \( x < 0 \) gives \( x^2 > 0 \) and \( x^3 = x^2 \cdot x < 0 \) (@prp-ordered-ring-rules (e), (c)). So \( x = p/q \) with \( p, q \in \nZ_{>0} \) and \( p^3 = 2q^3 \) (@prp-integers-embed-rationals (b), @def-rational-operations). Take \( q \) least among such denominators (@prp-integer-least-element), with its \( p \). Since \( p^3 = 2q^3 \) has the even form, \( p \) is not odd (its cube would be odd), so \( p = 2m \) with \( m \in \nZ \), and \( m > 0 \) because \( p > 0 \) (\( m \le 0 \) would give \( 2m \le 0 \)). Then \( 2q^3 = 8m^3 \), and canceling the non-zero factor \( 2 \) (@prp-ordered-ring-rules (f)), \( q^3 = 2(2m^3) \). So \( q \) is not odd either: \( q = 2l \) with \( l \in \nZ_{>0} \). Then \( 8m^3 = 2 \cdot 8l^3 \), so \( m^3 = 2l^3 \), and \( l < l + l = q \). So \( l \) is a smaller admissible denominator, with \( m \in \nZ_{>0} \): a contradiction.

*Why the look-alike fails.* The substitution \( p' \coloneqq 2q - p \), \( q' \coloneqq p - q \) of the square-root proof came from \( x = (2 - x)/(x - 1) \), which used \( x^2 = 2 \). For cubes it does not preserve the equation: expanding,
\[
(2q - p)^3 - 2(p - q)^3 = -3p^3 + 12p^2 q - 18pq^2 + 10q^3 ,
\]
which is not a constant multiple of \( p^3 - 2q^3 \) (it has a \( p^2 q \) term), so \( p^3 = 2q^3 \) does not give \( p'^3 = 2q'^3 \). Parity, by contrast, works for every power: "even cube, so even base" is the same argument for squares and cubes.
:::

<!-- dependency ledger
thm-no-rational-square-two (proof): 2 = 1 + 1 > 0 and 4 = 2 * 2; numerals compared in N | prp-ordered-ring-rules (b), (e); omega arithmetic (def-omega-arithmetic) carried into Q by prp-naturals-embed-integers and prp-integers-embed-rationals
thm-no-rational-square-two (proof): (a/b)^2 = a^2/b^2 for b in Z_{>0} | def-rational-operations (product of classes), cited
thm-no-rational-square-two (proof): p <= q with 0 <= p gives p^2 <= q^2 (the <= form of (g)) | prp-ordered-ring-rules (g) and the equality case; inline
thm-no-rational-square-two (proof): expansion (2q - p)^2 = 4q^2 - 4pq + p^2 and 2(p - q)^2 = 2p^2 - 4pq + 2q^2 | prp-ring-algebra (c), (d), cited; verify/ch10/thm-no-rational-square-two.py
thm-no-rational-square-two (claim): school proof of the same statement by parity in Ch 2; parity on the constructed Z in a later chapter of this volume | thm-sqrt2-irrational (prose comparison only); F3.5 (prose pointer; nothing depends on it)
thm-rationals-gap-sqrt2 (proof): the four identities (eq-newton-identities), by clearing denominators | thm-rationals-field (F8: multiplying by a non-zero element is undone by its inverse), prp-ring-algebra; inline; verify/ch10/thm-rationals-gap-sqrt2.py
thm-rationals-gap-sqrt2 (proof): z/w := z w^{-1}; a quotient of positives is positive | def-commutative-ring-and-field; prp-reciprocal-order (a) and (O4), cited
thm-rationals-gap-sqrt2 (proof): (S1), (S2) depend only on the set of upper bounds | def-order-supremum, cited; inline
thm-rationals-gap-sqrt2 (claim): (remark) the same set has a supremum in R; Ch 11 proves the rational statement | Ch 11 (prose pointer; nothing here depends on it)
exm-newton-rationals-sqrt2 (example): the sequence as a function N -> Q_{>0} | thm-recursion read on omega (thm-omega-recursion, via cor-omega-identification (b)), cited
exm-newton-rationals-sqrt2 (example): induction for (i) | ax-induction read on omega (thm-omega-induction (b), via cor-omega-identification (b)), cited
exm-newton-rationals-sqrt2 (example): values x_1..x_3, e_0..e_3, 577^2 = 332929, 408^2 = 166464, 144 * 1156 = 166464 | inline arithmetic; verify/ch10/exm-newton-rationals-sqrt2.py
exm-newton-rationals-sqrt2 (claim): (paragraph after the table) school decimals; "the squares approach L^2"; Cauchy and no rational limit | for orientation only, marked; a later chapter of this volume (F3.9, prose pointer; nothing here depends on it)
exm-newton-rationals-sqrt2 (claim): (closing paragraph) R from sequences of rationals identified when their difference tends to 0 | a later chapter of this volume (F3.10, prose pointer)
exr-gaps-in-the-rationals-a1 (solution): values t(3/2) = 17/12, u(7/5) = 140/99, 140^2 = 19600, 2 * 99^2 = 19602 | verify/ch10/exr-gaps-in-the-rationals-a1.py
exr-gaps-in-the-rationals-a1 (solution): in any ordered field the identities and t(r) = u(r) = r for r^2 = 2 | field arithmetic, as in the proof; inline
exr-gaps-in-the-rationals-b1 (solution): Q_{>0} has no least element | midpoint paragraph of Section 10.5 (after prp-reciprocal-order)
exr-gaps-in-the-rationals-b3 (solution): x_4 = 665857/470832, e_4 = 1/221682772224 and the products checking (ii) | inline arithmetic; verify/ch10/exr-gaps-in-the-rationals-b3.py
exr-gaps-in-the-rationals-c1 (solution): second route by parity | as in exr-gaps-in-the-rationals-r4's solution (prp-rational-integer-part); marking-scheme note only
exr-gaps-in-the-rationals-c2 (solution): (n + 1)^2 >= n + 1 > n; n^2 >= n for n >= 1 | prp-ordered-ring-rules (c); inline
exr-gaps-in-the-rationals-c2 (solution): identities (k^2 - n)(p^2 - n q^2), q(nq - kp) = p(p - kq) - (p^2 - nq^2), the four general maps; the witness n = 5, k = 2, q = 10, p = 28 | verify/ch10/exr-gaps-in-the-rationals-c2.py
exr-gaps-in-the-rationals-c2 (solution): midpoint of w and k lies strictly between | midpoint paragraph of Section 10.5
exr-gaps-in-the-rationals-r1 (solution): recursive equations of + and successor cancellation | def-omega-arithmetic (a), thm-omega-arithmetic-laws (a), cor-omega-successor-cancellation, cited
exr-gaps-in-the-rationals-r2 (solution): Chapter 8 results on omega; group (ii) citations allowed in an R item | cor-omega-identification and the citing rule after it (Section 9.7), cited
exr-gaps-in-the-rationals-r4 (solution): cube expansions (2m + 1)^3 and (2q - p)^3 - 2(p - q)^3 | prp-ring-algebra; verify/ch10/exr-gaps-in-the-rationals-r4.py
exr-gaps-in-the-rationals-r4 (solution): canceling a non-zero factor (2c = 2d gives c = d) | prp-ordered-ring-rules (f) applied to 2(c - d) = 0; inline
-->
