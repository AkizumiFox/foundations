# fd2 *Sets and Functions*: layout addendum (cardinal arithmetic and building functions)

**Status.** Binding addendum to `layout-final.md` (Option C), decided 2026-10-25. The author asked (verbatim): 「第二本 Sets, Relations, and Cardinality 我想換成 Sets and Functions 然後我希望可以多講一點 functions 跟 sets」. Asked how, the author chose to keep every current chapter (relations, cardinality, Zorn) and only add: cardinal arithmetic (基數算術) and the structure and construction of functions (函數的結構與構造). The placement below is the coordinator's. `layout-final.md` stays the record of the re-cut and is not edited; where the two differ, this addendum wins.

**Done in the structural commit (2026-10-25).** Title, Chapter 1 title, Zorn moved to Chapter 6, pointers swept, stubs created, atlas updated (§3–§6). No mathematics has been written for 3.6 or Chapter 5: each file holds a title line only, and `tools/check_structure.py` reports such a stub as an advisory, not a fatal problem (`is_stub`, added in the same commit).

---

## 1. The plan

**(a) Title.** Book fd2 is retitled ***Sets and Functions*** (Chinese 集合與函數). The prefix `fd2`, the atlas volume id F2 and every label stay as they are. Chapter 1 is retitled **"Proofs from Definitions: Sets and Functions"**, so that it does not repeat the book's title word for word (atlas F2.1 retitled to match).

**(b) New Section 3.6 "Cardinal Arithmetic"**, after Schröder–Bernstein and Infinite Sets, file `fd2/src/ch03-countable-and-uncountable/06-cardinal-arithmetic.md` (atlas F2.3). It may cite only Chapters 1–3 (and Sections 3.1–3.5). Content:

- sums, products and powers of sizes: \( \card{A \sqcup B} \), \( \card{A \times B} \), \( \card{Y^X} \); monotonicity (if \( \card{A} \le \card{A'} \) and \( \card{B} \le \card{B'} \), then the sum, product and power compare the same way, with the empty-set caveat for powers); the laws \( X^{Y \sqcup Z} \approx X^Y \times X^Z \) and \( (X^Y)^Z \approx X^{Y \times Z} \), with commutativity and associativity of \( \sqcup \) and \( \times \) up to bijection;
- \( \card{\powerset{X}} = \card{2^X} \). Chapter 5's characteristic functions come later, so **3.6 proves \( \powerset{X} \approx \{0, 1\}^X \) inline** (the map \( A \mapsto \) "1 on \( A \), 0 off \( A \)" and its inverse \( f \mapsto f^{-1}(\{1\}) \)), and 5.1 re-reads it as the first fact about \( \mathbf{1}_A \), citing 3.6. Moving `05-infinite-sets.md` after 3.6 is the alternative; S1 may take it only if it keeps every 3.5 label and the file slug (`exr-infinite-sets-…`);
- \( \card{\nR} = \card{\powerset{\nN}} = 2^{\aleph_0} \), from the decimal and binary expansions of Section 3.3 (`def-decimal-expansion`, `thm-binary-sequences-uncountable`) and Schröder–Bernstein (injections both ways, the dual-expansion nuisance absorbed by the injection direction);
- \( \nR^2 \approx \nR \) (interleaving digits, again through \( \{0,1\}^{\nN} \times \{0,1\}^{\nN} \approx \{0,1\}^{\nN \sqcup \nN} \approx \{0,1\}^{\nN} \), so the power law does the work), \( \nN^{\nN} \approx \nR \), and \( \nN \times \nN \approx \nN \) revisited as \( \aleph_0 \cdot \aleph_0 = \aleph_0 \);
- method box candidate: `exm-method-encode` ("build an explicit bijection by encoding": choose a code, check it is injective, decode, check the round trips), per STYLE §12.14; a second candidate `exm-method-laws-by-bijection` (prove a cardinal law by writing the bijection of the underlying sets, never by computing with the symbols). Names fixed at S1.

Because 3.6 becomes the last section of Chapter 3, the chapter's R group (STYLE §11.5) moves from 3.5 to 3.6 when 3.6 is drafted, unless S1 moves 3.5 after it (then the R group stays in that file). Until then 3.5 keeps it.

**(c) New Chapter 5 "Building Functions"** (atlas **F2.6**, directory `fd2/src/ch05-building-functions/`), after Chapter 4, since it uses quotient sets and well-definedness (4.2):

| § | File | Title | Content | Method it teaches first (box names fixed at S1) |
|---|---|---|---|---|
| 5.1 | `01-restriction-extension-and-gluing.md` | Restriction, Extension and Gluing | restriction \( f|_A \); extension; gluing functions given on the sets of a cover (agreement on overlaps is the condition); piecewise definitions as gluing; characteristic functions \( \mathbf{1}_A \); set operations as arithmetic of indicators (\( \mathbf{1}_{A \cap B} = \mathbf{1}_A \mathbf{1}_B \), \( \mathbf{1}_{A \cup B} = \mathbf{1}_A + \mathbf{1}_B - \mathbf{1}_A \mathbf{1}_B \), \( \mathbf{1}_{X \setminus A} = 1 - \mathbf{1}_A \)); \( \powerset{X} \approx \{0,1\}^X \) re-read (cites 3.6) | gluing: check agreement on overlaps, then that the glued relation is a function |
| 5.2 | `02-fibres-and-factorization.md` | Fibres and the Canonical Factorization | the fibres \( f^{-1}(\{y\}) \), \( y \in f(X) \), partition the domain (the "same value" relation of `exm-fibres-of-function`); every function is inclusion ∘ bijection ∘ quotient map; the image is in bijection with the quotient by "same value"; universal property of the quotient: a function constant on classes factors uniquely through the quotient map | factor through the quotient (well-definedness reused from `exm-method-well-definedness`) |
| 5.3 | `03-binary-operations.md` | Binary Operations | operations on a set, closure; associativity, commutativity; identity and inverses, with uniqueness proofs (no group axioms as a theory); pointwise operations on \( Y^X \); composition as an operation on \( X^X \) (associative, identity \( \mathrm{id}_X \), not commutative once \( X \) has two elements) | uniqueness of an identity and of an inverse (recalls `exm-method-uniqueness`) |
| 5.4 | `04-permutations-and-iteration.md` | Permutations and Iteration | the permutations of \( X \) under composition and inverse; iterates \( f^n \) by recursion (2.3, `thm-recursion`); orbits of a permutation partition \( X \) (an equivalence relation of Chapter 4); fixed points; cycle decomposition of a permutation of a finite set; orbits of a self-map of a finite set are eventually periodic (pigeonhole, 2.5) | follow an orbit (iterate, then argue by pigeonhole or well-ordering) |

House rules for both additions: method boxes, `[Scratch work]` at a method's first appearance, Givens/Goal tables in method sections, one *Prove or disprove* B item per method section, Quick checks, at most 5,000 main-line words per section; Cummings' structural moves (the hook before the definition, the naive attempt, the almost-correct proof); no footnote jokes, no history beyond one carrying line, no first-person persona.

**fd5.** *Algebraic Preliminaries*, Chapter 3 (groups and permutations) will later cite 5.3–5.4 for permutations, composition and cycles instead of teaching them again. Only noted here; fd5 text is not edited in this pass. fd5 already defines `def-symmetric-group`, `def-cycle` and `thm-disjoint-cycle-decomposition`; S1 for Chapter 5 picks fd2 labels that do not collide (atlas `labels defined in two books`), or plans fd5's switch to `@fd2:` citations as a later fd5 revision.

**(d) Zorn's lemma moves from Chapter 5 to Chapter 6.** Atlas id F2.4 unchanged. Done in the structural commit (§3).

## 2. Table of contents (after this addendum)

| Ch | Directory | Title | Atlas | Sections | State |
|---|---|---|---|---|---|
| 1 | `ch01-sets-and-functions/` | Proofs from Definitions: Sets and Functions | F2.1 | 1.1–1.7 | approved pending S9 |
| 2 | `ch02-induction-and-finite-sets/` | Induction, Contradiction, and Finite Sets | F2.2 | 2.1–2.5 | approved pending S9 |
| 3 | `ch03-countable-and-uncountable/` | Countable and Uncountable Sets | F2.3 | 3.1–3.5; **3.6 Cardinal Arithmetic (new, stub)** | 3.1–3.5 approved pending S9 |
| 4 | `ch04-relations-and-orders/` | Relations: Equivalence and Order | F2.5 | 4.1–4.3 | approved pending S9 |
| **5** | **`ch05-building-functions/` (new)** | **Building Functions** | **F2.6 (new)** | **5.1–5.4 (stubs)** | in preparation |
| 6 | `ch06-zorns-lemma/` (was `ch05-zorns-lemma/`) | Zorn's Lemma | F2.4 | 6.1–6.2 (were 5.1–5.2) | approved pending S9 |

The preface (`fd2/src/index.md`) lists 3.6 and Chapter 5 as "in preparation".

## 3. Label, file and pointer migration

**Labels.** No existing label changes name or book. New labels come only with 3.6 and Chapter 5, named at S1. Candidates: 3.6 `def-card-sum-product-power` (or one definition per operation), `thm-cardinal-laws`, `thm-power-set-two-power`, `thm-reals-power-set-naturals`, `thm-plane-equinumerous-line`, `thm-baire-space-reals`; Chapter 5 `def-restriction`, `thm-gluing`, `def-indicator`, `prp-indicator-arithmetic`, `def-fibre`, `thm-fibres-partition`, `thm-canonical-factorization`, `thm-quotient-universal-property`, `def-binary-operation`, `prp-operation-identity-unique`, `prp-operation-inverse-unique` (not `prp-inverse-unique`, which 1.6 owns), `def-iterate`, `def-orbit`, `thm-orbits-partition`, `thm-permutation-cycles`, `prp-eventually-periodic`.

**Files moved** (`git mv`): `fd2/src/ch05-zorns-lemma/` → `fd2/src/ch06-zorns-lemma/`; `fd2/verify/ch05/` → `fd2/verify/ch06/` (docstrings "Section 5.x"/"5.2" → 6.x); `fd2/authoring/ledger/ch05.yaml` → `ch06.yaml` (`chapter: 6`, `dir: ch06-zorns-lemma`; item evidence untouched). `fd2/config/config.json` chapters: `…ch04-relations-and-orders`, `src/ch05-building-functions`, `src/ch06-zorns-lemma`.

**Pointers** (`tools/renumber.py` with `{"fd2": {"chapters": {"5": "6"}, "moves": {"src/ch05-zorns-lemma": "src/ch06-zorns-lemma"}}}`, excluding ledgers, reviews and the frozen pre-re-cut blueprints `ch01.md`–`ch03.md`; then by hand):

- fd2 own text: every "Chapter 5"/"Section 5.1/5.2" meaning Zorn → 6 (3.2, 3.4 and the Chapter 3 index, 4.3 and the Chapter 4 index, Zorn's own sections and index); the dependency-ledger comment lines of 1.6 that read "fd1 Section 5.6" were restored (they point into fd1). The Chapter 4 index's closing paragraph now also names Chapter 5 as next. Blueprints `ch02-deepen`–`ch05-deepen` follow; `layout-final.md` is left as the record.
- fd1: `ch08…/03-levels-of-abbreviation.md`, "Chapters 1–5" of fd2 → "Chapters 1–6" (twice). fd3: "*Sets and Functions*, Chapters 1 to 5" → "1 to 6" in 1.1, 1.2 and the Chapter 1 and 2 indexes. Every other "Chapter 5"/"Section 5.x" on a line naming fd2 in fd1, fd3, fd4, fd5 and an1 was read by hand: each points into its own volume, none means Zorn.
- `authoring/STATUS.md`: the F2.4 row says Chapter 6 (6.1, 6.2); a new F2.6 row; the moved path updated.
- Title: "*Sets, Relations, and Cardinality*" (and "Sets, Relations and Cardinality") → "*Sets and Functions*" in prose, prefaces, configs (`external-books`), blueprints, tools' docstrings and test fixtures of foundations and analysis-series; ledger evidence (`*/authoring/ledger/*.yaml`), review records, `layout-final.md` and `layout-proposal.md` keep the old title as history.

**Not touched (other repositories, listed only):** `linear-algebra-split` names the old title in `la1/src/ch00-borrowed/index.md`, `la1/src/ch03-linear-maps/{index.md, 02-kernel-image.md, 04-algebra-of-linear-maps.md}`, `la1/src/ch05-matrices-of-maps/index.md`, the `config/config.json` of la1, la2, la4, geo, nla and ma (`external-books`), `authoring/split-plan.md`, `tools/split_volumes.py` and `tools/pointers.py`; none of its pointers names fd2 Chapter 5 (`@fd2:thm-zorn` is a label and resolves unchanged). `linear-algebra` has no mention.

## 4. Time

STYLE §2's formula, estimated before drafting: 3.6 adds about 5 h core / 8 h full to Chapter 3 (→ about 35/53 h); Chapter 5, four sections, about 20 h core / 30 h full. Volume: **about 155 h core, 215 h full** (now 130/180 h for what is written). Each Time line is recomputed with `tools/check_structure.py --words` after drafting.

## 5. Atlas (math-atlas, same day)

- `registry/volumes.yaml`: F2 title "Sets and Functions", `title_zh: 集合與函數`.
- `registry/chapters.yaml`: F2.1 "Proofs from Definitions: Sets and Functions" (從定義出發的證明：集合與函數); new **F2.6 "Building Functions"** (函數的構造, `src: new`) between F2.5 and F2.4, so F2.4 is ordered after F2.6.
- `registry/plan-edges.yaml`: `F2.6: {s: [F2.5, F2.2]}`; `F5.3: {s: [F2.1, F3.5], see: [F1.6, F2.6]}`; F2.4 keeps `{s: [F2.5, F2.3]}`.
- `site/books.json`: fd2 `subdir: sets-and-functions`, `aliases: [fd2, sets-relations-and-cardinality]` (old addresses redirect), blurb rewritten, `planned: 6`. The landing caption names volumes by id, so it needs no change.
- `spec/00-overview.md` and `spec/06-migration.md` name the new title; `spec/08` is left as approved.
- `authoring/series.json` in foundations and analysis-series regenerated (`tools/series.py refresh`).

## 6. Pipeline

3.6 and Chapter 5 run the full pipeline (S1 blueprint from `fd2/authoring/blueprints/ch01-deepen.md` as the model: `ch03-cardinal-arithmetic.md` and `ch05-building-functions.md`, S2, S3 drafting, S4 gates, S5–S8, S9 with the author). The Zorn chapter's move is numbering only: no review is reopened; its S9 sample reads the new numbers. Lean workflow rules apply (one workflow at a time).
