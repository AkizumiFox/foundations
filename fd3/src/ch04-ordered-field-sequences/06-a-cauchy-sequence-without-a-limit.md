# A Cauchy Sequence with No Rational Limit

Section 4.5 proved that every convergent sequence is Cauchy (@prp-convergent-cauchy-ordered-field). In \( \nQ \) the converse fails, and the failure sits exactly at the hole Chapter 3 found at \( \sqrt 2 \): no rational squares to \( 2 \) (@thm-no-rational-square-two). This section proves that the rational sequence of Chapter 3 that closes in on that hole (@exm-newton-rationals-sqrt2) is Cauchy in \( \nQ \) and converges to no rational. Chapter 5 starts from this sequence and builds the number it is aiming at. The section ends by listing what the chapter has not proved, and why, in \( \nQ \), it could not have.

Throughout this section the field is \( F = \nQ \): every tolerance \( \varepsilon \) is a positive rational, and "converges" means "converges in \( \nQ \)" (@def-sequence-limit-ordered-field).

## The sequence again

Recall the sequence of @exm-newton-rationals-sqrt2. For \( s \in \nQ_{>0} \) let \( t(s) \coloneqq (s^2 + 2)/(2s) \), the average of \( s \) and \( 2/s \); let \( x_0 \coloneqq 2 \) and \( x_{n+1} \coloneqq t(x_n) \), and let \( e_n \coloneqq x_n^2 - 2 \), the amount by which \( x_n^2 \) overshoots \( 2 \). The first terms are
\[
x_0 = 2 , \quad x_1 = \frac{3}{2} , \quad x_2 = \frac{17}{12} , \quad x_3 = \frac{577}{408} ,
\]
with
\[
e_0 = 2 , \quad e_1 = \frac{1}{4} , \quad e_2 = \frac{1}{144} , \quad e_3 = \frac{1}{166464} .
\]
Chapter 3 proved, for every \( n \in \nN \), the following facts, and we cite them from @exm-newton-rationals-sqrt2 without proving them again:
\[
\begin{aligned}
&x_n \in \nQ_{>0} , \qquad e_n > 0 \ \ (\text{so } x_n^2 > 2) , \\
&e_{n+1} = \frac{e_n^2}{4x_n^2} \le \frac{e_n^2}{8} , \qquad x_n - x_{n+1} = \frac{e_n}{2x_n} > 0 .
\end{aligned}
\]
The second line says two things. The overshoot is roughly squared at each step, so it shrinks very fast; and the terms decrease. Section 4.5 asks for more than decrease: any two late terms must be close. The overshoot \( e_n \) measures how close, because every later term lies between \( 2/x_n \) and \( x_n \), an interval of length \( e_n/x_n \).

For the proof we do not need the true speed of \( e_n \). A crude bound is enough, as long as it can be pushed below every rational tolerance:
\[
e_1 = \frac{1}{4} , \quad e_2 = \frac{1}{144} \le \frac{1}{8} , \quad e_3 = \frac{1}{166464} \le \frac{1}{12} ;
\]
that is, \( e_n \le 1/(4n) \) for \( n = 1, 2, 3 \), and the theorem proves it for every \( n \ge 1 \). Archimedes then turns \( 1/(4n) \) into anything below a given \( \varepsilon \).

## The theorem

::: {#thm-sqrt2-cauchy-no-rational-limit}
[The Newton Sequence Is Cauchy with No Rational Limit]

Let \( (x_n)_{n \in \nN} \) and \( e_n = x_n^2 - 2 \) be as in @exm-newton-rationals-sqrt2. Then \( x_n > 1 \) for every \( n \in \nN \), \( x_m \le x_n \) whenever \( m \ge n \), and \( e_n \le 1/(4n) \) for every \( n \ge 1 \). The sequence \( (x_n) \) is a Cauchy sequence in \( \nQ \), and there is **no** \( L \in \nQ \) with \( x_n \to L \).
:::

The first three clauses are part of the statement, rather than steps hidden in the proof, so that Chapter 5 can cite them.

::: {.idea}
*Cauchy.* This keeps the shape of @exm-method-limit-from-definition, with a second index in place of the limit: bound \( \abs{x_m - x_n} \) by an expression in \( n \) alone, then let Archimedes push it below \( \varepsilon \). For \( m \ge n \), the later term \( x_m \) lies below \( x_n \), since the terms decrease, and above \( 2/x_n \), since \( x_m > 2/x_m \ge 2/x_n \). So \( 0 \le x_n - x_m \le x_n - 2/x_n = e_n/x_n \le e_n \). With \( e_n \le 1/(4n) \), every two terms beyond \( N \) differ by at most \( 1/(4N) \), and Archimedes makes \( 1/N \) smaller than any rational \( \varepsilon \).

*No rational limit.* **Locate the missing limit**: suppose \( x_n \to L \) in \( \nQ \) and find out what \( L \) would have to satisfy. The limit laws turn \( x_n \to L \) into \( x_n^2 \to L^2 \). But \( x_n^2 = 2 + e_n \to 2 \), because \( e_n \) is squeezed between \( 0 \) and \( 1/(4n) \). Limits are unique, so \( L^2 = 2 \), and no rational satisfies that. *Before reading on: which law turns \( x_n \to L \) into \( x_n^2 \to L^2 \), and applied to which two sequences?*
:::

::: {.proof}
We prove six facts, then the two claims. Induction is @fd1:ax-induction, read on \( \nN = \omega \) through @cor-omega-identification (b).

*(i), (ii), (iv) in part: cited.* By @exm-newton-rationals-sqrt2, for every \( n \in \nN \): (i) \( x_n \in \nQ_{>0} \), \( e_n > 0 \) and \( x_n^2 > 2 \); (ii) \( e_{n+1} = e_n^2/(4x_n^2) \le e_n^2/8 \); and \( x_{n+1} < x_n \).

*(iii) \( x_n > 1 \).* Suppose \( x_n \le 1 \). Since \( x_n > 0 \) by (i), either \( x_n < 1 \), and then \( x_n^2 < 1 \) by @prp-ordered-ring-rules (g), or \( x_n = 1 \) and \( x_n^2 = 1 \). Either way \( x_n^2 \le 1 < 2 \), a contradiction with \( x_n^2 > 2 \). So \( x_n > 1 \), by totality (@prp-ordered-ring-rules (i)).

*(iv) \( x_m \le x_n \) for \( m \ge n \).* Fix \( n \). By induction on \( k \), \( x_{n+k} \le x_n \) for every \( k \in \nN \): the base \( P(0) \) is \( x_n \le x_n \), and if \( x_{n+k} \le x_n \), then \( x_{n+k+1} < x_{n+k} \le x_n \). Every \( m \ge n \) in \( \nN \) is \( n + k \) for some \( k \in \nN \) (@prp-omega-order-arithmetic (a)), so \( x_m \le x_n \).

*(v) \( e_n \le 1/(4n) \) for \( n \ge 1 \).* By induction on \( k \), for \( P(k) \): \( e_{k+1} \le 1/(4(k + 1)) \). Base \( P(0) \): \( e_1 = 1/4 \). Step: assume \( P(k) \), and let \( n \coloneqq k + 1 \ge 1 \), so \( 0 < e_n \le 1/(4n) \le 1/4 \) (by (i), \( P(k) \), and @prp-ordered-field-halves (c)). Then, by (ii) and @prp-ordered-field-halves (d) (multiplying by the non-negative factors \( e_n/8 \) and \( 1/32 \)),
\[
e_{n+1} \le \frac{e_n \cdot e_n}{8} \le \frac{e_n}{8} \cdot \frac{1}{4} = \frac{e_n}{32} \le \frac{1}{128 n} \le \frac{1}{4(n + 1)} ,
\]
where the last step is @prp-ordered-field-halves (c), since \( 0 < 4n + 4 \le 128 n \) for \( n \ge 1 \). This is \( P(k + 1) \).

*(vi) For \( m \ge n \ge 1 \): \( 0 \le x_n - x_m \le 1/(4n) \).* By (iv), \( x_m \le x_n \), so \( x_n - x_m \ge 0 \). By (i), \( x_m^2 > 2 \); multiplying by \( 1/x_m > 0 \) (@prp-reciprocal-order (a), @prp-ordered-ring-rules (c)) gives \( x_m > 2/x_m \). From \( 0 < x_m \le x_n \), @prp-ordered-field-halves (c) gives \( 1/x_n \le 1/x_m \), so \( 2/x_n \le 2/x_m < x_m \) (@prp-ordered-field-halves (d)). Hence
\[
x_n - x_m \le x_n - \frac{2}{x_n} = \frac{x_n^2 - 2}{x_n} = \frac{e_n}{x_n} \le e_n \le \frac{1}{4n} .
\]
Here \( e_n/x_n \le e_n \) because \( 0 < 1 < x_n \) by (iii), so \( 1/x_n < 1 \) (@prp-reciprocal-order (b)), and \( e_n > 0 \); the last step is (v).

*Cauchy.* Let \( \varepsilon \in \nQ_{>0} \). By @cor-rationals-archimedean-epsilon there is \( N \in \nZ_{>0} \) with \( 1/N < \varepsilon \); it depends only on \( \varepsilon \). Let \( m, n \ge N \), and let \( k \coloneqq \min\{m, n\} \ge N \ge 1 \) and \( l \coloneqq \max\{m, n\} \). By (vi) with the pair \( l \ge k \),
\[
\abs{x_m - x_n} = x_k - x_l \le \frac{1}{4k} \le \frac{1}{4N} \le \frac{1}{N} < \varepsilon ,
\]
where \( 1/(4k) \le 1/(4N) \le 1/N \) is @prp-ordered-field-halves (c) applied to \( N \le 4N \le 4k \). So \( (x_n) \) is Cauchy in \( \nQ \).

*No rational limit.* Suppose, for a contradiction, that \( x_n \to L \) for some \( L \in \nQ \). By the product law, @thm-limit-laws-ordered-field (c), applied with both sequences equal to \( (x_n) \), \( x_n^2 \to L^2 \).

Next, \( (e_n) \) is null. We use the squeeze, @prp-limit-preserves-order-ordered-field (c), with \( N_0 = 1 \), the lower sequence constantly \( 0 \) (which tends to \( 0 \)) and the upper sequence \( (1/(n + 1))_{n \in \nN} \). The upper sequence is defined for every \( n \in \nN \), and it is null in \( \nQ \) by @prp-archimedean-reciprocal, as in @exm-first-sequences-ordered-field. For \( n \ge 1 \) we have \( n + 1 \le 4n \) (as \( 1 \le 3n \)), so by (i), (v) and @prp-ordered-field-halves (c),
\[
0 < e_n \le \frac{1}{4n} \le \frac{1}{n + 1} \qquad (n \ge 1) .
\]
(At \( n = 0 \) the middle term is undefined and \( e_0 = 2 \); the squeeze needs the inequalities only from \( N_0 = 1 \) on.) So \( e_n \to 0 \).

Then \( x_n^2 = 2 + e_n \) for every \( n \), and the sum law, @thm-limit-laws-ordered-field (a), with the constant sequence \( 2 \) gives \( x_n^2 \to 2 + 0 = 2 \). The sequence \( (x_n^2) \) therefore tends to \( L^2 \) and to \( 2 \), and by @thm-limit-unique-ordered-field, \( L^2 = 2 \). This contradicts @thm-no-rational-square-two. Hence no \( L \in \nQ \) has \( x_n \to L \).
:::

The answer to the prompt: the product law, @thm-limit-laws-ordered-field (c), applied to \( a_n = b_n = x_n \). It is the only step that uses the hypothesis \( x_n \to L \); the rest of the second half is about \( e_n \), which we control without any limit, and then uniqueness compares the two limits of \( (x_n^2) \).

Archimedes is used twice, both times in \( \nQ \), where @thm-rationals-archimedean provides it: for the Cauchy threshold, through @cor-rationals-archimedean-epsilon, and for the upper sequence \( (1/(n + 1)) \) of the squeeze, through @prp-archimedean-reciprocal.

::: {.remark}
The sequence is Cauchy and not null, since \( \abs{x_n} = x_n > 1 \) for every \( n \), so @thm-cauchy-not-null-sign applies to it. Its proof, run with \( \varepsilon = 1 \), gives \( c = 1/2 \); directly, \( x_n \ge 1 \) for every \( n \). Chapter 5 turns the class of \( (x_n) \) into a positive real number whose square is \( 2 \).
:::

::: {.warning}
"Cauchy" does not mean "convergent to a limit we have not named yet". In \( \nQ \) there is nothing to name: by @thm-sqrt2-cauchy-no-rational-limit, the statement "every Cauchy sequence of rationals converges in \( \nQ \)" is **false**, not merely unproved. A proof that says "\( (a_n) \) is Cauchy, so let \( a \) be its limit" is wrong in \( \nQ \), whatever it goes on to do.
:::

::: {.check}
Give an upper bound and a positive lower bound for the terms \( x_n \) in \( \nQ \), with reasons.
:::

::: {.solution}
Upper bound \( 2 \): \( x_n \le x_0 = 2 \) for every \( n \), by clause (iv) of the proof with \( n = 0 \). Lower bound \( 1 \): \( x_n > 1 \) for every \( n \), by (iii). The upper bound is attained, at \( x_0 \); the lower bound \( 1 \) is crude (every term also exceeds \( 2/x_1 = 4/3 \), by the argument of (vi), and \( x_0 = 2 > 4/3 \)), but any positive lower bound answers the question.
:::

::: {.check}
For \( \varepsilon = 1/100 \), which \( N \) does the Cauchy half of the proof give, if \( N \) is taken least?
:::

::: {.solution}
The proof takes \( N \in \nZ_{>0} \) with \( 1/N < 1/100 \), that is \( N > 100 \). The least is \( N = 101 \); any \( N \ge 101 \) serves. (Because of the factor \( 4 \) in \( 1/(4N) \), a smaller \( N \) would do, but the proof does not ask for it.)
:::

## What this chapter did not prove

Looking back over the chapter, three familiar tools of real analysis are absent, and their absence is checkable.

- **No result asserts convergence without naming the limit.** Each result of the chapter that concludes \( a_n \to a \) has \( a \) in its hypotheses or in its statement: the examples of Section 4.3 (@exm-first-sequences-ordered-field), the tail-change rules (@prp-tail-change-ordered-field), the limit laws (@thm-limit-laws-ordered-field) and the squeeze (@prp-limit-preserves-order-ordered-field (c)). The results of Section 4.5, about sequences whose limit is unknown, conclude "Cauchy", "bounded", or a sign, never "convergent".
- **No supremum.** No result uses the supremum of a subset of \( F \) (@fd2:def-order-supremum), so nothing here rests on a least upper bound property.
- **No monotone convergence theorem, and no Bolzano–Weierstrass theorem.** Neither is stated or used.

In \( \nQ \) each of the three would fail. A least upper bound property fails by Section 3.3: the set of rationals with square below \( 2 \) is non-empty and bounded above, with no rational supremum. A monotone convergence theorem fails by the sequence of this section: \( (x_n) \) is decreasing (clause (iv) of the proof), bounded (the Quick check above) and Cauchy, and it has no limit in \( \nQ \). And so does Bolzano–Weierstrass, which would give the bounded sequence \( (x_n) \) a subsequence converging in \( \nQ \). Indeed, let \( n_0 < n_1 < n_2 < \cdots \) be indices and suppose \( x_{n_k} \to L \in \nQ \) as \( k \to \infty \). By induction, \( n_k \ge k \) for every \( k \) (if \( n_k \ge k \), then \( n_{k+1} > n_k \ge k \), so \( n_{k+1} \ge k + 1 \)). So for \( k \ge 1 \), \( 0 < e_{n_k} \le 1/(4n_k) \le 1/(4k) \le 1/(k + 1) \), and the argument of the proof, run on the sequence \( (x_{n_k})_{k \in \nN} \), gives \( L^2 = 2 \) again.

The reader who knows real analysis will have met all three as theorems about \( \nR \). They are true there because of an axiom about \( \nR \), completeness, that no ordered field satisfies automatically, and this chapter never assumed it. Chapter 5 builds, from Cauchy sequences of rationals, a field in which every Cauchy sequence converges, and proves that in it every non-empty subset that is bounded above has a supremum: a complete ordered field. Chapter 6 proves that any two complete ordered fields are copies of each other, by exactly one order-preserving field isomorphism. *Analysis on the Real Line*, Chapter 1 takes the axioms of a complete ordered field as its starting point, and its Chapter 2 revisits this chapter's sequences, now in \( \nR \).

## Exercises

### A. Check your understanding

::: {#exr-a-cauchy-sequence-without-a-limit-a1}
[A1]

These questions are about the proof of @thm-sqrt2-cauchy-no-rational-limit.

::: {.enumerate options="label=(\alph*)"}
1. Which result gives \( x_n^2 \to L^2 \) from \( x_n \to L \), applied to which two sequences?
2. Why does the proof need the bound \( e_n \le 1/(4n) \), and not only "\( e_n > 0 \) and \( (e_n) \) is decreasing"?
3. Where is the Archimedean property used?
4. Check fact (vi) at \( n = 2 \), \( m = 3 \): compute \( x_2 - x_3 \) and compare it with \( e_2/x_2 \), \( e_2 \) and \( 1/(4 \cdot 2) \).
5. State the idea of the proof that \( (x_n) \) has no rational limit, in two sentences.
:::
:::

::: {.solution}
(a) The product law, @thm-limit-laws-ordered-field (c), with \( a_n = b_n = x_n \) and \( a = b = L \).

(b) The proof must show that \( (e_n) \) is null, that is, below every rational \( \varepsilon \) from some index on. A sequence can be positive and decreasing without being null: \( 1 + 1/(n + 1) \) decreases and stays above \( 1 \). The bound \( 1/(4n) \le 1/(n + 1) \) ties \( e_n \) to a sequence known to be null, and the same bound gives the Cauchy threshold.

(c) Twice: for the Cauchy threshold, by @cor-rationals-archimedean-epsilon (an \( N \) with \( 1/N < \varepsilon \)); and for the upper sequence \( (1/(n + 1)) \) of the squeeze, null by @prp-archimedean-reciprocal.

(d) \( x_2 - x_3 = 17/12 - 577/408 = (17 \cdot 34 - 577)/408 = (578 - 577)/408 = 1/408 \). Next, \( e_2/x_2 = (1/144) \cdot (12/17) = 1/204 \). So
\[
\frac{1}{408} \le \frac{1}{204} \le \frac{1}{144} \le \frac{1}{8} ,
\]
which is the chain \( x_2 - x_3 \le e_2/x_2 \le e_2 \le 1/(4 \cdot 2) \) of (vi).

(e) A rational limit \( L \) of \( (x_n) \) would make \( x_n^2 \) tend to \( L^2 \), by the product law. But \( x_n^2 = 2 + e_n \) tends to \( 2 \), since \( e_n \) is squeezed to \( 0 \), so uniqueness of limits gives \( L^2 = 2 \), which no rational satisfies.
:::

### B. Practice

::: {#exr-a-cauchy-sequence-without-a-limit-b1}
[B1]

With \( (x_n) \) as in @thm-sqrt2-cauchy-no-rational-limit, prove that the sequence \( (x_n - 2/x_n) \) is null in \( \nQ \), that \( (2/x_n) \) is Cauchy in \( \nQ \), and that \( (2/x_n) \) has no limit in \( \nQ \).
:::

::: {.solution}
*Null.* For every \( n \), \( x_n - 2/x_n = (x_n^2 - 2)/x_n = e_n/x_n \), and as in step (vi) of the proof, \( 0 < e_n/x_n \le e_n \le 1/(4n) \le 1/(n + 1) \) for \( n \ge 1 \) (using \( x_n > 1 \) and \( e_n \le 1/(4n) \) from the theorem, and \( e_n > 0 \) from @exm-newton-rationals-sqrt2 (i)). By the squeeze (@prp-limit-preserves-order-ordered-field (c)) with \( N_0 = 1 \), lower sequence \( 0 \) and upper sequence \( (1/(n + 1)) \), null in \( \nQ \) (@exm-first-sequences-ordered-field), \( x_n - 2/x_n \to 0 \).

*Cauchy.* \( 2/x_n = x_n - (x_n - 2/x_n) \) is the difference of a Cauchy sequence (@thm-sqrt2-cauchy-no-rational-limit) and a null one, which is Cauchy by @thm-cauchy-algebra-ordered-field (a); so it is Cauchy by @thm-cauchy-algebra-ordered-field (b).

*No rational limit.* Suppose \( 2/x_n \to L \in \nQ \). Then \( x_n = 2/x_n + (x_n - 2/x_n) \to L + 0 = L \) by the sum law (@thm-limit-laws-ordered-field (a)), against @thm-sqrt2-cauchy-no-rational-limit.

The terms \( 2/x_n \) approach the gap from below (\( 2/x_n < x_m \) for all \( m \), and \( (2/x_n)^2 = 4/x_n^2 < 2 \)), while the \( x_n \) approach it from above; their differences are null, so in Chapter 5 the two sequences will represent the same real number.
:::

::: {#exr-a-cauchy-sequence-without-a-limit-b2}
[B2]

Let \( (H_n) \) be the sequence of @exm-consecutive-differences-not-cauchy: \( H_0 = 0 \) and \( H_{n+1} = H_n + 1/(n + 1) \) in \( \nQ \). Prove that \( H_{2^k} \ge 1 + k/2 \) for every \( k \in \nN \), and hence that \( (H_n) \) is not bounded.
:::

::: {.solution}
The powers \( 2^k \) of the natural number \( 2 \) are those of Section 1.3 (defined just before @prp-omega-powers-parity by @thm-omega-recursion), with \( 2^0 = 1 \) and \( 2^{k+1} = 2^k \cdot 2 = 2^k + 2^k \).

We use @fd1:ax-induction on \( k \). Base \( P(0) \): \( H_{2^0} = H_1 = H_0 + 1/1 = 1 \ge 1 + 0/2 \). Step: assume \( H_{2^k} \ge 1 + k/2 \). The example shows \( H_{2n} - H_n \ge 1/2 \) for every \( n \ge 1 \); with \( n = 2^k \ge 1 \) (by induction, \( 2^k \ge 1 \)) it gives \( H_{2^{k+1}} \ge H_{2^k} + 1/2 \ge 1 + (k + 1)/2 \).

*Not bounded.* Let \( M \in \nQ_{>0} \). By @thm-rationals-archimedean there is \( k \in \nN \) with \( 2M < k \). Then \( H_{2^k} \ge 1 + k/2 > M \), and \( H_{2^k} > 0 \), so \( \abs{H_{2^k}} > M \). No \( M \) bounds the sequence.

So \( (H_n) \) is not Cauchy for a second reason: a Cauchy sequence is bounded (@prp-cauchy-bounded-ordered-field).
:::

### C. Going deeper

::: {#exr-a-cauchy-sequence-without-a-limit-c1}
[C1: Exit check: a Cauchy sequence with no rational limit]

Let \( y_0 \coloneqq 2 \) and \( y_{n+1} \coloneqq (y_n^2 + 3)/(2y_n) \), a sequence in \( \nQ_{>0} \), and let \( d_n \coloneqq y_n^2 - 3 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that no rational number squares to \( 3 \).
2. Prove that \( (y_n) \) is a Cauchy sequence in \( \nQ \) and that it converges to no element of \( \nQ \).
:::
:::

::: {.solution}
[Hint 1]

For (b), copy facts (i)–(vi) of the proof of @thm-sqrt2-cauchy-no-rational-limit with \( 3 \) in place of \( 2 \). Since only the case \( 2 \) was proved in Chapter 3, prove the analogues of (i), (ii) and the decrease yourself, as @exm-newton-rationals-sqrt2 does for \( 2 \). For (a), run the descent of @thm-no-rational-square-two.
:::

::: {.solution}
[Hint 2]

First verify the identities \( d_{n+1} = d_n^2/(4y_n^2) \) and \( y_n - y_{n+1} = d_n/(2y_n) \) by clearing denominators. In the descent for (a), from \( p^2 = 3q^2 \) show \( q < p < 2q \), and try \( p' \coloneqq 3q - p \), \( q' \coloneqq p - q \).
:::

::: {.solution}
(a) Suppose \( x \in \nQ \) with \( x^2 = 3 \). Then \( x \ne 0 \), and replacing \( x \) by \( -x \) if needed, \( x > 0 \); write \( x = a/b \) with \( a, b \in \nZ_{>0} \) (@prp-integers-embed-rationals (b), @thm-rationals-ordered-field (a)), so \( a^2 = 3b^2 \). The set of \( q \in \nZ_{>0} \) for which some \( p \in \nZ_{>0} \) has \( p^2 = 3q^2 \) contains \( b \) and is bounded below by \( 0 \), so it has a least element \( q \) (@prp-integer-least-element); fix such a \( p \).

*\( q < p \):* if \( p \le q \), then \( p^2 \le q^2 \) (@prp-ordered-ring-rules (g), or equality), so \( 3q^2 \le q^2 \) and \( 2q^2 \le 0 \), against \( 2q^2 > 0 \) (@prp-ordered-ring-rules (e), (O4)). *\( p < 2q \):* if \( 2q \le p \), then \( 4q^2 \le p^2 = 3q^2 \), so \( q^2 \le 0 \), against \( q^2 > 0 \). By totality, \( q < p < 2q \).

Let \( p' \coloneqq 3q - p \) and \( q' \coloneqq p - q \). Then \( q' > 0 \) since \( q < p \); \( q' < q \) since \( p < 2q \); and \( p' > 0 \) since \( p < 2q < 3q \). Expanding,
\[
\begin{aligned}
p'^2 - 3q'^2 &= (9q^2 - 6pq + p^2) - (3p^2 - 6pq + 3q^2) \\
&= 6q^2 - 2p^2 = 2(3q^2 - p^2) = 0 .
\end{aligned}
\]
So \( q' \) is an admissible denominator smaller than \( q \), a contradiction. No rational squares to \( 3 \).

(b) *Positivity and the two identities.* For \( s \in \nQ_{>0} \), \( (s^2 + 3)/(2s) \in \nQ_{>0} \) (\( s^2 + 3 > 0 \), \( 2s > 0 \), @prp-reciprocal-order (a), (O4)), so the recursion (@fd2:thm-recursion, read on \( \omega \) through @cor-omega-identification (b)) defines \( (y_n) \) in \( \nQ_{>0} \). With \( u(s) \coloneqq (s^2 + 3)/(2s) \), clearing the non-zero denominators \( 4s^2 \) and \( 2s \),
\[
u(s)^2 - 3 = \frac{(s^2 + 3)^2 - 12 s^2}{4s^2} = \frac{(s^2 - 3)^2}{4s^2} , \qquad s - u(s) = \frac{s^2 - 3}{2s} .
\]
So \( d_{n+1} = d_n^2/(4y_n^2) \) and \( y_n - y_{n+1} = d_n/(2y_n) \). By induction, \( d_n > 0 \): \( d_0 = 1 \), and \( d_n > 0 \) gives \( d_n^2 > 0 \), so \( d_{n+1} > 0 \). Hence \( y_n^2 > 3 \), \( 4y_n^2 > 12 \), and \( d_{n+1} \le d_n^2/12 \) (@prp-reciprocal-order (b)). Also \( y_n - y_{n+1} > 0 \).

*Values.* \( y_1 = 7/4 \), \( y_2 = 97/56 \); \( d_0 = 1 \), \( d_1 = 49/16 - 3 = 1/16 \), \( d_2 = 9409/3136 - 3 = 1/3136 \), and indeed \( d_2 = (1/16)^2/(4 \cdot 49/16) = 1/3136 \).

*Monotone, and \( y_n > 1 \).* As in (iii) and (iv): \( y_n > 1 \), since \( 0 < y_n \le 1 \) would give \( y_n^2 \le 1 < 3 \); and \( y_m \le y_n \) for \( m \ge n \), by induction from \( y_{n+1} < y_n \).

*A bound on \( d_n \).* \( d_n \le 1/(16n) \) for \( n \ge 1 \), by induction: \( d_1 = 1/16 \); if \( 0 < d_n \le 1/(16n) \le 1/16 \), then \( d_{n+1} \le d_n \cdot d_n/12 \le d_n/192 \le 1/(3072 n) \le 1/(16(n + 1)) \), since \( 16n + 16 \le 3072 n \) for \( n \ge 1 \).

*Close terms.* For \( m \ge n \ge 1 \): \( y_m \le y_n \), and \( y_m > 3/y_m \ge 3/y_n \), so
\[
0 \le y_n - y_m \le y_n - \frac{3}{y_n} = \frac{d_n}{y_n} \le d_n \le \frac{1}{16 n} ,
\]
using \( y_n > 1 \).

*Cauchy.* Given \( \varepsilon \in \nQ_{>0} \), @cor-rationals-archimedean-epsilon gives \( N \in \nZ_{>0} \) with \( 1/N < \varepsilon \). For \( m, n \ge N \), with \( k \coloneqq \min\{m, n\} \ge N \), \( \abs{y_m - y_n} \le 1/(16k) \le 1/N < \varepsilon \).

*No rational limit.* If \( y_n \to L \in \nQ \), then \( y_n^2 \to L^2 \) (@thm-limit-laws-ordered-field (c)). For \( n \ge 1 \), \( 0 < d_n \le 1/(16n) \le 1/(n + 1) \), so \( d_n \to 0 \) by the squeeze (@prp-limit-preserves-order-ordered-field (c), with \( N_0 = 1 \) and the null upper sequence \( (1/(n + 1)) \)), and \( y_n^2 = 3 + d_n \to 3 \) (@thm-limit-laws-ordered-field (a)). By @thm-limit-unique-ordered-field, \( L^2 = 3 \), against (a).

**Marking scheme.** (10 points)
- 2: (a), a descent with a least denominator (@prp-integer-least-element), with the inequalities \( q < p < 2q \) and the positivity of \( p' \), \( q' \) justified (another correct route, such as divisibility by \( 3 \) with a least denominator, earns the same).
- 1: positivity of \( y_n \) and \( d_n \), and the recursion identity for \( d_{n+1} \).
- 2: a comparison of \( y_n \) and \( y_m \) for \( m \ge n \): monotonicity together with \( y_m \ge 3/y_n \), or (factorization route, as in R4) \( \abs{y_n - y_m} = \abs{d_n - d_m}/(y_n + y_m) \) with \( y_n + y_m > 2 \), since \( y_n > 1 \) follows from \( y_n^2 > 3 \).
- 2: an explicit bound on \( d_n \) (or on \( y_n - y_m \)) tending to \( 0 \), with Archimedes giving \( N \) for each rational \( \varepsilon \).
- 1: Cauchy concluded with the quantifiers in order.
- 2: no rational limit, by the product law, uniqueness of limits and (a).
Fatal errors (0 for the step): assuming that \( \sqrt 3 \) exists in \( \nQ \) or in a larger field and comparing with it; invoking a monotone convergence theorem. A route by factorization as in R4 earns the next 2 for showing \( d_n \to 0 \) (by an explicit bound with Archimedes, or by the squeeze), and the 1 for concluding that \( (d_n) \) is Cauchy by @prp-convergent-cauchy-ordered-field and transferring this to \( (y_n) \) with the quantifiers in order. A route through the steps \( y_n - y_{n+1} \) and a geometric bound earns the middle 2 + 1 only if the sum of the steps from \( n \) to \( m \) is bounded explicitly, independently of \( m \) (the example at the end of Section 4.5 shows why).
:::

::: {#exr-a-cauchy-sequence-without-a-limit-c2}
[C2: Cauchy depends on the field]

In the ordered field \( \nQ(t) \) of @exm-rational-function-field, consider the sequence \( a_n \coloneqq 1/((n + 1) \cdot 1) \), whose terms are the rationals \( 1/(n + 1) \). Explain why \( (a_n) \) is **not** a Cauchy sequence in \( \nQ(t) \), although it is Cauchy in \( \nQ \).
:::

::: {.solution}
In \( \nQ \), \( (1/(n + 1)) \) is Cauchy (Section 4.5, the examples after @def-cauchy-sequence-ordered-field).

In \( \nQ(t) \), take the tolerance \( \varepsilon \coloneqq 1/t \), which is positive (the example shows \( 0 < 1/t \)). Let \( N \in \nN \), and take \( m \coloneqq N \), \( n \coloneqq N + 1 \). Then
\[
\abs{a_m - a_n} = \frac{1}{N + 1} - \frac{1}{N + 2} = \frac{1}{(N + 1)(N + 2)} ,
\]
by @lem-field-fraction-rules (c), a positive rational. The natural number \( k \coloneqq (N + 1)(N + 2) \) satisfies \( k \cdot 1 < t \), because \( t - k \cdot 1 \) has leading coefficient \( 1 > 0 \) (@exm-rational-function-field). Since \( 0 < k \cdot 1 < t \), @prp-reciprocal-order (b) gives \( 1/t < 1/(k \cdot 1) = \abs{a_m - a_n} \). So for the tolerance \( 1/t \) no threshold \( N \) works, and \( (a_n) \) is not Cauchy in \( \nQ(t) \).

The terms are the same in both fields; what changed is the set of tolerances. \( \nQ(t) \) has the positive element \( 1/t \), below every positive rational, and the rational differences \( 1/((N + 1)(N + 2)) \) never get below it. Being Cauchy is a property of a sequence **in a field**, not of its terms alone. (The example \( \nQ(t) \) uses school polynomial algebra; nothing else in the book depends on this exercise.)
:::

### R. Review

::: {#exr-a-cauchy-sequence-without-a-limit-r1}
[R1]

Let \( \sC \) be the set of Cauchy sequences in \( \nQ \) and \( \sN \) the set of null sequences in \( \nQ \). Prove that \( \sN \subseteq \sC \), that \( (y_n + z_n) \in \sN \) whenever \( (y_n), (z_n) \in \sN \), and that \( (r_n z_n) \in \sN \) whenever \( (r_n) \in \sC \) and \( (z_n) \in \sN \).
:::

::: {.solution}
\( \sN \subseteq \sC \) by @thm-cauchy-algebra-ordered-field (a). If \( y_n \to 0 \) and \( z_n \to 0 \), then \( y_n + z_n \to 0 + 0 = 0 \) by @thm-limit-laws-ordered-field (a). If \( (r_n) \in \sC \), it has a bound \( M \in \nQ_{>0} \) (@prp-cauchy-bounded-ordered-field), so \( (z_n r_n) \) is null by @prp-null-times-bounded-ordered-field, and \( r_n z_n = z_n r_n \). Chapter 5 uses these two closure properties when it adds and multiplies classes.
:::

::: {#exr-a-cauchy-sequence-without-a-limit-r2}
[R2]

Let \( F \) be an ordered field. Define \( r_0 \coloneqq 1 \) and \( r_{n+1} \coloneqq r_n/2 + 1 \) for \( n \in \nN \). Prove that \( 1 \le r_n < 2 \) and \( r_n < r_{n+1} \) for every \( n \in \nN \).
:::

::: {.solution}
The tools are definition by recursion and proof by induction (@fd2:thm-recursion, @fd1:ax-induction), both read on \( \nN = \omega \) through @cor-omega-identification (b). Here \( 2 \coloneqq 1 + 1 > 0 \) (@prp-ordered-field-halves (b)), so \( 2 \ne 0 \) and \( x/2 \) is defined for every \( x \in F \). The recursion theorem with \( X = F \), starting value \( 1 \) and rule \( g(n, x) \coloneqq x/2 + 1 \) gives exactly one sequence \( (r_n) \) in \( F \) satisfying the two equations. Its first terms are \( r_1 = 3/2 \) and \( r_2 = 7/4 \).

*The bounds.* We prove \( P(n) \): "\( 1 \le r_n < 2 \)" by induction on \( n \). *Base \( P(0) \):* \( r_0 = 1 \), and \( 1 = 2/2 < 2 \) by @prp-ordered-field-halves (b) with \( \varepsilon = 2 \). *Step:* assume \( 1 \le r_n < 2 \). Then \( r_n > 0 \), so \( r_n/2 > 0 \) (@prp-reciprocal-order (a), (O4)). Multiplying \( r_n < 2 \) by \( 1/2 > 0 \) gives \( r_n/2 < 2/2 = 1 \) (@prp-ordered-ring-rules (c)). Adding \( 1 \) (@prp-ordered-ring-rules (b)),
\[
1 = 0 + 1 < \frac{r_n}{2} + 1 = r_{n+1} < 1 + 1 = 2 .
\]
So \( 1 \le r_{n+1} < 2 \), which is \( P(n + 1) \).

*The increase.* Let \( n \in \nN \). By \( P(n) \), \( r_n > 0 \), so \( r_n = r_n/2 + r_n/2 \) (@prp-ordered-field-halves (b) with \( \varepsilon = r_n \)), and \( r_n/2 < 1 \) as in the step. Hence
\[
r_{n+1} - r_n = \Bigl(\frac{r_n}{2} + 1\Bigr) - \Bigl(\frac{r_n}{2} + \frac{r_n}{2}\Bigr) = 1 - \frac{r_n}{2} > 0 ,
\]
and \( r_n < r_{n+1} \) by @prp-ordered-ring-rules (a).
:::

::: {#exr-a-cauchy-sequence-without-a-limit-r3}
[R3]

Say that a sequence \( (a_n) \) in an ordered field \( F \) **eventually keeps one sign** if there are \( c \in F_{>0} \) and \( N \in \nN \) such that either \( a_n \ge c \) for every \( n \ge N \), or \( a_n \le -c \) for every \( n \ge N \). Write this in symbols, and form its negation by moving \( \neg \) inward one law at a time, naming each law. Then use the negation to show that \( a_n \coloneqq (-1)^n/(n + 1) \) in \( \nQ \) does not eventually keep one sign, and explain why this does not contradict the theorem that a Cauchy sequence that is not null eventually keeps one sign.
:::

::: {.solution}
"\( (a_n) \) eventually keeps one sign" is
\[
\exists c \in F_{>0} \ \exists N \in \nN \ \Bigl( \forall n \in \nN \ (n \ge N \to a_n \ge c) \ \vee \ \forall n \in \nN \ (n \ge N \to a_n \le -c) \Bigr) .
\]
Negating, with the laws for bounded quantifiers (@fd1:prp-bounded-quantifier-negation), De Morgan's laws (@fd1:prp-de-morgan) and negated implication (@fd1:prp-negated-implication):

1. \( \forall c \in F_{>0} \ \neg \exists N \in \nN \ (\dots) \), by (b) of the bounded law;
2. \( \forall c \in F_{>0} \ \forall N \in \nN \ \neg \bigl( \forall n \, (\dots) \vee \forall n \, (\dots) \bigr) \), by (b) again;
3. \( \forall c \in F_{>0} \ \forall N \in \nN \ \bigl( \neg \forall n \, (\dots) \wedge \neg \forall n \, (\dots) \bigr) \), by De Morgan (a) (and (b) for the converse);
4. \( \forall c \in F_{>0} \ \forall N \in \nN \ \bigl( \exists n \in \nN \ \neg (n \ge N \to a_n \ge c) \wedge \exists n \in \nN \ \neg (n \ge N \to a_n \le -c) \bigr) \), by (a) of the bounded law, twice;
5. \( \forall c \in F_{>0} \ \forall N \in \nN \ \bigl( \exists n \in \nN \ (n \ge N \wedge \neg (a_n \ge c)) \wedge \exists n \in \nN \ (n \ge N \wedge \neg (a_n \le -c)) \bigr) \), by @fd1:prp-negated-implication, twice;
6. and \( \neg (a_n \ge c) \) is \( a_n < c \), \( \neg (a_n \le -c) \) is \( a_n > -c \), by totality (@prp-ordered-field-halves (a)).

So the negation says: **for every** \( c \in F_{>0} \) and **every** \( N \in \nN \), some \( n \ge N \) has \( a_n < c \), and some \( n \ge N \) has \( a_n > -c \).

*The example.* Here \( (-1)^n \) is the power in \( \nQ \) (@def-naturals-in-ordered-field), so \( (-1)^{n+1} = -(-1)^n \) (@prp-ring-algebra (c)), and by induction \( (-1)^n \) is \( 1 \) or \( -1 \) for every \( n \). Let \( c \in \nQ_{>0} \) and \( N \in \nN \). Of \( (-1)^N \) and \( (-1)^{N+1} = -(-1)^N \), one is \( 1 \) and the other \( -1 \); call \( p \) the index among \( N, N + 1 \) with \( (-1)^p = 1 \), and \( q \) the other. Both are \( \ge N \), and \( 1/(p + 1) > 0 \), \( 1/(q + 1) > 0 \) (@prp-reciprocal-order (a)). So \( a_q = -1/(q + 1) < 0 < c \) and \( a_p = 1/(p + 1) > 0 > -c \) (@prp-ordered-ring-rules (a)). This is the negation, so \( (a_n) \) does not eventually keep one sign.

*No contradiction.* \( \abs{a_n} = \abs{(-1)^n} \cdot \abs{1/(n + 1)} = 1/(n + 1) \) (@prp-absolute-value-ordered-field (b)), and \( (1/(n + 1)) \) is null in \( \nQ \) (@exm-first-sequences-ordered-field (b)). So for each \( \varepsilon \in \nQ_{>0} \) the threshold that serves \( (1/(n + 1)) \) gives \( \abs{a_n - 0} < \varepsilon \): the sequence \( (a_n) \) is null. It is Cauchy (@thm-cauchy-algebra-ordered-field (a)), but the theorem (@thm-cauchy-not-null-sign) assumes "not null", so it says nothing about \( (a_n) \). The example shows that this hypothesis cannot be dropped.
:::

::: {#exr-a-cauchy-sequence-without-a-limit-r4}
[R4]

Let \( (a_n) \) be a sequence in \( \nQ \) with \( a_n > 0 \) for every \( n \) and \( a_n^2 \to 2 \) in \( \nQ \). Is \( (a_n) \) a Cauchy sequence in \( \nQ \)? Prove your answer.
:::

::: {.solution}
**Yes.** The tool is the factorization \( a_n^2 - a_m^2 = (a_n - a_m)(a_n + a_m) \), which turns closeness of the squares into closeness of the terms once the factor \( a_n + a_m \) is bounded below by a positive constant.

*A lower bound.* By @lem-limit-bounded-away-ordered-field applied to \( a_n^2 \to 2 > 0 \), there is \( N_0 \) with \( a_n^2 > 2/2 = 1 \) for every \( n \ge N_0 \). For such \( n \), \( a_n > 1 \): otherwise \( 0 < a_n \le 1 \) would give \( a_n^2 \le 1 \) (@prp-ordered-ring-rules (g)). So \( a_n + a_m > 2 \) for \( m, n \ge N_0 \), and \( 1/(a_n + a_m) < 1/2 \) (@prp-reciprocal-order (b)).

*The estimate.* For \( m, n \ge N_0 \), dividing the factorization by \( a_n + a_m \ne 0 \),
\[
\abs{a_n - a_m} = \frac{\abs{a_n^2 - a_m^2}}{a_n + a_m} \le \frac{\abs{a_n^2 - a_m^2}}{2} .
\]
The sequence \( (a_n^2) \) converges, so it is Cauchy (@prp-convergent-cauchy-ordered-field). Given \( \varepsilon \in \nQ_{>0} \), choose \( N_1 \) with \( \abs{a_n^2 - a_m^2} < 2\varepsilon \) for all \( m, n \ge N_1 \), and let \( N \coloneqq \max\{N_0, N_1\} \). For \( m, n \ge N \), \( \abs{a_n - a_m} < 2\varepsilon/2 = \varepsilon \). So \( (a_n) \) is Cauchy.

*Why the look-alike tools fail.* The limit laws would need a limit of \( (a_n) \), and there is none in \( \nQ \): \( a_n \to L \) would give \( a_n^2 \to L^2 \), so \( L^2 = 2 \), against @thm-no-rational-square-two. @thm-cauchy-not-null-sign and @prp-cauchy-reciprocal-ordered-field presuppose that \( (a_n) \) is Cauchy, which is what is asked. The Newton sequence of @thm-sqrt2-cauchy-no-rational-limit is one such \( (a_n) \), so the question is not empty.
:::

<!-- dependency ledger
thm-sqrt2-cauchy-no-rational-limit (proof): x_n in Q_{>0}, e_n > 0, e_{n+1} = e_n^2/(4x_n^2) <= e_n^2/8, x_{n+1} < x_n | exm-newton-rationals-sqrt2 (i)-(iii), cited
thm-sqrt2-cauchy-no-rational-limit (proof): every m >= n in N is n + k | prp-omega-order-arithmetic (a), cited
thm-sqrt2-cauchy-no-rational-limit (proof): induction for (iv), (v) | fd1:ax-induction via cor-omega-identification (b), cited
thm-sqrt2-cauchy-no-rational-limit (proof): 4(n + 1) <= 128 n and n + 1 <= 4n for n >= 1; 4 <= 4n; N <= 4N <= 4k | inline arithmetic in N, carried into Q by prp-naturals-in-ordered-field (b); verify/ch04/thm-sqrt2-cauchy-no-rational-limit.py
thm-sqrt2-cauchy-no-rational-limit (proof): x_n - 2/x_n = (x_n^2 - 2)/x_n | lem-field-fraction-rules (b); inline
thm-sqrt2-cauchy-no-rational-limit (proof): constant sequence 2 tends to 2; constant 0 tends to 0 | exm-first-sequences-ordered-field, cited
thm-sqrt2-cauchy-no-rational-limit (example): values x_0..x_3, e_0..e_3 and e_n <= 1/(4n) for n = 1, 2, 3 | exm-newton-rationals-sqrt2; verify/ch04/thm-sqrt2-cauchy-no-rational-limit.py
thm-sqrt2-cauchy-no-rational-limit (claim): Section 3.3: {x in Q : x^2 < 2} has no rational supremum | F3.2 section 06 (thm-rationals-gap-sqrt2), prose pointer only, not used in a proof
thm-sqrt2-cauchy-no-rational-limit (claim): subsequence n_k >= k by induction; e_{n_k} <= 1/(4k) <= 1/(k + 1) | inline (discreteness of N, thm-omega-order); argument of the proof rerun
thm-sqrt2-cauchy-no-rational-limit (claim): closing paragraph, the complete ordered field, its uniqueness, the analysis volume | F3.10, F3.4, AN1.1 and AN1.2 (prose pointers; nothing depends on them)
thm-sqrt2-cauchy-no-rational-limit (solution): the Quick check, 1/N < 1/100 gives least N = 101 | cor-rationals-archimedean-epsilon; inline
exr-a-cauchy-sequence-without-a-limit-a1 (solution): x_2 - x_3 = 1/408, e_2/x_2 = 1/204 | verify/ch04/exr-a-cauchy-sequence-without-a-limit-a1.py
exr-a-cauchy-sequence-without-a-limit-b2 (solution): 2^{k+1} = 2^k + 2^k and 2^k >= 1 | prp-omega-powers-parity (powers in N, Section 1.3, defined by thm-omega-recursion); omega arithmetic; inline; verify/ch04/exr-a-cauchy-sequence-without-a-limit-b2.py
exr-a-cauchy-sequence-without-a-limit-b2 (solution): H_{2n} - H_n >= 1/2 | exm-consecutive-differences-not-cauchy, cited
exr-a-cauchy-sequence-without-a-limit-c1 (solution): identities for u(s) = (s^2 + 3)/(2s); descent identity (3q - p)^2 - 3(p - q)^2 = 2(3q^2 - p^2); values y_1, y_2, d_0..d_2; d_n <= 1/(16n) | verify/ch04/exr-a-cauchy-sequence-without-a-limit-c1.py
exr-a-cauchy-sequence-without-a-limit-c1 (solution): (a) follows the route of thm-no-rational-square-two | prp-integer-least-element, prp-ordered-ring-rules (e), (g), cited
exr-a-cauchy-sequence-without-a-limit-c2 (solution): Q(t) ordered by leading coefficients; t > k * 1 for every k in N | exm-rational-function-field (school fact; formal polynomials in F5.4); exercise only, nothing depends on it
exr-a-cauchy-sequence-without-a-limit-c2 (solution): 1/(N + 1) - 1/(N + 2) = 1/((N + 1)(N + 2)) | lem-field-fraction-rules (c); verify/ch04/exr-a-cauchy-sequence-without-a-limit-c2.py
exr-a-cauchy-sequence-without-a-limit-r1 (solution): N in C, N closed under +, r.z in N for r in C, z in N | thm-cauchy-algebra-ordered-field (a), thm-limit-laws-ordered-field (a), prp-cauchy-bounded-ordered-field, prp-null-times-bounded-ordered-field, cited
exr-a-cauchy-sequence-without-a-limit-r2 (solution): r_1 = 3/2, r_2 = 7/4; 1 <= r_n < 2 and r_n < r_{n+1}; r_{n+1} - r_n = 1 - r_n/2 | fd2:thm-recursion and fd1:ax-induction via cor-omega-identification (b), cited; verify/ch04/exr-a-cauchy-sequence-without-a-limit-r2.py
exr-a-cauchy-sequence-without-a-limit-r3 (solution): (-1)^n in {1, -1}, (-1)^{n+1} = -(-1)^n and |a_n| = 1/(n + 1) | prp-ring-algebra (c), prp-absolute-value-ordered-field (b); inline induction
exr-a-cauchy-sequence-without-a-limit-r3 (solution): negation of "eventually keeps one sign" | fd1:prp-bounded-quantifier-negation, fd1:prp-de-morgan (a), (b), fd1:prp-negated-implication, prp-ordered-field-halves (a), cited
exr-a-cauchy-sequence-without-a-limit-r4 (solution): a_n^2 - a_m^2 = (a_n - a_m)(a_n + a_m) | prp-ring-algebra; verify/ch04/exr-a-cauchy-sequence-without-a-limit-r4.py
-->
