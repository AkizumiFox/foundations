# Divisibility and Division with Remainder

Chapter 2 built \( \nZ \) as an ordered commutative ring, and a Quick check in Section 2.3 showed that it is not a field: \( 2x = 1 \) has no solution in \( \nZ \). So "\( a/b \)" is not available among the integers. What remains is a relation, "\( b \) is a multiple of \( a \)", and the next best thing to division: dividing with a quotient and a remainder. *Sets, Relations, and Cardinality*, Section 1.1 defined the relation and its Section 2.2 proved division with remainder for the school integers. This section does both again for the integers of Chapter 2, where every step must come from the ordered-ring axioms and from the least-element property of \( \nZ \).

Throughout, \( \nZ \) is the ordered ring of @thm-integers-ordered-ring, with \( \nN \subseteq \nZ \) and \( \nZ_{>0} = \{ n \in \nZ : n > 0 \} \) (@thm-integers-ordered-ring (b)), and \( a - b \coloneqq a + (-b) \). Numerals \( 2 \coloneqq 1 + 1 \), \( 3 \coloneqq 2 + 1 \), and so on, are the natural numbers of those names, as in Section 2.6; a sum or product of numerals may be computed in \( \nN \), because the embedding of @prp-naturals-embed-integers preserves \( + \) and \( \cdot \), and a sign is moved by @prp-ring-algebra (c), as in \( (-4) \cdot 5 = -(4 \cdot 5) = -20 \).

## Divisibility on the constructed integers

The definition of divisibility needs nothing that the ring \( \nZ \) lacks. We restate it, and the definition of a prime, from *Sets, Relations, and Cardinality*, Section 1.1, with \( \nZ \) now the ring of Chapter 2.

**Divisibility** (@fd2:def-divides). Let \( a, b \in \nZ \). Then \( a \) **divides** \( b \), written \( a \mid b \), if **there exists** \( k \in \nZ \) with \( b = ka \). Then \( a \) is a **divisor** of \( b \), and \( b \) is a **multiple** of \( a \). We write \( a \nmid b \) when \( a \) does not divide \( b \).

**Prime** (@fd2:def-prime). An integer \( p \) is **prime** if \( p \ge 2 \) and the only **positive** divisors of \( p \) are \( 1 \) and \( p \). A **prime factor** of an integer \( n \) is a prime \( p \) with \( p \mid n \).

Both definitions use only the multiplication of \( \nZ \), its order \( \le \), and the set \( \nZ_{>0} \), and Chapter 2 provides all three. They are the same definitions as before; what changes is that every fact about them must now be proved from Chapter 2.

*Divisibility is a question about existence: is \( b \) some integer times \( a \)?*

Some instances. \( 3 \mid -12 \), since \( -12 = (-4) \cdot 3 \). \( -4 \mid 0 \), since \( 0 = 0 \cdot (-4) \). Even \( 0 \mid 0 \) holds, since \( 0 = 1 \cdot 0 \): the definition asks for **some** \( k \), and here every \( k \) works. On the other hand \( 5 \nmid 12 \). That is a statement that **no** \( k \in \nZ \) has \( 12 = 5k \), and to prove it we need the theorem on division with remainder below.

The relation "\( a \mid b \)" is not a fraction. It is a statement, true or false, about two integers. The expression \( b/a \), for \( a \ne 0 \), is a rational number, and this chapter does not use it to decide divisibility.

Here are the rules for divisibility that the rest of the chapter uses. Each is a short consequence of the ring laws or of the order.

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
Parts (a)–(d) are identities in the commutative ring \( \nZ \): write each hypothesis as an equation \( b = ka \) and rearrange. Part (e) is the one that needs the order. If \( b = ka \) with \( a, b > 0 \), the factor \( k \) cannot be zero or negative, so by discreteness it is at least \( 1 \), and multiplying \( a \) by something at least \( 1 \) cannot make it smaller. Parts (f) and (g) then follow from (e), and (h) is (P2) for the positives of \( \nZ \).
:::

::: {.proof}
We use the ring laws (F1)–(F7) and (F9) of \( \nZ \) (@thm-integers-commutative-ring) without further mention.

(a) \( 0 = a \cdot 0 = 0 \cdot a \) by @prp-ring-algebra (b) and (F6), so \( a \mid 0 \) with \( k = 0 \). Also \( a = a \cdot 1 \) by (F7), so \( 1 \mid a \) with \( k = a \); and \( a = 1 \cdot a \), so \( a \mid a \) with \( k = 1 \). If \( 0 \mid a \), then \( a = k \cdot 0 = 0 \) for some \( k \in \nZ \), by @prp-ring-algebra (b).

(b) Let \( b = ka \) and \( c = lb \) with \( k, l \in \nZ \). Then \( c = l(ka) = (lk)a \) by (F5), so \( a \mid c \).

(c) Let \( b = ka \) and \( c = la \). Then
\[
bx + cy = (ka)x + (la)y = (kx)a + (ly)a = (kx + ly)a
\]
by (F5), (F6) and (F9), and \( kx + ly \in \nZ \). So \( a \mid bx + cy \).

(d) Let \( b = ka \). By @prp-ring-algebra (c), \( (-k)(-a) = ka = b \), so \( (-a) \mid b \); and \( (-k)a = -(ka) = -b \), so \( a \mid (-b) \).

(h) Let \( a \ne 0 \). By the converse part of @prp-order-from-positives, applied to the ordered ring \( \nZ \), the set \( \{ x \in \nZ : x > 0 \} \) satisfies (P2), so exactly one of \( a > 0 \), \( -a > 0 \) holds. That set is \( \nZ_{>0} \) by @thm-integers-ordered-ring (b).

(e) Let \( b = ka \) with \( k \in \nZ \), \( a > 0 \) and \( b > 0 \). We show first that \( k > 0 \). If \( k = 0 \), then \( b = 0 \cdot a = 0 \) by @prp-ring-algebra (b), against \( b > 0 \). If \( k < 0 \), then \( ka < 0 \cdot a = 0 \) by @prp-ordered-ring-rules (c) (multiplying \( k < 0 \) by \( a > 0 \)), again against \( b > 0 \). So \( k > 0 \), and by discreteness (@thm-integers-ordered-ring (c), with \( 0 < k \)) \( 1 \le k \). If \( k = 1 \), then \( b = a \). If \( 1 < k \), then \( k - 1 > 0 \) by @prp-ordered-ring-rules (a), so \( (k - 1)a > 0 \cdot a = 0 \) by @prp-ordered-ring-rules (c), that is, \( b - a = ka + (-1)a = (k - 1)a > 0 \) (@prp-ring-algebra (c), (F7) and (F9)), and \( a < b \) by @prp-ordered-ring-rules (a). In both cases \( a \le b \).

(f) Let \( a, b \in \nN \) with \( a \mid b \) and \( b \mid a \). If \( a = 0 \), then \( 0 \mid b \), so \( b = 0 = a \) by (a). If \( b = 0 \), then \( a = 0 \) in the same way. Otherwise \( a, b \in \nN \) are non-zero, hence positive (@thm-integers-ordered-ring (b)), and (e) gives \( a \le b \) and \( b \le a \). Since \( \le \) is a total order (@prp-ordered-ring-rules (i)), it is antisymmetric, and \( a = b \).

(g) Let \( a \mid 1 \), say \( 1 = ka \). Then \( a \ne 0 \): otherwise \( 1 = k \cdot 0 = 0 \), against \( 1 \ne 0 \) in \( \nZ \) (@thm-integers-commutative-ring). By (h), one of \( a \), \( -a \) is positive; call it \( e \). Then \( e \mid 1 \), by (d) if \( e = -a \). Since \( 1 > 0 \) (@prp-ordered-ring-rules (e)), part (e) gives \( e \le 1 \); and \( e > 0 \) gives \( 1 \le e \) by discreteness. So \( e = 1 \). If \( e = a \), then \( a = 1 \); if \( e = -a \), then \( a = -(-a) = -1 \) by @prp-ring-algebra (a). This proves the proposition.
:::

Part (f) is the antisymmetry of divisibility on \( \nN \), @fd2:prp-divides-partial-order of *Sets, Relations, and Cardinality*, Section 4.1, now proved on \( \nN \subseteq \nZ \) for the constructed integers. On all of \( \nZ \) it fails: \( 2 \mid -2 \) and \( -2 \mid 2 \), by (d), yet \( 2 \ne -2 \). That is why (f) is stated for \( a, b \in \nN \), and why (e) needs \( b > 0 \): \( 3 \mid -3 \), but \( 3 > -3 \). (The hypothesis \( a > 0 \) is a convenience for the proof: \( a = 0 \) cannot divide \( b > 0 \), by (a), and if \( a < 0 < b \), then \( a \le b \) holds anyway.)

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
2. Moreover \( q = \floor{a/n} \), the integer part of the rational number \( a/n \) (@prp-rational-integer-part), so \( r = a - n \floor{a/n} \).
:::

The integers \( q \) and \( r \) are the **quotient** and the **remainder** of \( a \) on division by \( n \).
:::

::: {.idea}
Among the integers \( a - kn \), \( k \in \nZ \), look at the non-negative ones. If there is at least one, @prp-integer-least-element hands us the least, \( r \). It must be below \( n \): otherwise \( r - n \) would be a smaller non-negative one of the same form. Finding a non-negative \( a - kn \) is easy for \( a \ge 0 \) (take \( k = 0 \)) and needs one inequality for \( a < 0 \) (take \( k = a \)). For uniqueness, two remainders differ by a multiple of \( n \) and yet by less than \( n \), and (e) of the rules above forbids a positive multiple of \( n \) below \( n \). Part (b) moves the inequalities \( qn \le a < qn + n \) into \( \nQ \) and divides by \( n \).
:::

::: {.proof}
(a) *Existence.* Let
\[
R \coloneqq \{ a - kn : k \in \nZ \} \cap \{ x \in \nZ : x \ge 0 \} .
\]
We show \( R \ne \emptyset \). If \( a \ge 0 \), take \( k = 0 \): \( a - 0 \cdot n = a - 0 = a \ge 0 \), by (F6), @prp-ring-algebra (b) and \( -0 = 0 \) (\( 0 + 0 = 0 \) and @prp-ring-algebra (a)). If \( a < 0 \), take \( k = a \): then \( a - an = a + a(-n) = a(1 - n) \) by @prp-ring-algebra (c), (F7) and (F9). Since \( n > 0 \), discreteness (@thm-integers-ordered-ring (c)) gives \( 1 \le n \). If \( n = 1 \), then \( a(1 - n) = a \cdot 0 = 0 \) by @prp-ring-algebra (b). If \( 1 < n \), then \( -n < -1 \) by @prp-ordered-ring-rules (a), so \( 1 - n < 0 \) by (O3); multiplying \( a < 0 \) by \( 1 - n < 0 \) reverses the inequality (@prp-ordered-ring-rules (d)), so \( a(1 - n) > 0 \cdot (1 - n) = 0 \). In every case \( R \) has an element.

The set \( R \subseteq \nZ \) is non-empty and has the lower bound \( 0 \), so by @prp-integer-least-element it has a least element \( r \). Write \( r = a - qn \) with \( q \in \nZ \). Then \( a = qn + r \) and \( r \ge 0 \).

Suppose \( r \ge n \). Then \( r - n \ge 0 \): if \( r = n \), then \( r - n = 0 \) by (F4); if \( r > n \), then \( r - n > 0 \) by @prp-ordered-ring-rules (a). Also \( r - n = a - qn - n = a + (-1)(qn) + (-1)n = a + (-1)\bigl((q + 1)n\bigr) = a - (q + 1)n \), since \( -x = (-1)x \) for every \( x \) (@prp-ring-algebra (c) and (F7)) and by (F9), so \( r - n \in R \). But \( -n < -0 = 0 \) (@prp-ordered-ring-rules (a), since \( n > 0 \)), so \( r - n < r \) by (O3). This contradicts the choice of \( r \) as least. Hence \( r < n \).

*Uniqueness.* Let \( a = qn + r = q'n + r' \) with \( q, q', r, r' \in \nZ \), \( 0 \le r < n \) and \( 0 \le r' < n \). Suppose \( r \ne r' \). Exchanging \( (q, r) \) and \( (q', r') \) changes neither the hypotheses nor the goal, so we may suppose \( r' < r \). Then
\[
r - r' = (q' - q)n ,
\]
so \( n \mid r - r' \). Here \( r - r' > 0 \) by @prp-ordered-ring-rules (a), and \( n > 0 \), so @prp-divisibility-rules-integers (e) gives \( n \le r - r' \). But adding \( r - r' \) to \( 0 \le r' \) gives \( r - r' \le (r - r') + r' = r \) (@prp-ordered-ring-rules (b)), and \( r < n \); so \( r - r' < n \), a contradiction. Hence \( r = r' \). Then \( qn = q'n \), so \( (q - q')n = 0 \), and since \( n \ne 0 \), @prp-ordered-ring-rules (f) gives \( q - q' = 0 \), that is, \( q = q' \).

(b) From (a), \( 0 \le r < n \); adding \( qn \) (@prp-ordered-ring-rules (b)) gives
\[
qn \le a < qn + n .
\]
These are inequalities between integers, and by @thm-rationals-ordered-field (b) and @prp-integers-embed-rationals they hold in \( \nQ \) as well, with the same sums and products. In \( \nQ \), \( n > 0 \), so \( n^{-1} > 0 \) (@prp-reciprocal-order (a)). Multiplying by \( n^{-1} \) preserves strict inequalities (@prp-ordered-ring-rules (c)) and equalities, so
\[
q = qn \cdot n^{-1} \le a \cdot n^{-1} < (qn + n) \cdot n^{-1} = q + 1 .
\]
That is, \( q \le a/n < q + 1 \), with \( q \in \nZ \). By the uniqueness in @prp-rational-integer-part, \( q = \floor{a/n} \), and then \( r = a - qn = a - n \floor{a/n} \). This proves the theorem.
:::

The hypothesis \( n > 0 \) is used four times in (a): to find an element of \( R \) when \( a < 0 \) (through \( 1 - n \le 0 \)), to see that \( r - n < r \), and in the uniqueness both to apply @prp-divisibility-rules-integers (e) and, as \( n \ne 0 \), to cancel \( n \) from \( (q - q')n = 0 \). For \( n = 0 \) the statement fails outright: no \( r \) satisfies \( 0 \le r < 0 \). Exercise B1 handles \( n < 0 \).

Uniqueness is what turns the theorem into a test for divisibility: **\( n \mid a \) if and only if the remainder of \( a \) on division by \( n \) is \( 0 \)**. Indeed, if \( a = kn \), then \( a = kn + 0 \) is a division with remainder, and by uniqueness it is the only one; conversely \( a = qn + 0 \) says \( n \mid a \). For instance \( 12 = 2 \cdot 5 + 2 \) with \( 0 \le 2 < 5 \), so the remainder is \( 2 \ne 0 \), and \( 5 \nmid 12 \).

::: {.remark}
The statement of (a) is @fd2:thm-division-algorithm of *Sets, Relations, and Cardinality*, Section 2.2, which was proved there for the school integers. The existence proof above follows the same route, with each school fact replaced by a result of Chapter 2: the closure of \( \nZ \) under \( + \), \( - \), \( \cdot \) by @thm-integers-commutative-ring; "a positive integer is at least \( 1 \)" by @thm-integers-ordered-ring (b), (c); and the least element of a set of integers bounded below by @prp-integer-least-element. The uniqueness argument there is the one packaged here as @prp-divisibility-rules-integers (e). For \( n = 2 \) and \( a \in \nN \), (a) is @prp-omega-powers-parity (d) of Section 1.6, which we compare with but do not use.
:::

Part (b) pays a debt of Section 2.5. There, after @prp-rational-integer-part, the integer part \( \floor{p/q} \) was announced as a quotient; (b) says exactly that, and it gives a second way to compute \( q \) and \( r \). Exercise C1 turns (b) around and proves the existence half of (a) from the integer part.

::: {.check}
Find the quotient and the remainder of \( a = -17 \) on division by \( n = 5 \), and check them against (b).
:::

::: {.solution}
\( q = -4 \) and \( r = 3 \): \( (-4) \cdot 5 + 3 = -20 + 3 = -17 \), and \( 0 \le 3 < 5 \). For (b), \( -4 \le -17/5 < -3 \), since \( (-4) \cdot 5 = -20 \le -17 \) and \( -17 < -15 = (-3) \cdot 5 \) (@thm-rationals-ordered-field (a)); so \( \floor{-17/5} = -4 \).
:::

::: {.warning}
"The remainder" means the \( r \) with \( 0 \le r < n \). The equation \( -17 = (-3) \cdot 5 - 2 \) is true, but \( -2 \) is **not** the remainder of \( -17 \) on division by \( 5 \); the remainder is \( 3 \). If negative "remainders" were allowed, uniqueness would fail at once: \( -17 = (-3) \cdot 5 + (-2) = (-4) \cdot 5 + 3 \). For negative \( a \), the quotient is not "\( a/n \) with the fraction dropped": that would give \( -3 \) here, while \( \floor{-17/5} = -4 \).
:::

## Even and odd

Recall that an integer \( a \) is **even** if \( a = 2k \) for some \( k \in \nZ \), that is, \( 2 \mid a \), and **odd** if \( a = 2k + 1 \) for some \( k \in \nZ \). These are the words *Logic and Proof*, Chapter 1 used, now read on the constructed \( \nZ \). Section 2.6 had parity for natural numbers from @prp-omega-powers-parity (d). With \( n = 2 \), the theorem gives it for every integer, negative ones included, with one citation.

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

Part (b) is @fd1:thm-square-even-implies-even of *Logic and Proof*, Section 2.1, proved there from the school facts (E1)–(E3) about the integers. Part (a) proves (E1) and (E2) for the constructed \( \nZ \), and the computation in (b) is (E3). We compare with that proof and do not use it. *Sets, Relations, and Cardinality*, Section 2.2 proved (E1) and (E2) for the school integers right after @fd2:thm-division-algorithm.

Section 2.6 proved that no rational squares to \( 2 \) by a descent on denominators (@thm-no-rational-square-two), a route that needs only the order and the least-element property of \( \nZ \) and adapts to other non-squares. With (b), and with lowest terms from Section 3.3, the classical parity proof of *Logic and Proof*, Chapter 2 can also be run on the constructed \( \nQ \), every step citable; one of the review exercises at the end of this chapter does so.

## Small primes

Later sections need to know that a few small integers are prime in the constructed \( \nZ \). *Sets, Relations, and Cardinality*, Section 1.1 checked some of these after @fd2:def-prime, for the school integers; that check is not a proof about the ring of Chapter 2, so we redo it here.

::: {.remark}
**The small-primes remark.** The integers \( 2 \), \( 3 \), \( 5 \) and \( 7 \) are prime in \( \nZ \). Let \( p \in \{2, 3, 5, 7\} \). Then \( p \ge 2 \). Let \( d \) be a positive divisor of \( p \). Then \( 1 \le d \) by discreteness (@thm-integers-ordered-ring (c)) and \( d \le p \) by @prp-divisibility-rules-integers (e), so \( d \) is one of \( 1, 2, \dots, p \): applying discreteness repeatedly (if \( d \ne 1 \) then \( 2 \le d \); if \( d \ne 2 \) then \( 3 \le d \); and so on up to \( p \)) leaves no other value. Each \( d \) with \( 1 < d < p \) leaves a non-zero remainder:
\[
\begin{aligned}
3 &= 1 \cdot 2 + 1, \qquad 5 = 2 \cdot 2 + 1 = 1 \cdot 3 + 2 = 1 \cdot 4 + 1, \\
7 &= 3 \cdot 2 + 1 = 2 \cdot 3 + 1 = 1 \cdot 4 + 3 = 1 \cdot 5 + 2 = 1 \cdot 6 + 1 .
\end{aligned}
\]
(For \( p = 2 \) there is no such \( d \).) So \( d \nmid p \) for these \( d \), by the divisibility test after @thm-integers-division-remainder: \( p = kd \) would give \( p = kd + 0 \), a second division of \( p \) by \( d \), with remainder \( 0 \), against the uniqueness in @thm-integers-division-remainder (a). Hence the positive divisors of \( p \) are \( 1 \) and \( p \), and \( p \) is prime.
:::

The later sections of this chapter cite this paragraph as "the small-primes remark". The same procedure decides, for any given \( p \ge 2 \), whether \( p \) is prime; Section 3.3 shortens it.

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

::: {#exr-division-with-remainder-c1}
[C1: Division from the integer part]

Let \( a \in \nZ \) and \( n \in \nZ_{>0} \). Prove the existence half of @thm-integers-division-remainder (a) directly from @prp-rational-integer-part, without the set \( R \): put \( q \coloneqq \floor{a/n} \) and \( r \coloneqq a - qn \), and show that \( 0 \le r < n \). Say where \( n > 0 \) is used.
:::

::: {.solution}
By @prp-rational-integer-part, \( q \coloneqq \floor{a/n} \in \nZ \) satisfies
\[
q \le a/n < q + 1
\]
in \( \nQ \), where \( a/n = a \cdot n^{-1} \) and \( n \ne 0 \) in \( \nQ \). Since \( n > 0 \), multiplying by \( n \) preserves the strict inequality (@prp-ordered-ring-rules (c)) and the equality case, so
\[
qn \le (a \cdot n^{-1}) \cdot n = a < (q + 1)n = qn + n .
\]
Subtracting \( qn \) (that is, adding \( -qn \), (O3)) gives \( 0 \le a - qn < n \). Here \( r \coloneqq a - qn \) is an integer, and by @thm-rationals-ordered-field (b) the inequalities \( 0 \le r < n \), proved in \( \nQ \), hold in \( \nZ \). So \( a = qn + r \) with \( 0 \le r < n \).

The hypothesis \( n > 0 \) is used when multiplying by \( n \): for \( n < 0 \), multiplication reverses inequalities (@prp-ordered-ring-rules (d)), and the same \( q \) would give \( qn \ge a > qn + n \), so \( n < r \le 0 \) instead. (This exercise is practice with a result already proved; nothing later rests on it.)
:::

<!-- dependency ledger
prp-divisibility-rules-integers (proof): ring laws (F1)-(F7), (F9) of Z | thm-integers-commutative-ring (cited at the start of the proof)
prp-divisibility-rules-integers (proof): (h), exactly one of a > 0, -a > 0 for a != 0 | prp-order-from-positives (converse part, (P2)), thm-integers-ordered-ring (b), cited
prp-divisibility-rules-integers (proof): (e), b - a = ka + (-1)a = (k - 1)a | prp-ring-algebra (c), (F7), (F9), cited
prp-divisibility-rules-integers (proof): antisymmetry of <= on Z | prp-ordered-ring-rules (i) (total order, fd2 def-partial-order), cited
thm-integers-division-remainder (proof): a - an = a + a(-n) = a(1 - n) and a - 0 = a | prp-ring-algebra (c), (F7), (F9), prp-ring-algebra (b), (F6), cited
thm-integers-division-remainder (proof): -0 = 0 (in a - 0 = a and -n < -0 = 0) | 0 + 0 = 0 by (F3), uniqueness prp-ring-algebra (a), cited
thm-integers-division-remainder (proof): r - n >= 0 from r >= n | (F4) if r = n, prp-ordered-ring-rules (a) if r > n, cited
thm-integers-division-remainder (proof): r - n = a + (-1)(qn) + (-1)n = a + (-1)((q + 1)n) = a - (q + 1)n | -x = (-1)x by prp-ring-algebra (c), (F7); (F9), cited
thm-integers-division-remainder (proof): adding r - r' to 0 <= r' gives r - r' <= r; adding qn to 0 <= r < n | prp-ordered-ring-rules (b), cited
thm-integers-division-remainder (proof): integer sums, products and comparisons are the same in Q | prp-integers-embed-rationals, thm-rationals-ordered-field (b) (cited); identification of F3.2 §04
thm-integers-division-remainder (proof): qn * n^{-1} = q and (qn + n) n^{-1} = q + 1 | field laws of Q (thm-rationals-field via thm-rationals-ordered-field), (F5), (F8), (F9)
thm-integers-division-remainder (claim): (the paragraph after the proof) no r with 0 <= r < 0 | (O1)
thm-integers-division-remainder (claim): (remark) fd2's uniqueness argument is the one packaged as prp-divisibility-rules-integers (e) | read against fd2 F2.2 §02 thm-division-algorithm (meta-claim, checkable there)
cor-integers-even-odd (proof): 2 = 1 + 1 > 0 | prp-ordered-ring-rules (b), (e) (1 > 0)
cor-integers-even-odd (proof): (2q + 1)^2 = 4q^2 + 4q + 1 = 2(2q^2 + 2q) + 1 | prp-ring-algebra (d) with ring laws; numerals 4 = 2 * 2 computed in N (opening paragraph)
cor-integers-even-odd (proof): contraposition | fd1 (classical reasoning, F1.2), standard
cor-integers-even-odd (claim): (the paragraph after the proof) part (b) is fd1:thm-square-even-implies-even, (E1)-(E3) there; fd2 proved (E1), (E2) after fd2:thm-division-algorithm | read against fd1 F1.2 §01 and fd2 F2.2 §02 (compared, not used)
cor-integers-even-odd (claim): the classical parity proof can now be rerun on the constructed Q, with lowest terms from Section 3.3 | prp-rationals-lowest-terms (Section 3.3) and Exercise R3 of Section 3.5 (blueprint ch03.md; prose pointer within the chapter, nothing depends on it)
cor-integers-even-odd (claim): (the small-primes remark after it) d in {1, ..., p} from 1 <= d <= p | thm-integers-ordered-ring (c) applied repeatedly, cited
cor-integers-even-odd (claim): (the small-primes remark after it) the displayed divisions, e.g. 7 = 1 * 4 + 3 with 0 <= 3 < 4 | numerals computed in N via prp-naturals-embed-integers (opening paragraph); verify/ch03/thm-integers-division-remainder.py
cor-integers-even-odd (claim): (the small-primes remark after it) Section 3.3 shortens the primality check | the remark after lem-least-divisor-prime (03-unique-factorization; blueprint ch03.md S3 deviation), applied in B3 (prose pointer within the chapter)
prp-divisibility-rules-integers (example): (the instances before it and the paragraph after it) 3 | -12, -4 | 0, 0 | 0, 5 does not divide 12, 2 | -2 | 2 | numerals; verify/ch03/prp-divisibility-rules-integers.py
cor-integers-even-odd (proof): the identity for (2q + 1)^2 | verify/ch03/cor-integers-even-odd.py
exr-division-with-remainder-a1 (solution): 47 = 7 * 6 + 5, -47 = (-8) * 6 + 1 | numerals; verify/ch03/exr-division-with-remainder-a1.py
exr-division-with-remainder-b2 (solution): r in {0, 1, 2} from 0 <= r < 3 | discreteness, thm-integers-ordered-ring (c), as in cor-integers-even-odd (cited)
exr-division-with-remainder-c1 (solution): (a n^{-1}) n = a in Q | field laws of Q, (F5), (F8)
-->
