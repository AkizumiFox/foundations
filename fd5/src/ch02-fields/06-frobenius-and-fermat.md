# The Binomial Theorem, the Frobenius Map, and Fermat's Little Theorem

In \( \nF_5 \), compute \( (1 + 2)^5 \) and \( 1^5 + 2^5 \). The first is \( 3^5 = 243 \), and \( 243 = 48 \cdot 5 + 3 \), so it is \( 3 \). The second is \( 1 + 32 = 33 = 6 \cdot 5 + 3 \), so it is \( 3 \) as well. The rule "\( (x + y)^n = x^n + y^n \)", the classic error of school algebra, is a theorem when \( n \) is the characteristic \( p \) of the field. This section proves it, and deduces Fermat's little theorem from it with the rigidity of Section 2.5: a homomorphism of \( \nF_p \) to itself is the identity.

The tool is the binomial theorem. School proves it for numbers; we need it in an arbitrary commutative ring, with the binomial coefficients acting as integer multiples, and so we first set up finite sums in a ring.

## Sums and powers in a commutative ring

*Sets and Functions*, Chapter 3 defines finite sums, products and powers of real numbers by recursion (@fd2:def-sum-product, @fd2:def-power, both from @fd2:thm-recursion). The definitions use nothing about \( \nR \) except an addition with a \( 0 \) and a multiplication with a \( 1 \). So, read on \( \nN = \omega \) through @fd3:cor-omega-identification (b), with \( X = R \), they define in every commutative ring \( R \):

- sums \( \sum_{k=m}^{n} a_k \) of elements \( a_k \in R \), with the empty sum \( 0 \), and the three remarks after @fd2:def-sum-product: a sum depends only on the terms it adds (finite lists), **shifting the index**, and **splitting off the last term**, \( \sum_{k=m}^{n+1} a_k = \sum_{k=m}^{n} a_k + a_{n+1} \) for \( m \le n + 1 \);
- powers \( x^0 \coloneqq 1 \), \( x^{n+1} \coloneqq x^n x \) for \( x \in R \) and \( n \in \nN \), with the laws of @fd2:prp-power-laws (a)–(c):
\[
x^{m+n} = x^m x^n , \qquad (x^m)^n = x^{mn} , \qquad (xy)^n = x^n y^n .
\]

The proofs of those laws in *Sets and Functions* use only (F1)–(F7), (F9) and induction, so they run unchanged in \( R \). We use this paragraph as a template and do not repeat it. (*Analytic Preliminaries*, Chapter 1 proves the same power laws for every commutative ring as @fd4:prp-power-laws-commutative-ring; we compare, and cite the template.) In particular \( 1^n = 1 \) for every \( n \), by induction: \( 1^0 = 1 \) and \( 1^{n+1} = 1^n \cdot 1 = 1 \).

The binomial theorem rearranges sums term by term, and the rules it needs are collected in the next lemma. The sums start at \( k = 0 \); by the definition, \( \sum_{k=0}^{0} a_k = 0 + a_0 = a_0 \).

::: {#lem-ring-finite-sums}
[Finite Sums in a Commutative Ring]

Let \( R \) be a commutative ring, \( n \in \nN \), \( c \in R \), and let \( (a_k)_{k \in \nN} \) and \( (b_k)_{k \in \nN} \) be sequences in \( R \).

::: {.enumerate options="label=(\alph*)"}
1. \( \sum_{k=0}^{n} (a_k + b_k) = \sum_{k=0}^{n} a_k + \sum_{k=0}^{n} b_k \).
2. \( c \sum_{k=0}^{n} a_k = \sum_{k=0}^{n} c\, a_k \).
3. \( \sum_{k=0}^{n} m \cdot a_k = m \cdot \sum_{k=0}^{n} a_k \) for every \( m \in \nZ \).
4. Let \( j \in \nN \), and suppose \( a_k = 0 \) for every \( k \ne j \). Then \( \sum_{k=0}^{n} a_k = a_j \) if \( j \le n \), and \( \sum_{k=0}^{n} a_k = 0 \) if \( j > n \).
5. \( -\sum_{k=0}^{n} a_k = \sum_{k=0}^{n} (-a_k) \).
6. *(Splitting off the first term.)* \( \sum_{k=0}^{n+1} a_k = a_0 + \sum_{k=0}^{n} a_{k+1} \).
:::
:::

In words: a finite sum may be split termwise, multiplied termwise, and negated termwise; a sum with one non-zero term is that term; and the first term may be split off, the rest being re-indexed from \( 0 \). By the finite-lists remark, the lemma applies to finitely many terms \( a_0, \dots, a_n \) as well.

::: {.idea}
A sum up to \( n + 1 \) is the sum up to \( n \) plus one term, so every rule that holds for one term and survives adding one more term holds for all sums: an induction on \( n \) whose step is a single axiom, (F1)–(F2) for (a), (F9) for (b), and associativity for (f). Parts (c) and (e) need no induction, because a multiple is a product, \( m \cdot a = (m \cdot 1)a \), so they are (b) in disguise.
:::

::: {.proof}
Each part is an induction on \( n \) (@fd1:ax-induction), splitting off the last term at the step, except (c) and (e), which follow from (b).

(a) For \( n = 0 \) both sides are \( a_0 + b_0 \). If (a) holds for \( n \), then splitting off the last term,
\[
\sum_{k=0}^{n+1} (a_k + b_k) = \Bigl( \sum_{k=0}^{n} a_k + \sum_{k=0}^{n} b_k \Bigr) + (a_{n+1} + b_{n+1}) ,
\]
which is \( \bigl( \sum_{k=0}^{n} a_k + a_{n+1} \bigr) + \bigl( \sum_{k=0}^{n} b_k + b_{n+1} \bigr) \) by (F1) and (F2), and that is the right side for \( n + 1 \).

(b) For \( n = 0 \) both sides are \( c a_0 \). At the step, \( c \bigl( \sum_{k=0}^{n} a_k + a_{n+1} \bigr) = c \sum_{k=0}^{n} a_k + c a_{n+1} \) by (F9), and the induction hypothesis rewrites the first term.

(c) By @lem-integer-multiples (c), which holds for \( m \in \nZ \) by part (d) there, \( m \cdot a_k = (m \cdot 1) a_k \) and \( m \cdot \sum a_k = (m \cdot 1) \sum a_k \). So (c) is (b) with \( c = m \cdot 1 \).

(d) For \( n = 0 \): if \( j = 0 \) the sum is \( a_0 = a_j \); if \( j > 0 \), then \( 0 \ne j \), so the sum is \( a_0 = 0 \). Suppose (d) holds for \( n \), and split off \( a_{n+1} \). If \( j \le n \), the sum up to \( n \) is \( a_j \) and \( a_{n+1} = 0 \) (as \( n + 1 \ne j \)), so the total is \( a_j \). If \( j = n + 1 \), the sum up to \( n \) is \( 0 \) (as \( j > n \)) and the total is \( 0 + a_{n+1} = a_j \). If \( j > n + 1 \), both parts are \( 0 \).

(e) By (c) with \( m = -1 \), since \( (-1) \cdot x = -(1 \cdot x) = -x \) (@lem-integer-multiples (d)).

(f) For \( n = 0 \) both sides are \( a_0 + a_1 \). If (f) holds for \( n \), then
\[
\sum_{k=0}^{n+2} a_k = \Bigl( a_0 + \sum_{k=0}^{n} a_{k+1} \Bigr) + a_{n+2} = a_0 + \sum_{k=0}^{n+1} a_{k+1} ,
\]
by splitting off the last term, the induction hypothesis, (F2), and splitting off the last term of the sequence \( (a_{k+1})_k \), whose term at \( k = n + 1 \) is \( a_{n+2} \). This proves the lemma.
:::

## Binomial coefficients

In \( (x + y)^n \), each product \( x^k y^{n-k} \) appears a certain number of times, and that number is the binomial coefficient. We define it by Pascal's rule, which is how the coefficients arise when \( (x + y)^n \) is multiplied by \( x + y \), and we never divide.

::: {#def-binomial-coefficients}
[Binomial Coefficients]

The **binomial coefficients** \( \binom{n}{k} \in \nN \), for \( n, k \in \nN \), are defined by recursion on \( n \) (@fd2:thm-recursion, with \( X \) the set of functions \( \nN \to \nN \)):
\[
\begin{aligned}
\binom{0}{0} &\coloneqq 1 , & \binom{0}{k} &\coloneqq 0 \quad (k \ge 1) , \\
\binom{n + 1}{0} &\coloneqq 1 , & \binom{n + 1}{k + 1} &\coloneqq \binom{n}{k} + \binom{n}{k + 1} \quad (k \in \nN) .
\end{aligned}
\]
:::

In words: row \( n + 1 \) starts with \( 1 \), and each later entry is the sum of the two entries of row \( n \) above it (**Pascal's rule**). Each row is a whole function \( \nN \to \nN \), so the recursion has values for every \( k \), and a coefficient is a natural number, never a quotient.

Three facts follow by one induction on \( n \) each.

- \( \binom{n}{k} = 0 \) for \( k > n \). For \( n = 0 \) this is the definition. If it holds for \( n \) and \( k > n + 1 \), write \( k = j + 1 \) with \( j > n \); then \( \binom{n+1}{j+1} = \binom{n}{j} + \binom{n}{j+1} = 0 + 0 \).
- \( \binom{n}{n} = 1 \). Indeed \( \binom{0}{0} = 1 \), and \( \binom{n+1}{n+1} = \binom{n}{n} + \binom{n}{n+1} = 1 + 0 \) by the first fact.
- \( \binom{n}{1} = n \). Indeed \( \binom{0}{1} = 0 \), and \( \binom{n+1}{1} = \binom{n}{0} + \binom{n}{1} = 1 + n \).

The rows \( n = 0, \dots, 6 \), with the zeros for \( k > n \) shown:

| \( n \) | \( k = 0 \) | \( 1 \) | \( 2 \) | \( 3 \) | \( 4 \) | \( 5 \) | \( 6 \) |
|---|---|---|---|---|---|---|---|
| 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| 2 | 1 | 2 | 1 | 0 | 0 | 0 | 0 |
| 3 | 1 | 3 | 3 | 1 | 0 | 0 | 0 |
| 4 | 1 | 4 | 6 | 4 | 1 | 0 | 0 |
| 5 | 1 | 5 | 10 | 10 | 5 | 1 | 0 |
| 6 | 1 | 6 | 15 | 20 | 15 | 6 | 1 |

::: {.remark}
The formula \( \binom{n}{k} \cdot k! \cdot (n - k)! = n! \) for \( k \le n \) is true, but we neither prove nor use it. The route below needs one identity between neighboring coefficients and avoids division altogether, which matters because in \( \nF_p \) the factorial \( p! \) is \( 0 \).
:::

The identity we need relates row \( n + 1 \) to row \( n \) by a factor. It is what makes a prime divide the middle coefficients of row \( p \).

::: {#prp-binomial-absorption}
[Absorption Identity]

For all \( n, k \in \nN \),
\[
(k + 1) \binom{n + 1}{k + 1} = (n + 1) \binom{n}{k} .
\]
:::

::: {.idea}
The definition is a recursion on \( n \), so we induct on \( n \), proving the statement for **all** \( k \) at once; the step then needs the hypothesis at two values of \( k \). In the step, expand the left side by Pascal's rule, split the factor \( k + 2 \) as \( (k + 1) + 1 \) in front of one of the two terms, apply the hypothesis twice, and recombine with Pascal's rule. For \( n = 2 \), \( k = 0 \) it reads \( 1 \cdot 3 = 3 \cdot 1 \); for \( n = 3 \), \( k = 1 \), \( 2 \cdot 6 = 4 \cdot 3 \).
:::

::: {.proof}
We prove by induction on \( n \) (@fd1:ax-induction) the statement "for every \( k \in \nN \), \( (k + 1)\binom{n+1}{k+1} = (n + 1)\binom{n}{k} \)".

*Base \( n = 0 \).* For \( k = 0 \): \( 1 \cdot \binom{1}{1} = 1 = 1 \cdot \binom{0}{0} \). For \( k \ge 1 \): \( \binom{1}{k+1} = 0 \) since \( k + 1 > 1 \), and \( \binom{0}{k} = 0 \); both sides are \( 0 \).

*Step.* Suppose the statement holds for \( n \). For \( k = 0 \), the claim for \( n + 1 \) reads \( \binom{n+2}{1} = (n + 2)\binom{n+1}{0} \), and both sides are \( n + 2 \) by the facts above. For \( k = j + 1 \) with \( j \in \nN \), Pascal's rule gives
\[
\begin{aligned}
(j + 2)\binom{n+2}{j+2} &= (j + 2)\binom{n+1}{j+1} + (j + 2)\binom{n+1}{j+2} \\
&= (j + 1)\binom{n+1}{j+1} + \binom{n+1}{j+1} + (j + 2)\binom{n+1}{j+2} \\
&= (n + 1)\binom{n}{j} + \binom{n+1}{j+1} + (n + 1)\binom{n}{j+1} \\
&= (n + 1)\binom{n+1}{j+1} + \binom{n+1}{j+1} = (n + 2)\binom{n+1}{j+1} ,
\end{aligned}
\]
where the third line uses the hypothesis at \( k = j \) and at \( k = j + 1 \), and the fourth line Pascal's rule again. This is the claim for \( n + 1 \) at \( k = j + 1 \). This proves the proposition.
:::

## The binomial theorem

Expanding \( (x + y)^n \) multiplies out \( n \) factors \( x + y \) and collects the products \( x^k y^{n-k} \). In a commutative ring this collecting is legitimate, and the counts are the binomial coefficients, acting as integer multiples.

::: {#thm-binomial-commutative-ring}
[The Binomial Theorem in a Commutative Ring]

Let \( R \) be a commutative ring, \( x, y \in R \) and \( n \in \nN \). Then
\[
(x + y)^n = \sum_{k=0}^{n} \binom{n}{k} \cdot \bigl( x^k y^{n-k} \bigr) .
\]
:::

Here \( \binom{n}{k} \cdot z \) is the integer multiple of Section 2.5, and \( n - k \in \nN \) since \( k \le n \).

::: {.idea}
Induct on \( n \), with \( (x + y)^{n+1} = (x + y)^n x + (x + y)^n y \). Multiplying the sum for \( (x + y)^n \) by \( x \) raises every power of \( x \) by one, which shifts the coefficients one place to the right; multiplying by \( y \) leaves them in place. Adding the two rows entry by entry is exactly Pascal's rule. The work is in lining the two sums up over the same range \( k = 0, \dots, n + 1 \): the shifted sum gets a zero first term, and the other one a zero last term.
:::

::: {.proof}
Induction on \( n \) (@fd1:ax-induction). For \( n = 0 \), \( (x + y)^0 = 1 \) and the right side is \( \binom{0}{0} \cdot (x^0 y^0) = 1 \cdot (1 \cdot 1) = 1 \).

Suppose the formula holds for \( n \), and put \( t_k \coloneqq \binom{n}{k} \cdot (x^k y^{n-k}) \) for \( 0 \le k \le n \). By the power recursion, (F9) and @lem-ring-finite-sums (b) with (F6),
\[
(x + y)^{n+1} = (x + y)^n x + (x + y)^n y = \sum_{k=0}^{n} t_k x + \sum_{k=0}^{n} t_k y .
\]
By the rule \( (m \cdot a) b = m \cdot (ab) \) of @lem-integer-multiples (d), with (F5), (F6) and the power recursion,
\[
t_k x = \binom{n}{k} \cdot \bigl( x^{k+1} y^{n-k} \bigr) , \qquad t_k y = \binom{n}{k} \cdot \bigl( x^k y^{n+1-k} \bigr) .
\]
For \( 0 \le k \le n + 1 \) let \( z_k \coloneqq x^k y^{n+1-k} \), and define
\[
u_0 \coloneqq 0 , \quad u_k \coloneqq \binom{n}{k - 1} \cdot z_k \ (1 \le k \le n + 1) , \qquad w_k \coloneqq \binom{n}{k} \cdot z_k \ (0 \le k \le n + 1) .
\]
Then \( t_k x = u_{k+1} \) and \( t_k y = w_k \) for \( 0 \le k \le n \), and \( w_{n+1} = 0 \cdot z_{n+1} = 0 \), since \( \binom{n}{n+1} = 0 \). By @lem-ring-finite-sums (f) and \( u_0 = 0 \), and by splitting off the last term \( w_{n+1} = 0 \),
\[
\sum_{k=0}^{n} t_k x = \sum_{k=0}^{n+1} u_k , \qquad \sum_{k=0}^{n} t_k y = \sum_{k=0}^{n+1} w_k .
\]
So \( (x + y)^{n+1} = \sum_{k=0}^{n+1} (u_k + w_k) \) by @lem-ring-finite-sums (a). Finally, \( u_0 + w_0 = 0 + 1 \cdot z_0 = \binom{n+1}{0} \cdot z_0 \), and for \( k = j + 1 \) with \( 0 \le j \le n \), the sum rule of @lem-integer-multiples (d) and Pascal's rule give
\[
u_k + w_k = \binom{n}{j} \cdot z_k + \binom{n}{j + 1} \cdot z_k = \binom{n + 1}{j + 1} \cdot z_k = \binom{n + 1}{k} \cdot z_k .
\]
Hence \( (x + y)^{n+1} = \sum_{k=0}^{n+1} \binom{n+1}{k} \cdot (x^k y^{n+1-k}) \), which is the formula for \( n + 1 \). This proves the theorem.
:::

The proof used (F6) at every regrouping of \( x^k y^{n-k} x \), and the theorem needs it: the linear-algebra volumes meet matrices, whose multiplication is not commutative, and there the expansion holds only for pairs that commute. For \( R = \nZ \) the theorem is the familiar expansion, since there \( m \cdot z = mz \) (Section 2.5).

In row \( 5 \) of the table, the four middle entries \( 5, 10, 10, 5 \) are all multiples of \( 5 \); in row \( 6 \) the middle entries \( 15 \) and \( 20 \) are not multiples of \( 6 \). Primes are special.

::: {#lem-prime-divides-binomial}
[A Prime Divides the Middle Binomial Coefficients]

Let \( p \) be a prime and \( k \in \nN \) with \( 0 < k < p \). Then \( p \mid \binom{p}{k} \).
:::

::: {.proof}
We read the coefficients in \( \nN \subseteq \nZ \). By @prp-binomial-absorption with \( n = p - 1 \) and \( k - 1 \) in place of \( k \),
\[
k \binom{p}{k} = p \binom{p - 1}{k - 1} ,
\]
so \( p \mid k \binom{p}{k} \). Since \( 0 < k < p \), \( p \nmid k \): a positive multiple of \( p \) is at least \( p \) (@fd3:prp-divisibility-rules-integers (e)). Hence \( \gcd(p, k) = 1 \) by @cor-prime-divides-product (a), and @thm-euclid-lemma-integers gives \( p \mid \binom{p}{k} \). This proves the lemma.
:::

The hypothesis "prime" is needed: \( \binom{4}{2} = 6 \), and \( 4 \nmid 6 \). In the proof, \( 4 \mid 2 \binom{4}{2} \), but \( \gcd(4, 2) = 2 \), so Euclid's lemma does not apply.

::: {.check}
Use @prp-binomial-absorption to compute \( \binom{7}{3} \) from \( \binom{6}{2} = 15 \), and check that \( 7 \) divides it.
:::

::: {.solution}
With \( n = 6 \), \( k = 2 \): \( 3 \binom{7}{3} = 7 \binom{6}{2} = 7 \cdot 15 = 105 \), so \( \binom{7}{3} = 35 \), and \( 35 = 5 \cdot 7 \). (By Pascal's rule, \( \binom{7}{3} = \binom{6}{2} + \binom{6}{3} = 15 + 20 = 35 \), the same.)
:::

## The Frobenius map

We can now expand \( (x + y)^p \) in a field of characteristic \( p \).

::: {#thm-frobenius-homomorphism}
[The Frobenius Homomorphism]

Let \( F \) be a field of characteristic \( p > 0 \).

::: {.enumerate options="label=(\alph*)"}
1. For all \( x, y \in F \),
\[
(x + y)^p = x^p + y^p , \qquad (xy)^p = x^p y^p ,
\]
and \( 1^p = 1 \). So the **Frobenius map** \( \mathrm{Fr} \colon F \to F \), \( \mathrm{Fr}(x) \coloneqq x^p \), is a homomorphism, and it is injective.
2. \( (x - y)^p = x^p - y^p \) for all \( x, y \in F \).
3. If \( F \) is finite, then \( \mathrm{Fr} \) is an automorphism of \( F \).
:::
:::

By @thm-characteristic-prime, the hypothesis \( \operatorname{char} F = p > 0 \) already makes \( p \) prime.

*Try it first (ten minutes): expand \( (x + y)^5 \) and \( (x + y)^6 \) in \( \nF_5 \), using the rows \( n = 5 \) and \( n = 6 \) of the table above, and see which coefficients survive.*

::: {.idea}
For \( (x + y)^5 \) the coefficients \( 1, 5, 10, 10, 5, 1 \) become \( 1, 0, 0, 0, 0, 1 \) in \( \nF_5 \), and \( (x + y)^5 = x^5 + y^5 \). For \( (x + y)^6 \) the coefficients \( 1, 6, 15, 20, 15, 6, 1 \) become \( 1, 1, 0, 0, 0, 1, 1 \), and \( (x + y)^6 = x^6 + x^5 y + x y^5 + y^6 \): the extra terms survive because \( 6 \) is not the characteristic. So the plan is: expand by the binomial theorem; every middle coefficient \( \binom{p}{k} \) is a multiple of \( p \); and a multiple of \( p \) acts on \( F \) as \( 0 \), because \( p \cdot 1 = 0 \). The product rule and \( 1^p = 1 \) are power laws, and injectivity is free for a homomorphism of fields.

*Before reading on: where is it used that \( p \) is prime?*
:::

::: {.proof}
(a) By @thm-binomial-commutative-ring, \( (x + y)^p = \sum_{k=0}^{p} t_k \) with \( t_k \coloneqq \binom{p}{k} \cdot (x^k y^{p-k}) \). Let \( 0 < k < p \). By @lem-prime-divides-binomial, \( p \mid \binom{p}{k} \), so \( \binom{p}{k} \cdot 1 = 0 \) by @prp-characteristic-divides (a), and then, by @lem-integer-multiples (c) and @thm-field-basic-properties (d),
\[
t_k = \Bigl( \binom{p}{k} \cdot 1 \Bigr) \bigl( x^k y^{p-k} \bigr) = 0 \cdot \bigl( x^k y^{p-k} \bigr) = 0 .
\]
The end terms are \( t_0 = 1 \cdot (x^0 y^p) = y^p \) and \( t_p = 1 \cdot (x^p y^0) = x^p \). Let \( b_k \coloneqq t_k \) for \( k = 0 \) and \( b_k \coloneqq 0 \) otherwise, and \( c_k \coloneqq t_k \) for \( k = p \) and \( c_k \coloneqq 0 \) otherwise. Since \( p \ne 0 \), \( t_k = b_k + c_k \) for every \( 0 \le k \le p \), so by @lem-ring-finite-sums (a) and (d),
\[
(x + y)^p = \sum_{k=0}^{p} b_k + \sum_{k=0}^{p} c_k = t_0 + t_p = y^p + x^p ,
\]
which is \( x^p + y^p \) by (F1). Next, \( (xy)^p = x^p y^p \) is the third power law of this section's opening paragraph (@fd2:prp-power-laws (c), read in \( F \)), and \( 1^p = 1 \). So \( \mathrm{Fr} \) is a homomorphism (@def-field-homomorphism), and it is injective by @prp-field-homomorphism-properties (c).

(b) By @prp-field-homomorphism-properties (a), \( \mathrm{Fr}(x - y) = \mathrm{Fr}(x) - \mathrm{Fr}(y) \).

(c) The image \( \mathrm{Fr}(F) \) is a subset of \( F \), and \( \mathrm{Fr} \), with codomain \( \mathrm{Fr}(F) \), is a bijection \( F \to \mathrm{Fr}(F) \) by (a). If \( \mathrm{Fr}(F) \ne F \), this would be a bijection from the finite set \( F \) onto a proper subset, which @fd2:thm-finite-no-proper-copy forbids. So \( \mathrm{Fr}(F) = F \), \( \mathrm{Fr} \) is bijective, and a bijective homomorphism \( F \to F \) is an automorphism (@def-field-homomorphism). This proves the theorem.
:::

*Answer to the prompt.* Primality is used in one place: @lem-prime-divides-binomial, whose proof needs Euclid's lemma, and so needs \( p \) prime. It costs nothing here, since a positive characteristic is always prime (@thm-characteristic-prime).

In words: in characteristic \( p \), raising to the \( p \)-th power respects sums. The map is not the identity in general; Exercise C3 of Section 2.5 found that on the four-element field it exchanges two elements. On \( \nF_p \) itself it is the identity, and that is Fermat's little theorem.

::: {.warning}
"\( (x + y)^n = x^n + y^n \)" is not a general rule. In a field of characteristic \( p > 0 \) it holds for \( n = p \) (@thm-frobenius-homomorphism (a)), and so for \( n = p^2 \) by Exercise B2 (and in the same way for every power of \( p \)). With other exponents it can fail: in \( \nF_3 \), \( (1 + 1)^2 = 4 = 1 \), while \( 1^2 + 1^2 = 2 \). In a ring of composite characteristic it can fail even with \( n \) equal to the characteristic: in \( \nZ/4\nZ \), which has characteristic \( 4 \), \( ([1] + [1])^4 = [16] = [0] \), while \( [1]^4 + [1]^4 = [2] \); the middle coefficient \( \binom{4}{2} = 6 \) is not a multiple of \( 4 \). In \( \nZ \) the identity fails for every \( n \ge 2 \): \( (1 + 1)^n = 2^n \ne 2 \).
:::

## Fermat's little theorem

On \( \nF_p \), the Frobenius map is a homomorphism \( \nF_p \to \nF_p \), and by @cor-homomorphisms-fix-prime-subfield (b) there is only one such map, the identity. That is the whole proof of the first part below.

::: {#thm-fermat-little}
[Fermat's Little Theorem]

Let \( p \) be a prime.

::: {.enumerate options="label=(\alph*)"}
1. \( a^p = a \) for every \( a \in \nF_p \).
2. \( a^{p-1} = 1 \) for every non-zero \( a \in \nF_p \); so \( a^{-1} = a^{p-2} \).
3. For every \( a \in \nZ \), \( p \mid a^p - a \); and if \( p \nmid a \), then \( p \mid a^{p-1} - 1 \).
:::
:::

::: {.proof}
(a) \( \operatorname{char} \nF_p = p \) (@exm-characteristics), so \( \mathrm{Fr} \colon \nF_p \to \nF_p \) is a homomorphism by @thm-frobenius-homomorphism (a). By @cor-homomorphisms-fix-prime-subfield (b), the only homomorphism \( \nF_p \to \nF_p \) is the identity. Hence \( a^p = \mathrm{Fr}(a) = a \) for every \( a \in \nF_p \).

(b) Let \( a \ne 0 \). Since \( p \ge 2 \), \( p - 1 \in \nN \) and \( a \cdot a^{p-1} = a^{p-1} a = a^p = a = a \cdot 1 \), by (F6), the power recursion and (a). Canceling \( a \ne 0 \) (@thm-field-basic-properties (b)) gives \( a^{p-1} = 1 \). Likewise \( p - 2 \in \nN \) and \( a \cdot a^{p-2} = a^{p-1} = 1 \), so \( a^{-1} = a^{p-2} \) by uniqueness of inverses (@thm-field-basic-properties (c)).

(c) Write \( [a] \) for the class of \( a \in \nZ \) in \( \nF_p = \nZ/p\nZ \). Since \( [a][b] = [ab] \) (@thm-quotient-ring-by-ideal (b)), induction on \( n \) gives \( [a]^n = [a^n] \) for every \( n \in \nN \): \( [a]^0 = [1] = [a^0] \), and \( [a]^{n+1} = [a]^n [a] = [a^n][a] = [a^{n+1}] \). By (a), \( [a^p] = [a]^p = [a] \), so \( p \mid a^p - a \) (@thm-quotient-ring-by-ideal (a), for the ideal \( p\nZ \)). If \( p \nmid a \), then \( [a] \ne [0] \) (@thm-quotient-ring-by-ideal (d)), so \( [a^{p-1}] = [a]^{p-1} = [1] \) by (b), and \( p \mid a^{p-1} - 1 \). This proves the theorem.
:::

Primality is needed in (c). For the modulus \( 4 \) and \( a = 2 \), \( 2^4 - 2 = 14 \) is not a multiple of \( 4 \) (in \( \nZ/4\nZ \) this is \( ([1] + [1])^4 = [0] \ne [2] \), from the warning above), and although \( 4 \nmid 2 \), \( 2^3 - 1 = 7 \) is not a multiple of \( 4 \) either.

Part (b) gives a second way to invert in \( \nF_p \), besides the Euclidean algorithm of Chapter 1: \( a^{-1} = a^{p-2} \). It also reduces large exponents: for non-zero \( a \), only the remainder of the exponent on division by \( p - 1 \) matters, since \( a^{q(p-1)+r} = (a^{p-1})^q a^r = a^r \). Exercise C2 below gives a second proof of (a), by induction, and Chapter 4 gives another proof of (b), from a product of all the non-zero elements.

::: {#exm-frobenius-computations}
[Powers and inverses in prime fields]

::: {.enumerate options="label=(\roman*)"}
1. Compute \( 3^{100} \) in \( \nF_7 \).
2. Compute \( 2^{100} \) in \( \nF_{101} \).
3. Find the inverse of \( 7 \) in \( \nF_{31} \) twice: by @thm-fermat-little (b), and by the Euclidean algorithm.
4. What is the Frobenius map of \( \nF_p \)?
:::
:::

::: {.solution}
(i) \( 7 \) is prime (the small-primes remark of Section 1.2) and \( 3 \ne 0 \) in \( \nF_7 \), so \( 3^6 = 1 \) by @thm-fermat-little (b). Since \( 100 = 16 \cdot 6 + 4 \), the power laws give \( 3^{100} = (3^6)^{16} \, 3^4 = 1 \cdot 81 \), and \( 81 = 11 \cdot 7 + 4 \). So \( 3^{100} = 4 \) in \( \nF_7 \).

(ii) \( 101 \) is prime: by the remark after @lem-least-divisor-prime it suffices that no \( d \) with \( 2 \le d \) and \( d \cdot d \le 101 \), that is \( 2 \le d \le 10 \), divides \( 101 \), and the remainders of \( 101 \) on division by \( 2, 3, \dots, 10 \) are \( 1, 2, 1, 1, 5, 3, 5, 2, 1 \). Since \( 2 \ne 0 \) in \( \nF_{101} \), @thm-fermat-little (b) gives \( 2^{100} = 2^{101 - 1} = 1 \). No multiplication was needed.

(iii) \( 31 \) is prime by the same test (\( d = 2, 3, 4, 5 \) leave remainders \( 1, 1, 3, 1 \)). *By Fermat:* since \( 7 \ne 0 \) in \( \nF_{31} \), @thm-fermat-little (b) gives \( 7^{-1} = 7^{29} \). Square repeatedly in \( \nF_{31} \): \( 7^2 = 49 = 18 \), \( 7^4 = 18^2 = 324 = 14 \), \( 7^8 = 14^2 = 196 = 10 \), \( 7^{16} = 10^2 = 100 = 7 \). With \( 29 = 16 + 8 + 4 + 1 \),
\[
7^{29} = 7^{16} \, 7^{8} \, 7^{4} \, 7 = 7 \cdot 10 \cdot 14 \cdot 7 = 70 \cdot 98 = 8 \cdot 5 = 40 = 9 .
\]
*By Euclid:* \( 31 = 4 \cdot 7 + 3 \) and \( 7 = 2 \cdot 3 + 1 \), so
\[
1 = 7 - 2 \cdot 3 = 7 - 2(31 - 4 \cdot 7) = 9 \cdot 7 - 2 \cdot 31 ,
\]
and \( 7^{-1} = 9 \) by @thm-units-mod-n. Both routes give \( 9 \). Check: \( 7 \cdot 9 = 63 = 2 \cdot 31 + 1 \). For small \( p \) the Euclidean algorithm is shorter; Fermat's route needs no back-substitution, only squaring.

(iv) The identity, by @thm-fermat-little (a): \( \mathrm{Fr}(a) = a^p = a \) for every \( a \in \nF_p \).
:::

::: {.check}
Compute \( 2^6 \) in \( \nF_7 \) and \( 3^{10} \) in \( \nF_{11} \), with and without @thm-fermat-little.
:::

::: {.solution}
Both are \( 1 \). Without it: \( 2^6 = 64 = 9 \cdot 7 + 1 \); and \( 3^5 = 243 = 22 \cdot 11 + 1 \), so \( 3^{10} = (3^5)^2 = 1 \). With it: \( 7 \) and \( 11 \) are prime, \( 2 \ne 0 \) in \( \nF_7 \) and \( 3 \ne 0 \) in \( \nF_{11} \), and the exponents are \( 7 - 1 \) and \( 11 - 1 \).
:::

## Exercises

### A. Check your understanding

::: {#exr-frobenius-and-fermat-a1}
[A1]

These parts are about @thm-frobenius-homomorphism and its proof.

::: {.enumerate options="label=(\alph*)"}
1. Where in the proof of (a) is it used that \( p \) is prime, and why does the theorem not need "\( p \) prime" as a separate hypothesis?
2. List \( \binom{5}{k} \) for \( 0 \le k \le 5 \) and \( \binom{6}{k} \) for \( 0 \le k \le 6 \). Which are divisible by \( 5 \), and which by \( 6 \)?
3. Why is \( \mathrm{Fr} \) injective? Does the proof use that \( F \) is finite?
4. State the idea of the proof of (a) in two sentences.
:::
:::

::: {.solution}
(a) In @lem-prime-divides-binomial, through Euclid's lemma: \( p \mid k\binom{p}{k} \) gives \( p \mid \binom{p}{k} \) only because \( \gcd(p, k) = 1 \), which needs \( p \) prime. A positive characteristic is always prime (@thm-characteristic-prime), so "\( \operatorname{char} F = p > 0 \)" already includes it.

(b) Row \( 5 \): \( 1, 5, 10, 10, 5, 1 \); the four middle ones are divisible by \( 5 \), the end ones are not. Row \( 6 \): \( 1, 6, 15, 20, 15, 6, 1 \); only the two \( 6 \)'s are divisible by \( 6 \), and \( 15 \), \( 20 \) are not. This is why \( (x + y)^6 \ne x^6 + y^6 \) in a ring of characteristic \( 6 \) such as \( \nZ/6\nZ \).

(c) Every homomorphism of fields is injective (@prp-field-homomorphism-properties (c)): \( \mathrm{Fr}(a) = 0 \) only for \( a = 0 \). The proof of injectivity does not use finiteness; finiteness is used only for surjectivity in (c).

(d) Expand \( (x + y)^p \) by the binomial theorem; every middle coefficient \( \binom{p}{k} \) is a multiple of \( p \). In characteristic \( p \), \( p \cdot 1 = 0 \), so every middle term vanishes and only \( x^p + y^p \) remains.
:::

### B. Practice

::: {#exr-frobenius-and-fermat-b1}
[B1]

Compute \( 5^{38} \) in \( \nF_{13} \), and find the inverse of \( 5 \) in \( \nF_{13} \) by @thm-fermat-little.
:::

::: {.solution}
\( 13 \) is prime (no \( d \) with \( 2 \le d \le 3 \) divides it, and \( 4 \cdot 4 > 13 \); the remark after @lem-least-divisor-prime), and \( 5 \ne 0 \) in \( \nF_{13} \). By @thm-fermat-little (b), \( 5^{12} = 1 \). Since \( 38 = 3 \cdot 12 + 2 \), \( 5^{38} = (5^{12})^3 \, 5^2 = 25 = 12 \) in \( \nF_{13} \). For the inverse, \( 5^{-1} = 5^{11} \). Now \( 5^2 = 12 = -1 \), so \( 5^{10} = (5^2)^5 = (-1)^5 = -1 \) and \( 5^{11} = -5 = 8 \). Check: \( 5 \cdot 8 = 40 = 3 \cdot 13 + 1 \). Hence \( 5^{38} = 12 \) and \( 5^{-1} = 8 \).
:::

::: {#exr-frobenius-and-fermat-b2}
[B2]

Let \( F \) be a field of characteristic \( p > 0 \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( (x + y)^{p^2} = x^{p^2} + y^{p^2} \) for all \( x, y \in F \).
2. Show that \( \bigl( \sum_{i=1}^{m} x_i \bigr)^p = \sum_{i=1}^{m} x_i^p \) for all \( m \in \nN \) and \( x_1, \dots, x_m \in F \).
:::
:::

::: {.solution}
(a) \( \mathrm{Fr} \circ \mathrm{Fr} \) is a homomorphism, as a composite of homomorphisms (@prp-field-homomorphism-properties (e)), and \( (\mathrm{Fr} \circ \mathrm{Fr})(x) = (x^p)^p = x^{p^2} \) by the power law \( (x^m)^n = x^{mn} \). Applying its additivity to \( x + y \) gives the claim.

(b) Induction on \( m \). For \( m = 0 \) both sides are \( 0 \): the empty sum is \( 0 \), and \( 0^p = 0^{p-1} \cdot 0 = 0 \) as \( p \ge 1 \). If the claim holds for \( m \), split off the last term and use @thm-frobenius-homomorphism (a):
\[
\Bigl( \sum_{i=1}^{m+1} x_i \Bigr)^p = \Bigl( \sum_{i=1}^{m} x_i + x_{m+1} \Bigr)^p = \Bigl( \sum_{i=1}^{m} x_i \Bigr)^p + x_{m+1}^p = \sum_{i=1}^{m+1} x_i^p .
\]
:::

::: {#exr-frobenius-and-fermat-b3}
[B3]

Let \( p \) be a prime. Show that the solutions \( x \in \nF_p \) of \( x^{p-1} = 1 \) are exactly the non-zero elements, and that every \( a \in \nF_p \) satisfies \( a^p - a = 0 \).
:::

::: {.solution}
Every non-zero \( a \) satisfies \( a^{p-1} = 1 \) by @thm-fermat-little (b). The element \( 0 \) does not: since \( p - 1 \ge 1 \), \( 0^{p-1} = 0^{p-2} \cdot 0 = 0 \ne 1 \). So the solutions are exactly the non-zero elements. And \( a^p - a = a - a = 0 \) for every \( a \) by @thm-fermat-little (a).
:::

### C. Going deeper

::: {#exr-frobenius-and-fermat-c1}
[C1: Exit check: the Frobenius identity]

Let \( F \) be a field of characteristic \( p > 0 \). Using @thm-binomial-commutative-ring and @lem-prime-divides-binomial, prove that \( \mathrm{Fr} \colon F \to F \), \( x \mapsto x^p \), is an injective homomorphism.
:::

::: {.solution}
*Sums.* By @thm-binomial-commutative-ring, \( (x + y)^p = \sum_{k=0}^{p} \binom{p}{k} \cdot (x^k y^{p-k}) \). For \( 0 < k < p \), \( \binom{p}{k} \cdot (x^k y^{p-k}) = (\binom{p}{k} \cdot 1)(x^k y^{p-k}) \) by @lem-integer-multiples (c). By @lem-prime-divides-binomial, \( p \mid \binom{p}{k} \), and since \( \operatorname{char} F = p \), \( \binom{p}{k} \cdot 1 = 0 \) (@prp-characteristic-divides (a)); so the term is \( 0 \) (@thm-field-basic-properties (d)). The terms \( k = 0 \) and \( k = p \) are \( 1 \cdot y^p = y^p \) and \( 1 \cdot x^p = x^p \), since \( \binom{p}{0} = \binom{p}{p} = 1 \) and \( x^0 = y^0 = 1 \). A sum whose terms vanish except at two places is the sum of those two terms (@lem-ring-finite-sums (a), (d)), so \( (x + y)^p = x^p + y^p \).

*Products and one.* \( (xy)^p = x^p y^p \) by the power law \( (xy)^n = x^n y^n \), and \( 1^p = 1 \). So \( \mathrm{Fr} \) is a homomorphism (@def-field-homomorphism).

*Injective.* Every homomorphism of fields is injective (@prp-field-homomorphism-properties (c)).

**Marking scheme.** (10 points)

- 2: the binomial expansion written with integer multiples \( \binom{p}{k} \cdot (x^k y^{p-k}) \).
- 2: each middle term reduced to a multiple that vanishes, with the rule named (for example \( (\binom{p}{k} \cdot 1)(x^k y^{p-k}) \) by \( (m \cdot 1) a = m \cdot a \), or \( \binom{p}{k} \cdot z = q \cdot (p \cdot z) \) where \( \binom{p}{k} = qp \)).
- 2: that multiple is \( 0 \) from \( p \mid \binom{p}{k} \) and \( \operatorname{char} F = p \), with both reasons named.
- 1: the end terms \( y^p \) and \( x^p \).
- 1: \( (xy)^p = x^p y^p \) and \( 1^p = 1 \).
- 2: injectivity, by @prp-field-homomorphism-properties (c) or by any correct direct argument.

Second route for injectivity: \( x^p = y^p \Rightarrow (x - y)^p = 0 \Rightarrow x = y \) earns the 2 points, 1 for \( (x - y)^p = x^p - y^p \) with its reason (@prp-field-homomorphism-properties (a), or \( (-y)^p = -y^p \) for every prime \( p \), the even one included), and 1 for \( x - y = 0 \) because a field has no zero divisors.

Fatal errors (0 for the step): "\( \binom{p}{k} = 0 \)" as an integer; using \( (x + y)^p = x^p + y^p \) in its own proof.
:::

::: {#exr-frobenius-and-fermat-c2}
[C2: Fermat by induction]

Let \( p \) be a prime. Give another proof of @thm-fermat-little (a) and of the first claim of @thm-fermat-little (c), without @cor-homomorphisms-fix-prime-subfield. In (a) use only @thm-frobenius-homomorphism (a) (with \( \operatorname{char} \nF_p = p \), @exm-characteristics) and @thm-integers-mod-n-ring (b), (d); in (b) you may also use @thm-quotient-ring-by-ideal.

::: {.enumerate options="label=(\alph*)"}
1. prove by induction on \( r \in \nN \) that \( (r \cdot 1)^p = r \cdot 1 \) in \( \nF_p \), and deduce \( a^p = a \) for every \( a \in \nF_p \);
2. deduce that \( p \mid a^p - a \) for every integer \( a \).
:::
:::

::: {.solution}
(a) For \( r = 0 \): \( (0 \cdot 1)^p = 0^p = 0^{p-1} \cdot 0 = 0 = 0 \cdot 1 \), as \( p \ge 1 \). If \( (r \cdot 1)^p = r \cdot 1 \), then by @thm-frobenius-homomorphism (a) (\( \operatorname{char} \nF_p = p \), @exm-characteristics),
\[
((r + 1) \cdot 1)^p = (r \cdot 1 + 1)^p = (r \cdot 1)^p + 1^p = r \cdot 1 + 1 = (r + 1) \cdot 1 .
\]
Every element of \( \nF_p \) is \( [r] \) for some \( r \in \{0, \dots, p - 1\} \) (@thm-integers-mod-n-ring (b)), and \( [r] = r \cdot [1] \) (part (d) there). So \( a^p = a \) for every \( a \in \nF_p \).

(b) Let \( a \in \nZ \). Then \( [a] \in \nF_p \), so \( [a]^p = [a] \) by (a). By induction on \( n \), \( [a]^n = [a^n] \), using \( [a][b] = [ab] \) (@thm-quotient-ring-by-ideal (b)), as in the proof of @thm-fermat-little (c). So \( [a^p] = [a] \), and \( p \mid a^p - a \) (@thm-quotient-ring-by-ideal (a), for the ideal \( p\nZ \)). (This proves only what @thm-fermat-little already gives; it is practice with the Frobenius identity, and nothing cites it.)
:::

::: {#exr-frobenius-and-fermat-c3}
[C3: Roots of order p]

Let \( F \) be a finite field of characteristic \( p \). Show that for every \( a \in F \) the equation \( x^p = a \) has **exactly one** solution \( x \in F \). Deduce that in \( \nF_p \), the only solution of \( x^p = a \) is \( x = a \).
:::

::: {.solution}
By @cor-finite-field-prime-characteristic (a), \( p \) is a prime, so \( p > 0 \), and by @thm-frobenius-homomorphism (c), \( \mathrm{Fr} \) is a bijection \( F \to F \). Surjectivity gives a solution of \( \mathrm{Fr}(x) = a \), and injectivity says there is at most one. In \( \nF_p \), \( x = a \) is a solution by @thm-fermat-little (a), \( a^p = a \), so it is the only one. The uniqueness half needs only that \( \mathrm{Fr} \) is injective, so it holds in every field of characteristic \( p > 0 \) (@thm-frobenius-homomorphism (a)); existence used the finiteness of \( F \).
:::

### R. Review

::: {#exr-frobenius-and-fermat-r1}
[R1]

Find all \( z \in \nC \) with \( z^2 = -3 + 4i \), and explain why there are exactly two.
:::

::: {.solution}
By the square-root formula of @fd4:prp-complex-square-roots, with \( a = -3 \), \( b = 4 \): \( r = \abs{-3 + 4i} = 5 \) (since \( 9 + 16 = 25 \)), \( (r + a)/2 = 1 \), \( (r - a)/2 = 4 \), and \( b > 0 \), so \( w = 1 + 2i \). Check: \( (1 + 2i)^2 = 1 + 4i + 4i^2 = -3 + 4i \). By @cor-field-squares-equal in the field \( \nC \) (@exm-fields), \( z^2 = w^2 \) if and only if \( z = w \) or \( z = -w \). So the solutions are \( 1 + 2i \) and \( -1 - 2i \). They are two, not one: \( w = -w \) would give \( 2w = 0 \), hence \( w = 0 \), since \( 2 \ne 0 \) in \( \nC \) (\( \operatorname{char} \nC = 0 \), @exm-characteristics, with @prp-characteristic-divides (b)).
:::

::: {#exr-frobenius-and-fermat-r2}
[R2]

Show that \( 7 \) has no square root in \( \nQ(\sqrt 2) \).
:::

::: {.solution}
Suppose \( (a + b\sqrt 2)^2 = 7 \) with \( a, b \in \nQ \). Expanding, \( (a^2 + 2b^2) + 2ab\sqrt 2 = 7 + 0 \sqrt 2 \), so by unique representation (@prp-cof-sqrt2-field-archimedean (a)), \( 2ab = 0 \) and \( a^2 + 2b^2 = 7 \). Since \( 2 \ne 0 \) in \( \nQ \) (\( \operatorname{char} \nQ = 0 \), @exm-characteristics, with @prp-characteristic-divides (b)), @thm-field-basic-properties (f) applied twice (to \( 2 \cdot (ab) = 0 \), then to \( ab = 0 \)) gives \( a = 0 \) or \( b = 0 \). If \( b = 0 \), then \( a^2 = 7 \). If \( a = 0 \), then \( 2b^2 = 7 \), so \( (2b)^2 = 14 \). Both are excluded by the claim stated with @prp-cof-sqrt2-field-incomplete: no natural number \( n \) with \( k^2 < n < (k + 1)^2 \) for some \( k \in \nN \) is the square of a rational; take \( (n, k) = (7, 2) \), as \( 4 < 7 < 9 \), and \( (n, k) = (14, 3) \), as \( 9 < 14 < 16 \). So \( 7 \) has no square root in \( \nQ(\sqrt 2) \). This is the method of *Number Systems: From \(\nN\) to \(\nR\)*, Chapter 6, which showed the same for \( 3 \).
:::

::: {#exr-frobenius-and-fermat-r3}
[R3]

Show that no relation \( < \) makes \( \nQ(i) \) (@exm-subfields-gaussian) an ordered field, and none makes the four-element field \( F \) of Exercise C1 of Section 2.2 an ordered field.
:::

::: {.solution}
*\( F \).* In \( F \), \( 1 + 1 = (1 + 1) + (0 + 0)\alpha = 0 \), by the definition of the sum, with coefficients in \( \nF_2 \). So \( 2 \cdot 1 = 0 \) and \( \operatorname{char} F \ne 0 \), while every ordered field has characteristic \( 0 \) (@exm-characteristics). This is the method of @thm-integers-mod-n-ring (e) and @fd3:exm-finite-ring-not-orderable: in an ordered field \( n \cdot 1 > 0 \) for \( n \ge 1 \) (@fd3:prp-ordered-ring-rules (h)), while here \( 2 \cdot 1 = 0 \).

*\( \nQ(i) \).* This is the method of @fd4:prp-complex-not-orderable; the proposition itself does not apply, since an order on the subfield \( \nQ(i) \) need not extend to \( \nC \). Suppose \( < \) made \( \nQ(i) \) an ordered field. Then \( i \ne 0 \) gives \( i^2 > 0 \), and \( 1 \ne 0 \) gives \( 1 > 0 \) (@fd3:prp-ordered-ring-rules (e)). But \( i^2 = -1 \) (@fd4:prp-reals-embed-complex; the operations of \( \nQ(i) \) are those of \( \nC \)), and \( 1 > 0 \) gives \( -1 < 0 \) (@fd3:prp-ordered-ring-rules (a)). So \( 0 < -1 < 0 \), and \( 0 < 0 \) by transitivity, which is impossible for the strict part of an order. The characteristic does not help here, since \( \operatorname{char} \nQ(i) = 0 \) (@exm-characteristics): the obstruction for \( \nQ(i) \) is a square, not a multiple of \( 1 \).
:::

::: {#exr-frobenius-and-fermat-r4}
[R4]

Find all homomorphisms \( \nQ(\sqrt 2) \to \nR \).
:::

::: {.solution}
There are exactly two: the inclusion \( a + b\sqrt 2 \mapsto a + b\sqrt 2 \), and \( a + b\sqrt 2 \mapsto a - b\sqrt 2 \).

*Every homomorphism is one of them.* Let \( \sigma \colon \nQ(\sqrt 2) \to \nR \) be a homomorphism. The inclusions \( \nQ \to \nQ(\sqrt 2) \) and \( \nQ \to \nR \) are homomorphisms (@exm-complex-conjugation-automorphism (ii); \( \nQ \) is a subfield of both), so they are \( \iota_{\nQ(\sqrt 2)} \) and \( \iota_{\nR} \) by the uniqueness clause of @thm-prime-subfield (b) (both fields have characteristic \( 0 \), @exm-characteristics). By @cor-homomorphisms-fix-prime-subfield (a), \( \sigma \circ \iota_{\nQ(\sqrt 2)} = \iota_{\nR} \): \( \sigma(q) = q \) for every \( q \in \nQ \). Then
\[
\sigma(\sqrt 2)^2 = \sigma\bigl( (\sqrt 2)^2 \bigr) = \sigma(2) = 2 = (\sqrt 2)^2 ,
\]
so \( \sigma(\sqrt 2) = \sqrt 2 \) or \( \sigma(\sqrt 2) = -\sqrt 2 \) by @cor-field-squares-equal in \( \nR \). Hence \( \sigma(a + b\sqrt 2) = \sigma(a) + \sigma(b)\sigma(\sqrt 2) = a \pm b\sqrt 2 \).

*Both occur.* The inclusion is a homomorphism (@exm-complex-conjugation-automorphism (ii)), and so is conjugation \( a + b\sqrt 2 \mapsto a - b\sqrt 2 \) of \( \nQ(\sqrt 2) \) followed by the inclusion (@exm-complex-conjugation-automorphism (iii) and @prp-field-homomorphism-properties (e)). They differ at \( \sqrt 2 \), since \( \sqrt 2 > 0 > -\sqrt 2 \).

*The tool, and the look-alikes.* The tool is rigidity on the prime subfield (@cor-homomorphisms-fix-prime-subfield) followed by "push the equation \( x^2 = 2 \) through \( \sigma \)". The uniqueness theorem for complete ordered fields of *Number Systems: From \(\nN\) to \(\nR\)*, Chapter 6 (@fd3:thm-cof-field-automorphism-identity) does not apply: it concerns maps of a complete ordered field to itself, and \( \nQ(\sqrt 2) \) is not complete. Nor does "a homomorphism into an ordered field preserves order": the second homomorphism sends \( \sqrt 2 > 0 \) to \( -\sqrt 2 < 0 \).
:::

<!-- dependency ledger
lem-ring-finite-sums (proof): finite sums, products, powers in a commutative ring R; finite-lists, shifting-the-index, splitting-off-the-last-term remarks; power laws (a)-(c) | fd2:def-sum-product, fd2:def-power, fd2:prp-power-laws (a)-(c) used as templates with X = R (fd2:thm-recursion read on omega, fd3:cor-omega-identification (b)); stated in the opening paragraph; their proofs use only (F1)-(F7), (F9) and induction
lem-ring-finite-sums (proof): sum_{k=0}^{0} a_k = a_0 | fd2:def-sum-product (general bounds) with the empty sum 0, and (F1), (F3)
thm-binomial-commutative-ring (proof): x^k x = x^{k+1}, y^{n-k} y = y^{n+1-k}, (n + 1) - (k + 1) = n - k | power recursion (template, opening paragraph); arithmetic of omega, fd3:cor-omega-identification (c)
def-binomial-coefficients (claim): the three facts C(n, k) = 0 for k > n, C(n, n) = 1, C(n, 1) = n; table rows 0-6 | inline inductions; verify/ch02/def-binomial-coefficients.py
prp-binomial-absorption (proof): arithmetic in N (distributivity, (j + 2) = (j + 1) + 1) | arithmetic of omega, fd3:cor-omega-identification (c); fd2:lem-naturals-arithmetic read on omega
prp-binomial-absorption (idea): 1 * 3 = 3 * 1; 2 * 6 = 4 * 3 | verify/ch02/prp-binomial-absorption.py
thm-binomial-commutative-ring (claim): matrix multiplication is not commutative, the expansion needs commuting pairs | linear-algebra volumes, prose comparison only; nothing depends on it
lem-prime-divides-binomial (claim): (check) C(7, 3) = 35 | verify/ch02/lem-prime-divides-binomial.py
lem-prime-divides-binomial (proof): coefficients read in N subset Z; p - 1, k - 1 in N | fd3:prp-naturals-embed-integers (a); arithmetic of omega
thm-frobenius-homomorphism (proof): (xy)^p = x^p y^p; 1^p = 1 | fd2:prp-power-laws (c) under the template line; inline induction for 1^n
thm-frobenius-homomorphism (idea): try-it-first coefficients of (x + y)^5, (x + y)^6 in F5 | verify/ch02/thm-frobenius-homomorphism.py
thm-frobenius-homomorphism (claim): (warning) (1 + 1)^2 = 1 in F3; ([1] + [1])^4 = [0] in Z/4Z; C(4, 2) = 6 | verify/ch02/thm-frobenius-homomorphism.py
thm-frobenius-homomorphism (claim): (opening) 3^5 = 243 = 3, 1 + 32 = 33 = 3 in F5 | verify/ch02/thm-frobenius-homomorphism.py
thm-frobenius-homomorphism (claim): (after the proof) Fr exchanges two elements of the four-element field | exr-characteristic-and-prime-subfield-c3, named only, nothing rests on it
thm-fermat-little (proof): p - 1, p - 2 in N for p >= 2 | arithmetic of omega
thm-fermat-little (proof): [a]^n = [a^n] by induction; [u] = [v] iff p | u - v | thm-quotient-ring-by-ideal (a), (b); fd1:ax-induction; inline
thm-fermat-little (claim): (after the proof) 2^4 - 2 = 14 and 2^3 - 1 = 7 are not multiples of 4; 4 does not divide 2 | verify/ch02/thm-fermat-little.py
thm-fermat-little (claim): (after the proof) a^{q(p-1)+r} = (a^{p-1})^q a^r | fd2:prp-power-laws (a), (b) under the template line; inline
thm-fermat-little (claim): Chapter 4 gives another proof of (b) | F5.4 blueprint, section 04 C4 (prose pointer; nothing depends on it)
exm-frobenius-computations (example): 7, 101, 31 prime; 100 = 16 * 6 + 4; 81 = 4 in F7; repeated squares of 7 in F31; 31 = 4 * 7 + 3 | small-primes remark (F5.1 §02); remark after lem-least-divisor-prime; verify/ch02/exm-frobenius-computations.py
thm-fermat-little (claim): (check) 2^6 = 1 in F7; 3^5 = 243 = 1 in F11 | verify/ch02/thm-fermat-little.py
exr-frobenius-and-fermat-a1 (solution): rows 5 and 6 | verify/ch02/exr-frobenius-and-fermat-a1.py
exr-frobenius-and-fermat-b1 (solution): 13 prime; 5^38 = 12, 5^{-1} = 8 in F13 | remark after lem-least-divisor-prime; verify/ch02/exr-frobenius-and-fermat-b1.py
exr-frobenius-and-fermat-b2 (solution): (x^m)^n = x^{mn}; empty sum 0 | fd2:prp-power-laws (b), fd2:def-sum-product, templates
exr-frobenius-and-fermat-c2 (solution): [a]^n = [a^n] for every a in Z | induction as in the proof of thm-fermat-little (c), with thm-quotient-ring-by-ideal (b); verify/ch02/exr-frobenius-and-fermat-c2.py
exr-frobenius-and-fermat-r1 (solution): |-3 + 4i| = 5, (1 + 2i)^2 = -3 + 4i | prp-complex-square-roots (F4.1, see edge; R item); verify/ch02/exr-frobenius-and-fermat-r1.py
exr-frobenius-and-fermat-r2 (solution): (a + b sqrt2)^2 = (a^2 + 2b^2) + 2ab sqrt2; 4 < 7 < 9, 9 < 14 < 16 | prp-cof-sqrt2-field-archimedean (a); the claim stated with prp-cof-sqrt2-field-incomplete (F3.4, soft); verify/ch02/exr-frobenius-and-fermat-r2.py
exr-frobenius-and-fermat-r3 (solution): i^2 = -1 in Q(i), whose operations are those of C | prp-reals-embed-complex (F4.1, see edge; R item); exm-subfields-gaussian (i)
exr-frobenius-and-fermat-r3 (solution): 1 + 1 = 0 in the four-element field | definition of the sum in exr-finite-fields-from-modular-arithmetic-c1, with 1 + 1 = 0 in F_2; verify/ch02/exr-frobenius-and-fermat-r3.py
exr-frobenius-and-fermat-r4 (solution): Q is a subfield of Q(sqrt2) and of R; sqrt2 > 0 | exm-q-sqrt2-field, exm-subfields-gaussian (iii); fd3:prp-cof-square-roots (soft)
-->
