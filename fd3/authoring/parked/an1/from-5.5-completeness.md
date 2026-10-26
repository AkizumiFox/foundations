# Parked: old Section 5.5, Every Cauchy Sequence of Reals Converges

<!-- Parked from fd3 (fd3/authoring/design/layout-proposal.md §4, approved 2026-10-26). Not part of any book's src; nothing builds or scans it.
Old section: fd3 5.5 Every Cauchy Sequence of Reals Converges (05-completeness.md)
Labels: thm-constructed-reals-cauchy-complete, eq-approximant-bound, exr-completeness-a1, exr-completeness-b1, exr-completeness-b2, exr-completeness-c1, exr-completeness-c2
Intended home: AN1.2 / AN1.11 source material (AN1.2 proves the Cauchy criterion from LUB); exm-representatives-need-choice moved to fd3 5.5
-->

# Every Cauchy Sequence of Reals Converges

We built \( \nR \) to fill the holes in \( \nQ \): the Newton sequence is Cauchy in \( \nQ \) and has no rational limit (@thm-sqrt2-cauchy-no-rational-limit), and in \( \nR \) it converges to the class it represents (@thm-terms-converge-to-class, @exm-sqrt2-class). Could \( \nR \) have holes of its own, Cauchy sequences of *real* numbers crowding around nothing? If so, the construction would have to be repeated, with Cauchy sequences of reals in place of Cauchy sequences of rationals, and perhaps again after that. This section proves that it need not be: every Cauchy sequence in \( \nR \) converges in \( \nR \). The proof builds the limit from rationals, by a rule, and so uses no axiom of choice.

Throughout, \( F = \nR \) whenever a result of Chapter 4 is applied, which is legitimate because \( \nR \) is an ordered field (@thm-reals-ordered-field). We use the identification of Section 5.4: a rational \( q \) also denotes the real number \( \kappa(q) \) (@def-rational-embedding). Where an inequality is carried from \( \nR \) back to \( \nQ \), we write \( \kappa \) out, because that step is where the proof must cite @thm-rational-embedding.

## The question

A sequence \( (x_k)_{k \in \nN} \) in \( \nR \) is Cauchy in \( \nR \) (@def-cauchy-sequence-ordered-field with \( F = \nR \)) if for every \( \varepsilon \in \nR_{>0} \) there is \( K \in \nN \) with \( \abs{x_j - x_k} < \varepsilon \) for all \( j, k \ge K \). By @cor-rational-epsilon-suffices (b), it is enough to test the tolerances \( 1/n \) with \( n \in \nZ_{>0} \), and the same holds for convergence. So the tolerances may as well be rational; the terms \( x_k \), however, are real numbers, that is, classes of Cauchy sequences of rationals (@def-reals-cauchy-classes).

We want a real number \( x \) with \( x_k \to x \). A real number is a class \( [a] \) with \( a \in \sC \) (@def-rational-cauchy-sequences), so we need a Cauchy sequence of rationals that "is" the limit. Where would its terms come from? The data are the classes \( x_0, x_1, x_2, \dots \), each of them an infinite set of sequences.

## The theorem

::: {#thm-constructed-reals-cauchy-complete}
[The Constructed Reals Are Cauchy-Complete]

Every Cauchy sequence \( (x_k)_{k \in \nN} \) in \( \nR \) (@def-cauchy-sequence-ordered-field, \( F = \nR \)) converges in \( \nR \) (@def-sequence-limit-ordered-field, \( F = \nR \)).
:::

*Try it first (ten minutes): given a Cauchy sequence of reals, which Cauchy sequence of rationals would you build, and why would its class be the limit?*

::: {.idea}
The obvious candidate is a diagonal. Each \( x_k \) has representatives; take one, \( a^{(k)} \in \sC \) with \( [a^{(k)}] = x_k \), for each \( k \), and use the diagonal terms \( a^{(k)}_k \). This attempt meets two separate obstacles.

- **No control.** A representative may begin with any finite list of rationals and still represent \( x_k \) (@exm-finite-change-equivalent). Its \( k \)-th term may be far from \( x_k \), and the diagonal terms need not settle down at all. Exercise C2 below turns this into a counterexample.
- **No rule.** "Take one representative for each \( k \)" picks one element from each of infinitely many sets, with no rule saying which. That is an instance of the axiom of choice (@fd2:ax-choice), which the construction of \( \nR \) has not used so far.

One device removes both: replace \( x_k \) by a single rational \( q_k \) within \( 1/(k + 1) \) of it, named by a formula. The plan has three steps.

① **The \( q_k \) form a member of \( \sC \).** Compare \( q_j \) with \( q_k \) through the reals \( x_j \) and \( x_k \): \( \abs{q_j - q_k} \le \abs{q_j - x_j} + \abs{x_j - x_k} + \abs{x_k - q_k} \). The outer two are small once \( j, k \) are large, by the choice of the approximant; the middle one is small because \( (x_k) \) is Cauchy. Give each a third of \( \varepsilon \).

② **Its class is a candidate.** Let \( x \coloneqq [(q_k)_k] \). A term approximates its class (@thm-terms-converge-to-class), so \( q_k \to x \) in \( \nR \).

③ **The candidate is the limit.** \( x_k \) is near \( q_k \), which is near \( x \): give each half of the tolerance.

The tolerance in ① must be **rational**, since membership of \( \sC \) is tested with \( \varepsilon \in \nQ_{>0} \) (@def-rational-cauchy-sequences); the triangle inequality, however, is used in \( \nR \), where the \( x_k \) live. Step 1 of the proof ends by carrying the inequality back to \( \nQ \) through \( \kappa \) (@thm-rational-embedding). The formula: \( q_k \coloneqq m_k/(k + 1) \), where \( m_k \) is the integer part of \( (k + 1) x_k \) in the Archimedean field \( \nR \). *Before reading on: why must \( m_k \) be **the** integer part, and not just some integer with \( m_k \le (k + 1) x_k < m_k + 1 \)?*
:::

::: {.proof}
Let \( (x_k) \) be a Cauchy sequence in \( \nR \).

**Step 0: the approximants.** For \( k \in \nN \), let \( m_k \in \nZ \) be the integer part of \( (k + 1) x_k \) in \( \nR \) (@prp-integer-part-ordered-field with \( F = \nR \), which is Archimedean by @thm-constructed-reals-archimedean; there \( \iota_{\nR} = \kappa \) by @thm-rational-embedding (d)), and let \( q_k \coloneqq m_k/(k + 1) \in \nQ \). Since the integer part is unique, \( k \mapsto q_k \) is a function \( \nN \to \nQ \) (@fd2:def-function); no use of @fd2:ax-choice is made. Multiplying \( m_k \le (k + 1) x_k < m_k + 1 \) by the positive element \( 1/(k + 1) \) (@prp-reciprocal-order (a), @prp-ordered-ring-rules (c)), and using \( \kappa(m_k)\kappa(k + 1)^{-1} = \kappa(q_k) \) (@thm-rational-embedding (a), (c)), we get
\[
0 \le x_k - \kappa(q_k) < \kappa\Bigl(\frac{1}{k + 1}\Bigr) \qquad \text{for every } k \in \nN .
\]{#eq-approximant-bound}

**Step 1: \( (q_k) \in \sC \).** Let \( \varepsilon \in \nQ_{>0} \). By @cor-rationals-archimedean-epsilon there is \( K_1 \in \nZ_{>0} \) with \( 1/m < \varepsilon/3 \) for every integer \( m \ge K_1 \); for \( k \ge K_1 \), the integer \( k + 1 \) is \( \ge K_1 \), so \( 1/(k + 1) < \varepsilon/3 \). Next, \( \kappa(\varepsilon/3) \in \nR_{>0} \) by @thm-rational-embedding (b), since \( \varepsilon/3 > 0 \) and \( \kappa(0) = 0 \). As \( (x_k) \) is Cauchy in \( \nR \), there is \( K_2 \in \nN \) with \( \abs{x_j - x_k} < \kappa(\varepsilon/3) \) for all \( j, k \ge K_2 \); fix one such \( K_2 \) [\( \rulename{\exists E} \)], one object for this one \( \varepsilon \). Let \( K \coloneqq \max\{K_1, K_2\} \); it depends on \( \varepsilon \) (and on the sequence) only.

Let \( j, k \ge K \). By @eq-approximant-bound and @thm-rational-embedding (b), \( \abs{x_j - \kappa(q_j)} < \kappa(1/(j + 1)) < \kappa(\varepsilon/3) \), and likewise for \( k \). The triangle inequality in \( \nR \) (@prp-absolute-value-ordered-field (e), applied twice, with \( \abs{-y} = \abs{y} \) from (b)) and @prp-ordered-ring-rules (b) give
\[
\begin{aligned}
\abs{\kappa(q_j) - \kappa(q_k)}
&\le \abs{\kappa(q_j) - x_j} + \abs{x_j - x_k} + \abs{x_k - \kappa(q_k)} \\
&< \kappa(\varepsilon/3) + \kappa(\varepsilon/3) + \kappa(\varepsilon/3) = \kappa(\varepsilon) ,
\end{aligned}
\]
where the last equality is @thm-rational-embedding (a). By @thm-rational-embedding (a) and (c), \( \abs{\kappa(q_j) - \kappa(q_k)} = \abs{\kappa(q_j - q_k)} = \kappa(\abs{q_j - q_k}) \). So \( \kappa(\abs{q_j - q_k}) < \kappa(\varepsilon) \), and @thm-rational-embedding (b) gives \( \abs{q_j - q_k} < \varepsilon \) in \( \nQ \). Hence \( (q_k) \) is Cauchy in \( \nQ \): \( (q_k) \in \sC \).

**Step 2: the candidate.** Let \( x \coloneqq [(q_k)_k] \in \nR \) (@def-reals-cauchy-classes). By @thm-terms-converge-to-class, \( \kappa(q_k) \to x \) in \( \nR \).

**Step 3: \( x_k \to x \).** By @cor-rational-epsilon-suffices (b) it suffices to find, for each \( n \in \nZ_{>0} \), a \( K \in \nN \) with \( \abs{x_k - x} < \kappa(1/n) \) for every \( k \ge K \). Let \( n \in \nZ_{>0} \). The tolerance \( \kappa(1/(2n)) \) is in \( \nR_{>0} \), so Step 2 gives \( K_3 \in \nN \) with \( \abs{\kappa(q_k) - x} < \kappa(1/(2n)) \) for every \( k \ge K_3 \). For \( k \ge 2n \) we have \( k + 1 > 2n \), so \( 1/(k + 1) < 1/(2n) \) (@prp-reciprocal-order (b)), and @eq-approximant-bound with @thm-rational-embedding (b) gives \( \abs{x_k - \kappa(q_k)} < \kappa(1/(2n)) \). Let \( K \coloneqq \max\{K_3, 2n\} \); it depends on \( n \) only. For \( k \ge K \),
\[
\begin{aligned}
\abs{x_k - x} &\le \abs{x_k - \kappa(q_k)} + \abs{\kappa(q_k) - x} \\
&< \kappa\Bigl(\frac{1}{2n}\Bigr) + \kappa\Bigl(\frac{1}{2n}\Bigr) = \kappa\Bigl(\frac{1}{n}\Bigr) ,
\end{aligned}
\]
by @prp-absolute-value-ordered-field (e) and @thm-rational-embedding (a). So \( x_k \to x \) in \( \nR \). This proves the theorem.
:::

The answer to the prompt about \( m_k \): existence alone would give, for each \( k \), a non-empty set of admissible integers, and taking one from each of these infinitely many sets, with no rule, is again a use of choice. Uniqueness makes each of these sets a singleton, so "the integer part of \( (k + 1) x_k \)" names one integer for each \( k \), and Step 0 defines a function outright. Existence of an integer part would not be enough; the proof needs the uniqueness half of @prp-integer-part-ordered-field.

Where is each hypothesis used? The Cauchy property of \( (x_k) \) is used once, for \( K_2 \) in Step 1; Step 3 uses only the approximants and Step 2. The Archimedean property of \( \nR \) is used in Step 0, through the integer part, and in Steps 2 and 3, through @cor-rational-epsilon-suffices (b) (cited in Step 3 and in the proof of @thm-terms-converge-to-class); the Archimedean property of \( \nQ \) is used in Step 1, for \( K_1 \). Without the Cauchy hypothesis the conclusion fails: the sequence \( x_k = k \) has approximants \( q_k = k \), which do not form a member of \( \sC \), and it converges to nothing in \( \nR \), being unbounded (@prp-convergent-bounded-ordered-field, with @thm-constructed-reals-archimedean for the unboundedness).

*Real numbers have no holes of their own.* Together with @prp-convergent-cauchy-ordered-field (with \( F = \nR \)), the theorem says that a sequence in \( \nR \) converges in \( \nR \) **if and only if** it is Cauchy in \( \nR \). In \( \nQ \) the "only if" half holds (@prp-convergent-cauchy-ordered-field, \( F = \nQ \)), and the "if" half fails (@thm-sqrt2-cauchy-no-rational-limit). A second round of the construction, starting from Cauchy sequences of reals, would find every such sequence already convergent: there is no hole left for it to fill.

## The approximant, by a rule

Step 0 is the heart of the proof, so we look at it again. By @thm-constructed-reals-archimedean, \( \nR \) is an Archimedean ordered field. So @prp-integer-part-ordered-field applies with \( F = \nR \), with \( \kappa \) in the role of \( \iota_{\nR} \) (@thm-rational-embedding (d)): for every \( y \in \nR \) there is **exactly one** \( m \in \nZ \) with \( m \le y < m + 1 \), the integer part of \( y \).

For a real number \( x_k \) and the positive integer \( k + 1 \), Step 0 applies this to \( y = (k + 1) x_k \) and divides by \( k + 1 \):
\[
\frac{m_k}{k + 1} \le x_k < \frac{m_k}{k + 1} + \frac{1}{k + 1} .
\]
The rational \( q_k \coloneqq m_k/(k + 1) \) is the largest multiple of \( 1/(k + 1) \) that does not exceed \( x_k \), and it is within \( 1/(k + 1) \) of \( x_k \). Picture the multiples of \( 1/(k + 1) \) as a ladder of rungs; \( q_k \) is the rung at or just below \( x_k \), and the ladder gets finer as \( k \) grows.

The word that matters is **exactly**. For each \( k \) the set of integers \( m \) with \( m \le (k + 1) x_k < m + 1 \) has one element, so the relation "\( q_k = m/(k + 1) \) for the \( m \) with \( m \le (k + 1) x_k < m + 1 \)" assigns exactly one rational to each \( k \in \nN \): it is a function \( \nN \to \nQ \) (@fd2:def-function), given by a rule. Nothing is picked.

::: {.check}
Let \( r \) be the real number of @exm-sqrt2-class, so \( r > 0 \) and \( r^2 = 2 \), and let \( x_k \coloneqq r + 1/(k + 1) \). Compute \( q_0 \), \( q_1 \) and \( q_2 \).
:::

::: {.solution}
First locate \( r \): \( (7/5)^2 = 49/25 < 2 < 9/4 = (3/2)^2 \). If \( r < 7/5 \), then \( r^2 < 49/25 < 2 \), and if \( r \ge 3/2 \), then \( r^2 \ge 9/4 > 2 \) (@prp-ordered-ring-rules (g), with \( r > 0 \)); both contradict \( r^2 = 2 \), so \( 7/5 \le r < 3/2 \).

Next, \( (k + 1) x_k = (k + 1) r + 1 \). For \( k = 0 \): \( 12/5 \le r + 1 < 5/2 \), and \( 2 \le 12/5 \), \( 5/2 < 3 \), so \( m_0 = 2 \). For \( k = 1 \): \( 19/5 \le 2r + 1 < 4 \), and \( 3 \le 19/5 \), so \( m_1 = 3 \). For \( k = 2 \): \( 26/5 \le 3r + 1 < 11/2 \), and \( 5 \le 26/5 \), \( 11/2 < 6 \), so \( m_2 = 5 \). Hence
\[
q_0 = 2 , \qquad q_1 = \frac{3}{2} , \qquad q_2 = \frac{5}{3} .
\]
Each \( q_k \) is within \( 1/(k + 1) \) below \( x_k \); for instance \( x_2 = r + 1/3 \in [26/15, 11/6) \) and \( q_2 = 5/3 = 25/15 \).
:::

## Exercises

### A. Check your understanding

::: {#exr-completeness-a1}
[A1]

These questions are about the proof of @thm-constructed-reals-cauchy-complete.

::: {.enumerate options="label=(\alph*)"}
1. Why \( \varepsilon/3 \) in Step 1? Which three distances does it bound, and in which field is each of them measured?
2. Why \( 1/(2n) \) in Step 3, for each of the two distances there?
3. Where is the Cauchy property of \( (x_k) \) used? Is it used in Step 3?
4. Run the construction on the constant sequence \( x_k = r \) (the real number of @exm-sqrt2-class). Which class is \( x \)?
5. Write "\( (x_k) \) converges in \( \nR \)" in symbols, and its negation.
:::
:::

::: {.solution}
(a) Step 1 bounds \( \abs{q_j - q_k} \) through \( x_j \) and \( x_k \): the three distances are \( \abs{\kappa(q_j) - x_j} \) and \( \abs{x_k - \kappa(q_k)} \), each below \( \kappa(1/(j + 1)) \) or \( \kappa(1/(k + 1)) \) by the choice of approximant, and \( \abs{x_j - x_k} \), small because \( (x_k) \) is Cauchy. All three are measured in \( \nR \); only the conclusion \( \abs{q_j - q_k} < \varepsilon \) is carried back to \( \nQ \). Three thirds make one \( \varepsilon \).

(b) Two distances are added: \( \abs{x_k - \kappa(q_k)} < \kappa(1/(2n)) \) for \( k \ge 2n \), from the approximant bound, and \( \abs{\kappa(q_k) - x} < \kappa(1/(2n)) \) for \( k \ge K_3 \), from @thm-terms-converge-to-class. Two halves make \( 1/n \).

(c) Only in Step 1, for the threshold \( K_2 \). Step 3 uses the approximant bound and Step 2, not the Cauchy property directly: by then it has been spent on making \( (q_k) \) a member of \( \sC \).

(d) The approximants are \( q_k = m_k/(k + 1) \), with \( m_k \) the integer part of \( (k + 1) r \), and \( x \coloneqq [(q_k)] \). By the theorem's proof, \( x_k \to x \); the constant sequence \( r \) also tends to \( r \), so \( x = r \) by @thm-limit-unique-ordered-field. Concretely, \( q_0 = 1 \), \( q_1 = 1 \) (since \( 2 \le 2r < 3 \)), \( q_2 = 4/3 \) (since \( 4 \le 3r < 5 \)): a third sequence of rationals, besides the Newton sequence of @exm-newton-rationals-sqrt2 and the truncations \( (d_k) \), both in the class \( r \) by @exm-sqrt2-class.

(e) Converges: \( \exists x \in \nR \ \forall \varepsilon \in \nR_{>0} \ \exists K \in \nN \ \forall k \in \nN \ (k \ge K \Rightarrow \abs{x_k - x} < \varepsilon) \). Negation (@fd1:prp-quantifier-negation, @fd1:prp-bounded-quantifier-negation, @fd1:prp-negated-implication, and \( \neg(y < \varepsilon) \) read as \( y \ge \varepsilon \) by (O1)):
\[
\forall x \in \nR \ \ \exists \varepsilon \in \nR_{>0} \ \ \forall K \in \nN \ \ \exists k \in \nN \ \ \bigl( k \ge K \wedge \abs{x_k - x} \ge \varepsilon \bigr) .
\]
Every candidate is beaten by some tolerance beyond every threshold.
:::

### B. Practice

::: {#exr-completeness-b1}
[B1]

Which results of Chapter 4, applied with \( F = \nR \), show that in \( \nR \) every convergent sequence is Cauchy and has only one limit? Why may they be applied? Deduce that a sequence in \( \nR \) converges if and only if it is Cauchy.
:::

::: {.solution}
@prp-convergent-cauchy-ordered-field (convergent sequences are Cauchy) and @thm-limit-unique-ordered-field (uniqueness of limits). Both are proved in Chapter 4 for an arbitrary ordered field \( F \), and \( \nR \) is an ordered field by @thm-reals-ordered-field, so they apply with \( F = \nR \) and tolerances in \( \nR_{>0} \).

If \( (x_k) \) converges in \( \nR \), it is Cauchy in \( \nR \) by the first; if it is Cauchy in \( \nR \), it converges by @thm-constructed-reals-cauchy-complete. So the two properties coincide in \( \nR \), and the limit is unique by the second.
:::

::: {#exr-completeness-b2}
[B2]

Let \( (p_k) \) be a sequence of rationals such that \( (\kappa(p_k))_k \) converges in \( \nR \) to some \( x \). Prove that \( (p_k) \in \sC \) and that \( x = [(p_k)] \).

*Hint: a convergent sequence is Cauchy.*
:::

::: {.solution}
By @prp-convergent-cauchy-ordered-field with \( F = \nR \), \( (\kappa(p_k)) \) is Cauchy in \( \nR \). Let \( \varepsilon \in \nQ_{>0} \). Then \( \kappa(\varepsilon) \in \nR_{>0} \) (@thm-rational-embedding (b)), so there is \( K \) with \( \abs{\kappa(p_j) - \kappa(p_k)} < \kappa(\varepsilon) \) for \( j, k \ge K \). As in Step 1 of the proof of @thm-constructed-reals-cauchy-complete, the left side is \( \kappa(\abs{p_j - p_k}) \) (@thm-rational-embedding (a), (c)), and @thm-rational-embedding (b) gives \( \abs{p_j - p_k} < \varepsilon \). So \( (p_k) \) is Cauchy in \( \nQ \), that is, \( (p_k) \in \sC \).

By @thm-terms-converge-to-class, \( \kappa(p_k) \to [(p_k)] \). Also \( \kappa(p_k) \to x \). By @thm-limit-unique-ordered-field with \( F = \nR \), \( x = [(p_k)] \).

So the real numbers that are limits of sequences of rationals in \( \nR \) are exactly the classes of those sequences; with @thm-terms-converge-to-class, every real number is one.
:::

### C. Going deeper

::: {#exr-completeness-c1}
[C1: Exit check: Cauchy completeness]

Prove that every Cauchy sequence in \( \nR \) converges in \( \nR \). Say where the axiom of choice could have entered your proof, and why it does not.
:::

::: {.solution}
Let \( (x_k) \) be Cauchy in \( \nR \).

*Approximants by a rule.* For \( k \in \nN \) let \( m_k \) be the integer part of \( (k + 1) x_k \), unique by @prp-integer-part-ordered-field (\( \nR \) is Archimedean, @thm-constructed-reals-archimedean), and \( q_k \coloneqq m_k/(k + 1) \). Then \( 0 \le x_k - q_k < 1/(k + 1) \), and \( k \mapsto q_k \) is a function because the integer part is unique. This is where choice could have entered: "for each \( k \) take some rational within \( 1/(k + 1) \) of \( x_k \)", or "take a representative of each \( x_k \)", makes infinitely many picks with no rule, a use of @fd2:ax-choice. The integer part names one rational for each \( k \), so no choice is made.

*Cauchy in \( \nQ \).* Let \( \varepsilon \in \nQ_{>0} \). Fix \( K_1 \) with \( 1/(k + 1) < \varepsilon/3 \) for \( k \ge K_1 \) (@cor-rationals-archimedean-epsilon) and \( K_2 \) with \( \abs{x_j - x_k} < \varepsilon/3 \) for \( j, k \ge K_2 \) (the Cauchy property, at the positive real \( \kappa(\varepsilon/3) \)). For \( j, k \ge \max\{K_1, K_2\} \), the triangle inequality in \( \nR \) gives \( \abs{q_j - q_k} < \varepsilon/3 + \varepsilon/3 + \varepsilon/3 = \varepsilon \) in \( \nR \); since \( \kappa \) preserves sums, absolute values and order and reflects order (@thm-rational-embedding (a)–(c)), the same inequality holds in \( \nQ \). So \( (q_k) \in \sC \).

*The limit.* Let \( x \coloneqq [(q_k)] \). By @thm-terms-converge-to-class, \( q_k \to x \) in \( \nR \). Let \( \varepsilon \in \nR_{>0} \). By @cor-rational-epsilon-suffices (a) there is \( n \in \nZ_{>0} \) with \( 1/n < \varepsilon \). Fix \( K_3 \) with \( \abs{q_k - x} < 1/(2n) \) for \( k \ge K_3 \). For \( k \ge \max\{K_3, 2n\} \), \( \abs{x_k - x} \le \abs{x_k - q_k} + \abs{q_k - x} < 1/(2n) + 1/(2n) = 1/n < \varepsilon \). So \( x_k \to x \).

**Marking scheme.** (10 points)
- 2: an approximant \( q_k \in \nQ \) defined by a rule (unique integer part, or another explicit formula), with an explicit bound on \( \abs{x_k - q_k} \) tending to \( 0 \).
- 3: \( (q_k) \in \sC \) by an \( \varepsilon/3 \) (or equivalent) estimate, with **rational** \( \varepsilon \) and the passage from \( \nR \) back to \( \nQ \) through \( \kappa \) justified.
- 1: the candidate \( x = [(q_k)] \) named.
- 2: \( q_k \to x \) in \( \nR \), by @thm-terms-converge-to-class, or directly as in its proof: \( \abs{x - \kappa(q_k)} = [(\abs{q_m - q_k})_m] \) (@prp-reals-absolute-value-termwise), bounded through @lem-termwise-order, which gives only \( \le \). Either route earns both points.
- 2: \( x_k \to x \), with the threshold chosen after the tolerance and depending on it only.
Fatal errors (0 for the step): approximants or representatives "chosen" with no rule and no mention of choice; a real \( \varepsilon \) used to test membership of \( \sC \); "\( q_k \to x \) because \( x \) is the limit of \( (q_k) \)" (circular: that is what @thm-terms-converge-to-class proves). A proof that uses choice openly (representatives, with a threshold for each) and says so proves the theorem, but earns at most 1 of the 2 points of the first step, since the question asks for a construction that avoids it.
:::

::: {#exr-completeness-c2}
[C2: Find the error]

Here is an argument for @thm-constructed-reals-cauchy-complete. Is its conclusion true? Does the argument prove it? If not, name the first line that fails and why.

> (1) Let \( (x_k) \) be a Cauchy sequence in \( \nR \).
> (2) For each \( k \in \nN \), pick a representative \( a^{(k)} \in \sC \) of \( x_k \).
> (3) Let \( q_k \coloneqq a^{(k)}_k \), the \( k \)-th term of the \( k \)-th representative.
> (4) The sequence \( (q_k) \) is Cauchy in \( \nQ \), and \( \abs{x_k - \kappa(q_k)} \to 0 \) in \( \nR \), since each \( a^{(k)} \) is Cauchy and \( (x_k) \) is Cauchy.
> (5) Let \( x \coloneqq [(q_k)] \). Then \( x_k \to x \), by an \( \varepsilon/2 \) argument through the terms \( q_k \).
:::

::: {.solution}
[Hint 1]

Ask whether \( a^{(k)}_k \) has to be close to \( x_k \) at all.
:::

::: {.solution}
[Hint 2]

Try the constant sequence \( x_k = 0 \) for every \( k \), and representatives that are not \( 0 \) at their first few terms.
:::

::: {.solution}
*The conclusion is true:* it is @thm-constructed-reals-cauchy-complete.

*The failing line is (4).* Each \( a^{(k)} \) being Cauchy says that the terms of one representative settle down eventually, past a threshold that depends on \( k \); nothing ties the \( k \)-th term of \( a^{(k)} \) to \( x_k \), and nothing ties different representatives to each other at index \( k \). The Cauchy property of \( (x_k) \) is about the classes, and the line uses it as if it were about the diagonal terms.

*Counterexample to the step.* Let \( x_k = 0 \) for every \( k \), a Cauchy sequence in \( \nR \). For each \( k \), let \( a^{(k)}_n \coloneqq k \) for \( n \le k \) and \( a^{(k)}_n \coloneqq 0 \) for \( n > k \). Each \( a^{(k)} \) is eventually equal to the zero sequence, so it is in \( \sC \) and represents \( 0 \) (@exm-finite-change-equivalent). Then \( q_k = a^{(k)}_k = k \), and \( (k) \) is not Cauchy in \( \nQ \): consecutive terms satisfy \( \abs{q_{k+1} - q_k} = 1 \), so the Cauchy condition fails for \( \varepsilon = 1 \). Nor does \( \abs{x_k - \kappa(q_k)} = \kappa(k) \) tend to \( 0 \): it is \( \ge 1 \) for every \( k \ge 1 \). The premises of (4) hold and both parts of its conclusion fail.

*A second, separate defect: line (2).* "For each \( k \), pick" makes one pick from each of infinitely many classes with no rule: an unflagged use of @fd2:ax-choice (@exm-representatives-need-choice). Even if (4) were repaired, the argument would use choice without saying so. Line (5) is correct given (4): \( \kappa(q_k) \to x \) in \( \nR \) by @thm-terms-converge-to-class, and \( \abs{x_k - x} \le \abs{x_k - \kappa(q_k)} + \abs{\kappa(q_k) - x} \). The bound on \( \abs{x_k - \kappa(q_k)} \) is needed: knowing only that \( (q_k) \) is Cauchy would not do (with \( a^{(k)}_n = 1 \) for \( n \le k \) and \( 0 \) after, \( q_k = 1 \) for every \( k \), yet \( x_k = 0 \) does not tend to \( [(1)] = 1 \)).

*Repair.* Either keep representatives and control the diagonal (for each \( k \), go far enough out in \( a^{(k)} \) that its terms are within \( 1/(k + 1) \) of \( x_k \), which @thm-terms-converge-to-class makes possible, and use that term in place of \( a^{(k)}_k \)), at the price of a choice of representatives and of thresholds, flagged; or, better, drop representatives and use the integer-part approximant \( q_k = m_k/(k + 1) \) of the text, which needs no choice at all.

**Marking scheme.** (10 points)
- 2: says the conclusion is true, and cites the theorem.
- 3: identifies line (4) as the failing line, and says why: nothing ties \( a^{(k)}_k \) to \( a^{(j)}_j \) for \( j \ne k \), or to \( x_k \).
- 3: a counterexample to the step, with every representative checked to lie in its class.
- 2: names the use of choice in line (2), and a repair that replaces \( q_k \) by a rational with a bound on \( \abs{x_k - \kappa(q_k)} \) tending to \( 0 \) (a later term of \( a^{(k)} \), or the integer-part approximant).
Fatal errors (0 for the step): calling the conclusion false; a "counterexample" in which the sequence \( (x_k) \) is not Cauchy.
:::

<!-- dependency ledger
thm-constructed-reals-cauchy-complete (proof): kappa(m/(k+1)) = kappa(m) kappa(k+1)^{-1}, kappa(n) = n * 1_R | thm-rational-embedding (a), (c), (d), cited in Step 0
thm-constructed-reals-cauchy-complete (proof): dividing an inequality by k + 1 > 0 in R | prp-ordered-ring-rules (c), prp-reciprocal-order (a) (in R, F3.9 results with F = R via thm-reals-ordered-field)
thm-constructed-reals-cauchy-complete (proof): k >= K_1 implies the integer k + 1 >= K_1; k >= 2n implies k + 1 > 2n | thm-omega-order, prp-omega-order-arithmetic (c); inline
thm-constructed-reals-cauchy-complete (proof): epsilon/3 + epsilon/3 + epsilon/3 = epsilon and 1/(2n) + 1/(2n) = 1/n in Q | field arithmetic in Q (thm-rationals-ordered-field); inline
thm-constructed-reals-cauchy-complete (proof): relation with exactly one output for each input is a function | fd2:def-function, cited
thm-constructed-reals-cauchy-complete (claim): x_k = k is unbounded in R, so not convergent | thm-constructed-reals-archimedean, prp-convergent-bounded-ordered-field, cited
thm-constructed-reals-cauchy-complete (solution): quick check, 7/5 <= r < 3/2 from (7/5)^2 < 2 < (3/2)^2; integer parts 2, 3, 5 | exm-sqrt2-class (r > 0, r^2 = 2), prp-ordered-ring-rules (g); verify/ch05/thm-constructed-reals-cauchy-complete.py
exr-completeness-a1 (solution): q_0 = 1, q_1 = 1, q_2 = 4/3 for x_k = r | verify/ch05/exr-completeness-a1.py
exr-completeness-c2 (solution): an eventually zero sequence represents 0 | exm-finite-change-equivalent, cited
exr-completeness-c2 (solution): (k) is not Cauchy in Q, since |(k+1) - k| = 1 | inline
exr-completeness-c2 (solution): kappa(k) >= 1 for k >= 1 | thm-rational-embedding (b), inline
-->
