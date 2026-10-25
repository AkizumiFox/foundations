# Equivalent Forms of Choice

Three statements have now appeared. The axiom of choice (@ax-choice) picks one element from each set of a family of non-empty sets. Zorn's lemma (@thm-zorn) gives a maximal element when every chain has an upper bound. The third is new: every set can be well-ordered, so that each of its non-empty subsets has a least element and "take the least one" becomes a rule that picks. This section proves that Zorn's lemma implies the other two, and that the well-ordering theorem implies the axiom again, by that rule. It also finishes the matching that opened Section 6.2: any two sets are comparable in size. The one missing implication, from the axiom to Zorn's lemma, needs a recursion that runs past every natural number; *Axiomatic Set Theory*, Chapter 4 proves it, and with it the three statements are equivalent.

## Zorn's lemma gives choice

::: {#thm-choice-from-zorn}
[Zorn's Lemma Gives Choice]

Assume @thm-zorn. Let \( I \) be a set and \( (A_i)_{i \in I} \) a family of **non-empty** sets. Then there is a function \( c \colon I \to \bigcup_{i \in I} A_i \) with \( c(i) \in A_i \) for every \( i \in I \).
:::

This is the conclusion of @ax-choice, so the axiom follows from Zorn's lemma.

::: {.idea}
By the method of @exm-method-maximality. A choice function can be built one index at a time, like the matching that opened Section 6.2. A **partial choice function** is a set \( G \subseteq I \times U \), \( U \coloneqq \bigcup_{i \in I} A_i \), with (C1) \( (i, x) \in G \Rightarrow x \in A_i \) and (C2) \( (i, x), (i, y) \in G \Rightarrow x = y \); let \( P \) be the set of them, ordered by \( \subseteq \). (C1) and (C2) mention at most two pairs, so unions of chains stay in \( P \); a maximal one that missed an index \( i_0 \) could take one \( x_0 \in A_{i_0} \). Choosing that \( x_0 \) is **one** use of \( \rulename{\exists E} \); Zorn's lemma does the infinitely many.
:::

::: {.proof}
Let \( U \) and \( P \) be as in the Idea. Then \( P \subseteq \powerset{I \times U} \) is a set, partially ordered by \( \subseteq \).

*\( P \) is non-empty:* \( \emptyset \) satisfies (C1) and (C2) vacuously.

*Chains have upper bounds:* let \( \sC \subseteq P \) be a non-empty chain and \( H \coloneqq \bigcup \sC \subseteq I \times U \). If \( (i, x) \in H \), it lies in some \( G \in \sC \), so \( x \in A_i \) by (C1) for \( G \). If \( (i, x), (i, y) \in H \), some \( G \in \sC \) contains both (@lem-chain-union (b) with \( n = 2 \)), so \( x = y \) by (C2) for \( G \). So \( H \in P \), and \( G \subseteq H \) for every \( G \in \sC \): \( H \) is an upper bound of \( \sC \) in \( P \).

*Zorn:* by @thm-zorn, \( P \) has a maximal element \( M \).

*\( M \) is defined everywhere:* suppose some \( i_0 \in I \) has no pair \( (i_0, x) \in M \). Since \( A_{i_0} \ne \emptyset \), take \( x_0 \in A_{i_0} \), and let \( M' \coloneqq M \cup \{(i_0, x_0)\} \). Then \( M' \subseteq I \times U \), since \( i_0 \in I \) and \( x_0 \in A_{i_0} \subseteq U \); \( M' \) satisfies (C1), and it satisfies (C2), because the only pair of \( M' \) with first coordinate \( i_0 \) is \( (i_0, x_0) \). So \( M' \in P \), \( M \subseteq M' \), and \( M \ne M' \), as \( (i_0, x_0) \notin M \); this contradicts the maximality of \( M \). Hence for every \( i \in I \) there is a pair \( (i, x) \in M \), and by (C2) exactly one. By @def-function, \( M \) is the graph of a function \( c \colon I \to U \), and \( c(i) \in A_i \) by (C1).
:::

If \( I = \emptyset \), then \( P = \{\emptyset\} \), and the proof produces the empty function, which is correct. Of the proof's four steps, only the last uses that the \( A_i \) are non-empty; the other three follow the template (@exm-method-maximality), with (C1) and (C2) as the conditions.

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

Comparability is itself equivalent to the axiom of choice, a fact proved in *Axiomatic Set Theory*, Chapter 4: this book needed choice for it, and no proof can avoid it. (The converse direction passes through well-orders, by a theorem of Hartogs that *Axiomatic Set Theory* proves.)

::: {.check}
Run the proof of @thm-cardinal-comparability on \( A = \{1, 2, 3\} \) and \( B = \{x, y\} \): describe the maximal elements of \( P \), and say which case of the proof occurs.
:::

::: {.solution}
A partial matching has at most two pairs, since each of \( x \), \( y \) occurs at most once. The maximal elements are the six two-pair matchings \( \{ (a, x), (a', y) \} \) with \( a \ne a' \) in \( A \) (three choices of \( a \), then two of \( a' \)). A matching with fewer pairs is not maximal: it leaves some element of \( A \) and some element of \( B \) unpaired, and one more pair fits. No maximal \( M \) pairs every element of \( A \): that would be an injection \( A \to B \), impossible by @cor-pigeonhole-finite-sets (a). So Case 2 occurs every time: \( M^{-1} \) is an injection \( B \to A \). This is the finite example of Section 6.2, where the matching \( (1, x) \), \( (2, y) \) ran out of \( B \).
:::

A maximal matching tells us which side is used up, not that the sizes differ. For \( A = B = \nN \), the identity \( \{ (n, n) : n \in \nN \} \) is a maximal matching that uses up both sides. So is \( \{ (n, n + 1) : n \in \nN \} \): it pairs every element of \( A \), and although \( 0 \in B \) is unpaired, no element of \( A \) is left to pair it with. That matching is an injection and not a bijection, although \( \card{\nN} = \card{\nN} \). The proof only promises an injection, and that is all it delivers.

## The well-ordering theorem

Section 6.1 met one rule that picks, again and again: the least element of a non-empty set of natural numbers (@thm-well-ordering). A set on which that rule works for every non-empty subset is a well-ordered set (@def-well-ordered-set). If a set \( U \) carries a well-order, a family of non-empty subsets of \( U \) needs no axiom: take the least element of each. \( \nR \) with \( \le \) is not well-ordered, since \( (0, 1) \) has no least element. The question is whether some **other** order on \( \nR \), or on any set, is a well-order. For a countable set an answer can be written down.

::: {.check}
Find a well-order on \( \nZ \). Hint: list \( 0, -1, 1, -2, 2, \dots \).
:::

::: {.solution}
Let \( m \preceq_{\nZ} n \) mean: \( \abs{m} < \abs{n} \), or \( \abs{m} = \abs{n} \) and \( m \le n \). It is a total order: compare \( \abs{m} \) and \( \abs{n} \) first, then \( m \) and \( n \). For a non-empty \( S \subseteq \nZ \), the set \( \{ \abs{s} : s \in S \} \subseteq \nN \) has a least element \( k \) (@thm-well-ordering). The least element of \( S \) for \( \preceq_{\nZ} \) is \( -k \) if \( -k \in S \), and \( k \) otherwise. So \( (\nZ, \preceq_{\nZ}) \) is well-ordered, and it lists \( \nZ \) in the order of the hint.
:::

The same idea works for every countable set. An injection \( j \colon X \to \nN \) well-orders \( X \) by "\( x \) before \( x' \) when \( j(x) \le j(x') \)": a non-empty \( S \subseteq X \) has as least element the point whose image is least in \( j(S) \), so every countable set has a well-order with no axiom (Exercise B2 asks for the proof). For \( \nR \) no formula for a well-order is known (compare the family with no rule in sight, the third example after @ax-choice); the theorem shows that one exists.

**Extending a well-order at the top: initial segments.** The proof builds a well-order of \( X \) piece by piece, by the template. A partial object is a pair \( (A, R) \) with \( A \subseteq X \) and \( R \) a well-order on \( A \) (so \( R \subseteq A \times A \)). For two of them, write \( (A, R) \trianglelefteq (B, S) \) when

- (E1) \( A \subseteq B \) and \( R \subseteq S \), and
- (E2) \( a \mathrel{S} b \) for every \( a \in A \) and every \( b \in B \setminus A \):

\( S \) keeps the order of \( R \) and puts every new element **above** all of \( A \). Exercise C3 shows that this says \( A \) is an **initial segment** of \( (B, S) \): everything of \( B \) below an element of \( A \) lies in \( A \), and \( S \) agrees with \( R \) on \( A \). Let \( P \) be the set of partial objects; it is a set, since \( P \subseteq \powerset{X} \times \powerset{X \times X} \) (@def-set-builder, @def-power-set). Then \( \trianglelefteq \) is a partial order on \( P \). It is reflexive, since for \( (A, R) \trianglelefteq (A, R) \) the set \( A \setminus A \) is empty and (E2) holds vacuously. It is antisymmetric, since (E1) both ways gives \( A = B \) and \( R = S \). It is transitive: let \( (A, R) \trianglelefteq (B, S) \trianglelefteq (C, T) \). (E1) for \( (A, R) \) and \( (C, T) \) follows from the two inclusions. For (E2), let \( a \in A \) and \( c \in C \setminus A \). Either \( c \in B \setminus A \), so \( a \mathrel{S} c \), and \( a \mathrel{T} c \) by \( S \subseteq T \); or \( c \in C \setminus B \), so \( a \mathrel{T} c \) by (E2) for \( (B, S) \trianglelefteq (C, T) \), as \( a \in B \).

Why not order the partial objects by inclusion alone, as the method box does? Inclusion alone is not enough; the warning below shows why.

::: {.warning}
**Ordered by inclusion alone, the template breaks.** Order the partial objects by (E1) only. For \( n \in \nN \) let \( A_n \coloneqq \{ -n, \dots, -1, 0 \} \subseteq \nZ \) and \( R_n \) the order \( \le \) on \( A_n \). Each is a well-order, since \( \le \) is total and every non-empty subset of the finite set \( A_n \) is finite (@prp-subset-finite) and so has a minimum (@prp-finite-max). Under (E1) they form a chain, and the union of the chain is \( \le \) on \( \{ k \in \nZ : k \le 0 \} \), which has no least element. So step (2) of the template fails: the union of the chain is not a partial object. "Every non-empty subset has a least element" speaks about infinitely many elements at once, the failure the method box names. (E2) repairs it: \( (A_n, R_n) \trianglelefteq (A_{n+1}, R_{n+1}) \) fails, since \( -(n + 1) \) is added **below** \( A_n \).
:::

::: {.check}
For which \( m \le n \) is \( (A_m, R_m) \trianglelefteq (A_n, R_n) \) in the warning's example? Which clause fails for the others?
:::

::: {.solution}
Only for \( m = n \). For \( m < n \), (E1) holds, and (E2) fails at \( b = -n \in A_n \setminus A_m \) with \( a = 0 \in A_m \), since \( 0 \le -n \) is false.
:::

::: {#thm-well-ordering-theorem}
[The Well-Ordering Theorem]

Every set \( X \) carries a well-order: there is a partial order \( \preceq \) on \( X \) such that \( (X, \preceq) \) is well-ordered (@def-well-ordered-set).
:::

::: {.idea}
By the method of @exm-method-maximality, with the partial objects \( (A, R) \) ordered by \( \trianglelefteq \). Two things change from the box: the order is \( \trianglelefteq \) rather than \( \subseteq \), and the union of a chain is taken coordinate by coordinate, with @lem-chain-union (a) in place of (b). The chain step is where (E2) earns its place: a least element found in one member stays least in the union, because everything added later sits above it. A maximal partial object covers \( X \), since a missed point can be put on top.
:::

::: {.proof}
Let \( P \) and \( \trianglelefteq \) be as above.

*Partial objects.* \( (\emptyset, \emptyset) \in P \): the empty relation is a well-order on \( \emptyset \), vacuously. So \( P \ne \emptyset \).

*Chains.* Let \( \sC \subseteq P \) be a non-empty chain for \( \trianglelefteq \); let \( A^* \) be the union of the first coordinates of its members and \( R^* \) the union of the second. Finitely many members of \( \sC \) have one member \( \trianglelefteq \)-above them all (@lem-chain-union (a)), and by (E1) its sets contain theirs; so any two or three elements of \( A^* \), and any two pairs of \( R^* \), lie in a single member. Each pair of \( R^* \) lies in some \( R \subseteq A \times A \subseteq A^* \times A^* \), so \( R^* \) is a relation on \( A^* \), and it is reflexive, antisymmetric, transitive and total, each property checked inside one member.

*Least elements.* Let \( \emptyset \ne S \subseteq A^* \). Take \( s \in S \) and a member \( (A_0, R_0) \) with \( s \in A_0 \), and let \( m \) be the \( R_0 \)-least element of the non-empty set \( S \cap A_0 \). For \( t \in S \), take a member \( (A_1, R_1) \) with \( t \in A_1 \). The two members are comparable. If \( (A_1, R_1) \trianglelefteq (A_0, R_0) \), then \( t \in A_0 \) and \( m \mathrel{R_0} t \). If \( (A_0, R_0) \trianglelefteq (A_1, R_1) \), then either \( t \in A_0 \), as before, or \( t \in A_1 \setminus A_0 \) and \( m \mathrel{R_1} t \) by (E2). In every case \( (m, t) \in R^* \), and \( m \in S \): \( m \) is the least element of \( S \). So \( (A^*, R^*) \in P \).

*Upper bound.* Let \( (A, R) \in \sC \). (E1) holds for \( (A, R) \) and \( (A^*, R^*) \) by the definition of the unions. For (E2), let \( a \in A \) and \( b \in A^* \setminus A \), with \( b \in A_1 \) for a member \( (A_1, R_1) \). \( (A_1, R_1) \trianglelefteq (A, R) \) would put \( b \) in \( A \), so \( (A, R) \trianglelefteq (A_1, R_1) \), and \( a \mathrel{R_1} b \) by (E2); hence \( (a, b) \in R^* \). So \( (A^*, R^*) \) is an upper bound of \( \sC \) in \( P \).

*Zorn.* By @thm-zorn, \( P \) has a maximal element \( (M, R_M) \).

*Complete.* Suppose \( M \ne X \), and take \( x \in X \setminus M \) (one \( \rulename{\exists E} \)). Put \( M' \coloneqq M \cup \{x\} \) and \( R' \coloneqq R_M \cup \{ (a, x) : a \in M' \} \). Then \( R' \) is a well-order on \( M' \). The new pairs all end at \( x \), and \( (x, x) \) is the only pair of \( R' \) that starts at \( x \); so (PO1)–(PO3) and totality reduce to those of \( R_M \) together with "everything is below \( x \)". A non-empty \( S \subseteq M' \) has as least element the \( R_M \)-least element of \( S \cap M \) if that set is non-empty, and \( x \) if \( S = \{x\} \). (E1) holds for \( (M, R_M) \) and \( (M', R') \), and so does (E2), since \( M' \setminus M = \{x\} \) and \( a \mathrel{R'} x \) for every \( a \in M \). So \( (M, R_M) \trianglelefteq (M', R') \), and \( x \notin M \) makes the two different, against the maximality of \( (M, R_M) \). Hence \( M = X \), and \( R_M \) is a well-order on \( X \).
:::

The proof never says which well-order it found, and there are many: on \( \nZ \), the order \( \preceq_{\nZ} \) of the Quick check "Find a well-order on \( \nZ \)" and its mirror image (\( k \) before \( -k \)) are two. For \( \nN \) the usual order is one, and \( \le \) on \( \nR \) is not; the theorem gives \( \nR \) a well-order for which no formula is known.

## Well-orders give choice

::: {#prp-well-ordering-gives-choice}
[Well-Orders Give Choice]

Let \( (A_i)_{i \in I} \) be a family of **non-empty** sets, and let \( \preceq \) be a well-order on \( U \coloneqq \bigcup_{i \in I} A_i \). Then \( c(i) \coloneqq \) the \( \preceq \)-least element of \( A_i \) defines a choice function \( c \colon I \to U \), with no appeal to @ax-choice.
:::

::: {.proof}
Each \( A_i \) is a non-empty subset of \( U \), so it has a least element (@def-well-ordered-set), and only one (@prp-greatest-unique). So the set of pairs \( (i, a) \in I \times U \) with \( a \) the least element of \( A_i \) is defined by specification (@def-set-builder). It has exactly one pair for each \( i \in I \), so it is the graph of a function \( c \colon I \to U \) (@def-function), and \( c(i) \in A_i \).
:::

Each hypothesis is needed. Without "non-empty" there is no least element of \( A_i = \emptyset \), and no choice function at all (the non-example by minimal change in Section 6.1). With a total order that is not a well-order the rule can fail: for \( n \ge 1 \), \( A_n \coloneqq (0, \frac{1}{n}) \) in \( (\nR, \le) \) has no least element, since \( \frac{x}{2} < x \) for every \( x \in A_n \).

With @thm-well-ordering-theorem this is a second road from Zorn's lemma to the axiom of choice: Zorn gives a well-order of \( \bigcup_{i \in I} A_i \), and the well-order gives the choice function by a rule. The axiom has not disappeared. It is hidden in the well-order, which for an arbitrary set only Zorn's lemma (or the axiom) supplies; for a countable set an injection into \( \nN \) gives one by a rule (Exercise B2).

::: {.check}
With the well-order \( \preceq_{\nZ} \) on \( \nZ \) of the Quick check "Find a well-order on \( \nZ \)", which element does \( c \) pick from \( \{ n \in \nZ : n^2 > 10 \} \)? From \( \{ n \in \nZ : n > 10 \} \)?
:::

::: {.solution}
The first set is \( \{ n \in \nZ : \abs{n} \ge 4 \} \), since \( 3^2 = 9 \) and \( 4^2 = 16 \). Its least \( \abs{n} \) is \( 4 \), and \( -4 \) is in it, so \( c \) picks \( -4 \). In the second set the least \( \abs{n} \) is \( 11 \), and \( -11 \) is not in it, so \( c \) picks \( 11 \).
:::

## What is proved where

The implications between the forms of choice met in this chapter, and where each is proved:

| Implication | Where |
|---|---|
| Zorn's lemma \( \Rightarrow \) axiom of choice | @thm-choice-from-zorn |
| Zorn's lemma \( \Rightarrow \) every set can be well-ordered | @thm-well-ordering-theorem |
| every set can be well-ordered \( \Rightarrow \) axiom of choice | @prp-well-ordering-gives-choice |
| Zorn's lemma \( \Rightarrow \) any two sets are comparable | @thm-cardinal-comparability |
| axiom of choice \( \Leftrightarrow \) every surjection has a right inverse | @thm-surjection-right-inverse and the paragraph after it (Section 6.1) |
| axiom of choice \( \Rightarrow \) Zorn's lemma | *Axiomatic Set Theory*, Chapter 4 |
| comparability \( \Rightarrow \) every set can be well-ordered | *Axiomatic Set Theory*, Chapter 4 (Hartogs) |

Once the last two rows are proved, all five statements are equivalent. This book takes the axiom and Zorn's lemma as given, uses whichever form fits the problem, and flags each use. *Linear Algebra*, Section 1.8 (@la:thm-basis-extension-general) runs the template once more, with independent sets as partial objects, to extend every independent set to a basis.

The runs of the template in this chapter, side by side:

| Object | Partial objects | Why unions of chains stay partial objects | Why a maximal one is complete |
|---|---|---|---|
| choice function (@thm-choice-from-zorn) | graphs defined on part of \( I \) | (C1), (C2) mention at most two pairs | a missed index can be added |
| representatives (@exm-zorn-representatives) | sets meeting each class at most once | the condition mentions two elements | a missed class can be added |
| injection (@thm-cardinal-comparability) | partial matchings | (M1), (M2) mention two pairs | if both sides have an unpaired element, they can be paired |
| total order (@thm-order-extension) | partial orders containing \( \preceq \) | (PO2), (PO3) mention two pairs | an incomparable pair can be compared (@lem-one-step-order-extension) |
| well-order (@thm-well-ordering-theorem) | well-orders of subsets, ordered by \( \trianglelefteq \) | @lem-chain-union (a) and (E1): the order axioms mention at most three elements; least elements survive because of (E2) | a missed point goes on top |

## Exercises

### A. Check your understanding

::: {#exr-using-zorn-a1}
[A1]

These questions are about the proofs of this section.

::: {.enumerate options="label=(\alph*)"}
1. Where does the proof of @thm-cardinal-comparability use (M1), and where (M2)?
2. In that proof, if \( A = \emptyset \), what is \( M \), and which case occurs?
3. In the proof of @thm-choice-from-zorn, where is "\( A_i \ne \emptyset \)" used, and which step fails without it?
4. In the proof of @thm-well-ordering-theorem, which step uses (E2), and what is \( (M, R_M) \) when \( X = \emptyset \)?
5. For \( X = \{1, 2\} \), list the partial objects \( (A, R) \) of that proof, and the maximal ones.
6. Why does the proof of @prp-well-ordering-gives-choice need no appeal to @ax-choice?
:::
:::

::: {.solution}
(a) The chain step uses both, to show that the union of a chain lies in \( P \). The step "\( M \) uses up a side" uses both for \( M \), to see that \( M \cup \{ (a_0, b_0) \} \) still satisfies them. Case 1 uses (M1) to get a function \( A \to B \) and (M2) for its injectivity; Case 2 uses (M2) to get a function \( B \to A \) and (M1) for its injectivity.

(b) \( A \times B = \emptyset \), so \( P = \{ \emptyset \} \) and \( M = \emptyset \). Case 1 occurs: every element of \( \emptyset \) occurs in \( M \), vacuously, and \( M \) is the graph of the empty function \( \emptyset \to B \), which is injective. If also \( B = \emptyset \), Case 2 holds as well.

(c) In the last step: \( x_0 \in A_{i_0} \) exists only because \( A_{i_0} \ne \emptyset \). Without it, \( M \) could miss \( i_0 \) and still be maximal, and indeed no choice function exists if some \( A_i \) is empty.

(d) The chain step, twice: for least elements of the union (an element of a later member is above \( m \)), and for the union being \( \trianglelefteq \)-above each member. It is also checked in the last step. For \( X = \emptyset \): \( P = \{ (\emptyset, \emptyset) \} \), and \( (M, R_M) = (\emptyset, \emptyset) \), the empty well-order.

(e) Five: \( (\emptyset, \emptyset) \); \( (\{1\}, \{(1, 1)\}) \); \( (\{2\}, \{(2, 2)\}) \); \( (\{1, 2\}, \{(1, 1), (2, 2), (1, 2)\}) \) (\( 1 \) before \( 2 \)); \( (\{1, 2\}, \{(1, 1), (2, 2), (2, 1)\}) \) (\( 2 \) before \( 1 \)). The last two are maximal.

(f) "The least element of \( A_i \)" is one description that names a value for every \( i \), so \( c \) is defined by specification (@exm-method-name-the-choice).
:::

### B. Practice

::: {#exr-using-zorn-r1}
[B1: Surjections one way or the other]

Let \( A \) and \( B \) be non-empty sets. Prove that there is a surjection \( A \to B \) or a surjection \( B \to A \).
:::

::: {.solution}
By @thm-cardinal-comparability, \( \card{A} \le \card{B} \) or \( \card{B} \le \card{A} \). In the first case, since \( A \ne \emptyset \), @prp-card-le-surjection gives a surjection \( B \to A \). In the second, since \( B \ne \emptyset \), the same proposition with the roles exchanged gives a surjection \( A \to B \).

**Marking scheme.** (10 points)
- 3: comparability cited, with the two cases.
- 4: in the first case, a surjection \( B \to A \) from @prp-card-le-surjection, with \( A \ne \emptyset \) used and the direction correct.
- 3: the second case, with the roles exchanged and \( B \ne \emptyset \) used.
:::

::: {#exr-using-zorn-b4}
[B2: Well-orders without Zorn]

::: {.enumerate options="label=(\alph*)"}
1. Let \( j \colon X \to Y \) be injective and let \( \preceq_Y \) be a well-order on \( Y \). Show that "\( x \preceq x' \) when \( j(x) \preceq_Y j(x') \)" is a well-order on \( X \).
2. Deduce, without Zorn's lemma or @ax-choice, that every countable set has a well-order.
3. Deduce that \( \nQ \) has a well-order.
:::
:::

::: {.solution}
(a) (PO1), (PO3) and totality for \( \preceq \) come from those of \( \preceq_Y \), applied to the images. (PO2): \( x \preceq x' \) and \( x' \preceq x \) give \( j(x) \preceq_Y j(x') \preceq_Y j(x) \), so \( j(x) = j(x') \), and \( x = x' \) by injectivity. For \( \emptyset \ne S \subseteq X \), the image \( j(S) \) is a non-empty subset of \( Y \) and has a least element \( j(s_0) \) with \( s_0 \in S \); then \( j(s_0) \preceq_Y j(s) \), that is \( s_0 \preceq s \), for every \( s \in S \).

(b) A countable \( X \) has an injection \( X \to \nN \) (@thm-countable-characterizations, (i) \( \Rightarrow \) (ii), a rule), and \( (\nN, \le) \) is well-ordered (@thm-well-ordering); apply (a). One injection is named by one \( \rulename{\exists E} \). (This is the route of Section 6.2, Exercise C2 (b), where an injection into \( \nN \) picked representatives; here it picks a whole order.)

(c) \( \nQ \) is countable (@thm-integers-rationals-countable), so (b) applies.
:::

::: {#exr-using-zorn-b5}
[B3: Right inverses from a well-order]

Let \( f \colon X \to Y \) be surjective. Using @thm-well-ordering-theorem, define a right inverse of \( f \) by a rule, and say which result of Section 6.1 you have proved again and where its use of choice has gone.
:::

::: {.solution}
Well-order \( X \) by \( \preceq \) (@thm-well-ordering-theorem). For \( y \in Y \), the preimage \( f^{-1}(\{y\}) \) (@def-preimage) is non-empty, since \( f \) is onto, so it has a least element \( g(y) \), and only one (@prp-greatest-unique). So \( g \colon Y \to X \) is defined by specification, and \( f(g(y)) = y \) for every \( y \in Y \). This is @thm-surjection-right-inverse. The choice has moved into the well-order, which came from @thm-zorn; @prp-well-ordering-gives-choice with \( I = Y \) and \( A_y = f^{-1}(\{y\}) \) is the same argument.
:::

::: {#exr-using-zorn-b6}
[B4: Prove or disprove]

Prove each true statement and refute each false one.

::: {.enumerate options="label=(\alph*)"}
1. Every total order on a finite set is a well-order.
2. If \( \preceq \) is a well-order on \( X \) and \( Y \subseteq X \), then \( \preceq \) restricted to \( Y \) is a well-order on \( Y \).
3. \( \ge \) is a well-order on \( \nN \).
4. A well-ordered set with a greatest element is finite.
5. In a well-ordered set, every non-empty subset has a greatest element.
:::
:::

::: {.solution}
(a) **True.** A non-empty subset \( S \) is finite (@prp-subset-finite); list it as \( x_1, \dots, x_n \), \( n \ge 1 \). Let \( \preceq \) be the total order. The reverse relation \( \succeq \) is a partial order (it satisfies (PO1)–(PO3) because \( \preceq \) does) and \( S \) is a chain for it, so @lem-chain-union (a) gives an \( x_k \) with \( x_j \succeq x_k \) for all \( j \): the least element. (On \( \emptyset \) there is no non-empty subset, so the condition holds vacuously.)

(b) **True.** Restriction keeps (PO1)–(PO3) and totality, which are statements about all elements, and a non-empty subset of \( Y \) is a non-empty subset of \( X \); its least element lies in it, hence in \( Y \).

(c) **False.** \( \nN \) itself has no \( \ge \)-least element: that would be a greatest natural number \( g \), but \( g + 1 > g \).

(d) **False.** The order \( \sqsubseteq \) of @exm-divisibility-linear-extension (positive integers in the usual order, \( 0 \) on top) is a well-order on the infinite set \( \nN \) with greatest element \( 0 \): a non-empty \( S \) has as least element its least positive member if it has one (@thm-well-ordering), and \( 0 \) if \( S = \{0\} \).

(e) **False.** \( \nN \) in \( (\nN, \le) \) has no greatest element.
:::

### C. Going deeper

::: {#exr-using-zorn-c2}
[C1: Find the error]

Claim: any two sets are comparable. "Proof": If \( A \) or \( B \) is empty, the empty function is an injection. Otherwise choose \( a_0 \in A \) and \( b_0 \in B \) and pair them. Choose \( a_1 \in A \setminus \{a_0\} \) and \( b_1 \in B \setminus \{b_0\} \), and so on. When one set runs out, the pairs so far are an injection from it into the other.

Is the conclusion true? Does the argument prove it?
:::

::: {.solution}
The conclusion is true: it is @thm-cardinal-comparability. The argument does not prove it. It fails at "and so on … when one set runs out", the gap that (N13) of @fd1:exm-not-allowed-catalogue flags: an "and so on" needs its step, and here the process has no last step in general. Indexed by \( \nN \), it uses a countable set of elements of each side (@prp-countable-image), and for \( A = B = \nR \) neither side runs out, since \( \nR \) is uncountable (@thm-reals-uncountable-decimal). That is a counterexample to the step "the process ends". The argument also makes infinitely many choices with no rule (Section 6.1). The repair is the proof by the template, in which "cannot be continued" replaces "runs out".

**Marking scheme.** (10 points)
- 2: the conclusion is true, with a citation.
- 3: the failing line ("and so on \( \dots \) runs out") identified, with the reason that it has no step.
- 2: a case where no step exhausts a side (for example any infinite \( A \), \( B \)).
- 1: why even the whole \( \nN \)-indexed process cannot exhaust \( \nR \) (countability).
- 2: the repair by the maximality template.
:::

::: {#exr-using-zorn-r2}
[C2: Maximal chains give Zorn's lemma]

::: {.enumerate options="label=(\alph*)"}
1. Let \( C \) be a maximal chain of a partially ordered set \( (X, \preceq) \): a chain contained properly in no chain. Let \( u \) be an upper bound of \( C \) in \( X \). Show that \( u \in C \), that \( u \) is the greatest element of \( C \), and that \( u \) is a maximal element of \( X \).
2. Deduce @thm-zorn from the statement that every chain lies in a maximal chain.
:::
:::

::: {.solution}
(a) Every element of \( C \) is below \( u \), so \( C \cup \{u\} \) is a chain containing \( C \); by maximality it is not larger, so \( u \in C \). Then \( u \in C \) is above every element of \( C \): it is the greatest element of \( C \). Suppose \( u \prec x \) for some \( x \in X \). For every \( c \in C \), \( c \preceq u \preceq x \), so \( C \cup \{x\} \) is a chain, and maximality gives \( x \in C \). Then \( x \preceq u \), and with \( u \preceq x \), (PO2) gives \( x = u \), contradicting \( u \prec x \). So \( u \) is maximal in \( X \).

(b) Let \( P \) be a non-empty partially ordered set in which every non-empty chain has an upper bound. The empty set is a chain, so by the hypothesis (the statement of Section 6.2, Exercise B1, @exr-chains-and-zorn-b1, applied with \( C_0 = \emptyset \)), \( P \) has a maximal chain \( C \). It is not empty: for \( p \in P \), \( \{p\} \) is a chain properly containing \( \emptyset \). So \( C \) has an upper bound \( u \), and \( u \) is a maximal element of \( P \) by (a). Since Exercise B1 was proved from Zorn's lemma, the two statements are equivalent.

**Marking scheme.** (10 points)
- 1: \( u \in C \) in (a).
- 1: \( u \) is the greatest element of \( C \).
- 3: \( u \) is maximal in \( X \), using (PO2).
- 2: a maximal chain \( C \) from the hypothesis (starting from \( \emptyset \) or from \( \{p\} \)).
- 1: \( C \ne \emptyset \) (immediate if the chain was started from \( \{p\} \)).
- 2: an upper bound of \( C \), and the conclusion.
:::

::: {#exr-using-zorn-c3}
[C3: Exit check: initial segments]

Let \( (A, R) \) and \( (B, S) \) be partial objects of the proof of @thm-well-ordering-theorem (well-orders on subsets of \( X \)) with \( A \subseteq B \). Prove that \( (A, R) \trianglelefteq (B, S) \) if and only if

- (i) \( R = S \cap (A \times A) \), and
- (ii) whenever \( a \in A \), \( b \in B \) and \( b \mathrel{S} a \), then \( b \in A \).
:::

::: {.solution}
\( (\Rightarrow) \) (i): \( R \subseteq S \) by (E1), and \( R \subseteq A \times A \); so \( R \subseteq S \cap (A \times A) \). Conversely, let \( (a, a') \in S \) with \( a, a' \in A \). \( R \) is total, so \( (a, a') \in R \) or \( (a', a) \in R \). In the second case \( (a', a) \in S \), and (PO2) for \( S \) gives \( a = a' \), so \( (a, a') = (a, a) \in R \) by (PO1). (ii): if \( b \notin A \), then \( a \mathrel{S} b \) by (E2), and with \( b \mathrel{S} a \), (PO2) gives \( b = a \in A \), a contradiction.

\( (\Leftarrow) \) (E1): \( A \subseteq B \) is given, and \( R \subseteq S \) by (i). (E2): let \( a \in A \) and \( b \in B \setminus A \). \( S \) is total, so \( a \mathrel{S} b \) or \( b \mathrel{S} a \). The second gives \( b \in A \) by (ii), which is false. So \( a \mathrel{S} b \).

**Marking scheme.** (10 points)
- 3: (i) in \( (\Rightarrow) \): 1 for \( R \subseteq S \cap (A \times A) \), 2 for the reverse inclusion by totality of \( R \) and antisymmetry of \( S \).
- 2: (ii) in \( (\Rightarrow) \), with (E2) and antisymmetry.
- 1: (E1) in \( (\Leftarrow) \).
- 4: (E2) in \( (\Leftarrow) \): 2 for comparing \( a \) and \( b \) (totality of \( S \), or the least element of \( \{a, b\} \)), 2 for excluding \( b \mathrel{S} a \) by (ii).
- Fatal errors (0 for the part): proving only \( R \subseteq S \cap (A \times A) \) for (i); in \( (\Leftarrow) \), concluding \( a \mathrel{S} b \) with no comparison of \( a \) and \( b \) at all.
:::

### R. Review

::: {#exr-using-zorn-r4}
[R1]

Let \( D \coloneqq \{2, 3, \dots, 30\} \), partially ordered by divisibility. Find the maximal elements of \( D \). Does \( D \) have a greatest element? A least element?
:::

::: {.solution}
Divisibility is a partial order on \( \nN \) (@prp-divides-partial-order), so on \( D \). An element \( n \in D \) is maximal when no multiple \( kn \) with \( k \ge 2 \) lies in \( D \) (@def-maximal-element), that is, when \( 2n > 30 \): for \( n \le 15 \), \( n \mid 2n \in D \) with \( 2n \ne n \), and for \( n \ge 16 \) every \( kn \) with \( k \ge 2 \) exceeds \( 30 \). So the maximal elements are \( 16, 17, \dots, 30 \).

There is no greatest element. A greatest element would be maximal (@prp-greatest-maximal (a)), so it would be one of \( 16, \dots, 30 \), and every other maximal element would divide it; but \( 16 \nmid 17 \) and \( 17 \nmid 16 \).

There is no least element: it would divide \( 2 \) and \( 3 \), so it would be \( 1 \), and \( 1 \notin D \).
:::

::: {#exr-using-zorn-r5}
[R2]

Let \( \preceq \) be a well-order on \( X \), with strict part \( \prec \). Show that there is no function \( s \colon \nN \to X \) with \( s(n + 1) \prec s(n) \) for every \( n \in \nN \).
:::

::: {.solution}
Suppose there were one. The image \( s(\nN) \) is non-empty, so it has a least element, of the form \( s(k) \) for some \( k \in \nN \). But \( s(k + 1) \in s(\nN) \) and \( s(k + 1) \prec s(k) \), against the minimality of \( s(k) \). The tool is the least-element argument of @exm-no-infinite-descent, with the well-order of \( X \) in place of \( \le \) on \( \nN \).
:::

::: {#exr-using-zorn-r6}
[R3]

Write the statement "\( (X, \preceq) \) is well-ordered" with quantifiers, negate it into positive form, and use the negation to show that \( (\nZ, \le) \) is not well-ordered.
:::

::: {.solution}
By @def-well-ordered-set, well-ordered says that \( \preceq \) is total and that the following least-element clause holds; the negation is therefore \( \preceq \) not total, or the negated clause. The clause is
\[
\forall S \, \bigl( S \subseteq X \wedge S \ne \emptyset \to \exists m \in S \; \forall s \in S \; m \preceq s \bigr).
\]
Its negation (@fd1:prp-bounded-quantifier-negation, as in @fd1:exm-negating-definitions), the second alternative, is
\[
\exists S \, \bigl( S \subseteq X \wedge S \ne \emptyset \wedge \forall m \in S \; \exists s \in S \; s \prec m \bigr),
\]
where \( s \prec m \) stands for "not \( m \preceq s \)", which for a total order means \( s \preceq m \) and \( s \ne m \). For \( \nZ \) with \( \preceq \) the usual \( \le \), take \( S \coloneqq \nZ \): for each \( m \in \nZ \), \( s \coloneqq m - 1 \in S \) has \( s < m \). Since \( \le \) on \( \nZ \) is a total order, it is the least-element condition that fails.
:::

::: {#exr-infinite-sets-r4}
[R4]

A function \( f \colon \nN \to \nN \) is **eventually zero** if there is \( N \in \nN \) with \( f(n) = 0 \) for every \( n \ge N \). Is the set of eventually zero functions countable?
:::

::: {.solution}
*Yes.* The tool is a **countable union of countable sets**. For \( N \in \nN \) let \( Z_N \) be the set of \( f \colon \nN \to \nN \) with \( f(n) = 0 \) for every \( n \ge N \); the set of eventually zero functions is \( Z \coloneqq \bigcup_{N \in \nN} Z_N \). Each \( Z_N \) is countable:

- \( Z_0 \) has one element, the zero function, so it is countable.
- For \( N = 1 \), \( f \mapsto f(0) \) is a bijection \( Z_1 \to \nN \): a function in \( Z_1 \) is determined by its value at \( 0 \), and every value occurs.
- For \( N \ge 2 \), \( f \mapsto (f(0), \dots, f(N - 1)) \) is a bijection \( Z_N \to \nN \times \dots \times \nN \) (\( N \) factors), by the same reasoning and the characteristic property of tuples; the product is countable by @cor-product-countable, and so is \( Z_N \) (compose a surjection \( \nN \to \nN \times \dots \times \nN \) with the inverse bijection, @prp-countable-image).

By @thm-countable-union, \( Z \) is countable. (That theorem uses @ax-choice; here it could be avoided, since each \( Z_N \) comes with an explicit listing, but the question did not ask for that.)

*Why the look-alike fails.* A diagonal argument, as in @thm-binary-sequences-uncountable, builds from a list \( f_0, f_1, \dots \) of eventually zero functions the function \( g(n) \coloneqq f_n(n) + 1 \). It differs from every \( f_n \), but \( g(n) \ge 1 \) for every \( n \), so \( g \) is **not** eventually zero: it is not in \( Z \), and nothing is contradicted. A diagonal argument proves uncountability only when the diagonal object stays inside the set; this is the usual failure named in @exm-method-diagonal.
:::

<!-- dependency ledger
thm-choice-from-zorn (proof): P(I x U) and P are sets | power set and set-builder (F2.1)
thm-cardinal-comparability (proof): P is a set of subsets of A x B; inclusion is a partial order on it | power set and set-builder (F2.1); inclusion on a set of sets as in F2.4 §02 before lem-chain-union
thm-cardinal-comparability (proof): two pairs of a union of a chain lie in one member | lem-chain-union (b) (cited, F2.4 §02)
thm-cardinal-comparability (proof): maximal element | thm-zorn (cited; stated without proof, F2.4 §02; proved in ST.4 (promised))
thm-cardinal-comparability (proof): graph of a function; inverse relation | def-function (F2.6), def-relation (F2.1) (cited)
thm-cardinal-comparability (claim): (Quick check) six maximal matchings of {1,2,3} and {x,y}; none pairs all of A | cor-pigeonhole-finite-sets (a) (cited); verify/ch06/thm-cardinal-comparability.py
cor-cardinal-trichotomy (proof): symmetry of equinumerosity; injections both ways | prp-equinumerous-properties (b), thm-schroder-bernstein, def-card-le (cited)
cor-cardinal-trichotomy (claim): comparability equivalent to choice | ST.4 (prose pointer; nothing depends on it)
exr-using-zorn-c2 (solution): N-indexed process uses countably many elements; R uncountable | prp-countable-image, thm-reals-uncountable-decimal (cited); fd1:exm-not-allowed-catalogue (N13)
exr-using-zorn-r1 (solution): injection gives surjection back | prp-card-le-surjection (cited)
exr-using-zorn-r2 (solution): maximal chain from a given chain | exr-chains-and-zorn-b1 (F2.4 §02, cited)
thm-cardinal-comparability (claim): comparability implies well-ordering (Hartogs) | ST.4 (prose pointer; nothing depends on it)
thm-well-ordering-theorem (claim): (Quick check) |m| < |n|, or |m| = |n| and m <= n, is a well-order on Z with least element -k or k | thm-well-ordering (cited); verify/ch06/thm-well-ordering-theorem.py
thm-well-ordering-theorem (claim): an injection X -> N gives a well-order on X | inline sketch; proved in Exercise B2 (exr-using-zorn-b4); nothing in the main line depends on it
thm-well-ordering-theorem (claim): no formula for a well-order of R is known | prose remark (nothing depends on it), as after ax-choice (F2.4 §01)
thm-well-ordering-theorem (proof): the order (E1)-(E2) is a partial order on P; P is a subset of P(X) x P(X x X) | inline; def-set-builder, def-power-set (cited)
thm-well-ordering-theorem (claim): (E1)-(E2) is equivalent to the initial-segment description | Exercise C3 (exr-using-zorn-c3); nothing depends on it
thm-well-ordering-theorem (claim): (warning) each (A_n, R_n) is a well-order; the union, <= on the non-positive integers, has no least element (k - 1 < k) | prp-subset-finite, prp-finite-max (cited); arithmetic of Z; verify/ch06/thm-well-ordering-theorem.py
thm-well-ordering-theorem (claim): (Quick check) (A_m, R_m) below (A_n, R_n) only for m = n; (E2) fails at b = -n | verify/ch06/thm-well-ordering-theorem.py
thm-well-ordering-theorem (proof): chain step (order axioms and least elements of the coordinatewise union; upper bound) | lem-chain-union (a) (cited); inline case analysis
thm-well-ordering-theorem (proof): maximal element | thm-zorn (cited; stated without proof, F2.4 §02; proved in ST.4 (promised))
thm-well-ordering-theorem (proof): top extension R' is a well-order on M', strictly above (M, R_M) | inline; verify/ch06/thm-well-ordering-theorem.py (all partial objects on {1, 2} and {1, 2, 3})
thm-well-ordering-theorem (claim): (aftermath) the mirror order (k before -k) is a well-order on Z | verify/ch06/thm-well-ordering-theorem.py
prp-well-ordering-gives-choice (proof): the least element is unique; specification; graph of a function | prp-greatest-unique, def-set-builder, def-function (cited)
prp-well-ordering-gives-choice (claim): (0, 1/n) has no least element (x/2 < x) | R order (school fact)
prp-well-ordering-gives-choice (claim): (Quick check) c picks -4 from {n : n^2 > 10} and 11 from {n : n > 10} | arithmetic; verify/ch06/thm-well-ordering-theorem.py
prp-well-ordering-gives-choice (claim): (closing table) AC implies Zorn; comparability implies well-ordering (Hartogs) | ST.4 (prose pointers; nothing depends on them)
prp-well-ordering-gives-choice (claim): (closing table) AC equivalent to right inverses | thm-surjection-right-inverse and the projection remark after it (F2.4 §01)
prp-well-ordering-gives-choice (claim): (closing paragraph) basis extension by the template | LA §1.8, la:thm-basis-extension-general (cross-volume pointer; nothing depends on it)
exr-using-zorn-a1 (solution): (c) the one use of A_i non-empty | inline (moved with exr-chains-and-zorn-a1 (a))
exr-using-zorn-a1 (solution): (e) five partial objects on {1, 2}, two maximal | finite check; verify/ch06/thm-well-ordering-theorem.py
exr-using-zorn-b4 (solution): injection into N from a countable set; Q countable | thm-countable-characterizations, thm-well-ordering, thm-integers-rationals-countable (cited)
exr-using-zorn-b5 (solution): least preimage gives a right inverse | thm-well-ordering-theorem, prp-greatest-unique, def-preimage (cited)
exr-using-zorn-b6 (solution): (a) the reverse order is a partial order (PO1)-(PO3 inherited); least element by lem-chain-union (a) on the reverse order; (d) the order of exm-divisibility-linear-extension is a well-order with greatest element 0; (c) g + 1 > g | lem-chain-union, prp-subset-finite, thm-well-ordering (cited); verify/ch06/exr-using-zorn-b6.py
exr-using-zorn-r4 (solution): maximal elements 16, ..., 30; no greatest; no least | prp-divides-partial-order, prp-greatest-maximal (cited); finite check; verify/ch06/exr-using-zorn-r4.py
exr-using-zorn-r5 (solution): least element of the image | def-well-ordered-set; exm-no-infinite-descent (cited)
exr-using-zorn-r6 (solution): negation of the well-order condition; m - 1 < m in Z | fd1:prp-bounded-quantifier-negation, fd1:exm-negating-definitions (cited); arithmetic of Z
exr-infinite-sets-r4 (solution): Z_N -> N x ... x N (N factors) bijection, N >= 2 | characteristic property of tuples (F2.1 §04, def-ordered-pair)
-->
