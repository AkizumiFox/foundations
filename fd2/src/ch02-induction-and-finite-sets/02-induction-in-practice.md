# Induction, Strong Induction and Divisibility

*Logic and Proof*, Chapter 4 gave the principle of induction (@fd1:ax-induction), its strong form (@fd1:thm-strong-induction), and the first worked proofs: a sum (@fd1:exm-sum-consecutive-products), an inequality (@fd1:exm-power-inequality), and a strong induction with three base cases (@fd1:exm-threes-and-fives). *Logic and Proof*, Chapter 8 showed how an induction is written in prose (@fd1:exm-rhetoric-induction). This section is about the craft: which form of induction fits a claim, where it starts, how to find the induction hypothesis inside the step, and how an induction goes wrong, each failure located at one step. On the way it proves two facts that *Logic and Proof* took from school: a fraction can be reduced until numerator and denominator are not both even, and every integer \( n \ge 2 \) has a prime factor.

## Induction from any integer

*Logic and Proof*, Chapter 4 already started inductions at numbers other than \( 0 \) (*Logic and Proof*, Section 4.2, "Starting from another number"), for a starting point \( b \in \nN \). With \( \nZ \) and @prp-integers-closed in hand, the starting point may be any integer, negative ones included.

*To prove a statement for every integer from \( n_0 \) on, prove it at \( n_0 \) and show that it passes from each integer to the next.*

::: {#thm-induction}
[Induction from a Base]

Let \( n_0 \) be an integer, and for each integer \( n \ge n_0 \) let \( P(n) \) be a statement. Suppose

::: {.enumerate options="label=(\roman*)"}
1. (**base case**) \( P(n_0) \) is true, and
2. (**inductive step**) for **every** integer \( n \ge n_0 \), if \( P(n) \) is true then \( P(n + 1) \) is true.
:::

Then \( P(n) \) is true for every integer \( n \ge n_0 \).
:::

::: {.idea}
Count from the base. The integers \( n \ge n_0 \) are exactly \( n_0 + k \) with \( k \in \nN \), and moving from \( n \) to \( n + 1 \) moves \( k \) to \( k + 1 \). So the statement "\( P(n_0 + k) \)" about \( k \in \nN \) is ready for @fd1:ax-induction, and its base case is \( P(n_0) \).
:::

::: {.proof}
For \( k \in \nN \), let \( Q(k) \) be the statement \( P(n_0 + k) \). This makes sense: \( n_0 + k \) is an integer by @prp-integers-closed (a), and \( n_0 + k \ge n_0 \) since \( k \ge 0 \) by @lem-naturals-arithmetic (a).

*Base case.* \( Q(0) \) is \( P(n_0) \), which holds by (i).

*Inductive step.* Let \( k \in \nN \), and suppose \( Q(k) \), that is, \( P(n_0 + k) \). The integer \( n \coloneqq n_0 + k \) satisfies \( n \ge n_0 \), so (ii) gives \( P(n + 1) \). Since \( n + 1 = n_0 + (k + 1) \), this is \( Q(k + 1) \).

By @fd1:ax-induction, \( Q(k) \) holds for every \( k \in \nN \). Now let \( n \) be an integer with \( n \ge n_0 \). Then \( k \coloneqq n - n_0 \) is an integer by @prp-integers-closed (a), and \( k \ge 0 \), so \( k \in \nN \) by @prp-integers-closed (b). Hence \( Q(k) \) holds, and \( Q(k) \) is \( P(n_0 + k) = P(n) \). This proves the theorem.
:::

For \( n_0 = 0 \) the theorem is @fd1:ax-induction itself, and for \( n_0 \in \nN \) it is *Logic and Proof*, Chapter 4's induction started at \( n_0 \). In the inductive step, "\( P(n) \) is true" is the induction hypothesis: one implication, proved once, inside a \( \rulename{{\to}I} \) box whose assumption is \( P(n) \) for one fixed but arbitrary integer \( n \ge n_0 \).

The strong form moves to a base in the same way.

::: {#thm-strong-induction-from-base}
[Strong Induction from a Base]

Let \( n_0 \) be an integer, and for each integer \( n \ge n_0 \) let \( P(n) \) be a statement. Suppose that, **for every** integer \( n \ge n_0 \): if \( P(k) \) is true for **every** integer \( k \) with \( n_0 \le k < n \), then \( P(n) \) is true. Then \( P(n) \) is true for every integer \( n \ge n_0 \).
:::

::: {.proof}
For \( j \in \nN \), let \( Q(j) \) be \( P(n_0 + j) \), as in the proof of @thm-induction. We check the hypothesis of @fd1:thm-strong-induction for \( Q \). Let \( j \in \nN \), and suppose \( Q(i) \) holds for every \( i \in \nN \) with \( i < j \). Put \( n \coloneqq n_0 + j \), an integer with \( n \ge n_0 \). Let \( k \) be an integer with \( n_0 \le k < n \). Then \( i \coloneqq k - n_0 \) is an integer with \( i \ge 0 \), so \( i \in \nN \) by @prp-integers-closed (b), and \( i < n - n_0 = j \); so \( Q(i) \), which is \( P(k) \), holds. The hypothesis of the theorem at \( n \) now gives \( P(n) \), that is, \( Q(j) \). By @fd1:thm-strong-induction, \( Q(j) \) holds for every \( j \in \nN \), and every integer \( n \ge n_0 \) is \( n_0 + j \) with \( j = n - n_0 \in \nN \), as in the proof of @thm-induction. This proves the theorem.
:::

So @thm-strong-induction-from-base is a corollary of @fd1:thm-strong-induction, by the same shift. When \( n_0 \in \nN \), it says what @fd1:exm-threes-and-fives achieved with a guard: there the property was "if \( n \ge 8 \), then …", stated for every \( n \in \nN \) and vacuous below \( 8 \). Here the property is stated only for \( n \ge n_0 \), and the hypothesis speaks only about \( k \ge n_0 \). The two are the same argument in two notations, and the base cases sit in the same place: they are the \( n \) for which the step reaches below \( n_0 \).

::: {.check}
Every integer \( n \ge 24 \) is \( 5a + 7b \) for some integers \( a, b \ge 0 \). A proof by @thm-strong-induction-from-base writes \( n = (n - 5) + 5 \) in its step. How many base cases does it need, and which? Can the base \( 24 \) be lowered?
:::

::: {.solution}
The step uses \( P(n - 5) \), which the hypothesis supplies only when \( n - 5 \ge 24 \), that is, \( n \ge 29 \). So \( n = 24, 25, 26, 27, 28 \) are base cases, five of them, checked directly:
\[
\begin{aligned}
24 &= 5 \cdot 2 + 7 \cdot 2 , & 25 &= 5 \cdot 5 , & 26 &= 5 \cdot 1 + 7 \cdot 3 , \\
27 &= 5 \cdot 4 + 7 \cdot 1 , & 28 &= 7 \cdot 4 .
\end{aligned}
\]
The base cannot be lowered: \( 23 \) is not of the form. With \( b = 0, 1, 2, 3 \) the difference \( 23 - 7b \) is \( 23, 16, 9, 2 \), none a multiple of \( 5 \), and \( b \ge 4 \) gives \( 23 - 7b < 0 \).
:::

## Finding \( P(n) \) inside \( P(n + 1) \)

In every induction the step is an implication \( P(n) \Rightarrow P(n + 1) \), proved for an arbitrary \( n \). The work is to find, inside the statement \( P(n + 1) \), the statement \( P(n) \), so that the hypothesis can be used: one more term to split off, one more factor to take out, one more case to bound. The first example is about divisibility (@def-divides).

::: {.idea}
[Scratch work]

The claim is \( 7 \mid 9^n - 2^n \) for every \( n \in \nN \), with the powers in their school meaning. The base is \( 9^0 - 2^0 = 0 = 7 \cdot 0 \). For the step, the hypothesis is about \( 9^n - 2^n \), so write \( P(n + 1) \) out and look for that expression in it. The first try, \( 9^{n+1} - 2^{n+1} = 9 \cdot 9^n - 2 \cdot 2^n \), does not contain it: the two powers have different factors in front, \( 9 \) and \( 2 \). Force the old expression in. Take \( 9 \) out of both terms, and pay back what that costs: \( 9 \cdot 9^n - 2 \cdot 2^n = 9(9^n - 2^n) + 9 \cdot 2^n - 2 \cdot 2^n \), and the payment \( 9 \cdot 2^n - 2 \cdot 2^n \) is \( 7 \cdot 2^n \), a multiple of \( 7 \) again.

| Givens | Goal |
|---|---|
| \( P(n) \): \( 9^n - 2^n = 7k \) with \( k \in \nZ \) | \( P(n + 1) \): \( 9^{n+1} - 2^{n+1} = 7m \) for some \( m \in \nZ \) |
| \( 9^{n+1} = 9 \cdot 9^n \), \( 2^{n+1} = 2 \cdot 2^n \) (school meaning) | \( 9^{n+1} - 2^{n+1} \) rewritten so that \( 9^n - 2^n \) appears |
| \( 9^{n+1} - 2^{n+1} = 9(9^n - 2^n) + 7 \cdot 2^n = 7(9k + 2^n) \) | \( m \coloneqq 9k + 2^n \in \nZ \): the gap is closed |

The old expression appears once, the hypothesis turns it into \( 7k \), and what is left over is a multiple of \( 7 \) by computation.
:::

Divisibility claims about powers are a staple of induction, because the step can usually be arranged to contain the old expression once. Here is the proof the scratch work found. *Claim:* \( 7 \mid 9^n - 2^n \) for every \( n \in \nN \), with \( 9^n \) and \( 2^n \) in their school meaning (\( a^0 = 1 \), \( a^{n+1} = a^n \cdot a \), and \( a^n \) is an integer for an integer \( a \); Section 2.3 makes this a definition). *Base case:* \( 9^0 - 2^0 = 0 = 7 \cdot 0 \). *Step:* if \( 9^n - 2^n = 7k \) with \( k \in \nZ \), then
\[
9^{n+1} - 2^{n+1} = 9(9^n - 2^n) + 7 \cdot 2^n = 7(9k + 2^n) ,
\]
and \( 9k + 2^n \in \nZ \). By @fd1:ax-induction, the claim holds for every \( n \in \nN \).

::: {#exm-method-induction-step}
[Method: finding \( P(n) \) inside \( P(n + 1) \)]

**Template.** (1) Write \( P(n + 1) \) out in full. (2) Find \( P(n) \) inside it: split off the last term, take out one factor, or separate the new piece from the old. (3) Apply the induction hypothesis to the old part. (4) Close the rest by computation. (5) Choose the base: the first \( n \) the claim covers from which steps (2)–(4) work, with any smaller \( n \) the claim covers checked directly.

**When to use it.** \( P(n + 1) \) is built from \( P(n) \) by one operation: a term added, a factor multiplied, an element added to a set.

**The usual failure.** Starting from \( P(n + 1) \) and deriving something true, which proves the converse, entry (N5) of @fd1:exm-not-allowed-catalogue. A step that works only from some \( n \) on, with the base set lower (as in the gallery below). Using \( P(n + 1) \) inside its own step (N9).
:::

::: {.check}
For a proof that \( 5 \mid 9^n - 4^n \) for every \( n \in \nN \), write \( 9^{n+1} - 4^{n+1} \) so that \( 9^n - 4^n \) appears.
:::

::: {.solution}
\( 9^{n+1} - 4^{n+1} = 9 \cdot 9^n - 4 \cdot 4^n = 9(9^n - 4^n) + 5 \cdot 4^n \). If \( 9^n - 4^n = 5k \) with \( k \in \nZ \), this is \( 5(9k + 4^n) \), and \( 9k + 4^n \in \nZ \).
:::

The fifth step of the template deserves an example of its own, because the place where the step starts working need not be the place where the claim starts being true.

::: {#exm-choosing-the-base}
[Where the step starts working]

Prove that \( 3^n \ge n^3 \) for every \( n \in \nN \), with the powers in their school meaning.
:::

::: {.idea}
By @exm-method-induction-step, write \( P(n + 1) \) out: it contains \( 3^n \) as \( 3^{n+1} = 3 \cdot 3^n \ge 3n^3 \), so the step needs \( 3n^3 \ge (n + 1)^3 \). That holds from \( n = 3 \) on, and not before. So the base is \( 3 \), and \( 0 \), \( 1 \), \( 2 \) are checked directly.
:::

::: {.solution}
*Small cases.* \( 3^0 = 1 \ge 0 = 0^3 \), \( 3^1 = 3 \ge 1 = 1^3 \), and \( 3^2 = 9 \ge 8 = 2^3 \).

*From \( 3 \) on*, by @thm-induction with base \( 3 \). *Base case:* \( 3^3 = 27 \ge 27 = 3^3 \). *Step:* let \( n \ge 3 \) be an integer with \( 3^n \ge n^3 \). Then \( 3^{n+1} = 3 \cdot 3^n \ge 3n^3 \). Since \( n \ge 3 \),
\[
2n^3 \ge 6n^2 = 3n^2 + 3n^2 \ge 3n^2 + 9n \ge 3n^2 + 3n + 1 ,
\]
so \( 3n^3 = n^3 + 2n^3 \ge n^3 + 3n^2 + 3n + 1 = (n + 1)^3 \). Hence \( 3^{n+1} \ge (n + 1)^3 \).

The small cases and the induction together give \( 3^n \ge n^3 \) for every \( n \in \nN \).
:::

The claim is true at \( 0 \), \( 1 \) and \( 2 \), but the argument of the step fails from \( 2 \) to \( 3 \): \( 3 \cdot 2^3 = 24 < 27 = 3^3 \). The base is where the step starts working, or the first \( n \) the claim covers if that is later. It need not be the first \( n \) at which the claim is true, and the cases below it are checked one by one.

::: {.check}
For which \( n \in \nN \) is \( 3n^3 \ge (n + 1)^3 \) false, and why does that make \( 3 \) the base although \( 3^n \ge n^3 \) holds at \( 0 \), \( 1 \) and \( 2 \)?
:::

::: {.solution}
For \( n = 0, 1, 2 \): \( 0 < 1 \), \( 3 < 8 \) and \( 24 < 27 \). The step is proved only from \( 3 \) on, so the three smaller cases need their own checks; an induction from base \( 0 \) would have three unproved transitions.
:::

## Divisibility and the division algorithm

The next results are about divisibility.

Divisibility and primes were defined in Section 1.1: for integers \( a \) and \( b \), \( a \mid b \) means \( b = ka \) for some \( k \in \nZ \) (@def-divides), and a prime is an integer \( p \ge 2 \) whose only positive divisors are \( 1 \) and \( p \) (@def-prime); divisibility is transitive (@prp-divides-transitive). For instance, \( 3 \mid 12 \), with \( k = 4 \).

Change \( 12 \) to \( 14 \): \( 3 \nmid 14 \). The witness \( k \) would have to be \( 14/3 \), and \( 4 < 14/3 < 5 \), so \( 14/3 \) is not an integer, by the discreteness clause of @prp-integers-closed. The clause that fails is "\( k \in \nZ \)": the equation \( 14 = k \cdot 3 \) has a real solution, just not an integer one.

Section 1.1 worked the first examples of primes and non-primes after @def-prime. The clause \( p \ge 2 \) keeps \( 1 \) out so that factorizations into primes can be unique, a fact this chapter does not prove or use: Exercise B2 below is about existence only.

Every integer, divided by a positive integer \( n \), leaves a remainder between \( 0 \) and \( n - 1 \). This is school arithmetic, and it is the tool behind "even or odd".

::: {#thm-division-algorithm}
[Division Algorithm]

Let \( a \in \nZ \) and \( n \in \nZ_{>0} \). Then there are **unique** integers \( q \) and \( r \) with
\[
a = qn + r \quad \text{and} \quad 0 \le r < n .
\]
:::

The hypothesis \( n > 0 \) matters: for \( n = 0 \) no \( r \) satisfies \( 0 \le r < 0 \).

*Try it first (ten minutes): which set of non-negative integers should have a least element, and why is that least element the remainder?*

::: {.idea}
The obvious attempt subtracts \( n \) from \( a \) again and again until what is left lies in \( [0, n) \), adding \( n \) instead when \( a \) is negative. "Again and again until" is a process, not yet a proof: why does it stop, and why at a number below \( n \)? Well-ordering replaces the process by its outcome. Among all the non-negative integers \( a - qn \), take the **least** (the method of @exm-method-least-element: \( S \) the non-negative integers \( a - qn \)). If it were \( n \) or more, subtracting one more \( n \) would leave a smaller non-negative one. For uniqueness: two remainders differ by a multiple of \( n \), yet lie less than \( n \) apart, so the multiple is \( 0 \).
:::

::: {.proof}
*Existence.* Let
\[
R \coloneqq \{ a - qn : q \in \nZ \} \cap \{ x \in \nZ : x \ge 0 \} ,
\]
the set of non-negative integers of the form \( a - qn \) (each \( a - qn \) is an integer by @prp-integers-closed (a)). The set \( R \) is non-empty. If \( a \ge 0 \), take \( q = 0 \): then \( a - 0 \cdot n = a \in R \). If \( a < 0 \), take \( q = a \): then \( a - an = a(1 - n) \ge 0 \), since \( a < 0 \) and \( 1 - n \le 0 \) (as \( n \ge 1 \) by @prp-integers-closed (b)). The set \( R \) is a non-empty set of integers with the integer lower bound \( 0 \), so by @cor-well-ordering-integers it has a least element \( r \); write \( r = a - qn \) with \( q \in \nZ \). Then \( a = qn + r \) and \( r \ge 0 \).

Suppose \( r \ge n \). Then \( r - n = a - (q + 1)n \) is an integer of the required form with \( r - n \ge 0 \), so \( r - n \in R \); and \( r - n < r \), since \( n > 0 \). This contradicts the choice of \( r \). Hence \( r < n \).

*Uniqueness.* Let \( a = qn + r = q'n + r' \) with \( q, q', r, r' \in \nZ \), \( 0 \le r < n \) and \( 0 \le r' < n \). Suppose \( r \ne r' \). By symmetry (exchanging \( (q, r) \) and \( (q', r') \) changes neither the hypotheses nor the goal) we may suppose \( r' < r \). Then \( r - r' = (q' - q)n \), and \( k \coloneqq q' - q \) is an integer with \( kn = r - r' > 0 \). Since \( n > 0 \), also \( k > 0 \), so \( k \ge 1 \) by @prp-integers-closed (b), and
\[
r - r' = kn \ge n .
\]
But \( r - r' \le r < n \), since \( r' \ge 0 \). This contradiction shows \( r = r' \). Then \( qn = q'n \), and since \( n \ne 0 \), \( q = q' \). This proves the theorem.
:::

The integers \( q \) and \( r \) are the **quotient** and the **remainder** of \( a \) on division by \( n \). For negative \( a \) the remainder is still non-negative: \( -7 = 3 \cdot (-3) + 2 \), with remainder \( 2 \), not \( -1 \). Existence and uniqueness do separate jobs, and the case \( n = 2 \) shows both:

- **Existence** says that every integer \( a \) is \( 2q \) or \( 2q + 1 \): every integer is **even or odd**.
- **Uniqueness** says that no integer is both. If \( a = 2q = 2q' + 1 \), then \( a \) would have remainders \( 0 \) and \( 1 \).

Section 1.1 proved this by induction (@thm-even-or-odd); here it falls out of the division algorithm with \( n = 2 \). *Logic and Proof* used it in Argument A of Chapter 1 and in the proof of @fd1:thm-square-even-implies-even. The same uniqueness shows that no integer \( m \) has \( 2m = 1 \), since \( 1 = 2 \cdot 0 + 1 \) has remainder \( 1 \) and \( 2m = 2m + 0 \) has remainder \( 0 \); this is the fact *Analysis on the Real Line*, Chapter 1 uses to show that \( \nZ \) is not a field. An integer \( 4k + 1 = 2(2k) + 1 \) or \( 4k + 3 = 2(2k + 1) + 1 \) is odd. With \( n = 3 \), every integer is \( 3k \), \( 3k + 1 \) or \( 3k + 2 \), for exactly one of the three forms.

::: {.warning}
"The remainder" is the \( r \) of the theorem, with \( 0 \le r < n \). The equations \( 17 = 5 \cdot 4 - 3 \) and \( 17 = 5 \cdot 2 + 7 \) are true, but \( -3 \) and \( 7 \) are not remainders, and allowing them destroys uniqueness: \( 17 \) would have the three "remainders" \( -3 \), \( 2 \) and \( 7 \). Every argument above that concludes from "remainder \( 1 \)" that a number is not a multiple of \( 2 \) uses the range \( 0 \le r < n \), through uniqueness.
:::

## Lowest terms and prime factors

*Logic and Proof*, Chapter 2 needed one more fact about fractions, the fact (L) in the proof of @fd1:thm-sqrt2-irrational: every rational number can be written with numerator and denominator not both even. The reason given there was that halving cannot go on for ever. Here is that reason as a proof. It supposes the claim fails, takes the least failure and derives a contradiction: a proof by **smallest counterexample**, the method of @exm-method-least-element applied to the set of failures. Section 2.4 makes it a method of its own; here its steps are named as they occur.

::: {#lem-lowest-terms}
[Lowest Terms, Up to Factors of Two]

Every rational number can be written as \( p/q \) with \( p \in \nZ \), \( q \in \nZ_{>0} \), and \( p \) and \( q \) **not both** even.
:::

::: {.idea}
A representation with both entries even can be halved. Halving makes the denominator smaller, so a least denominator cannot belong to a representation that can be halved. Well-ordering supplies the least denominator.
:::

::: {.proof}
*Suppose it fails.* Fix \( r \in \nQ \), and suppose that \( r \) has no representation \( p/q \) with \( p \in \nZ \), \( q \in \nZ_{>0} \), and \( p \) and \( q \) not both even. Let
\[
F \coloneqq \{ q \in \nZ_{>0} : r = p/q \text{ for some } p \in \nZ \} .
\]
Under the supposition, every \( q \in F \) is the denominator of a failing representation.

*Take the least failure.* By the definition of \( \nQ \), \( r = p/q \) for some \( p \in \nZ \) and \( q \in \nZ_{>0} \), so \( F \) is non-empty; and \( F \subseteq \nZ_{>0} \subseteq \nN \). By @thm-well-ordering, \( F \) has a least element \( m \). Write \( r = p/m \) with \( p \in \nZ \).

*Use the supposition at \( m \).* The representation \( r = p/m \) fails, so \( p \) and \( m \) are both even: \( p = 2p' \) and \( m = 2m' \) with \( p', m' \in \nZ \).

*Produce a smaller failure.* Since \( m > 0 \), \( m' = m/2 > 0 \), so \( m' \in \nZ_{>0} \) by @prp-integers-closed (b). Moreover \( r = 2p'/(2m') = p'/m' \), so \( m' \in F \); and \( m' < m' + m' = m \). So \( m' \) is an element of \( F \) smaller than its least element \( m \), a contradiction.

Hence \( r \) has a representation of the required kind. As \( r \in \nQ \) was arbitrary, this proves the lemma.
:::

This is (L), with more: the denominator can be taken positive, not merely non-zero. The proof of @fd1:thm-sqrt2-irrational now rests on a proved lemma. The same argument with "not both even" replaced by "no common divisor \( d \ge 2 \)" puts every fraction in lowest terms in the full sense; that is Exercise C2. This proof is written out in full; two later exercises use the same move with less given: Exercise B2 below leaves its last step blank, and Exercise C1 of Section 2.3 leaves the last half blank.

The next result is the prime-factor fact that *Logic and Proof*, Chapter 8 used. Its proof is a strong induction from base \( 2 \); the same argument inside an \( \rulename{RAA} \) box is a smallest-counterexample proof, in which the least failure \( m \) gets a prime factor from its divisor \( a \), contradicting the choice of \( m \) (compare Exercise B2).

::: {#thm-prime-factor}
[Every Integer at Least Two Has a Prime Factor]

Every integer \( n \ge 2 \) has a prime factor.
:::

::: {.idea}
A prime is its own prime factor. A number that is not prime has a divisor strictly between \( 1 \) and itself; that divisor is smaller, so it has a prime factor by the strong hypothesis, and divisibility passes it on.
:::

::: {.proof}
We use @thm-strong-induction-from-base with \( n_0 = 2 \). Let \( n \ge 2 \) be an integer, and suppose every integer \( k \) with \( 2 \le k < n \) has a prime factor.

If \( n \) is prime, then \( n \) is a prime factor of itself, since \( n = 1 \cdot n \).

If \( n \) is not prime, then, as \( n \ge 2 \), it has a positive divisor \( a \notin \{1, n\} \) (@def-prime). Write \( n = ka \) with \( k \in \nZ \). Since \( n > 0 \) and \( a > 0 \), also \( k > 0 \), so \( k \ge 1 \) and \( a \ge 1 \) by @prp-integers-closed (b). Hence \( a \le ka = n \). With \( a \ne 1 \) and \( a \ne n \) this gives \( 1 < a < n \), and so \( 2 \le a < n \) by the discreteness clause of @prp-integers-closed. By the hypothesis, \( a \) has a prime factor \( p \), say \( a = lp \) with \( l \in \nZ \). Then \( n = ka = (kl)p \), with \( kl \in \nZ \) by @prp-integers-closed (a), so \( p \mid n \).

In both cases \( n \) has a prime factor. By @thm-strong-induction-from-base, every integer \( n \ge 2 \) has one. This proves the theorem.
:::

The hypothesis was used at \( a \), which can be far below \( n - 1 \): for \( n = 91 = 7 \cdot 13 \) it is used at \( 7 \) or at \( 13 \). Ordinary induction, which offers only \( n - 1 \), would have nothing to say about \( 91 \) from \( 90 \).

## A gallery of broken inductions

An induction proof has few moving parts: a property, a base case, a step, and a citation of the right principle. Each can fail, and each failure has a place in the proof where it can be pointed at. Two questions are kept apart throughout: is the conclusion true, and does the argument prove it? Each entry below names the part that breaks.

::: {#exm-all-equal-induction}
[All Numbers Are Equal]

Here is a "theorem" and a "proof". Find the line that fails.

*"Theorem."* For every integer \( n \ge 1 \) and all real numbers \( x_1, \dots, x_n \), we have \( x_1 = x_2 = \dots = x_n \).

*"Proof."* For an integer \( n \ge 1 \), let \( P(n) \) be the statement "for all real numbers \( x_1, \dots, x_n \), all the entries of the list \( x_1, \dots, x_n \) are equal". We use @thm-induction with \( n_0 = 1 \).

::: {.enumerate options="label=(\arabic*)"}
1. *Base case.* A list \( x_1 \) of one number has only one entry, so all its entries are equal: \( P(1) \) holds.
2. *Step.* Let \( n \ge 1 \) be an integer, suppose \( P(n) \), and let \( x_1, \dots, x_{n+1} \) be real numbers.
3. The list \( x_1, \dots, x_n \) has \( n \) entries, so by \( P(n) \) its entries are all equal.
4. The list \( x_2, \dots, x_{n+1} \) has \( n \) entries, so by \( P(n) \) its entries are all equal.
5. The entry \( x_2 \) lies in both lists, so every entry of either list equals \( x_2 \).
6. Hence \( x_1 = x_2 = \dots = x_{n+1} \), which is \( P(n + 1) \). By @thm-induction, \( P(n) \) holds for every \( n \ge 1 \).
:::
:::

::: {.solution}
*Is the conclusion true?* No: the list \( x_1 = 0 \), \( x_2 = 1 \) has unequal entries, so \( P(2) \) is false.

*Does the argument prove it?* No, and the failing line is (5) at \( n = 1 \). Then the two lists of lines (3) and (4) are \( x_1 \) and \( x_2 \), one entry each, and \( x_2 \) is not in the first. They share an entry exactly when the first list, \( x_1, \dots, x_n \), contains \( x_2 \), that is, when \( n \ge 2 \). In the terms of @fd1:exm-not-allowed-catalogue, line (5) cites a "fact" that is false in the case at hand: entry (N9).

Everything else is correct. The base case (1) is true. For every \( n \ge 2 \) the step (2)–(6) is valid: if all lists of \( n \) reals had equal entries, so would all lists of \( n + 1 \). So the induction fails at exactly one transition, from \( 1 \) to \( 2 \), and the valid transitions from \( 2 \) on carry nothing, because \( P(2) \) is false and every later \( P(n) \) with it. A counterexample to the illegal step, as opposed to the conclusion: \( n = 1 \), \( x_1 = 0 \), \( x_2 = 1 \), where lines (3) and (4) hold and (5) does not.

| statement | true? | proved by the argument? |
|---|---|---|
| \( P(1) \) | yes | yes, line (1) |
| \( P(1) \Rightarrow P(2) \) | no | no: line (5) fails |
| \( P(n) \Rightarrow P(n + 1) \) for \( n \ge 2 \) | yes | yes, lines (2)–(6) |
| \( P(n) \) for every \( n \ge 1 \) | no | no |

This is the failure that *Logic and Proof*, Chapter 4's warning about \( 2^n \ge n^2 \) foreshadowed: a step that holds only from some point on, with a gap at the first transition. A step must be proved for **every** \( n \ge n_0 \), and the place to look for a gap is the smallest \( n \), where the objects the step talks about are smallest.
:::

The other failures are quicker to state.

**The missing base case.** "\( n = n + 1 \) for every \( n \in \nN \)." The step is valid: if \( n = n + 1 \), adding \( 1 \) to both sides gives \( n + 1 = n + 2 \). But \( P(0) \), "\( 0 = 1 \)", is false, and so is every \( P(n) \). The step is a true implication between false statements, and an induction with no true base proves nothing.

**The step run backwards.** Claim: \( n^2 \ge 2n \) for every integer \( n \ge 2 \). \"Step: \( (n + 1)^2 \ge 2(n + 1) \) gives \( n^2 + 2n + 1 \ge 2n + 2 \), so \( n^2 \ge 1 \), which is true.\" This starts from \( P(n + 1) \) and ends at a true statement, so it shows only that \( P(n + 1) \) implies something true, which every statement does (N5). Here each line can be reversed, and written forwards (\( n^2 \ge 1 \), so \( (n + 1)^2 = n^2 + 2n + 1 \ge 2n + 2 \)) it is a valid step, though one that never uses \( P(n) \). In general a backward chain cannot be reversed: from the false \( 1 = -1 \), squaring gives the true \( 1 = 1 \).

**The hypothesis used out of range.** A strong induction from a base \( n_0 \) may use \( P(k) \) only for \( n_0 \le k < n \). A step that writes \( n \) in terms of \( n - 3 \) needs \( n - 3 \ge n_0 \), and for the first few \( n \) that fails. @fd1:exm-threes-and-fives handled this correctly, with three base cases; the exit check C1 below is a proof that did not.

**The claim too weak to carry its own step.** Sometimes the statement is true and the base case holds, but the inductive step cannot be completed, because the hypothesis gives too little. The repair is to prove **more**. Section 2.3 shows a sum bounded by \( 2 \) whose own step will not go through, and which a stronger bound carries.

::: {.warning}
The induction hypothesis is "\( P(n) \)" for one fixed but arbitrary \( n \): the assumption of the \( \rulename{{\to}I} \) box inside the \( \rulename{\forall I} \) box of the step (@fd1:def-rules-universal). A step that begins "assume that \( P(n) \) holds for every \( n \)" assumes the conclusion of the theorem, and whatever follows is circular: entry (N9) of @fd1:exm-not-allowed-catalogue. The witness is a "for every \( n \)" in the assumption that binds the induction variable \( n \) itself; it should not be there. A quantifier over another variable is part of the statement and may stay: "for every \( k \) with \( n_0 \le k < n \)" in strong induction, or the "for every \( n \)" inside \( P(m) \) in the proof of @lem-naturals-arithmetic (d), where the induction is on \( m \).
:::

::: {.check}
A proof that \( n^2 \le 2^n \) for every integer \( n \ge 4 \) checks \( n = 4 \) and proves the step \( 2n^2 \ge (n + 1)^2 \) for \( n \ge 3 \). Is it complete? A second proof of "\( n^2 \le 2^n \) for every \( n \in \nN \)" uses base \( 0 \) and the same step. Which entry of the gallery does it commit?
:::

::: {.solution}
The first is complete: \( 16 \le 16 \), and the step is proved for every \( n \ge 4 \). The second has a true base but a step proved only from \( 3 \) on, so the transitions \( 0 \to 1 \), \( 1 \to 2 \), \( 2 \to 3 \) are unproved: a step valid only from some point on, as in @exm-all-equal-induction. Its conclusion is false at \( 3 \) (\( 9 > 8 \)). This is *Logic and Proof*, Chapter 4's warning about \( 2^n \ge n^2 \) (recalled at the end of @exm-all-equal-induction), made precise at the level of the step.
:::

## Exercises

### A. Check your understanding

::: {#exr-induction-in-practice-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. For each claim, name the form of proof that fits it most naturally (ordinary induction from \( 0 \), induction from another base, strong induction from a base with several base cases, or a smallest counterexample), and say in one clause why. Do not prove the claims. (i) \( 6 \mid 7^n - 1 \) for every \( n \in \nN \). (ii) \( 2^n > n^2 \) for every integer \( n \ge 5 \). (iii) Every integer \( n \ge 12 \) is \( 3a + 7b \) for some integers \( a, b \ge 0 \). (iv) There are no \( m, n \in \nZ_{>0} \) with \( n^2 = 2m^2 \).
2. Negate "every integer \( n \ge 2 \) has a prime factor", and say what a smallest counterexample to it would be.
3. In @exm-all-equal-induction, what is the smallest \( n \) for which the two lists \( x_1, \dots, x_n \) and \( x_2, \dots, x_{n+1} \) of lines (3) and (4) share an entry?
4. *Find the error.* Here is a "proof" that \( a^n = 1 \) for every real \( a \ne 0 \) and every \( n \in \nN \); the powers \( a^n \), \( a^0 = 1 \) and \( a^{-1} = 1/a \) have their school meaning (Section 2.3 defines \( a^n \) for \( n \in \nN \) only, so negative exponents lie outside that definition). "Fix \( a \ne 0 \). Base: \( a^0 = 1 \). Step: let \( n \in \nN \) and suppose \( a^k = 1 \) for every \( k \in \nN \) with \( k \le n \). Then \( a^{n+1} = a^n \cdot a^n / a^{n-1} = 1 \cdot 1 / 1 = 1 \)." The conclusion is false (take \( a = 2 \), \( n = 1 \)). Which transition fails, and why?
:::
:::

::: {.solution}
*(a)* (i) Ordinary induction from \( 0 \): the step takes out one factor \( 7 \) and leaves a multiple of \( 6 \), as in the example \( 7 \mid 9^n - 2^n \) in the subsection on finding the step. (ii) Induction from base \( 5 \) (@thm-induction): the claim fails at \( n = 2, 3, 4 \), so it cannot start at \( 0 \), and the step \( 2^{n+1} = 2 \cdot 2^n > 2n^2 \ge (n + 1)^2 \) works for \( n \ge 5 \). (iii) Strong induction from base \( 12 \) with three base cases \( 12 = 3 \cdot 4 \), \( 13 = 3 \cdot 2 + 7 \), \( 14 = 7 \cdot 2 \): the step reaches back three, from \( n \) to \( n - 3 \). (iv) A smallest counterexample: in a solution \( (m, n) \) with least \( n \), \( n^2 \) is even, so \( n = 2n' \) is even (@fd1:thm-square-even-implies-even), and then \( m^2 = 2n'^2 \), so \( (n', m) \) is a solution (\( n' = n/2 > 0 \)) whose second entry \( m \) is smaller than \( n \), since \( n^2 = 2m^2 > m^2 \) and \( m, n > 0 \). (Strong induction would also do; the forms are interchangeable, and the answers above name the natural fit.)

*(b)* The negation is: there is an integer \( n \ge 2 \) with no prime factor. A smallest counterexample would be an integer \( m \ge 2 \) with no prime factor such that every integer \( k \) with \( 2 \le k < m \) has one.

*(c)* \( n = 2 \). For \( n = 1 \) the lists are \( x_1 \) and \( x_2 \); for \( n \ge 2 \) both contain \( x_2 \).

*(d)* The transition from \( 0 \) to \( 1 \) fails. At \( n = 0 \) the step writes \( a^1 = a^0 \cdot a^0 / a^{-1} \) and uses \( a^{-1} = 1 \), which is "\( P(-1) \)"; but the hypothesis covers only \( k \in \nN \) with \( k \le 0 \), that is, \( k = 0 \), and \( -1 \notin \nN \). In fact \( a^{-1} = 1/a \ne 1 \) unless \( a = 1 \). The base case \( a^0 = 1 \) is true, and every transition from \( n \ge 1 \) on is valid, since then \( n - 1 \in \nN \) and \( n - 1 \le n \), and \( a^n a^n / a^{n-1} = a^{n+1} \) for \( n \ge 1 \). As in @exm-all-equal-induction, the valid transitions carry nothing, because \( P(1) \) is already false.
:::

### B. Practice

::: {#exr-induction-in-practice-b1}
[B1]

Prove that \( 3 \mid n^3 + 2n \) for every \( n \in \nN \).
:::

::: {.solution}
For \( n \in \nN \), let \( P(n) \) be "there is \( k \in \nZ \) with \( n^3 + 2n = 3k \)". *Base case:* \( 0^3 + 2 \cdot 0 = 0 = 3 \cdot 0 \). *Step:* let \( n \in \nN \) and suppose \( n^3 + 2n = 3k \) with \( k \in \nZ \). Expanding the cube,
\[
(n + 1)^3 + 2(n + 1) = (n^3 + 2n) + 3(n^2 + n + 1) = 3(k + n^2 + n + 1) ,
\]
and \( k + n^2 + n + 1 \in \nZ \) by @prp-integers-closed (a). So \( P(n + 1) \) holds. By @fd1:ax-induction, \( 3 \mid n^3 + 2n \) for every \( n \in \nN \). The step is the move of @exm-method-induction-step with no power of the form \( a^n \): the old expression plus a new piece that is visibly a multiple of \( 3 \).
:::

::: {#exr-induction-in-practice-b2}
[B2: Products of primes, used later]

An integer is a **product of primes** if it equals \( p_1 p_2 \cdots p_k \) for some \( k \ge 1 \) and primes \( p_1, \dots, p_k \) (a single prime counts, with \( k = 1 \)). Here \( p_1 p_2 \cdots p_k \) has its school meaning, and multiplying two such products gives the product of the joined list; Section 2.3 defines finite products (@def-sum-product). Here is a proof that every integer \( n \ge 2 \) is a product of primes, with its last step blank. *Name the move, then complete it.*

Suppose not. Then the set \( F \) of integers \( n \ge 2 \) that are not products of primes is non-empty and has the integer lower bound \( 2 \), so it has a least element \( m \) by @cor-well-ordering-integers. Since a prime is a product of primes, \( m \) is not prime; as \( m \ge 2 \), it has a positive divisor \( a \notin \{1, m\} \), and \( m = ab \) with \( b \in \nZ \). As in the proof of @thm-prime-factor, \( b > 0 \) and \( 2 \le a < m \). Since \( a < m = ab \) and \( a > 0 \), we get \( b > 1 \), so \( b \ge 2 \) by the discreteness clause of @prp-integers-closed; and since \( a \ge 2 \), \( b < 2b \le ab = m \). So \( 2 \le a < m \) and \( 2 \le b < m \), and as \( m \) is the least element of \( F \), neither \( a \) nor \( b \) lies in \( F \): both are products of primes.

\( \dots \)
:::

::: {.solution}
The move is the **smallest counterexample**, and the blank is the contradiction: the least failure \( m \) turns out not to be a failure, because its smaller factors are not failures (compare @lem-lowest-terms, where the contradiction is a smaller element of \( F \)). Write \( a = p_1 \cdots p_k \) and \( b = p'_1 \cdots p'_l \) with primes \( p_i \), \( p'_j \). Then
\[
m = ab = p_1 \cdots p_k \, p'_1 \cdots p'_l
\]
is a product of primes, which contradicts \( m \in F \). Hence \( F \) is empty, and every integer \( n \ge 2 \) is a product of primes.
:::

::: {#exr-induction-in-practice-b3}
[B3, used later]

::: {.enumerate options="label=(\alph*)"}
1. Find the quotient and remainder of @thm-division-algorithm for \( a = 17 \), \( n = 5 \), and for \( a = -17 \), \( n = 5 \).
2. Prove that the square of an odd integer leaves remainder \( 1 \) on division by \( 8 \).
3. Prove that if \( 2 \mid n \) and \( 3 \mid n \), then \( 6 \mid n \), for every integer \( n \).
:::

*Hint for (c): @thm-division-algorithm, dividing by \( 3 \).*
:::

::: {.solution}
*(a)* \( 17 = 5 \cdot 3 + 2 \), so \( q = 3 \), \( r = 2 \). And \( -17 = 5 \cdot (-4) + 3 \), so \( q = -4 \), \( r = 3 \); in both cases \( 0 \le r < 5 \), so by uniqueness these are the quotient and remainder. (Not \( -17 = 5 \cdot (-3) - 2 \): a remainder is never negative.)

*(b)* Let \( x = 2k + 1 \) with \( k \in \nZ \). Then \( x^2 = 4k^2 + 4k + 1 = 4k(k + 1) + 1 \). By @thm-division-algorithm with \( n = 2 \), \( k = 2j \) or \( k = 2j + 1 \) with \( j \in \nZ \). In the first case \( k(k + 1) = 2 \cdot j(2j + 1) \); in the second, \( k(k + 1) = (2j + 1)(2j + 2) = 2(2j + 1)(j + 1) \). Either way \( k(k + 1) = 2t \) with \( t \in \nZ \), so \( x^2 = 8t + 1 \). Since \( 0 \le 1 < 8 \), the uniqueness in @thm-division-algorithm says that the remainder of \( x^2 \) on division by \( 8 \) is \( 1 \).

*(c)* Let \( n = 2a \) with \( a \in \nZ \), and divide \( a \) by \( 3 \): \( a = 3q + r \) with \( q, r \in \nZ \) and \( 0 \le r < 3 \), so \( r \in \{0, 1, 2\} \) by discreteness. Then \( n = 6q + 2r \). Since \( 3 \mid n \), say \( n = 3s \) with \( s \in \nZ \), we get \( 2r = 3(s - 2q) \), so \( 3 \mid 2r \), where \( 2r \in \{0, 2, 4\} \). But \( 2 = 3 \cdot 0 + 2 \) and \( 4 = 3 \cdot 1 + 1 \) have non-zero remainders on division by \( 3 \), while a multiple \( 3t = 3t + 0 \) has remainder \( 0 \); by uniqueness, neither \( 2 \) nor \( 4 \) is a multiple of \( 3 \). So \( 2r = 0 \), \( r = 0 \), and \( n = 6q \): \( 6 \mid n \).
:::

::: {#exr-induction-in-practice-b4}
[B4: Prove or disprove]

Prove each true statement and refute each false one with a counterexample. Powers and finite sums have their school meaning (Section 2.3 defines them), as in the example \( 7 \mid 9^n - 2^n \).

::: {.enumerate options="label=(\alph*)"}
1. \( 3 \mid 2^{2n+1} + 1 \) for every \( n \in \nN \).
2. \( 2^n \ge n^3 \) for every integer \( n \ge 9 \).
3. \( 1 + 4 + 7 + \dots + (3n + 1) = (n + 1)(3n + 2)/2 \) for every \( n \in \nN \).
4. Every integer \( n \ge 10 \) is \( 3a + 7b \) for some integers \( a, b \ge 0 \).
5. \( 5^n \ge 4^n + 3^n \) for every integer \( n \ge 2 \).
6. \( n^2 + 1 \) is prime for every even integer \( n \ge 2 \).
:::
:::

::: {.solution}
(a) **True.** By @fd1:ax-induction. Base: \( 2^1 + 1 = 3 = 3 \cdot 1 \). Step: if \( 2^{2n+1} + 1 = 3k \) with \( k \in \nZ \), then
\[
2^{2n+3} + 1 = 4 \cdot 2^{2n+1} + 1 = 4(2^{2n+1} + 1) - 3 = 3(4k - 1) ,
\]
and \( 4k - 1 \in \nZ \).

(b) **False.** At \( n = 9 \): \( 2^9 = 512 < 729 = 9^3 \). (The inequality holds from \( 10 \) on: \( 2^{10} = 1024 \ge 1000 \), and \( 2n^3 \ge (n + 1)^3 \) for \( n \ge 10 \). The claim fails only at its base.)

(c) **True.** By @fd1:ax-induction. Base \( n = 0 \): \( 1 = 1 \cdot 2/2 \). Step: split off the last term. If the sum up to \( 3n + 1 \) is \( (n + 1)(3n + 2)/2 \), the sum up to \( 3(n + 1) + 1 = 3n + 4 \) is
\[
\frac{(n + 1)(3n + 2)}{2} + (3n + 4) = \frac{3n^2 + 11n + 10}{2} = \frac{(n + 2)(3n + 5)}{2} ,
\]
which is the formula at \( n + 1 \).

(d) **False.** Take \( n = 11 \). With \( b = 0 \) or \( b = 1 \) what is left, \( 11 - 7b \), is \( 11 \) or \( 4 \), and neither is a multiple of \( 3 \): \( 11 = 3 \cdot 3 + 2 \) and \( 4 = 3 \cdot 1 + 1 \) have non-zero remainders, so by the uniqueness in @thm-division-algorithm they are not of the form \( 3a + 0 \). With \( b \ge 2 \), \( 11 - 7b < 0 \), so \( a < 0 \).

(e) **True.** By @thm-induction with base \( 2 \). Base: \( 25 \ge 16 + 9 \). Step: let \( n \ge 2 \) with \( 5^n \ge 4^n + 3^n \). Then
\[
5^{n+1} = 5 \cdot 5^n \ge 5 \cdot 4^n + 5 \cdot 3^n \ge 4 \cdot 4^n + 3 \cdot 3^n = 4^{n+1} + 3^{n+1} .
\]
(The step works for every \( n \), but the inequality fails at \( n = 1 \), \( 5 < 7 \), and at \( n = 0 \), \( 1 < 2 \), and the claim is asserted only from \( 2 \), so the base is \( 2 \).)

(f) **False.** Take \( n = 8 \): \( 8^2 + 1 = 65 = 5 \cdot 13 \), with the positive divisor \( 5 \notin \{1, 65\} \). For \( n = 2, 4, 6 \) the values \( 5 \), \( 17 \), \( 37 \) are prime: three successes, then a failure (N1).
:::

### C. Going deeper

::: {#exr-induction-in-practice-c1}
[C1: Exit check: a flawed induction]

Here is a claim and a "proof".

*Claim.* Every integer \( n \ge 18 \) is \( 4a + 7b \) for some integers \( a, b \ge 0 \).

::: {.enumerate options="label=(\arabic*)"}
1. For an integer \( n \ge 18 \), let \( P(n) \) be "\( n = 4a + 7b \) for some integers \( a, b \ge 0 \)". We use strong induction from base \( 18 \) (@thm-strong-induction-from-base).
2. *Base case.* \( 18 = 4 \cdot 1 + 7 \cdot 2 \), so \( P(18) \) holds.
3. *Step.* Let \( n \ge 18 \) be an integer, and suppose \( P(k) \) holds for every integer \( k \) with \( 18 \le k \le n \).
4. Write \( n + 1 = (n - 3) + 4 \).
5. Since \( n - 3 < n \), the induction hypothesis gives \( n - 3 = 4a + 7b \) with integers \( a, b \ge 0 \).
6. Then \( n + 1 = 4(a + 1) + 7b \), with \( a + 1 \ge 0 \) and \( b \ge 0 \), so \( P(n + 1) \) holds.
7. By @thm-strong-induction-from-base, \( P(n) \) holds for every integer \( n \ge 18 \).
:::

Answer each question. (i) Is the claim true? (ii) Does the argument prove it? (iii) Which line fails, and for which \( n \)? (iv) Which rule does that line break? (v) Give a counterexample to the failing step, not merely to some conclusion. (vi) Repair the proof.
:::

::: {.solution}
*(i)* The claim is **true**. Directly,
\[
18 = 4 \cdot 1 + 7 \cdot 2 , \quad 19 = 4 \cdot 3 + 7 , \quad 20 = 4 \cdot 5 , \quad 21 = 7 \cdot 3 ,
\]
and from these four the repaired induction in (vi) reaches every larger integer.

*(ii)* The argument does **not** prove it, although its conclusion is true.

*(iii)* Line (5) fails for \( n = 18 \), \( 19 \) and \( 20 \). There \( n - 3 \) is \( 15 \), \( 16 \), \( 17 \), all below \( 18 \), and the induction hypothesis says nothing about them. For \( n \ge 21 \), \( 18 \le n - 3 < n \), and line (5) is correct. Lines (1)–(4), (6) and (7) are correct. Line (7) needs one remark, because the step is written from \( n \) to \( n + 1 \) and not in the theorem's own form. At \( N = 18 \) the theorem's hypothesis has a vacuous "if" part, so it asks for \( P(18) \) outright, which is line (2). At an integer \( N \ge 19 \), put \( n = N - 1 \ge 18 \). By the discreteness clause of @prp-integers-closed, the integers \( k \) with \( 18 \le k < N \) are exactly those with \( 18 \le k \le n \), so lines (3)–(6), were they valid for every \( n \ge 18 \), would prove the hypothesis at \( N \).

*(iv)* Line (5) applies \( \rulename{\forall E} \) to the hypothesis "for every integer \( k \) with \( 18 \le k \le n \), \( P(k) \)" at \( k = n - 3 \). That is a bounded quantifier, and its elimination needs the line "\( 18 \le n - 3 \)" (@fd1:prp-bounded-quantifier-rules); for \( n \le 20 \) that line is false. The proof checked only half of the bound, \( n - 3 < n \).

*(v)* Run the same argument with base \( 14 = 7 \cdot 2 \): it "proves" that every integer \( n \ge 14 \) is \( 4a + 7b \). That conclusion is false at \( 17 \): with \( b = 0, 1, 2 \) the remainder \( 17 - 7b \) is \( 17, 10, 3 \), none a multiple of \( 4 \), and \( b \ge 3 \) makes it negative. The step that breaks is line (5) at \( n = 16 \): it takes \( P(13) \) from the hypothesis, but \( 13 < 14 \) is outside it, and \( 13 \) is not of the form (\( 13 \) and \( 6 \) are not multiples of \( 4 \)). At \( n = 16 \) the induction hypothesis is true (\( 14 = 7 \cdot 2 \), \( 15 = 4 \cdot 2 + 7 \), \( 16 = 4 \cdot 4 \)), and the step concludes the false \( P(17) \). So line (5) is an illegal step, not merely an unlucky one.

*(vi)* Take four base cases, \( 18, 19, 20, 21 \), as in (i), and run the step only for \( n \ge 21 \), where \( n - 3 \ge 18 \). In the form of @thm-strong-induction-from-base: for \( n \in \{18, 19, 20, 21\} \), \( P(n) \) holds directly; for \( n \ge 22 \), \( n - 4 \ge 18 \) and \( n - 4 < n \), so the hypothesis gives \( n - 4 = 4a + 7b \) and \( n = 4(a + 1) + 7b \).

**Marking scheme.** (10 points)
- 2: judges the conclusion **true**, with the small cases \( 18 \), \( 19 \), \( 20 \), \( 21 \) written as \( 4a + 7b \).
- 3: identifies the failing line exactly: the appeal to the hypothesis for \( n - 3 \), for \( n = 18, 19, 20 \).
- 2: states the reason as a hypothesis used outside its range (\( \rulename{\forall E} \) at a \( k \) with \( k < 18 \)).
- 2: gives a counterexample **to the step**: the same step carrying a true statement to a false one (for example, base \( 14 \) and the failure at \( 17 \)), not merely a false conclusion.
- 1: gives a correct repair (four base cases, or any equivalent).
Fatal errors (0 for the item): calling the conclusion false; blaming the base case.
:::

::: {#exr-induction-in-practice-c2}
[C2: Lowest terms, used later]

Prove that every rational number can be written as \( p/q \) with \( p \in \nZ \), \( q \in \nZ_{>0} \), and no common divisor \( d \ge 2 \) of \( p \) and \( q \): there is no integer \( d \ge 2 \) with \( d \mid p \) and \( d \mid q \).
:::

::: {.solution}
[Hint 1]

Follow the proof of @lem-lowest-terms, step by step.
:::

::: {.solution}
[Hint 2]

Suppose \( r \in \nQ \) has no such representation, and let \( m \) be the least element of \( F \coloneqq \{ q \in \nZ_{>0} : r = p/q \text{ for some } p \in \nZ \} \).
:::

::: {.solution}
Fix \( r \in \nQ \), and suppose that \( r \) has no representation of the required kind. Let \( F \) be as in Hint 2. By the definition of \( \nQ \), \( F \) is non-empty, and \( F \subseteq \nZ_{>0} \subseteq \nN \), so by @thm-well-ordering it has a least element \( m \). Write \( r = p/m \) with \( p \in \nZ \).

By the supposition, this representation fails: there is an integer \( d \ge 2 \) with \( d \mid p \) and \( d \mid m \), say \( p = dp' \) and \( m = dm' \) with \( p', m' \in \nZ \). Since \( m > 0 \) and \( d > 0 \), \( m' = m/d > 0 \), so \( m' \in \nZ_{>0} \) by @prp-integers-closed (b). Then \( r = dp'/(dm') = p'/m' \), so \( m' \in F \). And \( m = dm' \ge 2m' > m' \), since \( d \ge 2 \) and \( m' > 0 \). So \( m' \) is an element of \( F \) smaller than its least element, a contradiction. Hence \( r \) has a representation \( p/q \) with no common divisor \( d \ge 2 \).

The statement contains @lem-lowest-terms, since \( d = 2 \) is one of the excluded common divisors. The only change in the proof is the size of the step down: \( m' = m/d \) instead of \( m/2 \), and \( d \ge 2 \) is what makes it a step **down**.

**Marking scheme.** (10 points)
- 2: sets up the smallest counterexample: fixes \( r \), supposes no good representation, and defines the set of denominators.
- 2: shows that set is a non-empty subset of \( \nN \) and takes its least element by @thm-well-ordering.
- 3: extracts the common divisor \( d \ge 2 \) and writes the reduced representation \( p'/m' \), checking \( m' \in \nZ_{>0} \).
- 2: shows \( m' < m \), using \( d \ge 2 \) and \( m' > 0 \).
- 1: concludes, with the contradiction to the choice of \( m \).
A strong induction on the denominator earns the same points step for step. Fatal errors (0 for the step): taking a least element of a set not shown to lie in \( \nN \); dividing by \( d \) without \( d \ne 0 \).
:::

::: {#exr-induction-in-practice-c3}
[C3: Smallest, not largest]

::: {.enumerate options="label=(\alph*)"}
1. Prove that a set \( A \subseteq \nR \) has at most one least element.
2. Deduce that a claim "\( P(n) \) for every \( n \in \nN \)" that is false has exactly one smallest counterexample.
3. Show that a false claim about \( \nN \) need not have a **largest** counterexample, by examining the claim "\( n < 5 \) for every \( n \in \nN \)".
:::
:::

::: {.solution}
*(a)* Let \( m \) and \( m' \) be least elements of \( A \). Since \( m' \in A \) and \( m \) is least, \( m \le m' \); since \( m \in A \) and \( m' \) is least, \( m' \le m \). Hence \( m = m' \).

*(b)* The smallest counterexamples are the least elements of the set \( F \coloneqq \{ n \in \nN : P(n) \text{ is false} \} \). The claim is false, so \( F \) is non-empty, and @thm-well-ordering gives a least element. By (a), there is only one.

*(c)* The claim is false, and its counterexamples form \( F = \{ n \in \nN : n \ge 5 \} \), which is non-empty. It has no greatest element: for every \( n \in F \), also \( n + 1 \in \nN \) by (\( \nN \)S), and \( n + 1 \ge 5 \), so \( n + 1 \in F \) and \( n + 1 > n \). So the claim has a smallest counterexample, \( 5 \), and no largest one. Well-ordering has no upward twin in \( \nN \): a non-empty subset of \( \nN \) has a greatest element when it is bounded above (@exr-naturals-and-well-ordering-c1), and not in general.
:::

<!-- dependency ledger
thm-induction (proof): n0 + k >= n0 from k >= 0; n + 1 = n0 + (k + 1) | R arithmetic and order, school fact; axioms in AN1.1
thm-strong-induction-from-base (proof): n0 <= k < n0 + j gives 0 <= k - n0 < j | R arithmetic and order, school fact; axioms in AN1.1
def-divides (example): (this section's subsection on divisibility, 3 does not divide 14) 4 < 14/3 < 5 | R arithmetic, school fact
def-divides (example): (this section's subsection on finding the step) 9^0 = 2^0 = 1, a^(n+1) = a^n * a, 9^n and 2^n integers (the example 7 | 9^n - 2^n) | powers, school meaning; def-power in F2.2 §03
exm-choosing-the-base (solution): 2n^3 >= 6n^2 >= 3n^2 + 9n >= 3n^2 + 3n + 1 for n >= 3; (n + 1)^3 expanded; 3^(n+1) = 3 * 3^n | R arithmetic and order, school fact; powers, school meaning
thm-division-algorithm (proof): a(1 - n) >= 0 for a < 0, n >= 1; r - n < r for n > 0; k > 0 from kn > 0, n > 0; cancellation qn = q'n, n != 0 | R arithmetic and order, school fact; axioms in AN1.1
thm-division-algorithm (proof): "by symmetry" for the exchange of (q, r) and (q', r') | exm-rhetoric-induction (b) (F1.5, the conditions for a legitimate symmetry); stated inline
thm-division-algorithm (claim): (aftermath) even and odd defined as 2k and 2k + 1 | F1.1 §01, F1.2 §01 (definitions recalled there)
lem-lowest-terms (proof): m' = m/2 > 0; m' < m' + m' = m; 2p'/(2m') = p'/m' | R arithmetic and order, school fact
thm-prime-factor (proof): k > 0 from n = ka, n > 0, a > 0; a <= ka for k >= 1, a > 0 | R arithmetic and order, school fact
exr-induction-in-practice-a1 (solution): (a)(ii) 2n^2 >= (n + 1)^2 for n >= 3; (a)(iv) n' = n/2 > 0; n^2 > m^2, m, n > 0 => n > m; (d) a^(n+1) = a^n a^n / a^(n-1) for n >= 1, a^(-1) = 1/a | powers, school meaning (negative exponents outside def-power, said in the item); R arithmetic
exr-induction-in-practice-b1 (solution): (n + 1)^3 expanded | R arithmetic, school fact
exr-induction-in-practice-b2 (solution): a product of two products of primes is a product of primes (concatenating the lists) | inline; products of finite lists defined in F2.2 §03 (def-sum-product), used here in their school meaning (said in the item); b > 1 from a < ab, a > 0; b < 2b <= ab for b > 0, a >= 2 | R arithmetic and order, school fact
exr-induction-in-practice-b3 (solution): (b) x^2 = 4k(k + 1) + 1; (c) n = 6q + 2r | R arithmetic, school fact
exr-induction-in-practice-b4 (solution): 2^(2n+3) = 4 * 2^(2n+1); 2n^3 >= (n + 1)^3 for n >= 10; (3n^2 + 11n + 10)/2 = (n + 2)(3n + 5)/2; 5 * 4^n >= 4 * 4^n; 65 = 5 * 13; (c) sum up to 3(n+1)+1 = sum up to 3n+1 plus 3n+4 | powers and finite sums, school meaning (said in the item; def-sum-product in F2.2 §03); R arithmetic and order, school fact
exr-induction-in-practice-c1 (solution): representability of 13, 15, 16, 17, 18-21 | arithmetic; checked in the solution. (i) every n >= 22 representable | the repaired induction in (vi) (cited inline)
exr-induction-in-practice-c2 (solution): m' = m/d > 0; dm' >= 2m' > m' | R arithmetic and order, school fact
-->
