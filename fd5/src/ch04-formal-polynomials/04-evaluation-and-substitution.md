# Evaluation, Substitution, and Polynomial Functions

A polynomial, in this chapter, is a sequence of coefficients (@def-polynomial), not a function. But every polynomial **defines** a function: put an element \( c \) of the ring in place of \( x \) and add up. More generally we can put in place of \( x \) a class modulo \( n \), or another polynomial, after first moving the coefficients into the ring where the substitution happens. This section proves one theorem, the substitution principle, that covers all of these at once, because each is a ring homomorphism out of \( R[x] \) determined by where it sends the constants and \( x \). Then it compares a polynomial with its function, and shows that over every finite ring other than the zero ring the passage from polynomials to functions loses information.

Throughout, \( R \) and \( S \) are commutative rings (@fd3:def-commutative-ring-and-field), and powers \( s^n \) and finite sums are those of @lem-finite-sums-and-powers.

## Evaluating a polynomial

*To evaluate a polynomial at \( c \), replace each monomial \( a x^k \) by the element \( a c^k \) and add.*

::: {#def-polynomial-evaluation}
[Evaluation, Root, Polynomial Function]

Let \( R \) be a commutative ring, \( p \in R[x] \) and \( c \in R \). The **value** of \( p \) at \( c \) is
\[
p(c) \coloneqq \sum_{k=0}^{N} p_k c^k \in R ,
\]
for **any** \( N \in \nN \) with \( p_k = 0 \) for every \( k > N \). The element \( c \) is a **root** of \( p \) if \( p(c) = 0 \). The **polynomial function** of \( p \) is the function \( R \to R \), \( c \mapsto p(c) \).
:::

In words: the value is the finite sum of the coefficients times the powers of \( c \), with \( c^0 = 1 \), so the constant coefficient enters as itself. The sum runs far enough to include every non-zero coefficient, and how far beyond that is our choice. Only finitely many coefficients are non-zero, and this is what makes the sum finite; a sequence such as \( (1, 1, 1, \dots) \) would ask for an infinite sum, which a ring does not provide.

*Well-definedness.* The definition allows many \( N \), and they all give the same element: enlarging \( N \) only adds terms \( 0 \cdot c^k = 0 \). The fold below writes this out.

::: {.second-reading title="Why the value does not depend on the bound"}
Let \( N \) be admissible for \( p \). We show by @fd1:ax-induction on \( j \) (through @fd3:cor-omega-identification (b)) that \( \sum_{k=0}^{N+j} p_k c^k = \sum_{k=0}^{N} p_k c^k \). The case \( j = 0 \) is trivial, and the sum recursion of @lem-finite-sums-and-powers (a) gives
\[
\begin{aligned}
\sum_{k=0}^{N+j+1} p_k c^k &= \sum_{k=0}^{N+j} p_k c^k + p_{N+j+1} c^{N+j+1} \\
&= \sum_{k=0}^{N+j} p_k c^k + 0 ,
\end{aligned}
\]
since \( p_{N+j+1} = 0 \) and \( 0 \cdot c^{N+j+1} = 0 \) (@fd3:prp-ring-algebra (b) with (F6)); then (F3) and the hypothesis finish. Any two admissible \( N \) and \( N' \) differ in this way, the larger being the smaller plus some \( j \in \nN \). So \( p(c) \) depends only on \( p \) and \( c \).
:::

**Examples.**

- In \( \nQ[x] \), let \( p = x^2 - 3x + 2 \), with coefficients \( 2, -3, 1 \). Then \( p(0) = 2 \), \( p(1) = 1 - 3 + 2 = 0 \) and \( p(2) = 4 - 6 + 2 = 0 \): \( 1 \) and \( 2 \) are roots.
- In \( \nF_3[x] \), let \( p = x^3 + 2 \). Its values at \( 0, 1, 2 \) are \( 2 \), \( 1 + 2 = 3 = 0 \) and \( 8 + 2 = 10 = 1 \) (in \( \nF_3 \)). Its only root in \( \nF_3 \) is \( 1 \).
- **A monomial.** For \( a x^m \), take \( N = m \): every term with \( k \ne m \) is \( 0 \cdot c^k = 0 \), so (Σ3) of @lem-finite-sums-and-powers gives \( (a x^m)(c) = a c^m \). In particular a constant \( a = a x^0 \) has value \( a c^0 = a \cdot 1 = a \) at every \( c \), and \( x = 1 x^1 \) has value \( 1 \cdot c^1 = c \).

::: {.warning}
**\( p(2) \) is a value; \( p_2 \) is a coefficient.** For \( p = x^2 - 3x + 2 \in \nZ[x] \), \( p_2 = 1 \) but \( p(2) = 0 \). At \( 0 \) the two always agree, \( p(0) = p_0 \), because \( 0^k = 0 \) for \( k \ge 1 \); at any other position they differ in general. Over \( \nZ \) both are integers, which is why this book never writes \( p(k) \) for a coefficient.
:::

## Evaluation respects the operations

At school, "substitute \( x = c \)" is done after or before multiplying out, with the same answer. In our setting that is a theorem: evaluation at \( c \) turns sums and products of polynomials into sums and products in \( R \).

::: {#thm-evaluation-respects-operations}
[Evaluation Respects the Operations]

Let \( R \) be a commutative ring, \( p, q \in R[x] \) and \( c \in R \). Then
\[
(p + q)(c) = p(c) + q(c) , \qquad (pq)(c) = p(c) \, q(c) ,
\]
and \( a(c) = a \) for every constant \( a \), and \( x(c) = c \).
:::

::: {.idea}
Sums are coefficientwise, and the sum rule (Σ1) splits the defining sum. For products, the move is **check on monomials, extend by additivity** (@lem-check-on-monomials): both sides are additive in \( p \) and in \( q \), and on monomials the product rule is the power law \( c^{m+n} = c^m c^n \) together with one reordering of factors in \( R \).
:::

::: {.proof}
*Sums.* Let \( N \) be admissible for both \( p \) and \( q \) (the larger of an admissible \( N \) for each). Then \( N \) is admissible for \( p + q \), and
\[
\begin{aligned}
(p + q)(c) &= \sum_{k=0}^{N} (p_k + q_k) c^k \\
&= \sum_{k=0}^{N} \bigl(p_k c^k + q_k c^k\bigr) = p(c) + q(c) ,
\end{aligned}
\]
by @def-polynomial-ring, then (F6) and (F9) in each term, then (Σ1) of @lem-finite-sums-and-powers.

*Constants and \( x \).* These are the monomial example after @def-polynomial-evaluation: \( a(c) = a c^0 = a \) and \( x(c) = 1 \cdot c^1 = c \).

*Products.* Define \( \Phi, \Psi \colon R[x] \times R[x] \to R \) by \( \Phi(p, q) \coloneqq (pq)(c) \) and \( \Psi(p, q) \coloneqq p(c) \, q(c) \). Both are additive in each argument. For \( \Phi \) in the first argument,
\[
\Phi(p + p', q) = \bigl(pq + p'q\bigr)(c) = (pq)(c) + (p'q)(c) = \Phi(p, q) + \Phi(p', q) ,
\]
by the distributive law of the ring \( R[x] \) (@thm-polynomial-ring-laws (a)) and the sum rule just proved. For \( \Psi \), \( \bigl(p(c) + p'(c)\bigr) q(c) = p(c) q(c) + p'(c) q(c) \) by the sum rule, (F6) and (F9). The second argument is the same with \( p(q + q') = pq + pq' \).

On monomials \( a x^m \) and \( b x^n \), @lem-monomial-product (b) gives \( (a x^m)(b x^n) = (ab) x^{m+n} \), so
\[
\Phi(a x^m, b x^n) = (ab) c^{m+n} = (ab)(c^m c^n) = (a c^m)(b c^n) = \Psi(a x^m, b x^n) ,
\]
by the value of a monomial, the power law \( c^{m+n} = c^m c^n \) (@lem-finite-sums-and-powers (c)), and (F5) and (F6) to move \( b \) past \( c^m \). By @lem-check-on-monomials with two arguments and \( T = R \), \( \Phi = \Psi \). This proves the theorem.
:::

::: {.remark}
The monomial line moves the coefficient \( b \) past the power \( c^m \); that is the one step that needs two elements of \( R \) to commute. Elsewhere (F6) is used only to get the mirror forms of (F7), (F9) and @fd3:prp-ring-algebra (b), namely \( 1 \cdot c = c \), \( (a + b)c = ac + bc \) and \( 0 \cdot c = 0 \). The same proof works for substituting a square matrix into a polynomial with coefficients in a field, as in the linear-algebra companion, Chapter 0, because there the mirror laws hold for matrices too, \( b \) is a scalar, and scalars commute with every matrix; two matrices need not commute, and nothing in the proof asks them to.
:::

Two consequences are used constantly. First, a root of a factor is a root of the product: if \( q(c) = 0 \), then \( (pq)(c) = p(c) \cdot 0 = 0 \). Second, if \( R \) has no zero divisors, the converse holds: \( (pq)(c) = p(c) q(c) = 0 \) forces \( p(c) = 0 \) or \( q(c) = 0 \). This is the school method for solving \( (x - 1)(x - 2) = 0 \). In \( \nQ[x] \), \( (x - 1)(x - 2) = x^2 - 3x + 2 \) by the product formula, so, since \( \nQ \) is an integral domain (@exm-integral-domains) and \( (x - a)(c) = c - a \) by the sum rule and the value of a constant, the roots of \( x^2 - 3x + 2 \) in \( \nQ \) are exactly the \( c \) with \( c - 1 = 0 \) or \( c - 2 = 0 \): the numbers \( 1 \) and \( 2 \) found above, and no others.

## Ring homomorphisms

Evaluation at \( c \) is a map \( R[x] \to R \) that respects \( + \), \( \cdot \) and \( 1 \). The quotient map \( \nZ \to \nZ/n\nZ \) of @thm-quotient-ring-by-ideal (c) does the same, and so does the map of the Chinese remainder theorem. Maps of this kind recur in every chapter from here on.

*A ring homomorphism is a map between rings that turns sums into sums, products into products, and the one into the one.*

::: {#def-ring-homomorphism}
[Ring Homomorphism]

Let \( R \) and \( S \) be commutative rings. A **ring homomorphism** \( \varphi \colon R \to S \) is a function such that, **for all** \( a, b \in R \),
\[
\varphi(a + b) = \varphi(a) + \varphi(b) , \qquad \varphi(ab) = \varphi(a) \varphi(b) ,
\]
and \( \varphi(1) = 1 \).
:::

In words: computing in \( R \) and then applying \( \varphi \) gives the same result as applying \( \varphi \) and then computing in \( S \). The sum and product on the left are those of \( R \), on the right those of \( S \). The condition on \( 1 \) is not a consequence of the other two, as the zero map below shows.

Between two fields this is exactly a homomorphism of fields (@def-field-homomorphism). The consequences below are the ring versions of @prp-field-homomorphism-properties (a), the composites in (e) and the powers in (f), with the same proofs. Parts (b)–(d) of that proposition do not carry over: the quotient map \( \nZ \to \nZ/n\nZ \) of @exm-ring-homomorphisms (i) is not injective.

*Consequences.* Let \( \varphi \colon R \to S \) be a ring homomorphism.

- \( \varphi(0) = 0 \). Let \( z \coloneqq \varphi(0) \). Then \( z + z = \varphi(0 + 0) = z \), by (F3) in \( R \). Adding \( -z \) to both sides and using (F2), (F4) and (F3) in \( S \) gives \( z = 0 \). (This is cancellation, not the uniqueness of \( 0 \) in @fd3:prp-ring-algebra (a): uniqueness concerns an element that is neutral for **every** element, and we only know \( z + z = z \).)
- \( \varphi(-a) = -\varphi(a) \): \( \varphi(a) + \varphi(-a) = \varphi(a + (-a)) = \varphi(0) = 0 \), and negatives are unique (@fd3:prp-ring-algebra (a)). Hence also \( \varphi(a - b) = \varphi(a) - \varphi(b) \).
- \( \varphi(s^n) = \varphi(s)^n \) for \( s \in R \) and \( n \in \nN \), by @fd1:ax-induction on \( n \): \( \varphi(s^0) = \varphi(1) = 1 = \varphi(s)^0 \), and \( \varphi(s^{n+1}) = \varphi(s^n s) = \varphi(s)^n \varphi(s) = \varphi(s)^{n+1} \).
- If \( \psi \colon S \to T \) is another ring homomorphism, then so is \( \psi \circ \varphi \colon R \to T \): \( \psi(\varphi(a + b)) = \psi(\varphi(a) + \varphi(b)) = \psi(\varphi(a)) + \psi(\varphi(b)) \), the same for products, and \( \psi(\varphi(1)) = \psi(1) = 1 \).

::: {#exm-ring-homomorphisms}
[Ring Homomorphisms and Two Impostors]

Which of the following are ring homomorphisms? (i) The quotient map \( \nZ \to \nZ/n\nZ \), \( a \mapsto [a] \), for \( n \in \nZ_{>0} \). (ii) The constants \( R \to R[x] \), \( a \mapsto a x^0 \). (iii) The map \( \nZ/mn\nZ \to \nZ/m\nZ \times \nZ/n\nZ \), \( [a]_{mn} \mapsto ([a]_m, [a]_n) \), for coprime \( m, n \in \nZ_{>0} \). (iv) \( \nZ \to \nZ \), \( a \mapsto 2a \). (v) The zero map \( \nZ \to \nZ \), \( a \mapsto 0 \).
:::

::: {.solution}
(i) Yes, by @thm-quotient-ring-by-ideal (c) with the ideal \( n\nZ \) (@def-integers-mod-n-ring); more generally, the quotient map \( R \to R/I \) is one for every ideal \( I \).

(ii) Yes, by @thm-polynomial-ring-laws (b).

(iii) Yes, by @thm-chinese-remainder-two (b), where the target carries componentwise operations; it is a commutative ring because each axiom holds in each component, and its one is \( ([1]_m, [1]_n) \).

(iv) No. It is additive, \( 2(a + b) = 2a + 2b \), but not multiplicative: \( 2(1 \cdot 1) = 2 \), while \( (2 \cdot 1)(2 \cdot 1) = 4 \). It also sends \( 1 \) to \( 2 \).

(v) No. It is additive and multiplicative (\( 0 = 0 + 0 = 0 \cdot 0 \)), but it sends \( 1 \) to \( 0 \ne 1 \).

Complex conjugation \( z \mapsto \conj{z} \) on \( \nC \), whose rules are proved in *Analytic Preliminaries*, Chapter 1, is another example; we use it only in a review exercise of the next section.
:::

## The substitution principle

Evaluation puts an element of \( R \) in place of \( x \). Reduction modulo \( n \) changes the coefficients from \( \nZ \) to \( \nZ/n\nZ \) and keeps \( x \). Composition puts a polynomial in place of \( x \). The next theorem does all three: it moves the coefficients along a ring homomorphism \( \varphi \) and puts an element \( s \) in place of \( x \), and it says that there is exactly one way to do so that respects the operations.

::: {#thm-polynomial-substitution}
[Substitution Principle]

Let \( R \) and \( S \) be commutative rings, \( \varphi \colon R \to S \) a ring homomorphism, and \( s \in S \). Define \( \Phi \colon R[x] \to S \) by
\[
\Phi(p) \coloneqq \sum_{k=0}^{N} \varphi(p_k) \, s^k ,
\]
for any \( N \) admissible for \( p \).

::: {.enumerate options="label=(\alph*)"}
1. \( \Phi \) is well defined, and it is a ring homomorphism with \( \Phi(a) = \varphi(a) \) for every constant \( a \in R \) and \( \Phi(x) = s \).
2. \( \Phi \) is the **only** ring homomorphism \( R[x] \to S \) with these two properties.
:::
:::

In words: (a) says that substituting \( s \) for \( x \), after moving each coefficient to \( S \) by \( \varphi \), respects sums, products and \( 1 \); (b) says that a ring homomorphism out of \( R[x] \) is pinned down by what it does to the constants and to \( x \).

*Try it first (ten minutes): take \( R = \nZ \), \( S = \nZ/5\nZ \), \( \varphi \) the quotient map, and \( s = [2] \). Which value must a ring homomorphism \( \Phi \) with \( \Phi(a) = [a] \) for constants and \( \Phi(x) = [2] \) give to \( 3x^2 + 1 \)? Why is there no choice?*

::: {.idea}
The attempt finds the value at once: \( 3x^2 + 1 \) is the constant \( 3 \) times \( x \) times \( x \), plus the constant \( 1 \) (@thm-polynomial-ring-laws (c)), so a homomorphism must send it to \( [3][2][2] + [1] = [13] = [3] \). The same reasoning applies to every polynomial: a homomorphism has no freedom, because it must send \( a x^n \) to \( \varphi(a) s^n \), and then the sum of the monomials to the sum of their images. That proves (b) and shows that the formula for \( \Phi \) is forced. The only work is (a), showing that the forced formula respects products, and that is again a check on monomials, with the coefficients now computed in \( S \).

*Before reading on: where is \( S \) commutative used, and where \( \varphi(1) = 1 \)?*
:::

::: {.proof}
*(a) Well defined.* If \( N \) is admissible, then so is \( N + j \), and each added term is \( \varphi(0) s^k = 0 \cdot s^k = 0 \), by \( \varphi(0) = 0 \) (after @def-ring-homomorphism) and @fd3:prp-ring-algebra (b) with (F6); as for @def-polynomial-evaluation, the value does not depend on \( N \). Taking \( N = m \) for a monomial, (Σ3) of @lem-finite-sums-and-powers gives
\[
\Phi(a x^m) = \varphi(a) \, s^m .
\]

*Additive.* Let \( N \) be admissible for \( p \) and \( q \). Then
\[
\begin{aligned}
\Phi(p + q) &= \sum_{k=0}^{N} \varphi(p_k + q_k) s^k \\
&= \sum_{k=0}^{N} \bigl(\varphi(p_k) s^k + \varphi(q_k) s^k\bigr) = \Phi(p) + \Phi(q) ,
\end{aligned}
\]
by additivity of \( \varphi \), (F6) and (F9) in \( S \), and (Σ1).

*Multiplicative.* The maps \( (p, q) \mapsto \Phi(pq) \) and \( (p, q) \mapsto \Phi(p)\Phi(q) \), from \( R[x] \times R[x] \) to \( S \), are additive in each argument: the first by the distributive laws of \( R[x] \) (@thm-polynomial-ring-laws (a)) and additivity of \( \Phi \), the second by additivity of \( \Phi \) and (F9), (F6) in \( S \). On monomials, by @lem-monomial-product (b), multiplicativity of \( \varphi \), the power law of @lem-finite-sums-and-powers (c), and (F5), (F6) **in \( S \)**,
\[
\begin{aligned}
\Phi\bigl((a x^m)(b x^n)\bigr) &= \Phi\bigl((ab) x^{m+n}\bigr) = \varphi(ab) \, s^{m+n} \\
&= \varphi(a) \varphi(b) \, s^m s^n = \bigl(\varphi(a) s^m\bigr)\bigl(\varphi(b) s^n\bigr) \\
&= \Phi(a x^m) \, \Phi(b x^n) .
\end{aligned}
\]
By @lem-check-on-monomials with two arguments and \( T = S \), \( \Phi(pq) = \Phi(p)\Phi(q) \) for all \( p, q \).

*The one, the constants, \( x \).* \( \Phi(1) = \Phi(1 x^0) = \varphi(1) s^0 = 1 \cdot 1 = 1 \). For a constant, \( \Phi(a x^0) = \varphi(a) s^0 = \varphi(a) \). And \( \Phi(x) = \Phi(1 x^1) = \varphi(1) s^1 = s \). So \( \Phi \) is a ring homomorphism with the two properties.

*(b)* Let \( \Psi \colon R[x] \to S \) be a ring homomorphism with \( \Psi(a x^0) = \varphi(a) \) for every \( a \in R \) and \( \Psi(x) = s \). By @thm-polynomial-ring-laws (c), the monomial \( a x^n \) is the product of the constant \( a \) and the \( n \)-th power of \( x \), so
\[
\Psi(a x^n) = \Psi(a x^0) \, \Psi(x)^n = \varphi(a) \, s^n = \Phi(a x^n) ,
\]
by multiplicativity and the power property of ring homomorphisms (after @def-ring-homomorphism). Both \( \Psi \) and \( \Phi \) are additive maps \( R[x] \to S \) that agree on monomials, so \( \Psi = \Phi \) by @lem-check-on-monomials with one argument. This proves the theorem.
:::

The answer to the prompt. Commutativity of \( S \) does real work in one place, the middle line of the monomial computation, where it moves \( \varphi(b) \) past \( s^m \). Its other uses (\( 0 \cdot s^k = 0 \), the right distributive law \( (u + v)w = uw + vw \) in the additivity steps, and \( 1 \cdot s = s \)) only supply the mirror forms of @fd3:prp-ring-algebra (b), (F9) and (F7), which a two-sided list of ring axioms gives directly. The condition \( \varphi(1) = 1 \) is used twice, for \( \Phi(1) = 1 \) and for \( \Phi(x) = s \). If \( S \) is not commutative but satisfies those two-sided laws, the same proof goes through provided \( s \) commutes with every \( \varphi(b) \), since that is all the monomial line asks; this is the case of a square matrix and scalar coefficients, from the remark after @thm-evaluation-respects-operations.

::: {.remark}
With \( S = R \), \( \varphi = \id_R \) and \( s = c \), the map \( \Phi \) is \( p \mapsto p(c) \), and part (a) contains @thm-evaluation-respects-operations. We proved evaluation first because it is the case used most, and its proof is the substitution proof with \( \varphi \) invisible.
:::

We call the move of (b) **a homomorphism out of \( R[x] \) is fixed by the constants and \( x \)**: to show that two ring homomorphisms out of \( R[x] \) agree, check that they agree on constants and on \( x \).

## Changing coefficients and composing

Two special cases of the substitution principle get names: the change of coefficients, which the algebra volumes of the series use for reduction modulo a prime, and composition, which Section 4.5 uses.

The first moves the coefficients and keeps \( x \): take the target \( S[x] \), the homomorphism "\( \varphi \), then a constant of \( S[x] \)", and \( s = x \).

::: {#cor-polynomial-coefficient-change}
[Changing the Coefficient Ring]

Let \( \varphi \colon R \to S \) be a ring homomorphism. For \( p \in R[x] \), let \( \varphi_*(p) \) be the sequence with \( \bigl(\varphi_*(p)\bigr)_k \coloneqq \varphi(p_k) \). Then \( \varphi_*(p) \in S[x] \), and \( \varphi_* \colon R[x] \to S[x] \) is a ring homomorphism with \( \varphi_*(a x^n) = \varphi(a) x^n \). Moreover \( \deg \varphi_*(p) \le \deg p \) for every \( p \), and for \( p \ne 0 \), equality holds **if and only if** \( \varphi(\operatorname{lc}(p)) \ne 0 \).
:::

::: {.idea}
Substitute \( x \) for \( x \), after moving each coefficient to \( S \): the substitution principle then hands us a ring homomorphism, and its formula is the coefficientwise image. The degree can only drop, and it drops exactly when the leading coefficient is sent to \( 0 \).
:::

::: {.proof}
If \( p_k = 0 \) for \( k > N \), then \( \varphi(p_k) = \varphi(0) = 0 \) for \( k > N \), so \( \varphi_*(p) \) is a polynomial over \( S \). Let \( \gamma \colon R \to S[x] \), \( \gamma(a) \coloneqq \varphi(a) x^0 \): the composite of \( \varphi \) and the constants of \( S[x] \), a ring homomorphism (@exm-ring-homomorphisms (ii) and the composite rule after @def-ring-homomorphism). @thm-polynomial-substitution with target \( S[x] \), \( \gamma \) and \( s = x \) gives a ring homomorphism \( \Phi \colon R[x] \to S[x] \) with
\[
\begin{aligned}
\Phi(p) &= \sum_{k=0}^{N} \bigl(\varphi(p_k) x^0\bigr) x^k \\
&= \sum_{k=0}^{N} \varphi(p_k) x^k = \varphi_*(p) ,
\end{aligned}
\]
where the middle equality is @thm-polynomial-ring-laws (c) in \( S[x] \), and the last is @prp-polynomial-sum-of-monomials applied to \( \varphi_*(p) \in S[x] \). So \( \varphi_* = \Phi \) is a ring homomorphism, and \( \varphi_*(a x^n) = \varphi(a) x^n \) by definition.

For the degree: if \( p = 0 \), then \( \varphi_*(p) = 0 \). Otherwise let \( d \coloneqq \deg p \). For \( k > d \), \( \varphi(p_k) = \varphi(0) = 0 \), so \( \deg \varphi_*(p) \le d \); and the coefficient of \( \varphi_*(p) \) at \( d \) is \( \varphi(\operatorname{lc}(p)) \), so the degree is exactly \( d \) if and only if this element is non-zero.
:::

The main example is **reduction modulo \( n \)**: the quotient map \( \nZ \to \nZ/n\nZ \) gives \( \nZ[x] \to (\nZ/n\nZ)[x] \), which reads every coefficient modulo \( n \) and respects sums and products. For \( n = 2 \),
\[
2x^2 + 3x - 1 \ \longmapsto \ 0x^2 + 1x + 1 = x + 1 \in \nF_2[x] ,
\]
since \( 2 = 0 \), \( 3 = 1 \) and \( -1 = 1 \) in \( \nF_2 \): the degree drops from \( 2 \) to \( 1 \), because the leading coefficient \( 2 \) reduces to \( 0 \). The opening computation of Section 4.3 is another instance: modulo \( 6 \), \( 6x^3 + 5x^2 + x \) reduces to \( [5]x^2 + x \), of lower degree because its leading coefficient \( 6 \) reduces to \( [0] \). The algebra volumes of the series test integer polynomials for factorization by reducing them modulo a prime in exactly this way.

The second special case substitutes a polynomial for \( x \): take \( S = R[x] \), \( \varphi \) the constants (@exm-ring-homomorphisms (ii)) and \( s = q \).

::: {#def-polynomial-composition}
[Composition of Polynomials]

Let \( R \) be a commutative ring and \( p, q \in R[x] \). The **composition** \( p \circ q \in R[x] \) is \( \Phi(p) \) for the homomorphism \( \Phi \) of @thm-polynomial-substitution with \( S = R[x] \), \( \varphi \colon a \mapsto a x^0 \) and \( s = q \):
\[
p \circ q = \sum_{k=0}^{N} p_k \, q^k \qquad (N \text{ admissible for } p).
\]
:::

By @thm-polynomial-substitution (a), \( p \mapsto p \circ q \) is a ring homomorphism \( R[x] \to R[x] \) that fixes every constant, \( a \circ q = a \), and sends \( x \) to \( x \circ q = q \). Substituting \( x \) itself changes nothing: \( p \circ x = \sum_k p_k x^k = p \), by @thm-polynomial-ring-laws (c) and @prp-polynomial-sum-of-monomials. For example, in \( \nZ[x] \),
\[
(x^2 + 1) \circ (x + 1) = (x + 1)^2 + 1 = x^2 + 2x + 2 ,
\]
where \( (x + 1)^2 = x^2 + 2x + 1 \) by the product formula. The polynomial \( p(-x) \coloneqq p \circ (-x) \) has coefficients \( (-1)^k p_k \), since \( (-x)^k = (-1)^k x^k \): it is the sign-change map \( \sigma \) of @exr-polynomial-ring-b2, which the substitution principle shows once more to be multiplicative.

::: {.check}
In \( (\nZ/8\nZ)[x] \), evaluate \( x^2 - 1 \) at \( [3] \). Which ring homomorphism of @thm-polynomial-substitution is "evaluate at \( [3] \)"?
:::

::: {.solution}
\( [3]^2 - [1] = [9 - 1] = [8] = [0] \), so \( [3] \) is a root. Evaluation at \( [3] \) is the \( \Phi \) of @thm-polynomial-substitution with \( R = S = \nZ/8\nZ \), \( \varphi = \id_{\nZ/8\nZ} \) and \( s = [3] \).
:::

## Polynomials and polynomial functions

Every polynomial \( p \in R[x] \) has a polynomial function \( R \to R \). The functions \( R \to R \) form a ring of their own, and passing from a polynomial to its function respects the operations. The question is whether anything is lost on the way.

::: {#prp-polynomial-function-map}
[Polynomials and Their Functions]

Let \( R \) be a commutative ring.

::: {.enumerate options="label=(\alph*)"}
1. The set \( R^R \) of functions \( R \to R \) (@fd2:def-function), with the pointwise operations \( (f + g)(c) \coloneqq f(c) + g(c) \) and \( (fg)(c) \coloneqq f(c) g(c) \), is a commutative ring, whose zero and one are the constant functions with values \( 0 \) and \( 1 \).
2. The map \( \varepsilon \colon R[x] \to R^R \), \( \varepsilon(p) \coloneqq (c \mapsto p(c)) \), is a ring homomorphism.
3. For all \( p, q \in R[x] \) and \( c \in R \), \( (p \circ q)(c) = p(q(c)) \): composition of polynomials matches composition of their functions.
4. If \( R \) is **finite** with \( 1 \ne 0 \), then \( \varepsilon \) is **not** injective. Explicitly, if \( c_1, \dots, c_r \) lists the elements of \( R \) without repetition, then
\[
P \coloneqq \prod_{j=1}^{r} (x - c_j)
\]
is monic of degree \( r \), so \( P \ne 0 \), yet \( P(c) = 0 \) for every \( c \in R \).
:::
:::

::: {.idea}
Parts (a) and (b) are bookkeeping: every ring law holds value by value, and evaluation respects the operations value by value. Part (c) compares two ring homomorphisms \( R[x] \to R \) and uses the move just named: they agree on constants and on \( x \). Part (d) builds a polynomial with a factor vanishing at each element of \( R \), and the degree, computed by multiplying monic factors, shows it is not the zero polynomial.
:::

::: {.proof}
*(a)* The two rules define functions \( R \to R \), so \( + \) and \( \cdot \) are operations on \( R^R \). Each of (F1)–(F7) and (F9) is an equation between functions with domain and codomain \( R \), so by @fd2:prp-function-equality it suffices that the two sides agree at every \( c \in R \), and there it is the same law in \( R \): for example \( \bigl(f(g + h)\bigr)(c) = f(c)\bigl(g(c) + h(c)\bigr) = f(c)g(c) + f(c)h(c) = (fg + fh)(c) \). The zero is the constant function \( 0 \) by (F3) in \( R \), the negative of \( f \) is \( c \mapsto -f(c) \) by (F4), and the one is the constant function \( 1 \) by (F7).

*(b)* For \( p, q \in R[x] \) and \( c \in R \), @thm-evaluation-respects-operations gives \( \varepsilon(p + q)(c) = p(c) + q(c) = \bigl(\varepsilon(p) + \varepsilon(q)\bigr)(c) \) and likewise for products; and \( \varepsilon(1)(c) = 1 \). By @fd2:prp-function-equality, \( \varepsilon(p + q) = \varepsilon(p) + \varepsilon(q) \), \( \varepsilon(pq) = \varepsilon(p)\varepsilon(q) \), and \( \varepsilon(1) \) is the one of \( R^R \).

*(c)* Fix \( q \) and \( c \), and consider \( \alpha, \beta \colon R[x] \to R \), \( \alpha(p) \coloneqq (p \circ q)(c) \), \( \beta(p) \coloneqq p(q(c)) \). The map \( \alpha \) is the composite of \( p \mapsto p \circ q \) (a ring homomorphism, after @def-polynomial-composition) and evaluation at \( c \) (a ring homomorphism, @thm-evaluation-respects-operations), so it is one; \( \beta \) is evaluation at \( q(c) \), a ring homomorphism. On a constant \( a \), \( \alpha(a) = a(c) = a \) and \( \beta(a) = a \). On \( x \), \( \alpha(x) = q(c) \) and \( \beta(x) = x(q(c)) = q(c) \). By the uniqueness in @thm-polynomial-substitution (b), with \( S = R \), \( \varphi = \id_R \) and \( s = q(c) \), \( \alpha = \beta \).

*(d)* Since \( R \) is finite, there is a bijection \( j \mapsto c_j \) from \( \{1, \dots, r\} \) to \( R \) (@fd2:def-finite), and \( r \ge 1 \) because \( R \) contains \( 0 \). The product \( P \) is the product of a finite list in the commutative ring \( R[x] \) (@lem-finite-sums-and-powers (a)). Write \( P_j \coloneqq \prod_{i=1}^{j} (x - c_i) \), so \( P_0 = 1 \) and \( P_{j+1} = P_j \, (x - c_{j+1}) \). We show by induction on \( j \le r \) that \( P_j \) is monic of degree \( j \). The base: \( P_0 = 1 \) is monic of degree \( 0 \), as \( 1 \ne 0 \). The step: \( x - c_{j+1} \) has coefficients \( -c_{j+1}, 1, 0, \dots \), so it is monic of degree \( 1 \); by @thm-degree-of-product (b) in its monic case, \( P_{j+1} \) has degree \( j + 1 \) and leading coefficient \( 1 \cdot 1 = 1 \). So \( P = P_r \) has degree \( r \in \nN \), and \( P \ne 0 \).

Now let \( c \in R \); then \( c = c_l \) for some \( l \), by surjectivity. By @thm-evaluation-respects-operations, \( P_{j+1}(c) = P_j(c) \, (c - c_{j+1}) \), using \( (x - c_{j+1})(c) = c - c_{j+1} \) (the sum rule, with \( (-a)(c) = -a \) for a constant). At \( j + 1 = l \) the second factor is \( c_l - c_l = 0 \), so \( P_l(c) = 0 \), and each later step multiplies \( 0 \) by an element, so \( P_r(c) = 0 \) (@fd3:prp-ring-algebra (b) with (F6)). Hence \( \varepsilon(P) = \varepsilon(0) \) with \( P \ne 0 \), and \( \varepsilon \) is not injective.
:::

The smallest instance is the one this chapter opened with.

::: {#exm-polynomial-vs-function-f2}
[Different Polynomials, Equal Functions]

Over \( \nF_2 \), compare \( x^2 + x \) with \( 0 \), and \( x^2 \) with \( x \), first as polynomials, then as functions \( \nF_2 \to \nF_2 \).
:::

::: {.solution}
*As polynomials.* \( x^2 + x \) has coefficient \( 1 \ne 0 \) in position \( 1 \), so it is not the zero polynomial; it has degree \( 2 \). And \( x^2 \ne x \), since their coefficients differ in position \( 2 \) (and in position \( 1 \)).

*As functions.* At \( 0 \): \( 0^2 + 0 = 0 \) and \( 0^2 = 0 \). At \( 1 \): \( 1^2 + 1 = 1 + 1 = 0 \) in \( \nF_2 \) (@exm-finite-fields), and \( 1^2 = 1 \). So the function of \( x^2 + x \) is the zero function, and \( x^2 \) and \( x \) have the same function, the identity of \( \nF_2 \).

This is @prp-polynomial-function-map (d) with \( R = \nF_2 \), \( c_1 = 0 \), \( c_2 = 1 \): \( P = (x - 0)(x - 1) = x(x + 1) = x^2 + x \), since \( -1 = 1 \) in \( \nF_2 \).
:::

::: {.warning}
**A polynomial is not its function.** "\( p(c) = 0 \) for every \( c \in R \)" does not give \( p = 0 \): over every finite ring with \( 1 \ne 0 \) the polynomial \( P \) of @prp-polynomial-function-map (d) is a counterexample, and over \( \nF_2 \) it is \( x^2 + x \). Over \( \nQ \) the implication does hold: Chapter 5 proves it for every infinite field, by bounding the number of roots of a non-zero polynomial. Over \( \nZ \) it follows, though we do not prove it here: read \( p \in \nZ[x] \) as a polynomial with the same coefficients in \( \nQ[x] \), where it vanishes at infinitely many points. In this chapter, two polynomials are equal only when their coefficients are equal.
:::

## Exercises

### A. Check your understanding

::: {#exr-evaluation-and-substitution-a1}
[A1]

These questions are about @thm-polynomial-substitution and its proof, except the last.

::: {.enumerate options="label=(\alph*)"}
1. Where in the proof is \( \varphi(1) = 1 \) used?
2. Where is the commutativity of \( S \) used?
3. Run the theorem with \( R = \nZ \), \( S = \nZ/5\nZ \), \( \varphi \) the quotient map, \( s = [2] \) and \( p = x^2 + 3x + 1 \): compute \( \Phi(p) \). For the uniqueness half, explain why **any** ring homomorphism \( \Psi \) with \( \Psi(a) = [a] \) on constants and \( \Psi(x) = [2] \) must send \( 3x^2 \) to \( [2] \).
4. Give the idea of the proof in two sentences.
5. In \( \nF_3[x] \), compute the values of \( (x + 2)(x^2 + x + 1) \) at \( 0 \), \( 1 \), \( 2 \), and find all its roots in \( \nF_3 \).
:::
:::

::: {.solution}
(a) Twice: for \( \Phi(1) = \varphi(1) s^0 = 1 \), and for \( \Phi(x) = \varphi(1) s^1 = s \).

(b) Essentially once: in the monomial computation, to rewrite \( \varphi(a)\varphi(b) s^m s^n \) as \( \bigl(\varphi(a) s^m\bigr)\bigl(\varphi(b) s^n\bigr) \), which moves \( \varphi(b) \) past \( s^m \) by (F6) in \( S \). The proof also uses (F6) in \( S \) for \( 0 \cdot s^k = 0 \), for the right distributive law in the additivity steps, and for \( 1 \cdot s = s \); these uses only give the mirror forms of \( a \cdot 0 = 0 \), (F9) and (F7). An answer that lists them too, with this distinction, is correct.

(c) The coefficients of \( p \) are \( 1, 3, 1 \), so \( \Phi(p) = [1] + [3][2] + [1][2]^2 = [1 + 6 + 4] = [11] = [1] \). For the uniqueness half: \( 3x^2 \) is the product of the constant \( 3 \) and \( x^2 \) (@thm-polynomial-ring-laws (c)), so \( \Psi(3x^2) = \Psi(3)\Psi(x)^2 = [3][2]^2 = [12] = [2] \). No other value is possible, because \( \Psi \) respects products.

(d) A ring homomorphism out of \( R[x] \) has no freedom: it must send \( a x^n \) to \( \varphi(a) s^n \), so the formula is forced and uniqueness follows by additivity. The only work is to show that the forced formula respects products, and that is a check on monomials, where it becomes the power law and one reordering of factors in the commutative ring \( S \).

(e) Evaluation respects products (@thm-evaluation-respects-operations), so the value is the product of the values of the factors. At \( 0 \): \( 2 \cdot 1 = 2 \). At \( 1 \): \( (1 + 2)(1 + 1 + 1) = 0 \cdot 0 = 0 \). At \( 2 \): \( (2 + 2)(4 + 2 + 1) = 1 \cdot 1 = 1 \) (in \( \nF_3 \), \( 4 = 7 = 1 \)). So the only root is \( 1 \). Multiplied out by the product formula, the polynomial is \( x^3 + 3x^2 + 3x + 2 = x^3 + 2 \) in \( \nF_3[x] \), the second example after @def-polynomial-evaluation, whose values \( 2, 0, 1 \) agree.
:::

### B. Practice

::: {#exr-evaluation-and-substitution-b1}
[B1: The degree of a composition]

Let \( R \) be an integral domain, \( p, q \in R[x] \), \( p \ne 0 \), and \( \deg q \ge 1 \). Prove that \( \deg(p \circ q) = \deg p \cdot \deg q \). Show by an example that the hypothesis \( \deg q \ge 1 \) cannot be dropped.
:::

::: {.solution}
Let \( d \coloneqq \deg p \) and \( e \coloneqq \deg q \ge 1 \).

*Powers of \( q \).* By @fd1:ax-induction on \( k \), \( q^k \ne 0 \), \( \deg q^k = ke \) and \( \operatorname{lc}(q^k) = \operatorname{lc}(q)^k \). For \( k = 0 \), \( q^0 = 1 \) has degree \( 0 \) and leading coefficient \( 1 \) (as \( 1 \ne 0 \)). For the step, \( q^{k+1} = q^k q \), and since \( R \) has no zero divisors, @thm-degree-of-product (b) gives degree \( ke + e = (k + 1)e \) and leading coefficient \( \operatorname{lc}(q)^k \operatorname{lc}(q) \).

*The top term.* By @def-polynomial-composition with \( N = d \), \( p \circ q = \sum_{k=0}^{d} p_k q^k \). The term \( p_d q^d \) is the product of the non-zero constant \( p_d \) (degree \( 0 \)) and \( q^d \), so by @thm-degree-of-product (b) it has degree \( de \). Every other term \( p_k q^k \) with \( k < d \) is \( 0 \) or has degree \( ke < de \), since \( e \ge 1 \) (@thm-degree-of-product (a)). By @thm-degree-of-sum and induction along the sum recursion, \( r \coloneqq \sum_{k=0}^{d-1} p_k q^k \) has \( \deg r < de \) (for \( d = 0 \), \( r \) is the empty sum \( 0 \)). Then \( p \circ q = r + p_d q^d \), and the equality case of @thm-degree-of-sum gives \( \deg(p \circ q) = de \).

*The hypothesis on \( q \).* Take \( R = \nZ \), \( p = x - 1 \) and \( q = 1 \), of degree \( 0 \). Then \( p \circ q = 1 - 1 = 0 \), of degree \( -\infty \), while \( \deg p \cdot \deg q = 1 \cdot 0 = 0 \). A constant \( q \) can make the top terms cancel.
:::

::: {#exr-evaluation-and-substitution-b2}
[B2: All polynomials of degree at most two over the field with two elements]

List the elements of \( \nF_2[x]_{\le 2} \) with their degrees and their functions \( \nF_2 \to \nF_2 \) (given by the values at \( 0 \) and \( 1 \)). How many functions \( \nF_2 \to \nF_2 \) are there, and how many of the eight polynomials give each one?
:::

::: {.solution}
By @def-polynomials-bounded-degree, the elements are \( a_0 + a_1 x + a_2 x^2 \) with \( a_i \in \{0, 1\} \); there are eight (@exr-degree-b3 for \( \nF_2 \), \( n = 2 \)). The value at \( 0 \) is \( a_0 \), and the value at \( 1 \) is \( a_0 + a_1 + a_2 \) in \( \nF_2 \).
\[
\begin{array}{l|c|c|c}
p & \deg p & p(0) & p(1) \\ \hline
0 & -\infty & 0 & 0 \\
1 & 0 & 1 & 1 \\
x & 1 & 0 & 1 \\
x + 1 & 1 & 1 & 0 \\
x^2 & 2 & 0 & 1 \\
x^2 + 1 & 2 & 1 & 0 \\
x^2 + x & 2 & 0 & 0 \\
x^2 + x + 1 & 2 & 1 & 1
\end{array}
\]
A function \( \nF_2 \to \nF_2 \) is determined by its two values, so there are \( 2 \cdot 2 = 4 \) of them, and each occurs for exactly **two** polynomials in the table: \( (0, 0) \) for \( 0 \) and \( x^2 + x \); \( (1, 1) \) for \( 1 \) and \( x^2 + x + 1 \); \( (0, 1) \) for \( x \) and \( x^2 \); \( (1, 0) \) for \( x + 1 \) and \( x^2 + 1 \). In each pair the two polynomials differ by \( x^2 + x \), the polynomial of @exm-polynomial-vs-function-f2.
:::

::: {#exr-evaluation-and-substitution-b3}
[B3: Shifting the variable]

Let \( R \) be a commutative ring and \( c \in R \). Define \( T_c \colon R[x] \to R[x] \) by \( T_c(p) \coloneqq p \circ (x + c) \). Prove that \( T_c \) is a bijective ring homomorphism with inverse \( T_{-c} \).
:::

::: {.solution}
By @def-polynomial-composition, \( T_c \) is a ring homomorphism that fixes every constant and sends \( x \) to \( x + c \); likewise \( T_{-c} \) fixes constants and sends \( x \) to \( x - c \). The composite \( T_{-c} \circ T_c \) is a ring homomorphism (after @def-ring-homomorphism) that fixes constants, and
\[
T_{-c}(T_c(x)) = T_{-c}(x + c) = T_{-c}(x) + T_{-c}(c) = (x - c) + c = x .
\]
The identity map of \( R[x] \) is also a ring homomorphism that fixes constants and sends \( x \) to \( x \). By the uniqueness in @thm-polynomial-substitution (b), with \( S = R[x] \), \( \varphi \) the constants and \( s = x \), \( T_{-c} \circ T_c = \id_{R[x]} \). Exchanging \( c \) and \( -c \) (and \( -(-c) = c \)), \( T_c \circ T_{-c} = \id_{R[x]} \). So \( T_c \) has the inverse \( T_{-c} \), and is a bijection (@fd2:def-bijective).
:::

### C. Going deeper

::: {#exr-evaluation-and-substitution-c1}
[C1: Exit check: the substitution principle]

State and prove @thm-polynomial-substitution.
:::

::: {.solution}
*Statement.* Let \( R \) and \( S \) be commutative rings, \( \varphi \colon R \to S \) a ring homomorphism and \( s \in S \), and let \( \Phi(p) \coloneqq \sum_{k=0}^{N} \varphi(p_k) s^k \) for \( N \) admissible for \( p \). Then \( \Phi \colon R[x] \to S \) is a well-defined ring homomorphism with \( \Phi(a) = \varphi(a) \) for constants and \( \Phi(x) = s \), and it is the only ring homomorphism \( R[x] \to S \) with these two properties.

*Well defined.* Enlarging \( N \) by one adds the term \( \varphi(0) s^{k} = 0 \cdot s^k = 0 \), since \( \varphi(0) + \varphi(0) = \varphi(0) \) gives \( \varphi(0) = 0 \); by induction any two admissible \( N \) give the same sum. In particular \( \Phi(a x^m) = \varphi(a) s^m \), the other terms being \( 0 \).

*Additive.* With \( N \) admissible for \( p \) and \( q \), \( \Phi(p + q) = \sum_k \varphi(p_k + q_k) s^k = \sum_k \bigl(\varphi(p_k) s^k + \varphi(q_k) s^k\bigr) = \Phi(p) + \Phi(q) \), by additivity of \( \varphi \), (F9) and (F6) in \( S \), and (Σ1).

*Multiplicative.* The maps \( (p, q) \mapsto \Phi(pq) \) and \( (p, q) \mapsto \Phi(p)\Phi(q) \) are additive in \( p \) for fixed \( q \), and in \( q \) for fixed \( p \): the first because multiplication in \( R[x] \) distributes over addition and \( \Phi \) is additive, the second because \( \Phi \) is additive and multiplication in \( S \) distributes. On monomials,
\[
\Phi\bigl((ab) x^{m+n}\bigr) = \varphi(a)\varphi(b) s^m s^n = \bigl(\varphi(a) s^m\bigr)\bigl(\varphi(b) s^n\bigr) ,
\]
by multiplicativity of \( \varphi \), \( s^{m+n} = s^m s^n \), and (F5), (F6) in \( S \) to move \( \varphi(b) \) past \( s^m \). Since \( (a x^m)(b x^n) = (ab) x^{m+n} \), the two maps agree on pairs of monomials, so they agree everywhere by @lem-check-on-monomials.

*The one, constants and \( x \).* \( \Phi(1) = \varphi(1) s^0 = 1 \), \( \Phi(a x^0) = \varphi(a) \), and \( \Phi(x) = \varphi(1) s = s \).

*Uniqueness.* If \( \Psi \) is a ring homomorphism with \( \Psi(a x^0) = \varphi(a) \) and \( \Psi(x) = s \), then, as \( a x^n \) is the constant \( a \) times the \( n \)-th power of \( x \), \( \Psi(a x^n) = \varphi(a) s^n = \Phi(a x^n) \). Both maps are additive and agree on monomials, so \( \Psi = \Phi \) by @lem-check-on-monomials with one argument.

**Marking scheme.** (10 points)

- 1: gives the formula for \( \Phi \) and proves it does not depend on \( N \), from \( \varphi(0) = 0 \).
- 1: proves \( \Phi \) additive.
- 3: reduces multiplicativity to monomials (in one argument or in both), justifying the additivity it uses.
- 2: computes the monomial case correctly, justifying the reordering of factors in \( S \) (commutativity).
- 1: shows \( \Phi(1) = 1 \) and \( \Phi(x) = s \) (and \( \Phi(a) = \varphi(a) \)).
- 2: proves uniqueness: the values on monomials are forced, then additivity.

Fatal errors (0 for the step): proving multiplicativity only for \( p, q \) of degree at most \( 1 \); assuming that a homomorphism is determined by its value at \( x \) alone, without using \( \Psi(a) = \varphi(a) \) on constants. A proof of multiplicativity by expanding \( \Phi(p)\Phi(q) \) as a double sum and regrouping by \( i + j = k \) earns the 3 points of the reduction step only if the regrouping is proved.
:::

::: {#exr-evaluation-and-substitution-c2}
[C2: Composition is associative]

Let \( R \) be a commutative ring and \( p, q, r \in R[x] \). Prove that \( (p \circ q) \circ r = p \circ (q \circ r) \).

The first half of a proof is given.

> Fix \( q \) and \( r \). Both sides are additive in \( p \): the left side is \( p \mapsto p \circ q \) followed by \( u \mapsto u \circ r \), two ring homomorphisms (@def-polynomial-composition), and the right side is \( p \mapsto p \circ (q \circ r) \), a ring homomorphism.

The second half is blank. *Name the move, then complete it.*
:::

::: {.solution}
One move is **check on monomials, extend by additivity**.

Let \( p = a x^n \). Since \( u \mapsto u \circ q \) is a ring homomorphism fixing the constant \( a \) and sending \( x \) to \( q \), and \( a x^n \) is the product of \( a \) and \( x^n \) (@thm-polynomial-ring-laws (c)),
\[
(a x^n) \circ q = (a \circ q)(x \circ q)^n = a q^n ,
\]
by the power property of ring homomorphisms (after @def-ring-homomorphism). Applying the ring homomorphism \( u \mapsto u \circ r \) in the same way,
\[
(a q^n) \circ r = (a \circ r)(q \circ r)^n = a \, (q \circ r)^n .
\]
On the other side, the same computation with \( q \circ r \) in place of \( q \) gives \( (a x^n) \circ (q \circ r) = a \, (q \circ r)^n \). So the two sides agree on every monomial. Both are additive in \( p \), so by @lem-check-on-monomials (with one argument and \( T = R[x] \)) they agree for every \( p \).

Also correct: the move **a homomorphism out of \( R[x] \) is fixed by the constants and \( x \)**. Both sides are ring homomorphisms \( R[x] \to R[x] \) (composites of ring homomorphisms, after @def-ring-homomorphism), both fix every constant (\( (a \circ q) \circ r = a \circ r = a \) and \( a \circ (q \circ r) = a \)), and both send \( x \) to \( q \circ r \): \( (x \circ q) \circ r = q \circ r \) and \( x \circ (q \circ r) = q \circ r \). So they are equal by the uniqueness in @thm-polynomial-substitution (b), with \( S = R[x] \), \( \varphi \colon a \mapsto a x^0 \) and \( s = q \circ r \).
:::

::: {#exr-evaluation-and-substitution-c3}
[C3: The factor theorem over any commutative ring]

Let \( R \) be a commutative ring and \( c \in R \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that for every \( n \ge 1 \),
\[
x^n - c^n = (x - c) \sum_{j=0}^{n-1} c^{\,n-1-j} x^j .
\]
2. Prove that for \( p \in R[x] \), \( p(c) = 0 \) if and only if \( p = (x - c) q \) for some \( q \in R[x] \).
3. In \( \nZ/8\nZ \), find all roots of \( x^2 - 1 \). The usual argument that a quadratic polynomial cannot have more than two roots goes: "if \( c_1 \) is a root, then \( p = (x - c_1) q \) with \( \deg q = 1 \); a second root \( c_2 \ne c_1 \) has \( (c_2 - c_1) q(c_2) = 0 \), so \( q(c_2) = 0 \)". Which step fails in \( \nZ/8\nZ \)?
:::
:::

::: {.solution}
[Hint 1]

For (a), compare coefficients: multiplying a polynomial by \( x \) shifts its coefficients up by one place (@lem-monomial-product (a)). For (b) \( (\Rightarrow) \), reduce to (a).
:::

::: {.solution}
[Hint 2]

For (b), let \( N \) be admissible for \( p \) and start from \( p - p(c) = \sum_{k=0}^{N} p_k x^k - \sum_{k=0}^{N} p_k c^k \), with \( p(c) \) read as a constant.
:::

::: {.solution}
(a) Let \( u \coloneqq \sum_{j=0}^{n-1} c^{\,n-1-j} x^j \), so \( u_j = c^{\,n-1-j} \) for \( 0 \le j \le n - 1 \) and \( u_j = 0 \) for \( j \ge n \). By @lem-monomial-product (a) and @thm-polynomial-ring-laws (d), \( (x - c)u = xu - cu \) has coefficient \( -c u_0 \) at \( 0 \) and \( u_{k-1} - c u_k \) at \( k \ge 1 \). So:

- at \( k = 0 \): \( -c \cdot c^{n-1} = -c^n \);
- at \( 1 \le k \le n - 1 \): \( c^{\,n-k} - c \cdot c^{\,n-1-k} = 0 \), by the power law;
- at \( k = n \): \( u_{n-1} - c u_n = c^0 - 0 = 1 \);
- at \( k > n \): \( 0 - 0 = 0 \).

These are the coefficients of \( x^n - c^n \). This is *Analytic Preliminaries*, Chapter 1's difference-of-powers identity (@fd4:lem-difference-of-powers), read in the commutative ring \( R[x] \) with \( z = x \) and \( w = c \); the proof above does not use it.

(b) \( (\Leftarrow) \) By @thm-evaluation-respects-operations, \( p(c) = (c - c)\, q(c) = 0 \cdot q(c) = 0 \).

\( (\Rightarrow) \) Let \( N \) be admissible for \( p \). By @prp-polynomial-sum-of-monomials and @thm-polynomial-ring-laws (b), (c), and since the constants respect sums,
\[
\begin{aligned}
p - p(c) &= \sum_{k=0}^{N} p_k x^k - \sum_{k=0}^{N} p_k c^k \\
&= \sum_{k=1}^{N} p_k \bigl(x^k - c^k\bigr) ,
\end{aligned}
\]
where the term \( k = 0 \) is \( p_0 (1 - 1) = 0 \). By (a), each \( x^k - c^k \) with \( k \ge 1 \) is \( (x - c) u^{(k)} \) for a polynomial \( u^{(k)} \), so by the distributive law \( p - p(c) = (x - c) q \) with \( q \coloneqq \sum_{k=1}^{N} p_k u^{(k)} \). If \( p(c) = 0 \), then \( p = (x - c) q \).

(c) The squares in \( \nZ/8\nZ \) of \( [0], \dots, [7] \) are \( [0], [1], [4], [1], [0], [1], [4], [1] \) (for instance \( [5]^2 = [25] = [1] \), \( [7]^2 = [49] = [1] \)). So \( x^2 - 1 \) has the four roots \( [1], [3], [5], [7] \). The failing step is "\( (c_2 - c_1) q(c_2) = 0 \), so \( q(c_2) = 0 \)": it needs \( \nZ/8\nZ \) to have no zero divisors. With \( c_1 = [1] \), \( q = x + 1 \) and \( c_2 = [3] \), \( (c_2 - c_1) q(c_2) = [2][4] = [8] = [0] \), with both factors non-zero.

Chapter 5 proves the factor theorem over a field again, by division with remainder.
:::

::: {#exr-evaluation-and-substitution-c4}
[C4: A second proof of Fermat's little theorem]

Let \( p \) be a prime. Give another proof that \( a^{p-1} = 1 \) for every non-zero \( a \in \nF_p \), along the following steps, and then compare \( x^p - x \) with its function.

::: {.enumerate options="label=(\alph*)"}
1. Let \( a \in \nF_p \) be non-zero. Show that \( b \mapsto ab \) is a bijection from \( \nF_p \setminus \{0\} \) to itself.
2. Deduce that \( a^{p-1} = 1 \), by computing the product of all non-zero elements of \( \nF_p \) in two ways.
3. Show that \( x^p - x \ne 0 \) in \( \nF_p[x] \), but \( \varepsilon(x^p - x) = 0 \).
:::
:::

::: {.solution}
Write \( F \coloneqq \nF_p \), a field (@def-field-fp); then \( F \setminus \{0\} \) has the \( p - 1 \) elements \( 1, \dots, p - 1 \) (@thm-integers-mod-n-ring (b)).

(a) For \( b \in F \setminus \{0\} \), \( ab \ne 0 \), since \( F \) has no zero divisors (@thm-field-basic-properties (f)); so \( b \mapsto ab \) maps \( F \setminus \{0\} \) to \( F \setminus \{0\} \). It is injective: \( ab = ab' \) gives \( a(b - b') = 0 \), so \( b = b' \). Its image is a subset of the finite set \( F \setminus \{0\} \) in bijection with \( F \setminus \{0\} \); if the image were a proper subset, this would contradict @fd2:thm-finite-no-proper-copy. So the map is surjective, hence a bijection.

(b) *A rearranged product is the same product.* For a list \( t_1, \dots, t_r \) in a commutative ring and a bijection \( \sigma \) of \( \{1, \dots, r\} \), we show \( \prod_{j=1}^{r} t_{\sigma(j)} = \prod_{j=1}^{r} t_j \), by @fd1:ax-induction on \( r \). For \( r = 0 \) both sides are the empty product \( 1 \). For the step, first a deletion rule: for a list \( u_1, \dots, u_{r+1} \) and a position \( k \), the product equals \( u_k \) times the product of the list with position \( k \) deleted. For \( k = r + 1 \) this is the product recursion; for \( k \le r \), it follows from the rule for the first \( r \) entries (induction on the length) and (F5), (F6):
\[
\begin{aligned}
\prod_{j=1}^{r+1} u_j = \Bigl(\prod_{j=1}^{r} u_j\Bigr) u_{r+1} &= \Bigl(\bigl(\textstyle\prod_{j \le r,\, j \ne k} u_j\bigr) u_k\Bigr) u_{r+1} \\
&= \Bigl(\bigl(\textstyle\prod_{j \le r,\, j \ne k} u_j\bigr) u_{r+1}\Bigr) u_k ,
\end{aligned}
\]
and the bracket in the last line is the product of the list with position \( k \) deleted, by the product recursion, since that list ends with \( u_{r+1} \). Now let \( u_j \coloneqq t_{\sigma(j)} \) and \( k \coloneqq \sigma^{-1}(r + 1) \). Deleting position \( k \) leaves the list \( t_{\sigma'(1)}, \dots, t_{\sigma'(r)} \), where \( \sigma'(i) \coloneqq \sigma(i) \) for \( i < k \) and \( \sigma'(i) \coloneqq \sigma(i + 1) \) for \( i \ge k \), a bijection of \( \{1, \dots, r\} \): its values lie in \( \{1, \dots, r\} \), since \( \sigma(m) = r + 1 \) only for \( m = k \) and the index used (\( i \) for \( i < k \), \( i + 1 \) for \( i \ge k \)) is never \( k \); it is injective because \( \sigma \) and this index map are; and every \( j \le r \) is \( \sigma(m) \) for some \( m \ne k \), so \( j = \sigma'(m) \) if \( m < k \) and \( j = \sigma'(m - 1) \) if \( m > k \). By the deletion rule and the hypothesis for \( r \), \( \prod_{j=1}^{r+1} t_{\sigma(j)} = \bigl(\prod_{i=1}^{r} t_i\bigr) t_{r+1} = \prod_{j=1}^{r+1} t_j \).

*The two computations.* List \( F \setminus \{0\} \) as \( b_1, \dots, b_{p-1} \), and let \( Q \coloneqq \prod_{j=1}^{p-1} b_j \). By (a), \( a b_j = b_{\sigma(j)} \) for a bijection \( \sigma \) of \( \{1, \dots, p - 1\} \), so the list \( a b_1, \dots, a b_{p-1} \) is a rearrangement of \( b_1, \dots, b_{p-1} \), and its product is \( Q \). By (F5), (F6) and induction on the length, the same product is \( a^{p-1} Q \). So \( a^{p-1} Q = Q = 1 \cdot Q \). Since \( Q \) is a product of non-zero elements of a field, \( Q \ne 0 \) (@thm-field-basic-properties (f), by induction), and canceling \( Q \) (@thm-field-basic-properties (b)) gives \( a^{p-1} = 1 \).

(c) The polynomial \( x^p - x \) has coefficient \( 1 \) at position \( p \) (since \( p \ge 2 \), the positions \( p \) and \( 1 \) differ), and \( 1 \ne 0 \) in \( F \); so it is not the zero polynomial. For every \( c \in F \), \( c^p - c = 0 \): if \( c \ne 0 \), \( c^p = c^{p-1} c = c \) by (b); and \( 0^p = 0 \) since \( p \ge 1 \). So \( \varepsilon(x^p - x) \) is the zero function. This gives a second proof, by Fermat rather than by the factors \( x - c \), that \( \varepsilon \) is not injective over \( \nF_p \). The two witnesses are in fact the same polynomial: Chapter 5 shows that \( x^p - x = \prod_{c \in \nF_p} (x - c) \), the \( P \) of @prp-polynomial-function-map (d) with \( R = \nF_p \) (@exm-polynomial-function-finite-field (b)).

This is the second proof of @thm-fermat-little (b); the first, in Chapter 2, went through the Frobenius map. Part (c) also follows directly from @thm-fermat-little (a).
:::

<!-- dependency ledger
def-polynomial-evaluation (claim): well defined: enlarging N adds 0 . c^k = 0 | sum recursion of lem-finite-sums-and-powers (a), fd3:prp-ring-algebra (b), (F3), induction on j (fd1:ax-induction through fd3:cor-omega-identification (b)); written out
def-polynomial-evaluation (example): x^2 - 3x + 2 at 0, 1, 2 is 2, 0, 0; x^3 + 2 over F_3 at 0, 1, 2 is 2, 0, 1 | arithmetic in Q and F_3; verify/ch04/def-polynomial-evaluation.py
def-polynomial-evaluation (example): value of a monomial a x^m is a c^m | (Sigma3) of lem-finite-sums-and-powers (b) (cited), fd3:prp-ring-algebra (b)
def-polynomial-evaluation (claim): (warning) p_2 = 1, p(2) = 0, p_0 = p(0) = 2 | verify/ch04/def-polynomial-evaluation.py
thm-evaluation-respects-operations (proof): common admissible N | max of two admissible N is admissible; order of N (fd3:thm-omega-order), used silently
thm-evaluation-respects-operations (claim): (remark) polynomials of a square matrix, linear-algebra companion (its Chapter 0) | companion (LA1.0), prose pointer; nothing depends on it
thm-evaluation-respects-operations (claim): (x - 1)(x - 2) = x^2 - 3x + 2 in Q[x] | product formula; verify/ch04/def-polynomial-evaluation.py
thm-evaluation-respects-operations (claim): roots of (x - 1)(x - 2) in Q are exactly 1, 2 | exm-integral-domains (cited); sum rule and value of a constant (cited)
def-ring-homomorphism (claim): phi(s^n) = phi(s)^n | induction on n, written out; power recursion of lem-finite-sums-and-powers (c)
def-ring-homomorphism (claim): between fields it is def-field-homomorphism; the consequences are the ring versions of prp-field-homomorphism-properties (a), (e) (composites), (f) (powers); (b)-(d) fail since Z -> Z/nZ is not injective | def-field-homomorphism, prp-field-homomorphism-properties (prose comparison; the consequences are proved here); exm-ring-homomorphisms (i)
exm-ring-homomorphisms (solution): Z/mZ x Z/nZ is a commutative ring componentwise | each axiom componentwise (thm-chinese-remainder-two (b) takes the componentwise operations); stated, one line
exm-ring-homomorphisms (claim): complex conjugation, rules proved in F4.1; used in a review exercise of the next section | F4.1 (def-conjugate-modulus, thm-conjugate-properties; blueprint ch01.md), backward prose pointer; the review exercise R2 of the chapter's last section (within the chapter); nothing here depends on it
thm-polynomial-substitution (claim): (try it first / idea) 3x^2 + 1 -> [3][2][2] + [1] = [13] = [3] in Z/5Z | verify/ch04/thm-polynomial-substitution.py
thm-polynomial-substitution (claim): (answer to prompt) commutativity of S used essentially once (monomial line); other (F6) uses only mirror (F7), (F9), a . 0 = 0; phi(1) = 1 used twice (Phi(1), Phi(x)) | meta-claim about the proof on the page; checkable line by line; well-definedness uses phi(0) = 0, which follows from additivity alone
thm-polynomial-substitution (claim): (answer to prompt) noncommutative S: proof goes through if s commutes with every phi(b) | the monomial line is the only use of (F6) in S beyond the mirror forms of (F7), (F9) and a . 0 = 0, which two-sided ring axioms give directly; (F5) and the power law hold without commutativity; prose
cor-polynomial-coefficient-change (claim): 2x^2 + 3x - 1 -> x + 1 over F_2; 6x^3 + 5x^2 + x -> [5]x^2 + x mod 6 | arithmetic mod 2 and mod 6; verify/ch04/cor-polynomial-coefficient-change.py
cor-polynomial-coefficient-change (claim): the algebra volumes reduce integer polynomials modulo a prime to test factorization | AL2.6 (prose pointer, no chapter number); nothing depends on it
cor-polynomial-coefficient-change (claim): composition is used in Section 4.5 | ch04 §05 cites def-polynomial-composition; forward pointer within the chapter; nothing here depends on it
def-polynomial-composition (claim): (x^2 + 1) o (x + 1) = x^2 + 2x + 2; (x + 1)^2 = x^2 + 2x + 1; (-x)^k = (-1)^k x^k | product formula; (-x)^k by the power law (st)^n = s^n t^n of lem-finite-sums-and-powers (c) with -x = (-1)x (fd3:prp-ring-algebra (c)); verify/ch04/def-polynomial-composition.py
def-polynomial-composition (claim): p(-x) is the map sigma of exr-polynomial-ring-b2 | prose comparison with an earlier exercise; no proof rests on it
prp-polynomial-function-map (proof): (a) pointwise axioms | fd2:prp-function-equality (cited) and (F1)-(F7), (F9) of R
prp-polynomial-function-map (proof): (d) r >= 1 since R contains 0; x - c has coefficients -c, 1 | fd2:def-finite (cited); def-polynomial-ring (sum of x and the constant -c), used silently
prp-polynomial-function-map (proof): (d) induction on j for P_j monic of degree j, and P_j(c) = 0 for j >= l | fd1:ax-induction (through fd3:cor-omega-identification (b)), product recursion of lem-finite-sums-and-powers (a)
prp-polynomial-function-map (proof): (d) (-a)(c) = -a for a constant | value of a constant (example after def-polynomial-evaluation)
exm-polynomial-vs-function-f2 (solution): 1 + 1 = 0 and -1 = 1 in F_2 | exm-finite-fields (cited)
exm-polynomial-vs-function-f2 (claim): (warning) F5.5 proves p(c) = 0 for all c implies p = 0 over infinite fields | F5.5 (forward prose pointer; blueprint ch05.md thm-polynomial-identity-from-values); nothing here depends on it
exm-polynomial-vs-function-f2 (claim): (warning) the same over Z, via Q[x] | not proved here (marked in the text); nothing depends on it
exr-evaluation-and-substitution-a1 (solution): [1 + 6 + 4] = [11] = [1]; [3][2]^2 = [12] = [2]; values 2, 0, 1 in F_3; (x + 2)(x^2 + x + 1) = x^3 + 3x^2 + 3x + 2 = x^3 + 2 | verify/ch04/exr-evaluation-and-substitution-a1.py
exr-evaluation-and-substitution-b1 (solution): deg q^k = k deg q by induction; ke < de for k < d, e >= 1 | fd1:ax-induction; order of N (fd3:thm-omega-order, fd3:prp-ordered-ring-rules (c) in Z), used silently
exr-evaluation-and-substitution-b2 (solution): table of F_2[x]_{<=2}; 4 functions, two polynomials each | verify/ch04/exr-evaluation-and-substitution-b2.py; count 2 . 2 = 4 by fd2:exr-finite-sets-c2 (b), used silently
exr-evaluation-and-substitution-c3 (solution): coefficients of (x - c)u; squares mod 8; [2][4] = [8] = [0] | verify/ch04/exr-evaluation-and-substitution-c3.py
exr-evaluation-and-substitution-c3 (solution): sum_k p_k x^k - sum_k p_k c^k = sum_k p_k (x^k - c^k) | (Sigma1), (Sigma4) of lem-finite-sums-and-powers (b), thm-polynomial-ring-laws (b) (constants respect sums), used silently
exr-evaluation-and-substitution-c3 (claim): F5.5 proves the factor theorem by division | F5.5 (forward prose pointer; blueprint ch05.md); nothing depends on it
exr-evaluation-and-substitution-c3 (claim): (a) is *Analytic Preliminaries*, Chapter 1's difference-of-powers identity in R[x] | lem-difference-of-powers (F4.1, see edge; prose comparison, no step rests on it)
exr-evaluation-and-substitution-c4 (solution): order-independence of a finite product in a commutative ring | proved inline by induction on the length (blueprint open question 4)
exr-evaluation-and-substitution-c4 (solution): Q != 0 for a product of non-zero elements; cancellation | thm-field-basic-properties (b), (f) (cited), induction on the length
exr-evaluation-and-substitution-c4 (solution): the first proof of Fermat in F5.2 via Frobenius | thm-fermat-little (cited), F5.2 §06 (backward pointer)
exr-evaluation-and-substitution-c4 (claim): x^p - x is the P of prp-polynomial-function-map (d) over F_p | F5.5 exm-polynomial-function-finite-field (b) (cited), forward pointer; nothing here depends on it
-->
