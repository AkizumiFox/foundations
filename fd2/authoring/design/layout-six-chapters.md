# fd2 *Sets and Functions*: six-chapter layout (Sets, Functions, Induction and Recursion, Cardinality, Relations, The Axiom of Choice)

**Status.** **Approved 2026-10-26** by the author, with the two open questions of §9 answered (§0 below). This file overrides `layout-final.md` and `layout-addendum-sets-and-functions.md`; both stay as the record of the earlier cuts. The structural commit of §7 was made on 2026-10-26; where §0 and the tables below differ, §0 governs.

**What the author asked for (2026-10-26, verbatim).** 「我覺得 fd2 好像有太多不必要的太難的知識了」. Asked which parts: 「Building Functions, AOC 直接放到 5 然後接到 zorn's lemma 跟他的等價敘述？set 的 cardinality 我覺得需要一的 standalone 的章節去處理它，然後 injections 跟 surjections 那邊應該很多東西可以講？ 第一章 sets 第二章 functions 第三章 induction, recursion 第四章 cardinatility 第五章 relations 第六章 aoc？」. The author chose to move the material that is too hard into ST (axiomatic set theory), approved the table of contents in §1, and asked to see this layout file before anything moves.

**Measured inputs (2026-10-26).**
- fd2 has 27 sections in 6 chapters: **167,145 main-line words** plus 3,580 folded (`tools/check_structure.py --book fd2 --words`).
- The chapter Time lines add up to **160 h core / 225 h full**.
- 14 of the 27 sections are already over the 5,000-word cap.
- Downstream citations of `@fd2:` labels were grepped in foundations (fd1, fd3, fd4, fd5), analysis-series (an1), linear-algebra-split (la1) and math-atlas. The survey file `fd2-downstream.txt` misses some an1 and la1 citations (for example `thm-infinite-countable-subset`, `thm-schroder-bernstein`, `thm-primes-infinite`, `thm-surjection-right-inverse`, `thm-zorn`, `def-partition`). None of these labels leaves fd2, so the misses change nothing below.

**Conventions.**
- Section numbers are positional, as in `layout-final.md`.
- **Labels keep their names**: no label is renamed, including exercise labels whose slug no longer matches the file they sit in (no tool checks that prefix).
- "exercises `b2`" in a table means `exr-<old slug>-b2`.
- **Scaffold levels** follow STYLE §11.4: **full** = `[Scratch work]` + method box + Givens/Goal + two worked examples; **Idea** = short Idea with a back-reference; **terse** = proof only.

---

## 0. Author decisions (2026-10-26) and the structural commit

**Q1, verbatim: 「Ch2 多開一節」.** The alternative of §9 Q1 is taken. Chapter 2 has **five** sections:

| § | File | Title | Sources |
|---|---|---|---|
| 2.1 | `01-functions-and-composition.md` | Functions and Composition | old 1.5, first half (up to "Composition"), verbatim; new A/B/C exercises at S3 |
| 2.2 | `02-injections-and-surjections.md` | Injections and Surjections | old 1.5, second half, with all seven `exr-functions-*`; the new topics of §1 at S3 |
| 2.3 | `03-gluing-and-characteristic-functions.md` | Gluing and Characteristic Functions (**new**) | old 5.1 whole (restriction, extension, gluing, indicators; exercises A1, B1–B4), plus `thm-power-set-two-power` (\(\powerset{X} \approx \{0,1\}^X\)) from old 3.6 |
| 2.4 | `04-inverses.md` | Left, Right and Two-Sided Inverses | old 1.6, verbatim |
| 2.5 | `05-images-and-preimages.md` | Images and Preimages | old 1.7, verbatim |

So restriction and extension stay with gluing in 2.3 instead of going to 2.1, and the 2.2 budget problem of §9 Q1 disappears. In §3 and §5 read: old 1.6 → **2.4**, old 1.7 → **2.5**, old 5.1 → **2.3** (all of it except C1 → 4.1, C2 → 5.2, C3 → 4.5), `thm-power-set-two-power` → **2.3**. R6 and R7 read "Section 2.4" for inverses. R2 still applies to `prp-restriction-properties`, now in 2.3 before 2.4 and 2.5.

**Q2, verbatim: 「移到 6.1」.** The default of §9 Q2 is taken: `prp-card-le-surjection` (old 3.4), `thm-infinite-countable-subset`, `thm-infinite-iff-proper-subset`, the rest of old 3.5 and `exr-infinite-sets-r4` move to 6.1; Chapter 4 uses no choice and nothing depends forward.

**What the structural commit did beyond the tables (2026-10-26).** Every block moved verbatim with its label; new text is marked `<!-- S3: rewrite per blueprint (...) -->` in place. Changes forced by `./build.py check`, each marked in the text:
- `prp-restriction-properties` (2.3): part (e) cut (R2), because its proof cites `def-image` of 2.5; the removed text is kept verbatim in an S3 comment, and exercises A1 and B1, which cite (e), are rewritten at S3.
- `thm-power-set-two-power` (2.3): the last sentence of the proof no longer cites `thm-bijection-iff-inverse` (2.4, later); the two round trips give injective and surjective directly (`def-bijective`). Changed-only review owed.
- `exr-cardinal-arithmetic-c3` (Rearrangements of ℕ) is parked to ST with `thm-baire-space-reals`, on which its solution rests.
- 4.3's opening frame and B4 solution, and the Chapter 4 index, lost their citations of parked labels (the algebraic numbers, `exm-choice-free-unions`, the Baire-space results).
- The sidecar `verify/ch02/exm-fraction-map.py` gave its five-string values to `exm-function-set-small.py`, since that Quick check now sits in 2.1.
- Chapter indexes: Chapter 2 is a title-only stub; the other five keep their old text under an S3 marker, retitled.
- Parked files: `fd2/authoring/parked/st/from-3.2-…`, `from-3.3-…`, `from-3.6-…`, `from-5.2-…` (with their dependency-ledger lines and four sidecars in `parked/st/verify/`), `fd5/authoring/parked/from-fd2/03-binary-operations.md`, `04-permutations-and-iteration.md` (with 17 sidecars and `_perm.py`), and the old Chapter 5 index in `fd2/authoring/parked/old-indexes/`. Ledger items of parked labels are in `fd2/authoring/parked/ledger-parked.yaml`.

---

## 1. Table of contents

**Words.** "Now" is the current main-line count of the material that moves in. "Target" follows the house cap of 5,000.
- Sections that only **move** (pipeline M, §7) keep their approved text. They are not cut to the cap in this pass; that overrun predates this proposal.
- Sections rebuilt through S1–S4 (pipeline F) are drafted to the cap, with second readings in folds (STYLE §12.0) and no cited statement in a fold.

### Chapter 1. Sets (F2.1), directory `ch01-sets/` (was `ch01-sets-and-functions/`)

Time: about **20 h core / 28 h full** (was 40/55 for the seven-section chapter). Measured after S7 (2026-10-26): **25 h core / 35 h full** (the chapter index's Time line; §10).

| § | File | Title | Sources | Method boxes, scaffold | Now → target | Pipeline |
|---|---|---|---|---|---|---|
| 1.1 | `01-proofs-from-definitions.md` | Proofs from Definitions | old 1.1, verbatim | `exm-method-direct-proof`, `exm-method-cases`, `exm-method-counterexample`; full | 4,558 → as is | M |
| 1.2 | `02-sets-and-subsets.md` | Sets, Subsets and Russell's Paradox | old 1.2, verbatim; the second reading at L298 repointed (§4, R7) | `exm-method-element-chasing`, `exm-method-double-inclusion`; full | 6,759 → as is | M |
| 1.3 | `03-set-operations.md` | Unions, Intersections, Complements and Families | old 1.3, verbatim | `exm-method-chain-of-iff`; Idea for element-chasing | 7,733 → as is | M |
| 1.4 | `04-products-and-relations.md` | Ordered Pairs and Products | old 1.4, verbatim. `def-relation` stays here as the closing subsection ("relations as sets of pairs"). Only the title changes. | `exm-method-uniqueness`; full | 6,386 → as is | M |

The chapter index is rewritten: it now names four sections, and its "Next" points to Chapter 2 Functions.

### Chapter 2. Functions (F2.6), new directory `ch02-functions/`

Time: about **22 h core / 30 h full**. Measured after S7 (2026-10-26): **30 h core / 45 h full** (the chapter index's Time line; §10).

| § | File | Title | Sources | Method boxes, scaffold | Now → target | Pipeline |
|---|---|---|---|---|---|---|
| 2.1 | `01-functions-and-composition.md` (new slug) | Functions and Composition | **verbatim** from old 1.5: "What is a function?", "When are two functions equal?", "Families, sequences, and the set of all functions", "Composition" (`def-function` … `prp-composition-associative`). **Condensed** from old 5.1: restriction, extension and inclusion maps (`def-restriction-extension`; `prp-restriction-properties` cut to its restriction-and-composition parts, with the image and bijection parts moved to 2.4 and 2.3 exercises, §4 R2). **New:** the identity map as the unit of composition (stated in prose, no new label); an A/B/C exercise set (every old 1.5 exercise is about injectivity or surjectivity, so all of them move to 2.2). | none new; the section is built on old 1.5's worked examples; Idea | ≈ 3,900 moved → **5,000** | F |
| 2.2 | `02-injections-and-surjections.md` (new slug) | Injections and Surjections | **Verbatim** from old 1.5: "Injective, surjective, bijective" and its worked examples, plus `thm-composition-injective-surjective`. `exm-square-three-ways` becomes an exercise to make room. All seven `exr-functions-*` move here. **Moved from old 5.1, condensed:** gluing (`thm-gluing`, `exm-method-gluing`, `exm-piecewise-as-gluing`, with a new hook, §4 R4) and characteristic functions (`def-indicator`, `prp-indicator-arithmetic`, `exm-symmetric-difference-associative`). **Moved from old 3.6:** `thm-power-set-two-power` (\(\powerset{X} \approx \{0,1\}^X\) by \(A \mapsto \mathbf 1_A\)), proved here as the first fact about indicators, so 4.3 and 4.5 cite it backwards. **New, see the list below.** | `exm-method-injectivity`, `exm-method-surjectivity` (full, unchanged); `exm-method-gluing` (Idea); new box `exm-method-cancel` (name fixed at S1) | ≈ 3,900 + 2,500 moved → **5,000** (tight, §9 Q1) | F |
| 2.3 | `03-inverses.md` | Left, Right and Two-Sided Inverses | old 1.6, verbatim; L251 and L402 repointed from Chapter 3 to Chapter 6 (§4, R6) | `exm-method-construct-and-verify`; full | 7,195 → as is | M |
| 2.4 | `04-images-and-preimages.md` | Images and Preimages | old 1.7, verbatim; gains one exercise ("restriction and image", from `prp-restriction-properties`) | none; Ideas only | 8,126 → as is | M |

**New topics in 2.2.** All of them use only Chapter 1 and 2.1, school arithmetic and the school real functions that fd2 already uses (\(x^2\), \(x^3\), \(|x|\), \(\lfloor x \rfloor\)).
1. **Cancellation.** \(f\) is injective iff \(f \circ g = f \circ h\) implies \(g = h\) for all \(g, h \colon W \to X\). \(f\) is surjective iff \(g \circ f = h \circ f\) implies \(g = h\) for all \(g, h \colon Y \to Z\), where \(Z\) has at least two elements. This is injectivity and surjectivity read through left and right composition. It is the new method box ("to prove \(g = h\), cancel an injection on the left or a surjection on the right"). Proposed label `thm-cancellation`.
2. **Partial converses for composites.** If \(g \circ f\) is injective then \(f\) is injective; if \(g \circ f\) is surjective then \(g\) is surjective; counterexamples show that \(g\) and \(f\) need not be. These are exercises `exr-functions-b2`, `c1` and `c2` today; they become one proposition, `prp-composite-partial-converse`, and those exercises are rewritten to use it.
3. **Structure maps of sets.** Inclusions \(A \hookrightarrow X\) are injective. Projections \(X \times Y \to X\) are surjective iff \(Y \ne \emptyset\) or \(X = \emptyset\). The diagonal \(X \to X \times X\) is injective. \(A \mapsto X \setminus A\) is a bijection \(\powerset{X} \to \powerset{X}\) and is its own inverse (the inverse is checked by hand; 2.3 names it).
4. **Examples from algebra.**
   - \(n \mapsto an + b\) on \(\nZ\) versus on \(\nQ\).
   - \((m, n) \mapsto m + n\) and \((m, n) \mapsto mn\) on \(\nN \times \nN\): surjective or not, never injective.
   - \(n \mapsto n^2\) on \(\nN\), \(\nZ\), \(\nZ_{\ge 0}\): the domain decides.
   - \((q, r) \mapsto qn + r\) on \(\nZ \times \{0, \dots, n-1\} \to \nZ\) is a bijection. This is `thm-division-algorithm` read as a statement about a map; it cites Chapter 3 only in a Looking-ahead line, or S1 uses \(n = 2\) with `thm-even-or-odd` from 1.1.
5. **Examples from calculus.** A strictly increasing function on a subset of \(\nR\) is injective. \(x \mapsto x^3\) is a bijection \(\nR \to \nR\) (injective by factoring \(x^3 - y^3\); surjectivity is quoted from school as a fact about cube roots and flagged). \(\lfloor \cdot \rfloor \colon \nR \to \nZ\) is surjective and not injective. Polynomial differentiation, as a map from polynomials of degree at most \(n\) to those of degree at most \(n-1\), is surjective and not injective, shown on coefficient tuples (no limits).
6. **Gluing and injectivity.** A glued function is injective iff each piece is injective and the images of the pieces are disjoint. This is exercise `exr-restriction-extension-and-gluing-b2` today; S1 decides whether it becomes a proposition.
7. **Counting maps between finite sets is left for 4.1**: one Looking-ahead line here. 4.1 already has `exr-finite-sets-c2` (counting products and functions) and gains one example counting injections \(\{1..k\} \to \{1..n\}\), \(n!/(n-k)!\).

### Chapter 3. Induction and Recursion (F2.2), directory `ch03-induction-and-recursion/` (was `ch02-induction-and-finite-sets/`)

Time: about **22 h core / 30 h full**. Measured after S7 (2026-10-26): **20 h core / 35 h full** (the chapter index's Time line; §10).

| § | File | Title | Sources | Method boxes, scaffold | Now → target | Pipeline |
|---|---|---|---|---|---|---|
| 3.1 | `01-naturals-and-well-ordering.md` | The Natural Numbers and Well-Ordering | old 2.1, verbatim | `exm-method-least-element`; full | 7,211 → as is | M |
| 3.2 | `02-induction-in-practice.md` | Induction, Strong Induction and Divisibility | old 2.2, verbatim | `exm-method-induction-step`; full, then Idea | 6,732 → as is | M |
| 3.3 | `03-recursion.md` | Definition by Recursion | old 2.3, verbatim; iterates are **not** brought in (they go to fd5 with permutations) | none; Idea | 6,318 → as is | M |
| 3.4 | `04-contrapositive-and-contradiction.md` | Contrapositive and Contradiction in Practice | old 2.4, verbatim | `exm-method-choosing-the-form`, `exm-method-smallest-counterexample`; full | 4,447 → as is | M |

The chapter index is rewritten: finite sets leave the chapter, and the title drops "Finite Sets".

### Chapter 4. Cardinality (F2.3), directory `ch04-cardinality/` (was `ch03-countable-and-uncountable/`)

Time: about **30 h core / 45 h full**. Measured after S7 (2026-10-26): **30 h core / 45 h full** (the chapter index's Time line; §10).

| § | File | Title | Sources | Method boxes, scaffold | Now → target | Pipeline |
|---|---|---|---|---|---|---|
| 4.1 | `01-finite-sets.md` | Equinumerous Sets and Finite Sets; the Pigeonhole Principle | old 2.5, verbatim; **new** example counting injections (≈ 300 words); receives exercise `exr-restriction-extension-and-gluing-c1` (counting extensions) | `exm-method-pigeonhole`; full | 8,561 → as is (+300) | M (+ one new example, changed-only review) |
| 4.2 | `02-countable-sets.md` | Countable Sets | old 3.1, verbatim | `exm-method-list-it`; full | 6,905 → as is | M |
| 4.3 | `03-diagonal-arguments.md` | Diagonal Arguments and Cantor's Theorem | old 3.3, verbatim, minus `cor-transcendental-exist` (to ST, §2); the chapter-intro and in-text choice remarks reworded (§4, R9) | `exm-method-diagonal`; full | 6,436 → ≈ 6,000 | M (hand edits) |
| 4.4 | `04-comparing-cardinalities.md` | Comparing Sizes: Schröder–Bernstein | old 3.4, verbatim, minus `prp-card-le-surjection` (to 6.1, §9 Q2). The choice-free half ("an injection \(A \to B\) with \(A \ne \emptyset\) gives a surjection \(B \to A\)") stays as a short statement, new label named at S1. | `exm-method-injections-both-ways`; Idea | 4,840 → ≈ 4,600 | M (hand edits) |
| 4.5 | `05-cardinal-arithmetic.md` | Infinite Sets and Cardinal Arithmetic | old 3.6, **condensed**. Kept: `def-disjoint-union`, `prp-card-operations-well-defined`, `prp-card-operations-monotone` (merged into one proof where possible), `exm-pairing-bijection`, `exm-method-encode`, `thm-cardinal-laws`, `exm-method-laws-by-bijection`, `cor-cantor-two-power` (now citing 2.2's `thm-power-set-two-power`), `thm-reals-power-set-naturals`, and `thm-plane-equinumerous-line`, proved by the power law alone (the payoff of the section's hook, "the plane and the line"). Parked to ST: `exm-interleaving-decimals`, `thm-baire-space-reals`, `cor-real-sequences`. The choice-free infinite-set facts (\(\nN \sqcup \nN \approx \nN\), Hilbert's hotel revisited, \(\aleph_0 \cdot \aleph_0 = \aleph_0\)) stay; the two choice-dependent theorems of old 3.5 move to 6.1. The chapter's R group (`exr-infinite-sets-r1`–`r3`) stays here; `r4` moves to 6.1. | `exm-method-encode`, `exm-method-laws-by-bijection`; Idea, then terse | 7,230 → **5,000** | F |

### Chapter 5. Relations (F2.5), directory `ch05-relations/` (was `ch04-relations-and-orders/`)

Time: about **22 h core / 28 h full**. Measured after S7 (2026-10-26): **15 h core / 30 h full** (the chapter index's Time line; §10).

| § | File | Title | Sources | Method boxes, scaffold | Now → target | Pipeline |
|---|---|---|---|---|---|---|
| 5.1 | `01-relations.md` | Properties of Relations | old 4.1, verbatim | `exm-method-relation-properties`; full | 4,460 → as is | M |
| 5.2 | `02-equivalence-relations.md` | Equivalence Relations and Partitions | old 4.2, verbatim. **Moved from old 5.2:** `prp-fibres-partition` (merged with `exm-fibres-of-function`, whose label stays), `thm-canonical-factorization` (every function is inclusion ∘ bijection ∘ quotient map), `exm-fraction-map-factorization`, exercises `a1`, `b2`, `c1`; exercise `exr-restriction-extension-and-gluing-c2` (find the error, well-definedness). The universal property of the quotient (`thm-functions-out-of-quotient`) goes to ST. The **induced map** (a rule constant on classes defines a function on the quotient) remains what `exm-method-well-definedness` already teaches. To make room, `exm-same-size-subsets` and one worked example move to exercises or folds. | `exm-method-well-definedness`; full | 7,234 + ≈ 1,500 → **5,000** with folds | F |
| 5.3 | `03-orders.md` | Partial Orders, Maximal and Greatest Elements | old 4.3, verbatim; the remark at L246 repointed (§4, R12) | none; Idea | 6,811 → as is | M |

### Chapter 6. The Axiom of Choice (F2.4), directory `ch06-axiom-of-choice/` (was `ch06-zorns-lemma/`)

Time: about **16 h core / 24 h full**. Measured after S7 (2026-10-26): **20 h core / 30 h full** (the chapter index's Time line; §10).

| § | File | Title | Sources | Method boxes, scaffold | Now → target | Pipeline |
|---|---|---|---|---|---|---|
| 6.1 | `01-countable-unions-and-choice.md` (slug kept) | The Axiom of Choice | **Verbatim** from old 3.2: "A union of countably many lists" (hook), "The axiom of choice" (`ax-choice`), "When choice is not needed" (finite choice, `exm-method-name-the-choice`, `exm-choice-or-rule`), "Right inverses" (`thm-surjection-right-inverse`, paying off 2.3's open item), "Countable unions" (`thm-countable-union`). **Moved:** `prp-card-le-surjection` from old 3.4, as the first use of right inverses; `thm-infinite-countable-subset` and `thm-infinite-iff-proper-subset` with old 3.5's "smallest infinite size" subsection, **condensed**, as "What choice buys for infinite sets" (§9 Q2); `exr-infinite-sets-r4`. **Parked to ST:** "The obstacle, rule by rule", "Unions without choice" (`exm-choice-free-unions`), "Algebraic numbers" (`thm-algebraic-countable`), exercise `c2`. **Exercises:** old 3.2's `a1`, `b1`–`b4`, `c1`, `c3`, plus old 3.5's six exercises. S1 trims the uncited ones to fit (no exercise of 3.2 or 3.5 is cited downstream). | `exm-method-name-the-choice`; full | ≈ 4,250 + ≈ 2,300 moved → **5,000** (+ folds) | F |
| 6.2 | `02-chains-and-zorn.md` (slug kept) | Zorn's Lemma and How to Use It | **Verbatim** from old 6.1: "Matching two sets, one pair at a time", "Chains", "Zorn's lemma" (`thm-zorn`, statement only), "The maximality template" (`exm-method-maximality`, `exm-zorn-representatives`), minus `thm-choice-from-zorn` (to 6.3). **Moved from old 6.2:** "Extending a partial order" (`lem-one-step-order-extension`, `thm-order-extension`, `exm-divisibility-linear-extension`), exercises `b1`, `b2`, `b3`, `c1`, and the optional basis subsection reduced to the R item `exr-using-zorn-r3` (LA §1.8 proves the theorem). | `exm-method-maximality`; full | ≈ 4,100 + ≈ 2,300 → **5,000** | F |
| 6.3 | `03-using-zorn.md` (slug kept) | Equivalent Forms of Choice | **Moved:** `thm-choice-from-zorn` (Zorn ⇒ AC) from old 6.1; `thm-cardinal-comparability` and `cor-cardinal-trichotomy` (Zorn ⇒ comparability; this pays off 4.4's open question) from old 6.2, with exercises `a1`, `c2`, `r1`, `r2` (`r2` is "maximal chains give Zorn's lemma"). **New:** the well-ordering theorem (Zorn ⇒ every set can be well-ordered, by the maximality template on well-orders of subsets ordered by initial segment; uses `def-well-ordered-set` from 5.3) and its easy converse (well-ordering ⇒ AC: choose the least element). A closing table lists which implications are proved here and which are proved in ST: AC ⇒ Zorn in ST.4, and comparability ⇒ well-ordering by Hartogs in ST.4. Proposed labels, fixed at S1: `thm-well-ordering-theorem`, `prp-well-ordering-gives-choice`. Holds the chapter's R group. | none new (the maximality template reused); Idea | ≈ 2,000 moved + ≈ 2,000 new → **4,500** | F |

The book preface (`fd2/src/index.md`) is rewritten for six chapters; it currently lists 3.6 and Chapter 5 as "in preparation".

## 2. What leaves fd2

Parked material is kept as source text, outside every `src/` tree, so the engine does not build it and atlas does not scan it. Each parked file starts with a header naming its old section, the labels it holds, and its intended home.

### 2.1 To fd5 *Algebraic Preliminaries* (parked at `fd5/authoring/parked/from-fd2/`)

| Old | Material | Labels (all d0 downstream) |
|---|---|---|
| 5.3 `03-binary-operations.md`, whole (5,927 words) | operations, closure, associativity, identities and inverses with uniqueness, pointwise operations, composition on \(X^X\), operations on a quotient | `def-binary-operation`, `exm-first-operations`, `def-operation-properties`, `exm-subtraction-identity`, `prp-operation-identity-unique`, `exm-method-two-ways`, `prp-operation-inverse-unique`, `prp-operation-inverse-rules`, `exm-two-inverses`, `prp-pointwise-operations`, `prp-composition-operation`, `prp-operation-on-quotient`, all `exr-binary-operations-*` |
| 5.4 `04-permutations-and-iteration.md`, whole (6,505 words) | permutations under composition, iterates, orbits, cycle decomposition, eventually periodic orbits | `def-permutation`, `prp-permutations-closed`, `def-iterate`, `prp-iterate-laws`, `def-orbit`, `thm-orbits-partition`, `prp-orbit-cycle`, `exm-method-follow-the-orbit`, `exm-three-pile-shuffle`, `def-permutation-cycle`, `thm-permutation-cycles`, `cor-permutation-power-identity`, `exm-squaring-mod-eleven`, `prp-eventually-periodic`, all `exr-permutations-and-iteration-*` |

fd5 Chapter 2 (Groups and Permutations) already defines `def-symmetric-group`, `def-cycle` and `thm-disjoint-cycle-decomposition`. The parked text is raw material for a later fd5 revision, and that revision resolves the overlap. Until then no fd5 file cites a parked label. The verify scripts move with the text (`fd2/verify/ch05/` binary-operation and permutation scripts → `fd5/authoring/parked/from-fd2/verify/`).

### 2.2 To ST (parked at `fd2/authoring/parked/st/`; no ST book exists yet)

| Old | Material | Labels | ST chapter |
|---|---|---|---|
| 3.2 | "The obstacle, rule by rule" (formal reason choice is needed); "Unions without choice"; "Algebraic numbers"; exercise `c2` (algebraic numbers without choice) | `exm-choice-free-unions`, `thm-algebraic-countable`, `exr-countable-unions-and-choice-c2` | ST.4 (obstacle), ST.3 (algebraic numbers) |
| 3.3 | transcendental numbers exist (depends on `thm-algebraic-countable`) | `cor-transcendental-exist` | ST.3 |
| 3.6 | interleaving decimals; \(\nN^{\nN} \approx \nR\); real sequences | `exm-interleaving-decimals`, `thm-baire-space-reals`, `cor-real-sequences` | ST.3 |
| 5.2 | "Functions out of a quotient": the universal property, its method box, maps out of the clock; exercises `b1`, `b3`, `b4`, `c2`, `c3` | `thm-functions-out-of-quotient`, `exm-method-factor-through-quotient`, `exm-clock-maps`, `exr-fibres-and-factorization-b1`, `-b3`, `-b4`, `-c2`, `-c3` | ST.1 |
| (new, for ST) | the proof that AC implies Zorn's lemma (already promised to ST.4 by `thm-zorn`'s statement); comparability ⇒ well-ordering (Hartogs) | none in fd2 | ST.4 |

### 2.3 Downstream citations stay satisfiable

Every label cited from outside fd2 either stays in fd2 (most of them only change number) or is repointed. Grep over foundations, analysis-series, linear-algebra-split and math-atlas (`*.md`, `*.yaml`, `*.json`) finds **exactly one** citation of a leaving label:

| Leaving label | Cited at | Repair |
|---|---|---|
| `thm-algebraic-countable` | `fd5/src/ch04-formal-polynomials/05-formal-derivative.md` L526 ("The same count … is the proof of @fd2:thm-algebraic-countable.") | Rewrite it as "The same count, with the polynomials written as integer tuples, shows that the algebraic numbers are countable (by @fd2:cor-product-countable and @fd2:thm-countable-union)". This is a one-sentence fd5 edit with a changed-only review. |
| `thm-algebraic-countable` | `fd5/authoring/blueprints/ch03.md` L25, L209, L312 | blueprint record: add a deviation note; no tool reads it |

The labels that **stay in fd2 but change chapter** are listed in §3. The ones cited downstream are: `ax-choice` (fd3 1.1, 1.7, Ch5; an1), `thm-countable-union` (an1, fd5), `thm-surjection-right-inverse` (la1), `prp-card-le-surjection` (2), `thm-infinite-countable-subset` (an1) and `thm-zorn` (la1). They all resolve unchanged; only their atlas chapter changes (F2.3 → F2.4 for the choice labels, §6).

## 3. Label migration (every label; names unchanged)

**Order of work.** The old section's file moves first (`git mv`), then the labels split off as listed. A label not listed moves with its section.

**New labels**, named at S1:
- 2.2: `thm-cancellation`, `prp-composite-partial-converse`, method box `exm-method-cancel`.
- 4.4: the choice-free half of `prp-card-le-surjection`.
- 6.3: `thm-well-ordering-theorem`, `prp-well-ordering-gives-choice`.

| Old § | New § | Labels |
|---|---|---|
| 1.1 | 1.1 | `def-parity`, `def-divides`, `def-prime`, `prp-divides-transitive`, `exm-method-direct-proof`, `exm-divides-combination`, `thm-even-or-odd`, `exm-method-cases`, `exm-cubes-plus-five-n`, `exm-parity-of-sums`, `exm-method-counterexample`, `exm-refute-2p-plus-1`, `exm-refute-product-of-divisors`, `exm-lattice-midpoint`; all `exr-proofs-from-definitions-*` |
| 1.2 | 1.2 | `def-set-equality`, `def-subset`, `exm-method-element-chasing`, `exm-subset-first-examples`, `prp-subset-antisymmetric`, `exm-method-double-inclusion`, `prp-subset-transitive`, `def-set-builder`, `exm-set-builder-small`, `def-empty-set`, `prp-empty-set-unique`, `thm-russell`; all `exr-sets-and-subsets-*` |
| 1.3 | 1.3 | `def-set-operations`, `thm-set-algebra`, `exm-method-chain-of-iff`, `exm-difference-chain`, `def-power-set`, `exm-power-set-small`, `def-indexed-family`, `def-family-union-intersection`, `exm-families-real-parameter`, `prp-smallest-closed-set`, `thm-de-morgan-families`; all `exr-set-operations-*` |
| 1.4 | 1.4 | `def-ordered-pair`, `exm-pair-equations`, `exm-method-uniqueness`, `def-cartesian-product`, `exm-coordinates-unique`, `exm-small-products`, `prp-product-set-laws`, `exm-product-of-intervals`, `def-relation`, `exm-relations-as-sets`; all `exr-products-and-relations-*` |
| 1.5 | **2.1** | `def-function`, `exm-first-functions`, `exm-not-a-function`, `prp-function-equality`, `exm-equal-functions`, `exm-function-set-small`, `prp-empty-function`, `def-composition`, `exm-composition-order`, `prp-composition-associative` |
| 1.5 | **2.2** | `def-injective`, `def-surjective`, `def-bijective`, `exm-method-injectivity`, `exm-method-surjectivity`, `exm-fraction-map`, `exm-injective-surjective-first`, `exm-square-three-ways`, `thm-composition-injective-surjective`; exercises `a1`, `b1`, `b2`, `b3`, `b4`, `c1`, `c2` |
| 1.6 | 2.3 | `def-left-right-inverse`, `exm-left-inverses-small-sets`, `thm-left-inverse-iff-injective`, `exm-method-construct-and-verify`, `exm-left-inverse-construction`, `prp-right-inverse-surjective`, `exm-right-inverses-finite`, `prp-inverse-unique`, `def-inverse-function`, `exm-two-sided-inverses`, `thm-bijection-iff-inverse`; all `exr-inverses-*` |
| 1.7 | 2.4 | `def-image`, `def-preimage`, `exm-images-finite`, `exm-images-of-square`, `exm-sets-of-numbers-as-images`, `thm-preimage-operations`, `prp-preimage-composition`, `thm-image-union`, `exm-image-two-witnesses`, `thm-image-intersection`, `prp-image-preimage`; all `exr-images-and-preimages-*` |
| 2.1 | 3.1 | `lem-naturals-arithmetic`, `exm-predecessor-no-hypothesis`, `prp-integers-closed`, `thm-well-ordering`, `exm-no-infinite-descent`, `exm-method-least-element`, `exm-least-element-down-by-two`, `thm-induction-iff-well-ordering`, `cor-well-ordering-integers`; all `exr-naturals-and-well-ordering-*` |
| 2.2 | 3.2 | `thm-induction`, `thm-strong-induction-from-base`, `exm-method-induction-step`, `exm-choosing-the-base`, `thm-division-algorithm`, `lem-lowest-terms`, `thm-prime-factor`, `exm-all-equal-induction`, `exm-strengthen-hypothesis` and the rest of the file; all `exr-induction-in-practice-*` |
| 2.3 | 3.3 | `thm-recursion`, `cor-recursion-from-base`, `cor-two-step-recursion`, `def-sum-product`, `def-power`, `prp-power-laws`, `prp-sum-first-n`, `prp-geometric-sum`, `thm-bernoulli`, `prp-finite-max`; all `exr-recursion-*` |
| 2.4 | 3.4 | `exm-contrapositive-mod-three`, `exm-method-choosing-the-form`, `thm-primes-infinite`, `prp-cube-root-two-irrational`, `exm-method-smallest-counterexample`, `exm-three-power-factor`; all `exr-contrapositive-and-contradiction-*` |
| 2.5 | **4.1** | `def-equinumerous`, `prp-equinumerous-properties`, `def-finite`, `def-infinite`, `thm-pigeonhole`, `cor-pigeonhole-finite-sets`, `exm-method-pigeonhole`, `exm-five-lattice-points`, `cor-finite-size-unique`, `prp-disjoint-union-count`, `prp-subset-finite`, `cor-remove-point`, `prp-power-set-count`, `thm-finite-no-proper-copy`, `exm-hilbert-hotel`; all `exr-finite-sets-*` |
| 3.1 | 4.2 | `def-countable`, `def-countably-infinite`, `lem-subsets-of-naturals`, `thm-countable-characterizations`, `exm-method-list-it`, `prp-countable-subset`, `prp-countable-image`, `prp-union-two-countable`, `exm-rows-first-listing`, `thm-product-countable`, `cor-product-countable`, `thm-integers-rationals-countable`, `exm-list-two-element-subsets`, `exm-list-integer-combinations`; all `exr-countable-sets-*` |
| 3.2 | **6.1** | `ax-choice`, `exm-method-name-the-choice`, `exm-choice-or-rule`, `thm-surjection-right-inverse`, `thm-countable-union`; exercises `a1`, `b1`, `b2`, `b3`, `b4`, `c1`, `c3` |
| 3.2 | ST | `exm-choice-free-unions`, `thm-algebraic-countable`; exercise `c2` |
| 3.3 | 4.3 | `exm-five-strings-diagonal`, `thm-binary-sequences-uncountable`, `exm-method-diagonal`, `exm-diagonal-outgrows-list`, `thm-cantor`, `cor-powerset-naturals-uncountable`, `def-decimal-expansion`, `thm-reals-uncountable-decimal`; all `exr-diagonal-arguments-*` |
| 3.3 | ST | `cor-transcendental-exist` |
| 3.4 | 4.4 | `def-card-le`, `prp-card-le-preorder`, `thm-schroder-bernstein`, `exm-method-injections-both-ways`, `exm-closed-open-interval`, `exm-reals-open-interval`; all `exr-comparing-cardinalities-*` |
| 3.4 | **6.1** | `prp-card-le-surjection` |
| 3.5 | **6.1** | `thm-infinite-countable-subset`, `thm-infinite-iff-proper-subset`; exercises `a1`, `b1`, `b2`, `b3`, `c1`, `c2` |
| 3.6 | 4.5 | `def-disjoint-union`, `exm-two-copies-of-naturals`, `prp-card-operations-well-defined`, `prp-card-operations-monotone`, `exm-pairing-bijection`, `exm-method-encode`, `thm-cardinal-laws`, `exm-method-laws-by-bijection`, `cor-cantor-two-power`, `thm-reals-power-set-naturals`, `thm-plane-equinumerous-line`; all `exr-cardinal-arithmetic-*`; `exr-infinite-sets-r1`, `-r2`, `-r3` |
| 3.6 | **2.2** | `thm-power-set-two-power` |
| 3.6 | ST | `exm-interleaving-decimals`, `thm-baire-space-reals`, `cor-real-sequences` |
| 3.6 | **6.1** | `exr-infinite-sets-r4` |
| 4.1 | 5.1 | `def-relation-properties`, `exm-checking-a-relation`, `exm-method-relation-properties`, `prp-divides-partial-order`, `exm-relation-table`; all `exr-relations-*` |
| 4.2 | 5.2 | `def-equivalence-relation`, `exm-first-equivalences`, `def-equivalence-class`, `def-partition`, `def-quotient-set`, `thm-classes-partition`, `thm-partition-equivalence`, `def-congruence`, `prp-congruence-equivalence`, `prp-integers-mod-n`, `exm-fibres-of-function`, `exm-reals-mod-integers`, `prp-congruence-arithmetic`, `exm-method-well-definedness`, `exm-ill-defined-class-map`, `exm-same-size-subsets`; all `exr-equivalence-relations-*` |
| 4.3 | 5.3 | `def-partial-order`, `exm-subset-order-not-total`, `def-order-bounds`, `def-greatest-element`, `def-maximal-element`, `prp-greatest-unique`, `prp-greatest-maximal`, `exm-maximal-not-greatest`, `def-order-supremum`, `exm-divisibility-lcm`, `def-well-ordered-set`; all `exr-orders-*` |
| 5.1 | **2.1** | `def-restriction-extension`, `prp-restriction-properties` |
| 5.1 | **2.2** | `thm-gluing`, `exm-method-gluing`, `exm-piecewise-as-gluing`, `def-indicator`, `prp-indicator-arithmetic`, `exm-symmetric-difference-associative`; exercises `a1`, `b1`, `b2`, `b3`, `b4` |
| 5.1 | 4.1 / 5.2 / 4.5 | exercise `c1` → 4.1; `c2` → 5.2; `c3` (Cantor through indicators) → 4.5 |
| 5.2 | 5.2 | `prp-fibres-partition`, `thm-canonical-factorization`, `exm-fraction-map-factorization`; exercises `a1`, `b2`, `c1` |
| 5.2 | ST | `thm-functions-out-of-quotient`, `exm-method-factor-through-quotient`, `exm-clock-maps`; exercises `b1`, `b3`, `b4`, `c2`, `c3` |
| 5.3 | fd5 (parked) | every label of the file (§2.1) |
| 5.4 | fd5 (parked) | every label of the file (§2.1) |
| 6.1 | 6.2 | `def-chain`, `lem-chain-union`, `thm-zorn`, `exm-method-maximality`, `exm-zorn-representatives`; all `exr-chains-and-zorn-*` |
| 6.1 | **6.3** | `thm-choice-from-zorn` |
| 6.2 | **6.2** | `lem-one-step-order-extension`, `thm-order-extension`, `exm-divisibility-linear-extension`; exercises `b1`, `b2`, `b3`, `c1`, `r3` |
| 6.2 | **6.3** | `thm-cardinal-comparability`, `cor-cardinal-trichotomy`; exercises `a1`, `c2`, `r1`, `r2` |

**Files.**
- **Directories.** `ch01-sets-and-functions` → `ch01-sets`. The new `ch02-functions` takes old 1.5–1.7. `ch02-induction-and-finite-sets` → `ch03-induction-and-recursion`. `ch03-countable-and-uncountable` → `ch04-cardinality`. `ch04-relations-and-orders` → `ch05-relations`. `ch05-building-functions` is removed after the split. `ch06-zorns-lemma` → `ch06-axiom-of-choice`.
- **Other files.** `verify/chNN/<label>.py` scripts follow their labels to the new chapter directory. `authoring/ledger/chNN.yaml` is regenerated per new chapter, with item evidence untouched. `config/config.json` lists the six new directories.

## 4. Forward-reference repairs

These are the forward references the new order creates (survey §B), with the fix for each. After the moves, `tools/check_structure.py` and the forward-dependency ledger check must show no `@label` citing a later section.

| # | Where (new) | Cites (new) | Repair |
|---|---|---|---|
| R1 | 2.1 exercises (old 1.5 `a1`, `b4`; L597, 705, 729) | 2.2 methods | Moot: all seven old 1.5 exercises move to 2.2, and 2.1 gets new ones. |
| R2 | 2.1 `prp-restriction-properties` (old 5.1 L60, L74); exercises `b1`, `b2`, `c1` | 2.3 `thm-bijection-iff-inverse`; 2.4 `def-image`, `thm-image-union`, `thm-image-intersection` | Cut the proposition to "restriction commutes with composition; the restriction of an injection is injective". The image parts become a 2.4 exercise and the bijection part a 2.3 exercise. Exercises `b1`, `b2` move to 2.2 after the definitions they need; `c1` goes to 4.1. |
| R3 | 2.1/2.2 (old 5.1 L41 remark, `a1`) | 4.1 `cor-pigeonhole-finite-sets` | The remark becomes a one-line Looking-ahead with no `@`; the part of `a1` that uses pigeonhole is cut. |
| R4 | 2.2 (old 5.1 hook L7 "a function in two pieces" = Schröder–Bernstein; `exm-piecewise-as-gluing`; `def-indicator`; `exm-symmetric-difference-associative`; `c3`) | 4.3 `thm-cantor`, `thm-binary-sequences-uncountable`; 4.4 `thm-schroder-bernstein`; 4.5 `thm-power-set-two-power`, `cor-cantor-two-power`; 4.2 `exr-countable-sets-c2` | New hook: \(|x|\) and the sign function as functions given in pieces. Schröder–Bernstein keeps its own "two pieces" motivation in 4.4, citing `thm-gluing` backwards. `thm-power-set-two-power` moves into 2.2 (§1). Forward sentences in the examples are cut. `c3` moves to 4.5. |
| R5 | 2.2 (old 5.1 `c2`) | 5.2 `exm-method-well-definedness` | The exercise moves to 5.2. |
| R6 | 2.3 prose L251, L402 "Chapter 3 states it / proves it" | 6.1 | Change to "Chapter 6". This is a prose pointer; nothing depends on it, and it is logged as a ledger promise. |
| R7 | 1.2 second reading L298 "until Chapter 3 … (Section 1.6 shows where it is first needed)" | 6.1, 2.3 | Change to "until Chapter 6 … (Section 2.3 shows …)". |
| R8 | 3.2 `exr-induction-in-practice-b2` | 3.3 `def-sum-product` | Exists today and was approved; left as is. |
| R9 | 4.3 chapter intro (L3), choice remarks, `cor-transcendental-exist` (L283) | 6.1 `thm-countable-union`, `ax-choice`; ST | The corollary is parked. The intro and remarks are reworded so that they no longer mention countable unions; one prose pointer to Chapter 6 is allowed. |
| R10 | 4.4 `prp-card-le-surjection` (L65); S–B remark L166 ("no use of @ax-choice"); `exm-reals-open-interval` L270 | 6.1 | The proposition moves to 6.1 (§9 Q2), and its choice-free half stays in 4.4. L166 becomes "every value of \(h\) is given by a rule; nothing is chosen", with no citation. L270's comparability question points to Chapter 6 in prose (its ledger promise is retargeted F2.4 §03). |
| R11 | 4.5 (old 3.5 L16, L20, L103; intro; `a1`, `b1`, `b2`) and old 3.6 `exr-infinite-sets-r4` (L736) | 6.1 `ax-choice`, `thm-countable-union` | Moot under the default: these move to 6.1. |
| R12 | 5.3 `def-well-ordered-set` remark (L246) | 6.1, 6.3 | Prose "Chapter 6" with no `@`; the ledger promise is retargeted F2.4 §03 (the well-ordering theorem is now proved in fd2). |
| R13 | 5.2 exercises (old 5.2 `b1`, `b3`, `b4`, `c2`, `c3`) | ST `thm-functions-out-of-quotient` | Parked with the theorem; 5.2's exercise set is refilled from the kept ones and S1. |
| R14 | 6.2 `thm-zorn` (L92); `exm-divisibility-linear-extension` (L182, L184); exercises `a1`, `c2`, `r1` | 6.3 `thm-choice-from-zorn`, `thm-cardinal-comparability` | The exercises move to 6.3. `thm-zorn`'s remark points forward to 6.3 in prose. S1 rewrites the example's two citations to use only `thm-order-extension`. |
| R15 | 3.3 iterates (if kept) | fd5 `prp-permutations-closed` | Not applicable: iterates go to fd5. |

## 5. Pointer sweep map

**Pass 1 (mechanical, `tools/renumber.py`).** Map the unambiguous section numbers, applied all at once, not in a chain:

| old | 1.6 | 1.7 | 2.1 | 2.2 | 2.3 | 2.4 | 2.5 | 3.1 | 3.2 | 3.3 | 3.4 | 3.5 | 3.6 | 4.1 | 4.2 | 4.3 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| new | 2.3 | 2.4 | 3.1 | 3.2 | 3.3 | 3.4 | 4.1 | 4.2 | 6.1 | 4.3 | 4.4 | 6.1 | 4.5 | 5.1 | 5.2 | 5.3 |

The file moves of §3 go into the same `moves` block. Excluded, as before: ledgers, reviews, and the frozen blueprints `ch01.md`–`ch03.md`.

**Pass 2 (by hand).** These are the split sections and the chapter numbers, where the meaning decides:

| old | new |
|---|---|
| Section 1.5 | 2.1 (function, equality, composition) or 2.2 (injective, surjective, bijective) |
| Section 3.4 when it means `prp-card-le-surjection` | 6.1 |
| Section 3.6 when it means a parked result | delete the pointer |
| Section 5.1 | 2.1 (restriction, extension) or 2.2 (gluing, indicators) |
| Section 5.2 | 5.2, or delete the pointer (universal property) |
| Section 5.3, 5.4 | delete the pointer, or name fd5 in prose |
| Section 6.1 | 6.2, or 6.3 for Zorn ⇒ AC |
| Section 6.2 | 6.2 (order extension) or 6.3 (comparability) |
| Chapter 1 | 1 (sets), or 2 (functions, inverses, images) |
| Chapter 2 | 3, or 4 for finite sets |
| Chapter 3 | 4, or 6 for choice and countable unions |
| Chapter 4 | 5 |
| Chapter 5 | 2 or 5, or delete the pointer |
| Chapter 6 | 6 |

**Scope.**
- **fd2 itself**: 494 prose "Section N.N"/"Chapter N" references, plus the six chapter indexes and the preface, which are rewritten rather than swept.
- **fd1**: 72 lines that name fd2 with a number. The eight "Minimum before *Sets and Functions*" lines change "Section 2.5" to "Section 4.1". In `ch08…/03-levels-of-abbreviation.md`, "Chapters 1–6" stays.
- **fd3**: 139 lines. The most frequent are "Chapter 2" (induction, recursion) → 3, "Section 4.2" → 5.2, "Section 2.3" → 3.3 and "Section 2.2" → 3.2. "Chapters 1 to 6" stays. About a dozen hits of the form "Chapter 4, and *Sets and Functions*" name fd1's own Chapter 4 and are left alone.
- **fd4**: 13 lines. **fd5**: 25 lines in `src` and blueprints, plus the L526 citation of §2.3.
- **an1** (analysis-series): 14 files name the book. All are read by hand; the ones that point at countable sets or choice need "Chapter 3" changed to 4 or 6.
- **la1** (linear-algebra-split): `ch00-borrowed/index.md` and the files listed in the addendum §3 name the book. Its `@fd2:` labels all stay. Prose numbers are read by hand and edited only in that repository's own pass; they are listed here only as a record.
- **`authoring/STATUS.md`**: the F2 rows are rewritten (six chapters, new section lists). Ledger promise rows that name a moved label are retagged by §3 when their text moves (for example 4.4 L464 → F2.4 §03).

## 6. Atlas changes (math-atlas, same commit as the structural move)

- **`registry/chapters.yaml`** gets the new order F2.1, F2.6, F2.2, F2.3, F2.5, F2.4:
  - F2.1 "Sets" (集合).
  - **F2.6 "Functions" (函數)**: the id is reused and the old title "Building Functions" retired. The `src` entries for functions (ab:6's function half; `la:ch00/04` if, as expected, that is the functions section) move from F2.1 to F2.6.
  - F2.2 "Induction and Recursion" (歸納與遞迴).
  - F2.3 "Cardinality" (基數); the "含選擇公理的陳述" tag is dropped from `title_zh`.
  - F2.5 "Relations" (關係).
  - F2.4 "The Axiom of Choice" (選擇公理).
- **`registry/renames.yaml`** `titles`: six rows (F2.1, F2.6, F2.2, F2.3, F2.5, F2.4), each `decided:` the approval date, `spec: fd2/authoring/design/layout-six-chapters.md`. No `ids` or `moves` rows are needed, because every id stays in volume F2.
- **`registry/plan-edges.yaml`**:
  - `F2.1: {s: [F1.5]}`, unchanged.
  - `F2.6: {s: [F2.1]}` (Functions; this replaces `{s: [F2.5, F2.2, F2.3]}`, which belonged to Building Functions).
  - `F2.2: {s: [F2.6, F1.6]}` (recursion needs functions).
  - `F2.3: {s: [F2.2, F2.6, F1.6]}` (finite sets keep the fd1 exercise citations).
  - `F2.5: {s: [F2.3, F2.2, F2.6], see: [F1.6]}` (5.2 uses fibres and equinumerosity).
  - `F2.4: {s: [F2.5, F2.3]}`, unchanged; it adds `see: [F1.6]` only if old 3.5's counter-model passage moves into 6.1.
  - Downstream:
    - F5.3 keeps `see: [F1.6, F2.6]`; its comment changes to "permutations and binary operations parked in fd5 (from fd2)".
    - Edges that need choice move from F2.3 to F2.4:
      - AN1.11 becomes `b: [F2.4]`, with its scope recomputed.
      - The comment on MT.1 changes.
      - ST.6a becomes `{s: [MT.1, F2.4]}`.
      - F3.1 adds `see: [F2.4]` (fd3 1.1 and 1.7 cite `ax-choice`).
      - fd3 Chapter 5's chapter adds `see: [F2.4]`.
      - an1 chapters whose blueprints cite `thm-countable-union` or `ax-choice` (an1 blueprints ch02, ch05, ch06, ch08) gain F2.4 wherever `atlas.py check` reports a missing ancestor.
- **`registry/statements.yaml`**:
  - `def-function`, `def-image`, `thm-bijection-iff-inverse`: F2.1 → F2.6.
  - `def-ac`, `thm-countable-union`: F2.3 → F2.4.
  - `thm-quotient-up` **stays F2.5**. Its gloss ("良定義的函數可通過商") is the induced map that 5.2's well-definedness method keeps. Only the formal universal-property theorem text is parked; retagging it to ST would break the `s` ancestry of `def-integers`, `def-zn`, `def-complete-metric` and `def-lp`, which use it.
  - New: `thm-well-ordering-theorem`, F2.4, "良序定理（由 Zorn 引理；AC ⇒ Zorn 延至 ST.4）".
- **`registry/terms.yaml`**: the function terms (function, graph, composition, composite, identity function, injective/surjective/bijective, image, preimage, inverse, restriction, extension, indicator) move `ch: F2.1` → F2.6. The set terms stay F2.1.
- **`registry/chapter-constraints.yaml`**: the F2.4 rule becomes: state the axiom of choice, Zorn's lemma, the well-ordering theorem and the easy implications; AC ⇒ Zorn and comparability ⇒ well-ordering are proved in ST.4; `takes: [thm-zorn]` is unchanged.
- **ST** (in `chapters.yaml`, as comments or notes; no new ids):
  - ST.4 Equivalents of the Axiom of Choice receives AC ⇒ Zorn, Hartogs, and "the obstacle, rule by rule".
  - ST.3 Cardinal Arithmetic receives the algebraic and transcendental numbers, \(\nN^{\nN} \approx \nR\) and real sequences.
  - ST.1 The Axioms of ZF receives the universal property of the quotient.
  - Each entry points to `fd2/authoring/parked/st/`.
- **`site/books.json`**: fd2 keeps `planned: 6`, and the blurb is rewritten for the six chapters. Section URLs change on the preview site; no redirects are made per page.
- **`authoring/series.json`** in foundations and analysis-series: regenerate (`tools/series.py refresh`).

## 7. Pipeline

There is **one structural commit**. It makes all the `git mv`s, the splits along §3, the parking of §2, pointer passes 1 and 2, the atlas edits, the ledger regeneration and the fd5 L526 sentence. `check_structure` (0 fatal) and `atlas.py check` must pass before it is committed. After that come the deepen passes, one workflow at a time (lean rules: changed-only blind review, S7 re-referee = S7r, hand round 2, Sonnet for minor revisers):

| Kind | Sections | What runs |
|---|---|---|
| **F**: full S1–S4, then S5–S8 and review | 2.1, 2.2, 4.5, 5.2, 6.1, 6.2, 6.3 (seven sections) | One S1 blueprint per chapter: `ch02-functions.md` (2.1, 2.2), `ch04-cardinality-tail.md` (4.5), `ch05-relations-fibres.md` (5.2), `ch06-axiom-of-choice.md` (6.1–6.3). Suggested order: Ch2, Ch6, 4.5, 5.2. |
| **M+**: moved, with hand edits | 1.2 (L298), 2.3 (L251, L402), 2.4 (one exercise), 4.1 (one example, two exercises), 4.3 (corollary out, intro), 4.4 (proposition out, L166, L270), 5.3 (L246) | S8 and a changed-only blind review of the edited passages |
| **M**: moved, numbering and pointers only | 1.1, 1.3, 1.4, 3.1, 3.2, 3.3, 3.4, 4.2, 5.1 | S8 build check only; no review is reopened; the S9 sample reads the new numbers |
| Outside fd2 | fd5 05-formal-derivative L526 | changed-only review |

The S9 sampling stays with the author, as for every chapter.

## 8. Time, before and after

These are estimates by STYLE §2's formula; each chapter's Time line is recomputed with `tools/check_structure.py --words` after its deepen pass.

| Before (chapter) | core/full h | After (chapter) | core/full h |
|---|---|---|---|
| 1 Proofs from Definitions: Sets and Functions | 40/55 | 1 Sets | 20/28 |
| — | — | 2 Functions | 22/30 |
| 2 Induction, Contradiction, and Finite Sets | 30/40 | 3 Induction and Recursion | 22/30 |
| 3 Countable and Uncountable Sets | 35/55 | 4 Cardinality | 30/45 |
| 4 Relations: Equivalence and Order | 20/25 | 5 Relations | 22/28 |
| 5 Building Functions | 25/35 | — (split into 2.1, 2.2 and 5.2; fd5; ST) | — |
| 6 Zorn's Lemma | 10/15 | 6 The Axiom of Choice | 16/24 |
| **Total** | **160/225** | **Total** | **≈ 132/185** |

**Words.** The main line goes from 167,145 to about **141,000** (−16%). About 12,400 words go to fd5 (parked) and about 4,500 to ST (parked, counting the 3.6 cuts). About 9,000 come out by condensing 4.5, 5.2, 6.1 and 6.2, and about 3,500 are added (2.2's new topics, 6.3's well-ordering theorem).

## 9. Open questions for the author (answered 2026-10-26, §0)

1. **2.2 is tight.** Injections and surjections, the six new topics, gluing and characteristic functions come to about 7,000 words if nothing is trimmed.
   - **Default:** keep the approved table of contents. Restriction and extension go to 2.1, one worked example of old 1.5 becomes an exercise, gluing and indicators are condensed, and 2.2 is drafted to 5,000.
   - **Alternative:** a fifth section in Chapter 2, "2.3 Gluing and Characteristic Functions", so that inverses become 2.4 and images 2.5.
2. **Choice used before Chapter 6.** Old 3.4's `prp-card-le-surjection` and old 3.5's two theorems (every infinite set has a countably infinite subset; infinite iff the same size as a proper subset) need the axiom of choice.
   - **Default:** move them to 6.1 as "what choice buys", so no proof uses a later axiom. 4.4 keeps the choice-free half, and 4.5 keeps the choice-free infinite-set facts.
   - **Alternative:** leave them in 4.4/4.5, with a flagged prose pointer to 6.1 in each proof. This matches the "infinite sets" wording of the approved 4.5 more literally, but puts a dependency on later material inside the book.

## 10. Addendum: after S7 (fd2 wrap-up, 2026-10-26)

**Time, measured.** Each chapter's Time line was recomputed by STYLE §2 after S7: reading at 15 minutes per 400 words of the whole section files (`tools/check_structure.py --words`; main line for the core track, plus the folds for the full track), plus 20–45 minutes per exercise (the midpoint, 32.5 minutes), the core track counting all of A, one B and one C per section and the exit checks, the full track every exercise; rounded to the nearest 5 hours.

| Chapter | Main line + folded words | Exercises core / all | core/full h (plan in §8) |
|---|---|---|---|
| 1 Sets | 26,384 + 1,054 | 12 / 33 | 25/35 (20/28) |
| 2 Functions | 33,267 + 880 | 15 / 41 | 30/45 (22/30) |
| 3 Induction and Recursion | 25,448 + 504 | 12 / 33 | 20/35 (22/30) |
| 4 Cardinality | 33,892 + 375 | 15 / 42 | 30/45 (30/45) |
| 5 Relations | 20,070 + 1,667 | 9 / 28 | 15/30 (22/28) |
| 6 The Axiom of Choice | 19,789 + 0 | 10 / 28 | 20/30 (16/24) |
| **Total** | **158,850 + 4,480** | **73 / 205** | **140/220** (≈ 132/185) |

The plan's word estimate (§8, about 141,000) counted the main line to `## Exercises`; the figures above count the whole files, exercises and solutions included, as the Time formula reads them.

**R group moved from 4.1 to 3.4 (S8 seam finding F027, coordinator's wrap-up).** The structural commit carried old 2.5's `### R. Review` into 4.1 verbatim, which left Chapter 4 with two R groups and Chapter 3, whose last section is 3.4, with none (STYLE §11.5: last section only). The three items moved to the end of `ch03-induction-and-recursion/04-contrapositive-and-contradiction.md` with their ledger lines, and were relabelled to that section's slug: `exr-finite-sets-r1`, `-r2`, `-r3` → `exr-contrapositive-and-contradiction-r1`, `-r2`, `-r3` (titles `[R1]`–`[R3]` unchanged; no `@ref` to them existed). Sidecars `verify/ch04/exr-finite-sets-r1.py`, `-r2.py` → `verify/ch03/exr-contrapositive-and-contradiction-r1.py`, `-r2.py`; ledger entries moved from `authoring/ledger/ch04.yaml` to `ch03.yaml` with their verdict history, plus an S8 `correct` by the coordinator. R1 (injections and surjections) now reaches one chapter back, as §11.5 wants; R2 and R3 are the *Logic and Proof* spiral items. The Chapter 3 index already named the review exercise's fd1 labels.

**Other wrap-up edits.** 4.1's fold "Subsets and functions to {0, 1}" now cites `@thm-power-set-two-power` (Section 2.3) for the correspondence (F040). The ten Chapter 6 exercises parked by the Chapter 6 blueprint (§3 "Parked") were written out to `fd2/authoring/parked/ch06-exercises.md` from `09cf1f1`, with their ledger items in `parked/ledger-parked.yaml` (`parked_file: ch06-exercises.md`). STYLE §6 now says that exercise ids are stable keys and need not match the section slug after a re-cut.

