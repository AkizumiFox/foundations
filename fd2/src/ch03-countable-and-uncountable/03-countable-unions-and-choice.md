# Countable Unions and the Axiom of Choice

Section 8.2 listed \( \nN \times \nN \), \( \nZ \) and \( \nQ \), and showed that a union of two countable sets is countable (@prp-union-two-countable). The next question is a union of **countably many** countable sets. The natural proof is short, and it contains one step that none of the rules met so far can justify. This section isolates that step, adds the principle that licenses it, the axiom of choice, and then shows how to tell a proof that needs the axiom from one that only seems to.

## A union of countably many lists

Let \( A_0, A_1, A_2, \dots \) be countable sets, a family \( (A_n)_{n \in \nN} \) in the sense of @def-indexed-family. We want to prove that \( \bigcup_{n \in \nN} A_n \) is countable.

Here is the proof most people write first. List each set: \( A_n = \{ a_{n,0}, a_{n,1}, a_{n,2}, \dots \} \). Put \( a_{n,m} \) in row \( n \) and column \( m \) of an infinite grid. Every element of the union stands somewhere in the grid, and the grid is indexed by \( \nN \times \nN \), which is countable (@thm-product-countable). So the union is the image of a countable set, and it is countable.

Every step but the first, "list each set", is a result of Section 8.2. Where do the lists come from?

## The obstacle, rule by rule

For a non-empty \( A_n \), "\( A_n \) is countable" says that **there exists** a surjection \( \nN \to A_n \) (@def-countable). To use it we apply \( \rulename{\exists E} \) (@def-rules-existential): we name the object and argue inside the box of that name. One \( \rulename{\exists E} \) names **one** surjection, for **one** \( n \).

- **Finitely many sets.** The proof of @prp-union-two-countable used two \( \rulename{\exists E} \)'s; for \( A_0, \dots, A_9 \) we could nest ten boxes.
- **All \( n \in \nN \) at once.** The grid needs a list of \( A_n \) for every \( n \), assembled into one object: a function that sends each \( n \) to a surjection \( \nN \to A_n \). A proof is a finite object. It cannot contain one \( \rulename{\exists E} \) for each of infinitely many indices, and no rule of Chapter 4 makes infinitely many choices in one step.

Two escape routes fail. *Recursion* (@thm-recursion) defines a function on all of \( \nN \) at once, but from a rule \( g \) given in advance, each value determined by the previous one. The list of \( A_{n+1} \) is not determined by the list of \( A_n \), and a rule producing a list of every \( A_{n+1} \) would already be the missing object. *Induction* on \( k \), with @prp-union-two-countable at each step, proves "for every \( k \), \( A_0 \cup \dots \cup A_k \) is countable" (Exercise C3 writes it out), but that is a statement about each \( k \) separately; nothing makes the lists for different \( k \) fit together.

Section 6.5 met the same wall: a right inverse of a surjection must pick a preimage of **every** point at once, and the rules could do that only for finitely many points, or when a rule names the preimage.

## The axiom of choice

None of the working rules (W1)–(W6) of Section 6.1 forms a set out of infinitely many arbitrary picks. The principle we add is the simplest statement that does.

*From any family of non-empty sets, one may pick one element from each set, all at once.*

::: {#ax-choice}
[Axiom of Choice]

Let \( I \) be a set, and let \( (A_i)_{i \in I} \) be a family of sets such that \( A_i \) is **non-empty** for **every** \( i \in I \). Then **there exists** a function
\[
c \colon I \to \bigcup_{i \in I} A_i \quad \text{with} \quad c(i) \in A_i \ \text{ for every } i \in I .
\]
Such a function \( c \) is called a **choice function** for the family.
:::

In symbols, with \( Y^X \) the set of functions of Section 6.4 and \( U \coloneqq \bigcup_{i \in I} A_i \):
\[
\forall i \in I \ (A_i \ne \emptyset) \ \to \ \exists c \in U^{I} \ \ \forall i \in I \ \ c(i) \in A_i .
\]

In words: the hypothesis says that each set of the family has an element; the conclusion says that **one** function picks an element of every \( A_i \) at the same time. The codomain, a set by (W3), only gives \( c \) somewhere to take its values. The axiom asserts that \( c \) exists and gives no recipe for it.

**Its status.** For finitely many indices the axiom adds nothing (proved below); for infinitely many it is a genuinely new principle. It is independent of the other axioms of set theory: Gödel (1938) showed that adding it creates no contradiction that was not there already, and Cohen (1963) that it cannot be proved from them. A later chapter states its best-known equivalent, Zorn's lemma; the companion volume on set theory proves it equivalent to the axiom, together with the other equivalents such as the well-ordering theorem, and surveys the independence results. This book uses the axiom openly on the main line, among other places: here, for countable unions and right inverses; in Section 8.6, for infinite subsets that can be listed; in Chapter 11, for sup approximations (the remark below); in Chapter 43, for the Vitali set; in Chapter 67, through Zorn's lemma, for the Hahn–Banach theorem; and in Chapter 69, for Tychonoff's theorem. Each use is flagged at its line.

::: {.remark}
A corollary in Chapter 11 gives, for each \( n \ge 1 \) separately, some \( a_n \in A \) with \( a_n > \sup A - \frac1n \): one \( \rulename{\exists E} \) per \( n \), and no axiom. Forming the **sequence** \( (a_n)_{n \ge 1} \) from these is a choice function for the family \( \bigl( \{ a \in A : a > \sup A - \tfrac1n \} \bigr)_{n \in \nZ_{>0}} \), an instance of @ax-choice with the countable index set \( I = \nZ_{>0} \). Chapter 11 flags exactly this step.
:::

**Examples.**

1. *The empty family.* If \( I = \emptyset \), the empty function \( \emptyset \to \bigcup_{i \in \emptyset} A_i = \emptyset \) (@prp-empty-function (a)) is a choice function: the condition "for every \( i \in \emptyset \)" holds vacuously. No axiom is needed.
2. *A family with a rule.* Let \( I = \nZ_{>0} \) and \( A_n \coloneqq \{ k \in \nN : n \mid k, \ k \ne 0 \} \), the positive multiples of \( n \). Each \( A_n \) contains \( n \). The rule \( c(n) \coloneqq n \) is a choice function, defined by specification (@def-set-builder); no axiom is needed.
3. *A family with no rule in sight.* Let \( I \) be the set of non-empty subsets of \( \nR \), and \( A_S \coloneqq S \) for \( S \in I \). A choice function picks an element of every non-empty set of reals. "The least element" fails, since \( (0, 1) \) has none, and no rule that works for every \( S \) is known. Here the axiom supplies what the other rules do not.

**A non-example by minimal change.** In Example 2, add the index \( n = 0 \). The positive multiples of \( 0 \) form the empty set (\( 0 \mid k \) means \( k = 0 \)), so \( A_0 = \emptyset \), and no function can have \( c(0) \in A_0 \). Only the clause "\( A_i \) is non-empty for every \( i \)" fails, and without it the conclusion is false. That is why the proofs below remove the empty sets from a family before they choose. (Dropping "all at once" instead would leave nothing beyond the hypothesis.)

## When choice is not needed

Two kinds of construction look like choice and are not; telling them apart from a real use is the skill this section is for.

**Finitely many sets.** *For every finite set \( I \) and every family \( (A_i)_{i \in I} \) of non-empty sets, a choice function exists, with no appeal to the axiom.* For \( I = \{1, 2, 3\} \), three applications of \( \rulename{\exists E} \) name \( a_i \in A_i \), and \( \{ (1, a_1), (2, a_2), (3, a_3) \} \) is the graph of a choice function. For a finite set of arbitrary size we induct on its number of elements (@def-finite). Let \( P(n) \) be: "for every set \( I \) with \( n \) elements and every family \( (A_i)_{i \in I} \) of non-empty sets, there is a choice function". *Base case* \( P(0) \): a set with \( 0 \) elements is the image of a bijection from \( \{1, \dots, 0\} = \emptyset \), so it is empty, and the empty function is a choice function (Example 1). *Inductive step:* assume \( P(n) \), and let \( I \) have \( n + 1 \) elements. Then \( I \ne \emptyset \), since a bijection \( \{1, \dots, n + 1\} \to I \) has a value at \( 1 \); pick \( i_0 \in I \) by \( \rulename{\exists E} \). The set \( I' \coloneqq I \setminus \{i_0\} \) has \( n \) elements (@cor-remove-point), so \( P(n) \) gives a choice function \( c' \) for \( (A_i)_{i \in I'} \). Since \( A_{i_0} \ne \emptyset \), one more \( \rulename{\exists E} \) names \( a_0 \in A_{i_0} \). The graph of \( c' \) together with the pair \( (i_0, a_0) \), with codomain \( \bigcup_{i \in I} A_i \), is a function on \( I' \cup \{i_0\} = I \), because \( i_0 \notin I' \); and it is a choice function. So \( P(n + 1) \) holds, and @ax-induction gives \( P(n) \) for every \( n \in \nN \). Each step uses two \( \rulename{\exists E} \)'s and no new principle; the induction says nothing about an infinite \( I \), which has no number of elements.

**A rule that picks.** If one description names an element of each \( A_i \), the choice function is defined by specification (W1), as the set of pairs \( (i, a) \) with \( a \) the element named for \( i \). Typical rules: the **least element** of a non-empty set of natural numbers (@thm-well-ordering); the **non-negative** square root of a positive real; in a bisection, **the left half** if it has the property in question, and otherwise the right half. The first rule is how @thm-countable-characterizations passed from a surjection \( \nN \to A \) to an injection \( A \to \nN \) with no axiom: the least preimage is named, not chosen.

::: {.warning}
**Choice is not "picking an element".** "Let \( a \in A \)" is a single \( \rulename{\exists E} \) and needs no axiom; neither does picking from ten sets. The axiom is needed only for picking **one element from each of infinitely many sets, with no rule**. A proof that says "choose" need not use it, and one that never says "choose" may: "for each \( n \), let \( g_n \) be a list of \( A_n \)" is a use, however it is worded.
:::

## Right inverses

The first consequence settles the question Section 6.5 left open. By @prp-right-inverse-surjective, a function with a right inverse is surjective; the converse is where choice enters.

::: {#thm-surjection-right-inverse}
[Surjections Have Right Inverses]

Let \( f \colon X \to Y \) be a surjective function. Then \( f \) has a right inverse: there is a function \( g \colon Y \to X \) with \( f(g(y)) = y \) for every \( y \in Y \).
:::

::: {.idea}
A right inverse must name a preimage of every \( y \). The preimages of the points of \( Y \) form a family of sets indexed by \( Y \), each non-empty because \( f \) is onto. A choice function for that family is exactly a right inverse.
:::

::: {.proof}
For \( y \in Y \), let \( P_y \coloneqq f^{-1}(\{y\}) = \{ x \in X : f(x) = y \} \) (@def-preimage). This defines a family \( (P_y)_{y \in Y} \) of subsets of \( X \), indexed by \( Y \). Each \( P_y \) is non-empty, since \( f \) is surjective (@def-surjective). By @ax-choice there is a function \( c \colon Y \to \bigcup_{y \in Y} P_y \) with \( c(y) \in P_y \) for every \( y \in Y \). The union is a subset of \( X \), so the graph of \( c \) is a subset of \( Y \times X \), and with codomain \( X \) it is a function \( g \colon Y \to X \) with \( g(y) = c(y) \) (@def-function). For every \( y \in Y \), \( g(y) \in P_y \), that is, \( f(g(y)) = y \). So \( f \circ g = \id_Y \), and \( g \) is a right inverse of \( f \) (@def-left-right-inverse (b)).
:::

Together with @prp-right-inverse-surjective: a function is surjective **if and only if** it has a right inverse. The theorem is in fact equivalent to the axiom: a right inverse of the projection \( (i, a) \mapsto i \), from the set of pairs with \( a \in A_i \) onto \( I \), is a choice function in disguise.

::: {.check}
Let \( f \colon \nZ \to \nN \), \( f(k) \coloneqq \abs{k} \). It is surjective. Does the existence of a right inverse of \( f \) need @ax-choice?
:::

::: {.solution}
No. Each \( n \in \nN \) has the preimages \( n \) and \( -n \), and the rule "take the non-negative one" names one of them: \( g(n) \coloneqq n \). Then \( f(g(n)) = \abs{n} = n \), so \( g \colon \nN \to \nZ \) is a right inverse, defined by a formula. The axiom is needed only when no such rule is available.
:::

## Countable unions

Now the theorem the section opened with. The second form, with any countable index set, is the one used in practice.

::: {#thm-countable-union}
[Countable Unions of Countable Sets]

(a) Let \( (A_n)_{n \in \nN} \) be a family of sets such that \( A_n \) is countable for every \( n \in \nN \). Then \( \bigcup_{n \in \nN} A_n \) is countable.

(b) Let \( I \) be a countable set and \( (A_i)_{i \in I} \) a family of sets such that \( A_i \) is countable for every \( i \in I \). Then \( \bigcup_{i \in I} A_i \) is countable.
:::

::: {.idea}
This is the grid of the opening, with the lists supplied by the axiom. ① Throw away the empty sets: the axiom needs non-empty ones, and they add nothing to the union. ② For each remaining \( n \), the surjections \( \nN \to A_n \) form a non-empty set; choose one from each, all at once. ③ The chosen lists turn the grid \( J \times \nN \) into a surjection onto the union, and the grid is countable by Section 8.2. Part (b) is part (a) after renumbering the index set by a list.

*Before reading on: which line uses choice, and why can \( \rulename{\exists E} \) not replace it?*
:::

::: {.proof}
(a) Let \( U \coloneqq \bigcup_{n \in \nN} A_n \) and \( J \coloneqq \{ n \in \nN : A_n \ne \emptyset \} \).

If \( J = \emptyset \), every \( A_n \) is empty, so \( U = \emptyset \), which is countable by @def-countable.

Suppose \( J \ne \emptyset \). For \( n \in J \), let
\[
S_n \coloneqq \{ h \in A_n^{\nN} : h \text{ is surjective} \} ,
\]
the set of surjections \( \nN \to A_n \) (@def-set-builder, with \( A_n^{\nN} \) the set of functions of Section 6.4). Since \( A_n \) is countable and non-empty, \( S_n \ne \emptyset \) (@def-countable). **By @ax-choice**, applied to the family \( (S_n)_{n \in J} \), there is a function \( c \colon J \to \bigcup_{n \in J} S_n \) with \( c(n) \in S_n \) for every \( n \in J \). This is the only line of the proof that uses the axiom.

Define \( F \colon J \times \nN \to U \) by \( F(n, m) \coloneqq c(n)(m) \). It takes values in \( U \): \( c(n) \) maps into \( A_n \subseteq U \). It is surjective: let \( x \in U \); then \( x \in A_n \) for some \( n \in \nN \) (@def-family-union-intersection), so \( A_n \ne \emptyset \) and \( n \in J \); since \( c(n) \) is a surjection onto \( A_n \), there is \( m \in \nN \) with \( c(n)(m) = x \), that is, \( F(n, m) = x \).

The set \( J \) is countable by @prp-countable-subset, as a subset of \( \nN \), which is countable (the identity is a surjection). So \( J \times \nN \) is countable by @cor-product-countable (a), and it is non-empty, since it contains \( (n_0, 0) \) for any \( n_0 \in J \). By @def-countable there is a surjection \( s \colon \nN \to J \times \nN \). Then \( F \circ s \colon \nN \to U \) is surjective (@thm-composition-injective-surjective (b)), and \( U \) is countable.

(b) Let \( U \coloneqq \bigcup_{i \in I} A_i \). If \( I = \emptyset \), then \( U = \emptyset \), which is countable. Otherwise @def-countable gives a surjection \( s \colon \nN \to I \); fix one. For \( n \in \nN \) put \( B_n \coloneqq A_{s(n)} \), a countable set. Then \( \bigcup_{n \in \nN} B_n = U \). \( (\subseteq) \) An element of \( B_n \) lies in \( A_{s(n)} \) with \( s(n) \in I \). \( (\supseteq) \) If \( x \in A_i \) with \( i \in I \), then \( i = s(n) \) for some \( n \in \nN \), because \( s \) is onto, and \( x \in B_n \). By (a), \( U \) is countable.
:::

The line in bold is the only use of the axiom. The surjections \( s \) of parts (a) and (b) are single objects, each named by one \( \rulename{\exists E} \). What needed the axiom was a surjection **for every** \( n \in J \) at once: \( \rulename{\exists E} \) supplies \( c(n) \) only inside the box of a fixed \( n \), and \( F \) needs all of them outside every such box. The set \( J \) is there because for \( A_n = \emptyset \) there is no function \( \nN \to A_n \) at all (@prp-empty-function (b)), so \( S_n = \emptyset \). The theorem completes the closure properties of countable sets: subsets, images, finite products, countable unions.

Neither hypothesis can be dropped: Section 8.4 shows that \( \nR \) is not countable, and \( \nR \) is the union of the single set \( \nR \), and also of the countable sets \( \{x\} \), \( x \in \nR \).

::: {.warning}
**The choice is of the lists, not of preimages.** A surjection \( \nN \to A \) gives least preimages by a rule (@thm-countable-characterizations), but only once the surjection is **in hand**. In @thm-countable-union, what is missing is the surjection itself, one for each \( A_n \), and the sets \( A_n \) need not be sets of natural numbers, so no "least" is available to name one.
:::

## Unions without choice

Many countable unions met in practice come with their lists, and then no axiom is used.

::: {#exm-choice-free-unions}
[Unions that come with their lists]

(a) Show that \( \nQ = \bigcup_{n \in \nZ_{>0}} Q_n \), where \( Q_n \coloneqq \{ m/n : m \in \nZ \} \), and list the union without using @ax-choice.

(b) Does the proof in @thm-integers-rationals-countable that \( \nQ \) is countable use @ax-choice?
:::

::: {.solution}
(a) By the definition \( \nQ \coloneqq \{ m/n : m \in \nZ, \ n \in \nZ_{>0} \} \), a number is rational exactly when it lies in \( Q_n \) for some \( n \in \nZ_{>0} \), so the two sets are equal. Fix the bijection \( z \colon \nN \to \nZ \) of @thm-integers-rationals-countable (\( z(2k) = k \), \( z(2k + 1) = -(k + 1) \)). Then \( k \mapsto z(k)/n \) lists \( Q_n \), and the whole family of lists is the single function
\[
L \colon \nZ_{>0} \times \nN \to \nQ , \qquad L(n, k) \coloneqq z(k)/n ,
\]
defined by specification. It is onto \( \nQ \): for \( m/n \) with \( m \in \nZ \), \( n \in \nZ_{>0} \), take \( k \) with \( z(k) = m \). Since \( \nZ_{>0} \times \nN \) is countable and non-empty (@prp-countable-subset, @cor-product-countable), composing \( L \) with a surjection \( \nN \to \nZ_{>0} \times \nN \) lists \( \nQ \). The grid is the same as in @thm-countable-union; the difference is that the rows were written down, not chosen.

(b) No, and its place before @ax-choice does not settle this, since by the warning in "When choice is not needed" a proof can use the axiom without naming it; we check the lines. The maps \( z \) and \( (m, n) \mapsto m/n \) are formulas. The results cited name finitely many objects by \( \rulename{\exists E} \): one injection in @prp-countable-subset, two in @cor-product-countable (a), one surjection in @prp-countable-image. The passage from a surjection to an injection in @thm-countable-characterizations takes the least preimage, a rule; the return from an injection to a list goes through @lem-subsets-of-naturals, whose list is defined by recursion from least elements (@thm-well-ordering), again a rule. No line picks from infinitely many sets without a rule.
:::

The pattern is general: if one formula in \( n \) lists every \( A_n \), the family of lists is a single function, and no axiom is used. Choice enters only when each \( A_n \) is known to be countable as a bare existence statement.

## Algebraic numbers

The theorem pays off at once. A real number is called **algebraic** if it is a root of a non-zero polynomial with integer coefficients. To keep this inside what the book has defined, we speak of coefficient tuples. For \( d \ge 1 \) and \( c = (c_0, c_1, \dots, c_d) \in \nZ^{d+1} \) (a \( (d + 1) \)-tuple, entries numbered from \( 0 \)), let
\[
p_c(x) \coloneqq \sum_{k=0}^{d} c_k x^k \qquad (x \in \nR)
\]
(@def-sum-product, @def-power), and call \( c \) **non-zero** if \( c_k \ne 0 \) for some \( k \). Then \( x \in \nR \) is **algebraic** if \( p_c(x) = 0 \) for some \( d \ge 1 \) and some non-zero \( c \in \nZ^{d+1} \). Constant polynomials are left out without loss, since a non-zero constant has no roots.

For example, \( \sqrt 2 \) is algebraic, a root of \( x^2 - 2 \) (\( c = (-2, 0, 1) \)). Every rational \( m/n \) is algebraic, a root of \( nx - m \) (\( c = (-m, n) \)). So is \( \sqrt 2 + \sqrt 3 \), a root of \( x^4 - 10x^2 + 1 \).

We use one fact from school algebra, not proved here: **if \( c \in \nZ^{d+1} \) is non-zero, then \( p_c \) has at most \( d \) real roots**. (It follows from the factor theorem.) In particular the set \( R(c) \coloneqq \{ x \in \nR : p_c(x) = 0 \} \) is finite.

::: {#thm-algebraic-countable}
[The Algebraic Numbers Are Countable]

The set of algebraic real numbers is countable.
:::

::: {.idea}
Sort the polynomials by degree. For each \( d \), the coefficient tuples form a countable set, and each polynomial contributes finitely many roots: a countable union of finite sets. Then take the union over \( d \). Both unions are instances of @thm-countable-union (b).
:::

::: {.proof}
Let \( \mathrm{Alg} \) be the set of algebraic real numbers, and for \( d \ge 1 \) let \( Z_d \) be the set of non-zero tuples in \( \nZ^{d+1} \).

*Step 1.* Let \( d \ge 1 \). The set \( \nZ \) is countable (@thm-integers-rationals-countable), and \( \nZ^{d+1} \) is the product of \( d + 1 \ge 2 \) factors all equal to \( \nZ \), so it is countable by @cor-product-countable (b). Hence \( Z_d \subseteq \nZ^{d+1} \) is countable (@prp-countable-subset).

*Step 2.* For \( c \in Z_d \), the root set \( R(c) \) is finite by the school fact above, hence countable (@thm-countable-characterizations, (iii) \( \Rightarrow \) (i)). So \( \mathrm{Alg}_d \coloneqq \bigcup_{c \in Z_d} R(c) \), the set of roots of the non-zero polynomials of degree at most \( d \), is countable by @thm-countable-union (b), with the countable index set \( Z_d \).

*Step 3.* By definition, \( \mathrm{Alg} = \bigcup_{d \in \nZ_{>0}} \mathrm{Alg}_d \). The index set \( \nZ_{>0} \subseteq \nN \) is countable (@prp-countable-subset). So \( \mathrm{Alg} \) is countable by @thm-countable-union (b).
:::

The proof cites @thm-countable-union twice, and so it uses @ax-choice. Here the axiom can be avoided (not proved in the text; nothing later uses it): list each finite root set in increasing order, which is a rule, and replace the two unions by one fixed enumeration of all integer coefficient tuples. Exercise C2 asks you to carry this out. The countability of \( \mathrm{Alg} \) has a striking consequence once we know that \( \nR \) is not countable: Section 8.4 deduces that some real numbers are not algebraic.

## Exercises

### A. Check your understanding

::: {#exr-countable-unions-and-choice-a1}
[A1]

These parts are about the proof of @thm-countable-union.

::: {.enumerate options="label=(\alph*)"}
1. Which line of the proof of part (a) uses @ax-choice? What are the index set \( I \) and the sets \( A_i \) of the axiom at that line?
2. Why does the proof introduce the set \( J \)?
3. Run the proof on \( A_n \coloneqq \{ n, n + 1 \} \) for \( n \in \nN \), with the lists \( c(n)(m) \coloneqq n \) for odd \( m \) and \( c(n)(m) \coloneqq n + 1 \) for even \( m \). What is \( J \), and what is \( F(3, 2) \)?
4. State the idea of the proof in two sentences.
5. Is @ax-choice needed to show that \( \bigcup_{n \in \nN} A_n \) is countable when every \( A_n \) is a subset of \( \nN \)? Justify your answer.
:::
:::

::: {.solution}
(a) The line "By @ax-choice, applied to the family \( (S_n)_{n \in J} \), there is a function \( c \) on \( J \) with \( c(n) \in S_n \)". There \( I = J \), the set of indices with \( A_n \ne \emptyset \), and the sets of the axiom are the \( S_n \), the sets of surjections \( \nN \to A_n \). The axiom chooses lists, not elements of the \( A_n \).

(b) The axiom applies only to families of **non-empty** sets. If \( A_n = \emptyset \), there is no function \( \nN \to A_n \) at all (@prp-empty-function (b)), so \( S_n = \emptyset \), and the family \( (S_n)_{n \in \nN} \) would not qualify. Empty sets add nothing to the union, so restricting to \( J \) loses nothing.

(c) Every \( A_n \) is non-empty, so \( J = \nN \). The pair \( (3, 2) \) has \( m = 2 \) even, so \( F(3, 2) = c(3)(2) = 3 + 1 = 4 \). (Each \( c(n) \) is onto \( \{n, n + 1\} \): \( c(n)(1) = n \) and \( c(n)(0) = n + 1 \).)

(d) Choose, with the axiom, a list of each non-empty \( A_n \), all at once. The lists turn the countable grid \( J \times \nN \) into a surjection onto the union, so the union is countable.

(e) No. The union is a subset of \( \nN \), so it is countable by @prp-countable-subset. (Even the proof can run without the axiom: \( h_A(m) \coloneqq m \) for \( m \in A \) and \( h_A(m) \coloneqq \min A \) otherwise (@thm-well-ordering) is a rule that maps \( \nN \) onto any non-empty \( A \subseteq \nN \).)
:::

### B. Practice

::: {#exr-countable-unions-and-choice-b1}
[B1: Which constructions need choice?]

Determine which of the following constructions need @ax-choice. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. Choose a real number in each interval \( (n, n + 1) \), \( n \in \nN \).
2. Choose an element of each non-empty subset of \( \nN \).
3. Choose an element of each non-empty subset of \( \nR \).
4. Choose one of the two square roots of each positive real number.
:::
:::

::: {.solution}
(a) No. The rule \( n \mapsto n + \frac12 \) names an element of each interval, since \( n < n + \frac12 < n + 1 \).

(b) No. The rule "the least element" names one, by @thm-well-ordering: \( S \mapsto \min S \) is a choice function, defined by specification.

(c) Yes, as far as this book is concerned. The rule "the least element" fails, since \( (0, 1) \) has no least element, and no rule is known that names an element of every non-empty set of reals. A proof that needs such a function uses the axiom, and says so.

(d) No. The rule "the positive one" names one root of each \( y > 0 \): \( y \mapsto \sqrt y \).
:::

::: {#exr-countable-unions-and-choice-b2}
[B2: Finite sequences]

Prove that the set of all finite sequences of natural numbers is countable, and say whether your proof uses @ax-choice. Here a finite sequence of length \( k \in \nN \) is a function \( \{1, \dots, k\} \to \nN \), represented by its graph, a subset of \( \nZ_{>0} \times \nN \); the sequence of length \( 0 \) is \( \emptyset \).

*Hint: @thm-recursion, together with one fixed surjection \( \nN \to \nN \times \nN \).*
:::

::: {.solution}
Let \( \mathrm{Seq} \) be the set of \( x \in \powerset{\nZ_{>0} \times \nN} \) such that \( x \) is the graph of a function \( \{1, \dots, k\} \to \nN \) for some \( k \in \nN \) (@def-set-builder, @def-power-set). This \( k \) is determined by \( x \), since \( \{1, \dots, k\} \) is the set of first coordinates of \( x \), and \( k \) is its number of elements (@cor-finite-size-unique); call it the **length** of \( x \), and let \( \mathrm{Seq}_k \) be the set of elements of length \( k \). So \( \mathrm{Seq} = \bigcup_{k \in \nN} \mathrm{Seq}_k \), and \( \mathrm{Seq}_0 = \{\emptyset\} \).

*With choice.* Each \( \mathrm{Seq}_k \) is countable (for \( k \ge 2 \) it is in bijection with \( \nN^k \), by \( x \mapsto (x(1), \dots, x(k)) \); \( \mathrm{Seq}_1 \) with \( \nN \); \( \mathrm{Seq}_0 \) has one element), so @thm-countable-union (a) applies. This route uses @ax-choice, through the theorem.

*Without choice.* Fix one surjection \( \sigma \colon \nN \to \nN \times \nN \) (@thm-product-countable, @def-countable; a single \( \rulename{\exists E} \)), and write \( \sigma(n) = (\sigma_1(n), \sigma_2(n)) \). For \( x \in \mathrm{Seq} \) of length \( k \) and \( m \in \nN \), let \( x \frown m \coloneqq x \cup \{ (k + 1, m) \} \), the sequence \( x \) with \( m \) appended; it has length \( k + 1 \). Every \( y \in \mathrm{Seq}_{k+1} \) is \( x \frown m \) for \( x \) the restriction of \( y \) to \( \{1, \dots, k\} \) and \( m = y(k + 1) \).

Let \( X \coloneqq \mathrm{Seq}^{\nN} \), the set of functions \( \nN \to \mathrm{Seq} \), let \( a \in X \) be the constant function with value \( \emptyset \), and define \( g \colon \nN \times X \to X \) by
\[
g(k, s)(n) \coloneqq s\bigl(\sigma_1(n)\bigr) \frown \sigma_2(n) .
\]
By @thm-recursion there is a function \( k \mapsto s_k \) from \( \nN \) to \( X \) with \( s_0 = a \) and \( s_{k+1}(n) = s_k(\sigma_1(n)) \frown \sigma_2(n) \) for all \( k, n \in \nN \).

*Claim: for every \( k \in \nN \), \( s_k \) maps \( \nN \) onto \( \mathrm{Seq}_k \).* By @ax-induction on \( k \). For \( k = 0 \), every value of \( s_0 \) is \( \emptyset \), and \( \mathrm{Seq}_0 = \{\emptyset\} \). Assume the claim for \( k \). Each value \( s_{k+1}(n) = s_k(\sigma_1(n)) \frown \sigma_2(n) \) has length \( k + 1 \), because \( s_k(\sigma_1(n)) \) has length \( k \). Let \( y \in \mathrm{Seq}_{k+1} \), say \( y = x \frown m \) with \( x \in \mathrm{Seq}_k \). By the hypothesis there is \( j \) with \( s_k(j) = x \), and since \( \sigma \) is onto there is \( n \) with \( \sigma(n) = (j, m) \). Then \( s_{k+1}(n) = s_k(j) \frown m = y \). This proves the claim.

Now \( n \mapsto s_{\sigma_1(n)}(\sigma_2(n)) \) maps \( \nN \) onto \( \mathrm{Seq} \): for \( y \in \mathrm{Seq}_k \), the claim gives \( j \) with \( s_k(j) = y \), and some \( n \) has \( \sigma(n) = (k, j) \). So \( \mathrm{Seq} \) is countable. One surjection was named, and the lists \( s_k \) were defined from it by recursion: no choice is used. Either route earns full credit if the use of choice is reported correctly.
:::

::: {#exr-countable-unions-and-choice-b3}
[B3]

A **rational point** of the plane is a point of \( \nQ \times \nQ \). Prove that the set of lines in the plane that pass through two different rational points is countable. Does your proof use @ax-choice?
:::

::: {.solution}
Let \( D \coloneqq \{ (p, q) \in (\nQ \times \nQ) \times (\nQ \times \nQ) : p \ne q \} \). The set \( \nQ \times \nQ \) is countable by @thm-integers-rationals-countable and @cor-product-countable; so is its product with itself, again by @cor-product-countable, and so is the subset \( D \) (@prp-countable-subset). For \( (p, q) \in D \), let \( \mathrm{line}(p, q) \) be the line through \( p \) and \( q \), as a subset of \( \nR^2 \): \( \mathrm{line}(p, q) \coloneqq \{ p + t(q - p) : t \in \nR \} \). Two different points lie on exactly one line (school geometry), so the lines in question form the image \( \mathrm{line}(D) \), countable by @prp-countable-image. The map \( \mathrm{line} \) is a formula, so no choice is used.
:::

### C. Going deeper

::: {#exr-countable-unions-and-choice-c1}
[C1: Exit check: countable unions]

Prove that if \( A_n \) is countable for every \( n \in \nN \), then so is \( \bigcup_{n \in \nN} A_n \). Point to the step of your proof that uses @ax-choice.
:::

::: {.solution}
Let \( U \coloneqq \bigcup_{n \in \nN} A_n \) and \( J \coloneqq \{ n \in \nN : A_n \ne \emptyset \} \). If \( J = \emptyset \), then \( U = \emptyset \), which is countable. Let \( J \ne \emptyset \). For \( n \in J \), the set \( S_n \) of surjections \( \nN \to A_n \) is non-empty (@def-countable). **By @ax-choice**, applied to \( (S_n)_{n \in J} \), there is a function \( c \) on \( J \) with \( c(n) \in S_n \) for every \( n \in J \): a list of every \( A_n \) at once, which no finite number of \( \rulename{\exists E} \)'s gives. This is the step that uses the axiom.

Put \( F(n, m) \coloneqq c(n)(m) \in A_n \subseteq U \) for \( (n, m) \in J \times \nN \). It is onto \( U \): if \( x \in U \), then \( x \in A_n \) for some \( n \in \nN \) (@def-family-union-intersection), so \( n \in J \), and \( c(n)(m) = x \) for some \( m \), as \( c(n) \) is onto \( A_n \). Since \( J \subseteq \nN \) is countable (@prp-countable-subset), \( J \times \nN \) is countable (@cor-product-countable (a)) and non-empty, so some \( s \colon \nN \to J \times \nN \) is onto (@def-countable), and so is \( F \circ s \colon \nN \to U \) (@thm-composition-injective-surjective (b)). This is the proof of @thm-countable-union (a).

**Marking scheme.** (10 points)
- 1: handles the empty sets: the case where every \( A_n \) is empty, and the restriction to the non-empty ones before choosing.
- 3: obtains, by @ax-choice, a surjection onto \( A_n \) for every \( n \) simultaneously, and says at that line that the axiom is used.
- 2: defines a map from a set of pairs (or another index set) to the union.
- 2: shows that this map is onto the union.
- 2: shows that the index set is countable and non-empty, citing the product result, and concludes.
Through injections \( \iota_n \colon A_n \to \nN \): 1 for noting that they exist for every \( n \), empty \( A_n \) included (the empty function), so nothing is discarded; 3 for choosing all \( \iota_n \) by @ax-choice, flagged; 2 for \( x \mapsto (n_x, \iota_{n_x}(x)) \) into \( \nN \times \nN \), with \( n_x \) the least \( n \) with \( x \in A_n \) (@thm-well-ordering); 2 for its injectivity; 2 for concluding with @thm-product-countable and @thm-countable-characterizations, (ii) \( \Rightarrow \) (i).
Fatal errors (0 for the step): "for each \( n \) let \( f_n \) be a list of \( A_n \)" with no mention of choice, an unflagged infinite \( \rulename{\exists E} \) that no rule licenses (0 for the choice step); listing \( \nN \times \nN \) row by row, as in @exm-rows-first-listing (0 for the countability step).
:::

::: {#exr-countable-unions-and-choice-c2}
[C2: Algebraic numbers without choice]

Prove @thm-algebraic-countable without using @ax-choice.
:::

::: {.solution}
[Hint 1]

*Use @exr-countable-unions-and-choice-b2 to obtain, without choice, one surjection from \( \nN \) onto all coefficient tuples of all lengths together.*
:::

::: {.solution}
[Hint 2]

*For an algebraic \( r \), let \( n(r) \) be the least index whose tuple has \( r \) as a root; it exists by @thm-well-ordering.*
:::

::: {.solution}
Use the notation of @thm-algebraic-countable, and let \( \mathrm{Alg} \) be the set of algebraic numbers.

*One list of all coefficient tuples.* Let \( \mathrm{ZSeq} \) be defined as \( \mathrm{Seq} \) in @exr-countable-unions-and-choice-b2, with \( \nZ \) in place of \( \nN \), and let \( z \colon \nN \to \nZ \) be the bijection of @thm-integers-rationals-countable. Sending \( x \in \mathrm{Seq} \) to the sequence \( i \mapsto z(x(i)) \) maps \( \mathrm{Seq} \) onto \( \mathrm{ZSeq} \) (use \( z^{-1} \) entrywise to find a preimage), so \( \mathrm{ZSeq} \) is countable without choice, by that exercise and @prp-countable-image. Since \( \mathrm{ZSeq} \) is non-empty (it contains \( \emptyset \), the sequence of length \( 0 \)), fix one surjection \( \mu \colon \nN \to \mathrm{ZSeq} \) (@def-countable), a single \( \rulename{\exists E} \). A sequence \( y \) of length \( d + 1 \ge 2 \) is read as the tuple \( c = (y(1), \dots, y(d + 1)) \in \nZ^{d+1} \), and every such tuple arises; write \( p_y \coloneqq p_c \) and \( R(y) \coloneqq R(c) \). Call \( n \in \nN \) **good for** \( r \in \nR \) if \( \mu(n) \) has length at least \( 2 \), is non-zero, and \( p_{\mu(n)}(r) = 0 \). Then \( r \) is algebraic if and only if some \( n \) is good for \( r \), since \( \mu \) is onto.

*An injection, by rules.* For \( r \in \mathrm{Alg} \), let \( n(r) \) be the **least** \( n \in \nN \) that is good for \( r \) (@thm-well-ordering), and let
\[
\rho(r) \coloneqq \text{the number of elements of } \{ s \in R(\mu(n(r))) : s < r \} ,
\]
well defined because this set is a subset of the finite set \( R(\mu(n(r))) \) (@prp-subset-finite, @cor-finite-size-unique). Both are named by rules, so \( r \mapsto (n(r), \rho(r)) \) is a function \( \mathrm{Alg} \to \nN \times \nN \), defined by specification.

It is injective. Let \( r, r' \in \mathrm{Alg} \) with \( n(r) = n(r') \) and \( \rho(r) = \rho(r') \); call this common index \( n \), and suppose \( r \ne r' \), say \( r < r' \). Both are roots of \( p_{\mu(n)} \). The set \( \{ s \in R(\mu(n)) : s < r \} \) is a subset of \( \{ s \in R(\mu(n)) : s < r' \} \), and a proper one, since \( r \) lies in the second and not in the first. By @prp-subset-finite, the first has fewer elements: \( \rho(r) < \rho(r') \), a contradiction. So \( r = r' \).

Following it with the injection \( (m, k) \mapsto 2^m 3^k \) of @thm-product-countable gives an injection \( \mathrm{Alg} \to \nN \) (@thm-composition-injective-surjective (a)), so \( \mathrm{Alg} \) is countable by @thm-countable-characterizations, (ii) \( \Rightarrow \) (i). Apart from the single surjection \( \mu \), every object was named by a rule, so @ax-choice is not used.

**Marking scheme.** (10 points)
- 3: produces, without choice, one surjection (or injection) relating \( \nN \) to the coefficient tuples of **all** degrees at once, citing @exr-countable-unions-and-choice-b2 or an explicit coding.
- 3: assigns to each algebraic number its data (an index of a polynomial and a position among its roots) by **rules**, such as a least index and a count or the increasing order of the finite root set.
- 4: proves that the resulting map is injective (or a map onto \( \mathrm{Alg} \) surjective), concludes, and says why no step uses choice.
Fatal errors (0 for the step): citing @thm-countable-union, which uses the axiom; "for each polynomial (or each \( d \)), take a list" with no rule given.
:::

::: {#exr-countable-unions-and-choice-c3}
[C3: Finite unions]

::: {.enumerate options="label=(\alph*)"}
1. Prove, without @ax-choice, that for every finite set \( I \) and every family \( (A_i)_{i \in I} \) of countable sets, \( \bigcup_{i \in I} A_i \) is countable.
2. Explain in two sentences why your induction does not prove @thm-countable-union.
:::
:::

::: {.solution}
(a) We use @ax-induction on the number of elements of \( I \). Let \( P(n) \) be: "for every set \( I \) with \( n \) elements and every family \( (A_i)_{i \in I} \) of countable sets, \( \bigcup_{i \in I} A_i \) is countable".

*Base case.* A set \( I \) with \( 0 \) elements is empty, so \( \bigcup_{i \in I} A_i = \emptyset \), which is countable.

*Inductive step.* Assume \( P(n) \), and let \( I \) have \( n + 1 \) elements and \( (A_i)_{i \in I} \) be a family of countable sets. Since \( n + 1 \ge 1 \), \( I \ne \emptyset \); pick \( i_0 \in I \). Then \( I' \coloneqq I \setminus \{i_0\} \) has \( n \) elements (@cor-remove-point), so \( B \coloneqq \bigcup_{i \in I'} A_i \) is countable by \( P(n) \), applied to the family \( (A_i)_{i \in I'} \). Since \( I = I' \cup \{i_0\} \), an element lies in some \( A_i \) with \( i \in I \) exactly when it lies in \( B \) or in \( A_{i_0} \), so
\[
\bigcup_{i \in I} A_i = B \cup A_{i_0} ,
\]
which is countable by @prp-union-two-countable. So \( P(n + 1) \) holds, and @ax-induction gives \( P(n) \) for every \( n \). Each step makes finitely many \( \rulename{\exists E} \)'s, so no choice is used.

(b) The induction proves the statement for each finite number \( n \) of sets, and \( \nN \) is not finite (@exm-hilbert-hotel), so no instance of \( P(n) \) is about the family \( (A_n)_{n \in \nN} \). Writing \( \bigcup_{n \in \nN} A_n \) as the union of the finite unions \( A_0 \cup \dots \cup A_k \) does not help, since that needs a list of every finite union at once, which is a choice of infinitely many lists again.
:::

<!-- dependency ledger
ax-choice (claim): no rule makes infinitely many choices; a proof is finite | def-rules-existential (cited); ch06 Section 6.5
ax-choice (claim): independence (Goedel 1938, Cohen 1963); Zorn, well-ordering theorem | F2.4 (Zorn stated), ST.4 (equivalences proved), ST.5 (independence) (prose pointers)
ax-choice (claim): uses in Section 8.6, Chapters 11, 43, 67, 69 | Section 8.6, ch11, ch43, ch67, ch69 (prose pointers)
ax-choice (claim): (remark) sup approximation, one exists-E per n | ch11 (prose pointer; flagged there)
ax-choice (example): (0, 1) has no least element | Ch 7 Section 7.1, halving as for (0, 1]
ax-choice (claim): positive reals have non-negative square roots | school fact (Part 0 convention); proved in Ch 11
ax-choice (example): 0 | k iff k = 0 | def-divides (Ch 7), silent
ax-choice (claim): (finite case) 0 elements gives empty; n + 1 elements gives non-empty | def-finite (Section 8.1)
thm-surjection-right-inverse (claim): equivalence with the axiom | inline sketch; ST.4 (prose pointer)
thm-countable-union (proof): N is countable | def-countable, identity map
thm-countable-union (claim): R is not countable | Section 8.4 (prose pointer)
exm-choice-free-unions (solution): Q = {m/n : m in Z, n in Z_{>0}} | Ch 7 Section 7.1
exm-choice-free-unions (solution): injection to list by recursion from least elements | lem-subsets-of-naturals, thm-well-ordering (cited)
thm-algebraic-countable (proof): non-zero integer polynomial of degree <= d has <= d real roots | school fact (factor theorem), stated as not proved here
thm-algebraic-countable (claim): choice avoidable for Alg | inline sketch; C2 (pointer); unused
thm-algebraic-countable (claim): sqrt 2 + sqrt 3 is a root of x^4 - 10x^2 + 1 | verify/ch08/thm-algebraic-countable.py
exr-countable-unions-and-choice-a1 (solution): F(3, 2) = 4 | verify/ch08/exr-countable-unions-and-choice-a1.py
exr-countable-unions-and-choice-b1 (solution): n < n + 1/2 < n + 1 | school fact; verify/ch08/exr-countable-unions-and-choice-b1.py
exr-countable-unions-and-choice-b1 (solution): y > 0 has square roots sqrt y > 0 and -sqrt y | school fact (Part 0 convention); proved in Ch 11
exr-countable-unions-and-choice-b2 (solution): Seq_k in bijection with N^k | characteristic property of tuples (Ch 6)
exr-countable-unions-and-choice-b3 (solution): two points lie on exactly one line | school geometry
exr-countable-unions-and-choice-c1 (solution): N is countable | def-countable, identity map
exr-countable-unions-and-choice-c2 (solution): inverse of the bijection z | thm-bijection-iff-inverse (Ch 6), silent
-->
