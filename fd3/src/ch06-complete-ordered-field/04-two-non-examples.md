# Two Non-Examples

The uniqueness theorem of Section 6.3 used three hypotheses in three different ways. The Archimedean property let rationals separate elements (@lem-cof-rationals-separate). Completeness built the map as a supremum (@thm-cof-embedding-into-complete), and it supplied square roots (@prp-cof-square-roots). The order condition was either assumed of the map or, for complete fields, recovered from the square roots (@thm-cof-field-automorphism-identity). This section builds two ordered fields that are not \( \nR \), each missing something. The field \( \nR(x) \) of rational functions obeys every axiom of an ordered field and fails the Archimedean property; it has an order-preserving symmetry that moves \( x \). The field \( \nQ(\sqrt 2) \) is Archimedean and not complete; it has a symmetry that does not preserve the order. A table at the end compares the four fields.

Throughout, \( \nR \) is the complete ordered field of Chapter 5 (@thm-reals-complete-ordered-field), and we write \( q \) for \( \iota_{\nR}(q) \) when \( q \in \nQ \), as Section 5.4 did. Powers \( t^i \) of a real number \( t \) are those of @def-naturals-in-ordered-field, and finite sums \( \sum_{i=0}^{d} c_i \) of real numbers are defined by recursion, as in *Sets and Functions*, Section 2.3 (@fd2:def-sum-product), with \( \nR \) as the set of values; the empty sum is \( 0 \).

## Polynomial functions

Chapter 4 met a field of quotients of polynomials, \( \nQ(t) \) (@exm-rational-function-field), and stated without proof that it is an ordered field. Here proofs depend on such a field, so we build it from things we can check: functions on \( \nR \), compared at large arguments, with no algebra of formal polynomials.

For \( d \in \nN \) and a list \( (a_0, a_1, \dots, a_d) \) of real numbers, the function
\[
p \colon \nR \to \nR , \qquad p(t) \coloneqq \sum_{i=0}^{d} a_i t^i ,
\]
is the **polynomial function of the list**. A **polynomial function** is a function \( \nR \to \nR \) that is the polynomial function of **at least one** list. When \( a_d \ne 0 \), the list has **top degree** \( d \) and **top coefficient** \( a_d \).

The phrase "of at least one list" matters. Appending zeros to a list does not change its function: \( (1, 2) \) and \( (1, 2, 0) \) both give \( t \mapsto 1 + 2t \). So degree and top coefficient belong to a list, not to a function, until we know more.

*Examples.* The **constant** \( c \in \nR \) is the polynomial function of the list \( (c) \). The function \( t \mapsto t \) is that of \( (0, 1) \), and \( t \mapsto t^2 - 100t \) is that of \( (0, -100, 1) \), with top degree \( 2 \) and top coefficient \( 1 \). The list \( (0, 0, 0) \) gives the zero function and has no top degree.

We compare such functions at large arguments. A statement \( S(t) \) about real numbers \( t \) holds **for all large \( t \)** if there is \( T \in \nR \) such that \( S(t) \) holds **for every** \( t > T \). If \( S_1(t) \) holds for \( t > T_1 \) and \( S_2(t) \) for \( t > T_2 \), both hold for \( t > \max\{T_1, T_2\} \); so finitely many statements that each hold for all large \( t \) hold together for all large \( t \). The finiteness matters: infinitely many thresholds may have no maximum.

The basic fact is that far out, the top term wins.

::: {#lem-cof-leading-term-sign}
[The Top Term Decides the Sign]

Let \( d \in \nN \), let \( a_0, \dots, a_d \in \nR \) with \( a_d \ne 0 \), and let \( p(t) = \sum_{i=0}^{d} a_i t^i \). Put
\[
T \coloneqq 1 + \sum_{i=0}^{d-1} \frac{\abs{a_i}}{\abs{a_d}} .
\]
Then for every \( t > T \), \( p(t) \ne 0 \), and \( p(t) \) has the sign of \( a_d \): \( p(t) > 0 \) if \( a_d > 0 \), and \( p(t) < 0 \) if \( a_d < 0 \).
:::

::: {.idea}
Split off the top term: \( p(t) = a_d t^d + R(t) \) with \( R(t) = \sum_{i<d} a_i t^i \). For \( t \ge 1 \) every power \( t^i \) with \( i < d \) is at most \( t^{d-1} \), so \( \abs{R(t)} \) is at most \( (\sum_{i<d} \abs{a_i}) t^{d-1} \). That is smaller than \( \abs{a_d} t^d = \abs{a_d} t \cdot t^{d-1} \) as soon as \( \abs{a_d} t > \sum_{i<d} \abs{a_i} \), which is what \( t > T \) guarantees. The \( 1 + \) in \( T \) makes \( t \ge 1 \).
:::

::: {.proof}
*Case \( d = 0 \).* Then \( p(t) = a_0 \) for every \( t \), with \( a_0 \ne 0 \), and the claim holds for every \( t \) (here \( T = 1 \), the sum being empty).

*Case \( d \ge 1 \).* Let \( t > T \). Since \( T \ge 1 \), \( t > 1 > 0 \), so \( t^i > 0 \) and \( 1 \le t^i \le t^{d-1} \) for \( 0 \le i \le d - 1 \) (power laws in the ordered field \( \nR \), recorded in the ledger). Let \( R(t) \coloneqq \sum_{i=0}^{d-1} a_i t^i \) and \( A \coloneqq \sum_{i=0}^{d-1} \abs{a_i} \ge 0 \). By the triangle inequality @prp-absolute-value-ordered-field (e), applied term by term (induction on the number of terms), and \( \abs{a_i t^i} = \abs{a_i} t^i \) (@prp-absolute-value-ordered-field (b)),
\[
\abs{R(t)} \le \sum_{i=0}^{d-1} \abs{a_i} t^i \le A \, t^{d-1} .
\]
From \( t > T > A/\abs{a_d} \) we get \( \abs{a_d} t > A \), and multiplying by \( t^{d-1} > 0 \) (@prp-ordered-ring-rules (c)),
\[
A \, t^{d-1} < \abs{a_d} t^d = \abs{a_d t^d} .
\]
So \( \abs{R(t)} < \abs{a_d t^d} \). Now \( p(t) = a_d t^d + R(t) \), where \( t^d > 0 \). If \( a_d > 0 \), then \( a_d t^d > 0 \) and \( p(t) \ge a_d t^d - \abs{R(t)} > 0 \) (@prp-absolute-value-ordered-field (c)). If \( a_d < 0 \), then \( a_d t^d < 0 \) and \( p(t) \le a_d t^d + \abs{R(t)} = -\abs{a_d t^d} + \abs{R(t)} < 0 \). In both cases \( p(t) \ne 0 \) and has the sign of \( a_d \).
:::

So a polynomial function given by a list with a non-zero entry has, far out, a constant non-zero sign.

::: {.check}
For \( p(t) = t^2 - 100t \), compute the threshold \( T \) of @lem-cof-leading-term-sign, and check the conclusion at \( t = 102 \). Is \( T \) the smallest threshold that works?
:::

::: {.solution}
The list is \( (0, -100, 1) \), so \( T = 1 + (0 + 100)/1 = 101 \). At \( t = 102 \), \( p(102) = 102 \cdot 2 = 204 > 0 \), the sign of the top coefficient \( 1 \). The threshold is not the smallest: \( p(t) = t(t - 100) > 0 \) already for every \( t > 100 \). The lemma promises a threshold, not the best one.
:::

Three facts about these functions are all the algebra the field \( \nR(x) \) needs: sums and products of polynomial functions are polynomial functions, the top coefficient of a product is the product of the top coefficients, and a list whose function vanishes far out is all zeros.

::: {#lem-cof-polynomial-closure}
[Sums, Products and the Identity Principle]

Let \( p(t) = \sum_{i=0}^{d} a_i t^i \) and \( r(t) = \sum_{j=0}^{e} b_j t^j \), for **arbitrary** lists \( (a_0, \dots, a_d) \) and \( (b_0, \dots, b_e) \) of real numbers (zero entries, and lists of zeros, are allowed).

::: {.enumerate options="label=(\alph*)"}
1. The function \( p + r \) is the polynomial function of the list \( (a_k + b_k)_k \), where the shorter list is first extended by zeros to the length of the longer.
2. The function \( p \cdot r \) is the polynomial function of a list \( (c_0, \dots, c_{d+e}) \) whose last entry is \( c_{d+e} = a_d b_e \). If moreover \( a_d \ne 0 \) and \( b_e \ne 0 \), then \( a_d b_e \ne 0 \): the product list has top degree \( d + e \) and top coefficient \( a_d b_e \).
3. *(Identity principle.)* If \( p(t) = 0 \) for all large \( t \), then \( a_i = 0 \) for every \( i \).
:::
:::

Part (b) gives no formula for the other entries \( c_k \); nothing below uses one. A consequence used in the next subsection: if each of two lists has a non-zero entry, the product of their functions is given by a list with a non-zero entry. Indeed, cut each list after its last non-zero entry (this drops only zero terms, so the function is unchanged); then (b) gives a list for the product whose last entry is a product of two non-zero reals, which is non-zero (@prp-ordered-ring-rules (f)).

::: {.proof}
(c) Suppose some \( a_i \ne 0 \). The indices \( i \le d \) with \( a_i \ne 0 \) form a non-empty set of integers bounded above by \( d \), so it has a greatest element \( k \) (@prp-integer-least-element). Dropping the terms with \( i > k \), which are \( 0 \), gives \( p(t) = \sum_{i=0}^{k} a_i t^i \) with \( a_k \ne 0 \). By @lem-cof-leading-term-sign there is \( T \) with \( p(t) \ne 0 \) for every \( t > T \). If also \( p(t) = 0 \) for every \( t > T' \), then \( t \coloneqq \max\{T, T'\} + 1 \) gives \( p(t) \ne 0 \) and \( p(t) = 0 \), a contradiction. So every \( a_i = 0 \).
:::

::: {.second-reading title="Proof of the sum and product rules"}
::: {.idea}
Sums regroup term by term. For products, peel off the lowest coefficient of \( r \): \( r = b_0 + t \cdot r' \), where \( r' \) has a shorter list, and multiplying by \( t \) only shifts a list. Induction on the length of the list of \( r \) then keeps track of the last entry.
:::

::: {.proof}
(a) Extending a list by zeros adds only terms \( 0 \cdot t^i = 0 \), so it does not change the function. After extending, both lists have the same length \( m + 1 \), and regrouping a finite sum term by term (commutativity and associativity of \( + \), by induction on \( m \)) and distributivity give \( \sum_{k=0}^{m} a_k t^k + \sum_{k=0}^{m} b_k t^k = \sum_{k=0}^{m} (a_k + b_k) t^k \).

(b) Two special products come first. For \( c \in \nR \), \( c \cdot p \) is the polynomial function of \( (c a_0, \dots, c a_d) \), by distributivity over a finite sum (induction on the number of terms). And \( t \cdot p(t) = \sum_{i=0}^{d} a_i t^{i+1} \), since \( t \cdot t^i = t^{i+1} \) (@def-naturals-in-ordered-field (b) and commutativity); re-indexing, \( t \mapsto t \cdot p(t) \) is the polynomial function of the **shifted** list \( (0, a_0, \dots, a_d) \), of length \( d + 2 \) with the same last entry \( a_d \).

Now we prove (b) by induction on \( e \) (@fd1:ax-induction, base \( P(0) \)), for every list \( (a_0, \dots, a_d) \) at once. For \( e = 0 \), \( p \cdot r = b_0 \cdot p \), the function of \( (b_0 a_0, \dots, b_0 a_d) \), of length \( d + 1 \) and last entry \( a_d b_0 \). For the step, let \( e \ge 1 \) and let \( r' \) be the function of \( (b_1, \dots, b_e) \), a list with last index \( e - 1 \). Re-indexing as above, \( r(t) = b_0 + t \cdot r'(t) \), so
\[
p(t) \, r(t) = b_0 \, p(t) + t \cdot \bigl( p(t) \, r'(t) \bigr) .
\]
By the induction hypothesis, \( p \cdot r' \) is the function of a list with last index \( d + e - 1 \) and last entry \( a_d b_e \). Shifting gives a list for \( t \mapsto t \, p(t) r'(t) \) with last index \( d + e \) and last entry \( a_d b_e \). The list of \( b_0 \cdot p \) has last index \( d \le d + e - 1 \), so in the sum (a) its extension has \( 0 \) in position \( d + e \), and the last entry of the sum list is \( a_d b_e + 0 = a_d b_e \). This is the claim for \( e \).

Nothing here used a non-zero entry, so the statement holds for arbitrary lists. Only the last sentence of (b) uses that \( \nR \) has no zero divisors: \( a_d \ne 0 \) and \( b_e \ne 0 \) give \( a_d b_e \ne 0 \) (@prp-ordered-ring-rules (f)).
:::
:::

## The field of rational functions

A rational function should be a quotient \( p/q \) of polynomial functions. As a function on \( \nR \) it is undefined where \( q \) vanishes, so we only ever look far out, where @lem-cof-leading-term-sign keeps \( q \) away from \( 0 \), and we count two quotients as equal when they agree far out.

*A rational function is a quotient of polynomial functions, seen only at large arguments.*

::: {#def-cof-rational-functions}
[The Ordered Field of Rational Functions]

A **fraction** is a pair \( (p, q) \) of polynomial functions such that \( q \) is the polynomial function of a list with **a non-zero** entry. By @lem-cof-leading-term-sign, applied to that list cut after its last non-zero entry, there is \( T_q \in \nR \) with \( q(t) \ne 0 \) for every \( t > T_q \); the **value** of the fraction at such \( t \) is the real number \( p(t)/q(t) \).

::: {.enumerate options="label=(\alph*)"}
1. Two fractions \( (p_1, q_1) \) and \( (p_2, q_2) \) are **equivalent** if \( p_1(t)/q_1(t) = p_2(t)/q_2(t) \) **for all large** \( t \). The set \( \nR(x) \) of **rational functions** is the set of equivalence classes (@fd2:def-quotient-set); the class of \( (p, q) \) is written \( [p/q] \).
2. **Sum and product:**
\[
\begin{aligned}
[p_1/q_1] + [p_2/q_2] &\coloneqq \bigl[ (p_1 q_2 + p_2 q_1)/(q_1 q_2) \bigr] , \\
[p_1/q_1] \cdot [p_2/q_2] &\coloneqq \bigl[ (p_1 p_2)/(q_1 q_2) \bigr] .
\end{aligned}
\]
3. **Positive set:** \( P \coloneqq \{ [p/q] \in \nR(x) : p(t)/q(t) > 0 \text{ for all large } t \} \), and \( f < g \) means \( g - f \in P \).
4. \( x \coloneqq [\id_{\nR}/1] \), where \( \id_{\nR} \colon t \mapsto t \) is the polynomial function of \( (0, 1) \) and \( 1 \) is the constant.
:::
:::

In words: (a) a rational function is known only through its values far out; (b) adds and multiplies by the school rules for fractions; (c) calls it positive if its values are eventually positive; (d) names the simplest non-constant one.

**Well-definedness.** Every condition in the definition is a statement about values at all large \( t \), and a value at a single \( t \) is computed in the field \( \nR \). In particular, sums and products are **pointwise at large \( t \)**: beyond the thresholds of the two denominators, the value of the sum fraction is the sum of the two values, and the value of the product fraction is their product (@lem-field-fraction-rules (b) in \( \nR \)). That is why equivalence of fractions is an equivalence relation, why the formulas give fractions, and why sum, product and \( P \) do not depend on the representatives; the fold checks each point.

::: {.second-reading title="The well-definedness checks"}

- *Equivalence relation* (@fd2:def-equivalence-relation). Reflexive: take \( T = T_q \). Symmetric: the definition is symmetric. Transitive: if the values of \( (p_1, q_1) \), \( (p_2, q_2) \) agree for \( t > T \) and those of \( (p_2, q_2) \), \( (p_3, q_3) \) for \( t > T' \), then those of the first and third agree for \( t > \max\{T, T'\} \).
- *The formulas give fractions.* \( p_1 q_2 + p_2 q_1 \) and \( p_1 p_2 \) are polynomial functions by @lem-cof-polynomial-closure (a), (b), and \( q_1 q_2 \) is given by a list with a non-zero entry, by the consequence stated after that lemma.
- *Values of a sum and a product.* For \( t > \max\{T_{q_1}, T_{q_2}\} \), \( q_1(t) q_2(t) \ne 0 \), and by the fraction rules in \( \nR \) (@lem-field-fraction-rules (b)) the value of the sum fraction is \( p_1(t)/q_1(t) + p_2(t)/q_2(t) \), and that of the product fraction is the product of the values. Sums and products are **pointwise at large \( t \)**.
- *Independence of representatives.* If \( (p_1, q_1) \) is replaced by an equivalent fraction, its values change at no large \( t \), so by the previous point the values of the sum and product fractions change at no large \( t \): the new sum and product are equivalent to the old. The same holds for the second argument. By @thm-well-defined-on-classes (b), sum and product are well-defined functions \( \nR(x) \times \nR(x) \to \nR(x) \). In the same way, "positive for all large \( t \)" does not depend on the representative, so \( P \) is well defined (@thm-well-defined-on-classes (c)).
:::

**Examples.** The constant \( c \in \nR \) gives the class \( [c/1] \), with value \( c \) at every \( t \). The class \( x = [\id_{\nR}/1] \) has value \( t \). The fraction whose numerator is \( t \mapsto t \) and whose denominator is \( t \mapsto t^2 \) is equivalent to the fraction \( (1, \id_{\nR}) \): their values \( t/t^2 \) and \( 1/t \) agree for every \( t > 0 \). This is the usual cancellation, now a statement about values.

::: {#prp-cof-rational-functions-ordered}
[Rational Functions Form an Ordered Field]

::: {.enumerate options="label=(\alph*)"}
1. \( \nR(x) \), with the sum, product and order of @def-cof-rational-functions, is an ordered field (@def-ordered-ring-and-field), with zero \( [0/1] \), unit \( [1/1] \), and positive elements exactly the elements of \( P \).
2. The map \( \nR \to \nR(x) \), \( c \mapsto [c/1] \), is an order-preserving field map (@def-cof-order-preserving-map).
:::
:::

::: {.idea}
Every field identity holds at each large \( t \), because it holds in \( \nR \) and the operations are pointwise there; so it holds in \( \nR(x) \). The two places where something more is needed are where an existence claim is made or a sign must be decided: the inverse of a non-zero class, and trichotomy. Both rest on @lem-cof-leading-term-sign: a fraction's numerator, unless its list is all zeros, has an eventually constant sign.
:::

::: {.second-reading title="Proof that the rational functions form an ordered field"}
::: {.proof}
*Commutative ring.* Each of (F1), (F2), (F5), (F6), (F9) of @def-commutative-ring-and-field is an identity between classes built from given classes by sums and products. By the pointwise rule, its two sides have, at every large \( t \), the values of the two sides of the same identity among real numbers, which holds in \( \nR \) (@thm-reals-field). So the two sides are equivalent fractions. For (F3), (F7) and (F4): \( [0/1] \) and \( [1/1] \) have values \( 0 \) and \( 1 \), so \( f + [0/1] = f \) and \( f \cdot [1/1] = f \); and \( [(-p)/q] \), where \( -p = (-1) \cdot p \) is a polynomial function by @lem-cof-polynomial-closure (b), has value \( -p(t)/q(t) \), so it is a negative of \( [p/q] \). The table at the end of this proof writes out two of the identities.

*\( 1 \ne 0 \).* If \( [1/1] = [0/1] \), then \( 1 = 0 \) at every \( t > T \) for some \( T \), and \( t = T + 1 \) gives \( 1 = 0 \) in \( \nR \), which is false.

*Inverses (F8).* Let \( f = [p/q] \ne [0/1] \). If every entry of a list of \( p \) were \( 0 \), then \( p(t) = 0 \) for all \( t \), and \( f \) would have value \( 0 \) at all large \( t \), so \( f = [0/1] \). Hence \( p \) is the function of a list with a non-zero entry, \( (q, p) \) is a fraction, and for \( t > \max\{T_p, T_q\} \) the value of \( f \cdot [q/p] \) is \( (p(t)/q(t))(q(t)/p(t)) = 1 \). So \( [q/p] \) is an inverse of \( f \).

*Positive set.* We check (P1) and (P2) of @prp-order-from-positives. (P1): if \( f, g \in P \), with values positive for \( t > T \) and for \( t > T' \) respectively, then for \( t > \max\{T, T'\} \) the values of \( f + g \) and \( fg \) are a sum and a product of two positive reals, hence positive by @prp-ordered-ring-rules (b) and (O4) in \( \nR \). (P2): let \( f = [p/q] \). If a list of \( p \) is all zeros, then \( f = [0/1] \), and neither \( f \) nor \( -f \) is in \( P \), since their values are \( 0 \) far out. Otherwise, cut the lists of \( p \) and \( q \) after their last non-zero entries; by @lem-cof-leading-term-sign, each of \( p(t) \) and \( q(t) \) has a constant non-zero sign for all large \( t \), so \( p(t)/q(t) \) has a constant non-zero sign for all large \( t \) (@prp-reciprocal-order (a) and @prp-ordered-ring-rules (c), (d)). If that sign is positive, \( f \in P \); if negative, \( -f \in P \). In this case \( f \ne [0/1] \), since a value that is non-zero for all large \( t \) is not \( 0 \) for all large \( t \). And \( f \in P \), \( -f \in P \) cannot both hold: at \( t \) beyond both thresholds the value would be positive and negative. So exactly one of \( f \in P \), \( f = 0 \), \( -f \in P \) holds.

By @prp-order-from-positives, \( \nR(x) \) with \( f < g \Leftrightarrow g - f \in P \) is an ordered commutative ring whose positive elements are those of \( P \). With (F8) and \( 1 \ne 0 \), it is an ordered field. This proves (a).

(b) The value of \( [c/1] \) is \( c \) at every \( t \). By the pointwise rule, \( [(c + c')/1] = [c/1] + [c'/1] \) and \( [cc'/1] = [c/1][c'/1] \), and \( [1/1] \) is the unit. If \( c < c' \), then \( [c'/1] - [c/1] = [(c' - c)/1] \) has the positive value \( c' - c \) at every \( t \), so it lies in \( P \), and \( [c/1] < [c'/1] \).
:::

**Two field identities written out.**

| Identity | Value of the left side at large \( t \) | Value of the right side | Why equal in \( \nR \) |
|---|---|---|---|
| (F9) \( f(g + h) = fg + fh \) | \( u(t)\bigl(v(t) + w(t)\bigr) \) | \( u(t)v(t) + u(t)w(t) \) | (F9) in \( \nR \) |
| (F2) \( (f + g) + h = f + (g + h) \) | \( \bigl(u(t) + v(t)\bigr) + w(t) \) | \( u(t) + \bigl(v(t) + w(t)\bigr) \) | (F2) in \( \nR \) |

Here \( u(t) \), \( v(t) \), \( w(t) \) are the values of chosen representatives of \( f \), \( g \), \( h \), and "large" means beyond the maximum of the finitely many thresholds \( T_q \) involved. Each value column is computed with the pointwise rule for sums and products; the representatives produced by the formulas of @def-cof-rational-functions (b) for the two sides are different fractions, but their values agree, and that is equivalence. Exercise B1 writes out one more identity, (F5), and the closure of \( P \) under sums.
:::

From now on we write \( c \) for the class \( [c/1] \) of a real number \( c \), as (b) permits. Then for \( q \in \nQ \), \( \iota_{\nR(x)}(q) = q \): the composite \( q \mapsto [\iota_{\nR}(q)/1] \) is \( \iota_{\nR(x)} \) by @prp-cof-map-fixes-rationals, applied to the map of (b). Also, by induction on \( i \), \( x^i \) is the class of \( t \mapsto t^i \) (the product is pointwise), so the polynomial function \( p(t) = \sum a_i t^i \) has class \( \sum a_i x^i \), and \( [p/q] = p(x)/q(x) \), a quotient in the field \( \nR(x) \). The notation for rational functions is now the familiar one.

::: {.warning}
The element \( x \) of \( \nR(x) \) is **not** a real number, and the order of \( \nR(x) \) is **not** "compare values at one \( t \)". At \( t = 1 \), the value of \( x \) is \( 1 \) and that of \( x^2 \) is also \( 1 \), yet \( x < x^2 \), since \( t^2 - t > 0 \) for every \( t > 1 \). A comparison made at one argument says nothing; a comparison made at all large arguments is the order.
:::

The order is unusual in one way that matters for this chapter: \( x \) lies above every natural number.

::: {#prp-cof-rational-functions-not-archimedean}
[Rational Functions Are Not Archimedean]

In \( \nR(x) \), \( n \cdot 1 < x \) for every \( n \in \nN \). Hence \( \nR(x) \) is not Archimedean (@def-archimedean-ordered-field), and it is not complete (@def-complete-ordered-field).
:::

::: {.proof}
Let \( n \in \nN \). By @thm-rationals-embed-ordered-field, \( n \cdot 1 = \iota_{\nR(x)}(n) \), which is the class of the constant \( n \). The difference \( x - n \) has value \( t - n \), positive for every \( t > n \). So \( x - n \in P \), that is, \( n \cdot 1 < x \).

So the element \( x \) has no \( n \in \nN \) with \( x < n \cdot 1 \), which is the negation of the Archimedean property (@fd1:prp-quantifier-negation). If \( \nR(x) \) were complete, it would be Archimedean by @thm-cof-complete-archimedean. So it is not complete.
:::

The set \( \{ n \cdot 1 : n \in \nN \} \) is non-empty and bounded above by \( x \); in fact it has no supremum, and Exercise C1 asks for a direct proof of that, with no appeal to @thm-cof-complete-archimedean.

Above every natural number sits \( x \); below every \( 1/n \) sits its reciprocal.

::: {#exm-cof-infinitesimal}
[An Element Smaller Than Every \( 1/n \)]

Show that \( 0 < 1/x < 1/n \) in \( \nR(x) \) for every \( n \in \nZ_{>0} \). Deduce that the sequence \( \bigl( 1/(n + 1) \bigr)_{n \in \nN} \) does **not** converge to \( 0 \) in \( \nR(x) \) (@def-sequence-limit-ordered-field), and that "\( 0 \le a < 1/n \) for every \( n \ge 1 \)" does not force \( a = 0 \).
:::

::: {.solution}
The class \( 1/x = [1/\id_{\nR}] \) has value \( 1/t \), positive for \( t > 0 \); so \( 1/x > 0 \). The class \( 1/n - 1/x \) has value \( 1/n - 1/t \), positive for every \( t > n \) (@prp-reciprocal-order (b)); so \( 1/x < 1/n \).

Take \( \varepsilon \coloneqq 1/x \in \nR(x)_{>0} \). For every \( n \in \nN \), \( \abs{1/(n + 1) - 0} = 1/(n + 1) > 1/x = \varepsilon \), so no \( N \) has \( \abs{1/(n+1) - 0} < \varepsilon \) for \( n \ge N \); the sequence does not converge to \( 0 \). This is the sequence of @prp-reciprocals-null-iff-archimedean, which is null exactly in Archimedean fields, and \( \nR(x) \) is not one. Finally, \( a \coloneqq 1/x \) satisfies \( 0 \le a < 1/n \) for every \( n \ge 1 \), and \( a \ne 0 \).
:::

A step about sequences in an ordered field that "obviously" holds is often the Archimedean property in disguise; \( \nR(x) \) is where to test it. It also shows why the rationals cannot separate elements without Archimedes (@lem-cof-rationals-separate): the elements \( 1/x \) and \( 2/x \) are different, and the same rationals lie below each, namely the \( q \le 0 \).

::: {#exm-cof-x-not-square}
[A Positive Element That Is Not a Square]

Show that \( x > 0 \) in \( \nR(x) \), but that there is no \( f \in \nR(x) \) with \( f^2 = x \).
:::

::: {.solution}
\( x > 0 \) because its value \( t \) is positive for \( t > 0 \).

Suppose \( x = f^2 \) with \( f = [p/q] \). Comparing values, \( t = p(t)^2/q(t)^2 \) for all large \( t \), so
\[
h(t) \coloneqq t \cdot q(t)^2 - p(t)^2 = 0 \qquad \text{for all large } t .
\]
By @lem-cof-polynomial-closure (a), (b), \( h \) is the polynomial function of a list: \( q^2 \) and \( p^2 \) are products, \( t \cdot q^2 \) is a product with the function of \( (0, 1) \), \( -p^2 \) is a product with the constant \( -1 \), and \( h \) is a sum. We now find a non-zero entry of such a list, against the identity principle (c).

Cut the list of \( q \) after its last non-zero entry \( b_e \) (it has one, since \( (p, q) \) is a fraction). By (b), \( q^2 \) has a list with top degree \( 2e \) and top coefficient \( b_e^2 \), and \( t \cdot q^2 \) has a list with top degree \( 2e + 1 \) and top coefficient \( b_e^2 \ne 0 \).

*If a list of \( p \) is all zeros*, then \( p^2 = 0 \), so \( t \cdot q(t)^2 = 0 \) for all large \( t \); by (c), every entry of the list of \( t \cdot q^2 \) is \( 0 \), against \( b_e^2 \ne 0 \).

*Otherwise*, cut the list of \( p \) after its last non-zero entry \( a_d \). By (b), \( p^2 \) has a list with top degree \( 2d \) and top coefficient \( a_d^2 \), so \( -p^2 \) has one with top degree \( 2d \) and top coefficient \( -a_d^2 \). Now \( 2d \ne 2e + 1 \): an integer is not both even and odd (@cor-integers-even-odd (a)). If \( 2e + 1 > 2d \), the sum list (a) for \( h \) has entry \( b_e^2 + 0 \ne 0 \) at index \( 2e + 1 \); if \( 2d > 2e + 1 \), it has entry \( 0 - a_d^2 \ne 0 \) at index \( 2d \). Either way (c) is contradicted.

So \( x \) is not a square in \( \nR(x) \), while in \( \nR \) every positive element is one (@prp-cof-square-roots).
:::

::: {.check}
Is \( -x \) a square in \( \nR(x) \)? Is \( x^2 - 2x + 1 \)? Answer each in one line, without the argument above.
:::

::: {.solution}
\( -x \) is not: \( -x < 0 \) because \( x > 0 \), and in any ordered field every square is \( \ge 0 \) (@prp-ordered-ring-rules (e)). \( x^2 - 2x + 1 \) is: it equals \( (x - 1)^2 \) by @prp-ring-algebra (d), since \( \nR(x) \) is a commutative ring. A sign test can only rule out negative elements; for the positive element \( x \) the example needed the top degrees.
:::

## The field \( \nQ(\sqrt 2) \)

The second non-example sits inside \( \nR \). By @prp-cof-square-roots in the complete field \( \nR \), there is exactly one \( r \ge 0 \) in \( \nR \) with \( r^2 = 2 \); we write \( \sqrt 2 \coloneqq r \). (It is the element of @exm-sqrt2-class, by the uniqueness in @prp-cof-square-roots.)

::: {#def-cof-sqrt2-field}
[The Field Generated by the Square Root of Two]

\[
\nQ(\sqrt 2) \coloneqq \{ a + b\sqrt 2 : a, b \in \nQ \} \subseteq \nR ,
\]
with the sum, product and order of \( \nR \).
:::

::: {#prp-cof-sqrt2-field-archimedean}
[An Archimedean Ordered Field Inside the Reals]

::: {.enumerate options="label=(\alph*)"}
1. *(Unique representation.)* If \( a + b\sqrt 2 = a' + b'\sqrt 2 \) with \( a, b, a', b' \in \nQ \), then \( a = a' \) and \( b = b' \).
2. \( \nQ(\sqrt 2) \) is closed under sums, negatives and products, contains \( 0 \) and \( 1 \), and contains the inverse of each of its non-zero elements:
\[
(a + b\sqrt 2)^{-1} = \frac{a}{a^2 - 2b^2} - \frac{b}{a^2 - 2b^2} \sqrt 2 , \qquad a^2 - 2b^2 \ne 0 .
\]
3. With the operations and order of \( \nR \), \( \nQ(\sqrt 2) \) is an Archimedean ordered field.
:::
:::

::: {.idea}
If two representations differed in the coefficient of \( \sqrt 2 \), we could solve for \( \sqrt 2 \) as a rational, which @thm-no-rational-square-two forbids. Inverses come from the school trick of multiplying by \( a - b\sqrt 2 \). The Archimedean property is inherited from \( \nR \), because \( n \cdot 1 \) is the same element in both fields.
:::

::: {.proof}
(a) Suppose \( b \ne b' \). Then \( \sqrt 2 = (a - a')/(b' - b) \), a rational \( s \). So \( \iota_{\nR}(s^2) = \iota_{\nR}(s)^2 = 2 = \iota_{\nR}(2) \), and \( s^2 = 2 \) since \( \iota_{\nR} \) is injective (@thm-rationals-embed-ordered-field), against @thm-no-rational-square-two. Hence \( b = b' \), and then \( a = a' \).

(b) Sums and negatives are clear. For products, with \( (\sqrt 2)^2 = 2 \),
\[
(a + b\sqrt 2)(c + d\sqrt 2) = (ac + 2bd) + (ad + bc)\sqrt 2 .
\]
\( 0 = 0 + 0\sqrt 2 \) and \( 1 = 1 + 0\sqrt 2 \). Let \( a + b\sqrt 2 \ne 0 \). If \( b = 0 \), then \( a \ne 0 \) and \( a^2 - 2b^2 = a^2 \ne 0 \). If \( b \ne 0 \) and \( a^2 = 2b^2 \), then \( (a/b)^2 = 2 \), against @thm-no-rational-square-two. So \( a^2 - 2b^2 \ne 0 \) in either case, and \( (a + b\sqrt 2)(a - b\sqrt 2) = a^2 - 2b^2 \) gives the displayed inverse, which lies in \( \nQ(\sqrt 2) \).

(c) The field axioms (F1)–(F9) and the order axioms (O1)–(O4) are statements "for all elements"; they hold for all elements of \( \nR \) (@thm-reals-complete-ordered-field), hence for all elements of the subset \( \nQ(\sqrt 2) \), which by (b) is closed under the operations and contains \( 0 \), \( 1 \), negatives and inverses. So \( \nQ(\sqrt 2) \) is an ordered field, with the same \( 1 \) and the same sums as \( \nR \); in particular \( n \cdot 1 \) is the same element in both. Let \( y \in \nQ(\sqrt 2) \). Since \( \nR \) is complete, it is Archimedean (@thm-cof-complete-archimedean), so \( y < n \cdot 1 \) for some \( n \in \nN \). This inequality holds in \( \nQ(\sqrt 2) \), whose order is that of \( \nR \). So \( \nQ(\sqrt 2) \) is Archimedean.
:::

Being Archimedean is inherited by every ordered subfield of \( \nR \). Completeness is not.

::: {#prp-cof-sqrt2-field-incomplete}
[The Field Generated by the Square Root of Two Is Not Complete]

The element \( 3 \) of \( \nQ(\sqrt 2) \) is positive and has no square root in \( \nQ(\sqrt 2) \). Hence \( \nQ(\sqrt 2) \) is not complete.
:::

::: {.idea}
A square root \( a + b\sqrt 2 \) of \( 3 \) would, by unique representation, have \( 2ab = 0 \) and \( a^2 + 2b^2 = 3 \). So either \( a^2 = 3 \) or \( (2b)^2 = 6 \), with \( a \), \( 2b \) rational. Neither \( 3 \) nor \( 6 \) is a rational square, by the descent that showed \( 2 \) is not (@thm-no-rational-square-two). The descent there used \( 1 < y < 2 \) for the would-be root \( y \); for \( 3 \) we use \( 1 < y < 2 \) again, and for \( 6 \), \( 2 < y < 3 \).
:::

We isolate the descent as a claim; its proof is that of @thm-no-rational-square-two with \( 2 \) replaced by \( n \), and it sits in the fold.

::: {.claim}
Let \( n, k \in \nN \) with \( k^2 < n < (k + 1)^2 \). Then no \( y \in \nQ \) has \( y^2 = n \).
:::

::: {.second-reading title="Proof of the claim: the descent"}
::: {.proof}
Suppose \( y \in \nQ \) and \( y^2 = n \). Then \( y \ne 0 \), since \( n > k^2 \ge 0 \). Replacing \( y \) by \( -y \) if necessary, as in @thm-no-rational-square-two, we may take \( y > 0 \). By @prp-integers-embed-rationals (b), \( y = a/b \) with \( a \in \nZ \) and \( b \in \nZ_{>0} \); then \( a > 0 \) by @thm-rationals-ordered-field (a), and \( y^2 = n \) says \( a^2 = n b^2 \), as in @thm-no-rational-square-two. So the set
\[
D \coloneqq \{ v \in \nZ_{>0} : u^2 = n v^2 \text{ for some } u \in \nZ_{>0} \}
\]
contains \( b \) and is bounded below by \( 0 \). By @prp-integer-least-element it has a least element \( v \); fix \( u \in \nZ_{>0} \) with \( u^2 = n v^2 \).

*\( kv < u \).* Otherwise \( 0 \le u \le kv \), so \( u^2 \le k^2 v^2 \) (@prp-ordered-ring-rules (g), or equality), and \( k^2 v^2 < n v^2 \) since \( v^2 > 0 \) (@prp-ordered-ring-rules (c), (e)). Then \( u^2 < n v^2 \), against \( u^2 = n v^2 \).

*\( u < (k + 1) v \).* Otherwise \( 0 \le (k + 1) v \le u \), so \( (k + 1)^2 v^2 \le u^2 = n v^2 < (k + 1)^2 v^2 \), a contradiction.

*Descent.* Put \( v' \coloneqq u - kv \) and \( u' \coloneqq nv - ku \). By the two inequalities, \( 0 < v' < v \). Multiplying \( kv < u \) by \( u > 0 \) gives \( v \cdot ku < u^2 = v \cdot nv \), so \( ku < nv \) (if \( ku \ge nv \), multiplying by \( v > 0 \) would give the reverse), and \( u' > 0 \). Expanding,
\[
\begin{aligned}
u'^2 - n v'^2 &= (n^2 v^2 - 2nkuv + k^2 u^2) - (n u^2 - 2nkuv + n k^2 v^2) \\
&= (k^2 - n)(u^2 - n v^2) = 0 .
\end{aligned}
\]
So \( v' \in D \) and \( v' < v \), against the choice of \( v \). This proves the claim.
:::
:::

::: {.proof}
Since \( 1 < 3 < 4 \) and \( 4 < 6 < 9 \), the claim with \( (n, k) = (3, 1) \) and \( (6, 2) \) shows that neither \( 3 \) nor \( 6 \) is the square of a rational.

Now suppose \( c = a + b\sqrt 2 \in \nQ(\sqrt 2) \), with \( a, b \in \nQ \), has \( c^2 = 3 \). By the product formula of @prp-cof-sqrt2-field-archimedean (b),
\[
(a^2 + 2b^2) + 2ab\sqrt 2 = 3 + 0\sqrt 2 ,
\]
so by unique representation, \( 2ab = 0 \) and \( a^2 + 2b^2 = 3 \). Hence \( a = 0 \) or \( b = 0 \) (@prp-ordered-ring-rules (f), as \( 2 \ne 0 \)). If \( b = 0 \), then \( a^2 = 3 \); if \( a = 0 \), then \( 2b^2 = 3 \), so \( (2b)^2 = 6 \). Both are excluded by the claim. So \( 3 \), which is positive, has no square root in \( \nQ(\sqrt 2) \).

If \( \nQ(\sqrt 2) \) were complete, @prp-cof-square-roots would give a square root of \( 3 \) in it. So \( \nQ(\sqrt 2) \) is not complete.
:::

The proof found no explicit set without a supremum; it found a missing square root and let @prp-cof-square-roots supply the set. The set is easy to name: \( \{ y \in \nQ(\sqrt 2) : y \ge 0, \ y^2 < 3 \} \) is non-empty and bounded above by \( 2 \), and in \( \nR \) its supremum is the square root \( \sqrt 3 \) of \( 3 \) given by @prp-cof-square-roots, which is not in \( \nQ(\sqrt 2) \).

::: {.second-reading title="Why the supremum is the square root of three"}
The element \( \sqrt 3 \) bounds the set above: \( y \ge 0 \) and \( y^2 < 3 = (\sqrt 3)^2 \) give \( y < \sqrt 3 \) (@prp-ordered-ring-rules (g)). If \( s < \sqrt 3 \), then, \( \nR \) being Archimedean (@thm-cof-complete-archimedean), @thm-rationals-dense-ordered-field gives a rational \( q \) with \( \max\{s, 0\} < q < \sqrt 3 \); then \( q \ge 0 \) and \( q^2 < 3 \), so \( q \) lies in the set and \( s \) is not an upper bound. Hence \( \sqrt 3 \) is the least upper bound.
:::

::: {.check}
Why does the descent claim not show that \( 4 \) is not a rational square? Which hypothesis fails?
:::

::: {.solution}
There is no \( k \in \nN \) with \( k^2 < 4 < (k + 1)^2 \): \( k^2 < 4 \) forces \( k \le 1 \) (for \( k \ge 2 \), \( k^2 \ge 4 \)), and then \( (k + 1)^2 \le 4 \). The descent needs the root \( y = u/v \) to lie strictly between \( k \) and \( k + 1 \), so that \( 0 < v' < v \); the natural choice \( k = 2 \) (for which \( k^2 < n \) fails) gives \( v' = u - 2v = 0 \) when \( y = 2 \), and the descent stops. And indeed \( 4 = 2^2 \).
:::

The field \( \nQ(\sqrt 2) \) has a symmetry that the uniqueness theorem forbids in \( \nR \).

::: {#exm-cof-sqrt2-conjugation}
[Conjugation in \( \nQ(\sqrt 2) \)]

Define \( \sigma \colon \nQ(\sqrt 2) \to \nQ(\sqrt 2) \) by \( \sigma(a + b\sqrt 2) \coloneqq a - b\sqrt 2 \) for \( a, b \in \nQ \). Show that \( \sigma \) is a bijection that respects sums and products and has \( \sigma(1) = 1 \), that it is not the identity, and that it is not order-preserving. Then find the line of the proof of @thm-cof-field-automorphism-identity that fails for \( \sigma \).
:::

::: {.solution}
*Well defined.* By unique representation (@prp-cof-sqrt2-field-archimedean (a)), each element has exactly one pair \( (a, b) \), so the formula defines a function.

*Sums, products, \( 1 \).* \( \sigma \) respects sums, since \( (a - b\sqrt 2) + (c - d\sqrt 2) = (a + c) - (b + d)\sqrt 2 \). For products, by the product formula,
\[
\sigma\bigl( (ac + 2bd) + (ad + bc)\sqrt 2 \bigr) = (ac + 2bd) - (ad + bc)\sqrt 2 = (a - b\sqrt 2)(c - d\sqrt 2) .
\]
And \( \sigma(1) = \sigma(1 + 0\sqrt 2) = 1 \).

*Bijective.* \( \sigma(\sigma(a + b\sqrt 2)) = a + b\sqrt 2 \), so \( \sigma \) is its own two-sided inverse (@fd2:thm-bijection-iff-inverse).

*Not the identity, not order-preserving.* \( \sqrt 2 > 0 \), since it is a non-zero element with \( \sqrt 2 \ge 0 \). But \( \sigma(\sqrt 2) = -\sqrt 2 < 0 = \sigma(0) \). So \( \sigma(\sqrt 2) \ne \sqrt 2 \), and \( 0 < \sqrt 2 \) while \( \sigma(0) > \sigma(\sqrt 2) \).

*The failing line.* Step 1 of the proof of @thm-cof-field-automorphism-identity begins: "there is \( b \in F \) with \( b \ge 0 \) and \( b^2 = a \)". For \( a = \sqrt 2 \) there is no such \( b \) in \( \nQ(\sqrt 2) \). Indeed, if \( c \in \nQ(\sqrt 2) \) had \( c^2 = \sqrt 2 \), then \( \sigma(c)^2 = \sigma(c^2) = \sigma(\sqrt 2) = -\sqrt 2 < 0 \); but \( \sigma(c)^2 \ge 0 \), as every square in the ordered field \( \nR \) is (@prp-ordered-ring-rules (e)). So the step "\( \sigma(a) = \sigma(b)^2 > 0 \)" cannot start, and \( \sigma \) indeed sends the positive element \( \sqrt 2 \) to a negative one. Step 2 works in any ordered field. Step 3 as written cites completeness of \( F \), for the Archimedean property and for the target of @thm-cof-embedding-into-complete, but its conclusion still holds in \( \nQ(\sqrt 2) \): if \( \sigma \) were order-preserving, then \( \sigma \) followed by the inclusion would be an order-preserving field map \( \nQ(\sqrt 2) \to \nR \), hence the inclusion by the uniqueness clause of @thm-cof-embedding-into-complete (source \( \nQ(\sqrt 2) \), Archimedean by @prp-cof-sqrt2-field-archimedean; target \( \nR \)), and \( \sigma \) would be the identity. Only Step 1 genuinely fails.

*Two maps into \( \nR \).* Since \( \nQ(\sqrt 2) \) is Archimedean and \( \nR \) complete, @thm-cof-embedding-into-complete gives exactly one order-preserving field map \( \nQ(\sqrt 2) \to \nR \); it is the inclusion. The composite of \( \sigma \) with the inclusion is a second map \( \nQ(\sqrt 2) \to \nR \) that respects sums, products and \( 1 \). The uniqueness clause is not contradicted, because this second map is not order-preserving.
:::

## A symmetry that keeps the order

The conjugation of \( \nQ(\sqrt 2) \) escapes @thm-cof-field-automorphism-identity by breaking the order. The field \( \nR(x) \) escapes @cor-cof-order-automorphism-identity in the other way: it has a symmetry that keeps the order and still moves elements. The symmetry shifts the argument by \( 1 \).

::: {#exm-cof-shift-automorphism}
[Shifting the Argument]

For a polynomial function \( p \), write \( p^{+} \) for the function \( t \mapsto p(t + 1) \). Show that \( \sigma([p/q]) \coloneqq [p^{+}/q^{+}] \) defines an order-preserving field automorphism \( \sigma \) of \( \nR(x) \) with \( \sigma(x) = x + 1 \ne x \).
:::

::: {.second-reading title="The checks for the shift"}
::: {.solution}
*(i) \( p^{+} \) is a polynomial function.* By induction on the length of a list of \( p \) (@fd1:ax-induction). A list of length \( 1 \) gives a constant \( p \), and \( p^{+} = p \). For a list \( (a_0, \dots, a_d) \) with \( d \ge 1 \), let \( p' \) be the function of \( (a_1, \dots, a_d) \); re-indexing the sum, \( p(t) = a_0 + t \cdot p'(t) \), so
\[
p(t + 1) = a_0 + (1 + t) \cdot p'(t + 1) .
\]
By the induction hypothesis \( p'^{+} \) is a polynomial function, \( t \mapsto 1 + t \) is that of \( (1, 1) \), and @lem-cof-polynomial-closure (b), (a) make the right side a polynomial function.

*(ii) Fractions go to fractions.* If \( (p, q) \) is a fraction, then \( q(t) \ne 0 \) for every \( t > T_q \), so \( q^{+}(t) \ne 0 \) for every \( t > T_q - 1 \). If every entry of a list of \( q^{+} \) were \( 0 \), then \( q^{+} \) would vanish everywhere; so a list of \( q^{+} \) has a non-zero entry, and \( (p^{+}, q^{+}) \) is a fraction. Its value at \( t \) is the value of \( (p, q) \) at \( t + 1 \).

*(iii) Well defined, additive, multiplicative.* If \( (p_1, q_1) \) and \( (p_2, q_2) \) have equal values for every \( t > T \), the shifted fractions have equal values for every \( t > T - 1 \); so \( \sigma \) is well defined (@thm-well-defined-on-classes (a)). Since sums and products are pointwise at large \( t \), and shifting the argument commutes with pointwise operations, \( \sigma(f + g) \) and \( \sigma(f) + \sigma(g) \) have the same values at all large \( t \), and likewise for products. And \( \sigma(1) = 1 \), since a constant is unchanged by the shift.

*(iv) Order.* If \( f \in P \), with positive values for \( t > T \), then \( \sigma(f) \) has positive values for \( t > T - 1 \), so \( \sigma(f) \in P \). For \( f < g \), \( \sigma(g) - \sigma(f) = \sigma(g - f) \in P \) (additivity gives \( \sigma(-f) = -\sigma(f) \), as in Step 2 of the proof of @thm-cof-field-automorphism-identity), so \( \sigma(f) < \sigma(g) \).

*(v) Bijective.* Shifting by \( -1 \) in the same way defines \( \tau \) with \( \tau(\sigma(f)) = f = \sigma(\tau(f)) \): the values are shifted by \( 1 \) and back. By @fd2:thm-bijection-iff-inverse, \( \sigma \) is bijective.

*(vi) It moves \( x \).* \( \sigma(x) \) has value \( t + 1 \), which is the value of \( x + 1 \); so \( \sigma(x) = x + 1 \). And \( x + 1 \ne x \), since \( 1 \ne 0 \).
:::
:::

::: {.remark}
So @cor-cof-order-automorphism-identity needs its hypothesis. Its proof went through @thm-cof-embedding-into-complete, whose uniqueness clause rests on @lem-cof-rationals-separate, which needs the Archimedean property. In \( \nR(x) \) that lemma fails exactly here: every rational lies below \( x \) and below \( x + 1 \), so \( x \) and \( x + 1 \) have the same rationals below them, all of \( \nQ \), and nothing can tell them apart. An order-preserving map that fixes the rationals is free to send one to the other. No proof uses this example; only the table below cites it.
:::

## What each hypothesis buys

The table collects the four fields of this chapter. Each entry names where it is proved; no entry rests on an exercise.

| | \( \nQ \) | \( \nQ(\sqrt 2) \) | \( \nR(x) \) | \( \nR \) |
|---|---|---|---|---|
| Archimedean | yes: @thm-rationals-archimedean | yes: @prp-cof-sqrt2-field-archimedean | no: @prp-cof-rational-functions-not-archimedean | yes: @thm-reals-complete-ordered-field, @thm-cof-complete-archimedean |
| complete | no: see below | no: @prp-cof-sqrt2-field-incomplete | no: @prp-cof-rational-functions-not-archimedean | yes: @thm-reals-complete-ordered-field |
| every positive element a square | no: @thm-no-rational-square-two | no: @prp-cof-sqrt2-field-incomplete | no: @exm-cof-x-not-square | yes: @prp-cof-square-roots |
| only field automorphism the identity | yes: see below | no: @exm-cof-sqrt2-conjugation | no: @exm-cof-shift-automorphism | yes: @thm-cof-field-automorphism-identity |

Two entries need a line. \( \nQ \) is not complete: if it were, @prp-cof-square-roots would give a rational square root of \( 2 \), against @thm-no-rational-square-two. And a map \( \sigma \colon \nQ \to \nQ \) that respects sums and products and fixes \( 1 \) is the identity, with no order hypothesis: by @prp-cof-map-fixes-rationals with \( F = L = \nQ \), \( \sigma = \sigma \circ \iota_{\nQ} = \iota_{\nQ} = \id_{\nQ} \), the last equality by the uniqueness clause of @thm-rationals-embed-ordered-field, since \( \id_{\nQ} \) is such a map.

Read across, the table shows what the uniqueness theorem used. \( \nQ(\sqrt 2) \) has the Archimedean property and lacks square roots, and its symmetry breaks the order. \( \nR(x) \) lacks the Archimedean property, and its symmetry keeps the order. Of these three, only \( \nR \), which has both, has no symmetry at all. Read down, the column of \( \nQ \) shows that the last row does not characterize \( \nR \): a field can be rigid for a cheaper reason, having nothing besides rationals to move.

## Exercises

### A. Check your understanding

::: {#exr-two-non-examples-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Is \( x^2 - 100x \) positive in \( \nR(x) \)? Justify your answer.
2. Here is an argument. "\( \nQ(\sqrt 2) \) is Archimedean, so by @thm-cof-embedding-into-complete it has an order-preserving field map into the complete ordered field \( \nR \). Hence \( \nQ(\sqrt 2) \) is complete." Is the conclusion true? Which step fails?
3. Put \( 1/x \), \( 1/x^2 \) and \( 1/10^6 \) in increasing order in \( \nR(x) \).
:::
:::

::: {.solution}
(a) Yes. Its value \( t^2 - 100t = t(t - 100) \) is positive for every \( t > 100 \). (Or: the list \( (0, -100, 1) \) has top coefficient \( 1 > 0 \), and @lem-cof-leading-term-sign applies with \( T = 101 \).)

(b) The conclusion is false (@prp-cof-sqrt2-field-incomplete). The illegal step is the last: completeness of the target says nothing about suprema in the source. A set \( A \subseteq \nQ(\sqrt 2) \) that is bounded above has a supremum in \( \nR \), but it may lie outside \( \nQ(\sqrt 2) \): for \( A = \{ y \in \nQ(\sqrt 2) : y \ge 0, \ y^2 < 3 \} \) it is \( \sqrt 3 \), which is not in \( \nQ(\sqrt 2) \) (the remark after @prp-cof-sqrt2-field-incomplete).

(c) \( 0 < 1/x^2 < 1/x < 1/10^6 \). The value of \( 1/x - 1/x^2 \) is \( (t - 1)/t^2 > 0 \) for \( t > 1 \), and that of \( 1/10^6 - 1/x \) is \( 1/10^6 - 1/t > 0 \) for \( t > 10^6 \).
:::

### B. Practice

::: {#exr-two-non-examples-b1}
[B1]

Prove that multiplication in \( \nR(x) \) is associative and that the positive set \( P \) is closed under sums. In each, choose representatives, name a threshold \( T \) beyond which every denominator involved is non-zero (and, for \( P \), every value involved is positive), compute the values of both sides at \( t > T \) with the pointwise rule, and say which fact about \( \nR \) makes them equal or positive.
:::

::: {.solution}
*Associativity.* Let \( f = [p_1/q_1] \), \( g = [p_2/q_2] \), \( h = [p_3/q_3] \), and \( T \coloneqq \max\{T_{q_1}, T_{q_2}, T_{q_3}\} \). For \( t > T \), the denominators of all fractions involved are non-zero, and by the pointwise rule the value of \( (fg)h \) is \( (u(t)v(t))w(t) \) and that of \( f(gh) \) is \( u(t)(v(t)w(t)) \), where \( u, v, w \) are the values of the three fractions. These are equal by (F5) in \( \nR \). So the two fractions produced by the formula have equal values for every \( t > T \): they are equivalent, and \( (fg)h = f(gh) \).

*Closure of \( P \) under sums.* Let \( f, g \in P \): the value of \( f \) is positive for \( t > T_1 \) and that of \( g \) for \( t > T_2 \) (these thresholds may be taken \( \ge T_{q_1}, T_{q_2} \)). For \( t > \max\{T_1, T_2\} \), the value of \( f + g \) is \( u(t) + v(t) > 0 \) by (O3) in \( \nR \) (@prp-ordered-ring-rules (b)). So \( f + g \in P \). The finiteness of the list of thresholds is what lets us take a maximum.
:::

::: {#exr-two-non-examples-b2}
[B2]

Show that no rational number squares to \( 5 \) or to \( 10 \). Then show that \( 5 \) has no square root in \( \nQ(\sqrt 2) \).
:::

::: {.solution}
Since \( 2^2 = 4 < 5 < 9 = 3^2 \) and \( 3^2 = 9 < 10 < 16 = 4^2 \), the claim stated with @prp-cof-sqrt2-field-incomplete, with \( (n, k) = (5, 2) \) and \( (10, 3) \), shows that neither is a rational square. (The descent there checks \( u'^2 - n v'^2 = (k^2 - n)(u^2 - n v^2) \) for these values too; the identity holds for all \( n, k \).)

Now let \( c = a + b\sqrt 2 \) with \( a, b \in \nQ \) and \( c^2 = 5 \). By the product formula, \( (a^2 + 2b^2) + 2ab\sqrt 2 = 5 + 0\sqrt 2 \), so by unique representation (@prp-cof-sqrt2-field-archimedean (a)), \( 2ab = 0 \) and \( a^2 + 2b^2 = 5 \). If \( b = 0 \), then \( a^2 = 5 \); if \( a = 0 \), then \( 2b^2 = 5 \), so \( (2b)^2 = 10 \). Both are excluded. Hence \( 5 \) has no square root in \( \nQ(\sqrt 2) \).
:::

::: {#exr-two-non-examples-b3}
[B3]

Show that \( x^3 + 1 \) is positive in \( \nR(x) \) but is not a square there.

*Hint: the argument of @exm-cof-x-not-square, with \( t^3 + 1 \) in place of \( t \).*
:::

::: {.solution}
*Positive.* \( t \mapsto t^3 + 1 \) is the function of \( (1, 0, 0, 1) \), with top coefficient \( 1 > 0 \); by @lem-cof-leading-term-sign its value is positive for all large \( t \).

*Not a square.* Suppose \( x^3 + 1 = [p/q]^2 \). Then \( h(t) \coloneqq (t^3 + 1) q(t)^2 - p(t)^2 = 0 \) for all large \( t \), and \( h \) is the function of a list by @lem-cof-polynomial-closure (a), (b). Cut \( q \) after its last non-zero entry \( b_e \). By (b), \( (t^3 + 1) \cdot q^2 \) has a list with top degree \( 3 + 2e = 2e + 3 \), odd, and top coefficient \( 1 \cdot b_e^2 \ne 0 \). If a list of \( p \) is all zeros, then \( (t^3 + 1) q(t)^2 = 0 \) for all large \( t \), and (c) contradicts \( b_e^2 \ne 0 \). Otherwise cut \( p \) after its last non-zero entry \( a_d \); then \( -p^2 \) has a list with top degree \( 2d \), even, and top coefficient \( -a_d^2 \ne 0 \). Since \( 2d \ne 2e + 3 \) (@cor-integers-even-odd (a)), the sum list for \( h \) has the non-zero entry \( b_e^2 \) or \( -a_d^2 \) at index \( \max\{2d, 2e + 3\} \), against @lem-cof-polynomial-closure (c). So \( x^3 + 1 \) is not a square.
:::

### C. Going deeper

::: {#exr-two-non-examples-c1}
[C1: Exit check: the supremum property fails in the rational functions]

Show directly from @def-complete-ordered-field, without @thm-cof-complete-archimedean, that \( \nR(x) \) is not complete.
:::

::: {.solution}
Let \( A \coloneqq \{ n \cdot 1 : n \in \nN \} \subseteq \nR(x) \). It is non-empty (\( 0 \cdot 1 \in A \)), and it is bounded above by \( x \): the value of \( x - n \) is \( t - n > 0 \) for \( t > n \) (@prp-cof-rational-functions-not-archimedean).

Suppose \( s \in \nR(x) \) is a supremum of \( A \). For every \( n \in \nN \), \( n + 1 \in \nN \), so \( (n + 1) \cdot 1 \le s \) by (S1), that is, \( n \cdot 1 + 1 \le s \) (@def-naturals-in-ordered-field (a)), and \( n \cdot 1 \le s - 1 \). So \( s - 1 \) is an upper bound of \( A \), and (S2) gives \( s \le s - 1 \), that is, \( 1 \le 0 \), which is false in an ordered field (@prp-ordered-ring-rules (e)). So \( A \) has no supremum, and \( \nR(x) \) is not complete.

**Marking scheme.** (10 points)
- 2: exhibits a non-empty set bounded above, with the bound verified (here \( x \), by a threshold for the value of \( x - n \), or by @lem-cof-leading-term-sign).
- 3: supposes a supremum \( s \), and uses (S1) on \( (n + 1) \cdot 1 \).
- 3: plays leastness against \( s - 1 \): either shows that \( s - 1 \) is an upper bound, from \( (n + 1) \cdot 1 \le s \Rightarrow n \cdot 1 \le s - 1 \) for every \( n \), or notes \( s - 1 < s \) so that (S2) gives \( n \) with \( n \cdot 1 > s - 1 \).
- 2: reaches the contradiction (with (S2), or with (S1) via \( (n + 1) \cdot 1 > s \)), concluding that no supremum exists.
Fatal errors (0 for the step): proving only "not Archimedean" and stopping; treating \( x \) as a real number (for instance, "take \( n > x \)").
:::

::: {#exr-two-non-examples-c2}
[C2: A complete ordered field is uncountable]

Let \( F \) be a complete ordered field. Write \( 3^{n} \) for the power \( (3 \cdot 1_F)^{n} \) of @def-naturals-in-ordered-field. For \( s = (s_n)_{n \in \nN} \in \{0, 1\}^{\nN} \), let
\[
S_k(s) \coloneqq \sum_{n=0}^{k} \frac{2 s_n}{3^{n+1}} \quad (k \in \nN) , \qquad \Phi(s) \coloneqq \sup_{k \in \nN} S_k(s) .
\]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \Phi(s) \) exists.
2. Show that \( \Phi \colon \{0, 1\}^{\nN} \to F \) is injective.
3. Deduce that \( F \) is uncountable (@fd2:thm-binary-sequences-uncountable).
:::
:::

::: {.solution}
[Hint 1]

Think of ternary expansions that use only the digits \( 0 \) and \( 2 \). For (a), find a single upper bound for all \( S_k(s) \) by comparing with \( s_n = 1 \) for every \( n \).
:::

::: {.solution}
[Hint 2]

For (b), let \( j \) be the least index where \( s \) and \( s' \) differ (it exists by least elements), with \( s_j = 1 \) and \( s'_j = 0 \), and put \( c \coloneqq S_{j-1}(s) = S_{j-1}(s') \) (with \( c \coloneqq 0 \) if \( j = 0 \)).
:::

::: {.solution}
*Tail bound.* For \( k \le m \), by induction on \( m \) (@fd1:ax-induction), exactly as in @eq-ternary-tail but in \( F \):
\[
0 \le S_m(s) - S_k(s) \le \frac{1}{3^{k+1}} - \frac{1}{3^{m+1}} ,
\]
since passing from \( m \) to \( m + 1 \) adds \( 2 s_{m+1}/3^{m+2} \in [0, 2/3^{m+2}] \), and \( -1/3^{m+1} + 2/3^{m+2} = -1/3^{m+2} \). In particular \( S_k(s) \) is non-decreasing in \( k \).

(a) The set \( \{ S_k(s) : k \in \nN \} \) is non-empty, and bounded above by \( 1 \): \( S_k(s) \le S_0(s) + 1/3 - 1/3^{k+1} \le 2/3 + 1/3 = 1 \) by the tail bound with \( k = 0 \). Since \( F \) is complete, \( \Phi(s) \) exists.

(b) Let \( s \ne s' \). The set of indices where they differ is a non-empty subset of \( \nN \), so it has a least element \( j \) (@prp-integer-least-element); say \( s_j = 1 \) and \( s'_j = 0 \). Let \( c \coloneqq S_{j-1}(s) = S_{j-1}(s') \), the sums agreeing up to \( j - 1 \) (with \( c \coloneqq 0 \) if \( j = 0 \)). Then \( \Phi(s) \ge S_j(s) = c + 2/3^{j+1} \) by (S1). For \( k \ge j \), the tail bound gives \( S_k(s') \le S_j(s') + 1/3^{j+1} = c + 1/3^{j+1} \); for \( k < j \), \( S_k(s') \le S_j(s') = c \). So \( c + 1/3^{j+1} \) is an upper bound of the \( S_k(s') \), and \( \Phi(s') \le c + 1/3^{j+1} \) by (S2). Hence \( \Phi(s) - \Phi(s') \ge 1/3^{j+1} > 0 \), and \( \Phi(s) \ne \Phi(s') \).

(c) If \( F \) were countable, there would be an injection \( g \colon F \to \nN \) (@fd2:thm-countable-characterizations), and \( g \circ \Phi \) would be an injection \( \{0, 1\}^{\nN} \to \nN \) (@fd2:thm-composition-injective-surjective), making \( \{0, 1\}^{\nN} \) countable, against @fd2:thm-binary-sequences-uncountable.

*Alternatively*, by @cor-cof-isomorphic-to-cauchy-reals there is a bijection \( F \to \nR \), and \( \nR \) is uncountable by @exr-the-least-upper-bound-property-r3. The route above shows that uncountability follows from the supremum property directly, with no construction behind it.

**Marking scheme.** (10 points)
- 2: (a), a common upper bound for the partial sums, and completeness invoked for the supremum.
- 2: the tail bound, by induction, in \( F \).
- 4: (b), the first differing index \( j \) by least elements, the lower bound \( c + 2/3^{j+1} \) for \( \Phi(s) \) by (S1), and the upper bound \( c + 1/3^{j+1} \) for \( \Phi(s') \) by (S2).
- 2: (c), the composite injection and the uncountability of \( \{0, 1\}^{\nN} \). The second route, by @cor-cof-isomorphic-to-cauchy-reals and the uncountability of \( \nR \), also earns these 2 points; (a) and (b) are still marked as above.
Fatal errors (0 for the step): treating \( \Phi(s) \) as an infinite sum computed term by term; using decimal or ternary expansions of real numbers as known facts.
:::

::: {#exr-two-non-examples-c3}
[C3: Increasing and bounded]

Let \( F \) be a complete ordered field and \( (a_n)_{n \in \nN} \) a sequence in \( F \) with \( a_n \le a_{n+1} \) for every \( n \), whose set of values is bounded above. Prove that \( a_n \to s \) in \( F \) (@def-sequence-limit-ordered-field), where \( s \) is the supremum of the set of values. Here is the start of a proof. *Name the move, then complete it.*

"Let \( s \coloneqq \sup \{ a_n : n \in \nN \} \), which exists because the set is non-empty and bounded above and \( F \) is complete. Let \( \varepsilon \in F_{>0} \). …"
:::

::: {.solution}
*The move* is **construct a point as a supremum, and use its leastness through "\( s - \varepsilon \) is not an upper bound"**, which hands us a witness. It built square roots in @prp-cof-square-roots; here it builds a limit.

*Completion.* Since \( s - \varepsilon < s \) and \( s \) is the least upper bound, \( s - \varepsilon \) is not an upper bound of the values, so \( a_N > s - \varepsilon \) for some \( N \in \nN \). For \( n \ge N \), \( a_N \le a_n \), by induction on \( n - N \) from \( a_m \le a_{m+1} \); and \( a_n \le s \) by (S1). So
\[
s - \varepsilon < a_N \le a_n \le s < s + \varepsilon ,
\]
that is, \( \abs{a_n - s} < \varepsilon \) for every \( n \ge N \) (@prp-absolute-value-ordered-field (d)). Since \( \varepsilon \) was arbitrary, \( a_n \to s \). Here \( N \) depends on \( \varepsilon \).
:::

<!-- dependency ledger
lem-cof-leading-term-sign (proof): finite sums in R; the triangle inequality for a finite sum, by induction on the number of terms | finite sums as fd2:def-sum-product with R in place of the school R (fd2:thm-recursion, X = R; empty sum 0); inline induction from prp-absolute-value-ordered-field (e)
lem-cof-leading-term-sign (proof): for t >= 1 and i <= d - 1, 1 <= t^i <= t^{d-1}; t^i > 0 for t > 0 | power laws in an ordered field, as fd2:prp-power-laws with R for the school R (powers of def-naturals-in-ordered-field; t^{d-1} = t^i t^{d-1-i}; t^k >= 1 by induction)
lem-cof-leading-term-sign (solution): quick check T = 101 and p(102) = 204 | verify/ch06/lem-cof-leading-term-sign.py
lem-cof-polynomial-closure (proof): regrouping and re-indexing finite sums; distributivity over a finite sum; t * t^i = t^{i+1} | finite sums as above, inline induction; def-naturals-in-ordered-field (b)
lem-cof-polynomial-closure (proof): the indices with a_i != 0 have a greatest element | prp-integer-least-element, cited
def-cof-rational-functions (claim): finitely many "for all large t" statements hold together (max of thresholds) | inline
prp-cof-rational-functions-ordered (proof): the value of a sum/product fraction is the sum/product of values | lem-field-fraction-rules (b) in R, cited
prp-cof-rational-functions-ordered (proof): sign of p(t)/q(t) from the signs of p(t), q(t) | prp-reciprocal-order (a), prp-ordered-ring-rules (c), (d), cited
prp-cof-rational-functions-ordered (claim): x^i is the class of t -> t^i, so [p/q] = p(x)/q(x) | inline induction on i (pointwise products)
exm-cof-x-not-square (solution): 2d != 2e + 1 | cor-integers-even-odd (a), cited
prp-cof-sqrt2-field-archimedean (proof): product formula and inverse formula in Q(sqrt 2) | inline; verify/ch06/prp-cof-sqrt2-field-archimedean.py
prp-cof-sqrt2-field-archimedean (proof): a subset closed under the operations inherits (F1)-(F9), (O1)-(O4) | inline (universal statements)
prp-cof-sqrt2-field-incomplete (proof): u'^2 - n v'^2 = (k^2 - n)(u^2 - n v^2); 1 < 3 < 4, 4 < 6 < 9 | inline; verify/ch06/prp-cof-sqrt2-field-incomplete.py
prp-cof-sqrt2-field-incomplete (proof): a positive rational is a/b with a, b in Z_{>0} | prp-integers-embed-rationals (b), thm-rationals-ordered-field (a), as in thm-no-rational-square-two
prp-cof-sqrt2-field-incomplete (claim): sup in R of {y in Q(sqrt 2) : y >= 0, y^2 < 3} is sqrt 3 | inline; prp-cof-square-roots, prp-ordered-ring-rules (g), thm-cof-complete-archimedean, thm-rationals-dense-ordered-field, cited
exr-two-non-examples-a1 (solution): sup in R of {y in Q(sqrt 2) : y >= 0, y^2 < 3} is sqrt 3, not in Q(sqrt 2) | the remark after prp-cof-sqrt2-field-incomplete; inline
exm-cof-sqrt2-conjugation (solution): sigma respects products | inline; verify/ch06/prp-cof-sqrt2-field-archimedean.py (product formula)
exm-cof-shift-automorphism (solution): p(t) = a_0 + t p'(t) by re-indexing | finite sums as above
exr-two-non-examples-a1 (solution): values (t - 1)/t^2 and 1/10^6 - 1/t | verify/ch06/exr-two-non-examples-a1.py
exr-two-non-examples-b2 (solution): descent identity for (n, k) = (5, 2), (10, 3) | verify/ch06/prp-cof-sqrt2-field-incomplete.py
exr-two-non-examples-c2 (solution): tail bound and gap 1/3^{j+1}; S_k <= 1 | inline induction in F (as eq-ternary-tail); verify/ch06/exr-two-non-examples-c2.py
exr-two-non-examples-c2 (solution): {0,1}^N indexed by omega | cor-omega-identification citing rule (fd2:thm-binary-sequences-uncountable, fd2:thm-countable-characterizations)
exr-two-non-examples-c3 (solution): a_N <= a_n for n >= N | inline induction
prp-cof-rational-functions-ordered (proof): identities (F1)-(F9) hold pointwise in R; sums and products of positive reals are positive | thm-reals-field, prp-ordered-ring-rules (b), (O4) in R, cited inline
exm-cof-x-not-square (solution): top degrees 2e + 1 (t q^2) and 2e + 3 ((t^3 + 1) q^2) | lem-cof-polynomial-closure (b); verify/ch06/lem-cof-polynomial-closure.py
exm-cof-shift-automorphism (solution): p(t + 1) is a polynomial function | inline induction (fd1:ax-induction), lem-cof-polynomial-closure (b), (a); verify/ch06/lem-cof-polynomial-closure.py
exr-two-non-examples-c2 (solution): uncountability via F = R | cor-cof-isomorphic-to-cauchy-reals and exr-the-least-upper-bound-property-r3 (an exercise cited by an exercise solution only)
-->
