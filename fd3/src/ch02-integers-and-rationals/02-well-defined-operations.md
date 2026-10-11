# Well-Definedness, and the Arithmetic of the Integers

Section 10.1 built \( \nZ \) as the set of classes of \( \sim \) on \( \nN \times \nN \), and gave each integer a normal form (@prp-integer-normal-form). The integers cannot yet be added. Every operation on classes will be defined by a formula on representatives, and Section 7.5 showed what can go wrong: a formula that gives two answers for one class (@exm-ill-defined-class-map). This section proves, once and for all, the lemma that says when such a formula defines a function. It then uses the lemma for the sum, product and negative of integers, and finds a copy of \( \nN \) inside \( \nZ \).

## Definitions through representatives

In Section 7.5 the addition of \( \nZ/n \) was defined by \( [a] + [b] \coloneqq [a + b] \), and @prp-congruence-arithmetic checked that the right side depends only on the classes, not on the integers \( a \) and \( b \) used to name them. In @exm-ill-defined-class-map the same kind of formula, \( [a]_6 \mapsto [a]_4 \), gave one class two values, and so defined no function.

The same situation will recur throughout this volume: for \( \nZ \) in this section, for \( \nQ \) in Section 10.4, and for \( \nR \) later in this volume. Each time, a set is a quotient \( X/{\sim} \), and something is defined on it by a formula on elements of \( X \). Rather than repeat the argument of @prp-congruence-arithmetic for every formula, we separate it into two parts: a general lemma, proved here once, which turns a **check on representatives** into a function on classes; and the check itself, which is different for each formula and is all that remains to do each time.

A rule "\( [x] \mapsto \) something computed from \( x \)" is called **well defined** when representatives of the same class always give the same result. The lemma below says that well defined is exactly what is needed, in three settings: a map from one quotient to another, a binary operation on a quotient, and a property of classes.

## The lemma

*A rule on classes is a function as soon as equivalent inputs give equivalent outputs.*

::: {#thm-well-defined-on-classes}
[Functions on Classes]

Let \( \sim \) be an equivalence relation on a set \( X \), and \( \approx \) an equivalence relation on a set \( Y \). Classes are taken for \( \sim \) in \( X \) and for \( \approx \) in \( Y \).

::: {.enumerate options="label=(\alph*)"}
1. Let \( f \colon X \to Y \) be a function such that, **for all** \( x, x' \in X \), \( x \sim x' \) implies \( f(x) \approx f(x') \). Then there is **exactly one** function \( F \colon X/{\sim} \to Y/{\approx} \) with \( F([x]) = [f(x)] \) for every \( x \in X \).
2. Let \( g \colon X \times X \to X \) be a function such that, **for all** \( x, x', y, y' \in X \),
\[
\begin{aligned}
x \sim x' &\implies g(x, y) \sim g(x', y) , \\
y \sim y' &\implies g(x, y) \sim g(x, y') .
\end{aligned}
\]
Then there is **exactly one** function \( G \colon (X/{\sim}) \times (X/{\sim}) \to X/{\sim} \) with \( G([x], [y]) = [g(x, y)] \) for all \( x, y \in X \).
3. Let \( S \subseteq X \) be such that, for all \( x, x' \in X \), \( x \sim x' \) and \( x \in S \) imply \( x' \in S \). Let \( \bar S \coloneqq \{ [x] : x \in S \} \subseteq X/{\sim} \). Then, **for every** \( x \in X \), \( [x] \in \bar S \) if and only if \( x \in S \).
:::
:::

In words: (a) says that a map on elements that respects the two relations passes to a map on classes; (b) says that a binary operation that respects \( \sim \) **in each argument separately** passes to an operation on classes; (c) says that a property that respects \( \sim \) can be asked of a class, and the answer is the answer for any of its representatives. Clause (a) will give the negative of an integer, (b) its sum and product, and (c) the positive integers in Section 10.3.

::: {.idea}
A function is a graph with **exactly one** output for each input (@def-function). The obvious graph is the set of all pairs \( ([x], [f(x)]) \). It has at least one output for each class, because every class is some \( [x] \). The only danger is two outputs for one class, coming from two representatives \( x \) and \( x' \) of it; @thm-classes-partition (b) turns "same class" into \( x \sim x' \), the hypothesis turns that into \( f(x) \approx f(x') \), and @thm-classes-partition (b) turns it back into "same output". For (b) the same plan works, once the two one-argument hypotheses are chained into one statement about both arguments by transitivity.
:::

::: {.proof}
*(a)* Let
\[
G_F \coloneqq \{ (C, D) \in (X/{\sim}) \times (Y/{\approx}) : C = [x] \text{ and } D = [f(x)] \text{ for some } x \in X \} ,
\]
a set by specification (@def-set-builder). We check the two clauses of @def-function. (Fn1): every \( C \in X/{\sim} \) is \( [x] \) for some \( x \in X \) (@def-quotient-set), and then \( (C, [f(x)]) \in G_F \). (Fn2): suppose \( (C, D) \in G_F \) and \( (C, D') \in G_F \), say \( C = [x] \), \( D = [f(x)] \), and \( C = [x'] \), \( D' = [f(x')] \). Then \( [x] = [x'] \), so \( x \sim x' \) by @thm-classes-partition (b). By the hypothesis, \( f(x) \approx f(x') \), so \( [f(x)] = [f(x')] \) by @thm-classes-partition (b), that is, \( D = D' \). So \( F \), the function with graph \( G_F \) and codomain \( Y/{\approx} \), is a function \( X/{\sim} \to Y/{\approx} \), and \( F([x]) = [f(x)] \) because \( ([x], [f(x)]) \in G_F \).

For uniqueness, let \( F' \colon X/{\sim} \to Y/{\approx} \) also satisfy \( F'([x]) = [f(x)] \) for every \( x \). Every \( C \in X/{\sim} \) is some \( [x] \), and then \( F'(C) = [f(x)] = F(C) \). The two functions have the same domain and codomain, so \( F' = F \) by @prp-function-equality.

*(b)* First, for all \( x, x', y, y' \in X \) with \( x \sim x' \) and \( y \sim y' \),
\[
g(x, y) \sim g(x', y) \quad \text{and} \quad g(x', y) \sim g(x', y') ,
\]
by the first hypothesis (with \( y \) fixed) and the second (with \( x' \) fixed). By transitivity, (Eq3) of @def-equivalence-relation, \( g(x, y) \sim g(x', y') \).

Now let \( G_G \) be the set of \( (P, E) \in \bigl((X/{\sim}) \times (X/{\sim})\bigr) \times (X/{\sim}) \) such that \( P = ([x], [y]) \) and \( E = [g(x, y)] \) for some \( x, y \in X \), a set by specification. (Fn1): an element of \( (X/{\sim}) \times (X/{\sim}) \) is a pair \( (C, D) \) of classes (@def-cartesian-product), and \( C = [x] \), \( D = [y] \) for some \( x, y \in X \) (@def-quotient-set); then \( ((C, D), [g(x, y)]) \in G_G \). (Fn2): suppose \( (P, E) \) and \( (P, E') \) lie in \( G_G \), with \( P = ([x], [y]) \), \( E = [g(x, y)] \), and \( P = ([x'], [y']) \), \( E' = [g(x', y')] \). From \( ([x], [y]) = ([x'], [y']) \) the characteristic property of pairs (@def-ordered-pair) gives \( [x] = [x'] \) and \( [y] = [y'] \), so \( x \sim x' \) and \( y \sim y' \) by @thm-classes-partition (b). By the first paragraph, \( g(x, y) \sim g(x', y') \), so \( E = E' \) by @thm-classes-partition (b). So \( G_G \), with codomain \( X/{\sim} \), defines a function \( G \) with \( G([x], [y]) = [g(x, y)] \). Uniqueness is as in (a), by @prp-function-equality.

*(c)* \( (\Leftarrow) \) If \( x \in S \), then \( [x] \in \bar S \) by the definition of \( \bar S \). \( (\Rightarrow) \) If \( [x] \in \bar S \), then \( [x] = [x'] \) for some \( x' \in S \). By @thm-classes-partition (b), \( x \sim x' \), so \( x' \sim x \) by (Eq2). The hypothesis, applied to \( x' \sim x \) and \( x' \in S \), gives \( x \in S \).

This proves the theorem.
:::

The functions \( F \) and \( G \) are said to be **induced** by \( f \) and \( g \). In practice we write the conclusion of (a) as "the rule \( [x] \mapsto [f(x)] \) is well defined", and of (b) as "the operation \( [x] \ast [y] \coloneqq [g(x, y)] \) is well defined", and the work is always the check of the hypotheses.

::: {.remark}
**Each hypothesis has a job.** Without the hypothesis of (c) the conclusion fails. On \( \nN \times \nN \) with the relation \( \sim \) of @def-integers-as-classes, let \( S \coloneqq \{ (a, b) : 0 < a \} \). Then \( (1, 1) \in S \), so \( [(1, 1)] \in \bar S \); and \( [(0, 0)] = [(1, 1)] \), so \( [(0, 0)] \in \bar S \), while \( (0, 0) \notin S \). Membership in \( \bar S \) does not tell us whether a particular representative lies in \( S \). The hypotheses of (a) and (b) are needed in the same way, and the examples below show them failing.
:::

## Sum, product and negative of integers

To guess the formulas, borrow the school picture once more. If \( (a, b) \) records "\( a - b \)" and \( (c, d) \) records "\( c - d \)", then school algebra gives
\[
\begin{aligned}
(a - b) + (c - d) &= (a + c) - (b + d) , \\
(a - b)(c - d) &= (ac + bd) - (ad + bc) , \\
-(a - b) &= b - a .
\end{aligned}
\]
These identities are a **heuristic**: they come from the school integers, which this chapter does not assume, and they are used only to find the definition. Each right side is again a difference of two natural numbers, so it can be recorded as a pair.

::: {#def-integer-operations}
[Sum, Product and Negative of Integers]

For all \( (a, b), (c, d) \in \nN \times \nN \), let
\[
\begin{aligned}
[(a, b)] + [(c, d)] &\coloneqq [(a + c, \ b + d)] , \\
[(a, b)] \cdot [(c, d)] &\coloneqq [(ac + bd, \ ad + bc)] , \\
-[(a, b)] &\coloneqq [(b, a)] .
\end{aligned}
\]
The **sum** \( + \colon \nZ \times \nZ \to \nZ \) and **product** \( \cdot \colon \nZ \times \nZ \to \nZ \) are the functions that @thm-well-defined-on-classes (b) induces from the maps \( g_+ \), \( g_\cdot \colon (\nN \times \nN) \times (\nN \times \nN) \to \nN \times \nN \) given by the pairs on the right; the **negative** \( - \colon \nZ \to \nZ \) is the function that @thm-well-defined-on-classes (a) induces from \( (a, b) \mapsto (b, a) \). We also write \( xy \) for \( x \cdot y \).
:::

In words: to add integers, add representatives coordinatewise; to multiply, use the cross formula; to negate, swap the coordinates. All the arithmetic on the right happens in \( \nN \), where it is always possible. The definition is legitimate only if the hypotheses of @thm-well-defined-on-classes hold for the three maps on pairs; the next proposition checks them, and until then the three formulas are rules, not yet functions.

The move used in the proof is the one this chapter is built on.

**Check on representatives, one argument at a time.** To show that \( [x] \ast [y] \coloneqq [g(x, y)] \) is well defined, change \( x \) to an equivalent \( x' \) with \( y \) fixed, then change \( y \) to an equivalent \( y' \) with \( x' \) fixed. Each change is a computation at the level below, in \( \nN \) here; @thm-well-defined-on-classes (b) joins the two by transitivity.

::: {#prp-integer-operations-well-defined}
[The Operations on Integers Are Well Defined]

The maps \( g_+ \) and \( g_\cdot \) of @def-integer-operations satisfy the hypotheses of @thm-well-defined-on-classes (b), and the map \( (a, b) \mapsto (b, a) \) satisfies those of @thm-well-defined-on-classes (a), with \( \sim \) on both sides. Hence the sum, product and negative of @def-integer-operations are well-defined functions.
:::

::: {.idea}
Each hypothesis is an equation in \( \nN \) to be derived from another. The given equation is the cross-sum equation for \( (a, b) \sim (a', b') \); the target is the cross-sum equation for the two outputs. For the sum, adding \( c + d \) to both sides of the given equation and rearranging is enough. For the product, the target has \( c \) and \( d \) in every term, so we multiply the given equation by \( c \), and separately by \( d \), and add the results; the rest is rearranging. Both formulas are unchanged when the two input pairs are swapped, so the second argument costs nothing.

*Before reading on: why may we change one argument at a time, rather than both at once?*
:::

::: {.proof}
Let \( (a, b), (a', b'), (c, d) \in \nN \times \nN \) with \( (a, b) \sim (a', b') \), that is,
\[
a + b' = a' + b .
\]{#eq-integer-rep-change}
All rearrangements below use @thm-omega-arithmetic-laws: commutativity and associativity of \( + \) and \( \cdot \), and distributivity.

*Sum, first argument.* We need \( (a + c, b + d) \sim (a' + c, b' + d) \), that is, \( (a + c) + (b' + d) = (b + d) + (a' + c) \). The left side is \( (a + b') + (c + d) \), which by @eq-integer-rep-change equals \( (a' + b) + (c + d) \), and that is the right side rearranged.

*Product, first argument.* We need
\[
(ac + bd, \ ad + bc) \sim (a'c + b'd, \ a'd + b'c) ,
\]
that is, the cross-sum equation
\[
(ac + bd) + (a'd + b'c) = (ad + bc) + (a'c + b'd) .
\]{#eq-integer-product-target}
Multiply both sides of @eq-integer-rep-change by \( c \) and use distributivity: \( ac + b'c = a'c + bc \). Multiply both sides of @eq-integer-rep-change, read from right to left, by \( d \): \( a'd + bd = ad + b'd \). Adding these two equations,
\[
(ac + b'c) + (a'd + bd) = (a'c + bc) + (ad + b'd) .
\]
The left side rearranges to the left side of @eq-integer-product-target, and the right side to its right side. This proves @eq-integer-product-target.

*Second arguments.* By commutativity in \( \nN \), \( g_+((a, b), (c, d)) = (a + c, b + d) = (c + a, d + b) = g_+((c, d), (a, b)) \), and likewise
\[
g_\cdot((a, b), (c, d)) = (ac + bd, \ ad + bc) = (ca + db, \ cb + da) = g_\cdot((c, d), (a, b)) .
\]
So if \( (c, d) \sim (c', d') \), then, by the first-argument case applied with the roles of the two pairs exchanged,
\[
g((a, b), (c, d)) = g((c, d), (a, b)) \sim g((c', d'), (a, b)) = g((a, b), (c', d'))
\]
for \( g = g_+ \) and \( g = g_\cdot \). This is the second hypothesis of @thm-well-defined-on-classes (b).

*Negative.* The pair \( (b, a) \) is related to \( (b', a') \) when \( b + a' = a + b' \), and that is @eq-integer-rep-change read from right to left. This is the hypothesis of @thm-well-defined-on-classes (a).

By @thm-well-defined-on-classes (b) and (a), the three rules define functions \( \nZ \times \nZ \to \nZ \), \( \nZ \times \nZ \to \nZ \) and \( \nZ \to \nZ \), as claimed.
:::

The answer to the prompt is the first paragraph of the proof of @thm-well-defined-on-classes (b): two one-argument changes, \( g(x, y) \sim g(x', y) \) and \( g(x', y) \sim g(x', y') \), are joined by transitivity of \( \sim \). Changing both at once is also possible, but the computation then mixes four equations in eight unknowns; one argument at a time keeps each computation to a single hypothesis.

## Rules that fail

Every check happens in the hypotheses of the lemma. Here they fail, next to a rule where they hold.

::: {#exm-ill-defined-first-coordinate}
[The first coordinate is not a function of the class]

::: {.enumerate options="label=(\alph*)"}
1. Does the rule \( [(a, b)] \mapsto a \) define a function \( \nZ \to \nN \)?
2. Does the rule \( [(a, b)] \mapsto [(a + 1, b)] \) define a function \( \nZ \to \nZ \)?
3. A student argues: "Each integer \( x \) has a pair with least first coordinate, by @thm-omega-well-ordering applied to the non-empty set of first coordinates of the pairs in \( x \); call that least first coordinate \( h(x) \). Then \( h \) is a function \( \nZ \to \nN \), since each \( x \) determines its own least first coordinate. So \( [(a, b)] \mapsto a \) is a function, namely \( h \), with \( h([(a, b)]) = a \) for every \( (a, b) \)." Find the error.
:::
:::

::: {.solution}
(a) No. \( (0, 2) \sim (1, 3) \), since \( 0 + 3 = 2 + 1 \), so \( [(0, 2)] = [(1, 3)] \) by @thm-classes-partition (b). Read with the representative \( (0, 2) \), the rule gives \( 0 \); read with \( (1, 3) \), it gives \( 1 \). One input gets two values, and (Fn2) of @def-function fails. The hypothesis of @thm-well-defined-on-classes (a) (with equality on \( \nN \) as \( \approx \), whose classes are single numbers) fails at \( x = (0, 2) \), \( x' = (1, 3) \).

(b) Yes. Let \( (a, b) \sim (a', b') \), so \( a + b' = a' + b \). Then
\[
(a + 1) + b' = (a + b') + 1 = (a' + b) + 1 = b + (a' + 1)
\]
by @thm-omega-arithmetic-laws (b), (c), which is \( (a + 1, b) \sim (a' + 1, b') \). By @thm-well-defined-on-classes (a), the rule is a function. In fact it is \( x \mapsto x + [(1, 0)] \), since \( [(a, b)] + [(1, 0)] = [(a + 1, b + 0)] = [(a + 1, b)] \).

(c) The conclusion is false, by (a), so some step fails. The function \( h \) is fine: the least first coordinate is computed from the set \( x \) alone. The failing step is the last clause, "\( h([(a, b)]) = a \) for every \( (a, b) \)". It holds only when \( (a, b) \) happens to be the pair with least first coordinate. The argument chose a particular representative to define \( h \), and then used an **arbitrary** one. Counterexample to the step: \( x = [(1, 3)] = [(0, 2)] \) contains \( (0, 2) \), so \( h(x) = 0 \), while the representative \( (1, 3) \) has first coordinate \( 1 \).
:::

::: {.warning}
**A formula that looks right need not be well defined.** "\( [(a, b)] \cdot [(c, d)] \coloneqq [(ac, bd)] \), like the sum" is not a definition: \( (1, 0) \sim (2, 1) \), since \( 1 + 1 = 0 + 2 \), but with \( (c, d) = (1, 2) \) the outputs are \( (1 \cdot 1, 0 \cdot 2) = (1, 0) \) and \( (2 \cdot 1, 1 \cdot 2) = (2, 2) \), and \( (1, 0) \not\sim (2, 2) \), since \( 1 + 2 \ne 0 + 2 \). **And well defined is necessary, not sufficient.** The rule \( [(a, b)] \ast [(c, d)] \coloneqq [(ad + bc, \ ac + bd)] \) is well defined, since it is the negative of the product; but it gives \( [(0, 1)] \ast [(0, 1)] = [(0 + 0, 0 + 1)] = [(0, 1)] \), so the "square" of the class of \( (0, 1) \) is that class itself, not \( [(1, 0)] \). Well-definedness says that a rule is a function; whether it is the right function is a separate question.
:::

## The natural numbers inside the integers

The integers were built to contain the natural numbers and more. They do not literally contain them: the natural number \( 0 \) is the empty set (@def-omega-arithmetic (c)), while every integer is a non-empty class (@thm-classes-partition (a)), so \( 0 \notin \nZ \). What \( \nZ \) contains is a **copy** of \( \nN \), the classes in normal form \( [(n, 0)] \), and the copy has the same arithmetic.

::: {#prp-naturals-embed-integers}
[The Natural Numbers Embed in the Integers]

Let \( \iota \colon \nN \to \nZ \), \( \iota(n) \coloneqq [(n, 0)] \).

::: {.enumerate options="label=(\alph*)"}
1. \( \iota \) is injective, and for all \( m, n \in \nN \),
\[
\iota(m + n) = \iota(m) + \iota(n), \qquad \iota(mn) = \iota(m) \, \iota(n) .
\]
2. For every \( x \in \nZ \), \( x + \iota(0) = x \) and \( \iota(1) \cdot x = x \). For every \( (a, b) \in \nN \times \nN \), \( [(a, b)] = \iota(a) + \bigl(-\iota(b)\bigr) \).
3. \( \nZ = \iota(\nN) \cup \{ -\iota(n) : n \in \nN \} \).
:::
:::

::: {.idea}
Every claim is a computation with the formulas of @def-integer-operations on pairs with a second coordinate \( 0 \), where the zeros make most terms vanish. Injectivity and (c) are the two halves of @prp-integer-normal-form: (b) of it says that different natural numbers give different classes, and (a) says that every class is in normal form.
:::

::: {.proof}
*(a)* If \( \iota(m) = \iota(n) \), then \( [(m, 0)] = [(n, 0)] \), so \( m = n \) by @prp-integer-normal-form (b); hence \( \iota \) is injective (@def-injective). By @def-integer-operations,
\[
\iota(m) + \iota(n) = [(m + n, \ 0 + 0)] = [(m + n, 0)] = \iota(m + n) ,
\]
since \( 0 + 0 = 0 \) (@def-omega-arithmetic (a)), and
\[
\iota(m) \, \iota(n) = [(mn + 0 \cdot 0, \ m \cdot 0 + 0 \cdot n)] = [(mn, 0)] = \iota(mn) ,
\]
since \( m \cdot 0 = 0 \) (@def-omega-arithmetic (b)), \( 0 \cdot n = 0 \) (@thm-omega-arithmetic-laws (e)) and \( k + 0 = k \).

*(b)* Let \( x = [(a, b)] \). Then \( x + \iota(0) = [(a + 0, b + 0)] = [(a, b)] = x \), and
\[
\iota(1) \cdot x = [(1 \cdot a + 0 \cdot b, \ 1 \cdot b + 0 \cdot a)] = [(a, b)] = x ,
\]
by @thm-omega-arithmetic-laws (e) (\( 1 \cdot n = n \), \( 0 \cdot n = 0 \)) and \( n + 0 = n \). Finally, \( -\iota(b) = -[(b, 0)] = [(0, b)] \), so \( \iota(a) + (-\iota(b)) = [(a + 0, \ 0 + b)] = [(a, b)] \), using \( 0 + b = b \) (@thm-omega-arithmetic-laws (a)).

*(c)* \( (\supseteq) \) Both sets on the right consist of integers. \( (\subseteq) \) Let \( x \in \nZ \). By @prp-integer-normal-form (a), \( x = [(k, 0)] \) or \( x = [(0, k)] \) for some \( k \in \nN \). In the first case \( x = \iota(k) \). In the second, \( x = [(0, k)] = -[(k, 0)] = -\iota(k) \) by @def-integer-operations. So \( x \) lies in the right side.
:::

**Identification.** From now on we write \( n \) for \( \iota(n) \) and regard \( \nN \) as a subset of \( \nZ \). This is a convenient abuse of notation, and (a) makes it honest: because \( \iota \) is injective, different natural numbers stay different; because \( \iota \) preserves \( + \) and \( \cdot \), a sum or product of natural numbers is the same whether computed in \( \nN \) or in \( \nZ \). One could rebuild \( \nZ \) so that it contains \( \nN \) literally, by putting each \( n \) in place of \( \iota(n) \), but nothing later needs it. The order of \( \nN \) is matched to an order on \( \nZ \) in Section 10.3.

With this convention, (b) reads \( [(a, b)] = a + (-b) \): the pair \( (a, b) \) records the difference it was meant to record. The notation \( a - b \) is defined in Section 10.3, where \( x - y \coloneqq x + (-y) \) is set up in every ring at once. Clause (c) reads
\[
\nZ = \nN \cup \{ -n : n \in \nN \} ,
\]
which is word for word the definition of the integers in Section 7.1. There it was a definition inside the familiar real numbers; here it is a theorem about a set built from \( \omega \). The positive integers keep the definition of Section 7.1,
\[
\nZ_{>0} \coloneqq \{ n \in \nN : n \ne 0 \} ,
\]
which mentions only \( \nN \), and so is now a subset of \( \nZ \). In particular \( 5 + x = 3 \) has the solution \( x = [(0, 2)] = -2 \) in \( \nZ \), since \( [(5, 0)] + [(0, 2)] = [(5, 2)] = [(3, 0)] \) by @prp-integer-normal-form (a).

::: {.check}
Compute \( [(2, 5)] \cdot [(4, 1)] \) from @def-integer-operations, and write the two factors and the product as \( n \) or \( -n \) with \( n \in \nN \).
:::

::: {.solution}
\( [(2, 5)] \cdot [(4, 1)] = [(2 \cdot 4 + 5 \cdot 1, \ 2 \cdot 1 + 5 \cdot 4)] = [(13, 22)] \). By @prp-integer-normal-form (a): \( 5 = 2 + 3 \), so \( [(2, 5)] = [(0, 3)] = -3 \); \( 4 = 1 + 3 \), so \( [(4, 1)] = [(3, 0)] = 3 \); and \( 22 = 13 + 9 \), so \( [(13, 22)] = [(0, 9)] = -9 \). So the product of \( -3 \) and \( 3 \) is \( -9 \), as school predicts; here it is a computation in \( \nN \), not a rule of signs.
:::

The integers now have a sum, a product and a negative, each a function on classes, and they contain a copy of \( \nN \) with its arithmetic. Section 10.3 checks that these operations obey the usual laws, by reducing each law to a law of \( \nN \), and defines the order.

## Exercises

### A. Check your understanding

::: {#exr-well-defined-operations-a1}
[A1]

These questions are about the proof of @prp-integer-operations-well-defined.

::: {.enumerate options="label=(\alph*)"}
1. Which hypothesis of @thm-well-defined-on-classes (b) does the computation leading to @eq-integer-product-target verify?
2. Run that computation with \( (a, b) = (1, 3) \), \( (a', b') = (4, 6) \) and \( (c, d) = (2, 0) \): check that \( (a, b) \sim (a', b') \), compute both outputs, and check that they are equivalent.
3. Where in the proof are the laws of arithmetic in \( \nN \) used?
4. Give the idea of the proof in two sentences.
:::
:::

::: {.solution}
(a) The first: for all \( x, x', y \), \( x \sim x' \) implies \( g_\cdot(x, y) \sim g_\cdot(x', y) \), with \( x = (a, b) \), \( x' = (a', b') \), \( y = (c, d) \).

(b) \( 1 + 6 = 7 = 3 + 4 \), so \( (1, 3) \sim (4, 6) \). The outputs are
\[
\begin{aligned}
(ac + bd, \ ad + bc) &= (2 + 0, \ 0 + 6) = (2, 6) , \\
(a'c + b'd, \ a'd + b'c) &= (8 + 0, \ 0 + 12) = (8, 12) ,
\end{aligned}
\]
and \( 2 + 12 = 14 = 6 + 8 \), so they are equivalent. The two intermediate equations are \( ac + b'c = a'c + bc \), here \( 2 + 12 = 8 + 6 \), and \( a'd + bd = ad + b'd \), here \( 0 = 0 \), since \( d = 0 \). Both outputs are representatives of \( -4 \), and indeed \( (-2) \cdot 2 = -4 \).

(c) In every rearrangement: commutativity and associativity of \( + \) (to regroup the four-term sums), distributivity (to multiply @eq-integer-rep-change by \( c \) and by \( d \)), and commutativity of \( \cdot \) and \( + \) (in the second-argument step, to see that both formulas are symmetric in the two input pairs).

(d) A change of representative in one argument is an equation in \( \nN \), and multiplying it by \( c \) and by \( d \) and adding gives exactly the cross-sum equation for the two products. The second argument follows by symmetry of the formula, and transitivity (inside @thm-well-defined-on-classes (b)) combines the two changes.
:::

### B. Practice

::: {#exr-well-defined-operations-b1}
[B1: Two rules that pass the check]

Prove that each rule defines a function \( \nZ \to \nZ \), and identify it in terms of the operations of @def-integer-operations.

::: {.enumerate options="label=(\alph*)"}
1. \( [(a, b)] \mapsto [(b, a)] \).
2. \( [(a, b)] \mapsto [(a + b, \ a + b)] \).
:::
:::

::: {.solution}
(a) Let \( (a, b) \sim (a', b') \), that is, \( a + b' = b + a' \). The target \( (b, a) \sim (b', a') \) is \( b + a' = a + b' \), the same equation read from right to left. By @thm-well-defined-on-classes (a), the rule is a function. It is the negative \( x \mapsto -x \) of @def-integer-operations.

(b) Every output is the zero class: \( (a + b, a + b) \sim (0, 0) \), since \( (a + b) + 0 = (a + b) + 0 \). So for \( (a, b) \sim (a', b') \) the outputs \( (a + b, a + b) \) and \( (a' + b', a' + b') \) are both related to \( (0, 0) \), hence to each other by (Eq2) and (Eq3), and @thm-well-defined-on-classes (a) applies. The function is the constant map \( x \mapsto 0 \), where \( 0 = \iota(0) = [(0, 0)] \).
:::

::: {#exr-well-defined-operations-b2}
[B2: Determine which]

Determine which of the following rules define a function. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \nZ \to \nN \), \( [(a, b)] \mapsto a + b \).
2. \( \nZ \to \nZ \), \( [(a, b)] \mapsto [(2a, 2b)] \).
3. \( \nZ \to \nZ \), \( [(a, b)] \mapsto [(a^2, b^2)] \), where \( n^2 \coloneqq n \cdot n \).
:::
:::

::: {.solution}
(a) No. \( [(0, 0)] = [(1, 1)] \), since \( 0 + 1 = 0 + 1 \), but the rule gives \( 0 + 0 = 0 \) for the first representative and \( 1 + 1 = 2 \) for the second.

(b) Yes. If \( a + b' = a' + b \), then by distributivity (@thm-omega-arithmetic-laws (d))
\[
2a + 2b' = 2(a + b') = 2(a' + b) = 2a' + 2b ,
\]
which is \( (2a, 2b) \sim (2a', 2b') \); @thm-well-defined-on-classes (a) applies. The function is \( x \mapsto x + x \): \( [(a, b)] + [(a, b)] = [(a + a, b + b)] \), and \( 2n = (1 + 1)n = n + n \) by @thm-omega-arithmetic-laws (d), (e).

(c) No. \( [(0, 1)] = [(1, 2)] \), since \( 0 + 2 = 1 + 1 \). The rule gives \( [(0, 1)] \) for the first representative and \( [(1, 4)] \) for the second, and \( (0, 1) \not\sim (1, 4) \), since \( 0 + 4 = 4 \ne 2 = 1 + 1 \).
:::

### C. Going deeper

::: {#exr-well-defined-operations-c1}
[C1: Properties of classes, and an operation that half works]

::: {.enumerate options="label=(\alph*)"}
1. Prove @thm-well-defined-on-classes (c), and give an example, different from the one in the remark after the theorem, of a subset \( S \subseteq \nN \times \nN \) for which its conclusion fails for \( \sim \) of @def-integers-as-classes.
2. Give an example of an equivalence relation \( \sim \) on \( \nN \) and a function \( g \colon \nN \times \nN \to \nN \) such that the first hypothesis of @thm-well-defined-on-classes (b) holds and the second fails. Check each property, and show that no function \( G \) as in the conclusion of (b) exists for your example.
:::
:::

::: {.solution}
(a) *Proof.* Let \( x \in X \). If \( x \in S \), then \( [x] \in \bar S \) by the definition of \( \bar S \). Conversely, if \( [x] \in \bar S \), there is \( x' \in S \) with \( [x] = [x'] \); then \( x \sim x' \) (@thm-classes-partition (b)), so \( x' \sim x \) by symmetry, and the hypothesis on \( S \), applied to \( x' \sim x \) and \( x' \in S \), gives \( x \in S \).

*Example.* Let \( S \coloneqq \{ (a, b) \in \nN \times \nN : a = 0 \} \). Then \( (0, 0) \in S \), so \( [(0, 0)] \in \bar S \); and \( [(1, 1)] = [(0, 0)] \), so \( [(1, 1)] \in \bar S \), but \( (1, 1) \notin S \). The hypothesis fails at \( (0, 0) \sim (1, 1) \). Any example must contain a pair of \( S \) and an equivalent pair outside \( S \), since that is exactly the negation of the hypothesis.

(b) *Example.* On \( \nN \), let \( x \sim y \) mean "\( x = 0 \) if and only if \( y = 0 \)". This is an equivalence relation: it says that \( x \) and \( y \) have the same value under the function sending \( 0 \) to \( 0 \) and every other number to \( 1 \), so it is an equivalence relation by @exm-fibres-of-function. Its two classes are \( \{0\} \) and \( \nN \setminus \{0\} \). Let
\[
g(x, y) \coloneqq
\begin{cases}
x & \text{if } y = 1 , \\
0 & \text{if } y \ne 1 .
\end{cases}
\]
*First hypothesis holds.* Let \( x \sim x' \) and \( y \in \nN \). If \( y = 1 \), then \( g(x, y) = x \sim x' = g(x', y) \). If \( y \ne 1 \), both values are \( 0 \), and \( 0 \sim 0 \).

*Second hypothesis fails.* \( 1 \sim 2 \), since neither is \( 0 \); but \( g(5, 1) = 5 \) and \( g(5, 2) = 0 \), and \( 5 \not\sim 0 \).

*No induced \( G \).* If \( G([x], [y]) = [g(x, y)] \) held for all \( x, y \), then, since \( [1] = [2] \), we would get \( [5] = [g(5, 1)] = G([5], [1]) = G([5], [2]) = [g(5, 2)] = [0] \), and \( [5] \ne [0] \) because \( 5 \not\sim 0 \).

*What any example must have.* (i) \( \sim \) is not equality: some class has two elements \( y \sim y' \) with \( y \ne y' \), else the second hypothesis holds trivially. (ii) \( \sim \) has at least two classes, else every two outputs are related and both hypotheses hold. (iii) For some \( x \) and some \( y \sim y' \), the values \( g(x, y) \) and \( g(x, y') \) lie in different classes, while for every \( y \), changing \( x \) within its class never moves \( g(x, y) \) out of its class. A different answer can be checked against (i)–(iii).
:::

::: {#exr-well-defined-operations-c2}
[C2: One at a time or both at once]

Let \( \sim \) be an equivalence relation on \( X \) and \( g \colon X \times X \to X \) a function. Prove that the hypotheses of @thm-well-defined-on-classes (b) hold if and only if, for all \( x, x', y, y' \in X \),
\[
x \sim x' \text{ and } y \sim y' \implies g(x, y) \sim g(x', y') .
\]
Name the property of \( \sim \) that each direction uses.
:::

::: {.solution}
\( (\Rightarrow) \) Let \( x \sim x' \) and \( y \sim y' \). The first hypothesis, with \( y \) fixed, gives \( g(x, y) \sim g(x', y) \); the second, with \( x' \) fixed, gives \( g(x', y) \sim g(x', y') \). By **transitivity** (Eq3), \( g(x, y) \sim g(x', y') \). This direction is the first paragraph of the proof of @thm-well-defined-on-classes (b).

\( (\Leftarrow) \) Let \( x \sim x' \) and \( y \in X \). By **reflexivity** (Eq1), \( y \sim y \), so the displayed condition with \( y' = y \) gives \( g(x, y) \sim g(x', y) \): the first hypothesis. Likewise \( x \sim x \) and \( y \sim y' \) give \( g(x, y) \sim g(x, y') \): the second.

So the two forms are interchangeable. The one-at-a-time form is the one to check, because each check involves a single hypothesis \( x \sim x' \); the both-at-once form is the one the proof of the lemma uses.
:::

<!-- dependency ledger
thm-well-defined-on-classes (proof): a function is (graph, codomain); defining F by its graph and codomain | def-function (cited), Ch 6 Section 6.4
thm-well-defined-on-classes (proof): substitution of equals (C = [x] and C = [x'] give [x] = [x']) | def-rules-equality (Ch 4 Section 4.7), used silently
thm-well-defined-on-classes (claim): (remark) 0 < 1, so (1, 1) in S and (0, 0) not in S | thm-omega-order (a), (d), used silently
def-integer-operations (claim): (heuristic) school identities for (a - b) + (c - d), (a - b)(c - d), -(a - b) | school algebra, labelled a heuristic; no proof uses it
prp-integer-operations-well-defined (proof): rearrangements of sums of four terms, and multiplying an equation by c | thm-omega-arithmetic-laws (cited) and substitution of equals; verify/ch10/prp-integer-operations-well-defined.py
exm-ill-defined-first-coordinate (solution): 0 + 3 = 2 + 1; 0 != 1 | numeral arithmetic by def-omega-arithmetic; distinct numerals; verify/ch10/exm-ill-defined-first-coordinate.py
def-integer-operations (claim): (warning) 1 + 1 = 0 + 2; 1 + 2 != 0 + 2; [(0, 1)] * [(0, 1)] under the twisted rule | numeral arithmetic; verify/ch10/def-integer-operations.py
prp-naturals-embed-integers (claim): (identification) 0 is the empty set and not an integer | def-omega-arithmetic (c), thm-classes-partition (a) (cited)
prp-naturals-embed-integers (claim): (identification) Z>0 recalled from Section 7.1; 5 + x = 3 solved by -2 | ch07 Section 7.1 definition (recalled in prose); prp-integer-normal-form (a) (cited); verify/ch10/prp-naturals-embed-integers.py
prp-naturals-embed-integers (claim): order on Z matches order on N | Section 10.3 (prose pointer, paid by thm-integers-ordered-ring (a); nothing here depends on it)
prp-naturals-embed-integers (claim): a - b := a + (-b) | Section 10.3 (prose pointer, paid by def-commutative-ring-and-field; nothing here depends on it)
def-integer-operations (claim): (check) [(2, 5)] * [(4, 1)] = [(13, 22)] = -9 | numeral arithmetic; verify/ch10/def-integer-operations.py
exr-well-defined-operations-a1 (solution): numerical run of the key proof | numeral arithmetic; verify/ch10/exr-well-defined-operations-a1.py
exr-well-defined-operations-b2 (solution): 2n = n + n; counterexample values | thm-omega-arithmetic-laws (d), (e) (cited); verify/ch10/exr-well-defined-operations-b2.py
exr-well-defined-operations-c1 (solution): 1 ~ 2, 5 not ~ 0 | definition of the example relation; verify/ch10/exr-well-defined-operations-c1.py
-->
