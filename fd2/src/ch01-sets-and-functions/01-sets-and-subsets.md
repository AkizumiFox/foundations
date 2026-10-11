# Sets, Subsets and Russell's Paradox

Chapters 1 to 5 built the grammar of mathematical statements: the connectives, the quantifiers, and the prose that carries their rules. The statements themselves have so far been about numbers, and occasionally about "collections" taken in their everyday sense. Analysis talks about collections all the time: the set of upper bounds of a set of numbers, the set of points where a function is positive, the set of all formulas. This section says what a set is allowed to be, what it means for one set to lie inside another, and how sets are described. One new notion carries the weight, the **subset**; the rest is the vocabulary it needs.

We begin with the simplest possible idea of a set, and we will see it fail.

## A naive idea, and what goes wrong with it

In everyday speech a collection is given by a property. "The students in this room", "the even numbers", "the prime numbers below 100": in each case we say what an object must satisfy, and the collection is everything that satisfies it. The naive rule is:

> *For every property, there is a set whose elements are exactly the objects having that property.*

It sounds harmless, and for the properties of everyday mathematics it gives the right answer. But a property may talk about sets themselves, and then the rule can be turned against itself. A set may be an element of another set: the set \( \{ \nN, \nZ \} \) has two elements, and each of them is a set. So it makes sense to ask of a set \( x \) whether \( x \in x \), and the property "\( x \notin x \)" is a property like any other. Most sets we know have it: the set of even numbers is not an even number, so it is not an element of itself.

Apply the naive rule to this property. It promises a set
\[
R = \text{the set of all } x \text{ with } x \notin x .
\]
Now ask whether \( R \in R \). By the way \( R \) was made, an object belongs to \( R \) exactly when it is not an element of itself; applied to the object \( R \), this says \( R \in R \) exactly when \( R \notin R \). A statement that is equivalent to its own negation leads to a contradiction by the rules of Chapter 2 alone; lines 4–11 of the derivation after Russell's theorem, at the end of this section, carry out exactly this argument, with an extra conjunct carried along. So the naive rule is contradictory: it cannot be part of mathematics.

This is **Russell's paradox**. We hold it until the end of the section, where it becomes a theorem, Russell's theorem, about the sets that do exist. First we set out what does work.

## Sets and membership

We do not define "set" or "element". They are the **primitive** notions of this chapter, in the way that "statement" was primitive in Chapter 1: we say how they are used, not what they are made of. A **set** is a collection of objects, its **elements**, and we write
\[
x \in A
\]
for "\( x \) is an element of \( A \)", or "\( x \) belongs to \( A \)", or "\( x \) lies in \( A \)". Its negation is written \( x \notin A \). The objects may be numbers, or sets, or (later in this chapter) pairs and functions.

In the language of Chapter 4, "\( \in \)" is a two-place predicate: \( x \in A \) is a statement about the two objects \( x \) and \( A \), true or false like \( x < y \). So everything Chapter 4 says about predicates, quantifiers, and their rules applies to it unchanged. A statement such as "every element of \( A \) is positive" is \( \forall x\, (x \in A \to x > 0) \), which the bounded notation of @def-bounded-quantifier shortens to \( \forall x \in A\ (x > 0) \).

Two conventions fix what kind of objects we deal with. First, the number sets \( \nN \), \( \nZ \), \( \nQ \), and \( \nR \) are **given**: we use them as familiar sets, with their school arithmetic and order, as the earlier chapters did. (Chapter 11 turns the facts we use about \( \nR \) into consequences of axioms.) Second, **numbers are not sets**: a number has no elements, and no number is equal to a set. So \( 1 \ne \{1\} \), and \( z \in 5 \) is false for every \( z \). The optional Chapters 9, 10 and 22 explain how numbers can be built out of sets; nothing in the main line depends on how that is done, and nothing here uses it.

The single most important fact about sets is that **a set is determined by its elements**. It has no other features: no order in which the elements come, no count of how often each is listed, no color. Two sets with the same elements are the same set.

::: {#def-set-equality}
[Equality of Sets]

Sets \( A \) and \( B \) are equal, \( A = B \), if and only if they have the same elements:
\[
\forall x\, (x \in A \leftrightarrow x \in B).
\]
:::

In words: every element of \( A \) is an element of \( B \), and every element of \( B \) is an element of \( A \). This principle is called **extensionality**: a set is fixed by its extension, the things it contains, and not by the words used to describe it. The sign \( = \) here is not new: it is the equality of @def-rules-equality, "names of the same object". The direction from \( A = B \) to the same elements is \( \rulename{{=}E} \), with \( \varphi \) the formula \( x \in z \) and \( z \) the variable replaced (and symmetry, @prp-equality-symmetric-transitive, for the way back from \( B \) to \( A \)). The converse direction is the principle just stated, that a set has no features beyond its elements; it is what lets an equation proved from "same elements" be used with \( \rulename{{=}E} \) like any other. The principle is an "if and only if", so it is used in both directions: to prove \( A = B \), prove the \( \forall \) statement; from \( A = B \), conclude \( x \in A \leftrightarrow x \in B \) for any \( x \) we like.

Sets with finitely many elements can be written by **listing** their elements between braces: \( \{1, 2, 3\} \) is the set whose elements are \( 1 \), \( 2 \), and \( 3 \), and nothing else. Extensionality has two immediate consequences for such lists.

- **Repetition does not matter.** \( \{1, 1, 2\} = \{1, 2\} \). An object \( x \) belongs to the left side exactly when \( x = 1 \) or \( x = 1 \) or \( x = 2 \), and to the right side exactly when \( x = 1 \) or \( x = 2 \); the two conditions are equivalent, since "\( x = 1 \) or \( x = 1 \)" says no more than "\( x = 1 \)".
- **Order does not matter.** \( \{1, 2\} = \{2, 1\} \). Here the two conditions are "\( x = 1 \) or \( x = 2 \)" and "\( x = 2 \) or \( x = 1 \)", which are equivalent because \( \vee \) commutes (@exm-disjunction-first-derivations).

Order and repetition are exactly what a list has and a set does not. When order matters we will need a different object, the ordered pair of Section 6.3.

A set with one element, \( \{a\} \), is a **singleton**. A singleton and its element are different things: \( \{1\} \) is a set, and \( 1 \) is a number, so \( 1 \ne \{1\} \) by our convention. For sets the difference is just as real. The set \( \{\nN\} \) has exactly one element, namely \( \nN \), while \( \nN \) has infinitely many; so they differ, by extensionality, as \( 2 \in \nN \) and \( 2 \notin \{\nN\} \).

::: {.check}
Are the sets \( \{1, 2, 2, 3\} \), \( \{3, 2, 1\} \), and \( \{1, \{2\}, 3\} \) equal?
:::

::: {.solution}
The first two are equal: each has exactly the elements \( 1 \), \( 2 \), \( 3 \), and repetition and order do not count. The third is different: its elements are \( 1 \), \( \{2\} \), and \( 3 \). The number \( 2 \) lies in the first set, but not in the third, since \( 2 \ne 1 \), \( 2 \ne 3 \), and \( 2 \ne \{2\} \) (a number is not a set). So by @def-set-equality the third set differs from the other two.
:::

## Subsets

Most statements about sets in analysis are not equalities but **inclusions**: every Cauchy sequence converges, every continuous function on \( [a, b] \) is bounded, every upper bound of a set is at least its supremum. Each has the shape "everything of this kind is also of that kind". Before a definition, look at one such statement in the language of sets. The multiples of \( 6 \) and the multiples of \( 3 \) form sets
\[
S = \{ \dots, -12, -6, 0, 6, 12, \dots \}, \qquad T = \{ \dots, -6, -3, 0, 3, 6, \dots \},
\]
and every element of \( S \) is an element of \( T \), because \( 6k = 3 \cdot (2k) \). The sets are not equal (\( 3 \in T \) but \( 3 \notin S \)), yet one sits inside the other. This relation between sets deserves a name.

*A set is a subset of another if everything in the first is also in the second.*

::: {#def-subset}
[Subset]

Let \( A \) and \( B \) be sets. \( A \) is a **subset** of \( B \), written \( A \subseteq B \), if **every** element of \( A \) is an element of \( B \):
\[
\forall x\, (x \in A \to x \in B).
\]
We also say that \( A \) is **contained in** \( B \), or that \( B \) **contains** \( A \). If \( A \subseteq B \) **and** \( A \ne B \), then \( A \) is a **proper subset** of \( B \), written \( A \subsetneq B \).
:::

In words, clause by clause. The quantifier \( \forall x \) ranges over every object whatsoever, not over the elements of \( A \) only; the implication \( x \in A \to x \in B \) restricts attention to the elements of \( A \), and says nothing about objects outside \( A \). With the bounded notation of @def-bounded-quantifier, the same condition is \( \forall x \in A\ (x \in B) \): "for every \( x \) in \( A \), \( x \) is in \( B \)". The symbol \( \subseteq \) allows equality, as \( \le \) does for numbers; the symbol \( \subsetneq \) excludes it, as \( < \) does. This book never writes \( \subset \), which some books use for \( \subseteq \) and others for \( \subsetneq \).

The definition is a \( \forall \) around an \( \to \), and its rules are the rules of those two symbols. To **prove** \( A \subseteq B \), we prove the \( \forall \) statement: by the rule \( \rulename{\forall I} \) of Chapter 4 we open a box for an arbitrary \( x \) (in prose, "let \( x \) be arbitrary"), and inside it we prove \( x \in A \to x \in B \) by \( \rulename{{\to}I} \) (@def-rules-implication): assume \( x \in A \) and reach \( x \in B \). The two openings are always written together, as "let \( x \in A \)". To **use** \( A \subseteq B \), we apply \( \rulename{\forall E} \) (Chapter 4) at the element we care about, and then \( \rulename{{\to}E} \): from \( A \subseteq B \) and \( a \in A \), conclude \( a \in B \). This gives the chapter's first named move.

*To show \( A \subseteq B \), take an arbitrary element of \( A \) and show that it lies in \( B \).*

We call this **element-chasing**: we follow one element from \( A \) to \( B \), unwinding the definition of \( A \) to find out what we know about it, and rewinding the definition of \( B \) to see what we must show. Here is the move three times: two ordinary inclusions, then the degenerate one. In each, the first sentence is the pair of openings, \( \rulename{\forall I} \) and \( \rulename{{\to}I} \), and the rest reaches \( x \in B \).

::: {#exm-subset-first-examples}
[Three inclusions]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( [1, 2] \subseteq [0, 3] \).
2. Let \( S \) be the set of integer multiples of \( 6 \) and \( T \) the set of integer multiples of \( 3 \), as above. Show that \( S \subseteq T \). Here \( d \mid n \), "\( d \) divides \( n \)", means that \( n = dk \) for some integer \( k \), so \( S \) consists of the integers \( x \) with \( 6 \mid x \), and \( T \) of those with \( 3 \mid x \).
3. Let \( A \) be any set. Show that \( A \subseteq A \).
:::
:::

::: {.solution}
(a) Let \( x \in [1, 2] \). Then \( 1 \le x \le 2 \), by the meaning of the interval. Hence \( 0 \le 1 \le x \) and \( x \le 2 \le 3 \), so \( 0 \le x \le 3 \), that is, \( x \in [0, 3] \). Since \( x \) was arbitrary, \( [1, 2] \subseteq [0, 3] \).

(b) Let \( x \in S \), that is, let \( x \) be an integer with \( 6 \mid x \). By the definition of \( \mid \), there is an integer \( k \) with \( x = 6k \); choose such a \( k \) (this is \( \rulename{\exists E} \) of Chapter 4, and the name \( k \) is new). Then \( x = 3 \cdot (2k) \), and \( 2k \) is an integer, so \( 3 \mid x \), with \( 2k \) as the witness (\( \rulename{\exists I} \)). Hence \( x \in T \). Since \( x \) was arbitrary, \( S \subseteq T \).

(c) Let \( x \in A \). Then \( x \in A \). Since \( x \) was arbitrary, \( A \subseteq A \). The box of \( \rulename{{\to}I} \) opens on \( x \in A \) and closes on the same line; in a derivation it is the one-line box that proves \( x \in A \to x \in A \).
:::

Part (c) is the degenerate case: every set is a subset of itself. It matters because it shows that \( \subseteq \) allows equality, and so "\( A \subseteq B \)" alone never tells us that \( B \) has anything \( A \) lacks. To say that \( A \) is a **proper** subset, \( A \subsetneq B \), we also need an element of \( B \) outside \( A \). In part (b) that element is \( 3 \): it lies in \( T \), not in \( S \).

A nonexample by minimal change. Replace \( 6 \) by \( 4 \) and \( 3 \) by \( 6 \) in (b): is the set of multiples of \( 4 \) a subset of the set of multiples of \( 6 \)? The first sentence of the proof still works (let \( x = 4k \)), but the last step fails: \( 4k \) need not be \( 6 \) times an integer. One element is enough to show the failure: \( 4 \) is a multiple of \( 4 \), and it is not a multiple of \( 6 \). What fails is the clause "**every** element of \( A \)" of @def-subset; here it fails at the element \( 4 \).

That last observation is worth recording in symbols, because it is how every inclusion is refuted. By the negation laws of Chapter 4 (\( \neg\forall x\, \varphi \) is equivalent to \( \exists x\, \neg\varphi \), and \( \neg(\varphi \to \psi) \) to \( \varphi \wedge \neg\psi \)),
\[
A \not\subseteq B \quad\text{means}\quad \exists x\, (x \in A \wedge x \notin B).
\]
*To refute an inclusion, exhibit one element of the first set that is not in the second.*

**Why this definition.** The definition says nothing about objects outside \( A \); that is the implication doing its job. If the \( \to \) were replaced by \( \wedge \), the condition \( \forall x\, (x \in A \wedge x \in B) \) would say that **every object** lies in \( A \) and in \( B \), which is false for every set we will meet (Russell's theorem at the end of this section shows that no set contains every set). This is the reason why a bounded "for every" always unfolds to an implication (@def-bounded-quantifier).

::: {.warning}
**Element or subset?** The symbols \( \in \) and \( \subseteq \) relate different things. \( x \in A \) says that \( x \) is one of the objects collected in \( A \); \( B \subseteq A \) says that every object collected in \( B \) is also collected in \( A \). For example \( 1 \in \{1\} \) and \( \{1\} \subseteq \{1\} \), but \( \{1\} \notin \{1\} \): the only element of \( \{1\} \) is the number \( 1 \), which is not the set \( \{1\} \). And "\( 1 \subseteq \{1\} \)" is not a comparison worth making: \( 1 \) is a number, not a set, so the definition of \( \subseteq \) does not apply to it. Before writing either symbol, ask whether the thing on the left is **one of the objects** in the set on the right, or a **collection** of such objects.
:::

Sometimes a set is both an element and a subset of the same set. In \( C = \{1, \{1\}\} \), the set \( \{1\} \) is an element (it is listed) and also a subset (its only element, \( 1 \), is listed too). Change one entry: in \( \{1, 2\} \), the set \( \{1\} \) is still a subset, but it is no longer an element, since the two elements are the numbers \( 1 \) and \( 2 \). Whether \( \{1\} \in D \) and whether \( \{1\} \subseteq D \) are two separate questions, and each is answered by looking at the elements of \( D \).

::: {.warning}
**Checking some elements proves nothing about all of them.** To prove \( A \subseteq B \), checking that a few elements of \( A \) lie in \( B \) is not enough, however many are checked. "The integers \( 0, 12, 24 \) and \( -12 \) are multiples of \( 4 \) and of \( 3 \)" does not prove that the set of multiples of \( 4 \) is a subset of the set of multiples of \( 3 \), and that inclusion is false (\( 4 \) is a witness). The error is entry (N1) of the catalogue of Chapter 5: verifying instances and concluding a \( \forall \). The rule \( \rulename{\forall I} \) needs an **arbitrary** element, one about which nothing is known except that it lies in \( A \).
:::

### Two inclusions make an equality

The first payoff of the definition connects it with equality. An equality of sets is an \( \leftrightarrow \) under a \( \forall \), and by @prp-iff-two-implications an \( \leftrightarrow \) is two implications. So an equality should be two inclusions.

::: {#prp-subset-antisymmetric}
[Equality Is Two Inclusions]

For all sets \( A \) and \( B \), \( A = B \) if and only if \( A \subseteq B \) and \( B \subseteq A \).
:::

::: {.idea}
Unwind all three definitions. \( A = B \) is \( \forall x\, (x \in A \leftrightarrow x \in B) \); the right side is \( \forall x\, (x \in A \to x \in B) \) and \( \forall x\, (x \in B \to x \in A) \). Inside the \( \forall \), the statements are \( P \leftrightarrow Q \) on one side and \( P \to Q \), \( Q \to P \) on the other, with \( P \) the statement \( x \in A \) and \( Q \) the statement \( x \in B \); @prp-iff-two-implications says exactly that these are interchangeable. So the proof is that proposition applied at an arbitrary \( x \), once in each direction.
:::

::: {.proof}
\( (\Rightarrow) \) Suppose \( A = B \). Let \( x \) be arbitrary. By @def-set-equality, \( x \in A \leftrightarrow x \in B \), so by the first half of @prp-iff-two-implications (with \( P \) the statement \( x \in A \) and \( Q \) the statement \( x \in B \), used as a derived rule, @def-derived-rule), \( x \in A \to x \in B \) and \( x \in B \to x \in A \). Since \( x \) was arbitrary, \( \forall x\, (x \in A \to x \in B) \) and \( \forall x\, (x \in B \to x \in A) \); by @def-subset, \( A \subseteq B \) and \( B \subseteq A \).

\( (\Leftarrow) \) Suppose \( A \subseteq B \) and \( B \subseteq A \). Let \( x \) be arbitrary. By @def-subset, \( x \in A \to x \in B \) and \( x \in B \to x \in A \), so by the second half of @prp-iff-two-implications, \( x \in A \leftrightarrow x \in B \). Since \( x \) was arbitrary, \( A = B \) by @def-set-equality.
:::

The name of the proposition in words is **antisymmetry** of \( \subseteq \): as for \( \le \) on numbers, \( A \subseteq B \) and \( B \subseteq A \) together force equality. It licenses the move that proves almost every set identity in this chapter.

*To show \( A = B \), show \( A \subseteq B \) and \( B \subseteq A \): two element-chases, one in each direction.*

A proof of this kind is written in two paragraphs, labeled \( (\subseteq) \) and \( (\supseteq) \), exactly as a proof of an "if and only if" is written in two paragraphs labeled \( (\Rightarrow) \) and \( (\Leftarrow) \) (Section 2.4). The two paragraphs are two separate boxes: neither may use the other's assumption.

### Transitivity, rule by rule

The second payoff is that inclusions chain, as \( \le \) does. Its proof is the first element-chase of the chapter written with every rule named, and we give it at two levels: first as a derivation, then as prose in which each sentence carries its rule in brackets. (These are levels 0 and 2 of Chapter 5; from here on the book writes level-3 prose; after one more fully tagged proof, in Section 6.2, brackets appear only on the step a proof is about.)

::: {#prp-subset-transitive}
[Inclusion Is Transitive]

For all sets \( A \), \( B \), and \( C \), if \( A \subseteq B \) and \( B \subseteq C \), then \( A \subseteq C \).
:::

::: {.idea}
The goal \( A \subseteq C \) is a \( \forall \) around an \( \to \), so the goal-directed moves open two boxes: a box for an arbitrary \( x_0 \), and inside it a box on \( x_0 \in A \). The new goal is \( x_0 \in C \). Each hypothesis is a \( \forall \) around an \( \to \) too, and we use each at \( x_0 \): the first carries \( x_0 \) from \( A \) into \( B \), the second from \( B \) into \( C \).
:::

::: {.proof}
Unwound by @def-subset, the hypotheses are \( \forall x\, (x \in A \to x \in B) \) and \( \forall x\, (x \in B \to x \in C) \), and the goal is \( \forall x\, (x \in A \to x \in C) \). The following is a derivation of the goal from the hypotheses. The outer box, flagged \( x_0 \), is the box of \( \rulename{\forall I} \) (Chapter 4); it has no assumption line.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x (x \in A \to x \in B)}
  \hypo {2} {\forall x (x \in B \to x \in C)}
  \open[x_0]
  \open
  \hypo {3} {x_0 \in A}
  \have {4} {x_0 \in A \to x_0 \in B} \Ae{1}
  \have {5} {x_0 \in B} \ie{4,3}
  \have {6} {x_0 \in B \to x_0 \in C} \Ae{2}
  \have {7} {x_0 \in C} \ie{6,5}
  \close
  \have {8} {x_0 \in A \to x_0 \in C} \ii{3-7}
  \close
  \have {9} {\forall x (x \in A \to x \in C)} \Ai{3-8}
\end{nd}$
\end{center}
```

The same proof in prose, with each step's rule in brackets:

> Suppose \( A \subseteq B \) and \( B \subseteq C \). Let \( x \) be arbitrary [\( \rulename{\forall I} \), opening], and suppose \( x \in A \) [\( \rulename{{\to}I} \), opening]. Since \( A \subseteq B \), in particular \( x \in A \to x \in B \) [\( \rulename{\forall E} \)], so \( x \in B \) [\( \rulename{{\to}E} \)]. Since \( B \subseteq C \), in particular \( x \in B \to x \in C \) [\( \rulename{\forall E} \)], so \( x \in C \) [\( \rulename{{\to}E} \)]. Hence \( x \in A \to x \in C \) [\( \rulename{{\to}I} \), closing], and since \( x \) was arbitrary, \( A \subseteq C \) [\( \rulename{\forall I} \), closing].

This proves the proposition.
:::

At level 3, the prose a mathematician writes, the same proof is one line: *let \( x \in A \); then \( x \in B \) since \( A \subseteq B \), and \( x \in C \) since \( B \subseteq C \).* The silent steps are those Chapter 5's convention allows: the two instances of \( \rulename{\forall E} \) at the obvious term \( x \), and the two closing sentences. What may never be silent is the opening "let \( x \in A \)", and the two citations, "since \( A \subseteq B \)" and "since \( B \subseteq C \)".

::: {.check}
Let \( A = \{1, 2\} \), \( B = \{1, 2, 3\} \), and \( C = \{1, 3\} \). Which of the six statements \( A \subseteq B \), \( B \subseteq A \), \( A \subseteq C \), \( C \subseteq A \), \( B \subseteq C \), \( C \subseteq B \) are true? For each false one, name a witness.
:::

::: {.solution}
True: \( A \subseteq B \) and \( C \subseteq B \) (every listed element of \( A \), and of \( C \), is listed in \( B \)). False: \( B \subseteq A \) (witness \( 3 \in B \), \( 3 \notin A \)); \( A \subseteq C \) (witness \( 2 \)); \( C \subseteq A \) (witness \( 3 \)); \( B \subseteq C \) (witness \( 2 \)). Both \( A \) and \( C \) are proper subsets of \( B \), and neither of \( A \), \( C \) is a subset of the other.
:::

## Describing sets: listing and specification

Listing works for a handful of elements. For a set such as "the real numbers whose square is less than \( 2 \)" we need to describe the elements by a property, as the naive rule wanted. The repair of the naive rule is small but essential: we may cut a set out **of a set we already have**.

::: {#def-set-builder}
[Specification]

Let \( A \) be a set and \( P(x) \) a property of objects \( x \). Then there is a set, written
\[
\{ x \in A : P(x) \},
\]
whose elements are exactly the elements of \( A \) that have the property \( P \): for every \( y \),
\[
y \in \{ x \in A : P(x) \} \iff y \in A \text{ and } P(y).
\]
:::

The notation is read "the set of \( x \) in \( A \) such that \( P(x) \)"; the colon is read "such that" (the book never writes a bar here, so that a bar stays free for divisibility and absolute value). The letter \( x \) is a bound variable, like the \( x \) of \( \forall x \): \( \{ x \in A : P(x) \} \) and \( \{ t \in A : P(t) \} \) are the same set. The set \( A \) is the **ambient set** of the description, and every set-builder in this book has one, named or fixed by the context; a set written \( \{ f(a) : a \in A \} \) is the image of \( A \) under \( f \) (Section 6.6), and any other set the book defines is shown to exist by (W1)–(W6) where it is introduced. By @def-set-equality, the equivalence in the definition determines the set completely, so "the" set is justified.

In the language of the rules: to show that \( y \) belongs to \( \{ x \in A : P(x) \} \), show \( y \in A \) and \( P(y) \); from \( y \in \{ x \in A : P(x) \} \), conclude both. Each is one \( \rulename{{\leftrightarrow}E} \) (@def-rules-biconditional) with the definition, followed or preceded by \( \rulename{\wedge I} \) or \( \rulename{\wedge E} \) (@def-rules-conjunction); at level 3 all of these are silent, and a proof simply writes "by definition" or nothing at all.

Specification is one of a short list of **working rules** that say which sets exist. We state them once, here, and use them from now on without comment.

::: {.enumerate options="label=(W\arabic*)"}
1. **Specification.** For a set \( A \) and a property \( P \), \( \{ x \in A : P(x) \} \) is a set (@def-set-builder).
2. **Listing.** Any finitely many objects \( a_1, \dots, a_n \) form a set \( \{ a_1, \dots, a_n \} \), whose elements are exactly \( a_1, \dots, a_n \).
3. **Unions.** For sets \( A \) and \( B \), there is a set whose elements are exactly the objects lying in \( A \) or in \( B \); more generally, for a family of sets indexed by a set, there is a set whose elements are exactly the objects lying in at least one member of the family (Section 6.2).
4. **Power sets.** For a set \( X \), the subsets of \( X \) form a set (Section 6.2).
5. **Products.** For sets \( A \) and \( B \), the ordered pairs \( (a, b) \) with \( a \in A \) and \( b \in B \) form a set; more generally, for a set \( X \) and \( n \in \nN \) with \( n \ge 2 \), the \( n \)-tuples \( (x_1, \dots, x_n) \) with every \( x_k \in X \) form a set (Section 6.3).
6. **Numbers.** \( \nN \), \( \nZ \), \( \nQ \), and \( \nR \) are sets.
:::

These rules are enough for everything the book does with sets until Chapter 8, which adds one more: a principle for making infinitely many choices at once (Section 6.5 shows where it is first needed). They are not axioms in the formal sense, and we do not try to derive them from fewer principles; the optional Chapter 9 states the axioms of set theory behind them and shows how (W1)–(W5) and the set \( \nN \) follow from them, and the optional Chapters 10 and 22 build \( \nZ \), \( \nQ \) and \( \nR \), which completes (W6). What matters here is what is **missing** from the list: there is no rule that collects all objects with a property, without an ambient set. The end of this section shows that such a rule would be contradictory.

## The empty set

Among all sets, one is special: the set with nothing in it. It turns up constantly: as the set of real solutions of \( x^2 = -1 \), as the intersection of two sets with nothing in common (Section 6.2), as the domain of a function with no inputs (Section 6.4). Without it, "the set of solutions" would not always name a set.

::: {#def-empty-set}
[Empty Set]

An **empty set** is a set with no elements: a set \( E \) such that \( \forall x\, (x \notin E) \).
:::

Such a set exists. Take any set we are given, say \( \nN \), and collect its elements \( x \) with \( x \ne x \); by specification (@def-set-builder), this is a set, and since \( x = x \) for every \( x \) (\( \rulename{{=}I} \), @def-rules-equality), nothing has the property, so the set has no elements. There is also at most one empty set, which justifies the article "**the**".

::: {#prp-empty-set-unique}
[The Empty Set Is Unique]

If \( E \) and \( E' \) are empty sets, then \( E = E' \).
:::

::: {.proof}
Let \( x \) be arbitrary. Since \( E \) and \( E' \) are empty, \( x \notin E \) and \( x \notin E' \). By @prp-vacuous-implication, \( x \notin E \) gives \( x \in E \to x \in E' \), and \( x \notin E' \) gives \( x \in E' \to x \in E \). So \( x \in E \leftrightarrow x \in E' \) by @prp-iff-two-implications. Since \( x \) was arbitrary, \( E = E' \) by @def-set-equality.
:::

We write \( \emptyset \) for **the** empty set. The same vacuous truth gives its most useful property at once: \( \emptyset \subseteq A \) **for every set** \( A \). Indeed, let \( x \) be arbitrary; \( x \notin \emptyset \), so \( x \in \emptyset \to x \in A \) by @prp-vacuous-implication; since \( x \) was arbitrary, \( \emptyset \subseteq A \). In words: to refute \( \emptyset \subseteq A \) we would need an element of \( \emptyset \) outside \( A \), and \( \emptyset \) has no elements at all.

The empty set is a set with no elements, and a set **containing** it is not empty. The set \( \{\emptyset\} \) has exactly one element, namely \( \emptyset \); so \( \{\emptyset\} \ne \emptyset \), with \( \emptyset \) itself as the witness: \( \emptyset \in \{\emptyset\} \) and \( \emptyset \notin \emptyset \). A box containing an empty box is not an empty box.

::: {.check}
::: {.enumerate options="label=(\alph*)"}
1. Is \( \emptyset \subseteq \emptyset \)?
2. Is \( \emptyset \in \emptyset \)?
3. Which of the sets \( \emptyset \), \( \{\emptyset\} \), \( \{\{\emptyset\}\} \) are equal?
:::
:::

::: {.solution}
(a) Yes: \( \emptyset \subseteq A \) for every set \( A \), and in particular for \( A = \emptyset \). (It also follows from \( A \subseteq A \).)

(b) No: \( \emptyset \) has no elements, so nothing, not even \( \emptyset \), belongs to it.

(c) None. \( \emptyset \) has no elements, and each of the other two has exactly one, so \( \emptyset \) differs from both. The only element of \( \{\emptyset\} \) is \( \emptyset \), and the only element of \( \{\{\emptyset\}\} \) is \( \{\emptyset\} \); these two elements are different by the first observation, so \( \emptyset \in \{\emptyset\} \) but \( \emptyset \notin \{\{\emptyset\}\} \), and the two sets differ by @def-set-equality.
:::

## Computing with set-builders

The next worked example shows how a set-builder is computed: we guess the answer, then prove the guess by two inclusions (@prp-subset-antisymmetric).

::: {#exm-set-builder-small}
[Computing sets given by a property]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \{ x \in \nZ : x^2 < 5 \} = \{-2, -1, 0, 1, 2\} \).
2. Show that \( \{ x \in \nR : x^2 < 0 \} = \emptyset \).
:::
:::

::: {.solution}
(a) Write \( S \) for the left side. Squaring the integers near \( 0 \) suggests the guess: \( 0^2 = 0 \), \( (\pm 1)^2 = 1 \), \( (\pm 2)^2 = 4 \) are below \( 5 \), and \( (\pm 3)^2 = 9 \) is not.

\( (\subseteq) \) Let \( x \in S \). Then \( x \in \nZ \) and \( x^2 < 5 \), by @def-set-builder. We claim \( \abs{x} \le 2 \). Otherwise \( \abs{x} \ge 3 \), since \( x \) is an integer, and then \( x^2 = \abs{x}^2 \ge 9 > 5 \), which contradicts \( x^2 < 5 \). So \( \abs{x} \le 2 \), and the integers with \( \abs{x} \le 2 \) are \( -2, -1, 0, 1, 2 \). Hence \( x \in \{-2, -1, 0, 1, 2\} \).

\( (\supseteq) \) Let \( x \in \{-2, -1, 0, 1, 2\} \). Then \( x \) is one of five integers, and we check each case: \( x^2 \) is \( 4, 1, 0, 1, 4 \) respectively, and each is less than \( 5 \). So \( x \in \nZ \) and \( x^2 < 5 \), that is, \( x \in S \).

By @prp-subset-antisymmetric, \( S = \{-2, -1, 0, 1, 2\} \).

(b) \( (\subseteq) \) Let \( x \in \{ x \in \nR : x^2 < 0 \} \). Then \( x \) is a real number with \( x^2 < 0 \); but \( x^2 \ge 0 \) for every real \( x \), a contradiction. So this case cannot occur, and \( x \in \emptyset \) holds in it vacuously (\( \rulename{\bot E} \), @def-rules-contradiction).

\( (\supseteq) \) \( \emptyset \subseteq \{ x \in \nR : x^2 < 0 \} \), because \( \emptyset \) is a subset of every set.

By @prp-subset-antisymmetric, the set is \( \emptyset \). A set-builder with an impossible property is a legitimate description of \( \emptyset \).
:::

Two remarks on the example. In (a), the \( (\supseteq) \) direction is a proof by cases over a finite list, which is legitimate: the five cases exhaust the set, because the list says exactly which elements it has. That is quite different from the error of the second warning above, where finitely many cases were checked for an infinite set. In (b), the \( (\supseteq) \) direction is free, and only \( (\subseteq) \) needs an argument. For "\( S = \emptyset \)" this is always so: the claim amounts to "\( S \) has no elements".

## Russell's paradox as a theorem

We return to the contradiction of the opening. The naive rule failed on \( R = \) "all \( x \) with \( x \notin x \)". Specification allows only the version with an ambient set: for any set \( A \),
\[
R_A \coloneqq \{ x \in A : x \notin x \}
\]
is a set, by (W1). What happens to the paradox now?

::: {#thm-russell}
[Russell's Theorem]

For every set \( A \), the set \( R_A = \{ x \in A : x \notin x \} \) is **not** an element of \( A \). Hence there is no set of which every set is an element.
:::

*Try it first (five minutes): suppose \( R_A \in A \). Is \( R_A \in R_A \)? Try each answer in turn, and see where each one leads.*

::: {.idea}
The attempt runs into the old paradox, but with one extra condition. If \( R_A \in R_A \), then by specification \( R_A \notin R_A \): the first answer refutes itself. If \( R_A \notin R_A \), then specification puts \( R_A \) into \( R_A \), **provided** \( R_A \in A \): the second answer refutes itself only under that proviso. So the two answers together are impossible exactly when \( R_A \in A \), and the conclusion is not a contradiction in mathematics but a fact: \( R_A \notin A \).

We do not need to split into the two answers. The first answer is refuted outright, with no proviso, by \( \rulename{\neg I} \) (@def-rules-negation); so \( R_A \notin R_A \) holds whenever \( R_A \in A \). That fact, fed back into specification, gives \( R_A \in R_A \), and the two collide.
:::

::: {.proof}
Let \( A \) be a set, and write \( R \) for \( R_A \). By @def-set-builder, for every \( y \),
\[
y \in R \iff y \in A \text{ and } y \notin y. \tag{$\ast$}
\]
Suppose \( R \in A \), for \( \rulename{\neg I} \). We first show \( R \notin R \). Suppose \( R \in R \). Then by \( (\ast) \) at \( y = R \), \( R \in A \) and \( R \notin R \); in particular \( R \notin R \), which contradicts \( R \in R \). Hence \( R \notin R \), by \( \rulename{\neg I} \). Now \( R \in A \) and \( R \notin R \), so \( R \in R \) by \( (\ast) \) read from right to left. This contradicts \( R \notin R \). Hence \( R \notin A \), by \( \rulename{\neg I} \).

For the second claim, suppose \( U \) were a set of which every set is an element. By the first claim with \( A = U \), the set \( R_U \) is not an element of \( U \); but \( R_U \) is a set, so it is an element of \( U \). This contradiction shows that no such \( U \) exists.
:::

Here is the first part of the proof as a derivation, with \( (\ast) \) as its premise, written as the universal statement it is, and \( R \) for \( R_A \):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall y (y \in R \leftrightarrow (y \in A \wedge y \notin y))}
  \open
  \hypo {2} {R \in A}
  \have {3} {R \in R \leftrightarrow (R \in A \wedge R \notin R)} \Ae{1}
  \open
  \hypo {4} {R \in R}
  \have {5} {R \in A \wedge R \notin R} \bie{3,4}
  \have {6} {R \notin R} \ae{5}
  \have {7} {\bot} \ne{4,6}
  \close
  \have {8} {R \notin R} \ni{4-7}
  \have {9} {R \in A \wedge R \notin R} \ai{2,8}
  \have {10} {R \in R} \bie{3,9}
  \have {11} {\bot} \ne{10,8}
  \close
  \have {12} {R \notin A} \ni{2-11}
\end{nd}$
\end{center}
```

Every rule in it is one of \( \rulename{\forall E} \), \( \rulename{{\leftrightarrow}E} \), \( \rulename{\wedge E} \), \( \rulename{\wedge I} \), \( \rulename{\neg E} \), and \( \rulename{\neg I} \). There is **no** \( \rulename{RAA} \), and no excluded middle: the inner box (lines 4–7) refutes one answer outright instead of splitting into two answers. This is worth noticing. The paradox is not an artifact of classical logic, and cannot be escaped by giving up a classical rule; it is a genuine contradiction in the naive rule, and the only repair is to change which sets exist.

**What the theorem says about sets.** Read with \( A \) arbitrary, the theorem says that **no set contains everything**: for every set \( A \) we have produced a set, \( R_A \), outside it. The naive rule "any property defines a set" is exactly specification **without** the phrase "\( x \in A \)", and the theorem shows that the phrase cannot be dropped: with \( A \) ranging over "everything", \( R_A \) would be the paradoxical \( R \). This is why every set-builder in this book has an ambient set, and why (W1)–(W6) contain no "set of all sets". When we want "all objects with a property", we first say where to look.

The argument has a shape that will return: a set built from \( A \) so that it disagrees with each candidate on the candidate itself. Chapter 8 proves by the same shape of argument that no function from a set \( X \) to the set of its subsets reaches every subset.

## Exercises

### A. Check your understanding

::: {#exr-sets-and-subsets-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Negate "\( A \subseteq B \)" in symbols, and then in words, with the negation pushed through the quantifier and the implication.
2. True or false: \( \{1\} \in \{\{1\}, 2\} \); \( \{1\} \subseteq \{\{1\}, 2\} \); \( \emptyset \subseteq \emptyset \); \( \{\emptyset\} \subseteq \{1\} \). Give a reason for each.
3. List the elements of \( \{ n \in \nZ : 0 < n^2 \le 9 \} \).
4. In an element-chasing proof of \( A \subseteq B \), the first sentence is "let \( x \in A \)". Which rule of logic gives its first clause, and which its second?
:::
:::

::: {.solution}
(a) By @def-subset, \( A \subseteq B \) is \( \forall x\, (x \in A \to x \in B) \). By the quantifier negation law of Chapter 4, its negation is equivalent to \( \exists x\, \neg(x \in A \to x \in B) \), and by the law for negated implications (also Chapter 4) to
\[
\exists x\, (x \in A \wedge x \notin B).
\]
In words: some element of \( A \) is not an element of \( B \).

(b) True: \( \{1\} \) is listed as an element of \( \{\{1\}, 2\} \). False: the only element of \( \{1\} \) is \( 1 \), and \( 1 \notin \{\{1\}, 2\} \), since \( 1 \ne \{1\} \) (a number is not a set) and \( 1 \ne 2 \); so \( 1 \) is a witness. True: \( \emptyset \) is a subset of every set. False: \( \emptyset \in \{\emptyset\} \) but \( \emptyset \notin \{1\} \), since \( \emptyset \ne 1 \); so \( \emptyset \) is a witness.

(c) \( \{-3, -2, -1, 1, 2, 3\} \). The integer \( 0 \) is excluded because \( 0^2 = 0 \) is not \( > 0 \), and integers with \( \abs{n} \ge 4 \) have \( n^2 \ge 16 > 9 \).

(d) "Let \( x \in A \)" opens two boxes. Its first clause, "let \( x \) be arbitrary", is \( \rulename{\forall I} \) (Chapter 4); its second, "suppose \( x \in A \)", is \( \rulename{{\to}I} \) (@def-rules-implication). The proof must then reach \( x \in B \) inside both boxes.
:::

### B. Practice

::: {#exr-sets-and-subsets-b1}
[B1: A set given by an equation]

Prove that \( \{ x \in \nR : x^2 - 3x + 2 = 0 \} = \{1, 2\} \), by two inclusions.
:::

::: {.solution}
Write \( S \) for the left side.

\( (\subseteq) \) Let \( x \in S \). Then \( x \) is real and \( x^2 - 3x + 2 = 0 \). Since \( x^2 - 3x + 2 = (x - 1)(x - 2) \), we have \( (x - 1)(x - 2) = 0 \). A product of two real numbers is zero only if one of the factors is zero, so \( x - 1 = 0 \) or \( x - 2 = 0 \), that is, \( x = 1 \) or \( x = 2 \). In either case \( x \in \{1, 2\} \).

\( (\supseteq) \) Let \( x \in \{1, 2\} \), so \( x = 1 \) or \( x = 2 \). If \( x = 1 \), then \( x^2 - 3x + 2 = 1 - 3 + 2 = 0 \). If \( x = 2 \), then \( x^2 - 3x + 2 = 4 - 6 + 2 = 0 \). In either case \( x \) is a real number satisfying the equation, so \( x \in S \).

By @prp-subset-antisymmetric, \( S = \{1, 2\} \).
:::

::: {#exr-sets-and-subsets-b2}
[B2: A subset of the empty set]

Let \( A \) be a set with \( A \subseteq \emptyset \). Prove that \( A = \emptyset \).
:::

::: {.solution}
We have \( A \subseteq \emptyset \) by hypothesis, and \( \emptyset \subseteq A \) because the empty set is a subset of every set. By @prp-subset-antisymmetric, \( A = \emptyset \).

Directly: if \( x \in A \), then \( x \in \emptyset \) because \( A \subseteq \emptyset \), which is impossible; so \( A \) has no elements, and it is **the** empty set by @prp-empty-set-unique.
:::

::: {#exr-sets-and-subsets-b3}
[B3: Equal or not?]

For each pair, determine whether the two sets are equal. Justify your answer: prove each equality, and give a witness element for each inequality.

::: {.enumerate options="label=(\alph*)"}
1. \( \{ x \in \nZ : 4 \mid x \} \) and \( \{ x \in \nZ : 2 \mid x \} \).
2. \( \{ x \in \nR : x^2 = 4 \} \) and \( \{-2, 2\} \).
3. \( \{\emptyset, \{\emptyset\}\} \) and \( \{\{\emptyset\}, \emptyset, \emptyset\} \).
4. \( \{ x \in \nZ : x^2 < 2 \} \) and \( \{ x \in \nN : x < 2 \} \).
:::
:::

::: {.solution}
(a) Not equal. The integer \( 2 \) lies in the second set (\( 2 = 2 \cdot 1 \)) but not in the first, since \( 2 = 4k \) would need \( k = \tfrac12 \), which is not an integer. (The first set is a proper subset of the second: \( x = 4k \) gives \( x = 2 \cdot (2k) \).)

(b) Equal. \( (\subseteq) \) If \( x \) is real with \( x^2 = 4 \), then \( (x - 2)(x + 2) = x^2 - 4 = 0 \), so \( x = 2 \) or \( x = -2 \). \( (\supseteq) \) \( 2^2 = 4 \) and \( (-2)^2 = 4 \).

(c) Equal. Both sets have exactly the elements \( \emptyset \) and \( \{\emptyset\} \): an object lies in the first exactly when it is \( \emptyset \) or \( \{\emptyset\} \), and in the second exactly when it is \( \{\emptyset\} \) or \( \emptyset \) or \( \emptyset \). Order and repetition do not count.

(d) Not equal. The first set is \( \{-1, 0, 1\} \): an integer with \( \abs{x} \ge 2 \) has \( x^2 \ge 4 \), and \( (-1)^2 = 1 \), \( 0^2 = 0 \), \( 1^2 = 1 \) are below \( 2 \). The second set is \( \{0, 1\} \), since \( \nN \) starts at \( 0 \). The witness \( -1 \) lies in the first set and not in the second (\( -1 \notin \nN \)).
:::

### C. Going deeper

::: {#exr-sets-and-subsets-c1}
[C1: Every set has something outside it]

Let \( A \) be a set, and let \( R_A = \{ x \in A : x \notin x \} \) as in @thm-russell.

::: {.enumerate options="label=(\alph*)"}
1. Let \( A^{+} \) be the set whose elements are the elements of \( A \) together with the object \( R_A \) (it exists by (W2) and (W3)). Show that \( A \subsetneq A^{+} \).
2. Deduce from @thm-russell that no set \( A \) has the property "every subset of \( A \) is an element of \( A \)".
:::
:::

::: {.solution}
[Hint 1]

In (a), a proper inclusion needs two things: the inclusion, and a witness in the larger set that is not in the smaller one. The theorem supplies the witness. In (b), look for a subset of \( A \) that the theorem says is not an element of \( A \).
:::

::: {.solution}
[Hint 2]

For (b): suppose, for \( \rulename{\neg I} \), that every subset of \( A \) is an element of \( A \). First show that \( R_A \subseteq A \).
:::

::: {.solution}
(a) First, \( A \subseteq A^{+} \): an element of \( A \) is an element of \( A^{+} \) by the description of \( A^{+} \). Second, \( A^{+} \ne A \): the object \( R_A \) lies in \( A^{+} \), and \( R_A \notin A \) by @thm-russell. So \( R_A \) is a witness, and \( A \subsetneq A^{+} \).

(b) Suppose, for \( \rulename{\neg I} \), that \( A \) is a set such that every subset of \( A \) is an element of \( A \). The set \( R_A \) is a subset of \( A \): if \( y \in R_A \), then \( y \in A \) (and \( y \notin y \)) by @def-set-builder. So by the assumption, \( R_A \in A \), which contradicts @thm-russell. Hence no set has the property.

Part (a) says that no set is "as large as possible": there is always a set with one more element. Part (b) rules out a set containing all of its own subsets; for instance, no set \( A \) has as its elements exactly the subsets of \( A \).

**Marking scheme.** (10 points)
- 2: (a) proves the inclusion \( A \subseteq A^{+} \) from the description of \( A^{+} \).
- 3: (a) names \( R_A \) as the witness to \( A^{+} \ne A \), citing @thm-russell for \( R_A \notin A \).
- 3: (b) proves \( R_A \subseteq A \) by element-chasing through @def-set-builder.
- 2: (b) combines the assumption with \( R_A \subseteq A \) to get \( R_A \in A \), and cites the theorem for the contradiction.

Fatal errors (0 for the step): using "the set of all sets" or any set-builder without an ambient set; taking \( A^{+} \ne A \) as obvious "because an element was added" (if \( R_A \) were already in \( A \), nothing would have been added).
:::

::: {#exr-sets-and-subsets-c2}
[C2: Antisymmetry for sets of sets]

Can there be sets \( A \) and \( B \), whose elements are themselves sets, such that \( A \subseteq B \), \( B \subseteq A \), and \( A \ne B \)? Explain why the answer does not depend on what the elements of \( A \) and \( B \) are.
:::

::: {.solution}
No. By @prp-subset-antisymmetric, \( A \subseteq B \) and \( B \subseteq A \) give \( A = B \), for **all** sets \( A \) and \( B \).

The answer does not depend on the elements, because nothing in the proof of @prp-subset-antisymmetric looks at them. The proof works with the statements \( x \in A \) and \( x \in B \) for an arbitrary object \( x \), and uses only @def-subset, @def-set-equality, and the propositional law @prp-iff-two-implications applied to those two statements. Whether \( x \) is a number, a set, or a set of sets never enters. For example, with \( A = \{\emptyset, \{\emptyset\}\} \) and \( B = \{\{\emptyset\}, \emptyset\} \), the two inclusions hold and indeed \( A = B \).

The point of the question is a habit: an element-chasing proof treats its element as a black box, and so it proves the statement for sets of anything at all.
:::

<!-- dependency ledger
def-set-equality (claim): {1, 1, 2} = {1, 2} uses "x = 1 or x = 1" iff "x = 1" | proved inline in words (vee-E / vee-I); disjunction rules def-rules-disjunction (Ch 1)
def-set-equality (claim): membership is a two-place predicate | ch04 (promised; prose pointer "Chapter 4")
def-set-equality (claim): numbers are not sets; no number equals a set | convention stated in this section (Part 0 working convention)
def-subset (claim): forall-I, forall-E and the flagged box | ch04 (promised; prose pointer "Chapter 4")
def-subset (claim): 6k = 3(2k); 3 is not a multiple of 6; 4 is not a multiple of 6; 4 is not a multiple of 3 | school fact (Part 0 convention); proved in Chapter 7 (integers)
exm-subset-first-examples (example): 0 <= 1, 2 <= 3 and transitivity of <= on R | school fact (Part 0 convention); proved in Chapter 11
exm-subset-first-examples (example): exists-E and exists-I on "6 | x" | ch04 (promised; prose pointer "Chapter 4")
exm-subset-first-examples (example): 2k is an integer when k is (Z closed under multiplication) | school fact (Part 0 convention); proved in Chapter 7 (integers)
def-subset (claim): negation of A subset B is "exists x (x in A and x notin B)" via quantifier negation and negated implication | ch04 (promised; prose pointer "Chapter 4")
def-subset (claim): the warning's catalogue entry (N1) | ch05 (promised; prose pointer "the catalogue of Chapter 5")
prp-subset-transitive (proof): forall-I with a flagged box, forall-E | ch04 (promised; prose pointer "Chapter 4"; the derivation is checked with Chapter 4's rules)
prp-subset-transitive (claim): levels 0, 2, 3 and the silent-step convention | ch05 (promised; prose pointer "Chapter 5")
prp-subset-transitive (claim): Section 6.2 tags one more proof rule by rule | Section 6.2 (prose pointer; nothing depends on it)
prp-subset-antisymmetric (proof): "let x be arbitrary ... since x was arbitrary" is forall-I | ch04 (promised; prose pointer)
exm-set-builder-small (example): an integer with |x| >= 3 has x^2 >= 9; the integers with |x| <= 2 are -2..2; x^2 >= 0 for real x | school fact (Part 0 convention); proved in Chapter 11 (order) and Chapter 7 (integers)
thm-russell (proof): forall-E on the specification premise | ch04 (promised; prose pointer); the derivation is checked with Chapter 4's rules
thm-russell (claim): Chapter 8's "no map X -> P(X) is onto" has the same shape | ch08 (prose pointer; nothing depends on it)
def-set-builder (claim): the working rules (W1)-(W5) and N follow from axioms; Z, Q, R are built from sets | optional ch09, ch10, ch22 (prose pointers; nothing depends on them)
def-set-builder (claim): Chapter 8 adds a principle of choice beyond (W1)-(W6); Section 6.5 shows where it is needed | ch08, Section 6.5 (prose pointers; nothing in this section depends on them)
def-set-builder (claim): a set written {f(a) : a in A} is an image | Section 6.6 (prose pointer; nothing in this section depends on it)
exr-sets-and-subsets-a1 (solution): quantifier negation and negated implication | ch04 (promised; prose pointer)
exr-sets-and-subsets-a1 (solution): integers with |n| >= 4 have n^2 >= 16 | school fact (Part 0 convention)
exr-sets-and-subsets-b1 (solution): x^2 - 3x + 2 = (x - 1)(x - 2); a product of reals is zero only if a factor is | school algebra (Part 0 convention); proved in Chapter 11
exr-sets-and-subsets-b3 (solution): 1/2 is not an integer; integers with |x| >= 2 have x^2 >= 4; -1 is not in N; x = 4k gives x = 2(2k) with 2k an integer | school facts (Part 0 convention); N = {0, 1, 2, ...} (NOTATION)
exr-sets-and-subsets-b3 (solution): x^2 - 4 = (x - 2)(x + 2); a product of reals is zero only if a factor is | school algebra (Part 0 convention); proved in Chapter 11
exr-sets-and-subsets-c1 (solution): A+ exists by (W2) and (W3) | working rules stated in this section
-->
