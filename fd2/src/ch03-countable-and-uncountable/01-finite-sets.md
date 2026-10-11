# Equinumerous Sets and Finite Sets

Chapter 6 made functions exact and sorted them into injective, surjective and bijective ones. Chapter 7 put the natural numbers on firm ground: their arithmetic, well-ordering, induction from any base and definition by recursion. This chapter asks how large a set is. For a finite set we count. For \( \nN \), \( \nQ \) or \( \nR \) counting gives no answer, and the question "are there more rational numbers than natural numbers?" needs a meaning before it can have an answer. This section gives "the same size" its meaning, a pairing, and then proves the facts about finite sets on which counting rests, starting with the pigeonhole principle.

## Same size without counting

So far we have compared functions; now we compare sets. The everyday word is "as many as", and we can check it without knowing any numbers. Put two piles of coins on a table, and take one coin from each pile at a time, setting the two aside as a pair. If both piles run out at the same moment, they had the same number of coins. We know this before counting either pile, and a child who cannot count past ten can do it with piles of a thousand.

The pairing is a function from the first pile to the second. Different coins are paired with different coins, so it is injective; every coin of the second pile is used, so it is surjective. Pairing makes sense for any two sets, finite or not, and that is the definition.

*Same size means there is a pairing.*

::: {#def-equinumerous}
[Equinumerous Sets]

Let \( A \) and \( B \) be sets. We say that \( A \) and \( B \) are **equinumerous**, and write \( \card{A} = \card{B} \), if **there exists** a bijection \( f \colon A \to B \). In symbols,
\[
\card{A} = \card{B} \iff \exists f \in B^A \ \ (f \text{ is injective} \wedge f \text{ is surjective}) .
\]
:::

In words: the definition asks for **one** bijection, and it does not care which. Injectivity says that no two elements of \( A \) are paired with the same element of \( B \); surjectivity says that no element of \( B \) is left over. The statement \( \card{A} = \card{B} \) is read as a whole, "\( A \) and \( B \) are equinumerous". It is a relation between two sets. We do not define an object \( \card{A} \), "the size of \( A \)", standing alone, and a remark below explains why the obvious candidate is not available. For finite sets, the definition of a finite set below gives \( \card{A} \) a meaning as a natural number, and the two uses agree.

Here are four examples, the degenerate one first.

- *The empty set.* The empty function \( \emptyset \to \emptyset \) of @prp-empty-function (a) is injective and surjective, vacuously: there are no two inputs to compare and no output to reach. So \( \card{\emptyset} = \card{\emptyset} \). Conversely, if \( \card{A} = \card{\emptyset} \), there is a function \( A \to \emptyset \), so \( A = \emptyset \) by @prp-empty-function (b). The empty set is equinumerous with itself and with nothing else. This case is the test case for every statement below about sets "with \( n \) elements", at \( n = 0 \).
- *Three letters and three numbers.* Let \( a, b, c \) be three different letters. The function \( \{a, b, c\} \to \{1, 2, 3\} \) with \( a \mapsto 1 \), \( b \mapsto 2 \), \( c \mapsto 3 \) sends different letters to different numbers and reaches each of \( 1, 2, 3 \). So \( \card{\{a, b, c\}} = \card{\{1, 2, 3\}} \).
- *Two intervals of different lengths.* The function \( f \colon [0, 1] \to [0, 2] \), \( f(x) = 2x \), has the inverse \( y \mapsto y/2 \), since \( y/2 \in [0, 1] \) for \( y \in [0, 2] \), \( f(y/2) = y \) and \( f(x)/2 = x \). By @thm-bijection-iff-inverse it is a bijection, so \( \card{[0, 1]} = \card{[0, 2]} \). Length and size are different things.
- *The natural numbers and the positive integers.* The function \( \nN \to \nZ_{>0} \), \( n \mapsto n + 1 \), is a bijection. It is the Quick check near the end of this section, where it shows that \( \nN \) is infinite.

**A non-example by a minimal change.** Shrink \( \{1, 2, 3\} \) to \( \{1, 2\} \). There is no bijection \( \{a, b, c\} \to \{1, 2\} \). Let \( g \) be any function \( \{a, b, c\} \to \{1, 2\} \). If \( g(a) = g(b) \), then \( g \) is not injective. Otherwise \( g(a) \) and \( g(b) \) are \( 1 \) and \( 2 \) in some order, and \( g(c) \), which is \( 1 \) or \( 2 \), equals one of them. In every case two different letters share a value. So the clause that fails is injectivity, and it fails for **every** function, which is what "not equinumerous" requires. Surjectivity can hold: \( a \mapsto 1 \), \( b \mapsto 2 \), \( c \mapsto 2 \) reaches both numbers.

::: {.warning}
To show that two sets are **not** equinumerous, one map is never enough. The map \( x \mapsto x \) from \( [0, 1] \) to \( [0, 2] \) is not surjective, since \( 2 \) is not a value, and yet \( \card{[0, 1]} = \card{[0, 2]} \) by the map \( x \mapsto 2x \) above. "Not equinumerous" is a statement about **all** functions, \( \forall f \in B^A \, \neg(f \text{ bijective}) \), and a proof of it must deal with an arbitrary \( f \), as the non-example did.
:::

**Why this definition.** To count a set is to pair it with \( \{1, \dots, n\} \): saying "one, two, three" while pointing at the coins is a bijection from \( \{1, 2, 3\} \) onto the pile. So the definition does not replace counting; it isolates the part of counting that still makes sense when the set is infinite. Each clause has a job. Without injectivity, the surjection \( \{1, 2, 3\} \to \{1\} \) would make a three-element set as large as a one-element set. Without surjectivity, the inclusion \( \{1\} \to \{1, 2, 3\} \) would do the same in the other direction.

The first result says that equinumerosity behaves like an equivalence relation.

::: {#prp-equinumerous-properties}
[Equinumerosity Is Reflexive, Symmetric and Transitive]

For all sets \( A \), \( B \) and \( C \):

::: {.enumerate options="label=(\alph*)"}
1. \( \card{A} = \card{A} \);
2. if \( \card{A} = \card{B} \), then \( \card{B} = \card{A} \);
3. if \( \card{A} = \card{B} \) and \( \card{B} = \card{C} \), then \( \card{A} = \card{C} \).
:::
:::

::: {.proof}
*(a)* The identity \( \id_A \) is injective, since \( \id_A(x) = \id_A(y) \) says \( x = y \), and surjective, since every \( x \in A \) is \( \id_A(x) \).

*(b)* Let \( f \colon A \to B \) be a bijection. By @thm-bijection-iff-inverse it has a two-sided inverse \( f^{-1} \colon B \to A \), with \( f^{-1} \circ f = \id_A \) and \( f \circ f^{-1} = \id_B \). Read with the roles exchanged, these two equations say that \( f \) is a two-sided inverse of \( f^{-1} \) (@def-inverse-function). So \( f^{-1} \) is a bijection \( B \to A \), by @thm-bijection-iff-inverse again.

*(c)* If \( f \colon A \to B \) and \( g \colon B \to C \) are bijections, then \( g \circ f \colon A \to C \) is a bijection by @thm-composition-injective-surjective (c). This proves the proposition.
:::

Clauses (a)–(c) have the form of (Eq1)–(Eq3) of @def-equivalence-relation, and yet we do not call equinumerosity an equivalence relation. An equivalence relation in Chapter 7 is a relation **on a set** \( X \), a subset of \( X \times X \). Equinumerosity relates any two sets whatever, and there is no set of all sets for it to live on (@thm-russell). That is also why the book reserves the symbol \( \sim \) for equivalence relations and writes \( \card{A} = \card{B} \) here.

::: {.remark}
Why not define \( \card{A} \) as "the collection of all sets equinumerous with \( A \)"? Because that collection is in general not a set. The next paragraph proves this for \( A = \{0\} \).
:::

Take \( A = \{0\} \). Every singleton \( \{x\} \) is equinumerous with \( \{0\} \), by \( 0 \mapsto x \). If the singletons formed a set \( \sS \), its union \( \bigcup \sS \) would be a set by (W3) of Section 6.1, and every object \( x \) would be an element of it, since \( x \in \{x\} \in \sS \). That is a set of which every set is an element, which @thm-russell rules out.

## Finite sets

Counting is pairing with \( \{1, \dots, n\} \), so "finite" is defined by such a pairing. Recall from Section 7.1 that for \( n \in \nN \),
\[
\{1, \dots, n\} \coloneqq \{ k \in \nN : 1 \le k \le n \} ,
\]
so that \( \{1, \dots, 0\} = \emptyset \), since no \( k \) has \( 1 \le k \le 0 \).

::: {#def-finite}
[Finite Set, Number of Elements]

Let \( A \) be a set and \( n \in \nN \). We say that \( A \) **has \( n \) elements** if \( \card{\{1, \dots, n\}} = \card{A} \), that is, if **there exists** a bijection \( \varphi \colon \{1, \dots, n\} \to A \). The set \( A \) is **finite** if it has \( n \) elements for **some** \( n \in \nN \). In that case we write \( \card{A} = n \).
:::

In words: \( \varphi \) numbers the elements of \( A \) as \( \varphi(1), \varphi(2), \dots, \varphi(n) \). Injectivity says that no element gets two numbers; surjectivity says that every element gets one. So a non-empty finite set is \( A = \{\varphi(1), \dots, \varphi(n)\} \), a list without repetitions. By @prp-equinumerous-properties (b), "\( A \) has \( n \) elements" is the same as \( \card{A} = \card{\{1, \dots, n\}} \), so the notation \( \card{A} = n \) is consistent with the relation of @def-equinumerous.

There is a gap in the notation \( \card{A} = n \). It presents \( n \) as **the** number of elements, but the definition only says that **some** \( n \) works. Could a set have \( 3 \) elements and also \( 4 \)? It cannot, and a corollary of the pigeonhole principle below proves it. That corollary is the well-definedness step this definition needs. Until it is proved, read \( \card{A} = n \) as "\( A \) has \( n \) elements".

Examples:

- The empty set has \( 0 \) elements: \( \{1, \dots, 0\} = \emptyset \), and the empty function \( \emptyset \to \emptyset \) is a bijection. Conversely, a set with \( 0 \) elements is empty, since a bijection \( \emptyset \to A \) is surjective and has no values.
- \( \{1, \dots, n\} \) has \( n \) elements, by \( \id_{\{1, \dots, n\}} \).
- For \( n \in \nN \), \( \{0, \dots, n\} \) has \( n + 1 \) elements: \( k \mapsto k - 1 \) maps \( \{1, \dots, n + 1\} \) to \( \{0, \dots, n\} \), because \( k - 1 \in \nN \) for \( k \ne 0 \) (@lem-naturals-arithmetic (c)) and \( k - 1 \le n \). It has the inverse \( j \mapsto j + 1 \), so it is a bijection (@thm-bijection-iff-inverse).
- The three-letter set \( \{a, b, c\} \) has \( 3 \) elements, by the inverse of the bijection of the second example after @def-equinumerous.

::: {#def-infinite}
[Infinite Set]

A set \( A \) is **infinite** if it is not finite: **for every** \( n \in \nN \) there is **no** bijection \( \{1, \dots, n\} \to A \).
:::

To prove a set infinite we must rule out every \( n \) at once, and for every \( n \) every candidate bijection. Nothing so far does that, not even for \( \nN \). The tool is the pigeonhole principle, and the last theorem of this section turns it into a usable test.

**Shrinking the codomain.** One small device is used throughout the chapter. Let \( f \colon X \to Y \) be a function, and let \( C \subseteq Y \) contain every value \( f(x) \). The graph of \( f \) is then a subset of \( X \times C \), and with the codomain \( C \) it is a function \( X \to C \) with the same values (@def-function). We call it "\( f \) with codomain \( C \)". It is injective if and only if \( f \) is, since injectivity speaks only of values. In particular, \( f \) with codomain \( f(X) \) is surjective (@def-image). So an **injective** \( f \colon X \to Y \) is a bijection \( X \to f(X) \) once its codomain is shrunk, and \( \card{X} = \card{f(X)} \).

## The pigeonhole principle

If more pigeons than holes fly into a dovecote, some hole gets two pigeons. In Chapter 6 we found one function from a three-element set to a two-element set that is not injective (@exm-injective-surjective-first (c)), and observed without proof that none can be. Here is the general fact, for the standard sets \( \{1, \dots, m\} \) and \( \{1, \dots, n\} \).

::: {#thm-pigeonhole}
[Pigeonhole Principle]

Let \( m, n \in \nN \) with \( m > n \). Then there is **no** injection \( \{1, \dots, m\} \to \{1, \dots, n\} \).
:::

::: {.idea}
Induct on the number \( n \) of holes. In the step there are \( n + 1 \) holes, and we look at the last one. If no pigeon sits in hole \( n + 1 \), all the pigeons sit in \( n \) holes, and the hypothesis applies at once. If pigeon \( j \) sits there, there is only one, by injectivity. Move pigeon \( j \) to the hole of pigeon \( m \), and send pigeon \( m \) away. That leaves \( m - 1 \) pigeons in \( n \) holes, still one to a hole, and \( m - 1 > n \). The hypothesis is used at \( m - 1 \), not at \( m \), so the property we induct on must say "for every \( m \)". *Before reading on: self-explain the construction of the injection \( g \) in Case 2: why are its values in \( \{1, \dots, n\} \), and why is it injective?*
:::

::: {.proof}
For \( n \in \nN \) let \( P(n) \) be the statement

> for every \( m \in \nN \) with \( m > n \), there is no injection \( \{1, \dots, m\} \to \{1, \dots, n\} \).

We prove \( P(n) \) for every \( n \in \nN \) by @ax-induction.

*Base case \( P(0) \).* Let \( m \in \nN \) with \( m > 0 \). Then \( m \ge 1 \) (@lem-naturals-arithmetic (a)), so \( 1 \in \{1, \dots, m\} \) and the domain is non-empty, while \( \{1, \dots, 0\} = \emptyset \). By @prp-empty-function (b) there is no function \( \{1, \dots, m\} \to \emptyset \) at all, so there is no injection.

*Inductive step.* Let \( n \in \nN \) and suppose \( P(n) \). Let \( m \in \nN \) with \( m > n + 1 \), and suppose, for a contradiction, that \( f \colon \{1, \dots, m\} \to \{1, \dots, n + 1\} \) is injective. There are two cases.

*Case 1: \( n + 1 \) is not a value of \( f \).* For every \( i \), \( f(i) \le n + 1 \) and \( f(i) \ne n + 1 \), so \( f(i) < n + 1 \), and \( f(i) \le n \) by @lem-naturals-arithmetic (e). So \( f \) with codomain \( \{1, \dots, n\} \) is an injection \( \{1, \dots, m\} \to \{1, \dots, n\} \), with \( m > n + 1 > n \). This contradicts \( P(n) \).

*Case 2: \( f(j) = n + 1 \) for some \( j \in \{1, \dots, m\} \).* Since \( m > n + 1 \ge 1 \), we have \( m \ne 0 \), so \( m - 1 \in \nN \) by @lem-naturals-arithmetic (c); and \( m - 1 > n \), by subtracting \( 1 \) from \( m > n + 1 \). Define \( \sigma \colon \{1, \dots, m - 1\} \to \{1, \dots, m\} \) by
\[
\sigma(i) \coloneqq
\begin{cases}
i & \text{if } i \ne j , \\
m & \text{if } i = j .
\end{cases}
\]
(The second line applies only when \( j \le m - 1 \); if \( j = m \), then \( \sigma(i) = i \) for every \( i \).) The map \( \sigma \) is injective: two different inputs other than \( j \) keep their different values, and if one input is \( j \), its value is \( m \), while the other has value \( i \le m - 1 < m \). Moreover \( \sigma(i) \ne j \) for every \( i \): either \( \sigma(i) = i \ne j \), or \( \sigma(i) = m \), which happens only when \( j \le m - 1 < m \).

Let \( g \coloneqq f \circ \sigma \). It is injective by @thm-composition-injective-surjective (a). For every \( i \), \( \sigma(i) \ne j \), and \( f \) is injective with \( f(j) = n + 1 \), so \( g(i) = f(\sigma(i)) \ne n + 1 \); as in Case 1, \( g(i) \in \{1, \dots, n\} \). So \( g \) with codomain \( \{1, \dots, n\} \) is an injection \( \{1, \dots, m - 1\} \to \{1, \dots, n\} \), with \( m - 1 > n \). This contradicts \( P(n) \), applied to the number \( m - 1 \).

In both cases the injection \( f \) cannot exist, so \( P(n + 1) \) holds. By @ax-induction, \( P(n) \) holds for every \( n \in \nN \). This proves the theorem.
:::

The theorem is about the standard sets only, but bijections carry it to any finite sets. Part (b) below is its mirror image for surjections.

::: {#cor-pigeonhole-finite-sets}
[Pigeonhole for Finite Sets]

Let \( m, n \in \nN \), let \( A \) have \( m \) elements, and let \( B \) have \( n \) elements.

::: {.enumerate options="label=(\alph*)"}
1. If \( m > n \), there is no injection \( A \to B \).
2. If \( m < n \), there is no surjection \( A \to B \).
:::
:::

::: {.idea}
For (a), the bijections of @def-finite turn an injection \( A \to B \) into an injection \( \{1, \dots, m\} \to \{1, \dots, n\} \), which @thm-pigeonhole forbids. For (b), a surjection \( g \colon A \to B \) has a right inverse \( h \), and \( h \) is an injection \( B \to A \), forbidden by (a). The right inverse is built by a rule: send \( b \) to the element of \( A \) with the **smallest** number among those that \( g \) sends to \( b \).
:::

::: {.proof}
Let \( \varphi \colon \{1, \dots, m\} \to A \) and \( \psi \colon \{1, \dots, n\} \to B \) be bijections (@def-finite). By @thm-bijection-iff-inverse, \( \psi \) has an inverse \( \psi^{-1} \colon B \to \{1, \dots, n\} \), which is a bijection: the equations \( \psi^{-1} \circ \psi = \id \) and \( \psi \circ \psi^{-1} = \id \) say that \( \psi \) is a two-sided inverse of \( \psi^{-1} \) (@def-inverse-function), so @thm-bijection-iff-inverse applies.

*(a)* Suppose \( m > n \) and \( f \colon A \to B \) is injective. Then \( \psi^{-1} \circ f \circ \varphi \colon \{1, \dots, m\} \to \{1, \dots, n\} \) is injective by @thm-composition-injective-surjective (a), which contradicts @thm-pigeonhole.

*(b)* Suppose \( m < n \) and \( g \colon A \to B \) is surjective. For \( b \in B \) let
\[
S_b \coloneqq \{ i \in \{1, \dots, m\} : g(\varphi(i)) = b \} .
\]
It is non-empty: since \( g \) is onto, \( b = g(a) \) for some \( a \in A \), and \( a = \varphi(i) \) for some \( i \), since \( \varphi \) is onto. By @thm-well-ordering, \( S_b \) has a least element. Define \( h \colon B \to A \) by \( h(b) \coloneqq \varphi(\min S_b) \). Then \( g(h(b)) = b \) for every \( b \in B \), because \( \min S_b \in S_b \). So \( g \circ h = \id_B \): the function \( g \) is a left inverse of \( h \), and \( h \) is injective by @thm-left-inverse-iff-injective (a). Now \( h \) is an injection from the \( n \)-element set \( B \) to the \( m \)-element set \( A \), with \( n > m \), which contradicts (a). This proves the corollary.
:::

The function \( h \) in (b) is defined by a **rule**, "the least element", applied to each \( b \) at once, so its existence needs nothing beyond specification. Section 8.3 meets surjections for which no such rule is available, and there the book adds a new principle.

Two special cases settle earlier loose ends. With \( m = n + 1 \), part (a) says that a set with \( n \) elements has no \( n + 1 \) different elements: there is no injection \( \{1, \dots, n + 1\} \to A \). That is the second school fact that @exr-models-c2 took on trust. With \( m = 3 \), \( n = 2 \) in (a) and \( m = 2 \), \( n = 3 \) in (b), the corollary gives the two observations after @exm-injective-surjective-first in general.

Here is a typical use of (a). Among any three integers, two have an even sum. Let \( A \) be a set of three integers, and let \( p \colon A \to \{0, 1\} \) send each \( a \) to its remainder \( r \) on division by \( 2 \) (@thm-division-algorithm), an integer with \( 0 \le r < 2 \); then \( r \in \nN \) by @prp-integers-closed (b), and \( r \le 1 \) by @lem-naturals-arithmetic (e), so \( r \in \{0, 1\} \). The set \( \{0, 1\} \) has \( 2 \) elements, so by (a), \( p \) is not injective: there are \( a \ne b \) in \( A \) with the same remainder \( r \). Writing \( a = 2q + r \) and \( b = 2q' + r \),
\[
a + b = 2(q + q' + r) ,
\]
which is even, since \( q + q' + r \in \nZ \) (@prp-integers-closed (a)). The pigeons are the integers and the holes are the remainders; the whole skill is choosing the holes.

The next corollary is the well-definedness promised after @def-finite.

::: {#cor-finite-size-unique}
[The Number of Elements Is Unique]

Let \( A \) be a set and \( m, n \in \nN \). If \( A \) has \( m \) elements and \( A \) has \( n \) elements, then \( m = n \).
:::

::: {.proof}
Let \( \varphi \colon \{1, \dots, m\} \to A \) and \( \psi \colon \{1, \dots, n\} \to A \) be bijections. If \( m > n \), then \( \psi^{-1} \circ \varphi \colon \{1, \dots, m\} \to \{1, \dots, n\} \) is injective (@thm-bijection-iff-inverse, @thm-composition-injective-surjective (a)), which contradicts @thm-pigeonhole. Exchanging the roles of \( \varphi \) and \( \psi \) rules out \( m < n \) in the same way. By trichotomy, \( m = n \).
:::

So a finite set has exactly one number of elements, and from now on \( \card{A} = n \) means "**the** number of elements of \( A \) is \( n \)".

## Subsets and unions of finite sets

Three facts about finite sets are used everywhere below: the sizes of disjoint sets add, a subset is no larger than the whole, and removing one point lowers the size by one. The first uses nothing else from this section, so it comes first.

::: {#prp-disjoint-union-count}
[Disjoint Unions]

Let \( m, n \in \nN \), let \( A \) have \( m \) elements, let \( B \) have \( n \) elements, and suppose \( A \cap B = \emptyset \). Then \( A \cup B \) has \( m + n \) elements.
:::

::: {.idea}
Number \( A \) with \( 1, \dots, m \) and then carry on numbering \( B \) with \( m + 1, \dots, m + n \): shift the numbering of \( B \) up by \( m \).
:::

::: {.proof}
Let \( \varphi \colon \{1, \dots, m\} \to A \) and \( \psi \colon \{1, \dots, n\} \to B \) be bijections. Note \( m + n \in \nN \) by @lem-naturals-arithmetic (b). For \( k \in \{1, \dots, m + n\} \) with \( k > m \), we have \( m + 1 \le k \) by @lem-naturals-arithmetic (e), so \( k - m \in \nN \) with \( 1 \le k - m \le n \) (@lem-naturals-arithmetic (d)). So we may define \( \chi \colon \{1, \dots, m + n\} \to A \cup B \) by
\[
\chi(k) \coloneqq
\begin{cases}
\varphi(k) & \text{if } k \le m , \\
\psi(k - m) & \text{if } k > m .
\end{cases}
\]

*Injective.* Let \( \chi(k) = \chi(k') \). If \( k, k' \le m \), then \( \varphi(k) = \varphi(k') \) gives \( k = k' \). If \( k, k' > m \), then \( \psi(k - m) = \psi(k' - m) \) gives \( k - m = k' - m \), so \( k = k' \). If \( k \le m < k' \), then \( \chi(k) \in A \) and \( \chi(k') \in B \), and \( A \cap B = \emptyset \), so \( \chi(k) \ne \chi(k') \): this case cannot occur, nor can its mirror image.

*Surjective.* Let \( x \in A \cup B \). If \( x \in A \), then \( x = \varphi(i) \) with \( 1 \le i \le m \), and \( \chi(i) = x \). If \( x \in B \), then \( x = \psi(j) \) with \( 1 \le j \le n \); put \( k \coloneqq m + j \), so \( m < k \le m + n \), and \( \chi(k) = \psi(j) = x \).

So \( \chi \) is a bijection, and \( A \cup B \) has \( m + n \) elements.
:::

Now subsets. The proof is an induction on the size of the whole set, and it must be set up with care: the step peels off one element, and the obvious way to say "peel off one element" is the corollary after it, on removing a point. But that corollary is proved **from** this proposition. So the step peels off \( \varphi(n + 1) \) by restricting the bijection \( \varphi \) directly, and cites nothing proved later.

::: {#prp-subset-finite}
[Subsets of Finite Sets]

Let \( n \in \nN \), let \( A \) have \( n \) elements, and let \( S \subseteq A \). Then \( S \) is finite and has \( k \) elements for some \( k \le n \). If \( S \ne A \), then \( k < n \).
:::

::: {.idea}
Remove the last element \( \varphi(n + 1) \) from \( A \). Either it is outside \( S \), and \( S \) sits inside the smaller set; or it is in \( S \), and \( S \) is its part in the smaller set plus one point, which @prp-disjoint-union-count counts.
:::

::: {.proof}
For \( n \in \nN \) let \( P(n) \) be the statement

> for every set \( A \) with \( n \) elements and every \( S \subseteq A \), the set \( S \) has \( k \) elements for some \( k \le n \), and \( k < n \) if \( S \ne A \).

We prove \( P(n) \) for every \( n \) by @ax-induction.

*Base case \( P(0) \).* A set \( A \) with \( 0 \) elements is empty, so \( S \subseteq \emptyset \) gives \( S = \emptyset = A \), which has \( 0 \le 0 \) elements; the second clause is vacuous.

*Inductive step.* Let \( n \in \nN \) and suppose \( P(n) \). Let \( A \) have \( n + 1 \) elements, with a bijection \( \varphi \colon \{1, \dots, n + 1\} \to A \), and let \( S \subseteq A \). Put
\[
A' \coloneqq \varphi(\{1, \dots, n\}) , \qquad a \coloneqq \varphi(n + 1) .
\]
The restriction of \( \varphi \) to \( \{1, \dots, n\} \), with codomain \( A' \), is injective and surjective, so \( A' \) has \( n \) elements. Every element of \( A \) is \( \varphi(i) \) with \( i \le n \) or \( i = n + 1 \) (@lem-naturals-arithmetic (e)), so \( A = A' \cup \{a\} \). And \( a \notin A' \): if \( a = \varphi(i) \) with \( i \le n \), injectivity would give \( i = n + 1 \).

*Case \( a \notin S \).* Then \( S \subseteq A' \), and \( P(n) \), applied to \( A' \) and \( S \), shows that \( S \) has \( k \le n < n + 1 \) elements. In this case \( S \ne A \), since \( a \in A \setminus S \), and indeed \( k < n + 1 \), as required.

*Case \( a \in S \).* Then \( S = (S \cap A') \cup \{a\} \), and the union is disjoint because \( a \notin A' \). By \( P(n) \), applied to \( A' \) and \( S \cap A' \subseteq A' \), the set \( S \cap A' \) has \( j \) elements for some \( j \le n \). The set \( \{a\} \) has \( 1 \) element (by \( 1 \mapsto a \)). By @prp-disjoint-union-count, \( S \) has \( j + 1 \le n + 1 \) elements. If \( S \ne A \), then \( S \cap A' \ne A' \), since otherwise \( S = A' \cup \{a\} = A \); so \( j < n \) by \( P(n) \), and \( j + 1 < n + 1 \).

In both cases \( P(n + 1) \) holds. By @ax-induction, \( P(n) \) holds for every \( n \in \nN \). This proves the proposition.
:::

Read contrapositively, with @cor-finite-size-unique: a subset of an \( n \)-element set that itself has \( n \) elements is the whole set. (If \( S \ne A \), its number of elements is \( k < n \), and by uniqueness it is not \( n \).) That is the first school fact that @exr-models-c1 took on trust.

::: {#cor-remove-point}
[Removing a Point]

Let \( n \in \nN \), let \( A \) have \( n + 1 \) elements, and let \( a \in A \). Then \( A \setminus \{a\} \) has \( n \) elements.
:::

::: {.proof}
Since \( a \in A \), the set \( A \setminus \{a\} \) is a proper subset of \( A \), so by @prp-subset-finite it has \( k \) elements for some \( k < n + 1 \). Now \( A = (A \setminus \{a\}) \cup \{a\} \) is a disjoint union, and \( \{a\} \) has \( 1 \) element, so \( A \) has \( k + 1 \) elements by @prp-disjoint-union-count. By @cor-finite-size-unique, \( k + 1 = n + 1 \), so \( k = n \).
:::

Every later induction on the number of elements uses this corollary in the same way: its step starts from an **arbitrary** set \( A \) with \( n + 1 \) elements, picks some \( a \in A \) (there is one, since \( n + 1 \ge 1 \)), and applies the hypothesis to \( A \setminus \{a\} \), which has \( n \) elements. It never presents the set as "\( X \) with one point added" from the outset, which would prove the claim only for sets that come in that form. Here is the first such induction. Chapter 6 promised the count of subsets of a finite set.

::: {#prp-power-set-count}
[Counting Subsets]

Let \( n \in \nN \). A set with \( n \) elements has \( 2^n \) subsets: if \( \card{A} = n \), then \( \card{\powerset{A}} = 2^n \).
:::

::: {.idea}
Fix one element \( a \). Every subset either leaves \( a \) out or contains it, and adding \( a \) pairs the subsets of the first kind with those of the second. So the count doubles with each new element.
:::

::: {.proof}
We use @ax-induction on \( n \). *Base case.* A set with \( 0 \) elements is \( \emptyset \), and \( \powerset{\emptyset} = \{\emptyset\} \) has \( 1 = 2^0 \) element (@def-power).

*Inductive step.* Let \( n \in \nN \), and suppose every set with \( n \) elements has \( 2^n \) subsets. Let \( A \) have \( n + 1 \) elements, pick \( a \in A \), and put \( X \coloneqq A \setminus \{a\} \). By @cor-remove-point, \( X \) has \( n \) elements, so \( \powerset{X} \) has \( 2^n \) elements by the hypothesis (here \( 2^n \in \nN \) by @prp-power-laws (d), so the count makes sense; likewise \( 2^{n+1} \in \nN \)). Let
\[
T \coloneqq \{ S \cup \{a\} : S \in \powerset{X} \} ,
\]
the image of \( \powerset{X} \) under \( S \mapsto S \cup \{a\} \), a function \( \powerset{X} \to \powerset{A} \).

*\( \powerset{A} \) is the disjoint union of \( \powerset{X} \) and \( T \).* Every member of \( T \) contains \( a \), and no member of \( \powerset{X} \) does, since \( a \notin X \); so the union is disjoint. Both sets consist of subsets of \( A \). Conversely, let \( U \subseteq A \). If \( a \notin U \), then \( U \subseteq X \). If \( a \in U \), then \( U = (U \setminus \{a\}) \cup \{a\} \) with \( U \setminus \{a\} \subseteq X \), so \( U \in T \).

*\( T \) has \( 2^n \) elements.* The map \( S \mapsto S \cup \{a\} \), with codomain \( T \), is surjective by the definition of \( T \). It is injective: for \( S \subseteq X \) we have \( a \notin S \), so \( (S \cup \{a\}) \setminus \{a\} = S \), and \( S \) can be read back from \( S \cup \{a\} \). So it is a bijection \( \powerset{X} \to T \), and composing a bijection \( \{1, \dots, 2^n\} \to \powerset{X} \) with it (@thm-composition-injective-surjective (c)) shows that \( T \) has \( 2^n \) elements.

By @prp-disjoint-union-count, \( \powerset{A} \) has \( 2^n + 2^n = 2^n \cdot 2 = 2^{n+1} \) elements (@def-power). By @ax-induction, the claim holds for every \( n \in \nN \).
:::

For any set \( Y \), the map \( S \mapsto \ind_S \), with inverse \( f \mapsto \{ y \in Y : f(y) = 1 \} \), is a bijection \( \powerset{Y} \to \{0, 1\}^Y \) onto the set of functions \( Y \to \{0, 1\} \) (the correspondence of Section 6.4 between subsets and indicator functions). Taking \( Y \) with \( n \) elements, a set with \( n \) elements also has exactly \( 2^n \) functions to \( \{0, 1\} \), and the two counting problems of Chapter 6 are one. Exercise C2 counts all functions between finite sets.

## No finite set is equinumerous with a proper subset

For finite sets, "a proper part is smaller" is a theorem.

::: {#thm-finite-no-proper-copy}
[A Finite Set Has No Proper Copy]

Let \( A \) be a finite set and \( B \subsetneq A \). Then \( A \) and \( B \) are not equinumerous: there is no bijection \( A \to B \).
:::

::: {.proof}
Let \( A \) have \( n \) elements, with a bijection \( \varphi \colon \{1, \dots, n\} \to A \). By @prp-subset-finite, \( B \) has \( k \) elements for some \( k < n \), since \( B \ne A \). Suppose \( g \colon A \to B \) were a bijection. Then \( g \circ \varphi \colon \{1, \dots, n\} \to B \) is a bijection (@thm-composition-injective-surjective (c)), so \( B \) also has \( n \) elements, and @cor-finite-size-unique gives \( k = n \). This contradicts \( k < n \).
:::

Turned around, the theorem is a test for infinity: **a set that is equinumerous with a proper subset of itself is infinite.** Here is its first use. For the even natural numbers we write
\[
2\nN \coloneqq \{ 2n : n \in \nN \} ,
\]
the image of \( \nN \) under \( n \mapsto 2n \).

::: {#exm-hilbert-hotel}
[Hilbert's Hotel]

A hotel has one room for every natural number, and every room is taken. A coach arrives with guests for the odd-numbered rooms: the guest in room \( n \) is asked to move to room \( 2n \). Show that this is a bijection \( \nN \to 2\nN \), that \( 2\nN \) is a proper subset of \( \nN \), and deduce that \( \nN \) is infinite.
:::

::: {.solution}
Let \( d \colon \nN \to 2\nN \), \( d(n) \coloneqq 2n \). Its values lie in \( 2\nN \) by definition, and \( 2\nN \subseteq \nN \) by @lem-naturals-arithmetic (b). It is injective, since \( 2n = 2n' \) gives \( n = n' \), and surjective, since every element of \( 2\nN \) is \( 2n = d(n) \) for some \( n \in \nN \). So \( \card{\nN} = \card{2\nN} \).

The inclusion is proper because \( 1 \notin 2\nN \): if \( n = 0 \), then \( 2n = 0 \); if \( n \ne 0 \), then \( n \ge 1 \) (@lem-naturals-arithmetic (a)) and \( 2n \ge 2 \). So \( 2n \ne 1 \) for every \( n \in \nN \).

If \( \nN \) were finite, @thm-finite-no-proper-copy would forbid a bijection from \( \nN \) onto its proper subset \( 2\nN \). So \( \nN \) is infinite. Every guest still has a room, and the odd rooms are now free.
:::

The finite intuition "a proper part is smaller" fails for \( \nN \), and it fails exactly because \( \nN \) is infinite. Section 8.6 proves that it fails for **every** infinite set.

::: {.warning}
\( A \subsetneq B \) does not make \( A \) smaller than \( B \) when \( B \) is infinite: \( 2\nN \subsetneq \nN \) and \( \card{2\nN} = \card{\nN} \). Equinumerous is not "one is a subset of the other", in either direction.
:::

::: {.warning}
"Finite" does not mean "bounded". The set \( E \coloneqq \{ 1/n : n \in \nZ_{>0} \} \) lies in \( [0, 1] \), and it is infinite: \( x \mapsto x/(1 + x) \) sends \( 1/n \) to \( 1/(n + 1) \), and it is a bijection from \( E \) onto \( \{ 1/n : n \ge 2 \} \), with inverse \( y \mapsto y/(1 - y) \). That set is a proper subset of \( E \), since \( 1 \in E \) and \( 1/n \le 1/2 \) for \( n \ge 2 \).
:::

::: {.check}
Is \( n \mapsto n + 1 \) a bijection \( \nN \to \nN \setminus \{0\} \)? What does that show?
:::

::: {.solution}
Yes. Its values lie in \( \nN \setminus \{0\} \), since \( n + 1 \ge 1 \). Its inverse is \( m \mapsto m - 1 \), which is defined on \( \nN \setminus \{0\} \) because \( m - 1 \in \nN \) for \( m \ne 0 \) (@lem-naturals-arithmetic (c)); the two maps undo each other, so it is a bijection by @thm-bijection-iff-inverse. So \( \nN \) is equinumerous with its proper subset \( \nN \setminus \{0\} = \nZ_{>0} \), and by @thm-finite-no-proper-copy, \( \nN \) is infinite, a second time. In the hotel, every guest moves up one room, and room \( 0 \) is free.
:::

::: {.remark}
By @def-finite, a non-empty finite set \( A \) with \( n \) elements is \( \{x_1, \dots, x_n\} \), with \( x_k \coloneqq \varphi(k) \). So when its elements are real numbers it has a maximum and a minimum, by @prp-finite-max. Section 7.3 announced this passage from a finite set to a list.
:::

## Exercises

### A. Check your understanding

::: {#exr-finite-sets-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define "\( A \) is finite", and write its negation in symbols, with every quantifier shown.
2. True or false, with a reason: a subset of an infinite set is infinite; a set that has an infinite subset is infinite.
3. How many injections \( \{1, 2, 3\} \to \{1, 2\} \) are there?
4. Let \( f \colon A \to B \), where \( A \) and \( B \) are finite and \( A \) has more elements than \( B \). What does the pigeonhole principle guarantee about \( f \)?
:::
:::

::: {.solution}
(a) \( A \) is finite if there are \( n \in \nN \) and a bijection \( \varphi \colon \{1, \dots, n\} \to A \) (@def-finite): \( \exists n \in \nN \ \exists \varphi \in A^{\{1, \dots, n\}} \ (\varphi \text{ injective} \wedge \varphi \text{ surjective}) \). By @prp-bounded-quantifier-negation, applied to each quantifier, and De Morgan, its negation is
\[
\forall n \in \nN \ \forall \varphi \in A^{\{1, \dots, n\}} \ (\varphi \text{ not injective} \vee \varphi \text{ not surjective}) ,
\]
which is @def-infinite.

(b) The first is false: \( \emptyset \subseteq \nN \), and \( \emptyset \) is finite while \( \nN \) is infinite (@exm-hilbert-hotel). The second is true: if \( B \) were finite, every subset of \( B \) would be finite by @prp-subset-finite; so a set with an infinite subset is not finite.

(c) None. By @thm-pigeonhole with \( m = 3 > 2 = n \), there is no injection \( \{1, 2, 3\} \to \{1, 2\} \).

(d) That \( f \) is not injective (@cor-pigeonhole-finite-sets (a)): there are two **different** elements \( a \ne a' \) of \( A \) with \( f(a) = f(a') \). It does not say which two, and it says nothing when \( A \) has at most as many elements as \( B \).
:::

### B. Practice

::: {#exr-finite-sets-b1}
[B1: Moving the guests]

Give explicit bijections \( \nN \to \nN \setminus \{0, 1, 2\} \), \( \nN \to \{ n \in \nN : n \ge 5 \} \) and \( \nN \to \{ 2n + 1 : n \in \nN \} \), and prove that each is a bijection by writing down its inverse.
:::

::: {.solution}
*First.* For \( m \in \nN \): if \( m \notin \{0, 1, 2\} \), then \( m \ge 3 \). Indeed \( m \ne 0 \) gives \( m \ge 1 \) (@lem-naturals-arithmetic (a)); with \( m \ne 1 \), \( m > 1 \), so \( m \ge 2 \) (@lem-naturals-arithmetic (e)); with \( m \ne 2 \), \( m \ge 3 \) likewise. Conversely every \( m \ge 3 \) lies outside \( \{0, 1, 2\} \). So \( \nN \setminus \{0, 1, 2\} = \{ m \in \nN : m \ge 3 \} \). Let \( f(n) \coloneqq n + 3 \); then \( f(n) \in \nN \) and \( f(n) \ge 3 \). Let \( g(m) \coloneqq m - 3 \) for \( m \ge 3 \); then \( g(m) \in \nN \) by @lem-naturals-arithmetic (d). Since \( g(f(n)) = n \) and \( f(g(m)) = m \), the map \( f \) is a bijection by @thm-bijection-iff-inverse.

*Second.* The same with \( 5 \) in place of \( 3 \): \( n \mapsto n + 5 \), with inverse \( m \mapsto m - 5 \), which lies in \( \nN \) for \( m \ge 5 \) by @lem-naturals-arithmetic (d).

*Third.* Let \( O \coloneqq \{ 2n + 1 : n \in \nN \} \), the odd natural numbers, and \( f(n) \coloneqq 2n + 1 \), which lies in \( O \) by definition. Every \( m \in O \) is \( 2n + 1 \) for exactly one \( n \in \nN \): one by the definition of \( O \), and only one since \( 2n + 1 = 2n' + 1 \) gives \( n = n' \). So \( g(m) \coloneqq (m - 1)/2 \) is that \( n \), a natural number. Then \( g(f(n)) = n \) and \( f(g(m)) = m \), so \( f \) is a bijection \( \nN \to O \). Each of the three sets is a proper subset of \( \nN \) equinumerous with \( \nN \), which shows again that \( \nN \) is infinite.
:::

::: {#exr-finite-sets-b2}
[B2: Choosing the holes]

::: {.enumerate options="label=(\alph*)"}
1. Prove that among any \( 6 \) different integers, two have the same remainder on division by \( 5 \).
2. Prove that among any \( 5 \) different elements of \( \{1, \dots, 8\} \), two have sum \( 9 \).
:::

*Hint: in (b), group \( \{1, \dots, 8\} \) into pairs.*
:::

::: {.solution}
(a) Let \( A \) be a set of \( 6 \) integers. By @thm-division-algorithm with divisor \( 5 \), each \( a \in A \) has a unique remainder \( r(a) \), an integer with \( 0 \le r(a) < 5 \); then \( r(a) \in \nN \) by @prp-integers-closed (b), and \( r(a) \le 4 \) by discreteness, @prp-integers-closed (c), so \( r(a) \in \{0, \dots, 4\} \). This defines \( r \colon A \to \{0, \dots, 4\} \). The set \( \{0, \dots, 4\} \) has \( 5 \) elements (the third example after @def-finite). Since \( 6 > 5 \), @cor-pigeonhole-finite-sets (a) shows that \( r \) is not injective: there are \( a \ne a' \) in \( A \) with \( r(a) = r(a') \).

(b) Let \( A \subseteq \{1, \dots, 8\} \) have \( 5 \) elements. The holes are the four pairs \( \{1, 8\} \), \( \{2, 7\} \), \( \{3, 6\} \), \( \{4, 5\} \), each of the form \( \{x, 9 - x\} \). Define \( p \colon A \to \{1, 2, 3, 4\} \) by \( p(x) \coloneqq \min\{x, 9 - x\} \), the smaller element of the pair containing \( x \); for \( 1 \le x \le 8 \) this lies in \( \{1, 2, 3, 4\} \), since \( x \le 4 \) or \( 9 - x \le 4 \). The codomain has \( 4 \) elements and \( 5 > 4 \), so by @cor-pigeonhole-finite-sets (a) there are \( x \ne y \) in \( A \) with \( p(x) = p(y) \). Then \( x \) and \( y \) lie in the same pair \( \{c, 9 - c\} \), where \( c = p(x) \), and being different they are its two elements, so \( x + y = 9 \). Five is the least number that works: \( \{1, 2, 3, 4\} \) has \( 4 \) elements, and no two of them sum to \( 9 \), since their largest sum is \( 3 + 4 = 7 \).
:::

::: {#exr-finite-sets-b3}
[B3: Finite unions]

Let \( n \in \nN \), and let \( A_1, \dots, A_n \) be finite sets, that is, a family \( (A_i)_{i \in \{1, \dots, n\}} \) of finite sets. Prove that \( \bigcup_{i \in \{1, \dots, n\}} A_i \) is finite.
:::

::: {.solution}
For \( n \in \nN \) let \( P(n) \) be "for every family \( (A_i)_{i \in \{1, \dots, n\}} \) of finite sets, the union \( U_n \coloneqq \bigcup_{i \in \{1, \dots, n\}} A_i \) is finite". We use @ax-induction.

*Base case.* For \( n = 0 \) the index set is \( \{1, \dots, 0\} = \emptyset \), and the union of the empty family is \( \emptyset \) (@def-family-union-intersection: no \( x \) lies in some \( A_i \)), which has \( 0 \) elements.

*Step.* Suppose \( P(n) \), and let \( (A_i)_{i \in \{1, \dots, n + 1\}} \) be a family of finite sets. Since \( \{1, \dots, n + 1\} = \{1, \dots, n\} \cup \{n + 1\} \), we have \( U_{n+1} = U_n \cup A_{n+1} \), and \( U_n \) is finite by \( P(n) \), applied to the first \( n \) sets; say it has \( p \) elements. Write
\[
U_{n+1} = U_n \cup (A_{n+1} \setminus U_n) ,
\]
a disjoint union. The set \( A_{n+1} \setminus U_n \) is a subset of the finite set \( A_{n+1} \), so it is finite by @prp-subset-finite; say it has \( q \) elements. By @prp-disjoint-union-count, \( U_{n+1} \) has \( p + q \) elements. By @ax-induction, \( P(n) \) holds for every \( n \).

The detour through \( A_{n+1} \setminus U_n \) is needed because @prp-disjoint-union-count is about **disjoint** sets, and \( U_n \) and \( A_{n+1} \) may overlap.
:::

### C. Going deeper

::: {#exr-finite-sets-c1}
[C1: Infinite means arbitrarily large finite pieces]

Prove that a set \( A \) is infinite if and only if for every \( n \in \nN \) there is an injection \( \{1, \dots, n\} \to A \). In the direction \( (\Rightarrow) \), say whether your proof makes infinitely many choices at once, and why.
:::

::: {.solution}
[Hint 1]

For \( (\Leftarrow) \), suppose \( A \) has \( m \) elements and use the hypothesis at one well-chosen \( n \). For \( (\Rightarrow) \), induct on \( n \).
:::

::: {.solution}
[Hint 2]

For \( (\Rightarrow) \): let \( P(n) \) be "there is an injection \( \{1, \dots, n\} \to A \)"; the base case is the empty function.
:::

::: {.solution}
\( (\Leftarrow) \) Suppose the condition holds and, for a contradiction, that \( A \) has \( m \) elements, with a bijection \( \varphi \colon \{1, \dots, m\} \to A \). Take \( n \coloneqq m + 1 \) and an injection \( f \colon \{1, \dots, m + 1\} \to A \). By @thm-bijection-iff-inverse, \( \varphi \) has an inverse \( \varphi^{-1} \colon A \to \{1, \dots, m\} \), which is a bijection, since \( \varphi \) is a two-sided inverse of it (@def-inverse-function, @thm-bijection-iff-inverse). Then \( \varphi^{-1} \circ f \colon \{1, \dots, m + 1\} \to \{1, \dots, m\} \) is injective (@thm-composition-injective-surjective (a)), which contradicts @thm-pigeonhole. So \( A \) is infinite.

\( (\Rightarrow) \) Let \( A \) be infinite. For \( n \in \nN \) let \( P(n) \) be "there is an injection \( \{1, \dots, n\} \to A \)". We use @ax-induction.

*Base case.* \( \{1, \dots, 0\} = \emptyset \), and the empty function \( \emptyset \to A \) (@prp-empty-function (a)) is injective, vacuously.

*Step.* Suppose \( P(n) \), and let \( f \colon \{1, \dots, n\} \to A \) be an injection. With its codomain shrunk to its image \( F \coloneqq f(\{1, \dots, n\}) \), it is a bijection, so \( F \) has \( n \) elements. Since \( A \) is infinite, \( F \ne A \); and \( F \subseteq A \), so there is some \( a \in A \setminus F \). Define \( g \colon \{1, \dots, n + 1\} \to A \) by \( g(k) \coloneqq f(k) \) for \( k \le n \) and \( g(n + 1) \coloneqq a \); this is a function because \( \{1, \dots, n + 1\} = \{1, \dots, n\} \cup \{n + 1\} \) and \( n + 1 \notin \{1, \dots, n\} \) (@lem-naturals-arithmetic (e)). It is injective: two inputs \( \le n \) are separated by \( f \), and \( g(n + 1) = a \notin F \) differs from every \( g(k) \) with \( k \le n \). So \( P(n + 1) \) holds. By @ax-induction, \( P(n) \) holds for every \( n \).

*No infinitely many choices are made.* The step uses two existence statements, \( P(n) \) and "\( A \setminus F \ne \emptyset \)", and names one witness for each: one \( \rulename{\exists E} \) each, inside the proof of the single implication \( P(n) \Rightarrow P(n + 1) \). Its conclusion, \( P(n + 1) \), is again an existence statement, so the witnesses never leave the step. Induction then gives \( P(n) \) for each \( n \) **separately**: for each \( n \) **some** injection exists, and different \( n \) may use unrelated ones. Gluing the steps into one injection \( \nN \to A \), with a new point picked at every stage, would require all the picks at once, with no rule saying which point to pick. That is a different statement; Section 8.6 proves it with the principle of choice of Section 8.3.

**Marking scheme.** (10 points)
- 2: \( (\Leftarrow) \) supposes \( A \) has \( m \) elements and uses the hypothesis at \( n = m + 1 \) to contradict the pigeonhole principle (@thm-pigeonhole or @cor-pigeonhole-finite-sets (a)).
- 1: \( (\Rightarrow) \) sets up an induction on \( n \) with the base case \( n = 0 \) (the empty function); a base \( n = 1 \) earns the point only if \( n = 0 \) is also covered (by the empty function).
- 3: in the step, shows that the image of the given injection has \( n \) elements and is therefore not \( A \), and takes a point outside it.
- 2: extends the injection by that point and checks injectivity, including the new value against the old ones.
- 2: explains that each step makes finitely many choices inside one implication, so no principle of choice is used, and that building one injection on all of \( \nN \) would be a different statement.
Fatal errors (0 for the step): picking "a new point for every \( n \)" to define one function \( \nN \to A \) and calling it induction; taking a point outside the image without showing the image is not all of \( A \).
:::

::: {#exr-finite-sets-c2}
[C2: Counting products and functions]

Let \( m, n \in \nN \), let \( A \) have \( m \) elements, and let \( B \) have \( n \) elements.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( A \times B \) has \( mn \) elements.
2. Prove that the set \( B^A \) of functions \( A \to B \) has \( n^m \) elements.
3. Check your formula in (b) against @prp-empty-function in the cases \( m = 0 \) and \( m \ge 1 \), \( n = 0 \).
:::
:::

::: {.solution}
[Hint 1]

Induct on \( m \), with \( B \) fixed, and remove one point \( a \) from \( A \) by @cor-remove-point.
:::

::: {.solution}
[Hint 2]

For (b), a function on \( A \) is the same as a function on \( A \setminus \{a\} \) together with one value at \( a \): consider \( f \mapsto (f|_{A \setminus \{a\}}, f(a)) \).
:::

::: {.solution}
(a) Fix \( B \) with \( n \) elements. For \( m \in \nN \) let \( P(m) \) be "for every set \( A \) with \( m \) elements, \( A \times B \) has \( mn \) elements" (\( mn \in \nN \) by @lem-naturals-arithmetic (b)). *Base case.* If \( A \) has \( 0 \) elements, then \( A = \emptyset \), and \( A \times B = \emptyset \), since a pair in it would need a first coordinate in \( \emptyset \). It has \( 0 = 0 \cdot n \) elements. *Step.* Suppose \( P(m) \), let \( A \) have \( m + 1 \) elements, pick \( a \in A \), and put \( A' \coloneqq A \setminus \{a\} \), which has \( m \) elements by @cor-remove-point. Then
\[
A \times B = (A' \times B) \cup (\{a\} \times B) ,
\]
and the union is disjoint, since first coordinates in \( A' \) differ from \( a \) (@def-ordered-pair). The first set has \( mn \) elements by \( P(m) \). The map \( B \to \{a\} \times B \), \( b \mapsto (a, b) \), is injective by @def-ordered-pair and surjective by @def-cartesian-product, so \( \{a\} \times B \) has \( n \) elements. By @prp-disjoint-union-count, \( A \times B \) has \( mn + n = (m + 1)n \) elements. By @ax-induction, \( P(m) \) holds for every \( m \), and \( B \) was arbitrary.

(b) Fix \( B \) with \( n \) elements, and let \( Q(m) \) be "for every set \( A \) with \( m \) elements, \( B^A \) has \( n^m \) elements" (\( n^m \in \nN \) by @prp-power-laws (d)). *Base case.* \( A = \emptyset \), and by @prp-empty-function (a), \( B^{\emptyset} \) has exactly one element, the empty function; \( n^0 = 1 \) (@def-power), also when \( n = 0 \). *Step.* Suppose \( Q(m) \), let \( A \) have \( m + 1 \) elements, pick \( a \in A \), and let \( A' \coloneqq A \setminus \{a\} \), with \( m \) elements. Define
\[
R \colon B^A \to B^{A'} \times B , \qquad R(f) \coloneqq (f|_{A'}, f(a)) .
\]
*Injective:* if \( R(f) = R(f') \), then \( f \) and \( f' \) agree on \( A' \) and at \( a \), hence on \( A = A' \cup \{a\} \), and they have the same domain and codomain, so \( f = f' \) by @prp-function-equality. *Surjective:* given \( (h, b) \in B^{A'} \times B \), let \( f \) have graph \( G \cup \{(a, b)\} \), where \( G \) is the graph of \( h \), and codomain \( B \). Each \( x \in A' \) has exactly one partner, its \( h \)-value, because \( (a, b) \) has first coordinate \( a \notin A' \); and \( a \) has exactly one, \( b \), because every pair of \( G \) has first coordinate in \( A' \). So \( f \in B^A \), and \( R(f) = (h, b) \). Hence \( R \) is a bijection. By \( Q(m) \), \( B^{A'} \) has \( n^m \) elements, so by (a), applied to the sets \( B^{A'} \) and \( B \), the product \( B^{A'} \times B \) has \( n^m \cdot n = n^{m+1} \) elements (@def-power). Since \( R \) is a bijection, \( \card{B^A} = \card{B^{A'} \times B} \) (@def-equinumerous), and \( \card{\{1, \dots, n^{m+1}\}} = \card{B^{A'} \times B} \). By @prp-equinumerous-properties (b) and (c), \( \card{\{1, \dots, n^{m+1}\}} = \card{B^A} \), that is, \( B^A \) has \( n^{m+1} \) elements. By @ax-induction, \( Q(m) \) holds for every \( m \).

(c) For \( m = 0 \): \( B^{\emptyset} \) has one element by @prp-empty-function (a), and \( n^0 = 1 \), even for \( n = 0 \). For \( m \ge 1 \) and \( n = 0 \): \( A \ne \emptyset \), so there is no function \( A \to \emptyset \) by @prp-empty-function (b), and \( B^A = \emptyset \) has \( 0 \) elements; and \( 0^m = 0^{m-1} \cdot 0 = 0 \). Both agree with (b). With \( B = \{0, 1\} \), (b) recovers the count \( 2^m \) of the paragraph after @prp-power-set-count.

**Marking scheme.** (10 points)
- 2: sets up each induction on \( m \) with \( B \) fixed, and handles \( m = 0 \) (the empty product; the empty function).
- 2: in each step, takes an **arbitrary** \( A \) with \( m + 1 \) elements, removes one point by @cor-remove-point, and applies the hypothesis to the rest.
- 2: (a) splits \( A \times B \) into two disjoint pieces and counts \( \{a\} \times B \) by a bijection with \( B \).
- 3: (b) gives a bijection between \( B^A \) and \( B^{A'} \times B \), checking injectivity (equality of functions) and surjectivity (the extended graph is a function).
- 1: (c) checks both degenerate cases against @prp-empty-function.
- Direct route for (a): composing the given bijections with a bijection \( \{1, \dots, m\} \times \{1, \dots, n\} \to \{1, \dots, mn\} \), e.g. \( (i, j) \mapsto (i - 1)n + j \), with injectivity and surjectivity checked (for example by @thm-division-algorithm) and the case \( m = 0 \) or \( n = 0 \) handled, earns the 2 points of the (a) line and the (a) halves (1 point each) of the two induction lines.
Fatal errors (0 for the step): "each of the \( m \) elements has \( n \) possible values, so \( n^m \)" with no bijection or induction; a step that applies the hypothesis to a set not shown to have \( m \) elements.
:::

<!-- dependency ledger
def-equinumerous (example): f(x) = 2x maps [0, 1] onto [0, 2], y/2 in [0, 1] for y in [0, 2] | R arithmetic and order, school fact; axioms in Ch 11
prp-equinumerous-properties (claim): (the remark after it and the paragraph after the remark) the union of a set of sets is a set | (W3) of Section 6.1 (working rule, no label)
def-finite (claim): the notation {1, ..., n} = {k in N : 1 <= k <= n} and {0, ..., n} | Section 7.1 (notation, no label)
def-infinite (claim): (Shrinking the codomain) a graph inside X x C with codomain C is a function X -> C with the same values | def-function (cited), stated inline
thm-pigeonhole (proof): m > n + 1 gives m - 1 > n; k <= m - 1 < m; trichotomy | R order, school fact
thm-pigeonhole (proof): {1, ..., m - 1} is a subset of {1, ..., m} | definition of {1, ..., n} (Section 7.1) and R order
cor-pigeonhole-finite-sets (example): (the three-integers paragraph) r in {0, 1}; q + q' + r in Z | thm-division-algorithm, prp-integers-closed (a), (b), lem-naturals-arithmetic (e) (cited)
cor-pigeonhole-finite-sets (example): (the three-integers paragraph) a + b = 2(q + q' + r), r + r = 2r | R arithmetic, school fact
cor-finite-size-unique (proof): trichotomy of < on N | R order, school fact
prp-disjoint-union-count (proof): 1 <= k - m <= n for m < k <= m + n; m < m + j <= m + n | R order, school fact; lem-naturals-arithmetic (d), (e) (cited)
prp-subset-finite (proof): {1, ..., n + 1} = {1, ..., n} u {n + 1}; restriction of an injective map is injective | lem-naturals-arithmetic (e) (cited); restriction, Section 6.4 (no label)
prp-power-set-count (proof): 2^n, 2^(n+1) in N | prp-power-laws (d) (cited)
prp-power-set-count (proof): (S u {a}) \ {a} = S when a is not in S; U = (U \ {a}) u {a} when a in U | set algebra, Section 6.2; checked inline
prp-power-set-count (claim): (the paragraph after it) S -> 1_S is a bijection P(Y) -> {0, 1}^Y with inverse f -> {y : f(y) = 1} | Section 6.4, the correspondence after exm-function-set-small (prose, no label)
exm-hilbert-hotel (solution): 2n = 2n' implies n = n'; 2n >= 2 for n >= 1 | R arithmetic and order, school fact
thm-finite-no-proper-copy (claim): (the second warning after exm-hilbert-hotel) x/(1 + x) maps 1/n to 1/(n + 1); y/(1 - y) inverts it; 1/n <= 1/2 for n >= 2 | R arithmetic, school fact; checked inline
exr-finite-sets-a1 (solution): De Morgan for "not (P and Q)" | Chapter 2 (DM, derived rule; no label cited)
exr-finite-sets-b1 (solution): (m - 1)/2 = n for m = 2n + 1; 2n + 1 = 2n' + 1 gives n = n' | R arithmetic, school fact
exr-finite-sets-b2 (solution): remainder r(a) in {0, ..., 4} | thm-division-algorithm, prp-integers-closed (b), (c) (cited)
exr-finite-sets-b2 (solution): min{x, 9 - x} <= 4 for 1 <= x <= 8; 3 + 4 = 7 | R arithmetic, school fact
exr-finite-sets-b3 (solution): {1, ..., n + 1} = {1, ..., n} u {n + 1}; the union over it splits accordingly | lem-naturals-arithmetic (e); def-family-union-intersection (cited)
exr-finite-sets-c1 (solution): phi^(-1) is a bijection; {1, ..., n + 1} = {1, ..., n} u {n + 1}, n + 1 not in {1, ..., n} | thm-bijection-iff-inverse, def-inverse-function, lem-naturals-arithmetic (e) (cited)
exr-finite-sets-c2 (solution): mn in N; n^m in N; B^A equinumerous with {1, ..., n^(m+1)} via R | lem-naturals-arithmetic (b), prp-power-laws (d), prp-equinumerous-properties (b), (c) (cited)
exr-finite-sets-c2 (solution): restriction f|_A' is a function A' -> B | restriction, Section 6.4 (no label)
-->
