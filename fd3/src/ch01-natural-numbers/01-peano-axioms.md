# Peano's Axioms and Induction

<!-- S3: rewrite per blueprint (layout-proposal.md §3, 1.1, pipeline F). New opening: why the reader needs axioms for ℕ now (to build ℝ we cannot start from the ℕ inside ℝ). Kept verbatim below from old 1.4 (def-peano-system, exm-peano-axioms-independent, exercises) and old 1.3 (thm-omega-induction, to be restated as a theorem about a Peano system); unique predecessor to be added (label named at S1). The old 1.4 opening paragraph follows; it describes ω and is to be replaced. -->

The previous section built \( \omega \) and proved induction on it (@thm-omega-induction). *Sets and Functions*, Chapter 3 used two further facts about the natural numbers without a second thought: \( 0 \) is not of the form \( n + 1 \), and \( m + 1 = n + 1 \) forces \( m = n \). For the sets of this chapter neither is automatic, and the obvious argument for the second fails, as we shall see. This section proves both for natural numbers, using one property of their membership structure; it then names the list of properties we have reached, Peano's axioms, and shows that each of its last three items, (P3), (P4) and (P5), does a job that the other two cannot do.

## Peano systems

*Sets and Functions*, Chapter 3 worked with a set \( \nN \) of real numbers, and this chapter with a set \( \omega \) of sets. Both come with a starting element and a step. The last section of the chapter asks whether they are "the same", and to ask it we need to say what any such structure must satisfy. The answer is the list just proved, with \( \omega \), \( 0 \) and \( \mathrm{S} \) replaced by letters.

*A Peano system is a set with a start and a step, where the step is one-to-one, never returns to the start, and reaches everything.*

::: {#def-peano-system}
[Peano system]

A **Peano system** \( (M, e, s) \) consists of a set \( M \), an element \( e \in M \), and a function \( s \colon M \to M \), such that:

- (P3) \( s(x) \ne e \) for **every** \( x \in M \);
- (P4) \( s \) is injective;
- (P5) **every** subset \( A \subseteq M \) with \( e \in A \) and \( s(x) \in A \) for every \( x \in A \) is equal to \( M \).
:::

In words: (P1) and (P2) are built into the data, since \( e \in M \) and \( s \) maps \( M \) into \( M \). (P3) says the step never leads back to the start. (P4) says two different elements never step to the same element. (P5) is induction for \( M \): a subset that contains the start and is closed under the step is everything, so every element of \( M \) is reached from \( e \) by steps. We write \( (M, e, s) \) and not \( (N, e, s) \), so that the letter never suggests \( \nN \). The notation \( (M, e, s) \) lists the three pieces of data; it is not a set built from them (if one object is wanted, take the pair \( ((M, e), s) \) of @def-kuratowski-pair).

The first example is the one we have, and the second shows that the elements need not be numbers.

- \( (\omega, 0, \mathrm{S}) \) is a Peano system, by @thm-omega-peano: \( \mathrm{S} \colon \omega \to \omega \) is a function, and (P3)–(P5) are those of the theorem.
- **Tagged numbers.** Let \( M \coloneqq \omega \times \{0\} \), a set by @prp-cartesian-product-exists, let \( e \coloneqq (0, 0) \), and let \( s(n, 0) \coloneqq (\mathrm{S}(n), 0) \). Every element of \( M \) is \( (n, 0) \) for exactly one \( n \in \omega \) (@thm-kuratowski-pair), so \( s \) is well defined, and its graph is a set by (Z6) inside \( M \times M \). (P3): \( (\mathrm{S}(n), 0) = (0, 0) \) would give \( \mathrm{S}(n) = 0 \) by @thm-kuratowski-pair, against (P3) for \( \omega \). (P4): \( (\mathrm{S}(m), 0) = (\mathrm{S}(n), 0) \) gives \( \mathrm{S}(m) = \mathrm{S}(n) \), so \( m = n \) by (P4) for \( \omega \). (P5): let \( A \subseteq M \) contain \( e \) and be closed under \( s \). The set \( B \coloneqq \{ n \in \omega : (n, 0) \in A \} \) has \( 0 \) as an element and is closed under \( \mathrm{S} \), so \( B = \omega \) by @thm-omega-induction (a), and \( A = M \). Here \( e = (0, 0) = \{\{0\}\} \) is not \( \emptyset \), and no element of \( M \) is a natural number, as we shall see at the end of the section.

Why these three clauses and no others? Each one does work that the other two cannot do: for each clause there is a structure satisfying the other two and failing it.

::: {#exm-peano-axioms-independent}
[Each axiom is needed]

Show that each of the following structures \( (M, e, s) \), with \( s \colon M \to M \), satisfies two of (P3), (P4), (P5) and fails the third.

::: {.enumerate options="label=(\roman*)"}
1. \( M \coloneqq \{0\} \), \( e \coloneqq 0 \), \( s(0) \coloneqq 0 \).
2. \( M \coloneqq \{0, 1\} \), \( e \coloneqq 0 \), \( s(0) \coloneqq 1 \), \( s(1) \coloneqq 1 \).
3. (**The natural numbers beside a two-sided chain.**) \( M \coloneqq \omega \times 3 \), whose elements are the pairs \( (n, i) \) with \( n \in \omega \) and \( i \in 3 = \{0, 1, 2\} \); \( e \coloneqq (0, 0) \); and
\[
\begin{aligned}
s(n, 0) &\coloneqq (\mathrm{S}(n), 0) , & s(n, 1) &\coloneqq (\mathrm{S}(n), 1) , \\
s(0, 2) &\coloneqq (0, 1) , & s(\mathrm{S}(k), 2) &\coloneqq (k, 2) ,
\end{aligned}
\]
for \( n, k \in \omega \).
:::
:::

::: {.solution}
(i) **Fails (P3)**: \( s(0) = 0 = e \). (P4) holds: \( M \) has one element, so two inputs with equal outputs are equal. (P5) holds: a subset of \( \{0\} \) containing \( e = 0 \) is \( \{0\} \).

(ii) **Fails (P4)**: \( s(0) = s(1) \) with \( 0 \ne 1 \). (P3) holds: both values are \( 1 \ne 0 = e \). (P5) holds: if \( A \subseteq \{0, 1\} \) has \( 0 \) as an element and is closed under \( s \), then \( s(0) = 1 \in A \), so \( A = \{0, 1\} \).

(iii) First, \( s \) is a function \( M \to M \). Each element of \( M \) is \( (n, i) \) for exactly one \( n \in \omega \) and one \( i \in 3 \), by @thm-kuratowski-pair. For \( i = 2 \), the first coordinate is \( 0 \) or \( \mathrm{S}(k) \) with \( k \in \omega \) (@lem-omega-transitive (d)); never both, by (P3) for \( \omega \); and the \( k \) is unique, by (P4) for \( \omega \). So exactly one line of the definition applies to each element, and it names one value. The values lie in \( M \), since \( \mathrm{S}(n), 0, k \in \omega \). The graph is a set by (Z6) inside \( M \times M \).

To check (P3) and (P4), sort the values by their second coordinates, which are \( 0 \), \( 1 \) and \( 2 \), three different sets (@exm-von-neumann-numerals):
\[
\begin{aligned}
&\text{second coordinate } 0 : && s(n, 0) = (\mathrm{S}(n), 0) , \\
&\text{second coordinate } 1 : && s(n, 1) = (\mathrm{S}(n), 1) \ \text{ and } \ s(0, 2) = (0, 1) , \\
&\text{second coordinate } 2 : && s(\mathrm{S}(k), 2) = (k, 2) .
\end{aligned}
\]

**(P3) holds.** A value equal to \( e = (0, 0) \) would have second coordinate \( 0 \), so it would be \( (\mathrm{S}(n), 0) \) with \( \mathrm{S}(n) = 0 \), against (P3) for \( \omega \).

**(P4) holds.** Suppose \( s(x) = s(x') \). The two values have the same second coordinate, so they come from the same row of the display. In the first row, \( (\mathrm{S}(n), 0) = (\mathrm{S}(n'), 0) \) gives \( n = n' \) by @thm-kuratowski-pair and (P4) for \( \omega \). In the third row, \( (k, 2) = (k', 2) \) gives \( k = k' \), so \( \mathrm{S}(k) = \mathrm{S}(k') \). In the second row, \( (\mathrm{S}(n), 1) \ne (0, 1) \) because \( \mathrm{S}(n) \ne 0 \); so either both values are of the form \( (\mathrm{S}(n), 1) \), and \( n = n' \) as before, or both are \( (0, 1) \), and both inputs are \( (0, 2) \). In every case \( x = x' \).

**(P5) fails.** Let \( A \coloneqq \omega \times \{0\} \), a subset of \( M \) (@prp-cartesian-product-exists). It contains \( e = (0, 0) \), and it is closed under \( s \), since \( s(n, 0) = (\mathrm{S}(n), 0) \in A \). But \( (0, 1) \in M \) is not in \( A \), because its second coordinate \( 1 \) is not \( 0 \). So \( A \ne M \).
:::

The picture shows (iii), with an arrow from each element to its image under \( s \).

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.85, every node/.style={font=\small}]
  \node (a0) at (0,1.5) {$(0,0)$};
  \node (a1) at (1.4,1.5) {$(1,0)$};
  \node (a2) at (2.8,1.5) {$(2,0)$};
  \node (a3) at (4.2,1.5) {$(3,0)$};
  \node (ad) at (5.6,1.5) {$\cdots$};
  \draw[->] (a0) -- (a1);
  \draw[->] (a1) -- (a2);
  \draw[->] (a2) -- (a3);
  \draw[->] (a3) -- (ad);
  \node[above] at (a0.north) {$e$};
  \node (bd) at (0,0) {$\cdots$};
  \node (b2) at (1.4,0) {$(2,2)$};
  \node (b1) at (2.8,0) {$(1,2)$};
  \node (b0) at (4.2,0) {$(0,2)$};
  \node (c0) at (5.6,0) {$(0,1)$};
  \node (c1) at (7.0,0) {$(1,1)$};
  \node (c2) at (8.4,0) {$(2,1)$};
  \node (cd) at (9.8,0) {$\cdots$};
  \draw[->] (bd) -- (b2);
  \draw[->] (b2) -- (b1);
  \draw[->] (b1) -- (b0);
  \draw[->] (b0) -- (c0);
  \draw[->] (c0) -- (c1);
  \draw[->] (c1) -- (c2);
  \draw[->] (c2) -- (cd);
\end{tikzpicture}
\end{center}
```

The top row is a copy of \( \omega \), starting at \( e \). The bottom row is a chain running forever in both directions: read \( (n, 1) \) as "\( n \)" and \( (k, 2) \) as "\( -(k + 1) \)", and \( s \) adds one everywhere, with \( (0, 2) \), playing \( -1 \), stepping to \( (0, 1) \), playing \( 0 \). Every element has exactly one arrow out and at most one arrow in, which is (P4); only \( e \) has no arrow in, which is (P3). What fails is that the bottom row cannot be reached from \( e \). Induction, (P5), is the clause that says "nothing else".

So (P3) and (P4) alone cannot prevent extra elements: in (iii) the whole bottom row is extra. That is why the definition of \( \omega \) needed "least", and why induction is part of the list.

<!-- S3: moved verbatim from old 1.3; restate (a) and (b) for a Peano system (M, e, s), where (b) is (P5) read as a property; the proof below is the ω proof and is replaced. -->

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
*(a)* The hypotheses say that \( A \) is inductive. By @thm-omega-least-inductive (b), \( \omega \subseteq A \). With \( A \subseteq \omega \), @fd2:prp-subset-antisymmetric gives \( A = \omega \).

*(b)* Let \( A \coloneqq \{ n \in \omega : P(n) \} \), a set by (Z6). Then \( 0 \in A \), because \( 0 \in \omega \) by @thm-omega-least-inductive (a) and \( P(0) \) holds. Let \( n \in A \). Then \( n \in \omega \) and \( P(n) \), so \( P(\mathrm{S}(n)) \) by hypothesis, and \( \mathrm{S}(n) \in \omega \) because \( \omega \) is inductive; hence \( \mathrm{S}(n) \in A \). By (a), \( A = \omega \), which says that \( P(n) \) holds for every \( n \in \omega \).
:::

Compare part (b) with the principle of induction, @fd1:ax-induction. Read with \( \omega \) in place of \( \nN \), and with \( \mathrm{S}(n) \) in place of \( n + 1 \), the two statements are the same; and once addition is defined, later in this chapter, \( n + 1 \) will be \( \mathrm{S}(n) \). The difference lies in their status. In *Logic and Proof*, Chapter 4, induction was an axiom, a basic property of \( \nN \) taken on trust. Here it is a **theorem**, proved from the seven axioms (Z1)–(Z7) about sets, and the proof is three lines long because all the work went into the definition of \( \omega \): the natural numbers were defined as what every inductive set contains, and induction says exactly that.

The proof of (b) is the model for the inductions in the rest of this chapter.

**Show the set is inductive.** To prove \( P(n) \) for every \( n \in \omega \), form \( \{ n \in \omega : P(n) \} \) and show that it has \( 0 \) as an element and is closed under \( \mathrm{S} \).

Here is the move once, on a statement about the shape of natural numbers: **every \( n \in \omega \) is \( 0 \), or is \( 1 \), or has \( 1 \) as an element**. Let \( A \coloneqq \{ n \in \omega : n = 0 \text{ or } n = 1 \text{ or } 1 \in n \} \), a set by (Z6). Then \( 0 \in A \) by the first alternative. Let \( n \in A \); there are three cases. If \( n = 0 \), then \( \mathrm{S}(n) = 1 \), which satisfies the second alternative. If \( n = 1 \), then \( \mathrm{S}(n) = 2 = \{0, 1\} \), which has \( 1 \) as an element. If \( 1 \in n \), then \( 1 \in n \subseteq \mathrm{S}(n) \). In every case \( \mathrm{S}(n) \in A \), since also \( \mathrm{S}(n) \in \omega \) because \( \omega \) is inductive (@thm-omega-least-inductive (a)). By @thm-omega-induction (a), \( A = \omega \).

Two features of this small proof recur. The property carried along is a disjunction, because "\( 1 \in n \)" alone is false at \( n = 0 \) and \( n = 1 \), and an induction can only carry a property that holds at the start. And the step is a case split along the disjunction, with one case for each alternative; dropping a case would be the error (N7) of @fd1:exm-not-allowed-catalogue.

::: {.check}
In the proof just given, which case of the step produces the first natural number that satisfies the third alternative "\( 1 \in n \)", and which number is it?
:::

::: {.solution}
The case \( n = 1 \). It produces \( \mathrm{S}(1) = 2 = \{0, 1\} \), which has \( 1 \) as an element. Neither \( 0 \) nor \( 1 \) has \( 1 \) as an element (\( 0 \) has no elements, and the only element of \( 1 \) is \( 0 \ne 1 \)), so \( 2 \) is the first. From then on the third case passes "\( 1 \in n \)" to \( \mathrm{S}(n) \), because \( n \subseteq \mathrm{S}(n) \).
:::

The next section uses the move five times in a row, to show that \( \omega \) satisfies Peano's axioms.

With Peano's axioms in hand, the next section proves the recursion theorem on \( \omega \) and uses it to define addition and multiplication.

## Exercises

### A. Check your understanding

::: {#exr-peano-properties-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. For each of the three structures in @exm-peano-axioms-independent, which of (P3), (P4), (P5) fails?
2. In the proof of (P4) in @thm-omega-peano, where is @lem-omega-transitive (a) used, and where is (c)?
3. Is \( \omega \cup \{\omega\} \) inductive? Justify your answer.
4. Is \( \{0, 1, \{1\}\} \) a transitive set? Is it an element of \( \omega \)?
:::
:::

::: {.solution}
(a) (i) fails (P3); (ii) fails (P4); (iii) fails (P5). Each satisfies the other two (@exm-peano-axioms-independent).

(b) Part (a) is used to pass from \( n \in m \) to \( n \subseteq m \): \( m \) is a natural number, hence a transitive set. Part (c) is used at the end: the argument reaches \( m \in m \), and (c) says \( m \notin m \), which gives the contradiction.

(c) No. The set \( \omega \cup \{\omega\} = \mathrm{S}(\omega) \) has \( \emptyset \) as an element and is closed under \( \mathrm{S} \) on its elements from \( \omega \), but \( \mathrm{S}(\omega) \) itself is not an element of \( \omega \cup \{\omega\} \). First, \( \mathrm{S}(\omega) \ne \omega \): \( \omega \in \mathrm{S}(\omega) \), while \( \omega \notin \omega \) (the Quick check after @thm-omega-peano). Second, \( \mathrm{S}(\omega) \notin \omega \): otherwise \( \mathrm{S}(\omega) \subseteq \omega \) because \( \omega \) is transitive (@lem-omega-transitive (b)), and \( \omega \in \mathrm{S}(\omega) \) would give \( \omega \in \omega \). So the closure clause fails at the element \( \omega \).

(d) It is transitive: \( 0 = \emptyset \) is a subset of every set; \( 1 = \{0\} \) is a subset, since \( 0 \) is listed; \( \{1\} \) is a subset, since \( 1 \) is listed. It is not an element of \( \omega \): by @lem-omega-transitive (b), every element of a natural number is a natural number, and \( \{1\} \) is not one. Indeed \( \{1\} \ne 0 \), and if \( \{1\} = \mathrm{S}(k) = k \cup \{k\} \) with \( k \in \omega \), then \( k \in \{1\} \), so \( k = 1 \), and \( \mathrm{S}(1) = \{0, 1\} \ne \{1\} \) since \( 0 \notin \{1\} \); this contradicts @lem-omega-transitive (d). So being transitive does not make a set a natural number.
:::

### B. Practice

::: {#exr-peano-properties-b1}
[B1: Put the proof in order]

Let \( m, n \in \omega \). The following lines contain a proof that **if \( \mathrm{S}(m) = \mathrm{S}(n) \), then \( m = n \)**, shuffled, together with two lines that do not belong. Write the seven correct lines in an order that makes a proof, say which other orders are also admissible, and say why each of the other two lines fails.

(i) So \( m \in n \subseteq m \), that is, \( m \in m \).

(ii) Suppose \( \mathrm{S}(m) = \mathrm{S}(n) \).

(iii) We have \( m \cup \{m\} = n \cup \{n\} \), so \( m = n \) by canceling \( {\cup}\{\cdot\} \) on both sides.

(iv) Since \( n \in \mathrm{S}(n) = \mathrm{S}(m) \), we have \( n \in m \) or \( n = m \).

(v) Suppose \( m \ne n \); then \( m \in n \) and \( n \in m \).

(vi) This contradicts \( m \notin m \) (@lem-omega-transitive (c)); so \( m = n \).

(vii) From \( m \in n \) and \( n \in m \) we get \( m = n \), since \( \in \) is antisymmetric.

(viii) Since \( m \) is transitive (@lem-omega-transitive (a)) and \( n \in m \), we have \( n \subseteq m \).

(ix) Since \( m \in \mathrm{S}(m) = \mathrm{S}(n) \), we have \( m \in n \) or \( m = n \).
:::

::: {.solution}
An admissible order is (ii), (ix), (iv), (v), (viii), (i), (vi):

> Suppose \( \mathrm{S}(m) = \mathrm{S}(n) \). Since \( m \in \mathrm{S}(m) = \mathrm{S}(n) \), we have \( m \in n \) or \( m = n \). Since \( n \in \mathrm{S}(n) = \mathrm{S}(m) \), we have \( n \in m \) or \( n = m \). Suppose \( m \ne n \); then \( m \in n \) and \( n \in m \). Since \( m \) is transitive and \( n \in m \), we have \( n \subseteq m \). So \( m \in n \subseteq m \), that is, \( m \in m \). This contradicts \( m \notin m \); so \( m = n \).

The only other admissible order exchanges (ix) and (iv), which use only (ii) and not each other. Everything else is forced: (v) needs both (ix) and (iv) to reduce each disjunction to its first alternative; (viii) needs the \( n \in m \) of (v); (i) needs the \( m \in n \) of (v) and the inclusion of (viii); (vi) closes the \( \rulename{RAA} \) box opened by (v), whose assumption is \( m \ne n \), the negation of the goal (@fd1:def-rule-raa).

The distractor (iii) cancels where no cancellation law exists. For sets in general, \( x \cup \{y\} = x' \cup \{y'\} \) does not give \( y = y' \): \( \{1\} \cup \{0\} = \{0\} \cup \{1\} \) with \( 0 \ne 1 \). For natural numbers the conclusion \( m = n \) happens to be true, but that is the statement being proved, not a reason for it.

The distractor (vii) cites a "fact" that is not available. No result so far says that \( m \in n \) and \( n \in m \) cannot both hold, and for natural numbers that is exactly what lines (viii), (i) and (vi) establish. Citing it is the circular step (N9) of @fd1:exm-not-allowed-catalogue: the line uses, as a reason, what the proof is there to show.
:::

::: {#exr-peano-properties-b2}
[B2: Two steps at a time]

Let \( d \coloneqq \mathrm{S} \circ \mathrm{S} \colon \omega \to \omega \) (@fd2:def-composition), so that \( d(n) = \mathrm{S}(\mathrm{S}(n)) \). Show that \( (\omega, 0, d) \) satisfies (P3) and (P4) of @def-peano-system, and that it does not satisfy (P5).

*Hint: look at the set \( \omega \setminus \{1\} \).*
:::

::: {.solution}
(P3): for \( n \in \omega \), \( d(n) = \mathrm{S}(\mathrm{S}(n)) \ne 0 \) by (P3) of @thm-omega-peano, applied to \( \mathrm{S}(n) \in \omega \).

(P4): if \( d(m) = d(n) \), then \( \mathrm{S}(\mathrm{S}(m)) = \mathrm{S}(\mathrm{S}(n)) \), so \( \mathrm{S}(m) = \mathrm{S}(n) \) by (P4) of @thm-omega-peano, and then \( m = n \) by (P4) again. (Equivalently: \( d \) is a composite of two injections, so it is injective by @fd2:thm-composition-injective-surjective (a).)

(P5) fails. Let \( A \coloneqq \omega \setminus \{1\} \). It contains \( 0 \), since \( 0 \ne 1 \). It is closed under \( d \): let \( n \in A \); then \( d(n) \in \omega \), and \( d(n) \ne 1 \), because \( \mathrm{S}(\mathrm{S}(n)) = 1 = \mathrm{S}(0) \) would give \( \mathrm{S}(n) = 0 \) by (P4), against (P3). But \( A \ne \omega \), since \( 1 \in \omega \) and \( 1 \notin A \). So a subset of \( \omega \) with \( 0 \) as an element and closed under \( d \) need not be all of \( \omega \). The step \( d \) skips \( 1 \), and starting from \( 0 \) it reaches only the "even" numbers.
:::

### C. Going deeper

::: {#exr-peano-properties-c1}
[C1: A Peano system with a different start]

Give an example of a Peano system \( (M, e, s) \) with \( M \subseteq \omega \) and \( e \ne 0 \). Check every clause of @def-peano-system.
:::

::: {.solution}
Any correct answer has: a set \( M \subseteq \omega \); an element \( e \in M \) with \( e \ne 0 \); a function \( s \colon M \to M \), so that every value lies in \( M \); and the three clauses (P3), (P4), (P5) for these data.

Take \( M \coloneqq \omega \setminus \{0\} \), \( e \coloneqq 1 \), and \( s(n) \coloneqq \mathrm{S}(n) \) for \( n \in M \).

- **The data.** \( 1 \in M \), since \( 1 \in \omega \) and \( 1 \ne 0 \). For \( n \in M \), \( \mathrm{S}(n) \in \omega \) by (P2) and \( \mathrm{S}(n) \ne 0 \) by (P3) of @thm-omega-peano, so \( \mathrm{S}(n) \in M \). The graph \( \{ (n, \mathrm{S}(n)) : n \in M \} \) is a set by (Z6) inside \( M \times M \). (Fn1) holds, since \( (n, \mathrm{S}(n)) \) is in the graph for each \( n \in M \); (Fn2) holds as in the proof of @thm-omega-peano, by @thm-kuratowski-pair. So \( s \colon M \to M \) is a function (@fd2:def-function).
- **(P3).** If \( s(n) = 1 \) for some \( n \in M \), then \( \mathrm{S}(n) = \mathrm{S}(0) \), so \( n = 0 \) by (P4) for \( \omega \); but \( 0 \notin M \).
- **(P4).** If \( \mathrm{S}(m) = \mathrm{S}(n) \) with \( m, n \in M \), then \( m = n \) by (P4) for \( \omega \).
- **(P5).** Let \( A \subseteq M \) with \( 1 \in A \) and \( \mathrm{S}(n) \in A \) for every \( n \in A \). The set \( A' \coloneqq A \cup \{0\} \subseteq \omega \) is inductive: \( 0 \in A' \); \( \mathrm{S}(0) = 1 \in A \subseteq A' \); and for \( n \in A \), \( \mathrm{S}(n) \in A \subseteq A' \). By @thm-omega-induction (a), \( A' = \omega \). Every \( n \in M \) lies in \( A' \) and is not \( 0 \), so \( n \in A \). Hence \( A = M \).

Other answers can be checked against the four properties at the start. For instance, \( M \coloneqq \omega \setminus \{0, 1\} \), \( e \coloneqq 2 \), \( s(n) \coloneqq \mathrm{S}(n) \) also works, by the same argument with \( \{0, 1\} \) added in (P5).
:::

::: {#exr-peano-properties-c2}
[C2: Closed subsets of the chain]

Let \( (M, e, s) \) be the structure (iii) of @exm-peano-axioms-independent. Call \( A \subseteq M \) **good** if \( e \in A \) and \( s(x) \in A \) for every \( x \in A \).

::: {.enumerate options="label=(\alph*)"}
1. Show that every good set contains \( \omega \times \{0\} \).
2. Show that each of the following sets is good, where \( m, k \in \omega \):
\[
\begin{aligned}
G_0 &\coloneqq \omega \times \{0\} , \qquad G_\infty \coloneqq M , \\
R_m &\coloneqq G_0 \cup \{ (n, 1) : n \in \omega, \ m \in \mathrm{S}(n) \} , \\
L_k &\coloneqq G_0 \cup (\omega \times \{1\}) \cup \{ (j, 2) : j \in \mathrm{S}(k) \} .
\end{aligned}
\]
3. Show that a good set that contains \( (k, 2) \) contains \( L_k \).
:::
:::

::: {.solution}
[Hint 1]

For (a), apply induction to the set of \( n \in \omega \) with \( (n, 0) \in A \). For (c), the arrows of the bottom row point toward \( (0, 1) \): from \( (\mathrm{S}(k), 2) \) the step goes to \( (k, 2) \).
:::

::: {.solution}
[Hint 2]

For (c), prove by induction on \( k \in \omega \) the property: "for every good \( A \), if \( (k, 2) \in A \), then \( L_k \subseteq A \)".
:::

::: {.solution}
(a) Let \( A \) be good, and let \( B \coloneqq \{ n \in \omega : (n, 0) \in A \} \). Then \( 0 \in B \), because \( (0, 0) = e \in A \); and if \( n \in B \), then \( (\mathrm{S}(n), 0) = s(n, 0) \in A \), so \( \mathrm{S}(n) \in B \). By @thm-omega-induction (a), \( B = \omega \), so \( \omega \times \{0\} \subseteq A \).

(b) All four sets contain \( e = (0, 0) \in G_0 \). Closure is checked element by element, using the definition of \( s \).

- \( G_0 \): \( s(n, 0) = (\mathrm{S}(n), 0) \in G_0 \).
- \( G_\infty = M \): \( s \) maps \( M \) into \( M \).
- \( R_m \): elements of \( G_0 \) are handled as before. If \( (n, 1) \in R_m \) with \( m \in \mathrm{S}(n) \), then \( s(n, 1) = (\mathrm{S}(n), 1) \), and \( m \in \mathrm{S}(n) \subseteq \mathrm{S}(\mathrm{S}(n)) \); so \( s(n, 1) \in R_m \).
- \( L_k \): elements of \( G_0 \) as before; \( s(n, 1) = (\mathrm{S}(n), 1) \in \omega \times \{1\} \). Every \( j \in \mathrm{S}(k) \) lies in \( \omega \), since \( \mathrm{S}(k) \in \omega \) by (P2) of @thm-omega-peano and \( \omega \) is transitive (@lem-omega-transitive (b)); so \( L_k \subseteq M \). For \( (j, 2) \) with \( j \in \mathrm{S}(k) \): if \( j = 0 \), then \( s(0, 2) = (0, 1) \in L_k \); if \( j = \mathrm{S}(i) \) with \( i \in \omega \) (@lem-omega-transitive (d)), then \( s(j, 2) = (i, 2) \), and \( i \in \mathrm{S}(i) = j \in \mathrm{S}(k) \), so \( i \in \mathrm{S}(k) \) because \( \mathrm{S}(k) \) is transitive (@lem-omega-transitive (a)); hence \( (i, 2) \in L_k \).

(c) We prove by @thm-omega-induction (b) the property \( P(k) \): "for every good \( A \), if \( (k, 2) \in A \), then \( L_k \subseteq A \)".

*Base.* Let \( A \) be good with \( (0, 2) \in A \). Then \( (0, 1) = s(0, 2) \in A \). The set \( \{ n \in \omega : (n, 1) \in A \} \) has \( 0 \) as an element and is closed under \( \mathrm{S} \), since \( s(n, 1) = (\mathrm{S}(n), 1) \); so it is \( \omega \) by @thm-omega-induction (a), and \( \omega \times \{1\} \subseteq A \). With (a) and \( \mathrm{S}(0) = \{0\} \), this gives \( L_0 \subseteq A \).

*Step.* Let \( k \in \omega \) with \( P(k) \), and let \( A \) be good with \( (\mathrm{S}(k), 2) \in A \). Then \( (k, 2) = s(\mathrm{S}(k), 2) \in A \), so \( L_k \subseteq A \) by \( P(k) \). Now \( L_{\mathrm{S}(k)} = L_k \cup \{ (\mathrm{S}(k), 2) \} \), because \( j \in \mathrm{S}(\mathrm{S}(k)) \) means \( j \in \mathrm{S}(k) \) or \( j = \mathrm{S}(k) \). Both parts lie in \( A \), so \( L_{\mathrm{S}(k)} \subseteq A \), which is \( P(\mathrm{S}(k)) \).

So the good sets include \( G_0 \), the sets \( R_m \) (whose part in the bottom row starts at \( (m, 1) \) and runs to the right), the sets \( L_k \) (whose part in the bottom row starts at \( (k, 2) \)), and \( M \). Read on the two-sided chain, these are the empty part, the rays starting at some point, and the whole chain. That they are **all** the good sets is also true, but the proof needs a least element of a non-empty set of natural numbers, which comes later in this chapter with the order on \( \omega \). Part (c) already shows that a good set containing every \( (k, 2) \) contains every \( L_k \), hence all of \( M \). Every good set other than \( M \) is a witness to the failure of (P5).
:::

<!-- dependency ledger
def-peano-system (example): (tagged numbers) the graph of s is a set by (Z6) inside M x M | prp-cartesian-product-exists (cited)
exm-peano-axioms-independent (solution): 0, 1, 2 are three different sets, and 3 = {0, 1, 2} | exm-von-neumann-numerals (cited)
exm-peano-axioms-independent (claim): (the paragraph after the picture) reading (k, 2) as -(k + 1) | prose reading only; no integer arithmetic is used in any proof
exr-peano-properties-a1 (solution): (d) 0 not in {1} since 0 != 1 | exm-von-neumann-numerals (cited)
exr-peano-properties-c2 (solution): every good set is one of G_0, R_m, L_k, M | needs thm-omega-well-ordering, later in this chapter (stated, not proved here; nothing depends on it)
thm-omega-induction (claim): (the remark after it) n + 1 = S(n) once addition is defined | def-omega-arithmetic (a), with 1 := S(0) from (c); the paragraph "The successor is plus one" after it, later in this chapter (prose pointer; nothing in this section depends on it)
thm-omega-induction (example): (the worked move) 2 = {0, 1}, 1 != 0 | exm-von-neumann-numerals (cited)
thm-omega-induction (example): (the worked move) S(n) in omega | thm-omega-least-inductive (a) (cited)
-->
