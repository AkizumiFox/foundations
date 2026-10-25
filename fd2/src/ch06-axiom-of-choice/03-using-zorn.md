# Equivalent Forms of Choice

<!-- S3: rewrite per blueprint (6.3: opening frame; closing table of implications proved here and in ST.4; layout §1) -->

Section 6.2 turned Zorn's lemma into a four-step template. This section uses it twice. The first use finishes the matching that opened Section 6.2 and answers the question Section 4.4 left open: any two sets are comparable in size. The second extends any partial order to a total one, the infinite form of putting tasks in an order that respects their prerequisites. An optional last subsection shows the same template in linear algebra.

## Back to comparing sizes

Section 4.4 defined \( \card{A} \le \card{B} \) as the existence of an injection \( A \to B \) (@def-card-le) and proved that injections both ways give a bijection (@thm-schroder-bernstein). It left open whether at least one of the two injections always exists. Section 6.2 tried to build one by matching elements pair by pair, and the attempt got two things right: an unfinished matching can be enlarged by one pair, and a growing family of matchings, put together, is again a matching. Those are steps (4) and (2) of the maximality template (@exm-method-maximality), and Zorn's lemma supplies the rest.

::: {#thm-cardinal-comparability}
[Any Two Sets Are Comparable]

For all sets \( A \) and \( B \), \( \card{A} \le \card{B} \) or \( \card{B} \le \card{A} \).
:::

::: {.idea}
By the method of @exm-method-maximality. The partial objects are the partial matchings: relations \( G \subseteq A \times B \) in which each element of \( A \) and each element of \( B \) occurs in at most one pair. The union of a chain of them is one, since each condition mentions two pairs at a time. A maximal matching uses up \( A \) or \( B \), since otherwise one more pair fits; read in the right direction, it is an injection.
:::

::: {.proof}
Let \( P \) be the set of relations \( G \subseteq A \times B \) such that

- (M1) if \( (a, b), (a, b') \in G \), then \( b = b' \);
- (M2) if \( (a, b), (a', b) \in G \), then \( a = a' \);

ordered by \( \subseteq \). It is a set of subsets of \( A \times B \), so \( \subseteq \) is a partial order on it.

*Partial objects.* \( \emptyset \in P \), since (M1) and (M2) hold vacuously; so \( P \ne \emptyset \).

*Chains.* Let \( \sC \subseteq P \) be a non-empty chain and \( H \coloneqq \bigcup \sC \subseteq A \times B \). Any two pairs of \( H \) lie in a single member \( G \in \sC \) (@lem-chain-union (b), with \( n = 2 \)). So if \( (a, b), (a, b') \in H \), then \( b = b' \) by (M1) for \( G \); and (M2) for \( H \) follows in the same way. Hence \( H \in P \), and \( G \subseteq H \) for every \( G \in \sC \): \( H \) is an upper bound of \( \sC \) in \( P \).

*Zorn.* By @thm-zorn, \( P \) has a maximal element \( M \).

*\( M \) uses up a side.* Suppose some \( a_0 \in A \) occurs in no pair of \( M \), and some \( b_0 \in B \) occurs in no pair of \( M \). Then \( M' \coloneqq M \cup \{ (a_0, b_0) \} \) satisfies (M1) and (M2), because the new pair shares no coordinate with a pair of \( M \). So \( M' \in P \), \( M \subseteq M' \), and \( M \ne M' \), since \( (a_0, b_0) \notin M \). This contradicts the maximality of \( M \). Hence every \( a \in A \) occurs in a pair of \( M \), or every \( b \in B \) does.

*Case 1: every \( a \in A \) occurs.* By (M1) it occurs in exactly one pair, so \( M \) is the graph of a function \( f \colon A \to B \) (@def-function). If \( f(a) = f(a') = b \), then \( (a, b), (a', b) \in M \), so \( a = a' \) by (M2): \( f \) is injective, and \( \card{A} \le \card{B} \).

*Case 2: every \( b \in B \) occurs.* Consider the inverse relation \( M^{-1} = \{ (b, a) : (a, b) \in M \} \subseteq B \times A \) (@def-relation). Every \( b \in B \) occurs as a first coordinate of \( M^{-1} \), and by (M2) in exactly one pair; so \( M^{-1} \) is the graph of a function \( g \colon B \to A \). By (M1), \( g(b) = g(b') = a \) gives \( b = b' \): \( g \) is injective, and \( \card{B} \le \card{A} \).
:::

Section 6.2's "continue until one side is used up" has become step (4): a maximal matching cannot be continued, and so a side is used up. The words "and so on" never appear.

::: {#cor-cardinal-trichotomy}
[Trichotomy for Sizes]

For all sets \( A \) and \( B \), exactly one of \( \card{A} < \card{B} \), \( \card{A} = \card{B} \), \( \card{B} < \card{A} \) holds.
:::

::: {.proof}
*At least one.* By @thm-cardinal-comparability, \( \card{A} \le \card{B} \) or \( \card{B} \le \card{A} \). In the first case, either \( \card{A} = \card{B} \), or not, and then \( \card{A} < \card{B} \) by @def-card-le. The second case gives \( \card{B} = \card{A} \), hence \( \card{A} = \card{B} \) (@prp-equinumerous-properties (b)), or \( \card{B} < \card{A} \).

*At most one.* \( \card{A} < \card{B} \) excludes \( \card{A} = \card{B} \) by @def-card-le. \( \card{B} < \card{A} \) excludes \( \card{B} = \card{A} \), and therefore \( \card{A} = \card{B} \), by symmetry (@prp-equinumerous-properties (b)). Finally, \( \card{A} < \card{B} \) and \( \card{B} < \card{A} \) together give injections \( A \to B \) and \( B \to A \), so \( \card{A} = \card{B} \) by @thm-schroder-bernstein, contradicting \( \card{A} < \card{B} \).
:::

Comparability is itself equivalent to the axiom of choice, a fact proved in *Axiomatic Set Theory*, Chapter 4: this book needed choice for it, and no proof can avoid it.

::: {.check}
Run the proof of @thm-cardinal-comparability on \( A = \{1, 2, 3\} \) and \( B = \{x, y\} \): describe the maximal elements of \( P \), and say which case of the proof occurs.
:::

::: {.solution}
A partial matching has at most two pairs, since each of \( x \), \( y \) occurs at most once. The maximal elements are the six two-pair matchings \( \{ (a, x), (a', y) \} \) with \( a \ne a' \) in \( A \) (three choices of \( a \), then two of \( a' \)). A matching with fewer pairs is not maximal: it leaves some element of \( A \) and some element of \( B \) unpaired, and one more pair fits. No maximal \( M \) pairs every element of \( A \): that would be an injection \( A \to B \), impossible by @cor-pigeonhole-finite-sets (a). So Case 2 occurs every time: \( M^{-1} \) is an injection \( B \to A \). This is the finite example of Section 6.2, where the matching \( (1, x) \), \( (2, y) \) ran out of \( B \).
:::

A maximal matching tells us which side is used up, not that the sizes differ. For \( A = B = \nN \), the identity \( \{ (n, n) : n \in \nN \} \) is a maximal matching that uses up both sides. So is \( \{ (n, n + 1) : n \in \nN \} \): it pairs every element of \( A \), and although \( 0 \in B \) is unpaired, no element of \( A \) is left to pair it with. That matching is an injection and not a bijection, although \( \card{\nN} = \card{\nN} \). The proof only promises an injection, and that is all it delivers.

## Zorn's lemma gives choice

::: {#thm-choice-from-zorn}
[Zorn's Lemma Gives Choice]

Assume @thm-zorn. Let \( I \) be a set and \( (A_i)_{i \in I} \) a family of **non-empty** sets. Then there is a function \( c \colon I \to \bigcup_{i \in I} A_i \) with \( c(i) \in A_i \) for every \( i \in I \).
:::

This is the conclusion of @ax-choice, so the axiom follows from Zorn's lemma.

::: {.idea}
[Scratch work]

A choice function can be built one index at a time, like the matching of the first subsection. Call a set of pairs \( (i, x) \) with \( x \in A_i \), at most one pair for each \( i \), a **partial choice function**: it is a graph (@def-function) defined on part of \( I \). Order these by \( \subseteq \): the larger of two comparable ones agrees with the smaller and is defined at more indices. Write \( U \coloneqq \bigcup_{i \in I} A_i \).

| Givens | Goal |
|---|---|
| \( A_i \ne \emptyset \) for each \( i \in I \) | \( c \colon I \to U \) with \( c(i) \in A_i \) for all \( i \) |
| \( P \): the \( G \subseteq I \times U \) with (C1) \( (i, x) \in G \Rightarrow x \in A_i \) and (C2) \( (i, x), (i, y) \in G \Rightarrow x = y \); order \( \subseteq \) | Zorn's hypotheses: \( P \ne \emptyset \), and each non-empty chain has an upper bound in \( P \) |
| \( \emptyset \in P \); for a chain \( \sC \), try \( \bigcup \sC \): (C1) and (C2) mention at most two pairs (@lem-chain-union) | a maximal \( M \in P \) is defined at every \( i \in I \) |
| \( M \) maximal; suppose \( i_0 \) is missed | \( M \cup \{(i_0, x_0)\} \in P \), strictly larger: a contradiction |

The last row is a proof by contradiction (@exm-method-choosing-the-form): a missed index gives a larger partial object. Choosing \( x_0 \in A_{i_0} \) is **one** use of \( \rulename{\exists E} \), which Section 6.1 showed is always allowed; Zorn's lemma does the infinitely many.
:::

::: {.proof}
Let \( U \) and \( P \) be as in the table. Then \( P \subseteq \powerset{I \times U} \) is a set, partially ordered by \( \subseteq \).

*\( P \) is non-empty:* \( \emptyset \) satisfies (C1) and (C2) vacuously.

*Chains have upper bounds:* let \( \sC \subseteq P \) be a non-empty chain and \( H \coloneqq \bigcup \sC \subseteq I \times U \). If \( (i, x) \in H \), it lies in some \( G \in \sC \), so \( x \in A_i \) by (C1) for \( G \). If \( (i, x), (i, y) \in H \), some \( G \in \sC \) contains both (@lem-chain-union (b) with \( n = 2 \)), so \( x = y \) by (C2) for \( G \). So \( H \in P \), and \( G \subseteq H \) for every \( G \in \sC \): \( H \) is an upper bound of \( \sC \) in \( P \).

*Zorn:* by @thm-zorn, \( P \) has a maximal element \( M \).

*\( M \) is defined everywhere:* suppose some \( i_0 \in I \) has no pair \( (i_0, x) \in M \). Since \( A_{i_0} \ne \emptyset \), take \( x_0 \in A_{i_0} \), and let \( M' \coloneqq M \cup \{(i_0, x_0)\} \). Then \( M' \subseteq I \times U \), since \( i_0 \in I \) and \( x_0 \in A_{i_0} \subseteq U \); \( M' \) satisfies (C1), and it satisfies (C2), because the only pair of \( M' \) with first coordinate \( i_0 \) is \( (i_0, x_0) \). So \( M' \in P \), \( M \subseteq M' \), and \( M \ne M' \), as \( (i_0, x_0) \notin M \); this contradicts the maximality of \( M \). Hence for every \( i \in I \) there is a pair \( (i, x) \in M \), and by (C2) exactly one. By @def-function, \( M \) is the graph of a function \( c \colon I \to U \), and \( c(i) \in A_i \) by (C1).
:::

If \( I = \emptyset \), then \( P = \{\emptyset\} \), and the proof produces the empty function, which is correct. Of the proof's four steps, only the last is about choice functions; the first three run the same way in every use of the lemma, and that is worth recording.

## The well-ordering theorem

<!-- S3: rewrite per blueprint (6.3: new: thm-well-ordering-theorem (Zorn gives a well-order), prp-well-ordering-gives-choice; uses def-well-ordered-set) -->

::: {.warning}
<!-- S3: rewrite per blueprint (6.3: warning to be written) -->
:::

## Exercises

### A. Check your understanding

::: {#exr-using-zorn-a1}
[A1]

These questions are about the proof of @thm-cardinal-comparability.

::: {.enumerate options="label=(\alph*)"}
1. Where does the proof use (M1), and where (M2)?
2. Why can "some \( a \in A \) is unpaired" and "some \( b \in B \) is unpaired" not both hold for a maximal \( M \)?
3. If \( A = \emptyset \), what is \( M \), and which case occurs?
4. In two sentences, give the proof's idea.
:::
:::

::: {.solution}
(a) The chain step uses both, to show that the union of a chain lies in \( P \). The step "\( M \) uses up a side" uses both for \( M \), to see that \( M \cup \{ (a_0, b_0) \} \) still satisfies them. Case 1 uses (M1) to get a function \( A \to B \) and (M2) for its injectivity; Case 2 uses (M2) to get a function \( B \to A \) and (M1) for its injectivity.

(b) Then the pair \( (a, b) \) can be added: \( M \cup \{ (a, b) \} \) satisfies (M1) and (M2) and is strictly larger, so \( M \) is not maximal.

(c) \( A \times B = \emptyset \), so \( P = \{ \emptyset \} \) and \( M = \emptyset \). Case 1 occurs: every element of \( \emptyset \) occurs in \( M \), vacuously, and \( M \) is the graph of the empty function \( \emptyset \to B \), which is injective. If also \( B = \emptyset \), Case 2 holds as well.

(d) A maximal partial matching between \( A \) and \( B \) cannot be extended, so it uses up \( A \) or \( B \). Read in the right direction, it is an injection.
:::

### B. Practice

<!-- S3: rewrite per blueprint (6.3: B exercises to be written) -->

### C. Going deeper

::: {#exr-using-zorn-c2}
[C2: Find the error]

Claim: any two sets are comparable. "Proof": If \( A \) or \( B \) is empty, the empty function is an injection. Otherwise choose \( a_0 \in A \) and \( b_0 \in B \) and pair them. Choose \( a_1 \in A \setminus \{a_0\} \) and \( b_1 \in B \setminus \{b_0\} \), and so on. When one set runs out, the pairs so far are an injection from it into the other.

Is the conclusion true? Does the argument prove it?
:::

::: {.solution}
The conclusion is true: it is @thm-cardinal-comparability. The argument does not prove it. It fails at "and so on … when one set runs out", the gap that (N13) of @fd1:exm-not-allowed-catalogue flags: an "and so on" needs its step, and here the process has no last step in general. Indexed by \( \nN \), it uses a countable set of elements of each side (@prp-countable-image), and for \( A = B = \nR \) neither side runs out, since \( \nR \) is uncountable (@thm-reals-uncountable-decimal). That is a counterexample to the step "the process ends". The argument also makes infinitely many choices with no rule (Section 6.1). The repair is the proof by the template, in which "cannot be continued" replaces "runs out".

**Marking scheme.** (10 points)
- 2: the conclusion is true, with a citation.
- 3: the failing line ("and so on \( \dots \) runs out") identified, with the reason that it has no step.
- 3: a counterexample to the step "the process ends" (for example \( A = B = \nR \)), with the countability reason.
- 2: the repair by the maximality template.
:::

### R. Review

::: {#exr-using-zorn-r1}
[R1: Surjections one way or the other]

Let \( A \) and \( B \) be non-empty sets. Prove that there is a surjection \( A \to B \) or a surjection \( B \to A \).
:::

::: {.solution}
By @thm-cardinal-comparability, \( \card{A} \le \card{B} \) or \( \card{B} \le \card{A} \). In the first case, since \( A \ne \emptyset \), @prp-card-le-surjection gives a surjection \( B \to A \). In the second, since \( B \ne \emptyset \), the same proposition with the roles exchanged gives a surjection \( A \to B \).

**Marking scheme.** (10 points)
- 3: comparability cited, with the two cases.
- 4: in the first case, a surjection \( B \to A \) from @prp-card-le-surjection, with \( A \ne \emptyset \) used and the direction correct.
- 3: the second case, with the roles exchanged and \( B \ne \emptyset \) used.
:::

::: {#exr-using-zorn-r2}
[R2: Maximal chains give Zorn's lemma]

::: {.enumerate options="label=(\alph*)"}
1. Let \( C \) be a maximal chain of a partially ordered set \( (X, \preceq) \): a chain contained properly in no chain. Let \( u \) be an upper bound of \( C \) in \( X \). Show that \( u \in C \), that \( u \) is the greatest element of \( C \), and that \( u \) is a maximal element of \( X \).
2. Deduce @thm-zorn from the statement that every chain lies in a maximal chain.
:::
:::

::: {.solution}
(a) Every element of \( C \) is below \( u \), so \( C \cup \{u\} \) is a chain containing \( C \); by maximality it is not larger, so \( u \in C \). Then \( u \in C \) is above every element of \( C \): it is the greatest element of \( C \). Suppose \( u \prec x \) for some \( x \in X \). For every \( c \in C \), \( c \preceq u \preceq x \), so \( C \cup \{x\} \) is a chain, and maximality gives \( x \in C \). Then \( x \preceq u \), and with \( u \preceq x \), (PO2) gives \( x = u \), contradicting \( u \prec x \). So \( u \) is maximal in \( X \).

(b) Let \( P \) be a non-empty partially ordered set in which every non-empty chain has an upper bound. The empty set is a chain, so by Section 6.2, Exercise B1 (@exr-chains-and-zorn-b1) with \( C_0 = \emptyset \), \( P \) has a maximal chain \( C \). It is not empty: for \( p \in P \), \( \{p\} \) is a chain properly containing \( \emptyset \). So \( C \) has an upper bound \( u \), and \( u \) is a maximal element of \( P \) by (a). Since Exercise B1 was proved from Zorn's lemma, the two statements are equivalent.

**Marking scheme.** (10 points)
- 1: \( u \in C \) in (a).
- 1: \( u \) is the greatest element of \( C \).
- 3: \( u \) is maximal in \( X \), using (PO2).
- 2: a maximal chain \( C \) from Exercise B1 with \( C_0 = \emptyset \).
- 1: \( C \ne \emptyset \).
- 2: an upper bound of \( C \), and the conclusion.
:::

<!-- dependency ledger
thm-choice-from-zorn (proof): P(I x U) and P are sets | power set and set-builder (Chapter 1)
thm-cardinal-comparability (proof): P is a set of subsets of A x B; inclusion is a partial order on it | power set and set-builder (F2.1); inclusion on a set of sets as in 5.1 before lem-chain-union
thm-cardinal-comparability (proof): two pairs of a union of a chain lie in one member | lem-chain-union (b) (cited, F2.4 §02)
thm-cardinal-comparability (proof): maximal element | thm-zorn (cited; stated without proof, F2.4 §02; proved in ST.4 (promised))
thm-cardinal-comparability (proof): graph of a function; inverse relation | def-function, def-relation (cited, F2.1)
thm-cardinal-comparability (claim): (Quick check) six maximal matchings of {1,2,3} and {x,y}; none pairs all of A | cor-pigeonhole-finite-sets (a) (cited); verify/ch06/thm-cardinal-comparability.py
cor-cardinal-trichotomy (proof): symmetry of equinumerosity; injections both ways | prp-equinumerous-properties (b), thm-schroder-bernstein, def-card-le (cited)
cor-cardinal-trichotomy (claim): comparability equivalent to choice | ST.4 (prose pointer; nothing depends on it)
exr-using-zorn-c2 (solution): N-indexed process uses countably many elements; R uncountable | prp-countable-image, thm-reals-uncountable-decimal (cited); fd1:exm-not-allowed-catalogue (N13)
exr-using-zorn-r1 (solution): injection gives surjection back | prp-card-le-surjection (cited)
exr-using-zorn-r2 (solution): maximal chain from a given chain | exr-chains-and-zorn-b1 (F2.4 §02, cited)
-->
