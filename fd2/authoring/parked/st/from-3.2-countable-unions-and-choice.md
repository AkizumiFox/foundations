# Parked: from old Section 3.2, Countable Unions and the Axiom of Choice

<!-- Parked from fd2 (layout-six-chapters.md §2, approved 2026-10-26). Not part of any book's src; nothing builds or scans it.
Old section: fd2 3.2 (02-countable-unions-and-choice.md)
Labels: exm-choice-free-unions, thm-algebraic-countable, exr-countable-unions-and-choice-c2
Intended home: ST.4 (the obstacle, rule by rule), ST.3 (algebraic numbers)
-->

## The obstacle, rule by rule

For a non-empty \( A_n \), "\( A_n \) is countable" says that **there exists** a surjection \( \nN \to A_n \) (@def-countable). To use it we apply \( \rulename{\exists E} \) (@fd1:def-rules-existential): we name the object and argue inside the box of that name. One \( \rulename{\exists E} \) names **one** surjection, for **one** \( n \).

- **Finitely many sets.** The proof of @prp-union-two-countable used two \( \rulename{\exists E} \)'s; for \( A_0, \dots, A_9 \) we could nest ten boxes.
- **All \( n \in \nN \) at once.** The grid needs a list of \( A_n \) for every \( n \), assembled into one object: a function that sends each \( n \) to a surjection \( \nN \to A_n \). A proof is a finite object. It cannot contain one \( \rulename{\exists E} \) for each of infinitely many indices, and no rule of *Logic and Proof*, Chapter 5 makes infinitely many choices in one step.

Two escape routes fail. *Recursion* (@thm-recursion) defines a function on all of \( \nN \) at once, but from a rule \( g \) given in advance, each value determined by the previous one. The list of \( A_{n+1} \) is not determined by the list of \( A_n \), and a rule producing a list of every \( A_{n+1} \) would already be the missing object. *Induction* on \( k \), with @prp-union-two-countable at each step, proves "for every \( k \), \( A_0 \cup \dots \cup A_k \) is countable" (Exercise C3 writes it out), but that is a statement about each \( k \) separately; nothing makes the lists for different \( k \) fit together.

Section 1.6 met the same wall: a right inverse of a surjection must pick a preimage of **every** point at once, and the rules could do that only for finitely many points, or when a rule names the preimage.

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
Sort the polynomials by degree. For each \( d \), the coefficient tuples form a countable set, and each polynomial contributes finitely many roots: a countable union of finite sets. Then take the union over \( d \). Both unions are instances of @thm-countable-union (b). Steps 2 and 3 are route (S) of @exm-method-list-it: each union is the image of a countable grid. Step 1 only cites closure under products and subsets.
:::

::: {.proof}
Let \( \mathrm{Alg} \) be the set of algebraic real numbers, and for \( d \ge 1 \) let \( Z_d \) be the set of non-zero tuples in \( \nZ^{d+1} \).

*Step 1.* Let \( d \ge 1 \). The set \( \nZ \) is countable (@thm-integers-rationals-countable), and \( \nZ^{d+1} \) is the product of \( d + 1 \ge 2 \) factors all equal to \( \nZ \), so it is countable by @cor-product-countable (b). Hence \( Z_d \subseteq \nZ^{d+1} \) is countable (@prp-countable-subset).

*Step 2.* For \( c \in Z_d \), the root set \( R(c) \) is finite by the school fact above, hence countable (@thm-countable-characterizations, (iii) \( \Rightarrow \) (i)). So \( \mathrm{Alg}_d \coloneqq \bigcup_{c \in Z_d} R(c) \), the set of roots of the non-zero polynomials of degree at most \( d \), is countable by @thm-countable-union (b), with the countable index set \( Z_d \).

*Step 3.* By definition, \( \mathrm{Alg} = \bigcup_{d \in \nZ_{>0}} \mathrm{Alg}_d \). The index set \( \nZ_{>0} \subseteq \nN \) is countable (@prp-countable-subset). So \( \mathrm{Alg} \) is countable by @thm-countable-union (b).
:::

The proof cites @thm-countable-union twice, and so it uses @ax-choice. Here the axiom can be avoided (not proved in the text; nothing later uses it): list each finite root set in increasing order, which is a rule, and replace the two unions by one fixed enumeration of all integer coefficient tuples. Exercise C2 asks you to carry this out. The countability of \( \mathrm{Alg} \) has a striking consequence once we know that \( \nR \) is not countable: Section 3.3 deduces that some real numbers are not algebraic.

## Exercises

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

<!-- dependency ledger
exm-choice-free-unions (solution): Q = {m/n : m in Z, n in Z_{>0}} | F2.2 §01
exm-choice-free-unions (solution): injection to list by recursion from least elements | lem-subsets-of-naturals, thm-well-ordering (cited)
thm-algebraic-countable (proof): non-zero integer polynomial of degree <= d has <= d real roots | school fact (factor theorem), stated as not proved here
thm-algebraic-countable (claim): choice avoidable for Alg | inline sketch; C2 (pointer); unused
thm-algebraic-countable (claim): sqrt 2 + sqrt 3 is a root of x^4 - 10x^2 + 1 | fd2/authoring/parked/st/verify/thm-algebraic-countable.py
exr-countable-unions-and-choice-c2 (solution): inverse of the bijection z | thm-bijection-iff-inverse (F2.1), silent
-->
