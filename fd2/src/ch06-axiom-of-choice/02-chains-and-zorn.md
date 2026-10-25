# Zorn's Lemma and How to Use It

Section 4.4 proved that injections both ways give a bijection, and left open whether, for any two sets, at least one injection exists. Section 5.3 ended with a question about partially ordered sets: if every chain has an upper bound, must there be a maximal element? One principle answers both. This section states it, Zorn's lemma, which answers the second question; says why this volume does not prove it; turns it into a method of proof, the maximality template; and runs the template twice, for a set of representatives and for a total order containing a given partial order. Section 6.3 runs it on the first question, and on the axiom of choice itself.

## Matching two sets, one pair at a time

Let \( A \) and \( B \) be sets, and suppose we want an injection from one of them into the other, in either direction. A natural plan is to **match** elements in pairs. Pick \( a_0 \in A \) and \( b_0 \in B \) and pair them. Then pick \( a_1 \in A \setminus \{a_0\} \) and \( b_1 \in B \setminus \{b_0\} \) and pair those. Continue until one side is used up. If \( A \) runs out first, every element of \( A \) has a partner, different elements have different partners, and the pairs form the graph of an injection \( A \to B \). If \( B \) runs out first, the same pairs read backwards form an injection \( B \to A \).

For finite sets the plan works, because each step uses one more element of each side, and a finite set is used up after as many steps as it has elements (Section 4.1). Take \( A = \{1, 2, 3\} \) and \( B = \{x, y\} \). Pair \( 1 \) with \( x \), then \( 2 \) with \( y \). Now \( B \) is used up, and reading the pairs backwards gives \( x \mapsto 1 \), \( y \mapsto 2 \), an injection \( B \to A \).

For \( A = B = \nR \) the plan breaks down. Suppose we have made one step for each natural number. The elements of \( A \) used so far are \( a_0, a_1, a_2, \dots \), the image of the function \( n \mapsto a_n \) on \( \nN \), so they form a countable set (@prp-countable-image). But \( \nR \) is uncountable (@thm-reals-uncountable-decimal), so \( A \) is not used up; neither is \( B \). The instruction "continue until one side is used up" has no last step, and the words "and so on" stand in for a step that is never stated: (N13) of @fd1:exm-not-allowed-catalogue, "an 'and so on' needs its step". (The infinitely many unnamed choices of \( a_n \) and \( b_n \) are a second problem, the one Section 6.1 met.)

Still, the attempt gets two things right, and they are the thesis of this section:

*Every unfinished matching can be enlarged by one more pair, and a growing family of matchings, put together, is again a matching.*

The first half is plain: if neither side is used up, an unused \( a \) and an unused \( b \) make one more pair. The rest of the section makes "growing family" exact and supplies a principle that turns these two facts into a finished matching. We return to the matching in Section 6.3.

## Chains

Look at the matchings the plan produces, each a set of pairs. Of any two of them, one was built from the other by adding pairs, so one is a subset of the other: under \( \subseteq \), any two are comparable. That is what "growing family" means, and it makes sense in any partially ordered set.

::: {#def-chain}
[Chain]

Let \( (X, \preceq) \) be a partially ordered set. A subset \( C \subseteq X \) is a **chain** if **any two** elements of \( C \) are comparable: for all \( x, y \in C \), \( x \preceq y \) or \( y \preceq x \).
:::

So a chain is a subset on which \( \preceq \) is total (@def-partial-order); in a totally ordered set, every subset is a chain.

**Examples.**

- In \( (\nN, \mid) \), the set \( \{1, 2, 4, 8, \dots\} = \{ 2^n : n \in \nN \} \) is a chain: for \( m \le n \), \( 2^n = 2^{n-m} \cdot 2^m \), so \( 2^m \mid 2^n \). The set \( \{2, 3\} \) is not, since \( 2 \nmid 3 \) and \( 3 \nmid 2 \).
- In \( (\powerset{\{1, 2, 3\}}, \subseteq) \), the set \( \{ \emptyset, \{2\}, \{2, 3\} \} \) is a chain.
- Degenerate cases: \( \emptyset \) is a chain, vacuously, and so is every one-element set \( \{x\} \), by (PO1).

::: {.check}
Decide: (a) Is \( \{ \{1\}, \{1, 2\}, \{3\} \} \) a chain in \( (\powerset{\{1, 2, 3\}}, \subseteq) \)? (b) Is \( \{0, 1, 5, 25\} \) a chain in \( (\nN, \mid) \)? (c) Is \( \{3, 6, 0\} \)? (d) In \( (\nR, \le) \), which subsets are chains?
:::

::: {.solution}
(a) No: \( \{1, 2\} \not\subseteq \{3\} \) and \( \{3\} \not\subseteq \{1, 2\} \).

(b) Yes. \( 1 \) divides every natural number, \( 25 = 5 \cdot 5 \), and every natural number \( a \) divides \( 0 = 0 \cdot a \); so any two of the four are comparable.

(c) Yes: \( 6 = 2 \cdot 3 \), and \( 3 \mid 0 \), \( 6 \mid 0 \).

(d) All of them, since \( \le \) is total on \( \nR \).
:::

Why do chains matter for the matching? Take two pairs from the union of a growing family of matchings. Each pair comes from some matching of the family, and the two matchings are comparable, so both pairs lie in the larger of the two. Any condition that speaks about two pairs at a time can then be checked inside one matching. The same works for any finite number of elements, and that is the content of the next lemma.

The lemma speaks about a set of sets ordered by \( \subseteq \). That is always a partially ordered set: each member of a set of sets \( \sS \) is a subset of \( \bigcup \sS \), and \( \subseteq \) is a partial order on \( \powerset{\bigcup \sS} \) (@exm-subset-order-not-total), which stays one when restricted to the subset \( \sS \), since (PO1)–(PO3) are statements about all elements.

::: {#lem-chain-union}
[Finitely Many Members of a Chain]

::: {.enumerate options="label=(\alph*)"}
1. Let \( C \) be a chain in a partially ordered set \( (X, \preceq) \), let \( n \ge 1 \) and \( x_1, \dots, x_n \in C \). Then some \( x_k \) satisfies \( x_j \preceq x_k \) for \( j = 1, \dots, n \).
2. Let \( \sS \) be a set of sets, partially ordered by \( \subseteq \), and \( \sC \subseteq \sS \) a chain. Then \( C \subseteq \bigcup \sC \) for every \( C \in \sC \); and if \( n \ge 1 \) and \( z_1, \dots, z_n \in \bigcup \sC \), then some single \( C \in \sC \) contains all of \( z_1, \dots, z_n \).
:::
:::

::: {.proof}
*(a)* By induction on \( n \) (@thm-induction with \( n_0 = 1 \)). For \( n = 1 \), take \( k = 1 \): \( x_1 \preceq x_1 \) by (PO1). For the step, let \( x_1, \dots, x_{n+1} \in C \), and by the induction hypothesis let \( x_k \) with \( k \le n \) be above \( x_1, \dots, x_n \). Since \( C \) is a chain, \( x_{n+1} \preceq x_k \) or \( x_k \preceq x_{n+1} \). In the first case \( x_k \) is above all \( n + 1 \) elements. In the second, \( x_{n+1} \) is: \( x_j \preceq x_k \preceq x_{n+1} \) gives \( x_j \preceq x_{n+1} \) by (PO3) for \( j \le n \), and \( x_{n+1} \preceq x_{n+1} \) by (PO1).

*(b)* The first claim is the definition of the union. For the second, induct on \( n \) (@thm-induction with \( n_0 = 1 \)). For \( n = 1 \): \( z_1 \in \bigcup \sC \) means that \( z_1 \in C \) for some \( C \in \sC \), and one use of \( \rulename{\exists E} \) (@fd1:def-rules-existential) names such a \( C \). For the step, by the induction hypothesis some \( C' \in \sC \) contains \( z_1, \dots, z_n \), and one use of \( \rulename{\exists E} \) gives \( C'' \in \sC \) with \( z_{n+1} \in C'' \). Since \( \sC \) is a chain, \( C' \subseteq C'' \) or \( C'' \subseteq C' \), and the larger of the two contains all of \( z_1, \dots, z_{n+1} \).
:::

Each step of the induction in (b) makes one use of \( \rulename{\exists E} \), so no choice is involved. Writing "use \( \rulename{\exists E} \) \( n \) times" instead would be the "and so on" that (N13) flags; the induction is what supplies its step.

::: {.check}
(a) Is there a chain of subsets of \( \nN \), none of whose members contains both \( 0 \) and \( 1 \), whose union contains both? (b) Is there such a family of subsets that is not a chain?
:::

::: {.solution}
(a) No. If \( 0 \) and \( 1 \) lie in the union of a chain, then by @lem-chain-union (b) with \( n = 2 \) some member contains both.

(b) Yes: \( \{ \{0\}, \{1\} \} \) has union \( \{0, 1\} \), and neither member contains both. This is exactly what "chain" rules out.
:::

## Zorn's lemma

Return to the question of Section 5.3: in a partially ordered set in which every chain has an upper bound, is there a maximal element? A naive attempt: start at any \( p_0 \). If \( p_0 \) is not maximal, there is \( p_1 \succ p_0 \); if \( p_1 \) is not maximal, there is \( p_2 \succ p_1 \); and so on. The \( p_n \) form a chain, which has an upper bound \( u \); if \( u \) is not maximal, continue above \( u \), and so on. Each single step is legitimate. But the chain \( p_0 \prec p_1 \prec \cdots \) may have an upper bound that is again not maximal, the next chain may too, and "continue past every such bound" is neither a finite process nor one indexed by \( \nN \). It is (N13) once more: the "and so on" has no step. Instead of a proof, there is a principle, stated as its own result.

::: {#thm-zorn}
[Zorn's Lemma]

Let \( (P, \preceq) \) be a **non-empty** partially ordered set in which **every non-empty chain** has an upper bound in \( P \). Then \( P \) has a maximal element.
:::

We do not prove @thm-zorn. It cannot be proved from the rules of logic and the working rules for sets of Chapter 1 alone: it is equivalent to the axiom of choice (@ax-choice), which, as Section 6.1 records, can be neither proved nor refuted from the other axioms. Section 6.3 proves one half of the equivalence, that Zorn's lemma gives the axiom of choice. The other half, which builds a maximal element from a choice function, needs a recursion longer than any indexed by \( \nN \); *Axiomatic Set Theory*, Chapter 4 proves it. As with the axiom, we use the lemma openly and cite it at each use. Zorn (1935) put the principle in this form, which suits algebra, where the objects to be built are sets ordered by inclusion.

**Why each hypothesis is needed.** Each of three small examples breaks one hypothesis and has no maximal element.

- \( (\nN, \le) \) is non-empty and total, and has no maximal element, since \( n < n + 1 \). The chain hypothesis fails: the chain \( \nN \) has no upper bound in \( \nN \).
- The empty partially ordered set satisfies the chain hypothesis vacuously, since it has no non-empty chain, and it has no maximal element. "Non-empty" is needed.
- The set of finite subsets of \( \nN \), ordered by \( \subseteq \), is non-empty, as \( \emptyset \) belongs to it, and has no maximal element. For finite \( F \), \( \nN \) is not a subset of \( F \), since a subset of a finite set is finite (@prp-subset-finite) and \( \nN \) is infinite (@exm-hilbert-hotel); for \( m \in \nN \setminus F \), the set \( F \cup \{m\} \) is finite (@prp-disjoint-union-count) and strictly larger. By the contrapositive of Zorn's lemma, some non-empty chain has no upper bound in this set, and here one is visible: \( \{ \{0, 1, \dots, n - 1\} : n \in \nN \} \), that is, \( \emptyset, \{0\}, \{0, 1\}, \dots \). An upper bound would be a finite set containing every natural number, hence containing \( \nN \), which is impossible.

::: {.warning}
**Maximal, not greatest, and not unique.** Zorn's lemma produces **a** maximal element, by no formula, and says nothing about how many there are. By @prp-greatest-maximal a greatest element would be maximal, but the converse fails (@exm-maximal-not-greatest). In the applications below there are usually many maximal objects and no greatest one; a proof that treats "the" maximal element as unique, or as above everything, has gone wrong.
:::

::: {.check}
Let \( P = \{ \{1\}, \{2\}, \{1, 3\} \} \), ordered by \( \subseteq \). List the chains with at least two elements; check that every non-empty chain has an upper bound in \( P \); name the maximal elements.
:::

::: {.solution}
The only comparable pair of different elements is \( \{1\} \subseteq \{1, 3\} \), so the only chain with at least two elements is \( \{ \{1\}, \{1, 3\} \} \), with upper bound \( \{1, 3\} \). A one-element chain \( \{p\} \) has the upper bound \( p \). The maximal elements are \( \{2\} \) and \( \{1, 3\} \): two of them, as the warning says, and no greatest element.
:::

::: {.remark}
[Every chain, or every non-empty chain]

Some books ask for an upper bound of **every** chain, the empty one included. An upper bound of \( \emptyset \) is any element of \( P \) (@def-order-bounds), so that form contains "\( P \ne \emptyset \)" as a special case. The two forms say the same thing.
:::

## The maximality template

Zorn's lemma is almost always used in one pattern.

::: {#exm-method-maximality}
[Method: the maximality template]

**Template.** To show that a complete object exists: (1) **partial objects:** let \( P \) be the set of partial objects, of which the complete ones are the finished case, ordered by \( \subseteq \) (extension); check \( P \ne \emptyset \), usually with the empty or the given starting object. (2) **chains:** for a non-empty chain \( \sC \subseteq P \), show \( \bigcup \sC \in P \); each defining condition mentions finitely many elements, which lie in one member (@lem-chain-union). (3) **Zorn:** \( P \) has a maximal element \( M \) (@thm-zorn). (4) **complete:** suppose \( M \) is not complete; use the missing piece to build a strictly larger partial object, a contradiction.

**When to use it.** The object can be built piece by piece, each condition on it checks finitely many pieces at a time, and the pieces cannot be listed.

**The usual failure.** The union of a chain is not a partial object, because a condition mentions infinitely many pieces ("finite", "countable"); step (4) builds an object that is not strictly larger, or not in \( P \); and treating \( M \) as the greatest or the only complete object.
:::

Here is its first run.

::: {#exm-zorn-representatives}
[A set of representatives]

Let \( \sim \) be an equivalence relation on a set \( X \). Show that there is a set \( S \subseteq X \) that meets every equivalence class in exactly one element.
:::

::: {.idea}
[Scratch work]

By the method of @exm-method-maximality. A partial object should be a set that meets each class **at most** once, so that the complete ones meet each class exactly once. "At most once" reads: \( s \sim t \) implies \( s = t \), a condition on two elements at a time, so step (2) works. For step (4), a class \( [x] \) that is missed gives the larger set \( S \cup \{x\} \), and no choice is needed, since \( x \) is already in hand. As givens and goal:

| Givens | Goal |
|---|---|
| \( \sim \) an equivalence relation on \( X \) | \( S \subseteq X \) meeting every class in exactly one element |
| \( P \): the \( S \subseteq X \) with \( s \sim t \Rightarrow s = t \) (each class met at most once), ordered by \( \subseteq \) | Zorn's hypotheses: \( P \ne \emptyset \), and every non-empty chain has an upper bound in \( P \) |
| \( \emptyset \in P \); for a chain \( \sC \), try \( \bigcup \sC \): the condition mentions two elements (@lem-chain-union (b)) | a maximal \( M \in P \) meets every class |
| \( M \) maximal; suppose the class \( [x] \) is missed | \( M \cup \{x\} \in P \), strictly larger: a contradiction (@exm-method-choosing-the-form) |

:::

::: {.solution}
Let \( P \) be the set of \( S \subseteq X \) such that for all \( s, t \in S \), \( s \sim t \) implies \( s = t \); order it by \( \subseteq \). Then \( \emptyset \in P \). For a non-empty chain \( \sC \subseteq P \), any two elements \( s, t \) of \( \bigcup \sC \) lie in one member (@lem-chain-union (b)), so \( s \sim t \) gives \( s = t \): \( \bigcup \sC \in P \), an upper bound of \( \sC \). By @thm-zorn, take a maximal \( M \in P \).

Suppose some class \( [x] \) (@def-equivalence-class) contains no element of \( M \). Then \( x \notin M \), since \( x \in [x] \) by (Eq1). And \( M \cup \{x\} \in P \): let \( s, t \in M \cup \{x\} \) with \( s \sim t \). If both lie in \( M \), then \( s = t \). If \( s = x \) and \( t \in M \), then \( t \sim x \) by (Eq2), so \( t \in [x] \cap M \), which is impossible; the case \( t = x \), \( s \in M \) is the same with the letters exchanged; and if \( s = t = x \), there is nothing to show. So \( M \subsetneq M \cup \{x\} \) in \( P \), contradicting maximality. Hence \( M \) meets every class, and by the condition defining \( P \) in at most one element: \( S \coloneqq M \) works.
:::

The axiom of choice gives the same set in one line, by choosing one element from each class; the template's advantage shows when the pieces interact, as in the next subsection. On \( \nR \), the relation \( x \sim y \iff x - y \in \nQ \) is an equivalence relation (Section 5.2, after @exm-reals-mod-integers). A set of representatives for it inside \( [0, 1] \) is a set of real numbers that *Measure, Integration, and Real Analysis*, Chapter 2 shows has no length, and no formula for one is known.

::: {.check}
Let \( X = \nZ \) and \( m \sim n \iff m - n \) is even. Describe the partial objects of @exm-zorn-representatives that have two elements, and the maximal ones.
:::

::: {.solution}
They are the sets \( \{e, o\} \) with \( e \) even and \( o \) odd: two even or two odd integers are related, since their difference is even, so a partial object holds at most one of each parity. Conversely, \( \{e, o\} \) is a partial object: with \( e = 2a \) and \( o = 2b + 1 \), \( e - o = 2(a - b - 1) + 1 \) is odd, hence not even (no integer is both, @thm-even-or-odd), so \( e \not\sim o \). These are exactly the maximal elements, since any third integer has the parity of \( e \) or of \( o \) (every integer is even or odd, @thm-even-or-odd), and \( \emptyset \) and the one-element sets are not maximal, since each lies strictly inside some \( \{e, o\} \). There are many maximal elements, such as \( \{0, 1\} \) and \( \{4, -7\} \), and no greatest one.
:::

::: {.warning}
**Check that the union is a partial object.** Here is an almost-correct proof that \( \nN \) has a maximal finite subset. "Let \( P \) be the set of finite subsets of \( \nN \), ordered by \( \subseteq \). A chain has its union as an upper bound. By Zorn's lemma, \( P \) has a maximal element." The conclusion is false, by the third example after @thm-zorn. The failing line is the second: the union is an upper bound in \( \powerset{\nN} \), but it need not be finite, so it need not lie in \( P \). "Finite" is a condition on all the elements at once, and @lem-chain-union handles only finitely many.
:::

In the next run the pieces interact: one added comparison forces others.

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

Section 6.3 runs the template three times more: on the matching that opened this section, on choice functions, and on well-orders.

## Exercises

### A. Check your understanding

::: {#exr-chains-and-zorn-a2}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Step (4) of @exm-zorn-representatives adds one point \( x \) of a class that \( M \) misses. Why is naming \( x \) a single \( \rulename{\exists E} \), and why does the proof make no other choice, although a set of representatives picks one point from each of possibly infinitely many classes?
2. Run @exm-zorn-representatives when \( \sim \) has a single class, on \( X = \{1, 2, 3\} \): list \( P \), name its maximal elements, and decide whether \( P \) has a greatest element.
3. @lem-one-step-order-extension asks for \( a \), \( b \) incomparable. What goes wrong with \( R \) if \( b \preceq a \) and \( a \ne b \)?
4. Give a partially ordered set that contains an infinite chain, in which every non-empty chain has an upper bound, and which has exactly two maximal elements.
:::
:::

::: {.solution}
(a) \( x \) is one element of one non-empty set, the missed class, named inside the proof by contradiction: one \( \rulename{\exists E} \) (@fd1:def-rules-existential). \( P \) is defined by specification and the union of a chain is defined outright; the maximal \( M \) is named by one \( \rulename{\exists E} \) from the conclusion of @thm-zorn. The one point per class is picked by Zorn's lemma, as \( M \); the proof itself picks nothing more.

(b) A member of \( P \) meets the one class at most once, so it has at most one element, and every set with at most one element qualifies:
\[
P = \bigl\{ \emptyset, \{1\}, \{2\}, \{3\} \bigr\}.
\]
The maximal elements are the three singletons. There is no greatest element: a greatest element would be maximal (@prp-greatest-maximal (a)), so it would be one of the singletons, and it would contain the other two.

(c) The pair \( (a, b) \) is new, since \( a \preceq a \) and \( b \preceq b \). With \( (b, a) \in {\preceq} \subseteq R \), (PO2) for \( R \) would give \( a = b \), which is false; so \( R \) is not a partial order.

(d) Take \( a \coloneqq -1 \) and \( b \coloneqq -2 \), integers not in \( \nN \), and on \( \nN \cup \{a, b\} \) let \( \preceq \) consist of the usual order \( \le \) of \( \nN \), the pairs \( n \preceq a \) and \( n \preceq b \) for all \( n \in \nN \), and \( a \preceq a \), \( b \preceq b \). (PO1)–(PO3) hold: they hold inside \( \nN \), and every other pair ends at \( a \) or \( b \) (for instance \( n \le m \) and \( m \preceq a \) give \( n \preceq a \)). \( \nN \) is an infinite chain. A non-empty chain containing \( a \) does not contain \( b \), since the two are incomparable, so \( a \) bounds it; likewise for \( b \); and a chain inside \( \nN \) is bounded by \( a \). The maximal elements are \( a \) and \( b \); no \( n \) is maximal, since \( n \preceq n + 1 \) and \( n \ne n + 1 \).
:::

### B. Practice

::: {#exr-chains-and-zorn-b1}
[B1: Maximal chains]

Let \( (X, \preceq) \) be a partially ordered set and \( C_0 \subseteq X \) a chain. Prove that there is a chain \( C \supseteq C_0 \) that is **maximal**: no chain contains \( C \) properly.
:::

::: {.solution}
[Hint]

The partial objects are the chains containing \( C_0 \).
:::

::: {.solution}
Let \( P \) be the set of chains \( C \subseteq X \) with \( C_0 \subseteq C \), ordered by \( \subseteq \); then \( C_0 \in P \). Let \( \sK \subseteq P \) be a non-empty chain and \( H \coloneqq \bigcup \sK \). Then \( H \supseteq C_0 \), since \( \sK \) has a member and each member contains \( C_0 \). Any \( x, y \in H \) lie in one member \( K \in \sK \) (@lem-chain-union (b)), which is a chain, so \( x \) and \( y \) are comparable. So \( H \in P \), and it is an upper bound of \( \sK \). By @thm-zorn, \( P \) has a maximal element \( C \). If a chain \( D \supsetneq C \) existed, then \( D \supseteq C_0 \), so \( D \in P \) and \( C \subsetneq D \), contradicting maximality. So \( C \) is a maximal chain containing \( C_0 \).
:::

::: {#exr-chains-and-zorn-b2}
[B2: Name the move, then complete it]

Here is the frame of a proof that for every set \( \sF \) of non-empty sets there is a subfamily \( \sD \subseteq \sF \) of pairwise disjoint sets such that every member of \( \sF \) meets some member of \( \sD \).

> Let \( P \) be the set of subfamilies \( \sE \subseteq \sF \) whose members are pairwise disjoint (\( E \cap E' = \emptyset \) for \( E \ne E' \) in \( \sE \)), ordered by \( \subseteq \). Then \( \emptyset \in P \). For a non-empty chain of such subfamilies, two members \( E \ne E' \) of its union lie in one subfamily of the chain, so \( E \cap E' = \emptyset \); the union lies in \( P \) and is an upper bound. By Zorn's lemma, \( P \) has a maximal element \( \sD \).
>
> \( \vdots \)
>
> … Hence every member of \( \sF \) meets some member of \( \sD \).

*Name the move, then complete it.*
:::

::: {.solution}
The move is step (4) of @exm-method-maximality: a missing piece gives a strictly larger partial object. Suppose \( F \in \sF \) meets no member of \( \sD \). Then \( F \notin \sD \): otherwise \( F \) would meet itself, as \( F \cap F = F \ne \emptyset \). And \( \sD \cup \{F\} \) is pairwise disjoint, since \( F \cap D = \emptyset \) for every \( D \in \sD \) by assumption. So \( \sD \subsetneq \sD \cup \{F\} \in P \), against the maximality of \( \sD \). The check \( F \notin \sD \) is what makes the new family strictly larger, the failure the method box warns about. Hence every member of \( \sF \) meets some member of \( \sD \).
:::

::: {#exr-chains-and-zorn-b4}
[B3: Prove or disprove]

Prove each true statement and refute each false one.

::: {.enumerate options="label=(\alph*)"}
1. If every chain of a non-empty partially ordered set \( P \) has an upper bound in \( P \), then \( P \) has a greatest element.
2. Every non-empty finite partially ordered set has a maximal element.
3. The set of subsets of \( \nN \) that contain no two consecutive numbers, ordered by \( \subseteq \), has a greatest element.
4. If \( P \) is a non-empty partially ordered set in which every non-empty chain has an upper bound, then every \( p \in P \) lies below some maximal element of \( P \).
5. The set of countable subsets of \( \nR \), ordered by \( \subseteq \), has a maximal element.
:::

*Hint for (d): apply Zorn's lemma to the elements above \( p \).*
:::

::: {.solution}
(a) False. Take \( P = \{ \{1\}, \{2\} \} \) under \( \subseteq \). Its chains are \( \emptyset \) (any element of \( P \) bounds it, @def-order-bounds), \( \{\{1\}\} \) and \( \{\{2\}\} \), each with an upper bound in \( P \). But \( P \) has no greatest element, since \( \{1\} \) and \( \{2\} \) are incomparable.

(b) True. Let \( P \) be non-empty and finite, and let \( C \) be a non-empty chain of \( P \). Then \( C \) is finite (@prp-subset-finite); list it as \( x_1, \dots, x_n \) with \( n \ge 1 \). By @lem-chain-union (a), one \( x_k \) is above all of them, an upper bound of \( C \) in \( P \). By @thm-zorn, \( P \) has a maximal element. (Section 5.3, Exercise R4 proves this without Zorn's lemma, by induction.)

(c) False. The set \( E \) of even numbers and the set \( O \) of odd numbers both contain no two consecutive numbers. A greatest element \( G \) would contain \( E \) and \( O \), so \( 0, 1 \in G \), which are consecutive. (In fact \( E \) and \( O \) are both maximal: adding any \( n \notin E \) to \( E \) puts \( n \) and \( n + 1 \) in it (\( n \) is odd by @thm-even-or-odd, so \( n + 1 \) is even), and adding any \( n \notin O \) to \( O \) does the same. So Zorn's lemma, if applied here, gives a maximal element, never a greatest one, as the warning after @thm-zorn says.)

(d) True. Let \( p \in P \), and let \( Q \coloneqq \{ q \in P : p \preceq q \} \), ordered by \( \preceq \); then \( p \in Q \). A non-empty chain \( C \) of \( Q \) is a chain of \( P \), so it has an upper bound \( u \in P \); for any \( c \in C \), \( p \preceq c \preceq u \), so \( u \in Q \) by (PO3). By @thm-zorn, \( Q \) has a maximal element \( m \), and \( p \preceq m \). If \( m \prec q \) for some \( q \in P \), then \( p \preceq q \) by (PO3), so \( q \in Q \), against the maximality of \( m \) in \( Q \). So \( m \) is maximal in \( P \).

(e) False. Let \( C \subseteq \nR \) be countable. Then \( C \ne \nR \), since \( \nR \) is uncountable (@thm-reals-uncountable-decimal); for \( x \in \nR \setminus C \), the set \( C \cup \{x\} \) is countable (@prp-union-two-countable) and strictly larger. So no countable set is maximal. (By the contrapositive of Zorn's lemma, some non-empty chain of countable sets has no countable upper bound; the answer does not need one.)
:::

::: {#exr-using-zorn-b2}
[B4: A total order on the subsets of a three-element set]

::: {.enumerate options="label=(\alph*)"}
1. Write the eight subsets of \( \{1, 2, 3\} \) in a list such that \( A \subsetneq B \) always puts \( A \) before \( B \), and prove that it does.
2. How many total orders on \( \powerset{\{1, 2\}} \) contain \( \subseteq \)?
:::
:::

::: {.solution}
(a) \( \emptyset, \{1\}, \{2\}, \{3\}, \{1, 2\}, \{1, 3\}, \{2, 3\}, \{1, 2, 3\} \). The list is arranged by the number of elements. If \( A \subsetneq B \), then \( A \) has fewer elements than \( B \) (@prp-subset-finite), so \( A \) comes in an earlier block of the list.

(b) Two. The empty set must come first, since \( \emptyset \subseteq Y \) for every \( Y \), and \( \{1, 2\} \) last, since every \( Y \subseteq \{1, 2\} \). The sets \( \{1\} \) and \( \{2\} \) are incomparable under \( \subseteq \), so they may come in either order. In each list \( \emptyset \) comes first and \( \{1, 2\} \) last, so every pair of \( \subseteq \) (the pairs \( (\emptyset, Y) \), \( (Y, \{1, 2\}) \) and \( (Y, Y) \)) appears in list order. A list of the four sets defines a total order, and different lists give different orders, so there are exactly two.
:::

### C. Going deeper

::: {#exr-chains-and-zorn-c1}
[C1: Find the error]

Claim: every chain \( C_0 \) of a partially ordered set \( X \) lies in a maximal chain.

"Proof": Let \( P \) be the set of chains containing \( C_0 \), ordered by \( \subseteq \); then \( C_0 \in P \). Let \( \sK \) be a non-empty chain in \( P \). Every \( K \in \sK \) is a subset of \( \bigcup \sK \), so \( \bigcup \sK \) is an upper bound of \( \sK \). By Zorn's lemma, \( P \) has a maximal element \( C \). A chain containing \( C \) contains \( C_0 \), so it lies in \( P \); hence \( C \) is a maximal chain.

Is the conclusion true? Does the argument prove it?
:::

::: {.solution}
The conclusion is true: it is Exercise B1.

The argument does not prove it. It never checks that \( \bigcup \sK \) lies in \( P \), in particular that it **is a chain** (that it contains \( C_0 \) is immediate, since \( \sK \) is non-empty); the upper bound in @thm-zorn must belong to \( P \). The step's general form, "the union of a chain of partial objects lies in \( P \)", is false: among the finite subsets of \( \nN \), the chain \( \{ \{0, \dots, n - 1\} : n \in \nN \} \) has union \( \nN \), which is not finite (the second warning of this section). Here the conclusion of the step happens to be true, which is exactly why it must be proved, not assumed. The repair is the chain step of B1: two elements of \( \bigcup \sK \) lie in one member \( K \in \sK \) (@lem-chain-union (b)), which is a chain, so they are comparable.

**Marking scheme.** (10 points)
- 2: the conclusion is true, with B1 cited.
- 3: the missing check named: \( \bigcup \sK \in P \).
- 3: explains why the upper bound must belong to \( P \) (Zorn's hypothesis); a counterexample to the general inference "the union of a chain of partial objects lies in \( P \)" is one way to do so.
- 2: the repair via @lem-chain-union.
Fatal errors (0 for the step): calling the conclusion false; "repairing" the proof by assuming that a union of chains is always a chain.
:::

::: {#exr-chains-and-zorn-c2}
[C2: Exit check: when no choice is needed]

::: {.enumerate options="label=(\alph*)"}
1. Let \( \sim \) be an equivalence relation on \( \nN \). Without Zorn's lemma or the axiom of choice, give a set \( S \) meeting every class exactly once, and prove that it does.
2. Do the same for an equivalence relation on a set \( X \) with an injection \( j \colon X \to \nN \).
3. Which ingredient of @exm-zorn-representatives does your answer to (a) make unnecessary, and why?
:::
:::

::: {.solution}
[Hint 1]

Each class is a non-empty set of natural numbers. Which element of it can be named without choosing?
:::

::: {.solution}
(a) Let \( S \coloneqq \{ m_x : x \in \nN \} \), where \( m_x \) is the least element of \( [x] \). It exists by @thm-well-ordering, since \( [x] \subseteq \nN \) contains \( x \) and so is non-empty, and it is unique (@prp-greatest-unique), so the rule names one value. *Every class is met:* \( m_x \in [x] \cap S \). *At most once:* let \( m_x, m_y \in S \) lie in the same class \( [z] \). Then \( m_x \in [x] \cap [z] \), so \( [x] = [z] \), and likewise \( [y] = [z] \), since different classes are disjoint (@thm-classes-partition). So \( [x] = [y] \), these classes have the same least element, and \( m_x = m_y \). Hence \( S \) meets each class \( [x] \) in \( m_x \) and nowhere else.

(b) For \( x \in X \), the set \( j([x]) \subseteq \nN \) is non-empty, so it has a least element \( k_x \) (@thm-well-ordering), and since \( j \) is injective exactly one \( s_x \in [x] \) has \( j(s_x) = k_x \). Let \( S \coloneqq \{ s_x : x \in X \} \). The argument of (a) applies word for word, with \( s_x \) for \( m_x \): equal classes give equal \( k_x \), hence equal \( s_x \).

(c) Zorn's lemma, that is, the whole argument with \( P \), chains and a maximal \( M \): a rule names each representative, so nothing needs to be chosen (@exm-method-name-the-choice).

**Marking scheme.** (10 points)
- 3: (a) each class has a well-defined representative (well-ordering, and the rule names one value).
- 3: (a) every class met, and met at most once (justified).
- 2: (b) the least value of \( j \), and injectivity naming one element.
- 2: (c) Zorn's lemma named as the unnecessary ingredient, because a rule names each representative.
Fatal errors (0 for the step): "choose an element of each class" in (a) or (b), which is the axiom of choice.
:::

::: {#exr-using-zorn-c1}
[C3: Exit check: an order is the intersection of its total extensions]

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

<!-- dependency ledger
lem-chain-union (claim): subset-inclusion restricted to a set of sets is a partial order | inline, by exm-subset-order-not-total and restriction of (PO1)-(PO3)
def-chain (example): 2^n = 2^(n-m) * 2^m for m <= n | school arithmetic
thm-zorn (claim): the set of finite subsets of N is a set | set-builder on P(N) (Chapter 1)
thm-zorn (claim): status paragraph, Zorn's lemma equivalent to ax-choice, which is independent (Section 6.1, ax-choice status remark); converse proved in ST.4; Zorn => AC in F2.4 §03 (prose pointer) | prose pointer to Axiomatic Set Theory and to Section 6.3; nothing depends on it
exm-zorn-representatives (example): a set of representatives for x - y in Q inside [0, 1] has no length | prose pointer to Measure, Integration, and Real Analysis Ch 2 (MT.1); nothing depends on it
exm-zorn-representatives (solution): Quick check, same-parity integers have even difference; every integer is even or odd | arithmetic; thm-even-or-odd
exr-chains-and-zorn-b4 (solution): (a) any element of P bounds the empty chain | def-order-bounds
exr-chains-and-zorn-b4 (solution): (c) n not in E is odd, so n + 1 is even | thm-even-or-odd
exm-zorn-representatives (example): x ~ y iff x - y in Q is an equivalence relation on R | Section 5.2 (after exm-reals-mod-integers)
thm-order-extension (claim): worked schedule: generated order has 11 pairs; two schedules; seven in all | finite check; verify/ch06/thm-order-extension.py
lem-one-step-order-extension (proof): all cases of (PO2), (PO3) | inline; verify/ch06/lem-one-step-order-extension.py (all partial orders on 4 points)
lem-one-step-order-extension (claim): (Quick check) R on P({1,2}) adds only ({1},{2}) | verify/ch06/lem-one-step-order-extension.py
thm-order-extension (proof): union of a chain of partial orders is one; maximal is total | lem-chain-union (b), thm-zorn, lem-one-step-order-extension (cited)
exm-divisibility-linear-extension (solution): totality and trichotomy of <= on N; a, b > 0 and b = ka give k > 0, k >= 1, b >= a | R order and arithmetic (school facts; axioms in AN1.1); def-divides (cited); verify/ch06/exm-divisibility-linear-extension.py
exm-divisibility-linear-extension (claim): (Quick check) order 1, 4, 6, 12, 0; only 4, 6 incomparable under divisibility | verify/ch06/exm-divisibility-linear-extension.py
exm-divisibility-linear-extension (claim): no formula for a total extension of inclusion on P(R) is known | prose remark (nothing depends on it)
exr-using-zorn-b2 (solution): proper subset of a finite set has fewer elements; two total extensions on P({1,2}) | prp-subset-finite (cited); verify/ch06/exr-using-zorn-b2.py
exr-using-zorn-c1 (solution): extension of R; exchanged lemma | thm-order-extension, lem-one-step-order-extension (cited); verify/ch06/lem-one-step-order-extension.py (intersection check on 4 points)
exr-chains-and-zorn-a2 (solution): (b) P = {{}, {1}, {2}, {3}}; three maximal, no greatest | finite check; verify/ch06/exr-chains-and-zorn-a2.py; prp-greatest-maximal (cited)
exr-chains-and-zorn-a2 (solution): (d) the order on N u {a, b} is a partial order, every non-empty chain bounded, exactly a, b maximal | inline (case check on pairs ending at a or b; <= on N, school fact)
-->
