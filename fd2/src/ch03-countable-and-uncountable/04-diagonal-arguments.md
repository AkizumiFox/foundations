# Diagonal Arguments: Uncountable Sets and Cantor's Theorem

Every infinite set met so far has turned out to be countable: \( \nN \), \( \nZ \), \( \nQ \), finite products of countable sets, countable unions of them (@thm-countable-union), and even the algebraic numbers (@thm-algebraic-countable). Is every infinite set countable? This section shows that the answer is no, by one argument used three times. Given any list, it builds an object that the list misses. The argument proves that the set of 0–1 sequences is uncountable, that no set can be mapped onto the set of its subsets (Cantor's theorem), and, with decimals, that \( \nR \) is uncountable.

## A sequence that is not on the list

Recall from Section 6.4 that \( \{0, 1\}^{\nN} \) is the set of all functions \( \nN \to \{0, 1\} \): the sequences of zeros and ones, indexed from \( 0 \). It is infinite, and it looks no bigger than \( \nN \times \nN \), which is countable. To show that it is **not** countable we must show, by @def-countable, that it is non-empty and that **no** function \( f \colon \nN \to \{0, 1\}^{\nN} \) is onto. So we take an arbitrary list \( f(0), f(1), f(2), \dots \) of sequences and look for a sequence that is not on it.

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

::: {.proof}
Let \( f \colon \nN \to \{0, 1\}^{\nN} \) be any function. Define \( g \colon \nN \to \{0, 1\} \) by
\[
g(n) \coloneqq 1 - f(n)(n) \qquad (n \in \nN) ;
\]
its values lie in \( \{0, 1\} \), since \( 1 - 0 = 1 \) and \( 1 - 1 = 0 \). So \( g \in \{0, 1\}^{\nN} \). For every \( n \in \nN \), \( g(n) \ne f(n)(n) \), since no \( b \in \{0, 1\} \) has \( 1 - b = b \). Hence \( g \ne f(n) \): if \( g = f(n) \), then \( g(n) = f(n)(n) \), which is false; the two functions differ at place \( n \) [\( \rulename{{=}E} \), \( \rulename{\neg I} \); @prp-function-equality]. So \( g \) is not a value of \( f \), and \( f \) is not surjective. Since \( f \) was arbitrary, no function \( \nN \to \{0, 1\}^{\nN} \) is surjective. The set \( \{0, 1\}^{\nN} \) is non-empty, since it contains the zero sequence. By @def-countable, \( \{0, 1\}^{\nN} \) is not countable.
:::

This is the move of the section, and it has a name.

**The diagonal.** *Given any list, build an object that differs from the \( n \)-th entry at the \( n \)-th place.* The new object is not on the list, because it disagrees with every entry somewhere, and the place of disagreement is chosen by the entry's own position.

::: {.check}
Run the proof on the list \( f(n) \coloneqq \ind_{\{n\}} \), the sequence with a \( 1 \) in place \( n \) and \( 0 \) elsewhere. What is \( g \)? Is it on the list?
:::

::: {.solution}
Here \( f(n)(n) = \ind_{\{n\}}(n) = 1 \) for every \( n \), so \( g(n) = 1 - 1 = 0 \) for every \( n \): \( g \) is the zero sequence. It is indeed not on the list, since every \( f(n) \) has a \( 1 \) in place \( n \).
:::

::: {.warning}
**The diagonal object depends on the list.** "The diagonal sequence" is not one sequence: each list has its own, and a different list may well contain the \( g \) built from this one (the list \( g, f(0), f(1), \dots \) does). And the conclusion "uncountable" needs the list to be **arbitrary**. Running the construction on one list, or on a few, shows only that those lists miss something; concluding "so no list works" from them is the error (N1) of @exm-not-allowed-catalogue. The proof above starts from "let \( f \) be **any** function", and that is what makes its conclusion universal.
:::

## Cantor's theorem

The table had a row for each \( n \in \nN \) and a column for each place \( k \in \nN \). Nothing about the diagonal needs the rows and the columns to be indexed by \( \nN \): it needs only that they are indexed by the **same** set. A subset \( S \) of a set \( X \) is a row with one entry for each \( x \in X \), "in" or "out", the values of \( \ind_S \). So the argument applies to any set and the set of its subsets.

::: {#thm-cantor}
[Cantor's Theorem]

Let \( X \) be a set. Then there is **no** surjection \( X \to \powerset{X} \).
:::

*Try it first (ten minutes): given a function \( f \colon X \to \powerset{X} \), which subset of \( X \) could be missed by \( f \)? Try \( X = \{1, 2, 3\} \) with a function of your own first.*

::: {.idea}
The first attempts look for a subset that is "too big" or "too small" to be a value, such as \( X \) itself or \( \emptyset \), and fail: \( f \) may well take both values. Size is the wrong idea. A set \( D \) differs from \( f(x) \) as soon as the two disagree about **one** element, and the only element we know anything about in connection with \( f(x) \) is \( x \) itself. So we make \( D \) disagree with \( f(x) \) at \( x \): put \( x \) into \( D \) exactly when \( x \notin f(x) \). This is the diagonal of the table, flipped.

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

(ii) *The power set is strictly bigger.* The map \( x \mapsto \{x\} \) is an injection \( X \to \powerset{X} \), since \( \{x\} = \{y\} \) gives \( x = y \). So \( \powerset{X} \) has at least as many elements as \( X \), in the sense that \( X \) is in bijection with a subset of it, and by the theorem it is not equinumerous with \( X \), since a bijection would be a surjection. Section 8.5 names this relation: \( X \) is strictly smaller than \( \powerset{X} \).

(iii) *There is no largest size.* \( \nN \), \( \powerset{\nN} \), \( \powerset{\powerset{\nN}} \), …: each set in this sequence is strictly bigger than the one before.

::: {#cor-powerset-naturals-uncountable}
[The Subsets of the Naturals]

The power set \( \powerset{\nN} \) is uncountable.
:::

::: {.proof}
The set \( \powerset{\nN} \) is non-empty, since \( \emptyset \in \powerset{\nN} \), and by @thm-cantor with \( X = \nN \) there is no surjection \( \nN \to \powerset{\nN} \). By @def-countable, \( \powerset{\nN} \) is not countable.
:::

The two diagonal proofs are one. By the correspondence of Section 6.4, \( S \mapsto \ind_S \) is a bijection \( \powerset{\nN} \to \{0, 1\}^{\nN} \), with inverse \( b \mapsto \{ n \in \nN : b(n) = 1 \} \) (@thm-bijection-iff-inverse). Given \( f \colon \nN \to \powerset{\nN} \), the sequence \( g(n) = 1 - \ind_{f(n)}(n) \) of @thm-binary-sequences-uncountable is \( 1 \) exactly when \( n \notin f(n) \), so \( g = \ind_D \) for the set \( D \) of Cantor's proof.

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

**Why this definition.** Both inequalities are non-strict. With a strict right inequality, \( x < t_n + 10^{-n} \), the all-nine sequence would be an expansion of no number at all: it would need \( x < 1 \) together with \( 1 - 10^{-n} \le x \) for every \( n \), and no real number satisfies both, by the Archimedean property (a school fact; Chapter 11 proves it). The non-strict form is what makes \( 0.999\ldots = 1 \) true, and true **by the definition**: the inequalities for \( x = 1 \) are checked in Example 3, and no other number satisfies them, since \( 1 - 10^{-n} \le x \le 1 \) for every \( n \) forces \( x = 1 \), again by the Archimedean property (this is the uniqueness half of (D2) below). Example 2 shows that the price is two expansions for some numbers.

What this book does not prove are the facts that make expansions behave as school says. We state them once and use them in this section and the next, always by name.

::: {.enumerate options="label=(D\arabic*)"}
1. Every \( x \in [0, 1) \) has a decimal expansion that does **not** end in all \( 9 \)s.
2. Every digit sequence is a decimal expansion of **exactly one** \( x \in [0, 1] \).
3. If two **different** digit sequences are expansions of the same \( x \), then one of them ends in all \( 9 \)s and the other ends in all \( 0 \)s.
:::

Here a digit sequence **ends in all \( 9 \)s** if there is \( N \ge 1 \) with \( d_k = 9 \) for every \( k \ge N \), and likewise for \( 0 \)s. By the uniqueness in (D2), we may write \( x = 0.d_1 d_2 d_3 \ldots \) for "\( x \) is the number of which \( d_1, d_2, d_3, \dots \) is an expansion". So \( 0.4999\ldots = 0.5000\ldots = \frac12 \), as in (D3).

Neither (D1) nor (D2) follows from what Part 0 has. (D3) does, by a finite computation at the first place where the two sequences differ (@thm-well-ordering, @prp-geometric-sum); we state it with the others to quote it by name. The **existence** half of (D2), that some \( x \) satisfies all the inequalities at once, is where the completeness of \( \nR \) hides, and Chapter 11 takes completeness as an axiom. The **uniqueness** half of (D2) and the "not ending in all \( 9 \)s" of (D1) rest on the Archimedean property: two numbers \( x, x' \) with \( \abs{x - x'} \le 10^{-n} \) for every \( n \) must be equal, which Chapter 11 also proves. Until then we use them as school facts, and each use names the fact it uses.

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

Chapter 11 proves that \( \nR \) is uncountable again, with no decimals at all, directly from its least upper bound axiom; that proof needs none of (D1)–(D3).

## Transcendental numbers

A real number that is not algebraic is called **transcendental**. Section 8.3 showed that the set \( \mathrm{Alg} \) of algebraic numbers is countable (@thm-algebraic-countable).

::: {#cor-transcendental-exist}
[Transcendental Numbers Exist]

The set \( \nR \setminus \mathrm{Alg} \) of transcendental numbers is uncountable. In particular, there is a real number that is not algebraic.
:::

::: {.proof}
By excluded middle (@prp-excluded-middle), every real number is in \( \mathrm{Alg} \) or not, so \( \nR = \mathrm{Alg} \cup (\nR \setminus \mathrm{Alg}) \). Suppose \( \nR \setminus \mathrm{Alg} \) is countable. Since \( \mathrm{Alg} \) is countable by @thm-algebraic-countable, \( \nR \) is countable by @prp-union-two-countable, contradicting @thm-reals-uncountable-decimal. So \( \nR \setminus \mathrm{Alg} \) is uncountable. In particular \( \nR \setminus \mathrm{Alg} \ne \emptyset \), since \( \emptyset \) is countable (@def-countable). So not every \( x \) satisfies \( x \notin \nR \setminus \mathrm{Alg} \): otherwise \( \nR \setminus \mathrm{Alg} \) would be an empty set (@def-empty-set), hence equal to \( \emptyset \) (@prp-empty-set-unique). By the classical law @prp-quantifier-negation (a) and \( \rulename{\neg\neg E} \), some \( x \) lies in \( \nR \setminus \mathrm{Alg} \); this \( x \) is a real number that is not algebraic. This last passage, from "not empty" to "has an element", is a classical step (Section 5.7).
:::

::: {.remark}
The proof names no transcendental number: it shows that the set of them is too large to be countable, hence not empty. Its classical steps are the split of \( \nR \) into \( \mathrm{Alg} \) and its complement (excluded middle) and the last one, from "not empty" to "has an element". Compare the classical proof of @thm-irrational-power-rational in Section 5.7, which also names no witness (unlike @prp-log2-9-irrational, which does). Proving that a particular number, such as \( \pi \), is transcendental is a different and much harder matter.
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
Let \( \sF \) be the set of finite subsets of \( \nN \) and \( \sI \) the set of infinite ones, both subsets of \( \powerset{\nN} \) defined by specification. By excluded middle (@prp-excluded-middle), every subset of \( \nN \) is finite or not finite, that is, finite or infinite (@def-infinite), so \( \powerset{\nN} = \sF \cup \sI \). The set \( \sF \) is countable by @exr-countable-sets-c1. If \( \sI \) were countable, \( \powerset{\nN} \) would be countable by @prp-union-two-countable, contradicting @cor-powerset-naturals-uncountable. So \( \sI \) is uncountable.
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
Fatal errors (0 for the step): \( D = \{ x \in X : x \in f(x) \} \) (it may well be a value of \( f \)); checking the claim for one particular \( f \) and concluding for all, as in (N1) of @exm-not-allowed-catalogue (0 for the first step).
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
thm-binary-sequences-uncountable (example): the table entries and the flipped diagonal 1, 0, 1, 0 | verify/ch08/thm-binary-sequences-uncountable.py
thm-cantor (claim): (ii) {x} = {y} gives x = y | def-set-equality (Ch 6 Section 6.1), used silently
thm-cantor (claim): (ii), (iii) "strictly bigger" as a relation | Section 8.5 (prose pointer within the chapter; nothing here depends on it)
cor-powerset-naturals-uncountable (claim): (after it) S -> ind_S is a bijection P(N) -> {0, 1}^N with inverse b -> {n : b(n) = 1} | Ch 6 Section 6.4 (the correspondence after exm-function-set-small); thm-bijection-iff-inverse (cited)
def-decimal-expansion (example): t_n = 1/2 - 10^(-n) for 0.4999..., t_n = 1 - 10^(-n) for 0.999...; the non-example 0.51 fails first at n = 3 | prp-geometric-sum (cited); verify/ch08/def-decimal-expansion.py
def-decimal-expansion (claim): (why this definition) no x has 1 - 10^(-n) <= x < 1 for every n | Archimedean property, school fact; Ch 11
def-decimal-expansion (claim): (why this definition) 1 is the only x with 1 - 10^(-n) <= x <= 1 for every n | Archimedean property, school fact; Ch 11 (the uniqueness half of (D2))
def-decimal-expansion (claim): 10^(-k) := (1/10)^k | def-power (cited)
def-decimal-expansion (example): (Examples 2, 3) a constant factor comes out of a finite sum; splitting off the first term | induction on n via def-sum-product (Ch 7); R arithmetic
exr-diagonal-arguments-b3 (solution): a constant factor comes out of a finite sum | induction on n via def-sum-product (Ch 7); R arithmetic
def-decimal-expansion (claim): (D1)-(D3) | school facts (D1)-(D3), stated in this section and not proved; Ch 11 (prose pointer: completeness and the Archimedean property, for (D1)-(D2))
def-decimal-expansion (claim): (D3) follows from Part 0 | thm-well-ordering, prp-geometric-sum (cited), def-sum-product (inline; the proof is not written out, (D3) is used as stated)
def-decimal-expansion (claim): a digit sequence with no 0 and no 9 is the only expansion of its number | school fact (D3), stated in this section
thm-reals-uncountable-decimal (proof): the expansion of x_n not ending in 9s exists and is unique | school facts (D1), (D3), stated in this section
thm-reals-uncountable-decimal (proof): some y has expansion (e_k), and y lies in [0.4, 0.6] | school fact (D2), stated in this section; the definition at n = 1
thm-reals-uncountable-decimal (proof): y = x_n is impossible | the consequence of (D3) stated in this section (a digit sequence with no 0 and no 9 is the only expansion of its number)
thm-reals-uncountable-decimal (claim): the naive rule gives 0.4999... = 1/2; the 4/5 rule gives 0.4555... = 41/90 | def-decimal-expansion Example 2; school fact (D2); verify/ch08/thm-reals-uncountable-decimal.py
thm-reals-uncountable-decimal (claim): Chapter 11 reproves it without decimals | ch11 (prose pointer; thm-reals-uncountable exists)
cor-transcendental-exist (proof): R = Alg u (R \ Alg), every real is algebraic or not | prp-excluded-middle (cited; classical step, flagged in the remark)
cor-transcendental-exist (proof): the empty set is countable | def-countable (Section 8.2)
cor-transcendental-exist (proof): a set that is not empty has an element | def-empty-set, prp-empty-set-unique (Ch 6); prp-quantifier-negation (a) and not-not-E (classical step, flagged)
cor-transcendental-exist (claim): (remark) Section 5.7 comparison | thm-irrational-power-rational, prp-log2-9-irrational (optional; pointer in a remark only)
cor-transcendental-exist (claim): (remark) pi is transcendental | not proved and not used (a remark only)
exr-diagonal-arguments-a1 (solution): D = {2} | verify/ch08/exr-diagonal-arguments-a1.py
exr-diagonal-arguments-b2 (solution): the finite subsets of N form a countable set | exr-countable-sets-c1 (cited; an exercise may cite an earlier one)
exr-diagonal-arguments-b2 (solution): every subset of N is finite or infinite | prp-excluded-middle (cited), def-infinite
exr-diagonal-arguments-b3 (solution): t_n for 0.333...; the bound t_m <= 1 - 2 * 10^(-m) | prp-geometric-sum (cited); school facts (D1)-(D3); verify/ch08/exr-diagonal-arguments-b3.py
exr-diagonal-arguments-b3 (solution): termwise comparison of finite sums (d_k <= 9 for k < m, d_m <= 9 - 1) | induction on n via def-sum-product (Ch 7) and the order axioms for +
exr-diagonal-arguments-b3 (solution): no sequence ends in both all 0s and all 9s | 0 != 9, at a place beyond both thresholds
exr-diagonal-arguments-c2 (solution): m = 2q + r uniquely with q in N, r in {0, 1} | thm-division-algorithm (cited), quotient in N as in prp-union-two-countable
exr-diagonal-arguments-c2 (solution): pi_b o pi_b = id; pi(2n) differs from f_n(2n) | inline; verify/ch08/exr-diagonal-arguments-c2.py
-->
