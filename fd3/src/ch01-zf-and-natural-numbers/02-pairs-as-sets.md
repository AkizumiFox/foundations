# Ordered Pairs Built from Sets

Section 6.3 introduced the ordered pair (@def-ordered-pair) as an object with one property, the characteristic property, and said that such an object could be built from sets. Section 9.1 has only sets to build with, and its pair \( \{a, b\} \) forgets which element came first. This section repairs that with one idea: mark the first coordinate by putting it in a set of its own. It proves that the result has the characteristic property, so that every pair of Chapters 6 to 8 can be read as a set, and then recovers the product \( A \times B \) and the working rules (W1)–(W5) of Section 6.1 from the axioms, in the form proved here: (W2) for lists written out in the text, (W3) for families of subsets of a given set, and (W5) for pairs. The rest of (W2) and (W5) comes in Section 9.6; (W3) for families with no ambient set needs the axiom of Replacement.

## Order from sets

**The problem.** The set \( \{a, b\} \) of @prp-zf-basic-sets (b) is symmetric: \( \{a, b\} = \{b, a\} \). A pair must not be. We want a set, built from \( a \) and \( b \) by the axioms, from which we can read off **which** of the two came first, and the second coordinate after that. Here is one way to see what to do. In \( \{a, b\} \) the two elements are on an equal footing; we must give \( a \) a role that \( b \) does not have. Put \( a \) into **every** member of the pair, and \( b \) into one member only.

*The first coordinate is the one in every member.*

::: {#def-kuratowski-pair}
[Ordered Pair as a Set]

For sets \( a \) and \( b \), the **ordered pair** of \( a \) and \( b \) is the set
\[
(a, b) \coloneqq \{\{a\}, \{a, b\}\} .
\]
Its **first coordinate** is \( a \) and its **second coordinate** is \( b \).
:::

The pair is a set of the axioms: (Z3) gives \( \{a\} = \{a, a\} \) and \( \{a, b\} \), and (Z3) once more gives the set whose elements are these two (@prp-zf-basic-sets (b)). In words: the members of \( (a, b) \) are the sets \( \{a\} \) and \( \{a, b\} \), which coincide when \( a = b \). Sets of this form are called **Kuratowski pairs**. The first coordinate lies in both members; the second lies in the member \( \{a, b\} \), and in \( \{a\} \) only if it equals \( a \).

Examples, simplest first.

- \( (a, a) = \{\{a\}, \{a, a\}\} = \{\{a\}, \{a\}\} = \{\{a\}\} \). This is the degenerate case: the two members coincide, and the pair has **one** member. It matters, because a proof that speaks of "the two members of a pair" silently excludes it.
- \( (\{\emptyset\}, \emptyset) = \{\{\{\emptyset\}\}, \{\{\emptyset\}, \emptyset\}\} \). Its two members are different: \( \emptyset \) lies in the second and not in the first, whose only element is \( \{\emptyset\} \).
- Swap the coordinates: \( (\emptyset, \{\emptyset\}) = \{\{\emptyset\}, \{\emptyset, \{\emptyset\}\}\} \). The second member is the same as before, \( \{\emptyset, \{\emptyset\}\} \); the singleton member has changed from \( \{\{\emptyset\}\} \) to \( \{\emptyset\} \). So \( (\{\emptyset\}, \emptyset) \ne (\emptyset, \{\emptyset\}) \), and the singleton member is what records the order.

**Why this definition: shorter encodings fail.** It is natural to try something simpler first. The next example shows three simpler sets, built from \( a \) and \( b \) with \( a \) written first, none of which is a pair.

::: {#exm-failed-pair-encodings}
[Three Encodings That Lose Information]

Consider the claim: *any set built from \( a \) and \( b \) in which \( a \) is mentioned first is an ordered pair*, that is, has the characteristic property. Test it on the three encodings
\[
\text{(i) } \{a, b\}, \qquad \text{(ii) } \{\{a\}, \{b\}\}, \qquad \text{(iii) } \{a, \{b\}\} .
\]
:::

::: {.solution}
The claim is **false**, and each encoding has its own counterexample.

(i) With \( a = \emptyset \), \( b = \{\emptyset\} \) and with the coordinates swapped, the encoding gives \( \{\emptyset, \{\emptyset\}\} \) both times, although \( \emptyset \ne \{\emptyset\} \). The order is lost.

(ii) The same two inputs give \( \{\{\emptyset\}, \{\{\emptyset\}\}\} \) both times: the encoding is \( \{\{a\}, \{b\}\} = \{\{b\}, \{a\}\} \), again symmetric in \( a \) and \( b \).

(iii) This one is not symmetric, and it fails in a less obvious way. Take \( a = \{\{\emptyset\}\} \), \( b = \emptyset \), and \( c = \{\emptyset\} \), \( d = \{\emptyset\} \). Then
\[
\{a, \{b\}\} = \{\{\{\emptyset\}\}, \{\emptyset\}\}, \qquad \{c, \{d\}\} = \{\{\emptyset\}, \{\{\emptyset\}\}\},
\]
the same set, by (Z1). But \( a \ne c \): the only element of \( a = \{\{\emptyset\}\} \) is \( \{\emptyset\} \), which is not \( \emptyset \), so \( \emptyset \in c \) and \( \emptyset \notin a \). So equal encodings do not force equal first coordinates. The trouble is that \( \{b\} \) can coincide with a first coordinate, and the encoding cannot tell which of its elements was meant as "\( a \)".

The definition avoids both failures. Both of its members are built from \( a \), so neither can be mistaken for a lone coordinate, and the member \( \{a\} \) singles out \( a \). Another encoding, often called the Wiener pair, uses \( \emptyset \) as a marker; exercise C3 asks you to show that it has the characteristic property.
:::

The lesson of (iii) is a habit: a proposed encoding is tested against the characteristic property with **all** inputs, including inputs that are themselves made of the sets being encoded.

::: {.warning}
**"The smaller member" names nothing when \( a = b \).** It is tempting to read off the first coordinate as "the element of the smaller member" and the second as "the new element of the larger member". When \( a = b \), the pair \( (a, a) = \{\{a\}\} \) has a **single** member, and there is no smaller and larger. An argument that compares the two members of \( (a, b) \) must treat \( a = b \) as a case of its own.
:::

## The characteristic property

Here is what makes the definition the right one: the set \( (a, b) \) determines \( a \) and \( b \), each in its place.

::: {#thm-kuratowski-pair}
[Characteristic Property of Pairs]

For all sets \( a, b, c, d \),
\[
(a, b) = (c, d) \iff a = c \text{ and } b = d .
\]
:::

*Try it first (ten minutes): given \( \{\{a\}, \{a, b\}\} = \{\{c\}, \{c, d\}\} \), get \( a = c \) first; then ask what changes when \( a = b \).*

::: {.idea}
The attempt goes well at first. The member \( \{a\} \) of the left side is a member of the right side, so \( \{a\} = \{c\} \) or \( \{a\} = \{c, d\} \), and either way @prp-zf-basic-sets (d) gives \( a = c \). Then \( \{a, b\} \) must be one of \( \{c\} \), \( \{c, d\} \), and the natural move is to say "it is \( \{c, d\} \), the larger one", giving \( \{a, b\} = \{a, d\} \) and so \( b = d \). That move is where the attempt runs into the warning above. If \( a = b \), then \( \{a, b\} = \{a\} \) and it may well equal \( \{c\} \); if \( c = d \), the right side has a single member. So the proof splits: when \( a = b \), the left side is \( \{\{a\}\} \), and both members of the right side must equal \( \{a\} \); when \( a \ne b \), both sides have two different members, and the matching above goes through.

*Before reading on: where is \( a \ne b \) used?*
:::

::: {.proof}
\( (\Leftarrow) \) If \( a = c \) and \( b = d \), then \( (a, b) = (c, d) \) by \( \rulename{{=}E} \).

\( (\Rightarrow) \) Suppose \( (a, b) = (c, d) \), that is, \( \{\{a\}, \{a, b\}\} = \{\{c\}, \{c, d\}\} \). Either \( a = b \) or \( a \ne b \), and we take the cases in turn.

*Case 1: \( a = b \).* Then \( \{a, b\} = \{a\} \), so \( (a, b) = \{\{a\}\} \). The members \( \{c\} \) and \( \{c, d\} \) of \( (c, d) \) are members of \( \{\{a\}\} \), so \( \{c\} = \{a\} \) and \( \{c, d\} = \{a\} \). By @prp-zf-basic-sets (d), the second equation gives \( a = c \) and \( c = d \). Hence \( a = c \), and \( b = a = c = d \).

*Case 2: \( a \ne b \).* First, \( c \ne d \). Indeed, if \( c = d \), then \( (c, d) = \{\{c\}\} \) as in Case 1, so the member \( \{a, b\} \) of \( (a, b) \) equals \( \{c\} \), and @prp-zf-basic-sets (d) gives \( c = a \) and \( a = b \), which contradicts \( a \ne b \).

Next, \( \{a\} \in (a, b) = (c, d) \), so \( \{a\} = \{c\} \) or \( \{a\} = \{c, d\} \). The second would give \( c = d \) by @prp-zf-basic-sets (d), which we have excluded. So \( \{a\} = \{c\} \), and \( a = c \) by the same proposition.

Finally, \( \{a, b\} \in (c, d) \), so \( \{a, b\} = \{c\} \) or \( \{a, b\} = \{c, d\} \). The first would give \( a = c \) and \( c = b \) by @prp-zf-basic-sets (d), hence \( a = b \), which is excluded. So \( \{a, b\} = \{c, d\} = \{a, d\} \), using \( c = a \). By @prp-zf-basic-sets (d), \( (a = a \wedge b = d) \vee (a = d \wedge b = a) \); in the first disjunct \( b = d \), and in the second \( b = a = d \). So \( b = d \).

In both cases \( a = c \) and \( b = d \). This proves the theorem.
:::

So \( a \ne b \) is used twice in Case 2: to exclude \( c = d \), and to exclude \( \{a, b\} = \{c\} \). Once both are excluded, each side has exactly two different members, and they can be matched.

**Alternatively**, the coordinates can be read off a pair \( p = (a, b) \) by two set operations. The members of \( p \) are \( \{a\} \) and \( \{a, b\} \) (@prp-zf-basic-sets (b)). An object lies in both if and only if it equals \( a \), since it must lie in \( \{a\} \), and \( a \in \{a, b\} \); so \( \bigcap p = \{a\} \) (@prp-zf-basic-sets (c)). And \( \bigcup p = \{a\} \cup \{a, b\} = \{a, b\} \). So \( a \) is the unique element of \( \bigcap p \). And \( \bigcup p \setminus \bigcap p = \{a, b\} \setminus \{a\} \) is \( \{b\} \) if \( b \ne a \), and \( \emptyset \) if \( b = a \); so \( b \) is the unique element of \( \bigcup p \setminus \bigcap p \) when that set is non-empty, and \( b = a \) when it is empty. Both coordinates are thus determined by the set \( p \) alone, which is the characteristic property again. The case split has not gone away here: it is the empty and non-empty cases of \( \bigcup p \setminus \bigcap p \). Comparing the unions of two pairs directly avoids it: from \( \{a, b\} = \{c, d\} \) with \( c = a \), @prp-zf-basic-sets (d) gives \( b = d \) in both of its disjuncts.

**What this pays.** Section 6.3 took the ordered pair as given, with the characteristic property, and said after @def-ordered-pair that nothing else about pairs is used in Chapter 6, apart from one working convention. From here on, the pair \( (a, b) \) of @def-ordered-pair **is** the set of @def-kuratowski-pair, and the property it was assumed to have is @thm-kuratowski-pair. Everything built on pairs becomes a set built by the axioms: a relation from \( A \) to \( B \) is a subset of \( A \times B \) (@def-relation), and a function \( X \to Y \) is the pair \( (G, Y) \) of its graph and codomain (@def-function), now a Kuratowski pair of two sets. The working convention said that **a pair is not a number**, and that a triple is not a pair. In the picture of this chapter numbers and tuples will be sets too, so both clauses become statements to be checked: Section 9.4 checks the first for the natural numbers (@prp-pair-not-natural), and Section 9.6 checks the second (@prp-tuples-as-sets (c)).

## Products, and the working rules recovered

The working rule (W5) said that the pairs with coordinates in given sets form a set. With pairs built from sets, this is now something to prove.

::: {#prp-cartesian-product-exists}
[The Product Exists]

For all sets \( A \) and \( B \) there is **exactly one** set \( A \times B \) whose elements are exactly the pairs \( (a, b) \) with \( a \in A \) and \( b \in B \):
\[
p \in A \times B \iff \exists a \in A\ \exists b \in B\ \ p = (a, b) .
\]
:::

::: {.idea}
Separation can only cut a set out of a set we already have, so we first need **some** set containing every pair \( (a, b) \) with \( a \in A \) and \( b \in B \). The members \( \{a\} \) and \( \{a, b\} \) of such a pair are subsets of \( A \cup B \), so the pair is a set of subsets of \( A \cup B \): an element of \( \powerset{\powerset{A \cup B}} \). Cut \( A \times B \) out of that.
:::

::: {.proof}
Let \( U \coloneqq A \cup B \), a set by @prp-zf-basic-sets (c), and let \( W \coloneqq \powerset{\powerset{U}} \), a set by (Z5) twice. Let \( a \in A \) and \( b \in B \). Then \( a, b \in U \), so \( \{a\} \subseteq U \) and \( \{a, b\} \subseteq U \); that is, \( \{a\} \in \powerset{U} \) and \( \{a, b\} \in \powerset{U} \). Hence \( (a, b) = \{\{a\}, \{a, b\}\} \subseteq \powerset{U} \), that is, \( (a, b) \in W \).

By (Z6) with ambient set \( W \) and parameters \( A \), \( B \), let
\[
A \times B \coloneqq \{ p \in W : \exists a \in A\ \exists b \in B\ \ p = (a, b) \} .
\]
(The property is admissible: "\( p = (a, b) \)" unwinds into \( \in \) and \( = \), as Section 9.1 explained for defined symbols.) If \( p \in A \times B \), then \( p = (a, b) \) for some \( a \in A \), \( b \in B \). Conversely, if \( p = (a, b) \) with \( a \in A \) and \( b \in B \), then \( p \in W \) by the first paragraph, so \( p \in A \times B \). This is the displayed membership condition. Any two sets with this condition are equal by (Z1).
:::

The product of @def-cartesian-product has the same membership condition, so it is this set; and \( X^2 \coloneqq X \times X \) is a set too. The construction never needed a "set of all pairs": every pair it collects lies in the set \( W \), which depends on \( A \) and \( B \).

The working rules of Section 6.1 can now be checked against the axioms one by one.

::: {#prp-working-rules-from-axioms}
[The Working Rules from the Axioms]

The axioms (Z1)–(Z6) give the working rules (W1)–(W5) of Section 6.1 in the following form.

::: {.enumerate options="label=(W\arabic*)"}
1. For every set \( A \) and every admissible property \( P(x) \) (one whose unwinding is a formula of the language, Section 9.1), \( \{ x \in A : P(x) \} \) is a set.
2. For each list \( a_1, \dots, a_n \) written out in the text, entry by entry, there is a set \( \{a_1, \dots, a_n\} \) whose elements are exactly \( a_1, \dots, a_n \).
3. For sets \( A \) and \( B \), \( A \cup B \) is a set. For a set \( X \) and a family \( (A_i)_{i \in I} \) of subsets of \( X \), given as a function \( I \to \powerset{X} \) (@def-indexed-family), the union \( \bigcup_{i \in I} A_i \) and the intersection \( \bigcap_{i \in I} A_i \) of @def-family-union-intersection are sets.
4. For every set \( X \), \( \powerset{X} \) is a set.
5. For sets \( A \) and \( B \), \( A \times B \) is a set.
:::
:::

::: {.idea}
Three of the rules are already in hand. For a written list, add one entry at a time with \( \cup \). For a union of a family of subsets of \( X \), the ambient set \( X \) is what lets (Z6) apply.
:::

::: {.proof}
(W1) is (Z6), applied to the unwinding of \( P(x) \), with the sets \( P \) mentions as parameters; (W4) is (Z5), and (W5) is @prp-cartesian-product-exists.

(W2) We build the set one entry at a time. The first set is \( \{a_1\} \), by (Z3). If \( \{a_1, \dots, a_k\} \) has been built and the list has a further entry \( a_{k+1} \), let
\[
\{a_1, \dots, a_{k+1}\} \coloneqq \{a_1, \dots, a_k\} \cup \{a_{k+1}\},
\]
a set by @prp-zf-basic-sets (c). Its elements are those of \( \{a_1, \dots, a_k\} \) together with \( a_{k+1} \), that is, the \( x \) with \( x = a_1 \vee \dots \vee x = a_{k+1} \). A list written out in the text has a definite number of entries, and the step is applied once for each entry after the first.

(W3) \( A \cup B \) is a set by @prp-zf-basic-sets (c). Now let \( f \colon I \to \powerset{X} \) be the function with \( f(i) = A_i \), and let \( G \) be its graph. By (Z6) with ambient set \( X \) and parameters \( I \), \( G \),
\[
V \coloneqq \{ x \in X : \exists i \in I\ \, x \in f(i) \}
\]
is a set; "\( x \in f(i) \)" unwinds to \( \exists S\, \bigl((i, S) \in G \wedge x \in S\bigr) \). Every element of every \( A_i \) lies in \( X \), since \( A_i \subseteq X \); so \( x \in V \) if and only if \( x \in A_i \) for some \( i \in I \), the membership condition of @def-family-union-intersection (a). Hence \( V \) is the union. The intersection of @def-family-union-intersection (b) is defined there by a set-builder inside \( X \), so it exists by (Z6).
:::

The proof of (W2) deserves a second look, because of what it does **not** prove. It is not a proof "for every \( n \in \nN \)": we have no \( \nN \) yet, so the number of entries cannot be a variable. It is a recipe which, applied to any list actually written down, produces its set in as many steps as the list has entries. That is all (W2) is used for in Section 6.1, but Chapters 7 and 8 also write \( \{x_1, \dots, x_n\} \) for a **variable** \( n \), for a function \( x \) defined on \( \{1, \dots, n\} \) (@prp-finite-max, @def-finite). That second half of (W2) needs the natural numbers and \( \{1, \dots, n\} \) as sets; it is part (d) of a proposition in Section 9.6, which also builds \( n \)-tuples and so gives (W5) for them.

The rest of the list is paid elsewhere. A family of sets with **no** ambient set \( X \) needs the axiom of Replacement, which belongs to the volume on set theory. And (W6), "\( \nN \), \( \nZ \), \( \nQ \), \( \nR \) are sets", becomes a series of constructions: \( \nN \) in Section 9.3, \( \nZ \) and \( \nQ \) in Chapter 10, and \( \nR \) later in this volume, from Cauchy sequences of rationals.

::: {.check}
Write \( (\emptyset, \emptyset) \) and \( (\emptyset, \{\emptyset\}) \) as sets, using only braces and \( \emptyset \).
:::

::: {.solution}
\( (\emptyset, \emptyset) = \{\{\emptyset\}, \{\emptyset, \emptyset\}\} = \{\{\emptyset\}\} \), a set with one member, as for every pair \( (a, a) \). And \( (\emptyset, \{\emptyset\}) = \{\{\emptyset\}, \{\emptyset, \{\emptyset\}\}\} \), with two different members.
:::

## Exercises

### A. Check your understanding

::: {#exr-pairs-as-sets-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. In the proof of @thm-kuratowski-pair, where is the hypothesis \( a \ne b \) of Case 2 used, and what replaces the argument when \( a = b \)?
2. Run the proof of @thm-kuratowski-pair on the equation \( (\{\emptyset\}, \emptyset) = (c, d) \): which case applies, and what does each step give?
3. Which axioms make \( (a, b) \) a set?
4. State the idea of the proof of @thm-kuratowski-pair in two sentences.
:::
:::

::: {.solution}
(a) Twice: to show \( c \ne d \) (if \( c = d \), the member \( \{a, b\} \) would equal \( \{c\} \), forcing \( a = b \)), and to rule out \( \{a, b\} = \{c\} \) (which would force \( a = b \)). When \( a = b \), the pair \( (a, b) = \{\{a\}\} \) has one member, so both members of \( (c, d) \) must equal \( \{a\} \), and \( \{c, d\} = \{a\} \) gives \( c = d = a \) by @prp-zf-basic-sets (d).

(b) Here \( a = \{\emptyset\} \) and \( b = \emptyset \), and \( a \ne b \) because \( \emptyset \in a \) and \( \emptyset \notin b \); so Case 2 applies. Step 1: \( c \ne d \). Step 2: \( \{a\} = \{\{\emptyset\}\} \) is a member of \( (c, d) \), and it cannot be \( \{c, d\} \), so \( \{\{\emptyset\}\} = \{c\} \) and \( c = \{\emptyset\} \). Step 3: \( \{a, b\} = \{\{\emptyset\}, \emptyset\} \) is a member of \( (c, d) \) and is not \( \{c\} \), so \( \{\{\emptyset\}, \emptyset\} = \{c, d\} = \{\{\emptyset\}, d\} \), which gives \( d = \emptyset \). So \( (c, d) = (\{\emptyset\}, \emptyset) \) forces \( c = \{\emptyset\} \) and \( d = \emptyset \).

(c) (Z3), three times: once for \( \{a\} = \{a, a\} \), once for \( \{a, b\} \), and once for the set with these two elements. Uniqueness of each is (Z1).

(d) The singleton member \( \{a\} \) of the pair must be one of the members of the other pair, which pins down the first coordinate. When \( a \ne b \) the remaining members must match and give the second coordinate; when \( a = b \) the pair has a single member, and that case is handled on its own.
:::

### B. Practice

::: {#exr-pairs-as-sets-b1}
[B1: Coordinates from unions and intersections]

Let \( p = (a, b) \). Compute \( \bigcap p \) and \( \bigcup p \), and show that, when \( a \ne b \), the set \( \bigcup p \setminus \bigcap p \) has exactly one element, namely \( b \).
:::

::: {.solution}
The members of \( p \) are \( \{a\} \) and \( \{a, b\} \). An object lies in both if and only if it equals \( a \) (it is in \( \{a\} \)), and \( a \) is in \( \{a, b\} \); so \( \bigcap p = \{a\} \). An object lies in at least one member if and only if it equals \( a \) or \( b \); so \( \bigcup p = \{a, b\} \).

Now let \( a \ne b \). Then \( x \in \bigcup p \setminus \bigcap p \) if and only if (\( x = a \) or \( x = b \)) and \( x \ne a \), that is, if and only if \( x = b \) and \( x \ne a \). Since \( b \ne a \), the element \( b \) satisfies this, and any \( x \) satisfying it equals \( b \). Hence \( \bigcup p \setminus \bigcap p = \{b\} \).
:::

::: {#exr-pairs-as-sets-b2}
[B2: Nested pairs]

Write \( ((a, b), c) \) for the pair whose first coordinate is the pair \( (a, b) \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( ((a, b), c) = ((a', b'), c') \) if and only if \( a = a' \), \( b = b' \) and \( c = c' \).
2. Determine whether \( ((\emptyset, \emptyset), \emptyset) = (\emptyset, (\emptyset, \emptyset)) \). Justify your answer.
:::
:::

::: {.solution}
(a) \( (\Leftarrow) \) by \( \rulename{{=}E} \). \( (\Rightarrow) \) By @thm-kuratowski-pair applied to the outer pairs, \( (a, b) = (a', b') \) and \( c = c' \). By @thm-kuratowski-pair again, \( (a, b) = (a', b') \) gives \( a = a' \) and \( b = b' \).

(b) No. Both sides are pairs, so by @thm-kuratowski-pair they are equal only if their first coordinates are equal. The first coordinates are \( (\emptyset, \emptyset) = \{\{\emptyset\}\} \) and \( \emptyset \), and \( \{\{\emptyset\}\} \ne \emptyset \), since \( \{\emptyset\} \in \{\{\emptyset\}\} \). Hence the two pairs are different.
:::

### C. Going deeper

::: {#exr-pairs-as-sets-c1}
[C1: Exit check: Kuratowski pairs]

Prove that for all sets \( a, b, c, d \), \( \{\{a\}, \{a, b\}\} = \{\{c\}, \{c, d\}\} \) if and only if \( a = c \) and \( b = d \). You may use @prp-zf-basic-sets.
:::

::: {.solution}
This is @thm-kuratowski-pair; its proof above is a complete answer. In outline: \( (\Leftarrow) \) is substitution. For \( (\Rightarrow) \), if \( a = b \), the left side is \( \{\{a\}\} \), so \( \{c, d\} = \{a\} \), giving \( c = d = a = b \). If \( a \ne b \), then \( c \ne d \) (else the left side would have a single member); \( \{a\} \) equals \( \{c\} \) or \( \{c, d\} \), the second being excluded by \( c \ne d \), so \( a = c \); and \( \{a, b\} \) equals \( \{c\} \) or \( \{c, d\} \), the first being excluded by \( a \ne b \), so \( \{a, b\} = \{a, d\} \) and \( b = d \).

**Marking scheme.** (10 points)
- 1: proves \( (\Leftarrow) \) by substitution.
- 2: in the case \( a = b \), identifies \( (a, b) = \{\{a\}\} \) and concludes \( c = d = a \), hence \( a = c \) and \( b = d \).
- 3: in the case \( a \ne b \), shows \( \{a\} = \{c\} \) or \( \{a\} = \{c, d\} \), excludes the second (via \( c \ne d \), itself proved), and concludes \( a = c \).
- 3: obtains \( b = d \) from the remaining members, excluding \( \{a, b\} = \{c\} \) and justifying \( \{a, b\} = \{a, d\} \Rightarrow b = d \).
- 1: joins the two cases into the conclusion.

Fatal errors (0 for the step): treating \( \{a, b\} \) as ordered, or matching "smaller with smaller and larger with larger" without justification; omitting the case \( a = b \) in an argument that matches the members of the two pairs (or reads \( b \) off \( \bigcup p \setminus \bigcap p \)).

Second route (through \( \bigcap p \) and \( \bigcup p \), as in the "Alternatively" paragraph): reading \( a \) off \( \bigcap p = \{a\} \) earns the 3 points for \( a = c \); reading \( b \) off \( \bigcup p \setminus \bigcap p \), with its empty case \( a = b \) treated separately, earns the 3 points for \( b = d \) and the 2 points of the case \( a = b \).

Third route (comparing \( \bigcap \) and \( \bigcup \) of the two pairs): showing \( \bigcap (x, y) = \{x\} \) and \( \bigcup (x, y) = \{x, y\} \) for every pair (no case split is needed), then getting \( a = c \) from \( \{a\} = \{c\} \) and \( b = d \) from \( \{a, b\} = \{c, d\} = \{a, d\} \) by @prp-zf-basic-sets (d), earns the 3 + 3 points and also the 2 + 1 points of the case structure; with \( (\Leftarrow) \) this is 10.
:::

::: {#exr-pairs-as-sets-c2}
[C2: Find the error]

Here is an argument for @thm-kuratowski-pair, direction \( (\Rightarrow) \).

> (1) Let \( (a, b) = (c, d) \). (2) Matching the members of \( \{\{a\}, \{a, b\}\} \) and \( \{\{c\}, \{c, d\}\} \) in the order written, \( \{a\} = \{c\} \) and \( \{a, b\} = \{c, d\} \). (3) From \( \{a\} = \{c\} \), \( a = c \). (4) Then \( \{a, b\} = \{a, d\} \), and so \( b = d \).

Is the conclusion true? Does the argument prove it? If not, name the first line that fails, the rule it breaks, and give a counterexample to that step.
:::

::: {.solution}
The conclusion is **true**: it is @thm-kuratowski-pair.

The argument does not prove it. The first failing line is (2). It uses the rule "if \( \{P, Q\} = \{P', Q'\} \), then \( P = P' \) and \( Q = Q' \)", which treats a set with two members as if it were ordered. No result of Section 9.1 gives this rule: @prp-zf-basic-sets (d) allows the crossed matching \( P = Q' \) and \( Q = P' \) as well. A counterexample to the step: take \( P = Q' = \emptyset \) and \( Q = P' = \{\emptyset\} \). Then \( \{P, Q\} = \{\emptyset, \{\emptyset\}\} = \{P', Q'\} \) by (Z1), but \( P \ne P' \), since \( \emptyset \in \{\emptyset\} \) and \( \emptyset \notin \emptyset \).

For pairs the two equations of line (2) happen to be true, since they follow from the theorem. But showing that the members of \( (a, b) \) and \( (c, d) \) match in this way is the work of the proof: Case 1 handles \( a = b \), where \( (a, b) = \{\{a\}\} \) has a single member, and Case 2 rules out \( c = d \) and \( \{a, b\} = \{c\} \) before matching. So line (2) assumes what is to be proved. This is entry (N9) of @exm-not-allowed-catalogue: line (2) cites a general rule that is false, and for pairs the matching it asserts is the goal itself.

A second, lesser point concerns line (4). "\( \{a, b\} = \{a, d\} \), so \( b = d \)" is true for all \( a, b, d \), but it needs a reason: @prp-zf-basic-sets (d) with \( c = a \). The disjunct \( a = a \wedge b = d \) gives \( b = d \) directly, and the disjunct \( a = d \wedge b = a \) gives \( b = a = d \). No hypothesis \( b \ne a \) is needed, and an answer saying so is correct.

Repair: split into the cases \( a = b \) and \( a \ne b \), as in the proof of the theorem.
:::

::: {#exr-pairs-as-sets-c3}
[C3: Wiener's encoding]

For sets \( a \) and \( b \) let \( W(a, b) \coloneqq \{\{\{a\}, \emptyset\}, \{\{b\}\}\} \). Prove that \( W(a, b) = W(c, d) \) if and only if \( a = c \) and \( b = d \).
:::

::: {.solution}
[Hint 1]

The empty set is a marker. Which member of \( W(a, b) \) has \( \emptyset \) as an element?
:::

::: {.solution}
[Hint 2]

Let \( P \coloneqq \{\{a\}, \emptyset\} \) and \( Q \coloneqq \{\{b\}\} \). Show first that \( \emptyset \in P \) and \( \emptyset \notin Q \).
:::

::: {.solution}
\( (\Leftarrow) \) by \( \rulename{{=}E} \).

\( (\Rightarrow) \) Let \( P \coloneqq \{\{a\}, \emptyset\} \), \( Q \coloneqq \{\{b\}\} \), \( P' \coloneqq \{\{c\}, \emptyset\} \), \( Q' \coloneqq \{\{d\}\} \), and suppose \( \{P, Q\} = \{P', Q'\} \). We have \( \emptyset \in P \) and \( \emptyset \in P' \). On the other hand \( \emptyset \notin Q \): the only element of \( Q \) is \( \{b\} \), and \( \{b\} \ne \emptyset \) because \( b \in \{b\} \). Likewise \( \emptyset \notin Q' \). So \( P \ne Q \) and \( P' \ne Q' \), and in each set of members exactly one member has \( \emptyset \) as an element.

Since \( P \in \{P', Q'\} \), \( P = P' \) or \( P = Q' \); the second is impossible, since \( \emptyset \in P \) and \( \emptyset \notin Q' \). So \( P = P' \). Since \( Q \in \{P', Q'\} \), \( Q = P' \) or \( Q = Q' \); the first is impossible, since \( \emptyset \in P' \) and \( \emptyset \notin Q \). So \( Q = Q' \).

From \( \{\{a\}, \emptyset\} = \{\{c\}, \emptyset\} \), @prp-zf-basic-sets (d) gives \( \{a\} = \{c\} \) (and \( \emptyset = \emptyset \)), or \( \{a\} = \emptyset \) (and \( \emptyset = \{c\} \)). The second is impossible, as \( a \in \{a\} \). So \( \{a\} = \{c\} \), and \( a = c \) by @prp-zf-basic-sets (d) again. From \( \{\{b\}\} = \{\{d\}\} \), the same proposition gives \( \{b\} = \{d\} \) and then \( b = d \).

Unlike @thm-kuratowski-pair, this proof needs no case \( a = b \): the marker \( \emptyset \) tells the two members apart whatever \( a \) and \( b \) are.

**Marking scheme.** (10 points)
- 3: shows \( \emptyset \in P \) and \( \emptyset \notin Q \) (with the reason \( \{b\} \ne \emptyset \)), and likewise for \( P' \), \( Q' \).
- 3: matches \( P = P' \) and \( Q = Q' \), excluding the crossed matches by the marker.
- 2: derives \( a = c \) from \( P = P' \), excluding \( \{a\} = \emptyset \).
- 2: derives \( b = d \) from \( Q = Q' \).

Fatal errors (0 for the step): assuming the members match in the order written; using @thm-kuratowski-pair, which is about a different set.
:::

<!-- dependency ledger
def-kuratowski-pair (example): {emptyset} differs from {{emptyset}}; emptyset differs from {emptyset} | inline (compare elements, Z1)
exm-failed-pair-encodings (example): {{emptyset}} differs from {emptyset}; the two encodings in (iii) are the same set | inline (elements compared; Z1)
thm-kuratowski-pair (proof): either a = b or a != b | excluded middle (prp-excluded-middle, Ch 2)
thm-kuratowski-pair (claim): Chapter 6 uses nothing about pairs but the characteristic property and one working convention (a pair is not a number; a triple is not a pair) | the paragraph after def-ordered-pair (Section 6.3), which says so
thm-kuratowski-pair (claim): Section 9.4 checks that a pair is not a natural number; Section 9.6 checks that a triple is not a pair | Sections 9.4 and 9.6 (prose pointers, this chapter; prp-pair-not-natural, prp-tuples-as-sets (c); nothing here depends on them)
thm-kuratowski-pair (claim): bigcap p = {a} for p = (a, b); comparing unions gives b = d with no case split | inline (members of p by prp-zf-basic-sets (b), bigcap by (c)); prp-zf-basic-sets (d) with c = a (cited)
exr-pairs-as-sets-c2 (solution): {emptyset, {emptyset}} = {{emptyset}, emptyset}; emptyset differs from {emptyset} | inline (Z1; compare elements)
prp-cartesian-product-exists (proof): "p = (a, b)" unwinds into in and = | Section 9.1, paragraph "Properties written with defined symbols"
prp-working-rules-from-axioms (claim): the variable-n half of (W2) and (W5) for n-tuples are paid in Section 9.6 | Section 9.6 (prose pointer, this chapter; prp-tuples-as-sets; nothing here depends on it)
prp-working-rules-from-axioms (claim): families with no ambient set need Replacement | the set-theory volume (prose pointer outside this book; nothing depends on it)
prp-working-rules-from-axioms (claim): N in Section 9.3, Z and Q in Chapter 10, R later in this volume | prose pointers (Section 9.3; Chapter 10; the construction of R from Cauchy sequences); nothing here depends on them
prp-working-rules-from-axioms (proof): elements of {a_1..a_k} union {a_(k+1)} are those with x = a_1 or ... or x = a_(k+1) | prp-zf-basic-sets (c) (cited), disjunctions grouped to the right
exr-pairs-as-sets-a1 (solution): {emptyset} differs from emptyset | inline
-->
