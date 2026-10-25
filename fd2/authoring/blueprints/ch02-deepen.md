<!-- hand-written -->
# Deepening blueprint: F2.2 Induction, Contradiction, and Finite Sets (fd2 Chapter 2), stage S1

**Status: S2 applied, frozen, 2026-10-25.** S2 (two blind referees, one round) answered below in "S2 replies (round 1)". Next: S2a, then S3.

**What this is.** The S1 blueprint for fd2 Chapter 2 under the binding layout `fd2/authoring/design/layout-final.md` (option C; §1 Ch2 rows, §2, §3, §4, §5, §7). A drafter executes it with this file, the current `fd2/src/ch02-induction-and-finite-sets/` files, `authoring/STYLE.md` (§1 "House manner from fd2 on", §2 item 6, §4, §11, §12.0, §12.1, §12.5, §12.8, §12.13.4, §12.14), `DRAFTING.md` and `NOTATION.md`. Format: `ch01-deepen.md` (frozen), leaner.

**File state and line references.** The S1 commit records the coordinator's moves: the directory renamed from `ch02-relations-and-induction`; old 2.4–2.6 now `fd2/src/ch04-relations-and-orders/01…03` (Chapter 4, no `index.md` yet); old 3.1 now `05-finite-sets.md`; old 3.2–3.6 now `ch03…/01…05`; sidecars moved by label; ledgers split (`ch02.yaml`, `ch03.yaml`, `ch04.yaml`); `config.json` lists four chapters. No text was edited. Line references are to the files at that commit: `21:` `01-naturals-and-well-ordering.md`, `22:` `02-induction-in-practice.md`, `23:` `03-recursion.md`, `25:` `05-finite-sets.md`, `ix:` the chapter's `index.md`; `3/0k:` and `4/0k:` are files of Chapters 3 and 4. `04-contrapositive-and-contradiction.md` is new.

**Word counts** are main-line prose words by `tools/check_structure.py`'s `prose_words` (a math span is one word; code and folds excluded), top of file to `## Exercises`, measured at the S1 commit:

| File | Main line now | Layout budget |
|---|---|---|
| 21 | 4,136 | 5,000 |
| 22 | 3,364 | 5,000 |
| 23 | 3,809 | 5,000 |
| 24 (new) | — | 4,500 |
| 25 | 4,160 | 5,000 + fold |

(`check_structure.py --words` prints 6,473 / 5,822 / 5,877 / 6,664 for the whole files, exercises included, and labels them "main line" as an advisory; that whole-file advisory is accepted, and the budget is the count to `## Exercises`, §8.) All four files are under budget now; the folds named below make room for what is added.

**Inputs.** Layout as above. The Cummings long-form skill for its moves only: motivation before a major definition, scratch work kept apart from the proof, hooks and payoffs; no footnotes, jokes, history or first person. *Proofs* (Cummings) was read for technique only. Not used, and checked against (pdftotext, at S2): its Propositions 1.9–1.11 (the {x, 2n + 1 − x} pairings; "one divides another") and Exercises 1.8–1.24 ("n + 1 numbers from {1, …, 2n}"); Exercises 2.25–2.26 (3 | 4ⁿ − 1; n² − n + 5); Exercises 4.3–4.7 (3 | 4ⁿ − 1, 5 | 6ⁿ − 1, 6 | n³ − n; 1·1! + ⋯ + n·n!; n! > 2ⁿ; n² < 3ⁿ); its Propositions 6.2–6.7 and 7.1–7.4 (n² odd ⇒ n odd; 3n + 5 even; m ∤ nt; "no largest natural number"; "no smallest positive rational"; 15m + 35n = 1), its Exercises 6.3–6.10 and 7.2–7.13 (3 ∤ n² ⇒ 3 ∤ n; 8 ∤ n² − 1 ⇒ n even; m ∤ nt ⇒ m ∤ n and m ∤ t; x + y ≥ 2 ⇒ x ≥ 1 or y ≥ 1; x³ + x > 0 ⇒ x > 0; x² − 5x + 6 < 0; mn odd; √5, √p, √15; a² + b² = c²; 4 ∤ n² + 2). Its list-and-contradiction write-up of the infinitude of primes and its 2·3·5·7 + 1 computation are not used; C2 of 2.4 is Euclid's argument in direct form with its own numbers. Its sums of distinct powers of 2 are not used, and its general kn + 1 pigeonhole theorem is not stated: the one generalized-pigeonhole item (25 B2 (b)) is a single instance proved from @prp-disjoint-union-count. Every example, item and answer below is the book's own; the items S2 found too close to the exercises above were replaced (S2 replies, items 1, 4, 9, 17–19). The old blueprints `ch02.md` and `ch03.md` fixed what this one keeps: key proofs `thm-well-ordering` and `thm-recursion`; the Try-it-firsts on `thm-well-ordering` and `thm-division-algorithm`; `exm-all-equal-induction`; the exit check 22 C1 (the 4a + 7b induction); and the finite-sets items 25 A1, B1–B3, C1, C2 (B2 (b), Cummings's Proposition 1.9 with its numbers, is replaced under its label: §4.5 item 21).

**Binding rules.**
1. **No label is lost or renamed; cited content is kept.** Every label now in 21, 22, 23, 25 stays in its file. The downstream-cited labels of layout §3.2 (rows 2.1, 2.2, 2.3, 3.1 → 2.5) keep the content of their blocks. 2.2's subsection `## The smallest counterexample` (22:69–84, heading to the end of 22:84) moves **verbatim** to 2.4; it contains no label. Moving a passage verbatim into a fold is not a change. No cited statement goes into a fold.
2. **fd1 is cited, never re-taught.** Induction and strong induction (@fd1:ax-induction, @fd1:thm-strong-induction); the three faces of "by contradiction" (*Logic and Proof*, Section 8.1, subsection "The three faces of 'by contradiction'"; @fd1:exm-rhetoric-contradiction, @fd1:prp-contrapositive, @fd1:prp-contrapositive-converse, @fd1:def-rule-raa, @fd1:def-rules-negation, @fd1:prp-de-morgan); √2 (@fd1:thm-sqrt2-irrational) and @fd1:prp-log2-9-irrational; witness-free existence (*Logic and Proof*, Section 8.7, @fd1:thm-irrational-power-rational); @fd1:exm-strengthen-the-claim; @fd1:thm-odd-iff-square-odd, @fd1:thm-square-even-implies-even; the catalogue @fd1:exm-not-allowed-catalogue.
3. **Chapter 1's method boxes are cited, not re-taught** (`exm-method-direct-proof`, `-cases`, `-counterexample`, `-element-chasing`, `-double-inclusion`, `-chain-of-iff`, `-uniqueness`, `-injectivity`, `-surjectivity`, `-construct-and-verify`).
4. **fd3 division (layout §4).** No gcd, Bézout, Euclid's lemma, unique factorization or ℤ/n. Divisibility arguments use @def-divides, @exm-divides-combination, @thm-division-algorithm and parity only. `thm-primes-infinite` is new to the series; fd3 needs no twin.
5. **Numbering.** Before S3 the coordinator applies the section map of §4.8 to the old-numbered files only (by hand from the table, or `tools/renumber.py --dry-run` and applying only the listed hunks); never series-wide at this stage, since fd2 Chapter 1, STATUS and the Ch1 ledgers already use the new numbering. Drafters then write every pointer in the final numbering. The fd1/fd3/fd4 pointers stay for layout §3.3's sweep.
6. **No drill banks; Quick checks about one per 800–1,000 main-line words** (layout §5). Each method section has one `[B4: Prove or disprove]`, verdicts withheld; the solution gives the verdict first.

---

## 1. Devices as applied

- **Method boxes** (STYLE §2 item 6): five, `::: {#exm-method-<slug>}`, title `[Method: …]`, lead-ins **Template.**, **When to use it.**, **The usual failure.**, each ≤ 130 words: `least-element` (2.1); `induction-step` (2.2); `choosing-the-form`, `smallest-counterexample` (2.4); `pigeonhole` (2.5). All linked from the index's Named moves.
- **`[Scratch work]` ideas** (`::: {.idea}` titled `[Scratch work]`, ≤ 20 lines), one at each box's first full appearance: `exm-no-infinite-descent` (2.1), the example 7 | 9ⁿ − 2ⁿ (2.2), `exm-contrapositive-mod-three` (2.4), `exm-three-power-factor` (2.4), `thm-pigeonhole` (2.5, replacing its Idea).
- **Givens/Goal tables in prose form** (§12.5), inside each of those scratch works; the last row shows the gap.
- **Prove or disprove** (§12.13.4): 21 B4, 22 B4, 24 B4, 25 B4. 2.3 is not a method section and gets none.
- **Fading** (layout §1): least element full in 2.1, Idea-level back-references in 2.2 (the Idea of `thm-division-algorithm`, §4.2 item 13; the pointer before `lem-lowest-terms`, §4.2 item 7) and 2.5 (the Idea of `cor-pigeonhole-finite-sets`, §4.5 item 22); induction step full in 2.2 (two worked examples), Idea in 2.3; choosing-the-form and smallest counterexample full in 2.4 (each with two worked examples: `exm-contrapositive-mod-three` and the Quick check's three forms; `lem-lowest-terms` and `exm-three-power-factor`), and in 2.5 a bold paragraph after the proof of `thm-finite-no-proper-copy` ("Contradiction at scale", §4.5 item 15); pigeonhole full in 2.5.
- **Threads** (layout §5): *the lattice points* (1.1 → 2.5 opening and `## Back to the pigeons`, paid by `thm-pigeonhole` and `exm-five-lattice-points`); *same size* (1.6 → 2.5 `def-equinumerous` → 4.2); *the halving* (21:148 → `exm-no-infinite-descent` → `lem-lowest-terms` → `prp-cube-root-two-irrational`); *infinitely many primes* (2.4 `thm-primes-infinite` → 2.5 Quick check on the set of primes).
- **Motivation before a major definition.** `def-finite` and `def-equinumerous` are already motivated (25:7–9, 25:71); 2.5 adds the hook (the five points) at the opening and a weird-examples Quick check after `def-equinumerous`. The method boxes are motivated by a stalled direct attempt in each scratch work.

## 2. Section map

| § | File | Main now → budget (expected) | Changes |
|---|---|---|---|
| index | `index.md` | — | retitle; story; What you need; Time; Roadmap; Named moves; Threads; Summary; Terms (§4.0) |
| 2.1 | `01-naturals-and-well-ordering.md` | 4,136 → ≤ 5,000 (~4,450) | new subsection with box, scratch work, 2 examples, check; 1 more check; folds F2.1-a, b; B4 |
| 2.2 | `02-induction-in-practice.md` | 3,364 → ≤ 5,000 (~4,210) | retitle; smallest-counterexample subsection out; new subsection with box, scratch work, `exm-choosing-the-base`; gallery; 3 checks; B4 |
| 2.3 | `03-recursion.md` | 3,809 → ≤ 5,000 (~4,200) | back-references; fd1 recall; 4 checks; pointer fix |
| 2.4 | `04-contrapositive-and-contradiction.md` **new** | — → ≤ 4,500 (~3,500) | 2 boxes; `thm-primes-infinite`; `prp-cube-root-two-irrational`; moved subsection; 5 checks; A1, B1–B4, C1–C3 |
| 2.5 | `05-finite-sets.md` | 4,160 → ≤ 5,000 (~4,870) | hook opening; repair; `## Back to the pigeons`; box; scratch work; `exm-five-lattice-points`; contradiction at scale; 5 checks; folds F2.5-a…d; B4 |

## 3. Labels

**Kept, in place:** every label now in 21, 22, 23, 25.

**New:**
- 2.1: `exm-method-least-element`, `exm-no-infinite-descent`, `exm-least-element-down-by-two`, `exr-naturals-and-well-ordering-b4`.
- 2.2: `exm-method-induction-step`, `exm-choosing-the-base`, `exr-induction-in-practice-b4`.
- 2.4: `exm-method-choosing-the-form`, `exm-method-smallest-counterexample`, `exm-contrapositive-mod-three`, `thm-primes-infinite`, `prp-cube-root-two-irrational`, `exm-three-power-factor`, `exr-contrapositive-and-contradiction-a1`, `-b1`…`-b4`, `-c1`…`-c3`.
- 2.5: `exm-method-pigeonhole`, `exm-five-lattice-points`, `exr-finite-sets-b4`.

∛2 is new to the series: fd1 proves √2 and log₂ 9 irrational and mentions √3, √5, √6 (fd1 8.1, 8.6, 8.7), never a cube root.

---

## 4. Per-section plans

### 4.0 `index.md` (coordinator, last, against the delivered sections)

- **Title** `# Induction, Contradiction, and Finite Sets`.
- **Story, ix:3** kept with three edits: drop "that every integer is even or odd and not both" (Section 1.1 proved it); replace "when to argue from a smallest counterexample" by "when to argue by contrapositive, by contradiction or from a smallest counterexample"; append "It proves that there are infinitely many primes, and that ∛2 is irrational."
- **ix:5** (relations) is replaced by: "The second half of the chapter is about size. Section 1.1 left a puzzle waiting for a principle: five objects in four boxes put two in one box. *What does 'finite' mean, so that this can be proved?* The answer is a pairing: two sets have the same size when a bijection joins them, a set is finite when it pairs with {1, …, n}, and the pigeonhole principle becomes a theorem, with the facts about counting that the earlier chapters took on trust. The proofs of these facts are where proof by contradiction works at full scale." ix:5's relations text moves to the Chapter 4 index (§4.10).
- **What you need (ix:7).** Keep the fd1 part; add *Logic and Proof*, Section 8.1's three faces of "by contradiction" (@fd1:exm-rhetoric-contradiction, @fd1:prp-contrapositive-converse), De Morgan (@fd1:prp-de-morgan), Section 8.7 (@fd1:thm-irrational-power-rational) and @fd1:exm-strengthen-the-claim. The Chapter 1 list becomes: the method boxes (@exm-method-direct-proof, @exm-method-cases, @exm-method-counterexample); even, odd, divides and prime (@def-parity, @def-divides, @def-prime, @thm-even-or-odd, @exm-divides-combination, @exm-lattice-midpoint); sets cut out by a property, power sets, unions of families (as now); relations and functions, equality of functions, the empty function (@def-relation, @def-function, @prp-function-equality, @prp-empty-function); injections, surjections, composites, inverses (@def-injective, @def-surjective, @thm-composition-injective-surjective, @thm-bijection-iff-inverse, @thm-left-inverse-iff-injective); images and preimages (@def-image, @def-preimage).
- **Time.** "About 30 hours on the core track …; about 40 hours for everything" (layout §2), recomputed after S3 (§5).
- **Roadmap** (five bullets): 2.1 as now plus "and the least element as a tool of proof"; 2.2 "**Induction, strong induction and divisibility.** Induction from any integer, finding the inductive hypothesis inside the step and choosing the base, the division algorithm, lowest terms and prime factors, and a gallery of broken inductions, each located at one step."; 2.3 as now; 2.4 "**Contrapositive and contradiction in practice.** Choosing among a direct proof, the contrapositive and a contradiction; infinitely many primes; an irrational cube root by lowest terms; the smallest counterexample as a method; existence without a witness."; 2.5 = the old Chapter 3 index's first bullet, with "the pigeonhole principle" replaced by "the pigeonhole principle, which settles the five lattice points of Section 1.1,".
- **Named moves**: "The first five are method boxes." Then least element (2.1), finding the step (2.2), choosing the form (2.4), smallest counterexample (2.4; ix:22's text), pigeonhole (2.5), one line each with "(Section 2.k)"; then ix:23 "Prove more" and ix:24 "Recursion, then induction", kept. ix:25 moves to Chapter 4.
- **Threads**: four bullets as in §1, each naming where it is planted and paid, in prose.
- **Summary** (new, ≤ 180 words): induction and well-ordering are one principle (@thm-induction-iff-well-ordering); the division algorithm (@thm-division-algorithm); every integer ≥ 2 has a prime factor (@thm-prime-factor), and there are infinitely many primes (@thm-primes-infinite); recursion defines (@thm-recursion); ∛2 is irrational (@prp-cube-root-two-irrational); pigeonhole (@thm-pigeonhole), a finite set has one number of elements (@cor-finite-size-unique) and no proper copy (@thm-finite-no-proper-copy). "What is open: are ℚ and ℝ the same size as ℕ? Chapter 3."
- **Terms** (new): equinumerous, factorial, finite / has n elements, greatest element, infinite, least element, maximum / minimum, power, prime factor, quotient and remainder, smallest counterexample, sum and product, each with its label.

### 4.1 Section 2.1: The Natural Numbers and Well-Ordering (`21`)

Budget 4,136 → ≤ 5,000 (expected ~4,450). Folds ~520.

1. **21:36.** "in Section 2.5" → "in Section 4.2".
2. **New subsection `## The least element as a tool`**, inserted after the solution 21:192–194 and before 21:196.
   - **Lead** (~70): "Well-ordering is used in two ways. The proof of @thm-induction-iff-well-ordering below uses it to compare principles; most proofs use it as a tool. They name a set of natural numbers, take its least element, and use the one thing a least element offers: nothing in the set lies below it. Here is the halving question that opened the subsection on well-ordering, answered that way."
   - **`exm-no-infinite-descent`** `[No endless descent in ℕ]`: "Show that there is no function f: ℕ → ℕ with f(n + 1) < f(n) for every n ∈ ℕ."
   - **`[Scratch work]`** (≤ 16 lines): the goal is a negation, so suppose such an f and aim for a contradiction (¬I, face (i)). Which set has a least element worth having? The values V ≔ f(ℕ) = {f(n) : n ∈ ℕ}: a least value would be undercut by the next one.

     | Givens | Goal |
     |---|---|
     | f: ℕ → ℕ, f(n + 1) < f(n) for every n | a contradiction |
     | V ≔ f(ℕ) ⊆ ℕ, and f(0) ∈ V | a least element of V, and an element of V below it |
     | f(m) least in V (@thm-well-ordering) | f(m + 1) ∈ V and f(m + 1) < f(m): the gap is closed |

   - *Solution:* "Suppose f is such a function, and let V ≔ f(ℕ) (@def-image). Then V ⊆ ℕ, and V ≠ ∅ since f(0) ∈ V. By @thm-well-ordering, V has a least element, say f(m) with m ∈ ℕ. Now m + 1 ∈ ℕ by (ℕS), so f(m + 1) ∈ V, and f(m + 1) < f(m) by hypothesis, contradicting the choice of f(m). So no such f exists." Aftermath (≤ 50): repeated halving of a fraction p/q with both entries even, taking q > 0, would give such a function, n ↦ the (positive) denominator after n halvings, as long as the halving never stopped; so it stops. Section 2.2 writes this as a proof, the lemma on lowest terms (prose, no @: 2.1 cites nothing after itself).
   - **`exm-method-least-element`** `[Method: the least element]`.
     - **Template.** (1) Name a set S whose least element would help: the failures, the values, the candidates. (2) Show that S is a non-empty subset of ℕ, by giving an element, or a non-empty set of integers with an integer lower bound. (3) Take its least element m (@thm-well-ordering, @cor-well-ordering-integers). (4) Use leastness: produce an element of S below m, a contradiction; or conclude what m must be.
     - **When to use it.** A process that must stop; a quantity that can always be made smaller; the first time something happens; an object chosen to be extreme.
     - **The usual failure.** Taking "the least element" of a set not shown non-empty, or of a set of rationals or of integers with no integer lower bound (the warning above); and forgetting to check that the smaller element lies in S again.
   - **`exm-least-element-down-by-two`** `[Going down by two]`: "Let S ⊆ ℕ be non-empty, and suppose s − 2 ∈ S for every s ∈ S with s ≥ 2. Show that 0 ∈ S or 1 ∈ S." Idea (one line): by the method of @exm-method-least-element, ending in step (4)'s second form. *Solution:* "Let m be the least element of S (@thm-well-ordering). If m ≥ 2, then m − 2 ∈ S by hypothesis, and m − 2 < m, contradicting the choice of m. So m < 2, that is, m ≤ 1 by @lem-naturals-arithmetic (e); and m = 0 or m ≥ 1 by (a), so m ∈ {0, 1}. Hence 0 ∈ S or 1 ∈ S." (m − 2 ∈ ℕ needs no comment: the hypothesis puts it in S ⊆ ℕ.)
   - **Quick check:** "Let S ≔ {17 − 5k : k ∈ ℕ, 5k ≤ 17}. List S, find its least element, and say what that element has to do with dividing 17 by 5." *Solution:* S = {17, 12, 7, 2} (k = 0, 1, 2, 3; 5·4 = 20 > 17); least element 2, the remainder of 17 on division by 5 (17 = 5·3 + 2). Section 2.2 proves that this always works.
3. **Idea of `thm-induction-iff-well-ordering` (21:213).** After "the least element m of X ∖ S is then a smallest failure" insert "(the method of @exm-method-least-element, applied to the set X ∖ S of failures, with the least-element property of X in place of @thm-well-ordering)".
4. **Fold F2.1-a** `title="Each hypothesis has a job"`: 21:222–228 verbatim (the lead sentence, the three witnesses, and the paragraph on vacuous induction properties). In 21:230, "The first witness above shows" → "The first witness in the fold above shows".
5. **Fold F2.1-b** `title="Why the bound must be an integer"`: 21:252 verbatim.
6. **Quick check** after the proof of `cor-well-ordering-integers` (before F2.1-b): "Does {n ∈ ℤ : n² < 30} have a least element? Which hypothesis of @cor-well-ordering-integers do you check, and how?" *Solution:* Yes. The set is non-empty (0 is in it) and has the integer lower bound −6: an integer n ≤ −6 has n² ≥ 36. The least element is −5: 25 < 30, and −6 is not in the set.
7. **B4** `[B4: Prove or disprove]`.
   - (a) Every non-empty set of integers has a least element.
   - (b) Every non-empty set of negative rational numbers has a greatest element.
   - (c) Every non-empty set of even natural numbers has a least element.
   - (d) Every non-empty subset of {1/n : n ∈ ℤ_{>0}} has a greatest element.
   - (e) Every non-empty subset of {1/n : n ∈ ℤ_{>0}} has a least element.
   - (f) If S ⊆ ℤ is non-empty and s ≥ −13/3 for every s ∈ S, then S has a least element.
   - *Solution:* (a) False: ℤ itself; for every n ∈ ℤ, n − 1 ∈ ℤ and n − 1 < n. (b) False: {−1/n : n ∈ ℤ_{>0}}; for each −1/n in it, −1/(n + 1) is in it and −1/n < −1/(n + 1). (c) True: such a set is a non-empty subset of ℕ; @thm-well-ordering. (d) True: for non-empty T, N ≔ {n ∈ ℤ_{>0} : 1/n ∈ T} is a non-empty subset of ℕ; its least element n₀ gives 1/n₀ ∈ T, and 1/n ≤ 1/n₀ for every 1/n ∈ T, since n ≥ n₀ > 0. (e) False: the whole set; 1/(n + 1) < 1/n is again in it. (f) True: −5 is an integer lower bound, since −5 < −13/3 ≤ s; @cor-well-ordering-integers.

Count: +740 (subsection) + 20 + 70 − 370 (F2.1-a) − 150 (F2.1-b) ≈ 4,450. Checks: 5 on the main line.

### 4.2 Section 2.2: Induction, Strong Induction and Divisibility (`22`)

Budget 3,364 → ≤ 5,000 (expected ~4,150). No folds.

1. **Title (22:1)** `# Induction, Strong Induction and Divisibility` (layout §1; slug kept).
2. **22:3** becomes: "*Logic and Proof*, Chapter 4 gave the principle of induction (@fd1:ax-induction), its strong form (@fd1:thm-strong-induction), and the first worked proofs: a sum (@fd1:exm-sum-consecutive-products), an inequality (@fd1:exm-power-inequality), and a strong induction with three base cases (@fd1:exm-threes-and-fives). *Logic and Proof*, Chapter 8 showed how an induction is written in prose (@fd1:exm-rhetoric-induction). This section is about the craft: which form of induction fits a claim, where it starts, how to find the induction hypothesis inside the step, and how an induction goes wrong, each failure located at one step. On the way it proves two facts that *Logic and Proof* took from school: a fraction can be reduced until numerator and denominator are not both even, and every integer n ≥ 2 has a prime factor."
3. **22:69–84** (`## The smallest counterexample`, heading to the end of 22:84) are cut and go verbatim to 2.4 (§4.4 item 6).
4. **New subsection `## Finding P(n) inside P(n + 1)`**, at the place of the cut (after 22:67).
   - **Lead** (~80): "In every induction the step is an implication P(n) ⇒ P(n + 1), proved for an arbitrary n. The work is to find, inside the statement P(n + 1), the statement P(n), so that the hypothesis can be used: one more term to split off, one more factor to take out, one more case to bound. The first example is about divisibility (@def-divides)."
   - **`[Scratch work]`** (≤ 16 lines), for the claim 7 | 9ⁿ − 2ⁿ (n ∈ ℕ), powers in their school meaning: write P(n + 1) out and look for 9ⁿ − 2ⁿ in it. The first try, 9·9ⁿ − 2·2ⁿ, has two different factors in front; take 9 out of both and pay back what that costs, 7·2ⁿ.

     | Givens | Goal |
     |---|---|
     | P(n): 9ⁿ − 2ⁿ = 7k with k ∈ ℤ | P(n + 1): 9ⁿ⁺¹ − 2ⁿ⁺¹ = 7m for some m ∈ ℤ |
     | 9ⁿ⁺¹ = 9·9ⁿ, 2ⁿ⁺¹ = 2·2ⁿ (school meaning) | 9ⁿ⁺¹ − 2ⁿ⁺¹ rewritten so that 9ⁿ − 2ⁿ appears |
     | 9ⁿ⁺¹ − 2ⁿ⁺¹ = 9(9ⁿ − 2ⁿ) + 7·2ⁿ = 7(9k + 2ⁿ) | m ≔ 9k + 2ⁿ ∈ ℤ: the gap is closed |

   - Then **22:94–98 rewritten** (not moved verbatim; S2): "Divisibility claims about powers are a staple of induction, because the step can usually be arranged to contain the old expression once. Here is the proof the scratch work found. *Claim:* 7 | 9ⁿ − 2ⁿ for every n ∈ ℕ, with 9ⁿ and 2ⁿ in their school meaning (a⁰ = 1, aⁿ⁺¹ = aⁿ·a, and aⁿ is an integer for an integer a; Section 2.3 makes this a definition). *Base case:* 9⁰ − 2⁰ = 0 = 7·0. *Step:* if 9ⁿ − 2ⁿ = 7k with k ∈ ℤ, then" display "9ⁿ⁺¹ − 2ⁿ⁺¹ = 9(9ⁿ − 2ⁿ) + 7·2ⁿ = 7(9k + 2ⁿ)," "and 9k + 2ⁿ ∈ ℤ. By @fd1:ax-induction, the claim holds for every n ∈ ℕ." No "For instance": the scratch work has already done the computation.
   - **`exm-method-induction-step`** `[Method: finding P(n) inside P(n + 1)]`.
     - **Template.** (1) Write P(n + 1) out in full. (2) Find P(n) inside it: split off the last term, take out one factor, or separate the new piece from the old. (3) Apply the induction hypothesis to the old part. (4) Close the rest by computation. (5) Choose the base: the first n from which steps (2)–(4) work, with any smaller n the claim covers checked directly.
     - **When to use it.** P(n + 1) is built from P(n) by one operation: a term added, a factor multiplied, an element added to a set.
     - **The usual failure.** Starting from P(n + 1) and deriving something true, which proves the converse (N5); a step that works only from some n on, with the base set lower (as in the gallery below); using P(n + 1) inside its own step (N9).
   - **Quick check:** "For a proof that 5 | 9ⁿ − 4ⁿ for every n ∈ ℕ, write 9ⁿ⁺¹ − 4ⁿ⁺¹ so that 9ⁿ − 4ⁿ appears." *Solution:* 9ⁿ⁺¹ − 4ⁿ⁺¹ = 9(9ⁿ − 4ⁿ) + 5·4ⁿ; if 9ⁿ − 4ⁿ = 5k, this is 5(9k + 4ⁿ).
   - **`exm-choosing-the-base`** `[Where the step starts working]`: "Prove that 3ⁿ ≥ n³ for every n ∈ ℕ." Idea (two lines, citing the box): P(n + 1) contains 3ⁿ as 3·3ⁿ ≥ 3n³, so the step needs 3n³ ≥ (n + 1)³, which holds from n = 3 on; the base is 3, and 0, 1, 2 are checked directly. *Solution:* "*Small cases.* 3⁰ = 1 ≥ 0, 3¹ = 3 ≥ 1, 3² = 9 ≥ 8. *From 3 on,* by @thm-induction with base 3. Base: 3³ = 27 ≥ 27. Step: let n ≥ 3 with 3ⁿ ≥ n³. Then 3ⁿ⁺¹ = 3·3ⁿ ≥ 3n³, and 3n³ ≥ (n + 1)³ = n³ + 3n² + 3n + 1, because 2n³ ≥ 6n² = 3n² + 3n² ≥ 3n² + 9n ≥ 3n² + 3n + 1 for n ≥ 3. So 3ⁿ⁺¹ ≥ (n + 1)³." Aftermath (≤ 50): the claim is true at 0, 1 and 2, but the argument of the step fails from 2 to 3 (3·2³ = 24 < 27 = 3³); the base is where the step starts working, not where the claim starts being true, and the cases below it are checked one by one.
   - **Quick check:** "For which n ∈ ℕ is 3n³ ≥ (n + 1)³ false, and why does that make 3 the base although 3ⁿ ≥ n³ holds at 0, 1 and 2?" *Solution:* n = 0, 1, 2 (0 < 1, 3 < 8, 24 < 27). The step is proved only from 3 on, so the three smaller cases need their own checks; an induction from base 0 would have three unproved transitions.
5. **22:88** "The first uses of the method are about divisibility." → "The next results are about divisibility."
6. **22:142**, first sentence ("This is the school fact … now proved.") becomes: "Section 1.1 proved this by induction (@thm-even-or-odd); here it falls out of the division algorithm with n = 2. *Logic and Proof* used it in Argument A of Chapter 1 and in the proof of @fd1:thm-square-even-implies-even." The rest of 22:142 is kept.
7. **22:150**, last sentence ("Here is that reason as a proof, written in the steps of the smallest-counterexample method, each step named.") becomes the one-line pointer: "Here is that reason as a proof. It supposes the claim fails, takes the least failure and derives a contradiction: a proof by **smallest counterexample**, the method of @exm-method-least-element applied to the set of failures. Section 2.4 makes it a method of its own; here its steps are named as they occur." The term stays defined in 2.2, so 22 A1, B2, C3 and 23 C1's "smallest counterexample of Section 2.2" read correctly.
8. **22:178.** Delete the sentence "Two of the proof's steps adapt those of the smallest-counterexample method above: … is the smaller failure \( m' \)." The rest of 22:178 is kept.
9. **Gallery (22:204–254).** Heading `## A gallery of broken inductions`. 22:206 gains a last sentence: "Each entry below names the part that breaks." After 22:246 add:
   **The step run backwards.** (~110) "Claim: n² ≥ 2n for every n ≥ 2. 'Step: (n + 1)² ≥ 2(n + 1) gives n² + 2n + 1 ≥ 2n + 2, so n² ≥ 1, which is true.' This starts from P(n + 1) and ends at a true statement, so it shows only that P(n + 1) implies something true, which every statement does (N5). Here each line can be reversed, and written forwards (n² ≥ 1, so (n + 1)² = n² + 2n + 1 ≥ 2n + 2) it is a valid step, though one that never uses P(n). In general a backward chain cannot be reversed: from the false 1 = −1, squaring gives the true 1 = 1."
10. **Quick check** after the warning 22:252–254: "A proof that n² ≤ 2ⁿ for every n ≥ 4 checks n = 4 and proves the step 2n² ≥ (n + 1)² for n ≥ 3. Is it complete? A second proof of 'n² ≤ 2ⁿ for every n ∈ ℕ' uses base 0 and the same step. Which entry of the gallery does it commit?" *Solution:* The first is complete: 16 ≤ 16, and the step is proved for every n ≥ 4. The second has a true base but a step proved only from 3 on, so the transitions 0 → 1, 1 → 2, 2 → 3 are unproved: a step valid only from some point on, as in @exm-all-equal-induction. Its conclusion is false at 3 (9 > 8). This is *Logic and Proof*, Chapter 4's warning about 2ⁿ ≥ n² (named at 22:241), made precise at the level of the step.
11. **22:272** (A1 (a)(i) solution): "the step factors out one copy of 7, as in the example 3 | 4ⁿ − 1 in the subsection on divisibility" → "the step takes out one factor 7 and leaves a multiple of 6, as in the example 7 | 9ⁿ − 2ⁿ in the subsection on finding the step".
12. **B4** `[B4: Prove or disprove]`.
    - (a) 3 | 2²ⁿ⁺¹ + 1 for every n ∈ ℕ.
    - (b) 2ⁿ ≥ n³ for every integer n ≥ 9.
    - (c) 1 + 4 + 7 + ⋯ + (3n + 1) = (n + 1)(3n + 2)/2 for every n ∈ ℕ.
    - (d) Every integer n ≥ 10 is 3a + 7b for some integers a, b ≥ 0.
    - (e) 5ⁿ ≥ 4ⁿ + 3ⁿ for every integer n ≥ 2.
    - (f) n² + 1 is prime for every even integer n ≥ 2.
    - *Solution:* (a) True. 2¹ + 1 = 3; if 2²ⁿ⁺¹ + 1 = 3k, then 2²ⁿ⁺³ + 1 = 4(2²ⁿ⁺¹ + 1) − 3 = 3(4k − 1). (b) False: n = 9, 2⁹ = 512 < 729 = 9³. (It holds from 10 on: 1024 ≥ 1000, and 2(n³) ≥ (n + 1)³ for n ≥ 10; the claim fails only at its base.) (c) True. n = 0: 1 = 1·2/2. Step: split off the last term, (n + 1)(3n + 2)/2 + (3n + 4) = (3n² + 11n + 10)/2 = (n + 2)(3n + 5)/2. (d) False: 11. With b = 0, 1 the remainder 11 − 7b is 11 or 4, neither a multiple of 3 (11 = 3·3 + 2, 4 = 3·1 + 1, uniqueness in @thm-division-algorithm), and b ≥ 2 makes it negative. (e) True, by @thm-induction with base 2: 25 ≥ 16 + 9; if 5ⁿ ≥ 4ⁿ + 3ⁿ, then 5ⁿ⁺¹ = 5·5ⁿ ≥ 5·4ⁿ + 5·3ⁿ ≥ 4·4ⁿ + 3·3ⁿ = 4ⁿ⁺¹ + 3ⁿ⁺¹. (It fails at n = 1: 5 < 7, and at 0: 1 < 2.) (f) False: n = 8 gives 65 = 5·13, with the positive divisor 5 ∉ {1, 65}. For n = 2, 4, 6 the values 5, 17, 37 are prime: three successes, then a failure (N1).
13. **Idea of `thm-division-algorithm` (22:116)**, after "take the **least**." append "(the method of @exm-method-least-element: S the non-negative integers a − qn)". Fading, Idea level (§1).
14. **22:308** (B2 solution): "the blank is its last step, *produce a contradiction*" → "the blank is the contradiction: a smaller failure is impossible, as in the proof of @lem-lowest-terms", so that 2.2 reads without 2.4's list.
15. **22 B1** (`exr-induction-in-practice-b1`, label kept; S2: 5 | 6ⁿ − 1 is Cummings's Exercise 4.3 (f)). Statement: "Prove that 3 | n³ + 2n for every n ∈ ℕ." *Solution:* P(n): n³ + 2n = 3k with k ∈ ℤ. Base: 0 = 3·0. Step: (n + 1)³ + 2(n + 1) = (n³ + 2n) + 3(n² + n + 1) = 3(k + n² + n + 1). By @fd1:ax-induction the claim holds for every n. (The old part plus a new piece, as in the box, without powers.) Sidecar `exr-induction-in-practice-b1.py` rewritten; ledger line 22:447 replaced by "(n + 1)³ expanded | R arithmetic, school fact".

Count: −267 (cut) + 80 + 170 (scratch) + 40 (22:94–98 rewritten, net) + 130 (box) + 70 (check) + 260 (`exm-choosing-the-base`) + 80 (check) + 30 (pointer net) + 120 (gallery) + 100 (check) ≈ 4,210. Checks: 4 on the main line.

### 4.3 Section 2.3: Definition by Recursion (`23`)

Budget 3,809 → ≤ 5,000 (expected ~4,200). No folds. Idea level: no box, no B4.

1. **Quick check** after the remark 23:95–97: "Name X, a and g for the sequence 1, 3, 7, 15, …, in which each term is twice the previous one plus one." *Solution:* X = ℕ (or ℝ), a = 1, g(n, x) = 2x + 1; g is a function ℕ × X → X, so @thm-recursion applies.
2. **Quick check** after the proof of `cor-two-step-recursion` (before 23:155): "Do a₀ = 1, a₁ = 1 and a_{n+2} = a_{n+1}·a_n define a sequence of reals? What is it?" *Solution:* Yes, by @cor-two-step-recursion with h(n, x, y) = yx; every term is 1, by induction on the pair statement "a_n = 1 and a_{n+1} = 1", as in the two-step example below.
3. **23:226**, append: "In the terms of @exm-method-induction-step, the recursion says where P(n) sits inside P(n + 1): in the last term split off, or the last factor."
4. **Idea of `thm-bernoulli` (23:311–313)**, append: "(the method of @exm-method-induction-step: (1 + x)ⁿ is the first factor of (1 + x)ⁿ⁺¹)".
5. **Quick check** after 23:326: "Check Bernoulli's inequality at x = −1/2, n = 3, and say which line of the proof uses x ≥ −1." *Solution:* (1/2)³ = 1/8 ≥ 1 − 3/2 = −1/2. The line "since x ≥ −1, we have 1 + x ≥ 0", which keeps the direction of the inequality when it is multiplied by 1 + x.
6. **23:356**: "what 'finite' will mean in Chapter 3" → "what 'finite' means in Section 2.5".
7. **23:360**, append: "*Logic and Proof* met this cure (@fd1:exm-strengthen-the-claim) with a sum that telescopes; here the sum does not telescope, and the stronger claim has to be guessed."
8. **Quick check** after 23:384: "Would 'S_n ≤ 2 − 1/(n + 1)' also carry its own step?" *Solution:* No. Its step needs 1/(n + 1)² ≤ 1/(n + 1) − 1/(n + 2) = 1/((n + 1)(n + 2)), that is, (n + 1)(n + 2) ≤ (n + 1)², which is false. A stronger claim works only if its margin pays for the next term; this margin is too small.

Count: +4 checks (~330) + 70 ≈ 4,210. Checks: 5.

### 4.4 Section 2.4: Contrapositive and Contradiction in Practice (`04-contrapositive-and-contradiction.md`, new)

Budget ≤ 4,500 (expected ~3,500). No folds. Five Quick checks, one warning, one Looking-ahead box.

**Opening (~150).** "Section 1.1 proved statements straight from their definitions, and Section 1.2 met the first contradiction about sets. *Logic and Proof*, Section 8.1 sorted the arguments called 'by contradiction' into three faces: refuting a statement (¬I), proving the contrapositive, and genuine reductio (RAA), with the rule 'use the weakest form that works, and say which one you use'. This section is about choosing. Which form a proof takes is decided by the shape of the claim and by what each assumption hands over to compute with. The section proves that there are infinitely many primes and that ∛2 is irrational, makes the smallest counterexample of Section 2.2 a method of its own, and ends with existence proofs that name no witness."

**`## Choosing the form` (~850).**
1. Lead (~100): to prove "if P, then Q" there are three starts: assume P (direct; @exm-method-direct-proof); assume ¬Q and reach ¬P (contrapositive; @fd1:prp-contrapositive-converse); assume P and ¬Q and reach a contradiction. A negative claim (irrational, no solution, no bijection) is proved by face (i): assume the positive statement, reach ⊥, conclude by ¬I. The choice is made by unwinding each candidate assumption and asking which hands over something to compute with.
2. **`exm-contrapositive-mod-three`** `[A negative hypothesis]`: "Let n ∈ ℤ. Show that if n² + n + 1 is not divisible by 3, then n leaves remainder 0 or 2 on division by 3."
   - **`[Scratch work]`** (≤ 18 lines). Direct: the hypothesis "3 ∤ n² + n + 1" says that no k has n² + n + 1 = 3k: a "there is no", with nothing to compute with. Contrapositive: the negation of "remainder 0 or remainder 2" is "remainder not 0 and not 2" (@fd1:prp-de-morgan), that is, remainder 1, since the remainder lies in {0, 1, 2} and is unique (@thm-division-algorithm). So assume n = 3q + 1: an equation to compute with; and the new goal 3 | n² + n + 1 asks for a witness.

     | Givens | Goal |
     |---|---|
     | 3 ∤ n² + n + 1 | remainder of n is 0 or 2 |
     | (contrapositive) n = 3q + 1, q ∈ ℤ | 3 \| n² + n + 1 |
     | n² + n + 1 = 9q² + 9q + 3 | n² + n + 1 = 3m: m = 3q² + 3q + 1, the gap is closed |

   - *Solution:* "We prove the contrapositive: if n does not leave remainder 0 or 2 on division by 3, then 3 | n² + n + 1. Divide n by 3 (@thm-division-algorithm): n = 3q + r with q ∈ ℤ and r ∈ {0, 1, 2}, r unique. By assumption r ≠ 0 and r ≠ 2, so r = 1. Then n² + n + 1 = (9q² + 6q + 1) + (3q + 1) + 1 = 9q² + 9q + 3 = 3(3q² + 3q + 1), so 3 | n² + n + 1." Aftermath (one sentence): the contrapositive turned a "not divisible" in the hypothesis into a witness to produce, and an "or" in the conclusion into a single case to compute with.
3. **Quick check:** "Write the contrapositive and the negation of the statement of @exm-contrapositive-mod-three. Which one is equivalent to it?" *Solution:* Contrapositive: "if n leaves remainder 1 on division by 3, then 3 | n² + n + 1", equivalent. Negation: "there is an integer n with 3 ∤ n² + n + 1 that leaves remainder 1", not equivalent, and false by the example.
4. **`exm-method-choosing-the-form`** `[Method: choosing direct, contrapositive or contradiction]`.
   - **Template.** Unwind P, Q, ¬P and ¬Q by their definitions. If P gives something to compute towards Q, go direct. If ¬Q gives an equation, a case split or an object, and ¬P is a statement you can reach, prove the contrapositive and announce it ("We prove the contrapositive"). If the claim is a negation (irrational, no solution, no bijection, no largest), assume the positive statement and derive a contradiction (¬I). Otherwise assume P and ¬Q together, and use both.
   - **When to use it.** Before every proof; at once when the direct attempt stalls, or the conclusion is "or", "not", "no" or "infinitely many".
   - **The usual failure.** A wrong negation (the negation of "A or B" is "not A and not B", @fd1:prp-de-morgan); a "contradiction" that never uses its assumption ¬Q, a direct proof in costume (@fd1:exm-costume-direct; for the contrapositive, @fd1:exm-costume-contrapositive); not saying which form is used.
5. **Quick check:** "Which form, and what first sentence, for: (a) for x ∈ ℝ, if x² ≠ x, then x ≠ 1; (b) there is no integer n with n² = 2; (c) for f: X → Y and g: Y → Z, if g ∘ f is injective, then f is injective?" *Solution:* (a) Contrapositive: "Suppose x = 1; then x² = 1 = x." (b) Face (i): "Suppose n ∈ ℤ and n² = 2." (Then |n| ≤ 1 gives n² ≤ 1 and |n| ≥ 2 gives n² ≥ 4.) (c) Direct, by the method of @exm-method-injectivity: "Let f(x₁) = f(x₂)."

**`## Infinitely many primes` (~580).**
1. Lead (~80): @thm-prime-factor gives every integer ≥ 2 a prime factor. To show that the primes never run out, build, for each n, a number all of whose prime factors exceed n.
2. **`thm-primes-infinite`** `[There Are Infinitely Many Primes]`: "For every n ∈ ℕ there is a prime p with p > n."
3. **Idea** (≤ 5 lines): n! + 1 leaves remainder 1 on division by every k with 2 ≤ k ≤ n; so none of them divides it, and its prime factor (@thm-prime-factor) must exceed n. The last step is a face (i) argument inside the proof: suppose p ≤ n.
4. **Proof.** "*Step 1.* For every n ∈ ℕ, n! is a positive integer and k | n! for every k ∈ {1, …, n}. By induction on n, following the clauses of n! (@def-sum-product): 0! = 1, and there is no k. If the claim holds for n, then (n + 1)! = n!·(n + 1) is a positive integer; for k ≤ n, n! = kj with j ∈ ℤ gives (n + 1)! = k·(j(n + 1)); and (n + 1)! = n!·(n + 1) for k = n + 1. Every k ∈ {1, …, n + 1} is k ≤ n or k = n + 1 (@lem-naturals-arithmetic (e)).
   *Step 2.* Let n ∈ ℕ, and N ≔ n! + 1. By Step 1, N ≥ 2, so N has a prime factor p (@thm-prime-factor). Suppose p ≤ n. Then p ∈ {1, …, n}, since p ≥ 2, so p | n! by Step 1. From p | N and p | n!, p | N − n! = 1 (@exm-divides-combination). So 1 = kp with k ∈ ℤ; then k > 0, k ≥ 1, and p ≤ kp = 1, against p ≥ 2. Hence p > n (trichotomy). This proves the theorem."
5. **Warning** `**The proof does not say that n! + 1 is prime.**` "For n = 4, n! + 1 = 25 = 5·5. The proof uses only that n! + 1 has some prime factor, and shows that every one of them exceeds n."
6. **Quick check:** "Run the proof at n = 5: compute N and a prime p > 5 dividing it. Is N prime?" *Solution:* N = 121 = 11·11, p = 11 > 5; N is not prime.
7. **Looking ahead** (`::: {.remark}` `[Looking ahead]`, the section's only forward pointer): "Section 2.5 defines infinite sets; with that definition, the set of primes is infinite."

**`## An irrational number by lowest terms` (~500).**
1. Lead (~60): *Logic and Proof* proved √2 irrational with the fact (L), which @lem-lowest-terms now proves. The same lemma settles a cube root. Here ∛2 is the real number x with x³ = 2 (its existence and uniqueness are school facts, as in Section 1.6).
2. **`prp-cube-root-two-irrational`** `[The Cube Root of 2 Is Irrational]`: "∛2 is irrational."
3. **Idea** (≤ 5 lines): the claim is a negation, so face (i): suppose ∛2 = p/q in the form of @lem-lowest-terms, and show that p and q are both even. One step, "p³ even ⇒ p even", is itself a contrapositive.
4. **Proof.** "*A contrapositive first.* For p ∈ ℤ, if p³ is even, then p is even. Suppose p is not even; then p is odd (@thm-even-or-odd), p = 2k + 1, and p³ = 8k³ + 12k² + 6k + 1 = 2(4k³ + 6k² + 3k) + 1 is odd, hence not even (@thm-even-or-odd).
   *The claim.* Suppose ∛2 is rational. By @lem-lowest-terms, ∛2 = p/q with p ∈ ℤ, q ∈ ℤ_{>0}, p and q not both even. Cubing, p³ = 2q³, so p³ is even and p is even: p = 2s with s ∈ ℤ. Then 8s³ = 2q³, so q³ = 4s³ = 2(2s³) is even, and q is even. So p and q are both even, a contradiction. Hence ∛2 is irrational (¬I)."
5. Aftermath (~60): face (i), no RAA; the contrapositive step is face (ii), whose conclusion "p even" is not a negation, so it rests on @fd1:prp-contrapositive-converse. The lemma's "not both even" is the given that the contradiction breaks.
6. **Quick check:** "Why does the same proof not show that ∛3 is irrational?" *Solution:* p³ = 3q³ gives no parity contradiction: with q odd, p³ is odd and p is odd, and "not both even" survives. The proof needs "no common divisor 3", which Exercise C2 of Section 2.2 provides.

**`## The smallest counterexample` (moved, + ~470).**
1. **22:69–84 verbatim**: the heading, 22:71, the algorithm block 22:73–82, and 22:84.
2. One added sentence after 22:84: "Section 2.2 used it twice, in @lem-lowest-terms and in the proof sketched before @thm-prime-factor."
3. **`exm-method-smallest-counterexample`** `[Method: the smallest counterexample]`.
   - **Template.** The four steps of the list above (not restated), opening with "Suppose not, and let m be the least integer ≥ n₀ for which P(m) fails"; the least failure is @exm-method-least-element applied to the set of failures. Worked examples: @lem-lowest-terms (Section 2.2) and @exm-three-power-factor below.
   - **When to use it.** A failure would give a smaller failure: a number with a factor, a fraction that can be reduced, a representation that can be shortened.
   - **The usual failure.** Not checking that the smaller object is still ≥ n₀ (or positive), so that it lies in the set of failures; and forgetting the case in which no smaller object exists, which must be ruled out directly (here, m not divisible by 3).
4. **`exm-three-power-factor`** `[Taking out the threes]`: "Show that every positive integer n is 3ᵃ·b with a ∈ ℕ, b ∈ ℤ and 3 ∤ b."
   - **`[Scratch work]`** (≤ 14 lines): a failure m divisible by 3 gives m/3, which is smaller; a failure not divisible by 3 is not a failure at all.

     | Givens | Goal |
     |---|---|
     | m least positive integer with no form 3ᵃb, 3 ∤ b; every k with 1 ≤ k < m has one | a contradiction |
     | case 3 ∤ m | m = 3⁰·m: m has the form after all |
     | case m = 3m′: 1 ≤ m′ < m, m′ = 3ᵃb with 3 ∤ b | m = 3ᵃ⁺¹b: m has the form; the gap is closed |

   - *Solution:* "Suppose not, and let F be the set of positive integers with no such form. F is a non-empty subset of ℕ, so it has a least element m (@thm-well-ordering). If 3 ∤ m, then m = 3⁰·m with 3 ∤ m, so m ∉ F, a contradiction. So m = 3m′ with m′ ∈ ℤ; m′ > 0 since m > 0, and m′ < 3m′ = m. As m is least in F, m′ ∉ F: m′ = 3ᵃb with a ∈ ℕ and 3 ∤ b. Then m = 3ᵃ⁺¹b (@def-power), so m ∉ F, a contradiction. Hence F = ∅."
5. **Quick check:** "Write 54 and 45 in the form of @exm-three-power-factor, and say why m′ ∉ F in the proof." *Solution:* 54 = 3³·2, 45 = 3²·5. m′ is a positive integer smaller than the least element of F.

**`## Existence without a witness` (~220).** A proof of "there exists" by contradiction (RAA on ∃) may name no object. @thm-well-ordering was proved so, and 21:174 said what that means. *Logic and Proof*, Section 8.7 gave the classical example (@fd1:thm-irrational-power-rational) and the book's position: classical rules are allowed, and a proof that names no witness is still a proof. Contrast with this section: the proof of @thm-primes-infinite names its witness (a prime factor of n! + 1, the least one found by trial division), and the contrapositive of @exm-contrapositive-mod-three hands over the witness m. When a witness is cheap, name it.

**Exercises (2.4).**
- **A1** (four parts, one folded solution).
  - (a) Write the converse, the contrapositive and the negation of "if n is prime and n ≥ 3, then n is odd". Which are true?
  - (b) Name the form you would choose and write the first sentence (no proofs): (i) ∛3 is irrational; (ii) for a, b ∈ ℤ, if a² + b² is odd, then a is even or b is even; (iii) for sets A, B, if A ∪ B = A ∩ B, then A = B.
  - (c) Run the proof of @thm-primes-infinite at n = 6: find N, its least prime factor, and check that it exceeds 6.
  - (d) "Suppose p is the largest prime. Then p! + 1 has a prime factor q > p, a contradiction." Which face of "by contradiction" is this, and does the proof name a prime larger than p?
  - *Solution:* (a) Converse: if n is odd, then n is prime and n ≥ 3 (false: 9 = 3·3). Contrapositive: if n is even, then n is not prime or n < 3 (equivalent to the statement; true: an even n ≥ 3 has the divisor 2 ∉ {1, n}). Negation: some prime n ≥ 3 is even (false). "Not odd" is "even" by @thm-even-or-odd. (b) (i) Face (i): "Suppose ∛3 = p/q with p ∈ ℤ, q ∈ ℤ_{>0} and no common divisor d ≥ 2" (Exercise C2 of Section 2.2; "not both even" is not enough, as the last Quick check of the section shows). (ii) Contrapositive: "Suppose a and b are both odd" (the negation of "a even or b even", @fd1:prp-de-morgan and @thm-even-or-odd); then a² and b² are odd (@fd1:thm-odd-iff-square-odd) and a² + b² is even (@exm-parity-of-sums). (iii) Direct, by @exm-method-double-inclusion. (c) 6! + 1 = 721. Not divisible by 2, 3, 5 (721 = 2·360 + 1 = 3·240 + 1 = 5·144 + 1); 721 = 7·103. Least prime factor 7 > 6, and 721 is not prime. (d) Face (i): it refutes "there is a largest prime". Its body names q, so it can be rewritten without contradiction: for every prime p, a prime factor of p! + 1 is a larger prime (@thm-primes-infinite with n = p).
- **B1** `[B1: Contrapositive]`. Prove: (a) for all a, b ∈ ℤ, if 3 ∤ a + b, then 3 ∤ a or 3 ∤ b; (b) for every x ∈ ℝ, if x² > 2x + 8, then x > 4 or x < −2. *Solution:* (a) We prove the contrapositive: if 3 | a and 3 | b, then 3 | a + b (the negation of "3 ∤ a or 3 ∤ b" by @fd1:prp-de-morgan). With a = 3k and b = 3l, a + b = 3(k + l) (@exm-divides-combination). (b) Contrapositive: suppose x ≤ 4 and x ≥ −2 (@fd1:prp-de-morgan, with trichotomy). Then x − 4 ≤ 0 and x + 2 ≥ 0, so x² − 2x − 8 = (x − 4)(x + 2) ≤ 0, that is, x² ≤ 2x + 8.
- **B2** `[B2: Contradiction]`. Prove: (a) there is no rational number r with r² = r + 1; (b) there are no integers m, n with m² − 8n = 5. *Solution:* (a) Suppose r² = r + 1 with r = p/q as in @lem-lowest-terms. Then p² = pq + q². Products: odd·odd is odd, (2k + 1)(2l + 1) = 2(2kl + k + l) + 1, and an even number times any integer is even. Three cases remain. p, q odd: p² odd, pq + q² = odd + odd, even (@exm-parity-of-sums). p even, q odd: p² even, pq + q² = even + odd, odd. p odd, q even: p² odd, pq + q² even. Each case equates an odd and an even integer, against @thm-even-or-odd. (b) Suppose m² = 8n + 5 = 2(4n + 2) + 1. Then m² is odd, so m is odd (@fd1:thm-odd-iff-square-odd), and m² = 8t + 1 with t ∈ ℤ by @exr-induction-in-practice-b3 (b). So 8(t − n) = 4, and 2(t − n) = 1: 1 would be even, against @thm-even-or-odd.
- **B3** `[B3: Name the move, then complete it]`. "Claim: n < 2ⁿ for every integer n ≥ 1. Suppose not. Then the set F of integers n ≥ 1 with n ≥ 2ⁿ is non-empty and has the integer lower bound 1, so it has a least element m (@cor-well-ordering-integers). Since 1 < 2 = 2¹, m ≠ 1, so m ≥ 2, and m − 1 is an integer with 1 ≤ m − 1 < m. ⋮" *Solution:* The move is the smallest counterexample; the blank is its last step. As m − 1 < m, m − 1 ∉ F: m − 1 < 2^{m−1}. Since 2^{m−1} ∈ ℕ (@prp-power-laws (d)), discreteness gives m ≤ 2^{m−1}, and 2^{m−1} < 2^{m−1}·2 = 2^m (@def-power, with m − 1 ∈ ℕ, and 2^{m−1} > 0 by @prp-power-laws (e)). So m < 2^m, that is, m ∉ F, a contradiction.
- **B4** `[B4: Prove or disprove]`. "Prove each true statement; refute each false one with a concrete counterexample." (STYLE §12.13.4 as written; every item is a universal statement.)
  - (a) For every n ∈ ℤ: if n² − 1 is not divisible by 5, then n is divisible by 5.
  - (b) For every n ∈ ℤ: if 4 ∤ n², then n is odd.
  - (c) For every x ∈ ℝ: if x is irrational, then x² is irrational.
  - (d) For every x ∈ ℝ: if x² is irrational, then x is irrational.
  - (e) For all positive integers a, b: a² − b² ≠ 10.
  - (f) For every n ∈ ℕ there is a prime p with n < p ≤ n + 6.
  - *Solution:* (a) False: n = 2; n² − 1 = 3 is not divisible by 5, and neither is 2. (b) True. Contrapositive: if n is not odd, it is even (@thm-even-or-odd), n = 2k, and n² = 4k², so 4 | n². (Its look-alike "if 4 | n², then 4 | n" is false at n = 2.) (c) False: x = √2 (@fd1:thm-sqrt2-irrational), x² = 2. (d) True. Contrapositive: if x = p/q is rational, so is x² = p²/q². (e) True, by contradiction (face (i)). Suppose a² − b² = (a − b)(a + b) = 10. The two factors differ by 2b, so they have the same parity (if one were even and the other odd, their difference would be odd). Both odd: the product is odd, but 10 is even. Both even: 4 divides the product, but 10 = 4·2 + 2 (uniqueness in @thm-division-algorithm). Verdicts: three true ((b), (d), (e)), three false. (f) False: n = 89. The numbers 90, …, 95 are not prime: 90, 92, 94 are even, 91 = 7·13, 93 = 3·31, 95 = 5·19. (89 is the smallest counterexample.)
- **C1** `[C1: Two proofs by contradiction]`. "*Proof A.* Claim: if n ∈ ℤ is odd, then n² + n is even. 'Suppose n is odd and n² + n is odd. Write n = 2k + 1. Then n² + n = (2k + 1)(2k + 2) = 2(2k + 1)(k + 1) is even, which contradicts n² + n odd.' *Proof B.* Claim: for every n ∈ ℤ, if n² ≥ 10, then n ≥ 4 or n ≤ −4. '(1) Suppose n² ≥ 10. (2) Suppose, for a contradiction, that n < 4 or n > −4. (3) Say n < 4, so n ≤ 3. (4) If also n ≥ −3, then n² ≤ 9 < 10; so n ≤ −4. (5) So n ≤ −4, which proves the claim.' For each: is the conclusion true? Is the argument valid? Name each flaw, and write a proof in the form the method box recommends."
  - *Solution:* A: the conclusion is true and the argument valid, but the assumption "n² + n odd" is used only to clash with the result: a direct proof in costume (@fd1:exm-costume-direct). Write it directly ("Let n = 2k + 1; then n² + n = 2(2k + 1)(k + 1)"). The hypothesis is not even needed: n² + n = n(n + 1), and one of n, n + 1 is even. B: the conclusion is true; the argument is not a proof. (2) negates "n ≥ 4 or n ≤ −4" wrongly (N11): the negation is "n < 4 and n > −4" (@fd1:prp-de-morgan). (3) takes one disjunct and drops the other, a missing case (N7). (5) reaches no contradiction at all. A proof: by the contrapositive, if n < 4 and n > −4, then −3 ≤ n ≤ 3 (@prp-integers-closed (c)), so |n| ≤ 3 and n² ≤ 9 < 10. Or by cases: n ≥ 4, done; n ≤ 3, then n ≤ −4 by (4)'s computation. (The entries are those of @fd1:exm-not-allowed-catalogue.)
  - *Marking scheme* (10): A judged valid, with the unused assumption named, 2; A rewritten directly, 1; B's wrong negation (N11) named with the correct one, 3; the missing case (N7), 1; the absence of a contradiction, 1; a correct proof of B, 2.
- **C2** `[C2: Euclid's list]`. "(a) Let k ≥ 1 and let p₁, …, p_k be primes. Prove that P ≔ p₁p₂⋯p_k + 1 has a prime factor different from each pᵢ. (b) Compute P and its prime factors for the lists 3, 5 and 2, 7. Is P prime?" *Solution:* (a) Each pᵢ ≥ 2, so p₁⋯p_k ≥ 2 and P ≥ 3; P has a prime factor p (@thm-prime-factor). Suppose p = pᵢ. Then pᵢ divides p₁⋯p_k, which is pᵢ times the product of the other entries (school arithmetic of finite products, @def-sum-product), so p | P − p₁⋯p_k = 1 (@exm-divides-combination), and p ≤ 1 as in the proof of @thm-primes-infinite, against p ≥ 2. (b) 3·5 + 1 = 16 = 2⁴: prime factor 2. 2·7 + 1 = 15 = 3·5: prime factors 3, 5. Neither P is prime; each has a prime factor off its list.
  - *Marking scheme* (8): P ≥ 2 and a prime factor 2; pᵢ divides the product 2; p | 1 by a named result 2; p | 1 contradicted 1; both computations 1.
- **C3** `[C3: Challenge: primes of the form 3k + 2]`. "Prove that for every integer n ≥ 1 there is a prime p > n with p = 3k + 2 for some k ∈ ℤ. *Hint:* consider N ≔ 3·n! − 1, and @exr-induction-in-practice-b2." *Solution:* N = 3(n! − 1) + 2 ≥ 2, since n! ≥ 1. By @exr-induction-in-practice-b2, N = q₁⋯q_k with primes qᵢ. Each qᵢ > n: if qᵢ ≤ n, then qᵢ | n! (Step 1 of the proof of @thm-primes-infinite), so qᵢ | 3·n! − N = 1, impossible. No qᵢ is 3, since N leaves remainder 2 on division by 3. So each qᵢ is 3t + 1 or 3t + 2 (if qᵢ = 3t, then 3 | qᵢ and qᵢ = 3). If every qᵢ were 3t + 1, then N would be too, since (3a + 1)(3b + 1) = 3(3ab + a + b) + 1 and an induction on k carries this along the product; but N = 3(n! − 1) + 2, against the uniqueness in @thm-division-algorithm. So some qᵢ = 3t + 2, and qᵢ > n.

**Ledger (2.4).** Real cube roots exist and are unique, (p/q)³ = p³/q³ (school facts, F1–F2 convention, as in Section 1.6); ℚ closed under multiplication; trichotomy for p ≤ n or p > n; |n| ≤ 1 ⇒ n² ≤ 1 and |n| ≥ 2 ⇒ n² ≥ 4; |n| ≤ 3 ⇒ n² ≤ 9 (C1); (x − 4)(x + 2) ≤ 0 from the signs of the factors (B1 (b)); finite products, factors commute (C2).

### 4.5 Section 2.5: Equinumerous Sets and Finite Sets (`25`)

Budget 4,160 → ≤ 5,000 (expected ~4,870). Folds ~300.

1. **Opening, 25:3**, replaced (~115): "Section 1.1 left a puzzle half solved: among any five lattice points two have a lattice point as midpoint, provided that five objects in four boxes always put two in one box. That principle sounds too obvious to need proof, but it is a statement about every finite collection, and 'finite' has no definition yet. Section 1.6 supplied the tool: a bijection pairs the elements of two sets one for one. This section makes 'the same size' mean 'there is a bijection', defines finite sets by pairing with {1, …, n}, proves the pigeonhole principle and comes back to the five points, and then proves the facts about finite sets on which counting rests. Whether ℚ is larger than ℕ is the question of Chapter 3."
   This paragraph is where the section opens on the hook; the theorem itself comes after `def-finite`, so that 1.1's Looking-ahead ("from a precise definition of 'finite'") holds as written.
2. **25:7**, append: "Section 1.6 proved that the bijections are exactly the maps with a two-sided inverse (@thm-bijection-iff-inverse), and said that such a pairing is how this book says 'the same size'."
3. **Quick check** after the list 25:26–29 (weird examples): "Decide, from @def-equinumerous: (a) |∅| = |{∅}|? (b) |{1, 2}| = |{{1, 2}}|? (c) |{x ∈ ℝ : x² = −1}| = |∅|?" *Solution:* (a) No: {∅} has the element ∅, and a function ∅ → {∅} has no values, so it is not surjective. (b) No: {{1, 2}} has one element, so every function {1, 2} → {{1, 2}} sends 1 and 2 to it and is not injective. (c) Yes: the set is empty, and the empty function ∅ → ∅ is a bijection.
4. **Internal repair, 25:61**, replaced (~70): "Clauses (a)–(c) say that equinumerosity behaves like an equivalence relation: reflexive, symmetric and transitive, as equality is. We do not call it one. Chapter 4 makes 'equivalence relation' precise for relations **on a set** X, subsets of X × X; equinumerosity relates any two sets whatever, and there is no set of all sets for it to live on (@thm-russell). That is also why the book writes |A| = |B| here and keeps the symbol ∼ for later."
5. **Fold F2.5-a** `title="Why |A| is not an object"`: 25:63–67 verbatim (the remark and the paragraph on singletons). Two edits it forces: **25:39** "behaves like an equivalence relation" → "behaves like equality: reflexive, symmetric and transitive" (the term "equivalence relation" is left to the 25:61 paragraph); **25:22** "a remark below explains why" → "a second-reading fold below explains why".
6. **Quick check** after the examples 25:89–92: "How many elements does {n ∈ ℕ : 3 ≤ n ≤ 7} have? Give the bijection." *Solution:* 5, by k ↦ k + 2 from {1, …, 5}, with inverse m ↦ m − 2 (@lem-naturals-arithmetic (d)).
7. **25:104** heading → `## Back to the pigeons`. **25:106** replaced (~110): "Section 1.1 reduced its question (Q1) to one step: five points, each with one of four parity patterns, put two points on one pattern. In the language of functions, sending each point to its pattern is a map from a five-element set to a four-element set, and the step says that it is not injective. Chapter 1 also found one function from a three-element set to a two-element set that is not injective (@exm-injective-surjective-first (c)), and observed without proof that none can be. Here is the general fact, for the standard sets {1, …, m} and {1, …, n}."
8. **Scratch work for `thm-pigeonhole`.** The Idea 25:114–116 becomes a **`[Scratch work]`** idea (≤ 20 lines). It keeps 25:115's text and its self-explain prompt, and adds before the prompt: "On scrap paper, with n = 1 and m = 3: three pigeons in two holes; if hole 2 is empty, all three sit in hole 1; if pigeon 2 sits in hole 2, move it to pigeon 3's place and send pigeon 3 away." The table:

   | Givens | Goal |
   |---|---|
   | P(n); m > n + 1; f: {1, …, m} → {1, …, n + 1} injective | a contradiction |
   | Case 1: n + 1 is no value of f | f with codomain {1, …, n} is injective, m > n: against P(n) |
   | Case 2: f(j) = n + 1 | an injection {1, …, m − 1} → {1, …, n}, with m − 1 > n: g ≔ f ∘ σ |

9. **25:175**: "Section 3.3 meets surjections" → "Section 3.2 meets surjections".
10. **Fold F2.5-d** `title="Two loose ends from Chapter 1 and *Logic and Proof*"`: 25:177 verbatim.
11. After the typical-use paragraph 25:179–183, insert:
    - **`exm-method-pigeonhole`** `[Method: the pigeonhole principle]`.
      - **Template.** (1) Choose the pigeons, a set A whose number of elements you know, and the holes, a set B with fewer. (2) Define p: A → B, "the hole of a pigeon", and check that its values lie in B. (3) By @cor-pigeonhole-finite-sets (a), p is not injective: two different pigeons a ≠ a′ share a hole. (4) Translate "same hole" back into the property you want.
      - **When to use it.** The claim says "among any N objects, two have …", or "some value is taken twice", and N exceeds the number of possible values.
      - **The usual failure.** Holes for which sharing a hole does not give the property: choose the holes by what two pigeons should share. Pigeons that need not be different (a list with repeats is not a set with N elements). Claiming to know which two pigeons share a hole.
    - **`exm-five-lattice-points`** `[Back to the five lattice points]`: "Show that among any five different lattice points, two have a lattice point as midpoint." Idea (one line): pigeons the points, holes the parity patterns (@exm-method-pigeonhole). *Solution:* "Let A be a set of five lattice points, so A has 5 elements. Let B ≔ {0, 1} × {0, 1}, which has the 4 elements (0, 0), (0, 1), (1, 0), (1, 1) (number them 1 to 4). Send (a, b) ∈ A to (r, s), the remainders of a and b on division by 2 (@thm-division-algorithm, r, s ∈ {0, 1} as in the paragraph above). Since 5 > 4, @cor-pigeonhole-finite-sets (a) gives two different points (a, b) ≠ (c, d) in A with the same remainders. Then a, c have the same parity, and so do b, d, so their midpoint is a lattice point by @exm-lattice-midpoint. This answers (Q1) of Section 1.1: yes." Aftermath (one sentence): "different" costs nothing, since a point and itself have the point as midpoint; and the four corners of a unit square (Section 1.1) show that five cannot be lowered.
    - **Quick check:** "Choose pigeons and holes: among any 11 integers, two differ by a multiple of 10." *Solution:* Pigeons: the 11 integers. Holes: the remainders 0, …, 9 on division by 10, a 10-element set. Two with the same remainder r: a = 10q + r, b = 10q′ + r, a − b = 10(q − q′).
12. **Fold F2.5-b** `title="Why the step does not remove a point"`: 25:230 verbatim.
13. **Quick check** after 25:264: "S ⊆ {1, …, 7} has 7 elements. What is S, and which results say so?" *Solution:* S = {1, …, 7}: if S ≠ {1, …, 7}, @prp-subset-finite gives S k < 7 elements, and @cor-finite-size-unique forbids k = 7.
14. **Fold F2.5-c** `title="Subsets and functions to {0, 1}"`: 25:304 verbatim.
15. **Contradiction at scale**, a bold-lead-in paragraph after the proof 25:316–318 (~85): "**Contradiction at scale.** The proof never computes with g. It supposes the bijection, hands it to two theorems already proved, and lets them disagree about the number of elements of B. The claim is a negation, 'no bijection', so this is face (i), chosen by @exm-method-choosing-the-form; but the clash is between results, not between two lines. The proofs of @thm-pigeonhole and @cor-finite-size-unique have the same shape inside them."
16. **25:340**: "Section 3.6 proves" → "Section 3.5 proves".
17. **Quick check** after the remark 25:358–360 (pays 2.4's Looking-ahead): "Show that the set of primes is infinite." *Solution:* Suppose it is finite. It is non-empty (2 is prime), so it is {p₁, …, p_n} with n ≥ 1 (@def-finite and the remark), and has a maximum M (@prp-finite-max). By @thm-primes-infinite there is a prime p > M, which is in the set and exceeds its maximum, a contradiction.
18. **Looking ahead** (`[Looking ahead]`, last on the main line): "Chapter 4 defines equivalence relations on a set, and meets equinumerosity again as a relation that behaves like one without living on a set."
19. **25:473** (C1 solution): "Section 3.6 proves it with the principle of choice of Section 3.3" → "Section 3.5 … of Section 3.2".
20. **B4** `[B4: Prove or disprove]`.
    - (a) Among any 12 different integers, two differ by a multiple of 12.
    - (b) Among any 3 different integers, two have an even sum.
    - (c) Among any 5 different lattice points of space (points of ℤ³), two have a lattice point as midpoint.
    - (d) If A has 8 elements and f: A → {1, 2, 3, 4}, then some value of f is taken at least 3 times.
    - (e) No function from the set of subsets of {1, 2, 3} to {1, …, 7} is injective.
    - (f) Every injection {1, …, n} → {1, …, n} is surjective.
    - *Solution:* (a) False: 0, 1, …, 11; any two differ by an integer d with 1 ≤ |d| ≤ 11, not a multiple of 12. (Thirteen would do, by the 11-integers Quick check's argument.) (b) True: pigeons the three integers, holes the two parities (@thm-even-or-odd), a 2-element set; 3 > 2, so two share a parity (@cor-pigeonhole-finite-sets (a)), and their sum is even (@exm-parity-of-sums). (c) False: five of the eight points with coordinates in {0, 1} (Exercise C3 of Section 1.1): any two differ in a coordinate, where the sum is 1. (d) False: A = {1, …, 8}, f(k) ≔ the integer part of (k + 1)/2, with values 1, 1, 2, 2, 3, 3, 4, 4: each value is taken exactly twice. (Nine elements would force a value three times, as in Exercise B2 (b).) (e) True: the power set has 2³ = 8 elements (@prp-power-set-count), and 8 > 7, so @cor-pigeonhole-finite-sets (a) applies. Verdicts: three true ((b), (e), (f)), three false. (f) True: an injection f with codomain shrunk to its image is a bijection, so f({1, …, n}) has n elements; it is a subset of {1, …, n}, so it is all of it (25:264), and f is surjective.

21. **25 B2 (b)** (`exr-finite-sets-b2`, label kept; S2: the old (b) is Cummings's Proposition 1.9 with its numbers). New (b): "Prove that among any 7 different points of {1, 2, 3} × {1, 2, 3}, three lie in one row, that is, have the same first coordinate." New hint: "*in (b), the rows are the holes; how many points can a row take if no row takes three?*" *Solution (b):* Let A ⊆ {1, 2, 3} × {1, 2, 3} have 7 elements, and Aᵢ ≔ {(x, y) ∈ A : x = i} for i = 1, 2, 3. These are disjoint with union A, and each is finite by @prp-subset-finite, with kᵢ elements. If every kᵢ ≤ 2, then A has k₁ + k₂ + k₃ ≤ 6 elements (@prp-disjoint-union-count twice), against @cor-finite-size-unique. So some kᵢ ≥ 3: three points in row i. Six points do not suffice: two in each row. Sidecar `exr-finite-sets-b2.py` and the ledger line of B2 updated (the min-pairing line goes; "k₁ + k₂ + k₃ ≤ 6 from kᵢ ≤ 2 | R arithmetic" comes in).
22. **Idea of `cor-pigeonhole-finite-sets` (25:160)**, after "the **smallest** number" append "(a least element, @exm-method-least-element)". Fading, Idea level (§1).

Count: +26 +35 +90 −5 +60 +60 (recall net) +100 (scratch net) +130 +180 +70 +60 +85 +80 +35 +15 ≈ +1,021; folds −(100 + 72 + 66 + 60) ≈ −300; ≈ 4,870. Checks: 6. **Reserve** (if over 5,000): 25:276 ("Every later induction …", 88 words) into a fold.

### 4.6 Chapter 3 index, provisional edit (`3/index.md`, coordinator with this chapter's S4; ch03-deepen redoes it)

- **Title** `# Countable and Uncountable Sets`.
- **¶1**: "The answer is in Section 3.4" → "Section 3.3".
- **¶2, last sentence** ("The finite sets come first, …") → "It starts from the finite sets of Section 2.5 and the pigeonhole principle."
- **What you need**: "Chapters 1–2" kept; add to the Chapter 2 list: equinumerous and finite sets (@def-equinumerous, @def-finite, @def-infinite), pigeonhole (@thm-pigeonhole, @cor-pigeonhole-finite-sets), subsets and disjoint unions (@prp-subset-finite, @prp-disjoint-union-count), no proper copy (@thm-finite-no-proper-copy, @exm-hilbert-hotel), and @prp-power-set-count. Renumber: "Section 3.3 shows why one use of ∃E" → 3.2; "Section 3.4 states three school facts" → 3.3; "Sections 3.4–3.5 use them" → 3.3–3.4; "Section 3.3 uses one fact from school algebra" → 3.2.
- **Time**: "About 25 hours on the core track …; about 30 hours for everything" (layout §2).
- **Roadmap**: drop the first bullet (it moves to Chapter 2).
- **Named moves**: unchanged until ch03-deepen adds the boxes.

### 4.7 Chapter 4 index, provisional (new `4/index.md`, coordinator; ch04-deepen redoes it)

- **Title** `# Relations: Equivalence and Order`.
- **Story**: old ix:5 verbatim, with its opening "The second half of the chapter is about relations." → "This chapter is about relations." ("what Section 2.1 proved about ℕ" stays.)
- **What you need.** "*Logic and Proof*, Chapters 1–8, and *Sets, Relations, and Cardinality*, Chapters 1–3." From fd1: the rules for "for every" and "there exists", equality (@fd1:def-rules-equality), bounded quantifiers (@fd1:prp-bounded-quantifier-rules), negating quantifiers (@fd1:prp-bounded-quantifier-negation). From Chapter 1: relations as sets of pairs and products (@def-relation, @def-cartesian-product), functions and preimages (@def-function, @def-preimage), power sets (@def-power-set). From Chapter 2: well-ordering (@thm-well-ordering), divisibility and the division algorithm (@def-divides, @thm-division-algorithm), finite maxima (@prp-finite-max), equinumerous sets (@def-equinumerous).
- **Time**: "About 15 hours on the core track …; about 20 hours for everything" (layout §2).
- **Roadmap**: old ix:16–18 (the three relations bullets) verbatim.
- **Named moves**: old ix:25 verbatim.
- **Threads**: *same size* (1.6 → 2.5 → 4.2); *the clock* (4.2's congruence → *Number Systems*, Chapter 3).
- No Summary or Terms yet (ch04-deepen).

### 4.8 fd2-internal prose pointers (coordinator, before S3; binding rule 5)

Section map for old-numbered text: 2.4 → 4.1, 2.5 → 4.2, 2.6 → 4.3, 3.1 → 2.5, 3.2 → 3.1, 3.3 → 3.2, 3.4 → 3.3, 3.5 → 3.4, 3.6 → 3.5. Not to be applied to fd2 Chapter 1 (already final), to STATUS, or to this blueprint.

| File:line | Now | Becomes |
|---|---|---|
| 21:36 | equivalence class "in Section 2.5" | Section 4.2 (§4.1 item 1) |
| 21:377 (C1 solution) | "Section 2.6 defines least upper bounds" | Section 4.3 |
| 23:356 | "will mean in Chapter 3" | "means in Section 2.5" (§4.3) |
| 25:3, 25:61 | Chapter 2 / Chapter 1 framing; @def-equivalence-relation | rewritten (§4.5 items 1, 4) |
| 25:175 | Section 3.3 | Section 3.2 |
| 25:340 | Section 3.6 | Section 3.5 |
| 25:473 | Sections 3.6, 3.3 | Sections 3.5, 3.2 |
| 3/01:3, :33, :35 (first), :47, :112, :150, :271, :443 | Section 3.1 (finite sets) | Section 2.5 |
| 3/01:35 (second), 3/01:125, :183, :274, :302 | Section 3.4; 3.3 | Section 3.3; 3.2 |
| 3/02:3, :11, :114 | Section 3.2 | Section 3.1 |
| 3/02:47 | Section 3.6 | Section 3.5 |
| 3/02:139, :201 | Section 3.4 | Section 3.3 |
| 3/03:93 | Section 3.5 | Section 3.4 |
| 3/03:195 | Section 3.3 | Section 3.2 |
| 3/04:3, :17 | Section 3.1 | Section 2.5 |
| 3/04:240 | Section 3.2 | Section 3.1 |
| 3/04:335 | Section 3.4 | Section 3.3 |
| 3/05:3 | Section 3.5 | Section 3.4 |
| 3/05:71, :80, :103 | Section 3.1 | Section 2.5 |
| 4/01:3, :148 | Sections 2.5 and 2.6 | Sections 4.2 and 4.3 |
| 4/01:97 | Section 2.6 | Section 4.3 |
| 4/01:273 | Section 2.5 | Section 4.2 |
| 4/02:3, :41, :74 | Section 2.4 | Section 4.1 |
| 4/03:3 | Section 2.5 | Section 4.2 |
| 4/03:7 | Section 2.4 | Section 4.1 |
| 4/03:257 | "what 'finite' will mean in Chapter 3" | "what 'finite' means in Section 2.5" |
| 1/03:609 (ledger line, `def-set-operations (claim)`) | "F2.2 proves it (exm-divisibility-lcm)" (that label is now in Chapter 4) | "F2.2 §02 proves it (exr-induction-in-practice-b3 (c))"; the one Chapter 1 line this blueprint touches, since it names a label, not a number |
| 3/index, 2/index | | §4.0, §4.6 |
| `fd2/src/index.md` (Preface) | table rows 2–4; "Chapters 1–3 are written; Chapter 4 is not yet." | rows: 2 "The arithmetic of ℕ and ℤ from induction, well-ordering, induction as a craft, recursion, contrapositive and contradiction, infinitely many primes, finite sets and the pigeonhole principle"; 3 "Countable sets, the axiom of choice, diagonal arguments and Cantor's theorem, the Schröder–Bernstein theorem, infinite sets"; 4 "Relations: equivalence relations and partitions, partial orders"; 5 "Zorn's lemma". "Chapters 1–4 are written; Chapter 5 is not yet." |

**3/04:52, the second internal repair (layout §3.2).** "As with equinumerosity (Section 3.1, after @prp-equinumerous-properties), we do not call this a partial order: … And antisymmetry, the clause (PO2) of @def-partial-order, would say …" becomes: "As with equinumerosity (Section 2.5, after @prp-equinumerous-properties), ≤ between sizes is reflexive and transitive, but we do not call it an order: there is no set of all sets for it to be a relation on (@thm-russell). And the clause one would expect next, the analogue of x ≤ y ≤ x ⇒ x = y for numbers, would say …"; the rest is kept.

**Kept** (correct as they stand): 1/index:13, 40–43, 49; 1/02:298, 441; 1/03:233, 249 (but 1/03:609 is repointed, table above); 1/04:344, 347; 1/05:93, 179, 200, 202, 464; 1/06:251, 374, 402; 22:94, 178, 250, 267, 286, 300 ("Section 2.3"); 23:481 ("smallest counterexample of Section 2.2"; §4.2 item 7 keeps the term there); 3/01:377 (2.2 sets unique factorization aside: still true, 22:100); 3/01:278, 431; 4/01:137 (the "2 is prime" example stays in 2.2's divisibility subsection); 4/02:271; 4/03:140, 223, 234, 461. fd2's own Ch1 ledgers already use the new numbering, except the stale label in 1/03:609 (table above).

## 5. Budgets and Time

| § | Main now | Budget | Expected | Folds |
|---|---|---|---|---|
| 2.1 | 4,136 | 5,000 | ~4,450 | ~520 |
| 2.2 | 3,364 | 5,000 | ~4,210 | 0 |
| 2.3 | 3,809 | 5,000 | ~4,200 | 0 |
| 2.4 | — | 4,500 | ~3,500 | 0 |
| 2.5 | 4,160 | 5,000 | ~4,870 | ~300 |
| total | 15,469 | 24,500 | ~21,170 | ~820 |

**Exercises.** New: 2.4's eight; four B4s. The chapter has 37 (A 5, B 19, C 13). Core track: all A, one B and one C per section, the exit check 22 C1: 15 items. Calibrated on the old Chapter 2 index (30/45 h) and the Ch1 figures (40 h core, 55 h full for 30,596 + 1,872 words and 54 exercises), ~21,200 main and ~800 folded words with 37 exercises come to about 30 h core and about 40 h full, as layout §2 expects. The coordinator recomputes with `check_structure.py --words` after S3 and writes the index.

## 6. Pointers, promises, edits outside the chapter

- **Forward pointers.** 2.4's Looking-ahead (primes as an infinite set → 2.5; paid by 2.5's Quick check, §4.5 item 17). 2.5's Looking-ahead (equivalence relations → Chapter 4; promise row, paid by 4.2 `def-equivalence-relation` with equinumerosity revisited per layout §1). 2.2's pointer to 2.4 (§4.2 item 7) and 22:250's to 2.3 are prose.
- **STATUS** (coordinator, S4). Rows 155 (pigeonhole, F2.1 §01 → F2.2 §05) and 158 (same size, F2.1 §06 → F2.2 §05): mark paid by `thm-pigeonhole` and `exm-five-lattice-points`, and by `def-equinumerous`. Row 162 (2ⁿ subsets; Yˣ): paid by `prp-power-set-count` and `exr-finite-sets-c2`. Row 179's first item (passing from a finite set to a list): paid by F2.2 §05 `def-finite` and its closing remark. Retag every F2.3 §01 row to F2.2 §05 and F2.2 §04–§06 rows to F2.5 §01–§03 (layout §3.3). New rows: the two Looking-aheads above. Deviation notes: (1) the §4.8 map was applied to old-numbered fd2 files only, so layout §3.3's sweep must not re-apply it to fd2 `src/`; (2) **layout §5 "2.5 opens 'Back to the pigeons'"**: 2.5 opens on the hook in its first paragraph (§4.5 item 1), and `## Back to the pigeons` heads the pigeonhole subsection after `def-finite`, because 1.1's approved Looking-ahead promises the principle "from a precise definition of 'finite'". The S1/S2 commit message says the same, so the S7 referee does not flag it.
- **Ledgers** (coordinator, S4, `tools/ledger.py`): new `ch02.yaml` lines for 2.4 (§4.4 ledger) and the new examples (2.1: f(ℕ) ⊆ ℕ, m − 2 ∈ S; 2.2: the 3ⁿ ≥ n³ inequalities; 2.5: remainders in {0, 1}); re-key 22's `def-divides (example)` lines, which name "this section's subsection on divisibility" for the example now in "Finding P(n) inside P(n + 1)", and rewrite the second of them (22:439) for the new example: "9^0 = 2^0 = 1, a^(n+1) = a^n * a, 9^n and 2^n integers (the example 7 | 9^n - 2^n) | powers, school meaning; def-power in F2.2 §03"; 22 B1 and 25 B2 lines as in §4.2 item 15 and §4.5 item 21; `ch04.yaml` unchanged.
- **NOTATION.** No new notation (n! is 2.3's). The `def-divides` row's tags were moved to F2.1 §01 by ch01-deepen; nothing to do.
- **fd3, fd4, fd1.** Untouched here; their pointers are layout §3.3's sweep. `thm-primes-infinite` needs no fd3 twin (layout §4).

## 7. S2a: claims to verify

1. 2.1: `exm-no-infinite-descent` (f(ℕ) non-empty, f(m + 1) ∈ f(ℕ)); `exm-least-element-down-by-two` (m ≥ 2 ⇒ m − 2 ∈ S, m − 2 < m; m ≤ 1 ⇒ m ∈ {0, 1}); Quick checks ({17, 12, 7, 2}, least 2; {n ∈ ℤ : n² < 30}, lower bound −6, least −5); B4 (a)–(f), in particular (d) and (f) (−4 < −7/2); the folds F2.1-a, b hold no cited statement and leave A1 (e) doable.
2. 2.2: the scratch-work identity 9ⁿ⁺¹ − 2ⁿ⁺¹ = 9(9ⁿ − 2ⁿ) + 7·2ⁿ and the rewritten 22:94–98; 9ⁿ⁺¹ − 4ⁿ⁺¹ = 9(9ⁿ − 4ⁿ) + 5·4ⁿ; 22 B1 ((n + 1)³ + 2(n + 1) = (n³ + 2n) + 3(n² + n + 1)); the 22:116 and 22:308 edits; `exm-choosing-the-base` (3ⁿ ≥ n³ for all n ∈ ℕ; 2n³ ≥ 3n² + 3n + 1 for n ≥ 3; 3n³ < (n + 1)³ exactly at n = 0, 1, 2); the backward-step entry (n² ≥ 1; the reversal; 1 = −1); the gallery check (n² ≤ 2ⁿ fails at 3; 2n² ≥ (n + 1)² for n ≥ 3); B4: 2²ⁿ⁺¹ + 1 (the step 4(2²ⁿ⁺¹ + 1) − 3), 2⁹ < 9³ and 2ⁿ ≥ n³ from 10 on, the sum (n + 2)(3n + 5)/2, 11 not 3a + 7b, 5ⁿ ≥ 4ⁿ + 3ⁿ for n ≥ 2 and its failure at 0, 1, n² + 1 at n = 2, 4, 6, 8 (65 = 5·13); three true, three false. After the cut, 22's remaining text (22:150, 178, 180; A1, B2, C3) reads correctly without the moved subsection, and the term "smallest counterexample" is defined before its first use.
3. 2.3: the Quick checks (1, 3, 7, 15; the constant sequence 1; Bernoulli at −1/2, 3; the failed strengthening (n + 1)(n + 2) > (n + 1)²); the fd1 recall matches @fd1:exm-strengthen-the-claim.
4. 2.4: `exm-contrapositive-mod-three` (n = 3q + 1 gives 9q² + 9q + 3; remainders 0 and 2 give 1 and 7, so the statement is true and not vacuous); the Quick checks (the negation; (a)–(c) forms, (a) now x² ≠ x ⇒ x ≠ 1; 121 = 11²; ∛3 and parity; 54, 45); `thm-primes-infinite` Step 1 (induction on n!, 0! = 1) and Step 2 (p | 1 ⇒ p ≤ 1); 4! + 1 = 25; `prp-cube-root-two-irrational` (p³ = 8k³ + 12k² + 6k + 1; q³ = 4s³); the moved 22:69–84 is verbatim and its references resolve; `exm-three-power-factor`; A1 (721 = 7·103; the three remainders; (b)(ii) a² + b²), B1–B4 (B1 (a) 3 | a + b, B1 (b) (x − 4)(x + 2); B2 (a)'s three cases; B2 (b) via 22 B3 (b); B3's 2^{m−1} ∈ ℕ and 2^{m−1} < 2^m; B4 (a) n = 2, (b) n even ⇒ 4 | n², (e)'s parity argument, (f) n = 89 smallest, with 91, 93, 95 factored; three true, three false), C1 (both diagnoses; Proof B's (N11), (N7) and its step (4)), C2 (16 = 2⁴, 15 = 3·5), C3 (N = 3·n! − 1 has a prime factor 3t + 2 above n, checked for n ≤ 8). Confirm against *Proofs* (Cummings) that none of 2.4's examples or items is its proposition or exercise (§ Inputs list, now including Exercises 6.6–6.8 item by item: 3 ∤ n² ⇒ 3 ∤ n, 8 ∤ n² − 1 ⇒ n even, m ∤ nt, x + y ≥ 2, x³ + x > 0), in particular that ∛2, the golden-ratio item B2 (a), m² − 8n = 5, a² − b² = 10, n² + n + 1, x² > 2x + 8 and n² ≥ 10 are not. The same check for 2.2 (Exercises 2.25–2.26, 4.3–4.7: 9ⁿ − 2ⁿ, 9ⁿ − 4ⁿ, n³ + 2n, 2²ⁿ⁺¹ + 1, 2ⁿ ≥ n³, the sum of 3k + 1, n² + 1) and 2.5 (Propositions 1.9–1.11, Exercises 1.8–1.24: the 3 × 3 rows, B4 (a)–(e)).
5. 2.5: the 25:22 and 25:39 rewordings; the 25:160 insertion; B2 (b) (rows, k₁ + k₂ + k₃ ≤ 6; six points with two per row); the weird-examples check; {3, …, 7}; the five-point example (B has 4 elements; the remainder map; "different" costs nothing); the 11-integers check; S ⊆ {1, …, 7}; the primes-infinite check (prp-finite-max needs n ≥ 1); the scratch-work table matches the proof's two cases; B4 (a)–(f) ((a) 0, …, 11; (b) parities; (c)'s five points; (d) the map k ↦ ⌊(k + 1)/2⌋ takes each value twice; (e) 8 > 7; (f) via 25:264; three true, three false); the folds F2.5-a…d hold no cited statement and no section's only check or warning; @def-equivalence-relation no longer cited in 2.5.
6. §4.8: every listed pointer, after the edit, names the right section; 1/03:609 names `exr-induction-in-practice-b3` (c), which proves 2 | n ∧ 3 | n ⇒ 6 | n; old ix:16–18 are the relations bullets; no fd2 Chapter 1 pointer changed; 3/04:52 no longer cites @def-partial-order; `check_forward_deps` passes for fd2.

## S2 replies (round 1)

Two blind referees (R1: 16 findings; R2: 15). All resolved here; no second round. Where both raised the same point, one reply covers both.

1. *R1, R2: 2.4 items close to Cummings Exercises 6.6–6.8 (error/gap).* Applied. B1 (a) → "if 3 ∤ a + b, then 3 ∤ a or 3 ∤ b" (R2's form; keeps the De Morgan lesson); A1 (b)(ii) → "if a² + b² is odd, then a is even or b is even" (not R2's "match B1", which would duplicate B1); B1 (b) → "x² > 2x + 8 ⇒ x > 4 or x < −2" (R1's x² + x > 6 changed in its numbers too); C1 Proof B → "n² ≥ 10 ⇒ n ≥ 4 or n ≤ −4" (R2), keeping the wrong negation and the dropped disjunct; Quick check (a) → "x² ≠ x ⇒ x ≠ 1" (R1); `exm-contrapositive-mod-three` → "3 ∤ n² + n + 1 ⇒ remainder 0 or 2", whose contrapositive turns an "or" into the single case remainder 1 (R1's idea; label kept, nothing cites it yet). Inputs corrected; the 6.6–6.8 check is item by item in S2a item 4.
2. *R1: Idea insertion "with S the failures" contradicts thm-induction-iff-well-ordering (gap).* Applied, R1's wording (§4.1 item 3).
3. *R1, R2: aftermath of exm-no-infinite-descent: forward @, negative denominators, "this section's opening" (gap/minor).* Applied: prose pointer without @, positive denominator with q > 0, "the halving question that opened the subsection on well-ordering".
4. *R1, R2: 2.2 B4 (b), (f), the gallery check repeat fd1 / near Cummings (gap).* Applied. (b) → 2ⁿ ≥ n³ for n ≥ 9 (false at 9 only). (f) → n² + 1 prime for even n ≥ 2 (65 at n = 8), not R2's n² + n + 17, which is Euler's polynomial, the family of fd1's n² − n + 41. Gallery check kept, its solution now names fd1 Chapter 4's warning and says the check makes it precise at the step.
5. *R1, R2: 2.4 B4 (a) is the worked example in disguise (gap).* Applied: "if 5 ∤ n² − 1, then 5 | n", false at n = 2 (R2). R1's suggested n² + n + 1 item became the worked example instead (item 1).
6. *R1: C1 Proof B cites (N8) for a missing case (error).* Applied: (N7) for the dropped disjunct, (N11) for the wrong negation, in the solution and the marking scheme.
7. *R1: Chapter 4 roadmap names ix:15–17 (error).* Applied: ix:16–18.
8. *R1: §1 Fading promises edits no item makes (gap).* Applied: §4.2 item 13 (22:116), §4.5 item 22 (25:160); §1 now names the bold paragraph after the proof of `thm-finite-no-proper-copy` (no Idea block is added there).
9. *R1: 2.5 B4 (a) clones B2 (a); (b) is Cummings Ex 1.8; (d) is the kn + 1 pigeonhole (gap).* Applied. (a) → the false "any 12 integers, two differ by a multiple of 12" (R1). (b): R1's "7 elements of {1, …, 12}, one divides another" is Cummings's Proposition 1.11 with n = 6, so rejected; (b) is "among any 3 integers two have an even sum". (d) → the false "8 elements, 4 values, some value 3 times" (R1's shape, made false for balance), refuted by an explicit map. Inputs reworded: the general kn + 1 theorem is not stated.
10. *R1, R2: exercise split A 5, B 17, C 15 (minor).* Applied: A 5, B 19, C 13.
11. *R1: §8 word budget not checkable by check_structure.py as written (minor).* Applied: §8 names a one-line snippet calling `prose_words` on the text before `## Exercises` (it reproduces 4,136 for 21) and accepts the whole-file advisory; the word-count paragraph says so too.
12. *R1: 25:39 uses "equivalence relation" before any gloss; 25:22 points into a fold (minor).* Applied, R1's wording, in §4.5 item 5.
13. *R1: "the step from 2 to 3 fails" (minor).* Applied: "the argument of the step fails from 2 to 3".
14. *R1: B3 discreteness needs 2^{m−1} ∈ ℤ; garbled range in the Idea of thm-primes-infinite (minor).* Applied: @prp-power-laws (d) cited; "every k with 2 ≤ k ≤ n".
15. *R1: 2.3 line reference and "met this cure once" (minor).* Applied: 23:311–313; "met this cure (@fd1:exm-strengthen-the-claim) with a sum that telescopes".
16. *R1, R2: 2.1 B4 (b) duplicates C1 (b); B4 (f) is the folded −7/2 example (minor).* Applied. (b) → "every non-empty set of negative rationals has a greatest element" (false, {−1/n}); R1's integer variants rejected because they would leave B4 with four true items. (f) → bound −13/3, integer −5 (R2). Sidecar named in §8 as before.
17. *R1 (optional), R2 (error): the (a + 1)ⁿ − 1 family; the scratch-work example 3 | 4ⁿ − 1 and 22 B1 5 | 6ⁿ − 1 are Cummings 2.25 / 4.3 (a), (f).* Applied. Scratch work and the 22:94–98 proof → 7 | 9ⁿ − 2ⁿ (R2), rewritten, not moved verbatim, with no "For instance"; Quick check → 5 | 9ⁿ − 4ⁿ (same move, practised); 22 B1 → 3 | n³ + 2n (R2's 11 | 12ⁿ − 1 stays in the family); B4 (a) → 3 | 2²ⁿ⁺¹ + 1; 22:272, ledger 22:439/22:447, sidecars, §1, S2a item 2 updated. A1 (a)(i) 6 | 7ⁿ − 1 is kept (approved text, not a Cummings item; only its pointer changes).
18. *R2: kept 25 B2 (b) is Cummings Proposition 1.9 with its numbers (error).* Applied: new (b), seven points of the 3 × 3 grid with three in one row (R2's suggestion), with hint, solution, sidecar and ledger (§4.5 item 21); Chapter 1 of *Proofs* added to the checked list.
19. *R2: 2.2 B4 (c) is the scratch-work example in disguise (gap).* Applied, but not with R2's n! ≥ 2ⁿ (Cummings Exercise 4.6): (c) is the sum 1 + 4 + ⋯ + (3n + 1) = (n + 1)(3n + 2)/2, whose step splits off a term. Verdicts 3 true, 3 false.
20. *R2: false existence claims in 2.4 B4 (e) and 2.5 B4 (e) need impossibility proofs (minor).* Applied: both are now true universal statements ("a² − b² ≠ 10"; "no function … is injective"), and 2.4's stem is STYLE §12.13.4's own. 2.4 B4 (b) became the true "if 4 ∤ n², then n is odd" to keep three true, three false; its false look-alike is named in the solution.
21. *R2: "Back to the pigeons" placement not recorded as a deviation (minor).* Applied: §6 STATUS deviation note (2), §8 item 1, and the commit message.
22. *R2: 22:308 names a step of 2.4's list (minor).* Applied: §4.2 item 14.
23. *R2: 1/03:609 cites exm-divisibility-lcm, now in Chapter 4 (minor).* Applied: §4.8 row, repointed to `exr-induction-in-practice-b3` (c).
24. *R2: smallest-counterexample box has one worked example and restates the list (minor).* Applied: the Template points at the list and names @lem-lowest-terms and @exm-three-power-factor as its two worked examples.
25. *R2: Inputs on list proofs; C1 Proof A should cite fd1's costume examples (minor).* Applied: Inputs reworded (C2 is Euclid's argument in direct form); @fd1:exm-costume-direct and @fd1:exm-costume-contrapositive cited in the choosing-the-form box and C1.
26. *R2: header says two warnings, plan has one (minor).* Applied: "one warning".

**Frozen after S2 (2026-10-25).**

## 8. Notes for S3 and S4

- **Before S3:** the coordinator applies §4.8 (pointers, 3/04:52, Preface) and commits.
- **Drafters:** three, in order. (i) 2.1 and 2.2, including the cut of 22:69–84, which it pastes unchanged into a stub `04-contrapositive-and-contradiction.md` under a provisional `# Contrapositive and Contradiction in Practice`; lands first (2.4 and 2.5 cite `exm-method-least-element`). (ii) 2.4 around the stub, and 2.3. (iii) 2.5 (cites `exm-method-choosing-the-form`, `thm-primes-infinite`). The coordinator writes the three indexes last. Sonnet may take 2.3 (Idea-level, minor; lean workflow).
- **Sidecars** (`fd2/verify/ch02/`, new): `exm-least-element-down-by-two.py`, `exm-choosing-the-base.py`, `exm-contrapositive-mod-three.py`, `thm-primes-infinite.py` (n ≤ 12: every prime factor of n! + 1 exceeds n), `prp-cube-root-two-irrational.py` (no p³ = 2q³ with 0 < q ≤ 10⁴; the parity lemma on a range), `exm-three-power-factor.py`, `exm-five-lattice-points.py` (all 5-subsets of a 4×4 grid), `exr-naturals-and-well-ordering-b4.py`, `exr-induction-in-practice-b4.py`, `exr-contrapositive-and-contradiction-a1.py`, `-b1.py`, `-b2.py`, `-b3.py`, `-b4.py`, `-c2.py`, `-c3.py`, `exr-finite-sets-b4.py`. Rewritten under kept labels: `exr-induction-in-practice-b1.py` (3 | n³ + 2n), `exr-finite-sets-b2.py` ((b): all 7-subsets of the 3 × 3 grid).
- **Checkers:** `check_structure.py` (0 fatal; its whole-file "main line" word advisory is accepted, since it counts exercises too). The budget (main line ≤ 5,000 per section, 2.4 ≤ 4,500) is measured to `## Exercises`: from `fd2/`, `../.venv/bin/python -c "import sys; sys.path.insert(0, '../tools'); from check_structure import prose_words; t = open(sys.argv[1]).read(); print(prose_words(t.split('## Exercises')[0]))" src/ch02-induction-and-finite-sets/0k-….md` (4,136 for 21 at S1, as in the table above). Also `check_numbers.py`, `check_notation.py`, `check_forward_deps.py` (2.1–2.4 cite nothing after themselves except the prose pointers; 2.5 cites no Chapter 4 label).
- **Review (lean workflow, layout §7):** 2.2, 2.4 and 2.5 run the full pipeline. 2.1 and 2.3 get a changed-only blind review (boxes, scratch work, tables, B4s, checks, folds and pointer edits count as changes). Chapters 3 and 4 get only the §4.8 edits here; their re-cut is ch03-/ch04-deepen.
- **Open for the author** (none blocking):
  1. (Recorded as a deviation from layout §5, §6 STATUS note (2), not an open question.) "Back to the pigeons" is the heading of 2.5's pigeonhole subsection, after `def-finite`; the section *opens* on the hook in its first paragraph. Putting `thm-pigeonhole` first is possible (its proof needs no definition of "finite") but would contradict 1.1's approved Looking-ahead ("from a precise definition of 'finite'").
  2. `thm-primes-infinite` is stated as "for every n ∈ ℕ there is a prime p > n" (via n! + 1), since "infinite" is defined only in 2.5; the list form is Exercise C2, and the set form is 2.5's Quick check.
  3. 2.2 keeps the phrase "smallest counterexample" with a one-sentence definition, so that its A1, B2, C3 and 2.3's C1 need no change; the method box is 2.4's.

- *Deviation (S3, 2026-10-25):* 2.4 quick check (c) names x_1, x_2 and finishes the one-line argument; the scratch work of `exm-three-power-factor` is prose followed by the table; |n| is written `\abs{n}`.
- *Deviation (S3, 2026-10-25):* index Terms "least element", "greatest element", "maximum/minimum" have no definition block and point to the prose before `thm-well-ordering` and `prp-finite-max`. Main-line words (fold-excluded for 2.5): 2.1 4,406; 2.2 3,892; 2.3 4,081; 2.4 2,195 (below the 3,500 expected, nothing omitted); 2.5 4,801 (+219 folded). Time: 30 h core, 40 h full.
- *Deviation (S3, 2026-10-25):* `tools/check_forward_deps.py` does not exist; the forward-dependency check of §8 was not run.
