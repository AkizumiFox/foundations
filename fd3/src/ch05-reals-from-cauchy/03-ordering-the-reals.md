# Positive Classes and the Order

<!-- S3: style revision per S1 change list (layout-proposal.md §3, 5.3, pipeline S): trim; prp-reals-absolute-value-termwise becomes an exercise (label kept); new method box (provisional exm-method-margin-before-index). -->

Section 5.2 made \( \nR \) a field: its elements are classes of Cauchy sequences of rationals, added and multiplied through representatives. A field is not yet a number line. To compare two real numbers we need an order, and it must cooperate with the arithmetic: \( \nR \) should be an ordered field in the sense of @def-ordered-ring-and-field. Chapter 3 ordered \( \nQ \) in two steps. It first said which rationals are positive, and then let \( a < b \) mean that \( b - a \) is positive (@prp-order-from-positives). This section takes the same two steps for \( \nR \). All the work is in the first: deciding which classes are positive, in a way that does not depend on the representative.

Throughout, \( \sC \) is the set of Cauchy sequences of rationals (@def-rational-cauchy-sequences), \( a \sim b \) means that \( a - b \) is null in \( \nQ \) (@def-cauchy-equivalent), and \( [a] \) is the class of \( a \), an element of \( \nR \) (@def-reals-cauchy-classes). Until \( \nR \) has an order, every tolerance, margin and threshold is a rational or a natural number: we are still building \( \nR \), and may not measure anything with it. The operations are those of @def-reals-operations: \( [a] + [b] = [a + b] \), \( [a][b] = [ab] \), \( -[a] = [-a] \), with \( 0_{\nR} = [(0)_n] \) and \( 1_{\nR} = [(1)_n] \), where \( (q)_n \) is the constant sequence with value \( q \). In particular
\[
[a] - [b] = [a] + [-b] = [a - b] ,
\]
since \( a + (-b) = a - b \) termwise. We use this without comment.

## Comparing terms does not compare classes

The first idea is to compare two classes by comparing their terms. It fails, and the way it fails shows what the definition must contain.

::: {#exm-strict-termwise-order-fails}
[Termwise Order Is Not an Order on Classes]

Consider the rule

> \( [a] < [b] \) means that \( a_n < b_n \) for every \( n \) from some index on.

Let \( a_n \coloneqq 0 \) and \( b_n \coloneqq 1/(n + 1) \) for \( n \in \nN \). Show that \( [a] = [b] \). Then apply the rule to the classes \( [a] \) and \( [a] \) twice: once through the representatives \( a \) and \( a \), once through \( a \) and \( b \). Conclude that the rule does not define a relation on \( \nR \).
:::

::: {.solution}
Both sequences are in \( \sC \): a constant sequence and a null sequence are Cauchy (@thm-cauchy-algebra-ordered-field (a)), and \( (1/(n + 1)) \) is null in \( \nQ \) (@exm-first-sequences-ordered-field (b)). Termwise, \( b - a = (1/(n + 1)) \), which is null, so \( b \sim a \), and \( [a] = [b] \) by @fd2:thm-classes-partition (b).

Through the representatives \( a \) and \( a \): the rule asks whether \( 0 < 0 \) from some index on, and \( 0 < 0 \) never holds. So the rule says that \( [a] < [a] \) is false.

Through the representatives \( a \) and \( b \), which name the same two classes, since \( b \in [b] = [a] \): for **every** \( n \), \( a_n = 0 < 1/(n + 1) = b_n \). So the rule says that \( [a] < [a] \) is true.

A relation on \( \nR \) must give one answer for each pair of classes. The rule gives two answers for the pair \( (0_{\nR}, 0_{\nR}) \), depending on the representatives, so it defines no relation on \( \nR \). Worse, the second answer, \( 0_{\nR} < 0_{\nR} \), is excluded by trichotomy (O1) in any ordered field.
:::

The trouble is that the gap between \( a_n \) and \( b_n \) is allowed to shrink to nothing, and a gap that shrinks to nothing is exactly what \( \sim \) ignores. A class that deserves to be called positive must have terms that stay above \( 0 \) by a **fixed** margin.

## Positive sequences

We look for a property of a single sequence \( a \in \sC \) that says "the number \( a \) names is greater than \( 0 \)". The example shows that "eventually \( a_n > 0 \)" is too weak, because a null sequence can have it. The repair is to name the margin first.

*Positive means: eventually above one fixed positive rational.*

::: {#def-positive-cauchy-sequence}
[Positive Cauchy Sequence]

A sequence \( a \in \sC \) is **positive** if **there exist** \( \delta \in \nQ_{>0} \) and \( N \in \nN \) such that \( a_n \ge \delta \) **for every** \( n \in \nN \) with \( n \ge N \). In symbols,
\[
\exists \delta \in \nQ_{>0} \ \ \exists N \in \nN \ \ \forall n \in \nN \ \ ( n \ge N \Rightarrow a_n \ge \delta ) .
\]
:::

In words: the first quantifier names a margin \( \delta \), a positive rational, before anything else is named; the second names a threshold; the third says that **every** term from the threshold on is at least the margin. Because \( \delta \) comes first, one margin serves all the late terms at once. The word "positive" describes the sequence as a name for a number, not its terms one by one: the terms before \( N \) may be negative, and, as the warning below shows, terms that are all \( > 0 \) are not enough.

Compare the definition with the weaker condition "the terms are eventually positive":
\[
\exists N \in \nN \ \ \forall n \in \nN \ \ ( n \ge N \Rightarrow a_n > 0 ) .
\]
Here each late term \( a_n \) is above \( 0 \) by its own amount, namely \( a_n \) itself, and these amounts may shrink as \( n \) grows. In the definition the amount is chosen before \( n \), so it cannot depend on \( n \). The two conditions differ only in the order of "there is a margin" and "for every late \( n \)", and that order is the whole point.

**Examples.**

*A positive constant.* For \( q \in \nQ_{>0} \), the constant sequence \( (q)_n \) is positive, with \( \delta = q \) and \( N = 0 \). This degenerate case is how Section 5.4 will see that the rational \( q \), placed inside \( \nR \), is greater than \( 0 \).

*The Newton sequence.* Let \( (x_n) \) be the sequence of @exm-newton-rationals-sqrt2, which is in \( \sC \) by @thm-sqrt2-cauchy-no-rational-limit. The same theorem states that \( x_n > 1 \) for every \( n \in \nN \). So \( (x_n) \) is positive, with \( \delta = 1 \) and \( N = 0 \).

*Late positivity.* Let \( a_n \coloneqq 1 - 2/(n + 1) \). It is in \( \sC \), as the difference of a constant sequence and a constant multiple of the null sequence \( (1/(n + 1)) \) (@thm-cauchy-algebra-ordered-field (a), (b)). Its first terms are \( -1, 0, 1/3, 1/2 \), so it is not positive "from the start". For \( n \ge 3 \), \( n + 1 \ge 4 \), so \( 1/(n + 1) \le 1/4 \) (@prp-ordered-field-halves (c)), hence \( 2/(n + 1) \le 2/4 = 1/2 \) (@prp-ordered-field-halves (d), with \( 0 \le 2 \le 2 \)), and \( a_n \ge 1/2 \). So \( a \) is positive, with \( \delta = 1/2 \) and \( N = 3 \). No smaller \( N \) works with this \( \delta \), since \( a_2 = 1/3 < 1/2 \); the definition allows any finite stretch of bad terms.

**Non-example by a minimal change.** Keep every term positive, but let the margin shrink: \( a_n \coloneqq 1/(n + 1) \). Every term is \( > 0 \), so the weaker condition above holds with \( N = 0 \). What fails is the order of the quantifiers. The negation of the definition, by @fd1:prp-bounded-quantifier-negation and @fd1:prp-negated-implication, reads
\[
\forall \delta \in \nQ_{>0} \ \ \forall N \in \nN \ \ \exists n \in \nN \ \ ( n \ge N \wedge a_n < \delta ) ,
\]
and it holds: given \( \delta \) and \( N \), @cor-rationals-archimedean-epsilon gives \( n_0 \in \nZ_{>0} \) with \( 1/m < \delta \) for every \( m \ge n_0 \). With \( n \coloneqq \max\{N, n_0\} \), we have \( n \ge N \), and \( m \coloneqq n + 1 \ge n_0 \), so \( a_n = 1/(n + 1) < \delta \). Every margin is eventually undercut.

**Why this definition.** Each clause has a job.

- *The margin \( \delta \).* Without it, the definition would be the weaker condition, and @exm-strict-termwise-order-fails shows the result: \( (1/(n + 1)) \) would be positive, while \( (0)_n \), which names the same number \( 0_{\nR} \), is not.
- *A rational margin.* The only positive numbers available are rationals. A real margin would use the order of \( \nR \), which is what we are defining.
- *The threshold \( N \).* Changing finitely many terms does not change the class (@exm-finite-change-equivalent), so a definition meant for classes must ignore every finite stretch of terms. The late-positivity example needs \( N = 3 \).
- *\( \ge \) rather than \( > \).* Either would do: \( a_n \ge \delta \) gives \( a_n > \delta/2 \), and \( a_n > \delta \) gives \( a_n \ge \delta \). We use \( \ge \), the form in which @thm-cauchy-not-null-sign delivers its conclusion.

::: {.warning}
"Every term of \( a \) is positive" does **not** make \( a \) positive. The sequence \( (1/(n + 1)) \) has every term \( > 0 \), and it is not positive (non-example above); its class is \( 0_{\nR} \).
:::

::: {.check}
Let \( a \in \sC \), with \( \delta \) ranging over \( \nQ_{>0} \). Which of the two conditions
\[
\text{(A)} \ \exists \delta \ \exists N \ \forall n \ge N \ \ a_n \ge \delta , \qquad \text{(B)} \ \exists N \ \forall n \ge N \ \exists \delta \ \ a_n \ge \delta
\]
implies the other? Which of them says the same as "eventually \( a_n > 0 \)"?
:::

::: {.solution}
(A) implies (B): the margin found once serves as the \( \delta \) for every late \( n \). (B) does not imply (A): \( (1/(n + 1)) \) satisfies (B), with \( \delta \coloneqq 1/(n + 1) \) chosen after \( n \), and fails (A). (B) says the same as "eventually \( a_n > 0 \)": if \( a_n > 0 \), take \( \delta \coloneqq a_n \); if \( a_n \ge \delta > 0 \), then \( a_n > 0 \). So (A) is the definition of positive, and (B) is the weaker condition.
:::

**Payoff: positivity belongs to the class.** A real number is a class, and a definition about sequences says something about the class only if equivalent sequences agree on it. Chapter 4 proved the fact we need while preparing for this chapter: a margin survives a null change of the sequence, at half its size (@prp-sign-stable-ordered-field).

::: {#prp-positivity-well-defined}
[Positivity Is a Property of the Class]

Let \( a, a' \in \sC \) with \( a' \sim a \). If \( a \) is positive, then \( a' \) is positive.
:::

::: {.proof}
Since \( a \) is positive, there are \( \delta \in \nQ_{>0} \) and \( N \in \nN \) with \( a_n \ge \delta \) for every \( n \ge N \); fix them \( [\rulename{\exists E}] \) (@fd1:def-rules-existential). Since \( \sim \) is symmetric (@prp-cauchy-equivalent-relation), \( a \sim a' \), that is, \( (a_n - a'_n) \) is null in \( \nQ \). @prp-sign-stable-ordered-field, with \( F = \nQ \), the sequences \( a \) and \( a' \), and \( c = \delta \), gives \( N' \in \nN \) with \( a'_n \ge \delta/2 \) for every \( n \ge N' \). Since \( \delta/2 \in \nQ_{>0} \) (@prp-ordered-field-halves (b)), \( a' \) is positive, with margin \( \delta/2 \) and threshold \( N' \).
:::

The margin halves, and that is harmless: the definition asks only for **some** margin. Exercise C2 shows a tempting proof of this proposition that keeps a margin of \( 0 \), and so does not prove it.

We can now name the set of positive real numbers. Let
\[
P \coloneqq \{ [a] : a \in \sC \text{ and } a \text{ is positive} \} \subseteq \nR .
\]
Chapters 2 and 3 built the positive sets \( P_{\nZ} \) and \( P_{\nQ} \); \( P \) is the same step for \( \nR \). For \( x \in \nR \):
\[
x \in P \iff \text{some representative of } x \text{ is positive} \iff \text{every representative of } x \text{ is positive} .
\]
The first equivalence is the definition of \( P \). For the second, every class has a representative (@fd2:thm-classes-partition (a)), which gives "every \( \Rightarrow \) some". Conversely, if \( x = [a] \) with \( a \) positive and \( b \in x \), then \( b \sim a \) (@fd2:def-equivalence-class), so \( b \) is positive by @prp-positivity-well-defined. Membership in \( P \) can therefore be tested on **any** representative we like. This is the well-definedness the termwise rule lacked.

## The positive classes

Chapter 2's recipe needs two facts about \( P \): it is closed under sum and product, and it splits \( \nR \) into three parts, \( P \), \( \{0_{\nR}\} \) and the negatives of \( P \). These are clauses (P1) and (P2) of @prp-order-from-positives.

::: {#thm-reals-positive-cone}
[The Positive Real Numbers]

::: {.enumerate options="label=(\roman*)"}
1. For every \( x \in \nR \), **exactly one** of \( x \in P \), \( x = 0_{\nR} \), \( -x \in P \) holds.
2. If \( x \in P \) and \( y \in P \), then \( x + y \in P \) and \( xy \in P \).
:::
:::

::: {.idea}
For (i), "at least one" is the sign theorem of Chapter 4: a Cauchy sequence that is not null is eventually above \( c \) or eventually below \( -c \) (@thm-cauchy-not-null-sign). A null representative gives \( 0_{\nR} \). "At most one" holds because a sequence cannot be eventually above a positive margin and also eventually below a negative one, or null. For (ii), add or multiply the two margins and take the later of the two thresholds.
:::

::: {.proof}
Let \( x \in \nR \), and write \( x = [a] \) with \( a \in \sC \).

(i), *at least one.* Suppose first that \( a \) is null. Termwise \( a - (0)_n = a \), so \( a \sim (0)_n \) and \( x = [(0)_n] = 0_{\nR} \). Suppose next that \( a \) is not null. By @thm-cauchy-not-null-sign with \( F = \nQ \), there are \( c \in \nQ_{>0} \) and \( N \in \nN \) such that either \( a_n \ge c \) for every \( n \ge N \), or \( a_n \le -c \) for every \( n \ge N \); fix them \( [\rulename{\exists E}] \). In the first case \( a \) is positive, so \( x \in P \). In the second case \( -a_n \ge c \) for every \( n \ge N \) (@prp-ordered-ring-rules (a)), so \( -a \) is positive and \( -x = [-a] \in P \).

(i), *at most one.* We exclude the three pairs.

- \( x \in P \) and \( x = 0_{\nR} \). Then \( (0)_n \) is a representative of \( x \), so it is positive, since every representative of an element of \( P \) is: some \( \delta \in \nQ_{>0} \) has \( 0 \ge \delta \). This contradicts \( \delta > 0 \) by (O1) in \( \nQ \).
- \( -x \in P \) and \( x = 0_{\nR} \). Then \( -x = [-(0)_n] = [(0)_n] = 0_{\nR} \), and the previous case, applied to \( -x \), excludes this.
- \( x \in P \) and \( -x \in P \). Then \( a \) and \( -a \) are both positive: \( a_n \ge \delta \) for \( n \ge N \) and \( -a_n \ge \delta' \) for \( n \ge N' \), with \( \delta, \delta' \in \nQ_{>0} \). At \( n \coloneqq \max\{N, N'\} \), \( \delta \le a_n \le -\delta' \) (@prp-ordered-ring-rules (a)), so \( 0 < \delta \le -\delta' < 0 \), against (O1) in \( \nQ \).

(ii) Let \( x, y \in P \), and write \( x = [a] \), \( y = [b] \). Both \( a \) and \( b \) are positive: there are \( \delta_a, \delta_b \in \nQ_{>0} \) and \( N_a, N_b \in \nN \) with \( a_n \ge \delta_a \) for \( n \ge N_a \) and \( b_n \ge \delta_b \) for \( n \ge N_b \). Let \( N \coloneqq \max\{N_a, N_b\} \) and \( n \ge N \). Adding the two inequalities (@prp-ordered-ring-rules (b)),
\[
a_n + b_n \ge \delta_a + \delta_b ,
\]
and \( \delta_a + \delta_b > 0 + 0 = 0 \) by the same rule. Multiplying, by @prp-ordered-field-halves (d) applied to \( 0 \le \delta_a \le a_n \) and \( 0 \le \delta_b \le b_n \),
\[
a_n b_n \ge \delta_a \delta_b ,
\]
and \( \delta_a \delta_b > 0 \) by (O4). So \( a + b \) and \( ab \) are positive, with margins \( \delta_a + \delta_b \) and \( \delta_a \delta_b \) and the threshold \( N \). Hence \( x + y = [a + b] \in P \) and \( xy = [ab] \in P \) (@def-reals-operations).
:::

Both parts rest on a choice of representatives, and neither depends on it: membership in \( P \) can be tested on any representative, which is what @prp-positivity-well-defined bought. In (ii), the margins and the threshold depend on \( a \) and \( b \), and on nothing else.

## The order of the reals

With \( P \) in hand the definition is the one Chapters 2 and 3 used for \( \nZ \) and \( \nQ \).

::: {#def-reals-order}
[Order on the Reals]

For \( x, y \in \nR \), \( x < y \) means \( y - x \in P \). As usual, \( x \le y \) means \( x < y \) or \( x = y \), and \( y > x \) means \( x < y \).
:::

In terms of representatives: \( [a] < [b] \) exactly when \( b - a \) is positive, that is, when \( b_n - a_n \ge \delta \) from some index on, for some margin \( \delta \in \nQ_{>0} \). The terms of \( b \) must eventually overtake those of \( a \) by a fixed rational amount. Since \( 0_{\nR} - x = -x \) and \( x - 0_{\nR} = x \), we have \( x > 0_{\nR} \) if and only if \( x \in P \), and \( x < 0_{\nR} \) if and only if \( -x \in P \).

::: {#thm-reals-ordered-field}
[The Reals Form an Ordered Field]

With the operations of @def-reals-operations and the order of @def-reals-order, \( \nR \) is an ordered field (@def-ordered-ring-and-field), and its positive elements are exactly the elements of \( P \).
:::

::: {.idea}
Each order axiom is a statement about one difference, and @thm-reals-positive-cone is exactly what @prp-order-from-positives asks for. (O1) is (i) applied to \( y - x \), since \( -(y - x) = x - y \). (O2) is closure under sums, since \( (z - y) + (y - x) = z - x \). (O3) holds because \( (y + z) - (x + z) = y - x \). (O4) is closure under products.
:::

::: {.proof}
By @thm-reals-field, \( \nR \) is a field, in particular a commutative ring (@def-commutative-ring-and-field). By @thm-reals-positive-cone, the subset \( P \subseteq \nR \) satisfies clause (P1) of @prp-order-from-positives (part (ii)) and clause (P2) (part (i)). That proposition then says that the relation "\( y - x \in P \)", which is \( x < y \) of @def-reals-order, makes \( \nR \) an ordered commutative ring with \( P = \{ x \in \nR : x > 0_{\nR} \} \). An ordered commutative ring that is a field is an ordered field (@def-ordered-ring-and-field).
:::

So \( \nR \) is an ordered field, and every result that Chapters 2 and 4 proved for an arbitrary ordered field holds in it. We write \( \nR_{>0} \coloneqq \{ x \in \nR : x > 0_{\nR} \} \), the set \( F_{>0} \) of Chapter 4 for \( F = \nR \); by the theorem, \( \nR_{>0} = P \). The rules for inequalities (@prp-ordered-ring-rules), the rules for halves (@prp-ordered-field-halves), the absolute value (@def-absolute-value-ordered-field, @prp-absolute-value-ordered-field), and limits, null sequences and Cauchy sequences with tolerances in \( \nR_{>0} \) (@def-sequence-limit-ordered-field, @def-cauchy-sequence-ordered-field) are now available in \( \nR \). From here on they may be applied with \( F = \nR \). It pays to name the field at each such use, so that a tolerance in \( \nQ_{>0} \) is never confused with one in \( \nR_{>0} \).

One consequence deserves a line. In any ordered field, \( x \le y \) holds if and only if \( y < x \) fails: by (O1), exactly one of \( x < y \), \( x = y \), \( y < x \) holds.

## Comparing classes through their terms

The order is defined through margins, but in practice we usually know a termwise inequality and want an inequality between classes. The next lemma is the bridge, and the example at the start of the section shows its limit.

::: {#lem-termwise-order}
[Termwise Inequalities Pass to Classes]

Let \( a, b \in \sC \) and \( N_0 \in \nN \). If \( a_n \le b_n \) for every \( n \ge N_0 \), then \( [a] \le [b] \).
:::

::: {.idea}
Suppose instead that \( [b] < [a] \). Then \( a - b \) is positive, so from some index on \( a_n \) exceeds \( b_n \) by a fixed margin; one index beyond both thresholds then contradicts \( a_n \le b_n \). By trichotomy, "not \( [b] < [a] \)" is "\( [a] \le [b] \)".
:::

::: {.proof}
Suppose that \( [b] < [a] \). By @def-reals-order, \( [a] - [b] = [a - b] \in P \), so \( a - b \) is positive, since every representative of an element of \( P \) is (@prp-positivity-well-defined). Fix \( \delta \in \nQ_{>0} \) and \( N \in \nN \) with \( a_n - b_n \ge \delta \) for every \( n \ge N \) \( [\rulename{\exists E}] \). Let \( n \coloneqq \max\{N, N_0\} \). Then \( a_n - b_n \ge \delta > 0 \). But \( n \ge N_0 \), so \( a_n \le b_n \), that is, \( a_n - b_n \le 0 \) (@prp-ordered-ring-rules (a)). These contradict (O1) in \( \nQ \). Hence \( [b] < [a] \) is false, by \( \rulename{\neg I} \) (@fd1:def-rules-negation). By (O1) in the ordered field \( \nR \) (@thm-reals-ordered-field), \( [a] < [b] \) or \( [a] = [b] \); that is, \( [a] \le [b] \).
:::

The proof opens its box with "\( [b] < [a] \)" and closes it with the negation of that statement, which is \( \rulename{\neg I} \). It is not reductio ad absurdum (@fd1:def-rule-raa), whose box opens with the negation of the goal. The step from "\( [b] < [a] \) is false" to "\( [a] \le [b] \)" is trichotomy in \( \nR \), a property of this particular order, not a rule of logic.

::: {.warning}
The strict version of the lemma is **false**. In @exm-strict-termwise-order-fails, \( a_n = 0 < 1/(n + 1) = b_n \) for **every** \( n \), and yet \( [a] = [b] \), so \( [a] < [b] \) fails. A strict termwise inequality passes to classes only as \( \le \). To get \( < \) between classes, show that the difference is eventually above a fixed margin.
:::

Most uses of the lemma compare a class with a constant: if \( a_n \le q \) for every \( n \ge N_0 \), then \( [a] \le [(q)_n] \); and if \( a_n \ge q \) for every \( n \ge N_0 \), then \( [a] \ge [(q)_n] \).

::: {.check}
Let \( a_n \coloneqq 1/(n + 1) - 1/(n + 1)^2 \). Every term satisfies \( a_n \ge 0 \). Is \( a \) positive?
:::

::: {.solution}
No. Here \( a_n = n/(n + 1)^2 \), so \( 0 \le a_n \le 1/(n + 1) \) for every \( n \) (as \( n \le n + 1 \)). The lower sequence \( (0)_n \) and the upper sequence \( (1/(n + 1)) \) are null, so \( a \) is null by the squeeze, @prp-limit-preserves-order-ordered-field (c) with \( F = \nQ \); being null, \( a \in \sC \) (@thm-cauchy-algebra-ordered-field (a)). Then \( [a] = 0_{\nR} \), as in the proof of @thm-reals-positive-cone (i), and \( 0_{\nR} \notin P \) by the same part. So \( a \) is not positive, although no term is negative. @lem-termwise-order gives only \( [a] \ge 0_{\nR} \), which is true.
:::

## The absolute value through representatives

Since \( \nR \) is an ordered field, every real number \( x \) has an absolute value \( \abs{x} \), by @def-absolute-value-ordered-field with \( F = \nR \): \( x \) if \( x \ge 0_{\nR} \), and \( -x \) if \( x < 0_{\nR} \). The proofs of the next section estimate \( \abs{[a] - [b]} \), and for that we want to compute an absolute value on representatives, the way sums and products are computed.

::: {#prp-reals-absolute-value-termwise}
[The Absolute Value Is Computed Termwise]

Let \( a \in \sC \). Then \( (\abs{a_n})_n \in \sC \), and
\[
\abs{[a]} = [(\abs{a_n})_n] ,
\]
where the left side is the absolute value in the ordered field \( \nR \) and \( \abs{a_n} \) is the absolute value in \( \nQ \).
:::

::: {.idea}
The reverse triangle inequality makes \( (\abs{a_n}) \) Cauchy with the same thresholds as \( a \). For the equality, sort \( a \) by @thm-cauchy-not-null-sign: null, eventually positive by a margin, or eventually negative by a margin. In each case \( (\abs{a_n}) \) agrees from some index on with \( a \), with \( -a \), or is null, and that settles which of \( [a] \), \( -[a] \), \( 0_{\nR} \) it represents.
:::

::: {.proof}
*Membership.* Let \( \varepsilon \in \nQ_{>0} \), and choose \( N \) with \( \abs{a_m - a_n} < \varepsilon \) for all \( m, n \ge N \). By the reverse triangle inequality in \( \nQ \) (@prp-absolute-value-ordered-field (f)), \( \bigl| \abs{a_m} - \abs{a_n} \bigr| \le \abs{a_m - a_n} < \varepsilon \) for the same \( m, n \). So \( (\abs{a_n}) \in \sC \), with the same thresholds as \( a \).

*Equality.* We use three facts. A class \( [b] \) with \( b \) eventually equal to \( b' \) equals \( [b'] \) (@exm-finite-change-equivalent). A null sequence represents \( 0_{\nR} \) (proof of @thm-reals-positive-cone (i)). And, in the ordered field \( \nR \), \( \abs{x} = x \) for \( x > 0_{\nR} \), \( \abs{x} = -x \) for \( x < 0_{\nR} \), and \( \abs{0_{\nR}} = 0_{\nR} \) (@def-absolute-value-ordered-field).

*Case 1: \( a \) is null.* Then \( [a] = 0_{\nR} \), so \( \abs{[a]} = 0_{\nR} \). The sequence \( (\abs{a_n}) \) is null too, since \( \bigl| \abs{a_n} - 0 \bigr| = \abs{a_n} = \abs{a_n - 0} \) (@prp-absolute-value-ordered-field (a) and @def-absolute-value-ordered-field), so the two sequences pass the same tests of @def-null-sequence-ordered-field. Hence \( [(\abs{a_n})_n] = 0_{\nR} = \abs{[a]} \).

*Case 2: \( a \) is not null.* By @thm-cauchy-not-null-sign with \( F = \nQ \), fix \( c \in \nQ_{>0} \) and \( N \in \nN \) with \( a_n \ge c \) for every \( n \ge N \), or with \( a_n \le -c \) for every \( n \ge N \) \( [\rulename{\exists E}] \).

If \( a_n \ge c \) for \( n \ge N \), then \( a \) is positive, so \( [a] \in P \) and \( [a] > 0_{\nR} \), whence \( \abs{[a]} = [a] \). For \( n \ge N \), \( a_n > 0 \), so \( \abs{a_n} = a_n \). The sequences \( (\abs{a_n}) \) and \( a \) agree from \( N \) on, so \( [(\abs{a_n})_n] = [a] = \abs{[a]} \).

If \( a_n \le -c \) for \( n \ge N \), then \( -a \) is positive, so \( -[a] = [-a] \in P \) and \( [a] < 0_{\nR} \), whence \( \abs{[a]} = -[a] = [-a] \). For \( n \ge N \), \( a_n < 0 \), so \( \abs{a_n} = -a_n \). The sequences \( (\abs{a_n}) \) and \( -a \) agree from \( N \) on, so \( [(\abs{a_n})_n] = [-a] = \abs{[a]} \).
:::

The proposition does **not** say that \( \abs{a_n} = a_n \) or \( -a_n \) for all \( n \); a representative of a positive number may have negative terms early on, as the late-positivity example shows. It says that the class of \( (\abs{a_n}) \) is the right one, and classes do not see early terms. Section 5.4 uses the proposition to estimate the distance from a real number \( [a] \) to the rational numbers \( a_k \), a term at a time.

## Exercises

### A. Check your understanding

::: {#exr-ordering-the-reals-a1}
[A1]

In parts (a)–(d), decide for each sequence whether it is in \( \sC \) and whether it is positive; when it is positive, give a margin \( \delta \) and a threshold \( N \).

::: {.enumerate options="label=(\alph*)"}
1. \( a_n = 1 - 1/(n + 1) \).
2. \( a_n = 1/(n + 1) \).
3. \( a_k = d_k - 1 \), where \( (d_k) \) is the sequence of decimal truncations of @exm-truncations-equivalent.
4. \( a_n = (-1)^n \).
5. Show from @def-reals-order and @def-positive-cauchy-sequence that \( 1_{\nR} > 0_{\nR} \). Which result of Chapter 2 gives the same conclusion in every ordered field?
:::
:::

::: {.solution}
(a) In \( \sC \) (a constant minus a null sequence, @thm-cauchy-algebra-ordered-field (a), (b)), and positive. For \( n \ge 1 \), \( n + 1 \ge 2 \), so \( 1/(n + 1) \le 1/2 \) (@prp-ordered-field-halves (c)) and \( a_n \ge 1/2 \). So \( \delta = 1/2 \), \( N = 1 \) work. (\( N = 0 \) fails for this \( \delta \): \( a_0 = 0 \).)

(b) In \( \sC \), being null, and not positive: this is the non-example after @def-positive-cauchy-sequence.

(c) In \( \sC \), as the difference of \( (d_k) \in \sC \) (@exm-truncations-equivalent) and a constant, and positive. The first truncations are \( d_0 = 1 \) and \( d_1 = 7/5 \) (\( 14 \) is the largest natural number whose square is at most \( 2 \cdot 10^2 = 200 \)), and \( (d_k) \) is non-decreasing (@exm-truncations-equivalent). So \( d_k \ge d_1 = 7/5 \) for every \( k \ge 1 \), and \( a_k \ge 2/5 \). So \( \delta = 2/5 \), \( N = 1 \) work. (\( N = 0 \) fails for every \( \delta > 0 \): \( a_0 = 0 \).)

(d) Not in \( \sC \): for every \( N \), the indices \( N \) and \( N + 1 \) give terms differing by \( 2 \), so the tolerance \( 1 \) has no threshold. The question "positive?" does not arise; the definition applies only to members of \( \sC \).

(e) \( 1_{\nR} - 0_{\nR} = [(1)_n - (0)_n] = [(1)_n] \), and \( (1)_n \) is positive with \( \delta = 1 \), \( N = 0 \). So \( 1_{\nR} - 0_{\nR} \in P \), that is, \( 0_{\nR} < 1_{\nR} \). In every ordered commutative ring with \( 1 \ne 0 \), @prp-ordered-ring-rules (e) gives \( 1 > 0 \); for \( \nR \), \( 1_{\nR} \ne 0_{\nR} \) holds by @thm-reals-commutative-ring.
:::

### B. Practice

::: {#exr-ordering-the-reals-b1}
[B1]

Prove part (ii) of @thm-reals-positive-cone directly from @def-positive-cauchy-sequence, naming the rule behind each step. Then take \( a_n = 1 - 1/(n + 1) \) and \( b_n = x_n - 1 \), with \( (x_n) \) the Newton sequence of @exm-newton-rationals-sqrt2, find margins and thresholds for \( a \) and \( b \), and state the margins and threshold that your proof produces for \( a + b \) and for \( ab \).

*Hint: for \( b \), compare \( x_n \) with \( 7/5 \) by squaring.*
:::

::: {.solution}
*The proof.* Let \( x, y \in P \). Choose representatives \( x = [a] \) and \( y = [b] \); they are positive, since every representative of an element of \( P \) is (@prp-positivity-well-defined). By @def-positive-cauchy-sequence, fix \( \delta_a \in \nQ_{>0} \), \( N_a \in \nN \) with \( a_n \ge \delta_a \) for every \( n \ge N_a \), and \( \delta_b \in \nQ_{>0} \), \( N_b \in \nN \) with \( b_n \ge \delta_b \) for every \( n \ge N_b \). Let \( N \coloneqq \max\{N_a, N_b\} \), and let \( n \ge N \); then \( n \ge N_a \) and \( n \ge N_b \).

*Sum.* Adding \( a_n \ge \delta_a \) and \( b_n \ge \delta_b \) gives \( a_n + b_n \ge \delta_a + \delta_b \) (@prp-ordered-ring-rules (b)), and adding \( \delta_a > 0 \) and \( \delta_b > 0 \) gives \( \delta_a + \delta_b > 0 \) (the same rule, strict form). So \( a + b \) is positive with margin \( \delta_a + \delta_b \) and threshold \( N \).

*Product.* From \( 0 \le \delta_a \le a_n \) and \( 0 \le \delta_b \le b_n \), @prp-ordered-field-halves (d) gives \( \delta_a \delta_b \le a_n b_n \), and \( \delta_a \delta_b > 0 \) by (O4). So \( ab \) is positive with margin \( \delta_a \delta_b \) and threshold \( N \).

By @def-reals-operations, \( x + y = [a + b] \) and \( xy = [ab] \), so both lie in \( P \).

*The example.* For \( a \), Exercise A1 (a) gives \( \delta_a = 1/2 \), \( N_a = 1 \). For \( b \): \( x_n > 0 \) and \( x_n^2 > 2 \) for every \( n \) (@exm-newton-rationals-sqrt2), while \( (7/5)^2 = 49/25 < 2 \). Both \( 7/5 \) and \( x_n \) are \( \ge 0 \), so @prp-ordered-ring-rules (g) turns \( (7/5)^2 < x_n^2 \) into \( 7/5 < x_n \). Hence \( b_n = x_n - 1 > 2/5 \) for every \( n \), and \( \delta_b = 2/5 \), \( N_b = 0 \) work. The proof then gives the threshold \( N = \max\{1, 0\} = 1 \), the margin \( 1/2 + 2/5 = 9/10 \) for \( a + b \), and the margin \( (1/2)(2/5) = 1/5 \) for \( ab \).
:::

::: {#exr-ordering-the-reals-b2}
[B2]

Let \( a, b \in \sC \). Prove that \( [a] < [b] \) if and only if there are \( \delta \in \nQ_{>0} \) and \( N \in \nN \) with \( b_n - a_n \ge \delta \) for every \( n \ge N \).
:::

::: {.solution}
By @def-reals-order, \( [a] < [b] \) means \( [b] - [a] \in P \). By @def-reals-operations, \( [b] - [a] = [b - a] \), where \( b - a \in \sC \) is the termwise difference (@thm-cauchy-algebra-ordered-field (b)). An element of \( \nR \) lies in \( P \) if and only if one (equivalently, every) representative of it is positive, by the definition of \( P \) and @prp-positivity-well-defined. So \( [a] < [b] \) holds if and only if \( b - a \) is positive, which, by @def-positive-cauchy-sequence, is the condition stated, since the \( n \)-th term of \( b - a \) is \( b_n - a_n \).
:::

::: {#exr-ordering-the-reals-b3}
[B3]

::: {.enumerate options="label=(\alph*)"}
1. Let \( a \in \sC \) with \( 0 \le a_n \le 1 \) for every \( n \in \nN \). Prove that \( 0_{\nR} \le [a] \le 1_{\nR} \).
2. Give an example of \( a \in \sC \) with \( 0 < a_n < 1 \) for every \( n \) and \( [a] = 1_{\nR} \). What does your example show about part (a)?
:::
:::

::: {.solution}
(a) The constant sequences \( (0)_n \) and \( (1)_n \) are in \( \sC \) (@thm-cauchy-algebra-ordered-field (a)). By @lem-termwise-order with \( N_0 = 0 \), \( (0)_n \le a \) termwise gives \( 0_{\nR} = [(0)_n] \le [a] \), and \( a \le (1)_n \) termwise gives \( [a] \le [(1)_n] = 1_{\nR} \).

(b) Let \( a_n \coloneqq 1 - 1/(n + 2) \). For every \( n \), \( n + 2 \ge 2 > 1 \), so \( 0 < 1/(n + 2) < 1 \) (@prp-reciprocal-order (b)), and \( 0 < a_n < 1 \). The sequence \( a - (1)_n = (-1/(n + 2)) \) is null: \( (1/(n + 2)) \) is the shift by one of the null sequence \( (1/(n + 1)) \) (@prp-tail-change-ordered-field (b)), and the negative of a null sequence is null (@thm-limit-laws-ordered-field (b)). So \( a = (1)_n + (-1/(n + 2))_n \) is in \( \sC \), as the sum of a constant and a null sequence (@thm-cauchy-algebra-ordered-field (a), (b)). Since \( a - (1)_n \) is null, \( a \sim (1)_n \) and \( [a] = 1_{\nR} \). The example shows that part (a) cannot be sharpened to strict inequalities: \( a_n < 1 \) for every \( n \), and still \( [a] = 1_{\nR} \). This is the warning after @lem-termwise-order once more. (Any \( a \) with \( 0 < a_n < 1 \) for all \( n \) and \( 1 - a_n \) null is a correct answer.)
:::

### C. Going deeper

::: {#exr-ordering-the-reals-c1}
[C1]

Show that the rule \( [a] \mapsto [(\abs{a_n})_n] \) is a well-defined function \( \nR \to \nR \), directly from the definitions and without using @prp-reals-absolute-value-termwise.

Here is the beginning of a proof. *Name the move, then complete it.*

"Let \( a, a' \in \sC \) with \( a \sim a' \). The sequences \( (\abs{a_n}) \) and \( (\abs{a'_n}) \) are in \( \sC \), by the reverse triangle inequality @prp-absolute-value-ordered-field (f), as in the membership part of @prp-reals-absolute-value-termwise. …"
:::

::: {.solution}
*The move* is **representatives, then independence**: the rule is defined on a representative, so we must show that replacing \( a \) by an equivalent \( a' \) gives the same output class. Then each class has exactly one output, and the rule is a function (@fd2:def-function).

*Completion.* Let \( e_n \coloneqq \abs{a_n} - \abs{a'_n} \). By the reverse triangle inequality in \( \nQ \) (@prp-absolute-value-ordered-field (f)),
\[
0 \le \abs{e_n} \le \abs{a_n - a'_n} \quad \text{for every } n \in \nN .
\]
The sequence \( (a_n - a'_n) \) is null, since \( a \sim a' \) (@def-cauchy-equivalent); so is \( (\abs{a_n - a'_n}) \), because \( \bigl| \abs{a_n - a'_n} - 0 \bigr| = \abs{a_n - a'_n - 0} \) and the two sequences pass the same tests of @def-null-sequence-ordered-field. The squeeze @prp-limit-preserves-order-ordered-field (c) in \( \nQ \), with lower sequence \( (0)_n \) and upper sequence \( (\abs{a_n - a'_n}) \), shows that \( (\abs{e_n}) \) is null. Then \( (e_n) \) is null, for the same reason as before: \( \abs{e_n - 0} = \bigl| \abs{e_n} - 0 \bigr| \). So \( (\abs{a_n}) \sim (\abs{a'_n}) \), and \( [(\abs{a_n})_n] = [(\abs{a'_n})_n] \) (@fd2:thm-classes-partition (b)).

So the output depends only on the class \( [a] \), and the rule defines a function \( \nR \to \nR \). (By @prp-reals-absolute-value-termwise, this function is \( x \mapsto \abs{x} \); the direct proof above does not need that.)

**Marking scheme.** (10 points)
- 2: names the move (representatives, then independence) and states the goal \( (\abs{a_n}) \sim (\abs{a'_n}) \).
- 3: proves \( \bigl| \abs{a_n} - \abs{a'_n} \bigr| \le \abs{a_n - a'_n} \) for every \( n \), citing the reverse triangle inequality in \( \nQ \).
- 3: from \( a \sim a' \) and the inequality of the previous step, shows that \( (\abs{a_n} - \abs{a'_n})_n \) is null.
- 2: concludes \( [(\abs{a_n})_n] = [(\abs{a'_n})_n] \), so each class has one output and the rule is a function \( \nR \to \nR \).

A direct \( \varepsilon \)–\( N \) proof of the third step, with no squeeze, earns its 3 points: given \( \varepsilon \in \nQ_{>0} \), take \( N \) for the null sequence \( (a_n - a'_n) \); then \( \bigl| \abs{a_n} - \abs{a'_n} \bigr| \le \abs{a_n - a'_n} < \varepsilon \) for every \( n \ge N \). Fatal errors (0 for the step): using \( \abs{x} \) on \( \nR \), or citing @prp-reals-absolute-value-termwise; proving only that the two output sequences are Cauchy, without proving them equivalent.
:::

::: {#exr-ordering-the-reals-c2}
[C2: Find the error]

Here is an argument for @prp-positivity-well-defined.

"Let \( a \) be positive and \( a' \sim a \). Fix \( \delta \in \nQ_{>0} \) and \( N \) with \( a_n \ge \delta \) for every \( n \ge N \). Since \( a' - a \) is null, there is \( N' \) with \( \abs{a'_n - a_n} < \delta \) for every \( n \ge N' \). So, for \( n \ge \max\{N, N'\} \), \( a'_n > a_n - \delta \ge 0 \). Hence \( a'_n > 0 \) for all large \( n \). Therefore \( a' \) is positive."

Is the conclusion true? Does the argument prove it? If not, name the line that fails, say why, give a counterexample to that step, and repair the argument.
:::

::: {.solution}
[Hint 1]

Write out in symbols what "\( a' \) is positive" requires, and compare it with what the argument has when it reaches the last line.
:::

::: {.solution}
[Hint 2]

"Positive" asks for one margin \( \delta' \in \nQ_{>0} \), chosen before \( n \), with \( a'_n \ge \delta' \) for all large \( n \). Find the line where the argument should produce such a \( \delta' \), and ask what it produces instead.
:::

::: {.solution}
*The conclusion is true:* it is @prp-positivity-well-defined.

*The middle lines are correct.* With the tolerance \( \delta \) and the strict inequality \( \abs{a'_n - a_n} < \delta \), we get \( a'_n > a_n - \delta \ge \delta - \delta = 0 \) for every \( n \ge \max\{N, N'\} \). So the line "\( a'_n > 0 \) for all large \( n \)" is proved.

*The failing line* is the last: "Therefore \( a' \) is positive." What has been proved is
\[
\exists N \in \nN \ \ \forall n \ge N \ \ a'_n > 0 ,
\]
while "positive" (@def-positive-cauchy-sequence) is
\[
\exists \delta \in \nQ_{>0} \ \ \exists N \in \nN \ \ \forall n \ge N \ \ a'_n \ge \delta .
\]
To pass from the first to the second, one would take the margin \( \delta \coloneqq a'_n \), which depends on \( n \), and then claim one margin for all \( n \). That swaps a "for every \( n \), there is a margin" for a "there is a margin for every \( n \)". It is the analogue, for a margin depending on \( n \), of entry (N2) of @fd1:exm-not-allowed-catalogue, where a threshold depending on \( \varepsilon \) is treated as uniform.

*Counterexample to the step.* The sequence \( (1/(n + 1)) \) has \( a'_n > 0 \) for all \( n \), so it satisfies the premise of the last line, and it is not positive (the non-example after @def-positive-cauchy-sequence). So "eventually \( > 0 \)" does not imply "positive". The argument reached a true conclusion through a step that is not valid.

*Repair.* Use the tolerance \( \delta/2 \in \nQ_{>0} \) (@prp-ordered-field-halves (b)) instead of \( \delta \). Since \( a' - a \) is null, choose \( N'' \) with \( \abs{a'_n - a_n} < \delta/2 \) for every \( n \ge N'' \). For \( n \ge \max\{N, N''\} \),
\[
a'_n > a_n - \frac{\delta}{2} \ge \delta - \frac{\delta}{2} = \frac{\delta}{2} .
\]
So \( a'_n \ge \delta/2 \) for every \( n \ge \max\{N, N''\} \): one margin, \( \delta/2 \), fixed before \( n \), and \( a' \) is positive. This is the proof of @prp-sign-stable-ordered-field.

**Marking scheme.** (10 points)
- 2: says the conclusion is true, citing @prp-positivity-well-defined.
- 3: identifies the last line as the failing one and names the quantifier swap (a margin depending on \( n \) treated as one margin for all \( n \)).
- 2: a counterexample to the step: a sequence whose terms are eventually \( > 0 \) and which is not positive, such as \( (1/(n + 1)) \).
- 3: a repair that produces one margin in \( \nQ_{>0} \) fixed before \( n \) (for instance the tolerance \( \delta/2 \) above; any tolerance strictly between \( 0 \) and \( \delta \) works equally well).
Fatal errors (0 for the step): blaming one of the valid middle lines; a "counterexample" to the conclusion; a repair whose margin still depends on \( n \).
:::

<!-- dependency ledger
lem-termwise-order (proof): [a] - [b] = [a - b], since a + (-b) = a - b termwise | def-reals-operations, cited; termwise field arithmetic in Q
exm-strict-termwise-order-fails (solution): (1/(n + 1)) is null in Q | exm-first-sequences-ordered-field (b), cited
exm-strict-termwise-order-fails (solution): trichotomy excludes 0 < 0 in an ordered field | def-ordered-ring-and-field (O1), cited by name
def-positive-cauchy-sequence (example): 1 - 2/(n + 1) >= 1/2 for n >= 3; first terms -1, 0, 1/3, 1/2 | prp-ordered-field-halves (c), (d), cited; verify/ch05/def-positive-cauchy-sequence.py
def-positive-cauchy-sequence (example): x_n > 1 for every n | thm-sqrt2-cauchy-no-rational-limit (statement), cited
def-positive-cauchy-sequence (claim): negation of the definition | fd1:prp-bounded-quantifier-negation, fd1:prp-negated-implication, cited; not(a_n >= delta) iff a_n < delta by (O1)
def-positive-cauchy-sequence (claim): a_n >= delta gives a_n > delta/2 | prp-ordered-field-halves (b); inline
prp-positivity-well-defined (claim): x in P iff every representative of x is positive | fd2:thm-classes-partition (a), fd2:def-equivalence-class, cited; inline
thm-reals-positive-cone (proof): a null sequence a satisfies a ~ (0)_n, so [a] = 0_R | def-cauchy-equivalent, a_n - 0 = a_n; inline
thm-reals-positive-cone (proof): -(0)_n = (0)_n | -0 = 0 in Q; inline
thm-reals-positive-cone (proof): max{N, N'} exists in N and is >= N and >= N' | thm-omega-order (a)
def-reals-order (claim): x > 0_R iff x in P; x < 0_R iff -x in P | 0 - x = -x, x - 0 = x in the ring R; inline
thm-reals-ordered-field (idea): -(y - x) = x - y, (z - y) + (y - x) = z - x, (y + z) - (x + z) = y - x | prp-order-from-positives (its proof records them), cited
thm-reals-ordered-field (claim): x <= y iff not y < x | (O1); inline
lem-termwise-order (claim): check after the lemma: 1/(n + 1) - 1/(n + 1)^2 = n/(n + 1)^2 and 0 <= n/(n + 1)^2 <= 1/(n + 1) (multiply 0 <= n <= n + 1 by 1/(n + 1)^2 > 0) | field arithmetic in Q; prp-ordered-field-halves (d), prp-reciprocal-order; inline
lem-termwise-order (claim): if a_n <= q eventually then [a] <= [(q)_n] | lem-termwise-order with b constant; constants in C by thm-cauchy-algebra-ordered-field (a)
prp-reals-absolute-value-termwise (proof): ||a_n| - 0| = |a_n| = |a_n - 0| | prp-absolute-value-ordered-field (a) (|y| >= 0) and def-absolute-value-ordered-field (|y| = y for y >= 0); inline
prp-reals-absolute-value-termwise (proof): a_n >= c > 0 gives |a_n| = a_n; a_n <= -c < 0 gives |a_n| = -a_n | def-absolute-value-ordered-field, cited
exr-ordering-the-reals-a1 (solution): d_0 = 1, d_1 = 7/5 (14^2 = 196 <= 200 < 225); (d_k) non-decreasing | exm-truncations-equivalent, cited; verify/ch05/exr-ordering-the-reals-a1.py
exr-ordering-the-reals-a1 (solution): ((-1)^n) not Cauchy: indices N, N + 1 give terms differing by 2 | inline
exr-ordering-the-reals-b1 (solution): (7/5)^2 = 49/25 < 2; margins 9/10 and 1/5, threshold 1 | prp-ordered-ring-rules (g), cited; verify/ch05/exr-ordering-the-reals-b1.py
exr-ordering-the-reals-b3 (solution): 0 < 1/(n + 2) < 1 | prp-reciprocal-order (b), cited; verify/ch05/exr-ordering-the-reals-b3.py
exr-ordering-the-reals-c1 (solution): (|e_n|) null iff (e_n) null | def-null-sequence-ordered-field with ||e_n| - 0| = |e_n - 0|; inline
exr-ordering-the-reals-c2 (solution): catalogue entry (N2) | fd1:exm-not-allowed-catalogue, cited
-->
