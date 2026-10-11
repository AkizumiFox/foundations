# Partial Orders, Maximal and Greatest Elements

Section 7.5 studied the relations that behave like equality. This section studies the ones that behave like \( \le \): reflexive and transitive like an equivalence relation, but antisymmetric instead of symmetric, so that they have a direction. For numbers, "the largest element of a set" is clear. For sets under \( \subseteq \), or for natural numbers under divisibility, two elements can be **incomparable**, neither below the other, and "largest" splits into two different notions. We separate them, prove what links them, and then take a first look at least upper bounds. That is the vocabulary Chapter 11 needs for the supremum.

## Partial orders

Section 7.4 found three relations with the same three properties: \( \le \) on \( \nR \), \( \subseteq \) on \( \powerset{X} \) (@exm-relation-table), and \( \mid \) on \( \nN \) (@prp-divides-partial-order). Each is reflexive, antisymmetric and transitive. Each says "below" in its own sense: smaller, contained in, a divisor of. What they share is what "being below" needs, and it deserves a name, so that a fact proved once holds for all three.

*A partial order says which elements lie below which, without requiring every two to be comparable.*

::: {#def-partial-order}
[Partial Order]

Let \( X \) be a set. A **partial order on \( X \)** is a relation \( \preceq \) on \( X \) that is reflexive, antisymmetric and transitive on \( X \) (@def-relation-properties):

::: {.enumerate options="label=(PO\arabic*)"}
1. **for every** \( x \in X \), \( x \preceq x \);
2. **for all** \( x, y \in X \), if \( x \preceq y \) and \( y \preceq x \), then \( x = y \);
3. **for all** \( x, y, z \in X \), if \( x \preceq y \) and \( y \preceq z \), then \( x \preceq z \).
:::

The pair \( (X, \preceq) \) is a **partially ordered set**. Elements \( x, y \in X \) are **comparable** if \( x \preceq y \) or \( y \preceq x \). The partial order is **total** if **every** two elements of \( X \) are comparable. The **strict part** of \( \preceq \) is the relation \( \prec \) on \( X \) given by
\[
x \prec y \iff x \preceq y \ \text{ and } \ x \ne y .
\]
We also write \( y \succeq x \) for \( x \preceq y \).
:::

In words: (PO1) everything is below itself. (PO2) is the clause that gives an order its direction: two elements below each other are the same element, so "below" cannot run both ways between different things. (PO3) lets "below" pass along a chain. "Total" adds that any two elements can be compared; "partial" is the word for not requiring it. The symbol \( \preceq \) is a letter for an arbitrary partial order, chosen so that \( \le \) keeps its meaning on numbers.

The strict part is irreflexive and transitive. No \( x \) has \( x \prec x \), since that would need \( x \ne x \). If \( x \prec y \) and \( y \prec z \), then \( x \preceq z \) by (PO3); and \( x \ne z \), because \( x = z \) would give \( x \preceq y \) and \( y \preceq x \), hence \( x = y \) by (PO2), contradicting \( x \ne y \). So \( x \prec z \).

**Examples.**

- \( (\nR, \le) \) is a partially ordered set, and it is total: for real numbers \( x \le y \) or \( y \le x \). Its strict part is \( < \). The same holds for \( (\nN, \le) \) and \( (\nZ, \le) \), since restricting a total order to a subset keeps all four properties: each is a statement about all elements, and holds in particular for the elements of the subset.
- \( (\nN, \mid) \) is a partially ordered set by @prp-divides-partial-order, and it is not total: \( 2 \nmid 3 \) and \( 3 \nmid 2 \), so \( 2 \) and \( 3 \) are incomparable.
- \( (\powerset{X}, \subseteq) \) is a partially ordered set; the example after this list decides when it is total.
- Degenerate cases: equality on any set \( X \) is a partial order, in which no two **different** elements are comparable; and the empty relation is a partial order on \( \emptyset \), vacuously.

**Non-examples by minimal change.** Divisibility on \( \nZ \) is reflexive and transitive, but not antisymmetric: \( 2 \mid -2 \) and \( -2 \mid 2 \), and \( 2 \ne -2 \) (@prp-divides-partial-order). Passing from \( \nN \) to \( \nZ \) loses exactly (PO2). The relation \( < \) on \( \nR \) is antisymmetric (vacuously: \( x < y \) and \( y < x \) never both hold) and transitive, but not reflexive, since \( 0 < 0 \) fails. It is the strict part of \( \le \), not a partial order.

**Why these clauses.** Without (PO2), two different elements could each be below the other, and "the largest element" of a set could fail to be unique; the uniqueness proof in the next subsection uses (PO2) and nothing else. A relation that keeps (PO1) and (PO3) and drops (PO2) is often called a preorder; \( \mid \) on \( \nZ \) is one. Totality is left out because the important examples, \( \subseteq \) and \( \mid \), do not have it, and much of the interest lies in what changes without it.

::: {#exm-subset-order-not-total}
[Inclusion is a partial order, rarely total]

Let \( X \) be a set. Show that \( \subseteq \) is a partial order on \( \powerset{X} \), and that it is total if and only if \( X \) has at most one element.
:::

::: {.solution}
*A partial order.* (PO1) \( A \subseteq A \) for every set \( A \). (PO2) If \( A \subseteq B \) and \( B \subseteq A \), then \( A = B \) by @prp-subset-antisymmetric. (PO3) is @prp-subset-transitive. (These are the entries of @exm-relation-table.)

*Total exactly when \( X \) has at most one element.* Suppose \( X \) has two different elements \( a \ne b \). Then \( \{a\}, \{b\} \in \powerset{X} \), and \( \{a\} \not\subseteq \{b\} \), since \( a \in \{a\} \) and \( a \notin \{b\} \); likewise \( \{b\} \not\subseteq \{a\} \). So \( \{a\} \) and \( \{b\} \) are incomparable, and \( \subseteq \) is not total. For \( X = \{1, 2\} \), the incomparable pair is \( \{1\} \), \( \{2\} \).

Conversely, suppose any two elements of \( X \) are equal. Let \( A \subseteq X \). If \( A \ne \emptyset \), take \( a \in A \); then every \( x \in X \) equals \( a \), so \( x \in A \), and \( A = X \). So every subset of \( X \) is \( \emptyset \) or \( X \). Any two of these are comparable, since \( \emptyset \subseteq X \) (Section 6.1, after @prp-empty-set-unique) and each is a subset of itself. So \( \subseteq \) is total on \( \powerset{X} \).
:::

::: {.warning}
In a partial order, "\( x \preceq y \) fails" does **not** give "\( y \prec x \)". In \( (\powerset{\{1, 2\}}, \subseteq) \), \( \{1\} \not\subseteq \{2\} \), and \( \{2\} \subsetneq \{1\} \) is false too: the two are incomparable. The habit from numbers, "not \( \le \) means \( > \)", is the totality of \( \le \) on \( \nR \), and it must not be carried into a partial order.
:::

## Bounds, greatest and maximal elements

From now on, \( (X, \preceq) \) is a partially ordered set and \( A \subseteq X \). The bounds come first, because both kinds of "largest" are measured against them.

::: {#def-order-bounds}
[Upper and Lower Bounds]

An element \( u \in X \) is an **upper bound** of \( A \) if \( a \preceq u \) for every \( a \in A \), and a **lower bound** of \( A \) if \( u \preceq a \) for every \( a \in A \). The set \( A \) is **bounded above** if it has an upper bound in \( X \), **bounded below** if it has a lower bound in \( X \), and **bounded** if both.
:::

An upper bound lives in \( X \) and need not belong to \( A \): in \( (\nR, \le) \), \( 5 \) is an upper bound of \( [0, 1] \). Every element of \( X \) is an upper bound of \( \emptyset \), vacuously. In \( (\nN, \mid) \), an upper bound of \( \{4, 6\} \) is a common multiple of \( 4 \) and \( 6 \), such as \( 12 \), \( 24 \) or \( 0 \).

Now the two notions of "largest". The first is the familiar one: an element of the set that is above everything in the set. The second asks less: an element with nothing in the set strictly above it.

::: {#def-greatest-element}
[Greatest and Least Elements]

An element \( g \) is a **greatest element** of \( A \) if \( g \in A \) and \( a \preceq g \) for **every** \( a \in A \). An element \( l \) is a **least element** of \( A \) if \( l \in A \) and \( l \preceq a \) for every \( a \in A \).
:::

::: {#def-maximal-element}
[Maximal and Minimal Elements]

An element \( m \) is a **maximal element** of \( A \) if \( m \in A \) and there is **no** \( a \in A \) with \( m \prec a \). An element \( m \) is a **minimal element** of \( A \) if \( m \in A \) and there is no \( a \in A \) with \( a \prec m \).
:::

In words: a greatest element is an upper bound of \( A \) that belongs to \( A \). A maximal element is one that cannot be beaten inside \( A \), which is weaker: an element can be unbeaten simply because it is incomparable with its rivals. In symbols the difference is where the negation sits:
\[
\begin{aligned}
g \text{ greatest:} &\quad g \in A \wedge \forall a \in A \ \, a \preceq g , \\
m \text{ maximal:} &\quad m \in A \wedge \neg \exists a \in A \ \, m \prec a .
\end{aligned}
\]
By @prp-bounded-quantifier-negation (b), \( \neg \exists a \in A \ \, m \prec a \) is \( \forall a \in A \ \, \neg (m \prec a) \), and \( \neg (m \prec a) \) says that \( m \preceq a \) implies \( m = a \). So "maximal" reads: everything in \( A \) that is above \( m \) **is** \( m \). "Greatest" reads: everything in \( A \) is below \( g \). The first only forbids elements above; the second demands that every element be compared.

For numbers the two coincide. In \( (\nR, \le) \), the set \( \{1, 4, 9\} \) has greatest element \( 9 \), its only maximal element, and least element \( 1 \). The interval \( [0, 1) \) has least element \( 0 \) and neither a greatest nor a maximal element: for each \( a \in [0, 1) \), the number \( (a + 1)/2 \) lies in \( [0, 1) \) and is strictly above \( a \). A one-point set \( \{x\} \) has \( x \) as greatest, least, maximal and minimal element, and \( \emptyset \) has none of the four, since each definition requires an element of \( A \).

The first result explains the article in "**the** greatest element".

::: {#prp-greatest-unique}
[Greatest and Least Elements Are Unique]

A subset \( A \) of a partially ordered set has at most one greatest element and at most one least element.
:::

::: {.proof}
Let \( g \) and \( g' \) be greatest elements of \( A \). Since \( g' \in A \) and \( g \) is greatest, \( g' \preceq g \); since \( g \in A \) and \( g' \) is greatest, \( g \preceq g' \). By (PO2), \( g = g' \). For least elements the same argument applies with the inequalities reversed.
:::

So we may speak of **the** greatest element and **the** least element of \( A \) when they exist. In \( (\nR, \le) \), the greatest element of a set is its maximum, \( \max A \), and the least element its minimum, \( \min A \). This settles a point left open in Section 6.4: the least \( q_0 \in \nZ_{>0} \) with \( r q_0 \in \nZ \) in @exm-not-a-function exists by @thm-well-ordering: the set of such \( q \) lies in \( \nZ_{>0} \subseteq \nN \), and it is non-empty, since writing \( r = p/q \) with \( q \in \nZ_{>0} \) (as the solution of (b) there notes) gives \( rq = p \in \nZ \). It is unique by the least-element half of the proposition, so the rule there names one value.

The second result compares the two notions.

::: {#prp-greatest-maximal}
[Greatest and Maximal Elements]

Let \( (X, \preceq) \) be a partially ordered set and \( A \subseteq X \).

::: {.enumerate options="label=(\alph*)"}
1. A greatest element of \( A \) is a maximal element of \( A \).
2. If \( \preceq \) is total, then a maximal element of \( A \) is a greatest element of \( A \).
:::

The same holds for least and minimal elements.
:::

::: {.idea}
For (a), anything strictly above the greatest element would also be below it, and antisymmetry forbids that. For (b), a maximal element \( m \) must be compared with each \( a \in A \), and totality says it can be: either \( a \preceq m \), as wanted, or \( m \preceq a \), and then maximality forces \( a = m \).
:::

::: {.proof}
*(a)* Let \( g \) be a greatest element of \( A \). Then \( g \in A \). Suppose some \( a \in A \) has \( g \prec a \), so \( g \preceq a \) and \( g \ne a \). Since \( g \) is greatest, \( a \preceq g \). By (PO2), \( a = g \), contradicting \( g \ne a \). So no such \( a \) exists, and \( g \) is maximal.

*(b)* Let \( \preceq \) be total and \( m \) a maximal element of \( A \), and let \( a \in A \). By totality, \( a \preceq m \) or \( m \preceq a \). *Case 1:* \( a \preceq m \). This is what we want. *Case 2:* \( m \preceq a \). If \( m \ne a \), then \( m \prec a \) with \( a \in A \), which maximality excludes. So \( m = a \), and \( a \preceq m \) by (PO1). In either case \( a \preceq m \). Since \( a \in A \) was arbitrary and \( m \in A \), \( m \) is a greatest element.

For least and minimal elements, apply (a) and (b) to the partial order \( \succeq \): its greatest and maximal elements are the least and minimal elements for \( \preceq \), and it is total when \( \preceq \) is. (That \( \succeq \) satisfies (PO1)–(PO3), and is total when \( \preceq \) is, comes from reading those clauses with the two variables exchanged. Its strict part is \( x \succ y \iff y \prec x \), since \( x \ne y \) is symmetric in \( x \) and \( y \). So "no \( a \in A \) with \( m \succ a \)" is "no \( a \in A \) with \( a \prec m \)", and "\( a \succeq l \) for every \( a \in A \)" is "\( l \preceq a \) for every \( a \in A \)".)
:::

Part (b) uses totality once, in the case split of its second sentence, and the case split is where it fails without it. The proof of @prp-finite-max in Section 7.3 compares two elements at a time and keeps the larger. Its maximum half uses nothing about \( \le \) on \( \nR \) beyond reflexivity, transitivity and the comparability of any two elements, so it works word for word in any totally ordered set. The minimum half passes to \( -x_1, \dots, -x_n \), which needs an ordered field; in a totally ordered set, apply the maximum half to the reverse order \( \succeq \) instead, which is total by the last paragraph of the proof above. In particular the whole proposition holds in any ordered field, which is how Chapter 11 reads it.

Without totality, (b) fails, and maximal elements need not be greatest.

::: {#exm-maximal-not-greatest}
[Maximal elements that are not greatest]

Find the maximal elements of each set, and decide whether it has a greatest element: (a) \( A = \{2, 3, 4, 5, 6\} \) in \( (\nN, \mid) \); (b) \( \sB = \{ \{1\}, \{2\} \} \) in \( (\powerset{\{1, 2\}}, \subseteq) \).
:::

::: {.solution}
(a) Within \( A \), the only strict divisibilities are \( 2 \mid 4 \), \( 2 \mid 6 \) and \( 3 \mid 6 \). So \( 2 \prec 4 \) and \( 3 \prec 6 \), and \( 2 \), \( 3 \) are not maximal. Nothing in \( A \) is strictly above \( 4 \), \( 5 \) or \( 6 \): every element of \( A \) is positive, and a positive multiple \( k n \) of \( n \in \{4, 5, 6\} \) other than \( n \) has \( k > 0 \) and \( k \ne 1 \), so \( k \ge 2 \) (@prp-integers-closed (c)), and then \( k n \ge 2n \ge 8 \), while every element of \( A \) is at most \( 6 \). So the maximal elements are \( 4 \), \( 5 \) and \( 6 \).

There is no greatest element. By @prp-greatest-maximal (a), a greatest element would be maximal, so it would be \( 4 \), \( 5 \) or \( 6 \). But \( 5 \nmid 4 \), \( 4 \nmid 5 \) and \( 4 \nmid 6 \), so none of the three is above every element of \( A \).

(b) \( \{1\} \) and \( \{2\} \) are incomparable (@exm-subset-order-not-total), so neither is strictly above the other: both are maximal. Neither is greatest, since neither contains the other.
:::

In (a), the minimal elements are \( 2 \), \( 3 \) and \( 5 \), and there is no least element either. The example is the minimal change from \( \{1, 2, 3, 4, 5, 6\} \), which has the least element \( 1 \) and still no greatest.

::: {.warning}
"Maximal" is not "greatest". A set can have many maximal elements and no greatest, as in @exm-maximal-not-greatest; and a set can have no maximal element at all: \( \nN \) under \( \le \), where \( n + 1 \in \nN \) (by (\( \nN \)S)) is strictly above \( n \). The answer also depends on the order, not just on the set: under divisibility, \( \nN \) **has** a greatest element, \( 0 \), since every \( a \in \nN \) divides \( 0 = 0 \cdot a \).
:::

::: {.check}
In \( \powerset{\{1, 2, 3\}} \setminus \{ \{1, 2, 3\} \} \), ordered by \( \subseteq \), name the maximal elements. Is there a greatest element?
:::

::: {.solution}
The maximal elements are the three two-element sets \( \{1, 2\} \), \( \{1, 3\} \), \( \{2, 3\} \): the only subset of \( \{1, 2, 3\} \) strictly containing a two-element set is \( \{1, 2, 3\} \), which was removed, and every set with at most one element lies strictly inside some two-element set. There is no greatest element: it would be maximal (@prp-greatest-maximal (a)), hence a two-element set, and no two-element set contains the other two.
:::

## Least upper bounds, a first look

Here is the notion that the rest of the book is built on. When a set has no greatest element, its upper bounds may still have a least one, and that element plays the part of "the top of the set" from outside.

*The supremum is the best upper bound: the least element of the set of upper bounds.*

::: {#def-order-supremum}
[Supremum and Infimum]

Let \( (X, \preceq) \) be a partially ordered set and \( A \subseteq X \). An element \( s \in X \) is a **least upper bound**, or **supremum**, of \( A \) in \( X \) if

::: {.enumerate options="label=(S\arabic*)"}
1. \( s \) is an upper bound of \( A \), and
2. \( s \preceq u \) for **every** upper bound \( u \) of \( A \).
:::

An element \( i \in X \) is a **greatest lower bound**, or **infimum**, of \( A \) in \( X \) if \( i \) is a lower bound of \( A \) and \( u \preceq i \) for every lower bound \( u \) of \( A \).
:::

In other words, a supremum of \( A \) is a least element of the set of upper bounds of \( A \), and an infimum a greatest element of the set of lower bounds. By @prp-greatest-unique, applied to those sets, each is **unique** when it exists, and we write \( \sup A \) and \( \inf A \). The words "in \( X \)" matter: the upper bounds are taken in \( X \), and enlarging or shrinking \( X \) can create or destroy a supremum. The definition also carries no promise that \( \sup A \) exists, or that it belongs to \( A \).

Two quick consequences. If \( A \) has a greatest element \( g \), then \( g = \sup A \): \( g \) is an upper bound, and every upper bound \( u \) has \( g \preceq u \) because \( g \in A \). And a supremum that belongs to \( A \) is a greatest element of \( A \), by (S1). So a supremum is a greatest element exactly when it lies in the set; the new cases are the ones where it lies outside.

**Suprema of sets.** In \( (\powerset{X}, \subseteq) \), let \( A, B \subseteq X \). Then \( \sup \{A, B\} = A \cup B \). (S1): \( A \subseteq A \cup B \) and \( B \subseteq A \cup B \), and \( A \cup B \in \powerset{X} \). (S2): let \( C \in \powerset{X} \) be an upper bound, so \( A \subseteq C \) and \( B \subseteq C \); every element of \( A \cup B \) lies in \( A \) or in \( B \), hence in \( C \), so \( A \cup B \subseteq C \). The supremum \( A \cup B \) belongs to \( \{A, B\} \) only when one of the two sets contains the other; for \( \{ \{1\}, \{2\} \} \) it is \( \{1, 2\} \), which is not in the set. Exercise B1 extends this to every family of subsets, and adds the infimum.

**Suprema under divisibility.** In \( (\nN, \mid) \), an upper bound of \( \{a, b\} \) is a common multiple of \( a \) and \( b \). The least upper bound turns out to be the least common multiple, and proving that it is **least in the divisibility order**, not merely the smallest number, is a job for the division algorithm.

::: {#exm-divisibility-lcm}
[The supremum under divisibility is the least common multiple]

Let \( a, b \in \nN \). Find \( \sup \{a, b\} \) in \( (\nN, \mid) \). Deduce that an integer divisible by \( 2 \) and by \( 3 \) is divisible by \( 6 \).
:::

::: {.solution}
*Case \( a, b \in \nZ_{>0} \).* Let \( M \coloneqq \{ m \in \nZ_{>0} : a \mid m \text{ and } b \mid m \} \), the positive common multiples. It is non-empty: \( ab \in \nN \) by @lem-naturals-arithmetic (b), \( ab > 0 \) as a product of positive numbers, so \( ab \in \nZ_{>0} \) (@prp-integers-closed (b)), and \( ab = b \cdot a = a \cdot b \) is a multiple of both. Since \( M \subseteq \nZ_{>0} \subseteq \nN \), \( M \) has a least element \( L \) (@thm-well-ordering), the **least common multiple** of \( a \) and \( b \).

We show that \( L \) divides **every** integer common multiple \( c \) of \( a \) and \( b \). By @thm-division-algorithm, \( c = qL + r \) with \( q, r \in \nZ \) and \( 0 \le r < L \). Write \( c = as \), \( L = at \) with \( s, t \in \nZ \); then \( r = c - qL = a(s - qt) \) with \( s - qt \in \nZ \) (@prp-integers-closed (a)), so \( a \mid r \), and in the same way \( b \mid r \). If \( r > 0 \), then \( r \in \nZ_{>0} \) (@prp-integers-closed (b)), so \( r \in M \) and \( r < L \), contradicting the choice of \( L \). Hence \( r = 0 \), and \( c = qL \): \( L \mid c \). The argument never used \( c \ge 0 \).

Now \( L = \sup \{a, b\} \). (S1): \( a \mid L \) and \( b \mid L \), since \( L \in M \). (S2): an upper bound \( c \in \nN \) of \( \{a, b\} \) is a common multiple, so \( L \mid c \) by the previous paragraph.

*Case \( a = 0 \) or \( b = 0 \).* Say \( a = 0 \). An upper bound \( c \) has \( 0 \mid c \), that is, \( c = k \cdot 0 = 0 \) for some \( k \in \nZ \). And \( 0 \) is an upper bound, since \( n \mid 0 = 0 \cdot n \) for every \( n \in \nN \). So \( 0 \) is the only upper bound, and \( \sup \{a, b\} = 0 \), the greatest element of \( (\nN, \mid) \).

*The instance.* For \( a = 2 \), \( b = 3 \): \( 6 \in M \), and none of \( 1, 2, 3, 4, 5 \) is a multiple of both \( 2 \) and \( 3 \) (\( 1, 3, 5 \) are odd, and \( 2, 4 \) lie strictly between consecutive multiples of \( 3 \)). So \( L = 6 \), and every integer \( n \) with \( 2 \mid n \) and \( 3 \mid n \) has \( 6 \mid n \), by the second paragraph with \( c = n \).
:::

The instance proves the fact that Section 6.2 used as a school fact: an integer divisible by \( 2 \) and by \( 3 \) is divisible by \( 6 \). It also shows the two orders on \( \nN \) disagreeing: \( \sup \{4, 6\} \) is \( 12 \) under divisibility and \( 6 \) under \( \le \).

**A supremum that does not exist.** In \( (\nQ, \le) \), the set \( \{ x \in \nQ : x > 0, \ x^2 < 2 \} \) is non-empty and bounded above (by \( 2 \), for instance: a rational \( x > 2 \) has \( x^2 > 4 \)). It has **no** least upper bound in \( \nQ \). We do not prove this here. Chapter 11 proves it, and then takes the existence of suprema in \( \nR \) as its axiom: the supremum of Chapter 11, defined in an ordered field, is @def-order-supremum for the order \( \le \) of that field; Chapter 11 uses it in \( \nQ \) and in \( \nR \). The ambient set decides: the same set has a supremum in \( (\nR, \le) \), namely \( \sqrt 2 \).

## Well-ordered sets

Section 7.1 proved that every non-empty subset of \( \nN \) has a least element (@thm-well-ordering). In the language of this section, that is a property of the partially ordered set \( (\nN, \le) \), and it has a name.

::: {#def-well-ordered-set}
[Well-Ordered Set]

A partially ordered set \( (X, \preceq) \) is **well-ordered**, and \( \preceq \) is a **well-order** on \( X \), if \( \preceq \) is total and every **non-empty** subset of \( X \) has a least element.
:::

\( (\nN, \le) \) is well-ordered: \( \le \) is total, and @thm-well-ordering supplies the least elements. \( (\nZ, \le) \) is not: \( \nZ \) itself has no least element, since for every \( n \in \nZ \) also \( n - 1 \in \nZ \) (@prp-integers-closed (a)) and \( n - 1 < n \). Nor is the set of positive rationals, which has no least element (\( q/2 < q \)). The word "non-empty" is needed because \( \emptyset \) has no least element in any order. Totality is in fact automatic: any two elements \( x, y \) form a non-empty set \( \{x, y\} \), whose least element is below the other one. Upper bounds work too: in \( (\nN, \le) \) a non-empty set bounded above has a greatest element (@cor-well-ordering-integers). Exercise C1 gives a well-ordered set that does not look like \( \nN \).

::: {.remark}
In a general partially ordered set, one may ask: if every **chain** (a subset on which \( \preceq \) is total) has an upper bound, must there be a maximal element? For a non-empty partially ordered set the answer "yes" is Zorn's lemma, and it cannot be proved from what we have: it is equivalent to the axiom of choice, which Chapter 8 states. Chapter 67 proves Zorn's lemma from the axiom of choice, and Chapter 9 lists the other statements equivalent to choice, among them the claim that every set has a well-order.
:::

## Exercises

### A. Check your understanding

::: {#exr-orders-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Let \( (X, \preceq) \) be a partially ordered set and \( A \subseteq X \). Write "\( g \) is a greatest element of \( A \)" and "\( m \) is a maximal element of \( A \)" in symbols, and negate each.
2. True or false, with a witness: every finite non-empty subset of a partially ordered set has a greatest element.
3. Find \( \sup \{4, 6\} \) in \( (\nN, \mid) \) and in \( (\nN, \le) \).
4. On \( \nN \times \nN \), the **lexicographic order** is \( (a, b) \preceq (c, d) \) if \( a < c \), or \( a = c \) and \( b \le d \). Given that it is a partial order, is it total?
:::
:::

::: {.solution}
(a) \( g \) greatest: \( g \in A \wedge \forall a \in A \ \, a \preceq g \). Its negation, by @prp-de-morgan and @prp-bounded-quantifier-negation (a): \( g \notin A \vee \exists a \in A \ \, \neg (a \preceq g) \).

\( m \) maximal: \( m \in A \wedge \neg \exists a \in A \ \, m \prec a \). Its negation: \( m \notin A \vee \exists a \in A \ \, m \prec a \), by @prp-de-morgan and @prp-double-negation. In words: \( g \) fails to be greatest if some element of \( A \) is **not below** it; \( m \) fails to be maximal if some element of \( A \) is **strictly above** it. The first failure can happen through incomparability; the second cannot.

(b) False. In \( (\powerset{\{1, 2\}}, \subseteq) \), the set \( \{ \{1\}, \{2\} \} \) is finite and non-empty and has no greatest element (@exm-maximal-not-greatest (b)). What is true is that it has a **maximal** element: listed as \( \{x_1, \dots, x_n\} \), which is what "finite" will mean in Chapter 8, it has one by Exercise R4.

(c) Under divisibility, \( \sup \{4, 6\} = 12 \), the least common multiple (@exm-divisibility-lcm): \( 12 \) is a common multiple, and none of \( 1, \dots, 11 \) is (the multiples of \( 6 \) below \( 12 \) are \( 6 \), and \( 4 \nmid 6 \)). Under \( \le \), \( \sup \{4, 6\} = 6 \), the greatest element.

(d) Yes. Let \( (a, b), (c, d) \in \nN \times \nN \). If \( a < c \), then \( (a, b) \preceq (c, d) \); if \( c < a \), then \( (c, d) \preceq (a, b) \); if \( a = c \), then \( b \le d \) or \( d \le b \), by totality of \( \le \), and the pairs are comparable. By trichotomy these cases cover everything.
:::

### B. Practice

::: {#exr-orders-b1}
[B1: Suprema of families of sets]

Let \( X \) be a set and \( (A_i)_{i \in I} \) a family of subsets of \( X \). In \( (\powerset{X}, \subseteq) \), prove that the set \( \{ A_i : i \in I \} \) has supremum \( \bigcup_{i \in I} A_i \) and infimum \( \bigcap_{i \in I} A_i \), the intersection taken in \( X \). What are they when \( I = \emptyset \)?
:::

::: {.solution}
Write \( U \coloneqq \bigcup_{i \in I} A_i \) and \( N \coloneqq \bigcap_{i \in I} A_i \) (@def-family-union-intersection). Both are subsets of \( X \), so they lie in \( \powerset{X} \).

*Supremum.* (S1) For each \( i \in I \), every element of \( A_i \) lies in \( U \), so \( A_i \subseteq U \). (S2) Let \( C \in \powerset{X} \) be an upper bound: \( A_i \subseteq C \) for every \( i \in I \). Let \( x \in U \). Then \( x \in A_i \) for some \( i \in I \); name it \( i \). Since \( A_i \subseteq C \), \( x \in C \). So \( U \subseteq C \).

*Infimum.* \( N \) is a lower bound: for each \( i \in I \), every \( x \in N \) lies in \( A_i \), so \( N \subseteq A_i \). Let \( D \in \powerset{X} \) be a lower bound: \( D \subseteq A_i \) for every \( i \). Let \( x \in D \). Then \( x \in X \), and \( x \in A_i \) for every \( i \in I \), so \( x \in N \). Hence \( D \subseteq N \).

*Empty index set.* If \( I = \emptyset \), then \( U = \emptyset \) and \( N = X \), since an intersection in \( X \) of no sets is \( X \). This agrees with the definitions: every element of \( \powerset{X} \) is an upper bound of the empty set, and the least of them is \( \emptyset \); every element is a lower bound, and the greatest is \( X \). The arguments above cover this case, since their "for every \( i \)" clauses hold vacuously.
:::

::: {#exr-orders-b2}
[B2: Two maximal elements and a least one]

Give an example of a partially ordered set that has exactly two maximal elements and a least element, and check each property. Then list the properties that every answer must have.
:::

::: {.solution}
*An example.* \( X = \{ \emptyset, \{1\}, \{2\} \} \) ordered by \( \subseteq \). It is a partial order, as a subset of \( (\powerset{\{1, 2\}}, \subseteq) \). The least element is \( \emptyset \), since \( \emptyset \subseteq A \) for every \( A \in X \) (Section 6.1, after @prp-empty-set-unique). The maximal elements are \( \{1\} \) and \( \{2\} \): neither is strictly contained in an element of \( X \). And \( \emptyset \) is not maximal, since \( \emptyset \subsetneq \{1\} \). So there are exactly two. Another answer: \( \{1, 2, 3\} \) under divisibility, with least element \( 1 \) and maximal elements \( 2 \), \( 3 \).

*What every answer must have.* Let \( l \) be the least element and \( m_1 \ne m_2 \) the maximal elements.

- \( m_1 \) and \( m_2 \) are incomparable: if \( m_1 \preceq m_2 \), then \( m_1 \prec m_2 \), since \( m_1 \ne m_2 \), and \( m_1 \) would not be maximal; symmetrically for \( m_2 \preceq m_1 \).
- So the order is not total, and there is no greatest element: a greatest element \( g \) would have \( m_1 \preceq g \), and maximality of \( m_1 \) gives \( m_1 = g \); likewise \( m_2 = g \), contradicting \( m_1 \ne m_2 \).
- \( l \), \( m_1 \), \( m_2 \) are three different elements: if \( l = m_1 \), then \( m_1 = l \preceq m_2 \), which the first point excludes; likewise \( l \ne m_2 \).

So an answer has at least three elements and two incomparable maximal ones above a common least element. A candidate failing any of these is not an answer.
:::

::: {#exr-orders-b3}
[B3: Minimal is least in a total order]

Let \( (X, \preceq) \) be a totally ordered set and \( A \subseteq X \). Prove that a minimal element of \( A \) is a least element of \( A \), by applying @prp-greatest-maximal (b) to the reverse order \( \succeq \). Check each fact about \( \succeq \) that you use.
:::

::: {.solution}
*The reverse order.* \( \succeq \) is the relation \( x \succeq y \iff y \preceq x \). (PO1): \( x \preceq x \), so \( x \succeq x \). (PO2): if \( x \succeq y \) and \( y \succeq x \), then \( y \preceq x \) and \( x \preceq y \), so \( x = y \). (PO3): if \( x \succeq y \) and \( y \succeq z \), then \( z \preceq y \) and \( y \preceq x \), so \( z \preceq x \), that is, \( x \succeq z \). Totality: for \( x, y \in X \), \( x \preceq y \) or \( y \preceq x \), that is, \( y \succeq x \) or \( x \succeq y \). Its strict part is \( x \succ y \iff y \prec x \), since \( x \ne y \) is symmetric in \( x, y \).

*Translating.* In the order \( \succeq \), "\( x \) lies below \( y \)" is written \( x \succeq y \), and "strictly below" is \( x \succ y \). Now \( m \) is minimal for \( \preceq \): \( m \in A \) and no \( a \in A \) has \( a \prec m \), that is, no \( a \in A \) has \( m \succ a \). That is exactly "\( m \) is maximal for \( \succeq \)". Likewise "\( l \) is greatest for \( \succeq \)" says \( l \in A \) and \( a \succeq l \) for every \( a \in A \), that is, \( l \preceq a \) for every \( a \in A \): "\( l \) is least for \( \preceq \)".

*Conclusion.* Let \( m \) be minimal in \( A \) for \( \preceq \). Then \( m \) is maximal in \( A \) for the total order \( \succeq \), so it is greatest for \( \succeq \) by @prp-greatest-maximal (b), hence least for \( \preceq \).
:::

### C. Going deeper

::: {#exr-orders-c1}
[C1: A well-order that is not like N]

Let \( \preceq \) be the lexicographic order on \( \nN \times \nN \) of Exercise A1 (d).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \preceq \) is a partial order.
2. Prove that \( (\nN \times \nN, \preceq) \) is well-ordered.
3. Show that \( (1, n) \prec (2, 1) \) for every \( n \in \nN \), and that these elements \( (1, n) \) are pairwise different. In \( (\nN, \le) \), which elements lie strictly below a given \( k \in \nN \)?
:::
:::

::: {.solution}
(a) (PO1) \( a = a \) and \( b \le b \), so \( (a, b) \preceq (a, b) \). (PO2) Let \( (a, b) \preceq (c, d) \) and \( (c, d) \preceq (a, b) \). If \( a < c \), the second relation needs \( c < a \) or \( c = a \), both impossible; likewise \( c < a \) is impossible. So \( a = c \) by trichotomy, and then \( b \le d \) and \( d \le b \) give \( b = d \). (PO3) Let \( (a, b) \preceq (c, d) \preceq (e, f) \). If \( a < c \) or \( c < e \), then \( a < e \), since in each case the other comparison is \( \le \); so \( (a, b) \preceq (e, f) \). Otherwise \( a = c = e \) and \( b \le d \le f \), so again \( (a, b) \preceq (e, f) \).

(b) Totality is A1 (d). Let \( S \subseteq \nN \times \nN \) be non-empty. The set \( F \coloneqq \{ a \in \nN : (a, b) \in S \text{ for some } b \in \nN \} \) of first coordinates is non-empty, so it has a least element \( a_0 \) (@thm-well-ordering). The set \( G \coloneqq \{ b \in \nN : (a_0, b) \in S \} \) is non-empty, since \( a_0 \in F \), so it has a least element \( b_0 \). Then \( (a_0, b_0) \in S \). Let \( (a, b) \in S \). Then \( a \in F \), so \( a_0 \le a \). If \( a_0 < a \), then \( (a_0, b_0) \preceq (a, b) \). If \( a_0 = a \), then \( b \in G \), so \( b_0 \le b \), and again \( (a_0, b_0) \preceq (a, b) \). So \( (a_0, b_0) \) is the least element of \( S \).

(c) For \( n \in \nN \), \( 1 < 2 \) gives \( (1, n) \preceq (2, 1) \), and \( (1, n) \ne (2, 1) \) since \( 1 \ne 2 \); so \( (1, n) \prec (2, 1) \). For \( n \ne n' \), \( (1, n) \ne (1, n') \) by the characteristic property of pairs. So one element, \( (2, 1) \), has an element \( (1, n) \) strictly below it for each of the natural numbers \( n \), all different. In \( (\nN, \le) \), the elements strictly below \( k \) are exactly \( 0, 1, \dots, k - 1 \) (none when \( k = 0 \)), by @lem-naturals-arithmetic (a) and (e): they form a list ending at \( k - 1 \). So a well-ordered set need not look like \( \nN \): here one element has a strictly smaller element for every natural number.
:::

::: {#exr-orders-c2}
[C2: Infima and suprema under divisibility]

Work in \( (\nN, \mid) \). Let \( a, b \in \nN \), not both \( 0 \), and let \( d \) be the least element of
\[
D \coloneqq \{ ka + lb : k, l \in \nZ \} \cap \nZ_{>0} .
\]

::: {.enumerate options="label=(\alph*)"}
1. Explain why \( d \) exists.
2. Prove that \( d \mid a \) and \( d \mid b \).
3. Prove that every common divisor \( c \in \nN \) of \( a \) and \( b \) divides \( d \), and conclude that \( d = \inf \{a, b\} \).
4. Decide whether every non-empty subset of \( \nN \) has a supremum in \( (\nN, \mid) \). Then decide the same question for \( (\nZ_{>0}, \mid) \).
:::
:::

::: {.solution}
[Hint 1]

For (b), apply the division algorithm to \( a \) and \( d \).
:::

::: {.solution}
[Hint 2]

Write \( a = qd + r \) with \( 0 \le r < d \), and write \( d = k_0 a + l_0 b \).
:::

::: {.solution}
(a) \( D \subseteq \nZ_{>0} \subseteq \nN \). It is non-empty: if \( a \ne 0 \), then \( a = 1 \cdot a + 0 \cdot b \) and \( a \in \nZ_{>0} \), so \( a \in D \); otherwise \( b \ne 0 \) and \( b \in D \) likewise. So \( D \) has a least element by @thm-well-ordering, unique by @prp-greatest-unique.

(b) Write \( d = k_0 a + l_0 b \) with \( k_0, l_0 \in \nZ \). Since \( d \in \nZ_{>0} \), @thm-division-algorithm gives \( a = qd + r \) with \( q, r \in \nZ \) and \( 0 \le r < d \). Then
\[
r = a - qd = (1 - q k_0) a + (-q l_0) b ,
\]
with integer coefficients (@prp-integers-closed (a)). If \( r > 0 \), then \( r \in \nZ_{>0} \), so \( r \in D \) and \( r < d \), contradicting the choice of \( d \). Hence \( r = 0 \), and \( a = qd \): \( d \mid a \). The same argument with \( b \) in place of \( a \) gives \( d \mid b \).

(c) Let \( c \in \nN \) with \( c \mid a \) and \( c \mid b \): \( a = cs \), \( b = ct \) with \( s, t \in \nZ \). Then \( d = k_0 cs + l_0 ct = c (k_0 s + l_0 t) \), so \( c \mid d \). In \( (\nN, \mid) \), the lower bounds of \( \{a, b\} \) are the common divisors in \( \nN \). By (b), \( d \) is one; by (c), every lower bound \( c \) has \( c \mid d \). So \( d \) is the greatest lower bound: \( d = \inf \{a, b\} \).

(d) *In \( (\nN, \mid) \): yes.* Let \( T \subseteq \nN \) be non-empty. An upper bound of \( T \) is a common multiple \( c \in \nN \) of all elements of \( T \), and \( 0 \) is one, since \( t \mid 0 = 0 \cdot t \) for every \( t \).

*Case 1: \( T \) has a positive common multiple.* The positive common multiples form a non-empty subset of \( \nN \), so they have a least element \( L \) (@thm-well-ordering). It is an upper bound. Let \( c \in \nN \) be any upper bound. By @thm-division-algorithm, \( c = qL + r \) with \( 0 \le r < L \). For each \( t \in T \), \( t \mid c \) and \( t \mid L \), so \( t \mid r = c - qL \) (as in @exm-divisibility-lcm). If \( r > 0 \), then \( r \) is a positive common multiple smaller than \( L \), which is impossible. So \( r = 0 \) and \( L \mid c \). Hence \( \sup T = L \). This is the argument of @exm-divisibility-lcm, which never used that the set had two elements.

*Case 2: \( T \) has no positive common multiple.* Then \( 0 \) is its only upper bound, and \( \sup T = 0 \), the least element of \( \{0\} \). This case includes every \( T \) containing \( 0 \), since \( 0 \mid c \) forces \( c = 0 \).

*In \( (\nZ_{>0}, \mid) \): no.* (It is a partial order, as the restriction of one.) Take \( T = \nZ_{>0} \). An upper bound would be some \( c \in \nZ_{>0} \) with \( t \mid c \) for every \( t \in \nZ_{>0} \), in particular \( (c + 1) \mid c \): \( c = k(c + 1) \) with \( k \in \nZ \). Since \( c > 0 \) and \( c + 1 > 0 \), \( k > 0 \) (if \( k \le 0 \), then \( k(c + 1) \le 0 \)), so \( k \ge 1 \) (@prp-integers-closed (b)), and \( c = k(c + 1) \ge c + 1 \), which is impossible. So \( T \) has no upper bound in \( \nZ_{>0} \), and no supremum. Removing \( 0 \) removed the element that bounded everything.

**Marking scheme.** (10 points)

- 1: (a) \( D \) is non-empty (exhibits \( a \) or \( b \) in it) and \( D \subseteq \nN \), so well-ordering applies.
- 3: (b) the division algorithm with divisor \( d \ge 1 \); the remainder is again of the form \( ka + lb \); minimality of \( d \) forces \( r = 0 \).
- 2: (c) a common divisor divides \( d \), and the conclusion \( d = \inf \{a, b\} \) checks both clauses of an infimum.
- 3: (d) for \( \nN \): \( 0 \) is always an upper bound; with a positive common multiple, the least one divides every upper bound (division algorithm again); without one, the supremum is \( 0 \).
- 1: (d) for \( \nZ_{>0} \): a set with no upper bound, with proof.

Fatal errors (0 for the step): concluding \( d \mid a \) from \( d \le a \); in (d), taking the numerically smallest upper bound and not checking that it **divides** every upper bound; treating \( \inf \) as the minimum under \( \le \).
:::

### R. Review

::: {#exr-orders-r1}
[R1]

Let \( f \colon \nR \to \nR \), \( f(x) = x^2 + 4x \). Compute \( f([-3, 1]) \) and \( f^{-1}([-3, 0]) \). Then compute \( f(\nR) \), and check that \( f(f^{-1}([-5, 0])) = [-5, 0] \cap f(\nR) \) by computing both sides.
:::

::: {.solution}
Complete the square: \( f(x) = (x + 2)^2 - 4 \). We use, as school facts, that squares are non-negative and that every \( y \ge 0 \) has a square root \( \sqrt y \ge 0 \), and, by @thm-squares-order, that for \( s, t \ge 0 \), \( s \le t \) exactly when \( s^2 \le t^2 \).

*\( f([-3, 1]) = [-4, 5] \).* \( (\subseteq) \) If \( -3 \le x \le 1 \), then \( -1 \le x + 2 \le 3 \), so \( \abs{x + 2} \le 3 \), \( 0 \le (x + 2)^2 \le 9 \), and \( -4 \le f(x) \le 5 \). \( (\supseteq) \) For \( -4 \le y \le 5 \), take \( x \coloneqq -2 + \sqrt{y + 4} \). Then \( 0 \le \sqrt{y + 4} \le 3 \), so \( x \in [-2, 1] \subseteq [-3, 1] \), and \( f(x) = (y + 4) - 4 = y \).

*\( f^{-1}([-3, 0]) = [-4, -3] \cup [-1, 0] \).* For \( x \in \nR \): \( -3 \le f(x) \le 0 \iff 1 \le (x + 2)^2 \le 4 \iff 1 \le \abs{x + 2} \le 2 \), and splitting by the sign of \( x + 2 \), this holds exactly when \( x + 2 \in [-2, -1] \cup [1, 2] \), that is, \( x \in [-4, -3] \cup [-1, 0] \).

*\( f(\nR) = [-4, \infty) \),* by the argument for \( f([-3, 1]) \): \( f(x) \ge -4 \) always, and \( y \ge -4 \) is \( f(-2 + \sqrt{y + 4}) \).

*The check.* \( f^{-1}([-5, 0]) = \{ x : (x + 2)^2 \le 4 \} = [-4, 0] \), since \( (x + 2)^2 - 4 \ge -4 > -5 \) always. Then \( f([-4, 0]) = [-4, 0] \), by the first computation's method (\( x + 2 \in [-2, 2] \), so \( (x + 2)^2 \in [0, 4] \), and each value is attained). On the other side, \( [-5, 0] \cap [-4, \infty) = [-4, 0] \). Both sides are \( [-4, 0] \), as @prp-image-preimage (b) predicts: the round trip removes exactly the part \( [-5, -4) \) of \( [-5, 0] \) that \( f \) never reaches.
:::

::: {#exr-orders-r2}
[R2]

Write in symbols, with bounded quantifiers, the statement "every element of \( A \) has an element of \( A \) strictly above it", for a set \( A \subseteq \nR \) ordered by \( \le \). Write its negation with no \( \neg \) in front of a quantifier, and decide which of the two holds for \( A = \nN \) and for \( A = \{1, \dots, 5\} \).
:::

::: {.solution}
The statement is \( \forall a \in A \ \exists b \in A \ \, a < b \). By @prp-bounded-quantifier-negation (a) and then (b), its negation is
\[
\exists a \in A \ \forall b \in A \ \, \neg (a < b) ,
\]
and since \( \le \) is total on \( \nR \), \( \neg (a < b) \) is \( b \le a \): the negation is \( \exists a \in A \ \forall b \in A \ \, b \le a \), "\( A \) has a greatest element". Passing the \( \neg \) through the quantifiers turns each \( \forall \) into \( \exists \) and each \( \exists \) into \( \forall \), and leaves the bounds \( a \in A \), \( b \in A \) untouched; negating the bound instead is entry (N11) of @exm-not-allowed-catalogue.

For \( A = \nN \) the statement holds: for \( a \in \nN \), \( b \coloneqq a + 1 \in \nN \) by (\( \nN \)S), and \( a < a + 1 \). For \( A = \{1, \dots, 5\} \) the negation holds, with \( a = 5 \): every \( b \in A \) has \( b \le 5 \).
:::

::: {#exr-orders-r3}
[R3]

Call a formula **biconditional** if it is built from atoms using \( \leftrightarrow \) alone: each atom is biconditional, and if \( \varphi \) and \( \psi \) are biconditional, so is \( (\varphi \leftrightarrow \psi) \); nothing else is. Prove that every biconditional formula is true under the valuation that makes every atom true.
:::

::: {.solution}
Let \( v_{\mathrm{T}} \) be the all-T valuation. We use @thm-structural-induction with the property
\[
P(\varphi): \ \text{if } \varphi \text{ is biconditional, then } v_{\mathrm{T}}(\varphi) = \mathrm{T} .
\]
The formulas \( \bot \), \( \neg\varphi \) and \( (\varphi \circ \psi) \) with \( \circ \) one of \( \wedge, \vee, \to \) are not biconditional, so \( P \) holds for them vacuously, and the corresponding clauses of the theorem need nothing more.

(i) For an atom \( p \), \( v_{\mathrm{T}}(p) = \mathrm{T} \) by the choice of \( v_{\mathrm{T}} \).

(iii) for \( \circ = \leftrightarrow \): suppose \( P(\varphi) \) and \( P(\psi) \), and that \( (\varphi \leftrightarrow \psi) \) is biconditional. Then \( \varphi \) and \( \psi \) are biconditional: by unique readability (@thm-unique-readability), they are the only immediate parts, and a biconditional formula that is not an atom is built by the second clause from biconditional parts. So \( v_{\mathrm{T}}(\varphi) = \mathrm{T} = v_{\mathrm{T}}(\psi) \), and by (V6) of @def-truth-value, \( v_{\mathrm{T}}(\varphi \leftrightarrow \psi) = \mathrm{T} \), since the two parts have the same value.

This covers every clause, and proves the claim. In particular no biconditional formula is equivalent to \( \neg p \), which is false under \( v_{\mathrm{T}} \): negation cannot be expressed with \( \leftrightarrow \) alone.
:::

::: {#exr-orders-r4}
[R4]

Let \( (X, \preceq) \) be a partially ordered set, let \( n \ge 1 \) be an integer, and let \( x_1, \dots, x_n \in X \). Show that the set \( \{x_1, \dots, x_n\} \) has a maximal element.
:::

::: {.solution}
*The tool* is induction from base \( 1 \) (@thm-induction with \( n_0 = 1 \)), in the shape of @prp-finite-max: add one element at a time and keep track of a maximal element. Let \( P(n) \) say: for all \( x_1, \dots, x_n \in X \), the set \( \{x_1, \dots, x_n\} \) has a maximal element.

*Base.* \( \{x_1\} \): no element \( a \) of it has \( x_1 \prec a \), since the only candidate is \( x_1 \) and \( x_1 \prec x_1 \) never holds. So \( x_1 \) is maximal.

*Step.* Let \( n \ge 1 \), assume \( P(n) \), and let \( x_1, \dots, x_{n+1} \in X \). Put \( A \coloneqq \{x_1, \dots, x_n\} \) and \( A' \coloneqq \{x_1, \dots, x_{n+1}\} \), where, as in Section 7.3, \( \{x_1, \dots, x_n\} \coloneqq \{ x_k : k \in \{1, \dots, n\} \} \), now for elements of \( X \). Since \( \{1, \dots, n + 1\} = \{1, \dots, n\} \cup \{n + 1\} \) (@lem-naturals-arithmetic (e), as in the proof of @prp-finite-max), \( A' = A \cup \{x_{n+1}\} \). By \( P(n) \), \( A \) has a maximal element \( m \).

*Case 1:* \( m \prec x_{n+1} \) fails. Then \( m \) is maximal in \( A' \): \( m \in A' \); no \( a \in A \) has \( m \prec a \), by maximality in \( A \); and \( a = x_{n+1} \) is excluded by the case.

*Case 2:* \( m \prec x_{n+1} \). Then \( x_{n+1} \) is maximal in \( A' \). Suppose \( x_{n+1} \prec a \) with \( a \in A' \). Then \( a \ne x_{n+1} \), so \( a \in A \); and \( m \prec x_{n+1} \prec a \) gives \( m \prec a \), since the strict part of a partial order is transitive. This contradicts the maximality of \( m \) in \( A \).

In either case \( A' \) has a maximal element, so \( P(n + 1) \) holds, and @thm-induction gives \( P(n) \) for every \( n \ge 1 \).

*The look-alikes.* "Take the greatest element" fails, because a finite set need not have one (@exm-maximal-not-greatest). "Take the largest, as in @prp-finite-max" fails for the same reason: that proof keeps the larger of \( M \) and \( x_{n+1} \), which needs the two to be comparable; here Case 1 covers incomparable elements by keeping \( m \). "Take \( x_n \), the last one" confuses the order of the list with the order \( \preceq \): nothing makes \( x_n \) large.
:::

<!-- dependency ledger
def-partial-order (claim): strict part irreflexive and transitive | inline (the paragraph after the definition)
def-partial-order (claim): (examples) <= on R is a total order; restricting to N, Z keeps the properties | R order, school fact; axioms in Chapter 11
def-partial-order (claim): (examples) 2 does not divide 3 and 3 does not divide 2 | arithmetic (division algorithm remainders 1 and 2); thm-division-algorithm uniqueness
exm-subset-order-not-total (solution): A subset of A | def-subset (Ch 6 Section 6.1), used silently
def-greatest-element (claim): (a + 1)/2 in [0, 1) and above a | R arithmetic and order, school fact
prp-greatest-maximal (proof): the reverse order is a partial order, total when the order is; its strict part is the reverse of the strict part; maximal/greatest for the reverse order = minimal/least for the order | inline in the proof; written out in full in exr-orders-b3
prp-greatest-maximal (claim): (after it) the maximum half of the proof of prp-finite-max uses only reflexivity, transitivity and comparability; the minimum half via the reverse order (negation needs an ordered field) | prp-finite-max (Section 7.3; meta-claim about its proof, checked against the blueprint's route "base {x1}, step max{M, x_(n+1)}"); the reverse order as in the proof of prp-greatest-maximal
prp-greatest-unique (claim): (after it) some q in Z_{>0} has rq in Z | exm-not-a-function (Ch 6 Section 6.4, solution of (b), clause (Fn1))
prp-greatest-maximal (claim): Chapter 11 reads prp-finite-max in an ordered field | Ch 11 (prose pointer)
exm-maximal-not-greatest (solution): kn > 0 and n > 0 give k > 0; k >= 2 gives kn >= 2n; 5 does not divide 4 etc. | R order, school fact; axioms in Chapter 11; prp-integers-closed (c) (cited); arithmetic; verify/ch07/exm-maximal-not-greatest.py
exm-maximal-not-greatest (claim): (warning after it) n + 1 in N and n < n + 1 | (NS) (Section 7.1, cited); R arithmetic
exm-divisibility-lcm (solution): a(s - qt) = as - qat | R arithmetic
exm-divisibility-lcm (solution): product of positive reals is positive; ab = ba | R arithmetic and order, school fact; axioms in Chapter 11
exm-divisibility-lcm (solution): 1..5 contain no common multiple of 2 and 3 | arithmetic; verify/ch07/exm-divisibility-lcm.py
exm-divisibility-lcm (claim): {x in Q : x > 0, x^2 < 2} non-empty (1) and bounded above by 2; no rational supremum; sqrt 2 its supremum in R | R order (school fact) for the bound; Ch 11 (prose pointer; nothing here depends on it)
def-well-ordered-set (claim): positive rationals: q/2 < q | R arithmetic
def-well-ordered-set (claim): (remark) Zorn's lemma, axiom of choice, well-ordering theorem | Ch 8, Ch 67, Ch 9 (prose pointers; nothing depends on them)
def-well-ordered-set (claim): N bounded above has a greatest element | cor-well-ordering-integers (cited; N subset of Z)
exr-orders-a1 (solution): multiples of 6 below 12; 4 does not divide 6 | arithmetic; verify/ch07/exr-orders-a1.py
exr-orders-a1 (solution): finite set -> list x_1, ..., x_n | Ch 8 (prose pointer; Chapter 8's definition of finite)
exr-orders-a1 (solution): trichotomy and totality of <= on N | R order, school fact; axioms in Chapter 11
exr-orders-c1 (solution): trichotomy; a < c <= e gives a < e; characteristic property of pairs | R order; def-ordered-pair (Ch 6 Section 6.3)
exr-orders-c2 (solution): k <= 0 and c + 1 > 0 give k(c + 1) <= 0; k >= 1 and c + 1 > 0 give k(c + 1) >= c + 1 | R order, school fact; axioms in Chapter 11
exr-orders-c2 (solution): 0 | c means c = k * 0 = 0 | R arithmetic
exr-orders-r2 (solution): a + 1 in N | (NS) (Section 7.1, cited); R arithmetic for a < a + 1
exr-orders-r1 (solution): square roots; completing the square; sign cases of |x + 2| | school facts (Part 0 convention); square roots proved in Chapter 11; thm-squares-order (cited); verify/ch07/exr-orders-r1.py
exr-orders-r4 (solution): strict part transitive | inline in the text after def-partial-order
exr-orders-r4 (solution): {x_1, ..., x_n} for elements of any set; {x_1..x_(n+1)} = {x_1..x_n} u {x_(n+1)} | notation of Section 7.3 (before prp-finite-max), extended; lem-naturals-arithmetic (e) (cited), as in prp-finite-max
-->
