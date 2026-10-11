# Successors, Inductive Sets and the Natural Numbers

Chapter 3 described the natural numbers as what we reach from \( 0 \) by adding \( 1 \), again and again, and nothing else; induction (@ax-induction) was the precise form of "nothing else". In this chapter every object is a set, so we need a set to play \( 0 \) and an operation on sets to play "add \( 1 \)". This section chooses both, adds the one axiom that lets the repetition be completed into a set, and proves induction as a theorem about the set it produces.

## Going one step further

The empty set is the only set we can name without first having another one, so it will be \( 0 \). For "add one" we want an operation that, started from \( \emptyset \), keeps producing new sets, never returning to one already met. Putting a set inside itself as an element does that, as we shall see.

*The successor of a set adds the set itself as an element.*

::: {#def-set-successor}
[Successor of a set]

For **every** set \( x \), the **successor** of \( x \) is the set
\[
\mathrm{S}(x) \coloneqq x \cup \{x\} .
\]
:::

In words: the elements of \( \mathrm{S}(x) \) are the elements of \( x \), together with \( x \) itself. So, for every set \( y \),
\[
y \in \mathrm{S}(x) \iff y \in x \ \text{ or } \ y = x .
\]
The set \( \mathrm{S}(x) \) exists and is unique: \( \{x\} \) is the set \( \{x, x\} \) of Pairing (Z3), and \( x \cup \{x\} = \bigcup \{x, \{x\}\} \) comes from Union (Z4), both by @prp-zf-basic-sets (b), (c). Two facts are visible at once. First, \( x \in \mathrm{S}(x) \) for every \( x \). Second, \( x \subseteq \mathrm{S}(x) \): the successor keeps every old element and adds \( x \) itself, which is a new element whenever \( x \notin x \). The next section proves \( n \notin n \) for every natural number \( n \).

The letter is an upright \( \mathrm{S} \). Chapter 6 used an italic \( S \) for a set in @prp-smallest-closed-set, and we are about to use that proposition with this operation as its step; the two letters never stand for the same thing.

Start from \( \emptyset \) and apply \( \mathrm{S} \) repeatedly.

::: {#exm-von-neumann-numerals}
[The first natural numbers as sets]

Define
\[
\begin{aligned}
0 &\coloneqq \emptyset , & 1 &\coloneqq \mathrm{S}(0) , & 2 &\coloneqq \mathrm{S}(1) , \\
3 &\coloneqq \mathrm{S}(2) , & 4 &\coloneqq \mathrm{S}(3) .
\end{aligned}
\]
Write each of \( 1, 2, 3, 4 \) as a set of the earlier numerals, and then using only \( \emptyset \) and braces. Check that \( 0, 1, 2, 3 \) are four different sets.
:::

::: {.solution}
Each step adds the previous set as a new element:
\[
\begin{aligned}
1 &= \emptyset \cup \{0\} = \{0\} = \{\emptyset\} , \\
2 &= 1 \cup \{1\} = \{0, 1\} = \{\emptyset, \{\emptyset\}\} , \\
3 &= 2 \cup \{2\} = \{0, 1, 2\} = \bigl\{\emptyset, \{\emptyset\}, \{\emptyset, \{\emptyset\}\}\bigr\} , \\
4 &= 3 \cup \{3\} = \{0, 1, 2, 3\} = \bigl\{\emptyset, \{\emptyset\}, \{\emptyset, \{\emptyset\}\}, \{\emptyset, \{\emptyset\}, \{\emptyset, \{\emptyset\}\}\}\bigr\} .
\end{aligned}
\]
Written with \( \emptyset \) and braces only, \( 4 \) already needs eight pairs of braces and eight copies of \( \emptyset \), which is why the numerals are worth having.

The four sets differ, by Extensionality (Z1): two sets are equal only if they have the same elements, so it is enough to find an element of one that is not an element of the other. The set \( 0 \) has no elements, while \( 1 \), \( 2 \) and \( 3 \) all have the element \( 0 \); so \( 0 \) differs from each of them. Next, \( 1 \in 2 \) and \( 1 \in 3 \), but \( 1 \notin 1 \): the only element of \( 1 = \{0\} \) is \( 0 \), and \( 1 \ne 0 \). So \( 1 \) differs from \( 2 \) and from \( 3 \). Finally \( 2 \in 3 \), but \( 2 \notin 2 \): the elements of \( 2 \) are \( 0 \) and \( 1 \), and \( 2 \) differs from both, as just shown. So \( 2 \ne 3 \).
:::

Each number is the set of the numbers before it: \( 3 = \{0, 1, 2\} \), and \( 0 = \emptyset \) because nothing comes before \( 0 \). The picture draws a set as a box and its elements as the boxes directly inside it.

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.2]
  \draw (0.00,0.00) rectangle (0.42,0.42);
  \node[below] at (0.21,-0.05) {$0$};
  \draw (1.12,0.00) rectangle (1.82,0.70);
  \draw (1.26,0.14) rectangle (1.68,0.56);
  \node[below] at (1.47,-0.05) {$1$};
  \draw (2.52,0.00) rectangle (4.04,0.98);
  \draw (2.66,0.14) rectangle (3.08,0.56);
  \draw (3.20,0.14) rectangle (3.90,0.84);
  \draw (3.34,0.28) rectangle (3.76,0.70);
  \node[below] at (3.28,-0.05) {$2$};
  \draw (4.74,0.00) rectangle (7.90,1.26);
  \draw (4.88,0.14) rectangle (5.30,0.56);
  \draw (5.42,0.14) rectangle (6.12,0.84);
  \draw (5.56,0.28) rectangle (5.98,0.70);
  \draw (6.24,0.14) rectangle (7.76,1.12);
  \draw (6.38,0.28) rectangle (6.80,0.70);
  \draw (6.92,0.28) rectangle (7.62,0.98);
  \draw (7.06,0.42) rectangle (7.48,0.84);
  \node[below] at (6.32,-0.05) {$3$};
\end{tikzpicture}
\end{center}
```

The box for \( 3 \) holds three boxes, which are copies of the boxes for \( 0 \), \( 1 \) and \( 2 \). In general a natural number \( n \) will turn out to be the set of the natural numbers less than \( n \), so that \( n = \{0, 1, \dots, n - 1\} \) for \( n \ne 0 \). That is a theorem, proved later in this chapter once the order on the natural numbers is defined. For now the pattern is only something we have seen in the first five cases.

From here to the end of the chapter, the numerals \( 0, 1, 2, 3, \dots \) name these sets. They are not real numbers; where the chapter compares the two pictures, it says so.

Other choices of "add one" are possible. The rule \( x \mapsto \{x\} \) also starts a list of different sets, \( \emptyset, \{\emptyset\}, \{\{\emptyset\}\}, \dots \). With an axiom of infinity stated for that rule, it too would give a set satisfying Peano's axioms, but not by the proofs of the next section. What it loses is the pattern above: under it, the set playing \( 3 \) has one element, not three, and it does not contain the sets playing \( 0 \) and \( 1 \). The next section's proofs rest on that pattern, and one of its results fails outright: under \( x \mapsto \{x\} \) the set playing \( 2 \) is \( \{\{\emptyset\}\} \), which is the pair \( (\emptyset, \emptyset) \) of @def-kuratowski-pair, while the next section shows that no pair is a natural number in our sense. The choice \( x \cup \{x\} \) makes the order of the numbers into membership, which the chapter uses repeatedly.

::: {.warning}
The successor is defined for **every** set, not only for numerals, and its result need not look like a number. For \( x = \{1\} = \{\{\emptyset\}\} \), the successor is \( \mathrm{S}(x) = \{1, \{1\}\} \). It does not contain \( 0 \), while every numeral after \( 0 \) computed above does. A statement about \( \mathrm{S}(x) \) that holds for the numerals may fail for other sets; this is why the results below are stated for elements of one particular set.
:::

## Inductive sets and the axiom of infinity

We want a set whose elements are exactly \( 0, 1, 2, \dots \). The dots are the problem: Pairing and Union make each numeral, one at a time, and no axiom so far collects them all. The way out is to describe the property such a set must have, ask for a set with that property, and then cut it down to size.

*An inductive set contains \( 0 \) and never runs out of successors.*

::: {#def-zf-inductive-set}
[Inductive set]

A set \( I \) is **inductive** if \( \emptyset \in I \) and, **for every** \( x \in I \), also \( \mathrm{S}(x) \in I \).
:::

In words: the first clause gives the set a starting point, and the second says it is **closed** under the successor, so that applying \( \mathrm{S} \) never leads out of it. In symbols, with bounded quantifiers,
\[
\emptyset \in I \ \wedge \ \forall x \in I \ \ \mathrm{S}(x) \in I .
\]

The word "inductive" has another use in the analysis volume of this series, for subsets of the real numbers that contain the number \( 0 \) and are closed under \( x \mapsto x + 1 \). The shape is the same, but here the starting point is the set \( \emptyset \), the step is \( \mathrm{S} \), and there is no ambient set of real numbers.

An inductive set contains all the numerals: \( 0 = \emptyset \) by the first clause, then \( 1 = \mathrm{S}(0) \) by the second, then \( 2 = \mathrm{S}(1) \), and so on, one application of the second clause per numeral. So an inductive set cannot be finite in any naive sense, and nothing we have so far produces one.

Non-examples by minimal change come cheaply. The set \( 4 = \{0, 1, 2, 3\} \) contains \( \emptyset \) and the successors of \( 0 \), \( 1 \) and \( 2 \); only the last successor is missing, since \( \mathrm{S}(3) = 4 \notin 4 \): the set \( 4 \) has the element \( 3 \), and none of \( 0, 1, 2, 3 \) does (\( 0 \) has no elements, and the elements of \( 1 \), \( 2 \) and \( 3 \) are among \( 0, 1, 2 \), each different from \( 3 \) by @exm-von-neumann-numerals). And \( \{1, 2, 3, \dots\} \), if we had it, would be closed under \( \mathrm{S} \) but would miss the starting point. Both clauses do work.

::: {.check}
Is \( \{\emptyset\} \) inductive? Is \( \{0, 1, 2\} \)?
:::

::: {.solution}
Neither. \( \{\emptyset\} \) contains \( \emptyset \), but \( \mathrm{S}(\emptyset) = \{\emptyset\} = 1 \) is not an element of \( \{\emptyset\} \): its only element is \( \emptyset = 0 \), and \( 1 \ne 0 \) because \( 0 \in 1 \). So the closure clause fails at \( x = \emptyset \).

\( \{0, 1, 2\} \) contains \( 0 \) and the successors of \( 0 \) and \( 1 \), but \( \mathrm{S}(2) = 3 \) is not among \( 0, 1, 2 \): the set \( 3 \) has the element \( 2 \), and none of \( 0, 1, 2 \) does (\( 0 \) has no elements, the only element of \( 1 \) is \( 0 \), and the elements of \( 2 \) are \( 0 \) and \( 1 \), both different from \( 2 \) by @exm-von-neumann-numerals). So the closure clause fails at \( x = 2 \).
:::

Axioms (Z1)–(Z6) of @ax-zf-fragment produce each numeral separately, never all of them at once. That they cannot do better, that is, that no inductive set can be shown to exist from (Z1)–(Z6), is a theorem of set theory proper; we state it without proof, and nothing in this book depends on it. So the existence of an inductive set has to be assumed.

::: {#ax-infinity}
[Axiom of Infinity]

(Z7) There is an inductive set.
:::

Everything else the chapter builds, the natural numbers and their arithmetic included, comes from the inductive set of (Z7) by the six axioms of @ax-zf-fragment.

The axiom provides **some** inductive set and says nothing else about it. It may contain sets other than \( 0, 1, 2, \dots \). We cannot simply call it "the set of natural numbers"; we have to carve that set out of it.

## The least inductive set

An inductive set contains the numerals, and perhaps more. To remove anything extra, keep only what lies in **every** inductive set: whatever a set must contain merely by being inductive.

*The natural numbers are what every inductive set is forced to contain.*

There is one obstacle. Separation (Z6) can only cut a set out of a set already given, so we need an ambient set for the natural numbers; and the smallest-closed-set construction of Chapter 6 (@prp-smallest-closed-set) intersects a set of subsets, but the inductive sets are not handed to us as the elements of any set. So we fix one inductive set \( I \) and look only at the inductive subsets of \( I \), which do form a set, by Power set and Separation; the theorem below shows that the choice of \( I \) does not matter.

::: {#def-omega}
[The set of natural numbers]

Fix an inductive set \( I \), which exists by (Z7). Define
\[
\omega \coloneqq \{ x \in I : x \in J \text{ for every inductive set } J \subseteq I \} .
\]
The elements of \( \omega \) are the **natural numbers**.
:::

In words: a natural number is an element of the fixed inductive set \( I \) that survives every attempt to shrink \( I \) to a smaller inductive set.

The set \( \omega \) exists by Separation (Z6), with ambient set \( I \), once the condition is a property in the sense of (Z6): a formula of Chapter 4's first-order language with \( \in \) and \( = \) (@def-first-order-formula), with \( I \) as a parameter. The condition is "for every \( J \), if \( J \subseteq I \) and \( J \) is inductive, then \( x \in J \)", and, since \( J \subseteq I \) abbreviates \( \forall y \, (y \in J \to y \in I) \) as in (Z5) (@def-subset), the only part not yet written in that language is "\( J \) is inductive". Written out with no abbreviations it is
\[
\begin{aligned}
&\exists e \, \bigl( e \in J \wedge \forall y \, \neg (y \in e) \bigr) \\
&\wedge \forall u \, \Bigl( u \in J \to \exists z \, \bigl( z \in J \wedge
  \forall w \, ( w \in z \leftrightarrow ( w \in u \vee w = u ) ) \bigr) \Bigr) .
\end{aligned}
\]
The first line says that \( J \) has an element with no elements, which is \( \emptyset \in J \), because \( \emptyset \) is the only set with no elements (@prp-zf-basic-sets (a)). The second says that for each \( u \in J \) some element \( z \) of \( J \) has exactly the elements of \( u \cup \{u\} \), which is \( \mathrm{S}(u) \in J \) by (Z1).

Here is what "least" means, and why the choice of \( I \) is harmless.

::: {#thm-omega-least-inductive}
[The Least Inductive Set]

::: {.enumerate options="label=(\alph*)"}
1. \( \omega \) is inductive.
2. \( \omega \subseteq J \) for **every** inductive set \( J \), whether or not \( J \subseteq I \).
3. \( \omega \) is the only set with properties (a) and (b). In particular, \( \omega \) does not depend on the inductive set \( I \) fixed in @def-omega.
:::
:::

::: {.idea}
Part (a) is Chapter 6's smallest closed set, with \( I \) as the ambient set, \( \emptyset \) as the starting element and \( \mathrm{S} \) as the step: the closed subsets of \( I \) are exactly its inductive subsets, and \( \omega \) is their intersection. For (b), an inductive \( J \) need not lie inside \( I \), so we cut it down to \( \omega \cap J \), which does; then the definition of \( \omega \) applies. Part (c) is two inclusions, each an instance of (b).
:::

::: {.proof}
*(a)* Apply @prp-smallest-closed-set with \( X \coloneqq I \), the single starting element \( \emptyset \), which lies in \( I \) because \( I \) is inductive, and the single step \( x \mapsto \mathrm{S}(x) \), which turns elements of \( I \) into elements of \( I \) for the same reason. A subset \( J \subseteq I \) is closed in the sense of that proposition exactly when \( \emptyset \in J \) and \( \mathrm{S}(x) \in J \) for every \( x \in J \), that is, when \( J \) is inductive. So the set of closed subsets is
\[
\sS \coloneqq \{ J \in \powerset{I} : J \text{ is inductive} \} ,
\]
a set by Power set (Z5) and Separation (Z6); it is non-empty, since \( I \in \sS \). Its intersection \( \bigcap \sS \), formed inside \( I \) as in @prp-zf-basic-sets (c), is \( \{ x \in I : x \in J \text{ for every } J \in \sS \} \), which is \( \omega \). By @prp-smallest-closed-set, \( \bigcap \sS \) is closed; that is, \( \omega \) is inductive.

*(b)* Let \( J \) be an inductive set. The set \( \omega \cap J \) exists by (Z6) (@prp-zf-basic-sets (c)), and \( \omega \cap J \subseteq \omega \subseteq I \). It is inductive: \( \emptyset \in \omega \) by (a) and \( \emptyset \in J \) because \( J \) is inductive; and if \( x \in \omega \cap J \), then \( \mathrm{S}(x) \in \omega \) by (a) and \( \mathrm{S}(x) \in J \) because \( J \) is inductive. So \( \omega \cap J \) is an inductive subset of \( I \), and by @def-omega every element of \( \omega \) lies in it. Hence \( \omega \subseteq \omega \cap J \subseteq J \).

*(c)* Let \( W \) be a set that is inductive and is contained in every inductive set. Then \( W \subseteq \omega \), because \( \omega \) is inductive by (a); and \( \omega \subseteq W \) by (b), because \( W \) is inductive. So \( W = \omega \) by @prp-subset-antisymmetric. Now let \( I' \) be another inductive set, and let \( \omega' \) be the set that @def-omega produces from \( I' \). The proofs of (a) and (b) used nothing about \( I \) except that it is inductive, so they apply to \( \omega' \) as well: \( \omega' \) is inductive and is contained in every inductive set. By what we just proved, \( \omega' = \omega \). This proves the theorem.
:::

So \( \omega \) is **the** least inductive set: it is inductive, and it lies inside every inductive set. From now on we forget \( I \). The numerals \( 0, 1, 2, 3, 4 \) of @exm-von-neumann-numerals are natural numbers, since \( \omega \) is inductive and contains each of them by the argument given after @def-zf-inductive-set.

::: {.warning}
"An inductive set is the set of natural numbers" is **false** in general. @thm-omega-least-inductive gives \( \omega \subseteq J \) for an inductive \( J \), and nothing more. The set-theory volume of this series, using the axiom of Replacement (not part of this chapter), builds the inductive set \( \omega \cup \{ \omega, \mathrm{S}(\omega), \mathrm{S}(\mathrm{S}(\omega)), \dots \} \); it contains \( \omega \) itself as an element, and the next section shows that \( \omega \notin \omega \). Axiom (Z7) does not say that its \( I \) is not a set of this kind. What distinguishes \( \omega \) among inductive sets is "least", and every argument about natural numbers must go through \( \omega \), not through an arbitrary inductive set.
:::

## Induction on the natural numbers

Leastness has an immediate consequence. To show that every natural number belongs to some set \( A \), it is enough to show that \( A \) is inductive, since then \( \omega \subseteq A \).

::: {#thm-omega-induction}
[Induction on \( \omega \)]

::: {.enumerate options="label=(\alph*)"}
1. (Set form.) Let \( A \subseteq \omega \). If \( 0 \in A \), and \( \mathrm{S}(n) \in A \) for every \( n \in A \), then \( A = \omega \).
2. (Property form.) Let \( P(n) \) be a property, that is, a formula of the first-order language with \( \in \) and \( = \), possibly with other variables as parameters. If \( P(0) \) holds and, **for every** \( n \in \omega \), \( P(n) \) implies \( P(\mathrm{S}(n)) \), then \( P(n) \) holds **for every** \( n \in \omega \).
:::
:::

::: {.proof}
*(a)* The hypotheses say that \( A \) is inductive. By @thm-omega-least-inductive (b), \( \omega \subseteq A \). With \( A \subseteq \omega \), @prp-subset-antisymmetric gives \( A = \omega \).

*(b)* Let \( A \coloneqq \{ n \in \omega : P(n) \} \), a set by (Z6). Then \( 0 \in A \), because \( 0 \in \omega \) by @thm-omega-least-inductive (a) and \( P(0) \) holds. Let \( n \in A \). Then \( n \in \omega \) and \( P(n) \), so \( P(\mathrm{S}(n)) \) by hypothesis, and \( \mathrm{S}(n) \in \omega \) because \( \omega \) is inductive; hence \( \mathrm{S}(n) \in A \). By (a), \( A = \omega \), which says that \( P(n) \) holds for every \( n \in \omega \).
:::

Compare part (b) with the principle of induction, @ax-induction. Read with \( \omega \) in place of \( \nN \), and with \( \mathrm{S}(n) \) in place of \( n + 1 \), the two statements are the same; and once addition is defined, later in this chapter, \( n + 1 \) will be \( \mathrm{S}(n) \). The difference lies in their status. In Chapter 3, induction was an axiom, a basic property of \( \nN \) taken on trust. Here it is a **theorem**, proved from the seven axioms (Z1)–(Z7) about sets, and the proof is three lines long because all the work went into the definition of \( \omega \): the natural numbers were defined as what every inductive set contains, and induction says exactly that.

The proof of (b) is the model for the inductions in the rest of this chapter.

**Show the set is inductive.** To prove \( P(n) \) for every \( n \in \omega \), form \( \{ n \in \omega : P(n) \} \) and show that it has \( 0 \) as an element and is closed under \( \mathrm{S} \).

Here is the move once, on a statement about the shape of natural numbers: **every \( n \in \omega \) is \( 0 \), or is \( 1 \), or has \( 1 \) as an element**. Let \( A \coloneqq \{ n \in \omega : n = 0 \text{ or } n = 1 \text{ or } 1 \in n \} \), a set by (Z6). Then \( 0 \in A \) by the first alternative. Let \( n \in A \); there are three cases. If \( n = 0 \), then \( \mathrm{S}(n) = 1 \), which satisfies the second alternative. If \( n = 1 \), then \( \mathrm{S}(n) = 2 = \{0, 1\} \), which has \( 1 \) as an element. If \( 1 \in n \), then \( 1 \in n \subseteq \mathrm{S}(n) \). In every case \( \mathrm{S}(n) \in A \), since also \( \mathrm{S}(n) \in \omega \) because \( \omega \) is inductive (@thm-omega-least-inductive (a)). By @thm-omega-induction (a), \( A = \omega \).

Two features of this small proof recur. The property carried along is a disjunction, because "\( 1 \in n \)" alone is false at \( n = 0 \) and \( n = 1 \), and an induction can only carry a property that holds at the start. And the step is a case split along the disjunction, with one case for each alternative; dropping a case would be the error (N7) of @exm-not-allowed-catalogue.

::: {.check}
In the proof just given, which case of the step produces the first natural number that satisfies the third alternative "\( 1 \in n \)", and which number is it?
:::

::: {.solution}
The case \( n = 1 \). It produces \( \mathrm{S}(1) = 2 = \{0, 1\} \), which has \( 1 \) as an element. Neither \( 0 \) nor \( 1 \) has \( 1 \) as an element (\( 0 \) has no elements, and the only element of \( 1 \) is \( 0 \ne 1 \)), so \( 2 \) is the first. From then on the third case passes "\( 1 \in n \)" to \( \mathrm{S}(n) \), because \( n \subseteq \mathrm{S}(n) \).
:::

The next section uses the move five times in a row, to show that \( \omega \) satisfies Peano's axioms.

## Exercises

### A. Check your understanding

::: {#exr-the-set-omega-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. List the elements of \( 3 \) and of \( 4 \) as sets of numerals.
2. Is \( 2 \subseteq 3 \)? Is \( 2 \in 3 \)?
3. True or false, with a reason: every inductive set has \( 5 \coloneqq \mathrm{S}(4) \) as an element.
4. Write "\( J \) is not inductive" in symbols, with the negation moved inward until it stands only in front of a membership statement.
:::
:::

::: {.solution}
(a) \( 3 = \{0, 1, 2\} \) and \( 4 = \{0, 1, 2, 3\} \), by @exm-von-neumann-numerals.

(b) Both are true. The elements of \( 2 \) are \( 0 \) and \( 1 \), and both are elements of \( 3 = \{0, 1, 2\} \); so \( 2 \subseteq 3 \) (@def-subset). And \( 2 \) is itself one of the listed elements of \( 3 \), so \( 2 \in 3 \). A set can be both an element and a subset of another set; for numerals this will turn out to be the rule, not an accident.

(c) True. Let \( J \) be inductive. Then \( 0 = \emptyset \in J \) by the first clause of @def-zf-inductive-set, and the second clause applied five times gives \( 1, 2, 3, 4, 5 \in J \), each being the successor of the one before.

(d) "\( J \) is inductive" is \( \emptyset \in J \wedge \forall x \in J \ \ \mathrm{S}(x) \in J \). Its negation is
\[
\neg\bigl( \emptyset \in J \wedge \forall x \in J \ \ \mathrm{S}(x) \in J \bigr) ,
\]
which by De Morgan's law @prp-de-morgan (d) and (c) is equivalent to \( \neg(\emptyset \in J) \vee \neg\forall x \in J \ \ \mathrm{S}(x) \in J \), and by @prp-bounded-quantifier-negation (a), the bounded form of @prp-quantifier-negation, to
\[
\emptyset \notin J \ \vee \ \exists x \in J \ \ \mathrm{S}(x) \notin J .
\]
In words: \( J \) lacks the starting point, or some element of \( J \) has its successor outside \( J \).
:::

### B. Practice

::: {#exr-the-set-omega-b1}
[B1: Intersections and differences]

Let \( J \) and \( K \) be inductive sets. Prove that \( J \cap K \) is inductive. Is \( J \setminus \{\emptyset\} \) inductive? Justify your answer, and say which clause of the definition holds and which fails.
:::

::: {.solution}
The set \( J \cap K \) exists by (Z6) (@prp-zf-basic-sets (c)). It contains \( \emptyset \), since \( \emptyset \in J \) and \( \emptyset \in K \). If \( x \in J \cap K \), then \( \mathrm{S}(x) \in J \) because \( J \) is inductive and \( x \in J \), and \( \mathrm{S}(x) \in K \) likewise; so \( \mathrm{S}(x) \in J \cap K \). Hence \( J \cap K \) is inductive.

The set \( J \setminus \{\emptyset\} \) is **not** inductive: it does not contain \( \emptyset \), so the first clause fails. The second clause holds: if \( x \in J \setminus \{\emptyset\} \), then \( \mathrm{S}(x) \in J \), and \( \mathrm{S}(x) \ne \emptyset \) because \( x \in \mathrm{S}(x) \); so \( \mathrm{S}(x) \in J \setminus \{\emptyset\} \). This is a non-example by minimal change: removing one element breaks exactly one clause.
:::

::: {#exr-the-set-omega-b2}
[B2: Zero or a successor]

Prove that every \( n \in \omega \) is \( \emptyset \) or is \( \mathrm{S}(k) \) for some \( k \in \omega \), by showing that the set
\[
A \coloneqq \{ n \in \omega : n = \emptyset \text{ or } n = \mathrm{S}(k) \text{ for some } k \in \omega \}
\]
is inductive.
:::

::: {.solution}
The set \( A \) exists by (Z6), and \( A \subseteq \omega \). It contains \( 0 = \emptyset \) by the first alternative. Let \( n \in A \). Then \( n \in \omega \), so \( \mathrm{S}(n) \in \omega \) because \( \omega \) is inductive (@thm-omega-least-inductive (a)), and \( \mathrm{S}(n) \) satisfies the second alternative with \( k \coloneqq n \in \omega \). So \( \mathrm{S}(n) \in A \). By @thm-omega-induction (a), \( A = \omega \), which is the claim.

The step never used the hypothesis that \( n \) satisfies one of the alternatives, only that \( n \in \omega \). That is legitimate: the step's conclusion was reached outright, and induction still does the work of saying that every natural number is reached from \( 0 \) by successors.
:::

### C. Going deeper

::: {#exr-the-set-omega-c1}
[C1: Two steps back]

::: {.enumerate options="label=(\alph*)"}
1. Prove that every \( n \in \omega \) is \( 0 \), or is \( 1 \), or is \( \mathrm{S}(\mathrm{S}(k)) \) for some \( k \in \omega \).
2. Let \( I \) be an arbitrary inductive set. Running the argument of (a) on \( \{ x \in I : x = 0 \text{ or } x = 1 \text{ or } x = \mathrm{S}(\mathrm{S}(k)) \text{ for some } k \in I \} \), what does it prove about the elements of \( I \), and what does it **not** prove?
:::
:::

::: {.solution}
(a) Let
\[
A \coloneqq \{ n \in \omega : n = 0 \text{ or } n = 1 \text{ or } n = \mathrm{S}(\mathrm{S}(k)) \text{ for some } k \in \omega \} ,
\]
a set by (Z6). Then \( 0 \in A \) by the first alternative. Let \( n \in A \); we show \( \mathrm{S}(n) \in A \), in three cases along the disjunction. If \( n = 0 \), then \( \mathrm{S}(n) = 1 \), the second alternative. If \( n = 1 \), then \( \mathrm{S}(n) = \mathrm{S}(\mathrm{S}(0)) \), the third alternative with \( k \coloneqq 0 \in \omega \). If \( n = \mathrm{S}(\mathrm{S}(k)) \) with \( k \in \omega \), then \( \mathrm{S}(n) = \mathrm{S}(\mathrm{S}(\mathrm{S}(k))) \), the third alternative with \( \mathrm{S}(k) \) in place of \( k \), and \( \mathrm{S}(k) \in \omega \) because \( \omega \) is inductive. In each case \( \mathrm{S}(n) \in \omega \), so \( \mathrm{S}(n) \in A \). By @thm-omega-induction (a), \( A = \omega \).

(b) Call the set \( A_I \). The same three cases show that \( A_I \) has \( 0 \) as an element and is closed under \( \mathrm{S} \), so \( A_I \) is inductive; by @thm-omega-least-inductive (b), \( \omega \subseteq A_I \). That says only that every **natural number** is \( 0 \), \( 1 \) or \( \mathrm{S}(\mathrm{S}(k)) \) for some \( k \in I \), which is weaker than (a), whose \( k \) lies in \( \omega \). It does not say that every element of \( I \) is \( 0 \), \( 1 \) or \( \mathrm{S}(\mathrm{S}(k)) \) for some \( k \in I \). The set form of induction concludes \( A = \omega \) only because \( A \subseteq \omega \) was given; for \( A_I \subseteq I \) the most we get is \( \omega \subseteq A_I \subseteq I \), and the elements of \( I \) outside \( \omega \), if any, are not reached. Induction proves statements about \( \omega \), not about arbitrary inductive sets.
:::

<!-- dependency ledger
def-set-successor (claim): x in S(x) and x subset of S(x) | inline, from y in S(x) iff y in x or y = x (prp-zf-basic-sets (b), (c), cited)
def-set-successor (claim): (the paragraph after it) n not in n for every natural number n | lem-omega-transitive (c), next section (prose pointer; nothing in this section depends on it)
exm-von-neumann-numerals (solution): 0, 1, 2, 3 are distinct, by comparing elements | inline, Extensionality (Z1) of ax-zf-fragment (cited)
exm-von-neumann-numerals (claim): (the paragraph after it) n = {m in omega : m < n}, so n = {0, ..., n - 1} for n != 0 | thm-omega-order (c), later in this chapter (prose pointer; nothing in this section depends on it)
exm-von-neumann-numerals (claim): (the paragraph on other choices) x -> {x} (with infinity stated for it) would also give Peano's axioms, by other proofs | not proved here; prose only, nothing depends on it
exm-von-neumann-numerals (claim): (the paragraph on other choices) {{emptyset}} = (emptyset, emptyset), and no pair is a natural number | def-kuratowski-pair (cited); prp-pair-not-natural, next section (prose pointer; nothing in this section depends on it)
def-zf-inductive-set (claim): (the paragraph of non-examples) 4 not in 4 | inline, from 3 in 4 and 3 != 0, 1, 2 (exm-von-neumann-numerals, cited)
ax-infinity (claim): (the paragraph before it) no inductive set can be shown to exist from (Z1)-(Z6) | set theory proper (the set-theory volume, ST.1; stated without proof, nothing depends on it)
def-omega (claim): "J is inductive" is a first-order formula with in and = | inline (displayed), with prp-zf-basic-sets (a) (cited) and Extensionality (Z1)
thm-omega-least-inductive (proof): prp-smallest-closed-set, proved in Ch 6 under the working rules, uses only the power set, Separation and the intersection of a non-empty set of subsets of X | ax-zf-fragment (Z5), (Z6) and prp-zf-basic-sets (c) (cited at the step)
thm-omega-least-inductive (claim): (the warning after it) Replacement yields the inductive set omega u {omega, S(omega), ...}; omega not in omega | the set-theory volume (ST.1, prose pointer, nothing depends on it); omega not in omega is the Quick check of the next section (lem-omega-transitive (c))
thm-omega-induction (claim): (the remark after it) n + 1 = S(n) once addition is defined | def-omega-arithmetic (a), with 1 := S(0) from (c); the paragraph "The successor is plus one" after it, later in this chapter (prose pointer; nothing in this section depends on it)
thm-omega-induction (example): (the worked move) 2 = {0, 1}, 1 != 0 | exm-von-neumann-numerals (cited)
thm-omega-induction (example): (the worked move) S(n) in omega | thm-omega-least-inductive (a) (cited)
exr-the-set-omega-a1 (solution): five applications of the closure clause | inline
exr-the-set-omega-b1 (solution): S(x) != emptyset since x in S(x) | inline (def-set-successor)
-->
