# Least Upper Bounds

Section 5.4 made \( \nR \) an Archimedean ordered field with \( \nQ \) dense in it. *Analysis on the Real Line*, Chapter 1 starts from a property of sets: every non-empty set of real numbers that is bounded above has a least upper bound. In \( \nQ \) it fails (@thm-rationals-gap-sqrt2). This section names the property for an arbitrary ordered field and proves that the constructed \( \nR \) has it. The proof halves intervals with rational ends. Their right ends form a Cauchy sequence of rationals, which is a real number by definition, and that number is the least upper bound. The sequence form of completeness, that every Cauchy sequence of reals converges, is proved from this one in *Analysis on the Real Line*, Chapter 4.

Throughout, \( F \) is an ordered field (@def-ordered-ring-and-field). Its order \( \le \) is a total order (@prp-ordered-field-halves (a)), so the words "upper bound", "bounded above" and "supremum" of *Sets and Functions*, Section 5.3 apply to subsets of \( F \) (@fd2:def-order-bounds, @fd2:def-order-supremum). When \( F = \nR \), we keep the identification of Section 5.4, writing \( q \) for \( \kappa(q) \).

## Complete ordered fields

Section 3.3 found a gap in \( \nQ \) without any sequence: the set \( A = \{ x \in \nQ : x^2 < 2 \} \) is non-empty and bounded above in \( \nQ \), and among its rational upper bounds there is no least one (@thm-rationals-gap-sqrt2). The upper bounds crowd down toward a place where \( \nQ \) has no element. A field without such gaps is one in which every set that could have a least upper bound does have one.

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

**Well-definedness.** A set has at most one supremum, since a supremum is a least element of the set of upper bounds (*Sets and Functions*, Section 5.3, the remark after @fd2:def-order-supremum, by @fd2:prp-greatest-unique). So "the supremum of \( A \)", written \( \sup A \), names one element when it exists.

**Examples.**

*The negative elements.* In every ordered field, \( A \coloneqq \{ x \in F : x < 0 \} \) has supremum \( 0 \). It is non-empty (\( -1 \in A \)). The element \( 0 \) is an upper bound. If an upper bound \( b \) had \( b < 0 \), then \( b < b/2 < 0 \) (@prp-ordered-field-halves (b)), so \( b/2 \in A \) lies above \( b \), which is impossible. So every upper bound \( b \) satisfies \( b \ge 0 \), and \( \sup A = 0 \notin A \). No completeness was needed: some sets have suprema in every ordered field.

*The rationals.* \( \nQ \) is **not** complete: @thm-rationals-gap-sqrt2 exhibits a non-empty subset bounded above with no supremum in \( \nQ \).

*The constructed reals.* \( \nR \) is complete; this is the main theorem of the section.

::: {.second-reading title="A degenerate case, and non-examples by minimal change"}
*A singleton.* \( \sup \{a\} = a \), in every ordered field, since a greatest element is the supremum (the same remark of *Sets and Functions*, Section 5.3). This degenerate case matters below: a set may be bounded above by its own element.

Drop "non-empty": the empty set is bounded above by every element of \( F \), so its upper bounds are all of \( F \), and \( F \) has no least element (\( x - 1 < x \)). Drop "bounded above": \( F \) itself has no upper bound (\( x < x + 1 \)), so no supremum. With either clause removed, no ordered field at all would be complete.
:::

**Why this definition.** It asks about suprema, not maxima: the set of negative elements has no greatest element in any ordered field, since \( x < x/2 < 0 \) for \( x < 0 \), and asking for maxima would make no field complete. It asks about sets, not sequences, the form *Analysis on the Real Line*, Chapter 1 takes as its axiom. "Complete" alone always means this property; the sequence property is "Cauchy-complete".

::: {.warning}
The supremum of a set is an upper bound **not necessarily in the set**, and "complete" is not "every non-empty bounded set has a **largest** element": the set of negative elements above has supremum \( 0 \) and no largest element. A proof that ends "so \( \sup A \in A \)" needs a reason, such as \( A \) being finite.
:::

So \( \nQ \) is not complete. The rest of the section proves that \( \nR \) is.

## Powers of two in an ordered field

The bisection below halves an interval at each step, so after \( k \) steps its length is the first length divided by \( 2^k \). We need \( 2^k \) to grow at least as fast as \( k + 1 \), here in \( \nQ \); the induction is the one for \( 10^k \) in Section 5.1.

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
We use @fd1:ax-induction, read on \( \nN \) through @cor-omega-identification (b), for \( P(k) \): \( (2 \cdot 1_F)^k \ge (k + 1) \cdot 1_F \).

*Base \( P(0) \).* \( (2 \cdot 1_F)^0 = 1_F \) by @def-naturals-in-ordered-field (b), and \( (0 + 1) \cdot 1_F = 1 \cdot 1_F = 0 \cdot 1_F + 1_F = 1_F \) by (a) of that definition, since \( 0 + 1 = 1 \) (@def-omega-arithmetic (c)). Equality holds.

*Step.* Assume \( P(k) \), and let \( y \coloneqq (k + 1) \cdot 1_F \). By @def-naturals-in-ordered-field (a) and @def-omega-arithmetic (c), \( 2 \cdot 1_F = 1 \cdot 1_F + 1_F = 1_F + 1_F \), which is positive (@prp-ordered-field-halves (b)). By @def-naturals-in-ordered-field (b), \( P(k) \), and @prp-ordered-ring-rules (c) (or equality, if \( P(k) \) holds with equality),
\[
(2 \cdot 1_F)^{k+1} = (2 \cdot 1_F)^k (2 \cdot 1_F) \ge y (1_F + 1_F) = y + y ,
\]
the last step by distributivity (F9) and (F7). Since \( k + 1 \ge 1 \) (@thm-omega-order (d)), @prp-naturals-in-ordered-field (b) gives \( y \ge 1_F \), so \( y + y \ge y + 1_F \) (@prp-ordered-ring-rules (b)). Finally \( y + 1_F = ((k + 1) + 1) \cdot 1_F \) by @def-naturals-in-ordered-field (a). Hence \( (2 \cdot 1_F)^{k+1} \ge ((k + 1) + 1) \cdot 1_F \), which is \( P(k + 1) \).

The last sentence of the lemma follows, since \( (k + 1) \cdot 1_F \ge 1_F > 0 \) (@prp-naturals-in-ordered-field (b), as \( k + 1 \ge 1 \)).
:::

From here on, \( 2^k \) means \( (2 \cdot 1_F)^k \). By @prp-naturals-in-ordered-field (c) it equals \( (2^k) \cdot 1_F \), the multiple of \( 1_F \) by the natural number \( 2^k \), so the two readings agree; the proofs below use only the power in \( F \) and the lemma. Since \( 2^k > 0 \), the quotient \( D/2^k \) is defined for every \( D \in F \).

## Bisection with rational ends

Section 3.3 found the gap of \( \nQ \) by improving each rational candidate. In \( \nR \) we trap the candidate instead. Start with a rational that is an upper bound of \( A \) and one that is not, and halve: keep the half whose right end is still an upper bound and whose left end is still not. The ends stay rational, and the intervals shrink, so the right ends form a Cauchy sequence of rationals: by definition, a real number. *Before reading on: which two properties of that number are needed, and which end of the intervals gives each?*

::: {#thm-reals-complete-ordered-field}
[The Constructed Reals Form a Complete Ordered Field]

The set \( \nR \) of @def-reals-cauchy-classes, with the operations of @def-reals-operations and the order of @def-reals-order, is a complete ordered field. The map \( \kappa \colon \nQ \to \nR \) of @def-rational-embedding is injective, preserves \( + \), \( \cdot \) and \( < \), and has dense image: between any two real numbers \( x < y \) there is \( \kappa(q) \) with \( q \in \nQ \).
:::

::: {.idea}
[Scratch work]

A real number is a class of members of \( \sC \), so the supremum should arrive as the class of a Cauchy sequence of rationals. The bisection supplies two: right ends \( u_k \), each an upper bound of \( A \), and left ends \( l_k \), none an upper bound, with the gap halved at each step. The invariants are proved by induction, finding the claim for \( k \) inside the claim for \( k + 1 \) (@fd2:exm-method-induction-step).

| Givens | Goal |
|---|---|
| \( A \subseteq \nR \) non-empty, bounded above | \( s \in \nR \) with (S1) and (S2) |
| a real number is a class \( [(u_k)] \), \( (u_k) \in \sC \) | rationals \( u_k \), upper bounds, and \( l_k \), not upper bounds, closing in |
| a step rule on the midpoint; induction keeps (I1)–(I3), \( u_k - l_k = D/2^k \) | \( (u_k), (l_k) \in \sC \), \( (l_k) \sim (u_k) \): \( s \coloneqq [(u_k)] = [(l_k)] \) |
| \( s < a \in A \): a rational \( q \) between; \( q - u_k \) eventually \( \ge \delta \) | some \( u_k < a \), against (I1): (S1) |
| \( b < s \), \( b \) an upper bound: a rational \( q \) between; \( l_k - q \) eventually \( \ge \delta \) | some \( l_k > b \), against (I2): (S2) |

Both clauses of the supremum are proved by contradiction, and each spends one invariant.
:::

::: {.proof}
\( \nR \) is an ordered field by @thm-reals-ordered-field. Let \( A \subseteq \nR \) be non-empty and bounded above.

**Step 1: rational ends.** Fix \( a_0 \in A \) and an upper bound \( M \) of \( A \). By @thm-constructed-rationals-dense, fix \( l_0, u_0 \in \nQ \) with \( a_0 - 1 < l_0 < a_0 \) and \( M < u_0 < M + 1 \). Then \( l_0 \) is not an upper bound, since \( a_0 \in A \) and \( a_0 > l_0 \); \( u_0 \) is one, since \( a \le M < u_0 \) for every \( a \in A \); and \( D \coloneqq u_0 - l_0 \in \nQ_{>0} \), since \( l_0 < a_0 \le M < u_0 \). Each of these is one object, fixed once.

**Step 2: the bisection.** Define \( g \colon \nN \times (\nQ \times \nQ) \to \nQ \times \nQ \) by
\[
g\bigl(k, (l, u)\bigr) \coloneqq
\begin{cases}
(l, c) & \text{if } c \text{ is an upper bound of } A , \\
(c, u) & \text{otherwise,}
\end{cases}
\qquad c \coloneqq \frac{l + u}{2} \in \nQ .
\]
For each input exactly one case applies, so \( g \) is a function, given by a rule. By @fd2:thm-recursion (read on \( \nN \) through @cor-omega-identification (b)), with \( X = \nQ \times \nQ \) and starting value \( (l_0, u_0) \), there is exactly one sequence \( k \mapsto (l_k, u_k) \) with \( (l_{k+1}, u_{k+1}) = g(k, (l_k, u_k)) \) for every \( k \).

We prove by induction on \( k \) that, for every \( k \in \nN \):

::: {.enumerate options="label=(I\arabic*)"}
1. \( u_k \) is an upper bound of \( A \);
2. \( l_k \) is not an upper bound of \( A \);
3. \( u_k - l_k = D/2^k \), in \( \nQ \).
:::

The base is Step 1, with \( D/2^0 = D/1 = D \). Suppose (I1)–(I3) hold for \( k \), and let \( c \coloneqq (l_k + u_k)/2 \). Then \( c - l_k = u_k - c = (u_k - l_k)/2 = D/(2^k \cdot 2) = D/2^{k+1} \), by field arithmetic in \( \nQ \) (@lem-field-fraction-rules (b)) and @def-naturals-in-ordered-field (b). If \( c \) is an upper bound, then \( (l_{k+1}, u_{k+1}) = (l_k, c) \): the right end \( c \) is an upper bound, the left end \( l_k \) is not, by (I2), and \( c - l_k = D/2^{k+1} \). Otherwise \( (l_{k+1}, u_{k+1}) = (c, u_k) \): the left end \( c \) is not an upper bound, the right end \( u_k \) is, by (I1), and \( u_k - c = D/2^{k+1} \). This proves (I1)–(I3) for \( k + 1 \).

By (I3), \( u_k - l_k = D/2^k > 0 \), so \( l_k < c < u_k \) (@prp-ordered-field-halves (b)); in either case \( l_k \le l_{k+1} \) and \( u_{k+1} \le u_k \). By induction on \( i \), \( l_k \le l_{k+i} \) and \( u_{k+i} \le u_k \) for every \( i \in \nN \), and every \( j \ge k \) is \( k + i \) for some \( i \) (@prp-omega-order-arithmetic (a)). So for \( j \ge k \), \( l_k \le l_j < u_j \le u_k \), and therefore
\[
\begin{aligned}
0 &\le u_k - u_j \le \frac{D}{2^k} , \\
0 &\le l_j - l_k \le \frac{D}{2^k}
\end{aligned}
\qquad (j \ge k) .
\]{#eq-rational-bisection-tail}

**Step 3: a real number.** Let \( \varepsilon \in \nQ_{>0} \). By @thm-rationals-archimedean there is \( n \in \nN \) with \( D/\varepsilon < n \). Let \( k \ge n \). By @lem-power-two-bound with \( F = \nQ \) and @prp-naturals-in-ordered-field (b), \( 2^k \ge k + 1 > n > D/\varepsilon > 0 \), so \( 1/2^k < \varepsilon/D \) (@prp-reciprocal-order (b)), and multiplying by \( D > 0 \) (@prp-ordered-ring-rules (c)) gives \( D/2^k < \varepsilon \). So \( (D/2^k)_k \) is null in \( \nQ \). For \( j, k \ge n \), say \( j \ge k \), @eq-rational-bisection-tail gives \( \abs{u_j - u_k} = u_k - u_j \le D/2^k < \varepsilon \) (@prp-absolute-value-ordered-field (b), @def-absolute-value-ordered-field); so \( (u_k) \in \sC \). Then \( (l_k) = (u_k - D/2^k)_k \in \sC \) (@thm-cauchy-algebra-ordered-field (a), (b)), and \( (u_k - l_k)_k = (D/2^k)_k \) is null, so \( (u_k) \sim (l_k) \) (@def-cauchy-equivalent). Let \( s \coloneqq [(u_k)] \); then \( s = [(l_k)] \) (@fd2:thm-classes-partition (b)).

**Step 4: (S1).** Let \( a \in A \), and suppose \( s < a \). By @thm-constructed-rationals-dense, fix \( q \in \nQ \) with \( s < q < a \). By @def-reals-operations, \( q - s = [(q - u_k)_k] \), and \( q - s \in P \) (@def-reals-order); so \( (q - u_k)_k \) is positive, since every representative of an element of \( P \) is (@prp-positivity-well-defined). Fix \( \delta \in \nQ_{>0} \) and \( N \in \nN \) with \( q - u_k \ge \delta \) for every \( k \ge N \). Then \( u_N \le q - \delta < q \), so \( u_N < q < a \) (@thm-rational-embedding (b)), and \( a \le u_N \) fails, against (I1). So \( s < a \) is false, and \( a \le s \) by (O1). Hence \( s \) is an upper bound of \( A \).

**Step 5: (S2).** Let \( b \) be an upper bound of \( A \), and suppose \( b < s \). Fix \( q \in \nQ \) with \( b < q < s \). Now read \( s \) through the left ends: \( s - q = [(l_k - q)_k] \in P \), so, as in Step 4, there are \( \delta \in \nQ_{>0} \) and \( N \in \nN \) with \( l_k - q \ge \delta \) for every \( k \ge N \); in particular \( l_N > q > b \). By (I2), \( l_N \) is not an upper bound: some \( a \in A \) has \( a \not\le l_N \) (@fd1:prp-bounded-quantifier-negation), that is, \( a > l_N \) by totality (@prp-ordered-field-halves (a)). Then \( a > l_N > b \), against \( b \) being an upper bound. So \( b < s \) is false, and \( s \le b \) by (O1).

By (S1) and (S2), \( s = \sup A \) (@fd2:def-order-supremum). Since \( A \) was an arbitrary non-empty subset bounded above, \( \nR \) is complete. The statements about \( \kappa \) are @thm-rational-embedding (a), (b) (injectivity is part of (b)) and @thm-constructed-rationals-dense.
:::

The answer to the prompt: (S1) is read off the right ends and spends (I1); (S2) is read off the left ends and spends (I2); \( (l_k) \sim (u_k) \) is what lets one number be read both ways. Archimedes enters twice, never as an assumption: the Archimedean property of \( \nQ \) (Chapter 3) makes \( D/2^k \) small in Step 3, and density of \( \nQ \) in \( \nR \), which came from the Archimedean property of \( \nR \), supplies the rationals of Steps 1, 4 and 5. One more consequence: for \( j \ge k \), \( u_j \le u_k \) and \( l_j \ge l_k \), so @lem-termwise-order gives \( l_k \le s \le u_k \) for every \( k \). The number \( s \) lies in every interval of the bisection.

::: {.remark}
Steps 2–5 use only that \( l_0 \) and \( u_0 \) are rational, that \( l_0 \) is not an upper bound of \( A \) and that \( u_0 \) is one (which forces \( D > 0 \)); Step 1 merely shows that such a pair exists. So the bisection may start from any such pair.
:::

::: {#exm-method-bisect-invariant}
[Method: bisect and keep the invariant]

**Template.** (1) Start with two points on opposite sides of a test (here: not an upper bound, an upper bound). (2) Define the step by a rule that applies the test to the midpoint and keeps one end on each side; the recursion theorem then builds the sequence with no choice. (3) Prove the invariants and the length \( D/2^k \) by induction. (4) Make \( D/2^k \) small, by Archimedes, to get Cauchy sequences. (5) Spend one invariant on each half of the conclusion.

**When to use it.** The point you want is the boundary between two kinds of points, and one test decides the kind of each point.

**The usual failure.** A step that "takes some point of \( A \) above the midpoint" with no rule. A starting left end that may itself be an upper bound (\( l_0 = a_0 \) for \( A = \{a_0\} \)). Asserting \( 1/2^k \to 0 \) without Archimedes.
:::

::: {.check}
Run Step 2 on \( A \coloneqq \{ q \in \nQ : q^2 < 2 \} \), viewed as a subset of \( \nR \), from \( l_0 = 0 \), \( u_0 = 2 \) (\( 0 \) is not an upper bound, as \( 1 \in A \); \( 2 \) is one). List \( (l_k, u_k) \) for \( k = 0, 1, 2, 3 \). This start was not obtained by Step 1; by the remark after the proof, it is allowed.
:::

::: {.solution}
\( (l_0, u_0) = (0, 2) \). Two tests decide the midpoints. An element \( c > 0 \) with \( c^2 \ge 2 \) is an upper bound of \( A \): if some \( q \in A \) had \( q > c \), then \( q^2 > c^2 \ge 2 \) (@prp-ordered-ring-rules (g)), against \( q^2 < 2 \). An element exceeded by some member of \( A \) is not an upper bound; we use the member \( 7/5 \), which is in \( A \) because \( (7/5)^2 = 49/25 < 2 \).

- \( k = 0 \to 1 \): \( c = 1 \); \( 7/5 \in A \) and \( 7/5 > 1 \), so \( 1 \) is not an upper bound: \( (l_1, u_1) = (1, 2) \).
- \( k = 1 \to 2 \): \( c = 3/2 \); \( (3/2)^2 = 9/4 \ge 2 \), so \( 3/2 \) is an upper bound: \( (l_2, u_2) = (1, 3/2) \).
- \( k = 2 \to 3 \): \( c = 5/4 \); \( 7/5 \in A \) and \( 7/5 > 5/4 \), so \( 5/4 \) is not an upper bound: \( (l_3, u_3) = (5/4, 3/2) \).

So the pairs are \( (0, 2) \), \( (1, 2) \), \( (1, 3/2) \), \( (5/4, 3/2) \), and \( u_3 - l_3 = 1/4 = D/2^3 \) with \( D = 2 \), as (I3) says.
:::

The bisection names \( \sup A \) as a class. For this set a second name is already known: Section 5.4 built a real number whose square is \( 2 \) from the Newton sequence. The next example shows that the two names agree.

::: {#exm-bisection-square-root-two}
[Bisection Finds the Square Root of Two]

Let \( A \) and \( (l_k, u_k) \) be as in the Quick check, and let \( r \) be the class of the Newton sequence (@exm-sqrt2-class). Show that a rational \( c \ge 0 \) is an upper bound of \( A \) if and only if \( c \ge r \). Deduce that \( l_k < r \le u_k \) for every \( k \), and that \( [(u_k)] = r \).
:::

::: {.solution}
Recall \( r > 0 \) and \( r^2 = 2 \) (@exm-sqrt2-class).

\( (\Leftarrow) \) Let \( c \ge r \), and suppose some \( q \in A \) has \( q > c \). Then \( q > r > 0 \), so \( q^2 > r^2 = 2 \) (@prp-ordered-ring-rules (g) in \( \nR \)), against \( q^2 < 2 \). So \( c \) is an upper bound.

\( (\Rightarrow) \) Let \( 0 \le c < r \). By @thm-constructed-rationals-dense there is \( q \in \nQ \) with \( c < q < r \). Then \( 0 < q < r \) gives \( q^2 < r^2 = 2 \), so \( q \in A \), and \( q > c \): \( c \) is not an upper bound.

Every end is \( \ge 0 \): \( l_0 = 0 \), the left ends never decrease, and \( u_k > l_k \). So (I1) and (I2) read \( r \le u_k \) and \( l_k < r \).

By Steps 3–5 of the proof of @thm-reals-complete-ordered-field, which apply to this start by the remark after the proof, \( [(u_k)] = \sup A \). And \( r = \sup A \): it is an upper bound, by the \( (\Leftarrow) \) argument with \( c \) replaced by \( r \); and if \( t < r \), density gives \( q \in \nQ \) with \( \max\{t, 0\} < q < r \), so \( q \in A \) and \( q > t \), and \( t \) is not an upper bound. A set has at most one supremum, so \( [(u_k)] = r \).
:::

So the bisection and the Newton sequence, two unrelated Cauchy sequences of rationals, name one real number, as the truncations did in Section 5.1.

The proof of @thm-reals-complete-ordered-field built two infinite sequences of rationals and chose nothing. The last example says what choosing would have meant.

::: {#exm-representatives-need-choice}
[Picking Representatives Is a Use of Choice]

A proof about a sequence \( (x_k) \) in \( \nR \) says: "for each \( k \), pick a representative \( a^{(k)} \in x_k \)." What does that ask for? Does the proof of @thm-reals-complete-ordered-field make such picks?
:::

::: {.solution}
Each \( x_k \) is a class, a non-empty subset of \( \sC \) (@fd2:def-equivalence-class). The family \( (x_k)_{k \in \nN} \) is a family of non-empty sets indexed by \( \nN \), and "pick \( a^{(k)} \in x_k \) for each \( k \)" asks for a function \( c \colon \nN \to \sC \) with \( c(k) \in x_k \) for every \( k \): a choice function for the family. Its existence, with no rule given, is what @fd2:ax-choice provides. Fixing one object would give one representative of one \( x_k \); it cannot give infinitely many in one step.

The proof of @thm-reals-complete-ordered-field fixes finitely many objects, one at a time: \( a_0 \), \( M \), \( l_0 \), \( u_0 \); in Step 3, for the given \( \varepsilon \), one \( n \); and in Steps 4 and 5 one \( q \), \( \delta \), \( N \) (and in Step 5 one \( a \in A \)). Each is fixed once and is ordinary logic. The infinitely many ends \( l_k \), \( u_k \) are not picked: the recursion theorem defines them from a rule, which applies a test, "is \( c \) an upper bound?", to a point it has already computed. So @fd2:ax-choice is not used. A proof that needs infinitely many objects must name the rule that gives them, or say that the axiom of choice is used and where (@fd2:exm-method-name-the-choice).
:::

## What we built, and what comes next

The table collects what the chapter proved about \( \nR \), beside the status of the same property in \( \nQ \).

| Property | In \( \nR \) | In \( \nQ \) |
|---|---|---|
| ordered field | yes: @thm-reals-ordered-field | yes: @thm-rationals-ordered-field |
| Archimedean | yes: @thm-constructed-reals-archimedean | yes: @thm-rationals-archimedean |
| an element whose square is \( 2 \) | yes: @exm-sqrt2-class | no: @thm-no-rational-square-two |
| complete | yes: @thm-reals-complete-ordered-field | no: @thm-rationals-gap-sqrt2 |

The first two rows are shared; the last two are what the construction was for.

Several chapters build on this one. Chapter 6 proves that any two complete ordered fields are isomorphic, by exactly one order-preserving field isomorphism; so "the" real numbers are well defined, and no theorem about them depends on how they were built. *Axiomatic Set Theory* builds a second complete ordered field from Dedekind cuts. *Analysis on the Real Line*, Chapter 1 starts from the axioms of a complete ordered field; the theorem above gives those axioms a model, so they cannot contradict each other unless the theory that supplies \( \nN \) and sets already does (this volume's Chapter 1 takes \( \nN \) as a Peano system; *Axiomatic Set Theory* builds it from axioms for sets). *Analytic Preliminaries*, Chapter 5 builds the complex numbers on this \( \nR \). And *Analysis on the Real Line*, Chapter 5 runs the construction of this chapter for an arbitrary metric space, as its completion.

## Exercises

### A. Check your understanding

::: {#exr-the-least-upper-bound-property-a1}
[A1]

These questions are about the proof of @thm-reals-complete-ordered-field and the definition of a complete ordered field.

::: {.enumerate options="label=(\alph*)"}
1. Where in the proof is (I1) used, and where (I2)?
2. Why must \( l_0 \) not be an upper bound, and why might \( a_0 \) itself be one?
3. Where does the proof use that \( \nQ \) is Archimedean, and where that \( \nR \) is?
4. State the idea of the proof in two sentences.
5. Write "\( F \) is complete" in symbols, and form its negation.
:::
:::

::: {.solution}
(a) (I1) is used in Step 4, for (S1): a rational \( q \) between \( s \) and a larger \( a \in A \) would put some right end \( u_N \) below \( a \). (I2) is used in Step 5, for (S2): a left end \( l_N \) above a supposed smaller upper bound \( b \) yields an element of \( A \) above \( b \). Both are carried by the induction of Step 2, which is what keeps them true.

(b) The left end must **not** be an upper bound, and \( a_0 \) might be one: for \( A = \{a_0\} \), the element \( a_0 \) is an upper bound (even the supremum), and (I2) would fail at \( k = 0 \). Any \( l_0 < a_0 \) is safe, since \( a_0 \in A \) lies above it, so it is never an upper bound.

(c) That \( \nQ \) is Archimedean: in Step 3, to make \( D/2^k \) smaller than \( \varepsilon \) (@thm-rationals-archimedean). That \( \nR \) is: through density (@thm-constructed-rationals-dense, proved from @thm-constructed-reals-archimedean), which supplies the rationals of Steps 1, 4 and 5.

(d) Halve an interval with rational ends by a rule that keeps the right end an upper bound and the left end not one; the ends form two equivalent Cauchy sequences of rationals, hence one real number \( s \). A rational between \( s \) and a larger element of \( A \) would undercut a right end, and one between a smaller upper bound and \( s \) would be overtaken by a left end.

(e) With \( \mathrm{ub}(u) \) for \( \forall a \in A \ a \le u \), "complete" is the display in @def-complete-ordered-field. Its negation (@fd1:prp-quantifier-negation, @fd1:prp-bounded-quantifier-negation, @fd1:prp-negated-implication, @fd1:prp-de-morgan (d), and \( \neg(x \le y) \) as \( y < x \) by (O1)):
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

*Least.* Let \( b < 1 \). Then \( 1 - b \in \nR_{>0} \), and @prp-archimedean-reciprocal in \( \nR \) (@thm-constructed-reals-archimedean) gives \( N \in \nZ_{>0} \) with \( 1/N < 1 - b \). With \( n \coloneqq N \), the element \( 1 - 1/(N + 1) \) of \( A \) satisfies \( 1/(N + 1) < 1/N < 1 - b \), so \( 1 - 1/(N + 1) > b \), and \( b \) is not an upper bound. By (O1), every upper bound \( u \) satisfies \( u \ge 1 \).

So \( \sup A = 1 \), and \( 1 \notin A \), since every element of \( A \) is \( < 1 \). The supremum exists here without @thm-reals-complete-ordered-field: we exhibited it.
:::

::: {#exr-the-least-upper-bound-property-b3}
[B3: Prove or disprove]

Let \( A \subseteq \nR \) be non-empty and bounded above, and let \( (l_k, u_k) \) and \( s \) be as in the proof of @thm-reals-complete-ordered-field, from any rational start allowed by the remark after the proof. Prove each true statement and refute each false one with a counterexample.

::: {.enumerate options="label=(\alph*)"}
1. \( a \le u_k \) for every \( a \in A \) and every \( k \in \nN \).
2. \( s \in A \).
3. If \( A \) has a largest element \( m \), then \( s = m \).
4. Some \( l_k \) lies in \( A \).
5. If the step rule is changed to "\( (c, u) \) if \( c \in A \), and \( (l, c) \) otherwise", the new \( s \) is still \( \sup A \).
:::
:::

::: {.solution}
(a) **True.** This is (I1): \( u_k \) is an upper bound of \( A \).

(b) **False.** For \( A = \{ x \in \nR : x < 0 \} \), \( s = \sup A = 0 \notin A \) (the example of the negative elements after @def-complete-ordered-field).

(c) **True.** A greatest element is the supremum (*Sets and Functions*, Section 5.3, the remark after @fd2:def-order-supremum), so \( m = \sup A \), and \( s = \sup A \) by the theorem's proof; a set has at most one supremum, so \( s = m \).

(d) **False.** For \( A = \{0\} \), (I2) says that \( l_k \) is not an upper bound of \( \{0\} \), that is, \( l_k < 0 \); so \( l_k \notin A \) for every \( k \).

(e) **False.** The changed rule still halves the interval and keeps \( l_{k+1}, u_{k+1} \) between \( l_k \) and \( u_k \), so Steps 2 and 3 still give a real number \( s = [(u_k)] \). Take \( A = \{0, 1\} \), with the start \( l_0 = -1/2 \), \( u_0 = 3/2 \), one that Step 1 allows for \( a_0 = 0 \), \( M = 1 \) (\( -1 < -1/2 < 0 \), \( 1 < 3/2 < 2 \)). The midpoint \( c = 1/2 \) is not in \( A \), so \( (l_1, u_1) = (-1/2, 1/2) \). From then on every end lies in \( [l_1, u_1] \), so \( u_k \le 1/2 \) for every \( k \ge 1 \), and the new \( s \le 1/2 < 1 = \sup A \) (@lem-termwise-order). The test must be the invariant itself.
:::

### C. Going deeper

::: {#exr-the-least-upper-bound-property-c1}
[C1: Exit check: bisection on a dyadic grid]

Let \( A \subseteq \nR \) be non-empty and bounded above. For \( k \in \nN \), let
\[
U_k \coloneqq \{ m \in \nZ : m/2^k \text{ is an upper bound of } A \} .
\]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( U_k \) has a least element \( m_k \).
2. Let \( u_k \coloneqq m_k/2^k \). Show that \( u_{k+1} \le u_k \) and that \( u_k - 1/2^k \) is not an upper bound of \( A \); deduce that \( u_k - 1/2^k < u_j \le u_k \) for \( j \ge k \).
3. Show that \( (u_k) \in \sC \), and that \( s \coloneqq [(u_k)] \) is the supremum of \( A \). Name the lines that use an Archimedean property, and of which field.
:::
:::

::: {.solution}
[Hint 1]

Least elements of sets of integers (Chapter 2), and integer parts in \( \nR \).
:::

::: {.solution}
[Hint 2]

For (a): fix \( a_0 \in A \) and an upper bound \( M \), and look at the integer parts of \( 2^k M \) and \( 2^k a_0 \).
:::

::: {.solution}
Integer parts exist in \( \nR \) by @prp-integer-part-ordered-field with \( F = \nR \), which is Archimedean (@thm-constructed-reals-archimedean).

(a) Fix \( a_0 \in A \) and an upper bound \( M \). Let \( p \) be the integer part of \( 2^k M \). Then \( 2^k M < p + 1 \), so \( M < (p + 1)/2^k \) (multiply by \( 1/2^k > 0 \)), and \( (p + 1)/2^k \) bounds \( A \): \( p + 1 \in U_k \), and \( U_k \ne \emptyset \). If \( m \in U_k \), then \( m/2^k \ge a_0 \), so \( m \ge 2^k a_0 \ge p' \), where \( p' \) is the integer part of \( 2^k a_0 \); thus \( p' \le m \) in \( \nZ \) (@thm-rational-embedding (b)), and \( p' \) is a lower bound of \( U_k \). By @prp-integer-least-element, \( U_k \) has a least element \( m_k \).

(b) \( 2m_k/2^{k+1} = m_k/2^k = u_k \) bounds \( A \), so \( 2m_k \in U_{k+1} \) and \( m_{k+1} \le 2m_k \), that is, \( u_{k+1} \le u_k \). Since \( m_k \) is least, \( m_k - 1 \notin U_k \): \( (m_k - 1)/2^k = u_k - 1/2^k \) is not an upper bound. For \( j \ge k \): \( u_j \le u_k \) by induction (@fd1:ax-induction; every \( j \ge k \) is \( k + i \), @prp-omega-order-arithmetic (a)). And \( u_j > u_k - 1/2^k \), since otherwise \( u_k - 1/2^k \ge u_j \) would be an upper bound.

(c) By (b), \( \abs{u_j - u_k} = u_k - u_j < 1/2^k \) for \( j \ge k \), and \( (1/2^k)_k \) is null in \( \nQ \), as in Step 3 of the proof of @thm-reals-complete-ordered-field (Archimedes in \( \nQ \)). So \( (u_k) \in \sC \). With \( l_k \coloneqq u_k - 1/2^k \in \nQ \): \( (l_k) \in \sC \) and \( (l_k) \sim (u_k) \), \( l_k \) is not an upper bound and \( u_k \) is one. Steps 4 and 5 of the proof used nothing else, so they apply word for word, and \( s = \sup A \).

Archimedean lines: the integer parts in (a), for \( \nR \); \( 1/2^k \to 0 \) in (c), for \( \nQ \); and the rationals \( q \) of Steps 4 and 5, reused in (c), come from density (@thm-constructed-rationals-dense), that is, from the Archimedean property of \( \nR \).

**Marking scheme.** (10 points)
- 2: (a), \( U_k \) non-empty and bounded below, each with a reason.
- 2: (b), \( u_{k+1} \le u_k \), and "\( u_k - 1/2^k \) is not an upper bound" from leastness.
- 2: \( (u_k) \in \sC \), with the Archimedean property of \( \nQ \) named (and that of \( \nR \) for the integer parts in (a)).
- 2: (S1), from (I1) and the fact that \( s \) is the class (or limit) of the \( u_k \).
- 2: (S2), through \( (l_k) \sim (u_k) \).
Fatal errors (0 for the step): "choose an upper bound \( m/2^k \)" with no least element (no rule); \( s \in A \) asserted.
:::

::: {#exr-the-least-upper-bound-property-c2}
[C2: The rationals are not complete, by bisection]

Run the bisection of Step 2 inside \( F = \nQ \), on \( A \coloneqq \{ q \in \nQ : q^2 < 2 \} \), with "upper bound" meaning upper bound in \( \nQ \), \( (l_0, u_0) = (0, 2) \) and \( D = 2 \).

::: {.enumerate options="label=(\alph*)"}
1. Explain why (I1)–(I3) and Step 3 hold in \( \nQ \), so that \( (u_k) \) is Cauchy in \( \nQ \).
2. Prove: if \( A \) had a supremum \( s \) in \( \nQ \), then \( u_k \to s \) in \( \nQ \).
3. Prove that \( (u_k) \) has no limit in \( \nQ \). *(Show \( l_k^2 < 2 \le u_k^2 \).)*
4. Conclude that \( A \) has no supremum in \( \nQ \). Why is "\( (u_k) \) is Cauchy with no rational limit" not enough on its own for this?
:::
:::

::: {.solution}
[Hint 1]

For (b), compare \( s \) with \( u_k \) and with \( l_k \), using (I1), (I2), (S1) and (S2). For (c), the left ends are below some element of \( A \).
:::

::: {.solution}
[Hint 2]

For \( u_k^2 \ge 2 \) in (c): suppose \( u_k^2 < 2 \), and look for a rational \( h \) with \( 0 < h \le 1 \) and \( (u_k + h)^2 < 2 \).
:::

::: {.solution}
(a) \( 1 \in A \) as \( 1^2 < 2 \), so \( 0 \) is not an upper bound, and \( 2 \) bounds \( A \), as \( q > 2 \ge 0 \) gives \( q^2 > 4 \) (@prp-ordered-ring-rules (g)). By the remark after the proof, this start is allowed. Steps 2 and 3 use only rational arithmetic, @lem-power-two-bound and @thm-rationals-archimedean, so (I1)–(I3) hold, \( (D/2^k) \) is null in \( \nQ \), and \( (u_k) \) is Cauchy in \( \nQ \). Steps 4 and 5 need \( \nR \): the rational between \( s \) and \( a \) presupposes \( s \).

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

(d) By (b) and (c), a supremum \( s \in \nQ \) would be a rational limit of \( (u_k) \), and there is none. So \( A \) has no supremum in \( \nQ \): \( \nQ \) is not complete. A Cauchy sequence with no rational limit shows only that \( \nQ \) is not **Cauchy**-complete; part (b) is the link between the two properties, and it uses the invariants of the bisection. Section 3.3 proved the same conclusion (@thm-rationals-gap-sqrt2 (a)) directly, by improving each rational candidate; here a sequence finds the gap.

**Marking scheme.** (10 points)
- 2: (a), with the Archimedean property of \( \nQ \) cited (Step 3), and Steps 4–5 located as needing \( s \in \nR \) and density.
- 3: (b), the two invariants used to get \( l_k < s \le u_k \), and the squeeze.
- 3: (c), both bounds \( l_k^2 < 2 \le u_k^2 \) justified (the second by a rational \( h \)), then the limit laws and @thm-no-rational-square-two.
- 2: (d), the conclusion, with the difference between "not Cauchy-complete" and "not complete" stated.
Fatal errors (0 for the step): using \( \sqrt 2 \) as a rational or as a real number in (b)–(d); concluding (d) from (c) alone.
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

"\( p \ge 2 \)" is not well defined: \( (1, 2) \sim (2, 4) \), since \( 1 \cdot 4 = 2 \cdot 2 \), but \( 1 \not\ge 2 \) while \( 2 \ge 2 \). One class, two verdicts: the hypothesis of @thm-well-defined-on-classes (c) fails. (The test "\( p \ge 1 \)" would pass, but only because for an integer it says \( p > 0 \) (@thm-integers-ordered-ring (c)), the positivity test of @def-rational-order.)
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

The method is that of *Sets and Functions*, Chapter 4: an injection from a set known to be uncountable. (The route through @fd2:prp-card-le-surjection is not taken: its (\( \Leftarrow \)) direction uses choice.)
:::

::: {#exr-the-least-upper-bound-property-r4}
[R4]

Let \( x \in \nR \). Prove that there is a **strictly increasing** sequence \( (q_k) \) of rationals with \( q_k \to x \) in \( \nR \).
:::

::: {.solution}
*The tool* is @fd2:thm-recursion with a step given by a rule, on the set \( X \coloneqq \{ q \in \nQ : q < x \} \). Integer parts (@prp-integer-part-ordered-field with \( F = \nR \), Archimedean by @thm-constructed-reals-archimedean; unique) supply the rule.

*Start.* Let \( p \) be the integer part of \( x \), and \( q_0 \coloneqq p - 1 \). Then \( q_0 < p \le x \), so \( q_0 \in X \).

*Step.* For \( k \in \nN \) and \( q \in X \), let \( L \coloneqq \max\{q, x - 1/(k + 1)\} \), a real number with \( L < x \). Let \( n \) be the integer part of \( 2/(x - L) \), plus \( 1 \): a positive integer (with \( p \) the integer part, \( 0 < 2/(x - L) < p + 1 \) gives \( p + 1 > 0 \), so \( p \ge 0 \) and \( n = p + 1 \ge 1 \)) with \( n > 2/(x - L) \), so \( 2/n < x - L \) (@prp-reciprocal-order (b)). Let \( m \) be the integer part of \( n x \), and put \( g(k, q) \coloneqq (m - 1)/n \). From \( m \le nx < m + 1 \), dividing by \( n \),
\[
L < x - \frac{2}{n} < \frac{m - 1}{n} \le x - \frac{1}{n} < x .
\]
So \( g(k, q) \in X \), and \( g \colon \nN \times X \to X \) is a function: each step is a formula, made unambiguous by the uniqueness of integer parts. By @fd2:thm-recursion there is exactly one sequence with \( q_{k+1} = g(k, q_k) \).

*Properties.* By the display, \( q_{k+1} > L \ge q_k \), so the sequence is strictly increasing; and \( x - 1/(k + 1) \le L < q_{k+1} < x \), so \( \abs{q_{k+1} - x} < 1/(k + 1) \). Given \( \varepsilon \in \nR_{>0} \), @prp-archimedean-reciprocal in \( \nR \) (@thm-constructed-reals-archimedean) gives \( N \in \nZ_{>0} \) with \( 1/N < \varepsilon \); for \( k \ge N + 1 \), \( \abs{q_k - x} < 1/k \le 1/N < \varepsilon \) (@prp-ordered-field-halves (c)). So \( q_k \to x \).

*Why the look-alikes fail.* The terms of a representative of \( x \) converge to \( x \) (@exr-rationals-inside-the-reals-b3) but need not increase. The approximants \( m_k/(k + 1) \) of @exr-rationals-inside-the-reals-b2 are \( \le x \) but not always strictly increasing (for \( x = 0 \) they are all \( 0 \)). Density (@thm-constructed-rationals-dense) only says that a rational exists; it is not a rule in the data \( (k, q) \), so it cannot serve as a recursion step. And "at each step take some rational between \( L \) and \( x \)" makes one pick for each \( k \) with no rule, an unflagged use of @fd2:ax-choice (compare @exm-representatives-need-choice).
:::

<!-- dependency ledger
def-complete-ordered-field (example): sup of {x < 0} is 0 in every ordered field; x < x/2 < 0 for x < 0 | prp-ordered-field-halves (b); inline
def-complete-ordered-field (claim): a set has at most one supremum | remark after fd2:def-order-supremum (fd2:prp-greatest-unique), cited
lem-power-two-bound (proof): 0 + 1 = 1 and 1 + 1 = 2 in N; k + 1 >= 1 | def-omega-arithmetic (c), thm-omega-order (d), cited (the blueprint's "F3.1 (promised)" source: F3.1 is now approved)
lem-power-two-bound (proof): y(1 + 1) = y + y | (F9), (F7) of def-commutative-ring-and-field
thm-reals-complete-ordered-field (proof): Step 1: rationals l_0 in (a_0 - 1, a_0) and u_0 in (M, M + 1) | thm-constructed-rationals-dense, cited; a_0 - 1 < a_0 < ... by (O3) in R; inline
thm-reals-complete-ordered-field (proof): Step 2: g is a function N x (Q x Q) -> Q x Q given by a rule; the sequence (l_k, u_k) | fd2:thm-recursion read on N via cor-omega-identification (b), cited; c in Q by closure of Q
thm-reals-complete-ordered-field (proof): Step 2: c - l = u - c = (u - l)/2; (D/2^k)/2 = D/2^{k+1}; D/2^0 = D | lem-field-fraction-rules (b), def-naturals-in-ordered-field (b), cited; inline
thm-reals-complete-ordered-field (proof): Step 2: invariants (I1)-(I3) and monotonicity by induction; every j >= k is k + i | fd1:ax-induction via cor-omega-identification (b); prp-omega-order-arithmetic (a), cited
thm-reals-complete-ordered-field (proof): Step 2: eq-rational-bisection-tail from l_k <= l_j < u_j <= u_k | inline, prp-ordered-ring-rules (a), (b)
thm-reals-complete-ordered-field (proof): Step 3: D/2^k -> 0 in Q: 2^k >= k + 1 > n > D/eps; 1/(D/eps) = eps/D | thm-rationals-archimedean, lem-power-two-bound (F = Q), prp-naturals-in-ordered-field (b), prp-reciprocal-order (b), lem-field-fraction-rules (a), prp-ordered-ring-rules (c), cited
thm-reals-complete-ordered-field (proof): Step 3: (l_k) in C, (u_k) ~ (l_k), [(u_k)] = [(l_k)] | thm-cauchy-algebra-ordered-field (a), (b), def-cauchy-equivalent, fd2:thm-classes-partition (b), cited
thm-reals-complete-ordered-field (proof): Steps 4-5: q - s = [(q - u_k)], s - q = [(l_k - q)] with q read as the constant class kappa(q) | def-reals-operations, def-rational-embedding (identification of 5.4), cited
thm-reals-complete-ordered-field (proof): Steps 4-5: positivity read off any representative; u_N <= q - delta < q; l_N >= q + delta > q | prp-positivity-well-defined, def-reals-order, prp-ordered-ring-rules (a), (b), thm-rational-embedding (b), cited
thm-reals-complete-ordered-field (proof): Steps 4-5: "s < a is false" gives a <= s; "not an upper bound" gives a in A with a > l_N | (O1) in R (thm-reals-ordered-field); fd1:prp-bounded-quantifier-negation and totality (prp-ordered-field-halves (a)), cited
thm-reals-complete-ordered-field (claim): l_k <= s <= u_k for every k | lem-termwise-order with eq-rational-bisection-tail (threshold k), cited
thm-reals-complete-ordered-field (claim): forward pointers to fd3 Chapter 6, Axiomatic Set Theory, AN1.1, AN1 (sequence completeness), F4.1, Metric and Topological Spaces Ch2 | prose pointers only; nothing depends on them
thm-reals-complete-ordered-field (solution): quick check, bisection pairs (0,2), (1,2), (1,3/2), (5/4,3/2); 49/25 < 2 <= 9/4 | verify/ch05/thm-reals-complete-ordered-field.py
exm-bisection-square-root-two (solution): c >= r iff c bounds A (c >= 0 rational); l_k < r <= u_k; [(u_k)] = r | exm-sqrt2-class (r > 0, r^2 = 2), prp-ordered-ring-rules (g) in R, thm-constructed-rationals-dense, cited; verify/ch05/exm-bisection-square-root-two.py
exm-bisection-square-root-two (solution): every end >= 0 | monotonicity of Step 2 (l_0 = 0, l_k non-decreasing, u_k > l_k); inline
exm-representatives-need-choice (example): a class is a non-empty subset of C | fd2:def-equivalence-class (a contains itself by reflexivity, prp-cauchy-equivalent-relation)
exr-the-least-upper-bound-property-a1 (solution): density is proved from the Archimedean property of R | thm-constructed-rationals-dense (its proof in 5.4 uses thm-constructed-reals-archimedean)
exr-the-least-upper-bound-property-b2 (solution): 1/(N + 1) < 1/N | prp-reciprocal-order (b); prp-archimedean-reciprocal with thm-constructed-reals-archimedean, cited
exr-the-least-upper-bound-property-b3 (solution): (e) run on A = {0, 1} from (-1/2, 3/2): (l_1, u_1) = (-1/2, 1/2), then u_k <= 1/2 | inline; verify/ch05/exr-the-least-upper-bound-property-b3.py
exr-the-least-upper-bound-property-b3 (solution): (c) a greatest element is the supremum (remark after fd2:def-order-supremum, cited), uniqueness of the supremum; (d) l_k not an upper bound of {0} means l_k < 0 | well-definedness paragraph after def-complete-ordered-field; totality (prp-ordered-field-halves (a))
exr-the-least-upper-bound-property-c1 (solution): (a) p + 1 in U_k, lower bound p' (integer parts); M < (p + 1)/2^k | prp-integer-part-ordered-field (F = R, thm-constructed-reals-archimedean), prp-ordered-ring-rules (c), thm-rational-embedding (b), prp-integer-least-element, cited
exr-the-least-upper-bound-property-c1 (solution): (b) 2m_k/2^{k+1} = m_k/2^k; u_j <= u_k by induction; anything above an upper bound is one | def-naturals-in-ordered-field (b), fd1:ax-induction, prp-omega-order-arithmetic (a), transitivity of <=; inline
exr-the-least-upper-bound-property-c1 (solution): (c) (1/2^k) null in Q; Steps 4 and 5 apply | Step 3 of the proof (D = 1), cited by step; verify/ch05/thm-reals-complete-ordered-field.py (dyadic run)
exr-the-least-upper-bound-property-c2 (solution): (u + h)^2 <= u^2 + (2u + 1)h for 0 < h <= 1, u >= 0 | inline; verify/ch05/exr-the-least-upper-bound-property-c2.py
exr-the-least-upper-bound-property-r2 (solution): the comparison formula reads p/q >= 1 as p >= q | thm-rationals-ordered-field (a), cited
exr-the-least-upper-bound-property-r3 (solution): tail bound and the gap 1/3^{j+1}; 3^k >= 2^k | inline induction; verify/ch05/exr-the-least-upper-bound-property-r3.py
exr-the-least-upper-bound-property-r3 (solution): {0,1}^N indexed by N | cor-omega-identification citing rule, group (i) (fd2:thm-binary-sequences-uncountable, fd2:thm-countable-characterizations)
exr-the-least-upper-bound-property-r4 (solution): L < x - 2/n < (m - 1)/n <= x - 1/n < x | inline; verify/ch05/exr-the-least-upper-bound-property-r4.py
exr-the-least-upper-bound-property-r4 (solution): 1/k <= 1/N for k >= N + 1 | prp-ordered-field-halves (c); prp-archimedean-reciprocal with thm-constructed-reals-archimedean, cited
-->
