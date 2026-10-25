# Using Zorn's Lemma

Section 5.1 turned Zorn's lemma into a four-step template. This section uses it twice. The first use finishes the matching that opened Section 5.1 and answers the question Section 3.4 left open: any two sets are comparable in size. The second extends any partial order to a total one, the infinite form of putting tasks in an order that respects their prerequisites. An optional last subsection shows the same template in linear algebra.

## Back to comparing sizes

Section 3.4 defined \( \card{A} \le \card{B} \) as the existence of an injection \( A \to B \) (@def-card-le) and proved that injections both ways give a bijection (@thm-schroder-bernstein). It left open whether at least one of the two injections always exists. Section 5.1 tried to build one by matching elements pair by pair, and the attempt got two things right: an unfinished matching can be enlarged by one pair, and a growing family of matchings, put together, is again a matching. Those are steps (4) and (2) of the maximality template (@exm-method-maximality), and Zorn's lemma supplies the rest.

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

Section 5.1's "continue until one side is used up" has become step (4): a maximal matching cannot be continued, and so a side is used up. The words "and so on" never appear.

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
A partial matching has at most two pairs, since each of \( x \), \( y \) occurs at most once. The maximal elements are the six two-pair matchings \( \{ (a, x), (a', y) \} \) with \( a \ne a' \) in \( A \) (three choices of \( a \), then two of \( a' \)). A matching with fewer pairs is not maximal: it leaves some element of \( A \) and some element of \( B \) unpaired, and one more pair fits. No maximal \( M \) pairs every element of \( A \): that would be an injection \( A \to B \), impossible by @cor-pigeonhole-finite-sets (a). So Case 2 occurs every time: \( M^{-1} \) is an injection \( B \to A \). This is the finite example of Section 5.1, where the matching \( (1, x) \), \( (2, y) \) ran out of \( B \).
:::

A maximal matching tells us which side is used up, not that the sizes differ. For \( A = B = \nN \), the identity \( \{ (n, n) : n \in \nN \} \) is a maximal matching that uses up both sides. So is \( \{ (n, n + 1) : n \in \nN \} \): it pairs every element of \( A \), and although \( 0 \in B \) is unpaired, no element of \( A \) is left to pair it with. That matching is an injection and not a bijection, although \( \card{\nN} = \card{\nN} \). The proof only promises an injection, and that is all it delivers.

## Extending a partial order

Suppose a project consists of tasks, and some tasks must be done before others. Write \( u \preceq v \) when task \( u \) must come no later than task \( v \): either \( u = v \), or \( u \) must be finished before \( v \) can start, directly or through a sequence of prerequisites. Counting each task as coming no later than itself makes \( \preceq \) reflexive; passing prerequisites along makes it transitive; and no two different tasks can each be required before the other, or nothing could ever start. So \( \preceq \) is a partial order. A **schedule** puts the tasks in one line, and it respects the prerequisites when its order, a total order, contains \( \preceq \).

For finitely many tasks there is a procedure: pick a task with no unfinished prerequisite, do it, and repeat. Here is a small case. Five tasks, survey \( S \), financing \( F \), design \( D \), permit \( P \) and building \( B \), with four prerequisites:
\[
S \text{ before } D, \qquad F \text{ before } D, \qquad D \text{ before } B, \qquad F \text{ before } P .
\]
The order they generate consists of the five pairs \( (t, t) \), the four given pairs, and the two pairs \( (S, B) \) and \( (F, B) \) that the prerequisites pass along through \( D \): eleven pairs in all. At the start, \( S \) and \( F \) have no prerequisites. Picking \( S \), then \( F \), leaves \( D \) and \( P \) free; picking \( D \), then \( P \), frees \( B \). That gives the schedule
\[
S, \ F, \ D, \ P, \ B .
\]
Picking \( F \) first instead, then \( P \), then \( S \), then \( D \), then \( B \), gives a second schedule
\[
F, \ P, \ S, \ D, \ B .
\]
Each contains all eleven pairs: in both lists \( S \) and \( F \) come before \( D \), \( D \) before \( B \), \( F \) before \( P \), and hence \( S \) and \( F \) before \( B \). So schedules are not unique (there are seven in all), and the procedure needs the tasks in hand, one free task at a time, until none is left. For an infinite set with no list there is no last step, and the maximality template does the work instead. Its engine is a single move: two incomparable elements can be made comparable without breaking anything.

A partial order on \( X \) is a relation on \( X \), a subset of \( X \times X \) (@def-relation), so it makes sense to say that one partial order is contained in another.

::: {#lem-one-step-order-extension}
[Adding One Comparison]

Let \( \preceq \) be a partial order on a set \( X \), and let \( a, b \in X \) be incomparable. Let
\[
R \coloneqq {\preceq} \cup \{ (x, y) \in X \times X : x \preceq a \text{ and } b \preceq y \} .
\]
Then \( R \) is a partial order on \( X \), \( {\preceq} \subseteq R \), and \( (a, b) \in R \setminus {\preceq} \).
:::

::: {.idea}
\( R \) puts everything below \( a \) below everything above \( b \). A new pair can break antisymmetry or transitivity only by producing \( b \preceq a \), and incomparability forbids that.
:::

::: {.proof}
Call a pair \( (x, y) \) **new** if \( x \preceq a \) and \( b \preceq y \), and **old** if \( x \preceq y \). Every pair of \( R \) is old or new. The pair \( (a, b) \) is new, since \( a \preceq a \) and \( b \preceq b \) by (PO1), and it is not old, since \( a \) and \( b \) are incomparable. By the definition of \( R \), \( {\preceq} \subseteq R \).

(PO1): \( x \preceq x \) for every \( x \in X \), and \( {\preceq} \subseteq R \).

(PO2): let \( x \mathrel{R} y \) and \( y \mathrel{R} x \). If both pairs are old, \( x = y \) by (PO2) for \( \preceq \). If \( (x, y) \) is new and \( (y, x) \) old, then \( b \preceq y \preceq x \preceq a \), so \( b \preceq a \) by (PO3), which incomparability excludes. If \( (x, y) \) is old and \( (y, x) \) new, then \( b \preceq x \preceq y \preceq a \), excluded in the same way. If both are new, then \( b \preceq x \) (from \( (y, x) \)) and \( x \preceq a \) (from \( (x, y) \)), so again \( b \preceq a \). Only the first case can occur, and it gives \( x = y \).

(PO3): let \( x \mathrel{R} y \) and \( y \mathrel{R} z \). If both pairs are old, \( x \preceq z \) by (PO3). If \( (x, y) \) is old and \( (y, z) \) new, then \( x \preceq y \preceq a \) and \( b \preceq z \), so \( (x, z) \) is new. If \( (x, y) \) is new and \( (y, z) \) old, then \( x \preceq a \) and \( b \preceq y \preceq z \), so \( (x, z) \) is new. If both are new, \( x \preceq a \) and \( b \preceq z \) directly. In every case \( x \mathrel{R} z \).
:::

::: {.check}
Apply @lem-one-step-order-extension to \( \subseteq \) on \( \powerset{\{1, 2\}} \) with \( a = \{1\} \) and \( b = \{2\} \). Which pairs does \( R \) add to \( \subseteq \)?
:::

::: {.solution}
A new pair \( (x, y) \) needs \( x \subseteq \{1\} \) and \( \{2\} \subseteq y \): \( x \in \{ \emptyset, \{1\} \} \) and \( y \in \{ \{2\}, \{1, 2\} \} \). Of these four pairs, all but \( (\{1\}, \{2\}) \) already belong to \( \subseteq \). So \( R \) adds exactly one pair, and it is the total order \( \emptyset, \{1\}, \{2\}, \{1, 2\} \).
:::

The lemma adds one comparison. The template adds them all at once.

::: {#thm-order-extension}
[Every Partial Order Extends to a Total Order]

Let \( \preceq \) be a partial order on a set \( X \). Then there is a total order \( T \) on \( X \) with \( {\preceq} \subseteq T \).
:::

This book's word is "total" (@def-partial-order); "linear order" is a common synonym, and \( T \) is then called a linear extension of \( \preceq \).

::: {.idea}
By the method of @exm-method-maximality. The partial objects are the partial orders on \( X \) containing \( \preceq \). The union of a chain of them is one, since (PO2) and (PO3) each mention two pairs. A maximal one is total, because @lem-one-step-order-extension enlarges any partial order that has an incomparable pair.
:::

::: {.proof}
Let \( P \) be the set of partial orders \( R \) on \( X \) with \( {\preceq} \subseteq R \), a set of subsets of \( X \times X \), ordered by \( \subseteq \). Then \( {\preceq} \in P \), so \( P \ne \emptyset \).

Let \( \sC \subseteq P \) be a non-empty chain and \( H \coloneqq \bigcup \sC \subseteq X \times X \). Since \( \sC \) has a member, and that member contains \( \preceq \), so does \( H \); in particular (PO1) holds for \( H \). If \( (x, y), (y, x) \in H \), some single \( R_0 \in \sC \) contains both (@lem-chain-union (b)), so \( x = y \) by (PO2) for \( R_0 \). If \( (x, y), (y, z) \in H \), some \( R_0 \in \sC \) contains both, so \( (x, z) \in R_0 \subseteq H \) by (PO3) for \( R_0 \). Hence \( H \in P \), and it is an upper bound of \( \sC \).

By @thm-zorn, \( P \) has a maximal element \( T \). Suppose \( T \) is not total, and let \( a, b \in X \) be incomparable for \( T \). By @lem-one-step-order-extension, applied to \( T \), there is a partial order \( R \) on \( X \) with \( T \subseteq R \) and \( T \ne R \). Since \( {\preceq} \subseteq T \subseteq R \), \( R \in P \), contradicting the maximality of \( T \). So \( T \) is total.
:::

::: {.warning}
**One comparison at a time.** It is tempting to skip Zorn's lemma and settle every incomparable pair at once, each in some direction. That can fail. Take equality on \( X = \{1, 2, 3\} \), where no two different elements are comparable, and decide the three pairs as \( 1 \) before \( 2 \), \( 2 \) before \( 3 \), \( 3 \) before \( 1 \). Each decision alone is harmless, but together they break transitivity, and adding the pairs that transitivity demands puts \( 1 \) before \( 3 \) and \( 3 \) before \( 1 \), against (PO2). @lem-one-step-order-extension adds one comparison and then passes the consequences along; the next comparison is made in the new order, where the earlier ones are already visible. The template is what turns this one-step move into a total order when the pairs cannot be listed.
:::

Sometimes no Zorn is needed, because a formula gives the extension.

::: {#exm-divisibility-linear-extension}
[A total order containing divisibility]

On \( \nN \), let \( x \sqsubseteq y \) mean: \( y = 0 \), or \( x \ne 0 \) and \( x \le y \). Show that \( \sqsubseteq \) is a total order on \( \nN \) containing \( \mid \), and that \( \le \) does not contain \( \mid \).
:::

::: {.solution}
In words, \( \sqsubseteq \) is the usual order on the positive integers with \( 0 \) moved to the top.

(PO1): if \( x = 0 \), then \( x \sqsubseteq x \) by the first alternative; otherwise \( x \le x \).

*Total:* let \( x, y \in \nN \). If \( y = 0 \), then \( x \sqsubseteq y \); if \( x = 0 \), then \( y \sqsubseteq x \); if both are non-zero, \( x \le y \) or \( y \le x \), by totality of \( \le \).

(PO2): let \( x \sqsubseteq y \) and \( y \sqsubseteq x \). If \( y = 0 \), then \( y \sqsubseteq x \) cannot hold by the second alternative, which needs \( y \ne 0 \); so \( x = 0 = y \). The case \( x = 0 \) is the same with the roles exchanged. If both are non-zero, \( x \le y \le x \), so \( x = y \).

(PO3): let \( x \sqsubseteq y \) and \( y \sqsubseteq z \). If \( z = 0 \), then \( x \sqsubseteq z \). Otherwise the second alternative holds for \( (y, z) \): \( y \ne 0 \) and \( y \le z \). Then \( x \sqsubseteq y \) with \( y \ne 0 \) also holds by the second alternative: \( x \ne 0 \) and \( x \le y \). So \( x \le z \), and \( x \sqsubseteq z \).

*Contains \( \mid \):* let \( a, b \in \nN \) with \( a \mid b \), say \( b = ka \) with \( k \in \nZ \) (@def-divides). If \( b = 0 \), then \( a \sqsubseteq b \). If \( b \ne 0 \), then \( a \ne 0 \), since \( 0 \mid b \) would mean \( b = k \cdot 0 = 0 \). With \( a, b > 0 \), \( k > 0 \), so \( k \ge 1 \) and \( b = ka \ge a \): \( a \sqsubseteq b \).

*\( \le \) does not contain \( \mid \):* \( 2 \mid 0 \), since \( 0 = 0 \cdot 2 \), but \( 2 \le 0 \) fails.
:::

Where a formula exists, it is the better proof. @thm-order-extension matters for orders such as \( \subseteq \) on \( \powerset{\nR} \), for which no formula for a total extension is known.

::: {.check}
Put \( 0, 1, 4, 6, 12 \) in \( \sqsubseteq \)-order. Which two of them are comparable under \( \sqsubseteq \) but not under \( \mid \)?
:::

::: {.solution}
\( 1 \sqsubseteq 4 \sqsubseteq 6 \sqsubseteq 12 \sqsubseteq 0 \). Every pair is comparable under \( \sqsubseteq \), which is total. Under \( \mid \): \( 1 \) divides all of them, all of them divide \( 0 \), \( 4 \mid 12 \) and \( 6 \mid 12 \). The remaining pair is \( 4 \), \( 6 \): \( 4 \sqsubseteq 6 \), but neither divides the other. So \( 4 \) and \( 6 \) are the only such pair.
:::

The four uses of the template on the main line of this chapter, side by side:

| Object | Partial objects | Why unions of chains stay partial objects | Why a maximal one is complete |
|---|---|---|---|
| choice function (@thm-choice-from-zorn) | graphs defined on part of \( I \) | (C1), (C2) mention at most two pairs | a missed index can be added |
| representatives (@exm-zorn-representatives) | sets meeting each class at most once | the condition mentions two elements | a missed class can be added |
| injection (@thm-cardinal-comparability) | partial matchings | (M1), (M2) mention two pairs | if both sides have an unpaired element, they can be paired |
| total order (@thm-order-extension) | partial orders containing \( \preceq \) | (PO2), (PO3) mention two pairs | an incomparable pair can be compared (@lem-one-step-order-extension) |

## Optional: every vector space has a basis

Nothing later in the book depends on this subsection. For a reader who has met vector spaces, it sketches, without proving here, how *Linear Algebra*, Section 1.8 uses the same template.

A basis of a vector space \( V \) is a linearly independent set of vectors that spans \( V \). The theorem there is that every linearly independent set \( S \subseteq V \) lies in a basis. In the language of @exm-method-maximality, the partial objects are the linearly independent sets containing \( S \), ordered by \( \subseteq \); \( S \) itself is one. Independence is a condition on finitely many vectors at a time: a set is independent when no finite non-trivial combination of its vectors is \( 0 \). So a dependence among vectors of the union of a chain involves finitely many vectors, which lie in one member of the chain (@lem-chain-union (b)), and that member is independent: the union is a partial object. Zorn's lemma gives a maximal independent set \( M \). It spans \( V \), since a vector outside its span could be added to \( M \) without creating a dependence, giving a strictly larger partial object. With \( S = \emptyset \), every vector space has a basis, including \( \nR \) as a vector space over \( \nQ \), where no basis can be written down.

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

::: {#exr-using-zorn-b1}
[B1: Name the move, then complete it]

Let \( R \) be a relation from \( A \) to \( B \) whose domain is \( A \) (@def-relation). Prove that there is a function \( f \colon A \to B \) whose graph is contained in \( R \).

Below, the proof is started; the second half is blank. *Name the move, then complete it.*

> Let \( P \) be the set of \( G \subseteq R \) such that each \( a \in A \) occurs in at most one pair of \( G \), ordered by \( \subseteq \). Then \( \emptyset \in P \).
> \( \underline{\hspace{8em}} \)
> Hence the graph of \( f \) is contained in \( R \).
:::

::: {.solution}
The move is the maximality template, @exm-method-maximality; steps (2) to (4) remain.

*Completion.* Let \( \sC \subseteq P \) be a non-empty chain. Its union lies in \( R \), and two pairs of the union lie in one member of \( \sC \) (@lem-chain-union (b)), so an element of \( A \) occurs in at most one pair of the union. The union is in \( P \) and is an upper bound of \( \sC \). By @thm-zorn, \( P \) has a maximal element \( M \). Suppose some \( a_0 \in A \) occurs in no pair of \( M \). Since \( a_0 \) is in the domain of \( R \), there is \( b_0 \) with \( (a_0, b_0) \in R \) (one use of \( \rulename{\exists E} \)). Then \( M \cup \{ (a_0, b_0) \} \subseteq R \), \( a_0 \) occurs in it once, and it is strictly larger than \( M \): a contradiction with maximality. So each \( a \in A \) occurs in exactly one pair of \( M \), and \( M \) is the graph of a function \( f \colon A \to B \) (@def-function), with \( M \subseteq R \).
:::

::: {#exr-using-zorn-b2}
[B2: A total order on the subsets of a three-element set]

::: {.enumerate options="label=(\alph*)"}
1. Write the eight subsets of \( \{1, 2, 3\} \) in a list such that \( A \subsetneq B \) always puts \( A \) before \( B \), and prove that it does.
2. How many total orders on \( \powerset{\{1, 2\}} \) contain \( \subseteq \)?
:::
:::

::: {.solution}
(a) \( \emptyset, \{1\}, \{2\}, \{3\}, \{1, 2\}, \{1, 3\}, \{2, 3\}, \{1, 2, 3\} \). The list is arranged by the number of elements. If \( A \subsetneq B \), then \( A \) has fewer elements than \( B \) (@prp-subset-finite), so \( A \) comes in an earlier block of the list.

(b) Two. The empty set must come first, since \( \emptyset \subseteq Y \) for every \( Y \), and \( \{1, 2\} \) last, since every \( Y \subseteq \{1, 2\} \). The sets \( \{1\} \) and \( \{2\} \) are incomparable under \( \subseteq \), so they may come in either order, and both orders work.
:::

::: {#exr-using-zorn-b3}
[B3: A total order on the plane]

On \( \nR^2 \), let \( (x_1, x_2) \le_p (y_1, y_2) \) mean \( x_1 \le y_1 \) and \( x_2 \le y_2 \); and let \( (x_1, x_2) \le_l (y_1, y_2) \) mean \( x_1 < y_1 \), or \( x_1 = y_1 \) and \( x_2 \le y_2 \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \le_p \) is a partial order and not total.
2. Show that \( \le_l \) is a total order containing \( \le_p \).
:::
:::

::: {.solution}
(a) (PO1), (PO2) and (PO3) for \( \le_p \) hold coordinate by coordinate, from the same properties of \( \le \) on \( \nR \); for (PO2), \( x_1 = y_1 \) and \( x_2 = y_2 \) give equal pairs. The points \( (0, 1) \) and \( (1, 0) \) are incomparable: \( 0 \le 1 \) but \( 1 \not\le 0 \) in the second coordinate, and the reverse in the first.

(b) That \( \le_l \) is a total order is the argument of Section 4.3, Exercises A1 (d) and C1 (a), with \( \nR \) in place of \( \nN \): it uses only trichotomy and transitivity of \( \le \). Containment: if \( x_1 \le y_1 \) and \( x_2 \le y_2 \), then either \( x_1 < y_1 \), or \( x_1 = y_1 \) and \( x_2 \le y_2 \); in both cases \( (x_1, x_2) \le_l (y_1, y_2) \).
:::

### C. Going deeper

::: {#exr-using-zorn-c1}
[C1: Exit check: an order is the intersection of its total extensions]

Let \( \preceq \) be a partial order on a set \( X \), and let \( \sT \) be the set of total orders on \( X \) that contain \( \preceq \). Prove that \( {\preceq} = \bigcap \sT \).
:::

::: {.solution}
[Hint 1]

For a pair \( (a, b) \) not in \( \preceq \), you need one \( T \in \sT \) without it. If \( a \) and \( b \) are incomparable, find a partial order containing \( \preceq \) and the pair \( (b, a) \).
:::

::: {.solution}
By @thm-order-extension, \( \sT \ne \emptyset \), so the intersection is defined, and \( {\preceq} \subseteq \bigcap \sT \) since every \( T \in \sT \) contains \( \preceq \).

Let \( (a, b) \in X \times X \) with \( (a, b) \notin {\preceq} \). Then \( a \ne b \) by (PO1). Since \( a \preceq b \) fails, either \( b \preceq a \) or \( a \) and \( b \) are incomparable.

*Case \( b \preceq a \).* Every \( T \in \sT \) contains \( (b, a) \). If it also contained \( (a, b) \), then \( a = b \) by (PO2) for \( T \). So no \( T \in \sT \) contains \( (a, b) \), and since \( \sT \ne \emptyset \), \( (a, b) \notin \bigcap \sT \).

*Case \( a \), \( b \) incomparable.* @lem-one-step-order-extension, with \( b \), \( a \) in place of \( a \), \( b \), gives a partial order \( R \supseteq {\preceq} \) with \( (b, a) \in R \). @thm-order-extension applied to \( R \) gives a total order \( T \supseteq R \). Then \( T \in \sT \) and \( (b, a) \in T \), so \( (a, b) \notin T \) by (PO2), as \( a \ne b \). Hence \( (a, b) \notin \bigcap \sT \).

In both cases \( (a, b) \notin \bigcap \sT \), so \( \bigcap \sT \subseteq {\preceq} \).

**Marking scheme.** (10 points)
- 1: \( \sT \ne \emptyset \), cited from @thm-order-extension.
- 1: \( {\preceq} \subseteq \bigcap \sT \).
- 2: the two cases are exhaustive, because \( a \preceq b \) fails.
- 2: the case \( b \preceq a \), with (PO2) and \( a \ne b \).
- 2: a partial order containing \( \preceq \) and \( (b, a) \) (for example, the lemma with \( a \) and \( b \) exchanged).
- 2: the extension of \( R \) to a total order and the conclusion.
Fatal error (0 for the case concerned): applying the lemma to \( (a, b) \) unexchanged, which puts \( (a, b) \) into the extension instead of keeping it out.
:::

::: {#exr-using-zorn-c2}
[C2: Find the error]

Claim: any two sets are comparable. "Proof": If \( A \) or \( B \) is empty, the empty function is an injection. Otherwise choose \( a_0 \in A \) and \( b_0 \in B \) and pair them. Choose \( a_1 \in A \setminus \{a_0\} \) and \( b_1 \in B \setminus \{b_0\} \), and so on. When one set runs out, the pairs so far are an injection from it into the other.

Is the conclusion true? Does the argument prove it?
:::

::: {.solution}
The conclusion is true: it is @thm-cardinal-comparability. The argument does not prove it. It fails at "and so on … when one set runs out", the gap that (N13) of @fd1:exm-not-allowed-catalogue flags: an "and so on" needs its step, and here the process has no last step in general. Indexed by \( \nN \), it uses a countable set of elements of each side (@prp-countable-image), and for \( A = B = \nR \) neither side runs out, since \( \nR \) is uncountable (@thm-reals-uncountable-decimal). That is a counterexample to the step "the process ends". The argument also makes infinitely many choices with no rule (Section 3.2). The repair is the proof by the template, in which "cannot be continued" replaces "runs out".

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

(b) Let \( P \) be a non-empty partially ordered set in which every non-empty chain has an upper bound. The empty set is a chain, so by Section 5.1, Exercise B1 (@exr-chains-and-zorn-b1) with \( C_0 = \emptyset \), \( P \) has a maximal chain \( C \). It is not empty: for \( p \in P \), \( \{p\} \) is a chain properly containing \( \emptyset \). So \( C \) has an upper bound \( u \), and \( u \) is a maximal element of \( P \) by (a). Since Exercise B1 was proved from Zorn's lemma, the two statements are equivalent.

**Marking scheme.** (10 points)
- 1: \( u \in C \) in (a).
- 1: \( u \) is the greatest element of \( C \).
- 3: \( u \) is maximal in \( X \), using (PO2).
- 2: a maximal chain \( C \) from Exercise B1 with \( C_0 = \emptyset \).
- 1: \( C \ne \emptyset \).
- 2: an upper bound of \( C \), and the conclusion.
:::

::: {#exr-using-zorn-r3}
[R3: The basis theorem, read as a template]

This item is optional and goes with the optional subsection. A set of vectors is linearly independent when no finite non-trivial combination of its vectors is \( 0 \).

::: {.enumerate options="label=(\alph*)"}
1. Which of the template's four steps uses that independence is tested on finitely many vectors at a time?
2. Why would the template fail for the property "\( S \) is a finite independent set"?
3. A maximal element of a partial order need not be greatest. What does this say about bases?
:::
:::

::: {.solution}
(a) Step (2), the chains: a dependence among vectors of the union of a chain involves finitely many vectors, all in one member (@lem-chain-union (b)), and that member is independent.

(b) The union of a chain of finite sets need not be finite (the second warning of Section 5.1), so step (2) fails: the union need not be a partial object.

(c) This is the point of @exm-maximal-not-greatest. Maximal independent sets need not contain one another, so a vector space can have many bases, none of them greatest. In \( \nR^2 \), \( \{ (1, 0), (1, 1) \} \) and \( \{ (2, 0), (0, 3) \} \) are both bases, and neither contains the other.
:::

<!-- dependency ledger
thm-cardinal-comparability (proof): P is a set of subsets of A x B; inclusion is a partial order on it | power set and set-builder (F2.1); inclusion on a set of sets as in 5.1 before lem-chain-union
thm-cardinal-comparability (proof): two pairs of a union of a chain lie in one member | lem-chain-union (b) (cited, F2.4 §01)
thm-cardinal-comparability (proof): maximal element | thm-zorn (cited; stated without proof, F2.4 §01; proved in ST.4 (promised))
thm-cardinal-comparability (proof): graph of a function; inverse relation | def-function, def-relation (cited, F2.1)
thm-cardinal-comparability (claim): (Quick check) six maximal matchings of {1,2,3} and {x,y}; none pairs all of A | cor-pigeonhole-finite-sets (a) (cited); verify/ch05/thm-cardinal-comparability.py
cor-cardinal-trichotomy (proof): symmetry of equinumerosity; injections both ways | prp-equinumerous-properties (b), thm-schroder-bernstein, def-card-le (cited)
cor-cardinal-trichotomy (claim): comparability equivalent to choice | ST.4 (prose pointer; nothing depends on it)
thm-order-extension (claim): worked schedule: generated order has 11 pairs; two schedules; seven in all | finite check; verify/ch05/thm-order-extension.py
lem-one-step-order-extension (proof): all cases of (PO2), (PO3) | inline; verify/ch05/lem-one-step-order-extension.py (all partial orders on 4 points)
lem-one-step-order-extension (claim): (Quick check) R on P({1,2}) adds only ({1},{2}) | verify/ch05/lem-one-step-order-extension.py
thm-order-extension (proof): union of a chain of partial orders is one; maximal is total | lem-chain-union (b), thm-zorn, lem-one-step-order-extension (cited)
exm-divisibility-linear-extension (solution): totality and trichotomy of <= on N; a, b > 0 and b = ka give k > 0, k >= 1, b >= a | R order and arithmetic (school facts; axioms in AN1.1); def-divides (cited); verify/ch05/exm-divisibility-linear-extension.py
exm-divisibility-linear-extension (claim): (Quick check) order 1, 4, 6, 12, 0; only 4, 6 incomparable under divisibility | verify/ch05/exm-divisibility-linear-extension.py
exm-divisibility-linear-extension (claim): no formula for a total extension of inclusion on P(R) is known | prose remark (nothing depends on it)
exm-divisibility-linear-extension (claim): (optional subsection) basis theorem, R over Q has no explicit basis | LA §1.8 thm-basis-extension-general (prose pointer; nothing depends on it)
exr-using-zorn-b2 (solution): proper subset of a finite set has fewer elements; two total extensions on P({1,2}) | prp-subset-finite (cited); verify/ch05/exr-using-zorn-b2.py
exr-using-zorn-b3 (solution): lexicographic order total | Section 4.3 Exercises A1 (d), C1 (a) (cited), with R for N; R order (school fact)
exr-using-zorn-c1 (solution): extension of R; exchanged lemma | thm-order-extension, lem-one-step-order-extension (cited); verify/ch05/lem-one-step-order-extension.py (intersection check on 4 points)
exr-using-zorn-c2 (solution): N-indexed process uses countably many elements; R uncountable | prp-countable-image, thm-reals-uncountable-decimal (cited); fd1:exm-not-allowed-catalogue (N13)
exr-using-zorn-r1 (solution): injection gives surjection back | prp-card-le-surjection (cited)
exr-using-zorn-r2 (solution): maximal chain from a given chain | exr-chains-and-zorn-b1 (F2.4 §01, cited)
exr-using-zorn-r3 (solution): bases of R^2 | linear algebra (optional item; prose only; nothing depends on it)
-->
