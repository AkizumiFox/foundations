# The Real Numbers Form a Complete Ordered Field

Section 5.5 proved one form of completeness: in \( \nR \) every Cauchy sequence converges (@thm-constructed-reals-cauchy-complete). The analysis volume starts from another form, about sets rather than sequences: every non-empty set of real numbers that is bounded above has a least upper bound. In \( \nQ \) both fail, the first by @thm-sqrt2-cauchy-no-rational-limit and the second by @thm-rationals-gap-sqrt2. This section names the second property for an arbitrary ordered field, proves that an ordered field that is Archimedean and Cauchy-complete has it, and concludes that the constructed \( \nR \) is a complete ordered field. The proof bisects intervals, and one line of it, which we shall point at, cannot do without Archimedes.

Throughout, \( F \) is an ordered field (@def-ordered-ring-and-field). Its order \( \le \) is a total order (@prp-ordered-field-halves (a)), so the words "upper bound", "bounded above" and "supremum" of *Sets, Relations, and Cardinality*, Section 2.6 apply to subsets of \( F \) (@fd2:def-order-bounds, @fd2:def-order-supremum). When \( F = \nR \), we keep the identification of Section 5.4, writing \( q \) for \( \kappa(q) \).

## Complete ordered fields

Section 2.6 found a gap in \( \nQ \) without any sequence: the set \( A = \{ x \in \nQ : x^2 < 2 \} \) is non-empty and bounded above in \( \nQ \), and among its rational upper bounds there is no least one (@thm-rationals-gap-sqrt2). The upper bounds crowd down toward a place where \( \nQ \) has no element. A field without such gaps is one in which every set that could have a least upper bound does have one.

*Every non-empty set that is bounded above has a least upper bound.*

::: {#def-complete-ordered-field}
[Complete Ordered Field]

An ordered field \( F \) is **complete** if **every non-empty** subset \( A \subseteq F \) that is **bounded above** in \( (F, \le) \) (@fd2:def-order-bounds) has a supremum in \( F \) (@fd2:def-order-supremum). In symbols, writing \( \mathrm{ub}(u) \) for \( \forall a \in A \ \ a \le u \),
\[
\begin{aligned}
&\forall A \subseteq F \ \ \bigl( (A \ne \emptyset \wedge \exists u \in F \ \mathrm{ub}(u)) \Rightarrow \\
&\qquad \exists s \in F \ \bigl( \mathrm{ub}(s) \wedge \forall u \in F \ (\mathrm{ub}(u) \Rightarrow s \le u) \bigr) \bigr) .
\end{aligned}
\]
An ordered field in which every Cauchy sequence (@def-cauchy-sequence-ordered-field) converges is called **Cauchy-complete**.
:::

In words: the hypothesis asks for a set with at least one element and at least one upper bound in \( F \); the conclusion asks for an element \( s \) of \( F \) that is an upper bound, clause (S1), and lies below every upper bound, clause (S2). The supremum need not belong to \( A \).

**Well-definedness.** A set has at most one supremum: if \( s \) and \( s' \) both are, then (S2) for each, with the other as the upper bound, gives \( s \le s' \) and \( s' \le s \), so \( s = s' \) by antisymmetry. So "the supremum of \( A \)", written \( \sup A \), names one element when it exists.

**Examples.**

*The negative elements.* In every ordered field, \( A \coloneqq \{ x \in F : x < 0 \} \) has supremum \( 0 \). It is non-empty (\( -1 \in A \)). The element \( 0 \) is an upper bound. If an upper bound \( b \) had \( b < 0 \), then \( b < b/2 < 0 \) (@prp-ordered-field-halves (b)), so \( b/2 \in A \) lies above \( b \), which is impossible. So every upper bound \( b \) satisfies \( b \ge 0 \), and \( \sup A = 0 \notin A \). No completeness was needed: some sets have suprema in every ordered field.

*The rationals.* \( \nQ \) is **not** complete: @thm-rationals-gap-sqrt2 exhibits a non-empty subset bounded above with no supremum in \( \nQ \).

*The constructed reals.* \( \nR \) is complete; this is the main theorem of the section, proved at its end.

::: {.second-reading title="A degenerate case, and non-examples by minimal change"}
*A singleton.* \( \sup \{a\} = a \), in every ordered field. This degenerate case matters below: a set may be bounded above by its own element.

Drop "non-empty": the empty set is bounded above by every element of \( F \), so its upper bounds are all of \( F \), and \( F \) has no least element (\( x - 1 < x \)). Drop "bounded above": \( F \) itself has no upper bound (\( x < x + 1 \)), so no supremum. With either clause removed, no ordered field at all would be complete.
:::

**Why this definition.** It asks about suprema, not maxima: the set of negative elements has no greatest element in any ordered field, since \( x < x/2 < 0 \) for \( x < 0 \), and asking for maxima would make no field complete. It asks about sets, not sequences, the form *Analysis on the Real Line* takes as its axiom. "Complete" alone always means this property; the sequence property of Section 5.5 is "Cauchy-complete".

::: {.warning}
The supremum of a set is an upper bound **not necessarily in the set**, and "complete" is not "every non-empty bounded set has a **largest** element": the set of negative elements above has supremum \( 0 \) and no largest element. A proof that ends "so \( \sup A \in A \)" needs a reason, such as \( A \) being finite.
:::

So \( \nQ \) is neither complete nor Cauchy-complete. Section 5.5 removed the second gap for \( \nR \); this section removes the first.

## Powers of two in an ordered field

The bisection below halves an interval at each step, so after \( k \) steps its length is the first length divided by \( 2^k \). We need \( 2^k \) to grow at least as fast as \( k + 1 \), inside the field.

::: {#lem-power-two-bound}
[A Lower Bound for Powers of Two]

Let \( F \) be an ordered field, and let \( (2 \cdot 1_F)^k \) be the power in \( F \) of @def-naturals-in-ordered-field (b). Then
\[
(2 \cdot 1_F)^k \ge (k + 1) \cdot 1_F \qquad \text{for every } k \in \nN .
\]
In particular \( (2 \cdot 1_F)^k \ge 1_F > 0 \).
:::

::: {.idea}
Induction on \( k \). Multiplying by \( 2 \) doubles the right side, \( (k + 1) + (k + 1) \), and doubling gains at least \( 1 \), which is all the step needs.
:::

::: {.proof}
We use @fd1:ax-induction, read on \( \nN = \omega \) through @cor-omega-identification (b), for \( P(k) \): \( (2 \cdot 1_F)^k \ge (k + 1) \cdot 1_F \).

*Base \( P(0) \).* \( (2 \cdot 1_F)^0 = 1_F \) by @def-naturals-in-ordered-field (b), and \( (0 + 1) \cdot 1_F = 1 \cdot 1_F = 0 \cdot 1_F + 1_F = 1_F \) by (a) of that definition, since \( 0 + 1 = 1 \) (@def-omega-arithmetic (c)). Equality holds.

*Step.* Assume \( P(k) \), and let \( y \coloneqq (k + 1) \cdot 1_F \). By @def-naturals-in-ordered-field (a) and @def-omega-arithmetic (c), \( 2 \cdot 1_F = 1 \cdot 1_F + 1_F = 1_F + 1_F \), which is positive (@prp-ordered-field-halves (b)). By @def-naturals-in-ordered-field (b), \( P(k) \), and @prp-ordered-ring-rules (c) (or equality, if \( P(k) \) holds with equality),
\[
(2 \cdot 1_F)^{k+1} = (2 \cdot 1_F)^k (2 \cdot 1_F) \ge y (1_F + 1_F) = y + y ,
\]
the last step by distributivity (F9) and (F7). Since \( k + 1 \ge 1 \) (@thm-omega-order (d)), @prp-naturals-in-ordered-field (b) gives \( y \ge 1_F \), so \( y + y \ge y + 1_F \) (@prp-ordered-ring-rules (b)). Finally \( y + 1_F = ((k + 1) + 1) \cdot 1_F \) by @def-naturals-in-ordered-field (a). Hence \( (2 \cdot 1_F)^{k+1} \ge ((k + 1) + 1) \cdot 1_F \), which is \( P(k + 1) \).

The last sentence of the lemma follows from \( (k + 1) \cdot 1_F \ge 1_F \) and \( 1_F > 0 \) (@prp-ordered-ring-rules (e)).
:::

From here on, \( 2^k \) means \( (2 \cdot 1_F)^k \). By @prp-naturals-in-ordered-field (c) it equals \( (2^k) \cdot 1_F \), the multiple of \( 1_F \) by the natural number \( 2^k \), so the two readings agree; the proofs below use only the power in \( F \) and the lemma. Since \( 2^k > 0 \), the quotient \( D/2^k \) is defined for every \( D \in F \).

## From Cauchy-complete to complete

::: {#thm-cauchy-archimedean-lub}
[Archimedean and Cauchy-Complete Implies Complete]

Let \( F \) be an ordered field that is Archimedean (@def-archimedean-ordered-field) and Cauchy-complete (@def-complete-ordered-field). Then \( F \) is complete.
:::

::: {.idea}
Given \( A \), we want a point \( s \) that is an upper bound and below every upper bound. Trap it. Start with an interval \( [l_0, u_0] \) whose right end is an upper bound of \( A \) and whose left end is not. Halve it: if the midpoint is an upper bound, it becomes the new right end; if not, the new left end. **Bisect and keep the invariant**: right end an upper bound, left end not.

The right ends decrease and the left ends increase, and both stay within the current interval, whose length is \( D/2^k \). If that length goes to \( 0 \), the right ends form a Cauchy sequence, and Cauchy-completeness gives a limit \( s \). Then \( s \) is an upper bound because every right end is, and it is the least one because left ends, which are not upper bounds, come arbitrarily close to it.

Step roadmap: ① the starting interval; ② the bisection, defined by a rule, and its invariants; ③ the lengths \( D/2^k \) tend to \( 0 \); ④ \( (u_k) \) converges to some \( s \); ⑤ \( s \) is the supremum. *Before reading on: which of these steps uses that \( F \) is Archimedean?*
:::

::: {.proof}
Let \( A \subseteq F \) be non-empty and bounded above.

**Step 1: the starting interval.** Fix \( a_0 \in A \) [\( \rulename{\exists E} \)] and an upper bound \( M \) of \( A \) [\( \rulename{\exists E} \)]; each is one object, fixed once, and no choice is involved. Let \( l_0 \coloneqq a_0 - 1 \), \( u_0 \coloneqq M \) and \( D \coloneqq u_0 - l_0 \). Then \( l_0 < a_0 \le M = u_0 \), so \( D > 0 \); \( u_0 \) is an upper bound of \( A \); and \( l_0 \) is not, because \( a_0 \in A \) and \( a_0 > l_0 \).

**Step 2: the bisection.** Define \( g \colon \nN \times (F \times F) \to F \times F \) by
\[
g\bigl(k, (l, u)\bigr) \coloneqq
\begin{cases}
(l, c) & \text{if } c \text{ is an upper bound of } A , \\
(c, u) & \text{otherwise,}
\end{cases}
\qquad c \coloneqq \frac{l + u}{2} .
\]
For each input exactly one case applies, so \( g \) is a function, given by a rule. By @fd2:thm-recursion (read on \( \nN = \omega \) through @cor-omega-identification (b)), with \( X = F \times F \) and starting value \( (l_0, u_0) \), there is exactly one sequence \( k \mapsto (l_k, u_k) \) with \( (l_{k+1}, u_{k+1}) = g(k, (l_k, u_k)) \) for every \( k \).

We prove by induction on \( k \) that, for every \( k \in \nN \):

::: {.enumerate options="label=(I\arabic*)"}
1. \( u_k \) is an upper bound of \( A \);
2. \( l_k \) is not an upper bound of \( A \);
3. \( u_k - l_k = D/2^k \).
:::

The base is Step 1, with \( D/2^0 = D/1_F = D \). Suppose (I1)–(I3) hold for \( k \), and let \( c \coloneqq (l_k + u_k)/2 \). Then \( c - l_k = u_k - c = (u_k - l_k)/2 = D/(2^k \cdot 2) = D/2^{k+1} \), by field arithmetic (@lem-field-fraction-rules (b)) and @def-naturals-in-ordered-field (b). If \( c \) is an upper bound, then \( (l_{k+1}, u_{k+1}) = (l_k, c) \): the right end \( c \) is an upper bound, the left end \( l_k \) is not, by (I2), and \( c - l_k = D/2^{k+1} \). Otherwise \( (l_{k+1}, u_{k+1}) = (c, u_k) \): the left end \( c \) is not an upper bound, the right end \( u_k \) is, by (I1), and \( u_k - c = D/2^{k+1} \). This proves (I1)–(I3) for \( k + 1 \).

By (I3), \( u_k - l_k = D/2^k > 0 \), so \( l_k < c < u_k \) (@prp-ordered-field-halves (b)); in either case \( l_k \le l_{k+1} \) and \( u_{k+1} \le u_k \). By induction on \( i \), \( l_k \le l_{k+i} \) and \( u_{k+i} \le u_k \) for every \( i \in \nN \), and every \( j \ge k \) is \( k + i \) for some \( i \) (@prp-omega-order-arithmetic (a)). So for \( j \ge k \), \( l_k \le l_j < u_j \le u_k \), and therefore
\[
0 \le u_k - u_j \le u_k - l_k = \frac{D}{2^k} \qquad (j \ge k) .
\]{#eq-bisection-tail}

**Step 3: the lengths tend to \( 0 \).** Let \( \varepsilon \in F_{>0} \). Since \( F \) is **Archimedean**, there is \( n \in \nN \) with
\[
\frac{D}{\varepsilon} < n \cdot 1_F .
\]{#eq-bisection-archimedes}
Let \( k \ge n \). By @lem-power-two-bound and @prp-naturals-in-ordered-field (b), \( 2^k \ge (k + 1) \cdot 1_F > k \cdot 1_F \ge n \cdot 1_F > D/\varepsilon > 0 \). By @prp-reciprocal-order (b), \( 1/2^k < \varepsilon/D \), and multiplying by \( D > 0 \) (@prp-ordered-ring-rules (c)) gives \( D/2^k < \varepsilon \). So \( \abs{D/2^k - 0} < \varepsilon \) for every \( k \ge n \): the sequence \( (D/2^k)_k \) is null.

Consequently \( (u_k) \) is Cauchy in \( F \): for \( \varepsilon \) and \( n \) as above and \( j, k \ge n \), say \( j \ge k \) (the other case is symmetric), @eq-bisection-tail gives \( \abs{u_j - u_k} = u_k - u_j \le D/2^k < \varepsilon \).

Steps 1–3 use only that \( F \) is an Archimedean ordered field. Step 4 is the only one that uses Cauchy-completeness.

**Step 4: the limit.** Since \( F \) is Cauchy-complete, \( (u_k) \) converges; fix \( s \in F \) with \( u_k \to s \) [\( \rulename{\exists E} \)]. Since \( l_k = u_k - D/2^k \) and \( D/2^k \to 0 \), @thm-limit-laws-ordered-field (b) gives \( l_k \to s - 0 = s \).

**Step 5: \( s \) is the supremum.** (S1): let \( a \in A \). By (I1), \( a \le u_k \) for every \( k \), so \( a \le s \) by @prp-limit-preserves-order-ordered-field (b). So \( s \) is an upper bound of \( A \).

(S2): let \( b \) be an upper bound of \( A \), and suppose, for \( \rulename{\neg I} \), that \( b < s \). Then \( \varepsilon \coloneqq s - b > 0 \), and since \( l_k \to s \) there is \( K \) with \( \abs{l_k - s} < \varepsilon \) for \( k \ge K \); in particular \( l_K > s - \varepsilon = b \) (@prp-absolute-value-ordered-field (d)). By (I2), \( l_K \) is not an upper bound: some \( a \in A \) has \( a \not\le l_K \), that is, \( a > l_K \) by totality (@prp-ordered-field-halves (a)). Then \( a > l_K > b \), against \( b \) being an upper bound. So \( b < s \) is false, and \( s \le b \) by (O1).

By (S1) and (S2), \( s = \sup A \) (@fd2:def-order-supremum). Since \( A \) was an arbitrary non-empty subset bounded above, \( F \) is complete.
:::

The answer to the prompt: Step 3, and only the line @eq-bisection-archimedes. The rest of Step 3 is algebra in \( F \) and @lem-power-two-bound, which hold in every ordered field. Archimedes is what makes the halved lengths smaller than an arbitrary positive \( \varepsilon \); without it, \( D/2^k \) could stay above some positive element for every \( k \), and \( (u_k) \) need not be Cauchy.

Each hypothesis has one job. Archimedes makes \( (u_k) \) Cauchy (Step 3); Cauchy-completeness supplies the limit (Step 4); "non-empty" supplies a left end that is not an upper bound, and "bounded above" a right end that is one. The invariants (I1) and (I2) are spent in Step 5, one on each clause of the supremum.

::: {.warning}
**A false conclusion: "every Cauchy-complete ordered field is complete".** Run the bisection without Archimedes. Steps 1, 2, 4 and 5 never mention it; the unjustified line is @eq-bisection-archimedes, "\( D/\varepsilon < n \cdot 1_F \) for some \( n \)". In the non-Archimedean field \( \nQ(t) \) of @exm-rational-function-field it fails for \( D = 1 \) and \( \varepsilon = 1/t \): every \( 2^k = (2^k) \cdot 1 \) lies below \( t \), so \( 1/2^k > 1/t \) for every \( k \) (@prp-reciprocal-order (b)), and the bisection lengths never get below the tolerance \( 1/t \). (\( \nQ(t) \) is not Cauchy-complete either, so it shows only that the line fails, not that the conclusion does.)
:::

::: {.remark}
**Not proved here.** There are ordered fields that are Cauchy-complete and not Archimedean, for instance a field of formal Laurent series in a positive infinitesimal \( t \). So the conclusion of the warning is false, and the Archimedean hypothesis of @thm-cauchy-archimedean-lub cannot be dropped. This book does not prove that such a field exists, and nothing in it depends on one; *Analysis on the Real Line*, Chapter 11 returns to the question when it compares the forms of completeness.
:::

## The constructed reals

::: {#thm-reals-complete-ordered-field}
[The Constructed Reals Form a Complete Ordered Field]

The set \( \nR \) of @def-reals-cauchy-classes, with the operations of @def-reals-operations and the order of @def-reals-order, is a complete ordered field. The map \( \kappa \colon \nQ \to \nR \) of @def-rational-embedding is injective, preserves \( + \), \( \cdot \) and \( < \), and has dense image: between any two real numbers \( x < y \) there is \( \kappa(q) \) with \( q \in \nQ \).
:::

::: {.proof}
\( \nR \) is an ordered field by @thm-reals-ordered-field, Archimedean by @thm-constructed-reals-archimedean, and Cauchy-complete by @thm-constructed-reals-cauchy-complete. By @thm-cauchy-archimedean-lub it is complete. The statements about \( \kappa \) are @thm-rational-embedding (a), (b) (injectivity is part of (b)) and @thm-constructed-rationals-dense.
:::

This ends the construction begun with the axioms of set theory in Chapter 1: \( \nN \), then \( \nZ \) and \( \nQ \) as classes of pairs, now \( \nR \) as classes of Cauchy sequences. No property of \( \nR \) was assumed.

::: {.check}
Run the bisection of the proof of @thm-cauchy-archimedean-lub in \( \nR \) on \( A \coloneqq \{ q \in \nQ : q^2 < 2 \} \), viewed as a subset of \( \nR \), with \( a_0 = 1 \) and \( M = 2 \). List \( (l_k, u_k) \) for \( k = 0, 1, 2, 3 \).
:::

::: {.solution}
\( l_0 = a_0 - 1 = 0 \) and \( u_0 = 2 \). Two tests decide the midpoints. An element \( c > 0 \) with \( c^2 \ge 2 \) is an upper bound of \( A \): if some \( q \in A \) had \( q > c \), then \( q^2 > c^2 \ge 2 \) (@prp-ordered-ring-rules (g)), against \( q^2 < 2 \). An element exceeded by some member of \( A \) is not an upper bound; we use the member \( 7/5 \), which is in \( A \) because \( (7/5)^2 = 49/25 < 2 \).

- \( k = 0 \to 1 \): \( c = 1 \); \( 7/5 \in A \) and \( 7/5 > 1 \), so \( 1 \) is not an upper bound: \( (l_1, u_1) = (1, 2) \).
- \( k = 1 \to 2 \): \( c = 3/2 \); \( (3/2)^2 = 9/4 \ge 2 \), so \( 3/2 \) is an upper bound: \( (l_2, u_2) = (1, 3/2) \).
- \( k = 2 \to 3 \): \( c = 5/4 \); \( 7/5 \in A \) and \( 7/5 > 5/4 \), so \( 5/4 \) is not an upper bound: \( (l_3, u_3) = (5/4, 3/2) \).

So the pairs are \( (0, 2) \), \( (1, 2) \), \( (1, 3/2) \), \( (5/4, 3/2) \), and \( u_3 - l_3 = 1/4 = D/2^3 \) with \( D = 2 \), as (I3) says.
:::

## What we built, and what comes next

The table collects what the chapter proved about \( \nR \), beside the status of the same property in \( \nQ \).

| Property | In \( \nR \) | In \( \nQ \) |
|---|---|---|
| ordered field | yes: @thm-reals-ordered-field | yes: @thm-rationals-ordered-field |
| Archimedean | yes: @thm-constructed-reals-archimedean | yes: @thm-rationals-archimedean |
| an element whose square is \( 2 \) | yes: @exm-sqrt2-class | no: @thm-no-rational-square-two |
| Cauchy-complete | yes: @thm-constructed-reals-cauchy-complete | no: @thm-sqrt2-cauchy-no-rational-limit |
| complete | yes: @thm-reals-complete-ordered-field | no: @thm-rationals-gap-sqrt2 |

The first two rows are shared; the last three are what the construction was for.

Several chapters build on this one. Chapter 6 proves that any two complete ordered fields are isomorphic, by exactly one order-preserving field isomorphism; so "the" real numbers are well defined, and no theorem about them depends on how they were built. The optional Chapter 7 builds a complete ordered field from Dedekind cuts, sets of rationals instead of sequences, and by Chapter 6 it is a copy of this one. *Analysis on the Real Line*, Chapter 1 starts from the axioms of a complete ordered field; the theorem above gives those axioms a model, so they cannot contradict each other unless the set theory of Chapter 1, in which \( \nQ \) was built, already does. *Algebraic Preliminaries*, Chapter 1 builds the complex numbers on this \( \nR \). And *Metric and Topological Spaces*, Chapter 2 runs the construction of this chapter for an arbitrary metric space, as its completion.

::: {.second-reading title="History"}
Charles Méray published a construction of the irrational numbers from convergent sequences of rationals in 1869. Georg Cantor gave an equivalent construction from fundamental sequences, our Cauchy sequences, in 1872, the year in which Richard Dedekind published his construction by cuts.
:::

## Exercises

### A. Check your understanding

::: {#exr-the-least-upper-bound-property-a1}
[A1]

These questions are about the proof of @thm-cauchy-archimedean-lub and the definition of a complete ordered field.

::: {.enumerate options="label=(\alph*)"}
1. Where in the proof is the invariant "\( l_k \) is not an upper bound" used, and where "\( u_k \) is an upper bound"?
2. Why does the proof start with \( l_0 = a_0 - 1 \), and not with \( l_0 = a_0 \)?
3. State the idea of the proof in two sentences.
4. Write "\( F \) is complete" in symbols, and form its negation.
:::
:::

::: {.solution}
(a) "Not an upper bound", (I2), is used in Step 5 for (S2): a left end \( l_K \) above a supposed smaller upper bound \( b \) yields an element of \( A \) above \( b \). "Upper bound", (I1), is used in Step 5 for (S1): every element of \( A \) lies below every \( u_k \), hence below their limit. (Both are also carried through the induction of Step 2, which is what keeps them true.)

(b) The left end must **not** be an upper bound, and \( a_0 \) might be one: for \( A = \{a_0\} \), the element \( a_0 \) is an upper bound (even the supremum), and (I2) would fail at \( k = 0 \). Moving one unit left gives \( a_0 - 1 < a_0 \in A \), which is never an upper bound.

(c) Halve an interval repeatedly by a rule that keeps its right end an upper bound of \( A \) and its left end not one; Archimedes makes the lengths tend to \( 0 \), so the right ends are Cauchy and converge. Their limit is an upper bound because the right ends are, and it is the least one because the left ends, which are not upper bounds, converge to it too.

(d) With \( \mathrm{ub}(u) \) for \( \forall a \in A \ a \le u \), "complete" is the display in @def-complete-ordered-field. Its negation (@fd1:prp-quantifier-negation, @fd1:prp-bounded-quantifier-negation, @fd1:prp-negated-implication, and \( \neg(x \le y) \) as \( y < x \) by (O1)):
\[
\begin{aligned}
&\exists A \subseteq F \ \bigl( A \ne \emptyset \wedge \exists u \in F \ \mathrm{ub}(u) \wedge \forall s \in F \\
&\qquad \bigl( \exists a \in A \ s < a \ \vee \ \exists u \in F \ (\mathrm{ub}(u) \wedge u < s) \bigr) \bigr) .
\end{aligned}
\]
Some non-empty set bounded above defeats every candidate \( s \), by an element above it or an upper bound below it.
:::

### B. Practice

::: {#exr-the-least-upper-bound-property-b1}
[B1]

Prove that every non-empty subset \( A \subseteq \nR \) that is bounded below has an infimum in \( \nR \) (@fd2:def-order-supremum), and that \( \inf A = -\sup(-A) \), where \( -A \coloneqq \{ -a : a \in A \} \).
:::

::: {.solution}
Let \( b \) be a lower bound of \( A \). The set \( -A \) is non-empty, and \( -b \) is an upper bound of it: for \( a \in A \), \( b \le a \) gives \( -a \le -b \) (@prp-ordered-ring-rules (a)). By @thm-reals-complete-ordered-field, \( s \coloneqq \sup(-A) \) exists.

We show that \( -s \) is the infimum of \( A \). *Lower bound:* for \( a \in A \), \( -a \in -A \), so \( -a \le s \) and \( -s \le a \). *Greatest:* let \( c \) be a lower bound of \( A \). As for \( b \), \( -c \) is an upper bound of \( -A \), so \( s \le -c \) by (S2), that is, \( c \le -s \). Hence \( \inf A = -s = -\sup(-A) \).
:::

::: {#exr-the-least-upper-bound-property-b2}
[B2]

Let \( A \coloneqq \{ 1 - 1/(n + 1) : n \in \nN \} \subseteq \nR \). Prove that \( \sup A = 1 \), and decide whether \( 1 \in A \).
:::

::: {.solution}
*Upper bound.* \( 1/(n + 1) > 0 \) (@prp-reciprocal-order (a)), so \( 1 - 1/(n + 1) < 1 \) for every \( n \).

*Least.* Let \( b < 1 \). Then \( 1 - b \in \nR_{>0} \), and @cor-rational-epsilon-suffices (a) gives \( N \in \nZ_{>0} \) with \( 1/n < 1 - b \) for every \( n \ge N \). With \( n \coloneqq N \), the element \( 1 - 1/(N + 1) \) of \( A \) satisfies \( 1/(N + 1) < 1/N < 1 - b \), so \( 1 - 1/(N + 1) > b \), and \( b \) is not an upper bound. By (O1), every upper bound \( u \) satisfies \( u \ge 1 \).

So \( \sup A = 1 \), and \( 1 \notin A \), since every element of \( A \) is \( < 1 \). The supremum exists here without @thm-reals-complete-ordered-field: we exhibited it.
:::

### C. Going deeper

::: {#exr-the-least-upper-bound-property-c1}
[C1: Exit check: completeness from Cauchy completeness]

Let \( F \) be an ordered field that is Archimedean and Cauchy-complete. Prove that every non-empty subset of \( F \) that is bounded above has a supremum in \( F \), and name the line of your proof that uses the Archimedean property.
:::

::: {.solution}
Let \( A \ne \emptyset \) be bounded above; fix \( a_0 \in A \) and an upper bound \( M \). Put \( l_0 \coloneqq a_0 - 1 \) (not an upper bound, since \( a_0 > l_0 \)), \( u_0 \coloneqq M \) (an upper bound), \( D \coloneqq u_0 - l_0 > 0 \).

*Bisection.* By the recursion theorem, with the step "replace \( u \) by \( c = (l + u)/2 \) if \( c \) is an upper bound, else replace \( l \) by \( c \)", define \( (l_k, u_k) \). By induction: \( u_k \) is an upper bound, \( l_k \) is not, and \( u_k - l_k = D/2^k \). Hence \( l_k \) is non-decreasing, \( u_k \) is non-increasing, and \( 0 \le u_k - u_j \le D/2^k \) for \( j \ge k \).

*Cauchy.* Let \( \varepsilon \in F_{>0} \). **Archimedes** gives \( n \in \nN \) with \( D/\varepsilon < n \cdot 1_F \) (this is the line). For \( k \ge n \), \( 2^k \ge (k + 1) \cdot 1_F > n \cdot 1_F > D/\varepsilon \) by @lem-power-two-bound, so \( D/2^k < \varepsilon \), and \( \abs{u_j - u_k} < \varepsilon \) for \( j, k \ge n \).

*Limit.* Cauchy-completeness gives \( s \) with \( u_k \to s \); and \( l_k = u_k - D/2^k \to s \), since \( D/2^k \to 0 \).

*Supremum.* For \( a \in A \), \( a \le u_k \) for all \( k \), so \( a \le s \) (@prp-limit-preserves-order-ordered-field (b)). If an upper bound \( b \) had \( b < s \), some \( l_K > b \) (as \( l_k \to s \), with tolerance \( s - b \)); \( l_K \) is not an upper bound, so some \( a \in A \) exceeds \( l_K \), hence exceeds \( b \): impossible. So \( s \le b \) for every upper bound \( b \), and \( s = \sup A \).

**Marking scheme.** (10 points)
- 2: a starting left end that is not an upper bound and a right end that is, each justified (in particular \( a_0 - 1 \), not \( a_0 \)).
- 2: the bisection defined by a rule, with the invariants stated and proved by induction.
- 2: \( (u_k) \) Cauchy, with the Archimedean property named at the step where \( D/2^k \) is made smaller than \( \varepsilon \).
- 2: the limit \( s \) is an upper bound, by the order-preservation of limits.
- 2: \( s \) is the least upper bound, through \( l_k \to s \) and "\( l_k \) is not an upper bound".
Fatal errors (0 for the step): claiming \( s \in A \); "\( 1/2^k \to 0 \)" asserted in a general \( F \) without Archimedes; midpoints or points of \( A \) "chosen" at each step with no rule. A route through monotone convergence earns the Cauchy and limit points only if monotone convergence is first proved from Cauchy-completeness and Archimedes in \( F \).
:::

::: {#exr-the-least-upper-bound-property-c2}
[C2: The rationals are not complete, by bisection]

Run the bisection of the proof of @thm-cauchy-archimedean-lub inside \( F = \nQ \), on \( A \coloneqq \{ q \in \nQ : q^2 < 2 \} \) with \( a_0 = 1 \) and \( M = 2 \), so \( l_0 = 0 \) and \( D = 2 \).

::: {.enumerate options="label=(\alph*)"}
1. Explain why Steps 1–3 of that proof apply in \( \nQ \), so that \( (u_k) \) is Cauchy in \( \nQ \) and \( D/2^k \to 0 \) in \( \nQ \).
2. Prove: if \( A \) had a supremum \( s \) in \( \nQ \), then \( u_k \to s \) in \( \nQ \).
3. Prove that \( (u_k) \) has no limit in \( \nQ \). *(Show \( l_k^2 < 2 \le u_k^2 \).)*
4. Conclude that \( A \) has no supremum in \( \nQ \). Why is "\( (u_k) \) is Cauchy with no rational limit" not enough on its own for this?
5. In \( \nR \), show that \( u_k \to r \), the real number of @exm-sqrt2-class.
:::
:::

::: {.solution}
[Hint 1]

For (b), squeeze \( u_k - s \) between \( 0 \) and the length \( u_k - l_k \). For (c), the left ends are below some element of \( A \).
:::

::: {.solution}
[Hint 2]

For \( u_k^2 \ge 2 \) in (c): if \( u_k^2 < 2 \), find a rational \( h > 0 \) with \( (u_k + h)^2 < 2 \); try \( h \coloneqq \min\{1, (2 - u_k^2)/(2(2u_k + 1))\} \).
:::

::: {.solution}
(a) The proof states that Steps 1–3 use only that the field is an Archimedean ordered field, and \( \nQ \) is one (@thm-rationals-ordered-field, @thm-rationals-archimedean). @lem-power-two-bound holds in \( \nQ \) too. So the invariants (I1)–(I3) hold, \( (D/2^k) \) is null in \( \nQ \), and \( (u_k) \) is Cauchy in \( \nQ \). Step 4 is where the proof would need Cauchy-completeness, which \( \nQ \) lacks.

(b) Suppose \( s = \sup A \) in \( \nQ \). Each \( u_k \) is an upper bound (I1), so \( s \le u_k \) by (S2). Each \( l_k \) is not an upper bound (I2), so some \( a \in A \) has \( l_k < a \le s \). Hence \( 0 \le u_k - s < u_k - l_k = D/2^k \) for every \( k \). By the squeeze, @prp-limit-preserves-order-ordered-field (c), with lower sequence \( 0 \) and the null upper sequence \( (D/2^k) \), \( u_k - s \to 0 \), so \( u_k \to s \) (@prp-limit-null-shift-ordered-field).

(c) *Left ends.* \( l_k \ge l_0 = 0 \), since the left ends are non-decreasing (Step 2). By (I2) some \( a \in A \) has \( a > l_k \ge 0 \), so \( l_k^2 < a^2 < 2 \) (@prp-ordered-ring-rules (g)).

*Right ends.* \( u_k > l_k \ge 0 \). Suppose \( u_k^2 < 2 \), and let \( h \coloneqq \min\{1, (2 - u_k^2)/(2(2u_k + 1))\} \), a positive rational (\( 2u_k + 1 > 0 \)). Since \( h \le 1 \), \( h^2 \le h \), and
\[
\begin{aligned}
(u_k + h)^2 &= u_k^2 + 2u_k h + h^2 \le u_k^2 + (2u_k + 1) h \\
&\le u_k^2 + \frac{2 - u_k^2}{2} < 2 .
\end{aligned}
\]
So \( u_k + h \in A \) and \( u_k + h > u_k \), against (I1). Hence \( u_k^2 \ge 2 \).

*No limit.* Suppose \( u_k \to L \in \nQ \). Then \( l_k = u_k - D/2^k \to L \) (@thm-limit-laws-ordered-field (b)), and by the product law (c), \( u_k^2 \to L^2 \) and \( l_k^2 \to L^2 \). By @prp-limit-preserves-order-ordered-field (b), \( u_k^2 \ge 2 \) gives \( L^2 \ge 2 \), and \( l_k^2 < 2 \) gives \( L^2 \le 2 \). So \( L^2 = 2 \), against @thm-no-rational-square-two.

(d) By (b) and (c), a supremum \( s \in \nQ \) would be a rational limit of \( (u_k) \), and there is none. So \( A \) has no supremum in \( \nQ \): \( \nQ \) is not complete. A Cauchy sequence with no rational limit shows only that \( \nQ \) is not **Cauchy**-complete; part (b) is the link between the two properties, and it uses the invariants of the bisection. Section 2.6 proved the same conclusion (@thm-rationals-gap-sqrt2 (a)) directly, by improving each rational candidate; here a sequence finds the gap.

(e) Run the bisection in \( \nR \) on \( A \), viewed as a subset of \( \nR \). A rational \( c \) is an upper bound of \( A \) in \( \nQ \) if and only if it is one in \( \nR \) (\( \kappa \) preserves and reflects order, @thm-rational-embedding (b)), so the midpoint tests give the same answers, and the sequence \( (l_k, u_k) \) is the same. By the proof of @thm-cauchy-archimedean-lub in \( \nR \) (Steps 4 and 5), \( u_k \to \sup A \) in \( \nR \). It remains to see \( \sup A = r \). For \( q \in \nQ \): if \( q \ge r \), then \( q > 0 \) and \( q^2 \ge r^2 = 2 \) (@prp-ordered-ring-rules (g) in \( \nR \), with \( r > 0 \)), so \( q \notin A \); hence \( r \) is an upper bound. If \( t < r \) in \( \nR \), @thm-constructed-rationals-dense gives a rational \( q \) with \( \max\{t, 0\} < q < r \); then \( 0 < q < r \) gives \( q^2 < 2 \), so \( q \in A \) and \( q > t \): \( t \) is not an upper bound. So \( \sup A = r \), and \( u_k \to r \).

**Marking scheme.** (10 points)
- 2: (a), with the Archimedean property of \( \nQ \) cited and Cauchy-completeness located in Step 4.
- 3: (b), the two invariants used to get \( l_k < s \le u_k \), and the squeeze.
- 3: (c), both bounds \( l_k^2 < 2 \le u_k^2 \) justified (the second by a rational \( h \)), then the limit laws and @thm-no-rational-square-two.
- 2: (d), the conclusion, with the difference between "not Cauchy-complete" and "not complete" stated.
Part (e) is not marked. Fatal errors (0 for the step): using \( \sqrt 2 \) as a rational or as a real number in (b)–(d); concluding (d) from (c) alone.
:::

### R. Review

::: {#exr-the-least-upper-bound-property-r1}
[R1]

Let \( F \) be an ordered field, \( (a_n) \) a sequence in \( F \), and \( L \in F \) with \( L > 0 \) and \( a_n \to L \). Prove that \( a_n \ge L/2 \) for every sufficiently large \( n \).
:::

::: {.solution}
By @def-sequence-limit-ordered-field with \( \varepsilon \coloneqq L/2 \in F_{>0} \) (@prp-ordered-field-halves (b)), there is \( N \) with \( \abs{a_n - L} < L/2 \) for every \( n \ge N \). For such \( n \), @prp-absolute-value-ordered-field (d) gives \( -L/2 < a_n - L \), so \( a_n > L - L/2 = L/2 \); in particular \( a_n \ge L/2 \).

This is the second half of @lem-limit-bounded-away-ordered-field. It is also the shape of @thm-cauchy-not-null-sign, in the case where the limit is known: a sequence with a positive limit is eventually above a fixed positive element, which is what "positive" meant for Cauchy sequences in Section 5.3.
:::

::: {#exr-the-least-upper-bound-property-r2}
[R2]

On \( X \coloneqq \nZ \times \nZ_{>0} \), let \( (p, q) \sim (p', q') \) mean \( pq' = p'q \). Show that the condition "\( p \ge q \)" on a pair gives a well-defined property of classes: if \( (p, q) \sim (p', q') \), then \( p \ge q \) if and only if \( p' \ge q' \). Then show that "\( p \ge 2 \)" does **not** give a well-defined property of classes.
:::

::: {.solution}
These are the classes of @def-rationals-as-classes, and the move is **representatives, then independence**: a property stated on a representative is a property of the class only if equivalent representatives agree. By @thm-well-defined-on-classes (c), with \( S \coloneqq \{ (p, q) \in X : p \ge q \} \), it suffices to check one direction (the relation is symmetric).

Let \( pq' = p'q \) with \( q, q' > 0 \), and suppose \( p \ge q \). Multiplying by \( q' > 0 \) (@prp-ordered-ring-rules (c), or equality), \( pq' \ge qq' \), that is, \( p'q \ge q'q \). If \( p' < q' \), then \( p'q < q'q \) by @prp-ordered-ring-rules (c), since \( q > 0 \), a contradiction by (O1). So \( p' \ge q' \). In \( \nQ \), the property says \( [(p, q)] \ge 1 \), by the comparison formula of @thm-rationals-ordered-field (a).

"\( p \ge 2 \)" is not well defined: \( (1, 2) \sim (2, 4) \), since \( 1 \cdot 4 = 2 \cdot 2 \), but \( 1 \not\ge 2 \) while \( 2 \ge 2 \). One class, two verdicts: the hypothesis of @thm-well-defined-on-classes (c) fails. (The test "\( p \ge 1 \)" would pass, but only because for an integer it says \( p > 0 \), the positivity test of @def-rational-order.)
:::

::: {#exr-the-least-upper-bound-property-r3}
[R3]

Prove that \( \nR \) is uncountable. For \( s \in \{0, 1\}^{\nN} \), consider the rationals
\[
S_k(s) \coloneqq \sum_{i=0}^{k} \frac{2 s_i}{3^{i+1}} \qquad (k \in \nN) ,
\]
and show that \( s \mapsto [(S_k(s))_k] \) is an injection \( \{0, 1\}^{\nN} \to \nR \).
:::

::: {.solution}
*(i) The sums.* The powers \( 3^{i} \) are those of @def-naturals-in-ordered-field in \( \nQ \), with \( 3^{i+1} = 3^i \cdot 3 \). The sum is defined by @fd2:thm-recursion with \( X = \nQ \): \( S_0(s) \coloneqq 2s_0/3 \) and \( S_{k+1}(s) \coloneqq S_k(s) + 2s_{k+1}/3^{k+2} \).

*(ii) A tail bound.* For \( m \ge k \),
\[
0 \le S_m(s) - S_k(s) \le \frac{1}{3^{k+1}} - \frac{1}{3^{m+1}} .
\]{#eq-ternary-tail}
By @fd1:ax-induction on \( m - k \) (base \( P(0) \), \( m = k \): \( 0 \le 0 \le 0 \)): passing from \( m \) to \( m + 1 \) adds \( 2s_{m+1}/3^{m+2} \), which lies between \( 0 \) and \( 2/3^{m+2} \), and \( -1/3^{m+1} + 2/3^{m+2} = -3/3^{m+2} + 2/3^{m+2} = -1/3^{m+2} \).

So \( \abs{S_m(s) - S_k(s)} < 1/3^{k+1} \) for \( m \ge k \). Also \( 3^{k+1} \ge 2^{k+1} \ge (k + 2) \cdot 1 \): the first by induction (\( 3^0 = 2^0 \), and \( 3^{i+1} = 3^i \cdot 3 \ge 2^i \cdot 2 \) by @prp-ordered-field-halves (d), with \( 2^i > 0 \)), the second by @lem-power-two-bound with \( F = \nQ \). So \( 1/3^{k+1} < 1/(k + 1) \). Given \( \varepsilon \in \nQ_{>0} \), @cor-rationals-archimedean-epsilon gives \( N \in \nZ_{>0} \) with \( 1/n < \varepsilon \) for \( n \ge N \); for \( m, k \ge N \), say \( m \ge k \), \( \abs{S_m(s) - S_k(s)} < 1/(k + 1) < \varepsilon \). So \( (S_k(s))_k \in \sC \).

*(iii) Different sequences give different classes.* Let \( s \ne t \). The set \( \{ i \in \nN : s_i \ne t_i \} \) is non-empty and bounded below by \( 0 \), so it has a least element \( j \) (@prp-integer-least-element). Say \( s_j = 1 \) and \( t_j = 0 \). Since \( s_i = t_i \) for \( i < j \), induction gives \( S_{j-1}(s) = S_{j-1}(t) \) when \( j \ge 1 \), so \( S_j(s) - S_j(t) = 2/3^{j+1} \) (also when \( j = 0 \)). For \( k \ge j \), by @eq-ternary-tail applied to \( s \) and to \( t \),
\[
\begin{aligned}
S_k(s) - S_k(t) &= \frac{2}{3^{j+1}} + \bigl( S_k(s) - S_j(s) \bigr) - \bigl( S_k(t) - S_j(t) \bigr) \\
&\ge \frac{2}{3^{j+1}} + 0 - \frac{1}{3^{j+1}} = \frac{1}{3^{j+1}} .
\end{aligned}
\]
So \( S(s) - S(t) \) is eventually \( \ge \delta \coloneqq 1/3^{j+1} \in \nQ_{>0} \): it is positive (@def-positive-cauchy-sequence), so \( [S(t)] < [S(s)] \) (@def-reals-order, @def-reals-operations), and in particular \( [S(s)] \ne [S(t)] \). The map \( \Phi \colon s \mapsto [(S_k(s))_k] \) is injective.

*(iv) Uncountable.* If \( \nR \) were countable, there would be an injection \( g \colon \nR \to \nN \) (@fd2:thm-countable-characterizations, (i) \( \Rightarrow \) (ii)). Then \( g \circ \Phi \colon \{0, 1\}^{\nN} \to \nN \) would be injective (@fd2:thm-composition-injective-surjective (a)), so \( \{0, 1\}^{\nN} \) would be countable ((ii) \( \Rightarrow \) (i)), against @fd2:thm-binary-sequences-uncountable.

The method is that of *Sets, Relations, and Cardinality*, Chapter 3: an injection from a set known to be uncountable. (The route through @fd2:prp-card-le-surjection is not taken: its (\( \Leftarrow \)) direction uses choice.)
:::

::: {#exr-the-least-upper-bound-property-r4}
[R4]

Let \( x \in \nR \). Prove that there is a **strictly increasing** sequence \( (q_k) \) of rationals with \( q_k \to x \) in \( \nR \).
:::

::: {.solution}
*The tool* is @fd2:thm-recursion with a step given by a rule, on the set \( X \coloneqq \{ q \in \nQ : q < x \} \). Integer parts (@prp-integer-part-ordered-field with \( F = \nR \), unique) supply the rule.

*Start.* Let \( p \) be the integer part of \( x \), and \( q_0 \coloneqq p - 1 \). Then \( q_0 < p \le x \), so \( q_0 \in X \).

*Step.* For \( k \in \nN \) and \( q \in X \), let \( L \coloneqq \max\{q, x - 1/(k + 1)\} \), a real number with \( L < x \). Let \( n \) be the integer part of \( 2/(x - L) \), plus \( 1 \): a positive integer with \( n > 2/(x - L) \), so \( 2/n < x - L \) (@prp-reciprocal-order (b)). Let \( m \) be the integer part of \( n x \), and put \( g(k, q) \coloneqq (m - 1)/n \). From \( m \le nx < m + 1 \), dividing by \( n \),
\[
L < x - \frac{2}{n} < \frac{m - 1}{n} \le x - \frac{1}{n} < x .
\]
So \( g(k, q) \in X \), and \( g \colon \nN \times X \to X \) is a function: each step is a formula, made unambiguous by the uniqueness of integer parts. By @fd2:thm-recursion there is exactly one sequence with \( q_{k+1} = g(k, q_k) \).

*Properties.* By the display, \( q_{k+1} > L \ge q_k \), so the sequence is strictly increasing; and \( x - 1/(k + 1) \le L < q_{k+1} < x \), so \( \abs{q_{k+1} - x} < 1/(k + 1) \). Given \( \varepsilon \in \nR_{>0} \), @cor-rational-epsilon-suffices (a) gives \( N \) with \( 1/n < \varepsilon \) for \( n \ge N \); for \( k \ge N \), \( \abs{q_{k+1} - x} < 1/(k + 1) < \varepsilon \). So \( q_k \to x \).

*Why the look-alikes fail.* The terms of a representative of \( x \) converge to \( x \) (@thm-terms-converge-to-class) but need not increase. The approximants \( m_k/(k + 1) \) of Section 5.5 are \( \le x \) but not always strictly increasing (for \( x = 0 \) they are all \( 0 \)). The rational between two reals from the proof of @thm-constructed-rationals-dense is a midpoint of terms of representatives at thresholds fixed by \( \exists \)E: it is not given by a rule in the data \( (k, q) \), so it cannot serve as a recursion step. And "at each step take some rational between \( L \) and \( x \)" makes one pick for each \( k \) with no rule, an unflagged use of @fd2:ax-choice (compare @exm-representatives-need-choice).
:::

<!-- dependency ledger
def-complete-ordered-field (example): sup of {x < 0} is 0 in every ordered field; x < x/2 < 0 for x < 0 | prp-ordered-field-halves (b); inline
def-complete-ordered-field (claim): a set has at most one supremum | antisymmetry of <= (fd2:def-partial-order (PO2), prp-ordered-field-halves (a)); inline
lem-power-two-bound (proof): 0 + 1 = 1 and 1 + 1 = 2 in N; k + 1 >= 1 | def-omega-arithmetic (c), thm-omega-order (d), cited (the blueprint's "F3.1 (promised)" source: F3.1 is now approved)
lem-power-two-bound (proof): y(1 + 1) = y + y | (F9), (F7) of def-commutative-ring-and-field
thm-cauchy-archimedean-lub (proof): c - l = u - c = (u - l)/2; (D/2^k)/2 = D/2^{k+1} | lem-field-fraction-rules (b), def-naturals-in-ordered-field (b); inline
thm-cauchy-archimedean-lub (proof): induction for the invariants and for monotonicity; every j >= k is k + i | fd1:ax-induction via cor-omega-identification (b); prp-omega-order-arithmetic (a), cited
thm-cauchy-archimedean-lub (proof): k >= n implies k * 1_F >= n * 1_F | prp-naturals-in-ordered-field (b), cited
thm-cauchy-archimedean-lub (proof): "not an upper bound" gives a in A with a > l_K | fd1:prp-bounded-quantifier-negation and totality (prp-ordered-field-halves (a)); inline
thm-cauchy-archimedean-lub (claim): Q(t) has 2^k < t for every k | exm-rational-function-field (school polynomial algebra; warning only, nothing depends on it)
thm-cauchy-archimedean-lub (claim): Cauchy-complete non-Archimedean fields exist (Laurent series) | not proved here; marked so in the text; nothing depends on it; an1 Ch 11 (prose pointer)
thm-reals-complete-ordered-field (claim): forward pointers to F3.4, F3.3, AN1.1, AN1.11, F4.1, AN2.2 | prose pointers only; nothing depends on them
thm-reals-complete-ordered-field (claim): history (Meray 1869, Cantor 1872, Dedekind 1872) | standard history; not used
thm-reals-complete-ordered-field (solution): quick check, bisection pairs (0,2), (1,2), (1,3/2), (5/4,3/2); 49/25 < 2 <= 9/4 | verify/ch05/thm-reals-complete-ordered-field.py
exr-the-least-upper-bound-property-c2 (solution): (u + h)^2 <= u^2 + (2u + 1)h for 0 < h <= 1, u >= 0 | inline; verify/ch05/exr-the-least-upper-bound-property-c2.py
exr-the-least-upper-bound-property-r2 (solution): the comparison formula reads p/q >= 1 as p >= q | thm-rationals-ordered-field (a), cited
exr-the-least-upper-bound-property-r3 (solution): tail bound and the gap 1/3^{j+1}; 3^k >= 2^k | inline induction; verify/ch05/exr-the-least-upper-bound-property-r3.py
exr-the-least-upper-bound-property-r3 (solution): {0,1}^N indexed by omega | cor-omega-identification citing rule, group (i) (fd2:thm-binary-sequences-uncountable, fd2:thm-countable-characterizations)
exr-the-least-upper-bound-property-r4 (solution): L < x - 2/n < (m - 1)/n <= x - 1/n < x | inline; verify/ch05/exr-the-least-upper-bound-property-r4.py
-->
