# The Rationals as Classes of Fractions

Section 10.3 made \( \nZ \) an ordered commutative ring and ended with a Quick check: \( \nZ \) is not a field, because \( 2x = 1 \) has no solution in it. This section repairs that defect the way Section 10.1 repaired the missing subtraction in \( \nN \). There, a pair \( (a, b) \) recorded "\( a - b \)" without performing it; here a pair \( (p, q) \) records "\( p \) divided by \( q \)" without performing it. We define \( \nQ \) as a set of classes of such pairs, give it addition and multiplication through representatives, check that they are well defined, and prove that \( \nQ \) is a field containing a copy of \( \nZ \).

## Fractions as pairs

At school, \( \tfrac12 \), \( \tfrac24 \) and \( \tfrac36 \) are "the same number", and the test for sameness is cross-multiplication: \( \tfrac pq = \tfrac rs \) when \( ps = rq \). The test is the useful part. It mentions only multiplication of integers, which we have, and not division, which we do not. So we keep the test and let a rational number **be** what the equivalent fractions have in common: the class of all of them.

*A rational number is a quotient you have not computed yet: the set of all fractions that would compute to it.*

Signs need a decision. The fractions \( \tfrac{1}{-2} \) and \( \tfrac{-1}{2} \) name the same number, and allowing both would put a sign in two places. We require the **denominator to be positive**, so that a sign can sit only in the numerator. This is the convention Section 7.5 already used for its fractions, and Section 10.5 will profit from it: there, the order of \( \nQ \) is read off a single inequality between integers. Recall that \( \nZ_{>0} = \{ n \in \nZ : n > 0 \} \), by @thm-integers-ordered-ring (b).

On \( \nZ \times \nZ_{>0} \), let \( (p, q) \sim (r, s) \) mean \( ps = rq \). We reuse the symbol \( \sim \) of Section 10.1; which relation is meant is always clear from the pairs, natural numbers there and an integer with a positive integer here.

::: {#prp-rational-pairs-equivalence}
[Cross-Multiplication Is an Equivalence Relation]

The relation \( \sim \) on \( \nZ \times \nZ_{>0} \) given by
\[
(p, q) \sim (r, s) \iff ps = rq
\]
is an equivalence relation (@def-equivalence-relation).
:::

::: {.idea}
Reflexivity and symmetry are commutativity of multiplication and symmetry of \( = \). For transitivity we are given \( ps = rq \) and \( ru = ts \), and want \( pu = tq \). Multiply the first equation by \( u \) and use the second to replace \( ru \): this gives \( (pu)s = (tq)s \). We cannot divide by \( s \), but \( \nZ \) has no zero divisors, so a factor \( s \ne 0 \) can be canceled.
:::

::: {.proof}
Let \( (p, q), (r, s), (t, u) \in \nZ \times \nZ_{>0} \). All computations are in the commutative ring \( \nZ \) (@thm-integers-commutative-ring).

(Eq1) \( pq = pq \), so \( (p, q) \sim (p, q) \).

(Eq2) If \( ps = rq \), then \( rq = ps \), so \( (r, s) \sim (p, q) \).

(Eq3) Let \( ps = rq \) and \( ru = ts \). Then, using (F5), (F6) and the two hypotheses,
\[
(pu)s = (ps)u = (rq)u = (ru)q = (ts)q = (tq)s .
\]
Hence \( (pu - tq)s = (pu)s - (tq)s = 0 \), by (F9) and @prp-ring-algebra (c). Since \( s \in \nZ_{>0} \), \( s > 0 \), so \( s \ne 0 \) by (O1). By @prp-ordered-ring-rules (f), \( pu - tq = 0 \), that is, \( pu = tq \). So \( (p, q) \sim (t, u) \). This proves the proposition.
:::

The hypothesis that denominators are non-zero is used once, for the **middle** pair \( (r, s) \), and it is needed there. On \( \nZ \times \nN \), with the same formula, \( (1, 0) \sim (0, 0) \) (since \( 1 \cdot 0 = 0 \cdot 0 \)) and \( (0, 0) \sim (1, 1) \) (since \( 0 \cdot 1 = 1 \cdot 0 \)), but \( (1, 0) \not\sim (1, 1) \) (since \( 1 \cdot 1 \ne 1 \cdot 0 \)). The pair \( (0, 0) \) is related to everything, and transitivity collapses through it.

::: {#def-rationals-as-classes}
[The Rational Numbers]

Let \( \sim \) be the equivalence relation of @prp-rational-pairs-equivalence on \( \nZ \times \nZ_{>0} \). The set of **rational numbers** is the quotient set (@def-quotient-set)
\[
\nQ \coloneqq (\nZ \times \nZ_{>0})/{\sim} .
\]
A **rational number** is an element of \( \nQ \): a class \( [(p, q)] \) with \( p \in \nZ \) and \( q \in \nZ_{>0} \). We call \( p \) a **numerator** and \( q \) a **denominator** of the representative \( (p, q) \).
:::

In words: a rational number is a **set of pairs**, all the pairs \( (r, s) \) with positive \( s \) that cross-multiply with \( (p, q) \). It is not a pair, and it is not a number with a sign and a bar. Numerators and denominators belong to representatives, not to the class: \( (1, 2) \) and \( (2, 4) \) represent the same rational number with different denominators. Nothing in the definition needs checking beyond @prp-rational-pairs-equivalence, which makes the quotient set meaningful. By @thm-classes-partition, every pair lies in exactly one class, and \( [(p, q)] = [(r, s)] \) holds exactly when \( ps = rq \).

**Examples.**

- \( [(1, 2)] = \{ (k, 2k) : k \in \nZ_{>0} \} \). Indeed, \( (r, s) \sim (1, 2) \) means \( 2r = s \). Then \( 2r > 0 \), and \( r \le 0 \) would give \( 2r = r + r \le 0 \) (@prp-ordered-ring-rules (b)), so \( r > 0 \). Conversely each \( (k, 2k) \) with \( k > 0 \) has \( 2k > 0 \) and \( k \cdot 2 = 2k \cdot 1 \). Its elements with denominator at most \( 6 \) are \( (1, 2) \), \( (2, 4) \), \( (3, 6) \).
- \( [(-2, 1)] = \{ (-2s, s) : s \in \nZ_{>0} \} \), since \( (r, s) \sim (-2, 1) \) means \( r = -2s \). This is the class that will be the integer \( -2 \).
- The degenerate case: \( [(0, 1)] = \{ (0, s) : s \in \nZ_{>0} \} \), since \( (r, s) \sim (0, 1) \) means \( r \cdot 1 = 0 \cdot s = 0 \). Every fraction with numerator \( 0 \) lies in this one class, whatever its denominator; it will be the zero of \( \nQ \).
- \( [(2, 3)] \) contains \( (4, 6) \) and \( (6, 9) \), since \( 2 \cdot 6 = 4 \cdot 3 \) and \( 2 \cdot 9 = 6 \cdot 3 \). It does not contain \( (-4, -6) \), which is not even an element of \( \nZ \times \nZ_{>0} \). Describing the whole class needs divisibility, which a later chapter of this volume develops on the constructed \( \nZ \).

**A non-example by minimal change.** Allow the denominator \( 0 \): take \( \nZ \times \nN \) instead of \( \nZ \times \nZ_{>0} \), with the same formula. Reflexivity and symmetry survive, by the same lines. Transitivity fails, as the triple \( (1, 0) \), \( (0, 0) \), \( (1, 1) \) above shows, so there is no quotient set. Section 7.5 met the same failure in an exercise; it is the reason denominators must be non-zero.

**Why positive and not merely non-zero denominators?** Non-zero denominators would also give an equivalence relation, and, as the last example of this section shows, essentially the same set \( \nQ \). The difference appears with the order. With positive denominators, "\( [(p, q)] \) is positive" can mean "\( p > 0 \)", one inequality in \( \nZ \); with non-zero denominators, it would have to say "\( p \) and \( q \) have the same sign", and a naive comparison of two fractions breaks, as the warning at the end of this section shows.

::: {.warning}
Do not read \( [(p, q)] \) as the number \( p/q \). There is no division in \( \nZ \), and \( \nQ \) has no multiplication yet, so "\( p/q \)" means nothing at this point. The class is a set of pairs, and any statement made with one representative, such as "the denominator of \( [(1, 2)] \) is \( 2 \)", must be checked against all of them (here it fails: \( (2, 4) \) is also in the class). The fraction notation becomes honest once \( \nZ \) is placed inside \( \nQ \), at the end of this section.
:::

::: {.check}
Is \( (3, 4) \sim (-6, -8) \) in \( \nZ \times \nZ_{>0} \)?
:::

::: {.solution}
The question is malformed: \( -8 \notin \nZ_{>0} \), so \( (-6, -8) \) is not an element of \( \nZ \times \nZ_{>0} \), and \( \sim \) says nothing about it. In the variant with non-zero denominators (the last example of this section), the answer is yes: \( 3 \cdot (-8) = -24 = (-6) \cdot 4 \).
:::

This construction pays a debt. Section 7.5 described \( \nQ \) as the quotient of \( \nZ \times \nZ_{>0} \) by cross-multiplication while \( \nZ \) was still the school integers; now \( \nZ \) is the ring of Section 10.3, and the quotient is the definition of \( \nQ \).

## Adding and multiplying classes

The school rules \( \tfrac pq + \tfrac rs = \tfrac{ps + rq}{qs} \) and \( \tfrac pq \cdot \tfrac rs = \tfrac{pr}{qs} \) are a **heuristic** for the definition, nothing more; the definition below does not depend on them, and the proofs never use them.

::: {#def-rational-operations}
[Operations on the Rationals]

For \( [(p, q)], [(r, s)] \in \nQ \), define
\[
\begin{aligned}
[(p, q)] + [(r, s)] &\coloneqq [(ps + rq, \ qs)] , \\
[(p, q)] \cdot [(r, s)] &\coloneqq [(pr, \ qs)] , \\
-[(p, q)] &\coloneqq [(-p, \ q)] .
\end{aligned}
\]
:::

The right-hand sides are classes of elements of \( \nZ \times \nZ_{>0} \): since \( q > 0 \) and \( s > 0 \), \( qs > 0 \) by (O4), so \( qs \in \nZ_{>0} \) by @thm-integers-ordered-ring (b). Each formula is computed from **chosen representatives**, so the definition is legitimate only once we know that other representatives give the same class. That is the next proposition.

::: {#prp-rational-operations-well-defined}
[The Operations on the Rationals Are Well Defined]

Let \( X \coloneqq \nZ \times \nZ_{>0} \), with \( \sim \) as in @prp-rational-pairs-equivalence. The maps
\[
\begin{aligned}
g_+\bigl((p, q), (r, s)\bigr) &\coloneqq (ps + rq, \ qs) , \\
g_\cdot\bigl((p, q), (r, s)\bigr) &\coloneqq (pr, \ qs)
\end{aligned}
\]
from \( X \times X \) to \( X \) satisfy the hypotheses of @thm-well-defined-on-classes (b), and \( f(p, q) \coloneqq (-p, q) \) satisfies the hypothesis of @thm-well-defined-on-classes (a). Hence \( + \), \( \cdot \) and \( - \) of @def-rational-operations are functions \( \nQ \times \nQ \to \nQ \), \( \nQ \times \nQ \to \nQ \) and \( \nQ \to \nQ \).
:::

::: {.idea}
This is the move of Section 10.2, **check on representatives, one argument at a time**. Change the first pair to an equivalent one with the second fixed, then the second with the first fixed; @thm-well-defined-on-classes (b) joins the two changes by transitivity. Each change is one identity in \( \nZ \): expand both cross-products and use the hypothesis \( pq' = p'q \) (or \( rs' = r's \)) once.
:::

::: {.proof}
All computations are in the commutative ring \( \nZ \) (@thm-integers-commutative-ring), and we reorder products by (F5), (F6) without comment.

*Multiplication, first argument.* Let \( (p, q) \sim (p', q') \), so \( pq' = p'q \), and let \( (r, s) \in X \). We need \( (pr, qs) \sim (p'r, q's) \), that is, \( (pr)(q's) = (p'r)(qs) \). Indeed
\[
(pr)(q's) = (pq')(rs) = (p'q)(rs) = (p'r)(qs) .
\]

*Multiplication, second argument.* Let \( (r, s) \sim (r', s') \), so \( rs' = r's \), and let \( (p, q) \in X \). We need \( (pr)(qs') = (pr')(qs) \). Indeed
\[
(pr)(qs') = (pq)(rs') = (pq)(r's) = (pr')(qs) .
\]

*Addition, first argument.* Let \( pq' = p'q \). We need \( (ps + rq, qs) \sim (p's + rq', q's) \), that is, \( (ps + rq)(q's) = (p's + rq')(qs) \). By (F9),
\[
\begin{aligned}
(ps + rq)(q's) &= (pq')s^2 + rqq's , \\
(p's + rq')(qs) &= (p'q)s^2 + rqq's ,
\end{aligned}
\]
and the right-hand sides are equal because \( pq' = p'q \).

*Addition, second argument.* Let \( rs' = r's \). We need \( (ps + rq, qs) \sim (ps' + r'q, qs') \), that is, \( (ps + rq)(qs') = (ps' + r'q)(qs) \). By (F9),
\[
\begin{aligned}
(ps + rq)(qs') &= pqss' + (rs')q^2 , \\
(ps' + r'q)(qs) &= pqss' + (r's)q^2 ,
\end{aligned}
\]
and the right-hand sides are equal because \( rs' = r's \).

*Negation.* If \( pq' = p'q \), then \( (-p)q' = -(pq') = -(p'q) = (-p')q \) by @prp-ring-algebra (c), so \( (-p, q) \sim (-p', q') \).

So \( g_+ \) and \( g_\cdot \) satisfy the hypotheses of @thm-well-defined-on-classes (b): for a change of both arguments, \( g(x, y) \sim g(x', y) \sim g(x', y') \), and transitivity joins the two steps, which is what the proof of that lemma does. By its conclusion, there is exactly one function \( \nQ \times \nQ \to \nQ \) with \( [x] + [y] = [g_+(x, y)] \), and likewise for \( \cdot \). By @thm-well-defined-on-classes (a), \( -[(p, q)] \coloneqq [(-p, q)] \) is a function \( \nQ \to \nQ \). This proves the proposition.
:::

Not every formula in representatives passes this test, and the failures are instructive.

::: {#exm-ill-defined-fraction-sum}
[Formulas that ignore the class]

Decide which of the following rules define a function on \( \nQ \).

::: {.enumerate options="label=(\alph*)"}
1. \( [(p, q)] \mapsto p + q \in \nZ \).
2. \( [(p, q)] \mapsto p \in \nZ \).
3. \( [(p, q)] \mapsto [(p^2, q^2)] \in \nQ \).
:::
:::

::: {.solution}
(a) Not a function. \( [(1, 2)] = [(2, 4)] \), since \( 1 \cdot 4 = 2 \cdot 2 \), yet the rule gives \( 1 + 2 = 3 \) for one representative and \( 2 + 4 = 6 \) for the other. A function has one value at each argument (@def-function), and this rule offers two at the same class.

(b) Not a function, for the same pair: the outputs are \( 1 \) and \( 2 \).

(c) A function. First, \( q^2 > 0 \) by @prp-ordered-ring-rules (e), as \( q \ne 0 \), so \( (p^2, q^2) \in \nZ \times \nZ_{>0} \). If \( pq' = p'q \), then
\[
p^2 (q')^2 = (pq')^2 = (p'q)^2 = (p')^2 q^2 ,
\]
by (F5), (F6), so \( (p^2, q^2) \sim (p'^2, q'^2) \), and @thm-well-defined-on-classes (a) applies. The function is \( x \mapsto x \cdot x \), since \( [(p, q)] \cdot [(p, q)] = [(p^2, q^2)] \) by @def-rational-operations.
:::

The tempting argument for (a) runs: "a rational number \( x \) **is** \( p/q \), so \( p \) and \( q \) are determined by \( x \), and so is \( p + q \)". Its conclusion is false, and the flaw is the word "is": \( (p, q) \) is **a** representative of \( x \), and \( (2p, 2q) \) is another, just as legitimate. A rule defined through representatives is a function on classes only when every representative gives the same value, and that has to be proved, as in (c).

## The rationals form a field

The ring axioms for \( \nQ \) are checked by the move of Section 10.3, **reduce to the level below**: each side of an axiom, written on representatives, is the class of an explicit pair in \( \nZ \times \nZ_{>0} \), and the two pairs are compared by an identity in \( \nZ \). One small observation recurs: for every \( (p, q) \in \nZ \times \nZ_{>0} \) and \( k \in \nZ_{>0} \),
\[
(p, q) \sim (kp, kq) , \quad \text{since } p(kq) = (kp)q .
\]
Scaling both entries by the same positive integer does not change the class.

::: {#thm-rationals-field}
[The Rationals Form a Field]

\( \nQ \), with the operations of @def-rational-operations, is a field (@def-commutative-ring-and-field), with zero \( [(0, 1)] \) and one \( [(1, 1)] \). A rational number \( [(p, q)] \) is zero if and only if \( p = 0 \). If \( p > 0 \), its inverse is \( [(q, p)] \); if \( p < 0 \), its inverse is \( [(-q, -p)] \).
:::

::: {.idea}
Eight laws are identities between pairs of integers, checked in a table as for \( \nZ \); as there, two rows give pairs that are related rather than equal, and for (F9) the scaling observation is what relates them. The genuinely new axiom is (F8): inverting \( [(p, q)] \) should swap numerator and denominator, and the sign of \( p \) decides whether the swapped pair is allowed.
:::

::: {.proof}
By @prp-rational-operations-well-defined, the operations are functions. Let \( x, y, z \in \nQ \); by @def-quotient-set, \( x = [(p, q)] \), \( y = [(r, s)] \), \( z = [(t, u)] \) with \( p, r, t \in \nZ \) and \( q, s, u \in \nZ_{>0} \). As in Section 10.3, "equal" means that the two pairs are the same pair of integers, by the laws (F1)–(F9) of \( \nZ \) (@thm-integers-commutative-ring); "related" means that they are related by \( \sim \), so that the classes agree by @thm-classes-partition (b).

| Axiom | left side, as a pair | right side, as a pair | why the classes agree |
|---|---|---|---|
| (F1) | \( (ps + rq, qs) \) | \( (rq + ps, sq) \) | equal |
| (F2) | \( ((ps + rq)u + tqs, \ qsu) \) | \( (psu + (ru + ts)q, \ qsu) \) | equal: both first entries are \( psu + qru + qst \) |
| (F3) \( x + [(0, 1)] = x \) | \( (p \cdot 1 + 0 \cdot q, \ q \cdot 1) \) | \( (p, q) \) | equal, by @prp-ring-algebra (b) |
| (F4) \( x + (-x) = [(0, 1)] \) | \( (pq + (-p)q, \ q^2) = (0, q^2) \) | \( (0, 1) \) | related: \( 0 \cdot 1 = 0 \cdot q^2 \) |
| (F5) | \( ((pr)t, \ (qs)u) \) | \( (p(rt), \ q(su)) \) | equal |
| (F6) | \( (pr, qs) \) | \( (rp, sq) \) | equal |
| (F7) \( x \cdot [(1, 1)] = x \) | \( (p \cdot 1, \ q \cdot 1) \) | \( (p, q) \) | equal |
| (F9) | \( (p(ru + ts), \ q(su)) \) | \( ((pr)(qu) + (pt)(qs), \ (qs)(qu)) \) | related: the right pair is the left pair scaled by \( q \) |

In (F4), \( pq + (-p)q = pq - pq = 0 \) by @prp-ring-algebra (c), and \( 0 \cdot 1 = 0 = 0 \cdot q^2 \) by @prp-ring-algebra (b). In (F9), the right side is \( xy + xz = [(pr, qs)] + [(pt, qu)] \); its first entry is \( q(pru + pts) = q \cdot p(ru + ts) \) and its second is \( q \cdot q(su) \), so the scaling observation above, with \( k = q \), relates it to the left pair.

*The zero.* \( [(p, q)] = [(0, 1)] \) if and only if \( p \cdot 1 = 0 \cdot q \), that is, \( p = 0 \).

*\( 1 \ne 0 \).* \( [(1, 1)] = [(0, 1)] \) would need \( 1 = 0 \) in \( \nZ \), which @thm-integers-commutative-ring excludes.

*(F8).* Let \( x = [(p, q)] \ne 0 \), so \( p \ne 0 \). If \( p > 0 \), then \( p \in \nZ_{>0} \), so \( (q, p) \in \nZ \times \nZ_{>0} \), and
\[
[(p, q)] \cdot [(q, p)] = [(pq, \ qp)] = [(1, 1)] ,
\]
since \( (pq) \cdot 1 = 1 \cdot (qp) \).
If \( p < 0 \), then \( -p > 0 \) by @prp-ordered-ring-rules (a), so \( (-q, -p) \in \nZ \times \nZ_{>0} \), and
\[
\begin{aligned}
[(p, q)] \cdot [(-q, -p)] &= [(p(-q), \ q(-p))] \\
&= [(-(pq), \ -(pq))] = [(1, 1)] ,
\end{aligned}
\]
by @prp-ring-algebra (c) and \( (-(pq)) \cdot 1 = 1 \cdot (-(pq)) \). By (O1), one of the two cases occurs. So every non-zero element has an inverse, and \( \nQ \) is a field. This proves the theorem.
:::

Six rows of the table are "equal" and two, (F4) and (F9), are "related"; the second needs the scaling observation because the product formula multiplies denominators even when they are already equal. The case split in (F8) is the price of the convention: the obvious inverse \( [(q, p)] \) of a negative \( [(p, q)] \) is not a class at all, since its "denominator" \( p \) is negative, and we must move the sign to the numerator.

::: {.check}
Compute \( [(1, 2)] + [(1, 3)] \) and \( [(-3, 4)]^{-1} \), and check the second answer by multiplying.
:::

::: {.solution}
\( [(1, 2)] + [(1, 3)] = [(1 \cdot 3 + 1 \cdot 2, \ 2 \cdot 3)] = [(5, 6)] \). For \( [(-3, 4)] \) the numerator is negative, so the inverse is \( [(-4, 3)] \). Check: \( [(-3, 4)] \cdot [(-4, 3)] = [(12, 12)] \), and \( (12, 12) \sim (1, 1) \) since \( 12 \cdot 1 = 1 \cdot 12 \).
:::

## The integers inside the rationals

As \( \nN \) sat inside \( \nZ \) through \( \iota \) (@prp-naturals-embed-integers), \( \nZ \) sits inside \( \nQ \) through the classes with denominator \( 1 \).

::: {#prp-integers-embed-rationals}
[The Integers Embed in the Rationals]

Let \( j \colon \nZ \to \nQ \), \( j(m) \coloneqq [(m, 1)] \). Then \( j \) is injective, and for all \( m, n \in \nZ \),
\[
j(m + n) = j(m) + j(n), \qquad j(mn) = j(m) j(n), \qquad j(-m) = -j(m),
\]
with \( j(0) = 0 \) and \( j(1) = 1 \). Moreover, writing \( a/b \coloneqq ab^{-1} \) in the field \( \nQ \):

::: {.enumerate options="label=(\alph*)"}
1. for \( p \in \nZ \) and \( q \in \nZ_{>0} \), \( [(p, q)] = j(p) \cdot j(q)^{-1} = j(p)/j(q) \);
2. every rational number is \( j(p)/j(q) \) for some \( p \in \nZ \) and \( q \in \nZ_{>0} \), and for \( p, r \in \nZ \) and \( q, s \in \nZ_{>0} \), \( j(p)/j(q) = j(r)/j(s) \) if and only if \( ps = rq \);
3. \( \nQ = \{ j(m)/j(n) : m \in \nZ, \ n \in \nZ_{>0} \} \).
:::
:::

::: {.idea}
The classes with denominator \( 1 \) add and multiply exactly as their numerators do, by the formulas of @def-rational-operations with \( q = s = 1 \). For (a), \( [(1, q)] \) is the inverse of \( [(q, 1)] \), and multiplying it by \( [(p, 1)] \) gives \( [(p, q)] \); (b) and (c) are (a) read through @thm-classes-partition.
:::

::: {.proof}
*Injective.* If \( j(m) = j(n) \), then \( (m, 1) \sim (n, 1) \) by @thm-classes-partition (b), that is, \( m \cdot 1 = n \cdot 1 \), so \( m = n \).

*Operations.* By @def-rational-operations, \( j(m) + j(n) = [(m \cdot 1 + n \cdot 1, \ 1 \cdot 1)] = [(m + n, 1)] = j(m + n) \), \( j(m) j(n) = [(mn, 1)] = j(mn) \), and \( -j(m) = [(-m, 1)] = j(-m) \). Also \( j(0) = [(0, 1)] \) and \( j(1) = [(1, 1)] \) are the zero and one of \( \nQ \) (@thm-rationals-field).

(a) Since \( q > 0 \), \( j(q) = [(q, 1)] \ne 0 \), and by @thm-rationals-field its inverse is \( [(1, q)] \) (the case of a positive numerator; inverses are unique, Section 10.3). Hence
\[
\begin{aligned}
j(p) \cdot j(q)^{-1} &= [(p, 1)] \cdot [(1, q)] \\
&= [(p \cdot 1, \ 1 \cdot q)] = [(p, q)] .
\end{aligned}
\]

(b) Every element of \( \nQ \) is \( [(p, q)] \) for some \( (p, q) \in \nZ \times \nZ_{>0} \) (@def-quotient-set), which is \( j(p)/j(q) \) by (a). By (a) again, \( j(p)/j(q) = j(r)/j(s) \) means \( [(p, q)] = [(r, s)] \), which holds if and only if \( ps = rq \) (@thm-classes-partition (b)).

(c) Each \( j(m)/j(n) \) lies in \( \nQ \), and every element of \( \nQ \) has this form by (b). This proves the proposition.
:::

**Identification.** From now on we write \( m \) for \( j(m) \), as Section 10.2 wrote \( n \) for \( \iota(n) \), and regard \( \nZ \) as a subset of \( \nQ \); together with Section 10.2, \( \nN \subseteq \nZ \subseteq \nQ \). This is a convenient abuse, made honest by \( j \): it is injective and carries \( 0 \), \( 1 \), \( + \), \( \cdot \) and \( - \) of \( \nZ \) to those of \( \nQ \), so a computation with integers gives the same result read in \( \nZ \) or in \( \nQ \). (One could replace \( j(\nZ) \) by \( \nZ \) itself inside \( \nQ \), but nothing needs it.) With this convention, (a)–(c) read:
\[
\begin{gathered}
[(p, q)] = \frac{p}{q} , \qquad \frac{p}{q} = \frac{r}{s} \iff ps = rq , \\
\nQ = \Bigl\{ \frac{m}{n} : m \in \nZ, \ n \in \nZ_{>0} \Bigr\} .
\end{gathered}
\]
The last equation is the description of \( \nQ \) that Section 7.1 took as a definition; it is now a theorem about the constructed set. The fraction bar is division in the field \( \nQ \), and the school rules for fractions, such as \( \tfrac pq + \tfrac rs = \tfrac{ps + rq}{qs} \), are now the formulas of @def-rational-operations read through (a). The order of \( \nQ \), and the fact that \( j \) respects it, are Section 10.5's business.

## Other denominators

The convention of positive denominators was a choice. The next example shows that the other natural choice gives the same set of rational numbers, and where it would cost us.

::: {#exm-fractions-nonzero-denominators}
[Non-zero denominators give the same rationals]

Let \( Y \coloneqq \nZ \times (\nZ \setminus \{0\}) \), and for \( (p, q), (r, s) \in Y \) let \( (p, q) \approx (r, s) \) mean \( ps = rq \). Show that \( \approx \) is an equivalence relation on \( Y \), and that
\[
I \colon \nQ \to Y/{\approx} , \qquad I\bigl([(p, q)]\bigr) \coloneqq [(p, q)]_{\approx} ,
\]
is a well-defined bijection.
:::

::: {.solution}
*Equivalence relation.* The proof of @prp-rational-pairs-equivalence works word for word: it used only that the denominator \( s \) of the middle pair is non-zero, and in \( Y \) every denominator is non-zero.

*Well defined.* Apply @thm-well-defined-on-classes (a) to the inclusion \( (p, q) \mapsto (p, q) \) from \( \nZ \times \nZ_{>0} \) to \( Y \): if \( (p, q) \sim (p', q') \), then \( pq' = p'q \), which says \( (p, q) \approx (p', q') \).

*Injective.* If \( [(p, q)]_{\approx} = [(p', q')]_{\approx} \), then \( (p, q) \approx (p', q') \) by @thm-classes-partition (b), so \( pq' = p'q \), so \( (p, q) \sim (p', q') \) and \( [(p, q)] = [(p', q')] \).

*Surjective.* Let \( [(p, q)]_{\approx} \in Y/{\approx} \), with \( q \ne 0 \). By (O1), \( q > 0 \) or \( q < 0 \). If \( q > 0 \), the class is \( I([(p, q)]) \). If \( q < 0 \), then \( -q > 0 \) (@prp-ordered-ring-rules (a)), and \( (p, q) \approx (-p, -q) \), since \( p(-q) = -(pq) = (-p)q \) by @prp-ring-algebra (c); so the class is \( I([(-p, -q)]) \).

So \( I \) is a bijection: the two constructions have "the same" rational numbers, matched by \( I \).
:::

::: {.warning}
The rule "\( [(p, q)]_{\approx} < [(r, s)]_{\approx} \) if and only if \( ps < rq \)" is **not** well defined on \( Y/{\approx} \). Compare \( (0, 1) \) with \( (1, 1) \): \( 0 \cdot 1 < 1 \cdot 1 \), that is, \( 0 < 1 \), true. Now replace \( (1, 1) \) by the equivalent \( (-1, -1) \): the rule asks whether \( 0 \cdot (-1) < (-1) \cdot 1 \), that is, \( 0 < -1 \), which is false. Multiplying an inequality by a negative denominator reverses it (@prp-ordered-ring-rules (d)), so the rule's verdict depends on the representative. With positive denominators this cannot happen, which is why @def-rationals-as-classes uses them.
:::

## Exercises

### A. Check your understanding

::: {#exr-rationals-as-classes-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. In @def-rational-operations, why is \( qs \in \nZ_{>0} \)?
2. Where does the proof of transitivity in @prp-rational-pairs-equivalence use that a denominator is non-zero, and which denominator is it?
3. Find the inverse of \( [(-3, 5)] \) in \( \nQ \), as a class with positive denominator.
4. True or false: \( j(2)^{-1} = [(1, 2)] \). Give a reason.
:::
:::

::: {.solution}
(a) \( q, s \in \nZ_{>0} \) means \( q > 0 \) and \( s > 0 \) (@thm-integers-ordered-ring (b)); then \( qs > 0 \) by (O4), so \( qs \in \nZ_{>0} \), again by @thm-integers-ordered-ring (b).

(b) In the last step: from \( (pu - tq)s = 0 \) it concludes \( pu - tq = 0 \) by @prp-ordered-ring-rules (f), which needs \( s \ne 0 \). Here \( s \) is the denominator of the **middle** pair \( (r, s) \).

(c) The numerator \( -3 \) is negative, so by @thm-rationals-field the inverse is \( [(-5, 3)] \). Check: \( [(-3, 5)] \cdot [(-5, 3)] = [(15, 15)] = [(1, 1)] \), since \( 15 \cdot 1 = 1 \cdot 15 \).

(d) True. \( j(2) = [(2, 1)] \) has positive numerator, so its inverse is \( [(1, 2)] \) by @thm-rationals-field; directly, \( [(2, 1)] \cdot [(1, 2)] = [(2, 2)] = [(1, 1)] \).
:::

### B. Practice

::: {#exr-rationals-as-classes-b1}
[B1: Three rows in detail]

Let \( x = [(p, q)] \), \( y = [(r, s)] \), \( z = [(t, u)] \) be rational numbers. Verify in detail, naming the law of \( \nZ \) used at each step, the rows (F9), (F4) and (F2) of the table in the proof of @thm-rationals-field.
:::

::: {.solution}
All operations are those of @def-rational-operations; (F1)–(F9) refer to the laws of \( \nZ \) (@thm-integers-commutative-ring).

(F9). \( y + z = [(ru + ts, \ su)] \), so \( x(y + z) = [(p(ru + ts), \ q(su))] = [(pru + pts, \ qsu)] \) by (F9) and (F5). On the other side, \( xy = [(pr, qs)] \) and \( xz = [(pt, qu)] \), so
\[
\begin{aligned}
xy + xz &= [((pr)(qu) + (pt)(qs), \ (qs)(qu))] \\
&= [(q(pru + pts), \ q(qsu))] ,
\end{aligned}
\]
by (F5), (F6) and (F9). The pairs \( (A, B) \coloneqq (pru + pts, qsu) \) and \( (qA, qB) \) are related, since \( A(qB) = (qA)B \) by (F5), (F6). By @thm-classes-partition (b), \( x(y + z) = xy + xz \).

(F4). \( -x = [(-p, q)] \), so \( x + (-x) = [(pq + (-p)q, \ qq)] \). By @prp-ring-algebra (c), \( (-p)q = -(pq) \), so the numerator is \( pq + (-(pq)) = 0 \) by (F4). The pair \( (0, q^2) \) is related to \( (0, 1) \), since \( 0 \cdot 1 = 0 = 0 \cdot q^2 \) (@prp-ring-algebra (b)). So \( x + (-x) = [(0, 1)] \).

(F2). \( x + y = [(ps + rq, qs)] \), so
\[
\begin{aligned}
(x + y) + z &= [((ps + rq)u + t(qs), \ (qs)u)] \\
&= [(psu + qru + qst, \ qsu)] ,
\end{aligned}
\]
by (F9), (F5), (F6). And \( y + z = [(ru + ts, su)] \), so
\[
\begin{aligned}
x + (y + z) &= [(p(su) + (ru + ts)q, \ q(su))] \\
&= [(psu + qru + qst, \ qsu)] ,
\end{aligned}
\]
by the same laws. The pairs are equal, so \( (x + y) + z = x + (y + z) \).
:::

::: {#exr-rationals-as-classes-b2}
[B2: Addition is well defined]

Prove, without looking back at @prp-rational-operations-well-defined, that the addition of @def-rational-operations is well defined. The first half is done for you.

*Change the first argument.* Let \( (p, q) \sim (p', q') \), that is, \( pq' = p'q \), and fix \( (r, s) \). Then
\[
\begin{aligned}
(ps + rq)(q's) &= (pq')s^2 + rqq's \\
&= (p'q)s^2 + rqq's = (p's + rq')(qs) ,
\end{aligned}
\]
so \( (ps + rq, qs) \sim (p's + rq', q's) \).

*Name the move, then complete it.*
:::

::: {.solution}
The move is **check on representatives, one argument at a time**: having changed the first argument with the second fixed, change the second with the first fixed, and join the two changes by transitivity.

*Change the second argument.* Let \( (r, s) \sim (r', s') \), that is, \( rs' = r's \), and fix \( (p, q) \). Then, by (F5), (F6), (F9) in \( \nZ \),
\[
\begin{aligned}
(ps + rq)(qs') &= pqss' + (rs')q^2 \\
&= pqss' + (r's)q^2 = (ps' + r'q)(qs) ,
\end{aligned}
\]
so \( (ps + rq, qs) \sim (ps' + r'q, qs') \).

*Join.* Let \( (p, q) \sim (p', q') \) and \( (r, s) \sim (r', s') \). Write \( g \) for the sum formula on representatives. The first step, with \( (r, s) \) fixed, gives \( g((p, q), (r, s)) \sim g((p', q'), (r, s)) \); the second, with \( (p', q') \) fixed, gives \( g((p', q'), (r, s)) \sim g((p', q'), (r', s')) \). By transitivity (@prp-rational-pairs-equivalence), \( g((p, q), (r, s)) \sim g((p', q'), (r', s')) \), so the classes \( [g((p, q), (r, s))] \) and \( [g((p', q'), (r', s'))] \) are equal (@thm-classes-partition (b)). These are exactly the hypotheses, and the conclusion, of @thm-well-defined-on-classes (b), which then gives addition as a function \( \nQ \times \nQ \to \nQ \).
:::

### C. Going deeper

::: {#exr-rationals-as-classes-c1}
[C1: The least denominator]

::: {.enumerate options="label=(\alph*)"}
1. Show that the rule "\( [(p, q)] \mapsto q \)" does not define a function \( \nQ \to \nZ_{>0} \).
2. Prove that there is exactly one function \( N \colon \nQ \to \nZ_{>0} \) such that, for every \( x \in \nQ \), \( N(x) \) is the least \( q \in \nZ_{>0} \) for which \( x = [(p, q)] \) for some \( p \in \nZ \).
3. Compute \( N(6/4) \), justifying that no smaller denominator is possible.
:::
:::

::: {.solution}
[Hint 1]

For (b), fix \( x \) and look at the set of all denominators of representatives of \( x \). Which result of Section 10.3 gives a least element?
:::

::: {.solution}
[Hint 2]

Let \( D_x \coloneqq \{ q \in \nZ_{>0} : (p, q) \in x \text{ for some } p \in \nZ \} \). It is non-empty because a class contains its representative.
:::

::: {.solution}
(a) \( [(1, 2)] = [(2, 4)] \), since \( 1 \cdot 4 = 2 \cdot 2 \), but the rule gives \( 2 \) for one representative and \( 4 \) for the other. A function has one value at each argument (@def-function).

(b) For \( x \in \nQ \), let \( D_x \coloneqq \{ q \in \nZ_{>0} : (p, q) \in x \text{ for some } p \in \nZ \} \). Note that \( x = [(p, q)] \) holds if and only if \( (p, q) \in x \), by @thm-classes-partition (a), (b). So \( D_x \) is the set of denominators allowed in the definition of \( N(x) \).

*\( D_x \) has a least element.* By @def-quotient-set, \( x = [(p_0, q_0)] \) for some pair, and \( (p_0, q_0) \in x \) by @thm-classes-partition (a), so \( q_0 \in D_x \) and \( D_x \) is non-empty. Every element of \( D_x \) is positive, so \( 0 \) is an integer lower bound. By @prp-integer-least-element, \( D_x \) has a least element, and it is unique, by antisymmetry of \( \le \) (@prp-ordered-ring-rules (i)).

*Existence and uniqueness of \( N \).* Let \( N \) be the function whose graph is \( \{ (x, \min D_x) : x \in \nQ \} \subseteq \nQ \times \nZ_{>0} \). Each \( x \) has exactly one partner \( \min D_x \), so \( N \) is a function (@def-function), and it has the required property. Any function with the property must take the value \( \min D_x \) at every \( x \), so it equals \( N \) (@prp-function-equality). Unlike the rule in (a), \( N \) is defined from the class \( x \) itself, not from a chosen representative, so there is nothing to check for well-definedness.

(c) \( 6/4 = [(6, 4)] \) by @prp-integers-embed-rationals (a). A pair \( (p, q) \) lies in this class if and only if \( 4p = 6q \).

- \( q = 1 \) is impossible: it needs \( 4p = 6 \). By discreteness (@thm-integers-ordered-ring (c)), \( p \le 1 \) or \( p \ge 2 \). If \( p \le 1 \), then \( 4p \le 4 < 6 \); if \( p \ge 2 \), then \( 4p \ge 8 > 6 \), by @prp-ordered-ring-rules (c) (or equality). Either way \( 4p \ne 6 \), by (O1).
- \( q = 2 \) works: \( 4 \cdot 3 = 12 = 6 \cdot 2 \), so \( (3, 2) \in [(6, 4)] \).

Since \( 1 \) is the only element of \( \nZ_{>0} \) below \( 2 \) (discreteness), \( N(6/4) = 2 \).

**Marking scheme.** (10 points)
- 2: (a) exhibits two representatives of one class with different denominators.
- 2: (b) defines the set of denominators of \( x \) from the class, and shows it non-empty.
- 2: (b) gets a least element from @prp-integer-least-element, with the lower bound named.
- 2: (b) explains why this defines exactly one function (one value per class; any such function has those values).
- 2: (c) shows \( 4p = 6 \) has no integer solution and exhibits \( (3, 2) \).
Fatal errors (0 for the step): defining \( N([(p, q)]) \) as "\( q \) divided by a common factor" (divisibility is not available, and the formula uses a representative); in (c), "\( 4p = 6 \) has no solution since \( p = 3/2 \)" (uses division in \( \nQ \) to decide a question about \( \nZ \) without the discreteness argument).
:::

::: {#exr-rationals-as-classes-c2}
[C2: Find the error]

Here is a proof that multiplication on \( \nQ \) is well defined. Is the conclusion true? Is the proof correct? If not, name the first line that fails, the error, and give a counterexample to the step.

> (1) Let \( (p, q) \sim (p', q') \), and let \( (r, s) \in \nZ \times \nZ_{>0} \). (2) Then \( p/q = p'/q' \). (3) So \( (p/q)(r/s) = (p'/q')(r/s) \). (4) That is, \( [(pr, qs)] = [(p'r, q's)] \), so the product does not depend on the first representative. (5) The second argument is handled in the same way.
:::

::: {.solution}
The conclusion is **true**: it is @prp-rational-operations-well-defined. The proof is **not** correct.

*The failing line is (3).* Line (2) is a harmless restatement of (1): it says that \( (p, q) \) and \( (p', q') \) name the same class. Line (3) then multiplies that class by \( r/s \), using the multiplication of \( \nQ \). But that multiplication is exactly what is being shown to exist: until it is known to be well defined, "\( (p/q)(r/s) \)" has no meaning, or rather means "\( [(pr, qs)] \), computed from the representative \( (p, q) \)", and whether this depends on the representative is the claim. The line cites the goal, which is circular: entry (N9) of @exm-not-allowed-catalogue.

*Counterexample to the step.* The inference "\( p/q = p'/q' \), so \( F(p, q) = F(p', q') \)" fails for formulas \( F \) in representatives. With \( F(p, q) \coloneqq p + q \), the same lines "prove" that \( [(p, q)] \mapsto p + q \) is a function on \( \nQ \), since "\( p + q \) is a function of \( p/q \)". It is not: \( (1, 2) \sim (2, 4) \) and \( 1 + 2 \ne 2 + 4 \) (@exm-ill-defined-fraction-sum (a)).

*Repair.* Replace (2)–(3) by an identity in \( \nZ \): from \( pq' = p'q \), \( (pr)(q's) = (pq')(rs) = (p'q)(rs) = (p'r)(qs) \), so \( (pr, qs) \sim (p'r, q's) \). Do the same for the second argument, and conclude with @thm-well-defined-on-classes (b). Lines (1), (4) and (5) are correct as stated, once (3) is replaced.

**Marking scheme.** (10 points)
- 2: says that the conclusion is true and that the proof is not correct.
- 3: names line (3) as the failing line and explains that it uses the multiplication of \( \nQ \), which is being defined.
- 2: names the error as circular, entry (N9).
- 2: gives a counterexample to the step (any formula in representatives that is not constant on classes, such as \( p + q \)).
- 1: gives the repair through the integer identity \( (pr)(q's) = (p'r)(qs) \).
Fatal errors (0 for the step): declaring the conclusion false; blaming line (1) or (2), which only restate the hypothesis.
:::

<!-- dependency ledger
prp-rational-pairs-equivalence (proof): s in Z_{>0} gives s > 0, hence s != 0 | thm-integers-ordered-ring (b) (recalled before the statement) and (O1)
def-rationals-as-classes (example): (r, s) ~ (1, 2) forces r > 0 | prp-ordered-ring-rules (b) (cited) and 2r = r + r by (F9), (F7)
def-rationals-as-classes (example): Section 7.5 met the transitivity failure for Z x N | Ch 7 Section 7.5, exercise B1 (b) (prose comparison only; nothing depends on it)
prp-rational-operations-well-defined (proof): reordering products and sums in Z | thm-integers-commutative-ring (F1), (F2), (F5), (F6), (F9) (cited at the start of the proof)
thm-rationals-field (proof): scaling (p, q) ~ (kp, kq) | inline (stated before the theorem)
prp-integers-embed-rationals (proof): the inverse of a non-zero element of a field is unique | Section 10.3, the paragraph after prp-ring-algebra (inline there; no label)
exr-rationals-as-classes-c1 (solution): elements of Z_{>0} are >= 0, so 0 is a lower bound; 1 is the only element of Z_{>0} below 2 | thm-integers-ordered-ring (b), (c) (cited)
exr-rationals-as-classes-c1 (solution): 4 < 6 < 8 in Z | thm-integers-ordered-ring (a) (order of N extended), computed in N
-->
