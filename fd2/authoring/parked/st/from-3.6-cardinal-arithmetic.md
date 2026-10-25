# Parked: from old Section 3.6, Cardinal Arithmetic

<!-- Parked from fd2 (layout-six-chapters.md §2, approved 2026-10-26). Not part of any book's src; nothing builds or scans it.
Old section: fd2 3.6 (06-cardinal-arithmetic.md)
Labels: exm-interleaving-decimals, thm-baire-space-reals, cor-real-sequences, exr-cardinal-arithmetic-c3 (its solution rests on thm-baire-space-reals)
Intended home: ST.3
-->

## Back to the plane

::: {#exm-interleaving-decimals}
[Interleaving digits]

The natural map \( [0, 1) \times [0, 1) \to [0, 1) \) interleaves digits. If \( x = 0.a_1 a_2 \ldots \) and \( y = 0.b_1 b_2 \ldots \), with the expansions not ending in all \( 9 \)s, let
\[
F(x, y) \coloneqq 0.a_1 b_1 a_2 b_2 \ldots ;
\]
the inverse splits the digits of \( z \) into the odd and the even places. Is \( F \) a bijection?
:::

::: {.solution}
*\( F \) is a function into \( [0, 1) \).* The expansions of \( x \) and \( y \) are fixed by the rule, as in the last proof. Let \( c \) be the interleaved sequence: \( c_{2k-1} \coloneqq a_k \), \( c_{2k} \coloneqq b_k \). It has infinitely many places that are not \( 9 \) (those of \( a \)), so it does not end in all \( 9 \)s, and by (D2) it is an expansion of exactly one \( z \in [0, 1] \). To see \( z < 1 \), let \( n \) be the first place with \( c_n \le 8 \) (@thm-well-ordering). Every earlier digit is \( 9 \), so by @prp-geometric-sum
\[
t_n \le \bigl(1 - 10^{-(n-1)}\bigr) + 8 \cdot 10^{-n} = 1 - 2 \cdot 10^{-n} ,
\]
and \( z \le t_n + 10^{-n} \le 1 - 10^{-n} < 1 \).

*\( F \) is injective.* If \( F(x, y) = F(x', y') = z \), both interleaved sequences are expansions of \( z \) and neither ends in all \( 9 \)s, so by (D3) they are equal. Then \( a = a' \) and \( b = b' \), and \( x = x' \), \( y = y' \) by (D2).

*\( F \) is not onto.* Take \( z = \frac{1}{11} = 0.090909\ldots \). The truncations at even places are \( t_{2j} = \frac{9}{99} (1 - 100^{-j}) = \frac{1}{11} - \frac{1}{11} 100^{-j} \) (@prp-geometric-sum with \( r = \frac{1}{100} \)), and the inequalities of @def-decimal-expansion hold at every place. This expansion has no tail of \( 0 \)s and no tail of \( 9 \)s, so by (D3) it is the only expansion of \( \frac{1}{11} \). A preimage \( (x, y) \) would need \( b = 9, 9, 9, \dots \); but \( b \) was the expansion of \( y \) not ending in all \( 9 \)s.

The splitting "inverse" named "the \( y \in [0, 1) \) whose expansion is \( 999\ldots \)" without checking that such a \( y \) exists: that is (N14) of @fd1:exm-not-allowed-catalogue. So the direct route gives an injection and no bijection. The injection is enough (@exm-method-injections-both-ways), and the laws give a bijection with no digit-fiddling.
:::

::: {#thm-baire-space-reals}
[Sequences of Natural Numbers]

\( \card{\nN^{\nN}} = \card{\nR} \).
:::

::: {.idea}
By the method of @exm-method-laws-by-bijection, with injections both ways: a 0–1 sequence is already a sequence of natural numbers, and a natural number is recorded by a 0–1 sequence.
:::

::: {.proof}
Send \( b \in \{0, 1\}^{\nN} \) to the same rule with codomain \( \nN \). This map is injective: two sequences with the same image have the same value at every point, so they are equal (@prp-function-equality). In the other direction, \( n \mapsto \ind_{\{n\}} \) is an injection \( \nN \to \{0, 1\}^{\nN} \), so \( \card{\nN^{\nN}} \le \card{(\{0, 1\}^{\nN})^{\nN}} \) (@prp-card-operations-monotone (c), as \( \{0, 1\}^{\nN} \ne \emptyset \)). This is \( \card{\{0, 1\}^{\nN \times \nN}} \) (@thm-cardinal-laws (f)), and that is \( \card{\{0, 1\}^{\nN}} \) by @exm-pairing-bijection and @prp-card-operations-well-defined (c). By @prp-card-le-preorder (b) and @thm-schroder-bernstein, \( \card{\nN^{\nN}} = \card{\{0, 1\}^{\nN}} \), which is \( \card{\nR} \) by @thm-reals-power-set-naturals.
:::

Exercise B4 (d) of Section 3.4 reached the equality \( \card{\nN^{\nN}} = \card{\{0, 1\}^{\nN}} \) through graphs and \( \powerset{\nN \times \nN} \).

::: {#cor-real-sequences}
[Sequences of Real Numbers]

\( \card{\nR^{\nN}} = \card{\nR} \).
:::

::: {.proof}
In one chain,
\[
\begin{aligned}
\card{\nR^{\nN}} &= \card{(\{0, 1\}^{\nN})^{\nN}} = \card{\{0, 1\}^{\nN \times \nN}} \\
&= \card{\{0, 1\}^{\nN}} = \card{\nR} ,
\end{aligned}
\]
by @prp-card-operations-well-defined (c) with @thm-reals-power-set-naturals, then @thm-cardinal-laws (f), then @exm-pairing-bijection with @prp-card-operations-well-defined (c), and @thm-reals-power-set-naturals again, chained by @prp-equinumerous-properties. No further appeal to @thm-schroder-bernstein is needed beyond the one inside @thm-reals-power-set-naturals.
:::

::: {.check}
Show that \( \card{\nR^{\nN} \times \nR} = \card{\nR} \).
:::

::: {.solution}
By @cor-real-sequences and @prp-card-operations-well-defined (b), \( \card{\nR^{\nN} \times \nR} = \card{\nR \times \nR} \), which is \( \card{\nR} \) by @thm-plane-equinumerous-line; chain with @prp-equinumerous-properties.
:::

## Exercises

::: {#exr-cardinal-arithmetic-c3}
[C3: Rearrangements of ℕ]

Let \( B \) be the set of bijections \( \nN \to \nN \). Exercise C2 of Section 4.3 showed that \( B \) is uncountable. Prove that it has exactly the size of \( \nR \): \( \card{B} = \card{\nR} \).
:::

::: {.solution}
*Up.* Every bijection \( \nN \to \nN \) is a function \( \nN \to \nN \), so \( B \subseteq \nN^{\nN} \), and the inclusion followed by a bijection \( \nN^{\nN} \to \nR \) (@thm-baire-space-reals) is an injection \( B \to \nR \).

*Down.* For \( b \in \{0, 1\}^{\nN} \), let \( \sigma_b \colon \nN \to \nN \) swap \( 2n \) and \( 2n + 1 \) when \( b(n) = 1 \), and fix them when \( b(n) = 0 \); this is a function, since each \( m \in \nN \) is \( 2n \) or \( 2n + 1 \) for exactly one \( n \). It is its own inverse, so \( \sigma_b \in B \) (@thm-bijection-iff-inverse). The map \( b \mapsto \sigma_b \) is injective, since \( b(n) = 1 \) exactly when \( \sigma_b(2n) = 2n + 1 \). This is the construction of @exr-diagonal-arguments-c2.

Composing the *Up* injection with a bijection \( \nR \to \{0, 1\}^{\nN} \) (@thm-reals-power-set-naturals) gives \( \card{B} \le \card{\{0, 1\}^{\nN}} \) (@prp-card-le-preorder (b)); by @thm-schroder-bernstein, \( \card{B} = \card{\{0, 1\}^{\nN}} \), and this is \( \card{\nR} \) by @thm-reals-power-set-naturals.

**Marking scheme.** (10 points)
- 3: shows \( \card{B} \le \card{\nR} \), through \( B \subseteq \nN^{\nN} \) and @thm-baire-space-reals.
- 3: defines \( \sigma_b \) and shows that it is a bijection of \( \nN \).
- 2: shows that \( b \mapsto \sigma_b \) is injective, by reading \( b(n) \) off \( \sigma_b(2n) \).
- 2: concludes by @thm-schroder-bernstein and @thm-reals-power-set-naturals.
Fatal errors (0 for the step): concluding \( \card{B} = \card{\nR} \) from "\( B \) is uncountable and \( B \subseteq \nN^{\nN} \)" alone, with no injection from a set the size of \( \nR \) into \( B \).
:::

<!-- dependency ledger
exm-interleaving-decimals (solution): t_n <= (1 - 10^-(n-1)) + 8 * 10^-n; termwise comparison of finite sums | prp-geometric-sum (cited); induction on n via def-sum-product and the order of R; fd2/authoring/parked/st/verify/exm-interleaving-decimals.py
exm-interleaving-decimals (solution): 0.090909... is an expansion of 1/11; t_(2j) = (1/11)(1 - 100^-j) | prp-geometric-sum (cited); fd2/authoring/parked/st/verify/exm-interleaving-decimals.py
cor-real-sequences (claim): (closing) |X x X| = |X| for all infinite X is equivalent to choice; |X u X| = |X| not provable without choice | set theory, stated without proof; nothing depends on it
exr-cardinal-arithmetic-c3 (solution): sigma_b is its own inverse; m = 2n or 2n + 1 uniquely | inline; exr-diagonal-arguments-c2 (an exercise, cited by an exercise); thm-division-algorithm as in prp-union-two-countable
-->
