# Induction on the Natural Numbers

Section 4.1 made formulas into objects: strings built from atoms and \( \bot \) by five clauses, and by nothing else. There are infinitely many of them, and the theorems this chapter is heading for are about all of them. This section supplies the tool for proving anything about infinitely many objects at once. It is **induction** on the natural numbers, where it is familiar. Section 4.3 then carries it over to formulas, where it takes the form this chapter uses again and again; with it Section 4.3 proves that every formula can be read in only one way, and that a definition given one clause per connective defines exactly one thing.

## One argument for infinitely many cases

Here is a claim about every formula: *every formula has as many left parentheses as right ones.* It is believable. The clause (F3) of @def-formula adds one of each, and the other clauses add none. But the claim is about infinitely many strings, and checking them one by one never ends.

The belief already contains the shape of a proof. Every formula is reached by finitely many building steps from atoms and \( \bot \) (clause (F4)). The starting pieces have no parentheses, so they have equally many of each kind. Each building step turns formulas that balance into a formula that balances. So, step by step along any formation sequence, balance is never lost, and every formula balances.

Exactly the same shape appears with numbers. To show that some property holds for every natural number, show that it holds for \( 0 \), and that it passes from each number to the next. Every natural number is reached from \( 0 \) by finitely many steps of "add one", so the property is never lost. This is **induction**. We state it for numbers first, because it is simpler there, then prove the version for formulas from it.

Two words about language before we start. Statements such as "for every \( n \in \nN \), …" and "there is a \( k \) with …" are used in this section in their everyday sense, as Chapters 1 and 2 used them. Their rules of proof are the subject of Chapter 5, and nothing here needs more than the everyday reading. Likewise, a "collection" of formulas or numbers is meant in its everyday sense; *Sets, Relations, and Cardinality*, Chapter 1 treats sets properly. As in the rest of the book, \( \nN = \{0, 1, 2, \dots\} \) starts at \( 0 \), and the arithmetic and order of the natural numbers are used as school facts.

## The principle of induction

A **property of natural numbers** is an open sentence \( P(n) \) about a natural number \( n \), such as "\( n^2 \ge n \)" or "\( 2^n > n \)": for each particular \( n \) it becomes a statement, true or false (compare the open sentence \( x > 2 \) of @exm-statements, which became a statement once \( x \) was fixed).

*If a property holds for \( 0 \), and passes from each number to the next, then it holds for every number.*

::: {#ax-induction}
[Principle of Induction]

Let \( P(n) \) be a property of natural numbers. Suppose that

::: {.enumerate options="label=(\roman*)"}
1. \( P(0) \) holds, and
2. **for every** \( n \in \nN \), if \( P(n) \) holds, then \( P(n + 1) \) holds.
:::

Then \( P(n) \) holds **for every** \( n \in \nN \).
:::

In symbols (the quantifier symbols are Chapter 5's; here they abbreviate the words):
\[
\Bigl( P(0) \ \wedge \ \forall n \in \nN \ \bigl( P(n) \to P(n + 1) \bigr) \Bigr)
\ \to \ \forall n \in \nN \ P(n) .
\]

In words: hypothesis (i) is the **base case**. Hypothesis (ii) is the **inductive step**, and inside it, the assumption "\( P(n) \) holds" is the **induction hypothesis**. The step is **one** implication, proved **once**, for a number \( n \) about which we assume nothing except that it is a natural number with \( P(n) \). The conclusion is about every natural number at once.

**Its status.** We take @ax-induction as a basic property of \( \nN \), given and not proved, in the same way that *Analysis on the Real Line*, Chapter 1 takes the least upper bound axiom as a basic property of \( \nR \). It is, in a precise sense, what the three dots in \( \{0, 1, 2, \dots\} \) mean: the natural numbers are what we reach from \( 0 \) by adding one, again and again, and nothing else. *Sets, Relations, and Cardinality*, Chapter 2 proves that it is equivalent to the well-ordering principle (every nonempty collection of natural numbers has a least element), and *Number Systems: From \(\nN\) to \(\nR\)*, Chapter 1 derives it from the axioms of set theory. Nothing in this book depends on those two routes; every later use cites this principle.

**Dominoes.** The usual picture is a row of dominoes, one for each natural number. The base case knocks over the first. The inductive step says that each domino, if it falls, knocks over the next. Then every domino falls. The picture carries the one point that matters: the step must work for **every** \( n \), the first transition from \( 0 \) to \( 1 \) included. A single domino standing too far from the next stops the whole row, however well the others are placed.

**Not an infinite derivation.** From \( P(0) \) and the step we could derive \( P(1) \) by \( \rulename{{\to}E} \), then \( P(2) \), and so on; each single \( P(n) \) has a finite derivation, \( n \) lines long or so. But no finite derivation contains all of them, and "and so on" is not a rule. The principle of induction is what licenses the passage, in one step, from the two hypotheses to "for every \( n \)". It is a rule about \( \nN \), not a rule of logic.

**The step as a box.** In the language of Chapter 1, the inductive step is proved by a \( \rulename{{\to}I} \) box. We fix a natural number \( n \), knowing nothing about it except what the step allows, and open a box assuming \( P(n) \); inside the box we reach \( P(n + 1) \); closing the box gives the implication.

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \open
  \hypo {i} {P(n)}
  \have {} {\vdots}
  \have {j} {P(n + 1)}
  \close
  \have {k} {P(n) \to P(n + 1)} \ii{i-j}
\end{nd}$
\end{center}
```

The passage from "this \( n \) was arbitrary" to "for every \( n \)" is a rule for "for every", and Chapter 5 states it. For now, "let \( n \in \nN \)" means what Chapter 1 made it mean (Section 1.1): one fixed number, not further specified.

**Starting from another number.** Often a property is claimed only from some \( b \in \nN \) on, as in "for every \( n \ge 1 \)". Then it suffices to prove \( P(b) \), and, for every \( n \in \nN \) with \( n \ge b \), that \( P(n) \) implies \( P(n + 1) \). Indeed, apply @ax-induction to the property \( Q(m) \): "\( P(b + m) \) holds". Its base case \( Q(0) \) is \( P(b) \), and its step from \( Q(m) \) to \( Q(m + 1) \) is the step from \( P(b + m) \) to \( P(b + m + 1) \), where \( b + m \ge b \). So \( Q(m) \) holds for every \( m \in \nN \), and every natural number \( n \ge b \) is \( b + m \) for the natural number \( m = n - b \). We call this induction **started at** \( b \); it is @ax-induction applied to \( Q \).

Here is the first proof by induction, with every part labeled.

::: {#exm-sum-consecutive-products}
[A sum of products of neighbors]

Prove that for every natural number \( n \ge 1 \),
\[
1 \cdot 2 + 2 \cdot 3 + \dots + n(n + 1) = \frac{n(n + 1)(n + 2)}{3} .
\]
:::

::: {.solution}
Let \( P(n) \) be the displayed equation. Its left side is the sum of the \( n \) terms \( k(k + 1) \) for \( k = 1, \dots, n \), so the left side for \( n + 1 \) is the left side for \( n \) plus the one new term \( (n + 1)(n + 2) \). Before proving anything, test small cases. For \( n = 1, 2, 3 \) the left side is \( 2 \), \( 2 + 6 = 8 \) and \( 8 + 12 = 20 \), and the right side is \( \frac{1 \cdot 2 \cdot 3}{3} = 2 \), \( \frac{2 \cdot 3 \cdot 4}{3} = 8 \) and \( \frac{3 \cdot 4 \cdot 5}{3} = 20 \). The claim is plausible. It starts at \( n = 1 \), so we use induction started at \( 1 \) (see above).

*Base case.* For \( n = 1 \) the left side is the single term \( 1 \cdot 2 = 2 \), and the right side is \( \frac{1 \cdot 2 \cdot 3}{3} = 2 \). So \( P(1) \) holds.

*Inductive step.* Let \( n \in \nN \) with \( n \ge 1 \), and suppose \( P(n) \) holds (the induction hypothesis). Then
\[
\begin{aligned}
1 \cdot 2 + \dots + n(n + 1) + (n + 1)(n + 2)
&= \frac{n(n + 1)(n + 2)}{3} + (n + 1)(n + 2) \\
&= \frac{(n + 1)(n + 2)(n + 3)}{3} ,
\end{aligned}
\]
where the first equality is the induction hypothesis and the second takes out the common factor \( (n + 1)(n + 2) \), leaving \( \frac{n}{3} + 1 = \frac{n + 3}{3} \). The last expression is the right side of \( P(n + 1) \). So \( P(n) \) implies \( P(n + 1) \).

*Conclusion.* By @ax-induction, started at \( 1 \), \( P(n) \) holds for every natural number \( n \ge 1 \).

Notice where the induction hypothesis entered: exactly once, to replace the sum of the first \( n \) terms by a closed expression. A proof by induction that never uses its induction hypothesis is either not an induction or is hiding a gap.
:::

The inductive step of an inequality usually has a second ingredient besides the hypothesis: a crude estimate that finishes the job.

::: {#exm-power-inequality}
[An inequality by induction]

Prove that \( 3^n \ge 2n + 1 \) for every \( n \in \nN \).
:::

::: {.solution}
Let \( P(n) \) be "\( 3^n \ge 2n + 1 \)".

*Base case.* \( 3^0 = 1 = 2 \cdot 0 + 1 \), so \( P(0) \) holds.

*Inductive step.* Let \( n \in \nN \) and suppose \( 3^n \ge 2n + 1 \). Then
\[
3^{n + 1} = 3 \cdot 3^n \ge 3(2n + 1) = 6n + 3 \ge 2n + 3 = 2(n + 1) + 1 ,
\]
where the first inequality multiplies the induction hypothesis by the positive number \( 3 \), and the second uses \( 6n \ge 2n \), true because \( n \ge 0 \). So \( P(n + 1) \) holds.

*Conclusion.* By @ax-induction, \( 3^n \ge 2n + 1 \) for every \( n \in \nN \).

The estimate \( 6n + 3 \ge 2n + 3 \) throws away a great deal. That is typical: the step needs only to reach \( P(n + 1) \), not to reach it tightly, and a generous estimate that is obviously true is better than a sharp one that needs its own proof.
:::

::: {.warning}
The inductive step must hold for **every** \( n \), including the first transition. Try to prove "\( 2^n \ge n^2 \) for every \( n \in \nN \)": the base case \( 1 \ge 0 \) holds, and the step \( 2^{n + 1} = 2 \cdot 2^n \ge 2n^2 \ge (n + 1)^2 \) looks fine, but its last inequality holds only for \( n \ge 3 \), so the steps from \( 0 \) to \( 1 \), from \( 1 \) to \( 2 \) and from \( 2 \) to \( 3 \) are not covered. The claim survives the first two gaps (at \( n = 1 \), \( 2 \ge 1 \), and at \( n = 2 \) both sides are \( 4 \)), but it is false at \( n = 3 \), where \( 2^3 = 8 < 9 = 3^2 \); it is true again from \( n = 4 \) on. *Sets, Relations, and Cardinality*, Chapter 2 shows a famous "proof" that fails in the same way at its very first step, from \( 1 \) to \( 2 \).
:::

## Strong induction

Sometimes the step from \( n \) to \( n + 1 \) is the wrong shape. The immediate parts of a formula \( (\varphi \circ \psi) \) are shorter than it, but not by exactly one symbol; a natural number may be best understood through a smaller one that is not its predecessor. In such cases we want to assume the property not just for \( n \), but for **every** smaller number.

*If a property holds for \( n \) whenever it holds for all smaller numbers, then it holds for every number.*

::: {#thm-strong-induction}
[Strong Induction]

Let \( P(n) \) be a property of natural numbers. Suppose that **for every** \( n \in \nN \): if \( P(k) \) holds for **every** \( k \in \nN \) with \( k < n \), then \( P(n) \) holds. Then \( P(n) \) holds for every \( n \in \nN \).
:::

This form is also called **course-of-values induction**: the hypothesis may use the whole course of values \( P(0), \dots, P(n - 1) \), not just the last one. Its induction hypothesis is stronger (we assume more), so its step is easier to prove; the theorem says we lose nothing by it.

There seems to be no base case. There is one, hidden. For \( n = 0 \), the hypothesis says: if \( P(k) \) holds for every \( k \in \nN \) with \( k < 0 \), then \( P(0) \) holds. No natural number is less than \( 0 \), so "\( P(k) \) holds for every \( k \in \nN \) with \( k < 0 \)" is **vacuously** true: for each \( k \in \nN \), the implication "if \( k < 0 \), then \( P(k) \)" has a false hypothesis, and an implication with a false hypothesis holds (@prp-vacuous-implication, \( \neg P \vdash P \to Q \)). So at \( n = 0 \) the hypothesis of the theorem hands us \( P(0) \) outright. In practice, the proof of the step usually treats small \( n \) separately, and that is where the base cases live.

::: {.idea}
Strong induction is ordinary induction applied to a stronger property. Let \( Q(n) \) say "\( P(k) \) holds for **every** \( k \le n \)". Then \( Q(n) \) is exactly the hypothesis the theorem needs at \( n + 1 \), since the numbers below \( n + 1 \) are those up to \( n \); so the theorem's hypothesis moves us from \( Q(n) \) to \( Q(n + 1) \). Ordinary induction on \( Q \) does the rest, and \( Q(n) \) contains \( P(n) \).
:::

::: {.proof}
Suppose the hypothesis of the theorem holds. For \( n \in \nN \), let \( Q(n) \) be the property "\( P(k) \) holds for every \( k \in \nN \) with \( k \le n \)". We prove \( Q(n) \) for every \( n \) by @ax-induction.

*Base case.* No natural number is less than \( 0 \), so \( P(k) \) holds for every \( k \in \nN \) with \( k < 0 \), vacuously. By the hypothesis of the theorem at \( n = 0 \), \( P(0) \) holds. The only \( k \in \nN \) with \( k \le 0 \) is \( 0 \), so \( Q(0) \) holds.

*Inductive step.* Let \( n \in \nN \) and suppose \( Q(n) \). The natural numbers \( k < n + 1 \) are exactly those with \( k \le n \), since no natural number lies strictly between \( n \) and \( n + 1 \). So \( Q(n) \) says that \( P(k) \) holds for every \( k \in \nN \) with \( k < n + 1 \), and the hypothesis of the theorem at \( n + 1 \) gives \( P(n + 1) \). A natural number \( k \le n + 1 \) satisfies \( k \le n \) or \( k = n + 1 \), and \( P(k) \) holds in both cases. Hence \( Q(n + 1) \).

By @ax-induction, \( Q(n) \) holds for every \( n \in \nN \). Given \( n \in \nN \), \( Q(n) \) applied to \( k = n \) gives \( P(n) \). This proves the theorem.
:::

::: {.check}
In the proof of @thm-strong-induction, to which property is @ax-induction applied, and why is it not applied to \( P(n) \) itself?
:::

::: {.solution}
To \( Q(n) \): "\( P(k) \) holds for every \( k \in \nN \) with \( k \le n \)". Applied to \( P(n) \) itself, ordinary induction would give us only \( P(n) \) as induction hypothesis, while the hypothesis of the theorem at \( n + 1 \) asks for \( P(k) \) at **every** \( k \le n \). The property \( Q \) carries exactly that information from one step to the next.
:::

The first use shows the typical shape: the step splits into a few small cases, handled directly, and a general case that reaches back further than one.

::: {#exm-threes-and-fives}
[Threes and fives]

Prove that every natural number \( n \ge 8 \) is a sum of threes and fives: \( n = 3a + 5b \) for some integers \( a, b \ge 0 \).
:::

::: {.solution}
Ordinary induction is awkward here. From \( n = 3a + 5b \) we cannot easily reach \( n + 1 \): we would have to trade some threes for fives or the other way round, and there may be none of the kind we want to trade. Going back **three** steps is easy instead: if \( n - 3 \) is a sum of threes and fives, add one more three. So we use strong induction.

For \( n \in \nN \), let \( P(n) \) be "if \( n \ge 8 \), then \( n = 3a + 5b \) for some integers \( a, b \ge 0 \)". Let \( n \in \nN \), and suppose \( P(k) \) holds for every \( k \in \nN \) with \( k < n \). We show \( P(n) \).

*Case \( n < 8 \).* Then the hypothesis "\( n \ge 8 \)" of \( P(n) \) is false, and \( P(n) \) holds vacuously.

*Cases \( n = 8, 9, 10 \).* Directly: \( 8 = 3 + 5 \), \( 9 = 3 \cdot 3 \), \( 10 = 5 \cdot 2 \).

*Case \( n \ge 11 \).* Let \( k = n - 3 \). Then \( k \ge 8 \), so \( k \in \nN \), and \( k < n \). By the induction hypothesis \( P(k) \), there are integers \( a, b \ge 0 \) with \( n - 3 = 3a + 5b \). Then \( n = 3(a + 1) + 5b \), with \( a + 1 \ge 0 \) and \( b \ge 0 \).

In every case \( P(n) \) holds. By @thm-strong-induction, \( P(n) \) holds for every \( n \in \nN \): every \( n \ge 8 \) is a sum of threes and fives.

The three direct cases are the base cases. They are needed because the general case reaches back three steps: for \( n = 8, 9, 10 \), the number \( n - 3 \) is \( 5, 6, 7 \), which is below \( 8 \), and there the induction hypothesis \( P(n - 3) \) is vacuous and gives us nothing. The bound \( 8 \) cannot be lowered: \( 7 \) is not a sum of threes and fives, since neither \( 7 \) nor \( 7 - 5 = 2 \) is a multiple of \( 3 \).
:::

## Exercises

### A. Check your understanding

::: {#exr-induction-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. For each statement, say which kind of induction fits best (ordinary, strong, structural), and write down its base case(s) and the statement of its inductive step, without proving them: (i) \( 4^n - 1 \) is divisible by \( 3 \) for every \( n \in \nN \); (ii) every natural number \( n \ge 12 \) is \( 4a + 5b \) for some integers \( a, b \ge 0 \); (iii) every formula contains an atom or \( \bot \).
2. True or false, with a reason: to apply @thm-strong-induction, one must first check \( P(0) \) separately.
3. In the proof of @thm-structural-induction, on what is the strong induction performed?
4. Which parts of @lem-parenthesis-count does the proof of @thm-unique-readability use, and for which formulas?
5. Where in the proof of @thm-structural-recursion is @thm-unique-readability used, and why is it not needed for uniqueness?
:::
:::

::: {.solution}
*(a)* (i) Ordinary induction. Base case: \( 4^0 - 1 = 0 \) is divisible by \( 3 \). Step: for every \( n \in \nN \), if \( 3 \mid 4^n - 1 \), then \( 3 \mid 4^{n + 1} - 1 \). (It holds because \( 4^{n + 1} - 1 = 4(4^n - 1) + 3 \).)

(ii) Strong induction, reaching back four: from \( n - 4 = 4a + 5b \) we get \( n = 4(a + 1) + 5b \). With \( P(n) \) "if \( n \ge 12 \), then \( n = 4a + 5b \) for some integers \( a, b \ge 0 \)", the step is: for every \( n \in \nN \), if \( P(k) \) holds for every \( k < n \), then \( P(n) \). Inside it, \( n < 12 \) is vacuous, and the base cases are \( n = 12, 13, 14, 15 \): \( 12 = 4 \cdot 3 \), \( 13 = 4 \cdot 2 + 5 \), \( 14 = 4 + 5 \cdot 2 \), \( 15 = 5 \cdot 3 \). For \( n \ge 16 \), \( k = n - 4 \ge 12 \) and \( k < n \), and the hypothesis \( P(n - 4) \) is used.

(iii) Structural induction. Base cases: an atom contains itself, and \( \bot \) contains \( \bot \). Steps: if \( \varphi \) contains an atom or \( \bot \), so does \( \neg\varphi \); if \( \varphi \) and \( \psi \) do, so does \( (\varphi \circ \psi) \), for each binary \( \circ \). (Compare the warning in the section: with "an atom" alone, the case \( \bot \) fails.)

*(b)* False. At \( n = 0 \) the hypothesis of @thm-strong-induction reads "if \( P(k) \) holds for every \( k \in \nN \) with \( k < 0 \), then \( P(0) \)", and its "if" part holds vacuously, since no natural number is less than \( 0 \). So proving the hypothesis for every \( n \) includes proving \( P(0) \); in practice small \( n \) are treated as separate cases inside the step, as in @exm-threes-and-fives.

*(c)* On the position \( i \) of an entry in a formation sequence \( \chi_1, \dots, \chi_m \) of the given formula, with the property "if \( 1 \le i \le m \), then \( \chi_i \) has \( P \)". Not on the height, which at that point is not yet known to be well defined.

*(d)* Part (a) for \( \varphi \), to get excess \( 1 \) before the main connective and to get excess \( 1 + 0 \) before the part \( \psi \); part (c) for \( \varphi \) and for \( \psi \), to get excess at least \( 2 \) before every other binary connective. Here \( \chi = (\varphi \circ \psi) \) is the formula being read. Part (b) is not used in that proof.

*(e)* In the inductive step, to define \( h(\chi) \) for a formula \( \chi \) of length \( n + 1 \): unique readability says which clause applies and to which parts, so the clauses give exactly one value. That two functions obeying the clauses agree needs no unique readability: by @thm-structural-induction, if \( f \) and \( f' \) both obey the clauses, they agree at atoms and \( \bot \); and if they agree at \( \varphi \) (and \( \psi \)), then at \( \neg\varphi \) both equal \( g_\neg(\varphi, f(\varphi)) \), and at \( (\varphi \circ \psi) \) both equal \( g_\circ(\varphi, \psi, f(\varphi), f(\psi)) \), whichever way the string may be split.
:::

### B. Practice

::: {#exr-induction-b1}
[B1]

Prove that \( 2^n \ge n + 1 \) for every \( n \in \nN \).
:::

::: {.solution}
Let \( P(n) \) be "\( 2^n \ge n + 1 \)".

*Base case.* \( 2^0 = 1 = 0 + 1 \), so \( P(0) \) holds.

*Inductive step.* Let \( n \in \nN \) and suppose \( 2^n \ge n + 1 \). Then
\[
2^{n + 1} = 2 \cdot 2^n \ge 2(n + 1) = 2n + 2 \ge n + 2 = (n + 1) + 1 ,
\]
where the first inequality multiplies the induction hypothesis by \( 2 > 0 \), and the second uses \( n \ge 0 \). So \( P(n + 1) \) holds.

By @ax-induction, \( 2^n \ge n + 1 \) for every \( n \in \nN \).
:::

### C. Going deeper

<!-- S3-PLACEHOLDER: items -->

<!-- dependency ledger
ax-induction (claim): each P(n) alone has a finite derivation from P(0) and the step by ->E | informal, motivation only; not used in any proof
exm-sum-consecutive-products (example): the sum 1*2 + ... + n(n+1) read as "the sum of the first n terms, plus the next"; algebra of fractions | school algebra (blueprint, Allowed prerequisites); recursion on N (finite sums) is F2.2 (promised; STATUS row "definition by recursion", from AN1.1); checked by verify/ch04/exm-sum-consecutive-products.py
exm-power-inequality (example): 3^(n+1) = 3 * 3^n; multiplying an inequality by a positive number; 6n >= 2n for n >= 0 | school algebra; powers by recursion are F2.2 (promised; STATUS row, from AN1.1); checked by verify/ch04/exm-power-inequality.py
ax-induction (example): (the warning after exm-power-inequality) 2n^2 >= (n+1)^2 exactly for n >= 3 (fails at n = 0, 1, 2); 2^3 = 8 < 9; 2^n >= n^2 for n = 0, 1, 2 and n >= 4 | school algebra; checked by verify/ch04/ax-induction.py
thm-strong-induction (proof): no natural number is less than 0; k < n + 1 iff k <= n for natural k (nothing strictly between n and n + 1); k <= n + 1 iff k <= n or k = n + 1 | school facts about N (blueprint, Allowed prerequisites); F2.2 (promised; STATUS row "nothing between n and n + 1", from AN1.1)
thm-strong-induction (proof): "for every k < 0, P(k)" holds vacuously | prp-vacuous-implication (cited in the prose before the proof); the rule for "every" is F1.4 (prose pointer)
exm-threes-and-fives (example): 8 = 3 + 5, 9 = 3*3, 10 = 5*2; 7 is not a sum of threes and fives | inline arithmetic; checked by verify/ch04/exm-threes-and-fives.py
exr-induction-a1 (solution): 4^(n+1) - 1 = 4(4^n - 1) + 3; 12..15 as 4a + 5b | school algebra; checked by verify/ch04/exr-induction-a1.py
-->
