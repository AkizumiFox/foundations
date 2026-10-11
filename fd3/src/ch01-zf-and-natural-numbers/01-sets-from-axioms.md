# Axioms for Sets

Chapters 6 to 8 worked with sets under six working rules, (W1)–(W6) of Section 6.1, and took the natural numbers as a given set inside the familiar real line, with induction as an axiom (@ax-induction). This volume builds the real numbers, so it may not lean on them: we start again from sets alone, and in this chapter **every object is a set**. This section asks which rules about sets are basic. It states six axioms, shows that they settle when two sets are equal, and produces the first sets from them: the empty set, unordered pairs, unions, intersections and differences.

## Starting again from sets

Section 6.1 listed its working rules and used them without asking where they came from. One of them, specification (@def-set-builder), was the repair of a rule that fails: "every property defines a set" is contradictory, because the property \( x \notin x \) would define a set that both is and is not an element of itself, and @thm-russell turns that contradiction into the fact that **no set has every set as an element**. So rules about sets cannot be chosen by what sounds harmless. They must be chosen with care and stated once, and everything else must then be derived from them.

That raises two questions, which this chapter answers in order. Which of the working rules are basic, and which follow from the others? And can the basic rules **produce** the objects Chapters 6 to 8 took as given (ordered pairs, functions, the natural numbers), rather than only describe them? Section 9.2 builds ordered pairs out of sets; Section 9.3 builds the natural numbers.

To build numbers out of sets we must let sets be the only objects. From here to the end of the chapter, **every object is a set**, and every element of a set is again a set. Section 6.1 used a different picture, in which numbers are given objects that are not sets, and it said that nothing in the main line would depend on how numbers are made. That picture stays valid for Chapters 6 to 8; this chapter works in the other one, where \( 0 \) will be the empty set and \( 0 \in 1 \) will be a true statement. The chapter's introduction says how the two pictures fit together.

**The language.** Statements about sets are written in the first-order language of Chapter 4 (@def-first-order-formula) with **one** predicate symbol, the two-place \( \in \), together with equality. There are no constant symbols and no function symbols. The variables range over sets. So "\( x \in y \)" and "\( x = y \)" are the atomic formulas, and everything else is built from them with the connectives and the quantifiers. A **property** \( P(x) \) of sets is a formula of this language in which the variable \( x \) may occur free; other free variables, called **parameters**, are allowed too, and stand for sets fixed in advance.

## The axioms

We want sets that can be built, and we know one way not to build them: by an arbitrary property, with nothing to cut the set out of. So instead of one rule for every property, we list a few specific ways of making a new set from sets we already have, together with one set to start from.

*A few ways to make sets, and one way to tell them apart.*

::: {#ax-zf-fragment}
[The Axioms (Z1)–(Z6)]

::: {.enumerate options="label=(Z\arabic*)"}
1. **Extensionality.** Sets with the same elements are equal: for all sets \( A \) and \( B \), if \( x \in A \leftrightarrow x \in B \) for every \( x \), then \( A = B \).
2. **Empty set.** **There is** a set with no elements.
3. **Pairing.** For all sets \( a \) and \( b \) **there is** a set whose elements are exactly \( a \) and \( b \).
4. **Union.** For every set \( \sS \) **there is** a set whose elements are exactly the elements of members of \( \sS \).
5. **Power set.** For every set \( X \) **there is** a set whose elements are exactly the subsets of \( X \).
6. **Separation.** For every set \( A \) and every property \( P(x) \) **there is** a set whose elements are exactly the \( x \in A \) with \( P(x) \).
:::
:::

In symbols, with \( S \subseteq X \) as an abbreviation of \( \forall y\, (y \in S \to y \in X) \) (@def-subset):
\[
\begin{aligned}
&(\mathrm{Z1}) && \forall A\, \forall B\, \bigl(\forall x\, (x \in A \leftrightarrow x \in B) \to A = B\bigr), \\
&(\mathrm{Z2}) && \exists E\, \forall x\, \neg(x \in E), \\
&(\mathrm{Z3}) && \forall a\, \forall b\, \exists C\, \forall x\, \bigl(x \in C \leftrightarrow (x = a \vee x = b)\bigr), \\
&(\mathrm{Z4}) && \forall \sS\, \exists U\, \forall x\, \bigl(x \in U \leftrightarrow \exists S\, (S \in \sS \wedge x \in S)\bigr), \\
&(\mathrm{Z5}) && \forall X\, \exists Q\, \forall S\, (S \in Q \leftrightarrow S \subseteq X).
\end{aligned}
\]
(Z6) is not one axiom but one for each property, an **axiom schema**. For every formula \( \varphi \) whose free variables are among \( x, p_1, \dots, p_k \) and in which the letter \( B \) does not appear,
\[
\forall p_1 \cdots \forall p_k\, \forall A\, \exists B\, \forall x\, \bigl(x \in B \leftrightarrow (x \in A \wedge \varphi)\bigr). \tag{Z6}
\]
The letter \( B \) here is bound, and may be renamed (Section 4.2) to any letter that appears nowhere else in (Z6) (not in \( \varphi \), and neither \( x \) nor \( A \)). So a property may mention a given set called \( B \), as \( A \setminus B \) below does, once the new set is given another letter, say \( D \): \( \forall B\, \forall A\, \exists D\, \forall x\, \bigl(x \in D \leftrightarrow (x \in A \wedge x \notin B)\bigr) \).

In words, clause by clause, with what each one licenses.

- *(Z1)* is the only axiom that proves two sets **equal** by comparing their elements: it turns "same elements" into \( A = B \). Section 6.1 stated it as the meaning of equality of sets (@def-set-equality); here it is an axiom, and only its direction "same elements, hence equal" needs to be assumed. The other direction, from \( A = B \) to \( x \in A \leftrightarrow x \in B \), is the equality rule \( \rulename{{=}E} \) of @def-rules-equality, a rule of logic.
- *(Z2)* gives the one set we start from. Each of (Z3)–(Z6) makes a set out of sets already given.
- *(Z3)* makes a set out of two given sets \( a \), \( b \). The two need not differ: with \( b = a \) its set has the single element \( a \).
- *(Z4)* flattens one level: from a set \( \sS \) of sets it makes the set of what lies **inside** the members of \( \sS \). With (Z3) it gives the union of two sets (below).
- *(Z5)* collects **all** subsets of \( X \) into one set; it is the working rule (W4).
- *(Z6)* cuts a set out of a set \( A \) already given, by a property. It is specification (@def-set-builder), now an axiom. The letter \( B \) must not appear in \( \varphi \), or the property could refer to the set being made: with \( \varphi \) the formula \( x \notin B \), and \( B \) the very set that (Z6) produces, it would say \( x \in B \leftrightarrow (x \in A \wedge x \notin B) \), which no set \( B \) satisfies when \( A \) has an element.

**Properties written with defined symbols.** The formulas of (Z6) contain only \( \in \) and \( = \). We shall write properties with defined symbols as well (\( \subseteq \), \( \emptyset \), \( \{a, b\} \), and later \( \cup \), pairs and functions), and that is harmless: each defined symbol is shorthand that unwinds into \( \in \) and \( = \). For instance "\( x = \emptyset \)" unwinds to \( \forall y\, \neg(y \in x) \), and "\( x = \{a, b\} \)" to \( \forall y\, \bigl(y \in x \leftrightarrow (y = a \vee y = b)\bigr) \). A property is admissible in (Z6) when its unwinding is a formula of the language, which is the case for every property in this chapter.

**One way to tell sets apart, and one way to make them unique.** Each of (Z2)–(Z6) says that **there is** a set with a certain membership condition. By (Z1) there is then **exactly one**: two sets with the same membership condition have the same elements, so they are equal. We use this move so often that we state it once:

*To show that a set is unique, show that any two sets with its membership condition have the same elements, and apply (Z1).*

**The first sets.** Here are the axioms at work, each set checked against the membership condition that made it.

- *The empty set.* (Z2) gives a set with no elements; @prp-zf-basic-sets below shows it is unique, and we write it \( \emptyset \).
- *A singleton.* (Z3) with \( a = b = \emptyset \) gives a set whose elements are exactly the \( x \) with \( x = \emptyset \vee x = \emptyset \), that is, \( x = \emptyset \). This is \( \{\emptyset\} \). It is not \( \emptyset \): it has the element \( \emptyset \), and \( \emptyset \) has none.
- *A two-element set.* (Z3) with \( a = \emptyset \) and \( b = \{\emptyset\} \) gives \( \{\emptyset, \{\emptyset\}\} \), whose elements are exactly \( \emptyset \) and \( \{\emptyset\} \). These two are different, by the previous item, so this set has two elements.
- *A union.* (Z4) with \( \sS = \{\emptyset, \{\emptyset\}\} \) gives the set of everything that lies in \( \emptyset \) or in \( \{\emptyset\} \). Nothing lies in \( \emptyset \), and only \( \emptyset \) lies in \( \{\emptyset\} \). So the union is \( \{\emptyset\} \): one element, although \( \sS \) has two.
- *A power set.* (Z5) with \( X = \{\emptyset\} \) gives the set of subsets of \( \{\emptyset\} \). There are two, \( \emptyset \) and \( \{\emptyset\} \) itself (the argument of @exm-power-set-small, which uses only extensionality and excluded middle, applies word for word). So \( \powerset{\{\emptyset\}} = \{\emptyset, \{\emptyset\}\} \), the set of the third item.
- *A separation.* (Z6) with \( A = \{\emptyset, \{\emptyset\}\} \) and the property \( x \ne \emptyset \) gives \( \{\{\emptyset\}\} \): of the two elements of \( A \), only \( \{\emptyset\} \) differs from \( \emptyset \).

The degenerate case is the empty set itself, and it matters: each natural number will be built from \( \emptyset \) by these axioms, one at a time. The set of all of them needs one more starting point, the Axiom of Infinity (Section 9.3).

**A non-example by minimal change.** Delete the ambient set from (Z6): "for every property \( P(x) \) there is a set whose elements are exactly the \( x \) with \( P(x) \)". This is the naive rule of Section 6.1, and it fails at once. With \( P(x) \) the property \( x \notin x \) it gives a set \( R \) with \( R \in R \leftrightarrow R \notin R \), a contradiction; and even with the harmless-looking property \( x = x \) it gives a set of which every set is an element, which @thm-russell rules out. What fails is exactly the clause "\( x \in A \)" that was deleted. Every other part of (Z6) survives the change; the ambient set is what makes it safe.

**Why this list.** Each axiom earns its place by something later in the chapter. Pairing and Union give finite sets and the union of two sets; Power set and Separation give the product \( A \times B \) (Section 9.2) and, with it, relations and functions; Extensionality makes every construction unique. Four further axioms complete the usual system of set theory with choice, and only one of them is needed here:

- **Infinity** says that some set contains \( \emptyset \) and is closed under one particular step. It is (Z7), stated in Section 9.3, once there is a step to iterate. Without it, the axioms above produce each finite set we write down, one at a time. That they cannot produce a set holding infinitely many of them is a theorem of set theory, which this book states and does not prove.
- **Replacement** and **Foundation** are not needed to build the natural numbers, and are left to the volume on set theory, which revisits this chapter.
- **Choice** is @ax-choice of Chapter 8. Nothing in this chapter uses it.

We do not ask whether the axioms are consistent, or (apart from exercise C1) whether one of them follows from the others. Those are questions about the axioms, and this chapter only uses them.

::: {.warning}
**Two traps in the list.** First, (Z3) gives an **unordered** pair: \( \{a, b\} = \{b, a\} \), since \( x = a \vee x = b \) and \( x = b \vee x = a \) say the same thing. So \( \{a, b\} \) cannot record which of \( a \), \( b \) came first, and Section 9.2 needs a different construction for the ordered pair. Second, (Z6) needs the ambient set \( A \): the rule without it is exactly the one @thm-russell refutes.
:::

## The first consequences

The existence axioms say "there is a set"; the first proposition says "there is exactly one", and so lets us give each such set a name. It also rebuilds from the axioms the operations of @def-set-operations and, for a set of sets \( \sS \), the \( \bigcup \sS \) and \( \bigcap \sS \) of @def-family-union-intersection; indexed families wait for Section 9.2.

::: {#prp-zf-basic-sets}
[The Sets Named by the Axioms]

::: {.enumerate options="label=(\alph*)"}
1. There is **exactly one** set with no elements. It is written \( \emptyset \).
2. For all sets \( a \) and \( b \) the set of (Z3) is unique. It is written \( \{a, b\} \), and \( \{a\} \coloneqq \{a, a\} \), the set whose only element is \( a \).
3. For every set \( \sS \) the set of (Z4) is unique. It is written \( \bigcup \sS \), and \( A \cup B \coloneqq \bigcup \{A, B\} \) for sets \( A \), \( B \), so that \( x \in A \cup B \) if and only if \( x \in A \) or \( x \in B \). The sets \( A \cap B \coloneqq \{ x \in A : x \in B \} \) and \( A \setminus B \coloneqq \{ x \in A : x \notin B \} \) exist by (Z6). For a **non-empty** set \( \sS \), the set
\[
\bigcap \sS \coloneqq \{ x \in A_0 : x \in S \text{ for every } S \in \sS \}
\]
exists by (Z6) for any \( A_0 \in \sS \), it **does not depend** on \( A_0 \), and \( x \in \bigcap \sS \) if and only if \( x \in S \) for every \( S \in \sS \).
4. For all sets \( a, b, c, d \),
\[
\{a, b\} = \{c, d\} \iff (a = c \wedge b = d) \vee (a = d \wedge b = c).
\]
In particular \( \{a\} = \{c, d\} \) if and only if \( a = c \) and \( c = d \).
:::
:::

::: {.idea}
Parts (a)–(c) are the uniqueness move three times: the axiom named gives a set, and any two sets with the same membership condition are equal by (Z1). For \( \bigcap \sS \), the condition "\( x \in A_0 \)" adds nothing, since \( A_0 \) is itself one of the \( S \in \sS \); so the condition does not mention \( A_0 \) at all. Part (d) is different: it compares elements. From \( a \in \{a, b\} = \{c, d\} \) we get \( a = c \) or \( a = d \), and each case is finished by locating \( b \) and then the remaining element of \( \{c, d\} \).
:::

::: {.proof}
(a) A set with no elements exists by (Z2). If \( E \) and \( E' \) both have no elements, then for every \( x \), both \( x \in E \) and \( x \in E' \) are false, so \( x \in E \leftrightarrow x \in E' \); hence \( E = E' \) by (Z1). This is the argument of @prp-empty-set-unique, with (Z1) in place of @def-set-equality.

(b) Let \( C \) and \( C' \) be sets as in (Z3) for the same \( a \), \( b \). For every \( x \), \( x \in C \) and \( x \in C' \) are each equivalent to \( x = a \vee x = b \), so \( C = C' \) by (Z1). With \( b = a \) the condition is \( x = a \vee x = a \), which is equivalent to \( x = a \); so the only element of \( \{a\} \) is \( a \).

(c) The set of (Z4) is unique by the same argument, its condition being \( \exists S\, (S \in \sS \wedge x \in S) \). For \( \sS = \{A, B\} \), an \( S \in \{A, B\} \) is \( A \) or \( B \), by (b); so \( x \in A \cup B \) if and only if \( x \in A \) or \( x \in B \). The sets \( A \cap B \) and \( A \setminus B \) are instances of (Z6), with ambient set \( A \) and parameter \( B \) (after renaming the bound letter of (Z6)), and are unique by (Z1).

Now let \( \sS \) be non-empty, and let \( A_0 \in \sS \). By (Z6) with ambient set \( A_0 \) and parameter \( \sS \), the set \( \bigcap \sS \) above exists. Its membership condition simplifies:
\[
x \in A_0 \wedge \forall S\, (S \in \sS \to x \in S) \iff \forall S\, (S \in \sS \to x \in S).
\]
From left to right, drop the first conjunct. From right to left, apply the condition at \( S = A_0 \), which is a member of \( \sS \), to get \( x \in A_0 \). The right-hand side does not mention \( A_0 \). So if \( A_1 \) is another member of \( \sS \), the sets built from \( A_0 \) and from \( A_1 \) have the same elements, and they are equal by (Z1).

(d) \( (\Leftarrow) \) If \( a = c \) and \( b = d \), then \( \{a, b\} = \{c, d\} \) by \( \rulename{{=}E} \). If \( a = d \) and \( b = c \), then \( \{a, b\} = \{d, c\} \), and \( \{d, c\} = \{c, d\} \) because \( x = d \vee x = c \) is equivalent to \( x = c \vee x = d \), so the two sets have the same elements (Z1).

\( (\Rightarrow) \) Suppose \( \{a, b\} = \{c, d\} \). Since \( a \in \{a, b\} \), we have \( a \in \{c, d\} \), so \( a = c \) or \( a = d \). We take the two cases in turn (\( \rulename{\vee E} \)).

*Case 1: \( a = c \).* Since \( b \in \{c, d\} \), \( b = c \) or \( b = d \). If \( b = d \), then \( a = c \) and \( b = d \), the first disjunct. If \( b = c \), then \( b = c = a \), so \( \{a, b\} = \{a\} \). Now \( d \in \{c, d\} = \{a, b\} = \{a\} \), so \( d = a \), and hence \( b = a = d \). Again \( a = c \) and \( b = d \).

*Case 2: \( a = d \).* Since \( b \in \{c, d\} \), \( b = c \) or \( b = d \). If \( b = c \), then \( a = d \) and \( b = c \), the second disjunct. If \( b = d \), then \( b = d = a \), so \( \{a, b\} = \{a\} \). Now \( c \in \{a\} \), so \( c = a \), and \( b = a = c \). So \( a = d \) and \( b = c \), the second disjunct again.

In each case one of the two disjuncts holds.

For the last claim, apply what was just proved with \( b = a \): \( \{a\} = \{a, a\} = \{c, d\} \) if and only if \( (a = c \wedge a = d) \vee (a = d \wedge a = c) \). Both disjuncts say that \( a = c \) and \( a = d \), that is, \( a = c \) and \( c = d \).
:::

Two consequences of (d) are used constantly. With \( c = d \) it says that \( \{a\} = \{c\} \) only if \( a = c \): a singleton determines its element. And with \( c = a \) it says that \( \{a, b\} = \{a, d\} \) only if \( b = d \): in the first disjunct \( b = d \) directly, and in the second \( a = d \) and \( b = a \), so again \( b = d \). Section 9.2 uses both.

**The sets of Chapter 6, rebuilt.** The union \( A \cup B \) of part (c) has the membership condition of @def-set-operations (a), and the intersection and difference are defined exactly as in parts (b) and (c) of that definition; so by (Z1) these are the sets Chapter 6 used. Likewise, if \( \sS \) is a non-empty set of subsets of a set \( X \), the \( \bigcap \sS \) of part (c) and the \( \bigcap \sS \) of @def-family-union-intersection, cut out of \( X \), have the same membership condition, "\( x \) lies in every member of \( \sS \)", and so they are the same set. The new version needs no ambient \( X \): any member \( A_0 \) of \( \sS \) does the job. For the empty \( \sS \) it would have to contain every set, and no set does (@thm-russell); exercise B2 returns to this.

::: {.check}
Compute \( \bigcup \emptyset \), \( \bigcup \{\emptyset\} \) and \( \bigcup \{\{\emptyset\}, \{\emptyset, \{\emptyset\}\}\} \).
:::

::: {.solution}
\( \bigcup \emptyset = \emptyset \): an element would have to lie in some member of \( \emptyset \), and \( \emptyset \) has no members. \( \bigcup \{\emptyset\} = \emptyset \): the only member is \( \emptyset \), which has no elements. \( \bigcup \{\{\emptyset\}, \{\emptyset, \{\emptyset\}\}\} = \{\emptyset, \{\emptyset\}\} \): the first member contributes \( \emptyset \), the second contributes \( \emptyset \) and \( \{\emptyset\} \), and repeats do not count.
:::

With @prp-zf-basic-sets every set we have named so far is a set of the axioms, and so are the operations of Section 6.2 on sets and on sets of sets: \( \cup \), \( \cap \), \( \setminus \), the power set (Z5), \( \bigcup \sS \), and \( \bigcap \sS \) for non-empty \( \sS \). Unions and intersections of an indexed family \( (A_i)_{i \in I} \) need the family as a function, which needs ordered pairs; Section 9.2 returns to them. What is not yet built is an **ordered** pair; the warning above says why \( \{a, b\} \) will not do, and Section 9.2 builds one.

## Exercises

### A. Check your understanding

::: {#exr-sets-from-axioms-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. For each of the sets \( \{\emptyset\} \), \( \{\emptyset, \{\emptyset\}\} \), \( \powerset{\emptyset} \), \( \bigcup \{\emptyset\} \), and \( \{ x \in A : x \notin x \} \) for a given set \( A \), name the axioms that produce it.
2. True or false: for all sets \( a \) and \( b \), \( \{a\} = \{b\} \) implies \( a = b \). Justify your answer.
3. Prove that \( \bigcup \{a\} = a \) for every set \( a \).
4. Is there a set \( T \) such that \( \{x\} \in T \) for **every** set \( x \)? Justify your answer.
:::
:::

::: {.solution}
(a) \( \{\emptyset\} \): (Z2) for \( \emptyset \), then (Z3) with both inputs \( \emptyset \). \( \{\emptyset, \{\emptyset\}\} \): (Z2), then (Z3) twice, once for \( \{\emptyset\} \) and once with the inputs \( \emptyset \) and \( \{\emptyset\} \). \( \powerset{\emptyset} \): (Z2), then (Z5); it is \( \{\emptyset\} \), since the only subset of \( \emptyset \) is \( \emptyset \). \( \bigcup \{\emptyset\} \): (Z2), (Z3), then (Z4); it is \( \emptyset \). \( \{ x \in A : x \notin x \} \): (Z6) with ambient set \( A \) and the property \( \neg(x \in x) \). Uniqueness, in every case, is (Z1).

(b) True. Apply @prp-zf-basic-sets (d) with \( c = d = b \): \( \{a\} = \{b, b\} \) gives \( a = b \) (and \( b = b \)).

(c) For every \( x \): \( x \in \bigcup \{a\} \) if and only if \( x \in S \) for some \( S \in \{a\} \). The only \( S \in \{a\} \) is \( a \) (@prp-zf-basic-sets (b)), so this holds if and only if \( x \in a \). The two sets have the same elements, so \( \bigcup \{a\} = a \) by (Z1).

(d) No. Suppose \( T \) were such a set. By (Z4), \( \bigcup T \) is a set. Let \( x \) be any set. Then \( x \in \{x\} \) and \( \{x\} \in T \), so \( x \in \bigcup T \). So every set is an element of \( \bigcup T \), which contradicts the second claim of @thm-russell. Hence no such \( T \) exists.
:::

### B. Practice

::: {#exr-sets-from-axioms-b1}
[B1: Power sets and unions]

::: {.enumerate options="label=(\alph*)"}
1. Compute \( \powerset{\powerset{\emptyset}} \).
2. Prove that \( \bigcup \powerset{X} = X \) for every set \( X \).
:::
:::

::: {.solution}
(a) \( \powerset{\emptyset} = \{\emptyset\} \), since the only subset of \( \emptyset \) is \( \emptyset \). So \( \powerset{\powerset{\emptyset}} = \powerset{\{\emptyset\}} = \{\emptyset, \{\emptyset\}\} \), as computed in the list of first sets after @ax-zf-fragment.

(b) We show both inclusions and apply @prp-subset-antisymmetric (whose proof is (Z1) and logic).

\( (\subseteq) \) Let \( x \in \bigcup \powerset{X} \). Then \( x \in S \) for some \( S \in \powerset{X} \), that is, for some \( S \subseteq X \). Hence \( x \in X \).

\( (\supseteq) \) Let \( x \in X \). The set \( \{x\} \) is a subset of \( X \), since its only element is \( x \) (@prp-zf-basic-sets (b)). So \( \{x\} \in \powerset{X} \), and \( x \in \{x\} \); hence \( x \in \bigcup \powerset{X} \).
:::

::: {#exr-sets-from-axioms-b2}
[B2: Intersections of sets of sets]

::: {.enumerate options="label=(\alph*)"}
1. Let \( \sS = \{ X, Y \} \) with \( X = \{\emptyset, \{\emptyset\}\} \) and \( Y = \{\{\emptyset\}, \{\{\emptyset\}\}\} \). Compute \( \bigcap \sS \) twice: once with \( A_0 = X \) in @prp-zf-basic-sets (c), once with \( A_0 = Y \).
2. Explain in one or two sentences why the two computations had to agree.
3. Explain why the definition of \( \bigcap \sS \) makes no sense for \( \sS = \emptyset \).
:::
:::

::: {.solution}
(a) With \( A_0 = X \): of the two elements of \( X \), \( \emptyset \) is not in \( Y \) (the elements of \( Y \) are \( \{\emptyset\} \) and \( \{\{\emptyset\}\} \), both non-empty), and \( \{\emptyset\} \) is in \( Y \) and in \( X \). So \( \bigcap \sS = \{\{\emptyset\}\} \). With \( A_0 = Y \): \( \{\emptyset\} \) lies in \( X \) and in \( Y \); \( \{\{\emptyset\}\} \) does not lie in \( X \), since it differs from \( \emptyset \) (it has an element) and from \( \{\emptyset\} \) (its element \( \{\emptyset\} \) is not \( \emptyset \)). So again \( \bigcap \sS = \{\{\emptyset\}\} \).

(b) An element of either set must lie in **every** member of \( \sS \), and that condition already forces it into \( A_0 \), because \( A_0 \) is a member. So the condition "\( x \in A_0 \)" adds nothing, and both computations describe the same elements.

(c) There is no \( A_0 \in \emptyset \) to cut the set out of. Without an ambient set, the condition "\( x \in S \) for every \( S \in \emptyset \)" holds for every set \( x \), vacuously; so \( \bigcap \emptyset \) would be a set of which every set is an element, and there is no such set (@thm-russell).
:::

### C. Going deeper

::: {#exr-sets-from-axioms-c1}
[C1: What the empty-set axiom really says; intersections as greatest lower bounds]

::: {.enumerate options="label=(\alph*)"}
1. Show that (Z2) follows from (Z6), once **some** set \( A \) is known to exist.
2. Let \( \sS \) be a non-empty set. Show that \( \bigcap \sS \subseteq S \) for every \( S \in \sS \), and that every set \( C \) with \( C \subseteq S \) for all \( S \in \sS \) satisfies \( C \subseteq \bigcap \sS \). Deduce that \( \bigcap \{A, B\} = A \cap B \) for all sets \( A \), \( B \).
:::
:::

::: {.solution}
[Hint 1]

For (a), cut a set out of \( A \) by a property that nothing has. For (b), unwind the membership condition of \( \bigcap \sS \) from @prp-zf-basic-sets (c).
:::

::: {.solution}
[Hint 2]

For (a): consider \( \{ x \in A : x \ne x \} \). For (b): let \( x \in \bigcap \sS \) and \( S \in \sS \); what does the condition say at this \( S \)?
:::

::: {.solution}
(a) Let \( A \) be a set. By (Z6) with the property \( \neg(x = x) \), the set \( E \coloneqq \{ x \in A : x \ne x \} \) exists. If \( x \in E \), then \( x \ne x \), which contradicts \( x = x \) (\( \rulename{{=}I} \), @def-rules-equality). So \( E \) has no elements, and (Z2) holds. Thus in the presence of (Z6), (Z2) says only "there is a set". The Axiom of Infinity of Section 9.3 also says that a set exists, so it could replace (Z2) altogether; that is how the full system is often stated, with the clause "\( \emptyset \in I \)" of Section 9.3 read as "\( I \) has an element with no elements", so that the symbol \( \emptyset \) is not needed before (Z2) is. (In the logic of Chapter 4 even "there is a set" can be derived: \( \rulename{{=}I} \) gives \( x = x \), and \( \rulename{\exists I} \) gives \( \exists x\, (x = x) \), because every domain is non-empty, Section 4.11. We keep (Z2) anyway, so that the axioms say plainly where the first set comes from.)

(b) Let \( x \in \bigcap \sS \) and \( S \in \sS \). By the membership condition of @prp-zf-basic-sets (c), \( x \) lies in every member of \( \sS \), in particular in \( S \). So \( \bigcap \sS \subseteq S \).

Now let \( C \) be a set with \( C \subseteq S \) for every \( S \in \sS \), and let \( x \in C \). Then \( x \in S \) for every \( S \in \sS \). Choose \( A_0 \in \sS \) (possible, as \( \sS \) is non-empty); then \( x \in A_0 \) as well, and so \( x \) satisfies the defining condition of \( \bigcap \sS \). Hence \( C \subseteq \bigcap \sS \).

For \( \sS = \{A, B\} \), which is non-empty, the members are exactly \( A \) and \( B \) (@prp-zf-basic-sets (b)). By the first part with \( S = A \) and with \( S = B \), \( \bigcap \{A, B\} \subseteq A \) and \( \bigcap \{A, B\} \subseteq B \), so \( \bigcap \{A, B\} \subseteq A \cap B \). Conversely, \( A \cap B \subseteq A \) and \( A \cap B \subseteq B \), so \( A \cap B \subseteq S \) for every \( S \in \{A, B\} \), and the second part gives \( A \cap B \subseteq \bigcap \{A, B\} \). Hence \( \bigcap \{A, B\} = A \cap B \) (@prp-subset-antisymmetric).

In words, (b) says that \( \bigcap \sS \) is the **largest** set contained in every member of \( \sS \): it is contained in each of them, and it contains every other set that is.

**Marking scheme.** (10 points)
- 3: (a) produces a set with no elements by (Z6) from a given set, with a property that no set has, and proves it has no elements.
- 2: (b) shows \( \bigcap \sS \subseteq S \) from the membership condition, at the given \( S \).
- 3: (b) shows \( C \subseteq \bigcap \sS \), placing \( x \) in the ambient member \( A_0 \) as well as in every \( S \).
- 2: deduces \( \bigcap \{A, B\} = A \cap B \) using that the members of \( \{A, B\} \) are exactly \( A \) and \( B \): by double inclusion, \( \bigcap \{A, B\} \subseteq A \cap B \) from the first half of (b) at \( S = A \) and \( S = B \), and \( A \cap B \subseteq \bigcap \{A, B\} \) from the second half with \( C = A \cap B \), then @prp-subset-antisymmetric (or (Z1)). A solution that compares membership conditions directly earns the same 2.

Fatal errors (0 for the step): using a set of all sets, or \( \bigcap \emptyset \); in (a), assuming \( \emptyset \) exists in order to prove (Z2).
:::

<!-- dependency ledger
ax-zf-fragment (claim): with phi the formula x notin B, no B satisfies x in B <-> (x in A and x notin B) when A has an element | inline (the instance x := that element gives P <-> (true and not P))
ax-zf-fragment (claim): each defined symbol unwinds into a formula in in and = | inline (two examples given; the rest by the same unwinding)
ax-zf-fragment (example): P({emptyset}) = {emptyset, {emptyset}} | exm-power-set-small (cited), whose argument uses only extensionality and excluded middle
ax-zf-fragment (claim): Infinity is (Z7), stated in Section 9.3 | Section 9.3 (prose pointer, this chapter; nothing here depends on it)
ax-zf-fragment (claim): (Z1)-(Z6) cannot produce a set with infinitely many elements | not proved in this book (a theorem of set theory, marked as such in the text); nothing rests on it
ax-zf-fragment (claim): Replacement and Foundation are left to the set-theory volume | prose pointer outside this book; nothing depends on it
prp-zf-basic-sets (proof): "x = a or x = a" iff "x = a"; "x = d or x = c" iff "x = c or x = d" | propositional logic (vee-I, vee-E; disjunction commutes, exm-disjunction-first-derivations in Ch 1)
prp-zf-basic-sets (proof): case split on a = c or a = d | vee-E, def-rules-disjunction (Ch 1)
exr-sets-from-axioms-c1 (solution): exists x (x = x) is derivable because every domain is non-empty | Section 4.11 (prose; nothing in the exercise rests on it)
exr-sets-from-axioms-c1 (solution): the clause "emptyset in I" of Section 9.3 | Section 9.3 (prose pointer, this chapter; a remark, nothing rests on it)
-->
