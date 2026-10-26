# Commutative Rings; the Integers Are One

Sections 2.1 and 2.2 built \( \nZ \) with well-defined operations \( + \), \( \cdot \) and \( - \). Why was it built at all? \( \nN \) already adds and multiplies by all the usual laws but one: it has no negatives, since \( 1 + x = x + 1 \ne 0 \) for every \( x \in \nN \) (@thm-omega-arithmetic-laws (b), @cor-omega-successor-cancellation). This section collects the laws of school algebra into one definition, a **commutative ring**, checks them for \( \nZ \) by reducing each to a law of \( \nN \), and derives the consequences that hold in every commutative ring.

## The laws of a ring

Expanding brackets or moving a term across an equation uses a short list of laws: sums and products may be reordered and regrouped, \( 0 \) and \( 1 \) do nothing, every element has a negative, and products distribute over sums. The list holds in \( \nZ \), it will hold in \( \nQ \), and a result proved from the list alone holds wherever the list does. It deserves a name.

*A commutative ring is a set where you may add, subtract and multiply by the usual rules; a field is one where you may also divide by anything non-zero.*

::: {#def-commutative-ring-and-field}
[Commutative Ring, Field]

A **commutative ring** is a set \( R \) with two functions, **addition** \( + \colon R \times R \to R \) and **multiplication** \( \cdot \colon R \times R \to R \) (written \( a \cdot b = ab \)), such that clauses (F1)–(F7) and (F9) of the following list hold; clause (F8) is used only for fields.

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

A **field** is a commutative ring in which, **in addition**, \( 1 \ne 0 \) and (F8) holds. We write \( a - b \coloneqq a + (-b) \), and in a field \( a / b \coloneqq a b^{-1} \) for \( b \ne 0 \).
:::

In words: (F1)–(F4) say that addition is commutative and associative, with a neutral element \( 0 \) and negatives; (F5)–(F7) say the first three things about multiplication; (F9) links the two and lets us expand brackets. (F8) asks for inverses of **non-zero** elements only, and only in a field. The notations \( -a \) and \( a^{-1} \) anticipate that these elements are unique, which we prove below. These are the axioms (F1)–(F9) of the linear-algebra companion, Chapter 0, and of the ordered fields of *Analysis on the Real Line*, Chapter 1, in the same numbering, except that there (F7) includes \( 1 \ne 0 \).

**Examples.**

- \( \nZ \), with the operations of @def-integer-operations: the next theorem.
- **The zero ring** \( R \coloneqq \{0\} \), with \( 0 + 0 \coloneqq 0 \), \( 0 \cdot 0 \coloneqq 0 \) and \( 1 \coloneqq 0 \). Every axiom other than (F8) is an equation in \( R \), and every such equation reads \( 0 = 0 \). So \( R \) is a commutative ring, with \( 1 = 0 \), and not a field. This degenerate ring is why several results below assume \( 1 \ne 0 \).

**A non-example by minimal change.** The set \( \nN \), with its addition and multiplication from Chapter 1, satisfies (F1)–(F3), (F5)–(F7) and (F9), by @thm-omega-arithmetic-laws and @def-omega-arithmetic (a). That one missing clause, (F4), is why \( \nZ \) had to be built.

**Why these clauses.** No axiom says that \( ab = 0 \) forces \( a = 0 \) or \( b = 0 \): that is true in \( \nZ \) but fails in other commutative rings (the warning below), so it must be proved where it holds. The condition \( 1 \ne 0 \) is kept out of the ring axioms, so that the zero ring is a ring, and put into the field axioms, so that \( \{0\} \), where (F8) holds vacuously, is not a field.

::: {.warning}
A commutative ring may have **zero divisors**: non-zero \( a, b \) with \( ab = 0 \). The integers modulo \( 6 \) of *Sets and Functions*, Section 5.2 (built there from the school integers, with well-defined operations by @fd2:prp-congruence-arithmetic) form a commutative ring: each of (F1)–(F7) and (F9) passes from the school integers to classes through representatives, a check we do not need and do not carry out here. In this ring \( [2] \ne [0] \) and \( [3] \ne [0] \), yet \( [2][3] = [6] = [0] \). So "\( ab = 0 \), hence \( a = 0 \) or \( b = 0 \)" is not a consequence of (F1)–(F9). In an **ordered** ring it is a theorem, proved in Section 2.4 from the order axioms.
:::

## The integers form a commutative ring

To prove a law for classes, compute both sides through representatives; the two pairs of natural numbers are then equal or related, and the classes agree.

::: {#thm-integers-commutative-ring}
[The Integers Form a Commutative Ring]

\( \nZ \), with the addition, multiplication and negation of @def-integer-operations, is a commutative ring, with zero \( [(0, 0)] \) and one \( [(1, 0)] \), and in it \( 1 \ne 0 \).
:::

::: {.idea}
[Scratch work]

Take (F9), the law with the most terms.

| Givens | Goal |
|---|---|
| \( x, y, z \in \nZ \) | \( x(y + z) = xy + xz \) |
| \( x = [(a, b)] \), \( y = [(c, d)] \), \( z = [(e, f)] \): every class has a representative (@fd2:def-quotient-set) | two classes, each computed by @def-integer-operations from these representatives |
| left: \( (a(c + e) + b(d + f), \ a(d + f) + b(c + e)) \); right: \( ((ac + bd) + (ae + bf), \ (ad + bc) + (af + be)) \) | equal pairs, or related pairs |
| distribute in \( \nN \), then regroup four terms | the same pair: the classes are equal |

The operations are functions (@prp-integer-operations-well-defined), so any representatives may be used. Only (F4) will need \( \sim \); only (F5) is long.
:::

::: {.proof}
By @prp-integer-operations-well-defined, \( + \) and \( \cdot \) are functions \( \nZ \times \nZ \to \nZ \). Let \( x, y, z \in \nZ \); by @fd2:def-quotient-set, \( x = [(a, b)] \), \( y = [(c, d)] \), \( z = [(e, f)] \) with \( a, \dots, f \in \nN \). By @def-integer-operations, each side of each axiom is the class of the pair shown in the table. "Equal" means the same pair of natural numbers, by @thm-omega-arithmetic-laws and @def-omega-arithmetic (a), (b). "Related" means related by \( \sim \) (@def-integers-as-classes: \( (p, q) \sim (r, s) \) means \( p + s = q + r \)), so the classes agree by @fd2:thm-classes-partition (b).

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

The proof used one move eight times. It has a name.

::: {#exm-method-reduce-to-level-below}
[Method: reduce to the level below]

**Template.** To prove a law about classes whose operations are defined on representatives: (1) write each element as a class \( [p] \); (2) compute each side by the defining formulas, with any representatives, since the operations are well defined; (3) compare the two representatives at the level below, by its laws: equal, or related; (4) conclude that the classes are equal (@fd2:thm-classes-partition (b)).

**When to use it.** Laws in \( \nZ \), with \( \nN \) below; any structure whose operations are formulas in a known ring (Exercise C1 below).

**The usual failure.** Claiming equal pairs where only \( \sim \) holds (the row (F4)); computing with representatives before the operation is known to be a function; using a law of \( \nZ \) inside the computation in \( \nN \), which is circular.
:::

::: {.remark}
The zero and one of this ring are \( [(0, 0)] = \iota(0) \) and \( [(1, 0)] = \iota(1) \) (@prp-naturals-embed-integers), so after the identification of Section 2.2 they are the elements \( 0 \) and \( 1 \) of \( \nN \). With \( a - b \coloneqq a + (-b) \), the formula \( [(a, b)] = \iota(a) + (-\iota(b)) \) of @prp-naturals-embed-integers reads \( [(a, b)] = a - b \) for \( a, b \in \nN \): the subtraction the pair recorded is now performed in \( \nZ \).
:::

::: {.check}
Which class is the negative of \( [(2, 7)] \)? Show by reducing to \( \nN \) that no other class \( [(c, d)] \) satisfies \( [(2, 7)] + [(c, d)] = [(0, 0)] \).
:::

::: {.solution}
\( -[(2, 7)] = [(7, 2)] \) (@def-integer-operations). Now suppose \( [(2 + c, \ 7 + d)] = [(0, 0)] \). By @fd2:thm-classes-partition (b) and @def-integers-as-classes, \( (2 + c) + 0 = (7 + d) + 0 \), so \( 2 + c = 7 + d = 2 + (5 + d) \), and \( c = 5 + d \) by cancellation (@prp-omega-order-arithmetic (b)). Then \( c + 2 = (5 + d) + 2 = d + 7 \), that is, \( (c, d) \sim (7, 2) \), and \( [(c, d)] = [(7, 2)] \) (@fd2:thm-classes-partition (b)). @prp-ring-algebra (a) below proves the same uniqueness in every commutative ring, from (F1)–(F9) alone.
:::

What the definition does not list must be derived, and the derivations work in every commutative ring at once.

::: {#prp-ring-algebra}
[Algebra in a Commutative Ring]

Let \( R \) be a commutative ring, and let \( a, b \in R \).

::: {.enumerate options="label=(\alph*)"}
1. The elements \( 0 \) and \( 1 \) of (F3) and (F7) are unique, the element \( -a \) of (F4) is unique, and \( -(-a) = a \).
2. \( a \cdot 0 = 0 \).
3. \( (-a)b = a(-b) = -(ab) \) and \( (-a)(-b) = ab \).
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

Every law of @prp-ring-algebra could also be checked in \( \nZ \) by the method of @exm-method-reduce-to-level-below. The next example puts the two routes side by side.

::: {#exm-integer-laws-two-routes}
[One law, two routes]

Prove that \( (-x)y = -(xy) \) for all \( x, y \in \nZ \) in two ways: (a) by reducing to the level below; (b) from (F1)–(F9) alone.
:::

::: {.solution}
(a) Let \( x = [(a, b)] \) and \( y = [(c, d)] \). By @def-integer-operations, \( -x = [(b, a)] \), so
\[
(-x)y = [(bc + ad, \ bd + ac)] ;
\]
and \( xy = [(ac + bd, \ ad + bc)] \), so \( -(xy) = [(ad + bc, \ ac + bd)] \). The two pairs are equal, since \( bc + ad = ad + bc \) and \( bd + ac = ac + bd \) by commutativity of \( + \) in \( \nN \) (@thm-omega-arithmetic-laws (b)). So the classes are equal.

(b) \( \nZ \) is a commutative ring (@thm-integers-commutative-ring), so @prp-ring-algebra (c), with \( a = x \) and \( b = y \), gives \( (-x)y = -(xy) \).

Route (a) is shorter here, but it proves the law only for \( \nZ \). Route (b) proves it in every commutative ring at once, which is why @prp-ring-algebra is stated for rings.
:::

The argument of (a) with multiplication shows that in a **field** a non-zero \( a \) has only one inverse: if \( ab = 1 \) and \( ac = 1 \), then \( b = b \cdot 1 = b(ac) = (ba)c = (ab)c = 1 \cdot c = c \), by (F7), (F5) and (F6). So \( a^{-1} \), and with it \( a/b \), names a single element. And (b) explains the zero ring: if \( 1 = 0 \) in a commutative ring, then \( a = a \cdot 1 = a \cdot 0 = 0 \) for every \( a \), so the ring is \( \{0\} \).

::: {.check}
In a field, let \( a \ne 0 \). Show that \( (a^{-1})^{-1} = a \).
:::

::: {.solution}
First, \( a^{-1} \ne 0 \): otherwise \( 1 = a a^{-1} = a \cdot 0 = 0 \), by (F8) and @prp-ring-algebra (b), against \( 1 \ne 0 \) in a field. So \( a^{-1} \) has an inverse by (F8). And \( a^{-1} a = a a^{-1} = 1 \) by (F6), so \( a \) is an inverse of \( a^{-1} \). By the uniqueness of inverses just proved, it is the inverse: \( (a^{-1})^{-1} = a \).
:::

## Exercises

### A. Check your understanding

::: {#exr-commutative-rings-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State (F4) with its quantifiers, and say why the zero ring satisfies it.
2. Name the move by which @thm-integers-commutative-ring was proved, and say which row of its table needed \( \sim \) rather than equality of pairs.
3. True or false, with a reason: in every commutative ring, \( ab = 0 \) implies \( a = 0 \) or \( b = 0 \).
4. Prove from (F1)–(F9) and @prp-ring-algebra that \( (a + b)(a - b) = a^2 - b^2 \) in every commutative ring, where \( x^2 \coloneqq xx \).
:::
:::

::: {.solution}
(a) For every \( a \in R \) there is an element \( -a \in R \) with \( a + (-a) = 0 \). In \( \{0\} \) the only element is \( 0 \), and \( -0 \coloneqq 0 \) works, since \( 0 + 0 = 0 \).

(b) **Reduce to the level below** (@exm-method-reduce-to-level-below). Only (F4) needed \( \sim \): the pair \( (a + b, b + a) \) is related to \( (0, 0) \), but it is not that pair.

(c) False. In the integers modulo \( 6 \), \( [2][3] = [6] = [0] \) with \( [2] \ne [0] \) and \( [3] \ne [0] \) (the warning after @def-commutative-ring-and-field, where the ring laws are taken for granted).

(d) By (F9), (F6) and (F9) again,
\[
\begin{aligned}
(a + b)\bigl(a + (-b)\bigr) &= (a + b)a + (a + b)(-b) \\
&= \bigl(aa + ba\bigr) + \bigl(a(-b) + b(-b)\bigr) .
\end{aligned}
\]
By @prp-ring-algebra (c), \( a(-b) = -(ab) \) and \( b(-b) = -(bb) \); and \( ba = ab \) by (F6). Regrouping by (F1) and (F2), the sum is
\[
a^2 + \bigl(ab + (-(ab))\bigr) + \bigl(-(b^2)\bigr) = a^2 + 0 + \bigl(-(b^2)\bigr) = a^2 - b^2 ,
\]
by (F4) and (F3), and the definition \( u - v \coloneqq u + (-v) \).
:::

### B. Practice

::: {#exr-ordered-rings-b1}
[B1: Three rows in detail]

Let \( x = [(a, b)] \), \( y = [(c, d)] \), \( z = [(e, f)] \) be integers. Verify in detail, naming the law of \( \nN \) used at each step, the rows (F9), (F4) and (F6) of the table in the proof of @thm-integers-commutative-ring.
:::

::: {.solution}
All operations are those of @def-integer-operations, and "Law" refers to @thm-omega-arithmetic-laws.

(F9). Since \( y + z = [(c + e, d + f)] \), \( x(y + z) = [(a(c + e) + b(d + f), \ a(d + f) + b(c + e))] \), whose coordinates are \( ac + ae + bd + bf \) and \( ad + af + bc + be \) by Law (d). And \( xy + xz = [((ac + bd) + (ae + bf), \ (ad + bc) + (af + be))] \), whose coordinates are the same sums by Laws (b), (c). So both sides are the class of one pair.

(F4). \( x + (-x) = [(a + b, b + a)] \), and \( (a + b, b + a) \sim (0, 0) \) means \( (a + b) + 0 = (b + a) + 0 \) (@def-integers-as-classes), true by @def-omega-arithmetic (a) and Law (b). So \( x + (-x) = [(0, 0)] \) by @fd2:thm-classes-partition (b).

(F6). \( yx = [(ca + db, cb + da)] \). By Law (f), \( ca = ac \), \( db = bd \), \( cb = bc \), \( da = ad \), and by Law (b), \( bc + ad = ad + bc \); so the pair is \( (ac + bd, ad + bc) \), the pair of \( xy \).
:::

::: {#exr-commutative-rings-b2}
[B2: Prove or disprove]

Prove or disprove.

::: {.enumerate options="label=(\alph*)"}
1. For all \( x, y \in \nZ \), \( -(x + y) = (-x) + (-y) \).
2. In every commutative ring, \( a \cdot a = a \) implies \( a = 0 \) or \( a = 1 \).
3. The set \( \nN \times \nN \) itself, with \( (a, b) + (c, d) \coloneqq (a + c, \ b + d) \) and \( (a, b) \cdot (c, d) \coloneqq (ac + bd, \ ad + bc) \), is a commutative ring.
4. In every commutative ring, \( a + b = a \) implies \( b = 0 \).
:::
:::

::: {.solution}
(a) **True**, by reducing to the level below. Let \( x = [(a, b)] \) and \( y = [(c, d)] \). By @def-integer-operations, \( -(x + y) = -[(a + c, \ b + d)] = [(b + d, \ a + c)] \), and \( (-x) + (-y) = [(b, a)] + [(d, c)] = [(b + d, \ a + c)] \). The pairs are equal, so the classes are.

(b) **False.** In the integers modulo \( 6 \) (ring laws taken for granted, as in the warning after @def-commutative-ring-and-field), \( [3][3] = [9] = [3] \), since \( 9 - 3 = 6 \); and \( [3] \) is neither \( [0] \) nor \( [1] \), since neither \( 3 \) nor \( 2 \) is a multiple of \( 6 \).

(c) **False:** (F4) fails. A zero \( z = (z_1, z_2) \) would satisfy \( (a, b) + z = (a, b) \) for all pairs; taking \( (a, b) = (0, 0) \) gives \( (0, 0) + z = (0 + z_1, \ 0 + z_2) = z \) by @thm-omega-arithmetic-laws (a), so \( z = (0, 0) \). But \( (1, 0) + (x, y) = (1 + x, \ y) \ne (0, 0) \) for every pair \( (x, y) \), since \( 1 + x = x + 1 \ne 0 \) (@thm-omega-arithmetic-laws (b), @cor-omega-successor-cancellation). So \( (1, 0) \) has no negative. Passing to classes is what supplies negatives.

(d) **True.** Add \( -a \):
\[
b = 0 + b = \bigl((-a) + a\bigr) + b = (-a) + (a + b) = (-a) + a = 0 ,
\]
by (F1) and (F3), (F1) and (F4), (F2), the hypothesis, and (F1) and (F4) again.
:::

### C. Going deeper

::: {#exr-commutative-rings-c1}
[C1: A ring in disguise]

On \( \nZ \) define \( x \oplus y \coloneqq x + y - 1 \) and \( x \odot y \coloneqq x + y - xy \).

::: {.enumerate options="label=(\alph*)"}
1. Find the elements that play the parts of \( 0 \) and \( 1 \) in (F3) and (F7), and the negative of \( x \) in (F4).
2. Prove (F9) for \( \oplus \), \( \odot \) directly.
3. Let \( \varphi(x) \coloneqq 1 - x \). Show that \( \varphi(x \oplus y) = \varphi(x) + \varphi(y) \), \( \varphi(x \odot y) = \varphi(x)\varphi(y) \) and \( \varphi(\varphi(x)) = x \), and use this to prove (F5) for \( \odot \) without expanding.
:::
:::

::: {.solution}
[Hint 1]

In (a), solve \( x \oplus e = x \) for \( e \).
:::

::: {.solution}
[Hint 2]

In (c), apply \( \varphi \) to both sides of (F5) and use that \( \varphi \) is injective.
:::

::: {.solution}
All computations below are in the commutative ring \( \nZ \) (@thm-integers-commutative-ring), with the rules of @prp-ring-algebra (c). We also use \( -(u + v) = (-u) + (-v) \): both sides are negatives of \( u + v \), by (F1), (F2) and (F4), and negatives are unique (@prp-ring-algebra (a)).

(a) The zero is \( 1 \): \( x \oplus 1 = x + 1 - 1 = x \). The one is \( 0 \): \( x \odot 0 = x + 0 - x \cdot 0 = x \). The negative of \( x \) is \( 2 - x \): \( x \oplus (2 - x) = x + (2 - x) - 1 = 1 \), the zero.

(b) On the left,
\[
\begin{aligned}
x \odot (y \oplus z) &= x + (y + z - 1) - x(y + z - 1) \\
&= 2x + y + z - 1 - xy - xz .
\end{aligned}
\]
On the right, \( (x \odot y) \oplus (x \odot z) = (x + y - xy) + (x + z - xz) - 1 \), which regroups to the same expression.

(c) The three identities:
\[
\begin{aligned}
1 - (x + y - 1) &= (1 - x) + (1 - y) , \\
1 - (x + y - xy) &= (1 - x)(1 - y) , \\
1 - (1 - x) &= x .
\end{aligned}
\]
(For the second, expand the right side: \( 1 - y - x + xy \).) The third makes \( \varphi \) injective: if \( \varphi(x) = \varphi(x') \), then \( x = \varphi(\varphi(x)) = \varphi(\varphi(x')) = x' \). Now
\[
\begin{aligned}
\varphi\bigl((x \odot y) \odot z\bigr) &= \bigl(\varphi(x)\varphi(y)\bigr)\varphi(z) \\
&= \varphi(x)\bigl(\varphi(y)\varphi(z)\bigr) = \varphi\bigl(x \odot (y \odot z)\bigr) ,
\end{aligned}
\]
by the second identity twice, (F5) in \( \nZ \), and the second identity twice more. Injectivity gives \( (x \odot y) \odot z = x \odot (y \odot z) \).

The level below is now \( \nZ \) itself, and \( \varphi \) carries every law of \( \nZ \) across to \( \oplus \), \( \odot \).

**Marking scheme.** (10 points)
- 3: (a) finds the zero \( 1 \), the one \( 0 \) and the negative \( 2 - x \), each checked by a computation.
- 3: (b) expands both sides to one expression, with the laws of \( \nZ \) used.
- 1: (c) verifies the three identities for \( \varphi \).
- 1: (c) shows that \( \varphi \) is injective from \( \varphi(\varphi(x)) = x \).
- 2: (c) carries (F5) across \( \varphi \) and concludes by injectivity.
Fatal errors (0 for the step): assuming the laws for \( \oplus \), \( \odot \) in (b); applying \( \varphi \) and concluding equality of the arguments without injectivity. A reader who proves (F5) for \( \odot \) by direct expansion earns the 2 points of the last step only if the expansion is complete and correct, and loses none of the others.
:::

<!-- dependency ledger
def-commutative-ring-and-field (example): the integers modulo 6 satisfy (F1)-(F7), (F9), and [2][3] = [0] (the warning after the definition) | not proved here: operations well defined by F2.5 §02 (prp-congruence-arithmetic, school integers), laws pass to classes through representatives; marked in the text; illustration only, nothing depends on it; F5.1 (Algebraic Preliminaries, Chapter 1) rebuilds it on the constructed Z
def-commutative-ring-and-field (claim): prose pointer, (F1)-(F9) match the field axioms of the linear-algebra companion, Chapter 0, and of the ordered fields of AN1.1 | AN1.1, companion ch 0 (prose pointer; nothing here depends on it)
def-commutative-ring-and-field (example): the zero ring satisfies (F1)-(F7), (F9) | inline (every equation reads 0 = 0)
thm-integers-commutative-ring (proof): substituting equal natural numbers inside sums and products | equality rules of F1.4 (=E)
exm-method-reduce-to-level-below (claim): (quick check) 2 + c = 7 + d gives c = 5 + d, and (5 + d) + 2 = d + 7 | numeral arithmetic by def-omega-arithmetic (2 + 5 = 7), thm-omega-arithmetic-laws (b), (c); cancellation cited; verify/ch02/exm-integer-laws-two-routes.py
prp-ring-algebra (claim): (quick check after the field paragraph) uniqueness of inverses in a field | inline (the paragraph after prp-ring-algebra, no label)
exm-integer-laws-two-routes (solution): the pairs (bc + ad, bd + ac) and (ad + bc, ac + bd) are equal | thm-omega-arithmetic-laws (b) (cited); verify/ch02/exm-integer-laws-two-routes.py
exr-commutative-rings-a1 (solution): (c) [2][3] = [0] in the integers modulo 6 | as the first line (illustration only; ring laws not proved here, marked)
exr-commutative-rings-a1 (solution): (d) u - v = u + (-v) | def-commutative-ring-and-field (cited by clause)
exr-commutative-rings-b2 (solution): (b) [3][3] = [9] = [3] in the integers modulo 6, 3 and 2 not multiples of 6 | ring laws as for the modulo-6 example (illustration only, marked); F2.5 §02 def-congruence; verify/ch02/exr-commutative-rings-b2.py
exr-commutative-rings-b2 (solution): (c) the only additive zero of N x N is (0, 0); (1, 0) has no negative | inline; verify/ch02/exr-commutative-rings-b2.py
exr-commutative-rings-c1 (solution): the arithmetic of 2 = 1 + 1, x + 0 = x, x.0 = 0 in Z, and the regroupings of (b), (c) | thm-integers-commutative-ring, prp-ring-algebra (cited at the start of the solution); -(u + v) = (-u) + (-v) inline; verify/ch02/exr-commutative-rings-c1.py
exr-commutative-rings-c1 (solution): phi injective from phi(phi(x)) = x | inline
-->
