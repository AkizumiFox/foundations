# Parked: from old Section 1.4, transitive sets, ω satisfies (P1)–(P5), pairs are not natural numbers

<!-- Parked from fd3 (fd3/authoring/design/layout-proposal.md §4, approved 2026-10-26). Not part of any book's src; nothing builds or scans it.
Old section: fd3 1.4 The Natural Numbers Satisfy Peano's Axioms (parts) (04-peano-properties.md)
Labels: def-transitive-set, lem-omega-transitive, thm-omega-peano, prp-pair-not-natural
Intended home: ST.1 (ω satisfies Peano's axioms; transitive sets; pairs are not natural numbers)
-->

## Transitive sets

We want to prove: if \( m, n \in \omega \) and \( \mathrm{S}(m) = \mathrm{S}(n) \), then \( m = n \). The tempting move is to cancel, reading \( m \cup \{m\} = n \cup \{n\} \) as "the same thing was added to both". But union does not cancel: \( \{1\} \cup \{0\} = \{0\} \cup \{1\} \), and \( 0 \ne 1 \). What \( \mathrm{S}(m) = \mathrm{S}(n) \) does give is membership. Since \( m \in \mathrm{S}(m) = \mathrm{S}(n) \), either \( m \in n \) or \( m = n \); and likewise \( n \in m \) or \( n = m \). So the one bad case is \( m \in n \) and \( n \in m \) at once, two sets each inside the other.

For the numerals, membership only ever points to earlier numerals, and the elements of an element are earlier still. In \( 3 = \{0, 1, 2\} \), the element \( 2 \) has the elements \( 0 \) and \( 1 \), and both are again elements of \( 3 \). This is the property we name.

*A transitive set contains the elements of its elements.*

::: {#def-transitive-set}
[Transitive set]

A set \( x \) is **transitive** if **every** element of \( x \) is a subset of \( x \): for every \( y \in x \), \( y \subseteq x \).
:::

In words: unpacking \( y \subseteq x \) (@fd2:def-subset), \( x \) is transitive when, for all sets \( y \) and \( z \),
\[
z \in y \ \text{ and } \ y \in x \ \Longrightarrow \ z \in x .
\]
Membership passes through \( x \) in two steps: whatever is an element of an element of \( x \) is already an element of \( x \). The name comes from this display, which has the shape of the transitivity of a relation (@fd2:def-relation-properties) with \( \in \) as the relation and \( x \) fixed at the end.

Examples, simplest first.

- \( \emptyset \) is transitive, vacuously: it has no element \( y \) at which the condition could fail. This degenerate case is the base of every induction below.
- \( 1 = \{0\} \) is transitive: its only element is \( 0 = \emptyset \), and \( \emptyset \subseteq 1 \).
- \( 3 = \{0, 1, 2\} \) is transitive: \( 0 = \emptyset \subseteq 3 \), \( 1 = \{0\} \subseteq 3 \), and \( 2 = \{0, 1\} \subseteq 3 \).

A non-example by minimal change: remove \( 1 \) from \( 3 \). The set \( \{0, 2\} \) is not transitive, because its element \( 2 = \{0, 1\} \) has the element \( 1 \), and \( 1 \notin \{0, 2\} \) (\( 1 \) differs from \( 0 \) and from \( 2 \), @exm-von-neumann-numerals). Deleting one element broke the property at exactly one place.

::: {.remark}
Transitivity is a property of the set, and it fails for sets that look harmless. The set \( \{1\} = \{\{\emptyset\}\} \) is not transitive: \( 1 \in \{1\} \), but \( 1 = \{0\} \) is not a subset of \( \{1\} \), since \( 0 \notin \{1\} \) (as \( 0 \ne 1 \)).
:::

If \( m \) is transitive, then \( n \in m \) gives \( n \subseteq m \), so \( m \in n \) and \( n \in m \) together give \( m \in m \). So the bad case above reduces to a set that is an element of itself. The lemma below rules that out for natural numbers, and with it the bad case.

::: {#lem-omega-transitive}
[Natural Numbers Are Transitive Sets]

::: {.enumerate options="label=(\alph*)"}
1. Every \( n \in \omega \) is a transitive set.
2. \( \omega \) is a transitive set: every element of a natural number is a natural number.
3. \( n \notin n \) for every \( n \in \omega \).
4. Every \( n \in \omega \) with \( n \ne 0 \) is \( \mathrm{S}(k) \) for some \( k \in \omega \).
5. \( 0 \in n \) for every \( n \in \omega \) with \( n \ne 0 \).
:::
:::

::: {.idea}
Each part is one use of the move of the previous section, **show the set is inductive**, in its property form @thm-omega-induction (b). The base is always \( 0 = \emptyset \), where the claim is empty or immediate. The steps of (a)–(c) start from "\( y \in \mathrm{S}(n) \) means \( y \in n \) or \( y = n \)" and treat the two cases. Part (c) is the only one that uses an earlier part: it argues by contradiction inside the step, and transitivity (a) is what turns a membership one level down into the forbidden \( n \in n \). In (d) and (e) the statement is false at \( 0 \), so the property carried is a disjunction "\( n = 0 \) or …". *Before reading on: in the proof of (c), why does \( \mathrm{S}(n) \in n \) give \( n \in n \)?*
:::

::: {.proof}
Each part is proved by @thm-omega-induction (b), with the property named at its start.

*(a)* Let \( P(n) \) be "\( n \) is transitive". \( P(0) \) holds because \( \emptyset \) has no elements. Let \( n \in \omega \) be transitive, and let \( y \in \mathrm{S}(n) \). If \( y \in n \), then \( y \subseteq n \) because \( n \) is transitive, and \( n \subseteq \mathrm{S}(n) \); so \( y \subseteq \mathrm{S}(n) \). If \( y = n \), then \( y = n \subseteq \mathrm{S}(n) \). In both cases \( y \subseteq \mathrm{S}(n) \), so \( \mathrm{S}(n) \) is transitive.

*(b)* Let \( P(n) \) be "\( n \subseteq \omega \)". \( P(0) \) holds because \( \emptyset \subseteq \omega \). Let \( n \in \omega \) with \( n \subseteq \omega \). The elements of \( \mathrm{S}(n) = n \cup \{n\} \) are the elements of \( n \), which lie in \( \omega \) by hypothesis, and \( n \) itself, which lies in \( \omega \) by the choice of \( n \). So \( \mathrm{S}(n) \subseteq \omega \). Hence \( n \subseteq \omega \) for every \( n \in \omega \), which says that \( \omega \) is transitive.

*(c)* Let \( P(n) \) be "\( n \notin n \)". \( P(0) \) holds because \( \emptyset \) has no elements. Let \( n \in \omega \) with \( n \notin n \), and suppose \( \mathrm{S}(n) \in \mathrm{S}(n) \). Then \( \mathrm{S}(n) \in n \) or \( \mathrm{S}(n) = n \).

- If \( \mathrm{S}(n) \in n \), then \( \mathrm{S}(n) \subseteq n \), because \( n \) is transitive by (a); and \( n \in \mathrm{S}(n) \), so \( n \in n \).
- If \( \mathrm{S}(n) = n \), then \( n \in \mathrm{S}(n) = n \).

Both cases contradict \( n \notin n \). So \( \mathrm{S}(n) \notin \mathrm{S}(n) \), by \( \rulename{\neg I} \) (@fd1:def-rules-negation).

*(d)* Let \( P(n) \) be "\( n = 0 \), or \( n = \mathrm{S}(k) \) for some \( k \in \omega \)". \( P(0) \) holds by the first alternative. For every \( n \in \omega \), \( P(\mathrm{S}(n)) \) holds by the second alternative, with \( k \coloneqq n \). So \( P(n) \) holds for every \( n \in \omega \), and for \( n \ne 0 \) the second alternative is the claim.

*(e)* Let \( P(n) \) be "\( n = 0 \) or \( 0 \in n \)". \( P(0) \) holds by the first alternative. Let \( n \in \omega \) with \( P(n) \). If \( n = 0 \), then \( \mathrm{S}(n) = \{0\} \), which has \( 0 \) as an element. If \( 0 \in n \), then \( 0 \in n \subseteq \mathrm{S}(n) \). Either way \( 0 \in \mathrm{S}(n) \), so \( P(\mathrm{S}(n)) \) holds. So \( P(n) \) holds for every \( n \in \omega \), and for \( n \ne 0 \) the second alternative is the claim. This proves the lemma.
:::

The step of (d) never used \( P(n) \). As with the predecessor in *Sets and Functions*, Chapter 3 (@fd2:exm-predecessor-no-hypothesis), the step's conclusion was reached outright, and induction is still what guarantees that \( 0 \) and the successors are all there is. Part (b) says that the natural numbers are built only from natural numbers: unwrapping a natural number never leads outside \( \omega \). Part (c) is the fact the bad case needed.

## Peano's axioms for the natural numbers

Here is the list. Its five items are traditionally called **Peano's axioms**; for \( \omega \) they are theorems.

::: {#thm-omega-peano}
[Peano's Axioms Hold in \( \omega \)]

::: {.enumerate options="label=(P\arabic*)"}
1. \( 0 \in \omega \).
2. For every \( n \in \omega \), \( \mathrm{S}(n) \in \omega \).
3. For every \( n \in \omega \), \( \mathrm{S}(n) \ne 0 \).
4. For all \( m, n \in \omega \), if \( \mathrm{S}(m) = \mathrm{S}(n) \), then \( m = n \).
5. Every \( A \subseteq \omega \) with \( 0 \in A \) and \( \mathrm{S}(n) \in A \) for every \( n \in A \) is equal to \( \omega \).
:::

Moreover, \( \{ (n, \mathrm{S}(n)) : n \in \omega \} \) is a set, and with codomain \( \omega \) it is a function \( \mathrm{S} \colon \omega \to \omega \), which is injective and does not take the value \( 0 \).
:::

::: {.idea}
(P1), (P2) and (P5) are the previous section restated: \( \omega \) is inductive, and induction holds. (P3) is one line, since \( n \in \mathrm{S}(n) \) and nothing is an element of \( \emptyset \). (P4) is the argument of the opening of this section: \( \mathrm{S}(m) = \mathrm{S}(n) \) leaves only the case \( m \in n \) and \( n \in m \) to exclude, and transitivity with \( m \notin m \) excludes it.
:::

::: {.proof}
(P1) and (P2) say that \( \omega \) is inductive, which is @thm-omega-least-inductive (a). (P5) is @thm-omega-induction (a).

(P3) Let \( n \in \omega \). Then \( n \in \mathrm{S}(n) \). If \( \mathrm{S}(n) = 0 \), then \( n \in 0 \) by \( \rulename{{=}E} \) (@fd1:def-rules-equality), which is impossible, since \( 0 = \emptyset \) has no elements. So \( \mathrm{S}(n) \ne 0 \), by \( \rulename{\neg I} \) (@fd1:def-rules-negation).

(P4) Let \( m, n \in \omega \) with \( \mathrm{S}(m) = \mathrm{S}(n) \). Since \( m \in \mathrm{S}(m) = \mathrm{S}(n) \), we have \( m \in n \) or \( m = n \); likewise, since \( n \in \mathrm{S}(n) = \mathrm{S}(m) \), we have \( n \in m \) or \( n = m \). Suppose \( m \ne n \). Then \( m \in n \) and \( n \in m \). Since \( m \) is transitive (@lem-omega-transitive (a)) and \( n \in m \), we get \( n \subseteq m \); so \( m \in n \subseteq m \), that is, \( m \in m \). This contradicts @lem-omega-transitive (c). Hence \( m = n \), by \( \rulename{RAA} \) (@fd1:def-rule-raa).

For the function: let \( G \coloneqq \{ p \in \omega \times \omega : p = (n, \mathrm{S}(n)) \text{ for some } n \in \omega \} \), a set by Separation (Z6) inside the product \( \omega \times \omega \) of @prp-cartesian-product-exists; the pairs \( (n, \mathrm{S}(n)) \) lie in that product by (P2). We check the two clauses of @fd2:def-function. (Fn1): for \( n \in \omega \), \( (n, \mathrm{S}(n)) \in G \). (Fn2): if \( (n, y) \in G \) and \( (n, y') \in G \), then \( (n, y) = (k, \mathrm{S}(k)) \) and \( (n, y') = (k', \mathrm{S}(k')) \) for some \( k, k' \in \omega \); by @thm-kuratowski-pair, \( k = n = k' \), and then \( y = \mathrm{S}(n) = y' \). So \( (G, \omega) \) is a function \( \omega \to \omega \), whose value at \( n \) is \( \mathrm{S}(n) \). It is injective by (P4) (@fd2:def-injective), and \( 0 \) is not a value by (P3). This proves the theorem.
:::

The function \( \mathrm{S} \colon \omega \to \omega \) and the operation \( x \mapsto \mathrm{S}(x) \) on all sets share a letter, and they agree wherever both are defined. Only the first is a set. The operation has no graph: a set containing the pair \( (x, \mathrm{S}(x)) = \{\{x\}, \{x, \mathrm{S}(x)\}\} \) for **every** set \( x \) would give, after two unions, a set containing every set, which @fd2:thm-russell forbids.

One more consequence is used constantly. By @lem-omega-transitive (d), every \( n \in \omega \) with \( n \ne 0 \) is \( \mathrm{S}(k) \) for some \( k \in \omega \), and by (P4) this \( k \) is **unique**: if \( \mathrm{S}(k) = n = \mathrm{S}(k') \), then \( k = k' \). So every non-zero natural number has exactly one predecessor, and \( 0 \) has none, by (P3).

::: {.check}
Is the function \( \mathrm{S} \colon \omega \to \omega \) surjective? Is \( \omega \in \omega \)?
:::

::: {.solution}
No to both. \( \mathrm{S} \) is not surjective: \( 0 \in \omega \), and by (P3) no \( n \in \omega \) has \( \mathrm{S}(n) = 0 \). (Every other natural number is a value, by @lem-omega-transitive (d).)

If \( \omega \in \omega \), then \( \omega \) would be a natural number \( n \) with \( n \in n \), which @lem-omega-transitive (c) rules out. So \( \omega \notin \omega \). In particular \( \omega \) is a set that is not a natural number, although all its elements are.
:::

## Pairs are not natural numbers

*Sets and Functions*, Chapter 1 adopted a working convention, stated after @fd2:def-ordered-pair: a pair is not a number. In that chapter numbers were given and pairs were postulated, and the convention said they were different kinds of object. Now both are sets: a pair is the set \( \{\{a\}, \{a, b\}\} \) of @def-kuratowski-pair, and a natural number is an element of \( \omega \). For natural numbers the convention becomes a theorem.

::: {#prp-pair-not-natural}
[No Pair Is a Natural Number]

For all sets \( a \) and \( b \), the pair \( (a, b) \) is not an element of \( \omega \).
:::

::: {.idea}
Every natural number other than \( 0 \) has \( \emptyset \) as an element, by @lem-omega-transitive (e). A pair is not \( \emptyset \), and it does not have \( \emptyset \) as an element, because both of its elements contain \( a \).
:::

::: {.proof}
Let \( a, b \) be sets, and suppose \( (a, b) = \{\{a\}, \{a, b\}\} \in \omega \) (@def-kuratowski-pair). The pair has the element \( \{a\} \), so \( (a, b) \ne \emptyset = 0 \). By @lem-omega-transitive (e), \( 0 = \emptyset \in (a, b) \), so \( \emptyset = \{a\} \) or \( \emptyset = \{a, b\} \). Both are impossible, since \( a \in \{a\} \) and \( a \in \{a, b\} \), while \( \emptyset \) has no elements. This contradiction shows \( (a, b) \notin \omega \).
:::

So, for instance, the tagged numbers \( (n, 0) \) in the second example of a Peano system above are never natural numbers, and *Sets and Functions*, Chapter 1's answer that \( ((1, 2), 3) \ne (1, (2, 3)) \) because "a pair is not a number" is borne out by @prp-pair-not-natural once the numbers \( 1 \), \( 2 \), \( 3 \) are read as elements of \( \omega \), as the later chapters of this volume read \( \nN \) (Section 1.4). The same statement for \( n \)-tuples with \( n \ge 3 \) needs a definition of \( n \)-tuples, which comes later in this chapter, together with the order on \( \omega \).

::: {.warning}
The encoding produces true statements that sound absurd. Since \( \{0\} = 1 \) and \( \{0, 1\} = 2 \),
\[
(0, 1) = \{\{0\}, \{0, 1\}\} = \{1, 2\} ,
\]
so "\( 1 \in (0, 1) \)" is **true** of the pair \( (0, 1) \), although \( 1 \) is not in the open interval \( (0, 1) \) of real numbers, and "\( 0 \in (0, 1) \)" is **false** of the pair. Such a statement is a fact about how pairs were encoded as sets, not about pairs: with Wiener's encoding \( \{\{\{a\}, \emptyset\}, \{\{b\}\}\} \), met in Section 1.2 (@exr-pairs-as-sets-c3), the pair of \( 0 \) and \( 1 \) is \( \{2, \{\{1\}\}\} \), which does not have \( 1 \) as an element. A proof about pairs should use only their characteristic property, @thm-kuratowski-pair. The places in this section that look inside a pair (the remark after @thm-omega-peano that the operation \( x \mapsto \mathrm{S}(x) \) has no graph, the closing remark of the tagged-numbers example that \( (0, 0) = \{\{0\}\} \) is not \( \emptyset \), @prp-pair-not-natural, and this warning) are about the encoding itself.
:::

<!-- dependency ledger
def-transitive-set (example): 0, 1, 2 are distinct; 1 = {0}, 2 = {0, 1}, 3 = {0, 1, 2} | exm-von-neumann-numerals (cited)
lem-omega-transitive (proof): y in S(n) iff y in n or y = n; n subset of S(n) | def-set-successor and the paragraph after it (inline)
lem-omega-transitive (proof): (d) the move "step without using the hypothesis" is valid | exm-predecessor-no-hypothesis (cited, F2.2)
thm-omega-peano (proof): (P3) a set with an element differs from the empty set | inline: =E of def-rules-equality and not-I of def-rules-negation (cited)
thm-omega-peano (claim): (the paragraph after it) a set containing (x, S(x)) for every x gives, after two unions, a set containing every set | inline: x in {x, S(x)} in (x, S(x)); thm-russell (cited)
prp-pair-not-natural (claim): (the paragraph after it) the n-tuple version, n >= 3 | prp-tuples-as-sets (e), later in this chapter (prose pointer; nothing in this section depends on it)
prp-pair-not-natural (claim): (the paragraph after it) F2.1's 1, 2, 3 read as elements of omega, as the later chapters read N | cor-omega-identification, F3.1 §07 (prose pointer, this chapter; nothing in this section depends on it)
prp-pair-not-natural (claim): (the warning after it) {0} = 1 and {0, 1} = 2, so (0, 1) = {1, 2} | def-kuratowski-pair and exm-von-neumann-numerals (cited)
prp-pair-not-natural (claim): (the warning after it) Wiener's pair of 0 and 1 is {2, {{1}}}, and 1 is not an element of it | inline ({0} = 1, {0, emptyset} = 2; 1 != 2 and 1 != {{1}} since 0 in 1 and 0 not in {{1}}); the encoding itself is F3.1 §02's exercise C3 (exr-pairs-as-sets-c3, cited only as a pointer; nothing here depends on it)
-->
