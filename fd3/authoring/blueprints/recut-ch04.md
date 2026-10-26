<!-- hand-written -->
# Blueprint: F3.9 Ordered Fields and Sequences (fd3 Chapter 4, re-cut), stage S1

**Status: S1, 2026-10-26; S2 round 1 applied (replies at the end).** **Frozen after S2 (2026-10-26).** Next: S2a, S3. Pipeline **S** for every section (layout §3 Chapter 4 table, §8).

**What this is.** The S1 change list for fd3 Chapter 4 under the approved layout `fd3/authoring/design/layout-proposal.md` (§0 approval 2026-10-26; §3 Chapter 4 rows 4.1–4.6; §4.4 row "4.6 R1"; §5 "風格補課"; §8 row S). Chapter 4 keeps its directory, files, statements and labels; the work is a style revision in fd2's manner, with one new method box (4.3) and trims. A drafter executes it with this file, the six files of `fd3/src/ch04-ordered-field-sequences/` at `b401a06`, `authoring/STYLE.md` (§1 "House manner from fd2 on", §2 item 6, §11.4, §12.0, §12.1, §12.5, §12.13.4, §12.14), `DRAFTING.md`, `PIPELINE.md`, `NOTATION.md`. Format: `fd2/authoring/blueprints/ch02-functions.md`, leaner.

**Line references** are to the files at `b401a06`: `41:` = `01-rules-and-absolute-value.md`, `42:` = `02-naturals-and-archimedes.md`, `43:` = `03-limits.md`, `44:` = `04-limit-laws.md`, `45:` = `05-cauchy-sequences.md`, `46:` = `06-a-cauchy-sequence-without-a-limit.md`, `ix:` = `index.md`.

**Word counts** as `tools/check_structure.py --book fd3 --words` counts them at `b401a06`: the whole file minus folds, exercises and solutions included. (The layout's "Now" column predates the structural commit; the budgets below use the tool's count at `b401a06`.)

| § | File | Now | Budget | Expected | Folded after | Pipeline |
|---|---|---|---|---|---|---|
| 4.1 | `01-rules-and-absolute-value.md` | 3,472 | ≤ 3,000 | ~2,950 | ~95 | S |
| 4.2 | `02-naturals-and-archimedes.md` | 5,120 | ≤ 4,000 | ~3,975 | ~670 | S |
| 4.3 | `03-limits.md` | 4,629 | ≤ 5,000 (layout 4,800) | ~4,890 | ~640 | S, method section |
| 4.4 | `04-limit-laws.md` | 3,820 | ≤ 3,800 | ~3,580 | ~110 | S |
| 4.5 | `05-cauchy-sequences.md` | 5,265 | ≤ 5,000 | ~4,900 | 0 | S |
| 4.6 | `06-a-cauchy-sequence-without-a-limit.md` | 4,440 | ≤ 4,400 | ~4,275 | 0 | S |

**House manner.** Motivation before a definition or theorem; `[Scratch work]` and Ideas kept apart from proofs; fading full → Idea → terse. No footnotes, jokes, history or first person. Nothing from `/home/akizumi/book`; every new example, exercise and answer below is the book's own.

**Binding rules.**
1. **Cite back only.** Chapter 4 cites fd1, fd2 and fd3 Chapters 1–3 (new order) and earlier parts of Chapter 4. Every `@label` named here was grepped at `b401a06`. No new prose pointer to a later chapter; the approved pointers to Chapters 5–6 and to *Analysis on the Real Line* stay where they stand.
2. **No statement changes; no label renamed.** Labels lost: `exr-rules-and-absolute-value-b2` (layout: delete B2) and `exr-naturals-and-archimedes-c3` (layout: "移到 Ch6 或刪除"; deleted, §4.2 item 8). Labels whose content is rewritten (changed items): `exr-limits-b1`, `exr-a-cauchy-sequence-without-a-limit-r1`.
3. **The citation rule of this chapter** (layout §5 "每個概念只引一次規則"). 4.1 states it once (§4.1 item 2); every section applies it: field and inequality steps are not cited, except a step that needs care (multiplying or dividing an inequality, which needs the sign of the factor; a reciprocal; the "or" inside ≤; trichotomy used to conclude), and such a step cites its rule once per proof. Axiom clause names (F1)–(F9), (O1)–(O4) survive only at the first use in a proof where the clause is the point. Parentheticals "(depending on ε)" stay at the first threshold of each proof only. No rule names (¬I, RAA, ∀E) in proofs or solutions; a contradiction ends "a contradiction", and the classical step is not flagged. The three survivors at `b401a06` are removed: 42:349 (§3.2 item 8), 43:399 (§3.3 item 10), 46:343 (§3.6 item 6).
4. **Section numbers of Chapters 1–3.** S3 for Chapter 4 runs after the Chapter 1–3 rewrites (layout §8 order). The drafter greps where each cited label lives when drafting and writes section numbers from that: after the Chapter 2 split, `def-commutative-ring-and-field`, `prp-ring-algebra`, `thm-integers-commutative-ring` are in 2.3, and `def-ordered-ring-and-field`, `prp-ordered-ring-rules` (with the multiples n·a defined before it), `prp-order-from-positives`, `thm-integers-ordered-ring`, `prp-integer-least-element`, `exm-finite-ring-not-orderable` in 2.4. So "Section 2.3" at 41:5, 41:35, 41:93, 42:9, 42:17 becomes "Section 2.4" or "Sections 2.3–2.4" as the content says.
5. **Induction and recursion citations.** Ch4 now writes "@fd1:ax-induction (through @cor-omega-identification (b))" and "@fd2:thm-recursion, read on ℕ = ω through @cor-omega-identification (b)" (42:21, 42:52, 42:73, 42:155, 43:26, 45:302, 45:306, 46:51, R2). Layout §5 item 4 restates `cor-omega-identification` with a citing rule for ℕ as a Peano system. Each of these citations takes the form that the delivered 1.4 prescribes; no "ℕ = ω" survives. If Chapter 1 has not landed at S3, the drafter leaves them and lists them in the S3 report.
6. **Quick checks:** at least two per section, at least one of them new: one new Quick check in each of 4.1–4.6 (texts below), next to the one each section already has.
7. **One method section: 4.3.** It gets the full scaffold and a Prove-or-disprove item. 4.1, 4.2, 4.4–4.6 are Idea level (layout §3), with no box and no Prove-or-disprove.

---

## 1. Devices as applied

- **Method box (new):** `exm-method-limit-from-definition` (4.3, ≤ 130 words, **Template / When to use it / The usual failure**).
- **`[Scratch work]` with Givens/Goal table:** at `exm-limit-from-definition` (4.3, the box's first full appearance).
- **Worked examples for the box:** `exm-limit-from-definition` (scratch work plus forward proof) and `exm-limit-alternating-numerator` (forward, with the box's steps numbered). `exm-first-sequences-ordered-field` (b), (c) stay before them as the first limits.
- **Prove or disprove:** 4.3 B4 (`exr-limits-b4`, new).
- **Fading.** Limit from the definition: full in 4.3; Idea in 4.4 (`thm-limit-laws-ordered-field`), 4.5 (`prp-convergent-cauchy-ordered-field`, Cauchy version) and 4.6 (the Cauchy half of `thm-sqrt2-cauchy-no-rational-limit`); terse in the 4.4–4.6 exercises. Split ε: Idea in 4.3 (uniqueness, kept), 4.4 (a), 4.5 (b). Bound, then shrink: Idea in 4.4 (c), 4.5 (c). Fix the bad ε: Idea in 4.5 (kept). Locate the missing limit: Idea in 4.6 (kept). The 4.4–4.6 back-references say "keeps the shape of" the box (estimate the distance, then choose the threshold and write forwards); they do not claim that step (2)'s bound \( C/(n + 1) \) recurs.
- **Named moves without boxes** (precedent: fd2 Chapter 2's "Compute with indicators"): split ε, bound then shrink, fix the bad ε, locate the missing limit.

## 2. Labels

**New** (grepped free at `b401a06`): `exm-limit-from-definition`, `exm-method-limit-from-definition`, `exm-limit-alternating-numerator`, `exr-limits-b4`.
**Deleted:** `exr-rules-and-absolute-value-b2`, `exr-naturals-and-archimedes-c3` (no reference outside the chapter, its ledger and one sidecar).
**Rewritten in place:** `exr-limits-b1`, `exr-a-cauchy-sequence-without-a-limit-r1`.

---

## 3. Per-section plans

### 3.1 Section 4.1: Working in an Ordered Field (`01`)

Budget 3,472 → ≤ 3,000 (expected ~2,950). Idea level; no box.

1. **41:3** S3 comment deleted. **41:5** verbatim, with the section number per binding rule 4.
2. **41:11 replaced** (the "by their letters" paragraph, ~75 words → ~85): "From here on we use the field rules and the rules for inequalities of Sections 2.3, 2.4 and 3.2 without naming them, as in school algebra. A step is cited only where it needs care: multiplying or dividing an inequality, which needs the sign of the factor; taking reciprocals, which reverses order (@prp-reciprocal-order); and a weak inequality, which hides an equality case. Such a step cites its rule once in each proof. In a field \( 1 \ne 0 \), so \( 1 > 0 \) (@prp-ordered-ring-rules (e))." 41:9, 41:12–15 verbatim.
3. **`lem-field-fraction-rules` proof (41:38–67).** Remove the clause lists: 41:43 "by (F7), (F8) with (F6), (F5), the hypothesis, and (F7); this is" → "This is"; 41:49 "by (F5), (F6) and (a)" → "by (a)"; 41:56 "Then (F9) with (F6) gives" → "Then distributivity gives"; 41:66 "by (F7), (F8), (F5) and @prp-ring-algebra (b)" → deleted. Content otherwise verbatim. The Idea (41:35) loses "with (F5), (F6) and (F9)".
4. **`prp-ordered-field-halves` proof (41:96–111).** Keep (O2), (O3), (O4) at their first use and `@prp-reciprocal-order (a)`; delete "By (F9) and (F7)," and "the third equality by (F5) and (F6)"; in (b)'s midpoint sentence delete "by (F7), (F9), (F6)"; (d) verbatim.
5. **`prp-absolute-value-ordered-field` proof (41:164–186).** In each part, the first use of `@prp-ordered-ring-rules (a)` (negation reverses order) stays; later repetitions in the same part go, as do "(@prp-ring-algebra (a))" after −(−x) = x and "by uniqueness of negatives (@prp-ring-algebra (a))" in (e) and (f) (replace by "since \( -(u + v) = (-u) + (-v) \)"). (c)'s last clause "by transitivity (@prp-ordered-ring-rules (i))" → "by transitivity". Expected −120 words.
6. **41:141** (Examples): drop the parenthesis "(@thm-rationals-ordered-field (a): \( (-3) \cdot 1 < 0 \cdot 4 \))" and "(@prp-ring-algebra (a))".
7. **New Quick check** after the existing check's solution (after 41:200), before the triangle-inequality paragraph, on the main line:
   - *Check:* "For which \( x \in \nQ \) do both \( \abs{x - 1} < 2 \) and \( \abs{x + 1} < 2 \) hold?"
   - *Solution:* "By the display above, \( \abs{x - 1} < 2 \) says \( -1 < x < 3 \), and \( \abs{x + 1} = \abs{x - (-1)} < 2 \) says \( -3 < x < 1 \). Both hold exactly when \( -1 < x < 1 \)."
8. **41:206–208** (remark on *Logic and Proof* and *Analysis on the Real Line*) deleted.
9. **Exercises.** B2 (41:258–278) deleted with its sidecar and ledger line. C1's marking scheme (41:327–332) keeps its four point lines; its "Fatal errors" line shrinks to: "Fatal errors: using strictness on \( x^2 > 0 \) without ruling out \( x = 0 \); asserting \( 1 > 0 \) with no reason; using \( \nR \) or \( \sqrt{\ } \)." A1, B1, B3, C2 verbatim. B3 keeps its label; display title stays **[B3: …]** (a gap in B numbering is allowed; S9 may renumber the display titles).
10. **Ledger:** drop the `exr-rules-and-absolute-value-b2` line; add "def-absolute-value-ordered-field (solution): the Quick check, intersection −1 < x < 1 | the display after prp-absolute-value-ordered-field; verify/ch04/def-absolute-value-ordered-field.py".

11. **Fold (mandatory):** "A non-example by minimal change" (41:143) moves, verbatim, into a fold `title="Why not \( x^2 \)?"` at the same place (~95).

**Count.** 3,472 − 176 (B2) − 45 (remark) − ~210 (citations, items 3–6) − 40 (C1) + 60 (Quick check) + 10 (item 2) ≈ 3,071; item 5's trims run fully (−150 instead of −120) ≈ 3,041; item 11's fold (−95) ≈ 2,946. The S3 report gives the measured count against 3,000.

### 3.2 Section 4.2: The Rationals inside an Ordered Field; the Archimedean Property (`02`)

Budget 5,120 → ≤ 4,000 (expected ~3,975). Folds ~670. Idea level.

1. **42:3** S3 comment deleted. 42:5 verbatim.
2. **42:9, 42:17, 42:21:** section numbers per binding rule 4; recursion citation per binding rule 5.
3. **New Quick check** after 42:76:
   - *Check:* "In an ordered field \( F \), write \( (3 \cdot 1_F)(4 \cdot 1_F) - 5 \cdot 1_F \) as a single multiple of \( 1_F \), and say why it is not \( 0 \)."
   - *Solution:* "By the product law of @prp-naturals-in-ordered-field (a), \( (3 \cdot 1_F)(4 \cdot 1_F) = 12 \cdot 1_F \), and by the sum law \( 12 \cdot 1_F = 7 \cdot 1_F + 5 \cdot 1_F \), since \( 12 = 7 + 5 \) in \( \nN \). So the element is \( 7 \cdot 1_F \), and \( 7 \cdot 1_F \ge 1_F > 0 \) by part (b)."
4. **`thm-rationals-embed-ordered-field` (42:84–160): Steps 1–3 into a fold** (layout). Order on the page:
   - Statement 42:84–95, the italic line 42:82 and the Idea 42:97–99 verbatim; in the Idea's roadmap, append to ③: "(①–③ are in the fold below)".
   - **New main-line paragraph** (~70 words), after the Idea: "**The map.** By @prp-integers-embed-rationals (b), every \( x \in \nQ \) is \( p/q \) with \( p \in \nZ \) and \( q \in \nZ_{>0} \). Extend \( n \mapsto n \cdot 1_F \) to \( \nZ \) by \( (-n) \cdot 1_F \coloneqq -(n \cdot 1_F) \), and set" display "\( \iota_F(p/q) \coloneqq (p \cdot 1_F)(q \cdot 1_F)^{-1} \)". "Here \( q \ge 1 \), so \( q \cdot 1_F \ge 1_F > 0 \) (@prp-naturals-in-ordered-field (b)), and the inverse exists. Steps 1–3 check that this is a well-defined map respecting \( 1 \), \( + \) and \( \cdot \)."
   - **Fold** `title="Steps 1–3: the integers, the fractions, sums and products"`: 42:102–151 verbatim, except Step 2's display 42:135–137 is replaced by "with the formula of the paragraph above", and Step 2's first two sentences (42:134) shrink to "As above, \( q \cdot 1_F \ne 0 \)." These are plain paragraphs, not a `.proof` (§12.0: a result proved in a fold may be cited; nothing is lost for `check_forward_deps.py`).
   - **Proof** (main line): first line "Steps 1–3 (the fold above) show that \( \iota_F \) is well defined, satisfies the three equations, and \( \iota_F(n) = n \cdot 1_F \) for \( n \in \nN \)." Then **Step 4** (42:153) and **Step 5** (42:155–159) verbatim with citation trims (binding rule 3). Step 4 stays on the main line (it is the order half, which Archimedes and density use); the layout named only the uniqueness step, and this is recorded in §6.
5. **42:162** shortened to two sentences (~55 words): "For \( F = \nQ \) the identity satisfies the three equations, so \( \iota_{\nQ} = \mathrm{id} \). In general we may read "\( \nQ \subseteq F \)", as \( \nN \subseteq \nZ \subseteq \nQ \) was read in Chapters 2 and 3; the statements below keep \( \iota_F \) visible." Remark 42:164–166 verbatim (Chapter 6 uses it).
6. **42:187** ("Why the name") cut to one sentence: "The name recalls the ancient axiom about lengths that Exercise B1 states: some multiple \( (n \cdot 1_F) y \) of any \( y > 0 \) exceeds any given \( x \)."
7. **42:297** (density fails in ℚ(t), ~150 words) → one main-line sentence plus a fold. Main line: "The density theorem needs its hypothesis: in \( \nQ(t) \) no rational lies strictly between \( 0 \) and \( 1/t \)." Fold `title="Why no rational lies between 0 and 1/t"`: 42:297 from "Suppose \( q \in \nQ \) had …" verbatim.
8. **Exercises.** C3 (42:452 to its last solution) deleted (layout §3; Chapter 6's 6.1 already proves that an order-preserving map fixes ℚ, and the exercise's reduction to positive sets is not used again). A1: (b)'s solution drops the \( t^2 \) sentence. C1 marking scheme: delete the "Second route" line. C2 marking scheme: two lines ("6: (a) and naming the step; 4: proving \( t \) is not a rational image. Fatal: blaming the comparison formula or discreteness."). B2 (a)'s solution (42:349): "Suppose, for \( \rulename{RAA} \) (@fd1:def-rule-raa), that \( x \ne 0 \)." → "Suppose, for a contradiction, that \( x \ne 0 \)." (binding rule 3); otherwise verbatim. B1, B3 verbatim.
9. Citation trims per binding rule 3 in 42:52–73, 42:201–205, 42:238–246, 42:264–268 (~90 words).
10. **Fold (mandatory):** the proof of `prp-naturals-in-ordered-field` (d) (42:69–73, ~110) into a fold `title="Part (d): the two copies of ℕ in ℚ agree"`; (a)–(c) stay on the main line.
11. **Ledger:** drop the C3 line; the Step 1–3 lines keep their keys (the fold is main line for the ledger); add "prp-naturals-in-ordered-field (solution): the Quick check, 12 = 7 + 5, 7.1_F >= 1_F | prp-naturals-in-ordered-field (a), (b); verify/ch04/prp-naturals-in-ordered-field.py".

**Count.** 5,120 − 320 (Steps 1–3 net of the new paragraph) − 354 (C3) − 120 (item 7) − 50 (item 5) − 40 (item 6) − 120 (marking schemes, A1) − 90 (item 9) + 60 (Quick check) ≈ 4,086; item 10's fold (−110) ≈ 3,976. The S3 report gives the measured count against 4,000.

### 3.3 Section 4.3: Sequences and Limits in an Ordered Field (`03`) — method section, full

Budget 4,629 → ≤ 5,000 (expected ~4,890; layout 4,800). Folds ~640. Order of subsections: Sequences; The limit of a sequence; **Proving a limit from the definition** (new); Archimedes and the sequence 1/(n + 1); Changing finitely many terms; A sequence has at most one limit; Convergent sequences are bounded; Exercises.

1. **43:3** S3 comment deleted. 43:5 verbatim; append one sentence: "On the way it isolates the method behind the limit proofs of the chapter: estimate the distance, find a threshold, then write the proof forwards."
2. **43:7** shortened to its first sentence plus "As agreed after @prp-naturals-in-ordered-field, we write \( n \) for \( n \cdot 1_F \), so \( 1/(n + 1) \coloneqq 1/((n + 1) \cdot 1_F) \) exists and is positive (@prp-naturals-in-ordered-field (b), @prp-reciprocal-order (a))." (The general-\( F \) facts are kept: the method box and the (⇐) half of `prp-reciprocals-null-iff-archimedean` rely on them.)
3. **43:30** ("Eventually" paragraph): keep through "one comparison at a time"; the last two sentences (infinitely many properties) go, verbatim, into a fold of their own `title="Infinitely many properties"` at the same place.
4. **43:57** cut to its first two sentences; **43:59** ("Well-definedness") deleted. The definition block 43:42–50 stays verbatim. The "a limit" remark survives in the prose after the definition: 43:52's first sentence "In words: …" becomes "In words (we say **a** limit until @thm-limit-unique-ordered-field): …".
5. **Fold** `title="Why this definition, clause by clause"` after the warning 43:115–117: contains 43:106 (non-example with candidate 2) and 43:108–113 (the four bullets), verbatim, except that the last bullet's pointer (43:113) "The remark after @prp-reciprocals-null-iff-archimedean shows this happen." becomes "The fold after @prp-reciprocals-null-iff-archimedean (\"Rational tolerances are not enough in \( \nQ(t) \)\") shows this happen." (item 7). Main line keeps, before the warning, one sentence: "Each clause of the definition is needed; the fold below shows what goes wrong when one is changed." (S2 check: the warning and the Quick check stay on the main line.)
6. **New subsection `## Proving a limit from the definition`**, after 43:133 (null and bounded sequences), before 43:135.
   - Lead (~45 words): "In @exm-first-sequences-ordered-field the distance \( \abs{a_n - a} \) was \( 1/(n + 1) \) or \( 1/(n + 2) \), and Archimedes supplied \( N \) at once. Usually the distance is messier, and the threshold has to be found before the proof can be written."
   - **`exm-limit-from-definition`** `[A limit found by working backwards]`: "Prove from @def-sequence-limit-ordered-field that \( \dfrac{n^2 + 1}{2n^2 + 3} \to \dfrac{1}{2} \) in \( \nQ \)."
   - **Word caps for the subsection** (≤ 875 in all): lead ≤ 45; statement ≤ 25; scratch work with table ≤ 200; Solution ≤ 200; box ≤ 130; second example, statement and solution, ≤ 195; Quick check with solution ≤ 100. The S3 report gives each element's count.
   - **Idea `[Scratch work]`** (≤ 22 lines): "The goal has the shape ∀ε ∃N ∀n ≥ N. So the proof starts "Let \( \varepsilon \in \nQ_{>0} \)", names an \( N \), and checks every \( n \ge N \). Finding \( N \) is the work, done backwards from the distance. One fraction: \( \frac{n^2 + 1}{2n^2 + 3} - \frac12 = \frac{-1}{2(2n^2 + 3)} \), so the distance is \( 1/(2(2n^2 + 3)) \). Solving \( 1/(2(2n^2 + 3)) < \varepsilon \) for \( n \) exactly would need a square root. But no proof needs the least \( N \), only some \( N \); so replace the distance by something larger and simpler. Since \( 2(2n^2 + 3) - (n + 1) = 4n^2 - n + 5 > 0 \) for every \( n \), the distance is at most \( 1/(n + 1) \), and "\( 1/(n + 1) < \varepsilon \) eventually" is Archimedes." Table:

     | Givens | Goal |
     |---|---|
     | \( \varepsilon \in \nQ_{>0} \) | \( N \) with \( \abs{a_n - \frac12} < \varepsilon \) for every \( n \ge N \) |
     | \( \abs{a_n - \frac12} = \frac{1}{2(2n^2 + 3)} \) | \( N \) with \( \frac{1}{2(2n^2 + 3)} < \varepsilon \) for \( n \ge N \) |
     | \( \frac{1}{2(2n^2 + 3)} \le \frac{1}{n + 1} \) for every \( n \) | \( N \) with \( \frac{1}{n + 1} < \varepsilon \) for \( n \ge N \) |
     | @prp-archimedean-reciprocal: \( N \in \nZ_{>0} \) with \( 1/m < \varepsilon \) for \( m \ge N \) | \( n \ge N \) gives \( n + 1 \ge N \): the gap is closed |

     Last line: "The proof runs the table upwards: given ε, choose N, check n ≥ N."
   - **Solution:** old B1's "Second limit" paragraph (43:318–326) moved here, opened with "Let \( \varepsilon \in \nQ_{>0} \). By @prp-archimedean-reciprocal (\( \nQ \) is Archimedean, @thm-rationals-archimedean) choose \( N \in \nZ_{>0} \) with \( 1/m < \varepsilon \) for every \( m \ge N \)." Its last sentence (43:326, "With the \( N \) of the first part, every \( n \ge N \) has distance \( \le 1/(n + 1) < \varepsilon \).") is replaced by "For \( n \ge N \), \( n + 1 \ge N \), so \( \abs{a_n - \frac12} \le 1/(n + 1) < \varepsilon \)." Then one sentence from 43:328: "Archimedes entered only in choosing \( N \); the algebra of the distance holds in every ordered field." The \( \nQ(t) \) sentences of 43:328 are dropped (item 11).
   - **`exm-method-limit-from-definition`** `[Method: proving a limit from the definition]`.
     - **Template.** (1) Bring the distance \( \abs{a_n - a} \) to one fraction. (2) Bound it, for all \( n \ge n_0 \), by \( C/(n + 1) \) with \( C \in F_{>0} \), enlarging numerators and shrinking denominators. (3) If \( F \) is Archimedean, take \( N' \) from @prp-archimedean-reciprocal with \( 1/m < \varepsilon/C \) for \( m \ge N' \), and let \( N \coloneqq \max\{N', n_0\} \). (4) Write forwards: let ε; let N be …; let n ≥ N; then \( \abs{a_n - a} \le C/(n + 1) < \varepsilon \).
     - **When to use it.** The candidate limit is known, the distance has a formula, and \( F \) is Archimedean (as \( \nQ \) is, @thm-rationals-archimedean); in a general \( F \), step (3) needs another source of thresholds (Section 4.4).
     - **The usual failure.** Writing the backward computation as the proof: that proves the converse, entry (N5) of @fd1:exm-not-allowed-catalogue. Choosing \( N \) before ε, or letting it depend on \( n \).
     - The box as written here is ~125 words ("the least \( N \) is never needed" is left to the scratch work, which says it); the drafter keeps it ≤ 130.
   - **`exm-limit-alternating-numerator`** `[A limit with an oscillating numerator]`: "Prove from the definition that \( a_n = \dfrac{2n + (-1)^n}{n + 1} \to 2 \) in \( \nQ \)." *Solution* (~170 words), steps numbered as in the box: "(1) \( a_n - 2 = \frac{(-1)^n - 2}{n + 1} \). (2) \( (-1)^n \) is \( 1 \) or \( -1 \) (@exm-first-sequences-ordered-field (d)), so \( \abs{(-1)^n - 2} \) is \( 1 \) or \( 3 \), and \( \abs{a_n - 2} \le 3/(n + 1) \) for every \( n \) (\( n_0 = 0 \), \( C = 3 \)). (3) Let \( \varepsilon \in \nQ_{>0} \). Then \( \varepsilon/3 > 0 \); choose \( N \in \nZ_{>0} \) with \( 1/m < \varepsilon/3 \) for every \( m \ge N \) (@prp-archimedean-reciprocal). (4) For \( n \ge N \), \( n + 1 \ge N \), so \( \abs{a_n - 2} \le 3/(n + 1) < 3 \cdot \varepsilon/3 = \varepsilon \)." Aftermath: "The distance itself goes up and down: \( 1, 3/2, 1/3, 3/4, 1/5, \dots \). Step (2) replaced it by \( 3/(n + 1) \), which decreases, and only the bound had to be pushed below ε."
   - **Quick check:** "In the proof just given, take \( \varepsilon = 1/10 \). Which \( N \) does step (3) produce if \( N \) is taken least? What is the least \( N \) that works in the definition itself?" *Solution:* "\( 1/m < 1/30 \) exactly when \( m \ge 31 \), so step (3) gives \( N = 31 \). In the definition: at even \( n \) the distance is \( 1/(n + 1) \), below \( 1/10 \) once \( n \ge 10 \); at odd \( n \) it is \( 3/(n + 1) \), below \( 1/10 \) exactly when \( n + 1 > 30 \). At \( n = 29 \) the distance is \( 3/30 = 1/10 \), not below it; from \( n = 30 \) on every term qualifies. So the least \( N \) is \( 30 \). The proof's \( N \) is larger, and that costs nothing."
7. **43:163** cut to its first sentence. **Remark 43:165–167** → fold `title="Rational tolerances are not enough in Q(t)"` (verbatim). The pointer at 43:113 lives in the item 5 fold and is reworded there to name this fold.
8. **Uniqueness (43:216–249).** The try-it-first line and the Idea stay (this is the ε/2 Idea of the layout). Proof: citation trims; last sentence "Hence the assumption \( a \ne b \) is refuted, and \( a = b \) (@fd1:def-rule-raa)." → "This contradiction shows \( a = b \)." Remark 43:244–246 deleted (the Idea already names @fd1:prp-arbitrarily-close-equal).
9. **43:202** cut to its first sentence. Citation trims in 43:189–199 and 43:265–273 (binding rule 3).
10. **Exercises.**
    - **A1** verbatim except (b)'s solution: keep the first four sentences and the last two; delete "This is the argument … needed: only one tolerance is in play)".
    - **B1 rewritten** (`exr-limits-b1`, title **[B1: Limits from the definition]**): "Prove from @def-sequence-limit-ordered-field, following @exm-method-limit-from-definition, that in \( \nQ \): (a) \( \dfrac{3n + 2}{n + 4} \to 3 \); (b) \( \dfrac{n + 5}{n^2 + 1} \to 0 \). Say where the Archimedean property is used."
      *Solution.* "(a) (1) \( \frac{3n + 2}{n + 4} - 3 = \frac{-10}{n + 4} \), distance \( 10/(n + 4) \). (2) \( 0 < n + 1 < n + 4 \), so \( 1/(n + 4) < 1/(n + 1) \) (@prp-reciprocal-order (b)) and the distance is \( < 10/(n + 1) \). (3) Given \( \varepsilon \in \nQ_{>0} \), choose \( N \in \nZ_{>0} \) with \( 1/m < \varepsilon/10 \) for \( m \ge N \). (4) For \( n \ge N \): distance \( < 10/(n + 1) < \varepsilon \). (b) (1) The distance is \( (n + 5)/(n^2 + 1) \). (2) For \( n \ge 1 \): \( n + 5 \le 6n \); \( n^2 < n^2 + 1 \) gives \( 1/(n^2 + 1) < 1/n^2 \); so the distance is \( < 6n/n^2 = 6/n \), and \( 6/n \le 12/(n + 1) \) because \( n + 1 \le 2n \). So distance \( < 12/(n + 1) \) for \( n \ge 1 \) (\( n_0 = 1 \); at \( n = 0 \) the term is \( 5 \)). (3) Choose \( N \in \nZ_{>0} \) with \( 1/m < \varepsilon/12 \) for \( m \ge N \); then \( N \ge 1 = n_0 \). (4) For \( n \ge N \): \( n \ge 1 \), so distance \( < 12/(n + 1) < \varepsilon \). *Where Archimedes is used:* in step (3) only, both times."
    - **B2, B3** verbatim. **C1, C2** verbatim, except C2's marking scheme keeps its four point lines and its Fatal line, without the parenthetical "(bounded ∀ used outside its range; entry (N9))". C2's solution (43:399): "(bounded \( \rulename{\forall E} \), @fd1:prp-bounded-quantifier-rules)" → "(the bounded universal applies only to \( n \ge N \))"; the (N9) citation stays (binding rule 3). Otherwise verbatim.
    - **B4 new** (`exr-limits-b4`, title **[B4: Prove or disprove]**), placed after B3: "Let \( F \) be an ordered field and \( (a_n) \), \( (b_n) \) sequences in \( F \). Prove each true statement from @def-sequence-limit-ordered-field and refute each false one with a counterexample. (a) If \( a_n \to a \), then \( (a_{2n})_{n \in \nN} \) converges to \( a \). (b) If \( (a_{2n})_n \) and \( (a_{2n+1})_n \) both converge, then \( (a_n) \) converges. (c) If \( (a_n) \) is null and \( \abs{b_n} \le \abs{a_n} \) for every \( n \), then \( (b_n) \) is null. (d) If \( a_n \to a \), then \( (a_{n+1} - a_n) \) is null. (e) If \( (a_n b_n) \) is null, then \( (a_n) \) or \( (b_n) \) is null. (f) In \( F = \nQ \): if \( a_n \to a \) and every \( a_n \) is an integer, then there is \( N \) with \( a_n = a_N \) for every \( n \ge N \)."
      *Solution.* "(a) **True.** Given ε, take the \( N \) of \( a_n \to a \). For \( n \ge N \), \( 2n = n + n \ge n \ge N \), so \( \abs{a_{2n} - a} < \varepsilon \). (b) **False.** \( a_n = (-1)^n \) in \( \nQ \): \( (-1)^{2n} = 1 \) and \( (-1)^{2n+1} = -1 \) for every \( n \) (induction, from \( (-1)^{k+2} = (-1)^k \)), so the two subsequences are constant, with limits \( 1 \) and \( -1 \); and \( (a_n) \) diverges (@exm-first-sequences-ordered-field (d)). (c) **True.** Given ε, take \( N \) with \( \abs{a_n} < \varepsilon \) for \( n \ge N \); then \( \abs{b_n - 0} \le \abs{a_n} < \varepsilon \) for \( n \ge N \). (d) **True.** Given ε, take \( N \) with \( \abs{a_n - a} < \varepsilon/2 \) for \( n \ge N \). For \( n \ge N \) also \( n + 1 \ge N \), and \( \abs{a_{n+1} - a_n} \le \abs{a_{n+1} - a} + \abs{a - a_n} < \varepsilon \). (e) **False.** In \( \nQ \) take \( a_n = (1 + (-1)^n)/2 \) and \( b_n = (1 - (-1)^n)/2 \). Since \( (-1)^n \) is \( 1 \) or \( -1 \) (@exm-first-sequences-ordered-field (d)), their values are \( 1, 0, 1, \dots \) and \( 0, 1, 0, \dots \), and \( a_n b_n = 0 \) for every \( n \): the constant \( 0 \), null. Neither factor is null: for \( \varepsilon = 1 \) and any \( N \), one of \( N, N + 1 \) is even and one odd, and there \( \abs{a_n} = 1 \), resp. \( \abs{b_n} = 1 \). (f) **True.** Take \( N \) with \( \abs{a_n - a} < 1/2 \) for \( n \ge N \). For \( n \ge N \), \( k \coloneqq a_n - a_N \) is an integer with \( \abs{k} \le \abs{a_n - a} + \abs{a - a_N} < 1 \). If \( k > 0 \), then \( k \ge 1 \) by discreteness (@thm-integers-ordered-ring (c); the order of \( \nQ \) agrees with that of \( \nZ \) on integers, by the comparison formula of @thm-rationals-ordered-field (a) with denominators \( 1 \)), against \( \abs{k} < 1 \); if \( k < 0 \), the same with \( -k \). So \( k = 0 \)."
11. **Fold (mandatory):** the "Bounds" half of the proof of `prp-tail-change-ordered-field` (43:191–195, ~120) into a fold `title="The bound part of (a)"`.
12. **Ledger:** move the first `exr-limits-b1` line (distance, 43:434) to `exm-limit-from-definition (solution)` (same fact, sidecar `verify/ch04/exm-limit-from-definition.py`); drop the second `exr-limits-b1` line (\( \nQ(t) \), 43:435) with the \( \nQ(t) \) sentences of 43:328; new lines for `exm-limit-alternating-numerator` (distances, the Quick check's 30 and 31), `exr-limits-b1` (−10/(n + 4); n + 5 ≤ 6n and 6/n ≤ 12/(n + 1) for n ≥ 1), `exr-limits-b4` ((−1)^{2n} = 1 by induction; (e)'s factors (1 ± (−1)^n)/2 take values 1, 0 alternately, product 0; discreteness transferred to ℚ by the comparison formula: thm-integers-ordered-ring (c), thm-rationals-ordered-field (a)).

**Count.** 4,629 + 1,295 (new subsection ≤ 875 by the caps, B1 net ~40, B4 ~380) − 230 (item 5 fold) − 90 (non-example into the fold) − 130 (item 7 fold) − 80 (item 8 remark) − 70 (A1 (b)) − 70 (item 3 fold) − 75 (item 4) − 25 (item 2) − 40 (43:163) − 30 (43:202) − 60 (citations, item 9 included) − 15 (C2) − 120 (item 11 fold) ≈ 4,889. The S3 report gives the measured count against 5,000; if a cap of the new subsection is exceeded, the drafter trims inside that element.

### 3.4 Section 4.4: The Algebra and Order of Limits (`04`)

Budget 3,820 → ≤ 3,800 (expected ~3,580). Idea level.

1. **44:3** S3 comment deleted. **44:5**: keep the first four sentences, with "Exercise B1 of Section 4.3" in the first replaced by "@exm-limit-from-definition"; replace the last two by "No result of this section uses the Archimedean property; only the examples in \( \nQ \) do, through @exm-first-sequences-ordered-field (b) or the non-example after @def-bounded-sequence-ordered-field."
2. **`prp-null-times-bounded-ordered-field` proof (44:19–25):** delete "(depending on ε and M)" and the citation "(@prp-ordered-ring-rules (c))"; keep 44:24's two clauses "multiplies \( \abs{b_n} \le M \) by \( \abs{a_n} \ge 0 \) (@prp-ordered-field-halves (d))" and "multiplies \( \abs{a_n} < \varepsilon/M \) by \( M > 0 \)" (binding rule 3: sign-sensitive multiplications keep one citation).
3. **44:45** shortened: keep the first sentence and the \( (1 + (-1)^n)/(n + 1) \) witness with its reason in one clause ("(the warning in Section 4.3)"); delete the last sentence.
4. **Idea of `thm-limit-laws-ordered-field` (44:62–68):** prepend "Each part keeps the shape of @exm-method-limit-from-definition (estimate the distance, then choose the threshold and write forwards), but the threshold comes from the hypotheses \( a_n \to a \), \( b_n \to b \) instead of from Archimedes, and the estimate bounds the distance by \( \abs{a_n - a} \), \( \abs{b_n - b} \) through split ε or bound-then-shrink." Rest verbatim.
5. **Proof (44:70–109):** citation trims (binding rule 3): in (a) delete the two "(depending on ε)" after the first and the citations of the strict addition; in (c) replace 44:86's three sentences after "We fix this \( M \) now; it depends on the sequence \( (a_n) \) only." by "Now let \( \varepsilon \in F_{>0} \). Since \( M > 0 \) and \( \abs{b} + 1 \ge 1 > 0 \), the tolerances \( \varepsilon/(2M) \) and \( \varepsilon/(2(\abs{b} + 1)) \) are positive." and 44:98 by "The second line uses @prp-ordered-field-halves (d), all factors being non-negative; the third multiplies the two estimates by the positive elements \( M \) and \( \abs{b} + 1 \)."; in (d) delete the bracketed citations except @lem-limit-bounded-away-ordered-field, @lem-field-fraction-rules (c), @prp-reciprocal-order (b).
6. **44:111, 44:113** verbatim (44:113 names the moves, linked from the index). **44:115** (the second route for (c)) → fold `title="The product law from the two tools"`, verbatim. 44:117, warning 44:119–121 and the Quick check 44:123–133 verbatim.
7. **New Quick check** after the warning 44:177–179:
   - *Check:* "Let \( a_n \to a \) in \( F \) with \( \abs{a_n} \le 3 \) for every \( n \). Show \( \abs{a} \le 3 \)."
   - *Solution:* "By @prp-absolute-value-ordered-field (d), \( -3 \le a_n \le 3 \) for every \( n \). Part (b) of @prp-limit-preserves-order-ordered-field, used twice, gives \( -3 \le a \le 3 \), and (d) again gives \( \abs{a} \le 3 \)."
8. **Exercises.** A1, B1, B2, B3, C2 verbatim. C1's marking scheme: the long "A route through null sequences …" sentence becomes "A route through @prp-null-times-bounded-ordered-field earns the same points, provided the sum of two null sequences is proved from the definition."
9. **Ledger:** add "prp-limit-preserves-order-ordered-field (solution): the Quick check |a| <= 3 | prp-absolute-value-ordered-field (d), prp-limit-preserves-order-ordered-field (b); inline".

**Count.** 3,820 − 30 (item 1) − 40 (item 3) − 170 (items 2, 5) + 60 (item 4) − 110 (fold) + 55 (Quick check) − 50 (C1) ≈ 3,535–3,580.

### 3.5 Section 4.5: Cauchy Sequences (`05`)

Budget 5,265 → ≤ 5,000 (expected ~4,900). Idea level.

1. **45:3** S3 comment deleted. 45:5 verbatim; **45:7**'s last sentence ("We use the absolute-value rules … in \( F \).") deleted (binding rule 3 covers it).
2. **Negation (45:33–37) as an Idea** (layout): replace the paragraph by
   - `::: {.idea}`: "Negate as in *Logic and Proof*, Chapter 6: each bounded quantifier flips (@fd1:prp-bounded-quantifier-negation), the implication becomes a conjunction (@fd1:prp-negated-implication), and \( \neg(x < \varepsilon) \) is \( x \ge \varepsilon \). "\( (a_n) \) is not Cauchy" reads" display 45:34–36 verbatim "One tolerance is beaten beyond every threshold."
3. **45:43** (reciprocals): keep, with "(@prp-reciprocal-order)" narrowed to "(@prp-reciprocal-order (b))" (a reciprocal step, binding rule 3); replace the sentence "Two elements \( x, y \) of \( (0, c) \) … (d)." replaced by "two elements of \( (0, 1/N) \) differ by less than \( 1/N \)".
4. **"Why this definition" (45:49–53):** bullets 1 and 2 verbatim; bullet 3 cut to: "*Tolerances from the field.* \( \nQ(t) \) has the tolerance \( 1/t \), below every positive rational; Exercise C2 of Section 4.6 shows a sequence of rationals that is Cauchy in \( \nQ \) and not in \( \nQ(t) \)."
5. **Idea of `prp-convergent-cauchy-ordered-field` (45:71–73):** append "This is split ε, as in the uniqueness proof of Section 4.3, with the point \( a \) between the two terms; the threshold comes from the hypothesis, as in the limit laws." Proof: citation trims.
6. **45:90** (Quick check solution): "(by induction, with \( \abs{xy} = \abs{x}\abs{y} \), @prp-absolute-value-ordered-field (b))" → "(@exm-first-sequences-ordered-field (d))".
7. **`thm-cauchy-algebra-ordered-field` proof (45:139–172).** (b) *Multiples* (45:151–155) replaced by "*Multiples.* The proof of @thm-limit-laws-ordered-field (b) carries over with \( a_m \) in place of \( a \): for \( c \ne 0 \), the tolerance \( \varepsilon/\abs{c} \) for \( (a_n) \) gives \( \abs{c a_m - c a_n} = \abs{c}\,\abs{a_m - a_n} < \varepsilon \) for all \( m, n \ge N \); for \( c = 0 \) it is the constant sequence \( 0 \), Cauchy by (a)." (b) *Sums* and (c): citation trims (binding rule 3); in (c) keep @prp-cauchy-bounded-ordered-field and the sentence on @prp-ordered-field-halves (d); delete the citations of the strict addition and of (F5)–(F8).
8. **Remark 45:176–178** cut to one sentence: "Chapter 5 adds and multiplies classes of Cauchy sequences of rationals termwise; clauses (b) and (c) with \( F = \nQ \) keep the termwise results Cauchy."
9. **`thm-cauchy-not-null-sign` proof, first paragraph (45:205):** replaced by "Negating @def-null-sequence-ordered-field (@fd1:prp-bounded-quantifier-negation, @fd1:prp-negated-implication) gives \( \varepsilon \in F_{>0} \) such that for every \( N \in \nN \) some \( n \ge N \) has \( \abs{a_n} \ge \varepsilon \). Fix such an \( \varepsilon \)." Rest verbatim with citation trims.
10. **New Quick check** after 45:229:
    - *Check:* "For \( a_n = (n - 3)/(n + 1) \) in \( \nQ \), which alternative of @thm-cauchy-not-null-sign holds? Give a valid \( c \) and \( N \)."
    - *Solution:* "\( a_n = 1 - 4/(n + 1) \). For \( n \ge 7 \), \( n + 1 \ge 8 \), so \( 4/(n + 1) \le 1/2 \) and \( a_n \ge 1/2 \): the first alternative, with \( c = 1/2 \), \( N = 7 \). (At \( n = 6 \), \( a_6 = 3/7 < 1/2 \), so this \( N \) is least for this \( c \); other pairs, such as \( c = 1/5 \), \( N = 4 \), work too.)"
11. **`prp-cauchy-reciprocal-ordered-field` proof (45:266–278):** citation trims; keep @lem-field-fraction-rules (c) and @prp-ordered-field-halves (c), (d).
12. **Exercises.** A1: delete (e). C2's marking scheme: keep the point lines, cut its Fatal line to one sentence. B1, B2, B3, C1, C3 verbatim. (C1 and B2 are named in an1's ch04 blueprint; labels and content unchanged.)
13. **Ledger:** add "thm-cauchy-not-null-sign (solution): the Quick check, a_n = 1 - 4/(n + 1), c = 1/2, N = 7 | lem-field-fraction-rules (b); verify/ch04/thm-cauchy-not-null-sign.py (new)".

**Count.** 5,265 − 30 (item 1) − 30 (item 2) − 32 (item 3) − 35 (item 4) + 30 (item 5) − 15 (item 6) − 60 (item 7 multiples) − 120 (citations, items 5, 7, 9, 11) − 25 (item 8) − 40 (item 9) + 70 (Quick check) − 30 (A1 (e)) − 40 (C2) ≈ 4,908.

### 3.6 Section 4.6: A Cauchy Sequence with No Rational Limit (`06`)

Budget 4,440 → ≤ 4,400 (expected ~4,275). Idea level.

1. **46:3** S3 comment deleted. 46:5–32 verbatim.
2. **Idea (46:45):** the *Cauchy* paragraph gets a first sentence: "This keeps the shape of @exm-method-limit-from-definition, with a second index in place of the limit: bound \( \abs{x_m - x_n} \) by an expression in \( n \) alone, then let Archimedes push it below ε." Rest verbatim.
3. **Proof (46:51–85):** induction citation per binding rule 5; citation trims in (iii), (v), (vi) (binding rule 3; keep @prp-ordered-field-halves (c), (d) where a reciprocal or a product of inequalities is taken).
4. **46:88–118** verbatim (remark, warning, Quick check, "What this chapter did not prove"), except one new Quick check after the existing check's solution:
   - *Check:* "For \( \varepsilon = 1/100 \), which \( N \) does the Cauchy half of the proof give, if \( N \) is taken least?"
   - *Solution:* "The proof takes \( N \in \nZ_{>0} \) with \( 1/N < 1/100 \), that is \( N > 100 \). The least is \( N = 101 \); any \( N \ge 101 \) serves. (Because of the factor \( 4 \) in \( 1/(4N) \), a smaller \( N \) would do, but the proof does not ask for it.)"
5. **R1 rewritten** (`exr-a-cauchy-sequence-without-a-limit-r1`, title **[R1]**), without ideals and with the closure facts only (layout §3 row 4.6, §4.4; the equivalence relation and well-definedness are Chapter 5's `prp-cauchy-equivalent-relation` and `thm-reals-operations-well-defined`, not anticipated here):
   - *Statement:* "Let \( \sC \) be the set of Cauchy sequences in \( \nQ \) and \( \sN \) the set of null sequences in \( \nQ \). Prove that \( \sN \subseteq \sC \), that \( (y_n + z_n) \in \sN \) whenever \( (y_n), (z_n) \in \sN \), and that \( (r_n z_n) \in \sN \) whenever \( (r_n) \in \sC \) and \( (z_n) \in \sN \)."
   - *Solution* (~90 words): "\( \sN \subseteq \sC \) by @thm-cauchy-algebra-ordered-field (a). If \( y_n \to 0 \) and \( z_n \to 0 \), then \( y_n + z_n \to 0 + 0 = 0 \) by @thm-limit-laws-ordered-field (a). If \( (r_n) \in \sC \), it has a bound \( M \in \nQ_{>0} \) (@prp-cauchy-bounded-ordered-field), so \( (z_n r_n) \) is null by @prp-null-times-bounded-ordered-field, and \( r_n z_n = z_n r_n \). Chapter 5 uses these two closure properties when it adds and multiplies classes."
6. **Other exercises** verbatim (A1, B1, B2, C1, C2, R2, R3, R4), except: R2's recursion citation per binding rule 5; R3's solution loses the parenthetical 46:343 "(The \( \vdash \) directions of steps 4 and 5 use \( \rulename{RAA} \), …)" and keeps "So the negation says: …" (binding rule 3).
7. **Ledger:** replace the R1 line by "exr-a-cauchy-sequence-without-a-limit-r1 (solution): N in C, N closed under +, r.z in N for r in C, z in N | thm-cauchy-algebra-ordered-field (a), thm-limit-laws-ordered-field (a), prp-cauchy-bounded-ordered-field, prp-null-times-bounded-ordered-field, cited"; add "thm-sqrt2-cauchy-no-rational-limit (solution): the Quick check, 1/N < 1/100 gives least N = 101 | cor-rationals-archimedean-epsilon; inline". The ledger's stale item for R1 (layout §9) is resolved by this rewrite; R1 joins the changed-only review.

**Count.** 4,440 + 25 (item 2) − 60 (item 3) + 45 (Quick check) − 20 (R3) − ~155 (R1: 356 → ~200) ≈ 4,275.

---

## 4. Chapter index (`index.md`)

By the coordinator after S3, STYLE §2 order. Title unchanged.

- **Story** (ix:3–5): verbatim, except ix:5's last sentence keeps "as Section 4.6 checks", and one sentence is added after ix:3's "Chapter 5 applies all of it with \( F = \nQ \).": "Section 4.3 introduces the method behind the limit proofs of the chapter: estimate the distance, find a threshold, then write the proof forwards."
- **What you need** (replaces ix:7; 25–40 labels). The list below is provisional: the drafter's grep of the delivered files decides it, listing only labels actually cited; the labels named here are known survivors at the time of S2. Chapters 1–3, chiefly Sections 2.3, 2.4, 3.2 and 3.3; *Logic and Proof*, Chapter 6; *Sets and Functions*, Chapters 1–5. From Chapters 2 and 3: @def-commutative-ring-and-field, @def-ordered-ring-and-field, @prp-ring-algebra, @prp-ordered-ring-rules, @prp-order-from-positives, @thm-integers-commutative-ring, @thm-integers-ordered-ring, @prp-integer-least-element, @exm-finite-ring-not-orderable, @prp-naturals-embed-integers, @prp-integers-embed-rationals, @thm-rationals-ordered-field, @prp-reciprocal-order, @thm-rationals-archimedean, @cor-rationals-archimedean-epsilon, @prp-rational-integer-part, @thm-no-rational-square-two, @exm-newton-rationals-sqrt2. From Chapter 1: the citing rule of Section 1.4 (@cor-omega-identification), @def-omega-arithmetic, @thm-omega-arithmetic-laws (4.2), @thm-omega-order, @prp-omega-order-arithmetic, @prp-omega-powers-parity. From *Logic and Proof*: @fd1:ax-induction, @fd1:prp-quantifier-negation (4.2), @fd1:prp-bounded-quantifier-negation, @fd1:prp-negated-implication, @fd1:prp-de-morgan (4.6 R3), @fd1:prp-arbitrarily-close-equal, @fd1:exm-not-allowed-catalogue. From *Sets and Functions*: @fd2:def-function, @fd2:thm-recursion, @fd2:prp-finite-max, @fd2:def-partial-order, @fd2:def-order-supremum (4.6), and for Exercise C1 of 4.2 @fd2:def-infinite, @fd2:def-finite, @fd2:cor-pigeonhole-finite-sets. (Gone after S3: @thm-well-defined-on-classes and @fd2:def-equivalence-relation with the old R1, @def-rational-order with C3, @fd1:def-rule-raa and @fd1:prp-bounded-quantifier-rules with binding rule 3.) Then one sentence each: ℚ(t) uses school polynomial algebra (*Algebraic Preliminaries*, Chapter 4) in examples and exercises only; nothing from *Analysis on the Real Line* and no fact about ℝ. *Algebraic Preliminaries*, Section 1.3 and the `@fd5:` labels disappear.
- **Time:** recomputed by `check_structure.py --words` after S3 (layout: about 22 h core / 35 h full); a departure is reported to the author, not overwritten.
- **Roadmap:** ix:13–18 verbatim except: the 4.3 bullet inserts after "its negation" the words "the method of proving a limit from the definition (work backwards to a threshold, then forwards)"; the 4.6 bullet ends "… and the review exercises return to the classes of Cauchy sequences, to induction, and to the negation laws of *Logic and Proof*, Chapter 6."
- **Named moves:** first entry new: "**Prove a limit from the definition** (@exm-method-limit-from-definition, Section 4.3): bound the distance by \( C/(n + 1) \), take \( N \) from Archimedes with ε/C, and write the proof forwards. Sections 4.4–4.6 keep its shape, with thresholds taken from hypotheses or with a second index." Then ix:22–25 verbatim (split ε; bound, then shrink; fix the bad ε; locate the missing limit), each pointing to where it first appears.
- **Threads, Summary, Terms:** if the delivered Chapter 1–3 indexes carry them (fd2 re-cut format), add: Threads: Archimedes (4.2 → 4.3 → 5.4 → 6.1); the Newton sequence (3.3 → 4.5 → 4.6 → 5.4). Terms: absolute value, Archimedean, bounded sequence, Cauchy sequence, convergent/divergent, distance, eventually, limit, null sequence, sequence.

## 5. Budgets and Time

As in the table at the top. Exercises: 4.1 −1 (B2); 4.2 −1 (C3); 4.3 B1 rewritten, B4 new; 4.4–4.5 unchanged; 4.6 R1 rewritten (shorter). Core track: all A, one B and one C per section, the exit checks, R1–R4. Chapter expected ≈ 2,946 + 3,976 + 4,889 + 3,580 + 4,908 + 4,275 ≈ 24,570 main-line words (layout ≈ 24,800), folds ≈ 1,515.

## 6. Deviations from the layout, and calls made here

1. **4.2 C3 deleted**, not moved to Chapter 6 (layout allows either). Chapter 6's blueprint may restore it from `b401a06` if it wants the positive-set argument.
2. **4.2 Step 4 stays on the main line**; only Steps 1–3 fold (layout named "陳述、Idea 與唯一性" as what stays; Step 4 is the order half that 4.2's later proofs and Chapters 5–6 use).
3. **4.3 adds a second worked example and B4**, so its expected count (~4,890) exceeds the layout's 4,800, within the 5,000 cap.
4. **Named moves keep four entries without boxes** (precedent fd2 Chapter 2); only the 4.3 method has a box, as the layout's §5 list says.
5. **4.6 R1 keeps only the closure facts** (layout §3 row 4.6); the S1 draft's parts on ~ and on well-definedness were cut at S2 as Chapter 5's theorems.
6. **The folds of 4.1 (41:143), 4.2 (part (d)) and 4.3 (the bound part of `prp-tail-change-ordered-field`, the "Infinitely many properties" sentences)** are mandatory budget items, not reserves (S2).
7. **The citation rule** (binding rule 3) is stated once in 4.1 instead of the old "by their letters" convention.

## 7. S2a: claims to verify

1. 4.1 Quick check: \( \abs{x - 1} < 2 \wedge \abs{x + 1} < 2 \iff -1 < x < 1 \).
2. 4.2 Quick check: \( (3 \cdot 1_F)(4 \cdot 1_F) - 5 \cdot 1_F = 7 \cdot 1_F \ne 0 \). The new "map" paragraph and the folded Steps 1–3 together still prove existence (well defined, three equations, \( \iota_F(n) = n \cdot 1_F \)); Step 4 reads Step 3's additivity and the formula of the main-line map paragraph (with \( q \ge 1 \)). The folded part (d) of `prp-naturals-in-ordered-field` is still citable (§12.0).
3. `exm-limit-from-definition`: the distance \( 1/(2(2n^2 + 3)) \); \( 4n^2 - n + 5 > 0 \) for every \( n \in \nN \), in the scratch work and in the moved proof (43:322, cases \( n \ge 1 \) and \( n = 0 \)) alike; each table row follows from the one above; the new closing sentence replaces 43:326's.
4. `exm-method-limit-from-definition`: in an Archimedean \( F \), \( N = \max\{N', n_0\} \) yields a valid proof whenever step (2)'s bound holds for \( n \ge n_0 \); the box is ≤ 130 words.
5. `exm-limit-alternating-numerator`: \( a_n - 2 = ((-1)^n - 2)/(n + 1) \); the distances \( 1, 3/2, 1/3, 3/4, 1/5 \) for \( n = 0, \dots, 4 \); the Quick check (step (3) gives 31; the least valid \( N \) is 30, failing at \( n = 29 \)).
6. New B1: (a) \( -10/(n + 4) \) and the bound \( 10/(n + 1) \); (b) for \( n \ge 1 \), \( n + 5 \le 6n \), \( 6/n \le 12/(n + 1) \), and the strict chain.
7. B4: verdicts T, F, T, T, F, T; \( (-1)^{2n} = 1 \), \( (-1)^{2n+1} = -1 \); (e)'s factors and the ε = 1 argument; (f)'s discreteness transfer from ℤ to ℚ.
8. 4.4 Quick check (|a| ≤ 3) and the folded second route still cites only earlier results.
9. 4.5: the negation display unchanged; the Multiples sentence ("carries over" against `thm-limit-laws-ordered-field` (b), pairs \( m, n \ge N \), \( c = 0 \) case by (a)); the sign-proof opening cites only fd1; Quick check (\( a_n = 1 - 4/(n + 1) \), \( c = 1/2 \), \( N = 7 \), \( a_6 = 3/7 \); \( c = 1/5 \), \( N = 4 \) also valid: \( a_4 = 1/5 \)).
10. 4.6 R1: the three closure facts; no ideal vocabulary, no equivalence-relation or well-definedness content, and no `@fd5:` label remains in Chapter 4. 4.6 Quick check: least \( N \) with \( 1/N < 1/100 \) is 101.
11. After S3: no `@label` points past Chapter 4 in a proof; every citation in binding rule 5's list matches the delivered 1.4; `blueprint/check_blueprint.py` finds the four new labels unique.

## 8. Notes for S3 and S4

- **Drafters** (one workflow at a time; lean):
  - **(A) 4.3** (Opus): `03-limits.md`; sidecars `verify/ch04/exm-limit-from-definition.py` (from the second half of `exr-limits-b1.py`), `exm-limit-alternating-numerator.py` (distances, Quick check), `exr-limits-b1.py` (rewritten for the new B1), `exr-limits-b4.py` (counterexamples (b), (e); brute-force sanity of (a), (d), (f) on sample sequences).
  - **(B) 4.1, 4.2, 4.4, 4.5, 4.6** (Sonnet suffices: trims, folds and the texts given verbatim above): delete `verify/ch04/exr-rules-and-absolute-value-b2.py`; add the Quick-check checks to `def-absolute-value-ordered-field.py`, `prp-naturals-in-ordered-field.py`, `prp-limit-preserves-order-ordered-field.py`, and a new `thm-cauchy-not-null-sign.py` (the 4.6 check is inline). (B) cites `exm-method-limit-from-definition` (4.4–4.6), so it lands after (A) or in the same build check.
  - **Coordinator:** `index.md` last; NOTATION (no new symbols), STATUS (no new promises; the Ch4 rows lose the fd5 R1 dependency), ledger re-keys (`tools/ledger.py`): drop the two deleted labels' items, move `exr-limits-b1`'s item as in §3.3 item 11.
- **Checkers:** `./build.py check` (fd1–fd5, an1); `check_structure.py --book fd3` (0 fatal; `--words` against §0's table); `check_forward_deps`; `blueprint/originality.py ch04`.
- **Review (lean):** changed-only blind review of the 4.3 new subsection, B1, B4; the 4.2 fold boundary and new paragraph; the new Quick checks of 4.1–4.6; 4.5's rewritten Multiples sentence and the sign-proof opening; 4.6 R1; the three rule-name removals (42:349, 43:399, 46:343); the 4.4/4.5/4.6 back-references to the box; citation trims sampled, not reviewed line by line. Then S7.

---

## S2 replies (round 1)

Two blind reviews (R-a: 14 findings, R-b: 13). All applied unless stated.

**R-a**
1. *§3.2 Count double-counts item 9* (error). Applied: Count corrected to ≈ 4,086; the part (d) fold is now mandatory item 10 (≈ 3,976); table and §5 updated.
2. *§3.3 item 6, line references and the dangling "first part" sentence* (error). Applied: 43:318–326 moved; 43:326's last sentence replaced explicitly; the Archimedes sentence is from 43:328; item 12 drops the old ℚ(t) ledger line (43:435) with 43:328's ℚ(t) sentences.
3. *Box step (3) silent on Archimedes and on N ≥ n₀* (gap). Applied: step (3) now "If F is Archimedean, take N′ … and let N ≔ max{N′, n₀}"; box recounted (~125 words, one clause left to the scratch work); §7 claim 4 restated.
4. *§3.4 item 1 false sentence; stale B1 pointer* (error). Applied: the non-example clause is kept; "Exercise B1 of Section 4.3" → @exm-limit-from-definition.
5. *4.4 Idea "one change in step (3)"* (gap). Applied, merged with R-b 5: "keeps the shape of … the threshold comes from the hypotheses … the estimate bounds the distance by |a_n − a|, |b_n − b| through split ε or bound-then-shrink."
6. *4.5 Idea "step (2) of the box"* (gap). Applied, merged with R-b 5: "This is split ε, as in the uniqueness proof of Section 4.3, with the point a between the two terms; the threshold comes from the hypothesis, as in the limit laws."
7. *43:7 positivity of 1/(n + 1) in general F* (minor). Applied: the short form is kept (item 2); count adjusted (+15).
8. *Citation trims at 45:43 and 44:24 against binding rule 3* (minor). Applied: @prp-reciprocal-order (b) kept at 45:43; both sign-sensitive multiplications at 44:24 keep their citation.
9. *Sign proof depends on the Idea box* (minor). Applied: the opening negates @def-null-sequence-ordered-field with its fd1 citations.
10. *Multiples "word for word"* (minor). Applied: "carries over"; c = 0 is "the constant sequence 0, Cauchy by (a)"; the pairs m, n ≥ N are stated.
11. *What you need omits survivors* (minor). Applied: list marked provisional (the drafter's grep decides); @fd1:prp-quantifier-negation, @fd1:prp-de-morgan, @fd2:def-infinite, @fd2:def-order-supremum, @thm-omega-arithmetic-laws added. Not added: @fd1:prp-bounded-quantifier-rules and @fd1:def-rule-raa (removed by R-b 6) and @def-rational-order (42:455, inside the deleted C3); these are listed as "gone after S3".
12. *Forward pointer inside the definition; item 3 sentences in the wrong fold* (minor). Applied: the "a limit" clause goes into 43:52's "In words" sentence, the definition block stays verbatim; item 3's sentences get their own fold "Infinitely many properties".
13. *Two Quick checks back to back in 4.1* (minor). Applied: the new check follows the existing check's solution (after 41:200).
14. *§7 claim 2 incomplete; q ≥ 1 step* (minor). Applied: claim restated; the map paragraph says "Here q ≥ 1, so q·1_F ≥ 1_F > 0 (…)".

**R-b**
1. *R1 anticipates Chapter 5* (error). Applied: R1 keeps the closure facts only, solution ~90 words with the closing sentence on Chapter 5; @thm-well-defined-on-classes and @fd2:def-equivalence-relation leave the ledger line and What you need; 4.6 recounted (≈ 4,275); §6 item 5 records it.
2. *4.2 and 4.1 counts* (error). Applied: both reserves are now numbered mandatory items (4.1 item 11, ≈ 2,946; 4.2 item 10, ≈ 3,976); §5 total corrected to ≈ 24,570 (the old figure should have read 24,630).
3. *4.3 count too tight* (gap). Applied: the "Bounds" fold is mandatory item 11; per-element caps set for the new subsection (≤ 875 in all; Solution ≤ 200 rather than 180, because the moved 43:318–326 alone runs ~175 words with its display); Count ≈ 4,889, item 9's trims no longer counted twice; the S3 report gives measured counts.
4. *B4 (e) is a third copy* (gap). Applied: (e) is now "If (a_n b_n) is null, then (a_n) or (b_n) is null", false, with the (1 ± (−1)^n)/2 counterexample; verdicts still T, F, T, T, F, T; ledger and §7 updated (the sidecar's counterexamples (b), (e) cover it).
5. *Back-references misdescribe the box* (gap). Applied in 4.3 intro, 4.4 Idea, 4.5 Idea, index Story and Named moves ("keeps its shape"), and 4.6's Idea ("This keeps the shape of …"); §1 records the convention.
6. *Rule names in "verbatim" items* (gap). Applied: 42:349, 43:399, 46:343 rewritten as proposed; binding rule 3 names them; added to the review list.
7. *Item 4 changes the definition block* (gap). Applied (same as R-a 12).
8. *Quick-check density* (gap). Rule 6 restated as "at least two per section, at least one new"; a 4.6 check added (least N = 101, with ledger line). The extra 4.3 check is declined: 4.3 already has two (43:98 and the new one) and sits ~110 words under its cap.
9. *Dangling "first part" sentence; scratch-work bound differs from the proof* (minor). Applied: replacement sentence stated; the scratch work now uses 2(2n² + 3) − (n + 1) = 4n² − n + 5 > 0, matching 43:322; §7 claim 3 updated.
10. *"When to use it" omits Archimedes* (minor). Applied as proposed.
11. *43:113 says "remark"* (minor). Applied: the folded bullet names the fold.
12. *What you need seed list* (minor). Applied (same as R-a 11); @fd2:def-finite kept beside @fd2:def-infinite, since 42:415 cites it.
13. *Header word-count note* (minor). Applied as proposed.
