# fd2 *Sets, Relations, and Cardinality*: the final layout (Option C)

**Status.** Binding whole-book layout for the fd2 re-cut, decided by the author on 2026-10-25. It makes Option C of `layout-proposal.md` (now superseded) final, with the proposal's defaults wherever the author did not choose otherwise (§9). No book text has moved yet: the moves in §3 happen in the per-chapter deepen passes, each from its own blueprint. The Gate system is retired (STYLE §11.10); no chapter has an examination section. **Amended 2026-10-25** by `layout-addendum-sets-and-functions.md`: the book is retitled *Sets and Functions*, Section 3.6 Cardinal Arithmetic and Chapter 5 Building Functions (F2.6) are added, and Zorn's lemma moves to Chapter 6; this file is otherwise kept as the record of the re-cut.

**Measured inputs (2026-10-25).** fd2 today: 18 sections in 3 chapters, 106,800 main-line words, 95/130 h (core/full) without Zorn. Downstream, fd1, fd3 and fd4 cite **99 distinct `@fd2:` labels** (fd3 95, fd4 50, the fd1 ledger 1), plus two truncated strings in `fd3/authoring/ledger/ch03.yaml` (`thm-divisi`, `thm-di`, both meaning `thm-division-algorithm`; ledger evidence prose, read by no tool). an1 cites no labels, only 13 prose phrases ("Chapter 2/3"). fd1, fd3 and fd4 carry about 142 prose pointers "Chapter N / Section N.M".

---

## 1. Final table of contents

Order: direct proof, sets with functions, induction, contrapositive and contradiction, sizes, relations, Zorn. Each chapter stays about one body of mathematics; each section is paired with the method it teaches first.

**Scaffold levels** (STYLE §11.4, the three-level fade): **full** = a `[Scratch work]` idea, a method box `exm-method-…`, a Givens/Goal table and two worked examples; **Idea** = a short Idea with a back-reference to the method box; **terse** = the proof alone. A **method section** is one that introduces at least one method box; each has one *Prove or disprove* B item (§5).

| § | File (`fd2/src/…`) | Title | Atlas | Method it teaches first | Method box(es) (names fixed at S1) | Scaffold / where it fades | Words (main) | Track |
|---|---|---|---|---|---|---|---|---|
| **Ch1** | `ch01-sets-and-functions/` | **Sets and Functions: Proofs from Definitions** | **F2.1** | | | | | |
| 1.1 N | `01-proofs-from-definitions.md` | Proofs from Definitions | F2.1 | direct proof from a definition; cases; WLOG; disproof by counterexample; existence by example (hook: a finite tiling or pigeon puzzle; even/odd by `@fd1:ax-induction`; divisibility; `def-divides`, `def-prime` move here) | `exm-method-direct-proof`, `exm-method-cases`, `exm-method-counterexample` | full; cases fade to Idea from 1.4 | 4,500 | core |
| 1.2 ← 1.1 | `02-sets-and-subsets.md` | Sets, Subsets and Russell's Paradox | F2.1 | element-chasing for ⊆, two inclusions for =; Russell as the first contradiction in practice | `exm-method-element-chasing`, `exm-method-double-inclusion` | full; element-chasing → Idea from 1.3, terse from 1.7 | 5,000 | core |
| 1.3 ← 1.2 | `03-set-operations.md` | Unions, Intersections, Complements and Families | F2.1 | laws via chains of iff (fd1 2.4); refute with a small witness | `exm-method-chain-of-iff` | element-chasing at Idea + back-reference | 5,000 | core |
| 1.4 ← 1.3 | `04-products-and-relations.md` | Ordered Pairs, Products and Relations | F2.1 | existence and uniqueness (the pair property) | `exm-method-uniqueness` | full for uniqueness; uniqueness → back-reference in 1.6 | 4,500 | core |
| 1.5 ← 1.4 | `05-functions.md` | Functions, Composition, Injections and Surjections | F2.1 | injectivity template; surjectivity by scratch work backwards, proof forwards; the 0–1 string game planted | `exm-method-injectivity`, `exm-method-surjectivity` | full; surjectivity scratch → Idea from 1.6 | 5,000 | core |
| 1.6 ← 1.5 | `06-inverses.md` | Left, Right and Two-Sided Inverses | F2.1 | construct and verify; an iff as two directions | `exm-method-construct-and-verify` | full for the new method; uniqueness faded | 5,000 | core |
| 1.7 ← 1.6 | `07-images-and-preimages.md` | Images and Preimages | F2.1 | name the witness; hunting a counterexample for f(A ∩ B) | none | faded: Ideas only | 5,000 | core |
| **Ch2** | `ch02-induction-and-finite-sets/` (was `ch02-relations-and-induction/`) | **Induction, Contradiction, and Finite Sets** | **F2.2** | | | | | |
| 2.1 ← 2.1 | `01-naturals-and-well-ordering.md` | The Natural Numbers and Well-Ordering | F2.2 | the least element as a proof tool | `exm-method-least-element` | full | 5,000 | core |
| 2.2 ← 2.2 | `02-induction-in-practice.md` | Induction, Strong Induction and Divisibility | F2.2 | finding P(k) inside P(k+1) (scratch work); choosing the base; a gallery of broken inductions (the smallest-counterexample subsection leaves for 2.4) | `exm-method-induction-step` | full, then Idea | 5,000 | core |
| 2.3 ← 2.3 | `03-recursion.md` | Definition by Recursion | F2.2 | recursion, then induction on it; strengthening the claim (recalls `@fd1:exm-strengthen-the-claim`) | none | Idea + back-reference | 5,000 | core |
| 2.4 N (+ part of 2.2) | `04-contrapositive-and-contradiction.md` | Contrapositive and Contradiction in Practice | F2.2 | choosing among direct, contrapositive and contradiction; infinitude of primes (new `thm-primes-infinite`); an irrational by lowest terms (not fd1's √2 or `prp-log2-9-irrational`); the smallest counterexample (moved from 2.2); witness-free existence, pointer to fd1 8.7 | `exm-method-choosing-the-form`, `exm-method-smallest-counterexample` | full | 4,500 | core |
| 2.5 ← 3.1 | `05-finite-sets.md` (slug kept) | Equinumerous Sets and Finite Sets | F2.2 | same size by a bijection; pigeonhole proved ("Back to the pigeons"); contradiction at scale (no proper copy) | `exm-method-pigeonhole` | full for pigeonhole | 5,000 + fold | core |
| **Ch3** | `ch03-countable-and-uncountable/` | **Countable and Uncountable Sets** | **F2.3** | | | | | |
| 3.1 ← 3.2 | `01-countable-sets.md` | Countable Sets | F2.3 | list it (surjection from ℕ or injection into ℕ) | `exm-method-list-it` | full | 5,000 | core |
| 3.2 ← 3.3 | `02-countable-unions-and-choice.md` | Countable Unions and the Axiom of Choice | F2.3 | name the choice | `exm-method-name-the-choice` | full | 5,000 | core |
| 3.3 ← 3.4 | `03-diagonal-arguments.md` | Diagonal Arguments | F2.3 | the diagonal ("Back to the five strings"; Cantor as Russell's payoff) | `exm-method-diagonal` | full | 5,000 | core |
| 3.4 ← 3.5 | `04-comparing-cardinalities.md` | Comparing Sizes: Schröder–Bernstein | F2.3 | injections both ways; the comparability question left open | `exm-method-injections-both-ways` | Idea | 4,200 | core |
| 3.5 ← 3.6 | `05-infinite-sets.md` | Infinite Sets | F2.3 | (R items reach back over Ch1–3 and fd1) | none | terse | 3,700 | core |
| **Ch4** | `ch04-relations-and-orders/` (new directory) | **Relations: Equivalence and Order** | **F2.5** (new) | | | | | |
| 4.1 ← 2.4 | `01-relations.md` | Properties of Relations | F2.5 | prove or disprove each property; a table of counterexamples | `exm-method-relation-properties` | full | 3,500 | core |
| 4.2 ← 2.5 | `02-equivalence-relations.md` | Equivalence Relations and Partitions | F2.5 | well-definedness; a correspondence proved both ways; "same size" revisited as an example | `exm-method-well-definedness` | full | 5,000 | core |
| 4.3 ← 2.6 | `03-orders.md` | Partial Orders, Maximal and Greatest Elements | F2.5 | greatest vs maximal; uniqueness by antisymmetry (R items) | none | Idea | 5,000 | core |
| **Ch5** | `ch05-zorns-lemma/` (new directory) | **Zorn's Lemma** | **F2.4** | | | | | |
| 5.1 N | `01-chains-and-zorn.md` | Chains and Zorn's Lemma | F2.4 | the maximality template: the poset of partial objects, unions of chains as bounds, a maximal object is complete (`thm-zorn` stated; proved in ST.4) | `exm-method-maximality` | full | 4,500 | core |
| 5.2 N | `02-using-zorn.md` | Using Zorn's Lemma | F2.4 | template reused: any two sets are comparable (paying off 3.4); extending a partial order to a linear order; **optional subsection**: the basis theorem, as a pointer to LA §1.8 (R items) | none | faded | 4,500 | core; the last subsection optional |

Section numbers are positional: a file's number prefix is its section number, so the moved files are renamed by number only and keep their slugs (every exercise label `exr-<slug>-…` keeps its name). Sections over 5,000 words reach budget by moving rule-by-rule second readings into folds (STYLE §12.0), for example "Transitivity, rule by rule" in 1.1 and "The obstacle, rule by rule" in 3.3. No cited statement goes into a fold.

## 2. Time

By STYLE §2's formula: **Ch1 40/50, Ch2 30/40, Ch3 25/30, Ch4 15/20, Ch5 10/15 h; total ≈ 120 h core, ≈ 160 h full** (now 95/130 h without Zorn). About 10 h of the rise is Zorn, always planned; the rest is the two new sections 1.1 and 2.4. Each chapter's Time line is recomputed with `tools/check_structure.py --words` after drafting.

## 3. Label migration

A label not named here stays in its section and moves with it. All 99 downstream-cited labels resolve unchanged (labels are book-wide; only their atlas chapter changes where marked **bold**).

### 3.1 Sections

| Old | New | File move |
|---|---|---|
| — | 1.1 | new `ch01…/01-proofs-from-definitions.md` |
| 1.1 … 1.6 | 1.2 … 1.7 | `ch01…/0k-<slug>.md` → `0(k+1)-<slug>.md` |
| 2.1, 2.2, 2.3 | 2.1, 2.2, 2.3 | directory renamed `ch02-relations-and-induction` → `ch02-induction-and-finite-sets` |
| — (+ 2.2's smallest-counterexample subsection) | 2.4 | new `ch02…/04-contrapositive-and-contradiction.md` |
| 3.1 | 2.5 | `ch03…/01-finite-sets.md` → `ch02…/05-finite-sets.md` |
| 3.2 … 3.6 | 3.1 … 3.5 | `ch03…/0k-<slug>.md` → `0(k−1)-<slug>.md` |
| 2.4, 2.5, 2.6 | 4.1, 4.2, 4.3 | `ch02…/04-relations.md`, `05-equivalence-relations.md`, `06-orders.md` → `ch04-relations-and-orders/01-…`, `02-…`, `03-…` |
| — | 5.1, 5.2 | new `ch05-zorns-lemma/` |

### 3.2 Every downstream-cited label (99), old → new

| Old § (file) | New § | Atlas | Labels |
|---|---|---|---|
| 1.1 `01-sets-and-subsets` | 1.2 | F2.1 | `def-empty-set`, `def-set-builder`, `def-set-equality`, `def-subset`, `prp-empty-set-unique`, `prp-subset-antisymmetric`, `prp-subset-transitive`, `thm-russell` |
| 1.2 `02-set-operations` | 1.3 | F2.1 | `def-family-union-intersection`, `def-indexed-family`, `def-power-set`, `def-set-operations`, `exm-power-set-small`, `prp-smallest-closed-set` |
| 1.3 `03-products-and-relations` | 1.4 | F2.1 | `def-cartesian-product`, `def-ordered-pair`, `def-relation` |
| 1.4 `04-functions` | 1.5 | F2.1 | `def-bijective`, `def-composition`, `def-function`, `def-injective`, `def-surjective`, `prp-composition-associative`, `prp-empty-function`, `prp-function-equality`, `thm-composition-injective-surjective` |
| 1.5 `05-inverses` | 1.6 | F2.1 | `def-inverse-function`, `def-left-right-inverse`, `prp-inverse-unique`, `prp-right-inverse-surjective`, `thm-bijection-iff-inverse`, `thm-left-inverse-iff-injective` |
| 1.6 `06-images-and-preimages` | 1.7 | F2.1 | `def-image`, `exm-sets-of-numbers-as-images` |
| 2.1 `01-naturals-and-well-ordering` | 2.1 | F2.2 | `cor-well-ordering-integers`, `exm-predecessor-no-hypothesis`, `lem-naturals-arithmetic`, `prp-integers-closed`, `thm-induction-iff-well-ordering`, `thm-well-ordering` |
| 2.2 `02-induction-in-practice` | 2.2 | F2.2 | `exr-induction-in-practice-c2`, `lem-lowest-terms`, `thm-division-algorithm`, `thm-induction`, `thm-prime-factor` |
| 2.2 `02-induction-in-practice` | **1.1** | **F2.2 → F2.1** | `def-divides`, `def-prime` |
| 2.3 `03-recursion` | 2.3 | F2.2 | `def-power`, `def-sum-product`, `prp-finite-max`, `prp-power-laws`, `thm-recursion` |
| 3.1 `01-finite-sets` | **2.5** | **F2.3 → F2.2** | `cor-finite-size-unique`, `cor-pigeonhole-finite-sets`, `cor-remove-point`, `def-finite`, `def-infinite`, `exm-hilbert-hotel`, `exr-finite-sets-c2`, `prp-disjoint-union-count`, `prp-equinumerous-properties`, `prp-subset-finite`, `thm-finite-no-proper-copy`, `thm-pigeonhole` (uncited, moving with them: `def-equinumerous`, `prp-power-set-count`) |
| 3.2 `02-countable-sets` | 3.1 | F2.3 | `cor-product-countable`, `def-countable`, `exr-countable-sets-b2`, `lem-subsets-of-naturals`, `prp-countable-image`, `prp-countable-subset`, `prp-union-two-countable`, `thm-countable-characterizations`, `thm-integers-rationals-countable`, `thm-product-countable` |
| 3.3 `03-countable-unions-and-choice` | 3.2 | F2.3 | `ax-choice`, `thm-algebraic-countable`, `thm-countable-union` |
| 3.4 `04-diagonal-arguments` | 3.3 | F2.3 | `thm-binary-sequences-uncountable` |
| 3.5 `05-comparing-cardinalities` | 3.4 | F2.3 | `def-card-le`, `prp-card-le-surjection` |
| 2.4 `04-relations` | **4.1** | **F2.2 → F2.5** | `def-relation-properties`, `prp-divides-partial-order` |
| 2.5 `05-equivalence-relations` | **4.2** | **F2.2 → F2.5** | `def-congruence`, `def-equivalence-class`, `def-equivalence-relation`, `def-quotient-set`, `exm-fibres-of-function`, `exm-ill-defined-class-map`, `exr-equivalence-relations-b1`, `prp-congruence-arithmetic`, `prp-congruence-equivalence`, `prp-integers-mod-n`, `thm-classes-partition` |
| 2.6 `06-orders` | **4.3** | **F2.2 → F2.5** | `def-order-bounds`, `def-order-supremum`, `def-partial-order`, `exm-divisibility-lcm`, `exm-subset-order-not-total`, `prp-greatest-unique` |

New labels: `thm-primes-infinite` (2.4), `thm-zorn` (5.1, taken over from LA §1.8 per `chapter-constraints.yaml`), and the method boxes of §1.

**Internal repairs.** Old 3.1 cites `@def-equivalence-relation` once and old 3.5 cites `@def-partial-order` once; both would now be forward. In 2.5 the text says "behaves like an equivalence relation" with a Looking-ahead pointer; in 3.4 reflexivity and transitivity of ≤ for cardinalities are stated directly. No other old-Chapter-3 proof cites old 2.4–2.6.

### 3.3 Prose pointers (one sweep, map like fd1 layout-final §5.1)

fd1, fd3, fd4: "Section 1.1/1.2/…/1.6" → 1.2/1.3/…/1.7; "Section 2.4/2.5/2.6" → 4.1/4.2/4.3; "Section 2.2" → 2.2, or 1.1 where it means the definition of divides or prime; "Chapter 2" → Chapter 2 where it means induction or arithmetic, Chapter 4 where it means relations or orders; finite-set mentions of "Chapter 3" or "Section 3.1" → Section 2.5; "Section 3.2–3.6" → 3.1–3.5. an1: none of the 13 phrases changes meaning. fd1's eight "Minimum before *Sets, Relations, and Cardinality*" lines become "… Sections 7.1–7.2 before its Section 2.5" (the proposal's approved one-phrase edit to the passed fd1; done in the sweep). STATUS promise rows that name a moved label are retagged by the table above when the text moves (e.g. F1.6 §02 → F2.2, F1.6 §04 → F2.5).

## 4. The fd3 division of labour

fd2 owns, for the school integers: `def-divides`, `def-prime`, `def-congruence`, `thm-division-algorithm`, `thm-prime-factor`, `lem-lowest-terms`, `prp-congruence-arithmetic`. fd3 Chapter 3 re-proves each for the constructed ℤ and names the twin. fd2's direct-proof playground in 1.1 uses only definitional unwinding: "divides" closed under sums and multiples, transitivity, parity of sums and products, cases mod 2 or 3. Its one new result that fd3 must twin is transitivity of "divides" (fd3 3.1 already proves it; its "Two integers, one theory" paragraph names the twin if it does not yet). Even/odd comes first, by `@fd1:ax-induction` in one example, extended to ℤ; no forward pointer. The infinitude of primes is new to the series (2.4). fd2 never proves gcd, Bézout, Euclid's lemma, unique factorization, CRT or the ring ℤ/n; a prose pointer to fd3 may preview them.

## 5. Shared devices and threads

**STYLE devices (adopted, STYLE §4, §2 item 6, §12.5, §12.13.4):** a `[Scratch work]` idea (up to ~20 lines with displays) at a method's first appearance and at most once more, then short Ideas with a back-reference to the method box; labelled method boxes `::: {#exm-method-<slug>}` titled `[Method: …]` (template, when to use it, the usual failure), linked from the chapter's Named moves and cited later ("by the method of @exm-method-element-chasing"); fd1's Givens/Goal table, in prose form, in the method sections; one *Prove or disprove* B item per method section, verdict not stated. Motivation before a major definition (weird examples as Quick checks, the naive attempt as the hook, an almost-correct proof checked against `@fd1:exm-not-allowed-catalogue`). No footnotes; history only as one-line prose when it carries mathematics (Russell, Cantor, Zermelo); voice "we". Quick checks one per 800–1,000 words in Ch1–2, STYLE §5's minimum after; drill banks stay fd1-only.

**Threads** (listed in each chapter index, each paid by a "Back to …" subsection):

- **Pigeonhole hook.** 1.1 states pigeonhole informally in a puzzle (nothing is proved from it there; one Looking-ahead box). 2.5 opens "Back to the pigeons" and proves `thm-pigeonhole`.
- **0–1 string game → diagonal argument.** 1.5 plants a game: given five 0–1 strings of length 5, write one not on the list; each string is a function {1,…,5} → {0,1}. 3.3 opens "Back to the five strings".
- **Russell → Cantor.** Russell (1.2) is the first contradiction in practice; Cantor's theorem (3.3) is presented as its payoff.
- **Same size.** 1.6 (bijections) → 2.5 (`def-equinumerous`) → 4.2 (an equivalence-like relation, revisited as an example).
- **Zorn 5.2 settles comparability.** 3.4 leaves open whether any two sets are comparable; 5.2 proves it by the maximality template.
- **The clock.** 4.2's congruence → fd3 3.4.

## 6. Atlas (math-atlas commit of 2026-10-25)

F2.1, F2.2, F2.3, F2.4 keep their ids. Retitled F2.1 "Sets and Functions: Proofs from Definitions", F2.2 "Induction, Contradiction, and Finite Sets", F2.3 "Countable and Uncountable Sets"; new **F2.5 "Relations: Equivalence and Order"**, ordered between F2.3 and F2.4. Edges: `F2.2: {s: [F2.1, F1.6]}`, `F2.3: {s: [F2.2, F1.6]}`, `F2.5: {s: [F2.2, F2.3], see: [F1.6]}`, `F2.4: {s: [F2.5, F2.3]}`, `F3.1: {s: [F2.2, F2.3, F2.5]}`; AN2.2, AN2.7, AL1.4 take F2.5 instead of F2.2; the five `scope: {F2.4: [F2.2]}` (AL2.3, AL2.8, FA.3, AL4.6, LA1.1) became `[F2.5]`. `thm-induction` stays with F2.2. Statements `def-equivalence`, `thm-quotient-up`, `def-poset` and the relational terms are retagged F2.5. Open: the linear-algebra import still maps `la:ch00/05` (relations and induction together) to F2.2, so the computed LA edges (e.g. LA1.4 → F2.2) keep F2.2 until that section is split or remapped.

## 7. Pipeline

The F2.1–F2.3 S5–S8 passes are void for re-cut sections. Sections that move unchanged except for numbering and pointers (old 1.2–1.6, 2.1, 2.3, 3.2–3.6, 2.4, 2.6) need only S8 and a changed-only blind review (lean workflow). The new and re-scaffolded sections (1.1, 1.2, 1.5, 2.2, 2.4, 2.5, 4.2, 5.1–5.2) run the full pipeline from a per-chapter deepen blueprint. The method boxes, Prove-or-disprove items and Givens/Goal tables added to otherwise unchanged sections count as changes for the blind review.

## 8. Checkers

`tools/check_structure.py` passes on fd1 and fd2 (0 fatal) and needs no change: it checks no label names, so `exm-method-…` is an ordinary example label, and a `[Scratch work]` idea is a `::: {.idea}` block, which its "Idea before a long proof" advisory already accepts. Possible later additions, not made: an advisory that each method section has a *Prove or disprove* B item, and an engine `.scratch` block (STYLE §4 leaves it optional).

## 9. Decisions (author, 2026-10-25)

1. **Option C (hybrid)** of `layout-proposal.md`.
2. **All four STYLE changes adopted**: (1) a longer `[Scratch work]` idea at a proof method's first appearance, then short Proof ideas with a back-reference; (2) labelled method boxes `exm-method-…`; (3) fd1's Givens/Goal tables in fd2's method sections; (4) one *Prove or disprove* B item in each method section. They apply to fd2 and later volumes; fd1 is unchanged.
3. **F2.2 keeps induction**; the new atlas id **F2.5** takes relations and orders; Zorn stays **F2.4** (Chapter 5).
4. **Zorn's 5.2**: the proposal's default, core with the last application (the basis theorem, pointing to LA §1.8) as an optional subsection.
5. **Not adopted** from the Cummings skill: footnotes for jokes or history, a first-person persona.
6. **No Gate sections.**
