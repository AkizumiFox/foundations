# Checking Proofs, and What Is Not Allowed

A reader working alone must judge proofs, including their own, and is the person least able to do it. The remedy is procedural. This section gives two questions to ask of every line and a catalogue of the errors that recur, each tied to the rule of Chapters 1–4 that it breaks, and then checks four short proofs line by line.

## Two questions for every line

A proof is correct when every line is licensed: by @def-derivation, each line is a premise (a hypothesis, a proved result or a true school fact), an assumption, or one rule applied to available lines. So checking a proof means asking two questions of every line, with the answers in two columns.

- **Is it true?** Is the line correct whenever the hypotheses and the assumptions of the open boxes are true?
- **Does it follow, and by which rule?** From which available lines, and by which rule?

*The first column finds where to look; the second decides.*

The two questions are different. A line can be **true and not follow**: a correct fact the proof has not earned. This is the dangerous case, because nothing about the line looks wrong. A line can also **follow and be false**: false in a situation where the hypotheses and open assumptions are true. Since the rules never lead from true lines to a false one (@thm-soundness; Section 4.11 for predicate logic), some line it rests on, neither a hypothesis nor an open assumption, is false there too; follow it back until the second column fails. (Proof C's "\( 1 \) is even" is true given its box's assumption.)

::: {.check}
A proof that \( n^2 \ge n \) for every integer \( n \) opens with the line "\( n^2 - n = n(n - 1) \ge 0 \)". Is the line true? Does it follow? Would the answers change if \( n \) ranged over the reals?
:::

::: {.solution}
For an integer \( n \) the line is true: no integer lies strictly between \( 0 \) and \( 1 \), so \( n \le 0 \) (both factors \( \le 0 \)) or \( n \ge 1 \) (both \( \ge 0 \)). But as written it follows from nothing: it is the goal rearranged, without the case split that makes it true. For real \( n \) it is false at \( n = 1/2 \), where \( n(n - 1) = -1/4 \). The first column depends on the situation; the second fails in both.
:::

## The catalogue

Most wrong proofs fail in one of a few ways, each breaking a particular rule.

::: {#exm-not-allowed-catalogue}
[What is not allowed]

Each entry names the error, the rule it breaks and where that rule lives, and a failing instance whose conclusion is marked **true** or **false**: a wrong argument can reach either.

::: {.enumerate options="label=(N\arabic*)"}
1. **Verifying instances and concluding "for all".** Breaks \( \rulename{\forall I} \), which needs one proof about a fresh name (@def-rules-universal, Section 4.4). Instance: \( n^2 - n + 11 \) is prime for \( n = 0, 1, \dots, 10 \) (the values are \( 11, 11, 13, 17, 23, 31, 41, 53, 67, 83, 101 \)), "so it is prime for every \( n \in \nN \)". **False:** at \( n = 11 \) the value is \( 121 = 11^2 \).
2. **A witness that depends on a variable introduced later, while uniformity is claimed.** Breaks the side conditions of \( \rulename{\exists E} \) and \( \rulename{\forall I} \): a witness \( \delta_0 \) obtained inside the box of \( x_0 \) may not leave it (Section 4.10, @exm-converse-fails). Instance: "\( x^2 \) is continuous at every \( x \), with \( \delta = \min\{1, \varepsilon/(2\abs{x} + 1)\} \); so one \( \delta \) for each \( \varepsilon \) serves every \( x \), and \( x^2 \) is uniformly continuous on \( \nR \)". **False** (@exm-square-not-uniform).
3. **Treating the name from \( \rulename{\exists E} \) as arbitrary.** Breaks the side condition of \( \rulename{\forall I} \): the witness appears in the open assumption of its box (@def-rules-existential, Section 4.6). Instance: "Some element of \( A \) is positive; let \( x \) be such an element. Since \( x \) was arbitrary, every element of \( A \) is positive." **False** for \( A = \{-1, 1\} \).
4. **Reusing one witness name for two \( \rulename{\exists E} \)'s.** Breaks the fresh-name condition: the second name may not appear in an open assumption, and the first box's assumption mentions it (Section 4.6, @exm-sum-of-evens). Sibling boxes may share a name. Instance: "\( m \) and \( n \) are even, so \( m = 2k \) and \( n = 2k \) for an integer \( k \); hence \( m = n \)". **False:** \( m = 2 \), \( n = 4 \).
5. **Proving the converse.** Breaks \( \rulename{{\to}I} \), whose box opens with the hypothesis, not the conclusion (@def-rules-implication, Section 1.5). Instance: "If \( x^2 > 1 \), then \( x > 1 \): suppose \( x > 1 \); then \( x^2 > x > 1 \)." **False:** \( x = -2 \). Argument B of Section 1.1 makes the same move with a **true** conclusion.
6. **Affirming the consequent; denying the antecedent.** Breaks @def-derivation (Section 1.5), being no rule: \( P \to Q \) with \( Q \) gives no \( P \), and with \( \neg P \) gives no \( \neg Q \). Each pattern has a refuting row, so no derivation exists (@cor-refuting-row, Section 3.5): @exm-affirming-the-consequent, and for denying the row \( P \) false, \( Q \) true. Instances: "a multiple of \( 4 \) is even and \( 6 \) is even, so \( 6 \) is a multiple of \( 4 \)"; "… and \( 6 \) is not a multiple of \( 4 \), so \( 6 \) is not even". Both **false**.
7. **A missing case.** Breaks \( \rulename{\vee E} \), which needs one box for each disjunct (@def-rules-disjunction, Section 1.7). Instance: "\( \abs{x} > 0 \) for every real \( x \): every real \( x \) has \( x > 0 \), \( x = 0 \) or \( x < 0 \); if \( x > 0 \), \( \abs{x} = x > 0 \); if \( x < 0 \), \( \abs{x} = -x > 0 \)". **False:** the case \( x = 0 \) was dropped, and \( \abs{0} = 0 \).
8. **Cases that do not exhaust.** Breaks \( \rulename{\vee E} \), whose first input must be a disjunction already derived (Section 1.7). Instance: "\( x^2 \ge x \) for every real \( x \): either \( x \ge 1 \) or \( x \le 0 \); in the first case \( x^2 = x \cdot x \ge x \), in the second \( x^2 \ge 0 \ge x \)". **False:** \( x = 1/2 \) satisfies neither case, and \( 1/4 < 1/2 \).
9. **Citing a line that is not available:** the goal itself (circular reasoning), a result proved later, or a general "fact" neither proved nor a true school fact (a false "fact" never qualifies). Breaks @def-derivation: every line is a premise, an assumption, or a rule applied to available lines (Section 1.5). Instances: "if \( n^2 \) is even, then \( n \) is even: suppose \( n^2 \) is even; since \( n \) is even, …" (**true**, and circular); "\( x < 1 \), so \( x^2 < 1 \), since squaring preserves \( < \)" (**false:** \( x = -2 \)).
10. **Using an assumption after its box has closed.** Breaks the scope rule of @def-derivation (Section 1.5). Instance: "Suppose \( n \) is even, say \( n = 2k \); then \( n^2 = 4k^2 \). Hence if \( n \) is even, \( 4 \mid n^2 \). Now \( n^2 = 4k^2 \), so \( 4 \mid n^2 \) for every integer \( n \)." **False:** \( n = 1 \). Proof D below makes the same move with a **true** conclusion.
11. **A wrong negation.** An \( \rulename{RAA} \) box opened with a statement that is not the negation of the goal; a bound negated instead of a quantifier (@prp-bounded-quantifier-negation); the negation of \( \varphi \to \psi \) written as an implication, \( \neg\varphi \to \neg\psi \) or \( \varphi \to \neg\psi \), instead of \( \varphi \wedge \neg\psi \) (@prp-negated-implication). Breaks \( \rulename{RAA} \), which closes only a box opened with \( \neg\varphi \) (Section 2.5), or the laws of Section 4.9. Instances: "if \( x > 2 \), then \( x^2 > 4 \)" is "refuted" because "if \( x \le 2 \), then \( x^2 \le 4 \)" holds at \( x = 0 \) (**false**: both are true at \( x = 0 \), so one is not the negation of the other); "\( a_n = 0 \) does not converge to \( 0 \), since some \( \varepsilon \le 0 \) has \( \abs{a_n - 0} \ge \varepsilon \) for all \( n \)" (**false**).
:::
:::

An entry diagnoses a step, not the conclusion: a **false** instance shows the step leading from true premises to a false conclusion, and a **true** one that a correct conclusion does not excuse it. From Chapter 6 on, a warning about one of these errors cites the entry by number, as in "(N3) of @exm-not-allowed-catalogue". Some entries name errors met before: (N1) is the first error of Section 4.4's list, and two parts of (N11) are warnings of Section 4.9.

::: {.check}
Which entry does the sentence "choose \( N \) larger than every \( N_\varepsilon \), one for each \( \varepsilon > 0 \)" commit, and when is the same move **not** an error?
:::

::: {.solution}
(N2). Each \( N_\varepsilon \) comes from \( \forall \varepsilon \, \exists N \), inside the box of its own \( \varepsilon \); one \( N \) above all of them would be uniform, as if the hypothesis were \( \exists N \, \forall \varepsilon \), and usually none exists, since the \( N_\varepsilon \) can grow without bound as \( \varepsilon \) shrinks. The move is legitimate when \( \varepsilon \) ranges over **finitely many** values \( \varepsilon_1, \dots, \varepsilon_k \): then \( \max\{N_{\varepsilon_1}, \dots, N_{\varepsilon_k}\} \) exists, because a finite set of natural numbers has a maximum.
:::

::: {.warning}
**A true conclusion does not make a proof correct.** "I know the result is true" answers the first column for the last line and nothing else. Argument B of Section 1.1 has a true conclusion and only true sentences, and it is wrong (Proof B below).
:::

## Four proofs, checked

Here are four short proofs as a student might write them; two are correct and two are not.

::: {#exm-verify-cases}
[Proof A]

> **Claim.** For a real number \( x \), if \( x^2 - 3x + 2 < 0 \), then \( 1 < x < 2 \).
>
> (1) Assume \( x^2 - 3x + 2 < 0 \). (2) Then \( (x - 1)(x - 2) < 0 \). (3) A product of two real numbers is negative only when one factor is positive and the other negative, so either \( x - 1 > 0 \) and \( x - 2 < 0 \), or \( x - 1 < 0 \) and \( x - 2 > 0 \). (4) In the first case, \( 1 < x < 2 \). (5) In the second case, \( x < 1 \) and \( x > 2 \), which is impossible. (6) Hence \( 1 < x < 2 \).
:::

::: {.solution}
| Line | True? | Follows? By which rule? |
|---|---|---|
| (1) | assumption | opens the \( \rulename{{\to}I} \) box |
| (2) | yes: \( (x - 1)(x - 2) = x^2 - 3x + 2 \) | \( \rulename{{=}E} \) with the algebraic identity |
| (3) | yes | \( \rulename{{\to}E} \) with the stated fact about signs; a disjunction of two conjunctions |
| (4) | yes, in this case | \( \rulename{\vee E} \), case 1: \( \rulename{\wedge E} \) gives \( x > 1 \) and \( x < 2 \) |
| (5) | the case is impossible | \( \rulename{\vee E} \), case 2: \( x > 2 \) and \( x < 1 \) give \( 2 < 1 \), which clashes with \( \neg(2 < 1) \) (\( \rulename{\neg E} \)); the case reaches \( 1 < x < 2 \) by \( \rulename{\bot E} \) |
| (6) | yes | \( \rulename{\vee E} \) on (3), (4), (5); then \( \rulename{{\to}I} \) on (1)–(6) |

**Verdict: correct.** The disjunction of line (3) is derived from a stated fact, so the cases exhaust and (N8) does not apply. Line (5) is the one to look at twice: "which is impossible" is \( \rulename{\bot E} \), which lets a case that cannot occur reach the goal, so that \( \rulename{\vee E} \) can combine the cases. By @def-silent-steps it could be silent, since the clash is stated.
:::

::: {#exm-verify-converse}
[Proof B]

> **Claim.** For an integer \( n \), if \( n^2 \) is even, then \( n \) is even.
>
> (1) Suppose \( n \) is even. (2) Then \( n = 2k \) for some integer \( k \). (3) So \( n^2 = 4k^2 = 2(2k^2) \). (4) Hence \( n^2 \) is even. (5) Therefore, if \( n^2 \) is even, then \( n \) is even.
:::

::: {.solution}
| Line | True? | Follows? By which rule? |
|---|---|---|
| (1) | assumption | opens a box, with "\( n \) is even" |
| (2) | yes, given (1) | the definition of "even", then \( \rulename{\exists E} \) with a fresh \( k \) |
| (3) | yes | algebra |
| (4) | yes, given (1) | \( \rulename{\exists I} \) with the witness \( 2k^2 \): the definition of "even" |
| (5) | the statement is true, but … | **does not follow**: \( \rulename{{\to}I} \) on the box (1)–(4) gives "if \( n \) is even, then \( n^2 \) is even", not (5) |

**Verdict: wrong; line (5) fails; entry (N5).** Every line is true, and lines (1)–(4) prove the converse. \( \rulename{{\to}I} \) turns a box from \( P \) to \( Q \) into \( P \to Q \), with the box's assumption on the **left**; writing the claim instead is the step from \( P \to Q \) to \( Q \to P \). That step has a refuting row, \( P \) false and \( Q \) true, so no derivation makes it (@cor-refuting-row); and it fails in practice: "if \( x > 1 \), then \( x^2 > 1 \)" is true, its converse false at \( x = -2 \). This is Argument B of Section 1.1, diagnosed in Section 1.5. The claim is true: @thm-square-even-implies-even proves it in a box that opens with "\( n^2 \) is even".
:::

::: {#exm-verify-negation}
[Proof C]

> **Claim.** For an integer \( n \), the number \( n^2 - 2 \) is not divisible by \( 4 \).
>
> (1) Suppose \( n^2 - 2 \) is divisible by \( 4 \), say \( n^2 - 2 = 4k \) with \( k \) an integer. (2) Then \( n^2 = 4k + 2 = 2(2k + 1) \), so \( n^2 \) is even. (3) By @thm-square-even-implies-even, \( n \) is even, say \( n = 2m \) with \( m \) an integer. (4) Then \( n^2 = 4m^2 \), so \( 4m^2 = 4k + 2 \), and hence \( 1 = 2(m^2 - k) \). (5) So \( 1 \) is even. (6) But \( 1 \) is odd, and no integer is both even and odd; this is a contradiction. (7) Hence \( n^2 - 2 \) is not divisible by \( 4 \).
:::

::: {.solution}
| Line | True? | Follows? By which rule? |
|---|---|---|
| (1) | assumption | opens the \( \rulename{\neg I} \) box, with "\( 4 \) divides \( n^2 - 2 \)"; then \( \rulename{\exists E} \) with a fresh \( k \) |
| (2) | yes, given (1) | algebra, then \( \rulename{\exists I} \) with witness \( 2k + 1 \) |
| (3) | yes, given (2) | \( \rulename{{\to}E} \) with @thm-square-even-implies-even and (2); then \( \rulename{\exists E} \) with a fresh \( m \) |
| (4) | yes, given (1) and (3) | algebra: subtract \( 4k \), divide by \( 2 \) |
| (5) | yes, given (4) | \( \rulename{\exists I} \) with witness \( m^2 - k \), an integer |
| (6) | yes | \( \rulename{\wedge I} \) of (5) and "\( 1 \) is odd", then \( \rulename{\neg E} \) against "no integer is both even and odd" |
| (7) | yes | \( \rulename{\neg I} \) on the box (1)–(6) |

**Verdict: correct.** The goal is a negation, and the \( \rulename{\neg I} \) box opens with the positive statement: a proof "by contradiction" of face (i) of Section 5.1, with no \( \rulename{RAA} \). The witness names \( k \) and \( m \) differ, as (N4) requires.
:::

::: {#exm-verify-scope}
[Proof D]

> **Claim.** For a real number \( x \): if \( x > 1 \), then \( x^2 > x \); and \( x^2 + 1 > x \).
>
> (1) Suppose \( x > 1 \). (2) Multiplying both sides by \( x \), which is positive, gives \( x^2 > x \). (3) Hence if \( x > 1 \), then \( x^2 > x \). (4) For the second part, \( x^2 + 1 > x^2 \), and \( x^2 > x \) by (2), so \( x^2 + 1 > x \).
:::

::: {.solution}
| Line | True? | Follows? By which rule? |
|---|---|---|
| (1) | assumption | opens the \( \rulename{{\to}I} \) box for the first conjunct |
| (2) | yes, given (1) | \( \rulename{{\to}E} \) with "multiplying by a positive number keeps \( > \)"; \( x > 0 \) since \( x > 1 > 0 \) |
| (3) | yes | \( \rulename{{\to}I} \) on the box (1)–(2) |
| (4) | "\( x^2 > x \)" is **false** for \( x = 1/2 \) | **does not follow**: it cites (2), which lies inside the box closed at (3) |

**Verdict: wrong; line (4) fails; entry (N10).** The claim is a conjunction, so the skeleton is \( \rulename{\wedge I} \) with two separate proofs. The second cites line (2), derived inside the box that assumed \( x > 1 \) and closed at line (3), so line (2) is not available. The first column confirms it: at \( x = 1/2 \), \( x^2 = 1/4 < 1/2 = x \), a counterexample to the illegal step, though not to the claim.

The claim is true. For every real \( x \),
\[
x^2 - x + 1 = \Bigl( x - \frac12 \Bigr)^2 + \frac34 > 0,
\]
since a square is non-negative; so \( x^2 + 1 > x \), with nothing from the closed box.
:::

In Proofs B and D every sentence sounds right, and in Proof B every sentence is true. The errors are in the connections, which the rules govern: "which rule, from which available lines?" catches both.

## Exercises

### A. Check your understanding

::: {#exr-checking-proofs-a1}
[A1]

Each line below comes from a proof. Name the catalogue entry of @exm-not-allowed-catalogue that it commits, and the rule it breaks.

::: {.enumerate options="label=(\alph*)"}
1. "We checked \( 3^n > n^2 \) for \( n = 0, 1, 2, 3, 4 \), so it holds for every \( n \in \nN \)."
2. "By hypothesis some \( x \in A \) has \( f(x) = 0 \); fix such an \( x \). Since \( x \) was arbitrary, \( f(x) = 0 \) for every \( x \in A \)."
3. "To prove that \( f(x_1) = f(x_2) \) implies \( x_1 = x_2 \), suppose \( x_1 = x_2 \); then \( f(x_1) = f(x_2) \)."
4. "To prove \( x \ge 0 \), suppose, for a contradiction, that \( x \le 0 \)."
5. "If \( n \) is divisible by \( 6 \), then \( n \) is even. Since \( n \) is even, \( n \) is divisible by \( 6 \)."
6. "Every real \( x \) satisfies \( x > 0 \) or \( x < 0 \); we consider the two cases."
:::
:::

::: {.solution}
*(a)* (N1): \( \rulename{\forall I} \) needs one proof about a fresh name, not five instances.

*(b)* (N3): \( x \) was chosen by \( \rulename{\exists E} \) and appears in the open assumption \( f(x) = 0 \), so \( \rulename{\forall I} \) on it breaks the side condition. For \( A = \{0, 1\} \) and \( f(x) = x \) the conclusion fails.

*(c)* (N5): the \( \rulename{{\to}I} \) box opens with the conclusion, so it proves the converse, which every function satisfies.

*(d)* (N11): the negation of \( x \ge 0 \) is \( x < 0 \), not \( x \le 0 \), so \( \rulename{RAA} \) cannot close this box with \( x \ge 0 \). Closed by \( \rulename{\neg I} \) it proves \( x > 0 \), more than the goal, so it closes only if the hypotheses exclude \( x = 0 \).

*(e)* (N6), affirming the consequent. No rule licenses it, so it breaks @def-derivation: \( P \to Q \) with \( Q \) gives no \( P \). Here \( n = 4 \) is even and not divisible by \( 6 \).

*(f)* (N8): the disjunction is not derived, and it is false at \( x = 0 \), so \( \rulename{\vee E} \) has no valid first input.
:::

### B. Practice

::: {#exr-checking-proofs-b1}
[B1: Two proofs in two columns]

Check each proof in two columns. For a wrong proof, name the first line that fails and its catalogue entry, and say whether the claim is true.

::: {.enumerate options="label=(\roman*)"}
1. **Claim.** For integers \( m \) and \( n \), if \( m \) and \( n \) are odd, then \( m + n \) is even. (1) Assume \( m \) and \( n \) are odd. (2) Choose integers \( k \) and \( l \) with \( m = 2k + 1 \) and \( n = 2l + 1 \). (3) Then \( m + n = 2k + 2l + 2 = 2(k + l + 1) \). (4) Since \( k + l + 1 \) is an integer, \( m + n \) is even.
2. **Claim.** For a real number \( x \), if \( x^2 < 1 \), then \( x < 1 \). (1) Assume \( x^2 < 1 \). (2) Suppose, for a contradiction, that \( x > 1 \). (3) Then \( x > 0 \), so \( x^2 = x \cdot x > x > 1 \). (4) This contradicts \( x^2 < 1 \). (5) Hence \( x < 1 \).
:::
:::

::: {.solution}
*(i)*

| Line | True? | Follows? By which rule? |
|---|---|---|
| (1) | assumption | opens the \( \rulename{{\to}I} \) box |
| (2) | yes, given (1) | \( \rulename{\wedge E} \), the definition of "odd", and two \( \rulename{\exists E} \)'s with the **different** fresh names \( k \) and \( l \) |
| (3) | yes | algebra, \( \rulename{{=}E} \) in a chain |
| (4) | yes | \( \rulename{\exists I} \) with the witness \( k + l + 1 \); then the boxes close, and \( \rulename{{\to}I} \) |

**Verdict: correct.** In (2) the second witness has a new name, as (N4) of @exm-not-allowed-catalogue requires.

*(ii)*

| Line | True? | Follows? By which rule? |
|---|---|---|
| (1) | assumption | opens the \( \rulename{{\to}I} \) box |
| (2) | assumption | opens a box with "\( x > 1 \)", announced as \( \rulename{RAA} \) |
| (3) | yes, given (2) | \( \rulename{{\to}E} \) with order facts |
| (4) | yes | (3) gives \( \neg(x^2 < 1) \) by order facts; \( \rulename{\neg E} \) on (1) and that line |
| (5) | true, given (1), but … | **does not follow**: the box assumed \( x > 1 \), which is not the negation of \( x < 1 \); \( \rulename{\neg I} \) on it gives only \( \neg(x > 1) \), that is, \( x \le 1 \) |

**Verdict: wrong; line (5) fails, because the box of line (2) opened with the wrong statement; entry (N11).** The negation of \( x < 1 \) is \( x \ge 1 \), and the case \( x = 1 \) is never examined: \( x = 1 \) has \( \neg(x > 1) \) and not \( x < 1 \), a counterexample to the step. The claim is true. Repair: suppose, for a contradiction, that \( x \ge 1 \); then \( x^2 = x \cdot x \ge x \ge 1 \), which contradicts \( x^2 < 1 \); hence \( x < 1 \).
:::

::: {#exr-checking-proofs-b2}
[B2: Find the error]

Find the error in the following proof, name its catalogue entry, and decide whether the claim is true.

> **Claim.** For all real numbers \( x \) and \( y \), \( \abs{x} + \abs{y} = \abs{x + y} \).
>
> (1) Let \( x \) and \( y \) be real numbers. (2) Either \( x \) and \( y \) are both \( \ge 0 \), or they are both \( < 0 \). (3) If both are \( \ge 0 \), then \( x + y \ge 0 \), so \( \abs{x} + \abs{y} = x + y = \abs{x + y} \). (4) If both are \( < 0 \), then \( x + y < 0 \), so \( \abs{x} + \abs{y} = -x - y = -(x + y) = \abs{x + y} \). (5) In either case \( \abs{x} + \abs{y} = \abs{x + y} \).
:::

::: {.solution}
Line (2) fails. Its disjunction is not derived, and it is false when \( x \) and \( y \) have opposite signs, so line (5) combines cases that do not exhaust: entry (N8) of @exm-not-allowed-catalogue. Lines (3) and (4) are correct in their cases.

The claim is **false**: for \( x = 1 \), \( y = -1 \), \( \abs{x} + \abs{y} = 2 \) and \( \abs{x + y} = 0 \); this pair satisfies neither case of line (2). What is true is \( \abs{x + y} \le \abs{x} + \abs{y} \) (@exm-triangle-inequality-cases).
:::

### C. Going deeper

::: {#exr-checking-proofs-c1}
[C1: The second half]

Let \( f \colon \nR \to \nR \) be continuous at \( a \), as the quantifier pattern of Section 4.8: for every \( \varepsilon > 0 \) there is \( \delta > 0 \) such that \( \abs{f(x) - f(a)} < \varepsilon \) for every real \( x \) with \( \abs{x - a} < \delta \). Suppose \( f(a) > 0 \). Here is a level-1 skeleton for the statement "there is \( \delta > 0 \) such that \( f(x) > 0 \) for every \( x \) with \( \abs{x - a} < \delta \)":

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall \varepsilon > 0 \; \exists \delta > 0 \; \forall x \; (\abs{x - a} < \delta \to \abs{f(x) - f(a)} < \varepsilon)}
  \hypo {2} {f(a) > 0}
  \have {3} {f(a)/2 > 0} \by{arith}{2}
  \have {4} {\exists \delta > 0 \; \forall x \; (\abs{x - a} < \delta \to \abs{f(x) - f(a)} < f(a)/2)} \Ae{1,3}
  \open[\delta_0]
  \hypo {5} {\delta_0 > 0}
  \hypo {6} {\forall x \; (\abs{x - a} < \delta_0 \to \abs{f(x) - f(a)} < f(a)/2)}
  \open[x_0]
  \open
  \hypo {7} {\abs{x_0 - a} < \delta_0}
  \have {8} {\abs{x_0 - a} < \delta_0 \to \abs{f(x_0) - f(a)} < f(a)/2} \Ae{6}
  \have {9} {\abs{f(x_0) - f(a)} < f(a)/2} \ie{8,7}
  \have {10} {f(x_0) > 0} \by{arith}{2,9}
  \close
  \have {11} {\abs{x_0 - a} < \delta_0 \to f(x_0) > 0} \ii{7-10}
  \close
  \have {12} {\forall x \; (\abs{x - a} < \delta_0 \to f(x) > 0)} \Ai{7-11}
  \have {13} {\exists \delta > 0 \; \forall x \; (\abs{x - a} < \delta \to f(x) > 0)} \Ei{5,12}
  \close
  \have {14} {\exists \delta > 0 \; \forall x \; (\abs{x - a} < \delta \to f(x) > 0)} \Ee{4,5-13}
\end{nd}$
\end{center}
```

Its level-3 prose begins:

> Since \( f(a) > 0 \), the number \( f(a)/2 \) is positive. By the continuity of \( f \) at \( a \), applied with \( \varepsilon = f(a)/2 \), choose \( \delta > 0 \) such that \( \abs{f(x) - f(a)} < f(a)/2 \) for every real \( x \) with \( \abs{x - a} < \delta \).

The rest is blank. *Name the move, then complete it.* Say which skeleton lines your sentences carry, and what \( \delta \) depends on.
:::

::: {.solution}
[Hint 1]

What is left is the box of \( x_0 \) and the witness.
:::

::: {.solution}
[Hint 2]

"Let \( x \) be a real number with \( \abs{x - a} < \delta \). Then …"
:::

::: {.solution}
*The move:* skeleton first: the goal fixes the \( \rulename{\exists I} \) of line 13 and the box of \( x_0 \). Filling it: \( \rulename{\forall E} \) at the non-obvious instance \( \varepsilon = f(a)/2 \) (line 4), \( \rulename{\exists E} \) on its \( \delta \) (line 5), and that \( \delta \) as the witness.

*Completion.*

> Let \( x \) be a real number with \( \abs{x - a} < \delta \). Then \( \abs{f(x) - f(a)} < f(a)/2 \), so, as \( -\abs{u} \le u \), \( f(x) - f(a) > -f(a)/2 \), that is, \( f(x) > f(a)/2 > 0 \). So this \( \delta \), which depends only on \( a \), is as required.

"Let \( x \) … with \( \abs{x - a} < \delta \)" opens the two boxes at line 7; "then \( \abs{f(x) - f(a)} < f(a)/2 \)" is lines 8–9, the \( \rulename{\forall E} \) at the obvious term \( x \) silent; "so … \( f(x) > f(a)/2 > 0 \)" is line 10, which uses line 2. Lines 11 and 12 are silent closings, and the last sentence is lines 13–14, with the \( \delta \) already chosen as witness. It depends on \( a \) (through \( f(a) \) and the continuity at \( a \)) and on no \( x \): the box of \( \delta_0 \) encloses the box of \( x_0 \).

**Marking scheme.** (10 points)
- 2: names the move (skeleton first; a hypothesis applied at a chosen \( \varepsilon \), then its \( \delta \) reused as the witness), or the rules \( \rulename{\forall E} \), \( \rulename{\exists E} \), \( \rulename{\exists I} \).
- 3: for an arbitrary \( x \) with \( \abs{x - a} < \delta \), derives \( f(x) > f(a)/2 \), with the step from \( \abs{u} < r \) to \( u > -r \) justified.
- 2: concludes \( f(x) > 0 \) using \( f(a) > 0 \), and states the conclusion with \( \delta \) before \( x \).
- 2: matches the sentences to the skeleton's lines.
- 1: says \( \delta \) depends on \( a \) and not on \( x \).
Second route: refuting \( f(x) \le 0 \) by \( \abs{f(x) - f(a)} \ge f(a) - f(x) \ge f(a) > f(a)/2 \) earns the second line and the \( f(x) > 0 \) part of the third.
Fatal errors (0 for the step): choosing \( \delta \) after \( x \); applying continuity at an \( \varepsilon \) not shown to be positive.
:::

::: {#exr-checking-proofs-c2}
[C2: A true conclusion]

Here is a proof that \( \sqrt 2 + \sqrt 3 \) is irrational, a true conclusion. Find the line that fails and its catalogue entry, give a counterexample to the illegal step, and write a correct proof.

> (1) Suppose \( \sqrt 2 + \sqrt 3 = r \) for some rational number \( r \). (2) Squaring, \( r^2 = 2 + 2\sqrt 6 + 3 = 5 + 2\sqrt 6 \). (3) Hence \( \sqrt 6 = (r^2 - 5)/2 \), which is rational, since \( r \) is. (4) But \( \sqrt 6 = \sqrt 2 \cdot \sqrt 3 \) is irrational, being a product of two irrational numbers. (5) This contradiction shows that \( \sqrt 2 + \sqrt 3 \) is irrational.
:::

::: {.solution}
[Hint 1]

Run the second column on every line.
:::

::: {.solution}
[Hint 2]

For a correct proof, isolate \( \sqrt 3 = r - \sqrt 2 \) before squaring.
:::

::: {.solution}
*The failing line is (4).* Its first half is true, \( \sqrt 6 = \sqrt 2 \cdot \sqrt 3 \), but its reason is not available. "A product of two irrational numbers is irrational" is neither proved nor a school fact: it is false, since \( \sqrt 2 \) is irrational (@thm-sqrt2-irrational), and \( \sqrt 2 \cdot \sqrt 2 = 2 \) is rational. So the line cites nothing: entry (N9) of @exm-not-allowed-catalogue. The product \( \sqrt 2 \cdot \sqrt 2 = 2 \) is a counterexample to the illegal step; there is none to the conclusion, which is true. Lines (1)–(3) and (5), and the \( \rulename{\neg I} \) skeleton, are correct.

*A correct proof.* Suppose \( \sqrt 2 + \sqrt 3 = r \) with \( r \) rational. Then \( r > 0 \), since both square roots are positive. Isolating, \( \sqrt 3 = r - \sqrt 2 \), and squaring,
\[
3 = r^2 - 2r\sqrt 2 + 2, \qquad\text{so}\qquad \sqrt 2 = \frac{r^2 - 1}{2r},
\]
where dividing by \( 2r \) is legitimate because \( r > 0 \). The right-hand side is rational, which contradicts @thm-sqrt2-irrational. Hence \( \sqrt 2 + \sqrt 3 \) is irrational.

**Marking scheme.** (10 points)
- 3: names line (4) as the failing line, and the illegal step as the unproved general "fact", entry (N9).
- 2: a counterexample to that step (\( \sqrt 2 \cdot \sqrt 2 = 2 \), or another product of two irrationals that is rational).
- 1: says the conclusion is true, so no counterexample to it exists.
- 4: a correct proof: the \( \rulename{\neg I} \) box on "\( r \) rational", the algebra, the division justified by \( r \ne 0 \), and the clash with @thm-sqrt2-irrational (or with \( \sqrt 3 \) or \( \sqrt 6 \), its irrationality proved).
Fatal errors (0 for the step): "correcting" line (4) by another unproved fact; dividing by \( r \) without \( r \ne 0 \).
:::

::: {#exr-checking-proofs-c3}
[C3: Exit check: four student proofs]

Judge each proof. If it is wrong, give the line that fails, its entry in @exm-not-allowed-catalogue, and a counterexample to the illegal step. If it is correct, name the rule of its most delicate step and check that step.

::: {.enumerate options="label=(\arabic*)"}
1. **Claim.** For every integer \( n \), if \( n \) is a multiple of \( 4 \) or a multiple of \( 6 \), then \( n \) is even. (1) Let \( n \) be an integer that is a multiple of \( 4 \) or of \( 6 \). (2) Case 1: \( n \) is a multiple of \( 4 \). Choose an integer \( k \) with \( n = 4k \); then \( n = 2(2k) \), so \( n \) is even. (3) Case 2: \( n \) is a multiple of \( 6 \). Choose an integer \( k \) with \( n = 6k \); then \( n = 2(3k) \), so \( n \) is even. (4) In either case, \( n \) is even.
2. **Claim.** For integers \( m \) and \( n \), if \( m \) and \( n \) are even, then \( mn \) is divisible by \( 4 \). (1) Assume \( m \) and \( n \) are even. (2) Then \( m = 2k \) and \( n = 2k \) for an integer \( k \). (3) So \( mn = 4k^2 \), which is divisible by \( 4 \).
3. **Claim.** For every real \( x \), \( \abs{x - 1} \le \abs{x} + 1 \). (1) Either \( x \ge 1 \) or \( x \le 0 \). (2) If \( x \ge 1 \), then \( \abs{x - 1} = x - 1 \le x + 1 = \abs{x} + 1 \). (3) If \( x \le 0 \), then \( \abs{x - 1} = 1 - x = 1 + \abs{x} \). (4) In either case, \( \abs{x - 1} \le \abs{x} + 1 \).
4. **Claim.** For every real \( x \), if \( x^2 = 2x \), then \( x = 2 \). (1) Assume \( x^2 = 2x \). (2) Canceling \( x \) from both sides, \( x = 2 \). (3) Hence if \( x^2 = 2x \), then \( x = 2 \).
:::
:::

::: {.solution}
[Hint 1]

Run the two-column check on every line, and keep the two questions apart: a true claim can have a wrong proof.
:::

::: {.solution}
[Hint 2]

In (1), ask which boxes are open when the second \( k \) is chosen. In (3), ask what \( \rulename{\vee E} \) needs from line (1).
:::

::: {.solution}
*(1)* **Correct.** The skeleton is \( \rulename{\forall I} \) and \( \rulename{{\to}I} \), then \( \rulename{\vee E} \) on the hypothesis itself, so the cases exhaust. The delicate step is the second "choose an integer \( k \)", an \( \rulename{\exists E} \) reusing a name. It is legal: the first box of \( k \) lies inside Case 1, which closed before Case 2 opened, so \( k \) appears in no open assumption, not in the existential and not in the conclusion. Sibling boxes may share a name (Section 4.6); (N4) forbids only a name still in use.

*(2)* **Wrong; line (2) fails; entry (N4) of @exm-not-allowed-catalogue.** The second witness is named \( k \) while the box of \( m = 2k \) is open. Counterexample to the step: \( m = 2 \), \( n = 4 \); no integer \( k \) has \( 2 = 2k \) and \( 4 = 2k \). The conclusion is true: with \( m = 2k \) and \( n = 2l \), \( mn = 4kl \).

*(3)* **Wrong; line (1) fails; entry (N8).** "Either \( x \ge 1 \) or \( x \le 0 \)" is not derived, and is false at \( x = 1/2 \), a counterexample to the step. The conclusion is true; the missing case repairs the proof: if \( 0 < x < 1 \), then \( \abs{x - 1} = 1 - x < 1 < \abs{x} + 1 \).

*(4)* **Wrong; line (2) fails; entry (N9); the claim is false.** Canceling uses the "fact" "if \( ax = bx \), then \( a = b \)", which is neither proved nor a school fact, and is false: \( a = 1 \), \( b = 2 \), \( x = 0 \). It needs \( x \ne 0 \), which no line provides. The claim fails at \( x = 0 \); what is true is "\( x = 0 \) or \( x = 2 \)", from \( x(x - 2) = 0 \).

**Marking scheme.** (10 points: 2.5 per proof)
- For each of (2), (3), (4): the verdict "wrong" (1); the failing line and its entry, (N4), (N8), (N9) (1); a counterexample to the illegal step (0.5).
- For (1): the verdict "correct" (1); the delicate step named as an \( \rulename{\exists E} \) reusing a name in a sibling box (or as the \( \rulename{\vee E} \) on the hypothesis) (1); that step checked against the side condition (0.5).
For (4), "\( \rulename{{\to}E} \) without its antecedent \( x \ne 0 \)" is also accepted. Fatal errors (0 for that proof): calling proof (1) wrong as an instance of (N4) because the name \( k \) recurs; judging (2) or (3) correct because its conclusion is true.
:::

<!-- dependency ledger
exm-not-allowed-catalogue (claim): (the section's opening, "Two questions") rules never lead from true lines to a false one | thm-soundness (cited); Section 4.11's statement (from-counter-models-to-non-derivability; its proof in Section 4.12, optional)
exm-not-allowed-catalogue (claim): (the Quick check after "Two questions") for integers n(n - 1) >= 0 since no integer lies strictly between 0 and 1; at n = 1/2 the product is -1/4 | school arithmetic of Z (ch07 promised in STATUS: "nothing between n and n + 1"); checked by verify/ch05/exm-not-allowed-catalogue.py
exm-not-allowed-catalogue (example): (N1) n^2 - n + 11 prime for n = 0..10 with the listed values, 121 = 11^2 at n = 11 | arithmetic; checked by verify/ch05/exm-not-allowed-catalogue.py
exm-not-allowed-catalogue (example): (N2) x^2 not uniformly continuous on R | exm-square-not-uniform (cited)
exm-not-allowed-catalogue (example): (N3)-(N11) instances: A = {-1, 1}; m = 2, n = 4; x = -2 (x^2 = 4 > 1, x < 1; x < 1 and x^2 = 4); 6 even, not a multiple of 4; |0| = 0; x = 1/2, x^2 = 1/4; n = 1; x = 0 for x > 2 -> x^2 > 4 and x <= 2 -> x^2 <= 4; |a_n - 0| >= eps for eps <= 0 | arithmetic and school order facts; checked by verify/ch05/exm-not-allowed-catalogue.py
exm-not-allowed-catalogue (example): (N4) sibling boxes may share a witness name | Section 4.6 (the remark on two exists-E boxes in the cases of or-E, after exm-existential-elimination-derivations; unlabeled), def-rules-existential (cited)
exm-not-allowed-catalogue (example): (N6) the denying-the-antecedent pattern P -> Q, not P |- not Q has a refuting row (P false, Q true) | inline (one row, by def-truth-value); cor-refuting-row (cited); exm-affirming-the-consequent (cited) covers affirming
exm-not-allowed-catalogue (claim): Argument B of Section 1.1; Section 4.4's list of forall-I errors; the warnings of Section 4.9 | prose pointers to earlier sections (unlabeled passages)
exm-not-allowed-catalogue (solution): (the Quick check on N2) a finite set of natural numbers has a maximum | ch07 (promised; STATUS row "every non-empty finite set has a maximum")
exm-verify-cases (solution): (x - 1)(x - 2) = x^2 - 3x + 2; a product of two reals is negative only if the factors have opposite signs; x > 2, x < 1 give 2 < 1, not(2 < 1) | school algebra; checked by verify/ch05/exm-verify-cases.py
exm-verify-converse (solution): n = 2k gives n^2 = 2(2k^2); the row P false, Q true refutes P -> Q |- Q -> P; x = -2 for the converse of x > 1 -> x^2 > 1 | inline row (def-truth-value); cor-refuting-row (cited); checked by verify/ch05/exm-verify-converse.py
exm-verify-negation (solution): 1 is odd; no integer is both even and odd; m^2 - k is an integer; 2 != 0 | school arithmetic (ch07 promised in STATUS: even or odd, not both); checked by verify/ch05/exm-verify-negation.py
exm-verify-scope (solution): multiplying by a positive number keeps >; x^2 - x + 1 = (x - 1/2)^2 + 3/4 > 0; at x = 1/2, x^2 < x | school algebra; checked by verify/ch05/exm-verify-scope.py
exr-checking-proofs-a1 (solution): 3^n > n^2 for n = 0..4; A = {0, 1}, f(x) = x; n = 4 even, not divisible by 6; not(x >= 0) iff x < 0; P -> Q with Q gives no P | arithmetic; trichotomy; def-derivation (cited); checked by verify/ch05/exr-checking-proofs-a1.py
exr-checking-proofs-b1 (solution): (2k + 1) + (2l + 1) = 2(k + l + 1); x > 1 gives x^2 > x; x^2 > 1 gives not(x^2 < 1); x >= 1 gives x^2 >= x >= 1; x = 1; not(x < 1) iff x >= 1 | school algebra; trichotomy; checked by verify/ch05/exr-checking-proofs-b1.py
exr-checking-proofs-b2 (solution): x = 1, y = -1 gives |x| + |y| = 2, |x + y| = 0; lines (3), (4) correct in their cases | arithmetic, school algebra of absolute value; exm-triangle-inequality-cases (cited) for the inequality; checked by verify/ch05/exr-checking-proofs-b2.py
exr-checking-proofs-c1 (solution): -|u| <= u; |u| < r gives u > -r; f(a) - f(a)/2 = f(a)/2 > 0; f(x) <= 0 gives |f(x) - f(a)| >= f(a) > f(a)/2 | school algebra of absolute value; checked by verify/ch05/exr-checking-proofs-c1.py
exr-checking-proofs-c1 (example): continuity at a used only as a quantifier pattern | exm-translate-limit (c) (Section 4.8)
exr-checking-proofs-c2 (solution): (sqrt2 + sqrt3)^2 = 5 + 2 sqrt6; sqrt6 = sqrt2 sqrt3; sqrt2 sqrt2 = 2; 3 = r^2 - 2r sqrt2 + 2 gives sqrt2 = (r^2 - 1)/(2r); r > 0; rationals closed under +, -, x, / by non-zero | school algebra of square roots (a school fact before thm-nth-root, per NOTATION) and of Q; thm-sqrt2-irrational (cited); checked by verify/ch05/exr-checking-proofs-c2.py
exr-checking-proofs-c3 (solution): n = 4k = 2(2k), n = 6k = 2(3k); m = 2k, n = 2l give mn = 4kl; x = 1/2 for (3) and the case 0 < x < 1; x = 0 for (4); x(x - 2) = 0 | school algebra; trichotomy; Section 4.6 (sibling boxes); checked by verify/ch05/exr-checking-proofs-c3.py
-->
