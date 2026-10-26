# Cauchy Sequences

<!-- S3: style revision per S1 change list (layout-proposal.md §3, 4.5, pipeline S): the negated-quantifier definition by an Idea pointing to *Logic and Proof*, Chapter 6; trim. -->

Every convergence proof so far began with the limit in hand: to show \( a_n \to a \) we estimated \( \abs{a_n - a} \), and the limit laws of Section 4.4 compute a new limit only from limits already known. That is no help for the sequence of Chapter 3 that closes in on the gap at \( \sqrt 2 \) (@exm-newton-rationals-sqrt2), whose terms \( 2, 3/2, 17/12, 577/408, \dots \) visibly settle down while no rational is available to be their limit. This section names a property that can be checked from the terms alone: eventually they are all close **to each other**. We prove the facts about it that Chapter 5 needs: convergent sequences have it, sequences with it are bounded and closed under sums and products, and, when such a sequence does not tend to \( 0 \), its terms eventually keep one sign and stay away from \( 0 \).

Throughout, \( F \) is an ordered field (@def-ordered-ring-and-field), sequences are indexed by \( \nN \) (@def-sequence-ordered-field), and \( \varepsilon \) ranges over \( F_{>0} \). We use the absolute-value rules of @prp-absolute-value-ordered-field and the halving rules of @prp-ordered-field-halves without restating them, and write \( 2 \) for \( 1 + 1 \) in \( F \).

## Terms that agree with one another

A limit relates a sequence to a point of \( F \); boundedness (@def-bounded-sequence-ordered-field) is a property of the sequence alone. We want a second property of the sequence alone, saying "the terms settle down" without saying where.

In \( \nQ \) the Newton terms satisfy \( 17/12 - 577/408 = 1/408 \), and the later terms are closer still to one another (Section 4.6 proves it). The way to say "settle down" without a target is to compare terms with terms: however small a tolerance is named, from some index on, any two terms differ by less than it.

*The terms eventually agree with one another to within any tolerance.*

::: {#def-cauchy-sequence-ordered-field}
[Cauchy Sequence]

A sequence \( (a_n)_{n \in \nN} \) in \( F \) is a **Cauchy sequence in \( F \)** (or **Cauchy**) if **for every** \( \varepsilon \in F_{>0} \) **there exists** \( N \in \nN \) such that \( \abs{a_m - a_n} < \varepsilon \) **for all** \( m, n \in \nN \) with \( m \ge N \) and \( n \ge N \). In symbols:
\[
\begin{aligned}
&\forall \varepsilon \in F_{>0} \ \ \exists N \in \nN \ \ \forall m \in \nN \ \ \forall n \in \nN \\
&\qquad \bigl( (m \ge N \wedge n \ge N) \Rightarrow \abs{a_m - a_n} < \varepsilon \bigr) .
\end{aligned}
\]
:::

In words: the first quantifier says the tolerance is arbitrary and is named first; the second says a threshold exists, and since it comes after \( \varepsilon \), it may depend on \( \varepsilon \) and on nothing else; the last two say that **every** pair of indices beyond the threshold, near or far apart, gives terms within \( \varepsilon \) of each other. Compared with @def-sequence-limit-ordered-field, the point \( a \) has been replaced by a second index \( m \).

The tolerances are the elements of \( F_{>0} \), so the field is part of the definition. For \( F = \nQ \), the tolerances are rational, and "Cauchy in \( \nQ \)" is a statement about rationals only, as Chapter 5 needs. Since \( \abs{a_m - a_n} = \abs{a_n - a_m} \) (@prp-absolute-value-ordered-field (b)), the roles of \( m \) and \( n \) are symmetric, and there is nothing else to check for the definition to make sense.

**Negation.** Moving \( \neg \) inward quantifier by quantifier (@fd1:prp-bounded-quantifier-negation, @fd1:prp-negated-implication) and reading \( \neg(x < \varepsilon) \) as \( x \ge \varepsilon \) by (O1), "\( (a_n) \) is not Cauchy" reads
\[
\exists \varepsilon \in F_{>0} \ \ \forall N \in \nN \ \ \exists m, n \in \nN \ \ \bigl( m \ge N \wedge n \ge N \wedge \abs{a_m - a_n} \ge \varepsilon \bigr) .
\]
One tolerance is beaten beyond every threshold.

**Examples.**

*A constant sequence.* Let \( a_n = c \) for every \( n \). Then \( \abs{a_m - a_n} = \abs{0} = 0 < \varepsilon \) for all \( m, n \), so \( N = 0 \) works for every \( \varepsilon \). This degenerate case matters: Chapter 5 represents each rational \( c \) by its constant sequence.

*The reciprocals in \( \nQ \).* Let \( a_n = 1/(n + 1) \) in \( \nQ \). Given \( \varepsilon \in \nQ_{>0} \), @cor-rationals-archimedean-epsilon gives \( N \in \nZ_{>0} \) with \( 1/N < \varepsilon \). Let \( m, n \ge N \). Then \( m + 1 > N \) and \( n + 1 > N \), so \( 0 < 1/(m + 1) < 1/N \) and \( 0 < 1/(n + 1) < 1/N \) (@prp-reciprocal-order). Two elements \( x, y \) of \( (0, c) \) satisfy \( x - y < x < c \) and \( y - x < y < c \), so \( \abs{x - y} < c \) by @prp-absolute-value-ordered-field (d). Hence \( \abs{a_m - a_n} < 1/N < \varepsilon \). The threshold depends on \( \varepsilon \) only: for \( \varepsilon = 1/100 \), \( N = 101 \) works.

*Sequences with a limit.* By the first result of the next subsection, the convergent sequences of Section 4.3 (@exm-first-sequences-ordered-field) are all examples. The definition earns its keep on sequences with no limit available, which Section 4.6 supplies.

**Non-example by a minimal change.** Change the constant sequence \( 1 \) at every odd index: let \( a_n = 1 \) for even \( n \) and \( a_n = 0 \) for odd \( n \). The sequence is still bounded, by \( 1 \), and every two terms still differ by at most \( 1 \). What fails is "for every \( \varepsilon \)": take \( \varepsilon = 1 \). Whatever \( N \) is offered, the indices \( N \) and \( N + 1 \) are both \( \ge N \), one even and one odd, and their terms differ by \( 1 \not< 1 \). So the negation above holds with \( \varepsilon = 1 \), \( m = N \), \( n = N + 1 \).

**Why this definition.** Each clause is there for a reason.

- *Every pair, not only neighbors.* Asking only that \( \abs{a_{n+1} - a_n} < \varepsilon \) for \( n \ge N \) is too weak: the example at the end of this section has consecutive differences tending to \( 0 \) and is not Cauchy.
- *The threshold after the tolerance.* With the quantifiers swapped, "\( \exists N \ \forall \varepsilon \ \forall m, n \ge N \)", the condition forces \( \abs{a_m - a_n} < \varepsilon \) for every \( \varepsilon \), hence \( a_m = a_n \) for all \( m, n \ge N \) (the argument of @thm-limit-unique-ordered-field): only sequences that are eventually constant would qualify.
- *Tolerances from the field.* Changing the set of tolerances changes the notion: in the non-Archimedean field \( \nQ(t) \) of Section 4.2 there are more tolerances than in \( \nQ \), among them \( 1/t \), and Exercise C2 of Section 4.6 shows a sequence of rationals that passes every rational test and fails the test \( 1/t \).

::: {.warning}
The definition asks for **one** \( N \) that serves **every** pair \( m, n \ge N \). A proof that checks only some pairs, say each \( n \) against \( n + 2 \), proves nothing: in the non-example above, \( a_{n+2} = a_n \) for every \( n \), so those pairs pass every test, and the sequence still fails.
:::

**Payoff.** The tail-change principle extends at once. If \( a_n = b_n \) for every \( n \ge N_0 \) and \( (a_n) \) is Cauchy, then for \( \varepsilon \in F_{>0} \) and its threshold \( N \) for \( (a_n) \), every \( m, n \ge \max\{N, N_0\} \) give \( \abs{b_m - b_n} = \abs{a_m - a_n} < \varepsilon \). So \( (b_n) \) is Cauchy, with thresholds \( \max\{N, N_0\} \), as in @prp-tail-change-ordered-field.

## Convergent sequences are Cauchy, and Cauchy sequences are bounded

The first result says the new property is no stronger than convergence: it is a necessary condition, one we can test without knowing the limit.

::: {#prp-convergent-cauchy-ordered-field}
[Convergent Sequences Are Cauchy]

If \( a_n \to a \) in \( F \), then \( (a_n) \) is a Cauchy sequence in \( F \).
:::

::: {.idea}
Two terms that are each within \( \varepsilon/2 \) of \( a \) are within \( \varepsilon \) of each other: insert the point \( a \) between them with the triangle inequality, and spend half the tolerance on each side.
:::

::: {.proof}
Let \( \varepsilon \in F_{>0} \). Then \( \varepsilon/2 \in F_{>0} \) by @prp-ordered-field-halves (b), so, since \( a_n \to a \), there is \( N \in \nN \) with \( \abs{a_n - a} < \varepsilon/2 \) for every \( n \ge N \); \( N \) depends only on \( \varepsilon \). Let \( m, n \ge N \). By the three-point triangle inequality (@prp-absolute-value-ordered-field (e)) with \( a \) in the middle, and by \( \abs{a - a_n} = \abs{a_n - a} \) (@prp-absolute-value-ordered-field (b)),
\[
\abs{a_m - a_n} \le \abs{a_m - a} + \abs{a - a_n} < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon ,
\]
where the strict inequality adds two strict inequalities (@prp-ordered-ring-rules (b)) and the equality is @prp-ordered-field-halves (b). This proves that \( (a_n) \) is Cauchy.
:::

The converse is the question of the chapter. In \( \nQ \) it fails (Section 4.6); Chapter 5 builds a field in which it holds.

::: {.check}
Is the sequence \( \bigl( (-1)^n/(n + 1) \bigr)_{n \in \nN} \) Cauchy in \( \nQ \)? Answer without estimating \( \abs{a_m - a_n} \).
:::

::: {.solution}
Yes. The sequence \( (1/(n + 1)) \) is null in \( \nQ \) (@exm-first-sequences-ordered-field), and \( ((-1)^n) \) is bounded by \( 1 \), since \( \abs{(-1)^n} = 1 \) (by induction, with \( \abs{xy} = \abs{x}\abs{y} \), @prp-absolute-value-ordered-field (b)). So the product is null by @prp-null-times-bounded-ordered-field. A null sequence converges, to \( 0 \), so it is Cauchy by @prp-convergent-cauchy-ordered-field.
:::

The second result is the Cauchy version of @prp-convergent-bounded-ordered-field. There the tail was trapped near the limit \( a \); here no limit is available, so we trap the tail near one of its own terms.

::: {#prp-cauchy-bounded-ordered-field}
[Cauchy Sequences Are Bounded]

Every Cauchy sequence in \( F \) is bounded.
:::

::: {.idea}
Apply the definition once, with the tolerance \( 1 \). It gives an index \( N \) beyond which every term is within \( 1 \) of the term \( a_N \), a base point we can name. The finitely many terms before \( N \) are handled by a finite maximum, as for convergent sequences.
:::

::: {.proof}
Let \( (a_n) \) be Cauchy in \( F \). Since \( 1 \in F_{>0} \) (@prp-ordered-ring-rules (e)), there is \( N \in \nN \) with \( \abs{a_m - a_n} < 1 \) for all \( m, n \ge N \). For \( n \ge N \), taking \( m = N \) and using the triangle inequality (@prp-absolute-value-ordered-field (e), (b)),
\[
\abs{a_n} = \abs{(a_n - a_N) + a_N} \le \abs{a_n - a_N} + \abs{a_N} < 1 + \abs{a_N} .
\]
Let
\[
M \coloneqq \max\{ \abs{a_0}, \dots, \abs{a_{N-1}}, \abs{a_N} + 1 \} ,
\]
a finite maximum in the totally ordered set \( F \) (@fd2:prp-finite-max, whose proof works in any totally ordered set; for \( N = 0 \) the set is \( \{ \abs{a_0} + 1 \} \) and \( M = \abs{a_0} + 1 \)). Then \( M \ge \abs{a_N} + 1 \ge 1 > 0 \), so \( M \in F_{>0} \). For \( n < N \), \( \abs{a_n} \le M \) because \( \abs{a_n} \) is in the set; for \( n \ge N \), \( \abs{a_n} < \abs{a_N} + 1 \le M \). So \( \abs{a_n} \le M \) for every \( n \in \nN \), and \( (a_n) \) is bounded (@def-bounded-sequence-ordered-field).
:::

The bound \( M \) depends on the whole sequence, not on any tolerance. That is what makes it usable in the next proof: it can be fixed before \( \varepsilon \) is named.

## Sums and products of Cauchy sequences

Chapter 5 will add and multiply real numbers by adding and multiplying Cauchy sequences of rationals term by term. For that, sums and products of Cauchy sequences must again be Cauchy. The limit laws (@thm-limit-laws-ordered-field) do not apply, since they need limits; the proofs below copy their estimates with a second index in place of the limit.

::: {#thm-cauchy-algebra-ordered-field}
[Sums and Products of Cauchy Sequences]

Let \( (a_n) \) and \( (b_n) \) be Cauchy sequences in \( F \), and let \( c \in F \).

::: {.enumerate options="label=(\alph*)"}
1. Every constant sequence and every null sequence in \( F \) is Cauchy.
2. The sequences \( (a_n + b_n) \), \( (c \, a_n) \), \( (-a_n) \) and \( (a_n - b_n) \) are Cauchy.
3. The sequence \( (a_n b_n) \) is Cauchy.
:::
:::

::: {.idea}
(a) is @prp-convergent-cauchy-ordered-field. For (b), split \( \varepsilon \): give each of \( (a_n) \) and \( (b_n) \) the tolerance \( \varepsilon/2 \) and take the larger threshold. For (c), the difference \( a_n b_n - a_m b_m \) splits as \( a_n (b_n - b_m) + b_m (a_n - a_m) \). The factors \( a_n \) and \( b_m \) do not get small, but they are bounded (@prp-cauchy-bounded-ordered-field). So **bound, then shrink**: replace each factor we cannot control by a bound fixed in advance, then make the other factor small enough to absorb the bound.
:::

::: {.proof}
(a) A constant sequence \( (c) \) converges to \( c \), and a null sequence converges to \( 0 \) (@exm-first-sequences-ordered-field, @def-null-sequence-ordered-field). Both are Cauchy by @prp-convergent-cauchy-ordered-field.

(b) *Sums.* Let \( \varepsilon \in F_{>0} \), so \( \varepsilon/2 \in F_{>0} \) (@prp-ordered-field-halves (b)). Since \( (a_n) \) is Cauchy, there is \( N_1 \) with \( \abs{a_m - a_n} < \varepsilon/2 \) for all \( m, n \ge N_1 \); since \( (b_n) \) is Cauchy, there is \( N_2 \) with \( \abs{b_m - b_n} < \varepsilon/2 \) for all \( m, n \ge N_2 \). Let \( N \coloneqq \max\{N_1, N_2\} \), which depends only on \( \varepsilon \). For \( m, n \ge N \), we have \( (a_m + b_m) - (a_n + b_n) = (a_m - a_n) + (b_m - b_n) \) (@prp-ring-algebra), so the triangle inequality (@prp-absolute-value-ordered-field (e)) gives
\[
\begin{aligned}
\abs{(a_m + b_m) - (a_n + b_n)} &\le \abs{a_m - a_n} + \abs{b_m - b_n} \\
&< \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon ,
\end{aligned}
\]
where the strict step adds two strict inequalities (@prp-ordered-ring-rules (b)) and the equality is @prp-ordered-field-halves (b).

*Multiples.* If \( c = 0 \), then \( (c \, a_n) \) is the constant sequence \( 0 \) (@prp-ring-algebra (b)), Cauchy by (a). If \( c \ne 0 \), then \( \abs{c} > 0 \) (@prp-absolute-value-ordered-field (a)), so \( \varepsilon/\abs{c} \in F_{>0} \) (@prp-reciprocal-order, (O4)); choose \( N \) (depending on \( \varepsilon \) and \( c \)) with \( \abs{a_m - a_n} < \varepsilon/\abs{c} \) for all \( m, n \ge N \). For such \( m, n \),
\[
\abs{c \, a_m - c \, a_n} = \abs{c (a_m - a_n)} = \abs{c} \, \abs{a_m - a_n} < \abs{c} \cdot \frac{\varepsilon}{\abs{c}} = \varepsilon ,
\]
by distributivity (F9) and @prp-ring-algebra (c), then @prp-absolute-value-ordered-field (b) and @prp-ordered-ring-rules (c); the last equality \( \abs{c} \cdot \varepsilon \abs{c}^{-1} = \varepsilon \) is (F5)–(F8).

*Negatives and differences.* Since \( -a_n = (-1) a_n \) (@prp-ring-algebra (c)), \( (-a_n) \) is the multiple with \( c = -1 \). Then \( a_n - b_n = a_n + (-b_n) \) is the sum of two Cauchy sequences.

(c) By @prp-cauchy-bounded-ordered-field, fix \( A, B \in F_{>0} \) with \( \abs{a_n} \le A \) and \( \abs{b_n} \le B \) for every \( n \in \nN \); they depend on the two sequences only. Now let \( \varepsilon \in F_{>0} \). Then \( \varepsilon/(2A) \) and \( \varepsilon/(2B) \) lie in \( F_{>0} \) (@prp-ordered-field-halves (b), (O4), @prp-reciprocal-order (a)), so there are \( N_1 \) with \( \abs{b_n - b_m} < \varepsilon/(2A) \) for all \( m, n \ge N_1 \), and \( N_2 \) with \( \abs{a_n - a_m} < \varepsilon/(2B) \) for all \( m, n \ge N_2 \). Let \( N \coloneqq \max\{N_1, N_2\} \), depending on \( \varepsilon \), \( A \), \( B \), and let \( m, n \ge N \). Expanding the right side shows
\[
a_n b_n - a_m b_m = a_n (b_n - b_m) + b_m (a_n - a_m) .
\]
By the triangle inequality and \( \abs{xy} = \abs{x}\abs{y} \) (@prp-absolute-value-ordered-field (e), (b)), then @prp-ordered-field-halves (d) applied to \( 0 \le \abs{a_n} \le A \) and to \( 0 \le \abs{b_m} \le B \),
\[
\begin{aligned}
\abs{a_n b_n - a_m b_m} &\le \abs{a_n} \, \abs{b_n - b_m} + \abs{b_m} \, \abs{a_n - a_m} \\
&\le A \abs{b_n - b_m} + B \abs{a_n - a_m} \\
&< A \cdot \frac{\varepsilon}{2A} + B \cdot \frac{\varepsilon}{2B} = \varepsilon ,
\end{aligned}
\]
where the strict step multiplies by \( A > 0 \) and \( B > 0 \) (@prp-ordered-ring-rules (c)) and adds (@prp-ordered-ring-rules (b)); the equality uses \( A \cdot \varepsilon/(2A) = \varepsilon/2 \) (@lem-field-fraction-rules (a), (F5)–(F8)), likewise for \( B \), and @prp-ordered-field-halves (b). So \( (a_n b_n) \) is Cauchy.
:::

The order of choices in (c) is the whole proof: \( A \) and \( B \) are chosen before \( \varepsilon \), from the sequences alone, so that \( \varepsilon/(2A) \) is one fixed tolerance. Exercise C3 shows what goes wrong when the bound is skipped.

::: {.remark}
In Chapter 5, \( \nR \) is a set of classes of Cauchy sequences in \( \nQ \), and the sum and product of two classes are the classes of the termwise sum and product. Clauses (b) and (c) with \( F = \nQ \) are exactly what makes these termwise operations stay inside the set of Cauchy sequences.
:::

## The sign of a Cauchy sequence that is not null

A null sequence is the Cauchy analogue of \( 0 \). Chapter 5 must decide, for each Cauchy sequence of rationals that is not null, whether it represents a positive or a negative number, and it needs an inverse for it. Both rest on one fact: such a sequence eventually keeps one sign, at a definite distance from \( 0 \).

::: {#thm-cauchy-not-null-sign}
[The Sign of a Non-Null Cauchy Sequence]

Let \( (a_n) \) be a Cauchy sequence in \( F \) that is not null. Then there are \( c \in F_{>0} \) and \( N \in \nN \) such that either
\[
a_n \ge c \ \text{ for every } n \ge N , \qquad \text{or} \qquad a_n \le -c \ \text{ for every } n \ge N .
\]
The two alternatives do not both hold.
:::

*Try it first (ten minutes): write "\( (a_n) \) is not null" in symbols. Which \( \varepsilon \) does it hand you, and what does the Cauchy condition do with it?*

::: {.idea}
"Not null" is the negation of @def-null-sequence-ordered-field:
\[
\exists \varepsilon \in F_{>0} \ \ \forall N \in \nN \ \ \exists n \in \nN \ \ \bigl( n \ge N \wedge \abs{a_n} \ge \varepsilon \bigr) .
\]
The obvious attempt reads this as "\( \abs{a_n} \ge \varepsilon \) for all large \( n \)", and that is not what it says: it promises, beyond each threshold, **one** term at least \( \varepsilon \) from \( 0 \), and between such terms others might come near \( 0 \) or change sign. The Cauchy condition is what forbids that wandering. So **fix the bad \( \varepsilon \)** and keep it for the rest of the proof. Ask the Cauchy condition for a threshold \( N_0 \) with tolerance \( \varepsilon/2 \), and only then ask the negation for one term \( a_{n_0} \), beyond \( N_0 \), with \( \abs{a_{n_0}} \ge \varepsilon \). Every later term is within \( \varepsilon/2 \) of \( a_{n_0} \), so it has the sign of \( a_{n_0} \) and size at least \( \varepsilon/2 \). *Before reading on: where is \( n_0 \ge N_0 \) used?*
:::

::: {.proof}
Since \( (a_n) \) is not null, the negation of @def-null-sequence-ordered-field holds. Moving \( \neg \) inward by @fd1:prp-bounded-quantifier-negation (a), (b), @fd1:prp-quantifier-negation (a) and @fd1:prp-negated-implication, and reading \( \neg(\abs{a_n - 0} < \varepsilon) \) as \( \abs{a_n} \ge \varepsilon \) by (O1), it says: there is \( \varepsilon \in F_{>0} \) such that for every \( N \in \nN \) some \( n \ge N \) has \( \abs{a_n} \ge \varepsilon \). Fix such an \( \varepsilon \).

By @prp-ordered-field-halves (b), \( \varepsilon/2 \in F_{>0} \). Since \( (a_n) \) is Cauchy, there is \( N_0 \in \nN \) (depending only on the sequence, through \( \varepsilon \)) with
\[
\abs{a_m - a_n} < \frac{\varepsilon}{2} \quad \text{for all } m, n \ge N_0 .
\]
Applying the negation with \( N \coloneqq N_0 \) gives \( n_0 \in \nN \) with \( n_0 \ge N_0 \) and \( \abs{a_{n_0}} \ge \varepsilon \). By @def-absolute-value-ordered-field, either \( a_{n_0} \ge 0 \) and \( a_{n_0} = \abs{a_{n_0}} \ge \varepsilon \), or \( a_{n_0} < 0 \) and \( -a_{n_0} \ge \varepsilon \), that is, \( a_{n_0} \le -\varepsilon \) (@prp-ordered-ring-rules (a)).

Let \( n \ge N_0 \). Since both \( n \) and \( n_0 \) are \( \ge N_0 \), \( \abs{a_n - a_{n_0}} < \varepsilon/2 \), that is, \( -\varepsilon/2 < a_n - a_{n_0} < \varepsilon/2 \) (@prp-absolute-value-ordered-field (d)).

*Case 1: \( a_{n_0} \ge \varepsilon \).* Adding \( a_{n_0} \) to the left inequality (@prp-ordered-ring-rules (b)), \( a_n > a_{n_0} - \varepsilon/2 \ge \varepsilon - \varepsilon/2 = \varepsilon/2 \), where the last equality is @prp-ordered-field-halves (b).

*Case 2: \( a_{n_0} \le -\varepsilon \).* Adding \( a_{n_0} \) to the right inequality, \( a_n < a_{n_0} + \varepsilon/2 \le -\varepsilon + \varepsilon/2 = -\varepsilon/2 \).

Let \( c \coloneqq \varepsilon/2 \) and \( N \coloneqq N_0 \); both depend only on \( (a_n) \). In Case 1, \( a_n \ge c \) for every \( n \ge N \); in Case 2, \( a_n \le -c \) for every \( n \ge N \).

Finally, both alternatives cannot hold, even with different constants and thresholds: if \( a_n \ge c \) for \( n \ge N \) and \( a_n \le -c' \) for \( n \ge N' \), with \( c, c' \in F_{>0} \), then \( n \coloneqq \max\{N, N'\} \) gives \( 0 < c \le a_n \le -c' < 0 \), against (O1). This proves the theorem.
:::

The answer to the prompt: \( n_0 \ge N_0 \) is used once, to apply the Cauchy estimate to the pair \( n, n_0 \). Had we taken \( n_0 \) from the negation first and \( N_0 \) afterwards, \( n_0 \) might lie below \( N_0 \), and the term \( a_{n_0} \) would say nothing about the tail.

Both hypotheses are needed; the witnesses are in \( \nQ \).

- *Not null.* The sequence \( (1/(n + 1)) \) is Cauchy (the examples after @def-cauchy-sequence-ordered-field) and null. For any \( c \in \nQ_{>0} \) and any \( N \), @cor-rationals-archimedean-epsilon gives an index \( n \ge N \) with \( 0 < 1/(n + 1) < c \), so neither alternative holds.
- *Cauchy.* The sequence \( ((-1)^n) \) is not null, since \( \abs{(-1)^n} = 1 \ge 1 \) for every \( n \). Its terms alternate between \( 1 \) and \( -1 \), so neither alternative holds for any \( c > 0 \) and \( N \): \( a_N \) and \( a_{N+1} \) have opposite signs.

## Sign stability and reciprocals

Two smaller results complete the toolkit: the sign found by @thm-cauchy-not-null-sign survives a null change of the sequence, and a sequence that stays away from \( 0 \) can be inverted.

::: {#prp-sign-stable-ordered-field}
[Sign Stability under Null Differences]

Let \( (a_n) \) and \( (b_n) \) be sequences in \( F \) such that \( (a_n - b_n) \) is null. If \( c \in F_{>0} \), \( N \in \nN \), and \( a_n \ge c \) for every \( n \ge N \), then there is \( N' \in \nN \) with \( b_n \ge c/2 \) for every \( n \ge N' \).
:::

::: {.proof}
Since \( c/2 \in F_{>0} \) (@prp-ordered-field-halves (b)) and \( (a_n - b_n) \) is null, there is \( N_1 \) (depending on \( c \)) with \( \abs{a_n - b_n} < c/2 \) for every \( n \ge N_1 \). Let \( N' \coloneqq \max\{N, N_1\} \), which depends on \( c \) and \( N \), and \( n \ge N' \). Then \( a_n - b_n < c/2 \) (@prp-absolute-value-ordered-field (c)), so
\[
b_n > a_n - \frac{c}{2} \ge c - \frac{c}{2} = \frac{c}{2}
\]
by @prp-ordered-ring-rules (a), (b) and @prp-ordered-field-halves (b). In particular \( b_n \ge c/2 \).
:::

Neither sequence needs to be Cauchy here. In Chapter 5, two Cauchy sequences with null difference represent the same real number, and this proposition is what shows that "represented by a sequence eventually \( \ge c \) for some \( c > 0 \)" does not depend on the representative chosen.

::: {#prp-cauchy-reciprocal-ordered-field}
[Reciprocals of Cauchy Sequences]

Let \( (a_n) \) be a Cauchy sequence in \( F \), and let \( c \in F_{>0} \) and \( N \in \nN \) be such that \( \abs{a_n} \ge c \) for every \( n \ge N \). Define
\[
b_n \coloneqq \begin{cases} 1/a_n & \text{if } n \ge N , \\ 1 & \text{if } n < N . \end{cases}
\]
Then \( (b_n) \) is a Cauchy sequence in \( F \), and \( a_n b_n = 1 \) for every \( n \ge N \).
:::

::: {.idea}
For \( n \ge N \), \( a_n \ne 0 \), so \( b_n \) is defined. The difference of reciprocals is \( (a_m - a_n)/(a_n a_m) \); its numerator can be made small, and the denominator is at least \( c^2 \) in absolute value. So \( \abs{b_n - b_m} \le \abs{a_m - a_n}/c^2 \), and the tolerance \( c^2 \varepsilon \) for \( (a_n) \) gives the tolerance \( \varepsilon \) for \( (b_n) \).
:::

::: {.proof}
For \( n \ge N \), \( \abs{a_n} \ge c > 0 \), so \( a_n \ne 0 \) (@prp-absolute-value-ordered-field (a)), and \( b_n = a_n^{-1} \) is defined, with \( a_n b_n = 1 \). For \( m, n \ge N \), @lem-field-fraction-rules (c) gives
\[
b_n - b_m = \frac{1}{a_n} - \frac{1}{a_m} = \frac{a_m - a_n}{a_n a_m} .
\]
By @prp-absolute-value-ordered-field (b), \( \abs{b_n - b_m} = \abs{a_m - a_n} \cdot \bigl(1/(\abs{a_n} \, \abs{a_m})\bigr) \). From \( 0 < c \le \abs{a_n} \) and \( 0 < c \le \abs{a_m} \), @prp-ordered-field-halves (d) gives \( c^2 \le \abs{a_n} \, \abs{a_m} \), and then @prp-ordered-field-halves (c) gives \( 1/(\abs{a_n} \, \abs{a_m}) \le 1/c^2 \). As \( 1/(\abs{a_n} \, \abs{a_m}) > 0 \) (@prp-reciprocal-order (a)), @prp-ordered-field-halves (d) with \( 0 \le \abs{a_m - a_n} \le \abs{a_m - a_n} \) gives
\[
\abs{b_n - b_m} \le \frac{\abs{a_m - a_n}}{c^2} \quad \text{for all } m, n \ge N .
\]
Now let \( \varepsilon \in F_{>0} \). Then \( c^2 \varepsilon \in F_{>0} \) by (O4), so there is \( N_1 \) (depending on \( \varepsilon \) and \( c \)) with \( \abs{a_m - a_n} < c^2 \varepsilon \) for all \( m, n \ge N_1 \). Let \( N' \coloneqq \max\{N, N_1\} \). For \( m, n \ge N' \), multiplying by \( 1/c^2 > 0 \) (@prp-reciprocal-order (a), @prp-ordered-ring-rules (c)),
\[
\abs{b_n - b_m} \le \frac{\abs{a_m - a_n}}{c^2} < \frac{c^2 \varepsilon}{c^2} = \varepsilon .
\]
So \( (b_n) \) is Cauchy. The values \( b_n = 1 \) for \( n < N \) play no part; any values would do, by the tail-change remark after @def-cauchy-sequence-ordered-field.
:::

The hypothesis "\( \abs{a_n} \ge c \)" cannot be weakened to "\( a_n \ne 0 \)". In \( \nQ \), \( a_n = 1/(n + 1) \) is Cauchy and never \( 0 \), but \( 1/a_n = n + 1 \) is not bounded (for each \( M \in \nQ_{>0} \), @thm-rationals-archimedean gives an \( n \) with \( n + 1 > M \)), so it is not Cauchy, by @prp-cauchy-bounded-ordered-field. Combined with @thm-cauchy-not-null-sign, which supplies \( c \) and \( N \) for every Cauchy sequence that is not null, this proposition is how Chapter 5 inverts a non-zero real number.

## Small steps do not make a Cauchy sequence

The commonest wrong proof that a sequence is Cauchy looks only at neighboring terms.

::: {.warning}
"If \( a_{n+1} - a_n \to 0 \), then \( (a_n) \) is Cauchy" is **false**. The next example gives a sequence of rationals whose steps shrink to \( 0 \) and whose terms do not settle down at all.
:::

::: {#exm-consecutive-differences-not-cauchy}
[Shrinking Steps, Terms That Do Not Settle]

Here is an argument for the false claim in the warning.

"Let \( \varepsilon \in F_{>0} \). Since \( a_{n+1} - a_n \to 0 \), choose \( N \) with \( \abs{a_{k+1} - a_k} < \varepsilon \) for every \( k \ge N \). Let \( m > n \ge N \). Then \( a_m - a_n \) is the sum of the consecutive differences \( a_{k+1} - a_k \) for \( k = n, \dots, m - 1 \), and each of them is smaller than \( \varepsilon \) in absolute value. So \( \abs{a_m - a_n} < \varepsilon \), and \( (a_n) \) is Cauchy."

In \( \nQ \), let \( H_0 \coloneqq 0 \) and \( H_{n+1} \coloneqq H_n + 1/(n + 1) \) for \( n \in \nN \). Show that \( H_{n+1} - H_n \to 0 \), that \( H_{2n} - H_n \ge 1/2 \) for every \( n \ge 1 \), and that \( (H_n) \) is not Cauchy. Find the line of the argument that fails.
:::

::: {.solution}
*The sequence.* By @fd2:thm-recursion (read on \( \nN = \omega \) as @thm-omega-recursion, by @cor-omega-identification (b)), with \( X = \nQ \), starting value \( 0 \) and \( g(n, s) \coloneqq s + 1/(n + 1) \), there is exactly one sequence \( (H_n) \) in \( \nQ \) with \( H_0 = 0 \) and \( H_{n+1} = H_n + 1/(n + 1) \). Its first terms are \( 0, 1, 3/2, 11/6, 25/12 \).

*Shrinking steps.* \( H_{n+1} - H_n = 1/(n + 1) \), and \( (1/(n + 1)) \) is null in \( \nQ \) (@exm-first-sequences-ordered-field).

*Long stretches.* Fix \( n \ge 1 \). We show, by @fd1:ax-induction on \( k \) (through @cor-omega-identification (b)), that
\[
H_{n+k} - H_n \ge \frac{k}{n + k} \quad \text{for every } k \in \nN .
\]
Base \( P(0) \): both sides are \( 0 \). Step: assume it for \( k \). Since \( n + k \ge 1 \), we have \( 0 < n + k < n + k + 1 \), so \( 0 < 1/(n + k + 1) < 1/(n + k) \) (@prp-reciprocal-order (b)). With \( 0 \le k \le k \), @prp-ordered-field-halves (d) gives \( k/(n + k + 1) \le k/(n + k) \). Hence, by the induction hypothesis, transitivity (@prp-ordered-ring-rules (i)) and adding \( 1/(n + k + 1) \) to both sides (@prp-ordered-ring-rules (b)),
\[
\begin{aligned}
H_{n+k+1} - H_n &= (H_{n+k} - H_n) + \frac{1}{n + k + 1} \\
&\ge \frac{k}{n + k + 1} + \frac{1}{n + k + 1} = \frac{k + 1}{n + k + 1} .
\end{aligned}
\]
Taking \( k = n \) gives \( H_{2n} - H_n \ge n/(2n) = 1/2 \). (Directly: each of the \( n \) terms \( 1/(n + 1), \dots, 1/(2n) \) is at least \( 1/(2n) \).)

*Not Cauchy.* We prove the negation displayed after @def-cauchy-sequence-ordered-field with \( \varepsilon = 1/2 \). Let \( N \in \nN \), and put \( n \coloneqq N + 1 \) and \( m \coloneqq 2n \). Then \( m, n \ge N \), \( n \ge 1 \), and \( \abs{H_m - H_n} = H_{2n} - H_n \ge 1/2 \). So no threshold works for the tolerance \( 1/2 \).

*The failing line.* "Each of them is smaller than \( \varepsilon \) … so \( \abs{a_m - a_n} < \varepsilon \)." A sum of \( m - n \) terms, each of absolute value below \( \varepsilon \), is only below \( (m - n) \varepsilon \) (triangle inequality, @prp-absolute-value-ordered-field (e), applied \( m - n - 1 \) times). The number of summands \( m - n \) is not fixed: \( m \) is chosen **after** \( N \), and the definition allows it to be as far beyond \( n \) as we like. To repair the line one would need each step below \( \varepsilon/(m - n) \), a tolerance that depends on \( m \) and \( n \); no single \( N \) is promised for it. For \( (H_n) \), with \( n = N + 1 \) and \( m = 2n \), the \( n \) steps are each below \( 1/n \le 1 \), and their sum is at least \( 1/2 \).
:::

Section 4.6 goes further: its Exercise B2 shows \( H_{2^k} \ge 1 + k/2 \) for every \( k \in \nN \), so \( (H_n) \) even grows without bound.

## Exercises

### A. Check your understanding

::: {#exr-cauchy-sequences-a1}
[A1]

These questions are about @thm-cauchy-not-null-sign and its proof.

::: {.enumerate options="label=(\alph*)"}
1. Write "\( (a_n) \) is not null" in symbols, with every quantifier and its domain.
2. The proof asks the Cauchy condition for the tolerance \( \varepsilon/2 \). Why not \( \varepsilon \) itself?
3. Where is the inequality \( n_0 \ge N_0 \) used?
4. Run the proof in \( \nQ \) on \( a_n = 1/(n + 1) - 1 \) with \( \varepsilon = 1/2 \): check that this \( \varepsilon \) witnesses "not null", give the least \( N_0 \) that the Cauchy condition with tolerance \( 1/4 \) allows, choose \( n_0 \), and state the \( c \) and \( N \) the proof produces.
5. State the idea of the proof in two sentences.
:::
:::

::: {.solution}
(a) \( \exists \varepsilon \in F_{>0} \ \forall N \in \nN \ \exists n \in \nN \ (n \ge N \wedge \abs{a_n} \ge \varepsilon) \): one tolerance and, beyond every threshold, some term at least that far from \( 0 \).

(b) With tolerance \( \varepsilon \), Case 1 would give only \( a_n > a_{n_0} - \varepsilon \ge \varepsilon - \varepsilon = 0 \): every later term is positive, but no positive \( c \) with \( a_n \ge c \) comes out, and the terms might still approach \( 0 \). Any tolerance strictly smaller than \( \varepsilon \) leaves a positive margin; \( \varepsilon/2 \) is the simplest.

(c) In the line "since both \( n \) and \( n_0 \) are \( \ge N_0 \), \( \abs{a_n - a_{n_0}} < \varepsilon/2 \)": the Cauchy estimate holds only for pairs of indices beyond \( N_0 \). It is the reason \( N_0 \) is chosen first and the negation is applied **at** \( N_0 \).

(d) Here \( \abs{a_n} = 1 - 1/(n + 1) = n/(n + 1) \), which is \( 0 \) at \( n = 0 \) and at least \( 1/2 \) for every \( n \ge 1 \) (as \( 2n \ge n + 1 \)). So beyond any \( N \) the index \( n = N + 1 \) has \( \abs{a_n} \ge 1/2 \): \( \varepsilon = 1/2 \) witnesses "not null". Next, \( \abs{a_m - a_n} = \abs{1/(m + 1) - 1/(n + 1)} \). For \( m, n \ge 3 \), both reciprocals lie in \( (0, 1/4] \), so their difference is below \( 1/4 \), as in the examples after @def-cauchy-sequence-ordered-field. For \( N_0 = 2 \) the pair \( m = 2 \), \( n = 11 \) gives \( 1/3 - 1/12 = 1/4 \not< 1/4 \). So the least \( N_0 \) is \( 3 \). Take \( n_0 = 3 \ge N_0 \): \( a_3 = -3/4 \), \( \abs{a_3} = 3/4 \ge 1/2 \), Case 2. The proof gives \( a_n < a_3 + 1/4 = -1/2 \le -1/4 \) for \( n \ge 3 \), and it states the result as \( c = \varepsilon/2 = 1/4 \), \( N = 3 \): \( a_n \le -1/4 \) for every \( n \ge 3 \). (\( n_0 = 0 \) is not allowed: it is below \( N_0 \), and \( \abs{a_0} = 0 < 1/2 \).)

(e) "Not null" provides one tolerance \( \varepsilon \) and, beyond any threshold, a term at least \( \varepsilon \) from \( 0 \). Taking the threshold from the Cauchy condition with \( \varepsilon/2 \) first, every later term stays within \( \varepsilon/2 \) of that one term, so it keeps its sign and stays at least \( \varepsilon/2 \) from \( 0 \).
:::

### B. Practice

::: {#exr-cauchy-sequences-b1}
[B1]

Determine which of the following sequences in \( \nQ \) are Cauchy. Justify your answers, and for the first one work directly from @def-cauchy-sequence-ordered-field.

::: {.enumerate options="label=(\alph*)"}
1. \( a_n = (n + 1)/(n + 2) \).
2. \( a_n = (-1)^n \).
3. \( a_n = n \).
:::
:::

::: {.solution}
(a) Cauchy. For every \( k \in \nN \), \( (k + 1)/(k + 2) = 1 - 1/(k + 2) \), so \( \abs{a_m - a_n} = \abs{1/(n + 2) - 1/(m + 2)} \). Let \( \varepsilon \in \nQ_{>0} \), and use @cor-rationals-archimedean-epsilon to choose \( N \in \nZ_{>0} \) with \( 1/N < \varepsilon \). For \( m, n \ge N \), both \( 1/(m + 2) \) and \( 1/(n + 2) \) lie in \( (0, 1/N) \), since \( m + 2, n + 2 > N \) (@prp-reciprocal-order (b)). Two elements of \( (0, 1/N) \) differ by less than \( 1/N \) (as in the examples after the definition), so \( \abs{a_m - a_n} < 1/N < \varepsilon \).

(b) Not Cauchy. Take \( \varepsilon = 1 \). For any \( N \), the indices \( N \) and \( N + 1 \) have \( a_{N+1} = -a_N \) and \( \abs{a_N} = 1 \), so \( \abs{a_N - a_{N+1}} = \abs{2 a_N} = 2 \ge 1 \).

(c) Not Cauchy. If it were, it would be bounded (@prp-cauchy-bounded-ordered-field): \( \abs{n} \le M \) for some \( M \in \nQ_{>0} \) and every \( n \). By @thm-rationals-archimedean there is \( n \in \nN \) with \( M < n = \abs{n} \), a contradiction. (Archimedes is used here; in the non-Archimedean field \( \nQ(t) \) of Section 4.2 the sequence \( (n \cdot 1) \) is bounded, by \( t \), and the boundedness argument says nothing.)
:::

::: {#exr-cauchy-sequences-b2}
[B2]

Let \( (a_n) \) and \( (b_n) \) be Cauchy sequences in \( F \). Prove directly from @def-cauchy-sequence-ordered-field that \( (a_n - b_n) \) is Cauchy, naming the rule behind each step.
:::

::: {.solution}
Let \( \varepsilon \in F_{>0} \). By @prp-ordered-field-halves (b), \( \varepsilon/2 \in F_{>0} \). Since \( (a_n) \) is Cauchy, choose \( N_1 \) with \( \abs{a_m - a_n} < \varepsilon/2 \) for all \( m, n \ge N_1 \); since \( (b_n) \) is Cauchy, choose \( N_2 \) with \( \abs{b_m - b_n} < \varepsilon/2 \) for all \( m, n \ge N_2 \). Let \( N \coloneqq \max\{N_1, N_2\} \) (a maximum of two natural numbers; it depends only on \( \varepsilon \)). Let \( m, n \ge N \); then \( m, n \ge N_1 \) and \( m, n \ge N_2 \). By the ring rules (@prp-ring-algebra),
\[
(a_m - b_m) - (a_n - b_n) = (a_m - a_n) + \bigl(-(b_m - b_n)\bigr) .
\]
By the triangle inequality (@prp-absolute-value-ordered-field (e)) and \( \abs{-x} = \abs{x} \) (@prp-absolute-value-ordered-field (b)),
\[
\abs{(a_m - b_m) - (a_n - b_n)} \le \abs{a_m - a_n} + \abs{b_m - b_n} < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon ,
\]
adding strict inequalities by @prp-ordered-ring-rules (b) and using @prp-ordered-field-halves (b) for the equality. Since \( \varepsilon \) was arbitrary, \( (a_n - b_n) \) is Cauchy.
:::

::: {#exr-cauchy-sequences-b3}
[B3]

Let \( a_n = 2 - 1/(n + 1) \) in \( \nQ \). Show that \( (a_n) \) is Cauchy and not null, and find \( c \in \nQ_{>0} \) and \( N \in \nN \) as in @thm-cauchy-not-null-sign. Then run the proof of the theorem with \( \varepsilon = 1 \) and the least admissible \( N_0 \): which \( c \) and \( N \) does it produce?
:::

::: {.solution}
*Cauchy.* \( (a_n) \) is the difference of the constant sequence \( 2 \) and the Cauchy sequence \( (1/(n + 1)) \) (examples after @def-cauchy-sequence-ordered-field), so it is Cauchy by @thm-cauchy-algebra-ordered-field (a), (b).

*Not null, and \( c \), \( N \) directly.* For every \( n \), \( 0 < 1/(n + 1) \le 1 \), so \( a_n \ge 1 \). Then \( \abs{a_n} \ge 1 \) for every \( n \), so \( \varepsilon = 1 \) witnesses "not null", and \( c = 1 \), \( N = 0 \) satisfy the first alternative. (Any smaller positive \( c \), for instance \( c = 1/2 \), works with \( N = 0 \) as well.)

*The proof run.* With \( \varepsilon = 1 \), the Cauchy condition is asked for tolerance \( 1/2 \). Here \( \abs{a_m - a_n} = \abs{1/(n + 1) - 1/(m + 1)} \); for \( m, n \ge 1 \) both reciprocals lie in \( (0, 1/2] \), so the difference is below \( 1/2 \), while \( N_0 = 0 \) fails (\( m = 0 \), \( n = 1 \): \( 1 - 1/2 = 1/2 \not< 1/2 \)). So \( N_0 = 1 \). Take \( n_0 = 1 \): \( a_1 = 3/2 \ge 1 \), Case 1. The proof gives \( c = 1/2 \), \( N = 1 \): \( a_n > 3/2 - 1/2 = 1 \ge 1/2 \) for every \( n \ge 1 \).
:::

### C. Going deeper

::: {#exr-cauchy-sequences-c1}
[C1]

Let \( (a_n) \) be a Cauchy sequence in \( F \) and \( (b_n) \) a sequence in \( F \) such that \( (a_n - b_n) \) is null. Prove that \( (b_n) \) is Cauchy.

Here is the beginning of a proof. *Name the move, then complete it.*

"Let \( \varepsilon \in F_{>0} \). For all \( m, n \in \nN \), the triangle inequality (@prp-absolute-value-ordered-field (e)), applied twice, gives
\[
\abs{b_n - b_m} \le \abs{b_n - a_n} + \abs{a_n - a_m} + \abs{a_m - b_m} .
\]
…"
:::

::: {.solution}
*The move* is **split \( \varepsilon \)**, now into three parts, one for each term on the right: two come from the null difference, one from the Cauchy condition.

*Completion.* Let \( 3 \coloneqq 1 + 1 + 1 = 3 \cdot 1_F \); then \( 3 > 0 \) (@prp-naturals-in-ordered-field (b)), so \( \varepsilon/3 \in F_{>0} \) (@prp-reciprocal-order (a), (O4)), and \( \varepsilon/3 + \varepsilon/3 + \varepsilon/3 = 3 \cdot (\varepsilon/3) = \varepsilon \): by (F5)–(F9), with \( 3 \ne 0 \). Since \( (a_n - b_n) \) is null, choose \( N_1 \) with \( \abs{a_n - b_n} < \varepsilon/3 \) for every \( n \ge N_1 \). Since \( (a_n) \) is Cauchy, choose \( N_2 \) with \( \abs{a_n - a_m} < \varepsilon/3 \) for all \( m, n \ge N_2 \). Let \( N \coloneqq \max\{N_1, N_2\} \), which depends only on \( \varepsilon \). For \( m, n \ge N \), using \( \abs{b_n - a_n} = \abs{a_n - b_n} \) (@prp-absolute-value-ordered-field (b)),
\[
\abs{b_n - b_m} < \frac{\varepsilon}{3} + \frac{\varepsilon}{3} + \frac{\varepsilon}{3} = \varepsilon ,
\]
adding three strict inequalities (@prp-ordered-ring-rules (b)). So \( (b_n) \) is Cauchy.

The split \( \varepsilon/4 \), \( \varepsilon/2 \), \( \varepsilon/4 \), which needs only halving, works as well.
:::

::: {#exr-cauchy-sequences-c2}
[C2: Exit check: the sign theorem]

Let \( (a_n) \) be a Cauchy sequence in an ordered field \( F \) that is not null. Prove that there are \( c \in F_{>0} \) and \( N \in \nN \) such that either \( a_n \ge c \) for every \( n \ge N \), or \( a_n \le -c \) for every \( n \ge N \).
:::

::: {.solution}
"Null" means \( \forall \varepsilon \in F_{>0} \ \exists N \in \nN \ \forall n \in \nN \ (n \ge N \Rightarrow \abs{a_n} < \varepsilon) \). Its negation (@fd1:prp-bounded-quantifier-negation, @fd1:prp-quantifier-negation (a), @fd1:prp-negated-implication, then (O1)) is
\[
\exists \varepsilon \in F_{>0} \ \ \forall N \in \nN \ \ \exists n \in \nN \ \ \bigl( n \ge N \wedge \abs{a_n} \ge \varepsilon \bigr) .
\]
Fix such an \( \varepsilon \); it stays fixed from here on.

Apply the Cauchy condition with the tolerance \( \varepsilon/2 \in F_{>0} \) (@prp-ordered-field-halves (b)): there is \( N_0 \) with \( \abs{a_m - a_n} < \varepsilon/2 \) for all \( m, n \ge N_0 \). Apply the negation at \( N_0 \): there is \( n_0 \ge N_0 \) with \( \abs{a_{n_0}} \ge \varepsilon \). By the definition of \( \abs{\cdot} \), \( a_{n_0} \ge \varepsilon \) or \( a_{n_0} \le -\varepsilon \).

Let \( n \ge N_0 \). As \( n, n_0 \ge N_0 \), \( -\varepsilon/2 < a_n - a_{n_0} < \varepsilon/2 \) (@prp-absolute-value-ordered-field (d)). If \( a_{n_0} \ge \varepsilon \), then \( a_n > a_{n_0} - \varepsilon/2 \ge \varepsilon/2 \). If \( a_{n_0} \le -\varepsilon \), then \( a_n < a_{n_0} + \varepsilon/2 \le -\varepsilon/2 \). With \( c \coloneqq \varepsilon/2 \) and \( N \coloneqq N_0 \), the first case gives \( a_n \ge c \) and the second \( a_n \le -c \), for every \( n \ge N \).

**Marking scheme.** (10 points)
- 2: negates "null" correctly, with the quantifiers in order, and fixes one \( \varepsilon \).
- 2: applies the Cauchy condition with a fixed tolerance \( \delta \) such that \( 0 < \delta < \varepsilon \) (for example \( \delta = \varepsilon/2 \)) to get \( N_0 \).
- 2: obtains \( n_0 \ge N_0 \) with \( \abs{a_{n_0}} \ge \varepsilon \) from the negation applied **at** \( N_0 \).
- 3: derives the one-signed bound (with \( c = \varepsilon - \delta \)) for every \( n \ge N_0 \), in both sign cases.
- 1: names \( c \) and \( N \) and concludes.
Fatal errors (0 for the step): \( n_0 \) chosen before \( N_0 \), or from the negation at a threshold unrelated to \( N_0 \); "\( \abs{a_n} \ge \varepsilon \) for all large \( n \)" asserted from "not null" alone. A complete proof by contradiction (assume neither alternative holds for any \( c \), \( N \), and refute it at \( c = \varepsilon - \delta \), \( N = N_0 \)) maps onto the same 2 + 2 + 2 + 3 + 1.
:::

::: {#exr-cauchy-sequences-c3}
[C3: Find the error]

Here is an argument that the product of two Cauchy sequences \( (a_n) \), \( (b_n) \) in \( F \) is Cauchy.

"For all \( m, n \), \( \abs{a_n b_n - a_m b_m} \le \abs{a_n} \, \abs{b_n - b_m} + \abs{b_m} \, \abs{a_n - a_m} \). Given \( \varepsilon \in F_{>0} \), choose \( N \) such that \( \abs{b_n - b_m} < \varepsilon/(2\abs{a_n}) \) and \( \abs{a_n - a_m} < \varepsilon/(2\abs{b_m}) \) for all \( m, n \ge N \). Then for \( m, n \ge N \), \( \abs{a_n b_n - a_m b_m} < \varepsilon/2 + \varepsilon/2 = \varepsilon \)."

Is the conclusion true? Does the argument prove it? If not, name the line that fails, say why, and repair it.
:::

::: {.solution}
*The conclusion is true:* it is @thm-cauchy-algebra-ordered-field (c).

*The argument does not prove it.* The failing line is "choose \( N \) such that \( \abs{b_n - b_m} < \varepsilon/(2\abs{a_n}) \) … for all \( m, n \ge N \)". The tolerances \( \varepsilon/(2\abs{a_n}) \) and \( \varepsilon/(2\abs{b_m}) \) depend on \( n \) and \( m \), which are introduced **after** \( N \). The definition of Cauchy supplies a threshold for one fixed tolerance \( \varepsilon' \in F_{>0} \), named before the threshold; here the threshold is asked to serve a tolerance that changes with the very indices it controls. This is a witness depending on variables introduced later, entry (N2) of @fd1:exm-not-allowed-catalogue.

*A counterexample to the step.* The step gets one \( N \) for all the tolerances \( \varepsilon/(2\abs{a_n}) \) from their being positive. In \( \nQ \) take the Cauchy sequence \( b_n = 1/(n + 1) \), the never-zero (but unbounded) \( a_n = n + 1 \), and \( \varepsilon = 1 \). For any \( N \), \( n = N \) and \( m = 2N + 1 \) give
\[
\abs{b_n - b_m} = \frac{1}{N + 1} - \frac{1}{2N + 2} = \frac{1}{2(N + 1)} = \frac{\varepsilon}{2\abs{a_n}} ,
\]
which is not smaller: no \( N \) works. Inside the exercise \( (a_n) \) is Cauchy, hence bounded, but the argument never uses that; the repair does.

*Repair.* Fix bounds first: by @prp-cauchy-bounded-ordered-field, choose \( A, B \in F_{>0} \) with \( \abs{a_n} \le A \) and \( \abs{b_n} \le B \) for every \( n \), before \( \varepsilon \) is named. Then the fixed tolerances \( \varepsilon/(2A) \le \varepsilon/(2\abs{a_n}) \) (when \( a_n \ne 0 \)) and \( \varepsilon/(2B) \) give thresholds \( N_1 \), \( N_2 \), and \( N \coloneqq \max\{N_1, N_2\} \) works, as in the proof of @thm-cauchy-algebra-ordered-field (c).
:::

<!-- dependency ledger
def-cauchy-sequence-ordered-field (claim): negation of the definition | fd1:prp-bounded-quantifier-negation, fd1:prp-negated-implication, cited; not(x < e) iff x >= e by (O1)
def-cauchy-sequence-ordered-field (example): two elements of (0, c) differ by less than c | prp-absolute-value-ordered-field (d); inline
def-cauchy-sequence-ordered-field (example): for e = 1/100, N = 101 works for 1/(n + 1) | inline arithmetic; verify/ch04/def-cauchy-sequence-ordered-field.py
def-cauchy-sequence-ordered-field (claim): swapped quantifiers force a_m = a_n for m, n >= N | argument of thm-limit-unique-ordered-field (cited); inline
def-cauchy-sequence-ordered-field (claim): tail change extends to Cauchy | inline, thresholds max{N, N_0}
def-cauchy-sequence-ordered-field (claim): non-example a_{n+2} = a_n | inline
prp-cauchy-bounded-ordered-field (proof): finite maximum of elements of F | fd2:prp-finite-max with F2.5's remark that its proof works in any totally ordered set (F2.5 §03), cited as in prp-convergent-bounded-ordered-field
prp-cauchy-bounded-ordered-field (proof): 1 > 0 in F | prp-ordered-ring-rules (e), cited
thm-cauchy-algebra-ordered-field (proof): identity a_n b_n - a_m b_m = a_n (b_n - b_m) + b_m (a_n - a_m) | prp-ring-algebra (field axioms); verify/ch04/thm-cauchy-algebra-ordered-field.py
thm-cauchy-algebra-ordered-field (proof): -a = (-1) a | prp-ring-algebra (c), cited
thm-cauchy-algebra-ordered-field (proof): c(x - y) = cx - cy; e/(2A) > 0; A * e/(2A) = e/2; |c| * (e/|c|) = e | (F5)-(F9), prp-ring-algebra (c), lem-field-fraction-rules (a), prp-reciprocal-order (a), cited
thm-cauchy-algebra-ordered-field (proof): (a_m + b_m) - (a_n + b_n) = (a_m - a_n) + (b_m - b_n); adding strict inequalities; e/2 + e/2 = e | prp-ring-algebra, prp-ordered-ring-rules (b), prp-ordered-field-halves (b), cited
thm-cauchy-algebra-ordered-field (proof): a constant sequence converges to its value | exm-first-sequences-ordered-field, cited
thm-cauchy-not-null-sign (proof): |a_n - 0| = |a_n| (a - 0 = a) | (F3), (F4) with -0 = 0; inline
thm-cauchy-not-null-sign (proof): e - e/2 = e/2 | prp-ordered-field-halves (b), cited
thm-cauchy-not-null-sign (claim): |(-1)^n| = 1 | induction with prp-absolute-value-ordered-field (b); inline
thm-cauchy-not-null-sign (claim): in Q, some n >= N has 1/(n + 1) < c | cor-rationals-archimedean-epsilon, cited
prp-cauchy-reciprocal-ordered-field (proof): 1/b - 1/d = (d - b)/(bd) | lem-field-fraction-rules (c), cited; verify/ch04/prp-cauchy-reciprocal-ordered-field.py
prp-cauchy-reciprocal-ordered-field (proof): non-strict product bound | prp-ordered-field-halves (d), cited
prp-cauchy-reciprocal-ordered-field (claim): n + 1 is unbounded in Q | thm-rationals-archimedean, cited
exm-consecutive-differences-not-cauchy (example): H defined by recursion | fd2:thm-recursion read on omega (thm-omega-recursion, cor-omega-identification (b)), cited
exm-consecutive-differences-not-cauchy (example): H_{n+k} - H_n >= k/(n + k) by induction on k; first terms 0, 1, 3/2, 11/6, 25/12 | fd1:ax-induction via cor-omega-identification (b), cited; verify/ch04/exm-consecutive-differences-not-cauchy.py
exm-consecutive-differences-not-cauchy (example): k/(n + k + 1) <= k/(n + k) and adding 1/(n + k + 1) | prp-reciprocal-order (b), prp-ordered-field-halves (d), prp-ordered-ring-rules (i), (b), cited
exm-consecutive-differences-not-cauchy (example): sum of m - n terms each below e is below (m - n) e | prp-absolute-value-ordered-field (e) applied repeatedly; inline
exr-cauchy-sequences-a1 (solution): least N_0 = 3 for tolerance 1/4; a_3 = -3/4; pair (2, 11) gives exactly 1/4 | verify/ch04/exr-cauchy-sequences-a1.py
exr-cauchy-sequences-b1 (solution): (k + 1)/(k + 2) = 1 - 1/(k + 2) | field arithmetic; verify/ch04/exr-cauchy-sequences-b1.py
exr-cauchy-sequences-b1 (solution): Q(t) remark: (n * 1) bounded by t | exm-rational-function-field (school fact; formal polynomials in F5.4); remark only, nothing depends on it
exr-cauchy-sequences-b3 (solution): least N_0 = 1 for tolerance 1/2; c = 1/2, N = 1 | verify/ch04/exr-cauchy-sequences-b3.py
exr-cauchy-sequences-c1 (solution): 3 * 1_F > 0 and e/3 + e/3 + e/3 = e | prp-naturals-in-ordered-field (b), (F5)-(F9); inline
exr-cauchy-sequences-c3 (solution): catalogue entry (N2) | fd1:exm-not-allowed-catalogue, cited
exr-cauchy-sequences-c3 (solution): counterexample identity | verify/ch04/exr-cauchy-sequences-c3.py
-->
