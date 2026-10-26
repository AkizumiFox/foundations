# Division with Remainder

Two facts about the integers of school, taken as known, were proved in the previous volume: every integer is even or odd, and not both (*Sets and Functions*, Section 1.1, @fd2:thm-even-or-odd), and division with remainder (*Sets and Functions*, Section 3.2, @fd2:thm-division-algorithm). The integers are now the set of classes built in Section 2.1. Is \( [(0, 7)] \), the class that school calls \( -7 \), still odd, and could some integer be even and odd at once? Nothing proved so far says. This section answers by proving division with remainder again, on the constructed \( \nZ \): the proof is that of *Sets and Functions*, Section 3.2, with each school fact replaced by a result of this chapter. Divisibility comes first, since uniqueness of the remainder rests on it.

Throughout, \( \nZ \) is the ordered ring of @thm-integers-ordered-ring, with \( \nN \subseteq \nZ \) and \( \nZ_{>0} = \{ n \in \nZ : n > 0 \} \) (@thm-integers-ordered-ring (b)), and \( a - b \coloneqq a + (-b) \). Numerals \( 2 \coloneqq 1 + 1 \), \( 3 \coloneqq 2 + 1 \), and so on, are the natural numbers of those names, as in Section 2.2; a sum or product of numerals may be computed in \( \nN \), because the embedding of @prp-naturals-embed-integers preserves \( + \) and \( \cdot \), and a sign is moved by @prp-ring-algebra (c), as in \( (-4) \cdot 5 = -(4 \cdot 5) = -20 \).

## Divisibility on the constructed integers

The definition of divisibility needs nothing that the ring \( \nZ \) lacks. We restate it, and the definition of a prime, from *Sets and Functions*, Section 1.1, with \( \nZ \) now the ring of Chapter 2.

**Divisibility** (@fd2:def-divides). Let \( a, b \in \nZ \). Then \( a \) **divides** \( b \), written \( a \mid b \), if **there exists** \( k \in \nZ \) with \( b = ka \). Then \( a \) is a **divisor** of \( b \), and \( b \) is a **multiple** of \( a \). We write \( a \nmid b \) when \( a \) does not divide \( b \).

**Prime** (@fd2:def-prime). An integer \( p \) is **prime** if \( p \ge 2 \) and the only **positive** divisors of \( p \) are \( 1 \) and \( p \). A **prime factor** of an integer \( n \) is a prime \( p \) with \( p \mid n \).

*Divisibility is a question about existence: is \( b \) some integer times \( a \)?*

Some instances. \( 3 \mid -12 \), since \( -12 = (-4) \cdot 3 \). \( -4 \mid 0 \), since \( 0 = 0 \cdot (-4) \). Even \( 0 \mid 0 \) holds, since \( 0 = 1 \cdot 0 \): the definition asks for **some** \( k \), and here every \( k \) works. On the other hand \( 5 \nmid 12 \). That is a statement that **no** \( k \in \nZ \) has \( 12 = 5k \), and to prove it we need the theorem on division with remainder below.

The rules below are short consequences of the ring laws and the order.

::: {#prp-divisibility-rules-integers}
[Rules for Divisibility in \( \nZ \)]

Let \( a, b, c, x, y \in \nZ \).

::: {.enumerate options="label=(\alph*)"}
1. \( a \mid 0 \), \( 1 \mid a \) and \( a \mid a \). If \( 0 \mid a \), then \( a = 0 \).
2. If \( a \mid b \) and \( b \mid c \), then \( a \mid c \).
3. If \( a \mid b \) and \( a \mid c \), then \( a \mid bx + cy \).
4. If \( a \mid b \), then \( (-a) \mid b \) and \( a \mid (-b) \).
5. If \( a \mid b \), \( a > 0 \) and \( b > 0 \), then \( a \le b \).
6. If \( a, b \in \nN \), \( a \mid b \) and \( b \mid a \), then \( a = b \).
7. If \( a \mid 1 \), then \( a = 1 \) or \( a = -1 \).
8. If \( a \ne 0 \), then **exactly one** of \( a \), \( -a \) lies in \( \nZ_{>0} \).
:::
:::

::: {.idea}
Parts (a)–(d) are identities in the commutative ring \( \nZ \): write each hypothesis as an equation \( b = ka \) and rearrange. Part (e) is the one that needs the order. If \( b = ka \) with \( a, b > 0 \), the factor \( k \) cannot be zero or negative, so by discreteness it is at least \( 1 \), and multiplying \( a \) by something at least \( 1 \) cannot make it smaller (the method of @exm-method-one-positive-element). Parts (f) and (g) then follow from (e), and (h) is (P2) for the positives of \( \nZ \).
:::

::: {.proof}
We use the ring laws (F1)–(F7) and (F9) of \( \nZ \) (@thm-integers-commutative-ring) without further mention. Parts (a)–(d) are one-line identities and (h) restates (P2); their proofs are written out in the fold. After it come (e), which needs the order and discreteness, and the two parts built on it, (f) and (g).

::: {.second-reading title="Parts (a)–(d) and (h)"}
(a) \( 0 = a \cdot 0 = 0 \cdot a \) by @prp-ring-algebra (b) and (F6), so \( a \mid 0 \) with \( k = 0 \). Also \( a = a \cdot 1 \) by (F7), so \( 1 \mid a \) with \( k = a \); and \( a = 1 \cdot a \), so \( a \mid a \) with \( k = 1 \). If \( 0 \mid a \), then \( a = k \cdot 0 = 0 \) for some \( k \in \nZ \), by @prp-ring-algebra (b).

(b) Let \( b = ka \) and \( c = lb \) with \( k, l \in \nZ \). Then \( c = l(ka) = (lk)a \) by (F5), so \( a \mid c \).

(c) Let \( b = ka \) and \( c = la \). Then
\[
bx + cy = (ka)x + (la)y = (kx)a + (ly)a = (kx + ly)a
\]
by (F5), (F6) and (F9), and \( kx + ly \in \nZ \). So \( a \mid bx + cy \).

(d) Let \( b = ka \). By @prp-ring-algebra (c), \( (-k)(-a) = ka = b \), so \( (-a) \mid b \); and \( (-k)a = -(ka) = -b \), so \( a \mid (-b) \).

(h) Let \( a \ne 0 \). By the converse part of @prp-order-from-positives, applied to the ordered ring \( \nZ \), the set \( \{ x \in \nZ : x > 0 \} \) satisfies (P2), so exactly one of \( a > 0 \), \( -a > 0 \) holds. That set is \( \nZ_{>0} \) by @thm-integers-ordered-ring (b).
:::

(e) Let \( b = ka \) with \( k \in \nZ \), \( a > 0 \) and \( b > 0 \). We show first that \( k > 0 \). If \( k = 0 \), then \( b = 0 \cdot a = 0 \) by @prp-ring-algebra (b), against \( b > 0 \). If \( k < 0 \), then \( ka < 0 \cdot a = 0 \) by @prp-ordered-ring-rules (c) (multiplying \( k < 0 \) by \( a > 0 \)), again against \( b > 0 \). So \( k > 0 \), and by discreteness (@thm-integers-ordered-ring (c), with \( 0 < k \)) \( 1 \le k \). If \( k = 1 \), then \( b = a \). If \( 1 < k \), then \( k - 1 > 0 \) by @prp-ordered-ring-rules (a), so \( (k - 1)a > 0 \cdot a = 0 \) by @prp-ordered-ring-rules (c), that is, \( b - a = ka + (-1)a = (k - 1)a > 0 \) (@prp-ring-algebra (c), (F7) and (F9)), and \( a < b \) by @prp-ordered-ring-rules (a). In both cases \( a \le b \).

(f) Let \( a, b \in \nN \) with \( a \mid b \) and \( b \mid a \). If \( a = 0 \), then \( 0 \mid b \), so \( b = 0 = a \) by (a). If \( b = 0 \), then \( a = 0 \) in the same way. Otherwise \( a, b \in \nN \) are non-zero, hence positive (@thm-integers-ordered-ring (b)), and (e) gives \( a \le b \) and \( b \le a \). Since \( \le \) is a total order (@prp-ordered-ring-rules (i)), it is antisymmetric, and \( a = b \).

(g) Let \( a \mid 1 \), say \( 1 = ka \). Then \( a \ne 0 \): otherwise \( 1 = k \cdot 0 = 0 \), against \( 1 \ne 0 \) in \( \nZ \) (@thm-integers-commutative-ring). By (h), one of \( a \), \( -a \) is positive; call it \( e \). Then \( e \mid 1 \), by (d) if \( e = -a \). Since \( 1 > 0 \) (@prp-ordered-ring-rules (e)), part (e) gives \( e \le 1 \); and \( e > 0 \) gives \( 1 \le e \) by discreteness. So \( e = 1 \). If \( e = a \), then \( a = 1 \); if \( e = -a \), then \( a = -(-a) = -1 \) by @prp-ring-algebra (a). This proves the proposition.
:::

Part (f) is the antisymmetry of divisibility on \( \nN \), @fd2:prp-divides-partial-order of *Sets and Functions*, Section 5.1, now proved on \( \nN \subseteq \nZ \) for the constructed integers. On all of \( \nZ \) it fails: \( 2 \mid -2 \) and \( -2 \mid 2 \), by (d), yet \( 2 \ne -2 \).

::: {.check}
Which hypothesis of (e) fails for \( a = 3 \), \( b = 0 \), and is the conclusion \( a \le b \) true there?
:::

::: {.solution}
\( 3 \mid 0 \) by (a), and \( a = 3 > 0 \), but \( b = 0 \) is not positive. The conclusion \( 3 \le 0 \) is false. Every integer divides \( 0 \), so no bound of the form \( a \le b \) can hold for \( b = 0 \); that is the reason for the hypothesis \( b > 0 \).
:::

## Division with remainder

Now the substitute for division. Given \( a \in \nZ \) and \( n \in \nZ_{>0} \), we want to write \( a \) as a multiple of \( n \) plus something small, and we want "small" to make the answer unique. The obvious attempt subtracts \( n \) from \( a \) until what is left lies in \( \{0, \dots, n - 1\} \), adding \( n \) instead when \( a \) is negative. That is a process; the theorem replaces it by a least element.

::: {#thm-integers-division-remainder}
[Division with Remainder in \( \nZ \)]

Let \( a \in \nZ \) and \( n \in \nZ_{>0} \).

::: {.enumerate options="label=(\alph*)"}
1. There are **unique** \( q, r \in \nZ \) with
\[
a = qn + r \quad \text{and} \quad 0 \le r < n .
\]
:::

The integers \( q \) and \( r \) are the **quotient** and the **remainder** of \( a \) on division by \( n \).
:::

::: {.idea}
This is @fd2:thm-division-algorithm, and the proof is that volume's: the method of @fd2:exm-method-least-element, with \( S \) the non-negative integers of the form \( a - kn \), and @prp-integer-least-element in place of the school least-element principle. The least one, \( r \), lies below \( n \), or else \( r - n \) would be a smaller one. Uniqueness is @fd2:exm-method-uniqueness: two remainders differ by a multiple of \( n \) and by less than \( n \), and @prp-divisibility-rules-integers (e) forbids a positive multiple of \( n \) below \( n \). What is new is only that every step is now a theorem about the constructed \( \nZ \).
:::

::: {.proof}
Read the proof of @fd2:thm-division-algorithm with these replacements:

- the closure of \( \nZ \) under \( + \), \( - \), \( \cdot \) (@fd2:prp-integers-closed (a)) → @thm-integers-commutative-ring, with the identities \( a - an = a(1 - n) \) and \( r - n = a - (q + 1)n \) from the ring laws and @prp-ring-algebra;
- "a positive integer is at least \( 1 \)" (@fd2:prp-integers-closed (b)) → discreteness, @thm-integers-ordered-ring (c);
- @fd2:cor-well-ordering-integers → @prp-integer-least-element;
- the step "a positive multiple of \( n \) is at least \( n \)" → @prp-divisibility-rules-integers (e);
- the school rules for inequalities, and cancelling \( n \ne 0 \) from \( qn = q'n \) → @prp-ordered-ring-rules.

With these, the proof of *Sets and Functions*, Section 3.2 goes through step for step on the constructed \( \nZ \); the fold below writes it out.

::: {.second-reading title="The proof, line by line on the constructed ℤ"}
(a) *Existence.* Let
\[
R \coloneqq \{ a - kn : k \in \nZ \} \cap \{ x \in \nZ : x \ge 0 \} .
\]
We show \( R \ne \emptyset \). If \( a \ge 0 \), take \( k = 0 \): \( a - 0 \cdot n = a - 0 = a \ge 0 \), by (F6), @prp-ring-algebra (b) and \( -0 = 0 \) (\( 0 + 0 = 0 \) and @prp-ring-algebra (a)). If \( a < 0 \), take \( k = a \): then \( a - an = a + a(-n) = a(1 - n) \) by @prp-ring-algebra (c), (F7) and (F9). Since \( n > 0 \), discreteness (@thm-integers-ordered-ring (c)) gives \( 1 \le n \). If \( n = 1 \), then \( a(1 - n) = a \cdot 0 = 0 \) by @prp-ring-algebra (b). If \( 1 < n \), then \( -n < -1 \) by @prp-ordered-ring-rules (a), so \( 1 - n < 0 \) by (O3); multiplying \( a < 0 \) by \( 1 - n < 0 \) reverses the inequality (@prp-ordered-ring-rules (d)), so \( a(1 - n) > 0 \cdot (1 - n) = 0 \). In every case \( R \) has an element.

The set \( R \subseteq \nZ \) is non-empty and has the lower bound \( 0 \), so by @prp-integer-least-element it has a least element \( r \). Write \( r = a - qn \) with \( q \in \nZ \). Then \( a = qn + r \) and \( r \ge 0 \).

Suppose \( r \ge n \). Then \( r - n \ge 0 \): if \( r = n \), then \( r - n = 0 \) by (F4); if \( r > n \), then \( r - n > 0 \) by @prp-ordered-ring-rules (a). Also \( r - n = a - qn - n = a + (-1)(qn) + (-1)n = a + (-1)\bigl((q + 1)n\bigr) = a - (q + 1)n \), since \( -x = (-1)x \) for every \( x \) (@prp-ring-algebra (c) and (F7)) and by (F9), so \( r - n \in R \). But \( -n < -0 = 0 \) (@prp-ordered-ring-rules (a), since \( n > 0 \)), so \( r - n < r \) by (O3). This contradicts the choice of \( r \) as least. Hence \( r < n \).

*Uniqueness.* Let \( a = qn + r = q'n + r' \) with \( q, q', r, r' \in \nZ \), \( 0 \le r < n \) and \( 0 \le r' < n \). Suppose \( r \ne r' \). Exchanging \( (q, r) \) and \( (q', r') \) changes neither the hypotheses nor the goal, so we may suppose \( r' < r \). Adding \( -r' - qn \) to both sides of \( qn + r = q'n + r' \) gives
\[
r - r' = q'n - qn = (q' - q)n ,
\]
by (F1)–(F4), and by @prp-ring-algebra (c) with (F9) for the last step, so \( n \mid r - r' \). Here \( r - r' > 0 \) by @prp-ordered-ring-rules (a), and \( n > 0 \), so @prp-divisibility-rules-integers (e) gives \( n \le r - r' \). But adding \( r - r' \) to \( 0 \le r' \) gives \( r - r' \le (r - r') + r' = r \) (@prp-ordered-ring-rules (b)), and \( r < n \); so \( r - r' < n \), a contradiction. Hence \( r = r' \). Then \( qn = q'n \) (add \( -r \) to both sides of \( qn + r = q'n + r \)), so \( (q - q')n = qn - q'n = 0 \) by @prp-ring-algebra (c) and (F9), and since \( n \ne 0 \), @prp-ordered-ring-rules (f) gives \( q - q' = 0 \). Hence \( q = (q - q') + q' = q' \), by (F1)–(F4).
:::
:::

For \( n = 0 \) the statement fails: no \( r \) satisfies \( 0 \le r < 0 \). Exercise B1 handles \( n < 0 \).

Uniqueness is what turns the theorem into a test for divisibility: **\( n \mid a \) if and only if the remainder of \( a \) on division by \( n \) is \( 0 \)**. Indeed, if \( a = kn \), then \( a = kn + 0 \) is a division with remainder, and by uniqueness it is the only one; conversely \( a = qn + 0 \) says \( n \mid a \). For instance \( 12 = 2 \cdot 5 + 2 \) with \( 0 \le 2 < 5 \), so the remainder is \( 2 \ne 0 \), and \( 5 \nmid 12 \).

::: {.check}
Find the quotient and the remainder of \( a = -23 \) on division by \( n = 4 \).
:::

::: {.solution}
\( q = -6 \) and \( r = 1 \): \( (-6) \cdot 4 + 1 = -24 + 1 = -23 \), and \( 0 \le 1 < 4 \). By uniqueness this is the only such pair. The equation \( -23 = (-5) \cdot 4 - 3 \) is also true, but \( -3 \) is not a remainder, since it fails \( 0 \le r < 4 \); the warning below says why that matters.
:::

::: {.warning}
"The remainder" means the \( r \) with \( 0 \le r < n \). The equation \( -17 = (-3) \cdot 5 - 2 \) is true, but \( -2 \) is **not** the remainder of \( -17 \) on division by \( 5 \); the remainder is \( 3 \). If negative "remainders" were allowed, uniqueness would fail at once: \( -17 = (-3) \cdot 5 + (-2) = (-4) \cdot 5 + 3 \).
:::

## Even and odd

Recall that an integer \( a \) is **even** if \( a = 2k \) for some \( k \in \nZ \), and **odd** if \( a = 2k + 1 \) for some \( k \in \nZ \) (@fd2:def-parity, as in @fd2:thm-even-or-odd), now read on the constructed \( \nZ \). With \( n = 2 \), the theorem answers the opening question.

::: {#cor-integers-even-odd}
[Even and Odd Integers]

::: {.enumerate options="label=(\alph*)"}
1. Every \( a \in \nZ \) is even or odd, and **not both**. More precisely, either \( a = 2q \) for exactly one \( q \in \nZ \) and \( a \) is not of the form \( 2k + 1 \), or \( a = 2q + 1 \) for exactly one \( q \in \nZ \) and \( a \) is not of the form \( 2k \).
2. If \( a \in \nZ \) and \( a^2 \) is even, then \( a \) is even.
:::
:::

::: {.idea}
Divide by \( 2 \). The remainder lies in \( \{0, 1\} \), by discreteness, and it is unique, so each integer has exactly one of the two forms. For (b), square the odd form and read off the remainder.
:::

::: {.proof}
(a) Since \( 2 = 1 + 1 > 0 \), the theorem with \( n = 2 \) gives unique \( q, r \in \nZ \) with \( a = 2q + r \) and \( 0 \le r < 2 \). Then \( r \in \{0, 1\} \): if \( r \ne 0 \), then \( 0 < r \), so \( 1 \le r \) by discreteness (@thm-integers-ordered-ring (c)); and if moreover \( 1 < r \), then \( 2 = 1 + 1 \le r \) by discreteness again, against \( r < 2 \). If \( a = 2k \) and \( a = 2k' + 1 \) for some \( k, k' \in \nZ \), then \( (k, 0) \) and \( (k', 1) \) would be two pairs as in the theorem, and \( 0 \ne 1 \) contradicts its uniqueness. The same uniqueness shows that \( q \) is the only integer with \( a = 2q + r \).

(b) Suppose \( a \) is not even. By (a), \( a = 2q + 1 \) with \( q \in \nZ \). Then
\[
a^2 = (2q + 1)^2 = 4q^2 + 4q + 1 = 2(2q^2 + 2q) + 1 ,
\]
by @prp-ring-algebra (d) and (F5), (F6), (F9), so \( a^2 \) is odd, and by (a) it is not even. This proves (b) by contraposition.
:::

So \( -7 = (-4) \cdot 2 + 1 \) is odd and not even, as school says, and now by proof. Part (a) is @fd2:thm-even-or-odd on the constructed \( \nZ \), and part (b) is @fd1:thm-square-even-implies-even, whose proof used (a) and the computation above as school facts. For \( a \in \nN \), (a) is also @prp-omega-powers-parity (d) of Chapter 1.

::: {.remark}
[Looking ahead]

*Algebraic Preliminaries*, Chapter 1 builds on this section: greatest common divisors and Bézout's identity, primes and unique factorization, and arithmetic modulo \( n \), all on the constructed \( \nZ \). Chapter 3 of this volume builds the rationals as classes of fractions, and its integer part of \( a/n \) is the quotient found here.
:::

## Exercises

### A. Check your understanding

::: {#exr-division-with-remainder-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Find the quotient and the remainder on division by \( n = 6 \) of \( a = 47 \), of \( a = -47 \) and of \( a = 0 \).
2. Where is \( n > 0 \) used in the existence half of @thm-integers-division-remainder (a)?
3. True or false, with a reason: \( 0 \mid 0 \).
4. True or false, with a reason: for all \( a, b \in \nZ \), if \( a \mid b \) and \( b \mid a \), then \( a = b \).
:::
:::

::: {.solution}
(a) \( 47 = 7 \cdot 6 + 5 \), so \( (q, r) = (7, 5) \). \( -47 = (-8) \cdot 6 + 1 \), since \( -48 + 1 = -47 \), so \( (q, r) = (-8, 1) \). \( 0 = 0 \cdot 6 + 0 \), so \( (q, r) = (0, 0) \). In each case \( 0 \le r < 6 \), so by uniqueness these are the quotient and remainder. Note \( (-8, 1) \), not \( (-7, -5) \).

(b) Twice. For \( a < 0 \), the element \( a - an = a(1 - n) \) of \( R \) is non-negative because \( 1 - n \le 0 \), which comes from \( n \ge 1 \), that is, from \( n > 0 \) and discreteness. And the contradiction "\( r - n < r \)" needs \( -n < 0 \), that is, \( n > 0 \).

(c) True: \( 0 = 1 \cdot 0 \), so \( k = 1 \) witnesses \( 0 \mid 0 \) (@prp-divisibility-rules-integers (a)).

(d) False: \( 2 \mid -2 \) and \( -2 \mid 2 \) (@prp-divisibility-rules-integers (d)), but \( 2 \ne -2 \). The statement is true for \( a, b \in \nN \) (@prp-divisibility-rules-integers (f)).
:::

### B. Practice

::: {#exr-division-with-remainder-b1}
[B1: Negative divisors]

Let \( a, n \in \nZ \) with \( n < 0 \). Prove that there are unique \( q, r \in \nZ \) with \( a = qn + r \) and \( 0 \le r < -n \).
:::

::: {.solution}
Since \( n < 0 \), \( -n > 0 \) by @prp-ordered-ring-rules (a), so \( -n \in \nZ_{>0} \).

*Existence.* By @thm-integers-division-remainder (a) applied to \( a \) and \( -n \), there are \( q_0, r \in \nZ \) with \( a = q_0(-n) + r \) and \( 0 \le r < -n \). Let \( q \coloneqq -q_0 \). Then \( q_0(-n) = (-q_0)n = qn \) by @prp-ring-algebra (c), so \( a = qn + r \).

*Uniqueness.* Let \( a = qn + r = q'n + r' \) with \( 0 \le r, r' < -n \). By @prp-ring-algebra (c), \( qn = (-q)(-n) \) and \( q'n = (-q')(-n) \), so \( a = (-q)(-n) + r = (-q')(-n) + r' \) are two divisions of \( a \) by \( -n \). The uniqueness in @thm-integers-division-remainder (a) gives \( r = r' \) and \( -q = -q' \), hence \( q = -(-q) = -(-q') = q' \) by @prp-ring-algebra (a).
:::

::: {#exr-division-with-remainder-b2}
[B2: Three in a row]

Let \( a \in \nZ \). Prove that **exactly one** of \( a \), \( a + 1 \), \( a + 2 \) is divisible by \( 3 \).
:::

::: {.solution}
*At least one.* By @thm-integers-division-remainder (a), \( a = 3q + r \) with \( 0 \le r < 3 \), and \( r \in \{0, 1, 2\} \) by discreteness, as in the proof of @cor-integers-even-odd. If \( r = 0 \), then \( 3 \mid a \). If \( r = 1 \), then \( a + 2 = 3q + 3 = 3(q + 1) \). If \( r = 2 \), then \( a + 1 = 3q + 3 = 3(q + 1) \).

*At most one.* Suppose \( 3 \mid a + i \) and \( 3 \mid a + j \) with \( 0 \le i < j \le 2 \). By @prp-divisibility-rules-integers (c) (with \( x = 1 \), \( y = -1 \)), \( 3 \mid (a + j) - (a + i) = j - i \), and \( j - i \in \{1, 2\} \) is positive. By @prp-divisibility-rules-integers (e), \( 3 \le j - i \le 2 \), which is false. So no two of the three are divisible by \( 3 \).

(Equivalently: the remainders of \( a \), \( a + 1 \), \( a + 2 \) on division by \( 3 \) are \( r \), and then the other two of \( 0, 1, 2 \), and uniqueness of remainders allows only one of them to be \( 0 \).)
:::

### C. Going deeper

::: {#exr-division-with-remainder-c2}
[C1: Exit check: remainders of squares]

::: {.enumerate options="label=(\alph*)"}
1. Prove that for every \( a \in \nZ \), the remainder of \( a^2 \) on division by \( 4 \) is \( 0 \) or \( 1 \).
2. Deduce that no integer whose remainder on division by \( 4 \) is \( 3 \) is a sum \( x^2 + y^2 \) of two squares of integers.
:::

Name the result behind each step.
:::

::: {.solution}
(a) By @cor-integers-even-odd (a), \( a = 2q \) or \( a = 2q + 1 \) for some \( q \in \nZ \). In the first case \( a^2 = (2q)(2q) = 4q^2 = q^2 \cdot 4 + 0 \), by the ring laws (F5), (F6) and \( 4 = 2 \cdot 2 \), computed in \( \nN \). In the second,
\[
a^2 = (2q + 1)^2 = 4q^2 + 4q + 1 = (q^2 + q) \cdot 4 + 1 ,
\]
by @prp-ring-algebra (d) and the ring laws (F5), (F6), (F9). Since \( 4 \) is a non-zero natural number, \( 4 > 0 \) (@thm-integers-ordered-ring (b)), and both remainders, \( 0 \) and \( 1 \), satisfy \( 0 \le r < 4 \), so by the uniqueness in @thm-integers-division-remainder (a) they are the remainders of \( a^2 \) on division by \( 4 \).

(b) Let \( x, y \in \nZ \). By (a), \( x^2 = 4k + s \) and \( y^2 = 4l + t \) with \( k, l \in \nZ \) and \( s, t \in \{0, 1\} \). Then
\[
x^2 + y^2 = 4(k + l) + (s + t) , \qquad s + t \in \{0, 1, 2\} ,
\]
by (F1), (F2) and (F9). So \( 0 \le s + t \le 2 < 4 \), and by uniqueness \( s + t \) is the remainder of \( x^2 + y^2 \) on division by \( 4 \). It is not \( 3 \), so no sum of two squares has remainder \( 3 \).

**Marking scheme.** (10 points)

- 2: splits into the two cases \( a = 2q \), \( a = 2q + 1 \), citing @cor-integers-even-odd (a).
- 3: expands both squares and writes each in the form \( q' \cdot 4 + r \), with the identities justified by the ring laws.
- 2: checks \( 0 \le r < 4 \) and invokes uniqueness to conclude that \( r \) is **the** remainder.
- 3: for (b), adds the two forms, checks \( 0 \le s + t \le 2 < 4 \), and concludes by uniqueness (or by @prp-divisibility-rules-integers (e) applied to the difference) that the remainder is \( s + t \ne 3 \).

Fatal errors (0 for the step): calling a value outside \( 0 \le r < 4 \) a remainder; concluding in (b) that the remainder is \( s + t \) without checking \( 0 \le s + t < 4 \) or an equivalent divisibility argument.

A proof that divides \( a \) by \( 4 \) instead, with four cases \( a = 4m + j \), \( j \in \{0, 1, 2, 3\} \), earns the first 2 points for the case split (citing @thm-integers-division-remainder (a) and discreteness) and the rest as above.
:::

### R. Review

::: {#exr-division-with-remainder-r1}
[R1]

Let \( f \colon \nN \to \nN \) satisfy \( f(0) = 0 \) and \( f(n + 1) = f(n) + 2n + 1 \) for every \( n \in \nN \). Prove that \( f(n) = n \cdot n \) for every \( n \).
:::

::: {.solution}
By @thm-omega-recursion, with \( g(n, x) = x + 2n + 1 \), exactly one such \( f \) exists, so the question is about a definite function. We prove \( f(n) = n \cdot n \) by induction on \( n \) (@thm-omega-induction).

*Base.* \( f(0) = 0 = 0 \cdot 0 \), by @def-omega-arithmetic (b).

*Step.* Suppose \( f(n) = n \cdot n \). Then \( f(n + 1) = (n \cdot n + 2n) + 1 \). On the other side, with \( \mathrm{S}(n) = n + 1 \) (@def-omega-arithmetic (c)),
\[
\begin{aligned}
(n + 1)(n + 1) &= (n + 1) \cdot n + (n + 1) \\
&= (n \cdot n + n) + (n + 1) = (n \cdot n + (n + n)) + 1 ,
\end{aligned}
\]
by @def-omega-arithmetic (b) applied to \( (n + 1) \cdot \mathrm{S}(n) \), then @thm-omega-arithmetic-laws (e) for \( (n + 1) \cdot n = n \cdot n + n \), and @thm-omega-arithmetic-laws (c) to regroup. Finally \( 2n = (1 + 1)n = 1 \cdot n + 1 \cdot n = n + n \), by \( 1 + 1 = 2 \) (@def-omega-arithmetic (c)) and @thm-omega-arithmetic-laws (d), (e). So \( f(n + 1) = (n + 1)(n + 1) \), and the claim holds for every \( n \).

This is Chapter 1's move of fixing everything else and inducting on the recursion variable, as in the proof of @thm-omega-arithmetic-laws.
:::

::: {#exr-division-with-remainder-r2}
[R2]

Decide which of the following maps \( \nZ \to \nZ \) are injective and which are surjective:

::: {.enumerate options="label=(\alph*)"}
1. \( x \mapsto -x \);
2. \( x \mapsto 2x \);
3. \( x \mapsto x^2 \).
:::
:::

::: {.solution}
(a) Bijective. Since \( -(-x) = x \) (@prp-ring-algebra (a)), equal values \( -x = -y \) give \( x = -(-x) = -(-y) = y \), and every \( y \) is the value at \( -y \).

(b) Injective, not surjective. If \( 2x = 2y \), then \( 2(x - y) = 2x - 2y = 0 \) by (F9) and @prp-ring-algebra (c); and \( 2 \ne 0 \), since \( 2 = 1 + 1 > 0 \). So \( x - y = 0 \) by @prp-ordered-ring-rules (f), and \( x = y \). Not surjective: \( 1 = 2x \) would make \( 1 \) even, but \( 1 = 2 \cdot 0 + 1 \) is odd, and no integer is both (@cor-integers-even-odd (a)).

(c) Neither. Not injective: \( (-1)^2 = 1 = 1^2 \) (@prp-ring-algebra (c)), and \( -1 \ne 1 \), since \( -1 < 0 < 1 \) (shown below) gives \( -1 < 1 \) by (O2), and (O1) forbids equality. Not surjective: \( x^2 \ge 0 \) for every \( x \) (\( x^2 = 0 \) for \( x = 0 \) by @prp-ring-algebra (b), and \( x^2 > 0 \) otherwise by @prp-ordered-ring-rules (e)), while \( -1 < 0 \) (\( 1 > 0 \) by @prp-ordered-ring-rules (e), so \( -1 < -0 = 0 \) by @prp-ordered-ring-rules (a)). So \( -1 \) is not a value.

The methods are those of @fd2:exm-method-injectivity and @fd2:exm-method-surjectivity: for injectivity, start from equal values and reach equal inputs; for surjectivity, solve for the input, or show that a target is never reached.
:::

::: {#exr-division-with-remainder-r3}
[R3]

Prove that for every \( a \in \nZ \): if \( 3 \mid a^2 \), then \( 3 \mid a \).
:::

::: {.solution}
By contraposition, as in @fd1:thm-square-even-implies-even. Suppose \( 3 \nmid a \). Since \( 3 \) is a non-zero natural number, \( 3 > 0 \) (@thm-integers-ordered-ring (b)), so division by \( 3 \) (@thm-integers-division-remainder (a)) gives \( a = 3q + r \) with \( 0 \le r < 3 \), so \( r \in \{0, 1, 2\} \) by discreteness (@thm-integers-ordered-ring (c)), as in the proof of @cor-integers-even-odd; and \( r \ne 0 \), since otherwise \( a = 3q \) and \( 3 \mid a \). By @prp-ring-algebra (d) and the ring laws,
\[
\begin{aligned}
r = 1 &: \quad a^2 = 9q^2 + 6q + 1 = 3(3q^2 + 2q) + 1 , \\
r = 2 &: \quad a^2 = 9q^2 + 12q + 4 = 3(3q^2 + 4q + 1) + 1 .
\end{aligned}
\]
In both cases \( 0 \le 1 < 3 \), so the remainder of \( a^2 \) on division by \( 3 \) is \( 1 \ne 0 \), and \( 3 \nmid a^2 \) by the divisibility test after @thm-integers-division-remainder. This proves the contrapositive.
:::

<!-- dependency ledger
prp-divisibility-rules-integers (proof): ring laws (F1)-(F7), (F9) of Z | thm-integers-commutative-ring (cited at the start of the proof)
prp-divisibility-rules-integers (proof): (h), exactly one of a > 0, -a > 0 for a != 0 | prp-order-from-positives (converse part, (P2)), thm-integers-ordered-ring (b), cited
prp-divisibility-rules-integers (proof): (e), b - a = ka + (-1)a = (k - 1)a | prp-ring-algebra (c), (F7), (F9), cited
prp-divisibility-rules-integers (proof): antisymmetry of <= on Z | prp-ordered-ring-rules (i) (total order, fd2 def-partial-order), cited
prp-divisibility-rules-integers (claim): (the proof's opening) (a)-(d) are one-line identities, (h) restates (P2), (e) needs order and discreteness, (f) and (g) build on (e) | read against the proof on the page (meta-claim)
thm-integers-division-remainder (proof): a - an = a + a(-n) = a(1 - n) and a - 0 = a | prp-ring-algebra (c), (F7), (F9), prp-ring-algebra (b), (F6), cited
thm-integers-division-remainder (proof): -0 = 0 (in a - 0 = a and -n < -0 = 0) | 0 + 0 = 0 by (F3), uniqueness prp-ring-algebra (a), cited
thm-integers-division-remainder (proof): r - n >= 0 from r >= n | (F4) if r = n, prp-ordered-ring-rules (a) if r > n, cited
thm-integers-division-remainder (proof): r - n = a + (-1)(qn) + (-1)n = a + (-1)((q + 1)n) = a - (q + 1)n | -x = (-1)x by prp-ring-algebra (c), (F7); (F9), cited
thm-integers-division-remainder (proof): adding r - r' to 0 <= r' gives r - r' <= r | prp-ordered-ring-rules (b), cited
thm-integers-division-remainder (proof): r - r' = q'n - qn = (q' - q)n; qn = q'n from r = r'; (q - q')n = 0; q = (q - q') + q' | (F1)-(F4), (F9), prp-ring-algebra (c), cited
thm-integers-division-remainder (proof): (main line) fd2's proof of fd2:thm-division-algorithm goes through step for step with the five listed replacements, and the fold is that proof | read against fd2 F2.2 §02 thm-division-algorithm (meta-claim, checkable there): closure (prp-integers-closed (a)), n >= 1 and k >= 1 (prp-integers-closed (b)), cor-well-ordering-integers, kn >= n, order rules and cancelling n
thm-integers-division-remainder (claim): (the paragraph after the proof) no r with 0 <= r < 0 | (O1)
thm-integers-division-remainder (claim): (quick check) -23 = (-6) * 4 + 1 with 0 <= 1 < 4; -23 = (-5) * 4 - 3 | numerals computed in N, sign by prp-ring-algebra (c) (opening paragraph); verify/ch02/thm-integers-division-remainder.py
thm-integers-division-remainder (claim): (warning) -17 = (-3) * 5 + (-2) = (-4) * 5 + 3 | numerals (opening paragraph); verify/ch02/thm-integers-division-remainder.py
cor-integers-even-odd (proof): 2 = 1 + 1 > 0 | prp-ordered-ring-rules (b), (e) (1 > 0)
cor-integers-even-odd (proof): (2q + 1)^2 = 4q^2 + 4q + 1 = 2(2q^2 + 2q) + 1 | prp-ring-algebra (d) with ring laws; numerals 4 = 2 * 2 computed in N (opening paragraph)
cor-integers-even-odd (proof): contraposition | fd1 (classical reasoning, F1.2), standard
cor-integers-even-odd (claim): (opening) [(0, 7)] is the integer school calls -7 | prp-naturals-embed-integers ([(a, b)] = a - b after the identification of Section 2.2), (F3)
cor-integers-even-odd (claim): (the paragraph after the proof) -7 = (-4) * 2 + 1 | numerals, sign by prp-ring-algebra (c) (opening paragraph); verify/ch02/cor-integers-even-odd.py
cor-integers-even-odd (claim): (the paragraph after the proof) part (a) is fd2:thm-even-or-odd on the constructed Z; part (b) is fd1:thm-square-even-implies-even, whose proof used (a) and the computation as school facts; for a in N, (a) is prp-omega-powers-parity (d) | read against fd2 F2.1 §01 and fd1 F1.2 §01 (compared, not used); prp-omega-powers-parity (d) cited
cor-integers-even-odd (claim): (Looking ahead) F5.1 builds gcd, Bezout, primes, unique factorization and congruences on the constructed Z; Chapter 3's integer part of a/n is the quotient | prose pointer: F5.1 (Algebraic Preliminaries, Chapter 1); F3.11 §02 exr-ordered-field-of-rationals-b4 (recut-ch03.md, 3.2 B3); nothing depends on it
prp-divisibility-rules-integers (example): (the instances before it and the paragraph after it) 3 | -12, -4 | 0, 0 | 0, 5 does not divide 12, 2 | -2 | 2 | numerals; verify/ch02/prp-divisibility-rules-integers.py
cor-integers-even-odd (proof): the identity for (2q + 1)^2 | verify/ch02/cor-integers-even-odd.py
exr-division-with-remainder-a1 (solution): 47 = 7 * 6 + 5, -47 = (-8) * 6 + 1 | numerals; verify/ch02/exr-division-with-remainder-a1.py
exr-division-with-remainder-b2 (solution): r in {0, 1, 2} from 0 <= r < 3 | discreteness, thm-integers-ordered-ring (c), as in cor-integers-even-odd (cited)
exr-division-with-remainder-c2 (solution): (2q)(2q) = 4q^2 and (2q + 1)^2 = (q^2 + q) * 4 + 1; 4 = 2 * 2 | prp-ring-algebra (d), ring laws (cited); numerals computed in N (opening paragraph); verify/ch02/exr-division-with-remainder-c2.py
exr-division-with-remainder-c2 (solution): s, t in {0, 1} gives s + t in {0, 1, 2}, 0 <= s + t <= 2 < 4, and s + t != 3 | numerals 0 + 1 = 1, 1 + 1 = 2, 2 < 4 and 2 != 3 in N (thm-omega-order (a)), embedded by thm-integers-ordered-ring (a); verify/ch02/exr-division-with-remainder-c2.py
exr-division-with-remainder-r1 (solution): (n + 1)(n + 1) = (n * n + (n + n)) + 1 and n + n = 2n | def-omega-arithmetic (b), (c), thm-omega-arithmetic-laws (c), (d), (e) (cited); verify/ch02/exr-division-with-remainder-r1.py
exr-division-with-remainder-r2 (solution): 2x - 2y = 2(x - y); -1 != 1 | (F9), prp-ring-algebra (c) (cited); -1 < 0 < 1 from the solution's own step and (O1)
exr-division-with-remainder-r3 (solution): (3q + 1)^2 = 3(3q^2 + 2q) + 1, (3q + 2)^2 = 3(3q^2 + 4q + 1) + 1 | prp-ring-algebra (d) with ring laws; numerals (opening paragraph); verify/ch02/exr-division-with-remainder-r3.py
exr-division-with-remainder-r3 (solution): contraposition | fd1 (classical reasoning, F1.2), standard
-->
