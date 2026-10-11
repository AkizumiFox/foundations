# The Natural Numbers and Well-Ordering

Chapter 3 took one fact about the natural numbers on trust: the principle of induction (@ax-induction), which says that a property holding at \( 0 \) and passing from each \( n \) to \( n + 1 \) holds for every \( n \in \nN \). From it, Chapter 3 proved strong induction (@thm-strong-induction), whose step may use the property at **every** smaller number. Everything else we have said about \( \nN \) was school knowledge: that \( 7 - 3 \) is a natural number, that none lies strictly between \( 3 \) and \( 4 \), that every non-empty set of natural numbers has a least member. This section derives those facts from induction, extends them to the integers, and then proves that the least-member property, **well-ordering**, is induction in another form.

## What we assume about the natural numbers

The principle of induction is usually used with a property written as a sentence. It has an equivalent form about sets, which is the one Chapter 11 uses.

::: {.remark}
Let \( S \subseteq \nN \) contain \( 0 \), and suppose \( n + 1 \in S \) whenever \( n \in S \). Apply @ax-induction to the property "\( n \in S \)": its base case is \( 0 \in S \), and its step is the closure of \( S \). So every \( n \in \nN \) lies in \( S \), that is, \( \nN \subseteq S \), and with \( S \subseteq \nN \) this gives \( S = \nN \) (@prp-subset-antisymmetric). In words: the only subset of \( \nN \) that contains \( 0 \) and is closed under \( n \mapsto n + 1 \) is \( \nN \) itself. Chapter 11 states this as "\( \nN \) is contained in every inductive set", where an inductive set contains \( 0 \), as here.
:::

Here is everything the section assumes about \( \nN \). The natural numbers form a subset \( \nN \subseteq \nR \) of the familiar real numbers such that

- (\( \nN \)0) \( 0 \in \nN \);
- (\( \nN \)S) for every \( n \in \nN \), also \( n + 1 \in \nN \);

and @ax-induction holds. The arithmetic and the order of the real numbers (the laws of \( + \), \( - \), \( \cdot \) and \( \le \), trichotomy, multiplying an inequality by a positive number) are school facts in Part 0; Chapter 11 states them as axioms of an ordered field. These three items are a description of \( \nN \), not new axioms: Chapter 3 already used all of them.

**The rule for this section.** From here to the end of the section, a fact about \( \nN \) is used only if it is (\( \nN \)0), (\( \nN \)S), @ax-induction, a statement proved earlier in the section, or @thm-strong-induction once the paragraph after @lem-naturals-arithmetic has shown that its Chapter 3 proof rests only on these. The real-number arithmetic is used freely. In particular "\( n \ge 0 \)" for a natural number \( n \), which looks too obvious to mention, is not available until it is proved below, in @lem-naturals-arithmetic (a).

The integers and the rationals are then **defined** from \( \nN \), as subsets of \( \nR \):
\[
\begin{aligned}
\nZ &\coloneqq \nN \cup \{ -n : n \in \nN \} , \\
\nZ_{>0} &\coloneqq \{ n \in \nN : n \ne 0 \} , \\
\nQ &\coloneqq \{ m/n : m \in \nZ, \ n \in \nZ_{>0} \} .
\end{aligned}
\]
In words: an integer is a natural number or the negative of one; a positive integer is a natural number other than \( 0 \); a rational number is a quotient of an integer by a positive integer. These are word for word the definitions of Chapter 11's Section 11.5, so the two chapters speak of the same sets. Examples: \( -3 \in \nZ \) because \( 3 \in \nN \); \( 0 \) lies in \( \nZ \) twice over, as \( 0 \in \nN \) and as \( -0 \), which a union does not mind; \( -\tfrac12 = (-1)/2 \in \nQ \). The definitions do not yet tell us that \( \tfrac12 \notin \nZ \), or that \( \nZ_{>0} \) is the set of natural numbers \( \ge 1 \). Both need the lemma below.

Two pieces of notation will save words later. For \( n \in \nN \),
\[
\{1, \dots, n\} \coloneqq \{ k \in \nN : 1 \le k \le n \} , \qquad \{0, \dots, n\} \coloneqq \{ k \in \nN : k \le n \} .
\]
So \( \{1, \dots, 0\} = \emptyset \), since no \( k \) has \( 1 \le k \le 0 \). We do not write \( [n] \) for these sets: square brackets will mean an equivalence class in Section 7.5.

## The arithmetic of the natural numbers

The facts below are the ones Chapter 3 and Chapter 11 used without proof. Each of (a)–(d) is one ordinary induction, and the only work is to choose the property to induct on; (e) follows from (a) and (d).

::: {#lem-naturals-arithmetic}
[Arithmetic of the Natural Numbers]

For all \( m, n \in \nN \):

::: {.enumerate options="label=(\alph*)"}
1. \( n \ge 0 \); and if \( n \ne 0 \), then \( n \ge 1 \);
2. \( m + n \in \nN \) and \( mn \in \nN \);
3. if \( n \ne 0 \) (equivalently, by (a), \( n \ge 1 \)), then \( n - 1 \in \nN \);
4. if \( m \le n \), then \( n - m \in \nN \);
5. there is **no** \( k \in \nN \) with \( n < k < n + 1 \); equivalently, if \( m < n \), then \( m + 1 \le n \).
:::
:::

In words: (a) says that \( 0 \) is the smallest natural number and that nothing in \( \nN \) lies between \( 0 \) and \( 1 \). (b) says \( \nN \) is closed under sums and products, (c) that every natural number except \( 0 \) has a predecessor in \( \nN \), and (d) that a difference "larger minus smaller" stays in \( \nN \). (e) says the natural numbers come one unit apart, with no gaps to hide in.

::: {.idea}
Each induction needs a property that is true at \( 0 \) and survives the step, and the statement as written does not always qualify. "If \( n \ne 0 \), then \( n \ge 1 \)" says nothing useful at \( 0 \), so for (a) we induct on the disjunction "\( n = 0 \) or \( n \ge 1 \)". For (b) we fix one of the two numbers and induct on the other. For (d) we induct on \( m \). The step from \( m \) to \( m + 1 \) uses the hypothesis only at the same \( n \), with the weaker bound \( m \le n \), and then subtracts \( 1 \) using (c). So \( n \) could be fixed first, as \( m \) is in (b); the proof below puts "for every \( n \)" inside the property instead, which is harmless.
:::

::: {.proof}
*(a)* Let \( P(n) \) be "\( n = 0 \) or \( n \ge 1 \)". *Base case:* \( P(0) \) holds by its first disjunct. *Step:* let \( n \in \nN \) with \( P(n) \). If \( n = 0 \), then \( n + 1 = 1 \ge 1 \); if \( n \ge 1 \), then \( n + 1 \ge 2 \ge 1 \). In both cases \( n + 1 \ge 1 \), so \( P(n + 1) \) holds by its second disjunct. By @ax-induction, every \( n \in \nN \) satisfies \( n = 0 \) or \( n \ge 1 \). In both cases \( n \ge 0 \); and if \( n \ne 0 \), the first disjunct is excluded, so \( n \ge 1 \).

*(b)* Fix \( m \in \nN \). *Sums:* let \( P(n) \) be "\( m + n \in \nN \)". Then \( P(0) \) holds, since \( m + 0 = m \in \nN \). If \( m + n \in \nN \), then \( m + (n + 1) = (m + n) + 1 \in \nN \) by (\( \nN \)S). By @ax-induction, \( m + n \in \nN \) for every \( n \in \nN \); as \( m \) was arbitrary, this holds for all \( m, n \in \nN \). *Products:* let \( Q(n) \) be "\( mn \in \nN \)". Then \( m \cdot 0 = 0 \in \nN \) by (\( \nN \)0). If \( mn \in \nN \), then \( m(n + 1) = mn + m \), a sum of the two natural numbers \( mn \) and \( m \), so it lies in \( \nN \) by the half just proved. By @ax-induction, \( mn \in \nN \) for every \( n \).

*(c)* Let \( P(n) \) be "\( n = 0 \) or \( n - 1 \in \nN \)". \( P(0) \) holds by its first disjunct. Let \( n \in \nN \); then \( (n + 1) - 1 = n \in \nN \), so \( P(n + 1) \) holds by its second disjunct. By @ax-induction, \( P(n) \) holds for every \( n \in \nN \), and for \( n \ne 0 \) its second disjunct is the claim.

*(d)* Let \( P(m) \) be "for every \( n \in \nN \), if \( m \le n \), then \( n - m \in \nN \)". *Base case:* \( n - 0 = n \in \nN \). *Step:* let \( m \in \nN \) with \( P(m) \), and let \( n \in \nN \) with \( m + 1 \le n \). Then \( m < m + 1 \le n \), so \( n - m \in \nN \) by \( P(m) \). Moreover \( n - m \ge 1 > 0 \), so \( n - m \ne 0 \), and (c) gives \( (n - m) - 1 \in \nN \). Since \( (n - m) - 1 = n - (m + 1) \), this is \( P(m + 1) \). By @ax-induction, \( P(m) \) holds for every \( m \in \nN \).

*(e)* Let \( m < n \). By (d), \( n - m \in \nN \), and \( n - m > 0 \), so \( n - m \ne 0 \) and (a) gives \( n - m \ge 1 \), that is, \( m + 1 \le n \). Now suppose \( k \in \nN \) with \( n < k < n + 1 \). Applying what we just proved to \( n < k \) gives \( n + 1 \le k \), which contradicts \( k < n + 1 \). So no such \( k \) exists. This proves the lemma.
:::

Read the proof of (c) again. Its inductive step never mentions \( P(n) \).

::: {#exm-predecessor-no-hypothesis}
[An induction that ignores its hypothesis]

Chapter 3, after its first worked induction (@exm-sum-consecutive-products), said: "A proof by induction that never uses its induction hypothesis is either not an induction or is hiding a gap." The proof of @lem-naturals-arithmetic (c) never uses its induction hypothesis. Is it an induction, and is it hiding a gap?
:::

::: {.solution}
It is an induction, and it hides no gap. Its base case \( P(0) \) is proved, and its step "\( P(n) \Rightarrow P(n + 1) \)" is a valid implication for every \( n \in \nN \): the conclusion \( P(n + 1) \) is proved outright, so the implication holds whatever \( P(n) \) says. Then @ax-induction delivers \( P(n) \) for every \( n \). The hypothesis \( n \in \nN \) of the step is used, through \( (n + 1) - 1 = n \in \nN \); only \( P(n) \) is not.

Nor can a case analysis replace the axiom here. A direct proof would have to say which numbers lie in \( \nN \), and the only thing that says so is induction: the step shows that every number of the form \( n + 1 \) with \( n \in \nN \) has the property, and it is @ax-induction that tells us every natural number other than \( 0 \) is of this form. Chapter 3's sentence is a rule of thumb, and a good one: an unused hypothesis is a reason to check the proof line by line. Here the check passes. The exception is a step whose conclusion is reached without the hypothesis, and the axiom is still what carries the property from \( 0 \) to every \( n \).
:::

The lemma also closes a gap in Chapter 3. The proof of @thm-strong-induction used two facts about \( \nN \) as school knowledge. In its base case it said "No natural number is less than \( 0 \), so \( P(k) \) holds for every \( k \in \nN \) with \( k < 0 \), vacuously" and "The only \( k \in \nN \) with \( k \le 0 \) is \( 0 \)": both are (a), the second with trichotomy. In its inductive step it said "The natural numbers \( k < n + 1 \) are exactly those with \( k \le n \), since no natural number lies strictly between \( n \) and \( n + 1 \)", and then "A natural number \( k \le n + 1 \) satisfies \( k \le n \) or \( k = n + 1 \)": both are (e), with trichotomy. The proofs of (a), (d) and (e) above use only @ax-induction, (\( \nN \)0), (\( \nN \)S), part (c) and the arithmetic of \( \nR \), and none of them uses strong induction. So strong induction rests on those items alone, and from now on we may cite @thm-strong-induction with no school fact behind it.

::: {.check}
Where in the proof of @lem-naturals-arithmetic (d) is part (c) used, and could \( n \) have been fixed before the induction on \( m \), as \( m \) was in (b)?
:::

::: {.solution}
Part (c) is used to pass from \( n - m \in \nN \) to \( n - (m + 1) = (n - m) - 1 \in \nN \), after checking \( n - m \ne 0 \). The step from \( m \) to \( m + 1 \) is about one \( n \) with \( m + 1 \le n \), and it uses \( P(m) \) at that same \( n \), with the weaker bound \( m \le n \). So yes: fixing \( n \in \nN \) and inducting on "if \( m \le n \), then \( n - m \in \nN \)" proves the same thing, and then \( n \) was arbitrary. Putting "for every \( n \)" inside \( P(m) \) is harmless but not needed. It would be needed only if the step used the hypothesis at a different \( n \), such as \( n - 1 \).
:::

## The integers

Chapter 11 uses that sums, differences and products of integers are integers, and that an integer greater than \( 3 \) is at least \( 4 \). Both now follow from the lemma, by sorting integers into natural numbers and their negatives.

::: {#prp-integers-closed}
[Arithmetic of the Integers]

Let \( m, n \in \nZ \).

::: {.enumerate options="label=(\alph*)"}
1. \( m + n \), \( m - n \) and \( mn \) are integers.
2. If \( n \ge 0 \), then \( n \in \nN \); if \( n > 0 \), then \( n \in \nZ_{>0} \). Hence
\[
\nN = \{ n \in \nZ : n \ge 0 \} , \qquad \nZ_{>0} = \{ n \in \nZ : n > 0 \} = \{ n \in \nN : n \ge 1 \} .
\]
3. (**Discreteness.**) If \( m < n \), then \( m + 1 \le n \).
:::
:::

::: {.idea}
Every integer is \( a \) or \( -a \) with \( a \in \nN \), so each claim splits into cases by signs. Only one case has content: \( a + (-b) = a - b \) with \( a, b \in \nN \), which is in \( \nN \) when \( b \le a \), by @lem-naturals-arithmetic (d), and is the negative of a natural number when \( a < b \). Discreteness then follows from (b) applied to the difference \( n - m \): it is a positive integer, hence a natural number with \( n - m \ge 1 \), by (a) of the lemma.
:::

::: {.proof}
*(a)* First, \( \nZ \) is closed under \( x \mapsto -x \): if \( x \in \nN \), then \( -x \in \nZ \) by the definition of \( \nZ \); if \( x = -k \) with \( k \in \nN \), then \( -x = k \in \nN \subseteq \nZ \).

Next let \( a, b \in \nN \); we show \( a - b \in \nZ \). By trichotomy there are three cases. If \( a > b \) or \( a = b \), then \( b \le a \), and \( a - b \in \nN \) by @lem-naturals-arithmetic (d). If \( a < b \), then \( b - a \in \nN \) by (d), and \( a - b = -(b - a) \in \nZ \).

Now write \( m = \pm a \) and \( n = \pm b \) with \( a, b \in \nN \). The table lists the four sign patterns; in each, \( a + b \) and \( ab \) lie in \( \nN \) by @lem-naturals-arithmetic (b), and \( a - b \), \( b - a \) lie in \( \nZ \) by the previous paragraph.

| \( m \) | \( n \) | \( m + n \) | \( mn \) |
|---|---|---|---|
| \( a \) | \( b \) | \( a + b \in \nN \) | \( ab \in \nN \) |
| \( a \) | \( -b \) | \( a - b \in \nZ \) | \( -(ab) \in \nZ \) |
| \( -a \) | \( b \) | \( b - a \in \nZ \) | \( -(ab) \in \nZ \) |
| \( -a \) | \( -b \) | \( -(a + b) \in \nZ \) | \( ab \in \nN \) |

So \( m + n \) and \( mn \) are integers. Finally \( m - n = m + (-n) \), a sum of two integers, since \( -n \in \nZ \) by the first paragraph.

*(b)* Let \( n \ge 0 \). By the definition of \( \nZ \), either \( n \in \nN \), and we are done, or \( n = -k \) with \( k \in \nN \). In the second case \( k = -n \le 0 \), and \( k \ge 0 \) by @lem-naturals-arithmetic (a), so \( k = 0 \) and \( n = 0 \in \nN \) by (\( \nN \)0). If moreover \( n > 0 \), then \( n \) is a natural number with \( n \ne 0 \), so \( n \in \nZ_{>0} \).

For the set equalities: \( \nN \subseteq \nZ \), and every \( n \in \nN \) has \( n \ge 0 \) by (a) of the lemma; with the first sentence of (b) this gives \( \nN = \{ n \in \nZ : n \ge 0 \} \). Every element of \( \nZ_{>0} \) is a natural number \( n \ne 0 \), so \( n \ge 1 > 0 \) by (a) of the lemma; with the second sentence of (b) this gives \( \nZ_{>0} = \{ n \in \nZ : n > 0 \} \). Finally, for \( n \in \nN \), \( n \ne 0 \) implies \( n \ge 1 \) by (a), and \( n \ge 1 \) implies \( n \ne 0 \); so \( \nZ_{>0} = \{ n \in \nN : n \ge 1 \} \).

*(c)* Let \( m < n \). By (a), \( n - m \in \nZ \), and \( n - m > 0 \), so \( n - m \in \nZ_{>0} \) by (b), that is, \( n - m \ge 1 \). Hence \( m + 1 \le n \). This proves the proposition.
:::

Discreteness is the fact behind "an integer greater than \( 3 \) is at least \( 4 \)" (take \( m = 3 \)), and behind "the integers \( x \) with \( -2 \le x \le 2 \) are \( -2, -1, 0, 1, 2 \)": an integer \( x \) with \( -2 \le x \) is \( -2 \) or at least \( -1 \), and so on up to \( 2 \). It also settles the question left open above: \( \tfrac12 \notin \nZ \), since \( 0 < \tfrac12 \) would force \( 1 \le \tfrac12 \).

## Well-ordering

A fraction with even numerator and denominator can be halved, and halved again, and Chapter 2 claimed that this cannot go on for ever (the fact (L) in the proof of @thm-sqrt2-irrational). The reason is that the absolute values of the denominators form a strictly decreasing list of positive integers, and such a list must stop. The precise form of "must stop" is a statement about least elements.

A **least element** of a set \( S \subseteq \nR \) is an element \( m \in S \) such that \( m \le s \) for **every** \( s \in S \). Not every set has one: \( (0, 1] \) has none, since for every \( x \in (0, 1] \) the number \( x/2 \) lies in the set and is smaller. The empty set has none either, as a least element must be an element. Reversing the inequality, a **greatest element** of \( S \) is an element \( m \in S \) with \( s \le m \) for every \( s \in S \); this is the maximum of Section 4.7.

*Every non-empty set of natural numbers has a least element.*

::: {#thm-well-ordering}
[Well-Ordering of the Natural Numbers]

Every **non-empty** subset of \( \nN \) has a least element.
:::

*Try it first (ten minutes): suppose that \( S \subseteq \nN \) has no least element. Which property of \( n \) would you prove for every \( n \in \nN \) by strong induction, and why does it finish the proof?*

::: {.idea}
A least element cannot be found by inspecting \( S \), since we know nothing about \( S \). So we suppose there is none and show \( S \) is empty, which contradicts "non-empty". The property to carry is "\( n \notin S \)". If no number below \( n \) is in \( S \) and \( n \) were in \( S \), then \( n \) would be a least element; so \( n \) is not in \( S \). The hypothesis must speak about **every** number below \( n \), which is why the induction is strong. *Before reading on: at which line is trichotomy used, and what would go wrong without it?*
:::

::: {.proof}
Let \( S \subseteq \nN \) be non-empty, and suppose, for a contradiction, that \( S \) has no least element. For \( n \in \nN \), let \( P(n) \) be "\( n \notin S \)".

Let \( n \in \nN \), and suppose \( P(k) \) holds for every \( k \in \nN \) with \( k < n \), that is, no natural number less than \( n \) lies in \( S \). Suppose \( n \in S \). Let \( s \in S \). By trichotomy, \( s < n \), \( s = n \) or \( s > n \). The first is impossible: \( s \) is a natural number less than \( n \), so \( s \notin S \) by the hypothesis. So \( s \ge n \). As \( s \in S \) was arbitrary, \( n \) is a least element of \( S \), which contradicts our supposition. Hence \( n \notin S \), that is, \( P(n) \) holds.

By @thm-strong-induction, \( n \notin S \) for every \( n \in \nN \). Since \( S \subseteq \nN \), the set \( S \) has no elements, which contradicts \( S \) being non-empty. So \( S \) has a least element. This proves the theorem.
:::

The outer frame is an \( \rulename{RAA} \) on the statement "\( S \) has a least element". The proof shows that a least element **exists**; it does not say how to find it. Section 5.7 explained why mathematicians have argued over proofs of this kind. Here the debate has a quiet ending: if \( S \) is given by a property that can be checked number by number, testing \( 0, 1, 2, \dots \) in turn finds the least element, and the theorem says the search stops. Nothing in the proof above depends on such a test.

::: {.check}
In the proof of @thm-well-ordering, to which property is strong induction applied, and what is the induction hypothesis at \( n \)?
:::

::: {.solution}
To \( P(n) \): "\( n \notin S \)". At \( n \), the induction hypothesis is that \( k \notin S \) for every natural number \( k < n \): no element of \( S \) lies below \( n \). Together with "\( n \in S \)" it would make \( n \) a least element, which is why \( n \in S \) leads to a contradiction.
:::

::: {.warning}
Well-ordering is a property of subsets of \( \nN \), not of every set of numbers. The set of positive rationals is non-empty and has no least element: for every positive rational \( q \), the number \( q/2 \) is a smaller positive rational. Neither has \( \nZ \): \( n - 1 < n \) is again an integer. A proof that takes "the least element" of a set must first show that the set is a non-empty subset of \( \nN \), or a non-empty set of integers with an integer lower bound, as in @cor-well-ordering-integers below.
:::

::: {.check}
Does \( \{ n \in \nN : n^2 > 50 \} \) have a least element? If so, which?
:::

::: {.solution}
Yes. The set is non-empty, since \( 10^2 = 100 > 50 \), and it is a subset of \( \nN \), so @thm-well-ordering applies. The least element is \( 8 \): \( 8^2 = 64 > 50 \), while \( 7^2 = 49 \le 50 \), and for \( n \le 7 \) we have \( n^2 \le 49 \). The theorem promised a least element; finding it took a search from below.
:::

## Induction and well-ordering are the same principle

The proof of @thm-well-ordering derived well-ordering from induction. The derivation also runs the other way, and the cleanest way to say so is to ask which sets of numbers satisfy which principle. For a set \( X \subseteq \nR \), consider three structural properties:

- \( 0 \in X \);
- **closure:** for every \( n \in X \), \( n + 1 \in X \);
- the **predecessor property:** for every \( n \in X \) with \( n \ne 0 \), \( n - 1 \in X \).

The set \( \nN \) has all three, by (\( \nN \)0), (\( \nN \)S) and @lem-naturals-arithmetic (c). Say that \( X \) has the **induction property** if every \( S \subseteq X \) with \( 0 \in S \) and \( n + 1 \in S \) for every \( n \in S \) equals \( X \); and the **least-element property** if every non-empty subset of \( X \) has a least element. The closure of \( S \) in the induction property is plain closure under \( n \mapsto n + 1 \), not "closure as long as one stays in \( X \)"; the witnesses below show why that matters.

::: {#thm-induction-iff-well-ordering}
[Induction Is Equivalent to Well-Ordering]

Let \( X \subseteq \nR \) contain \( 0 \), be closed under \( n \mapsto n + 1 \), and have the predecessor property. Then \( X \) has the induction property **if and only if** \( X \) has the least-element property.
:::

::: {.idea}
\( (\Rightarrow) \) A set \( X \) with the induction property and the first two properties must be \( \nN \) itself: \( \nN \) sits inside \( X \) by @ax-induction, and the induction property of \( X \), applied to the subset \( \nN \), forces equality. Then @thm-well-ordering applies. \( (\Leftarrow) \) Take \( S \) as in the induction property and suppose \( S \ne X \); the least element \( m \) of \( X \setminus S \) is then a smallest failure; the number \( m - 1 \) just below it is not a failure, so it lies in \( S \), and closure passes that success up to \( m = (m - 1) + 1 \), a contradiction. *Before reading on: in \( (\Leftarrow) \), which of the three hypotheses on \( X \) gives \( m - 1 \in X \), and which two are not used at all?*
:::

::: {.proof}
\( (\Rightarrow) \) Suppose \( X \) has the induction property. Apply @ax-induction to the property "\( n \in X \)": its base case is \( 0 \in X \), and its step is the closure of \( X \). So \( \nN \subseteq X \). Now \( \nN \) is a subset of \( X \) that contains \( 0 \) and is closed under \( n \mapsto n + 1 \), by (\( \nN \)0) and (\( \nN \)S); the induction property of \( X \) gives \( \nN = X \). By @thm-well-ordering, every non-empty subset of \( X = \nN \) has a least element.

\( (\Leftarrow) \) Suppose \( X \) has the least-element property. Let \( S \subseteq X \) contain \( 0 \) and be closed under \( n \mapsto n + 1 \). Suppose \( S \ne X \). Then \( X \setminus S \) is non-empty: if it were empty, every element of \( X \) would lie in \( S \), so \( X \subseteq S \), and with \( S \subseteq X \) this would give \( S = X \) by @prp-subset-antisymmetric. So \( X \setminus S \) has a least element \( m \). We have \( m \ne 0 \), since \( 0 \in S \). So \( m - 1 \in X \), by the predecessor property. Since \( m - 1 < m \) and \( m \) is least in \( X \setminus S \), \( m - 1 \notin X \setminus S \), that is, \( m - 1 \in S \). Hence \( m = (m - 1) + 1 \in S \) by the closure of \( S \), which contradicts \( m \in X \setminus S \). So \( S = X \), and \( X \) has the induction property. This proves the theorem.
:::

Each hypothesis on \( X \) has a job, and dropping any one of them breaks the theorem. Each witness below names the direction that fails and the step of the proof it blocks.

- **Drop the predecessor property; \( (\Leftarrow) \) fails.** Let \( X \coloneqq \nN \cup \{ n + \tfrac12 : n \in \nN \} \). It contains \( 0 \) and is closed, since \( (n + \tfrac12) + 1 = (n + 1) + \tfrac12 \). It has the least-element property: for non-empty \( T \subseteq X \), compare a least element of \( T \cap \nN \) with \( \tfrac12 \) plus a least element of \( \{ t - \tfrac12 : t \in T \setminus \nN \} \), each of the two sets, when non-empty, being a subset of \( \nN \); the smaller of the candidates is least in \( T \) (Exercise C2 asks for the details). But \( S \coloneqq \nN \) contains \( 0 \), is closed, and is not \( X \), since \( \tfrac12 \notin \nN \) by @lem-naturals-arithmetic (e). The proof of \( (\Leftarrow) \) breaks at "\( m - 1 \in X \)": here \( m = \tfrac12 \) is least in \( X \setminus S \), and \( m \ne 0 \), but \( m - 1 = -\tfrac12 \notin X \).
- **Drop closure; \( (\Rightarrow) \) fails.** Let \( X \coloneqq \{ -n : n \in \nN \} = \{ 0, -1, -2, \dots \} \). It contains \( 0 \), and it has the predecessor property, since \( (-n) - 1 = -(n + 1) \). Its induction property holds **vacuously**: a subset \( S \subseteq X \) containing \( 0 \) and closed under \( n \mapsto n + 1 \) would contain \( 1 \), and \( 1 \notin X \), since \( 1 = -n \) would give \( n = -1 < 0 \), against @lem-naturals-arithmetic (a); so no such \( S \) exists, and every one of them (there are none) equals \( X \). But \( X \) itself has no least element, since \( -(n + 1) < -n \). The proof of \( (\Rightarrow) \) breaks at "\( \nN \subseteq X \) by @ax-induction": the property "\( n \in X \)" has no inductive step.
- **Drop \( 0 \in X \); \( (\Rightarrow) \) fails.** Let \( X \coloneqq \{ k + \tfrac12 : k \in \nZ \} \). It is closed, and it has the predecessor property, since \( (k + \tfrac12) \pm 1 = (k \pm 1) + \tfrac12 \) with \( k \pm 1 \in \nZ \) by @prp-integers-closed (a). Its induction property holds vacuously, because \( 0 \notin X \), so no subset of \( X \) contains \( 0 \). (Indeed \( 0 = k + \tfrac12 \) would need \( k = -\tfrac12 \in \nZ \), and then \( \tfrac12 = -k \in \nZ \) by @prp-integers-closed (a), which discreteness rules out, as shown above.) And \( X \) has no least element, since \( (k - 1) + \tfrac12 < k + \tfrac12 \). The proof of \( (\Rightarrow) \) breaks at "\( \nN \subseteq X \) by @ax-induction": the property "\( n \in X \)" has no base case, since \( 0 \notin X \).

In the last two witnesses the induction property is not false but vacuous. That is why the theorem uses plain closure of \( S \). Under a "closure relative to \( X \)" reading (\( n + 1 \in S \) only when \( n + 1 \in X \)), the set \( S = \{0\} \) would qualify in the closure witness, the induction property would fail there, and the witness would no longer separate the two properties.

So the slogan "induction and well-ordering are the same principle" means exactly @thm-induction-iff-well-ordering: for a set of numbers with \( 0 \), closure and predecessors, either principle implies the other. So Chapter 3 could have taken, alongside (\( \nN \)0) and (\( \nN \)S), the predecessor property and well-ordering as its axioms, and proved induction from them by the \( (\Leftarrow) \) half of @thm-induction-iff-well-ordering. The first witness above shows that the predecessor property cannot be left out, and with induction gone it could no longer be proved as @lem-naturals-arithmetic (c) was. Chapter 9 builds \( \nN \) from sets and proves the Peano axioms, induction among them, there.

## Sets of integers

Well-ordering moves to sets of integers by a shift, provided the bound that makes the shift work is itself an integer.

::: {#cor-well-ordering-integers}
[Well-Ordering of Sets of Integers]

Let \( S \subseteq \nZ \) be non-empty. If \( S \) has a lower bound \( b \in \nZ \), then \( S \) has a least element. If \( S \) has an upper bound \( b \in \nZ \), then \( S \) has a greatest element.
:::

::: {.idea}
Slide \( S \) to the right by \( -b \), so that its lower bound lands on \( 0 \); the shifted set lies in \( \nN \), where @thm-well-ordering applies, and sliding back preserves order. For an upper bound, reflect: \( -S \) is bounded below by \( -b \).
:::

::: {.proof}
*Lower bound.* Let \( T \coloneqq \{ s - b : s \in S \} \). Each \( s - b \) is an integer by @prp-integers-closed (a), and \( s - b \ge 0 \) since \( b \le s \); so \( s - b \in \nN \) by @prp-integers-closed (b). Thus \( T \) is a non-empty subset of \( \nN \), and by @thm-well-ordering it has a least element \( m_0 - b \) with \( m_0 \in S \). For every \( s \in S \), \( m_0 - b \le s - b \), so \( m_0 \le s \). Hence \( m_0 \) is a least element of \( S \).

*Upper bound.* Let \( -S \coloneqq \{ -s : s \in S \} \). It is a non-empty set of integers (negatives of integers are integers, by the definition of \( \nZ \) and @prp-integers-closed (a)), and \( -b \) is an integer lower bound for it, since \( s \le b \) gives \( -b \le -s \). By the first half, \( -S \) has a least element \( -m \) with \( m \in S \). For every \( s \in S \), \( -m \le -s \), so \( s \le m \): \( m \) is a greatest element of \( S \). This proves the corollary.
:::

The bound must be an integer, or at least have an integer below it. Given a set of integers bounded below by the real number \( -\tfrac{7}{2} \), we would first replace \( -\tfrac72 \) by the integer \( -4 \), and that step, for an arbitrary real bound, is the Archimedean property of Chapter 11: Chapter 11's integer-part lemma in Section 11.6 does exactly this. In an ordered field without the Archimedean property, a set of integers can be bounded below and have no least element (in the field \( \nR(x) \) of Chapter 11's example of a non-Archimedean field, every \( n \in \nN \) has \( n < x \), so the set \( \{ -n : n \in \nN \} \) is bounded below by \( -x \), and it has no least element, since \( -(n + 1) < -n \)), so this chapter, which has no Archimedean property, proves the corollary with an integer bound, and Chapter 11 supplies the rest.

## Exercises

### A. Check your understanding

::: {#exr-naturals-and-well-ordering-a1}
[A1]

Parts (a)–(d) are about the proof of @thm-well-ordering.

::: {.enumerate options="label=(\alph*)"}
1. Where is trichotomy used?
2. Why would ordinary induction (@ax-induction) on the same property "\( n \notin S \)" not do?
3. Run the proof on \( S = \{4, 7, 9\} \): at which \( n \) does the argument meet an element of \( S \), and what does it conclude there?
4. State the idea of the proof in two sentences.
5. Let \( X = \nN \cup \{ n + \tfrac12 : n \in \nN \} \). Which statements of @lem-naturals-arithmetic remain true when every "\( \nN \)" in them is replaced by "\( X \)"? Decide each clause of (a), each half of (b), and (c), (d), (e) separately, with a witness for each failure.
:::
:::

::: {.solution}
*(a)* In the inductive step, to split an arbitrary \( s \in S \) into \( s < n \), \( s = n \) or \( s > n \). The first case is excluded by the hypothesis, so \( s \ge n \). Without trichotomy, "\( s \) is not less than \( n \)" would not give "\( s \ge n \)", and \( n \) would not be shown to be least.

*(b)* Ordinary induction gives only \( P(n - 1) \), that is, \( n - 1 \notin S \), as hypothesis for \( P(n) \). That does not exclude a smaller element of \( S \), such as \( n - 5 \), so "\( n \in S \)" would not make \( n \) least, and no contradiction would follow. The proof needs **all** numbers below \( n \) to be outside \( S \).

*(c)* \( S = \{4, 7, 9\} \) has a least element, so the supposition of the proof is false, and the argument meets its contradiction. For \( n = 0, 1, 2, 3 \), no smaller number is in \( S \), and indeed \( n \notin S \). At \( n = 4 \), no natural number below \( 4 \) is in \( S \), and \( 4 \in S \); the argument shows that every \( s \in S \) has \( s \ge 4 \), so \( 4 \) is a least element of \( S \). That contradicts the supposition "\( S \) has no least element", and the proof concludes that \( S \) has a least element, namely \( 4 \).

*(d)* If \( S \) had no least element, then no \( n \) could be in \( S \), because the first one would be least; strong induction makes "the first one" precise. So \( S \) would be empty, against the hypothesis.

*(e)* Holding: the first clause of (a) (every element is \( \ge 0 \)); the sum half of (b), since a sum of two halves \( (m + \tfrac12) + (n + \tfrac12) = m + n + 1 \) is a natural number and a half plus a natural number is a half; and (d): if \( x \le y \) in \( X \), then \( y - x \in X \). For (d) there are four cases. Two natural numbers, or two halves, have a difference in \( \nN \) by @lem-naturals-arithmetic (d). For \( x = m \le y = n + \tfrac12 \), we have \( m \le n \) (else \( m \ge n + 1 > y \) by (e) of the lemma), so \( y - x = (n - m) + \tfrac12 \in X \). For \( x = m + \tfrac12 \le y = n \), we have \( m < n \), so \( m + 1 \le n \) and \( y - x = (n - m - 1) + \tfrac12 \in X \).

Failing: the second clause of (a), since \( \tfrac12 \ne 0 \) and \( \tfrac12 < 1 \); the product half of (b), since \( \tfrac12 \cdot \tfrac12 = \tfrac14 \notin X \) (it is not a natural number, as \( 0 < \tfrac14 < 1 \), and not a half, as \( \tfrac14 - \tfrac12 < 0 \)); (c), since \( \tfrac12 \ne 0 \) and \( \tfrac12 - 1 = -\tfrac12 \notin X \); (e), since \( 0 < \tfrac12 < 1 \) with \( \tfrac12 \in X \).

Each clause had to be decided by its own witness. The proofs of (a)–(d) were inductions over \( \nN \), and \( X \) does not have the induction property (\( \nN \subseteq X \) contains \( 0 \) and is closed), so none of those proofs carries over; some conclusions survive anyway. (c) fails because the predecessor property fails at \( \tfrac12 \). (e) fails through the second clause of (a), not through (d), which still holds. The set \( \nZ \cup \{ k + \tfrac12 : k \in \nZ \} \) has the predecessor property and still has \( \tfrac12 \) between \( 0 \) and \( 1 \), so the predecessor property alone (with \( 0 \) and closure) does not give (e); together with the least-element property it does: the set then has the induction property by @thm-induction-iff-well-ordering, and, as in the proof of its \( (\Rightarrow) \) half, it equals \( \nN \).
:::

### B. Practice

::: {#exr-naturals-and-well-ordering-b1}
[B1]

Use only @lem-naturals-arithmetic and the arithmetic of \( \nR \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( m, n \in \nN \) and \( mn = 1 \), then \( m = n = 1 \).
2. Prove that \( n^2 \ge n \) for every \( n \in \nN \).
:::
:::

::: {.solution}
*(a)* Since \( 0 \cdot n = 0 \ne 1 \), we have \( m \ne 0 \), and likewise \( n \ne 0 \). By the second clause of @lem-naturals-arithmetic (a), \( m \ge 1 \) and \( n \ge 1 \). Suppose \( m > 1 \). Multiplying by \( n > 0 \) gives \( mn > n \ge 1 \), which contradicts \( mn = 1 \). So \( m = 1 \), and then \( n = mn = 1 \).

*(b)* Let \( n \in \nN \). By @lem-naturals-arithmetic (a), \( n = 0 \) or \( n \ge 1 \). If \( n = 0 \), then \( n^2 = 0 = n \). If \( n \ge 1 \), multiplying \( n \ge 1 \) by \( n > 0 \) gives \( n^2 \ge n \). In both cases \( n^2 \ge n \).
:::

::: {#exr-naturals-and-well-ordering-b2}
[B2: Putting a proof in order]

The lines below, (i)–(ix), include the seven lines of a proof of \( (\Leftarrow) \) in @thm-induction-iff-well-ordering, shuffled, and two lines that do not belong. Here \( X \) has \( 0 \in X \), closure and the predecessor property, and the least-element property. Write the seven lines in an order that makes a correct proof, and say why each of the other two lines fails.

::: {.enumerate options="label=(\roman*)"}
1. So \( m - 1 \in X \), by the predecessor property.
2. Let \( m \) be the least element of \( S \).
3. Then \( X \setminus S \) is non-empty, so it has a least element \( m \).
4. Hence \( m = (m - 1) + 1 \in S \), a contradiction; so \( S = X \).
5. Let \( S \subseteq X \) contain \( 0 \) and be closed under \( n \mapsto n + 1 \).
6. \( m - 1 < m \), so \( m - 1 \notin X \setminus S \), that is, \( m - 1 \in S \).
7. Since \( m \) is least and \( m - 1 < m \), \( m - 1 \in X \setminus S \).
8. Suppose \( S \ne X \).
9. \( m \ne 0 \), since \( 0 \in S \).
:::
:::

::: {.solution}
The order is (v), (viii), (iii), (ix), (i), (vi), (iv). It is the only admissible one. (v) introduces \( S \), (viii) is the supposition the rest contradicts, and (iii) introduces \( m \) from it. (ix) must sit between (iii) and (i): it needs the \( m \) of (iii), and (i) applies the predecessor property, which needs \( m \ne 0 \). (vi) uses the \( m - 1 \in X \) of (i): only an element of \( X \) can be sorted into \( S \) or \( X \setminus S \). (iv) uses (vi) and closure.

Line (ii) takes the least element of the wrong set. The set whose least element locates a failure is \( X \setminus S \): its least element is the first number of \( X \) missing from \( S \). A least element of \( S \) says nothing about where \( S \) and \( X \) differ; in the case \( X = \nN \) it is \( 0 \), which lies in \( S \) by (v) and is no failure at all. Line (vii) reads leastness backwards: "\( m \) is least in \( X \setminus S \)" says that nothing **below** \( m \) lies in \( X \setminus S \), so a smaller number of \( X \) is in \( S \), not outside it.
:::

::: {#exr-naturals-and-well-ordering-b3}
[B3]

Prove the second half of @cor-well-ordering-integers directly from @thm-well-ordering, without using the first half: if \( S \subseteq \nZ \) is non-empty and \( b \in \nZ \) is an upper bound of \( S \), then \( S \) has a greatest element.

*Hint: shift by \( s \mapsto b - s \).*
:::

::: {.solution}
Let \( T \coloneqq \{ b - s : s \in S \} \). For \( s \in S \), \( b - s \) is an integer by @prp-integers-closed (a), and \( b - s \ge 0 \) because \( s \le b \); so \( b - s \in \nN \) by @prp-integers-closed (b). Thus \( T \) is a non-empty subset of \( \nN \), and by @thm-well-ordering it has a least element, of the form \( b - s_0 \) with \( s_0 \in S \). For every \( s \in S \), \( b - s_0 \le b - s \), so \( s \le s_0 \). Hence \( s_0 \) is a greatest element of \( S \).
:::

### C. Going deeper

::: {#exr-naturals-and-well-ordering-c1}
[C1: A greatest element from a least upper bound]

Let \( S \subseteq \nN \) be non-empty, and suppose some \( M \in \nN \) satisfies \( s \le M \) for every \( s \in S \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( S \) has a greatest element by applying @thm-well-ordering to the set \( U \) of upper bounds of \( S \) that lie in \( \nN \), not by citing @cor-well-ordering-integers: show that the least element of \( U \) lies in \( S \).
2. Show that the hypothesis "some \( M \in \nN \) bounds \( S \) above" cannot be dropped.
:::
:::

::: {.solution}
[Hint 1]

Consider \( U \coloneqq \{ u \in \nN : s \le u \text{ for every } s \in S \} \).
:::

::: {.solution}
[Hint 2]

\( U \) is non-empty because \( M \in U \); let \( u \) be its least element, which exists by @thm-well-ordering.
:::

::: {.solution}
*(a)* Let \( U \coloneqq \{ u \in \nN : s \le u \text{ for every } s \in S \} \). Then \( M \in U \), so \( U \) is a non-empty subset of \( \nN \), and @thm-well-ordering gives a least element \( u \) of \( U \). We show \( u \in S \).

Suppose \( u \notin S \). Then every \( s \in S \) satisfies \( s \le u \) and \( s \ne u \), so \( s < u \), and \( s + 1 \le u \) by @lem-naturals-arithmetic (e); that is, \( s \le u - 1 \). Since \( S \) is non-empty, it has an element \( s_0 \), and \( 0 \le s_0 < u \) by @lem-naturals-arithmetic (a), so \( u \ne 0 \). By @lem-naturals-arithmetic (c), \( u - 1 \in \nN \). So \( u - 1 \) is an upper bound of \( S \) in \( \nN \), that is, \( u - 1 \in U \), and \( u - 1 < u \), which contradicts the choice of \( u \). Hence \( u \in S \).

Since \( u \in S \) and \( s \le u \) for every \( s \in S \), \( u \) is a greatest element of \( S \).

*(b)* \( S = \nN \) is non-empty and has no greatest element: for every \( n \in \nN \), also \( n + 1 \in \nN \) by (\( \nN \)S), and \( n + 1 > n \). In the proof, \( U \) is then empty, and @thm-well-ordering has nothing to apply to.

The number \( u \) of (a) is the **least upper bound** of \( S \) among natural numbers, and the proof shows that it lies in \( S \). Section 7.6 defines least upper bounds in any partially ordered set, and Chapter 11 is about sets of real numbers whose least upper bound, when it exists, need **not** lie in the set.

**Marking scheme.** (10 points)
- 2: defines the set of upper bounds in \( \nN \), shows it is non-empty, and takes its least element by @thm-well-ordering.
- 2: handles \( u = 0 \) separately, or shows \( u \ne 0 \) using that \( S \) is non-empty, before using \( u - 1 \in \nN \) (@lem-naturals-arithmetic (c)).
- 3: uses the minimality of \( u \): either shows directly that \( u - 1 \notin U \), so some \( s \in S \) has \( s > u - 1 \), or, supposing \( u \notin S \), derives \( u - 1 \in U \) and contradicts minimality.
- 1: uses discreteness (@lem-naturals-arithmetic (e)) to show that an element of \( S \) greater than \( u - 1 \) equals \( u \), or to get \( s \le u - 1 \) in the contradiction route, and concludes that \( u \in S \) is a greatest element.
- 2: (b) the witness \( S = \nN \), with the reason it has no greatest element.
Fatal errors (0 for the step): using \( u - 1 \in \nN \) without checking \( u \ne 0 \); taking a least element of \( U \) without showing \( U \) non-empty.

A second route, through the least element \( M - s_0 \) of \( \{ M - s : s \in S \} \subseteq \nN \) (as in @exr-naturals-and-well-ordering-b3), proves the conclusion of (a) but not by the method the task names, so it earns at most 4 points for (a): 2 for showing that this set is a non-empty subset of \( \nN \) and taking its least element, and 2 for deducing \( s \le s_0 \) for every \( s \in S \) from \( M - s_0 \le M - s \), with \( s_0 \in S \); and (b) as above.
:::

::: {#exr-naturals-and-well-ordering-c2}
[C2: A well-ordered set with gaps]

Let \( X \coloneqq \nN \cup \{ n + \tfrac12 : n \in \nN \} \). Prove that every non-empty subset of \( X \) has a least element.
:::

::: {.solution}
Let \( T \subseteq X \) be non-empty, and put
\[
A \coloneqq T \cap \nN , \qquad B \coloneqq \{ t - \tfrac12 : t \in T \setminus \nN \} .
\]
Every \( t \in T \setminus \nN \) is \( n + \tfrac12 \) for some \( n \in \nN \), since \( t \in X \); so \( t - \tfrac12 = n \in \nN \), and \( B \subseteq \nN \). Since \( T = A \cup (T \setminus \nN) \) is non-empty, \( A \) or \( B \) is non-empty. By @thm-well-ordering, \( A \), if non-empty, has a least element \( a \), and \( B \), if non-empty, has a least element \( b \). Define
\[
c \coloneqq
\begin{cases}
a & \text{if } B = \emptyset , \\
b + \tfrac12 & \text{if } A = \emptyset , \\
\min\{ a, \, b + \tfrac12 \} & \text{otherwise.}
\end{cases}
\]
In each case \( c \in T \): \( a \in A \subseteq T \), and \( b = t - \tfrac12 \) for some \( t \in T \setminus \nN \), so \( b + \tfrac12 = t \in T \).

Let \( t \in T \). If \( t \in \nN \), then \( t \in A \), so \( A \ne \emptyset \) and \( t \ge a \ge c \). If \( t \notin \nN \), then \( t - \tfrac12 \in B \), so \( B \ne \emptyset \) and \( t - \tfrac12 \ge b \), that is, \( t \ge b + \tfrac12 \ge c \). (In both chains, the last inequality holds in every case of the definition of \( c \) that can occur.) So \( c \) is a least element of \( T \).

The set \( X \) has the least-element property, contains \( 0 \) and is closed under \( n \mapsto n + 1 \), but it does not have the induction property (\( \nN \subseteq X \) contains \( 0 \) and is closed, and \( \nN \ne X \)). That is the first witness after @thm-induction-iff-well-ordering: without the predecessor property, well-ordering does not give induction.

**Marking scheme.** (10 points)
- 2: splits \( T \) into its natural-number part and its half part, and shows the shifted half part lies in \( \nN \).
- 2: applies @thm-well-ordering to each non-empty part, saying that at least one part is non-empty.
- 2: defines the candidate in all cases, including those where one part is empty, and checks it lies in \( T \).
- 3: checks the candidate is \( \le t \) for every \( t \in T \), by cases on \( t \in \nN \) or not.
- 1: concludes, with the quantifiers right: one least element for the given \( T \).
Fatal errors (0 for the step): applying @thm-well-ordering to \( T \) itself (it need not be a subset of \( \nN \)); taking a least element of an empty part.

A second route, through the least element of \( \{ 2t : t \in T \} \subseteq \nN \), earns the same points. It earns 4 for showing that this set lies in \( \nN \), checking both \( 2n \) and \( 2n + 1 \) by @lem-naturals-arithmetic (b), and that it is non-empty, and for taking its least element \( 2t_0 \) with \( t_0 \in T \) by @thm-well-ordering. It earns 4 for deducing \( t_0 \le t \) from \( 2t_0 \le 2t \) for every \( t \in T \), and 2 for the conclusion. The same fatal errors apply.
:::

<!-- dependency ledger
lem-naturals-arithmetic (proof): real arithmetic and order (n + 1 >= 2 >= 1 from n >= 1; (m + n) + 1 = m + (n + 1); m(n + 1) = mn + m; (n - m) - 1 = n - (m + 1); m < m + 1) | R arithmetic and order, school fact; axioms in Chapter 11
exm-predecessor-no-hypothesis (solution): an implication whose conclusion is proved outright holds | Ch 1 ->I (the step proved inside the box without its assumption); stated inline
thm-well-ordering (proof): trichotomy s < n, s = n or s > n for reals | R order, school fact; axioms in Chapter 11
thm-well-ordering (proof): RAA on "S has a least element" | Ch 2 RAA, named in the prose after the proof
prp-integers-closed (proof): trichotomy for a, b in N; -(b - a) = a - b; (+-a)(+-b) = +-(ab); m - n = m + (-n) | R arithmetic and order, school fact; axioms in Chapter 11
cor-well-ordering-integers (proof): m0 - b <= s - b gives m0 <= s; s <= b gives -b <= -s | R arithmetic and order, school fact; axioms in Chapter 11
thm-induction-iff-well-ordering (claim): (the witness paragraph) n + 1/2 not in N; 1 not of the form -n; 1/2 not in Z; (n + 1/2) + 1 = (n + 1) + 1/2 and similar | lem-naturals-arithmetic (a), (e), prp-integers-closed (c) (cited); R arithmetic
thm-induction-iff-well-ordering (claim): (the first witness) N u (N + 1/2) has the least-element property | inline sketch; proved in full in exr-naturals-and-well-ordering-c2 (not used by any proof)
cor-well-ordering-integers (claim): (the paragraph after it) a real bound must first be replaced by an integer below it (Archimedean); a non-Archimedean field has a set of integers bounded below with no least element ({-n : n in N} in R(x), bounded below by -x since n < x) | Ch 11 exm-nonarchimedean-field (n < x for every n in N; prose pointer, no @ref; nothing here depends on it); -(n + 1) < -n, R arithmetic
thm-well-ordering (claim): (the remark after the proof) disputes over existence proofs | Ch 5 Section 5.7 (prose pointer)
thm-well-ordering (claim): (the paragraph before it) a greatest element is the maximum of Section 4.7 | Ch 4 Section 4.7 (prose pointer; the definition is restated here)
thm-induction-iff-well-ordering (claim): (aftermath) N built from sets, Peano axioms (induction among them) proved | Ch 9 (prose pointer; nothing depends on it)
exr-naturals-and-well-ordering-a1 (solution): (e) 1/4 not in N, 1/2 - 1 < 0; Z u (Z + 1/2) has the predecessor property | R arithmetic; lem-naturals-arithmetic (a), (d), (e) (cited); verify/ch07/exr-naturals-and-well-ordering-a1.py
exr-naturals-and-well-ordering-b1 (solution): multiplying an inequality by a positive number | R order, school fact
thm-well-ordering (claim): (the quick check) 7^2 = 49, 8^2 = 64, 10^2 = 100, n^2 <= 49 for n <= 7 | arithmetic; powers, school meaning (def-power in Section 7.3); verify/ch07/thm-well-ordering.py
-->
