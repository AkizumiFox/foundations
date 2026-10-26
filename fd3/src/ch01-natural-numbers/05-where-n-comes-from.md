# Where \( \nN \) Comes From

Section 1.1 assumed one thing: that a Peano system exists (@ax-natural-numbers). Why should we believe it? Inside the real numbers there is one, the set \( \nN_{\nR} \) of *Sets and Functions* (@cor-omega-identification (a)); but that answer presupposes \( \nR \), an object far richer than the one it is meant to support. *Axiomatic Set Theory* gives a better answer: it builds a Peano system out of sets alone. This section describes that construction, without proofs. Nothing later in the book depends on it.

## Sets as the raw material

*Sets and Functions* used sets as a working language. Its Section 1.2 stated a short list of working rules (W1)–(W6) that say which sets exist: a set may be cut out of a given set by a property (@fd2:def-set-builder), finitely many objects may be listed, sets have unions, the subsets of a set form a set (@fd2:def-power-set), pairs from two sets form a product, and the number sets are sets. It did not derive these rules from more basic principles, and it took numbers and pairs as given objects. Two questions were left open: where these rules come from, and whether everything else, numbers and pairs included, is a set too.

Set theory answers both questions with a list of axioms. The construction below uses seven of them, each of which can be said in one line:

- **Extensionality.** Two sets with the same elements are equal (@fd2:def-set-equality, now an axiom).
- **Empty set.** There is a set with no elements, written \( \emptyset \).
- **Pairing.** For any sets \( a \), \( b \) there is a set \( \{a, b\} \) whose elements are exactly \( a \) and \( b \).
- **Union.** For any set \( \mathcal{S} \) of sets there is a set \( \bigcup \mathcal{S} \) of the elements of its members; with pairing it gives \( a \cup b \).
- **Power set.** For any set \( X \) there is a set \( \powerset{X} \) of all its subsets.
- **Specification.** For any set \( A \) and any property, the elements of \( A \) with that property form a set.
- **Infinity.** Some set contains \( \emptyset \) and is closed under one particular step, the successor below.

*Axiomatic Set Theory* states the rest of the list (replacement, foundation and choice) and proves everything this section only describes.

Two features of the list matter for us. First, every axiom but extensionality says that **some set exists**. All of them except the empty set and infinity build their set out of sets already given; infinity is the one axiom that hands us a set no finite chain of building steps reaches. Second, there is nothing on the list except sets: no numbers, no points, no pairs as separate objects. So if natural numbers are to exist in this world, they must be particular sets. The question is which ones.

The answer is a matter of choice, not discovery. We need a set \( \omega \), an element of it to call zero and a function on it to call the successor, such that the three satisfy (P3), (P4) and (P5) of @def-peano-system. By @thm-peano-categoricity, any two such choices are copies of each other, so it does not matter much which one we make. It only has to be made from the empty set by the operations on the list.

## Zero and the successor as sets

There is only one set we are given outright, so it plays zero. For the successor we need a step that always produces something new, and the axioms offer a natural one: add the set itself as a new element. From here through Exercise B2, \( 0 \) and \( \mathrm{S} \) stand for these sets, except in a sentence that names \( \nN \), \( \nN_{\nR} \) or \( \nR \), where they keep their usual meanings; elsewhere in the section, and in the rest of the book, they mean what they meant before:
\[
0 \coloneqq \emptyset , \qquad \mathrm{S}(x) \coloneqq x \cup \{x\} .
\]
The right-hand side is a set by pairing (with \( a = b = x \)) and union. The first few numerals then come out as follows:
\[
\begin{aligned}
1 &= \mathrm{S}(0) = \emptyset \cup \{\emptyset\} = \{0\} , \\
2 &= \mathrm{S}(1) = \{0\} \cup \{1\} = \{0, 1\} , \\
3 &= \mathrm{S}(2) = \{0, 1\} \cup \{2\} = \{0, 1, 2\} .
\end{aligned}
\]
The pattern is the point of the choice: *each numeral is the set of the numerals before it.* So \( n \) has exactly \( n \) elements, and "\( m \) comes before \( n \)" can be read as \( m \in n \). Thus \( 2 \in 3 \), and also \( 2 \subseteq 3 \), since every element of \( 2 \) is an element of \( 3 \).

This reading is a feature of this construction, not of the natural numbers. In \( \nN_{\nR} \) the question "is \( 2 \in 3 \)?" has no meaning, and a warning in Section 1.4 records that no theorem of this book asks it. These sets are called the **von Neumann numerals**.

::: {.check}
Write \( 3 \) using only \( \emptyset \) and braces. Is \( 1 \subseteq 3 \)? Is \( 3 \in 1 \)?
:::

::: {.solution}
\( 3 = \{\emptyset, \{\emptyset\}, \{\emptyset, \{\emptyset\}\}\} \). Yes, \( 1 \subseteq 3 \): the only element of \( 1 = \{0\} \) is \( 0 \), and \( 0 \in 3 \). No, \( 3 \notin 1 \): the only element of \( 1 \) is \( \emptyset \), and \( 3 \ne \emptyset \), since \( 3 \) has elements.
:::

## The least inductive set

We now want a set holding all the numerals and nothing else. The other axioms build \( 0 \), then \( 1 \), then \( 2 \), one at a time, each in finitely many steps. A set holding all of them at once is what the axiom of infinity is for, and its "particular step" is \( \mathrm{S} \).

A set \( I \) is **inductive** if \( \emptyset \in I \) and \( \mathrm{S}(x) \in I \) whenever \( x \in I \). The axiom of infinity says that an inductive set exists. It says nothing more, and in particular it does not say that its inductive set holds only numerals.

The cure is the move of @fd2:prp-smallest-closed-set, with \( I \) as the ambient set, \( \emptyset \) as the starting element and \( \mathrm{S} \) as the step. The inductive subsets of \( I \) form a set, cut out of \( \powerset{I} \) by specification, and their intersection is the smallest inductive subset of \( I \). *Axiomatic Set Theory* checks that it lies inside every inductive set, not only inside those contained in \( I \), and so does not depend on which \( I \) the axiom supplied. This least inductive set is called \( \omega \).

Is \( (\omega, \emptyset, \mathrm{S}) \) a Peano system? The three axioms fare differently.

- **(P5)** is leastness itself. A subset of \( \omega \) that contains \( \emptyset \) and is closed under \( \mathrm{S} \) is inductive, so it contains the least inductive set \( \omega \); hence it is \( \omega \).
- **(P3)** is immediate. Every \( \mathrm{S}(x) \) has \( x \) as an element, and \( \emptyset \) has none, so \( \mathrm{S}(x) \ne \emptyset \).
- **(P4)** is the real work. From \( x \cup \{x\} = y \cup \{y\} \) we want \( x = y \), and for arbitrary sets this needs care. For elements of \( \omega \) it holds because each \( n \in \omega \) has two properties that the pattern above suggests: an element of an element of \( n \) is an element of \( n \), and \( n \notin n \). *Axiomatic Set Theory* proves both by induction on \( \omega \), and (P4) follows from them.

With all three in hand, \( (\omega, \emptyset, \mathrm{S}) \) is a Peano system. By @thm-peano-categoricity it is a copy of \( (\nN, 0, \mathrm{S}) \), by exactly one isomorphism, which carries the von Neumann numeral \( n \) to the natural number \( n \). So the assumption @ax-natural-numbers is not a new article of faith: it follows from the axioms for sets. A reader who trusts them may read @ax-natural-numbers as a theorem.

::: {.warning}
**An inductive set need not be \( \omega \).** The axiom of infinity supplies *some* inductive set, which may hold much else. In the same way, \( \nR \) contains \( 0 \) and is closed under \( x \mapsto x + 1 \), and \( \nR \) is not \( \nN_{\nR} \). Arguments about natural numbers use leastness, that is (P5), and never closure alone.
:::

## Pairs as sets

One more object from *Sets and Functions* has to be found among the sets: the ordered pair. @fd2:def-ordered-pair took \( (a, b) \) as a new kind of object and asked only for its characteristic property, that \( (a, b) = (c, d) \) exactly when \( a = c \) and \( b = d \). Set theory has no new kinds of objects, so a pair must be a set built from \( a \) and \( b \).

The first idea, \( \{a, b\} \), fails at once: \( \{a, b\} = \{b, a\} \), so it cannot record which coordinate came first. The standard repair marks the first coordinate by giving it a set of its own:
\[
(a, b) \coloneqq \bigl\{ \{a\}, \{a, b\} \bigr\} .
\]
This is the **Kuratowski pair**. The singleton \( \{a\} \) names the first coordinate; the other member adds the second. When \( a = b \), both members are \( \{a\} \), and \( (a, a) = \{\{a\}\} \) has a single element. *Axiomatic Set Theory* proves the characteristic property for this definition, by comparing the members of two such sets case by case.

Once pairs are sets, so is everything built from them. The product \( A \times B \) is a set of pairs, cut out of \( \powerset{\powerset{A \cup B}} \) by specification. A function is a set of pairs (@fd2:def-function), so \( \nN \times \nN \), the operations \( + \) and \( \cdot \) of Section 1.2, and the isomorphisms of Section 1.4 are all sets. Chapter 2 of this volume needs none of this: it uses pairs only through the characteristic property of @fd2:def-ordered-pair.

::: {.check}
Is \( \{\{0\}\} \) an ordered pair? If so, of what?
:::

::: {.solution}
Yes: \( (0, 0) = \{\{0\}, \{0, 0\}\} = \{\{0\}\} \), since \( \{0, 0\} = \{0\} \). As a set, it is also \( \{1\} \), because \( 1 = \{0\} \).
:::

## Exercises

### A. Check your understanding

::: {#exr-where-n-comes-from-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. List the elements of \( \mathrm{S}(3) \).
2. True or false: \( 2 \in 3 \) and \( 2 \subseteq 3 \), for the von Neumann numerals.
3. Why can the set \( \{a, b\} \) not serve as the ordered pair \( (a, b) \)?
4. Which Peano axiom is "\( \omega \) is the least inductive set" in disguise?
:::
:::

::: {.solution}
(a) \( \mathrm{S}(3) = 3 \cup \{3\} \) has the elements \( 0 \), \( 1 \), \( 2 \), \( 3 \); it is the numeral \( 4 \).

(b) Both are true: \( 3 = \{0, 1, 2\} \) has \( 2 \) as an element, and the elements \( 0 \), \( 1 \) of \( 2 \) are elements of \( 3 \).

(c) It forgets the order: \( \{1, 2\} = \{2, 1\} \), while the pairs \( (1, 2) \) and \( (2, 1) \) must differ, by the characteristic property, since \( 1 \ne 2 \).

(d) (P5): a subset of \( \omega \) containing \( \emptyset \) and closed under \( \mathrm{S} \) is inductive, so by leastness it is all of \( \omega \).
:::

### B. Practice

::: {#exr-where-n-comes-from-b1}
[B1: Numerals by hand]

::: {.enumerate options="label=(\alph*)"}
1. Write \( \mathrm{S}(4) \) as a set of numerals. How many elements does the numeral \( n \) have, for \( n \le 5 \)?
2. Compute \( 2 \cup 3 \) and \( 2 \cap 3 \).
3. Is \( \{1\} \subseteq 3 \)? Is \( \{1\} \) one of the numerals \( 0, 1, \dots, 5 \)?
:::
:::

::: {.solution}
(a) \( \mathrm{S}(4) = \{0, 1, 2, 3\} \cup \{4\} = \{0, 1, 2, 3, 4\} \), the numeral \( 5 \). The numeral \( n \) is \( \{0, 1, \dots, n - 1\} \), and it has \( n \) elements: \( 0 = \emptyset \) has none, \( 1 = \{0\} \) has one, and so on, going up one numeral at a time. The step \( \mathrm{S}(k) = k \cup \{k\} \) gives one more element than \( k \) has, because \( k \notin k \): the elements of \( k \) are earlier numerals, which have fewer elements than \( k \), so none of them is \( k \). So \( 0, 1, \dots, 5 \) have \( 0, 1, \dots, 5 \) elements, and in particular they are all different.

(b) \( 2 = \{0, 1\} \) and \( 3 = \{0, 1, 2\} \), so \( 2 \cup 3 = \{0, 1, 2\} = 3 \) and \( 2 \cap 3 = \{0, 1\} = 2 \): the union is the larger numeral and the intersection the smaller.

(c) Yes, \( \{1\} \subseteq 3 \), since \( 1 \in 3 \). But \( \{1\} \) is none of the numerals \( 0, \dots, 5 \). It has one element, so by (a) the only candidate is \( 1 = \{0\} \); and \( \{1\} \ne \{0\} \), since their only elements \( 1 \) and \( 0 \) differ (\( 1 \) has an element, \( 0 \) has none).
:::

::: {#exr-where-n-comes-from-b2}
[B2: Pairs as sets]

Write \( (0, 1) \), \( (1, 0) \) and \( (1, 1) \) as Kuratowski pairs, using numerals where you can. Show directly that \( (0, 1) \ne (1, 0) \). How many elements does \( (a, b) \) have when \( a \ne b \), and when \( a = b \)?
:::

::: {.solution}
\( (0, 1) = \{\{0\}, \{0, 1\}\} = \{1, 2\} \), since \( \{0\} = 1 \) and \( \{0, 1\} = 2 \). Next, \( (1, 0) = \{\{1\}, \{1, 0\}\} = \{\{1\}, 2\} \), and \( (1, 1) = \{\{1\}, \{1, 1\}\} = \{\{1\}\} \).

The set \( 1 \) is an element of \( (0, 1) \). It is not an element of \( (1, 0) \): it is not \( \{1\} \), since \( 0 \in 1 \) while the only element of \( \{1\} \) is \( 1 \ne 0 \); and it is not \( 2 \), since \( 1 \in 2 \) while \( 1 \notin 1 = \{0\} \). So the two sets have different elements, and \( (0, 1) \ne (1, 0) \).

If \( a \ne b \), then \( \{a\} \ne \{a, b\} \), because \( b \) lies in the second and not in the first; so \( (a, b) \) has two elements. If \( a = b \), then \( (a, a) = \{\{a\}\} \) has one. (Note also that \( (0, 1) = \{1, 2\} \) is not a numeral, although both its elements are: it is not \( 0 = \emptyset \), since it has elements, and every other numeral \( \{0, 1, \dots, n - 1\} \) contains \( 0 \), which \( \{1, 2\} \) does not, since \( 1 \) and \( 2 \) have elements and \( 0 \) has none.)
:::

### C. Going deeper

::: {#exr-where-n-comes-from-c1}
[C1: Closed is not least]

Each of the sets \( \nR \), \( [0, \infty) \) and \( \nN_{\nR} \cup \{ n + \tfrac12 : n \in \nN_{\nR} \} \) contains \( 0 \) and is closed under \( x \mapsto x + 1 \). For each, with \( e = 0 \) and \( s(x) = x + 1 \), decide which of (P3), (P4), (P5) hold. Then find the least subset of \( \nR \) that contains \( 0 \) and is closed under \( x \mapsto x + 1 \), and prove that it is least.
:::

::: {.solution}
This exercise is about subsets of the real numbers of *Sets and Functions*, so it uses their arithmetic freely, as @cor-omega-identification (a) does; facts about \( \nN_{\nR} \) itself come from @fd2:lem-naturals-arithmetic.

*(P4)* holds in all three: \( x + 1 = y + 1 \) gives \( x = y \).

*(P3)* fails only in \( \nR \), where \( s(-1) = -1 + 1 = 0 \). In the other two sets, \( x + 1 = 0 \) would need \( x = -1 \). But every \( n \in \nN_{\nR} \) has \( n \ge 0 \) (@fd2:lem-naturals-arithmetic (a)), so \( -1 \notin \nN_{\nR} \), \( -1 \notin [0, \infty) \), and \( n + \tfrac12 \ge \tfrac12 > -1 \).

*(P5)* fails in all three. The subset \( \nN_{\nR} \) of each contains \( 0 \) and is closed under \( x \mapsto x + 1 \) (it lies in \( [0, \infty) \) by the same clause (a)), but it is not the whole set: it misses \( -1 \in \nR \) (as above), and \( \tfrac12 \), which lies in \( [0, \infty) \) and in the third set, by @fd2:lem-naturals-arithmetic (e) with \( n = 0 \) (no natural number lies strictly between \( 0 \) and \( 1 \)).

*The least such set is \( \nN_{\nR} \).* It contains \( 0 \) and is closed under \( x \mapsto x + 1 \). Let \( T \subseteq \nR \) be any set with these two properties. Then \( T \cap \nN_{\nR} \) contains \( 0 \), and it is closed: if \( n \in T \cap \nN_{\nR} \), then \( n + 1 \in T \) and \( n + 1 \in \nN_{\nR} \). By the set form of @fd1:ax-induction (the remark at the start of *Sets and Functions*, Section 3.1), the only such subset of \( \nN_{\nR} \) is \( \nN_{\nR} \) itself, so \( T \cap \nN_{\nR} = \nN_{\nR} \), that is, \( \nN_{\nR} \subseteq T \).

The three sets show the point of the warning above: closure under the step is cheap, and only the least closed set is the natural numbers.
:::

### R. Review

::: {#exr-categoricity-r1}
[R1]

Prove that \( \nN \setminus \{0\} \) is infinite.
:::

::: {.solution}
We read @fd2:def-infinite and @fd2:thm-finite-no-proper-copy on subsets of \( \nN \), through the citing rule of Section 1.4 (group (i)). Write \( A \coloneqq \nN \setminus \{0\} \) and \( B \coloneqq \nN \setminus \{0, 1\} \), where \( 1 = \mathrm{S}(0) \) (@def-omega-arithmetic (c)). Consider \( \mathrm{S} \) restricted to \( A \), with codomain \( B \). Its values lie in \( B \): for \( n \in A \), \( \mathrm{S}(n) \ne 0 \) by (P3) for \( \nN \) (@ax-natural-numbers), and \( \mathrm{S}(n) \ne \mathrm{S}(0) = 1 \) by (P4), since \( n \ne 0 \). It is injective by (P4). It is onto \( B \): if \( m \in B \), then \( m \ne 0 \), so \( m = \mathrm{S}(k) \) for some \( k \in \nN \) by @prp-peano-predecessor (a), and \( k \ne 0 \) because \( m \ne 1 = \mathrm{S}(0) \); so \( k \in A \). Hence it is a bijection \( A \to B \). The set \( B \) is a proper subset of \( A \): \( B \subseteq A \) is clear, and \( 1 \in A \), since \( 1 = \mathrm{S}(0) \ne 0 \) by (P3), while \( 1 \notin B \). By @fd2:thm-finite-no-proper-copy, a finite set is not equinumerous with any proper subset; so \( A \) is not finite, that is, it is infinite (@fd2:def-infinite).
:::

::: {#exr-categoricity-r2}
[R2]

Let \( D \colon \nN \to \nN \) be \( D(n) \coloneqq \mathrm{S}(\mathrm{S}(n)) \). Show that \( D \) has a left inverse and no right inverse. Write a left inverse down explicitly. Is it the only one?
:::

::: {.solution}
*No right inverse.* A function with a right inverse is surjective (@fd2:prp-right-inverse-surjective), and \( D \) is not: \( 0 \) is not a value, since \( D(n) = \mathrm{S}(\mathrm{S}(n)) \ne 0 \) by (P3) for \( \nN \).

*A left inverse.* Write \( 1 = \mathrm{S}(0) \) (@def-omega-arithmetic (c)). Let \( L \colon \nN \to \nN \) have the graph
\[
G \coloneqq \bigl\{ (n, k) \in \nN \times \nN : (n \in \{0, 1\} \text{ and } k = 0) \text{ or } n = \mathrm{S}(\mathrm{S}(k)) \bigr\} .
\]
Each \( n \in \nN \) has exactly one partner. If \( n = 0 \), the partner \( k = 0 \) works, and no \( k \) has \( 0 = \mathrm{S}(\mathrm{S}(k)) \), by (P3). If \( n = 1 \), the partner \( k = 0 \) works, and no \( k \) has \( \mathrm{S}(0) = \mathrm{S}(\mathrm{S}(k)) \): by (P4) that would give \( 0 = \mathrm{S}(k) \), against (P3). If \( n \notin \{0, 1\} \), then \( n \ne 0 \), so \( n = \mathrm{S}(m) \) for exactly one \( m \), by @prp-peano-predecessor (a); this \( m \) is not \( 0 \), since \( n \ne \mathrm{S}(0) \), so \( m = \mathrm{S}(k) \) for exactly one \( k \), by @prp-peano-predecessor (a) again. Thus \( n = \mathrm{S}(\mathrm{S}(k)) \) for exactly one \( k \). So \( L \) is a function (@fd2:def-function) with \( L(0) = L(1) = 0 \) and \( L(\mathrm{S}(\mathrm{S}(k))) = k \). Hence \( L(D(n)) = n \) for every \( n \in \nN \), that is, \( L \circ D = \id_{\nN} \): \( L \) is a left inverse of \( D \) (@fd2:def-left-right-inverse (a)). This matches @fd2:thm-left-inverse-iff-injective: \( D \) is injective, by (P4) applied twice, and \( \nN \ne \emptyset \).

*Not unique.* The values of a left inverse at \( 0 \) and \( 1 \) are never used, since neither is of the form \( D(n) \); setting \( L'(0) \coloneqq 5 \), \( L'(1) \coloneqq 0 \) and \( L'(\mathrm{S}(\mathrm{S}(k))) \coloneqq k \) gives another left inverse.
:::

::: {#exr-categoricity-r3}
[R3]

Let \( M = \{0, 1\} \), \( e = 0 \) and \( s(0) = s(1) = 1 \). Show that there is no function \( f \colon M \to \nN \) with \( f(0) = 0 \) and \( f(s(x)) = \mathrm{S}(f(x)) \) for every \( x \in M \). Which of the Peano axioms play the part, for definitions on \( \nN \), that a theorem about reading formulas plays for definitions on formulas?
:::

::: {.solution}
Suppose \( f \) exists. Taking \( x = 1 \), \( f(1) = f(s(1)) = \mathrm{S}(f(1)) \). But no \( n \in \nN \) has \( n = \mathrm{S}(n) \) (@prp-peano-predecessor (b)). So no such \( f \) exists. (Taking \( x = 0 \) instead gives \( f(1) = \mathrm{S}(0) = 1 \), so the two equations at the input \( 1 \) also contradict each other.)

The trouble is that \( 1 \) is built in two ways, as \( s(0) \) and as \( s(1) \), and the two ways ask for different values. In *Logic and Proof*, Chapter 4, @fd1:thm-structural-recursion defines functions on formulas, and what makes it work is @fd1:thm-unique-readability: each compound formula is built from its parts in exactly one way. On \( \nN \) the same job is done by (P3) and (P4): \( 0 \) is not a successor, so its value is not asked for twice, and a successor is the successor of exactly one number, so the equation at \( \mathrm{S}(n) \) asks for one thing. The structure \( M \) fails (P4), since \( s(0) = s(1) \), though it satisfies (P5).
:::

<!-- dependency ledger
exr-where-n-comes-from-c1 (solution): x + 1 = y + 1 gives x = y; -1 + 1 = 0; n + 1/2 >= 1/2 > -1 | real arithmetic, school fact of fd2 (as in cor-omega-identification (a))
exr-where-n-comes-from-c1 (solution): n >= 0 for n in N_R, so -1 not in N_R, N_R inside [0, inf); 1/2 not in N_R | fd2:lem-naturals-arithmetic (a), (e) with n = 0 (cited)
exr-where-n-comes-from-c1 (solution): a subset of N_R containing 0 and closed under n -> n + 1 is N_R | the remark opening fd2:ch03-01 (unlabeled; set form of fd1:ax-induction, cited)
exr-where-n-comes-from-c1 (solution): n in N_R gives n + 1 in N_R | (N S) in the description of N opening fd2:ch03-01 (school fact, fd2)
exr-categoricity-r1 (solution): def-infinite and thm-finite-no-proper-copy read on N | the citing rule of Section 1.4, group (i) (cor-omega-identification (b), (c))
exr-categoricity-r1 (solution): S is injective on N; 0 is not a value of S; S(n) = 1 = S(0) gives n = 0 | (P4), (P3) for N, ax-natural-numbers with def-peano-system (cited)
exr-categoricity-r1 (solution): 1 = S(0) | def-omega-arithmetic (c) (numerals)
exr-categoricity-r1 (solution): every m != 0 in N is S(k) for some k | prp-peano-predecessor (a) (cited)
exr-categoricity-r2 (solution): G is a set (a subset of N x N cut out by a property) | fd2:def-set-builder
exr-categoricity-r2 (solution): 1 = S(0); D = S o S injective; D(n) != 0; S(0) = S(S(k)) impossible | def-omega-arithmetic (c); (P4) twice, (P3) for N (cited)
exr-categoricity-r2 (solution): n not in {0, 1} is S(S(k)) for exactly one k | prp-peano-predecessor (a) twice (cited)
exr-categoricity-r3 (solution): f(1) = S(0) = 1 | def-omega-arithmetic (c) (numerals)
exr-categoricity-r3 (solution): (structure M) M satisfies (P5): the only subset of {0, 1} containing 0 and closed under s is {0, 1} | inline (a closed subset containing 0 contains s(0) = 1)
-->
