# Unions, Intersections, Complements and Families

Section 6.1 said what sets are, when two of them are equal, and when one lies inside another. It gave us ways to describe a single set, by listing or by a property cut out of an ambient set. This section makes new sets from old ones. Each connective of Chapter 1 gives a set operation: "or" gives the union, "and" gives the intersection, "and not" gives the difference. That observation is the thesis of the chapter: *the laws of sets are the laws of logic, read through membership*. We state it, prove the standard laws of set algebra from it, and then take the step analysis needs constantly, from two sets to a whole family of them, where "or" becomes "there exists" and "and" becomes "for all".

## Union, intersection and difference

Here is the standard example of a new set. Let \( A \) be the set of integers divisible by \( 2 \) and \( B \) the set of integers divisible by \( 3 \). Three natural questions about an integer \( x \) are: is it divisible by \( 2 \) **or** by \( 3 \)? by \( 2 \) **and** by \( 3 \)? by \( 2 \) **and not** by \( 3 \)? Each question collects integers into a set, and each set is built from \( A \) and \( B \) by one connective applied to the statements \( x \in A \) and \( x \in B \). The pattern does not depend on divisibility at all, so we name the three constructions once, for any sets.

*The union collects what lies in either set, the intersection what lies in both, the difference what lies in the first and not the second.*

::: {#def-set-operations}
[Union, Intersection, Difference]

Let \( A \) and \( B \) be sets.

::: {.enumerate options="label=(\alph*)"}
1. The **union** \( A \cup B \) is the set whose elements are exactly the objects lying in \( A \) **or** in \( B \): \( x \in A \cup B \iff (x \in A \vee x \in B) \).
2. The **intersection** \( A \cap B \) is the set \( \{ x \in A : x \in B \} \): so \( x \in A \cap B \iff (x \in A \wedge x \in B) \).
3. The **difference** \( A \setminus B \) is the set \( \{ x \in A : x \notin B \} \): so \( x \in A \setminus B \iff (x \in A \wedge x \notin B) \).
:::

Sets \( A \) and \( B \) are **disjoint** if \( A \cap B = \emptyset \). If \( A \subseteq X \), the difference \( X \setminus A \) is called the **complement of \( A \) in \( X \)**.
:::

In words, clause by clause. The union exists by the working rule (W3) of Section 6.1; it is not cut out of an ambient set, since its elements come from two sets at once. The intersection and the difference **are** cut out of an ambient set, namely \( A \), so they exist by specification (W1), and the description \( \{ x \in A : \dots \} \) names its ambient set as Section 6.1 requires. The "or" of the union is inclusive, as \( \vee \) always is: an object in both sets is in the union. "Disjoint" means "no common element".

The complement is always written \( X \setminus A \), with the ambient set \( X \) named. Many books write \( A^c \) and leave \( X \) to the reader, and a reader who guesses \( X \) wrongly gets a different set: the complement of \( [0, 1] \) in \( [0, 2] \) is \( (1, 2] \), and in \( \nR \) it is \( (-\infty, 0) \cup (1, \infty) \). There is no "complement of \( A \)" on its own: by Russell's theorem (@thm-russell) there is no set of everything outside \( A \) (such a set, joined with \( A \), would contain every set). So this book never writes \( A^c \).

Examples, simplest first, each checked against the membership conditions.

- **Finite sets.** For \( A = \{1, 2, 3\} \) and \( B = \{2, 4\} \): \( A \cup B = \{1, 2, 3, 4\} \), \( A \cap B = \{2\} \), \( A \setminus B = \{1, 3\} \), \( B \setminus A = \{4\} \). For instance \( 3 \in A \setminus B \) because \( 3 \in A \) and \( 3 \notin B \); and \( 4 \notin A \setminus B \) because \( 4 \notin A \).
- **Intervals.** For \( A = [0, 2] \) and \( B = [1, 3] \): \( A \cup B = [0, 3] \), \( A \cap B = [1, 2] \), \( A \setminus B = [0, 1) \). The last one shows how an endpoint behaves: \( 1 \in B \), so \( 1 \notin A \setminus B \), while every \( x \) with \( 0 \le x < 1 \) lies in \( A \) and not in \( B \).
- **Divisibility.** With \( A \) and \( B \) the multiples of \( 2 \) and of \( 3 \) in \( \nZ \), as in the opening, \( A \cap B \) is the set of multiples of \( 6 \) (this uses the school fact that an integer divisible by \( 2 \) and by \( 3 \) is divisible by \( 6 \)), and \( \nZ \setminus A \) is the set of odd integers, the complement of \( A \) in \( \nZ \).
- **Degenerate cases.** For every set \( A \): \( A \cup \emptyset = A \), \( A \cap \emptyset = \emptyset \), \( A \setminus \emptyset = A \), and \( A \setminus A = \emptyset \). Each is one line: for example, \( x \in A \setminus A \) would mean \( x \in A \) and \( x \notin A \), which is impossible, so \( A \setminus A \) has no element. They matter because \( \emptyset \) behaves for \( \cup \) as \( 0 \) does for \( + \), and for \( \cap \) as \( 0 \) does for \( \times \).

Three inclusions hold for all sets and are used without comment from now on:
\[
A \cap B \subseteq A \subseteq A \cup B, \qquad A \setminus B \subseteq A .
\]
Each is one element-chase that drops or adds a disjunct or a conjunct: if \( x \in A \cap B \), then \( x \in A \) (\( \rulename{\wedge E} \)); if \( x \in A \), then \( x \in A \cup B \) (\( \rulename{\vee I} \)); if \( x \in A \setminus B \), then \( x \in A \) (\( \rulename{\wedge E} \)).

A nonexample by minimal change: the "difference" of two sets is **not** "everything in one but not in both". The set \( \{ x \in A \cup B : \text{not both } x \in A \text{ and } x \in B \} \) is a different set: for \( A = \{1, 2, 3\} \) and \( B = \{2, 4\} \) it is \( \{1, 3, 4\} \), while \( A \setminus B = \{1, 3\} \). The element \( 4 \) is in the first and not in \( A \setminus B \), because the difference keeps only elements **of \( A \)**.

::: {.warning}
**The difference is not symmetric.** In general \( A \setminus B \ne B \setminus A \). With \( A = \{1\} \) and \( B = \{2\} \), \( A \setminus B = \{1\} \) and \( B \setminus A = \{2\} \), and the witness \( 1 \) lies in the first and not the second. In fact \( A \setminus B \) and \( B \setminus A \) are always disjoint, since an element of both would lie in \( A \) and not in \( A \); they are equal only when both are empty, that is, when \( A = B \).
:::

::: {.check}
Let \( X = \{1, 2, 3, 4, 5, 6\} \), \( A = \{1, 2, 3\} \), and \( B = \{2, 4, 6\} \). Compute \( A \cup B \), \( A \cap B \), \( X \setminus (A \cup B) \), and \( (X \setminus A) \cap (X \setminus B) \).
:::

::: {.solution}
\( A \cup B = \{1, 2, 3, 4, 6\} \) and \( A \cap B = \{2\} \). Then \( X \setminus (A \cup B) = \{5\} \). Also \( X \setminus A = \{4, 5, 6\} \) and \( X \setminus B = \{1, 3, 5\} \), whose intersection is \( \{5\} \). The last two answers agree. This is the two-set case of De Morgan's law for sets, which is proved for arbitrary families later in this section.
:::

## Laws of sets are laws of logic

Unwinding the three definitions turns every question about \( \cup \), \( \cap \), and \( \setminus \) into a question about \( \vee \), \( \wedge \), and \( \neg \). Here is the dictionary, with the notions of Section 6.1 included.

| On sets | Unwound through membership | Logic |
|---|---|---|
| \( x \in A \cup B \) | \( x \in A \vee x \in B \) | \( \vee \) |
| \( x \in A \cap B \) | \( x \in A \wedge x \in B \) | \( \wedge \) |
| \( x \in A \setminus B \) | \( x \in A \wedge \neg(x \in B) \) | \( \wedge \) and \( \neg \) |
| \( A = \emptyset \) | \( \forall x\, \neg(x \in A) \) | \( \neg \) under \( \forall \) |
| \( A \subseteq B \) | \( \forall x\, (x \in A \to x \in B) \) | \( \to \) under \( \forall \) |
| \( A = B \) | \( \forall x\, (x \in A \leftrightarrow x \in B) \) | \( \leftrightarrow \) under \( \forall \) |

The dictionary makes an idea precise. Fix an object \( x \) and write \( p \), \( q \), \( r \) for the statements \( x \in A \), \( x \in B \), \( x \in C \). Then membership of \( x \) in any set built from \( A \), \( B \), \( C \) by \( \cup \), \( \cap \), \( \setminus \) is a propositional formula in \( p \), \( q \), \( r \): for instance,
\[
x \in A \cap (B \cup C) \iff p \wedge (q \vee r) .
\]
Two such sets are equal if their membership formulas can each be derived from the other, for then \( x \) lies in one exactly when it lies in the other, and \( x \) was arbitrary. So a law of propositional logic, with letters replaced by membership statements, is a law of sets. That is the thesis of this chapter.

*The laws of sets are the laws of logic, read through membership.*

Here are the laws used most.

::: {#thm-set-algebra}
[Algebra of Sets]

For all sets \( A \), \( B \), and \( C \):

::: {.enumerate options="label=(\alph*)"}
1. (commutativity) \( A \cup B = B \cup A \) and \( A \cap B = B \cap A \);
2. (associativity) \( (A \cup B) \cup C = A \cup (B \cup C) \) and \( (A \cap B) \cap C = A \cap (B \cap C) \);
3. (distributivity) \( A \cap (B \cup C) = (A \cap B) \cup (A \cap C) \) and \( A \cup (B \cap C) = (A \cup B) \cap (A \cup C) \);
4. (differences) \( A \setminus (B \cup C) = (A \setminus B) \cap (A \setminus C) \) and \( A \setminus (B \cap C) = (A \setminus B) \cup (A \setminus C) \).
:::
:::

::: {.idea}
Each law is a propositional equivalence under \( \forall x \). Chapter 3 gives a uniform license for all of them at once: an equivalence that holds in every row of a truth table is derivable in both directions, by completeness, and a derived sequent may be used with its letters replaced by any statements. So one argument covers every law, and the table after the proof names, for each law, the equivalence it comes from. We also write out two laws in full, as element-chases, so that the reader sees what the uniform argument does: the first distributive law, and the second difference law, the one law whose element-chase needs a classical rule (the uniform argument uses one for every law, inside the proof of @thm-completeness).
:::

::: {.proof}
*The uniform argument.* Fix one of the eight equations, \( L = R \), and let \( \varphi \) and \( \psi \) be the propositional formulas in the atoms \( p, q, r \) that describe membership in \( L \) and in \( R \), as in the dictionary: for the first distributive law, \( \varphi = p \wedge (q \vee r) \) and \( \psi = (p \wedge q) \vee (p \wedge r) \). For (a)–(c), the semantic equivalence \( \varphi \equiv \psi \) is a clause of @prp-standard-equivalences, with \( p, q, r \) in the places of \( \varphi, \psi, \chi \): (f) for (a), (h) for (b), (g) for (c). For (d), it is checked by the truth table displayed below. By @def-semantic-equivalence, \( \varphi \models \psi \) and \( \psi \models \varphi \), so by @thm-completeness, \( \varphi \vdash \psi \) and \( \psi \vdash \varphi \). Now let \( x \) be arbitrary. By @def-derived-rule, each of these two sequents may be used with \( p \), \( q \), \( r \) replaced by the statements \( x \in A \), \( x \in B \), \( x \in C \); with @def-set-operations, the first gives \( x \in L \to x \in R \) and the second \( x \in R \to x \in L \). Hence \( x \in L \leftrightarrow x \in R \), and since \( x \) was arbitrary, \( L = R \) by @def-set-equality.

The truth table for (d), with the atoms in the book's order (T before F, the last atom alternating fastest):
\[
\begin{array}{ccc|cccc}
p & q & r & p \wedge \neg(q \vee r) & (p \wedge \neg q) \wedge (p \wedge \neg r) & p \wedge \neg(q \wedge r) & (p \wedge \neg q) \vee (p \wedge \neg r) \\
\hline
\mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} \\
\mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} \\
\mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} \\
\mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F}
\end{array}
\]
The fourth and fifth columns agree in every row, and so do the sixth and seventh. This proves all eight laws.

*The first distributive law, in full.* \( (\subseteq) \) Let \( x \in A \cap (B \cup C) \). Then \( x \in A \) and \( x \in B \cup C \), that is, \( x \in A \) and (\( x \in B \) or \( x \in C \)). By @prp-distributivity, with \( P \), \( Q \), \( R \) replaced by \( x \in A \), \( x \in B \), \( x \in C \), we get (\( x \in A \) and \( x \in B \)) or (\( x \in A \) and \( x \in C \)); that is, \( x \in A \cap B \) or \( x \in A \cap C \), so \( x \in (A \cap B) \cup (A \cap C) \). \( (\supseteq) \) The same chain read backwards, using the second sequent of @prp-distributivity. By @prp-subset-antisymmetric the two sets are equal.

*The second difference law, in full.* \( (\subseteq) \) Let \( x \in A \setminus (B \cap C) \). Then \( x \in A \) and \( \neg(x \in B \wedge x \in C) \). By @prp-de-morgan (d), \( x \notin B \) or \( x \notin C \) [\( \rulename{RAA} \), inside (d)]. So \( x \in A \) and (\( x \notin B \) or \( x \notin C \)), and by @prp-distributivity, (\( x \in A \) and \( x \notin B \)) or (\( x \in A \) and \( x \notin C \)); that is, \( x \in (A \setminus B) \cup (A \setminus C) \). \( (\supseteq) \) Let \( x \in (A \setminus B) \cup (A \setminus C) \). By the second sequent of @prp-distributivity, \( x \in A \) and (\( x \notin B \) or \( x \notin C \)). By @prp-de-morgan (c), \( \neg(x \in B \wedge x \in C) \), so \( x \notin B \cap C \), and \( x \in A \setminus (B \cap C) \). By @prp-subset-antisymmetric the two sets are equal.
:::

Each law is a propositional equivalence, and the table records where each comes from: the clause of @prp-standard-equivalences, and the derivations of Chapters 1 and 2, where they exist, that prove one or both directions directly.

| Law | Clause of @prp-standard-equivalences | Derived in Chapters 1–2 |
|---|---|---|
| \( A \cap B = B \cap A \) | (f) | @prp-and-commutes (either direction, letters exchanged) |
| \( A \cup B = B \cup A \) | (f) | @exm-disjunction-first-derivations (likewise) |
| \( (A \cap B) \cap C = A \cap (B \cap C) \) | (h) | @prp-and-associative (left to right) |
| \( (A \cup B) \cup C = A \cup (B \cup C) \) | (h) | @exm-disjunction-regroup (right to left) |
| \( A \cap (B \cup C) = (A \cap B) \cup (A \cap C) \) | (g) | @prp-distributivity (both directions) |
| \( A \cup (B \cap C) = (A \cup B) \cap (A \cup C) \) | (g) | none in the text (both directions are exercises in Chapters 1 and 2) |
| \( A \setminus (B \cup C) = (A \setminus B) \cap (A \setminus C) \) | (b), then regrouping of \( \wedge \) | @prp-de-morgan (a), (b) |
| \( A \setminus (B \cap C) = (A \setminus B) \cup (A \setminus C) \) | (b), then (g) | @prp-de-morgan (c), (d); @prp-distributivity |

The two difference laws look alike, but their element-chases are not alike. The first needs De Morgan's laws (a) and (b), which Section 2.5 derives without \( \rulename{RAA} \), followed by regrouping the conjunction \( x \in A \wedge (x \notin B \wedge x \notin C) \) into \( (x \in A \wedge x \notin B) \wedge (x \in A \wedge x \notin C) \), which takes only \( \rulename{\wedge E} \) and \( \rulename{\wedge I} \). The second needs De Morgan (d) in its \( (\subseteq) \) direction, and (d) is the one of the four De Morgan laws that Section 2.5 derives with \( \rulename{RAA} \); its \( (\supseteq) \) direction uses (c), derived without it. Knowing that \( x \) is not in both \( B \) and \( C \) does not by itself tell us which of the two it misses; De Morgan (d) supplies the answer "one of them", and it is the classical rule that supplies it.

The laws let us calculate with sets as with numbers, but more symmetrically: each of \( \cup \) and \( \cap \) distributes over the other, whereas \( \times \) distributes over \( + \) and not conversely. They also let us drop brackets: by associativity, \( A \cup B \cup C \) and \( A \cap B \cap C \) are unambiguous.

::: {.check}
Which propositional equivalence proves \( A \cap (A \cup B) = A \)? Is it one of the clauses of @prp-standard-equivalences?
:::

::: {.solution}
Membership in the left side is \( p \wedge (p \vee q) \), and in the right side \( p \). The equivalence \( p \wedge (p \vee q) \equiv p \) holds in all four rows: if \( p \) is true, both sides are true; if \( p \) is false, both are false. It is not one of the clauses of @prp-standard-equivalences, so the uniform argument applies with a two-atom truth table instead of a clause. (Directly: \( (\subseteq) \) is \( \rulename{\wedge E} \); \( (\supseteq) \) is \( \rulename{\vee I} \) followed by \( \rulename{\wedge I} \).) This is one of the absorption laws.
:::

## Power sets

The operations so far build sets whose elements are elements of the old sets. The next construction collects **sets** as elements. Many questions of analysis quantify over subsets: "every non-empty set of reals that is bounded above has a supremum" is a statement about all subsets of \( \nR \). So the subsets of a set deserve to be collected into one set.

::: {#def-power-set}
[Power Set]

Let \( X \) be a set. The **power set** of \( X \) is the set \( \powerset{X} \) whose elements are exactly the subsets of \( X \):
\[
S \in \powerset{X} \iff S \subseteq X .
\]
:::

The set exists by the working rule (W4) of Section 6.1. Its elements are sets, and "\( S \in \powerset{X} \)" is just another way of writing "\( S \subseteq X \)". Two elements are always present: \( \emptyset \in \powerset{X} \), because the empty set is a subset of every set, and \( X \in \powerset{X} \), because \( X \subseteq X \).

::: {#exm-power-set-small}
[Small power sets]

Compute \( \powerset{\emptyset} \), \( \powerset{\{\emptyset\}} \), and \( \powerset{\{1, 2\}} \).
:::

::: {.solution}
*\( \powerset{\emptyset} = \{\emptyset\} \).* The only subset of \( \emptyset \) is \( \emptyset \) itself: if \( S \subseteq \emptyset \), then an element of \( S \) would be an element of \( \emptyset \), so \( S \) has no elements, and \( S = \emptyset \) by @prp-empty-set-unique. And \( \emptyset \subseteq \emptyset \). So \( \powerset{\emptyset} \) has exactly one element, \( \emptyset \). It is **not** empty: the empty set has one subset.

*\( \powerset{\{\emptyset\}} = \{\emptyset, \{\emptyset\}\} \).* Let \( S \subseteq \{\emptyset\} \). Either \( \emptyset \in S \) or \( \emptyset \notin S \) (excluded middle, @prp-excluded-middle). If \( \emptyset \in S \), then \( S \) and \( \{\emptyset\} \) have the same elements (\( S \) has no element other than \( \emptyset \), since \( S \subseteq \{\emptyset\} \)), so \( S = \{\emptyset\} \). If \( \emptyset \notin S \), then \( S \) has no elements, so \( S = \emptyset \). Conversely, both \( \emptyset \) and \( \{\emptyset\} \) are subsets of \( \{\emptyset\} \).

*\( \powerset{\{1, 2\}} = \{\emptyset, \{1\}, \{2\}, \{1, 2\}\} \).* Let \( S \subseteq \{1, 2\} \). A subset of \( \{1, 2\} \) is determined by which of \( 1 \) and \( 2 \) it contains, by @def-set-equality, and for each of the two there are two cases, \( 1 \in S \) or \( 1 \notin S \), and \( 2 \in S \) or \( 2 \notin S \). The four combinations give \( S = \{1, 2\} \), \( \{1\} \), \( \{2\} \), \( \emptyset \). All four are subsets of \( \{1, 2\} \). So \( \powerset{\{1, 2\}} \) has exactly four elements.
:::

In each case the number of subsets is a power of two: \( 1 \), \( 2 \), \( 4 \), for sets with \( 0 \), \( 1 \), \( 2 \) elements, because each element is independently in or out. That a set with \( n \) elements has exactly \( 2^n \) subsets is proved in Chapter 8, where counting is made exact. The name "power set" comes from this count.

::: {.warning}
**The elements of \( \powerset{X} \) are subsets, not elements, of \( X \).** For \( X = \{1, 2\} \): \( 1 \in X \) but \( 1 \notin \powerset{X} \), since \( 1 \) is a number, not a subset; whereas \( \{1\} \in \powerset{X} \) and \( \{1\} \notin X \). The correct translations are \( a \in X \iff \{a\} \in \powerset{X} \), and \( S \subseteq X \iff S \in \powerset{X} \).
:::

## Families of sets

Analysis rarely stops at two or three sets. It intersects all the intervals \( (-t, t) \) with \( t > 0 \), or all the closed sets containing a given set, or all the subsets of \( \nR \) with some property. We need unions and intersections of many sets at once, and first a way to name "many sets at once".

::: {#def-indexed-family}
[Indexed Family]

Let \( I \) be a set. A **family of sets indexed by \( I \)**, written \( (A_i)_{i \in I} \), assigns to **each** \( i \in I \) a set \( A_i \). The set \( I \) is the **index set**, and \( A_i \) is the **member** of the family with index \( i \). If \( X \) is a set with \( A_i \subseteq X \) for every \( i \in I \), we speak of a **family of subsets of \( X \)**.
:::

Here "assigns" is used in its everyday sense. Section 6.4 makes it exact for a family of subsets of a set \( X \): such a family is a function \( I \to \powerset{X} \), \( i \mapsto A_i \), whose value at \( i \) is written \( A_i \). The parentheses follow the book's rule that ordered or indexed things go in parentheses; the family \( (A_i)_{i \in I} \) knows which set has which index, and two indices may carry the same set. Examples: for \( I = \{1, 2\} \) the family is just a pair of sets \( A_1, A_2 \); for \( I = (0, \infty) \) and \( A_t = (-t, t) \) it is a family of intervals, one for each positive real \( t \); for \( I = \nN \) it is a sequence of sets \( A_0, A_1, A_2, \dots \) (indexed from \( 0 \); the sequences of real numbers in Section 6.4 are indexed from \( 1 \)), which Chapter 7 treats as a sequence defined by recursion and Chapter 8 uses to form countable unions.

"Or" becomes "for some index", and "and" becomes "for every index".

*The union of a family collects what lies in at least one member; the intersection collects what lies in every member.*

::: {#def-family-union-intersection}
[Union and Intersection of a Family]

Let \( (A_i)_{i \in I} \) be a family of sets.

::: {.enumerate options="label=(\alph*)"}
1. The **union** \( \bigcup_{i \in I} A_i \) is the set whose elements are exactly the objects lying in \( A_i \) for **some** \( i \in I \):
\[
x \in \bigcup_{i \in I} A_i \iff \exists i \in I\ (x \in A_i).
\]
2. If \( (A_i)_{i \in I} \) is a family of subsets of a set \( X \), the **intersection** is
\[
\bigcap_{i \in I} A_i \coloneqq \{ x \in X : \forall i \in I\ (x \in A_i) \} .
\]
:::

For a set \( \sS \) whose elements are sets, \( \bigcup \sS \coloneqq \bigcup_{A \in \sS} A \); and for a **non-empty** set \( \sS \subseteq \powerset{X} \), \( \bigcap \sS \coloneqq \bigcap_{A \in \sS} A \). In both, the family is indexed by \( \sS \) itself, the member with index \( A \) being \( A \).
:::

In words, clause by clause. The union exists by (W3), like the union of two sets; when all \( A_i \subseteq X \), it may also be written \( \{ x \in X : \exists i \in I\ (x \in A_i) \} \), since then every element of the union lies in \( X \), and this form names its ambient set as Section 6.1 requires. The intersection is cut out of \( X \) by specification. The last sentence covers sets of sets that come with no index: \( \bigcap \sS \) is the set of objects lying in every set that belongs to \( \sS \). For example, Chapter 11 defines \( \nN \) inside \( \nR \) as \( \bigcap \sS \), where \( \sS \) is the set of all subsets of \( \nR \) that contain \( 0 \) and are closed under \( x \mapsto x + 1 \); \( \sS \) is non-empty because \( \nR \) itself belongs to it.

With two sets the new definitions give the old ones back. For \( I = \{1, 2\} \), "\( \exists i \in \{1, 2\} \) with \( x \in A_i \)" says "\( x \in A_1 \) or \( x \in A_2 \)", since an \( i \in \{1, 2\} \) is \( 1 \) or \( 2 \); so \( \bigcup_{i \in \{1, 2\}} A_i = A_1 \cup A_2 \), and likewise \( \bigcap_{i \in \{1, 2\}} A_i = A_1 \cap A_2 \). The dictionary gains two rows:

| On sets | Unwound through membership | Logic |
|---|---|---|
| \( x \in \bigcup_{i \in I} A_i \) | \( \exists i \in I\ (x \in A_i) \) | \( \exists \) |
| \( x \in \bigcap_{i \in I} A_i \), for \( x \in X \) | \( \forall i \in I\ (x \in A_i) \) | \( \forall \) |

**Why the intersection is taken inside \( X \).** The ambient set is not decoration; it is forced by the case \( I = \emptyset \). If \( I \) is empty, the condition \( \forall i \in I\ (x \in A_i) \) is **vacuously true** for every object \( x \): there is no index at which it could fail (Chapter 4, vacuous truth for \( \forall \)). A definition without an ambient set, "\( \bigcap_{i \in I} A_i = \) all \( x \) with \( \forall i \in I\ (x \in A_i) \)", would then describe the set of all objects, which @thm-russell forbids. Inside \( X \), the empty intersection is simply \( X \):
\[
\bigcap_{i \in \emptyset} A_i = X, \qquad \bigcup_{i \in \emptyset} A_i = \emptyset .
\]
The union needs no ambient set, because its condition \( \exists i \in \emptyset\ (x \in A_i) \) is false for every \( x \); the empty union is empty. For a **non-empty** index set the choice of \( X \) does not matter: if some \( i_0 \in I \) exists and \( x \) lies in every \( A_i \), then in particular \( x \in A_{i_0} \subseteq X \), so the condition "\( x \in X \)" adds nothing. Only the empty family sees \( X \), and there it must. This is also why \( \bigcap \sS \) above asks \( \sS \) to be non-empty: a set of sets with no index carries no ambient set with it.

### The smallest set closed under some steps

One use of the intersection pays a debt to Chapter 3. There, the formulas were described as the smallest collection of strings closed under (F1)–(F3) of @def-formula: the collection that contains the atoms and \( \bot \) and is closed under the building steps (F2) and (F3). What does "smallest" mean, and why does such a collection exist? Intersections answer both questions, in any setting of this kind.

Let \( X \) be a set, and consider some **starting elements** of \( X \) and some **steps**, each of which turns elements of \( X \) into an element of \( X \). Call a subset \( S \subseteq X \) **closed** if it contains the starting elements and, whenever a step is applied to elements of \( S \), the result lies in \( S \).

::: {#prp-smallest-closed-set}
[Smallest Closed Set]

Let \( X \) be a set with given starting elements and steps, and let \( \sS \subseteq \powerset{X} \) be the set of closed subsets of \( X \). Then \( \sS \) is non-empty, and \( M \coloneqq \bigcap \sS \) is closed and lies inside every closed set: \( M \) is the **smallest** closed subset of \( X \).
:::

::: {.idea}
An element of \( M \) is an object lying in every closed set. So \( M \) lies inside each closed set by its very definition, and each requirement of being closed, met by every closed set at once, is met by what they have in common.
:::

::: {.proof}
The set \( \sS \) is non-empty, since \( X \) itself is closed; so \( \bigcap \sS \) is defined (@def-family-union-intersection).

- **\( M \) lies inside every closed set.** If \( S \in \sS \) and \( x \in M \), then \( x \) lies in every member of \( \sS \), in particular in \( S \).
- **\( M \) is closed.** Each starting element lies in every \( S \in \sS \), hence in \( M \). If a step is applied to elements of \( M \), those elements lie in every \( S \in \sS \); since each such \( S \) is closed, the result lies in every \( S \in \sS \), hence in \( M \).

This proves the proposition.
:::

For Chapter 3, \( X \) is the set of all strings of symbols, the starting elements are the atoms and \( \bot \), and the steps are (F2) and (F3) of @def-formula; \( M \) is then the set of formulas. (That this \( M \) consists exactly of the strings with a formation sequence, as clause (F4) says, follows by strong induction along a formation sequence, @thm-strong-induction; we do not need it here.) For Chapter 11, \( X = \nR \), the starting element is \( 0 \), the step is \( x \mapsto x + 1 \), and \( M \) is \( \nN \), the set Chapter 11 works with.

### Worked examples with a real parameter

Families indexed by an interval of real numbers are the ones analysis meets most. In each example we guess the answer, then prove it by two inclusions; the union needs a **witness index** for each point, and the intersection needs, for each point outside the answer, an index whose member **excludes** it.

::: {#exm-families-real-parameter}
[Unions and intersections of intervals]

Show that:

::: {.enumerate options="label=(\alph*)"}
1. \( \bigcup_{t \in (0, 1)} [t, 1] = (0, 1] \);
2. \( \bigcap_{t \in (0, \infty)} (-t, t) = \{0\} \), inside \( X = \nR \);
3. \( \bigcap_{t \in (0, \infty)} (0, t) = \emptyset \), inside \( X = \nR \).
:::
:::

::: {.solution}
(a) \( (\subseteq) \) Let \( x \in \bigcup_{t \in (0, 1)} [t, 1] \). Then there is \( t \in (0, 1) \) with \( x \in [t, 1] \); choose such a \( t \). So \( 0 < t \le x \le 1 \), and \( x \in (0, 1] \).

\( (\supseteq) \) Let \( x \in (0, 1] \). We need an index \( t \in (0, 1) \) with \( t \le x \). Take \( t \coloneqq x/2 \). Then \( 0 < x/2 \le 1/2 < 1 \), so \( t \in (0, 1) \); and \( x/2 < x \le 1 \), so \( x \in [t, 1] \). Hence \( x \) lies in the union. (The witness depends on \( x \), which is allowed: the union asks for **some** index for each point.)

(b) \( (\supseteq) \) For every \( t > 0 \), \( -t < 0 < t \), so \( 0 \in (-t, t) \). Since \( t \) was arbitrary, \( 0 \) lies in the intersection.

\( (\subseteq) \) Let \( x \) lie in the intersection. For a real number, \( x < 0 \) or \( x = 0 \) or \( x > 0 \), and we argue by cases. If \( x < 0 \) or \( x > 0 \), then \( \abs{x} > 0 \), so \( t \coloneqq \abs{x} \) is an index, and \( x \in (-\abs{x}, \abs{x}) \) would give \( \abs{x} < \abs{x} \) (since \( x \) is \( \abs{x} \) or \( -\abs{x} \)), which is false; this contradicts the assumption that \( x \) lies in every member, so these cases cannot occur. In the remaining case \( x = 0 \), and \( x \in \{0\} \). The index \( t = \abs{x} \) depends on the point \( x \) it excludes.

(c) Let \( x \) lie in the intersection. With the index \( t = 1 \), \( x \in (0, 1) \), so \( x > 0 \). Then \( x \) is itself an index, and \( x \in (0, x) \) would give \( x < x \), which is false. So nothing lies in the intersection, and it is empty.
:::

Part (c) is a degenerate case worth remembering. Each interval \( (0, t) \) is non-empty, and the intervals are **nested**: \( (0, s) \subseteq (0, t) \) whenever \( s \le t \). Yet nothing lies in all of them. Chapter 11 meets the same phenomenon with a sequence of intervals, and it is why its nested interval theorem needs **closed** intervals.

A nonexample by minimal change. Close the left endpoint of (c): \( \bigcap_{t > 0} [0, t) = \{0\} \). The number \( 0 \) now lies in every member, since \( 0 \le 0 < t \); and any \( x \ne 0 \) is excluded as before (if \( x < 0 \), by \( [0, 1) \); if \( x > 0 \), by \( [0, x) \)). One endpoint changes the answer from \( \emptyset \) to \( \{0\} \), and the element that (c) loses is exactly the endpoint \( 0 \).

::: {.check}
Compute \( \bigcup_{t \in [1, 2]} [0, t] \) and \( \bigcap_{t \in [1, 2]} [0, t] \), inside \( X = \nR \).
:::

::: {.solution}
The union is \( [0, 2] \): each \( [0, t] \subseteq [0, 2] \) since \( t \le 2 \), and \( [0, 2] \) is itself a member (\( t = 2 \)). The intersection is \( [0, 1] \): \( [0, 1] \subseteq [0, t] \) for every \( t \ge 1 \), and \( [0, 1] \) is itself a member (\( t = 1 \)). In general, when the members are nested and there is a largest and a smallest member, the union is the largest and the intersection the smallest.
:::

## De Morgan's laws for families

The laws of set algebra have versions for families, and the most used are De Morgan's laws: the complement of a union is the intersection of the complements, and the complement of an intersection is the union of the complements. In analysis they convert statements about open sets into statements about closed sets, and back. By the dictionary, they should be the quantifier negation laws of Chapter 4, read through membership: "not in some \( A_i \)" is "outside every \( A_i \)", and "not in every \( A_i \)" is "outside some \( A_i \)".

::: {#thm-de-morgan-families}
[De Morgan's Laws for Families]

Let \( X \) be a set and \( (A_i)_{i \in I} \) a family of subsets of \( X \), with any index set \( I \), including \( I = \emptyset \). Then
\[
X \setminus \bigcup_{i \in I} A_i = \bigcap_{i \in I} (X \setminus A_i)
\quad\text{and}\quad
X \setminus \bigcap_{i \in I} A_i = \bigcup_{i \in I} (X \setminus A_i) .
\]
:::

All intersections here are taken inside \( X \); the family \( (X \setminus A_i)_{i \in I} \) is again a family of subsets of \( X \), so both sides make sense.

::: {.idea}
Unwind both sides of each law through membership, for an element \( x \in X \). In the first law, the left side says \( \neg\exists i \in I\ (x \in A_i) \), and the right side says \( \forall i \in I\ \neg(x \in A_i) \). In the second, the left side says \( \neg\forall i \in I\ (x \in A_i) \), and the right side says \( \exists i \in I\ \neg(x \in A_i) \). So each law is a quantifier negation law, and each inclusion is one of its directions. We write the first law out rule by rule, since it is the chapter's model element-chase for families, and the second at level 3, tagging only the step it is about.

*Before reading on: which law of Chapter 4 turns "not in every \( A_i \)" into "outside some \( A_i \)", and which of its directions is classical?*
:::

::: {.proof}
*First law.* \( (\subseteq) \) Let \( x \in X \setminus \bigcup_{i \in I} A_i \) [\( \rulename{\forall I} \) and \( \rulename{{\to}I} \), opening]. By @def-set-operations, \( x \in X \) and \( x \notin \bigcup_{i \in I} A_i \) [\( \rulename{{\leftrightarrow}E} \), \( \rulename{\wedge E} \)]. Let \( i \in I \) [\( \rulename{\forall I} \) for the bounded \( \forall i \in I \) (@prp-bounded-quantifier-rules), opening]. Suppose \( x \in A_i \) [\( \rulename{\neg I} \), opening]. Then \( \exists j \in I\ (x \in A_j) \), with \( i \) as the witness [\( \rulename{\exists I} \)], so \( x \in \bigcup_{j \in I} A_j \) by @def-family-union-intersection [\( \rulename{{\leftrightarrow}E} \)]. This contradicts \( x \notin \bigcup_{j \in I} A_j \) [\( \rulename{\neg E} \)]. Hence \( x \notin A_i \) [\( \rulename{\neg I} \), closing]. With \( x \in X \), this gives \( x \in X \setminus A_i \) [\( \rulename{\wedge I} \), \( \rulename{{\leftrightarrow}E} \)]. Since \( i \in I \) was arbitrary, \( \forall i \in I\ (x \in X \setminus A_i) \) [\( \rulename{\forall I} \), closing]. With \( x \in X \), this is \( x \in \bigcap_{i \in I} (X \setminus A_i) \) by @def-family-union-intersection [\( \rulename{\wedge I} \), \( \rulename{{\leftrightarrow}E} \)]. Since \( x \) was arbitrary, the inclusion holds [\( \rulename{{\to}I} \), \( \rulename{\forall I} \), closing].

\( (\supseteq) \) Let \( x \in \bigcap_{i \in I} (X \setminus A_i) \) [\( \rulename{\forall I} \) and \( \rulename{{\to}I} \), opening]. Then \( x \in X \), and \( x \in X \setminus A_i \) for every \( i \in I \) [\( \rulename{{\leftrightarrow}E} \), \( \rulename{\wedge E} \)]. Suppose \( x \in \bigcup_{i \in I} A_i \) [\( \rulename{\neg I} \), opening]. Then there is \( i \in I \) with \( x \in A_i \); choose such an index \( i_0 \) [\( \rulename{\exists E} \), opening, with the new name \( i_0 \)]. Applying the hypothesis at \( i_0 \), \( x \in X \setminus A_{i_0} \) [\( \rulename{\forall E} \)], so \( x \notin A_{i_0} \) [\( \rulename{{\leftrightarrow}E} \), \( \rulename{\wedge E} \)], which contradicts \( x \in A_{i_0} \) [\( \rulename{\neg E} \)]. The contradiction \( \bot \) does not mention \( i_0 \), so it stands outside the choice [\( \rulename{\exists E} \), closing]. Hence \( x \notin \bigcup_{i \in I} A_i \) [\( \rulename{\neg I} \), closing], and with \( x \in X \), \( x \in X \setminus \bigcup_{i \in I} A_i \) [\( \rulename{\wedge I} \), \( \rulename{{\leftrightarrow}E} \)]. Since \( x \) was arbitrary, the inclusion holds [\( \rulename{{\to}I} \), \( \rulename{\forall I} \), closing].

By @prp-subset-antisymmetric, the first law holds.

*Second law.* \( (\subseteq) \) Let \( x \in X \setminus \bigcap_{i \in I} A_i \), so \( x \in X \) and \( x \notin \bigcap_{i \in I} A_i \). Then \( \forall i \in I\ (x \in A_i) \) fails: if it held, then together with \( x \in X \) it would put \( x \) in \( \bigcap_{i \in I} A_i \). By the bounded quantifier negation law of Chapter 4 (\( \neg\forall i \in I\ \varphi \) gives \( \exists i \in I\ \neg\varphi \), the bound kept), there is \( i \in I \) with \( x \notin A_i \) [\( \rulename{RAA} \), inside the quantifier negation law]. Choose such an index \( i_0 \). Then \( x \in X \setminus A_{i_0} \), so \( x \in \bigcup_{i \in I} (X \setminus A_i) \), with \( i_0 \) as the witness.

\( (\supseteq) \) Let \( x \in \bigcup_{i \in I} (X \setminus A_i) \), and choose \( i_0 \in I \) with \( x \in X \setminus A_{i_0} \). Then \( x \in X \) and \( x \notin A_{i_0} \). If \( x \) were in \( \bigcap_{i \in I} A_i \), then \( x \in A_{i_0} \) by the definition, applied at \( i_0 \); so \( x \notin \bigcap_{i \in I} A_i \), and \( x \in X \setminus \bigcap_{i \in I} A_i \).

By @prp-subset-antisymmetric, the second law holds. This proves the theorem.
:::

The answer to the prompt: the bounded quantifier negation law of Chapter 4 turns \( \neg\forall i \in I \) into \( \exists i \in I\ \neg \), and that direction is classical because it rests on the unbounded law \( \neg\forall x\, \varphi \vdash \exists x\, \neg\varphi \), which needs \( \rulename{RAA} \). It is used once, in the \( (\subseteq) \) half of the second law. The first law and the \( (\supseteq) \) half of the second use no classical rule: they are the directions of quantifier negation that Chapter 4 derives without \( \rulename{RAA} \). The pattern is the one met in the difference laws of @thm-set-algebra, which are the case \( I = \{1, 2\} \), \( X = A \), \( A_1 = A \cap B \), \( A_2 = A \cap C \) (replacing \( B \) and \( C \) by \( A \cap B \) and \( A \cap C \) changes neither side): "not in every member" does not by itself name the member it misses.

**The empty family.** The theorem was stated for every index set, and the conventions of @def-family-union-intersection are what make that true. For \( I = \emptyset \), the first law reads \( X \setminus \emptyset = X \), since the empty union is \( \emptyset \) and the empty intersection is \( X \); and the second reads \( X \setminus X = \emptyset \), since the empty intersection is \( X \) and the empty union is \( \emptyset \). Both are true. Had the empty intersection been defined as anything other than \( X \), the laws would have needed the hypothesis \( I \ne \emptyset \).

::: {.warning}
**De Morgan swapped the wrong way.** "The complement of a union is the union of the complements" is false. Take \( X = \{1, 2\} \), \( A_1 = \{1\} \), \( A_2 = \{2\} \). Then \( X \setminus (A_1 \cup A_2) = X \setminus X = \emptyset \), but \( (X \setminus A_1) \cup (X \setminus A_2) = \{2\} \cup \{1\} = \{1, 2\} \). Complementing turns \( \cup \) into \( \cap \) and \( \cap \) into \( \cup \), just as negation turns \( \exists \) into \( \forall \) and \( \vee \) into \( \wedge \); nothing stays the same.
:::

## Exercises

### A. Check your understanding

::: {#exr-set-operations-a1}
[A1]

These parts are about @thm-de-morgan-families and its proof.

::: {.enumerate options="label=(\alph*)"}
1. Which law of Chapter 4 is used in the \( (\subseteq) \) half of the second law, and which of its directions is classical?
2. Run the first law on \( X = \nZ \), \( I = \{2, 3\} \), and \( A_i \) the set of integer multiples of \( i \). Describe both sides in words, and name two integers in each side and two outside it.
3. What are the two sides of each law when \( I = \emptyset \)?
4. Let \( x \in X \). Translate \( x \notin \bigcap_{i \in I} A_i \) into a statement with \( \exists \). What is the correct translation if \( x \in X \) is **not** assumed?
:::
:::

::: {.solution}
(a) The bounded quantifier negation law of Chapter 4: \( \neg\forall i \in I\ \varphi \) gives \( \exists i \in I\ \neg\varphi \), with the bound kept. That direction is classical: it rests on the unbounded law \( \neg\forall x\, \varphi \vdash \exists x\, \neg\varphi \), which needs \( \rulename{RAA} \).

(b) The left side \( \nZ \setminus (A_2 \cup A_3) \) is the set of integers divisible by neither \( 2 \) nor \( 3 \). The right side \( (\nZ \setminus A_2) \cap (\nZ \setminus A_3) \) is the set of integers that are odd and not multiples of \( 3 \). By the theorem they are equal. For instance \( 1 \) and \( 5 \) (also \( -1 \), \( 7 \)) lie in both, and \( 3 \) and \( 4 \) (also \( 6 \)) lie in neither.

(c) For \( I = \emptyset \), the empty union is \( \emptyset \) and the empty intersection is \( X \). First law: \( X \setminus \emptyset = X \) and \( \bigcap_{i \in \emptyset} (X \setminus A_i) = X \). Second law: \( X \setminus X = \emptyset \) and \( \bigcup_{i \in \emptyset} (X \setminus A_i) = \emptyset \).

(d) By @def-family-union-intersection, \( x \in \bigcap_{i \in I} A_i \) means \( x \in X \wedge \forall i \in I\ (x \in A_i) \). For \( x \in X \), its negation is \( \neg\forall i \in I\ (x \in A_i) \), which by the law of (a) is \( \exists i \in I\ (x \notin A_i) \). Without \( x \in X \), the negation of the conjunction is, by @prp-de-morgan (d), "\( x \notin X \) or \( \exists i \in I\ (x \notin A_i) \)": an object may fail to be in the intersection simply because it is not in \( X \), since the intersection is taken inside \( X \).
:::

### B. Practice

::: {#exr-set-operations-b1}
[B1: Intersection and difference]

Prove that \( A \cap (B \setminus C) = (A \cap B) \setminus (A \cap C) \) for all sets \( A \), \( B \), \( C \), and name the propositional equivalence behind it.
:::

::: {.solution}
With \( p, q, r \) for \( x \in A \), \( x \in B \), \( x \in C \), the membership conditions are \( p \wedge (q \wedge \neg r) \) and \( (p \wedge q) \wedge \neg(p \wedge r) \), and the equivalence behind the law is \( p \wedge (q \wedge \neg r) \equiv (p \wedge q) \wedge \neg(p \wedge r) \). Both directions have short direct derivations, which the element-chase follows.

\( (\subseteq) \) Let \( x \in A \cap (B \setminus C) \). Then \( x \in A \), \( x \in B \), and \( x \notin C \). So \( x \in A \cap B \). If \( x \) were in \( A \cap C \), then \( x \in C \), a contradiction; so \( x \notin A \cap C \). Hence \( x \in (A \cap B) \setminus (A \cap C) \).

\( (\supseteq) \) Let \( x \in (A \cap B) \setminus (A \cap C) \). Then \( x \in A \), \( x \in B \), and \( x \notin A \cap C \). If \( x \) were in \( C \), then, since \( x \in A \), \( x \in A \cap C \), a contradiction; so \( x \notin C \). Hence \( x \in B \setminus C \), and \( x \in A \cap (B \setminus C) \).

By @prp-subset-antisymmetric the sets are equal. Both halves use \( \rulename{\neg I} \) and no classical rule.
:::

::: {#exr-set-operations-b2}
[B2: Three families of intervals]

For each family, indexed by \( t \in (0, \infty) \), compute the union and the intersection (inside \( X = \nR \)), and prove each answer by two inclusions.

::: {.enumerate options="label=(\alph*)"}
1. \( A_t = [t, 1 + t] \);
2. \( B_t = (-t, 1/t) \);
3. \( C_t = (t, 2t) \).
:::
:::

::: {.solution}
(a) *Union \( (0, \infty) \).* \( (\subseteq) \) If \( x \in [t, 1 + t] \) for some \( t > 0 \), then \( x \ge t > 0 \). \( (\supseteq) \) If \( x > 0 \), take \( t \coloneqq x \): then \( x \in [x, 1 + x] \). *Intersection \( \emptyset \).* Let \( x \) be any real number and take \( t \coloneqq \abs{x} + 1 > 0 \). Then \( x \le \abs{x} < t \), so \( x \notin [t, 1 + t] \). So no real number lies in every \( A_t \).

(b) *Union \( \nR \).* \( (\subseteq) \) Every \( B_t \) is a set of reals. \( (\supseteq) \) Let \( x \in \nR \). If \( x \le 0 \), take \( t \coloneqq 1 - x \ge 1 \): then \( -t = x - 1 < x \), and \( 1/t > 0 \ge x \), so \( x \in B_t \). If \( x > 0 \), take \( t \coloneqq 1/(2x) \): then \( -t < 0 < x \) and \( 1/t = 2x > x \), so \( x \in B_t \). *Intersection \( \{0\} \).* \( (\supseteq) \) For every \( t > 0 \), \( -t < 0 < 1/t \). \( (\subseteq) \) Let \( x \) lie in every \( B_t \). If \( x < 0 \), take \( t \coloneqq -x > 0 \): \( x \in B_t \) would need \( -t < x \), that is, \( x < x \). If \( x > 0 \), take \( t \coloneqq 1/x \): \( x \in B_t \) would need \( x < 1/t = x \). Both cases are impossible, so the remaining case of \( x < 0 \), \( x = 0 \), \( x > 0 \) holds: \( x = 0 \).

(c) *Union \( (0, \infty) \).* \( (\subseteq) \) If \( t < x < 2t \) for some \( t > 0 \), then \( x > 0 \). \( (\supseteq) \) If \( x > 0 \), take \( t \coloneqq 2x/3 \): then \( t = 2x/3 < x \) and \( 2t = 4x/3 > x \), so \( x \in C_t \). *Intersection \( \emptyset \).* Already two members are disjoint: \( C_1 = (1, 2) \) and \( C_2 = (2, 4) \) have no common element, since \( x < 2 \) and \( x > 2 \) cannot both hold. An element of every \( C_t \) would lie in both.

In each union the witness \( t \) depends on the point \( x \). In the intersections of (a) and (b) the index that excludes \( x \) depends on \( x \) too; in (c) two fixed disjoint members, \( C_1 \) and \( C_2 \), already exclude every \( x \). All of these are allowed by the definitions.
:::

::: {#exr-set-operations-b3}
[B3: Canceling a union]

Give sets \( A \), \( B \), \( C \) with \( A \cup B = A \cup C \) and \( B \ne C \). Then list the properties that any correct answer must have, so that a different answer can be checked against them.
:::

::: {.solution}
Take \( A = \{1\} \), \( B = \emptyset \), \( C = \{1\} \). Then \( A \cup B = \{1\} = A \cup C \), and \( B \ne C \), with the witness \( 1 \in C \), \( 1 \notin B \).

*Properties of any answer.* Call an element **odd one out** if it lies in exactly one of \( B \) and \( C \).

- \( B \ne C \) holds exactly when there is at least one odd one out (by @def-set-equality; getting such an element from \( B \ne C \) uses the classical direction of quantifier negation, Chapter 4).
- \( A \cup B = A \cup C \) holds exactly when **every** odd one out lies in \( A \). Indeed, if \( x \in B \setminus C \) and \( x \notin A \), then \( x \in A \cup B \) but \( x \notin A \cup C \); symmetrically for \( x \in C \setminus B \). Conversely, if every odd one out lies in \( A \), then an element of \( A \cup B \) either lies in \( A \), or lies in \( B \) and then, by excluded middle on \( x \in C \) (@prp-excluded-middle), in \( C \) or in \( A \); so it lies in \( A \cup C \), and symmetrically.

So an answer is correct exactly when some element lies in exactly one of \( B \), \( C \), and every such element lies in \( A \). The union with \( A \) "hides" the difference between \( B \) and \( C \); the lesson is that \( \cup \) cannot be canceled.
:::

### C. Going deeper

::: {#exr-set-operations-c1}
[C1: Power sets and operations]

Let \( A \) and \( B \) be sets.

::: {.enumerate options="label=(\alph*)"}
1. Decide whether \( \powerset{A \setminus B} = \powerset{A} \setminus \powerset{B} \) can hold. Then prove that every **non-empty** element of \( \powerset{A \setminus B} \) lies in \( \powerset{A} \setminus \powerset{B} \).
2. Show by an example that \( \powerset{A} \cup \powerset{B} = \powerset{A \cup B} \) can fail. Then prove that it holds if and only if \( A \subseteq B \) or \( B \subseteq A \).
:::
:::

::: {.solution}
[Hint 1]

In (a), test the empty set against both sides. In (b), one inclusion always holds; for the other, ask which subset of \( A \cup B \) could fail to be a subset of \( A \) and of \( B \).
:::

::: {.solution}
[Hint 2]

For (b) \( (\Rightarrow) \), argue by the contrapositive: if \( A \not\subseteq B \) and \( B \not\subseteq A \), choose \( a \in A \setminus B \) and \( b \in B \setminus A \).
:::

::: {.solution}
(a) **Never.** \( \emptyset \in \powerset{A \setminus B} \), since \( \emptyset \) is a subset of every set. But \( \emptyset \in \powerset{B} \) as well, so \( \emptyset \notin \powerset{A} \setminus \powerset{B} \). The empty set is a witness for every \( A \) and \( B \).

Now let \( S \in \powerset{A \setminus B} \) be non-empty, and choose \( s \in S \). Since \( S \subseteq A \setminus B \subseteq A \), we have \( S \in \powerset{A} \). Since \( s \in A \setminus B \), \( s \notin B \); so \( s \) is an element of \( S \) outside \( B \), and \( S \not\subseteq B \), that is, \( S \notin \powerset{B} \). Hence \( S \in \powerset{A} \setminus \powerset{B} \).

(b) *Failure.* For \( A = \{1\} \), \( B = \{2\} \): \( \{1, 2\} \in \powerset{A \cup B} \), but \( \{1, 2\} \) is a subset of neither \( A \) nor \( B \), so \( \{1, 2\} \notin \powerset{A} \cup \powerset{B} \).

*One inclusion always holds.* If \( S \in \powerset{A} \), then \( S \subseteq A \subseteq A \cup B \) (@prp-subset-transitive), so \( S \in \powerset{A \cup B} \); likewise for \( S \in \powerset{B} \). So \( \powerset{A} \cup \powerset{B} \subseteq \powerset{A \cup B} \).

\( (\Leftarrow) \) Suppose \( A \subseteq B \). Then \( A \cup B = B \) (if \( x \in A \cup B \), then \( x \in A \subseteq B \) or \( x \in B \); and \( B \subseteq A \cup B \)). Let \( S \in \powerset{A \cup B} \). Then \( S \subseteq B \), so \( S \in \powerset{B} \subseteq \powerset{A} \cup \powerset{B} \). With the inclusion above, equality holds. The case \( B \subseteq A \) is the same with \( A \) and \( B \) exchanged.

\( (\Rightarrow) \) We prove the contrapositive. Suppose that neither \( A \subseteq B \) nor \( B \subseteq A \). By the negation of \( \subseteq \) (@exr-sets-and-subsets-a1 (a) records it), there is \( a \in A \) with \( a \notin B \), and there is \( b \in B \) with \( b \notin A \); choose such \( a \) and \( b \). Let \( S \coloneqq \{a, b\} \). Then \( S \subseteq A \cup B \), so \( S \in \powerset{A \cup B} \). But \( S \not\subseteq A \), because \( b \in S \) and \( b \notin A \); and \( S \not\subseteq B \), because \( a \in S \) and \( a \notin B \). So \( S \notin \powerset{A} \cup \powerset{B} \), and the two sets differ. Two steps here are classical: turning "\( A \not\subseteq B \)" into a witness uses the classical directions of quantifier negation and of the law for negated implications (Chapter 4; see @exr-sets-and-subsets-a1 (a)), and concluding the implication from its contrapositive is @prp-contrapositive-converse.

**Marking scheme.** (10 points)
- 2: (a) the empty set as the witness that the equality never holds, with both memberships checked.
- 2: (a) a non-empty \( S \subseteq A \setminus B \) is shown to lie in \( \powerset{A} \) and, via an element outside \( B \), not in \( \powerset{B} \).
- 1: (b) a counterexample with the offending subset named.
- 2: (b) the inclusion \( \powerset{A} \cup \powerset{B} \subseteq \powerset{A \cup B} \) and the direction \( (\Leftarrow) \).
- 3: (b) \( (\Rightarrow) \): witnesses \( a \in A \setminus B \) and \( b \in B \setminus A \) named, and \( \{a, b\} \) shown to lie in \( \powerset{A \cup B} \) and in neither \( \powerset{A} \) nor \( \powerset{B} \).

A direct proof also earns the 3: assume equality and \( A \not\subseteq B \), fix \( a \in A \setminus B \) (1 point); for arbitrary \( b \in B \), \( \{a, b\} \in \powerset{A \cup B} = \powerset{A} \cup \powerset{B} \), and \( \{a, b\} \not\subseteq B \) because \( a \notin B \), so \( \{a, b\} \subseteq A \) and \( b \in A \), giving \( B \subseteq A \) (2 points). Both routes also end with a classical step: excluded middle on \( A \subseteq B \) in the direct route, the contrapositive in the book's.

Fatal errors (0 for the step): in (a), testing only non-empty subsets and concluding equality; in (b) \( (\Rightarrow) \), in the contrapositive route, using one witness \( a \) for both failures, or a set such as \( \{a\} \) that lies in \( \powerset{A} \).
:::

::: {#exr-set-operations-c2}
[C2: Find the error]

Here is a "proof" that \( (A \cup B) \cap (A \cup C) \subseteq A \cup (B \cap C) \) for all sets \( A \), \( B \), \( C \).

> (1) Let \( x \in (A \cup B) \cap (A \cup C) \). (2) Then \( x \in A \cup B \) and \( x \in A \cup C \). (3) We consider two cases, according to \( x \in A \cup B \). (4) *Case \( x \in A \).* Then \( x \in A \cup (B \cap C) \). (5) *Case \( x \in B \).* Since \( x \in A \cup C \), \( x \in C \). (6) So \( x \in B \cap C \), and hence \( x \in A \cup (B \cap C) \). (7) In both cases \( x \in A \cup (B \cap C) \), which proves the inclusion.

::: {.enumerate options="label=(\alph*)"}
1. Is the conclusion true?
2. Which line fails, which rule does it break, and which entry of the catalogue of Chapter 5 does it commit?
3. Give a counterexample to the illegal step itself: sets and an element for which the line's premise holds and its conclusion fails.
4. Repair the proof.
:::
:::

::: {.solution}
(a) Yes. It is the \( (\supseteq) \) half of the second distributive law of @thm-set-algebra (c).

(b) Line (5). From \( x \in A \cup C \), that is, \( x \in A \) or \( x \in C \), it concludes \( x \in C \), dropping the case \( x \in A \). A disjunction is used by \( \rulename{\vee E} \), which needs **both** cases; the line uses only one. This is a missing case, entry (N7) of the catalogue of Chapter 5.

(c) Take \( A = \{1\} \), \( B = \{1\} \), \( C = \emptyset \), and \( x = 1 \). Then \( x \in B \) (the case of line (5)) and \( x \in A \cup C \) (the premise of the line), but \( x \notin C \). The step is illegal although the conclusion of the whole proof is true: here \( x \in A \), so \( x \in A \cup (B \cap C) \) by the other case.

(d) Replace lines (5)–(6) by: *Case \( x \in B \).* Since \( x \in A \cup C \), there are two sub-cases. If \( x \in A \), then \( x \in A \cup (B \cap C) \). If \( x \in C \), then \( x \in B \cap C \), so \( x \in A \cup (B \cap C) \). In both sub-cases \( x \in A \cup (B \cap C) \). The rest of the proof stands.
:::

<!-- dependency ledger
def-set-operations (claim): an integer divisible by 2 and by 3 is divisible by 6; Z minus the evens is the odd integers | school fact (Part 0 convention); Chapter 7 proves the arithmetic of Z
def-set-operations (claim): no complement without an ambient set (the set of everything outside A joined with A would contain every set) | thm-russell, one-line argument inline
def-set-operations (example): interval computations [0,2] union [1,3] = [0,3] etc. | school order facts (Part 0 convention); proved in Chapter 11
thm-set-algebra (proof): letters of a derived sequent replaced by membership statements x in A (first-order atomic statements) | def-derived-rule; statements with variables are Chapter 4's (prose pointer)
thm-set-algebra (proof): "let x be arbitrary ... since x was arbitrary" is forall-I | ch04 (promised; prose pointer)
thm-set-algebra (claim): prp-de-morgan (a)-(c) derived without RAA, (d) with it | ch02 section 2.5 (checked on the page there)
thm-set-algebra (claim): truth table for (d) | computed inline (checked table)
def-power-set (claim): a set with n elements has 2^n subsets | ch08 (prose pointer; nothing depends on it)
def-power-set (claim): the empty set is a subset of every set | Section 6.1 (prose after prp-empty-set-unique: def-subset with prp-vacuous-implication)
exm-power-set-small (example): the empty set is a subset of the empty set | Section 6.1 (prose after prp-empty-set-unique: def-subset with prp-vacuous-implication)
exm-power-set-small (example): excluded middle on membership | prp-excluded-middle (cited)
def-indexed-family (claim): a family of subsets of X is a function I -> P(X), i -> A_i | Section 6.4 (prose pointer, same chapter; nothing depends on it)
def-indexed-family (claim): sequences of sets by recursion; countable unions | ch07, ch08 (prose pointers; nothing depends on them)
def-family-union-intersection (claim): vacuous truth of forall over an empty index set | ch04 (promised; prose pointer)
def-family-union-intersection (claim): Chapter 11 defines N as the intersection of all subsets of R containing 0 and closed under x -> x + 1 | ch11 (prose pointer; the set-level construction is done here)
prp-smallest-closed-set (proof): bigcap S is defined for non-empty S subset P(X); elements of bigcap S lie in every member | def-family-union-intersection (cited)
prp-smallest-closed-set (claim): (applications after it) the set of all strings of symbols is a set | taken as given, as in Chapter 3 section 3.1
prp-smallest-closed-set (claim): the smallest closed set equals the set of strings with a formation sequence | stated without proof, marked so (strong induction, thm-strong-induction); nothing depends on it
exm-families-real-parameter (example): order facts on R (0 < x/2 <= 1/2 < 1 and x/2 < x for 0 < x <= 1; trichotomy x < 0 or x = 0 or x > 0; |x| > 0 for x != 0 and x is |x| or -|x|; x < x is false) | school fact (Part 0 convention); proved in Chapter 11
exm-families-real-parameter (claim): nonexample: intersection over t > 0 of [0,t) is {0} (0 <= 0 < t; x < 0 is excluded by [0,1), x > 0 by [0,x)) | school order facts (Part 0 convention); proved in Chapter 11
exm-families-real-parameter (solution): (the quick check after it) [0,t] subset [0,2] for t <= 2; [0,1] subset [0,t] for t >= 1 | school order facts (Part 0 convention); proved in Chapter 11
exm-families-real-parameter (claim): Chapter 11's nested interval theorem needs closed intervals | ch11 (prose pointer)
thm-de-morgan-families (proof): bounded forall-I, forall-E, exists-I, exists-E over I | prp-bounded-quantifier-rules (cited)
thm-de-morgan-families (proof): unbounded forall-I/->-I for the element x | ch04 (promised; prose pointer)
thm-de-morgan-families (proof): bounded quantifier negation, not-forall to exists-not, classical via quantifier negation (a) | ch04 (promised; prose pointer; blueprint labels prp-bounded-quantifier-negation, prp-quantifier-negation)
exr-set-operations-a1 (solution): 1, 5, -1, 7 divisible by neither 2 nor 3; 3, 4, 6 by one of them | arithmetic
exr-set-operations-a1 (solution): bounded quantifier negation (not-forall over I to exists-not over I, bound kept), used in (a) and (d); its classical direction rests on not-forall x phi |- exists x not-phi, which needs RAA | ch04 (promised; prose pointer; blueprint labels prp-bounded-quantifier-negation, prp-quantifier-negation)
exr-set-operations-b2 (solution): order facts on R (|x| + 1 > x, 1/(2x) > 0, 4x/3 > x for x > 0) | school fact (Part 0 convention); proved in Chapter 11
exr-set-operations-b3 (solution): from B != C to an odd one out, by the classical direction of quantifier negation (not-forall to exists-not) and not(P<->Q) giving exactly one of P, Q; the forward half of the A-cup characterization by contrapositive; the converse splits on x in C | ch04 (promised; prose pointer); prp-contrapositive-converse; prp-excluded-middle (cited)
exr-set-operations-c1 (solution): classical quantifier negation and the law for negated implications to obtain witnesses a, b | ch04 (promised; prose pointer)
exr-set-operations-c1 (solution): the empty set is a subset of every set | Section 6.1 (prose after prp-empty-set-unique: def-subset with prp-vacuous-implication)
exr-set-operations-c2 (solution): catalogue entry (N7) | ch05 (promised; prose pointer "the catalogue of Chapter 5")
-->
