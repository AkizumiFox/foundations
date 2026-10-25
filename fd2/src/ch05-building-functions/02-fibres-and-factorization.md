# Fibers and the Canonical Factorization

Section 4.2 cut a set into classes, and Section 5.1 cut functions down and glued them together. This section joins the two threads. Every function sorts its domain into piles by value, the fibers, and we prove that the piles carry all the information the function has, apart from the names of the values: every function is a quotient map, then a bijection, then an inclusion. Read in reverse, the same argument says exactly which functions on a set pass to a function on a quotient set, and gives a method for defining one.

## Functions on the clock

Section 4.2 built the clock \( \nZ/12 \), whose elements are the twelve hours \( [0], [1], \dots, [11] \). Some questions about an integer are really questions about its hour. "Is \( a \) even?" is one: \( 14 \) and \( 2 \) name the same hour, and both are even; \( 13 \) and \( 1 \) name the same hour, and both are odd. In general, let \( g \colon \nZ \to Y \) be a function with
\[
g(a) = g(a') \quad \text{whenever } 12 \mid a - a' ,
\]
so that \( g \) takes one value on each class modulo \( 12 \). Then \( g \) "is" a function of the hour: to compute it at an hour, pick any integer naming that hour and apply \( g \). The condition is stated for all pairs in one class at once. A condition such as \( g(a + 12) = g(a) \) for every \( a \) says the same thing in the end, but getting from it to \( g(a + 12k) = g(a) \) for every \( k \in \nZ \) takes an induction in each direction.

Other functions are not functions of the hour. "Is \( a \) positive?" gives different answers at \( 2 \) and at \( -10 \), which name the same hour, so no function on \( \nZ/12 \) can answer it.

There is a second way into the same idea, from the side of an arbitrary function. A function \( f \colon X \to Y \) sorts its domain: put two points in one pile when \( f \) gives them the same value. Section 4.2 met these piles as the classes of the relation \( \sim_f \) (@exm-fibres-of-function). So every function produces a quotient set of its domain.

Two questions organize the section.

- **(Q1)** Given an equivalence relation \( \sim \) on \( X \), when does a function on \( X \) pass to a function on \( X/{\sim} \), and is the function it passes to unique?
- **(Q2)** What does a function look like once its domain has been sorted by value?

We answer (Q2) first, because its answer contains the answer to (Q1).

## The fibers of a function

Recall the relation of @exm-fibres-of-function. For \( f \colon X \to Y \) and \( x, x' \in X \), \( x \sim_f x' \) means \( f(x) = f(x') \). It is an equivalence relation on \( X \), and the class of \( a \in X \) is the **fiber** of \( f \) over \( f(a) \),
\[
[a] = \{ x \in X : f(x) = f(a) \} = f^{-1}(\{ f(a) \}) ,
\]
a preimage in the sense of @def-preimage. A fiber over a point of \( Y \) that \( f \) never takes is empty, and so is not a class.

*The fibers of a function are the piles it sorts its domain into, one pile for each value it takes.*

::: {#prp-fibres-partition}
[The Fibers of a Function]

Let \( f \colon X \to Y \) be a function.

::: {.enumerate options="label=(\alph*)"}
1. The fibers \( f^{-1}(\{y\}) \) over the points \( y \in f(X) \) are exactly the classes of \( \sim_f \), and they form a partition of \( X \).
2. The rule \( y \mapsto f^{-1}(\{y\}) \) is a bijection \( f(X) \to X/{\sim_f} \). Hence \( \card{f(X)} = \card{X/{\sim_f}} \).
:::
:::

::: {.idea}
Part (a) is already proved: @exm-fibres-of-function identified the classes with the fibers, and @thm-classes-partition says the classes partition \( X \). For (b), a fiber over a value is a class, so the rule lands in \( X/{\sim_f} \); every class is the fiber over the value at its representative, which is surjectivity; and two different values have different fibers, because a point of the first fiber is not in the second.
:::

::: {.proof}
*(a)* Let \( y \in f(X) \), say \( y = f(a) \) with \( a \in X \) (@def-image). Then \( f^{-1}(\{y\}) = f^{-1}(\{f(a)\}) = [a] \), by the computation in @exm-fibres-of-function; so each such fiber is a class. Conversely, each class is \( [a] \) for some \( a \in X \), and \( [a] = f^{-1}(\{f(a)\}) \) with \( f(a) \in f(X) \). So the fibers over the points of \( f(X) \) are the elements of \( X/{\sim_f} \), and these form a partition of \( X \) by @thm-classes-partition (d).

*(b)* By (a), each \( y \in f(X) \) is sent to an element of \( X/{\sim_f} \), and to only one, so the rule is a function \( \Phi \colon f(X) \to X/{\sim_f} \) (@def-function). It is surjective: an element of \( X/{\sim_f} \) is \( [a] \) for some \( a \in X \), and \( [a] = \Phi(f(a)) \) by (a). It is injective: let \( y, y' \in f(X) \) with \( y \ne y' \), and write \( y = f(a) \) with \( a \in X \). Then \( a \in f^{-1}(\{y\}) \), while \( a \notin f^{-1}(\{y'\}) \) because \( f(a) = y \ne y' \). So \( \Phi(y) \ne \Phi(y') \), and different values have different fibers. Hence \( \Phi \) is a bijection (@def-bijective), and \( \card{f(X)} = \card{X/{\sim_f}} \) by @def-equinumerous.
:::

So a function takes exactly as many values as it has fibers, in the sense of equinumerosity: the values and the piles can be paired off. The partition remembers which points share a value, and forgets only what the values are called.

::: {.check}
List the classes of \( \sim_f \) for \( f(n) = n^2 - 2n \) on \( \{-1, 0, 1, 2, 3\} \), and match each class with its value.
:::

::: {.solution}
The values are \( f(-1) = 3 \), \( f(0) = 0 \), \( f(1) = -1 \), \( f(2) = 0 \), \( f(3) = 3 \). So the classes are \( \{-1, 3\} \) (value \( 3 \)), \( \{0, 2\} \) (value \( 0 \)) and \( \{1\} \) (value \( -1 \)): three classes for the three values in \( f(X) = \{-1, 0, 3\} \).
:::

The proposition explains a computation of Section 4.2. In @exm-same-size-subsets, the subsets of \( \{1, 2, 3\} \) were sorted by "same number of elements". That relation is \( \sim_f \) for the function \( f \colon \powerset{\{1, 2, 3\}} \to \{0, 1, 2, 3\} \) sending each subset to its number of elements, a function by @cor-finite-size-unique. Its four fibers are \( \{\emptyset\} \), the three singletons, the three pairs, and \( \{\{1, 2, 3\}\} \), and its image is all of \( \{0, 1, 2, 3\} \). Part (c) of that example, the well-defined map from classes to numbers, is the bijection of (b) read backwards.

::: {.check}
List the fibers of \( f \colon \{1, \dots, 6\} \to \{0, 1, 2\} \), where \( f(n) \) is the remainder of \( n \) on division by \( 3 \).
:::

::: {.solution}
\( f^{-1}(\{0\}) = \{3, 6\} \), \( f^{-1}(\{1\}) = \{1, 4\} \), \( f^{-1}(\{2\}) = \{2, 5\} \). Three fibers, three values; every value is taken, so \( f(X) \) is the whole codomain.
:::

## Every function factors

Now (Q2). The quotient map \( q \colon X \to X/{\sim_f} \), \( q(x) = [x] \) (@def-quotient-set), sends each point to its fiber. The bijection of @prp-fibres-partition (b) goes from values to fibers; turn it around, and it sends the fiber \( [x] \) to the value \( f(x) \). Finally, a value of \( f \) lies in the image \( f(X) \), and the **inclusion map** \( \iota \colon f(X) \to Y \), \( \iota(y) = y \) (@def-restriction-extension), puts it back into the codomain. Composed, the three maps take \( x \) to \( [x] \), to \( f(x) \), to \( f(x) \). That is \( f \).

\begin{center}
\begin{tikzpicture}[x=2.6cm, y=1cm]
  \node (X) at (0,0) {$X$};
  \node (Q) at (1,0) {$X/{\sim_f}$};
  \node (I) at (2,0) {$f(X)$};
  \node (Y) at (3,0) {$Y$};
  \draw[->] (X) -- node[above] {$q$} (Q);
  \draw[->] (Q) -- node[above] {$\bar f$} (I);
  \draw[->] (I) -- node[above] {$\iota$} (Y);
  \draw[->] (X) to[bend right=25] node[below] {$f$} (Y);
\end{tikzpicture}
\end{center}

::: {#thm-canonical-factorization}
[Canonical Factorization]

Let \( f \colon X \to Y \) be a function, let \( q \colon X \to X/{\sim_f} \) be the quotient map, and let \( \iota \colon f(X) \to Y \) be the inclusion map. There is **exactly one** function \( \bar f \colon X/{\sim_f} \to f(X) \) with
\[
f = \iota \circ \bar f \circ q .
\]
It is given by \( \bar f([x]) = f(x) \), and it is a **bijection**.
:::

::: {.idea}
[Scratch work]

The only candidate is forced. If \( \iota(\bar f(q(x))) = f(x) \), then \( \bar f([x]) = f(x) \), since \( \iota \) changes no value. So uniqueness costs nothing, and the work is to show that the forced rule is a function and a bijection. The rule \( [x] \mapsto f(x) \) reads a representative, so the first check is well-definedness, by the method of @exm-method-well-definedness. The twist is in the table's third row: injectivity is the well-definedness line read backwards.

| Givens | Goal |
|---|---|
| \( [x] = [x'] \iff x \sim_f x' \) (@thm-classes-partition (b)), and \( x \sim_f x' \iff f(x) = f(x') \) | \( \bar f \) a function, bijective, \( f = \iota \circ \bar f \circ q \), unique |
| \( [x] = [x'] \) | \( f(x) = f(x') \): one class, one value, (Fn2), well defined |
| \( f(x) = f(x') \) | \( [x] = [x'] \): injective, the same equivalence read right to left |
| \( y \in f(X) \), so \( y = f(a) \) with \( a \in X \) | \( y = \bar f([a]) \): surjective |

Uniqueness: \( q \) is onto, so every class is \( [x] \) for some \( x \); a second \( \bar f' \) with \( \iota \circ \bar f' \circ q = f \) has \( \bar f'([x]) = f(x) \) at every class. The proof writes this forwards.
:::

::: {.proof}
*A function.* Every element of \( X/{\sim_f} \) is \( [x] \) for some \( x \in X \), and \( f(x) \in f(X) \) by @def-image; this gives (Fn1). Let \( [x] = [x'] \). By @thm-classes-partition (b), \( x \sim_f x' \), that is, \( f(x) = f(x') \). So all representatives of one class give one value, which is (Fn2), and \( \bar f([x]) \coloneqq f(x) \) defines a function \( \bar f \colon X/{\sim_f} \to f(X) \) (@def-function).

*Injective.* Let \( \bar f([x]) = \bar f([x']) \), that is, \( f(x) = f(x') \). Then \( x \sim_f x' \), and \( [x] = [x'] \) by @thm-classes-partition (b).

*Surjective.* Let \( y \in f(X) \). By @def-image there is \( a \in X \) with \( f(a) = y \), and then \( \bar f([a]) = f(a) = y \).

*The factorization.* Both \( f \) and \( \iota \circ \bar f \circ q \) have domain \( X \) and codomain \( Y \), and for every \( x \in X \),
\[
(\iota \circ \bar f \circ q)(x) = \iota\bigl( \bar f([x]) \bigr) = \iota\bigl( f(x) \bigr) = f(x) ,
\]
by @def-composition. Hence \( f = \iota \circ \bar f \circ q \) by @prp-function-equality.

*Uniqueness.* Let \( \bar f' \colon X/{\sim_f} \to f(X) \) satisfy \( f = \iota \circ \bar f' \circ q \). Every element of \( X/{\sim_f} \) is \( [x] = q(x) \) for some \( x \in X \), and
\[
\bar f'([x]) = \iota\bigl( \bar f'(q(x)) \bigr) = f(x) = \bar f([x]) ,
\]
where the first equality holds because \( \iota \) sends each point to itself. The two functions have the same domain and codomain, so \( \bar f' = \bar f \) by @prp-function-equality. This proves the theorem.
:::

Read the factorization from left to right: every function is a **surjection** (\( q \), onto by @def-quotient-set), followed by a **bijection** (\( \bar f \)), followed by an **injection** (\( \iota \), which sends each point to itself, so different points stay different). All the identifying is done by \( q \), all the renaming by \( \bar f \), and all the enlarging of the target by \( \iota \). The two properties of Section 1.5 sit at the two ends. The function \( f \) is injective exactly when \( q \) is, that is, when every fiber is a single point (the second reading after @thm-classes-partition): if \( f \) is injective and \( q(x) = q(x') \), then \( f(x) = f(x') \) and \( x = x' \); if \( q \) is injective and \( f(x) = f(x') \), then \( q(x) = q(x') \) and \( x = x' \). And \( f \) is surjective exactly when \( f(X) = Y \), that is, when \( \iota = \id_Y \).

::: {.warning}
The middle map is a bijection onto the **image**, not onto the codomain. With target \( Y \), the rule \( [x] \mapsto f(x) \) is still a well-defined injection, but it is surjective only when \( f \) is. For \( f(x) = x^2 \) on \( \nR \), the rule \( [x] \mapsto x^2 \) maps the classes \( \{-x, x\} \) onto \( [0, \infty) \) and reaches no negative number of the codomain \( \nR \).
:::

The factorization also explains a failure from Section 1.5.

::: {#exm-fraction-map-factorization}
[Fractions as classes]

Let \( f \colon \nZ \times \nZ_{>0} \to \nQ \), \( f(a, b) \coloneqq a/b \). Describe \( \sim_f \), the three maps of @thm-canonical-factorization, and decide whether "send \( a/b \) to its numerator \( a \)" passes through \( q \).
:::

::: {.solution}
*The relation.* \( (a, b) \sim_f (c, d) \) means \( a/b = c/d \), and since \( b, d \ne 0 \) this holds exactly when \( ad = bc \), by the arithmetic of fractions. It is the relation of Exercise B1 in Section 4.2 (@exr-equivalence-relations-b1), now seen as the fiber relation of a function; that it is an equivalence relation is also immediate from @exm-fibres-of-function. The class of \( (1, 2) \) is the fiber over \( \tfrac12 \): the pairs \( (1, 2), (2, 4), (3, 6), \dots \), all the ways of writing one half as a fraction.

*The three maps.* The quotient map \( q \) sends a pair to its class, "the fraction \( a/b \) up to rewriting". The map \( \bar f \) sends a class to the rational number its pairs all name. And \( f \) is onto \( \nQ \), since every rational number is \( a/b \) for some \( a \in \nZ \) and \( b \in \nZ_{>0} \); so \( f(X) = \nQ \) and \( \iota = \id_\nQ \). By @thm-canonical-factorization, \( \bar f \) is a bijection from the set of classes onto \( \nQ \): a rational number "is" a class of fractions, and nothing is lost by identifying the two.

*The numerator.* Let \( p(a, b) \coloneqq a \). If \( p \) were \( g \circ q \) for some function \( g \) on the classes, then \( (a, b) \sim_f (c, d) \) would force \( p(a, b) = g([(a, b)]) = g([(c, d)]) = p(c, d) \). But \( (1, 2) \sim_f (2, 4) \), since \( 1 \cdot 4 = 2 \cdot 2 \), while \( p(1, 2) = 1 \ne 2 = p(2, 4) \). So \( p \) does not pass through \( q \), and no function on the classes, hence none on \( \nQ \), sends each fraction to its numerator. This is the failure of @exm-not-a-function (b), located: the numerator is a function of the pair, not of its fiber.
:::

::: {.check}
In @exm-fraction-map-factorization, which of \( q \), \( \bar f \), \( \iota \) are injective, and which are surjective?
:::

::: {.solution}
\( q \) is surjective, and not injective, since \( q(1, 2) = q(2, 4) \). \( \bar f \) is both, by @thm-canonical-factorization. \( \iota \) is injective, as every inclusion is; here it is \( \id_\nQ \), so it is also surjective.
:::

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
This is the canonical factorization's argument with \( \sim \) in place of \( \sim_f \) (@exm-method-well-definedness for the existence, \( q \) onto for the uniqueness). The new part is the forward direction of (a): if \( \bar g \) exists, equivalent points have one class, so \( g = \bar g \circ q \) gives them one value. For (b) and (c), translate statements about classes into statements about representatives with @thm-classes-partition (b).
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

Here is the method three times on the clock. As in Section 4.2, the subscript in \( [a]_n \) names the modulus: it is the class of \( a \) in \( \nZ/n \).

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

### A. Check your understanding

::: {#exr-fibres-and-factorization-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. For \( f \colon \nR \to \nR \), \( f(x) = x^2 - 1 \), find the fibers over \( 3 \), over \( -1 \) and over \( -2 \). Which of them are classes of \( \sim_f \)?
2. Let \( f \colon \{a, b, c, d\} \to \{1, 2, 3\} \) send \( a \) and \( c \) to \( 1 \), and \( b \) and \( d \) to \( 3 \). Write down \( X/{\sim_f} \), \( f(X) \), \( \bar f \) and \( \iota \) of @thm-canonical-factorization.
3. Which of the functions \( a \mapsto [a]_2 \), \( a \mapsto [a]_8 \) and \( a \mapsto [a^2]_8 \), from \( \nZ \), are constant on the classes of congruence modulo \( 4 \)?
:::
:::

::: {.solution}
(a) \( x^2 - 1 = 3 \) means \( x^2 = 4 \), so the fiber over \( 3 \) is \( \{-2, 2\} \). \( x^2 - 1 = -1 \) means \( x^2 = 0 \), so the fiber over \( -1 \) is \( \{0\} \). \( x^2 - 1 = -2 \) would need \( x^2 = -1 \), and no real square is negative, so the fiber over \( -2 \) is \( \emptyset \). The first two are classes, since \( 3 = f(2) \) and \( -1 = f(0) \) lie in \( f(\nR) \); the empty fiber is not a class, because \( -2 \notin f(\nR) \) and every class is non-empty (@thm-classes-partition (a)).

(b) The fibers over the values are \( \{a, c\} \) and \( \{b, d\} \), so \( X/{\sim_f} = \{ \{a, c\}, \{b, d\} \} \). The image is \( f(X) = \{1, 3\} \). The bijection is \( \bar f(\{a, c\}) = 1 \), \( \bar f(\{b, d\}) = 3 \), and \( \iota \colon \{1, 3\} \to \{1, 2, 3\} \) sends \( 1 \mapsto 1 \) and \( 3 \mapsto 3 \). The value \( 2 \) is in the codomain but outside the image, which is why \( \iota \) is not surjective.

(c) Let \( a' = a + 4k \) with \( k \in \nZ \), the general element of the class of \( a \) modulo \( 4 \).
\( a \mapsto [a]_2 \): yes, since \( a' - a = 4k = 2(2k) \).
\( a \mapsto [a]_8 \): no. \( 0 \equiv 4 \pmod 4 \), but \( [0]_8 \ne [4]_8 \), since \( 4 - 0 = 4 \) lies strictly between \( 0 \) and \( 8 \).
\( a \mapsto [a^2]_8 \): yes, since \( a'^2 - a^2 = 8ak + 16k^2 = 8(ak + 2k^2) \), with \( ak + 2k^2 \in \nZ \).
:::

### B. Practice

::: {#exr-fibres-and-factorization-b1}
[B1: The absolute value, factored]

Let \( f \colon \nR \to \nR \), \( f(x) = \abs{x} \). Describe the classes of \( \sim_f \), the image \( f(\nR) \) and the bijection \( \bar f \). Then show that \( [x] \mapsto x^2 \) is a well-defined injective function \( \nR/{\sim_f} \to \nR \).
:::

::: {.solution}
*The pieces.* \( \abs{x} = \abs{x'} \) holds exactly when \( x' = x \) or \( x' = -x \), so the class of \( x \) is \( \{-x, x\} \), which is \( \{0\} \) for \( x = 0 \). Every value \( \abs{x} \) is \( \ge 0 \), and every \( t \ge 0 \) is \( \abs{t} \), so \( f(\nR) = [0, \infty) \). The bijection of @thm-canonical-factorization is \( \bar f(\{-x, x\}) = \abs{x} \), from the set of classes onto \( [0, \infty) \).

*Well defined.* Let \( g(x) \coloneqq x^2 \). Since \( x^2 = \abs{x}^2 \), \( x \sim_f x' \) gives \( x^2 = \abs{x}^2 = \abs{x'}^2 = x'^2 \). So \( g \) is constant on classes, and \( [x] \mapsto x^2 \) is a function by @thm-functions-out-of-quotient (a).

*Injective.* Let \( x^2 = x'^2 \). Then \( \abs{x}^2 = \abs{x'}^2 \) with \( \abs{x}, \abs{x'} \ge 0 \), and @fd1:thm-squares-order, applied in both orders, gives \( \abs{x} \le \abs{x'} \) and \( \abs{x'} \le \abs{x} \). So \( \abs{x} = \abs{x'} \), that is, \( x \sim_f x' \). By @thm-functions-out-of-quotient (b), the induced function is injective. (It is not surjective onto \( \nR \): no class goes to \( -1 \).)
:::

::: {#exr-fibres-and-factorization-b2}
[B2: Same fibers]

Let \( f \colon X \to Y \) and \( g \colon X \to Z \) be functions. Prove that \( \sim_f = \sim_g \) if and only if there is a bijection \( h \colon f(X) \to g(X) \) with \( g(x) = h(f(x)) \) for every \( x \in X \).
:::

::: {.solution}
\( (\Leftarrow) \) Let \( h \) be such a bijection, and let \( x, x' \in X \). If \( f(x) = f(x') \), then \( g(x) = h(f(x)) = h(f(x')) = g(x') \). If \( g(x) = g(x') \), then \( h(f(x)) = h(f(x')) \), and \( f(x) = f(x') \) because \( h \) is injective. So \( x \sim_f x' \iff x \sim_g x' \): the two relations contain the same pairs, and are equal (@def-set-equality).

\( (\Rightarrow) \) Suppose \( \sim_f = \sim_g \); write \( \sim \) for both, so the two quotient sets are one set \( X/{\sim} \). By @thm-canonical-factorization there are bijections \( \bar f \colon X/{\sim} \to f(X) \) and \( \bar g \colon X/{\sim} \to g(X) \) with \( \bar f([x]) = f(x) \) and \( \bar g([x]) = g(x) \). The inverse \( \bar f^{-1} \colon f(X) \to X/{\sim} \) is a bijection (@def-inverse-function, @thm-bijection-iff-inverse), so \( h \coloneqq \bar g \circ \bar f^{-1} \colon f(X) \to g(X) \) is a bijection by @thm-composition-injective-surjective (c). For every \( x \in X \), \( \bar f^{-1}(f(x)) = [x] \), since \( \bar f([x]) = f(x) \); so \( h(f(x)) = \bar g([x]) = g(x) \).
:::

::: {#exr-fibres-and-factorization-b3}
[B3: A coarser relation]

Let \( \sim \) and \( \approx \) be equivalence relations on a set \( X \) such that \( x \sim x' \) implies \( x \approx x' \). Show that \( [x]_\sim \mapsto [x]_\approx \) is a well-defined surjection \( X/{\sim} \to X/{\approx} \). Give the instance \( \nZ/12 \to \nZ/4 \).
:::

::: {.solution}
Apply @thm-functions-out-of-quotient to the relation \( \sim \) and to \( g \coloneqq q_\approx \colon X \to X/{\approx} \), the quotient map of \( \approx \). It is constant on \( \sim \)-classes: if \( x \sim x' \), then \( x \approx x' \) by hypothesis, so \( [x]_\approx = [x']_\approx \) by @thm-classes-partition (b). By part (a), \( [x]_\sim \mapsto [x]_\approx \) is a function, and by part (c) it is surjective, since \( q_\approx \) is onto (@def-quotient-set).

For \( \nZ/12 \to \nZ/4 \), the hypothesis is: \( 12 \mid a - a' \) implies \( 4 \mid a - a' \). This holds by @prp-divides-transitive, since \( 4 \mid 12 \) (\( 12 = 3 \cdot 4 \)). So \( [a]_{12} \mapsto [a]_4 \) is a well-defined surjection: each hour of the clock is sent to its quarter-day position.
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

(d) **False.** Let \( g(a) \coloneqq [3a]_{12} \). It is constant on classes modulo \( 4 \): if \( a - a' = 4k \), then \( 3a - 3a' = 12k \). The induced map is injective by @thm-functions-out-of-quotient (b): if \( [3a]_{12} = [3a']_{12} \), then \( 3(a - a') = 12k \) for some \( k \in \nZ \), so \( a - a' = 4k \) after cancelling \( 3 \). But it is not surjective, so by part (c) of the theorem, look for a class that \( g \) misses. If \( [1]_{12} = [3a]_{12} \), then \( 1 - 3a = 12k \) for some \( k \in \nZ \), so \( 1 = 3(a + 4k) \) and \( 3 \mid 1 \). That is impossible: \( 1 = 0 \cdot 3 + 1 \) with \( 0 \le 1 < 3 \), so by the uniqueness in @thm-division-algorithm the remainder of \( 1 \) on division by \( 3 \) is \( 1 \), not \( 0 \). So \( [1]_{12} \) is missed. (Counting gives the same verdict: four classes cannot fill twelve.)

(e) **False.** Take \( X = Y = \nR \), \( f = \id_\nR \) and \( g(x) = 2x \). Both are injective, so \( \sim_f \) and \( \sim_g \) are both equality on \( \nR \), but \( f(1) = 1 \ne 2 = g(1) \). Equal fiber relations make the functions differ only by a renaming of values, which is Exercise B2.
:::

### C. Going deeper

::: {#exr-fibres-and-factorization-c1}
[C1: Equal fibers]

Let \( k, m, n \in \nN \), let \( X \) be a set with \( n \) elements, and let \( f \colon X \to \{1, \dots, k\} \) be a function such that the fiber \( f^{-1}(\{i\}) \) has exactly \( m \) elements for every \( i \in \{1, \dots, k\} \). Prove that \( n = km \).
:::

::: {.solution}
For \( k \in \nN \), let \( P(k) \) be the statement: for every \( n \in \nN \), every set \( X \) with \( n \) elements, and every \( f \colon X \to \{1, \dots, k\} \) all of whose fibers over \( 1, \dots, k \) have \( m \) elements, \( n = km \). We prove \( P(k) \) for every \( k \) by @fd1:ax-induction, with \( m \) fixed.

*Base case \( P(0) \).* Here \( \{1, \dots, 0\} = \emptyset \), so \( f \) is a function \( X \to \emptyset \), and \( X = \emptyset \) by @prp-empty-function (b). Then \( n = 0 \): for \( n \ge 1 \), a bijection \( \{1, \dots, n\} \to \emptyset \) would give \( 1 \) a value in \( \emptyset \). So \( n = 0 = 0 \cdot m \).

*Inductive step.* Suppose \( P(k) \), and let \( X \) have \( n \) elements and \( f \colon X \to \{1, \dots, k + 1\} \) have every fiber of \( m \) elements. Put \( X' \coloneqq f^{-1}(\{1, \dots, k\}) \) and \( F \coloneqq f^{-1}(\{k + 1\}) \). Every \( x \in X \) has \( f(x) \le k \) or \( f(x) = k + 1 \), and not both, so \( X = X' \cup F \) and \( X' \cap F = \emptyset \). By @prp-subset-finite, \( X' \) has \( j \) elements for some \( j \in \nN \). Let \( f' \colon X' \to \{1, \dots, k\} \), \( f'(x) \coloneqq f(x) \); this is a function, because \( f(x) \in \{1, \dots, k\} \) for \( x \in X' \). For \( i \le k \), its fiber is \( f'^{-1}(\{i\}) = \{ x \in X' : f(x) = i \} = f^{-1}(\{i\}) \), since every \( x \) with \( f(x) = i \) lies in \( X' \); so it has \( m \) elements. By \( P(k) \), \( j = km \). The fiber \( F \) has \( m \) elements by hypothesis, so @prp-disjoint-union-count gives that \( X = X' \cup F \) has \( km + m = (k + 1)m \) elements. Since \( X \) also has \( n \) elements, \( n = (k + 1)m \) by @cor-finite-size-unique. This proves \( P(k + 1) \).

The statement says that a function whose fibers all have one size cuts \( X \) into equal piles, so the size of \( X \) is the number of piles times the pile size. With fibers of different sizes the same induction gives the sum of the fiber sizes.
:::

::: {#exr-fibres-and-factorization-c2}
[C2: Find the error]

A student proves the uniqueness clause of @thm-functions-out-of-quotient (a) as follows.

> (1) Suppose \( \bar g \colon X/{\sim} \to Z \) and \( h \colon X/{\sim} \to Z \) both satisfy \( \bar g \circ q = g \) and \( h \circ q = g \). (2) Then \( \bar g \circ q = h \circ q \). (3) The quotient map \( q \) is injective, so \( q \) can be cancelled on the right, and \( \bar g = h \).

Is the conclusion true? Which line fails, and why? Give a counterexample to the failing step, and repair the proof.
:::

::: {.solution}
The conclusion is true: it is the uniqueness clause, proved in the text. Lines (1) and (2) are correct. Line (3) fails: \( q \) is injective only when every class is a single point (the second reading after @thm-classes-partition), which the theorem does not assume.

*Counterexample to the step.* For congruence modulo \( 12 \) on \( \nZ \), \( q(0) = [0] = [12] = q(12) \) with \( 0 \ne 12 \), so \( q \) is not injective, and the claim "\( q \) is injective" is false in the very case the clock needs.

*Repair.* What cancels \( q \) on the right is that \( q \) is **onto**. Replace (3) by: "Let \( C \in X/{\sim} \). Since \( q \) is surjective (@def-quotient-set), \( C = q(x) \) for some \( x \in X \), and then \( \bar g(C) = \bar g(q(x)) = h(q(x)) = h(C) \) by (2). The two functions have the same domain and codomain, so \( \bar g = h \) by @prp-function-equality." Injectivity of \( q \) would let one cancel \( q \) on the **left**, in \( q \circ u = q \circ v \), which is a different situation.

**Marking scheme.** (10 points)

- 2: says the conclusion is true.
- 3: identifies line (3), and says that the false step is the injectivity of \( q \).
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
prp-fibres-partition (proof): the fiber over f(a) is the class [a] | exm-fibres-of-function (cited)
prp-fibres-partition (claim): (quick check) values of n^2 - 2n on {-1, ..., 3} | arithmetic; verify/ch05/prp-fibres-partition.py
prp-fibres-partition (claim): (same-size payoff) sizes of the eight subsets of {1, 2, 3}; "number of elements" is a function | arithmetic; cor-finite-size-unique (cited); verify/ch05/prp-fibres-partition.py
prp-fibres-partition (claim): (quick check) remainders of 1, ..., 6 on division by 3 | thm-division-algorithm (F2.2), arithmetic; verify/ch05/prp-fibres-partition.py
thm-canonical-factorization (proof): the inclusion map sends each point to itself | def-restriction-extension (cited, F2.6 §01)
thm-canonical-factorization (claim): (aftermath) f injective iff every fiber is a single point | thm-classes-partition (b), its second reading (cited)
thm-canonical-factorization (claim): (warning) x^2 >= 0, every t >= 0 is a square | R arithmetic and order, square roots, school fact (AN1.1 thm-nth-root)
exm-fraction-map-factorization (solution): a/b = c/d iff ad = bc for b, d != 0; every rational is a/b with b > 0 | arithmetic of fractions, school fact (Q built in F3.2); verify/ch05/exm-fraction-map-factorization.py
exm-clock-maps (solution): remainder test a = a' (mod n) iff same remainder | prose after prp-integers-mod-n (F2.5 §02), recalled with a pointer
exm-clock-maps (solution): 2 is not a multiple of 12; (a + 1) - (a' + 1) = a - a' | prp-integers-closed (c) (cited); R arithmetic; verify/ch05/exm-clock-maps.py
thm-functions-out-of-quotient (claim): (warning) 24 | d implies 12 | d; 12 is not a multiple of 24 | arithmetic (d = 24k = 12(2k)); 0 < 12 < 24 with prp-integers-closed (c); verify/ch05/exm-clock-maps.py
thm-functions-out-of-quotient (claim): (quick check) 10k = 5(2k); 5 not a multiple of 10 | arithmetic; prp-integers-closed (c); verify/ch05/exm-clock-maps.py
exm-method-factor-through-quotient (claim): (second reading) the remainder picks a representative of each class mod n | prp-integers-mod-n (cited)
exr-fibres-and-factorization-a1 (solution): fibers of x^2 - 1; no real square is negative; 8ak + 16k^2 = 8(ak + 2k^2); 4 not a multiple of 8 | R arithmetic and order, school fact; verify/ch05/exr-fibres-and-factorization-a1.py
exr-fibres-and-factorization-b1 (solution): |x| = |x'| iff x' = x or x' = -x; |x| >= 0; x^2 = |x|^2; t = |t| for t >= 0 | R arithmetic and order, school fact
exr-fibres-and-factorization-b4 (solution): cancelling 3 in 3(a - a') = 12k; 1 = 0 * 3 + 1 | R arithmetic (a product with a non-zero factor), school fact; thm-division-algorithm (cited); verify/ch05/exr-fibres-and-factorization-b4.py
exr-fibres-and-factorization-c1 (solution): f(x) <= k or f(x) = k + 1, not both, for f(x) in {1, ..., k + 1}; km + m = (k + 1)m | lem-naturals-arithmetic (F2.2), arithmetic
exr-fibres-and-factorization-c1 (solution): 1 is in {1, ..., n} for n >= 1 | lem-naturals-arithmetic (F2.2), with def-finite
exr-fibres-and-factorization-c3 (solution): (x^2)^2 = x^4; 1^3 = 1, (-1)^3 = -1, (-1)^2 = 1 | R arithmetic, school fact
exm-clock-maps (claim): (Looking ahead) the tick iterated, its orbit the whole clock | F2.6 §04 (prose pointer, same chapter; paid by the tick Quick check after exm-method-follow-the-orbit and the 12-cycle example after def-permutation-cycle; nothing here depends on it)
-->
