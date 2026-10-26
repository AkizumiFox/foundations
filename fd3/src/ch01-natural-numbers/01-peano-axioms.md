# Peano's Axioms and Induction

*Sets and Functions*, Chapter 3 took the natural numbers as a subset \( \nN \) of the familiar real numbers, and borrowed the arithmetic of \( \nR \) whenever it was convenient. This volume builds the integers, the rationals and the real numbers. If we started from the \( \nN \) inside \( \nR \), the real numbers would rest on the real numbers. So we need \( \nN \) on its own. We make one assumption: there is a set with a start and a step that obey three rules. This section shows that each rule is needed, proves induction in the form we use, and proves that every natural number except \( 0 \) has exactly one predecessor.

## What counting needs

Two descriptions of \( \nN \) come to mind at once, and neither will do.

The first is \( \nN = \{0, 1, 2, 3, \dots\} \). It names four elements and then writes three dots, and the dots carry all the content. They say "keep going one at a time, and nothing else", and to say what that means is exactly the job of a definition of \( \nN \).

The second is more careful: \( \nN \) is the smallest subset of \( \nR \) that contains \( 0 \) and is closed under \( x \mapsto x + 1 \). A smallest such subset exists, by @fd2:prp-smallest-closed-set with start \( 0 \) and step \( x \mapsto x + 1 \), and the set form of @fd1:ax-induction shows that it is the \( \nN \) of *Sets and Functions*. Either way the description needs \( \nR \). Since \( \nR \) is where this volume is going, it cannot be where \( \nN \) comes from.

So we describe \( \nN \) by what counting has to do, not by where its elements live. Counting needs

- (P1) a **start**: an element where counting begins;
- (P2) a **step**: a rule sending each element to a next element of the same set.

That is a set \( M \), an element \( e \in M \), and a function \( s \colon M \to M \). A start and a step are not enough, and here are three ways they fail to count. In each picture an arrow goes from \( x \) to \( s(x) \).

**A loop.** Let \( M \coloneqq \{p, q, r\} \), start at \( p \), and step \( p \mapsto q \mapsto r \mapsto p \).

```{=latex}
\begin{center}
\begin{tikzpicture}[structure]
  \node[elt, label=below:$p$] (p) at (0,0) {};
  \node[elt, label=above:$q$] (q) at (1.6,1.2) {};
  \node[elt, label=below:$r$] (r) at (3.2,0) {};
  \draw[rel] (p) -- (q);
  \draw[rel] (q) -- (r);
  \draw[rel] (r) -- (p);
\end{tikzpicture}
\end{center}
```

Counting comes back to its start: three steps after \( p \) we are at \( p \) again, as on a clock.

**A merge.** Let \( M \coloneqq \{p, q, r\} \) again, start at \( p \), and step \( p \mapsto q \mapsto r \mapsto q \).

```{=latex}
\begin{center}
\begin{tikzpicture}[structure]
  \node[elt, label=below:$p$] (p) at (0,0) {};
  \node[elt, label=below:$q$] (q) at (1.6,0) {};
  \node[elt, label=below:$r$] (r) at (3.2,0) {};
  \draw[rel] (p) -- (q);
  \draw[rel] (q) to[bend left] (r);
  \draw[rel] (r) to[bend left] (q);
\end{tikzpicture}
\end{center}
```

Counting never returns to \( p \), but two different elements, \( p \) and \( r \), step to the same \( q \). After \( r \) the count repeats \( q \), and runs in a circle from there.

**An extra row.** Take the counting numbers, and beside them a second copy with its own step, which the start never reaches. Every element still has one next element, no two elements step to the same one, and nothing steps back to the start. Yet starting at the start and stepping, we never meet the second copy. Counting cannot see those elements, and a description of the natural numbers must exclude them.

Each failure is ruled out by one clause: the step never returns to the start; the step never sends two elements to the same one; and nothing is there that steps from the start cannot reach. The last clause needs care, since "reached by steps" is the three dots again. The way around it is the one @fd2:prp-smallest-closed-set takes: speak of subsets. A subset that contains the start and is closed under the step contains everything the steps reach. If the only such subset is the whole set, nothing is left over.

*A Peano system is a set with a start and a step, where the step is one-to-one, never returns to the start, and reaches everything.*

::: {#def-peano-system}
[Peano system]

A **Peano system** \( (M, e, s) \) consists of a set \( M \), an element \( e \in M \), and a function \( s \colon M \to M \), such that:

- (P3) \( s(x) \ne e \) for **every** \( x \in M \);
- (P4) \( s \) is injective;
- (P5) **every** subset \( A \subseteq M \) with \( e \in A \) and \( s(x) \in A \) for every \( x \in A \) is equal to \( M \).
:::

In words: (P1) and (P2) are built into the data, since \( e \in M \) and \( s \) maps \( M \) into \( M \). (P3) says the step never leads back to the start. (P4) says two different elements never step to the same element. (P5) is induction for \( M \): a subset that contains the start and is closed under the step is everything, so every element of \( M \) is reached from \( e \) by steps. We write \( (M, e, s) \) and not \( (N, e, s) \), so that the letter never suggests \( \nN \). The notation \( (M, e, s) \) lists the three pieces of data; it is not a set built from them (if one object is wanted, take the pair \( ((M, e), s) \) of @fd2:def-ordered-pair).

The merge breaks (P4), since \( s(p) = q = s(r) \) with \( p \ne r \). The extra row breaks (P5): the first copy contains the start, is closed under the step, and is not everything. The loop is the subject of the first Quick check.

::: {.check}
For the loop (\( M = \{p, q, r\} \), \( e = p \), \( s(p) = q \), \( s(q) = r \), \( s(r) = p \)), which of (P3), (P4), (P5) fail?
:::

::: {.solution}
Only (P3): \( s(r) = p = e \). (P4) holds, since the three values \( s(p) = q \), \( s(q) = r \), \( s(r) = p \) are different. (P5) holds: a subset containing \( p \) and closed under \( s \) contains \( s(p) = q \), then \( s(q) = r \), so it is \( M \).
:::

## The one assumption

The natural numbers are to be a Peano system. That is the whole of what we assume about them.

::: {#ax-natural-numbers}
[The Natural Numbers]

There is a Peano system.
:::

We fix one Peano system for the rest of the volume and write it \( (\nN, 0, \mathrm{S}) \). Its elements are the **natural numbers**, \( 0 \) is **zero**, and \( \mathrm{S}(n) \) is the **successor** of \( n \). Spelled out, \( \nN \) is a set, \( 0 \in \nN \), \( \mathrm{S} \colon \nN \to \nN \) is a function, and:

- (P3) \( \mathrm{S}(n) \ne 0 \) for every \( n \in \nN \);
- (P4) \( \mathrm{S}(m) = \mathrm{S}(n) \) implies \( m = n \);
- (P5) every \( A \subseteq \nN \) that contains \( 0 \) and is closed under \( \mathrm{S} \) is \( \nN \).

Why believe the assumption? If the school real numbers are trusted, the \( \nN \) of *Sets and Functions*, with start \( 0 \) and step \( x \mapsto x + 1 \), is a Peano system; Section 1.4 checks this. And *Axiomatic Set Theory* builds a Peano system from sets alone, assuming nothing about numbers; Section 1.5 describes how. Which Peano system we fix does not matter: Section 1.4 proves that any two are copies of each other, matched by exactly one bijection that sends start to start and step to step.

From here on, every fact about \( \nN \) is proved from @ax-natural-numbers. We do not borrow the order, the subtraction or the arithmetic of \( \nR \). Addition and multiplication are not defined yet; Section 1.2 defines them. Even the numeral \( 1 \) is not available until then, and the element after \( 0 \) is written \( \mathrm{S}(0) \).

Why these three clauses and no others? Each one does work that the other two cannot do: for each clause there is a structure satisfying the other two and failing it.

::: {#exm-peano-axioms-independent}
[Each axiom is needed]

Show that each of the following structures \( (M, e, s) \), with \( s \colon M \to M \), satisfies two of (P3), (P4), (P5) and fails the third.

::: {.enumerate options="label=(\roman*)"}
1. \( M \coloneqq \{0\} \), \( e \coloneqq 0 \), \( s(0) \coloneqq 0 \).
2. \( M \coloneqq \{0, 1\} \), \( e \coloneqq 0 \), \( s(0) \coloneqq 1 \), \( s(1) \coloneqq 1 \).
3. (**Two copies of \( \nN \).**) Let \( a \ne b \) be two objects, \( M \coloneqq \nN \times \{a, b\} \), \( e \coloneqq (0, a) \), and \( s(n, t) \coloneqq (\mathrm{S}(n), t) \) for \( n \in \nN \) and \( t \in \{a, b\} \).
:::
:::

::: {.solution}
(i) **Fails (P3)**: \( s(0) = 0 = e \). (P4) holds: \( M \) has one element, so two inputs with equal outputs are equal. (P5) holds: a subset of \( \{0\} \) containing \( e = 0 \) is \( \{0\} \).

(ii) **Fails (P4)**: \( s(0) = s(1) \) with \( 0 \ne 1 \). (P3) holds: both values are \( 1 \ne 0 = e \). (P5) holds: if \( A \subseteq \{0, 1\} \) has \( 0 \) as an element and is closed under \( s \), then \( s(0) = 1 \in A \), so \( A = \{0, 1\} \).

(iii) First, \( s \) is a function \( M \to M \). Each element of \( M \) is \( (n, t) \) for exactly one \( n \in \nN \) and one \( t \in \{a, b\} \), by @fd2:def-ordered-pair, so the formula names one value; and \( (\mathrm{S}(n), t) \in M \), since \( \mathrm{S} \) maps \( \nN \) into \( \nN \).

**(P3) holds.** If \( s(n, t) = (0, a) \), then \( (\mathrm{S}(n), t) = (0, a) \) gives \( \mathrm{S}(n) = 0 \) (@fd2:def-ordered-pair), against (P3) for \( \nN \).

**(P4) holds.** If \( s(n, t) = s(n', t') \), then \( (\mathrm{S}(n), t) = (\mathrm{S}(n'), t') \) gives \( t = t' \) and \( \mathrm{S}(n) = \mathrm{S}(n') \), so \( n = n' \) by (P4) for \( \nN \). Hence \( (n, t) = (n', t') \).

**(P5) fails.** Let \( A \coloneqq \nN \times \{a\} \). It contains \( e = (0, a) \), and it is closed under \( s \), since \( s(n, a) = (\mathrm{S}(n), a) \in A \). But \( (0, b) \in M \) is not in \( A \), because its second coordinate is \( b \ne a \). So \( A \ne M \).
:::

The picture shows (iii), with an arrow from each element to its image under \( s \).

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.85, every node/.style={font=\small}]
  \node (a0) at (0,1.5) {$(0,a)$};
  \node (a1) at (2.4,1.5) {$(\mathrm{S}(0),a)$};
  \node (a2) at (5.4,1.5) {$(\mathrm{S}(\mathrm{S}(0)),a)$};
  \node (ad) at (7.6,1.5) {$\cdots$};
  \draw[->] (a0) -- (a1);
  \draw[->] (a1) -- (a2);
  \draw[->] (a2) -- (ad);
  \node[above] at (a0.north) {$e$};
  \node (b0) at (0,0) {$(0,b)$};
  \node (b1) at (2.4,0) {$(\mathrm{S}(0),b)$};
  \node (b2) at (5.4,0) {$(\mathrm{S}(\mathrm{S}(0)),b)$};
  \node (bd) at (7.6,0) {$\cdots$};
  \draw[->] (b0) -- (b1);
  \draw[->] (b1) -- (b2);
  \draw[->] (b2) -- (bd);
\end{tikzpicture}
\end{center}
```

This is the extra row of the start of the section. The element \( (0, b) \) has no arrow coming in, and it is not \( e \). The top row is a copy of \( \nN \), and so is the bottom row; but the bottom row cannot be reached from \( e \). (P3) and (P4) cannot prevent this, and (P5) is the clause that says "nothing else".

(P5) speaks of **every** subset of \( M \), and that is what lets it exclude every kind of extra row. A first-order induction schema speaks only of subsets defined by formulas, and *Logic and Proof*, Section 7.6 showed (@fd1:exm-non-standard-naturals) that the sentences true in \( \nN \) also hold in a structure with an element beyond every numeral; its closing remark promised the comparison made here. Exercise C2 builds an extra row in which, unlike \( (0, b) \) above, every element has an arrow coming in.

## Induction in the form we use

(P5) is induction, stated about subsets of a Peano system. For \( \nN \) we record it in the two forms the rest of the volume cites: a set form, and a form about properties.

::: {#thm-omega-induction}
[Induction on \( \nN \)]

::: {.enumerate options="label=(\alph*)"}
1. (Set form.) Let \( A \subseteq \nN \). If \( 0 \in A \), and \( \mathrm{S}(n) \in A \) for every \( n \in A \), then \( A = \nN \).
2. (Property form.) Let \( P(n) \) be a property of natural numbers, possibly with other variables as parameters. If \( P(0) \) holds and, **for every** \( n \in \nN \), \( P(n) \) implies \( P(\mathrm{S}(n)) \), then \( P(n) \) holds **for every** \( n \in \nN \).
:::
:::

::: {.proof}
*(a)* This is (P5) of @def-peano-system for the Peano system \( (\nN, 0, \mathrm{S}) \) of @ax-natural-numbers.

*(b)* Let \( A \coloneqq \{ n \in \nN : P(n) \} \) (@fd2:def-set-builder). Then \( 0 \in A \), because \( P(0) \) holds. Let \( n \in A \). Then \( P(n) \), so \( P(\mathrm{S}(n)) \) by hypothesis, and \( \mathrm{S}(n) \in \nN \) because \( \mathrm{S} \) maps \( \nN \) into \( \nN \); hence \( \mathrm{S}(n) \in A \). By (a), \( A = \nN \), which says that \( P(n) \) holds for every \( n \in \nN \).
:::

Compare part (b) with the principle of induction, @fd1:ax-induction. Read with \( \mathrm{S}(n) \) in place of \( n + 1 \), the two statements are the same, and Section 1.2 shows that \( n + 1 = \mathrm{S}(n) \) once addition is defined. The difference lies in their status. In *Logic and Proof*, Chapter 4, induction was taken on trust, for an \( \nN \) that came with the school arithmetic attached. Here (P5) is part of the one assumption, and arithmetic is not assumed at all: Section 1.2 builds it, and proves its laws by this theorem.

::: {.warning}
**Both halves of the hypothesis are needed.** The set \( \nN \setminus \{0\} \) is closed under \( \mathrm{S} \), by (P3), and it is not \( \nN \). The set \( \{0\} \) contains \( 0 \) and is not closed under \( \mathrm{S} \), since \( \mathrm{S}(0) \ne 0 \).
:::

::: {.check}
Let \( P(n) \) be "\( n = 0 \)". Does the base case hold? Does the step hold? What does @thm-omega-induction (b) conclude?
:::

::: {.solution}
The base case holds: \( P(0) \) says \( 0 = 0 \). The step fails at \( n = 0 \): \( P(0) \) holds, while \( P(\mathrm{S}(0)) \) says \( \mathrm{S}(0) = 0 \), which is false by (P3). So the theorem concludes nothing, and indeed \( P \) fails at \( \mathrm{S}(0) \).
:::

## Every natural number except 0 has one predecessor

*Sets and Functions* used that \( n - 1 \in \nN \) for every natural number \( n \ne 0 \) (@fd2:lem-naturals-arithmetic (c)), with the subtraction done in \( \nR \). Our \( \nN \) has no subtraction. Yet Sections 1.2–1.4 split, again and again, into the cases "\( n = 0 \)" and "\( n = \mathrm{S}(k) \) for some \( k \)". For that we need every \( n \ne 0 \) to be a successor, and of exactly one \( k \). The fact holds in every Peano system, and we prove it there, because Section 1.4 uses it for systems other than \( \nN \).

::: {#prp-peano-predecessor}
[Predecessors in a Peano System]

Let \( (M, e, s) \) be a Peano system.

::: {.enumerate options="label=(\alph*)"}
1. For every \( x \in M \) with \( x \ne e \) there is **exactly one** \( y \in M \) with \( s(y) = x \).
2. \( s(x) \ne x \) for every \( x \in M \).
:::
:::

::: {.idea}
[Scratch work]

For (a), "at most one" is (P4): if \( s(y) = x = s(y') \), then \( y = y' \). "At least one" is the real question. Of the three clauses, only (P5) tells us anything about **all** elements of \( M \), and (P5) speaks of subsets. So we must choose a subset \( A \) of \( M \) and show \( A = M \). That choice is the new point. Inside an abstract \( M \) nothing can be computed: there is no subtraction that would produce \( y \) from \( x \).

The first candidate is the set of values of \( s \), \( \{ z \in M : z = s(y) \text{ for some } y \in M \} \). It fails at the start, since \( e \) is not a value, by (P3). The cure is the shape of @fd2:lem-naturals-arithmetic (c): carry "\( z = e \) or …".

| Givens | Goal |
|---|---|
| \( (M, e, s) \) a Peano system; \( x \in M \), \( x \ne e \) | some \( y \in M \) with \( s(y) = x \) |
| \( A \coloneqq \{ z \in M : z = e \text{ or } z = s(y) \text{ for some } y \in M \} \) | \( A = M \); then \( x \in A \) and \( x \ne e \) give \( y \) |
| (P5) for \( A \) | \( e \in A \); and \( z \in A \Rightarrow s(z) \in A \), since \( s(z) \) is a value of \( s \) |

The step never uses \( z \in A \), as in @fd2:exm-predecessor-no-hypothesis.
:::

::: {.idea}
Both parts apply (P5) to a subset chosen for the purpose: (a) to \( e \) together with the values of \( s \), and (b) to the set where \( s(x) \ne x \). In (b), unlike (a), the step uses its hypothesis, through (P4).
:::

::: {.proof}
*(a)* Let \( x \in M \) with \( x \ne e \). *At most one:* if \( s(y) = x \) and \( s(y') = x \), then \( y = y' \) by (P4). *At least one:* let
\[
A \coloneqq \{ z \in M : z = e \text{ or } z = s(y) \text{ for some } y \in M \}
\]
(@fd2:def-set-builder). Then \( e \in A \), by the first alternative. Let \( z \in A \). Then \( s(z) \in M \) is the value of \( s \) at \( z \), so \( s(z) \in A \), by the second alternative with \( y \coloneqq z \). By (P5), \( A = M \). Hence \( x \in A \); since \( x \ne e \), the second alternative holds, and \( x = s(y) \) for some \( y \in M \).

*(b)* Let \( A' \coloneqq \{ x \in M : s(x) \ne x \} \). Then \( e \in A' \), since \( s(e) \ne e \) by (P3). Let \( x \in A' \), so that \( s(x) \ne x \). If \( s(s(x)) = s(x) \), then (P4), applied to the inputs \( s(x) \) and \( x \), gives \( s(x) = x \), a contradiction. So \( s(s(x)) \ne s(x) \), that is, \( s(x) \in A' \). By (P5), \( A' = M \). This proves the proposition.
:::

For \( \nN \), part (a) says that every natural number \( n \ne 0 \) is \( \mathrm{S}(k) \) for exactly one \( k \in \nN \); this \( k \) is the **predecessor** of \( n \). Part (b) says that no natural number is its own successor.

The two proofs make the same move with one difference. In (a) the closure step proves \( s(z) \in A \) outright, whatever \( z \) is; in (b) it needs \( x \in A' \), and (P4) turns the hypothesis \( s(x) \ne x \) into the conclusion \( s(s(x)) \ne s(x) \). The move has a name.

::: {#exm-method-closed-subset}
[Method: induction through a closed subset]

**Template.** (1) Name \( A \coloneqq \{ x \in M : P(x) \} \). (2) Show \( e \in A \). (3) Take \( x \in A \) and show \( s(x) \in A \), using \( P(x) \) if needed. (4) Conclude \( A = M \) by (P5). If \( P \) fails at \( e \), carry "\( x = e \) or \( P(x) \)" (the shape of @fd2:lem-naturals-arithmetic (c)).

**When to use it.** A statement about every element of a Peano system whose elements are not known one by one: an abstract \( (M, e, s) \), the image of a map out of \( \nN \), a set of pairs.

**The usual failure.** A property false at \( e \). Closure checked only for elements of a special form (\( x = s(y) \)), forgetting \( e \). (P5) applied to a set that is not a subset of \( M \).
:::

On \( \nN \) the method is @thm-omega-induction (b), and @fd2:exm-method-induction-step still finds \( P(n) \) inside \( P(\mathrm{S}(n)) \) in the step; the box adds the choice of the set.

::: {.check}
In structure (ii) of @exm-peano-axioms-independent, which element has two predecessors, and which conclusions of @prp-peano-predecessor fail?
:::

::: {.solution}
The element \( 1 \): \( s(0) = 1 = s(1) \). So "exactly one" in (a) fails at \( x = 1 \), because (P4) fails; and (b) fails at \( x = 1 \), since \( s(1) = 1 \).
:::

::: {.check}
Does the loop (\( e = p \), \( s(p) = q \), \( s(q) = r \), \( s(r) = p \)) satisfy the conclusion of @prp-peano-predecessor (a)? What does the answer say about a converse?
:::

::: {.solution}
Yes. Every element, \( e \) included, has exactly one element stepping to it: \( r \) to \( p \), \( p \) to \( q \), \( q \) to \( r \). Yet the loop is not a Peano system, since it fails (P3). So the conclusion of (a) does not give back the axioms; Exercise C2 shows that it does not even together with (P3) and (P4).
:::

The next section uses (P3), (P4) and (P5) once each to prove that a function on \( \nN \) can be defined by recursion, and then defines addition and multiplication.

## Exercises

### A. Check your understanding

::: {#exr-peano-properties-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. For each of the three structures in @exm-peano-axioms-independent, which of (P3), (P4), (P5) fails?
2. In the proof of @prp-peano-predecessor (a), which axiom gives at least one \( y \), and which gives at most one?
3. Is \( \nN \setminus \{0\} \) closed under \( \mathrm{S} \)? Is it \( \nN \)? Which hypothesis of @thm-omega-induction (a) fails for it?
4. True or false: in a Peano system \( (M, e, s) \), the function \( s \) is a bijection \( M \to M \).
:::
:::

::: {.solution}
(a) (i) fails (P3); (ii) fails (P4); (iii) fails (P5). Each satisfies the other two (@exm-peano-axioms-independent).

(b) At least one comes from (P5), applied to the set \( A \) of elements that are \( e \) or a value of \( s \). At most one is (P4).

(c) Yes: for \( n \in \nN \setminus \{0\} \), \( \mathrm{S}(n) \in \nN \) and \( \mathrm{S}(n) \ne 0 \) by (P3). No: \( 0 \in \nN \) is not in it. The hypothesis that fails is \( 0 \in A \).

(d) False. The function \( s \) is injective, by (P4), but not surjective: \( e \) is not a value of \( s \), by (P3) (@fd2:def-surjective).
:::

### B. Practice

::: {#exr-peano-properties-b1}
[B1: Put the proof in order]

Let \( (M, e, s) \) be a Peano system. The following lines contain a proof that **\( s(s(x)) \ne x \) for every \( x \in M \)**, shuffled, together with two lines that do not belong. Write the six correct lines in an order that makes a proof, say which other orders are also admissible, and say why each of the other two lines fails.

(i) Let \( x \in A \); we show \( s(x) \in A \).

(ii) Let \( A \coloneqq \{ x \in M : s(s(x)) \ne x \} \).

(iii) Then \( s(s(x)) = x \) by (P4), contradicting \( x \in A \).

(iv) \( e \in A \), since \( s(s(e)) \) is a value of \( s \), so it is not \( e \), by (P3).

(v) Suppose \( s(s(s(x))) = s(x) \).

(vi) So \( s(s(s(x))) \ne s(x) \), that is, \( s(x) \in A \); by (P5), \( A = M \).

(vii) Since \( s \) is a bijection, write \( x = s(y) \) and apply the hypothesis to \( y \).

(viii) Since \( s(s(e)) \ne e \), and every element is reached from \( e \) by steps, \( s(s(x)) \ne x \) for every \( x \).
:::

::: {.solution}
An admissible order is (ii), (iv), (i), (v), (iii), (vi):

> Let \( A \coloneqq \{ x \in M : s(s(x)) \ne x \} \). Then \( e \in A \), since \( s(s(e)) \) is a value of \( s \), so it is not \( e \), by (P3). Let \( x \in A \); we show \( s(x) \in A \). Suppose \( s(s(s(x))) = s(x) \). Then \( s(s(x)) = x \) by (P4), contradicting \( x \in A \). So \( s(s(s(x))) \ne s(x) \), that is, \( s(x) \in A \); by (P5), \( A = M \).

Line (ii) comes first, since every other line mentions \( A \). Lines (i), (v), (iii), (vi) come in that order: (i) opens the closure step, (v) opens a supposition, (iii) applies (P4) to the inputs \( s(s(x)) \) and \( x \) and reaches a contradiction, and (vi) closes the supposition and applies (P5), which needs both \( e \in A \) and the closure step. So (iv) may stand anywhere after (ii) and before (vi); stating the base case first, as above, is the convention.

Line (vii) cites a false fact: \( s \) is not surjective, since \( e \) is not a value, by (P3). Citing an unavailable "fact" is (N9) of @fd1:exm-not-allowed-catalogue. Line (viii) is an "and so on" with nothing behind it: "every element is reached from \( e \) by steps" is (P5) only if the step from \( x \) to \( s(x) \) is proved, and line (viii) never proves it. That is (N13).
:::

::: {#exr-peano-properties-b2}
[B2: Two steps at a time]

Let \( d \coloneqq \mathrm{S} \circ \mathrm{S} \colon \nN \to \nN \) (@fd2:def-composition), so that \( d(n) = \mathrm{S}(\mathrm{S}(n)) \). Show that \( (\nN, 0, d) \) satisfies (P3) and (P4) of @def-peano-system, and that it does not satisfy (P5).

*Hint: look at the set \( \nN \setminus \{\mathrm{S}(0)\} \).*
:::

::: {.solution}
(P3): for \( n \in \nN \), \( d(n) = \mathrm{S}(\mathrm{S}(n)) \ne 0 \) by (P3) for \( \nN \), applied to \( \mathrm{S}(n) \in \nN \).

(P4): if \( d(m) = d(n) \), then \( \mathrm{S}(\mathrm{S}(m)) = \mathrm{S}(\mathrm{S}(n)) \), so \( \mathrm{S}(m) = \mathrm{S}(n) \) by (P4) for \( \nN \), and then \( m = n \) by (P4) again. (Equivalently: \( d \) is a composite of two injections, so it is injective by @fd2:thm-composition-injective-surjective (a).)

(P5) fails. Let \( A \coloneqq \nN \setminus \{\mathrm{S}(0)\} \). It contains \( 0 \), since \( 0 \ne \mathrm{S}(0) \) by (P3). It is closed under \( d \): let \( n \in A \); then \( d(n) \in \nN \), and \( d(n) \ne \mathrm{S}(0) \), because \( \mathrm{S}(\mathrm{S}(n)) = \mathrm{S}(0) \) would give \( \mathrm{S}(n) = 0 \) by (P4), against (P3). But \( A \ne \nN \), since \( \mathrm{S}(0) \in \nN \) and \( \mathrm{S}(0) \notin A \). So a subset of \( \nN \) with \( 0 \) as an element and closed under \( d \) need not be all of \( \nN \). The step \( d \) skips \( \mathrm{S}(0) \), and starting from \( 0 \) it meets only \( 0 \), \( \mathrm{S}(\mathrm{S}(0)) \), \( \mathrm{S}(\mathrm{S}(\mathrm{S}(\mathrm{S}(0)))) \), …: every second number.
:::

::: {#exr-peano-properties-b3}
[B3: Prove or disprove]

Let \( (M, e, s) \) be a Peano system. Prove or disprove each statement.

::: {.enumerate options="label=(\alph*)"}
1. If \( A \subseteq M \) contains \( s(e) \) and is closed under \( s \), then \( A \cup \{e\} = M \).
2. If \( A \subseteq M \) is non-empty and closed under \( s \), then \( A = M \).
3. Every \( x \ne e \) in \( M \) is \( s(y) \) for some \( y \in M \) with \( y \ne x \).
4. If \( f \colon M \to M \) satisfies \( f(e) = e \) and \( f(s(x)) = s(f(x)) \) for every \( x \in M \), then \( f = \id_M \).
5. Every \( x \in M \) is \( e \) or \( s(s(y)) \) for some \( y \in M \).
:::
:::

::: {.solution}
(a) **True.** The set \( A \cup \{e\} \) is a subset of \( M \) containing \( e \). It is closed under \( s \): for \( x = e \), \( s(e) \in A \) by hypothesis; for \( x \in A \), \( s(x) \in A \) by closure. By (P5), \( A \cup \{e\} = M \).

(b) **False.** Let \( A \coloneqq M \setminus \{e\} \). It contains \( s(e) \), since \( s(e) \ne e \) by (P3), so it is non-empty. It is closed under \( s \), since no value of \( s \) is \( e \), by (P3). It misses \( e \), so \( A \ne M \).

(c) **True.** Let \( x \ne e \). By @prp-peano-predecessor (a) there is \( y \in M \) with \( s(y) = x \). If \( y = x \), then \( s(x) = x \), against @prp-peano-predecessor (b). So \( y \ne x \).

(d) **True**, by @exm-method-closed-subset. Let \( A \coloneqq \{ x \in M : f(x) = x \} \). Then \( e \in A \), since \( f(e) = e \). If \( x \in A \), then \( f(s(x)) = s(f(x)) = s(x) \), so \( s(x) \in A \). By (P5), \( A = M \). So \( f \) and \( \id_M \) have the same domain, the same codomain and the same value at every \( x \in M \), and \( f = \id_M \) by @fd2:prp-function-equality.

(e) **False.** Take \( x \coloneqq s(e) \). It is not \( e \), by (P3). If \( s(e) = s(s(y)) \) for some \( y \in M \), then \( e = s(y) \) by (P4), against (P3). So \( s(e) \) is neither \( e \) nor of the form \( s(s(y)) \).
:::

### C. Going deeper

::: {#exr-peano-properties-c1}
[C1: A Peano system with a different start]

Give an example of a Peano system \( (M, e, s) \) with \( M \subseteq \nN \) and \( e \ne 0 \). Check every clause of @def-peano-system.
:::

::: {.solution}
Any correct answer has: a set \( M \subseteq \nN \); an element \( e \in M \) with \( e \ne 0 \); a function \( s \colon M \to M \), so that every value lies in \( M \); and the three clauses (P3), (P4), (P5) for these data.

Take \( M \coloneqq \nN \setminus \{0\} \), \( e \coloneqq \mathrm{S}(0) \), and \( s(n) \coloneqq \mathrm{S}(n) \) for \( n \in M \).

- **The data.** \( \mathrm{S}(0) \in M \), since \( \mathrm{S}(0) \in \nN \) and \( \mathrm{S}(0) \ne 0 \) by (P3) for \( \nN \). For \( n \in M \), \( \mathrm{S}(n) \in \nN \) since \( \mathrm{S} \) maps \( \nN \) into \( \nN \), and \( \mathrm{S}(n) \ne 0 \) by (P3) for \( \nN \), so \( \mathrm{S}(n) \in M \). So \( s \colon M \to M \) is a function, since \( \mathrm{S} \) is one and its values on \( M \) lie in \( M \) (@fd2:def-function).
- **(P3).** If \( s(n) = \mathrm{S}(0) \) for some \( n \in M \), then \( \mathrm{S}(n) = \mathrm{S}(0) \), so \( n = 0 \) by (P4) for \( \nN \); but \( 0 \notin M \).
- **(P4).** If \( \mathrm{S}(m) = \mathrm{S}(n) \) with \( m, n \in M \), then \( m = n \) by (P4) for \( \nN \).
- **(P5).** Let \( A \subseteq M \) with \( \mathrm{S}(0) \in A \) and \( \mathrm{S}(n) \in A \) for every \( n \in A \). The set \( A' \coloneqq A \cup \{0\} \subseteq \nN \) contains \( 0 \) and is closed under \( \mathrm{S} \): \( \mathrm{S}(0) \in A \subseteq A' \); and for \( n \in A \), \( \mathrm{S}(n) \in A \subseteq A' \). By @thm-omega-induction (a), \( A' = \nN \). Every \( n \in M \) lies in \( A' \) and is not \( 0 \), so \( n \in A \). Hence \( A = M \).

Other answers can be checked against the four properties at the start. For instance, \( M \coloneqq \nN \setminus \{0, \mathrm{S}(0)\} \), \( e \coloneqq \mathrm{S}(\mathrm{S}(0)) \), \( s(n) \coloneqq \mathrm{S}(n) \) also works, by the same argument with \( \{0, \mathrm{S}(0)\} \) added in (P5).
:::

::: {#exr-peano-properties-c2}
[C2: Every element but one is a successor, used later]

Let \( a, b, c \) be three different objects, \( M \coloneqq \nN \times \{a, b, c\} \), \( e \coloneqq (0, a) \), and, for \( n, k \in \nN \),
\[
\begin{aligned}
s(n, a) &\coloneqq (\mathrm{S}(n), a) , & s(n, b) &\coloneqq (\mathrm{S}(n), b) , \\
s(0, c) &\coloneqq (0, b) , & s(\mathrm{S}(k), c) &\coloneqq (k, c) .
\end{aligned}
\]

::: {.enumerate options="label=(\alph*)"}
1. Explain why \( s \) is a function \( M \to M \).
2. Show that \( (M, e, s) \) satisfies (P3) and (P4).
3. Show that every \( x \in M \) with \( x \ne e \) is a value of \( s \).
4. Show that \( (M, e, s) \) fails (P5).
5. Which conclusions of @prp-peano-predecessor hold in \( (M, e, s) \)?
:::
:::

::: {.solution}
[Hint 1]

For (a), apply @prp-peano-predecessor (a) to \( \nN \).
:::

::: {.solution}
[Hint 2]

For (d), try the set \( \nN \times \{a\} \).
:::

::: {.solution}
(a) Each element of \( M \) is \( (n, t) \) for exactly one \( n \in \nN \) and one \( t \in \{a, b, c\} \) (@fd2:def-ordered-pair). For \( t = a \) and \( t = b \), one formula applies and names one value. For \( t = c \), the first coordinate is \( 0 \) or \( \mathrm{S}(k) \) for some \( k \in \nN \), by @prp-peano-predecessor (a) for \( \nN \); never both, by (P3) for \( \nN \); and the \( k \) is unique. So exactly one line of the definition applies to each element, and it names one value. The values lie in \( M \), since \( \mathrm{S}(n), 0, k \in \nN \).

(b) Sort the values by their second coordinates (@fd2:def-ordered-pair):
\[
\begin{aligned}
&\text{second coordinate } a : && s(n, a) = (\mathrm{S}(n), a) , \\
&\text{second coordinate } b : && s(n, b) = (\mathrm{S}(n), b) \ \text{ and } \ s(0, c) = (0, b) , \\
&\text{second coordinate } c : && s(\mathrm{S}(k), c) = (k, c) .
\end{aligned}
\]

**(P3) holds.** A value equal to \( e = (0, a) \) would have second coordinate \( a \), so it would be \( (\mathrm{S}(n), a) \) with \( \mathrm{S}(n) = 0 \), against (P3) for \( \nN \).

**(P4) holds.** Suppose \( s(x) = s(x') \). The two values have the same second coordinate, so they come from the same row of the display. In the first row, \( (\mathrm{S}(n), a) = (\mathrm{S}(n'), a) \) gives \( n = n' \) by (P4) for \( \nN \). In the third row, \( (k, c) = (k', c) \) gives \( k = k' \), so \( \mathrm{S}(k) = \mathrm{S}(k') \). In the second row, \( (\mathrm{S}(n), b) \ne (0, b) \) because \( \mathrm{S}(n) \ne 0 \); so either both values are of the form \( (\mathrm{S}(n), b) \), and \( n = n' \) as before, or both are \( (0, b) \), and both inputs are \( (0, c) \). In every case \( x = x' \).

(c) Let \( x = (m, t) \ne e \). If \( t = a \), then \( m \ne 0 \), so \( m = \mathrm{S}(n) \) for some \( n \) (@prp-peano-predecessor (a) for \( \nN \)), and \( x = s(n, a) \). If \( t = b \), then \( x = (0, b) = s(0, c) \), or \( m = \mathrm{S}(n) \) and \( x = s(n, b) \). If \( t = c \), then \( x = (m, c) = s(\mathrm{S}(m), c) \).

(d) The set \( \nN \times \{a\} \) contains \( e \), is closed under \( s \), since \( s(n, a) = (\mathrm{S}(n), a) \), and misses \( (0, b) \), since \( b \ne a \). So it is a subset of \( M \) containing \( e \), closed under \( s \), and not equal to \( M \).

(e) Both. Part (a) of @prp-peano-predecessor holds: a predecessor exists by (c), and it is unique by (P4), proved in (b). Part (b) holds: \( (\mathrm{S}(n), a) \ne (n, a) \) and \( (\mathrm{S}(n), b) \ne (n, b) \), since \( \mathrm{S}(n) \ne n \) in \( \nN \) (@prp-peano-predecessor (b)); \( s(0, c) = (0, b) \ne (0, c) \), since \( b \ne c \); and \( s(\mathrm{S}(k), c) = (k, c) \ne (\mathrm{S}(k), c) \), since \( k \ne \mathrm{S}(k) \). So neither conclusion of the proposition gives back (P5), even together with (P3) and (P4).

The picture to keep in mind: the elements with second coordinate \( a \) form a copy of \( \nN \), starting at \( e \). The elements with second coordinates \( b \) and \( c \) form one chain running forever in both directions. Read \( (n, b) \) as "\( n \)" and \( (k, c) \) as "\( -(k + 1) \)": the step moves one place to the right everywhere, with \( (0, c) \), playing \( -1 \), stepping to \( (0, b) \), playing \( 0 \). Every element of the chain has an arrow coming in, and none of it is reached from \( e \).
:::

<!-- dependency ledger
ax-natural-numbers (claim): if the school reals are trusted, the N of Sets and Functions is a Peano system | F3.1 §04 cor-omega-identification (a) (prose pointer "Section 1.4 checks this"; not a reason)
ax-natural-numbers (claim): Axiomatic Set Theory builds a Peano system from sets | ST.1, described in F3.1 §05 (prose pointer; nothing here depends on it)
ax-natural-numbers (claim): any two Peano systems are matched by exactly one bijection respecting start and step | F3.1 §04 thm-peano-categoricity (prose pointer; nothing here depends on it)
thm-omega-induction (claim): (the paragraph after it) n + 1 = S(n) once addition is defined | F3.1 §02 def-omega-arithmetic (c) (prose pointer; nothing in this section depends on it)
exm-peano-axioms-independent (claim): (the paragraph after the picture) the sentences true in N hold in a structure with a non-standard element; a first-order schema speaks only of definable subsets | fd1:exm-non-standard-naturals (cited) and the Looking ahead closing F1.7 §06 (prose only)
exr-peano-properties-b2 (solution): d reaches only every second number | prose description only; parity is defined in F3.1 §03 and nothing uses this sentence
exr-peano-properties-c2 (solution): reading (k, c) as -(k + 1) | prose reading only; no integer arithmetic is used in any proof
-->
