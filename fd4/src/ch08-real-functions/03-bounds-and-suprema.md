# Bounded Functions and Their Suprema

*Number Systems* proved that \( \nR \) is a complete ordered field (@fd3:thm-reals-complete-ordered-field): every non-empty set of real numbers that is bounded above has a supremum (@fd3:def-complete-ordered-field), a least upper bound in the sense of *Sets and Functions* (@fd2:def-order-supremum). A real function \( f \colon D \to \nR \) hands us such sets, one for each \( A \subseteq D \): the set \( f(A) \) of its values on \( A \). This section asks when \( f(A) \) is bounded, names its supremum and infimum, and fixes one method for computing them: bound every value, then find a witness. It ends with rules for comparing suprema without computing them.

## A least upper bound that is never reached

Let \( f(x) = x/(1 + x) \) on \( [0, \infty) \). A few values:
\[
f(0) = 0 , \qquad f(1) = \frac12 , \qquad f(9) = \frac{9}{10} , \qquad f(99) = \frac{99}{100} .
\]
Every value is below \( 1 \), since \( x < 1 + x \) and \( 1 + x > 0 \). The values creep toward \( 1 \) and never reach it.

"Its maximum is \( 1 \)" is false: a maximum is a value, and \( 1 \) is not a value of \( f \). "Its least upper bound is \( 1 \)" is true, and proving it takes two halves. First, \( 1 \) bounds every value. Second, no number below \( 1 \) bounds every value. The first half is one line. The second half is the real work, and the first tool of this section turns it into a search for a single point.

## The infimum and the epsilon test

Suprema come with a mirror image. *Sets and Functions* defined the infimum of a set as its greatest lower bound (@fd2:def-order-supremum), but completeness speaks only of suprema. Reflection in \( 0 \) turns one into the other. For \( A \subseteq \nR \), write \( -A \coloneqq \{ -a : a \in A \} \), the image of \( A \) under \( x \mapsto -x \) (@fd2:exm-sets-of-numbers-as-images).

::: {#prp-real-infimum}
[Infimum by Reflection]

Let \( A \subseteq \nR \).

::: {.enumerate options="label=(\alph*)"}
1. A real number \( l \) is a lower bound of \( A \) if and only if \( -l \) is an upper bound of \( -A \).
2. If \( A \) is **non-empty** and bounded below, then \( A \) has an infimum, and \( \inf A = -\sup(-A) \).
:::
:::

::: {.proof}
(a) For \( a \in A \), \( l \le a \) holds if and only if \( -a \le -l \), by @fd3:prp-ordered-ring-rules (a) together with the case of equality. The elements of \( -A \) are exactly the numbers \( -a \) with \( a \in A \), so \( l \le a \) for every \( a \in A \) if and only if \( b \le -l \) for every \( b \in -A \).

(b) Let \( l \) be a lower bound of \( A \). By (a), \( -l \) is an upper bound of \( -A \), and \( -A \) is non-empty because \( A \) is. Since \( \nR \) is complete (@fd3:thm-reals-complete-ordered-field), \( s \coloneqq \sup(-A) \) exists. By (a), applied to \( -s \), the number \( -s \) is a lower bound of \( A \), since \( -(-s) = s \) is an upper bound of \( -A \). If \( l' \) is any lower bound of \( A \), then \( -l' \) is an upper bound of \( -A \) by (a), so \( s \le -l' \) by (S2), that is, \( l' \le -s \). So \( -s \) is the greatest lower bound of \( A \).
:::

Every statement about suprema thus has a twin about infima; below we write out only the supremum half.

The second half of "least upper bound" says that nothing smaller is an upper bound. In \( \nR \) "smaller" can be measured by a positive gap \( \varepsilon \), and "not an upper bound" means that some element sticks out above. That gives a test with an explicit witness.

::: {#prp-real-sup-approximation}
[The Epsilon Test for a Supremum]

Let \( A \subseteq \nR \) be **non-empty** and let \( s \) be an upper bound of \( A \). Then \( s = \sup A \) if and only if **for every** \( \varepsilon > 0 \) **there exists** \( a \in A \) with \( a > s - \varepsilon \):
\[
\forall \varepsilon > 0 \ \ \exists a \in A \ \ a > s - \varepsilon .
\]
Likewise, if \( i \) is a lower bound of \( A \), then \( i = \inf A \) if and only if for every \( \varepsilon > 0 \) there exists \( a \in A \) with \( a < i + \varepsilon \).
:::

::: {.proof}
\( (\Rightarrow) \) Let \( s = \sup A \) and \( \varepsilon > 0 \). Then \( s - \varepsilon < s \). If \( s - \varepsilon \) were an upper bound of \( A \), (S2) would give \( s \le s - \varepsilon \), which is false. So some \( a \in A \) fails \( a \le s - \varepsilon \); by totality of the order (@fd3:prp-ordered-ring-rules (i)), \( a > s - \varepsilon \).

\( (\Leftarrow) \) Assume the condition, and let \( u \) be an upper bound of \( A \). Suppose \( u < s \), and put \( \varepsilon \coloneqq s - u > 0 \). The condition gives \( a \in A \) with \( a > s - \varepsilon = u \), against \( u \) being an upper bound. So \( s \le u \) by totality, and \( s \) satisfies (S1) and (S2).

For the infimum, apply the supremum statement to \( -A \) and the upper bound \( -i \) (@prp-real-infimum (a)). By the proof of @prp-real-infimum (b), \( i = \inf A \) if and only if \( -i = \sup(-A) \); and \( -a > -i - \varepsilon \) if and only if \( a < i + \varepsilon \).
:::

The element \( a \) is a **witness** for \( \varepsilon \). It may depend on \( \varepsilon \), and it usually does: a smaller \( \varepsilon \) asks for an element closer to the top.

::: {.check}
Is \( 0.99 \) the supremum of \( [0, 1) \)? Use the test.
:::

::: {.solution}
No, and the test does not even apply: it is stated for an upper bound \( s \), and \( 0.99 \) is not one, since \( 0.995 \in [0, 1) \) and \( 0.995 > 0.99 \). The supremum is \( 1 \): it bounds \( [0, 1) \), and for \( \varepsilon > 0 \) the element \( \max(0, 1 - \varepsilon/2) \) of \( [0, 1) \) exceeds \( 1 - \varepsilon \).
:::

## Bounded functions and their suprema

A real function (@def-real-function) on \( D \) has a set of values on each \( A \subseteq D \), and the words of the previous subsection apply to that set.

*A function is bounded on \( A \) when its values on \( A \) stay inside a fixed window.*

::: {#def-bounded-function}
[Bounded Function]

Let \( f \colon D \to \nR \) and \( A \subseteq D \). The function \( f \) is **bounded above on \( A \)** if the set \( f(A) = \{ f(x) : x \in A \} \) (@fd2:def-image) is bounded above: **there exists** \( M \in \nR \) with \( f(x) \le M \) **for every** \( x \in A \). It is **bounded below on \( A \)** if \( f(A) \) is bounded below, and **bounded on \( A \)** if there exists \( M \in \nR \) with \( \abs{f(x)} \le M \) for every \( x \in A \). When \( A = D \), "on \( D \)" may be dropped.
:::

In words: one number \( M \), chosen before \( x \), works for all \( x \in A \). By @fd3:prp-absolute-value-ordered-field (d), \( \abs{f(x)} \le M \) says \( -M \le f(x) \le M \), so a bounded function is bounded above and below. Conversely, if \( L \le f(x) \le U \) on \( A \), then \( M \coloneqq \max(\abs{L}, \abs{U}) \) gives \( f(x) \le \abs{U} \le M \) and \( -f(x) \le -L \le \abs{L} \le M \), so \( \abs{f(x)} \le M \). The two meanings of "bounded" agree.

Examples. The hook function \( x/(1 + x) \) is bounded on \( [0, \infty) \), with \( 0 \le f(x) < 1 \). A constant function \( c \) is bounded on every \( A \), by \( \abs{c} \). The function \( 1/x \) on \( (0, 1] \) is bounded below by \( 0 \) but not above: given \( M \), the point \( x \coloneqq 1/(\abs{M} + 1) \) lies in \( (0, 1] \) and \( 1/x = \abs{M} + 1 > M \). Change only the set to \( [1, 2] \) and the same formula is bounded, with \( 1/2 \le 1/x \le 1 \) (@fd3:prp-ordered-field-halves (c)). Boundedness belongs to the pair \( (f, A) \), not to the formula.

::: {#def-sup-of-function}
[Supremum and Infimum of a Function]

Let \( f \colon D \to \nR \), let \( A \subseteq D \) be **non-empty**, and let \( f \) be bounded above on \( A \). The **supremum of \( f \) on \( A \)** is
\[
\sup_A f \coloneqq \sup f(A) ,
\]
also written \( \sup_{x \in A} f(x) \). If \( f \) is bounded below on \( A \), its **infimum** on \( A \) is \( \inf_A f \coloneqq \inf f(A) \). The supremum is **attained** if \( \sup_A f \in f(A) \), that is, \( \sup_A f = f(x_0) \) for some \( x_0 \in A \); it is then the **maximum** of \( f \) on \( A \), written \( \max_A f \). Likewise an attained infimum is the **minimum** \( \min_A f \).
:::

Both exist under the stated hypotheses: \( f(A) \) is non-empty because \( A \) is, so completeness gives \( \sup f(A) \), and @prp-real-infimum (b) gives \( \inf f(A) \). The set \( A \) must be non-empty, since every real number bounds the empty set and no least one exists. An attained supremum \( f(x_0) \) is an upper bound of \( f(A) \) lying in \( f(A) \), so it is the largest value; conversely a largest value \( f(x_0) \) is an upper bound, and every upper bound is at least \( f(x_0) \), so it is the supremum.

::: {.warning}
**The supremum need not be a value.** A proof that starts "let \( x_0 \) be the point where \( f \) reaches \( \sup_A f \)" has assumed that the supremum is attained. For \( x/(1 + x) \) on \( [0, \infty) \) no such point exists. The supremum also depends on \( A \): \( \sup_{[0, 1]} x^2 = 1 \) and \( \sup_{[0, 2]} x^2 = 4 \).
:::

The two halves of the hook are now a method.

::: {#exm-method-sup-two-halves}
[Method: bound every value, then find a witness]

**Template.** To prove \( \sup_A f = M \) for a non-empty \( A \) and a candidate \( M \in \nR \):

- \( (\le) \) *Bound every value.* Let \( x \in A \) be arbitrary and prove \( f(x) \le M \).
- \( (\ge) \) *Find a witness.* Let \( \varepsilon > 0 \) be arbitrary and produce \( x \in A \), depending on \( \varepsilon \), with \( f(x) > M - \varepsilon \).

The first half shows that \( f \) is bounded above on \( A \) and that \( M \) is an upper bound of \( f(A) \); then \( M = \sup_A f \) by @prp-real-sup-approximation. For an infimum, reverse the inequalities: \( f(x) \ge m \) for every \( x \in A \), and for each \( \varepsilon > 0 \) some \( x \) with \( f(x) < m + \varepsilon \).

| Givens | Goal |
|---|---|
| \( f \) on \( A \ne \emptyset \); a candidate \( M \) | \( (\le) \) \( \forall x \in A \ \ f(x) \le M \); \( (\ge) \) \( \forall \varepsilon > 0 \ \exists x \in A \ \ f(x) > M - \varepsilon \) |

**When to use it.** Whenever a supremum or infimum is to be computed. An inequality \( \sup_A f \le M \) needs only the first half, since the supremum is the least upper bound; an equality needs both.

**The usual failures.** Proving only \( (\le) \): that shows \( M \) is an upper bound, not the least one. Producing a witness for one \( \varepsilon \), such as \( 1/10 \), instead of for every \( \varepsilon \). Pairing a witness for \( f \) with a different witness for \( g \), as if \( f(x) + g(y) \) were a value of \( f + g \) (Exercise B4 dissects this one).
:::

## Two worked examples

The first example is the hook; its witness has to move with \( \varepsilon \).

::: {#exm-sup-not-attained}
[A supremum that is not attained]

Let \( f(x) = x/(1 + x) \) on \( A = [0, \infty) \). Prove that \( \sup_A f = 1 \) and that it is not attained. Find \( \inf_A f \).
:::

::: {.idea}
[Scratch work]

The bounding half: \( x/(1 + x) \le 1 \) means \( x \le 1 + x \), after multiplying by \( 1 + x > 0 \), and that holds, even strictly.

The witness half is the gap. Given \( \varepsilon > 0 \), we want \( x \ge 0 \) with
\[
\frac{x}{1 + x} > 1 - \varepsilon .
\]
For \( \varepsilon \ge 1 \) the right side is at most \( 0 \) and any \( x > 0 \) works. For \( 0 < \varepsilon < 1 \), work backwards: multiply by \( 1 + x \), collect \( x \):
\[
x > (1 - \varepsilon)(1 + x) \iff \varepsilon x > 1 - \varepsilon \iff x > \frac{1}{\varepsilon} - 1 .
\]
So \( x \coloneqq 1/\varepsilon \) is a clean choice, a little larger than needed. Does it also cover \( \varepsilon \ge 1 \)? At \( x = 1/\varepsilon \) the value is \( 1/(1 + \varepsilon) \), and \( 1/(1 + \varepsilon) > 1 - \varepsilon \) means \( 1 > (1 - \varepsilon)(1 + \varepsilon) = 1 - \varepsilon^2 \), true for every \( \varepsilon > 0 \). One choice, no cases; the restriction \( \varepsilon < 1 \) was needed only while solving backwards.

| Givens | Goal |
|---|---|
| \( x \in [0, \infty) \) | \( x/(1 + x) \le 1 \) |
| \( \varepsilon > 0 \) | some \( x \ge 0 \) with \( x/(1 + x) > 1 - \varepsilon \) |
| \( x \coloneqq 1/\varepsilon \), value \( 1/(1 + \varepsilon) \) | \( 1/(1 + \varepsilon) > 1 - \varepsilon \), i.e. \( 1 > 1 - \varepsilon^2 \): the gap is closed |

The proof runs forwards: bound, then choose \( x \) from \( \varepsilon \), then check.
:::

::: {.solution}
*Bound every value.* Let \( x \ge 0 \). Then \( 1 + x > 0 \) and \( x < 1 + x \); multiplying by \( 1/(1 + x) > 0 \) (@fd3:prp-ordered-ring-rules (c)) gives \( f(x) < 1 \).

*Find a witness.* Let \( \varepsilon > 0 \) and put \( x \coloneqq 1/\varepsilon \), which lies in \( A \). Then
\[
f(x) = \frac{1/\varepsilon}{1 + 1/\varepsilon} = \frac{1}{1 + \varepsilon} .
\]
Since \( (1 - \varepsilon)(1 + \varepsilon) = 1 - \varepsilon^2 < 1 \) and \( 1 + \varepsilon > 0 \), dividing by \( 1 + \varepsilon \) gives \( 1 - \varepsilon < 1/(1 + \varepsilon) = f(x) \).

By the method of @exm-method-sup-two-halves, \( \sup_A f = 1 \). It is not attained, because \( f(x) < 1 \) for every \( x \in A \).

For the infimum, \( f(x) \ge 0 \) for \( x \ge 0 \), as a quotient of \( x \ge 0 \) by \( 1 + x > 0 \), and \( f(0) = 0 \). So \( \inf_A f = 0 \), attained: \( \min_A f = 0 \).
:::

::: {.check}
For \( \varepsilon = 2 \), which \( x \) does the proof choose, and is its value above \( 1 - \varepsilon \)?
:::

::: {.solution}
\( x = 1/2 \), with \( f(1/2) = (1/2)/(3/2) = 1/3 \), and \( 1/3 > -1 = 1 - \varepsilon \). The proof needs no separate case for large \( \varepsilon \).
:::

In the second example the candidate is a value, and the witness half costs nothing.

::: {#exm-sup-attained-parabola}
[A supremum that is attained]

Find \( \sup \) and \( \inf \) of \( g(x) = x(1 - x) \) on \( [0, 1] \).
:::

::: {.solution}
Completing the square, \( x(1 - x) = \frac14 - \bigl( x - \frac12 \bigr)^2 \).

*Bound every value.* Since \( \bigl( x - \frac12 \bigr)^2 \ge 0 \), \( g(x) \le \frac14 \) for every \( x \).

*Find a witness.* \( g(1/2) = 1/4 \), and \( \frac14 > \frac14 - \varepsilon \) for every \( \varepsilon > 0 \). So \( x = 1/2 \) is a witness for every \( \varepsilon \) at once.

Hence \( \sup_{[0, 1]} g = 1/4 \), attained at \( 1/2 \): it is \( \max_{[0, 1]} g \). For the infimum, on \( [0, 1] \) both \( x \ge 0 \) and \( 1 - x \ge 0 \), so \( g(x) \ge 0 \), and \( g(0) = 0 \): \( \min_{[0, 1]} g = 0 \).
:::

An attained value is its own witness, which is why no \( \varepsilon \) appears in the second solution.

::: {.check}
Find \( \sup \) and \( \inf \) of \( x^2 \) on \( (-1, 2) \), and of \( \ind_{\nQ} \colon \nR \to \{0, 1\} \) (@fd2:def-indicator) on \( [0, 1] \). Which are attained?
:::

::: {.solution}
For \( x^2 \): the values on \( (-1, 2) \) form \( [0, 4) \), so \( \sup = 4 \), not attained (\( x^2 = 4 \) needs \( x = \pm 2 \)), and \( \inf = 0 \), attained at \( 0 \).

For \( \ind_{\nQ} \): \( \sup = 1 \), attained at any rational point such as \( 0 \), and \( \inf = 0 \), attained at any irrational point of \( [0, 1] \). One is \( \sqrt2/2 \), with \( \sqrt2 \) from @fd3:prp-cof-square-roots: it lies in \( [0, 1] \) since \( 0 \le \sqrt 2 \le 2 \). If \( \sqrt2/2 = q \in \nQ \), then \( \sqrt2 = 2q \) would be rational with square \( 2 \); since the copy of \( \nQ \) in \( \nR \) respects products and is injective (@fd3:thm-rationals-embed-ordered-field), \( (2q)^2 = 2 \) would hold in \( \nQ \), against @fd3:thm-no-rational-square-two.
:::

## Rules for suprema of functions

Suprema are compared more often than they are computed. Each comparison below is one or both halves of the method.

::: {#thm-sup-function-rules}
[Rules for Suprema of Functions]

Let \( f, g \colon D \to \nR \), let \( A \subseteq D \) be **non-empty**, let \( f \) and \( g \) be bounded above on \( A \), and let \( c \in \nR \). All suprema are on \( A \), and \( f + g \), \( cf \), \( \abs{f} \) are as in @def-function-algebra.

::: {.enumerate options="label=(\alph*)"}
1. If \( f(x) \le g(x) \) for every \( x \in A \), then \( \sup f \le \sup g \).
2. \( \sup (f + g) \le \sup f + \sup g \).
3. \( \sup (f + c) = \sup f + c \).
4. If \( c \ge 0 \), then \( \sup (cf) = c \sup f \).
5. If \( f \) is bounded below on \( A \), then \( -f \) is bounded above on \( A \) and \( \sup (-f) = -\inf f \).
6. If \( B \subseteq A \) is non-empty, then \( \sup_B f \le \sup_A f \).
7. If \( f \) and \( g \) are bounded (above and below) on \( A \), then \( \bigl| \sup f - \sup g \bigr| \le \sup \abs{f - g} \).
:::
:::

::: {.idea}
Parts (a), (b) and (f) are inequalities between suprema, so only the bounding half is needed: the right side bounds every value of the left side, and the left supremum is the least such bound. Parts (c) and (d) are equalities and take both halves; (d) treats \( c = 0 \) apart, since a witness for \( cf \) comes from \( \varepsilon/c \). Part (e) is @prp-real-infimum read on the set of values. Part (g) sandwiches \( f \) between \( g \) shifted down and up by the constant \( \sup \abs{f - g} \).
:::

::: {.proof}
Write \( S_f \coloneqq \sup_A f \) and \( S_g \coloneqq \sup_A g \).

(a) For \( x \in A \), \( f(x) \le g(x) \le S_g \). So \( S_g \) is an upper bound of \( f(A) \), and \( S_f \le S_g \) by (S2).

(b) *Bound every value.* For \( x \in A \), \( f(x) \le S_f \) and \( g(x) \le S_g \), so \( f(x) + g(x) \le S_f + S_g \) (@fd3:prp-ordered-ring-rules (b)). So \( f + g \) is bounded above on \( A \), and \( S_f + S_g \) is an upper bound of \( (f + g)(A) \). *Least upper bound.* The supremum is at most every upper bound (S2), so \( \sup (f + g) \le S_f + S_g \).

(c) For \( x \in A \), \( f(x) + c \le S_f + c \). For \( \varepsilon > 0 \), @prp-real-sup-approximation gives \( x \in A \) with \( f(x) > S_f - \varepsilon \), so \( f(x) + c > (S_f + c) - \varepsilon \). By the method, \( \sup (f + c) = S_f + c \).

(d) If \( c = 0 \), then \( cf \) is the constant \( 0 \) on the non-empty set \( A \), so \( \sup (cf) = 0 = 0 \cdot S_f \). Let \( c > 0 \). *Bound every value.* For \( x \in A \), \( f(x) \le S_f \), so \( cf(x) \le c S_f \) (@fd3:prp-ordered-ring-rules (c), with equality allowed). *Find a witness.* Let \( \varepsilon > 0 \). Then \( \varepsilon/c > 0 \), and @prp-real-sup-approximation gives \( x \in A \) with \( f(x) > S_f - \varepsilon/c \); multiplying by \( c > 0 \), \( cf(x) > c S_f - \varepsilon \). By the method, \( \sup (cf) = c S_f \).

(e) Let \( l \) be a lower bound of \( f(A) \). Then \( -f(x) \le -l \) for \( x \in A \), so \( -f \) is bounded above. The set of values of \( -f \) on \( A \) is \( -f(A) \), so \( \sup (-f) = \sup(-f(A)) = -\inf f(A) = -\inf f \) by @prp-real-infimum (b).

(f) \( f(B) \subseteq f(A) \), so \( S_f \) is an upper bound of \( f(B) \), and \( f(B) \) is non-empty. Hence \( f \) is bounded above on \( B \) and \( \sup_B f \le S_f \) by (S2).

(g) If \( \abs{f(x)} \le M \) and \( \abs{g(x)} \le N \) on \( A \), then \( \abs{f(x) - g(x)} \le M + N \) by the triangle inequality (@fd3:prp-absolute-value-ordered-field (e)), so \( d \coloneqq \sup \abs{f - g} \) exists. For \( x \in A \),
\[
f(x) = g(x) + \bigl( f(x) - g(x) \bigr) \le g(x) + \abs{f(x) - g(x)} \le g(x) + d ,
\]
by @fd3:prp-absolute-value-ordered-field (c). By (a) and then (c), \( S_f \le \sup (g + d) = S_g + d \). Swapping \( f \) and \( g \), and using \( \abs{g - f} = \abs{f - g} \), gives \( S_g \le S_f + d \). So \( -d \le S_f - S_g \le d \), which is \( \abs{S_f - S_g} \le d \) by @fd3:prp-absolute-value-ordered-field (d).
:::

Rule (b) bounds the supremum of a sum, and rule (g) says that two functions close at every point have close suprema.

::: {.warning}
**Rule (b) is an inequality, and it can be strict.** On \( [0, 1] \) let \( f(x) = x \) and \( g(x) = 1 - x \). Then \( \sup f = \sup g = 1 \), while \( f + g \) is the constant \( 1 \), so \( \sup (f + g) = 1 < 2 \). The two suprema are reached at different points, \( 1 \) and \( 0 \).
:::

::: {.check}
Which half of the method does rule (f) use, and why is the other half not needed?
:::

::: {.solution}
Only \( (\le) \), bounding every value: every value of \( f \) on \( B \) is a value on \( A \), so \( \sup_A f \) bounds \( f(B) \), and the least upper bound of \( f(B) \) is at most it. No witness is needed because the claim is an inequality, not an equality.
:::

## How far apart can two values be?

For a bounded function, the largest gap between two of its values measures how much the function varies on \( A \). The obvious guess is "the top minus the bottom", and the next result confirms it, with the top and bottom read as supremum and infimum.

::: {#prp-sup-oscillation}
[The Spread of Values]

Let \( A \) be **non-empty** and let \( f \colon D \to \nR \) be bounded (above and below) on \( A \subseteq D \). Then
\[
\sup \bigl\{ \abs{f(x) - f(y)} : x, y \in A \bigr\} = \sup_A f - \inf_A f .
\]
:::

*Try it first (ten minutes): which two points make \( \abs{f(x) - f(y)} \) almost \( \sup_A f - \inf_A f \)?*

::: {.idea}
The natural attempt takes \( x \) where \( f \) is largest and \( y \) where it is smallest. That attempt fails at once: neither point need exist, as the hook function showed. What does exist, for each \( \varepsilon > 0 \), is a point \( x \) with \( f(x) \) within \( \varepsilon/2 \) of the supremum and a point \( y \) with \( f(y) \) within \( \varepsilon/2 \) of the infimum (@prp-real-sup-approximation). Their gap falls short of \( \sup_A f - \inf_A f \) by less than \( \varepsilon/2 + \varepsilon/2 = \varepsilon \). The bounding half is a two-sided trap.

*Before reading on: why \( \varepsilon/2 \), and not \( \varepsilon \)?*
:::

::: {.proof}
Let \( S \coloneqq \sup_A f \) and \( I \coloneqq \inf_A f \), which exist by @def-sup-of-function, and let \( T \coloneqq \{ \abs{f(x) - f(y)} : x, y \in A \} \), a non-empty set.

*Bound every value.* Let \( x, y \in A \). Then \( I \le f(x) \le S \) and \( I \le f(y) \le S \), so \( f(x) - f(y) \le S - I \) and \( f(y) - f(x) \le S - I \). Thus \( -(S - I) \le f(x) - f(y) \le S - I \), and \( \abs{f(x) - f(y)} \le S - I \) by @fd3:prp-absolute-value-ordered-field (d). So \( S - I \) is an upper bound of \( T \).

*Find a witness.* Let \( \varepsilon > 0 \). Then \( \varepsilon/2 > 0 \) (@fd3:prp-ordered-field-halves (b)). By @prp-real-sup-approximation there are \( x \in A \) with \( f(x) > S - \varepsilon/2 \) and \( y \in A \) with \( f(y) < I + \varepsilon/2 \). Then, by @fd3:prp-absolute-value-ordered-field (c),
\[
\abs{f(x) - f(y)} \ge f(x) - f(y) > \Bigl( S - \frac{\varepsilon}{2} \Bigr) - \Bigl( I + \frac{\varepsilon}{2} \Bigr) = (S - I) - \varepsilon .
\]
By @prp-real-sup-approximation, \( \sup T = S - I \).
:::

With \( \varepsilon \) in place of each \( \varepsilon/2 \), the last display would end in \( (S - I) - 2\varepsilon \), and the test asks for \( -\varepsilon \); any two positive tolerances adding up to \( \varepsilon \) would do. The proof never used a point where \( f \) is largest. The result holds for \( x/(1 + x) \) on \( [0, \infty) \), where the spread is \( 1 - 0 = 1 \) and is not attained.

## Polynomials are unbounded

On a set like \( [0, 1] \) many functions are bounded. On all of \( \nR \), no polynomial function of degree at least \( 1 \) is. Chapter 7 proved how fast a complex polynomial grows (@lem-complex-polynomial-growth), and a real polynomial is a complex one whose coefficients happen to be real. Nothing new has to be estimated.

::: {#exm-polynomial-unbounded}
[Polynomials of positive degree are unbounded]

Let \( p = \sum_{j=0}^{d} a_j x^j \in \nR[x] \) with \( d = \deg p \ge 1 \), and put
\[
K \coloneqq \abs{a_0} + \dots + \abs{a_{d-1}} , \qquad R \coloneqq \max\Bigl\{ 1, \frac{2K}{\abs{a_d}} \Bigr\} .
\]
Show: (a) \( \abs{p(x)} \ge \tfrac12 \abs{a_d} \abs{x} \) for every real \( x \) with \( \abs{x} \ge R \); (b) every real root of \( p \) lies in \( (-R, R) \); (c) the polynomial function of \( p \) on \( \nR \) (@def-polynomial-rational-function) is not bounded.
:::

::: {.solution}
Regard \( p \) as an element of \( \nC[x] \), with coefficients \( a_j \in \nR \subseteq \nC \) (@prp-reals-embed-complex). The inclusion respects sums and products, so for real \( x \) the value of \( p \) at \( x \) computed in \( \nC \) is the real number \( p(x) \); and the modulus of a real number is its absolute value (@prp-modulus-of-real). So the numbers \( K \) and \( R \) above are the \( A \) and \( R \) of @lem-complex-polynomial-growth, with \( n = d \).

(a) For real \( x \) with \( \abs{x} \ge R \), the lemma gives \( \abs{p(x)} \ge \tfrac12 \abs{a_d} \abs{x}^d \ge \tfrac12 \abs{a_d} \abs{x} \).

(b) If \( \abs{x} \ge R \), then \( \abs{x} \ge 1 \) and \( a_d \ne 0 \), so (a) gives \( \abs{p(x)} \ge \tfrac12 \abs{a_d} > 0 \), and \( x \) is not a root. So every real root has \( \abs{x} < R \), that is, \( -R < x < R \) (@fd3:prp-absolute-value-ordered-field (d)).

(c) Let \( M \in \nR \) and put \( x \coloneqq R + 2\abs{M}/\abs{a_d} \). Then \( x \ge R > 0 \), so \( \abs{x} = x \ge R \), and (a) gives
\[
\abs{p(x)} \ge \tfrac12 \abs{a_d} \, x = \tfrac12 \abs{a_d} R + \abs{M} > \abs{M} \ge M ,
\]
since \( \tfrac12 \abs{a_d} R > 0 \). So no \( M \) satisfies \( \abs{p(x)} \le M \) for every \( x \in \nR \).
:::

The growth bound says where roots can be, not that one exists: \( x^2 + 1 \) has no real root. That a real polynomial of odd degree has a real root came from factoring, in Chapter 7 (@cor-real-odd-degree-root), and (b) now adds that such a root lies in \( (-R, R) \). For example \( x^3 - 4x + 1 \) has \( K = 5 \) and \( R = 10 \), so its roots lie in \( (-10, 10) \).

::: {.check}
Is \( x^3 - 100x \) bounded on \( [-20, 20] \)? On \( \nR \)?
:::

::: {.solution}
On \( [-20, 20] \), yes: \( \abs{x^3 - 100x} \le \abs{x}^3 + 100\abs{x} \le 8000 + 2000 = 10000 \), by the triangle inequality and \( \abs{x} \le 20 \). On \( \nR \), no, by @exm-polynomial-unbounded (c). Boundedness depends on the set, as in the warning before the method box.
:::

## Suprema over a product

A function of two variables can be bounded in two stages: first over one variable with the other frozen, then over the other. The order of the stages does not matter. Here \( A \) and \( B \) are any sets, not necessarily of numbers, and \( \sup_{A \times B} f \) means \( \sup f(A \times B) \), the supremum of the set of values, as in @def-sup-of-function; likewise for the inner suprema.

::: {#prp-iterated-sup}
[Iterated Suprema]

Let \( A \) and \( B \) be non-empty sets and let \( f \colon A \times B \to \nR \) be bounded above. Then
\[
\sup_{A \times B} f = \sup_{a \in A} \, \sup_{b \in B} f(a, b) = \sup_{b \in B} \, \sup_{a \in A} f(a, b) .
\]
:::

In words: to find the top of a table of numbers, take the top of each row and then the top of those, or the same with columns.

::: {.second-reading title="Suprema over a product"}
::: {.proof}
Let \( S \coloneqq \sup_{A \times B} f \), which exists since \( A \times B \) is non-empty. For fixed \( a \in A \), every \( f(a, b) \) is a value of \( f \), so \( f(a, b) \le S \) for every \( b \in B \); hence \( b \mapsto f(a, b) \) is bounded above on the non-empty \( B \), and \( \varphi(a) \coloneqq \sup_{b \in B} f(a, b) \le S \) by (S2). So \( \varphi \) is bounded above on \( A \) by \( S \), and \( \sup_A \varphi \le S \), again by (S2).

Conversely, for \( (a, b) \in A \times B \), \( f(a, b) \le \varphi(a) \le \sup_A \varphi \). So \( \sup_A \varphi \) is an upper bound of the values of \( f \), and \( S \le \sup_A \varphi \). Hence \( S = \sup_A \varphi \), the first equality. Exchanging the roles of \( A \) and \( B \) gives the second.
:::

If \( B = \{ b_0 \} \) is a singleton, the inner supremum is \( f(a, b_0) \), and the statement says only that \( \sup_{A \times \{b_0\}} f = \sup_{a \in A} f(a, b_0) \): the same set of values, written twice. The hypothesis that \( A \) and \( B \) are non-empty cannot be dropped, since an empty factor makes \( A \times B \) empty and leaves nothing to take the supremum of.
:::

::: {.remark}
[Looking ahead]

*Analysis on the Real Line* calls the number \( \sup_A f - \inf_A f \) of @prp-sup-oscillation the oscillation of \( f \) on \( A \), and measures integrability with it.
:::

## Exercises

### A. Check your understanding

::: {#exr-bounds-and-suprema-a1}
[A1]

This item is about the proof of @prp-sup-oscillation.

::: {.enumerate options="label=(\alph*)"}
1. Run the statement on \( f(x) = x^2 \) on \( A = [-1, 2) \): find \( \sup_A f \), \( \inf_A f \) and the supremum of \( \abs{f(x) - f(y)} \). Is that supremum attained?
2. Which line of the proof uses that \( f \) is bounded below on \( A \)?
3. State the idea of the proof in two sentences.
:::
:::

::: {.solution}
(a) The values of \( x^2 \) on \( [-1, 2) \) form \( [0, 4) \), so \( \sup_A f = 4 \) and \( \inf_A f = 0 \), and the supremum of \( \abs{f(x) - f(y)} \) is \( 4 - 0 = 4 \). It is not attained: both values lie in \( [0, 4) \), so \( \abs{f(x) - f(y)} < 4 \), and equality would need \( f(x) = 4 \), that is, \( x = \pm 2 \), neither of which lies in \( A \).

(b) The choice of \( y \) with \( f(y) < I + \varepsilon/2 \). It needs \( I = \inf_A f \) to exist, which @prp-real-infimum (b) supplies only for a function bounded below; the infimum version of @prp-real-sup-approximation then gives \( y \). (The bounding half also uses \( I \le f(y) \).)

(c) A largest and a smallest value need not exist, so take points whose values are within \( \varepsilon/2 \) of the supremum and of the infimum. Their gap is within \( \varepsilon \) of \( \sup_A f - \inf_A f \), which also bounds every gap.
:::

::: {#exr-bounds-and-suprema-a2}
[A2]

Let \( A \) be non-empty and \( f \) bounded on \( A \). True or false? Give a reason or a counterexample.

::: {.enumerate options="label=(\alph*)"}
1. \( \sup_A f \in f(A) \).
2. \( \inf_A f \le \sup_A f \).
3. \( \sup_A \abs{f} = \max\bigl( \abs{\sup_A f}, \abs{\inf_A f} \bigr) \).
:::
:::

::: {.solution}
(a) False: @exm-sup-not-attained.

(b) True: pick any \( x \in A \), possible since \( A \ne \emptyset \); then \( \inf_A f \le f(x) \le \sup_A f \).

(c) True. Write \( S = \sup_A f \), \( I = \inf_A f \), \( m = \max(\abs{S}, \abs{I}) \). *Bound every value:* \( I \le f(x) \le S \) gives \( f(x) \le \abs{S} \le m \) and \( -f(x) \le -I \le \abs{I} \le m \), so \( \abs{f(x)} \le m \). *Find a witness*, for \( \varepsilon > 0 \). If \( S \ge 0 \) and \( m = \abs{S} = S \), take \( x \) with \( f(x) > S - \varepsilon \); then \( \abs{f(x)} \ge f(x) > m - \varepsilon \). If \( I \le 0 \) and \( m = \abs{I} = -I \), take \( x \) with \( f(x) < I + \varepsilon \); then \( \abs{f(x)} \ge -f(x) > m - \varepsilon \). No other case occurs: \( S < 0 \) forces \( I \le S < 0 \), so \( m = \abs{I} = -I \); and \( I > 0 \) forces \( S \ge I > 0 \), so \( m = \abs{S} = S \).
:::

### B. Practice

::: {#exr-bounds-and-suprema-b1}
[B1]

Let \( A \) be non-empty and \( f, g \) bounded below on \( A \). Here is a proof that \( \inf_A (f + g) \ge \inf_A f + \inf_A g \), with its last step left out.

> For each \( x \in A \), \( f(x) \ge \inf_A f \) and \( g(x) \ge \inf_A g \), so \( f(x) + g(x) \ge \inf_A f + \inf_A g \).

*Name the move, then complete it.*
:::

::: {.solution}
The move is the bounding half of @exm-method-sup-two-halves, mirrored for an infimum, followed by "the infimum is the greatest lower bound". The displayed line shows that \( \inf_A f + \inf_A g \) is a lower bound of \( (f + g)(A) \); in particular \( f + g \) is bounded below on \( A \), so \( \inf_A (f + g) \) exists (@def-sup-of-function). The infimum is greater than or equal to every lower bound (@fd2:def-order-supremum), so \( \inf_A (f + g) \ge \inf_A f + \inf_A g \).
:::

::: {#exr-bounds-and-suprema-b2}
[B2: Prove or disprove]

Let \( A \) be non-empty and \( f, g \) bounded on \( A \). Prove or disprove each statement; all suprema and infima are on \( A \).

::: {.enumerate options="label=(\alph*)"}
1. \( \sup (f + g) = \sup f + \sup g \).
2. \( \sup \max(f, g) = \max(\sup f, \sup g) \).
3. If \( f(x) > 0 \) and \( g(x) > 0 \) for every \( x \in A \), then \( \sup (fg) = \sup f \cdot \sup g \).
4. \( \sup f = -\inf (-f) \).
:::
:::

::: {.solution}
(a) False. On \( [0, 1] \), \( f(x) = x \) and \( g(x) = 1 - x \) give \( \sup (f + g) = 1 \) and \( \sup f + \sup g = 2 \), as in the warning after @thm-sup-function-rules.

(b) True. Let \( m \coloneqq \max(\sup f, \sup g) \). *Bound every value:* \( \max(f(x), g(x)) \) is \( f(x) \le \sup f \le m \) or \( g(x) \le \sup g \le m \). So \( \sup \max(f, g) \le m \). *Other half:* \( f \le \max(f, g) \) and \( g \le \max(f, g) \) on \( A \), so rule (a) of @thm-sup-function-rules gives \( \sup f \le \sup \max(f, g) \) and \( \sup g \le \sup \max(f, g) \), hence \( m \le \sup \max(f, g) \).

(c) False. On \( (0, 1) \) let \( f(x) = x \) and \( g(x) = 1 - x \), both positive. Then \( \sup f = \sup g = 1 \), but \( fg = x(1 - x) \le 1/4 \) by @exm-sup-attained-parabola, with \( \sup (fg) = 1/4 \) attained at \( 1/2 \in (0, 1) \). So \( 1/4 \ne 1 \).

(d) True. \( -f \) is bounded (above and below) on \( A \), and rule (e) of @thm-sup-function-rules applied to \( -f \) gives \( \sup (-(-f)) = -\inf (-f) \), that is, \( \sup f = -\inf(-f) \).
:::

::: {#exr-bounds-and-suprema-b3}
[B3]

Find \( \sup \) and \( \inf \) of \( h(x) = x/(x^2 + 1) \) on \( \nR \), and say whether each is attained. Hence \( \abs{h(x)} \le \tfrac12 \) for every real \( x \).

*Hint: compare \( h(x) \) with \( \tfrac12 \) over a common denominator.*
:::

::: {.solution}
For every real \( x \), \( x^2 + 1 > 0 \), and
\[
\frac12 - \frac{x}{x^2 + 1} = \frac{x^2 - 2x + 1}{2(x^2 + 1)} = \frac{(x - 1)^2}{2(x^2 + 1)} \ge 0 ,
\qquad
\frac{x}{x^2 + 1} + \frac12 = \frac{(x + 1)^2}{2(x^2 + 1)} \ge 0 .
\]
So \( -\tfrac12 \le h(x) \le \tfrac12 \) for every \( x \): every value is bounded. Witnesses: \( h(1) = \tfrac12 \) and \( h(-1) = -\tfrac12 \) are values, each its own witness for every \( \varepsilon \). Hence \( \sup_{\nR} h = \tfrac12 = \max_{\nR} h \) and \( \inf_{\nR} h = -\tfrac12 = \min_{\nR} h \), both attained. The two-sided bound is \( \abs{h(x)} \le \tfrac12 \) by @fd3:prp-absolute-value-ordered-field (d).
:::

::: {#exr-bounds-and-suprema-b4}
[B4: Find the error]

Here is an argument for "\( \sup_A (f + g) = \sup_A f + \sup_A g \) for \( f, g \) bounded above on a non-empty \( A \)."

::: {.enumerate options="label=(\roman*)"}
1. The inequality \( \le \) is rule (b) of @thm-sup-function-rules.
2. For \( \ge \), let \( \varepsilon > 0 \). Choose \( x \in A \) with \( f(x) > \sup f - \varepsilon/2 \) and \( y \in A \) with \( g(y) > \sup g - \varepsilon/2 \).
3. Then \( f(x) + g(y) > \sup f + \sup g - \varepsilon \).
4. So \( \sup f + \sup g \) passes the epsilon test for the values of \( f + g \), and equality holds.
:::

Is the conclusion true? Which line fails, and why?
:::

::: {.solution}
The conclusion is false: @exr-bounds-and-suprema-b2 (a) gives \( f(x) = x \), \( g(x) = 1 - x \) on \( [0, 1] \), with \( 1 \ne 2 \).

Lines (i)–(iii) are correct. Line (iv) fails: the epsilon test needs an element of the set of values \( (f + g)(A) = \{ f(z) + g(z) : z \in A \} \), and \( f(x) + g(y) \) with \( x \ne y \) is not of that form. In the counterexample, \( x = 1 \) and \( y = 0 \) (each a witness for every \( \varepsilon \)) give \( f(1) + g(0) = 2 \), while every value of \( f + g \) is \( 1 \). This is the third usual failure of @exm-method-sup-two-halves.
:::

### C. Going deeper

::: {#exr-bounds-and-suprema-c1}
[C1: Exit check: the supremum of a square]

Let \( A \) be non-empty and let \( f \colon D \to \nR \) be bounded on \( A \subseteq D \), with \( f(x) \ge 0 \) for every \( x \in A \). Prove that \( \sup_A f^2 = \bigl( \sup_A f \bigr)^2 \).
:::

::: {.solution}
[Hint 1]

Use both halves of @exm-method-sup-two-halves, with \( s \coloneqq \sup_A f \).
:::

::: {.solution}
[Hint 2]

For the witness, aim at \( f(x) > s - \delta \) and expand \( (s - \delta)^2 \); then choose \( \delta \) from \( \varepsilon \) and \( s \).
:::

::: {.solution}
Let \( s \coloneqq \sup_A f \). Since \( A \ne \emptyset \) and \( f \ge 0 \) on \( A \), \( s \ge f(x) \ge 0 \) for any \( x \in A \).

*Bound every value.* For \( x \in A \), \( 0 \le f(x) \le s \), so \( f(x)^2 \le s^2 \) by @fd3:prp-ordered-field-halves (d), applied with both factors equal. So \( f^2 \) is bounded above on \( A \) by \( s^2 \).

*Find a witness.* Let \( \varepsilon > 0 \). If \( s = 0 \), then \( f(x) = 0 \) on \( A \), so \( f^2 \) is the constant \( 0 \) and any \( x \in A \) has \( f(x)^2 = 0 > s^2 - \varepsilon \). Let \( s > 0 \) and put \( \delta \coloneqq \varepsilon/(2s) > 0 \), chosen from \( \varepsilon \) and \( s \). By @prp-real-sup-approximation there is \( x \in A \) with \( f(x) > s - \delta \).

*Case \( s - \delta \ge 0 \).* Then \( 0 \le s - \delta < f(x) \), so \( (s - \delta)^2 < f(x)^2 \) by @fd3:prp-ordered-ring-rules (g), and
\[
(s - \delta)^2 = s^2 - 2s\delta + \delta^2 = s^2 - \varepsilon + \delta^2 > s^2 - \varepsilon .
\]
So \( f(x)^2 > s^2 - \varepsilon \).

*Case \( s - \delta < 0 \).* Then \( s < \delta = \varepsilon/(2s) \), so \( s^2 < \varepsilon/2 \), and \( s^2 - \varepsilon < -\varepsilon/2 < 0 \le f(x)^2 \).

In every case \( f(x)^2 > s^2 - \varepsilon \). By the method, \( \sup_A f^2 = s^2 \).

The hypothesis \( f \ge 0 \) is needed: \( f(x) = x \) on \( [-2, 1] \) has \( \sup f = 1 \), but \( \sup f^2 = 4 \).

**Marking scheme.** (10 points)

- 2: names \( s = \sup_A f \) and states both halves as the goal (every \( f(x)^2 \le s^2 \); for every \( \varepsilon > 0 \) some \( f(x)^2 > s^2 - \varepsilon \)).
- 3: proves the bounding half, naming the nonnegativity of \( f(x) \) (and of \( s \)) as what allows squaring the inequality.
- 3: chooses the witness tolerance from \( \varepsilon \) (and \( s \)) before taking the witness, and verifies \( f(x)^2 > s^2 - \varepsilon \).
- 2: handles the cases the choice leaves open (\( s = 0 \), and \( s - \delta < 0 \) or its equivalent in another route).

Fatal errors (0 for the step): squaring an inequality between numbers that may be negative; a witness that does not depend on \( \varepsilon \); dividing by \( s \) without treating \( s = 0 \). A route that writes \( f(x)^2 - s^2 = (f(x) - s)(f(x) + s) \) and bounds \( \abs{f(x) + s} \le 2s \) earns the same points for the same steps.
:::

::: {#exr-bounds-and-suprema-c2}
[C2]

Let \( a < b \), \( L \ge 0 \), and let \( f \colon [a, b] \to \nR \) satisfy \( \abs{f(x) - f(y)} \le L \abs{x - y} \) for all \( x, y \in [a, b] \). Here is the first half of a proof that \( f \) is bounded and \( \sup f - \inf f \le L(b - a) \), all suprema on \( [a, b] \).

> For \( x \in [a, b] \), \( \abs{f(x)} \le \abs{f(a)} + \abs{f(x) - f(a)} \le \abs{f(a)} + L(x - a) \le \abs{f(a)} + L(b - a) \), so \( f \) is bounded. By @prp-sup-oscillation, \( \sup f - \inf f = \sup \{ \abs{f(x) - f(y)} : x, y \in [a, b] \} \), so it suffices to bound this supremum.

*Name the move, then complete it.*
:::

::: {.solution}
The move is the bounding half of @exm-method-sup-two-halves, followed by "the supremum is the least upper bound".

*Bound every value.* Let \( x, y \in [a, b] \). Both lie between \( a \) and \( b \), so \( -(b - a) \le x - y \le b - a \), that is, \( \abs{x - y} \le b - a \) (@fd3:prp-absolute-value-ordered-field (d)). Since \( L \ge 0 \),
\[
\abs{f(x) - f(y)} \le L \abs{x - y} \le L(b - a) .
\]
So \( L(b - a) \) is an upper bound of \( \{ \abs{f(x) - f(y)} : x, y \in [a, b] \} \), and its supremum is at most \( L(b - a) \) by (S2). Hence \( \sup f - \inf f \le L(b - a) \).

(The first half used the triangle inequality, @fd3:prp-absolute-value-ordered-field (e), and \( 0 \le x - a \le b - a \).) The bound can be an equality: \( f(x) = Lx \) has \( \sup f - \inf f = Lb - La \).
:::

<!-- dependency ledger
prp-real-infimum (proof): l <= a iff -a <= -l (the case of equality added to the strict rule) | fd3:prp-ordered-ring-rules (a) (cited)
prp-real-sup-approximation (proof): not (a <= t) implies a > t | totality, fd3:prp-ordered-ring-rules (i) (cited)
def-bounded-function (claim): from L <= f(x) <= U on A, M = max(|L|, |U|) bounds |f| | fd3:prp-absolute-value-ordered-field (c), (d); fd3:prp-ordered-ring-rules (a)
def-bounded-function (example): 1/(|M| + 1) lies in (0, 1] and its reciprocal is |M| + 1 > M | |M| >= 0 (fd3:prp-absolute-value-ordered-field (a)), fd3:prp-ordered-field-halves (c)
def-sup-of-function (claim): an attained supremum is the largest value and conversely | fd2:def-order-supremum (S1), (S2), inline
exm-sup-not-attained (solution): (1/eps)/(1 + 1/eps) = 1/(1 + eps); (1 - eps)(1 + eps) = 1 - eps^2; dividing an inequality by 1 + eps > 0 | fd3:lem-field-fraction-rules; fd3:prp-ordered-ring-rules (c); verify/ch08/exm-sup-not-attained.py
exm-sup-not-attained (example): the hook values f(0), f(1), f(9), f(99), the scratch-work equivalence x > 1/eps - 1, and Quick check 2 (f(1/2) = 1/3) | verify/ch08/exm-sup-not-attained.py
exm-sup-attained-parabola (solution): x(1 - x) = 1/4 - (x - 1/2)^2; squares are >= 0 | fd3:prp-ordered-ring-rules (e); verify/ch08/exm-sup-attained-parabola.py
exm-sup-attained-parabola (claim): Quick check 3: x^2 on (-1, 2) takes exactly the values [0, 4) | x^2 = t for t in [0, 4) by sqrt t in [0, 2) (fd3:prp-cof-square-roots); x^2 < 4 by fd3:prp-ordered-ring-rules (g) applied to |x| < 2, with |x|^2 = x^2 (fd3:prp-absolute-value-ordered-field (b)); verify/ch08/exm-sup-attained-parabola.py
exm-sup-attained-parabola (claim): Quick check 3: 0 <= sqrt 2 <= 2, and sqrt2 = 2q with q rational would give (2q)^2 = 2 in Q | fd3:prp-ordered-ring-rules (g) (sqrt2^2 = 2 <= 4 = 2^2); fd3:thm-rationals-embed-ordered-field (cited)
thm-sup-function-rules (proof): (d) multiplying an inequality by c > 0 keeps it, also for <= | fd3:prp-ordered-ring-rules (c) (cited), equality case inline
thm-sup-function-rules (proof): (e) the values of -f on A form -f(A) | fd2:exm-sets-of-numbers-as-images (definition of -A), inline
thm-sup-function-rules (proof): (g) |g - f| = |f - g| | fd3:prp-absolute-value-ordered-field (b)
thm-sup-function-rules (example): warning: x + (1 - x) = 1, sup x = sup (1 - x) = 1 on [0, 1] | inline (attained at 1 and 0); verify/ch08/thm-sup-function-rules.py
prp-sup-oscillation (claim): sup x/(1+x) - inf x/(1+x) = 1 - 0 on [0, infinity) | exm-sup-not-attained (cited)
exm-polynomial-unbounded (solution): for real x, the value of p at x computed in C is the real p(x), since the inclusion R -> C respects sums and products | prp-reals-embed-complex (cited), inline (evaluation is built from sums and products, def-polynomial-evaluation)
exm-polynomial-unbounded (solution): |x|^d >= |x| for |x| >= 1 | part of the second inequality of lem-complex-polynomial-growth (cited)
exm-polynomial-unbounded (example): x^3 - 4x + 1: K = 5, R = 10 | verify/ch08/exm-polynomial-unbounded.py
exm-polynomial-unbounded (claim): x^2 + 1 has no real root (x^2 + 1 >= 1 > 0) | fd3:prp-ordered-ring-rules (e)
exm-polynomial-unbounded (claim): Quick check 5: |x^3 - 100x| <= 8000 + 2000 on [-20, 20] | triangle inequality fd3:prp-absolute-value-ordered-field (e), |x|^3 <= 20^3 by fd3:prp-ordered-field-halves (d); verify/ch08/exm-polynomial-unbounded.py
prp-iterated-sup (proof): A x B non-empty when A, B are | fd2:def-cartesian-product (cited in 8.1), inline
exr-bounds-and-suprema-a1 (solution): values of x^2 on [-1, 2) are [0, 4); a difference of two numbers in [0, 4) has absolute value < 4 | as in Quick check 3; fd3:prp-absolute-value-ordered-field (d); verify/ch08/exr-bounds-and-suprema-a1.py
exr-bounds-and-suprema-a2 (solution): (c) case analysis on the signs of S and I | inline; verify/ch08/exr-bounds-and-suprema-a2.py (sample functions)
exr-bounds-and-suprema-b2 (solution): (c) x(1 - x) <= 1/4 on (0, 1), attained at 1/2 | exm-sup-attained-parabola (cited); verify/ch08/exr-bounds-and-suprema-b2.py
exr-bounds-and-suprema-b3 (solution): 1/2 - x/(x^2+1) = (x-1)^2/(2(x^2+1)), x/(x^2+1) + 1/2 = (x+1)^2/(2(x^2+1)); h(1) = 1/2, h(-1) = -1/2 | verify/ch08/exr-bounds-and-suprema-b3.py
exr-bounds-and-suprema-b4 (solution): f(1) + g(0) = 2, f + g = 1 on [0, 1] | inline; verify/ch08/thm-sup-function-rules.py
exr-bounds-and-suprema-c1 (solution): (s - delta)^2 = s^2 - eps + delta^2 for delta = eps/(2s); s < eps/(2s) gives s^2 < eps/2; the counterexample x on [-2, 1] | fd3:prp-ordered-ring-rules (c) (multiplying s < eps/(2s) by s > 0); verify/ch08/exr-bounds-and-suprema-c1.py
exr-bounds-and-suprema-c2 (solution): x, y in [a, b] give -(b - a) <= x - y <= b - a; multiplying |x - y| <= b - a by L >= 0 | fd3:prp-ordered-ring-rules (b), (c); equality case f = Lx: sup - inf = L(b - a) on [a, b], inline (Lx increasing for L >= 0)
-->
