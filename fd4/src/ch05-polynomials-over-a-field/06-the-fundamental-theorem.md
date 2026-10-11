# The Fundamental Theorem of Algebra

Over \( \nQ \) the polynomial \( x^2 - 2 \) has no root, and over \( \nR \) the polynomial \( x^2 + 1 \) has none. Chapter 1 announced that over \( \nC \) this stops: every non-constant complex polynomial has a root. This section proves it, and then reads off what it says about factoring complex and real polynomials.

No argument from the field axioms alone can prove the theorem. The field \( \nQ(i) = \{ a + bi : a, b \in \nQ \} \) of @exm-subfields-gaussian satisfies every field axiom, and it contains an element \( i \) with \( i^2 = -1 \), just as \( \nC \) does. Yet \( x^2 - 2 \) has no root in it. If \( (a + bi)^2 = 2 \) with \( a, b \in \nQ \), then comparing real and imaginary parts (@def-complex-numbers), \( a^2 - b^2 = 2 \) and \( 2ab = 0 \), so \( a = 0 \) or \( b = 0 \) (\( \nQ \) has no zero divisors, @thm-field-basic-properties (f), and \( 2 \ne 0 \)). If \( b = 0 \), then \( a^2 = 2 \), which no rational satisfies (@fd3:thm-no-rational-square-two). If \( a = 0 \), then \( -b^2 = 2 \), impossible since \( -b^2 \le 0 \) (@fd3:prp-ordered-ring-rules (e)). So the proof must use a property of \( \nR \) that \( \nQ \) lacks. It is the supremum property of *Number Systems: From \( \nN \) to \( \nR \)*, Chapter 5 (@fd3:thm-reals-complete-ordered-field).

The plan has two halves. First, \( \abs{p} \) attains a smallest value on \( \nC \) (@thm-complex-polynomial-minimum). Second, at any point where \( p \) is not \( 0 \), some nearby point gives \( \abs{p} \) a smaller value (@lem-complex-polynomial-descent). So at a point where the smallest value is attained, \( p \) must be \( 0 \). The first half is where completeness is invoked directly (Steps 2 and 5); the second half uses it only indirectly, through square roots (see the remark after the minimum theorem).

Throughout, \( p \) is a polynomial in \( \nC[x] \), and \( p(z) \) is its value at \( z \in \nC \) (@def-polynomial-evaluation). Inequalities are between real numbers; the modulus \( \abs{z} \) is a non-negative real (@def-conjugate-modulus).

## Two estimates

::: {.second-reading title="The facts about the modulus used in this section"}
All of them are from Chapter 1. For \( z, w \in \nC \): \( \abs{z}^2 = (\operatorname{Re} z)^2 + (\operatorname{Im} z)^2 \) (@def-conjugate-modulus); \( \abs{\operatorname{Re} z} \le \abs{z} \), \( \abs{\operatorname{Im} z} \le \abs{z} \) and \( \abs{z} \le \abs{\operatorname{Re} z} + \abs{\operatorname{Im} z} \) (@lem-real-part-at-most-modulus); \( \abs{zw} = \abs{z} \abs{w} \), so \( \abs{z^j} = \abs{z}^j \) by induction on \( j \), and \( \abs{z} = 0 \) only for \( z = 0 \) (@thm-conjugate-properties (d), (e)); \( \abs{z_1 + \dots + z_m} \le \abs{z_1} + \dots + \abs{z_m} \) and \( \abs{z} - \abs{w} \le \abs{z + w} \) (@cor-complex-triangle-variants (b), (c)). For a real number the modulus is the absolute value of *Number Systems: From \( \nN \) to \( \nR \)*, Chapter 4 (@prp-modulus-of-real), so the rules of @fd3:prp-absolute-value-ordered-field apply to it.

Three facts about powers of non-negative reals are used as well, each by induction on the exponent with @fd3:prp-ordered-ring-rules (c): if \( 0 \le a \le b \), then \( a^j \le b^j \); if \( a \ge 1 \) and \( i \le j \), then \( a^i \le a^j \); if \( 0 < t \le 1 \) and \( i \le j \), then \( t^j \le t^i \).
:::

The first estimate says that \( \abs{p(z)} \) is large when \( \abs{z} \) is large, so the search for a smallest value can be confined to a bounded region.

::: {#lem-complex-polynomial-growth}
[Growth of a Complex Polynomial]

Let \( p = \sum_{j=0}^{n} a_j x^j \in \nC[x] \) with \( n = \deg p \ge 1 \), so \( a_n \ne 0 \). Let
\[
A \coloneqq \abs{a_0} + \dots + \abs{a_{n-1}} , \qquad R \coloneqq \max\Bigl\{ 1, \frac{2A}{\abs{a_n}} \Bigr\} .
\]
Then for every \( z \in \nC \) with \( \abs{z} \ge R \),
\[
\abs{p(z)} \ge \tfrac12 \abs{a_n} \abs{z}^n \ge \tfrac12 \abs{a_n} \abs{z} .
\]
:::

*In words: beyond the radius \( R \), the top term outweighs all the others together, at least by half.*

::: {.second-reading title="The proof: the top term against the rest"}
::: {.proof}
Let \( \abs{z} \ge R \). Then \( \abs{z} \ge 1 \), so \( \abs{z}^j \le \abs{z}^{n-1} \) for \( 0 \le j \le n - 1 \). Write \( p(z) = a_n z^n + w \) with \( w \coloneqq \sum_{j=0}^{n-1} a_j z^j \) (the sum recursion). By @cor-complex-triangle-variants (b) and @thm-conjugate-properties (d),
\[
\abs{w} \le \sum_{j=0}^{n-1} \abs{a_j} \abs{z}^j \le A \abs{z}^{n-1} .
\]
By @cor-complex-triangle-variants (c), which is the reverse triangle inequality (a) with the second number negated, \( \abs{p(z)} \ge \abs{a_n} \abs{z}^n - \abs{w} \ge \abs{z}^{n-1} \bigl( \abs{a_n} \abs{z} - A \bigr) \). Since \( \abs{z} \ge 2A/\abs{a_n} \) and \( \abs{a_n} > 0 \), \( A \le \tfrac12 \abs{a_n} \abs{z} \), so \( \abs{a_n} \abs{z} - A \ge \tfrac12 \abs{a_n} \abs{z} \). Hence \( \abs{p(z)} \ge \tfrac12 \abs{a_n} \abs{z}^n \). Finally \( \abs{z}^n \ge \abs{z} \), since \( \abs{z} \ge 1 \) and \( n \ge 1 \).
:::
:::

The second estimate replaces continuity, which this volume does not have. It bounds how much \( p \) can change between two points of a bounded region, with an explicit constant.

::: {#lem-complex-polynomial-lipschitz}
[A Lipschitz Bound for a Complex Polynomial]

Let \( p = \sum_{j=0}^{n} a_j x^j \in \nC[x] \) and let \( M \in \nR \) with \( M \ge 0 \). Put
\[
L \coloneqq \sum_{j=1}^{n} j \abs{a_j} M^{j-1} \qquad (j \abs{a_j} \text{ the multiple } (j \cdot 1)\abs{a_j} \text{ in } \nR) .
\]
Then \( \abs{p(z) - p(w)} \le L \abs{z - w} \) for all \( z, w \in \nC \) with \( \abs{z} \le M \) and \( \abs{w} \le M \).
:::

*In words: on the disc of radius \( M \), \( p \) moves at most \( L \) times as far as its argument.*

::: {.second-reading title="The proof: factor each difference of powers"}
::: {.proof}
Let \( \abs{z}, \abs{w} \le M \). Termwise (the sum rules (Σ1), (Σ2), (Σ4) of @lem-finite-sums-and-powers), \( p(z) - p(w) = \sum_{j=0}^{n} a_j (z^j - w^j) \), and the term \( j = 0 \) is \( 0 \). For \( j \ge 1 \), @lem-difference-of-powers gives
\[
z^j - w^j = (z - w) \sum_{i=0}^{j-1} z^i w^{j-1-i} .
\]
Each of the \( j \) terms of the sum has modulus \( \abs{z}^i \abs{w}^{j-1-i} \le M^i M^{j-1-i} = M^{j-1} \). So \( \abs{z^j - w^j} \le j M^{j-1} \abs{z - w} \) by @cor-complex-triangle-variants (b), and summing over \( j \) with the same corollary, \( \abs{p(z) - p(w)} \le \sum_{j=1}^{n} \abs{a_j} \, j M^{j-1} \abs{z - w} = L \abs{z - w} \).
:::
:::

This is the only "continuity" the proof below needs, and it comes with a constant that can be computed.

::: {.check}
For \( p = x^2 + 1 \), compute \( A \) and \( R \) of @lem-complex-polynomial-growth, and the constant \( L \) of @lem-complex-polynomial-lipschitz for \( M = 4 \).
:::

::: {.solution}
Here \( a_0 = 1 \), \( a_1 = 0 \), \( a_2 = 1 \), \( n = 2 \). So \( A = \abs{1} + \abs{0} = 1 \) and \( R = \max\{1, 2 \cdot 1/1\} = 2 \). For \( M = 4 \), \( L = 1 \cdot 0 \cdot 4^0 + 2 \cdot 1 \cdot 4^1 = 8 \). (Check of the Lipschitz bound in one case: \( \abs{p(z) - p(w)} = \abs{z^2 - w^2} = \abs{z + w} \abs{z - w} \le 8 \abs{z - w} \) when \( \abs{z}, \abs{w} \le 4 \).)
:::

## The smallest value of the modulus is attained

We now look for a point where \( \abs{p} \) is smallest. The infimum of the values \( \abs{p(z)} \) exists by completeness; the work is to find a point **at** which it is attained. We trap such a point in smaller and smaller squares.

For \( \sigma, \tau \in \nR \) and \( s \in \nR \) with \( s > 0 \), let
\[
S(\sigma, \tau, s) \coloneqq \{ z \in \nC : \sigma \le \operatorname{Re} z \le \sigma + s , \ \tau \le \operatorname{Im} z \le \tau + s \} ,
\]
the closed square with lower-left corner \( \sigma + \tau i \) and side \( s \). (In this section \( \sigma \) and \( \tau \) are real numbers. Chapter 3 uses the same letters for permutations, which do not appear here.) Each such square contains its corner, so it is non-empty. Its four **quarters**, in this fixed order, are
\[
\begin{aligned}
&S(\sigma, \tau, s/2) , && S(\sigma + s/2, \tau, s/2) , \\
&S(\sigma, \tau + s/2, s/2) , && S(\sigma + s/2, \tau + s/2, s/2) .
\end{aligned}
\]
Each quarter lies in the square, and every point of the square lies in some quarter: \( \operatorname{Re} z \le \sigma + s/2 \) or \( \operatorname{Re} z \ge \sigma + s/2 \), and likewise for \( \operatorname{Im} z \), since \( \le \) is a total order on \( \nR \) (@fd3:prp-ordered-ring-rules (i)).

::: {#thm-complex-polynomial-minimum}
[The Modulus of a Complex Polynomial Attains Its Minimum]

For every \( p \in \nC[x] \) there is \( z^* \in \nC \) with \( \abs{p(z^*)} \le \abs{p(z)} \) for **every** \( z \in \nC \).
:::

::: {.idea}
Confine the search to one big square \( S_0 \) by the growth lemma. The infimum \( m \) of \( \abs{p} \) over \( S_0 \) exists. Cut \( S_0 \) into four quarters: the infimum over \( S_0 \) is the least of the four infima, so some quarter has the **same** infimum \( m \); keep the first such quarter, and repeat. We call this move **keep the quarter that keeps the infimum**. The squares shrink to a single point \( z^* \), which completeness supplies as a supremum of corners. Near \( z^* \) every square still has points where \( \abs{p} \) is almost \( m \), and the Lipschitz bound says \( \abs{p(z^*)} \) is almost the same; so \( \abs{p(z^*)} = m \). This is the bisection of *Number Systems: From \( \nN \) to \( \nR \)*, Chapter 5, now in the plane. *Before reading on: why keep a quarter whose **infimum** equals the square's, rather than a quarter containing a point where \( \abs{p} \) is smallest?*
:::

::: {.proof}
If \( p \) is a constant \( a_0 \) (including \( 0 \)), then \( p(z) = a_0 \) for every \( z \), and \( z^* \coloneqq 0 \) works. Let \( n \coloneqq \deg p \ge 1 \), with leading coefficient \( a_n \ne 0 \), let \( R \) be as in @lem-complex-polynomial-growth, and let
\[
\rho \coloneqq \max\Bigl\{ R, \frac{2\abs{p(0)}}{\abs{a_n}} \Bigr\} ,
\]
so \( \rho \ge 1 \).

**Step 1 (a square that suffices).** Let \( S_0 \coloneqq S(-\rho, -\rho, 2\rho) \). It contains \( 0 \). If \( z \notin S_0 \), then \( \abs{\operatorname{Re} z} > \rho \) or \( \abs{\operatorname{Im} z} > \rho \) (@fd3:prp-absolute-value-ordered-field (d)), so \( \abs{z} > \rho \ge R \) (@lem-real-part-at-most-modulus), and by @lem-complex-polynomial-growth,
\[
\abs{p(z)} \ge \tfrac12 \abs{a_n} \abs{z} > \tfrac12 \abs{a_n} \rho \ge \abs{p(0)} . \tag{1}
\]

**Step 2 (the infimum; completeness, first use).** For a square \( S \), the set \( V(S) \coloneqq \{ \abs{p(z)} : z \in S \} \subseteq \nR \) is non-empty and bounded below by \( 0 \). So it has an infimum \( m(S) \) in \( \nR \) (@fd2:def-order-supremum); the fold after the proof derives this from the supremum property. Two consequences are used: \( m(S) \le \abs{p(z)} \) for every \( z \in S \); and for every \( \varepsilon > 0 \) there is \( z \in S \) with \( \abs{p(z)} < m(S) + \varepsilon \), since otherwise \( m(S) + \varepsilon \) would be a lower bound of \( V(S) \) larger than the greatest one. If \( S' \subseteq S \), then \( m(S) \) is a lower bound of \( V(S') \subseteq V(S) \), so \( m(S) \le m(S') \).

**Step 3 (a quarter with the same infimum).** Let \( S \) be a square and \( Q_1, \dots, Q_4 \) its quarters. Each \( m(Q_i) \ge m(S) \) by Step 2. Let \( \mu \) be the least of the four numbers \( m(Q_i) \). Every \( z \in S \) lies in some \( Q_i \), so \( \abs{p(z)} \ge m(Q_i) \ge \mu \): \( \mu \) is a lower bound of \( V(S) \), hence \( \mu \le m(S) \). So \( \mu = m(S) \), and some quarter has \( m(Q_i) = m(S) \). Let \( q(S) \) be the **first** quarter, in the fixed order, with \( m(Q_i) = m(S) \). This is a rule: \( q \) is a function from squares to squares.

**Step 4 (the nested squares).** Identify the square \( S(\sigma, \tau, s) \) with the triple \( (\sigma, \tau, s) \). By @fd2:thm-recursion (read on \( \nN = \omega \) through @fd3:cor-omega-identification), there is exactly one sequence of squares \( S_k = S(\sigma_k, \tau_k, s_k) \), \( k \in \nN \), with \( S_0 \) as in Step 1 and \( S_{k+1} = q(S_k) \). By induction on \( k \):

- \( s_k = 2\rho/2^k \), the power \( 2^k \) taken in \( \nR \) (@fd3:def-naturals-in-ordered-field), since each quarter has half the side;
- \( m(S_k) = m \), where \( m \coloneqq m(S_0) \), by the choice of \( q \);
- \( \sigma_k \le \sigma_{k'} \le \sigma_k + s_k - s_{k'} \) and \( \tau_k \le \tau_{k'} \le \tau_k + s_k - s_{k'} \) for all \( k' \ge k \), since the corner of a quarter is \( \sigma \) or \( \sigma + s/2 \) and its far edge \( \sigma + s/2 \) or \( \sigma + s \). In particular \( S_{k'} \subseteq S_k \subseteq S_0 \).

**Step 5 (the common point; completeness, second use).** The set \( \{ \sigma_k : k \in \nN \} \) is non-empty and bounded above by \( \sigma_0 + s_0 \) (Step 4 with \( k = 0 \)). By @fd3:thm-reals-complete-ordered-field it has a supremum \( \sigma^* \) (@fd3:def-complete-ordered-field). Fix \( k \). Then \( \sigma_k \le \sigma^* \), and \( \sigma_k + s_k \) is an upper bound of the set: for \( k' \ge k \), \( \sigma_{k'} \le \sigma_k + s_k \) by Step 4, and for \( k' < k \), \( \sigma_{k'} \le \sigma_k \) by Step 4 with the roles of \( k \) and \( k' \) exchanged. So \( \sigma_k \le \sigma^* \le \sigma_k + s_k \) for every \( k \). In the same way \( \tau^* \coloneqq \sup \{ \tau_k : k \in \nN \} \) satisfies \( \tau_k \le \tau^* \le \tau_k + s_k \). Hence \( z^* \coloneqq \sigma^* + \tau^* i \) lies in every \( S_k \).

**Step 6 (the value at the common point).** For \( z, w \in S_k \), \( \abs{\operatorname{Re}(z - w)} \le s_k \) and \( \abs{\operatorname{Im}(z - w)} \le s_k \), so \( \abs{z - w} \le 2 s_k \) (@lem-real-part-at-most-modulus). Every point of \( S_0 \) has modulus at most \( \rho + \rho = 2\rho \), by the same lemma. Let \( L \) be the constant of @lem-complex-polynomial-lipschitz for \( M = 2\rho \).

Let \( \varepsilon \in \nR \) with \( \varepsilon > 0 \). By @fd3:thm-constructed-reals-archimedean there is \( k \in \nN \) with \( k > 8\rho L/\varepsilon \); then \( 2^k \ge k + 1 > 8\rho L/\varepsilon \) by @fd3:lem-power-two-bound, so
\[
2 s_k L = \frac{4\rho L}{2^k} < \frac{\varepsilon}{2} . \tag{2}
\]
This \( k \) depends on \( \varepsilon \) (and on \( p \), through \( \rho \) and \( L \)). Since \( m(S_k) = m \), Step 2 gives a point \( w \in S_k \) with \( \abs{p(w)} < m + \varepsilon/2 \) (\( \rulename{\exists E} \): the point \( w \) is used only inside this argument for this \( \varepsilon \)). Both \( z^* \) and \( w \) lie in \( S_k \subseteq S_0 \), so by the triangle inequality (@thm-complex-triangle-inequality), the Lipschitz bound and (2),
\[
\abs{p(z^*)} \le \abs{p(w)} + \abs{p(z^*) - p(w)} < m + \frac{\varepsilon}{2} + L \cdot 2 s_k < m + \varepsilon .
\]
As \( \varepsilon > 0 \) was arbitrary, \( \abs{p(z^*)} \le m \): otherwise \( \varepsilon \coloneqq \abs{p(z^*)} - m > 0 \) would give \( \abs{p(z^*)} < \abs{p(z^*)} \). Also \( \abs{p(z^*)} \ge m \), since \( z^* \in S_0 \). So \( \abs{p(z^*)} = m \).

**Step 7 (the minimum over all of the plane).** Let \( z \in \nC \). If \( z \in S_0 \), then \( \abs{p(z)} \ge m = \abs{p(z^*)} \). If \( z \notin S_0 \), then \( \abs{p(z)} > \abs{p(0)} \ge m \) by (1), since \( 0 \in S_0 \). This proves the theorem.
:::

::: {.second-reading title="Step 2: why the infimum exists"}
Let \( V \subseteq \nR \) be non-empty and bounded below by \( 0 \), and let \( B \) be the set of lower bounds of \( V \). Then \( 0 \in B \), and every element of \( V \) is an upper bound of \( B \), so \( B \) is non-empty and bounded above; by @fd3:thm-reals-complete-ordered-field it has a supremum \( m \) (@fd3:def-complete-ordered-field). Each \( v \in V \) is an upper bound of \( B \), so \( m \le v \): \( m \) is a lower bound of \( V \). Each lower bound \( u \) of \( V \) is in \( B \), so \( u \le m \). Thus \( m \) is the greatest lower bound of \( V \), its infimum in the sense of @fd2:def-order-supremum.
:::

*The answer to the prompt.* A quarter containing a point where \( \abs{p} \) is smallest is what the theorem is trying to prove exists, so it cannot be used to choose quarters. The infimum of a quarter always exists, by completeness, and Step 3 shows that some quarter keeps it. Choosing "the first such quarter in a fixed order" makes the step a rule, so the recursion theorem applies and no choice is made at any stage; compare @fd3:exm-representatives-need-choice, where a proof that picks infinitely many objects without a rule uses the axiom of choice.

::: {.remark}
The supremum property is invoked directly in Steps 2 and 5 and nowhere else in this chapter. It also enters indirectly, through the non-negative real square roots of @fd3:prp-cof-square-roots, which that result derives from the supremum: they give the modulus used in every inequality of this section, and the complex square roots of @prp-complex-square-roots used in the next lemma. In \( \nQ(i) \), with \( \nQ \) in place of \( \nR \), both fail; Exercise C1 (c) asks where.
:::

::: {.check}
In Step 3, why does it matter that there are only **four** quarters?
:::

::: {.solution}
The proof takes \( \mu \), the least of the numbers \( m(Q_1), \dots, m(Q_4) \). A finite list of real numbers has a least element, so \( \mu \) exists and equals one of them; that is what produces a quarter with \( m(Q_i) = m(S) \). With infinitely many pieces, the infimum of their infima need not be attained by any one piece.
:::

## A direction in which the modulus decreases

The second half of the plan is algebra, together with complex square roots (@prp-complex-square-roots). Near a point \( z_0 \), write \( p(z_0 + h) = b_0 + b_k h^k + (\text{higher powers of } h) \), with \( b_0 = p(z_0) \). If we can choose the direction of \( h \) so that \( b_k h^k \) points back toward \( 0 \) from \( b_0 \), and \( h \) so small that the higher terms do not undo the gain, then \( \abs{p} \) decreases. Dividing by \( b_0 \), the first need is a \( \zeta \) for which \( c\zeta^k \) has negative real part.

::: {#lem-complex-direction-negative-real-part}
[A Direction with Negative Real Part]

Let \( c \in \nC \) with \( c \ne 0 \), and let \( k \in \nN \) with \( k \ge 1 \). Then there is \( \zeta \in \nC \) with \( \operatorname{Re}(c\zeta^k) < 0 \).
:::

*Try it first (ten minutes): for \( c = i \), find \( \zeta \) with \( \operatorname{Re}(c\zeta^3) < 0 \). Then find \( \zeta \) with \( \operatorname{Re}(c\zeta^2) < 0 \).*

::: {.idea}
For \( k = 3 \), the four "axis" directions \( \zeta \in \{1, -1, i, -i\} \) already turn \( c \) around: \( \zeta^3 \) runs through \( 1, -1, -i, i \), and \( i \cdot i = -1 \). For \( k = 2 \) they do not: \( \zeta^2 \in \{1, -1\} \) for these four, and \( c\zeta^2 \in \{i, -i\} \) has real part \( 0 \). What works for \( k = 2 \) is a square root of a direction that works for \( k = 1 \): \( \eta = i \) gives \( \operatorname{Re}(i \cdot i) = -1 \), and if \( \zeta^2 = \eta \), then \( c\zeta^2 = c\eta \). So odd \( k \) is handled by the axes, and even \( k = 2j \) by a square root of a direction for \( j \), which is strong induction. Square roots of complex numbers come from real square roots (@prp-complex-square-roots), so no polar form is needed.
:::

::: {.second-reading title="The proof: the axes for odd k, a square root for even k"}
::: {.proof}
We prove, by strong induction on \( k \) (@fd1:thm-strong-induction, on \( \nN = \omega \)), the statement: if \( k \ge 1 \), then for every non-zero \( c \in \nC \) there is \( \zeta \) with \( \operatorname{Re}(c\zeta^k) < 0 \). For \( k = 0 \) there is nothing to prove. Let \( k \ge 1 \), assume the statement for every smaller exponent, and let \( c \ne 0 \). By @fd3:prp-omega-powers-parity (d), \( k = 2j + 1 \) or \( k = 2j \) for some \( j \in \nN \).

*Case 1: \( k \) odd*, \( k = 2j + 1 \). Since \( i^2 = -1 \), the power laws (@prp-power-laws-commutative-ring (a)–(c)) give \( i^k = (i^2)^j i = (-1)^j i \in \{ i, -i \} \), \( (-1)^k = -1 \) and \( (-i)^k = (-1)^k i^k = -i^k \). So as \( \zeta \) runs through \( 1, -1, i, -i \), the products \( c\zeta^k \) run through \( c, -c \) and \( ic, -ic \) (in some order). If \( \operatorname{Re} c \ne 0 \), one of \( \operatorname{Re} c \) and \( \operatorname{Re}(-c) = -\operatorname{Re} c \) is negative. If \( \operatorname{Re} c = 0 \), then \( c = bi \) with \( b \coloneqq \operatorname{Im} c \ne 0 \), and \( ic = -b \), \( -ic = b \): one of them has negative real part.

*Case 2: \( k \) even*, \( k = 2j \) with \( 1 \le j < k \). By the induction hypothesis for \( j \), there is \( \eta \) with \( \operatorname{Re}(c\eta^j) < 0 \). Then \( \eta \ne 0 \), since otherwise \( c\eta^j = 0 \). By @prp-complex-square-roots there is \( \zeta \) with \( \zeta^2 = \eta \), and \( \zeta^k = (\zeta^2)^j = \eta^j \) (@prp-power-laws-commutative-ring (b)). So \( \operatorname{Re}(c\zeta^k) = \operatorname{Re}(c\eta^j) < 0 \). This proves the lemma.
:::
:::

With polar form one would take \( \zeta \) to be a \( k \)-th root of \( -\conj{c}/\abs{c} \). This volume's \( k \)-th roots of complex numbers (@thm-complex-nth-roots) rest on the cosine and sine of @ax-cosine-sine, which it borrows from analysis. The proof above uses only the complex square roots of @prp-complex-square-roots, which Section 1.4 builds from the real square roots of *Number Systems: From \( \nN \) to \( \nR \)* (@fd3:prp-cof-square-roots).

::: {.check}
For \( c = i \) and \( k = 1 \), which \( \zeta \in \{1, -1, i, -i\} \) gives \( \operatorname{Re}(c\zeta) < 0 \)?
:::

::: {.solution}
\( \zeta = i \): \( c\zeta = i \cdot i = -1 \), with real part \( -1 < 0 \). The others give \( i \), \( -i \) and \( -i \cdot i = 1 \), with real parts \( 0, 0, 1 \).
:::

Now the descent itself. Re-centering at \( z_0 \) is @thm-polynomial-taylor-shift of Section 5.4.

::: {#lem-complex-polynomial-descent}
[d'Alembert's Lemma]

Let \( p \in \nC[x] \) be non-constant, and let \( z_0 \in \nC \) with \( p(z_0) \ne 0 \). Then there is \( z \in \nC \) with \( \abs{p(z)} < \abs{p(z_0)} \).
:::

::: {.idea}
Expand around \( z_0 \): \( p(z_0 + h) = b_0 \bigl( 1 + (b_k/b_0) h^k + \dots \bigr) \), where \( k \) is the first index \( j \ge 1 \) with \( b_j \ne 0 \). With \( h = t\zeta \), \( t > 0 \) real and \( \zeta \) from the previous lemma, the bracket is \( 1 + t^k u + E \) with \( \operatorname{Re} u < 0 \). For small \( s > 0 \), \( \abs{1 + su} \) is about \( 1 - s\alpha \) with \( \alpha = -\operatorname{Re} u \), and \( E \) is of order \( t^{k+1} \), smaller than the gain \( t^k \alpha \). The proof fixes \( t \) first and then checks the inequality. *Before reading on: where is \( k \), the first index with \( b_k \ne 0 \), used?*
:::

::: {.proof}
Let \( n \coloneqq \deg p \ge 1 \). By @thm-polynomial-taylor-shift there are \( b_0, \dots, b_n \in \nC \) with \( p = \sum_{j=0}^{n} b_j (x - z_0)^j \), \( b_0 = p(z_0) \ne 0 \) and \( b_n \ne 0 \) (the leading coefficient of \( p \)). So the set of \( j \in \{1, \dots, n\} \) with \( b_j \ne 0 \) contains \( n \), and it has a least element \( k \) (@fd2:thm-well-ordering): \( k \ge 1 \), \( b_k \ne 0 \), and \( b_j = 0 \) for \( 1 \le j < k \).

Let \( c \coloneqq b_k/b_0 \ne 0 \). By @lem-complex-direction-negative-real-part there is \( \zeta \) with \( \operatorname{Re}(c\zeta^k) < 0 \). Put
\[
u \coloneqq c\zeta^k , \qquad \alpha \coloneqq -\operatorname{Re} u > 0 , \qquad B \coloneqq \sum_{j=k+1}^{n} \Bigl| \frac{b_j}{b_0} \Bigr| \abs{\zeta}^j \ge 0 .
\]
Then \( \alpha \le \abs{u} \) (@lem-real-part-at-most-modulus), so \( \abs{u} > 0 \). Choose
\[
t \coloneqq \min\Bigl\{ 1, \frac{\alpha}{\abs{u}^2}, \frac{\alpha}{4B} \Bigr\} \qquad (\text{the last entry omitted if } B = 0) ,
\]
a real number with \( 0 < t \le 1 \). It depends only on \( p \), \( z_0 \) and \( \zeta \). We show that \( z \coloneqq z_0 + t\zeta \) works.

*The expansion.* By @thm-polynomial-taylor-shift (c) with \( h = t\zeta \), and since \( b_j = 0 \) for \( 1 \le j < k \),
\[
p(z_0 + t\zeta) = b_0 + b_k t^k \zeta^k + \sum_{j=k+1}^{n} b_j t^j \zeta^j = b_0 \bigl( 1 + t^k u + E \bigr) ,
\]
where \( E \coloneqq \sum_{j=k+1}^{n} (b_j/b_0) t^j \zeta^j \). Since \( 0 < t \le 1 \), \( t^j \le t^{k+1} \) for \( j \ge k + 1 \), so \( \abs{E} \le t^{k+1} B \) (@cor-complex-triangle-variants (b)).

*The main term.* Let \( s \in \nR \) with \( 0 < s \le \alpha/\abs{u}^2 \). Since \( 1 + su \) has real part \( 1 - s\alpha \) and imaginary part \( s \operatorname{Im} u \),
\[
\abs{1 + su}^2 = (1 - s\alpha)^2 + s^2 (\operatorname{Im} u)^2 = 1 - 2s\alpha + s^2 \abs{u}^2 \le 1 - s\alpha ,
\]
where the last step uses \( s\abs{u}^2 \le \alpha \). Also \( (1 - s\alpha/2)^2 = 1 - s\alpha + s^2\alpha^2/4 \ge 1 - s\alpha \), and \( 1 - s\alpha/2 > 0 \) because \( s\alpha \le \alpha^2/\abs{u}^2 \le 1 \). Two non-negative reals whose squares are in the order \( \abs{1 + su}^2 \le (1 - s\alpha/2)^2 \) are in the same order (@fd3:prp-ordered-ring-rules (g)), so
\[
\abs{1 + su} \le 1 - \frac{s\alpha}{2} . \tag{3}
\]

*The choice of \( t \) at work.* Let \( s \coloneqq t^k \). Then \( 0 < s \le t \le \alpha/\abs{u}^2 \), so (3) applies; and \( tB \le \alpha/4 \). Hence, by @thm-conjugate-properties (d) and the triangle inequality,
\[
\begin{aligned}
\abs{p(z_0 + t\zeta)} &\le \abs{b_0} \bigl( \abs{1 + t^k u} + \abs{E} \bigr) \le \abs{b_0} \Bigl( 1 - \frac{t^k \alpha}{2} + t^k \cdot tB \Bigr) \\
&\le \abs{b_0} \Bigl( 1 - \frac{t^k \alpha}{4} \Bigr) < \abs{b_0} = \abs{p(z_0)} ,
\end{aligned}
\]
the last step because \( \abs{b_0} > 0 \) and \( t^k \alpha > 0 \). This proves the lemma.
:::

*Where \( k \) is used.* The index \( k \) is the first non-zero coefficient after \( b_0 \), so the expansion has no terms between \( b_0 \) and \( b_k t^k \zeta^k \). A term \( b_j t^j \zeta^j \) with \( 1 \le j < k \) would be of order \( t^j \), larger than the gain \( t^k \alpha \) for small \( t \), and in an uncontrolled direction. And the direction lemma is applied with this exponent \( k \).

::: {#exm-complex-polynomial-descent-step}
[One step of descent]

Run the proof of @lem-complex-polynomial-descent for \( p = x^3 + x^2 + 1 \) at \( z_0 = 0 \), and compare with moving along the real axis.
:::

::: {.solution}
Here the expansion around \( 0 \) is \( p \) itself: \( b_0 = 1 \), \( b_1 = 0 \), \( b_2 = 1 \), \( b_3 = 1 \). So \( k = 2 \) and \( c = b_2/b_0 = 1 \).

*The direction.* The proof of @lem-complex-direction-negative-real-part for \( k = 2 = 2 \cdot 1 \) first finds a direction for \( j = 1 \): since \( \operatorname{Re} c = 1 \ne 0 \), \( \eta = -1 \) works, with \( \operatorname{Re}(c\eta) = -1 \). Then it takes a square root of \( \eta = -1 \); the formula of @prp-complex-square-roots (with \( a = -1 \), \( b = 0 \), \( r = 1 \)) gives \( \zeta = 0 + 1 \cdot i = i \).

*The constants.* \( u = c\zeta^2 = -1 \), \( \alpha = 1 \), \( \abs{u}^2 = 1 \), \( B = \abs{b_3/b_0} \abs{\zeta}^3 = 1 \), so \( t = \min\{1, 1, 1/4\} = 1/4 \).

*The new point.* \( z = i/4 \), and
\[
p(i/4) = -\frac{i}{64} - \frac{1}{16} + 1 = \frac{15}{16} - \frac{i}{64} , \qquad \abs{p(i/4)}^2 = \frac{225}{256} + \frac{1}{4096} = \frac{3601}{4096} < 1 .
\]
The proof's bound is \( 1 - t^2 \alpha/4 = 63/64 \), and indeed \( 3601/4096 \le (63/64)^2 = 3969/4096 \).

*The real axis.* \( p(1/4) = 1/64 + 1/16 + 1 = 69/64 > 1 \). Moving from \( 0 \) to the right increases \( \abs{p} \); the direction \( \zeta = i \) chosen by the lemma decreases it. The direction matters.
:::

## The theorem, and complex polynomials

::: {#thm-fundamental-theorem-algebra}
[Fundamental Theorem of Algebra]

Every non-constant \( p \in \nC[x] \) has a root in \( \nC \).
:::

::: {.proof}
By @thm-complex-polynomial-minimum there is \( z^* \in \nC \) with \( \abs{p(z^*)} \le \abs{p(z)} \) for every \( z \in \nC \). Suppose \( p(z^*) \ne 0 \). By @lem-complex-polynomial-descent, applied at \( z_0 = z^* \), some \( z \) has \( \abs{p(z)} < \abs{p(z^*)} \), a contradiction. So \( p(z^*) = 0 \).
:::

Chapter 1 announced the theorem for expressions \( \sum_{k=0}^{n} a_k z^k \) with \( a_n \ne 0 \) and \( n \ge 1 \). Such an expression is the value at \( z \) of the non-constant polynomial \( \sum_{k=0}^{n} a_k x^k \) (@def-polynomial-evaluation), so every complex polynomial expression of positive degree has a root.

::: {#cor-complex-polynomials-linear-factors}
[Complex Polynomials Split]

::: {.enumerate options="label=(\alph*)"}
1. Every non-zero \( p \in \nC[x] \) splits over \( \nC \) (@def-splits-over-field): \( p = a(x - z_1) \cdots (x - z_n) \) with \( n = \deg p \), \( a \) the leading coefficient of \( p \), and \( z_1, \dots, z_n \in \nC \). The multiplicities of the roots of \( p \) add up to \( n \).
2. The irreducible polynomials of \( \nC[x] \) are exactly those of degree \( 1 \).
:::
:::

::: {.proof}
(a) Let \( c_1, \dots, c_k \) be the distinct roots of \( p \) in \( \nC \), with multiplicities \( m_1, \dots, m_k \). By @thm-polynomial-roots-with-multiplicity, \( p = (x - c_1)^{m_1} \cdots (x - c_k)^{m_k} g \) with \( g \in \nC[x] \) having no root in \( \nC \). Then \( g \ne 0 \), since \( p \ne 0 \), and \( g \) is constant, since a non-constant \( g \) would have a root by @thm-fundamental-theorem-algebra. A product of monic polynomials is monic (@thm-degree-of-product (b)), so comparing leading coefficients, \( g = a \); and comparing degrees, \( \deg p = m_1 + \dots + m_k \). Writing each power \( (x - c_i)^{m_i} \) as the product of \( m_i \) factors \( x - c_i \) gives the displayed form.

(b) A polynomial of degree \( 1 \) is irreducible (the examples after @def-irreducible-over-field). Conversely, let \( p \) be irreducible over \( \nC \). Then \( \deg p \ge 1 \), so \( p \) has a root \( c \) (@thm-fundamental-theorem-algebra), and \( p = (x - c)h \) by @thm-polynomial-remainder-factor (b). Since \( x - c \) is not constant, \( h \) is a non-zero constant, and \( \deg p = 1 \).
:::

::: {#exm-factor-x4-plus-one-reals}
[Factoring a quartic over the reals and over the complex numbers]

Factor \( x^4 + 1 \) into linear factors over \( \nC \), and into irreducible factors over \( \nR \).
:::

::: {.solution}
*Over \( \nC \).* Since \( i^2 = -1 \), \( x^4 + 1 = x^4 - i^2 = (x^2 - i)(x^2 + i) \). The formula of @prp-complex-square-roots gives the square roots: for \( i \) (\( a = 0 \), \( b = 1 \), \( r = 1 \)), \( w_1 \coloneqq \tfrac{\sqrt2}{2}(1 + i) \); for \( -i \) (\( b = -1 \)), \( w_2 \coloneqq \tfrac{\sqrt2}{2}(1 - i) \). Here \( \sqrt{1/2} = \sqrt2/2 \), since \( \sqrt2/2 \ge 0 \) and \( (\sqrt2/2)^2 = 1/2 \) (@fd3:prp-cof-square-roots). Since \( w_1^2 = i \) and \( w_2^2 = -i \) (@prp-complex-square-roots (a)), expanding gives \( x^2 - i = x^2 - w_1^2 = (x - w_1)(x + w_1) \) and \( x^2 + i = x^2 - w_2^2 = (x - w_2)(x + w_2) \), so
\[
x^4 + 1 = (x - w_1)(x + w_1)(x - w_2)(x + w_2) .
\]

*Over \( \nR \).* Note \( w_2 = \conj{w_1} \) and \( -w_2 = \conj{-w_1} \). Pair each root with its conjugate:
\[
(x - w_1)(x - \conj{w_1}) = x^2 - \sqrt2 \, x + 1 , \qquad (x + w_1)(x + \conj{w_1}) = x^2 + \sqrt2 \, x + 1 ,
\]
since \( w_1 + \conj{w_1} = 2\operatorname{Re} w_1 = \sqrt2 \) and \( w_1 \conj{w_1} = \abs{w_1}^2 = \tfrac12 + \tfrac12 = 1 \) (@thm-conjugate-properties (c)). So
\[
x^4 + 1 = (x^2 + \sqrt2 \, x + 1)(x^2 - \sqrt2 \, x + 1) ,
\]
which can be checked directly: the right side is \( (x^2 + 1)^2 - 2x^2 = x^4 + 1 \). Neither quadratic has a real root, since for every \( c \in \nR \), \( c^2 \pm \sqrt2 \, c + 1 = (c \pm \tfrac{\sqrt2}{2})^2 + \tfrac12 > 0 \); so both are irreducible over \( \nR \) (@prp-irreducible-low-degree (b)). No polar form was used: only the square roots of \( \pm i \).
:::

::: {.check}
Factor \( x^3 - 1 \) over \( \nR \) and over \( \nC \).
:::

::: {.solution}
\( x^3 - 1 = (x - 1)(x^2 + x + 1) \) (@lem-difference-of-powers, or expand). The quadratic has no real root, since for every \( c \in \nR \), \( c^2 + c + 1 = (c + \tfrac12)^2 + \tfrac34 > 0 \), so this is the factorization over \( \nR \) (@prp-irreducible-low-degree (b)). Over \( \nC \): a square root of \( -3 \) is \( i\sqrt3 \), and \( z_{\pm} \coloneqq (-1 \pm i\sqrt3)/2 \) satisfy \( z^2 + z + 1 = 0 \) (expand: \( z_\pm^2 = (-1 \mp i\sqrt3)/2 \), and \( z_\pm^2 + z_\pm + 1 = -1 + 1 = 0 \)). They are distinct roots, so \( (x - z_+)(x - z_-) \mid x^2 + x + 1 \) (@thm-polynomial-root-count); both are monic of degree \( 2 \), so they are equal, and \( x^3 - 1 = (x - 1)(x - z_+)(x - z_-) \).
:::

## Real polynomials

A real polynomial is also a complex one, so it splits over \( \nC \). The question is what that says over \( \nR \). The answer comes from conjugation: the non-real roots of a real polynomial come in conjugate pairs, and each pair makes a real quadratic factor.

For \( f = \sum_k f_k x^k \in \nC[x] \), write \( \bar f \coloneqq \sum_k \conj{f_k} \, x^k \), the polynomial with conjugated coefficients. A polynomial in \( \nR[x] \) is one in \( \nC[x] \) whose coefficients are real (\( \nR \subseteq \nC \), @prp-reals-embed-complex).

::: {#prp-real-polynomial-conjugate-roots}
[Conjugate Roots of Real Polynomials]

::: {.enumerate options="label=(\alph*)"}
1. The map \( \nC[x] \to \nC[x] \), \( f \mapsto \bar f \), is a ring homomorphism (@def-ring-homomorphism), and \( \conj{f(z)} = \bar f(\conj{z}) \) for every \( f \in \nC[x] \) and \( z \in \nC \).
2. Let \( f \in \nR[x] \), \( f \ne 0 \), and \( z \in \nC \). Then \( z \) is a root of \( f \) if and only if \( \conj{z} \) is, and \( \operatorname{mult}_{\conj{z}}(f) = \operatorname{mult}_z(f) \).
:::
:::

::: {.idea}
Conjugating every coefficient is a substitution homomorphism, so it respects sums, products and powers, and it commutes with evaluation once the point is conjugated too. A real polynomial is its own conjugate; so conjugating a root, or a factorization \( (x - z)^m g \), gives a root, or a factorization \( (x - \conj{z})^m \bar g \), of the same polynomial.
:::

::: {.proof}
(a) Conjugation \( \nC \to \nC \) preserves \( + \) and \( \cdot \) (@thm-conjugate-properties (a), (b)) and sends \( 1 \) to \( 1 \), so it is a ring homomorphism (see also @exm-complex-conjugation-automorphism); followed by the constants \( \nC \to \nC[x] \) (@thm-polynomial-ring-laws (b)) it is a ring homomorphism \( \varphi \colon \nC \to \nC[x] \), a composite of two. By @thm-polynomial-substitution with \( R = \nC \), \( S = \nC[x] \) and \( s = x \), the map \( f \mapsto \sum_k \varphi(f_k) x^k = \bar f \) is a ring homomorphism. For the values, \( \conj{z^k} = \conj{z}^k \) by induction with @thm-conjugate-properties (b), and then, through the sum recursion with @thm-conjugate-properties (a), (b),
\[
\conj{f(z)} = \conj{\textstyle\sum_k f_k z^k} = \textstyle\sum_k \conj{f_k} \, \conj{z}^k = \bar f(\conj{z}) .
\]
For real coefficients this is the computation of @prp-real-coefficients-conjugate-roots.

(b) The coefficients of \( f \) are real, so \( \bar f = f \) (@prp-modulus-of-real: \( \conj{a} = a \) for \( a \in \nR \)). By (a), \( f(\conj{z}) = \bar f(\conj{z}) = \conj{f(z)} \), and \( \conj{w} = 0 \) if and only if \( w = 0 \) (\( \conj{0} = 0 \) by @def-conjugate-modulus, and conversely \( w = \conj{\conj{w}} \) by @thm-conjugate-properties (a)); so \( z \) is a root exactly when \( \conj{z} \) is. Let \( m \coloneqq \operatorname{mult}_z(f) \). By @lem-polynomial-multiplicity-cofactor (a), \( f = (x - z)^m g \) with \( g(z) \ne 0 \). Apply the homomorphism of (a): \( f = \bar f = (x - \conj{z})^m \bar g \), and \( \bar g(\conj{z}) = \conj{g(z)} \ne 0 \). By @lem-polynomial-multiplicity-cofactor (a) again, \( \operatorname{mult}_{\conj{z}}(f) = m \).
:::

::: {.check}
The number \( 2 + i \) is a root of \( x^2 - 4x + 5 \in \nR[x] \). Name the other root without computing, and factor the polynomial over \( \nC \).
:::

::: {.solution}
By @prp-real-polynomial-conjugate-roots (b), \( \conj{2 + i} = 2 - i \) is a root. The two roots are distinct, so \( (x - 2 - i)(x - 2 + i) \) divides the polynomial (@thm-polynomial-root-count); both are monic of degree \( 2 \), so \( x^2 - 4x + 5 = (x - 2 - i)(x - 2 + i) \). (Check: the product is \( (x - 2)^2 + 1 \).)
:::

::: {#cor-real-irreducible-polynomials}
[The Irreducible Real Polynomials]

A polynomial \( p \in \nR[x] \) is irreducible over \( \nR \) if and only if \( \deg p = 1 \), or \( \deg p = 2 \) and \( p \) has no real root.
:::

::: {.idea}
An irreducible real polynomial has a complex root \( z \) by the theorem. A real root splits off a real linear factor. A non-real root brings its conjugate along, and the two together split off the real quadratic \( (x - z)(x - \conj{z}) \), first in \( \nC[x] \) and then, because division does not depend on the field, in \( \nR[x] \). Irreducibility leaves nothing else.
:::

::: {.proof}
\( (\Leftarrow) \) A polynomial of degree \( 1 \) is irreducible, and one of degree \( 2 \) without a root in \( \nR \) is irreducible by @prp-irreducible-low-degree (b).

\( (\Rightarrow) \) Let \( p \) be irreducible over \( \nR \). Then \( \deg p \ge 1 \), and by @thm-fundamental-theorem-algebra, \( p \), as an element of \( \nC[x] \), has a root \( z \in \nC \).

*Case 1: \( z \in \nR \).* Then \( x - z \mid p \) in \( \nR[x] \) (@thm-polynomial-remainder-factor (b), over \( \nR \)), so \( p = (x - z)h \) with \( h \in \nR[x] \); since \( x - z \) is not constant, \( h \) is constant, and \( \deg p = 1 \).

*Case 2: \( z \notin \nR \).* Then \( \conj{z} \ne z \) (@exm-complex-conjugation-automorphism), and \( \conj{z} \) is also a root (@prp-real-polynomial-conjugate-roots (b)). So the two distinct roots give \( q \coloneqq (x - z)(x - \conj{z}) \mid p \) in \( \nC[x] \) (@thm-polynomial-root-count). By @thm-conjugate-properties (c),
\[
q = x^2 - (z + \conj{z})x + z\conj{z} = x^2 - 2(\operatorname{Re} z)x + \abs{z}^2 ,
\]
which has real coefficients. Since \( \nR \) is a subfield of \( \nC \) (@exm-subfields-gaussian), @prp-polynomial-gcd-field-extension (b) gives \( q \mid p \) in \( \nR[x] \): \( p = qh \) with \( h \in \nR[x] \). Since \( q \) is not constant, \( h \) is constant, and \( \deg p = 2 \). Finally \( p \) has no real root: a root would make \( p \), of degree \( 2 \), reducible (@prp-irreducible-low-degree (a)). This proves the corollary.
:::

::: {#thm-real-polynomial-factorization}
[Factorization of Real Polynomials]

Let \( f \in \nR[x] \) be non-constant, with leading coefficient \( a \). Then \( f = a \, p_1 \cdots p_k \) for a list \( p_1, \dots, p_k \) (\( k \ge 1 \)) of monic polynomials in \( \nR[x] \), each of the form \( x - c \) with \( c \in \nR \) or a quadratic with no real root. If \( r \) entries are linear and \( s \) are quadratic, then \( r + 2s = \deg f \). The list is unique up to order, in the sense of @thm-polynomial-unique-factorization (b).
:::

::: {.proof}
By @thm-polynomial-unique-factorization (a) over \( F = \nR \), \( f = a \, p_1 \cdots p_k \) with monic irreducible \( p_i \), and the list is unique up to order by part (b). By @cor-real-irreducible-polynomials each \( p_i \) has degree \( 1 \), so it is \( x - c \) with \( c \in \nR \) (monic), or degree \( 2 \) with no real root. Degrees add over a product (@thm-degree-of-product (b), induction on \( k \)), so \( \deg f = r \cdot 1 + s \cdot 2 \).
:::

When the linear entries come first in the list, the factorization reads \( f = a(x - c_1) \cdots (x - c_r) \, q_1 \cdots q_s \), the familiar form. (Reordering a list does not change its product, by repeated use of commutativity; nothing below needs this.) For \( x^4 + 1 \), \( r = 0 \) and \( s = 2 \) (@exm-factor-x4-plus-one-reals).

::: {#cor-real-odd-degree-root}
[Real Polynomials of Odd Degree Have a Real Root]

Every \( f \in \nR[x] \) of odd degree has a root in \( \nR \).
:::

::: {.proof}
Factor \( f = a \, p_1 \cdots p_k \) as in @thm-real-polynomial-factorization, with \( r + 2s = \deg f \). If \( r = 0 \), then \( \deg f = 2s \) is even, which an odd number is not (@fd3:cor-integers-even-odd (a)). So \( r \ge 1 \): some \( p_i = x - c \) with \( c \in \nR \). By (L2) of Section 5.3, \( x - c \) divides \( p_1 \cdots p_k \), hence divides \( f = a \, p_1 \cdots p_k \) (@prp-polynomial-divisibility-rules (b)), so \( f(c) = 0 \) by @thm-polynomial-remainder-factor (b).
:::

::: {.check}
A real cubic \( f \) has exactly one real root \( c \). What are \( r \), \( s \) and \( \operatorname{mult}_c(f) \)?
:::

::: {.solution}
Every linear entry \( x - c' \) divides \( f \), so \( c' \) is a real root (@thm-polynomial-remainder-factor (b)); hence each linear entry is \( x - c \). Then \( r + 2s = 3 \) is odd, so \( r \ge 1 \) (@fd3:cor-integers-even-odd (a), as in the proof of @cor-real-odd-degree-root), and \( (r, s) = (1, 1) \) or \( (3, 0) \). Multiplicities add over the list (@prp-polynomial-multiplicity-product): a quadratic entry \( q \) has \( q(c) \ne 0 \), so \( \operatorname{mult}_c(q) = 0 \), and \( \operatorname{mult}_c(f) = r \), which is \( 1 \) or \( 3 \). Examples: \( x(x^2 + 1) \) and \( x^3 \).
:::

::: {.warning}
Beyond degree \( 2 \), "no real root" does not make a real polynomial irreducible. The polynomial \( x^4 + 1 \) has no real root, since \( c^4 + 1 = (c^2)^2 + 1 \ge 1 \) for every \( c \in \nR \), yet it is the product of two real quadratics (@exm-factor-x4-plus-one-reals). @cor-real-irreducible-polynomials says that every irreducible real polynomial has degree at most \( 2 \); so a real polynomial of degree \( 4 \) or more is always reducible, root or no root.
:::

::: {.remark}
[Looking ahead]

*Analysis on the Real Line*, Chapter 6 proves the intermediate value theorem for continuous functions on an interval. With it, the odd-degree corollary has a second proof that uses no complex numbers: a real polynomial of odd degree takes values of both signs.
:::

## Exercises

### A. Check your understanding

::: {#exr-the-fundamental-theorem-a1}
[A1]

These parts are about the proof of @thm-complex-polynomial-minimum.

::: {.enumerate options="label=(\alph*)"}
1. Where is the completeness of \( \nR \) used?
2. Why does Step 3 take "the **first** quarter in a fixed order" with the same infimum, rather than "a quarter" with the same infimum?
3. Run Steps 1–4 for \( p = x^2 + 1 \): find \( \rho \), \( S_0 \), \( m \), \( S_1 \) and \( S_2 \).
4. Give the idea of the proof in two sentences.
:::
:::

::: {.solution}
(a) Directly, twice: in Step 2, for the existence of each infimum \( m(S) \), and in Step 5, for the suprema \( \sigma^* \) and \( \tau^* \) that give the common point. Indirectly, through the real square roots behind the modulus (@def-conjugate-modulus, built on @fd3:prp-cof-square-roots), which every inequality of the proof uses.

(b) "A quarter with the same infimum" exists, but there may be several, and naming one at each of infinitely many stages without a rule is a use of the axiom of choice. "The first one in a fixed order" is a rule, a function \( q \) from squares to squares, so @fd2:thm-recursion defines the whole sequence \( (S_k) \) at once.

(c) Here \( a_0 = 1 \), \( a_1 = 0 \), \( a_2 = 1 \), so \( A = 1 \), \( R = \max\{1, 2\} = 2 \), and \( 2\abs{p(0)}/\abs{a_2} = 2 \); hence \( \rho = 2 \) and \( S_0 = S(-2, -2, 4) \). The infimum is \( m = 0 \): \( \abs{p} \ge 0 \), and \( p(-i) = 0 \) with \( -i \in S_0 \). The first quarter of \( S_0 \) is \( S(-2, -2, 2) \), which contains \( -i \) (real part \( 0 \in [-2, 0] \), imaginary part \( -1 \in [-2, 0] \)); so its infimum is \( 0 = m \), and \( S_1 = S(-2, -2, 2) \). The quarters of \( S_1 \) have side \( 1 \). The first, \( S(-2, -2, 1) \), has no point with \( \abs{p} \) small: for \( z = x + yi \) in it, \( x, y \in [-2, -1] \), so \( \abs{p(z)} \ge \abs{\operatorname{Im}(z^2 + 1)} = \abs{2xy} \ge 2 \) (@lem-real-part-at-most-modulus), and its infimum is at least \( 2 > 0 \). The second, \( S(-1, -2, 1) \), contains \( -i \), so its infimum is \( 0 \), and \( S_2 = S(-1, -2, 1) \).

(d) The infimum of \( \abs{p} \) over a big square is what we want to attain; halving keeps a quarter with the same infimum, chosen by a rule. The squares shrink to one point, and the Lipschitz bound forces the value there to be the infimum.
:::

### B. Practice

::: {#exr-the-fundamental-theorem-b1}
[B1]

Factor \( x^4 - x^2 - 2 \) into irreducible factors over \( \nQ \), over \( \nR \) and over \( \nC \). Then factor \( x^4 + 4 \) over \( \nR \) and over \( \nC \).
:::

::: {.solution}
*\( x^4 - x^2 - 2 \).* Expanding shows \( x^4 - x^2 - 2 = (x^2 - 2)(x^2 + 1) \). Over \( \nQ \): \( x^2 - 2 \) has no rational root (@fd3:thm-no-rational-square-two) and \( x^2 + 1 \) has none (\( c^2 + 1 > 0 \), @fd3:prp-ordered-ring-rules (e)), so both are irreducible (@prp-irreducible-low-degree (b)), and the factorization is \( (x^2 - 2)(x^2 + 1) \). Over \( \nR \): \( x^2 - 2 = (x - \sqrt2)(x + \sqrt2) \) (@fd3:prp-cof-square-roots), while \( x^2 + 1 \) still has no real root: \( (x - \sqrt2)(x + \sqrt2)(x^2 + 1) \). Over \( \nC \): \( x^2 + 1 = (x - i)(x + i) \), so \( (x - \sqrt2)(x + \sqrt2)(x - i)(x + i) \).

*\( x^4 + 4 \).* By the warning of Section 5.3, \( x^4 + 4 = (x^2 + 2x + 2)(x^2 - 2x + 2) \), and \( c^2 \pm 2c + 2 = (c \pm 1)^2 + 1 > 0 \) for every \( c \in \nR \); so this is the factorization over \( \nR \) (@cor-real-irreducible-polynomials). Over \( \nC \): \( -1 \pm i \) are the roots of \( x^2 + 2x + 2 \) (\( (-1 + i)^2 = -2i \), and \( -2i + 2(-1 + i) + 2 = 0 \); then its conjugate, by @prp-real-polynomial-conjugate-roots (b)), and \( 1 \pm i \) those of \( x^2 - 2x + 2 \) likewise. So \( x^4 + 4 = (x + 1 - i)(x + 1 + i)(x - 1 - i)(x - 1 + i) \), each quadratic being the product of its two distinct linear factors (@thm-polynomial-root-count, monic and of the same degree).
:::

::: {#exr-the-fundamental-theorem-b2}
[B2]

Run the proof of @lem-complex-polynomial-descent for \( p = x^3 - 2 \) at \( z_0 = 1 \): find \( b_0, \dots, b_3 \), \( k \), \( c \), \( \zeta \), \( u \), \( \alpha \), \( B \), \( t \) and the new point \( z \), and compare \( \abs{p(z)} \) with \( \abs{p(1)} \).
:::

::: {.solution}
*Expansion around \( 1 \).* Writing \( x = (x - 1) + 1 \) and expanding, \( x^3 = (x - 1)^3 + 3(x - 1)^2 + 3(x - 1) + 1 \), so
\[
x^3 - 2 = -1 + 3(x - 1) + 3(x - 1)^2 + (x - 1)^3 ,
\]
and by the uniqueness in @thm-polynomial-taylor-shift, \( (b_0, b_1, b_2, b_3) = (-1, 3, 3, 1) \). So \( k = 1 \) and \( c = b_1/b_0 = -3 \).

*Direction.* \( k = 1 \) is odd and \( \operatorname{Re} c = -3 \ne 0 \); \( \zeta = 1 \) gives \( \operatorname{Re}(c\zeta) = -3 < 0 \). So \( u = -3 \), \( \alpha = 3 \), \( \abs{u}^2 = 9 \).

*Constants.* \( B = \abs{b_2/b_0} \abs{\zeta}^2 + \abs{b_3/b_0} \abs{\zeta}^3 = 3 + 1 = 4 \), and
\[
t = \min\Bigl\{ 1, \frac{3}{9}, \frac{3}{16} \Bigr\} = \frac{3}{16} .
\]

*New point.* \( z = 1 + \tfrac{3}{16} = \tfrac{19}{16} \), and \( p(19/16) = 6859/4096 - 2 = -1333/4096 \). So \( \abs{p(z)} = 1333/4096 < 1 = \abs{p(1)} \), well inside the proof's bound \( 1 - t\alpha/4 = 55/64 \).
:::

::: {#exr-the-fundamental-theorem-b3}
[B3]

Let \( f \in \nR[x] \) have degree \( 5 \) and exactly one real root \( c \). What can the multiplicity of \( c \) be, and how many quadratic factors without real root does \( f \) have? Give an example for each possibility.
:::

::: {.solution}
Factor \( f = a \, p_1 \cdots p_k \) as in @thm-real-polynomial-factorization, with \( r \) linear and \( s \) quadratic entries, \( r + 2s = 5 \). Each linear entry \( x - c' \) divides \( f \), so \( c' \) is a real root (@thm-polynomial-remainder-factor (b)); hence every linear entry is \( x - c \). Multiplicities add over products (@prp-polynomial-multiplicity-product, with induction on \( k \)); \( \operatorname{mult}_c(x - c) = 1 \), a quadratic entry \( q \) has \( q(c) \ne 0 \) and so \( \operatorname{mult}_c(q) = 0 \), and the constant \( a \ne 0 \) has multiplicity \( 0 \). So \( \operatorname{mult}_c(f) = r \). Since \( r + 2s = 5 \) is odd, \( r \ge 1 \) (@fd3:cor-integers-even-odd (a), as in the proof of @cor-real-odd-degree-root), so the possibilities are \( (r, s) = (1, 2) \), \( (3, 1) \), \( (5, 0) \): the multiplicity of \( c \) is \( 1 \), \( 3 \) or \( 5 \), with \( 2 \), \( 1 \) or \( 0 \) quadratic factors. Examples with \( c = 0 \): \( x(x^2 + 1)^2 \), \( x^3(x^2 + 1) \), \( x^5 \). Each has only the real root \( 0 \), since \( t^2 + 1 > 0 \) for every \( t \in \nR \).
:::

### C. Going deeper

::: {#exr-the-fundamental-theorem-c1}
[C1: Exit check: the descent and the theorem]

::: {.enumerate options="label=(\alph*)"}
1. Prove @lem-complex-polynomial-descent from @lem-complex-direction-negative-real-part and @thm-polynomial-taylor-shift.
2. Deduce @thm-fundamental-theorem-algebra from (a) and @thm-complex-polynomial-minimum.
3. The field \( \nQ(i) \) of @exm-subfields-gaussian satisfies the field axioms, and \( x^2 - 2 \) has no root in it. Say which steps of the whole proof fail when \( \nR \) is replaced by \( \nQ \) and \( \nC \) by \( \nQ(i) \), and why \( x^2 - 2 \) shows that some step must fail.
:::
:::

::: {.solution}
[Hint 1]

Expand \( p \) around \( z_0 \) and divide by \( p(z_0) \). Which coefficient after the constant one decides what happens near \( z_0 \)?
:::

::: {.solution}
[Hint 2]

Let \( k \) be the least \( j \ge 1 \) with \( b_j \ne 0 \), and fix a real \( t \) with \( 0 < t \le 1 \) before estimating \( \abs{p(z_0 + t\zeta)} \).
:::

::: {.solution}
(a) Let \( n \coloneqq \deg p \ge 1 \). By @thm-polynomial-taylor-shift, \( p = \sum_{j=0}^{n} b_j (x - z_0)^j \) with \( b_0 = p(z_0) \ne 0 \) and \( b_n \ne 0 \); let \( k \) be the least \( j \ge 1 \) with \( b_j \ne 0 \) (@fd2:thm-well-ordering; \( n \) is such a \( j \)). Let \( c \coloneqq b_k/b_0 \), take \( \zeta \) with \( \operatorname{Re}(c\zeta^k) < 0 \) (@lem-complex-direction-negative-real-part), and put \( u \coloneqq c\zeta^k \), \( \alpha \coloneqq -\operatorname{Re} u > 0 \) (so \( 0 < \alpha \le \abs{u} \)), \( B \coloneqq \sum_{j=k+1}^{n} \abs{b_j/b_0} \abs{\zeta}^j \), and
\[
t \coloneqq \min\{ 1, \alpha/\abs{u}^2, \alpha/(4B) \}
\]
(the last entry omitted if \( B = 0 \)). Then \( p(z_0 + t\zeta) = b_0(1 + t^k u + E) \) with \( \abs{E} \le t^{k+1} B \), since \( b_j = 0 \) for \( 1 \le j < k \) and \( t^j \le t^{k+1} \) for \( j > k \). With \( s \coloneqq t^k \le t \le \alpha/\abs{u}^2 \),
\[
\abs{1 + su}^2 = 1 - 2s\alpha + s^2\abs{u}^2 \le 1 - s\alpha \le \bigl( 1 - s\alpha/2 \bigr)^2 ,
\]
and \( 1 - s\alpha/2 > 0 \) because \( s\alpha \le \alpha^2/\abs{u}^2 \le 1 \) (as \( \alpha \le \abs{u} \)); two non-negative reals are ordered as their squares (@fd3:prp-ordered-ring-rules (g)), so \( \abs{1 + su} \le 1 - s\alpha/2 \). Using \( tB \le \alpha/4 \),
\[
\abs{p(z_0 + t\zeta)} \le \abs{b_0}\bigl( 1 - t^k\alpha/2 + t^{k+1}B \bigr) \le \abs{b_0}\bigl( 1 - t^k\alpha/4 \bigr) < \abs{b_0} .
\]

(b) Let \( p \) be non-constant. By @thm-complex-polynomial-minimum, some \( z^* \) has \( \abs{p(z^*)} \le \abs{p(z)} \) for all \( z \). If \( p(z^*) \ne 0 \), (a) gives \( z \) with \( \abs{p(z)} < \abs{p(z^*)} \): a contradiction. So \( p(z^*) = 0 \).

(c) Completeness fails in \( \nQ \), and with it two kinds of step. *The infimum and the supremum.* Step 2 of @thm-complex-polynomial-minimum needs the infimum of a set of values, and Step 5 the supremum of the corners \( \sigma_k \); in \( \nQ \) a bounded set need not have either (@fd3:thm-rationals-gap-sqrt2: the positive rationals \( q \) with \( q^2 < 2 \) have no rational supremum). *The square roots.* The modulus \( \sqrt{a^2 + b^2} \) need not be rational (\( \abs{1 + i} = \sqrt2 \)), and the square roots of @prp-complex-square-roots, used in Case 2 of @lem-complex-direction-negative-real-part, need real square roots. The polynomial \( x^2 - 2 \) is non-constant with coefficients in \( \nQ(i) \) and no root there (the opening of this section), so the theorem is false for \( \nQ(i) \); a proof that went through unchanged would prove a falsehood, so some step must fail. In fact the failure for \( x^2 - 2 \) is exactly a missing square root: its roots in \( \nC \) are \( \pm\sqrt2 \).

**Marking scheme.** (10 points)

- 2: re-centers at \( z_0 \) with \( b_0 = p(z_0) \ne 0 \), and takes \( k \) to be the first index \( j \ge 1 \) with \( b_j \ne 0 \), with a reason that it exists.
- 1: obtains a direction \( \zeta \) with \( \operatorname{Re}(c\zeta^k) < 0 \) from @lem-complex-direction-negative-real-part.
- 2: proves that the leading term decreases by a definite amount: \( \abs{1 + su} \le 1 - \kappa s \) or \( \abs{1 + su}^2 \le 1 - \kappa s \) (or the same kind of bound for \( \abs{1 + su + E}^2 \) directly), with an explicit \( \kappa > 0 \) (for example \( \kappa = \alpha/2 \), resp. \( \alpha \)), for all \( s \) in an explicit range such as \( 0 < s \le \alpha/\abs{u}^2 \).
- 2: bounds the tail by \( t^{k+1}B \) and fixes \( t \) explicitly before the estimate that uses it.
- 2: concludes \( \abs{p(z_0 + t\zeta)} < \abs{p(z_0)} \), and derives the theorem by contradiction with the minimum.
- 1: (c) names both uses of completeness (the infimum of Step 2, with the supremum of Step 5; the real square roots behind the modulus and behind the complex square roots of the direction lemma), and says why \( x^2 - 2 \) forces a failure.

Fatal errors (0 for the step): choosing \( t \) after the inequality that needs it, or letting it depend on the point being estimated; assuming the minimum exists without citing @thm-complex-polynomial-minimum; using polar form or \( k \)-th roots of complex numbers, which this chapter does not have (a \( k \)-th root is accepted only with a proof). A proof that obtains the direction by polar form, if the reader has it from elsewhere, earns the 1 point of the direction step only together with a proof of the \( k \)-th root it uses.
:::

::: {#exr-the-fundamental-theorem-c2}
[C2: Faded: the real polynomials vanishing at a non-real number]

Let \( \alpha \in \nC \) with \( \alpha \notin \nR \), and let \( J \coloneqq \{ f \in \nR[x] : f(\alpha) = 0 \} \), evaluating in \( \nC \). You are given only: \( J \) is an ideal of \( \nR[x] \), and \( q \coloneqq x^2 - 2(\operatorname{Re} \alpha)x + \abs{\alpha}^2 \in J \). *Name the move, then complete it:* show that \( J = \langle q \rangle \) and that \( q \) is irreducible over \( \nR \).
:::

::: {.solution}
*The move* is **least degree, then divide**, as in @thm-polynomial-ideals-principal. Since \( q \ne 0 \) is in \( J \), the degrees of the non-zero elements of \( J \) form a non-empty subset of \( \nN \); let \( e \in J \) have the least degree (@fd2:thm-well-ordering), and let \( d \) be its monic associate, which is in \( J \) because \( J \) is an ideal. Divide \( q \) by \( d \): \( q = hd + r \) with \( \deg r < \deg d \) (@thm-polynomial-division-remainder). Then \( r = q - hd \in J \), and a non-zero \( r \) would have smaller degree than the least; so \( r = 0 \) and \( d \mid q \).

*The degree of \( d \).* A non-zero constant does not vanish at \( \alpha \), so \( \deg d \ge 1 \). If \( \deg d = 1 \), then \( d = x - c \) with \( c \in \nR \), and \( d(\alpha) = 0 \) gives \( \alpha = c \in \nR \), which is excluded. So \( \deg d \ge 2 \), and since \( d \mid q \) with \( \deg q = 2 \), \( \deg d = 2 \) (@prp-polynomial-divisibility-rules (d)). Then \( q = hd \) with \( \deg h = 0 \), and comparing leading coefficients of the monic \( q \) and \( d \), \( h = 1 \): \( d = q \).

*\( J = \langle q \rangle \).* Multiples of \( q \) are in \( J \). For \( f \in J \), divide: \( f = gq + r \) with \( \deg r < 2 \); \( r = f - gq \in J \), and a non-zero element of \( J \) has degree at least \( 2 \); so \( r = 0 \) and \( f \in \langle q \rangle \).

*Irreducible.* If \( q = gh \) with \( g, h \in \nR[x] \) non-constant, both have degree \( 1 \), and \( 0 = q(\alpha) = g(\alpha) h(\alpha) \) (@thm-evaluation-respects-operations), so \( g(\alpha) = 0 \) or \( h(\alpha) = 0 \) (@thm-field-basic-properties (f)): an element of \( J \) of degree \( 1 \), which was just excluded. So \( q \) is irreducible.
:::

::: {#exr-the-fundamental-theorem-c3}
[C3: Find the error]

Here is an argument.

> **Claim.** For every non-constant \( p \in \nC[x] \), \( \abs{p} \) attains a minimum on \( \nC \).
>
> **Proof.** (1) Let \( m \coloneqq \inf \{ \abs{p(z)} : z \in \nC \} \), which exists since the set is non-empty and bounded below by \( 0 \). (2) For each \( k \ge 1 \), pick \( z_k \in \nC \) with \( \abs{p(z_k)} < m + 1/k \). (3) Since \( \abs{p(z_k)} < m + 1 \le \abs{p(0)} + 1 \), @lem-complex-polynomial-growth puts the \( z_k \) in a bounded set. (4) So they converge to some \( z^* \in \nC \). (5) Then \( \abs{p(z^*)} = \lim \abs{p(z_k)} = m \).

Is the claim true? Does the argument prove it? Name the line that fails and the reason, give a counterexample to the illegal step, and say how the proof in the text avoids it.
:::

::: {.solution}
[Hint 1]

For each line, ask which result of this volume or of *Number Systems: From \( \nN \) to \( \nR \)* justifies it.
:::

::: {.solution}
[Hint 2]

Is every bounded sequence of real numbers convergent?
:::

::: {.solution}
**The claim is true:** it is @thm-complex-polynomial-minimum. **The argument does not prove it.**

*Line (4) fails.* "The \( z_k \) lie in a bounded set, so they converge" uses a general "fact" that is neither proved here nor true: entry (N9) of @fd1:exm-not-allowed-catalogue. Counterexample to the step: \( z_k \coloneqq (-1)^k \) lies in the bounded set \( \{ z : \abs{z} \le 1 \} \) and does not converge. (What is true, that a bounded sequence has a convergent **subsequence**, is not available in this volume; and the subsequence would still have to be chosen by a rule.) There is no counterexample to the conclusion.

*Two further slips.* Line (2) picks infinitely many \( z_k \) with no rule given, which is a use of the axiom of choice (compare @fd3:exm-representatives-need-choice). Line (5) moves \( \abs{p} \) past a limit, which needs continuity; @lem-complex-polynomial-lipschitz would supply it, but the line cites nothing.

*The repair* is the bisection of @thm-complex-polynomial-minimum: it chooses squares by a rule ("the first quarter with the same infimum"), finds the common point as a supremum of corners, and replaces the limit by the Lipschitz estimate of Step 6. No sequence is ever asked to converge.

**Marking scheme.** (10 points)

- 2: says the claim is true and the argument, as written, does not prove it.
- 3: names line (4) and the reason: "bounded implies convergent" is unproved and false, (N9).
- 2: a counterexample to the step, such as \( z_k = (-1)^k \).
- 1: names one further slip: the rule-less choice in line (2), or the unproved continuity in line (5).
- 2: describes the repair: squares chosen by a rule, the common point from completeness, the Lipschitz bound in place of a limit.

Fatal errors (0 for the step): a counterexample to the conclusion (there is none); "repairing" line (4) by citing Bolzano–Weierstrass as if it were proved in this volume.
:::

### R. Review

::: {#exr-the-fundamental-theorem-r1}
[R1]

Let \( F \) be a field. Show that there are no non-zero \( f, g \in F[x] \) with \( f^2 = x g^2 \).
:::

::: {.solution}
This uses the degree of a product from Chapter 4 (@thm-degree-of-product (b)), which holds over a field since a field has no zero divisors. Suppose \( f, g \ne 0 \) and \( f^2 = xg^2 \). Then \( \deg(f^2) = 2\deg f \), and \( \deg(xg^2) = 1 + 2\deg g \). So the natural number \( 2\deg f \) would equal \( 2\deg g + 1 \): even and odd at once, which @fd3:cor-integers-even-odd (a) rules out. Hence no such \( f, g \) exist.
:::

::: {#exr-the-fundamental-theorem-r2}
[R2]

In \( \nQ[x]/\langle x^2 - 2 \rangle \), show that every non-zero class \( [a + bx] \) (\( a, b \in \nQ \)) is a unit, by multiplying it by \( [a - bx] \). Compute \( [1 + x]^{-1} \).
:::

::: {.solution}
In \( \nQ[x] \), \( (a + bx)(a - bx) = a^2 - b^2x^2 = (a^2 - 2b^2) - b^2(x^2 - 2) \), so \( [a + bx][a - bx] = [a^2 - 2b^2] \). If \( (a, b) \ne (0, 0) \), the rational number \( N \coloneqq a^2 - 2b^2 \) is non-zero: if \( b = 0 \), then \( N = a^2 \ne 0 \); if \( b \ne 0 \), then \( N = 0 \) would give \( (a/b)^2 = 2 \), against @fd3:thm-no-rational-square-two. So \( [a + bx] \cdot [N^{-1}(a - bx)] = [1] \), and \( [a + bx] \) is a unit. Every class is \( [a + bx] \) for exactly one pair (@thm-polynomial-quotient-ring (b)), and the zero class is the pair \( (0, 0) \), so every non-zero class is a unit: \( \nQ[x]/\langle x^2 - 2 \rangle \) is a field, as @thm-polynomial-quotient-field also says (\( x^2 - 2 \) is irreducible over \( \nQ \)). For \( 1 + x \): \( N = 1 - 2 = -1 \), so \( [1 + x]^{-1} = [-(1 - x)] = [x - 1] \). Check: \( (1 + x)(x - 1) = x^2 - 1 = 1 + (x^2 - 2) \).

This is the computation of @exm-q-sqrt2-field in Chapter 2, "multiply by the conjugate", with \( [x] \) in place of \( \sqrt2 \): the class \( [a + bx] \) behaves as \( a + b\sqrt2 \), and \( (1 + \sqrt2)^{-1} = \sqrt2 - 1 \).
:::

::: {#exr-the-fundamental-theorem-r3}
[R3]

Let \( m, n \in \nZ_{>0} \). Prove that \( \gcd(2^m - 1, 2^n - 1) = 2^{\gcd(m, n)} - 1 \) in \( \nZ \).
:::

::: {.solution}
The method is the integer Euclidean step of *Number Systems: From \( \nN \) to \( \nR \)*, Chapter 3 (@fd3:lem-gcd-remainder-step), used on the exponents and on the numbers at once. We prove the claim for all \( m, n \ge 1 \) by strong induction on \( m + n \) (@fd1:thm-strong-induction).

If \( m = n \), both sides are \( 2^m - 1 \): the gcd of a positive integer with itself is that integer (it divides both, and every common divisor is at most it, @fd3:def-integer-gcd), and \( \gcd(m, m) = m \). If \( m > n \), then
\[
2^m - 1 = 2^{m-n}(2^n - 1) + (2^{m-n} - 1) ,
\]
and \( 2^n - 1 > 0 \), so @fd3:lem-gcd-remainder-step gives \( \gcd(2^m - 1, 2^n - 1) = \gcd(2^n - 1, 2^{m-n} - 1) \). Likewise \( m = 1 \cdot n + (m - n) \) gives \( \gcd(m, n) = \gcd(n, m - n) \). Since \( n + (m - n) = m < m + n \) and \( m - n \ge 1 \), the induction hypothesis gives \( \gcd(2^n - 1, 2^{m-n} - 1) = 2^{\gcd(n, m-n)} - 1 = 2^{\gcd(m, n)} - 1 \). If \( m < n \), exchange the roles (the gcd is symmetric). For example, \( \gcd(2^{12} - 1, 2^{18} - 1) = \gcd(4095, 262143) = 63 = 2^6 - 1 \).

This is the integer twin of Exercise C3 of Section 5.2 (@exr-polynomial-gcd-c3), where \( x^m - 1 \) and \( x^n - 1 \) play the parts of \( 2^m - 1 \) and \( 2^n - 1 \).
:::

::: {#exr-the-fundamental-theorem-r4}
[R4]

Is \( x^4 + x + 1 \) irreducible over \( \nF_2 \)?
:::

::: {.solution}
**Yes.** *The tool* is a degree count over a finite field: list the possible factorizations and check each.

The values are \( 0 + 0 + 1 = 1 \) at \( 0 \) and \( 1 + 1 + 1 = 1 \) at \( 1 \), so \( f \coloneqq x^4 + x + 1 \) has no root in \( \nF_2 \), and hence no factor of degree \( 1 \) (@thm-polynomial-remainder-factor (c)). A factorization into non-constant factors would then be \( f = gh \) with \( \deg g = \deg h = 2 \). Over \( \nF_2 \) the only non-zero constant is \( 1 \), so \( g \) and \( h \) are monic. A root of \( g \) or \( h \) would be a root of \( f \), so both are rootless quadratics, hence irreducible (@prp-irreducible-low-degree (b)). The monic quadratics over \( \nF_2 \) are \( x^2 \), \( x^2 + 1 = (x + 1)^2 \), \( x^2 + x = x(x + 1) \) and \( x^2 + x + 1 \); only the last is rootless. So \( g = h = x^2 + x + 1 \), and \( gh = x^4 + 2x^3 + 3x^2 + 2x + 1 = x^4 + x^2 + 1 \ne f \) in \( \nF_2[x] \). So \( f \) is irreducible.

*Look-alikes that fail.* "No root, hence irreducible" (@prp-irreducible-low-degree) applies only in degrees \( 2 \) and \( 3 \); in degree \( 4 \) it is the error of Exercise C2 of Section 5.3, and \( x^4 + x^2 + 1 = (x^2 + x + 1)^2 \) is a rootless reducible quartic over \( \nF_2 \). The rational root test (@thm-rational-root-test) is about \( \nQ \), not \( \nF_2 \). Eisenstein's criterion is not in this volume.
:::

<!-- dependency ledger
thm-fundamental-theorem-algebra (claim): (opening) Q(i) is a field containing i with i^2 = -1; (a + bi)^2 = 2 has no solution in Q(i) | exm-subfields-gaussian, fd3:thm-no-rational-square-two, fd3:prp-ordered-ring-rules (e), thm-field-basic-properties (f) (2ab = 0 with 2 != 0); compare real and imaginary parts (def-complex-numbers), cited; inline
lem-complex-polynomial-growth (proof): |z|^j <= |z|^(n-1) for |z| >= 1; |z|^n >= |z| | the power facts of the first fold, induction with fd3:prp-ordered-ring-rules (c); inline
lem-complex-polynomial-growth (proof): |z^j| = |z|^j | thm-conjugate-properties (d), induction on j; inline
lem-complex-polynomial-lipschitz (proof): |z|^i |w|^(j-1-i) <= M^(j-1) for |z|, |w| <= M | power facts of the first fold (0 <= a <= b gives a^j <= b^j), fd3:prp-ordered-ring-rules (c) by induction; prp-power-laws-commutative-ring (a) in R; inline
lem-complex-polynomial-lipschitz (claim): (quick check) A = 1, R = 2, L = 8 for x^2 + 1 and M = 4 | verify/ch05/lem-complex-polynomial-lipschitz.py
thm-complex-polynomial-minimum (proof): squares and their quarters as triples in R x R x R_{>0}; the recursion of fd2:thm-recursion with X the set of triples | fd2:thm-recursion read on omega (fd3:cor-omega-identification), cited
thm-complex-polynomial-minimum (proof): the least of four real numbers exists and is one of them (Step 3) | fd3:prp-ordered-ring-rules (i) (total order), three comparisons; inline
thm-complex-polynomial-minimum (proof): s_k = 2 rho / 2^k; 2^(k+1) = 2^k * 2 | fd3:def-naturals-in-ordered-field (b), induction; inline
thm-complex-polynomial-minimum (proof): (Step 4) sigma_k <= sigma_k' <= sigma_k + s_k - s_k' for k' >= k | induction on k' from the four quarters; inline
thm-complex-polynomial-minimum (proof): |Re(z - w)| <= s_k when both real parts lie in [sigma_k, sigma_k + s_k] | fd3:prp-absolute-value-ordered-field (d); inline
thm-complex-polynomial-minimum (proof): supremum property of R, directly in Steps 2 and 5 only | fd3:thm-reals-complete-ordered-field, fd3:def-complete-ordered-field, cited (chapter ledger line "analysis, isolated")
thm-complex-polynomial-minimum (claim): (Step 3 quick check) a finite list of reals has a least element attained by one entry | inline (as above)
lem-complex-direction-negative-real-part (proof): i^(2j+1) = (-1)^j i, (-1)^(2j+1) = -1, (-i)^k = -i^k | prp-power-laws-commutative-ring (a)-(c), cited; inline
lem-complex-direction-negative-real-part (proof): k in N is 2j + 1 or 2j with j in N | fd3:prp-omega-powers-parity (d), cited
lem-complex-direction-negative-real-part (claim): (remark) F4.1's k-th roots of complex numbers rest on its borrowed cosine and sine | thm-complex-nth-roots, ax-cosine-sine (borrowed from AN1.10), cited; prose comparison only, nothing rests on it
lem-complex-polynomial-descent (proof): |1 + su|^2 = 1 - 2 s alpha + s^2 |u|^2; (1 - s alpha / 2)^2 >= 1 - s alpha; t^j <= t^(k+1) for j >= k + 1 and 0 < t <= 1 | def-conjugate-modulus, def-complex-numbers; power facts of the first fold; fd3:prp-ordered-ring-rules (g) (contrapositive form for <=); inline
exm-complex-polynomial-descent-step (example): b = (1, 0, 1, 1), k = 2, zeta = i, t = 1/4, p(i/4) = 15/16 - i/64, |p|^2 = 3601/4096, bound 63/64, (63/64)^2 = 3969/4096, p(1/4) = 69/64 | verify/ch05/exm-complex-polynomial-descent-step.py
cor-complex-polynomials-linear-factors (proof): a product of monic polynomials is monic; (x - c)^m is the product of m factors x - c | thm-degree-of-product (b) with induction; the power recursion (lem-finite-sums-and-powers (c)); inline
exm-factor-x4-plus-one-reals (example): x^4 + 1 = (x^2 - i)(x^2 + i); square roots of i and -i; the two real quadratics and their product; (x +- sqrt2/2)^2 + 1/2 | prp-complex-square-roots (formula and (a)), fd3:prp-cof-square-roots, thm-conjugate-properties (c), cited; verify/ch05/exm-factor-x4-plus-one-reals.py (sqrt 2 handled symbolically as a^2 = 2)
exm-factor-x4-plus-one-reals (claim): (quick check) x^3 - 1 = (x - 1)(x^2 + x + 1); z_+-^2 + z_+- + 1 = 0 | lem-difference-of-powers, cited; verify/ch05/exm-factor-x4-plus-one-reals.py
prp-real-polynomial-conjugate-roots (proof): conj(z^k) = conj(z)^k; conj of a finite sum is the sum of the conjugates | thm-conjugate-properties (a), (b), induction with the sum recursion (fd2:def-sum-product template); inline
prp-real-polynomial-conjugate-roots (proof): the composite of two ring homomorphisms is one; conj(1) = 1 | def-ring-homomorphism (consequences paragraph), def-conjugate-modulus; inline
prp-real-polynomial-conjugate-roots (claim): (quick check) (x - 2 - i)(x - 2 + i) = (x - 2)^2 + 1 = x^2 - 4x + 5 | verify/ch05/prp-real-polynomial-conjugate-roots.py
cor-real-irreducible-polynomials (proof): R[x] inside C[x] coefficientwise; z not real implies conj(z) != z | ledger line of the chapter (Q in R in C); exm-complex-conjugation-automorphism (z-bar = z iff z in R), cited
thm-real-polynomial-factorization (proof): deg of a product of a list is the sum of the degrees, so deg f = r + 2s | thm-degree-of-product (b), induction on k; inline
cor-real-odd-degree-root (proof): x - c divides p_1...p_k, hence f = a p_1...p_k | (L2) of Section 5.3, cited by name; prp-polynomial-divisibility-rules (b)
cor-real-odd-degree-root (claim): (Looking ahead) the intermediate value theorem in AN1.6 | an1 (AN1.6 blueprint, item 5); prose pointer, nothing here depends on it
exr-the-fundamental-theorem-a1 (solution): rho = 2, S_0, S_1, S_2 for x^2 + 1; |Im(z^2 + 1)| = |2xy| >= 2 on S(-2, -2, 1) | verify/ch05/exr-the-fundamental-theorem-a1.py
exr-the-fundamental-theorem-b1 (solution): (x^2 - 2)(x^2 + 1); x^4 + 4 = (x^2 + 2x + 2)(x^2 - 2x + 2); roots -1 +- i, 1 +- i | verify/ch05/exr-the-fundamental-theorem-b1.py
exr-the-fundamental-theorem-b2 (solution): b = (-1, 3, 3, 1), t = 3/16, p(19/16) = -1333/4096, 6859/4096, bound 55/64 | verify/ch05/exr-the-fundamental-theorem-b2.py
exr-the-fundamental-theorem-b3 (solution): (r, s) in {(1, 2), (3, 1), (5, 0)}; mult_c of a product of a list is the sum | prp-polynomial-multiplicity-product with induction on the length, inline; fd3:cor-integers-even-odd (a) (r + 2s = 5 odd gives r >= 1), cited; verify/ch05/exr-the-fundamental-theorem-b3.py
cor-real-odd-degree-root (claim): (quick check) a real cubic with one real root c: (r, s) in {(1, 1), (3, 0)}, mult_c(f) = r | thm-polynomial-remainder-factor (b), fd3:cor-integers-even-odd (a) (r + 2s = 3 odd gives r >= 1), prp-polynomial-multiplicity-product (with induction on the length), cited; inline
thm-real-polynomial-factorization (claim): (after it) reordering a list does not change its product | general commutativity of finite products in a commutative ring, not proved in fd1-fd4 in this form; a parenthetical remark, nothing rests on it
exr-the-fundamental-theorem-c1 (solution): (c) the positive rationals q with q^2 < 2 have no rational supremum; |1 + i| = sqrt 2 not rational | fd3:thm-rationals-gap-sqrt2, fd3:thm-no-rational-square-two, cited; inline
exr-the-fundamental-theorem-c1 (solution): (a) 1 - s alpha / 2 > 0 since s alpha <= alpha^2/|u|^2 <= 1; |1 + su| <= 1 - s alpha / 2 from the squares | fd3:prp-ordered-ring-rules (g), cited; inline
exr-the-fundamental-theorem-c3 (solution): z_k = (-1)^k is bounded and does not converge | inline (its terms alternate between 1 and -1); the notion of convergence of a sequence is F3.9's def-sequence-limit-ordered-field (for C only in prose)
exr-the-fundamental-theorem-r1 (solution): degrees are natural numbers, inside Z | fd3:cor-integers-even-odd (a), cited
exr-the-fundamental-theorem-r2 (solution): (a + bx)(a - bx) = (a^2 - 2b^2) - b^2(x^2 - 2); [1 + x]^{-1} = [x - 1] | verify/ch05/exr-the-fundamental-theorem-r2.py
exr-the-fundamental-theorem-r3 (solution): 2^m - 1 = 2^(m-n)(2^n - 1) + (2^(m-n) - 1); gcd(4095, 262143) = 63 | verify/ch05/exr-the-fundamental-theorem-r3.py
exr-the-fundamental-theorem-r4 (solution): values of x^4 + x + 1 on F_2; the four monic quadratics; (x^2 + x + 1)^2 = x^4 + x^2 + 1 | verify/ch05/exr-the-fundamental-theorem-r4.py (all products of two quadratics over F_2)
-->
