# The Polynomial Ring

Section 4.1 made a polynomial a coefficient sequence, and the display \( \sum_k p_k x^k \) only a way of writing it down. This section gives the sequences their sum and product, read off from what school algebra does with expressions, and proves that the result obeys every law of @fd3:def-commutative-ring-and-field. The obvious proof of associativity needs a theorem about reordering double sums that we have not proved. We avoid it with one device, **check on monomials, extend by additivity**, which returns in Sections 4.4 and 4.5.

Throughout, \( R \) is a commutative ring and \( R[x] \) is the set of polynomials over \( R \) (@def-polynomial).

## Adding and multiplying coefficient sequences

At school, \( (3x^2 - x + 2)(x + 1) \) is computed by multiplying every term of the first factor by every term of the second, using \( a_i x^i \cdot b_j x^j = a_i b_j x^{i+j} \), and then collecting the terms with the same power. The coefficient of \( x^k \) in the result collects the products \( a_i b_j \) over all pairs with \( i + j = k \), that is, over \( i = 0, \dots, k \) with \( j = k - i \). Addition collects like powers too, so it adds coefficients position by position. We turn these two recipes into definitions.

*Add position by position; multiply by collecting, in position \( k \), every product of a coefficient from position \( i \) with one from position \( k - i \).*

::: {#def-polynomial-ring}
[The Polynomial Ring]

Let \( R \) be a commutative ring. For \( p, q \in R[x] \) and \( k \in \nN \) define
\[
(p + q)_k \coloneqq p_k + q_k , \qquad (-p)_k \coloneqq -p_k , \qquad (pq)_k \coloneqq \sum_{i=0}^{k} p_i \, q_{k-i} .
\]
The set \( R[x] \) with this addition and this multiplication is the **polynomial ring** over \( R \).
:::

In words: the sum and the negative act on each position separately. The product is the **convolution** of the two sequences: its entry in position \( k \) is a sum of \( k + 1 \) products in \( R \), and the two positions in each product add up to \( k \). For \( i \le k \), the index \( k - i \) lies in \( \nN \), computed in \( \nZ \supseteq \nN \) (@fd3:prp-naturals-embed-integers); the sum is a finite sum in \( R \) (@lem-finite-sums-and-powers (a)). The name "ring" is a promise: the theorem at the end of this section keeps it.

**The operations stay inside \( R[x] \).** There is something to check: the three formulas produce sequences \( \nN \to R \), and we must see that only finitely many of their entries are non-zero. Let \( m \) be admissible for \( p \) and \( n \) admissible for \( q \).

- For \( k > \max(m, n) \), \( (p + q)_k = 0 + 0 = 0 \) by (F3). So \( \max(m, n) \) is admissible for \( p + q \).
- For \( k > m \), \( (-p)_k = -0 = 0 \), since \( 0 + 0 = 0 \) and negatives are unique (@fd3:prp-ring-algebra (a)). So \( m \) is admissible for \( -p \).
- Let \( k > m + n \) and \( 0 \le i \le k \). If \( i > m \), then \( p_i = 0 \). If \( i \le m \), then \( k - i \ge k - m > n \), so \( q_{k-i} = 0 \). Either way the term \( p_i q_{k-i} \) is \( 0 \), by @fd3:prp-ring-algebra (b) with (F6). A sum whose terms are all \( 0 \) is \( 0 \) (@lem-finite-sums-and-powers (b), (Σ3) with \( j = k + 1 \)), so \( (pq)_k = 0 \), and \( m + n \) is admissible for \( pq \).

So \( + \) and \( \cdot \) are functions \( R[x] \times R[x] \to R[x] \), and \( p \mapsto -p \) is a function \( R[x] \to R[x] \). The bound \( m + n \) is the first hint of the degree of a product, the subject of Section 4.3.

::: {#exm-polynomial-product}
[A product, coefficient by coefficient]

Compute \( (3x^2 - x + 2)(x + 1) \) from @def-polynomial-ring in \( \nQ[x] \), in \( \nF_3[x] \) and in \( (\nZ/6\nZ)[x] \).
:::

::: {.solution}
In \( \nQ[x] \), let \( p = 3x^2 - x + 2 \) and \( q = x + 1 \), so \( (p_0, p_1, p_2) = (2, -1, 3) \) and \( (q_0, q_1) = (1, 1) \), all other coefficients \( 0 \). Then \( 2 \) is admissible for \( p \) and \( 1 \) for \( q \), so \( (pq)_k = 0 \) for \( k \ge 4 \) by the closure argument, and
\[
\begin{aligned}
(pq)_0 &= p_0 q_0 = 2 , \\
(pq)_1 &= p_0 q_1 + p_1 q_0 = 2 - 1 = 1 , \\
(pq)_2 &= p_0 q_2 + p_1 q_1 + p_2 q_0 = 0 - 1 + 3 = 2 , \\
(pq)_3 &= p_0 q_3 + p_1 q_2 + p_2 q_1 + p_3 q_0 = 0 + 0 + 3 + 0 = 3 .
\end{aligned}
\]
Hence \( pq = 3x^3 + 2x^2 + x + 2 \), as expanding by hand gives.

In \( \nF_3[x] \) the same display names other coefficients: \( 3 = 0 \) and \( -1 = 2 \) in \( \nF_3 \), so \( (p_0, p_1, p_2) = (2, 2, 0) \), and \( p = 2x + 2 \). The formula gives \( (pq)_0 = 2 \), \( (pq)_1 = 2 + 2 = 4 = 1 \), \( (pq)_2 = 0 + 2 + 0 = 2 \), and \( (pq)_3 = 0 \). So \( pq = 2x^2 + x + 2 \) in \( \nF_3[x] \).

In \( (\nZ/6\nZ)[x] \), \( (p_0, p_1, p_2) = ([2], [5], [3]) \), since \( [-1] = [5] \). The formula gives \( [2] \), \( [2] + [5] = [7] = [1] \), \( [5] + [3] = [8] = [2] \) and \( [3] \). So \( pq = [3]x^3 + [2]x^2 + x + [2] \).

Each answer over \( \nF_3 \) and \( \nZ/6\nZ \) is the answer over \( \nQ \) with every integer coefficient replaced by its class. Section 4.4 explains why this always happens.
:::

::: {.warning}
**The product is not taken position by position.** The rule \( (pq)_k = p_k q_k \) looks like the natural partner of the sum, but it is not the product of school algebra. For \( p = q = x = (0, 1, 0, \dots) \) it would give \( (0, 1, 0, \dots) \), that is, \( x \cdot x = x \). The convolution gives \( (x \cdot x)_2 = x_0 x_2 + x_1 x_1 + x_2 x_0 = 0 + 1 + 0 = 1 \) and \( (x \cdot x)_k = 0 \) for \( k \ne 2 \), so \( x \cdot x = x^2 \), as it should be. Only the sum is coefficientwise.
:::

## Monomials do the work

The display \( \sum_k p_k x^k \) of Section 4.1 can now be read as a genuine sum in \( R[x] \). The sum is formed with the addition just defined, by @lem-finite-sums-and-powers (a) with \( T = R[x] \). That part of the lemma asks only for a function \( + \colon T \times T \to T \) and an element \( 0 \) with \( 0 + u = u \); in \( R[x] \) the zero polynomial is such an element, since \( (0 + u)_k = 0 + u_k = u_k \) by (F1) and (F3). We do not yet know any other law of \( R[x] \), and the next proposition needs none.

::: {#prp-polynomial-sum-of-monomials}
[A Polynomial Is the Sum of Its Monomials]

Let \( p \in R[x] \) and \( N \in \nN \). The sum \( \sum_{k=0}^{N} p_k x^k \) of the monomials \( p_k x^k \), formed in \( (R[x], +) \), has coefficient \( p_j \) in position \( j \) for every \( j \le N \), and \( 0 \) in every position \( j > N \). In particular, if \( N \) is admissible for \( p \), then
\[
p = \sum_{k=0}^{N} p_k x^k .
\]
:::

::: {.proof}
Write \( s_N \coloneqq \sum_{k=0}^{N} p_k x^k \). We use @fd1:ax-induction on \( N \). For \( N = 0 \), \( s_0 = p_0 x^0 \), which has \( p_0 \) in position \( 0 \) and \( 0 \) elsewhere (@def-polynomial). Suppose \( s_N \) has the stated coefficients. By the recursion of @lem-finite-sums-and-powers (a), \( s_{N+1} = s_N + p_{N+1} x^{N+1} \), so by @def-polynomial-ring its \( j \)-th coefficient is \( (s_N)_j + (p_{N+1} x^{N+1})_j \). This is \( p_j + 0 = p_j \) for \( j \le N \); it is \( 0 + p_{N+1} = p_{N+1} \) for \( j = N + 1 \); and it is \( 0 + 0 = 0 \) for \( j > N + 1 \), by (F1) and (F3). These are the stated coefficients for \( N + 1 \).

If \( N \) is admissible for \( p \), then \( p_j = 0 \) for \( j > N \), so \( p \) and \( s_N \) agree in every position, and \( p = s_N \) by @fd2:prp-function-equality. This proves the proposition.
:::

So the display of @def-polynomial is now an honest sum: \( 3x^2 - x + 2 \) is the sum, in \( (R[x], +) \), of the monomials \( 2x^0 \), \( (-1)x^1 \) and \( 3x^2 \). Every polynomial is a finite sum of monomials.

Next we multiply by a monomial. Multiplying by \( a x^m \) should move every coefficient \( m \) places up and multiply it by \( a \).

::: {#lem-monomial-product}
[Multiplying by a Monomial]

Let \( a, b \in R \), \( m, n \in \nN \) and \( q \in R[x] \).

::: {.enumerate options="label=(\alph*)"}
1. \( \bigl( (a x^m) q \bigr)_k = a \, q_{k-m} \) for \( k \ge m \), and \( \bigl( (a x^m) q \bigr)_k = 0 \) for \( k < m \).
2. \( (a x^m)(b x^n) = (ab) \, x^{m+n} \).
:::
:::

::: {.proof}
(a) By @def-polynomial-ring, \( \bigl( (a x^m) q \bigr)_k = \sum_{i=0}^{k} (a x^m)_i \, q_{k-i} \). For \( i \ne m \), \( (a x^m)_i = 0 \), so the \( i \)-th term is \( 0 \cdot q_{k-i} = 0 \) (@fd3:prp-ring-algebra (b) with (F6)). By (Σ3) of @lem-finite-sums-and-powers (b) with \( j = m \), the sum is the term with \( i = m \), namely \( a \, q_{k-m} \), when \( m \le k \), and \( 0 \) when \( m > k \).

(b) Apply (a) with \( q = b x^n \). For \( k < m \) the coefficient is \( 0 \). For \( k \ge m \) it is \( a \, (b x^n)_{k-m} \), which is \( ab \) when \( k - m = n \), that is, when \( k = m + n \), and \( a \cdot 0 = 0 \) otherwise. Since \( k < m \) implies \( k \ne m + n \), the product has \( ab \) in position \( m + n \) and \( 0 \) elsewhere: it is the monomial \( (ab) x^{m+n} \).
:::

Part (b) is the school rule \( a x^m \cdot b x^n = ab \, x^{m+n} \), now a theorem about sequences. It contains everything multiplication does: the next lemma shows that a law which holds on monomials, and which survives sums in each argument, holds everywhere.

**Additivity in each argument.** For all \( p, p', q, q' \in R[x] \),
\[
(p + p') q = pq + p'q \tag{$\ast$}
\]
\[
p (q + q') = pq + pq' . \tag{$\ast\ast$}
\]
For (\( \ast \)), the \( k \)-th coefficient of the left side is
\[
\sum_{i=0}^{k} (p_i + p'_i) \, q_{k-i} = \sum_{i=0}^{k} \bigl( p_i q_{k-i} + p'_i q_{k-i} \bigr) = \sum_{i=0}^{k} p_i q_{k-i} + \sum_{i=0}^{k} p'_i q_{k-i} ,
\]
where the first equality applies (F6), (F9) and (F6) again inside each term, and the second is (Σ1). The right side is the \( k \)-th coefficient of \( pq + p'q \). For (\( \ast\ast \)) the same computation runs with \( p_i (q_{k-i} + q'_{k-i}) = p_i q_{k-i} + p_i q'_{k-i} \), which is (F9) itself. Each sum has a single index \( i \), and no term is moved past another. So each distributive law is one line of algebra in \( R \), with compare coefficients doing the rest.

A map of several polynomial arguments is **additive in each argument** if, whenever one argument is replaced by a sum \( u + u' \) and the others are held fixed, the value is the sum of the two values. By (\( \ast \)) and (\( \ast\ast \)), the product \( (p, q) \mapsto pq \) is additive in each argument. Here is what that buys.

::: {#lem-check-on-monomials}
[Check on Monomials]

Let \( R \) be a commutative ring, let \( T \) be a set with a function \( + \colon T \times T \to T \), and let \( m \in \{1, 2, 3\} \). Let \( \Phi, \Psi \colon R[x]^m \to T \) be maps that are **additive in each argument**: for each position \( j \le m \) and **all** fixed values of the other arguments,
\[
\Phi(\dots, u + u', \dots) = \Phi(\dots, u, \dots) + \Phi(\dots, u', \dots)
\]
with \( u, u' \) in position \( j \), and the same for \( \Psi \). If \( \Phi(u_1, \dots, u_m) = \Psi(u_1, \dots, u_m) \) whenever **every** \( u_j \) is a monomial, then \( \Phi = \Psi \).
:::

Here \( R[x]^1 = R[x] \), and \( R[x]^2 \), \( R[x]^3 \) are the sets of pairs and triples. The proof uses no law of \( T \) at all, not even associativity of its addition, and no product on \( T \). That is why it may be applied with \( T = R[x] \) inside the proof that \( R[x] \) is a ring.

::: {.idea}
Every polynomial is a finite sum of monomials (@prp-polynomial-sum-of-monomials), so a map that is additive is fixed by what it does to monomials: peel off the top monomial and induct. With several arguments, unlock them one at a time: first let the last argument be arbitrary while the others stay monomials, then the one before, and so on.

*Before reading on: why is additivity in **each** argument separately enough, and where would "additive in the pair", \( \Phi(p + p', q + q') = \Phi(p, q) + \Phi(p', q') \), fail?*
:::

::: {.proof}
*The case \( m = 1 \).* We prove by @fd1:ax-induction on \( N \): *for every \( p \in R[x] \) for which \( N \) is admissible, \( \Phi(p) = \Psi(p) \).* Every polynomial has an admissible \( N \) (@def-polynomial), so this gives \( \Phi = \Psi \) (@fd2:prp-function-equality). For \( N = 0 \), \( p \) agrees in every position with the monomial \( p_0 x^0 \), so \( p = p_0 x^0 \) and \( \Phi(p) = \Psi(p) \) by hypothesis. Suppose the statement holds for \( N \), and let \( N + 1 \) be admissible for \( p \). Put \( p' \coloneqq \sum_{k=0}^{N} p_k x^k \). By @prp-polynomial-sum-of-monomials, \( N \) is admissible for \( p' \), and by the recursion of @lem-finite-sums-and-powers (a) and the same proposition,
\[
p = \sum_{k=0}^{N+1} p_k x^k = p' + p_{N+1} x^{N+1} .
\]
Hence
\[
\Phi(p) = \Phi(p') + \Phi(p_{N+1} x^{N+1}) = \Psi(p') + \Psi(p_{N+1} x^{N+1}) = \Psi(p) ,
\]
by additivity of \( \Phi \), the induction hypothesis for \( p' \) together with the hypothesis on monomials, and additivity of \( \Psi \).

*The case \( m = 2 \).* Fix a monomial \( u \). The maps \( v \mapsto \Phi(u, v) \) and \( v \mapsto \Psi(u, v) \) are additive and agree on monomials, so by the case \( m = 1 \) they agree everywhere: \( \Phi(u, q) = \Psi(u, q) \) for every monomial \( u \) and **every** \( q \in R[x] \). Now fix any \( q \). The maps \( u \mapsto \Phi(u, q) \) and \( u \mapsto \Psi(u, q) \) are additive and, by what was just shown, agree on monomials; so they agree everywhere.

*The case \( m = 3 \).* The same, one argument at a time. For monomials \( u_1, u_2 \), the case \( m = 1 \) in the third argument gives \( \Phi(u_1, u_2, r) = \Psi(u_1, u_2, r) \) for every \( r \). For a monomial \( u_1 \) and any \( r \), the case \( m = 1 \) in the second argument then gives agreement for every \( q \) in the middle. Finally, for any \( q, r \), the case \( m = 1 \) in the first argument gives \( \Phi(p, q, r) = \Psi(p, q, r) \) for every \( p \). This proves the lemma.
:::

The answer to the prompt. Each step of the proof changes **one** argument from "a monomial" to "arbitrary" while the other arguments are held fixed, and it only ever splits that one argument into a sum. Additivity in each argument separately is exactly that. "Additive in the pair" is a different condition, and the product does not satisfy it: with \( p = q' = 1 \) and \( p' = q = 0 \), \( (p + p')(q + q') = 1 \cdot 1 = 1 \), while \( pq + p'q' = 0 + 0 = 0 \) whenever \( 1 \ne 0 \) in \( R \). A proof that split both arguments at once would lose the cross terms \( pq' \) and \( p'q \).

We call this move **check on monomials, extend by additivity**. To prove that two expressions in polynomials agree, check that both are additive in each argument, and check the identity when every argument is a monomial. The second check is a computation with a single coefficient in each argument.

## The ring laws

Now the payoff: every law of a commutative ring holds in \( R[x] \). The theorem also records how \( R \) sits inside \( R[x] \) and why the school notation \( a x^n \) means what it seems to mean. The five rules in (a) are listed in the order in which the linear algebra companion numbers them, so that its references to the parts "1" to "5" read correctly.

::: {#thm-polynomial-ring-laws}
[The Polynomial Ring Is a Commutative Ring]

Let \( R \) be a commutative ring.

::: {.enumerate options="label=(\alph*)"}
1. \( R[x] \), with the operations of @def-polynomial-ring, is a commutative ring (@fd3:def-commutative-ring-and-field), with zero the zero polynomial, negative \( -p \) as defined there, and one \( 1 \coloneqq 1 \, x^0 \). Spelled out, for all \( p, q, r \in R[x] \): (1) \( p + q = q + p \) and \( (p + q) + r = p + (q + r) \); (2) \( p + 0 = p \) and \( p + (-p) = 0 \); (3) \( pq = qp \) and \( (pq)r = p(qr) \); (4) \( 1 \cdot p = p \); (5) \( p(q + r) = pq + pr \).
2. The map \( R \to R[x] \), \( a \mapsto a \, x^0 \), is injective and satisfies \( (a + b) x^0 = a x^0 + b x^0 \), \( (ab) x^0 = (a x^0)(b x^0) \) and \( 1 x^0 = 1 \). If \( 1 \ne 0 \) in \( R \), then \( 1 \ne 0 \) in \( R[x] \).
3. For \( n \in \nN \), the \( n \)-th power of \( x \) in the ring \( R[x] \) (@lem-finite-sums-and-powers (c)) is the monomial \( 1 \, x^n \), and the product of the constant \( a \) with it is the monomial \( a \, x^n \). Hence \( p = \sum_{k=0}^{N} p_k x^k \), for admissible \( N \), is a sum of products of constants and powers of \( x \).
4. For a constant \( a \) and \( p \in R[x] \), \( (ap)_k = a \, p_k \) for every \( k \).
:::
:::

In words: (a) says we may compute in \( R[x] \) by every rule of a commutative ring; (b) says that computing with constant polynomials is computing in \( R \), which justifies calling \( a \, x^0 \) "the constant \( a \)"; (c) says that the monomial \( a x^n \) of Section 4.1, a sequence, is the product \( a \cdot x \cdot x \cdots x \) of school algebra; and (d) says that multiplying by a constant multiplies every coefficient.

*Try it first (ten minutes): for \( p = a_0 + a_1 x \), \( q = b_0 + b_1 x \) and \( r = c_0 + c_1 x \), write the coefficient of \( x^2 \) in \( (pq)r \) and in \( p(qr) \) from @def-polynomial-ring. Which laws of \( R \) did you need to see that they are equal, and how would your argument scale to polynomials of degree \( 10 \)?*

::: {.idea}
The attempt gives \( pq = a_0 b_0 + (a_0 b_1 + a_1 b_0) x + a_1 b_1 x^2 \), and the coefficient of \( x^2 \) in \( (pq)r \) is \( (a_0 b_1 + a_1 b_0) c_1 + (a_1 b_1) c_0 \), while in \( p(qr) \) it is \( a_0 (b_1 c_1) + a_1 (b_0 c_1 + b_1 c_0) \). Both expand, by (F9), to the three products \( a_0 b_1 c_1 \), \( a_1 b_0 c_1 \), \( a_1 b_1 c_0 \), grouped and ordered differently, so (F1), (F2), (F5), (F6) and (F9) all enter. In degree \( 10 \) the two coefficients of \( x^k \) are double sums, \( \sum_s \bigl( \sum_i a_i b_{s-i} \bigr) c_{k-s} \) and \( \sum_i a_i \bigl( \sum_j b_j c_{k-i-j} \bigr) \), and the plan "both are the sum of all \( a_i b_j c_l \) with \( i + j + l = k \)" needs a theorem on reordering finite double sums, which we have not proved.

Monomials avoid that theorem. When each of \( p \), \( q \), \( r \) has a single non-zero coefficient, every double sum collapses to one product, and the law becomes a law of \( R \) together with a law of \( \nN \) for the exponents. Both sides are additive in each argument, by (\( \ast \)) and (\( \ast\ast \)), so @lem-check-on-monomials carries the monomial case to all polynomials. The additive laws need nothing new: they are the laws of \( R \), position by position.

*Before reading on: self-explain the monomial line for (F5) in the proof below. Which law of \( R \) does it use, and which law of \( \nN \)?*
:::

::: {.proof}
*(a)* By @def-polynomial-ring and the closure paragraph after it, \( + \) and \( \cdot \) are functions \( R[x] \times R[x] \to R[x] \). We check the clauses of @fd3:def-commutative-ring-and-field.

*(F1)–(F4), position by position.* For every \( k \), \( (p + q)_k = p_k + q_k = q_k + p_k = (q + p)_k \) by (F1) in \( R \); \( ((p + q) + r)_k = (p_k + q_k) + r_k = p_k + (q_k + r_k) = (p + (q + r))_k \) by (F2); \( (p + 0)_k = p_k + 0 = p_k \) by (F3); and \( (p + (-p))_k = p_k + (-p_k) = 0 \) by (F4). So (F1)–(F4) hold in \( R[x] \), by **compare coefficients** (@fd2:prp-function-equality), with the zero polynomial as \( 0 \) and \( -p \) as the negative of \( p \).

*(F9).* This is (\( \ast\ast \)).

*(F6).* Let \( \Phi(p, q) \coloneqq pq \) and \( \Psi(p, q) \coloneqq qp \). Both are additive in each argument: for \( \Phi \) this is (\( \ast \)) and (\( \ast\ast \)), and for \( \Psi \) it is the same two laws with the roles of the factors exchanged, \( q(p + p') = qp + qp' \) and \( (q + q')p = qp + q'p \). On monomials,
\[
(a x^m)(b x^n) = (ab) \, x^{m+n} = (ba) \, x^{n+m} = (b x^n)(a x^m) ,
\]
by @lem-monomial-product (b), (F6) in \( R \) with \( m + n = n + m \) in \( \nN \) (@fd3:thm-omega-arithmetic-laws (b)), and @lem-monomial-product (b) again. By @lem-check-on-monomials with \( m = 2 \) and \( T = R[x] \), whose addition is a function by the closure paragraph, \( pq = qp \) for all \( p, q \).

*(F7).* By @lem-monomial-product (a) with \( a = 1 \) and \( m = 0 \), \( (1 \cdot p)_k = 1 \, p_k = p_k \) for every \( k \), by (F7) and (F6) in \( R \). So \( 1 \cdot p = p \), and \( p \cdot 1 = 1 \cdot p = p \) by (F6) in \( R[x] \).

*(F5).* Let \( \Phi(p, q, r) \coloneqq (pq)r \) and \( \Psi(p, q, r) \coloneqq p(qr) \). Each is additive in each argument, by two applications of (\( \ast \)) and (\( \ast\ast \)); for instance, in the middle argument,
\[
\bigl( p(q + q') \bigr) r = (pq + pq') r = (pq) r + (pq') r , \qquad p\bigl( (q + q') r \bigr) = p (qr + q'r) = p(qr) + p(q'r) ,
\]
and in the first and third arguments in the same way. On monomials \( a x^m \), \( b x^n \), \( c x^l \), two applications of @lem-monomial-product (b) on each side give
\[
\bigl( (a x^m)(b x^n) \bigr)(c x^l) = \bigl( (ab) c \bigr) x^{(m+n)+l} = \bigl( a (bc) \bigr) x^{m+(n+l)} = (a x^m)\bigl( (b x^n)(c x^l) \bigr) ,
\]
where the middle equality is (F5) in \( R \) and \( (m + n) + l = m + (n + l) \) in \( \nN \) (@fd3:thm-omega-arithmetic-laws (c)). By @lem-check-on-monomials with \( m = 3 \) and \( T = R[x] \), \( (pq)r = p(qr) \) for all \( p, q, r \). This proves (a); the rules (1)–(5) are (F1) with (F2), (F3) with (F4), (F6) with (F5), (F7) in the form \( 1 \cdot p = p \), and (F9).

*(b)* If \( a x^0 = b x^0 \), the entries in position \( 0 \) give \( a = b \). The sum \( a x^0 + b x^0 \) has \( a + b \) in position \( 0 \) and \( 0 + 0 = 0 \) elsewhere, so it is \( (a + b) x^0 \). The product is \( (ab) x^{0+0} = (ab) x^0 \) by @lem-monomial-product (b), and \( 1 x^0 = 1 \) by the definition of \( 1 \) in (a). If \( 1 \ne 0 \) in \( R \), then by injectivity \( 1 x^0 \ne 0 x^0 \), and \( 0 x^0 \) is the zero polynomial.

*(c)* By @lem-finite-sums-and-powers (c) in the commutative ring \( R[x] \), \( x^0 = 1 = 1 x^0 \) and \( x^{n+1} = x^n x \). By @fd1:ax-induction on \( n \): if \( x^n = 1 x^n \), then \( x^{n+1} = (1 x^n)(1 x^1) = (1 \cdot 1) x^{n+1} = 1 x^{n+1} \), by @lem-monomial-product (b) and (F7) in \( R \). For a constant \( a \), \( (a x^0)(1 x^n) = (a \cdot 1) x^{0+n} = a x^n \), by the same lemma. With @prp-polynomial-sum-of-monomials, \( p = \sum_{k=0}^{N} p_k x^k \) is the sum of the products of the constants \( p_k \) with the powers \( x^k \).

*(d)* @lem-monomial-product (a) with \( m = 0 \): \( (a x^0 \, p)_k = a \, p_{k-0} = a \, p_k \). This proves the theorem.
:::

The answer to the prompt. The monomial line for (F5) uses associativity of multiplication in \( R \), \( (ab)c = a(bc) \), for the coefficient, and associativity of addition in \( \nN \), \( (m + n) + l = m + (n + l) \), for the exponent. Nothing else: the regrouping that the direct route needed has been absorbed into @lem-check-on-monomials, whose proof only peels off one monomial at a time.

The proof never reordered a double sum. Its only sums are the single-index sums of @def-polynomial-ring, used in the closure paragraph, in (\( \ast \)) and (\( \ast\ast \)), and in @lem-monomial-product.

::: {.remark}
Part (a) makes the name "polynomial ring" honest, and everything proved for commutative rings now applies to \( R[x] \). In particular, ideals and quotient rings (@fd3:def-ideal-commutative-ring, @fd3:thm-quotient-ring-by-ideal) are available in \( R[x] \); Chapter 5 builds quotients of \( F[x] \) for a field \( F \) this way. Also, \( (R[x], +) \) is an abelian group in the sense of Chapter 3, by (F1)–(F4).
:::

From now on we compute in \( R[x] \) as at school: expand brackets, collect terms, and move terms across equations, citing (a) and (c). The two things school algebra does **not** give us are any rule that needs division, and any rule about the degree of a product; the second depends on \( R \), and Section 4.3 finds out how.

::: {.check}
In \( \nQ[x] \) and in \( \nF_2[x] \): is \( (x + 1)^2 \) equal to \( x^2 + 2x + 1 \)? Is it equal to \( x^2 + 1 \)?
:::

::: {.solution}
By @def-polynomial-ring, \( (x + 1)^2 = (x + 1)(x + 1) \) has coefficients \( 1 \cdot 1 = 1 \), \( 1 \cdot 1 + 1 \cdot 1 = 2 \) and \( 1 \cdot 1 = 1 \) in positions \( 0, 1, 2 \), and \( 0 \) beyond, where \( 2 = 1 + 1 \). Over \( \nQ \), \( (x + 1)^2 = x^2 + 2x + 1 \), and it is **not** \( x^2 + 1 \), since \( 2 \ne 0 \) in position \( 1 \). Over \( \nF_2 \), \( 2 = 1 + 1 = 0 \), so the sequence is \( (1, 0, 1, 0, \dots) \): \( (x + 1)^2 = x^2 + 1 \), and also \( (x + 1)^2 = x^2 + 2x + 1 \), because over \( \nF_2 \) the display \( x^2 + 2x + 1 \) names the same sequence. The same three-term display means different things over different rings.
:::

## Exercises

### A. Check your understanding

::: {#exr-polynomial-ring-a1}
[A1]

These questions are about the proof of @thm-polynomial-ring-laws.

::: {.enumerate options="label=(\alph*)"}
1. Where is the commutativity of \( R \), \( ab = ba \), used?
2. Run the monomial check of (F5) on \( (2x)(3x^2)(x) \) in \( \nZ[x] \): compute both groupings.
3. In the proof of (F5), which additivity does @lem-check-on-monomials need for the third argument? Write out both identities.
4. Give the idea of the proof of (F5) in two sentences.
:::
:::

::: {.solution}
(a) In the monomial line of (F6), where \( ab = ba \) in \( R \) gives \( (ab) x^{m+n} = (ba) x^{n+m} \). In the additivity law (\( \ast \)), where \( (p_i + p'_i) q_{k-i} = p_i q_{k-i} + p'_i q_{k-i} \) is (F9) only after (F6) has moved \( q_{k-i} \) to the left. And in small ways, wherever \( 0 \cdot b = 0 \) is obtained from \( b \cdot 0 = 0 \) (@fd3:prp-ring-algebra (b)), as in @lem-monomial-product (a), and in (F7), where \( 1 \, p_k = p_k \cdot 1 \). The monomial line of (F5) does **not** use it.

(b) With \( a = 2, m = 1 \), \( b = 3, n = 2 \), \( c = 1, l = 1 \): \( \bigl( (2x)(3x^2) \bigr) x = (6 x^3) x = 6x^4 \), using \( 2 \cdot 3 = 6 \), \( 1 + 2 = 3 \), then \( 6 \cdot 1 = 6 \), \( 3 + 1 = 4 \); and \( (2x)\bigl( (3x^2) x \bigr) = (2x)(3x^3) = 6x^4 \), using \( 3 \cdot 1 = 3 \), \( 2 + 1 = 3 \), then \( 2 \cdot 3 = 6 \), \( 1 + 3 = 4 \). Both are \( 6x^4 \).

(c) For \( \Phi \): \( (pq)(r + r') = (pq)r + (pq)r' \), which is (\( \ast\ast \)) with \( pq \) in place of \( p \). For \( \Psi \): \( p\bigl( q(r + r') \bigr) = p(qr + qr') = p(qr) + p(qr') \), which is (\( \ast\ast \)) twice.

(d) On monomials, associativity is a single product: \( (ab)c = a(bc) \) in \( R \) and \( (m + n) + l = m + (n + l) \) in \( \nN \). Both sides of \( (pq)r = p(qr) \) are additive in each argument and every polynomial is a finite sum of monomials, so the monomial case extends to all polynomials, one argument at a time.
:::

### B. Practice

::: {#exr-polynomial-ring-b1}
[B1: A product over two rings]

Compute \( (2x^3 - x + 4)(-2x^3 + x^2 + 3) \) in \( \nZ[x] \) and in \( \nF_2[x] \), from @def-polynomial-ring.
:::

::: {.solution}
In \( \nZ[x] \), \( (p_0, p_1, p_2, p_3) = (4, -1, 0, 2) \) and \( (q_0, q_1, q_2, q_3) = (3, 0, 1, -2) \), with \( 3 \) admissible for both; so \( (pq)_k = 0 \) for \( k > 6 \), and
\[
\begin{aligned}
(pq)_0 &= 4 \cdot 3 = 12 , \\
(pq)_1 &= 4 \cdot 0 + (-1) \cdot 3 = -3 , \\
(pq)_2 &= 4 \cdot 1 + (-1) \cdot 0 + 0 \cdot 3 = 4 , \\
(pq)_3 &= 4 \cdot (-2) + (-1) \cdot 1 + 0 \cdot 0 + 2 \cdot 3 = -3 , \\
(pq)_4 &= (-1)(-2) + 0 \cdot 1 + 2 \cdot 0 = 2 , \\
(pq)_5 &= 0 \cdot (-2) + 2 \cdot 1 = 2 , \\
(pq)_6 &= 2 \cdot (-2) = -4 ,
\end{aligned}
\]
where in positions \( 4, 5, 6 \) the terms with an index above \( 3 \) are \( 0 \) and have been left out. Hence
\[
pq = -4x^6 + 2x^5 + 2x^4 - 3x^3 + 4x^2 - 3x + 12 .
\]
In \( \nF_2[x] \) the displays name other sequences: \( 2 = 0 \), \( 4 = 0 \), \( -1 = 1 \), \( -2 = 0 \) and \( 3 = 1 \) in \( \nF_2 \), so the first factor is \( x \) and the second is \( x^2 + 1 \). By @lem-monomial-product (a) with \( a = 1 \), \( m = 1 \), the product shifts \( (1, 0, 1, 0, \dots) \) one place up: \( x(x^2 + 1) = x^3 + x \). This agrees with reducing the integer coefficients \( 12, -3, 4, -3, 2, 2, -4 \) modulo \( 2 \), which gives \( 0, 1, 0, 1, 0, 0, 0 \).
:::

::: {#exr-polynomial-ring-b2}
[B2: Changing the sign of x]

Define \( \sigma \colon R[x] \to R[x] \) by \( \sigma(p)_k \coloneqq (-1)^k p_k \), where \( (-1)^k \) is the power in \( R \) (@lem-finite-sums-and-powers (c)). Then \( \sigma(p) \) is a polynomial, since \( (-1)^k \cdot 0 = 0 \). We want to prove that \( \sigma(pq) = \sigma(p) \sigma(q) \) for all \( p, q \in R[x] \).

You may use the following, without proof. The map \( \sigma \) is additive: \( \sigma(p + q) = \sigma(p) + \sigma(q) \), position by position by (F9). Hence, with (\( \ast \)) and (\( \ast\ast \)), the maps \( \Phi(p, q) \coloneqq \sigma(pq) \) and \( \Psi(p, q) \coloneqq \sigma(p) \sigma(q) \) are additive in each argument.

The last step is blank. *Name the move, then complete it.*
:::

::: {.solution}
The move is **check on monomials, extend by additivity**.

Let \( a, b \in R \) and \( m, n \in \nN \). The monomial \( a x^m \) has only position \( m \) possibly non-zero, so \( \sigma(a x^m) = \bigl( (-1)^m a \bigr) x^m \). By @lem-monomial-product (b),
\[
\Phi(a x^m, b x^n) = \sigma\bigl( (ab) x^{m+n} \bigr) = \bigl( (-1)^{m+n} ab \bigr) x^{m+n} ,
\]
\[
\Psi(a x^m, b x^n) = \bigl( (-1)^m a \bigr) x^m \cdot \bigl( (-1)^n b \bigr) x^n = \bigl( (-1)^m a \, (-1)^n b \bigr) x^{m+n} .
\]
The two coefficients agree: \( (-1)^m a \, (-1)^n b = \bigl( (-1)^m (-1)^n \bigr) (ab) = (-1)^{m+n} ab \), by (F5) and (F6) in \( R \) and the first power law of @lem-finite-sums-and-powers (c). So \( \Phi \) and \( \Psi \) agree on monomials, and by @lem-check-on-monomials with \( m = 2 \) and \( T = R[x] \), \( \sigma(pq) = \sigma(p) \sigma(q) \) for all \( p, q \).

Also \( \sigma(1) = 1 \), since \( (-1)^0 = 1 \). Section 4.4 writes \( \sigma(p) \) as \( p(-x) \).
:::

### C. Going deeper

::: {#exr-polynomial-ring-c1}
[C1: Exit check: the ring laws]

Let \( R \) be a commutative ring. Prove, from @def-polynomial-ring, that the multiplication of \( R[x] \) is commutative and associative. You may use @lem-finite-sums-and-powers and @fd2:prp-function-equality, but not @thm-polynomial-ring-laws.
:::

::: {.solution}
*Distributivity.* For \( p, p', q, q' \in R[x] \), the \( k \)-th coefficient of \( (p + p')q \) is \( \sum_{i=0}^{k} (p_i + p'_i) q_{k-i} \). Inside each term, (F6), (F9), (F6) give \( p_i q_{k-i} + p'_i q_{k-i} \), and (Σ1) splits the sum into \( (pq)_k + (p'q)_k \). So \( (p + p')q = pq + p'q \), and in the same way, with (F9) directly, \( p(q + q') = pq + pq' \). Hence \( (p, q) \mapsto pq \) and \( (p, q) \mapsto qp \) are additive in each argument, and so are \( (p, q, r) \mapsto (pq)r \) and \( (p, q, r) \mapsto p(qr) \), by applying the two laws twice.

*Monomials.* For \( a, b \in R \) and \( m, n \in \nN \), the \( k \)-th coefficient of \( (a x^m)(b x^n) \) is \( \sum_{i=0}^{k} (a x^m)_i (b x^n)_{k-i} \). Every term with \( i \ne m \) is \( 0 \), and the term with \( i = m \) (present when \( m \le k \)) is \( a \, (b x^n)_{k-m} \), which is \( ab \) if \( k = m + n \) and \( 0 \) otherwise. By (Σ3), \( (a x^m)(b x^n) = (ab) x^{m+n} \).

*Reduction.* Every polynomial is a finite sum of monomials, \( p = \sum_{k=0}^{N} p_k x^k \) for admissible \( N \), checked position by position. So a map additive in each argument is determined by its values on monomials: by induction on \( N \), peeling off the top monomial \( p_{N+1} x^{N+1} \), two such maps of one argument that agree on monomials agree everywhere; with two or three arguments, apply this to one argument at a time, holding the others fixed (first as monomials, then as arbitrary polynomials).

*Commutativity.* \( (a x^m)(b x^n) = (ab) x^{m+n} = (ba) x^{n+m} = (b x^n)(a x^m) \), by (F6) in \( R \) and \( m + n = n + m \) in \( \nN \); the reduction gives \( pq = qp \).

*Associativity.* \( \bigl( (a x^m)(b x^n) \bigr)(c x^l) = \bigl( (ab)c \bigr) x^{(m+n)+l} \) and \( (a x^m)\bigl( (b x^n)(c x^l) \bigr) = \bigl( a(bc) \bigr) x^{m+(n+l)} \), equal by (F5) in \( R \) and associativity of \( + \) in \( \nN \); the reduction with three arguments gives \( (pq)r = p(qr) \).

**Marking scheme.** (10 points)
- 2: both distributive laws from the coefficient formula, naming the rule for a single-index sum ((Σ1)) and the law of \( R \) used inside each term.
- 2: the product of two monomials, \( (a x^m)(b x^n) = (ab) x^{m+n} \), with the vanishing of the other terms shown.
- 3: the reduction to monomials, with additivity in each argument stated and used one argument at a time (an induction on the number of monomials, or a citation of the checking principle once proved).
- 1: commutativity on monomials, naming (F6) in \( R \).
- 2: associativity on monomials, naming (F5) in \( R \) and the law of \( \nN \) used for the exponents.

Fatal errors (0 for the step): treating polynomials as functions on \( R \) and citing the laws of \( R \) "pointwise"; checking only on \( x^m \) and \( x^n \), with no account of the coefficients (the coefficients are where (F5) and (F6) of \( R \) are needed).

A second route rewrites both triple products as one sum over all \( (i, j, l) \) with \( i + j + l = k \), after proving a reindexing lemma for finite double sums by induction. It maps to the same points, with the reindexing lemma, proved, taking the 3 points of the reduction step.
:::

::: {#exr-polynomial-ring-c2}
[C2: Formal power series]

Let \( R^{\nN} \) be the set of **all** sequences \( \nN \to R \), with sum and product given by the formulas of @def-polynomial-ring.

::: {.enumerate options="label=(\alph*)"}
1. Show that the formulas define functions \( R^{\nN} \times R^{\nN} \to R^{\nN} \).
2. Show that \( R[x] \subseteq R^{\nN} \) is closed under the sum and the product.
3. Let \( s \coloneqq (1, 1, 1, \dots) \). Show that \( (1 - x) s = 1 \).
4. Which step of the proof of @lem-check-on-monomials (with \( m = 1 \)) does not reach the elements of \( R^{\nN} \)?
:::
:::

::: {.solution}
(a) For \( p, q \in R^{\nN} \) and \( k \in \nN \), \( p_k + q_k \in R \), and \( \sum_{i=0}^{k} p_i q_{k-i} \) is a sum of \( k + 1 \) elements of \( R \), defined by @lem-finite-sums-and-powers (a). No finiteness of \( p \) or \( q \) is needed: each coefficient of the product only looks at positions \( 0, \dots, k \). So both formulas give sequences \( \nN \to R \).

(b) This is the closure paragraph after @def-polynomial-ring: if \( m \) and \( n \) are admissible for \( p \) and \( q \), then \( \max(m, n) \) is admissible for \( p + q \) and \( m + n \) for \( pq \).

(c) \( 1 - x = (1, -1, 0, 0, \dots) \). In position \( 0 \), \( \bigl( (1 - x)s \bigr)_0 = 1 \cdot 1 = 1 \). In position \( k \ge 1 \), the terms with \( i \ge 2 \) are \( 0 \cdot 1 = 0 \), and the terms with \( i = 0 \) and \( i = 1 \) give \( 1 \cdot 1 + (-1) \cdot 1 = 0 \). So \( (1 - x)s = (1, 0, 0, \dots) = 1 \).

(d) The induction proves \( \Phi(p) = \Psi(p) \) only for sequences \( p \) that have an admissible \( N \); its last line uses that every polynomial has one. The sequence \( s \) has none, and it is not a finite sum of monomials either, since by (b) such a sum is a polynomial. So @lem-check-on-monomials says nothing about \( s \), and the proof of @thm-polynomial-ring-laws does not apply to \( R^{\nN} \). The ring laws do hold in \( R^{\nN} \), the ring of **formal power series**, but a proof needs the route through reordered double sums, which we do not take; nothing in this book depends on it.

So \( 1 - x \) has an inverse among all sequences. Section 4.3 shows that over \( \nZ \) it has none in \( \nZ[x] \) itself.
:::

<!-- dependency ledger
def-polynomial-ring (claim): k - i in N for i <= k | fd3:prp-naturals-embed-integers (cited), with fd3:thm-omega-order and the ordered-ring rules of Number Systems Ch 2 (fd3:prp-ordered-ring-rules), used silently
def-polynomial-ring (claim): closure: for k > m + n and i <= m, k - i >= k - m > n | index arithmetic in Z (fd3:thm-integers-ordered-ring, fd3:prp-ordered-ring-rules (O3)), used silently; terms 0 by fd3:prp-ring-algebra (b) with (F6) (cited); (Sigma3) of lem-finite-sums-and-powers with j = k + 1
def-polynomial-ring (claim): -0 = 0 | 0 + 0 = 0 by (F3), uniqueness fd3:prp-ring-algebra (a) (cited)
def-polynomial-ring (claim): Section 4.3 degree of a product; Section 4.4 explains reduction of coefficients; Sections 4.4, 4.5 reuse the move | ch04 blueprint (within the chapter: thm-degree-of-product, cor-polynomial-coefficient-change, thm-evaluation-respects-operations, thm-formal-derivative-rules); nothing here depends on them
exm-polynomial-product (solution): coefficients 2, 1, 2, 3 over Q; 2, 1, 2 over F_3; [2], [1], [2], [3] over Z/6Z; [-1] = [5], [7] = [1], [8] = [2] | arithmetic in Z, def-field-fp, fd3:def-integers-mod-n-ring; verify/ch04/exm-polynomial-product.py
def-polynomial-ring (claim): (warning) coefficientwise product would give x * x = x | arithmetic; verify/ch04/def-polynomial-ring.py
prp-polynomial-sum-of-monomials (proof): induction on N | fd1:ax-induction read on omega through fd3:cor-omega-identification (b), as in Section 4.1
lem-monomial-product (proof): k - m = n iff k = m + n; k < m implies k != m + n | index arithmetic in N (fd3:thm-omega-arithmetic-laws, fd3:thm-omega-order), used silently
lem-check-on-monomials (proof): induction on N; every polynomial has an admissible N | fd1:ax-induction; def-polynomial (cited)
lem-check-on-monomials (claim): (answer) (p + p')(q + q') = 1 and pq + p'q' = 0 for p = q' = 1, p' = q = 0 | products of constants by lem-monomial-product (b) with m = n = 0, (F7) and fd3:prp-ring-algebra (b) in R; 1 != 0 in R[x] from 1 != 0 in R (positions 0), used silently
thm-polynomial-ring-laws (claim): the five rules (1)-(5) follow the linear algebra companion's numbering | la:thm-polynomial-ring-laws items 1-5 (companion ch 0, Section 0.8), checked against its text; prose only
thm-polynomial-ring-laws (idea): Try-it-first coefficients of x^2 | verify/ch04/thm-polynomial-ring-laws.py (identity checked on random integers)
thm-polynomial-ring-laws (proof): m + n = n + m; (m + n) + l = m + (n + l) in N | fd3:thm-omega-arithmetic-laws (b), (c) (cited)
thm-polynomial-ring-laws (claim): (meta) the proof never reorders a double sum; its sums are the single-index sums of def-polynomial-ring | meta-claim about this section: closure paragraph, (*), (**), lem-monomial-product, prp-polynomial-sum-of-monomials (sums of monomials, single index)
thm-polynomial-ring-laws (claim): (remark) ideals and quotient rings apply to R[x]; Chapter 5 builds F[x]/<f>; (R[x], +) is an abelian group in the sense of Chapter 3 | fd3:def-ideal-commutative-ring, fd3:thm-quotient-ring-by-ideal (cited); F4.5 (prose pointer, ch05 blueprint thm-polynomial-quotient-ring); F4.3 def-group (prose, not cited); nothing depends on them
thm-polynomial-ring-laws (claim): (check) (x + 1)^2 over Q and F_2; 2 = 1 + 1 = 0 in F_2 | exm-finite-fields (tables of F_2), used silently; verify/ch04/thm-polynomial-ring-laws.py
exr-polynomial-ring-a1 (solution): 2*3 = 6, exponents 1 + 2 + 1 = 4 | numerals; verify/ch04/exr-polynomial-ring-a1.py
exr-polynomial-ring-b1 (solution): coefficients 12, -3, 4, -3, 2, 2, -4; reduction mod 2 | arithmetic in Z and F_2; verify/ch04/exr-polynomial-ring-b1.py
exr-polynomial-ring-b2 (solution): sigma(a x^m) = ((-1)^m a) x^m; (-1)^m (-1)^n = (-1)^(m+n) | lem-finite-sums-and-powers (c) (cited); verify/ch04/exr-polynomial-ring-b2.py (sigma multiplicative on random pairs over Z/nZ)
exr-polynomial-ring-b2 (claim): Section 4.4 writes sigma(p) as p(-x) | ch04 blueprint def-polynomial-composition (prose pointer within the chapter)
exr-polynomial-ring-c1 (solution): reduction to monomials by induction on N | the proof of lem-check-on-monomials, rewritten inside the solution (the exercise forbids thm-polynomial-ring-laws, not the lemma)
exr-polynomial-ring-c2 (solution): (1 - x)s = 1 | arithmetic; verify/ch04/exr-polynomial-ring-c2.py
exr-polynomial-ring-c2 (claim): the ring laws hold for formal power series | not proved here; stated as such; nothing depends on it
exr-polynomial-ring-c2 (claim): Section 4.3 shows 1 - x is not a unit of Z[x] | ch04 blueprint prp-polynomial-units (prose pointer within the chapter)
-->
