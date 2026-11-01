# Finite Sums

*Sets and Functions*, Chapter 3 defined \( \sum \), \( \prod \) and powers of real numbers by recursion. It proved three formulas with them:

- the sum of the first \( n \) natural numbers (@fd2:prp-sum-first-n);
- the geometric sum (@fd2:prp-geometric-sum);
- Bernoulli's inequality (@fd2:thm-bernoulli).

Analysis rearranges such sums on every page. The algebra chapters of this volume need the same sums with terms in \( \nZ/n\nZ \), in a field, in \( \nC \) and among polynomials. This section states the rules once, for any commutative ring. It also teaches the one computational method that turns a sum into two terms: telescoping.

## Sums and powers in any commutative ring

The recursions for sums and products (@fd2:def-sum-product) and for powers use only a \( 0 \), a \( 1 \), an addition and a multiplication. So they run unchanged in any commutative ring \( R \), as defined in *Number Systems* (@fd3:def-commutative-ring-and-field). We index from \( 0 \). For \( a_0, a_1, a_2, \dots \in R \) the empty sum \( \sum_{k=0}^{-1} a_k \) is \( 0 \), and
\[
\sum_{k=0}^{n} a_k \coloneqq \sum_{k=0}^{n-1} a_k + a_n \quad \text{for every } n \in \nN ,
\]
so the recursion appends the last term; we also write \( a_0 + a_1 + \dots + a_n \). Products \( \prod_{k=0}^{n} a_k \) are defined in the same way, with the empty product \( 1 \). Sums and products between other bounds, \( \sum_{k=m}^{n} a_k \) for integers \( m \le n + 1 \), are defined by shifting the index. *Sets and Functions* made three remarks after defining sums, and they hold in \( R \) with the same proofs:

- a sum may be taken over a finite list \( a_0, \dots, a_n \) (the finite-lists remark);
- the index may be shifted;
- the last term may be split off.

**Powers.** Let \( R \) be a commutative ring and \( z \in R \). The **powers** \( z^n \), for \( n \in \nN \), are defined by the recursion
\[
z^0 \coloneqq 1 , \qquad z^{n+1} \coloneqq z^n z \quad \text{for every } n \in \nN .
\]
This is the recursion of *Sets and Functions*, Section 3.3 (@fd2:def-power), stated there for real numbers. The recursion theorem of that volume runs it just as well with values in \( R \). In particular \( z^1 = 1 \cdot z = z \) and \( z^2 = z^1 z = zz \). This matches the \( z^2 \) of @fd3:prp-ring-algebra (d).

For example, \( z^2 z^3 = (zz)(zzz) = z^5 \), and \( (z^2)^3 = z^2 z^2 z^2 = z^6 \). The next proposition proves such laws for all exponents.

::: {#prp-power-laws-commutative-ring}
[Laws of Powers in a Commutative Ring]

Let \( R \) be a commutative ring (@fd3:def-commutative-ring-and-field), let \( z, w \in R \), and let \( m, n \in \nN \).

::: {.enumerate options="label=(\alph*)"}
1. \( z^{m+n} = z^m z^n \).
2. \( (z^m)^n = z^{mn} \).
3. \( (zw)^n = z^n w^n \).
4. If \( R \) is a field and \( z \ne 0 \), then \( z^n \ne 0 \).
:::
:::

::: {.idea}
The definition of \( z^n \) is a recursion on \( n \), so every law is proved by induction on \( n \), peeling off the last factor with \( z^{n+1} = z^n z \). Each inductive step rests on one ingredient:

- for (a), associativity of multiplication, (F5);
- for (b), the law (a);
- for (c), associativity and commutativity of multiplication, (F5), (F6);
- for (d), the fact that a field has no zero divisors.
:::

::: {.proof}
Each part is proved by induction on \( n \), with \( z \), \( w \) and \( m \) fixed.

(a) For \( n = 0 \): \( z^{m+0} = z^m = z^m \cdot 1 = z^m z^0 \). If \( z^{m+n} = z^m z^n \), then
\[
z^{m+(n+1)} = z^{(m+n)+1} = z^{m+n} z = (z^m z^n) z = z^m (z^n z) = z^m z^{n+1} ,
\]
by the recursion, the hypothesis and associativity of multiplication.

(b) For \( n = 0 \): \( (z^m)^0 = 1 = z^0 = z^{m \cdot 0} \). If \( (z^m)^n = z^{mn} \), then \( (z^m)^{n+1} = (z^m)^n z^m = z^{mn} z^m = z^{mn + m} = z^{m(n+1)} \), by the recursion, the hypothesis and (a).

(c) For \( n = 0 \): \( (zw)^0 = 1 = 1 \cdot 1 = z^0 w^0 \). If \( (zw)^n = z^n w^n \), then
\[
(zw)^{n+1} = (zw)^n (zw) = (z^n w^n)(zw) = (z^n z)(w^n w) = z^{n+1} w^{n+1} ,
\]
where the third equality regroups and reorders the four factors.

(d) Let \( R \) be a field and \( z \ne 0 \). For \( n = 0 \): \( z^0 = 1 \ne 0 \), by the definition of a field. If \( z^n \ne 0 \), then \( z^{n+1} = z^n z \) is a product of two non-zero elements. So it is non-zero, since a field has no zero divisors (@fd3:lem-field-fraction-rules (d)).

::: {.uses}
@fd1:ax-induction (induction on n); @fd3:cor-omega-identification (b) (induction on this ℕ); @fd3:def-commutative-ring-and-field (F5)–(F7), rules of multiplication.
:::
:::

For \( R = \nR \) these are @fd2:prp-power-laws (a)–(c). The proofs are the same inductions and use only the ring axioms.

**Natural multiples.** The binomial theorem of Section 1.2 has coefficients that are natural numbers acting on ring elements. So we need the rules for such multiples. *Number Systems: From \(\nN\) to \(\nR\)*, Section 2.4 defines, just before @fd3:prp-ordered-ring-rules, for \( a \in R \), the multiples \( n \cdot a \) by the recursion \( 0 \cdot a \coloneqq 0 \), \( (n + 1) \cdot a \coloneqq n \cdot a + a \). So \( n \cdot a \) is the sum of \( n \) copies of \( a \). A dot with a natural number on its left always means this multiple.

For example, \( 2 \cdot a + 3 \cdot a = (a + a) + (a + a + a) = 5 \cdot a \), and \( 2 \cdot (3 \cdot a) = 6 \cdot a \). The next lemma lists the rules in general.

::: {#lem-natural-multiples}
[Natural Multiples in a Commutative Ring]

Let \( R \) be a commutative ring, \( a, b \in R \) and \( m, k \in \nN \).

::: {.enumerate options="label=(\alph*)"}
1. \( (m + k) \cdot a = m \cdot a + k \cdot a \).
2. \( m \cdot (a + b) = m \cdot a + m \cdot b \).
3. \( (m \cdot a) b = m \cdot (ab) \).
4. \( (mk) \cdot a = m \cdot (k \cdot a) \).
5. \( m \cdot a = (m \cdot 1) a \).
:::
:::

Part (a) is @fd3:prp-ordered-ring-rules (h), whose proof uses no order. Each of (b)–(d) is one induction on the recursion for \( m \cdot a \), and (e) is (c) with \( a = 1 \).

::: {.second-reading title="The inductions for natural multiples"}
::: {.proof}
All inductions are on \( m \in \nN \). Part (a) is @fd3:prp-ordered-ring-rules (h).

(b) Induction on \( m \). For \( m = 0 \) both sides are \( 0 \), since \( 0 + 0 = 0 \). If it holds for \( m \), then \( (m + 1) \cdot (a + b) = (m \cdot a + m \cdot b) + (a + b) = (m \cdot a + a) + (m \cdot b + b) \), by commutativity and associativity of addition. This is \( (m + 1) \cdot a + (m + 1) \cdot b \).

(c) Induction on \( m \). For \( m = 0 \), \( (0 \cdot a) b = 0 b = 0 = 0 \cdot (ab) \), by @fd3:prp-ring-algebra (b) and commutativity of multiplication. If it holds for \( m \), then \( ((m + 1) \cdot a) b = (m \cdot a + a) b = (m \cdot a) b + ab = m \cdot (ab) + ab = (m + 1) \cdot (ab) \). The second step is the distributive law with commutativity, and the third is the induction hypothesis.

(d) Induction on \( m \). For \( m = 0 \) both sides are \( 0 \). If it holds for \( m \), then, since \( (m + 1)k = mk + k \) in \( \nN \),
\[
((m + 1)k) \cdot a = (mk + k) \cdot a = (mk) \cdot a + k \cdot a = m \cdot (k \cdot a) + k \cdot a = (m + 1) \cdot (k \cdot a) ,
\]
by (a), the induction hypothesis and the recursion.

(e) By (c) with \( 1 \) in place of \( a \) and \( a \) in place of \( b \), \( (m \cdot 1) a = m \cdot (1 a) = m \cdot a \), since \( 1 a = a 1 = a \). This proves the lemma.

::: {.uses}
@fd1:ax-induction (induction on m); @fd3:cor-omega-identification (b) (induction on this ℕ); @fd3:def-commutative-ring-and-field (F1)–(F3), (F6), (F7), (F9), ring rules.
:::
:::
:::

In \( \nR \) the dot can be dropped. By (e), \( n \cdot a = (n \cdot 1) a \), and \( n \cdot 1 \) is the real number \( n \) (@fd3:def-naturals-in-ordered-field). So \( n \cdot a = na \), and from here on, in \( \nR \) we write \( na \).

For two terms, the rules for rearranging a sum are familiar: \( (a_0 + b_0) + (a_1 + b_1) = (a_0 + a_1) + (b_0 + b_1) \) and \( c(a_0 + a_1) = ca_0 + ca_1 \). The next lemma proves such rules for any number of terms.

::: {#lem-ring-finite-sums}
[Finite Sums in a Commutative Ring]

Let \( R \) be a commutative ring, \( n \in \nN \), \( c \in R \), and let \( (a_k)_{k \in \nN} \) and \( (b_k)_{k \in \nN} \) be sequences in \( R \).

::: {.enumerate options="label=(\alph*)"}
1. \( \sum_{k=0}^{n} (a_k + b_k) = \sum_{k=0}^{n} a_k + \sum_{k=0}^{n} b_k \).
2. \( c \sum_{k=0}^{n} a_k = \sum_{k=0}^{n} c\, a_k \).
3. \( \sum_{k=0}^{n} m \cdot a_k = m \cdot \sum_{k=0}^{n} a_k \) for every \( m \in \nN \).
4. Let \( j \in \nN \), and suppose \( a_k = 0 \) for every \( k \ne j \). Then \( \sum_{k=0}^{n} a_k = a_j \) if \( j \le n \), and \( \sum_{k=0}^{n} a_k = 0 \) if \( j > n \).
5. \( -\sum_{k=0}^{n} a_k = \sum_{k=0}^{n} (-a_k) \).
6. *(Splitting off the first term.)* \( \sum_{k=0}^{n+1} a_k = a_0 + \sum_{k=0}^{n} a_{k+1} \).
:::
:::

In words: a finite sum may be split, multiplied and negated termwise. A sum with one non-zero term is that term. The first term may be split off, and the rest re-indexed from \( 0 \). By the finite-lists remark, the lemma applies to finitely many terms \( a_0, \dots, a_n \) as well.

::: {.idea}
A sum up to \( n + 1 \) is the sum up to \( n \) plus one term. So a rule that holds for one term, and survives adding one more term, holds for all sums. Each such proof is an induction on \( n \) whose step needs only the rules listed below:

- for (a), commutativity and associativity of addition, (F1), (F2);
- for (b), the distributive law, (F9);
- for (f), associativity of addition.

Part (c) is (b) in disguise, since \( m \cdot a = (m \cdot 1)a \) (@lem-natural-multiples (e)). Part (e) is an induction whose step is the uniqueness of negatives.
:::

::: {.second-reading title="Proof of the sum rules"}
::: {.proof}
Each part is an induction on \( n \), splitting off the last term at the step, except (c), which follows from (b).

(a) For \( n = 0 \) both sides are \( a_0 + b_0 \). If (a) holds for \( n \), then splitting off the last term,
\[
\sum_{k=0}^{n+1} (a_k + b_k) = \Bigl( \sum_{k=0}^{n} a_k + \sum_{k=0}^{n} b_k \Bigr) + (a_{n+1} + b_{n+1}) .
\]
By commutativity and associativity of addition, this is \( \bigl( \sum_{k=0}^{n} a_k + a_{n+1} \bigr) + \bigl( \sum_{k=0}^{n} b_k + b_{n+1} \bigr) \), and that is the right side for \( n + 1 \).

(b) For \( n = 0 \) both sides are \( c a_0 \). At the step, \( c \bigl( \sum_{k=0}^{n} a_k + a_{n+1} \bigr) = c \sum_{k=0}^{n} a_k + c a_{n+1} \) by the distributive law. The induction hypothesis rewrites the first term.

(c) By @lem-natural-multiples (e), \( m \cdot a_k = (m \cdot 1) a_k \) for every \( k \) and \( m \cdot \sum_{k=0}^{n} a_k = (m \cdot 1) \sum_{k=0}^{n} a_k \). So (c) is (b) with \( c = m \cdot 1 \).

(d) For \( n = 0 \): if \( j = 0 \) the sum is \( a_0 = a_j \); if \( j > 0 \), then \( 0 \ne j \), so the sum is \( a_0 = 0 \). Suppose (d) holds for \( n \), and split off \( a_{n+1} \). If \( j \le n \), the sum up to \( n \) is \( a_j \) and \( a_{n+1} = 0 \) (as \( n + 1 \ne j \)), so the total is \( a_j \). If \( j = n + 1 \), the sum up to \( n \) is \( 0 \) (as \( j > n \)) and the total is \( 0 + a_{n+1} = a_j \). If \( j > n + 1 \), both parts are \( 0 \).

(e) For \( n = 0 \) both sides are \( -a_0 \). Suppose (e) holds for \( n \), and write \( s \coloneqq \sum_{k=0}^{n} a_k \). By the four rules of addition, \( (s + a_{n+1}) + \bigl((-s) + (-a_{n+1})\bigr) = (s + (-s)) + (a_{n+1} + (-a_{n+1})) = 0 \). So \( -(s + a_{n+1}) = (-s) + (-a_{n+1}) \) by the uniqueness of negatives (@fd3:prp-ring-algebra (a)). By the induction hypothesis \( -s = \sum_{k=0}^{n} (-a_k) \), and splitting off the last term gives \( -\sum_{k=0}^{n+1} a_k = \sum_{k=0}^{n+1} (-a_k) \).

(f) For \( n = 0 \) both sides are \( a_0 + a_1 \). If (f) holds for \( n \), then
\[
\sum_{k=0}^{n+2} a_k = \Bigl( a_0 + \sum_{k=0}^{n} a_{k+1} \Bigr) + a_{n+2} = a_0 + \sum_{k=0}^{n+1} a_{k+1} .
\]
The first step splits off the last term and uses the induction hypothesis. The second uses associativity of addition, and splits off the last term of the sequence \( (a_{k+1})_k \), whose term at \( k = n + 1 \) is \( a_{n+2} \). This proves the lemma.

::: {.uses}
@fd1:ax-induction (induction on n); @fd3:def-commutative-ring-and-field (F1)–(F4), (F9), ring rules.
:::
:::
:::

::: {.check}
In \( \nR \), compute \( \sum_{k=0}^{3} (2k - 1) \), \( \sum_{k=4}^{3} k^2 \) and \( \prod_{k=1}^{0} 7 \).
:::

::: {.solution}
\( \sum_{k=0}^{3} (2k - 1) = -1 + 1 + 3 + 5 = 8 \). The second sum has upper bound below its lower bound, so it is the empty sum, \( 0 \). The product is the empty product, \( 1 \).
:::

## Reindexing and comparing

Two more tools are used constantly: reading a sum backwards, and cutting it in two. Both are bookkeeping, and both are proved once here. For three terms they say
\[
a_0 + a_1 + a_2 = a_2 + a_1 + a_0 \qquad \text{and} \qquad a_0 + a_1 + a_2 = a_0 + (a_1 + a_2) .
\]

::: {#prp-sum-reindex}
[Reindexing a Finite Sum]

Let \( R \) be a commutative ring, \( n \in \nN \) and \( a_0, \dots, a_n \in R \).

::: {.enumerate options="label=(\alph*)"}
1. *(Reversal.)* \( \sum_{k=0}^{n} a_k = \sum_{k=0}^{n} a_{n-k} \).
2. *(Splitting.)* For every integer \( m \) with \( -1 \le m \le n \),
\[
\sum_{k=0}^{n} a_k = \sum_{k=0}^{m} a_k + \sum_{k=m+1}^{n} a_k .
\]
:::
:::

::: {.idea}
For (b), fix \( m \) and induct on \( n \ge m \): each step splits off the last term of the whole sum and of the second piece at once. For (a), induct on \( n \) **for all lists at once**. Split off the last term of the reversed sum, which is \( a_0 \), and apply the hypothesis to the shorter list \( a_1, \dots, a_{n+1} \). Then @lem-ring-finite-sums (f) puts \( a_0 \) back at the front.
:::

::: {.second-reading title="Proof of the reindexing rules"}
::: {.proof}
By the finite-lists remark we may extend the list to a sequence \( (a_k)_{k \in \nN} \).

(b) If \( m = -1 \), the first sum on the right is empty, and (b) reads \( \sum_{k=0}^{n} a_k = 0 + \sum_{k=0}^{n} a_k \), which is true. Let \( m \ge 0 \). We prove (b) for every integer \( n \ge m \) by induction with base \( m \) (@fd2:thm-induction). For \( n = m \) the second sum is \( \sum_{k=m+1}^{m} a_k = 0 \), the empty sum, and (b) holds. Suppose (b) holds for \( n \). We split off the last term of the left side and of \( \sum_{k=m+1}^{n+1} a_k \), which is allowed since \( m + 1 \le n + 1 \). By the induction hypothesis and associativity of addition,
\[
\begin{aligned}
\sum_{k=0}^{n+1} a_k &= \Bigl( \sum_{k=0}^{m} a_k + \sum_{k=m+1}^{n} a_k \Bigr) + a_{n+1} \\
&= \sum_{k=0}^{m} a_k + \sum_{k=m+1}^{n+1} a_k .
\end{aligned}
\]

(a) Induction on \( n \), with the statement "for every list \( a_0, \dots, a_n \) in \( R \), \( \sum_{k=0}^{n} a_k = \sum_{k=0}^{n} a_{n-k} \)". For \( n = 0 \) both sides are \( a_0 \). Suppose the statement holds for \( n \), and let \( a_0, \dots, a_{n+1} \in R \). Splitting off the last term, whose index is \( (n + 1) - (n + 1) = 0 \),
\[
\sum_{k=0}^{n+1} a_{n+1-k} = \sum_{k=0}^{n} a_{n+1-k} + a_0 .
\]
Let \( c_j \coloneqq a_{j+1} \) for \( 0 \le j \le n \). Then \( a_{n+1-k} = c_{n-k} \) for \( 0 \le k \le n \). The hypothesis, applied to the list \( c_0, \dots, c_n \), gives \( \sum_{k=0}^{n} c_{n-k} = \sum_{k=0}^{n} c_k = \sum_{k=0}^{n} a_{k+1} \). So, by commutativity of addition and @lem-ring-finite-sums (f),
\[
\sum_{k=0}^{n+1} a_{n+1-k} = a_0 + \sum_{k=0}^{n} a_{k+1} = \sum_{k=0}^{n+1} a_k .
\]
This proves the proposition.

::: {.uses}
@fd1:ax-induction (induction on n); @fd3:def-commutative-ring-and-field (F1)–(F3), rules of addition.
:::
:::
:::

::: {.check}
Split \( \sum_{k=0}^{5} a_k \) by (b) at \( m = 2 \) and at \( m = -1 \). What are the pieces?
:::

::: {.solution}
At \( m = 2 \): \( (a_0 + a_1 + a_2) + (a_3 + a_4 + a_5) \). At \( m = -1 \): the empty sum \( 0 \), plus the whole sum \( \sum_{k=0}^{5} a_k \).
:::

Reversal gives the oldest trick for sums.

::: {#exm-odd-sum-reversal}
[Odd numbers by reversal]

Show that \( \sum_{k=0}^{n} (2k + 1) = (n + 1)^2 \) for every \( n \in \nN \).
:::

::: {.solution}
Call the sum \( S \). By reversal (@prp-sum-reindex (a)), \( S = \sum_{k=0}^{n} \bigl( 2(n - k) + 1 \bigr) \). Adding the two expressions termwise (@lem-ring-finite-sums (a)),
\[
2S = \sum_{k=0}^{n} \bigl( (2k + 1) + (2(n - k) + 1) \bigr) = \sum_{k=0}^{n} (2n + 2) .
\]
A constant \( c \) summed over \( n + 1 \) indices gives \( (n + 1) \cdot c \). Indeed, for \( n = 0 \) the sum is \( c = 1 \cdot c \). If \( \sum_{k=0}^{n} c = (n + 1) \cdot c \), then \( \sum_{k=0}^{n+1} c = (n + 1) \cdot c + c = (n + 2) \cdot c \) by the recursion for multiples. In \( \nR \) this is \( (n + 1)c \). So \( 2S = (n + 1)(2n + 2) = 2(n + 1)^2 \), and \( S = (n + 1)^2 \). For \( n = 2 \): \( 1 + 3 + 5 = 9 = 3^2 \).

Reversal pairs the first term with the last, the second with the second-to-last, and each pair has the same sum \( 2n + 2 \).
:::

In an ordered field, sums can also be compared. For example, from \( 1 \le 2 \) and \( 3 \le 5 \) we get \( 1 + 3 \le 2 + 5 \); and \( \abs{2 + (-3)} = 1 \le 5 = \abs{2} + \abs{-3} \). The next proposition collects the comparisons that estimates use.

::: {#prp-sum-order}
[Comparing Sums Termwise]

Let \( F \) be an ordered field, \( n \in \nN \) and \( a_k, b_k \in F \) for \( 0 \le k \le n \). All sums run over \( 0 \le k \le n \) unless bounds are shown.

::: {.enumerate options="label=(\alph*)"}
1. If \( a_k \le b_k \) for every \( k \), then \( \sum a_k \le \sum b_k \); if moreover \( a_j < b_j \) for some \( j \), the inequality is strict.
2. If \( a_k \ge 0 \) for every \( k \), then \( \sum_{k=0}^{n} a_k \ge \sum_{k=0}^{m} a_k \) for every integer \( m \) with \( -1 \le m \le n \), and \( \sum_{k=0}^{n} a_k \ge a_j \) for every \( j \le n \).
3. If \( a_k \le M \) for every \( k \), then \( \sum_{k=0}^{n} a_k \le (n + 1) \cdot M \).
4. *(Triangle inequality for sums.)* \( \abs{\sum_{k=0}^{n} a_k} \le \sum_{k=0}^{n} \abs{a_k} \).
5. If \( a_k \ge 0 \) for every \( k \) and \( \sum_{k=0}^{n} a_k = 0 \), then \( a_k = 0 \) for every \( k \).
:::
:::

::: {.idea}
Every part adds inequalities one term at a time. Parts (a) and (d) are inductions whose step adds one inequality (@fd3:prp-ordered-ring-rules (b)). Part (b) splits the sum by @prp-sum-reindex (b) and compares the tail with a list of zeros by (a). Parts (c) and (e) are (a) and (b) applied to special data.
:::

::: {.proof}
By the finite-lists remark we may extend the lists to sequences; in (a), extend with \( a_k \coloneqq b_k \coloneqq 0 \) for \( k > n \), so that the hypotheses still hold, and in (d) extend with \( a_k \coloneqq 0 \). Then the inductions below run over all \( n \).

(a) Induction on \( n \), proving \( \sum_{k=0}^{n} a_k \le \sum_{k=0}^{n} b_k \), strictly if \( a_j < b_j \) for some \( j \le n \). For \( n = 0 \) this is the hypothesis on \( a_0, b_0 \). At the step, \( \sum_{k=0}^{n+1} a_k = \sum_{k=0}^{n} a_k + a_{n+1} \le \sum_{k=0}^{n} b_k + b_{n+1} \) by adding the two inequalities. The conclusion is strict if either inequality added is strict: the first when \( j \le n \), by the hypothesis, the second when \( j = n + 1 \).

(b) By @prp-sum-reindex (b), \( \sum_{k=0}^{n} a_k = \sum_{k=0}^{m} a_k + \sum_{k=m+1}^{n} a_k \). The tail is \( 0 \) if \( m = n \). Otherwise, shifted to start at \( 0 \), it is \( \ge \) the sum of zeros by (a), and that sum is \( 0 \) (@lem-ring-finite-sums (d)). Adding the tail to \( \sum_{k=0}^{m} a_k \) gives the first claim. For the single term, split around \( j \) twice. By the first claim with \( m = j \), \( \sum_{k=0}^{n} a_k \ge \sum_{k=0}^{j} a_k = \sum_{k=0}^{j-1} a_k + a_j \). Also \( \sum_{k=0}^{j-1} a_k \ge 0 \): for \( j = 0 \) it is the empty sum, and for \( j \ge 1 \) it is the first claim with \( j - 1 \) in place of \( n \) and \( m = -1 \). So the total is \( \ge 0 + a_j = a_j \).

(c) This is (a) with \( b_k \coloneqq M \), since \( \sum_{k=0}^{n} M = (n + 1) \cdot M \) by the constant sum computed in @exm-odd-sum-reversal.

(d) Induction on \( n \). For \( n = 0 \) both sides are \( \abs{a_0} \). At the step,
\[
\Bigl| \sum_{k=0}^{n} a_k + a_{n+1} \Bigr| \le \Bigl| \sum_{k=0}^{n} a_k \Bigr| + \abs{a_{n+1}} \le \sum_{k=0}^{n} \abs{a_k} + \abs{a_{n+1}} ,
\]
by the triangle inequality (@fd3:prp-absolute-value-ordered-field (e)), then the induction hypothesis and adding inequalities.

(e) For each \( j \le n \), \( 0 \le a_j \le \sum_{k=0}^{n} a_k = 0 \) by (b), so \( a_j = 0 \) by antisymmetry (@fd3:prp-ordered-ring-rules (i)).

::: {.uses}
@fd1:ax-induction (induction on n); @fd3:prp-ordered-ring-rules (b) (adding inequalities).
:::
:::

Part (b) is the estimate *drop non-negative terms*, which Section 1.2 uses to keep a few terms of a binomial expansion; part (c) *replaces each term by the largest*. For real terms a largest term exists by @fd2:prp-finite-max (the same induction works in any ordered field), which supplies an \( M \) for (c).

::: {.warning}
A sum of products is not a product of sums, and a sum of reciprocals is not the reciprocal of the sum. With \( n = 1 \) and \( a_0 = a_1 = b_0 = b_1 = 1 \), \( \sum a_k b_k = 2 \) while \( \bigl(\sum a_k\bigr)\bigl(\sum b_k\bigr) = 4 \); and \( \frac11 + \frac11 = 2 \ne \frac12 \).
:::

What *is* true of products of sums is that they multiply out, every term with every term. With two terms in each factor,
\[
(x_0 + x_1)(y_0 + y_1) = (x_0 y_0 + x_0 y_1) + (x_1 y_0 + x_1 y_1) = (x_0 y_0 + x_1 y_0) + (x_0 y_1 + x_1 y_1) :
\]
the four products can be grouped by rows or by columns. The general form of that statement exchanges two sums.

::: {#prp-double-sum}
[Double Sums over a Rectangle]

Let \( R \) be a commutative ring, \( m, n \in \nN \) and \( a_{ij} \in R \) for \( 0 \le i \le m \), \( 0 \le j \le n \). Then
\[
\sum_{i=0}^{m} \sum_{j=0}^{n} a_{ij} = \sum_{j=0}^{n} \sum_{i=0}^{m} a_{ij} .
\]
In particular, for \( x_0, \dots, x_m, y_0, \dots, y_n \in R \),
\[
\Bigl( \sum_{i=0}^{m} x_i \Bigr) \Bigl( \sum_{j=0}^{n} y_j \Bigr) = \sum_{i=0}^{m} \sum_{j=0}^{n} x_i y_j .
\]
:::

::: {.idea}
Induct on the number of rows \( m \). Adding the row \( i = m + 1 \) adds one sum over \( j \) to the left side. On the right it adds, termwise, one entry to each inner sum, and @lem-ring-finite-sums (a) says these agree.
:::

::: {.second-reading title="Proof of the double-sum rule"}
::: {.proof}
Induction on \( m \). For \( m = 0 \), a sum over \( 0 \le i \le 0 \) is its one term, so both sides are \( \sum_{j=0}^{n} a_{0j} \). Suppose the rule holds for \( m \) and every array. Splitting off the last term, the induction hypothesis, and @lem-ring-finite-sums (a) give
\[
\begin{aligned}
\sum_{i=0}^{m+1} \sum_{j=0}^{n} a_{ij} &= \sum_{j=0}^{n} \sum_{i=0}^{m} a_{ij} + \sum_{j=0}^{n} a_{m+1,j} \\
&= \sum_{j=0}^{n} \Bigl( \sum_{i=0}^{m} a_{ij} + a_{m+1,j} \Bigr) = \sum_{j=0}^{n} \sum_{i=0}^{m+1} a_{ij} ,
\end{aligned}
\]
the last step splitting off the last term of each inner sum. For the product form, let \( Y \coloneqq \sum_{j=0}^{n} y_j \). By commutativity of multiplication and @lem-ring-finite-sums (b), \( \bigl( \sum_{i} x_i \bigr) Y = \sum_{i} Y x_i = \sum_{i} x_i Y \). By (b) again, \( x_i Y = \sum_{j} x_i y_j \) for each \( i \). This proves the proposition.

::: {.uses}
@fd3:def-commutative-ring-and-field (F6), commutativity of multiplication.
:::
:::
:::

The analysis volumes need the same exchange for infinite sums: *Integration, Series, and Function Spaces*, Chapter 5 studies double series, where the exchange can fail and needs a hypothesis. For finite sums nothing can go wrong.

## Telescoping

*Logic and Proof* met the sum
\[
S_n = \sum_{k=1}^{n} \frac{1}{k(k+1)} ,
\]
guessed \( S_n = \frac{n}{n+1} \) from the values \( \frac12, \frac23, \frac34 \), and proved the guess by induction (@fd1:exm-strengthen-the-claim). Induction confirms a value once someone has guessed it. We want a way to **find** the value instead, and this sum shows how.

::: {.idea}
[Scratch work]

We want a closed form for \( \sum_{k=1}^{n} \frac{1}{k(k+1)} \). A sum we can always evaluate is one where each term is a difference of consecutive values, \( a_k = b_k - b_{k+1} \): then neighbors cancel. The denominator is a product of two consecutive factors \( k \), \( k + 1 \), which suggests \( b_k = \frac1k \). Check:
\[
\frac1k - \frac1{k+1} = \frac{(k + 1) - k}{k(k + 1)} = \frac{1}{k(k + 1)} .
\]
Written out, the sum is \( \bigl(1 - \frac12\bigr) + \bigl(\frac12 - \frac13\bigr) + \dots + \bigl(\frac1n - \frac1{n+1}\bigr) \), and every inner fraction appears once with each sign.

| We know | We want |
|---|---|
| \( a_k = \frac{1}{k(k+1)} \) for \( 1 \le k \le n \) | a closed form for \( \sum_{k=1}^{n} a_k \) |
| \( a_k = \frac1k - \frac1{k+1} \) (by @fd3:lem-field-fraction-rules (c)) | \( \sum_{k=1}^{n} \bigl(\frac1k - \frac1{k+1}\bigr) \) |
| every \( \frac1{k+1} \) with \( k < n \) is cancelled by the next term | \( 1 - \frac1{n+1} \): needs a theorem that does the cancelling |

The dots in the written-out sum hide the cancelling. The next theorem proves that it works, once and for all sums of this shape.
:::

::: {#thm-telescoping}
[Telescoping Sums and Products]

Let \( R \) be a commutative ring, \( n \in \nN \) and \( b_0, \dots, b_{n+1} \in R \).

::: {.enumerate options="label=(\alph*)"}
1. \( \sum_{k=0}^{n} (b_{k+1} - b_k) = b_{n+1} - b_0 \).
2. If \( R \) is a field and every \( b_k \ne 0 \), then \( \prod_{k=0}^{n} \frac{b_{k+1}}{b_k} = \frac{b_{n+1}}{b_0} \).
:::
:::

::: {.proof}
By the finite-lists remark we may extend \( b_0, \dots, b_{n+1} \) to a sequence \( (b_k)_{k \in \nN} \); for (b) we extend with \( b_k \coloneqq 1 \) for \( k > n + 1 \), so that every \( b_k \ne 0 \).

(a) Induction on \( n \). For \( n = 0 \) the sum is its one term \( b_1 - b_0 \). If the sum up to \( n \) is \( b_{n+1} - b_0 \), then the sum up to \( n + 1 \) is \( (b_{n+1} - b_0) + (b_{n+2} - b_{n+1}) = b_{n+2} - b_0 \).

(b) The same induction with products. For \( n = 0 \) the product is \( \frac{b_1}{b_0} \). At the step, \( \frac{b_{n+1}}{b_0} \cdot \frac{b_{n+2}}{b_{n+1}} = b_{n+2} b_0^{-1} \bigl( b_{n+1} b_{n+1}^{-1} \bigr) = \frac{b_{n+2}}{b_0} \), since \( b_{n+1} b_{n+1}^{-1} = 1 \).

::: {.uses}
@fd1:ax-induction (induction on n); @fd3:def-commutative-ring-and-field (F1)–(F4) for sums, (F5)–(F8) for products.
:::
:::

::: {#exm-telescoping-reciprocals}
[A telescoping sum]

Find \( \sum_{k=1}^{n} \frac{1}{k(k+1)} \) for \( n \ge 1 \) with @thm-telescoping.
:::

::: {.solution}
Shift the index to start at \( 0 \), with \( j = k - 1 \): the sum is \( \sum_{j=0}^{n-1} \frac{1}{(j+1)(j+2)} \). Let \( b_j \coloneqq -\frac{1}{j+1} \). The computation above gives \( \frac{1}{(j+1)(j+2)} = \frac{1}{j+1} - \frac{1}{j+2} = b_{j+1} - b_j \). By @thm-telescoping (a) with \( n - 1 \) in place of \( n \), the sum is \( b_n - b_0 = 1 - \frac{1}{n+1} = \frac{n}{n+1} \).
:::

::: {#exm-method-telescoping}
[Method: telescoping]

**How it goes.** To find \( \sum a_k \), write \( a_k = b_{k+1} - b_k \), or \( b_k - b_{k+1} \), for a sequence \( b \) you choose. Then the sum is the last \( b \) minus the first (the first minus the last for \( b_k - b_{k+1} \)) (@thm-telescoping). To *verify* a guessed formula \( \sum_{k=0}^{n} a_k = F(n) \), check \( F(0) = a_0 \) and \( F(k) - F(k-1) = a_k \) for \( 1 \le k \le n \). Telescoping over \( 1 \le k \le n \) then gives \( \sum_{k=0}^{n} a_k = a_0 + F(n) - F(0) = F(n) \).

**When to use it.** Quotients whose denominator is a product of shifted factors; differences of powers or roots; any sum whose partial sums you can guess.

**Common mistakes.** A common mistake is to use a difference \( b_{k+2} - b_k \), which skips a step. Such a sum leaves **two** terms at each end, not one.
:::

The first use is an identity about powers that this volume needs again and again. For \( n = 2 \) it is the school identity \( z^2 - w^2 = (z - w)(w + z) \). The proof below is the method with \( b_k \coloneqq z^k w^{n-k} \).

::: {#lem-difference-of-powers}
[Difference of Powers]

Let \( R \) be a commutative ring, let \( z, w \in R \), and let \( n \in \nN \) with \( n \ge 1 \). Then
\[
z^n - w^n = (z - w) \sum_{k=0}^{n-1} z^k w^{n-1-k} .
\]
In particular \( z^n - 1 = (z - 1)(1 + z + z^2 + \dots + z^{n-1}) \).
:::

::: {.idea}
Multiply out: \( (z - w) \sum_{k=0}^{n-1} z^k w^{n-1-k} = \sum_{k=0}^{n-1} \bigl( z^{k+1} w^{n-1-k} - z^k w^{n-k} \bigr) \). Each term is a difference of consecutive values of \( z^k w^{n-k} \), so the sum telescopes, as in @exm-method-telescoping.
:::

::: {.proof}
Let \( b_k \coloneqq z^k w^{n-k} \) for \( 0 \le k \le n \). For \( 0 \le k \le n - 1 \), the distributive law and @fd3:prp-ring-algebra (c), with the factors regrouped, give
\[
(z - w) z^k w^{n-1-k} = (z z^k) w^{n-1-k} - z^k (w\, w^{n-1-k}) = b_{k+1} - b_k ,
\]
since \( z z^k = z^{k+1} \) and \( w\, w^{n-1-k} = w^{n-k} \) by the recursion for powers. By @lem-ring-finite-sums (b), the product \( (z - w) \sum_{k=0}^{n-1} z^k w^{n-1-k} \) is therefore \( \sum_{k=0}^{n-1} (b_{k+1} - b_k) \). Since \( n - 1 \in \nN \), @thm-telescoping (a) with \( n - 1 \) in place of \( n \) gives \( b_n - b_0 = z^n w^0 - z^0 w^n = z^n - w^n \). The particular case is \( w = 1 \), since \( 1^j = 1 \) for every \( j \in \nN \) (by induction, \( 1^0 = 1 \) and \( 1^{j+1} = 1^j \cdot 1 = 1 \)).

::: {.uses}
@fd1:ax-induction (induction on j); @fd3:def-commutative-ring-and-field (F5)–(F7), (F9), ring rules.
:::
:::

With \( z = r \) and \( w = 1 \) in \( \nR \), the lemma is @fd2:prp-geometric-sum multiplied out: \( r^n - 1 = (r - 1)(1 + r + \dots + r^{n-1}) \). Section 1.5 uses it to compare roots.

::: {#exm-telescoping-squares}
[The sum of the squares]

Find \( \sum_{k=1}^{n} k^2 \) for \( n \in \nN \).
:::

::: {.solution}
The squares are not differences of anything obvious. But they appear inside a difference of cubes: expanding, \( (k + 1)^3 - k^3 = 3k^2 + 3k + 1 \). Sum this over \( 1 \le k \le n \). On the left, take \( b_j \coloneqq (j + 1)^3 \) and shift the index to \( j = k - 1 \). Then @thm-telescoping (a) gives \( b_n - b_0 = (n + 1)^3 - 1 \); for \( n = 0 \) both sides below are \( 0 \). On the right, split the sum termwise and take out the constants (@lem-ring-finite-sums (a), (b)). The constant sum \( \sum_{k=1}^{n} 1 \) is \( n \), as in @exm-odd-sum-reversal. The sum \( \sum_{k=1}^{n} k \) is \( \frac{n(n+1)}{2} \) by @fd2:prp-sum-first-n. So
\[
(n + 1)^3 - 1 = 3 \sum_{k=1}^{n} k^2 + \frac{3n(n + 1)}{2} + n .
\]
Solve for the sum:
\[
\begin{aligned}
3 \sum_{k=1}^{n} k^2 &= (n + 1)^3 - (n + 1) - \frac{3n(n + 1)}{2} \\
&= (n + 1)\Bigl( n^2 + 2n - \frac{3n}{2} \Bigr) = \frac{n(n + 1)(2n + 1)}{2} .
\end{aligned}
\]
So \( \sum_{k=1}^{n} k^2 = \frac{n(n + 1)(2n + 1)}{6} \). Check at \( n = 3 \): \( 1 + 4 + 9 = 14 = \frac{3 \cdot 4 \cdot 7}{6} \).
:::

::: {.second-reading title="When the cancellation skips"}
Change \( b_{k+1} - b_k \) to \( b_{k+2} - b_k \). Each term still is a difference of two values of \( b \), but the cancellation now skips a step. Write \( b_{k+2} - b_k = (b_{k+2} - b_{k+1}) + (b_{k+1} - b_k) \). By @lem-ring-finite-sums (a), the sum splits into two telescoping sums, one for the sequence \( c_k \coloneqq b_{k+1} \):
\[
\sum_{k=0}^{n} (b_{k+2} - b_k) = (b_{n+2} - b_1) + (b_{n+1} - b_0) .
\]
Two terms survive at each end. For \( b_k = \frac{1}{k+1} \) and \( n = 1 \), the sum is \( \bigl(\frac13 - 1\bigr) + \bigl(\frac14 - \frac12\bigr) = -\frac{11}{12} \), which is \( b_3 + b_2 - b_1 - b_0 \) and not \( b_3 - b_0 = -\frac34 \).
:::

::: {.check}
Which \( b_k \) makes \( a_k = \frac{1}{(2k-1)(2k+1)} \) telescope, as \( a_k = b_{k+1} - b_k \)?
:::

::: {.solution}
The factors \( 2k - 1 \) and \( 2k + 1 \) differ by \( 2 \), so \( \frac{1}{2k-1} - \frac{1}{2k+1} = \frac{2}{(2k-1)(2k+1)} \), and \( a_k = \frac12\bigl(\frac{1}{2k-1} - \frac{1}{2k+1}\bigr) \). So \( b_k \coloneqq -\frac{1}{2(2k-1)} \) gives \( b_{k+1} - b_k = -\frac{1}{2(2k+1)} + \frac{1}{2(2k-1)} = a_k \).
:::

**Telescoping products.** *Sets and Functions*, Section 3.3 computed \( \prod_{k=1}^{n} \frac{k+1}{k} = n + 1 \). This is @thm-telescoping (b) with \( b_k \coloneqq k + 1 \), with the index shifted to run from \( 0 \) to \( n - 1 \). Products that do not telescope at once may split into two that do. For every \( k \ne 0 \), \( 1 - \frac{1}{k^2} = \frac{k-1}{k} \cdot \frac{k+1}{k} \), and a product of products splits as a sum of sums does. So, for \( n \ge 2 \),
\[
\prod_{k=2}^{n} \Bigl( 1 - \frac{1}{k^2} \Bigr) = \prod_{k=2}^{n} \frac{k-1}{k} \cdot \prod_{k=2}^{n} \frac{k+1}{k} = \frac1n \cdot \frac{n+1}{2} = \frac{n+1}{2n} .
\]
For \( n = 3 \): \( \frac34 \cdot \frac89 = \frac23 = \frac{4}{6} \).

::: {.remark}
[Looking ahead]

Chapter 4 uses these sums with terms in a field, and Chapter 9 proves the Cauchy–Schwarz inequality with them.
:::

## Exercises

### A. Check your understanding

:::: {#exr-finite-sums-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \sum_{k=5}^{4} k \) and \( \prod_{k=1}^{3} (k + 1) \).
2. True or false, with a reason: \( \sum_{k=0}^{n} a_k b_k = \bigl(\sum_{k=0}^{n} a_k\bigr)\bigl(\sum_{k=0}^{n} b_k\bigr) \) for all \( n \in \nN \) and all reals \( a_k, b_k \).
3. Rewrite \( \sum_{k=2}^{6} k^2 \) with the index starting at \( 0 \).
4. Which \( b_k \) makes \( a_k = 2k + 1 \) a telescoping difference \( b_{k+1} - b_k \)?
:::
::::

::: {.solution}
(a) \( \sum_{k=5}^{4} k = 0 \), the empty sum; \( \prod_{k=1}^{3} (k + 1) = 2 \cdot 3 \cdot 4 = 24 \).

(b) False. With \( n = 1 \) and every term \( 1 \), the left side is \( 2 \) and the right side \( 4 \).

(c) Shift by \( 2 \), with \( j = k - 2 \): \( \sum_{j=0}^{4} (j + 2)^2 \).

(d) \( b_k = k^2 \), since \( (k + 1)^2 - k^2 = 2k + 1 \).
:::

### B. Practice

::: {#exr-finite-sums-b1}
[B1: Telescoping computations]

Find, for \( n \ge 1 \), (a) \( \sum_{k=1}^{n} \frac{1}{(2k-1)(2k+1)} \); (b) \( \sum_{k=1}^{n} k \cdot k! \).
:::

::: {.solution}
(a) Since \( \frac{1}{2k-1} - \frac{1}{2k+1} = \frac{2}{(2k-1)(2k+1)} \), each term is \( a_k = b_{k+1} - b_k \) with \( b_k = -\frac{1}{2(2k-1)} \). Shifting to start at \( 0 \) and applying @thm-telescoping (a) with \( n - 1 \) in place of \( n \), the sum is
\[
b_{n+1} - b_1 = -\frac{1}{2(2n+1)} + \frac12 = \frac12 \Bigl( 1 - \frac{1}{2n+1} \Bigr) = \frac{n}{2n+1} .
\]
(b) Since \( (k + 1)! = k!\,(k + 1) = k \cdot k! + k! \), each term is \( k \cdot k! = (k + 1)! - k! \), a difference of consecutive values of \( b_k \coloneqq k! \). By @thm-telescoping (a), after the same shift, the sum is \( b_{n+1} - b_1 = (n + 1)! - 1 \). Check at \( n = 2 \): \( 1 + 4 = 5 = 6 - 1 \).
:::

:::: {#exr-finite-sums-b2}
[B2: Prove or disprove]

Prove or disprove, for all \( n \ge 1 \) and all reals \( a_k \), \( b_k \):

::: {.enumerate options="label=(\alph*)"}
1. \( \sum_{k=1}^{n} (a_k + 1) = \sum_{k=1}^{n} a_k + n \).
2. \( \bigl(\sum_{k=1}^{n} a_k\bigr)^2 = \sum_{k=1}^{n} a_k^2 \).
3. \( \sum_{k=0}^{n} a_{n-k} b_k = \sum_{k=0}^{n} a_k b_{n-k} \).
4. \( \sum_{k=1}^{n} \frac{1}{k(k+2)} = \frac12 \bigl(1 - \frac{1}{n+2}\bigr) \).
:::
::::

::: {.solution}
(a) True. By @lem-ring-finite-sums (a), the left side is \( \sum_{k=1}^{n} a_k + \sum_{k=1}^{n} 1 \). A constant \( 1 \) summed over \( n \) indices is \( n \cdot 1 = n \), as in @exm-odd-sum-reversal.

(b) False. With \( n = 2 \) and \( a_1 = a_2 = 1 \): \( (1 + 1)^2 = 4 \), but \( 1 + 1 = 2 \).

(c) True. Let \( c_k \coloneqq a_k b_{n-k} \) for \( 0 \le k \le n \). By reversal (@prp-sum-reindex (a)), \( \sum_{k=0}^{n} c_k = \sum_{k=0}^{n} c_{n-k} \), and \( c_{n-k} = a_{n-k} b_{n-(n-k)} = a_{n-k} b_k \).

(d) False, although it holds at \( n = 1 \), where both sides are \( \frac13 \). At \( n = 2 \) the left side is \( \frac13 + \frac18 = \frac{11}{24} \) and the right side is \( \frac12 \cdot \frac34 = \frac38 = \frac{9}{24} \). The correct value comes from a telescope that skips: \( \frac{1}{k(k+2)} = \frac12 \bigl( \frac1k - \frac{1}{k+2} \bigr) \), so two terms survive at each end, and
\[
\sum_{k=1}^{n} \frac{1}{k(k+2)} = \frac12 \Bigl( \frac32 - \frac{1}{n+1} - \frac{1}{n+2} \Bigr) .
\]
At \( n = 2 \) this is \( \frac12 \cdot \frac{11}{12} = \frac{11}{24} \).
:::

::: {#exr-finite-sums-b3}
[B3: Name the method]

*Say which method this is, then complete it.* Show that, for every \( n \in \nN \),
\[
\sum_{k=1}^{n} \frac{2k+1}{k^2(k+1)^2} = 1 - \frac{1}{(n+1)^2} .
\]
:::

::: {.solution}
The method is telescoping (@exm-method-telescoping), with \( b_k \coloneqq \frac{1}{k^2} \). By @fd3:lem-field-fraction-rules (c),
\[
\frac{1}{k^2} - \frac{1}{(k+1)^2} = \frac{(k+1)^2 - k^2}{k^2(k+1)^2} = \frac{2k+1}{k^2(k+1)^2} .
\]
So each term is \( b_k - b_{k+1} \). By @thm-telescoping (a), after shifting to start at \( 0 \) and with both signs reversed, the sum is \( b_1 - b_{n+1} = 1 - \frac{1}{(n+1)^2} \). For \( n = 0 \) both sides are \( 0 \).
:::

::: {#exr-finite-sums-b4}
[B4: Find the error]

Claim: for every \( n \ge 1 \) and all \( b_1, \dots, b_{n+1} \) in a commutative ring, \( \sum_{k=1}^{n} (b_{k+1} - b_k) = b_n - b_1 \).

*Proof.* With \( j = k - 1 \) the sum is \( \sum_{j=0}^{n-1} (b_{j+2} - b_{j+1}) \), and @thm-telescoping (a) with \( n - 1 \) in place of \( n \) gives the last term minus the first, \( b_n - b_1 \).

Find the wrong step. Is the claim true?
:::

::: {.solution}
The shift is right; the endpoint is wrong. The shifted sum is a telescoping sum for \( c_j \coloneqq b_{j+1} \), and @thm-telescoping (a) with \( n - 1 \) in place of \( n \) gives \( c_{(n-1)+1} - c_0 = c_n - c_0 = b_{n+1} - b_1 \). The proof read "the last term" as \( b_n \), the last index of the original sum, instead of \( c_n = b_{n+1} \). The claim is false: with \( b_k \coloneqq k \) and \( n = 1 \), the left side is \( b_2 - b_1 = 1 \) and the right side \( b_1 - b_1 = 0 \).
:::

### C. Going deeper

::: {#exr-finite-sums-c1}
[C1: The sum of the cubes]

Prove that \( \sum_{k=1}^{n} k^3 = \Bigl( \frac{n(n+1)}{2} \Bigr)^2 \) for every \( n \in \nN \), by the verification form of @exm-method-telescoping.
:::

::: {.solution}
Index from \( 0 \): the term \( k = 0 \) is \( 0^3 = 0 \), so \( \sum_{k=0}^{n} k^3 = \sum_{k=1}^{n} k^3 \) by @prp-sum-reindex (b) with \( m = 0 \). Let \( F(k) \coloneqq \frac{k^2(k+1)^2}{4} \), the guessed value. Then \( F(0) = 0 = 0^3 \), and for \( 1 \le k \le n \),
\[
F(k) - F(k - 1) = \frac{k^2}{4} \bigl( (k + 1)^2 - (k - 1)^2 \bigr) = \frac{k^2}{4} \cdot 4k = k^3 .
\]
By @thm-telescoping (a), with \( b_j \coloneqq F(j) \) and \( n - 1 \) in place of \( n \), \( \sum_{k=1}^{n} \bigl( F(k) - F(k-1) \bigr) = F(n) - F(0) \) for \( n \ge 1 \). So
\[
\sum_{k=0}^{n} k^3 = 0^3 + \sum_{k=1}^{n} k^3 = F(0) + F(n) - F(0) = F(n) = \Bigl( \frac{n(n+1)}{2} \Bigr)^2 ,
\]
and for \( n = 0 \) both sides are \( 0 \). Check at \( n = 3 \): \( 1 + 8 + 27 = 36 = 6^2 \).

**What a complete answer needs.** (10 points)
- 4: computes \( F(k) - F(k-1) = k^3 \) for \( 1 \le k \le n \) and checks \( F(0) \).
- 3: applies @thm-telescoping with the endpoints stated correctly, \( F(n) - F(0) \).
- 3: concludes the formula, with the term \( k = 0 \) (or the case \( n = 0 \)) accounted for.

A proof by induction on \( n \) earns the points for the corresponding steps: the step computation for the first 4, the base case and the inductive structure for the next 3.

**Slips that lose the step.** Telescoping to \( F(n) - F(1) \) or to \( F(n + 1) - F(0) \) earns 0 for the step.
:::

<!-- dependency ledger
prp-power-laws-commutative-ring (proof): (m + n) + 1 = m + (n + 1) and m(n + 1) = mn + m in N | fd3 Chapter 1 arithmetic of N (thm-omega-arithmetic-laws), used as in the moved proof
lem-natural-multiples (proof): (m + 1)k = mk + k in N | fd3 Chapter 1 arithmetic of N (def-omega-arithmetic), as in the moved proof
prp-power-laws-commutative-ring (claim): (paragraph Powers, before it) the power recursion exists in R | fd2:thm-recursion with X = R, start 1, step (k, y) -> yz, on fd3's N through fd3:cor-omega-identification (b); it is the recursion of fd3:def-naturals-in-ordered-field (b)
lem-ring-finite-sums (proof): sum of one term is that term, 0 + a_0 = a_0 | (F1), (F3), unfolding the recursion
prp-sum-reindex (proof): sums with general bounds m+1..n in a ring obey the finite-lists, shift and split-off-the-last-term remarks | fd2:def-sum-product remarks, same proofs in R (stated in prose at the section start)
prp-sum-order (proof): a tail sum from m+1 to n, shifted to start at 0, compared by (a) | shift remark after fd2:def-sum-product
exm-odd-sum-reversal (solution): constant sum sum_{k=0}^{n} c = (n + 1) . c | inline (one-line induction)
exm-odd-sum-reversal (solution): 2S = S + S and S = (n+1)^2 from 2S = 2(n+1)^2 in R | ordered field R, dividing by 2 != 0
prp-double-sum (proof): induction "for every array" on the number of rows | inline
thm-telescoping (proof): (b_{n+1} - b_0) + (b_{n+2} - b_{n+1}) = b_{n+2} - b_0 | (F1)-(F4), on the Uses line
thm-telescoping (proof): b_{n+1} b_{n+1}^{-1} = 1 and the regrouping in (b) | (F5)-(F8), on the Uses line
exm-telescoping-squares (solution): (k + 1)^3 = k^3 + 3k^2 + 3k + 1 | school expansion, fd3:prp-ring-algebra (d) twice with (F9)
exm-telescoping-squares (solution): solving a linear equation for the sum in R | field arithmetic in R
thm-telescoping (claim): (paragraph Telescoping products) prod (x_k y_k) = (prod x_k)(prod y_k) | same induction as lem-ring-finite-sums (a), with (F5), (F6); not written out
thm-telescoping (claim): (paragraph Telescoping products) prod_{k=2}^{n} (k-1)/k = 1/n and prod_{k=2}^{n} (k+1)/k = (n+1)/2 | thm-telescoping (b) after a shift
exr-finite-sums-b1 (solution): (k + 1)! = k! (k + 1) | fd2:def-sum-product (factorial recursion)
exr-finite-sums-b1 (solution): 1/(2k-1) - 1/(2k+1) = 2/((2k-1)(2k+1)) | fd3:lem-field-fraction-rules (c), as in the Quick check before the exercises
exr-finite-sums-b2 (solution): 1/(k(k+2)) = (1/2)(1/k - 1/(k+2)) and the skipping telescope | fd3:lem-field-fraction-rules (c); the fold "When the cancellation skips"
exr-finite-sums-c1 (solution): (k+1)^2 - (k-1)^2 = 4k | school expansion, fd3:prp-ring-algebra (d)
-->
