# Sequences That Should Converge

Chapter 4 ended with a rational sequence that is Cauchy in \( \nQ \) and converges to no rational (@thm-sqrt2-cauchy-no-rational-limit). Its terms crowd around a place where \( \nQ \) has a hole. This chapter builds the number that belongs in the hole, and the first step is to notice that many different sequences crowd around the same hole. This section sets up the raw material, the set \( \sC \) of Cauchy sequences of rationals, and the relation that will decide when two of them aim at the same number: their difference dies out. Nothing about real numbers is assumed. Every tolerance, bound and threshold in this section is a rational number.

## Two sequences aimed at one hole

The first sequence is the Newton sequence of Chapter 2 (@exm-newton-rationals-sqrt2): \( x_0 \coloneqq 2 \) and
\[
x_{n+1} \coloneqq \frac{x_n^2 + 2}{2 x_n} = \frac{x_n}{2} + \frac{1}{x_n} \qquad (n \in \nN) ,
\]
with error \( e_n \coloneqq x_n^2 - 2 \). Its first terms are \( 2, 3/2, 17/12, 577/408 \). We shall use the following facts, each proved earlier, for every \( n \in \nN \):

::: {.enumerate options="label=(NS\arabic*)"}
1. \( x_n \in \nQ_{>0} \), and \( e_n > 0 \), that is, \( x_n^2 > 2 \) (@exm-newton-rationals-sqrt2);
2. \( x_n > 1 \), and \( e_n \le 1/(4n) \) when \( n \ge 1 \) (the first clauses of the statement of @thm-sqrt2-cauchy-no-rational-limit);
3. \( (x_n) \) is a Cauchy sequence in \( \nQ \), and there is no \( L \in \nQ \) with \( x_n \to L \) (@thm-sqrt2-cauchy-no-rational-limit).
:::

From (NS1) and (NS2), \( 0 < x_n^2 - 2 \le 1/(4n) \) for every \( n \ge 1 \). At \( n = 0 \) the expression \( 1/(4n) \) is not defined, and indeed \( x_0^2 - 2 = 2 \) is not small.

The second sequence approaches the hole from below, by decimal truncation. To define it inside \( \nQ \), without the school decimals, we need powers of ten.

**Powers of ten.** For \( k \in \nN \), \( 10^k \) is the power in the ordered field \( \nQ \) of @def-naturals-in-ordered-field (b): \( 10^0 = 1 \) and \( 10^{k+1} = 10^k \cdot 10 \). (Here \( 10 = 10 \cdot 1_{\nQ} \), by the identification \( \nN \subseteq \nZ \subseteq \nQ \) of Chapter 2 and @prp-naturals-in-ordered-field (d).) Two facts about it are used below, both by induction (@fd1:ax-induction, read on \( \nN = \omega \) through @cor-omega-identification (b)) with base \( P(0) \).

- \( 10^k \in \nZ \). Base: \( 10^0 = 1 \in \nZ \). Step: if \( 10^k \in \nZ \), then \( 10^{k+1} = 10^k \cdot 10 \) is a product of two integers, and products of integers computed in \( \nQ \) are integers (@prp-integers-embed-rationals: \( j(m) j(n) = j(mn) \)).
- \( 10^k \ge k + 1 \). Base: \( 10^0 = 1 = 0 + 1 \). Step: suppose \( 10^k \ge y \), where \( y \coloneqq k + 1 \). Then \( y \ge 1 \) (@prp-naturals-in-ordered-field (b)), and multiplying by \( 10 > 0 \) gives \( 10^{k+1} = 10^k \cdot 10 \ge 10y \) (@prp-ordered-ring-rules (c)). Moreover \( 10y - (y + 1) = 9y - 1 \ge 9 - 1 > 0 \). So \( 10^{k+1} > y + 1 = k + 2 \), where \( (k + 1) + 1 = k + 2 \) is arithmetic in \( \nN \) (@thm-omega-arithmetic-laws), carried into \( \nQ \) by the sum law of @prp-naturals-in-ordered-field (a).

In particular \( 10^k \ge 1 > 0 \), and @prp-ordered-field-halves (c), applied to \( 0 < k + 1 \le 10^k \), gives
\[
0 < \frac{1}{10^k} \le \frac{1}{k + 1} \qquad (k \in \nN) .
\]{#eq-ten-power-reciprocal}
The inequality is not strict at \( k = 0 \), where both sides are \( 1 \). We write \( 1/10^k \) throughout; negative powers have not been defined.

**The truncations.** For \( k \in \nN \), let \( m_k \) be the **largest** natural number \( m \) with
\[
m^2 \le 2 \cdot (10^k)^2 ,
\]
and let \( d_k \coloneqq m_k / 10^k \). In school terms, \( d_k \) is \( \sqrt 2 \) cut off after \( k \) decimal places; but the definition mentions only integers and the rational \( 10^k \).

That such a largest \( m \) exists, and is unique, is a fact about sets of integers. Let
\[
S_k \coloneqq \{ m \in \nZ : m \ge 0 \text{ and } m^2 > 2 \cdot (10^k)^2 \} .
\]
It is bounded below by \( 0 \), and it is non-empty: \( 2 \cdot 10^k \) is a non-negative integer, and \( (2 \cdot 10^k)^2 = 4 (10^k)^2 > 2 (10^k)^2 \) because \( (10^k)^2 > 0 \). By @prp-integer-least-element, \( S_k \) has a least element \( m^\ast \). Since \( 0^2 = 0 \le 2 (10^k)^2 \), \( 0 \notin S_k \), so \( m^\ast \ge 1 \) by discreteness (@thm-integers-ordered-ring (c)), and \( m_k \coloneqq m^\ast - 1 \) is a natural number. It is not in \( S_k \), being smaller than the least element, so \( m_k^2 \le 2 (10^k)^2 \). Every natural number \( m > m_k \) satisfies \( m \ge m^\ast \) (discreteness again), so \( m^2 \ge (m^\ast)^2 > 2 (10^k)^2 \) (@prp-ordered-ring-rules (g)). So \( m_k \) is the largest natural number with \( m^2 \le 2 (10^k)^2 \), and there is exactly one. Because the description singles out one number for each \( k \), the rule \( k \mapsto d_k \) is a function \( \nN \to \nQ \) (@fd2:def-function), with no choices made.

The first values are:
\[
\begin{array}{c|ccccccc}
k & 0 & 1 & 2 & 3 & 4 & 5 & 6 \\ \hline
m_k & 1 & 14 & 141 & 1414 & 14142 & 141421 & 1414213
\end{array}
\]
For instance \( m_1 = 14 \), because \( 14^2 = 196 \le 200 = 2 \cdot 10^2 \) and \( 15^2 = 225 > 200 \). So \( d_0 = 1 \), \( d_1 = 7/5 \), \( d_2 = 141/100 \), \( d_3 = 707/500 \).

**Different sequences, one intended number.** The two sequences never meet: \( x_k^2 > 2 \ge d_k^2 \) for every \( k \), so \( x_k \ne d_k \). They approach from opposite sides, and their differences \( x_1 - d_1 = 1/10 \), \( x_2 - d_2 = 1/150 \), \( x_3 - d_3 = 11/51000 \) shrink fast. Both "should" converge to the same number, and \( \nQ \) has no such number. The plan of the chapter is to make the sequences themselves into the numbers, and for that we must first say when two sequences count as one.

## Cauchy sequences of rationals

The raw material is every sequence that behaves as if it had a limit.

::: {#def-rational-cauchy-sequences}
[Cauchy Sequences of Rationals]

\( \sC \) is the set of all sequences \( a \colon \nN \to \nQ \) (@def-sequence-ordered-field, \( F = \nQ \)) that are Cauchy sequences in \( \nQ \) (@def-cauchy-sequence-ordered-field): **for every** \( \varepsilon \in \nQ_{>0} \) **there is** \( N \in \nN \) with \( \abs{a_m - a_n} < \varepsilon \) **for all** \( m, n \ge N \). In symbols, \( a \in \sC \) means
\[
\begin{aligned}
&\forall \varepsilon \in \nQ_{>0} \ \ \exists N \in \nN \ \ \forall m \in \nN \ \ \forall n \in \nN \\
&\qquad \bigl( (m \ge N \wedge n \ge N) \Rightarrow \abs{a_m - a_n} < \varepsilon \bigr) .
\end{aligned}
\]
A sequence \( a \) of rationals is **null** if \( a_n \to 0 \) in \( \nQ \) (@def-null-sequence-ordered-field, \( F = \nQ \)).
:::

We write a sequence as a single letter, \( a = (a_n)_{n \in \nN} \), and do arithmetic on sequences **termwise**: \( a + b \coloneqq (a_n + b_n)_n \), \( ab \coloneqq (a_n b_n)_n \), \( -a \coloneqq (-a_n)_n \) and \( a - b \coloneqq (a_n - b_n)_n \). For \( q \in \nQ \), \( (q)_n \) is the constant sequence with every term \( q \).

Nothing is new here except the name: this is Chapter 4's definition with \( F = \nQ \), so every tolerance \( \varepsilon \) is **rational**. That is the point. The definition can be read by someone who knows only \( \nQ \), and it will be used to build a larger field without assuming anything about it.

**Examples.** Every constant sequence \( (q)_n \) is in \( \sC \), with \( N = 0 \) for every \( \varepsilon \). The sequence \( (1/(n + 1))_n \) is null (@exm-first-sequences-ordered-field (b)), so it is in \( \sC \) (@thm-cauchy-algebra-ordered-field (a)). The Newton sequence \( (x_n) \) is in \( \sC \), by (NS3), and is not null, since \( x_n > 1 \) for every \( n \). The sequence \( (n)_n \) is not in \( \sC \): a Cauchy sequence is bounded (@prp-cauchy-bounded-ordered-field), and for every \( M \in \nQ_{>0} \) some \( n \in \nN \) has \( n > M \) (@thm-rationals-archimedean).

**The toolkit from Chapter 4, with \( F = \nQ \).** This chapter uses the following facts so often that we list them once. Each was proved in Chapter 4 for an arbitrary ordered field; here \( F = \nQ \).

- Constant sequences and null sequences are in \( \sC \), and \( \sC \) is closed under \( + \), \( - \), \( \cdot \) and negatives (@thm-cauchy-algebra-ordered-field).
- Sums, negatives and constant multiples of null sequences are null (@thm-limit-laws-ordered-field (a), (b)).
- A null sequence times a bounded sequence is null (@prp-null-times-bounded-ordered-field).
- Every member of \( \sC \) is bounded (@prp-cauchy-bounded-ordered-field).
- Changing finitely many terms changes no limit, and so no nullity (@prp-tail-change-ordered-field (a)).
- A sequence squeezed, from some index on, between two sequences with the same limit has that limit too (@prp-limit-preserves-order-ordered-field (c)); in particular one squeezed between \( (0)_n \), or \( (-u_n)_n \), and a null \( (u_n)_n \) is null.

## When two sequences name the same number

The Newton sequence and the truncations should name one number, yet they share no term. "Eventually equal" is therefore too strict a test. What the two sequences do share is visible in the differences above: \( x_k - d_k \) shrinks to nothing. In \( \nQ \) we cannot compare the two sequences through a common limit, since there is none; but their difference is again a sequence of rationals, and whether it tends to \( 0 \) is a question \( \nQ \) can answer.

*Two Cauchy sequences are equivalent when their difference dies out.*

::: {#def-cauchy-equivalent}
[Equivalent Cauchy Sequences]

For \( a, b \in \sC \), we write \( a \sim b \), and say that \( a \) is **equivalent** to \( b \), if the sequence \( a - b = (a_n - b_n)_n \) is null. In symbols, \( a \sim b \) means
\[
\forall \varepsilon \in \nQ_{>0} \ \ \exists N \in \nN \ \ \forall n \in \nN \ \ \bigl( n \ge N \Rightarrow \abs{a_n - b_n} < \varepsilon \bigr) .
\]
:::

In words: whatever rational tolerance is named, **from some index on**, the two sequences agree to within it **at the same index**. The threshold \( N \) comes after \( \varepsilon \), so it may depend on \( \varepsilon \). The comparison is always between \( a_n \) and \( b_n \) with the same \( n \); nothing is said about \( a_m \) against \( b_n \). The relation is defined only on \( \sC \): both sequences must be Cauchy before we ask whether they are equivalent.

**Examples.**

- *Constant sequences (the degenerate case).* For \( p, q \in \nQ \), \( (p)_n \sim (q)_n \) if and only if \( p = q \). The difference is the constant \( (p - q)_n \), which converges to \( p - q \) (@exm-first-sequences-ordered-field (a)); by uniqueness of limits (@thm-limit-unique-ordered-field) it is null exactly when \( p - q = 0 \). So on constant sequences \( \sim \) is plain equality, as it must be if \( (q)_n \) is to stand for \( q \).
- *A null sequence and zero.* \( (1/(n + 1))_n \sim (0)_n \): the difference is \( (1/(n + 1))_n \), null by @exm-first-sequences-ordered-field (b). No term of the first sequence is \( 0 \).
- *The truncations and the Newton sequence.* \( (d_k) \sim (x_k) \); this is @exm-truncations-equivalent below.

**Non-example by a minimal change.** Shift the null sequence of the second example up by one: \( b_n \coloneqq 1 + 1/(n + 1) \). It is still in \( \sC \), and \( b - (1)_n \) is still null, so \( b \sim (1)_n \). But \( b \not\sim (0)_n \): the clause that fails is "for every \( \varepsilon \)". With \( \varepsilon = 1 \), every \( n \) has \( \abs{b_n - 0} = 1 + 1/(n + 1) \ge 1 \), so no threshold exists.

**Why this definition.**

- *Why "null", and not "same limit".* Two sequences with a common limit in \( \nQ \) have null difference (@thm-limit-laws-ordered-field (b)), so for convergent sequences the new relation says "same limit". But it is stated without mentioning any limit, so it applies equally to \( (x_k) \) and \( (d_k) \), which have none in \( \nQ \).
- *Why not "eventually equal".* Then \( (x_k) \) and \( (d_k) \) would name different numbers, and so would \( (1/(n + 1))_n \) and \( (0)_n \). Sequences that agree ever more closely, without ever agreeing exactly, would never be identified.
- *Why only on \( \sC \).* On all sequences of rationals the same relation would not respect products, and Section 5.2 needs it to. For instance \( (1/(n + 1))_n \) and \( (0)_n \) have null difference, but multiplying both termwise by \( (n + 1)_n \), which is not Cauchy, gives \( (1)_n \) and \( (0)_n \), whose difference is not null. Inside \( \sC \) every multiplier is bounded, and that is what saves the product.

It must be checked that \( \sim \) really sorts sequences into groups, that is, that it is an equivalence relation in the sense of *Sets, Relations, and Cardinality*, Section 2.5.

::: {#prp-cauchy-equivalent-relation}
[Equivalence of Cauchy Sequences Is an Equivalence Relation]

The relation \( \sim \) of @def-cauchy-equivalent is an equivalence relation on \( \sC \) (@fd2:def-equivalence-relation).
:::

::: {.idea}
Each of the three clauses becomes a statement about one difference sequence. Reflexivity looks at \( a - a \), the zero sequence. Symmetry looks at \( b - a \), the negative of \( a - b \). Transitivity writes \( a - c \) as the sum \( (a - b) + (b - c) \) of two null sequences. *Before reading on: which fact from Chapter 4 does transitivity use, and where is the triangle inequality hiding?*
:::

::: {.proof}
Let \( a, b, c \in \sC \).

(Eq1) \( a - a = (0)_n \), which is null (@exm-first-sequences-ordered-field (a)). So \( a \sim a \).

(Eq2) Suppose \( a \sim b \). For every \( n \), \( b_n - a_n = -(a_n - b_n) \) (@prp-ring-algebra (c)), so \( b - a = -(a - b) \), which is null by @thm-limit-laws-ordered-field (b) (\( -0 = 0 \)). So \( b \sim a \).

(Eq3) Suppose \( a \sim b \) and \( b \sim c \). For every \( n \),
\[
a_n - c_n = (a_n - b_n) + (b_n - c_n) ,
\]
so \( a - c = (a - b) + (b - c) \), a sum of two null sequences. By the sum rule @thm-limit-laws-ordered-field (a), it is null (\( 0 + 0 = 0 \)). So \( a \sim c \).

This proves that \( \sim \) is an equivalence relation on \( \sC \).
:::

The answer to the prompt: transitivity uses the sum rule of the limit laws, @thm-limit-laws-ordered-field (a), and the triangle inequality is inside its proof, where \( \abs{(a_n - b_n) + (b_n - c_n)} \le \abs{a_n - b_n} + \abs{b_n - c_n} \) splits the tolerance into two halves. Written out directly: given \( \varepsilon \), take thresholds for \( a - b \) and \( b - c \) with tolerance \( \varepsilon/2 \), and their maximum serves \( a - c \).

By @fd2:thm-classes-partition, \( \sC \) now falls apart into disjoint classes, and two Cauchy sequences lie in the same class exactly when their difference is null. Section 5.2 takes these classes as the real numbers.

## The truncations and the Newton sequence

The two sequences of the hook are the first test of the definition.

::: {#exm-truncations-equivalent}
[The Truncations and the Newton Sequence Are Equivalent]

Show that \( (d_k) \) is non-decreasing, that \( (d_k) \in \sC \), and that \( (d_k) \sim (x_k) \).
:::

::: {.solution}
*Step 1: \( (d_k) \) is non-decreasing.* Let \( k \in \nN \). By the choice of \( m_k \) and the defining equation \( 10^{k+1} = 10^k \cdot 10 \),
\[
(10 m_k)^2 = 100 \, m_k^2 \le 200 \, (10^k)^2 = 2 \, (10^k \cdot 10)^2 = 2 \, (10^{k+1})^2 .
\]
So \( 10 m_k \) is a natural number whose square is at most \( 2 (10^{k+1})^2 \), and \( m_{k+1} \) is the largest such: \( 10 m_k \le m_{k+1} \). Dividing by \( 10^{k+1} > 0 \) (@prp-reciprocal-order (a), @prp-ordered-ring-rules (c)),
\[
d_{k+1} = \frac{m_{k+1}}{10^{k+1}} \ge \frac{10 m_k}{10^k \cdot 10} = \frac{m_k}{10^k} = d_k .
\]
By @fd1:ax-induction on \( i \), with base \( P(0) \) (\( d_k \le d_k \)) and the step just proved, \( d_k \le d_{k+i} \) for every \( i \in \nN \). Every \( j \ge k \) is \( k + i \) for some \( i \in \nN \) (@prp-omega-order-arithmetic (a)), so \( d_k \le d_j \) whenever \( j \ge k \). In particular \( d_k \ge d_0 = 1 \) for every \( k \) (\( m_0 = 1 \), since \( 1^2 \le 2 < 2^2 \)). No law of exponents was used, only the defining equation of \( 10^{k+1} \).

*Step 2: \( d_k \le d_j < d_k + 1/10^k \) for \( j \ge k \), and \( (d_k) \in \sC \).* The lower bound is Step 1. For the upper bound, \( m_j^2 \le 2 (10^j)^2 \) gives \( d_j^2 \le 2 \). Since \( m_k + 1 > m_k \), the maximality of \( m_k \) gives \( (m_k + 1)^2 > 2 (10^k)^2 \), that is,
\[
\Bigl( d_k + \frac{1}{10^k} \Bigr)^2 = \frac{(m_k + 1)^2}{(10^k)^2} > 2 .
\]
If we had \( d_j \ge d_k + 1/10^k \), then, both sides being non-negative, \( d_j^2 \ge (d_k + 1/10^k)^2 > 2 \) (@prp-ordered-ring-rules (g)), against \( d_j^2 \le 2 \). By trichotomy, \( d_j < d_k + 1/10^k \). With @eq-ten-power-reciprocal,
\[
0 \le d_j - d_k < \frac{1}{10^k} \le \frac{1}{k + 1} \qquad (j \ge k) .
\]{#eq-truncation-cauchy-bound}
Now let \( \varepsilon \in \nQ_{>0} \). By @cor-rationals-archimedean-epsilon there is \( n_\varepsilon \in \nZ_{>0} \) with \( 1/m < \varepsilon \) for every integer \( m \ge n_\varepsilon \). Let \( N \coloneqq n_\varepsilon \), which depends on \( \varepsilon \) only. For \( j, k \ge N \), say with \( j \ge k \) (the other case is symmetric, as \( \abs{d_j - d_k} = \abs{d_k - d_j} \)), @eq-truncation-cauchy-bound gives \( \abs{d_j - d_k} < 1/(k + 1) < \varepsilon \), since \( k + 1 > N \). So \( (d_k) \in \sC \).

*Step 3: \( 0 \le 2 - d_k^2 < 5/10^k \).* The first inequality is \( d_k^2 \le 2 \). For the second, expand the display of Step 2 (@prp-ring-algebra (d)):
\[
2 < d_k^2 + \frac{2 d_k}{10^k} + \frac{1}{10^k} \cdot \frac{1}{10^k} .
\]
Here \( d_k < 2 \), since \( 0 \le d_k \) and \( d_k^2 \le 2 < 4 = 2^2 \) (@prp-ordered-ring-rules (g)); and \( (1/10^k)(1/10^k) \le 1/10^k \), since \( 0 < 1/10^k \le 1 \) by @eq-ten-power-reciprocal. So \( 2 - d_k^2 < 4/10^k + 1/10^k = 5/10^k \).

*Step 4: \( (d_k) \sim (x_k) \).* Let \( k \ge 1 \). By (NS2), \( x_k > 1 \), and \( d_k \ge 1 \) by Step 1, so \( x_k + d_k \ge 1 \). Since \( \abs{x_k - d_k} \ge 0 \), @prp-ordered-field-halves (d) gives
\[
\begin{aligned}
\abs{x_k - d_k} &\le \abs{x_k - d_k} (x_k + d_k) = \abs{x_k^2 - d_k^2} \\
&\le \abs{x_k^2 - 2} + \abs{2 - d_k^2} \le \frac{1}{4k} + \frac{5}{10^k} ,
\end{aligned}
\]
by @prp-absolute-value-ordered-field (b) and (e), the bound \( 0 < x_k^2 - 2 \le 1/(4k) \) from (NS1)–(NS2), and Step 3. Since \( 4k - (k + 1) = 3k - 1 > 0 \), \( 1/(4k) \le 1/(k + 1) \) (@prp-ordered-field-halves (c)). Define, for **every** \( k \in \nN \),
\[
u_k \coloneqq \frac{1}{k + 1} + \frac{5}{10^k} .
\]
Then \( -u_k \le x_k - d_k \le u_k \) for every \( k \ge 1 \) (@prp-absolute-value-ordered-field (d)). The sequence \( (u_k) \) is null: \( (1/(k + 1)) \) is null (@exm-first-sequences-ordered-field (b)); \( (1/10^k) \) is null by the squeeze @prp-limit-preserves-order-ordered-field (c) between \( (0)_k \) and \( (1/(k + 1)) \), using @eq-ten-power-reciprocal; \( (5/10^k) \) is null by @thm-limit-laws-ordered-field (b) with \( c = 5 \); and the sum of two null sequences is null (@thm-limit-laws-ordered-field (a)). So \( (-u_k) \) is null too, by (b) with \( c = -1 \). The squeeze @prp-limit-preserves-order-ordered-field (c), with \( N_0 = 1 \), lower sequence \( (-u_k) \) and upper sequence \( (u_k) \), shows that \( (x_k - d_k) \) is null. Both sequences are in \( \sC \) (by (NS3) and Step 2), so \( (x_k) \sim (d_k) \), and \( (d_k) \sim (x_k) \) by symmetry.

The bound of Step 4 is crude but honest: at \( k = 1 \) it gives \( \abs{x_1 - d_1} \le 1/4 + 5/10 = 3/4 \), while in fact \( x_1 - d_1 = 3/2 - 7/5 = 1/10 \).
:::

The upper sequence \( (u_k) \) is defined for every \( k \), including \( k = 0 \), where \( 1/(4k) \) is not; the squeeze only needs the inequality from \( N_0 = 1 \) on. One consequence is worth recording at once: **\( (d_k) \) has no limit in \( \nQ \) either.** If \( d_k \to L \in \nQ \), then \( x_k = d_k + (x_k - d_k) \to L + 0 = L \) by the sum rule, against (NS3). So the truncations, like the Newton sequence, are Cauchy and aim at nothing in \( \nQ \), and @exm-truncations-equivalent says they aim at the same nothing.

## Finite changes, and shifts

A class will contain far more than the two sequences of the hook. The next example shows how loose the relation is at the start of a sequence.

::: {#exm-finite-change-equivalent}
[Finite Changes and Shifts]

::: {.enumerate options="label=(\alph*)"}
1. Let \( a, b \in \sC \), and suppose there is \( N_0 \in \nN \) with \( a_n = b_n \) for every \( n \ge N_0 \). Show that \( a \sim b \).
2. Let \( a \in \sC \), and let \( s \coloneqq (a_{n+1})_{n \in \nN} \) be the shifted sequence. Show that \( s \in \sC \) and \( s \sim a \).
:::
:::

::: {.solution}
(a) For \( n \ge N_0 \), \( a_n - b_n = 0 \). So \( a - b \) agrees with the null sequence \( (0)_n \) from \( N_0 \) on, and is null by @prp-tail-change-ordered-field (a). Hence \( a \sim b \).

(b) Let \( \varepsilon \in \nQ_{>0} \), and let \( N \) be a threshold for \( a \) with tolerance \( \varepsilon \) (@def-rational-cauchy-sequences). For \( m, n \ge N \), also \( m + 1, n + 1 \ge N \), so \( \abs{s_m - s_n} = \abs{a_{m+1} - a_{n+1}} < \varepsilon \): \( s \in \sC \), with the same thresholds. For \( n \ge N \), apply the Cauchy condition to the pair \( (n + 1, n) \), both indices \( \ge N \):
\[
\abs{s_n - a_n} = \abs{a_{n+1} - a_n} < \varepsilon .
\]
So \( s - a \) is null, and \( s \sim a \).
:::

By (a), a representative of a class may begin with **any** finite list of rationals: \( (5, -3, 7, 1/4, 1/5, 1/6, \dots) \), which is \( 1/(n + 1) \) from \( n = 3 \) on, is equivalent to \( (1/(n + 1))_n \), and so to \( (0)_n \). Part (b) uses the Cauchy condition with the two indices \( n + 1 \) and \( n \); a sequence of rationals that is not Cauchy can fail it (for \( ((-1)^n)_n \), every \( \abs{a_{n+1} - a_n} \) is \( 2 \)).

::: {.warning}
**Equivalent is not "eventually equal", and not "close at the start".** \( (1/(n + 1))_n \sim (0)_n \), though no term of the first sequence is \( 0 \). And \( (0)_n \) and \( (1 - 1/(n + 1))_n \) have the same first term, \( 0 \), but are **not** equivalent: their difference converges to \( 1 \) (@thm-limit-laws-ordered-field), so it is not null, by uniqueness of limits. Only the behavior far out counts, and it counts at every tolerance.
:::

::: {.check}
Let \( a \coloneqq (1, 0, 1, 0, \dots) \), with \( a_n = 1 \) for even \( n \) and \( a_n = 0 \) for odd \( n \); and let \( b \coloneqq (1, 0, 1/2, 0, 1/3, 0, \dots) \), with \( b_{2k} = 1/(k + 1) \) and \( b_{2k+1} = 0 \). Which of them lies in \( \sC \)? For the one that does, find a constant sequence equivalent to it.
:::

::: {.solution}
\( a \notin \sC \). The negation of the Cauchy condition (moving \( \neg \) inward as in @fd1:prp-bounded-quantifier-negation) reads
\[
\exists \varepsilon \in \nQ_{>0} \ \ \forall N \in \nN \ \ \exists m, n \ge N \ \ \abs{a_m - a_n} \ge \varepsilon ,
\]
and it holds with \( \varepsilon = 1/2 \): for any \( N \), the indices \( m = N \) and \( n = N + 1 \) have one even and one odd, so \( \abs{a_m - a_n} = 1 \ge 1/2 \).

\( b \in \sC \), and \( b \sim (0)_n \). Indeed \( b \) is null: given \( \varepsilon \in \nQ_{>0} \), @cor-rationals-archimedean-epsilon gives \( K \in \nZ_{>0} \) with \( 1/m < \varepsilon \) for every integer \( m \ge K \). For \( n \ge 2K \), either \( n \) is odd and \( b_n = 0 < \varepsilon \), or \( n = 2k \) with \( k \ge K \) and \( b_n = 1/(k + 1) < \varepsilon \). So \( b \) is null, hence in \( \sC \) (@thm-cauchy-algebra-ordered-field (a)), and \( b - (0)_n = b \) is null. The pattern "a non-zero term every other index" is the same in \( a \) and \( b \); what differs is whether those terms die out.
:::

The relation is in place, and it is an equivalence relation. The next section takes its classes as the real numbers and gives them an arithmetic.

## Exercises

### A. Check your understanding

::: {#exr-cauchy-sequences-of-rationals-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. For each sequence of rationals, decide whether it lies in \( \sC \) and whether it is null, with a one-line reason: \( ((-1)^n/(n + 1))_n \); \( (n)_n \); \( (1 + 1/(n + 1))_n \); \( (d_k)_k \); \( ((-1)^n)_n \).
2. Write "\( a \not\sim b \)", for \( a, b \in \sC \), in symbols, with no \( \neg \) in front of a quantifier.
3. True or false: if \( a \sim b \), then \( a_n = b_n \) for at least one \( n \). Give a reason.
:::
:::

::: {.solution}
(a)

- \( ((-1)^n/(n + 1)) \): in \( \sC \) and null. Its absolute value is \( 1/(n + 1) \) (@prp-absolute-value-ordered-field (b), \( \abs{(-1)^n} = 1 \)), which is below any \( \varepsilon \in \nQ_{>0} \) from some index on (@exm-first-sequences-ordered-field (b)); null sequences are in \( \sC \) (@thm-cauchy-algebra-ordered-field (a)).
- \( (n) \): neither. It is not bounded (@thm-rationals-archimedean), so it is not Cauchy (@prp-cauchy-bounded-ordered-field), and not null (a null sequence is convergent, hence bounded, @prp-convergent-bounded-ordered-field).
- \( (1 + 1/(n + 1)) \): in \( \sC \), not null. It converges to \( 1 \) (@thm-limit-laws-ordered-field (a)), so it is Cauchy (@prp-convergent-cauchy-ordered-field), and its limit is not \( 0 \) (@thm-limit-unique-ordered-field).
- \( (d_k) \): in \( \sC \) (@exm-truncations-equivalent), not null: \( d_k \ge 1 \) for every \( k \), so the tolerance \( \varepsilon = 1 \) has no threshold.
- \( ((-1)^n) \): neither. Consecutive terms differ by \( 2 \), so \( \varepsilon = 1 \) has no Cauchy threshold; and it is not null, since every term has absolute value \( 1 \).

(b) By @fd1:prp-bounded-quantifier-negation and @fd1:prp-negated-implication, reading \( \neg(x < \varepsilon) \) as \( x \ge \varepsilon \):
\[
\exists \varepsilon \in \nQ_{>0} \ \ \forall N \in \nN \ \ \exists n \in \nN \ \ \bigl( n \ge N \wedge \abs{a_n - b_n} \ge \varepsilon \bigr) .
\]
One rational tolerance is beaten at indices beyond every threshold.

(c) False. \( (1/(n + 1))_n \sim (0)_n \), and \( 1/(n + 1) \ne 0 \) for every \( n \).
:::

### B. Practice

::: {#exr-cauchy-sequences-of-rationals-b1}
[B1: Equivalent or not]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( (1/(n + 1))_n \sim (1/(n + 2))_n \) and that both are equivalent to \( (0)_n \).
2. Determine which constant sequences \( (c)_n \), \( c \in \nQ \), are equivalent to \( (3 + 1/(n + 1))_n \). Justify your answer.
:::
:::

::: {.solution}
(a) Both sequences are null: the first by @exm-first-sequences-ordered-field (b); the second is the first shifted by one, \( (a_{n+1})_n \) with \( a_n = 1/(n + 1) \), so it is null by @prp-tail-change-ordered-field (b). Null sequences lie in \( \sC \) (@thm-cauchy-algebra-ordered-field (a)), and a null sequence \( a \) satisfies \( a \sim (0)_n \), since \( a - (0)_n = a \). By symmetry and transitivity (@prp-cauchy-equivalent-relation), \( (1/(n + 1)) \sim (0)_n \sim (1/(n + 2)) \) gives \( (1/(n + 1)) \sim (1/(n + 2)) \).

(b) Only \( c = 3 \). The difference \( (3 + 1/(n + 1)) - (c)_n = (3 - c) + 1/(n + 1) \) converges to \( 3 - c \), by the sum rule (@thm-limit-laws-ordered-field (a)) with the constant \( 3 - c \) and the null \( (1/(n + 1)) \). By uniqueness of limits (@thm-limit-unique-ordered-field) it is null if and only if \( 3 - c = 0 \). Hence \( (3 + 1/(n + 1)) \sim (c)_n \) exactly when \( c = 3 \); this is consistent with the degenerate example after @def-cauchy-equivalent, since two constants equivalent to one sequence are equivalent to each other, hence equal.
:::

::: {#exr-cauchy-sequences-of-rationals-b2}
[B2: Null differences preserve Cauchy]

::: {.enumerate options="label=(\alph*)"}
1. Let \( a \in \sC \), and let \( b \colon \nN \to \nQ \) be a sequence such that \( a - b \) is null. Prove that \( b \in \sC \) and \( b \sim a \).
2. Hence show that \( (2/x_n)_n \in \sC \) and \( (2/x_n)_n \sim (x_n)_n \), where \( (x_n) \) is the Newton sequence.
:::
:::

::: {.solution}
(a) For every \( n \), \( b_n = a_n - (a_n - b_n) \), so \( b = a - (a - b) \). Here \( a \in \sC \), and \( a - b \) is null, hence in \( \sC \) (@thm-cauchy-algebra-ordered-field (a)); the difference of two members of \( \sC \) is in \( \sC \) (@thm-cauchy-algebra-ordered-field (b)). So \( b \in \sC \). Then \( a \sim b \) by definition, and \( b \sim a \) by symmetry.

(b) By (NS1), \( x_n > 0 \), so \( 2/x_n \) is defined. For every \( n \),
\[
x_n - \frac{2}{x_n} = \frac{x_n^2 - 2}{x_n} = \frac{e_n}{x_n} .
\]
By (NS1) and (NS2), \( e_n > 0 \) and \( x_n > 1 \), so \( 0 < 1/x_n < 1 \) (@prp-reciprocal-order) and \( 0 < e_n/x_n < e_n \) (@prp-ordered-ring-rules (c)). For \( n \ge 1 \), \( e_n \le 1/(4n) \le 1/(n + 1) \). So \( 0 \le x_n - 2/x_n \le 1/(n + 1) \) for every \( n \ge 1 \), and the squeeze @prp-limit-preserves-order-ordered-field (c), with \( N_0 = 1 \) and the null sequence \( (1/(n + 1)) \) (@exm-first-sequences-ordered-field (b)), shows that \( (x_n - 2/x_n) \) is null. Part (a), with \( a = (x_n) \in \sC \) (NS3) and \( b = (2/x_n) \), gives the claim. The terms \( 2/x_n \) satisfy \( (2/x_n)^2 = 4/x_n^2 < 2 \), so this sequence approaches the hole from below, as the truncations do.
:::

::: {#exr-cauchy-sequences-of-rationals-b3}
[B3: Every other Newton term]

Show that \( (x_{2n})_n \sim (x_n)_n \) for the Newton sequence. *Hint: imitate @exm-finite-change-equivalent (b).*
:::

::: {.solution}
First, \( (x_{2n})_n \in \sC \). Let \( \varepsilon \in \nQ_{>0} \), and let \( N \) be a threshold for \( (x_n) \) with tolerance \( \varepsilon \) (NS3). For \( m, n \ge N \), also \( 2m \ge m \ge N \) and \( 2n \ge N \), so \( \abs{x_{2m} - x_{2n}} < \varepsilon \).

Second, the difference is null. For \( n \ge N \), the two indices \( 2n \) and \( n \) are both \( \ge N \), so \( \abs{x_{2n} - x_n} < \varepsilon \). So \( (x_{2n} - x_n)_n \) is null, with the same thresholds as \( (x_n) \), and \( (x_{2n}) \sim (x_n) \).

The Cauchy condition was used with two indices that are far apart (\( 2n \) and \( n \)). This is exactly where "every pair of indices beyond \( N \)" is needed, and not only neighbors.
:::

### C. Going deeper

::: {#exr-cauchy-sequences-of-rationals-c1}
[C1: Subsequences]

Let \( a \in \sC \), and let \( k \mapsto n_k \) be a function \( \nN \to \nN \) with \( n_k < n_{k+1} \) for every \( k \in \nN \) (for instance \( n_k = 2k \), or any sequence of indices defined by @fd2:thm-recursion with this property).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( n_k \ge k \) for every \( k \), that \( (a_{n_k})_{k \in \nN} \in \sC \), and that \( (a_{n_k})_k \sim a \).
2. Deduce: if \( a, b \in \sC \) and \( a_{n_k} = b_{n_k} \) for every \( k \), then \( a \sim b \). Compare with the warning after @exm-finite-change-equivalent: why does this not say that sequences which are "close at the start" are equivalent?
:::
:::

::: {.solution}
[Hint 1]

For (a), the indices \( n_k \) run ahead of \( k \). Once you know \( n_k \ge k \), the Cauchy condition applies to the pair \( (n_k, k) \).
:::

::: {.solution}
[Hint 2]

For (a), prove \( n_k \ge k \) by @fd1:ax-induction on \( k \); the step uses \( n_{k+1} > n_k \ge k \).
:::

::: {.solution}
(a) *\( n_k \ge k \).* By @fd1:ax-induction on \( k \), base \( P(0) \): \( n_0 \ge 0 \) (@thm-omega-order (d)). Step: if \( n_k \ge k \), then \( n_{k+1} > n_k \ge k \), so \( k < n_{k+1} \); by @thm-omega-order (b), \( n_{k+1} < k + 1 \) would give \( n_{k+1} \le k \), so by trichotomy \( n_{k+1} \ge k + 1 \).

*In \( \sC \).* Let \( \varepsilon \in \nQ_{>0} \), and let \( N \) be a threshold for \( a \) with tolerance \( \varepsilon \). For \( j, k \ge N \), \( n_j \ge j \ge N \) and \( n_k \ge k \ge N \), so \( \abs{a_{n_j} - a_{n_k}} < \varepsilon \).

*Equivalent to \( a \).* For \( k \ge N \), both \( n_k \ge N \) and \( k \ge N \), so \( \abs{a_{n_k} - a_k} < \varepsilon \). So \( (a_{n_k} - a_k)_k \) is null, with the same thresholds, and \( (a_{n_k})_k \sim a \).

(b) By (a), \( (a_{n_k})_k \sim a \) and \( (b_{n_k})_k \sim b \). The two subsequences are the same sequence, since \( a_{n_k} = b_{n_k} \) for every \( k \). So \( a \sim (a_{n_k})_k = (b_{n_k})_k \sim b \), using symmetry for the first step, and transitivity (@prp-cauchy-equivalent-relation) gives \( a \sim b \).

The hypothesis of (b) is that the sequences agree at **infinitely many** indices, \( n_0 < n_1 < \cdots \), arbitrarily far out. In the warning, \( (0)_n \) and \( (1 - 1/(n + 1))_n \) agree only at \( n = 0 \). Agreement far out, along a whole subsequence, forces equivalence for Cauchy sequences; agreement at finitely many places says nothing. (For sequences that are not Cauchy, (b) fails: \( (1, 0, 1, 0, \dots) \) and \( (1)_n \) agree at every even index, and their difference is not null.)

**Marking scheme.** (10 points)

- 2: proves \( n_k \ge k \) by induction, with the step justified.
- 3: shows \( (a_{n_k}) \in \sC \), with one threshold that serves all \( j, k \ge N \) and with \( n_j, n_k \ge N \) justified from \( n_k \ge k \).
- 3: shows \( (a_{n_k} - a_k)_k \) is null by applying the Cauchy condition to the pair \( (n_k, k) \).
- 2: deduces (b) by symmetry and transitivity of \( \sim \).

Fatal errors (0 for the step): using a limit of \( a \) in \( \nQ \); a threshold that depends on \( k \).
:::

<!-- dependency ledger
exm-truncations-equivalent (claim): N = omega and the identification N in Z in Q, so that 10 = 10 * 1_Q and k + 1 is rational | cor-omega-identification (b), prp-naturals-in-ordered-field (d), F3.2 identification remarks (cited)
exm-truncations-equivalent (claim): (k + 1) + 1 = k + 2 and 1 <= k + 1 in N | thm-omega-arithmetic-laws (cited), thm-omega-order (d); carried into Q by prp-naturals-in-ordered-field (a), (b)
exm-truncations-equivalent (claim): 10^k in Z and 10^k >= k + 1, by induction | inline, fd1:ax-induction (cited); 9y - 1 >= 8 > 0 for y >= 1 by prp-ordered-ring-rules (b), (c)
exm-truncations-equivalent (claim): existence and uniqueness of m_k, the largest natural number with m^2 <= 2 (10^k)^2 | inline, prp-integer-least-element and thm-integers-ordered-ring (c) (cited); (10^k)^2 > 0 from 10^k >= 1
exm-truncations-equivalent (claim): table of m_k for k <= 6 and the differences x_k - d_k for k = 1, 2, 3 | verify/ch05/exm-truncations-equivalent.py
exm-truncations-equivalent (claim): x_k^2 > 2 >= d_k^2, so x_k != d_k | exm-newton-rationals-sqrt2 (i) (cited) and the definition of m_k
def-cauchy-equivalent (claim): a convergent pair with a common limit has null difference | thm-limit-laws-ordered-field (b) (cited)
prp-cauchy-equivalent-relation (proof): b_n - a_n = -(a_n - b_n); -0 = 0, 0 + 0 = 0 | prp-ring-algebra (c) (cited); field axioms of Q
exm-truncations-equivalent (solution): (10 m)^2 = 100 m^2 and 100 * 2 (10^k)^2 = 2 (10^k * 10)^2; m_{k+1}/(10^k 10) rearranged | field arithmetic in Q (thm-rationals-ordered-field, prp-ring-algebra); defining equation of 10^{k+1}; no exponent law
exm-truncations-equivalent (solution): every j >= k is k + i | prp-omega-order-arithmetic (a) (cited)
exm-truncations-equivalent (solution): m_0 = 1, d_0 = 1 | 1 <= 2 < 4; verify/ch05/exm-truncations-equivalent.py
exm-truncations-equivalent (solution): a <= b with a, b >= 0 gives a^2 <= b^2 | prp-ordered-ring-rules (g) (cited) with the case a = b
exm-truncations-equivalent (solution): (d + h)^2 = d^2 + 2dh + h^2 | prp-ring-algebra (d) (cited)
exm-truncations-equivalent (solution): 0 <= x <= 1 gives x * x <= x | prp-ordered-field-halves (d) (cited) with (x, 1)
exm-truncations-equivalent (solution): 4k >= k + 1 for k >= 1 | inline, 3k - 1 > 0
exm-truncations-equivalent (solution): |x - d| (x + d) = |x^2 - d^2| | prp-absolute-value-ordered-field (b) (cited), |x + d| = x + d as x + d > 0
exm-truncations-equivalent (solution): numerical check at k = 1 (3/4 and 1/10) | verify/ch05/exm-truncations-equivalent.py
exm-truncations-equivalent (claim): (d_k) has no limit in Q | thm-limit-laws-ordered-field (a), thm-sqrt2-cauchy-no-rational-limit (cited)
exm-finite-change-equivalent (claim): the example list (5, -3, 7, 1/4, ...) is 1/(n + 1) from n = 3 on | inline
exm-finite-change-equivalent (claim): |(-1)^{n+1} - (-1)^n| = 2 | inline, as in F3.9's ledger for thm-cauchy-not-null-sign
exm-finite-change-equivalent (claim): (warning) 1 - 1/(n + 1) -> 1 | thm-limit-laws-ordered-field (a), (b) and exm-first-sequences-ordered-field (cited)
exm-finite-change-equivalent (claim): (check) b is null, n >= 2K splits into odd n and n = 2k with k >= K | inline parity of natural numbers (prp-omega-powers-parity, F3.1 §06)
exr-cauchy-sequences-of-rationals-a1 (solution): |(-1)^n| = 1 | prp-absolute-value-ordered-field (b), induction; inline
exr-cauchy-sequences-of-rationals-a1 (solution): negation of a ~ b | fd1:prp-bounded-quantifier-negation, fd1:prp-negated-implication (cited)
exr-cauchy-sequences-of-rationals-b2 (solution): x - 2/x = (x^2 - 2)/x; 4/x^2 < 2 from x^2 > 2 | field arithmetic (lem-field-fraction-rules (b)), prp-reciprocal-order; verify/ch05/exr-cauchy-sequences-of-rationals-b2.py
exr-cauchy-sequences-of-rationals-c1 (solution): (1, 0, 1, 0, ...) and (1) agree at even indices | inline
-->
