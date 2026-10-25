# The Formal Derivative

The polynomials of this chapter are coefficient sequences, and @thm-polynomial-substitution showed how to evaluate them and how to substitute into them. One more operation from school survives the passage to an arbitrary commutative ring: the derivative. This section defines it by its coefficients, proves the sum, product and power rules with the move of @lem-check-on-monomials, and asks when a derivative can be \( 0 \). Over a field the answer depends on the characteristic of Chapter 1, and over \( \nF_p \) it is not the answer of calculus.

At school a double root shows itself in the graph. The parabola \( y = (x - 1)^2 \) touches the axis at \( 1 \) instead of crossing it, and its slope there is \( 0 \): the derivative \( 2(x - 1) \) vanishes at \( 1 \) as well. Over \( \nF_p \) there is no graph and no slope; the field has \( p \) elements and no limits. What survives is the formula: the derivative of \( a x^n \) is \( n a x^{n-1} \). We keep the formula and drop the limit. Chapter 4 uses the result to detect repeated roots; this section builds the tool.

Throughout, \( R \) is a commutative ring (@fd3:def-commutative-ring-and-field). Polynomials are written \( f, g, h \), with coefficients \( f_k, g_k, h_k \), because the letter \( p \) is kept for a prime. A dot with an integer on its left is a **multiple**, \( n \cdot a = a + \dots + a \) with \( n \) terms (the "Multiples" paragraph of *Number Systems: From \(\nN\) to \(\nR\)*, Section 2.3, collected in @lem-finite-sums-and-powers (d)); the product of two ring elements is written by juxtaposition.

## The derivative by coefficients

At school, \( (3x^4 + 5x^2)' = 12x^3 + 10x \). Each term moves down one place, and its coefficient is multiplied by the exponent it had. In \( R[x] \) "multiplied by the exponent" has a meaning without any division or limit: the exponent \( n \) is a natural number, and \( n \cdot a \) is the \( n \)-th multiple of \( a \). That recurring computation deserves a name.

*The formal derivative moves every coefficient down one place and takes it as many times as its old exponent.*

::: {#def-formal-derivative}
[Formal Derivative]

Let \( R \) be a commutative ring and \( f \in R[x] \). The **formal derivative** of \( f \) is the sequence \( f' \colon \nN \to R \) given by
\[
(f')_k \coloneqq (k + 1) \cdot f_{k+1} \qquad \text{for every } k \in \nN ,
\]
where \( (k + 1) \cdot f_{k+1} \) is the \( (k + 1) \)-th multiple of \( f_{k+1} \). The **higher derivatives** are defined by
\[
f^{(0)} \coloneqq f , \qquad f^{(k+1)} \coloneqq \bigl( f^{(k)} \bigr)' \quad (k \in \nN) ,
\]
and we write \( f'' \) for \( f^{(2)} \).
:::

In words: the coefficient of \( x^k \) in \( f' \) is read off from the coefficient of \( x^{k+1} \) in \( f \), added to itself \( k + 1 \) times. The definition uses only the addition of \( R \), so it makes sense, word for word, over \( \nZ \), \( \nQ \), \( \nZ/6\nZ \) and \( \nF_p \).

*Well-definedness.* Two things need checking: that \( f' \) is again a polynomial, and that the higher derivatives exist.

- **\( f' \in R[x] \).** First, \( m \cdot 0 = 0 \) for every \( m \in \nN \): by @lem-finite-sums-and-powers (d), \( m \cdot 0 = (m \cdot 1) 0 \), and this is \( 0 \) by @fd3:prp-ring-algebra (b). Now choose \( N \in \nN \) with \( f_k = 0 \) for every \( k > N \) (@def-polynomial). For \( k \ge N \) we have \( k + 1 > N \), so \( f_{k+1} = 0 \) and \( (f')_k = (k + 1) \cdot 0 = 0 \). So \( f' \) has only finitely many non-zero terms, and \( f' \in R[x] \). Moreover \( (f')_k = 0 \) for \( k > N - 1 \), so for \( N \ge 1 \), @prp-polynomial-sum-of-monomials writes \( f' \) as an honest sum:
\[
f' = \sum_{k=0}^{N-1} \bigl( (k + 1) \cdot f_{k+1} \bigr) x^k = 1 \cdot f_1 + (2 \cdot f_2) x + \dots + (N \cdot f_N) x^{N-1} .
\]
- **Higher derivatives.** Since \( u \mapsto u' \) is a function \( R[x] \to R[x] \), @fd2:thm-recursion, with \( X = R[x] \), starting value \( f \) and step \( (k, u) \mapsto u' \), gives exactly one sequence \( k \mapsto f^{(k)} \) with the two displayed properties.

**Monomials.** Let \( a \in R \) and \( n \in \nN \). The monomial \( a x^n \) has \( a \) in position \( n \) and \( 0 \) elsewhere (@def-polynomial), so \( (a x^n)_{k+1} \) is \( a \) when \( k + 1 = n \) and \( 0 \) otherwise. Hence \( ((a x^n)')_k \) is \( n \cdot a \) when \( k = n - 1 \), and \( (k + 1) \cdot 0 = 0 \) otherwise:
\[
(a x^n)' = (n \cdot a) \, x^{n-1} \quad (n \ge 1) , \qquad (a x^0)' = 0 . \tag{M}
\]
The case \( n = 0 \) is separate because \( x^{n-1} \) has no meaning there: \( -1 \notin \nN \). Every constant has derivative \( 0 \).

**The element \( n \cdot 1 \).** By @lem-finite-sums-and-powers (d), \( n \cdot a = (n \cdot 1) a \). So the exponent enters the derivative only through one element of \( R \), the multiple \( n \cdot 1 \), and **that element can be \( 0 \)**. In \( \nF_2 \), \( 2 \cdot 1 = 1 + 1 = 0 \), so \( (x^2)' = (2 \cdot 1) x = 0 \). This is the whole difference between the derivative here and the derivative of calculus, and the rest of the section keeps track of it.

**Why this definition.** The formula is the school formula with the limit removed. Exercise C1 asks you to show that it is the only additive map \( R[x] \to R[x] \) that sends constants to \( 0 \), sends \( x \) to \( 1 \) and obeys the product rule. A definition by limits is not available, since \( \nF_p \) and \( \nZ/6\nZ \) have no distances.

::: {.warning}
The coefficient of \( x^k \) in \( f' \) is \( (k + 1) \cdot f_{k+1} \), not \( k \cdot f_k \): the derivative shifts before it multiplies. For \( f = x^2 \) over \( \nQ \), the coefficient of \( x^1 \) in \( f' = 2x \) is \( 2 \cdot f_2 = 2 \), while \( 1 \cdot f_1 = 0 \). Reading the formula without the shift gives \( \sum_k (k \cdot f_k) x^k \), which is \( x f' \), not \( f' \).
:::

::: {#exm-formal-derivatives}
[Formal derivatives in five rings]

Compute the following derivatives.

(i) \( (x^4 - 2x^3 + 2x - 1)' \) over \( \nQ \).

(ii) \( a' \), \( x' \) and \( (x - c)' \) over any commutative ring \( R \), for \( a, c \in R \).

(iii) \( (x^3 + x)' \) over \( \nF_3 \), and \( (x^2)' \) over \( \nF_2 \).

(iv) \( ([2]x^3 + x)' \) over \( \nZ/6\nZ \).

(v) \( (x^n)' \) over \( \nZ \), for \( n \ge 1 \).

(vi) The higher derivatives \( (x^4)' \), \( (x^4)'' \) and \( (x^4)''' \) over \( \nQ \) and over \( \nF_3 \).
:::

::: {.solution}
In each case, by (M) and @lem-finite-sums-and-powers (d), the derivative of \( a x^n \) with \( n \ge 1 \) is \( ((n \cdot 1) a) x^{n-1} \), and the derivative of a sum is computed coefficient by coefficient from @def-formal-derivative.

(i) The coefficients are \( f_0 = -1 \), \( f_1 = 2 \), \( f_2 = 0 \), \( f_3 = -2 \), \( f_4 = 1 \), and \( f_k = 0 \) for \( k \ge 5 \). So \( (f')_0 = 1 \cdot 2 = 2 \), \( (f')_1 = 2 \cdot 0 = 0 \), \( (f')_2 = 3 \cdot (-2) = -6 \), \( (f')_3 = 4 \cdot 1 = 4 \), and \( (f')_k = 0 \) for \( k \ge 4 \). In \( \nQ \) the multiple \( n \cdot a \) is the product \( na \): \( n \cdot a = (n \cdot 1) a \) by @lem-finite-sums-and-powers (d), and \( n \cdot 1 \) is the rational number \( n \), by induction on \( n \) from \( (n + 1) \cdot 1 = n \cdot 1 + 1 \), since the embeddings \( \nN \subseteq \nZ \subseteq \nQ \) preserve sums and \( 1 \) (@fd3:prp-naturals-embed-integers, @fd3:prp-integers-embed-rationals). Hence
\[
(x^4 - 2x^3 + 2x - 1)' = 4x^3 - 6x^2 + 2 ,
\]
as at school.

(ii) \( a = a x^0 \), so \( a' = 0 \) by (M). \( x = 1 x^1 \) (@def-polynomial), so \( x' = (1 \cdot 1) x^0 = 1 \), since \( 1 \cdot 1 = 0 \cdot 1 + 1 = 1 \) by the recursion of multiples. The polynomial \( x - c \) has \( -c \) in position \( 0 \), \( 1 \) in position \( 1 \) and \( 0 \) elsewhere, so \( ((x - c)')_0 = 1 \cdot 1 = 1 \), and \( ((x - c)')_k = (k + 1) \cdot 0 = 0 \) for \( k \ge 1 \): \( (x - c)' = 1 \).

(iii) Over \( \nF_3 \), \( (x^3 + x)' = (3 \cdot 1) x^2 + 1 = 1 \), since \( 3 \cdot 1 = 1 + 1 + 1 = 0 \) in \( \nF_3 \) (@fd3:thm-integers-mod-n-ring (d): \( p \cdot [1] = [p] = [0] \) in \( \nZ/p\nZ \)). Over \( \nF_2 \), \( (x^2)' = (2 \cdot 1) x = 0 \), since \( 1 + 1 = 0 \) in \( \nF_2 \) (@exm-finite-fields).

(iv) \( ([2]x^3 + x)' = (3 \cdot [2]) x^2 + 1 = [6] x^2 + 1 = 1 \), since \( 3 \cdot [2] = (3 \cdot [1])[2] = [3][2] = [6] = [0] \), by @lem-finite-sums-and-powers (d), @fd3:thm-integers-mod-n-ring (d), and the product of classes computed on representatives (@fd3:thm-quotient-ring-by-ideal (b)). The polynomial has degree \( 3 \) and its derivative has degree \( 0 \): the degree dropped by \( 3 \), not by \( 1 \).

(v) \( (x^n)' = (n \cdot 1) x^{n-1} = n x^{n-1} \), since in \( \nZ \) the multiple \( n \cdot 1 \) is the integer \( n \) (the "Multiples" paragraph cited above).

(vi) Apply (M) three times, with the rule \( m \cdot (j \cdot 1) = (mj) \cdot 1 \) of @lem-finite-sums-and-powers (d). Over any commutative ring,
\[
(x^4)' = (4 \cdot 1) x^3 , \qquad (x^4)'' = \bigl( 3 \cdot (4 \cdot 1) \bigr) x^2 = (12 \cdot 1) x^2 , \qquad (x^4)''' = \bigl( 2 \cdot (12 \cdot 1) \bigr) x = (24 \cdot 1) x .
\]
Over \( \nQ \), as in (i), these are \( 4x^3 \), \( 12x^2 \) and \( 24x \). Over \( \nF_3 \), \( 3 \cdot 1 = 0 \), so \( 4 \cdot 1 = 3 \cdot 1 + 1 \cdot 1 = 1 \) and \( 12 \cdot 1 = 4 \cdot (3 \cdot 1) = 4 \cdot 0 = 0 \), by @lem-finite-sums-and-powers (d) and \( m \cdot 0 = 0 \). So \( (x^4)' = x^3 \), but already \( (x^4)'' = 0 \), and then \( (x^4)''' = 0' = 0 \) by (M).
:::

Examples (iii) and (iv) are the new phenomena. Over \( \nF_2 \) a non-constant polynomial has derivative \( 0 \); over \( \nZ/6\nZ \) the coefficient of \( x^2 \) in the derivative, \( 3 \cdot [2] \), is \( [0] \) although neither \( 3 \cdot [1] = [3] \) nor \( [2] \) is. Both come from the element \( n \cdot 1 \) above.

::: {.check}
Compute \( (x^3 + x^2 + x + 1)' \) over \( \nF_2 \).
:::

::: {.solution}
\( (3 \cdot 1) x^2 + (2 \cdot 1) x + 1 = x^2 + 1 \), since \( 3 \cdot 1 = 1 + 1 + 1 = 1 \) and \( 2 \cdot 1 = 0 \) in \( \nF_2 \).
:::

## The rules of differentiation

Calculus proves the sum, product and power rules with limits. Here they must come from the coefficients. The sum rule is one line per coefficient. The product rule is where a direct attack hurts: the \( k \)-th coefficient of \( (fg)' \) is \( (k + 1) \cdot \sum_{i=0}^{k+1} f_i g_{k+1-i} \), and matching it with \( f'g + fg' \) means splitting each term between two sums with shifted indices. The move of Section 3.2, **check on monomials, extend by additivity**, avoids that: both sides of the product rule are additive in \( f \) and in \( g \), so it is enough to compare them on monomials, where (M) does the work.

::: {#thm-formal-derivative-rules}
[Rules for the Formal Derivative]

Let \( R \) be a commutative ring, \( f, g \in R[x] \), \( a, c \in R \) and \( m \in \nZ_{>0} \).

::: {.enumerate options="label=(\alph*)"}
1. (Linearity) \( (f + g)' = f' + g' \), and \( (af)' = a f' \) for the constant \( a \); moreover \( a' = 0 \).
2. (Product rule) \( (fg)' = f'g + fg' \).
3. (Power rule) \( (g^m)' = (m \cdot 1) \, g^{m-1} g' \). In particular \( \bigl( (x - c)^m \bigr)' = (m \cdot 1)(x - c)^{m-1} \).
:::
:::

::: {.idea}
① Linearity is one coefficient at a time: the multiple \( (k + 1) \cdot b \) is additive in \( b \) and commutes with multiplication by a constant. ② For the product rule, both \( (fg)' \) and \( f'g + fg' \) are additive in each argument, by ①; so @lem-check-on-monomials reduces the rule to \( f = a x^i \), \( g = b x^j \). There (M) and @lem-monomial-product (b) turn both sides into one monomial, and the coefficients agree because \( (i + j) \cdot (ab) = i \cdot (ab) + j \cdot (ab) \). ③ The power rule is the product rule applied \( m - 1 \) times, by induction.
:::

::: {.proof}
Equality of polynomials is equality of all coefficients (@def-polynomial), so it is enough to compare coefficients in (a); (b) and (c) are then built on (a).

(a) Let \( k \in \nN \). Since addition in \( R[x] \) is coefficientwise (@def-polynomial-ring),
\[
\begin{aligned}
\bigl( (f + g)' \bigr)_k &= (k + 1) \cdot (f_{k+1} + g_{k+1}) \\
&= (k + 1) \cdot f_{k+1} + (k + 1) \cdot g_{k+1} = (f' + g')_k ,
\end{aligned}
\]
where the second equality is the rule \( n \cdot (b + d) = n \cdot b + n \cdot d \) of @lem-finite-sums-and-powers (d). For the constant \( a \), \( (af)_{k+1} = a f_{k+1} \) by @thm-polynomial-ring-laws (d), so
\[
\begin{aligned}
\bigl( (af)' \bigr)_k &= (k + 1) \cdot (f_{k+1} a) \\
&= \bigl( (k + 1) \cdot f_{k+1} \bigr) a = a (f')_k = (a f')_k ,
\end{aligned}
\]
using (F6) of \( R \) in the first and third equalities, the rule \( (n \cdot b) d = n \cdot (bd) \) of @lem-finite-sums-and-powers (d) in the second, and @thm-polynomial-ring-laws (d) in the last. Finally \( a' = 0 \) is (M) with \( n = 0 \).

(b) Define \( \Phi, \Psi \colon R[x] \times R[x] \to R[x] \) by
\[
\Phi(f, g) \coloneqq (fg)' , \qquad \Psi(f, g) \coloneqq f'g + fg' .
\]
By @thm-polynomial-ring-laws (a), \( R[x] \) is a commutative ring, so (F1)–(F7), (F9) and @fd3:prp-ring-algebra hold in it.

*Additivity.* Let \( f, h, g \in R[x] \). By the distributive law (F9) of \( R[x] \) and (a),
\[
\Phi(f + h, g) = (fg + hg)' = (fg)' + (hg)' = \Phi(f, g) + \Phi(h, g) .
\]
By (a), (F9) and a regrouping of four terms by (F1) and (F2),
\[
\begin{aligned}
\Psi(f + h, g) &= (f' + h') g + (f + h) g' \\
&= (f'g + fg') + (h'g + hg') = \Psi(f, g) + \Psi(h, g) .
\end{aligned}
\]
Both maps are symmetric: \( \Phi(f, g) = \Phi(g, f) \) because \( fg = gf \), and \( \Psi(f, g) = \Psi(g, f) \) because \( f'g + fg' = gf' + g'f = g'f + gf' \), by (F6) and (F2) of \( R[x] \). So each is additive in its second argument as well.

*Monomials.* Let \( u = a x^i \) and \( v = b x^j \), with \( a, b \in R \) and \( i, j \in \nN \). By @lem-monomial-product (b), \( uv = (ab) x^{i+j} \).

*Case \( i \ge 1 \) and \( j \ge 1 \).* Then \( i + j \ge 1 \), and (M) gives
\[
\Phi(u, v) = \bigl( (i + j) \cdot (ab) \bigr) x^{i+j-1} .
\]
On the other side, (M) gives \( u' = (i \cdot a) x^{i-1} \) and \( v' = (j \cdot b) x^{j-1} \), and @lem-monomial-product (b), with \( (i - 1) + j = i + (j - 1) = i + j - 1 \) in \( \nN \), gives
\[
\Psi(u, v) = \bigl( (i \cdot a) b \bigr) x^{i+j-1} + \bigl( a (j \cdot b) \bigr) x^{i+j-1} .
\]
Now \( (i \cdot a) b = i \cdot (ab) \), and \( a (j \cdot b) = (j \cdot b) a = j \cdot (ba) = j \cdot (ab) \), by @lem-finite-sums-and-powers (d) and (F6) of \( R \). Two monomials in the same position add coefficientwise (@def-polynomial-ring), and \( i \cdot (ab) + j \cdot (ab) = (i + j) \cdot (ab) \) (@lem-finite-sums-and-powers (d)). So \( \Psi(u, v) = \Phi(u, v) \).

*Case \( i = 0 \).* Then \( u = a \) is a constant, \( u' = 0 \) by (a), and \( uv = (ab) x^j \). So \( \Psi(u, v) = 0 \cdot v + a v' = a v' \), by @fd3:prp-ring-algebra (b) and (F3) of \( R[x] \). If \( j = 0 \), then \( v' = 0 \) and \( uv \) is a constant, so both sides are \( 0 \) (by (a) and @fd3:prp-ring-algebra (b)). If \( j \ge 1 \), then by (M) and @lem-monomial-product (b) with \( m = 0 \),
\[
a v' = \bigl( a (j \cdot b) \bigr) x^{j-1} = \bigl( j \cdot (ab) \bigr) x^{j-1} = \bigl( (ab) x^j \bigr)' = \Phi(u, v) ,
\]
where the middle step is the computation of the previous case.

*Case \( j = 0 \), \( i \ge 1 \).* By the symmetry of \( \Phi \) and \( \Psi \) this is the case \( i = 0 \) with \( u \) and \( v \) exchanged.

So \( \Phi \) and \( \Psi \) agree whenever both arguments are monomials, and both are additive in each argument. By @lem-check-on-monomials, with two arguments and \( T = R[x] \), \( \Phi = \Psi \). This is the product rule.

(c) First, \( (f - g)' = f' - g' \): by (a), \( (f - g)' + g' = \bigl( (f - g) + g \bigr)' = f' \), and adding \( -g' \) to both sides gives the claim, by (F2)–(F4) of \( R[x] \). We prove the power rule by induction on \( m \ge 1 \) (@fd1:ax-induction, with base \( 1 \)). For \( m = 1 \): \( g^0 = 1 \) (@lem-finite-sums-and-powers (c)) and \( 1 \cdot 1 = 1 \), so the right side is \( 1 \cdot 1 \cdot g' = g' \). Suppose \( (g^m)' = (m \cdot 1) g^{m-1} g' \) for some \( m \ge 1 \). Since \( g^{m+1} = g^m g \), the product rule (b) gives
\[
\begin{aligned}
(g^{m+1})' &= (g^m)' g + g^m g' = (m \cdot 1) g^{m-1} g' g + g^m g' \\
&= (m \cdot 1) g^m g' + 1 \cdot g^m g' = \bigl( (m + 1) \cdot 1 \bigr) g^m g' .
\end{aligned}
\]
The third equality uses (F5), (F6), \( g^{m-1} g = g^m \) (the power recursion, since \( (m - 1) + 1 = m \)) and (F7); the last uses (F9), the fact that constants add as in \( R \) (@thm-polynomial-ring-laws (b)), and the recursion \( (m + 1) \cdot 1 = m \cdot 1 + 1 \) of multiples. This completes the induction.

For the particular case, \( (x - c)' = x' - c' = 1 - 0 = 1 \), by the difference rule and @exm-formal-derivatives (ii). The power rule with \( g = x - c \) gives \( \bigl( (x - c)^m \bigr)' = (m \cdot 1)(x - c)^{m-1} \cdot 1 \), and \( \cdot \, 1 \) may be dropped by (F7). This proves the theorem.
:::

The theorem is the calculus toolkit with every limit removed, and it holds over every commutative ring. The power rule shows the element \( m \cdot 1 \) once more: the derivative of \( (x - c)^m \) is \( (x - c)^{m-1} \) times the constant \( m \cdot 1 \), and over \( \nF_p \) that constant is \( 0 \) for \( m = p \). So over \( \nF_p \) the polynomial \( (x - c)^p \) has derivative \( 0 \), although it is not constant; the next subsection says exactly when this happens.

::: {.remark}
Over \( \nQ \), and over the real numbers, \( f' \) is the derivative of the polynomial function \( c \mapsto f(c) \) in the sense of calculus. This book never uses the agreement, and nothing in it depends on it; it explains only why the formulas look familiar.
:::

::: {.check}
Over \( \nF_3 \), compute \( \bigl( (x + 1)^3 \bigr)' \) twice: by the power rule, and by expanding \( (x + 1)^3 \) first.
:::

::: {.solution}
By @thm-formal-derivative-rules (c), \( \bigl( (x + 1)^3 \bigr)' = (3 \cdot 1)(x + 1)^2 = 0 \), since \( 3 \cdot 1 = 0 \) in \( \nF_3 \). Expanding, \( (x + 1)^3 = x^3 + 3x^2 + 3x + 1 = x^3 + 1 \) in \( \nF_3[x] \), and \( (x^3 + 1)' = (3 \cdot 1) x^2 = 0 \). The two answers agree.
:::

## When the derivative vanishes

In calculus, a function with derivative \( 0 \) on an interval is constant. Over \( \nF_2 \) the polynomial \( x^2 \) is not constant, yet \( (x^2)' = 0 \) (@exm-formal-derivatives (iii)). Which polynomials have derivative \( 0 \)? Over a field the answer depends only on the characteristic. Recall @def-characteristic: \( \operatorname{char} F \) is the least positive integer \( n \) with \( n \cdot 1 = 0 \) in \( F \), and \( 0 \) if there is none; by @thm-characteristic-prime it is \( 0 \) or a prime.

::: {#prp-formal-derivative-zero}
[When the Formal Derivative Is Zero]

Let \( F \) be a field (@def-field) and \( f \in F[x] \).

::: {.enumerate options="label=(\alph*)"}
1. If \( \operatorname{char} F = 0 \), then \( f' = 0 \) **if and only if** \( f \) is constant. Moreover, \( \deg f' = \deg f - 1 \) whenever \( \deg f \ge 1 \).
2. If \( \operatorname{char} F = p > 0 \), then \( p \) is prime, and the following are equivalent: (i) \( f' = 0 \); (ii) \( f_k = 0 \) for every \( k \in \nN \) **not** divisible by \( p \); (iii) \( f = g \circ x^p \) for some \( g \in F[x] \) (@def-polynomial-composition).
:::
:::

::: {.idea}
Everything rests on one identity: for \( k \ge 1 \), the coefficient of \( x^{k-1} \) in \( f' \) is \( k \cdot f_k = (k \cdot 1) f_k \). In a field a product is \( 0 \) only when a factor is. So \( f' = 0 \) forces \( f_k = 0 \) exactly at the \( k \) with \( k \cdot 1 \ne 0 \): in characteristic \( 0 \) that is every \( k \ge 1 \), and in characteristic \( p \) it is every \( k \) not divisible by \( p \). A polynomial whose only non-zero coefficients sit at multiples of \( p \) is a polynomial in \( x^p \).
:::

::: {.proof}
For every \( k \ge 1 \), @def-formal-derivative at the index \( k - 1 \) and @lem-finite-sums-and-powers (d) give
\[
(f')_{k-1} = k \cdot f_k = (k \cdot 1) f_k . \tag{$\ast$}
\]
As \( k \) runs through the integers \( \ge 1 \), the index \( k - 1 \) runs through \( \nN \), so \( f' = 0 \) **if and only if** \( (k \cdot 1) f_k = 0 \) for every \( k \ge 1 \).

(a) Let \( \operatorname{char} F = 0 \). Then \( k \cdot 1 \ne 0 \) for every \( k \ge 1 \), by @def-characteristic. Suppose \( f' = 0 \), and let \( k \ge 1 \). By \( (\ast) \), \( (k \cdot 1) f_k = 0 \) with \( k \cdot 1 \ne 0 \), so \( f_k = 0 \) by @thm-field-basic-properties (f). Thus \( f \) and the constant \( f_0 \) agree in every position, and \( f = f_0 \) (@def-polynomial). Conversely, a constant has derivative \( 0 \) by @thm-formal-derivative-rules (a).

Now let \( n \coloneqq \deg f \ge 1 \), so that \( f_n \ne 0 \) and \( f_k = 0 \) for every \( k > n \) (@def-degree). By \( (\ast) \), \( (f')_{n-1} = (n \cdot 1) f_n \), a product of two non-zero elements of \( F \), which is non-zero by @thm-field-basic-properties (f). For \( k \ge n \), \( (f')_k = (k + 1) \cdot f_{k+1} = (k + 1) \cdot 0 = 0 \), as in the well-definedness paragraph after @def-formal-derivative. So \( n - 1 \) is the largest index of a non-zero coefficient of \( f' \): \( \deg f' = n - 1 \).

(b) Let \( \operatorname{char} F = p > 0 \). Then \( p \) is prime by @thm-characteristic-prime.

By @prp-characteristic-divides (a), with \( c = p \): for \( k \in \nN \), \( k \cdot 1 = 0 \) **if and only if** \( p \mid k \).

\( \text{(i)} \Rightarrow \text{(ii)} \). Let \( f' = 0 \) and let \( k \in \nN \) with \( p \nmid k \). Then \( k \ne 0 \), since \( p \mid 0 \); so \( k \ge 1 \), and \( (k \cdot 1) f_k = 0 \) by \( (\ast) \). By @prp-characteristic-divides (a), \( k \cdot 1 \ne 0 \), so \( f_k = 0 \) by @thm-field-basic-properties (f).

\( \text{(ii)} \Rightarrow \text{(i)} \). Let \( k \ge 1 \). If \( p \nmid k \), then \( f_k = 0 \) by (ii); if \( p \mid k \), then \( k \cdot 1 = 0 \) by @prp-characteristic-divides (a). Either way \( (k \cdot 1) f_k = 0 \) (@fd3:prp-ring-algebra (b)), so \( f' = 0 \) by \( (\ast) \).

\( \text{(ii)} \Rightarrow \text{(iii)} \). Choose \( N \in \nN \) with \( f_k = 0 \) for every \( k > N \), and define \( g \colon \nN \to F \) by \( g_j \coloneqq f_{pj} \). For \( j > N \) we have \( pj \ge j > N \), so \( g_j = 0 \), and \( g \in F[x] \). By @def-polynomial-composition, then the power law \( (x^p)^j = x^{pj} \) in the commutative ring \( F[x] \) (@lem-finite-sums-and-powers (c)) and @thm-polynomial-ring-laws (c),
\[
g \circ x^p = \sum_{j=0}^{N} g_j \, (x^p)^j = \sum_{j=0}^{N} f_{pj} \, x^{pj} .
\]
We compare the coefficients of both sides with those of \( f \) at an index \( k \in \nN \). Addition in \( F[x] \) is coefficientwise (@def-polynomial-ring), so the \( k \)-th coefficient of a finite sum of polynomials is the finite sum of their \( k \)-th coefficients (induction on the number of terms, through the sum recursion of @lem-finite-sums-and-powers (a)). The monomial \( f_{pj} x^{pj} \) has \( k \)-th coefficient \( f_k \) if \( pj = k \), and \( 0 \) otherwise.

- If \( p \nmid k \), no \( j \) has \( pj = k \), so every term is \( 0 \) at \( k \), and \( f_k = 0 \) by (ii).
- If \( p \mid k \), then \( k = pj_0 \) for some \( j_0 \in \nZ \), and \( j_0 \ge 0 \): if \( j_0 < 0 \), then \( pj_0 < 0 \cdot p = 0 \) by @fd3:prp-ordered-ring-rules (c), since \( p > 0 \), against \( k \ge 0 \). This \( j_0 \) is unique (if \( pj = pj' \), then \( j = j' \) by @fd3:prp-ordered-ring-rules (f), since \( p \ne 0 \)). If \( j_0 \le N \), the sum of the \( k \)-th coefficients has the single possibly non-zero term \( f_{pj_0} = f_k \), so it equals \( f_k \) by (Σ3) of @lem-finite-sums-and-powers (b). If \( j_0 > N \), every term is \( 0 \) at \( k \), and \( f_k = 0 \) because \( k = pj_0 \ge j_0 > N \).

In every case the \( k \)-th coefficients agree, so \( g \circ x^p = f \).

\( \text{(iii)} \Rightarrow \text{(ii)} \). Let \( f = g \circ x^p \), and choose \( N \) with \( g_j = 0 \) for \( j > N \). The computation above gives \( f = \sum_{j=0}^{N} g_j \, x^{pj} \), and by the first bullet, the coefficient of this sum at any \( k \) with \( p \nmid k \) is \( 0 \). This proves the proposition.
:::

So in characteristic \( p \) the polynomials with derivative \( 0 \) are exactly the polynomials in \( x^p \). Over \( \nF_2 \), \( x^2 + 1 = (x + 1) \circ x^2 \); over \( \nF_3 \), \( x^6 + 2x^3 + 1 = (x^2 + 2x + 1) \circ x^3 \), and indeed its derivative is \( (6 \cdot 1) x^5 + (6 \cdot 1) x^2 = 0 \), since \( 6 \cdot 1 = 0 \) in \( \nF_3 \). Part (a) is the case where the school statement survives, and its proof spends the hypothesis at exactly one place: \( k \cdot 1 \ne 0 \).

::: {.warning}
"\( f' = 0 \) means \( f \) is constant" and "differentiating lowers the degree by one" both fail in characteristic \( p \). Over \( \nF_p \), \( (x^p)' = (p \cdot 1) x^{p-1} = 0 \), although \( x^p \) has degree \( p \); and \( (x^p - x)' = (p \cdot 1) x^{p-1} - 1 = -1 \) has degree \( 0 \), not \( p - 1 \). Tests for repeated roots that use the derivative must therefore say which characteristic they assume. Chapter 4 concludes from \( (x^p - x)' = -1 \) that \( x^p - x \) has no repeated roots in \( \nF_p \).
:::

::: {.check}
Compute \( (x^5 + x)' \) over \( \nF_5 \).
:::

::: {.solution}
\( (x^5 + x)' = (5 \cdot 1) x^4 + 1 = 1 \), since \( 5 \cdot 1 = 0 \) in \( \nF_5 \).
:::

## Exercises

### A. Check your understanding

::: {#exr-formal-derivative-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Compute \( (x^5 - x)' \) over \( \nQ \) and over \( \nF_5 \).
2. True or false: if \( f' = 0 \), then \( f \) is constant. Answer over \( \nQ \) and over \( \nF_2 \), with a reason or a witness.
3. Let \( f \in (\nZ/6\nZ)[x] \) have degree \( 3 \) and leading coefficient \( [2] \). What can \( \deg f' \) be? Give a witness for each possibility.
4. In the proof of the product rule (@thm-formal-derivative-rules (b)), why is the case \( i = 0 \) treated separately?
:::
:::

::: {.solution}
(a) Over \( \nQ \): \( (x^5 - x)' = 5x^4 - 1 \), by (M), with \( 5 \cdot 1 = 5 \). Over \( \nF_5 \): \( (x^5 - x)' = (5 \cdot 1) x^4 - 1 = -1 \), since \( 5 \cdot 1 = 0 \) in \( \nF_5 \); in the elements \( 0, \dots, 4 \) of \( \nF_5 \), \( -1 = 4 \).

(b) Over \( \nQ \): **true**. \( \nQ \) is a field (@fd3:thm-rationals-field) of characteristic \( 0 \) (@exm-characteristics); so @prp-formal-derivative-zero (a) applies. Over \( \nF_2 \): **false**. The witness is \( x^2 \), which is not constant, with \( (x^2)' = (2 \cdot 1) x = 0 \) (@exm-formal-derivatives (iii)).

(c) \( \deg f' \in \{ 1, 0, -\infty \} \), and each occurs. Write \( f = [2] x^3 + f_2 x^2 + f_1 x + f_0 \). Then
\[
f' = (3 \cdot [2]) x^2 + (2 \cdot f_2) x + f_1 = (2 \cdot f_2) x + f_1 ,
\]
since \( 3 \cdot [2] = [6] = [0] \). So \( \deg f' \le 1 \) (@def-degree). Witnesses: \( [2]x^3 + x^2 \) has derivative \( [2] x \), of degree \( 1 \); \( [2]x^3 + x \) has derivative \( 1 \), of degree \( 0 \); \( [2]x^3 \) has derivative \( 0 \), of degree \( -\infty \). The school rule "degree drops by one" fails because \( 3 \cdot [2] = [0] \): the leading coefficient of \( f' \) would be \( (3 \cdot 1) \operatorname{lc}(f) \), and here that product is \( 0 \).

(d) For \( i = 0 \) the monomial \( u = a x^0 \) is a constant, and (M) gives \( u' = 0 \), not \( (0 \cdot a) x^{-1} \): the exponent \( i - 1 = -1 \) is not in \( \nN \), so \( x^{i-1} \) has no meaning. The general computation, which writes \( u' = (i \cdot a) x^{i-1} \), therefore cannot be used, and the case is checked directly.
:::

### B. Practice

::: {#exr-formal-derivative-b1}
[B1: The chain rule]

Let \( R \) be a commutative ring and \( f, g \in R[x] \). Prove that
\[
(f \circ g)' = (f' \circ g) \, g' .
\]
Check the formula on \( f = x^2 \), \( g = x^2 + 1 \) over \( \nZ \).
:::

::: {.solution}
Fix \( g \), and define \( \Phi, \Psi \colon R[x] \to R[x] \) by
\[
\Phi(f) \coloneqq (f \circ g)' , \qquad \Psi(f) \coloneqq (f' \circ g) \, g' .
\]
The move is the one of the product rule: check on monomials, extend by additivity.

*Additivity.* By @def-polynomial-composition and @thm-polynomial-substitution (a), \( u \mapsto u \circ g \) is a ring homomorphism \( R[x] \to R[x] \) that fixes the constants and sends \( x \) to \( g \); in particular \( (f + h) \circ g = f \circ g + h \circ g \). With @thm-formal-derivative-rules (a),
\[
\Phi(f + h) = (f \circ g + h \circ g)' = \Phi(f) + \Phi(h) ,
\]
and, using also (F9) of \( R[x] \),
\[
\Psi(f + h) = (f' \circ g + h' \circ g) \, g' = \Psi(f) + \Psi(h) .
\]

*Monomials.* Let \( f = a x^n \) with \( a \in R \), \( n \in \nN \). By @thm-polynomial-ring-laws (c), \( a x^n \) is the product of the constant \( a \) and the \( n \)-th power of \( x \); a ring homomorphism preserves products and powers (@def-ring-homomorphism), so \( (a x^n) \circ g = a g^n \).

If \( n = 0 \), then \( f = a \) and \( f \circ g = a \), so \( \Phi(f) = 0 \) by @thm-formal-derivative-rules (a). Also \( f' = 0 \), and \( 0 \circ g = 0 \) because a ring homomorphism sends \( 0 \) to \( 0 \) (@def-ring-homomorphism); so \( \Psi(f) = 0 \cdot g' = 0 \).

If \( n \ge 1 \), then by @thm-formal-derivative-rules (a) and (c),
\[
\Phi(f) = (a g^n)' = a \, (g^n)' = a \, (n \cdot 1) \, g^{n-1} g' .
\]
On the other side \( f' = (n \cdot a) x^{n-1} \) by (M), so \( f' \circ g = (n \cdot a) g^{n-1} \) and \( \Psi(f) = (n \cdot a) g^{n-1} g' \). The constants agree: \( a (n \cdot 1) = (n \cdot 1) a = n \cdot a \), by (F6) and @lem-finite-sums-and-powers (d), and constants multiply as in \( R \) (@thm-polynomial-ring-laws (b)). So \( \Phi(f) = \Psi(f) \).

By @lem-check-on-monomials with one argument and \( T = R[x] \), \( \Phi = \Psi \), which is the chain rule.

*Check.* Over \( \nZ \), \( f \circ g = (x^2 + 1)^2 = x^4 + 2x^2 + 1 \), whose derivative is \( 4x^3 + 4x \). On the other side, \( f' = 2x \), \( f' \circ g = 2(x^2 + 1) \) and \( g' = 2x \), so \( (f' \circ g) g' = 4x^3 + 4x \).
:::

::: {#exr-formal-derivative-b2}
[B2: Higher derivatives]

For \( n, k \in \nN \) write \( P(n, k) \) for the product \( n(n - 1) \cdots (n - k + 1) \) of \( k \) factors, defined by \( P(n, 0) \coloneqq 1 \) and \( P(n, k + 1) \coloneqq P(n, k) \, (n - k) \); it is a natural number for \( k \le n \).

::: {.enumerate options="label=(\alph*)"}
1. Let \( R \) be a commutative ring. Show that \( (x^n)^{(k)} = \bigl( P(n, k) \cdot 1 \bigr) x^{n-k} \) for \( k \le n \), and \( (x^n)^{(k)} = 0 \) for \( k > n \).
2. Let \( p \) be a prime. Show that \( f^{(p)} = 0 \) for every \( f \in \nF_p[x] \).
:::
:::

::: {.solution}
(a) Induction on \( k \le n \). For \( k = 0 \), \( (x^n)^{(0)} = x^n = (1 \cdot 1) x^n \). Let \( k < n \) and suppose \( (x^n)^{(k)} = (P(n, k) \cdot 1) x^{n-k} \). Since \( n - k \ge 1 \), (M) gives
\[
\begin{aligned}
(x^n)^{(k+1)} &= \bigl( (n - k) \cdot (P(n, k) \cdot 1) \bigr) x^{n-k-1} \\
&= \bigl( P(n, k + 1) \cdot 1 \bigr) x^{n-(k+1)} ,
\end{aligned}
\]
by the rule \( m \cdot (j \cdot b) = (mj) \cdot b \) of @lem-finite-sums-and-powers (d) and \( (n - k) P(n, k) = P(n, k + 1) \) in \( \nN \). This proves the formula for \( k \le n \). At \( k = n \) the polynomial \( (x^n)^{(n)} \) is a constant, so \( (x^n)^{(n+1)} = 0 \) by (M), and the derivative of \( 0 \) is \( 0 \); by induction, \( (x^n)^{(k)} = 0 \) for every \( k > n \).

(b) *The coefficients of \( f^{(k)} \).* Let \( R \) be any commutative ring and \( f \in R[x] \). We show by induction on \( k \) that
\[
\bigl( f^{(k)} \bigr)_j = P(j + k, k) \cdot f_{j+k} \qquad \text{for every } j \in \nN .
\]
For \( k = 0 \) both sides are \( f_j \). If it holds for \( k \), then by @def-formal-derivative and @lem-finite-sums-and-powers (d),
\[
\begin{aligned}
\bigl( f^{(k+1)} \bigr)_j &= (j + 1) \cdot \bigl( P(j + k + 1, k) \cdot f_{j+k+1} \bigr) \\
&= \bigl( P(j + k + 1, k)(j + 1) \bigr) \cdot f_{j+k+1} = P(j + k + 1, k + 1) \cdot f_{j+k+1} ,
\end{aligned}
\]
since the factor added by the recursion is \( (j + k + 1) - k = j + 1 \).

*The case \( k = p \) over \( \nF_p \).* The number \( P(j + p, p) = (j + p)(j + p - 1) \cdots (j + 1) \) is a product of the \( p \) consecutive integers \( j + 1, \dots, j + p \). Divide \( j = qp + r \) with \( 0 \le r < p \) (@fd3:thm-integers-division-remainder); then \( j + (p - r) = (q + 1)p \), and \( 1 \le p - r \le p \), so one of the factors is divisible by \( p \). A product with a factor divisible by \( p \) is divisible by \( p \) (@fd3:prp-divisibility-rules-integers (c), one factor at a time). So \( P(j + p, p) = Mp \) with \( M \in \nZ \), and
\[
P(j + p, p) \cdot f_{j+p} = M \cdot \bigl( p \cdot f_{j+p} \bigr) = M \cdot \bigl( (p \cdot 1) f_{j+p} \bigr) = M \cdot 0 = 0 ,
\]
by @lem-finite-sums-and-powers (d), which allows integer multiples, \( p \cdot 1 = 0 \) in \( \nF_p \) (@fd3:thm-integers-mod-n-ring (d)), @fd3:prp-ring-algebra (b) and \( M \cdot 0 = 0 \). So every coefficient of \( f^{(p)} \) is \( 0 \). For instance, over \( \nF_3 \), \( (x^4)''' = (P(4, 3) \cdot 1) x = (24 \cdot 1) x = 0 \).
:::

### C. Going deeper

::: {#exr-formal-derivative-c1}
[C1: Derivations]

Let \( R \) be a commutative ring, and let \( \delta \colon R[x] \to R[x] \) be a map such that, for all \( f, g \in R[x] \) and every constant \( a \),
\[
\delta(f + g) = \delta(f) + \delta(g) , \qquad \delta(a) = 0 , \qquad \delta(fg) = \delta(f) g + f \delta(g) .
\]
Prove that \( \delta(f) = f' \, \delta(x) \) for every \( f \in R[x] \). Deduce that \( f \mapsto f' \) is the only such map with \( \delta(x) = 1 \).
:::

::: {.solution}
*Both sides are additive in \( f \).* \( \delta \) is additive by hypothesis, and \( f \mapsto f' \delta(x) \) is additive by @thm-formal-derivative-rules (a) and (F9) of \( R[x] \) (@thm-polynomial-ring-laws (a)).

*Powers of \( x \).* We show \( \delta(x^n) = (n \cdot 1) x^{n-1} \delta(x) \) for every \( n \ge 1 \), by induction. For \( n = 1 \), \( (1 \cdot 1) x^0 \delta(x) = \delta(x) \). If it holds for \( n \), then, since \( x^{n+1} = x^n x \),
\[
\begin{aligned}
\delta(x^{n+1}) &= \delta(x^n) x + x^n \delta(x) = (n \cdot 1) x^{n-1} \delta(x) \, x + x^n \delta(x) \\
&= \bigl( n \cdot 1 + 1 \bigr) x^n \delta(x) = \bigl( (n + 1) \cdot 1 \bigr) x^n \delta(x) ,
\end{aligned}
\]
by (F5), (F6), (F7), (F9) of \( R[x] \), \( x^{n-1} x = x^n \), and the recursion of multiples. Also \( \delta(x^0) = \delta(1) = 0 \), since \( 1 \) is a constant.

*Monomials.* Let \( a \in R \) and \( n \in \nN \). By @thm-polynomial-ring-laws (c), \( a x^n \) is the product of the constant \( a \) and \( x^n \), so
\[
\delta(a x^n) = \delta(a) x^n + a \, \delta(x^n) = a \, \delta(x^n) .
\]
If \( n = 0 \), this is \( 0 = (a x^0)' \delta(x) \), by (M). If \( n \ge 1 \), it is \( a (n \cdot 1) x^{n-1} \delta(x) = (n \cdot a) x^{n-1} \delta(x) = (a x^n)' \delta(x) \), by (F6), @lem-finite-sums-and-powers (d) and (M).

*Conclusion.* The two additive maps \( \delta \) and \( f \mapsto f' \delta(x) \) agree on every monomial, so they are equal by @lem-check-on-monomials (one argument, \( T = R[x] \)).

*Uniqueness.* The formal derivative satisfies the three conditions, by @thm-formal-derivative-rules (a) and (b), and \( x' = 1 \) (@exm-formal-derivatives (ii)). If \( \delta \) satisfies them with \( \delta(x) = 1 \), then \( \delta(f) = f' \cdot 1 = f' \) for every \( f \).

**Marking scheme.** (10 points)
- 2: both sides additive in \( f \), with the additivity of \( f \mapsto f' \delta(x) \) justified.
- 2: \( \delta(a x^n) = a \, \delta(x^n) \) from the product condition and \( \delta(a) = 0 \).
- 3: \( \delta(x^n) = (n \cdot 1) x^{n-1} \delta(x) \) by induction, with the case \( n = 0 \) handled separately.
- 2: comparison with \( (a x^n)' \), using \( a (n \cdot 1) = n \cdot a \).
- 1: conclusion by extending from monomials, and the uniqueness statement.

A solution that shows instead that \( K \coloneqq \{ f \in R[x] : \delta(f) = f' \delta(x) \} \) is all of \( R[x] \) is marked on the same points: closure of \( K \) under \( + \) earns the first 2; the constants and \( x \) in \( K \) earn the next 2; closure of \( K \) under products, by @thm-formal-derivative-rules (b), earns the 3; \( K = R[x] \) earns the 2; the uniqueness statement earns the last 1.

Fatal errors (0 for the step): checking only on \( x^n \), with no account of the coefficient \( a \) (that is where \( \delta(a) = 0 \) is needed); writing \( x^{-1} \) in the case \( n = 0 \).
:::

::: {#exr-formal-derivative-c2}
[C2: Find the error]

Here is an argument.

> **Claim.** If \( f \in \nQ[x] \) and \( f' = 0 \), then \( f \) is constant.
>
> **Proof.** (1) For \( k \ge 1 \), the coefficient of \( x^{k-1} \) in \( f' \) is \( k \cdot f_k = (k \cdot 1) f_k \), by the definition of \( f' \) and the rules for multiples. (2) Since \( f' = 0 \), \( (k \cdot 1) f_k = 0 \) for every \( k \ge 1 \). (3) For \( k \ge 1 \) we have \( k \ne 0 \), so \( k \cdot 1 \ne 0 \); since \( \nQ \) has no zero divisors, \( f_k = 0 \) for every \( k \ge 1 \). (4) So \( f = f_0 x^0 \) is constant.

Is the claim true? Does the argument prove it? Name the line that fails and the reason, give a counterexample to the illegal step, and repair the argument.
:::

::: {.solution}
**The claim is true:** it is @prp-formal-derivative-zero (a) for \( F = \nQ \). **The argument, as written, does not prove it.**

Lines (1), (2) and (4) are correct: (1) is @def-formal-derivative with @lem-finite-sums-and-powers (d), (2) reads \( f' = 0 \) coefficient by coefficient, and (4) compares coefficients (@def-polynomial). The second half of line (3) is correct too: \( \nQ \) is a field (@fd3:thm-rationals-field), so it has no zero divisors (@thm-field-basic-properties (f)).

*Line (3) fails, in its first half.* "\( k \ne 0 \) in \( \nZ \), so \( k \cdot 1 \ne 0 \) in the ring" is a general "fact" that is neither proved nor true, and the line uses nothing about \( \nQ \) to support it: entry (N9) of @fd1:exm-not-allowed-catalogue. *Counterexample to the step:* in \( \nF_2 \), \( k = 2 \) gives \( 2 \cdot 1 = 1 + 1 = 0 \). The same four lines, read over \( \nF_2 \), would "prove" that \( x^2 \) is constant, since \( (x^2)' = 0 \) (@exm-formal-derivatives (iii)). There is no counterexample to the conclusion, which is true.

*Repair.* What line (3) needs is that \( \nQ \) has characteristic \( 0 \) (@def-characteristic): for \( k \ge 1 \), \( k \cdot 1 \) is the rational number \( k \) (induction on \( k \), since the embeddings \( \nN \subseteq \nZ \subseteq \nQ \) preserve sums and \( 1 \), @fd3:prp-naturals-embed-integers and @fd3:prp-integers-embed-rationals), and \( k \ne 0 \). With that sentence in place of "so", the argument is the proof of @prp-formal-derivative-zero (a), whose hypothesis is exactly the characteristic.

**Marking scheme.** (10 points)
- 2: says the claim is true and that the argument, as written, does not prove it.
- 3: names the first half of line (3) and the reason: \( k \ne 0 \) does not give \( k \cdot 1 \ne 0 \) in a general ring, (N9), or an equivalent statement.
- 2: a counterexample to the step, such as \( 2 \cdot 1 = 0 \) in \( \nF_2 \), or the "proof" that \( x^2 \) is constant over \( \nF_2 \).
- 3: repairs the step by proving \( k \cdot 1 \ne 0 \) in \( \nQ \) for every \( k \ge 1 \), that is, \( \operatorname{char} \nQ = 0 \). Two routes earn full marks: \( k \cdot 1 = k \) via the embeddings, as in the solution; or \( k \cdot 1 > 0 \) by @fd3:prp-ordered-ring-rules (h), since \( \nQ \) is an ordered field (@fd3:thm-rationals-ordered-field) with \( 1 \ne 0 \).
Fatal errors (0 for the step): a counterexample to the conclusion (there is none); blaming the no-zero-divisors half of line (3), which is correct.
:::

### R. Review

::: {#exr-formal-derivative-r1}
[R1]

Let \( R \) be a commutative ring and \( E \colon R[x] \to R[x] \), \( E(f) \coloneqq f + f' \). Show that \( E \) is an injective homomorphism of the group \( (R[x], +) \) to itself. If \( 1 \ne 0 \) in \( R \), show that \( E(fg) = E(f) E(g) \) fails for some \( f, g \).
:::

::: {.solution}
The tools are the notion of a group homomorphism and its kernel, @def-group-homomorphism, written additively (@def-group), and @prp-homomorphism-injective-iff-kernel-trivial.

*The group.* By @thm-polynomial-ring-laws (a), \( R[x] \) satisfies (F1)–(F4), so \( (R[x], +) \) is an abelian group, with identity the zero polynomial and inverse \( -f \).

*A homomorphism.* By @thm-formal-derivative-rules (a) and (F1), (F2) of \( R[x] \),
\[
E(f + g) = (f + g) + (f' + g') = (f + f') + (g + g') = E(f) + E(g) ,
\]
which is the homomorphism condition in additive notation.

*The kernel is \( \{0\} \).* Let \( f \ne 0 \), with \( n \coloneqq \deg f \), so \( f_n \ne 0 \) and \( f_{n+1} = 0 \) (@def-degree). By @def-formal-derivative, \( (f')_n = (n + 1) \cdot f_{n+1} = (n + 1) \cdot 0 = 0 \), as in the well-definedness paragraph after it. Addition is coefficientwise (@def-polynomial-ring), so \( E(f)_n = f_n + 0 = f_n \ne 0 \), and \( E(f) \ne 0 \). Also \( 0 = 0 x^0 \), so \( 0' = 0 \) by (M), and \( E(0) = 0 + 0 = 0 \) by (F3) of \( R[x] \). So \( \ker E = \{0\} \), and \( E \) is injective by @prp-homomorphism-injective-iff-kernel-trivial.

*Not multiplicative.* Take \( f = g = x \). By @exm-formal-derivatives (ii), \( x' = 1 \), so \( E(x) = x + 1 \), and \( E(x) E(x) = (x + 1)^2 = x^2 + 2x + 1 \) by @fd3:prp-ring-algebra (d). On the other side, (M) gives \( (x^2)' = (2 \cdot 1) x = 2x \), so \( E(x^2) = x^2 + 2x \). The two differ in position \( 0 \), where they have \( 1 \) and \( 0 \); since \( 1 \ne 0 \), \( E(x \cdot x) \ne E(x) E(x) \). So only the group structure of \( R[x] \) is respected, and \( E \) is not a ring homomorphism.
:::

::: {#exr-formal-derivative-r2}
[R2]

For \( f \in \nR[x] \) and \( z \in \nC \), let \( f(z) \) denote the value obtained by substituting \( z \) for \( x \), where a real coefficient \( a \) is read as the complex number \( a \). Show that \( f(\conj{z}) = \conj{f(z)} \). Deduce that if \( z_0 \in \nC \) is a root of \( f \) that is not real, then \( \conj{z_0} \) is a different root of \( f \).
:::

::: {.solution}
The tool is the uniqueness in @thm-polynomial-substitution (b), applied to the field \( \nC \) of *Analytic Preliminaries*, Chapter 1.

*The setting.* \( \nC \) is a field, and \( \nR \subseteq \nC \) is closed under its operations (@fd4:thm-complex-numbers-field); so \( \nC \) and \( \nR \) are commutative rings and \( \nR[x] \) is defined. Let \( \iota \colon \nR \to \nC \) be the map of @fd4:prp-reals-embed-complex; it preserves \( + \), \( \cdot \) and \( 1 \), so it is a ring homomorphism (@def-ring-homomorphism). For \( s \in \nC \), let \( \Phi_s \colon \nR[x] \to \nC \) be the homomorphism of @thm-polynomial-substitution with \( \varphi = \iota \) and this \( s \); then \( f(z) \) means \( \Phi_z(f) \).

*Conjugation is a ring homomorphism.* By @fd4:thm-conjugate-properties (a) and (b), \( \conj{u + v} = \conj{u} + \conj{v} \) and \( \conj{uv} = \conj{u} \, \conj{v} \), and \( \conj{1} = 1 \), since \( 1 = 1 + 0i \) and \( \conj{1} = 1 - 0i = 1 \) (@fd4:def-conjugate-modulus).

*Two homomorphisms.* Let \( A(f) \coloneqq \conj{\Phi_z(f)} \) and \( B(f) \coloneqq \Phi_{\conj{z}}(f) \). Then \( A \) is a composite of ring homomorphisms, hence one (@def-ring-homomorphism), and \( B \) is one by @thm-polynomial-substitution (a). On a constant \( a \in \nR \), \( A(a) = \conj{\iota(a)} = \iota(a) \), since \( a = a + 0i \) has conjugate \( a - 0i = a \); and \( B(a) = \iota(a) \). On \( x \), \( A(x) = \conj{z} = B(x) \). By the uniqueness in @thm-polynomial-substitution (b), \( A = B \): \( \conj{f(z)} = f(\conj{z}) \) for every \( f \in \nR[x] \).

*Roots.* If \( f(z_0) = 0 \), then \( f(\conj{z_0}) = \conj{0} = 0 \). If \( z_0 = a + bi \) is not real, then \( b \ne 0 \), so \( \conj{z_0} = a - bi \ne a + bi \): equality would give \( -b = b \) by comparing imaginary parts (@fd4:def-complex-numbers), so \( 2b = 0 \), and \( b = 0 \) because \( 2 = 2 \cdot 1 \ne 0 \) in the ordered field \( \nR \) (@fd3:prp-ordered-ring-rules (h)) and \( \nR \) has no zero divisors (@fd3:prp-ordered-ring-rules (f)). So the non-real roots of a real polynomial come in pairs \( z_0 \ne \conj{z_0} \).

The identity and the first deduction are the statement of @fd4:prp-real-coefficients-conjugate-roots, and the distinctness of \( \conj{z_0} \) is the paragraph after it; *Analytic Preliminaries*, Chapter 1 proved both by a direct computation with the sum \( \sum_k a_k z^k \). Here the computation is replaced by the uniqueness of a substitution homomorphism. Polynomials with rational coefficients are a special case, since \( \nQ \) sits inside \( \nR \).
:::

::: {#exr-formal-derivative-r3}
[R3]

Show that \( \nZ[x] \) and \( \nF_2[x] \) are countable, and that the set of all sequences \( \nN \to \nF_2 \) is uncountable. Which clause of the definition of a polynomial does the difference rest on?
:::

::: {.solution}
The tools are the countability results of *Sets, Relations, and Cardinality*, Chapter 3, read on \( \nN = \omega \) through @fd3:cor-omega-identification.

*\( \nZ \) and \( \nF_2 \) are countable.* \( \nN \times \nN \) is countable (@fd2:thm-product-countable). The class map \( \nN \times \nN \to \nZ = (\nN \times \nN)/{\sim} \) is surjective (@fd2:def-quotient-set), so \( \nZ \) is countable by @fd2:prp-countable-image; this is the count of @fd3:exr-gaps-in-the-rationals-r2. The map \( \nN \to \nF_2 \), \( n \mapsto [n] \), is surjective, since every class is \( [0] \) or \( [1] \) (@fd3:thm-integers-mod-n-ring (b)); so \( \nF_2 \) is countable (@fd2:def-countable).

*Polynomials of bounded length.* Let \( R \) be \( \nZ \) or \( \nF_2 \), and for \( N \in \nN \) let \( A_N \coloneqq \{ f \in R[x] : f_k = 0 \text{ for every } k > N \} \). By @exr-polynomials-as-sequences-b1, \( A_N \) is in bijection with \( R^{N+1} \). For \( N \ge 1 \), \( R^{N+1} \) is countable by @fd2:cor-product-countable (b); for \( N = 0 \) it is \( R \) itself. So each \( A_N \) is countable, as the image of a countable set under a bijection (@fd2:prp-countable-image).

*The union.* Every polynomial lies in some \( A_N \) (@def-polynomial), so \( R[x] = \bigcup_{N \in \nN} A_N \), a countable union of countable sets, which is countable by @fd2:thm-countable-union (a). (That theorem uses the axiom of countable choice to pick a list of each \( A_N \).)

*All sequences.* The set \( \{0, 1\}^{\nN} \) is uncountable (@fd2:thm-binary-sequences-uncountable). The map \( \{0, 1\} \to \nF_2 \), \( 0 \mapsto [0] \), \( 1 \mapsto [1] \), is a bijection; composing a sequence with its inverse turns every sequence \( \nN \to \nF_2 \) into a sequence of zeros and ones, and this is a surjection onto \( \{0, 1\}^{\nN} \). If the sequences \( \nN \to \nF_2 \) were countable, so would be \( \{0, 1\}^{\nN} \), by @fd2:prp-countable-image. So they are uncountable.

*The clause.* The difference is the clause **only finitely many** of @def-polynomial: a polynomial is a sequence that is \( 0 \) from some point on, so it is determined by a finite tuple, and there are countably many finite tuples. A general sequence carries infinitely many independent choices. The same count, with the polynomials written as integer tuples, is the proof of @fd2:thm-algebraic-countable.
:::

::: {#exr-formal-derivative-r4}
[R4]

Find all \( f \in \nQ[x] \) with \( f \circ x^2 = f^2 \).
:::

::: {.solution}
**Answer:** \( f = 0 \), and \( f = x^n \) for \( n \in \nN \).

*They work.* \( 0 \circ x^2 = 0 = 0^2 \), and \( x^n \circ x^2 = (x^2)^n = x^{2n} = (x^n)^2 \) by @def-polynomial-composition and the power laws (@lem-finite-sums-and-powers (c)).

*The tool* is **look at the top coefficient**, then at the next non-zero one. Let \( f \ne 0 \) satisfy \( f \circ x^2 = f^2 \), with \( n \coloneqq \deg f \) and \( a \coloneqq \operatorname{lc}(f) \). As in the proof of @prp-formal-derivative-zero (b), \( f \circ x^2 = \sum_{j=0}^{n} f_j x^{2j} \), whose coefficient at \( 2j \) is \( f_j \) and whose coefficients at odd positions are \( 0 \). So its coefficient at \( 2n \) is \( a \), and none beyond \( 2n \) is non-zero. By @thm-degree-of-product (b), since \( \nQ \) has no zero divisors, \( f^2 \) has degree \( 2n \) and leading coefficient \( a^2 \). Hence \( a^2 = a \), so \( a(a - 1) = 0 \), and \( a = 1 \) since \( a \ne 0 \) (@thm-field-basic-properties (f)).

Now let \( r \coloneqq f - x^n \), so \( f = x^n + r \) and \( \deg r < n \) (@thm-degree-of-sum, since the coefficients at \( n \) cancel). Suppose \( r \ne 0 \), and let \( k \coloneqq \deg r < n \). By @fd3:prp-ring-algebra (d) in the commutative ring \( \nQ[x] \) (@thm-polynomial-ring-laws (a)),
\[
f^2 = x^{2n} + 2 x^n r + r^2 .
\]
Its coefficient at \( n + k \) is \( 2 r_k \): \( x^{2n} \) contributes \( 0 \), since \( n + k < 2n \); \( 2 x^n r \) contributes \( 2 r_k \), since multiplying by \( x^n \) shifts by \( n \) (@lem-monomial-product (a)); and \( r^2 \) contributes \( 0 \), since \( \deg r^2 \le 2k < n + k \) (@thm-degree-of-product (a)). On the other side, the coefficient of \( f \circ x^2 \) at \( n + k \) is \( 0 \): if \( n + k \) is odd, it is an odd position; if \( n + k = 2j \), then \( k < j < n \), so \( f_j = r_j = 0 \), because \( j < n \) and \( j > \deg r \). Hence \( 2 r_k = 0 \) in \( \nQ \), and \( r_k = 0 \) since \( 2 \ne 0 \): a contradiction with \( r_k = \operatorname{lc}(r) \ne 0 \). So \( r = 0 \) and \( f = x^n \).

*Why the look-alikes fail.* Evaluating at points gives \( f(c^2) = f(c)^2 \) for every \( c \in \nQ \), a statement about polynomial functions; turning it back into a statement about coefficients needs the fact that a polynomial over an infinite field is determined by its values, which this chapter does not prove (@prp-polynomial-function-map (d) shows that over a finite ring with \( 1 \ne 0 \) it is false). Differentiating with the chain rule of Exercise B1 gives \( 2x \, (f' \circ x^2) = 2 f f' \), an equation of the same kind and no easier.

*Over \( \nF_2 \) every \( f \) works.* There \( (u + v)^2 = u^2 + v^2 \), since \( 2uv = 0 \), and \( c^2 = c \) for \( c \in \nF_2 \); so \( f^2 = \sum_k f_k^2 x^{2k} = \sum_k f_k x^{2k} = f \circ x^2 \). The step that fails is "\( 2 r_k = 0 \) implies \( r_k = 0 \)": in \( \nF_2 \), \( 2 = 0 \).
:::

<!-- dependency ledger
def-formal-derivative (claim): (hook) a double root of (x - 1)^2 has slope 0; the school derivative of a x^n is n a x^(n-1) | school calculus, motivation only; nothing in fd4 rests on it
def-formal-derivative (claim): higher derivatives exist and are unique | fd2:thm-recursion, cited; read on N = omega through fd3:cor-omega-identification (b) as set up in Section 3.1, not repeated; the step u -> u' is a function R[x] -> R[x] by the well-definedness bullet
def-formal-derivative (claim): k >= N gives k + 1 > N; (f')_k = 0 for k > N - 1 | index arithmetic in N, fd3:thm-omega-order with fd3:prp-naturals-embed-integers; inline
def-formal-derivative (claim): formula (M) for (a x^n)' | def-polynomial (the monomial), def-formal-derivative, m * 0 = 0 (proved in the first bullet); inline
def-formal-derivative (claim): 1 + 1 = 0 in F_2, so (x^2)' = 0 | exm-finite-fields, cited where repeated in exm-formal-derivatives (iii)
def-formal-derivative (claim): (why this definition) uniqueness of the derivation with delta(x) = 1 | exr-formal-derivative-c1, a pointer only; nothing in the text rests on it
def-formal-derivative (claim): (warning) sum_k (k * f_k) x^k = x f' | coefficient comparison with lem-monomial-product (a), m = 1; inline, not used
exm-formal-derivatives (example): 1 * 1 = 1, n * 1 = n in Z | the recursion of multiples, "Multiples" paragraph of F3.2 Section 2.3 (cited by position, as fd3 F3.5 does)
exm-formal-derivatives (example): n * 1 = n in Q by induction | fd3:prp-naturals-embed-integers, fd3:prp-integers-embed-rationals, cited; fd1:ax-induction read on omega; inline
exm-formal-derivatives (example): all quoted coefficients (2, 0, -6, 4; 1; 0; [6] = [0]); (vi) (x^4)', (x^4)'', (x^4)''' = 4x^3, 12x^2, 24x over Q and x^3, 0, 0 over F_3 | verify/ch03/exm-formal-derivatives.py
def-formal-derivative (claim): (quick check) (x^3 + x^2 + x + 1)' = x^2 + 1 over F_2 | verify/ch03/def-formal-derivative.py
thm-formal-derivative-rules (proof): regrouping four terms in R[x]; f'g + fg' = g'f + gf' | (F1), (F2), (F6) of R[x] via thm-polynomial-ring-laws (a); inline
thm-formal-derivative-rules (proof): (i - 1) + j = i + (j - 1) = i + j - 1 in N for i, j >= 1 | fd3:thm-omega-arithmetic-laws, fd3:prp-naturals-embed-integers; inline
thm-formal-derivative-rules (proof): two monomials in the same position add coefficientwise | def-polynomial-ring (coefficientwise +), cited
thm-formal-derivative-rules (proof): induction on m >= 1; g^(m-1) g = g^m; (m + 1) * 1 = m * 1 + 1 | fd1:ax-induction read on omega (fd3:cor-omega-identification); lem-finite-sums-and-powers (c) (power recursion); the recursion of multiples (F3.2 Section 2.3, by position)
thm-formal-derivative-rules (proof): (f - g)' = f' - g' | from (a), proved inline in (c)
thm-formal-derivative-rules (claim): (aftermath) (x - c)^p has derivative 0 over F_p | thm-formal-derivative-rules (c) and p * 1 = 0 in F_p (fd3:thm-integers-mod-n-ring (d)); inline
thm-formal-derivative-rules (claim): (remark) over Q and over the reals f' agrees with the derivative of calculus | prose only; no an1 citation; nothing depends on it
thm-formal-derivative-rules (claim): (quick check) ((x + 1)^3)' = 0 over F_3; (x + 1)^3 = x^3 + 1 | verify/ch03/thm-formal-derivative-rules.py
prp-formal-derivative-zero (claim): (opening) a function with derivative 0 on an interval is constant | school calculus, motivation only; nothing rests on it
prp-formal-derivative-zero (proof): as k runs through k >= 1, k - 1 runs through N | index arithmetic, fd3:prp-naturals-embed-integers; inline
prp-formal-derivative-zero (proof): k * 1 = 0 iff p | k | prp-characteristic-divides (a) with c = p, cited
prp-formal-derivative-zero (proof): p | 0, so p does not divide k forces k != 0 | fd3:prp-divisibility-rules-integers (a); inline
prp-formal-derivative-zero (proof): pj >= j > N for p >= 1, j > N; k = pj_0, k >= 0, p > 0 implies j_0 >= 0; pj = pj' implies j = j' | fd3:thm-integers-ordered-ring with fd3:prp-ordered-ring-rules (c), (f); inline
prp-formal-derivative-zero (proof): the k-th coefficient of a finite sum in F[x] is the sum of the k-th coefficients | def-polynomial-ring (coefficientwise +) and the sum recursion of lem-finite-sums-and-powers (a), induction on the number of terms; inline
prp-formal-derivative-zero (claim): (aftermath) x^2 + 1 = (x + 1) o x^2 over F_2; x^6 + 2x^3 + 1 = (x^2 + 2x + 1) o x^3 over F_3 with derivative 0 | verify/ch03/prp-formal-derivative-zero.py
prp-formal-derivative-zero (claim): (warning) (x^p)' = 0 and (x^p - x)' = -1 over F_p; Chapter 4 shows x^p - x has no repeated roots | (M) and fd3:thm-integers-mod-n-ring (d), inline; Chapter 4 = F5.5 (promised; prose pointer, nothing here depends on it)
prp-formal-derivative-zero (claim): (quick check) (x^5 + x)' = 1 over F_5 | verify/ch03/prp-formal-derivative-zero.py
exr-formal-derivative-a1 (solution): (x^5 - x)' = 5x^4 - 1 over Q and -1 = 4 over F_5; deg f' in {1, 0, -infinity} with witnesses | verify/ch03/exr-formal-derivative-a1.py
exr-formal-derivative-b1 (solution): a ring homomorphism sends 0 to 0 and preserves powers | def-ring-homomorphism (its consequences paragraph), cited
exr-formal-derivative-b1 (solution): check (x^2 + 1)^2 = x^4 + 2x^2 + 1, derivative 4x^3 + 4x | verify/ch03/exr-formal-derivative-b1.py
exr-formal-derivative-b2 (solution): P(n, k + 1) = P(n, k)(n - k); the added factor is j + 1; P(4, 3) = 24 | arithmetic in N, fd3:thm-omega-arithmetic-laws; verify/ch03/exr-formal-derivative-b2.py
exr-formal-derivative-b2 (solution): one of p consecutive integers is divisible by p; a product with such a factor is divisible by p | fd3:thm-integers-division-remainder, fd3:prp-divisibility-rules-integers (c), cited; induction on the number of factors, inline
exr-formal-derivative-c1 (solution): induction for delta(x^n) | fd1:ax-induction read on omega; inline
exr-formal-derivative-c2 (solution): k * 1 = k in Q | as in exm-formal-derivatives (i): fd3:prp-naturals-embed-integers, fd3:prp-integers-embed-rationals, cited
exr-formal-derivative-r1 (solution): (f')_n = 0 at n = deg f; E(0) = 0 + 0' = 0; E(x)E(x) = x^2 + 2x + 1 and E(x^2) = x^2 + 2x differ in position 0 when 1 != 0 | def-formal-derivative ((M) for 0' = 0), def-degree, fd3:prp-ring-algebra (d), cited; verify/ch03/exr-formal-derivative-r1.py
exr-formal-derivative-r1 (solution): R1 reaches back to F5.3 (group homomorphisms and kernels) | def-group-homomorphism, prp-homomorphism-injective-iff-kernel-trivial, cited; R review item
exr-formal-derivative-r2 (solution): conj 1 = 1, conj a = a for real a, conj 0 = 0 | def-conjugate-modulus, cited (a + 0i notation of prp-reals-embed-complex)
exr-formal-derivative-r2 (solution): R is an ordered field (2 != 0, no zero divisors) | R of F3.10, through def-complex-numbers (C := R^2); fd3:prp-ordered-ring-rules (f), (h), cited; R review item under the see edge to F4.1
exr-formal-derivative-r3 (solution): {0, 1} -> F_2 is a bijection ([0] != [1]) | fd3:thm-integers-mod-n-ring (b), (c); inline
exr-formal-derivative-r3 (solution): fd2 countability results read on omega | fd3:cor-omega-identification, cited; fd2:thm-countable-union (a) uses countable choice (flagged in the text)
exr-formal-derivative-r3 (solution): A_N in bijection with R^(N+1) | exr-polynomials-as-sequences-b1, an exercise cited from an exercise solution, which STYLE allows
exr-formal-derivative-r4 (solution): the coefficients of f o x^2 = sum_j f_j x^(2j) | the computation in the proof of prp-formal-derivative-zero (b), (ii) => (iii), with p = 2
exr-formal-derivative-r4 (solution): 2k < n + k < 2n and n + k = 2j imply k < j < n | order in N; inline
exr-formal-derivative-r4 (solution): over F_2, (u + v)^2 = u^2 + v^2 and c^2 = c, extended to a finite sum by induction | fd3:prp-ring-algebra (d) with 2 = 0 in F_2; inline
exr-formal-derivative-r4 (solution): brute-force sanity check of the answer for small degrees and coefficients over Q, and of "every f works" over F_2 | verify/ch03/exr-formal-derivative-r4.py
-->
