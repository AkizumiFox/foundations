# Cuts

This section opens Chapter 7, which is optional: nothing outside the chapter depends on it, and the volume's main line ended with Chapter 6. Chapter 5 built a real number as a class of Cauchy sequences of rationals, and Chapter 6 proved that any two complete ordered fields are linked by exactly one order-preserving field isomorphism. Here we begin a second construction, Dedekind's, in which a real number is a single set of rationals: the set of all rationals **below** it. This section defines these sets, called cuts, tests the definition on the rationals and on the gap that Section 2.6 found, and proves two lemmas on which the rest of the chapter rests. The inside and the outside of a cut are separated, and one can walk up through a cut in steps of any fixed size until one steps out.

Throughout the chapter, lower-case Latin letters such as \( p, q, r, s \) stand for rationals and \( m, n, k \) for natural numbers; Section 7.6, which brings back the field of Chapter 5, says where that changes. Nothing about real numbers is assumed: they are what is being built.

## The set below the gap

Section 2.6 proved that the set \( A \coloneqq \{ x \in \nQ : x^2 < 2 \} \) is non-empty and bounded above in \( \nQ \), and has no supremum in \( \nQ \) (@thm-rationals-gap-sqrt2 (a)). Its rational upper bounds crowd down toward a place where \( \nQ \) has no element. Chapter 5 filled that place with a new object, a class of sequences. Dedekind noticed that something already present in \( \nQ \) describes the place exactly: the set of rationals that lie below it.

That set is not quite \( A \). The set \( A \) contains \( -1 \), since \( (-1)^2 = 1 < 2 \), but not \( -2 \), since \( (-2)^2 = 4 > 2 \); it is a window of rationals around \( 0 \), not "everything below" anything. Adding the non-positive rationals repairs this. Let
\[
\sigma \coloneqq \{ p \in \nQ : p \le 0 \text{ or } p^2 < 2 \} .
\]
This set has the same upper bounds in \( \nQ \) as \( A \). It contains \( A \), so every upper bound of \( \sigma \) bounds \( A \). Conversely, let \( u \) be an upper bound of \( A \); since \( 1 \in A \), \( u \ge 1 > 0 \), and every element \( p \) of \( \sigma \) outside \( A \) has \( p \le 0 < u \). The conditions (S1) and (S2) of a supremum mention only the set of upper bounds (@fd2:def-order-supremum), so \( \sigma \), like \( A \), has no supremum in \( \nQ \); this is the argument of @thm-rationals-gap-sqrt2 (b).

So no rational sits at the top of \( \sigma \), yet \( \sigma \) itself is a perfectly good set of rationals. Dedekind's move is to **take the set as the number**. The rest of the chapter makes this precise: it says which sets of rationals qualify, orders them, adds and multiplies them, and proves that they form a complete ordered field.

## Dedekind cuts

Which subsets of \( \nQ \) should count as "the set of rationals below a number"? Three features of \( \sigma \) suggest the answer. It is neither empty nor all of \( \nQ \): a number should have rationals below it and rationals above it. With any rational it contains every smaller one. And it has no largest element, as @exm-cut-sqrt2 below shows. The third feature is the least obvious, and the paragraph "Why this definition" after the examples explains it.

*A real number is the set of rationals below it.*

::: {#def-dedekind-cut}
[Dedekind Cut]

A subset \( \alpha \subseteq \nQ \) is a **cut** (or **Dedekind cut**) if

::: {.enumerate options="label=(C\arabic*)"}
1. \( \alpha \ne \emptyset \) and \( \alpha \ne \nQ \);
2. **for every** \( p \in \alpha \) and **every** \( q \in \nQ \) with \( q < p \), \( q \in \alpha \);
3. \( \alpha \) has **no largest element**: **for every** \( p \in \alpha \) **there exists** \( p' \in \alpha \) with \( p' > p \).
:::

The set of all cuts is
\[
\nR_{\mathrm D} \coloneqq \{ \alpha \in \powerset{\nQ} : \alpha \text{ satisfies (C1), (C2) and (C3)} \} ,
\]
a subset of the power set \( \powerset{\nQ} \) (@fd2:def-power-set).
:::

In symbols, with bounded quantifiers,
\[
\begin{aligned}
&\text{(C1)} \quad \exists p \in \nQ \ (p \in \alpha) \ \wedge \ \exists q \in \nQ \ (q \notin \alpha) , \\
&\text{(C2)} \quad \forall p \in \alpha \ \forall q \in \nQ \ (q < p \Rightarrow q \in \alpha) , \\
&\text{(C3)} \quad \forall p \in \alpha \ \exists p' \in \alpha \ (p' > p) .
\end{aligned}
\]

In words, clause by clause. (C1) says that the cut is a proper, non-empty part of \( \nQ \): some rational is in it and some rational is not. (C2) says that the cut is **closed downward**: whatever rational it contains, it contains every smaller one too. (C3) says that it has **no top**: above each of its elements it has another. The letters \( \alpha, \beta, \gamma, \delta \) are reserved for cuts in this chapter.

**Well-definedness.** The collection \( \nR_{\mathrm D} \) is a set: it is carved out of the set \( \powerset{\nQ} \) by a condition, which (Z6) of @ax-zf-fragment allows, and \( \powerset{\nQ} \) exists by (Z5). A real number in the sense of this chapter is therefore literally an element of \( \powerset{\nQ} \), a subset of \( \nQ \).

**Negations.** We shall often show that a set is **not** a cut, so the three negations are worth writing out once. By @fd1:prp-bounded-quantifier-negation and @fd1:prp-negated-implication, a subset \( \alpha \subseteq \nQ \) fails

- (C1) if \( \alpha = \emptyset \) or \( \alpha = \nQ \);
- (C2) if \( \exists p \in \alpha \ \exists q \in \nQ \ (q < p \wedge q \notin \alpha) \): some element has a smaller rational missing;
- (C3) if \( \exists p \in \alpha \ \forall p' \in \alpha \ (p' \le p) \): \( \alpha \) has a **largest element**.

In the last line, "not \( p' > p \)" became \( p' \le p \) by trichotomy in \( \nQ \) (@prp-ordered-ring-rules (i)).

The first examples are the rationals themselves. For a rational \( q \), the rationals below \( q \) form a cut, and this is how the old numbers will sit among the new ones.

::: {#def-rational-cut}
[Rational Cut]

For \( q \in \nQ \), let
\[
D_q \coloneqq \{ r \in \nQ : r < q \} .
\]
It is a cut (checked below), the **rational cut** of \( q \). A cut \( \alpha \) is **rational** if \( \alpha = D_q \) for some \( q \in \nQ \).
:::

**\( D_q \) is a cut.** (C1): \( q - 1 \in D_q \), since \( q - (q - 1) = 1 > 0 \) (@prp-ordered-ring-rules (e), as \( 1 \ne 0 \) in the field \( \nQ \), @thm-rationals-ordered-field), so \( q - 1 < q \) by @prp-ordered-ring-rules (a); and \( q \notin D_q \), since \( q < q \) fails by (O1). (C2): if \( p \in D_q \) and \( r < p \), then \( r < p < q \), so \( r < q \) by (O2), and \( r \in D_q \). (C3): if \( r \in D_q \), the midpoint \( (r + q)/2 \) satisfies \( r < (r + q)/2 < q \) (Section 2.5, "Between two rationals"), so it lies in \( D_q \) and is larger than \( r \).

The letter \( D \) is for Dedekind.

::: {#exm-cut-sqrt2}
[The cut of the gap]

Show that \( \sigma = \{ p \in \nQ : p \le 0 \text{ or } p^2 < 2 \} \) is a cut.
:::

::: {.solution}
(C1): \( 0 \in \sigma \), since \( 0 \le 0 \). And \( 2 \notin \sigma \): \( 2 > 0 \), and \( 2^2 = 4 > 2 \).

(C2): let \( p \in \sigma \) and \( q \in \nQ \) with \( q < p \). If \( q \le 0 \), then \( q \in \sigma \). Otherwise \( 0 < q < p \). Then \( p > 0 \), so \( p \le 0 \) fails and \( p^2 < 2 \). Since \( 0 \le q < p \), @prp-ordered-ring-rules (g) gives \( q^2 < p^2 \), so \( q^2 < 2 \) by (O2), and \( q \in \sigma \).

(C3): let \( p \in \sigma \). If \( p \le 0 \), then \( 1 \in \sigma \) (as \( 1^2 = 1 < 2 \)) and \( 1 > 0 \ge p \). If \( p > 0 \), then \( p^2 < 2 \). Put
\[
d \coloneqq 2 - p^2 , \qquad h \coloneqq \frac{d}{2p + 2} .
\]
Here \( d > 0 \), and \( d < 2 \) because \( p^2 > 0 \) (@prp-ordered-ring-rules (e)); also \( 2p + 2 > 2 \), since \( p > 0 \). So \( 0 < h < 1 \) (@prp-reciprocal-order (a) for \( h > 0 \); \( d < 2p + 2 \) for \( h < 1 \)). From \( 0 < h < 1 \), \( h^2 < h \) by @prp-ordered-ring-rules (c). Hence
\[
\begin{aligned}
(p + h)^2 &= p^2 + 2ph + h^2 < p^2 + 2ph + h \\
&< p^2 + h(2p + 2) = p^2 + d = 2 ,
\end{aligned}
\]
where the second inequality adds \( h > 0 \) (O3). So \( p + h \in \sigma \), and \( p + h > p \).
:::

The step size \( h \) depends on \( p \): the closer \( p^2 \) is to \( 2 \), the smaller \( d \) and so \( h \). That is unavoidable, since a fixed step would jump out of \( \sigma \) from points near the top. Section 7.5 proves that \( \sigma \) is not a rational cut, \( \sigma \ne D_q \) for every \( q \in \nQ \), and Exercise C1 below asks for a direct proof. So \( \sigma \) is a genuinely new number: the cut that will square to \( 2 \).

::: {.check}
Which of the following subsets of \( \nQ \) are cuts? For each that is not, name a condition that fails.

::: {.enumerate options="label=(\alph*)"}
1. \( \{ p \in \nQ : p < 0 \text{ or } p^2 < 4 \} \);
2. \( \{ p \in \nQ : p^2 < 2 \} \);
3. \( \{ p \in \nQ : p^3 < 5 \} \);
4. \( \emptyset \).
:::
:::

::: {.solution}
(a) It is a cut, because it equals \( D_2 \). If \( p < 0 \), then \( p < 2 \). If \( p \ge 0 \) and \( p^2 < 4 = 2^2 \), then \( p < 2 \) by @prp-ordered-ring-rules (g). Conversely, if \( p < 2 \), either \( p < 0 \), or \( 0 \le p < 2 \) and then \( p^2 < 4 \) by (g).

(b) Not a cut: (C2) fails. The set contains \( 1 \), and \( -2 < 1 \), but \( (-2)^2 = 4 > 2 \), so \( -2 \) is missing.

(c) A cut. Call the set \( E \). *Cubes are monotone on non-negatives:* for \( 0 \le q < p \), \( p^3 - q^3 = (p - q)(p^2 + pq + q^2) \), where \( p - q > 0 \) and \( p^2 + pq + q^2 \ge p^2 > 0 \) (@prp-ordered-ring-rules (e), with \( pq, q^2 \ge 0 \)); so \( p^3 - q^3 > 0 \) by (O4). (C1): \( 0 \in E \), and \( 2 \notin E \), as \( 2^3 = 8 > 5 \). (C2): let \( q < p \in E \). If \( q \le 0 \), then \( q^3 \le 0 < 5 \) (\( q^3 = q \cdot q^2 \), a non-positive times a non-negative). If \( q > 0 \), then \( 0 < q < p \) and \( q^3 < p^3 < 5 \). (C3): let \( p \in E \). If \( p \le 0 \), then \( 1 \in E \) is larger. If \( p > 0 \), put \( d \coloneqq 5 - p^3 \) and \( h \coloneqq d/(3p^2 + 3p + 5) \). Then \( 0 < d < 5 < 3p^2 + 3p + 5 \), so \( 0 < h < 1 \), hence \( h^3 < h^2 < h \) by @prp-ordered-ring-rules (c), and
\[
\begin{aligned}
(p + h)^3 &= p^3 + 3p^2 h + 3p h^2 + h^3 \\
&< p^3 + h(3p^2 + 3p + 1) < p^3 + d = 5 .
\end{aligned}
\]
So \( p + h \in E \) and \( p + h > p \).

(d) Not a cut: (C1) fails, since \( \emptyset \) has no element.
:::

**Why this definition.** Each clause excludes something that would spoil the arithmetic to come.

- Without (C1), \( \emptyset \) and \( \nQ \) would be numbers, below and above every rational. Section 7.3 adds cuts as sets, and \( \nQ + D_0 = \nQ = \nQ + D_1 \) there would make cancellation fail.
- Without (C2), \( \{ p : p^2 < 2 \} \) of the Quick check would be a number. It contains \( 1 \) but not the smaller rational \( -2 \), so it is not the set of **all** rationals below anything.
- Without (C3), each rational \( q \) would be represented twice, by \( D_q \) and by \( \{ r \in \nQ : r \le q \} \). The next example shows that this is more than untidy: the sum of sets cannot tell the two apart.

::: {#exm-cut-with-largest-element .optional}
[Two candidates for one rational]

Let \( E_1 \coloneqq \{ r \in \nQ : r \le 1 \} \). Show that \( E_1 \) satisfies (C1) and (C2) but not (C3), and that, with the sum of sets \( X + Y \coloneqq \{ x + y : x \in X, \ y \in Y \} \) of *Sets, Relations, and Cardinality*, Section 1.6 (@fd2:exm-sets-of-numbers-as-images),
\[
E_1 + D_1 = D_2 = D_1 + D_1 , \qquad \text{although } E_1 \ne D_1 .
\]
:::

::: {.solution}
*The conditions.* (C1): \( 0 \in E_1 \) and \( 2 \notin E_1 \). (C2): \( q < p \le 1 \) gives \( q < 1 \). (C3) fails: \( 1 \in E_1 \), and every \( p' \in E_1 \) has \( p' \le 1 \), so \( 1 \) is a largest element. And \( E_1 \ne D_1 \), since \( 1 \in E_1 \setminus D_1 \).

*\( E_1 + D_1 = D_2 \).* \( (\subseteq) \): if \( a \le 1 \) and \( b < 1 \), then \( a + b < 2 \) by @prp-ordered-ring-rules (b). \( (\supseteq) \): if \( s < 2 \), then \( s = 1 + (s - 1) \) with \( 1 \in E_1 \) and \( s - 1 < 1 \), so \( s - 1 \in D_1 \).

*\( D_1 + D_1 = D_2 \).* \( (\subseteq) \): \( a < 1 \) and \( b < 1 \) give \( a + b < 2 \), by (b) again. \( (\supseteq) \): if \( s < 2 \), then \( s = s/2 + s/2 \), and multiplying \( s < 2 \) by \( 1/2 > 0 \) (@prp-ordered-ring-rules (c)) gives \( s/2 < 1 \), so \( s/2 \in D_1 \).

So if \( E_1 \) were admitted as a number, the equation \( \xi + D_1 = D_2 \) would have two solutions, \( E_1 \) and \( D_1 \), and addition could not be canceled, so the numbers could not form a group under addition.
:::

Condition (C3) chooses between the two sets \( \{ r \in \nQ : r < 1 \} \) and \( \{ r \in \nQ : r \le 1 \} \) that describe "the rationals up to \( 1 \)": it keeps the one that leaves \( 1 \) out.

::: {.warning}
A cut is a set of rationals, not a rational. "\( \sigma < 2 \)" compares a set with a number and means nothing yet. Section 7.2 orders cuts, so that \( \sigma < D_2 \) acquires a meaning, and Section 7.5 shows that \( D_2 \) plays the part of the rational \( 2 \) among the cuts. Until then, every comparison in this chapter is between rationals, or between sets by inclusion.
:::

## Inside and outside

The defining conditions speak about the inside of a cut. The first lemma says what they imply about the outside: everything outside lies above everything inside.

::: {#lem-cut-separation}
[Separation]

Let \( \alpha \) be a cut, \( p \in \alpha \) and \( q \in \nQ \setminus \alpha \). Then \( p < q \). Consequently the complement \( \nQ \setminus \alpha \) is **closed upward**: if \( q \notin \alpha \) and \( q' \in \nQ \) with \( q' > q \), then \( q' \notin \alpha \).
:::

::: {.proof}
Suppose \( p < q \) fails. By trichotomy (@prp-ordered-ring-rules (i)), \( q \le p \). If \( q = p \), then \( q \in \alpha \); if \( q < p \), then \( q \in \alpha \) by (C2). Either way \( q \in \alpha \), against \( q \notin \alpha \). So \( p < q \).

For the consequence, let \( q \notin \alpha \) and \( q' > q \), and suppose \( q' \in \alpha \). The first part, with \( q' \) in the role of \( p \), gives \( q' < q \), which together with \( q < q' \) contradicts (O1). So \( q' \notin \alpha \).
:::

So a cut and its complement split \( \nQ \) into a lower piece and an upper piece, every element of the lower below every element of the upper. In particular every rational outside a cut is an upper bound of it. Together with (C3), this gives the picture to keep in mind, and one of the chapter's named moves:

*A cut is a downset with an open top.*

Inside is closed downward, outside is closed upward, everything inside lies below everything outside, and the inside has no largest element. The outside may have a least element: the complement of \( D_q \) is \( \{ r \in \nQ : r \ge q \} \), with least element \( q \). Most "is it a cut?" checks in this chapter are this sentence, read clause by clause.

The second result locates a rational relative to a cut by comparing two sets. It is the bridge between a rational \( q \) and its cut \( D_q \).

::: {#prp-rational-in-cut}
[Where a Rational Lies]

Let \( \alpha \) be a cut and \( q \in \nQ \). Then

::: {.enumerate options="label=(\alph*)"}
1. \( q \in \alpha \) if and only if \( D_q \subsetneq \alpha \);
2. \( q \notin \alpha \) if and only if \( \alpha \subseteq D_q \).
:::
:::

::: {.idea}
If \( q \) is in \( \alpha \), closure downward brings everything below \( q \) along, and \( q \) itself is the extra element. If \( q \) is outside, separation puts all of \( \alpha \) below \( q \). The two converses come from the same two facts.
:::

::: {.proof}
(a) \( (\Rightarrow) \) Let \( q \in \alpha \). For \( r \in D_q \), \( r < q \), so \( r \in \alpha \) by (C2); thus \( D_q \subseteq \alpha \). The inclusion is proper, because \( q \in \alpha \) and \( q \notin D_q \) (as \( q < q \) fails, (O1)). \( (\Leftarrow) \) Let \( D_q \subsetneq \alpha \). Then some \( r \in \alpha \) has \( r \notin D_q \), that is, \( r < q \) fails, so \( q \le r \) (@prp-ordered-ring-rules (i)). If \( q = r \), then \( q \in \alpha \); if \( q < r \), then \( q \in \alpha \) by (C2).

(b) \( (\Rightarrow) \) Let \( q \notin \alpha \). For \( r \in \alpha \), @lem-cut-separation gives \( r < q \), so \( r \in D_q \); thus \( \alpha \subseteq D_q \). \( (\Leftarrow) \) Let \( \alpha \subseteq D_q \). Since \( q \notin D_q \), also \( q \notin \alpha \).
:::

Since every rational is either in \( \alpha \) or not, exactly one of \( D_q \subsetneq \alpha \) and \( \alpha \subseteq D_q \) holds. Section 7.2 rewrites (a) as \( q \in \alpha \iff D_q < \alpha \), once inclusion has become the order on cuts.

## Walking up through a cut

Many proofs in this chapter need two rationals, one inside a cut and one outside, that are **close together**: within a prescribed rational distance \( \varepsilon > 0 \). Separation says that the inside lies below the outside, but not that the two come close. They do, and the reason is a walk: start inside, climb in steps of \( \varepsilon \), and stop at the first step that leaves the cut.

::: {#lem-cut-step}
[The Step Lemma]

Let \( \alpha \) be a cut, \( a \in \alpha \), and \( \varepsilon \in \nQ \) with \( \varepsilon > 0 \). Then there is \( n \in \nN \) with
\[
a + n\varepsilon \in \alpha \qquad \text{and} \qquad a + (n + 1)\varepsilon \notin \alpha .
\]
:::

::: {.idea}
Picture the rungs \( a, a + \varepsilon, a + 2\varepsilon, \dots \). The bottom rung \( a \) is inside. Some rung is outside: pick any rational \( b \) outside \( \alpha \); the rationals are Archimedean, so finitely many steps of size \( \varepsilon \) climb past \( b \), and everything above \( b \) is outside by separation. Among the rungs outside there is a lowest one, because a non-empty set of natural numbers has a least element. It is not the bottom rung, so the rung just below it exists and is inside. The \( n \) found depends on \( \alpha \), \( a \) and \( \varepsilon \).
:::

::: {.proof}
By (C1), there is \( b \in \nQ \) with \( b \notin \alpha \). By @thm-rationals-archimedean, applied to the rational \( (b - a)/\varepsilon \), there is \( m \in \nN \) with \( (b - a)/\varepsilon < m \). Multiplying by \( \varepsilon > 0 \) (@prp-ordered-ring-rules (c)) gives \( b - a < m\varepsilon \), so \( b < a + m\varepsilon \) by (O3). Since \( b \notin \alpha \), @lem-cut-separation gives \( a + m\varepsilon \notin \alpha \).

Let
\[
K \coloneqq \{ k \in \nN : a + k\varepsilon \notin \alpha \} .
\]
Then \( m \in K \), so \( K \) is a non-empty set of integers, and \( 0 \) is a lower bound of it. By @prp-integer-least-element, \( K \) has a least element \( k_0 \). Since \( a + 0 \cdot \varepsilon = a \in \alpha \), \( 0 \notin K \), so \( k_0 \ne 0 \) and \( k_0 > 0 \). By discreteness (@thm-integers-ordered-ring (c)), \( k_0 \ge 1 \). Put \( n \coloneqq k_0 - 1 \). Then \( n \ge 0 \) by (O3), so \( n \in \nN \) (@thm-integers-ordered-ring (b)). Since \( n < k_0 \) and \( k_0 \) is least in \( K \), \( n \notin K \), that is, \( a + n\varepsilon \in \alpha \). And \( a + (n + 1)\varepsilon = a + k_0 \varepsilon \notin \alpha \), since \( k_0 \in K \). This proves the lemma.
:::

Since \( n \ge 0 \) and \( \varepsilon > 0 \), the point \( p \coloneqq a + n\varepsilon \) found by the lemma satisfies \( p \ge a \). So the lemma hands over a pair \( p \in \alpha \), \( p + \varepsilon \notin \alpha \): a point inside and a point outside, exactly \( \varepsilon \) apart, with the inside point as high as we like above a given element. This is another of the chapter's named moves.

*Walk up by \( \varepsilon \): from a point inside a cut, add \( \varepsilon \) until you leave; the last step inside and the first step outside are \( \varepsilon \) apart.*

It drives the hardest "\( \supseteq \)" halves to come: the additive inverse in Section 7.3 and, in its multiplicative form of Section 7.4, the multiplicative inverse in Section 7.4 and the square of \( \sigma \) in Section 7.5. Note what it needs from \( \nQ \): the Archimedean property, to know that the walk leaves the cut at all, and least elements and discreteness of the integers, to find the first step out and the step before it.

Here is one walk, through \( \sigma \) from \( a = 1 \) in steps of \( \varepsilon = 1/10 \). The rungs \( 1, 11/10, 12/10, \dots \) are positive, so a rung \( r \) lies in \( \sigma \) exactly when \( r^2 < 2 \). Now \( (14/10)^2 = 196/100 < 2 \), because \( 196 < 200 \), and the lower positive rungs have smaller squares (@prp-ordered-ring-rules (g)), so the rungs for \( k = 0, \dots, 4 \) are inside. But \( (15/10)^2 = 225/100 > 2 \). So the least \( k \) with \( 1 + k/10 \notin \sigma \) is \( k_0 = 5 \), the \( n \) of the lemma is \( 4 \), and the pair is \( 7/5 \in \sigma \), \( 3/2 \notin \sigma \).

::: {.check}
Continue the walk with a finer step: start at \( a = 7/5 \in \sigma \) and take \( \varepsilon = 1/100 \). Which pair \( p \in \sigma \), \( p + \varepsilon \notin \sigma \) does the lemma give?
:::

::: {.solution}
The rungs are \( 140/100, 141/100, 142/100, \dots \). Since \( 141^2 = 19881 < 20000 \), \( (141/100)^2 < 2 \), so \( 141/100 \in \sigma \). Since \( 142^2 = 20164 > 20000 \), \( 142/100 \notin \sigma \). So \( k_0 = 2 \), \( n = 1 \), and the pair is \( p = 141/100 \), \( p + \varepsilon = 142/100 = 71/50 \).
:::

Each walk traps the top of \( \sigma \) between two rationals \( \varepsilon \) apart, and a smaller \( \varepsilon \) traps it more tightly. No walk ever lands on the top, since \( \sigma \) has none.

## Exercises

### A. Check your understanding

::: {#exr-cuts-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State (C1)–(C3) for a subset \( \alpha \subseteq \nQ \), and write the negation of (C3) in symbols.
2. For each set, name every condition among (C1)–(C3) that fails: (i) \( \{ p \in \nQ : p \le 3 \} \); (ii) \( \{ p \in \nQ : p > 0 \} \); (iii) \( \{ p \in \nQ : p^2 \le 0 \} \); (iv) \( \{ p \in \nQ : p < p + 1 \} \).
3. Let \( q, r \in \nQ \). Is \( D_q \cup D_r \) a cut? Is \( D_q \cap D_r \)? Identify each.
:::
:::

::: {.solution}
(a) (C1) \( \alpha \ne \emptyset \) and \( \alpha \ne \nQ \); (C2) for every \( p \in \alpha \) and every \( q \in \nQ \) with \( q < p \), \( q \in \alpha \); (C3) for every \( p \in \alpha \) there is \( p' \in \alpha \) with \( p' > p \). The negation of (C3) is \( \exists p \in \alpha \ \forall p' \in \alpha \ (p' \le p) \): \( \alpha \) has a largest element.

(b) (i) Only (C3) fails: \( 3 \) is a largest element. (C1) holds (\( 0 \) in, \( 4 \) out) and (C2) holds (\( q < p \le 3 \) gives \( q < 3 \)). (ii) Only (C2) fails: \( 1 \) is in, and \( 0 < 1 \) is not. (C1) holds (\( 1 \) in, \( 0 \) out), and (C3) holds (\( p + 1 > p > 0 \)). (iii) The set is \( \{0\} \), since \( p \ne 0 \) gives \( p^2 > 0 \) (@prp-ordered-ring-rules (e)). (C2) fails (\( -1 < 0 \), \( -1 \) missing) and (C3) fails (\( 0 \) is largest); (C1) holds. (iv) The set is \( \nQ \), since \( 0 < 1 \) gives \( p < p + 1 \) for every \( p \) (O3). (C1) fails; (C2) and (C3) hold.

(c) Both are cuts. If \( q \le r \), then \( D_q \subseteq D_r \) (\( s < q \le r \) gives \( s < r \)), so \( D_q \cup D_r = D_r \) and \( D_q \cap D_r = D_q \); if \( r \le q \), the roles swap. So \( D_q \cup D_r = D_{\max(q, r)} \) and \( D_q \cap D_r = D_{\min(q, r)} \), rational cuts by @def-rational-cut.
:::

### B. Practice

::: {#exr-cuts-b1}
[B1]

Prove that \( \{ p \in \nQ : 3p < 2 \} \) is a cut, and that it equals \( D_{2/3} \).
:::

::: {.solution}
For \( p \in \nQ \), \( 3p < 2 \) implies \( p < 2/3 \), by multiplying with \( 1/3 > 0 \) (@prp-reciprocal-order (a), @prp-ordered-ring-rules (c)); and \( p < 2/3 \) implies \( 3p < 2 \), by multiplying with \( 3 > 0 \). So the set is \( \{ p \in \nQ : p < 2/3 \} = D_{2/3} \), and it is a cut because every rational cut is one (@def-rational-cut, with the check after it).
:::

::: {#exr-cuts-b2}
[B2]

Prove that \( \{ p \in \nQ : p < 0 \text{ or } p^2 < 3 \} \) is a cut. For (C3), give an explicit larger element.
:::

::: {.solution}
Call the set \( \beta \). (C1): \( 0 \in \beta \), since \( 0^2 = 0 < 3 \); and \( 2 \notin \beta \), since \( 2 \ge 0 \) and \( 2^2 = 4 > 3 \).

(C2): let \( q < p \in \beta \). If \( q < 0 \), then \( q \in \beta \). Otherwise \( 0 \le q < p \), so \( p > 0 \), \( p < 0 \) fails, and \( p^2 < 3 \). By @prp-ordered-ring-rules (g), \( q^2 < p^2 < 3 \), so \( q \in \beta \).

(C3): let \( p \in \beta \). If \( p < 0 \), then \( 0 \in \beta \) and \( 0 > p \). If \( p \ge 0 \), then \( p^2 < 3 \). Put
\[
d \coloneqq 3 - p^2 , \qquad h \coloneqq \frac{d}{2p + 4} .
\]
Then \( 0 < d \le 3 < 4 \le 2p + 4 \), so \( 0 < h < 1 \) and \( h^2 < h \) (@prp-ordered-ring-rules (c)). Hence
\[
\begin{aligned}
(p + h)^2 &= p^2 + 2ph + h^2 < p^2 + h(2p + 1) \\
&< p^2 + h(2p + 4) = p^2 + d = 3 ,
\end{aligned}
\]
so \( p + h \in \beta \) and \( p + h > p \). (The denominator is chosen to exceed \( d \), so that \( h < 1 \), and to be at least \( 2p + 1 \); any such denominator works.)
:::

### C. Going deeper

::: {#exr-cuts-c1}
[C1: The cut of the gap is not rational]

Prove directly from the definitions that \( \sigma \ne D_q \) for every \( q \in \nQ \).
:::

::: {.solution}
[Hint 1]

If \( \sigma = D_q \), where would \( q \) itself sit relative to \( \sigma \)? What does that say about \( q \) and \( q^2 \)?
:::

::: {.solution}
[Hint 2]

You will reach \( q > 0 \) and \( q^2 \ge 2 \). If \( q^2 > 2 \), look for a smaller positive rational whose square still exceeds \( 2 \); Section 2.6 has one.
:::

::: {.solution}
Suppose \( \sigma = D_q \) for some \( q \in \nQ \). Since \( q \notin D_q \), \( q \notin \sigma \): so \( q \le 0 \) fails, and \( q^2 < 2 \) fails. That is, \( q > 0 \) and \( q^2 \ge 2 \).

*Case \( q^2 = 2 \).* Impossible, by @thm-no-rational-square-two.

*Case \( q^2 > 2 \).* Let \( q' \coloneqq (q^2 + 2)/(2q) \), the rational \( t(q) \) of Section 2.6. It is positive, as a quotient of positives (@prp-reciprocal-order (a), (O4)). By the identities @eq-newton-identities,
\[
q - q' = \frac{q^2 - 2}{2q} > 0 , \qquad q'^2 - 2 = \frac{(q^2 - 2)^2}{4q^2} > 0 ,
\]
the first a quotient of positives, the second because \( q^2 - 2 \ne 0 \) (@prp-ordered-ring-rules (e)). So \( q' < q \), that is, \( q' \in D_q = \sigma \). But \( q' > 0 \) and \( q'^2 > 2 \), so \( q' \notin \sigma \). This contradiction shows that \( \sigma \ne D_q \).

**Marking scheme.** (10 points)
- 3: from \( q \notin D_q = \sigma \), derives both \( q > 0 \) and \( q^2 \ge 2 \).
- 2: excludes \( q^2 = 2 \), citing that no rational squares to \( 2 \).
- 3: for \( q^2 > 2 \), exhibits a rational \( q' \) with \( 0 < q' < q \) and \( q'^2 > 2 \), with both inequalities verified (any such \( q' \) earns the points).
- 2: concludes: \( q' \) lies in \( D_q \) but not in \( \sigma \).
Fatal errors (0 for the step): "\( q = \sqrt 2 \)" or any use of a square root of \( 2 \) as a number; a candidate \( q' \) whose square is not checked to exceed \( 2 \).
:::

<!-- dependency ledger
def-dedekind-cut (claim): sigma has the same upper bounds as A; 1 in A | inline (as in thm-rationals-gap-sqrt2 (b))
def-dedekind-cut (claim): R_D is a set, carved out of P(Q) | ax-zf-fragment (Z5), (Z6), cited
def-dedekind-cut (claim): negations of (C1)-(C3); not (p' > p) iff p' <= p | fd1:prp-bounded-quantifier-negation, fd1:prp-negated-implication, prp-ordered-ring-rules (i), cited
def-rational-cut (claim): D_q is a cut: q - (q - 1) = 1 > 0 as 1 != 0 in Q, so q - 1 < q; midpoint (r + q)/2 strictly between | Q ordered field, F3.2 (thm-rationals-ordered-field); prp-ordered-ring-rules (a), (e), cited; midpoint paragraph of F3.2 §05 ("Between two rationals")
exm-cut-sqrt2 (solution): 2^2 = 4 > 2, 1^2 < 2; p > 0 gives p^2 > 0, 2p + 2 > 2 | Q ordered field, F3.2; prp-ordered-ring-rules (e), cited
exm-cut-sqrt2 (solution): 0 < h < 1 gives h^2 < h; (p + h)^2 < 2 | prp-ordered-ring-rules (c), (O3); inline; verify/ch07/exm-cut-sqrt2.py
def-dedekind-cut (claim): Quick check: (a) equals D_2; (c) cubes monotone on non-negatives, p^3 - q^3 = (p - q)(p^2 + pq + q^2); q^3 <= 0 for q <= 0; the step h = d/(3p^2 + 3p + 5) | prp-ordered-ring-rules (c), (e), (g), (O4); inline; verify/ch07/def-dedekind-cut.py
def-dedekind-cut (claim): "Why this definition": Q + D_0 = Q = Q + D_1 as set sums | inline (set sum of fd2:exm-sets-of-numbers-as-images; Section 7.3 in prose)
exm-cut-with-largest-element (solution): a <= 1, b < 1 give a + b < 2; s/2 < 1 for s < 2 | prp-ordered-ring-rules (b), (c), cited; verify/ch07/exm-cut-with-largest-element.py
lem-cut-separation (proof): q <= p or p < q | prp-ordered-ring-rules (i), cited
prp-rational-in-cut (proof): q < q fails | (O1)
lem-cut-step (proof): (b - a)/epsilon < m gives b - a < m epsilon | thm-rationals-archimedean, prp-ordered-ring-rules (c), cited; (O3)
lem-cut-step (proof): a + 0 * epsilon = a; a + (n + 1) epsilon = a + k_0 epsilon; n epsilon >= 0 | Q ordered field, F3.2 (ring algebra, prp-ordered-ring-rules (c)); inline
lem-cut-step (proof): K is a set of integers (N inside Z) | identification N in Z of F3.2 §02 (thm-integers-ordered-ring (b)), cited
lem-cut-step (example): the walk through sigma from 1 by 1/10: 196 < 200, 225 > 200; rungs positive, squares increasing | prp-ordered-ring-rules (g); inline; verify/ch07/lem-cut-step.py
lem-cut-step (claim): Quick check after it: 141^2 = 19881, 142^2 = 20164 | inline arithmetic; verify/ch07/lem-cut-step.py
exr-cuts-a1 (solution): D_q subset D_r for q <= r; p^2 > 0 for p != 0; p < p + 1 | (O2), (O3), prp-ordered-ring-rules (e); inline
exr-cuts-b1 (solution): 3p < 2 iff p < 2/3 | prp-reciprocal-order (a), prp-ordered-ring-rules (c), cited
exr-cuts-b2 (solution): 0 < d <= 3 < 4 <= 2p + 4 gives 0 < h < 1; (p + h)^2 < 3; the closing remark (any denominator > d and >= 2p + 1 works) | prp-ordered-ring-rules (c), (g); inline; verify/ch07/exr-cuts-b2.py
exr-cuts-c1 (solution): q' = (q^2 + 2)/(2q) and its two identities | eq-newton-identities (thm-rationals-gap-sqrt2), cited; verify/ch07/exr-cuts-c1.py
-->
