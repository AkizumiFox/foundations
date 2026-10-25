# Addition and Negatives

Like every section of this chapter, this one is optional: nothing outside Chapter 7 depends on it. Sections 7.1 and 7.2 made cuts and ordered them, and the least upper bound property came almost for free, as a union (@thm-dedekind-lub). Now the arithmetic. Adding two cuts is the obvious thing, and it works; the zero cut works too, once (C3) is used. Negatives are where the obvious recipe fails, on the simplest cuts of all, and the repair is a small positive margin. The proof that the repaired negative is right is the **walk up by ε** (@lem-cut-step) worked in full. The section ends with cuts forming an ordered group under addition.

Throughout, \( \nQ \) is the ordered field of @thm-rationals-ordered-field, and every letter \( p, q, r, s, t, x \) stands for a rational. We use the rules of an ordered field for rationals without comment: (F1)–(F9) of @def-commutative-ring-and-field, (O1)–(O4) of @def-ordered-ring-and-field, @prp-ordered-ring-rules, and the halves of @prp-ordered-field-halves (b).

## Adding two cuts

A cut is a set of rationals, so the first candidate for a sum is the set of all sums.

::: {#def-cut-sum}
[Sum of Cuts]

For cuts \( \alpha \) and \( \beta \), the **sum** is the set
\[
\alpha + \beta \coloneqq \{ p + q : p \in \alpha, \ q \in \beta \} .
\]
:::

In symbols, \( x \in \alpha + \beta \iff \exists p \in \alpha \ \exists q \in \beta \ \ x = p + q \). This is the set sum \( A + B \) of *Sets, Relations, and Cardinality*, Section 1.7 (@fd2:exm-sets-of-numbers-as-images), applied to two sets of rationals: the same notation with the same meaning. For instance, if \( p < 1 \) and \( q < 2 \), then \( p + q < 3 \), so \( D_1 + D_2 \subseteq D_3 \); the Quick check later in this section shows how the reverse inclusion goes for a similar pair.

The definition makes sense for any two sets of rationals. The work is to show that a sum of cuts is again a cut, and that this addition behaves.

::: {#thm-cut-sum}
[The Sum of Two Cuts Is a Cut]

For all cuts \( \alpha \) and \( \beta \), the set \( \alpha + \beta \) is a cut. Addition of cuts is commutative and associative: for all cuts \( \alpha \), \( \beta \), \( \gamma \),
\[
\alpha + \beta = \beta + \alpha \qquad \text{and} \qquad (\alpha + \beta) + \gamma = \alpha + (\beta + \gamma) .
\]
:::

::: {.idea}
Each cut condition for \( \alpha + \beta \) comes from the same condition for \( \alpha \) or \( \beta \). A rational outside a cut is above every element of it (@lem-cut-separation), so the sum of a point outside \( \alpha \) and a point outside \( \beta \) is outside the sum. To go down from \( p + q \), go down in the first summand. To go up, go up in the first summand. The two laws are laws of \( \nQ \), applied element by element.
:::

::: {.proof}
Let \( \alpha \) and \( \beta \) be cuts. We check (C1)–(C3) of @def-dedekind-cut for \( \alpha + \beta \).

(C1) By (C1) for \( \alpha \) and \( \beta \), there are \( p_0 \in \alpha \) and \( q_0 \in \beta \), so \( p_0 + q_0 \in \alpha + \beta \), and \( \alpha + \beta \ne \emptyset \). Also by (C1), there are \( a \in \nQ \setminus \alpha \) and \( b \in \nQ \setminus \beta \). Let \( p \in \alpha \) and \( q \in \beta \). By @lem-cut-separation, \( p < a \) and \( q < b \), so \( p + q < a + b \) by @prp-ordered-ring-rules (b). So no element of \( \alpha + \beta \) equals \( a + b \), and \( a + b \notin \alpha + \beta \). Hence \( \alpha + \beta \ne \nQ \).

(C2) Let \( x \in \alpha + \beta \) and \( y \in \nQ \) with \( y < x \). Write \( x = p + q \) with \( p \in \alpha \), \( q \in \beta \). Adding \( -q \) to \( y < p + q \) gives \( y - q < p \) (O3), so \( y - q \in \alpha \) by (C2) for \( \alpha \). Hence \( y = (y - q) + q \in \alpha + \beta \).

(C3) Let \( x = p + q \in \alpha + \beta \) with \( p \in \alpha \), \( q \in \beta \). By (C3) for \( \alpha \) there is \( p' \in \alpha \) with \( p' > p \). Then \( p' + q \in \alpha + \beta \) and \( p' + q > p + q = x \) (O3).

So \( \alpha + \beta \) is a cut.

*Commutativity.* If \( x \in \alpha + \beta \), then \( x = p + q \) with \( p \in \alpha \), \( q \in \beta \), and \( x = q + p \in \beta + \alpha \) by (F1) in \( \nQ \). So \( \alpha + \beta \subseteq \beta + \alpha \); exchanging the roles of \( \alpha \) and \( \beta \) gives the reverse inclusion.

*Associativity.* Let \( \gamma \) be a cut. \( (\subseteq) \) If \( x \in (\alpha + \beta) + \gamma \), then \( x = y + s \) with \( y \in \alpha + \beta \) and \( s \in \gamma \), and \( y = p + q \) with \( p \in \alpha \), \( q \in \beta \). By (F2) in \( \nQ \), \( x = p + (q + s) \), and \( q + s \in \beta + \gamma \), so \( x \in \alpha + (\beta + \gamma) \). \( (\supseteq) \) If \( x = p + z \) with \( p \in \alpha \) and \( z = q + s \in \beta + \gamma \), then \( x = (p + q) + s \in (\alpha + \beta) + \gamma \), by (F2) again. This proves the theorem.
:::

Only (C3) for \( \alpha \) was needed in the third step; (C3) for \( \beta \) would serve equally. The two laws used nothing about cuts at all: they hold for the set sum of arbitrary sets of rationals (commutativity for any two, associativity for any three), and Exercise B2 asks you to check associativity in this generality.

## The zero cut

The natural zero is \( D_0 = \{ r \in \nQ : r < 0 \} \), the rational cut of \( 0 \) (@def-rational-cut). Adding an element of \( D_0 \) pushes a rational down, so \( \alpha + D_0 \) cannot leave \( \alpha \). The other inclusion needs a point of \( \alpha \) strictly above the given one.

::: {#prp-cut-sum-zero}
[The Zero Cut]

For every cut \( \alpha \), \( \alpha + D_0 = \alpha \).
:::

::: {.proof}
Let \( \alpha \) be a cut.

\( (\subseteq) \) Let \( x \in \alpha + D_0 \), say \( x = p + q \) with \( p \in \alpha \) and \( q < 0 \). Then \( p + q < p + 0 = p \) (O3), so \( x \in \alpha \) by (C2).

\( (\supseteq) \) Let \( p \in \alpha \). By (C3) there is \( p' \in \alpha \) with \( p' > p \); fix one \( \bigl[ \rulename{\exists E} \bigr] \) (@fd1:def-rules-existential). Then \( p - p' < 0 \) by @prp-ordered-ring-rules (a), so \( p - p' \in D_0 \), and
\[
p = p' + (p - p') \in \alpha + D_0 .
\]
As \( p \in \alpha \) was arbitrary, \( \alpha \subseteq \alpha + D_0 \) \( \bigl[ \rulename{\forall I} \bigr] \) (@fd1:def-rules-universal).
:::

The second half used (C3), and it cannot do without it. The tempting shortcut "\( p = p + 0 \)" fails because \( 0 \notin D_0 \); Exercise C2 shows a proof built on that shortcut. A set with a largest element fails the proposition: \( A \coloneqq \{ r \in \nQ : r \le 1 \} \) satisfies (C1) and (C2), and \( A + D_0 = D_1 \), since \( a \le 1 \), \( q < 0 \) give \( a + q < 1 \), and every \( x < 1 \) is \( 1 + (x - 1) \); so adding \( D_0 \) removes \( 1 \). Section 7.1's example of a set with a largest element makes a related point about cancellation (@exm-cut-with-largest-element).

## Negatives

*Before reading on.* Find a cut \( \beta \) with \( D_1 + \beta = D_0 \). Then try to write down a recipe that produces such a \( \beta \) from any cut \( \alpha \), so that \( \alpha + \beta = D_0 \).

For \( D_1 \) the answer is \( \beta = D_{-1} \). Indeed, \( p < 1 \) and \( q < -1 \) give \( p + q < 0 \); and for \( s < 0 \), put \( h \coloneqq -s/2 > 0 \), so that \( s = (1 - h) + (-1 - h) \) with \( 1 - h < 1 \) and \( -1 - h < -1 \). For a general \( \alpha \), a natural recipe reads the picture of a cut as a downset: the negative of "the rationals below \( x \)" should be "the rationals below \( -x \)", and those are the negatives of the rationals **above** \( x \), that is, of the rationals outside \( \alpha \). The example below tests that recipe.

::: {#exm-naive-negative .optional}
[The Negatives of the Outside]

For a cut \( \alpha \), is the set \( \{ -q : q \in \nQ \setminus \alpha \} \) a cut? Test it on \( \sigma = \{ p \in \nQ : p \le 0 \text{ or } p^2 < 2 \} \) (@exm-cut-sqrt2) and on \( D_1 \). Then decide in general. Is the set \( \{ -p : p \in \alpha \} \) a cut?
:::

::: {.solution}
*For \( \sigma \) it works.* A rational \( q \) is outside \( \sigma \) exactly when \( q > 0 \) and \( q^2 \ge 2 \); by @thm-no-rational-square-two, \( q^2 \ne 2 \), so \( q^2 > 2 \). Since \( (-q)^2 = q^2 \) (@prp-ring-algebra (c)), the set is
\[
\{ -q : q \in \nQ \setminus \sigma \} = \{ x \in \nQ : x < 0 \text{ and } x^2 > 2 \} .
\]
It is a cut. (C1): \( -2 \) is in it, \( 0 \) is not. (C2): if \( y < x \) with \( x < 0 \) and \( x^2 > 2 \), then \( 0 < -x < -y \), so \( x^2 = (-x)^2 < (-y)^2 = y^2 \) by @prp-ordered-ring-rules (g), and \( y < 0 \), \( y^2 > 2 \). (C3): let \( x < 0 \) with \( x^2 > 2 \), put \( q \coloneqq -x > 0 \) and
\[
q' \coloneqq \frac{q^2 + 2}{2q} ; \quad \text{then} \quad
\begin{aligned}
q - q' &= \frac{q^2 - 2}{2q} > 0 , \\
q'^2 - 2 &= \frac{(q^2 - 2)^2}{4q^2} > 0 .
\end{aligned}
\]
Then \( q' > 0 \), and \( x' \coloneqq -q' \) has \( x < x' < 0 \) and \( x'^2 > 2 \): an element of the set above \( x \).

*For \( D_1 \) it fails.* The outside of \( D_1 \) is \( \{ q : q \ge 1 \} \), so the set is \( \{ x \in \nQ : x \le -1 \} \). It has a largest element, \( -1 \), so (C3) fails.

*In general.* The set always satisfies (C1) and (C2). (C1): for \( b \notin \alpha \), \( -b \) is in it; for \( a \in \alpha \), \( -a \) is not, since \( -a = -q \) forces \( q = a \in \alpha \). (C2): if \( y < -q \) with \( q \notin \alpha \), then \( -y > q \), so \( -y \notin \alpha \) by @lem-cut-separation, and \( y = -(-y) \) is in the set. (C3) fails exactly when the set has a largest element \( -m \), that is, when \( \nQ \setminus \alpha \) has a least element \( m \). That happens exactly when \( \alpha \) is a rational cut. If \( \alpha = D_m \), the outside \( \{ q : q \ge m \} \) has least element \( m \). Conversely, if \( m \) is least in \( \nQ \setminus \alpha \), then every \( r < m \) is in \( \alpha \) (else it would be a smaller element of the outside), and every \( r \in \alpha \) has \( r < m \) (@lem-cut-separation), so \( \alpha = D_m \). So the recipe gives a cut **unless** \( \alpha \) is rational.

*The negatives of the inside.* For \( \alpha = D_1 \), \( \{ -p : p \in D_1 \} = \{ x : x > -1 \} \). It contains \( 0 \) but not \( -2 < 0 \), so (C2) fails. In general this set is closed **upward**, the mirror image of a cut: if \( p \in \alpha \) and \( y > -p \), then \( -y < p \), so \( -y \in \alpha \) by (C2), and \( y = -(-y) \) is in the set. And it is never a cut, because (C2) fails as it did for \( D_1 \). Take \( a \in \alpha \) and \( b \notin \alpha \) (C1). Then \( a < b \) by @lem-cut-separation, so \( -b < -a \). The set contains \( -a \) but not \( -b \), since \( -b = -p \) forces \( p = b \notin \alpha \).

The recipe passes the test on \( \sigma \), the first cut one tries, and fails on the rational cuts, the simplest cuts there are.
:::

The failure is a single point: for \( D_1 \) the recipe produces \( D_{-1} \) together with the one extra point \( -1 \). The repair is to stay a positive margin away from the outside.

*The negative of a cut is the set of negatives of the outside, pushed down by a positive margin.*

::: {#def-cut-negative}
[Negative of a Cut]

For a cut \( \alpha \), its **negative** is the set
\[
-\alpha \coloneqq \{ p \in \nQ : -p - r \notin \alpha \text{ for some rational } r > 0 \} .
\]
In symbols, \( p \in -\alpha \iff \exists r \in \nQ_{>0} \ \ {-p - r} \notin \alpha \). It is a cut (checked below). A rational \( r \) with this property is a **margin** for \( p \).
:::

In words: \( p \) belongs to \( -\alpha \) when \( -p \) is not merely outside \( \alpha \) but outside with room to spare, since even \( -p - r \), a positive distance below \( -p \), is still outside. The quantifier is "some": one margin suffices, and it may depend on \( p \). Equivalently, \( p \in -\alpha \) exactly when \( p < -q \) for some \( q \notin \alpha \) (take \( q \coloneqq -p - r \), and conversely \( r \coloneqq -q - p \)).

**\( -\alpha \) is a cut.** Let \( \alpha \) be a cut.

- (C1) By (C1) for \( \alpha \) there is \( b \notin \alpha \). For \( p \coloneqq -b - 1 \), the margin \( r \coloneqq 1 \) gives \( -p - 1 = b \notin \alpha \), so \( p \in -\alpha \). Also there is \( a \in \alpha \), and \( -a \notin -\alpha \): for every rational \( r > 0 \), \( -(-a) - r = a - r < a \), so \( a - r \in \alpha \) by (C2), and no margin exists.
- (C2) Let \( p \in -\alpha \) with margin \( r \), and \( p' < p \). Then \( -p' - r > -p - r \), and \( -p - r \notin \alpha \), so \( -p' - r \notin \alpha \), because the outside of a cut is closed upward (@lem-cut-separation). So \( p' \in -\alpha \), with the same margin.
- (C3) Let \( p \in -\alpha \) with margin \( r \). Then \( p + r/2 > p \), and \( -(p + r/2) - r/2 = -p - r \notin \alpha \), so \( p + r/2 \in -\alpha \) with margin \( r/2 \).

So \( -\alpha \in \nR_{\mathrm D} \), and \( \alpha \mapsto -\alpha \) is a function \( \nR_{\mathrm D} \to \nR_{\mathrm D} \).

**Examples.** The degenerate case is \( -D_0 = D_0 \). A rational \( p \) is in \( -D_0 \) when \( -p - r \ge 0 \) for some \( r > 0 \), that is, \( p \le -r < 0 \); and every \( p < 0 \) qualifies, with margin \( r \coloneqq -p \). The case that matters is \( -D_1 = D_{-1} \). Here \( p \in -D_1 \) when \( -p - r \ge 1 \) for some \( r > 0 \), that is, \( p \le -1 - r \) for some \( r > 0 \). That holds for every \( p < -1 \), with margin \( r \coloneqq -1 - p \), and for no \( p \ge -1 \). The point \( -1 \) that spoiled the recipe has no margin. The same computation gives \( -D_q = D_{-q} \) for every rational \( q \) (Exercise B1; the Quick check below does \( q = 3 \)).

**A non-example by minimal change.** Allow the margin \( r = 0 \). The condition becomes \( -p \notin \alpha \), and the set is the recipe of @exm-naive-negative: for \( D_1 \) it contains \( -1 \) and has a largest element. Exactly (C3) breaks, and the proof of (C3) above shows why: it moves up from \( p \) by half the margin, which needs \( r > 0 \).

**Why the margin.** The margin is what makes \( -\alpha \) satisfy (C3) when the outside of \( \alpha \) has a least element, and it changes nothing when the outside has none: then \( -\alpha \) is exactly the recipe \( \{ -q : q \in \nQ \setminus \alpha \} \) of @exm-naive-negative. For every cut, if \( p \in -\alpha \), then \( p < -q \) for some \( q \notin \alpha \) by the equivalence above, so \( -p > q \) is outside \( \alpha \) (@lem-cut-separation), and \( p = -(-p) \) is in the recipe. Conversely, if the outside has no least element and \( q \notin \alpha \), there is \( q' \notin \alpha \) with \( q' < q \); then \( -q < -q' \), so \( -q \in -\alpha \) by the equivalence above. The fold below works this out for \( \sigma \).

::: {.second-reading title="Edge case: for the cut of the square root of two, the margin changes nothing"}
For \( \sigma \), the definition gives \( -\sigma = \{ x \in \nQ : x < 0 \text{ and } x^2 > 2 \} \).

\( (\subseteq) \) Let \( p \in -\sigma \) with margin \( r \). Then \( -p - r \notin \sigma \), so \( -p - r > 0 \) and \( (-p - r)^2 \ge 2 \). Hence \( -p > -p - r > 0 \), so \( p < 0 \), and \( p^2 = (-p)^2 > (-p - r)^2 \ge 2 \) by @prp-ordered-ring-rules (g).

\( (\supseteq) \) Let \( p < 0 \) with \( p^2 > 2 \), and put \( q \coloneqq -p \). The rational \( q' \coloneqq (q^2 + 2)/(2q) \) satisfies \( 0 < q' < q \) and \( q'^2 > 2 \), by the identities \( q - q' = (q^2 - 2)/(2q) \) and \( q'^2 - 2 = (q^2 - 2)^2/(4q^2) \). With the margin \( r \coloneqq q - q' > 0 \), \( -p - r = q' \), which is positive with square at least \( 2 \), so \( q' \notin \sigma \), and \( p \in -\sigma \).

The outside of \( \sigma \) has no least element, and that is why no margin is needed.
:::

::: {.warning}
The negative of a cut is **not** the set \( \{ -p : p \in \alpha \} \). The book's notation \( -A \) for a set of numbers means that set, but for a cut \( -\alpha \) always means @def-cut-negative. The two differ even in shape: for \( \alpha = D_1 \), \( \{ -p : p \in D_1 \} = \{ x : x > -1 \} \) contains \( 0 \) but not \( -2 \), so it fails (C2), while \( -D_1 = D_{-1} \).
:::

::: {.check}
Compute \( -D_3 \) from @def-cut-negative, and \( D_{1/2} + D_{1/3} \) from @def-cut-sum.
:::

::: {.solution}
\( -D_3 = D_{-3} \). A rational \( p \) is in \( -D_3 \) when \( -p - r \ge 3 \) for some \( r > 0 \), that is, \( p \le -3 - r \). Every \( p < -3 \) qualifies, with margin \( r \coloneqq -3 - p > 0 \); no \( p \ge -3 \) does, since then \( -p - r \le 3 - r < 3 \).

\( D_{1/2} + D_{1/3} = D_{5/6} \). \( (\subseteq) \) \( p < 1/2 \) and \( q < 1/3 \) give \( p + q < 5/6 \). \( (\supseteq) \) For \( x < 5/6 \), put \( h \coloneqq (5/6 - x)/2 > 0 \). Then \( x = (1/2 - h) + (1/3 - h) \), with \( 1/2 - h < 1/2 \) and \( 1/3 - h < 1/3 \). Section 7.5 proves \( D_p + D_q = D_{p+q} \) for all rationals by the same split.
:::

## A cut plus its negative

Here is the theorem the margin was designed for. Its proof is a key proof of the chapter.

::: {#thm-cut-additive-inverse}
[Additive Inverses of Cuts]

For every cut \( \alpha \), \( \alpha + (-\alpha) = D_0 \).
:::

::: {.idea}
The inclusion \( \subseteq \) is separation: an element of \( \alpha \) is below every outside point, in particular below \( -t - r \) for \( t \in -\alpha \).

For \( \supseteq \), work backwards from the goal. Given \( s < 0 \), we want \( p \in \alpha \) and \( t \in -\alpha \) with \( p + t = s \). The second summand is forced, \( t = s - p \), and "\( t \in -\alpha \) with margin \( r \)" unwinds to \( -t - r = p + (-s - r) \notin \alpha \). So we need **a point inside \( \alpha \) and a point outside, at distance \( -s - r \)**, a little less than \( -s \). That is what the walk up by ε supplies (@lem-cut-step): start inside, add \( \varepsilon \) until you leave, and the last point inside and the first point outside are exactly \( \varepsilon \) apart. Take \( \varepsilon \) and the margin \( r \) both equal to \( -s/2 \); then \( -s - r = \varepsilon \).

*Before reading on: why is \( \varepsilon = -s/2 \) and not \( -s \)?*
:::

::: {.proof}
Let \( \alpha \) be a cut. By @def-cut-negative and @thm-cut-sum, \( -\alpha \) and \( \alpha + (-\alpha) \) are cuts.

\( (\subseteq) \) Let \( x \in \alpha + (-\alpha) \), say \( x = p + t \) with \( p \in \alpha \) and \( t \in -\alpha \), and let \( r > 0 \) be a margin for \( t \), so \( -t - r \notin \alpha \). By @lem-cut-separation, \( p < -t - r \). Adding \( t \) gives \( p + t < -r < 0 \). So \( x \in D_0 \).

\( (\supseteq) \) Let \( s \in D_0 \), so \( s < 0 \), and let
\[
\varepsilon \coloneqq -s/2 ;
\]
it depends only on \( s \), and \( \varepsilon > 0 \) by @prp-ordered-field-halves (b), since \( -s > 0 \). By (C1) there is \( a \in \alpha \); fix one \( \bigl[ \rulename{\exists E} \bigr] \). By @lem-cut-step, applied to \( \alpha \), \( a \) and \( \varepsilon \), there is \( n \in \nN \) with
\[
a + n\varepsilon \in \alpha \qquad \text{and} \qquad a + (n + 1)\varepsilon \notin \alpha ;
\]
fix one such \( n \) \( \bigl[ \rulename{\exists E} \bigr] \) and put \( p \coloneqq a + n\varepsilon \), so that \( p \in \alpha \) and \( p + \varepsilon \notin \alpha \). Now let
\[
t \coloneqq s - p .
\]
Since \( s = -2\varepsilon \),
\[
-t - \varepsilon = p - s - \varepsilon = p + 2\varepsilon - \varepsilon = p + \varepsilon \notin \alpha ,
\]
so \( \varepsilon \) is a margin for \( t \), and \( t \in -\alpha \) \( \bigl[ \rulename{\exists I} \bigr] \) (@fd1:def-rule-existential-introduction), with witness \( r \coloneqq \varepsilon \). Finally \( p + t = s \), so \( s \in \alpha + (-\alpha) \) \( \bigl[ \rulename{\exists I} \bigr] \), with witnesses \( p \) and \( t \). As \( s \in D_0 \) was arbitrary, \( D_0 \subseteq \alpha + (-\alpha) \) \( \bigl[ \rulename{\forall I} \bigr] \).

The two inclusions give \( \alpha + (-\alpha) = D_0 \) (@fd2:prp-subset-antisymmetric).
:::

The answer to the prompt. With \( \varepsilon = -s \), the walk gives \( p \in \alpha \) with \( p - s \notin \alpha \), and \( t = s - p \) would need a margin \( r > 0 \) with \( p - s - r \notin \alpha \). Nothing guarantees one: \( p - s - r \) lies below the first outside point of the walk, and may be inside. For \( \alpha = D_1 \), \( s = -1 \) and \( a = 0 \), the walk stops at \( p = 0 \), and \( p - s - r = 1 - r \in D_1 \) for every \( r > 0 \). The margin must be strictly smaller than the gap, and halving \( -s \) leaves room for both.

The proof treats rational and irrational cuts alike: it never asks whether the outside of \( \alpha \) has a least element. The margin in @def-cut-negative is exactly what absorbs the rational case; without it the \( \supseteq \) half would still go through, but for a rational cut \( \alpha \) the set it lands in would not be a cut (@exm-naive-negative).

## An ordered group

The results so far say that cuts under \( + \) behave like the rationals under \( + \), with the order of Section 7.2 respected. We collect them, together with the consequences that Section 7.4 uses.

::: {#thm-cut-ordered-group}
[Cuts Form an Ordered Group under Addition]

For all cuts \( \alpha \), \( \beta \), \( \gamma \):

::: {.enumerate options="label=(\alph*)"}
1. \( \alpha + \beta = \beta + \alpha \) and \( (\alpha + \beta) + \gamma = \alpha + (\beta + \gamma) \);
2. \( \alpha + D_0 = \alpha \);
3. \( \alpha + (-\alpha) = D_0 \);
4. \( \le \) is a total order on \( \nR_{\mathrm D} \); if \( \alpha \le \beta \), then \( \alpha + \gamma \le \beta + \gamma \); and if \( \alpha < \beta \), then \( \alpha + \gamma < \beta + \gamma \);
5. (cancellation and unique inverses) if \( \alpha + \gamma = \beta + \gamma \), then \( \alpha = \beta \); if \( \alpha + \beta = D_0 \), then \( \beta = -\alpha \); and \( -(-\alpha) = \alpha \), \( -D_0 = D_0 \), \( -(\alpha + \beta) = (-\alpha) + (-\beta) \);
6. \( \alpha < \beta \) if and only if \( -\beta < -\alpha \), and \( \alpha \le \beta \) if and only if \( -\beta \le -\alpha \). In particular \( \alpha > D_0 \iff -\alpha < D_0 \), and \( \alpha < D_0 \iff -\alpha > D_0 \).
:::

So \( (\nR_{\mathrm D}, +, \le) \) is an **ordered abelian group**: (a)–(c) are (F1)–(F4) for \( + \), with zero \( D_0 \), and (d) is a total order with (O3). Clauses (e) and (f) are consequences.
:::

::: {.proof}
(a) is @thm-cut-sum, (b) is @prp-cut-sum-zero and (c) is @thm-cut-additive-inverse.

(d) By the paragraph after @def-cut-order, \( \le \) is a partial order, and by @thm-cut-order-total any two cuts are comparable, so \( \le \) is a total order. If \( \alpha \subseteq \beta \) and \( x = p + q \in \alpha + \gamma \) with \( p \in \alpha \), \( q \in \gamma \), then \( p \in \beta \) and \( x \in \beta + \gamma \); so \( \alpha + \gamma \le \beta + \gamma \). The strict form follows from the cancellation law in (e): if \( \alpha < \beta \), then \( \alpha + \gamma \le \beta + \gamma \), and equality would give \( \alpha = \beta \).

(e) If \( \alpha + \gamma = \beta + \gamma \), then by (b), (c) and (a),
\[
\begin{aligned}
\alpha &= \alpha + \bigl( \gamma + (-\gamma) \bigr) = (\alpha + \gamma) + (-\gamma) \\
&= (\beta + \gamma) + (-\gamma) = \beta + \bigl( \gamma + (-\gamma) \bigr) = \beta .
\end{aligned}
\]
If \( \alpha + \beta = D_0 \), then \( \beta + \alpha = D_0 = (-\alpha) + \alpha \) by (a) and (c), and cancellation gives \( \beta = -\alpha \). Since \( (-\alpha) + \alpha = D_0 \), the same applied to the cut \( -\alpha \) gives \( \alpha = -(-\alpha) \). Since \( D_0 + D_0 = D_0 \) by (b), it gives \( D_0 = -D_0 \). Finally, by (a), (c) and (b),
\[
(\alpha + \beta) + \bigl( (-\alpha) + (-\beta) \bigr) = \bigl( \alpha + (-\alpha) \bigr) + \bigl( \beta + (-\beta) \bigr) = D_0 + D_0 = D_0 ,
\]
so \( (-\alpha) + (-\beta) = -(\alpha + \beta) \).

(f) Let \( \alpha < \beta \) and \( \delta \coloneqq (-\alpha) + (-\beta) \). By (d), \( \alpha + \delta < \beta + \delta \). By (a), (c) and (b), \( \alpha + \delta = -\beta \) and \( \beta + \delta = -\alpha \). So \( -\beta < -\alpha \). Conversely, if \( -\beta < -\alpha \), the same argument applied to the cuts \( -\beta \) and \( -\alpha \) gives \( -(-\alpha) < -(-\beta) \), which is \( \alpha < \beta \) by (e). The non-strict form adds the case of equality: \( \alpha = \beta \) if and only if \( -\alpha = -\beta \), by (e). For the last sentence, take \( \alpha \) or \( \beta \) to be \( D_0 \) and use \( -D_0 = D_0 \).
:::

Half of the field axioms now hold for cuts. The other half needs a product, and Section 7.4 builds it by reducing to positive cuts. There (f) is what turns a negative cut into a positive one, and (e) is what lets the signs be put back.

## Exercises

### A. Check your understanding

::: {#exr-addition-a1}
[A1]

These questions are about the proof of @thm-cut-additive-inverse and the definition of \( -\alpha \).

::: {.enumerate options="label=(\alph*)"}
1. Run the \( \supseteq \) half of the proof for \( \alpha = D_1 \), \( s = -1/2 \) and the starting point \( a = 0 \). What are \( \varepsilon \), \( n \), \( p \), \( t \) and the margin? Check that \( t \in -D_1 \) and \( p + t = s \).
2. Where in the proof is @lem-cut-step used, and what does that lemma need from \( \nQ \)?
3. In the check that \( -\alpha \) is a cut, which condition uses \( r > 0 \)? What goes wrong for \( \alpha = D_1 \) if the margin \( r = 0 \) is allowed?
4. State the idea of the proof in two sentences.
:::
:::

::: {.solution}
(a) \( \varepsilon = -s/2 = 1/4 \). The points \( a + k\varepsilon = k/4 \) are in \( D_1 \) exactly for \( k < 4 \), so \( n = 3 \), \( p = 3/4 \in D_1 \) and \( p + \varepsilon = 1 \notin D_1 \). Then \( t = s - p = -1/2 - 3/4 = -5/4 \), with margin \( \varepsilon = 1/4 \): \( -t - 1/4 = 5/4 - 1/4 = 1 \notin D_1 \), so \( t \in -D_1 \). And \( p + t = 3/4 - 5/4 = -1/2 = s \). (Another starting point \( a \) may give another pair, for example \( a = 1/8 \) gives \( p = 7/8 \); any \( p \in D_1 \) with \( p + 1/4 \ge 1 \), that is \( 3/4 \le p < 1 \), works with \( t = -1/2 - p \).)

(b) Once, in the \( \supseteq \) half, to produce \( p \in \alpha \) with \( p + \varepsilon \notin \alpha \). Its proof in Section 7.1 needs the Archimedean property of \( \nQ \) (@thm-rationals-archimedean), to get some multiple of \( \varepsilon \) that leaves \( \alpha \), and the least element of a non-empty set of natural numbers (@prp-integer-least-element), to get the first one, and discreteness of the integers (@thm-integers-ordered-ring (c)), to step back from the first one to the one before it.

(c) (C3): from \( p \in -\alpha \) with margin \( r \) we moved up to \( p + r/2 \), which is larger than \( p \) only when \( r > 0 \). With \( r = 0 \) allowed, the set for \( D_1 \) is \( \{ x : -x \notin D_1 \} = \{ x : x \le -1 \} \), which has the largest element \( -1 \), so it is not a cut.

(d) Inside \( \alpha \) and outside it, there are points exactly \( \varepsilon \) apart, found by walking up from a point of \( \alpha \) in steps of \( \varepsilon \). With \( \varepsilon = -s/2 \), the last point \( p \) inside and \( t = s - p \) split \( s \), and the first point outside certifies \( t \in -\alpha \) with margin \( \varepsilon \).
:::

### B. Practice

::: {#exr-addition-b1}
[B1]

Prove that \( -D_q = D_{-q} \) for every \( q \in \nQ \).
:::

::: {.solution}
Let \( q, p \in \nQ \). By @def-cut-negative and @def-rational-cut, \( p \in -D_q \) if and only if \( -p - r \ge q \) for some rational \( r > 0 \).

\( (\subseteq) \) Let \( p \in -D_q \) with margin \( r \). Then \( -p \ge q + r > q \), so \( p < -q \) (@prp-ordered-ring-rules (a)), and \( p \in D_{-q} \).

\( (\supseteq) \) Let \( p < -q \). Then \( r \coloneqq -q - p > 0 \), and \( -p - r = q \ge q \), so \( q \notin D_q \) shows that \( r \) is a margin for \( p \). Hence \( p \in -D_q \).

So \( -D_q = D_{-q} \).
:::

::: {#exr-addition-b2}
[B2: Associativity, element by element]

Let \( A \), \( B \), \( C \) be any subsets of \( \nQ \), and let \( A + B \coloneqq \{ a + b : a \in A, \ b \in B \} \). Prove that \( (A + B) + C = A + (B + C) \), writing out both inclusions element by element and naming the rule of \( \nQ \) used in each. Which of the cut conditions (C1)–(C3) did you use?
:::

::: {.solution}
\( (\subseteq) \) Let \( x \in (A + B) + C \). By the definition, \( x = y + c \) for some \( y \in A + B \) and \( c \in C \), and \( y = a + b \) for some \( a \in A \), \( b \in B \). So \( x = (a + b) + c = a + (b + c) \) by (F2) in \( \nQ \). Since \( b + c \in B + C \), \( x \in A + (B + C) \).

\( (\supseteq) \) Let \( x \in A + (B + C) \). Then \( x = a + z \) with \( a \in A \) and \( z \in B + C \), and \( z = b + c \) with \( b \in B \), \( c \in C \). So \( x = a + (b + c) = (a + b) + c \) by (F2), and \( a + b \in A + B \), so \( x \in (A + B) + C \).

The two inclusions give the equality (@fd2:prp-subset-antisymmetric). None of (C1)–(C3) was used: associativity of the set sum holds for all sets of rationals, and the only fact used was (F2). For cuts, @thm-cut-sum adds that the sum is again a cut.
:::

### C. Going deeper

::: {#exr-addition-c1}
[C1: Exit check: a cut plus its negative]

Prove that \( \alpha + (-\alpha) = D_0 \) for every cut \( \alpha \). Then explain, on the cut \( \alpha = D_1 \), why the recipe \( \{ -q : q \in \nQ \setminus \alpha \} \) does not give an additive inverse in \( \nR_{\mathrm D} \), while @def-cut-negative does.
:::

::: {.solution}
[Hint 1]

For \( \supseteq \), given \( s < 0 \), you need a point of \( \alpha \) and a point outside \( \alpha \) that are a fixed positive distance apart. Which lemma of Section 7.1 produces such a pair?
:::

::: {.solution}
[Hint 2]

Let \( \varepsilon \coloneqq -s/2 \), and apply @lem-cut-step to a point of \( \alpha \) and this \( \varepsilon \).
:::

::: {.solution}
Let \( \alpha \) be a cut; \( -\alpha \) is a cut by @def-cut-negative.

\( (\subseteq) \) Let \( p \in \alpha \) and \( t \in -\alpha \), with a margin \( r > 0 \), so \( -t - r \notin \alpha \). By @lem-cut-separation, \( p < -t - r \), so \( p + t < -r < 0 \), and \( p + t \in D_0 \).

\( (\supseteq) \) Let \( s < 0 \) be arbitrary, and \( \varepsilon \coloneqq -s/2 > 0 \). Fix \( a \in \alpha \) (C1). By @lem-cut-step there is \( n \in \nN \) with \( p \coloneqq a + n\varepsilon \in \alpha \) and \( p + \varepsilon \notin \alpha \). Let \( t \coloneqq s - p \). Then \( -t - \varepsilon = p - s - \varepsilon = p + \varepsilon \notin \alpha \), so \( t \in -\alpha \) with margin \( \varepsilon \), and \( p + t = s \). So \( s \in \alpha + (-\alpha) \).

*The comparison on \( D_1 \).* The recipe gives \( \{ -q : q \ge 1 \} = \{ x : x \le -1 \} \). This set has the largest element \( -1 \), so it fails (C3) and is not a cut; it is not an element of \( \nR_{\mathrm D} \) at all, whatever its sum with \( D_1 \) may be. In @def-cut-negative, \( -1 \) would need a margin \( r > 0 \) with \( 1 - r \notin D_1 \), and there is none, since \( 1 - r < 1 \). So the margin removes exactly the point \( -1 \), and \( -D_1 = \{ x : x < -1 \} = D_{-1} \), a cut, with \( D_1 + D_{-1} = D_0 \) by the first part.

**Marking scheme.** (10 points)
- 2: \( \subseteq \), using separation against the outside point \( -t - r \) to get \( p + t < 0 \).
- 1: fixes \( s < 0 \) arbitrary.
- 3: produces \( p \in \alpha \) with \( p + \varepsilon \notin \alpha \) for an \( \varepsilon \) chosen from \( s \) alone, citing the step lemma (or proving it from the Archimedean property and least elements).
- 2: exhibits \( t \in -\alpha \) with its margin, and checks \( p + t = s \).
- 2: the \( D_1 \) comparison: the recipe's set has the largest element \( -1 \), and the margin removes it.
Fatal errors (0 for the step): a margin equal to the whole gap (\( \varepsilon = -s \) with margin \( -s \)); \( \varepsilon \) chosen depending on \( p \) after \( p \) was found from \( \varepsilon \).
:::

::: {#exr-addition-c2}
[C2: Find the error]

Here is a proof that \( \alpha + D_0 = \alpha \) for every cut \( \alpha \).

> *Proof.* (1) Let \( \alpha \) be a cut. (2) \( (\subseteq) \) Let \( x \in \alpha + D_0 \), so \( x = p + q \) with \( p \in \alpha \) and \( q \in D_0 \). (3) Then \( q < 0 \), so \( x = p + q < p \), and \( x \in \alpha \) by (C2). (4) \( (\supseteq) \) Let \( p \in \alpha \). (5) Then \( p = p + 0 \) with \( p \in \alpha \) and \( 0 \in D_0 \), so \( p \in \alpha + D_0 \). (6) Hence \( \alpha + D_0 = \alpha \).

::: {.enumerate options="label=(\alph*)"}
1. Is the conclusion true?
2. Which line fails, and why?
3. Give a counterexample to the step itself.
4. Repair the proof.
5. The flawed proof never uses (C3). Show that without it the conclusion can fail: compute \( A + D_0 \) for \( A \coloneqq \{ r \in \nQ : r \le 1 \} \).
:::
:::

::: {.solution}
(a) Yes: it is @prp-cut-sum-zero.

(b) Line (5). It asserts \( 0 \in D_0 \), which is false: \( D_0 = \{ r : r < 0 \} \), and \( 0 < 0 \) fails by (O1). The line cites a "fact" that is neither proved nor true, error (N9) of @fd1:exm-not-allowed-catalogue. Lines (1)–(4) and (6) are correct.

(c) Take \( \alpha = D_1 \) and \( p = 1/2 \). The decomposition \( 1/2 = 1/2 + 0 \) of line (5) is not a decomposition into an element of \( D_1 \) and an element of \( D_0 \), because \( 0 \notin D_0 \). (The conclusion \( 1/2 \in D_1 + D_0 \) is still true, by \( 1/2 = 3/4 + (-1/4) \); the step does not show it.)

(d) Replace line (5) by: "By (C3) there is \( p' \in \alpha \) with \( p' > p \). Then \( p - p' < 0 \), so \( p - p' \in D_0 \), and \( p = p' + (p - p') \in \alpha + D_0 \)." This is the proof of @prp-cut-sum-zero.

(e) Without (C3) the conclusion fails. The set \( A = \{ r : r \le 1 \} \) satisfies (C1) and (C2) but not (C3), and \( A + D_0 = D_1 \ne A \). Indeed, if \( a \le 1 \) and \( q < 0 \), then \( a + q < 1 \); and every \( x < 1 \) is \( 1 + (x - 1) \) with \( 1 \in A \) and \( x - 1 < 0 \). So \( A + D_0 = D_1 \), which does not contain \( 1 \in A \). An argument that never uses (C3) would prove the same equation for \( A \), where it is false; that is the tell that some line is wrong.
:::

<!-- dependency ledger
thm-cut-sum (proof): rational arithmetic and order, (F1)-(F9), (O1)-(O4), and the rules of prp-ordered-ring-rules for rationals | Q ordered field, F3.2 (thm-rationals-ordered-field, recalled in the opening frame)
thm-cut-sum (proof): a + b notin alpha + beta because every element is < a + b; (O1) | inline, from lem-cut-separation and prp-ordered-ring-rules (b)
prp-cut-sum-zero (proof): D_0 is a cut | def-rational-cut (Section 7.1)
def-cut-negative (claim): before-reading-on answer, D_1 + D_{-1} = D_0, by s = (1 - h) + (-1 - h) | inline, with prp-ordered-field-halves (b); verify/ch07/def-cut-negative.py
exm-naive-negative (example): q' = (q^2 + 2)/(2q) has 0 < q' < q and q'^2 > 2 when q > 0, q^2 > 2 | inline (two displayed identities); verify/ch07/exm-naive-negative.py
exm-naive-negative (example): (-q)^2 = q^2 | prp-ring-algebra (c), cited
exm-naive-negative (example): alpha = D_m when m is least outside alpha | inline, from lem-cut-separation
exm-naive-negative (example): {-p : p in alpha} is closed upward and fails (C2) (-a in it, -b not, -b < -a) | inline, from (C1), (C2) and lem-cut-separation
def-cut-negative (claim): -alpha is a cut; -D_0 = D_0; -D_1 = D_{-1} | inline (the paragraph and examples after def-cut-negative); r/2 > 0, r/2 + r/2 = r by prp-ordered-field-halves (b)
def-cut-negative (claim): -alpha equals {-q : q notin alpha} when the outside of alpha has no least element | inline, from the equivalence after def-cut-negative and lem-cut-separation
def-cut-negative (claim): fold, -sigma = {x < 0 : x^2 > 2} | inline, same identities as exm-naive-negative, re-proved in the fold; verify/ch07/exm-naive-negative.py
def-cut-negative (solution): quick check, -D_3 = D_{-3}, D_{1/2} + D_{1/3} = D_{5/6} with h = (5/6 - x)/2 | inline, with prp-ordered-field-halves (b); verify/ch07/def-cut-negative.py
thm-cut-additive-inverse (proof): s = -2 epsilon, -t - epsilon = p + epsilon | inline; verify/ch07/thm-cut-additive-inverse.py
thm-cut-additive-inverse (claim): with epsilon = -s the margin can fail (D_1, s = -1, a = 0, p = 0) | inline; verify/ch07/thm-cut-additive-inverse.py
thm-cut-ordered-group (proof): rearranging (a + b) + ((-a) + (-b)) | (a) of the same theorem, applied repeatedly; inline
exr-addition-a1 (solution): epsilon = 1/4, n = 3, p = 3/4, t = -5/4; a = 1/8 gives p = 7/8 | verify/ch07/exr-addition-a1.py
exr-addition-a1 (solution): lem-cut-step's proof uses thm-rationals-archimedean, prp-integer-least-element and thm-integers-ordered-ring (c) | Section 7.1's proof of lem-cut-step (blueprint ch07)
exr-addition-c2 (solution): {r <= 1} + D_0 = D_1; 1/2 = 3/4 + (-1/4) | inline; verify/ch07/exr-addition-c2.py
-->
