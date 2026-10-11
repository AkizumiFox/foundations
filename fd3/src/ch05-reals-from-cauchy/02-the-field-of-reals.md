# The Real Numbers and Their Arithmetic

Section 5.1 sorted the Cauchy sequences of rationals by a relation, \( a \sim b \) when \( a - b \) is null, and proved it an equivalence relation (@prp-cauchy-equivalent-relation). This section takes the classes as the new numbers. It defines their sum, product and negative on representatives, proves that the definitions do not depend on the representatives, and shows that the result is a field. The construction follows a pattern seen three times already: the integers modulo \( n \) in *Sets, Relations, and Cardinality*, Section 2.5, the integers and the rationals in Chapter 2, and the quotient of a ring by an ideal in Chapter 3. The order comes in Section 5.3.

## The real numbers as classes

The Newton sequence and the decimal truncations are different sequences that aim at one number (@exm-truncations-equivalent). Rather than search \( \nQ \) for that number, we let the whole group of sequences aiming at it **be** the number.

*A real number is a Cauchy sequence of rationals, up to a null difference.*

::: {#def-reals-cauchy-classes}
[The Real Numbers]

The set of **real numbers** is the quotient set (@fd2:def-quotient-set)
\[
\nR \coloneqq \sC/{\sim}
\]
of the set \( \sC \) of Cauchy sequences of rationals (@def-rational-cauchy-sequences) by the relation \( \sim \) of @def-cauchy-equivalent. Its elements are the classes \( [a] = \{ b \in \sC : b \sim a \} \) for \( a \in \sC \) (@fd2:def-equivalence-class), and any \( b \in [a] \) is a **representative** of \( [a] \).
:::

In words: a real number is a set of Cauchy sequences of rationals, namely all those equivalent to one of them. By @fd2:thm-classes-partition (b), for all \( a, b \in \sC \),
\[
[a] = [b] \iff a \sim b \iff a - b \text{ is null} .
\]
This is the only tool we have, so far, for deciding when two real numbers are equal: compare representatives, and ask whether their difference is null.

**Examples.**

- *The Newton class.* By @exm-truncations-equivalent, \( [(x_n)_n] = [(d_k)_k] \): one real number, with two quite different representatives. By @exm-finite-change-equivalent (b), \( (x_{n+1})_n \) is a third.
- *The class of a constant.* For \( q \in \nQ \), the class \( [(q)_n] \) contains \( (q)_n \), and also \( (q + 1/(n + 1))_n \), since the difference is null. Different constants give different classes, because constant sequences are equivalent only when they are equal (the degenerate example after @def-cauchy-equivalent). Section 5.4 uses these classes to place a copy of \( \nQ \) inside \( \nR \).
- *Zero.* \( [(0)_n] \) is the set of all null sequences in \( \sC \): \( b \sim (0)_n \) means that \( b - (0)_n = b \) is null. So \( (1/(n + 1))_n \), \( ((-1)^n/(n + 1))_n \) and every sequence that is eventually \( 0 \) are representatives of it.

**What has been done, and what has not.** The symbol \( \nR \) now names one definite set, built from \( \nQ \) by the set-building tools of *Sets, Relations, and Cardinality*. In earlier volumes, the "familiar real numbers" were used informally; from here on in this volume \( \nR \) means this set and nothing else, and every fact about it must be proved from the definition. At this moment \( \nR \) has no addition, no multiplication, no order, and it does not contain \( \nQ \): the rational number \( 2 \) is not a class of sequences. All of these must be built. This section builds the arithmetic.

## Arithmetic on representatives

To add two real numbers, add representatives term by term; likewise for products and negatives. The terms are rationals, where the arithmetic is known.

::: {#def-reals-operations}
[Sum, Product and Negative of Real Numbers]

For \( a, b \in \sC \), let
\[
[a] + [b] \coloneqq [a + b] , \qquad [a] \, [b] \coloneqq [ab] , \qquad -[a] \coloneqq [-a] ,
\]
where \( a + b \), \( ab \) and \( -a \) are the termwise sum, product and negative. Let \( 0_{\nR} \coloneqq [(0)_n] \) and \( 1_{\nR} \coloneqq [(1)_n] \).
:::

The right-hand sides are classes of members of \( \sC \), because \( \sC \) is closed under termwise sums, products and negatives and contains the constants (@thm-cauchy-algebra-ordered-field). That makes the right-hand sides **meaningful**. It does not yet make the definition **legitimate**. Each formula takes a class and reads off a representative; if two representatives of the same class gave different answers, the "operation" would assign two values to one input, and so would not be a function (@fd2:def-function).

This danger is real, and it has been met before. In *Sets, Relations, and Cardinality*, Section 2.5, the arithmetic of the integers modulo \( n \) was defined by the same kind of formula and survived the check (@fd2:prp-congruence-arithmetic), while the rule \( [a]_6 \mapsto [a]_4 \) failed it (@fd2:exm-ill-defined-class-map). Chapter 2 made the same check for the integers and for the rationals, through the lemma @thm-well-defined-on-classes, which says that a rule on classes is a function as soon as equivalent inputs give equivalent outputs. Here the check is the same, and only the computation behind it is new.

**Representatives, then independence.** To define an operation on classes, define it on representatives; then show that the output class survives replacing each input by an equivalent one.

For sums this is a one-line computation. For products it is not, and the next theorem is the reason Chapter 4 proved that Cauchy sequences are bounded.

::: {#thm-reals-operations-well-defined}
[The Operations on Real Numbers Are Well Defined]

Let \( a, a', b, b' \in \sC \) with \( a \sim a' \) and \( b \sim b' \). Then
\[
a + b \sim a' + b' , \qquad ab \sim a'b' , \qquad -a \sim -a' .
\]
Hence the rules of @def-reals-operations define functions \( + \colon \nR \times \nR \to \nR \), \( \cdot \colon \nR \times \nR \to \nR \) and \( - \colon \nR \to \nR \).
:::

::: {.idea}
For the product we must show that \( a_n b_n - a'_n b'_n \) dies out, knowing only that \( a_n - a'_n \) and \( b_n - b'_n \) do. Replace one factor at a time: subtract and add the mixed term \( a_n b'_n \), so that
\[
a_n b_n - a'_n b'_n = a_n (b_n - b'_n) + (a_n - a'_n) \, b'_n .
\]
Each summand is a null sequence times another sequence. A null sequence times an **unbounded** one need not be null, so we need the multipliers \( (a_n) \) and \( (b'_n) \) bounded; they are, because they are Cauchy. Then each summand is null, and so is the sum.
:::

::: {.proof}
Let \( a, a', b, b' \in \sC \) with \( a \sim a' \) and \( b \sim b' \); so \( a - a' \) and \( b - b' \) are null (@def-cauchy-equivalent).

*Sum.* For every \( n \), \( (a_n + b_n) - (a'_n + b'_n) = (a_n - a'_n) + (b_n - b'_n) \), by the field axioms of \( \nQ \). So \( (a + b) - (a' + b') \) is the sum of two null sequences, which is null by @thm-limit-laws-ordered-field (a). Hence \( a + b \sim a' + b' \).

*Negative.* For every \( n \), \( (-a_n) - (-a'_n) = -(a_n - a'_n) \) (@prp-ring-algebra (c)). So \( (-a) - (-a') = -(a - a') \), which is null by @thm-limit-laws-ordered-field (b). Hence \( -a \sim -a' \).

*Product.* For every \( n \), by the field axioms of \( \nQ \),
\[
a_n b_n - a'_n b'_n = a_n (b_n - b'_n) + (a_n - a'_n) \, b'_n .
\]{#eq-reals-product-split}
The sequence \( a \) is in \( \sC \), so it is bounded (@prp-cauchy-bounded-ordered-field): there is \( M \in \nQ_{>0} \) with \( \abs{a_n} \le M \) for every \( n \). Since \( b - b' \) is null, the sequence \( \bigl( (b_n - b'_n) \, a_n \bigr)_n \) is null by @prp-null-times-bounded-ordered-field, and it is the first summand of @eq-reals-product-split, by commutativity in \( \nQ \). Likewise \( b' \in \sC \) is bounded, by some \( M' \in \nQ_{>0} \) (@prp-cauchy-bounded-ordered-field), and \( a - a' \) is null, so the second summand \( \bigl( (a_n - a'_n) \, b'_n \bigr)_n \) is null (@prp-null-times-bounded-ordered-field). By the sum rule (@thm-limit-laws-ordered-field (a)), \( ab - a'b' \) is null. Hence \( ab \sim a'b' \).

*Functions.* The maps \( (a, b) \mapsto a + b \) and \( (a, b) \mapsto ab \) are functions \( \sC \times \sC \to \sC \), and \( a \mapsto -a \) is a function \( \sC \to \sC \) (@thm-cauchy-algebra-ordered-field). Taking \( b' = b \) above (\( b \sim b \) by reflexivity) shows that each binary map respects \( \sim \) in its first argument; taking \( a' = a \) shows the same for the second. These are the hypotheses of @thm-well-defined-on-classes (b), and \( -a \sim -a' \) is the hypothesis of @thm-well-defined-on-classes (a). So the three rules define functions \( \nR \times \nR \to \nR \), \( \nR \times \nR \to \nR \) and \( \nR \to \nR \), as claimed.
:::

The proof used two different bounds: one for \( a \), which multiplies \( b_n - b'_n \), and one for \( b' \), which multiplies \( a_n - a'_n \). A bound for \( b \) would be of no use, since \( b \) appears nowhere in @eq-reals-product-split as a multiplier. Every Cauchy sequence is bounded, so both bounds exist; this is where the restriction of \( \sim \) to \( \sC \) pays (compare the "Why only on \( \sC \)" paragraph of Section 5.1).

So \( \nR \) has a sum, a product and a negative. For example, \( [(x_n)] + [(1)_n] = [(x_n + 1)_n] \), and the answer does not change if \( (x_n) \) is replaced by \( (d_k) \): the theorem says \( (x_n + 1) \sim (d_n + 1) \).

## The null sequences form an ideal

Chapter 3 made the check of well-definedness once and for all, for the quotient of a commutative ring by an ideal (@def-ideal-commutative-ring, @thm-quotient-ring-by-ideal). The construction of \( \nR \) is an instance of it, and seeing it that way gives the laws of arithmetic in \( \nR \) without checking them one by one.

Let \( \sN \subseteq \sC \) be the set of null sequences of rationals; it lies in \( \sC \) by @thm-cauchy-algebra-ordered-field (a). Then
\[
a \sim b \iff a - b \in \sN \qquad (a, b \in \sC) ,
\]
which is the relation \( \sim_{\sN} \) of @thm-quotient-ring-by-ideal (a). So \( \nR = \sC/{\sim} \) is \( \sC/\sN \) in the notation of Chapter 3, and the rules of @def-reals-operations are the rules of @thm-quotient-ring-by-ideal (b). What must be checked is that \( \sC \) is a commutative ring and \( \sN \) an ideal of it. The proof of the product clause in @thm-reals-operations-well-defined is then the general proof of Chapter 3 in this instance, with (I3) supplied by "null times bounded is null".

::: {#thm-reals-commutative-ring}
[The Real Numbers Form a Commutative Ring]

\( (\nR, +, \cdot) \), with the operations of @def-reals-operations, is a commutative ring (@def-commutative-ring-and-field) with zero \( 0_{\nR} \) and one \( 1_{\nR} \): it satisfies (F1)–(F7) and (F9), the additive inverse of \( [a] \) is \( -[a] \), and \( 0_{\nR} \ne 1_{\nR} \).
:::

::: {.idea}
Two claims, then Chapter 3's theorem. Termwise operations inherit every law of \( \nQ \), because a law about sequences is an equation between functions on \( \nN \), checked one index at a time. And the null sequences satisfy the three clauses of an ideal: \( (0)_n \) is null, sums of null sequences are null, and a null sequence times a Cauchy sequence is null. The quotient theorem then hands over all the laws at once. For \( 0_{\nR} \ne 1_{\nR} \), the constant \( 1 \) is not null.
:::

::: {.proof}
::: {.claim}
\( \sC \), with the termwise operations, is a commutative ring with zero \( (0)_n \), one \( (1)_n \), and \( -a \) the additive inverse of \( a \).
:::

::: {.proof}
By @thm-cauchy-algebra-ordered-field, the termwise sum and product of two members of \( \sC \), the termwise negative of a member, and the constants \( (0)_n \), \( (1)_n \) lie in \( \sC \); so \( + \) and \( \cdot \) are functions \( \sC \times \sC \to \sC \). Each of (F1)–(F7) and (F9) asserts an equality of sequences, that is, of functions \( \nN \to \nQ \), so it holds if and only if it holds at every index \( n \) (@fd2:prp-function-equality). At the index \( n \) it is the same clause in \( \nQ \), with \( a_n, b_n, c_n \) in place of \( a, b, c \), and \( \nQ \) is a field (@thm-rationals-ordered-field). For example, (F9) at \( n \) reads \( a_n (b_n + c_n) = a_n b_n + a_n c_n \), and (F4) reads \( a_n + (-a_n) = 0 \).
:::

::: {.claim}
\( \sN \) is an ideal of \( \sC \) (@def-ideal-commutative-ring).
:::

::: {.proof}
(I1) The zero sequence \( (0)_n \) is null (@exm-first-sequences-ordered-field (a)). (I2) If \( a, b \in \sN \), then \( a + b \in \sN \), by the sum rule @thm-limit-laws-ordered-field (a). (I3) Let \( a \in \sN \) and \( r \in \sC \). Then \( r \) is bounded (@prp-cauchy-bounded-ordered-field), so \( (a_n r_n)_n \) is null (@prp-null-times-bounded-ordered-field), and \( ra = (r_n a_n)_n = (a_n r_n)_n \) by commutativity in \( \nQ \). So \( ra \in \sN \).
:::

As noted before the theorem, \( \sim \) is the relation \( \sim_{\sN} \), so \( \nR = \sC/\sN \), and the operations of @def-reals-operations are those of @thm-quotient-ring-by-ideal (b). By @thm-quotient-ring-by-ideal (c), \( \nR \) is a commutative ring with zero \( [(0)_n] = 0_{\nR} \) and one \( [(1)_n] = 1_{\nR} \). Its additive inverse of \( [a] \) is \( [-a] = -[a] \), since \( [a] + [-a] = [a + (-a)] = [(0)_n] \) by the first claim.

Finally, by @thm-quotient-ring-by-ideal (d), \( 1_{\nR} = 0_{\nR} \) if and only if \( \sN = \sC \). But \( (1)_n \in \sC \) is not null: for \( \varepsilon = 1/2 \), every \( n \) has \( \abs{1 - 0} = 1 \ge 1/2 \). So \( \sN \ne \sC \), and \( 0_{\nR} \ne 1_{\nR} \). This proves the theorem.
:::

To see what the quotient theorem did, here is distributivity unfolded. For \( a, b, c \in \sC \), using @def-reals-operations three times and (F9) in \( \sC \),
\[
\begin{aligned}
[a] \bigl( [b] + [c] \bigr) &= [a] \, [b + c] = [a (b + c)] \\
&= [ab + ac] = [ab] + [ac] = [a][b] + [a][c] .
\end{aligned}
\]
Every law goes the same way: move to representatives, use the law in \( \sC \), which is the law in \( \nQ \) at each index, and move back. Only the legitimacy of "move to representatives" needed an argument, and @thm-reals-operations-well-defined supplied it.

## Inverses

A commutative ring is not yet a field. The missing clause is (F8): every \( x \ne 0_{\nR} \) needs an inverse. The obvious idea is to invert term by term, and it fails; the example after the theorem shows how. What saves it is a fact from Chapter 4: a Cauchy sequence that is not null stays **a fixed distance** away from \( 0 \) from some index on (@thm-cauchy-not-null-sign).

::: {#thm-reals-field}
[The Real Numbers Form a Field]

Every \( x \in \nR \) with \( x \ne 0_{\nR} \) has a multiplicative inverse: there is \( y \in \nR \) with \( xy = 1_{\nR} \). Hence \( \nR \), with the operations of @def-reals-operations, is a field (@def-commutative-ring-and-field).
:::

::: {.idea}
Write \( x = [a] \). Since \( x \ne 0_{\nR} \), \( a \) is not null, so from some index \( N \) on its terms are at least \( c > 0 \) in absolute value. Invert \( a_n \) for \( n \ge N \), and put anything harmless, say \( 1 \), before \( N \); Chapter 4 showed the result is again Cauchy (@prp-cauchy-reciprocal-ordered-field). The product with \( a \) is \( 1 \) from \( N \) on, and the first \( N \) terms do not matter. *Before reading on: the inverse is built from one representative \( a \). Why does the class \( [b] \) not depend on which representative of \( x \) we started from?*
:::

::: {.proof}
Let \( x \in \nR \) with \( x \ne 0_{\nR} \). By @fd2:def-quotient-set, \( x = [a] \) for some \( a \in \sC \); fix one such \( a \) (\( \rulename{\exists E} \), @fd1:def-rules-existential). The sequence \( a \) is not null: otherwise \( a \sim (0)_n \), and \( x = [(0)_n] = 0_{\nR} \) by @fd2:thm-classes-partition (b).

By @thm-cauchy-not-null-sign (with \( F = \nQ \)) there are \( c \in \nQ_{>0} \) and \( N \in \nN \) such that \( a_n \ge c \) for every \( n \ge N \), or \( a_n \le -c \) for every \( n \ge N \). Fix one such pair \( (c, N) \) (\( \rulename{\exists E} \) again). This fixes two objects, once; it is not a selection from infinitely many sets. In either case \( \abs{a_n} \ge c \) for every \( n \ge N \): if \( a_n \ge c > 0 \), then \( \abs{a_n} = a_n \); if \( a_n \le -c \), then \( \abs{a_n} = -a_n \ge c \) (@def-absolute-value-ordered-field, @prp-ordered-ring-rules (a)).

By @prp-cauchy-reciprocal-ordered-field, the sequence \( b \) with \( b_n \coloneqq 1/a_n \) for \( n \ge N \) and \( b_n \coloneqq 1 \) for \( n < N \) is in \( \sC \), and \( a_n b_n = 1 \) for every \( n \ge N \). So the sequence \( ab - (1)_n \) agrees with \( (0)_n \) from \( N \) on, and it is null by @prp-tail-change-ordered-field (a). Hence \( ab \sim (1)_n \), and
\[
x \, [b] = [a] \, [b] = [ab] = [(1)_n] = 1_{\nR} .
\]
So \( y \coloneqq [b] \) is an inverse of \( x \), and (F8) holds. Together with @thm-reals-commutative-ring, which gives (F1)–(F7), (F9) and \( 0_{\nR} \ne 1_{\nR} \), this shows that \( \nR \) is a field.
:::

The answer to the prompt: **inverses in a commutative ring are unique.** If \( xy = 1_{\nR} \) and \( xy' = 1_{\nR} \), then \( y = y \cdot 1_{\nR} = y (x y') = (y x) y' = 1_{\nR} \, y' = y' \), by (F7), (F5) and (F6). So starting from another representative \( a' \) of \( x \), with its own \( c' \), \( N' \) and \( b' \), gives \( [b'] = [b] \); we write \( x^{-1} \) for it.

::: {#exm-termwise-reciprocal-ill-defined}
[Termwise Reciprocals Are Not a Definition]

A shorter route to inverses would be: for \( x = [a] \ne 0_{\nR} \), let \( x^{-1} \coloneqq [(1/a_n)_n] \). Explain why this is not a definition, and why \( 0_{\nR} \) must be excluded in any case.
:::

::: {.solution}
*It need not make sense.* The sequences \( a \coloneqq (0, 1, 1, 1, \dots) \) and \( (1)_n \) agree from \( n = 1 \) on, so they are equivalent (@exm-finite-change-equivalent (a)) and represent the same real number \( 1_{\nR} \ne 0_{\nR} \). With the representative \( a \), the rule asks for \( 1/a_0 = 1/0 \), which does not exist. A rule that cannot be applied to some representatives does not define a function on classes; it would need a statement of which representatives are allowed, and a proof that the answer does not depend on the allowed one. The proof of @thm-reals-field supplies both at once: it inverts only from an index \( N \) on, and the uniqueness of inverses makes the class independent of all the choices.

*Why \( 0_{\nR} \) is excluded.* The null sequence \( (1/(n + 1))_n \) represents \( 0_{\nR} \) and has no zero term, so the termwise reciprocal \( (n + 1)_n \) exists. But it is not bounded (@thm-rationals-archimedean), so it is not in \( \sC \) (@prp-cauchy-bounded-ordered-field), and it represents no real number. No inverse of \( 0_{\nR} \) is possible in any case, since \( 0_{\nR} \cdot y = 0_{\nR} \ne 1_{\nR} \) for every \( y \) (@prp-ring-algebra (b), @thm-reals-commutative-ring).
:::

::: {.warning}
**A termwise formula is not an operation until it is checked on every representative.** "\( [a]^{-1} \coloneqq [(1/a_n)] \)" fails on \( (0, 1, 1, 1, \dots) \), a representative of \( 1_{\nR} \), whose first term cannot be inverted. Every definition on \( \nR \) must say what it does to **each** representative of a class, and then prove that the class of the answer is the same for all of them.
:::

::: {.check}
Find a representative of \( [(1 + 1/(n + 1))_n] \cdot [(2)_n] - [(2)_n] \), and name its class.
:::

::: {.solution}
By @def-reals-operations, with \( x - y \coloneqq x + (-y) \) in the ring \( \nR \), the real number is \( [(1 + 1/(n + 1)) \cdot 2] + [(-2)_n] = [(2 + 2/(n + 1) - 2)_n] \), so \( (2/(n + 1))_n \) represents it. This sequence is null (@thm-limit-laws-ordered-field (b) with \( c = 2 \), applied to \( (1/(n + 1)) \)), so the class is \( 0_{\nR} \). In other words, \( [(1 + 1/(n + 1))_n] \cdot [(2)_n] = [(2)_n] \): the first factor is \( 1_{\nR} \), represented by a sequence none of whose terms is \( 1 \).
:::

\( \nR \) is now a field. It has no order yet: "positive" for a class of sequences needs care, and Section 5.3 defines it.

## Exercises

### A. Check your understanding

::: {#exr-the-field-of-reals-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Prove, directly from @def-reals-operations and the field axioms of \( \nQ \), that \( ([a][b])[c] = [a]([b][c]) \) and \( 1_{\nR} \, [a] = [a] \) for all \( a, b, c \in \sC \).
2. In the product part of the proof of @thm-reals-operations-well-defined, which two of the four sequences \( a, a', b, b' \) must be bounded, and why is "\( b \) is bounded" not what @eq-reals-product-split needs?
3. Run that proof on \( a = (2 + 1/(n + 1))_n \), \( a' = (2)_n \), \( b = (x_n)_n \) (the Newton sequence) and \( b' = (d_n)_n \) (the truncations): check that \( a \sim a' \) and \( b \sim b' \), write \( a_n b_n - a'_n b'_n \) as in @eq-reals-product-split, and give a bound for each multiplier.
4. State the idea of the proof of @thm-reals-operations-well-defined in two sentences.
:::
:::

::: {.solution}
(a) By @def-reals-operations twice, \( ([a][b])[c] = [ab][c] = [(ab)c] \) and \( [a]([b][c]) = [a][bc] = [a(bc)] \). For every \( n \), \( (a_n b_n) c_n = a_n (b_n c_n) \) by (F5) in \( \nQ \), so \( (ab)c = a(bc) \) as sequences (@fd2:prp-function-equality), and the two classes are equal. Likewise \( 1_{\nR} [a] = [(1)_n][a] = [(1 \cdot a_n)_n] = [a] \), by (F6) and (F7) in \( \nQ \).

(b) \( a \) and \( b' \). In @eq-reals-product-split, \( a_n \) multiplies the null \( b_n - b'_n \), and \( b'_n \) multiplies the null \( a_n - a'_n \); @prp-null-times-bounded-ordered-field needs the multiplier bounded. The sequence \( b \) appears in @eq-reals-product-split only inside the null factor \( b_n - b'_n \), so its bound is never used.

(c) \( a - a' = (1/(n + 1))_n \) is null, so \( a \sim a' \); \( b \sim b' \) is @exm-truncations-equivalent. The split is
\[
\Bigl( 2 + \frac{1}{n + 1} \Bigr) x_n - 2 d_n = \Bigl( 2 + \frac{1}{n + 1} \Bigr) (x_n - d_n) + \frac{1}{n + 1} \, d_n .
\]
Multipliers: \( \abs{2 + 1/(n + 1)} \le 3 \), since \( 0 < 1/(n + 1) \le 1 \); and \( \abs{d_n} \le 2 \), since \( 1 \le d_n < 2 \) (Steps 1 and 3 of the solution of @exm-truncations-equivalent). So the first summand is null (null times bounded by \( 3 \)) and the second is null (null times bounded by \( 2 \)).

(d) Changing both factors of a product at once is split into two changes, one factor at a time, by adding and subtracting a mixed term. Each change is a null sequence times a bounded one, because Cauchy sequences are bounded, so each is null, and so is their sum.
:::

### B. Practice

::: {#exr-the-field-of-reals-b1}
[B1: The negative, directly]

Without using @thm-quotient-ring-by-ideal, prove that the rule \( -[a] \coloneqq [-a] \) defines a function \( \nR \to \nR \), and that \( [a] + (-[a]) = 0_{\nR} \) for every \( a \in \sC \). Deduce that \( [a] - [b] = [a - b] \) for all \( a, b \in \sC \).
:::

::: {.solution}
*Well defined.* \( -a \in \sC \) for \( a \in \sC \) (@thm-cauchy-algebra-ordered-field (b)). Let \( a \sim a' \). For every \( n \), \( (-a_n) - (-a'_n) = -(a_n - a'_n) \) (@prp-ring-algebra (c)), and \( (-(a_n - a'_n))_n \) is null because \( a - a' \) is (@thm-limit-laws-ordered-field (b)). So \( -a \sim -a' \), and @thm-well-defined-on-classes (a) gives a function \( \nR \to \nR \).

*Inverse.* \( [a] + (-[a]) = [a] + [-a] = [a + (-a)] = [(a_n + (-a_n))_n] = [(0)_n] = 0_{\nR} \), by @def-reals-operations and (F4) in \( \nQ \) at each index.

*Differences.* \( [a] - [b] = [a] + (-[b]) = [a] + [-b] = [a + (-b)] = [a - b] \), by the definition \( x - y \coloneqq x + (-y) \) in a ring and @def-reals-operations.
:::

::: {#exr-the-field-of-reals-b2}
[B2: The larger of two reals, faded]

For \( x, y \in \nQ \) let \( \max(x, y) \coloneqq x \) if \( x \ge y \), and \( \max(x, y) \coloneqq y \) otherwise. For \( a, b \in \sC \) consider the rule
\[
[a] \vee [b] \coloneqq [(\max(a_n, b_n))_n] .
\]

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \abs{\max(x, y) - \max(x', y')} \le \abs{x - x'} + \abs{y - y'} \) for all \( x, y, x', y' \in \nQ \). *Hint: suppose \( \max(x, y) \ge \max(x', y') \), and split into the cases \( \max(x, y) = x \) and \( \max(x, y) = y \).*
2. Deduce from (a) that \( (\max(a_n, b_n))_n \in \sC \) whenever \( a, b \in \sC \).
3. Here is the start of a proof that \( \vee \) is well defined. *Name the move, then complete it.*

   "Let \( a, a', b, b' \in \sC \) with \( a \sim a' \) and \( b \sim b' \). By (b), the sequences \( (\max(a_n, b_n))_n \) and \( (\max(a'_n, b'_n))_n \) are in \( \sC \). Let \( d_n \coloneqq \max(a_n, b_n) - \max(a'_n, b'_n) \). By (a), for every \( n \),
   \[
   0 \le \abs{d_n} \le \abs{a_n - a'_n} + \abs{b_n - b'_n} .
   \]
   ⟨ blank ⟩"
:::
:::

::: {.solution}
(a) Write \( M \coloneqq \max(x, y) \) and \( M' \coloneqq \max(x', y') \). Note \( M \ge x \), \( M \ge y \), and \( M \) is one of \( x \), \( y \); likewise for \( M' \). Suppose first \( M \ge M' \). If \( M = x \), then \( 0 \le M - M' \le x - x' \le \abs{x - x'} \), since \( M' \ge x' \) (@prp-ordered-ring-rules (b), @prp-absolute-value-ordered-field (c)). If \( M = y \), then likewise \( 0 \le M - M' \le y - y' \le \abs{y - y'} \). Either way \( \abs{M - M'} = M - M' \le \abs{x - x'} + \abs{y - y'} \). If \( M' > M \), exchange the roles of \( (x, y) \) and \( (x', y') \); the right-hand side is unchanged, as \( \abs{x' - x} = \abs{x - x'} \).

(b) Let \( \varepsilon \in \nQ_{>0} \), and let \( N \) be a threshold with tolerance \( \varepsilon/2 \) for both \( a \) and \( b \) (the larger of the two thresholds). For \( m, n \ge N \), (a) with \( (x, y, x', y') = (a_m, b_m, a_n, b_n) \) gives \( \abs{\max(a_m, b_m) - \max(a_n, b_n)} \le \abs{a_m - a_n} + \abs{b_m - b_n} < \varepsilon/2 + \varepsilon/2 = \varepsilon \).

(c) *The move:* representatives, then independence; here its last step, "a sequence squeezed between \( 0 \) and a null sequence is null, so the outputs are equivalent and the classes agree". *Completion:* The sequences \( (\abs{a_n - a'_n})_n \) and \( (\abs{b_n - b'_n})_n \) are null, since \( \bigl| \abs{t} - 0 \bigr| = \abs{t - 0} \) for every \( t \in \nQ \) (@def-null-sequence-ordered-field). So their sum is null (@thm-limit-laws-ordered-field (a)). By the squeeze @prp-limit-preserves-order-ordered-field (c), with lower sequence \( (0)_n \) and this upper sequence, \( (\abs{d_n})_n \) is null; hence \( (d_n)_n \) is null, by the same remark on \( \abs{d_n - 0} \). So \( (\max(a_n, b_n))_n \sim (\max(a'_n, b'_n))_n \). Taking \( b' = b \), and then \( a' = a \), gives the two hypotheses of @thm-well-defined-on-classes (b), so \( \vee \) is a function \( \nR \times \nR \to \nR \).
:::

::: {#exr-the-field-of-reals-b3}
[B3: A square root of two]

Let \( (x_n) \) be the Newton sequence. Show that \( [(x_n)] \cdot [(x_n)] = [(2)_n] \).
:::

::: {.solution}
By @def-reals-operations, \( [(x_n)] \cdot [(x_n)] = [(x_n^2)_n] \), so we must show that \( (x_n^2 - 2)_n \) is null. By the bound \( 0 < x_n^2 - 2 \le 1/(4n) \) for \( n \ge 1 \) (Section 5.1, (NS1)–(NS2)), and \( 1/(4n) \le 1/(n + 1) \) for \( n \ge 1 \),
\[
0 \le x_n^2 - 2 \le \frac{1}{n + 1} \qquad (n \ge 1) .
\]
The squeeze @prp-limit-preserves-order-ordered-field (c), with \( N_0 = 1 \), lower sequence \( (0)_n \) and the null upper sequence \( (1/(n + 1))_n \) (@exm-first-sequences-ordered-field (b)), defined for every \( n \in \nN \), shows that \( (x_n^2 - 2)_n \) is null. So \( (x_n^2) \sim (2)_n \) and the classes are equal. (The inequality fails at \( n = 0 \), where \( x_0^2 - 2 = 2 \); the squeeze does not need it there.) Section 5.4 returns to this class.
:::

### C. Going deeper

::: {#exr-the-field-of-reals-c1}
[C1: Exit check: multiplication is well defined]

State precisely what must be proved for the rule \( [a][b] \coloneqq [ab] \) to define a function \( \nR \times \nR \to \nR \), and prove it, including the fact that \( ab \in \sC \) for \( a, b \in \sC \).
:::

::: {.solution}
*What must be shown.* (i) For \( a, b \in \sC \), the termwise product \( ab \) is in \( \sC \), so that \( [ab] \) is a real number. (ii) If \( a \sim a' \) and \( b \sim b' \), then \( ab \sim a'b' \). By @thm-well-defined-on-classes (b), (i) and (ii) give exactly one function \( \nR \times \nR \to \nR \) with \( ([a], [b]) \mapsto [ab] \); without (ii), one pair of classes could receive two values, and (Fn2) of @fd2:def-function would fail.

*(i) Bound, then shrink.* Let \( a, b \in \sC \). Both are bounded (@prp-cauchy-bounded-ordered-field); let \( M \in \nQ_{>0} \) be a bound for both (the larger of the two bounds). For all \( m, n \),
\[
\begin{aligned}
\abs{a_m b_m - a_n b_n} &= \abs{a_m (b_m - b_n) + (a_m - a_n) b_n} \\
&\le M \abs{b_m - b_n} + M \abs{a_m - a_n} ,
\end{aligned}
\]
by @prp-absolute-value-ordered-field (b), (e). Let \( \varepsilon \in \nQ_{>0} \), and let \( N \) be a threshold with tolerance \( \varepsilon/(2M) \) for both \( a \) and \( b \). For \( m, n \ge N \), the right side is less than \( M \cdot \varepsilon/(2M) + M \cdot \varepsilon/(2M) = \varepsilon \). So \( ab \in \sC \). (This is @thm-cauchy-algebra-ordered-field (c), which may be cited instead.)

*(ii) The add-and-subtract decomposition.* For every \( n \),
\[
a_n b_n - a'_n b'_n = a_n (b_n - b'_n) + (a_n - a'_n) b'_n .
\]
The multipliers \( a \) and \( b' \) are in \( \sC \), hence bounded (@prp-cauchy-bounded-ordered-field). The sequences \( b - b' \) and \( a - a' \) are null. By @prp-null-times-bounded-ordered-field, both summands are null, and by the sum rule (@thm-limit-laws-ordered-field (a)) so is \( ab - a'b' \). Hence \( ab \sim a'b' \).

**Marking scheme.** (10 points)

- 2: states what must be shown (the product lies in \( \sC \); equivalent inputs give equivalent outputs) and why this makes the rule a function.
- 2: proves \( ab \in \sC \), by "bound, then shrink" with the threshold's dependence on \( \varepsilon \) and \( M \) clear, or by citing @thm-cauchy-algebra-ordered-field (c).
- 2: the add-and-subtract decomposition, or any identity writing \( a_n b_n - a'_n b'_n \) as a sum of (null) \( \times \) (sequence) terms.
- 2: boundedness of the two multipliers, justified by "Cauchy implies bounded".
- 2: concludes with null \( \times \) bounded is null and null \( + \) null is null.

A proof that changes one factor at a time (first \( ab \sim a'b \), then \( a'b \sim a'b' \)) earns the same points; the multipliers are then \( b \) and \( a' \). Fatal errors (0 for the step): "both differences are small, so the product difference is small" with no bound on the multipliers; a bound for \( b \) used where \( b' \) is the multiplier.
:::

::: {#exr-the-field-of-reals-c2}
[C2: No square is zero except zero]

::: {.enumerate options="label=(\alph*)"}
1. Let \( a \) be a sequence of rationals such that \( (a_n^2)_n \) is null. Prove that \( a \) is null.
2. Deduce, using only @def-reals-operations and (a), and not @thm-reals-field, that for \( x \in \nR \), \( x^2 = 0_{\nR} \) implies \( x = 0_{\nR} \).
:::
:::

::: {.solution}
(a) Let \( \varepsilon \in \nQ_{>0} \). Then \( \varepsilon^2 \in \nQ_{>0} \), so there is \( N \) with \( \abs{a_n^2} < \varepsilon^2 \) for every \( n \ge N \). For such \( n \), \( \abs{a_n}^2 = a_n^2 = \abs{a_n^2} < \varepsilon^2 \) (@prp-absolute-value-ordered-field (b), and \( a_n^2 \ge 0 \)), and \( \abs{a_n} \ge 0 \), \( \varepsilon > 0 \); so \( \abs{a_n} < \varepsilon \) by @prp-ordered-ring-rules (g). The threshold for \( \varepsilon \) is the threshold of \( (a_n^2) \) for \( \varepsilon^2 \). So \( a \) is null.

(b) Let \( x = [a] \) with \( a \in \sC \). Then \( x^2 = [a][a] = [(a_n^2)_n] \) by @def-reals-operations. If \( x^2 = 0_{\nR} = [(0)_n] \), then \( (a_n^2)_n \sim (0)_n \) (@fd2:thm-classes-partition (b)), that is, \( (a_n^2)_n \) is null. By (a), \( a \) is null, so \( a \sim (0)_n \) and \( x = 0_{\nR} \).

In a field this also follows from inverses: if \( x \ne 0_{\nR} \), then \( x = x^{-1} x^2 = x^{-1} 0_{\nR} = 0_{\nR} \), a contradiction. The direct proof shows the fact is already visible in the representatives, before any inverse exists. It fails in some commutative rings: in \( \nZ/4\nZ \) of Chapter 3 (@def-integers-mod-n-ring), \( [2]^2 = [4] = [0] \) while \( [2] \ne [0] \).
:::

<!-- dependency ledger
def-reals-cauchy-classes (claim): (q + 1/(n + 1)) ~ (q) and eventually-zero sequences represent 0_R | exm-first-sequences-ordered-field (b), exm-finite-change-equivalent (a) (cited in prose)
def-reals-cauchy-classes (claim): x_{n+1} represents the Newton class | exm-finite-change-equivalent (b) (cited)
thm-reals-operations-well-defined (proof): (a_n + b_n) - (a'_n + b'_n) = (a_n - a'_n) + (b_n - b'_n); the split a_n b_n - a'_n b'_n = a_n (b_n - b'_n) + (a_n - a'_n) b'_n | field axioms of Q (thm-rationals-ordered-field), prp-ring-algebra; verify/ch05/thm-reals-operations-well-defined.py
thm-reals-operations-well-defined (proof): both-at-once compatibility gives each one-argument hypothesis by reflexivity | prp-cauchy-equivalent-relation (Eq1) (cited in words)
thm-reals-commutative-ring (proof): an equality of sequences holds iff it holds at every index | fd2:prp-function-equality (cited)
thm-reals-commutative-ring (proof): the relation ~ equals ~_N, so C/~ = C/N | def-cauchy-equivalent and thm-quotient-ring-by-ideal (a) (cited)
thm-reals-field (proof): |a_n| >= c from a_n >= c > 0 or a_n <= -c | def-absolute-value-ordered-field, prp-ordered-ring-rules (a) (cited)
thm-reals-field (claim): inverses in a commutative ring are unique | inline, (F5)-(F7)
exm-termwise-reciprocal-ill-defined (solution): 0 * y = 0 in a commutative ring | prp-ring-algebra (b) (cited)
def-reals-operations (claim): (check) (1 + 1/(n + 1)) * 2 - 2 = 2/(n + 1) | field arithmetic; verify/ch05/exm-termwise-reciprocal-ill-defined.py
exr-the-field-of-reals-a1 (solution): bounds 3 and 2 for the multipliers; the split in the run | exm-truncations-equivalent Steps 1 and 3 (cited); verify/ch05/exr-the-field-of-reals-a1.py
exr-the-field-of-reals-b2 (solution): case analysis for |max(x, y) - max(x', y')| | inline; verify/ch05/exr-the-field-of-reals-b2.py
exr-the-field-of-reals-b2 (solution): ||t| - 0| = |t - 0| | prp-absolute-value-ordered-field (a), (b); inline
exr-the-field-of-reals-b3 (solution): 0 < x_n^2 - 2 <= 1/(4n) for n >= 1 | exm-newton-rationals-sqrt2 (i) and thm-sqrt2-cauchy-no-rational-limit (statement), as recalled in Section 5.1
exr-the-field-of-reals-c1 (solution): M * e/(2M) + M * e/(2M) = e | field arithmetic, prp-ordered-field-halves (b)
exr-the-field-of-reals-c2 (solution): [2]^2 = [0] in Z/4Z | def-integers-mod-n-ring (cited); remark only
-->
