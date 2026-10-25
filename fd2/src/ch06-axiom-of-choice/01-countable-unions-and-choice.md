# The Axiom of Choice

Chapter 4 avoided picking one element from each of infinitely many sets: every function it built was given by a formula, a least element, or a list fixed in advance. This chapter adds the one principle that allows such picking, the axiom of choice, and gathers the theorems that need it. Section 4.2 listed \( \nN \times \nN \), \( \nZ \) and \( \nQ \), and showed that a union of two countable sets is countable (@prp-union-two-countable). The next question is a union of **countably many** countable sets. The natural proof is short, and one of its steps cannot be justified by any rule met so far. This section isolates that step, adds the axiom that licenses it, shows how to tell a proof that needs the axiom from one that only seems to, and proves the four results this book draws from it: right inverses, comparing sizes by surjections, countable unions, and the place of \( \nN \) among the infinite sets.

## A union of countably many lists

Let \( A_0, A_1, A_2, \dots \) be countable sets, a family \( (A_n)_{n \in \nN} \) in the sense of @def-indexed-family. We want to prove that \( \bigcup_{n \in \nN} A_n \) is countable.

Here is the proof most people write first. List each set: \( A_n = \{ a_{n,0}, a_{n,1}, a_{n,2}, \dots \} \). Put \( a_{n,m} \) in row \( n \) and column \( m \) of an infinite grid. Every element of the union stands somewhere in the grid, and the grid is indexed by \( \nN \times \nN \), which is countable (@thm-product-countable). So the union is the image of a countable set, and it is countable.

Every step but the first, "list each set", is a result of Section 4.2. Where do the lists come from?

## The axiom of choice

None of the working rules (W1)–(W6) of Section 1.2 forms a set out of infinitely many arbitrary picks. The principle we add is the simplest statement that does.

*From any family of non-empty sets, one may pick one element from each set, all at once.*

::: {#ax-choice}
[Axiom of Choice]

Let \( I \) be a set, and let \( (A_i)_{i \in I} \) be a family of sets such that \( A_i \) is **non-empty** for **every** \( i \in I \). Then **there exists** a function
\[
c \colon I \to \bigcup_{i \in I} A_i \quad \text{with} \quad c(i) \in A_i \ \text{ for every } i \in I .
\]
Such a function \( c \) is called a **choice function** for the family.
:::

In symbols, with \( Y^X \) the set of functions of Section 2.1 and \( U \coloneqq \bigcup_{i \in I} A_i \):
\[
\forall i \in I \ (A_i \ne \emptyset) \ \to \ \exists c \in U^{I} \ \ \forall i \in I \ \ c(i) \in A_i .
\]

In words: the hypothesis says that each set of the family has an element; the conclusion says that **one** function picks an element of every \( A_i \) at the same time. The codomain, a set by (W3), only gives \( c \) somewhere to take its values. The axiom asserts that \( c \) exists and gives no recipe for it.

**Its status.** For finitely many indices the axiom adds nothing (proved below); for infinitely many it is a genuinely new principle. It can be neither proved nor refuted from the other axioms of set theory (Gödel, Cohen). Section 6.2 states Zorn's lemma, and Section 6.3 proves that Zorn's lemma gives the axiom and the well-ordering theorem; *Axiomatic Set Theory*, Chapter 4 proves the converse, and Chapter 5 surveys the independence results. This book uses the axiom openly on the main line, among other places: in this section, for right inverses, countable unions and infinite sets; in *Analysis on the Real Line*, Chapter 1, for sup approximations (the remark below); in *Measure, Integration, and Real Analysis*, Chapter 2, for the Vitali set; in the same volume, Chapter 10, through Zorn's lemma, for the Hahn–Banach theorem; and in *Functional Analysis*, Chapter 2, for Tychonoff's theorem. Each use is flagged at its line.

::: {.remark}
A corollary in *Analysis on the Real Line*, Chapter 1 gives, for each \( n \ge 1 \) separately, some \( a_n \in A \) with \( a_n > \sup A - \frac1n \): one \( \rulename{\exists E} \) per \( n \), and no axiom. Forming the **sequence** \( (a_n)_{n \ge 1} \) from these is a choice function for the family \( \bigl( \{ a \in A : a > \sup A - \tfrac1n \} \bigr)_{n \in \nZ_{>0}} \), an instance of @ax-choice with the countable index set \( I = \nZ_{>0} \). *Analysis on the Real Line*, Chapter 1 flags exactly this step.
:::

**Examples.**

1. *The empty family.* If \( I = \emptyset \), the empty function \( \emptyset \to \bigcup_{i \in \emptyset} A_i = \emptyset \) (@prp-empty-function (a)) is a choice function: the condition "for every \( i \in \emptyset \)" holds vacuously. No axiom is needed.
2. *A family with a rule.* Let \( I = \nZ_{>0} \) and \( A_n \coloneqq \{ k \in \nN : n \mid k, \ k \ne 0 \} \), the positive multiples of \( n \). Each \( A_n \) contains \( n \). The rule \( c(n) \coloneqq n \) is a choice function, defined by specification (@def-set-builder); no axiom is needed.
3. *A family with no rule in sight.* Let \( I \) be the set of non-empty subsets of \( \nR \), and \( A_S \coloneqq S \) for \( S \in I \). A choice function picks an element of every non-empty set of reals. "The least element" fails, since \( (0, 1) \) has none, and no rule that works for every \( S \) is known. Here the axiom supplies what the other rules do not.

**A non-example by minimal change.** In Example 2, add the index \( n = 0 \). The positive multiples of \( 0 \) form the empty set (\( 0 \mid k \) means \( k = 0 \)), so \( A_0 = \emptyset \), and no function can have \( c(0) \in A_0 \). Only the clause "\( A_i \) is non-empty for every \( i \)" fails, and without it the conclusion is false. That is why the proofs below remove the empty sets from a family before they choose. (Dropping "all at once" instead would leave nothing beyond the hypothesis.)

## When choice is not needed

Two kinds of construction look like choice and are not; telling them apart from a real use is the skill this section is for.

**Finitely many sets.** *For every finite set \( I \) and every family \( (A_i)_{i \in I} \) of non-empty sets, a choice function exists, with no appeal to the axiom.* For \( I = \{1, 2, 3\} \), three applications of \( \rulename{\exists E} \) name \( a_i \in A_i \), and \( \{ (1, a_1), (2, a_2), (3, a_3) \} \) is the graph of a choice function. For a finite set of arbitrary size we induct on its number of elements (@def-finite). Let \( P(n) \) be: "for every set \( I \) with \( n \) elements and every family \( (A_i)_{i \in I} \) of non-empty sets, there is a choice function". *Base case* \( P(0) \): a set with \( 0 \) elements is the image of a bijection from \( \{1, \dots, 0\} = \emptyset \), so it is empty, and the empty function is a choice function (Example 1). *Inductive step:* assume \( P(n) \), and let \( I \) have \( n + 1 \) elements. Then \( I \ne \emptyset \), since a bijection \( \{1, \dots, n + 1\} \to I \) has a value at \( 1 \); pick \( i_0 \in I \) by \( \rulename{\exists E} \). The set \( I' \coloneqq I \setminus \{i_0\} \) has \( n \) elements (@cor-remove-point), so \( P(n) \) gives a choice function \( c' \) for \( (A_i)_{i \in I'} \). Since \( A_{i_0} \ne \emptyset \), one more \( \rulename{\exists E} \) names \( a_0 \in A_{i_0} \). The graph of \( c' \) together with the pair \( (i_0, a_0) \), with codomain \( \bigcup_{i \in I} A_i \), is a function on \( I' \cup \{i_0\} = I \), because \( i_0 \notin I' \); and it is a choice function. So \( P(n + 1) \) holds, and @fd1:ax-induction gives \( P(n) \) for every \( n \in \nN \). Each step uses two \( \rulename{\exists E} \)'s and no new principle; the induction says nothing about an infinite \( I \), which has no number of elements.

**A rule that picks.** If one description names an element of each \( A_i \), the choice function is defined by specification (W1), as the set of pairs \( (i, a) \) with \( a \) the element named for \( i \). Typical rules: the **least element** of a non-empty set of natural numbers (@thm-well-ordering); the **non-negative** square root of a positive real; in a bisection, **the left half** if it has the property in question, and otherwise the right half. The first rule is how @thm-countable-characterizations passed from a surjection \( \nN \to A \) to an injection \( A \to \nN \) with no axiom: the least preimage is named, not chosen.

::: {.warning}
**Choice is not "picking an element".** "Let \( a \in A \)" is a single \( \rulename{\exists E} \) and needs no axiom; neither does picking from ten sets. The axiom is needed only for picking **one element from each of infinitely many sets, with no rule**. A proof that says "choose" need not use it, and one that never says "choose" may: "for each \( n \), let \( g_n \) be a list of \( A_n \)" is a use, however it is worded.
:::

The warning is the whole method; here it is as a checklist.

::: {#exm-method-name-the-choice}
[Method: name the choice]

**Template.** At each line that produces an object for each of many indices at once, ask whether one rule names it for every index: a formula, "the least", "the unique", or one list fixed in advance. If so, define the function by specification; no choice is used. If not, form the family \( (S_i) \) of non-empty sets of candidates and write "**by @ax-choice** there is \( c \) with \( c(i) \in S_i \)" at that line, in bold.

**When to use it.** A proof says "for each \( n \), let …", builds a sequence or a family of lists, or inverts a surjection.

**The usual failure.** An unflagged "for each \( n \), choose". Flagging a single \( \rulename{\exists E} \), or a rule, as a use. An empty \( S_i \) left in the family (the non-example above).
:::

::: {.check}
A proof says: "For each \( n \in \nN \) the set \( \{ k \in \nN : k^2 > n \} \) is non-empty; choose \( k_n \) in it." Does this line need @ax-choice? Rewrite it so that it plainly does not.
:::

::: {.solution}
No: it need not. The least element (@thm-well-ordering) names \( k_n \), and so does the formula \( k_n \coloneqq n + 1 \), since \( (n + 1)^2 = n^2 + 2n + 1 > n \). Either rewrite defines \( n \mapsto k_n \) by specification.
:::

::: {#exm-choice-or-rule}
[Choice or a rule?]

Which of the following needs @ax-choice?

::: {.enumerate options="label=(\alph*)"}
1. A function sending each non-empty finite set of reals to one of its elements.
2. A function sending each open interval \( \{ x \in \nR : a < x < b \} \) with \( a < b \) to a rational number in it.
3. A function sending each countably infinite subset \( A \subseteq \nR \) to a bijection \( \nN \to A \).
4. For a given family \( (A_n)_{n \in \nN} \) of non-empty subsets of \( \nQ \), a sequence with \( a_n \in A_n \) for every \( n \).
:::
:::

::: {.solution}
(a) No: \( S \mapsto \max S \), which exists by @prp-finite-max.

(b) No, once one list of \( \nQ \) is fixed. Take a surjection \( q \colon \nN \to \nQ \) (@thm-integers-rationals-countable, one \( \rulename{\exists E} \)). Between two reals lies a rational (a school fact; *Analysis on the Real Line*, Chapter 1 proves it), so \( \{ n \in \nN : a < q(n) < b \} \) is non-empty, and \( q \) of its least element (@thm-well-ordering) is named by a rule.

(c) Yes, as far as this book is concerned. Each \( A \) has bijections \( \nN \to A \) (@def-countably-infinite), but no rule names one for an arbitrary \( A \). The family \( (S_A) \) of sets of bijections, indexed by the countably infinite subsets of \( \nR \) (a set, by specification in \( \powerset{\nR} \)), consists of non-empty sets, and @ax-choice gives the function.

(d) No: with the same fixed \( q \), \( a_n \coloneqq q\bigl(\min \{ k \in \nN : q(k) \in A_n \}\bigr) \); the set is non-empty because \( A_n \ne \emptyset \) and \( q \) is onto.

One fixed list turns "pick an element" into "take the first one on the list", and that is a rule.
:::

## Right inverses

The first consequence settles the question Section 2.4 left open. By @prp-right-inverse-surjective, a function with a right inverse is surjective; the converse is where choice enters.

::: {#thm-surjection-right-inverse}
[Surjections Have Right Inverses]

Let \( f \colon X \to Y \) be a surjective function. Then \( f \) has a right inverse: there is a function \( g \colon Y \to X \) with \( f(g(y)) = y \) for every \( y \in Y \).
:::

::: {.idea}
A right inverse must name a preimage of every \( y \). The preimages of the points of \( Y \) form a family of sets indexed by \( Y \), each non-empty because \( f \) is onto. A choice function for that family is exactly a right inverse. This is the method of @exm-method-name-the-choice: for an arbitrary \( f \) no rule names a preimage, so the line is flagged.
:::

::: {.proof}
For \( y \in Y \), let \( P_y \coloneqq f^{-1}(\{y\}) = \{ x \in X : f(x) = y \} \) (@def-preimage). This defines a family \( (P_y)_{y \in Y} \) of subsets of \( X \), indexed by \( Y \). Each \( P_y \) is non-empty, since \( f \) is surjective (@def-surjective). **By @ax-choice** there is a function \( c \colon Y \to \bigcup_{y \in Y} P_y \) with \( c(y) \in P_y \) for every \( y \in Y \). The union is a subset of \( X \), so the graph of \( c \) is a subset of \( Y \times X \), and with codomain \( X \) it is a function \( g \colon Y \to X \) with \( g(y) = c(y) \) (@def-function). For every \( y \in Y \), \( g(y) \in P_y \), that is, \( f(g(y)) = y \). So \( f \circ g = \id_Y \), and \( g \) is a right inverse of \( f \) (@def-left-right-inverse (b)).
:::

Together with @prp-right-inverse-surjective: a function is surjective **if and only if** it has a right inverse. The theorem is in fact equivalent to the axiom: a right inverse of the projection \( (i, a) \mapsto i \), from the set of pairs with \( a \in A_i \) onto \( I \), is a choice function in disguise.

::: {.check}
Let \( f \colon \nZ \to \nN \), \( f(k) \coloneqq \abs{k} \). It is surjective. Does the existence of a right inverse of \( f \) need @ax-choice?
:::

::: {.solution}
No. Each \( n \in \nN \) has the preimage \( n \), and also \( -n \) when \( n > 0 \); the rule "take the non-negative one" names one of them: \( g(n) \coloneqq n \). Then \( f(g(n)) = \abs{n} = n \), so \( g \colon \nN \to \nZ \) is a right inverse, defined by a formula. The axiom is needed only when no such rule is available.
:::

## Comparing sizes by surjections

Right inverses give a second reading of \( \le \). Section 4.4 compared sizes by injections, and turned an injection \( A \to B \) into a surjection \( B \to A \) (@prp-injection-gives-surjection). This section supplies the converse, at the price of the axiom: the direction from a surjection to an injection uses @thm-surjection-right-inverse.

::: {#prp-card-le-surjection}
[Injections and Surjections]

Let \( A \) and \( B \) be sets with \( A \ne \emptyset \). Then \( \card{A} \le \card{B} \) if and only if there is a surjection \( B \to A \).
:::

::: {.proof}
\( (\Rightarrow) \) This half is @prp-injection-gives-surjection (Section 4.4); it uses no choice.

\( (\Leftarrow) \) Let \( g \colon B \to A \) be a surjection. By @thm-surjection-right-inverse, \( g \) has a right inverse \( h \colon A \to B \), so \( g \circ h = \id_A \); **this step uses @ax-choice**, through @thm-surjection-right-inverse. Then \( g \) is a left inverse of \( h \), so \( h \) is injective by @thm-left-inverse-iff-injective (a). Hence \( \card{A} \le \card{B} \). This proves the proposition.
:::

The hypothesis \( A \ne \emptyset \) is needed for \( (\Rightarrow) \) only, as Section 4.4 showed with \( A = \emptyset \), \( B = \{b\} \). The choice in \( (\Leftarrow) \) is genuine in general, but not for \( B = \nN \): a surjection from \( \nN \) has least preimages, a rule, which is how @thm-countable-characterizations went from (i) to (ii) without the axiom.

::: {.check}
Is \( \card{\{0, 1\}^{\nN}} \le \card{\powerset{\nN}} \)? Give an injection, and say whether your answer needed @prp-card-le-surjection.
:::

::: {.solution}
Yes. Send a sequence \( a \in \{0, 1\}^{\nN} \) to the set \( \{ n \in \nN : a(n) = 1 \} \). If two sequences give the same set, they take the value \( 1 \) at the same places, and so the value \( 0 \) at the same places too; hence they are equal (@prp-function-equality), and the map is injective. No appeal to @prp-card-le-surjection is needed: the definition asks for an injection, and we wrote one down. (The map is in fact a bijection, with inverse \( S \mapsto \ind_S \), by @thm-power-set-two-power with \( X = \nN \).)
:::

## Countable unions

Now the theorem the section opened with. The second form, with any countable index set, is the one used in practice.

::: {#thm-countable-union}
[Countable Unions of Countable Sets]

(a) Let \( (A_n)_{n \in \nN} \) be a family of sets such that \( A_n \) is countable for every \( n \in \nN \). Then \( \bigcup_{n \in \nN} A_n \) is countable.

(b) Let \( I \) be a countable set and \( (A_i)_{i \in I} \) a family of sets such that \( A_i \) is countable for every \( i \in I \). Then \( \bigcup_{i \in I} A_i \) is countable.
:::

::: {.idea}
[Scratch work]

This is the grid of the opening, with the lists supplied by the axiom.
① Throw away the empty sets: the axiom needs non-empty ones, and they add nothing to the union.
② For each remaining \( n \), the surjections \( \nN \to A_n \) form a non-empty set; choose one from each, all at once.
③ The chosen lists turn the grid \( J \times \nN \) into a surjection onto the union, and the grid is countable by Section 4.2.

Part (b) is part (a) after renumbering the index set by a list. As givens and goal, for (a):

| Givens | Goal |
|---|---|
| \( A_n \) countable for every \( n \) | \( \bigcup_{n \in \nN} A_n \) countable |
| \( J \coloneqq \{ n : A_n \ne \emptyset \} \); \( J \times \nN \) countable (@cor-product-countable) | a surjection \( F \colon J \times \nN \to \bigcup_{n \in \nN} A_n \) |
| for each single \( n \in J \): some surjection \( \nN \to A_n \) (one \( \rulename{\exists E} \) per \( n \)) | \( F(n, m) \coloneqq \) (a list of \( A_n \))\( (m) \), which needs every list at once, as one function \( n \mapsto c(n) \) |
| gap: from "for every \( n \) there is a list" to "there is one function giving a list for every \( n \)" | closed by @ax-choice on \( (S_n)_{n \in J} \), the only flagged line |

*Before reading on: which line uses choice, and why can \( \rulename{\exists E} \) not replace it?*
:::

::: {.proof}
(a) Let \( U \coloneqq \bigcup_{n \in \nN} A_n \) and \( J \coloneqq \{ n \in \nN : A_n \ne \emptyset \} \).

If \( J = \emptyset \), every \( A_n \) is empty, so \( U = \emptyset \), which is countable by @def-countable.

Suppose \( J \ne \emptyset \). For \( n \in J \), let
\[
S_n \coloneqq \{ h \in A_n^{\nN} : h \text{ is surjective} \} ,
\]
the set of surjections \( \nN \to A_n \) (@def-set-builder, with \( A_n^{\nN} \) the set of functions of Section 2.1). Since \( A_n \) is countable and non-empty, \( S_n \ne \emptyset \) (@def-countable). **By @ax-choice**, applied to the family \( (S_n)_{n \in J} \), there is a function \( c \colon J \to \bigcup_{n \in J} S_n \) with \( c(n) \in S_n \) for every \( n \in J \). This is the only line of the proof that uses the axiom.

Define \( F \colon J \times \nN \to U \) by \( F(n, m) \coloneqq c(n)(m) \). It takes values in \( U \): \( c(n) \) maps into \( A_n \subseteq U \). It is surjective: let \( x \in U \); then \( x \in A_n \) for some \( n \in \nN \) (@def-family-union-intersection), so \( A_n \ne \emptyset \) and \( n \in J \); since \( c(n) \) is a surjection onto \( A_n \), there is \( m \in \nN \) with \( c(n)(m) = x \), that is, \( F(n, m) = x \).

The set \( J \) is countable by @prp-countable-subset, as a subset of \( \nN \), which is countable (the identity is a surjection). So \( J \times \nN \) is countable by @cor-product-countable (a), and it is non-empty, since it contains \( (n_0, 0) \) for any \( n_0 \in J \). By @def-countable there is a surjection \( s \colon \nN \to J \times \nN \). Then \( F \circ s \colon \nN \to U \) is surjective (@thm-composition-injective-surjective (b)), and \( U \) is countable.

(b) Let \( U \coloneqq \bigcup_{i \in I} A_i \). If \( I = \emptyset \), then \( U = \emptyset \), which is countable. Otherwise @def-countable gives a surjection \( s \colon \nN \to I \); fix one. For \( n \in \nN \) put \( B_n \coloneqq A_{s(n)} \), a countable set. Then \( \bigcup_{n \in \nN} B_n = U \). \( (\subseteq) \) An element of \( B_n \) lies in \( A_{s(n)} \) with \( s(n) \in I \). \( (\supseteq) \) If \( x \in A_i \) with \( i \in I \), then \( i = s(n) \) for some \( n \in \nN \), because \( s \) is onto, and \( x \in B_n \). By (a), \( U \) is countable.
:::

The line in bold is the only use of the axiom. The surjections \( s \) of parts (a) and (b) are single objects, each named by one \( \rulename{\exists E} \). What needed the axiom was a surjection **for every** \( n \in J \) at once: \( \rulename{\exists E} \) supplies \( c(n) \) only inside the box of a fixed \( n \), and \( F \) needs all of them outside every such box. The set \( J \) is there because for \( A_n = \emptyset \) there is no function \( \nN \to A_n \) at all (@prp-empty-function (b)), so \( S_n = \emptyset \). The theorem completes the closure properties of countable sets: subsets, images, finite products, countable unions.

Neither hypothesis can be dropped: Section 4.3 shows that \( \nR \) is not countable, and \( \nR \) is the union of the single set \( \nR \), and also of the countable sets \( \{x\} \), \( x \in \nR \).

::: {.warning}
**The choice is of the lists, not of preimages.** A surjection \( \nN \to A \) gives least preimages by a rule (@thm-countable-characterizations), but only once the surjection is **in hand**. In @thm-countable-union, what is missing is the surjection itself, one for each \( A_n \), and the sets \( A_n \) need not be sets of natural numbers, so no "least" is available to name one.
:::

## Every infinite set contains a copy of the natural numbers

Every infinite set met so far contains a copy of \( \nN \), and Section 4.5 showed what such a copy does (@prp-copy-of-naturals-absorbs). Picking new elements one at a time looks like a proof that every infinite set has one; it is not one, since "one at a time" is a recursion whose step must pick a new element from every set \( X \setminus F \), \( F \) finite, at once. So the proof chooses once, on all non-empty subsets of \( X \). With @ax-choice it becomes a proof, and it gives two results: \( \nN \) is the smallest infinite size, and a set is infinite exactly when it is the same size as a proper part of itself.

The question has a goal theorem: we want to show that an infinite set \( X \) has a countably infinite subset, that is, a subset equinumerous with \( \nN \) (@def-countably-infinite). Equivalently, we want an injection \( \nN \to X \): its image is then such a subset.

::: {#thm-infinite-countable-subset}
[Infinite Sets Contain a Countably Infinite Subset]

Every infinite set \( X \) has a countably infinite subset. Equivalently, there is an injection \( \nN \to X \).
:::

::: {.idea}
The natural attempt picks \( x_0 \in X \), then \( x_1 \in X \setminus \{x_0\} \), then \( x_2 \in X \setminus \{x_0, x_1\} \), and so on. Each pick is possible, because a finite set cannot exhaust the infinite \( X \), and each single pick is one \( \rulename{\exists E} \). But "and so on" is a definition by recursion, and @thm-recursion needs a **function** \( g \) that says, once and for all, which new element to take after any finite stage. That function must pick an element from every non-empty set of the form \( X \setminus F \) at once, with no rule for doing so when \( X \) is arbitrary. So we let @ax-choice supply a choice function \( c \) on all non-empty subsets of \( X \) first, and then the recursion is an ordinary one, with \( c \) as its rule.
:::

::: {.proof}
Let \( X \) be infinite. The family \( (S)_{S \in \powerset{X} \setminus \{\emptyset\}} \), indexed by the non-empty subsets of \( X \) with each index as its own member, consists of non-empty sets, and its union is \( X \): every index is a subset of \( X \), and each \( x \in X \) lies in the index \( \{x\} \). **By @ax-choice** there is a function \( c \colon \powerset{X} \setminus \{\emptyset\} \to X \) with
\[
c(S) \in S \quad \text{for every non-empty } S \subseteq X .
\]
This is the one line of the proof that uses the axiom.

Define \( g \colon \nN \times \powerset{X} \to \powerset{X} \) by \( g(n, F) \coloneqq F \cup \{ c(X \setminus F) \} \) if \( F \ne X \), and \( g(n, F) \coloneqq F \) if \( F = X \). In the first case \( X \setminus F \) is non-empty, so \( c(X \setminus F) \) is defined; so \( g \) is a function. By @thm-recursion, applied with the set \( \powerset{X} \), the starting value \( \emptyset \) and this \( g \), there are sets \( F_n \subseteq X \), for \( n \in \nN \), with \( F_0 = \emptyset \) and \( F_{n+1} = g(n, F_n) \).

We show by induction (@fd1:ax-induction) that **\( F_n \) has exactly \( n \) elements, for every \( n \in \nN \)**. For \( n = 0 \), \( F_0 = \emptyset \) has \( 0 \) elements (@def-finite). Suppose \( F_n \) has \( n \) elements. Then \( F_n \) is finite and \( X \) is not, so \( F_n \ne X \), and \( F_{n+1} = F_n \cup \{ c(X \setminus F_n) \} \) with \( c(X \setminus F_n) \in X \setminus F_n \). This is a union of disjoint sets with \( n \) elements and \( 1 \) element, so \( F_{n+1} \) has \( n + 1 \) elements by @prp-disjoint-union-count.

In particular \( F_n \ne X \) for every \( n \in \nN \), so we may define
\[
x_n \coloneqq c(X \setminus F_n) \in X \setminus F_n , \qquad\text{and then}\qquad F_{n+1} = F_n \cup \{x_n\} .
\]
Hence \( F_n \subseteq F_{n+1} \) for every \( n \), and by induction on \( k \), \( F_m \subseteq F_{m+k} \) for all \( m, k \in \nN \).

Now let \( m, n \in \nN \) with \( m < n \). Then \( x_m \in F_{m+1} \subseteq F_n \), because \( m + 1 \le n \) (@lem-naturals-arithmetic (e)), so \( k \coloneqq n - (m + 1) \in \nN \) (@lem-naturals-arithmetic (d)) and \( F_{m+1} \subseteq F_{(m+1)+k} = F_n \); and \( x_n \notin F_n \). So \( x_m \ne x_n \). Hence \( n \mapsto x_n \) is an injection \( \nN \to X \). Its image \( \{ x_n : n \in \nN \} \subseteq X \) is equinumerous with \( \nN \), since \( n \mapsto x_n \) is a bijection from \( \nN \) onto it. This proves the theorem.
:::

The proof shows where the axiom enters and why one \( \rulename{\exists E} \) per step is not enough: \( \rulename{\exists E} \) names one element for one set, while the recursion needs \( g \) as a single function defined on every stage at once. Each \( F_n \) is then determined by \( c \); the only arbitrary thing is \( c \) itself.

**A non-example by a minimal change.** Run the same construction on the finite set \( X = \{a, b\} \), with \( a \ne b \). The choice function \( c \) and the recursion still make sense, since \( g \) is defined on every \( F \subseteq X \). But \( F_1 = \{ c(X) \} \) has one element, \( F_2 \) adds the other, so \( F_2 = X \), and from then on \( g \) leaves \( F_n \) unchanged. So \( x_2 = c(X \setminus F_2) = c(\emptyset) \) is not defined. The step that fails is "\( F_n \) is finite and \( X \) is not, so \( F_n \ne X \)", exactly where the hypothesis that \( X \) is infinite is used.

::: {.remark}
Compare *Analysis on the Real Line*, Chapter 1's proof that the real numbers cannot be listed. There, a given list is used to build nested closed intervals, and each interval is obtained from the previous one by an explicit rule (keep an outer third that misses the next point of the list), so no choice principle is involved. Here \( X \) is an arbitrary infinite set, and there is no rule available for picking an element of an arbitrary non-empty subset of it; the choice function **is** the rule.
:::

For a particular \( X \) a rule may exist: for \( X \subseteq \nN \), "the least element" is one (@thm-well-ordering), and then the proof needs no axiom. That the theorem cannot be proved in general from the other rules of set formation alone is a result of set theory; we state it without proof, and nothing depends on it.

## Consequences: the smallest infinite size

The theorem says \( \card{\nN} \le \card{X} \) for every infinite \( X \) (@def-card-le). Three consequences follow at once.

- **\( \nN \) is the smallest infinite size.** If \( X \) is infinite and \( \card{X} \le \card{\nN} \), then \( \card{X} = \card{\nN} \), by @thm-schroder-bernstein and the theorem. So no infinite set is strictly smaller than \( \nN \).
- **Countable sets are exactly the sets of size at most \( \card{\nN} \)**, by @thm-countable-characterizations, (i) \( \iff \) (ii). Combining with the first point: a countable set is finite or equinumerous with \( \nN \), which @thm-countable-characterizations (iii) already said.
- **An uncountable set is strictly bigger than \( \nN \).** If \( X \) is uncountable, then \( X \) is infinite (a finite set is countable, by @thm-countable-characterizations), so \( \card{\nN} \le \card{X} \); and \( \card{\nN} = \card{X} \) would make \( X \) countable. So \( \card{\nN} < \card{X} \). For example \( \card{\nN} < \card{\nR} \), since \( \nR \) is uncountable (@thm-reals-uncountable-decimal).

::: {.warning}
"Infinite" and "uncountable" are different words. \( \nQ \) is infinite (it contains \( \nN \), which is infinite by @exm-hilbert-hotel, and a subset of a finite set is finite, by @prp-subset-finite) and countable (@thm-integers-rationals-countable). Likewise "\( X \) contains a copy of \( \nN \)" is not "\( X \) is equinumerous with \( \nN \)": \( \nR \) contains \( \nN \), and \( \card{\nN} < \card{\nR} \) (as above).
:::

::: {.check}
Let \( X \) be uncountable. Is \( X \setminus \{x\} \) uncountable for every \( x \in X \)? Why must \( X \) have an element at all?
:::

::: {.solution}
\( X \ne \emptyset \), because \( \emptyset \) is countable by @def-countable. For \( x \in X \), if \( X \setminus \{x\} \) were countable, then \( X = (X \setminus \{x\}) \cup \{x\} \) would be a union of two countable sets, countable by @prp-union-two-countable. So \( X \setminus \{x\} \) is uncountable.
:::

## Infinite sets are the same size as a proper part

Section 4.1 proved that a finite set is never equinumerous with a proper subset (@thm-finite-no-proper-copy), and @exm-hilbert-hotel showed \( \nN \) doing exactly that. With @thm-infinite-countable-subset, the hotel can be built inside any infinite set: run it on the copy of \( \nN \), and leave everything else alone.

::: {#thm-infinite-iff-proper-subset}
[Infinite Sets and Proper Subsets]

A set \( X \) is infinite if and only if \( \card{X} = \card{Y} \) for some proper subset \( Y \subsetneq X \).
:::

::: {.idea}
One direction is already done: Section 4.1 showed that finite sets have no proper subset of their own size. For the other, take the copy \( x_0, x_1, x_2, \dots \) of \( \nN \) inside \( X \) and move every guest one room up, \( x_n \mapsto x_{n+1} \), as \( n \mapsto n + 1 \) does in the Quick check after @exm-hilbert-hotel. Room \( x_0 \) is vacated, and every point outside the copy stays where it is.
:::

::: {.proof}
\( (\Leftarrow) \) This is the contrapositive of @thm-finite-no-proper-copy: a finite set is not equinumerous with any proper subset, so a set that is equinumerous with one is not finite.

\( (\Rightarrow) \) Let \( X \) be infinite. By @thm-infinite-countable-subset (which uses @ax-choice) there is an injection \( s \colon \nN \to X \). By @prp-copy-of-naturals-absorbs (a), \( Y \coloneqq X \setminus \{s(0)\} \) has \( \card{Y} = \card{X} \), and \( Y \) is a proper subset, as \( s(0) \in X \setminus Y \). This proves the theorem.
:::

Together with Section 4.1, this gives a characterization of "infinite" that never mentions \( \nN \) or counting: a set is infinite precisely when some proper part of it is as big as the whole. The finite intuition "a part is smaller than the whole" is exactly the property that separates finite sets from infinite ones. The direction \( (\Rightarrow) \) used @ax-choice, through @thm-infinite-countable-subset; the direction \( (\Leftarrow) \) did not.

::: {.check}
Name a proper subset of \( \nR \) that is equinumerous with \( \nR \), and give a bijection.
:::

::: {.solution}
\( (-1, 1) \), with the bijection \( x \mapsto x/(1 + \abs{x}) \) of @exm-reals-open-interval. (Any interval with more than one point other than \( \nR \) itself works, by the same example.) No choice is needed for \( \nR \): the bijection is a formula.
:::

## Exercises

### A. Check your understanding

::: {#exr-countable-unions-and-choice-a1}
[A1]

These parts are about the proofs of @thm-countable-union, @thm-infinite-countable-subset and @thm-infinite-iff-proper-subset.

::: {.enumerate options="label=(\alph*)"}
1. Which line of the proof of part (a) of @thm-countable-union uses @ax-choice? What are the index set \( I \) and the sets \( A_i \) of the axiom at that line?
2. Why does the proof of @thm-countable-union introduce the set \( J \)?
3. Run the proof of @thm-countable-union on \( A_n \coloneqq \{ n, n + 1 \} \) for \( n \in \nN \), with the lists \( c(n)(m) \coloneqq n \) for odd \( m \) and \( c(n)(m) \coloneqq n + 1 \) for even \( m \). What is \( J \), and what is \( F(3, 2) \)?
4. Is @ax-choice needed to show that \( \bigcup_{n \in \nN} A_n \) is countable when every \( A_n \) is a subset of \( \nN \)? Justify your answer.
5. Where does the proof of @thm-infinite-countable-subset use @ax-choice? Why is one \( \rulename{\exists E} \) per step not enough?
6. The proof of @thm-infinite-iff-proper-subset passes the copy of \( \nN \) to @prp-copy-of-naturals-absorbs (a), whose proof moves each \( s(n) \) to \( s(n + 1) \) and fixes every other point. Write down the resulting bijection \( X \to X \setminus \{s(0)\} \) for \( X = \nZ \) and \( s(n) = n \) for \( n \in \nN \).
:::
:::

::: {.solution}
(a) The line "By @ax-choice, applied to the family \( (S_n)_{n \in J} \), there is a function \( c \) on \( J \) with \( c(n) \in S_n \)". There \( I = J \), the set of indices with \( A_n \ne \emptyset \), and the sets of the axiom are the \( S_n \), the sets of surjections \( \nN \to A_n \). The axiom chooses lists, not elements of the \( A_n \).

(b) The axiom applies only to families of **non-empty** sets. If \( A_n = \emptyset \), there is no function \( \nN \to A_n \) at all (@prp-empty-function (b)), so \( S_n = \emptyset \), and the family \( (S_n)_{n \in \nN} \) would not qualify. Empty sets add nothing to the union, so restricting to \( J \) loses nothing.

(c) Every \( A_n \) is non-empty, so \( J = \nN \). The pair \( (3, 2) \) has \( m = 2 \) even, so \( F(3, 2) = c(3)(2) = 3 + 1 = 4 \). (Each \( c(n) \) is onto \( \{n, n + 1\} \): \( c(n)(1) = n \) and \( c(n)(0) = n + 1 \).)

(d) No. The union is a subset of \( \nN \), so it is countable by @prp-countable-subset. (Even the proof can run without the axiom: \( h_A(m) \coloneqq m \) for \( m \in A \) and \( h_A(m) \coloneqq \min A \) otherwise (@thm-well-ordering) is a rule that maps \( \nN \) onto any non-empty \( A \subseteq \nN \).)

(e) At the line "By @ax-choice there is a function \( c \) with \( c(S) \in S \) for every non-empty \( S \subseteq X \)." One \( \rulename{\exists E} \) names one element of one non-empty set; that would give \( x_0 \), then \( x_1 \), and any finite number of steps. But @thm-recursion needs the step as a **function** \( g \), defined once for every stage \( F \) at once, before the sequence exists. Defining \( g \) means picking an element of \( X \setminus F \) for every such \( F \) simultaneously, and that is what the axiom provides.

(f) \( h(n) = n + 1 \) for \( n \in \nN \), and \( h(k) = k \) for \( k < 0 \). It maps \( \nZ \) onto \( \nZ \setminus \{0\} \): a positive \( m \) is \( h(m - 1) \), and a negative \( k \) is \( h(k) \). No choice is needed here: the copy of \( \nN \) inside \( \nZ \) is given.
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

*Claim: for every \( k \in \nN \), \( s_k \) maps \( \nN \) onto \( \mathrm{Seq}_k \).* By @fd1:ax-induction on \( k \). For \( k = 0 \), every value of \( s_0 \) is \( \emptyset \), and \( \mathrm{Seq}_0 = \{\emptyset\} \). Assume the claim for \( k \). Each value \( s_{k+1}(n) = s_k(\sigma_1(n)) \frown \sigma_2(n) \) has length \( k + 1 \), because \( s_k(\sigma_1(n)) \) has length \( k \). Let \( y \in \mathrm{Seq}_{k+1} \), say \( y = x \frown m \) with \( x \in \mathrm{Seq}_k \). By the hypothesis there is \( j \) with \( s_k(j) = x \), and since \( \sigma \) is onto there is \( n \) with \( \sigma(n) = (j, m) \). Then \( s_{k+1}(n) = s_k(j) \frown m = y \). This proves the claim.

Now \( n \mapsto s_{\sigma_1(n)}(\sigma_2(n)) \) maps \( \nN \) onto \( \mathrm{Seq} \): for \( y \in \mathrm{Seq}_k \), the claim gives \( j \) with \( s_k(j) = y \), and some \( n \) has \( \sigma(n) = (k, j) \). So \( \mathrm{Seq} \) is countable. One surjection was named, and the lists \( s_k \) were defined from it by recursion: no choice is used. Either route earns full credit if the use of choice is reported correctly.
:::

::: {#exr-countable-unions-and-choice-b4}
[B3: Prove or disprove]

Prove each true statement, naming each use of @ax-choice as in @exm-method-name-the-choice, and refute each false one with a concrete counterexample.

::: {.enumerate options="label=(\alph*)"}
1. If \( A_n \) is finite for every \( n \in \nN \), then \( \bigcup_{n \in \nN} A_n \) is countable.
2. If \( A_n \) is finite for every \( n \in \nN \), then \( \bigcup_{n \in \nN} A_n \) is finite.
3. Every surjection \( f \colon \nN \to Y \) has a right inverse that can be defined without @ax-choice.
4. If \( A_n \) is countable for every \( n \in \nN \), then \( \bigcup_{n \in \nN} A_n \) is countably infinite.
5. If \( A_n \ne \emptyset \) for every \( n \in \nN \) and \( \bigcup_{n \in \nN} A_n \) is finite, then \( A_m \cap A_n \ne \emptyset \) for some \( m \ne n \).
6. Every infinite set \( X \) admits a surjection \( X \to \nN \).
7. If a set \( X \) admits a surjection \( X \to \nN \), then \( X \) is countable.
:::
:::

::: {.solution}
(a) **True.** Finite sets are countable (@thm-countable-characterizations, (iii) \( \Rightarrow \) (i)), and @thm-countable-union (a) applies. That theorem uses @ax-choice.

(b) **False.** Take \( A_n \coloneqq \{n\} \): the union is \( \nN \), which is infinite (@exm-hilbert-hotel).

(c) **True.** For \( y \in Y \), the set \( f^{-1}(\{y\}) \subseteq \nN \) is non-empty, since \( f \) is onto, so \( g(y) \coloneqq \min f^{-1}(\{y\}) \) exists by @thm-well-ordering. This is a rule, and \( f(g(y)) = y \).

(d) **False.** Take \( A_n \coloneqq \{0\} \) for every \( n \): the union is \( \{0\} \), which is finite, hence not countably infinite: a bijection \( \nN \to \{0\} \) would make \( \nN \) finite (@prp-equinumerous-properties, @def-finite), against @exm-hilbert-hotel.

(e) **True, with no axiom.** The set \( U \coloneqq \bigcup_{n \in \nN} A_n \) is non-empty (it contains the elements of \( A_0 \)) and finite, say with \( k \ge 1 \) elements via a bijection \( \varphi \colon \{1, \dots, k\} \to U \) (one \( \rulename{\exists E} \)). Define \( c(n) \coloneqq \varphi\bigl(\min \{ j : \varphi(j) \in A_n \}\bigr) \) (@thm-well-ordering); the set is non-empty because \( A_n \ne \emptyset \) and \( \varphi \) is onto. This is a rule, and \( c(n) \in A_n \). If \( c \) were injective, \( \nN \) would be equinumerous with \( c(\nN) \subseteq U \), which is finite (@prp-subset-finite). Then \( \nN \) would be finite (@prp-equinumerous-properties, @def-finite), against @exm-hilbert-hotel. So \( c(m) = c(n) \) for some \( m \ne n \), and that element lies in \( A_m \cap A_n \). This is the pigeonhole idea of @exm-method-pigeonhole, with infinitely many pigeons.

(f) **True, using the axiom.** By @thm-infinite-countable-subset (which uses @ax-choice) there is an injection \( \nN \to X \). Since \( \nN \ne \emptyset \), @prp-injection-gives-surjection gives a surjection \( X \to \nN \); that step uses no choice. (Concretely, with the injection written \( n \mapsto x_n \): send \( x_n \) to \( n \) and every other point to \( 0 \).)

(g) **False.** \( x \mapsto \floor{\abs{x}} \), the integer part of \( \abs{x} \) (the \( m \in \nN \) with \( m \le \abs{x} < m + 1 \), a school fact), maps \( \nR \) onto \( \nN \) (each \( n \in \nN \) is the image of \( n \)), and \( \nR \) is uncountable (@thm-reals-uncountable-decimal). A surjection onto \( \nN \) says \( X \) is at least as big as \( \nN \), not at most.
:::

::: {#exr-infinite-sets-b2}
[B4: Absorbing a countable set]

Let \( X \) be infinite, and let \( C \) be countable with \( C \cap X = \emptyset \). Prove that \( \card{X \cup C} = \card{X} \).

*Hint: absorb \( C \) into a countably infinite subset of \( X \).*
:::

::: {.solution}
By @thm-infinite-countable-subset (using @ax-choice) there is an injection \( s \colon \nN \to X \); its image \( S \coloneqq s(\nN) \) is a countably infinite subset of \( X \). Now @prp-copy-of-naturals-absorbs (b) gives \( \card{X \cup C} = \card{X} \). The axiom enters only through the copy \( s \); the absorbing itself is a rule.
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

::: {#exr-countable-unions-and-choice-c3}
[C2: Finite unions]

::: {.enumerate options="label=(\alph*)"}
1. Prove, without @ax-choice, that for every finite set \( I \) and every family \( (A_i)_{i \in I} \) of countable sets, \( \bigcup_{i \in I} A_i \) is countable.
2. Explain in two sentences why your induction does not prove @thm-countable-union.
:::
:::

::: {.solution}
(a) We use @fd1:ax-induction on the number of elements of \( I \). Let \( P(n) \) be: "for every set \( I \) with \( n \) elements and every family \( (A_i)_{i \in I} \) of countable sets, \( \bigcup_{i \in I} A_i \) is countable".

*Base case.* A set \( I \) with \( 0 \) elements is the image of a bijection from \( \{1, \dots, 0\} = \emptyset \) (@def-finite), so it is empty and \( \bigcup_{i \in I} A_i = \emptyset \), which is countable.

*Inductive step.* Assume \( P(n) \), and let \( I \) have \( n + 1 \) elements and \( (A_i)_{i \in I} \) be a family of countable sets. A bijection \( \{1, \dots, n + 1\} \to I \) (@def-finite) has a value at \( 1 \), so \( I \ne \emptyset \); pick \( i_0 \in I \). Then \( I' \coloneqq I \setminus \{i_0\} \) has \( n \) elements (@cor-remove-point), so \( B \coloneqq \bigcup_{i \in I'} A_i \) is countable by \( P(n) \), applied to the family \( (A_i)_{i \in I'} \). Since \( I = I' \cup \{i_0\} \), an element lies in some \( A_i \) with \( i \in I \) exactly when it lies in \( B \) or in \( A_{i_0} \), so
\[
\bigcup_{i \in I} A_i = B \cup A_{i_0} ,
\]
which is countable by @prp-union-two-countable. So \( P(n + 1) \) holds, and @fd1:ax-induction gives \( P(n) \) for every \( n \). Each step makes finitely many \( \rulename{\exists E} \)'s, so no choice is used.

(b) The induction proves the statement for each finite number \( n \) of sets, and \( \nN \) is not finite (@exm-hilbert-hotel), so no instance of \( P(n) \) is about the family \( (A_n)_{n \in \nN} \). Writing \( \bigcup_{n \in \nN} A_n \) as the union of the finite unions \( A_0 \cup \dots \cup A_k \) does not help, since that needs a list of every finite union at once, which is a choice of infinitely many lists again.

**Marking scheme.** (10 points)
- 2: states \( P(n) \), quantified over all sets \( I \) with \( n \) elements and all families of countable sets.
- 1: base case.
- 2: shows \( I \ne \emptyset \), picks \( i_0 \) and shows that \( I \setminus \{i_0\} \) has \( n \) elements (@cor-remove-point).
- 2: proves \( \bigcup_{i \in I} A_i = B \cup A_{i_0} \).
- 1: applies \( P(n) \) and @prp-union-two-countable to conclude.
- 2: part (b), in two sentences.
Fatal error (0 for the step): an induction that "reaches" \( n = \nN \), or that treats \( \nN \) as a finite index set.
:::

::: {#exr-infinite-sets-c2}
[C3: Removing a countable set]

Let \( X \) be uncountable and let \( C \subseteq X \) be countable. Deduce from @exr-infinite-sets-b2 that \( \card{X \setminus C} = \card{X} \).
:::

::: {.solution}
The set \( X \setminus C \) is uncountable: otherwise \( X = (X \setminus C) \cup C \) would be a union of two countable sets, countable by @prp-union-two-countable, against the choice of \( X \). An uncountable set is infinite, since finite sets are countable (@thm-countable-characterizations). Now apply @exr-infinite-sets-b2 with \( X \setminus C \) in the role of \( X \) and \( C \) as the countable set, which is disjoint from \( X \setminus C \): \( \card{(X \setminus C) \cup C} = \card{X \setminus C} \), and the left side is \( \card{X} \) because \( C \subseteq X \). Here \( X \setminus C \) is given by no formula, so no explicit copy of \( \nN \) in it is available; the copy comes from @thm-infinite-countable-subset, which uses @ax-choice. For \( X = \nR \) and \( C = \nQ \) (@thm-integers-rationals-countable, @thm-reals-uncountable-decimal) this is \( \card{\nR \setminus \nQ} = \card{\nR} \), which Section 4.5, Exercise B5 (a) proves without the axiom, using the explicit copy \( n \mapsto \sqrt2 + n \).
:::

<!-- dependency ledger
ax-choice (claim): no rule makes infinitely many choices; a proof is finite | def-rules-existential (cited); F2.6 §01
ax-choice (claim): independence (Goedel 1938, Cohen 1963); Zorn, well-ordering theorem | F2.4 §02 (Zorn stated), F2.4 §03 (Zorn => AC, Zorn => well-ordering, proved), ST.4 (AC => Zorn), ST.5 (independence) (prose pointers)
ax-choice (claim): uses in F2.4 §01, AN1.1, MT.1, FA.3, FA.5 | F2.4 §01, AN1.1, MT.1, FA.3, FA.5 (prose pointers)
ax-choice (claim): (remark) sup approximation, one exists-E per n | AN1.1 (prose pointer; flagged there)
ax-choice (example): (0, 1) has no least element | F2.2 §01, halving as for (0, 1]
ax-choice (claim): positive reals have non-negative square roots | school fact (F1-F2 convention); proved in AN1.1
ax-choice (example): 0 | k iff k = 0 | def-divides (F2.1 §01), silent
ax-choice (claim): (finite case) 0 elements gives empty; n + 1 elements gives non-empty | def-finite (F2.3 §01)
thm-surjection-right-inverse (claim): equivalence with the axiom | inline sketch; ST.4 (prose pointer)
thm-countable-union (proof): N is countable | def-countable, identity map
thm-countable-union (claim): R is not countable | F2.3 §03 (prose pointer)
exr-countable-unions-and-choice-a1 (solution): F(3, 2) = 4 | verify/ch06/exr-countable-unions-and-choice-a1.py
exr-countable-unions-and-choice-b1 (solution): n < n + 1/2 < n + 1 | school fact; verify/ch06/exr-countable-unions-and-choice-b1.py
exr-countable-unions-and-choice-b1 (solution): y > 0 has square roots sqrt y > 0 and -sqrt y | school fact (F1-F2 convention); proved in AN1.1
exr-countable-unions-and-choice-b2 (solution): Seq_k in bijection with N^k | characteristic property of tuples (F2.1)
exr-countable-unions-and-choice-c1 (solution): N is countable | def-countable, identity map
exm-method-name-the-choice (example): (n + 1)^2 = n^2 + 2n + 1 exceeds n | arithmetic, school fact; verify/ch06/exr-countable-unions-and-choice-b4.py
exm-choice-or-rule (solution): between two reals lies a rational | school fact (F1-F2 convention); proved in AN1.1
exm-choice-or-rule (solution): the countably infinite subsets of R form a set | def-set-builder (F2.1 §02) in def-power-set (F2.1 §03)
exr-countable-unions-and-choice-b4 (solution): (e) c(n) = phi(min{j : phi(j) in A_n}) repeats; (c) least preimage is a right inverse | verify/ch06/exr-countable-unions-and-choice-b4.py
exr-countable-unions-and-choice-b4 (solution): (f) x_n -> n, others -> 0, is onto N | prp-injection-gives-surjection (F2.3 §04, cited); verify/ch06/exr-countable-unions-and-choice-b4.py
exr-countable-unions-and-choice-b4 (solution): (g) floor(|x|) maps R onto N | floor function, school fact (F1-F2 convention); thm-reals-uncountable-decimal (cited); verify/ch06/exr-countable-unions-and-choice-b4.py
thm-infinite-countable-subset (proof): the family (S) indexed by P(X) \ {empty}, union equal to X | def-indexed-family, def-family-union-intersection (F2.1 §03), used silently; ax-choice (cited)
thm-infinite-countable-subset (proof): a singleton {x} has 1 element | def-finite (cited): the bijection 1 -> x from {1}
thm-infinite-countable-subset (proof): F_m subset of F_(m+k), induction on k | inline (ax-induction, cited)
thm-infinite-countable-subset (claim): (remark) AN1.1's nested-interval proof uses an explicit rule | AN1.1 §07 (prose pointer; nothing depends on it)
thm-infinite-countable-subset (claim): (prose after the remark) the theorem is not provable without choice | set theory, stated without proof; nothing depends on it
thm-infinite-iff-proper-subset (proof): the hotel bijection X -> X \ {s(0)} | prp-copy-of-naturals-absorbs (a) (F2.3 §05, cited)
prp-card-le-surjection (proof): (=>) half, A != empty | prp-injection-gives-surjection (F2.3 §04, cited)
exr-infinite-sets-b2 (solution): absorbing C into the copy s(N) | prp-copy-of-naturals-absorbs (b) (F2.3 §05, cited); thm-infinite-countable-subset (cited, uses ax-choice)
exr-infinite-sets-c2 (solution): X \ C uncountable, hence infinite | prp-union-two-countable (cited), thm-countable-characterizations (cited)
exr-countable-unions-and-choice-c3 (solution): 0 elements gives empty; n + 1 elements gives non-empty; cor-remove-point; union of I = I' + {i_0} | def-finite (F2.3 §01, cited); cor-remove-point (cited); inline
exr-infinite-sets-c2 (claim): Section 4.5, Exercise B5 (a) proves the same without choice | F2.3 §05 (prose pointer; nothing depends on it)
exr-countable-unions-and-choice-a1 (solution): (f) h(n) = n + 1 on N, identity on negatives, onto Z \ {0} | inline; prp-copy-of-naturals-absorbs (a) (F2.3 §05, cited in the stem)
-->
