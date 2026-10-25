# Units, Prime Moduli, and the Chinese Remainder Theorem

Section 3.4 made \( \nZ/n\nZ \) a commutative ring, and @exm-integers-mod-six put two of these rings side by side. In \( \nZ/5\nZ \) every non-zero class has a partner whose product with it is \( [1] \), so we may divide by it. In \( \nZ/6\nZ \) the class \( [2] \) has no such partner: the products \( [2][x] \) are only \( [0], [2], [4] \). Which classes can be divided by, and for which moduli can all non-zero classes? This section answers both questions with the gcd of Section 3.2, and finds a field with \( p \) elements for every prime \( p \). It then solves two congruences at once, the Chinese remainder theorem, by the move of Section 3.3, multiply the Bézout identity: write \( 1 \) as a combination and multiply.

Throughout, \( n \in \nZ_{>0} \) and classes are taken in \( \nZ/n\nZ \) unless another modulus is named. Two classes are equal exactly when their representatives are congruent:
\[
[u] = [v] \iff u - v \in n\nZ \iff n \mid u - v .
\]
The first equivalence is @fd2:thm-classes-partition (b) for the relation of @thm-quotient-ring-by-ideal (a); the second is the definition of \( n\nZ \) (@def-integer-linear-combinations) read with @fd2:def-divides. We call it the **class test**. Products of classes are computed on representatives, \( [u][v] = [uv] \) (@thm-quotient-ring-by-ideal (b)).

## Units of a commutative ring

In \( \nZ/6\nZ \) the equation \( [2][x] = [1] \) has no solution, while \( [5][x] = [1] \) has the solution \( [x] = [5] \). The elements that can be divided by are the ones that solve "\( u \) times something is \( 1 \)", and they deserve a name in every commutative ring at once.

*A unit is an element that has a multiplicative inverse in the ring itself.*

::: {#def-ring-unit}
[Unit of a Commutative Ring]

Let \( R \) be a commutative ring (@def-commutative-ring-and-field). An element \( u \in R \) is a **unit** of \( R \) if **there exists** \( v \in R \) with \( uv = 1 \). The set of units of \( R \) is written \( R^{\times} \). For a unit \( u \), the element \( v \) is **unique**; it is written \( u^{-1} \) and called the **inverse** of \( u \).
:::

In words: \( u \) is a unit when the equation \( ux = 1 \) can be solved **inside** \( R \). The definition asks for one solution; it does not ask \( u \) to be non-zero.

*Well-definedness of \( u^{-1} \).* Let \( uv = 1 \) and \( uv' = 1 \). Then, by (F7), (F5) and (F6),
\[
v = v \cdot 1 = v(uv') = (vu)v' = (uv)v' = 1 \cdot v' = v' .
\]
So the inverse is unique, and the notation \( u^{-1} \) names one element.

*Closure.* The element \( 1 \) is a unit, since \( 1 \cdot 1 = 1 \). If \( u \) is a unit, so is \( u^{-1} \), with \( (u^{-1})^{-1} = u \), because \( u^{-1} u = u u^{-1} = 1 \) by (F6). If \( u \) and \( w \) are units, then
\[
(uw)(u^{-1} w^{-1}) = (u u^{-1})(w w^{-1}) = 1 \cdot 1 = 1 ,
\]
reordering the four factors by (F5) and (F6); so \( uw \) is a unit and \( (uw)^{-1} = u^{-1} w^{-1} \), by uniqueness.

*A unit is not a zero divisor.* If \( u \) is a unit and \( ux = 0 \), then
\[
x = (u^{-1} u) x = u^{-1}(ux) = u^{-1} \cdot 0 = 0 ,
\]
by \( u^{-1} u = 1 \) (above) and \( 1 \cdot x = x \cdot 1 = x \) ((F6), (F7)) in the first equality, (F5) in the second, and @prp-ring-algebra (b) in the third. So a unit times a non-zero element is never \( 0 \).

**Examples.**

- **The integers.** \( \nZ^{\times} = \{ 1, -1 \} \). Indeed \( 1 \cdot 1 = 1 \) and \( (-1)(-1) = 1 \) (@prp-ring-algebra (c)). Conversely, \( uv = 1 \) says \( u \mid 1 \), so \( u = 1 \) or \( u = -1 \) by @prp-divisibility-rules-integers (g).
- **The rationals.** \( \nQ^{\times} = \nQ \setminus \{0\} \): every non-zero rational has an inverse by (F8) (@thm-rationals-field), and \( 0 \) is not a unit, since \( 0 \cdot v = 0 \ne 1 \) (@prp-ring-algebra (b)).
- **The integers modulo six.** By the multiplication table of @exm-integers-mod-six, the units of \( \nZ/6\nZ \) are \( [1] \) and \( [5] \), and \( [5]^{-1} = [5] \).
- **The zero ring** \( \{0\} \) of Section 2.3, where \( 1 = 0 \). Here \( 0 \cdot 0 = 0 = 1 \), so \( 0 \) is a unit and \( R^{\times} = R \). This degenerate case is why "every non-zero element is a unit" is not by itself the definition of a field.

*A non-example by minimal change.* Change \( 5 \) to \( 2 \) in the third example. The class \( [2] \in \nZ/6\nZ \) is non-zero, like \( [5] \), but \( [2][3] = [6] = [0] \): it is a zero divisor, so by the paragraph above it is **not** a unit. Concretely, the clause "there exists \( v \) with \( uv = 1 \)" fails: the products \( [2][x] \) for \( x = 0, \dots, 5 \) are \( [0], [2], [4], [0], [2], [4] \), and \( [1] \) is not among them.

**Why this definition.** With units, the field axiom (F8) reads: every non-zero element is a unit. So a field (@def-commutative-ring-and-field) is exactly a commutative ring with \( 1 \ne 0 \) in which \( R^{\times} = R \setminus \{0\} \); when \( 1 \ne 0 \), the element \( 0 \) is never a unit, since \( 0 \cdot v = 0 \) (@prp-ring-algebra (b)). The definition asks for an inverse in \( R \), not in some bigger ring: \( 2 \in \nZ \) has the inverse \( 1/2 \) in \( \nQ \), and it is still not a unit of \( \nZ \).

::: {.warning}
"Non-zero and not a zero divisor" does not make an element a unit. In \( \nZ \) there are no zero divisors at all (@prp-ordered-ring-rules (f)), yet \( 2 \) is not a unit, since \( 2 \nmid 1 \). The paragraph above proves only one direction: a unit is never a zero divisor. So "not a unit" must be checked against the definition, or, in \( \nZ/n\nZ \), by the next theorem.
:::

The units of a commutative ring are closed under products and inverses and contain \( 1 \): they form what *Algebraic Preliminaries*, Chapter 2 calls a group. Here we only need to find them in \( \nZ/n\nZ \).

## Which classes are units

In \( \nZ/6\nZ \) the units \( [1] \) and \( [5] \) are the classes of the integers coprime to \( 6 \), and the non-units \( [0], [2], [3], [4] \) share a factor with \( 6 \). The equation \( [a][x] = [1] \) says \( n \mid ax - 1 \), that is, \( ax + ny = 1 \) for some integer \( y \): a Bézout identity. So the question is answered by Section 3.2.

::: {#thm-units-mod-n}
[Units Modulo n]

Let \( n \in \nZ_{>0} \) and \( a \in \nZ \). Then \( [a] \) is a unit of \( \nZ/n\nZ \) **if and only if** \( \gcd(a, n) = 1 \). In that case, for **any** \( x, y \in \nZ \) with \( ax + ny = 1 \), \( [a]^{-1} = [x] \).
:::

::: {.idea}
Both directions translate between one equation in \( \nZ/n\nZ \) and one equation in \( \nZ \). A solution of \( [a][x] = [1] \) is an integer combination \( ax + ny = 1 \), and @cor-coprime-iff-combination says that such a combination exists exactly when \( \gcd(a, n) = 1 \). The class test does the translation.
:::

::: {.proof}
\( (\Leftarrow) \) Suppose \( \gcd(a, n) = 1 \). By @cor-coprime-iff-combination there are \( x, y \in \nZ \) with \( ax + ny = 1 \). Let \( x, y \) be any such pair. Then \( ax - 1 = -ny = (-y)n \), so \( n \mid ax - 1 \), and by the class test \( [ax] = [1] \). Hence \( [a][x] = [ax] = [1] \), where the first equality is the definition of the product on classes (@thm-quotient-ring-by-ideal (b)). So \( [a] \) is a unit, and \( [x] \) is its inverse, which is unique (@def-ring-unit); thus \( [a]^{-1} = [x] \) for every such pair.

\( (\Rightarrow) \) Suppose \( [a] \) is a unit. Every element of \( \nZ/n\nZ \) is the class of an integer (@fd2:def-quotient-set), so \( [a][x] = [1] \) for some \( x \in \nZ \). Then \( [ax] = [1] \), so \( n \mid ax - 1 \) by the class test: \( ax - 1 = yn \) for some \( y \in \nZ \). Hence \( ax + n(-y) = 1 \), and \( \gcd(a, n) = 1 \) by @cor-coprime-iff-combination. This proves the theorem.
:::

The theorem turns "is \( [a] \) invertible?" into a gcd, and the Euclidean algorithm (@thm-euclidean-algorithm-integers) computes the gcd. Back-substitution, as in @exm-euclidean-algorithm-run, then produces the \( x \) with \( ax + ny = 1 \), and with it the inverse. Whether \( \gcd(a, n) = 1 \) depends only on the class \( [a] \), since by the theorem it is equivalent to a statement about \( [a] \); so any representative may be used.

::: {#exm-unit-inverse-mod-n}
[Inverting a class modulo sixty]

Decide whether \( [17] \) and \( [12] \) are units of \( \nZ/60\nZ \), and find the inverse of each one that is.
:::

::: {.solution}
*The class \( [17] \).* Run the Euclidean algorithm on \( (60, 17) \):
\[
\begin{aligned}
60 &= 3 \cdot 17 + 9 , & 17 &= 1 \cdot 9 + 8 , \\
9 &= 1 \cdot 8 + 1 , & 8 &= 8 \cdot 1 + 0 .
\end{aligned}
\]
The last non-zero remainder is \( 1 \), so \( \gcd(60, 17) = 1 \) (@thm-euclidean-algorithm-integers (c)), and \( [17] \) is a unit by @thm-units-mod-n. Back-substitute, using the lines from the bottom up:
\[
\begin{aligned}
1 &= 9 - 8 = 9 - (17 - 9) = 2 \cdot 9 - 17 \\
&= 2 \cdot (60 - 3 \cdot 17) - 17 = 2 \cdot 60 - 7 \cdot 17 .
\end{aligned}
\]
So \( 17 \cdot (-7) + 60 \cdot 2 = 1 \), and @thm-units-mod-n gives \( [17]^{-1} = [-7] \). The representative in \( \{0, \dots, 59\} \) is \( 53 \), since \( -7 - 53 = -60 \). Check: \( 17 \cdot 53 = 901 = 15 \cdot 60 + 1 \), so \( [17][53] = [1] \).

*The class \( [12] \).* Here \( 12 \mid 60 \), so \( 12 \) is a common divisor of \( 12 \) and \( 60 \), and every common divisor of them divides \( 12 \); hence \( \gcd(12, 60) = 12 \ne 1 \) (@def-integer-gcd, with @prp-divisibility-rules-integers (e) for the comparison), and \( [12] \) is not a unit by @thm-units-mod-n. A witness: \( [12][5] = [60] = [0] \) with \( [5] \ne [0] \), so \( [12] \) is a zero divisor, and a unit never is (@def-ring-unit and the paragraph after it).
:::

::: {.check}
Find the inverse of \( [3] \) in \( \nZ/7\nZ \).
:::

::: {.solution}
\( [3]^{-1} = [5] \): \( 3 \cdot 5 = 15 = 2 \cdot 7 + 1 \), so \( [3][5] = [1] \). In the form of @thm-units-mod-n, \( 3 \cdot 5 + 7 \cdot (-2) = 1 \).
:::

## The field of integers modulo a prime

By @thm-units-mod-n, every non-zero class of \( \nZ/n\nZ \) is a unit exactly when every \( a \) with \( n \nmid a \) is coprime to \( n \). For a prime, @cor-prime-divides-product (a) says precisely this. For a composite \( n \), a proper factor of \( n \) is neither divisible by \( n \) nor coprime to it. So the field property sorts the moduli into primes and the rest.

::: {#thm-integers-mod-prime-field}
[The Integers Modulo n Form a Field Exactly When n Is Prime]

Let \( n \in \nZ \) with \( n \ge 2 \). Then \( \nZ/n\nZ \) is a field in the sense of @def-commutative-ring-and-field, that is, a commutative ring with \( [1] \ne [0] \) in which every non-zero element is a unit, **if and only if** \( n \) is prime.
:::

::: {.idea}
For a prime \( p \), a non-zero class \( [a] \) has \( p \nmid a \), so the only common divisors left are \( \pm 1 \), and @thm-units-mod-n inverts \( [a] \). For a composite \( n = rs \) with \( 1 < r, s < n \), the classes \( [r] \) and \( [s] \) are non-zero with product \( [n] = [0] \); a zero divisor cannot be a unit, so (F8) fails.
:::

::: {.proof}
By @thm-integers-mod-n-ring (a), \( \nZ/n\nZ \) is a commutative ring, and by @thm-integers-mod-n-ring (c), \( [1] \ne [0] \) since \( n \ge 2 \). So it is a field if and only if every non-zero class is a unit (@def-commutative-ring-and-field, (F8), and @def-ring-unit).

\( (\Leftarrow) \) Let \( n \) be prime, and let \( [a] \ne [0] \). By @thm-quotient-ring-by-ideal (d), \( a \notin n\nZ \), that is, \( n \nmid a \). By @cor-prime-divides-product (a), \( \gcd(n, a) = 1 \), and \( \gcd(a, n) = \gcd(n, a) \) (@def-integer-gcd). So \( [a] \) is a unit by @thm-units-mod-n.

\( (\Rightarrow) \) Let \( n \ge 2 \) be not prime. By @fd2:def-prime, \( n \) has a positive divisor \( r \notin \{1, n\} \); write \( n = rs \) with \( s \in \nZ \). Then \( 1 \le r \) by discreteness (@thm-integers-ordered-ring (c)) and \( r \le n \) by @prp-divisibility-rules-integers (e), so \( 1 < r < n \). Next, \( s > 0 \): if \( s \le 0 \), then \( rs \le 0 \) (\( rs = 0 \) if \( s = 0 \) by @prp-ring-algebra (b), and \( rs < r \cdot 0 = 0 \) if \( s < 0 \) by @prp-ordered-ring-rules (c)), against \( n > 0 \). So \( s \) is a positive divisor of \( n \), and \( s \le n \) by @prp-divisibility-rules-integers (e). Also \( s \ne n \): otherwise \( rn = n \), so \( (r - 1)n = 0 \) and \( r = 1 \) by @prp-ordered-ring-rules (f), since \( n \ne 0 \). Hence \( 0 < s < n \) as well.

Now \( [r] \ne [0] \): if \( n \mid r \), then \( n \le r \) by @prp-divisibility-rules-integers (e), since \( n, r > 0 \), against \( r < n \). In the same way \( [s] \ne [0] \). But \( [r][s] = [rs] = [n] = [0] \), by the class test. Suppose \( [r] \) were a unit. Then \( [s] = [0] \), since a unit is not a zero divisor (the paragraph after @def-ring-unit). This contradiction shows that the non-zero class \( [r] \) is not a unit, so \( \nZ/n\nZ \) is not a field. This proves the theorem.
:::

So for every prime \( p \) there is a field with exactly \( p \) elements (@thm-integers-mod-n-ring (b)). The smallest is \( \nZ/2\nZ \), whose tables are those of the two-element field of @exm-finite-ring-not-orderable with \( 0 \), \( 1 \) renamed \( [0] \), \( [1] \). *Algebraic Preliminaries*, Chapter 1 studies fields in general and gives these finite fields a name of their own.

::: {.remark}
In particular \( \nZ/5\nZ \) is a field, since \( 5 \) is prime (the small-primes remark of Section 3.1). In it \( 5 \cdot [1] = [5] = [0] \) (@thm-integers-mod-n-ring (d)), so \( [1] + [1] + [1] + [1] + [1] = [0] \) with \( [1] \ne [0] \), and no order makes it an ordered field (@thm-integers-mod-n-ring (e)). Being a field does not help a finite ring to be ordered.
:::

::: {.warning}
In \( \nZ/p\nZ \), "\( [a] \ne [0] \)" means \( p \nmid a \), not \( a \ne 0 \). The class \( [7] \) is the zero of \( \nZ/7\nZ \), and it has no inverse, although \( 7 \ne 0 \). The proof above applies @cor-prime-divides-product (a) to the condition \( p \nmid a \); with only \( a \ne 0 \) in hand, the case \( p \mid a \), \( \gcd(p, a) = p \), is left open.
:::

## Two congruences at once

A number leaves the remainder \( 2 \) on division by \( 3 \) and the remainder \( 3 \) on division by \( 5 \). What can it be? Each condition alone is a single class. The question is whether the two classes meet, and in how much. The next theorem says that for coprime moduli they always meet, and in exactly one class modulo the product.

::: {#thm-chinese-remainder-two}
[Chinese Remainder Theorem for Two Moduli]

Let \( m, n \in \nZ_{>0} \) with \( \gcd(m, n) = 1 \), and choose \( u, v \in \nZ \) with \( mu + nv = 1 \) (@cor-coprime-iff-combination).

::: {.enumerate options="label=(\alph*)"}
1. For all \( a, b \in \nZ \), the integer \( x \coloneqq a \cdot nv + b \cdot mu \) satisfies
\[
x \equiv a \pmod{m} \qquad \text{and} \qquad x \equiv b \pmod{n} ,
\]
and an integer \( x' \) satisfies both congruences **if and only if** \( x' \equiv x \pmod{mn} \).
2. The rule \( \Phi([x]_{mn}) \coloneqq ([x]_m, [x]_n) \) is a well-defined **bijection** \( \nZ/mn\nZ \to \nZ/m\nZ \times \nZ/n\nZ \). With \( + \) and \( \cdot \) on \( \nZ/m\nZ \times \nZ/n\nZ \) taken componentwise, for all \( x, y \in \nZ \),
\[
\begin{aligned}
\Phi([x]_{mn} + [y]_{mn}) &= \Phi([x]_{mn}) + \Phi([y]_{mn}) , \\
\Phi([x]_{mn}[y]_{mn}) &= \Phi([x]_{mn}) \, \Phi([y]_{mn}) ,
\end{aligned}
\]
and \( \Phi([1]_{mn}) = ([1]_m, [1]_n) \).
:::
:::

*Try it first (ten minutes): find an \( x \) with \( x \equiv 2 \pmod{3} \) and \( x \equiv 3 \pmod{5} \) by trying. Then use \( 1 = 2 \cdot 3 - 1 \cdot 5 \) to find a formula that works for every pair of right-hand sides.*

::: {.idea}
Trying works: among \( 3, 8, 13, \dots \), the numbers that are \( 3 \) modulo \( 5 \), the second one is \( 2 \) modulo \( 3 \). But trial and error gives one answer and no reason, and it does not say why no answer can be missing. The identity \( mu + nv = 1 \) supplies two special integers:
\[
e \coloneqq nv = 1 - mu , \qquad f \coloneqq mu = 1 - nv .
\]
The first is \( \equiv 1 \pmod{m} \) and \( \equiv 0 \pmod{n} \); the second the other way round. So \( ae + bf \) is \( a \) modulo \( m \) and \( b \) modulo \( n \), like a vector built from two coordinate vectors. For \( 3 \) and \( 5 \), \( e = -5 \) and \( f = 6 \), and \( 2e + 3f = 8 \). Uniqueness modulo \( mn \) is @prp-coprime-divisors-product: a difference divisible by \( m \) and by \( n \) is divisible by \( mn \).
:::

::: {.proof}
(a) Since \( nv - 1 = -mu \) and \( mu - 1 = -nv \),
\[
\begin{aligned}
x - a &= a(nv - 1) + bmu = m(bu - au) , \\
x - b &= anv + b(mu - 1) = n(av - bv) .
\end{aligned}
\]
So \( m \mid x - a \) and \( n \mid x - b \): \( x \equiv a \pmod{m} \) and \( x \equiv b \pmod{n} \) (@fd2:def-congruence).

Let \( x' \in \nZ \). Suppose first that \( x' \equiv a \pmod{m} \) and \( x' \equiv b \pmod{n} \). Then \( x' - x = (x' - a) - (x - a) \) is divisible by \( m \), and \( x' - x = (x' - b) - (x - b) \) by \( n \) (@prp-divisibility-rules-integers (c)). Since \( \gcd(m, n) = 1 \), @prp-coprime-divisors-product gives \( mn \mid x' - x \), that is, \( x' \equiv x \pmod{mn} \). Conversely, suppose \( mn \mid x' - x \). Since \( m \mid mn \), \( m \mid x' - x \) (@prp-divisibility-rules-integers (b)), and then \( m \mid (x' - x) + (x - a) = x' - a \) by @prp-divisibility-rules-integers (c). In the same way \( n \mid x' - b \). So \( x' \) satisfies both congruences.

(b) *Well defined.* Let \( k \in \{m, n\} \). If \( x \equiv x' \pmod{mn} \), then \( k \mid mn \mid x - x' \), so \( x \equiv x' \pmod{k} \) (@prp-divisibility-rules-integers (b)). By @fd2:thm-classes-partition (b) and @thm-well-defined-on-classes (a), applied to the identity map of \( \nZ \), with congruence modulo \( mn \) on the source and modulo \( k \) on the target, there is exactly one function \( \nZ/mn\nZ \to \nZ/k\nZ \) sending \( [x]_{mn} \) to \( [x]_k \). Pairing the two values for \( k = m \) and \( k = n \) gives the function \( \Phi \) into \( \nZ/m\nZ \times \nZ/n\nZ \) (@fd2:def-cartesian-product).

*Surjective.* Let \( (\alpha, \beta) \in \nZ/m\nZ \times \nZ/n\nZ \). By @fd2:def-quotient-set, \( \alpha = [a]_m \) and \( \beta = [b]_n \) for some \( a, b \in \nZ \). With \( x \) as in (a), \( x \equiv a \pmod{m} \) and \( x \equiv b \pmod{n} \), so \( \Phi([x]_{mn}) = ([x]_m, [x]_n) = ([a]_m, [b]_n) \) by @fd2:thm-classes-partition (b).

*Injective.* Let \( z, z' \in \nZ \) with \( \Phi([z]_{mn}) = \Phi([z']_{mn}) \). Then \( [z']_m = [z]_m \) and \( [z']_n = [z]_n \), so \( m \mid z' - z \) and \( n \mid z' - z \) by @fd2:thm-classes-partition (b). By @prp-coprime-divisors-product, \( mn \mid z' - z \), that is, \( [z']_{mn} = [z]_{mn} \). So \( \Phi \) is a bijection (@fd2:def-bijective).

*The operations.* By the definition of \( + \) on each of the three rings (@thm-quotient-ring-by-ideal (b)) and of the componentwise sum,
\[
\begin{aligned}
\Phi([x]_{mn} + [y]_{mn}) &= \Phi([x + y]_{mn}) = ([x + y]_m, [x + y]_n) \\
&= ([x]_m + [y]_m, [x]_n + [y]_n) = \Phi([x]_{mn}) + \Phi([y]_{mn}) .
\end{aligned}
\]
The same lines with \( xy \) in place of \( x + y \) give the product, and \( \Phi([1]_{mn}) = ([1]_m, [1]_n) \) is the definition. This proves the theorem.
:::

The theorem answers the opening question: the numbers with remainder \( 2 \) modulo \( 3 \) and remainder \( 3 \) modulo \( 5 \) form one class modulo \( 15 \), and the formula of (a) names a representative. Clause (b) says the same thing as a bijection. Each class modulo \( mn \) is the same information as a pair of classes, one modulo \( m \) and one modulo \( n \), and the sums and products of classes can be computed in either form. Each coordinate of \( \nZ/m\nZ \times \nZ/n\nZ \) is a commutative ring, so with zero \( ([0]_m, [0]_n) \), one \( ([1]_m, [1]_n) \) and negatives taken componentwise, every axiom (F1)–(F7), (F9) holds in each coordinate and hence for the pairs; then \( \Phi \) matches two commutative rings, element for element and operation for operation.

::: {#exm-chinese-remainder-instances}
[Two remainders at once, and two failures]

(i) Find every \( x \in \nZ \) with \( x \equiv 2 \pmod{3} \) and \( x \equiv 3 \pmod{5} \).

(ii) Show that \( x \equiv 0 \pmod{2} \), \( x \equiv 1 \pmod{4} \) has no solution, and that the solutions of \( x \equiv 0 \pmod{2} \), \( x \equiv 2 \pmod{4} \) are not one class modulo \( 8 \). Which hypothesis of @thm-chinese-remainder-two fails, and what happens to its map \( \Phi \colon \nZ/8\nZ \to \nZ/2\nZ \times \nZ/4\nZ \)?
:::

::: {.solution}
(i) Here \( m = 3 \), \( n = 5 \), and \( 1 = 2 \cdot 3 + (-1) \cdot 5 \), so \( \gcd(3, 5) = 1 \) (@cor-coprime-iff-combination) with \( u = 2 \), \( v = -1 \). By @thm-chinese-remainder-two (a),
\[
x = 2 \cdot 5 \cdot (-1) + 3 \cdot 3 \cdot 2 = -10 + 18 = 8 .
\]
Check: \( 8 = 2 \cdot 3 + 2 \) and \( 8 = 1 \cdot 5 + 3 \). The solutions are exactly the \( x' \) with \( x' \equiv 8 \pmod{15} \), the class \( 8 + 15\nZ = \{ \dots, -7, 8, 23, 38, \dots \} \).

(ii) Here \( \gcd(2, 4) = 2 \ne 1 \): \( 2 \) divides both, and every common divisor divides \( 2 \), since \( 2 = 1 \cdot 2 + 0 \cdot 4 \) (@prp-divisibility-rules-integers (c), (e)). The hypothesis \( \gcd(m, n) = 1 \) fails, and both halves of the conclusion fail with it.

*Existence fails.* If \( x \equiv 1 \pmod{4} \), then \( x = 4k + 1 = 2(2k) + 1 \) for some \( k \in \nZ \), so \( x \) has the form \( 2q + 1 \). If also \( x \equiv 0 \pmod{2} \), then \( x = 2q' \). No integer has both forms (@cor-integers-even-odd (a)), so there is no solution.

*Uniqueness modulo \( mn \) fails.* If \( x \equiv 2 \pmod{4} \), then \( x = 4k + 2 = 2(2k + 1) \), so \( x \equiv 0 \pmod{2} \) holds automatically, and the solutions are exactly the class \( 2 + 4\nZ \). It contains \( 2 \) and \( 6 \), but \( 6 - 2 = 4 \) and \( 8 \nmid 4 \) (@prp-divisibility-rules-integers (e)), so \( 2 \not\equiv 6 \pmod{8} \): the solutions form two classes modulo \( 8 \), \( [2]_8 \) and \( [6]_8 \).

*The map.* The rule \( \Phi([x]_8) \coloneqq ([x]_2, [x]_4) \) is still well defined, since \( 2 \mid 8 \) and \( 4 \mid 8 \) (the first step of the proof of (b) used only these divisibilities). It is not injective: \( \Phi([0]_8) = ([0]_2, [0]_4) = \Phi([4]_8) \), since \( 4 \equiv 0 \) modulo \( 2 \) and modulo \( 4 \), while \( [4]_8 \ne [0]_8 \). It is not surjective either: by the existence part, no \( x \) has \( \Phi([x]_8) = ([0]_2, [1]_4) \).
:::

::: {.remark}
For a map from a finite set to itself, injectivity alone gives surjectivity, by counting. Take \( g \colon \nZ/5\nZ \to \nZ/5\nZ \), \( g([x]) \coloneqq [2][x] \). It is injective: if \( [2][x] = [2][y] \), multiplying by \( [3] \), with \( [3][2] = [6] = [1] \), gives \( [x] = [y] \) ((F5)–(F7)). Let \( T \coloneqq g(\nZ/5\nZ) \). With codomain \( T \), \( g \) is a bijection \( \nZ/5\nZ \to T \), and \( \nZ/5\nZ \) is finite (@thm-integers-mod-n-ring (b)); so \( T \) is not a proper subset of \( \nZ/5\nZ \) (@fd2:thm-finite-no-proper-copy), that is, \( T = \nZ/5\nZ \), and \( g \) is surjective. Could injectivity of \( \Phi \) alone have given its surjectivity in the same way? Its source and target are different sets, so their sizes must be compared first; Exercise B3 asks for this. The formula of (a) is kept because it does more: it **computes** the solution.
:::

::: {.warning}
The coprimality hypothesis is used twice in @thm-chinese-remainder-two: for the identity \( mu + nv = 1 \), which builds \( x \), and in @prp-coprime-divisors-product, which makes the solution unique modulo \( mn \). Part (ii) of @exm-chinese-remainder-instances shows each use failing on its own: the moduli \( 2, 4 \) with right-hand sides \( 0, 1 \) have no solution, and with \( 0, 2 \) they have solutions spread over two classes modulo \( 8 \).
:::

In this section the identity \( 1 = ax + by \) of Section 3.2 gave inverses (@thm-units-mod-n) and the solutions of two congruences (@thm-chinese-remainder-two), inside the rings that Section 3.4's quotient construction built.

## Exercises

### A. Check your understanding

::: {#exr-units-and-crt-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Find \( [5]^{-1} \) in \( \nZ/12\nZ \).
2. List the units of \( \nZ/12\nZ \).
3. True or false: \( \nZ/1\nZ \) is a field. Justify your answer.
4. Find every \( x \in \nZ \) with \( x \equiv 1 \pmod{4} \) and \( x \equiv 2 \pmod{9} \).
5. In the proof of @thm-integers-mod-prime-field, where is it used that a unit is not a zero divisor?
:::
:::

::: {.solution}
(a) \( [5]^{-1} = [5] \), since \( 5 \cdot 5 = 25 = 2 \cdot 12 + 1 \).

(b) By @thm-units-mod-n, \( [a] \) is a unit exactly when \( \gcd(a, 12) = 1 \), and by @thm-integers-mod-n-ring (b) each class is \( [a] \) for exactly one \( a \in \{0, \dots, 11\} \). Among these, \( 0, 2, 4, 6, 8, 10 \) share the divisor \( 2 \) with \( 12 \), and \( 3, 9 \) share \( 3 \). The rest are coprime to \( 12 \): \( 1 \cdot 1 = 1 \), \( 5 \cdot 5 = 25 \), \( 7 \cdot 7 = 49 \) and \( 11 \cdot 11 = 121 \) are each \( 1 \) more than a multiple of \( 12 \), so each class is its own inverse. The units are \( [1], [5], [7], [11] \).

(c) **False.** In \( \nZ/1\nZ \) every \( a \) has \( 1 \mid a - 0 \), so \( [1] = [0] \) (@thm-integers-mod-n-ring (c)), and a field requires \( 1 \ne 0 \) (@def-commutative-ring-and-field). It is the zero ring. (Every element of it is a unit, as in the zero ring of the examples after @def-ring-unit; that is not enough.)

(d) \( \gcd(4, 9) = 1 \), from \( 4 \cdot (-2) + 9 \cdot 1 = 1 \) (@cor-coprime-iff-combination), so @thm-chinese-remainder-two applies with \( m = 4 \), \( n = 9 \), \( u = -2 \), \( v = 1 \):
\[
x = 1 \cdot 9 \cdot 1 + 2 \cdot 4 \cdot (-2) = 9 - 16 = -7 .
\]
The solutions are the \( x' \equiv -7 \pmod{36} \), that is, the class \( 29 + 36\nZ \), since \( -7 + 36 = 29 \). Check: \( 29 = 7 \cdot 4 + 1 = 3 \cdot 9 + 2 \).

(e) In the direction \( (\Rightarrow) \), at the end: \( [r][s] = [0] \) with \( [s] \ne [0] \), so \( [r] \), a non-zero class, cannot be a unit. That is how the proof shows (F8) fails.
:::

### B. Practice

::: {#exr-units-and-crt-b1}
[B1]

Let \( p \) be prime and \( a \in \nZ \). Prove that if \( [a]^2 = [1] \) in \( \nZ/p\nZ \), then \( [a] = [1] \) or \( [a] = [-1] \). Show by an example that this fails in \( \nZ/8\nZ \).
:::

::: {.solution}
\( [a]^2 = [a][a] = [a^2] \), so \( [a^2] = [1] \), and \( p \mid a^2 - 1 \) by the class test. Expanding (@prp-ring-algebra), \( a^2 - 1 = (a - 1)(a + 1) \). By @cor-prime-divides-product (b), \( p \mid a - 1 \) or \( p \mid a + 1 \). In the first case \( [a] = [1] \); in the second, \( a + 1 = a - (-1) \), so \( [a] = [-1] \), again by the class test.

In \( \nZ/8\nZ \), \( [3]^2 = [9] = [1] \), since \( 9 - 1 = 8 \). But \( [3] \ne [1] \), since \( 8 \nmid 2 \), and \( [3] \ne [-1] \), since \( 3 - (-1) = 4 \) and \( 8 \nmid 4 \) (@prp-divisibility-rules-integers (e)). The proof breaks at @cor-prime-divides-product (b): \( 8 \mid 2 \cdot 4 = (3 - 1)(3 + 1) \), yet \( 8 \) divides neither factor. (So do \( [5] \) and \( [7] \): all four units of \( \nZ/8\nZ \) square to \( [1] \).)
:::

::: {#exr-units-and-crt-b2}
[B2]

::: {.enumerate options="label=(\alph*)"}
1. Let \( m, n \in \nZ_{>0} \) and \( x \in \nZ \). Show that \( [x]_{mn} \) is a unit of \( \nZ/mn\nZ \) if and only if \( [x]_m \) and \( [x]_n \) are units of \( \nZ/m\nZ \) and \( \nZ/n\nZ \).
2. Now let \( m \) and \( n \) be coprime. Deduce that the map \( \Phi \) of @thm-chinese-remainder-two (b) maps \( (\nZ/mn\nZ)^{\times} \) bijectively onto \( (\nZ/m\nZ)^{\times} \times (\nZ/n\nZ)^{\times} \).
3. Which of (a) and (b) uses coprimality? Illustrate with \( m = n = 2 \).
:::
:::

::: {.solution}
(a) \( (\Rightarrow) \) Let \( [x]_{mn}[s]_{mn} = [1]_{mn} \), with \( s \in \nZ \). Then \( mn \mid xs - 1 \) by the class test, and \( m \mid mn \), so \( m \mid xs - 1 \) (@prp-divisibility-rules-integers (b)); thus \( [x]_m [s]_m = [1]_m \). Likewise \( [x]_n [s]_n = [1]_n \). So both are units.

\( (\Leftarrow) \) Let \( [x]_m [s]_m = [1]_m \) and \( [x]_n [s']_n = [1]_n \). By the class test, \( xs - 1 = -mt \) and \( xs' - 1 = -nt' \) for some \( t, t' \in \nZ \), so \( xs + mt = 1 \) and \( xs' + nt' = 1 \). Multiplying the two equations and expanding,
\[
x(xss' + snt' + s'mt) + mn \cdot tt' = 1 .
\]
So \( \gcd(x, mn) = 1 \) (@cor-coprime-iff-combination), and \( [x]_{mn} \) is a unit (@thm-units-mod-n).

(b) By (a), \( \Phi([x]_{mn}) = ([x]_m, [x]_n) \) lies in \( (\nZ/m\nZ)^{\times} \times (\nZ/n\nZ)^{\times} \) exactly when \( [x]_{mn} \) is a unit. So \( \Phi \) maps \( (\nZ/mn\nZ)^{\times} \) into that set, and the restriction is injective, since \( \Phi \) is. Each element of that set is \( \Phi(c) \) for some \( c \in \nZ/mn\nZ \), since \( \Phi \) is surjective, and that \( c \) is a unit by (a). So the restriction is a bijection.

(c) Only (b), through @thm-chinese-remainder-two; (a) holds for all \( m, n \). For \( m = n = 2 \), (a) says that \( [x]_4 \) is a unit exactly when \( [x]_2 \) is, and both hold exactly for odd \( x \): the units of \( \nZ/4\nZ \) are \( [1], [3] \) and that of \( \nZ/2\nZ \) is \( [1] \). Yet \( \Phi([x]_4) \coloneqq ([x]_2, [x]_2) \) sends both units \( [1]_4 \) and \( [3]_4 \) to \( ([1]_2, [1]_2) \), so it is not injective on the units, and it is not a bijection \( \nZ/4\nZ \to \nZ/2\nZ \times \nZ/2\nZ \) either (compare @exm-chinese-remainder-instances (ii)).
:::

::: {#exr-units-and-crt-b3}
[B3]

Let \( m, n \in \nZ_{>0} \) be coprime. Show by counting that injectivity of the map \( \Phi \) of @thm-chinese-remainder-two (b) already forces its surjectivity, without using the formula of part (a).
:::

::: {.solution}
By @thm-integers-mod-n-ring (b), applied to the modulus \( mn \), the set \( \nZ/mn\nZ \) has \( mn \) elements: there is a bijection \( \varphi \colon \{1, \dots, mn\} \to \nZ/mn\nZ \). Let \( T \coloneqq \Phi(\nZ/mn\nZ) \) be the image of \( \Phi \). Since \( \Phi \) is injective, \( \Phi \) with codomain \( T \) is a bijection, and so is its composite with \( \varphi \) (@fd2:prp-equinumerous-properties (c)): \( T \) has \( mn \) elements.

The target \( \nZ/m\nZ \times \nZ/n\nZ \) also has \( mn \) elements, by @thm-integers-mod-n-ring (b) for \( m \) and for \( n \), and the count of a product, part (a) of @fd2:exr-finite-sets-c2. Suppose \( T \) were a proper subset of the target. Then @fd2:prp-subset-finite gives it \( k \) elements for some \( k < mn \), and @fd2:cor-finite-size-unique gives \( k = mn \): a contradiction. So \( T \) is the whole target, and \( \Phi \) is surjective. (Equivalently: composing the two bijections from \( \{1, \dots, mn\} \) gives a bijection from the target onto \( T \), which @fd2:thm-finite-no-proper-copy forbids when \( T \) is a proper subset.)
:::

### C. Going deeper

::: {#exr-units-and-crt-c1}
[C1: Exit check: units and the field \( \nZ/p\nZ \)]

Let \( n \in \nZ_{>0} \) and \( a \in \nZ \). Prove that \( [a] \in \nZ/n\nZ \) is a unit if and only if \( \gcd(a, n) = 1 \). Deduce that \( \nZ/p\nZ \) is a field for every prime \( p \).
:::

::: {.solution}
*Units, \( (\Leftarrow) \).* If \( \gcd(a, n) = 1 \), then \( ax + ny = 1 \) for some \( x, y \in \nZ \) (@cor-coprime-iff-combination). The product on \( \nZ/n\nZ \) is well defined and computed on representatives (@thm-quotient-ring-by-ideal (b)), so \( [a][x] = [ax] \). Since \( ax - 1 = (-y)n \), \( n \mid ax - 1 \), and \( [ax] = [1] \) by the class test. So \( [a] \) is a unit with inverse \( [x] \).

*Units, \( (\Rightarrow) \).* If \( [a][x] = [1] \) for some \( x \in \nZ \), then \( [ax] = [1] \), so \( ax - 1 = yn \) with \( y \in \nZ \), and \( ax + n(-y) = 1 \). By @cor-coprime-iff-combination, \( \gcd(a, n) = 1 \).

*The field.* Let \( p \) be prime. \( \nZ/p\nZ \) is a commutative ring (@thm-integers-mod-n-ring (a)), and \( [1] \ne [0] \), since \( [1] = [0] \) would give \( p \mid 1 \), so \( p \le 1 \) by @prp-divisibility-rules-integers (e), while \( p \ge 2 \). Let \( [a] \ne [0] \). Then \( p \nmid a \). The integer \( g \coloneqq \gcd(p, a) \ge 1 \) divides \( p \), so \( g \in \{1, p\} \) by @fd2:def-prime; and \( g = p \) would give \( p \mid a \). So \( g = 1 \), and \( [a] \) is a unit by the first part. Every non-zero class is a unit, which is (F8), so \( \nZ/p\nZ \) is a field.

**Marking scheme.** (10 points)
- 3: \( (\Leftarrow) \) of units: a Bézout identity \( ax + ny = 1 \) and the class computation \( [a][x] = [ax] = [1] \), naming that the product is well defined (computed on representatives).
- 3: \( (\Rightarrow) \) of units: from \( [a][x] = [1] \) to an integer combination of \( a \) and \( n \) equal to \( 1 \), then \( \gcd(a, n) = 1 \) with a cited reason.
- 2: \( [a] \ne [0] \) gives \( p \nmid a \), and \( \gcd(a, p) = 1 \) because the gcd divides \( p \) and is not \( p \).
- 1: \( [1] \ne [0] \) for \( p \ge 2 \).
- 1: concludes with (F8): every non-zero class is a unit.
Fatal errors (0 for the step): canceling \( [a] \) in \( \nZ/p\nZ \) without justification (circular, since cancellation is what inverses give); "\( \gcd(a, p) = 1 \) because \( p \) is prime" with no treatment of the case \( p \mid a \). A proof of the field part that cites @cor-prime-divides-product (a) instead of the divisor argument earns the same 2 points.
:::

::: {#exr-units-and-crt-c2}
[C2: Find the error]

Here is an argument.

> **Claim.** For every prime \( p \), \( \nZ/p\nZ \) is a field.
>
> **Proof.** (0) By @thm-integers-mod-n-ring (a) and (c), \( \nZ/p\nZ \) is a commutative ring with \( [1] \ne [0] \), since \( p \ge 2 \). (1) Let \( [a] \ne [0] \) in \( \nZ/p\nZ \). (2) If \( [a][x] = [a][y] \), then canceling \( [a] \) gives \( [x] = [y] \). (3) So the map \( f \colon \nZ/p\nZ \to \nZ/p\nZ \), \( f([x]) \coloneqq [a][x] \), is injective. (4) With codomain its image, \( f \) is a bijection from \( \nZ/p\nZ \) onto \( f(\nZ/p\nZ) \), a subset of the finite set \( \nZ/p\nZ \) (@thm-integers-mod-n-ring (b)). By @fd2:thm-finite-no-proper-copy the image is not a proper subset, so \( f \) is surjective. (5) So some \( [x] \) has \( [a][x] = [1] \), and \( [a] \) is a unit. So (F8) holds, and \( \nZ/p\nZ \) is a field.

Is the claim true? Does the argument prove it? Name the line that fails and the reason, give a counterexample to the illegal step, and repair the argument.
:::

::: {.solution}
[Hint 1]

List the properties of \( \nZ/p\nZ \) that each line uses. Which of them have been proved in this chapter, and which are things a field has?
:::

::: {.solution}
[Hint 2]

Write \( [a][x] = [a][y] \) as a divisibility statement about integers.
:::

::: {.solution}
**The claim is true:** it is @thm-integers-mod-prime-field. **The argument does not prove it as written.**

*Line (2) fails.* "Cancel a non-zero factor" is a rule of fields (multiply by the inverse) or of rings without zero divisors, and neither has been established for \( \nZ/p\nZ \): it is close to what the argument is trying to prove, and it is false in general. So the line cites a "fact" that is neither proved nor true, entry (N9) of @fd1:exm-not-allowed-catalogue. Counterexample to the step: in \( \nZ/6\nZ \), \( [2][1] = [2] \) and \( [2][4] = [8] = [2] \), so \( [2][1] = [2][4] \) with \( [2] \ne [0] \), yet \( [1] \ne [4] \). There is no counterexample to the conclusion.

*Repair of line (2).* If \( [a][x] = [a][y] \), then \( [a(x - y)] = [0] \), so \( p \mid a(x - y) \) by the class test. Since \( [a] \ne [0] \), \( p \nmid a \), so \( p \mid x - y \) by @cor-prime-divides-product (b), and \( [x] = [y] \). This uses that \( p \) is prime, the hypothesis the flawed line never touched. With this repair, the argument is a correct second proof.

**Marking scheme.** (10 points)
- 2: says the claim is true and the argument, as written, does not prove it.
- 3: names line (2) and the reason: cancellation by a non-zero class is unproved here and false in general, (N9), or an equivalent statement of the reason.
- 2: a counterexample to the step, such as \( [2][1] = [2][4] \) in \( \nZ/6\nZ \).
- 3: repairs line (2) without assuming the field property: \( p \mid a(x - y) \) by the class test and Euclid's lemma for a prime (@cor-prime-divides-product (b), from @thm-euclid-lemma-integers); or \( \gcd(a, p) = 1 \) (@cor-prime-divides-product (a)) and an inverse of \( [a] \) from @thm-units-mod-n, which earns full points even though it makes lines (3)–(5) redundant.
Fatal errors (0 for the step): a counterexample to the conclusion (there is none); a repair that cancels \( [a] \) by appeal to the field property being proved (citing @thm-units-mod-n is not such an appeal).
:::

::: {#exr-units-and-crt-c3}
[C3]

Find every \( x \in \nZ \) with
\[
x \equiv 1 \pmod{3} , \qquad x \equiv 2 \pmod{5} , \qquad x \equiv 3 \pmod{7} ,
\]
by applying @thm-chinese-remainder-two twice.
:::

::: {.solution}
*The first two congruences.* \( 1 = 2 \cdot 3 + (-1) \cdot 5 \), so \( \gcd(3, 5) = 1 \) (@cor-coprime-iff-combination), with \( m = 3 \), \( n = 5 \), \( u = 2 \), \( v = -1 \). By @thm-chinese-remainder-two (a),
\[
x_1 = 1 \cdot 5 \cdot (-1) + 2 \cdot 3 \cdot 2 = -5 + 12 = 7 ,
\]
and an integer satisfies the first two congruences **if and only if** it is \( \equiv 7 \pmod{15} \).

*Adding the third.* So the three congruences together say exactly \( x \equiv 7 \pmod{15} \) and \( x \equiv 3 \pmod{7} \). Now \( 1 = 1 \cdot 15 + (-2) \cdot 7 \), so \( \gcd(15, 7) = 1 \), with \( m = 15 \), \( n = 7 \), \( u = 1 \), \( v = -2 \). By @thm-chinese-remainder-two (a) again,
\[
x_2 = 7 \cdot 7 \cdot (-2) + 3 \cdot 15 \cdot 1 = -98 + 45 = -53 ,
\]
and the solutions are the \( x \equiv -53 \pmod{105} \), that is, the class \( 52 + 105\nZ \).

Check: \( 52 = 17 \cdot 3 + 1 = 10 \cdot 5 + 2 = 7 \cdot 7 + 3 \). (Coprimality of \( 3 \) and \( 5 \), and of \( 15 \) and \( 7 \), also follows from the small-primes remark of Section 3.1 with @cor-prime-divides-product (a).) The "if and only if" in the first step is what allows replacing two congruences by one; with "if" alone, the second step could lose solutions.
:::

### R. Review

::: {#exr-units-and-crt-r1}
[R1]

Let \( \nZ = (\nN \times \nN)/{\sim} \) be the integers built as classes of pairs, with \( (a, b) \sim (c, d) \iff a + d = b + c \). Show that \( [(a, b)] \mapsto [a + b]_2 \) is a well-defined function \( \nZ \to \nZ/2\nZ \), and identify it.
:::

::: {.solution}
This is the method of @thm-well-defined-on-classes (a), from the construction @def-integers-as-classes. Take \( X = \nN \times \nN \) with \( \sim \), \( Y = \nZ \) with congruence modulo \( 2 \), the equivalence relation \( \sim_{2\nZ} \) whose quotient set is \( \nZ/2\nZ \) (@def-integers-mod-n-ring, @thm-quotient-ring-by-ideal (a)), and \( f(a, b) \coloneqq a + b \). Let \( (a, b) \sim (a', b') \), so \( a + b' = a' + b \). Then, in \( \nZ \),
\[
\begin{aligned}
(a + b) - (a' + b') &= (a + b' - a' - b) + 2b - 2b' \\
&= 0 + 2(b - b') ,
\end{aligned}
\]
so \( a + b \equiv a' + b' \pmod{2} \). By @thm-well-defined-on-classes (a) there is exactly one function \( F \colon \nZ \to \nZ/2\nZ \) with \( F([(a, b)]) = [a + b]_2 \).

*Identification.* By the remark after @thm-integers-commutative-ring, \( [(a, b)] = a - b \) in \( \nZ \). Since \( (a + b) - (a - b) = 2b \), \( [a + b]_2 = [a - b]_2 \) by the class test. So \( F(z) = [z]_2 \) for every \( z \in \nZ \): \( F \) is the quotient map of \( \nZ/2\nZ \), which sends an integer to its parity class.
:::

::: {#exr-units-and-crt-r2}
[R2]

Let \( m, n, m', n' \in \nN \) with \( 2^m 3^n = 2^{m'} 3^{n'} \). Prove that \( m = m' \) and \( n = n' \). Conclude that \( (m, n) \mapsto 2^m 3^n \) is injective on \( \nN \times \nN \).
:::

::: {.solution}
The tool is unique factorization, @thm-fundamental-arithmetic. The powers are those of \( \nN = \omega \) (@prp-omega-powers-parity), carried into \( \nZ \), which preserves products (@prp-naturals-embed-integers); \( b^0 = 1 \) and \( b^{j+1} = b^j \cdot b \).

*A factorization.* For \( m, n \in \nN \), let \( L_{m,n} \) be the list of length \( m + n \) whose first \( m \) entries are \( 2 \) and whose last \( n \) entries are \( 3 \). Its entries are prime, by the small-primes remark of Section 3.1, and it is non-decreasing, since \( 2 \le 3 \). Its product is \( 2^m 3^n \). Indeed, with \( P_j \) the product of the first \( j \) entries, the recursion of @def-prime-factorization and induction on \( j \le m \) give \( P_j = 2^j \) (\( P_0 = 1 = 2^0 \); \( P_{j+1} = P_j \cdot 2 = 2^{j+1} \)), and then induction on \( i \le n \) gives \( P_{m+i} = 2^m 3^i \). So \( L_{m,n} \) is a prime factorization of \( 2^m 3^n \), which is positive, being a product of positive integers (@prp-ordered-ring-rules (c)).

*Uniqueness.* If \( 2^m 3^n = 2^{m'} 3^{n'} \), then \( L_{m,n} \) and \( L_{m',n'} \) are prime factorizations of the same positive integer, so they are equal (@thm-fundamental-arithmetic): \( m + n = m' + n' \), with equal entries. Suppose \( m < m' \). Then the entry of index \( m' \) is \( 2 \) in \( L_{m',n'} \), and in \( L_{m,n} \) it is \( 3 \), since \( m < m' \le m + n \): a contradiction. Exchanging the two lists rules out \( m' < m \). So \( m = m' \), and then \( n = n' \) by canceling \( m \) in \( m + n = m' + n' \).

This is line (vii) of @fd2:exr-countable-sets-b2, which was not available when that exercise was set; @fd2:thm-product-countable proves the same injectivity by parity instead.
:::

::: {#exr-units-and-crt-r3}
[R3]

Prove that no \( x \in \nQ \) satisfies \( x^2 = 2 \), by the parity argument: write \( x \) as a fraction and show that numerator and denominator are both even. Then show that, for every prime \( p \), no \( x \in \nQ \) satisfies \( x^2 = p \).
:::

::: {.solution}
This is the school argument of @fd1:thm-sqrt2-irrational, now with every step citable.

*The case \( 2 \).* Suppose \( x \in \nQ \) and \( x^2 = 2 \). By @prp-rationals-lowest-terms, \( x = a/b \) with \( a \in \nZ \), \( b \in \nZ_{>0} \) and \( \gcd(a, b) = 1 \). By @def-rational-operations, \( x^2 = a^2/b^2 \), and \( 2 = 2/1 \), so \( a^2 = 2b^2 \) (@prp-integers-embed-rationals (b)). Then \( a^2 \) is even, so \( a \) is even by @cor-integers-even-odd (b): \( a = 2c \) with \( c \in \nZ \). Then \( 4c^2 = 2b^2 \), and canceling the non-zero factor \( 2 \) (@prp-ordered-ring-rules (f), applied to \( 2(b^2 - 2c^2) = 0 \)) gives \( b^2 = 2c^2 \). So \( b \) is even as well. Now \( 2 \) divides \( a \) and \( b \), hence divides \( \gcd(a, b) = 1 \) (@thm-integers-bezout (c), (d)), so \( 2 \in \{1, -1\} \) (@prp-divisibility-rules-integers (g)): a contradiction.

*A prime \( p \).* The same argument works with "\( p \mid \)" in place of "even": from \( a^2 = p b^2 \), \( p \mid a \cdot a \), so \( p \mid a \) by @cor-prime-divides-product (b); \( a = pc \) gives \( p^2 c^2 = p b^2 \), so \( b^2 = p c^2 \) (cancel \( p \ne 0 \)), and \( p \mid b \) in the same way. Then \( p \mid \gcd(a, b) = 1 \), against \( p \ge 2 \).

*Comparison.* Chapter 2's proof, @thm-no-rational-square-two, needed neither parity nor gcd: it descended to a smaller denominator using order alone. The argument here is shorter, but it stands on lowest terms, and lowest terms stands on Bézout (@prp-rationals-lowest-terms uses @cor-coprime-iff-combination).
:::

::: {#exr-units-and-crt-r4}
[R4]

Find all \( x \in \nZ \) with \( 6x \equiv 4 \pmod{10} \).
:::

::: {.solution}
**Answer:** the class \( 4 + 5\nZ \).

*The tool* is to divide the congruence by \( \gcd(6, 10) = 2 \), and then invert a unit (@thm-units-mod-n). Since \( 6x - 4 = 2(3x - 2) \) and \( 10 = 2 \cdot 5 \),
\[
10 \mid 6x - 4 \iff 5 \mid 3x - 2 :
\]
if \( 2(3x - 2) = 10k = 2(5k) \), cancel \( 2 \ne 0 \) (@prp-ordered-ring-rules (f)); conversely, multiply \( 3x - 2 = 5k \) by \( 2 \). So the condition is \( [3][x] = [2] \) in \( \nZ/5\nZ \). There \( [3]^{-1} = [2] \), since \( 3 \cdot 2 = 6 = 5 + 1 \). Multiplying by \( [2] \), \( [x] = [2][2] = [4] \); and conversely \( [3][4] = [12] = [2] \). So the solutions are exactly the \( x \equiv 4 \pmod{5} \). Check: \( 6 \cdot 4 - 4 = 20 \) and \( 6 \cdot 9 - 4 = 50 \) are multiples of \( 10 \).

*Why the look-alikes fail.* "Multiply by \( [6]^{-1} \) in \( \nZ/10\nZ \)" fails: \( \gcd(6, 10) = 2 \), so \( [6] \) is not a unit there (@thm-units-mod-n). Canceling the \( 2 \) from every term but keeping the modulus gives \( 3x \equiv 2 \pmod{10} \), and that is wrong: it keeps \( 4 \) and loses \( 9 \) (\( 6 \cdot 9 - 4 = 50 \), while \( 3 \cdot 9 - 2 = 25 \)). The modulus must be divided too. The Chinese remainder theorem is not a look-alike that fails: splitting \( 10 = 2 \cdot 5 \), @thm-chinese-remainder-two (b) turns the condition \( [6]_{10}[x]_{10} = [4]_{10} \) into \( [0]_2 [x]_2 = [0]_2 \), which always holds, and \( [x]_5 = [4]_5 \), since \( [6]_5 = [1]_5 \); so it is a second route to the same answer. Note also that the answer is a class modulo \( 5 \), not modulo \( 10 \): it is the two classes \( [4]_{10} \) and \( [9]_{10} \).
:::

<!-- dependency ledger
thm-units-mod-n (proof): the class test (opening paragraph) [u] = [v] iff n | u - v | thm-quotient-ring-by-ideal (a) with fd2:thm-classes-partition (b), def-integer-linear-combinations, fd2:def-divides, cited
def-ring-unit (claim): uniqueness of the inverse, closure under products and inverses, a unit is not a zero divisor | (F5)-(F7) of def-commutative-ring-and-field, prp-ring-algebra (b); inline
def-ring-unit (example): Z^x = {1, -1}; Q^x = Q \ {0}; units of Z/6Z; the products [2][x] | prp-divisibility-rules-integers (g), prp-ring-algebra (b), (c), thm-rationals-field, exm-integers-mod-six, cited; verify/ch03/def-ring-unit.py
def-ring-unit (claim): (paragraph after the warning) units form a group | Algebraic Preliminaries, Chapter 2 (F5.3, prose pointer; nothing here depends on it)
thm-units-mod-n (proof): every element of Z/nZ is a class [x] | fd2:def-quotient-set, cited
thm-units-mod-n (claim): (quick check after exm-unit-inverse-mod-n) [3]^{-1} = [5] in Z/7Z | inline arithmetic; verify/ch03/thm-units-mod-n.py
exm-unit-inverse-mod-n (example): Euclidean run on (60, 17), back-substitution, 17 * 53 = 901 = 15 * 60 + 1; gcd(12, 60) = 12; [12][5] = [0] | inline arithmetic; verify/ch03/exm-unit-inverse-mod-n.py
thm-integers-mod-prime-field (proof): s > 0 from rs = n > 0; s != n by cancellation | prp-ring-algebra (b), prp-ordered-ring-rules (c), (f), cited; inline; verify/ch03/thm-integers-mod-prime-field.py (n <= 200)
thm-integers-mod-prime-field (claim): (aftermath) Z/2Z has the tables of exm-finite-ring-not-orderable; Algebraic Preliminaries, Chapter 1 names these fields | inline comparison of tables; F5.2 prose pointer, nothing here depends on it
thm-integers-mod-prime-field (claim): (remark) 5 is prime; 5 * [1] = [0]; Z/5Z cannot be ordered | the small-primes remark of Section 3.1; thm-integers-mod-n-ring (d), (e), cited
thm-chinese-remainder-two (proof): the identities x - a = m(bu - au), x - b = n(av - bv) | prp-ring-algebra; inline; verify/ch03/thm-chinese-remainder-two.py
thm-chinese-remainder-two (proof): componentwise operations on Z/mZ x Z/nZ | defined in the statement; fd2:def-cartesian-product
thm-chinese-remainder-two (claim): (aftermath) the componentwise product of two commutative rings is a commutative ring | each axiom is an equation, checked in each coordinate; inline, not used in any proof
thm-chinese-remainder-two (idea): try-it-first numbers e = -5, f = 6, 2e + 3f = 8 | verify/ch03/thm-chinese-remainder-two.py
exm-chinese-remainder-instances (example): x = 8, 8 + 15Z; 2 + 4Z, 6 - 2 = 4, Phi([0]) = Phi([4]) | inline arithmetic; verify/ch03/exm-chinese-remainder-instances.py
exm-chinese-remainder-instances (example): well-definedness of Phi for non-coprime 2, 4 | first step of the proof of thm-chinese-remainder-two (b), which uses only m | mn and n | mn; inline
exm-chinese-remainder-instances (claim): (remark after it) [x] -> [2][x] on Z/5Z is injective via [3][2] = [1], hence surjective by counting | (F5)-(F7); thm-integers-mod-n-ring (b); fd2:thm-finite-no-proper-copy, group (i) of F3.1's citing rule (cor-omega-identification), cited; verify/ch03/exm-chinese-remainder-instances.py
exr-units-and-crt-a1 (solution): [5]^2 = [1] mod 12; units of Z/12Z; x = -7, 29 + 36Z | verify/ch03/exr-units-and-crt-a1.py
exr-units-and-crt-b1 (solution): a^2 - 1 = (a - 1)(a + 1); [3]^2 = [1] in Z/8Z, units of Z/8Z square to [1] | prp-ring-algebra; verify/ch03/exr-units-and-crt-b1.py
exr-units-and-crt-b2 (solution): the product identity (xs + mt)(xs' + nt') | prp-ring-algebra; verify/ch03/exr-units-and-crt-b2.py
exr-units-and-crt-b3 (solution): count of a product of finite sets | fd2:exr-finite-sets-c2 (a), an exercise cited from an exercise solution, which STYLE allows; group (i) of F3.1's citing rule (cor-omega-identification)
exr-units-and-crt-b3 (solution): fd2 finite-set results read on omega | group (i) of F3.1's citing rule after cor-omega-identification, cited by label
exr-units-and-crt-c2 (solution): [2][1] = [2][4] in Z/6Z | verify/ch03/exr-units-and-crt-c2.py
exr-units-and-crt-c2 (solution): (statement) the quoted proof's lines (0) and (4) | thm-integers-mod-n-ring (a), (b), (c); fd2:thm-finite-no-proper-copy, group (i) of F3.1's citing rule (cor-omega-identification), cited
exr-units-and-crt-c3 (solution): x_1 = 7, x_2 = -53, 52 + 105Z | verify/ch03/exr-units-and-crt-c3.py
exr-units-and-crt-r1 (solution): (a + b) - (a' + b') = 2(b - b'); [(a, b)] = a - b | prp-ring-algebra; remark after thm-integers-commutative-ring (prp-naturals-embed-integers), cited; def-integers-mod-n-ring, thm-quotient-ring-by-ideal (a) (congruence mod 2 is the equivalence relation of Z/2Z), cited; verify/ch03/exr-units-and-crt-r1.py
exr-units-and-crt-r2 (solution): powers b^n on omega carried into Z; product of the list L_{m,n} by induction | prp-omega-powers-parity, prp-naturals-embed-integers, def-prime-factorization (its recursion), fd1:ax-induction read on omega (cor-omega-identification (b)); inline
exr-units-and-crt-r2 (solution): 2^m 3^n > 0 | prp-ordered-ring-rules (c), induction; inline
exr-units-and-crt-r2 (solution): fd2:thm-product-countable mentioned for comparison | group (ii) of F3.1's citing rule; R item, prose comparison only
exr-units-and-crt-r3 (solution): (a/b)^2 = a^2/b^2 | def-rational-operations, cited
exr-units-and-crt-r4 (solution): 6x - 4 = 2(3x - 2); [3][2] = [1] mod 5; 20, 50; look-alike 3x = 2 mod 10 loses 9 (25); CRT route via 10 = 2 * 5, [6]_5 = [1]_5 | thm-chinese-remainder-two (b), cited; verify/ch03/exr-units-and-crt-r4.py
-->
