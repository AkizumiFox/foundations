# Interpolation, Quotient Rings, and the Chinese Remainder Theorem

Section 5.4 proved a uniqueness statement: two polynomials of degree at most \( n \) that agree at \( n + 1 \) distinct points are equal (@thm-polynomial-identity-from-values (a)). It said nothing about existence. Is there, for instance, a quadratic through the points \( (0, 1) \), \( (1, 3) \), \( (2, 7) \)? This section builds one by a formula. It then reads the same question as three congruences. By @thm-polynomial-remainder-factor (a), "the value at \( c \) is \( y \)" says that \( f \) leaves the remainder \( y \) on division by \( x - c \). So we look for \( f \) with
\[
f \equiv 1 \pmod{x} , \qquad f \equiv 3 \pmod{x - 1} , \qquad f \equiv 7 \pmod{x - 2} .
\]
Three congruences to coprime moduli: that is the Chinese remainder theorem of *Number Systems: From \( \nN \) to \( \nR \)*, Chapter 3 (@fd3:thm-chinese-remainder-two), with polynomials in place of integers. On the way we meet the classes modulo a polynomial \( m \). They form a ring \( F[x]/\langle m \rangle \), and it is a field exactly when \( m \) is irreducible, as \( \nZ/p\nZ \) is a field exactly when \( p \) is prime.

Throughout, \( F \) is a field. "Polynomial" means an element of \( F[x] \) unless another field is named.

## Polynomials through given points

The points at which values are prescribed are called **nodes**. Suppose the nodes are \( c_0, \dots, c_n \in F \) and the values \( y_0, \dots, y_n \in F \). Fitting all the values at once is hard. Fitting one value while ignoring the others would be easy if we had, for each node \( c_i \), a polynomial that is \( 1 \) at \( c_i \) and \( 0 \) at every other node: then \( y_0 \) times the first, plus \( y_1 \) times the second, and so on, has every value right. A polynomial that vanishes at the nodes \( c_j \) with \( j \ne i \) is a multiple of the product of the factors \( x - c_j \) (@thm-polynomial-root-count); the simplest is that product itself. Its value at \( c_i \) is the product of the numbers \( c_i - c_j \), and dividing by that product makes the value \( 1 \).

*Each Lagrange polynomial is \( 1 \) at its own node and \( 0 \) at all the others.*

::: {#def-lagrange-polynomials-for-nodes}
[Lagrange Polynomials]

Let \( n \in \nN \) and let \( c_0, \dots, c_n \in F \) be **distinct**. For \( i \in \{0, \dots, n\} \), the \( i \)-th **Lagrange polynomial** of these nodes is
\[
\ell_i \coloneqq \prod_{\substack{j = 0 \\ j \ne i}}^{n} (c_i - c_j)^{-1} (x - c_j) \in F[x] ,
\]
the product, in increasing order of \( j \), of the \( n \) polynomials \( (c_i - c_j)^{-1}(x - c_j) \) with \( j \ne i \).
:::

The inverse \( (c_i - c_j)^{-1} \) exists because \( c_i \ne c_j \) for \( j \ne i \), and \( F \) is a field. The product of a list of polynomials is given by the recursion of @fd2:def-sum-product, read in the commutative ring \( F[x] \) (@thm-polynomial-ring-laws (a)); the pattern *Number Systems: From \( \nN \) to \( \nR \)* used for lists of integers.

**Examples.**

- *Two nodes.* For the nodes \( 0, 1 \in \nQ \): \( \ell_0 = (0 - 1)^{-1}(x - 1) = 1 - x \) and \( \ell_1 = (1 - 0)^{-1}(x - 0) = x \). Indeed \( \ell_0(0) = 1 \), \( \ell_0(1) = 0 \), \( \ell_1(0) = 0 \), \( \ell_1(1) = 1 \).
- *Three nodes.* For the nodes \( 0, 1, 2 \in \nQ \), the polynomial \( \ell_0 \) is
\[
\ell_0 = (0 - 1)^{-1}(x - 1) \cdot (0 - 2)^{-1}(x - 2) = \tfrac12 (x - 1)(x - 2) .
\]
It vanishes at \( 1 \) and \( 2 \), and \( \ell_0(0) = \tfrac12 \cdot (-1)(-2) = 1 \).
- *Over a finite field.* In \( \nF_3 \), with the nodes \( 0, 1, 2 \), the same formula gives \( \ell_0 = 2^{-1}(x - 1)(x - 2) = 2(x - 1)(x - 2) \), since \( 2 \cdot 2 = 4 = 1 \) in \( \nF_3 \). Its value at \( 0 \) is \( 2 \cdot (-1)(-2) = 4 = 1 \).

::: {.second-reading title="One node, and a repeated node"}
*One node* (\( n = 0 \)). The product defining \( \ell_0 \) has no factors, so \( \ell_0 = 1 \), the empty product. The theorem below then says that the only polynomial of degree at most \( 0 \) with value \( y_0 \) at \( c_0 \) is the constant \( y_0 \), which is right.

*A repeated node.* Change the nodes \( 0, 1 \) of the first example to \( 0, 0 \). The clause that fails is "distinct": the factor \( (c_0 - c_1)^{-1} = 0^{-1} \) does not exist. Nothing can repair this. A polynomial cannot have the value \( 1 \) at \( 0 \) and also the value \( 2 \) at \( 0 \), so with a repeated node some prescribed values have no interpolating polynomial at all.
:::

The next theorem says that the Lagrange polynomials do what they were built for, and that the polynomial they produce is the only one.

::: {#thm-polynomial-interpolation}
[Lagrange Interpolation]

Let \( n \in \nN \), let \( c_0, \dots, c_n \in F \) be distinct, and let \( y_0, \dots, y_n \in F \). Let \( \ell_0, \dots, \ell_n \) be the Lagrange polynomials of the nodes (@def-lagrange-polynomials-for-nodes).

::: {.enumerate options="label=(\alph*)"}
1. For all \( i, k \in \{0, \dots, n\} \), \( \ell_i(c_k) = 1 \) if \( k = i \) and \( \ell_i(c_k) = 0 \) if \( k \ne i \). Each \( \ell_i \) has degree exactly \( n \).
2. The polynomial \( p \coloneqq \sum_{i=0}^{n} y_i \ell_i \) satisfies \( \deg p \le n \) and \( p(c_k) = y_k \) for every \( k \).
3. It is the **only** polynomial of degree at most \( n \) with \( p(c_k) = y_k \) for every \( k \).
4. Every \( q \in F[x] \) with \( \deg q \le n \) satisfies \( q = \sum_{i=0}^{n} q(c_i) \ell_i \).
:::
:::

*Try it first (ten minutes): for the nodes \( 0, 1, 2 \in \nQ \), write down \( \ell_0, \ell_1, \ell_2 \) and check (a) on them. Then find a quadratic through \( (0, 1) \), \( (1, 3) \), \( (2, 7) \). Why can there be no second one?*

::: {.idea}
The direct attempt writes \( p = a_0 + a_1 x + a_2 x^2 \) and solves the three equations \( p(0) = 1 \), \( p(1) = 3 \), \( p(2) = 7 \) for \( a_0, a_1, a_2 \). It works here, but it gives no formula, and for \( n + 1 \) nodes it is a system of \( n + 1 \) equations. The Lagrange polynomials replace the system by a sum: (a) is "evaluate at a root", since every factor \( x - c_j \) with \( j \ne i \) vanishes at \( c_j \), and (b) follows from (a) term by term. The second question, why there is no other quadratic, is not answered by any construction. It is answered by counting roots: two such quadratics differ by a polynomial of degree at most \( 2 \) with three roots.
:::

::: {.proof}
(a) Let \( i, k \in \{0, \dots, n\} \). Evaluation respects products (@thm-evaluation-respects-operations), so \( \ell_i(c_k) \) is the product of the values of the factors at \( c_k \):
\[
\ell_i(c_k) = \prod_{\substack{j = 0 \\ j \ne i}}^{n} (c_i - c_j)^{-1} (c_k - c_j) .
\]
If \( k \ne i \), the factor with \( j = k \) is \( (c_i - c_k)^{-1} \cdot 0 = 0 \), so the product is \( 0 \). If \( k = i \), every factor is \( (c_i - c_j)^{-1}(c_i - c_j) = 1 \), so the product is \( 1 \). For the degree, each factor \( (c_i - c_j)^{-1} x - (c_i - c_j)^{-1} c_j \) has degree \( 1 \), since its coefficient of \( x \) is non-zero. A field has no zero divisors, so by @thm-degree-of-product (b) the degree of a product is the sum of the degrees; with \( n \) factors, \( \deg \ell_i = n \).

(b) Each term \( y_i \ell_i \) has degree at most \( n \) (@thm-degree-of-product (a)), so \( \deg p \le n \) by @thm-degree-of-sum, applied one term at a time. Evaluating at \( c_k \) and using (a),
\[
p(c_k) = \sum_{i=0}^{n} y_i \ell_i(c_k) = y_k ,
\]
since every term with \( i \ne k \) is \( y_i \cdot 0 = 0 \), and the term \( i = k \) is \( y_k \cdot 1 \) ((Σ3) of @lem-finite-sums-and-powers).

(c) Let \( q \in F[x] \) with \( \deg q \le n \) and \( q(c_k) = y_k \) for every \( k \). Then \( p \) and \( q \) both have degree at most \( n \) and agree at the \( n + 1 \) distinct points \( c_0, \dots, c_n \). By @thm-polynomial-identity-from-values (a), \( q = p \).

(d) Let \( \deg q \le n \), and apply (b) and (c) with \( y_i \coloneqq q(c_i) \). The polynomial \( \sum_i q(c_i) \ell_i \) and \( q \) itself both have degree at most \( n \) and the values \( q(c_0), \dots, q(c_n) \) at the nodes, so they are equal by (c). This proves the theorem.
:::

So for distinct nodes and any values, there is exactly one polynomial of degree at most \( n \) through the points, and (b) writes it down. Part (d) says that a polynomial of degree at most \( n \) is determined by its values at \( n + 1 \) nodes, and rebuilt from them by the same formula. Where the linear-algebra companion, Chapter 6, speaks of "the Lagrange basis", this book has only the formula (d); no basis is defined here.

::: {.warning}
The bound "degree at most \( n \)" in (c) is what makes the interpolant unique. Without it, uniqueness fails: \( p \) and \( p + (x - c_0)(x - c_1) \cdots (x - c_n) \) have the same values at every node, and the second has degree \( n + 1 \). For the nodes \( 0, 1 \) and the values \( 5, 8 \), both \( 5 + 3x \) and \( 5 + 3x + x(x - 1) = 5 + 2x + x^2 \) pass through \( (0, 5) \) and \( (1, 8) \).
:::

::: {.check}
Write down the Lagrange polynomials of the nodes \( 0, 1 \) in \( \nQ \), and use them to find the line through \( (0, 5) \) and \( (1, 8) \).
:::

::: {.solution}
\( \ell_0 = 1 - x \) and \( \ell_1 = x \) (the first example after @def-lagrange-polynomials-for-nodes). By @thm-polynomial-interpolation (b), the line is \( 5 \ell_0 + 8 \ell_1 = 5(1 - x) + 8x = 5 + 3x \). Check: its values at \( 0 \) and \( 1 \) are \( 5 \) and \( 8 \).
:::

Here is a cubic, worked through the formula.

::: {#exm-polynomial-interpolation-cubic}
[A cubic through four points]

Find the polynomial \( p \in \nQ[x] \) of degree at most \( 3 \) with \( p(-1) = 2 \), \( p(0) = 1 \), \( p(1) = 2 \) and \( p(2) = 11 \).
:::

::: {.solution}
The nodes \( c_0 = -1 \), \( c_1 = 0 \), \( c_2 = 1 \), \( c_3 = 2 \) are distinct. From @def-lagrange-polynomials-for-nodes, with the denominators computed first,
\[
\begin{aligned}
\ell_0 &= \bigl( (-1)(-2)(-3) \bigr)^{-1} x(x - 1)(x - 2) = (-6)^{-1} (x^3 - 3x^2 + 2x) , \\
\ell_1 &= \bigl( (1)(-1)(-2) \bigr)^{-1} (x + 1)(x - 1)(x - 2) = 2^{-1} (x^3 - 2x^2 - x + 2) , \\
\ell_2 &= \bigl( (2)(1)(-1) \bigr)^{-1} (x + 1)x(x - 2) = (-2)^{-1} (x^3 - x^2 - 2x) , \\
\ell_3 &= \bigl( (3)(2)(1) \bigr)^{-1} (x + 1)x(x - 1) = 6^{-1} (x^3 - x) .
\end{aligned}
\]
By @thm-polynomial-interpolation (b), \( p = 2\ell_0 + \ell_1 + 2\ell_2 + 11\ell_3 \). Collect each power of \( x \):
\[
\begin{aligned}
x^3 &: \ -\tfrac13 + \tfrac12 - 1 + \tfrac{11}{6} = 1 , & x^2 &: \ 1 - 1 + 1 = 1 , \\
x &: \ -\tfrac23 - \tfrac12 + 2 - \tfrac{11}{6} = -1 , & 1 &: \ 0 + 1 + 0 + 0 = 1 .
\end{aligned}
\]
So \( p = x^3 + x^2 - x + 1 \). Check the four values: \( p(-1) = -1 + 1 + 1 + 1 = 2 \), \( p(0) = 1 \), \( p(1) = 1 + 1 - 1 + 1 = 2 \), \( p(2) = 8 + 4 - 2 + 1 = 11 \). By @thm-polynomial-interpolation (c), no other polynomial of degree at most \( 3 \) has these values.
:::

## Congruence modulo a polynomial

The opening question turned values into remainders. To compute with remainders as *Number Systems: From \( \nN \) to \( \nR \)*, Chapter 3 did with integers, we need the relation "same remainder" and the classes it makes.

::: {#def-polynomial-congruence}
[Congruence Modulo a Polynomial]

Let \( m \in F[x] \). Polynomials \( f, g \in F[x] \) are **congruent modulo** \( m \), written \( f \equiv g \pmod{m} \), if \( m \mid f - g \) (@def-polynomial-divides), that is, if \( f - g \in \langle m \rangle \) (@def-polynomial-combinations).
:::

In words: \( f \) and \( g \) differ by a multiple of \( m \). The set \( \langle m \rangle \) of multiples of \( m \) is an ideal of the commutative ring \( F[x] \) (@def-polynomial-combinations), so the relation is the relation \( \sim_I \) of @fd3:thm-quotient-ring-by-ideal for the ideal \( I = \langle m \rangle \), and @fd3:thm-quotient-ring-by-ideal (a) makes it an equivalence relation. We write \( [f] = f + \langle m \rangle \) for the class of \( f \), and \( [f]_m \) when the modulus must be named.

**Examples.**

- \( x^2 \equiv -1 \pmod{x^2 + 1} \), since \( x^2 - (-1) = 1 \cdot (x^2 + 1) \).
- For every \( c \in F \), \( f \equiv f(c) \pmod{x - c} \): by @thm-polynomial-remainder-factor (a), \( f = q(x - c) + f(c) \) for some \( q \), so \( f - f(c) \) is a multiple of \( x - c \).
- Two polynomials are congruent modulo \( m \) exactly when they leave the same remainder on division by \( m \ne 0 \); this is (b) of the next theorem.

::: {.second-reading title="The degenerate moduli 0 and the constants"}
For \( m = 0 \), \( f \equiv g \pmod{0} \) means \( 0 \mid f - g \), that is, \( f = g \) (@prp-polynomial-divisibility-rules (a)): every class is a single polynomial. For a non-zero constant \( m \), every \( f \) is a multiple of \( m \) (@prp-polynomial-divisibility-rules (a)), so all polynomials are congruent and there is one class; the ring it forms is the zero ring, in which \( [1] = [0] \). Both cases are legal and neither is useful, which is why the next theorem asks for \( \deg m \ge 1 \).
:::

::: {.check}
Is \( x^3 \equiv x \pmod{x^2 + 1} \) in \( \nQ[x] \)? In \( \nF_2[x] \)?
:::

::: {.solution}
Divide: \( x^3 = x(x^2 + 1) - x \), so \( x^3 \equiv -x \), and \( x^3 - x = x(x^2 + 1) - 2x \). Hence \( x^3 \equiv x \) exactly when \( x^2 + 1 \mid -2x \). In \( \nQ[x] \) the polynomial \( -2x \) is non-zero of degree \( 1 < 2 \), so \( x^2 + 1 \) does not divide it (@prp-polynomial-divisibility-rules (d)): **no**. In \( \nF_2[x] \), \( -2x = 0 \), which every polynomial divides: **yes**. The same symbols give different answers over different fields.
:::

## The ring of classes modulo a polynomial

*Number Systems: From \( \nN \) to \( \nR \)*, Chapter 3 built \( \nZ/n\nZ \) as the quotient of \( \nZ \) by the ideal \( n\nZ \), and found in each class exactly one remainder in \( \{0, \dots, n - 1\} \). The same construction works for \( F[x] \) and an ideal \( \langle m \rangle \), and division with remainder again picks one representative per class, now "of degree less than \( \deg m \)".

::: {#thm-polynomial-quotient-ring}
[The Ring of Polynomials Modulo m]

Let \( m \in F[x] \) with \( d \coloneqq \deg m \ge 1 \), and write \( [f] = f + \langle m \rangle \).

::: {.enumerate options="label=(\alph*)"}
1. \( F[x]/\langle m \rangle \), with \( [f] + [g] \coloneqq [f + g] \) and \( [f][g] \coloneqq [fg] \), is a commutative ring with zero \( [0] \) and one \( [1] \), and \( [1] \ne [0] \).
2. Each class contains **exactly one** polynomial of degree less than \( d \): the remainder of any of its members on division by \( m \). In particular \( f \equiv g \pmod{m} \) if and only if \( f \) and \( g \) leave the same remainder, and sending each class to its member of degree less than \( d \) is a bijection from \( F[x]/\langle m \rangle \) onto \( \{ r \in F[x] : \deg r < d \} \).
3. The map \( F \to F[x]/\langle m \rangle \), \( c \mapsto [c] \) (\( c \) a constant), is injective and preserves \( + \) and \( \cdot \).
4. \( [f] \) is a unit of \( F[x]/\langle m \rangle \) (@fd3:def-ring-unit) **if and only if** \( \gcd(f, m) = 1 \). In that case \( [f]^{-1} = [a] \) for **any** \( a, b \in F[x] \) with \( af + bm = 1 \).
:::
:::

::: {.idea}
Part (a) is the quotient theorem of *Number Systems: From \( \nN \) to \( \nR \)* applied to the ideal \( \langle m \rangle \); only \( [1] \ne [0] \) needs the degree. Part (b) is division with remainder read twice: existence of the remainder puts one polynomial of small degree into each class, and "compare degrees" shows a class cannot hold two, since their difference would be a non-zero multiple of \( m \) of smaller degree than \( m \). Part (d) translates \( [a][f] = [1] \) into a Bézout identity, exactly as for \( \nZ/n\nZ \).
:::

::: {.proof}
(a) By @def-polynomial-combinations, \( \langle m \rangle \) is an ideal of the commutative ring \( F[x] \), so @fd3:thm-quotient-ring-by-ideal (a)–(c) give the commutative ring \( F[x]/\langle m \rangle \) with these operations, zero \( [0] \) and one \( [1] \). By @fd3:thm-quotient-ring-by-ideal (d), \( [1] = [0] \) would mean \( 1 \in \langle m \rangle \), that is, \( m \mid 1 \); then \( \deg m \le \deg 1 = 0 \) by @prp-polynomial-divisibility-rules (d), against \( d \ge 1 \). So \( [1] \ne [0] \).

(b) Since \( d \ge 1 \), \( m \ne 0 \). *Existence.* Let \( f \in F[x] \). By @thm-polynomial-division-remainder (a), \( f = qm + r \) with \( \deg r < d \). Then \( f - r = qm \in \langle m \rangle \), so \( r \in [f] \). *Uniqueness.* Let \( r, r' \in [f] \) with \( \deg r, \deg r' < d \). Then \( r - r' \in \langle m \rangle \) (both are \( \sim \) to \( f \), and \( \sim \) is an equivalence relation), so \( m \mid r - r' \), and \( \deg(r - r') < d \) by @thm-degree-of-sum. If \( r - r' \ne 0 \), then \( d \le \deg(r - r') \) by @prp-polynomial-divisibility-rules (d), a contradiction. So \( r = r' \).

Hence two polynomials are congruent exactly when their classes are equal (@fd2:thm-classes-partition (b)), exactly when the classes have the same member of degree less than \( d \), which is the common remainder. The map "class \( \mapsto \) its member of degree less than \( d \)" is a function by the uniqueness just proved. It is injective, since two classes with a common member are equal (@fd2:thm-classes-partition (c)); and it is surjective, since a polynomial \( r \) with \( \deg r < d \) is the member of degree less than \( d \) of its own class \( [r] \).

(c) For constants \( c, c' \), \( [c] + [c'] = [c + c'] \) and \( [c][c'] = [cc'] \) by the definition of the operations, where \( c + c' \) and \( cc' \) are computed in \( F \) (@thm-polynomial-ring-laws (b)). If \( [c] = [c'] \), then \( c \) and \( c' \) are members of one class of degree at most \( 0 < d \), so \( c = c' \) by (b).

(d) \( (\Leftarrow) \) Suppose \( \gcd(f, m) = 1 \). By @cor-polynomial-coprime-iff-combination there are \( a, b \in F[x] \) with \( af + bm = 1 \); let \( a, b \) be any such pair. Then \( af - 1 = -bm \in \langle m \rangle \), so \( [a][f] = [af] = [1] \). So \( [f] \) is a unit, and its inverse, which is unique (@fd3:def-ring-unit), is \( [a] \).

\( (\Rightarrow) \) Suppose \( [a][f] = [1] \) for some \( a \in F[x] \) (every element of the quotient is a class, @fd2:def-quotient-set). Then \( af - 1 \in \langle m \rangle \): \( af - 1 = km \) for some \( k \in F[x] \). Hence \( af + (-k)m = 1 \), and \( \gcd(f, m) = 1 \) by @cor-polynomial-coprime-iff-combination. This proves the theorem.
:::

So \( F[x]/\langle m \rangle \) is a ring whose elements may be named by the polynomials of degree less than \( \deg m \), and by (c) its constants form a copy of \( F \). From now on we write \( c \) for the class \( [c] \) of a constant when no confusion can arise. A computation in the quotient is: compute with representatives, then replace the result by its remainder. The integer twins are @fd3:thm-integers-mod-n-ring (b) (one remainder per class) and @fd3:thm-units-mod-n (units).

::: {.check}
In \( \nQ[x]/\langle x^2 - 2 \rangle \), show that \( [x + 1] \) is a unit, and find its inverse with (d).
:::

::: {.solution}
Divide: \( x^2 - 2 = (x - 1)(x + 1) - 1 \). Hence \( (x - 1)(x + 1) + (-1)(x^2 - 2) = 1 \), so \( \gcd(x + 1, x^2 - 2) = 1 \) (@cor-polynomial-coprime-iff-combination), and by @thm-polynomial-quotient-ring (d) with \( a = x - 1 \), \( [x + 1] \) is a unit with \( [x + 1]^{-1} = [x - 1] \). Check: \( (x + 1)(x - 1) = x^2 - 1 \equiv 2 - 1 = 1 \pmod{x^2 - 2} \).
:::

When is every non-zero class a unit? By (d), when every \( f \) with \( m \nmid f \) is coprime to \( m \). For an irreducible \( m \), @cor-irreducible-divides-product (a) says exactly this. For a reducible \( m \), a factor of \( m \) of smaller positive degree is neither a multiple of \( m \) nor coprime to it.

::: {#thm-polynomial-quotient-field}
[The Quotient Is a Field Exactly When m Is Irreducible]

Let \( m \in F[x] \) with \( \deg m \ge 1 \). Then \( F[x]/\langle m \rangle \) is a field (@def-field) **if and only if** \( m \) is irreducible over \( F \) (@def-irreducible-over-field).
:::

::: {.proof}
By @thm-polynomial-quotient-ring (a), \( F[x]/\langle m \rangle \) is a commutative ring with \( [1] \ne [0] \). So it is a field exactly when every non-zero element is a unit.

\( (\Leftarrow) \) Let \( m \) be irreducible and \( [f] \ne [0] \). Then \( f \notin \langle m \rangle \) by @fd3:thm-quotient-ring-by-ideal (d), that is, \( m \nmid f \). By @cor-irreducible-divides-product (a), \( \gcd(m, f) = 1 \); the definition of the gcd (@def-polynomial-gcd) is symmetric in its two arguments, so \( \gcd(f, m) = 1 \). Hence \( [f] \) is a unit by @thm-polynomial-quotient-ring (d).

\( (\Rightarrow) \) Let \( m \) be not irreducible. Since \( \deg m \ge 1 \), @def-irreducible-over-field gives \( g, h \in F[x] \), neither a constant, with \( m = gh \). Then \( g, h \ne 0 \) and \( \deg g, \deg h \ge 1 \), and \( \deg g + \deg h = \deg m \) (@thm-degree-of-product (b)), so \( \deg g, \deg h < \deg m \). A non-zero polynomial of degree less than \( \deg m \) is not a multiple of \( m \) (@prp-polynomial-divisibility-rules (d)), so \( [g] \ne [0] \) and \( [h] \ne [0] \). But \( [g][h] = [gh] = [m] = [0] \). In a field a product of non-zero elements is non-zero (@thm-field-basic-properties (f)), so \( F[x]/\langle m \rangle \) is not a field. This proves the theorem.
:::

This is @fd3:thm-integers-mod-prime-field with "prime" replaced by "irreducible". It manufactures new fields: from \( F \) and an irreducible \( m \) of degree \( d \), a field whose elements are named by the polynomials of degree less than \( d \).

::: {#exm-polynomial-quotient-four-elements}
[A field with four elements, and the complex numbers again]

(i) Describe \( \nF_2[x]/\langle x^2 + x + 1 \rangle \), and show that it is a field with four elements.

(ii) Describe \( \nR[x]/\langle x^2 + 1 \rangle \).
:::

::: {.solution}
(i) Let \( m \coloneqq x^2 + x + 1 \in \nF_2[x] \). Its values are \( m(0) = 1 \) and \( m(1) = 1 + 1 + 1 = 1 \) in \( \nF_2 \), so \( m \) has no root in \( \nF_2 \); it has degree \( 2 \), so it is irreducible by @prp-irreducible-low-degree (b), and the quotient is a field by @thm-polynomial-quotient-field. By @thm-polynomial-quotient-ring (b), its elements are the classes of the polynomials of degree less than \( 2 \) over \( \nF_2 \), namely \( 0, 1, x, x + 1 \): four elements. Write \( \alpha \coloneqq [x] \). Since \( x^2 - (x + 1) = x^2 + x + 1 \) in \( \nF_2[x] \) (where \( -1 = 1 \)), \( x^2 \equiv x + 1 \), and so
\[
\alpha^2 = \alpha + 1 , \qquad \alpha(\alpha + 1) = \alpha^2 + \alpha = 2\alpha + 1 = 1 , \qquad (\alpha + 1)^2 = \alpha^2 + 2\alpha + 1 = \alpha ,
\]
using \( 2 = 0 \) in \( \nF_2 \). The multiplication table of the non-zero elements is therefore
\[
\begin{array}{c|ccc}
\cdot & 1 & \alpha & \alpha + 1 \\ \hline
1 & 1 & \alpha & \alpha + 1 \\
\alpha & \alpha & \alpha + 1 & 1 \\
\alpha + 1 & \alpha + 1 & 1 & \alpha
\end{array}
\]
and every non-zero element has an inverse in it, as the theorem promised. Also \( \alpha^3 = \alpha \cdot \alpha^2 = \alpha(\alpha + 1) = 1 \). This is the four-element field of @exr-finite-fields-from-modular-arithmetic-c1. There the rule \( \alpha^2 = 1 + \alpha \) is part of the definition of the multiplication; here it is computed, as the remainder of \( x^2 \) on division by \( x^2 + x + 1 \).

(ii) The polynomial \( x^2 + 1 \in \nR[x] \) has no real root, since \( c^2 + 1 \ge 1 > 0 \) for every \( c \in \nR \) (@fd3:prp-ordered-ring-rules (e)); it has degree \( 2 \), so it is irreducible (@prp-irreducible-low-degree (b)), and \( \nR[x]/\langle x^2 + 1 \rangle \) is a field. Its elements are the classes \( [a + bx] \) with \( a, b \in \nR \), each named by exactly one such polynomial, and \( [x]^2 = [x^2] = [-1] \). So it is a field containing a copy of \( \nR \) (@thm-polynomial-quotient-ring (c)) and an element whose square is \( -1 \): it looks like the complex numbers of Chapter 1, and Exercise B3 shows it is a copy of them.
:::

The theorem needs "irreducible", and having no root is not a substitute: Section 5.3 showed that the two differ from degree \( 4 \) on.

::: {.warning}
"\( m \) has no root, so \( F[x]/\langle m \rangle \) is a field" is false. The polynomial \( m = (x^2 + 1)^2 \in \nR[x] \) has no real root: for every \( c \in \nR \), \( c^2 + 1 > 0 \) (@exm-polynomial-quotient-four-elements (ii)), so \( m(c) = (c^2 + 1)^2 > 0 \) by @fd3:prp-ordered-ring-rules (e). But \( [x^2 + 1] \ne [0] \), since \( x^2 + 1 \) has degree \( 2 < 4 = \deg m \), while \( [x^2 + 1]^2 = [(x^2 + 1)^2] = [0] \). A non-zero element with square zero cannot be a unit, so \( \nR[x]/\langle (x^2 + 1)^2 \rangle \) is not a field.
:::

::: {.check}
Is \( \nQ[x]/\langle x^2 - 2 \rangle \) a field? Is \( \nR[x]/\langle x^2 - 2 \rangle \)?
:::

::: {.solution}
\( \nQ[x]/\langle x^2 - 2 \rangle \): **yes**. A rational root \( c \) would give \( c^2 = 2 \), impossible by @fd3:thm-no-rational-square-two; so \( x^2 - 2 \) is irreducible over \( \nQ \) (@prp-irreducible-low-degree (b)), and @thm-polynomial-quotient-field applies. \( \nR[x]/\langle x^2 - 2 \rangle \): **no**. With \( s \) the positive square root of \( 2 \) in \( \nR \) (@fd3:prp-cof-square-roots), \( x^2 - 2 = (x - s)(x + s) \) is reducible over \( \nR \), and the theorem says the quotient is not a field; concretely \( [x - s][x + s] = [0] \).
:::

## The Chinese remainder theorem for polynomials

Now several congruences at once. *Number Systems: From \( \nN \) to \( \nR \)*, Chapter 3 solved two congruences to coprime integer moduli by writing \( 1 \) as a combination of the moduli and multiplying (@fd3:thm-chinese-remainder-two). With polynomials the move is the same, and we take \( k \) moduli at once. The one new ingredient is that coprimality survives products.

::: {#lem-polynomial-coprime-to-product}
[Coprime to Each Factor, Coprime to the Product]

::: {.enumerate options="label=(\alph*)"}
1. Let \( s \ge 1 \) and \( p, q_1, \dots, q_s \in F[x] \). If \( \gcd(p, q_j) = 1 \) for every \( j \), then \( \gcd(p, q_1 \cdots q_s) = 1 \).
2. Let \( k \ge 1 \) and let \( m_1, \dots, m_k \in F[x] \) be **pairwise coprime**: \( \gcd(m_i, m_j) = 1 \) whenever \( i \ne j \). If \( m_i \mid h \) for every \( i \), then \( m_1 \cdots m_k \mid h \).
:::
:::

*In words: a polynomial coprime to each factor is coprime to the product, and pairwise coprime divisors of \( h \) divide \( h \) together.*

::: {.second-reading title="The proof: multiply the Bézout identities"}
::: {.idea}
For (a), write \( 1 \) as a combination of \( p \) and each factor, and multiply the identities: every term of the product but one contains \( p \), and the remaining term is a multiple of the product of the factors. For (b), the product of the first \( k \) moduli is coprime to the next one by (a), so two coprime divisors combine (@prp-polynomial-coprime-divisors-product); induction adds one modulus at a time.
:::

::: {.proof}
(a) Induction on \( s \) (@fd1:ax-induction, from \( s = 1 \)). For \( s = 1 \) there is nothing to prove. Suppose the claim holds for \( s \), and let \( p \) be coprime to each of \( q_1, \dots, q_{s+1} \). Write \( Q \coloneqq q_1 \cdots q_s \), so that \( q_1 \cdots q_{s+1} = Q q_{s+1} \) by the product recursion (@fd2:def-sum-product, read in \( F[x] \)). By the induction hypothesis and @cor-polynomial-coprime-iff-combination, \( ap + bQ = 1 \) and \( a'p + b'q_{s+1} = 1 \) for some \( a, b, a', b' \in F[x] \). Multiplying the two identities and expanding,
\[
p \, (aa'p + ab'q_{s+1} + a'bQ) + (bb') \, Q q_{s+1} = 1 .
\]
So \( \gcd(p, Qq_{s+1}) = 1 \) by @cor-polynomial-coprime-iff-combination.

(b) Induction on \( k \) (@fd1:ax-induction, from \( k = 1 \)). For \( k = 1 \) there is nothing to prove. Suppose the claim holds for \( k \), and let \( m_1, \dots, m_{k+1} \) be pairwise coprime, each dividing \( h \). With \( M \coloneqq m_1 \cdots m_k \), the induction hypothesis gives \( M \mid h \). The modulus \( m_{k+1} \) is coprime to each of \( m_1, \dots, m_k \), so \( \gcd(m_{k+1}, M) = 1 \) by (a), and \( \gcd(M, m_{k+1}) = 1 \) since the gcd is symmetric (@def-polynomial-gcd). By @prp-polynomial-coprime-divisors-product, \( M m_{k+1} = m_1 \cdots m_{k+1} \) divides \( h \).
:::
:::

Without coprimality (b) fails: for \( m_1 = m_2 = x \) and \( h = x \), each \( m_i \) divides \( h \), but \( m_1 m_2 = x^2 \) does not (@prp-polynomial-divisibility-rules (d)); here \( \gcd(m_1, m_2) = x \ne 1 \).

::: {#thm-polynomial-chinese-remainder}
[Chinese Remainder Theorem for Polynomials]

Let \( k \ge 1 \), let \( m_1, \dots, m_k \in F[x] \) be non-zero and pairwise coprime, and let \( m \coloneqq m_1 \cdots m_k \). For each \( i \), let \( M_i \) be the product of the \( m_j \) with \( j \ne i \) (in increasing order of \( j \)).

::: {.enumerate options="label=(\alph*)"}
1. For each \( i \) there are \( a_i, b_i \in F[x] \) with \( a_i M_i + b_i m_i = 1 \). Put \( e_i \coloneqq a_i M_i \). Then \( e_i \equiv 1 \pmod{m_i} \) and \( e_i \equiv 0 \pmod{m_j} \) for \( j \ne i \), and for all \( r_1, \dots, r_k \in F[x] \) the polynomial \( f \coloneqq \sum_{i=1}^{k} r_i e_i \) satisfies
\[
f \equiv r_i \pmod{m_i} \qquad \text{for every } i \in \{1, \dots, k\} .
\]
2. A polynomial \( g \) satisfies the same \( k \) congruences **if and only if** \( g \equiv f \pmod{m} \).
3. Exactly one polynomial of degree less than \( \deg m \) satisfies the \( k \) congruences.
4. The rule \( \Phi([f]_m) \coloneqq ([f]_{m_1}, \dots, [f]_{m_k}) \) is a well-defined **bijection**
\[
\Phi \colon F[x]/\langle m \rangle \to F[x]/\langle m_1 \rangle \times \dots \times F[x]/\langle m_k \rangle ,
\]
and, with \( + \) and \( \cdot \) on the right taken componentwise, \( \Phi \) preserves \( + \) and \( \cdot \) and sends \( [1]_m \) to \( ([1]_{m_1}, \dots, [1]_{m_k}) \).
:::
:::

::: {.idea}
This is the integer proof of @fd3:thm-chinese-remainder-two with \( k \) moduli. The identity \( a_i M_i + b_i m_i = 1 \) makes a polynomial \( e_i \) that is \( 1 \) modulo \( m_i \) and \( 0 \) modulo every other modulus, as \( \ell_i \) is \( 1 \) at one node and \( 0 \) at the others. Then \( \sum r_i e_i \) has every remainder right. Uniqueness modulo \( m \) is @lem-polynomial-coprime-to-product (b): a difference divisible by every \( m_i \) is divisible by their product. Part (c) picks the remainder modulo \( m \), and (d) restates (a) and (b) as a bijection.
:::

::: {.proof}
By (L2) of Section 5.3, applied to the list \( (m_1, \dots, m_k) \) with the entry \( i \) removed, \( m = M_i m_i \), so \( m_i \mid m \); and \( m_j \mid M_i \) for \( j \ne i \), by the last clause of (L2), since \( m_j \) is an entry of the list whose product is \( M_i \). By (L1) of Section 5.3, \( m \ne 0 \), since every \( m_i \) is non-zero.

(a) If \( k = 1 \), then \( M_1 = 1 \) (the empty product), and \( a_1 \coloneqq 1 \), \( b_1 \coloneqq 0 \) will do. If \( k \ge 2 \), then \( m_i \) is coprime to each \( m_j \) with \( j \ne i \), so @lem-polynomial-coprime-to-product (a) gives \( \gcd(m_i, M_i) = 1 \); by the symmetry of the gcd and @cor-polynomial-coprime-iff-combination, \( a_i M_i + b_i m_i = 1 \) for some \( a_i, b_i \). In either case \( e_i - 1 = -b_i m_i \), so \( e_i \equiv 1 \pmod{m_i} \); and for \( j \ne i \), \( m_j \mid M_i \mid e_i \), so \( e_i \equiv 0 \pmod{m_j} \).

Now fix \( j \). In \( f - r_j = \sum_{i \ne j} r_i e_i + r_j(e_j - 1) \), every term with \( i \ne j \) is a multiple of \( m_j \), and so is \( r_j(e_j - 1) = -r_j b_j m_j \). A sum of multiples of \( m_j \) is a multiple of \( m_j \) (@prp-polynomial-divisibility-rules (c), and induction on the number of terms). So \( f \equiv r_j \pmod{m_j} \).

(b) \( (\Rightarrow) \) Suppose \( g \equiv r_i \pmod{m_i} \) for every \( i \). Then \( m_i \mid (g - r_i) - (f - r_i) = g - f \) for every \( i \) (@prp-polynomial-divisibility-rules (c)). The \( m_i \) are pairwise coprime, so \( m \mid g - f \) by @lem-polynomial-coprime-to-product (b). \( (\Leftarrow) \) Suppose \( m \mid g - f \). Since \( m_i \mid m \), \( m_i \mid g - f \) (@prp-polynomial-divisibility-rules (b)), and then \( m_i \mid (g - f) + (f - r_i) = g - r_i \) for every \( i \).

(c) *Existence.* Since \( m \ne 0 \), divide \( f \) by \( m \): \( f = qm + r \) with \( \deg r < \deg m \) (@thm-polynomial-division-remainder). Then \( r \equiv f \pmod{m} \), so \( r \) satisfies the \( k \) congruences by (b). *Uniqueness.* If \( g \) and \( g' \) both satisfy them and have degree less than \( \deg m \), then \( g \equiv f \equiv g' \pmod{m} \) by (b), so \( m \mid g - g' \), while \( \deg(g - g') < \deg m \) (@thm-degree-of-sum). A non-zero multiple of \( m \) has degree at least \( \deg m \) (@prp-polynomial-divisibility-rules (d)), so \( g = g' \). (If every \( m_i \) is a non-zero constant, then \( \deg m = 0 \), and the one solution of degree less than \( 0 \) is the zero polynomial.)

(d) *Well defined.* Fix \( i \). If \( f \equiv g \pmod{m} \), then \( f \equiv g \pmod{m_i} \), since \( m_i \mid m \). By @fd3:thm-well-defined-on-classes (a), applied to the identity map of \( F[x] \) with congruence modulo \( m \) on the source and modulo \( m_i \) on the target, there is exactly one function \( F[x]/\langle m \rangle \to F[x]/\langle m_i \rangle \) sending \( [f]_m \) to \( [f]_{m_i} \). Taking these \( k \) functions together gives \( \Phi \).

*Surjective.* An element of the target is \( ([r_1]_{m_1}, \dots, [r_k]_{m_k}) \) for some \( r_1, \dots, r_k \in F[x] \) (@fd2:def-quotient-set). With \( f \) as in (a), \( [f]_{m_i} = [r_i]_{m_i} \) for every \( i \) (@fd2:thm-classes-partition (b)), so \( \Phi([f]_m) \) is that element.

*Injective.* If \( \Phi([f]_m) = \Phi([g]_m) \), then \( [f]_{m_i} = [g]_{m_i} \), that is, \( m_i \mid g - f \), for every \( i \) (@fd2:thm-classes-partition (b)). By @lem-polynomial-coprime-to-product (b), \( m \mid g - f \), that is, \( [g]_m = [f]_m \).

*Operations.* By the definition of \( + \) in each quotient (@fd3:thm-quotient-ring-by-ideal (b)) and of the componentwise sum,
\[
\begin{aligned}
\Phi([f]_m + [g]_m) &= \Phi([f + g]_m) = ([f + g]_{m_1}, \dots, [f + g]_{m_k}) \\
&= ([f]_{m_1} + [g]_{m_1}, \dots, [f]_{m_k} + [g]_{m_k}) = \Phi([f]_m) + \Phi([g]_m) .
\end{aligned}
\]
The same lines with \( fg \) in place of \( f + g \) give the product, and \( \Phi([1]_m) = ([1]_{m_1}, \dots, [1]_{m_k}) \) by definition. This proves the theorem.
:::

In (a) the solution is built from the moduli alone, and the right-hand sides \( r_i \) enter linearly; the \( e_i \) depend only on \( m_1, \dots, m_k \). Part (c) is the version used in computation: reduce any solution modulo \( m \). Compared with @fd3:thm-chinese-remainder-two, this theorem allows any number \( k \ge 1 \) of moduli in one step, where the integer theorem combines two at a time.

::: {.check}
Find the polynomial \( f \in \nQ[x] \) of degree less than \( 2 \) with \( f \equiv 3 \pmod{x} \) and \( f \equiv 5 \pmod{x - 1} \).
:::

::: {.solution}
By @thm-polynomial-remainder-factor (b), \( f \equiv 3 \pmod{x} \) says that \( 0 \) is a root of \( f - 3 \), that is, \( f(0) = 3 \); likewise the second congruence says \( f(1) = 5 \). By @thm-polynomial-interpolation, \( f = 3(1 - x) + 5x = 3 + 2x \). (The Chinese remainder route: \( x - (x - 1) = 1 \), so \( e_1 = -(x - 1) = 1 - x \) and \( e_2 = x \), and \( f = 3e_1 + 5e_2 \), the same polynomial.)
:::

The check is no accident. Interpolation is the Chinese remainder theorem for the moduli \( x - c_i \).

::: {#prp-interpolation-as-chinese-remainder}
[Interpolation Is the Chinese Remainder Theorem for Linear Moduli]

Let \( n \in \nN \), let \( c_0, \dots, c_n \in F \) be distinct, let \( y_0, \dots, y_n \in F \), and let \( m \coloneqq (x - c_0) \cdots (x - c_n) \).

::: {.enumerate options="label=(\alph*)"}
1. The moduli \( x - c_0, \dots, x - c_n \) are pairwise coprime, and \( \deg m = n + 1 \).
2. For \( f \in F[x] \) and each \( i \): \( f \equiv y_i \pmod{x - c_i} \) **if and only if** \( f(c_i) = y_i \).
3. The polynomial of degree less than \( n + 1 \) given by @thm-polynomial-chinese-remainder (c) for the right-hand sides \( y_0, \dots, y_n \) is \( \sum_{i} y_i \ell_i \), the interpolating polynomial of @thm-polynomial-interpolation. In particular, the remainder of the polynomial \( e_i \) of @thm-polynomial-chinese-remainder (a) on division by \( m \) is the Lagrange polynomial \( \ell_i \).
:::
:::

*In words: the congruences modulo \( x - c_i \) are the values at \( c_i \), so the polynomial of the Chinese remainder theorem is the interpolating polynomial, and its building blocks \( e_i \), reduced modulo \( m \), are the Lagrange polynomials.*

::: {.second-reading title="The proof: evaluate, and compare by uniqueness"}
::: {.idea}
Two linear moduli differ by a non-zero constant, which is a Bézout identity after scaling. A congruence modulo \( x - c \) is a statement about the value at \( c \), by the factor theorem. And two polynomials of degree less than \( n + 1 \) solving the same congruences are equal, by the uniqueness half of the Chinese remainder theorem; so it is enough to check that the Lagrange formula solves them.
:::

::: {.proof}
(a) For \( i \ne j \), \( (x - c_i) - (x - c_j) = c_j - c_i \), a non-zero constant. Multiplying by its inverse,
\[
(c_j - c_i)^{-1}(x - c_i) - (c_j - c_i)^{-1}(x - c_j) = 1 ,
\]
so \( \gcd(x - c_i, x - c_j) = 1 \) by @cor-polynomial-coprime-iff-combination. Each factor of \( m \) has degree \( 1 \), so \( \deg m = n + 1 \) by @thm-degree-of-product (b).

(b) By @thm-polynomial-remainder-factor (b), \( x - c_i \mid f - y_i \) if and only if \( c_i \) is a root of \( f - y_i \), and \( (f - y_i)(c_i) = f(c_i) - y_i \) by @thm-evaluation-respects-operations.

(c) The polynomial \( p \coloneqq \sum_i y_i \ell_i \) has degree at most \( n < n + 1 \) and \( p(c_i) = y_i \) for every \( i \) (@thm-polynomial-interpolation (b)), so by (b) it satisfies the congruences \( p \equiv y_i \pmod{x - c_i} \). By the uniqueness in @thm-polynomial-chinese-remainder (c), it is the solution of degree less than \( \deg m \). For the second claim, fix \( i \) and take the right-hand sides \( 1 \) at the index \( i \) and \( 0 \) elsewhere. By @thm-polynomial-chinese-remainder (a), \( e_i \) satisfies these congruences, and so does its remainder on division by \( m \), which is congruent to \( e_i \) modulo \( m \) (@thm-polynomial-chinese-remainder (b)) and has degree less than \( \deg m \). By the first claim, with these right-hand sides, that remainder is \( \sum_j y_j \ell_j = \ell_i \).
:::
:::

So two routes lead to the same polynomial. The Lagrange route needs only evaluation and the root count; the Chinese remainder route needs Bézout identities, and in exchange it works for moduli of any degree. The next two examples use moduli that are not all linear.

::: {#exm-polynomial-chinese-remainder-run}
[A linear and a quadratic modulus]

Find the polynomial \( f \in \nQ[x] \) of degree less than \( 3 \) with
\[
f \equiv 1 \pmod{x - 2} \qquad \text{and} \qquad f \equiv 2x - 1 \pmod{x^2 + 1} .
\]
:::

::: {.solution}
*A Bézout identity.* Divide: \( x^2 + 1 = (x + 2)(x - 2) + 5 \). Hence
\[
1 = \tfrac15 (x^2 + 1) - \tfrac15 (x + 2)(x - 2) ,
\]
so the moduli \( m_1 \coloneqq x - 2 \) and \( m_2 \coloneqq x^2 + 1 \) are coprime (@cor-polynomial-coprime-iff-combination), and \( m = (x - 2)(x^2 + 1) = x^3 - 2x^2 + x - 2 \) has degree \( 3 \).

*The polynomials \( e_1, e_2 \).* Here \( M_1 = x^2 + 1 \) and \( M_2 = x - 2 \). The identity reads \( a_1 M_1 + b_1 m_1 = 1 \) with \( a_1 = \tfrac15 \), and \( a_2 M_2 + b_2 m_2 = 1 \) with \( a_2 = -\tfrac15(x + 2) \). So
\[
e_1 = \tfrac15 (x^2 + 1) , \qquad e_2 = -\tfrac15 (x + 2)(x - 2) = -\tfrac15 (x^2 - 4) .
\]

*Assemble and reduce.* By @thm-polynomial-chinese-remainder (a),
\[
\begin{aligned}
1 \cdot e_1 + (2x - 1) e_2 &= \tfrac15 \bigl( x^2 + 1 - (2x - 1)(x^2 - 4) \bigr) \\
&= \tfrac15 \bigl( -2x^3 + 2x^2 + 8x - 3 \bigr) .
\end{aligned}
\]
Its remainder on division by \( m \) is found by adding \( \tfrac25 m \): since \( -2x^3 + 2x^2 + 8x - 3 + 2(x^3 - 2x^2 + x - 2) = -2x^2 + 10x - 7 \),
\[
f = -\tfrac25 x^2 + 2x - \tfrac75 ,
\]
the unique solution of degree less than \( 3 \) (@thm-polynomial-chinese-remainder (c)).

*Check.* \( f(2) = -\tfrac85 + 4 - \tfrac75 = 1 \), which is the first congruence (@prp-interpolation-as-chinese-remainder (b)). Modulo \( x^2 + 1 \), replace \( x^2 \) by \( -1 \): \( f \equiv \tfrac25 + 2x - \tfrac75 = 2x - 1 \).
:::

Squares of linear moduli prescribe a value and a derivative at once.

::: {#exm-hermite-by-chinese-remainder}
[Values and derivatives at once]

(a) Let \( c, a, b \in F \) and \( f \in F[x] \). Show that \( f \equiv a + b(x - c) \pmod{(x - c)^2} \) if and only if \( f(c) = a \) and \( f'(c) = b \) (the formal derivative of @def-formal-derivative).

(b) Find the polynomial \( p \in \nQ[x] \) of degree at most \( 3 \) with \( p(0) = 2 \), \( p'(0) = -1 \), \( p(1) = 1 \) and \( p'(1) = 3 \).
:::

::: {.solution}
(a) Divide by \( (x - c)^2 \), which has degree \( 2 \): \( f = q(x - c)^2 + r \) with \( \deg r \le 1 \) (@thm-polynomial-division-remainder). Every polynomial of degree at most \( 1 \) can be written \( \alpha + \beta(x - c) \) with \( \alpha, \beta \in F \): if \( r = r_0 + r_1 x \), take \( \beta \coloneqq r_1 \) and \( \alpha \coloneqq r_0 + r_1 c \). Evaluating at \( c \) (@thm-evaluation-respects-operations), \( f(c) = q(c) \cdot 0 + \alpha = \alpha \). By @thm-formal-derivative-rules (a)–(c),
\[
f' = q'(x - c)^2 + (2 \cdot 1) \, q \, (x - c) + \beta ,
\]
so \( f'(c) = \beta \). Now \( f \equiv a + b(x - c) \) if and only if \( r \equiv a + b(x - c) \), and both have degree less than \( 2 \), so by @thm-polynomial-quotient-ring (b) this holds if and only if \( \alpha + \beta(x - c) = a + b(x - c) \). Comparing the coefficients of \( x \) and then the constant terms, that is \( \beta = b \) and \( \alpha = a \), that is, \( f'(c) = b \) and \( f(c) = a \).

(b) By (a), the conditions say \( p \equiv 2 - x \pmod{x^2} \) and \( p \equiv 1 + 3(x - 1) = 3x - 2 \pmod{(x - 1)^2} \). The moduli are coprime: expanding,
\[
(2x + 1)(x - 1)^2 + (3 - 2x) x^2 = (2x^3 - 3x^2 + 1) + (3x^2 - 2x^3) = 1 .
\]
So, with \( m_1 = x^2 \) and \( m_2 = (x - 1)^2 \), @thm-polynomial-chinese-remainder (a) gives \( e_1 = 2x^3 - 3x^2 + 1 \) and \( e_2 = 3x^2 - 2x^3 \), and
\[
(2 - x)e_1 + (3x - 2)e_2 = -8x^4 + 20x^3 - 12x^2 - x + 2 .
\]
Adding \( 8m = 8(x^4 - 2x^3 + x^2) \) gives the remainder modulo \( m = x^2(x - 1)^2 \):
\[
p = 4x^3 - 4x^2 - x + 2 .
\]
Check: \( p(0) = 2 \); \( p' = 12x^2 - 8x - 1 \), so \( p'(0) = -1 \); \( p(1) = 4 - 4 - 1 + 2 = 1 \); \( p'(1) = 12 - 8 - 1 = 3 \). By @thm-polynomial-chinese-remainder (c), \( p \) is the only polynomial of degree less than \( 4 \) with these four conditions.
:::

This section met the Chinese remainder theorem three times: as interpolation (moduli \( x - c_i \)), as a value and a derivative at a point (moduli \( (x - c)^2 \)), and in general. In each case the ring \( F[x]/\langle m \rangle \) of @thm-polynomial-quotient-ring is the place where the computation happens.

## Exercises

### A. Check your understanding

::: {#exr-interpolation-and-congruences-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Finish the Try it first before @thm-polynomial-interpolation: find the polynomial of degree at most \( 2 \) through \( (0, 1) \), \( (1, 3) \), \( (2, 7) \) in \( \nQ[x] \).
2. Describe the classes of \( F[x]/\langle x \rangle \). Which ring is it, up to renaming?
3. True or false: \( \nR[x]/\langle x^2 - 1 \rangle \) is a field. Justify your answer.
4. Where does the proof of @thm-polynomial-interpolation (c) use that the nodes are distinct, and where do (a) and (b) use it?
:::
:::

::: {.solution}
(a) With the nodes \( 0, 1, 2 \), @def-lagrange-polynomials-for-nodes gives
\[
\ell_0 = \tfrac12 (x - 1)(x - 2) , \qquad \ell_1 = -x(x - 2) , \qquad \ell_2 = \tfrac12 x(x - 1) .
\]
So \( p = \ell_0 + 3\ell_1 + 7\ell_2 = \tfrac12(x^2 - 3x + 2) - 3(x^2 - 2x) + \tfrac72(x^2 - x) = x^2 + x + 1 \). Check: \( p(0) = 1 \), \( p(1) = 3 \), \( p(2) = 7 \). It is the only one of degree at most \( 2 \) (@thm-polynomial-interpolation (c)).

(b) By @thm-polynomial-quotient-ring (b) with \( d = 1 \), each class contains exactly one polynomial of degree less than \( 1 \), a constant; the constant in \( [f] \) is \( f(0) \), the remainder on division by \( x - 0 \) (@thm-polynomial-remainder-factor (a)). So the classes are the \( [c] \), \( c \in F \), and they are distinct for distinct \( c \). By @thm-polynomial-quotient-ring (c), \( c \mapsto [c] \) preserves \( + \) and \( \cdot \); it is injective, and surjective by what was just said. So \( F[x]/\langle x \rangle \) is \( F \) with each element \( c \) renamed \( [c] \); and \( [f] = [f(0)] \), so passing to the quotient is "evaluate at \( 0 \)".

(c) **False.** \( x^2 - 1 = (x - 1)(x + 1) \) is reducible, so @thm-polynomial-quotient-field says the quotient is not a field. Concretely, \( [x - 1] \ne [0] \ne [x + 1] \) (degree \( 1 < 2 \)), while \( [x - 1][x + 1] = [x^2 - 1] = [0] \).

(d) Part (c) uses distinctness only through @thm-polynomial-identity-from-values (a), which needs the \( n + 1 \) points to be distinct, ultimately because the root count of Section 5.4 counts distinct roots. Parts (a) and (b) use it to form the inverses \( (c_i - c_j)^{-1} \) in the definition of \( \ell_i \).
:::

### B. Practice

::: {#exr-interpolation-and-congruences-b1}
[B1]

Find the polynomial \( f \in \nQ[x] \) of degree less than \( 4 \) with \( f \equiv 1 \pmod{x^2} \) and \( f \equiv -1 \pmod{x^2 + 1} \).
:::

::: {.solution}
The moduli are coprime, since \( (x^2 + 1) - x^2 = 1 \) (@cor-polynomial-coprime-iff-combination), so by @thm-polynomial-chinese-remainder (c) there is exactly one such \( f \). The first congruence says \( f - 1 = x^2 h \) for some \( h \in \nQ[x] \). Then
\[
f + 1 = 2 + x^2 h = (2 - h) + h(x^2 + 1) ,
\]
so the second congruence holds if and only if \( x^2 + 1 \mid 2 - h \), that is, \( h \equiv 2 \pmod{x^2 + 1} \). The choice \( h = 2 \) gives \( f = 1 + 2x^2 \), of degree \( 2 < 4 \). Check: \( f - 1 = 2x^2 \) and \( f + 1 = 2(x^2 + 1) \). Hence \( f = 1 + 2x^2 \).
:::

::: {#exr-interpolation-and-congruences-b2}
[B2]

In \( \nQ[x]/\langle x^3 - 2 \rangle \), show that \( [x^2 + 1] \) is a unit, and compute its inverse.
:::

::: {.solution}
Run the Euclidean algorithm (@thm-euclidean-algorithm-polynomials) on \( x^3 - 2 \) and \( x^2 + 1 \):
\[
\begin{aligned}
x^3 - 2 &= x(x^2 + 1) + (-x - 2) , \\
x^2 + 1 &= (-x + 2)(-x - 2) + 5 .
\end{aligned}
\]
The last remainder is the non-zero constant \( 5 \), so the gcd is \( 1 \). Back-substitute:
\[
\begin{aligned}
5 &= (x^2 + 1) - (-x + 2)\bigl( (x^3 - 2) - x(x^2 + 1) \bigr) \\
&= (-x^2 + 2x + 1)(x^2 + 1) + (x - 2)(x^3 - 2) .
\end{aligned}
\]
Dividing by \( 5 \): \( \tfrac15(-x^2 + 2x + 1) \cdot (x^2 + 1) + \tfrac15 (x - 2) \cdot (x^3 - 2) = 1 \). By @thm-polynomial-quotient-ring (d), \( [x^2 + 1] \) is a unit and
\[
[x^2 + 1]^{-1} = \bigl[ \tfrac15 (-x^2 + 2x + 1) \bigr] .
\]
Check: \( (x^2 + 1)(-x^2 + 2x + 1) = -x^4 + 2x^3 + 2x + 1 \), and with \( x^3 \equiv 2 \), \( x^4 \equiv 2x \), this is \( \equiv -2x + 4 + 2x + 1 = 5 \).
:::

::: {#exr-interpolation-and-congruences-b3}
[B3]

::: {.enumerate options="label=(\alph*)"}
1. Write the addition and multiplication tables of \( \nF_2[x]/\langle x^2 + x + 1 \rangle \), with its elements named \( 0, 1, \alpha, \alpha + 1 \) as in @exm-polynomial-quotient-four-elements, and check from the table that every non-zero element is a unit.
2. Show that \( \varphi(a + bi) \coloneqq [a + bx] \) (\( a, b \in \nR \)) is a bijection \( \nC \to \nR[x]/\langle x^2 + 1 \rangle \) that preserves \( + \) and \( \cdot \) and sends \( 1 \) to \( [1] \).
:::
:::

::: {.solution}
(a) Addition is coefficientwise in \( \nF_2 \), where \( 1 + 1 = 0 \):
\[
\begin{array}{c|cccc}
{+} & 0 & 1 & \alpha & \alpha + 1 \\ \hline
0 & 0 & 1 & \alpha & \alpha + 1 \\
1 & 1 & 0 & \alpha + 1 & \alpha \\
\alpha & \alpha & \alpha + 1 & 0 & 1 \\
\alpha + 1 & \alpha + 1 & \alpha & 1 & 0
\end{array}
\qquad
\begin{array}{c|cccc}
\cdot & 0 & 1 & \alpha & \alpha + 1 \\ \hline
0 & 0 & 0 & 0 & 0 \\
1 & 0 & 1 & \alpha & \alpha + 1 \\
\alpha & 0 & \alpha & \alpha + 1 & 1 \\
\alpha + 1 & 0 & \alpha + 1 & 1 & \alpha
\end{array}
\]
The products come from \( \alpha^2 = \alpha + 1 \), \( \alpha(\alpha + 1) = 1 \), \( (\alpha + 1)^2 = \alpha \) (@exm-polynomial-quotient-four-elements). Each non-zero row of the multiplication table contains \( 1 \): \( 1^{-1} = 1 \), \( \alpha^{-1} = \alpha + 1 \), \( (\alpha + 1)^{-1} = \alpha \).

(b) Every complex number is \( a + bi \) for exactly one pair \( (a, b) \in \nR^2 \) (@prp-reals-embed-complex and the comparison of real and imaginary parts after it), and every element of \( \nR[x]/\langle x^2 + 1 \rangle \) is \( [a + bx] \) for exactly one such pair, by @thm-polynomial-quotient-ring (b) (the polynomials of degree less than \( 2 \) are the \( a + bx \), distinct for distinct pairs). So \( \varphi \) is a bijection. Sums: \( \varphi \) of \( (a + bi) + (c + di) = (a + c) + (b + d)i \) is \( [(a + c) + (b + d)x] = [a + bx] + [c + dx] \). Products: in \( \nR[x] \),
\[
(a + bx)(c + dx) = (ac - bd) + (ad + bc)x + bd(x^2 + 1) ,
\]
so \( [a + bx][c + dx] = [(ac - bd) + (ad + bc)x] \), which is \( \varphi \) of \( (a + bi)(c + di) = (ac - bd) + (ad + bc)i \) (@def-complex-numbers, @prp-reals-embed-complex). Finally \( \varphi(1) = [1] \). So the field of Chapter 1 could have been built as this quotient: the multiplication rule of @def-complex-numbers is "multiply, then replace \( x^2 \) by \( -1 \)".
:::

### C. Going deeper

::: {#exr-interpolation-and-congruences-c1}
[C1: Two routes to the same theorem]

Let \( c_0, \dots, c_n \in F \) be distinct and \( m \coloneqq (x - c_0) \cdots (x - c_n) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove, using @thm-polynomial-interpolation and the root count but no Bézout identity, that for all \( r_0, \dots, r_n \in F[x] \) some \( f \) satisfies \( f \equiv r_i \pmod{x - c_i} \) for every \( i \), and that \( g \) satisfies the same congruences if and only if \( g \equiv f \pmod{m} \).
2. Conversely, derive from @thm-polynomial-chinese-remainder that for all \( y_0, \dots, y_n \in F \) exactly one polynomial of degree at most \( n \) satisfies \( p(c_k) = y_k \) for every \( k \) (the content of @thm-polynomial-interpolation (b) and (c), without the formula \( \sum_i y_i \ell_i \)).
3. Which derivation is shorter, and why?
:::
:::

::: {.solution}
(a) By the second example after @def-polynomial-congruence, \( r_i \equiv r_i(c_i) \pmod{x - c_i} \). Let \( f \coloneqq \sum_i r_i(c_i) \ell_i \). By @thm-polynomial-interpolation (b), \( f(c_i) = r_i(c_i) \), so \( f \equiv r_i(c_i) \equiv r_i \pmod{x - c_i} \), by @prp-interpolation-as-chinese-remainder (b) and transitivity. If \( g \) also satisfies the congruences, then \( g - f \equiv 0 \pmod{x - c_i} \) for every \( i \), so each \( c_i \) is a root of \( g - f \) (@thm-polynomial-remainder-factor (b)). The \( c_i \) are distinct roots, so \( m \mid g - f \) by @thm-polynomial-root-count. Conversely, if \( m \mid g - f \), then each \( x - c_i \) divides \( m \) (it is an entry of the list whose product is \( m \), (L2) of Section 5.3) and so divides \( g - f \) (@prp-polynomial-divisibility-rules (b)), and \( g \equiv f \equiv r_i \pmod{x - c_i} \).

(b) By @prp-interpolation-as-chinese-remainder (a), (b), the moduli \( x - c_i \) are pairwise coprime, \( \deg m = n + 1 \), and "\( f(c_i) = y_i \) for every \( i \)" is the system \( f \equiv y_i \pmod{x - c_i} \). By @thm-polynomial-chinese-remainder (c), exactly one polynomial of degree less than \( n + 1 \), that is, of degree at most \( n \), solves it. That is the existence of an interpolating polynomial and its uniqueness at once, without the formula for \( \ell_i \); identifying it with \( \sum_i y_i \ell_i \) still needs @thm-polynomial-interpolation (a).

(c) The route in (a) is shorter in what it needs: evaluation and the root count. The route in (b) passes through @lem-polynomial-coprime-to-product and Bézout identities for the moduli. The Lagrange route is shorter because linear moduli are special: "divisible by \( x - c \)" can be tested by evaluating at \( c \), which turns every congruence into an equation in \( F \). For moduli of higher degree, evaluation at a single point is no longer enough. For \( (x - c)^2 \), @exm-hermite-by-chinese-remainder (a) needs the derivative as well as the value. For \( x^2 + 1 \) over \( \nQ \) in @exm-polynomial-chinese-remainder-run, the modulus has no root in \( \nQ \), so no evaluation in \( \nQ \) detects divisibility at all. The Chinese remainder route handles every modulus in the same way.
:::

::: {#exr-interpolation-and-congruences-c2}
[C2: Every function on a prime field is a polynomial]

Let \( p \) be a prime. Prove that every function \( \varphi \colon \nF_p \to \nF_p \) is the polynomial function \( c \mapsto f(c) \) of **exactly one** \( f \in \nF_p[x] \) with \( \deg f < p \).
:::

::: {.solution}
The elements \( 0, 1, \dots, p - 1 \) of \( \nF_p \) are \( p \) distinct elements (@def-field-fp), and there are no others. Use them as nodes, \( c_i \coloneqq i \) for \( i = 0, \dots, p - 1 \), so \( n = p - 1 \).

*Existence.* With \( y_i \coloneqq \varphi(i) \), @thm-polynomial-interpolation (b) gives \( f \) with \( \deg f \le p - 1 < p \) and \( f(i) = \varphi(i) \) for every \( i \). Since the \( i \) are all the elements of \( \nF_p \), the polynomial function of \( f \) is \( \varphi \).

*Uniqueness.* If \( g \) also has degree less than \( p \) and the function \( \varphi \), then \( f \) and \( g \) have degree at most \( p - 1 \) and agree at the \( p \) distinct nodes, so \( f = g \) by @thm-polynomial-interpolation (c).

So over \( \nF_p \) every function is a polynomial function, and the polynomials of degree less than \( p \) correspond one to one to the functions \( \nF_p \to \nF_p \). (As a count: both sets have \( p^p \) elements, \( p \) choices for each of \( p \) coefficients, or for each of \( p \) values.) Interpolation over \( \nF_p \) can use at most \( p \) nodes, since \( \nF_p \) has no more distinct elements. Polynomials of degree \( p \) or more are no longer determined by their functions: \( x^p \) and \( x \) have the same function by @thm-fermat-little (a), which is the warning of Section 5.4.
:::

<!-- dependency ledger
def-lagrange-polynomials-for-nodes (claim): product of a list of polynomials by the recursion of fd2:def-sum-product, read in the commutative ring F[x] | fd2:def-sum-product template, thm-polynomial-ring-laws (a); ledger line of the chapter (sums, products, powers)
def-lagrange-polynomials-for-nodes (example): l_0 = 1 - x, l_1 = x; l_0 = (1/2)(x - 1)(x - 2); 2 * 2 = 1 in F_3 | inline arithmetic; verify/ch05/def-lagrange-polynomials-for-nodes.py
thm-polynomial-interpolation (proof): the value of a product of a finite list is the product of the values; a product of a list with a zero entry is 0; the degree of a product of n factors of degree 1 is n | thm-evaluation-respects-operations, fd3:prp-ring-algebra (b), thm-degree-of-product (b), each extended to lists by induction on the length (fd1:ax-induction read on omega via fd3:cor-omega-identification); inline
thm-polynomial-interpolation (proof): the value of a sum of n + 1 terms is the sum of the values | thm-evaluation-respects-operations, induction on the number of terms; inline
thm-polynomial-interpolation (proof): the degree of a sum of n + 1 terms is at most the largest of their degrees | thm-degree-of-sum, extended to n + 1 terms by induction on the number of terms (fd1:ax-induction); inline
thm-polynomial-interpolation (claim): the companion's Lagrange basis (its Chapter 6) | companion (LA2.6), prose pointer; nothing depends on it
thm-polynomial-interpolation (claim): (warning) 5 + 3x and 5 + 2x + x^2 agree at 0, 1 | inline arithmetic; verify/ch05/thm-polynomial-interpolation.py
exm-polynomial-interpolation-cubic (example): the four l_i, the collected coefficients 1, 1, -1, 1, and the four values | inline arithmetic; verify/ch05/exm-polynomial-interpolation-cubic.py
def-polynomial-congruence (claim): congruence modulo m is an equivalence relation | fd3:thm-quotient-ring-by-ideal (a) with I = <m>, an ideal by def-polynomial-combinations, cited
def-polynomial-congruence (claim): (quick check) x^3 = x(x^2 + 1) - x; -2x = 0 in F_2[x] | inline arithmetic; verify/ch05/def-polynomial-congruence.py
thm-polynomial-quotient-ring (proof): two members of one class are congruent to each other | fd3:thm-quotient-ring-by-ideal (a) (sim_I is an equivalence relation), cited
thm-polynomial-quotient-ring (claim): (quick check) x^2 - 2 = (x - 1)(x + 1) - 1; [x + 1]^{-1} = [x - 1] in Q[x]/<x^2 - 2> | inline arithmetic; verify/ch05/thm-polynomial-quotient-ring.py
thm-polynomial-quotient-field (proof): gcd(m, f) = gcd(f, m) | def-polynomial-gcd (the defining conditions are symmetric in f and g), cited
exm-polynomial-quotient-four-elements (example): m(0) = m(1) = 1 in F_2; alpha^2 = alpha + 1, alpha(alpha + 1) = 1, (alpha + 1)^2 = alpha, alpha^3 = 1; the table | inline arithmetic in F_2; verify/ch05/exm-polynomial-quotient-four-elements.py
exm-polynomial-quotient-four-elements (example): comparison with the four-element field of exr-finite-fields-from-modular-arithmetic-c1 (F4.2) | prose comparison only; nothing rests on the exercise
exm-polynomial-quotient-four-elements (example): c^2 + 1 >= 1 > 0 in R | fd3:prp-ordered-ring-rules (e), with (b) and 1 > 0, cited
thm-polynomial-quotient-field (claim): (warning) c^2 + 1 != 0 (exm-polynomial-quotient-four-elements (ii)), so (c^2 + 1)^2 > 0; a non-zero element with square 0 is not a unit | fd3:prp-ordered-ring-rules (e), cited; thm-field-basic-properties (f) (or the paragraph after fd3:def-ring-unit); inline
thm-polynomial-quotient-field (claim): (quick check) x^2 - 2 = (x - s)(x + s) in R[x], s = sqrt 2 | fd3:prp-cof-square-roots, cited; inline expansion
lem-polynomial-coprime-to-product (proof): (ap + bQ)(a'p + b'q) = p(aa'p + ab'q + a'bQ) + bb'Qq | thm-polynomial-ring-laws (a) (commutative ring laws); inline; verify/ch05/lem-polynomial-coprime-to-product.py
lem-polynomial-coprime-to-product (proof): gcd is symmetric | def-polynomial-gcd, cited
thm-polynomial-chinese-remainder (proof): m = M_i m_i, so m_i | m; m_j | M_i for j != i; m = m_1...m_k is non-zero | (L2) and (L1) of Section 5.3 (03-irreducible-factorization, "Two facts about products of lists"), cited by name
thm-polynomial-chinese-remainder (proof): f - r_j = sum_{i != j} r_i e_i + r_j(e_j - 1); a sum of multiples of m_j is a multiple | lem-finite-sums-and-powers (b) (Sigma1), (Sigma3); prp-polynomial-divisibility-rules (c) with induction on the number of terms; inline
thm-polynomial-chinese-remainder (proof): the k-fold product of the quotient sets with componentwise operations | NOTATION row A_1 x ... x A_k (F2.3 §02); componentwise operations defined in the statement
thm-polynomial-chinese-remainder (claim): (quick check) e_1 = 1 - x, e_2 = x, f = 3 + 2x | inline arithmetic; verify/ch05/thm-polynomial-chinese-remainder.py
prp-interpolation-as-chinese-remainder (proof): deg m = n + 1 | thm-degree-of-product (b) with induction on the number of factors; inline
exm-polynomial-chinese-remainder-run (example): x^2 + 1 = (x + 2)(x - 2) + 5; e_1, e_2; the product and the reduction; f = -(2/5)x^2 + 2x - 7/5 and its check | inline arithmetic; verify/ch05/exm-polynomial-chinese-remainder-run.py
exm-hermite-by-chinese-remainder (example): r = alpha + beta(x - c); f' = q'(x - c)^2 + (2*1) q (x - c) + beta | thm-formal-derivative-rules (a)-(c), cited; inline
exm-hermite-by-chinese-remainder (example): the Bezout identity, e_1, e_2, the product, the reduction, p = 4x^3 - 4x^2 - x + 2 and its four checks | inline arithmetic; verify/ch05/exm-hermite-by-chinese-remainder.py
exr-interpolation-and-congruences-a1 (solution): l_0, l_1, l_2 for the nodes 0, 1, 2 and p = x^2 + x + 1 | verify/ch05/exr-interpolation-and-congruences-a1.py
exr-interpolation-and-congruences-b1 (solution): f = 1 + 2x^2 | verify/ch05/exr-interpolation-and-congruences-b1.py
exr-interpolation-and-congruences-b2 (solution): the Euclidean run, back-substitution and the check | verify/ch05/exr-interpolation-and-congruences-b2.py
exr-interpolation-and-congruences-b3 (solution): the two tables of F_2[x]/<x^2 + x + 1>; the product identity (a + bx)(c + dx) | verify/ch05/exr-interpolation-and-congruences-b3.py; def-complex-numbers, prp-reals-embed-complex and the comparison of real and imaginary parts after it, cited
exr-interpolation-and-congruences-c1 (solution): congruence modulo x - c_i is transitive | fd3:thm-quotient-ring-by-ideal (a), cited through def-polynomial-congruence
exr-interpolation-and-congruences-c1 (solution): an entry of a list divides the product of the list | (L2) of Section 5.3, cited by name
exr-interpolation-and-congruences-c2 (solution): 0, 1, ..., p - 1 are all the elements of F_p and are distinct; the count p^p | def-field-fp (fd3:thm-integers-mod-n-ring (b)); the count is a remark, nothing rests on it; verify/ch05/exr-interpolation-and-congruences-c2.py (p <= 5)
-->
