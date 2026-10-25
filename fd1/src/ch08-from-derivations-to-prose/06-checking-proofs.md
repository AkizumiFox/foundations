# Checking Proofs, and What Is Not Allowed

A reader working alone must judge proofs, including their own, and is the person least able to do it. The remedy is procedural. This section gives two questions to ask of every line and a catalogue of the errors that recur, each tied to the rule of Chapters 1–7 that it breaks, and then checks four short proofs line by line.

## Two questions for every line

A proof is correct when every line is licensed: by @def-derivation, each line is a premise (a hypothesis, a proved result or a true school fact), an assumption, or one rule applied to available lines. So checking a proof means asking two questions of every line, with the answers in two columns.

- **Is it true?** Is the line correct whenever the hypotheses and the assumptions of the open boxes are true?
- **Does it follow, and by which rule?** From which available lines, and by which rule?

*The first column finds where to look; the second decides.*

The two questions are different. A line can be **true and not follow**: a correct fact the proof has not earned. This is the dangerous case, because nothing about the line looks wrong.

| | It follows | It does not follow |
|---|---|---|
| **It is true** | the normal case: "\( n = 2k \), so \( n^2 = 2(2k^2) \)", in a proof that \( n^2 \) is even when \( n \) is | the dangerous case: Proof B's last line, "if \( n^2 \) is even, then \( n \) is even", true and not earned |
| **It is false** | the fault is higher up: from the false line "every real \( x \) has \( x \ge 1 \) or \( x \le 0 \)", \( \rulename{\forall E} \) at \( \tfrac12 \) gives "\( \tfrac12 \ge 1 \) or \( \tfrac12 \le 0 \)", which follows and is false | "\( x < 1 \), so \( x^2 < 1 \)": false at \( x = -2 \) |

"False" means false in some situation where the hypotheses and the open assumptions are true. When a line follows and is false, some line it rests on, neither a hypothesis nor an open assumption, is false there too, because the rules never lead from true lines to a false one (@thm-soundness); follow it back until the second column fails.

The two columns, as a procedure for one line:

```{=latex}
\begin{center}
\begin{tikzpicture}[flowchart]
  \node[fc start] (s) {the next line of the proof};
  \node[fc step, below=of s] (q) {first column: is it true wherever\\the hypotheses and the open\\assumptions are true?};
  \node[fc test, below=of q] (t) {second column: which rule, or\\which chain of rules and silent\\steps, from which available lines?};
  \node[fc start, right=of t] (f) {no such chain: the proof fails\\here; name its entry, (N1)--(N14)};
  \node[fc start, below=of t] (n) {the line is licensed at its level;\\go on to the next one};
  \draw[fc arrow] (s) -- (q);
  \draw[fc arrow] (q) -- (t);
  \draw[fc arrow] (t) -- node[above, font=\scriptsize] {none} (f);
  \draw[fc arrow] (t) -- node[right, font=\scriptsize] {found} (n);
\end{tikzpicture}
\end{center}
```

A "no" in the first column marks a line to look at first; only the second column decides. The silent steps are those of @def-silent-steps.

::: {.second-reading title="Two notes on the two columns"}
The same holds for derivations with quantifiers and equality, by the soundness statement for predicate logic in Section 7.2 ("From counter-models to non-derivability").

(Proof C's "\( 1 \) is even" is true given its box's assumption.)
:::

::: {.check}
A proof that \( n^2 \ge n \) for every integer \( n \) opens with the line "\( n^2 - n = n(n - 1) \ge 0 \)". Is the line true? Does it follow? Would the answers change if \( n \) ranged over the reals?
:::

::: {.solution}
For an integer \( n \) the line is true: no integer lies strictly between \( 0 \) and \( 1 \), so \( n \le 0 \) (both factors \( \le 0 \)) or \( n \ge 1 \) (both \( \ge 0 \)). But as written it follows from nothing: it is the goal rearranged, without the case split that makes it true. For real \( n \) it is false at \( n = 1/2 \), where \( n(n - 1) = -1/4 \). The first column depends on the situation; the second fails in both.
:::

## The catalogue

Most wrong proofs fail in one of a few ways, each breaking a particular rule. The entries fall into seven families.

| Family | Entries | Slogan |
|---|---|---|
| "For all" errors | (N1), (N2), (N3) | A "for all" needs one argument about a name that is new and arbitrary. |
| Naming errors | (N4), (N12) | A new choice gets a new name, and two names may name one thing. |
| Implication errors | (N5), (N6) | The box of \( P \to Q \) opens with \( P \); \( Q \) alone gives no \( P \). |
| Case errors | (N7), (N8) | Every case, from a disjunction that covers everything. |
| Scope and citation errors | (N9), (N10) | Cite only what is proved, given, or open around you. |
| Negation errors | (N11) | Negate exactly: an \( \rulename{RAA} \) box opens with the negation of the goal; negate the quantifier, not the bound; \( \varphi \wedge \neg\psi \), not an implication. |
| Iteration and existence errors | (N13), (N14) | An "and so on" needs its step; a "the" needs its object. |

::: {#exm-not-allowed-catalogue}
[What is not allowed]

Each entry names the error, the rule it breaks and where that rule lives, and a failing instance whose conclusion is marked **true** or **false**: a wrong argument can reach either.

::: {.enumerate options="label=(N\arabic*)"}
1. **Verifying instances and concluding "for all".** Breaks \( \rulename{\forall I} \), which needs one proof about a fresh name (@def-rules-universal, Section 5.4). Instance: \( n^2 - n + 11 \) is prime for \( n = 0, 1, \dots, 10 \) (the values are \( 11, 11, 13, 17, 23, 31, 41, 53, 67, 83, 101 \)), "so it is prime for every \( n \in \nN \)". **False:** at \( n = 11 \) the value is \( 121 = 11^2 \).
2. **A witness that depends on a variable introduced later, while uniformity is claimed.** Breaks the side conditions of \( \rulename{\exists E} \) and \( \rulename{\forall I} \): a witness \( \delta_0 \) obtained inside the box of \( x_0 \) may not leave it (Section 6.4, @exm-converse-fails). Instance: "\( x^2 \) is continuous at every \( x \), with \( \delta = \min\{1, \varepsilon/(2\abs{x} + 1)\} \); so one \( \delta \) for each \( \varepsilon \) serves every \( x \), and \( x^2 \) is uniformly continuous on \( \nR \)". **False** (@exm-square-not-uniform).
3. **Treating the name from \( \rulename{\exists E} \) as arbitrary.** Breaks the side condition of \( \rulename{\forall I} \): the witness appears in the open assumption of its box (@def-rules-existential, Section 5.6). Instance: "Some element of \( A \) is positive; let \( x \) be such an element. Since \( x \) was arbitrary, every element of \( A \) is positive." **False** for \( A = \{-1, 1\} \).
4. **Reusing one witness name for two \( \rulename{\exists E} \)'s.** Breaks the fresh-name condition: the second name may not appear in an open assumption, and the first box's assumption mentions it (Section 5.6, @exm-sum-of-evens). Sibling boxes may share a name. Instance: "\( m \) and \( n \) are even, so \( m = 2k \) and \( n = 2k \) for an integer \( k \); hence \( m = n \)". **False:** \( m = 2 \), \( n = 4 \).
5. **Proving the converse.** Breaks \( \rulename{{\to}I} \), whose box opens with the hypothesis, not the conclusion (@def-rules-implication, Section 1.4). Instance: "If \( x^2 > 1 \), then \( x > 1 \): suppose \( x > 1 \); then \( x^2 > x > 1 \)." **False:** \( x = -2 \). Argument B of Section 1.1 makes the same move with a **true** conclusion.
6. **Affirming the consequent; denying the antecedent.** Breaks @def-derivation (Section 1.4), being no rule: \( P \to Q \) with \( Q \) gives no \( P \), and with \( \neg P \) gives no \( \neg Q \). Each pattern has a refuting row, so no derivation exists (@cor-refuting-row, Section 4.7): @exm-affirming-the-consequent, and for denying the row \( P \) false, \( Q \) true. Instances: "a multiple of \( 4 \) is even and \( 6 \) is even, so \( 6 \) is a multiple of \( 4 \)"; "… and \( 6 \) is not a multiple of \( 4 \), so \( 6 \) is not even". Both **false**.
7. **A missing case.** Breaks \( \rulename{\vee E} \), which needs one box for each disjunct (@def-rules-disjunction, Section 1.6). Instance: "\( \abs{x} > 0 \) for every real \( x \): every real \( x \) has \( x > 0 \), \( x = 0 \) or \( x < 0 \); if \( x > 0 \), \( \abs{x} = x > 0 \); if \( x < 0 \), \( \abs{x} = -x > 0 \)". **False:** the case \( x = 0 \) was dropped, and \( \abs{0} = 0 \).
8. **Cases that do not exhaust.** Breaks \( \rulename{\vee E} \), whose first input must be a disjunction already derived (Section 1.6). Instance: "\( x^2 \ge x \) for every real \( x \): either \( x \ge 1 \) or \( x \le 0 \); in the first case \( x^2 = x \cdot x \ge x \), in the second \( x^2 \ge 0 \ge x \)". **False:** \( x = 1/2 \) satisfies neither case, and \( 1/4 < 1/2 \).
9. **Citing a line that is not available:** the goal itself (circular reasoning), a result proved later, or a general "fact" neither proved nor a true school fact (a false "fact" never qualifies). Breaks @def-derivation: every line is a premise, an assumption, or a rule applied to available lines (Section 1.4). Instances: "if \( n^2 \) is even, then \( n \) is even: suppose \( n^2 \) is even; since \( n \) is even, …" (**true**, and circular); "\( x < 1 \), so \( x^2 < 1 \), since squaring preserves \( < \)" (**false:** \( x = -2 \)).
10. **Using an assumption after its box has closed.** Breaks the scope rule of @def-derivation (Section 1.4). Instance: "Suppose \( n \) is even, say \( n = 2k \); then \( n^2 = 4k^2 \). Hence if \( n \) is even, \( 4 \mid n^2 \). Now \( n^2 = 4k^2 \), so \( 4 \mid n^2 \) for every integer \( n \)." **False:** \( n = 1 \). Proof D below makes the same move with a **true** conclusion.
11. **A wrong negation**, in three forms. Each breaks \( \rulename{RAA} \), which closes only a box opened with \( \neg\varphi \) (Section 2.5), or the laws of Section 6.2.
    - (a) An \( \rulename{RAA} \) box opened with a statement that is not the negation of the goal. Instance: "if \( x^2 > 9 \) and \( x > 0 \), then \( x > 3 \): suppose, for a contradiction, that \( x < 3 \); then \( 0 < x < 3 \) gives \( x^2 < 9 \), against \( x^2 > 9 \); hence \( x > 3 \)" (**true**: the box should open with \( x \le 3 \), and the case \( x = 3 \) is never examined).
    - (b) A bound negated instead of a quantifier (@prp-bounded-quantifier-negation). Instance: "\( a_n = 0 \) does not converge to \( 0 \), since some \( \varepsilon \le 0 \) has \( \abs{a_n - 0} \ge \varepsilon \) for all \( n \)" (**false**).
    - (c) The negation of \( \varphi \to \psi \) written as an implication, \( \neg\varphi \to \neg\psi \) or \( \varphi \to \neg\psi \), instead of \( \varphi \wedge \neg\psi \) (@prp-negated-implication). Instance: "if \( x > 2 \), then \( x^2 > 4 \)" is "refuted" because "if \( x \le 2 \), then \( x^2 \le 4 \)" holds at \( x = 0 \) (**false**: both are true at \( x = 0 \), so one is not the negation of the other).
12. **Distinct letters taken for distinct objects.** Two names introduced separately are treated as naming different objects, though no line says they differ. Breaks \( \rulename{\forall I} \): a box opened for two arbitrary names must cover every pair, including the pairs in which both name one object (\( \rulename{\forall E} \) may put the same term for both, @def-rule-universal-elimination). Instance: "if \( a \) and \( b \) are roots of \( x^2 - 5x + 6 = 0 \), then \( a + b = 5 \): the two roots give \( x^2 - 5x + 6 = (x - a)(x - b) \), and comparing coefficients, \( a + b = 5 \)". **False:** \( a = b = 2 \) are roots, and \( 2 + 2 = 4 \).
13. **An "and so on" with nothing behind it.** A step is repeated "and so on", and its outcome is used for every stage, but the passage from each stage to the next, or the reason the process ends, is never proved. Breaks @ax-induction (or @thm-strong-induction): \( \rulename{{\to}E} \) on the axiom needs its step as a line, and "and so on" is not that line. Instance: "a non-empty set \( A \) of positive rational numbers has a least element: take \( a_1 \in A \); if it is not least, take \( a_2 \in A \) with \( a_2 < a_1 \), and so on, until the least element is reached" (**false:** \( \{ 1/n : n \in \nZ_{>0} \} \) has no least element, and the process never ends).
14. **An object named before it is shown to exist.** A step names an object, with "the …" or "let … be the …", and so presupposes that such an object exists (for "the", exactly one), though no line states or proves it. In (N9) the step asserts a fact that is not available; here the missing premise is never asserted at all, because it hides inside a name. Breaks \( \rulename{\exists E} \), which opens its box only by citing a line \( \exists x \, \varphi \) (@def-rules-existential), and the use of "the" (Section 5.8), which needs existence and uniqueness. Instance: "let \( N \) be the largest natural number; then \( N + 1 \le N \), so \( 1 \le 0 \)" (**false:** the presupposed premise, that a largest natural number exists, is false).
:::
:::

::: {.second-reading title="True conclusions behind an 'and so on' and a 'the'"}
Both new kinds of error can reach a true conclusion. The words of (N13)'s instance, said of a non-empty set of natural numbers, reach a true conclusion, but they leave out why the process ends: a strictly decreasing list of natural numbers that starts at \( a_1 \) has at most \( a_1 + 1 \) terms, which needs an induction. "Let \( m \) be the least positive integer with \( m^2 > 50 \); since \( 7^2 = 49 \) and \( 8^2 = 64 \), \( m = 8 \)" reaches a true conclusion too, but the existence of a least such integer is a premise the proof must state: it is (N14). The barber who shaves exactly the villagers who do not shave themselves is (N14) as well; Section 5.6 shows that no such barber can exist (@thm-barber).
:::

An entry diagnoses a step, not the conclusion: a **false** instance shows the step leading from true premises to a false conclusion, and a **true** one that a correct conclusion does not excuse it. Some entries name errors met before: (N1) is the first error of Section 5.4's list, and parts (b) and (c) of (N11) are warnings of Section 6.2.

The catalogue lists steps that can lead from true lines to a false one. A step can also be **valid but improper**. "For all reals \( a \) and \( b \), \( a^2 + b^2 \ge 2ab \); so for all reals \( b \) and \( a \), \( a^2 + b^2 \ge 2ab \)", taken as one line, never leads from truth to falsehood, but no rule of the book writes it in one line, TAUT included (Section 8.3). That is a matter of level (@def-levels-of-proof), not an error: at level 0 it is \( \rulename{\forall E} \) twice and \( \rulename{\forall I} \) twice, and in prose it needs no words.

::: {.second-reading title="The errors under their traditional names"}
Older books name some of these errors as fallacies:

| Traditional name | Entry |
|---|---|
| hasty generalization | (N1) |
| equivocation: one name for two things | (N4) |
| affirming the consequent; denying the antecedent | (N6) |
| false dichotomy | (N8) |
| begging the question | (N9) |
| a presupposition ("the …") | (N14) |

Affirming a disjunct is a common error of Section 1.6.
:::

::: {.check}
Which family, and which entry, does this belong to: "Some integer \( n \) has \( n^2 = n + 6 \); fix such an \( n \). Since \( n \) was arbitrary, every integer \( n \) satisfies \( n^2 = n + 6 \)"?
:::

::: {.solution}
A "for all" error, (N3): a name chosen by \( \rulename{\exists E} \) is not arbitrary. The premise holds at \( n = 3 \); the conclusion fails at \( n = 0 \).
:::

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

**Verdict: wrong; line (5) fails; entry (N5).** Every line is true, and lines (1)–(4) prove the converse. \( \rulename{{\to}I} \) turns a box from \( P \) to \( Q \) into \( P \to Q \), with the box's assumption on the **left**; writing the claim instead is the step from \( P \to Q \) to \( Q \to P \). That step has a refuting row, \( P \) false and \( Q \) true, so no derivation makes it (@cor-refuting-row); and it fails in practice: "if \( x > 1 \), then \( x^2 > 1 \)" is true, its converse false at \( x = -2 \). This is Argument B of Section 1.1, diagnosed in Section 1.4. The claim is true: @thm-square-even-implies-even proves it in a box that opens with "\( n^2 \) is even".
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

**Verdict: correct.** The goal is a negation, and the \( \rulename{\neg I} \) box opens with the positive statement: a proof "by contradiction" of face (i) of Section 8.1, with no \( \rulename{RAA} \). The witness names \( k \) and \( m \) differ, as (N4) requires.
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

::: {.remark}
[Looking ahead]

From *Sets, Relations, and Cardinality*, Chapter 1 on, a warning about one of these errors cites its entry by number, as in "(N3) of the catalogue".
:::

## Exercises

### A. Check your understanding

::: {#exr-checking-proofs-a1}
[A1]

Each line below comes from a proof. Name the catalogue entry of @exm-not-allowed-catalogue that it commits, and the rule it breaks.

::: {.enumerate options="label=(\alph*)"}
1. "We checked \( 3^n > n^2 \) for \( n = 0, 1, 2, 3, 4 \), so it holds for every \( n \in \nN \)."
2. "By hypothesis some \( x \in A \) has \( f(x) = 0 \); fix such an \( x \). Since \( x \) was arbitrary, \( f(x) = 0 \) for every \( x \in A \)."
3. "To prove that \( f(x_1) = f(x_2) \) implies \( x_1 = x_2 \), suppose \( x_1 = x_2 \); then \( f(x_1) = f(x_2) \)."
4. "To prove \( x > 0 \), suppose, for a contradiction, that \( x < 0 \)."
5. "If \( n \) is divisible by \( 6 \), then \( n \) is even. Since \( n \) is even, \( n \) is divisible by \( 6 \)."
6. "Every real \( x \) satisfies \( x > 0 \) or \( x < 0 \); we consider the two cases."
:::
:::

::: {.solution}
*(a)* (N1): \( \rulename{\forall I} \) needs one proof about a fresh name, not five instances.

*(b)* (N3): \( x \) was chosen by \( \rulename{\exists E} \) and appears in the open assumption \( f(x) = 0 \), so \( \rulename{\forall I} \) on it breaks the side condition. For \( A = \{0, 1\} \) and \( f(x) = x \) the conclusion fails.

*(c)* (N5): the \( \rulename{{\to}I} \) box opens with the conclusion, so it proves the converse, which every function satisfies.

*(d)* (N11) (part (a)): the negation of \( x > 0 \) is \( x \le 0 \), not \( x < 0 \), so \( \rulename{RAA} \) cannot close this box with \( x > 0 \); the case \( x = 0 \) is never examined, and \( \rulename{\neg I} \) on the box gives only \( x \ge 0 \).

*(e)* (N6), affirming the consequent. No rule licenses it, so it breaks @def-derivation: \( P \to Q \) with \( Q \) gives no \( P \). Here \( n = 4 \) is even and not divisible by \( 6 \).

*(f)* (N8): the disjunction is not derived, and it is false at \( x = 0 \), so \( \rulename{\vee E} \) has no valid first input.
:::

::: {#exr-checking-proofs-a2}
[A2: Drill]

Name the entry of @exm-not-allowed-catalogue that each line commits, if any, and say whether its conclusion is true.

::: {.enumerate options="label=(\alph*)"}
1. "We checked that \( n^2 + n \) is even for \( n = 1, \dots, 6 \), so it is even for every \( n \)."
2. "Let \( \varepsilon > 0 \) and choose \( N \) with \( \abs{a_n - L} < \varepsilon \) for \( n \ge N \); since \( \varepsilon \) was arbitrary, this one \( N \) works for every \( \varepsilon \)."
3. "\( x \) and \( y \) are odd, so \( x = 2k + 1 \) and \( y = 2k + 1 \)."
4. "If \( n \) is divisible by \( 4 \), then \( n \) is even; \( n \) is not divisible by \( 4 \), so \( n \) is not even."
5. "\( n^3 - n \) is even for every integer \( n \): if \( n \) is even, say \( n = 2k \), then \( n^3 - n = 2(4k^3 - k) \); so \( n^3 - n \) is even."
6. "Suppose \( x > 0 \); then \( x^2 > 0 \). Hence if \( x > 0 \), then \( x^2 > 0 \). Since \( x^2 > 0 \), …"
7. "The negation of 'for every \( \varepsilon > 0 \), \( \abs{x} < \varepsilon \)' is 'for some \( \varepsilon \le 0 \), \( \abs{x} \ge \varepsilon \)'."
8. "To prove 'if \( n^2 \) is odd, then \( n \) is odd': suppose \( n \) is odd; then \( n^2 \) is odd."
9. "Let \( x \) and \( y \) be solutions of \( x^2 = 9 \). Then \( x^2 - y^2 = 0 \), so \( (x - y)(x + y) = 0 \), and since \( x \ne y \), \( x + y = 0 \)."
10. "\( a_1 = 2 \) and \( a_{n+1} = a_n^2 - 2 \). Then \( a_2 = 2 \), \( a_3 = 2 \), and so on, so \( a_n = 2 \) for every \( n \ge 1 \)."
11. "Let \( n \) be the positive integer with \( n^2 = 2 \). Then \( 1 < n^2 < 4 \), so \( 1 < n < 2 \)."
12. "From '\( x > 0 \)' and '(\( x > 0 \) implies \( y > 0 \)) and (\( y > 0 \) implies \( z > 0 \))', conclude '\( z > 0 \)' in one line."
:::
:::

::: {.solution}
(a) (N1); true (\( n^2 + n = n(n + 1) \)), still not a proof.

(b) (N2); in general false.

(c) (N4); false (\( x = 1 \), \( y = 3 \)).

(d) (N6), denying the antecedent; false (\( n = 2 \)).

(e) (N7), a missing case: the odd case is never written. The conclusion is true (\( n^3 - n = (n - 1)n(n + 1) \), and of \( n - 1 \), \( n \) one is even), still not a proof.

(f) (N10); "\( x^2 > 0 \)" is false at \( x = 0 \).

(g) (N11), part (b); false. The stated "negation" holds for every \( x \) (take \( \varepsilon = -1 \)), also at \( x = 0 \), where the original holds too, so it is not the negation; the negation is "for some \( \varepsilon > 0 \), \( \abs{x} \ge \varepsilon \)".

(h) (N5); the claim is true, but the proof proves the converse.

(i) (N12) (the "since" also cites the unavailable line \( x \ne y \), an (N9) step); false: \( x = y = 3 \) gives \( x + y = 6 \).

(j) (N13); true. The step "if \( a_n = 2 \), then \( a_{n+1} = 4 - 2 = 2 \)" is one line, and the proof must write it, as the step of an induction.

(k) (N14). The presupposed premise, that such an integer exists, is false, and so is the conclusion that an integer lies strictly between \( 1 \) and \( 2 \).

(l) No entry. No primitive rule writes the step in one line: at level 0 it is \( \rulename{\wedge E} \) twice and \( \rulename{{\to}E} \) twice. From Section 6.3 on, a single TAUT line on the propositional skeleton (@prp-taut-skeleton), citing both premises, also writes it (Section 8.3). Either way it is a matter of level, not an error.
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

::: {#exr-checking-proofs-b3}
[B3: Correct, or which entry?]

Each proof below is correct, or commits one of (N12), (N13), (N14); you are not told how many of each. For a correct proof, name its most delicate step. For a wrong one, name the entry, say whether the claim is true, and give a counterexample to the claim or a repair of the proof.

::: {.enumerate options="label=(\roman*)"}
1. *Claim:* for all integers \( m \), \( n \), if \( m \) and \( n \) are odd, then \( mn \) is odd. *Proof:* write \( m = 2k + 1 \) and \( n = 2l + 1 \) with integers \( k \), \( l \); then \( mn = 4kl + 2k + 2l + 1 = 2(2kl + k + l) + 1 \).
2. *Claim:* for all real \( a \), \( b \), if \( a^2 = b^2 \), then \( a = b \) or \( a = -b \). *Proof:* \( (a - b)(a + b) = a^2 - b^2 = 0 \), and a product of real numbers is \( 0 \) only if a factor is.
3. *Claim:* for all integers \( m \), \( n \), \( m^2 + n^2 \ge 1 \). *Proof:* two different integers are not both \( 0 \), so one of \( m^2 \), \( n^2 \) is at least \( 1 \).
4. *Claim:* every integer \( n \ge 2 \) is a product of primes. *Proof:* if \( n \) is prime, it is a product of one prime. If not, \( n = ab \) with \( 1 < a, b < n \); split \( a \) and \( b \) in the same way, and so on, until only primes remain.
5. *Claim:* \( 1 \) is a solution of \( x^2 + x + 1 = 0 \). *Proof:* let \( x \) be the real solution. Then \( x^3 - 1 = (x - 1)(x^2 + x + 1) = 0 \), so \( x^3 = 1 \), and since \( x \) is real, \( x = 1 \).
:::
:::

::: {.solution}
*(i)* **Correct.** The delicate step is the second \( \rulename{\exists E} \), which uses a second name \( l \). The case \( m = n \) is covered, since nothing stops \( k = l \): the names are distinct, the objects need not be.

*(ii)* **Correct.** The delicate step is the product fact. It gives "\( a - b = 0 \) or \( a + b = 0 \)" (\( \rulename{{\to}E} \), citing it), which is the claim, and no distinctness is assumed.

*(iii)* **(N12); the claim is false**: \( m = n = 0 \) gives \( 0 \). The proof took \( m \) and \( n \) to be different integers.

*(iv)* **(N13); the claim is true.** The "and so on" hides why the splitting ends: each factor is at least \( 2 \) and smaller than the number split. Repair by strong induction (@thm-strong-induction): if every \( k \) with \( 2 \le k < n \) is a product of primes, so is \( n \), being prime or \( ab \) with \( a \), \( b \) in that range.

*(v)* **(N14); the claim is false**: \( 1 + 1 + 1 = 3 \ne 0 \). The presupposed premise "\( x^2 + x + 1 = 0 \) has a real solution" is false, since \( x^2 + x + 1 = (x + \tfrac12)^2 + \tfrac34 > 0 \).

Look-alikes: (i) and (iii) both use two letters; only (iii) assumes the letters differ.

**Marking scheme.** (10 points: 2 per part)
- 1: the verdict.
- 1: for a correct proof, the delicate step named; for a wrong one, the entry with a counterexample (iii, v) or a repair (iv).
Fatal errors (0 for that part): calling (i) an instance of (N12) because \( k \) and \( l \) might be equal; calling (iv) correct.
:::

### C. Going deeper

::: {#exr-checking-proofs-c1}
[C1: The second half]

Let \( f \colon \nR \to \nR \) be continuous at \( a \), as the quantifier pattern of Section 6.1: for every \( \varepsilon > 0 \) there is \( \delta > 0 \) such that \( \abs{f(x) - f(a)} < \varepsilon \) for every real \( x \) with \( \abs{x - a} < \delta \). Suppose \( f(a) > 0 \). Here is a level-1 skeleton for the statement "there is \( \delta > 0 \) such that \( f(x) > 0 \) for every \( x \) with \( \abs{x - a} < \delta \)":

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
*(1)* **Correct.** The skeleton is \( \rulename{\forall I} \) and \( \rulename{{\to}I} \), then \( \rulename{\vee E} \) on the hypothesis itself, so the cases exhaust. The delicate step is the second "choose an integer \( k \)", an \( \rulename{\exists E} \) reusing a name. It is legal: the first box of \( k \) lies inside Case 1, which closed before Case 2 opened, so \( k \) appears in no open assumption, not in the existential and not in the conclusion. Sibling boxes may share a name (Section 5.6); (N4) forbids only a name still in use.

*(2)* **Wrong; line (2) fails; entry (N4) of @exm-not-allowed-catalogue.** The second witness is named \( k \) while the box of \( m = 2k \) is open. Counterexample to the step: \( m = 2 \), \( n = 4 \); no integer \( k \) has \( 2 = 2k \) and \( 4 = 2k \). The conclusion is true: with \( m = 2k \) and \( n = 2l \), \( mn = 4kl \).

*(3)* **Wrong; line (1) fails; entry (N8).** "Either \( x \ge 1 \) or \( x \le 0 \)" is not derived, and is false at \( x = 1/2 \), a counterexample to the step. The conclusion is true; the missing case repairs the proof: if \( 0 < x < 1 \), then \( \abs{x - 1} = 1 - x < 1 < \abs{x} + 1 \).

*(4)* **Wrong; line (2) fails; entry (N9); the claim is false.** Canceling uses the "fact" "if \( ax = bx \), then \( a = b \)", which is neither proved nor a school fact, and is false: \( a = 1 \), \( b = 2 \), \( x = 0 \). It needs \( x \ne 0 \), which no line provides. The claim fails at \( x = 0 \); what is true is "\( x = 0 \) or \( x = 2 \)", from \( x(x - 2) = 0 \).

**Marking scheme.** (10 points: 2.5 per proof)
- For each of (2), (3), (4): the verdict "wrong" (1); the failing line and its entry, (N4), (N8), (N9) (1); a counterexample to the illegal step (0.5).
- For (1): the verdict "correct" (1); the delicate step named as an \( \rulename{\exists E} \) reusing a name in a sibling box (or as the \( \rulename{\vee E} \) on the hypothesis) (1); that step checked against the side condition (0.5).
For (4), "\( \rulename{{\to}E} \) without its antecedent \( x \ne 0 \)" is also accepted. Fatal errors (0 for that proof): calling proof (1) wrong as an instance of (N4) because the name \( k \) recurs; judging (2) or (3) correct because its conclusion is true.
:::

### R. Review

::: {#exr-checking-proofs-r1}
[R1: A dialogue]

Two students discuss a claim.

> **Ana:** For every integer \( n \), \( n^2 + n \) is even.
>
> **Ben:** Why?
>
> **Ana:** Take \( n = 3 \): \( 9 + 3 = 12 \). Take \( n = 4 \): \( 16 + 4 = 20 \). It always works.
>
> **Ben:** That is two numbers.
>
> **Ana:** All right. \( n^2 + n = n(n + 1) \). If \( n \) is even, the product has an even factor. If \( n \) is odd, \( n + 1 \) is even, so again it has an even factor. Either way \( n^2 + n \) is even.
>
> **Ben:** You only did positive numbers.
>
> **Ana:** I never used that \( n \) is positive.

::: {.enumerate options="label=(\alph*)"}
1. Which entry of @exm-not-allowed-catalogue does Ana's first argument commit?
2. Write her second argument as a level-3 proof, and name the rule each sentence carries.
3. Is Ben's last objection right?
4. On which fact does the case split rest, and where was it stated?
:::
:::

::: {.solution}
*(a)* (N1) of @exm-not-allowed-catalogue: two instances, then "always".

*(b)* "Let \( n \) be an integer [\( \rulename{\forall I} \)]. Then \( n^2 + n = n(n + 1) \) [algebra]. By (E1), \( n \) is even or odd [\( \rulename{\vee E} \), with the reason the cases exhaust]. If \( n \) is even, say \( n = 2k \) [\( \rulename{\exists E} \)], then \( n(n + 1) = 2\bigl(k(n + 1)\bigr) \) is even [\( \rulename{\exists I} \), witness \( k(n + 1) \)]. If \( n \) is odd, say \( n = 2k + 1 \), then \( n + 1 = 2(k + 1) \), and \( n(n + 1) = 2\bigl(n(k + 1)\bigr) \) is even [\( \rulename{\exists E} \), \( \rulename{\exists I} \)]. In either case \( n^2 + n \) is even [\( \rulename{\vee E} \), closing; silent at level 3]."

*(c)* No. The box of \( n \) assumed only that \( n \) is an integer, and no line used more, so \( \rulename{\forall I} \) (@def-rules-universal, Section 5.4) gives the claim for every integer: \( n \) is in no premise, and the conclusion is about the bound variable. A proof that used \( n > 0 \) would have had to assume it in the box.

*(d)* (E1), "every integer is even or odd", stated in Section 2.1 as a school fact, before @thm-square-even-implies-even.
:::

<!-- dependency ledger
exm-not-allowed-catalogue (claim): (the section's opening, "Two questions") rules never lead from true lines to a false one | thm-soundness (cited); F1.6 §02's statement (from-counter-models-to-non-derivability; its proof in F1.6 §03, optional)
exm-not-allowed-catalogue (claim): (the Quick check after "Two questions") for integers n(n - 1) >= 0 since no integer lies strictly between 0 and 1; at n = 1/2 the product is -1/4 | school arithmetic of Z (F2.2 promised in STATUS: "nothing between n and n + 1"); checked by verify/ch08/exm-not-allowed-catalogue.py
exm-not-allowed-catalogue (example): (N1) n^2 - n + 11 prime for n = 0..10 with the listed values, 121 = 11^2 at n = 11 | arithmetic; checked by verify/ch08/exm-not-allowed-catalogue.py
exm-not-allowed-catalogue (example): (N2) x^2 not uniformly continuous on R | exm-square-not-uniform (cited)
exm-not-allowed-catalogue (example): (N3)-(N11) instances: A = {-1, 1}; m = 2, n = 4; x = -2 (x^2 = 4 > 1, x < 1; x < 1 and x^2 = 4); 6 even, not a multiple of 4; |0| = 0; x = 1/2, x^2 = 1/4; n = 1; x = 0 for x > 2 -> x^2 > 4 and x <= 2 -> x^2 <= 4; |a_n - 0| >= eps for eps <= 0 | arithmetic and school order facts; checked by verify/ch08/exm-not-allowed-catalogue.py
exm-not-allowed-catalogue (example): (N4) sibling boxes may share a witness name | F1.4 §06 (the remark on two exists-E boxes in the cases of or-E, after exm-existential-elimination-derivations; unlabeled), def-rules-existential (cited)
exm-not-allowed-catalogue (example): (N6) the denying-the-antecedent pattern P -> Q, not P |- not Q has a refuting row (P false, Q true) | inline (one row, by def-truth-value); cor-refuting-row (cited); exm-affirming-the-consequent (cited) covers affirming
exm-not-allowed-catalogue (claim): Argument B of F1.1 §01; F1.4 §04's list of forall-I errors; the warnings of F1.8 §02 | prose pointers to earlier sections (unlabeled passages)
exm-not-allowed-catalogue (solution): (the Quick check on N2) a finite set of natural numbers has a maximum | F2.2 (promised; STATUS row "every non-empty finite set has a maximum")
exm-verify-cases (solution): (x - 1)(x - 2) = x^2 - 3x + 2; a product of two reals is negative only if the factors have opposite signs; x > 2, x < 1 give 2 < 1, not(2 < 1) | school algebra; checked by verify/ch08/exm-verify-cases.py
exm-verify-converse (solution): n = 2k gives n^2 = 2(2k^2); the row P false, Q true refutes P -> Q |- Q -> P; x = -2 for the converse of x > 1 -> x^2 > 1 | inline row (def-truth-value); cor-refuting-row (cited); checked by verify/ch08/exm-verify-converse.py
exm-verify-negation (solution): 1 is odd; no integer is both even and odd; m^2 - k is an integer; 2 != 0 | school arithmetic (F2.2 promised in STATUS: even or odd, not both); checked by verify/ch08/exm-verify-negation.py
exm-verify-scope (solution): multiplying by a positive number keeps >; x^2 - x + 1 = (x - 1/2)^2 + 3/4 > 0; at x = 1/2, x^2 < x | school algebra; checked by verify/ch08/exm-verify-scope.py
exr-checking-proofs-a1 (solution): 3^n > n^2 for n = 0..4; A = {0, 1}, f(x) = x; n = 4 even, not divisible by 6; not(x > 0) iff x <= 0, not(x < 0) iff x >= 0; P -> Q with Q gives no P | arithmetic; trichotomy; def-derivation (cited); checked by verify/ch08/exr-checking-proofs-a1.py
exr-checking-proofs-b1 (solution): (2k + 1) + (2l + 1) = 2(k + l + 1); x > 1 gives x^2 > x; x^2 > 1 gives not(x^2 < 1); x >= 1 gives x^2 >= x >= 1; x = 1; not(x < 1) iff x >= 1 | school algebra; trichotomy; checked by verify/ch08/exr-checking-proofs-b1.py
exr-checking-proofs-b2 (solution): x = 1, y = -1 gives |x| + |y| = 2, |x + y| = 0; lines (3), (4) correct in their cases | arithmetic, school algebra of absolute value; exm-triangle-inequality-cases (cited) for the inequality; checked by verify/ch08/exr-checking-proofs-b2.py
exr-checking-proofs-c1 (solution): -|u| <= u; |u| < r gives u > -r; f(a) - f(a)/2 = f(a)/2 > 0; f(x) <= 0 gives |f(x) - f(a)| >= f(a) > f(a)/2 | school algebra of absolute value; checked by verify/ch08/exr-checking-proofs-c1.py
exr-checking-proofs-c1 (example): continuity at a used only as a quantifier pattern | exm-translate-limit (c) (F1.8 §01)
exr-checking-proofs-c2 (solution): (sqrt2 + sqrt3)^2 = 5 + 2 sqrt6; sqrt6 = sqrt2 sqrt3; sqrt2 sqrt2 = 2; 3 = r^2 - 2r sqrt2 + 2 gives sqrt2 = (r^2 - 1)/(2r); r > 0; rationals closed under +, -, x, / by non-zero | school algebra of square roots (a school fact before thm-nth-root, per NOTATION) and of Q; thm-sqrt2-irrational (cited); checked by verify/ch08/exr-checking-proofs-c2.py
exr-checking-proofs-c3 (solution): n = 4k = 2(2k), n = 6k = 2(3k); m = 2k, n = 2l give mn = 4kl; x = 1/2 for (3) and the case 0 < x < 1; x = 0 for (4); x(x - 2) = 0 | school algebra; trichotomy; F1.4 §06 (sibling boxes); checked by verify/ch08/exr-checking-proofs-c3.py
exm-not-allowed-catalogue (claim): (the 2x2 table) n = 2k gives n^2 = 2(2k^2); forall-E at 1/2 of "x >= 1 or x <= 0" gives a false line that follows; x = -2 has x < 1 and x^2 = 4 | arithmetic; Proof B's line (5) (this section); checked by verify/ch08/exm-not-allowed-catalogue.py
exm-not-allowed-catalogue (claim): (the paragraph after the 2x2 table) a line that follows and is false rests on a false line | thm-soundness (cited); the same statement as the ledger's first line
exm-not-allowed-catalogue (claim): (the flowchart and its caption) a line written by a chain of rules and silent steps is licensed at its level; only a line no chain writes fails | def-derivation, def-levels-of-proof, def-silent-steps (cited or within the chapter)
exm-not-allowed-catalogue (claim): (fold "Two notes on the two columns") the same for quantifiers and equality | F1.6 §02's statement under "From counter-models to non-derivability" (prose; its proof in F1.6 §03, optional, not cited)
exm-not-allowed-catalogue (claim): the families table | a regrouping, read off the entries
exm-not-allowed-catalogue (example): (N11)(a) 0 < x < 3 gives x^2 < 9; x^2 > 9 and x > 0 give x > 3; x = 3 has x^2 = 9 | school algebra; checked by verify/ch08/exm-not-allowed-catalogue.py
exm-not-allowed-catalogue (example): (N12) 2 and 3 are the roots of x^2 - 5x + 6; a = b = 2 gives a + b = 4; forall-E may put one term for two variables | def-rule-universal-elimination (cited); arithmetic; checked by verify/ch08/exm-not-allowed-catalogue.py
exm-not-allowed-catalogue (example): (N13) the step of an induction must be a line | ax-induction, thm-strong-induction (cited); {1/n : n in Z>0} has no least element since 1/(n + 1) < 1/n; checked by verify/ch08/exm-not-allowed-catalogue.py
exm-not-allowed-catalogue (example): (N14) exists-E needs a line exists x phi; "the" needs existence and uniqueness; N largest gives N + 1 <= N | def-rules-existential (cited); F1.4 §08's definite description (prose pointer, "Section 5.8"); arithmetic
exm-not-allowed-catalogue (claim): (fold F8.6-b) a strictly decreasing list in N from a_1 has at most a_1 + 1 terms (stated, not used as a reason); the least positive integer with m^2 > 50 is 8 (7^2 = 49, 8^2 = 64), its existence a premise named in the fold | F2.2 (promised): well-ordering of N, thm-well-ordering; checked by verify/ch08/exm-not-allowed-catalogue.py
exm-not-allowed-catalogue (claim): (fold F8.6-b) no barber shaves exactly those who do not shave themselves | thm-barber (cited)
exm-not-allowed-catalogue (claim): (the valid-but-improper paragraph) forall a forall b phi to forall b forall a phi is forall-E twice and forall-I twice, and no TAUT step; a^2 + b^2 >= 2ab | def-levels-of-proof (within the chapter); F1.5 §03's TAUT paragraph (prose pointer, "Section 8.3"); (a - b)^2 >= 0, school algebra
exm-not-allowed-catalogue (claim): (fold F8.6-c) the traditional names against the entries; affirming a disjunct | a regrouping, read off the entries; F1.1 §07 (prose pointer, "Section 1.6")
exm-not-allowed-catalogue (claim): (the family Quick check) n = 3 has n^2 = n + 6; n = 0 does not | arithmetic; checked by verify/ch08/exm-not-allowed-catalogue.py
exr-checking-proofs-a2 (solution): (a) n(n + 1) even; (c) x = 1, y = 3; (d) n = 2; (e) (2k)^3 - 2k = 2(4k^3 - k), n^3 - n = (n - 1)n(n + 1); (f) x = 0; (g) |x| >= -1 for every x; (i) x = y = 3; (j) a_n = 2 for every n >= 1; (k) no integer squares to 2 | school algebra; checked by verify/ch08/exr-checking-proofs-a2.py
exr-checking-proofs-a2 (solution): (l) the step is wedge-E twice and to-E twice at level 0, or one TAUT line on the propositional skeleton from Section 6.3 on | def-rule-taut (F1.3 §08, prose pointer); prp-taut-skeleton (F1.8 §03, cited); F1.5 §03's TAUT paragraph (prose pointer, "Section 8.3")
exr-checking-proofs-b3 (solution): (i) (2k + 1)(2l + 1) = 2(2kl + k + l) + 1; (ii) (a - b)(a + b) = a^2 - b^2, a product of reals is 0 only if a factor is; (iii) m = n = 0; (iv) every n in [2, 500] is a product of primes; (v) 1 + 1 + 1 = 3, x^2 + x + 1 = (x + 1/2)^2 + 3/4 > 0 | school algebra; thm-strong-induction (cited); checked by verify/ch08/exr-checking-proofs-b3.py
exr-checking-proofs-r1 (solution): n^2 + n = n(n + 1); 2k(2k + 1) = 2(k(2k + 1)); (2k + 1) + 1 = 2(k + 1); n^2 + n even for every integer n | school algebra; checked by verify/ch08/exr-checking-proofs-r1.py
exr-checking-proofs-r1 (solution): every integer is even or odd | (E1) of F1.2 §01 (school fact, stated there; pointer via thm-square-even-implies-even, cited)
exr-checking-proofs-r1 (solution): the box of n assumes only that n is an integer, so forall-I gives every integer | def-rules-universal (F1.4 §04, cited)
-->
