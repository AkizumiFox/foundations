<!-- hand-written -->
# Deepening blueprint: F2.4 The Axiom of Choice (fd2 Chapter 6), stage S1

**Status: S1, 2026-10-26.** Next: S2 (blind referees, then S2a), then S3 (one drafter per section), S4, and the lean review the author asked for (changed-only blind review, S7, S7r).

**What this is.** The S1 blueprint for fd2 Chapter 6 under the approved six-chapter layout `fd2/authoring/design/layout-six-chapters.md` (§0, §1 Ch6 rows, §2.2, §3, §4 R10–R14, §7). The author's decisions of 2026-10-26 bind it: 「移到 6.1」 (every theorem that needs choice is in 6.1, Chapter 4 uses none) and 「Ch2 多開一節」 (inverses are Section **2.4**, gluing and indicators **2.3**). A drafter executes it with this file, the current `fd2/src/ch06-axiom-of-choice/` files (as committed in `09cf1f1`), `authoring/STYLE.md` (§1 "House manner from fd2 on", §2 item 6, §4 item 3, §6, §11, §12.0, §12.5, §12.13.4, §12.14), `DRAFTING.md` and `NOTATION.md`. The format follows `ch01-deepen.md`, leaner.

**House manner.** Cummings' structural moves only: motivation before a major statement, the naive attempt as hook, an almost-correct proof to repair, scratch work kept apart from the proof. No footnotes, no jokes, no first-person persona (the voice is "we"), history in one line only where it carries mathematics. Nothing is copied from `/home/akizumi/book`; every new example, item and answer below is the book's own.

**Line references** are to the files at `09cf1f1`: `61:` is `01-countable-unions-and-choice.md`, `62:` `02-chains-and-zorn.md`, `63:` `03-using-zorn.md`, `ix:` `index.md`.

**Word counts** are main-line prose words as `tools/check_structure.py`'s `prose_words` counts them, from the top of the file to `## Exercises`, measured at `09cf1f1`:

| File | Main line now | Budget | Expected |
|---|---|---|---|
| 6.1 `01-countable-unions-and-choice.md` | 4,411 | 5,000 | ~4,700 |
| 6.2 `02-chains-and-zorn.md` | 4,248 | 5,000 | ~4,200 |
| 6.3 `03-using-zorn.md` | 1,380 | 4,500 | ~3,950 |

(The structural commit already parked about 2,000 words of old 3.2, so 6.1 needs no condensing to reach the cap. No folds are planned; §5 names reserves.)

**Binding rules.**
1. **No label is lost or renamed.** Every label now in 61–63 stays in this chapter. Labels that move between the three files are listed in §3 and move **verbatim** (fence to fence), apart from the edits named here. Exercise labels keep their old slugs (layout, Conventions).
2. **No forward citation.** No `@label` in 6.1 cites 6.2 or 6.3, and none in 6.2 cites 6.3. Forward mentions are prose only ("Section 6.3 proves …"). Today 62:94 (`@thm-choice-from-zorn`), 62:282–289 (the four-uses table) and `exr-chains-and-zorn-a1` (about `thm-choice-from-zorn`) cite forward; §4.2 repairs them.
3. **Prerequisites** are earlier sections in the new order only (Sets, Functions, Induction and Recursion, Cardinality, Relations, then this chapter), plus fd1. §2 lists every label cited; all were grepped at `09cf1f1`.
4. **What stays out.** AC ⇒ Zorn, comparability ⇒ well-ordering (Hartogs), "the obstacle, rule by rule" and the independence proofs belong to *Axiomatic Set Theory* (ST.4, ST.5) and are prose pointers only. Ordinals and transfinite recursion are not introduced.
5. **R group in the last section only** (STYLE §6, §11.5; `check_structure.py` advises on it). `exr-infinite-sets-r4` (in 61 now) and `exr-using-zorn-r3` (in 62 now) move to 6.3; `exr-using-zorn-r1` and `-r2` move out of R into 6.3's B and C groups (labels kept), and two new R items reach back to Chapters 5 and 3.
6. **Exercise titles** are renumbered by position in each file (`[B5: …]`); labels are not. Every prose reference "Exercise B1" is checked after renumbering (the ones that exist: 62:465 and 63:195 name `exr-chains-and-zorn-b1`, which stays B1).

---

## 1. Devices as applied

- **Method boxes** (STYLE §2 item 6): two, both kept verbatim: `exm-method-name-the-choice` (6.1, 61:66) and `exm-method-maximality` (6.2, 62:124). Both are linked from the index's Named moves. 6.3 has none and reuses the template (Idea scaffold).
- **`[Scratch work]` at first appearances.** 6.1: `thm-countable-union` (61:177, kept, with its Givens/Goal table). 6.2: `exm-zorn-representatives` (62:142), the template's first run now that `thm-choice-from-zorn` has left; it gains a Givens/Goal table (§4.2 item 5). 6.3: `thm-choice-from-zorn` keeps its scratch work and table verbatim (63:79); the new `thm-well-ordering-theorem` gets a short Idea citing the box.
- **Givens/Goal tables** (§12.5): 6.1 at `thm-countable-union` (kept); 6.2 at `exm-zorn-representatives` (new); 6.3 at `thm-choice-from-zorn` (kept).
- **Prove or disprove** (§12.13.4), one per method section: 6.1 `exr-countable-unions-and-choice-b4` (kept, two parts added); 6.2 `exr-chains-and-zorn-b4` (kept). 6.3 is not a method section; it gets `exr-using-zorn-b6` anyway, since its new theorem needs an item that tests the definition.
- **Motivation before a major statement.** `ax-choice`: the countable-union proof whose first step has no licence (61:7–13, kept). `thm-zorn`: the matching hook and the naive "and so on" (62:7–19, 62:86, kept). `thm-well-ordering-theorem`: the least-element rule that 6.1 used again and again, and a weird well-order on ℤ as a Quick check (§4.3 item 4).
- **Almost-correct proofs to repair.** 62:165 (maximal finite subset, kept); the new warning in 6.3, the well-ordering proof with partial objects ordered by plain inclusion (§4.3 item 4).
- **Threads** (index): *right inverses* (2.4 → 6.1); *countable unions* (4.2 → 6.1); *the place of ℕ* (4.1 Hilbert's hotel → 6.1); *maximal elements* (5.3 → 6.2); *comparing sizes* (4.4 → 6.2 hook → 6.3); *least elements* (3.1 → 5.3 → 6.3: every set has a well-order).
- **Quick checks**: 6.1 five (kept), 6.2 six (kept), 6.3 one kept and three new.

## 2. Prerequisites (every label cited in the chapter; all exist at `09cf1f1`)

- **fd1:** `@fd1:def-rules-existential`, `@fd1:exm-not-allowed-catalogue` (N13), `@fd1:ax-induction`.
- **Chapter 1:** `def-set-builder`, `def-power-set`, `def-indexed-family`, `def-family-union-intersection`, `def-ordered-pair`, `def-relation`, `def-divides`, `thm-even-or-odd`, `exm-method-counterexample`.
- **Chapter 2:** `def-function`, `prp-function-equality`, `prp-empty-function`, `def-composition`, `def-injective`, `def-surjective`, `def-bijective`, `thm-composition-injective-surjective`, `def-left-right-inverse`, `thm-left-inverse-iff-injective`, `prp-right-inverse-surjective`, `def-preimage`, `thm-power-set-two-power` (2.3).
- **Chapter 3:** `lem-naturals-arithmetic`, `thm-well-ordering`, `exm-no-infinite-descent`, `thm-induction`, `thm-recursion`, `prp-finite-max`, `exm-method-choosing-the-form`.
- **Chapter 4:** `def-equinumerous`, `prp-equinumerous-properties`, `def-finite`, `cor-remove-point`, `prp-disjoint-union-count`, `prp-subset-finite`, `thm-finite-no-proper-copy`, `exm-hilbert-hotel`, `cor-pigeonhole-finite-sets`, `exm-method-pigeonhole`, `def-countable`, `def-countably-infinite`, `lem-subsets-of-naturals`, `thm-countable-characterizations`, `prp-countable-subset`, `prp-countable-image`, `prp-union-two-countable`, `thm-product-countable`, `cor-product-countable`, `exm-rows-first-listing`, `thm-integers-rationals-countable`, `thm-binary-sequences-uncountable`, `exm-method-diagonal`, `cor-powerset-naturals-uncountable`, `thm-reals-uncountable-decimal`, `def-card-le`, `thm-schroder-bernstein`, `exm-reals-open-interval`.
- **Chapter 5:** `def-partial-order`, `exm-subset-order-not-total`, `def-order-bounds`, `def-greatest-element`, `def-maximal-element`, `prp-greatest-unique`, `prp-greatest-maximal`, `exm-maximal-not-greatest`, `def-well-ordered-set`, `def-equivalence-relation`, `def-equivalence-class`, `thm-classes-partition`, `exm-reals-mod-integers`.

`thm-power-set-two-power` replaces the prose "the correspondence of Section 2.1" at 61:162. Nothing in Chapter 6 cites a parked label.

## 3. Labels

**Kept in place.**
- 6.1: `ax-choice`, `exm-method-name-the-choice`, `exm-choice-or-rule`, `thm-surjection-right-inverse`, `prp-card-le-surjection`, `thm-countable-union`, `thm-infinite-countable-subset`, `thm-infinite-iff-proper-subset`; exercises `exr-countable-unions-and-choice-a1`, `-b1`…`-b4`, `-c1`, `-c3`; `exr-infinite-sets-a1`, `-b1`, `-b2`, `-b3`, `-c1`, `-c2`.
- 6.2: `def-chain`, `lem-chain-union`, `thm-zorn`, `exm-method-maximality`, `exm-zorn-representatives`, `lem-one-step-order-extension`, `thm-order-extension`, `exm-divisibility-linear-extension`; exercises `exr-chains-and-zorn-b1`…`-b4`, `-c1`, `-c2`; `exr-using-zorn-b1`, `-b2`, `-b3`, `-c1`.
- 6.3: `thm-cardinal-comparability`, `cor-cardinal-trichotomy`, `thm-choice-from-zorn`; exercises `exr-using-zorn-a1`, `-c2`, `-r1` (to B), `-r2` (to C).

**Moved between files (verbatim, with the edits of §4).**
- 61 → 63: `exr-infinite-sets-r4` (R group).
- 62 → 63: `exr-chains-and-zorn-a1` (it is about `thm-choice-from-zorn`); `exr-using-zorn-r3` (R group, stem rewritten, §4.3 item 8); the four-uses table 62:282–289 (unlabelled, gains a fifth row).

**New.**
- 6.2: `exr-chains-and-zorn-a2`.
- 6.3: `thm-well-ordering-theorem`, `prp-well-ordering-gives-choice`, `exr-using-zorn-a2`, `-b4`, `-b5`, `-b6`, `-c3`, `-r4`, `-r5`.

**Removed:** none. The optional basis subsection 62:291–295 (unlabelled) is deleted; its content lives in `exr-using-zorn-r3`'s stem.

---

## 4. Per-section plans

### 4.1 Section 6.1: The Axiom of Choice (`01-countable-unions-and-choice.md`)

**Budget:** ≤ 5,000 (expected ~4,700). No folds. Scaffold full (method box, scratch work, table, worked example `exm-choice-or-rule` and the countable-union proof).

1. **Opening frame (61:3–5, ~150), replacing the S3 marker and 61:5:** "Chapter 4 compared sizes without ever picking infinitely many things with no rule: every function it built was given by a formula, a least element, or a list fixed in advance. This chapter adds the one principle that allows such picking, the axiom of choice, and gathers the theorems that need it. Section 4.2 listed \( \nN \times \nN \), \( \nZ \) and \( \nQ \), and showed that a union of two countable sets is countable (@prp-union-two-countable). The next question is a union of **countably many** countable sets. The natural proof is short, and one of its steps cannot be justified by any rule met so far. This section isolates that step, adds the axiom that licenses it, shows how to tell a proof that needs the axiom from one that only seems to, and proves the four results this book draws from it: right inverses, comparing sizes by surjections, countable unions, and the place of \( \nN \) among the infinite sets."
2. **61:38, "Its status".** Replace the sentence "Section 6.2 states its best-known equivalent, Zorn's lemma; *Axiomatic Set Theory* proves it equivalent to the axiom, together with the other equivalents such as the well-ordering theorem, and surveys the independence results." by: "Section 6.2 states Zorn's lemma, and Section 6.3 proves that Zorn's lemma gives the axiom and the well-ordering theorem; *Axiomatic Set Theory*, Chapter 4 proves the converse, and surveys the independence results." In the list of uses, "here, for countable unions and right inverses, and below, for infinite subsets that can be listed" becomes "in this section, for right inverses, countable unions and infinite sets". The rest of the paragraph and the remark 61:40–42 are kept.
3. **61:111** "the question Section 2.4 left open" is correct under the new numbering (inverses are 2.4); keep.
4. **"Comparing sizes by surjections" (61:137–163).** Delete the S3 marker. Replace the lead 61:141 (~45) by (~60): "Right inverses give a second reading of \( \le \). Section 4.4 compared sizes by injections; a surjection \( B \to A \) points the other way. The two readings agree, with one exception, the empty set, and one price: the direction from a surjection to an injection uses the axiom, through @thm-surjection-right-inverse." The proposition, its proof and 61:155 are kept verbatim. In the Quick check solution 61:162, replace "(The map is in fact a bijection, with inverse \( S \mapsto \ind_S \); this is the correspondence of Section 2.1, recalled after @cor-powerset-naturals-uncountable.)" by "(The map is in fact a bijection, with inverse \( S \mapsto \ind_S \), by @thm-power-set-two-power with \( X = \nN \).)" The check stays: 2.3 (gluing, 03:303) points to it by name.
5. **Order of subsections.** Kept: axiom, when not needed, right inverses, comparing by surjections, countable unions, then the infinite-set material.
6. **Old 3.5 material (61:223–335).** Two `##` headings stand back to back (61:223, 61:229). Delete the heading "## What choice buys for infinite sets" and the S3 marker. Its paragraph 61:227 (122) is condensed to a lead (~80) under "## Every infinite set contains a copy of the natural numbers": "Every infinite set met so far contains a copy of \( \nN \). Picking new elements one at a time looks like a proof that this always happens; it is not one, since 'one at a time' is a recursion whose step must pick from every non-empty subset at once. With @ax-choice it becomes a proof, and it gives two results: \( \nN \) is the smallest infinite size, and a set is infinite exactly when it is the same size as a proper part of itself." Then 61:231 onward is kept verbatim (theorem, Idea, proof, 61:263, the non-example 61:265, the remark 61:267, 61:271, "Consequences", the warning, the Quick check, "Infinite sets are the same size as a proper part", the final Quick check).
7. **B4 gains two parts** (after (e); solutions after (e)'s):
   - (f) "Every infinite set \( X \) admits a surjection \( X \to \nN \)."
   - (g) "If a set \( X \) admits a surjection \( X \to \nN \), then \( X \) is countable."
   - *Solution (f).* **True, using the axiom.** By @thm-infinite-countable-subset (which uses @ax-choice) there is an injection \( \nN \to X \). Since \( \nN \ne \emptyset \), @prp-card-le-surjection, direction \( (\Rightarrow) \), gives a surjection \( X \to \nN \); that direction uses no choice. (Concretely: send \( x_n \) to \( n \) and every other point to \( 0 \).)
   - *Solution (g).* **False.** \( x \mapsto \lfloor \abs{x} \rfloor \) maps \( \nR \) onto \( \nN \) (each \( n \in \nN \) is the image of \( n \)), and \( \nR \) is uncountable (@thm-reals-uncountable-decimal). A surjection onto \( \nN \) says \( X \) is at least as big as \( \nN \), not at most.
   - The stem's instruction "naming each use of @ax-choice" already covers (f).
8. **`exr-infinite-sets-c1`** (increasing functions; uses no choice). Kept, and its stem gains a last sentence: "Does your completed proof use @ax-choice?" Its solution gains: "No: the recursion has an explicit step, \( (n, x) \mapsto \max\{ x, f_{n+1}(n + 1) \} + 1 \), and the list \( n \mapsto f_n \) is given; nothing is chosen." Marking scheme: the 10 points are kept; this answer is unmarked (one sentence).
9. **Move out:** `exr-infinite-sets-r4` and the `### R. Review` heading go to 6.3 (§4.3 item 9).
10. **Exercise titles:** A1 (`-a1`), A2 (`exr-infinite-sets-a1`); B1–B4 (`exr-countable-unions-and-choice-b1`…`b4`), B5–B7 (`exr-infinite-sets-b1`…`b3`); C1 (`-c1`), C2 (`-c3`), C3 (`exr-infinite-sets-c1`), C4 (`exr-infinite-sets-c2`).
11. **Ledger (61:643–679).** Re-key the `ax-choice` status line ("Zorn, well-ordering theorem | F2.4 (Zorn stated), ST.4 …") to "F2.4 §02 (Zorn stated), F2.4 §03 (Zorn ⇒ AC, Zorn ⇒ well-ordering, proved), ST.4 (AC ⇒ Zorn), ST.5 (independence)". Add lines for B4 (f), (g) (floor of |x| onto ℕ: school function; `thm-reals-uncountable-decimal` cited) and C3's new sentence. Move the R4 line to 63's ledger.

Count: +~100 (opening) +~25 (status) +~15 (lead) −~40 (heading merge) ≈ 4,510 to `## Exercises`; ~4,700 allows for the drafter's wording.

### 4.2 Section 6.2: Zorn's Lemma and How to Use It (`02-chains-and-zorn.md`)

**Budget:** ≤ 5,000 (expected ~4,200). No folds. Scaffold full: box, scratch work with table at `exm-zorn-representatives`, two worked runs (`exm-zorn-representatives`, `thm-order-extension`), the B4.

1. **Opening (62:3–5, ~110),** replacing the marker and 62:5: "Section 4.4 proved that injections both ways give a bijection, and left open whether, for any two sets, at least one injection exists. Section 5.3 ended with a question about partially ordered sets: if every chain has an upper bound, must there be a maximal element? One principle answers both. This section states it, Zorn's lemma, which answers the second question; says why this volume does not prove it; turns it into a method of proof, the maximality template; and runs the template twice, for a set of representatives and for a total order containing a given partial order. Section 6.3 runs it on the first question, and on the axiom of choice itself."
2. **62:7–84** (matching hook, chains, `lem-chain-union`, checks) kept verbatim. 62:13's "(… the one Section 6.1 met.)" is correct; keep.
3. **62:94, status paragraph.** Replace "One half of the equivalence, that Zorn's lemma implies the axiom of choice, is the first application below (@thm-choice-from-zorn). The other half, which builds a maximal element from a choice function, is proved in *Axiomatic Set Theory*, Chapter 4, together with the other equivalents." by: "Section 6.3 proves one half of the equivalence, that Zorn's lemma gives the axiom of choice. The other half, which builds a maximal element from a choice function, needs a recursion longer than any indexed by \( \nN \); *Axiomatic Set Theory*, Chapter 4 proves it." No `@thm-choice-from-zorn` (binding rule 2). The rest is kept.
4. **62:122.** "Zorn's lemma is almost always used in one pattern. Its first use proves the half of the equivalence with the axiom of choice that this volume can prove." becomes "Zorn's lemma is almost always used in one pattern." 62:134 "The second use runs the template with a shorter plan." becomes "Here is its first run."
5. **Scratch work of `exm-zorn-representatives` (62:142–146)** keeps its paragraph and adds the table (one sentence before it: "As givens and goal:"):

   | Givens | Goal |
   |---|---|
   | \( \sim \) an equivalence relation on \( X \) | \( S \subseteq X \) meeting every class in exactly one element |
   | \( P \): the \( S \subseteq X \) with \( s \sim t \Rightarrow s = t \) (each class met at most once), ordered by \( \subseteq \) | Zorn's hypotheses: \( P \ne \emptyset \), and every non-empty chain has an upper bound in \( P \) |
   | \( \emptyset \in P \); for a chain \( \sC \), try \( \bigcup \sC \): the condition mentions two elements (@lem-chain-union (b)) | a maximal \( M \in P \) meets every class |
   | \( M \) maximal; suppose the class \( [x] \) is missed | \( M \cup \{x\} \in P \), strictly larger: a contradiction (@exm-method-choosing-the-form) |

   Scratch work stays ≤ 20 lines.
6. **62:154.** "…the template's advantage shows when the pieces interact, as in Section 6.3." becomes "…as in the next subsection." The rest of the paragraph is kept.
7. **62:168** "Section 6.3 applies the template twice more, first to the matching that opened this section." becomes "In the next run the pieces interact: one added comparison forces others."
8. **"Extending a partial order" (62:170–280)** kept verbatim. R14 is satisfied as is: `exm-divisibility-linear-extension` cites only `def-divides` and order facts.
9. **62:282–289 (the four-uses table and its lead)** move to 6.3's closing subsection (§4.3 item 7). In their place one closing sentence: "Section 6.3 runs the template three times more: on the matching that opened this section, on choice functions, and on well-orders."
10. **62:291–295 (optional basis subsection)** deleted (layout: reduced to `exr-using-zorn-r3`, which moves to 6.3).
11. **Exercises.** `exr-chains-and-zorn-a1` moves to 6.3 (§4.3 item 8). New **A1**, `exr-chains-and-zorn-a2`:
    - (a) Run @exm-zorn-representatives on \( X = \{1, 2, 3\} \) with the classes \( \{1, 2\} \) and \( \{3\} \): list \( P \), name its maximal elements, and decide whether \( P \) has a greatest element.
    - (b) Why does the chain step of @thm-order-extension need @lem-chain-union (b) only for two pairs?
    - (c) @lem-one-step-order-extension asks for \( a \), \( b \) incomparable. What goes wrong with \( R \) if \( b \preceq a \) and \( a \ne b \)?
    - (d) Give a partially ordered set in which every non-empty chain has an upper bound and which has exactly three maximal elements and no greatest element.
    - *Solution.* (a) \( P = \{ \emptyset, \{1\}, \{2\}, \{3\}, \{1, 3\}, \{2, 3\} \} \): a member meets \( \{1, 2\} \) at most once. The maximal elements are \( \{1, 3\} \) and \( \{2, 3\} \); there is no greatest element, since the two are incomparable and a greatest element would be maximal (@prp-greatest-maximal), hence one of them, containing the other. (b) (PO2) and (PO3) each mention two pairs, and (PO1) holds for the union because each member contains \( \preceq \), and the chain has a member. (c) The pair \( (a, b) \) is new, and with \( (b, a) \in {\preceq} \subseteq R \), (PO2) for \( R \) would give \( a = b \); so \( R \) is not a partial order. (d) \( \{ \{1\}, \{2\}, \{3\} \} \) under \( \subseteq \): the non-empty chains are the singletons, each its own upper bound; all three elements are maximal; none is greatest.
12. **Exercise titles:** A1 (`-a2`); B1–B4 (`exr-chains-and-zorn-b1`…`b4`), B5–B7 (`exr-using-zorn-b1`…`b3`); C1, C2 (`exr-chains-and-zorn-c1`, `-c2`), C3 (`exr-using-zorn-c1`). No R group.
13. **62:371** (B3 solution) "(Section 6.3 shows that this always happens …)" stays: prose, no `@`.
14. **Ledger (62:563–586).** The `thm-zorn` status line: "converse proved in ST.4" plus "Zorn ⇒ AC in F2.4 §03 (prose pointer)". The optional-subsection line (62:581) is re-keyed to `exr-using-zorn-r3` and moves to 63's ledger with it. Lines for `exr-chains-and-zorn-a1` move to 63. Add lines for A1 (`-a2`): (a) the six members (finite check, sidecar); (d) three maximal singletons.

Count: −201 (basis) −~95 (table and lead) +~70 (table) +~45 (opening, sentences) ≈ 4,070; ~4,200 with wording.

### 4.3 Section 6.3: Equivalent Forms of Choice (`03-using-zorn.md`)

**Budget:** ≤ 4,500 (expected ~3,950). No folds. Scaffold Idea (template reused); `thm-choice-from-zorn` keeps its full scratch work.

**Order of subsections:** opening; `## Zorn's lemma gives choice`; `## Back to comparing sizes`; `## The well-ordering theorem`; `## Well-orders give choice`; `## What is proved where`.

1. **Opening (63:3–5, ~170),** replacing the marker and 63:5: "Three statements have now appeared. The axiom of choice (@ax-choice) picks one element from each set of a family of non-empty sets. Zorn's lemma (@thm-zorn) gives a maximal element when every chain has an upper bound. The third is new: every set can be well-ordered, so that each of its non-empty subsets has a least element and 'take the least one' becomes a rule that picks. This section proves that Zorn's lemma implies the other two, and that the well-ordering theorem implies the axiom again, by that rule. It also finishes the matching that opened Section 6.2: any two sets are comparable in size. The one missing implication, from the axiom to Zorn's lemma, needs a recursion that runs past every natural number; *Axiomatic Set Theory*, Chapter 4 proves it, and with it the three statements are equivalent."
2. **`## Zorn's lemma gives choice`** moves up, before comparability (63:68–105 verbatim, as the first subsection), with these edits:
   - Add a one-sentence lead before the theorem: "The first run of the template in this section builds a choice function one index at a time."
   - 63:81 "like the matching of the first subsection" → "like the matching that opened Section 6.2".
   - 63:105 second sentence "Of the proof's four steps, only the last is about choice functions; the first three run the same way in every use of the lemma, and that is worth recording." → "Of the proof's four steps, only the last is about choice functions; the first three are the template's (@exm-method-maximality), and so is the shape of the last."
3. **`## Back to comparing sizes`** (63:7–66) follows, verbatim. 63:9 is correct. At 63:56, after "…no proof can avoid it." add: "(The converse direction passes through well-orders, by a theorem of Hartogs that *Axiomatic Set Theory* proves.)"
4. **`## The well-ordering theorem` (new, ~1,250).** Replaces the S3 markers 63:109–113.
   - **Hook (~170).** "Section 6.1 met one rule that picks, again and again: the least element of a non-empty set of natural numbers (@thm-well-ordering). A set on which that rule works for every non-empty subset is a well-ordered set (@def-well-ordered-set). If a set \( U \) carries a well-order, a family of non-empty subsets of \( U \) needs no axiom: take the least element of each. \( \nR \) with \( \le \) is not well-ordered, since \( (0, 1) \) has no least element. The question is whether some **other** order on \( \nR \), or on any set, is a well-order. For small sets the answer is easy to find by hand."
   - **Quick check (weird example).** "Find a well-order on \( \nZ \). Hint: list \( 0, -1, 1, -2, 2, \dots \)." *Solution:* let \( m \preceq_{\nZ} n \) mean \( \abs{m} < \abs{n} \), or \( \abs{m} = \abs{n} \) and \( m \le n \) (the symbol is defined in the check and used only in this section). It is a total order: compare \( \abs{m} \) and \( \abs{n} \) first, then \( m \) and \( n \). For a non-empty \( S \subseteq \nZ \), the set \( \{ \abs{s} : s \in S \} \subseteq \nN \) has a least element \( k \) (@thm-well-ordering); the least element of \( S \) is \( -k \) if \( -k \in S \), and \( k \) otherwise. (\( \sqsubseteq \) is not used: 6.2 gave it to `exm-divisibility-linear-extension`.)
   - **Transfer (~60), one sentence and its reason:** an injection \( j \colon X \to \nN \) well-orders \( X \) by "\( x \) before \( x' \) when \( j(x) \le j(x') \)", so every countable set has a well-order with no axiom (B4 asks for the proof). "For \( \nR \) no well-order can be written down; the theorem shows that one exists."
   - **The partial objects (~220), a bold-lead-in paragraph `**Extending a well-order at the top.**`.** A partial object is a pair \( (A, R) \) with \( A \subseteq X \) and \( R \) a well-order on \( A \) (so \( R \subseteq A \times A \)). For two of them, write \( (A, R) \trianglelefteq (B, S) \) when
     - (E1) \( A \subseteq B \) and \( R \subseteq S \), and
     - (E2) \( a \mathrel{S} b \) for every \( a \in A \) and every \( b \in B \setminus A \):
     
     \( S \) keeps the order of \( R \) and puts every new element **above** all of \( A \). Then: "\( \trianglelefteq \) is a partial order on the set \( P \) of partial objects" with its three-line check (reflexive: \( B \setminus A = \emptyset \); antisymmetric: (E1) both ways; transitive: for \( a \in A \), \( c \in C \setminus A \), either \( c \in B \setminus A \), so \( a \mathrel{S} c \) and \( a \mathrel{T} c \) by \( S \subseteq T \), or \( c \in C \setminus B \), so \( a \mathrel{T} c \) by (E2), as \( a \in B \)). \( P \) is a set: \( P \subseteq \powerset{X} \times \powerset{X \times X} \) (@def-set-builder, @def-power-set). One sentence on why (E2): "inclusion alone is not enough; the warning below shows why."
   - **Warning** `**Ordered by inclusion alone, the template breaks.**` (the almost-correct proof, ~140). "Order the partial objects by (E1) only. For \( n \in \nN \) let \( A_n \coloneqq \{ -n, \dots, -1, 0 \} \subseteq \nZ \) and \( R_n \) the order \( \le \) on \( A_n \); each is a well-order, since \( A_n \) is finite and \( \le \) is total. Under (E1) they form a chain, and the union of the chain is \( \le \) on \( \{ k \in \nZ : k \le 0 \} \), which has no least element. So step (2) of the template fails: the union of the chain is not a partial object. 'Every non-empty subset has a least element' speaks about infinitely many elements at once, the failure the method box names. (E2) repairs it: \( (A_n, R_n) \trianglelefteq (A_{n+1}, R_{n+1}) \) fails, since \( -(n+1) \) is added **below** \( A_n \)."
   - **Quick check.** "For which \( m \le n \) is \( (A_m, R_m) \trianglelefteq (A_n, R_n) \) in the warning's example? Which clause fails for the others?" *Solution:* only for \( m = n \): for \( m < n \), (E1) holds and (E2) fails at \( b = -n \in A_n \setminus A_m \), since \( 0 \le -n \) is false.
   - **`thm-well-ordering-theorem`** `[The Well-Ordering Theorem]`: "Every set \( X \) carries a well-order: there is a partial order \( \le \) on \( X \) such that \( (X, \le) \) is well-ordered (@def-well-ordered-set)."
   - **Idea (≤ 8 lines).** "By the method of @exm-method-maximality, with the partial objects \( (A, R) \) ordered by \( \trianglelefteq \). The chain step is where (E2) earns its place: a least element found in one member stays least in the union, because everything added later sits above it. A maximal partial object covers \( X \), since a missed point can be put on top."
   - **Proof** (four paragraphs, template steps):
     - *Partial objects.* \( (\emptyset, \emptyset) \in P \): the empty relation is a well-order on \( \emptyset \), vacuously.
     - *Chains.* Let \( \sC \subseteq P \) be a non-empty chain for \( \trianglelefteq \); let \( A^* \) be the union of the first coordinates and \( R^* \) the union of the second. Finitely many members of \( \sC \) have one member \( \trianglelefteq \)-above them all (@lem-chain-union (a)), and by (E1) its sets contain theirs; so any two or three elements of \( A^* \), and any two pairs of \( R^* \), lie in a single member. Hence \( R^* \subseteq A^* \times A^* \) is reflexive, antisymmetric, transitive and total, each property checked inside one member. *Least elements:* let \( \emptyset \ne S \subseteq A^* \), take \( s \in S \) and a member \( (A_0, R_0) \) with \( s \in A_0 \), and let \( m \) be the \( R_0 \)-least element of \( S \cap A_0 \). For \( t \in S \), take a member \( (A_1, R_1) \) with \( t \in A_1 \). If \( (A_1, R_1) \trianglelefteq (A_0, R_0) \), then \( t \in A_0 \) and \( m \mathrel{R_0} t \). If \( (A_0, R_0) \trianglelefteq (A_1, R_1) \), then either \( t \in A_0 \), as before, or \( t \in A_1 \setminus A_0 \) and \( m \mathrel{R_1} t \) by (E2). In every case \( (m, t) \in R^* \): \( m \) is the least element of \( S \). *Upper bound:* for a member \( (A, R) \), (E1) holds for \( (A^*, R^*) \); for (E2), let \( a \in A \) and \( b \in A^* \setminus A \), with \( b \in A_1 \) for a member \( (A_1, R_1) \); \( (A_1, R_1) \trianglelefteq (A, R) \) would put \( b \) in \( A \), so \( (A, R) \trianglelefteq (A_1, R_1) \) and \( a \mathrel{R_1} b \), so \( (a, b) \in R^* \).
     - *Zorn.* By @thm-zorn, \( P \) has a maximal element \( (M, R_M) \).
     - *Complete.* Suppose \( M \ne X \); take \( x \in X \setminus M \) (one \( \rulename{\exists E} \)). Put \( M' \coloneqq M \cup \{x\} \) and \( R' \coloneqq R_M \cup \{ (a, x) : a \in M' \} \). \( R' \) is a well-order on \( M' \): the new pairs all end at \( x \), so (PO1)–(PO3) and totality reduce to those of \( R_M \) plus "everything is below \( x \)"; a non-empty \( S \subseteq M' \) has as least element the \( R_M \)-least element of \( S \cap M \) if that set is non-empty, and \( x \) if \( S = \{x\} \). (E1) and (E2) hold for \( (M, R_M) \trianglelefteq (M', R') \), and \( x \notin M \) makes it strict: a contradiction. So \( M = X \), and \( R_M \) is a well-order on \( X \).
   - **Aftermath (~50).** "The proof never says which well-order it found, and there are many: for a finite set with \( n \ge 2 \) elements, every one of its listings is one. For \( \nN \) the usual order is one, and \( \le \) on \( \nR \) is not; the theorem gives \( \nR \) a well-order that no one can write down."
5. **`## Well-orders give choice` (new, ~300).**
   - **`prp-well-ordering-gives-choice`** `[Well-Orders Give Choice]`: "Let \( (A_i)_{i \in I} \) be a family of **non-empty** sets, and let \( \le \) be a well-order on \( U \coloneqq \bigcup_{i \in I} A_i \). Then \( c(i) \coloneqq \) the \( \le \)-least element of \( A_i \) defines a choice function \( c \colon I \to U \), with no appeal to @ax-choice."
   - **Proof (~70).** Each \( A_i \) is a non-empty subset of \( U \), so it has a least element (@def-well-ordered-set), and only one (@prp-greatest-unique). So the set of pairs \( (i, a) \in I \times U \) with \( a \) the least element of \( A_i \) is defined by specification (@def-set-builder); it has exactly one pair for each \( i \), so it is the graph of a function \( c \colon I \to U \) (@def-function), and \( c(i) \in A_i \).
   - **Each hypothesis (~60).** Without "non-empty" there is no least element of \( A_i = \emptyset \) (the non-example of 6.1). With a total order that is not a well-order the rule can fail: \( A_n \coloneqq (0, \frac1n) \) in \( (\nR, \le) \) has no least element.
   - **Aftermath (~70).** "With @thm-well-ordering-theorem this is a second road from Zorn's lemma to the axiom of choice: Zorn gives a well-order of \( \bigcup_{i \in I} A_i \), and the well-order gives the choice function by a rule. The axiom has not disappeared; it is hidden in the well-order, which only Zorn's lemma supplies."
   - **Quick check.** "With the well-order on \( \nZ \) of the first Quick check of this section, which element does \( c \) pick from \( \{ n \in \nZ : n^2 > 10 \} \)? From \( \{ n \in \nZ : n > 10 \} \)?" *Solution:* the set is \( \{ n : \abs{n} \ge 4 \} \); its least \( \abs{n} \) is \( 4 \), and \( -4 \) is in it, so \( c \) picks \( -4 \). From the second set: \( 11 \).
6. **No new method box.** The index's Named moves lists the two boxes only.
7. **`## What is proved where` (closing, ~350).**
   - Lead sentence, then the implication table:

     | Implication | Where |
     |---|---|
     | Zorn's lemma ⇒ axiom of choice | @thm-choice-from-zorn |
     | Zorn's lemma ⇒ every set can be well-ordered | @thm-well-ordering-theorem |
     | every set can be well-ordered ⇒ axiom of choice | @prp-well-ordering-gives-choice |
     | Zorn's lemma ⇒ any two sets are comparable | @thm-cardinal-comparability |
     | axiom of choice ⇔ every surjection has a right inverse | @thm-surjection-right-inverse and the paragraph after it (Section 6.1) |
     | axiom of choice ⇒ Zorn's lemma | *Axiomatic Set Theory*, Chapter 4 |
     | comparability ⇒ every set can be well-ordered | *Axiomatic Set Theory*, Chapter 4 (Hartogs) |

   - One paragraph: "Once the last two rows are proved, all five statements are equivalent. This book takes the axiom and Zorn's lemma as given, uses whichever form fits the problem, and flags each use."
   - Then the template table moved from 62:282–289, lead changed to "The runs of the template in this chapter, side by side:", with its four rows verbatim and a fifth row: "| well-order (@thm-well-ordering-theorem) | well-orders of subsets, ordered by \( \trianglelefteq \) | the order axioms mention at most three elements; least elements survive because of (E2) | a missed point goes on top |".
8. **Exercises.**
   - **A1** = `exr-chains-and-zorn-a1` (moved from 62, verbatim; its stem names `@thm-choice-from-zorn`, now earlier in the same file).
   - **A2** = `exr-using-zorn-a1` (kept).
   - **A3** = `exr-using-zorn-a2` (new):
     - (a) In the proof of @thm-well-ordering-theorem, which step uses (E2), and what is \( (M, R_M) \) when \( X = \emptyset \)?
     - (b) For \( X = \{1, 2\} \), list the partial objects \( (A, R) \) and the maximal ones.
     - (c) Why does the proof of @prp-well-ordering-gives-choice need no appeal to @ax-choice?
     - *Solution.* (a) The chain step, twice: for least elements of the union (an element of a later member is above \( m \)), and for the union being \( \trianglelefteq \)-above each member. It is also checked in the last step. For \( X = \emptyset \): \( P = \{ (\emptyset, \emptyset) \} \), and \( (M, R_M) = (\emptyset, \emptyset) \), the empty well-order. (b) Five: \( (\emptyset, \emptyset) \); \( (\{1\}, \{(1, 1)\}) \); \( (\{2\}, \{(2, 2)\}) \); \( (\{1, 2\}, \{(1, 1), (2, 2), (1, 2)\}) \) (1 before 2); \( (\{1, 2\}, \{(1, 1), (2, 2), (2, 1)\}) \) (2 before 1). The last two are maximal. (c) "The least element of \( A_i \)" is one description that names a value for every \( i \), so \( c \) is defined by specification (@exm-method-name-the-choice).
   - **B1** = `exr-using-zorn-r1` (moved from R; kept verbatim; title `[B1: Surjections one way or the other]`).
   - **B2** = `exr-using-zorn-b4` (new) `[B2: Well-orders without Zorn]`: "(a) Let \( j \colon X \to Y \) be injective and let \( \le \) be a well-order on \( Y \). Show that '\( x \preceq x' \) when \( j(x) \le j(x') \)' is a well-order on \( X \). (b) Deduce, without Zorn's lemma or @ax-choice, that every countable set has a well-order. (c) Give a well-order on \( \nQ \)." *Solution.* (a) (PO1), (PO3) and totality come from those of \( \le \); (PO2): \( j(x) \le j(x') \le j(x) \) gives \( j(x) = j(x') \), so \( x = x' \) by injectivity. For \( \emptyset \ne S \subseteq X \), \( j(S) \) is non-empty and has a least element \( j(s_0) \), \( s_0 \in S \); then \( s_0 \preceq s \) for every \( s \in S \). (b) A countable \( X \) has an injection \( X \to \nN \) (@thm-countable-characterizations, (i) ⇒ (ii), a rule), and \( (\nN, \le) \) is well-ordered (@thm-well-ordering); apply (a). One injection is named by one \( \rulename{\exists E} \). (c) \( \nQ \) is countable (@thm-integers-rationals-countable), so (b) applies; the answer names the injection \( \nQ \to \nN \) that @thm-countable-characterizations builds from a fixed surjection \( \nN \to \nQ \) (least preimage). No explicit formula is asked for.
   - **B3** = `exr-using-zorn-b5` (new) `[B3: Right inverses from a well-order]`: "Let \( f \colon X \to Y \) be surjective. Using @thm-well-ordering-theorem, define a right inverse of \( f \) by a rule, and say which result of Section 6.1 you have proved again and where its use of choice has gone." *Solution.* Well-order \( X \) by \( \le \) (@thm-well-ordering-theorem). For \( y \in Y \), \( f^{-1}(\{y\}) \) is non-empty (\( f \) is onto), so it has a least element \( g(y) \); \( g \) is defined by specification, and \( f(g(y)) = y \). This is @thm-surjection-right-inverse. The choice has moved into the well-order, which came from @thm-zorn; @prp-well-ordering-gives-choice with \( I = Y \), \( A_y = f^{-1}(\{y\}) \) is the same argument.
   - **B4** = `exr-using-zorn-b6` (new) `[B4: Prove or disprove]`, "Prove each true statement and refute each false one.":
     - (a) Every total order on a non-empty finite set is a well-order.
     - (b) If \( \le \) is a well-order on \( X \) and \( Y \subseteq X \), then \( \le \) restricted to \( Y \) is a well-order on \( Y \).
     - (c) \( \ge \) is a well-order on \( \nN \).
     - (d) A well-ordered set with a greatest element is finite.
     - (e) In a well-ordered set, every non-empty subset has a greatest element.
     - *Solution.* (a) **True.** A non-empty subset \( S \) is finite (@prp-subset-finite); list it as \( x_1, \dots, x_n \), \( n \ge 1 \). The reverse relation \( \ge \) is a partial order and \( S \) is a chain for it, so @lem-chain-union (a) gives an \( x_k \) with \( x_j \ge x_k \) for all \( j \): the least element. (b) **True.** Restriction keeps (PO1)–(PO3) and totality (statements about all elements), and a non-empty subset of \( Y \) is a non-empty subset of \( X \); its least element lies in it, hence in \( Y \). (c) **False.** \( \nN \) itself has no \( \ge \)-least element: that would be a greatest natural number \( g \), but \( g + 1 > g \). (d) **False.** The order \( \sqsubseteq \) of @exm-divisibility-linear-extension (positive integers in the usual order, \( 0 \) on top) is a well-order on the infinite set \( \nN \) with greatest element \( 0 \): a non-empty \( S \) has as least element its least positive member if it has one (@thm-well-ordering), and \( 0 \) if \( S = \{0\} \). (e) **False.** \( \nN \) in \( (\nN, \le) \) has no greatest element.
   - **C1** = `exr-using-zorn-c2` (kept).
   - **C2** = `exr-using-zorn-r2` (moved from R; kept verbatim; title `[C2: Maximal chains give Zorn's lemma]`). It is an equivalent form and belongs here.
   - **C3** = `exr-using-zorn-c3` (new) `[C3: Exit check: the union of a chain of well-orders]`: "Let \( X \) be a set, let \( \sC \) be a non-empty chain of partial objects of the proof of @thm-well-ordering-theorem, ordered by \( \trianglelefteq \), and let \( (A^*, R^*) \) be the union of their first and of their second coordinates. Prove that \( R^* \) is a well-order on \( A^* \) and that \( (A, R) \trianglelefteq (A^*, R^*) \) for every \( (A, R) \in \sC \)." *Solution:* the chain paragraph of the proof, written out (any two or three elements in one member by @lem-chain-union (a) and (E1); the four order properties in that member; least element by the three cases; (E1) and (E2) for the upper bound). **Marking scheme** (10): 2 for reducing finitely many elements or pairs to one member, with the citation; 2 for the order axioms and totality; 4 for least elements (1 for the candidate \( m \) in one member, 3 for the case analysis with (E2) used where the later member adds \( t \)); 2 for the upper-bound claim, including why the member containing \( b \) is above \( (A, R) \). Fatal error (0 for the least-element part): taking \( m \) least in \( S \cap A_0 \) and concluding it is least in \( S \) without the case \( t \notin A_0 \).
   - **R1** = `exr-using-zorn-r4` (new; one chapter back, Section 5.2) `[R1]`: "Let \( \sim \) be an equivalence relation on a set \( X \) and \( \le \) a well-order on \( X \). Show that the least elements of the classes form a set meeting every class exactly once." *Solution:* \( S \coloneqq \{ m_x : x \in X \} \) with \( m_x \) the least element of \( [x] \) (non-empty: \( x \in [x] \)). \( m_x \in [x] \cap S \). If \( m_x, m_y \) lie in one class, then \( [x] = [y] \) (@thm-classes-partition), so \( m_x = m_y \). This is @exm-zorn-representatives with the well-order in place of Zorn's lemma, and Exercise C2 of Section 6.2 with \( X = \nN \).
   - **R2** = `exr-infinite-sets-r4` (moved from 61, verbatim; title `[R2]`).
   - **R3** = `exr-using-zorn-r5` (new; three chapters back, Section 3.1) `[R3]`: "Let \( \le \) be a well-order on \( X \), with strict part \( < \). Show that there is no function \( s \colon \nN \to X \) with \( s(n + 1) < s(n) \) for every \( n \in \nN \)." *Solution:* the image \( s(\nN) \) is non-empty, so it has a least element \( s(k) \); but \( s(k + 1) \in s(\nN) \) and \( s(k + 1) < s(k) \), against minimality. The tool is the least-element argument of @exm-no-infinite-descent.
   - **R4** = `exr-using-zorn-r3` (moved from 62; title `[R4: The basis theorem, read as a template]`). Stem rewritten to stand alone: "This item is optional. A set of vectors of a vector space \( V \) is linearly independent when no finite non-trivial linear combination of its vectors is \( 0 \), and a basis is an independent set that spans \( V \). *Linear Algebra*, Section 1.8 proves that every independent set \( S \) lies in a basis, by the maximality template (@exm-method-maximality) with the independent sets containing \( S \) as partial objects." Parts (a)–(c) and the solution verbatim, except (b)'s "(the second warning of Section 6.2)" → "(the warning on finite subsets in Section 6.2)".
9. **Ledger (63:206–218)** keeps its lines; add: `thm-well-ordering-theorem` (proof): ⊴ is a partial order, P is a set, chain step, top extension (inline; `lem-chain-union` (a), `thm-zorn` cited); (claim) every finite listing is a well-order (B4 (a)); `prp-well-ordering-gives-choice` (proof): least element unique (`prp-greatest-unique`); (claim) (0, 1/n) has no least element (R order, school fact); the ℤ well-order Quick checks (sidecar); "What is proved where": AC ⇒ Zorn, Hartogs (ST.4, prose pointers; nothing depends on them); the R2, R4 lines moved with their items.

Count: 1,380 + 170 − 100 (opening) + ~40 (edits) + ~1,250 (well-ordering) + ~300 (choice) + ~350 (closing) + ~95 (table moved in) ≈ 3,485 + wording ≈ 3,950.

### 4.4 `index.md`

Rewritten against the delivered sections by the coordinator (as for Chapter 1).
- **Title** `# The Axiom of Choice`.
- **Story (~150).** Some constructions pick one object for each of infinitely many indices with no rule: a list for each set of a countable family, a preimage for each point, a new element at each stage. Chapter 4 avoided them. This chapter adds the axiom that permits them (6.1), states Zorn's lemma, the form in which choice is used to build objects piece by piece (6.2), and proves that Zorn's lemma gives the axiom back and gives every set a well-order (6.3). Keep the existing second paragraph's thesis sentence on Zorn (ix:5, last sentence) as the 6.2 summary.
- **What you need.** fd1 Chapters 1–8 (`@fd1:def-rules-existential`, `@fd1:exm-not-allowed-catalogue` (N13), `@fd1:ax-induction`); from this volume the labels of §2, grouped by chapter (Chapters 1–2: functions, inverses, preimages, indicators; Chapter 3: well-ordering, recursion, induction; Chapter 4: finite and countable sets, `def-card-le`, `thm-schroder-bernstein`; Chapter 5: orders, maximal elements, well-ordered sets, equivalence classes). Proof methods: `exm-method-choosing-the-form`, `exm-method-counterexample`.
- **Time.** Layout: about 16 h core / 24 h full; recomputed with `check_structure.py --words` after S3 and written as measured.
- **Roadmap**, one bullet per section: 6.1 the axiom, when it is not needed, right inverses, surjections and size, countable unions, infinite sets; 6.2 chains, Zorn's lemma and why each hypothesis is needed, the maximality template, representatives, total extensions of orders; 6.3 Zorn ⇒ choice, comparability and trichotomy, the well-ordering theorem, well-orders give choice, what is proved where.
- **Named moves.** Name the choice (`@exm-method-name-the-choice`, 6.1); the maximality template (`@exm-method-maximality`, 6.2; reused in 6.3, including the variant ordered by ⊴).
- **Threads**: the six of §1, each with where it is planted and paid.
- **Summary** (~200) and **What is open** ("AC ⇒ Zorn's lemma and Hartogs' theorem: *Axiomatic Set Theory*, Chapter 4").
- **Terms:** add *choice function* (`ax-choice`), *well-ordering theorem* (`thm-well-ordering-theorem`), *extension at the top* (the order ⊴, 6.3); keep the seven existing terms.

## 5. Budgets and Time

| § | Main now | Budget | Expected | Folds | Reserve if long |
|---|---|---|---|---|---|
| 6.1 | 4,411 | 5,000 | ~4,700 | 0 | fold the remark 61:267 and the non-example 61:265 (~180) |
| 6.2 | 4,248 | 5,000 | ~4,200 | 0 | — |
| 6.3 | 1,380 | 4,500 | ~3,950 | 0 | fold the transitivity check of ⊴ (~60) |
| total | 10,039 | 14,500 | ~12,850 | 0 | |

Exercises: 6.1 14, 6.2 12, 6.3 14 (40 in all; 9 new). Core track: all A, one B and one C per section, the exit checks (6.1 C1, 6.2 C2 and C3, 6.3 C3), the R group.

## 6. Pointers, promises, edits outside the chapter

- **5.3 remark (`ch05-relations/03-orders.md:246`, R12).** The 6.3 drafter rewrites it: "… it is equivalent to the axiom of choice, which Chapter 6 states. Chapter 6 states Zorn's lemma, uses it, and proves from it that every set has a well-order; *Axiomatic Set Theory*, Chapter 4 proves that the axiom of choice gives Zorn's lemma." No `@ax-choice` (forward). Its ledger line 03:494 is retagged "F2.4 §01 (choice stated), §02 (Zorn stated), §03 (well-ordering theorem proved), ST.4 (AC ⇒ Zorn)" (changed-only review).
- **Not this chapter's (for the Ch4 pass, recorded so the sweep finds them):** 4.3's opening cites `@thm-countable-union` (`03-diagonal-arguments.md:5`) and 4.4 cites `@ax-choice` (`04-comparing-cardinalities.md:144`, 248): both forward under the new order (R9, R10). If the Ch4 pass gives 4.4 the choice-free half of `prp-card-le-surjection` under a new label, 6.1's \( (\Rightarrow) \) gains "(this half is @<label>)" then; Chapter 6 does not wait for it.
- **STATUS.** Rows 193 and 204 (equivalents of choice; well-ordering theorem): mark "the well-ordering theorem, Zorn ⇒ WO ⇒ AC" paid by F2.4 §03 (`thm-well-ordering-theorem`, `prp-well-ordering-gives-choice`); AC ⇒ Zorn and Hartogs stay with ST.4. Row 183: the well-ordering theorem part, paid by F2.4 §03.
- **NOTATION** (coordinator, S4): the chain row's section tags (§01 → §02, §02 → §03 for (C1)–(C2), (M1)–(M2); \( \sqsubseteq \), \( \le_p \), \( \le_l \) in §02); the cut row's "F2.4 §03 (C1)–(C2)" tag stays; new row: \( \trianglelefteq \) and (E1)–(E2), "extension at the top" of partial well-orders, local to F2.4 §03 (`thm-well-ordering-theorem`, A3, C3); \( \preceq_{\nZ} \), local to the 6.3 Quick checks.
- **Atlas:** nothing; `thm-well-ordering-theorem` (F2.4) and the F2.4 chapter constraint already match (structural commit).

## 7. S2a: claims to verify

1. 6.1 B4 (f): the surjection \( x_n \mapsto n \), others \( \mapsto 0 \), is onto ℕ and the \( (\Rightarrow) \) direction of `prp-card-le-surjection` uses no choice; (g): \( \lfloor \abs{x} \rfloor \) maps ℝ onto ℕ.
2. 6.1 C3's added claim: the recursion step is explicit; no choice.
3. 6.1: the merged lead under "Every infinite set contains a copy of the natural numbers" makes no claim the section does not prove.
4. 6.2 A1 (`-a2`): (a) the six members and two maximal ones; (c) the antisymmetry failure; (d).
5. 6.2: after the edits, no `@` in 62 cites a 6.3 label (grep `thm-choice-from-zorn`, `thm-cardinal-comparability`).
6. 6.3 Quick check 1: the order on ℤ is total and every non-empty subset has the stated least element (\( -k \) or \( k \)).
7. ⊴ is a partial order on \( P \) (all three properties, transitivity's two cases); \( P \) is a set.
8. The warning's example: each \( (A_n, R_n) \) is a well-order; (E1)-chain; union without least element; (E2) fails for \( m < n \) (Quick check 2).
9. `thm-well-ordering-theorem`, chain step: `lem-chain-union` (a) applies to a ⊴-chain (it is a chain in the poset \( (P, \trianglelefteq) \)); the least-element case analysis is exhaustive; the upper-bound argument for (E2). Is "non-empty chain" used anywhere, and is the empty chain harmless?
10. The top extension: \( R' \) is a well-order on \( M' \); \( (M, R_M) \trianglelefteq (M', R') \) strictly.
11. `prp-well-ordering-gives-choice`: hypotheses needed (non-empty; well-order vs total order, the \( (0, 1/n) \) family); the specification is legitimate (`prp-greatest-unique` for least elements).
12. Quick check 3: \( c \) picks \( -4 \) and \( 11 \).
13. The implication table: each row's citation says what the row claims; "AC ⇔ right inverses" rests on 61:127 (the projection remark).
14. 6.3 A3 (b): exactly five partial objects for \( X = \{1, 2\} \), two maximal.
15. B2 (a)–(c), with (b) choice-free; B3; B4 (a)–(e), in particular (a) via the reverse order and `lem-chain-union` (a), and (d) via `exm-divisibility-linear-extension` (check that \( \sqsubseteq \) is a well-order).
16. C3 marking scheme matches the proof; R1, R3 answers; R4's rewritten stem is self-contained and makes no claim LA §1.8 does not.
17. Exercise renumbering: every prose "Exercise X" in 61–63 and in other chapters still names the right item (grep "Section 6.1, Exercise", "Section 6.2, Exercise", "Section 6.3, Exercise" across fd2–fd5 and an1).

## 8. Notes for S3 and S4

- **Drafters: three, one per section, in parallel** (no new label of one section is cited by another, except 6.3 citing 6.1/6.2 labels that already exist).
  - **Drafter 6.1** edits `fd2/src/ch06-axiom-of-choice/01-countable-unions-and-choice.md` only (items 4.1.1–4.1.11), and removes `exr-infinite-sets-r4` from it. Sidecar: `fd2/verify/ch06/exr-countable-unions-and-choice-b4.py` (extend for (f), (g) on sample points).
  - **Drafter 6.2** edits `fd2/src/ch06-axiom-of-choice/02-chains-and-zorn.md` only (items 4.2.1–4.2.14), removing `exr-chains-and-zorn-a1`, `exr-using-zorn-r3`, the table and the basis subsection. Sidecar: new `fd2/verify/ch06/exr-chains-and-zorn-a2.py` (enumerate \( P \) for (a)).
  - **Drafter 6.3** edits `fd2/src/ch06-axiom-of-choice/03-using-zorn.md` (items 4.3.1–4.3.9, inserting the three moved items and the table verbatim from the 09cf1f1 versions of 61 and 62) and `fd2/src/ch05-relations/03-orders.md` (L246 remark and ledger line 494, §6). Sidecars: new `fd2/verify/ch06/thm-well-ordering-theorem.py` (the ℤ order on a window, Quick checks 1 and 3; the warning's chain for small \( n \); ⊴ axioms and the five partial objects on \( \{1, 2\} \), A3 (b)) and `exr-using-zorn-b6.py` (B4 (d)'s order on a finite window).
  - Moved items are cut from 61/62 by their drafters and pasted into 63 by drafter 6.3 from the `09cf1f1` text, so the three commits can land in any order; the coordinator checks that each moved label appears exactly once after all three land.
  - **Coordinator:** `index.md` (§4.4) last, against the delivered sections; STATUS, NOTATION (§6); ledger re-keys with `tools/ledger.py`.
- **Checkers (S4):** `./build.py check`, `check_structure.py` (0 fatal; main line within budget by `--words`; the R-group advisory gone from 61 and 62), `check_numbers.py`, `check_notation.py`, the forward-dependency check (no 6.1 → 6.2/6.3 and no 6.2 → 6.3 citation; 5.3 cites nothing in Chapter 6), downstream builds (fd1–fd5, an1).
- **Review (lean, as the author asked):** changed-only blind review of each section; the changed items are 6.1's opening, status, lead and heading merge, B4 (f)–(g), C3's sentence; 6.2's opening, status, table, A1; all of 6.3's new text, the moved items in their new places, and the 5.3 remark. Then S7 (Sonnet revisers for minor-only sections), S7r, hand round 2. S9 sampling stays with the author.
- **Open for the author:** none blocking. Calls made here: `exr-using-zorn-r1` and `-r2` leave the R group (now B1 and C2 of 6.3) so that the R items reach back to Chapters 5, 4 and 3 as STYLE §11.5 asks; `exr-infinite-sets-c1`, the one exercise of old 3.5 that uses no choice, stays in 6.1 with a "does it use choice?" question added rather than moving to 4.3.
