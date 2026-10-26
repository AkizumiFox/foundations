<!-- hand-written -->
# Blueprint: F3.2 Number Systems: The Integers (fd3 Chapter 2, re-cut), stage S1

**Status: S1, 2026-10-26.** Next: S2 (blind referees), S2a, S3.

**What this is.** The S1 blueprint for fd3 Chapter 2 under the approved layout `fd3/authoring/design/layout-proposal.md` (§0 Q2 「整章移到 fd5 (Recommended)」: only division with remainder stays, as 2.5; §0 Q3 「分兩章 (Recommended)」: ℤ here, ℚ in Chapter 3; §3 Chapter 2 rows; §5; §9 structural record). A drafter executes it with this file, the `fd3/src/ch02-integers/` files at `b401a06`, `authoring/STYLE.md` (§1 "House manner from fd2 on", §2, §6, §11.4–§11.6, §12.0, §12.1, §12.5, §12.14), `DRAFTING.md`, `PIPELINE.md` and `NOTATION.md`. The format follows `fd2/authoring/blueprints/ch02-functions.md`, leaner.

**Line references** are to `b401a06`: `21:`, `22:`, `23:` (old 2.3, whole), `25:` = files `01`, `02`, `03`, `05` of `ch02-integers/`. `04` and `index.md` are title-only stubs.

**Word counts** (main line to `## Exercises`, `check_structure.py --book fd3 --words`, at `b401a06`; the 23: split estimated by the ratio counted/raw of the whole file):

| § | File | Main line now | Budget | Pipeline |
|---|---|---|---|---|
| 2.1 | `01-integers-as-classes.md` | 3,934 | ≤ 5,000 (expected ~3,800) | S |
| 2.2 | `02-well-defined-operations.md` | 3,948 | ≤ 5,000 (expected ~4,050) | S |
| 2.3 | `03-commutative-rings.md` (23:1–142) | ~1,870 of 5,596 | ≤ 5,000 (expected ~3,000) | S (split) |
| 2.4 | `04-ordered-rings.md` (23:144–417) | ~3,725 of 5,596 | ≤ 5,000 (expected ~4,500) | S (split) |
| 2.5 | `05-division-with-remainder.md` | 3,643 | ≤ 5,000 (expected ~2,500) | F |

**House manner.** As in fd2 (STYLE §1, §12.14). No footnotes, jokes, history or first person. Nothing comes from `/home/akizumi/book`; every new example, item and answer below is the book's own.

**Binding rules.**
1. **Cite back only.** Chapter 2 cites fd1, fd2, and fd3 Chapter 1 and earlier sections of Chapter 2. Every `@label` named here was grepped at `b401a06`. Chapter 3 and later, and other volumes' later books, are named in prose only: at most one Looking-ahead box per section (STYLE §12.1), plus the approved prose pointers already in the moved text (§6). No new prose pointer to a later section is added outside a box, except the section renumbering of existing pointers listed in §6.
2. **No label is lost or renamed.** Every label now in 21:, 22:, 23:, 25: stays, with its name and statement letters. Labels that change file: everything after 23:143 (to `04-ordered-rings.md`), except `exr-ordered-rings-b1`, which stays in `03` as 2.3's B1 (exercise ids are stable keys, STYLE §6). `exr-division-with-remainder-c1` is parked (§4.5 item 13).
3. **Chapter 1 is being rewritten (layout §0, §3: F).** Chapter 2 cites only Chapter 1 labels that the layout keeps with their letters: `def-omega-arithmetic` (a)–(b), `thm-omega-arithmetic-laws` (a)–(g), `cor-omega-successor-cancellation`, `thm-omega-order` (a), (b), (d), `prp-omega-order-arithmetic` (a)–(g), `thm-omega-well-ordering`, `thm-omega-induction`, `thm-omega-recursion`, `cor-omega-identification` (b), `prp-omega-powers-parity` (d), `def-peano-system`. Nothing in Chapter 2 may cite `def-omega-arithmetic` (c) (numerals as von Neumann sets) or say that 0 is ∅: in the re-cut, ℕ is a Peano system. If the Chapter 1 S1 renames or reletters any of these, the coordinator patches Chapter 2's citations in the same S3 pass.
4. **Statements that change.** None. `thm-integers-division-remainder` keeps the single item (a) (its (b) is parked, layout §9). All other statements verbatim.
5. Quick checks about one per 800–1,000 main-line words. No drill banks.

---

## 1. Devices as applied

- **Method boxes** (≤ 130 words; **Template.**, **When to use it.**, **The usual failure.**). New: `exm-method-one-argument-at-a-time` (2.2), `exm-method-reduce-to-level-below` (2.3), `exm-method-one-positive-element` (2.4). Names fixed here (layout §5's provisional names kept; grepped free). Back-references only (Idea level, no new box): `@fd2:exm-method-relation-properties` (2.1), `@fd2:exm-method-well-definedness` (2.2), `@fd2:exm-method-least-element` (2.4, 2.5), `@fd2:exm-method-uniqueness` (2.5).
- **`[Scratch work]` with a Givens/Goal table** at each new method's first full appearance: `prp-integer-operations-well-defined`, product case (2.2); `thm-integers-commutative-ring` (2.3); `prp-ordered-ring-rules` (c) (2.4).
- **Two worked examples per method:** 2.2: the product check in `prp-integer-operations-well-defined` and `exm-ill-defined-first-coordinate` (b) (kept); 2.3: the table of `thm-integers-commutative-ring` and **new** `exm-integer-laws-two-routes`; 2.4: `prp-ordered-ring-rules` (c), (d) and **new** `exm-product-of-inequalities`.
- **Prove or disprove** (new): 2.2 `exr-well-defined-operations-b3`, 2.3 `exr-commutative-rings-b2`, 2.4 `exr-ordered-rings-b3`. 2.1 and 2.5 are not method sections.
- **Fading.** Each box: full at its first use, Idea afterwards (2.2 B3 (d); 2.3 B1, C1 and 2.4's (P1)/(P2); `prp-ordered-ring-rules` (d)–(h) and 2.5's (e)), terse for (i).
- **Motivation first:** 2.1's naive attempt (kept); 2.2 fd2's ill-defined class map; 2.3 ℕ's one missing law; 2.4 "an inequality is about one difference"; 2.5 the question 「在建構出來的 ℤ 上，每個整數仍是偶數或奇數嗎？」 (layout §3).

## 2. Section map

Budgets: the table at the top. Changes: §4.

## 3. Labels

**Kept in place:** every label of 21:, 22:, 25: (except `exr-division-with-remainder-c1`, parked), and of 23:1–142 plus `exr-ordered-rings-b1`.
**Move to `04-ordered-rings.md`:** `def-ordered-ring-and-field`, `prp-order-from-positives`, `def-integer-order`, `thm-integers-ordered-ring`, `prp-ordered-ring-rules`, `prp-integer-least-element`, `exm-finite-ring-not-orderable`, `exr-ordered-rings-a1`, `-b2`, `-c1`.
**New** (all grepped free at `b401a06`):
- 2.2: `exm-method-one-argument-at-a-time`; `exr-well-defined-operations-b3`.
- 2.3: `exm-method-reduce-to-level-below`, `exm-integer-laws-two-routes`; `exr-commutative-rings-a1`, `-b2`, `-c1`.
- 2.4: `exm-method-one-positive-element`, `exm-product-of-inequalities`; `exr-ordered-rings-b3`.
- 2.5: `exr-division-with-remainder-c2`, `-r1`, `-r2`, `-r3`.

Printed titles follow the place (STYLE §6): in 2.3, `exr-ordered-rings-b1` is **[B1: Three rows in detail]**, `exr-commutative-rings-b2` is **[B2: Prove or disprove]**; in 2.4, `exr-ordered-rings-b2` is **[B1: The wrong positive set]**, `exr-ordered-rings-b3` is **[B2: Prove or disprove]**; in 2.5, `-c2` is **[C1: Exit check: remainders of squares]**, `-r1`–`-r3` are **[R1]**–**[R3]**.

---

## 4. Per-section plans

### 4.1 Section 2.1: The Integers as Classes of Pairs (`01`, S)

Budget 3,934 → ~3,800. Scaffold: Idea (the equivalence-relation check is fd2's method).

1. **Delete** the S3 comment 21:3.
2. **Opening, 21:5, rewritten** (~120 words): "Chapter 1 took the natural numbers to be a Peano system and built on it addition, multiplication and the order, with the laws of arithmetic and well-ordering; by Section 1.4 any two Peano systems are alike, and from here on \( \nN \) is that system (@cor-omega-identification, with the citing rule of Section 1.4)." Then 21:5's argument that \( 5 + x = 3 \) has no solution, verbatim, and its last sentence ("This section builds a larger set …") verbatim. Delete "from the axioms for sets".
3. **21:7–18 ("What we use about the natural numbers") compressed** to ~150 words: keep the heading and the bullet list, one line per bullet, labels as now; drop from the first bullet "and the numerals \( 0 \coloneqq \emptyset \), …" and write "the numerals \( 1 \coloneqq \mathrm{S}(0) \), \( 2 \coloneqq \mathrm{S}(1) \), …, with \( n + 1 = \mathrm{S}(n) \)" citing @def-omega-arithmetic only by its letters (a), (b) (binding rule 3). Keep 21:9's exemption for numeral sums and 21:18's last two sentences.
4. **21:20–36 verbatim** (the naive attempt is the layout's hook).
5. **21:38–60 verbatim.** After 21:60 add the **Idea back-pointer** into the existing Idea 21:67–71, first sentence: "This is the check of @fd2:exm-method-relation-properties: three clauses, each unwound to an equation in \( \nN \)." Rest of the Idea verbatim.
6. **21:73–91 verbatim.** **21:93 trimmed** to ~60 words: "The answer to the prompt is the last line of (Eq3). Subtracting \( c + d \) would need a check that the difference exists in \( \nN \) (@prp-omega-order-arithmetic (a)), and reading the difference off uses uniqueness, itself proved by cancellation. Cancellation removes \( c + d \) for every value, with no check."
7. **New Quick check** after 21:95: "Which classes contain \( (4, 0) \), \( (0, 4) \) and \( (4, 4) \)? Is any pair in two of them?" *Solution:* \( [(4, 0)] = \{ (y + 4, y) : y \in \nN \} \), \( [(0, 4)] = \{ (x, x + 4) \} \), \( [(4, 4)] = [(0, 0)] \), the diagonal (cross sums \( 4 + 0 = 4 + 0 \)). No pair lies in two: the classes are distinct (cross sums \( 4 + 4 \ne 0 + 0 \), \( 4 + 0 \ne 0 + 0 \), \( 0 + 0 \ne 4 + 0 \)), and distinct classes are disjoint (@fd2:thm-classes-partition).
8. **21:97–152 verbatim**, except 21:116: keep the argument, drop the label tags after the first of each kind ("by the same two steps as for \( [(3, 5)] \)" already covers the cancellation; cut the repeated @-citations of `thm-omega-arithmetic-laws (b)` and `prp-omega-order-arithmetic (b)`, ~40 words). 21:152's pointer "Section 3.1" stays (approved).
9. **21:154–158 verbatim. 21:160 cut** except its first sentence ("The class of \( (0, 0) \) is the diagonal; it will be the zero of \( \nZ \).") appended to 21:158. The etymology and its "Section 3.1" go (layout §3).
10. **21:162–198 verbatim.** After 21:198 a **new Quick check**: "Find the normal forms of \( [(17, 9)] \) and \( [(9, 17)] \), and a third pair in each class." *Solution:* \( 17 = 9 + 8 \), so \( [(17, 9)] = [(8, 0)] \); \( [(9, 17)] = [(0, 8)] \) (@prp-integer-normal-form (a)). Third pairs: \( (18, 10) \) and \( (10, 18) \), since \( 17 + 10 = 9 + 18 \).
11. **21:200–212 verbatim**, with 21:201's pointer "Section 2.3 gives it" → "Section 2.4 gives it" (renumbering, §6).
12. **Exercises verbatim** (A1, B1, B2, C1 exit check). Not a method section: no Prove-or-disprove.
13. **Ledger:** 21:330 keeps; rewrite nothing else; add lines for the two Quick checks (numeral cross sums; `thm-classes-partition`); drop any line citing the von Neumann numerals (none at `b401a06`; check).

**Count.** ≈ 3,820.

### 4.2 Section 2.2: Well-Definedness, and the Arithmetic of the Integers (`02`, S)

Budget 3,948 → ~4,050. Method section; full scaffold.

1. **Delete** the S3 comment 22:3. **22:5–13 verbatim.**
2. **22:15–37 verbatim** (the theorem statement).
3. **22:38**: "(c) the positive integers in Section 2.3" → "Section 2.4" (§6).
4. **Idea 22:40–42**: prepend one sentence: "Clause (a) is @fd2:exm-method-well-definedness turned into a theorem: steps (1)–(3) of that method are its hypothesis, and step (4) is the graph built below." Rest verbatim.
5. **Proof 22:44–64.** (a) and (c) verbatim. (b): keep the first paragraph 22:53–57 (the one-argument-at-a-time step) on the main line; move the second paragraph 22:59 (the graph \( G_G \), a repeat of (a)) into a **second-reading fold** `title="The graph of G, checked as in (a)"`, verbatim, and replace it on the main line by: "The rest is the proof of (a) with pairs of classes in place of classes: the graph of all \( (([x], [y]), [g(x, y)]) \) has an output for each pair of classes, and only one, by the paragraph above and @fd2:thm-classes-partition (b)." (~170 words leave the main line, ~45 return.)
6. **22:66–98 verbatim.**
7. **22:100–102 replaced** by the method box **`exm-method-one-argument-at-a-time`** `[Method: check on representatives, one argument at a time]`:
   - **Template.** To show that \( [x] \ast [y] \coloneqq [g(x, y)] \) is well defined: (1) fix \( y \), take \( x \sim x' \), and derive \( g(x, y) \sim g(x', y) \) from the single equation that \( x \sim x' \) unwinds to; (2) fix \( x' \), take \( y \sim y' \), and derive \( g(x', y) \sim g(x', y') \), or, if \( g(x, y) = g(y, x) \) for all \( x, y \), get (2) from (1) with the roles exchanged; (3) conclude by @thm-well-defined-on-classes (b). A map of one class needs (1) only, and (a).
   - **When to use it.** Every operation on a quotient defined by a formula on representatives: the sum and product of \( \nZ \) here, and of every later quotient built the same way.
   - **The usual failure.** Changing both arguments at once and losing track of which equation was used; checking one numerical instance; using a law of \( \nZ \) to check an operation of \( \nZ \) (the computation must stay in \( \nN \)); claiming symmetry for a formula that is not symmetric, such as \( [(a + d, \ b + c)] \).
   One sentence before the box: "The proof below uses the move this chapter is built on, after @fd2:exm-method-well-definedness:"
8. **New Quick check** after the box: "Does \( [(a, b)] \mapsto [(a + a, \ b)] \) define a function \( \nZ \to \nZ \)?" *Solution:* No. \( (0, 0) \sim (1, 1) \), but the outputs \( (0, 0) \) and \( (2, 1) \) have cross sums \( 0 + 1 \ne 0 + 2 \). In school terms the rule computes \( 2a - b \), which is not a function of \( a - b \).
9. **`prp-integer-operations-well-defined` (22:104–152).** Statement verbatim. **Replace the Idea 22:110–114** by a `[Scratch work]` idea (≤ 20 lines). Text: "The sum is one line; the product is the real check. Take the first argument (step (1) of the box):

   | Givens | Goal |
   |---|---|
   | \( (a, b) \sim (a', b') \); \( (c, d) \) fixed | \( g_\cdot((a, b), (c, d)) \sim g_\cdot((a', b'), (c, d)) \) |
   | \( a + b' = b + a' \) | \( (ac + bd) + (a'd + b'c) = (ad + bc) + (a'c + b'd) \) |
   | every term of the goal contains \( c \) or \( d \); the given contains neither | multiply the given by \( c \), and, read from right to left, by \( d \) |
   | \( ac + b'c = bc + a'c \) and \( bd + a'd = ad + b'd \) | add the two and regroup: the goal |

   Both formulas are unchanged when the two input pairs are exchanged, so step (2) comes free. *Before reading on: why may we change one argument at a time, rather than both at once?*" Proof 22:116–152 verbatim. 22:154 (answer to the prompt) verbatim.
10. **22:156–184 verbatim.** `exm-ill-defined-first-coordinate` is the second worked example (part (b) is a success by step (1), part (a) a failure).
11. **22:186–188 rewritten** (binding rule 3; ~70 words): "The integers were built to contain the natural numbers and more. What \( \nZ \) contains is a **copy** of \( \nN \): the classes in normal form \( [(n, 0)] \), each a set of pairs. Whether a natural number \( n \) is itself an element of \( \nZ \) depends on what the elements of a Peano system are, which the axioms leave open (Section 1.5); the copy is all we use, and it has the same arithmetic." Ledger 22:387 is rewritten to match.
12. **22:190–228 verbatim. 22:229**: "in Section 2.3" → "in Section 2.4" (§6). **22:231–239 verbatim** except 22:235 "a set built from \( \omega \)" → "a set built from \( \nN \)". **22:241–249 verbatim**, with 22:249's last sentence → "Section 2.3 checks that these operations obey the usual laws, by reducing each law to a law of \( \nN \); Section 2.4 orders \( \nZ \)."
13. **Exercises.** A1, B1, B2, C1, C2 verbatim. **New B3** (`exr-well-defined-operations-b3`, `[B3: Prove or disprove]`), placed after B2:
   - Stem: "Prove or disprove that each rule defines a function. (a) \( \nZ \times \nZ \to \nZ \), \( ([(a, b)], [(c, d)]) \mapsto [(a + d, \ b + c)] \). (b) \( \nZ \to \nZ \), \( [(a, b)] \mapsto [(b, \ a + b)] \). (c) \( \nZ \times \nZ \to \nZ \), \( ([(a, b)], [(c, d)]) \mapsto [(ad, \ bc)] \). (d) \( \nZ \to \nZ \), \( [(a, b)] \mapsto [(a \cdot a + b \cdot b, \ a \cdot b + b \cdot a)] \)."
   - *Solution.* (a) **True.** The formula is not symmetric, so both steps are needed. First argument: if \( a + b' = b + a' \), then \( (a + d) + (b' + c) = (a + b') + (c + d) = (b + a') + (c + d) = (b + c) + (a' + d) \). Second argument: if \( c + d' = d + c' \), then \( (a + d) + (b + c') = (a + b) + (d + c') = (a + b) + (c + d') = (b + c) + (a + d') \). Rearrangements by @thm-omega-arithmetic-laws (b), (c); conclude by @thm-well-defined-on-classes (b). The rule is \( (x, y) \mapsto x + (-y) \). (b) **False.** \( (0, 0) \sim (1, 1) \), with outputs \( (0, 0) \) and \( (1, 2) \), and \( 0 + 2 \ne 0 + 1 \). The heuristic predicts it: \( b - (a + b) = -a \) depends on \( a \), not on \( a - b \). (c) **False.** \( (1, 0) \sim (2, 1) \); with \( (c, d) = (0, 1) \) the outputs are \( (1 \cdot 1, 0 \cdot 0) = (1, 0) \) and \( (2 \cdot 1, 1 \cdot 0) = (2, 0) \), and \( 1 + 0 \ne 0 + 2 \). (d) **True.** The output is \( g_\cdot(x, x) \) for \( x = (a, b) \). If \( x \sim x' \), then \( g_\cdot(x, x) \sim g_\cdot(x', x) \sim g_\cdot(x', x') \) by the two hypotheses checked in @prp-integer-operations-well-defined, and transitivity joins them (as in @exr-well-defined-operations-c2); @thm-well-defined-on-classes (a) applies. The rule is \( x \mapsto x \cdot x \).
14. **Ledger:** rewrite 22:387 ("0 ∉ ℤ") to the new paragraph (no claim to check: the question is left open; Section 1.5 prose pointer); re-key 22:390 and 22:389 to F3.2 §03/§04; add lines for the Quick check (numeral cross sums) and B3 (rearrangements, cited; counterexample numerals; sidecar).

**Count.** ≈ 4,140. **Reserve:** trim the remark 22:68–70 to its first three sentences (−50).

### 4.3 Section 2.3: Commutative Rings; the Integers Are One (`03`, S, split)

Budget ~1,870 → ~3,000. Method section; full scaffold.

1. **Split.** Title line → `# Commutative Rings; the Integers Are One`. Delete the S3 comment 23:3. Everything from 23:144 (`## Ordered rings`) through 23:417 and the exercises `exr-ordered-rings-a1`, `-b2`, `-c1` with their ledger lines move to `04-ordered-rings.md` (§4.4). `exr-ordered-rings-b1` (23:448–462) stays here.
2. **Opening, 23:6 rewritten** (~110 words), with the non-example 23:41 moved up as the hook: "Sections 2.1 and 2.2 built \( \nZ \) with well-defined operations \( + \), \( \cdot \) and \( - \). Why was it built at all? \( \nN \) already adds and multiplies by all the usual laws but one: it has no negatives (\( 1 + x \ne 0 \) for every \( x \in \nN \), @cor-omega-successor-cancellation). This section collects the laws of school algebra into one definition, a **commutative ring**, checks them for \( \nZ \) by reducing each to a law of \( \nN \), and derives the consequences that hold in every commutative ring." 23:41 itself stays where it is, shortened to its first and last sentences (~45 words), since the opening now carries the computation.
3. **23:8–40 verbatim.** 23:34's external pointers stay.
4. **23:43–47 verbatim**, except 23:46's last sentence: "proved later in this section from the order axioms" → "proved in Section 2.4 from the order axioms" (§6).
5. **23:49–51**: keep 23:49; replace 23:51 by one lead sentence: "To prove a law for classes, compute both sides through representatives; the two pairs of natural numbers are then equal or related, and the classes agree." The named move goes into the box (item 7).
6. **`thm-integers-commutative-ring` (23:53–96).** Statement verbatim. **Replace the Idea 23:59–61** by `[Scratch work]` (≤ 15 lines): "Take (F9), the law with the most terms.

   | Givens | Goal |
   |---|---|
   | \( x, y, z \in \nZ \) | \( x(y + z) = xy + xz \) |
   | \( x = [(a, b)] \), \( y = [(c, d)] \), \( z = [(e, f)] \): every class has a representative (@fd2:def-quotient-set) | two classes, each computed by @def-integer-operations from these representatives |
   | left: \( (a(c + e) + b(d + f), \ a(d + f) + b(c + e)) \); right: \( ((ac + bd) + (ae + bf), \ (ad + bc) + (af + be)) \) | equal pairs, or related pairs |
   | distribute in \( \nN \), then regroup four terms | the same pair: the classes are equal |

   The operations are functions (@prp-integer-operations-well-defined), so any representatives may be used. Only (F4) will need \( \sim \); only (F5) is long." Proof 23:63–94 verbatim; 23:96 verbatim.
7. **Method box `exm-method-reduce-to-level-below`** `[Method: reduce to the level below]`, after 23:96:
   - **Template.** To prove a law about classes whose operations are defined on representatives: (1) write each element as \( [p] \) for a representative \( p \); (2) compute each side with the defining formulas, which may use any representatives, since the operations are well defined; (3) compare the two resulting representatives at the level below, by its laws: equal, or related; (4) conclude that the classes are equal (@fd2:thm-classes-partition (b)).
   - **When to use it.** Laws and identities in \( \nZ \), with \( \nN \) as the level below; and in any structure whose operations are formulas in a known ring (2.3 C1).
   - **The usual failure.** Claiming equal pairs where only \( \sim \) holds (the row (F4)); computing with representatives before the operation is known to be a function; using a law of \( \nZ \) inside the computation in \( \nN \), which is circular.
8. **23:98–100 (remark) verbatim**; "the identification of Section 2.2" stays.
9. **New Quick check** after the remark: "Is \( [(5, 5)] \) a second zero of \( \nZ \), besides \( [(0, 0)] \)?" *Solution:* No: it is the same element. \( 5 + 0 = 5 + 0 \), so \( (5, 5) \sim (0, 0) \) and the classes are equal (@fd2:thm-classes-partition (b)). A pair is a name; the zero is the class. (This agrees with the uniqueness of zero proved next.)
10. **23:102–140 (`prp-ring-algebra`) verbatim**, including its Idea (it already states the "defining equation" move; Idea level).
11. **New worked example `exm-integer-laws-two-routes`** `[One law, two routes]`, after the proof (~200 words). Statement: "Prove that \( (-x)y = -(xy) \) for all \( x, y \in \nZ \) in two ways: (a) by reducing to the level below; (b) from (F1)–(F9) alone." *Solution:* (a) Let \( x = [(a, b)] \), \( y = [(c, d)] \). Then \( -x = [(b, a)] \), so \( (-x)y = [(bc + ad, \ bd + ac)] \); and \( xy = [(ac + bd, \ ad + bc)] \), so \( -(xy) = [(ad + bc, \ ac + bd)] \) (@def-integer-operations). The two pairs are equal by commutativity of \( + \) in \( \nN \) (@thm-omega-arithmetic-laws (b)). (b) This is @prp-ring-algebra (c), with \( a = x \), \( b = y \), since \( \nZ \) is a commutative ring (@thm-integers-commutative-ring). Aftermath (two sentences): "Route (a) is shorter here, but it proves the law only for \( \nZ \). Route (b) proves it in every commutative ring at once, which is why @prp-ring-algebra is stated for rings."
12. **23:142 verbatim.** Then a **Quick check**: "Show that \( (-1)a = -a \) in every commutative ring." *Solution:* By @prp-ring-algebra (c), \( (-1)a = -(1 \cdot a) \), and \( 1 \cdot a = a \cdot 1 = a \) by (F6), (F7).
13. **Exercises** (new group headers `## Exercises`, `### A.`, `### B.`, `### C.`):
   - **A1** (`exr-commutative-rings-a1`, `[A1]`). "(a) State (F4) with its quantifiers, and say why the zero ring satisfies it. (b) Name the move by which @thm-integers-commutative-ring was proved, and say which row of its table needed \( \sim \) rather than equality of pairs. (c) True or false, with a reason: in every commutative ring, \( ab = 0 \) implies \( a = 0 \) or \( b = 0 \). (d) Prove from (F1)–(F9) that \( (-1)(-1) = 1 \) in every commutative ring." *Solution:* (a) For every \( a \in R \) there is \( -a \in R \) with \( a + (-a) = 0 \). In \( \{0\} \), \( -0 \coloneqq 0 \) works, since \( 0 + 0 = 0 \). (b) Reduce to the level below; only (F4): \( (a + b, b + a) \) is related to \( (0, 0) \), not equal to it. (c) False: in the integers modulo \( 6 \), \( [2][3] = [0] \) with \( [2], [3] \ne [0] \) (the warning after @def-commutative-ring-and-field, ring laws taken for granted there). (d) @prp-ring-algebra (c) with \( a = b = 1 \) gives \( (-1)(-1) = 1 \cdot 1 \), and \( 1 \cdot 1 = 1 \) by (F7).
   - **B1** = `exr-ordered-rings-b1`, verbatim, title `[B1: Three rows in detail]` (unchanged).
   - **B2** (`exr-commutative-rings-b2`, `[B2: Prove or disprove]`). "Prove or disprove. (a) For all \( x, y \in \nZ \), \( -(x + y) = (-x) + (-y) \). (b) In every commutative ring, \( a \cdot a = a \) implies \( a = 0 \) or \( a = 1 \). (c) The set \( \nN \times \nN \) itself, with \( (a, b) + (c, d) \coloneqq (a + c, \ b + d) \) and \( (a, b) \cdot (c, d) \coloneqq (ac + bd, \ ad + bc) \), is a commutative ring. (d) In every commutative ring, \( a + b = a \) implies \( b = 0 \)." *Solution:* (a) **True**, by reduction: with \( x = [(a, b)] \), \( y = [(c, d)] \), both sides are the class of \( (b + d, \ a + c) \) (@def-integer-operations). (b) **False.** In the integers modulo \( 6 \) (ring laws taken for granted, as in the warning after @def-commutative-ring-and-field), \( [3][3] = [9] = [3] \), since \( 9 - 3 = 6 \), and \( [3] \) is neither \( [0] \) nor \( [1] \). (c) **False:** (F4) fails. The zero would be \( (0, 0) \), the only pair with \( (a, b) + z = (a, b) \) for all pairs (take \( (a, b) = (0, 0) \) and cancel, @prp-omega-order-arithmetic (b)); and \( (1, 0) + (x, y) = (1 + x, \ y) \ne (0, 0) \), since \( 1 + x = x + 1 \ne 0 \) (@thm-omega-arithmetic-laws (b), @cor-omega-successor-cancellation). Passing to classes is what supplies negatives. (d) **True.** Add \( -a \): \( b = 0 + b = ((-a) + a) + b = (-a) + (a + b) = (-a) + a = 0 \), by (F3), (F1), (F4), (F2) and the hypothesis.
   - **C1** (`exr-commutative-rings-c1`, `[C1: A ring in disguise]`). "On \( \nZ \) define \( x \oplus y \coloneqq x + y - 1 \) and \( x \odot y \coloneqq x + y - xy \). (a) Find the elements that play the parts of \( 0 \) and \( 1 \) in (F3), (F7), and the negative of \( x \) in (F4). (b) Prove (F9) for \( \oplus \), \( \odot \) directly. (c) Let \( \varphi(x) \coloneqq 1 - x \). Show that \( \varphi(x \oplus y) = \varphi(x) + \varphi(y) \), \( \varphi(x \odot y) = \varphi(x)\varphi(y) \) and \( \varphi(\varphi(x)) = x \), and use this to prove (F5) for \( \odot \) without expanding." Hint ladder: rung 1 "In (a), solve \( x \oplus e = x \) for \( e \)."; rung 2 "In (c), apply \( \varphi \) to both sides of (F5) and use that \( \varphi \) is injective." *Solution:* (a) Zero \( 1 \): \( x \oplus 1 = x \). One \( 0 \): \( x \odot 0 = x + 0 - 0 = x \). Negative \( 2 - x \): \( x \oplus (2 - x) = 1 \). (b) \( x \odot (y \oplus z) = x + (y + z - 1) - x(y + z - 1) = 2x + y + z - 1 - xy - xz \), and \( (x \odot y) \oplus (x \odot z) = (x + y - xy) + (x + z - xz) - 1 \) is the same, by the ring laws of \( \nZ \) (@thm-integers-commutative-ring, @prp-ring-algebra (c)). (c) \( 1 - (x + y - 1) = (1 - x) + (1 - y) \); \( 1 - (x + y - xy) = (1 - x)(1 - y) \); \( 1 - (1 - x) = x \). So \( \varphi \) is injective (equal values give \( x = \varphi(\varphi(x)) = \varphi(\varphi(x')) = x' \)), and \( \varphi((x \odot y) \odot z) = (\varphi(x)\varphi(y))\varphi(z) = \varphi(x)(\varphi(y)\varphi(z)) = \varphi(x \odot (y \odot z)) \) by (F5) in \( \nZ \); injectivity gives (F5) for \( \odot \). Aftermath: the level below is now \( \nZ \), and \( \varphi \) carries every law across. **Marking scheme** (8): 2 for (a) with each element checked; 3 for (b), both sides expanded with the laws named; 3 for (c): 1 for the three identities, 2 for the injectivity step. Fatal: assuming the laws for \( \oplus \), \( \odot \) in (b).
14. **Ledger.** Lines 23:548, 23:550, 23:552, 23:553 stay; 23:551 moves with the Quick check to 2.4. New lines for each new block (A1 (c), B2 (b): ℤ/6, illustration only, as 23:548); sidecars as §8 (A).

**Count.** Expected 2,400–3,000 (the split estimate is rough); no reserve needed.

### 4.4 Section 2.4: Ordered Rings and the Rules for Inequalities (`04`, S, split)

Budget ~3,725 → ~4,500. Method section; full scaffold.

1. **File.** `04-ordered-rings.md` keeps its title line `# Ordered Rings and the Rules for Inequalities`; below it, 23:144–417 and the exercises `exr-ordered-rings-a1`, `-b2`, `-c1`, with their ledger lines 23:549, 23:551, 23:554–561.
2. **Opening frame** (new, before 23:146, ~90 words): "Section 2.3 made \( \nZ \) a commutative ring and proved the rules for equations from (F1)–(F9). Inequalities need the same treatment. In school, \( -3 < -2 \) is read off a number line; here there is no line, only classes of pairs. This section lists four order axioms, shows that an order is the same thing as a set of positive elements, orders \( \nZ \), and derives the rules for inequalities in every ordered ring. Each rule will come from one observation: \( a < b \) is a statement about the single element \( b - a \)." Then 23:146–148 verbatim, the heading `## Ordered rings` turned into the first subsection.
3. **23:150–215 verbatim.** The move named at 23:169 ("order from a positive set") stays a named move in prose (no box; it is `prp-order-from-positives`).
4. **23:217–245 verbatim.** 23:233 "Section 2.1's warning" stays. 23:245 "Recall from Section 2.2" stays.
5. **`thm-integers-ordered-ring` (23:247–292) verbatim.** Its Idea gets one clause after the first sentence: "each a fact about \( \nN \), reached by reducing to the level below (@exm-method-reduce-to-level-below)".
6. **23:294–297 verbatim.**
7. **23:299–307 verbatim** (multiples; the citations of @fd2:thm-recursion and @fd1:ax-induction through @cor-omega-identification (b) stand, binding rule 3).
8. **`prp-ordered-ring-rules` (23:309–355).** Statement verbatim. **Replace the Idea 23:327–329** by `[Scratch work]` for (c) (≤ 15 lines): "Every part is a comparison, and by @prp-order-from-positives a comparison \( a < b \) is the statement \( b - a > 0 \). Positive elements are closed under \( + \) and \( \cdot \). So the plan is always: write the goal as one difference, and build it from given positive elements. For (c):

   | Givens | Goal |
   |---|---|
   | \( a < b \), \( c > 0 \) | \( ac < bc \) |
   | \( b - a > 0 \), \( c > 0 \) (@prp-order-from-positives) | \( bc - ac > 0 \) |
   | \( (b - a)c > 0 \) by (O4) | \( bc - ac = (b - a)c \)? |
   | (F9), (F6), @prp-ring-algebra (c) | yes: the gap closes |

   (d) is (c) with \( -c \) in place of \( c \); (e), (f) apply (O4) to whichever of \( a \), \( -a \) is positive. We prove (i) first, since (b) and (g) use it." Proof 23:331–355 verbatim. 23:357 verbatim.
9. **Method box `exm-method-one-positive-element`** `[Method: turn the comparison into one positive element]`, after 23:357:
   - **Template.** To prove an inequality in an ordered ring: (1) rewrite the goal \( u < v \) as \( v - u > 0 \) (@prp-order-from-positives); (2) express \( v - u \) by the ring laws as a sum or product of elements known to be positive (or non-negative); (3) conclude by closure, (P1), or by @prp-ordered-ring-rules (b), (c); (4) translate back.
   - **When to use it.** Any rule for inequalities; comparisons in \( \nZ \) and, later, in every ordered field.
   - **The usual failure.** Multiplying by an element whose sign is unknown; treating \( \le \) as \( < \) in (O4); using a picture of the number line as a reason.
10. **23:359–361 (warning) shortened** to its first two sentences (the false rule and its counterexample, ~60 words). The rest becomes the **new worked example `exm-product-of-inequalities`** `[Multiplying two inequalities]` (~170 words): "Let \( R \) be an ordered commutative ring and \( 0 \le a < b \), \( 0 \le c < d \). Prove \( ac < bd \)." *Solution:* By the method, the goal is \( bd - ac > 0 \). Write \( bd - ac = b(d - c) + (b - a)c \) (ring laws: \( bd - bc + bc - ac \)). Here \( b > 0 \) (from \( 0 \le a < b \), @prp-ordered-ring-rules (i)) and \( d - c > 0 \), so \( b(d - c) > 0 \) by (O4); and \( (b - a)c \) is \( > 0 \) if \( c > 0 \) (O4) and \( = 0 \) if \( c = 0 \) (@prp-ring-algebra (b)). A positive element plus a non-negative one is positive (@prp-ordered-ring-rules (b)). Aftermath (one sentence): "The hypotheses \( a \ge 0 \), \( c \ge 0 \) are exactly what make the two summands non-negative; the warning shows what goes wrong without them."
11. **New Quick check** after the example: "Which positive element shows that \( a < b \) gives \( a + a < b + b \)?" *Solution:* \( (b + b) - (a + a) = (b - a) + (b - a) \) (ring laws), a sum of two positive elements, positive by (P1).
12. **23:363–369 verbatim** (Is ℤ a field?). **23:371–388 verbatim**, with an Idea added to `prp-integer-least-element` (2 lines): "Shift the set into \( \nN \) and use well-ordering there: the method of @fd2:exm-method-least-element, with @thm-omega-well-ordering in place of the school version (@fd2:cor-well-ordering-integers)." **23:389–416 verbatim. 23:417**: "a later chapter of this volume rebuilds them on the constructed \( \nZ \)" → "*Algebraic Preliminaries*, Chapter 1 rebuilds them on the constructed \( \nZ \)" (§6).
13. **Exercises.**
   - **A1** (label kept): (a)–(c) verbatim. (d) replaced: "(d) Use the method of @exm-method-one-positive-element to show: if \( a < b \) and \( c \le 0 \), then \( ac \ge bc \)." *Solution:* \( ac - bc = (a - b)c = (b - a)(-c) \) (@prp-ring-algebra (c)); \( b - a > 0 \) and \( -c \ge 0 \), so the product is \( > 0 \) by (O4) if \( c < 0 \), and \( 0 \) if \( c = 0 \) (@prp-ring-algebra (b)). So \( ac - bc \ge 0 \), that is, \( bc \le ac \).
   - **B1** = `exr-ordered-rings-b2` verbatim, retitled `[B1: The wrong positive set]`.
   - **B2** (`exr-ordered-rings-b3`, `[B2: Prove or disprove]`). "Prove or disprove. (a) In every ordered commutative ring, \( a < b \) implies \( a^2 < b^2 \). (b) In every ordered commutative ring with \( 1 \ne 0 \), \( a^2 + 1 > 0 \). (c) In \( \nZ \), if \( x > 0 \) and \( xy = x \), then \( y = 1 \). (d) In every ordered commutative ring, \( a < b \) and \( c < d \) imply \( a - d < b - c \). (e) In \( \nZ \), \( x < y \) implies \( x + 1 < y \)." *Solution:* (a) **False:** \( -3 < 1 \) in \( \nZ \), but \( (-3)^2 = 9 > 1 = 1^2 \). The true version needs \( a \ge 0 \) (@prp-ordered-ring-rules (g)). (b) **True:** \( a^2 \ge 0 \) (0 if \( a = 0 \), @prp-ring-algebra (b); positive otherwise, (e)), \( 1 > 0 \) by (e), and (b) with one strict hypothesis gives \( a^2 + 1 > 0 + 0 = 0 \). (c) **True:** \( x(y - 1) = xy - x = 0 \) and \( x \ne 0 \), so \( y - 1 = 0 \) by (f). (d) **True:** \( -d < -c \) by (a); add to \( a < b \) with (b), strict. (e) **False:** \( x = 0 \), \( y = 1 \). Discreteness gives only \( x + 1 \le y \) (@thm-integers-ordered-ring (c)).
   - **C1** verbatim.
14. **Ledger:** moved lines as item 1; add lines for the new blocks; sidecars as §8 (A).

**Count.** ≈ 4,300; expected ≤ 4,600.

### 4.5 Section 2.5: Division with Remainder (`05`, F)

Budget 3,643 → ~2,500. Title line → `# Division with Remainder` (layout §3). Scaffold: Idea (fd2's method of the least element).

1. **Delete** the S3 comments 25:3, 25:96, 25:134, 25:195.
2. **Opening (new, ~140 words), replacing 25:5:** "*Sets and Functions*, Section 1.1 proved that every integer is even or odd, and not both (@fd2:thm-even-or-odd), and Section 3.2 there proved division with remainder (@fd2:thm-division-algorithm). Both were proved for the integers of school, taken as known. The integers are now the set of classes built in Section 2.1. Is \( [(0, 7)] \), the class that school calls \( -7 \), still odd, and could some integer be even and odd at once? Nothing so far says. This section answers by proving division with remainder again, on the constructed \( \nZ \): the proof is fd2's, with each school fact replaced by a result of this chapter. Divisibility comes first, since uniqueness of the remainder rests on it." Then 25:7 verbatim, except "as in Section 3.3" → "as in Section 2.2" (the identification paragraph) (§6).
3. **25:9–23 trimmed** to ~200 words: keep 25:11, the two bold definitions 25:13 and 25:15 verbatim, 25:19's italic line, and 25:21 verbatim. Cut 25:17 and 25:23.
4. **`prp-divisibility-rules-integers` (25:25–80).** 25:25 → "The rules below are short consequences of the ring laws and the order." Statement verbatim (all eight letters; downstream cites every letter). Idea 25:44–46 verbatim, plus one clause at the end of its third sentence: "(the method of @exm-method-one-positive-element)". **Proof:** main line has 25:49, then (e) (25:65) and (g) (25:69) verbatim. Parts (a)–(d), (f), (h) (25:51–63, 25:67) go verbatim into a **second-reading fold** `title="Parts (a)–(d), (f) and (h)"` placed right after the main-line proof (order inside the fold: (a), (b), (c), (d), (h), (f)). The main-line proof's first sentence adds: "Parts (a)–(d), (f) and (h) are one-line identities, written out in the fold below; here are the two parts that use the order." Since (g) cites (h) and (d), and (e) cites nothing folded, the main line reads forward; the fold sits before any later citation of (a)–(d). 25:72 trimmed to its first two sentences. 25:74–80 (Quick check) verbatim.
5. **`thm-integers-division-remainder` (25:82–124).** 25:84 verbatim. Statement verbatim minus the S3 comment (single item (a)). **Idea 25:102–104 replaced** (~110 words): "This is @fd2:thm-division-algorithm, and the proof is fd2's: the method of @fd2:exm-method-least-element, with \( S \) the non-negative integers of the form \( a - kn \), and @prp-integer-least-element in place of the school least-element principle. The least one, \( r \), lies below \( n \), or else \( r - n \) would be a smaller one. Uniqueness is @fd2:exm-method-uniqueness: two remainders differ by a multiple of \( n \) and by less than \( n \), and @prp-divisibility-rules-integers (e) forbids a positive multiple of \( n \) below \( n \). What is new is only that every step is now a theorem about the constructed \( \nZ \)." Proof 25:106–121 verbatim; delete 25:122–123 (blank lines).
6. **25:126 trimmed** to two sentences: "For \( n = 0 \) the statement fails: no \( r \) satisfies \( 0 \le r < 0 \). Exercise B1 handles \( n < 0 \)." **25:128 verbatim** (the divisibility test; fd5 uses it).
7. **25:130–135 cut** (the remark is now the Idea; part (b)'s paragraph went with (b)).
8. **Quick check 25:137–143 replaced:** "Find the quotient and the remainder of \( a = -17 \) on division by \( n = 5 \). Why is \( -17 = (-3) \cdot 5 + (-2) \) not the answer?" *Solution:* \( q = -4 \), \( r = 3 \): \( (-4) \cdot 5 + 3 = -17 \) and \( 0 \le 3 < 5 \); by uniqueness this is the only such pair. \( -2 \) fails \( 0 \le r \).
9. **Warning 25:145–147** kept without its last sentence (the floor).
10. **25:149–176.** 25:151 → "Recall that an integer \( a \) is **even** if \( a = 2k \) for some \( k \in \nZ \), and **odd** if \( a = 2k + 1 \) for some \( k \in \nZ \) (@fd2:def-divides, as in @fd2:thm-even-or-odd), now read on the constructed \( \nZ \). With \( n = 2 \), the theorem answers the opening question." `cor-integers-even-odd`, its Idea and proof verbatim. 25:176 → (~70 words) "So \( -7 = (-4) \cdot 2 + 1 \) is odd and not even, as school says, and now by proof. Part (a) is @fd2:thm-even-or-odd on the constructed \( \nZ \), and part (b) is @fd1:thm-square-even-implies-even, whose proof used (a) and the computation above as school facts. For \( a \in \nN \), (a) is also @prp-omega-powers-parity (d) of Chapter 1." Delete 25:178.
11. **25:180–196 (Small primes) cut** from fd3. The remark moves verbatim to fd5 (§6), where its users are.
12. **Looking ahead** box at the end of the main line (~60 words): "*Algebraic Preliminaries*, Chapter 1 builds on this section: greatest common divisors and Bézout's identity, primes and unique factorization, and arithmetic modulo \( n \), all on the constructed \( \nZ \). Chapter 3 of this volume builds the rationals as classes of fractions, and its integer part of \( a/n \) is the quotient found here." (STATUS: F5.1 promise rows; F3.11 §02 for the quotient, keyed to wherever the Chapter 3 blueprint places part (b).)
13. **Exercises.**
   - A1, B1, B2 verbatim.
   - **C1 (old) parked:** `exr-division-with-remainder-c1` (25:255–273) with its ledger line 25:301 and sidecar (if any) is appended verbatim to `fd3/authoring/parked/from-3.1-division-part-b.md` under a heading "Parked exercise", header updated to name the label. It uses ℚ (@prp-rational-integer-part). The Chapter 3 blueprint decides its place, next to part (b).
   - **C1 (new)** (`exr-division-with-remainder-c2`, `[C1: Exit check: remainders of squares]`). "(a) Prove that for every \( a \in \nZ \), the remainder of \( a^2 \) on division by \( 4 \) is \( 0 \) or \( 1 \). (b) Deduce that no integer whose remainder on division by \( 4 \) is \( 3 \) is a sum \( x^2 + y^2 \) of two squares of integers. Name the result behind each step." *Solution:* (a) By @cor-integers-even-odd (a), \( a = 2q \) or \( a = 2q + 1 \). Then \( a^2 = 4q^2 = q^2 \cdot 4 + 0 \), or \( a^2 = 4q^2 + 4q + 1 = (q^2 + q) \cdot 4 + 1 \) (@prp-ring-algebra (d), ring laws; \( 4 = 2 \cdot 2 \) computed in \( \nN \)). Both have \( 0 \le r < 4 \), so by the uniqueness in @thm-integers-division-remainder (a) these are the remainders. (b) Write \( x^2 = 4k + s \), \( y^2 = 4l + t \) with \( s, t \in \{0, 1\} \) by (a). Then \( x^2 + y^2 = 4(k + l) + (s + t) \) with \( s + t \in \{0, 1, 2\} \), so \( 0 \le s + t < 4 \) and \( s + t \) is the remainder, by uniqueness; it is not \( 3 \). **Marking scheme** (10): 2 for the two cases from the corollary; 3 for the two expansions with the remainder form \( q' \cdot 4 + r \) displayed; 2 for invoking uniqueness with \( 0 \le r < 4 \) checked; 3 for (b), including that \( s + t \le 2 < 4 \) and uniqueness. Fatal: "remainder" used for a value outside \( [0, 4) \); omitting uniqueness in (b).
   - **R. Review** (new group, STYLE §11.5; this is the chapter's last section):
     - `exr-division-with-remainder-r1` `[R1]` (Chapter 1; recursion and induction). "Let \( f \colon \nN \to \nN \) satisfy \( f(0) = 0 \) and \( f(n + 1) = f(n) + 2n + 1 \) for every \( n \in \nN \). Prove that \( f(n) = n \cdot n \) for every \( n \)." *Solution:* Such an \( f \) exists and is unique by @thm-omega-recursion; the claim is proved by induction on \( n \) (@thm-omega-induction). Base: \( f(0) = 0 = 0 \cdot 0 \) (@def-omega-arithmetic (b)). Step: \( f(n + 1) = n \cdot n + 2n + 1 \), and \( (n + 1)(n + 1) = (n + 1)n + (n + 1) = (n \cdot n + n) + n + 1 \) by @def-omega-arithmetic (b) and @thm-omega-arithmetic-laws (e); \( n + n = 2n \) by \( 1 + 1 = 2 \) and @thm-omega-arithmetic-laws (d), (e). Method source: Chapter 1's induction on the recursion variable.
     - `-r2` `[R2]` (fd2 Chapter 2; injectivity and surjectivity). "Decide which of the maps \( \nZ \to \nZ \) are injective and which are surjective: (a) \( x \mapsto -x \); (b) \( x \mapsto 2x \); (c) \( x \mapsto x^2 \)." *Solution:* (a) Bijective: \( -(-x) = x \) (@prp-ring-algebra (a)), so equal values give equal inputs and every \( y \) is the value at \( -y \). (b) Injective: \( 2x = 2y \) gives \( 2(x - y) = 0 \), and \( 2 \ne 0 \) (\( 2 = 1 + 1 > 0 \)), so \( x = y \) (@prp-ordered-ring-rules (f)). Not surjective: \( 1 = 2x \) would make \( 1 \) even, but \( 1 = 2 \cdot 0 + 1 \) is odd (@cor-integers-even-odd (a)). (c) Neither: \( (-1)^2 = 1 = 1^2 \) (@prp-ring-algebra (c)); and \( x^2 \ge 0 > -1 \) (@prp-ordered-ring-rules (e)), so \( -1 \) is not a value. Methods: @fd2:exm-method-injectivity, @fd2:exm-method-surjectivity.
     - `-r3` `[R3]` (spiral, fd1 Chapter 2). "Prove that for every \( a \in \nZ \): if \( 3 \mid a^2 \), then \( 3 \mid a \)." *Solution:* By contraposition, as in @fd1:thm-square-even-implies-even. Suppose \( 3 \nmid a \). Division by \( 3 \) gives \( a = 3q + r \) with \( r \in \{1, 2\} \) (\( r \ne 0 \), else \( 3 \mid a \); \( r \le 2 \) by discreteness, as in @exr-division-with-remainder-b2). Then \( a^2 = 3(3q^2 + 2q) + 1 \) or \( a^2 = 3(3q^2 + 4q + 1) + 1 \), remainder \( 1 \ne 0 \), so \( 3 \nmid a^2 \) by the divisibility test after @thm-integers-division-remainder.
14. **Ledger.** Delete 25:285, 25:286, 25:301 (ℚ; 25:301 travels with parked C1), 25:288 (remark cut), 25:293, 25:294–296 (small primes; travel to fd5 with the remark). Rewrite 25:292 to the new 25:176. Keep the rest. Add lines for the new blocks; sidecars as §8 (C). The two stale ledger items (`thm-integers-division-remainder` statement and proof, layout §9) are re-reviewed in S5 with this section's changed blocks.

**Count.** ≈ 2,500 main line, ~380 folded.

### 4.6 Chapter index (`index.md`)

By the coordinator after S3, in STYLE §2 order; source: `fd3/authoring/parked/old-indexes/ch02-integers-and-rationals-index.md` (rewrite, not copy):
- **Title** `# The Integers`.
- **Story** (2 paragraphs): "subtract 5 from 3" has no answer in ℕ; pairs record it; the quotient of fd2 5.2 makes ℤ; the danger is a formula that depends on the representative; at the end ℤ is an ordered ring with division with remainder.
- **What you need.** The Chapter 1 labels of binding rule 3; *Sets and Functions*, Section 5.2 (quotients, @fd2:exm-method-well-definedness), Chapters 1–3 (pairs, functions, recursion, @fd2:thm-division-algorithm, @fd2:exm-method-least-element), Section 4.1 for 2.4 C1 only; @fd1:ax-induction, @fd1:thm-square-even-implies-even. Grep the delivered files; list only what is cited (≤ 30 labels, layout §5).
- **Time.** Recomputed by `check_structure.py --words` (layout §3: about 18 h core / 25 h full); a departure is reported to the author, not overwritten.
- **Roadmap** (5 bullets, one per section, from the plans above).
- **Named moves:** `exm-method-one-argument-at-a-time` (2.2), `exm-method-reduce-to-level-below` (2.3), `exm-method-one-positive-element` (2.4); "Order from a positive set" (2.4, prose, `prp-order-from-positives`); back-references to @fd2:exm-method-well-definedness, @fd2:exm-method-least-element.
- **Threads:** well-definedness, the level below and positive sets (2.2–2.4 → Chapters 3, 5); least elements (Chapter 1 → 2.4 → 2.5 → *Algebraic Preliminaries*).
- **Summary** (4–8 sentences) and **Terms:** commutative ring, field, ordered commutative ring, ordered field, positive set, well defined, induced function, normal form, discreteness, multiple \( n \cdot a \), divides, prime, quotient and remainder, even, odd.

---

## 5. Budgets and Time

Table at the top. Exercises: 2.1 none new; 2.2 one new (B3); 2.3 four new (A1, B2, C1) plus B1 kept; 2.4 one new (B2) and A1 (d) rewritten; 2.5 one new C, three R, old C1 parked. Core track: all A, one B and one C per section, the exit checks (2.1 C1, 2.5 C1), R1–R3. Chapter main line ≈ 3,800 + 4,100 + 2,700 + 4,400 + 2,500 ≈ 17,500 (layout target ≈ 19,300).

## 6. Edits outside the chapter, pointers, promises

- **fd5 (small primes).** Insert 25:180–193 (heading `## Small primes`, the lead 25:182 with "*Sets and Functions*, Section 1.1" kept and "the ring of Chapter 2" → "the constructed \( \nZ \) (*Number Systems*, Chapter 2)", and the remark verbatim with its citations prefixed `@fd3:`) into `fd5/src/ch01-divisibility-and-congruences/02-unique-factorization.md` immediately before `def-prime-factorization` (L39 at `b401a06`); 25:196's last sentence becomes "Section 1.2 shortens it below (after @lem-least-divisor-prime)." Retarget "the small-primes remark of *Number Systems*, Section 2.5" to "… above" (fd5 1.2 L57, L70, L142, L433) and to "… of Section 1.2" (`04-units-and-crt.md` L143, L418, L502; `ch02-fields/06-frobenius-and-fermat.md` L305, L533). fd5 1.2 L5 ("As in *Number Systems*, Section 2.5, numerals …") stays: 25:7 is kept. Ledger lines 25:294–296 move to fd5 1.2. This is an fd5 changed block: S8 build check and changed-only review, with the Chapter 2 review.
- **Parked:** `fd3/authoring/parked/from-3.1-division-part-b.md` receives `exr-division-with-remainder-c1` (§4.5 item 13); its header names both. `ledger-parked.yaml` gets the C1 item (`tools/ledger.py`).
- **Pointer renumbering inside the chapter** (old 2.3 → 2.3/2.4): 21:201, 22:38, 22:229, 22:249, 23:46, 25:5 ("a Quick check in Section 2.3" → "Section 2.4"), 25:7 ("Section 3.3" → "Section 2.2"), 23:417 (→ *Algebraic Preliminaries*, Chapter 1). Approved pointers kept: 21:152, 21:198, 22:11, 22:231, 22:235, 23:34, 23:301.
- **Chapter 3 blueprint** (next S1): place part (b) and old C1 (parked) after `prp-rational-integer-part`; the 2.5 Looking-ahead box promises it.
- **STATUS:** promise rows for 2.5's box (F5.1; F3.11 §02); F3.2 §03 rows re-keyed to §03/§04.
- **Ledgers** (coordinator, S4, `tools/ledger.py`): the split re-keys check items of 23: to `04`; the moved B1 stays in `03`.

## 7. S2a: claims to verify

1. Every computation in a new block of §4 (Quick checks, scratch tables, worked examples, exercise solutions, R items), each by a sidecar or by hand; in particular 2.2 B3 (a) both steps and (b)–(c) counterexamples; 2.3 B2 (c) (zero of ℕ×ℕ, (F4) at \( (1, 0) \)) and C1 (\( \varphi \) identities); 2.4 `exm-product-of-inequalities` (\( bd - ac = b(d - c) + (b - a)c \)) and B2 (a)–(e); 2.5 C1 and R1–R3.
2. 2.2: with the fold, (b)'s main-line proof is still complete; the rewritten 22:186–188 makes no claim about \( n \in \nZ \).
3. 2.5: the main line of `prp-divisibility-rules-integers` reads forward with (a)–(d), (f), (h) folded; the new Idea matches fd2's proof of @fd2:thm-division-algorithm.
4. No `@label` in Chapter 2 points past Chapter 2 after S3 (removed: `prp-rational-integer-part`, `thm-rationals-ordered-field`, `prp-reciprocal-order`, `fd5:prp-rationals-lowest-terms`, `fd5:lem-least-divisor-prime`), nor to `def-omega-arithmetic` (c) or a parked ZF label; new labels unique (`blueprint/check_blueprint.py`).
5. fd5: the inserted remark resolves its `@fd3:` citations; every retargeted pointer reads correctly.

## 8. Notes for S3 and S4

- **Drafters** (one workflow at a time; lean):
  - **(A) 2.3 and 2.4** (Opus): the split of `03-commutative-rings.md` into `03` and `04`; sidecars in `fd3/verify/ch02/`: `exm-integer-laws-two-routes.py`, `exr-commutative-rings-b2.py`, `exr-commutative-rings-c1.py`, `exm-product-of-inequalities.py`, `exr-ordered-rings-b3.py`.
  - **(B) 2.1 and 2.2** (Sonnet: style revision on kept text; the new blocks are written out above): `01`, `02`; sidecar `exr-well-defined-operations-b3.py`; update `exr-well-defined-operations-*.py` only if a solution changed (none). B cites nothing new in 2.3/2.4, so it is independent of A.
  - **(C) 2.5 and the fd5 move** (Opus): `05`; `fd5/src/ch01-divisibility-and-congruences/02-unique-factorization.md`, `04-units-and-crt.md`, `fd5/src/ch02-fields/06-frobenius-and-fermat.md` (pointers only); parked file; sidecars `exr-division-with-remainder-c2.py`, `-r1.py`, `-r3.py`. C cites `exm-method-one-positive-element` (2.4), so C lands after A, or both in one build check.
  - **Coordinator:** `index.md` last; STATUS, ledgers, `known-unresolved.json`, Time.
- **Checkers:** `./build.py check` (fd1–fd5, an1); `check_structure.py`; the forward-deps check.
- **Review (lean):** changed-only blind review: all new blocks (boxes, scratch work, examples, Quick checks, new exercises, R group, 2.5's rewritten prose, the fd5 insertion and pointers); kept verbatim blocks get the S8 build check only. Then S7.
- **Calls made here for the author (not blocking):** (1) The small-primes remark moves to fd5 1.2 rather than being deleted, because six fd5 passages use it. (2) Old 2.5 C1 is parked with part (b) for Chapter 3. (3) In 2.5 the proofs of `prp-divisibility-rules-integers` (a)–(d), (f), (h) sit in a second-reading fold instead of being deleted, so that every cited letter keeps a proof. (4) 2.3 stays near 2,700 words, below the layout's 4,000: old 2.3's first half was shorter than estimated, and nothing was added to fill it.
