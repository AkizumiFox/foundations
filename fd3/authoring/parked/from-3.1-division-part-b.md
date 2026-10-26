# Parked: part (b) of thm-integers-division-remainder

<!-- Parked from fd3 (fd3/authoring/design/layout-proposal.md §3, 2.5, approved 2026-10-26). Not part of any book's src.
Old section: fd3 3.1 Division with Remainder (now fd3 2.5)
Labels: (none; part (b) of thm-integers-division-remainder, which keeps its label and part (a))
Intended home: S3 of fd3 2.5 or 3.2 decides (for example an exercise after prp-rational-integer-part): the quotient is the integer part of a/n. Its proof uses ℚ, which the re-cut puts after the integers.
-->

**Statement.**

(b) Moreover \( q = \floor{a/n} \), the integer part of the rational number \( a/n \) (@prp-rational-integer-part), so \( r = a - n \floor{a/n} \).

**Proof.**

(b) From (a), \( 0 \le r < n \); adding \( qn \) (@prp-ordered-ring-rules (b)) gives
\[
qn \le a < qn + n .
\]
These are inequalities between integers, and by @thm-rationals-ordered-field (b) and @prp-integers-embed-rationals they hold in \( \nQ \) as well, with the same sums and products. In \( \nQ \), \( n > 0 \), so \( n^{-1} > 0 \) (@prp-reciprocal-order (a)). Multiplying by \( n^{-1} \) preserves strict inequalities (@prp-ordered-ring-rules (c)) and equalities, so
\[
q = qn \cdot n^{-1} \le a \cdot n^{-1} < (qn + n) \cdot n^{-1} = q + 1 .
\]
That is, \( q \le a/n < q + 1 \), with \( q \in \nZ \). By the uniqueness in @prp-rational-integer-part, \( q = \floor{a/n} \), and then \( r = a - qn = a - n \floor{a/n} \). This proves the theorem.
