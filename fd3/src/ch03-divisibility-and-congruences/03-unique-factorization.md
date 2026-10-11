# Euclid's Lemma and the Fundamental Theorem of Arithmetic

Section 3.2 gave every pair of integers, not both zero, a greatest common divisor, and wrote it as a combination \( ax + by \) (@thm-integers-bezout). This section spends that identity. Take \( 60 \). It splits as \( 2 \cdot 30 \), as \( 6 \cdot 10 \), as \( 4 \cdot 15 \), and every way of splitting it further, until no factor splits again, ends with the same primes \( 2, 2, 3, 5 \). *Sets, Relations, and Cardinality*, Section 2.2 proved, for the school integers, that every integer at least \( 2 \) has a prime factor, and set the uniqueness of the full splitting aside. Here we prove both, for the integers of Chapter 2. The key is a property of primes that the definition ("no positive divisors except \( 1 \) and itself") does not obviously give: a prime that divides a product divides one of the factors.

As in Section 3.1, numerals are the natural numbers of those names, and their sums and products may be computed in \( \nN \) (@prp-naturals-embed-integers (a)).

## Euclid's lemma

The definition of a prime \( p \) speaks about the divisors **of** \( p \). The property we want speaks about the numbers that \( p \) **divides**. Something has to connect the two, and the connection is the Bézout identity of Section 3.2. We first prove a version for any divisor that shares no factor with one of the two numbers multiplied.

::: {#thm-euclid-lemma-integers}
[Euclid's Lemma]

Let \( a, b, c \in \nZ \). If \( a \mid bc \) and \( \gcd(a, b) = 1 \), then \( a \mid c \).
:::

::: {.idea}
The hypothesis \( \gcd(a, b) = 1 \) is a statement about common divisors, which is hard to use directly. By @cor-coprime-iff-combination it is the same as an equation \( 1 = ax + by \), and an equation can be multiplied. Multiplying it by \( c \) writes \( c \) as \( acx + bcy \). The first term is a multiple of \( a \) on sight, and the second is one because \( bc \) is.
:::

::: {.proof}
Suppose \( a \mid bc \) and \( \gcd(a, b) = 1 \). By @cor-coprime-iff-combination there are \( x, y \in \nZ \) with \( ax + by = 1 \). Since \( a \mid bc \), there is \( k \in \nZ \) with \( bc = ka \) (@fd2:def-divides). Multiplying the identity by \( c \), with (F7), (F9), (F5) and (F6),
\[
c = c(ax + by) = a(cx) + (bc)y = a(cx) + a(ky) = a(cx + ky) .
\]
Since \( cx + ky \in \nZ \), this shows \( a \mid c \).
:::

We call the move of this proof **multiply the Bézout identity**: from \( 1 = ax + by \), multiply by \( c \) and read off what divides \( c \). It turns a statement about divisors into an equation, which is where the work can be done.

Each hypothesis has a job. Without \( \gcd(a, b) = 1 \) the conclusion fails: \( 4 \mid 2 \cdot 6 = 12 \), but \( 4 \nmid 6 \), since \( 6 = 1 \cdot 4 + 2 \) leaves a non-zero remainder (uniqueness in @thm-integers-division-remainder (a)); here \( \gcd(4, 2) = 2 \). The common factor \( 2 \) of \( 4 \) and \( 2 \) let \( 4 \) divide the product without dividing \( 6 \).

## Lists, products and prime factorizations

To say that a factorization is unique, we must first say what a factorization is. The products \( 2 \cdot 2 \cdot 3 \cdot 5 \) and \( 3 \cdot 2 \cdot 5 \cdot 2 \) are equal and use the same primes, and we want to count them as one. We do so by writing the primes in order, smallest first. A factorization also has a length, and the length may be \( 0 \): the number \( 1 \) is the product of no primes at all.

Products of lists are defined by the recursion of @fd2:def-sum-product. That definition was made for sequences of real numbers, and we use it as a pattern, as group (iii) of the citing rule of Section 1.7 allows.

::: {#def-prime-factorization}
[List, Product of a List, Prime Factorization]

Let \( k \in \nN \). A **list** of length \( k \) in \( \nZ \) is a function \( p \colon \{1, \dots, k\} \to \nZ \), written \( (p_1, \dots, p_k) \) with \( p_i \coloneqq p(i) \); for \( k = 0 \) it is the **empty list**. Its **product** \( \prod_{i=1}^{k} p_i \in \nZ \) is given by the recursion
\[
\prod_{i=1}^{0} p_i = 1 , \qquad \prod_{i=1}^{j+1} p_i = \Bigl( \prod_{i=1}^{j} p_i \Bigr) p_{j+1} \quad \text{for } j < k ,
\]
where \( \prod_{i=1}^{j} p_i \) is the product of the shortened list \( (p_1, \dots, p_j) \).

A **prime factorization** of \( n \in \nZ_{>0} \) is a list \( (p_1, \dots, p_k) \) such that **every** entry \( p_i \) is prime (@fd2:def-prime), the list is **non-decreasing** (\( i \le j \) implies \( p_i \le p_j \)), and \( \prod_{i=1}^{k} p_i = n \).
:::

In words: a list is a finite sequence of integers, possibly empty; its product starts at \( 1 \) and multiplies by one more entry at each stage; and a prime factorization lists primes in non-decreasing order with the right product.

**Why the product exists.** Extend the list to a sequence \( \bar p \) on \( \nZ_{>0} \) by \( \bar p_i \coloneqq p_i \) for \( i \le k \) and \( \bar p_i \coloneqq 1 \) for \( i > k \). Then @fd2:thm-recursion, read on \( \nN = \omega \) through @cor-omega-identification (b), with \( X = \nZ \), starting value \( 1 \) and step \( g(j, x) \coloneqq x \bar p_{j+1} \), gives exactly one function \( P \colon \nN \to \nZ \) with \( P_0 = 1 \) and \( P_{j+1} = P_j \bar p_{j+1} \); we set \( \prod_{i=1}^{j} p_i \coloneqq P_j \) for \( j \le k \). The "Finite lists" remark after @fd2:def-sum-product shows that \( P_j \) depends only on \( p_1, \dots, p_j \), not on how the list was extended. Its proof is an induction on \( j \) that uses only the recursion and the multiplication of the target set, so it runs unchanged with \( \nZ \) in place of \( \nR \). In particular \( P_j \) is also the product of the shortened list \( (p_1, \dots, p_j) \), which is the displayed recursion. We cite it as **the recursion of @def-prime-factorization**: it peels the **last** entry off a product.

**Examples.**

- \( (2, 2, 3, 5) \) is a prime factorization of \( 60 \). Its entries are prime by the small-primes remark of Section 3.1; it is non-decreasing; and the recursion gives the products \( 1, 2, 4, 12, 60 \).
- \( (5) \) is a prime factorization of \( 5 \), with products \( 1, 5 \). A prime \( p \) has the one-entry factorization \( (p) \).
- The degenerate case: the empty list is a prime factorization of \( 1 \). Its product is \( 1 \) by the first clause of the recursion, and the conditions "every entry is prime" and "non-decreasing" hold vacuously. Without this case the number \( 1 \) would have no factorization, and the uniqueness proof below would have no base case.

**Non-examples by minimal change.** Exchange two entries of the first example: \( (2, 3, 2, 5) \) has prime entries and product \( 60 \), but it is not non-decreasing, since positions \( 2 \le 3 \) carry \( 3 > 2 \). Merge two entries: \( (2, 2, 15) \) is non-decreasing with product \( 60 \), but \( 15 = 3 \cdot 5 \) is not prime.

**Why these clauses.** Without "non-decreasing", \( 60 \) would have twelve factorizations, its four primes in every order, and uniqueness could only be stated up to rearrangement, which needs a theory of permutations. Without "prime", splitting would stop anywhere. And the requirement \( p \ge 2 \) in @fd2:def-prime is what keeps \( (1, 2, 2, 3, 5) \) out: if \( 1 \) counted as a prime, every factorization could be padded with as many \( 1 \)s as we like.

::: {.check}
Find the prime factorization of \( 360 \), and check each clause of @def-prime-factorization.
:::

::: {.solution}
\( (2, 2, 2, 3, 3, 5) \). Its entries are prime by the small-primes remark of Section 3.1. It is non-decreasing. Its products, by the recursion, are \( 1, 2, 4, 8, 24, 72, 360 \). By the theorem below there is no other.
:::

## Primes dividing products

For a prime, the coprimality that Euclid's lemma asks for comes almost free: a prime shares no factor with a number unless it divides that number.

::: {#cor-prime-divides-product}
[A Prime Dividing a Product]

Let \( p \) be prime.

::: {.enumerate options="label=(\alph*)"}
1. For every \( a \in \nZ \): \( p \mid a \) or \( \gcd(p, a) = 1 \).
2. For all \( b, c \in \nZ \): if \( p \mid bc \), then \( p \mid b \) or \( p \mid c \).
3. If \( (q_1, \dots, q_l) \) is a list of primes, with \( l \in \nN \), and \( p \mid \prod_{j=1}^{l} q_j \), then \( p = q_j \) for some \( j \in \{1, \dots, l\} \).
:::
:::

::: {.idea}
For (a), the gcd of \( p \) and \( a \) is a positive divisor of \( p \), so it is \( 1 \) or \( p \), and the second case says \( p \mid a \). Then (b) is Euclid's lemma in the first case of (a). For (c), peel the last prime off the product and apply (b) to the two factors; an induction on the length handles the rest, and a prime that divides a prime is equal to it.
:::

::: {.proof}
*(a)* Since \( p \ge 2 \), \( (p, a) \ne (0, 0) \), so \( g \coloneqq \gcd(p, a) \ge 1 \) (@def-integer-gcd). As a common divisor, \( g \mid p \) and \( g \mid a \). So \( g \) is a positive divisor of the prime \( p \), and \( g = 1 \) or \( g = p \) (@fd2:def-prime). If \( g = p \), then \( p \mid a \).

*(b)* Let \( p \mid bc \). By (a), \( p \mid b \) or \( \gcd(p, b) = 1 \). In the second case @thm-euclid-lemma-integers, with \( a = p \), gives \( p \mid c \).

*(c)* We use @fd1:ax-induction (through @cor-omega-identification (b)) on \( l \), for \( P(l) \): "for every list of primes \( (q_1, \dots, q_l) \), if \( p \mid \prod_{j=1}^{l} q_j \), then \( p = q_j \) for some \( j \le l \)".

*Base case \( P(0) \).* The empty product is \( 1 \) (the recursion of @def-prime-factorization). If \( p \mid 1 \), then \( p = 1 \) or \( p = -1 \) (@prp-divisibility-rules-integers (g)), and both contradict \( p \ge 2 \). So the hypothesis of \( P(0) \) never holds, and \( P(0) \) is true.

*Step.* Assume \( P(l) \), and let \( (q_1, \dots, q_{l+1}) \) be a list of primes with \( p \mid \prod_{j=1}^{l+1} q_j \). By the recursion of @def-prime-factorization,
\[
\prod_{j=1}^{l+1} q_j = \Bigl( \prod_{j=1}^{l} q_j \Bigr) q_{l+1} ,
\]
where the first factor is the product of the list of primes \( (q_1, \dots, q_l) \). By (b), \( p \) divides that first factor or \( p \mid q_{l+1} \). In the first case \( P(l) \) gives \( j \le l \) with \( p = q_j \). In the second, \( p \ge 2 > 0 \) is a positive divisor of the prime \( q_{l+1} \), so \( p \in \{1, q_{l+1}\} \), and \( p \ne 1 \); hence \( p = q_{l+1} \). This proves \( P(l + 1) \), and with it the corollary.
:::

Part (b) is the property promised at the start of the section, and it is what makes primes the right atoms for multiplication. It fails for \( 6 \), which is not prime: \( 6 \mid 2 \cdot 3 \), but \( 6 \nmid 2 \) and \( 6 \nmid 3 \), since \( 0 < 2 < 6 \) and \( 0 < 3 < 6 \) rule both out by @prp-divisibility-rules-integers (e).

The second application of Euclid's lemma combines two coprime divisors into one.

::: {#prp-coprime-divisors-product}
[Coprime Divisors of a Number]

Let \( m, n, c \in \nZ \) with \( m \mid c \), \( n \mid c \) and \( \gcd(m, n) = 1 \). Then \( mn \mid c \).
:::

::: {.proof}
Write \( c = km \) with \( k \in \nZ \). Then \( n \mid km \), and \( \gcd(n, m) = \gcd(m, n) = 1 \) (@def-integer-gcd), so @thm-euclid-lemma-integers gives \( n \mid k \), say \( k = ln \) with \( l \in \nZ \). Hence \( c = (ln)m = l(mn) \), by (F5) and (F6), and \( mn \mid c \).
:::

The coprimality is needed: \( 4 \mid 12 \) and \( 6 \mid 12 \), but \( 24 \nmid 12 \), since a positive divisor of \( 12 \) is at most \( 12 \) (@prp-divisibility-rules-integers (e)); here \( \gcd(4, 6) = 2 \).

## The least divisor is prime

The existence half of unique factorization needs a supply of primes: every integer \( n \ge 2 \) must have a prime factor. *Sets, Relations, and Cardinality*, Section 2.2 proved this for the school integers by strong induction (@fd2:thm-prime-factor). On the constructed \( \nZ \) the least-element property gives a shorter route: the least divisor bigger than \( 1 \) is already prime.

::: {#lem-least-divisor-prime}
[The Least Divisor Is Prime]

Let \( n \in \nZ \) with \( n \ge 2 \). The set \( D \coloneqq \{ d \in \nZ : d \ge 2 \text{ and } d \mid n \} \) has a least element, and that element is prime. In particular, \( n \) has a prime factor.
:::

::: {.proof}
Since \( n \ge 2 \) and \( n \mid n \) (@prp-divisibility-rules-integers (a)), \( n \in D \), so \( D \) is non-empty; and \( 2 \) is a lower bound of \( D \) by its definition. By @prp-integer-least-element, \( D \) has a least element \( p \).

Suppose \( p \) were not prime. Since \( p \ge 2 \), the clause of @fd2:def-prime that fails is the one about divisors: \( p \) has a positive divisor \( e \) with \( e \ne 1 \) and \( e \ne p \). Then \( e \ge 1 \) by discreteness (@thm-integers-ordered-ring (c)), and \( e \le p \) by @prp-divisibility-rules-integers (e). So \( 1 < e < p \), and \( e \ge 2 \) by discreteness again. Also \( e \mid p \) and \( p \mid n \) give \( e \mid n \) (@prp-divisibility-rules-integers (b)). So \( e \in D \) and \( e < p \), against the choice of \( p \). Hence \( p \) is prime, and \( p \mid n \) because \( p \in D \).
:::

::: {.remark}
This is @fd2:thm-prime-factor on the constructed \( \nZ \), proved by a least element instead of strong induction. It also shortens the primality test of Section 3.1's small-primes remark. If \( p \ge 2 \) is not prime, its least divisor \( e \ge 2 \) is prime by the lemma, so it is not \( p \) itself, and \( p = ef \) with \( f \in \nZ \); then \( f > 0 \) (as \( e, p > 0 \)), \( f \ne 1 \), so \( f \ge 2 \) and \( f \mid p \), and therefore \( e \le f \) by the choice of \( e \). Multiplying by \( e > 0 \) gives \( e \cdot e \le ef = p \) (@prp-ordered-ring-rules (c)). So to prove \( p \ge 2 \) prime it is enough to check that **no** \( d \) with \( d \ge 2 \) and \( d \cdot d \le p \) divides \( p \). For \( 11 \) only \( d = 2, 3 \) need checking, since \( 4 \cdot 4 = 16 > 11 \).
:::

## The fundamental theorem

Everything is now in place for the main result of the chapter's first half.

::: {#thm-fundamental-arithmetic}
[Fundamental Theorem of Arithmetic]

Every \( n \in \nZ_{>0} \) has **exactly one** prime factorization.
:::

::: {.idea}
*Existence.* Take the least \( n \) with no factorization. It is at least \( 2 \), so it has prime factors, and a largest one, \( p \). Then \( n = pm \) with \( m < n \), so \( m \) has a factorization. Every entry of it divides \( n \), so it is at most \( p \), and appending \( p \) at the end keeps the list non-decreasing.

*Uniqueness.* Take two factorizations with the same product, \( (p_1, \dots, p_k) \) and \( (q_1, \dots, q_l) \). The largest entry \( p_k \) divides the product of the \( q \)'s, so by @cor-prime-divides-product (c) it **is** one of the \( q_j \), and that is at most the largest, \( q_l \). By symmetry \( q_l \le p_k \). So the two last entries are equal; cancel them and induct on the length.

*Before reading on: why compare the largest primes, \( p_k \) and \( q_l \), and not the first ones?*
:::

::: {.proof}
*Existence.* Let \( B \coloneqq \{ n \in \nZ_{>0} : n \text{ has no prime factorization} \} \), and suppose \( B \ne \emptyset \). It has the lower bound \( 0 \), so it has a least element \( n \) (@prp-integer-least-element). The empty list is a prime factorization of \( 1 \), so \( n \ne 1 \); as \( n \ge 1 \) (discreteness, @thm-integers-ordered-ring (c)), \( n > 1 \), and so \( n \ge 2 \) by discreteness.

The set \( F \) of prime factors of \( n \) is non-empty by @lem-least-divisor-prime. Each \( q \in F \) is positive and divides \( n > 0 \), so \( q \le n \) (@prp-divisibility-rules-integers (e)). By @prp-integer-least-element, \( F \) has a greatest element \( p \). Write \( n = mp \) with \( m \in \nZ \). If \( m \le 0 \), then \( mp \le 0 \) (\( m = 0 \): @prp-ring-algebra (b); \( m < 0 \): \( mp < 0 \cdot p = 0 \) by @prp-ordered-ring-rules (c)), against \( n > 0 \). So \( m > 0 \), that is, \( m \in \nZ_{>0} \) (@thm-integers-ordered-ring (b)). Moreover \( m < n \): since \( p \ge 2 \) and \( m > 0 \), \( n = pm \ge 2m = m + m > m \), by @prp-ordered-ring-rules (c) (or equality if \( p = 2 \)), (F9) with (F7), and (O3).

By the minimality of \( n \), \( m \notin B \): let \( (q_1, \dots, q_l) \) be a prime factorization of \( m \). If \( l \ge 1 \), the recursion of @def-prime-factorization gives \( m = \bigl(\prod_{j=1}^{l-1} q_j\bigr) q_l \), so \( q_l \mid m \); with \( m \mid n \) this gives \( q_l \mid n \) (@prp-divisibility-rules-integers (b)), so \( q_l \in F \) and \( q_l \le p \). As the list is non-decreasing, \( q_i \le q_l \le p \) for every \( i \le l \). Now let \( (q_1, \dots, q_l, p) \) be the list of length \( l + 1 \) whose first \( l \) entries are those of \( (q_1, \dots, q_l) \) and whose last entry is \( p \). Its entries are prime. It is non-decreasing: two positions among the first \( l \) compare as before, and every entry is at most \( p \) (for \( l = 0 \) it is the one-entry list \( (p) \), and there is nothing to check). By the recursion its product is
\[
\Bigl( \prod_{j=1}^{l} q_j \Bigr) p = mp = n .
\]
So \( n \) has a prime factorization, against \( n \in B \). Hence \( B = \emptyset \).

*Uniqueness.* We prove, by @fd1:ax-induction (through @cor-omega-identification (b)) on \( k \), the statement \( P(k) \): "for every \( l \in \nN \), if \( (p_1, \dots, p_k) \) and \( (q_1, \dots, q_l) \) are non-decreasing lists of primes with \( \prod_{i=1}^{k} p_i = \prod_{j=1}^{l} q_j \), then \( l = k \) and \( p_i = q_i \) for every \( i \le k \)". Two prime factorizations of the same \( n \) are such lists, so \( P(k) \) for every \( k \) gives the uniqueness.

First, a non-empty list of primes \( (r_1, \dots, r_h) \) does not have product \( 1 \): by the recursion its product is \( \bigl(\prod_{i=1}^{h-1} r_i\bigr) r_h \), so \( r_h \) would divide \( 1 \), and \( r_h = \pm 1 \) (@prp-divisibility-rules-integers (g)) contradicts \( r_h \ge 2 \).

*Base case \( P(0) \).* If \( k = 0 \), then \( \prod_{j=1}^{l} q_j = 1 \), so \( l = 0 \) by the previous paragraph, and both lists are empty.

*Step.* Assume \( P(k) \). Let \( (p_1, \dots, p_{k+1}) \) and \( (q_1, \dots, q_l) \) be non-decreasing lists of primes with the same product \( N \). Since \( k + 1 \ge 1 \), \( N \ne 1 \), so \( l \ge 1 \). By the recursion, \( p_{k+1} \mid N = \prod_{j=1}^{l} q_j \), so @cor-prime-divides-product (c) gives \( p_{k+1} = q_j \) for some \( j \le l \), and \( q_j \le q_l \) because the \( q \)-list is non-decreasing. In the same way \( q_l \mid N = \prod_{i=1}^{k+1} p_i \) gives \( q_l = p_i \le p_{k+1} \) for some \( i \le k + 1 \). So \( p_{k+1} \le q_l \le p_{k+1} \), and \( p_{k+1} = q_l \) (@prp-ordered-ring-rules (i)). By the recursion,
\[
\Bigl( \prod_{i=1}^{k} p_i \Bigr) p_{k+1} = N = \Bigl( \prod_{j=1}^{l-1} q_j \Bigr) p_{k+1} .
\]
Subtracting, \( \bigl(\prod_{i=1}^{k} p_i - \prod_{j=1}^{l-1} q_j\bigr) p_{k+1} = 0 \) by (F9) and @prp-ring-algebra (c), and \( p_{k+1} \ne 0 \), so the bracket is \( 0 \) (@prp-ordered-ring-rules (f)). The shortened lists \( (p_1, \dots, p_k) \) and \( (q_1, \dots, q_{l-1}) \) are non-decreasing lists of primes with equal products, so \( P(k) \), applied with \( l - 1 \in \nN \), gives \( l - 1 = k \) and \( p_i = q_i \) for \( i \le k \). With \( p_{k+1} = q_l = q_{k+1} \), the two lists have the same length \( k + 1 \) and the same entries, so they are equal (@fd2:prp-function-equality). This proves \( P(k + 1) \), and the theorem.
:::

The answer to the prompt lies in the recursion of @def-prime-factorization. It peels off the **last** factor, so once the two last entries are known to be equal they can be canceled at once, leaving two shortened lists to which \( P(k) \) applies. And the comparison "largest with largest" needs only that both lists are non-decreasing. Comparing the first entries would also show \( p_1 = q_1 \), but removing a first entry shifts every index, and the recursion says nothing directly about that.

::: {.remark}
*Sets, Relations, and Cardinality*, Section 2.2 named unique factorization as a fact it did not prove or use, and @fd2:exr-countable-sets-b2 lists, as line (vii), a step that cites it and is therefore not available there. On the constructed \( \nZ \) the fact is now proved, and Exercise R2 of Section 3.5 uses it.
:::

::: {.warning}
**Uniqueness is not automatic.** Let \( H \coloneqq \{ 4k + 1 : k \in \nN \} = \{1, 5, 9, 13, 17, 21, \dots\} \). It is closed under multiplication, since \( (4k + 1)(4l + 1) = 4(4kl + k + l) + 1 \). Call \( h \in H \) with \( h > 1 \) an **\( H \)-prime** if it is not a product of two elements of \( H \) both greater than \( 1 \). Then \( 9 \), \( 21 \) and \( 49 \) are \( H \)-primes, and
\[
441 = 9 \cdot 49 = 21 \cdot 21
\]
gives two different factorizations into \( H \)-primes. What breaks is Euclid's lemma: \( 9 \) divides \( 21 \cdot 21 \) inside \( H \), but \( 9 \nmid 21 \). The proof of @thm-euclid-lemma-integers wrote \( 1 = ax + by \), with **sums** and with negative coefficients, and \( H \) is closed under neither. The proof of uniqueness above is only as good as Euclid's lemma.
:::

## Lowest terms

Every rational number is a fraction in many ways: \( 6/4 = 3/2 = 9/6 \). Section 2.4 found, in its Exercise C1, a least positive denominator by the least-element property, and *Sets, Relations, and Cardinality*, Section 2.2 removed common factors of \( 2 \) only (@fd2:lem-lowest-terms). With the gcd we can remove every common factor at once, and Euclid's lemma shows that the result is unique. Recall that after the identification of Section 2.4, \( p/q \coloneqq pq^{-1} \) in \( \nQ \) for \( p \in \nZ \) and \( q \in \nZ_{>0} \), and \( p/q = r/s \) holds if and only if \( ps = rq \) (@prp-integers-embed-rationals (b)).

::: {#prp-rationals-lowest-terms}
[Lowest Terms]

Let \( x \in \nQ \).

::: {.enumerate options="label=(\alph*)"}
1. There are \( p \in \nZ \) and \( q \in \nZ_{>0} \) with \( x = p/q \) and \( \gcd(p, q) = 1 \), and the pair \( (p, q) \) is **unique**.
2. If \( x = r/s \) with \( r \in \nZ \) and \( s \in \nZ_{>0} \), then \( r = tp \) and \( s = tq \) for some \( t \in \nZ_{>0} \). In particular \( q \mid s \) and \( q \le s \): \( q \) is the least positive denominator of \( x \).
:::
:::

::: {.idea}
For existence, divide numerator and denominator by their gcd \( d \); the Bézout identity for \( d \), divided by \( d \), is a Bézout identity \( 1 = px_0 + qy_0 \) for the new pair. For (b), cross-multiplying gives \( ps = rq \), so \( q \mid ps \), and Euclid's lemma removes \( p \). Uniqueness is (b) applied to a second coprime pair.
:::

::: {.proof}
*Existence in (a).* By @prp-integers-embed-rationals (b), \( x = r/s \) for some \( r \in \nZ \), \( s \in \nZ_{>0} \). Since \( s \ne 0 \), \( d \coloneqq \gcd(r, s) \ge 1 \), and by @thm-integers-bezout (d) there are \( x_0, y_0 \in \nZ \) with \( d = rx_0 + sy_0 \). As \( d \mid r \) and \( d \mid s \), write \( r = dp \) and \( s = dq \) with \( p, q \in \nZ \). If \( q \le 0 \), then \( dq \le 0 \) (as in the existence proof of @thm-fundamental-arithmetic), against \( s > 0 \); so \( q \in \nZ_{>0} \). Now
\[
d \cdot 1 = d = (dp)x_0 + (dq)y_0 = d(px_0 + qy_0) ,
\]
so \( d(px_0 + qy_0 - 1) = 0 \), and since \( d \ne 0 \), \( px_0 + qy_0 = 1 \) (@prp-ordered-ring-rules (f)). Hence \( \gcd(p, q) = 1 \) by @cor-coprime-iff-combination. Finally \( rq = dpq = p(dq) = ps \), so \( r/s = p/q \) by @prp-integers-embed-rationals (b), and \( x = p/q \).

*(b), for any such pair.* Let \( x = p/q \) with \( \gcd(p, q) = 1 \), and \( x = r/s \) with \( s > 0 \). By @prp-integers-embed-rationals (b), \( ps = rq \). So \( q \mid ps \), and \( \gcd(q, p) = 1 \), hence \( q \mid s \) by @thm-euclid-lemma-integers; write \( s = tq \) with \( t \in \nZ \). Since \( s > 0 \) and \( q > 0 \), \( t > 0 \), by the sign argument used for \( q \) above. Then \( q(pt) = ps = rq \), so \( q(pt - r) = 0 \), and \( r = tp \) because \( q \ne 0 \) (@prp-ordered-ring-rules (f)). As \( q \) and \( s \) are positive, \( q \mid s \) gives \( q \le s \) (@prp-divisibility-rules-integers (e)).

*Uniqueness in (a).* Let \( (r, s) \) be a second pair with \( x = r/s \), \( s > 0 \) and \( \gcd(r, s) = 1 \). By (b), \( r = tp \) and \( s = tq \) with \( t > 0 \). So \( t \) is a common divisor of \( r \) and \( s \), and it divides \( \gcd(r, s) = 1 \) (@thm-integers-bezout (c), (d)). Hence \( t = 1 \) (@prp-divisibility-rules-integers (g), with \( t > 0 \)), and \( (r, s) = (p, q) \).
:::

So the least denominator \( N(x) \) of Section 2.4's Exercise C1 is the \( q \) of (a), and every other denominator of \( x \) is a multiple of it. For example \( 252/198 \) has \( \gcd(252, 198) = 18 \) (@exm-euclidean-algorithm-run), and \( 252 = 18 \cdot 14 \), \( 198 = 18 \cdot 11 \), so its lowest terms are \( 14/11 \).

::: {.remark}
The twins in *Sets, Relations, and Cardinality*, Section 2.2 are @fd2:lem-lowest-terms, which removes only factors of \( 2 \), and @fd2:exr-induction-in-practice-c2, which asks for lowest terms in the full sense, for the school \( \nQ \). @prp-rationals-lowest-terms is the full statement, with uniqueness, for the constructed \( \nQ \).
:::

## Exercises

### A. Check your understanding

::: {#exr-unique-factorization-a1}
[A1]

These questions are about the uniqueness half of the proof of @thm-fundamental-arithmetic.

::: {.enumerate options="label=(\alph*)"}
1. Why must the empty list count as a prime factorization?
2. Run the induction step on \( (p_1, p_2, p_3, p_4) = (2, 2, 3, 5) \) and a second prime factorization \( (q_1, \dots, q_l) \) of \( 60 \). Which equalities does the proof derive, and to which two lists is \( P(3) \) applied?
3. Which line of the proof uses Euclid's lemma, and through which result?
4. Where is "non-decreasing" used?
5. Give the idea of the uniqueness proof in two sentences.
:::
:::

::: {.solution}
(a) Without it the base case \( P(0) \) would be about nothing, and the number \( 1 \) would have no prime factorization, so the theorem would be false for \( n = 1 \). The existence proof also uses it, to exclude \( n = 1 \) from \( B \).

(b) The step first gets \( l \ge 1 \), since the product is \( 60 \ne 1 \). Then \( p_4 = 5 \) divides \( \prod q_j \), so \( 5 = q_j \le q_l \) for some \( j \); and \( q_l \) divides \( 60 = 2 \cdot 2 \cdot 3 \cdot 5 \), so \( q_l = p_i \le 5 \) for some \( i \). Hence \( q_l = 5 \). Canceling \( 5 \) gives \( \prod_{j=1}^{l-1} q_j = 2 \cdot 2 \cdot 3 = 12 \), and \( P(3) \) is applied to \( (2, 2, 3) \) and \( (q_1, \dots, q_{l-1}) \), which gives \( l - 1 = 3 \) and \( (q_1, q_2, q_3) = (2, 2, 3) \).

(c) The lines "\( p_{k+1} = q_j \) for some \( j \)" and "\( q_l = p_i \) for some \( i \)". They cite @cor-prime-divides-product (c), whose step uses (b), which is @thm-euclid-lemma-integers applied with \( a = p \).

(d) In \( q_j \le q_l \) and in \( p_i \le p_{k+1} \): the entry found in the other list is at most that list's last entry.

(e) The largest prime of one factorization divides the other product, so by Euclid's lemma it is an entry there, hence at most the other's largest; by symmetry the two largest entries are equal. Canceling them leaves two shorter factorizations with equal products, and induction on the length finishes.
:::

### B. Practice

::: {#exr-unique-factorization-b1}
[B1: Put the proof in order]

The following lines contain a proof of @thm-euclid-lemma-integers, shuffled, together with two lines that do not belong. Write the seven correct lines in an order that makes a proof, say which other orders are also admissible, and say why each of the other two lines fails.

(i) Suppose \( a \mid bc \) and \( \gcd(a, b) = 1 \).

(ii) There are \( x, y \in \nZ \) with \( ax + by = 1 \).

(ii′) Since \( \gcd(a, b) = 1 \) and \( a \mid bc \), we have \( a \mid b \) or \( a \mid c \).

(iii) Multiplying by \( c \): \( c = acx + bcy \).

(iii′) Dividing \( 1 = ax + by \) by \( a \): \( 1/a = x + (b/a)y \).

(iv) \( a \mid acx \), since \( acx = a(cx) \).

(v) Write \( bc = ak \); then \( bcy = a(ky) \), so \( a \mid bcy \).

(vi) Hence \( a \mid acx + bcy \).

(vii) So \( a \mid c \).
:::

::: {.solution}
An admissible order is (i), (ii), (iii), (iv), (v), (vi), (vii):

> Suppose \( a \mid bc \) and \( \gcd(a, b) = 1 \). There are \( x, y \in \nZ \) with \( ax + by = 1 \) (@cor-coprime-iff-combination). Multiplying by \( c \): \( c = acx + bcy \). Then \( a \mid acx \), since \( acx = a(cx) \). Write \( bc = ak \); then \( bcy = a(ky) \), so \( a \mid bcy \). Hence \( a \mid acx + bcy \) (@prp-divisibility-rules-integers (c)). So \( a \mid c \).

Lines (iv) and (v) mention the \( x \) and \( y \) introduced in (ii), and (v) also uses the hypothesis \( a \mid bc \) of (i); neither uses the other or (iii). So they may be exchanged, and either may come before (iii), as long as both follow (ii). Everything else is forced: (ii) needs the hypothesis \( \gcd(a, b) = 1 \) of (i); (iii) multiplies the equation of (ii); (vi) needs both (iv) and (v); (vii) rewrites (vi) through the equation of (iii).

The distractor (ii′) cites a "fact" that is not available. For a prime \( a \) it is @cor-prime-divides-product (b), which is proved **from** this lemma, so citing it here is circular; for a composite \( a \) nothing provides it. Either way the line uses what has not been established, which is (N9) of @fd1:exm-not-allowed-catalogue.

The distractor (iii′) divides in \( \nZ \), where there is no division: \( 1/a \) is not an integer for \( a \ge 2 \), and divisibility is defined by multiplication (@fd2:def-divides), not by fractions.
:::

::: {#exr-unique-factorization-b2}
[B2: The least common multiple]

Let \( a, b \in \nZ_{>0} \), and let \( M \coloneqq \{ m \in \nZ_{>0} : a \mid m \text{ and } b \mid m \} \). Prove that \( M \) has a least element \( L \), and that \( L \mid c \) for **every** \( c \in \nZ \) with \( a \mid c \) and \( b \mid c \).

The first part of a proof is given.

> \( ab > 0 \) by (O4), and \( a \mid ab \), \( b \mid ab \), so \( ab \in M \); and \( 0 \) is a lower bound of \( M \). By @prp-integer-least-element, \( M \) has a least element \( L \). Let \( c \in \nZ \) with \( a \mid c \) and \( b \mid c \). By @thm-integers-division-remainder (a), \( c = qL + r \) with \( q, r \in \nZ \) and \( 0 \le r < L \). Since \( r = c + (-q)L \), and \( a \) divides \( c \) and \( L \), \( a \mid r \) (@prp-divisibility-rules-integers (c)); likewise \( b \mid r \).

The last step is blank. *Name the move, then complete it.*
:::

::: {.solution}
The move is **least positive element, then divide**: the remainder lies in the set and is smaller than its least positive element, so it is not positive.

Completion: if \( r > 0 \), then \( r \in \nZ_{>0} \) is a common multiple of \( a \) and \( b \), so \( r \in M \), and \( r < L \), against the choice of \( L \). Hence \( r = 0 \) (as \( r \ge 0 \)), and \( c = qL \), that is, \( L \mid c \).

The same argument proved @thm-integers-bezout (b), with the set of positive combinations in place of \( M \). This is the twin of @fd2:exm-divisibility-lcm, now on the constructed \( \nZ \).
:::

::: {#exr-unique-factorization-b3}
[B3: Two factorizations and a gcd]

Find the prime factorizations of \( 1001 \) and of \( 2^{10} - 1 \), proving that each entry is prime. Then show that \( \gcd(1001, 1023) = 11 \) in two ways: from the factorizations, and by the Euclidean algorithm.

*Hint: the remark after @lem-least-divisor-prime shortens each primality check.*
:::

::: {.solution}
*Factorizations.* \( 1001 = 7 \cdot 143 = 7 \cdot 11 \cdot 13 \), and \( 2^{10} - 1 = 1024 - 1 = 1023 = 3 \cdot 341 = 3 \cdot 11 \cdot 31 \). So the prime factorizations are \( (7, 11, 13) \) and \( (3, 11, 31) \), both non-decreasing, once the entries are known to be prime. The primes \( 3 \) and \( 7 \) are covered by the small-primes remark of Section 3.1. For \( 11 \), \( 13 \) and \( 31 \) we use the remark after @lem-least-divisor-prime: it suffices that no \( d \ge 2 \) with \( d \cdot d \le p \) divides \( p \).

- \( p = 11 \) and \( p = 13 \): \( d \in \{2, 3\} \), since \( d \ge 4 \) gives \( d \cdot d \ge 16 \). The divisions \( 11 = 5 \cdot 2 + 1 = 3 \cdot 3 + 2 \) and \( 13 = 6 \cdot 2 + 1 = 4 \cdot 3 + 1 \) leave non-zero remainders.
- \( p = 31 \): \( d \in \{2, 3, 4, 5\} \), since \( d \ge 6 \) gives \( d \cdot d \ge 36 \). The divisions \( 31 = 15 \cdot 2 + 1 = 10 \cdot 3 + 1 = 7 \cdot 4 + 3 = 6 \cdot 5 + 1 \) leave non-zero remainders.

A non-zero remainder means \( d \nmid p \), by the uniqueness in @thm-integers-division-remainder (a). By @thm-fundamental-arithmetic these are the only prime factorizations.

*The gcd from the factorizations.* We do not use a rule "the gcd is the product of the shared primes", which this chapter does not prove. We have \( 1001 = 11 \cdot 91 \) and \( 1023 = 11 \cdot 93 \). First, \( \gcd(91, 93) = 1 \): a common divisor of \( 91 \) and \( 93 \) divides \( 93 - 91 = 2 \) (@prp-divisibility-rules-integers (c)), so a positive one is \( 1 \) or \( 2 \) (@prp-divisibility-rules-integers (e) and discreteness), and \( 2 \nmid 91 = 45 \cdot 2 + 1 \). By @cor-coprime-iff-combination, \( 91x + 93y = 1 \) for some \( x, y \in \nZ \); indeed \( 91 \cdot 46 - 93 \cdot 45 = 4186 - 4185 = 1 \). Multiplying by \( 11 \),
\[
1001 \cdot 46 - 1023 \cdot 45 = 11 .
\]
So every common divisor of \( 1001 \) and \( 1023 \) divides \( 11 \) (@prp-divisibility-rules-integers (c)), and a positive one is at most \( 11 \) (@prp-divisibility-rules-integers (e)). Since \( 11 \) is itself a common divisor, \( \gcd(1001, 1023) = 11 \) (@def-integer-gcd).

*The gcd by the algorithm* (@thm-euclidean-algorithm-integers): \( 1023 = 1 \cdot 1001 + 22 \), \( 1001 = 45 \cdot 22 + 11 \), \( 22 = 2 \cdot 11 + 0 \). The last non-zero remainder is \( 11 \).
:::

### C. Going deeper

::: {#exr-unique-factorization-c1}
[C1: Exit check: unique factorization]

Prove that two prime factorizations of the same positive integer are equal: the uniqueness half of @thm-fundamental-arithmetic. You may cite @thm-euclid-lemma-integers.
:::

::: {.solution}
The proof of uniqueness in @thm-fundamental-arithmetic is a complete answer. Its steps, in order: set up \( P(k) \) for non-decreasing lists of primes of length \( k \) and arbitrary length \( l \), with equal products; base case \( k = 0 \), where a non-empty list of primes cannot have product \( 1 \); in the step, \( l \ge 1 \), then \( p_{k+1} = q_j \le q_l \) and \( q_l = p_i \le p_{k+1} \) by @cor-prime-divides-product (c) (proved from Euclid's lemma by induction on the length of the product) and the order of the lists; so \( p_{k+1} = q_l \); cancel this non-zero factor (@prp-ordered-ring-rules (f)); apply \( P(k) \) to the shortened lists.

**Marking scheme.** (10 points)
- 2: sets up an induction on the length of one list (or a least counterexample), with the statement quantified over all lengths of the other list, and proves the base case.
- 3: shows that the largest (or any chosen) prime of one list divides the other product, and identifies it with an entry of the other list by Euclid's lemma for products of several factors, proved or cited.
- 2: uses the symmetric step and the non-decreasing order to get equality of the two largest entries.
- 1: justifies the cancellation by the absence of zero divisors.
- 2: applies the induction hypothesis (or minimality) to the shortened lists and concludes equality of length and entries.
Fatal errors (0 for the step): using the uniqueness of the factorization of a smaller number without an induction or a least counterexample set up; applying Euclid's lemma for two factors to a product of many with no induction. Canceling a prime without noting that it is non-zero costs 1 point and is not fatal. A least-counterexample proof on \( n \) (the least positive integer with two different factorizations) maps to the same points: its set-up and the case \( n = 1 \) take the first 2, and "the cofactor \( m \) in \( n = m p_k \) has only one factorization" takes the last 2.
:::

::: {#exr-unique-factorization-c2}
[C2: Find the error]

Here is a statement and an argument for it.

> **Claim.** Let \( m, n, c \in \nZ \). If \( m \mid c \), \( n \mid c \) and \( \gcd(m, n) = 1 \), then \( mn \mid c \).
>
> **Argument.** (1) Write \( c = mk \) and \( c = nl \) with \( k, l \in \nZ \). (2) Then \( c^2 = c \cdot c = (mk)(nl) = mn \cdot kl \). (3) So \( mn \mid c^2 \). (4) Hence \( mn \mid c \).

Is the claim true? Does the argument prove it? If not, name the line that fails, explain why, and give a counterexample to the step.
:::

::: {.solution}
The claim is **true**: it is @prp-coprime-divisors-product. The argument does **not** prove it.

Lines (1)–(3) are correct. The failing line is (4). It rests on a general "fact": \( x \mid c^2 \) implies \( x \mid c \). That has not been proved, and it is false, so the line cites nothing: entry (N9) of @fd1:exm-not-allowed-catalogue. A counterexample to the step: \( x = 4 \), \( c = 2 \), with \( 4 \mid 4 = c^2 \) and \( 4 \nmid 2 \) (a positive divisor of \( 2 \) is at most \( 2 \), @prp-divisibility-rules-integers (e)). There is no counterexample to the conclusion, which is true.

A sign that something is wrong: the argument never uses \( \gcd(m, n) = 1 \), and without that hypothesis the claim is false (\( 4 \mid 12 \), \( 6 \mid 12 \), \( 24 \nmid 12 \)). The repair is the proof of @prp-coprime-divisors-product, which spends the coprimality in Euclid's lemma.
:::

::: {#exr-unique-factorization-c3}
[C3: There is no last prime]

Prove that no finite list contains every prime: for every list of primes \( (p_1, \dots, p_k) \), with \( k \in \nN \), there is a prime that is not an entry of the list.
:::

::: {.solution}
[Hint 1]

Consider \( N \coloneqq \prod_{i=1}^{k} p_i + 1 \), and ask which primes can divide it.
:::

::: {.solution}
[Hint 2]

First prove, by induction on \( k \), that every entry of a list of primes divides its product, and that the product is at least \( 1 \).
:::

::: {.solution}
*A lemma on products.* For a list of primes \( (p_1, \dots, p_k) \), write \( P_j \coloneqq \prod_{i=1}^{j} p_i \) for \( j \le k \). We prove, by @fd1:ax-induction (through @cor-omega-identification (b)) on \( j \), the statement "if \( j \le k \), then \( P_j \ge 1 \) and \( p_i \mid P_j \) for every \( i \le j \)". Base \( j = 0 \): \( P_0 = 1 \) (the recursion of @def-prime-factorization), and there are no entries to check. Step: let \( j + 1 \le k \); then \( j \le k \), so the statement holds for \( j \), and \( P_{j+1} = P_j p_{j+1} \) by the recursion. Each \( p_i \) with \( i \le j \) divides \( P_j \), which divides \( P_{j+1} \), so \( p_i \mid P_{j+1} \) (@prp-divisibility-rules-integers (b)); and \( p_{j+1} \mid P_{j+1} \) by @fd2:def-divides. Since \( P_j \ge 1 > 0 \) and \( p_{j+1} \ge 2 > 0 \), \( P_{j+1} > 0 \cdot p_{j+1} = 0 \) (@prp-ordered-ring-rules (c), @prp-ring-algebra (b)), so \( P_{j+1} \ge 1 \) by discreteness (@thm-integers-ordered-ring (c)).

*The new prime.* Let \( N \coloneqq P_k + 1 \). Then \( N \ge 2 \), so its least divisor \( q \ge 2 \) is prime (@lem-least-divisor-prime), and \( q \mid N \). If \( q = p_i \) for some \( i \), then \( q \mid P_k \) by the lemma, so \( q \) divides \( N - P_k = 1 \) (@prp-divisibility-rules-integers (c)), and \( q = \pm 1 \) (@prp-divisibility-rules-integers (g)), against \( q \ge 2 \). So \( q \) is a prime that is not an entry of the list.

For the empty list, \( N = 2 \) and \( q = 2 \). For \( (2, 3, 5, 7) \), \( N = 211 \), which happens to be prime; for \( (2, 3, 5, 7, 11, 13) \), \( N = 30031 = 59 \cdot 509 \) is not, and the new prime is \( 59 \). The proof promises a new prime factor of \( N \), not that \( N \) itself is prime.

**Marking scheme.** (10 points)
- 2: defines \( N \) as the product plus \( 1 \) and shows \( N \ge 2 \), with a reason that the product is positive.
- 2: shows that each \( p_i \) divides the product, by an induction or a cited result.
- 2: produces a prime factor \( q \) of \( N \), citing @lem-least-divisor-prime or an equivalent.
- 3: shows \( q \) is not any \( p_i \), since it would divide \( 1 \).
- 1: concludes with the quantifiers in order: for every list there is a prime outside it.
Fatal errors (0 for the step): claiming that \( N \) is prime; assuming "the set of primes is finite" and taking its product without a list (no list, no product).
:::

<!-- dependency ledger
thm-euclid-lemma-integers (claim): (opening) 60 = 2*30 = 6*10 = 4*15, factored to 2, 2, 3, 5 | numerals computed in N via prp-naturals-embed-integers (a) (cited); verify/ch03/def-prime-factorization.py
thm-euclid-lemma-integers (proof): c = c * 1 = c(ax + by) = a(cx) + (bc)y, rearrangements | ring axioms (F5)-(F7), (F9) of def-commutative-ring-and-field for Z (thm-integers-commutative-ring), named in the proof
thm-euclid-lemma-integers (claim): (aftermath) 4 | 12, 6 = 1*4 + 2, gcd(4, 2) = 2 | numerals; thm-integers-division-remainder (a) (cited); gcd(4, 2) = 2 from def-integer-gcd: 2 is a common divisor, a positive common divisor of 2 is <= 2 (prp-divisibility-rules-integers (e)); verify/ch03/thm-euclid-lemma-integers.py
def-prime-factorization (claim): products of lists by fd2:def-sum-product used as a pattern; its recursive clause and the proof of its "Finite lists" remark use only fd2:thm-recursion, fd1:ax-induction on omega and the multiplication of the target set, so they run with X = Z (an ordered commutative ring, F3.2); equivalently read in Q containing Z, closed under * (prp-integers-embed-rationals); the general-index part (fd2:prp-integers-closed) is not used | F3.1 citing rule, group (iii) (cor-omega-identification, Section 1.7), stated in the text; blueprint ch03.md template ledger line
def-prime-factorization (claim): the extension pbar with pbar_i = 1 for i > k is a function on Z>0 | definition by cases on i <= k (thm-integers-ordered-ring (a), order of N), inline
def-prime-factorization (example): (2, 2, 3, 5) products 1, 2, 4, 12, 60; non-examples (2, 3, 2, 5), (2, 2, 15); 15 = 3 * 5 not prime | small-primes remark of Section 3.1 (by name); numerals; verify/ch03/def-prime-factorization.py
def-prime-factorization (claim): (why) 60 has twelve orderings of (2, 2, 3, 5) | counting 4!/2! = 12, stated as motivation, nothing depends on it; verify/ch03/def-prime-factorization.py
def-prime-factorization (claim): (check) 360 = (2, 2, 2, 3, 3, 5), products 1, 2, 4, 8, 24, 72, 360 | small-primes remark (by name); numerals; verify/ch03/def-prime-factorization.py
cor-prime-divides-product (proof): p >= 2 > 0, so (p, a) != (0, 0) and p is positive | 0 < 1 < 2 by prp-ordered-ring-rules (e) and (O3), transitivity (O2); used silently
cor-prime-divides-product (claim): (aftermath) 6 | 6, 6 not dividing 2 or 3 | prp-divisibility-rules-integers (e) (cited); numerals
prp-coprime-divisors-product (claim): (aftermath) 4 | 12, 6 | 12, 24 not dividing 12, gcd(4, 6) = 2 | prp-divisibility-rules-integers (e) (cited); gcd(4, 6) = 2 by def-integer-gcd as above; verify/ch03/prp-coprime-divisors-product.py
lem-least-divisor-prime (claim): (remark) f > 0 from p = ef with e, p > 0; f != 1 since e != p | sign argument as in thm-fundamental-arithmetic existence (prp-ring-algebra (b), prp-ordered-ring-rules (c)), inline; (F7)
lem-least-divisor-prime (claim): (remark) d >= 4 gives d * d >= 16 > 11 | prp-ordered-ring-rules (c) twice and transitivity, numerals; verify/ch03/lem-least-divisor-prime.py
thm-fundamental-arithmetic (proof): 2m = m + m > m for m > 0; pm >= 2m for p >= 2 | (F9), (F7), (O3); prp-ordered-ring-rules (c) applied to (p - 2) > 0, or equality; named in the proof
thm-fundamental-arithmetic (proof): the appended list (q_1, ..., q_l, p) is a function on {1, ..., l + 1} and its first l entries give the shortened list | def-prime-factorization (recursion, cited), definition by cases on i <= l, inline
thm-fundamental-arithmetic (proof): induction on k with the statement quantified over l; l - 1 in N for l >= 1 | fd1:ax-induction via cor-omega-identification (b) (cited); prp-omega-order-arithmetic (a) for l - 1, used silently
thm-fundamental-arithmetic (proof): equality of lists from equal length and entries | fd2:prp-function-equality (cited)
thm-fundamental-arithmetic (claim): (warning) H closed under *; (4k + 1)(4l + 1) = 4(4kl + k + l) + 1; 9, 21, 49 are H-prime; 441 = 9 * 49 = 21 * 21; 9 divides 21 * 21 in H and 9 does not divide 21 | ring arithmetic; H-primality by finite check of elements 5, 9, ..., h - 4 of H; verify/ch03/thm-fundamental-arithmetic.py
thm-fundamental-arithmetic (claim): (remark) Exercise R2 of Section 3.5 uses unique factorization | blueprint ch03.md, 05-units-and-crt R2 (prose pointer within the chapter); nothing here depends on it
prp-rationals-lowest-terms (proof): p/q := p q^{-1}; r/s = p/q iff ps = rq; every x is r/s | prp-integers-embed-rationals (b) (cited) and the identification of Section 2.4, recalled in prose
prp-rationals-lowest-terms (proof): q > 0 and t > 0 from products of positives being positive | sign argument of thm-fundamental-arithmetic existence (prp-ring-algebra (b), prp-ordered-ring-rules (c)), referenced
prp-rationals-lowest-terms (claim): N(x) of Section 2.4 C1 equals q | exr-rationals-as-classes-c1 (F3.2, an exercise; prose remark only, no proof uses it)
prp-rationals-lowest-terms (example): 252 = 18 * 14, 198 = 18 * 11, lowest terms 14/11; gcd(14, 11) = 1 by (a) | exm-euclidean-algorithm-run (cited); numerals; verify/ch03/prp-rationals-lowest-terms.py
exr-unique-factorization-a1 (solution): run of the step on (2, 2, 3, 5); q_l divides 60 so q_l in {2, 3, 5} | cor-prime-divides-product (c) (cited); verify/ch03/exr-unique-factorization-a1.py
exr-unique-factorization-b1 (solution): admissible orders; distractors | the solution's own analysis
exr-unique-factorization-b2 (solution): ab > 0 by (O4); a | ab | def-ordered-ring-and-field (O4), fd2:def-divides
exr-unique-factorization-b3 (solution): 1001 = 7 * 11 * 13, 1023 = 3 * 11 * 31, 2^10 = 1024; the divisions by 2, 3, 4, 5; 91 * 46 - 93 * 45 = 1; Euclidean run | numerals; 2^10 as a power on N (prp-omega-powers-parity (a)), computed; verify/ch03/exr-unique-factorization-b3.py
exr-unique-factorization-b3 (solution): d >= 4 gives d * d >= 16, d >= 6 gives d * d >= 36 | prp-ordered-ring-rules (c), numerals; verify/ch03/exr-unique-factorization-b3.py
exr-unique-factorization-c2 (solution): 4 | 4, 4 does not divide 2; 4 | 12, 6 | 12, 24 does not divide 12 | prp-divisibility-rules-integers (e) (cited); verify/ch03/exr-unique-factorization-c2.py
exr-unique-factorization-c3 (solution): 2*3*5*7 + 1 = 211 prime; 2*3*5*7*11*13 + 1 = 30031 = 59 * 509 | numerals; primality of 211 and 59 stated as illustration, nothing depends on it; verify/ch03/exr-unique-factorization-c3.py
-->
