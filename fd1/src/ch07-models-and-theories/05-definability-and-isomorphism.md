# Definability and Isomorphism

A sentence is true or false in a structure. A formula with one free variable is different: it is true of some elements of a structure and false of others, so it picks out a set. In \( (\nN; +) \) the formula \( \exists y\, (x = y + y) \) is true of \( 0, 2, 4, \dots \) and false of the odd numbers, so it picks out the even numbers, although the structure has no symbol for "even". This section asks which sets a structure's language can pick out. Its first half writes formulas for sets: points, intervals, orders, the primes, a supremum. Its second half, for a second reading, asks why some sets cannot be picked out at all, and answers with a map that moves the elements of a structure without changing anything a formula can see.

::: {.remark}
[Looking back]

Section 4.9 asked what the connectives can say, and answered: every truth function, by a normal form. This section asks the same question of a first-order language inside one structure. There the answer was "everything"; here it depends on the structure, and a set that one structure's formulas define, another's cannot.
:::

## Formulas define sets

*A formula defines the set of elements (or tuples of elements) that make it true.*

::: {#def-definable-set}
[Definable Set]

Let \( \fM \) be a structure with domain \( D \), and \( \varphi \) a formula whose free variables are among \( x_1, \dots, x_n \), all different. The set **defined by** \( \varphi \) in \( \fM \) is
\[
\{ (d_1, \dots, d_n) \in D^n : \fM, \ell[x_1 \mapsto d_1] \cdots [x_n \mapsto d_n] \models \varphi \} ,
\]
for any assignment \( \ell \). A set \( S \subseteq D^n \) is **definable** in \( \fM \) if some formula defines it.
:::

By @lem-free-coincidence the set does not depend on \( \ell \): the assignments \( \ell[x_1 \mapsto d_1] \cdots [x_n \mapsto d_n] \), for different \( \ell \), agree on \( x_1, \dots, x_n \), and only the values of the free variables matter. For \( n = 1 \) the set is a set of elements, and we write it in set-builder form, \( \{ x \in D : \varphi \} \). Set-builder notation, used since school, is exactly this: the reading of a formula in a structure.

Two remarks on the definition. The structure is part of the question: the same formula defines different sets in different structures, and a set is definable **in** \( \fM \), never definable outright. And the formula may use only the symbols of \( \fM \): to define a set in \( (\nN; +) \) we may write \( + \), \( = \), connectives and quantifiers, and nothing else, not even \( 0 \) or \( < \).

The connectives act on defined sets as the set operations do. If \( \varphi \) and \( \psi \) define \( S \) and \( T \) (with the same free variable \( x \)), then by (S4) and (S5) the formula \( \varphi \wedge \psi \) defines \( S \cap T \), \( \varphi \vee \psi \) defines \( S \cup T \), and \( \neg\varphi \) defines \( D \setminus S \), the elements not in \( S \). So the definable sets of a structure are closed under intersection, union and complement, and a set built from definable sets by these operations is definable without further work.

::: {#exm-definable-sets}
[Sets Defined by Formulas]

Each formula is read back in words.

::: {.enumerate options="label=(\alph*)"}
1. In \( (\nR; +, \cdot) \), the formula \( \exists y\, (x = y \cdot y) \), "\( x \) is a square", defines \( [0, \infty) \): a real number is the square of a real number exactly when it is non-negative.
2. In \( (\nN; +) \), the formula \( x + x = x \), "\( x \) added to itself gives itself", defines \( \{ 0 \} \), since \( d + d = d \) forces \( d = 0 \). The formula \( \exists z\, (\neg(z + z = z) \wedge x + z = y) \), "\( y \) is \( x \) plus something non-zero", defines the set of pairs \( (d, e) \) with \( d < e \).
3. In \( (\nN; \cdot) \), write \( U(x) \) for the formula \( \forall y\, (x \cdot y = y) \), "multiplying by \( x \) changes nothing". It defines \( \{ 1 \} \): at \( x = 0 \) the instance \( y = 1 \) fails, since \( 0 \cdot 1 = 0 \); at \( x \ge 2 \) the instance \( y = 1 \) fails too, since \( x \cdot 1 = x \ne 1 \); and at \( x = 1 \) every instance holds.
4. In \( (\nN; \cdot) \), the formula
\[
\neg U(x) \wedge \forall y\, \forall z\, \bigl( y \cdot z = x \to (U(y) \vee U(z)) \bigr) ,
\]
"\( x \) is not \( 1 \), and whenever \( x \) is a product, one factor is \( 1 \)", defines the primes. At \( x = 0 \) the instance \( y = z = 0 \) fails (\( 0 \cdot 0 = 0 \), and neither factor is \( 1 \)); at \( x = 1 \) the first conjunct fails; at a composite \( x = yz \) with \( y, z \ge 2 \) the instance at that \( y \), \( z \) fails; at a prime, every factorization has a factor \( 1 \).
:::
:::

Each definition builds on the last: \( 0 \) and \( 1 \) are not symbols of these structures, yet the language can name them, and once \( 1 \) is defined, "prime" can be written with it. In (d), \( U(y) \) is the formula \( U(x) \) with \( y \) for \( x \) and its bound \( y \) renamed, say \( \forall w\, (y \cdot w = w) \), so that the substituted letter is not captured.

To check that a formula defines a given set, check two directions, as for any equality of sets: every element of the set satisfies the formula, and every element that satisfies the formula is in the set. In (d) the cases \( x = 0 \), \( x = 1 \) and "\( x \) composite" are the second direction, and "at a prime" is the first. Leave out a case and a definition can be wrong at one point. Delete the conjunct \( \neg U(x) \) from (d): at \( x = 1 \) every factorization \( y \cdot z = 1 \) has \( y = z = 1 \), so the remaining formula is true of \( 1 \), and it defines the primes together with \( 1 \). Exactly one element changed sides.

::: {.check}
What does \( \exists y\, (x = y + y) \) define in \( (\nZ; +) \)? In \( (\nQ; +) \)?
:::

::: {.solution}
In \( (\nZ; +) \), the even integers. In \( (\nQ; +) \), all of \( \nQ \): every rational \( x \) is \( y + y \) for \( y = x/2 \), which is again rational. Same formula, two structures, two sets.
:::

## \( \exists \) is a projection

A formula with two free variables defines a set of pairs, and a set of pairs of reals can be drawn. In \( (\nR; \cdot) \), the formula \( y \cdot y = x \) defines \( \{ (d, e) : e^2 = d \} \), a parabola lying on its side. The formula \( \exists y\, (y \cdot y = x) \) has the one free variable \( x \), and by (S7) it is true of \( d \) exactly when some \( e \) puts the point \( (d, e) \) on the parabola. So it defines the set of first coordinates of the points of the parabola: its **shadow** on the \( x \)-axis, \( [0, \infty) \).

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.1]
  \draw[->] (-0.5,0) -- (4.6,0) node[right] {$x$};
  \draw[->] (0,-2.3) -- (0,2.3) node[above] {$y$};
  \draw[thick] plot[domain=-2.1:2.1, smooth, variable=\t] ({\t*\t},{\t});
  \node[above] at (3.3,2.0) {$y \cdot y = x$};
  \draw[dashed] (1,1) -- (1,0);
  \draw[dashed] (1,-1) -- (1,0);
  \draw[dashed] (4,2) -- (4,0);
  \draw[very thick, ->] (0,0) -- (4.4,0);
  \node[below] at (2.4,-0.15) {$\exists y\,(y \cdot y = x)$};
\end{tikzpicture}
\end{center}
```

The dashed segments drop two points, \( (1, 1) \) and \( (1, -1) \), and the point \( (4, 2) \), onto their shadows \( 1 \) and \( 4 \). No point of the parabola lies above a negative \( x \), so no negative number is in the shadow.

In general, \( \exists y\, \varphi \) defines the **projection** of the set that \( \varphi \) defines: \( d \) is in it exactly when some \( e \) puts \( (d, e) \) in \( \varphi \)'s set, by (S7). Dually, \( \forall y\, \varphi \) keeps the \( d \) whose whole vertical line lies in \( \varphi \)'s set, by (S6). This is the picture behind every \( \exists \) in a definition: to show a set definable, it is often easiest to describe a set of pairs and project.

The two readings are tied by negation. By (S4), (S6) and (S7), \( \forall y\, \varphi \) is satisfied exactly when \( \exists y\, \neg\varphi \) is not, so the set defined by \( \forall y\, \varphi \) is the complement of the projection of the complement of \( \varphi \)'s set: remove \( \varphi \)'s set from the plane, take the shadow of what is left, and keep the points of the axis that are not in that shadow.

::: {.check}
In \( (\nR; \le, \cdot) \), which set does \( \forall y\, (x \le y \cdot y) \) define?
:::

::: {.solution}
\( (-\infty, 0] \). The least value of \( y \cdot y \) is \( 0 \), at \( y = 0 \), so \( x \le y^2 \) holds for every \( y \) exactly when \( x \le 0 \). In the picture: the vertical line at \( x \) lies wholly in the region \( x \le y^2 \) when \( x \le 0 \), and the line at a positive \( x \) leaves it near \( y = 0 \).
:::

## Define it by a formula

A common task in mathematics is to turn a notion described in words into a formula, and the skill is the reverse of reading back. The notion must be said using only the symbols of the structure, and every variable that is not the defined set's own must be bound.

::: {#exm-define-by-formula}
[Maximum, Maximal, Supremum]

::: {.enumerate options="label=(\alph*)"}
1. In a structure with one two-place symbol \( \le \) read as a partial order: "\( x \) is a **greatest** element" is \( \forall y\, (y \le x) \), "everything is below \( x \)". "\( x \) is a **maximal** element" is \( \forall y\, (x \le y \to y = x) \), "nothing is above \( x \) except \( x \) itself". In the divisibility order on \( \{ 1, 2, 3 \} \) (\( d \le e \) when \( d \) divides \( e \)), \( 2 \) and \( 3 \) are maximal, and there is no greatest element, since \( 2 \) does not divide \( 3 \) nor \( 3 \) divide \( 2 \). On \( \{ 1, 2, 3, 6 \} \), \( 6 \) is both maximal and greatest.
2. Add a one-place symbol \( A \) for a set of reals, and work in \( (\nR; \le, A) \). "\( x \) is an upper bound of \( A \)" is the formula \( B(x) \): \( \forall y\, (A(y) \to y \le x) \), "every element of \( A \) is at most \( x \)". "\( x \) is the supremum of \( A \)" is \( B(x) \wedge \forall z\, (B(z) \to x \le z) \), "\( x \) is an upper bound, and below every upper bound". For \( A = [0, 1) \), the supremum is \( 1 \): it is an upper bound, and any \( z < 1 \) is exceeded by an element of \( [0, 1) \), such as the larger of \( 0 \) and \( (z + 1)/2 \), so \( z \) is not one. No element of \( A \) is greatest.
3. "\( A \) has a greatest element" is the sentence \( \exists x\, (A(x) \wedge B(x)) \), "some element of \( A \) is an upper bound of \( A \)". It is false for \( A = [0, 1) \) and true for \( A = [0, 1] \).
:::
:::

In (c) the formula \( B(x) \) is used inside a larger formula, as a word is used in a sentence. This is how definitions accumulate: each defined notion is an abbreviation, and the full formula is the abbreviation written out.

Defining a notion goes in three steps. First, say the notion in words that use only the structure's symbols: "upper bound" becomes "every element of \( A \) is at most \( x \)". Second, write each auxiliary notion as a formula with its own free variable, and substitute it where it is used, renaming bound variables so that nothing is captured. Third, check both directions on a small case. The commonest slip is a variable left free. Written without its \( \forall y \), the formula \( A(y) \to y \le x \) has two free variables and defines a set of **pairs**, those \( (d, e) \) with \( d \notin A \) or \( d \le e \); it is not a property of \( x \) at all.

A defined notion can also be given its own symbol, as "even" and "the supremum of \( A \)" are in ordinary mathematics. Section 5.8 showed (@prp-definitional-extension) that such a definition is safe: introducing a predicate symbol by \( \forall x\, (P(x) \leftrightarrow \varphi) \), or a constant for an element that \( \varphi \) is proved to have, proves nothing new about the old symbols. Definability says which notions can be so introduced in a given structure: exactly those some formula of its language defines.

::: {.warning}
Greatest is not maximal. A maximal element has nothing strictly above it; a greatest element is above everything. In the divisibility order on \( \{ 1, 2, 3 \} \), \( 2 \) is maximal and not greatest. Writing \( \forall y\, (y \le x) \) for "maximal" defines the wrong set: in that order it defines \( \emptyset \), while the maximal elements are \( 2 \) and \( 3 \).
:::

::: {.check}
In the divisibility order on \( \{ 1, 2, 3, 4, 6 \} \), which elements are maximal? Is there a greatest element?
:::

::: {.solution}
\( 4 \) and \( 6 \): neither divides any other element of the set. There is no greatest element: \( 4 \) does not divide \( 6 \), and \( 6 \) does not divide \( 4 \).
:::

## Isomorphic structures (second pass)

This half of the section is for a second reading. It asks when two structures are the same except for the names of their elements, and proves that such structures satisfy the same sentences. From that comes a way to show that a set is **not** definable. It uses functions and bijections in their everyday sense: a rule that sends each element to one element, and, for a bijection, one that matches the two domains one to one, every element of the second domain hit exactly once.

::: {#def-isomorphism-of-structures}
[Isomorphism of Structures]

Let \( \fM \) and \( \fN \) be structures for the same symbols, with domains \( D \) and \( E \). An **isomorphism** \( h \colon \fM \to \fN \) is a bijection \( h \colon D \to E \) such that

::: {.enumerate options="label=(\roman*)"}
1. \( h(c^{\fM}) = c^{\fN} \) for each constant \( c \);
2. \( h\bigl( f^{\fM}(d_1, \dots, d_n) \bigr) = f^{\fN}\bigl( h(d_1), \dots, h(d_n) \bigr) \) for each function symbol \( f \) of arity \( n \) and all \( d_1, \dots, d_n \in D \);
3. \( (d_1, \dots, d_n) \in R^{\fM} \) if and only if \( \bigl( h(d_1), \dots, h(d_n) \bigr) \in R^{\fN} \), for each predicate symbol \( R \) of arity \( n \) and all \( d_1, \dots, d_n \in D \).
:::

An isomorphism \( \fM \to \fM \) is an **automorphism** of \( \fM \). \( \fM \) and \( \fN \) are **isomorphic** if an isomorphism \( \fM \to \fN \) exists.
:::

In words: \( h \) renames every element, and the renaming carries each constant to the corresponding constant, each operation to the corresponding operation, and each relation onto the corresponding relation, in both directions.

Clause (iii) is needed in both directions. The identity map \( 1 \mapsto 1 \), \( 2 \mapsto 2 \), from \( \{ 1, 2 \} \) with \( R \) empty to \( \{ 1, 2 \} \) with \( R = \{ (1, 2) \} \), is a bijection, and it sends every pair in the first relation into the second, since there are none. Yet the sentence \( \exists x\, \exists y\, R(x, y) \) is false in the first structure and true in the second. The converse half of (iii) fails at \( (1, 2) \), and with it the map is not an isomorphism.

*Examples.* \( (\nN, <) \) and the even numbers with \( < \) are isomorphic, by \( h(d) = 2d \): every even number is \( 2d \) for exactly one \( d \), and \( d < e \) if and only if \( 2d < 2e \). A finite example, with the bijection as a table:

```{=latex}
\begin{center}
\begin{tikzpicture}[structure]
  \node[elt, label=below:$a$] (a) at (0,0) {};
  \node[elt, label=below:$b$] (b) at (1.4,0) {};
  \node[elt, label=below:$c$] (c) at (2.8,0) {};
  \draw[rel] (a) -- (b);
  \draw[rel] (b) -- (c);
  \draw[rel] (a) to[bend left] (c);
  \node[align=left] at (4.6,0.3) {$a \mapsto 1$\\$b \mapsto 2$\\$c \mapsto 3$};
  \node[elt, label=below:$1$] (p) at (6.4,0) {};
  \node[elt, label=below:$2$] (q) at (7.8,0) {};
  \node[elt, label=below:$3$] (r) at (9.2,0) {};
  \draw[rel] (p) -- (q);
  \draw[rel] (q) -- (r);
  \draw[rel] (p) to[bend left] (r);
\end{tikzpicture}
\end{center}
```

On the left, \( \fM \) has \( D = \{ a, b, c \} \) and \( R^{\fM} = \{ (a, b), (b, c), (a, c) \} \); on the right is \( (\{ 1, 2, 3 \}, <) \), with an arrow from \( d \) to \( e \) when \( d < e \). The table is a bijection, and it sends the three arrows on the left exactly onto the three on the right. A non-example: \( d \mapsto d + 1 \), from \( (\nN, <) \) to itself, preserves \( < \) in both directions and is one to one, but it is not onto: nothing is sent to \( 0 \). So it is not an automorphism.

::: {#thm-isomorphism-invariance}
[Isomorphic Structures Satisfy the Same Sentences]

Let \( h \colon \fM \to \fN \) be an isomorphism. For every formula \( \varphi \) and every assignment \( \ell \) in \( \fM \),
\[
\fM, \ell \models \varphi \quad \text{if and only if} \quad \fN, h \circ \ell \models \varphi ,
\]
where \( h \circ \ell \) gives each variable \( x \) the value \( h(\ell(x)) \). In particular, \( \fM \models \sigma \) if and only if \( \fN \models \sigma \), for every sentence \( \sigma \).
:::

*In words: renaming the elements, consistently, changes the truth of nothing.*

The theorem is most often used backwards: a sentence true in one structure and false in another shows that the two are **not** isomorphic. The sentence \( \forall x\, \exists y\, (y + y = x) \), "every element is a sum of two equal ones", is true in \( (\nQ; +) \) (take \( y = x/2 \)) and false in \( (\nZ; +) \) (at \( x = 1 \)), so no bijection \( \nQ \to \nZ \) carries addition to addition, although bijections \( \nQ \to \nZ \) exist (*Sets and Functions*, Chapter 4). The converse of the theorem fails: two structures can satisfy the same sentences without being isomorphic, and the optional Section 7.6 meets such a pair.

The proof is in the fold below.

::: {.second-reading title="The proof: terms, then formulas"}
::: {.idea}
An induction on terms and then on formulas, of the kind Section 7.1 gave for @lem-free-coincidence. Each clause of the definition of isomorphism carries one kind of atomic formula across; injectivity carries equations back; and in the quantifier cases, as \( d \) runs over \( D \), its image \( h(d) \) must run over all of \( E \), which is what "onto" gives.
:::

::: {.proof}
*Terms.* First, \( h(t^{\fM, \ell}) = t^{\fN, h \circ \ell} \) for every term \( t \), by induction on \( t \). For a variable \( x \), both sides are \( h(\ell(x)) \), by the definition of \( h \circ \ell \). For a constant, this is clause (i). For \( t = f(t_1, \dots, t_n) \), clause (ii) and the hypothesis for \( t_1, \dots, t_n \) give
\[
h\bigl( f^{\fM}(t_1^{\fM, \ell}, \dots, t_n^{\fM, \ell}) \bigr) = f^{\fN}\bigl( h(t_1^{\fM, \ell}), \dots, h(t_n^{\fM, \ell}) \bigr) = f^{\fN}\bigl( t_1^{\fN, h \circ \ell}, \dots, t_n^{\fN, h \circ \ell} \bigr) .
\]

*Formulas.* Structural induction on \( \varphi \), with the claim stated for **all** assignments \( \ell \) at once, since the quantifier clauses change the assignment.

*Atomic.* By (S1), \( \fM, \ell \models R(t_1, \dots, t_n) \) means that the tuple of the values \( t_i^{\fM, \ell} \) is in \( R^{\fM} \). By clause (iii) that holds exactly when the tuple of their images is in \( R^{\fN} \), and by the claim for terms the images are the values \( t_i^{\fN, h \circ \ell} \): this is (S1) for \( \fN, h \circ \ell \). *Equations.* \( t_1^{\fM, \ell} = t_2^{\fM, \ell} \) implies \( h(t_1^{\fM, \ell}) = h(t_2^{\fM, \ell}) \); the converse holds because \( h \) is **injective**. With the claim for terms, this is (S2) on both sides. \( \bot \) is satisfied on neither side, by (S3).

*Connectives.* The answers for \( \varphi \) and \( \psi \) agree on the two sides by hypothesis, and (S4), (S5) combine them by the same rule on both sides.

*Universal quantifier.* \( \fM, \ell \models \forall x\, \varphi \) holds if and only if \( \fM, \ell[x \mapsto d] \models \varphi \) for every \( d \in D \), by (S6); by the hypothesis, applied to the assignment \( \ell[x \mapsto d] \), if and only if \( \fN, h \circ (\ell[x \mapsto d]) \models \varphi \) for every \( d \in D \). Now \( h \circ (\ell[x \mapsto d]) = (h \circ \ell)[x \mapsto h(d)] \): both give \( x \) the value \( h(d) \) and every other variable \( y \) the value \( h(\ell(y)) \). As \( d \) runs over \( D \), \( h(d) \) runs over **all** of \( E \), because \( h \) is **onto**. So the condition says that \( \fN, (h \circ \ell)[x \mapsto e] \models \varphi \) for every \( e \in E \), which is (S6) for \( \fN, h \circ \ell \models \forall x\, \varphi \).

*Existential quantifier.* The same, with (S7): some \( d \in D \) works on the left exactly when some \( e = h(d) \in E \) works on the right, and every \( e \in E \) is such an \( h(d) \), since \( h \) is **onto**.

For a sentence, @lem-free-coincidence makes the assignment irrelevant on both sides, which gives the last sentence of the statement.
:::
:::

::: {.check}
Why can no sentence in the symbol \( < \) tell \( (\nN, <) \) from the even numbers with \( < \)?
:::

::: {.solution}
Doubling is an isomorphism between them, so by @thm-isomorphism-invariance they satisfy the same sentences.
:::

## What an automorphism cannot move (second pass)

An automorphism is a renaming of a structure onto itself. By the theorem, a formula cannot tell an element from its image.

::: {#cor-automorphisms-fix-definable-sets}
[Automorphisms Preserve Definable Sets]

If \( h \) is an automorphism of \( \fM \) and \( S \subseteq D \) is definable in \( \fM \), then for every \( d \in D \), \( d \in S \) if and only if \( h(d) \in S \).
:::

::: {.proof}
Let \( \varphi \), with free variable \( x \), define \( S \), and let \( \ell \) be an assignment with \( \ell(x) = d \). By @thm-isomorphism-invariance with \( \fN = \fM \), \( \fM, \ell \models \varphi \) if and only if \( \fM, h \circ \ell \models \varphi \). The first says \( d \in S \); since \( (h \circ \ell)(x) = h(d) \), the second says \( h(d) \in S \).
:::

So to show that a set is **not** definable, find an automorphism that moves an element of it to an element outside it.

::: {#exm-shift-automorphism}
[Zero Cannot Be Defined from the Order of the Integers]

In \( (\nZ, <) \), the shift \( h(d) = d + 1 \) is an automorphism: it is a bijection, with inverse \( d \mapsto d - 1 \), and \( d < e \) if and only if \( d + 1 < e + 1 \). It sends \( 0 \) to \( 1 \), and \( 1 \notin \{ 0 \} \). By @cor-automorphisms-fix-definable-sets, \( \{ 0 \} \) is not definable in \( (\nZ, <) \): no formula in \( < \) alone singles out zero among the integers.

Contrast \( (\nN, <) \). There \( \{ 0 \} \) is definable, by \( \forall y\, \neg(y < x) \), "nothing is below \( x \)". The corollary is not contradicted, since \( d \mapsto d + 1 \) is not an automorphism of \( (\nN, <) \): it is not onto.

A finite picture: the four-cycle below, with \( D = \{ a, b, c, d \} \) and \( R \) the four arrows \( a \to b \to c \to d \to a \).

```{=latex}
\begin{center}
\begin{tikzpicture}[structure]
  \node[elt, label=below left:$a$] (a) at (0,0) {};
  \node[elt, label=below right:$b$] (b) at (1.6,0) {};
  \node[elt, label=above right:$c$] (c) at (1.6,1.6) {};
  \node[elt, label=above left:$d$] (d) at (0,1.6) {};
  \draw[rel] (a) -- (b);
  \draw[rel] (b) -- (c);
  \draw[rel] (c) -- (d);
  \draw[rel] (d) -- (a);
\end{tikzpicture}
\end{center}
```

The rotation \( a \mapsto b \), \( b \mapsto c \), \( c \mapsto d \), \( d \mapsto a \) is a bijection that sends each arrow to an arrow and each non-arrow to a non-arrow, so it is an automorphism. Applied once, twice or three times, it moves any element to any other, so no single element is definable.

A minimal change makes one element definable again. Add the loop \( (a, a) \) to \( R \). Now \( R(x, x) \) defines \( \{ a \} \), and the rotation is no longer an automorphism, since it sends the arrow \( (a, a) \) to \( (b, b) \), which is not an arrow. The method can only use the automorphisms a structure has; each of the three non-trivial rotations sends the loop \( (a, a) \) to a loop at \( b \), \( c \) or \( d \), so adding one arrow removed all three.
:::

::: {.warning}
An automorphism shows that a set is **not** definable; it never shows that one is. That no automorphism moves a set is not evidence that a formula defines it. To show a set definable, write the formula.
:::

::: {.check}
In the four-cycle, where does the rotation send the set \( \{ a, c \} \)? Could \( \{ a, c \} \) be definable?
:::

::: {.solution}
The rotation sends \( a \) to \( b \) and \( c \) to \( d \), so it moves \( a \in \{ a, c \} \) to \( b \notin \{ a, c \} \). By @cor-automorphisms-fix-definable-sets, \( \{ a, c \} \) is not definable. Its complement \( \{ b, d \} \) is not definable either, by the same rotation.
:::

::: {.remark}
[Looking ahead]

*Number Systems: From \(\nN\) to \(\nR\)*, Chapter 6, proves that any two complete ordered fields are isomorphic, by an isomorphism built from the rationals below each element; by this section, they then satisfy the same sentences.
:::

## Exercises

### A. Check your understanding

::: {#exr-definability-and-isomorphism-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define "\( S \subseteq D \) is definable in \( \fM \)".
2. Write formulas defining, in \( (\nN; +) \), the even numbers and the set \( \{ 0 \} \).
3. Why does a formula with two free variables define a set of pairs, and not a set of elements?
4. *(Second pass.)* State @thm-isomorphism-invariance.
5. *(Second pass; key proof.)* Where does the proof of @thm-isomorphism-invariance use that \( h \) is onto, and where that it is injective? What goes wrong for \( d \mapsto d + 1 \) on \( (\nN, <) \)?
6. *(Second pass.)* Why does \( x \mapsto x + 1 \) show \( \{ 0 \} \) undefinable in \( (\nZ, <) \) but not in \( (\nN, <) \)?
:::
:::

::: {.solution}
*(a)* Some formula \( \varphi \) with free variable \( x \) (at most) defines it: \( S = \{ d \in D : \fM, \ell[x \mapsto d] \models \varphi \} \), for any assignment \( \ell \) (@def-definable-set).

*(b)* \( \exists y\, (x = y + y) \), "\( x \) is a sum of two equal numbers"; \( x + x = x \), "\( x \) added to itself is itself".

*(c)* Its truth depends on the values of both variables (and, by @lem-free-coincidence, on nothing else), so it is true or false of pairs of values.

*(d)* If \( h \colon \fM \to \fN \) is an isomorphism, then \( \fM, \ell \models \varphi \) if and only if \( \fN, h \circ \ell \models \varphi \), for every formula \( \varphi \) and every assignment \( \ell \) in \( \fM \); in particular \( \fM \) and \( \fN \) satisfy the same sentences.

*(e)* Onto: in the \( \forall \) and \( \exists \) cases, so that \( h(d) \) runs over all of \( E \) as \( d \) runs over \( D \). Injective: in the equation case, to go from \( h(t_1^{\fM, \ell}) = h(t_2^{\fM, \ell}) \) back to \( t_1^{\fM, \ell} = t_2^{\fM, \ell} \). The map \( d \mapsto d + 1 \) is not onto, and the \( \forall \) case fails: \( \forall y\, \neg(y < x) \) is satisfied when \( x \) has the value \( 0 \), and not when \( x \) has the value \( h(0) = 1 \), because the element \( 0 \) below \( 1 \) is exactly the one the map never reaches.

*(f)* It is an automorphism of \( (\nZ, <) \) and moves \( 0 \); it is not an automorphism of \( (\nN, <) \) (not onto), and in \( (\nN, <) \) the set \( \{ 0 \} \) is in fact definable, by \( \forall y\, \neg(y < x) \).
:::

::: {#exr-definability-and-isomorphism-a2}
[A2: Drill]

Each part takes a line or two. Parts (a)–(f) belong to the first half of the section; parts (g)–(l) to the second half (second pass). They run from reading a formula, through writing one, to judging maps and using them.

::: {.enumerate options="label=(\alph*)"}
1. What subset of \( \nZ \) does \( \exists y\, (x = y + y + y) \) define in \( (\nZ; +) \)?
2. Define \( \{ 0 \} \) in \( (\nZ; +) \).
3. Define the pairs with \( x \le y \) in \( (\nN; +) \).
4. In \( (\{ 1, 2, 3 \}, <) \), which set does \( \forall y\, \neg(y < x) \) define? In \( (\nZ, <) \)?
5. Write "\( x \) is maximal" and "\( x \) is greatest" for a partial order \( \le \).
6. In \( (\nR; 1, +, \cdot) \), \( \varphi \) is \( x \cdot x + y \cdot y = 1 \). What does \( \exists y\, \varphi \) define?
7. Is \( h(d) = 2d \) an isomorphism from \( (\nZ, <) \) to the even integers with \( < \)?
8. Is \( h(d) = -d \) an automorphism of \( (\nZ, <) \)? Of \( (\nZ; +) \)?
9. Using (h), is \( \{ 1 \} \) definable in \( (\nZ; +) \)?
10. Is that consistent with (b)?
11. \( \fM \) has \( D = \{ a, b, c \} \) and \( R^{\fM} = \{ (a, c), (b, c) \} \). Which singletons are definable?
12. Are \( (\nN, <) \) and \( (\nZ, <) \) isomorphic? Give a sentence that shows it.
:::
:::

::: {.solution}
(a) The multiples of \( 3 \).

(b) \( x + x = x \).

(c) \( \exists z\, (x + z = y) \), "\( y \) is \( x \) plus something".

(d) \( \{ 1 \} \), "nothing is below \( x \)"; \( \emptyset \), since every integer has a smaller one.

(e) \( \forall y\, (x \le y \to y = x) \); \( \forall y\, (y \le x) \).

(f) \( [-1, 1] \), the shadow of the unit circle on the \( x \)-axis.

(g) Yes: a bijection onto the evens, and \( d < e \) if and only if \( 2d < 2e \).

(h) Not of \( (\nZ, <) \): \( 0 < 1 \), but \( -0 = 0 > -1 \). Yes of \( (\nZ; +) \): it is a bijection (its own inverse), and \( -(d + e) = (-d) + (-e) \).

(i) No: the automorphism \( d \mapsto -d \) sends \( 1 \) to \( -1 \notin \{ 1 \} \).

(j) Yes: \( d \mapsto -d \) sends \( 0 \) to \( 0 \), so it does not move \( \{ 0 \} \).

(k) \( \{ c \} \), by \( \exists y\, R(y, x) \), "something points to \( x \)". Not \( \{ a \} \) or \( \{ b \} \): swapping \( a \) and \( b \) (and fixing \( c \)) is an automorphism.

(l) No. \( \exists x\, \forall y\, \neg(y < x) \), "there is a least element", is true in \( (\nN, <) \) and false in \( (\nZ, <) \); isomorphic structures would agree on it.
:::

### B. Practice

::: {#exr-definability-and-isomorphism-b1}
[B1: Define it by a formula]

Define by a formula, and read each formula back in words. Parts (i)–(iii) are in \( (\nN; \cdot) \); parts (iv) and (v) are in \( (\nR; \le, A) \), with \( A \) a one-place symbol.

::: {.enumerate options="label=(\roman*)"}
1. "\( x \) divides \( y \)".
2. "\( x \) is a square".
3. "\( x \) and \( y \) have no common divisor except \( 1 \)".
4. "\( A \) is bounded above".
5. "\( A \) has a supremum that is not in \( A \)".
:::
:::

::: {.solution}
(i) \( \exists z\, (x \cdot z = y) \): "\( y \) is \( x \) times something".

(ii) \( \exists y\, (y \cdot y = x) \): "\( x \) is something times itself".

(iii) \( \forall z\, \bigl( (\exists u\, (z \cdot u = x) \wedge \exists v\, (z \cdot v = y)) \to \forall w\, (z \cdot w = w) \bigr) \): "every common divisor \( z \) of \( x \) and \( y \) is \( 1 \)". The consequent is \( U(z) \) of @exm-definable-sets (c), with its bound variable renamed to \( w \): written with the bound \( y \) of \( U \), it would capture the free \( y \). (At \( x = y = 0 \) every \( z \) is a common divisor, so the formula fails, as it should.)

(iv) \( \exists x\, B(x) \), with \( B(x) \) the upper-bound formula \( \forall y\, (A(y) \to y \le x) \): "some \( x \) is at least every element of \( A \)".

(v) \( \exists x\, \bigl( B(x) \wedge \forall z\, (B(z) \to x \le z) \wedge \neg A(x) \bigr) \): "some least upper bound of \( A \) is not in \( A \)".

**Marking scheme.** (10 points) 2 for each part: 1 for the formula, 1 for its reading back, with any auxiliary formula (\( U \), \( B \)) written out or cited. Fatal error (0 for the part): a free variable left over that is not one of the defined set's.
:::

::: {#exr-definability-and-isomorphism-b2}
[B2: What does this formula define?]

Describe the set each formula defines.

::: {.enumerate options="label=(\roman*)"}
1. \( \exists y\, (x = y \cdot y \cdot y) \) in \( (\nR; \cdot) \).
2. The same formula in \( (\nZ; \cdot) \).
3. \( \forall y\, (y \cdot x = x) \) in \( (\nN; \cdot) \).
4. \( \exists z\, (\neg(z + z = z) \wedge x + z = y) \) in \( (\nZ; +) \).
5. \( \exists y\, \bigl( x < y \wedge \forall z\, \neg(x < z \wedge z < y) \bigr) \) in \( (\nQ, <) \), and in \( (\nZ, <) \).
:::
:::

::: {.solution}
(i) All of \( \nR \): every real number has a real cube root.

(ii) The cubes, \( \{ \dots, -8, -1, 0, 1, 8, 27, \dots \} \).

(iii) \( \{ 0 \} \): at \( x = 0 \), \( y \cdot 0 = 0 \) for every \( y \); at \( x \ge 1 \), the instance \( y = 0 \) fails.

(iv) All pairs \( (x, y) \) with \( x \ne y \). In \( \nZ \), \( z = y - x \) always exists, and it is non-zero exactly when \( x \ne y \). The same formula defined \( x < y \) in \( (\nN; +) \) (@exm-definable-sets (b)); in \( \nZ \), where a negative \( z \) is available, it defines something else.

(v) In \( (\nQ, <) \), \( \emptyset \): between \( x \) and any larger \( y \) lies \( (x + y)/2 \). In \( (\nZ, <) \), all of \( \nZ \): take \( y = x + 1 \).

**Marking scheme.** (10 points) 2 for each part; in (iv), full marks require noticing that \( \nZ \) is not \( \nN \). Fatal error (0 for the part): an answer that ignores the structure, such as the same set for both structures in (v).
:::

::: {#exr-definability-and-isomorphism-b3}
[B3: Automorphisms of small structures]

*(Second pass.)*

::: {.enumerate options="label=(\alph*)"}
1. Find every automorphism of \( \fM \): \( D = \{ 1, 2, 3, 4 \} \), \( R^{\fM} = \{ (1, 1), (1, 2), (2, 1), (2, 2), (3, 3) \} \), the answer given to @exr-theories-and-models-b1 (ii).
2. Which singletons and which two-element subsets of \( D \) does that leave possibly definable? Define those that are.
3. Is \( d \mapsto d + 1 \) an automorphism of \( (\nZ; <, 0) \), with \( 0 \) a constant?
:::
:::

::: {.solution}
*(a)* An automorphism sends related pairs to related pairs and unrelated pairs to unrelated pairs. \( 4 \) is the only element related to nothing, so it must go to \( 4 \). \( 3 \) is the only element related to itself and to nothing else, so it must go to \( 3 \). That leaves \( 1 \) and \( 2 \), which may stay or be swapped, and both choices preserve \( R \). So there are two automorphisms: the identity, and the swap of \( 1 \) and \( 2 \).

*(b)* \( \{ 1 \} \) and \( \{ 2 \} \) are not definable: the swap moves them. \( \{ 3 \} \) is defined by \( R(x, x) \wedge \forall y\, (R(x, y) \to y = x) \); \( \{ 4 \} \) by \( \neg R(x, x) \). Among the two-element sets, \( \{ 1, 2 \} \) is defined by \( \exists y\, (R(x, y) \wedge \neg(y = x)) \), "\( x \) is related to something else", and \( \{ 3, 4 \} \) by its negation \( \neg\exists y\, (R(x, y) \wedge \neg(y = x)) \). The other four, \( \{ 1, 3 \} \), \( \{ 1, 4 \} \), \( \{ 2, 3 \} \), \( \{ 2, 4 \} \), are moved by the swap, so none is definable.

*(c)* No: it sends the value \( 0 \) of the constant to \( 1 \), and clause (i) of @def-isomorphism-of-structures asks \( h(0) = 0 \).

**Marking scheme.** (10 points) 4 for (a): both automorphisms, with the argument that \( 3 \) and \( 4 \) are fixed. 4 for (b): each definable set with its formula, and each other set with the automorphism that moves it. 2 for (c). Fatal error (0 for (b)): claiming a set definable because no automorphism moving it was found.
:::

### C. Going deeper

::: {#exr-definability-and-isomorphism-c1}
[C1: The definable subsets of \( (\nZ, <) \)]

*(Second pass.)*

::: {.enumerate options="label=(\alph*)"}
1. Prove that the only subsets of \( \nZ \) definable in \( (\nZ, <) \) by a formula with one free variable are \( \emptyset \) and \( \nZ \).
2. Show that the relation "\( y = x + 1 \)" is definable in \( (\nZ, <) \).
3. Why does (a) not contradict (b)?
:::
:::

::: {.solution}
*(a)* \( \emptyset \) and \( \nZ \) are defined by \( \neg(x = x) \) and \( x = x \). Conversely, let \( S \) be definable and non-empty, with \( n \in S \), and let \( m \in \nZ \). The shift \( d \mapsto d + (m - n) \) is an automorphism of \( (\nZ, <) \): it is a bijection, with inverse \( d \mapsto d - (m - n) \), and \( d < e \) if and only if \( d + (m - n) < e + (m - n) \). It sends \( n \) to \( m \), so \( m \in S \) by @cor-automorphisms-fix-definable-sets. Since \( m \) was arbitrary, \( S = \nZ \).

*(b)* \( x < y \wedge \neg\exists z\, (x < z \wedge z < y) \), "\( y \) is above \( x \) with nothing in between". In \( \nZ \) it holds of \( (d, e) \) exactly when \( d < e \) and no integer lies strictly between, that is, \( e = d + 1 \): if \( e = d + 1 \), an integer \( z \) with \( d < z < d + 1 \) does not exist; if \( e \ge d + 2 \), then \( z = d + 1 \) lies between.

*(c)* The corollary, and the argument of (a), concern sets of elements. "\( y = x + 1 \)" defines a set of pairs, and a shift moves each pair \( (n, n + 1) \) to another pair \( (m, m + 1) \) of the same set, so the set of pairs is not moved. What (a) forbids is a formula singling out some integers and not others; (b) singles out a relation that every integer has to its successor.

**Marking scheme.** (10 points) 5 for (a): the shift shown to be an automorphism (bijective and order-preserving), then the corollary applied. 3 for (b), with both directions checked in \( \nZ \). 2 for (c). Fatal error (0 for (a)): using \( d \mapsto -d \), which does not preserve \( < \).
:::

::: {#exr-definability-and-isomorphism-c2}
[C2: Challenge: the automorphisms of \( (\nQ, <) \)]

*(Second pass.)*

::: {.enumerate options="label=(\alph*)"}
1. Show that \( x \mapsto 2x \), and \( x \mapsto x + q \) for each rational \( q \), are automorphisms of \( (\nQ, <) \).
2. Deduce that the only subsets of \( \nQ \) definable in \( (\nQ, <) \) by a formula with one free variable are \( \emptyset \) and \( \nQ \).
3. Show that \( \{ x \in \nQ : x > 0 \} \) is definable in \( (\nQ; <, 0) \), with \( 0 \) a constant, but not in \( (\nQ, <) \).
:::
:::

::: {.solution}
*(a)* Both are bijections of \( \nQ \), with inverses \( x \mapsto x/2 \) and \( x \mapsto x - q \), and both preserve \( < \) in both directions: \( x < y \) if and only if \( 2x < 2y \), if and only if \( x + q < y + q \).

*(b)* The translations alone suffice: given \( p \) in a non-empty definable set \( S \) and any \( p' \in \nQ \), the automorphism \( x \mapsto x + (p' - p) \) sends \( p \) to \( p' \), so \( p' \in S \) by @cor-automorphisms-fix-definable-sets. As in C1, \( S = \nQ \).

*(c)* In \( (\nQ; <, 0) \) the formula \( 0 < x \) defines it. In \( (\nQ, <) \) it is neither \( \emptyset \) nor \( \nQ \), so by (b) it is not definable.

**Marking scheme.** (10 points) 3 for (a), 4 for (b), 3 for (c). Fatal error (0 for (b)): an argument with \( x \mapsto 2x \) alone, which fixes \( 0 \) and so cannot move \( 0 \) to anything else.
:::

### R. Review

::: {#exr-models-r1}
[R1]

Decide whether each sequent is derivable, and justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( (p \to q) \to r \vdash p \to r \).
2. \( (p \to q) \to r \vdash q \to r \).
:::
:::

::: {.solution}
*(a)* Not derivable. Look for a refuting row, backwards from the conclusion: \( p \to r \) is false only when \( p = \mathrm{T} \) and \( r = \mathrm{F} \). The premise must then be true, so its hypothesis \( p \to q \) must be false, which needs \( q = \mathrm{F} \). In the row \( p = \mathrm{T} \), \( q = \mathrm{F} \), \( r = \mathrm{F} \), the premise is \( \mathrm{F} \to \mathrm{F} \), true, and the conclusion is \( \mathrm{T} \to \mathrm{F} \), false. By @cor-refuting-row there is no derivation.

*(b)* Derivable. The goal is an implication, so open a box on \( q \); the premise is waiting for \( p \to q \), which a box on \( p \) produces by repeating \( q \) (the goal-directed and premise-directed steps of the search method of Section 3.1).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(p \to q) \to r}
  \open
  \hypo {2} {q}
  \open
  \hypo {3} {p}
  \have {4} {q} \r{2}
  \close
  \have {5} {p \to q} \ii{3-4}
  \have {6} {r} \ie{1,5}
  \close
  \have {7} {q \to r} \ii{2-6}
\end{nd}$
\end{center}
```

The row method of (a) could not settle (b): no row refutes it, and only a derivation (or @thm-completeness) shows it is derivable.
:::

::: {#exr-models-r2}
[R2]

Derive \( \neg(P \to \neg Q) \vdash \neg\neg P \wedge \neg\neg Q \) without \( \rulename{RAA} \) and without derived rules that use it. Which rule would you need to derive \( P \wedge Q \) itself?
:::

::: {.solution}
The goal is a conjunction, so derive each conjunct. Each is a negation, so each gets a \( \rulename{\neg I} \) box, whose goal is \( \bot \). The only way to use the premise \( \neg(P \to \neg Q) \) is to clash with it, so inside each box we build \( P \to \neg Q \). In the first box, from \( \neg P \): a \( \rulename{{\to}I} \) box on \( P \) clashes \( P \) with \( \neg P \) and uses \( \rulename{\bot E} \) (the pattern of @prp-vacuous-implication). In the second, from \( \neg Q \): a \( \rulename{{\to}I} \) box on \( P \) simply repeats \( \neg Q \). These are the rules of Chapters 1 and 2 (@def-rules-negation, @def-rules-contradiction, @def-rules-implication).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \to \neg Q)}
  \open
  \hypo {2} {\neg P}
  \open
  \hypo {3} {P}
  \have {4} {\bot} \ne{3,2}
  \have {5} {\neg Q} \be{4}
  \close
  \have {6} {P \to \neg Q} \ii{3-5}
  \have {7} {\bot} \ne{6,1}
  \close
  \have {8} {\neg\neg P} \ni{2-7}
  \open
  \hypo {9} {\neg Q}
  \open
  \hypo {10} {P}
  \have {11} {\neg Q} \r{9}
  \close
  \have {12} {P \to \neg Q} \ii{10-11}
  \have {13} {\bot} \ne{12,1}
  \close
  \have {14} {\neg\neg Q} \ni{9-13}
  \have {15} {\neg\neg P \wedge \neg\neg Q} \ai{8,14}
\end{nd}$
\end{center}
```

No \( \rulename{RAA} \) is used. To reach \( P \wedge Q \) we would need \( P \) from \( \neg\neg P \) and \( Q \) from \( \neg\neg Q \), that is, \( \rulename{\neg\neg E} \), which is derived with \( \rulename{RAA} \) (@prp-double-negation), or an \( \rulename{RAA} \) box directly (@def-rule-raa). The look-alike is @exr-finding-derivations-b1 (b), \( \neg(P \to Q) \vdash P \wedge \neg Q \): there the conjunct \( P \) needed \( \rulename{RAA} \), while \( \neg Q \) came by \( \rulename{\neg I} \) alone. Here both conjuncts stop at a double negation. That no derivation of \( P \) (or of \( P \wedge Q \)) from the premise avoids \( \rulename{RAA} \) is true, but we state it without proof, and nothing depends on it.
:::

::: {#exr-models-r3}
[R3]

Derive \( \neg\exists x\, (P(x) \to \neg Q(x)) \vdash \forall x\, \bigl( \neg\neg P(x) \wedge \neg\neg Q(x) \bigr) \) without \( \rulename{RAA} \).
:::

::: {.solution}
The goal is \( \forall x \), so open a flagged box with a fresh name \( x_0 \) (@def-rules-universal); the new goal is \( \neg\neg P(x_0) \wedge \neg\neg Q(x_0) \). Inside, run the derivation of R2 (@exr-models-r2) with \( P(x_0) \) and \( Q(x_0) \) in place of \( P \) and \( Q \). One change: the premise is now \( \neg\exists x\, (P(x) \to \neg Q(x)) \), not \( \neg(P \to \neg Q) \), so each clash first turns \( P(x_0) \to \neg Q(x_0) \) into \( \exists x\, (P(x) \to \neg Q(x)) \) by \( \rulename{\exists I} \) at \( x_0 \) (@def-rule-existential-introduction).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg \exists x\, (P(x) \to \neg Q(x))}
  \open[x_0]
  \open
  \hypo {2} {\neg P(x_0)}
  \open
  \hypo {3} {P(x_0)}
  \have {4} {\bot} \ne{3,2}
  \have {5} {\neg Q(x_0)} \be{4}
  \close
  \have {6} {P(x_0) \to \neg Q(x_0)} \ii{3-5}
  \have {7} {\exists x\, (P(x) \to \neg Q(x))} \Ei{6}
  \have {8} {\bot} \ne{7,1}
  \close
  \have {9} {\neg\neg P(x_0)} \ni{2-8}
  \open
  \hypo {10} {\neg Q(x_0)}
  \open
  \hypo {11} {P(x_0)}
  \have {12} {\neg Q(x_0)} \r{10}
  \close
  \have {13} {P(x_0) \to \neg Q(x_0)} \ii{11-12}
  \have {14} {\exists x\, (P(x) \to \neg Q(x))} \Ei{13}
  \have {15} {\bot} \ne{14,1}
  \close
  \have {16} {\neg\neg Q(x_0)} \ni{10-15}
  \have {17} {\neg\neg P(x_0) \wedge \neg\neg Q(x_0)} \ai{9,16}
  \close
  \have {18} {\forall x\, (\neg\neg P(x) \wedge \neg\neg Q(x))} \Ai{2-17}
\end{nd}$
\end{center}
```

The side condition of \( \rulename{\forall I} \) at line 18: \( x_0 \) does not appear in the premise on line 1, no box is open at line 18, and \( x_0 \) does not appear in the conclusion. The flagged box immediately contains the \( \rulename{\neg I} \) box of line 2, so it is cited from line 2, the first line of that inner box. Lines 7 and 14 are legal \( \rulename{\exists I} \) steps: \( P(x_0) \to \neg Q(x_0) \) is \( (P(x) \to \neg Q(x))[x_0/x] \). The whole derivation is R2's, run inside a flagged box, with an \( \rulename{\exists I} \) before each clash.
:::

::: {#exr-models-r4}
[R4]

Is the sentence \( \forall x\, \exists y\, (x < y) \to \exists y\, \forall x\, (x < y) \) true in \( (\nN, <) \)? Is it derivable?
:::

::: {.solution}
*True in \( (\nN, <) \)?* No. The hypothesis \( \forall x\, \exists y\, (x < y) \) is true in \( (\nN, <) \): each \( d \) has \( d + 1 \) above it. The conclusion \( \exists y\, \forall x\, (x < y) \) is false: a candidate \( e \) fails at \( x = e \), since \( e < e \) is false. By (S5) of @def-satisfaction, an implication with a true hypothesis and a false conclusion is false.

*Derivable?* No. By the soundness statement of [Section 7.2](#from-counter-models-to-non-derivability), a derivable sentence is true in every structure; this one is false in \( (\nN, <) \), so no derivation exists.

*Why these tools.* A structure settles the question in two lines, while a derivation search could only fail, and a failed search proves nothing. A truth table is the wrong look-alike: it reads the sentence as \( p \to q \) with two atoms, and a refuting row for \( p \to q \) says nothing here, since the sentence \( \forall x\, P(x) \to \exists x\, P(x) \) has the same shape and is derivable (@prp-forall-implies-exists, then \( \rulename{{\to}I} \)). The soundness statement used here is proved in Section 7.3.
:::

<!-- dependency ledger
def-definable-set (claim): the defined set does not depend on l | lem-free-coincidence (cited)
exm-definable-sets (example): a real is a square of a real iff it is non-negative | school algebra (AN1.1 thm-nth-root, prose only); verify/ch07/exm-definable-sets.py
exm-definable-sets (example): d + d = d iff d = 0; x + z = y with z non-zero iff x < y in N; U defines {1}; the prime formula defines the primes | inline case checks; verify/ch07/exm-definable-sets.py (window 0-200, primes against a sieve)
exm-definable-sets (claim): U(y) written with its bound variable renamed so that y is not captured | renaming of bound variables, F1.4 §02 (prose); the formula is written out
exm-definable-sets (solution): Quick check, x = y + y in Z exactly for the even integers | definition of even; every integer is even or odd and not both, F2.2 (promised, STATUS row F1.1 §01 …)
exm-definable-sets (solution): Quick check, every rational is y + y with y = x/2 rational | school algebra of fractions
def-definable-set (claim): exists y phi defines the projection; forall y phi keeps the full vertical lines | (S6), (S7) of def-satisfaction (cited by name); def-definable-set
def-definable-set (solution): Quick check, x <= y*y for all real y iff x <= 0 | school algebra (squares are non-negative, 0 is a square)
exm-define-by-formula (example): maximal and greatest in the divisibility orders on {1,2,3} and {1,2,3,6}; the Quick check on {1,2,3,4,6} | verify/ch07/exm-define-by-formula.py
exm-define-by-formula (example): sup [0,1) = 1, the element max(0, (z+1)/2) of [0,1) above z < 1; [0,1) has no greatest element, [0,1] has | school algebra of the order of R
exm-define-by-formula (claim): a defined predicate or a constant for a proved-existing element proves nothing new | prp-definitional-extension (cited; F1.4 §08, parts (a) and (b))
def-isomorphism-of-structures (claim): functions, bijections, inverses and composition in the everyday sense | F2.1 (paid: def-function, def-bijective, def-composition, def-inverse-function; everyday sense, prose only)
def-isomorphism-of-structures (example): h(d) = 2d is a bijection from N onto the evens preserving <; d -> d + 1 on N preserves < and misses 0; the table of the finite example | inline; verify/ch07/exm-shift-automorphism.py (the finite example)
thm-isomorphism-invariance (proof): induction on terms and structural induction on formulas for all assignments at once | thm-structural-recursion and structural induction as used for lem-free-coincidence (F1.6 §01); inline
thm-isomorphism-invariance (proof): h o (l[x -> d]) = (h o l)[x -> h(d)]; h onto, so h(d) runs over all of E | inline (definition of l[x -> d], def-assignment)
cor-automorphisms-fix-definable-sets (proof): from thm-isomorphism-invariance with N = M | thm-isomorphism-invariance (cited)
exm-shift-automorphism (example): the shift on Z is a bijection preserving <; forall y not(y < x) defines {0} in (N, <); the rotation of the four-cycle is an automorphism and its powers move any element to any other | inline; verify/ch07/exm-shift-automorphism.py (all 24 permutations of the four-cycle)
exm-shift-automorphism (solution): Quick check, the rotation moves {a, c} and {b, d} | verify/ch07/exm-shift-automorphism.py
cor-automorphisms-fix-definable-sets (claim): Looking ahead, any two complete ordered fields are isomorphic | F3.4 thm-cof-uniqueness (exists; Looking ahead only, nothing rests on it)
thm-isomorphism-invariance (example): forall x exists y (y+y=x) true in (Q;+) with y = x/2, false in (Z;+) at x = 1 (y <= 0 gives y+y <= 0, y >= 1 gives y+y >= 2) | inline case check; school arithmetic of Z
thm-isomorphism-invariance (claim): bijections Q -> Z exist | F2.3 thm-integers-rationals-countable (exists; aside only, nothing rests on it)
exm-definable-sets (solution): Quick check, exists y (x = y+y) defines the even integers in (Z;+) | inline (definition of even)
exr-definability-and-isomorphism-a2 (solution): each set and map on a window or by enumeration | verify/ch07/exr-definability-and-isomorphism-a2.py
exr-definability-and-isomorphism-b1 (solution): the five formulas | verify/ch07/exr-definability-and-isomorphism-b1.py (window)
exr-definability-and-isomorphism-b2 (solution): every real is a cube of a real | school algebra (AN1.1 thm-nth-root, prose only); verify/ch07/exr-definability-and-isomorphism-b2.py (window)
exr-definability-and-isomorphism-b3 (solution): the two automorphisms and the definable sets | verify/ch07/exr-definability-and-isomorphism-b3.py (all 24 permutations)
exr-definability-and-isomorphism-c1 (solution): shifts of Z are automorphisms; the successor relation | inline; verify/ch07/exr-definability-and-isomorphism-c1.py (spot checks)
exr-definability-and-isomorphism-c2 (solution): x -> 2x and translations are order automorphisms of Q | inline; verify/ch07/exr-definability-and-isomorphism-c2.py (spot checks)
exr-models-r4 (solution): non-derivability from a false instance | the soundness statement of Section 7.2 (not proved there; F1.6 §03)
-->
