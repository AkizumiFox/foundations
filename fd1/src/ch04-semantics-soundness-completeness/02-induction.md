# Induction on the Natural Numbers

Section 4.1 made formulas into objects: strings built from atoms and \( \bot \) by the clauses of @def-formula, and by nothing else. There are infinitely many of them, and the theorems this chapter is heading for are about all of them. This section supplies the tool for proving anything about infinitely many objects at once. It is **induction** on the natural numbers, where it is familiar. Section 4.3 carries it over to formulas, where the chapter needs it most.

## One argument for infinitely many cases

Here is a claim about every formula: *every formula has as many left parentheses as right ones.* It is believable. The clause (F3) of @def-formula adds one of each, and the other clauses add none. But the claim is about infinitely many strings, and checking them one by one never ends.

The belief already contains the shape of a proof. Every formula is reached by finitely many building steps from atoms and \( \bot \) (clause (F4)). The starting pieces have no parentheses, so they have equally many of each kind. Each building step turns formulas that balance into a formula that balances. So, step by step along any formation sequence, balance is never lost, and every formula balances.

Exactly the same shape appears with numbers. To show that some property holds for every natural number, show that it holds for \( 0 \), and that it passes from each number to the next. Every natural number is reached from \( 0 \) by finitely many steps of "add one", so the property is never lost. This is **induction**. We state it for numbers first, because it is simpler there, then prove the version for formulas from it.

As in Chapters 1 and 2, "for every \( n \in \nN \)" and "there is a \( k \)" are used in their everyday sense. As in the rest of the book, \( \nN = \{0, 1, 2, \dots\} \) starts at \( 0 \), and the arithmetic and order of the natural numbers are school facts.

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

In symbols (here \( \forall \) abbreviates the words "for every"):
\[
\Bigl( P(0) \ \wedge \ \forall n \in \nN \ \bigl( P(n) \to P(n + 1) \bigr) \Bigr)
\ \to \ \forall n \in \nN \ P(n) .
\]

In words: hypothesis (i) is the **base case**. Hypothesis (ii) is the **inductive step**, and inside it, the assumption "\( P(n) \) holds" is the **induction hypothesis**. The step is **one** implication, proved **once**, for a number \( n \) about which we assume nothing except that it is a natural number with \( P(n) \). The conclusion is about every natural number at once.

**Its status.** We take @ax-induction as a basic property of \( \nN \), given and not proved. It is, in a precise sense, what the three dots in \( \{0, 1, 2, \dots\} \) mean: the natural numbers are what we reach from \( 0 \) by adding one, again and again, and nothing else. Every later use cites this principle.

**Dominoes.** The usual picture is a row of dominoes, one for each natural number. The base case knocks over the first. The inductive step says that each domino, if it falls, knocks over the next. Then every domino falls. The picture carries the one point that matters: the step must work for **every** \( n \), the first transition from \( 0 \) to \( 1 \) included. A single domino standing too far from the next stops the whole row, however well the others are placed.

::: {.second-reading title="Why induction is not a rule of logic"}
**Not an infinite derivation.** From \( P(0) \) and the instances \( P(0) \to P(1) \), \( P(1) \to P(2) \), \dots{} of the step we could derive \( P(1) \) by \( \rulename{{\to}E} \), then \( P(2) \), and so on; each single \( P(n) \) has a finite derivation, \( n \) lines long or so. But no finite derivation contains all of them, and "and so on" is not a rule. The principle of induction is what licenses the passage, in one step, from the two hypotheses to "for every \( n \)". It is a rule about \( \nN \), not a rule of logic.
:::

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

For now, "let \( n \in \nN \)" means what Chapter 1 made it mean (Section 1.1): one fixed number, not further specified.

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

::: {.check}
For the claim "\( 5^n - 1 \) is divisible by \( 4 \) for every \( n \in \nN \)", write down the base case and the statement of the inductive step, without proving the step.
:::

::: {.solution}
Base case: \( 5^0 - 1 = 0 = 4 \cdot 0 \). Step: for every \( n \in \nN \), if \( 4 \mid 5^n - 1 \), then \( 4 \mid 5^{n + 1} - 1 \). (It holds, since \( 5^{n + 1} - 1 = 5(5^n - 1) + 4 \).)
:::

::: {.warning}
The inductive step must hold for **every** \( n \), including the first transition. Try to prove "\( 2^n \ge n^2 \) for every \( n \in \nN \)": the base case \( 1 \ge 0 \) holds, and the step \( 2^{n + 1} = 2 \cdot 2^n \ge 2n^2 \ge (n + 1)^2 \) looks fine, but its last inequality holds only for \( n \ge 3 \), so the steps from \( 0 \) to \( 1 \), from \( 1 \) to \( 2 \) and from \( 2 \) to \( 3 \) are not covered. The claim survives the first two gaps (at \( n = 1 \), \( 2 \ge 1 \), and at \( n = 2 \) both sides are \( 4 \)), but it is false at \( n = 3 \), where \( 2^3 = 8 < 9 = 3^2 \); it is true again from \( n = 4 \) on.
:::

::: {.remark}
**A checklist for a proof by induction.** Before writing, and again after, answer five questions.

::: {.enumerate options="label=\arabic*."}
1. *Objects.* What does the induction run over: the natural numbers from \( 0 \), from some \( m \), the formulas, the lines of a derivation?
2. *Property.* Write \( P \) as an open sentence about **one** object. Everything the step will need must be inside it, restrictions such as "if \( n \ge 8 \)" included.
3. *Base cases.* Which objects does the step not reach from earlier ones: those not built from others, or, in strong induction, those whose step would reach outside the range? Check every one of them.
4. *Steps.* One for each way of building, proved for an arbitrary object, using the hypothesis only for objects built earlier: the one before, any earlier one, or the immediate parts.
5. *Principle.* Name it (@ax-induction, @thm-strong-induction) and say what it gives.
:::

Every induction in this chapter can be checked against these five questions, and Sections 4.3 and 4.7 do so.
:::

## Strong induction

Sometimes the step from \( n \) to \( n + 1 \) is the wrong shape. The immediate parts of a formula \( (\varphi \circ \psi) \) are shorter than it, but not by exactly one symbol; a natural number may be best understood through a smaller one that is not its predecessor. In such cases we want to assume the property not just for \( n \), but for **every** smaller number.

*If a property holds for \( n \) whenever it holds for all smaller numbers, then it holds for every number.*

::: {#thm-strong-induction}
[Strong Induction]

Let \( P(n) \) be a property of natural numbers. Suppose that **for every** \( n \in \nN \): if \( P(k) \) holds for **every** \( k \in \nN \) with \( k < n \), then \( P(n) \) holds. Then \( P(n) \) holds for every \( n \in \nN \).
:::

This form is also called **course-of-values induction**: the hypothesis may use the whole course of values \( P(0), \dots, P(n - 1) \), not just the last one. Its induction hypothesis is stronger (we assume more), so its step is easier to prove; the theorem says we lose nothing by it.

There seems to be no base case. There is one, hidden. For \( n = 0 \), the hypothesis says: if \( P(k) \) holds for every \( k \in \nN \) with \( k < 0 \), then \( P(0) \) holds. No natural number is less than \( 0 \), so "\( P(k) \) holds for every \( k \in \nN \) with \( k < 0 \)" is **vacuously** true: for each \( k \in \nN \), the implication "if \( k < 0 \), then \( P(k) \)" has a false hypothesis, and an implication with a false hypothesis holds (@prp-vacuous-implication: from \( \neg (k < 0) \) we get \( (k < 0) \to P(k) \)). So at \( n = 0 \) the hypothesis of the theorem hands us \( P(0) \) outright. In practice, the proof of the step usually treats small \( n \) separately, and that is where the base cases live.

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

## Proving more to prove less

Sometimes the step will not go through although the claim is true. The cure is surprising: prove more.

::: {#exm-strengthen-the-claim}
[Prove more to prove less]

For \( n \ge 1 \) let
\[
S_n = \frac{1}{1 \cdot 2} + \frac{1}{2 \cdot 3} + \dots + \frac{1}{n(n + 1)} .
\]
Show that \( S_n < 1 \) for every \( n \ge 1 \).
:::

::: {.solution}
*First try.* Let \( P(n) \) be "\( S_n < 1 \)". The base case holds: \( S_1 = \frac12 \). In the step, \( S_{n+1} = S_n + \frac{1}{(n+1)(n+2)} \), and the hypothesis \( S_n < 1 \) tells us nothing more about \( S_n \): a number \( x < 1 \) may exceed \( 1 - \frac{1}{(n+1)(n+2)} \), and then \( x + \frac{1}{(n+1)(n+2)} > 1 \). From \( S_n < 1 \) alone we cannot reach \( S_{n+1} < 1 \). The hypothesis is too weak to give \( P(n + 1) \). The claim is not to blame; the hypothesis is.

*Guess more.* \( S_1 = \frac12 \), \( S_2 = \frac12 + \frac16 = \frac23 \), \( S_3 = \frac23 + \frac{1}{12} = \frac34 \). Let \( Q(n) \) be "\( S_n = \frac{n}{n+1} \)".

*Base case.* \( S_1 = \frac12 = \frac{1}{1 + 1} \).

*Inductive step.* Let \( n \ge 1 \) and suppose \( S_n = \frac{n}{n+1} \). Then
\[
S_{n+1} = \frac{n}{n+1} + \frac{1}{(n+1)(n+2)} = \frac{n(n+2) + 1}{(n+1)(n+2)} = \frac{(n+1)^2}{(n+1)(n+2)} = \frac{n+1}{n+2} ,
\]
which is \( Q(n + 1) \).

*Conclusion.* By @ax-induction started at \( 1 \) ("Starting from another number"), \( Q(n) \) holds for every \( n \ge 1 \), and \( \frac{n}{n+1} < 1 \) gives the claim.

A stronger claim gives the step a stronger hypothesis to use, and asks the step to deliver more; here it can. The same need returns with formulas in Section 4.3, where facts about parentheses are proved together, because one of them, alone, does not pass through the step.
:::

::: {.check}
Run the checklist on @exm-threes-and-fives.
:::

::: {.solution}
Objects: the natural numbers. Property: "if \( n \ge 8 \), then \( n = 3a + 5b \) for some integers \( a, b \ge 0 \)", with the restriction inside. Base cases: \( 8, 9, 10 \), the numbers whose step would reach below \( 8 \) (for \( n < 8 \) the property holds vacuously). Step: for \( n \ge 11 \), the hypothesis for \( n - 3 \ge 8 \), an earlier number, and one more \( 3 \). Principle: @thm-strong-induction.
:::

::: {.remark}
[Looking ahead]

Chapter 5 gives "for every" and "there is" their rules, among them the step from "this \( n \) was arbitrary" to "for every \( n \)" that every inductive step takes.
:::

## Exercises

### A. Check your understanding

::: {#exr-induction-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. For each statement, say which kind of induction fits best (ordinary or strong), and write down its base case(s) and the statement of its inductive step, without proving them: (i) \( 4^n - 1 \) is divisible by \( 3 \) for every \( n \in \nN \); (ii) every natural number \( n \ge 12 \) is \( 4a + 5b \) for some integers \( a, b \ge 0 \).
2. True or false, with a reason: to apply @thm-strong-induction, one must first check \( P(0) \) separately.
3. A proof of "\( P(n) \) for every \( n \ge 5 \)" checks \( P(5) \) and proves "if \( P(n) \), then \( P(n + 1) \)" for every \( n \ge 5 \). Which form of @ax-induction is this, and why is \( P(4) \) never needed?
4. In @exm-strengthen-the-claim, why can "\( S_n < 1 \)" not serve as the induction hypothesis?
:::
:::

::: {.solution}
*(a)* (i) Ordinary induction. Base case: \( 4^0 - 1 = 0 \) is divisible by \( 3 \). Step: for every \( n \in \nN \), if \( 3 \mid 4^n - 1 \), then \( 3 \mid 4^{n + 1} - 1 \). (It holds because \( 4^{n + 1} - 1 = 4(4^n - 1) + 3 \).)

(ii) Strong induction, reaching back four: from \( n - 4 = 4a + 5b \) we get \( n = 4(a + 1) + 5b \). With \( P(n) \) "if \( n \ge 12 \), then \( n = 4a + 5b \) for some integers \( a, b \ge 0 \)", the step is: for every \( n \in \nN \), if \( P(k) \) holds for every \( k < n \), then \( P(n) \). Inside it, \( n < 12 \) is vacuous, and the base cases are \( n = 12, 13, 14, 15 \): \( 12 = 4 \cdot 3 \), \( 13 = 4 \cdot 2 + 5 \), \( 14 = 4 + 5 \cdot 2 \), \( 15 = 5 \cdot 3 \). For \( n \ge 16 \), \( k = n - 4 \ge 12 \) and \( k < n \), and the hypothesis \( P(n - 4) \) is used.

*(b)* False. At \( n = 0 \) the hypothesis of @thm-strong-induction reads "if \( P(k) \) holds for every \( k \in \nN \) with \( k < 0 \), then \( P(0) \)", and its "if" part holds vacuously, since no natural number is less than \( 0 \). So proving the hypothesis for every \( n \) includes proving \( P(0) \); in practice small \( n \) are treated as separate cases inside the step, as in @exm-threes-and-fives.

*(c)* Induction started at \( 5 \) ("Starting from another number"): @ax-induction applied to \( Q(m) \): "\( P(m + 5) \) holds". The claim is only about \( n \ge 5 \), and no step reaches below \( 5 \), so nothing about \( 4 \) is ever asked.

*(d)* It says nothing about how close \( S_n \) is to \( 1 \): a number \( x < 1 \) within \( \frac{1}{(n+1)(n+2)} \) of \( 1 \) has \( x + \frac{1}{(n+1)(n+2)} > 1 \), so from \( S_n < 1 \) alone the step cannot reach \( S_{n+1} < 1 \). The step would need a bound on how close \( S_n \) is to \( 1 \); the stronger \( S_n = \frac{n}{n+1} \) gives one (and so would \( S_n \le \frac{n}{n+1} \)).
:::

::: {#exr-induction-a2}
[A2: Drill]

The parts run from locating the hypothesis, through writing one base case or one step, to judging claims and running the checklist.

::: {.enumerate options="label=(\alph*)"}
1. In the inductive step of @exm-power-inequality, where is the induction hypothesis used?
2. Write down the base case and the step for "\( n^2 + n \) is even for every \( n \in \nN \)".
3. Ordinary or strong induction for "every \( n \ge 2 \) is a product of one or more primes"?
4. Write down \( P(n + 1) \) for the property \( P(n) \): "\( 1 + 3 + \dots + (2n - 1) = n^2 \)" (\( n \ge 1 \)).
5. Write down the base case for "\( n! \ge 2^n \) for every \( n \ge 4 \)" (here \( n! = 1 \cdot 2 \cdots n \)).
6. Does checking \( P(0) \), \( P(1) \) and \( P(2) \) prove the step "if \( P(n) \), then \( P(n + 1) \)"?
7. "\( n^2 - n + 41 \) is prime" holds for \( n = 0, 1, \dots, 40 \). Is it true for every \( n \in \nN \)?
8. A proof shows \( P(0) \) and "if \( P(n) \), then \( P(n + 2) \)" for every \( n \in \nN \). For which \( n \) is \( P(n) \) proved?
9. In @thm-strong-induction, what may the step assume when \( n = 3 \)?
10. Run items 1–3 of the checklist on @exm-sum-consecutive-products.
11. In the step for "\( 3 \mid n^3 + 2n \) for every \( n \in \nN \)", \( (n + 1)^3 + 2(n + 1) = (n^3 + 2n) + 3(n^2 + n + 1) \). Is the hypothesis enough to finish the step?
12. For "\( S_n < 1 \)" in @exm-strengthen-the-claim, which item of the checklist failed on the first try?
:::
:::

::: {.solution}
(a) In \( 3 \cdot 3^n \ge 3(2n + 1) \).

(b) Base: \( 0^2 + 0 = 0 \) is even. Step: if \( n^2 + n \) is even, then so is \( (n + 1)^2 + (n + 1) = (n^2 + n) + 2(n + 1) \).

(c) Strong: a composite \( n = ab \) with \( 1 < a, b < n \) reaches back to \( a \) and \( b \), not to \( n - 1 \).

(d) \( 1 + 3 + \dots + (2n - 1) + (2n + 1) = (n + 1)^2 \).

(e) \( 4! = 24 \ge 16 = 2^4 \).

(f) No. The step is one implication for **every** \( n \); three checked cases prove those three cases only.

(g) No: at \( n = 41 \) the value is \( 41^2 - 41 + 41 = 41^2 \), not a prime. Checked cases are not a proof.

(h) For the even \( n \) only.

(i) \( P(0) \), \( P(1) \) and \( P(2) \).

(j) Objects: the natural numbers \( n \ge 1 \). Property: the displayed equation for \( n \). Base case: \( n = 1 \), where \( 1 \cdot 2 = 2 = \frac{1 \cdot 2 \cdot 3}{3} \).

(k) Yes: \( n^3 + 2n \) is a multiple of \( 3 \) by hypothesis, and so is \( 3(n^2 + n + 1) \).

(l) Item 2: the property was too weak for the step (item 4) to go through.
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

::: {#exr-induction-b4}
[B2: Divisible by six]

Prove by induction that \( n^3 - n \) is divisible by \( 6 \) for every \( n \in \nN \). You may use that \( n(n + 1) \) is even for every \( n \in \nN \).
:::

::: {.solution}
Let \( P(n) \) be "\( 6 \mid n^3 - n \)".

*Base case.* \( 0^3 - 0 = 0 = 6 \cdot 0 \), so \( P(0) \) holds.

*Inductive step.* Let \( n \in \nN \) and suppose \( 6 \mid n^3 - n \). Expanding,
\[
(n + 1)^3 - (n + 1) = n^3 + 3n^2 + 2n = (n^3 - n) + 3n(n + 1) .
\]
By the induction hypothesis, \( 6 \mid n^3 - n \). Since \( n(n + 1) \) is even, \( n(n + 1) = 2m \) for some integer \( m \), and \( 3n(n + 1) = 6m \). A sum of two multiples of \( 6 \) is a multiple of \( 6 \), so \( P(n + 1) \) holds.

*Conclusion.* By @ax-induction, \( 6 \mid n^3 - n \) for every \( n \in \nN \).

**Marking scheme.** (6 points)

- 1: states the property \( P(n) \).
- 1: base case.
- 3: inductive step: the identity (1), the use of the induction hypothesis (1), the evenness of \( n(n + 1) \) (1).
- 1: names the principle.
:::

::: {#exr-induction-b5}
[B3: Two base cases]

A sequence is given by \( a_0 = 2 \), \( a_1 = 3 \), and \( a_{n+2} = 3a_{n+1} - 2a_n \) for \( n \in \nN \). Prove that \( a_n = 2^n + 1 \) for every \( n \in \nN \). Which form of induction do you use, and why does it need two base cases?
:::

::: {.solution}
We use @thm-strong-induction with \( P(n) \): "\( a_n = 2^n + 1 \)". Let \( n \in \nN \), and suppose \( P(k) \) for every \( k < n \).

*Cases \( n = 0, 1 \).* \( a_0 = 2 = 2^0 + 1 \) and \( a_1 = 3 = 2^1 + 1 \).

*Case \( n \ge 2 \).* Then \( n - 1 \) and \( n - 2 \) are natural numbers less than \( n \), so \( P(n - 1) \) and \( P(n - 2) \) hold, and
\[
a_n = 3a_{n-1} - 2a_{n-2} = 3(2^{n-1} + 1) - 2(2^{n-2} + 1) = 3 \cdot 2^{n-1} - 2^{n-1} + 1 = 2^n + 1 .
\]
(Check: \( a_2 = 3 \cdot 3 - 2 \cdot 2 = 5 = 2^2 + 1 \).)

By @thm-strong-induction, \( a_n = 2^n + 1 \) for every \( n \in \nN \). The step reaches back two places, so it cannot be used at \( n = 0 \) or \( n = 1 \), where \( n - 2 \) is not a natural number: those two are the base cases.

**Marking scheme.** (6 points)

- 1: names strong induction (or ordinary induction on "\( P(n) \) and \( P(n + 1) \)").
- 2: both base cases.
- 2: the step, with the hypothesis used at \( n - 1 \) and at \( n - 2 \).
- 1: says why there are two base cases.
:::

### C. Going deeper

::: {#exr-induction-c4}
[C1: Find the error]

Claim: for every \( n \ge 1 \),
\[
1 + 2 + \dots + n = \frac{n^2 + n + 2}{2} .
\]
"Proof": suppose it holds for \( n \). Then
\[
1 + \dots + n + (n + 1) = \frac{n^2 + n + 2}{2} + (n + 1) = \frac{n^2 + 3n + 4}{2} = \frac{(n+1)^2 + (n+1) + 2}{2} ,
\]
so it holds for \( n + 1 \); by induction it holds for every \( n \ge 1 \).

::: {.enumerate options="label=(\alph*)"}
1. Is the claim true for any \( n \ge 1 \)?
2. Which item of the checklist fails, and which part of the "proof" is correct?
3. Show that the same step "proves" \( 1 + \dots + n = \frac{n^2 + n}{2} + c \) for every number \( c \). What singles out \( c = 0 \)?
:::
:::

::: {.solution}
*(a)* No. The true sum is \( \frac{n^2 + n}{2} \): that is the case \( c = 0 \) of (c), whose step is correct, with the base case \( 1 = \frac{1 + 1}{2} \). The claimed value is larger by \( 1 \) for every \( n \).

*(b)* Item 3: no base case is checked, and at \( n = 1 \) it fails, since the left side is \( 1 \) and the right side \( \frac{1 + 1 + 2}{2} = 2 \). The step itself is correct algebra.

*(c)* For every \( c \),
\[
\frac{n^2 + n}{2} + c + (n + 1) = \frac{n^2 + 3n + 2}{2} + c = \frac{(n+1)^2 + (n+1)}{2} + c ,
\]
so a correct step passes any constant along. Only the base case decides \( c \): at \( n = 1 \), \( 1 = 1 + c \) forces \( c = 0 \).

**Marking scheme.** (10 points)

- 3: (a), with the true sum.
- 4: (b), naming the missing base case and endorsing the step.
- 3: (c).

Fatal error (0 for (b)): calling the step wrong, or claiming the formula holds at \( n = 1 \).
:::

::: {#exr-induction-c5}
[C2: Prove more]

Prove that for every \( n \ge 2 \),
\[
\Bigl(1 - \frac14\Bigr)\Bigl(1 - \frac19\Bigr) \cdots \Bigl(1 - \frac{1}{n^2}\Bigr) > \frac12 .
\]
Write \( R_n \) for this product. First show that the hypothesis \( R_n > \frac12 \) alone, with \( R_{n+1} = R_n \bigl(1 - \frac{1}{(n+1)^2}\bigr) \), does not give \( R_{n+1} > \frac12 \); then prove more.
:::

::: {.solution}
[Hint 1]

Compute the product for \( n = 2, 3, 4 \) as fractions.
:::

::: {.solution}
[Hint 2]

Write \( R_2, R_3, R_4 \) with denominators \( 4, 6, 8 \) and guess a formula for the product; then prove that formula by induction.
:::

::: {.solution}
*The plain claim.* The step multiplies by \( 1 - \frac{1}{(n+1)^2} < 1 \), and the hypothesis \( R_n > \frac12 \) tells us nothing more about \( R_n \): for a number \( x \) just above \( \frac12 \), such as \( x = \frac12 + \frac{1}{4(n+1)^2} \), the number \( x \bigl(1 - \frac{1}{(n+1)^2}\bigr) \) is below \( \frac12 \), so the hypothesis alone does not give the claim for \( n + 1 \).

*Prove more.* \( R_2 = \frac34 \), \( R_3 = \frac34 \cdot \frac89 = \frac23 \), \( R_4 = \frac23 \cdot \frac{15}{16} = \frac58 \) suggest \( R_n = \frac{n+1}{2n} \). Base case \( n = 2 \): \( R_2 = \frac34 = \frac{2 + 1}{2 \cdot 2} \). Step: let \( n \ge 2 \) and suppose \( R_n = \frac{n+1}{2n} \). Then
\[
R_{n+1} = \frac{n+1}{2n} \cdot \frac{(n+1)^2 - 1}{(n+1)^2} = \frac{n+1}{2n} \cdot \frac{n(n+2)}{(n+1)^2} = \frac{n+2}{2(n+1)} .
\]
By @ax-induction started at \( 2 \), \( R_n = \frac{n+1}{2n} \) for every \( n \ge 2 \), and so \( R_n = \frac12 + \frac{1}{2n} > \frac12 \).

**Marking scheme.** (10 points)

- 2: argues that the plain claim does not pass through the step.
- 2: states the stronger claim.
- 2: base case.
- 3: the algebra of the step.
- 1: the conclusion, naming the principle.

Fatal error (0 for the step): "proving" the step from \( R_n > \frac12 \) alone.
:::

<!-- dependency ledger
ax-induction (claim): each P(n) alone has a finite derivation from P(0) and the instances P(k) -> P(k+1) of the step by ->E | informal, motivation only; not used in any proof
ax-induction (claim): (Starting from another number) n >= b implies n - b in N and n = b + (n - b); b + m >= b | school facts about N (blueprint, Allowed prerequisites)
exm-sum-consecutive-products (example): the sum 1*2 + ... + n(n+1) read as "the sum of the first n terms, plus the next"; algebra of fractions | school algebra (blueprint, Allowed prerequisites); recursion on N (finite sums) is F2.2 (promised; STATUS row F1.3 §02, paid by thm-recursion, def-sum-product); checked by verify/ch04/exm-sum-consecutive-products.py
exm-power-inequality (example): 3^(n+1) = 3 * 3^n; multiplying an inequality by a positive number; 6n >= 2n for n >= 0 | school algebra; powers by recursion are F2.2 (promised; STATUS row F1.3 §02, paid by def-power); checked by verify/ch04/exm-power-inequality.py
ax-induction (example): (the warning after exm-power-inequality) 2n^2 >= (n+1)^2 exactly for n >= 3 (fails at n = 0, 1, 2); 2^3 = 8 < 9; 2^n >= n^2 for n = 0, 1, 2 and n >= 4 | school algebra; checked by verify/ch04/ax-induction.py
thm-strong-induction (proof): no natural number is less than 0; k < n + 1 iff k <= n for natural k (nothing strictly between n and n + 1); k <= n + 1 iff k <= n or k = n + 1 | school facts about N (blueprint, Allowed prerequisites); F2.2 (promised; STATUS row F1.3 §02, paid by lem-naturals-arithmetic (e))
thm-strong-induction (proof): "for every k < 0, P(k)" holds vacuously | prp-vacuous-implication (cited in the prose before the proof); the rule for "every" is F1.4 (prose pointer)
exm-threes-and-fives (example): 8 = 3 + 5, 9 = 3*3, 10 = 5*2; 7 is not a sum of threes and fives | inline arithmetic; checked by verify/ch04/exm-threes-and-fives.py
exr-induction-a1 (solution): 4^(n+1) - 1 = 4(4^n - 1) + 3; 12..15 as 4a + 5b | school algebra; checked by verify/ch04/exr-induction-a1.py
ax-induction (claim): (the Quick check after exm-power-inequality) 5^0 - 1 = 0; 5^(n+1) - 1 = 5(5^n - 1) + 4 | school algebra; checked by verify/ch04/ax-induction.py
exm-strengthen-the-claim (example): sums of fractions; S_1, S_2, S_3 = 1/2, 2/3, 3/4; the guess S_n = n/(n+1) and its step algebra; a number x < 1 with x + 1/((n+1)(n+2)) > 1 | school algebra; finite sums by recursion are F2.2 (promised, as for exm-sum-consecutive-products; STATUS row F1.3 §02, paid by thm-recursion, def-sum-product); checked by verify/ch04/exm-strengthen-the-claim.py
exr-induction-a1 (solution): (c) induction started at 5 is ax-induction applied to Q(m) = P(m + 5) | "Starting from another number" (this section)
exr-induction-a2 (solution): (b) (n+1)^2 + (n+1) = (n^2 + n) + 2(n + 1); (e) 4! = 24 >= 16; (g) 41^2 - 41 + 41 = 41^2; (k) (n+1)^3 + 2(n+1) = (n^3 + 2n) + 3(n^2 + n + 1) | school arithmetic (factorial: school arithmetic); checked by verify/ch04/exr-induction-a2.py
exr-induction-b4 (solution): (n+1)^3 - (n+1) = (n^3 - n) + 3n(n+1); n(n+1) even | school algebra; evenness stated in the item; parity is F2.2 (promised: parity); checked by verify/ch04/exr-induction-b4.py
exr-induction-b5 (solution): a sequence given by recursion; a_n = 2^n + 1 from the recursion | the sequence is the item's own; sequences by recursion are F2.2 (promised); checked by verify/ch04/exr-induction-b5.py
exr-induction-c4 (solution): 1 + ... + n = (n^2 + n)/2; the step passes any constant c along | school algebra; checked by verify/ch04/exr-induction-c4.py
exr-induction-c5 (solution): R_2, R_3, R_4 = 3/4, 2/3, 5/8; x = 1/2 + 1/(4(n+1)^2) has x(1 - 1/(n+1)^2) < 1/2; R_n = (n+1)/(2n) and its step algebra | school algebra; checked by verify/ch04/exr-induction-c5.py
-->
