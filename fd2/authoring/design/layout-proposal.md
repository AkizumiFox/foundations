# fd2 *Sets, Relations, and Cardinality*: layout proposal (proof methods)

**Superseded 2026-10-25** by `layout-final.md` (the author chose Option C, all four STYLE changes, F2.2 keeps induction, new F2.5 for relations and orders).

**Status.** A proposal for the author to choose from, written 2026-10-25. No book text is changed. It answers the request of 2026-10-25: fd2 should teach proof methods as it goes, in the arrangement of Cummings' *Proofs* (technique only; no wording, example or exercise taken), in the long-form style without footnotes and without a first-person author, with functions and bijections arriving together with sets. The Gate system is retired (STYLE §11.10); no option has an examination section.

**Measured inputs.** fd2 has 18 sections in 3 chapters: 106,800 words of main line, 0 folded; every section except 3.5 and 3.6 is over the 5,000-word budget, under an approved exception. Time is 35 + 30 + 30 h core and 45 + 45 + 40 h full. Downstream, fd3 cites 95 distinct `@fd2:` labels (1,117 occurrences), fd4 cites 50 (535), and an fd1 ledger cites 1 (`lem-lowest-terms`). an1 cites no labels, only prose ("*Sets, Relations, and Cardinality*, Chapter 2/3", 13 phrases). fd1, fd3 and fd4 carry 142 prose pointers of the form "Chapter N / Section N.M". Two citations are truncated in the source and must be checked: `@fd2:thm-di` and `@fd2:thm-divisi`, both meant for `thm-division-algorithm`. Atlas: F2.1–F2.3 are drafted, F2.4 (Zorn) is planned and has no blueprint. F2.2 owns `thm-induction` (chapter-constraints), F2.4 owns `thm-zorn`, and five chapters borrow F2.4 with `scope: {F2.4: [F2.2]}`: AL2.3, AL2.8, FA.3, AL4.6 and the LA §1.8 row.

---

## 1. Diagnosis

**Methods are taught, but implicitly and in content order.** Each chapter index has a "Named moves" list: element-chasing, unwinding the image, refuting with a small witness, building the inverse, list it, the diagonal, injections both ways, name the choice. These moves are discovered inside sections whose titles name objects, not methods. A reader learns element-chasing in 1.1, but nothing marks it as the first full appearance of a reusable template, and no later section points back to it as to a method. Three methods have no home at all:

- **Direct proof from a definition**, on a playground small enough to see the definition at work. Cummings uses parity and divisibility for this. fd2 opens on sets, where unwinding a definition and the logic of ⊆ arrive in the same paragraph.
- **Proof by cases and "without loss of generality"** as a named move. Cases occur throughout, but symmetric cases are never named as a licence to skip work.
- **Contrapositive and contradiction in practice.** fd1 supplies the rules (`@fd1:prp-contrapositive`, RAA in 2.5, `@fd1:thm-sqrt2-irrational`, prose rows in 8.1). fd2 uses them (Russell in 1.1, the smallest counterexample in 2.2, finite sets in 3.1), but never asks which of direct, contrapositive or contradiction to choose, or why.

**Scaffolding is uniform.** Each section explains its proofs at about the same density. Ideas run 1–6 per section and are never a worked search. No method gets full scaffolding at its first appearance followed by fading.

**Where functions and bijections sit.** Functions, bijections and inverses already share Chapter 1 with sets (1.4–1.6). What is separated from them is **size**: "same size" (`def-equinumerous`), finite sets and pigeonhole wait until 3.1, two chapters later, behind well-ordering, recursion, equivalence relations and orders. In Cummings, cardinality follows functions immediately. The author's "functions, bijections etc. should come along" with sets is best served by bringing finite cardinality, the first use of bijections, up to meet them.

**What Cummings' order does differently**, adapted to a reader who has read fd1:

| Cummings | fd2 now | Adapted for fd1 readers |
|---|---|---|
| 1 Intuitive proofs: a finite puzzle, pigeonhole | pigeonhole formal in 3.1 | plant pigeonhole informally at the start, prove it later ("Back to …") |
| 2 Direct proof: definitions, cases, divisibility, gcd, mod | divisibility in 2.2 (after induction); gcd and mod in fd3 3.2–3.4 | parity and divisibility as the first playground; gcd and the ring ℤ/n stay in fd3 |
| 3 Sets: proving ⊆, proving = | 1.1–1.2 | same, with the methods named |
| 4 Induction | 2.1–2.3 (logic in fd1 4.2) | the craft only; the principle is cited from fd1 |
| 5 Logic | — | fd1; never re-taught |
| 6–7 Contrapositive, contradiction | scattered | one section on choosing the form, once primes exist |
| 8 Functions, then cardinality | functions 1.4–1.6; cardinality 3.1–3.6 | functions with sets (the author's rule); finite sizes right after induction |
| 9 Relations | 2.4–2.6, before cardinality | after cardinality; Zorn right after orders |

---

## 2. The options

The three options share these decisions:

- **Integers shared with fd3.** fd2 keeps what it owns: `def-divides`, `def-prime`, `def-congruence`, `thm-division-algorithm`, `thm-prime-factor`, `lem-lowest-terms` and `prp-congruence-arithmetic`, all for the school integers. fd3 Chapter 3 already re-proves each of these for the constructed ℤ and names the twin. fd2's direct-proof playground uses only definitional unwinding: closure of "divides" under sums and multiples, transitivity, parity of sums and products, and cases mod 2 or 3. It adds at most one new result that fd3 must twin (transitivity of "divides", which fd3 3.1 already proves). The infinitude of primes is new to the series: fd1 5.1 only reads it, and fd3 never proves it. fd2 never proves gcd, Bézout, Euclid's lemma, unique factorization, CRT or the ring ℤ/n; a prose pointer to fd3 may preview them. Irrationality examples avoid fd1's √2 and `prp-log2-9-irrational`.
- **Even or odd before the division algorithm.** fd1 4.2 already gives induction on ℕ, so the playground proves "every natural number is even or odd" by `@fd1:ax-induction` in one example and extends it to ℤ. No forward pointer is needed.
- **Finite toy, then the infinite argument.** A game is planted in the section on the set of all functions: given five 0–1 strings of length 5, write one that is not on the list. It is a function {1,…,5} → {0,1}. The diagonal section opens with "Back to the five strings", and Cantor's theorem is presented as the payoff of Russell's argument.
- **Pigeonhole.** The opening section states pigeonhole informally in a puzzle hook (nothing is proved from it there; one Looking-ahead box). It is proved as `thm-pigeonhole` in the finite-sets section, which opens with "Back to the pigeons".
- **Zorn.** A chapter of 2 sections, after choice and after orders. It states `thm-zorn`, which is proved in ST.4. It teaches the maximality template (the poset of partial objects, unions of chains as bounds, a maximal object is complete) and pays off 3.5's open remark that any two sets are comparable.
- **Every label keeps its name.** The four downstream-cited exercise labels (`exr-finite-sets-c2`, `exr-countable-sets-b2`, `exr-induction-in-practice-c2`, `exr-equivalence-relations-b1`) stay attached to their exercises, so their host files keep their slugs.

### Option A: method spine (seven chapters, closest to Cummings)

Each chapter is named by a method family. Content is redistributed to serve the method.

| Ch | Atlas | Title | Sections (old → new) | First methods | Core h |
|---|---|---|---|---|---|
| 1 | **F2.5** new | Direct Proof and Cases | 1.1 a puzzle and pigeonhole, informally (N); 1.2 proving from definitions: parity, divisibility (N; `def-divides`, `def-prime` from 2.2); 1.3 cases, WLOG, existence and counterexample (N) | direct proof, cases, WLOG, example/counterexample | 18 |
| 2 | F2.1 | Sets and Functions | old 1.1–1.6, trimmed to 6 × ≤ 5,000 | element-chasing, double inclusion, injective/surjective templates, construct-and-verify | 35 |
| 3 | F2.2 | Induction and Recursion | old 2.1, 2.2, 2.3 | the craft of the induction step, smallest counterexample | 18 |
| 4 | **F2.6** new | Contradiction and the Contrapositive: Finite Sets | choosing the form, infinitude of primes (N); old 3.1 split into two | contrapositive and contradiction in practice; pigeonhole | 18 |
| 5 | F2.3 | Infinite Sets | old 3.2–3.6 | list it, diagonal, injections both ways, name the choice | 25 |
| 6 | **F2.7** new | Relations: Equivalence and Order | old 2.4–2.6 | well-definedness, extremal elements | 15 |
| 7 | F2.4 | Zorn's Lemma | 2 sections (N) | maximality argument | 10 |

**Total ≈ 140 h core, ≈ 185 h full.** Three new atlas ids. The old Chapter 2 is cut in two and the old 3.1 is split, so every "Chapter 2/3" pointer and all 13 an1 phrases change. Chapter 1 has no sets, so the author's "functions come with sets" holds only from Chapter 2. Chapters 1 and 4 are thin method chapters that borrow their content from later volumes' territory, and Chapter 1 risks crowding fd3. **Not recommended**: it is the most churn for the least gain over C.

### Option B: content chapters kept, a method paired with each section

The 3 + 1 chapters keep their content and order. One new section opens the book. Every section names its first method in its roadmap entry and carries a **method box** at that method's first appearance (§3), with scaffolding that fades.

| § | Title | First method taught | Fades at |
|---|---|---|---|
| 1.1 (N) | Proofs from Definitions: Parity and Divisibility | direct proof, cases, WLOG, counterexample | cases → Idea only from 1.4 |
| 1.2 ← 1.1 | Sets, Subsets and Russell's Paradox | element-chasing, double inclusion; contradiction in practice (Russell) | element-chasing → Idea from 1.3, terse from 1.7 |
| 1.3 ← 1.2 | Unions, Intersections, Complements and Families | laws by chains of iff; refute with a small set | — |
| 1.4 ← 1.3 | Ordered Pairs, Products and Relations | existence and uniqueness | uniqueness → back-reference in 1.6 |
| 1.5 ← 1.4 | Functions, Composition, Injections and Surjections | injectivity and surjectivity templates (scratch work: solve backwards); diagonal toy planted | surjectivity scratch → Idea from 1.6 |
| 1.6 ← 1.5 | Left, Right and Two-Sided Inverses | construct and verify | — |
| 1.7 ← 1.6 | Images and Preimages | name the witness (faded element-chasing) | — |
| 2.1–2.6 | as now | well-ordering as a tool (2.1); the induction step and a gallery of failures (2.2, plus a contrapositive/contradiction subsection with the infinitude of primes); recursion then induction (2.3); proving relation properties (2.4); well-definedness (2.5); greatest vs maximal (2.6) | |
| 3.1–3.6 | as now | pigeonhole payoff (3.1); list it (3.2); name the choice (3.3); diagonal with toy payoff (3.4); injections both ways (3.5) | |
| 4.1–4.2 (N) | Zorn's Lemma | maximality argument | |

**Total ≈ 110 h core, ≈ 150 h full** (with Zorn). No atlas id changes. Labels stay in their sections, except that `def-divides` may be restated in 1.1 by prose and keeps its home in 2.2. Only Ch1 section numbers shift by one: "Section 1.1" (11 pointers) → 1.2, "1.4" → 1.5, "1.6" → 1.7. Cost: Cummings' *arrangement* is only half adopted. Contrapositive and contradiction stay a subsection, finite sizes still wait two chapters after bijections, and relations still precede cardinality.

### Option C (recommended): hybrid, four content chapters re-sequenced in Cummings' order

Content chapters stay recognisable, but they follow Cummings' order: direct proof, sets with functions, induction, contrapositive and contradiction, sizes, relations, Zorn. Each section is paired with a method as in B.

| § | Title (content) | Method it teaches first | Scaffold | Words (main) | |
|---|---|---|---|---|---|
| **Ch1 F2.1** | **Sets and Functions: Proofs from Definitions** | | | | |
| 1.1 N | Proofs from Definitions (hook: a finite tiling or pigeon puzzle; even/odd by fd1 induction; divisibility; `def-divides`, `def-prime` move here) | direct proof; cases; WLOG; disproof by counterexample; existence by example | full | 4,500 | core |
| 1.2 ← 1.1 | Sets, Subsets and Russell's Paradox | element-chasing for ⊆, two inclusions for =; Russell as the first contradiction in practice | full | 5,000 | core |
| 1.3 ← 1.2 | Unions, Intersections, Complements and Families | laws via chains of iff (fd1 2.4); refute with a small witness | element-chasing: Idea + back-reference | 5,000 | core |
| 1.4 ← 1.3 | Ordered Pairs, Products and Relations | existence and uniqueness (the pair property) | full for uniqueness | 4,500 | core |
| 1.5 ← 1.4 | Functions, Composition, Injections and Surjections | injectivity template; surjectivity by scratch work backwards, proof forwards; diagonal toy planted | full | 5,000 | core |
| 1.6 ← 1.5 | Left, Right and Two-Sided Inverses | construct and verify; an iff as two directions | uniqueness faded | 5,000 | core |
| 1.7 ← 1.6 | Images and Preimages | name the witness; hunting a counterexample for f(A ∩ B) | faded: Ideas only | 5,000 | core |
| **Ch2 F2.2** | **Induction, Contradiction and Finite Sets** | | | | |
| 2.1 ← 2.1 | The Natural Numbers and Well-Ordering | the least element as a proof tool | full | 5,000 | core |
| 2.2 ← 2.2 | Induction, Strong Induction and Divisibility (minus the smallest counterexample) | finding P(k) inside P(k+1) (scratch work); choosing the base; a gallery of broken inductions | full, then Idea | 5,000 | core |
| 2.3 ← 2.3 | Definition by Recursion | recursion, then induction on it; strengthening the claim | Idea + back-reference | 5,000 | core |
| 2.4 N + part of 2.2 | Contrapositive and Contradiction in Practice | choosing among direct, contrapositive and contradiction; infinitude of primes (new `thm-primes-infinite`); an irrational by lowest terms; the smallest counterexample (moved from 2.2); witness-free existence, with a pointer to fd1 8.7 | full | 4,500 | core |
| 2.5 ← 3.1 | Equinumerous Sets and Finite Sets (slug kept) | same size by a bijection; pigeonhole proved ("Back to the pigeons"); contradiction at scale (no proper copy) | full for pigeonhole | 5,000 + fold | core |
| **Ch3 F2.3** | **Countable and Uncountable Sets** | | | | |
| 3.1 ← 3.2 | Countable Sets | list it (surjection from ℕ or injection into ℕ) | full | 5,000 | core |
| 3.2 ← 3.3 | Countable Unions and the Axiom of Choice | name the choice | full | 5,000 | core |
| 3.3 ← 3.4 | Diagonal Arguments | the diagonal ("Back to the five strings"; Cantor as Russell's payoff) | full | 5,000 | core |
| 3.4 ← 3.5 | Comparing Sizes: Schröder–Bernstein | injections both ways; the comparability question left open | Idea | 4,200 | core |
| 3.5 ← 3.6 | Infinite Sets | (R items reach back over Ch1–3 and fd1) | terse | 3,700 | core |
| **Ch4 F2.5 new** | **Relations: Equivalence and Order** | | | | |
| 4.1 ← 2.4 | Properties of Relations | prove or disprove each property; table of counterexamples | full | 3,500 | core |
| 4.2 ← 2.5 | Equivalence Relations and Partitions | well-definedness (full scaffold); a correspondence proved both ways; "same size" revisited as an example | full | 5,000 | core |
| 4.3 ← 2.6 | Partial Orders, Maximal and Greatest Elements | greatest vs maximal; uniqueness by antisymmetry (R items) | Idea | 5,000 | core |
| **Ch5 F2.4** | **Zorn's Lemma** | | | | |
| 5.1 N | Chains and Zorn's Lemma | the maximality template | full | 4,500 | core |
| 5.2 N | Using Zorn's Lemma (any two sets are comparable, paying off 3.4; extending an order to a linear order; the basis theorem as a pointer to LA §1.8) | template reused, faded | 4,500 | core; the last application optional (R items) |

**Total ≈ 120 h core, ≈ 160 h full**: Ch1 40/50, Ch2 30/40, Ch3 25/30, Ch4 15/20, Ch5 10/15, by STYLE §2's formula. The current 95/130 h has no Zorn. About 10 h of the rise is Zorn, which was always planned; the rest is the two new sections.

**Moves out of the main line.** Each section over 5,000 words reaches budget by moving its rule-by-rule second readings into folds (STYLE §12.0): for example "Transitivity, rule by rule" in 1.1 and "The obstacle, rule by rule" in 3.3. No cited statement goes into a fold.

**Section and label migration (C).** A label not listed here stays in its old section and moves with it.

| Old → new | Labels that move with the section (all downstream-cited except `def-equinumerous`, `prp-power-set-count`; chapter change in **bold**) |
|---|---|
| 1.1 → 1.2 … 1.6 → 1.7 | all F2.1 labels; Ch1 numbering +1 |
| 2.1 → 2.1, 2.3 → 2.3 | `thm-well-ordering`, `thm-induction-iff-well-ordering`, `cor-well-ordering-integers`, `lem-naturals-arithmetic`, `prp-integers-closed`, `exm-predecessor-no-hypothesis`; `thm-recursion`, `def-sum-product`, `def-power`, `prp-power-laws`, `prp-finite-max` |
| 2.2 → 2.2 | `thm-induction`, `thm-division-algorithm`, `thm-prime-factor`, `lem-lowest-terms`, `exr-induction-in-practice-c2` stay. **`def-divides`, `def-prime` → 1.1 (F2.2 → F2.1)**. The smallest-counterexample subsection (no cited label) → 2.4 |
| 3.1 → 2.5 | **F2.3 → F2.2**: `def-equinumerous`, `prp-equinumerous-properties`, `def-finite`, `def-infinite`, `thm-pigeonhole`, `cor-pigeonhole-finite-sets`, `cor-finite-size-unique`, `prp-disjoint-union-count`, `prp-subset-finite`, `cor-remove-point`, `prp-power-set-count`, `thm-finite-no-proper-copy`, `exm-hilbert-hotel`, `exr-finite-sets-c2` |
| 3.2–3.6 → 3.1–3.5 | `def-countable`, `thm-countable-characterizations`, `prp-countable-subset`, `prp-countable-image`, `prp-union-two-countable`, `thm-product-countable`, `cor-product-countable`, `thm-integers-rationals-countable`, `lem-subsets-of-naturals`, `exr-countable-sets-b2`; `ax-choice`, `thm-countable-union`, `thm-algebraic-countable`; `thm-binary-sequences-uncountable`; `def-card-le`, `prp-card-le-surjection` |
| 2.4–2.6 → 4.1–4.3 | **F2.2 → F2.5**: `def-relation-properties`, `prp-divides-partial-order`; `def-equivalence-relation`, `def-equivalence-class`, `def-quotient-set`, `thm-classes-partition`, `def-congruence`, `prp-congruence-equivalence`, `prp-congruence-arithmetic`, `prp-integers-mod-n`, `exm-fibres-of-function`, `exm-ill-defined-class-map`, `exr-equivalence-relations-b1`; `def-partial-order`, `def-order-bounds`, `def-order-supremum`, `prp-greatest-unique`, `exm-divisibility-lcm`, `exm-subset-order-not-total` |

**Internal repairs (C).** Old 3.1 cites `@def-equivalence-relation` once and old 3.5 cites `@def-partial-order` once. Both become forward prose and are no longer reasons: 2.5 says "behaves like an equivalence relation" with a Looking-ahead pointer, and 3.4 states reflexivity and transitivity of ≤ for cardinalities directly. No other old-Chapter-3 proof cites old 2.4–2.6, so the reordering is otherwise clean.

---

## 3. Cummings' moves on the series' devices

| Cummings move | Series device | Change needed |
|---|---|---|
| Proof Idea | `::: {.idea}` (STYLE §4, 2–6 lines) | none |
| Scratch Work (search, working backwards, the gap in the middle) | `.idea` titled `[Scratch work]`, which may run to ~20 lines with displays, at a method's first appearance and once more | **STYLE §4 exception (approve)**; an engine `.scratch` block later, optional |
| Proof outline with a gap ("Assume P … unwind … ? … rewind … so Q") | fd1's Givens/Goal table (§12.5) and partial derivation (§12.4), written in prose form | **adopt §12.4–12.5 for fd2's method sections (approve)** |
| A named technique, reusable | **method box**: a labelled example `::: {#exm-method-<slug>}` titled `[Method: proving an inclusion]`, giving the template, when to use it, and the usual failure. The chapter's Named moves list links to it, and later sections cite it ("by the method of @exm-method-element-chasing") | **STYLE §2 item 6 extended (approve)**; no engine change |
| Scaffolding that fades | full (scratch idea + method box + two worked examples) → Idea + back-reference → terse proof; the tables above mark the fades | write the existing §1 "taper" as an explicit three-level rule |
| Motivation: weird examples | numbered Quick checks before the definition | none |
| Motivation: naive approach | the explain template's hook (§3) | none |
| Motivation: almost-correct proof | §11.8 *Try it first*, plus a broken proof checked against fd1's catalogue `exm-not-allowed-catalogue` (fd1 8.6) | none |
| Hooks, long-range payoffs | chapter-opening paragraphs; "Back to …" subsections; threads listed in each chapter index | none. Threads: pigeons 1.1 → 2.5; five strings 1.5 → 3.3; Russell 1.2 → 3.3; same size 1.6 → 2.5 → 4.2; comparability 3.4 → 5.2; the clock 4.2 → fd3 3.4 |
| Finite toy before the infinite | a worked example or Quick check on a 5-element case | none |
| Two solutions; delegated symmetric cases | worked examples; WLOG taught in 1.1, then used | none |
| "Give an example or prove none exists" | a **Prove or disprove** B item per method section, verdict not stated; the fd1 derive-or-break item (§12.13.4) transposed | **extend §12.13.4 to fd2 (approve)** |
| "Which method?" | an A item part: "name the method you would try, and why" | none (A items already allow "name the method") |
| Footnotes for jokes and history; "I" | not used (author's decision). History appears only as one-line prose when it carries mathematics (Russell, Cantor, Zermelo); voice stays "we" (§7) | none |
| Brief Review | the "What you need" paragraph | none |

Drill banks (§12.8) stay fd1-only; fd2's A items carry the method-naming drills. Quick-check density follows §12.7 (one per 800–1,000 words) in Ch1–2 and STYLE §5's minimum after that.

---

## 4. Effects and recommendation

**Time.** A ≈ 140/185 h; B ≈ 110/150 h; C ≈ 120/160 h (core/full, Zorn included). The current figure is 95/130 h without Zorn. Every chapter's Time line is recomputed with `check_structure.py --words` after drafting.

**fd1 (approved).** C and A move finite sets out of Chapter 3. The "Minimum before *Sets, Relations, and Cardinality*" line in the eight fd1 indexes then reads "… Sections 7.1–7.2 before its Section 2.5" (a one-phrase edit, with the author's consent since fd1 has passed). The F1.6 §02 STATUS row is now paid by F2.2. B leaves fd1 untouched.

**fd3 / fd4.** All `@fd2:` labels resolve unchanged in every option. The 142 prose pointers are swept once by a map like fd1 layout-final §5.2's `ptrs.py`. Under C: "Section 1.1/1.4/1.6" → 1.2/1.5/1.7; "Section 2.5/2.6" → 4.2/4.3; "Section 2.2" → 2.2, or 1.1 where it means the definition of divides or prime; "Chapter 2" → Chapter 2 where it means induction or arithmetic and Chapter 4 where it means relations; finite-set mentions of "Chapter 3" → Section 2.5. fd3 3's "Two integers, one theory" paragraph gains the twin of transitivity of "divides" if it is not already named.

**an1.** Under C, none of the 13 phrases changes meaning. "Chapter 2" still means well-ordering, recursion and the arithmetic of ℕ and ℤ; "Chapter 3" still means countable sets; "Chapter 1" still means sets and images. Under A all 13 change.

**Atlas (C).**
- F2.1, F2.2 and F2.3 keep their ids. Retitle F2.1 "Sets and Functions: Proofs from Definitions" and F2.2 "Induction, Contradiction, and Finite Sets"; F2.2 still takes `thm-induction`.
- New **F2.5** "Relations: Equivalence and Order", `src: ab:7` (part).
- Edges:
  - `F2.2: {s: [F2.1], see: [F1.6]}` becomes `s: [F2.1, F1.6]` (2.5 cites `exr-models-c1/c2`).
  - `F2.3: {s: [F2.2, F1.6]}` stays.
  - `F2.5: {s: [F2.2, F2.3], see: [F1.6]}`.
  - `F2.4: {s: [F2.5, F2.3]}`.
  - `F3.1: {s: [F2.2, F2.3, F2.5]}`.
  - AN2.2, AN2.7 and AL1.4 move `s: F2.2` → F2.5 where they use classes or orders (to be checked per chapter).
  - The five `scope: {F2.4: [F2.2]}` become `[F2.5]`.
- Rows in `terms.yaml` and `statements.yaml` for the labels in **bold** above are retagged, with `moves.yaml` rows until the text moves.
- B changes only F2.1's title. A adds F2.5, F2.6 and F2.7 and reassigns more.

**STATUS.** The F2.1–F2.3 S5–S8 passes are void for re-cut sections. Sections that move unchanged except for numbering and pointers (C: old 1.2–1.6, 2.1, 2.3, 3.2–3.6, 2.4–2.6) need only S8 and a changed-only blind review, under the lean workflow. The new and re-scaffolded sections (C: 1.1, 1.2, 1.5, 2.2, 2.4, 2.5, 4.2, 5.1–5.2) run the full pipeline from blueprint.

**Recommendation: Option C.** It is the only option that adopts Cummings' *arrangement*, not just his devices. Direct proof comes before sets; induction comes before contrapositive and contradiction; sizes follow bijections in the next chapter instead of two chapters later; relations come last, with Zorn directly after orders. It keeps every chapter about one body of mathematics, so methods have real content to work on, unlike A's thin method chapters. It keeps three of four atlas ids, changes none of an1's pointers, and moves only two definitions and two blocks of labels between chapters. The cost over B (one new id, a one-phrase fd1 edit, the pointer sweep) buys the order the author asked for. If the author wants the smallest change now, B is a clean subset of C: its new 1.1, method boxes and fades carry over unchanged if C follows later.

**Decisions for the author.**
1. A, B or C.
2. The STYLE changes marked "approve" in §3: the scratch-work Idea, method boxes, §12.4–12.5 and Prove-or-disprove for fd2.
3. Under C, whether F2.5 or F2.2 keeps the relations content. This proposal keeps F2.2 on induction because `thm-induction` and most citations live there.
4. Whether Zorn's 5.2 has an optional subsection.
