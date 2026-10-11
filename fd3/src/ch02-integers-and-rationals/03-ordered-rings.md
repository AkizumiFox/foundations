# The Integers as an Ordered Ring

Sections 10.1 and 10.2 built \( \nZ \) as a set of classes with well-defined operations \( + \), \( \cdot \) and \( - \), but we do not yet know which laws they obey. This section collects the laws of school algebra into one definition, a **commutative ring**, and checks them for \( \nZ \) by reducing each to a law of \( \nN \). Then it orders \( \nZ \) and derives the rules for inequalities from axioms alone: from here on, an inequality about integers is proved, never read off a picture.

## The laws of a ring

Expanding brackets or moving a term across an equation uses a short list of laws: sums and products may be reordered and regrouped, \( 0 \) and \( 1 \) do nothing, every element has a negative, and products distribute over sums. The list holds in \( \nZ \), it will hold in \( \nQ \), and a result proved from the list alone holds wherever the list does. It deserves a name.

*A commutative ring is a set where you may add, subtract and multiply by the usual rules; a field is one where you may also divide by anything non-zero.*

::: {#def-commutative-ring-and-field}
[Commutative Ring, Field]

A **commutative ring** is a set \( R \) with two functions, **addition** \( + \colon R \times R \to R \) and **multiplication** \( \cdot \colon R \times R \to R \) (written \( a \cdot b = ab \)), such that the following hold.

::: {.enumerate options="label=(F\arabic*)"}
1. \( a + b = b + a \) **for all** \( a, b \in R \).
2. \( (a + b) + c = a + (b + c) \) **for all** \( a, b, c \in R \).
3. **There is** an element \( 0 \in R \) with \( a + 0 = a \) **for every** \( a \in R \).
4. **For every** \( a \in R \) there is an element \( -a \in R \) with \( a + (-a) = 0 \).
5. \( (ab)c = a(bc) \) **for all** \( a, b, c \in R \).
6. \( ab = ba \) **for all** \( a, b \in R \).
7. **There is** an element \( 1 \in R \) with \( a \cdot 1 = a \) **for every** \( a \in R \).
8. **For every non-zero** \( a \in R \) there is an element \( a^{-1} \in R \) with \( a a^{-1} = 1 \).
9. \( a(b + c) = ab + ac \) **for all** \( a, b, c \in R \).
:::

A commutative ring must satisfy (F1)–(F7) and (F9). A **field** is a commutative ring in which, **in addition**, \( 1 \ne 0 \) and (F8) holds. We write \( a - b \coloneqq a + (-b) \), and in a field \( a / b \coloneqq a b^{-1} \) for \( b \ne 0 \).
:::

In words: (F1)–(F4) say that addition is commutative and associative, with a neutral element \( 0 \) and negatives; (F5)–(F7) say the first three things about multiplication; (F9) links the two and lets us expand brackets. (F8) asks for inverses of **non-zero** elements only, and only in a field. The notations \( -a \) and \( a^{-1} \) anticipate that these elements are unique, which we prove below. These are the axioms (F1)–(F9) of the linear-algebra companion, Chapter 0, and of the analysis volume's ordered fields, in the same numbering, except that there (F7) includes \( 1 \ne 0 \).

**Examples.**

- \( \nZ \), with the operations of @def-integer-operations: the next theorem.
- **The zero ring** \( R \coloneqq \{0\} \), with \( 0 + 0 \coloneqq 0 \), \( 0 \cdot 0 \coloneqq 0 \) and \( 1 \coloneqq 0 \). Every axiom other than (F8) is an equation in \( R \), and every such equation reads \( 0 = 0 \). So \( R \) is a commutative ring, with \( 1 = 0 \), and not a field. This degenerate ring is why several results below assume \( 1 \ne 0 \).

**A non-example by minimal change.** The set \( \nN \), with its addition and multiplication from Chapter 9, satisfies (F1)–(F3), (F5)–(F7) and (F9), by @thm-omega-arithmetic-laws and @def-omega-arithmetic (a). Only (F4) fails, at \( a = 1 \): \( 1 + x = x + 1 \ne 0 \) for every \( x \in \nN \), by @thm-omega-arithmetic-laws (b) and @cor-omega-successor-cancellation. That one missing clause is why \( \nZ \) had to be built.

**Why these clauses.** No axiom says that \( ab = 0 \) forces \( a = 0 \) or \( b = 0 \): that is true in \( \nZ \) but fails in other commutative rings (the warning below), so it must be proved where it holds. The condition \( 1 \ne 0 \) is kept out of the ring axioms, so that the zero ring is a ring, and put into the field axioms, so that \( \{0\} \), where (F8) holds vacuously, is not a field.

::: {.warning}
A commutative ring may have **zero divisors**: non-zero \( a, b \) with \( ab = 0 \). The integers modulo \( 6 \) of Section 7.5 (built there from the school integers, @prp-congruence-arithmetic) form a commutative ring, and in it \( [2] \ne [0] \) and \( [3] \ne [0] \), yet \( [2][3] = [6] = [0] \). So "\( ab = 0 \), hence \( a = 0 \) or \( b = 0 \)" is not a consequence of (F1)–(F9). In an **ordered** ring it is a theorem, proved later in this section from the order axioms.
:::

## The integers form a commutative ring

To prove a law for classes, write each side through representatives (@def-integer-operations) and compare the two pairs of natural numbers: if they are equal, or related by \( \sim \) (@thm-classes-partition (b)), the classes are equal. We call this move **reduce to the level below**: a statement about classes becomes an identity in \( \nN \), which Chapter 9 has proved.

::: {#thm-integers-commutative-ring}
[The Integers Form a Commutative Ring]

\( \nZ \), with the addition, multiplication and negation of @def-integer-operations, is a commutative ring, with zero \( [(0, 0)] \) and one \( [(1, 0)] \), and in it \( 1 \ne 0 \).
:::

::: {.idea}
The operations are functions by @prp-integer-operations-well-defined, so only the eight laws remain. On representatives each side of a law is the class of an explicit pair, and we compare the pairs in \( \nN \). Only associativity of multiplication is laborious; it is written out below the table.
:::

::: {.proof}
By @prp-integer-operations-well-defined, \( + \) and \( \cdot \) are functions \( \nZ \times \nZ \to \nZ \). Let \( x, y, z \in \nZ \); by @def-quotient-set, \( x = [(a, b)] \), \( y = [(c, d)] \), \( z = [(e, f)] \) with \( a, \dots, f \in \nN \). By @def-integer-operations, each side of each axiom is the class of the pair shown in the table. "Equal" means the same pair of natural numbers, by @thm-omega-arithmetic-laws and @def-omega-arithmetic (a), (b). "Related" means related by \( \sim \) (@def-integers-as-classes: \( (p, q) \sim (r, s) \) means \( p + s = q + r \)), so the classes agree by @thm-classes-partition (b).

| Axiom | left side, as a pair | right side, as a pair | why the classes agree |
|---|---|---|---|
| (F1) \( x + y = y + x \) | \( (a + c, b + d) \) | \( (c + a, d + b) \) | equal: \( + \) is commutative on \( \nN \) |
| (F2) \( (x + y) + z = x + (y + z) \) | \( ((a + c) + e, (b + d) + f) \) | \( (a + (c + e), b + (d + f)) \) | equal: \( + \) is associative on \( \nN \) |
| (F3) \( x + [(0, 0)] = x \) | \( (a + 0, b + 0) \) | \( (a, b) \) | equal: \( m + 0 = m \) |
| (F4) \( x + (-x) = [(0, 0)] \) | \( (a + b, b + a) \) | \( (0, 0) \) | related: \( (a + b) + 0 = (b + a) + 0 \) |
| (F5) \( (xy)z = x(yz) \) | see below | see below | equal, after expanding (below) |
| (F6) \( xy = yx \) | \( (ac + bd, ad + bc) \) | \( (ca + db, cb + da) \) | equal: \( \cdot \) and \( + \) are commutative |
| (F7) \( x \cdot [(1, 0)] = x \) | \( (a \cdot 1 + b \cdot 0, a \cdot 0 + b \cdot 1) \) | \( (a, b) \) | equal: \( n \cdot 1 = n \), \( n \cdot 0 = 0 \), \( n + 0 = 0 + n = n \) |
| (F9) \( x(y + z) = xy + xz \) | \( (a(c + e) + b(d + f), a(d + f) + b(c + e)) \) | \( ((ac + bd) + (ae + bf), (ad + bc) + (af + be)) \) | equal: distribute, then reorder the four terms |

For (F5), write \( xy = [(g, h)] \) with \( g \coloneqq ac + bd \), \( h \coloneqq ad + bc \). Then \( (xy)z = [(ge + hf, gf + he)] \), and in \( \nN \)
\[
\begin{aligned}
ge + hf &= ace + bde + adf + bcf, \\
gf + he &= acf + bdf + ade + bce .
\end{aligned}
\]
On the other side, \( yz = [(ce + df, cf + de)] \), and \( x(yz) \) is the class of the pair whose coordinates are
\[
\begin{aligned}
a(ce + df) + b(cf + de) &= ace + adf + bcf + bde, \\
a(cf + de) + b(ce + df) &= acf + ade + bce + bdf .
\end{aligned}
\]
Both first coordinates are sums of \( ace, adf, bcf, bde \), and both second coordinates of \( acf, ade, bce, bdf \), so the pairs are equal (@thm-omega-arithmetic-laws (b)–(g)).

Finally, \( 1 \ne 0 \): if \( [(1, 0)] = [(0, 0)] \), then \( 1 = 0 \) by @prp-integer-normal-form (b). But \( 0 < 1 \) in \( \nN \) (@thm-omega-order (d)), and \( < \) is irreflexive (@thm-omega-order (a)), so \( 1 \ne 0 \). This proves the theorem.
:::

Seven of the eight rows end in "equal". Only (F4) needs \( \sim \): the pair \( (a + b, b + a) \) records "\( (a + b) - (b + a) \)", which is zero, without performing the subtraction, and that is the whole point of passing to classes.

::: {.remark}
The zero and one of this ring are \( [(0, 0)] = \iota(0) \) and \( [(1, 0)] = \iota(1) \) (@prp-naturals-embed-integers), so after the identification of Section 10.2 they are the natural numbers \( 0 \) and \( 1 \). With \( a - b \coloneqq a + (-b) \), the formula \( [(a, b)] = \iota(a) + (-\iota(b)) \) of @prp-naturals-embed-integers reads \( [(a, b)] = a - b \) for \( a, b \in \nN \): the subtraction the pair recorded is now performed in \( \nZ \).
:::

What the definition does not list must be derived, and the derivations work in every commutative ring at once.

::: {#prp-ring-algebra}
[Algebra in a Commutative Ring]

Let \( R \) be a commutative ring, and let \( a, b \in R \).

::: {.enumerate options="label=(\alph*)"}
1. The elements \( 0 \) and \( 1 \) of (F3) and (F7) are unique, the element \( -a \) of (F4) is unique, and \( -(-a) = a \).
2. \( a \cdot 0 = 0 \).
3. \( (-a)b = -(ab) \) and \( (-a)(-b) = ab \).
4. \( (a + b)^2 = a^2 + 2ab + b^2 \), where \( x^2 \coloneqq xx \) and \( 2 \coloneqq 1 + 1 \).
:::
:::

::: {.idea}
To show that something equals \( 0 \), or \( -(ab) \), show that it satisfies the **defining equation** of that element and let uniqueness, part (a), finish.
:::

::: {.proof}
(a) Suppose \( 0 \) and \( 0' \) both satisfy (F3). Then \( 0' = 0' + 0 = 0 + 0' = 0 \), by (F3) for \( 0 \), (F1), and (F3) for \( 0' \). Likewise, if \( 1 \) and \( 1' \) both satisfy (F7), then \( 1' = 1' \cdot 1 = 1 \cdot 1' = 1 \), by (F7) and (F6). Next, suppose \( a + b = 0 \) and \( a + c = 0 \). Then
\[
\begin{aligned}
b &= b + 0 = b + (a + c) = (b + a) + c \\
  &= (a + b) + c = 0 + c = c + 0 = c ,
\end{aligned}
\]
by (F3), the second hypothesis, (F2), (F1), the first hypothesis, (F1) and (F3). So \( -a \) is the **only** element whose sum with \( a \) is \( 0 \). Finally, \( (-a) + a = a + (-a) = 0 \) by (F1) and (F4), so \( a \) satisfies the defining equation of \( -(-a) \), and uniqueness gives \( -(-a) = a \).

(b) Let \( z \coloneqq a \cdot 0 \). By (F3) and (F9), \( z = a(0 + 0) = a \cdot 0 + a \cdot 0 = z + z \). Adding \( -z \) to both sides,
\[
0 = z + (-z) = (z + z) + (-z) = z + \bigl(z + (-z)\bigr) = z + 0 = z ,
\]
by (F4), the equation \( z = z + z \), (F2), (F4) and (F3). So \( a \cdot 0 = 0 \).

(c) By (F6) and (F9), \( ab + (-a)b = b\bigl(a + (-a)\bigr) = b \cdot 0 = 0 \), the last step by (b). So \( (-a)b \) satisfies the defining equation of \( -(ab) \), and (a) gives \( (-a)b = -(ab) \). By (F6) also \( a(-b) = (-b)a = -(ba) = -(ab) \). Hence \( (-a)(-b) = -\bigl(a(-b)\bigr) = -\bigl(-(ab)\bigr) = ab \), using the first identity, the second, and (a).

(d) By (F9) and (F6), \( (a + b)(a + b) = (a + b)a + (a + b)b = a^2 + ba + ab + b^2 \), and \( ba + ab = ab \cdot 1 + ab \cdot 1 = ab(1 + 1) = 2ab \) by (F6), (F7) and (F9). Regrouping by (F1) and (F2) gives \( (a + b)^2 = a^2 + 2ab + b^2 \).
:::

The argument of (a) with multiplication shows that in a **field** a non-zero \( a \) has only one inverse: if \( ab = 1 \) and \( ac = 1 \), then \( b = b \cdot 1 = b(ac) = (ba)c = (ab)c = 1 \cdot c = c \), by (F7), (F5) and (F6). So \( a^{-1} \), and with it \( a/b \), names a single element. And (b) explains the zero ring: if \( 1 = 0 \) in a commutative ring, then \( a = a \cdot 1 = a \cdot 0 = 0 \) for every \( a \), so the ring is \( \{0\} \).

## Ordered rings

The integers carry an order tied to the operations: adding the same number to both sides keeps an inequality, and a product of positives is positive. We want every rule for inequalities to follow from a short list of axioms, as for equations. The list is the order axioms of the analysis volume, with "field" relaxed to "commutative ring".

*An ordered ring is a ring with a strict order that adding respects, in which a product of positives is positive.*

::: {#def-ordered-ring-and-field}
[Ordered Ring, Ordered Field]

An **ordered commutative ring** is a commutative ring \( R \) (@def-commutative-ring-and-field) together with a relation \( < \) on \( R \) such that, **for all** \( a, b, c \in R \):

::: {.enumerate options="label=(O\arabic*)"}
1. (trichotomy) **exactly one** of \( a < b \), \( a = b \), \( b < a \) holds;
2. (transitivity) if \( a < b \) and \( b < c \), then \( a < c \);
3. (addition) if \( a < b \), then \( a + c < b + c \);
4. (multiplication) if \( 0 < a \) and \( 0 < b \), then \( 0 < ab \).
:::

An **ordered field** is a field that is an ordered commutative ring. We write \( b > a \) for \( a < b \), and \( a \le b \) for "\( a < b \) or \( a = b \)" (likewise \( b \ge a \)). An element \( a \) is **positive** if \( a > 0 \), **negative** if \( a < 0 \), and **non-negative** if \( a \ge 0 \).
:::

In words: any two elements compare in exactly one way, so \( a < a \) never holds; comparisons chain; we may add the same element to both sides; and (O4), the only clause about multiplication, speaks only of **positive** elements.

The degenerate case: the zero ring \( \{0\} \) with the **empty** relation is an ordered commutative ring. Only the middle option of (O1) holds, and (O2)–(O4) are vacuous. There \( 1 = 0 \), so any rule concluding \( 1 > 0 \) must assume \( 1 \ne 0 \).

Checking (O1)–(O4) directly means handling pairs of elements. It is easier to say which elements are positive and let \( a < b \) mean that \( b - a \) is positive. The next proposition says which "positive sets" give an order, and that every order arises so. We call the move **order from a positive set**.

::: {#prp-order-from-positives}
[Order from a Positive Set]

Let \( R \) be a commutative ring and \( P \subseteq R \) a subset such that:

::: {.enumerate options="label=(P\arabic*)"}
1. if \( a, b \in P \), then \( a + b \in P \) and \( ab \in P \);
2. **for every** \( a \in R \), **exactly one** of \( a \in P \), \( a = 0 \), \( -a \in P \) holds.
:::

Define \( a < b \) to mean \( b - a \in P \). Then \( (R, <) \) is an ordered commutative ring (@def-ordered-ring-and-field), and \( P = \{ a \in R : a > 0 \} \).

Conversely, if \( (R, <) \) is an ordered commutative ring, then \( P \coloneqq \{ a \in R : a > 0 \} \) satisfies (P1) and (P2), and for all \( a, b \in R \), \( a < b \) holds if and only if \( b - a \in P \).
:::

The labels (P1), (P2) are local; they are not the clauses of a partition (Section 7.5) or Peano's axioms (Chapter 9).

::: {.idea}
Each order axiom is a statement about one difference. (O1) is (P2) applied to \( b - a \), since \( -(b - a) = a - b \). (O2) is closure under sums, since \( (c - b) + (b - a) = c - a \). (O3) holds since \( (b + c) - (a + c) = b - a \). (O4) is closure under products. The algebra is uniqueness of negatives.
:::

::: {.proof}
We first record three identities in \( R \), for \( a, b, c \in R \):
\[
\begin{gathered}
-(b - a) = a - b , \qquad (c - b) + (b - a) = c - a , \\
(b + c) - (a + c) = b - a .
\end{gathered}
\]
For the first, \( (b - a) + (a - b) = (b + (-b)) + ((-a) + a) = 0 \) by (F1), (F2), (F4), and @prp-ring-algebra (a) gives the identity. The second is regrouping by (F1)–(F4). For the third, \( (a + c) + ((-a) + (-c)) = 0 \) likewise, so \( -(a + c) = (-a) + (-c) \) by @prp-ring-algebra (a), and the \( c \)'s cancel. Also \( -0 = 0 \) (as \( 0 + 0 = 0 \)), so \( a - 0 = a \); and \( b - a = 0 \) if and only if \( b = a \): one direction is (F4), and \( b - a = 0 \) gives \( b = (b - a) + a = 0 + a = a \).

Now let \( P \) satisfy (P1), (P2), and let \( a < b \) mean \( b - a \in P \).

(O1) Apply (P2) to \( b - a \): exactly one of \( b - a \in P \), \( b - a = 0 \), \( -(b - a) \in P \) holds. By the facts above, these say \( a < b \), \( a = b \) and \( a - b \in P \), that is, \( b < a \). So exactly one of the three holds.

(O2) If \( b - a \in P \) and \( c - b \in P \), then \( c - a = (c - b) + (b - a) \in P \) by (P1).

(O3) If \( b - a \in P \), then \( (b + c) - (a + c) = b - a \in P \).

(O4) Since \( a - 0 = a \), we have \( 0 < a \) if and only if \( a \in P \). So \( 0 < a \) and \( 0 < b \) give \( a, b \in P \), hence \( ab \in P \) by (P1), that is, \( 0 < ab \). The same equivalence says \( P = \{ a \in R : a > 0 \} \).

Conversely, let \( (R, <) \) be an ordered commutative ring and \( P \coloneqq \{ a : a > 0 \} \). If \( a < b \), then \( a + (-a) < b + (-a) \) by (O3), that is, \( 0 < b - a \). If \( 0 < b - a \), then \( 0 + a < (b - a) + a = b \) by (O3), that is, \( a < b \). This is the last claim. For (P1), let \( a, b > 0 \). Then \( 0 + b < a + b \) by (O3), so \( 0 < b < a + b \) and \( a + b > 0 \) by (O2); and \( ab > 0 \) by (O4). For (P2), let \( a \in R \). By (O1) exactly one of \( 0 < a \), \( a = 0 \), \( a < 0 \) holds, and by the last claim \( a < 0 \) holds exactly when \( 0 - a = -a \) is in \( P \). This proves the proposition.
:::

So an order on a commutative ring is the same thing as a positive set. For \( \nZ \), the natural one is the classes \( [(a, b)] \) with \( b < a \). Section 10.1 warned that "\( b < a \)" is a statement about **one** representative; we now check that it is a statement about the class.

## The order of the integers

::: {#def-integer-order}
[Order on the Integers]

Let \( S \coloneqq \{ (a, b) \in \nN \times \nN : b < a \} \), and
\[
P_{\nZ} \coloneqq \{ [(a, b)] : (a, b) \in S \} \subseteq \nZ .
\]
For \( x, y \in \nZ \), define \( x < y \) to mean \( y - x \in P_{\nZ} \).
:::

**Well-definedness.** By @thm-well-defined-on-classes (c), with \( X = \nN \times \nN \), it suffices that \( (a, b) \sim (a', b') \) and \( b < a \) imply \( b' < a' \). Write \( a = b + k \) with \( k \ne 0 \) (@prp-omega-order-arithmetic (a)). Then \( a + b' = b + a' \) reads \( b + (k + b') = b + a' \) (@thm-omega-arithmetic-laws), and canceling \( b \) (@prp-omega-order-arithmetic (b)) gives \( a' = b' + k \), so \( b' < a' \). Hence, for **every** pair,
\[
[(a, b)] \in P_{\nZ} \iff b < a .
\]
So "positive" may be tested on any representative, as Section 10.1's warning required.

**Examples.** \( [(5, 2)] \in P_{\nZ} \), since \( 2 < 5 \); this is the integer \( 3 \). \( [(2, 5)] \notin P_{\nZ} \) and \( [(4, 4)] \notin P_{\nZ} \), since neither \( 5 < 2 \) nor \( 4 < 4 \). To compare \( x = [(3, 5)] \) and \( y = [(4, 1)] \): \( y - x = [(4, 1)] + [(5, 3)] = [(9, 4)] \), and \( 4 < 9 \), so \( x < y \), as "\( -2 < 3 \)" leads us to expect. The degenerate pair \( (0, 0) \) is not in \( S \), so \( 0 \notin P_{\nZ} \): zero is not positive.

::: {.check}
Is \( [(7, 10)] < [(2, 4)] \)?
:::

::: {.solution}
Compute \( [(2, 4)] - [(7, 10)] = [(2, 4)] + [(10, 7)] = [(12, 11)] \) by @def-integer-operations. Since \( 11 < 12 \), the difference lies in \( P_{\nZ} \), so yes: \( [(7, 10)] < [(2, 4)] \), which is \( -3 < -2 \).
:::

Recall from Section 10.2 that \( \nZ_{>0} \coloneqq \{ n \in \nN : n \ne 0 \} \), a set of natural numbers, inside \( \nZ \) through the identification \( n = \iota(n) \). The next theorem shows that it is exactly the set of positive integers.

::: {#thm-integers-ordered-ring}
[The Integers Form an Ordered Ring]

\( \nZ \), with the operations of @def-integer-operations and the relation \( < \) of @def-integer-order, is an ordered commutative ring, and its positive elements are exactly \( P_{\nZ} \). Moreover:

::: {.enumerate options="label=(\alph*)"}
1. for \( m, n \in \nN \), \( \iota(m) < \iota(n) \) if and only if \( m < n \);
2. \( \nN = \{ x \in \nZ : x \ge 0 \} \), and \( \nZ_{>0} = \{ x \in \nZ : x > 0 \} \);
3. (**discreteness**) there is no \( k \in \nZ \) with \( 0 < k < 1 \); hence, for \( m, n \in \nZ \) with \( m < n \), \( m + 1 \le n \).
:::
:::

::: {.idea}
By @prp-order-from-positives it is enough to check (P1) and (P2) for \( P_{\nZ} \), each a fact about \( \nN \). For products, write \( a = b + k \), \( c = d + l \): the product's two coordinates differ by exactly \( kl \ne 0 \). (P2) is trichotomy in \( \nN \). Parts (a)–(c) follow from the positive classes being the \( [(k, 0)] \) with \( k \ne 0 \).
:::

::: {.proof}
By @thm-integers-commutative-ring, \( \nZ \) is a commutative ring. We check (P1) and (P2) of @prp-order-from-positives for \( P = P_{\nZ} \), using the criterion \( [(a, b)] \in P_{\nZ} \iff b < a \).

(P1), sums. Let \( x = [(a, b)] \) and \( y = [(c, d)] \) with \( b < a \) and \( d < c \). Then \( x + y = [(a + c, b + d)] \), and
\[
b + d < a + d < a + c
\]
by @prp-omega-order-arithmetic (c) twice (with commutativity), so \( b + d < a + c \) by transitivity (@thm-omega-order (a)). Hence \( x + y \in P_{\nZ} \).

(P1), products. With the same \( x, y \), write \( a = b + k \) and \( c = d + l \) with \( k, l \ne 0 \) (@prp-omega-order-arithmetic (a)). Then \( xy = [(ac + bd, ad + bc)] \), and expanding by @thm-omega-arithmetic-laws,
\[
\begin{aligned}
ac + bd &= (b + k)(d + l) + bd = bd + bl + kd + kl + bd , \\
ad + bc &= (b + k)d + b(d + l) = bd + kd + bd + bl .
\end{aligned}
\]
So \( ac + bd = (ad + bc) + kl \). Since \( k \ne 0 \) and \( l \ne 0 \), \( kl \ne 0 \) by @prp-omega-order-arithmetic (d), and therefore \( ad + bc < ac + bd \) by @prp-omega-order-arithmetic (a). Hence \( xy \in P_{\nZ} \).

(P2). Let \( x = [(a, b)] \). Then \( x \in P_{\nZ} \) if and only if \( b < a \). Next, \( x = [(0, 0)] \) if and only if \( (a, b) \sim (0, 0) \) (@thm-classes-partition (b)), that is, \( a + 0 = b + 0 \), that is, \( a = b \). Finally, \( -x = [(b, a)] \in P_{\nZ} \) if and only if \( a < b \). By trichotomy in \( \nN \) (@thm-omega-order (a)), exactly one of \( b < a \), \( a = b \), \( a < b \) holds. So exactly one of \( x \in P_{\nZ} \), \( x = 0 \), \( -x \in P_{\nZ} \) holds.

By @prp-order-from-positives, \( (\nZ, <) \) is an ordered commutative ring with positive set \( P_{\nZ} \).

(a) By @def-integer-operations, \( \iota(n) - \iota(m) = [(n, 0)] + [(0, m)] = [(n, m)] \), which lies in \( P_{\nZ} \) if and only if \( m < n \).

(b) If \( x = [(a, b)] > 0 \), then \( a = b + k \) with \( k \ne 0 \) (@prp-omega-order-arithmetic (a)), and \( x = [(k, 0)] = \iota(k) \) by @prp-integer-normal-form (a). Conversely, for \( k \ne 0 \), \( \iota(k) = [(k, 0)] \) is positive since \( 0 < k \) (@thm-omega-order (d)). So the positive integers are the \( \iota(k) \) with \( k \in \nZ_{>0} \); adding \( 0 = \iota(0) \) gives the first equation.

(c) If \( 0 < k \), then \( k = \iota(m) \) with \( m \ne 0 \) by (b), so \( 1 \le m \) (@thm-omega-order (d)) and \( 1 \le k \) by (a); then \( k < 1 \) would give \( 1 < 1 \) by (O2), or contradict (O1) directly. Now let \( m < n \). Then \( n - m > 0 \) (@prp-order-from-positives), so \( n - m \ge 1 \), and adding \( m \) by (O3) gives \( n \ge 1 + m \). This proves the theorem.
:::

With the identification of Section 10.2, (a) says that the order of \( \nZ \) **extends** the order of \( \nN \).

**Two non-examples by minimal change**, each breaking exactly one order axiom:

- Replace \( < \) by \( \le \). (O2)–(O4) still hold, by the axioms for \( < \) and the cases of equality (for (O4), \( ab = 0 \) when a factor is \( 0 \), by @prp-ring-algebra (b)). But (O1) fails at \( a = b = 0 \): both "\( 0 \le 0 \)" and "\( 0 = 0 \)" hold. The axioms describe a **strict** order.
- Reverse the order: \( a \prec b \) means \( b < a \). (O1)–(O3) hold, by the same axioms for \( < \). But (O4) fails: \( 0 \prec -1 \), since \( 0 - (-1) = 1 = [(1, 0)] \in P_{\nZ} \) (@prp-ring-algebra (a)), and \( (-1)(-1) = 1 \) (@prp-ring-algebra (c)), yet \( 0 \prec 1 \) is false, since \( 0 - 1 = [(0, 1)] \notin P_{\nZ} \). So (O4) fixes which way round the order goes.

## Rules for inequalities

The rules below hold in every ordered commutative ring: in \( \nZ \) now, and in \( \nQ \) once Section 10.5 orders it. One of them needs multiples first.

**Multiples.** Let \( R \) be a commutative ring and \( a \in R \). By @thm-recursion, read on \( \nN = \omega \) through @cor-omega-identification (b), with \( X = R \), starting value \( 0 \) and step \( (n, y) \mapsto y + a \), there is exactly one function \( \nN \to R \), written \( n \mapsto n \cdot a \), with
\[
0 \cdot a = 0 , \qquad (n + 1) \cdot a = n \cdot a + a \quad \text{for every } n \in \nN .
\]
So \( 1 \cdot a = a \) and \( 2 \cdot a = a + a \). The dot is not the multiplication of \( R \). When \( R = \nZ \), the two readings agree, by @ax-induction (through @cor-omega-identification (b)): \( 0 \cdot a = 0 = 0a \) by @prp-ring-algebra (b), and \( n \cdot a = na \) gives \( (n + 1) \cdot a = na + a = (n + 1)a \) by (F7), (F9).

::: {#prp-ordered-ring-rules}
[Rules for Inequalities in an Ordered Ring]

Let \( R \) be an ordered commutative ring, and let \( a, b, c, d \in R \).

::: {.enumerate options="label=(\alph*)"}
1. \( a < b \) if and only if \( b - a > 0 \), if and only if \( -b < -a \).
2. If \( a \le b \) and \( c \le d \), then \( a + c \le b + d \), and the conclusion is strict if one of the hypotheses is strict.
3. If \( a < b \) and \( c > 0 \), then \( ac < bc \).
4. If \( a < b \) and \( c < 0 \), then \( ac > bc \).
5. If \( a \ne 0 \), then \( a^2 > 0 \). If \( 1 \ne 0 \), then \( 1 > 0 \).
6. If \( ab = 0 \), then \( a = 0 \) or \( b = 0 \).
7. If \( a \ge 0 \) and \( b \ge 0 \), then \( a < b \) if and only if \( a^2 < b^2 \).
8. For every \( m, k \in \nN \), \( (m + k) \cdot a = m \cdot a + k \cdot a \). If \( 1 \ne 0 \), then \( n \cdot 1 > 0 \) for every \( n \in \nN \) with \( n \ge 1 \), and \( m \cdot 1 < n \cdot 1 \) whenever \( m, n \in \nN \) and \( m < n \).
9. \( \le \) is a total order on \( R \) (@def-partial-order), and its strict part is \( < \).
:::
:::

::: {.idea}
The method is **turn the comparison into one positive element**: by @prp-order-from-positives, \( a < b \) says that \( b - a \) is positive, and positive elements are closed under \( + \) and \( \cdot \). For instance (c) says: if \( b - a \) and \( c \) are positive, so is \( bc - ac = (b - a)c \). We prove (i) first, since (b) and (g) use it.
:::

::: {.proof}
(i) Reflexivity is \( a = a \). Antisymmetry: \( a \le b \), \( b \le a \) and \( a \ne b \) give \( a < b < a \), so \( a < a \) by (O2), against (O1). Transitivity: if \( a \le b \le c \), either an equality holds and we substitute, or \( a < c \) by (O2); and \( a < c \) whenever one step is strict. Totality is (O1). Strict part: \( a < b \) implies \( a \ne b \) by (O1), and \( a \le b \), \( a \ne b \) give \( a < b \).

(a) The first equivalence is the last claim of @prp-order-from-positives. For the second, \( (-a) - (-b) = (-a) + b = b - a \) by @prp-ring-algebra (a) and (F1), so \( -b < -a \) also says \( b - a > 0 \).

(b) By (O3) (or equality) and (F1), \( a + c \le b + c \le b + d \); conclude by (i).

(c) By (a), \( b - a > 0 \). By (O4), \( (b - a)c > 0 \). By (F9), (F6) and @prp-ring-algebra (c), \( (b - a)c = bc + (-a)c = bc - ac \). So \( bc - ac > 0 \), and \( ac < bc \) by (a).

(d) By (a), \( c < 0 \) gives \( 0 - c = -c > 0 \). By (c) applied with \( -c \), \( a(-c) < b(-c) \), that is, \( -(ac) < -(bc) \) by @prp-ring-algebra (c), and then \( bc < ac \) by (a) together with \( -(-x) = x \).

(e) If \( a > 0 \), then \( a^2 = aa > 0 \) by (O4). If \( a < 0 \), then \( -a > 0 \) as in (d), and \( a^2 = (-a)(-a) > 0 \) by @prp-ring-algebra (c) and (O4). By (O1) one of the two cases occurs when \( a \ne 0 \). If \( 1 \ne 0 \), then \( 1 = 1 \cdot 1 = 1^2 > 0 \).

(f) Contrapositive: let \( a, b \ne 0 \). By (O1) and (a), some \( a' \in \{ a, -a \} \) and \( b' \in \{ b, -b \} \) are positive, so \( a'b' > 0 \) by (O4). By @prp-ring-algebra (c), \( a'b' \) is \( ab \) or \( -(ab) \); if \( ab = 0 \), both are \( 0 \), against (O1). So \( ab \ne 0 \).

(g) Let \( a, b \ge 0 \). (\( \Rightarrow \)) If \( a < b \), then \( b > 0 \) by (i), and (c) gives \( ab < b^2 \). Also \( a^2 \le ab \): by (c) if \( a > 0 \), and by @prp-ring-algebra (b) if \( a = 0 \). So \( a^2 < b^2 \) by (i). (\( \Leftarrow \)) If \( a^2 < b^2 \) but not \( a < b \), then \( b = a \) or \( b < a \) by (O1), giving \( a^2 = b^2 \) or, by (\( \Rightarrow \)), \( b^2 < a^2 \); both contradict (O1).

(h) Fix \( m \in \nN \). We prove the sum law by @ax-induction on \( k \) (through @cor-omega-identification (b)), for \( P(k) \): "\( (m + k) \cdot a = m \cdot a + k \cdot a \)". *Base case:* \( (m + 0) \cdot a = m \cdot a = m \cdot a + 0 = m \cdot a + 0 \cdot a \), by @def-omega-arithmetic (a), (F3) and the definition of multiples. *Inductive step:* assume \( P(k) \). Then
\[
\begin{aligned}
(m + (k + 1)) \cdot a &= ((m + k) + 1) \cdot a = (m + k) \cdot a + a \\
&= (m \cdot a + k \cdot a) + a = m \cdot a + (k + 1) \cdot a ,
\end{aligned}
\]
by associativity in \( \nN \) (@thm-omega-arithmetic-laws (c)), the definition of multiples, \( P(k) \), and (F2) with the definition of multiples again.

Now let \( 1 \ne 0 \). By @ax-induction on \( n \), for \( Q(n) \): "\( (n + 1) \cdot 1 > 0 \)": the base is \( 1 \cdot 1 = 0 + 1 = 1 > 0 \) by (e), and the step is \( (n + 2) \cdot 1 = (n + 1) \cdot 1 + 1 > 0 \) by (b) and (e). Every \( n \ge 1 \) in \( \nN \) is \( j + 1 \) for some \( j \) (@prp-omega-order-arithmetic (a)), so \( n \cdot 1 > 0 \). Finally, if \( m < n \), then \( n = m + k \) with \( k \ne 0 \) (@prp-omega-order-arithmetic (a)), so \( k \ge 1 \) (@thm-omega-order (d)), and by the sum law and (b),
\[
n \cdot 1 = m \cdot 1 + k \cdot 1 > m \cdot 1 + 0 = m \cdot 1 .
\]
This proves the proposition.
:::

The school rules for inequalities between integers are now theorems about \( \nZ \). The hypothesis \( 1 \ne 0 \) in (e) and (h) cannot be dropped: in the zero ring with the empty order, neither \( 1 > 0 \) nor \( 1 \cdot 1 > 0 \) holds.

::: {.warning}
(O4) and (c) are about multiplying by something **positive**. The tempting rule "if \( a < b \) and \( c < d \), then \( ac < bd \)" is false in \( \nZ \): \( -3 < -1 \) and \( -3 < -1 \), yet \( (-3)(-3) = 9 \) and \( (-1)(-1) = 1 \), and \( 9 > 1 \). What is true is the version with \( 0 \le a \) and \( 0 \le c \), which follows from (c) applied twice.
:::

::: {.check}
Is \( \nZ \) a field?
:::

::: {.solution}
No: \( 2 \coloneqq 1 + 1 \) is non-zero (it is \( > 1 > 0 \)) and has no inverse. Suppose \( 2x = x + x = 1 \). If \( x \le 0 \), then \( x + x \le 0 < 1 \) by @prp-ordered-ring-rules (b), (e). If \( x > 0 \), then \( x \ge 1 \) by discreteness (@thm-integers-ordered-ring (c)), so \( x + x \ge 1 + 1 > 1 \) by @prp-ordered-ring-rules (b), (e). Both contradict \( 2x = 1 \) by (O1).
:::

## Least elements, and a ring that cannot be ordered

The natural numbers are well ordered (@thm-omega-well-ordering); the integers are not, since \( x - 1 < x \) for every \( x \). But a set of integers bounded below can be shifted into \( \nN \).

::: {#prp-integer-least-element}
[Least and Greatest Elements of Sets of Integers]

Let \( S \subseteq \nZ \) be **non-empty**. If \( S \) has a lower bound \( b \in \nZ \) (that is, \( b \le s \) for every \( s \in S \)), then \( S \) has a least element. If \( S \) has an upper bound \( c \in \nZ \), then \( S \) has a greatest element.
:::

::: {.proof}
Let \( b \) be a lower bound and \( T \coloneqq \{ s - b : s \in S \} \), a non-empty set. For \( s \in S \), \( s \ge b \) gives \( s - b \ge 0 \) by (O3), so \( T \subseteq \{ x \in \nZ : x \ge 0 \} = \nN \) by @thm-integers-ordered-ring (b). By @thm-omega-well-ordering, \( T \) has an element \( m \) with \( m \le t \) for every \( t \in T \), in the order of \( \nN \) and so in that of \( \nZ \) (@thm-integers-ordered-ring (a)). Then \( m = s_0 - b \) for some \( s_0 \in S \), so \( m + b = s_0 \in S \); and for \( s \in S \), \( s - b \ge m \) gives \( s \ge m + b \) by (O3). So \( m + b \) is least in \( S \).

If \( c \) is an upper bound, then \( -S \coloneqq \{ -s : s \in S \} \) has the lower bound \( -c \) (@prp-ordered-ring-rules (a)); if \( -s_1 \) is its least element, then \( s \le s_1 \) for every \( s \in S \), by @prp-ordered-ring-rules (a) again. This proves the proposition.
:::

Both hypotheses are needed: \( \nZ \) has no least element, and neither has \( \emptyset \), which every integer bounds. The rules of @prp-ordered-ring-rules also show that some rings carry no order at all.

::: {#exm-finite-ring-not-orderable}
[A field with two elements that cannot be ordered]

Let \( R \coloneqq \{0, 1\} \), two distinct elements, with addition and multiplication given by the tables
\[
\begin{array}{c|cc}
+ & 0 & 1 \\ \hline
0 & 0 & 1 \\
1 & 1 & 0
\end{array}
\qquad\qquad
\begin{array}{c|cc}
\cdot & 0 & 1 \\ \hline
0 & 0 & 0 \\
1 & 0 & 1
\end{array}
\]
Check that \( R \) satisfies (F1)–(F9), so that it is a field, and show that no relation \( < \) on \( R \) makes it an ordered commutative ring.
:::

::: {.solution}
*The axioms.* (F1), (F6): both tables are symmetric. (F3), (F7): the row of \( 0 \) in the first table and of \( 1 \) in the second repeat the headings. (F4): \( -0 = 0 \) and \( -1 = 1 \), since \( 1 + 1 = 0 \). (F8): \( 1 \cdot 1 = 1 \). And \( 1 \ne 0 \).

The three laws with three variables can be checked over the eight triples \( (a, b, c) \), or by cases. From the tables, \( 0 \cdot x = 0 \) and \( 1 \cdot x = x \), and \( x + y = 1 \) exactly when one of \( x, y \) is \( 1 \). (F2): both sides are \( 1 \) exactly when an odd number of \( a, b, c \) (one or three) are \( 1 \). (F5): both sides are \( 1 \) exactly when \( a = b = c = 1 \). (F9): if \( a = 0 \), both sides are \( 0 \); if \( a = 1 \), both sides are \( b + c \). So \( R \) is a field.

*No order.* If \( < \) made \( R \) an ordered commutative ring, then, as \( 1 \ne 0 \), @prp-ordered-ring-rules (h) would give \( 2 \cdot 1 > 0 \). But \( 2 \cdot 1 = 1 \cdot 1 + 1 = (0 + 1) + 1 = 0 \) by the definition of multiples, and \( 0 > 0 \) is forbidden by (O1).
:::

The argument uses only \( 1 \ne 0 \) and \( n \cdot 1 = 0 \) for some \( n \ge 1 \). So **no commutative ring with \( 1 \ne 0 \) in which \( n \cdot 1 = 0 \) for some \( n \in \nN \), \( n \ge 1 \), can be ordered**. The integers modulo \( n \ge 2 \) of Section 7.5 are such rings, since \( n \cdot [1] = [n] = [0] \); a later chapter of this volume rebuilds them on the constructed \( \nZ \).

## Exercises

### A. Check your understanding

::: {#exr-ordered-rings-a1}
[A1]

Let \( R \) be an ordered commutative ring.

::: {.enumerate options="label=(\alph*)"}
1. Here is a proof that if \( a < 0 < b \), then \( ab < a^2 + b^2 \). Name the axiom, rule or result that justifies each of the five steps. (1) \( ab < 0 \cdot b \). (2) \( 0 \cdot b = 0 \). (3) \( a^2 > 0 \) and \( b^2 > 0 \). (4) \( a^2 + b^2 > 0 + 0 = 0 \). (5) \( ab < a^2 + b^2 \).
2. True or false: "\( R \) has no zero divisors." Give a reason.
3. True or false: "\( 1 > 0 \) in every ordered commutative ring." Give a reason.
4. Name the move by which @thm-integers-commutative-ring was proved, and say which row of its table needed the relation \( \sim \) rather than equality of pairs.
:::
:::

::: {.solution}
(a) (1) @prp-ordered-ring-rules (c), with \( a < 0 \) and \( b > 0 \). (2) @prp-ring-algebra (b) and (F6). (3) @prp-ordered-ring-rules (e), as \( a, b \ne 0 \) by (O1). (4) @prp-ordered-ring-rules (b), strict, and (F3). (5) (O2).

(b) True, by @prp-ordered-ring-rules (f); a general commutative ring may have zero divisors (the warning after @def-commutative-ring-and-field).

(c) False: in the zero ring with the empty relation, \( 1 = 0 \). It is true when \( 1 \ne 0 \) (@prp-ordered-ring-rules (e)).

(d) **Reduce to the level below**: on representatives, each axiom becomes an identity in \( \nN \). Only (F4) needed \( \sim \): \( (a + b, b + a) \) is related to \( (0, 0) \) but is not that pair.
:::

### B. Practice

::: {#exr-ordered-rings-b1}
[B1: Three rows in detail]

Let \( x = [(a, b)] \), \( y = [(c, d)] \), \( z = [(e, f)] \) be integers. Verify in detail, naming the law of \( \nN \) used at each step, the rows (F9), (F4) and (F6) of the table in the proof of @thm-integers-commutative-ring.
:::

::: {.solution}
All operations are those of @def-integer-operations, and "Law" refers to @thm-omega-arithmetic-laws.

(F9). Since \( y + z = [(c + e, d + f)] \), \( x(y + z) = [(a(c + e) + b(d + f), \ a(d + f) + b(c + e))] \), whose coordinates are \( ac + ae + bd + bf \) and \( ad + af + bc + be \) by Law (d). And \( xy + xz = [((ac + bd) + (ae + bf), \ (ad + bc) + (af + be))] \), whose coordinates are the same sums by Laws (b), (c). So both sides are the class of one pair.

(F4). \( x + (-x) = [(a + b, b + a)] \), and \( (a + b, b + a) \sim (0, 0) \) means \( (a + b) + 0 = (b + a) + 0 \) (@def-integers-as-classes), true by @def-omega-arithmetic (a) and Law (b). So \( x + (-x) = [(0, 0)] \) by @thm-classes-partition (b).

(F6). \( yx = [(ca + db, cb + da)] \). By Law (f), \( ca = ac \), \( db = bd \), \( cb = bc \), \( da = ad \), and by Law (b), \( bc + ad = ad + bc \); so the pair is \( (ac + bd, ad + bc) \), the pair of \( xy \).
:::

::: {#exr-ordered-rings-b2}
[B2: The wrong positive set]

Let \( P' \coloneqq \{ [(a, b)] : a < b \} \subseteq \nZ \). Show that membership in \( P' \) does not depend on the representative, that \( P' \) satisfies (P2) of @prp-order-from-positives, and that it does not satisfy (P1). Which part of (P1) fails?
:::

::: {.solution}
*Independence of representatives.* If \( (a, b) \sim (a', b') \) and \( b = a + k \) with \( k \ne 0 \), then \( a + b' = a + (k + a') \), so \( b' = a' + k \) by cancellation (@prp-omega-order-arithmetic (a), (b)). By @thm-well-defined-on-classes (c), \( [(a, b)] \in P' \) if and only if \( a < b \).

*(P2).* For \( x = [(a, b)] \): \( x \in P' \) iff \( a < b \); \( x = 0 \) iff \( a = b \) (as in the proof of @thm-integers-ordered-ring); \( -x \in P' \) iff \( b < a \). By trichotomy in \( \nN \) (@thm-omega-order (a)), exactly one holds.

*(P1) fails for products.* \( [(0, 1)] \in P' \), but
\[
[(0, 1)] \cdot [(0, 1)] = [(0 \cdot 0 + 1 \cdot 1, \ 0 \cdot 1 + 1 \cdot 0)] = [(1, 0)] ,
\]
and \( [(1, 0)] \notin P' \), since \( 1 < 0 \) is false. The sum half of (P1) holds, as in the proof of @thm-integers-ordered-ring. So \( P' \), the negative integers, fails only closure under products; it would define the reversed order, which breaks exactly (O4).
:::

### C. Going deeper

::: {#exr-ordered-rings-c1}
[C1: Ordered rings are infinite]

::: {.enumerate options="label=(\alph*)"}
1. Prove the sum law of @prp-ordered-ring-rules (h) in full: for every ordered commutative ring \( R \), every \( a \in R \) and all \( m, k \in \nN \), \( (m + k) \cdot a = m \cdot a + k \cdot a \). State the property you induct on and justify every equality.
2. Deduce that every ordered commutative ring with \( 1 \ne 0 \) is infinite (@def-infinite).
3. The set \( \{0, 1, 2\} \) with addition and multiplication "modulo \( 3 \)", given by the tables below, is a commutative ring with \( 1 \ne 0 \) (you may take this for granted). Show that it cannot be ordered.
:::

\[
\begin{array}{c|ccc}
+ & 0 & 1 & 2 \\ \hline
0 & 0 & 1 & 2 \\
1 & 1 & 2 & 0 \\
2 & 2 & 0 & 1
\end{array}
\qquad\qquad
\begin{array}{c|ccc}
\cdot & 0 & 1 & 2 \\ \hline
0 & 0 & 0 & 0 \\
1 & 0 & 1 & 2 \\
2 & 0 & 2 & 1
\end{array}
\]
:::

::: {.solution}
[Hint 1]

For (b): what does (h) say about \( k \mapsto k \cdot 1 \)?
:::

::: {.solution}
[Hint 2]

Suppose \( R \) has \( m \) elements; consider \( k \mapsto k \cdot 1 \) on \( \{1, \dots, m + 1\} \).
:::

::: {.solution}
(a) Fix \( R \), \( a \in R \), \( m \in \nN \), and use @ax-induction (through @cor-omega-identification (b)) on \( k \), for \( P(k) \): "\( (m + k) \cdot a = m \cdot a + k \cdot a \)". *Base:* \( (m + 0) \cdot a = m \cdot a = m \cdot a + 0 = m \cdot a + 0 \cdot a \), by @def-omega-arithmetic (a), (F3) and \( 0 \cdot a = 0 \). *Step:* assume \( P(k) \). Then
\[
\begin{aligned}
(m + (k + 1)) \cdot a &= ((m + k) + 1) \cdot a = (m + k) \cdot a + a \\
&= (m \cdot a + k \cdot a) + a = m \cdot a + (k \cdot a + a) \\
&= m \cdot a + (k + 1) \cdot a .
\end{aligned}
\]
by associativity in \( \nN \) (@thm-omega-arithmetic-laws (c)), the recursion for multiples, \( P(k) \), (F2), and the recursion again. So \( P(k + 1) \) holds, and \( P(k) \) holds for every \( k \).

(b) Let \( 1 \ne 0 \) in \( R \), and suppose \( R \) has \( m \) elements for some \( m \in \nN \) (@def-finite). Let \( f \colon \{1, \dots, m + 1\} \to R \), \( f(k) \coloneqq k \cdot 1 \). If \( k < l \), then \( k \cdot 1 < l \cdot 1 \) by @prp-ordered-ring-rules (h), so \( k \cdot 1 \ne l \cdot 1 \) by (O1): \( f \) is injective. But \( \{1, \dots, m + 1\} \) has \( m + 1 > m \) elements (by its identity map), so @cor-pigeonhole-finite-sets (a) forbids an injection into \( R \). This contradiction shows that \( R \) is infinite (@def-infinite).

(c) By the definition of multiples and the tables, \( 1 \cdot 1 = 0 + 1 = 1 \), \( 2 \cdot 1 = 1 + 1 = 2 \) and \( 3 \cdot 1 = 2 + 1 = 0 \). An order would give \( 3 \cdot 1 > 0 \) by @prp-ordered-ring-rules (h), since \( 1 \ne 0 \), that is, \( 0 > 0 \), against (O1). (Alternatively, (b) applies to this finite ring.)

**Marking scheme.** (10 points)
- 1: (a) states the induction property with \( m \) and \( a \) fixed and \( k \) the induction variable.
- 2: (a) base case, citing \( m + 0 = m \), \( 0 \cdot a = 0 \) and (F3).
- 2: (a) inductive step, with associativity in \( \nN \), the recursion, the hypothesis and (F2) each named.
- 2: (b) shows that \( k \mapsto k \cdot 1 \) is injective, citing (h) and (O1).
- 2: (b) derives the contradiction from @cor-pigeonhole-finite-sets (a) with \( m + 1 > m \) elements (or any correct count).
- 1: (c) computes \( 3 \cdot 1 = 0 \) and concludes.
Fatal errors (0 for the step): inducting on \( m \) and \( k \) at once without fixing one; using \( 1 > 0 \) without \( 1 \ne 0 \); in (b), "the multiples are all different, so there are infinitely many" with no pigeonhole step. A route for (b) composing the inverse of a bijection \( \{1, \dots, m\} \to R \) with \( f \) earns the same 4 points.
:::

<!-- dependency ledger
def-commutative-ring-and-field (example): the integers modulo 6 form a commutative ring, and [2][3] = [0] (the warning after the definition) | Ch 7 Section 7.5 (prp-congruence-arithmetic, school integers); illustration only, nothing depends on it
def-commutative-ring-and-field (example): the zero ring satisfies (F1)-(F7), (F9) | inline (every equation reads 0 = 0)
thm-integers-commutative-ring (proof): substituting equal natural numbers inside sums and products | equality rules of Ch 4 (=E)
prp-order-from-positives (proof): -(b - a) = a - b, (c - b) + (b - a) = c - a, -(a + c) = (-a) + (-c), -0 = 0 | inline (from prp-ring-algebra (a))
thm-integers-ordered-ring (proof): (a, b) ~ (0, 0) iff a = b | def-integers-as-classes with def-omega-arithmetic (a) (cited)
prp-ordered-ring-rules (proof): the multiples n.a exist and are unique | thm-recursion via cor-omega-identification (b) (cited before the statement)
prp-ordered-ring-rules (proof): a natural number n >= 1 is j + 1 for some j | prp-omega-order-arithmetic (a) (cited), with 1 + j = j + 1 by thm-omega-arithmetic-laws (b)
prp-integer-least-element (proof): T = {s - b : s in S} is a set | image of S under s |-> s - b (Ch 6, def-image); not cited by label
exm-finite-ring-not-orderable (solution): (F2), (F5), (F9) for the two-element tables | inline case check (all eight triples)
exr-ordered-rings-c1 (solution): {1, ..., m + 1} has m + 1 elements | def-finite (identity bijection; inline)
-->
