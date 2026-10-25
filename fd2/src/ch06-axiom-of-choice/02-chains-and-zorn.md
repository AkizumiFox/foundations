# Zorn's Lemma and How to Use It

<!-- S3: rewrite per blueprint (6.2: opening frame; thm-choice-from-zorn moved to 6.3; R14; optional basis subsection reduced to exr-using-zorn-r3; layout §1) -->

Section 4.4 proved that injections both ways give a bijection, and left open whether, for any two sets, at least one injection exists. Section 5.3 ended with a question about partially ordered sets: if every chain has an upper bound, must there be a maximal element? One principle answers both questions. This section states it, Zorn's lemma, which answers the second question; explains why this volume does not prove it; and turns it into a method of proof, the maximality template, with two first uses. Section 6.3 uses the template to answer the first question.

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

We do not prove @thm-zorn. It cannot be proved from the rules of logic and the working rules for sets of Chapter 1 alone: it is equivalent to the axiom of choice (@ax-choice), which, as Section 6.1 records, can be neither proved nor refuted from the other axioms. One half of the equivalence, that Zorn's lemma implies the axiom of choice, is the first application below (@thm-choice-from-zorn). The other half, which builds a maximal element from a choice function, is proved in *Axiomatic Set Theory*, Chapter 4, together with the other equivalents. As with the axiom, we use the lemma openly and cite it at each use. Zorn (1935) put the principle in this form, which suits algebra, where the objects to be built are sets ordered by inclusion.

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

Zorn's lemma is almost always used in one pattern. Its first use proves the half of the equivalence with the axiom of choice that this volume can prove.

::: {#exm-method-maximality}
[Method: the maximality template]

**Template.** To show that a complete object exists: (1) **partial objects:** let \( P \) be the set of partial objects, of which the complete ones are the finished case, ordered by \( \subseteq \) (extension); check \( P \ne \emptyset \), usually with the empty or the given starting object. (2) **chains:** for a non-empty chain \( \sC \subseteq P \), show \( \bigcup \sC \in P \); each defining condition mentions finitely many elements, which lie in one member (@lem-chain-union). (3) **Zorn:** \( P \) has a maximal element \( M \) (@thm-zorn). (4) **complete:** suppose \( M \) is not complete; use the missing piece to build a strictly larger partial object, a contradiction.

**When to use it.** The object can be built piece by piece, each condition on it checks finitely many pieces at a time, and the pieces cannot be listed.

**The usual failure.** The union of a chain is not a partial object, because a condition mentions infinitely many pieces ("finite", "countable"); step (4) builds an object that is not strictly larger, or not in \( P \); and treating \( M \) as the greatest or the only complete object.
:::

The second use runs the template with a shorter plan.

::: {#exm-zorn-representatives}
[A set of representatives]

Let \( \sim \) be an equivalence relation on a set \( X \). Show that there is a set \( S \subseteq X \) that meets every equivalence class in exactly one element.
:::

::: {.idea}
[Scratch work]

By the method of @exm-method-maximality. A partial object should be a set that meets each class **at most** once, so that the complete ones meet each class exactly once. "At most once" reads: \( s \sim t \) implies \( s = t \), a condition on two elements at a time, so step (2) works. For step (4), a class \( [x] \) that is missed gives the larger set \( S \cup \{x\} \), and no choice is needed, since \( x \) is already in hand.
:::

::: {.solution}
Let \( P \) be the set of \( S \subseteq X \) such that for all \( s, t \in S \), \( s \sim t \) implies \( s = t \); order it by \( \subseteq \). Then \( \emptyset \in P \). For a non-empty chain \( \sC \subseteq P \), any two elements \( s, t \) of \( \bigcup \sC \) lie in one member (@lem-chain-union (b)), so \( s \sim t \) gives \( s = t \): \( \bigcup \sC \in P \), an upper bound of \( \sC \). By @thm-zorn, take a maximal \( M \in P \).

Suppose some class \( [x] \) (@def-equivalence-class) contains no element of \( M \). Then \( x \notin M \), since \( x \in [x] \) by (Eq1). And \( M \cup \{x\} \in P \): let \( s, t \in M \cup \{x\} \) with \( s \sim t \). If both lie in \( M \), then \( s = t \). If \( s = x \) and \( t \in M \), then \( t \sim x \) by (Eq2), so \( t \in [x] \cap M \), which is impossible; the case \( t = x \), \( s \in M \) is the same with the letters exchanged; and if \( s = t = x \), there is nothing to show. So \( M \subsetneq M \cup \{x\} \) in \( P \), contradicting maximality. Hence \( M \) meets every class, and by the condition defining \( P \) in at most one element: \( S \coloneqq M \) works.
:::

The axiom of choice gives the same set in one line, by choosing one element from each class; the template's advantage shows when the pieces interact, as in Section 6.3. On \( \nR \), the relation \( x \sim y \iff x - y \in \nQ \) is an equivalence relation (Section 5.2, after @exm-reals-mod-integers). A set of representatives for it inside \( [0, 1] \) is a set of real numbers that *Measure and Integration*, Chapter 1 shows has no length, and no formula for one is known.

::: {.check}
Let \( X = \nZ \) and \( m \sim n \iff m - n \) is even. Describe the partial objects of @exm-zorn-representatives that have two elements, and the maximal ones.
:::

::: {.solution}
They are the sets \( \{e, o\} \) with \( e \) even and \( o \) odd: two even or two odd integers are related, since their difference is even, so a partial object holds at most one of each parity. Conversely, \( \{e, o\} \) is a partial object: with \( e = 2a \) and \( o = 2b + 1 \), \( e - o = 2(a - b - 1) + 1 \) is odd, hence not even (no integer is both, @thm-even-or-odd), so \( e \not\sim o \). These are exactly the maximal elements, since any third integer has the parity of \( e \) or of \( o \) (every integer is even or odd, @thm-even-or-odd), and \( \emptyset \) and the one-element sets are not maximal, since each lies strictly inside some \( \{e, o\} \). There are many maximal elements, such as \( \{0, 1\} \) and \( \{4, -7\} \), and no greatest one.
:::

::: {.warning}
**Check that the union is a partial object.** Here is an almost-correct proof that \( \nN \) has a maximal finite subset. "Let \( P \) be the set of finite subsets of \( \nN \), ordered by \( \subseteq \). A chain has its union as an upper bound. By Zorn's lemma, \( P \) has a maximal element." The conclusion is false, by the third example after @thm-zorn. The failing line is the second: the union is an upper bound in \( \powerset{\nN} \), but it need not be finite, so it need not lie in \( P \). "Finite" is a condition on all the elements at once, and @lem-chain-union handles only finitely many.
:::

Section 6.3 applies the template twice more, first to the matching that opened this section.

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

::: {#exr-chains-and-zorn-a1}
[A1]

These questions are about the proof of @thm-choice-from-zorn.

::: {.enumerate options="label=(\alph*)"}
1. Where is "\( A_i \ne \emptyset \)" used, and which step fails without it?
2. Why does the chain step need @lem-chain-union only for \( n = 2 \)?
3. Run the proof on \( I = \{1, 2\} \), \( A_1 = \{0\} \), \( A_2 = \{5, 6\} \): list \( P \), name its maximal elements, and decide whether \( P \) has a greatest element.
4. Which of the two hypotheses of @thm-zorn does the empty partially ordered set satisfy?
:::
:::

::: {.solution}
(a) In the last step: \( x_0 \in A_{i_0} \) exists only because \( A_{i_0} \ne \emptyset \). Without it, \( M \) could miss \( i_0 \) and still be maximal, and indeed no choice function exists if some \( A_i \) is empty.

(b) Condition (C1) mentions one pair and (C2) mentions two; no condition defining \( P \) mentions more.

(c) \( U = \{0, 5, 6\} \), and
\[
P = \bigl\{ \emptyset, \{(1, 0)\}, \{(2, 5)\}, \{(2, 6)\}, \{(1, 0), (2, 5)\}, \{(1, 0), (2, 6)\} \bigr\}.
\]
The maximal elements are the last two, each the graph of a choice function. There is no greatest element: the two maximal elements are incomparable, and a greatest element would be maximal (@prp-greatest-maximal (a)), so it would be one of them and contain the other.

(d) The chain hypothesis, vacuously; not non-emptiness.
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

::: {#exr-chains-and-zorn-b3}
[B3: A small poset of partial injections]

Let \( A = \{1, 2\} \) and \( B = \{b\} \). List the relations \( G \subseteq A \times B \) in which each element of \( A \) and each element of \( B \) occurs in at most one pair, ordered by \( \subseteq \). Name the maximal elements. For each, is every element of \( A \) paired? Every element of \( B \)?
:::

::: {.solution}
They are \( \emptyset \), \( \{(1, b)\} \) and \( \{(2, b)\} \); the only other subset of \( A \times B \), \( \{(1, b), (2, b)\} \), fails because \( b \) occurs twice. The maximal elements are \( \{(1, b)\} \) and \( \{(2, b)\} \). Neither pairs every element of \( A \); each pairs every element of \( B \), and read backwards it is an injection \( B \to A \). (Section 6.3 shows that this always happens: a maximal partial injection uses up one side.)
:::

::: {#exr-chains-and-zorn-b4}
[B4: Prove or disprove]

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
(a) False. Take \( P = \{ \{1\}, \{2\} \} \) under \( \subseteq \). Its chains are \( \emptyset \), \( \{\{1\}\} \) and \( \{\{2\}\} \), each with an upper bound in \( P \). But \( P \) has no greatest element, since \( \{1\} \) and \( \{2\} \) are incomparable.

(b) True. Let \( P \) be non-empty and finite, and let \( C \) be a non-empty chain of \( P \). Then \( C \) is finite (@prp-subset-finite); list it as \( x_1, \dots, x_n \) with \( n \ge 1 \). By @lem-chain-union (a), one \( x_k \) is above all of them, an upper bound of \( C \) in \( P \). By @thm-zorn, \( P \) has a maximal element. (Section 5.3, Exercise R4 proves this without Zorn's lemma, by induction.)

(c) False. The set \( E \) of even numbers and the set \( O \) of odd numbers both contain no two consecutive numbers. A greatest element \( G \) would contain \( E \) and \( O \), so \( 0, 1 \in G \), which are consecutive. (In fact \( E \) and \( O \) are both maximal: adding any \( n \notin E \) to \( E \) puts \( n \) and \( n + 1 \) in it (\( n \) is odd by @thm-even-or-odd, so \( n + 1 \) is even), and adding any \( n \notin O \) to \( O \) does the same. So Zorn's lemma, if applied here, gives a maximal element, never a greatest one, as the warning after @thm-zorn says.)

(d) True. Let \( p \in P \), and let \( Q \coloneqq \{ q \in P : p \preceq q \} \), ordered by \( \preceq \); then \( p \in Q \). A non-empty chain \( \sK \) of \( Q \) is a chain of \( P \), so it has an upper bound \( u \in P \); for any \( c \in \sK \), \( p \preceq c \preceq u \), so \( u \in Q \) by (PO3). By @thm-zorn, \( Q \) has a maximal element \( m \), and \( p \preceq m \). If \( m \prec q \) for some \( q \in P \), then \( p \preceq q \) by (PO3), so \( q \in Q \), against the maximality of \( m \) in \( Q \). So \( m \) is maximal in \( P \).

(e) False. Let \( C \subseteq \nR \) be countable. Then \( C \ne \nR \), since \( \nR \) is uncountable (@thm-reals-uncountable-decimal); for \( x \in \nR \setminus C \), the set \( C \cup \{x\} \) is countable (@prp-union-two-countable) and strictly larger. So no countable set is maximal. (By the contrapositive of Zorn's lemma, some non-empty chain of countable sets has no countable upper bound; the answer does not need one.)
:::

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

(b) That \( \le_l \) is a total order is the argument of Section 5.3, Exercises A1 (d) and C1 (a), with \( \nR \) in place of \( \nN \): it uses only trichotomy and transitivity of \( \le \). Containment: if \( x_1 \le y_1 \) and \( x_2 \le y_2 \), then either \( x_1 < y_1 \), or \( x_1 = y_1 \) and \( x_2 \le y_2 \); in both cases \( (x_1, x_2) \le_l (y_1, y_2) \).
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

The argument does not prove it. It never checks that \( \bigcup \sK \) **is a chain**, that is, that it lies in \( P \); the upper bound in @thm-zorn must belong to \( P \). The step's general form, "the union of a chain of partial objects lies in \( P \)", is false: among the finite subsets of \( \nN \), the chain \( \{ \{0, \dots, n - 1\} : n \in \nN \} \) has union \( \nN \), which is not finite (the warning before these exercises). Here the conclusion of the step happens to be true, which is exactly why it must be proved, not assumed. The repair is the chain step of B1: two elements of \( \bigcup \sK \) lie in one member \( K \in \sK \) (@lem-chain-union (b)), which is a chain, so they are comparable.

**Marking scheme.** (10 points)
- 2: the conclusion is true, with B1 cited.
- 3: the missing check named: \( \bigcup \sK \in P \).
- 3: a counterexample to the general inference "the union of a chain of partial objects lies in \( P \)" (in any partially ordered set), with the remark that here the step's conclusion is true but unproved.
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

### R. Review

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

(b) The union of a chain of finite sets need not be finite (the second warning of Section 6.2), so step (2) fails: the union need not be a partial object.

(c) This is the point of @exm-maximal-not-greatest. Maximal independent sets need not contain one another, so a vector space can have many bases, none of them greatest. In \( \nR^2 \), \( \{ (1, 0), (1, 1) \} \) and \( \{ (2, 0), (0, 3) \} \) are both bases, and neither contains the other.
:::

<!-- dependency ledger
lem-chain-union (claim): subset-inclusion restricted to a set of sets is a partial order | inline, by exm-subset-order-not-total and restriction of (PO1)-(PO3)
def-chain (example): 2^n = 2^(n-m) * 2^m for m <= n | school arithmetic
thm-zorn (claim): the set of finite subsets of N is a set | set-builder on P(N) (Chapter 1)
thm-zorn (claim): status paragraph, Zorn's lemma equivalent to ax-choice, which is independent (Section 6.1, ax-choice status remark); converse proved in ST.4 | prose pointer to Axiomatic Set Theory; nothing depends on it
exm-zorn-representatives (example): a set of representatives for x - y in Q inside [0, 1] has no length | prose pointer to Measure and Integration Ch 1 (MT.1); nothing depends on it
exm-zorn-representatives (solution): Quick check, same-parity integers have even difference; every integer is even or odd | arithmetic; thm-even-or-odd
exr-chains-and-zorn-b4 (solution): (c) n not in E is odd, so n + 1 is even | thm-even-or-odd
exm-zorn-representatives (example): x ~ y iff x - y in Q is an equivalence relation on R | Section 5.2 (after exm-reals-mod-integers)
exr-chains-and-zorn-a1 (solution): the enumeration of P for I = {1, 2} | finite check
exr-chains-and-zorn-b3 (solution): the three relations and the maximal ones | finite check
thm-order-extension (claim): worked schedule: generated order has 11 pairs; two schedules; seven in all | finite check; verify/ch06/thm-order-extension.py
lem-one-step-order-extension (proof): all cases of (PO2), (PO3) | inline; verify/ch06/lem-one-step-order-extension.py (all partial orders on 4 points)
lem-one-step-order-extension (claim): (Quick check) R on P({1,2}) adds only ({1},{2}) | verify/ch06/lem-one-step-order-extension.py
thm-order-extension (proof): union of a chain of partial orders is one; maximal is total | lem-chain-union (b), thm-zorn, lem-one-step-order-extension (cited)
exm-divisibility-linear-extension (solution): totality and trichotomy of <= on N; a, b > 0 and b = ka give k > 0, k >= 1, b >= a | R order and arithmetic (school facts; axioms in AN1.1); def-divides (cited); verify/ch06/exm-divisibility-linear-extension.py
exm-divisibility-linear-extension (claim): (Quick check) order 1, 4, 6, 12, 0; only 4, 6 incomparable under divisibility | verify/ch06/exm-divisibility-linear-extension.py
exm-divisibility-linear-extension (claim): no formula for a total extension of inclusion on P(R) is known | prose remark (nothing depends on it)
exm-divisibility-linear-extension (claim): (optional subsection) basis theorem, R over Q has no explicit basis | LA §1.8 thm-basis-extension-general (prose pointer; nothing depends on it)
exr-using-zorn-b2 (solution): proper subset of a finite set has fewer elements; two total extensions on P({1,2}) | prp-subset-finite (cited); verify/ch06/exr-using-zorn-b2.py
exr-using-zorn-b3 (solution): lexicographic order total | Section 5.3 Exercises A1 (d), C1 (a) (cited), with R for N; R order (school fact)
exr-using-zorn-c1 (solution): extension of R; exchanged lemma | thm-order-extension, lem-one-step-order-extension (cited); verify/ch06/lem-one-step-order-extension.py (intersection check on 4 points)
exr-using-zorn-r3 (solution): bases of R^2 | linear algebra (optional item; prose only; nothing depends on it)
-->
