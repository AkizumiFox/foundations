# Parked: from old Section 5.2, Fibers and the Canonical Factorization

<!-- Parked from fd2 (layout-six-chapters.md §2, approved 2026-10-26). Not part of any book's src; nothing builds or scans it.
Old section: fd2 5.2 (02-fibres-and-factorization.md); the fibres and the factorization moved to 5.2
Labels: thm-functions-out-of-quotient, exm-method-factor-through-quotient, exm-clock-maps, exr-fibres-and-factorization-b1, -b3, -b4, -c2, -c3
Intended home: ST.1
-->

Old opening frame:

Section 4.2 cut a set into classes, and Section 5.1 cut functions down and glued them together. This section joins the two threads. Every function sorts its domain into piles by value, the fibers, and we prove that the piles carry all the information the function has, apart from the names of the values: every function is a quotient map, then a bijection, then an inclusion. Read in reverse, the same argument says exactly which functions on a set pass to a function on a quotient set, and gives a method for defining one.

## Functions out of a quotient

Now (Q1). The canonical factorization built a function on the classes of \( \sim_f \) from \( f \) itself. Nothing in its first step needed the relation to come from \( f \): what made \( [x] \mapsto f(x) \) a function was only that equivalent points have equal values. So the same argument works for any equivalence relation, as long as the function is constant on its classes.

::: {#thm-functions-out-of-quotient}
[Functions out of a Quotient]

Let \( \sim \) be an equivalence relation on a set \( X \), let \( q \colon X \to X/{\sim} \) be its quotient map, and let \( g \colon X \to Z \) be a function.

::: {.enumerate options="label=(\alph*)"}
1. There is a function \( \bar g \colon X/{\sim} \to Z \) with \( \bar g \circ q = g \) **if and only if** \( g \) is **constant on classes**: for all \( x, x' \in X \), if \( x \sim x' \), then \( g(x) = g(x') \). In that case \( \bar g \) is unique, and \( \bar g([x]) = g(x) \).
2. Suppose \( g \) is constant on classes. Then \( \bar g \) is injective **if and only if**, for all \( x, x' \in X \), \( g(x) = g(x') \) implies \( x \sim x' \).
3. Suppose \( g \) is constant on classes. Then \( \bar g \) is surjective **if and only if** \( g \) is surjective.
:::
:::

::: {.idea}
This is the argument of @thm-canonical-factorization with \( \sim \) in place of \( \sim_f \) (@exm-method-well-definedness for the existence, \( q \) onto for the uniqueness). The new part is the forward direction of (a): if \( \bar g \) exists, equivalent points have one class, so \( g = \bar g \circ q \) gives them one value. For (b) and (c), translate statements about classes into statements about representatives with @thm-classes-partition (b).
:::

::: {.proof}
*(a)* \( (\Rightarrow) \) Suppose \( \bar g \circ q = g \), and let \( x \sim x' \). Then \( q(x) = [x] = [x'] = q(x') \) by @thm-classes-partition (b), so
\[
g(x) = \bar g(q(x)) = \bar g(q(x')) = g(x') .
\]

\( (\Leftarrow) \) Suppose \( g \) is constant on classes. Every element of \( X/{\sim} \) is \( [x] \) for some \( x \in X \), with \( g(x) \in Z \), which is (Fn1). If \( [x] = [x'] \), then \( x \sim x' \) by @thm-classes-partition (b), so \( g(x) = g(x') \), which is (Fn2). Hence \( \bar g([x]) \coloneqq g(x) \) defines a function \( \bar g \colon X/{\sim} \to Z \) (@def-function). Both \( \bar g \circ q \) and \( g \) have domain \( X \) and codomain \( Z \), and \( (\bar g \circ q)(x) = \bar g([x]) = g(x) \) for every \( x \in X \), so \( \bar g \circ q = g \) by @prp-function-equality.

*Uniqueness.* If \( h \colon X/{\sim} \to Z \) also satisfies \( h \circ q = g \), then each element of \( X/{\sim} \) is \( q(x) \) for some \( x \in X \), since \( q \) is onto (@def-quotient-set), and \( h(q(x)) = g(x) = \bar g(q(x)) \). So \( h = \bar g \) by @prp-function-equality.

*(b)* By @def-injective, \( \bar g \) is injective when \( \bar g(C) = \bar g(D) \) implies \( C = D \) for all \( C, D \in X/{\sim} \). Every class is \( [x] \) for some \( x \in X \), and \( \bar g([x]) = g(x) \); so the condition reads: for all \( x, x' \in X \), \( g(x) = g(x') \) implies \( [x] = [x'] \). By @thm-classes-partition (b), \( [x] = [x'] \) is \( x \sim x' \).

*(c)* By @def-surjective, \( \bar g \) is surjective when every \( z \in Z \) is \( \bar g(C) \) for some class \( C \). Since every class is \( [x] \) for some \( x \in X \), and \( \bar g([x]) = g(x) \), this says that every \( z \in Z \) is \( g(x) \) for some \( x \in X \): that \( g \) is surjective.
:::

The canonical factorization is the case where \( \sim \) is \( \sim_f \), with \( g \) the function \( X \to f(X) \), \( x \mapsto f(x) \). That \( g \) is constant on the classes of \( \sim_f \) by the definition of \( \sim_f \); the converse condition of (b) holds for the same reason, so \( \bar g \) is injective; and \( g \) is onto \( f(X) \) by @def-image, so \( \bar g \) is surjective by (c). The map \( \bar g \) is \( \bar f \).

::: {.warning}
"Constant on classes" runs from equivalence to equal values: \( x \sim x' \Rightarrow g(x) = g(x') \). Its converse, \( g(x) = g(x') \Rightarrow x \sim x' \), is the injectivity condition of (b), and checking it instead proves nothing about existence. For congruence modulo \( 12 \) and \( g(a) = [a]_{24} \), the converse holds, since \( 24 \mid a - a' \) gives \( 12 \mid a - a' \); but \( 0 \equiv 12 \pmod{12} \) while \( [0]_{24} \ne [12]_{24} \), so "\( [a]_{12} \mapsto [a]_{24} \)" is not a function.
:::

The theorem turns the check of @exm-method-well-definedness into a complete method: it says what the check buys, and how to read off injectivity and surjectivity afterwards.

::: {#exm-method-factor-through-quotient}
[Method: define a function on a quotient]

**Template.** (1) Write the function \( g \) on \( X \) that the rule computes from a representative. (2) Check that \( g \) is constant on classes (@exm-method-well-definedness). (3) Conclude by @thm-functions-out-of-quotient: \( \bar g \) exists, is unique, and \( \bar g \circ q = g \). (4) Read injectivity of \( \bar g \) as "equal values force equivalence", and surjectivity of \( \bar g \) as surjectivity of \( g \).

**When to use it.** Maps out of \( \nZ/n \), out of classes of fractions, out of any "the same in some respect".

**The usual failure.** Proving (4)'s converse condition instead of (2); a \( g \) not defined on all of \( X \); running the check for a map **into** a quotient, which needs none: compose with \( q \).
:::

Here is the method three times, twice on the clock and once on \( \nZ/2 \). As in Section 4.2, the subscript in \( [a]_n \) names the modulus: it is the class of \( a \) in \( \nZ/n \).

::: {#exm-clock-maps}
[Maps out of the clock]

(a) Let \( r \colon \nZ \to \{0, 1\} \) send each integer to its remainder on division by \( 2 \). Show that "\( [a]_{12} \mapsto r(a) \)" is a function \( \nZ/12 \to \{0, 1\} \), and decide whether it is injective and whether it is surjective.

(b) Do the same for "\( [a]_2 \mapsto r(a) \)", from \( \nZ/2 \).

(c) Show that "\( [a]_{12} \mapsto [a + 1]_{12} \)" is a bijection \( t \colon \nZ/12 \to \nZ/12 \).
:::

::: {.solution}
The remainder \( r(a) \) is well defined by the uniqueness in @thm-division-algorithm. We use the remainder test of Section 4.2, after @prp-integers-mod-n: \( a \equiv a' \pmod{n} \) if and only if \( a \) and \( a' \) leave the same remainder on division by \( n \).

(a) *Step (1).* The rule computes \( r(a) \) from the representative \( a \), so \( g = r \). *Step (2).* Let \( a \equiv a' \pmod{12} \), so \( a - a' = 12k \) with \( k \in \nZ \). Then \( a - a' = 2(6k) \) with \( 6k \in \nZ \), so \( a \equiv a' \pmod 2 \), and \( r(a) = r(a') \) by the remainder test. *Step (3).* By @thm-functions-out-of-quotient (a), \( \bar r([a]_{12}) \coloneqq r(a) \) is a function \( \nZ/12 \to \{0, 1\} \): "is the hour even?" is a question about the hour. *Step (4).* It is surjective by @thm-functions-out-of-quotient (c), since \( r(0) = 0 \) and \( r(1) = 1 \). It is not injective, by part (b) of the theorem: \( r(0) = r(2) \), but \( 0 \not\equiv 2 \pmod{12} \), since \( 2 - 0 = 2 \) lies strictly between \( 0 \) and \( 12 \) and so is not a multiple of \( 12 \) (@prp-integers-closed (c)). So \( \bar r([0]_{12}) = \bar r([2]_{12}) \) with \( [0]_{12} \ne [2]_{12} \).

(b) *Step (2).* If \( a \equiv a' \pmod 2 \), then \( r(a) = r(a') \) by the remainder test. *Step (4).* Conversely, \( r(a) = r(a') \) gives \( a \equiv a' \pmod 2 \), again by the remainder test, so the induced map \( \nZ/2 \to \{0, 1\} \) is injective by @thm-functions-out-of-quotient (b), and surjective by part (c), as in (a). It is a bijection: the two classes of \( \nZ/2 \) are the even and the odd integers, matched with the remainders \( 0 \) and \( 1 \).

(c) *Steps (1)–(3).* Here \( g(a) \coloneqq [a + 1]_{12} \), a function \( \nZ \to \nZ/12 \). If \( a - a' = 12k \), then \( (a + 1) - (a' + 1) = a - a' = 12k \), so \( [a + 1]_{12} = [a' + 1]_{12} \) (@thm-classes-partition (b)). So \( t([a]_{12}) \coloneqq [a + 1]_{12} \) is a function \( \nZ/12 \to \nZ/12 \), the **tick** of the clock. *A bijection.* In the same way, \( (a - 1) - (a' - 1) = a - a' \), so \( s([a]_{12}) \coloneqq [a - 1]_{12} \) is a function \( \nZ/12 \to \nZ/12 \). For every \( a \in \nZ \), \( s(t([a])) = s([a + 1]) = [a] \) and \( t(s([a])) = t([a - 1]) = [a] \); so \( s \circ t \) and \( t \circ s \) are the identity of \( \nZ/12 \) (@prp-function-equality), and \( t \) is a bijection with inverse \( s \) (@thm-bijection-iff-inverse).
:::

In (c) the codomain is itself a quotient set, and the check compared outputs as classes. In (a) and (b) the codomain is \( \{0, 1\} \), and outputs were compared as numbers. Step (2) of the method is the same check in both cases; only the meaning of "equal outputs" changes with the codomain.

::: {.second-reading title="Surjections are quotient maps, and choosing representatives"}
If \( f \colon X \to Y \) is onto, then \( \iota = \id_Y \), and @thm-canonical-factorization reads \( f = \bar f \circ q \) with \( \bar f \colon X/{\sim_f} \to Y \) a bijection. So every surjection is a quotient map up to renaming the classes: to give an onto map out of \( X \) is to give an equivalence relation on \( X \) and names for its classes. In the other direction, \( q \) itself is onto, so it has a right inverse \( c \colon X/{\sim} \to X \) by @thm-surjection-right-inverse, which uses @ax-choice. Then \( q(c(C)) = C \), that is, \( c(C) \in C \) for every class \( C \): a right inverse of a quotient map is a choice of one representative from each class. For \( \nZ/n \) no axiom is needed, since the remainder picks one, \( c([a]) \coloneqq \) the remainder of \( a \) on division by \( n \) (@prp-integers-mod-n).
:::

::: {.check}
Is the rule \( [a]_{10} \mapsto [a]_5 \) a well-defined function \( \nZ/10 \to \nZ/5 \)? Is it injective? Is it surjective?
:::

::: {.solution}
Take \( g \colon \nZ \to \nZ/5 \), \( g(a) = [a]_5 \). *Well defined:* yes. If \( a - a' = 10k \) with \( k \in \nZ \), then \( a - a' = 5(2k) \), so \( g(a) = g(a') \) (this was Exercise B3 (c) of Section 4.2). *Injective:* no. \( g(0) = [0]_5 = [5]_5 = g(5) \), but \( 0 \not\equiv 5 \pmod{10} \), since \( 0 < 5 < 10 \); by @thm-functions-out-of-quotient (b), the classes \( [0]_{10} \ne [5]_{10} \) have one image. *Surjective:* yes, by (c), because \( g \) is the quotient map of congruence modulo \( 5 \), which is onto.
:::

::: {.remark}
[Looking ahead]

Later in this chapter, in the section on permutations and iteration, the tick \( t \) of @exm-clock-maps is applied again and again; its iterates carry each hour once round the whole clock.
:::

## Exercises

::: {#exr-fibres-and-factorization-b1}
[B1: The absolute value, factored]

Let \( f \colon \nR \to \nR \), \( f(x) = \abs{x} \). Describe the classes of \( \sim_f \), the image \( f(\nR) \) and the bijection \( \bar f \). Then show that \( [x] \mapsto x^2 \) is a well-defined injective function \( \nR/{\sim_f} \to \nR \).
:::

::: {.solution}
*The pieces.* \( \abs{x} = \abs{x'} \) holds exactly when \( x' = x \) or \( x' = -x \), so the class of \( x \) is \( \{-x, x\} \), which is \( \{0\} \) for \( x = 0 \). Every value \( \abs{x} \) is \( \ge 0 \), and every \( t \ge 0 \) is \( \abs{t} \), so \( f(\nR) = [0, \infty) \). The bijection of @thm-canonical-factorization is \( \bar f(\{-x, x\}) = \abs{x} \), from the set of classes onto \( [0, \infty) \).

*Well defined.* Let \( g(x) \coloneqq x^2 \). Since \( x^2 = \abs{x}^2 \), \( x \sim_f x' \) gives \( x^2 = \abs{x}^2 = \abs{x'}^2 = x'^2 \). So \( g \) is constant on classes, and \( [x] \mapsto x^2 \) is a function by @thm-functions-out-of-quotient (a).

*Injective.* Let \( x^2 = x'^2 \). Then \( \abs{x}^2 = \abs{x'}^2 \) with \( \abs{x}, \abs{x'} \ge 0 \), and @fd1:thm-squares-order, applied in both orders, gives \( \abs{x} \le \abs{x'} \) and \( \abs{x'} \le \abs{x} \). So \( \abs{x} = \abs{x'} \), that is, \( x \sim_f x' \). By @thm-functions-out-of-quotient (b), the induced function is injective. (It is not surjective onto \( \nR \): no class goes to \( -1 \).)
:::

::: {#exr-fibres-and-factorization-b3}
[B3: A coarser relation]

Let \( \sim \) and \( \approx \) be equivalence relations on a set \( X \) such that \( x \sim x' \) implies \( x \approx x' \). Show that \( [x]_\sim \mapsto [x]_\approx \) is a well-defined surjection \( X/{\sim} \to X/{\approx} \). Give the instance \( \nZ/12 \to \nZ/4 \).
:::

::: {.solution}
Apply @thm-functions-out-of-quotient to the relation \( \sim \) and to \( g \coloneqq q_\approx \colon X \to X/{\approx} \), the quotient map of \( \approx \). It is constant on \( \sim \)-classes: if \( x \sim x' \), then \( x \approx x' \) by hypothesis, so \( [x]_\approx = [x']_\approx \) by @thm-classes-partition (b). By part (a), \( [x]_\sim \mapsto [x]_\approx \) is a function, and by part (c) it is surjective, since \( q_\approx \) is onto (@def-quotient-set).

For \( \nZ/12 \to \nZ/4 \), the hypothesis is: \( 12 \mid a - a' \) implies \( 4 \mid a - a' \). This holds by @prp-divides-transitive, since \( 4 \mid 12 \) (\( 12 = 3 \cdot 4 \)). So \( [a]_{12} \mapsto [a]_4 \) is a well-defined surjection: each hour is sent to its position within a block of four hours (\( 0 \), \( 4 \) and \( 8 \) go to \( [0]_4 \)).
:::

::: {#exr-fibres-and-factorization-b4}
[B4: Prove or disprove]

Prove or disprove each statement.

::: {.enumerate options="label=(\alph*)"}
1. If \( g \colon X \to Z \) is constant on the classes of an equivalence relation \( \sim \) on \( X \) and \( g \) is surjective, then \( \bar g \colon X/{\sim} \to Z \) is a bijection.
2. For every function \( f \colon X \to Y \), \( \card{f(X)} = \card{X/{\sim_f}} \).
3. If \( f \colon X \to Y \) is injective, then the quotient map \( X \to X/{\sim_f} \) is a bijection.
4. The rule \( [a]_4 \mapsto [3a]_{12} \) is a bijection \( \nZ/4 \to \nZ/12 \).
5. If \( f, g \colon X \to Y \) satisfy \( \sim_f = \sim_g \), then \( f = g \).
:::
:::

::: {.solution}
(a) **False.** Let \( X = \{1, 2\} \), let \( \sim \) be equality, and let \( g \colon X \to \{0\} \) be the constant function. It is constant on classes (every function is, for equality) and surjective. But \( \bar g([1]) = 0 = \bar g([2]) \) with \( [1] = \{1\} \ne \{2\} = [2] \), so \( \bar g \) is not injective. Surjectivity of \( g \) gives surjectivity of \( \bar g \) only, by @thm-functions-out-of-quotient (c).

(b) **True.** This is @prp-fibres-partition (b).

(c) **True.** If \( x \sim_f x' \), then \( f(x) = f(x') \), so \( x = x' \) by injectivity; hence \( [x] = \{x\} \) for every \( x \). The quotient map \( q \) is injective: \( q(x) = q(x') \) gives \( x \sim_f x' \) by @thm-classes-partition (b), so \( x = x' \). And \( q \) is onto by @def-quotient-set.

(d) **False.** Let \( g(a) \coloneqq [3a]_{12} \). It is constant on classes modulo \( 4 \): if \( a - a' = 4k \), then \( 3a - 3a' = 12k \). The induced map is injective by @thm-functions-out-of-quotient (b): if \( [3a]_{12} = [3a']_{12} \), then \( 3(a - a') = 12k \) for some \( k \in \nZ \), so \( a - a' = 4k \) after cancelling \( 3 \). But it is not surjective, so by part (c) of the theorem, look for a class that \( g \) misses. If \( [1]_{12} = [3a]_{12} \), then \( 1 - 3a = 12k \) for some \( k \in \nZ \), so \( 1 = 3(a + 4k) \) and \( 3 \mid 1 \). That is impossible: \( 1 = 0 \cdot 3 + 1 \) with \( 0 \le 1 < 3 \), so by the uniqueness in @thm-division-algorithm the remainder of \( 1 \) on division by \( 3 \) is \( 1 \), not \( 0 \). So \( [1]_{12} \) is missed.

(e) **False.** Take \( X = Y = \nR \), \( f = \id_\nR \) and \( g(x) = 2x \). Both are injective, so \( \sim_f \) and \( \sim_g \) are both equality on \( \nR \), but \( f(1) = 1 \ne 2 = g(1) \). Equal fiber relations make the functions differ only by a renaming of values, which is Exercise B2.
:::

::: {#exr-fibres-and-factorization-c2}
[C2: Find the error]

A student proves the uniqueness clause of @thm-functions-out-of-quotient (a) as follows.

> (1) Suppose \( \bar g \colon X/{\sim} \to Z \) and \( h \colon X/{\sim} \to Z \) both satisfy \( \bar g \circ q = g \) and \( h \circ q = g \). (2) Then \( \bar g \circ q = h \circ q \). (3) The quotient map \( q \) is injective, so \( q \) can be cancelled on the right, and \( \bar g = h \).

Is the conclusion true? Which line fails, and why? Give a counterexample to the failing step, and repair the proof.
:::

::: {.solution}
The conclusion is true: it is the uniqueness clause, proved in the text. Lines (1) and (2) are correct. Line (3) fails twice. First, \( q \) is injective only when every class is a single point (the second reading after @thm-classes-partition), which the theorem does not assume. Second, even for an injective map \( p \), \( u \circ p = v \circ p \) need not give \( u = v \).

*Counterexample to the step.* For congruence modulo \( 12 \) on \( \nZ \), \( q(0) = [0] = [12] = q(12) \) with \( 0 \ne 12 \), so \( q \) is not injective, and the claim "\( q \) is injective" is false in the very case the clock needs. *Counterexample to the inference.* The inclusion \( \iota \colon \{0\} \to \{0, 1\} \) is injective; let \( u = \id_{\{0, 1\}} \) and \( v \) be the constant function \( 0 \). Then \( u \circ \iota = v \circ \iota \) but \( u \ne v \).

*Repair.* What cancels \( q \) on the right is that \( q \) is **onto**. Replace (3) by: "Let \( C \in X/{\sim} \). Since \( q \) is surjective (@def-quotient-set), \( C = q(x) \) for some \( x \in X \), and then \( \bar g(C) = \bar g(q(x)) = h(q(x)) = h(C) \) by (2). The two functions have the same domain and codomain, so \( \bar g = h \) by @prp-function-equality." Injectivity of \( q \) would let one cancel \( q \) on the **left**, in \( q \circ u = q \circ v \), which is a different situation.

**Marking scheme.** (10 points)

- 2: says the conclusion is true.
- 3: identifies line (3), and says either that \( q \) need not be injective or that injectivity does not license cancelling on the right (surjectivity does).
- 2: gives a concrete non-injective quotient map, such as \( q(0) = q(12) \) modulo \( 12 \).
- 3: repairs the proof by surjectivity of \( q \): every class is \( q(x) \), where both functions take the value \( g(x) \).

Fatal errors (0 for the step): calling the conclusion false; a repair that assumes classes are singletons.
:::

::: {#exr-fibres-and-factorization-c3}
[C3: Exit check: depends only on f]

Let \( f \colon X \to Y \) and \( g \colon X \to Z \) be functions such that, for all \( x, x' \in X \), \( f(x) = f(x') \) implies \( g(x) = g(x') \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that there is exactly one function \( h \colon f(X) \to Z \) with \( g(x) = h(f(x)) \) for every \( x \in X \).
2. For \( f \colon \nR \to \nR \), \( f(x) = x^2 \), decide whether \( g(x) = x^4 \) and whether \( g(x) = x^3 \) are of the form \( h \circ f \) for some function \( h \colon f(\nR) \to \nR \).
:::
:::

::: {.solution}
(a) *Existence.* The hypothesis says that \( g \) is constant on the classes of \( \sim_f \). By @thm-functions-out-of-quotient (a), there is a function \( \bar g \colon X/{\sim_f} \to Z \) with \( \bar g([x]) = g(x) \). By @thm-canonical-factorization, \( \bar f \colon X/{\sim_f} \to f(X) \), \( \bar f([x]) = f(x) \), is a bijection, so it has an inverse \( \bar f^{-1} \colon f(X) \to X/{\sim_f} \) (@thm-bijection-iff-inverse), and \( \bar f^{-1}(f(x)) = [x] \) for every \( x \in X \). Put \( h \coloneqq \bar g \circ \bar f^{-1} \). Then, for every \( x \in X \),
\[
h(f(x)) = \bar g\bigl( \bar f^{-1}(f(x)) \bigr) = \bar g([x]) = g(x) .
\]

*Uniqueness.* Let \( h, h' \colon f(X) \to Z \) both satisfy the condition. Let \( y \in f(X) \); by @def-image, \( y = f(x) \) for some \( x \in X \). Then \( h(y) = g(x) = h'(y) \). The two functions have the same domain and codomain, so \( h = h' \) by @prp-function-equality.

(b) \( g(x) = x^4 \) is of this form: \( x^4 = (x^2)^2 \), so \( h(t) \coloneqq t^2 \) on \( f(\nR) \) works, and by (a) it is the only such \( h \). \( g(x) = x^3 \) is not: if \( x^3 = h(x^2) \) for every \( x \), then \( 1 = 1^3 = h(1) = h((-1)^2) = (-1)^3 = -1 \), which is false. The hypothesis of (a) fails at the pair \( 1, -1 \): \( f(1) = f(-1) \), while \( g(1) \ne g(-1) \).

**Marking scheme.** (10 points)

- 2: recognizes the hypothesis as "\( g \) is constant on the classes of \( \sim_f \)" and obtains \( \bar g \) with \( \bar g([x]) = g(x) \) (or defines \( h(f(x)) \coloneqq g(x) \) directly and checks it is well defined).
- 2: uses the bijection \( \bar f \) onto \( f(X) \), or an equivalent argument, so that \( h \) is defined at **every** point of \( f(X) \) and only there.
- 2: verifies \( h(f(x)) = g(x) \) for every \( x \).
- 2: uniqueness, using that every point of \( f(X) \) is a value \( f(x) \).
- 2: part (b): \( h(t) = t^2 \) for \( x^4 \); the witness pair \( 1, -1 \) for \( x^3 \).

A direct proof that defines \( h(y) \coloneqq g(x) \) for any \( x \) with \( f(x) = y \) earns the first two steps if it checks that the value does not depend on the choice of \( x \) (that is the hypothesis) and that every \( y \in f(X) \) has such an \( x \). Fatal errors (0 for the step): defining \( h \) on all of \( Y \) without a value for points outside \( f(X) \); proving the converse implication \( g(x) = g(x') \Rightarrow f(x) = f(x') \) instead of using the hypothesis.
:::

<!-- dependency ledger
exm-clock-maps (solution): remainder test a = a' (mod n) iff same remainder | prose after prp-integers-mod-n (F2.5 §02), recalled with a pointer
exm-clock-maps (solution): 2 is not a multiple of 12; (a + 1) - (a' + 1) = a - a' | prp-integers-closed (c) (cited); R arithmetic; fd2/authoring/parked/st/verify/exm-clock-maps.py
thm-functions-out-of-quotient (claim): (warning) 24 | d implies 12 | d; 12 is not a multiple of 24 | arithmetic (d = 24k = 12(2k)); 0 < 12 < 24 with prp-integers-closed (c); fd2/authoring/parked/st/verify/exm-clock-maps.py
thm-functions-out-of-quotient (claim): (quick check) 10k = 5(2k); 5 not a multiple of 10 | arithmetic; prp-integers-closed (c); fd2/authoring/parked/st/verify/exm-clock-maps.py
exm-method-factor-through-quotient (claim): (second reading) the remainder picks a representative of each class mod n | prp-integers-mod-n (cited)
exr-fibres-and-factorization-b1 (solution): |x| = |x'| iff x' = x or x' = -x; |x| >= 0; x^2 = |x|^2; t = |t| for t >= 0 | R arithmetic and order, school fact
exr-fibres-and-factorization-b4 (solution): cancelling 3 in 3(a - a') = 12k; 1 = 0 * 3 + 1 | R arithmetic (a product with a non-zero factor), school fact; thm-division-algorithm (cited); fd2/authoring/parked/st/verify/exr-fibres-and-factorization-b4.py
exr-fibres-and-factorization-c3 (solution): (x^2)^2 = x^4; 1^3 = 1, (-1)^3 = -1, (-1)^2 = 1 | R arithmetic, school fact
exm-clock-maps (claim): (Looking ahead) the tick iterated, its orbit the whole clock | F2.6 §04 (prose pointer, same chapter; paid by the tick Quick check after exm-method-follow-the-orbit and the 12-cycle example after def-permutation-cycle; nothing here depends on it)
-->
