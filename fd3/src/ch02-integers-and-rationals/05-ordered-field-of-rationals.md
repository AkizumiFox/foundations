# The Rationals as an Ordered Field; the Archimedean Property

Section 10.4 built \( \nQ \) as a set of classes of fractions and proved that it is a field (@thm-rationals-field): we can add, subtract, multiply, and divide by anything non-zero. What it did not give us is an order. In school one "sees" that \( -3/5 < -7/12 \) by placing both on a line, but the line is the school picture this volume has set aside, so the order must be defined on the classes and its rules proved. This section does that, by the method of Section 10.3: name the positive rationals, check two closure properties, and let @prp-order-from-positives produce the rest. Then we prove the first fact about \( \nQ \) that later chapters of this volume lean on at every turn: every rational is exceeded by a natural number, and so \( 1/n \) eventually drops below any positive rational. Finally every rational gets an integer part.

## Which fractions are positive

Throughout, a rational is written as in Section 10.4. By @prp-integers-embed-rationals (b), every \( x \in \nQ \) is \( p/q \) for some \( p \in \nZ \) and \( q \in \nZ_{>0} \), where \( p/q \) is the class \( [(p, q)] \), and \( p/q = r/s \) if and only if \( ps = rq \). The integers sit inside \( \nQ \) as \( m = m/1 \), and the natural numbers inside the integers.

The order of \( \nZ \) came from its positive set \( P_{\nZ} \) (@def-integer-order), and @prp-order-from-positives turned closure under \( + \) and \( \cdot \), together with a trichotomy, into all of (O1)–(O4). We do the same for \( \nQ \), so the whole question is: which fractions should count as positive? A first guess from school is "numerator and denominator have the same sign". But in \( \nQ \) the denominator is always positive. That was the decision recorded with @def-rationals-as-classes, and here it pays: the sign of a fraction is the sign of its numerator.

*A fraction with a positive denominator is positive exactly when its numerator is.*

::: {#def-rational-order}
[The Order on \( \nQ \)]

Let
\[
P_{\nQ} \coloneqq \bigl\{ [(p, q)] : (p, q) \in \nZ \times \nZ_{>0} \text{ and } p > 0 \bigr\} .
\]
For \( x, y \in \nQ \), we write \( x < y \) if \( y - x \in P_{\nQ} \). As in @def-ordered-ring-and-field, \( x > y \) means \( y < x \), and \( x \le y \) means \( x < y \) or \( x = y \).
:::

In words: a rational is in \( P_{\nQ} \) if it **has a** representative \( (p, q) \) with \( p > 0 \), the inequality being the order of \( \nZ \); and \( x < y \) means that the difference \( y - x \), computed in the field \( \nQ \), lies in \( P_{\nQ} \).

**Well-definedness.** The definition says "has a representative with \( p > 0 \)". To use it we want more: that **every** representative of a class in \( P_{\nQ} \) has a positive numerator, so that the test can be run on whichever representative is at hand. This is the situation of @thm-well-defined-on-classes (c), with \( X = \nZ \times \nZ_{>0} \) and \( S = \{ (p, q) \in X : p > 0 \} \). Its hypothesis asks: if \( (p, q) \sim (p', q') \) and \( p > 0 \), is \( p' > 0 \)? It is, and the reason is the sign of the denominators.

Suppose \( pq' = p'q \) with \( q, q' \in \nZ_{>0} \) and \( p > 0 \). Since \( q, q' > 0 \) (@thm-integers-ordered-ring (b)), (O4) gives \( pq' > 0 \), so \( p'q > 0 \). If \( p' = 0 \), then \( p'q = 0 \) (@prp-ring-algebra (b)); if \( p' < 0 \), then \( p'q < 0 \cdot q = 0 \) by @prp-ordered-ring-rules (c), since \( q > 0 \). Both contradict \( p'q > 0 \) by trichotomy, so \( p' > 0 \). Now @thm-well-defined-on-classes (c) gives, for every \( (p, q) \in \nZ \times \nZ_{>0} \),
\[
[(p, q)] \in P_{\nQ} \iff p > 0 .
\]{#eq-positive-test}

**Examples.** The class \( 3/4 \) lies in \( P_{\nQ} \), and so does \( 6/8 \), the same class: both numerators are positive, as @eq-positive-test says they must be. The class \( -6/8 \) does not, since \( -6 > 0 \) fails. The degenerate case is zero: \( 0 = 0/1 = 0/7 \), and \( 0 > 0 \) fails, so \( 0 \notin P_{\nQ} \). That matters, because (P2) of @prp-order-from-positives will ask for exactly one of \( x \in P_{\nQ} \), \( x = 0 \), \( -x \in P_{\nQ} \).

**Non-example by minimal change.** Allow negative denominators, as in @exm-fractions-nonzero-denominators, and keep the test "the numerator is positive". The relation is the same and still an equivalence relation, but now \( (1, 1) \sim (-1, -1) \): the class of \( (1, 1) \) passes the test with one representative and fails it with another. The clause that fails is the hypothesis of @thm-well-defined-on-classes (c), and the step of the check above that breaks is "\( q > 0 \)".

**Why this definition.** With non-zero denominators of either sign one could test "\( pq > 0 \)" instead, which is well defined; the price is a product in every sign test and two sign cases in every proof. Positive denominators put all the sign information in one integer. The order is defined through the positive set rather than through a formula for \( x < y \), so that @prp-order-from-positives does the work of (O1)–(O4) once and for all.

::: {.warning}
Comparing numerators alone is not comparing fractions. The rationals \( 1/2 \) and \( 2/5 \) have \( 1 < 2 \), yet \( 1/2 > 2/5 \), since \( 1/2 - 2/5 = 1/10 \in P_{\nQ} \). Only after bringing both to the same positive denominator do the numerators decide: that is the comparison formula below.
:::

::: {.check}
Which of \( [(-2, 3)] \), \( [(0, 5)] \), \( [(4, 6)] \) lie in \( P_{\nQ} \)? Why can one not ask whether \( [(2, -3)] \) lies in \( P_{\nQ} \)?
:::

::: {.solution}
By @eq-positive-test, only \( [(4, 6)] \) does: its numerator \( 4 \) is positive, while \( -2 > 0 \) and \( 0 > 0 \) both fail. The symbol \( [(2, -3)] \) names no element of \( \nQ \): the denominator \( -3 \) is not in \( \nZ_{>0} \), so \( (2, -3) \) is not in \( \nZ \times \nZ_{>0} \) and has no class. (The rational one might mean is \( -2/3 = [(-2, 3)] \), which is not in \( P_{\nQ} \).)
:::

## The rationals form an ordered field

The payoff is that the order of \( \nQ \) has every property of the order of \( \nZ \), together with a formula that compares two fractions with one integer inequality.

::: {#thm-rationals-ordered-field}
[The Rationals Form an Ordered Field]

With the order of @def-rational-order, \( \nQ \) is an ordered field (@def-ordered-ring-and-field), and \( P_{\nQ} = \{ x \in \nQ : x > 0 \} \). Moreover:

::: {.enumerate options="label=(\alph*)"}
1. *(The comparison formula.)* For \( p, r \in \nZ \) and \( q, s \in \nZ_{>0} \),
\[
\frac{p}{q} < \frac{r}{s} \iff ps < rq ;
\]
in particular \( p/q > 0 \) if and only if \( p > 0 \).
2. For \( m, n \in \nZ \), \( j(m) < j(n) \) if and only if \( m < n \).
:::
:::

::: {.idea}
By @prp-order-from-positives, a commutative ring with a positive set satisfying (P1) and (P2) is an ordered commutative ring, and \( \nQ \) is already a field. So everything reduces to the two properties of \( P_{\nQ} \), and @eq-positive-test turns each into a statement about numerators in \( \nZ \): reduce to the level below. A sum \( p/q + r/s \) has numerator \( ps + rq \), and with \( p, r > 0 \) this is positive **because \( s \) and \( q \) are**. The comparison formula is (P1)'s computation run on a difference. *Before reading on: where is \( q > 0 \) used?*
:::

::: {.proof}
By @thm-rationals-field, \( \nQ \) is a field, in particular a commutative ring. We check (P1) and (P2) of @prp-order-from-positives for \( P = P_{\nQ} \).

(P1) Let \( x, y \in P_{\nQ} \), say \( x = [(p, q)] \) and \( y = [(r, s)] \) with \( q, s \in \nZ_{>0} \). By @eq-positive-test, \( p > 0 \) and \( r > 0 \); and \( q, s > 0 \) by @thm-integers-ordered-ring (b). By @def-rational-operations,
\[
x + y = [(ps + rq, \, qs)] , \qquad xy = [(pr, \, qs)] ,
\]
with \( qs \in \nZ_{>0} \). By (O4) in \( \nZ \), \( ps > 0 \) and \( rq > 0 \), so \( ps + rq > 0 + 0 = 0 \) by @prp-ordered-ring-rules (b); and \( pr > 0 \) by (O4). By @eq-positive-test, \( x + y \in P_{\nQ} \) and \( xy \in P_{\nQ} \).

(P2) Let \( x = [(p, q)] \in \nQ \). Then \( -x = [(-p, q)] \) (@def-rational-operations). By @thm-rationals-field, the zero of \( \nQ \) is \( [(0, 1)] \), and \( x = 0 \) if and only if \( p = 0 \). By @eq-positive-test, \( x \in P_{\nQ} \) if and only if \( p > 0 \), and \( -x \in P_{\nQ} \) if and only if \( -p > 0 \), which by @prp-ordered-ring-rules (a) means \( p < 0 \). By (O1) in \( \nZ \), exactly one of \( p > 0 \), \( p = 0 \), \( p < 0 \) holds, so exactly one of \( x \in P_{\nQ} \), \( x = 0 \), \( -x \in P_{\nQ} \) holds.

By @prp-order-from-positives, the relation \( x < y \iff y - x \in P_{\nQ} \), which is the relation of @def-rational-order, satisfies (O1)–(O4), and \( P_{\nQ} = \{ x : x > 0 \} \). A field that is an ordered commutative ring is an ordered field (@def-ordered-ring-and-field).

(a) Let \( p, r \in \nZ \) and \( q, s \in \nZ_{>0} \). By @def-rational-operations and @prp-ring-algebra (c),
\[
\frac{r}{s} - \frac{p}{q} = [(r, s)] + [(-p, q)] = [(rq + (-p)s, \, sq)] = [(rq - ps, \, qs)] .
\]
So \( p/q < r/s \) holds if and only if this class lies in \( P_{\nQ} \), that is (by @eq-positive-test, since \( qs \in \nZ_{>0} \)), if and only if \( rq - ps > 0 \), which by @prp-ordered-ring-rules (a) means \( ps < rq \). For the special case, compare \( 0 = 0/1 \) with \( p/q \): the formula gives \( 0/1 < p/q \) if and only if \( 0 \cdot q < p \cdot 1 \), that is, \( p > 0 \).

(b) \( j(m) = m/1 \) and \( j(n) = n/1 \) (@prp-integers-embed-rationals), so by (a), \( j(m) < j(n) \) if and only if \( m \cdot 1 < n \cdot 1 \), that is, \( m < n \).

This proves the theorem.
:::

The answer to the prompt: \( q > 0 \) is used three times. In the well-definedness check before @eq-positive-test, the positive \( q \) and \( q' \) carry the sign from \( p \) to \( p' \). In (P1), \( ps \) and \( rq \) are positive because \( s \) and \( q \) are. In (a), the difference has denominator \( qs \), a positive integer, so that @eq-positive-test can read its sign off the numerator. Without positive denominators the first of these fails outright (the non-example above), and so does the comparison formula: see @exm-fractions-nonzero-denominators.

Since \( p/q = r/s \) exactly when \( ps = rq \) (@prp-integers-embed-rationals (b)), the comparison formula has a version with \( \le \): for \( q, s \in \nZ_{>0} \),
\[
\frac{p}{q} \le \frac{r}{s} \iff ps \le rq .
\]{#eq-comparison-le}
By (b), the order of \( \nQ \) restricted to \( \nZ \) is the order of \( \nZ \), which in turn restricts to the order of \( \nN \) (@thm-integers-ordered-ring (a)). So after the identifications \( \nN \subseteq \nZ \subseteq \nQ \), a comparison of two integers means the same thing in all three sets, and we never need to say where it is made. Every rule of @prp-ordered-ring-rules now holds in \( \nQ \), and we write
\[
\nQ_{>0} \coloneqq \{ x \in \nQ : x > 0 \}
\]
for the set of positive rationals, which is \( P_{\nQ} \).

One rule is new with fields, because rings have no inverses: taking reciprocals reverses the order of positive elements.

::: {#prp-reciprocal-order}
[Reciprocals Reverse Order]

Let \( F \) be an ordered field and \( a, b \in F \).

::: {.enumerate options="label=(\alph*)"}
1. If \( a > 0 \), then \( a^{-1} > 0 \).
2. If \( 0 < a < b \), then \( 0 < b^{-1} < a^{-1} \), that is, \( 0 < 1/b < 1/a \).
:::
:::

::: {.idea}
For (a), turn \( a^{-1} \) into a product we can sign: \( a^{-1} = a \cdot (a^{-1})^2 \), a positive element times a non-zero square. For (b), multiply \( a < b \) by the positive element \( a^{-1} b^{-1} \): it cancels \( a \) on the left and \( b \) on the right, and swaps which reciprocal stands on which side.
:::

::: {.proof}
(a) Let \( a > 0 \). Then \( a \ne 0 \), so \( a^{-1} \) exists, and \( a^{-1} \ne 0 \): otherwise \( 1 = a a^{-1} = a \cdot 0 = 0 \) (@prp-ring-algebra (b)), against \( 1 \ne 0 \) in a field. By @prp-ordered-ring-rules (e), \( (a^{-1})^2 > 0 \). Now
\[
a \cdot (a^{-1})^2 = (a a^{-1}) a^{-1} = 1 \cdot a^{-1} = a^{-1} ,
\]
and the left side is a product of two positive elements, so \( a^{-1} > 0 \) by (O4).

(b) Let \( 0 < a < b \). Then \( b > 0 \) by (O2), so \( a^{-1} > 0 \) and \( b^{-1} > 0 \) by (a), and \( c \coloneqq a^{-1} b^{-1} > 0 \) by (O4). Multiplying \( a < b \) by \( c > 0 \) (@prp-ordered-ring-rules (c)) gives
\[
b^{-1} = (a a^{-1}) b^{-1} = ac < bc = (b b^{-1}) a^{-1} = a^{-1} .
\]
Since \( 1/b = 1 \cdot b^{-1} = b^{-1} \) (@def-commutative-ring-and-field), this is \( 0 < 1/b < 1/a \).
:::

## Between two rationals

In \( \nZ \) every integer has a next one: there is no integer strictly between \( m \) and \( m + 1 \) (@thm-integers-ordered-ring (c)). In \( \nQ \) the opposite holds. Let \( 2 \coloneqq 1 + 1 \). By @prp-ordered-ring-rules (e) and (b), \( 1 > 0 \) and \( 2 > 0 \), so \( 1/2 > 0 \) by @prp-reciprocal-order (a). Now let \( a < b \) in \( \nQ \). Adding \( a \), and then \( b \), by (O3),
\[
a + a < a + b < b + b ,
\]
and \( a + a = (1 + 1)a = 2a \), \( b + b = 2b \) by distributivity. Multiplying by \( 1/2 > 0 \) (@prp-ordered-ring-rules (c)) gives
\[
a < \frac{a + b}{2} < b .
\]
So between two distinct rationals there is always a third, their **midpoint**. Applied with \( a = 0 \): for every \( x > 0 \), also \( 0 < x/2 < x \). Hence \( \nQ_{>0} \) has **no least element**. In particular, well-ordering is a property of \( \nN \) (@thm-omega-well-ordering) that \( \nQ_{>0} \) does not share.

::: {.warning}
Between any two rationals lies another, but that does not mean every rational has a neighbor "right next to it". It means the opposite: no rational \( x \) has a next one, since any candidate \( y > x \) is beaten by the midpoint of \( x \) and \( y \). Phrases like "the rational just after \( 0 \)" name nothing.
:::

::: {.check}
Find the midpoint of \( 1/3 \) and \( 1/2 \), and confirm with the comparison formula that it lies strictly between them.
:::

::: {.solution}
\( 1/3 + 1/2 = 5/6 \) by @def-rational-operations (\( [(1 \cdot 2 + 1 \cdot 3, \, 6)] \)), and \( (5/6) \cdot (1/2) = 5/12 \). By @thm-rationals-ordered-field (a): \( 1/3 < 5/12 \) because \( 1 \cdot 12 = 12 < 15 = 5 \cdot 3 \), and \( 5/12 < 1/2 \) because \( 5 \cdot 2 = 10 < 12 = 1 \cdot 12 \).
:::

## The Archimedean property

Here is a statement so familiar that it seems not to need proof: every rational number is smaller than some natural number. For the real numbers it is a genuine theorem. Chapter 11 obtains it from the least upper bound axiom, and there are ordered fields, built from rational functions, in which the natural numbers are bounded above. For the constructed \( \nQ \) it is true for a simpler reason: every rational is a quotient of integers, and integers are as discrete as natural numbers.

::: {#thm-rationals-archimedean}
[The Rationals Are Archimedean]

For every \( x \in \nQ \) there is \( n \in \nN \) with \( x < n \).
:::

*Try it first (ten minutes): given \( x = p/q \) with \( q \in \nZ_{>0} \), which natural number beats it? Do not forget negative \( p \).*

::: {.idea}
The first candidate is \( p + 1 \), on the grounds that dividing by \( q \ge 1 \) "makes things smaller", so \( p/q \le p < p + 1 \). An attempt meets two obstacles. Dividing by \( q \ge 1 \) makes a **negative** number larger: \( -3/2 > -3 \). And \( p + 1 \) is not a natural number when \( p \le -2 \). Both disappear if we split on the sign of \( p \). A fraction with \( p \le 0 \) is at most \( 0 \), and \( 1 \) beats it. For \( p > 0 \) the school intuition is right and provable: \( q \ge 1 \) gives \( p \le pq \), which the comparison formula reads as \( p/q \le p \).
:::

::: {.proof}
Let \( x \in \nQ \). By @prp-integers-embed-rationals (b), \( x = p/q \) with \( p \in \nZ \) and \( q \in \nZ_{>0} \).

*Case 1: \( p \le 0 \).* By @eq-comparison-le, \( p/q \le 0/1 \), since \( p \cdot 1 \le 0 \cdot q \). So \( x \le 0 < 1 \) (@prp-ordered-ring-rules (e)), and \( n \coloneqq 1 \in \nN \) works.

*Case 2: \( p > 0 \).* Then \( p \in \nN \) by @thm-integers-ordered-ring (b). Since \( q > 0 \), discreteness (@thm-integers-ordered-ring (c), with \( 0 < q \)) gives \( 1 \le q \). Multiplying by \( p > 0 \) (@prp-ordered-ring-rules (c), or equality if \( q = 1 \)) gives \( p \cdot 1 \le p \cdot q \). By @eq-comparison-le this says \( p/q \le p/1 = p \). Finally \( p < p + 1 \) by (O3), since \( 0 < 1 \). So \( x \le p < p + 1 \), and \( n \coloneqq p + 1 \) lies in \( \nN \), because \( \nN \) is closed under addition. Hence \( x < n \).

In both cases \( x < n \) for some \( n \in \nN \), as claimed.
:::

The \( n \) found depends on \( x \), through the numerator of the representative used; a different representative may give a different \( n \), and any one will do. The proof cites the representation \( x = p/q \), the comparison formula, discreteness of \( \nZ \), and the order axioms, and nothing else: no supremum is mentioned in it. That is the contrast with the real numbers, where the same conclusion needs the completeness axiom.

The form in which later chapters of this volume use the property is about reciprocals: \( 1/n \) eventually falls below any positive rational.

::: {#cor-rationals-archimedean-epsilon}
[Small Reciprocals in \( \nQ \)]

For every \( \varepsilon \in \nQ_{>0} \) there is \( n \in \nZ_{>0} \) with \( 1/n < \varepsilon \). Moreover every \( m \in \nZ \) with \( m \ge n \) then also satisfies \( 1/m < \varepsilon \). In symbols,
\[
\forall \varepsilon \in \nQ_{>0} \ \ \exists n \in \nZ_{>0} \ \ \forall m \in \nZ_{>0} \ \ \bigl( m \ge n \Rightarrow 1/m < \varepsilon \bigr) .
\]
:::

::: {.proof}
Let \( \varepsilon \in \nQ_{>0} \). By @prp-reciprocal-order (a), \( 1/\varepsilon > 0 \). By @thm-rationals-archimedean there is \( n \in \nN \) with \( 1/\varepsilon < n \). Then \( n > 0 \), so \( n \in \nZ_{>0} \) (@thm-integers-ordered-ring (b)). By @prp-reciprocal-order (b) with \( 0 < 1/\varepsilon < n \),
\[
\frac{1}{n} < \frac{1}{1/\varepsilon} = \varepsilon ,
\]
where \( 1/(1/\varepsilon) = \varepsilon \) because \( \varepsilon \) is a multiplicative inverse of \( \varepsilon^{-1} \), and inverses are unique (if \( bc = 1 = bc' \), then \( c = c(bc') = (cb)c' = c' \)). If \( m \ge n \), then either \( m = n \), or \( 0 < n < m \) and \( 1/m < 1/n \) by @prp-reciprocal-order (b); in both cases \( 1/m \le 1/n < \varepsilon \).
:::

The order of the quantifiers is the point: \( \varepsilon \) is given first, and \( n \) is chosen after it and **depends on \( \varepsilon \)**. Exercise A1 asks what happens if the order is swapped. In this volume \( \varepsilon \) is always a **rational** number; the real numbers are not yet available, and the corollary is the form in which a later chapter of this volume uses the Archimedean property, with \( \varepsilon \in \nQ_{>0} \).

## The integer part

By @thm-rationals-archimedean, every rational lies below an integer. With the least-element property of \( \nZ \), it pins every rational between two consecutive integers.

::: {#prp-rational-integer-part}
[Integer Part of a Rational]

For every \( x \in \nQ \) there is **exactly one** \( m \in \nZ \) with \( m \le x < m + 1 \). It is called the **integer part** of \( x \) and written \( \floor{x} \).
:::

::: {.idea}
The integer just above \( x \) should be the least integer exceeding \( x \). So look at the set of integers that exceed \( x \): @thm-rationals-archimedean makes it non-empty, and applied to \( -x \) it bounds the set below, so @prp-integer-least-element hands us its least element. One less than that is the integer part. Uniqueness is discreteness: two candidates one unit apart cannot both fit below \( x \) and above \( x - 1 \).
:::

::: {.proof}
Let \( x \in \nQ \), and let \( S \coloneqq \{ k \in \nZ : x < k \} \). By @thm-rationals-archimedean there is \( n \in \nN \subseteq \nZ \) with \( x < n \), so \( S \ne \emptyset \). Applying @thm-rationals-archimedean to \( -x \) gives \( n' \in \nN \) with \( -x < n' \), that is, \( -n' < x \) (@prp-ordered-ring-rules (a)). Every \( k \in S \) then has \( -n' < x < k \), so the integer \( -n' \) is a lower bound of \( S \). By @prp-integer-least-element, \( S \) has a least element \( l \). Let \( m \coloneqq l - 1 \in \nZ \), so that \( l = m + 1 \).

*Existence.* \( x < l = m + 1 \), since \( l \in S \). And \( m \notin S \): otherwise \( l \le m = l - 1 < l \), so \( l < l \), against (O1). So \( x < m \) fails, and \( m \le x \) by totality (@prp-ordered-ring-rules (i)).

*Uniqueness.* Let \( m, m' \in \nZ \) both satisfy the condition, and suppose \( m < m' \). By discreteness (@thm-integers-ordered-ring (c)), \( m + 1 \le m' \). Then \( m' \le x < m + 1 \le m' \), so \( m' < m' \), against (O1). By symmetry \( m' < m \) is impossible too, so \( m = m' \) by (O1).
:::

The comparisons in this proof mix integers and rationals (\( x < k \)), and the least element is taken in \( \nZ \); by @thm-rationals-ordered-field (b) the two orders agree on \( \nZ \), so nothing is lost. A later chapter of this volume reads \( \floor{p/q} \), for \( q \in \nZ_{>0} \), as the quotient in the division of \( p \) by \( q \).

::: {.check}
Compute \( \floor{-7/3} \). Then find the least \( n \in \nZ_{>0} \) with \( 1/n < 3/1000 \).
:::

::: {.solution}
\( \floor{-7/3} = -3 \): by @eq-comparison-le, \( -3 = -3/1 \le -7/3 \) because \( (-3) \cdot 3 = -9 \le -7 \), and \( -7/3 < -2 \) because \( -7 < -6 = (-2) \cdot 3 \) (@thm-rationals-ordered-field (a)). Not \( -2 \): the rule "drop the fraction" works only for \( x \ge 0 \).

For \( n \in \nZ_{>0} \), the comparison formula gives \( 1/n < 3/1000 \) if and only if \( 1 \cdot 1000 < 3n \). Since \( 3 \cdot 333 = 999 < 1000 \) and \( 3 \cdot 334 = 1002 > 1000 \), the least such \( n \) is \( 334 \) (for \( n \le 333 \), \( 3n \le 999 \)).
:::

## Exercises

### A. Check your understanding

::: {#exr-ordered-field-of-rationals-a1}
[A1]

These questions are about the proof of @thm-rationals-ordered-field and about @cor-rationals-archimedean-epsilon.

::: {.enumerate options="label=(\alph*)"}
1. Where in the proof (including the well-definedness check before it) is \( q > 0 \) used? What goes wrong without it?
2. Why does (P2) need "**exactly** one" of \( x \in P_{\nQ} \), \( x = 0 \), \( -x \in P_{\nQ} \), and not just "at least one"?
3. Run the comparison formula on \( -2/3 \) and \( -3/5 \): which is larger?
4. State the idea of the proof in two sentences.
5. Write @cor-rationals-archimedean-epsilon (its first sentence) in symbols. Then write the version with the two quantifiers swapped, negate it, and decide which of the two versions is true.
:::
:::

::: {.solution}
(a) Three times: in the well-definedness check, \( q, q' > 0 \) turn \( p > 0 \) into \( p' > 0 \); in (P1), \( ps > 0 \) and \( rq > 0 \) need \( s > 0 \) and \( q > 0 \); in (a), the difference \( r/s - p/q \) has denominator \( qs > 0 \), so its sign is the sign of its numerator. Without it, the test "numerator positive" is not well defined: in @exm-fractions-nonzero-denominators, \( (1, 1) \sim (-1, -1) \) gives two verdicts for one class, and "\( ps < rq \)" gives \( 0 < 1 \) for \( (0, 1), (1, 1) \) but \( 0 < -1 \) for \( (0, 1), (-1, -1) \).

(b) "At least one" would allow a non-zero \( x \) with both \( x \) and \( -x \) positive, and then \( x < 0 \) and \( 0 < x \) at once, against (O1). The "at most one" half is what makes the order antisymmetric; @prp-order-from-positives uses it to get trichotomy (O1).

(c) By @thm-rationals-ordered-field (a), \( -2/3 < -3/5 \) if and only if \( (-2) \cdot 5 < (-3) \cdot 3 \), that is, \( -10 < -9 \), which is true. So \( -3/5 \) is the larger.

(d) By @prp-order-from-positives it is enough to show that the positive set is closed under \( + \) and \( \cdot \) and satisfies the trichotomy (P2). Each of these, run on representatives with positive denominators, is a statement about integer numerators, which holds because \( \nZ \) is an ordered ring.

(e) The corollary: \( \forall \varepsilon \in \nQ_{>0} \ \exists n \in \nZ_{>0} \ \ 1/n < \varepsilon \). Swapped: \( \exists n \in \nZ_{>0} \ \forall \varepsilon \in \nQ_{>0} \ \ 1/n < \varepsilon \), "one \( n \) works for every \( \varepsilon \)". By @prp-bounded-quantifier-negation (the bounded form of @prp-quantifier-negation), applied twice, its negation is
\[
\forall n \in \nZ_{>0} \ \ \exists \varepsilon \in \nQ_{>0} \ \ \neg (1/n < \varepsilon) .
\]
This negation is true: given \( n \in \nZ_{>0} \), take \( \varepsilon \coloneqq 1/n \), which lies in \( \nQ_{>0} \) by @prp-reciprocal-order (a), and \( 1/n < 1/n \) fails by (O1). So the swapped version is false, and the corollary (proved above) is true. The \( n \) must be allowed to depend on \( \varepsilon \).
:::

### B. Practice

::: {#exr-ordered-field-of-rationals-b1}
[B1]

Put \( -7/12 \), \( -3/5 \) and \( -4/7 \) in increasing order, using only the comparison formula.
:::

::: {.solution}
By @thm-rationals-ordered-field (a), pair by pair:

- \( -3/5 < -7/12 \), since \( (-3) \cdot 12 = -36 < -35 = (-7) \cdot 5 \);
- \( -7/12 < -4/7 \), since \( (-7) \cdot 7 = -49 < -48 = (-4) \cdot 12 \);
- \( -3/5 < -4/7 \), since \( (-3) \cdot 7 = -21 < -20 = (-4) \cdot 5 \).

Hence \( -3/5 < -7/12 < -4/7 \). (The third comparison follows from the first two by (O2); computing it is a check.)
:::

::: {#exr-ordered-field-of-rationals-b2}
[B2: A rational of the form a + 1/n]

::: {.enumerate options="label=(\alph*)"}
1. Let \( a, b \in \nQ \) with \( a < b \). Prove that there is \( n \in \nZ_{>0} \) with \( a < a + 1/n < b \), and that every \( m \in \nZ \) with \( m \ge n \) works too.
2. Find the least such \( n \) for \( a = 1/3 \) and \( b = 1/2 \).
:::
:::

::: {.solution}
(a) Let \( \varepsilon \coloneqq b - a \). Then \( \varepsilon > 0 \) by @prp-ordered-ring-rules (a), so @cor-rationals-archimedean-epsilon gives \( n \in \nZ_{>0} \) with \( 1/n < \varepsilon \), and \( 1/m < \varepsilon \) for every \( m \ge n \). Fix such an \( m \) (for instance \( m = n \)). Adding \( a \) (O3): \( a + 1/m < a + (b - a) = b \). And \( 1/m > 0 \) by @prp-reciprocal-order (a), since \( m > 0 \); adding \( a \) gives \( a < a + 1/m \).

(b) Here \( b - a = 1/2 - 1/3 = 1/6 \), and for \( n \in \nZ_{>0} \) the comparison formula gives \( 1/n < 1/6 \) if and only if \( 6 < n \). So the least \( n \) is \( 7 \), and \( a + 1/7 = 1/3 + 1/7 = 10/21 \). Check: \( 1/3 < 10/21 \) since \( 21 < 30 \), and \( 10/21 < 1/2 \) since \( 20 < 21 \). For \( n = 6 \), \( a + 1/6 = 1/2 = b \), which is not strictly below \( b \).
:::

::: {#exr-ordered-field-of-rationals-b3}
[B3]

Compute \( \floor{22/7} \), \( \floor{-22/7} \), \( \floor{0} \) and \( \floor{-1/100} \), and check each against the defining inequalities of @prp-rational-integer-part.
:::

::: {.solution}
We use @eq-comparison-le and the comparison formula with denominators \( 1 \) for the integers.

- \( \floor{22/7} = 3 \): \( 3 \le 22/7 \) since \( 3 \cdot 7 = 21 \le 22 \), and \( 22/7 < 4 \) since \( 22 < 28 = 4 \cdot 7 \).
- \( \floor{-22/7} = -4 \): \( -4 \le -22/7 \) since \( -28 \le -22 \), and \( -22/7 < -3 \) since \( -22 < -21 \).
- \( \floor{0} = 0 \): \( 0 \le 0 < 1 \).
- \( \floor{-1/100} = -1 \): \( -1 \le -1/100 \) since \( -100 \le -1 \), and \( -1/100 < 0 \) since \( -1 < 0 \).

The second and fourth show that \( \floor{-x} \ne -\floor{x} \) in general: \( \floor{-22/7} = -4 \), not \( -3 \).
:::

### C. Going deeper

::: {#exr-ordered-field-of-rationals-c1}
[C1: Exit check: \( \nQ \) is Archimedean]

Prove, from the construction of \( \nQ \) and the results of this chapter (and not from any fact about the real numbers), that for every \( x \in \nQ \) there is \( n \in \nN \) with \( x < n \); and deduce that for every \( \varepsilon \in \nQ_{>0} \) there is \( n \in \nZ_{>0} \) with \( 1/n < \varepsilon \).
:::

::: {.solution}
*The theorem.* Let \( x \in \nQ \). By @prp-integers-embed-rationals (b), \( x = p/q \) with \( p \in \nZ \) and \( q \in \nZ_{>0} \).

If \( p \le 0 \), then \( p \cdot 1 \le 0 \cdot q \), so \( x = p/q \le 0/1 = 0 \) by the comparison formula (@thm-rationals-ordered-field (a), with equality by @prp-integers-embed-rationals (b)). Hence \( x \le 0 < 1 \), and \( n = 1 \) works.

If \( p > 0 \), then \( p \in \nN \) (@thm-integers-ordered-ring (b)), and \( q \ge 1 \) by discreteness (@thm-integers-ordered-ring (c)), since \( q > 0 \). Multiplying \( 1 \le q \) by \( p > 0 \) gives \( p \le pq \) (@prp-ordered-ring-rules (c)), which by the comparison formula says \( p/q \le p/1 \). So \( x \le p < p + 1 \), and \( n \coloneqq p + 1 \in \nN \) works.

*The corollary.* Let \( \varepsilon \in \nQ_{>0} \) be given. Then \( 1/\varepsilon > 0 \) (@prp-reciprocal-order (a)), and the theorem gives \( n \in \nN \) with \( 1/\varepsilon < n \); in particular \( n > 0 \), so \( n \in \nZ_{>0} \). By @prp-reciprocal-order (b), \( 1/n < 1/(1/\varepsilon) = \varepsilon \). The \( n \) depends on \( \varepsilon \), which was fixed first.

**Marking scheme.** (10 points)
- 1: writes \( x = p/q \) with \( p \in \nZ \), \( q \in \nZ_{>0} \), citing the representation of rationals.
- 2: the case \( p \le 0 \): \( x \le 0 < 1 \), justified by the comparison formula.
- 3: the case \( p > 0 \): \( q \ge 1 \) by discreteness of \( \nZ \), and \( p/q \le p \) by the comparison formula (or an equivalent inequality argument from the ordered-field rules).
- 1: exhibits \( n \in \nN \) (for instance \( p + 1 \)) and checks \( x < n \).
- 3: the corollary: \( \varepsilon \) fixed first, \( n > 1/\varepsilon \) from the theorem, reciprocals reverse order.
Fatal errors (0 for the step): no separate treatment of \( p < 0 \) (there "\( p/q \le p \)" fails once \( q \ge 2 \), as \( -3/2 > -3 \) shows, and \( p + 1 \notin \nN \) once \( p \le -2 \)); using a supremum, the real numbers, or "the decimal expansion of \( x \)". A route through @prp-rational-integer-part is circular here (its proof uses the theorem) and earns nothing for the first five points.
:::

::: {#exr-ordered-field-of-rationals-c2}
[C2: The comparison, on representatives]

The comparison formula of @thm-rationals-ordered-field (a) was proved through the positive set. Prove directly that the relation "\( ps < rq \)" on pairs in \( \nZ \times \nZ_{>0} \) does not depend on the representatives: if \( (p, q) \sim (p', q') \) and \( (r, s) \sim (r', s') \), then \( ps < rq \) if and only if \( p's' < r'q' \).

Here is the start.

> We change one argument at a time. *First argument:* let \( (p, q) \sim (p', q') \) and \( ps < rq \); we must show \( p's < rq' \).
>
> ...

*Name the move, then complete it.*
:::

::: {.solution}
The move is **check on representatives, one argument at a time**: change the first pair with the second fixed, then the second with the first fixed, and join the two by transitivity of \( \iff \).

*First argument.* Let \( pq' = p'q \) and \( ps < rq \). Multiply by \( q' > 0 \) (@prp-ordered-ring-rules (c)): \( psq' < rqq' \). The left side is \( (pq')s = (p'q)s = (p's)q \), and the right side is \( (rq')q \). So \( (p's)q < (rq')q \). If \( p's \ge rq' \), then multiplying by \( q > 0 \) would give \( (p's)q \ge (rq')q \) (@prp-ordered-ring-rules (c), or equality), against (O1). So \( p's < rq' \). Since \( \sim \) is symmetric, the same argument with the roles of \( (p, q) \) and \( (p', q') \) exchanged gives the converse: \( ps < rq \iff p's < rq' \).

*Second argument.* Let \( rs' = r's \), and fix \( (p', q') \). If \( p's < rq' \), multiply by \( s' > 0 \): \( p'ss' < rq's' \), and \( rs' = r's \) turns the right side into \( (r's)q' = (r'q')s \). So \( (p's')s < (r'q')s \), and canceling \( s > 0 \) as above gives \( p's' < r'q' \). By symmetry again, \( p's < rq' \iff p's' < r'q' \).

*Join.* Chaining the two equivalences,
\[
ps < rq \iff p's < rq' \iff p's' < r'q' .
\]
This proves the claim. By @thm-rationals-ordered-field (a) both sides also mean \( p/q < r/s \); the point of the exercise is that the integer relation alone is already independent of the representatives, and positivity of \( q, q', s, s' \) is used at every multiplication and cancellation.
:::

::: {#exr-ordered-field-of-rationals-c3}
[C3: Find the error]

Here is an argument for @thm-rationals-archimedean. Is the conclusion true? Is the argument correct? If not, name the first line that fails, say what makes it illegal, and give a counterexample to the step.

> (1) Let \( x \in \nQ \), and write \( x = p/q \) with \( p \in \nZ \) and \( q \in \nZ_{>0} \). (2) Then \( q \ge 1 \), by discreteness of \( \nZ \). (3) So \( x = p/q \le p \), since dividing by a number at least \( 1 \) cannot increase it. (4) Hence \( n \coloneqq p + 1 \) is a natural number with \( n > x \).
:::

::: {.solution}
The conclusion is **true**: it is @thm-rationals-archimedean. The argument is **not** correct.

*The failing line is (3).* It cites the general "fact" that \( p/q \le p \) whenever \( q \ge 1 \). That is neither proved in this chapter nor true, so the line rests on nothing: entry (N9) of @exm-not-allowed-catalogue. What is true, and what the proof of the theorem uses, is the special case \( p \ge 0 \).

*Counterexample to the step.* \( p = -3 \), \( q = 2 \): then \( q \ge 1 \), but \( x = -3/2 > -3 = p \). Indeed the comparison formula gives \( -3/1 < -3/2 \), because \( (-3) \cdot 2 = -6 < -3 = (-3) \cdot 1 \). There is no counterexample to the conclusion.

*A second failing line.* Line (4) also fails for \( p \le -2 \): then \( p + 1 \le -1 \), which is not in \( \nN = \{ n \in \nZ : n \ge 0 \} \) (@thm-integers-ordered-ring (b)). For \( p = -1 \), \( n = 0 \) happens to work, because \( x < 0 \); but the stated reason "\( x \le p \)" still fails there once \( q \ge 2 \).

*Repair.* Split on the sign of \( p \), as the proof of @thm-rationals-archimedean does: for \( p \le 0 \), \( x \le 0 < 1 \); for \( p > 0 \), line (3) is correct, with the comparison formula as its reason (\( p \cdot 1 \le p \cdot q \)).

**Marking scheme.** (10 points)
- 2: says that the conclusion is true and the argument is not correct.
- 3: names line (3), and the unproved general claim "\( p/q \le p \) for \( q \ge 1 \)" (entry (N9)) as what makes it illegal.
- 2: gives a counterexample to the step with \( p < 0 \) and \( q \ge 2 \), checked by the comparison formula.
- 1: notes that line (4) fails as well for \( p \le -2 \).
- 2: repairs the argument by a case split on the sign of \( p \).
Fatal errors (0 for the step): declaring the conclusion false; offering a counterexample to the conclusion.
:::

<!-- dependency ledger
def-rational-order (claim): equal classes have related representatives, so [(p, q)] = [(0, 1)] iff p = 0 | prp-integers-embed-rationals (b) (cited)
thm-rationals-ordered-field (proof): 0 + 0 = 0 and 0 * q = 0, p * 1 = p in Z | prp-ring-algebra (b), thm-integers-commutative-ring (ring axioms of Z)
thm-rationals-ordered-field (proof): s q = q s and the regrouping of rq + (-p)s as rq - ps | thm-integers-commutative-ring (F1)-(F9), def-commutative-ring-and-field (a - b := a + (-b))
thm-rationals-ordered-field (claim): p/q = r/s is [(p, q)] = [(r, s)], and j(m) = m/1 | prp-integers-embed-rationals (a), (b) (cited)
prp-reciprocal-order (proof): 1 != 0 in a field; a a^{-1} = 1; associativity and commutativity of products | def-commutative-ring-and-field (F7), (F8), (F1)-(F9)
prp-reciprocal-order (proof): 0 < a < b gives 0 < b | def-ordered-ring-and-field (O2)
thm-rationals-archimedean (proof): N is closed under +, so p + 1 in N for p in N | prp-naturals-embed-integers (iota preserves +; + is a function on omega, def-omega-arithmetic)
thm-rationals-archimedean (proof): 1 <= q and p > 0 give p * 1 <= p * q (equality case q = 1 separately) | prp-ordered-ring-rules (c), cited
cor-rationals-archimedean-epsilon (proof): inverses in a field are unique, so 1/(1/eps) = eps | inline (one line)
prp-rational-integer-part (proof): totality of <= on Q (not x < m gives m <= x) | prp-ordered-ring-rules (i), cited
prp-rational-integer-part (proof): the order of Q restricted to Z is that of Z, so prp-integer-least-element applies to S | thm-rationals-ordered-field (b), cited in the paragraph after the proof
prp-rational-integer-part (claim): floor(p/q) is the quotient of division with remainder | a later chapter of this volume (F3.5, prose pointer; nothing depends on it)
thm-rationals-archimedean (claim): for R the property needs the least upper bound axiom; ordered fields of rational functions with N bounded above | Ch 11 (prose pointer; nothing here depends on it)
prp-reciprocal-order (claim): (the midpoint paragraph after it) a + a = (1 + 1) a; (a + b)/2 = (a + b) * 2^{-1} | def-commutative-ring-and-field (distributivity, a/b := a b^{-1})
exr-ordered-field-of-rationals-a1 (solution): numerals and products such as (-2) * 5 = -10 in Z | omega arithmetic (def-omega-arithmetic) carried by iota (prp-naturals-embed-integers) and signs by prp-ring-algebra (c); verify/ch10/exr-ordered-field-of-rationals-a1.py
exr-ordered-field-of-rationals-b1 (solution): integer products -36, -35, -49, -48, -21, -20 | as above; verify/ch10/exr-ordered-field-of-rationals-b1.py
exr-ordered-field-of-rationals-b2 (solution): 1/2 - 1/3 = 1/6 and 1/3 + 1/7 = 10/21 | def-rational-operations; verify/ch10/exr-ordered-field-of-rationals-b2.py
exr-ordered-field-of-rationals-b3 (solution): the eight integer comparisons | thm-rationals-ordered-field (a); verify/ch10/exr-ordered-field-of-rationals-b3.py
exr-ordered-field-of-rationals-c2 (solution): symmetry of ~ on Z x Z_{>0} | prp-rational-pairs-equivalence (cited in section 10.4)
-->
