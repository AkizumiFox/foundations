# Sequences and Limits in an Ordered Field

<!-- S3: style revision per S1 change list (layout-proposal.md §3, 4.3, pipeline S): scratch work finding N from |aₙ − a| (B1 as the worked example); new method box (provisional exm-method-limit-from-definition); ε/2 uniqueness by Idea. -->

In \( \nQ \) the fractions \( 1/2, 2/3, 3/4, \dots \) "tend to \( 1 \)". Sections 4.1 and 4.2 supplied the tools to say what that means without leaving \( \nQ \): an absolute value to measure distance, and the Archimedean property to make \( 1/(n + 1) \) small. This section defines the limit of a sequence in an arbitrary ordered field, with tolerances taken from that field. It then proves that a sequence has at most one limit, and that a convergent sequence is bounded. Chapter 5 applies these results with \( F = \nQ \), at a stage when no other number system is available.

Throughout, \( F \) is an ordered field (@def-ordered-ring-and-field), and \( F_{>0} = \{ x \in F : x > 0 \} \) is its set of positive elements, as in Section 4.1; for \( F = \nQ \) this is \( \nQ_{>0} \). As agreed after @prp-naturals-in-ordered-field, we write \( n \) for \( n \cdot 1_F \) where no confusion arises. So \( 1/(n + 1) \) in \( F \) means \( 1/((n + 1) \cdot 1_F) \), which exists and is positive, since \( (n + 1) \cdot 1_F \ge 1 > 0 \) by @prp-naturals-in-ordered-field (b) and reciprocals of positive elements are positive (@prp-reciprocal-order (a)).

## Sequences

A list \( 1, 1/2, 1/3, \dots \) is a rule that assigns a term to each position, and a rule of that kind already has a name: a function on \( \nN \).

::: {#def-sequence-ordered-field}
[Sequence; Eventually]

A **sequence** in \( F \) is a function \( a \colon \nN \to F \) (@fd2:def-function). Its value at \( n \) is written \( a_n \) and called the \( n \)-th **term**; the sequence is written \( (a_n)_{n \in \nN} \), or \( (a_n) \), and \( \{ a_n : n \in \nN \} \) is its set of values.

A property \( P(n) \) of natural numbers holds **eventually** if **there is** \( N_0 \in \nN \) such that \( P(n) \) holds **for every** \( n \in \nN \) with \( n \ge N_0 \).
:::

**Examples.**

- In \( \nQ \): \( a_n \coloneqq 1/(n + 1) \), with terms \( 1, 1/2, 1/3, \dots \).
- In any \( F \): \( a_n \coloneqq n \), that is, \( n \cdot 1_F \), with terms \( 0, 1, 2, \dots \); and \( a_n \coloneqq (-1)^n \), with the powers of @def-naturals-in-ordered-field, with terms \( 1, -1, 1, \dots \). The second sequence has infinitely many terms but only two values: its set of values is \( \{ 1, -1 \} \). A sequence is ordered and may repeat; its set of values forgets both.
- The degenerate case: a **constant sequence** \( a_n \coloneqq c \) for a fixed \( c \in F \). It matters because every definition below must give the expected answer on it.
- A sequence may be defined by recursion (@fd2:thm-recursion, read on \( \nN = \omega \) as @thm-omega-recursion through @cor-omega-identification (b)). The Newton sequence of @exm-newton-rationals-sqrt2, \( x_0 = 2 \) and \( x_{n+1} = (x_n^2 + 2)/(2x_n) \), is a sequence in \( \nQ \); Section 4.6 studies it.

**Non-example by minimal change.** The formula \( n \mapsto 1/n \) defines no sequence: at \( n = 0 \) it asks for \( 1/0 \), and \( 0 \) has no inverse. Everything else about the first example survives the change, and only "a function on all of \( \nN \)" fails. This is why the book's sequences start at \( n = 0 \) and why we write \( 1/(n + 1) \).

"Eventually" absorbs any finite beginning. In \( \nQ \), "\( 1/(n + 1) < 1/10 \)" holds eventually, from \( N_0 = 10 \) on, although it fails for \( n \le 9 \); "\( (-1)^n = 1 \)" does not hold eventually, since it fails at every odd \( n \). Two eventual properties hold together eventually: if \( P(n) \) holds for \( n \ge N_0 \) and \( Q(n) \) for \( n \ge N_1 \), then both hold for \( n \ge \max\{N_0, N_1\} \), the larger of the two numbers, which exists by trichotomy in \( \nN \) (@thm-omega-order (a)). The same goes for any finite number of properties, taking the larger number one comparison at a time. For infinitely many properties it fails: "\( 1/(n + 1) < 1/(k + 1) \)" holds eventually for each \( k \in \nN \), from \( N_0 = k + 1 \) on, but no single \( N_0 \) serves every \( k \), since \( k = N_0 \) fails at \( n = N_0 \).

## The limit of a sequence

We want a precise sense in which \( 1/2, 2/3, 3/4, \dots \) "tends to \( 1 \)" in \( \nQ \). The first idea is "the terms get closer and closer to \( 1 \)". Here is why it fails. With \( a_n \coloneqq (n + 1)/(n + 2) \),
\[
1 - a_n = \frac{1}{n + 2} , \qquad 2 - a_n = \frac{n + 3}{n + 2} = 1 + \frac{1}{n + 2} .
\]
Both distances shrink at every step, so the terms get "closer and closer" to \( 2 \) as well. What singles out \( 1 \) is that the distance to \( 1 \) falls below **any** tolerance we name, and stays below it, while the distance to \( 2 \) never falls below \( 1 \). The tolerances must come from \( F \) itself, since in \( \nQ \) there is nothing else to measure with.

*Every tolerance in \( F \) is eventually met.*

::: {#def-sequence-limit-ordered-field}
[Limit of a Sequence in an Ordered Field]

Let \( (a_n) \) be a sequence in \( F \) and \( a \in F \). The sequence **converges to** \( a \) in \( F \), written \( a_n \to a \), if **for every** \( \varepsilon \in F_{>0} \) **there exists** \( N \in \nN \) such that \( \abs{a_n - a} < \varepsilon \) **for every** \( n \in \nN \) with \( n \ge N \). In symbols,
\[
\forall \varepsilon \in F_{>0} \ \ \exists N \in \nN \ \ \forall n \in \nN \ \ \bigl( n \ge N \Rightarrow \abs{a_n - a} < \varepsilon \bigr) .
\]
Then \( a \) is **a limit** of \( (a_n) \). The sequence is **convergent** if it converges to some \( a \in F \), and **divergent** otherwise.
:::

In words: the first clause hands us an arbitrary tolerance \( \varepsilon \), a positive element of \( F \). The second says that some index \( N \) can be found, and it may depend on \( \varepsilon \). The third says that from \( N \) on, **every** term lies within \( \varepsilon \) of \( a \): the inequality holds **eventually**. The absolute value is that of @def-absolute-value-ordered-field, and by @prp-absolute-value-ordered-field (d) the condition on each term reads
\[
\abs{a_n - a} < \varepsilon \iff a - \varepsilon < a_n < a + \varepsilon .
\]

The domain of \( \varepsilon \) is part of the definition. For \( F = \nQ \), \( \varepsilon \) is a **rational** number, and "\( a_n \to a \) in \( \nQ \)" mentions nothing outside \( \nQ \). The formula is the one translated in @fd1:exm-translate-limit (a), where it was read in the school real numbers. Here it is read in \( F \), and every fact used about it will be proved from the ordered-field axioms.

**Well-definedness.** Nothing needs checking for "converges to \( a \)". We say "**a** limit" for now, because a sequence might have two; @thm-limit-unique-ordered-field below rules that out.

Negating the definition, quantifier by quantifier (@fd1:prp-bounded-quantifier-negation for the bounded quantifiers, @fd1:prp-negated-implication for the implication), and using that \( \neg(x < \varepsilon) \) means \( x \ge \varepsilon \) in the totally ordered \( F \) (@prp-ordered-field-halves (a)): \( a_n \not\to a \) means
\[
\exists \varepsilon \in F_{>0} \ \ \forall N \in \nN \ \ \exists n \in \nN \ \ \bigl( n \ge N \wedge \abs{a_n - a} \ge \varepsilon \bigr) .
\]
One bad tolerance, and beyond every threshold a term that misses it. A sequence is divergent when this holds for **every** \( a \in F \).

::: {#exm-first-sequences-ordered-field}
[First Limits]

Decide, from @def-sequence-limit-ordered-field, which of these converge, and to what.

::: {.enumerate options="label=(\alph*)"}
1. A constant sequence \( a_n = c \) in any ordered field \( F \).
2. \( a_n = 1/(n + 1) \) in \( \nQ \).
3. \( a_n = (n + 1)/(n + 2) \) in \( \nQ \).
4. \( a_n = (-1)^n \) in any ordered field \( F \).
:::
:::

::: {.solution}
(a) \( a_n \to c \). Let \( \varepsilon \in F_{>0} \) and take \( N \coloneqq 0 \). For every \( n \), \( \abs{a_n - c} = \abs{0} = 0 < \varepsilon \). Here \( N \) does not depend on \( \varepsilon \) at all: the degenerate case.

(b) \( a_n \to 0 \). The field \( \nQ \) is Archimedean (@def-archimedean-ordered-field, by @thm-rationals-archimedean). Let \( \varepsilon \in \nQ_{>0} \). By @prp-archimedean-reciprocal there is \( N \in \nZ_{>0} \) with \( 1/m < \varepsilon \) for every \( m \ge N \). For \( n \ge N \) also \( n + 1 \ge N \), so \( \abs{a_n - 0} = 1/(n + 1) < \varepsilon \), where the absolute value drops because \( 1/(n + 1) > 0 \). The \( N \) depends on \( \varepsilon \), and Archimedes is what supplies it.

(c) \( a_n \to 1 \). By the computation above the definition, \( \abs{a_n - 1} = 1/(n + 2) \). Given \( \varepsilon \in \nQ_{>0} \), take the \( N \) of (b). For \( n \ge N \), \( n + 2 > n + 1 \ge N \), so \( 1/(n + 2) < \varepsilon \).

(d) Divergent, in **every** ordered field. By the recursion for powers, \( (-1)^{n+1} = (-1)^n (-1) = -(-1)^n \) (@prp-ring-algebra (c)), and \( \abs{(-1)^n} = 1 \) for every \( n \), by induction with @prp-absolute-value-ordered-field (b). Hence
\[
\abs{a_{n+1} - a_n} = \abs{-2 a_n} = 2 \abs{a_n} = 2
\]
for every \( n \). Suppose \( a_n \to a \) for some \( a \in F \). Take \( \varepsilon \coloneqq 1 \) and its \( N \), and let \( n \coloneqq N \), so that \( n \) and \( n + 1 \) are both \( \ge N \). The three-point triangle inequality (@prp-absolute-value-ordered-field (e)) gives
\[
2 = \abs{a_{n+1} - a_n} \le \abs{a_{n+1} - a} + \abs{a - a_n} < 1 + 1 = 2 ,
\]
so \( 2 < 2 \), against (O1). So no \( a \in F \) is a limit. The bad tolerance is \( \varepsilon = 1 \): two consecutive terms are \( 2 \) apart and cannot both lie within \( 1 \) of one point.
:::

::: {.check}
For \( a_n = 1/(n + 1) \) in \( \nQ \) and \( \varepsilon = 1/100 \), which \( N \in \nN \) satisfy "\( \abs{a_n} < \varepsilon \) for every \( n \ge N \)"?
:::

::: {.solution}
Exactly the \( N \ge 100 \). By the comparison formula (@thm-rationals-ordered-field (a)), \( 1/(n + 1) < 1/100 \) if and only if \( 100 < n + 1 \), that is, \( n \ge 100 \). So every \( N \ge 100 \) works, and an \( N \le 99 \) fails at \( n = N \) itself, where \( 1/(N + 1) \ge 1/100 \). The definition asks only for **some** working \( N \); any larger one works too.
:::

**Non-example by minimal change.** Keep the sequence \( a_n = (n + 1)/(n + 2) \) and change the candidate limit from \( 1 \) to \( 2 \). The distance \( \abs{a_n - 2} = 1 + 1/(n + 2) \) still shrinks at every step, and still the definition fails, at its first clause: for \( \varepsilon \coloneqq 1 \), every term has \( \abs{a_n - 2} > 1 \), so no \( N \) exists. This is the negation displayed above, with \( \varepsilon = 1 \) and \( n = N \) for every \( N \).

**Why this definition.**

- *Strict or not.* Replacing \( \abs{a_n - a} < \varepsilon \) by \( \abs{a_n - a} \le \varepsilon \) gives the same notion: given \( \varepsilon \), apply the weak form to \( \varepsilon/2 \), and \( \varepsilon/2 < \varepsilon \) (@prp-ordered-field-halves (b)).
- *Every \( n \ge N \), not some.* With "some \( n \ge N \)" the sequence \( (-1)^n \) would "converge" both to \( 1 \) and to \( -1 \): beyond any \( N \) there are terms equal to each.
- *The order of the quantifiers.* With \( \exists N \) before \( \forall \varepsilon \), the condition says that \( a_n = a \) for every \( n \ge N \): for each such \( n \), \( \abs{a_n - a} \) lies below every element of \( F_{>0} \), so it is not itself positive, and it is \( 0 \) by @prp-absolute-value-ordered-field (a). (Exercise A1 (b) asks for the details.) Then \( 1/(n + 1) \) would have no limit in \( \nQ \).
- *Tolerances from \( F \).* In a field with more elements than \( \nQ \), "every rational tolerance is eventually met" can be strictly weaker than "every tolerance in \( F \) is eventually met". The remark after @prp-reciprocals-null-iff-archimedean shows this happen.

::: {.warning}
\( a_n \to a \) does **not** say that some term equals \( a \): \( 1/(n + 1) \to 0 \) in \( \nQ \) (@exm-first-sequences-ordered-field (b)), and no term is \( 0 \). Nor does it say that \( \abs{a_n - a} \) decreases: \( a_n \coloneqq (1 + (-1)^n)/(n + 1) \) in \( \nQ \) has \( 0 \le a_n \le 2/(n + 1) \), so \( \abs{a_n} < \varepsilon \) as soon as \( 1/(n + 1) < \varepsilon/2 \), and it tends to \( 0 \); yet its terms run \( 2, 0, 2/3, 0, 2/5, \dots \), up and down, hitting \( 0 \) at \( n = 1, 3, 5, \dots \).
:::

Two kinds of sequence get their own names, because they recur throughout the rest of the chapter.

::: {#def-null-sequence-ordered-field}
[Null Sequence]

A sequence \( (a_n) \) in \( F \) is **null** if \( a_n \to 0 \).
:::

::: {#def-bounded-sequence-ordered-field}
[Bounded Sequence]

A sequence \( (a_n) \) in \( F \) is **bounded** if **there exists** \( M \in F_{>0} \) with \( \abs{a_n} \le M \) **for every** \( n \in \nN \). Such an \( M \) is a **bound** for \( (a_n) \).
:::

**Examples.** In \( \nQ \), \( (1/(n + 1)) \) is null and bounded by \( 1 \); in every \( F \), \( ((-1)^n) \) is bounded by \( 1 \) and not null (@exm-first-sequences-ordered-field (d)); a constant sequence \( c \) is bounded by \( \abs{c} + 1 \), which is positive even when \( c = 0 \). **Non-example.** In \( \nQ \) the sequence \( (n) \) is not bounded: for any \( M \in \nQ_{>0} \), Archimedes (@thm-rationals-archimedean) gives \( n \in \nN \) with \( M < n = \abs{n} \). The bound is required to be positive only for convenience, so that we may divide by it; any \( M \ge 0 \) that works can be replaced by \( M + 1 \).

## Archimedes and the sequence 1/(n + 1)

In \( \nQ \), \( 1/(n + 1) \to 0 \) came straight from Archimedes. In a general ordered field, the two statements turn out to be the same.

::: {#prp-reciprocals-null-iff-archimedean}
[Archimedes as a Null Sequence]

The sequence \( \bigl( 1/((n + 1) \cdot 1_F) \bigr)_{n \in \nN} \) is null in \( F \) if and only if \( F \) is Archimedean.
:::

::: {.idea}
One direction is @prp-archimedean-reciprocal read as a limit. For the other, a field that is not Archimedean has an element \( x \) above every \( n \cdot 1_F \); then every \( 1/(n + 1) \) is at least \( 1/x \), and \( 1/x \) is a tolerance that is never met.
:::

::: {.proof}
\( (\Leftarrow) \) Let \( F \) be Archimedean and \( \varepsilon \in F_{>0} \). By @prp-archimedean-reciprocal there is \( N \in \nZ_{>0} \) (depending on \( \varepsilon \)) with \( 1/(m \cdot 1_F) < \varepsilon \) for every \( m \ge N \). For \( n \ge N \) also \( n + 1 \ge N \), so
\[
\Bigl\lvert \frac{1}{(n + 1) \cdot 1_F} - 0 \Bigr\rvert = \frac{1}{(n + 1) \cdot 1_F} < \varepsilon ,
\]
where the absolute value drops because the term is positive. So the sequence is null.

\( (\Rightarrow) \) We prove the contrapositive. Suppose \( F \) is not Archimedean. Negating @def-archimedean-ordered-field (@fd1:prp-bounded-quantifier-negation, and @prp-ordered-field-halves (a) for \( \neg(x < n \cdot 1_F) \iff x \ge n \cdot 1_F \)), there is \( x \in F \) with \( x \ge n \cdot 1_F \) for every \( n \in \nN \). In particular \( x \ge 1 \cdot 1_F = 1 > 0 \), so \( \varepsilon \coloneqq 1/x \in F_{>0} \) (@prp-reciprocal-order (a)). For every \( n \in \nN \), \( 0 < (n + 1) \cdot 1_F \le x \) (@prp-naturals-in-ordered-field (b)), so @prp-ordered-field-halves (c) gives
\[
\Bigl\lvert \frac{1}{(n + 1) \cdot 1_F} - 0 \Bigr\rvert = \frac{1}{(n + 1) \cdot 1_F} \ge \frac{1}{x} = \varepsilon .
\]
So for this \( \varepsilon \) no \( N \) works, even with \( n = N \), and the sequence is not null.
:::

So in \( \nQ(t) \), the field of @exm-rational-function-field, which is not Archimedean, \( 1/(n + 1) \) does not tend to \( 0 \): the tolerance \( 1/t \) is never met. In \( \nQ \), \( 1/(n + 1) \to 0 \) is @exm-first-sequences-ordered-field (b), which rests on the Archimedean property; every result proved without the Archimedean property holds in \( \nQ(t) \) as well.

::: {.remark}
The same example shows why tolerances must come from \( F \). In \( \nQ(t) \), every **rational** tolerance is eventually met by \( 1/(n + 1) \). Write \( \iota \) for the embedding \( \iota_F \) of @thm-rationals-embed-ordered-field. Since \( \iota \) respects products, \( \iota(1) = 1 \) and \( \iota(n + 1) = (n + 1) \cdot 1 \), we have \( ((n + 1) \cdot 1) \cdot \iota(1/(n + 1)) = \iota(1) = 1 \), so the term \( 1/((n + 1) \cdot 1) \) is \( \iota(1/(n + 1)) \). Given \( q \in \nQ_{>0} \), @exm-first-sequences-ordered-field (b) gives \( N \) with \( 1/(n + 1) < q \) in \( \nQ \) for every \( n \ge N \), and \( \iota \), being strictly increasing, carries this to \( \iota(1/(n + 1)) < \iota(q) \). Yet the sequence is not null in \( \nQ(t) \). For \( F = \nQ \) the two readings coincide, because there every tolerance is rational.
:::

## Changing finitely many terms

Whether a sequence converges, and to what, depends only on its terms from some point on. Two forms of this are used constantly: altering finitely many terms, and dropping the first \( k \).

::: {#prp-tail-change-ordered-field}
[Only the Tail Matters]

Let \( (a_n) \) and \( (b_n) \) be sequences in \( F \), and \( a \in F \).

::: {.enumerate options="label=(\alph*)"}
1. If there is \( N_0 \in \nN \) with \( a_n = b_n \) for every \( n \ge N_0 \), then \( a_n \to a \) if and only if \( b_n \to a \); in particular \( (a_n) \) is null if and only if \( (b_n) \) is; and \( (a_n) \) is bounded if and only if \( (b_n) \) is.
2. For \( k \in \nN \), the shifted sequence \( (a_{n+k})_{n \in \nN} \) converges to \( a \) if and only if \( (a_n) \) does.
:::
:::

::: {.idea}
For limits, a threshold for one sequence becomes a threshold for the other once it is pushed past \( N_0 \), or moved by \( k \). For bounds, the finitely many terms before \( N_0 \) are absorbed by a finite maximum.
:::

::: {.proof}
(a) *Limits.* Suppose \( a_n \to a \), and let \( \varepsilon \in F_{>0} \). Choose \( N \) with \( \abs{a_n - a} < \varepsilon \) for every \( n \ge N \), and let \( N' \coloneqq \max\{N, N_0\} \). For \( n \ge N' \), \( b_n = a_n \) and \( \abs{b_n - a} = \abs{a_n - a} < \varepsilon \). So \( b_n \to a \). The hypothesis is symmetric in the two sequences, so the converse follows by exchanging them. The case \( a = 0 \) is the statement about null sequences.

*Bounds.* Suppose \( \abs{a_n} \le M \) for every \( n \), with \( M \in F_{>0} \). If \( N_0 = 0 \), the two sequences are equal. Otherwise let
\[
M' \coloneqq \max\{ \abs{b_0}, \dots, \abs{b_{N_0 - 1}}, M \} ,
\]
the maximum of finitely many elements of \( F \), which exists by @fd2:prp-finite-max (its proof works in any ordered field, as *Sets and Functions*, Section 5.3 remarks). Then \( M' \ge M > 0 \). For \( n < N_0 \), \( \abs{b_n} \le M' \) because \( \abs{b_n} \) is one of the listed elements; for \( n \ge N_0 \), \( \abs{b_n} = \abs{a_n} \le M \le M' \). So \( M' \) bounds \( (b_n) \). The converse is the same with the sequences exchanged.

(b) Suppose \( a_n \to a \), and let \( \varepsilon \in F_{>0} \), with \( N \) as in the definition. For \( n \ge N \), also \( n + k \ge N \), so \( \abs{a_{n+k} - a} < \varepsilon \). Hence \( (a_{n+k})_n \) converges to \( a \), with the same \( N \).

Conversely, suppose \( a_{n+k} \to a \), and let \( \varepsilon \in F_{>0} \), with \( N \) such that \( \abs{a_{m+k} - a} < \varepsilon \) for every \( m \ge N \). Let \( n \ge N + k \). Then \( n = m + k \) for the natural number \( m \coloneqq n - k \), and \( m \ge N \) (@prp-omega-order-arithmetic (a), (c)). So \( \abs{a_n - a} = \abs{a_{m+k} - a} < \varepsilon \), and \( N + k \) is a threshold for \( (a_n) \). This proves the proposition.
:::

The shift clause is about convergence only; it is used to start a sequence later, for instance to read a formula such as \( 1/n \), which needs \( n \ge 1 \), as the shift by \( 1 \) of a sequence indexed from \( 0 \). Section 4.5 adds the Cauchy property to clause (a).

One more reformulation moves every limit to \( 0 \).

::: {#prp-limit-null-shift-ordered-field}
[Limits Through Null Sequences]

For a sequence \( (a_n) \) in \( F \) and \( a \in F \): \( a_n \to a \) if and only if the sequence \( (a_n - a) \) is null.
:::

::: {.proof}
For every \( n \), \( \abs{(a_n - a) - 0} = \abs{a_n - a} \). So the two conditions of @def-sequence-limit-ordered-field, for \( (a_n) \) with limit \( a \) and for \( (a_n - a) \) with limit \( 0 \), say word for word the same thing, with the same \( N \) for each \( \varepsilon \).
:::

## A sequence has at most one limit

If "the terms are eventually within every tolerance of \( a \)" is to name **the** number the sequence tends to, it must single out one \( a \). It does.

::: {#thm-limit-unique-ordered-field}
[Uniqueness of Limits]

Let \( (a_n) \) be a sequence in \( F \) and \( a, b \in F \). If \( a_n \to a \) and \( a_n \to b \), then \( a = b \).
:::

*Try it first (ten minutes): suppose \( a_n \to a \) and \( a_n \to b \) with \( a \ne b \). Which \( \varepsilon \) makes the two tails collide?*

::: {.idea}
The natural first choice is \( \varepsilon \coloneqq \abs{a - b} \), positive because \( a \ne b \); it is the choice that worked in @fd1:prp-arbitrarily-close-equal. Beyond both thresholds a term \( a_n \) is within \( \abs{a - b} \) of \( a \) and of \( b \), and the triangle inequality through \( a_n \) yields only \( \abs{a - b} < 2\abs{a - b} \): true, and no contradiction. The two tolerances **add**. So give each half: with \( \varepsilon \coloneqq \abs{a - b}/2 \), the same chain ends in \( \abs{a - b} < \abs{a - b} \).
:::

::: {.proof}
Let \( a_n \to a \) and \( a_n \to b \), and suppose, for a contradiction, that \( a \ne b \). Then \( a - b \ne 0 \), so \( \abs{a - b} > 0 \) (@prp-absolute-value-ordered-field (a)), and
\[
\varepsilon \coloneqq \frac{\abs{a - b}}{2} \in F_{>0}
\]
by @prp-ordered-field-halves (b); it depends only on \( a \) and \( b \). Since \( a_n \to a \), there is \( N_1 \) with \( \abs{a_n - a} < \varepsilon \) for every \( n \ge N_1 \); since \( a_n \to b \), there is \( N_2 \) with \( \abs{a_n - b} < \varepsilon \) for every \( n \ge N_2 \). Let \( n \coloneqq \max\{N_1, N_2\} \). Then both inequalities hold at this \( n \), and the three-point triangle inequality (@prp-absolute-value-ordered-field (e)), with \( \abs{a - a_n} = \abs{a_n - a} \) by part (b) of the same proposition, gives
\[
\abs{a - b} \le \abs{a - a_n} + \abs{a_n - b} < \varepsilon + \varepsilon = \abs{a - b} ,
\]
where the strict inequality is @prp-ordered-ring-rules (b) and the last equality is @prp-ordered-field-halves (b). So \( \abs{a - b} < \abs{a - b} \), against (O1). Hence the assumption \( a \ne b \) is refuted, and \( a = b \) (@fd1:def-rule-raa).
:::

::: {.remark}
This is the argument of @fd1:prp-arbitrarily-close-equal, rerun in \( F \). There a hypothesis valid for **every** \( \varepsilon \) was fed the one \( \varepsilon \) that makes the numbers collide. Here the two hypotheses give \( \abs{a - b} < 2\varepsilon \) for every \( \varepsilon \in F_{>0} \), and the colliding choice is \( \abs{a - b}/2 \). The facts about the absolute value that the old argument took from school are now @prp-absolute-value-ordered-field, valid in every ordered field.
:::

Since a convergent sequence has exactly one limit, we may speak of **the** limit and write it \( \lim a_n \), or \( \lim_{n \to \infty} a_n \). So \( \lim a_n = a \) means the same as \( a_n \to a \). In \( \nQ \), @exm-first-sequences-ordered-field gives \( \lim 1/(n + 1) = 0 \) and \( \lim (n + 1)/(n + 2) = 1 \), while \( \lim (-1)^n \) names nothing.

## Convergent sequences are bounded

A convergent sequence cannot run off: from some index on, its terms are trapped near the limit, and only finitely many terms come before that index.

::: {#prp-convergent-bounded-ordered-field}
[Convergent Sequences Are Bounded]

Every convergent sequence in \( F \) is bounded.
:::

::: {.idea}
Use the definition once, with the tolerance \( 1 \): from some \( N \) on, \( \abs{a_n} \le \abs{a_n - a} + \abs{a} < 1 + \abs{a} \). The terms before \( N \) are finitely many, so one of them, or \( \abs{a} + 1 \), is the largest absolute value in sight.
:::

::: {.proof}
Let \( a_n \to a \). Applying @def-sequence-limit-ordered-field with \( \varepsilon \coloneqq 1 \in F_{>0} \) gives \( N \in \nN \) with \( \abs{a_n - a} < 1 \) for every \( n \ge N \). For such \( n \), the triangle inequality (@prp-absolute-value-ordered-field (e), with \( x = a_n - a \) and \( y = a \)) gives
\[
\abs{a_n} = \abs{(a_n - a) + a} \le \abs{a_n - a} + \abs{a} < 1 + \abs{a} .
\]
If \( N = 0 \), let \( M \coloneqq \abs{a} + 1 \). Otherwise let
\[
M \coloneqq \max\{ \abs{a_0}, \dots, \abs{a_{N-1}}, \abs{a} + 1 \} ,
\]
which exists by @fd2:prp-finite-max in the totally ordered \( F \) (as in the proof of @prp-tail-change-ordered-field). In both cases \( M \ge \abs{a} + 1 \ge 1 > 0 \), by @prp-absolute-value-ordered-field (a), so \( M \in F_{>0} \). For \( n < N \), \( \abs{a_n} \le M \) because \( \abs{a_n} \) is one of the listed elements; for \( n \ge N \), \( \abs{a_n} < \abs{a} + 1 \le M \). So \( M \) bounds \( (a_n) \).
:::

The bound \( M \) depends on the whole sequence, through \( a \), \( N \) and the first \( N \) terms, but on no tolerance: it is one element of \( F \), fixed once. Section 4.4 uses exactly that, in the product of two limits. The converse fails: \( ((-1)^n) \) is bounded by \( 1 \) and divergent (@exm-first-sequences-ordered-field (d)).

## Exercises

### A. Check your understanding

::: {#exr-limits-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Write "\( a_n \not\to a \)" in symbols, and name the law used at each step.
2. What does \( \exists N \in \nN \ \forall \varepsilon \in F_{>0} \ \forall n \in \nN \ \bigl( n \ge N \Rightarrow \abs{a_n - a} < \varepsilon \bigr) \) say about \( (a_n) \)? Does \( (1/(n + 1)) \) satisfy it in \( \nQ \), with \( a = 0 \)?
3. For \( a_n = (2n + 1)/(n + 1) \) in \( \nQ \), find the least \( N \) that works in @def-sequence-limit-ordered-field for the limit \( 2 \) and \( \varepsilon = 1/50 \).
:::
:::

::: {.solution}
(a) Start from \( \neg \forall \varepsilon \in F_{>0} \ \exists N \in \nN \ \forall n \in \nN \ (n \ge N \Rightarrow \abs{a_n - a} < \varepsilon) \). The bounded negation laws (@fd1:prp-bounded-quantifier-negation (a), then (b), then (a)) move \( \neg \) past the three quantifiers, turning each \( \forall \) into \( \exists \) and the \( \exists \) into \( \forall \). That leaves \( \neg(n \ge N \Rightarrow \abs{a_n - a} < \varepsilon) \), which is \( n \ge N \wedge \neg(\abs{a_n - a} < \varepsilon) \) by @fd1:prp-negated-implication. Finally \( \neg(\abs{a_n - a} < \varepsilon) \) is \( \abs{a_n - a} \ge \varepsilon \), by trichotomy in \( F \) (@prp-ordered-field-halves (a)). The result:
\[
\exists \varepsilon \in F_{>0} \ \ \forall N \in \nN \ \ \exists n \in \nN \ \ \bigl( n \ge N \wedge \abs{a_n - a} \ge \varepsilon \bigr) .
\]

(b) It says that \( a_n = a \) for every \( n \ge N \): the sequence is eventually constant, equal to \( a \). Indeed, fix \( n \ge N \). Then \( \abs{a_n - a} < \varepsilon \) for every \( \varepsilon \in F_{>0} \). If \( a_n \ne a \), then \( \varepsilon \coloneqq \abs{a_n - a} \) is in \( F_{>0} \) (@prp-absolute-value-ordered-field (a)) and gives \( \abs{a_n - a} < \abs{a_n - a} \), against (O1); so \( a_n = a \). This is the argument of @fd1:prp-arbitrarily-close-equal, rerun in \( F \) for one \( n \) at a time (no halving is needed: only one tolerance is in play). Conversely, an eventually constant sequence satisfies the formula, since \( \abs{0} = 0 < \varepsilon \). The sequence \( (1/(n + 1)) \) does not satisfy it: no term equals \( 0 \). It converges to \( 0 \), but its \( N \) must depend on \( \varepsilon \). The quantifier order is the whole difference.

(c) \( a_n - 2 = \bigl( 2n + 1 - 2(n + 1) \bigr)/(n + 1) = -1/(n + 1) \), so \( \abs{a_n - 2} = 1/(n + 1) \). By the comparison formula, \( 1/(n + 1) < 1/50 \) if and only if \( n + 1 > 50 \), that is, \( n \ge 50 \). So \( N = 50 \) works, and every \( N \le 49 \) fails at \( n = 49 \) (which is \( \ge N \)), where \( \abs{a_{49} - 2} = 1/50 \). The least \( N \) is \( 50 \).
:::

### B. Practice

::: {#exr-limits-b1}
[B1]

Prove from @def-sequence-limit-ordered-field that, in \( \nQ \),
\[
\frac{2n + 1}{n + 1} \to 2 \qquad \text{and} \qquad \frac{n^2 + 1}{2n^2 + 3} \to \frac{1}{2} .
\]
Say exactly where the Archimedean property is used.
:::

::: {.solution}
*First limit.* As in A1 (c), \( \abs{(2n + 1)/(n + 1) - 2} = 1/(n + 1) \). Let \( \varepsilon \in \nQ_{>0} \). Since \( \nQ \) is Archimedean (@thm-rationals-archimedean), @prp-archimedean-reciprocal gives \( N \in \nZ_{>0} \), depending on \( \varepsilon \), with \( 1/m < \varepsilon \) for every \( m \ge N \). For \( n \ge N \), \( n + 1 \ge N \), so the distance \( 1/(n + 1) \) is \( < \varepsilon \).

*Second limit.* Bring the difference to one fraction:
\[
\frac{n^2 + 1}{2n^2 + 3} - \frac{1}{2} = \frac{2(n^2 + 1) - (2n^2 + 3)}{2(2n^2 + 3)} = \frac{-1}{2(2n^2 + 3)} ,
\]
so the distance is \( 1/(2(2n^2 + 3)) \). We bound it by \( 1/(n + 1) \). For \( n \ge 1 \), \( n^2 = n \cdot n \ge n \cdot 1 = n \) (@prp-ordered-field-halves (d), applied to \( 0 \le 1 \le n \) and \( 0 \le n \le n \)), so
\[
2(2n^2 + 3) - (n + 1) = 4n^2 - n + 5 \ge 3n + 5 > 0 ;
\]
for \( n = 0 \) the left side is \( 5 > 0 \). So \( 0 < n + 1 < 2(2n^2 + 3) \), and @prp-ordered-field-halves (c) gives \( 1/(2(2n^2 + 3)) \le 1/(n + 1) \). With the \( N \) of the first part, every \( n \ge N \) has distance \( \le 1/(n + 1) < \varepsilon \).

*Where Archimedes is used.* Only in obtaining \( N \) from \( \varepsilon \), through @prp-archimedean-reciprocal. The algebra of the distances holds in any ordered field. In \( \nQ(t) \) the same algebra gives the same distances, and the proofs fail exactly there: both take \( N \) from \( 1/(n + 1) < \varepsilon \), and by the proof of @prp-reciprocals-null-iff-archimedean with \( x = t \) (@exm-rational-function-field) no \( N \) makes \( 1/(n + 1) < 1/t \) for all \( n \ge N \).
:::

::: {#exr-limits-b2}
[B2]

Prove that if \( a_n \to a \) in \( F \), then \( \abs{a_n} \to \abs{a} \). Show by an example that the converse fails, and prove that it holds when \( a = 0 \).
:::

::: {.solution}
Let \( \varepsilon \in F_{>0} \), and choose \( N \) with \( \abs{a_n - a} < \varepsilon \) for \( n \ge N \). By the reverse triangle inequality (@prp-absolute-value-ordered-field (f)), for \( n \ge N \),
\[
\bigl\lvert \abs{a_n} - \abs{a} \bigr\rvert \le \abs{a_n - a} < \varepsilon .
\]
So \( \abs{a_n} \to \abs{a} \), with the same \( N \).

The converse fails for \( a_n = (-1)^n \) and \( a = 1 \): \( \abs{a_n} = 1 \) for every \( n \), a constant sequence, so \( \abs{a_n} \to 1 = \abs{1} \) (@exm-first-sequences-ordered-field (a)); but \( (a_n) \) converges to nothing (part (d) of that example).

For \( a = 0 \) the converse holds: \( \bigl\lvert \abs{a_n} - \abs{0} \bigr\rvert = \bigl\lvert \abs{a_n} \bigr\rvert = \abs{a_n} = \abs{a_n - 0} \), by @prp-absolute-value-ordered-field (a), since \( \abs{a_n} \ge 0 \). So the two conditions coincide: a sequence is null if and only if its absolute values form a null sequence.
:::

::: {#exr-limits-b3}
[B3: Bounded but not convergent, in \( \nQ(t) \)]

In the field \( \nQ(t) \) of @exm-rational-function-field, show that the sequence \( (n \cdot 1)_{n \in \nN} \) is bounded and does not converge. Is \( (n) \) bounded in \( \nQ \)?
:::

::: {.solution}
*Bounded.* By @exm-rational-function-field, \( t > n \cdot 1 \) for every \( n \in \nN \). Also \( n \cdot 1 \ge 0 \) (@prp-naturals-in-ordered-field (b), and \( 0 \cdot 1 = 0 \)), so \( \abs{n \cdot 1} = n \cdot 1 < t \). And \( t > 1 \cdot 1 = 1 > 0 \), so \( M \coloneqq t \in \nQ(t)_{>0} \) is a bound.

*Not convergent.* Suppose \( n \cdot 1 \to a \) for some \( a \in \nQ(t) \). Take \( \varepsilon \coloneqq 1/2 \), which is positive (@prp-ordered-field-halves (b)), and its \( N \). With \( n \coloneqq N \), both \( n \) and \( n + 1 \) are \( \ge N \), and \( (n + 1) \cdot 1 - n \cdot 1 = 1 \) by @def-naturals-in-ordered-field (a). The three-point triangle inequality gives
\[
1 = \abs{(n + 1) \cdot 1 - n \cdot 1} \le \abs{(n + 1) \cdot 1 - a} + \abs{a - n \cdot 1} < \tfrac12 + \tfrac12 = 1 ,
\]
against (O1). So the sequence diverges.

*In \( \nQ \).* No: by the non-example after @def-bounded-sequence-ordered-field, Archimedes puts some \( n \) above any proposed bound. The same sequence is bounded in one field and unbounded in another. Boundedness is a property of the sequence **in** \( F \), like convergence.
:::

### C. Going deeper

::: {#exr-limits-c1}
[C1: A positive limit keeps the terms positive]

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( a_n \to a \) in \( F \) and \( a > 0 \), then \( a_n > a/2 \) eventually; in particular \( a_n > 0 \) eventually.
2. Give a sequence in \( \nQ \) with \( a_n > 0 \) for every \( n \) whose limit is not positive. What does this say about the converse of (a)?
:::
:::

::: {.solution}
(a) Let \( \varepsilon \coloneqq a/2 \), which lies in \( F_{>0} \) by @prp-ordered-field-halves (b), since \( a > 0 \). Choose \( N \) with \( \abs{a_n - a} < a/2 \) for every \( n \ge N \). By @prp-absolute-value-ordered-field (d), for such \( n \),
\[
a_n > a - \frac{a}{2} = \frac{a}{2} > 0 ,
\]
where \( a - a/2 = a/2 \) because \( a/2 + a/2 = a \) (@prp-ordered-field-halves (b)). So \( a_n > a/2 \) for every \( n \ge N \).

(b) \( a_n = 1/(n + 1) \): every term is positive, and the limit is \( 0 \) (@exm-first-sequences-ordered-field (b)). So "every term positive" does not give "limit positive": the strict inequality is lost in the limit. What survives is the weak inequality \( a \ge 0 \), proved in Section 4.4.
:::

::: {#exr-limits-c2}
[C2: Find the error]

Here is an argument for @prp-convergent-bounded-ordered-field. Is the conclusion true? Is the argument correct? If not, name the line that fails, say what makes it illegal, and give a counterexample to the step. Then repair the argument.

> (1) Let \( a_n \to a \). (2) Take \( \varepsilon \coloneqq 1 \) in the definition of the limit, and let \( N \) be the index it provides. (3) Then for every \( n \in \nN \), \( \abs{a_n} \le \abs{a_n - a} + \abs{a} < 1 + \abs{a} \). (4) So \( M \coloneqq 1 + \abs{a} \) is a bound for \( (a_n) \).
:::

::: {.solution}
The conclusion is **true**: it is @prp-convergent-bounded-ordered-field. The argument is **not** correct.

*The failing line is (3).* The first inequality is the triangle inequality and is fine. The second uses \( \abs{a_n - a} < 1 \) "for every \( n \in \nN \)". Line (2) supplies it only for \( n \ge N \): it is the bounded universal \( \forall n \in \nN \, (n \ge N \Rightarrow \abs{a_n - a} < 1) \). Instantiating it at \( n \) needs the line \( n \ge N \) (bounded \( \rulename{\forall E} \), @fd1:prp-bounded-quantifier-rules), and for \( n < N \) no such line is available. Line (3) cites a line that is not there: entry (N9) of @fd1:exm-not-allowed-catalogue.

*Counterexample to the step.* In \( \nQ \), let \( a_0 \coloneqq 5 \) and \( a_n \coloneqq 0 \) for \( n \ge 1 \), with \( a = 0 \). Then \( a_n \to 0 \), and \( N = 1 \) is a legitimate choice in line (2) for \( \varepsilon = 1 \), since \( \abs{a_n - 0} = 0 < 1 \) for \( n \ge 1 \). At \( n = 0 \), line (3) claims \( \abs{a_0} < 1 + \abs{0} = 1 \), but \( \abs{a_0} = 5 \); and the \( M = 1 \) of line (4) is not a bound. No counterexample to the conclusion exists: \( 5 \) is a bound.

*Repair.* Keep line (3) for \( n \ge N \) only, and take \( M \coloneqq \max\{ \abs{a_0}, \dots, \abs{a_{N-1}}, \abs{a} + 1 \} \), the finite maximum of the proof of @prp-convergent-bounded-ordered-field.

**Marking scheme.** (10 points)
- 2: says that the conclusion is true and the argument is not correct.
- 3: names line (3) and the use of \( \abs{a_n - a} < 1 \) for \( n < N \), where the hypothesis does not apply (bounded \( \forall \) used outside its range; entry (N9)).
- 3: gives a convergent sequence and a legitimate \( N \) for which the step's inequality fails at some \( n < N \), and checks it.
- 2: repairs the argument with a finite maximum over the terms before \( N \).
Fatal errors (0 for the step): declaring the conclusion false; offering a counterexample to the conclusion; blaming the triangle inequality.
:::

<!-- dependency ledger
def-sequence-ordered-field (claim): max{N0, N1} exists for N0, N1 in N | thm-omega-order (a) (cited)
def-sequence-ordered-field (example): (-1)^n fails "= 1" at every odd n | (-1)^{n+1} = -(-1)^n from the recursion of def-naturals-in-ordered-field and prp-ring-algebra (c); the odd indices 1, 3, 5, ... by (-1)^{n+2} = (-1)^n; verify/ch04/def-sequence-limit-ordered-field.py
def-sequence-limit-ordered-field (claim): 1 - (n+1)/(n+2) = 1/(n+2), 2 - (n+1)/(n+2) = 1 + 1/(n+2) | lem-field-fraction-rules (b), (c); verify/ch04/def-sequence-limit-ordered-field.py
def-sequence-limit-ordered-field (claim): not(x < eps) iff x >= eps | prp-ordered-field-halves (a) (cited)
def-sequence-limit-ordered-field (claim): (1 + (-1)^n)/(n + 1) lies in [0, 2/(n+1)], is 0 at odd n and is null | (-1)^n in {1, -1} as in exm-first-sequences-ordered-field (d); null via the bound 2/(n+1) and prp-archimedean-reciprocal (the squeeze itself is §04, so the claim is checked directly from the definition); verify/ch04/def-sequence-limit-ordered-field.py
exm-first-sequences-ordered-field (solution): |(-1)^n| = 1 for every n, by induction | fd1:ax-induction via cor-omega-identification (b) with prp-absolute-value-ordered-field (b); inline
exm-first-sequences-ordered-field (solution): -2 a_n = a_{n+1} - a_n and |-2 a_n| = 2|a_n| | prp-ring-algebra (c), prp-absolute-value-ordered-field (b), |2| = 2 since 2 > 0 (prp-ordered-field-halves (b))
exm-first-sequences-ordered-field (solution): n + 2 > n + 1 >= N in N, so (b)'s bound 1/m < eps applies at m = n + 2 | prp-omega-order-arithmetic (c), thm-omega-order (a)
exm-first-sequences-ordered-field (solution): Q is Archimedean in the sense of def-archimedean-ordered-field | thm-rationals-archimedean with prp-naturals-in-ordered-field (d), as §02 records after def-archimedean-ordered-field
def-bounded-sequence-ordered-field (example): Q is Archimedean, so (n) is unbounded in Q | thm-rationals-archimedean (cited)
def-bounded-sequence-ordered-field (example): |c| + 1 > 0 | prp-absolute-value-ordered-field (a), prp-ordered-ring-rules (b), (e)
prp-reciprocals-null-iff-archimedean (proof): negation of def-archimedean-ordered-field; not(x < n 1_F) iff x >= n 1_F | fd1:prp-bounded-quantifier-negation (cited), prp-ordered-field-halves (a)
prp-reciprocals-null-iff-archimedean (claim): Q(t) is not Archimedean (t > n 1 for every n) | exm-rational-function-field: school fact; formal polynomials in F5.4 (flagged; nothing in fd3 depends on it, and no proof here cites it)
prp-reciprocals-null-iff-archimedean (claim): (the remark after it) 1/(n+1) in Q(t) is iota(1/(n+1)) (iota respects products, iota(1) = 1), and 1/(n+1) < q eventually in Q, carried over by iota | thm-rationals-embed-ordered-field, exm-first-sequences-ordered-field (b) (cited); Q(t) as above, school fact; formal polynomials in F5.4
prp-tail-change-ordered-field (proof): finite maximum of elements of F | fd2:prp-finite-max (stated for reals; its proof works in any ordered field, fd2 Section 3.3, prose remark after prp-greatest-maximal)
prp-convergent-bounded-ordered-field (proof): finite maximum of elements of F | fd2:prp-finite-max (stated for reals; its proof works in any ordered field, fd2 Section 3.3, prose remark after prp-greatest-maximal), as in prp-tail-change-ordered-field (proof)
prp-tail-change-ordered-field (proof): n >= N gives n + k >= N; n >= N + k gives n = m + k with m >= N | prp-omega-order-arithmetic (a), (c) (cited)
thm-limit-unique-ordered-field (proof): a != b gives a - b != 0 | (F4), prp-ring-algebra (a)
thm-limit-unique-ordered-field (proof): max{N1, N2} exists in N | thm-omega-order (a); the same in prp-tail-change-ordered-field (proof)
exr-limits-a1 (solution): (2n + 1)/(n + 1) - 2 = -1/(n + 1); the least N is 50 | verify/ch04/exr-limits-a1.py
exr-limits-b1 (solution): the distance 1/(2(2n^2 + 3)) and 4n^2 - n + 5 >= 3n + 5 for n >= 1 | verify/ch04/exr-limits-b1.py
exr-limits-b1 (solution): in Q(t), 1/(n+1) >= 1/t for every n, so no N meets the tolerance 1/t | proof of prp-reciprocals-null-iff-archimedean ((=>) direction, x = t), exm-rational-function-field: school fact; formal polynomials in F5.4 (flagged)
exr-limits-b3 (solution): t > n 1 for every n in Q(t) | exm-rational-function-field: school fact; formal polynomials in F5.4 (flagged)
exr-limits-b3 (solution): (n + 1) 1 - n 1 = 1 | def-naturals-in-ordered-field (a) (cited)
exr-limits-c1 (solution): the weak inequality a >= 0 survives limits | prp-limit-preserves-order-ordered-field (b), Section 4.4 (prose pointer; the solution does not use it)
exr-limits-c2 (solution): the counterexample a_0 = 5, a_n = 0 | verify/ch04/exr-limits-c2.py
-->
