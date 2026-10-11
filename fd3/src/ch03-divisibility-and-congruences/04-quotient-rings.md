# Ideals, Quotient Rings, and the Integers Modulo n

*Sets, Relations, and Cardinality*, Section 2.5 turned the school integers into a clock, \( \nZ/n \), and checked by hand that its sum and product are well defined (@fd2:prp-congruence-arithmetic). Chapter 2 made the same kind of check twice more, for \( \nZ \) and for \( \nQ \), each time through @thm-well-defined-on-classes and a computation special to the formula. This section makes the check **once**, for every commutative ring and every subset of the right kind, called an ideal. The integers modulo \( n \), now a ring, are the first example. Chapter 5 builds \( \nR \) in the same shape, from classes of Cauchy sequences of rationals that differ by a null sequence, and checks its operations there directly; *Algebraic Preliminaries*, Chapter 5 runs division with remainder, gcd and unique factorization again for polynomials over a field.

Throughout, \( R \) is a commutative ring (@def-commutative-ring-and-field), with \( a - b \coloneqq a + (-b) \).

## What a quotient needs

Let \( I \subseteq R \), and call \( a \) and \( b \) related when they differ by an element of \( I \):
\[
a \sim_I b \quad :\Longleftrightarrow \quad a - b \in I .
\]
For \( R = \nZ \) and \( I \) the multiples of \( n \), this is congruence modulo \( n \). We want two things: \( \sim_I \) should be an equivalence relation, and the sum and product of classes should be computable on representatives. Each wish makes a demand on \( I \).

- **Reflexivity**, \( a - a \in I \), needs \( 0 \in I \).
- **Symmetry**: \( b - a = -(a - b) \), so it needs \( I \) to be closed under negatives.
- **Transitivity**: \( a - c = (a - b) + (b - c) \), so it needs \( I \) to be closed under sums.
- **The sum on classes.** Changing \( a \) to \( a' \) changes \( a + b \) to \( a' + b \), and the difference is \( a - a' \) again: no new demand.
- **The product on classes.** Changing \( a \) to \( a' \) changes \( ab \) to \( a'b \), and the difference is \( (a - a')b \): an element of \( I \) multiplied by an **arbitrary** element of \( R \). So \( I \) must swallow such products.

The last demand contains the second: \( -x = (-1)x \). Three clauses remain, and they get a name.

*An ideal is a set of allowed errors: it contains \( 0 \), it is closed under adding errors, and an error multiplied by anything is still an error.*

::: {#def-ideal-commutative-ring}
[Ideal]

Let \( R \) be a commutative ring. A subset \( I \subseteq R \) is an **ideal** of \( R \) if

::: {.enumerate options="label=(I\arabic*)"}
1. \( 0 \in I \);
2. **for all** \( a, b \in I \), \( a + b \in I \);
3. **for all** \( a \in I \) and **all** \( r \in R \), \( ra \in I \).
:::
:::

In words: (I1) and (I2) say that \( I \) contains \( 0 \) and is closed under addition; (I3), **absorption**, says that multiplying an element of \( I \) by any element of the ring, inside \( I \) or not, lands in \( I \). The ring element \( r \) in (I3) ranges over all of \( R \), and that is what separates (I3) from mere closure under multiplication, where \( r \) would have to lie in \( I \).

Two consequences are used constantly. First, an ideal is closed under negatives and differences: for \( a \in I \), \( -a = (-1)a \in I \) by (I3), since \( (-1)a = -(1 \cdot a) = -a \) by @prp-ring-algebra (c) and (F7) with (F6); then \( a - b = a + (-b) \in I \) for \( a, b \in I \), by (I2). Second, if \( 1 \in I \), then \( I = R \), since every \( r = r \cdot 1 \in I \) by (I3).

**Examples.**

- The degenerate cases: \( \{0\} \) and \( R \) itself are ideals of \( R \). For \( \{0\} \): \( 0 + 0 = 0 \) and \( r \cdot 0 = 0 \) (@prp-ring-algebra (b)). For \( R \), every clause asks for an element of \( R \). They are the two extremes: "no error allowed" and "everything allowed".
- For \( n \in \nZ \), the multiples \( n\nZ = \{ kn : k \in \nZ \} \) form an ideal of \( \nZ \) (@def-integer-linear-combinations): \( 0 = 0 \cdot n \); \( kn + ln = (k + l)n \); \( r(kn) = (rk)n \). In particular the even integers \( 2\nZ \) form an ideal.
- For \( a, b \in \nZ \), the combinations \( a\nZ + b\nZ \) form an ideal of \( \nZ \), by the closure properties in @def-integer-linear-combinations; @thm-integer-ideals-principal below records this.

**Non-examples by minimal change.** \( \nN \subseteq \nZ \) satisfies (I1) and (I2), but (I3) fails at \( a = 1 \), \( r = -1 \): \( (-1) \cdot 1 = -1 \notin \nN \), since \( -1 < 0 \) (\( 1 > 0 \) by @prp-ordered-ring-rules (e), as \( 1 \ne 0 \) in \( \nZ \) by @thm-integers-commutative-ring, then (a)) while \( \nN = \{ x \in \nZ : x \ge 0 \} \) (@thm-integers-ordered-ring (b)). And \( \nZ \subseteq \nQ \) satisfies (I1), (I2) and is even closed under negatives and products, but (I3) fails at \( a = 1 \), \( r = 1/2 \): \( (1/2) \cdot 1 = 1/2 \notin \nZ \). (If \( 1/2 = m \in \nZ \), then \( 2m = 1 \), but \( 1 = 2 \cdot 0 + 1 \) is odd and so not of the form \( 2m \), by @cor-integers-even-odd (a).) In both cases the ring element \( r \) comes from **outside** the subset, which is exactly what (I3) allows.

**Why these clauses.** Each clause was forced by one of the five wishes above, and dropping one loses its wish: without (I1) or (I2), \( \sim_I \) is not reflexive or not transitive; without (I3), the product on classes can fail, as the warning after the next theorem shows for \( \nZ \subseteq \nQ \).

## The quotient ring

The payoff is a single theorem that builds a ring of classes from any ideal. We write \( [a] \), or \( [a]_I \) when the ideal must be named, for the class of \( a \) under \( \sim_I \), and \( R/I \) for the quotient set \( R/{\sim_I} \) (@fd2:def-quotient-set).

::: {#thm-quotient-ring-by-ideal}
[Quotient Ring by an Ideal]

Let \( R \) be a commutative ring and \( I \) an ideal of \( R \).

::: {.enumerate options="label=(\alph*)"}
1. Setting \( a \sim_I b \iff a - b \in I \) defines an equivalence relation \( \sim_I \) on \( R \), and the class of \( a \) is \( [a] = a + I \coloneqq \{ a + x : x \in I \} \).
2. The rules \( [a] + [b] \coloneqq [a + b] \), \( [a] \cdot [b] \coloneqq [ab] \) and \( -[a] \coloneqq [-a] \) are well defined on \( R/I \coloneqq R/{\sim_I} \).
3. \( R/I \), with these operations, is a commutative ring with zero \( [0] \) and one \( [1] \). The **quotient map** \( \pi \colon R \to R/I \), \( \pi(a) \coloneqq [a] \), satisfies \( \pi(a + b) = \pi(a) + \pi(b) \), \( \pi(ab) = \pi(a) \pi(b) \) and \( \pi(1) = [1] \).
4. \( [a] = [0] \) if and only if \( a \in I \). In particular \( [1] = [0] \) if and only if \( I = R \).
:::
:::

In words: (a) and (b) say that classes modulo an ideal can be added, multiplied and negated through any representatives; (c) says that the result obeys every ring law, and that passing to classes respects the operations; (d) says that the elements of \( I \) are exactly those that become \( 0 \), and that the quotient collapses to the zero ring exactly when \( I \) is everything.

::: {.idea}
A change of representative is an element of \( I \). The equivalence-relation clauses ask that such changes can be reversed and chained, which is closure under negatives and sums. The operations ask that a change in one argument produce a change in the output: for the sum the change is the same element of \( I \), and for the product it is that element multiplied by the other argument, which (I3) keeps in \( I \). The ring laws are then laws of \( R \) read on classes.

*Before reading on: where is "\( ra \in I \) for every \( r \in R \)" used, and why does closure under \( + \) not suffice for the product?*
:::

::: {.proof}
*(a)* Let \( a, b, c \in R \). (Eq1): \( a - a = 0 \in I \), by (F4) and (I1). (Eq2): if \( a - b \in I \), then \( b - a = -(a - b) \in I \), since \( I \) is closed under negatives; here \( (a - b) + (b - a) = 0 \) by (F1)–(F4), so \( b - a = -(a - b) \) by the uniqueness of negatives (@prp-ring-algebra (a)). (Eq3): if \( a - b \in I \) and \( b - c \in I \), then \( a - c = (a - b) + (b - c) \in I \), by (F2)–(F4) and (I2). So \( \sim_I \) is an equivalence relation (@fd2:def-equivalence-relation). For the class: if \( x \sim_I a \), then \( x - a \in I \) and \( x = a + (x - a) \in a + I \); conversely, for \( y \in I \), \( (a + y) - a = y \in I \), so \( a + y \sim_I a \). Hence \( [a] = a + I \).

*(b)* We check the hypotheses of @thm-well-defined-on-classes (b), with \( X = R \) and the relation \( \sim_I \), for the maps \( (a, b) \mapsto a + b \) and \( (a, b) \mapsto ab \). Let \( a \sim_I a' \), so \( a - a' \in I \), and let \( b \in R \). Then
\[
\begin{aligned}
(a + b) - (a' + b) &= a - a' \in I , \\
ab - a'b &= (a - a')b = b(a - a') \in I ,
\end{aligned}
\]
by (F1)–(F4) in the first line, and by (F9), (F6) and @prp-ring-algebra (c) in the second, where the membership is (I3) with \( r = b \): **the ideal absorbs \( b \)**. This is the first hypothesis. Since \( a + b = b + a \) and \( ab = ba \) ((F1), (F6)), the second hypothesis is the first with the two arguments exchanged. For the negative we check the hypothesis of @thm-well-defined-on-classes (a) for \( a \mapsto -a \): \( (-a) - (-a') = -(a - a') \in I \), by @prp-ring-algebra (a) and closure under negatives. Hence the three rules define functions.

*(c)* Every element of \( R/I \) is a class \( [a] \) (@fd2:def-quotient-set). Each axiom of @def-commutative-ring-and-field other than (F8) is an equation, and by (b) both of its sides, read on classes, are the classes of the two sides of the same equation in \( R \). For example, for (F9),
\[
[a]\bigl([b] + [c]\bigr) = [a][b + c] = [a(b + c)] = [ab + ac] = [ab] + [ac] = [a][b] + [a][c] ,
\]
using (F9) in \( R \) in the middle; for (F3), \( [a] + [0] = [a + 0] = [a] \); for (F4), \( [a] + (-[a]) = [a] + [-a] = [a + (-a)] = [0] \); for (F7), \( [a][1] = [a \cdot 1] = [a] \). The laws (F1), (F2), (F5) and (F6) go the same way. So \( R/I \) is a commutative ring with zero \( [0] \) and one \( [1] \). The equations for \( \pi \) are the definitions in (b) read from right to left, and \( \pi(1) = [1] \) by definition of \( \pi \).

*(d)* \( [a] = [0] \) holds if and only if \( a \sim_I 0 \) (@fd2:thm-classes-partition (b)), that is, \( a - 0 \in I \); and \( a - 0 = a + 0 = a \), since \( -0 = 0 \) (\( 0 + 0 = 0 \) and @prp-ring-algebra (a)). So \( [a] = [0] \iff a \in I \). In particular \( [1] = [0] \iff 1 \in I \). If \( 1 \in I \), then \( I = R \), since \( r = r \cdot 1 \in I \) for every \( r \in R \) by (I3); and if \( I = R \), then \( 1 \in I \). This proves the theorem.
:::

The answer to the prompt. Absorption with an arbitrary \( r \in R \), the full force of (I3), is used exactly once in the proof of (a) and (b): in the product, at \( ab - a'b = (a - a')b \), where the change of representative \( a - a' \in I \) is multiplied by an arbitrary \( b \in R \). Elsewhere (I3) enters only with \( r = -1 \), through closure under negatives (\( -x = (-1)x \)), and otherwise the proof uses (I1) and (I2). Closure under \( + \) does not suffice for the product because \( b \) need not lie in \( I \): the product changes by a multiple of the error, not by a sum of errors.

We call this move **compute on representatives; the ideal absorbs the change**. It is the move of Chapter 2's "one argument at a time", now with the change of representative recorded as one element of \( I \).

::: {.warning}
**Closure under \( + \) and \( - \) is not enough for the product.** \( \nZ \subseteq \nQ \) contains \( 0 \) and is closed under sums and negatives, and these are all that the proof of (a) and of the sum and negative in (b) used. So "\( x - y \in \nZ \)" relates rationals by an equivalence relation, and \( [x] + [y] \coloneqq [x + y] \) is well defined on its classes. But \( [x][y] \coloneqq [xy] \) is **not**: \( [1/2] = [3/2] \), since \( 3/2 - 1/2 = 1 \in \nZ \), while
\[
\tfrac12 \cdot \tfrac12 = \tfrac14 , \qquad \tfrac32 \cdot \tfrac12 = \tfrac34 , \qquad \tfrac34 - \tfrac14 = \tfrac12 \notin \nZ .
\]
One class, two products in different classes. The missing clause is (I3): \( \nZ \) is not an ideal of \( \nQ \).
:::

## The ideals of the integers

In \( \nZ \) every ideal is as simple as possible: the multiples of one number. The proof is the move that gave the gcd in Section 3.2.

::: {#thm-integer-ideals-principal}
[Ideals of the Integers]

::: {.enumerate options="label=(\alph*)"}
1. For all \( a, b \in \nZ \), \( a\nZ + b\nZ \) is an ideal of \( \nZ \). In particular \( n\nZ \) is an ideal of \( \nZ \) for every \( n \in \nZ \).
2. Every ideal \( I \) of \( \nZ \) equals \( n\nZ \) for **exactly one** \( n \in \nN \): \( n = 0 \) if \( I = \{0\} \), and otherwise \( n \) is the least positive element of \( I \).
:::
:::

::: {.idea}
For (b), take the least positive element \( n \) of \( I \). Its multiples lie in \( I \) by absorption. Conversely, divide any \( a \in I \) by \( n \): the remainder \( a - qn \) lies in \( I \) and is smaller than \( n \), so it is not positive, and it is \( 0 \). This is **least positive element, then divide** once more.
:::

::: {.proof}
*(a)* \( 0 = a \cdot 0 + b \cdot 0 \in a\nZ + b\nZ \) (@prp-ring-algebra (b)), and @def-integer-linear-combinations shows that \( a\nZ + b\nZ \) is closed under sums and under multiplication by any integer. These are (I1)–(I3). Since \( n\nZ = n\nZ + 0\nZ \) (@def-integer-linear-combinations), \( n\nZ \) is an ideal.

*(b)* *Existence.* If \( I = \{0\} \), then \( I = 0\nZ \), since \( k \cdot 0 = 0 \) for every \( k \) (@prp-ring-algebra (b)). Otherwise \( I \) has an element \( a \ne 0 \), and \( -a \in I \) as well; one of \( a \), \( -a \) is positive (@prp-divisibility-rules-integers (h)). So \( I \cap \nZ_{>0} \) is non-empty, with lower bound \( 0 \), and has a least element \( n \) (@prp-integer-least-element). By (I3), \( kn \in I \) for every \( k \in \nZ \), so \( n\nZ \subseteq I \). Conversely, let \( a \in I \). By @thm-integers-division-remainder (a), \( a = qn + r \) with \( q, r \in \nZ \) and \( 0 \le r < n \). Then \( r = a + (-q)n \in I \), by (I3) and (I2). If \( r > 0 \), then \( r \) is a positive element of \( I \) smaller than \( n \), against the choice of \( n \). So \( r = 0 \), and \( a = qn \in n\nZ \). Hence \( I = n\nZ \).

*Uniqueness.* Let \( n\nZ = m\nZ \) with \( n, m \in \nN \). Then \( n = 1 \cdot n \in m\nZ \), so \( m \mid n \); likewise \( n \mid m \). By @prp-divisibility-rules-integers (f), \( n = m \).
:::

::: {.remark}
For \( I = a\nZ + b\nZ \) with \( (a, b) \ne (0, 0) \), (b) says \( a\nZ + b\nZ = n\nZ \) where \( n \) is the least positive combination. That is @thm-integers-bezout (a), (d), (e), with \( n = \gcd(a, b) \): the theorem of Section 3.2 was this one in disguise.
:::

## The ring of integers modulo n

Now the clock of *Sets, Relations, and Cardinality*, Section 2.5 can be rebuilt on the constructed \( \nZ \), as an instance of the general theorem.

::: {#def-integers-mod-n-ring}
[The Integers Modulo n]

Let \( n \in \nZ_{>0} \). The ring \( \nZ/n\nZ \) is the quotient ring of \( \nZ \) by the ideal \( n\nZ \) (@thm-quotient-ring-by-ideal, @thm-integer-ideals-principal (a)).
:::

Its relation is congruence modulo \( n \) of @fd2:def-congruence, read on the constructed \( \nZ \): \( a - b \in n\nZ \) means \( a - b = kn \) for some \( k \in \nZ \), that is, \( n \mid a - b \), that is, \( a \equiv b \pmod{n} \). Its elements are the classes \( [a] = a + n\nZ \), written \( [a]_n \) when two moduli are in play. Its operations, \( [a] + [b] = [a + b] \) and \( [a][b] = [ab] \), are those of @fd2:prp-congruence-arithmetic; there they were checked by hand for the school integers, and here they are a consequence of @thm-quotient-ring-by-ideal (b). The set \( \nZ/n \) of *Sets, Relations, and Cardinality* is the same construction on the school \( \nZ \); from now on we write \( \nZ/n\nZ \), to recall the ideal.

::: {#thm-integers-mod-n-ring}
[The Ring of Integers Modulo n]

Let \( n \in \nZ_{>0} \).

::: {.enumerate options="label=(\alph*)"}
1. \( \nZ/n\nZ \) is a commutative ring with zero \( [0] \) and one \( [1] \).
2. For each \( a \in \nZ \) there is **exactly one** \( r \in \{0, \dots, n - 1\} \) with \( [a] = [r] \), namely the remainder of \( a \) on division by \( n \). The map \( \{0, \dots, n - 1\} \to \nZ/n\nZ \), \( r \mapsto [r] \), is a bijection, so \( \nZ/n\nZ \) is finite with \( n \) elements (@fd2:def-finite).
3. \( [1] \ne [0] \) if and only if \( n \ge 2 \).
4. \( k \cdot [1] = [k] \) for every \( k \in \nN \), where \( k \cdot x \) is the \( k \)-th multiple in the commutative ring \( \nZ/n\nZ \); in particular \( n \cdot [1] = [0] \).
5. If \( n \ge 2 \), no relation \( < \) makes \( \nZ/n\nZ \) an ordered commutative ring.
:::
:::

The multiples in (d) are those of Section 2.3, defined there by recursion for every commutative ring \( R \) (\( 0 \cdot x \coloneqq 0 \), \( (k + 1) \cdot x \coloneqq k \cdot x + x \)), before @prp-ordered-ring-rules; the recursion uses no order, so it applies to \( \nZ/n\nZ \), which for \( n \ge 2 \) carries no order compatible with its arithmetic, by (e).

::: {.idea}
Most of the work is done: (a) is the general theorem, and (b) is division with remainder read on classes, the remainder naming the class and its uniqueness making the naming one-to-one. Then (c) asks when \( 1 \) is a multiple of \( n \), (d) is an induction along the recursion that defines multiples, and (e) puts (c) and (d) against the rule that \( n \cdot 1 > 0 \) in an ordered ring.
:::

::: {.proof}
*(a)* @thm-quotient-ring-by-ideal (c), since \( n\nZ \) is an ideal (@thm-integer-ideals-principal (a)).

*(b)* *Existence.* By @thm-integers-division-remainder (a), \( a = qn + r \) with \( 0 \le r < n \). Then \( a - r = qn \in n\nZ \), so \( [a] = [r] \). Also \( r \in \nN \) by @thm-integers-ordered-ring (b), and \( r + 1 \le n \) by discreteness (@thm-integers-ordered-ring (c)), so \( r \le n - 1 \) by (O3); that is, \( r \in \{0, \dots, n - 1\} \).

*Uniqueness.* Let \( r, s \in \{0, \dots, n - 1\} \) with \( [r] = [s] \). Then \( r - s = kn \) for some \( k \in \nZ \), so \( r = kn + s \) and \( r = 0 \cdot n + r \) are two divisions of \( r \) by \( n \), with remainders \( s \) and \( r \), each at least \( 0 \) and less than \( n \). By the uniqueness in @thm-integers-division-remainder (a), \( s = r \).

So the map \( \varphi \colon \{0, \dots, n - 1\} \to \nZ/n\nZ \), \( r \mapsto [r] \), is surjective (existence: every class is some \( [a] \), @fd2:def-quotient-set) and injective (uniqueness), hence a bijection (@fd2:def-bijective). Since \( n \ge 1 \), adding \( -1 \) gives \( n - 1 \ge 0 \) (O3), so \( n - 1 \in \nN \) by @thm-integers-ordered-ring (b), and the third example after @fd2:def-finite, with \( n - 1 \) in place of its \( n \), gives the bijection \( \psi \colon \{1, \dots, n\} \to \{0, \dots, n - 1\} \), \( k \mapsto k - 1 \). The composite \( \varphi \circ \psi \colon \{1, \dots, n\} \to \nZ/n\nZ \) is a bijection (@fd2:thm-composition-injective-surjective (c)), so \( \nZ/n\nZ \) has \( n \) elements.

*(c)* By @thm-quotient-ring-by-ideal (d), \( [1] = [0] \) if and only if \( 1 \in n\nZ \), that is, \( n \mid 1 \). By @prp-divisibility-rules-integers (g) and \( n > 0 \), this happens exactly when \( n = 1 \). As \( n \ge 1 \) by discreteness, \( n \ne 1 \) means \( n \ge 2 \).

*(d)* By @fd1:ax-induction (through @cor-omega-identification (b)) on \( k \). Base: \( 0 \cdot [1] = [0] \), by the recursion. Step: if \( k \cdot [1] = [k] \), then
\[
(k + 1) \cdot [1] = k \cdot [1] + [1] = [k] + [1] = [k + 1] ,
\]
by the recursion, the hypothesis, and the definition of \( + \) in @thm-quotient-ring-by-ideal (b) (the sum \( k + 1 \) is the same in \( \nN \) and in \( \nZ \), @prp-naturals-embed-integers (a)). Finally \( [n] = [0] \), since \( n - 0 = 1 \cdot n \in n\nZ \).

*(e)* Let \( n \ge 2 \), and suppose \( < \) made \( \nZ/n\nZ \) an ordered commutative ring. By (c), \( [1] \ne [0] \), so @prp-ordered-ring-rules (h), applied with \( n \ge 1 \), gives \( n \cdot [1] > [0] \). By (d), \( n \cdot [1] = [0] \), and \( [0] > [0] \) contradicts (O1). This proves the theorem.
:::

Part (e) is the general clause after @exm-finite-ring-not-orderable, now applied to a ring that this volume has built: \( \nZ/2\nZ \) has the tables of that example, with \( [0] \), \( [1] \) for \( 0 \), \( 1 \). Part (b) says that the elements of \( \nZ/n\nZ \) can be listed as \( [0], [1], \dots, [n - 1] \), and that to compute with classes we may always reduce to remainders.

::: {#exm-integers-mod-six}
[Multiplication modulo six and modulo five]

Write out the multiplication table of \( \nZ/6\nZ \). Find the pairs of non-zero classes whose product is \( [0] \), and the classes \( [a] \) for which some \( [b] \) has \( [a][b] = [1] \). Then do the same for \( \nZ/5\nZ \).
:::

::: {.solution}
By @thm-integers-mod-n-ring (b), the classes of \( \nZ/6\nZ \) are \( [0], \dots, [5] \), and \( [a][b] = [ab] = [r] \), where \( r \) is the remainder of \( ab \) on division by \( 6 \). For instance \( [4][5] = [20] = [2] \), since \( 20 = 3 \cdot 6 + 2 \). Writing \( r \) for \( [r] \), the table is
\[
\begin{array}{c|cccccc}
\cdot & 0 & 1 & 2 & 3 & 4 & 5 \\ \hline
0 & 0 & 0 & 0 & 0 & 0 & 0 \\
1 & 0 & 1 & 2 & 3 & 4 & 5 \\
2 & 0 & 2 & 4 & 0 & 2 & 4 \\
3 & 0 & 3 & 0 & 3 & 0 & 3 \\
4 & 0 & 4 & 2 & 0 & 4 & 2 \\
5 & 0 & 5 & 4 & 3 & 2 & 1
\end{array}
\]
The non-zero classes with product \( [0] \) are \( [2][3] = [6] = [0] \) and \( [3][4] = [12] = [0] \), with their mirror images \( [3][2] \), \( [4][3] \). So \( \nZ/6\nZ \) has zero divisors, unlike \( \nZ \) (@prp-ordered-ring-rules (f)). Also \( [4][4] = [16] = [4] \): a class can equal its own square without being \( [0] \) or \( [1] \). The entry \( 1 \) occurs only in the rows of \( [1] \) and \( [5] \): \( [1][1] = [1] \) and \( [5][5] = [25] = [1] \). So exactly \( [1] \) and \( [5] \) have a partner with product \( [1] \).

For \( \nZ/5\nZ \) the same method gives
\[
\begin{array}{c|ccccc}
\cdot & 0 & 1 & 2 & 3 & 4 \\ \hline
0 & 0 & 0 & 0 & 0 & 0 \\
1 & 0 & 1 & 2 & 3 & 4 \\
2 & 0 & 2 & 4 & 1 & 3 \\
3 & 0 & 3 & 1 & 4 & 2 \\
4 & 0 & 4 & 3 & 2 & 1
\end{array}
\]
No product of non-zero classes is \( [0] \), and every non-zero class has a partner with product \( [1] \): \( [1][1] = [1] \), \( [2][3] = [6] = [1] \), \( [4][4] = [16] = [1] \). Moreover \( 5 \cdot [1] = [0] \) by @thm-integers-mod-n-ring (d), so \( \nZ/5\nZ \) cannot be ordered, by (e).
:::

The classes with a partner of product \( [1] \) are the **units** of Section 3.5, which finds them for every \( n \) and shows that for a prime \( n \), as for \( 5 \), every non-zero class is one. Chapter 6 uses the ring \( \nZ/5\nZ \), with \( 5 \cdot [1] = [0] \), as a field that no order can fit.

::: {.check}
In \( \nZ/12\nZ \), compute \( [7] + [8] \) and \( [7][8] \), each as \( [r] \) with \( 0 \le r \le 11 \). How many elements has \( \nZ/1\nZ \)?
:::

::: {.solution}
\( [7] + [8] = [15] = [3] \), since \( 15 = 1 \cdot 12 + 3 \); and \( [7][8] = [56] = [8] \), since \( 56 = 4 \cdot 12 + 8 \). The ring \( \nZ/1\nZ \) has one element, by @thm-integers-mod-n-ring (b): every integer is congruent to \( 0 \) modulo \( 1 \), so \( [0] = [1] \), and it is a zero ring, like the ring \( \{0\} \) of Section 2.3.
:::

::: {.warning}
**A class is not its remainder.** \( [3] \) in \( \nZ/12\nZ \) is the set \( 3 + 12\nZ = \{ \dots, -9, 3, 15, \dots \} \), not the integer \( 3 \), and the same symbol \( [3] \) in \( \nZ/5\nZ \) is a different set. A comparison such as "\( [3] < [8] \)" cannot be read off the remainders and respect the arithmetic: by @thm-integers-mod-n-ring (e) no order makes \( \nZ/12\nZ \) an ordered ring. Reducing to remainders is a way of **naming** classes, not a way of turning them back into integers.
:::

## Exercises

### A. Check your understanding

::: {#exr-quotient-rings-a1}
[A1]

These questions are about the proof of @thm-quotient-ring-by-ideal.

::: {.enumerate options="label=(\alph*)"}
1. Where is the clause "\( ra \in I \) for every \( r \in R \)" used?
2. Run the product check of (b) with \( R = \nZ \), \( I = 6\nZ \), \( a = 2 \), \( a' = 8 \) and \( b = 5 \): verify \( a \sim_I a' \), compute \( ab - a'b \), and say why it lies in \( I \).
3. For \( \nZ \subseteq \nQ \), which step of the proof fails, and which clause of @def-ideal-commutative-ring is missing?
4. Give the idea of the proof in two sentences.
:::
:::

::: {.solution}
(a) In (b), for the product in the first argument: \( ab - a'b = (a - a')b \in I \), with \( a - a' \in I \) and \( r = b \). (It also gives closure under negatives, which (a) and (b) use through \( -x = (-1)x \); and it is used in (d), to get \( I = R \) from \( 1 \in I \).)

(b) \( a - a' = 2 - 8 = -6 = (-1) \cdot 6 \in 6\nZ \), so \( 2 \sim_I 8 \). Then \( ab - a'b = 10 - 40 = -30 \), which is \( (a - a')b = (-6) \cdot 5 \), and \( -30 = (-5) \cdot 6 \in 6\nZ \). It lies in \( I \) because \( I \) absorbs the factor \( 5 \).

(c) The product step of (b): \( (a - a')b \) need not lie in \( \nZ \), as with \( a = 3/2 \), \( a' = 1/2 \), \( b = 1/2 \), where it is \( 1/2 \). The missing clause is (I3): \( (1/2) \cdot 1 \notin \nZ \).

(d) A change of representative is an element of \( I \); for the sum it passes through unchanged, and for the product it gets multiplied by the other argument, which absorption keeps inside \( I \). The ring laws then hold in \( R/I \) because both sides of each are classes of the two sides of the same law in \( R \).
:::

### B. Practice

::: {#exr-quotient-rings-b1}
[B1: The ring with four elements]

Write the addition and multiplication tables of \( \nZ/4\nZ \). Find its zero divisors (non-zero \( x \) with \( xy = [0] \) for some non-zero \( y \)) and the classes \( [a] \) with \( [a][b] = [1] \) for some \( [b] \).
:::

::: {.solution}
By @thm-integers-mod-n-ring (b) the elements are \( [0], [1], [2], [3] \), and each entry is the class of the remainder of the sum or product on division by \( 4 \). Writing \( r \) for \( [r] \):
\[
\begin{array}{c|cccc}
+ & 0 & 1 & 2 & 3 \\ \hline
0 & 0 & 1 & 2 & 3 \\
1 & 1 & 2 & 3 & 0 \\
2 & 2 & 3 & 0 & 1 \\
3 & 3 & 0 & 1 & 2
\end{array}
\qquad\qquad
\begin{array}{c|cccc}
\cdot & 0 & 1 & 2 & 3 \\ \hline
0 & 0 & 0 & 0 & 0 \\
1 & 0 & 1 & 2 & 3 \\
2 & 0 & 2 & 0 & 2 \\
3 & 0 & 3 & 2 & 1
\end{array}
\]
For instance \( [3] + [3] = [6] = [2] \) and \( [3][3] = [9] = [1] \), since \( 6 = 1 \cdot 4 + 2 \) and \( 9 = 2 \cdot 4 + 1 \). The only zero divisor is \( [2] \): \( [2][2] = [4] = [0] \), and in the rows of \( [1] \) and \( [3] \) the entry \( 0 \) occurs only in the column of \( [0] \). The classes with a partner of product \( [1] \) are \( [1] \) (\( [1][1] = [1] \)) and \( [3] \) (\( [3][3] = [1] \)); the rows of \( [0] \) and \( [2] \) contain no \( 1 \).
:::

::: {#exr-quotient-rings-b2}
[B2: Determine which]

For each subset of \( \nZ \) below, decide whether it is an ideal of \( \nZ \). Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \nN \).
2. \( 2\nZ \cup 3\nZ \).
3. \( 4\nZ + 6\nZ \).
4. \( \{0\} \).
5. \( \{ n \in \nZ : 6 \mid n^2 \} \), where \( n^2 \coloneqq nn \).
:::
:::

::: {.solution}
(a) No. (I3) fails: \( 1 \in \nN \), but \( (-1) \cdot 1 = -1 \notin \nN \), since \( -1 < 0 \) (\( 1 > 0 \) by @prp-ordered-ring-rules (e), as \( 1 \ne 0 \) in \( \nZ \) by @thm-integers-commutative-ring, then (a)) while \( \nN = \{ x \in \nZ : x \ge 0 \} \) (@thm-integers-ordered-ring (b)).

(b) No. (I2) fails: \( 2 \in 2\nZ \) and \( 3 \in 3\nZ \), but \( 5 \) is in neither, since \( 5 = 2 \cdot 2 + 1 \) and \( 5 = 1 \cdot 3 + 2 \) leave non-zero remainders (uniqueness in @thm-integers-division-remainder (a)).

(c) Yes, by @thm-integer-ideals-principal (a). In fact \( 4\nZ + 6\nZ = 2\nZ \): every \( 4x + 6y = 2(2x + 3y) \) is even, and every \( 2k = 4(-k) + 6k \) is a combination.

(d) Yes: the ideal \( 0\nZ \), or directly as in the examples after @def-ideal-commutative-ring.

(e) Yes: the set is \( 6\nZ \). If \( n = 6k \), then \( n^2 = 6(6k^2) \). Conversely, let \( 6 \mid n^2 \), say \( n^2 = 6m \). Then \( n \cdot n = 2(3m) = 3(2m) \), so \( 2 \mid nn \) and \( 3 \mid nn \). Since \( 2 \) and \( 3 \) are prime (the small-primes remark of Section 3.1), @cor-prime-divides-product (b) gives \( 2 \mid n \) and \( 3 \mid n \). As \( 1 = (-1) \cdot 2 + 1 \cdot 3 \), \( \gcd(2, 3) = 1 \) (@cor-coprime-iff-combination), so \( 6 = 2 \cdot 3 \mid n \) by @prp-coprime-divisors-product. Hence the set equals \( 6\nZ \), an ideal by @thm-integer-ideals-principal (a).
:::

### C. Going deeper

::: {#exr-quotient-rings-c1}
[C1: Changing the modulus]

Let \( m, n \in \nZ_{>0} \). Prove that there is a function \( F \colon \nZ/n\nZ \to \nZ/m\nZ \) with \( F([a]_n) = [a]_m \) for every \( a \in \nZ \) if and only if \( m \mid n \). Show that, when it exists, \( F \) preserves sums, products and the one.
:::

::: {.solution}
\( (\Leftarrow) \) Let \( n = lm \). Then \( n\nZ \subseteq m\nZ \), since \( kn = (kl)m \). We apply @thm-well-defined-on-classes (a) with \( X = Y = \nZ \), congruence modulo \( n \) on \( X \), congruence modulo \( m \) on \( Y \), and \( f(a) \coloneqq a \): if \( a - a' \in n\nZ \), then \( a - a' \in m\nZ \). So \( F \) exists (and is unique).

\( (\Rightarrow) \) Suppose \( F \) exists. Since \( n - 0 = 1 \cdot n \), \( [n]_n = [0]_n \), so
\[
[n]_m = F([n]_n) = F([0]_n) = [0]_m ,
\]
so \( n \in m\nZ \) by @thm-quotient-ring-by-ideal (d), that is, \( m \mid n \).

*Operations.* \( F([a]_n + [b]_n) = F([a + b]_n) = [a + b]_m = [a]_m + [b]_m \), by the definition of \( + \) in @thm-quotient-ring-by-ideal (b) on both sides; likewise for products, and \( F([1]_n) = [1]_m \).

This is the general form of @fd2:exm-ill-defined-class-map: \( [a]_6 \mapsto [a]_4 \) fails because \( 4 \nmid 6 \), and \( [a]_6 \mapsto [a]_3 \) works because \( 3 \mid 6 \).

**Marking scheme.** (10 points)
- 3: \( (\Leftarrow) \) writes \( n = lm \), shows \( n\nZ \subseteq m\nZ \), and invokes @thm-well-defined-on-classes (a) with \( f(a) = a \).
- 3: \( (\Rightarrow) \) uses \( [n]_n = [0]_n \) and applies \( F \) to get \( [n]_m = [0]_m \), hence \( m \mid n \).
- 3: computes \( F \) of a sum and of a product on representatives, citing the definition of the operations on both quotient rings.
- 1: \( F([1]_n) = [1]_m \).
Fatal errors (0 for the step): defining \( F \) by a formula on representatives without checking that it does not depend on the representative; in \( (\Rightarrow) \), assuming \( n\nZ \subseteq m\nZ \) (circular).
:::

::: {#exr-quotient-rings-c2}
[C2: Closed under subtraction]

Let \( S \subseteq \nZ \) be **non-empty**, with \( a - b \in S \) for all \( a, b \in S \). Prove that \( S = n\nZ \) for some \( n \in \nN \).

The first half of a proof is given.

> Pick \( a \in S \); then \( 0 = a - a \in S \). If \( S = \{0\} \), then \( S = 0\nZ \). Otherwise \( S \) contains some \( a \ne 0 \), and \( -a = 0 - a \in S \); one of \( a \), \( -a \) is positive (@prp-divisibility-rules-integers (h)). By @prp-integer-least-element, \( S \) has a least positive element \( n \).

The second half is blank. *Name the move, then complete it.*
:::

::: {.solution}
The move is **least positive element, then divide**.

*\( n\nZ \subseteq S \).* First, \( kn \in S \) for every \( k \in \nN \), by @fd1:ax-induction on \( k \). Base: \( 0 \cdot n = 0 \in S \). Step: \( -n = 0 - n \in S \), and if \( kn \in S \), then \( (k + 1)n = kn + n = kn - (-n) \in S \), using (F9), (F7) and \( -(-n) = n \) (@prp-ring-algebra (a)). Next, every \( k \in \nZ \) is \( j \) or \( -j \) for some \( j \in \nN \) (@prp-naturals-embed-integers (c)), and \( (-j)n = -(jn) = 0 - jn \in S \) (@prp-ring-algebra (c)).

*\( S \subseteq n\nZ \).* Let \( a \in S \). By @thm-integers-division-remainder (a), \( a = qn + r \) with \( 0 \le r < n \). Since \( qn \in S \), \( r = a - qn \in S \). If \( r > 0 \), it is a positive element of \( S \) smaller than \( n \), against the choice of \( n \). So \( r = 0 \) and \( a = qn \).

Hence \( S = n\nZ \). No multiplication hypothesis was needed: closure under subtraction alone forces the multiples of \( n \), and so \( S \) is automatically an ideal. The sets \( S \) of this exercise are the subgroups of \( (\nZ, +) \), which *Algebraic Preliminaries*, Chapter 3 studies.
:::

<!-- dependency ledger
def-ideal-commutative-ring (claim): (opening) Chapter 5 builds R from classes of rational Cauchy sequences up to a null difference, checking its operations directly; Algebraic Preliminaries Ch 5 redoes division, gcd and unique factorization for polynomials | F3.10 (prose pointer; blueprint ch05.md def-reals-cauchy-classes), F4.5 (prose pointer; math-atlas spec/06-migration.md F4.5 plan); nothing here depends on them
def-ideal-commutative-ring (claim): (motivation) b - a = -(a - b), a - c = (a - b) + (b - c), ab - a'b = (a - a')b | ring axioms; proved again in thm-quotient-ring-by-ideal
def-ideal-commutative-ring (claim): -x = (-1)x | prp-ring-algebra (c) (cited) with (F7), (F6)
def-ideal-commutative-ring (example): nZ is an ideal; aZ + bZ is an ideal | def-integer-linear-combinations (cited); (F9), (F5)
def-ideal-commutative-ring (example): Z not an ideal of Q: 1/2 not in Z | cor-integers-even-odd (a) (cited); identification of Section 2.4 (2m = 1 in Q gives 2m = 1 in Z, j injective and preserves products, prp-integers-embed-rationals), used silently
thm-quotient-ring-by-ideal (proof): rearrangements (a + b) - (a' + b) = a - a', a = (a - b) + ... | (F1)-(F4), named in the proof
thm-quotient-ring-by-ideal (proof): -0 = 0 | 0 + 0 = 0 by (F3), uniqueness prp-ring-algebra (a), named in the proof
thm-quotient-ring-by-ideal (claim): (answer to prompt) (I3) with arbitrary r is used once in (a), (b), in the product step; elsewhere (I3) only with r = -1 (closure under negatives), otherwise (I1), (I2) | meta-claim about the proof on the page: (a) uses (I1), (I2), negatives; (b) sum uses nothing, product uses (I3), negative uses closure under negatives; (d) uses (I3) to get I = R, outside (a), (b)
thm-quotient-ring-by-ideal (claim): (warning) Z in Q closed under +, -, contains 0; 1/2 * 1/2 = 1/4, 3/2 * 1/2 = 3/4, 3/4 - 1/4 = 1/2 not in Z | field arithmetic in Q (thm-rationals-field); 1/2 not in Z as in the non-example; verify/ch03/thm-quotient-ring-by-ideal.py
thm-integer-ideals-principal (proof): r = a + (-q)n | (F1)-(F4), prp-ring-algebra (c), used silently
def-integers-mod-n-ring (claim): a - b in nZ iff n | a - b iff a = b mod n | fd2:def-divides, fd2:def-congruence read on the constructed Z (definitions only; blueprint ledger line "definitions on the constructed Z")
thm-integers-mod-n-ring (proof): r <= n - 1 from r + 1 <= n; n - 1 in N for n >= 1 | (O3); thm-integers-ordered-ring (b) (cited)
thm-integers-mod-n-ring (proof): phi o psi is a bijection | fd2:thm-composition-injective-surjective (c) (cited)
thm-integers-mod-n-ring (proof): {0, ..., n - 1} has n elements by the third example after fd2:def-finite with n - 1 in place of n, read on omega | fd2:def-finite and its examples, group (i) of the F3.1 citing rule (cor-omega-identification); cited by position as the blueprint allows
thm-integers-mod-n-ring (proof): multiples k . x defined for every commutative ring by recursion (Section 2.3, "Multiples") | F3.2 §03 paragraph before prp-ordered-ring-rules (cited by section, no label); prp-ordered-ring-rules (h) (cited) for n . 1 > 0
thm-integers-mod-n-ring (claim): Z/2Z has the tables of exm-finite-ring-not-orderable | thm-integers-mod-n-ring (b) and the definitions; computed: 1 + 1 = 2 = 0 mod 2; verify/ch03/exm-integers-mod-six.py
exm-integers-mod-six (solution): tables of Z/6Z and Z/5Z; 20 = 3*6 + 2; zero divisors; classes with partner of product [1] | numerals; verify/ch03/exm-integers-mod-six.py
exm-integers-mod-six (claim): units of Section 3.5; Chapter 6 uses Z/5Z | blueprint ch03.md 05-units-and-crt (within the chapter) and ch06.md R2 (F3.4, prose pointer); nothing here depends on them
thm-integers-mod-n-ring (claim): (check) [7] + [8] = [3], [7][8] = [8] in Z/12Z; Z/1Z has one element | numerals; verify/ch03/thm-integers-mod-n-ring.py
thm-integers-mod-n-ring (claim): (warning) the class 3 + 12Z | thm-quotient-ring-by-ideal (a) (cited by section)
exr-quotient-rings-a1 (solution): 2 - 8 = -6, 10 - 40 = -30 = (-5) * 6 | numerals; verify/ch03/exr-quotient-rings-a1.py
def-ideal-commutative-ring (example): (non-example N) -1 < 0 | prp-ordered-ring-rules (a), (e) (cited), with 1 != 0 from thm-integers-commutative-ring (cited); -0 = 0 used silently
exr-quotient-rings-b2 (solution): (a) -1 < 0 | as for the non-example N after def-ideal-commutative-ring, cited the same way
exr-quotient-rings-c1 (solution): [n]_m = [0]_m gives n in mZ | thm-quotient-ring-by-ideal (d) (cited), n - 0 = n as in its proof
exr-quotient-rings-b1 (solution): tables of Z/4Z | numerals; verify/ch03/exr-quotient-rings-b1.py
exr-quotient-rings-b2 (solution): 5 = 2*2 + 1 = 1*3 + 2; 4x + 6y = 2(2x + 3y); 2k = 4(-k) + 6k; 1 = (-1)*2 + 1*3; n^2 = 6m gives 2 | nn and 3 | nn | numerals and ring algebra; verify/ch03/exr-quotient-rings-b2.py
exr-quotient-rings-c2 (solution): induction on k in N | fd1:ax-induction, read on omega through cor-omega-identification (b) as elsewhere in the chapter
exr-quotient-rings-c2 (claim): subgroups of (Z, +) studied in Algebraic Preliminaries Ch 3 | F4.3 (prose pointer); nothing depends on it
-->
