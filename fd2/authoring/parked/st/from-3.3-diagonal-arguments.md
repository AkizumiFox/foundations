# Parked: from old Section 3.3, Diagonal Arguments

<!-- Parked from fd2 (layout-six-chapters.md §2, approved 2026-10-26). Not part of any book's src; nothing builds or scans it.
Old section: fd2 3.3 (03-diagonal-arguments.md)
Labels: cor-transcendental-exist
Intended home: ST.3
-->

## Transcendental numbers

A real number that is not algebraic is called **transcendental**. Section 3.2 showed that the set \( \mathrm{Alg} \) of algebraic numbers is countable (@thm-algebraic-countable).

::: {#cor-transcendental-exist}
[Transcendental Numbers Exist]

The set \( \nR \setminus \mathrm{Alg} \) of transcendental numbers is uncountable. In particular, there is a real number that is not algebraic.
:::

::: {.proof}
By excluded middle (@fd1:prp-excluded-middle), every real number is in \( \mathrm{Alg} \) or not, so \( \nR = \mathrm{Alg} \cup (\nR \setminus \mathrm{Alg}) \). Suppose \( \nR \setminus \mathrm{Alg} \) is countable. Since \( \mathrm{Alg} \) is countable by @thm-algebraic-countable, \( \nR \) is countable by @prp-union-two-countable, contradicting @thm-reals-uncountable-decimal. So \( \nR \setminus \mathrm{Alg} \) is uncountable. In particular \( \nR \setminus \mathrm{Alg} \ne \emptyset \), since \( \emptyset \) is countable (@def-countable). So not every \( x \) satisfies \( x \notin \nR \setminus \mathrm{Alg} \): otherwise \( \nR \setminus \mathrm{Alg} \) would be an empty set (@def-empty-set), hence equal to \( \emptyset \) (@prp-empty-set-unique). By the classical law @fd1:prp-quantifier-negation (a) and \( \rulename{\neg\neg E} \), some \( x \) lies in \( \nR \setminus \mathrm{Alg} \); this \( x \) is a real number that is not algebraic. This last passage, from "not empty" to "has an element", is a classical step (*Logic and Proof*, Section 8.7).
:::

::: {.remark}
The proof names no transcendental number: it shows that the set of them is too large to be countable, hence not empty. Its classical steps are the split of \( \nR \) into \( \mathrm{Alg} \) and its complement (excluded middle) and the last one, from "not empty" to "has an element". Compare the classical proof of @fd1:thm-irrational-power-rational in *Logic and Proof*, Section 8.7, which also names no witness (unlike @fd1:prp-log2-9-irrational, which does). Proving that a particular number, such as \( \pi \), is transcendental is a different and much harder matter.
:::

<!-- dependency ledger
cor-transcendental-exist (proof): R = Alg u (R \ Alg), every real is algebraic or not | prp-excluded-middle (cited; classical step, flagged in the remark)
cor-transcendental-exist (proof): the empty set is countable | def-countable (F2.3 §01)
cor-transcendental-exist (proof): a set that is not empty has an element | def-empty-set, prp-empty-set-unique (F2.1); prp-quantifier-negation (a) and not-not-E (classical step, flagged)
cor-transcendental-exist (claim): (remark) F1.5 §07 comparison | thm-irrational-power-rational, prp-log2-9-irrational (optional; pointer in a remark only)
cor-transcendental-exist (claim): (remark) pi is transcendental | not proved and not used (a remark only)
-->
