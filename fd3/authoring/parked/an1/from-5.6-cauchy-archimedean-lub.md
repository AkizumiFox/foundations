# Parked: from old Section 5.6, from Cauchy-complete to complete

<!-- Parked from fd3 (fd3/authoring/design/layout-proposal.md §4, approved 2026-10-26). Not part of any book's src; nothing builds or scans it.
Old section: fd3 5.6 The Real Numbers Form a Complete Ordered Field (part) (06-the-least-upper-bound-property.md)
Labels: thm-cauchy-archimedean-lub, eq-bisection-tail, eq-bisection-archimedes
Intended home: AN1.11, Step 5 of thm-completeness-equiv ((CC) + (A) ⇒ (LUB))
-->

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
Let \( k \ge n \). By @lem-power-two-bound and @prp-naturals-in-ordered-field (b), \( 2^k \ge (k + 1) \cdot 1_F > k \cdot 1_F \ge n \cdot 1_F > D/\varepsilon > 0 \). By @prp-reciprocal-order (b), \( 1/2^k < (D/\varepsilon)^{-1} = \varepsilon/D \) (@lem-field-fraction-rules (a)), and multiplying by \( D > 0 \) (@prp-ordered-ring-rules (c)) gives \( D/2^k < \varepsilon \). So \( \abs{D/2^k - 0} < \varepsilon \) for every \( k \ge n \): the sequence \( (D/2^k)_k \) is null.

Consequently \( (u_k) \) is Cauchy in \( F \): for \( \varepsilon \) and \( n \) as above and \( j, k \ge n \), say \( j \ge k \) (the other case is symmetric), @eq-bisection-tail gives \( \abs{u_j - u_k} = \abs{u_k - u_j} = u_k - u_j \le D/2^k < \varepsilon \) (@prp-absolute-value-ordered-field (b), @def-absolute-value-ordered-field).

Steps 1–3 use only that \( F \) is an Archimedean ordered field. Step 4 is the only one that uses Cauchy-completeness.

**Step 4: the limit.** Since \( F \) is Cauchy-complete, \( (u_k) \) converges; fix \( s \in F \) with \( u_k \to s \) [\( \rulename{\exists E} \)]. Since \( l_k = u_k - D/2^k \) and \( D/2^k \to 0 \), @thm-limit-laws-ordered-field (b) gives \( l_k \to s - 0 = s \).

**Step 5: \( s \) is the supremum.** (S1): let \( a \in A \). By (I1), \( a \le u_k \) for every \( k \), so \( a \le s \) by @prp-limit-preserves-order-ordered-field (b). So \( s \) is an upper bound of \( A \).

(S2): let \( b \) be an upper bound of \( A \), and suppose, for \( \rulename{\neg I} \), that \( b < s \). Then \( \varepsilon \coloneqq s - b > 0 \), and since \( l_k \to s \) there is \( K \) with \( \abs{l_k - s} < \varepsilon \) for \( k \ge K \); in particular \( l_K > s - \varepsilon = b \) (@prp-absolute-value-ordered-field (d)). By (I2), \( l_K \) is not an upper bound: some \( a \in A \) has \( a \not\le l_K \) (@fd1:prp-bounded-quantifier-negation (a)), that is, \( a > l_K \) by totality (@prp-ordered-field-halves (a)). Then \( a > l_K > b \), against \( b \) being an upper bound. So \( b < s \) is false, and \( s \le b \) by (O1).

By (S1) and (S2), \( s = \sup A \) (@fd2:def-order-supremum). Since \( A \) was an arbitrary non-empty subset bounded above, \( F \) is complete.
:::

The answer to the prompt: Step 3, and only the line @eq-bisection-archimedes. The rest of Step 3 is algebra in \( F \) and @lem-power-two-bound, which hold in every ordered field. Archimedes is what makes the halved lengths smaller than an arbitrary positive \( \varepsilon \); without it, \( D/2^k \) could stay above some positive element for every \( k \), and \( (u_k) \) need not be Cauchy.

Each hypothesis has one job. Archimedes makes \( (u_k) \) Cauchy (Step 3); Cauchy-completeness supplies the limit (Step 4); "non-empty" supplies a left end that is not an upper bound, and "bounded above" a right end that is one. The invariants (I1) and (I2) are spent in Step 5, one on each clause of the supremum.

::: {.warning}
**A false conclusion: "every Cauchy-complete ordered field is complete".** Run the bisection without Archimedes. Steps 1, 2, 4 and 5 never mention it; the unjustified line is @eq-bisection-archimedes, "\( D/\varepsilon < n \cdot 1_F \) for some \( n \)". In the non-Archimedean field \( \nQ(t) \) of @exm-rational-function-field it fails for \( D = 1 \) and \( \varepsilon = 1/t \): every \( 2^k = (2^k) \cdot 1 \) lies below \( t \), so \( 1/2^k > 1/t \) for every \( k \) (@prp-reciprocal-order (b)), and the bisection lengths never get below the tolerance \( 1/t \). (It shows only that the line fails, not that the conclusion does.)
:::

::: {.remark}
**Not proved here.** There are ordered fields that are Cauchy-complete and not Archimedean, for instance a field of formal Laurent series in a positive infinitesimal \( t \). So the conclusion of the warning is false, and the Archimedean hypothesis of @thm-cauchy-archimedean-lub cannot be dropped. This book does not prove that such a field exists, and nothing in it depends on one; *Analysis on the Real Line*, Chapter 11 returns to the question when it compares the forms of completeness.
:::

<!-- dependency ledger
thm-cauchy-archimedean-lub (proof): c - l = u - c = (u - l)/2; (D/2^k)/2 = D/2^{k+1}; D/2^k > 0; D(eps/D) = eps | lem-field-fraction-rules (b), def-naturals-in-ordered-field (b), prp-reciprocal-order (a), (O4), (F5), (F6); inline
thm-cauchy-archimedean-lub (proof): induction for the invariants and for monotonicity; every j >= k is k + i | fd1:ax-induction via cor-omega-identification (b); prp-omega-order-arithmetic (a), cited
thm-cauchy-archimedean-lub (proof): k >= n implies k * 1_F >= n * 1_F | prp-naturals-in-ordered-field (b), cited
thm-cauchy-archimedean-lub (proof): "not an upper bound" gives a in A with a > l_K | fd1:prp-bounded-quantifier-negation (a) and totality (prp-ordered-field-halves (a)); cited
thm-cauchy-archimedean-lub (claim): Q(t) has 2^k < t for every k | exm-rational-function-field (school polynomial algebra; warning only, nothing depends on it)
thm-cauchy-archimedean-lub (claim): Cauchy-complete non-Archimedean fields exist (Laurent series) | not proved here; marked so in the text; nothing depends on it; an1 Ch 11 (prose pointer)
-->
