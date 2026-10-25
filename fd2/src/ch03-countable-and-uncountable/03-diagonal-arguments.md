# Diagonal Arguments: Uncountable Sets and Cantor's Theorem

Every infinite set met so far has turned out to be countable: \( \nN \), \( \nZ \), \( \nQ \), finite products of countable sets, countable unions of them (@thm-countable-union), and even the algebraic numbers (@thm-algebraic-countable). Is every infinite set countable? This section shows that the answer is no, by one argument, which starts from the game of Section 1.5 and is then used three times. Given any list, it builds an object that the list misses. The argument proves that the set of 0–1 sequences is uncountable, that no set can be mapped onto the set of its subsets (Cantor's theorem), and, with decimals, that \( \nR \) is uncountable.

## Back to the five strings

Section 1.5 left a game open: one player lists five strings of five symbols \( 0 \) or \( 1 \), and the other must write a string that is not on the list. Searching all \( 32 \) strings works; a rule is better.

::: {#exm-five-strings-diagonal}
[Back to the five strings]

Find a rule that, from any list \( s_1, \dots, s_5 \) of strings of five symbols \( 0 \) or \( 1 \), builds a string not on the list. Run it on \( 00000 \), \( 11111 \), \( 01010 \), \( 10101 \), \( 00111 \), and prove that it always works.
:::

::: {.solution}
Let the new string \( g \) have, as its \( k \)-th symbol, the flip of the \( k \)-th symbol of the \( k \)-th string:
\[
g(k) \coloneqq 1 - s_k(k) \qquad (k = 1, \dots, 5)
\]
(strings are functions \( \{1, \dots, 5\} \to \{0, 1\} \), Section 1.5). On the given list, the symbols \( s_1(1), \dots, s_5(5) \) are \( 0, 1, 0, 0, 1 \), so \( g = 10110 \). It differs from \( 00000 \) in place \( 1 \), from \( 11111 \) in place \( 2 \), from \( 01010 \) in place \( 3 \), from \( 10101 \) in place \( 4 \) and from \( 00111 \) in place \( 5 \).

For any list: for each \( k \), \( g(k) \ne s_k(k) \), since \( 1 - b \ne b \) for \( b \in \{0, 1\} \). So \( g \ne s_k \) (@prp-function-equality), for \( k = 1, \dots, 5 \). The \( k \)-th step looks only at the \( k \)-th string, in its own place \( k \).
:::

The rule never used the number \( 32 \). It used one place for each string on the list. Give the strings infinitely many places, indexed by \( \nN \), and let the list be infinite too, and the same rule still applies.

::: {.check}
Can the rule handle a list of six strings of five symbols? Does that contradict anything?
:::

::: {.solution}
No. The sixth string has no sixth place to be flipped in. Nothing is contradicted: a list of \( 32 \) strings may contain every string. The rule needs as many places as strings, and in the next subsection both are indexed by \( \nN \).
:::

## A sequence that is not on the list

Recall from Section 1.5 that \( \{0, 1\}^{\nN} \) is the set of all functions \( \nN \to \{0, 1\} \): the sequences of zeros and ones, indexed from \( 0 \). These are the strings of the game with places indexed by \( \nN \). It is infinite, and it looks no bigger than \( \nN \times \nN \), which is countable. To show that it is **not** countable we must show, by @def-countable, that it is non-empty and that **no** function \( f \colon \nN \to \{0, 1\}^{\nN} \) is onto. So we take an arbitrary list \( f(0), f(1), f(2), \dots \) of sequences and look for a sequence that is not on it.

Write the list as a table: row \( n \) is the sequence \( f(n) \), and the entry in row \( n \) and column \( k \) is the number \( f(n)(k) \). Here is the start of one such table, with the entries in places \( (0, 0), (1, 1), (2, 2), (3, 3) \) boxed:

\begin{center}
\begin{tikzpicture}[x=0.85cm, y=0.62cm]
  \node at (-1.2, 1) {place};
  \foreach \k in {0,1,2,3,4} { \node at (\k, 1) {$\k$}; }
  \node at (5, 1) {$\cdots$};
  \node at (-1.2, 0) {$f(0)$};
  \node at (0, 0) {$0$}; \node at (1, 0) {$1$}; \node at (2, 0) {$0$}; \node at (3, 0) {$1$}; \node at (4, 0) {$0$}; \node at (5, 0) {$\cdots$};
  \node at (-1.2, -1) {$f(1)$};
  \node at (0, -1) {$1$}; \node at (1, -1) {$1$}; \node at (2, -1) {$1$}; \node at (3, -1) {$1$}; \node at (4, -1) {$1$}; \node at (5, -1) {$\cdots$};
  \node at (-1.2, -2) {$f(2)$};
  \node at (0, -2) {$0$}; \node at (1, -2) {$0$}; \node at (2, -2) {$0$}; \node at (3, -2) {$0$}; \node at (4, -2) {$0$}; \node at (5, -2) {$\cdots$};
  \node at (-1.2, -3) {$f(3)$};
  \node at (0, -3) {$1$}; \node at (1, -3) {$0$}; \node at (2, -3) {$0$}; \node at (3, -3) {$1$}; \node at (4, -3) {$1$}; \node at (5, -3) {$\cdots$};
  \node at (-1.2, -4) {$\vdots$};
  \foreach \n in {0,1,2,3} { \draw (\n-0.35, -\n-0.4) rectangle (\n+0.35, -\n+0.4); }
  \node at (-1.2, -5.2) {$g$};
  \node at (0, -5.2) {$1$}; \node at (1, -5.2) {$0$}; \node at (2, -5.2) {$1$}; \node at (3, -5.2) {$0$}; \node at (5, -5.2) {$\cdots$};
\end{tikzpicture}
\end{center}

The boxed entries run down the **diagonal** of the table. The bottom row \( g \) is the diagonal with every entry flipped: \( g(n) = 1 - f(n)(n) \). It cannot be row \( 0 \), because it differs from \( f(0) \) in place \( 0 \); it cannot be row \( 1 \), because it differs from \( f(1) \) in place \( 1 \); and so on down the table. Nothing in this reasoning used the particular entries.

::: {#thm-binary-sequences-uncountable}
[The 0–1 Sequences Are Uncountable]

The set \( \{0, 1\}^{\nN} \) of all sequences of zeros and ones is uncountable.
:::

::: {.idea}
[Scratch work]

By @def-countable, "uncountable" has two parts: the set is non-empty, and no map from \( \nN \) onto it exists. The second is a statement about **every** \( f \), so take \( f \) arbitrary and look for a sequence it misses. As givens and goal:

| Givens | Goal |
|---|---|
| \( f \colon \nN \to \{0, 1\}^{\nN} \) arbitrary | \( f \) is not onto; and \( \{0, 1\}^{\nN} \ne \emptyset \) |
| — | some \( g \in \{0, 1\}^{\nN} \) with \( g \ne f(n) \) for every \( n \) |
| \( g \ne f(n) \) as soon as \( g \) and \( f(n) \) differ at one place (@prp-function-equality) | pick the place for each \( n \): place \( n \), as in the game |
| gap: \( g(n) \ne f(n)(n) \) for every \( n \) | closed by \( g(n) \coloneqq 1 - f(n)(n) \) |

The proof writes this forwards.
:::

::: {.proof}
Let \( f \colon \nN \to \{0, 1\}^{\nN} \) be any function. Define \( g \colon \nN \to \{0, 1\} \) by
\[
g(n) \coloneqq 1 - f(n)(n) \qquad (n \in \nN) ;
\]
its values lie in \( \{0, 1\} \), since \( 1 - 0 = 1 \) and \( 1 - 1 = 0 \). So \( g \in \{0, 1\}^{\nN} \). For every \( n \in \nN \), \( g(n) \ne f(n)(n) \), since no \( b \in \{0, 1\} \) has \( 1 - b = b \). Hence \( g \ne f(n) \): if \( g = f(n) \), then \( g(n) = f(n)(n) \), which is false; the two functions differ at place \( n \) [\( \rulename{{=}E} \), \( \rulename{\neg I} \); @prp-function-equality]. So \( g \) is not a value of \( f \), and \( f \) is not surjective. Since \( f \) was arbitrary, no function \( \nN \to \{0, 1\}^{\nN} \) is surjective. The set \( \{0, 1\}^{\nN} \) is non-empty, since it contains the zero sequence. By @def-countable, \( \{0, 1\}^{\nN} \) is not countable.
:::

This is the move of the section.

::: {#exm-method-diagonal}
[Method: the diagonal]

**Template.** To show that no map from \( I \) onto \( X \) exists (for "uncountable": \( I = \nN \), and check \( X \ne \emptyset \)), let \( f \colon I \to X \) be arbitrary. Build \( d \in X \) whose entry at \( i \) differs from the entry of \( f(i) \) at \( i \), for every \( i \in I \). Then \( d \ne f(i) \) for each \( i \), so \( f \) is not onto. Since \( f \) was arbitrary, no such map exists.

**When to use it.** The elements of \( X \) are themselves functions or subsets on the index set of the list: sequences, digit strings, subsets of \( I \).

**The usual failure.** A \( d \) that falls outside \( X \) (a decimal ending in \( 9 \)s, met below; a sequence of the wrong kind). A difference at place \( i \) that is not a real difference (two expansions of one number). Running the construction on one list only (the warning below).
:::

::: {.check}
Would the unflipped diagonal, \( g(n) \coloneqq f(n)(n) \), do? Test it on the list whose every entry is the zero sequence.
:::

::: {.solution}
No. There \( g \) is the zero sequence, which is \( f(0) \). The new object must differ from the \( n \)-th entry at place \( n \), for every \( n \).
:::

::: {.check}
Run the proof on the list \( f(n) \coloneqq \ind_{\{n\}} \), the sequence with a \( 1 \) in place \( n \) and \( 0 \) elsewhere. What is \( g \)? Is it on the list?
:::

::: {.solution}
Here \( f(n)(n) = \ind_{\{n\}}(n) = 1 \) for every \( n \), so \( g(n) = 1 - 1 = 0 \) for every \( n \): \( g \) is the zero sequence. It is indeed not on the list, since every \( f(n) \) has a \( 1 \) in place \( n \).
:::

::: {.warning}
**The diagonal object depends on the list.** "The diagonal sequence" is not one sequence: each list has its own, and a different list may well contain the \( g \) built from this one (the list \( g, f(0), f(1), \dots \) does). And the conclusion "uncountable" needs the list to be **arbitrary**. Running the construction on one list, or on a few, shows only that those lists miss something; concluding "so no list works" from them is the error (N1) of @fd1:exm-not-allowed-catalogue. The proof above starts from "let \( f \) be **any** function", and that is what makes its conclusion universal.
:::

::: {#exm-diagonal-outgrows-list}
[A function that outgrows a list]

Let \( f_0, f_1, f_2, \dots \) be any list of functions \( \nN \to \nN \). Find \( g \colon \nN \to \nN \) such that, for every \( k \in \nN \), \( g(n) > f_k(n) \) for every \( n \ge k \).
:::

::: {.solution}
*Idea.* The flipped diagonal beats \( f_n \) at place \( n \) only. To beat \( f_k \) from place \( k \) on, let place \( n \) beat \( f_0, \dots, f_n \) at once: finitely many, so a maximum exists.

Let
\[
g(n) \coloneqq \max \{ f_0(n), \dots, f_n(n) \} + 1 \qquad (n \in \nN) .
\]
The set is \( \{x_1, \dots, x_{n+1}\} \) with \( x_{k+1} \coloneqq f_k(n) \), so the maximum exists by @prp-finite-max; it is one of the \( x_j \), so \( g(n) \in \nN \). For \( k \in \nN \) and \( n \ge k \), \( f_k(n) \) is one of the numbers in the set, so \( f_k(n) \le \max \{ f_0(n), \dots, f_n(n) \} < g(n) \). The example asks more of \( g \) than a diagonal does, and each step still looks at finitely many entries at one place.
:::

## Back to Russell: Cantor's theorem

Section 1.2 proved Russell's theorem (@thm-russell): the set \( R_A \) disagrees with each candidate \( x \in A \) about \( x \) itself, so it is not in \( A \). Here the same disagreement becomes a theorem about sizes.

The table had a row for each \( n \in \nN \) and a column for each place \( k \in \nN \). Nothing about the diagonal needs the rows and the columns to be indexed by \( \nN \): it needs only that they are indexed by the **same** set. A subset \( S \) of a set \( X \) is a row with one entry for each \( x \in X \), "in" or "out", the values of \( \ind_S \). So the argument applies to any set and the set of its subsets.

::: {#thm-cantor}
[Cantor's Theorem]

Let \( X \) be a set. Then there is **no** surjection \( X \to \powerset{X} \).
:::

*Try it first (ten minutes): given a function \( f \colon X \to \powerset{X} \), which subset of \( X \) could be missed by \( f \)? Try \( X = \{1, 2, 3\} \) with a function of your own first.*

::: {.idea}
The first attempts look for a subset that is "too big" or "too small" to be a value, such as \( X \) itself or \( \emptyset \), and fail: \( f \) may well take both values. Size is the wrong idea. A set \( D \) differs from \( f(x) \) as soon as the two disagree about **one** element, and the only element we know anything about in connection with \( f(x) \) is \( x \) itself. So we make \( D \) disagree with \( f(x) \) at \( x \): put \( x \) into \( D \) exactly when \( x \notin f(x) \). This is the diagonal of the table, flipped. It is the method of @exm-method-diagonal, with the rows and the places both indexed by \( X \).

*Before reading on: where is surjectivity used?*
:::

::: {.proof}
Let \( f \colon X \to \powerset{X} \) be a function, and let
\[
D \coloneqq \{ x \in X : x \notin f(x) \} ,
\]
a subset of \( X \) by @def-set-builder, so \( D \in \powerset{X} \) (@def-power-set). Suppose \( f \) is surjective. Then there is \( d \in X \) with \( f(d) = D \) (@def-surjective). If \( d \in D \), then \( d \notin f(d) \) by the definition of \( D \), that is, \( d \notin D \), a contradiction. Hence \( d \notin D \). Then \( d \notin f(d) \), and since \( d \in X \), the definition of \( D \) gives \( d \in D \), a contradiction again. So \( f \) is not surjective. This proves the theorem.
:::

Surjectivity was used once, to obtain \( d \); everything else holds for every function \( f \). Read without the supposition, the proof shows that \( D \ne f(x) \) for **every** \( x \in X \): the two sets disagree about \( x \). Three consequences follow.

(i) *Russell's theorem is the same argument.* In @thm-russell, the set \( R_A = \{ x \in A : x \notin x \} \) is the set \( D \) built from the rule \( f(x) \coloneqq x \): each \( x \in A \) is tested against itself. The proof that \( D \) differs from every \( f(x) \) becomes the proof that \( R_A \) differs from every element of \( A \), that is, \( R_A \notin A \). (The rule \( x \mapsto x \) need not map into \( \powerset{A} \), but the argument never used that \( f(x) \subseteq X \), only the test "\( x \in f(x) \)".)

(ii) *The power set is strictly bigger.* The map \( x \mapsto \{x\} \) is an injection \( X \to \powerset{X} \), since \( \{x\} = \{y\} \) gives \( x = y \). So \( \powerset{X} \) has at least as many elements as \( X \), in the sense that \( X \) is in bijection with a subset of it, and by the theorem it is not equinumerous with \( X \), since a bijection would be a surjection. Section 3.4 names this relation: \( X \) is strictly smaller than \( \powerset{X} \).

(iii) *There is no largest size.* \( \nN \), \( \powerset{\nN} \), \( \powerset{\powerset{\nN}} \), …: each set in this sequence is strictly bigger than the one before.

::: {#cor-powerset-naturals-uncountable}
[The Subsets of the Naturals]

The power set \( \powerset{\nN} \) is uncountable.
:::

::: {.proof}
The set \( \powerset{\nN} \) is non-empty, since \( \emptyset \in \powerset{\nN} \), and by @thm-cantor with \( X = \nN \) there is no surjection \( \nN \to \powerset{\nN} \). By @def-countable, \( \powerset{\nN} \) is not countable.
:::

The two diagonal proofs are one. By the correspondence of Section 1.5, \( S \mapsto \ind_S \) is a bijection \( \powerset{\nN} \to \{0, 1\}^{\nN} \), with inverse \( b \mapsto \{ n \in \nN : b(n) = 1 \} \) (@thm-bijection-iff-inverse). Given \( f \colon \nN \to \powerset{\nN} \), the sequence \( g(n) = 1 - \ind_{f(n)}(n) \) of @thm-binary-sequences-uncountable is \( 1 \) exactly when \( n \notin f(n) \), so \( g = \ind_D \) for the set \( D \) of Cantor's proof.

## Decimal expansions

The real numbers should be next. A real number in \( [0, 1) \) is written as a decimal \( 0.d_1 d_2 d_3 \ldots \), a sequence of digits, so the diagonal suggests itself: list the numbers, write their decimals as the rows of a table, and change the diagonal digits. Two questions must be answered first. What does it **mean** that a sequence of digits is the decimal of \( x \)? And what is \( 0.999\ldots \)? School says it equals \( 1 \), and a diagonal that produces \( 0.4999\ldots \) when \( 0.5000\ldots \) is on the list has produced a number that is on the list.

An infinite sum would answer the first question, but this book has not yet defined one. Finite sums are enough. The first \( n \) digits of \( x \) should pin \( x \) down to within \( 10^{-n} \).

*A digit sequence is a decimal of \( x \) when each of its finite truncations is within one unit of its last place below \( x \).*

::: {#def-decimal-expansion}
[Decimal Expansion]

A **digit sequence** is a function \( k \mapsto d_k \) from \( \nZ_{>0} \) to \( \{0, 1, \dots, 9\} \). For \( n \ge 1 \) let
\[
t_n \coloneqq \sum_{k=1}^{n} d_k 10^{-k}
\]
(@def-sum-product), where \( 10^{-k} \coloneqq (1/10)^k \) (@def-power). The digit sequence is a **decimal expansion** of \( x \in [0, 1] \) if **for every** \( n \ge 1 \),
\[
t_n \le x \le t_n + 10^{-n} .
\]
:::

In words: \( t_n \) is the number written with the first \( n \) digits, \( 0.d_1 \ldots d_n \), and the condition says that \( x \) lies in the closed interval of length \( 10^{-n} \) starting at \( t_n \), for every \( n \). The digits are indexed from \( 1 \), so that \( d_k \) is the digit in the \( k \)-th place after the point. No infinite sum appears: every \( t_n \) is a finite sum.

**Examples.**

1. *Zero.* The all-zero sequence has \( t_n = 0 \), and \( 0 \le 0 \le 10^{-n} \); it is an expansion of \( 0 \).
2. *One half, twice.* The sequence \( 5, 0, 0, \dots \) has \( t_n = \frac12 \) for every \( n \ge 1 \), and \( \frac12 \le \frac12 \le \frac12 + 10^{-n} \). The sequence \( 4, 9, 9, \dots \) has \( t_n = \frac{4}{10} + \sum_{k=2}^{n} 9 \cdot 10^{-k} = \frac12 - 10^{-n} \), by @prp-geometric-sum, so \( t_n \le \frac12 \le t_n + 10^{-n} = \frac12 \). Both are expansions of \( \frac12 \).
3. *One.* The all-nine sequence has \( t_n = \sum_{k=1}^{n} 9 \cdot 10^{-k} = 1 - 10^{-n} \) (@prp-geometric-sum), so \( t_n \le 1 \le t_n + 10^{-n} = 1 \): it is an expansion of \( 1 \).

**A non-example by minimal change.** Keep the sequence \( 5, 0, 0, \dots \) and move \( x \) from \( \frac12 \) to \( 0.51 \). The inequalities still hold for \( n = 1 \) (\( 0.5 \le 0.51 \le 0.6 \)) and for \( n = 2 \) (\( 0.50 \le 0.51 \le 0.51 \)), and they fail at \( n = 3 \): \( 0.51 > 0.500 + 0.001 \). So \( 5, 0, 0, \dots \) is not an expansion of \( 0.51 \); the clause "for every \( n \ge 1 \)" is what fails.

**Why this definition.** Both inequalities are non-strict. With a strict right inequality, \( x < t_n + 10^{-n} \), the all-nine sequence would be an expansion of no number at all: it would need \( x < 1 \) together with \( 1 - 10^{-n} \le x \) for every \( n \), and no real number satisfies both, by the Archimedean property (a school fact; *Analysis on the Real Line*, Chapter 1 proves it). The non-strict form is what makes \( 0.999\ldots = 1 \) true, and true **by the definition**: the inequalities for \( x = 1 \) are checked in Example 3, and no other number satisfies them, since \( 1 - 10^{-n} \le x \le 1 \) for every \( n \) forces \( x = 1 \), again by the Archimedean property (this is the uniqueness half of (D2) below). Example 2 shows that the price is two expansions for some numbers.

What this book does not prove are the facts that make expansions behave as school says. We state them once and use them in this section and the next, always by name.

::: {.enumerate options="label=(D\arabic*)"}
1. Every \( x \in [0, 1) \) has a decimal expansion that does **not** end in all \( 9 \)s.
2. Every digit sequence is a decimal expansion of **exactly one** \( x \in [0, 1] \).
3. If two **different** digit sequences are expansions of the same \( x \), then one of them ends in all \( 9 \)s and the other ends in all \( 0 \)s.
:::

Here a digit sequence **ends in all \( 9 \)s** if there is \( N \ge 1 \) with \( d_k = 9 \) for every \( k \ge N \), and likewise for \( 0 \)s. By the uniqueness in (D2), we may write \( x = 0.d_1 d_2 d_3 \ldots \) for "\( x \) is the number of which \( d_1, d_2, d_3, \dots \) is an expansion". So \( 0.4999\ldots = 0.5000\ldots = \frac12 \), as in (D3).

Neither (D1) nor (D2) follows from what we have so far. (D3) does, by a finite computation at the first place where the two sequences differ (@thm-well-ordering, @prp-geometric-sum); we state it with the others to quote it by name. The **existence** half of (D2), that some \( x \) satisfies all the inequalities at once, is where the completeness of \( \nR \) hides, and *Analysis on the Real Line*, Chapter 1 takes completeness as an axiom. The **uniqueness** half of (D2) and the "not ending in all \( 9 \)s" of (D1) rest on the Archimedean property: two numbers \( x, x' \) with \( \abs{x - x'} \le 10^{-n} \) for every \( n \) must be equal, which *Analysis on the Real Line*, Chapter 1 also proves. Until then we use them as school facts, and each use names the fact it uses.

One consequence is used below. *A digit sequence with no digit \( 0 \) and no digit \( 9 \) is the **only** expansion of its number.* Indeed, by (D3) a second expansion of the same number would force one of the two to end in all \( 9 \)s and the other in all \( 0 \)s; the given sequence ends in neither, since it has no \( 9 \)s and no \( 0 \)s at all.

## The real numbers are uncountable

With the facts in hand, the diagonal runs on digits. Two precautions are built in. Each number on the list gets its expansion by a **rule**, so that no choosing is needed. And the new digits avoid \( 0 \) and \( 9 \), so that the new number has only one expansion.

::: {#thm-reals-uncountable-decimal}
[The Reals Are Uncountable, by Decimals]

The interval \( [0, 1) \) is uncountable. Hence \( \nR \) is uncountable.
:::

::: {.idea}
Take an arbitrary list of numbers in \( [0, 1) \), write each as its expansion with no tail of \( 9 \)s, and change the \( n \)-th digit of the \( n \)-th number to \( 4 \) or \( 5 \). The resulting digit sequence is an expansion of some \( y \), by (D2). If \( y \) were the \( n \)-th number, it would have two different expansions, one with no \( 0 \)s or \( 9 \)s, against (D3).
:::

::: {.proof}
Let \( f \colon \nN \to [0, 1) \) be any function. For \( n \ge 1 \) let \( x_n \coloneqq f(n - 1) \), so that the list \( x_1, x_2, x_3, \dots \) has the same values as \( f \).

For each \( n \ge 1 \), \( x_n \) has an expansion not ending in all \( 9 \)s, by (D1), and only one: by (D3), two different such expansions would include one ending in all \( 9 \)s. Let \( (d_{n,k})_{k \ge 1} \) be this expansion. It is named by a rule, "the expansion of \( x_n \) not ending in all \( 9 \)s", so no choice is involved. Define a digit sequence by
\[
e_n \coloneqq
\begin{cases}
5 & \text{if } d_{n,n} \ne 5, \\
4 & \text{if } d_{n,n} = 5,
\end{cases}
\qquad (n \ge 1) .
\]
Then \( e_n \ne d_{n,n} \) for every \( n \ge 1 \). By (D2), there is \( y \in [0, 1] \) of which \( (e_k)_{k \ge 1} \) is an expansion. Its first truncation is \( t_1 = e_1/10 \in \{0.4, 0.5\} \), so \( 0.4 \le t_1 \le y \le t_1 + 0.1 \le 0.6 \), and in particular \( y \in [0, 1) \).

Let \( n \ge 1 \), and suppose \( y = x_n \). Then \( (e_k) \) and \( (d_{n,k}) \) are both expansions of \( y \), and they are different, since they differ in place \( n \). But \( (e_k) \) has no digit \( 0 \) and no digit \( 9 \), so by the consequence of (D3) stated above it is the **only** expansion of \( y \), a contradiction. So \( y \ne x_n \) for every \( n \ge 1 \), and \( y \) is not a value of \( f \). Since \( f \) was arbitrary, no function \( \nN \to [0, 1) \) is surjective; and \( [0, 1) \) is non-empty, since it contains \( 0 \). By @def-countable, \( [0, 1) \) is not countable.

Finally, if \( \nR \) were countable, its subset \( [0, 1) \) would be countable by @prp-countable-subset. So \( \nR \) is uncountable.
:::

**Why the digits \( 4 \) and \( 5 \).** The first rule that comes to mind is \( e_n \coloneqq 9 - d_{n,n} \), which also changes every diagonal digit. Run it on the list \( x_1 = \frac12 \), \( x_n = 0 \) for \( n \ge 2 \) (that is, \( f(0) = \frac12 \) and \( f(n) = 0 \) for \( n \ge 1 \)). The expansions are \( 0.5000\ldots \) and \( 0.000\ldots \), so \( d_{1,1} = 5 \) and \( d_{n,n} = 0 \) for \( n \ge 2 \). The naive rule produces \( e_1 = 4 \) and \( e_n = 9 \) for \( n \ge 2 \): the sequence \( 0.4999\ldots \), which is an expansion of \( \frac12 = x_1 \) by Example 2. The new digit sequence differs from every row, and its number is on the list. The rule with \( 4 \) and \( 5 \), on the same list, gives \( 0.4555\ldots = \frac{41}{90} \), which is on no row. Avoiding \( 0 \) and \( 9 \) is exactly what the last paragraph of the proof uses.

*Analysis on the Real Line*, Chapter 1 proves that \( \nR \) is uncountable again, with no decimals at all, directly from its least upper bound axiom; that proof needs none of (D1)–(D3).

## Transcendental numbers

A real number that is not algebraic is called **transcendental**. Section 3.2 showed that the set \( \mathrm{Alg} \) of algebraic numbers is countable (@thm-algebraic-countable).

::: {#cor-transcendental-exist}
[Transcendental Numbers Exist]

The set \( \nR \setminus \mathrm{Alg} \) of transcendental numbers is uncountable. In particular, there is a real number that is not algebraic.
:::

::: {.proof}
By excluded middle (@fd1:prp-excluded-middle), every real number is in \( \mathrm{Alg} \) or not, so \( \nR = \mathrm{Alg} \cup (\nR \setminus \mathrm{Alg}) \). Suppose \( \nR \setminus \mathrm{Alg} \) is countable. Since \( \mathrm{Alg} \) is countable by @thm-algebraic-countable, \( \nR \) is countable by @prp-union-two-countable, contradicting @thm-reals-uncountable-decimal. So \( \nR \setminus \mathrm{Alg} \) is uncountable. In particular \( \nR \setminus \mathrm{Alg} \ne \emptyset \), since \( \emptyset \) is countable (@def-countable). So not every \( x \) satisfies \( x \notin \nR \setminus \mathrm{Alg} \): otherwise \( \nR \setminus \mathrm{Alg} \) would be an empty set (@def-empty-set), hence equal to \( \emptyset \) (@prp-empty-set-unique). By the classical law @fd1:prp-quantifier-negation (a) and \( \rulename{\neg\neg E} \), some \( x \) lies in \( \nR \setminus \mathrm{Alg} \); this \( x \) is a real number that is not algebraic. This last passage, from "not empty" to "has an element", is a classical step (*Logic and Proof*, Section 8.7).
:::

::: {.remark}
The proof names no transcendental number: it shows that the set of them is too large to be countable, hence not empty. Its classical steps are the split of \( \nR \) into \( \mathrm{Alg} \) and its complement (excluded middle) and the last one, from "not empty" to "has an element". Compare the classical proof of @fd1:thm-irrational-power-rational in *Logic and Proof*, Section 8.7, which also names no witness (unlike @fd1:prp-log2-9-irrational, which does). Proving that a particular number, such as \( \pi \), is transcendental is a different and much harder matter.
:::

## Exercises

### A. Check your understanding

::: {#exr-diagonal-arguments-a1}
[A1]

These parts are about the proof of @thm-cantor.

::: {.enumerate options="label=(\alph*)"}
1. Where in the proof is the surjectivity of \( f \) used, and what does it supply?
2. Run the proof on \( X = \{1, 2, 3\} \) and \( f(1) = \{1, 2\} \), \( f(2) = \emptyset \), \( f(3) = \{1, 3\} \). What is \( D \)? Is \( D \) a value of \( f \)?
3. State the idea of the proof in two sentences.
4. Why does the same argument not show that there is no surjection \( X \to X \)?
:::
:::

::: {.solution}
(a) It is used once, right after \( D \) is defined: surjectivity supplies an element \( d \in X \) with \( f(d) = D \). The two cases \( d \in D \) and \( d \notin D \) are then both refuted. Everything before that line holds for every function \( f \).

(b) Test each \( x \) against \( f(x) \): \( 1 \in f(1) \), so \( 1 \notin D \); \( 2 \notin f(2) = \emptyset \), so \( 2 \in D \); \( 3 \in f(3) \), so \( 3 \notin D \). Hence \( D = \{2\} \). It is not a value of \( f \): the values are \( \{1, 2\} \), \( \emptyset \), \( \{1, 3\} \), and \( D \) differs from \( f(x) \) about \( x \) in each case (\( 1 \in f(1) \setminus D \), \( 2 \in D \setminus f(2) \), \( 3 \in f(3) \setminus D \)).

(c) Build the set \( D \) of those \( x \) that are not in their own image \( f(x) \). Then \( D \) disagrees with every \( f(x) \) about the element \( x \), so it is not a value of \( f \).

(d) The set \( D \) is a **subset** of \( X \), so it is a candidate value only for a function into \( \powerset{X} \). For \( f \colon X \to X \), the argument (where the test \( x \in f(x) \) makes sense at all) shows that \( D \) is not a value of \( f \), but \( D \) need not be an element of \( X \), so nothing contradicts surjectivity. Indeed \( \id_X \) is a surjection \( X \to X \); with \( f = \id_X \) the argument is Russell's, and shows only that \( D = R_X \) is not an element of \( X \) (@thm-russell).
:::

### B. Practice

::: {#exr-diagonal-arguments-b1}
[B1: A faded diagonal]

Let \( \nN^{\nN} \) be the set of all functions \( \nN \to \nN \). Here is a proof that \( \nN^{\nN} \) is uncountable, with its last step left blank. *Name the move, then complete it.*

> Let \( f \colon \nN \to \nN^{\nN} \) be any function, and write \( f_n \coloneqq f(n) \), so that \( f_0, f_1, f_2, \dots \) is a list of elements of \( \nN^{\nN} \). Define \( g \colon \nN \to \nN \) by \( g(n) \coloneqq f_n(n) + 1 \). (Last step: ____________________.) Since \( f \) was arbitrary, no function \( \nN \to \nN^{\nN} \) is surjective, and as \( \nN^{\nN} \) is non-empty (it contains the zero function), \( \nN^{\nN} \) is not countable.
:::

::: {.solution}
The move is **the diagonal**: \( g \) is built to disagree with the list's \( n \)-th entry in place \( n \). The last step: for every \( n \in \nN \), \( g(n) = f_n(n) + 1 \ne f_n(n) \), so \( g \ne f_n \) by @prp-function-equality (two equal functions agree at \( n \)). Hence \( g \) is not on the list: \( g \) is an element of \( \nN^{\nN} \) (its values \( f_n(n) + 1 \) are natural numbers) that is not a value of \( f \), and \( f \) is not surjective.
:::

::: {#exr-diagonal-arguments-b2}
[B2]

Prove that the set of **infinite** subsets of \( \nN \) is uncountable.
:::

::: {.solution}
Let \( \sF \) be the set of finite subsets of \( \nN \) and \( \sI \) the set of infinite ones, both subsets of \( \powerset{\nN} \) defined by specification. By excluded middle (@fd1:prp-excluded-middle), every subset of \( \nN \) is finite or not finite, that is, finite or infinite (@def-infinite), so \( \powerset{\nN} = \sF \cup \sI \). The set \( \sF \) is countable by @exr-countable-sets-c1. If \( \sI \) were countable, \( \powerset{\nN} \) would be countable by @prp-union-two-countable, contradicting @cor-powerset-naturals-uncountable. So \( \sI \) is uncountable.
:::

::: {#exr-diagonal-arguments-b3}
[B3: Expansions of three numbers]

For each of \( x = \frac13 \), \( \frac12 \), \( 1 \), find **all** decimal expansions of \( x \), checking the inequalities of @def-decimal-expansion for each one you give, and say which of (D1)–(D3) each case illustrates.
:::

::: {.solution}
We use @prp-geometric-sum with \( r = \frac{1}{10} \), after taking the constant factor \( \frac{1}{10} \) out of the sum: \( \sum_{k=1}^{n} 10^{-k} = \frac{1}{10} \sum_{k=1}^{n} (\frac{1}{10})^{k-1} = \frac{1}{10} \cdot \frac{1 - 10^{-n}}{9/10} = \frac19 (1 - 10^{-n}) \).

\( x = \frac13 \). The all-three sequence has \( t_n = \frac39 (1 - 10^{-n}) = \frac13 - \frac13 10^{-n} \), so \( t_n \le \frac13 \le t_n + 10^{-n} \). It is an expansion, and it does not end in all \( 9 \)s, as (D1) promises. It ends in neither \( 9 \)s nor \( 0 \)s, so by (D3) no other expansion of \( \frac13 \) exists. Answer: \( 0.333\ldots \) only.

\( x = \frac12 \). Example 2 after @def-decimal-expansion checks that \( 0.5000\ldots \) and \( 0.4999\ldots \) are expansions. There are no others: if three different expansions existed, two of them would both end in all \( 9 \)s or both not; but by (D3), of two different expansions of one number, one ends in all \( 9 \)s and the other in all \( 0 \)s, and a sequence ending in all \( 0 \)s does not end in all \( 9 \)s (from some place on, its digits would be both \( 0 \) and \( 9 \)). Answer: exactly these two, which illustrate (D3); the first is the one (D1) promises.

\( x = 1 \). The all-nine sequence is an expansion (Example 3). Conversely, let \( (d_k) \) be an expansion of \( 1 \), and suppose \( d_m \le 8 \) for some \( m \). Since every digit is at most \( 9 \), \( t_m \le \sum_{k=1}^{m} 9 \cdot 10^{-k} - 10^{-m} = 1 - 2 \cdot 10^{-m} \), so \( t_m + 10^{-m} \le 1 - 10^{-m} < 1 \), against the definition. So every digit is \( 9 \). Answer: \( 0.999\ldots \) only. The all-nine sequence is an expansion of \( 1 \), an instance of the existence half of (D2). Here (D3) has no second expansion to compare. The case also shows why (D1) is stated for \( [0, 1) \) only: the one expansion of \( 1 \) ends in all \( 9 \)s.
:::

::: {#exr-diagonal-arguments-b4}
[B4: Prove or disprove]

Prove each true statement, and show each false one false.

::: {.enumerate options="label=(\alph*)"}
1. The set of periodic 0–1 sequences, those \( a \in \{0, 1\}^{\nN} \) with some \( p \ge 1 \) such that \( a(n + p) = a(n) \) for every \( n \in \nN \), is uncountable.
2. The set of 0–1 sequences with no two consecutive \( 1 \)s is uncountable.
3. For every set \( X \) there is no injection \( \powerset{X} \to X \).
4. If \( X \) is infinite, there is no surjection \( X \to X \times X \).
5. The set of all functions \( \nZ \to \{0, 1\} \) is uncountable.
:::
:::

::: {.solution}
(a) **False:** the set is countable. For \( p \in \nZ_{>0} \) let \( P_p \) be the set of sequences \( a \) with \( a(n + p) = a(n) \) for every \( n \in \nN \). For \( a \in P_p \), \( a(qp + r) = a(r) \) for all \( q \in \nN \) and \( 0 \le r < p \), by induction on \( q \). Every \( n \in \nN \) is \( qp + r \) for such \( q \) and \( r \) (@thm-division-algorithm; \( q \ge 0 \) since \( n \ge 0 \) and \( r < p \)). So \( a \) is determined by \( a(0), \dots, a(p - 1) \), and \( a \mapsto a|_{\{0, \dots, p-1\}} \) is an injection of \( P_p \) into the set of functions \( \{0, \dots, p - 1\} \to \{0, 1\} \), which is finite, with \( 2^p \) elements (@prp-power-set-count, through indicator functions). A finite set injects into \( \nN \) (@thm-countable-characterizations, (iii) ⇒ (ii)); composing, \( P_p \) injects into \( \nN \), so \( P_p \) is countable ((ii) ⇒ (i)). The set of periodic sequences is \( \bigcup_{p \in \nZ_{>0}} P_p \), countable by @thm-countable-union (b), since \( \nZ_{>0} \subseteq \nN \) is countable (@prp-countable-subset). Choice is not needed here, although the proof of the cited theorem uses @ax-choice in general: the lists are given by a formula. Let \( w_{p,k} \) (\( k < 2^p \)) be the \( k \)-th pattern \( \{0, \dots, p - 1\} \to \{0, 1\} \) in binary order, put \( w_{p,k} \coloneqq w_{p,2^p-1} \) for \( k \ge 2^p \), and let \( L(p,k) \) be the sequence \( n \mapsto w_{p,k}(r) \), \( r \) the remainder of \( n \) on division by \( p \). Then \( L \) maps \( \nZ_{>0} \times \nN \) onto the set of periodic sequences, and composing it with a surjection \( \nN \to \nZ_{>0} \times \nN \), as in @exm-choice-free-unions, lists them without @ax-choice. The diagonal fails here because the flipped diagonal of a list of periodic sequences need not be periodic: the first usual failure of @exm-method-diagonal.

(b) **True.** Send \( b \in \{0, 1\}^{\nN} \) to the sequence \( a \) with \( a(2n) \coloneqq b(n) \) and \( a(2n + 1) \coloneqq 0 \). Every odd place of \( a \) is \( 0 \), and of two consecutive places one is odd, so \( a \) has no two consecutive \( 1 \)s. The map is injective, since \( b \) is read back from the even places (@prp-function-equality). If the set were countable, composing with an injection of it into \( \nN \) (@thm-countable-characterizations, (i) ⇒ (ii)) would give an injection \( \{0, 1\}^{\nN} \to \nN \), so \( \{0, 1\}^{\nN} \) would be countable ((ii) ⇒ (i)), against @thm-binary-sequences-uncountable.

(c) **True.** Let \( i \colon \powerset{X} \to X \) be injective. Since \( \emptyset \in \powerset{X} \), the domain is non-empty, so \( i \) has a left inverse \( r \colon X \to \powerset{X} \) (@thm-left-inverse-iff-injective (b)). The equation \( r \circ i = \id_{\powerset{X}} \) says that \( i \) is a right inverse of \( r \), so \( r \) is surjective (@prp-right-inverse-surjective), against @thm-cantor.

(d) **False.** Take \( X = \nN \). The set \( \nN \times \nN \) is countable (@thm-product-countable) and non-empty, so @def-countable gives a surjection \( \nN \to \nN \times \nN \).

(e) **True.** Restriction \( a \mapsto a|_{\nN} \) maps \( \{0, 1\}^{\nZ} \) onto \( \{0, 1\}^{\nN} \): a given \( b \in \{0, 1\}^{\nN} \) is the restriction of its extension by \( 0 \) on the negative integers. If \( \{0, 1\}^{\nZ} \) were countable, its image \( \{0, 1\}^{\nN} \) would be countable (@prp-countable-image), against @thm-binary-sequences-uncountable.
:::

### C. Going deeper

::: {#exr-diagonal-arguments-c1}
[C1: Exit check: Cantor]

Prove @thm-cantor: for every set \( X \), there is no surjection \( X \to \powerset{X} \). Deduce that \( \powerset{\nN} \) is uncountable.
:::

::: {.solution}
Let \( f \colon X \to \powerset{X} \) be a function, and let \( D \coloneqq \{ x \in X : x \notin f(x) \} \), a subset of \( X \), so \( D \in \powerset{X} \). Suppose \( f \) is surjective. Then \( D = f(d) \) for some \( d \in X \). If \( d \in D \), then \( d \notin f(d) = D \) by the definition of \( D \), a contradiction; so \( d \notin D \). But then \( d \notin f(d) \) and \( d \in X \), so \( d \in D \) by the definition of \( D \), a contradiction. Hence \( f \) is not surjective, and since \( f \) was arbitrary, no surjection \( X \to \powerset{X} \) exists.

For \( X = \nN \): by @def-countable, \( \powerset{\nN} \) is countable only if it is empty or there is a surjection \( \nN \to \powerset{\nN} \). It is not empty, since \( \emptyset \in \powerset{\nN} \), and the theorem excludes the surjection. So \( \powerset{\nN} \) is uncountable.

**Marking scheme.** (10 points)
- 2: takes an arbitrary \( f \colon X \to \powerset{X} \) and either assumes it onto, towards a contradiction, or sets out to show that it misses a set.
- 3: defines \( D = \{ x \in X : x \notin f(x) \} \) and notes that it is a subset of \( X \).
- 2: uses surjectivity to obtain \( d \) with \( f(d) = D \) (or, in the direct form, fixes an arbitrary \( x \)).
- 2: refutes both cases, \( d \in D \) and \( d \notin D \) (or shows that \( D \) and \( f(x) \) disagree about \( x \)).
- 1: the deduction for \( \powerset{\nN} \), handling both clauses of "countable": non-empty, and no surjection from \( \nN \).
The direct form ("\( D \ne f(x) \) for every \( x \), since they disagree about \( x \)") earns the same points: 2 for the arbitrary \( f \), 3 for \( D \), 4 for the disagreement at every \( x \), 1 for the deduction.
Fatal errors (0 for the step): \( D = \{ x \in X : x \in f(x) \} \) (it may well be a value of \( f \)); checking the claim for one particular \( f \) and concluding for all, as in (N1) of @fd1:exm-not-allowed-catalogue (0 for the first step).
:::

::: {#exr-diagonal-arguments-c2}
[C2: Permutations of the naturals]

Prove that the set of all bijections \( \nN \to \nN \) is uncountable.
:::

::: {.solution}
[Hint 1]

*Consider the bijections that only swap \( 2n \) and \( 2n + 1 \), for some of the \( n \in \nN \), and fix every other number.*
:::

::: {.solution}
[Hint 2]

*Such bijections correspond to \( \{0, 1\}^{\nN} \): the \( n \)-th entry says whether the pair \( 2n, 2n + 1 \) is swapped.*
:::

::: {.solution}
Every \( m \in \nN \) is \( 2q + r \) for exactly one pair \( (q, r) \) with \( q \in \nN \) and \( r \in \{0, 1\} \) (@thm-division-algorithm with divisor \( 2 \), the quotient lying in \( \nN \) as in the proof of @prp-union-two-countable). For \( b \in \{0, 1\}^{\nN} \) define \( \pi_b \colon \nN \to \nN \) by
\[
\pi_b(2q + r) \coloneqq
\begin{cases}
2q + r & \text{if } b(q) = 0, \\
2q + 1 - r & \text{if } b(q) = 1,
\end{cases}
\]
so \( \pi_b \) swaps \( 2q \) and \( 2q + 1 \) when \( b(q) = 1 \) and fixes them otherwise. It maps each pair \( \{2q, 2q + 1\} \) to itself, and applying it twice returns every number to its place, so \( \pi_b \circ \pi_b = \id_{\nN} \), and \( \pi_b \) is a bijection by @thm-bijection-iff-inverse.

Let \( B \) be the set of bijections \( \nN \to \nN \); it is non-empty, since \( \id_{\nN} \in B \). Let \( f \colon \nN \to B \) be any function, and write \( f_n \coloneqq f(n) \). Define \( b \in \{0, 1\}^{\nN} \) by \( b(n) \coloneqq 1 \) if \( f_n(2n) = 2n \), and \( b(n) \coloneqq 0 \) otherwise, and let \( \pi \coloneqq \pi_b \in B \). For every \( n \in \nN \), \( \pi(2n) \ne f_n(2n) \): if \( f_n(2n) = 2n \), then \( b(n) = 1 \) and \( \pi(2n) = 2n + 1 \); if \( f_n(2n) \ne 2n \), then \( b(n) = 0 \) and \( \pi(2n) = 2n \). So \( \pi \ne f_n \) for every \( n \) (@prp-function-equality), and \( f \) is not surjective. Since \( f \) was arbitrary and \( B \ne \emptyset \), \( B \) is uncountable (@def-countable).

This is the diagonal again, with the \( n \)-th entry tested at the place \( 2n \). Alternatively, \( b \mapsto \pi_b \) is an injection \( \{0, 1\}^{\nN} \to B \), since \( \pi_b(2q) \) is \( 2q \) or \( 2q + 1 \) according to \( b(q) \); if \( B \) were countable, composing with an injection \( B \to \nN \) (@thm-countable-characterizations) would make \( \{0, 1\}^{\nN} \) countable, against @thm-binary-sequences-uncountable.

**Marking scheme.** (10 points)
- 3: defines, for each \( b \in \{0, 1\}^{\nN} \) (or each set of pairs), the bijection that swaps \( 2n \) and \( 2n + 1 \) exactly when \( b(n) = 1 \), and proves it is a bijection.
- 4: given an arbitrary list of bijections, defines \( b \) from the \( n \)-th entry's value at a place belonging to the \( n \)-th pair, and shows that the resulting bijection differs from the \( n \)-th entry; or shows that \( b \mapsto \pi_b \) is injective.
- 3: concludes, with the non-emptiness of the set of bijections or through @thm-binary-sequences-uncountable and the closure properties of countable sets.
Fatal errors (0 for the step): the plain diagonal \( g(n) \coloneqq f_n(n) + 1 \), which is not a bijection; a "bijection" that moves numbers between different pairs without checking that it stays one-to-one and onto.
:::

<!-- dependency ledger
thm-binary-sequences-uncountable (proof): 1 - b is in {0, 1} and differs from b, for b in {0, 1} | arithmetic (two cases)
thm-binary-sequences-uncountable (example): the table entries and the flipped diagonal 1, 0, 1, 0 | verify/ch03/thm-binary-sequences-uncountable.py
thm-cantor (claim): (ii) {x} = {y} gives x = y | def-set-equality (F2.1 §02), used silently
thm-cantor (claim): (ii), (iii) "strictly bigger" as a relation | F2.3 §04 (prose pointer within the chapter; nothing here depends on it)
cor-powerset-naturals-uncountable (claim): (after it) S -> ind_S is a bijection P(N) -> {0, 1}^N with inverse b -> {n : b(n) = 1} | F2.1 §05 (the correspondence after exm-function-set-small); thm-bijection-iff-inverse (cited)
def-decimal-expansion (example): t_n = 1/2 - 10^(-n) for 0.4999..., t_n = 1 - 10^(-n) for 0.999...; the non-example 0.51 fails first at n = 3 | prp-geometric-sum (cited); verify/ch03/def-decimal-expansion.py
def-decimal-expansion (claim): (why this definition) no x has 1 - 10^(-n) <= x < 1 for every n | Archimedean property, school fact; AN1.1
def-decimal-expansion (claim): (why this definition) 1 is the only x with 1 - 10^(-n) <= x <= 1 for every n | Archimedean property, school fact; AN1.1 (the uniqueness half of (D2))
def-decimal-expansion (claim): 10^(-k) := (1/10)^k | def-power (cited)
def-decimal-expansion (example): (Examples 2, 3) a constant factor comes out of a finite sum; splitting off the first term | induction on n via def-sum-product (F2.2); R arithmetic
exr-diagonal-arguments-b3 (solution): a constant factor comes out of a finite sum | induction on n via def-sum-product (F2.2); R arithmetic
def-decimal-expansion (claim): (D1)-(D3) | school facts (D1)-(D3), stated in this section and not proved; AN1.1 (prose pointer: completeness and the Archimedean property, for (D1)-(D2))
def-decimal-expansion (claim): (D3) follows from F1.1-F2.3 | thm-well-ordering, prp-geometric-sum (cited), def-sum-product (inline; the proof is not written out, (D3) is used as stated)
def-decimal-expansion (claim): a digit sequence with no 0 and no 9 is the only expansion of its number | school fact (D3), stated in this section
thm-reals-uncountable-decimal (proof): the expansion of x_n not ending in 9s exists and is unique | school facts (D1), (D3), stated in this section
thm-reals-uncountable-decimal (proof): some y has expansion (e_k), and y lies in [0.4, 0.6] | school fact (D2), stated in this section; the definition at n = 1
thm-reals-uncountable-decimal (proof): y = x_n is impossible | the consequence of (D3) stated in this section (a digit sequence with no 0 and no 9 is the only expansion of its number)
thm-reals-uncountable-decimal (claim): the naive rule gives 0.4999... = 1/2; the 4/5 rule gives 0.4555... = 41/90 | def-decimal-expansion Example 2; school fact (D2); verify/ch03/thm-reals-uncountable-decimal.py
thm-reals-uncountable-decimal (claim): AN1.1 reproves it without decimals | AN1.1 (prose pointer; thm-reals-uncountable exists)
cor-transcendental-exist (proof): R = Alg u (R \ Alg), every real is algebraic or not | prp-excluded-middle (cited; classical step, flagged in the remark)
cor-transcendental-exist (proof): the empty set is countable | def-countable (F2.3 §01)
cor-transcendental-exist (proof): a set that is not empty has an element | def-empty-set, prp-empty-set-unique (F2.1); prp-quantifier-negation (a) and not-not-E (classical step, flagged)
cor-transcendental-exist (claim): (remark) F1.5 §07 comparison | thm-irrational-power-rational, prp-log2-9-irrational (optional; pointer in a remark only)
cor-transcendental-exist (claim): (remark) pi is transcendental | not proved and not used (a remark only)
exm-five-strings-diagonal (solution): diagonal 0, 1, 0, 0, 1 of the 1.5 list; g = 10110 differs from s_k in place k; any list | verify/ch03/exm-five-strings-diagonal.py; prp-function-equality (cited)
exm-five-strings-diagonal (claim): (check) a list of 32 strings may contain every string | 2^5 = 32 (prp-power-set-count, F2.2 §05), used silently
exm-method-diagonal (claim): (check) the unflipped diagonal of the all-zero list is f(0) | inline
thm-binary-sequences-uncountable (claim): (scratch work) table rows match the proof | inline
exm-diagonal-outgrows-list (solution): max of n + 1 numbers exists; g(n) > f_k(n) for n >= k | prp-finite-max (F2.2 §03, cited); verify/ch03/exm-diagonal-outgrows-list.py
thm-cantor (claim): (hook) R_A disagrees with each x in A about x | thm-russell (F2.1 §02, cited)
exr-diagonal-arguments-b4 (solution): (a) periodic sequences determined by p values; P_p listed by a rule; union countable | thm-division-algorithm (F2.2 §02), prp-power-set-count (F2.2 §05), thm-countable-characterizations, thm-countable-union, prp-countable-subset, exm-choice-free-unions (cited); verify/ch03/exr-diagonal-arguments-b4.py
exr-diagonal-arguments-b4 (solution): (b) interleaving injection; (c) left inverse, right inverse; (d) N x N countable; (e) restriction onto | prp-function-equality, thm-left-inverse-iff-injective, prp-right-inverse-surjective (F2.1 §06), thm-product-countable, prp-countable-image (cited); verify/ch03/exr-diagonal-arguments-b4.py
exr-diagonal-arguments-a1 (solution): D = {2} | verify/ch03/exr-diagonal-arguments-a1.py
exr-diagonal-arguments-b2 (solution): the finite subsets of N form a countable set | exr-countable-sets-c1 (cited; an exercise may cite an earlier one)
exr-diagonal-arguments-b2 (solution): every subset of N is finite or infinite | prp-excluded-middle (cited), def-infinite
exr-diagonal-arguments-b3 (solution): t_n for 0.333...; the bound t_m <= 1 - 2 * 10^(-m) | prp-geometric-sum (cited); school facts (D1)-(D3); verify/ch03/exr-diagonal-arguments-b3.py
exr-diagonal-arguments-b3 (solution): termwise comparison of finite sums (d_k <= 9 for k < m, d_m <= 9 - 1) | induction on n via def-sum-product (F2.2) and the order axioms for +
exr-diagonal-arguments-b3 (solution): no sequence ends in both all 0s and all 9s | 0 != 9, at a place beyond both thresholds
exr-diagonal-arguments-c2 (solution): m = 2q + r uniquely with q in N, r in {0, 1} | thm-division-algorithm (cited), quotient in N as in prp-union-two-countable
exr-diagonal-arguments-c2 (solution): pi_b o pi_b = id; pi(2n) differs from f_n(2n) | inline; verify/ch03/exr-diagonal-arguments-c2.py
-->
