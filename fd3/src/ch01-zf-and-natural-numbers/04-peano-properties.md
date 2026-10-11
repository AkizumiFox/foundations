# The Natural Numbers Satisfy Peano's Axioms

The previous section built \( \omega \) and proved induction on it (@thm-omega-induction). Chapter 7 used two further facts about the natural numbers without a second thought: \( 0 \) is not of the form \( n + 1 \), and \( m + 1 = n + 1 \) forces \( m = n \). For the sets of this chapter neither is automatic, and the obvious argument for the second fails, as we shall see. This section proves both for natural numbers, using one property of their membership structure; it then names the list of properties we have reached, Peano's axioms, and shows that each of its last three items, (P3), (P4) and (P5), does a job that the other two cannot do.

## Transitive sets

We want to prove: if \( m, n \in \omega \) and \( \mathrm{S}(m) = \mathrm{S}(n) \), then \( m = n \). The tempting move is to cancel, reading \( m \cup \{m\} = n \cup \{n\} \) as "the same thing was added to both". But union does not cancel: \( \{1\} \cup \{0\} = \{0\} \cup \{1\} \), and \( 0 \ne 1 \). What \( \mathrm{S}(m) = \mathrm{S}(n) \) does give is membership. Since \( m \in \mathrm{S}(m) = \mathrm{S}(n) \), either \( m \in n \) or \( m = n \); and likewise \( n \in m \) or \( n = m \). So the one bad case is \( m \in n \) and \( n \in m \) at once, two sets each inside the other.

For the numerals, membership only ever points to earlier numerals, and the elements of an element are earlier still. In \( 3 = \{0, 1, 2\} \), the element \( 2 \) has the elements \( 0 \) and \( 1 \), and both are again elements of \( 3 \). This is the property we name.

*A transitive set contains the elements of its elements.*

::: {#def-transitive-set}
[Transitive set]

A set \( x \) is **transitive** if **every** element of \( x \) is a subset of \( x \): for every \( y \in x \), \( y \subseteq x \).
:::

In words: unpacking \( y \subseteq x \) (@def-subset), \( x \) is transitive when, for all sets \( y \) and \( z \),
\[
z \in y \ \text{ and } \ y \in x \ \Longrightarrow \ z \in x .
\]
Membership passes through \( x \) in two steps: whatever is an element of an element of \( x \) is already an element of \( x \). The name comes from this display, which has the shape of the transitivity of a relation (@def-relation-properties) with \( \in \) as the relation and \( x \) fixed at the end.

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

Both cases contradict \( n \notin n \). So \( \mathrm{S}(n) \notin \mathrm{S}(n) \), by \( \rulename{\neg I} \) (@def-rules-negation).

*(d)* Let \( P(n) \) be "\( n = 0 \), or \( n = \mathrm{S}(k) \) for some \( k \in \omega \)". \( P(0) \) holds by the first alternative. For every \( n \in \omega \), \( P(\mathrm{S}(n)) \) holds by the second alternative, with \( k \coloneqq n \). So \( P(n) \) holds for every \( n \in \omega \), and for \( n \ne 0 \) the second alternative is the claim.

*(e)* Let \( P(n) \) be "\( n = 0 \) or \( 0 \in n \)". \( P(0) \) holds by the first alternative. Let \( n \in \omega \) with \( P(n) \). If \( n = 0 \), then \( \mathrm{S}(n) = \{0\} \), which has \( 0 \) as an element. If \( 0 \in n \), then \( 0 \in n \subseteq \mathrm{S}(n) \). Either way \( 0 \in \mathrm{S}(n) \), so \( P(\mathrm{S}(n)) \) holds. So \( P(n) \) holds for every \( n \in \omega \), and for \( n \ne 0 \) the second alternative is the claim. This proves the lemma.
:::

The step of (d) never used \( P(n) \). As with the predecessor in Chapter 7 (@exm-predecessor-no-hypothesis), the step's conclusion was reached outright, and induction is still what guarantees that \( 0 \) and the successors are all there is. Part (b) says that the natural numbers are built only from natural numbers: unwrapping a natural number never leads outside \( \omega \). Part (c) is the fact the bad case needed.

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

(P3) Let \( n \in \omega \). Then \( n \in \mathrm{S}(n) \). If \( \mathrm{S}(n) = 0 \), then \( n \in 0 \) by \( \rulename{{=}E} \) (@def-rules-equality), which is impossible, since \( 0 = \emptyset \) has no elements. So \( \mathrm{S}(n) \ne 0 \), by \( \rulename{\neg I} \) (@def-rules-negation).

(P4) Let \( m, n \in \omega \) with \( \mathrm{S}(m) = \mathrm{S}(n) \). Since \( m \in \mathrm{S}(m) = \mathrm{S}(n) \), we have \( m \in n \) or \( m = n \); likewise, since \( n \in \mathrm{S}(n) = \mathrm{S}(m) \), we have \( n \in m \) or \( n = m \). Suppose \( m \ne n \). Then \( m \in n \) and \( n \in m \). Since \( m \) is transitive (@lem-omega-transitive (a)) and \( n \in m \), we get \( n \subseteq m \); so \( m \in n \subseteq m \), that is, \( m \in m \). This contradicts @lem-omega-transitive (c). Hence \( m = n \), by \( \rulename{RAA} \) (@def-rule-raa).

For the function: let \( G \coloneqq \{ p \in \omega \times \omega : p = (n, \mathrm{S}(n)) \text{ for some } n \in \omega \} \), a set by Separation (Z6) inside the product \( \omega \times \omega \) of @prp-cartesian-product-exists; the pairs \( (n, \mathrm{S}(n)) \) lie in that product by (P2). We check the two clauses of @def-function. (Fn1): for \( n \in \omega \), \( (n, \mathrm{S}(n)) \in G \). (Fn2): if \( (n, y) \in G \) and \( (n, y') \in G \), then \( (n, y) = (k, \mathrm{S}(k)) \) and \( (n, y') = (k', \mathrm{S}(k')) \) for some \( k, k' \in \omega \); by @thm-kuratowski-pair, \( k = n = k' \), and then \( y = \mathrm{S}(n) = y' \). So \( (G, \omega) \) is a function \( \omega \to \omega \), whose value at \( n \) is \( \mathrm{S}(n) \). It is injective by (P4) (@def-injective), and \( 0 \) is not a value by (P3). This proves the theorem.
:::

The function \( \mathrm{S} \colon \omega \to \omega \) and the operation \( x \mapsto \mathrm{S}(x) \) on all sets share a letter, and they agree wherever both are defined. Only the first is a set. The operation has no graph: a set containing the pair \( (x, \mathrm{S}(x)) = \{\{x\}, \{x, \mathrm{S}(x)\}\} \) for **every** set \( x \) would give, after two unions, a set containing every set, which @thm-russell forbids.

One more consequence is used constantly. By @lem-omega-transitive (d), every \( n \in \omega \) with \( n \ne 0 \) is \( \mathrm{S}(k) \) for some \( k \in \omega \), and by (P4) this \( k \) is **unique**: if \( \mathrm{S}(k) = n = \mathrm{S}(k') \), then \( k = k' \). So every non-zero natural number has exactly one predecessor, and \( 0 \) has none, by (P3).

::: {.check}
Is the function \( \mathrm{S} \colon \omega \to \omega \) surjective? Is \( \omega \in \omega \)?
:::

::: {.solution}
No to both. \( \mathrm{S} \) is not surjective: \( 0 \in \omega \), and by (P3) no \( n \in \omega \) has \( \mathrm{S}(n) = 0 \). (Every other natural number is a value, by @lem-omega-transitive (d).)

If \( \omega \in \omega \), then \( \omega \) would be a natural number \( n \) with \( n \in n \), which @lem-omega-transitive (c) rules out. So \( \omega \notin \omega \). In particular \( \omega \) is a set that is not a natural number, although all its elements are.
:::

## Peano systems

Chapter 7 worked with a set \( \nN \) of real numbers, and this chapter with a set \( \omega \) of sets. Both come with a starting element and a step. The last section of the chapter asks whether they are "the same", and to ask it we need to say what any such structure must satisfy. The answer is the list just proved, with \( \omega \), \( 0 \) and \( \mathrm{S} \) replaced by letters.

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

## Pairs are not natural numbers

Chapter 6 adopted a working convention, stated after @def-ordered-pair: a pair is not a number. In that chapter numbers were given and pairs were postulated, and the convention said they were different kinds of object. Now both are sets: a pair is the set \( \{\{a\}, \{a, b\}\} \) of @def-kuratowski-pair, and a natural number is an element of \( \omega \). For natural numbers the convention becomes a theorem.

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

So, for instance, the tagged numbers \( (n, 0) \) in the second example of a Peano system above are never natural numbers, and Chapter 6's answer that \( ((1, 2), 3) \ne (1, (2, 3)) \) because "a pair is not a number" is borne out by @prp-pair-not-natural once the numbers \( 1 \), \( 2 \), \( 3 \) are read as elements of \( \omega \), as the later chapters of this volume read \( \nN \) (Section 9.7). The same statement for \( n \)-tuples with \( n \ge 3 \) needs a definition of \( n \)-tuples, which comes later in this chapter, together with the order on \( \omega \).

::: {.warning}
The encoding produces true statements that sound absurd. Since \( \{0\} = 1 \) and \( \{0, 1\} = 2 \),
\[
(0, 1) = \{\{0\}, \{0, 1\}\} = \{1, 2\} ,
\]
so "\( 1 \in (0, 1) \)" is **true** of the pair \( (0, 1) \), although \( 1 \) is not in the open interval \( (0, 1) \) of real numbers, and "\( 0 \in (0, 1) \)" is **false** of the pair. Such a statement is a fact about how pairs were encoded as sets, not about pairs: with Wiener's encoding \( \{\{\{a\}, \emptyset\}, \{\{b\}\}\} \), met in Section 9.2 (@exr-pairs-as-sets-c3), the pair of \( 0 \) and \( 1 \) is \( \{2, \{\{1\}\}\} \), which does not have \( 1 \) as an element. A proof about pairs should use only their characteristic property, @thm-kuratowski-pair. The places in this section that look inside a pair (the remark after @thm-omega-peano that the operation \( x \mapsto \mathrm{S}(x) \) has no graph, the closing remark of the tagged-numbers example that \( (0, 0) = \{\{0\}\} \) is not \( \emptyset \), @prp-pair-not-natural, and this warning) are about the encoding itself.
:::

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

The only other admissible order exchanges (ix) and (iv), which use only (ii) and not each other. Everything else is forced: (v) needs both (ix) and (iv) to reduce each disjunction to its first alternative; (viii) needs the \( n \in m \) of (v); (i) needs the \( m \in n \) of (v) and the inclusion of (viii); (vi) closes the \( \rulename{RAA} \) box opened by (v), whose assumption is \( m \ne n \), the negation of the goal (@def-rule-raa).

The distractor (iii) cancels where no cancellation law exists. For sets in general, \( x \cup \{y\} = x' \cup \{y'\} \) does not give \( y = y' \): \( \{1\} \cup \{0\} = \{0\} \cup \{1\} \) with \( 0 \ne 1 \). For natural numbers the conclusion \( m = n \) happens to be true, but that is the statement being proved, not a reason for it.

The distractor (vii) cites a "fact" that is not available. No result so far says that \( m \in n \) and \( n \in m \) cannot both hold, and for natural numbers that is exactly what lines (viii), (i) and (vi) establish. Citing it is the circular step (N9) of @exm-not-allowed-catalogue: the line uses, as a reason, what the proof is there to show.
:::

::: {#exr-peano-properties-b2}
[B2: Two steps at a time]

Let \( d \coloneqq \mathrm{S} \circ \mathrm{S} \colon \omega \to \omega \) (@def-composition), so that \( d(n) = \mathrm{S}(\mathrm{S}(n)) \). Show that \( (\omega, 0, d) \) satisfies (P3) and (P4) of @def-peano-system, and that it does not satisfy (P5).

*Hint: look at the set \( \omega \setminus \{1\} \).*
:::

::: {.solution}
(P3): for \( n \in \omega \), \( d(n) = \mathrm{S}(\mathrm{S}(n)) \ne 0 \) by (P3) of @thm-omega-peano, applied to \( \mathrm{S}(n) \in \omega \).

(P4): if \( d(m) = d(n) \), then \( \mathrm{S}(\mathrm{S}(m)) = \mathrm{S}(\mathrm{S}(n)) \), so \( \mathrm{S}(m) = \mathrm{S}(n) \) by (P4) of @thm-omega-peano, and then \( m = n \) by (P4) again. (Equivalently: \( d \) is a composite of two injections, so it is injective by @thm-composition-injective-surjective (a).)

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

- **The data.** \( 1 \in M \), since \( 1 \in \omega \) and \( 1 \ne 0 \). For \( n \in M \), \( \mathrm{S}(n) \in \omega \) by (P2) and \( \mathrm{S}(n) \ne 0 \) by (P3) of @thm-omega-peano, so \( \mathrm{S}(n) \in M \). The graph \( \{ (n, \mathrm{S}(n)) : n \in M \} \) is a set by (Z6) inside \( M \times M \). (Fn1) holds, since \( (n, \mathrm{S}(n)) \) is in the graph for each \( n \in M \); (Fn2) holds as in the proof of @thm-omega-peano, by @thm-kuratowski-pair. So \( s \colon M \to M \) is a function (@def-function).
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
def-transitive-set (example): 0, 1, 2 are distinct; 1 = {0}, 2 = {0, 1}, 3 = {0, 1, 2} | exm-von-neumann-numerals (cited)
lem-omega-transitive (proof): y in S(n) iff y in n or y = n; n subset of S(n) | def-set-successor and the paragraph after it (inline)
lem-omega-transitive (proof): (d) the move "step without using the hypothesis" is valid | exm-predecessor-no-hypothesis (cited, Chapter 7)
thm-omega-peano (proof): (P3) a set with an element differs from the empty set | inline: =E of def-rules-equality and not-I of def-rules-negation (cited)
thm-omega-peano (claim): (the paragraph after it) a set containing (x, S(x)) for every x gives, after two unions, a set containing every set | inline: x in {x, S(x)} in (x, S(x)); thm-russell (cited)
def-peano-system (example): (tagged numbers) the graph of s is a set by (Z6) inside M x M | prp-cartesian-product-exists (cited)
exm-peano-axioms-independent (solution): 0, 1, 2 are three different sets, and 3 = {0, 1, 2} | exm-von-neumann-numerals (cited)
exm-peano-axioms-independent (claim): (the paragraph after the picture) reading (k, 2) as -(k + 1) | prose reading only; no integer arithmetic is used in any proof
prp-pair-not-natural (claim): (the paragraph after it) the n-tuple version, n >= 3 | prp-tuples-as-sets (e), later in this chapter (prose pointer; nothing in this section depends on it)
prp-pair-not-natural (claim): (the paragraph after it) Chapter 6's 1, 2, 3 read as elements of omega, as the later chapters read N | cor-omega-identification, Section 9.7 (prose pointer, this chapter; nothing in this section depends on it)
prp-pair-not-natural (claim): (the warning after it) {0} = 1 and {0, 1} = 2, so (0, 1) = {1, 2} | def-kuratowski-pair and exm-von-neumann-numerals (cited)
prp-pair-not-natural (claim): (the warning after it) Wiener's pair of 0 and 1 is {2, {{1}}}, and 1 is not an element of it | inline ({0} = 1, {0, emptyset} = 2; 1 != 2 and 1 != {{1}} since 0 in 1 and 0 not in {{1}}); the encoding itself is Section 9.2's exercise C3 (exr-pairs-as-sets-c3, cited only as a pointer; nothing here depends on it)
exr-peano-properties-a1 (solution): (d) 0 not in {1} since 0 != 1 | exm-von-neumann-numerals (cited)
exr-peano-properties-c2 (solution): every good set is one of G_0, R_m, L_k, M | needs thm-omega-well-ordering, later in this chapter (stated, not proved here; nothing depends on it)
-->
