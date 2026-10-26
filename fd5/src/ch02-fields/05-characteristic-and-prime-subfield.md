# Integer Multiples, the Characteristic, and the Prime Subfield

Add \( 1 \) to itself in \( \nQ \) and the sums \( 1, 1 + 1, 1 + 1 + 1, \dots \) never return to \( 0 \). In \( \nF_2 \) two copies of \( 1 \) already give \( 0 \), and in \( \nF_p \) it takes \( p \) copies. This one number decides whether "\( 2x = 0 \), so \( x = 0 \)" is a valid step, and Section 2.4 showed that homomorphisms respect it: there is none from \( \nF_2 \) to \( \nQ \) (@exm-field-homomorphism-obstructions (ii)). This section names the number, the **characteristic**, proves that it is \( 0 \) or a prime, and uses it to find the smallest subfield of every field: a copy of \( \nQ \) or of exactly one \( \nF_p \).

Throughout, \( F \) and \( L \) are fields (@def-field), \( 0 \) and \( 1 \) are the zero and one of the field in play, and we write \( 1_F \) when two fields are in play at once.

## Integer multiples

The question "can \( 1 + 1 + \dots + 1 \) be \( 0 \)?" is about the elements \( n \cdot 1 \). For \( n \in \nN \) these are already defined in every commutative ring. *Number Systems: From \(\nN\) to \(\nR\)*, Section 2.4 ("Multiples") defines, for a commutative ring \( R \) and \( a \in R \), by recursion on \( \nN = \omega \),
\[
0 \cdot a \coloneqq 0 , \qquad (n + 1) \cdot a \coloneqq n \cdot a + a \quad (n \in \nN) .
\]
So \( 1 \cdot a = a \), \( 2 \cdot a = a + a \), and \( n \cdot a \) is the sum of \( n \) copies of \( a \). We need negative multiples too, because the divisibility arguments below write \( n = qc + r \) with \( q \) possibly negative.

**Negative multiples.** Every integer is \( m \) or \( -m \) for some \( m \in \nN \) (@fd3:prp-naturals-embed-integers (c)). For \( n \in \nZ \) with \( n < 0 \) we have \( -n > 0 \), so \( -n \in \nN \) by @fd3:thm-integers-ordered-ring (b), and we define
\[
n \cdot a \coloneqq -\bigl( (-n) \cdot a \bigr) .
\]
So \( (-3) \cdot a = -(a + a + a) \). Extending the convention of *Number Systems: From \(\nN\) to \(\nR\)*, Section 2.4 (there for natural numbers), a dot with an integer on its left always means this multiple, and the product of two ring elements is written by juxtaposition, \( ab \). When \( R = \nZ \) the two readings agree: for \( n \in \nN \) this is the remark after the definition of multiples in that section, and for \( n < 0 \), \( n \cdot a = -((-n)a) = -(-(na)) = na \) by @fd3:prp-ring-algebra (c) and (a).

The lemma below collects the rules for multiples. Parts (a)–(c) are the three identities that the linear-algebra volumes cite; part (d) extends everything to integer multiples.

::: {#lem-integer-multiples}
[Integer Multiples]

Let \( R \) be a commutative ring, \( a, b \in R \), and \( m, k \in \nN \).

::: {.enumerate options="label=(\alph*)"}
1. \( (m \cdot 1) + (k \cdot 1) = (m + k) \cdot 1 \).
2. \( (m \cdot 1)(k \cdot 1) = (mk) \cdot 1 \).
3. \( (m \cdot 1)\, a = m \cdot a \).
4. The identities (a)–(c) hold for **all** \( m, k \in \nZ \), and so do
\[
\begin{aligned}
(m + k) \cdot a &= m \cdot a + k \cdot a , & (-m) \cdot a &= -(m \cdot a) , \\
m \cdot (a + b) &= m \cdot a + m \cdot b , & (m \cdot a)\, b &= m \cdot (ab) , \\
(mk) \cdot a &= m \cdot (k \cdot a) . & &
\end{aligned}
\]
:::
:::

In words: integer multiples obey the rules one expects of "\( m \) copies of \( a \)", with signs behaving as in \( \nZ \). Since every field is a commutative ring (the remark after @def-field), the lemma holds in every field.

::: {.idea}
For natural numbers everything is one induction each, on the recursion that defines \( m \cdot a \): four rules for natural multiples (a sum law, a distributive law, a product law and a composition law) and then (a)–(c) as special cases with \( a = 1 \). Negative multiples are reduced to natural ones by writing an integer as a difference \( m_1 - m_2 \) of natural numbers; that bookkeeping is (d), and its proof is in the fold below.
:::

::: {.proof}
All inductions are @fd1:ax-induction, read on \( \nN = \omega \) through @fd3:cor-omega-identification (b). We first prove four rules for \( m, k \in \nN \).

*(i) \( (m + k) \cdot a = m \cdot a + k \cdot a \).* Induction on \( k \). For \( k = 0 \), \( (m + 0) \cdot a = m \cdot a = m \cdot a + 0 = m \cdot a + 0 \cdot a \) by (F3). If it holds for \( k \), then
\[
\begin{aligned}
(m + (k + 1)) \cdot a &= ((m + k) + 1) \cdot a = (m + k) \cdot a + a \\
&= (m \cdot a + k \cdot a) + a = m \cdot a + (k + 1) \cdot a ,
\end{aligned}
\]
by the recursion, the induction hypothesis, (F2) and the recursion again. (This is the sum law of @fd3:prp-ordered-ring-rules (h), whose proof uses no order.)

*(ii) \( m \cdot (a + b) = m \cdot a + m \cdot b \).* Induction on \( m \). For \( m = 0 \) both sides are \( 0 \) (with \( 0 + 0 = 0 \) by (F3)). If it holds for \( m \), then \( (m + 1) \cdot (a + b) = (m \cdot a + m \cdot b) + (a + b) = (m \cdot a + a) + (m \cdot b + b) \) by (F1) and (F2), which is \( (m + 1) \cdot a + (m + 1) \cdot b \).

*(iii) \( (m \cdot a) b = m \cdot (ab) \).* Induction on \( m \). For \( m = 0 \), \( (0 \cdot a) b = 0 b = 0 = 0 \cdot (ab) \) by @fd3:prp-ring-algebra (b) and (F6). If it holds for \( m \), then \( ((m + 1) \cdot a) b = (m \cdot a + a) b = (m \cdot a) b + ab = m \cdot (ab) + ab = (m + 1) \cdot (ab) \), by (F9) with (F6), and the induction hypothesis.

*(iv) \( (mk) \cdot a = m \cdot (k \cdot a) \).* Induction on \( m \). For \( m = 0 \) both sides are \( 0 \). If it holds for \( m \), then, since \( (m + 1)k = mk + k \) in \( \nN \),
\[
((m + 1)k) \cdot a = (mk + k) \cdot a = (mk) \cdot a + k \cdot a = m \cdot (k \cdot a) + k \cdot a = (m + 1) \cdot (k \cdot a) ,
\]
by (i), the induction hypothesis and the recursion.

Now (a) is (i) with \( a = 1 \). For (c), \( (m \cdot 1) a = m \cdot (1 a) = m \cdot a \) by (iii), then (F6) and (F7). For (b), \( (m \cdot 1)(k \cdot 1) = m \cdot (1 (k \cdot 1)) = m \cdot (k \cdot 1) = (mk) \cdot 1 \) by (iii), (F6) with (F7), and (iv). Part (d) is proved in the fold below. This proves the lemma.
:::

::: {.second-reading title="Proof of (d): from natural to integer multiples"}
::: {.idea}
Every integer is a difference \( m_1 - m_2 \) of natural numbers, and a negative multiple is the negative of a natural one. So each identity of (d) splits into identities for natural multiples, which are rules (i)–(iv), combined with the ring rules for negatives. Only the composition law needs the four sign cases separately, and a table keeps them apart.
:::

::: {.proof of="lem-integer-multiples"}
*Step 1: \( (-m) \cdot a = -(m \cdot a) \) for every \( m \in \nZ \).* If \( m > 0 \), then \( -m < 0 \) and the definition gives \( (-m) \cdot a = -((-(-m)) \cdot a) = -(m \cdot a) \). If \( m = 0 \), both sides are \( 0 \), since \( -0 = 0 \) (\( 0 + 0 = 0 \) and uniqueness of negatives, @fd3:prp-ring-algebra (a)). If \( m < 0 \), the definition gives \( m \cdot a = -((-m) \cdot a) \), so \( -(m \cdot a) = (-m) \cdot a \) because \( -(-x) = x \) (@fd3:prp-ring-algebra (a)).

*Step 2: \( (m - k) \cdot a = m \cdot a - k \cdot a \) for \( m, k \in \nN \).* If \( m \ge k \), then \( m - k \in \nN \) and \( (m - k) + k = m \), so \( m \cdot a = (m - k) \cdot a + k \cdot a \) by rule (i) of the proof above; adding \( -(k \cdot a) \) to both sides gives the claim. If \( m < k \), then by Step 1 and the first case
\[
(m - k) \cdot a = -\bigl( (k - m) \cdot a \bigr) = -\bigl( k \cdot a - m \cdot a \bigr) = m \cdot a - k \cdot a ,
\]
the last step because \( (k \cdot a - m \cdot a) + (m \cdot a - k \cdot a) = 0 \) by (F1)–(F4), and negatives are unique.

*Step 3: the sum, distributive and product rules.* By @fd3:prp-naturals-embed-integers (c), every integer is a difference \( m_1 - m_2 \) of natural numbers (\( m = m - 0 \), \( -m = 0 - m \)). Let \( x = m_1 - m_2 \) and \( y = k_1 - k_2 \) with \( m_1, m_2, k_1, k_2 \in \nN \). Then \( x + y = (m_1 + k_1) - (m_2 + k_2) \), and by Step 2 and rule (i),
\[
\begin{aligned}
(x + y) \cdot a &= (m_1 \cdot a + k_1 \cdot a) - (m_2 \cdot a + k_2 \cdot a) \\
&= (m_1 \cdot a - m_2 \cdot a) + (k_1 \cdot a - k_2 \cdot a) = x \cdot a + y \cdot a ,
\end{aligned}
\]
using \( -(u + v) = (-u) + (-v) \) (both are negatives of \( u + v \)) and (F1), (F2). In the same way, Step 2 with rules (ii) and (iii) gives \( x \cdot (a + b) = x \cdot a + x \cdot b \) and \( (x \cdot a) b = (m_1 \cdot a) b - (m_2 \cdot a) b = x \cdot (ab) \), the middle step by (F9) and \( (-u) b = -(ub) \) (@fd3:prp-ring-algebra (c)). From the distributive rule, \( x \cdot c + x \cdot (-c) = x \cdot 0 \), and \( x \cdot 0 = (x \cdot 1) 0 = 0 \) by the product rule just proved (with \( a = 1 \), \( b = 0 \)) and @fd3:prp-ring-algebra (b); so \( x \cdot (-c) = -(x \cdot c) \).

*Step 4: \( (xy) \cdot a = x \cdot (y \cdot a) \).* Write \( x = \pm m' \) and \( y = \pm k' \) with \( m', k' \in \nN \). In \( \nZ \), \( (-m')k' = m'(-k') = -(m'k') \) and \( (-m')(-k') = m'k' \) (@fd3:prp-ring-algebra (c)). Each row of the table reduces both sides to rule (iv), using Step 1 and the last line of Step 3.

| \( x \), \( y \) | \( (xy) \cdot a \) | \( x \cdot (y \cdot a) \) |
|---|---|---|
| \( m' \), \( k' \) | \( (m'k') \cdot a \) | \( m' \cdot (k' \cdot a) \) |
| \( -m' \), \( k' \) | \( -((m'k') \cdot a) \) | \( -(m' \cdot (k' \cdot a)) \) |
| \( m' \), \( -k' \) | \( -((m'k') \cdot a) \) | \( m' \cdot (-(k' \cdot a)) = -(m' \cdot (k' \cdot a)) \) |
| \( -m' \), \( -k' \) | \( (m'k') \cdot a \) | \( -(m' \cdot (-(k' \cdot a))) = m' \cdot (k' \cdot a) \) |

*Step 5: (a)–(c) for integers.* (a) is the sum rule with \( a = 1 \). (c): \( (x \cdot 1) a = x \cdot (1 a) = x \cdot a \). (b): \( (x \cdot 1)(y \cdot 1) = x \cdot (1 (y \cdot 1)) = x \cdot (y \cdot 1) = (xy) \cdot 1 \), by the product rule and Step 4. This proves (d).
:::
:::

Two readings of the lemma are used constantly. First, by (a) and (b) with (d), the map \( \nZ \to R \), \( n \mapsto n \cdot 1 \), turns sums of integers into sums in \( R \) and products into products, and sends \( 1 \) to \( 1 \cdot 1 = 1 \). Second, by (c) with (d), every multiple \( n \cdot a \) is a product in \( R \), namely \( (n \cdot 1) a \): to know how multiples behave, it is enough to know the elements \( n \cdot 1 \).

In \( \nZ/n\nZ \) these elements are the classes themselves: \( k \cdot [1] = [k] \) for \( k \in \nN \) (@thm-integers-mod-n-ring (d)), and for \( k < 0 \), \( k \cdot [1] = -((-k) \cdot [1]) = -[-k] = [k] \), since \( -[u] = [-u] \) in a quotient ring (@thm-quotient-ring-by-ideal (b)).

::: {.check}
In \( \nZ/5\nZ \), compute \( (-3) \cdot [2] \) in two ways: by the definition of a negative multiple, and by (c) of @lem-integer-multiples, extended to integers by (d).
:::

::: {.solution}
By the definition, \( (-3) \cdot [2] = -(3 \cdot [2]) = -([2] + [2] + [2]) = -[6] = [-6] = [4] \), since \( -6 - 4 = -10 \) is divisible by \( 5 \). By (c) and (d), \( (-3) \cdot [2] = ((-3) \cdot [1])[2] = [-3][2] = [-6] = [4] \), using \( k \cdot [1] = [k] \) for \( k = -3 \).
:::

## The characteristic

The elements \( 1, 2 \cdot 1, 3 \cdot 1, \dots \) of a field either never reach \( 0 \), or reach it for some positive \( n \). In the second case the first time they reach it is the number that matters.

*The characteristic counts how many copies of \( 1 \) add up to \( 0 \), and is \( 0 \) if no number of copies does.*

::: {#def-characteristic}
[Characteristic]

Let \( F \) be a field. If **there exists** a positive integer \( n \) with \( n \cdot 1 = 0 \), the **characteristic** of \( F \), written \( \operatorname{char} F \), is the **least** such \( n \). If there is none, \( \operatorname{char} F \coloneqq 0 \).
:::

In words: test \( n = 1, 2, 3, \dots \) in turn; \( \operatorname{char} F \) is the first \( n \) with \( n \cdot 1 = 0 \), and \( 0 \) if the test never stops. The same words define the characteristic of a commutative ring.

*Well-definedness.* If the set \( S \coloneqq \{ n \in \nZ_{>0} : n \cdot 1 = 0 \} \) is non-empty, it is a non-empty set of integers bounded below by \( 1 \), so it has a least element by @fd3:prp-integer-least-element. So "the least such \( n \)" names exactly one integer.

**First examples.**

- \( \nF_2 \): \( 1 \cdot 1 = 1 \ne 0 \) and \( 2 \cdot 1 = 1 + 1 = 0 \) by the table of @exm-finite-fields, so \( \operatorname{char} \nF_2 = 2 \).
- \( \nF_3 \): \( 1 \cdot 1 = 1 \), \( 2 \cdot 1 = 2 \), \( 3 \cdot 1 = 3 = 0 \), and \( 1, 2 \ne 0 \) in \( \nF_3 \), so \( \operatorname{char} \nF_3 = 3 \).
- \( \nQ \): \( n \cdot 1 = n \ne 0 \) for every \( n \ge 1 \), so \( \operatorname{char} \nQ = 0 \). The reason is the order of \( \nQ \); the example at the end of the next subsection gives it.
- The ring \( \nZ/6\nZ \), which is not a field: \( k \cdot [1] = [k] \ne [0] \) for \( k = 1, \dots, 5 \) and \( 6 \cdot [1] = [0] \), so it has characteristic \( 6 \).

*The degenerate case.* In the zero ring \( \{0\} \) of *Number Systems: From \(\nN\) to \(\nR\)*, Section 2.3, \( 1 = 0 \), so \( 1 \cdot 1 = 1 = 0 \) and the characteristic is \( 1 \). It is the only ring of characteristic \( 1 \): characteristic \( 1 \) means \( 1 = 1 \cdot 1 = 0 \), and then every \( a = a \cdot 1 = a \cdot 0 = 0 \) (@fd3:prp-ring-algebra (b)). It is not a field. For fields, the clause \( 1 \ne 0 \) of (F7) rules out characteristic \( 1 \), and that is the first step of the theorem below on which characteristics occur.

**Why \( 0 \) and not "infinity".** The convention \( \operatorname{char} F = 0 \) makes the next proposition read the same in every case: \( n \cdot 1 = 0 \) exactly when \( \operatorname{char} F \) divides \( n \). For \( \operatorname{char} F = 0 \) this says \( n \cdot 1 = 0 \) only for \( n = 0 \), because \( 0 \mid n \) only for \( n = 0 \) (@fd3:prp-divisibility-rules-integers (a)).

The proposition is the form in which the characteristic is used. Its proof is the move of Chapter 1: take the least positive element, then divide by it.

::: {#prp-characteristic-divides}
[The Characteristic Divides Every Vanishing Multiple]

Let \( F \) be a field, \( c \coloneqq \operatorname{char} F \), and \( n \in \nZ \).

::: {.enumerate options="label=(\alph*)"}
1. \( n \cdot 1 = 0 \) **if and only if** \( c \mid n \).
2. \( n \cdot 1 \) is invertible in \( F \) if and only if \( c \nmid n \). In particular \( 2 \coloneqq 1 + 1 \) is invertible in \( F \) if and only if \( \operatorname{char} F \ne 2 \).
:::
:::

::: {.idea}
For \( c > 0 \), divide \( n \) by \( c \) with remainder, \( n = qc + r \). The multiple \( c \cdot 1 \) is \( 0 \), so the rules of @lem-integer-multiples kill the part \( qc \) and leave \( n \cdot 1 = r \cdot 1 \). The remainder is smaller than \( c \), and \( c \) was the **least** positive integer with a vanishing multiple, so \( r \cdot 1 = 0 \) forces \( r = 0 \). For \( c = 0 \) there is nothing to divide: no positive multiple vanishes, and negatives follow by a sign.
:::

::: {.proof}
(a) *Case \( c = 0 \).* We show \( n \cdot 1 = 0 \) iff \( n = 0 \), which is the claim since \( 0 \mid n \) iff \( n = 0 \) (@fd3:prp-divisibility-rules-integers (a)). If \( n = 0 \), \( n \cdot 1 = 0 \). If \( n > 0 \), then \( n \cdot 1 \ne 0 \) by @def-characteristic, since \( c = 0 \) means no positive multiple vanishes. If \( n < 0 \), then \( n \cdot 1 = -((-n) \cdot 1) \) with \( (-n) \cdot 1 \ne 0 \); and \( -x = 0 \) would give \( x = -(-x) = -0 = 0 \) (@fd3:prp-ring-algebra (a)), so \( n \cdot 1 \ne 0 \).

*Case \( c > 0 \).* (\( \Leftarrow \)) If \( c \mid n \), say \( n = qc \) with \( q \in \nZ \), then by @lem-integer-multiples (b), which holds for integers by part (d),
\[
n \cdot 1 = (qc) \cdot 1 = (q \cdot 1)(c \cdot 1) = (q \cdot 1) \, 0 = 0 ,
\]
the last step by @thm-field-basic-properties (d) and (F6).

(\( \Rightarrow \)) Suppose \( n \cdot 1 = 0 \). By @fd3:thm-integers-division-remainder there are \( q, r \in \nZ \) with \( n = qc + r \) and \( 0 \le r < c \). By the sum rule of @lem-integer-multiples (d) and the computation just made,
\[
0 = n \cdot 1 = (qc) \cdot 1 + r \cdot 1 = 0 + r \cdot 1 = r \cdot 1 ,
\]
using (F1) and (F3) at the end. If \( r > 0 \), then \( r \) is a positive integer with \( r \cdot 1 = 0 \) and \( r < c \), against the minimality of \( c \) in @def-characteristic. So \( r = 0 \), and \( n = qc \), that is, \( c \mid n \).

(b) In a field an element is invertible if and only if it is non-zero: a non-zero element has an inverse by (F8), and \( 0 \) has none, since \( 0 \cdot y = 0 \ne 1 \) (@thm-field-basic-properties (d), and \( 1 \ne 0 \) by (F7)). So (b) is (a) negated. For \( n = 2 \): \( 2 \cdot 1 = (0 \cdot 1 + 1) + 1 = 1 + 1 \). The positive divisors of \( 2 \) are \( 1 \) and \( 2 \) (\( 2 \) is prime), and \( 0 \nmid 2 \); and \( c \ne 1 \), since \( 1 \cdot 1 = 1 \ne 0 \). So \( c \mid 2 \) iff \( c = 2 \), and \( 1 + 1 \) is invertible iff \( c \ne 2 \). This proves the proposition.
:::

This is the form the linear-algebra volumes use, in sentences such as "\( \operatorname{char} F \ne 2 \), so \( 2 \) is invertible" and "\( m \cdot 1 \) is invertible when \( \operatorname{char} F \nmid m \)". It also says that the integers \( n \) with \( n \cdot 1 = 0 \) are exactly the multiples of one integer, \( c \), with nothing else vanishing by accident.

::: {.warning}
In characteristic \( 2 \), \( 1 + 1 = 0 \), so \( -1 = 1 \) and \( x = -x \) for every \( x \). The familiar step "\( x = -x \), so \( 2x = 0 \), so \( x = 0 \)" divides by \( 2 = 1 + 1 \), which is \( 0 \) there. In \( \nF_2 \), the element \( 1 \) satisfies \( 1 = -1 \) and \( 1 \ne 0 \). This is why many later results, for instance about symmetric and alternating bilinear forms in the linear-algebra volumes, assume \( \operatorname{char} F \ne 2 \): by @prp-characteristic-divides (b), that is exactly the hypothesis that makes the step valid.
:::

::: {#exm-completing-square-f3}
[Completing the square in \( \nF_3 \)]

Solve \( x^2 + x + 1 = 0 \) in \( \nF_3 \) by completing the square.
:::

::: {.solution}
Since \( \operatorname{char} \nF_3 = 3 \ne 2 \) (the first examples above), \( 2 = 1 + 1 \) is invertible by @prp-characteristic-divides (b); indeed \( 2 \cdot 2 = 4 = 1 \), so \( 2^{-1} = 2 \). Also \( 4 = 1 \ne 0 \), so \( x^2 + x + 1 = 0 \) holds if and only if \( 4(x^2 + x + 1) = 0 \) (one direction by @thm-field-basic-properties (d) and (F6), the other by (f)). By @fd3:prp-ring-algebra (d), with the multiples regrouped by @lem-integer-multiples (b), (F5) and (F6), \( (2x + 1)^2 = 4x^2 + 4x + 1 \), so
\[
4(x^2 + x + 1) = (2x + 1)^2 + 3 = (2x + 1)^2 ,
\]
as \( 3 = 0 \) in \( \nF_3 \). So the equation says \( (2x + 1)^2 = 0 \), that is, \( 2x + 1 = 0 \) by @thm-field-basic-properties (f), and \( x = 2^{-1}(-1) = 2 \cdot 2 = 1 \) by @prp-field-linear-equation (a), using \( -1 = 2 \). Testing all three elements agrees: \( x = 0, 1, 2 \) give \( 1 \), \( 3 = 0 \) and \( 7 = 1 \). In \( \nF_2 \) the method stops at the first step: there \( 2 = 0 \) and \( 4 = 0 \), so multiplying by \( 4 \) cannot be undone and \( 2 \) has no inverse.
:::

The characteristics found so far are \( 0 \), \( 2 \) and \( 3 \), and the ring \( \nZ/6\nZ \) has characteristic \( 6 \). A field cannot.

::: {#thm-characteristic-prime}
[The Characteristic Is Zero or a Prime]

Let \( F \) be a field. Then \( \operatorname{char} F \) is \( 0 \) or a prime.
:::

::: {.idea}
This is the argument that showed \( \nZ/n\nZ \) is not a field for composite \( n \) (@thm-zp-field-iff-prime), run inside \( F \). If \( c = rs \) with smaller factors, then \( (r \cdot 1)(s \cdot 1) = c \cdot 1 = 0 \). A field has no zero divisors, so one of the two factors is already \( 0 \), at a multiple smaller than \( c \).
:::

::: {.proof}
Let \( c \coloneqq \operatorname{char} F \) and suppose \( c > 0 \). Since \( 1 \cdot 1 = 1 \ne 0 \) by (F7), \( c \ne 1 \), so \( c \ge 2 \). Suppose \( c \) is not prime. By @fd2:def-prime it has a positive divisor \( r \notin \{1, c\} \); write \( c = rs \) with \( s \in \nZ \). Then \( s > 0 \), as \( r, c > 0 \), and \( s \mid c \); \( r \le c \) and \( s \le c \) by @fd3:prp-divisibility-rules-integers (e); and \( s \ne 1 \), \( s \ne c \), since \( s = 1 \) would give \( r = c \) and \( s = c \) would give \( r = 1 \) (cancel \( c \ne 0 \) in \( \nZ \)). So \( 1 < r < c \) and \( 1 < s < c \). By @lem-integer-multiples (b),
\[
(r \cdot 1)(s \cdot 1) = (rs) \cdot 1 = c \cdot 1 = 0 ,
\]
so \( r \cdot 1 = 0 \) or \( s \cdot 1 = 0 \) by @thm-field-basic-properties (f). Either way a positive integer smaller than \( c \) has a vanishing multiple, against the minimality of \( c \). Hence \( c \) is prime. This proves the theorem.
:::

So the possible characteristics of fields are \( 0, 2, 3, 5, 7, 11, \dots \), and the example at the end of the next subsection shows that each of them occurs. The hypothesis "field" is used twice, at \( 1 \ne 0 \) and at "no zero divisors", and the ring \( \nZ/6\nZ \) shows the second cannot be dropped: there \( [2][3] = [0] \).

## The characteristic under subfields and homomorphisms

The characteristic is computed from \( 0 \), \( 1 \) and \( + \) alone. A subfield has the same three, and a homomorphism carries them over, so both must preserve it.

::: {#prp-characteristic-invariant}
[Subfields and Homomorphisms Preserve the Characteristic]

::: {.enumerate options="label=(\alph*)"}
1. If \( K \) is a subfield of \( L \), then \( \operatorname{char} K = \operatorname{char} L \).
2. If \( \varphi \colon F \to L \) is a homomorphism, then \( \operatorname{char} F = \operatorname{char} L \).
3. There is no homomorphism between two fields of different characteristic.
:::
:::

::: {.proof}
(a) By @prp-subfield-test (a), \( K \) has the zero \( 0_L \), the one \( 1_L \), and the restricted addition of \( L \). Hence \( n \cdot 1_K = n \cdot 1_L \) for every \( n \in \nN \), by induction (@fd1:ax-induction): both are \( 0_L \) at \( n = 0 \), and both add \( 1_L \) at each step. So the sets of positive \( n \) with \( n \cdot 1 = 0 \) are the same in \( K \) and in \( L \), and so are their least elements, or both sets are empty.

(b) For \( n \in \nN \), \( \varphi(n \cdot 1_F) = n \cdot \varphi(1_F) = n \cdot 1_L \) by @prp-field-homomorphism-properties (f) and @def-field-homomorphism. Since \( \varphi(0) = 0 \) (@prp-field-homomorphism-properties (a)) and \( \varphi \) is injective (part (c) there), \( n \cdot 1_F = 0 \) if and only if \( \varphi(n \cdot 1_F) = 0 \), that is, if and only if \( n \cdot 1_L = 0 \). As in (a), the two characteristics coincide.

(c) is (b) read contrapositively. This proves the proposition.
:::

Part (c) explains two of the obstructions of Section 2.4 at once: there is no homomorphism \( \nF_2 \to \nQ \) and none \( \nQ \to \nF_p \) (@exm-field-homomorphism-obstructions (ii), (iii)), because the characteristics are \( 2 \) and \( 0 \), and \( 0 \) and \( p \).

::: {#exm-characteristics}
[The characteristics of the standard fields]

Find the characteristic of every ordered field, of \( \nQ \) and \( \nR \), of \( \nC \), of \( \nF_p \) for a prime \( p \), and of \( \nQ(\sqrt 2) \) and \( \nQ(i) \).
:::

::: {.solution}
*Ordered fields.* Let \( F \) be an ordered field (@fd3:def-ordered-ring-and-field). Since \( 1 \ne 0 \), @fd3:prp-ordered-ring-rules (h) gives \( n \cdot 1 > 0 \) for every \( n \in \nN \) with \( n \ge 1 \); in particular \( n \cdot 1 \ne 0 \). So no positive multiple of \( 1 \) vanishes, and \( \operatorname{char} F = 0 \).

*\( \nQ \) and \( \nR \).* Both are ordered fields (@fd3:thm-rationals-ordered-field, @fd3:thm-reals-ordered-field), so both have characteristic \( 0 \). For \( \nR \) one can also use @prp-characteristic-invariant (a), as \( \nQ \) is a subfield of \( \nR \) (@exm-subfields-gaussian (iii)).

*\( \nC \).* The field \( \nR \) is a subfield of \( \nC \) (@exm-subfields-gaussian (iii)), so \( \operatorname{char} \nC = \operatorname{char} \nR = 0 \) by @prp-characteristic-invariant (a). This argument uses no order on \( \nC \).

*\( \nF_p \).* (In this section we keep the brackets on classes of \( \nF_p = \nZ/p\nZ \) wherever integers and their classes appear side by side, as in \( n \cdot [1] = [n] \); elsewhere elements of \( \nF_p \) are written without brackets, as in Section 2.2.) For \( n \in \nN \), \( n \cdot [1] = [n] \) (@thm-integers-mod-n-ring (d)), and \( [n] = [0] \) if and only if \( n \in p\nZ \), that is, \( p \mid n \) (@thm-quotient-ring-by-ideal (d)). A positive \( n \) with \( p \mid n \) has \( p \le n \) (@fd3:prp-divisibility-rules-integers (e)), and \( p \mid p \). So the least positive \( n \) with \( n \cdot [1] = [0] \) is \( p \), and \( \operatorname{char} \nF_p = p \).

*\( \nQ(\sqrt 2) \) and \( \nQ(i) \).* They are subfields of \( \nR \) and of \( \nC \) (@exm-q-sqrt2-field, @exm-subfields-gaussian (i)), so both have characteristic \( 0 \) by @prp-characteristic-invariant (a).

So every prime occurs as a characteristic, and so does \( 0 \). The four-element field of Section 2.2's Exercise C1 has characteristic \( 2 \); Exercise C3 below checks it, and nothing here depends on it.
:::

::: {.check}
What are \( \operatorname{char} \nF_7 \) and \( \operatorname{char} \nQ(\sqrt 2) \)? Is \( 7 \cdot [3] = [1] \) in \( \nF_5 \)?
:::

::: {.solution}
\( \operatorname{char} \nF_7 = 7 \) and \( \operatorname{char} \nQ(\sqrt 2) = 0 \) (@exm-characteristics). Yes: \( 7 \cdot [3] = (7 \cdot [1])[3] = [7][3] = [21] \) by @lem-integer-multiples (c), and \( [21] = [1] \) since \( 21 - 1 = 20 = 4 \cdot 5 \). Equivalently, \( 7 \cdot [3] = 2 \cdot [3] \) because \( 5 \cdot [3] = [0] \), and \( 2 \cdot [3] = [6] = [1] \).
:::

## The prime subfield

Section 2.3 defined the prime subfield of a field \( F \) as the smallest subfield, the intersection of all subfields of \( F \) (@def-prime-subfield), and promised to identify it. Every subfield contains \( 1 \), hence every \( n \cdot 1 \), hence every quotient \( (m \cdot 1)(n \cdot 1)^{-1} \) with \( n \cdot 1 \ne 0 \). The characteristic decides which of these quotients exist, and so which number system the prime subfield copies.

The identification goes through a homomorphism into \( F \), and the main point is that there is exactly one. For ordered fields this is *Number Systems: From \(\nN\) to \(\nR\)*, Chapter 4's embedding \( \iota_F \colon \nQ \to F \) (@fd3:thm-rationals-embed-ordered-field). We keep the name \( \iota_F \), and, as before, the brackets on the classes of \( \nF_p \).

::: {#thm-prime-subfield}
[The Prime Subfield]

Let \( F \) be a field and \( P \) its prime subfield (@def-prime-subfield).

::: {.enumerate options="label=(\alph*)"}
1. If \( \operatorname{char} F = p > 0 \), then \( \iota_F([n]) \coloneqq n \cdot 1 \) (\( n \in \nZ \)) is a well-defined homomorphism \( \iota_F \colon \nF_p \to F \). It is the **only** homomorphism \( \nF_p \to F \), and its image is \( P \). Hence \( P \cong \nF_p \).
2. If \( \operatorname{char} F = 0 \), then \( \iota_F(m/n) \coloneqq (m \cdot 1)(n \cdot 1)^{-1} \) (\( m \in \nZ \), \( n \in \nZ_{>0} \)) is a well-defined homomorphism \( \iota_F \colon \nQ \to F \). It is the **only** homomorphism \( \nQ \to F \), and its image is \( P \). Hence \( P \cong \nQ \).
:::
:::

In (a), \( p \) is prime by @thm-characteristic-prime, so \( \nF_p \) is a field (@def-field-fp) and "homomorphism \( \nF_p \to F \)" has a meaning.

*Try it first (ten minutes): a homomorphism \( \psi \colon \nQ \to F \) must send \( 1 \) to \( 1 \). Where must it send \( 3 \), \( -3 \) and \( 1/3 \)? What could go wrong with \( 1/3 \)?*

::: {.idea}
An attempt runs as follows. \( \psi(3) = \psi(1 + 1 + 1) = 1 + 1 + 1 = 3 \cdot 1 \), then \( \psi(-3) = -\psi(3) = (-3) \cdot 1 \), and \( \psi(1/3) \) must be the inverse of \( \psi(3) \), so \( \psi(1/3) = (3 \cdot 1)^{-1} \). The homomorphism has no freedom at all: it is determined by \( \psi(1) = 1 \), through sums, negatives and inverses. That gives **uniqueness**, and it also dictates the only possible formula, \( m/n \mapsto (m \cdot 1)(n \cdot 1)^{-1} \).

What can go wrong is \( 1/3 \): if \( 3 \cdot 1 = 0 \) in \( F \), it has no inverse, and no homomorphism exists. The characteristic says exactly when this happens. In characteristic \( 0 \) the formula makes sense, and what remains is to check that it does not depend on how a rational is written, which follows from @lem-integer-multiples (b) and a regrouping by (F5)–(F8), and that it respects \( + \) and \( \cdot \), which the fraction rules of @thm-field-basic-properties (g) give. In characteristic \( p \), the classes \( [n] \) play the role of the rationals, and \( p \cdot 1 = 0 \) is exactly what makes \( [n] \mapsto n \cdot 1 \) well defined. The image is then a subfield (Section 2.4) built from \( 1 \) alone, so it lies inside every subfield: it is the prime subfield.

*Before reading on: where is \( \operatorname{char} F = 0 \) used in (b), and why does the same formula fail for \( F = \nF_5 \)?*
:::

::: {.proof}
**Part (a).** Let \( \operatorname{char} F = p > 0 \).

*Well defined.* Every element of \( \nF_p \) is a class \( [n] \) with \( n \in \nZ \) (@fd2:def-quotient-set). If \( [n] = [n'] \), then \( p \mid n - n' \) (@thm-quotient-ring-by-ideal (a), for the ideal \( p\nZ \)), so \( (n - n') \cdot 1 = 0 \) by @prp-characteristic-divides (a), and \( n \cdot 1 - n' \cdot 1 = (n - n') \cdot 1 = 0 \) by @lem-integer-multiples (d). So \( n \cdot 1 = n' \cdot 1 \): the value does not depend on the representative. (This is @fd3:thm-well-defined-on-classes (a) with equality as the relation on \( F \), whose classes are the singletons \( \{y\} \), followed by \( \{y\} \mapsto y \).)

*Homomorphism.* For \( m, n \in \nZ \), by the operations of \( \nZ/p\nZ \) (@thm-quotient-ring-by-ideal (b)) and @lem-integer-multiples (d), parts (a) and (b) there,
\[
\begin{aligned}
\iota_F([m] + [n]) &= \iota_F([m + n]) = (m + n) \cdot 1 = m \cdot 1 + n \cdot 1 , \\
\iota_F([m][n]) &= \iota_F([mn]) = (mn) \cdot 1 = (m \cdot 1)(n \cdot 1) ,
\end{aligned}
\]
and \( \iota_F([1]) = 1 \cdot 1 = 1 \). So \( \iota_F \) is a homomorphism (@def-field-homomorphism).

*Image \( = P \).* The image \( \iota_F(\nF_p) \) is a subfield of \( F \) (@prp-field-homomorphism-properties (d)), and \( P \) is contained in every subfield (@def-prime-subfield), so \( P \subseteq \iota_F(\nF_p) \). Conversely, let \( K \) be any subfield of \( F \). It contains \( 0 \) and \( 1 \) and is closed under \( + \) (@def-subfield), so \( n \cdot 1 \in K \) for every \( n \in \nN \), by induction on \( n \) (@fd1:ax-induction): \( 0 \cdot 1 = 0 \in K \), and \( (n + 1) \cdot 1 = n \cdot 1 + 1 \in K \). It is closed under negatives, so \( n \cdot 1 = -((-n) \cdot 1) \in K \) for \( n < 0 \) as well. So \( \iota_F(\nF_p) \subseteq K \) for every subfield \( K \), that is, \( \iota_F(\nF_p) \subseteq P \).

*Uniqueness.* Let \( \psi \colon \nF_p \to F \) be a homomorphism and \( n \in \nZ \). Then \( [n] = n \cdot [1] \) (@thm-integers-mod-n-ring (d), extended to \( n < 0 \) after @lem-integer-multiples). For \( n \in \nN \), \( \psi(n \cdot [1]) = n \cdot \psi([1]) = n \cdot 1 \) by @prp-field-homomorphism-properties (f); for \( n < 0 \),
\[
\psi(n \cdot [1]) = \psi\bigl( -((-n) \cdot [1]) \bigr) = -\bigl( (-n) \cdot 1 \bigr) = n \cdot 1 ,
\]
by the definition of negative multiples at both ends, and in the middle by @prp-field-homomorphism-properties (a) followed by the case \( -n \in \nN \) just done. So \( \psi([n]) = n \cdot 1 = \iota_F([n]) \) for every \( n \), and \( \psi = \iota_F \).

Finally, \( \iota_F \) is an isomorphism from \( \nF_p \) onto its image \( P \) by @prp-field-homomorphism-properties (d), so \( P \cong \nF_p \).

**Part (b).** Let \( \operatorname{char} F = 0 \). Recall that \( \nQ = (\nZ \times \nZ_{>0})/{\sim} \) (@fd3:def-rationals-as-classes), that the class \( [(m, n)] \) is the quotient \( m/n \) of the integers \( m \) and \( n \) in \( \nQ \) (@fd3:prp-integers-embed-rationals (a)), and that for \( n, n' \in \nZ_{>0} \), \( m/n = m'/n' \) if and only if \( mn' = m'n \) (part (b) there).

*The formula makes sense.* For \( n > 0 \), \( n \cdot 1 \ne 0 \) by @prp-characteristic-divides (a), since \( 0 \nmid n \). So \( (n \cdot 1)^{-1} \) exists by (F8). This is the only place where \( \operatorname{char} F = 0 \) is used.

*Well defined.* Let \( m/n = m'/n' \) with \( n, n' > 0 \), so \( mn' = m'n \). By @lem-integer-multiples (d), part (b) there,
\[
(m \cdot 1)(n' \cdot 1) = (mn') \cdot 1 = (m'n) \cdot 1 = (m' \cdot 1)(n \cdot 1) .
\]
Multiply both sides by \( (n \cdot 1)^{-1} (n' \cdot 1)^{-1} \) and regroup by (F5), (F6), (F8) and (F7): the left side becomes \( (m \cdot 1)(n \cdot 1)^{-1} \) and the right side \( (m' \cdot 1)(n' \cdot 1)^{-1} \). So the value does not depend on the representative.

*Homomorphism.* Let \( m/n, r/s \in \nQ \) with \( n, s > 0 \), and put \( \bar m \coloneqq m \cdot 1 \), and likewise \( \bar n \), \( \bar r \), \( \bar s \). By @fd3:def-rational-operations, \( m/n + r/s = (ms + rn)/(ns) \) and \( (m/n)(r/s) = (mr)/(ns) \), with \( ns > 0 \). By @lem-integer-multiples (d), \( (ms + rn) \cdot 1 = \bar m \bar s + \bar r \bar n \), \( (mr) \cdot 1 = \bar m \bar r \) and \( (ns) \cdot 1 = \bar n \bar s \). So, by the fraction rules @thm-field-basic-properties (g) in \( F \) (with \( \bar n, \bar s \ne 0 \)),
\[
\begin{aligned}
\iota_F\Bigl( \frac{m}{n} + \frac{r}{s} \Bigr) &= \frac{\bar m \bar s + \bar n \bar r}{\bar n \bar s} = \frac{\bar m}{\bar n} + \frac{\bar r}{\bar s} , \\
\iota_F\Bigl( \frac{m}{n} \cdot \frac{r}{s} \Bigr) &= \frac{\bar m \bar r}{\bar n \bar s} = \frac{\bar m}{\bar n} \cdot \frac{\bar r}{\bar s} ,
\end{aligned}
\]
where \( x/y \coloneqq xy^{-1} \) in \( F \) and \( \bar r \bar n = \bar n \bar r \) by (F6). Also \( \iota_F(1) = \iota_F(1/1) = (1 \cdot 1)(1 \cdot 1)^{-1} = 1 \cdot 1^{-1} = 1 \). So \( \iota_F \) is a homomorphism.

*Image \( = P \).* As in (a), \( P \subseteq \iota_F(\nQ) \) because the image is a subfield. Conversely, every subfield \( K \) contains \( m \cdot 1 \) and \( n \cdot 1 \) (as in (a)), hence \( (n \cdot 1)^{-1} \), as \( n \cdot 1 \ne 0 \), and the product \( (m \cdot 1)(n \cdot 1)^{-1} \) (@def-subfield). So \( \iota_F(\nQ) \subseteq P \).

*Uniqueness.* Let \( \psi \colon \nQ \to F \) be a homomorphism. In \( \nQ \), the integer \( m \in \nZ \subseteq \nQ \) is the multiple \( m \cdot 1_{\nQ} \): the embedding \( j \) of @fd3:prp-integers-embed-rationals has \( j(0) = 0 \) and \( j(k + 1) = j(k) + 1 \), so \( j(k) = k \cdot 1_{\nQ} \) for \( k \in \nN \) by induction, and \( j(-k) = -j(k) = (-k) \cdot 1_{\nQ} \). As in (a), \( \psi(m \cdot 1_{\nQ}) = m \cdot 1 \) for every \( m \in \nZ \), by @prp-field-homomorphism-properties (f) and (a). For \( n > 0 \), \( m/n = m n^{-1} \) in \( \nQ \) with \( n \ne 0 \) (@fd3:prp-integers-embed-rationals (a)), so by @prp-field-homomorphism-properties (b),
\[
\psi\Bigl( \frac{m}{n} \Bigr) = \psi(m)\, \psi(n^{-1}) = \psi(m)\, \psi(n)^{-1} = (m \cdot 1)(n \cdot 1)^{-1} = \iota_F\Bigl( \frac{m}{n} \Bigr) .
\]
So \( \psi = \iota_F \). As in (a), \( \iota_F \) is an isomorphism onto \( P \), and \( P \cong \nQ \). This proves the theorem.
:::

*Answer to the prompt.* In (b), \( \operatorname{char} F = 0 \) is used only to know that \( n \cdot 1 \ne 0 \) for \( n > 0 \), so that \( (n \cdot 1)^{-1} \) exists; every other step works in any field. In \( F = \nF_5 \), \( 5 \cdot 1 = 0 \), so "\( 1/5 \mapsto (1 \cdot 1)(5 \cdot 1)^{-1} \)" names no element: the formula has no meaning there, which matches @exm-field-homomorphism-obstructions (iii), where no homomorphism \( \nQ \to \nF_p \) exists at all.

::: {.second-reading title="Two remarks on the formulas"}
Two consequences of the formulas are worth recording, though nothing below rests on them. For \( F = \nQ \), \( \iota_{\nQ}(m/n) = j(m) j(n)^{-1} = m/n \), so \( \iota_{\nQ} = \id_{\nQ} \); for \( F = \nF_p \), \( \iota_{\nF_p}([n]) = n \cdot [1] = [n] \), so \( \iota_{\nF_p} = \id_{\nF_p} \). And in (b) the formula also holds for negative denominators: if \( n < 0 \), then \( m/n = (-m)/(-n) \) with \( -n > 0 \), and \( ((-m) \cdot 1)((-n) \cdot 1)^{-1} = (-\bar m)(-\bar n)^{-1} = \bar m \bar n^{-1} \), because \( (-\bar n)^{-1} = -\bar n^{-1} \) (their product with \( -\bar n \) is \( \bar n \bar n^{-1} = 1 \) by @fd3:prp-ring-algebra (c)).
:::

::: {.remark}
For an ordered field \( F \), part (b) is @fd3:thm-rationals-embed-ordered-field, where order supplied \( n \cdot 1 > 0 \) (@fd3:prp-naturals-in-ordered-field); by uniqueness the two maps called \( \iota_F \) are the same map. Here the characteristic supplies the weaker fact \( n \cdot 1 \ne 0 \), which is all the construction needs. The same "no freedom on \( 1 \)" argument gave *Number Systems: From \(\nN\) to \(\nR\)*, Chapter 6's @fd3:prp-cof-map-fixes-rationals.
:::

The uniqueness half of the theorem is a rigidity statement. It says that a homomorphism has no choice on the prime subfield, and the next corollary spells this out.

::: {#cor-homomorphisms-fix-prime-subfield}
[Homomorphisms Respect the Prime Subfield]

::: {.enumerate options="label=(\alph*)"}
1. Let \( \varphi \colon F \to L \) be a homomorphism. Then \( \varphi \circ \iota_F = \iota_L \), and \( \varphi \) maps the prime subfield of \( F \) onto the prime subfield of \( L \).
2. The identity is the only homomorphism \( \nQ \to \nQ \), and the only homomorphism \( \nF_p \to \nF_p \) for each prime \( p \). In particular the only automorphism of \( \nQ \), and of \( \nF_p \), is the identity.
3. Every automorphism of a field \( F \) fixes each element of the prime subfield of \( F \).
:::
:::

::: {.proof}
(a) By @prp-characteristic-invariant (b), \( \operatorname{char} F = \operatorname{char} L \), so \( \iota_F \) and \( \iota_L \) have the same domain \( D \), which is \( \nQ \) or \( \nF_p \) by @thm-prime-subfield. The composite \( \varphi \circ \iota_F \colon D \to L \) is a homomorphism (@prp-field-homomorphism-properties (e)), so it equals \( \iota_L \) by the uniqueness clause of @thm-prime-subfield. Hence \( \varphi(\iota_F(D)) = \iota_L(D) \), and by @thm-prime-subfield these images are the prime subfields of \( F \) and of \( L \).

(b) The identity \( \id_{\nQ} \) is a homomorphism (@prp-field-homomorphism-properties (e)), and \( \operatorname{char} \nQ = 0 \) (@exm-characteristics), so by the uniqueness clause of @thm-prime-subfield (b) with \( F = \nQ \), every homomorphism \( \nQ \to \nQ \) equals \( \id_{\nQ} \). Likewise for \( \nF_p \), using \( \operatorname{char} \nF_p = p \) and part (a) of the theorem. An automorphism is a homomorphism, so it is the identity.

(c) Let \( \sigma \) be an automorphism of \( F \). By (a) with \( L = F \), \( \sigma \circ \iota_F = \iota_F \), so \( \sigma(x) = x \) for every \( x = \iota_F(d) \) in the image of \( \iota_F \), which is the prime subfield. This proves the corollary.
:::

For instance, complex conjugation fixes every rational number, and the automorphisms of \( \nQ(\sqrt 2) \) and of \( \nQ(i) \) in Section 2.4 had no choice on \( \nQ \); only the images of \( \sqrt 2 \) and of \( i \) were free.

Finite fields are the case that matters most for computation, and for them the characteristic cannot be \( 0 \).

::: {#cor-finite-field-prime-characteristic}
[A Finite Field Has Prime Characteristic]

Let \( F \) be a finite field.

::: {.enumerate options="label=(\alph*)"}
1. \( \operatorname{char} F \) is a prime \( p \).
2. \( F \) contains a subfield isomorphic to \( \nF_p \), namely its prime subfield.
3. \( p \cdot a = 0 \) for every \( a \in F \).
:::
:::

::: {.proof}
(a) Say \( F \) has \( N \) elements (@fd2:def-finite). Suppose \( \operatorname{char} F = 0 \), and consider \( f \colon \{1, \dots, N + 1\} \to F \), \( f(k) \coloneqq k \cdot 1 \). If \( k \cdot 1 = k' \cdot 1 \), then \( (k - k') \cdot 1 = 0 \) (@lem-integer-multiples (d)), so \( 0 \mid k - k' \) by @prp-characteristic-divides (a), hence \( k - k' = 0 \) (@fd3:prp-divisibility-rules-integers (a)) and \( k = k' \). So \( f \) is an injection from a set with \( N + 1 \) elements into a set with \( N \) elements, which @fd2:cor-pigeonhole-finite-sets (a) forbids. Hence \( \operatorname{char} F \ne 0 \), and \( \operatorname{char} F \) is a prime by @thm-characteristic-prime.

(b) is @thm-prime-subfield (a).

(c) By @lem-integer-multiples (c), \( p \cdot a = (p \cdot 1) a = 0 \cdot a = 0 \), using @thm-field-basic-properties (d). This proves the corollary.
:::

A finite field therefore contains one of the fields \( \nF_p \) of Section 2.2. One can show that it has \( p^n \) elements for some \( n \ge 1 \); that needs the vector spaces of the linear-algebra volumes, and nothing in this volume uses it.

::: {.check}
Can a field with \( 6 \) elements contain a copy of \( \nF_2 \) and also a copy of \( \nF_3 \)?
:::

::: {.solution}
No. A copy of \( \nF_2 \) is a subfield \( K \) with \( \operatorname{char} K = 2 \), and a copy of \( \nF_3 \) a subfield with characteristic \( 3 \) (@exm-characteristics, @prp-characteristic-invariant (b) for the isomorphisms). By @prp-characteristic-invariant (a) both characteristics equal \( \operatorname{char} F \), and \( 2 \ne 3 \). (In fact no field has \( 6 \) elements, but that is the \( p^n \) fact just mentioned, which we do not prove.)
:::

## Exercises

### A. Check your understanding

::: {#exr-characteristic-and-prime-subfield-a1}
[A1]

These parts are about the proof of @thm-prime-subfield.

::: {.enumerate options="label=(\alph*)"}
1. In the proof of part (b), where is the hypothesis \( \operatorname{char} F = 0 \) used, and where is it not needed?
2. Try to define \( \nQ \to \nF_5 \) by \( m/n \mapsto [m][n]^{-1} \) (\( n > 0 \)). Name a rational number that has no image, and explain why the rule also fails to be well defined.
3. What are \( \iota_{\nR} \) and \( \iota_{\nC} \)? Justify your answer from the uniqueness clause.
4. State the idea of the proof in two sentences.
:::
:::

::: {.solution}
(a) Only in the step "the formula makes sense": \( n \cdot 1 \ne 0 \) for \( n > 0 \) (@prp-characteristic-divides (a)), so \( (n \cdot 1)^{-1} \) exists. Well-definedness, the homomorphism property, the image and uniqueness are computations in an arbitrary field once these inverses exist.

(b) \( 1/5 \): its image would be \( [1][5]^{-1} \), and \( [5] = [0] \) has no inverse. The rule is not even well defined on the rationals where it seems to make sense: \( 1 = 1/1 = 5/5 \), and the representative \( (5, 5) \) gives \( [5][5]^{-1} \), which does not exist, while \( (1, 1) \) gives \( [1] \).

(c) Both are inclusions. \( \nQ \) is a subfield of \( \nR \) and \( \nR \) of \( \nC \) (@exm-subfields-gaussian (iii)), so \( \nQ \) is a subfield of \( \nC \), and the inclusion of a subfield is a homomorphism (@exm-complex-conjugation-automorphism (ii)). By the uniqueness clause of @thm-prime-subfield (b) (both fields have characteristic \( 0 \), @exm-characteristics), \( \iota_{\nR} \) and \( \iota_{\nC} \) are these inclusions, \( q \mapsto q \).

(d) A homomorphism out of \( \nQ \) or \( \nF_p \) is forced by \( 1 \mapsto 1 \) to send \( m/n \) to \( (m \cdot 1)(n \cdot 1)^{-1} \) (or \( [n] \) to \( n \cdot 1 \)), so there is at most one, and its image lies in every subfield. The characteristic decides whether this forced formula makes sense, and when it does, the fraction rules show it is a homomorphism, whose image is then the prime subfield.
:::

### B. Practice

::: {#exr-characteristic-and-prime-subfield-b1}
[B1: Reducing multiples]

Let \( F \) be a field of characteristic \( p > 0 \) and \( a \in F \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( (p - 1) \cdot a = -a \).
2. Show that \( (kp + r) \cdot a = r \cdot a \) for all \( k, r \in \nZ \).
3. In \( \nF_7 \), compute \( 100 \cdot [3] \) directly, and again using (b).
:::
:::

::: {.solution}
(a) By @lem-integer-multiples (d) and (c), \( (p - 1) \cdot a + a = (p - 1) \cdot a + 1 \cdot a = p \cdot a = (p \cdot 1) a = 0 \cdot a = 0 \), using @thm-field-basic-properties (d). By uniqueness of negatives (@thm-field-basic-properties (c)), \( (p - 1) \cdot a = -a \).

(b) By @lem-integer-multiples (d), \( (kp + r) \cdot a = (kp) \cdot a + r \cdot a = k \cdot (p \cdot a) + r \cdot a \). Now \( p \cdot a = 0 \) as in (a), and \( k \cdot 0 = (k \cdot 1) 0 = 0 \) by @lem-integer-multiples (c) with (d) and @thm-field-basic-properties (d). So \( (kp + r) \cdot a = 0 + r \cdot a = r \cdot a \).

(c) Directly: \( 100 \cdot [3] = (100 \cdot [1])[3] = [100][3] = [300] \) (@lem-integer-multiples (c), @thm-integers-mod-n-ring (d)), and \( 300 = 42 \cdot 7 + 6 \), so \( 100 \cdot [3] = [6] \). By (b): \( 100 = 14 \cdot 7 + 2 \), so \( 100 \cdot [3] = 2 \cdot [3] = [6] \). The two agree.
:::

::: {#exr-characteristic-and-prime-subfield-b2}
[B2: Completing the square]

Let \( F \) be a field with \( \operatorname{char} F \ne 2 \), and write \( 2 \coloneqq 2 \cdot 1 \), \( 4 \coloneqq 4 \cdot 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( x = -x \) implies \( x = 0 \), for \( x \in F \).
2. Let \( b, c \in F \). Show that the equation \( x^2 + bx + c = 0 \) has a solution \( x \in F \) if and only if \( b^2 - 4c = s^2 \) for some \( s \in F \), and that then its solutions are exactly \( x = (-b + s)/2 \) and \( x = (-b - s)/2 \).
3. Use (b) to solve \( x^2 + x + 1 = 0 \) in \( \nF_7 \).
4. Explain why (b) says nothing in \( \nF_2 \), and show that its conclusion is in fact false there.
:::
:::

::: {.solution}
By @prp-characteristic-divides (b), \( 2 \ne 0 \), so \( 2 \) is invertible; and \( 4 = (2 \cdot 2) \cdot 1 = 2 \cdot 2 \ne 0 \) by @lem-integer-multiples (b) and @thm-field-basic-properties (f). For \( u \in F \), \( 2u = (2 \cdot 1)u = u + u \) by @lem-integer-multiples (c).

(a) If \( x = -x \), then \( 2x = x + x = x + (-x) = 0 \). Since \( 2 \ne 0 \), \( x = 0 \) by @thm-field-basic-properties (f).

(b) Since \( 4 \ne 0 \), \( x^2 + bx + c = 0 \) if and only if \( 4(x^2 + bx + c) = 0 \) (one direction by @thm-field-basic-properties (d) and (F6), the other by (f)). By @fd3:prp-ring-algebra (d), \( (2x + b)^2 = (2x)^2 + 2(2x)b + b^2 = 4x^2 + 4bx + b^2 \), the products of the multiples regrouped by @lem-integer-multiples (b), (F5) and (F6). Hence, with \( D \coloneqq b^2 - 4c \),
\[
4(x^2 + bx + c) = (2x + b)^2 - D ,
\]
and the equation is equivalent to \( (2x + b)^2 = D \). (Multiplying this identity by \( 4^{-1} \) gives the familiar \( x^2 + bx + c = (x + b/2)^2 - D/4 \).) If \( x \) is a solution, \( s \coloneqq 2x + b \) has \( s^2 = D \). Conversely, if \( s^2 = D \), then by @cor-field-squares-equal, \( (2x + b)^2 = s^2 \) if and only if \( 2x + b = s \) or \( 2x + b = -s \), and by @prp-field-linear-equation (a) (with \( 2 \ne 0 \)) these say \( x = (-b + s)/2 \) or \( x = (-b - s)/2 \).

(c) Here \( b = c = 1 \) and \( D = 1 - 4 = -3 = 4 = 2^2 \) in \( \nF_7 \), so \( s = 2 \); and \( 2^{-1} = 4 \), since \( 2 \cdot 4 = 8 = 1 \). The solutions are \( x = 4(-1 + 2) = 4 \) and \( x = 4(-1 - 2) = -12 = 2 \). Check: \( 4^2 + 4 + 1 = 21 = 0 \) and \( 2^2 + 2 + 1 = 7 = 0 \) in \( \nF_7 \). This agrees with @exr-finite-fields-from-modular-arithmetic-c3, found there by trying all seven elements.

(d) In \( \nF_2 \), \( 2 = 0 \) and \( 4 = 0 \), so the first step, "\( x^2 + bx + c = 0 \) iff \( 4(\dots) = 0 \)", fails, and \( /2 \) has no meaning. The conclusion of (b) is false there: for \( x^2 + x + 1 = 0 \), \( D = 1 - 0 = 1 = 1^2 \) is a square, yet the equation has no solution, since \( x = 0 \) and \( x = 1 \) both give \( 1 \).
:::

::: {#exr-characteristic-and-prime-subfield-b3}
[B3: When the integers embed]

Let \( F \) be a field.

::: {.enumerate options="label=(\alph*)"}
1. Show that for \( n, n' \in \nZ \), \( n \cdot 1 = n' \cdot 1 \) if and only if \( \operatorname{char} F \mid n - n' \).
2. Deduce that the map \( \nZ \to F \), \( n \mapsto n \cdot 1 \), is injective if \( \operatorname{char} F = 0 \), and is not injective if \( \operatorname{char} F = p > 0 \).
:::
:::

::: {.solution}
(a) By @lem-integer-multiples (d), \( n \cdot 1 - n' \cdot 1 = (n - n') \cdot 1 \). So \( n \cdot 1 = n' \cdot 1 \) iff \( (n - n') \cdot 1 = 0 \), iff \( \operatorname{char} F \mid n - n' \) by @prp-characteristic-divides (a).

(b) If \( \operatorname{char} F = 0 \) and \( n \cdot 1 = n' \cdot 1 \), then \( 0 \mid n - n' \) by (a), so \( n - n' = 0 \) (@fd3:prp-divisibility-rules-integers (a)) and \( n = n' \). If \( \operatorname{char} F = p > 0 \), then \( p \cdot 1 = 0 = 0 \cdot 1 \) with \( p \ne 0 \), so the map is not injective.
:::

### C. Going deeper

::: {#exr-characteristic-and-prime-subfield-c1}
[C1: Exit check: the characteristic]

Using only @def-characteristic, @lem-integer-multiples, division with remainder in \( \nZ \), @fd2:def-prime and the rules for divisibility in \( \nZ \) (@fd3:prp-divisibility-rules-integers), and the field axioms with @thm-field-basic-properties, prove:

::: {.enumerate options="label=(\alph*)"}
1. for a field \( F \) and \( n \in \nZ \), \( n \cdot 1 = 0 \) if and only if \( \operatorname{char} F \mid n \);
2. \( \operatorname{char} F \) is \( 0 \) or a prime.
:::
:::

::: {.solution}
(a) Let \( c \coloneqq \operatorname{char} F \).

*Case \( c = 0 \).* No positive \( n \) has \( n \cdot 1 = 0 \), by @def-characteristic. For \( n < 0 \), \( n \cdot 1 = -((-n) \cdot 1) \), and \( (-n) \cdot 1 \ne 0 \); since \( -x = 0 \) implies \( x = -(-x) = 0 \), also \( n \cdot 1 \ne 0 \). And \( 0 \cdot 1 = 0 \). So \( n \cdot 1 = 0 \) iff \( n = 0 \), iff \( 0 \mid n \) (@fd3:prp-divisibility-rules-integers (a)).

*Case \( c > 0 \).* Divide: \( n = qc + r \) with \( q, r \in \nZ \), \( 0 \le r < c \) (@fd3:thm-integers-division-remainder). By @lem-integer-multiples (d), \( (qc) \cdot 1 = (q \cdot 1)(c \cdot 1) = (q \cdot 1) 0 = 0 \) and \( n \cdot 1 = (qc) \cdot 1 + r \cdot 1 = r \cdot 1 \). If \( c \mid n \), then \( r = 0 \) by uniqueness of the remainder, so \( n \cdot 1 = 0 \cdot 1 = 0 \). If \( n \cdot 1 = 0 \), then \( r \cdot 1 = 0 \) with \( 0 \le r < c \); \( r > 0 \) would contradict the minimality of \( c \), so \( r = 0 \) and \( c \mid n \).

(b) Let \( c > 0 \). As \( 1 \cdot 1 = 1 \ne 0 \), \( c \ge 2 \). If \( c \) were not prime, by @fd2:def-prime it would have a positive divisor \( r \notin \{1, c\} \); write \( c = rs \). Then \( s > 0 \), \( r, s \le c \) by @fd3:prp-divisibility-rules-integers (e), and \( s \notin \{1, c\} \), since \( s = 1 \) gives \( r = c \) and \( s = c \) gives \( r = 1 \) (cancel \( c \ne 0 \)). So \( 1 < r, s < c \), and \( (r \cdot 1)(s \cdot 1) = (rs) \cdot 1 = 0 \) by @lem-integer-multiples (b), so \( r \cdot 1 = 0 \) or \( s \cdot 1 = 0 \) (@thm-field-basic-properties (f)), contradicting the minimality of \( c \). So \( c \) is prime.

**Marking scheme.** (10 points)

- 2: the case \( c = 0 \), including negative \( n \) (a negative multiple is the negative of a non-zero element, hence non-zero).
- 3: division of \( n \) by \( c \) with remainder, and \( n \cdot 1 = r \cdot 1 \) justified by the rules for multiples and \( c \cdot 1 = 0 \).
- 2: minimality of \( c \) forces \( r = 0 \); the converse \( c \mid n \Rightarrow n \cdot 1 = 0 \).
- 1: \( c \ne 1 \) from \( 1 \ne 0 \).
- 2: a factorization \( c = rs \) with \( 1 < r, s < c \), bounds justified, gives \( (r \cdot 1)(s \cdot 1) = 0 \), and the absence of zero divisors contradicts minimality.

Fatal errors (0 for the step): "\( c \cdot 1 = 0 \), so \( c \mid n \)" for every \( n \) with \( n \cdot 1 = 0 \), without the division step; treating \( n \cdot 1 \) as the integer \( n \) (for instance "\( n \cdot 1 = 0 \), so \( n = 0 \)" in \( \nF_p \)).
:::

::: {#exr-characteristic-and-prime-subfield-c2}
[C2: Find the error]

Here is an argument.

> *Claim.* A finite field \( F \) has prime characteristic.
>
> *Proof.* (1) The elements \( 1 \cdot 1, 2 \cdot 1, 3 \cdot 1, \dots \) of \( F \) cannot all be different, since \( F \) is finite. (2) So \( m \cdot 1 = k \cdot 1 \) for some positive integers \( k < m \). (3) Hence \( (m - k) \cdot 1 = m \cdot 1 - k \cdot 1 = 0 \). (4) So \( m - k \) is the characteristic of \( F \), and it is prime by @thm-characteristic-prime.

Is the conclusion true? Does the argument prove it? Name the failing step, say what is wrong with it, and give a counterexample to the step.
:::

::: {.solution}
*The conclusion is true:* it is @cor-finite-field-prime-characteristic (a). Steps (1) and (2) are correct (they are the pigeonhole argument of that proof, @fd2:cor-pigeonhole-finite-sets), and so is step (3), by @lem-integer-multiples (d). Step (4) fails.

*Step (4).* The argument only produces **some** positive integer with a vanishing multiple. The characteristic is the **least** one (@def-characteristic), and \( m - k \) need not be least: in \( \nF_3 \), \( 7 \cdot 1 = 1 = 1 \cdot 1 \) gives \( m - k = 6 \), while \( \operatorname{char} \nF_3 = 3 \). The step cites a property, "is the characteristic", that no line supplies, which is (N9) of @fd1:exm-not-allowed-catalogue.

*Repair.* By (2) and @lem-integer-multiples (d), \( (m - k) \cdot 1 = 0 \) with \( m - k > 0 \), so the set of positive integers with a vanishing multiple is non-empty and \( \operatorname{char} F > 0 \) (@def-characteristic); then @thm-characteristic-prime makes it prime.

**Marking scheme.** (10 points)

- 2: the conclusion is true, with the reference.
- 2: steps (1)–(3) are correct (including \( (m - k) \cdot 1 = 0 \) via @lem-integer-multiples (d)).
- 6: step (4) named: only some positive multiple vanishes, the characteristic is the least one (@def-characteristic), with a counterexample to the step.
:::

::: {#exr-characteristic-and-prime-subfield-c3}
[C3: The four-element field]

Let \( F = \{0, 1, \alpha, \beta\} \) be the four-element field of @exr-finite-fields-from-modular-arithmetic-c1, with \( \beta = 1 + \alpha \), \( \alpha^2 = \beta \) and \( \alpha\beta = 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \operatorname{char} F = 2 \).
2. Show that the prime subfield of \( F \) is \( \{0, 1\} \), and that it is isomorphic to \( \nF_2 \).
3. Show that the map \( F \to F \), \( x \mapsto x^2 \), is an automorphism of \( F \) that exchanges \( \alpha \) and \( \beta \).
:::
:::

::: {.solution}
(a) \( 1 \cdot 1 = 1 \ne 0 \), and \( 2 \cdot 1 = 1 + 1 = (1 + 1) + (0 + 0)\alpha = 0 \) by the addition rule of @exr-finite-fields-from-modular-arithmetic-c1, coefficient by coefficient in \( \nF_2 \). So \( \operatorname{char} F = 2 \).

(b) By @thm-prime-subfield (a), the prime subfield is the image of \( \iota_F \colon \nF_2 \to F \), which is \( \{0 \cdot 1, 1 \cdot 1\} = \{0, 1\} \), and \( \iota_F \) is an isomorphism from \( \nF_2 \) onto it.

(c) Let \( s(x) \coloneqq x^2 \). For \( x, y \in F \), \( (x + y)^2 = x^2 + 2xy + y^2 \) by @fd3:prp-ring-algebra (d), where \( 2xy = (1 + 1)(xy) = 0\,(xy) = 0 \), since \( 1 + 1 = 2 \cdot 1 = 0 \) by part (a) and \( 0\,(xy) = 0 \) by @thm-field-basic-properties (d); so \( s(x + y) = s(x) + s(y) \). Next \( (xy)^2 = (xy)(xy) = (xx)(yy) = x^2 y^2 \) by (F5) and (F6), and \( 1^2 = 1 \). So \( s \) is a homomorphism (@def-field-homomorphism). Its values are
\[
s(0) = 0 , \quad s(1) = 1 , \quad s(\alpha) = \alpha^2 = \beta , \quad s(\beta) = (1 + \alpha)^2 = 1 + \alpha^2 = 1 + \beta = \alpha ,
\]
using the additivity just proved and \( 1 + \beta = 1 + 1 + \alpha = \alpha \). So \( s \) permutes the four elements, is bijective, and is an automorphism exchanging \( \alpha \) and \( \beta \). (The next section shows that \( x \mapsto x^p \) is a homomorphism in every field of characteristic \( p \), and an automorphism when the field is finite.)
:::

<!-- dependency ledger
lem-integer-multiples (proof): (m + 1)k = mk + k, m - k in N for m >= k with (m - k) + k = m, the sum n + 1 in N and Z agree | arithmetic of omega, fd3:cor-omega-identification (c) with fd3:prp-naturals-embed-integers (a); fd2:lem-naturals-arithmetic read on omega
lem-integer-multiples (proof): -0 = 0; -(u + v) = (-u) + (-v); -(x - y) = y - x | uniqueness of negatives, fd3:prp-ring-algebra (a); inline
lem-integer-multiples (proof): in Z, (-m)k = m(-k) = -(mk), (-m)(-k) = mk; m < 0 implies -m in N | fd3:prp-ring-algebra (c); fd3:thm-integers-ordered-ring (b), cited (paragraph before the lemma)
lem-integer-multiples (claim): (paragraph before it) n . a = na in Z for n < 0 | fd3:prp-ring-algebra (c), (a); F3.2 Section 2.4 remark for n in N (cited by position)
lem-integer-multiples (claim): (quick check) (-3).[2] = [4] in Z/5Z | inline; verify/ch02/lem-integer-multiples.py
def-characteristic (example): char F2 = 2, char F3 = 3, Z/6Z has characteristic 6, zero ring characteristic 1 | exm-finite-fields table; thm-integers-mod-n-ring (d); verify/ch02/def-characteristic.py
def-characteristic (claim): first examples, char Q = 0 | forward pointer to exm-characteristics in the same section, not used as a reason before it
prp-characteristic-divides (proof): positive divisors of 2 are 1 and 2 | 2 prime, fd2:def-prime (the example after it)
thm-characteristic-prime (proof): r != 1, r <= c, r != c gives 1 < r < c | discreteness of Z, fd3:thm-integers-ordered-ring (c) (via fd3:prp-integer-least-element's setting); fd3:prp-divisibility-rules-integers (e), cited
thm-characteristic-prime (proof): s > 0 from r, c > 0 (s = 0 gives c = 0; s < 0 gives rs < 0); rc = c with c != 0 gives r = 1 | fd3:prp-ordered-ring-rules (c), (f) on Z (fd3:thm-integers-ordered-ring)
exm-completing-square-f3 (solution): 2.2 = 4 = 1, 3 = 0 in F3; 4(x^2 + x + 1) = (2x + 1)^2; root 1; values 1, 3, 7 | verify/ch02/exm-completing-square-f3.py
prp-characteristic-invariant (proof): induction on n | fd1:ax-induction read on omega (fd3:cor-omega-identification (b))
exm-characteristics (example): R is an ordered field; Q subfield of R; R subfield of C | fd3:thm-reals-ordered-field (F3.10, soft); exm-subfields-gaussian (iii); F4.1 labels through it (soft, example only)
exm-characteristics (example): four-element field has characteristic 2 | exr-finite-fields-from-modular-arithmetic-c1 and exr-characteristic-and-prime-subfield-c3; named only, nothing rests on it
thm-prime-subfield (proof): every element of F_p is a class [n] | fd2:def-quotient-set, cited
thm-prime-subfield (proof): the regrouping (m.1)(n'.1) = (m'.1)(n.1) implies (m.1)(n.1)^{-1} = (m'.1)(n'.1)^{-1} | (F5)-(F8), done inline (the computation of exr-field-axioms-b2, not cited)
thm-prime-subfield (proof): psi(m/n) = psi(m) psi(n)^{-1} | prp-field-homomorphism-properties (b) and multiplicativity, inline (the computation of exr-field-homomorphisms-b1, not cited)
thm-prime-subfield (proof): j(k) = k . 1_Q by induction | fd3:prp-integers-embed-rationals (j additive, j(1) = 1), fd1:ax-induction; inline
thm-prime-subfield (claim): (after the proof) (-b)^{-1} = -b^{-1} | fd3:prp-ring-algebra (c) and uniqueness of inverses; inline
thm-prime-subfield (claim): (remark after it) comparison with fd3:thm-rationals-embed-ordered-field, fd3:prp-cof-map-fixes-rationals | F3.9, F3.4 soft citations, comparison only
cor-finite-field-prime-characteristic (proof): {1, ..., N + 1} has N + 1 elements | fd2:def-finite (identity bijection)
cor-finite-field-prime-characteristic (claim): a finite field has p^n elements | not proved here; linear-algebra volumes; nothing uses it
cor-finite-field-prime-characteristic (claim): (quick check) no field has 6 elements | the p^n fact, marked not proved; the answer rests on prp-characteristic-invariant only
exm-characteristics (claim): (quick check) 7.[3] = [21] = [1] in F5 | verify/ch02/exm-characteristics.py
exr-characteristic-and-prime-subfield-b1 (solution): 300 = 42 * 7 + 6, 100 = 14 * 7 + 2 | verify/ch02/exr-characteristic-and-prime-subfield-b1.py
exr-characteristic-and-prime-subfield-b2 (solution): roots 4, 2 of x^2 + x + 1 in F7; 2^{-1} = 4; no root in F2 | verify/ch02/exr-characteristic-and-prime-subfield-b2.py
exr-characteristic-and-prime-subfield-b2 (solution): (2x)^2 = 4x^2 | power and product regrouping (F5), (F6) with lem-integer-multiples (b); inline
exr-characteristic-and-prime-subfield-c1 (solution): r = 0 when c | n, by uniqueness of the remainder | fd3:thm-integers-division-remainder (a), cited
exr-characteristic-and-prime-subfield-c1 (solution): s > 0, s != 1, s != c in c = rs; 1 < r, s < c | as in the proof of thm-characteristic-prime: fd3:prp-ordered-ring-rules (c), (f) on Z, discreteness fd3:thm-integers-ordered-ring (c)
exr-characteristic-and-prime-subfield-c2 (solution): 7.1 = 1.1 = 1 in F3, 7 - 1 = 6 | verify/ch02/exr-characteristic-and-prime-subfield-c2.py
exr-characteristic-and-prime-subfield-c3 (solution): the field of exr-finite-fields-from-modular-arithmetic-c1, its tables | an exercise cited from an exercise solution (STYLE 9); verify/ch02/exr-characteristic-and-prime-subfield-c3.py
-->
