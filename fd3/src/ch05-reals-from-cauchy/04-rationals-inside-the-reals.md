# The Rationals Inside the Reals

<!-- S3: rewrite per blueprint (layout-proposal.md §3, 5.4, pipeline F): density in one line (@thm-rationals-dense-ordered-field plus Archimedes), the direct proof becomes an exercise; cor-rational-epsilon-suffices and thm-terms-converge-to-class become exercises (labels kept). -->

Section 5.3 made \( \nR \) an ordered field. We built it to enlarge \( \nQ \), but so far \( \nQ \) is not inside it: a rational number is a class of pairs of integers, and a real number is a class of Cauchy sequences. This section places a copy of \( \nQ \) in \( \nR \) and shows how the copy sits there. It is preserved by all the operations and the order; it is spread through \( \nR \) without gaps, so that between any two real numbers there is a rational one; and every real number is the limit of rationals. Along the way we prove that \( \nR \) is Archimedean and that rational tolerances suffice for limits in \( \nR \). At the end we meet the number that Chapter 4 promised: a positive real whose square is \( 2 \).

Notation is as in Section 5.3: \( \sC \) is the set of Cauchy sequences of rationals, \( [a] \) is the class of \( a \in \sC \), \( (q)_n \) is the constant sequence with value \( q \), \( P = \nR_{>0} \) is the set of positive reals, and \( x < y \) means \( y - x \in P \) (@def-reals-order). By @thm-reals-ordered-field, the results of Chapters 2 and 4 for an arbitrary ordered field apply with \( F = \nR \); we say "in \( \nR \)" where the context does not make the field clear.

## A copy of the rationals

Section 5.2 already represented each rational \( q \) by the class of its constant sequence, as Chapter 4 said it would. We make that a map.

::: {#def-rational-embedding}
[The Rationals in the Reals]

For \( q \in \nQ \), let
\[
\kappa(q) \coloneqq [(q)_n] \in \nR ,
\]
the class of the constant sequence with value \( q \). This defines a function \( \kappa \colon \nQ \to \nR \).
:::

The right side is in \( \nR \) because constant sequences are Cauchy (@thm-cauchy-algebra-ordered-field (a)), and \( \kappa \) is a function because each \( q \) determines one constant sequence and that sequence one class. In this notation \( 0_{\nR} = \kappa(0) \) and \( 1_{\nR} = \kappa(1) \) (@def-reals-operations). The letter \( \kappa \) is new on purpose: Chapter 2 used \( \iota \) and \( j \) for \( \nN \to \nZ \to \nQ \), and Chapter 4 wrote \( \iota_F \) for the copy of \( \nQ \) in an ordered field \( F \). Part (d) of the next theorem shows that \( \kappa \) is \( \iota_{\nR} \).

The theorem says that \( \kappa \) carries everything we know how to do with rationals into \( \nR \) without change: sums, products, negatives, reciprocals, the order and the absolute value.

::: {#thm-rational-embedding}
[The Rationals Embed in the Reals]

For all \( q, s \in \nQ \):

::: {.enumerate options="label=(\alph*)"}
1. \( \kappa(q + s) = \kappa(q) + \kappa(s) \), \( \kappa(qs) = \kappa(q) \kappa(s) \), \( \kappa(0) = 0_{\nR} \) and \( \kappa(1) = 1_{\nR} \);
2. \( q < s \) if and only if \( \kappa(q) < \kappa(s) \); hence \( \kappa \) is injective;
3. \( \kappa(-q) = -\kappa(q) \), \( \kappa(\abs{q}) = \abs{\kappa(q)} \), and, if \( q \ne 0 \), \( \kappa(q) \ne 0_{\nR} \) and \( \kappa(1/q) = \kappa(q)^{-1} \);
4. \( \kappa \) is the map \( \iota_{\nR} \) of @thm-rationals-embed-ordered-field for the ordered field \( F = \nR \); in particular \( \kappa(n) = n \cdot 1_{\nR} \) for every \( n \in \nN \) (@def-naturals-in-ordered-field).
:::
:::

::: {.idea}
Constant sequences add, multiply and negate termwise into constant sequences, so (a) and the first identity of (c) are the definitions of the operations. For (b), the difference of two constant sequences is constant, and a constant \( s - q > 0 \) is its own margin. The rest is algebra in a field: the absolute value by cases, reciprocals by uniqueness of inverses, and (d) by the uniqueness clause of Chapter 4's embedding theorem.
:::

::: {.proof}
(a) By @def-reals-operations, \( \kappa(q) + \kappa(s) = [(q)_n + (s)_n] = [(q + s)_n] = \kappa(q + s) \), since the termwise sum of two constant sequences is the constant sequence of the sum. The product is the same with \( \cdot \) in place of \( + \). The last two identities are the definitions of \( 0_{\nR} \) and \( 1_{\nR} \).

(c), first identity. By @def-reals-operations, \( -\kappa(q) = [-(q)_n] = [(-q)_n] = \kappa(-q) \).

(b) \( (\Rightarrow) \) Let \( q < s \). By (a) and the first identity of (c), \( \kappa(s) - \kappa(q) = \kappa(s) + \kappa(-q) = \kappa(s - q) = [(s - q)_n] \). The constant \( s - q \) lies in \( \nQ_{>0} \) (@prp-ordered-ring-rules (a)), so the constant sequence \( (s - q)_n \) is positive, with margin \( \delta = s - q \) and threshold \( N = 0 \) (@def-positive-cauchy-sequence). Hence \( \kappa(s) - \kappa(q) \in P \), that is, \( \kappa(q) < \kappa(s) \).

\( (\Leftarrow) \) Let \( \kappa(q) < \kappa(s) \). By trichotomy in \( \nQ \), \( q < s \), \( q = s \) or \( s < q \). If \( q = s \), then \( \kappa(q) = \kappa(s) \); if \( s < q \), then \( \kappa(s) < \kappa(q) \) by \( (\Rightarrow) \). Either contradicts \( \kappa(q) < \kappa(s) \) by (O1) in \( \nR \) (@thm-reals-ordered-field). So \( q < s \).

Injectivity: if \( q \ne s \), then \( q < s \) or \( s < q \), so \( \kappa(q) < \kappa(s) \) or \( \kappa(s) < \kappa(q) \), and in either case \( \kappa(q) \ne \kappa(s) \) by (O1).

(c), the rest. If \( q > 0 \), then \( \kappa(q) > \kappa(0) = 0_{\nR} \) by (b), so \( \abs{\kappa(q)} = \kappa(q) = \kappa(\abs{q}) \) (@def-absolute-value-ordered-field, in \( \nR \) and in \( \nQ \)). If \( q = 0 \), both sides are \( 0_{\nR} \). If \( q < 0 \), then \( \kappa(q) < 0_{\nR} \) by (b), so \( \abs{\kappa(q)} = -\kappa(q) = \kappa(-q) = \kappa(\abs{q}) \). Now let \( q \ne 0 \). Then \( \kappa(q) \ne \kappa(0) = 0_{\nR} \) by injectivity, and by (a),
\[
\kappa(q) \, \kappa(1/q) = \kappa(q \cdot (1/q)) = \kappa(1) = 1_{\nR} .
\]
In the field \( \nR \) (@thm-reals-field), the inverse of \( \kappa(q) \) is the only element with this property (@lem-field-fraction-rules (a)), so \( \kappa(1/q) = \kappa(q)^{-1} \).

(d) By @thm-reals-ordered-field, \( \nR \) is an ordered field, so @thm-rationals-embed-ordered-field gives **exactly one** map \( \iota_{\nR} \colon \nQ \to \nR \) with \( \iota_{\nR}(1) = 1_{\nR} \) that preserves sums and products. By (a), \( \kappa \) is such a map, so \( \kappa = \iota_{\nR} \). The same theorem states that \( \iota_{\nR}(n) = n \cdot 1_{\nR} \) for every \( n \in \nN \).
:::

By (d), part (b) and the injectivity of \( \kappa \) are also part of @thm-rationals-embed-ordered-field with \( F = \nR \), and (d) needs only (a). The direct proof of (b) is kept because it shows how a constant sequence is positive, with its own value as margin.

Two more identities follow from (a) and (c):
\[
\begin{aligned}
\kappa(q - s) &= \kappa(q) + \kappa(-s) = \kappa(q) - \kappa(s) , \\
\kappa(q/s) &= \kappa(q) \, \kappa(1/s) = \kappa(q)/\kappa(s) \quad \text{for } s \ne 0 .
\end{aligned}
\]
So any computation with rationals, done in \( \nQ \) and then moved into \( \nR \) by \( \kappa \), gives the same answer as the computation done in \( \nR \) on the images. Part (b) adds that comparisons agree too.

## Archimedes in the reals

Chapter 4 showed that an ordered field need not be Archimedean: in \( \nQ(t) \) the element \( t \) is larger than every \( n \cdot 1 \) (@exm-rational-function-field). So the Archimedean property of \( \nR \) has to be proved. It comes from \( \nQ \), through the fact that a Cauchy sequence is bounded.

::: {#thm-constructed-reals-archimedean}
[The Reals Are Archimedean]

\( \nR \) is an Archimedean ordered field (@def-archimedean-ordered-field): for every \( x \in \nR \) there is \( n \in \nN \) with \( x < n \cdot 1_{\nR} \).
:::

::: {.idea}
A representative of \( x \) is a Cauchy sequence of rationals, so all its terms lie below one rational bound \( M \). Archimedes in \( \nQ \) puts a natural number above \( M \); one more unit gives a fixed margin above every term, and a fixed margin is what positivity asks for.
:::

::: {.proof}
Let \( x \in \nR \), and write \( x = [a] \) with \( a \in \sC \). By @prp-cauchy-bounded-ordered-field with \( F = \nQ \), there is \( M \in \nQ_{>0} \) with \( \abs{a_k} \le M \) for every \( k \in \nN \). By @thm-rationals-archimedean, there is \( n \in \nN \) with \( M < n \). For every \( k \),
\[
(n + 1) - a_k \ge (n + 1) - M = (n - M) + 1 > 1 ,
\]
since \( a_k \le \abs{a_k} \le M \) (@prp-absolute-value-ordered-field (c)), so \( -M \le -a_k \) and then \( (n + 1) - a_k \ge (n + 1) - M \) (@prp-ordered-ring-rules (a), (b)), and \( n - M > 0 \). So the sequence \( ((n + 1) - a_k)_k \) is positive, with margin \( 1 \) and threshold \( 0 \). It represents \( \kappa(n + 1) - x \), by @def-reals-operations. Hence \( x < \kappa(n + 1) \), and \( \kappa(n + 1) = (n + 1) \cdot 1_{\nR} \) by @thm-rational-embedding (d). Since \( n + 1 \in \nN \), this proves the theorem.
:::

Every result of Chapter 4 about Archimedean ordered fields now applies with \( F = \nR \). Two of them are used at once.

**The integer part in \( \nR \).** By @prp-integer-part-ordered-field with \( F = \nR \), and \( \iota_{\nR} = \kappa \) (@thm-rational-embedding (d)), for every \( x \in \nR \) there is **exactly one** \( m \in \nZ \) with
\[
\kappa(m) \le x < \kappa(m + 1) .
\]
We call \( m \) the **integer part** of \( x \). For a rational \( q \), the integer part of \( \kappa(q) \) is the integer part \( \floor{q} \) of @prp-rational-integer-part, because \( \kappa \) preserves and reflects \( \le \) (@thm-rational-embedding (b)). The word "exactly" matters: Section 5.5 builds a sequence by taking integer parts, and uniqueness is what makes that a rule rather than a choice.

The second consequence, @prp-archimedean-reciprocal in \( \nR \), turns into the statement that rational tolerances suffice; it comes after the density theorem.

## Between two reals there is a rational

::: {#thm-constructed-rationals-dense}
[The Rationals Are Dense in the Reals]

Let \( x, y \in \nR \) with \( x < y \). Then there is \( q \in \nQ \) with \( x < \kappa(q) < y \).
:::

*Try it first (ten minutes): write \( x = [a] \) and \( y = [b] \). Which rational would you put between them? Build it from the terms of \( a \) and \( b \), and say how far out you must go.*

::: {.idea}
The obvious attempt takes a rational between \( a_n \) and \( b_n \), say their midpoint, and has to say **which** \( n \). An early index is no good: \( a_0 \) may be larger than \( b_0 \), since early terms are irrelevant to the classes. Even where \( a_n < b_n \), a later term \( a_m \) may climb past the midpoint, and the midpoint must sit above **every** late \( a_m \) by a fixed margin.

So go far out, in two ways. Since \( y - x \) is positive, from some index on \( b_n - a_n \ge \delta \), a fixed rational gap. Since \( a \) and \( b \) are Cauchy, from some index \( N \) on all their terms stay within \( \delta/4 \) of \( a_N \) and of \( b_N \), respectively. The midpoint \( q \) of \( a_N \) and \( b_N \) is at least \( \delta/2 \) above \( a_N \); every later \( a_n \) is less than \( \delta/4 \) above \( a_N \); so \( q \) beats every later \( a_n \) by more than \( \delta/4 \). The same holds below \( b_n \).
:::

::: {.proof}
Write \( x = [a] \) and \( y = [b] \) with \( a, b \in \sC \). By @def-reals-order, \( y - x = [b - a] \in P \), so \( b - a \) is positive (@prp-positivity-well-defined). Fix \( \delta \in \nQ_{>0} \) and \( N_1 \in \nN \) with
\[
b_n - a_n \ge \delta \quad \text{for every } n \ge N_1
\]
\( [\rulename{\exists E}] \) (@fd1:def-rules-existential). Then \( \delta/4 = (\delta/2)/2 \in \nQ_{>0} \) (@prp-ordered-field-halves (b), twice). Since \( a \) and \( b \) are Cauchy in \( \nQ \), fix \( N_2 \) with \( \abs{a_m - a_n} < \delta/4 \) for all \( m, n \ge N_2 \), and \( N_3 \) with \( \abs{b_m - b_n} < \delta/4 \) for all \( m, n \ge N_3 \) \( [\rulename{\exists E}] \). Let
\[
N \coloneqq \max\{N_1, N_2, N_3\} , \qquad q \coloneqq \frac{a_N + b_N}{2} \in \nQ .
\]
Let \( n \ge N \). Expanding the right sides shows
\[
\begin{aligned}
q - a_n &= (a_N - a_n) + \frac{b_N - a_N}{2} , \\
b_n - q &= (b_n - b_N) + \frac{b_N - a_N}{2} .
\end{aligned}
\]
Since \( n, N \ge N_2 \), \( a_N - a_n > -\delta/4 \) (@prp-absolute-value-ordered-field (d)); since \( N \ge N_1 \), \( b_N - a_N \ge \delta \), and multiplying by \( 1/2 > 0 \) (@prp-ordered-field-halves (b) with \( \varepsilon = 1 \)) gives \( (b_N - a_N)/2 \ge \delta/2 \) (@prp-ordered-ring-rules (c), with equality allowed). Adding (@prp-ordered-ring-rules (b)),
\[
q - a_n > -\frac{\delta}{4} + \frac{\delta}{2} = \frac{\delta}{4} .
\]
In the same way, since \( n, N \ge N_3 \), \( b_n - b_N > -\delta/4 \), and \( b_n - q > \delta/4 \). So the sequences \( (q - a_n)_n \) and \( (b_n - q)_n \) are positive, each with margin \( \delta/4 \) and threshold \( N \). By @def-reals-operations they represent \( \kappa(q) - x \) and \( y - \kappa(q) \). Hence \( x < \kappa(q) \) and \( \kappa(q) < y \).
:::

The rational \( q \) depends on the representatives \( a, b \) and on the constants fixed in the proof; nothing makes it the "best" rational, and a different run of the proof may give a different \( q \). The theorem only claims that one exists.

The proof cites neither @thm-rationals-archimedean nor @thm-constructed-reals-archimedean: density came from the Cauchy property of the representatives, not from Archimedes. Chapter 4 proved density in every Archimedean ordered field (@thm-rationals-dense-ordered-field), so, with @thm-constructed-reals-archimedean, it gives the same conclusion for \( \nR \) by another route (Exercise B1). We keep the direct proof for what it shows: in this construction, the rationals are dense because each real number is made of rationals.

## Rational tolerances suffice

A tolerance for a limit in \( \nR \) is an element of \( \nR_{>0} \), a class of sequences. That is awkward to work with. The next result lets us test convergence in \( \nR \) with the tolerances \( \kappa(1/n) \) only.

::: {#cor-rational-epsilon-suffices}
[Rational Tolerances Suffice]

::: {.enumerate options="label=(\alph*)"}
1. For every \( \varepsilon \in \nR_{>0} \) there is \( N \in \nZ_{>0} \) with \( \kappa(1/n) < \varepsilon \) for every \( n \in \nN \) with \( n \ge N \).
2. Let \( (x_k)_{k \in \nN} \) be a sequence in \( \nR \) and \( x \in \nR \). Then \( x_k \to x \) in \( \nR \) (@def-sequence-limit-ordered-field with \( F = \nR \)) if and only if, **for every** \( n \in \nZ_{>0} \), **there is** \( K \in \nN \) with \( \abs{x_k - x} < \kappa(1/n) \) **for every** \( k \ge K \). Likewise, \( (x_k) \) is Cauchy in \( \nR \) (@def-cauchy-sequence-ordered-field with \( F = \nR \)) if and only if, for every \( n \in \nZ_{>0} \), there is \( K \in \nN \) with \( \abs{x_j - x_k} < \kappa(1/n) \) for all \( j, k \ge K \).
:::
:::

::: {.proof}
(a) Let \( \varepsilon \in \nR_{>0} \). Since \( \nR \) is Archimedean (@thm-constructed-reals-archimedean), @prp-archimedean-reciprocal in \( \nR \) gives \( N \in \nZ_{>0} \) with \( 1/(n \cdot 1_{\nR}) < \varepsilon \) for every \( n \ge N \). For such \( n \), \( n \ne 0 \), \( n \cdot 1_{\nR} = \kappa(n) \) (@thm-rational-embedding (d)) and \( 1/\kappa(n) = \kappa(1/n) \) (@thm-rational-embedding (c)). So \( \kappa(1/n) < \varepsilon \).

(b) \( (\Rightarrow) \) For \( n \in \nZ_{>0} \), \( 1/n > 0 \) in \( \nQ \) (@prp-reciprocal-order (a)), so \( \kappa(1/n) > \kappa(0) = 0_{\nR} \) (@thm-rational-embedding (b)): it is one of the tolerances of the definition, which then supplies \( K \).

\( (\Leftarrow) \) Let \( \varepsilon \in \nR_{>0} \). By (a), there is \( N \in \nZ_{>0} \) with \( \kappa(1/N) < \varepsilon \). The hypothesis with \( n \coloneqq N \) gives \( K \) with \( \abs{x_k - x} < \kappa(1/N) \) for every \( k \ge K \), and then \( \abs{x_k - x} < \varepsilon \) by (O2). So \( K \) serves for \( \varepsilon \). The Cauchy version is the same argument with \( \abs{x_j - x_k} \) for \( j, k \ge K \) in place of \( \abs{x_k - x} \).
:::

In practice: to prove a limit in \( \nR \), fix \( n \in \nZ_{>0} \) and find a threshold for the rational tolerance \( 1/n \). The threshold may depend on \( n \), and on nothing chosen later.

## Each real number is the limit of its terms

A real number \( [a] \) was introduced as a name for "what the rationals \( a_k \) are approaching". Inside \( \nQ \) there may be nothing to approach. Inside \( \nR \) there is, and it is \( [a] \) itself.

::: {#thm-terms-converge-to-class}
[A Cauchy Sequence Converges to Its Class]

Let \( a \in \sC \). Then the sequence \( (\kappa(a_k))_{k \in \nN} \) converges in \( \nR \) to \( [a] \).
:::

::: {.idea}
For a fixed \( k \), the difference \( [a] - \kappa(a_k) \) is represented by \( (a_m - a_k)_m \): the sequence \( a \) with the single rational \( a_k \) subtracted from every term. For \( m \) and \( k \) past a Cauchy threshold, these terms are small, and @lem-termwise-order turns a termwise bound into a bound between classes. That lemma yields only \( \le \), so we aim the termwise bound at \( 1/(2n) \), strictly below the target \( 1/n \).
:::

::: {.proof}
Let \( n \in \nZ_{>0} \). By @cor-rational-epsilon-suffices (b), it suffices to find \( K \in \nN \) with \( \abs{\kappa(a_k) - [a]} < \kappa(1/n) \) for every \( k \ge K \). Since \( \kappa(a_k) - [a] = -([a] - \kappa(a_k)) \), @prp-absolute-value-ordered-field (b) in \( \nR \) gives \( \abs{\kappa(a_k) - [a]} = \abs{[a] - \kappa(a_k)} \), so we bound the latter.

Since \( a \in \sC \) and \( 1/(2n) \in \nQ_{>0} \), fix \( N \in \nN \) with \( \abs{a_m - a_k} < 1/(2n) \) for all \( m, k \ge N \). Let \( k \ge N \).

By @def-reals-operations, \( [a] - \kappa(a_k) = [a] + [(-a_k)_m] = [(a_m - a_k)_m] \), and \( (a_m - a_k)_m \in \sC \) as the difference of \( a \) and a constant sequence (@thm-cauchy-algebra-ordered-field (a), (b)). By @prp-reals-absolute-value-termwise,
\[
\abs{[a] - \kappa(a_k)} = [(\abs{a_m - a_k})_m] .
\]
For every \( m \ge N \), \( \abs{a_m - a_k} \le 1/(2n) \). So @lem-termwise-order, with the constant sequence \( (1/(2n))_m \) and \( N_0 = N \), gives
\[
\abs{[a] - \kappa(a_k)} \le \kappa(1/(2n)) .
\]
Finally \( 0 < n < 2n \) in \( \nQ \), so \( 1/(2n) < 1/n \) (@prp-reciprocal-order (b)), and \( \kappa(1/(2n)) < \kappa(1/n) \) by @thm-rational-embedding (b). Combining \( \le \) with \( < \) (@prp-ordered-ring-rules (i)), \( \abs{[a] - \kappa(a_k)} < \kappa(1/n) \) for every \( k \ge N \). So \( K \coloneqq N \) works.
:::

Why \( 1/(2n) \) and not \( 1/n \) directly? The Cauchy property gives \( \abs{a_m - a_k} < 1/n \), but @lem-termwise-order passes only the non-strict inequality to classes, so we would reach \( \abs{[a] - \kappa(a_k)} \le \kappa(1/n) \), one symbol short of the definition. Halving the tolerance first leaves room for the strict inequality.

*The sequence does converge to the number it names, once that number exists.* The theorem has a consequence worth stating in words: **every real number is a limit of rationals**, namely of the terms of any of its representatives. It also explains the slogan of the chapter. Equivalent sequences have the same class, so their terms converge in \( \nR \) to the same number; by uniqueness of limits (@thm-limit-unique-ordered-field in \( \nR \)), that number is the only limit they have. A real number is what all its representatives converge to.

**Identification.** From here on we write \( q \) for \( \kappa(q) \) when \( q \in \nQ \), and \( \nQ \subseteq \nR \). This is a convention about notation, of the kind Chapter 2 adopted twice, writing \( n \) for \( \iota(n) \) and \( m \) for \( j(m) \) (@prp-naturals-embed-integers, @prp-integers-embed-rationals). It is safe because of @thm-rational-embedding: \( \kappa \) is injective and preserves sums, products, negatives, reciprocals, the order and the absolute value, so a statement about rationals means the same whether it is read in \( \nQ \) or, through \( \kappa \), in \( \nR \). It is not a set inclusion: the rational \( q \) is a class of pairs of integers, and \( \kappa(q) \) is a class of sequences of rationals, a different set. In the new notation the theorem says \( a_k \to [a] \) in \( \nR \), and @cor-rational-epsilon-suffices says that the tolerances \( 1/n \), \( n \in \nZ_{>0} \), suffice in \( \nR \).

## The square root of two

Chapter 4 ended with the Newton sequence \( (x_n) \) of @exm-newton-rationals-sqrt2, Cauchy in \( \nQ \) and with no limit in \( \nQ \) (@thm-sqrt2-cauchy-no-rational-limit). Its class is the number it was aiming at.

::: {#exm-sqrt2-class}
[The Class of the Newton Sequence]

Let \( (x_n) \) be the Newton sequence of @exm-newton-rationals-sqrt2, and let \( r \coloneqq [(x_n)] \in \nR \). Show that \( r > 0 \), that \( r^2 = 2 \), that \( r \ne q \) for every \( q \in \nQ \), and that \( r = [(d_k)] \), where \( (d_k) \) is the sequence of decimal truncations of @exm-truncations-equivalent.
:::

::: {.solution}
The sequence \( (x_n) \) is in \( \sC \) by @thm-sqrt2-cauchy-no-rational-limit, so \( r \in \nR \). We use the facts \( x_n > 1 \) for every \( n \in \nN \) and \( e_n \le 1/(4n) \) for every \( n \ge 1 \), where \( e_n \coloneqq x_n^2 - 2 \), stated in @thm-sqrt2-cauchy-no-rational-limit, and \( e_n > 0 \) for every \( n \in \nN \), proved in @exm-newton-rationals-sqrt2. The first values are
\[
e_0 = 2 , \quad e_1 = \frac{1}{4} , \quad e_2 = \frac{1}{144} , \quad e_3 = \frac{1}{166464} , \quad e_4 = \frac{1}{221682772224} .
\]

*\( r > 0 \).* Since \( x_n > 1 \) for every \( n \), the sequence \( (x_n) \) is positive, with margin \( 1 \) and threshold \( 0 \). So \( r \in P \), that is, \( r > 0 \). By @lem-termwise-order, also \( r \ge 1 \).

*\( r^2 = 2 \).* By @def-reals-operations, \( r^2 = r \cdot r = [(x_n^2)] \), and \( 2 = [(2)_n] \). Termwise, \( (x_n^2) - (2)_n = (e_n) \). For \( n \ge 1 \),
\[
0 < e_n \le \frac{1}{4n} \le \frac{1}{n + 1} ,
\]
where the last step is @prp-ordered-field-halves (c), since \( 4n - (n + 1) = 3n - 1 > 0 \). The sequence \( (1/(n + 1)) \) is defined for every \( n \in \nN \) and null in \( \nQ \) (@exm-first-sequences-ordered-field (b)); so is \( (0)_n \). The squeeze @prp-limit-preserves-order-ordered-field (c) in \( \nQ \), with \( N_0 = 1 \), shows that \( (e_n) \) is null. (At \( n = 0 \) the bound \( 1/(4n) \) is undefined and \( e_0 = 2 \); the threshold \( N_0 = 1 \) skips it.) Hence \( (x_n^2) \sim (2)_n \) and \( r^2 = 2 \).

*\( r \) is not rational.* Suppose \( r = \kappa(q) \) for some \( q \in \nQ \). Then \( \kappa(q^2) = \kappa(q)^2 = r^2 = \kappa(2) \) by @thm-rational-embedding (a), so \( q^2 = 2 \) by injectivity. This contradicts @thm-no-rational-square-two. So \( r \notin \kappa(\nQ) \).

*\( r = [(d_k)] \).* By @exm-truncations-equivalent, \( (d_k) \sim (x_k) \), so the classes are equal.

So \( \nR \) contains a positive element whose square is \( 2 \), and \( \nQ \) contains none. It is the number Chapter 4 promised, and the decimal truncations name the same number as the Newton sequence.
:::

::: {.second-reading title="The lower Newton sequence names the same number"}
Section 4.6 noted that the rationals \( 2/x_n \) approach the gap from below while the \( x_n \) approach it from above. They name the same real number. The sequence \( (1/x_n) \) is in \( \sC \) by @prp-cauchy-reciprocal-ordered-field with \( c = 1 \) and \( N = 0 \), since \( \abs{x_n} = x_n \ge 1 \); so \( (2/x_n) \in \sC \) (@thm-cauchy-algebra-ordered-field (b)). Termwise,
\[
x_n - \frac{2}{x_n} = \frac{x_n^2 - 2}{x_n} = \frac{e_n}{x_n} , \qquad 0 < \frac{e_n}{x_n} \le e_n ,
\]
using \( 0 < 1/x_n \) (@prp-reciprocal-order (a)) and \( 1/x_n \le 1 \) (@prp-ordered-field-halves (c) with \( a = 1 \), \( b = x_n \)): then \( e_n/x_n > 0 \) as a product of positives (O4), and \( e_n/x_n \le 1 \cdot e_n = e_n \) (@prp-ordered-field-halves (d)). Since \( (e_n) \) is null, the squeeze makes \( (e_n/x_n) \) null, so \( (2/x_n) \sim (x_n) \) and \( [(2/x_n)] = r \).
:::

::: {.warning}
\( r \) is **not** "the limit of \( (x_n) \) in \( \nQ \)": there is no such limit (@thm-sqrt2-cauchy-no-rational-limit), and nothing in this section changes that. The statement \( x_n \to r \) holds in \( \nR \), by @thm-terms-converge-to-class; it is a statement about a different field, with different tolerances and a different set of candidate limits.
:::

::: {.check}
Find a rational number strictly between \( [(d_k)] \) and \( [(d_k + 1/(k + 1))] \).
:::

::: {.solution}
There is none, and @thm-constructed-rationals-dense does not apply. The two sequences differ by \( (1/(k + 1)) \), which is null, so they are equivalent and the classes are equal. The hypothesis \( x < y \) fails, and no number lies strictly between a number and itself.
:::

## Exercises

### A. Check your understanding

::: {#exr-rationals-inside-the-reals-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \kappa(q^k) = \kappa(q)^k \) for every \( q \in \nQ \) and \( k \in \nN \), the powers being those of @def-naturals-in-ordered-field in \( \nQ \) and in \( \nR \).
2. Let \( r \) be as in @exm-sqrt2-class. Find the integer parts of \( r \) and of \( 10r \), and justify each from the terms \( d_k \): use \( d_1 = 7/5 \), \( d_2 = 141/100 \), and the bounds of @exm-truncations-equivalent.
3. True or false: if \( a \in \sC \), \( q \in \nQ \) and \( a_n < q \) for every \( n \), then \( [a] < q \). Give a reason or a counterexample.
4. Is \( \kappa \colon \nQ \to \nR \) surjective?
:::
:::

::: {.solution}
(a) By @fd1:ax-induction on \( k \), with base \( P(0) \). Base: \( \kappa(q^0) = \kappa(1) = 1_{\nR} = \kappa(q)^0 \), by @def-naturals-in-ordered-field (b) in \( \nQ \) and in \( \nR \) and @thm-rational-embedding (a). Step: if \( \kappa(q^k) = \kappa(q)^k \), then
\[
\kappa(q^{k+1}) = \kappa(q^k q) = \kappa(q^k) \, \kappa(q) = \kappa(q)^k \, \kappa(q) = \kappa(q)^{k+1} ,
\]
by the defining equation of powers, @thm-rational-embedding (a), and the induction hypothesis. In particular \( \kappa(q^2) = \kappa(q)^2 \), the step used in @exm-sqrt2-class.

(b) By @exm-truncations-equivalent, \( (d_k) \) is non-decreasing, and \( d_j < d_k + 1/10^k \) whenever \( j \ge k \). With \( k = 2 \): for every \( j \ge 2 \),
\[
\frac{7}{5} = d_1 \le d_j < d_2 + \frac{1}{100} = \frac{142}{100} = \frac{71}{50} .
\]
By @lem-termwise-order with \( N_0 = 2 \), and \( r = [(d_k)] \) (@exm-sqrt2-class), \( 7/5 \le r \le 71/50 \). Since \( 1 \le 7/5 \) and \( 71/50 < 2 \), \( 1 \le r < 2 \), so the integer part of \( r \) is \( 1 \). Multiplying by \( 10 > 0 \) in \( \nR \) (@prp-ordered-ring-rules (c), with equality allowed), \( 14 \le 10r \le 71/5 < 15 \), so the integer part of \( 10r \) is \( 14 \).

(c) False. Take \( a_n \coloneqq q - 1/(n + 1) \). Here \( a \in \sC \): \( (q)_n \) is constant and \( (1/(n + 1)) \) is null (@exm-first-sequences-ordered-field (b)), so both are Cauchy (@thm-cauchy-algebra-ordered-field (a)), and so is their difference (@thm-cauchy-algebra-ordered-field (b)). Then \( a_n < q \) for every \( n \), and \( a - (q)_n = (-1/(n + 1)) \) is null (@thm-limit-laws-ordered-field (b)), so \( [a] = \kappa(q) \), and \( [a] < \kappa(q) \) fails. The correct conclusion is \( [a] \le q \) (@lem-termwise-order); see the warning after it.

(d) No. By @exm-sqrt2-class, \( r \in \nR \) is not \( \kappa(q) \) for any \( q \in \nQ \).
:::

### B. Practice

::: {#exr-rationals-inside-the-reals-b1}
[B1]

Deduce @thm-constructed-rationals-dense from @thm-rationals-dense-ordered-field and @thm-constructed-reals-archimedean. Then say which hypothesis each of the two proofs uses that the other does not.
:::

::: {.solution}
By @thm-constructed-reals-archimedean, \( \nR \) is an Archimedean ordered field. So @thm-rationals-dense-ordered-field applies with \( F = \nR \): for \( x < y \) in \( \nR \) there is \( q \in \nQ \) with \( x < \iota_{\nR}(q) < y \). By @thm-rational-embedding (d), \( \iota_{\nR}(q) = \kappa(q) \), which is the conclusion of @thm-constructed-rationals-dense.

The general theorem of Chapter 4 uses that \( F \) is **Archimedean**; it knows nothing about representatives, since an element of an arbitrary ordered field is not a class of sequences. The direct proof of @thm-constructed-rationals-dense uses the **Cauchy property of the representatives** \( a \) and \( b \), and positivity of \( b - a \); it uses no Archimedean property, neither @thm-rationals-archimedean nor @thm-constructed-reals-archimedean.
:::

::: {#exr-rationals-inside-the-reals-b2}
[B2]

Let \( x \in \nR \). For \( k \in \nN \), let \( m_k \) be the integer part of \( (k + 1)x \), and \( q_k \coloneqq m_k/(k + 1) \in \nQ \). Prove that \( q_k \le x < q_k + 1/(k + 1) \) for every \( k \), and that \( q_k \to x \) in \( \nR \).
:::

::: {.solution}
Fix \( k \in \nN \). By the definition of the integer part (after @thm-constructed-reals-archimedean), \( m_k \le (k + 1)x < m_k + 1 \). Since \( k + 1 > 0 \), also \( 1/(k + 1) > 0 \) (@prp-reciprocal-order (a)), and multiplying by it in \( \nR \) preserves both inequalities (@prp-ordered-ring-rules (c), with equality allowed on the left):
\[
q_k = \frac{m_k}{k + 1} \le x < \frac{m_k + 1}{k + 1} = q_k + \frac{1}{k + 1} .
\]
So \( 0 \le x - q_k < 1/(k + 1) \) for every \( k \). In \( \nR \), the sequence \( (1/(k + 1)) \), that is \( (1/((k + 1) \cdot 1_{\nR})) \) by @thm-rational-embedding (c), (d), is null, by @prp-reciprocals-null-iff-archimedean and @thm-constructed-reals-archimedean. The squeeze @prp-limit-preserves-order-ordered-field (c) in \( \nR \), with lower sequence \( (0) \), gives that \( (x - q_k) \) is null. Then \( (q_k - x) \) is null (@thm-limit-laws-ordered-field (b)), so \( q_k \to x \) (@prp-limit-null-shift-ordered-field).

Each \( q_k \) is given by a rule: the integer part of \( (k + 1)x \) is the **only** integer with the defining property, so nothing is chosen. Section 5.5 uses the same approximants, with a different real number \( x_k \) for each \( k \).
:::

::: {#exr-rationals-inside-the-reals-b3}
[B3: Put the proof in order]

The lines below, after the identification paragraph (so \( q \) stands for \( \kappa(q) \)), contain the proof of @thm-terms-converge-to-class for \( a \in \sC \), shuffled, together with two lines that do not belong. Put the correct lines in order, and say what is wrong with each of the other two.

::: {.enumerate options="label=(\roman*)"}
1. so \( \abs{[a] - a_k} = [(\abs{a_m - a_k})_m] \), by @prp-reals-absolute-value-termwise;
2. since \( a \in \sC \), fix \( N \) with \( \abs{a_m - a_k} < 1/(2n) \) for all \( m, k \ge N \);
3. its terms are \( < 1/(2n) \) for \( m \ge N \), so \( \abs{[a] - a_k} < 1/(2n) \);
4. \( 1/(2n) < 1/n \); take \( K = N \);
5. let \( k \ge N \);
6. let \( n \in \nZ_{>0} \); by @cor-rational-epsilon-suffices (b), it suffices to find \( K \) with \( \abs{[a] - a_k} < 1/n \) for every \( k \ge K \), since \( \abs{a_k - [a]} = \abs{[a] - a_k} \) (@prp-absolute-value-ordered-field (b));
7. \( [a] - a_k \) is represented by \( (a_m - a_k)_m \);
8. for each \( k \), fix \( N_k \) with \( \abs{a_m - a_k} < 1/(2n) \) for every \( m \ge N_k \);
9. its terms are \( \le 1/(2n) \) for \( m \ge N \), so \( \abs{[a] - a_k} \le 1/(2n) \), by @lem-termwise-order.
:::
:::

::: {.solution}
*Order:* (vi), (ii), (v), (vii), (i), (ix), (iv). No other order is admissible: line (ii) introduces \( N \), which line (v) needs; line (v) fixes the \( k \) that lines (vii), (i) and (ix) are about; line (i) rewrites the class that line (vii) names; line (ix) bounds that class; and line (iv) concludes from line (ix), so it comes last.

*Line (iii)* uses the strict version of @lem-termwise-order, which is false: termwise \( < \) passes to classes only as \( \le \) (@exm-strict-termwise-order-fails). That is why the proof aims at \( 1/(2n) \) and then uses \( 1/(2n) < 1/n \).

*Line (viii)* claims a threshold \( N_k \) for every \( k \), and the Cauchy property does not supply one for an early \( k \): \( a_k \) can be far from all later terms. For \( a = (5, 0, 0, \dots) \in \sC \), \( n = 1 \) and \( k = 0 \), \( \abs{a_m - a_0} = 5 \) for every \( m \ge 1 \), so no \( N_0 \) exists. The Cauchy property gives \( \abs{a_m - a_k} < 1/(2n) \) only when both \( m \) and \( k \) are at least one \( N \), which is why line (v) takes \( k \ge N \). (If line (viii) did hold for every \( k \), the remaining lines would give the bound for every \( k \), so it is the claim that is unjustified, not the dependence on \( k \).)
:::

### C. Going deeper

::: {#exr-rationals-inside-the-reals-c1}
[C1]

::: {.enumerate options="label=(\alph*)"}
1. Let \( x \in \nR \) with \( \abs{x} \le 1/n \) for every \( n \in \nZ_{>0} \). Prove that \( x = 0 \).
2. Which result used in your proof needs \( \nR \) to be Archimedean? Show that the statement of (a) fails in the ordered field \( \nQ(t) \) of @exm-rational-function-field.
:::
:::

::: {.solution}
(a) Suppose that \( \abs{x} > 0 \). By @cor-rational-epsilon-suffices (a) with \( \varepsilon \coloneqq \abs{x} \), there is \( N \in \nZ_{>0} \) with \( 1/n < \abs{x} \) for every \( n \ge N \); in particular \( 1/N < \abs{x} \). The hypothesis with \( n = N \) gives \( \abs{x} \le 1/N \). These contradict (O1). So \( \abs{x} > 0 \) is false, by \( \rulename{\neg I} \). Since \( \abs{x} \ge 0 \) (@prp-absolute-value-ordered-field (a)), trichotomy leaves \( \abs{x} = 0 \), and then \( x = 0 \) by @prp-absolute-value-ordered-field (a).

(b) @cor-rational-epsilon-suffices (a) rests on @thm-constructed-reals-archimedean, through @prp-archimedean-reciprocal. In \( \nQ(t) \), @exm-rational-function-field shows \( 0 < 1/t < 1/(n \cdot 1) \) for every \( n \ge 1 \). So \( x \coloneqq 1/t \) satisfies \( \abs{x} = x \le 1/(n \cdot 1) \) for every \( n \ge 1 \), and \( x \ne 0 \). The statement of (a) is a form of the Archimedean property, and it fails without it.
:::

::: {#exr-rationals-inside-the-reals-c2}
[C2]

Let \( r \) be as in @exm-sqrt2-class. Prove that the set \( \{ x \in \nR : x \notin \kappa(\nQ) \} \) of irrational real numbers is dense in \( \nR \): for all \( x, y \in \nR \) with \( x < y \) there is an irrational \( z \) with \( x < z < y \).
:::

::: {.solution}
[Hint 1]

Use @thm-constructed-rationals-dense, and the irrational number \( r \).
:::

::: {.solution}
[Hint 2]

Let \( q \in \nQ \) with \( x < q < y \) (@thm-constructed-rationals-dense). How small must \( r/k \) be for \( q + r/k \) to stay below \( y \)?
:::

::: {.solution}
Let \( x < y \). By @thm-constructed-rationals-dense, fix \( q \in \nQ \) with \( x < q < y \). Then \( y - q > 0 \), and \( r > 0 \) (@exm-sqrt2-class), so \( \varepsilon \coloneqq (y - q)/r \in \nR_{>0} \) (@prp-reciprocal-order (a), (O4)). By @cor-rational-epsilon-suffices (a), there is \( k \in \nZ_{>0} \) with \( 1/k < \varepsilon \). Multiplying by \( r > 0 \) (@prp-ordered-ring-rules (c)), \( r/k < y - q \). Let \( z \coloneqq q + r/k \). Since \( r/k > 0 \),
\[
x < q < z < q + (y - q) = y .
\]
If \( z \) were rational, \( z = p \) with \( p \in \nQ \), then \( r = k(p - q) \) would be rational, since \( \kappa \) preserves differences and products (the identities after @thm-rational-embedding, and its part (a)); this contradicts @exm-sqrt2-class. So \( z \) is irrational, and lies strictly between \( x \) and \( y \).

The same argument works with \( r \) replaced by any positive irrational number. Between any two reals there are therefore both rationals and irrationals.
:::

<!-- dependency ledger
def-rational-embedding (claim): kappa is a function | constant sequences in C (thm-cauchy-algebra-ordered-field (a)) and classes (def-reals-cauchy-classes), cited; inline
thm-rational-embedding (proof): termwise sum/product/negative of constant sequences is constant | def-reals-operations (termwise), inline
thm-rational-embedding (proof): s - q > 0 from q < s | prp-ordered-ring-rules (a), cited
thm-rational-embedding (proof): |q| = q for q > 0, -q for q < 0, in Q and in R | def-absolute-value-ordered-field, cited
thm-rational-embedding (claim): (b) and injectivity of kappa also follow from (d) | thm-rationals-embed-ordered-field with F = R, cited (remark after the proof)
thm-rational-embedding (claim): kappa(q - s) = kappa(q) - kappa(s), kappa(q/s) = kappa(q)/kappa(s) | thm-rational-embedding (a), (c); proved inline after the theorem
thm-constructed-reals-archimedean (proof): (n + 1) - a_k >= (n + 1) - M from a_k <= M, and (n + 1) - M = (n - M) + 1 > 1 from n > M | field arithmetic in Q, prp-ordered-ring-rules (a), (b); cited inline
thm-constructed-reals-archimedean (claim): Q(t) is a non-Archimedean ordered field | exm-rational-function-field, cited (stated there, not verified)
thm-constructed-reals-archimedean (claim): integer part of kappa(q) is floor(q) | prp-rational-integer-part and thm-rational-embedding (b), cited; uniqueness of prp-integer-part-ordered-field
thm-constructed-rationals-dense (proof): q - a_n = (a_N - a_n) + (b_N - a_N)/2 and b_n - q = (b_n - b_N) + (b_N - a_N)/2 | field arithmetic in Q; verify/ch05/thm-constructed-rationals-dense.py
thm-constructed-rationals-dense (proof): -delta/4 + delta/2 = delta/4 | prp-ordered-field-halves (b); verify/ch05/thm-constructed-rationals-dense.py
thm-constructed-rationals-dense (claim): the proof cites neither thm-rationals-archimedean nor thm-constructed-reals-archimedean | meta-claim, checkable on the proof as written
cor-rational-epsilon-suffices (proof): n >= N >= 1 gives n != 0 | thm-integers-ordered-ring (b), (c); inline
thm-terms-converge-to-class (proof): 1/(2n) in Q_{>0} | prp-ordered-field-halves (b) with 1/n > 0 (prp-reciprocal-order (a)); 1/(2n) = (1/n)/2, field arithmetic
thm-terms-converge-to-class (proof): x <= y < z gives x < z | prp-ordered-ring-rules (i) (total order, strict part) with (O2), cited
thm-terms-converge-to-class (claim): equivalent sequences have the same limit in R | thm-limit-unique-ordered-field in R with thm-terms-converge-to-class, cited
exm-sqrt2-class (solution): x_n > 1 and e_n <= 1/(4n) for n >= 1 | thm-sqrt2-cauchy-no-rational-limit (statement), cited (blueprint routes the bound through exm-truncations-equivalent; F3.9's delivered statement carries it)
exm-sqrt2-class (solution): e_n > 0 | exm-newton-rationals-sqrt2, cited
exm-sqrt2-class (solution): e_0..e_4 = 2, 1/4, 1/144, 1/166464, 1/221682772224 | verify/ch05/exm-sqrt2-class.py
exm-sqrt2-class (solution): 4n - (n + 1) = 3n - 1 > 0 for n >= 1 | integer arithmetic; inline
exm-sqrt2-class (solution): r * r = [(x_n^2)], 2 = [(2)_n] | def-reals-operations, def-rational-embedding (identification), cited
exm-sqrt2-class (claim): (fold) x_n - 2/x_n = e_n/x_n; 0 < 1/x_n <= 1; 0 < e_n/x_n <= e_n | field arithmetic; prp-reciprocal-order (a); prp-ordered-field-halves (c), (d); (O4); verify/ch05/exm-sqrt2-class.py
exr-rationals-inside-the-reals-a1 (solution): d_1 = 7/5, d_2 = 141/100, 71/50 < 2, 14 <= 10r <= 71/5 < 15 | exm-truncations-equivalent (non-decreasing; d_j < d_k + 1/10^k for j >= k), cited; verify/ch05/exr-rationals-inside-the-reals-a1.py
exr-rationals-inside-the-reals-a1 (solution): (c) a = (q - 1/(n + 1)) in C, and (-1/(n + 1)) null in Q | exm-first-sequences-ordered-field (b), thm-cauchy-algebra-ordered-field (a), (b), thm-limit-laws-ordered-field (b), cited
exr-rationals-inside-the-reals-b2 (solution): (1/(k + 1)) null in R | prp-reciprocals-null-iff-archimedean, thm-constructed-reals-archimedean, cited
exr-rationals-inside-the-reals-b3 (solution): a = (5, 0, 0, ...) in C (eventually constant), |a_m - a_0| = 5 for m >= 1 | verify/ch05/exr-rationals-inside-the-reals-b3.py
exr-rationals-inside-the-reals-c1 (solution): 0 < 1/t < 1/(n * 1) in Q(t) | exm-rational-function-field, cited
exr-rationals-inside-the-reals-c2 (solution): kappa preserves differences and products | identities after thm-rational-embedding (inline there), thm-rational-embedding (a)
exr-rationals-inside-the-reals-a1 (solution): induction on k | fd1:ax-induction read on omega through cor-omega-identification (b), as in Chapter 4
-->
