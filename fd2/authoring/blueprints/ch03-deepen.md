<!-- hand-written -->
# Deepening blueprint: F2.3 Countable and Uncountable Sets (fd2 Chapter 3), stage S2

**Status: S2 applied, frozen, 2026-10-25.** Two blind referees (round 1), all findings applied or answered (end of file). Next: S2a, then S3.

**What this is.** The S1 blueprint for fd2 Chapter 3 under the binding layout `fd2/authoring/design/layout-final.md` (option C; §1 Ch3 rows, §2, §3, §5, §7). A drafter executes it with this file, the current `fd2/src/ch03-countable-and-uncountable/` files, `authoring/STYLE.md` (§1 "House manner from fd2 on", §2 item 6, §4 item 3, §5, §11, §12.0, §12.5, §12.13.4, §12.14), `DRAFTING.md` and `NOTATION.md`. Format: `ch01-deepen.md` (frozen), leaner. All five sections are **moved** sections (layout §7): they get the new devices, pointer fixes and the one internal repair, and nothing else is rewritten. The changes are kept in proportion to that.

**File state and line references.** The coordinator's S1 commit for Chapter 2 (`4bd59ac`) already renamed old 3.2–3.6 to `01…05` and moved old 3.1 to `ch02…/05-finite-sets.md`. No Chapter 3 text has been edited since. Line references are to the files at `0b0197b`: `01:` `01-countable-sets.md`, `02:` `02-countable-unions-and-choice.md`, `03:` `03-diagonal-arguments.md`, `04:` `04-comparing-cardinalities.md`, `05:` `05-infinite-sets.md`, `ix:` `index.md`. This blueprint moves no files.

**Word counts** are main-line prose words by `tools/check_structure.py`'s `prose_words` (a math span is one word; code and folds excluded), from the top of the file to `## Exercises`, as in ch01/ch02-deepen. Measured at `0b0197b`:

| File | Main line now (to Exercises) | Whole file | Layout budget |
|---|---|---|---|
| 01 | 3,610 | 5,991 | 5,000 |
| 02 | 3,068 | 5,384 | 5,000 |
| 03 | 2,960 | 5,074 | 5,000 |
| 04 | 2,398 | 4,214 | 4,200 |
| 05 | 1,448 | 3,709 | 3,700 |

The layout's figures for 3.4 and 3.5 (4,200, 3,700) are the whole-file counts. Both files already exceed those figures. This blueprint reads every budget as main line to Exercises, as Chapters 1 and 2 do, and lists the reading for the author (§8, item 3). Every section stays well under 5,000 without folds, so **no fold is planned** (STYLE §12.0: folding is not a way to grow a section).

**Inputs.** Layout §1 (rows 3.1–3.5), §3.2 (downstream-cited labels: 3.1 `cor-product-countable`, `def-countable`, `exr-countable-sets-b2`, `lem-subsets-of-naturals`, `prp-countable-image`, `prp-countable-subset`, `prp-union-two-countable`, `thm-countable-characterizations`, `thm-integers-rationals-countable`, `thm-product-countable`; 3.2 `ax-choice`, `thm-algebraic-countable`, `thm-countable-union`; 3.3 `thm-binary-sequences-uncountable`; 3.4 `def-card-le`, `prp-card-le-surjection`), §3.2's internal repair, §3.3, §5 (devices, threads), §7. The frozen `ch02-deepen.md` supplies Chapter 2's boxes, which are cited here and never re-taught: `exm-method-least-element` (2.1), `exm-method-induction-step` (2.2), `exm-method-choosing-the-form`, `exm-method-smallest-counterexample` (2.4), `exm-method-pigeonhole` (2.5). From Chapter 1: `exm-method-injectivity`, `exm-method-surjectivity`, `exm-method-construct-and-verify`, `exm-method-counterexample`. The Cummings long-form skill is used for its moves only: motivation before a major definition, scratch work kept apart from the proof, hooks and payoffs. There are no footnotes, no jokes, no history beyond one line, and no first person. *Proofs* (Cummings) was read for technique only. None of its countability or Cantor exercises, examples or wording is used. Every new example, item and answer below is the book's own. The old blueprint `ch03.md` fixed what is kept: the key proofs (`thm-countable-characterizations`, `thm-countable-union`, `thm-cantor`, `thm-schroder-bernstein`); the faded diagonal triple (worked `thm-binary-sequences-uncountable`, 03 B1 with the last step blank, 03 C1); the two Try-it-firsts (`thm-product-countable`, `thm-cantor`); the find-the-error items 01 C2 and 04 C2; the exit checks 02 C1 and 03 C1; and R1–R4.

**Binding rules.**
1. **No label is lost or renamed; cited content is kept.** Every label now in 01–05 stays in its file. The 16 downstream-cited labels listed above keep the content of their blocks. Exercise labels keep their names (`exr-<slug>-…`).
2. **fd1, Chapter 1 and Chapter 2 are cited, never re-taught.** That covers ∃E (@fd1:def-rules-existential), the catalogue `@fd1:exm-not-allowed-catalogue`, the irrationality of √2 (@fd1:thm-sqrt2-irrational), the injectivity and surjectivity templates, pigeonhole and the least element. Each is recalled in a clause and linked.
3. **No forward citation (@label) into Chapters 4–5.** The repair at 04:52 removes the one `@def-partial-order`. Pointers into later sections of this chapter and into Chapter 5 are prose only and are never reasons (STYLE §12.1, first bullet). The files have more than one per section (3.1 points to 3.2 and 3.3; 3.2 has 02:47, 02:139, 02:201); these in-chapter previews are kept as they stand, renumbered, and no new one is added except the thread hook below. The comparability hook ends 3.4's main line as a `.remark` titled `[Looking ahead]`, STYLE §12.1's form (§4.4 item 5); it is a promise row in STATUS (§6).
4. **Quick checks.** Layout §5 asks only for STYLE §5's minimum after Chapter 2. Each method section still gets one new check after its box, and 3.3 gets two because of its new opening.
5. **Pointers.** All Chapter-3 pointer fixes are done in this chapter's S3, by hand, from the table in §4.6. That table repeats ch02-deepen §4.8's Chapter-3 rows, with a few rows added. If the Chapter 2 coordinator has already applied those rows, the drafter skips them. The S3 drafter checks with `grep -n 'Section 3\.[1-6]' src/ch03-countable-and-uncountable/*.md`.

---

## 1. Devices as applied

- **Method boxes** (STYLE §2 item 6): four. Each is `::: {#exm-method-<slug>}` titled `[Method: …]`, with the bold lead-ins **Template.**, **When to use it.** and **The usual failure.**, and each is ≤ 130 words of box text (the drafts below are ≤ 120; blueprint line pointers in them are not printed). They are `list-it` (3.1), `name-the-choice` (3.2), `diagonal` (3.3) and `injections-both-ways` (3.4), and each is linked from the index's Named moves. Three of them replace an existing named-move paragraph (01:127, 03:47–49) or the old index's Named moves (ix:22–25).
- **`[Scratch work]` ideas** (`::: {.idea}` titled `[Scratch work]`, ≤ 20 lines), one at each full box's first full appearance: `thm-product-countable` (3.1, replacing 01:217–219), `thm-countable-union` (3.2, replacing 02:113–117 and keeping its "Before reading on"), and `thm-binary-sequences-uncountable` (3.3, new; the theorem has no Idea now). 3.4 is Idea-level (layout §1), so it gets no scratch work.
- **Givens/Goal tables in prose form** (§12.5): one inside each of those three scratch works, plus one short table at the start of the "With the theorem" part of `exm-closed-open-interval` (3.4). In each, the last row shows the gap.
- **Prove or disprove** (§12.13.4): 01 B4, 02 B4, 03 B4, 04 B4. Verdicts are withheld in the stem. Solutions give the verdict first. 3.5 is not a method section and gets none.
- **Fading** (layout §1):
  - *List it* is full in 3.1: box, scratch work, and two worked examples, `exm-list-integer-combinations` (surjection) and `exm-list-two-element-subsets` (injection). In 3.2 it is a back-reference (the Idea of `thm-algebraic-countable`), and in 3.5 it is terse.
  - *Name the choice* is full in 3.2: box, scratch work, `exm-choice-or-rule`, and the existing `exm-choice-free-unions`. In 3.4 (04:65) and 3.5 (05:20) it stays as the bold "**By @ax-choice**" line, which is the template applied, with no new prose.
  - *The diagonal* is full in 3.3: box, scratch work, `exm-five-strings-diagonal`, `exm-diagonal-outgrows-list`, and Cantor's Idea, which gains a back-reference. In 3.5 it appears only in R4's solution.
  - *Injections both ways* is Idea-level in 3.4: box, one table, the two existing interval examples, and a back-reference in `exm-reals-open-interval`.
- **Threads** (layout §5):
  - *The five strings*: planted in 1.5 (1/05:202) and paid by 3.3's new opening subsection `## Back to the five strings`.
  - *Russell → Cantor*: 1.2 (1/02:441) is paid by 3.3's Cantor subsection, retitled `## Back to Russell: Cantor's theorem`, which opens with a short hook paragraph.
  - *Comparability*: 3.4 leaves it open in a `[Looking ahead]` remark at the end of its main line (replacing the remark 04:170–172), and Section 5.2 answers it.
  - *Choice*: 1.6 (1/06:251) → 3.2 `ax-choice` → 3.5 `thm-infinite-countable-subset` → Chapter 5 (Zorn).
  
  All four are listed in the index.
- **Motivation before a major definition.** The chapter has four major notions: `def-countable`, `ax-choice`, `def-decimal-expansion` and `def-card-le`. All four are already motivated: 01:7–11 (the density paradox), 02:5–22 (the naive grid, then the obstacle), 03:111–115 (what 0.999… means) and 04:3–9 (the three intervals). No change.

## 2. Section map

| § | File | Main now → budget (expected) | Changes |
|---|---|---|---|
| index | `index.md` | — | retitle; story; What you need; Time; Roadmap; Named moves (4 boxes); Threads; Summary; Terms (§4.0) |
| 3.1 | `01-countable-sets.md` | 3,610 → ≤ 5,000 (~4,250) | box; scratch work with table; subsection "Listing in practice" with 2 examples; 1 check; B4; pointers |
| 3.2 | `02-countable-unions-and-choice.md` | 3,068 → ≤ 5,000 (~3,700) | box; `exm-choice-or-rule`; scratch work with table; 1 check; Idea clause; B4; pointers |
| 3.3 | `03-diagonal-arguments.md` | 2,960 → ≤ 5,000 (~3,950) | opening subsection with `exm-five-strings-diagonal` and 1 check; scratch work with table; box; 1 check; `exm-diagonal-outgrows-list`; retitled Cantor subsection with Russell hook; Idea clause; B4; pointers |
| 3.4 | `04-comparing-cardinalities.md` | 2,398 → ≤ 4,200 (~2,680) | internal repair; box; table; `[Looking ahead]` remark; 1 check; back-reference; B4; pointers |
| 3.5 | `05-infinite-sets.md` | 1,448 → ≤ 3,700 (~1,450) | pointers; two clauses in R solutions |

## 3. Labels

**Kept, in place:** every label now in 01–05.

**New:**
- 3.1: `exm-method-list-it`, `exm-list-integer-combinations`, `exm-list-two-element-subsets`, `exr-countable-sets-b4`.
- 3.2: `exm-method-name-the-choice`, `exm-choice-or-rule`, `exr-countable-unions-and-choice-b4`.
- 3.3: `exm-five-strings-diagonal`, `exm-method-diagonal`, `exm-diagonal-outgrows-list`, `exr-diagonal-arguments-b4`.
- 3.4: `exm-method-injections-both-ways`, `exr-comparing-cardinalities-b4`.

**Titles.** The `#` titles of 03 and 04 are kept ("Diagonal Arguments: Uncountable Sets and Cantor's Theorem", "Comparing Sizes: the Schröder–Bernstein Theorem"). The layout's shorter forms are abbreviations in its table, and Chapter 1 kept its full titles in the same way.

---

## 4. Per-section plans

### 4.0 `index.md` (coordinator, last, against the delivered sections)

- **Title** `# Countable and Uncountable Sets`.
- **¶1 (ix:3).** "The answer is in Section 3.4" → "Section 3.3". Add a last sentence: "Each section teaches one method of proof on the way: list a set, name the choices a proof makes, run a diagonal, and compare sizes by injections both ways."
- **¶2 (ix:5).** The last sentence ("The finite sets come first, …") → "It starts from the finite sets of Section 2.5 and the pigeonhole principle."
- **What you need (ix:7).** "Chapters 1–2" is kept. Add to the Chapter 1 list the boxes @exm-method-injectivity and @exm-method-surjectivity. Add to the Chapter 2 list: equinumerous and finite sets (@def-equinumerous, @def-finite, @def-infinite), pigeonhole (@thm-pigeonhole, @cor-pigeonhole-finite-sets), subsets and disjoint unions (@prp-subset-finite, @prp-disjoint-union-count), no proper copy (@thm-finite-no-proper-copy, @exm-hilbert-hotel), @prp-power-set-count, @prp-finite-max, and the boxes @exm-method-least-element and @exm-method-pigeonhole. From *Logic and Proof*, add @fd1:thm-sqrt2-irrational (used in `exm-list-integer-combinations`). Renumber: "Section 3.3 shows why one use of ∃E" → 3.2; "Section 3.4 states three school facts" → 3.3; "Sections 3.4–3.5 use them" → 3.3–3.4; "Section 3.3 uses one fact from school algebra" → 3.2.
- **Time.** "About 25 hours on the core track …; about 30 hours for everything" (layout §2), recomputed after S3 (§5).
- **Roadmap** (five bullets). Drop ix:13 (finite sets, now 2.5). Keep ix:14–18, and end each bullet with its method:
  - 3.1 "…; the method: list a set, by a surjection from ℕ or an injection into ℕ."
  - 3.2 "…; the method: name each choice a proof makes."
  - 3.3 "…, opening with the five-string game of Section 1.5; the method: the diagonal."
  - 3.4 "…; the method: injections both ways; whether any two sets are comparable is left open."
  - 3.5 unchanged.
- **Named moves (ix:20–25).** Four lines, in section order, each linking its box. Each line keeps the substance of the old entry, shortened to one sentence. Order: list it (3.1), name the choice (3.2), the diagonal (3.3), injections both ways (3.4).
- **Threads** (new, after Named moves), four bullets:
  - *The five strings.* "Section 1.5 plants a game: write a string of five symbols not on a given list of five. Section 3.3 opens with the rule that always works, and the same rule, run on infinitely long strings, proves that the 0–1 sequences cannot be listed."
  - *Russell to Cantor.* "Russell's theorem (Section 1.2) built a set that disagrees with each candidate on the candidate itself; Cantor's theorem (Section 3.3) is the same construction, as a theorem about sizes."
  - *Choice.* "Section 1.6 could not build a right inverse of an arbitrary surjection; Section 3.2 adds the axiom of choice that does, Section 3.5 uses it again, and Chapter 5 states its strongest everyday form, Zorn's lemma."
  - *Comparability.* "Section 3.4 asks whether any two sets are comparable and leaves the question open; Section 5.2 answers it."
- **Summary** (new, ≤ 180 words). Countable means listable (@def-countable). There are three equivalent forms (@thm-countable-characterizations), and countable sets are closed under subsets, images, finite products and, with the axiom of choice, countable unions (@thm-countable-union). So ℤ, ℚ and the algebraic numbers are countable. The diagonal shows that the 0–1 sequences, ℝ and every power set are too big (@thm-binary-sequences-uncountable, @thm-reals-uncountable-decimal, @thm-cantor), and that transcendental numbers exist. Sizes compare by injections, and injections both ways give a bijection without choice (@thm-schroder-bernstein). Every infinite set contains a copy of ℕ (@thm-infinite-countable-subset, by choice) and has a proper subset of its own size. **Open:** whether any two sets are comparable (Chapter 5). **Next:** Chapter 4 studies relations, and "same size" returns there as an example.
- **Terms** (new, alphabetical, one line each):
  - algebraic number (02, prose definition before `thm-algebraic-countable`, linked by section);
  - at most as big as / strictly smaller (@def-card-le);
  - choice function (@ax-choice);
  - countable (@def-countable);
  - countably infinite (@def-countably-infinite);
  - decimal expansion (@def-decimal-expansion);
  - digit sequence (@def-decimal-expansion);
  - transcendental number (03, prose, linked by section);
  - uncountable (@def-countable).

### 4.1 Section 3.1: Countable Sets (`01`)

Budget: 3,610 → ≤ 5,000 (expected ~4,250). No folds.

1. **Pointers:** the 01 rows of §4.6.
2. **01:127 is replaced** (42 words) by one lead sentence, "Which form to use is the first decision in every countability proof:", followed by **`exm-method-list-it`** `[Method: list it]`.
   - **Template.** To show that A is countable, give one of two maps and check it. *(S)* A surjection onto A from ℕ or from a countable set: check that every a ∈ A is a value (repetitions are free; split off A = ∅), then cite @def-countable or @prp-countable-image. *(I)* An injection of A into ℕ or into a countable set: check that equal values come from equal elements, then cite @thm-countable-characterizations, (ii) ⇒ (i).
   - **When to use it.** (S) when A is "all objects of the form φ(m, n, …)": list the parameters. (I) when each element carries a code that can be read back, above all when a parametrization would leave A.
   - **The usual failure.** A list that runs through an infinite block before the next (@exm-rows-first-listing). An "injection" whose injectivity is never checked. (Concluding "uncountable" from one failed list is already the warning at 01:35.)
3. **Quick check** after the box.
   - "Which route of the method would you take for (a) the set of numbers n² + 3n with n ∈ ℕ; (b) the set of pairs (q, n) ∈ ℚ × ℕ with q·n ∈ ℤ?"
   - *Solution:* (a) (S): the set is the image of n ↦ n² + 3n, so @prp-countable-image applies and nothing is left to check. (b) (I): the inclusion into ℚ × ℕ is an injection with nothing to check, and ℚ × ℕ is countable (@thm-integers-rationals-countable, @cor-product-countable (a)); this is @prp-countable-subset. No parametrization of the set is needed.
4. **`thm-product-countable`.** The Try-it-first (01:215) is kept. The Idea 01:217–219 (~150 words) is replaced by a **`[Scratch work]`** idea (≤ 18 lines). It keeps the old Idea's content in order: the rows-first list fails; the diagonal list works but is costly to write down; route (I) of @exm-method-list-it is cheaper; the code 2^m 3^n; parity, not unique factorization, reads it back. Insert the table after "an injection only has to be a code":

   | Givens | Goal |
   |---|---|
   | — | ℕ × ℕ countable |
   | @thm-countable-characterizations (ii) ⇒ (i) | an injection p: ℕ × ℕ → ℕ |
   | p(m, n) = 2^m 3^n, and 2^m 3^n = 2^{m′} 3^{n′} | m = m′ and n = n′ |
   | suppose m > m′ (symmetry); cancel 2^{m′}: 2^{m−m′} 3^n = 3^{n′} | gap: an even number equals an odd one, which is impossible (the claim in @prp-union-two-countable); so m = m′, and then n = n′ because k ↦ 3^k is increasing |

   The proof is unchanged.
5. **New subsection `## Listing in practice`**, after 01:302 (end of the section, before `## Exercises`). Lead (one sentence): "Two more uses of @exm-method-list-it, one by each route."
   - **`exm-list-integer-combinations`** `[Integer combinations of 1 and √2]`. "Let S ≔ {m + n√2 : m, n ∈ ℤ}. Show that S is countably infinite."
     - *Solution:* "Route (S). The map ℤ × ℤ → S, (m, n) ↦ m + n√2, is onto by the definition of S, and ℤ × ℤ is countable (@thm-integers-rationals-countable, @cor-product-countable (a)). So S is countable by @prp-countable-image. It is infinite: ℕ ⊆ S (take n = 0 and m ∈ ℕ), and ℕ is infinite (@exm-hilbert-hotel), so S is not finite by @prp-subset-finite. By @thm-countable-characterizations, (i) ⇒ (iii), S is countably infinite."
     - *Aftermath (≤ 55 words):* "Route (I) would need the map to be injective. If m + n√2 = m′ + n′√2 with n ≠ n′, then √2 = (m − m′)/(n′ − n) would be rational, against @fd1:thm-sqrt2-irrational. So route (I) works here, but it costs a theorem. Route (S) never asks whether two parameter pairs give the same number."
   - **`exm-list-two-element-subsets`** `[Coding the two-element subsets of ℕ]`. "Let P₂ be the set of subsets of ℕ with exactly two elements. Show that P₂ is countably infinite."
     - *Scratch (two sentences, in the solution):* "Route (S) from ℕ × ℕ, (m, n) ↦ {m, n}, leaves P₂ when m = n, the usual failure of the box. Route (I) needs a code from which S can be read back, and a two-element set has a least and a largest element."
     - *Solution:* "Let S ∈ P₂. By @def-finite, S = {s, t} with s ≠ t, and by trichotomy one of them is smaller. Write min S and max S for the smaller and the larger. They are named by a rule, so no choice is made. Define c(S) ≔ 2^{min S} 3^{max S}, that is, c(S) = p(min S, max S) with p of @thm-product-countable. If c(S) = c(T), then (min S, max S) = (min T, max T), since p is injective, and so S = {min S, max S} = T. By (ii) ⇒ (i), P₂ is countable. It is infinite: n ↦ {0, n + 1} is an injection ℕ → P₂ (the sets differ in their larger elements), so P₂ contains a copy of ℕ, and a set with a subset equinumerous with ℕ is not finite (@exm-hilbert-hotel, @prp-equinumerous-properties, @prp-subset-finite). By (i) ⇒ (iii), P₂ is countably infinite."
6. **B4** `[B4: Prove or disprove]`.
   - (a) The set of all functions {0, 1} → ℕ is countable.
   - (b) If A is countable and there is an injection ℕ → A, then A is countably infinite.
   - (c) If f: A → B is an injection and B is countably infinite, then A is countably infinite.
   - (d) For every countable set A there is a surjection ℕ → A.
   - (e) If A and B are countably infinite, then A ∪ B is countably infinite.
   - *Solution:*
     - (a) True. f ↦ (f(0), f(1)) is injective into ℕ × ℕ, since two functions on {0, 1} with the same two values are equal (@prp-function-equality). Composed with p of @thm-product-countable it is an injection into ℕ. Countable by (ii) ⇒ (i).
     - (b) True. Let j: ℕ → A be injective. Then ℕ is equinumerous with j(ℕ) ⊆ A. If A were finite, j(ℕ) would be finite (@prp-subset-finite), and so would ℕ (compose the bijections), against @exm-hilbert-hotel. So A is countable and not finite, and countably infinite by @thm-countable-characterizations, (i) ⇒ (iii).
     - (c) False. A = {0}, B = ℕ, with the inclusion: A is finite.
     - (d) False. A = ∅ is countable, and there is no function ℕ → ∅ at all (@prp-empty-function (b)).
     - (e) True. A ∪ B is countable by @prp-union-two-countable. It is not finite, since it contains the infinite set A (@prp-subset-finite). Countably infinite by (i) ⇒ (iii).

Count: +box 130 + check 95 + scratch net +90 + subsection ~420 − 42 ≈ +690 → ~4,300.

### 4.2 Section 3.2: Countable Unions and the Axiom of Choice (`02`)

Budget: 3,068 → ≤ 5,000 (expected ~3,700). No folds.

1. **Pointers:** the 02 rows of §4.6, including 02:47: "A later chapter states its best-known equivalent, Zorn's lemma" → "Chapter 5 states its best-known equivalent, Zorn's lemma", and "in Section 3.6" → "in Section 3.5". In the same paragraph the two history sentences ("It is independent … Cohen (1963) that it cannot be proved from them.") become one line (STYLE §1): "It can be neither proved nor refuted from the other axioms of set theory (Gödel, Cohen)." The rest of 02:47 is kept.
2. **`exm-method-name-the-choice`** `[Method: name the choice]`, after the warning 02:69–71 (end of "When choice is not needed"). Lead: "The warning is the whole method; here it is as a checklist."
   - **Template.** At each line that produces an object for each of many indices at once, ask whether one rule names it for every index: a formula, "the least", "the unique", or one list fixed in advance. If so, define the function by specification and say that no choice is used. If not, form the family (S_i) of non-empty sets of candidates and write "**by @ax-choice** there is c with c(i) ∈ S_i" at that line, in bold.
   - **When to use it.** A proof says "for each n, let …", builds a sequence or a family of lists, or inverts a surjection.
   - **The usual failure.** An unflagged "for each n, choose". Flagging a single ∃E, or a rule, as a use of the axiom. An empty S_i left in the family, so that the axiom's hypothesis fails (02:59).
3. **Quick check** after the box.
   - "A proof says: 'For each n ∈ ℕ the set {k ∈ ℕ : k² > n} is non-empty; choose k_n in it.' Does this line need @ax-choice? Rewrite it so that it plainly does not."
   - *Solution:* No: it need not. The least element (@thm-well-ordering) names k_n, and so does the formula k_n ≔ n + 1, since (n + 1)² = n² + 2n + 1 > n. Either rewrite defines n ↦ k_n by specification.
4. **`exm-choice-or-rule`** `[Choice or a rule?]`, after the check and before `## Right inverses`. This is the method's first worked example, and `exm-choice-free-unions` (02:149–165) is its second. The parts avoid 02 B1's intervals (n, n + 1), subsets of ℕ, subsets of ℝ and square roots. "Which of the following needs @ax-choice?"
   - (a) A function sending each non-empty finite set of reals to one of its elements.
   - (b) A function sending each open interval (a, b) of reals, a < b, to a rational number in it.
   - (c) A function sending each countably infinite subset A ⊆ ℝ to a bijection ℕ → A.
   - (d) For a given family (A_n)_{n∈ℕ} of non-empty subsets of ℚ, a sequence with a_n ∈ A_n for every n.
   - *Solution:*
     - (a) No: S ↦ max S, by @prp-finite-max.
     - (b) No, once one list of ℚ is fixed. Take a surjection q: ℕ → ℚ (@thm-integers-rationals-countable, one ∃E). Between two reals lies a rational (a school fact; *Analysis on the Real Line*, Chapter 1 proves it), so {n ∈ ℕ : a < q(n) < b} is non-empty, and q of its least element (@thm-well-ordering) is named by a rule.
     - (c) Yes, as far as this book is concerned. Each A has bijections ℕ → A (@def-countably-infinite), but no rule names one for an arbitrary A. The family (S_A) of sets of bijections, indexed by the countably infinite subsets of ℝ, consists of non-empty sets, and @ax-choice gives the function.
     - (d) No: with the same fixed q, a_n ≔ q(min{k ∈ ℕ : q(k) ∈ A_n}). (No comparison with 02 B1 (c) is printed: it would rest on 3.3.)
     - Closing sentence: "One fixed list turns 'pick an element' into 'take the first one on the list', and that is a rule."
5. **`thm-surjection-right-inverse`, Idea (02:83–85).** Add the last sentence: "This is the method of @exm-method-name-the-choice: for an arbitrary f no rule names a preimage, so the line is flagged."
6. **`thm-countable-union`.** The Idea 02:113–117 is replaced by a **`[Scratch work]`** idea (≤ 20 lines). It keeps ①–③ and the "Before reading on" line. The table:

   | Givens | Goal |
   |---|---|
   | A_n countable for every n | ⋃ A_n countable |
   | J ≔ {n : A_n ≠ ∅}; J × ℕ countable (@cor-product-countable) | a surjection F: J × ℕ → ⋃ A_n |
   | for each single n ∈ J: some surjection ℕ → A_n (one ∃E per n) | F(n, m) ≔ (a list of A_n)(m), which needs every list at once, as one function n ↦ c(n) |
   | gap: from "∀n ∃ a list" to "∃ one function giving a list for every n" | closed by @ax-choice on (S_n)_{n∈J}, the only flagged line |

   The proof is unchanged.
7. **`thm-algebraic-countable`, Idea (02:187–189).** Add: "Steps 2 and 3 are route (S) of @exm-method-list-it: each union is the image of a countable grid. Step 1 only cites closure under products and subsets."
8. **B4** `[B4: Prove or disprove]`.
   - (a) If A_n is finite for every n ∈ ℕ, then ⋃_{n∈ℕ} A_n is countable.
   - (b) If A_n is finite for every n ∈ ℕ, then ⋃_{n∈ℕ} A_n is finite.
   - (c) Every surjection f: ℕ → Y has a right inverse that can be defined without @ax-choice.
   - (d) If A_n is countable for every n ∈ ℕ, then ⋃_{n∈ℕ} A_n is countably infinite.
   - (e) If A_n ≠ ∅ for every n ∈ ℕ and ⋃_{n∈ℕ} A_n is finite, then A_m ∩ A_n ≠ ∅ for some m ≠ n.
   - *Solution:*
     - (a) True. Finite sets are countable (@thm-countable-characterizations, (iii) ⇒ (i)), and @thm-countable-union (a) applies.
     - (b) False. A_n ≔ {n}: the union is ℕ, which is infinite (@exm-hilbert-hotel).
     - (c) True. g(y) ≔ min f⁻¹({y}), which exists by @thm-well-ordering since f is onto, is a rule. Then f(g(y)) = y.
     - (d) False. A_n ≔ {0} for every n: the union is {0}.
     - (e) True, with no axiom. U ≔ ⋃ A_n is non-empty (it contains A₀) and finite, say with k elements via a bijection φ: {1, …, k} → U (one ∃E). Define c(n) ≔ φ(min{j : φ(j) ∈ A_n}). This is a rule, and c(n) ∈ A_n. If c were injective, ℕ would be equinumerous with c(ℕ) ⊆ U, which is finite (@prp-subset-finite). Then ℕ would be finite, against @exm-hilbert-hotel. So c(m) = c(n) for some m ≠ n, and that element lies in A_m ∩ A_n. This is the pigeonhole idea of @exm-method-pigeonhole, with infinitely many pigeons.

Count: box 130 + check 75 + example ~330 + clauses 40 + scratch net +90 ≈ +665 → ~3,730.

### 4.3 Section 3.3: Diagonal Arguments (`03`)

Budget: 2,960 → ≤ 5,000 (expected ~3,950). No folds.

1. **Pointers:** the 03 rows of §4.6.
2. **03:3** (frame paragraph): "by one argument used three times" → "by one argument, which starts from the game of Section 1.5 and is then used three times". The list of the three uses is kept.
   **New first subsection `## Back to the five strings`**, between 03:3 and 03:5. Lead (≤ 40 words): "Section 1.5 left a game open: one player lists five strings of five symbols 0 or 1, and the other must write a string that is not on the list. Searching all 32 strings works; a rule is better." Then:
   - **`exm-five-strings-diagonal`** `[Back to the five strings]`. "Find a rule that, from any list s₁, …, s₅ of strings of five symbols 0 or 1, builds a string not on the list. Run it on 00000, 11111, 01010, 10101, 00111, and prove that it always works."
   - *Solution:* "Let the new string g have, as its k-th symbol, the flip of the k-th symbol of the k-th string: g(k) ≔ 1 − s_k(k) for k = 1, …, 5 (strings are functions {1, …, 5} → {0, 1}, Section 1.5). On the list, the symbols s₁(1), …, s₅(5) are 0, 1, 0, 0, 1, so g = 10110. It differs from 00000 in place 1, from 11111 in place 2, from 01010 in place 3, from 10101 in place 4 and from 00111 in place 5. For any list: for each k, g(k) ≠ s_k(k), since 1 − b ≠ b for b ∈ {0, 1}. So g ≠ s_k (@prp-function-equality), for k = 1, …, 5. The k-th step looks only at the k-th string, in its own place k."
   - *Aftermath (≤ 45 words):* "The rule never used the number 32. It used one place for each string on the list. Give the strings infinitely many places, indexed by ℕ, and let the list be infinite too, and the same rule still applies."
   - **Quick check:** "Can the rule handle a list of six strings of five symbols? Does that contradict anything?" *Solution:* No. The sixth string has no sixth place to be flipped in. Nothing is contradicted: a list of 32 strings may contain every string. The rule needs as many places as strings, and in the next subsection both are indexed by ℕ.
3. **03:7.** "Recall from Section 1.5 that" is kept; add after its first sentence: "These are the strings of the game with places indexed by ℕ."
4. **`thm-binary-sequences-uncountable`** gets a **`[Scratch work]`** idea between statement and proof (≤ 14 lines):

   | Givens | Goal |
   |---|---|
   | f: ℕ → {0, 1}^ℕ arbitrary | f is not onto; and {0, 1}^ℕ ≠ ∅ |
   | — | some g ∈ {0, 1}^ℕ with g ≠ f(n) for every n |
   | g ≠ f(n) as soon as g and f(n) differ at one place (@prp-function-equality) | pick the place for each n: place n, as in the game |
   | gap: g(n) ≠ f(n)(n) for every n | closed by g(n) ≔ 1 − f(n)(n) |

   Then one sentence: "The proof writes this forwards."
5. **03:47–49** ("This is the move of the section, …" and the bold paragraph) are replaced by **`exm-method-diagonal`** `[Method: the diagonal]`, with the lead "This is the move of the section."
   - **Template.** To show that no map from I onto X exists (for "uncountable": I = ℕ, and check X ≠ ∅), let f: I → X be arbitrary. Build d ∈ X whose entry at i differs from the entry of f(i) at i, for every i ∈ I. Then d ≠ f(i) for each i, so f is not onto. Since f was arbitrary, no such map exists.
   - **When to use it.** The elements of X are themselves functions or subsets on the index set of the list: sequences, digit strings, subsets of I.
   - **The usual failure.** A d that falls outside X (a decimal ending in 9s, 03:189; a sequence of the wrong kind). A difference at place i that is not a real difference (two expansions of one number). Running the construction on one list only (the warning 03:59–61).
6. **Quick check** after the box (the existing check 03:51–57 stays after it).
   - "Would the unflipped diagonal, g(n) ≔ f(n)(n), do? Test it on the list whose every entry is the zero sequence."
   - *Solution:* No. There g is the zero sequence, which is f(0). The new object must differ from the n-th entry at place n, for every n.
7. **`exm-diagonal-outgrows-list`** `[A function that outgrows a list]`, after the warning 03:59–61 (end of the first subsection). "Let f₀, f₁, f₂, … be any list of functions ℕ → ℕ. Find g: ℕ → ℕ such that, for every k ∈ ℕ, g(n) > f_k(n) for every n ≥ k."
   - *Idea line (in the solution):* "The flipped diagonal beats f_n at place n only. To beat f_k from place k on, let place n beat f₀, …, f_n at once: finitely many, so a maximum exists."
   - *Solution:* "Let g(n) ≔ max{f₀(n), …, f_n(n)} + 1. The set is {x₁, …, x_{n+1}} with x_{k+1} ≔ f_k(n), so the maximum exists by @prp-finite-max, and g(n) ∈ ℕ. For k ∈ ℕ and n ≥ k, f_k(n) is one of the numbers in the set, so f_k(n) ≤ max < g(n). The example asks more of g than a diagonal does, and each step still looks at finitely many entries at one place."
   - The text never states that g differs from each f_k, nor that g is off the list: that inference is 03 B1's blank, which stays the reader's.
8. **Cantor subsection, the Russell payoff.** Retitle 03:63 `## Cantor's theorem` → `## Back to Russell: Cantor's theorem` (layout §5: each thread is paid by a "Back to …" subsection). Before 03:65, add one hook paragraph (≤ 45 words), no bold lead-in: "Section 1.2 proved Russell's theorem (@thm-russell): the set R_A disagrees with each candidate x ∈ A about x itself, so it is not in A. Here the same disagreement becomes a theorem about sizes." 03:65 is kept. 03:91 (consequence (i)) is kept as it stands and makes the precise identification; the hook does not repeat it.
9. **`thm-cantor`, Idea (03:76).** Append: "It is the method of @exm-method-diagonal, with the rows and the places both indexed by X."
10. **B4** `[B4: Prove or disprove]`.
    - (a) The set of periodic 0–1 sequences, those a ∈ {0, 1}^ℕ with some p ≥ 1 such that a(n + p) = a(n) for every n ∈ ℕ, is uncountable.
    - (b) The set of 0–1 sequences with no two consecutive 1s is uncountable.
    - (c) For every set X there is no injection 𝒫(X) → X.
    - (d) If X is infinite, there is no surjection X → X × X.
    - (e) The set of all functions ℤ → {0, 1} is uncountable.
    - *Solution:*
      - (a) False: the set is countable. Let P_p be the set of sequences with period p ≥ 1. For a ∈ P_p, a(qp + r) = a(r) for all q ∈ ℕ and 0 ≤ r < p, by induction on q. Every n ∈ ℕ is qp + r for such q and r (@thm-division-algorithm). So a is determined by a(0), …, a(p − 1), and a ↦ a|_{{0,…,p−1}} is an injection of P_p into the finite set of functions {0, …, p − 1} → {0, 1} (2^p elements, @prp-power-set-count via indicators). So P_p is countable, and the set of periodic sequences, ⋃_{p∈ℤ_{>0}} P_p, is countable by @thm-countable-union (b). No choice is involved: each P_p is listed by a rule (order the 2^p patterns lexicographically), so the union is listed without @ax-choice, as in @exm-choice-free-unions. The diagonal fails here because the flipped diagonal of a list of periodic sequences need not be periodic: the usual failure of @exm-method-diagonal.
      - (b) True. b ↦ a with a(2n) ≔ b(n) and a(2n + 1) ≔ 0 sends {0, 1}^ℕ into the set (every odd place is 0, so no two consecutive places are both 1), and it is injective (b is read back from the even places, @prp-function-equality). If the set were countable, composing with its injection into ℕ would give an injection {0, 1}^ℕ → ℕ, so {0, 1}^ℕ would be countable (@thm-countable-characterizations, (ii) ⇒ (i)), against @thm-binary-sequences-uncountable.
      - (c) True. Let i: 𝒫(X) → X be injective. Since 𝒫(X) ∋ ∅ is non-empty, i has a left inverse r: X → 𝒫(X) (@thm-left-inverse-iff-injective (b)). r ∘ i = id says that i is a right inverse of r, so r is surjective (@prp-right-inverse-surjective), against @thm-cantor.
      - (d) False. X = ℕ: ℕ × ℕ is countable (@thm-product-countable) and non-empty, so @def-countable gives a surjection ℕ → ℕ × ℕ.
      - (e) True. Restriction a ↦ a|_ℕ maps {0, 1}^ℤ onto {0, 1}^ℕ: a given b extends by 0 on the negative integers. If {0, 1}^ℤ were countable, its image {0, 1}^ℕ would be countable (@prp-countable-image), against @thm-binary-sequences-uncountable.

Count: subsection ~330 (with check) + scratch ~140 + box net +90 + check 55 + example ~230 + Russell 85 + clause 15 ≈ +945 → ~3,905.

### 4.4 Section 3.4: Comparing Sizes (`04`)

Budget: 2,398 → ≤ 4,200 (expected ~2,680). No folds. Idea-level (layout §1): box, one table, back-references; no scratch work.

1. **Pointers:** the 04 rows of §4.6.
2. **Internal repair, 04:52** (layout §3.2; the wording of ch02-deepen §4.8). "As with equinumerosity (Section 3.1, after @prp-equinumerous-properties), we do not call this a partial order: … And antisymmetry, the clause (PO2) of @def-partial-order, would say" becomes: "As with equinumerosity (Section 2.5, after @prp-equinumerous-properties), comparing sizes is reflexive and transitive (@prp-card-le-preorder), but we do not call it an order: there is no set of all sets for it to be a relation on (@thm-russell). And the clause one would expect next, the analogue of x ≤ y ≤ x ⇒ x = y for numbers, would say". The rest of 04:52 is kept. `prp-card-le-preorder` (04:35–50) already states reflexivity and transitivity directly. The section cites no Chapter 4 label after this.
3. **`exm-method-injections-both-ways`** `[Method: injections both ways]`, after 04:168 ("Each hypothesis is used. …"). Lead: "In practice the theorem is used as a method."
   - **Template.** To show |A| = |B|, write an injection f: A → B and an injection g: B → A, check each one separately, and cite @thm-schroder-bernstein. Often one map is an inclusion and the other squeezes B into a part of A. Do not hunt for the bijection: the theorem builds it.
   - **When to use it.** A and B differ by "a little" (endpoints, a countable piece, a factor), so that a bijection would need cases; or A sits inside B, and B fits back into A.
   - **The usual failure.** Two injections in the same direction. One injection that is not onto, read as strictness or as a bijection (the warning 04:30, 04:232). A squeeze whose values leave the target (x ↦ x/2 sends [0, 1] into [0, ½] and hits 0 ∉ (0, 1)).
4. **Quick check** after the box.
   - "Show |[0, 1] ∪ {5}| = |[0, 1]| by the method."
   - *Solution:* The inclusion [0, 1] → [0, 1] ∪ {5} is injective. In the other direction, take x ↦ x/2 on [0, 1] and 5 ↦ 1. Since 5 ∉ [0, 1], the two clauses define a function into [0, 1]. It is injective, since x/2 ≤ ½ < 1. By @thm-schroder-bernstein the sets are equinumerous.
5. **The comparability remark (04:170–172)** is removed from mid-section, and its content moves to a `::: {.remark}` titled `[Looking ahead]` at the end of 3.4's main line, just before `## Exercises` (STYLE §12.1's form; ≤ 90 words), the thread's hook: "The method needs an injection each way. Are any two sets comparable, that is, is |A| ≤ |B| or |B| ≤ |A| for all A and B? Building an injection one element at a time does not settle it: a recursion indexed by ℕ reaches only countably many elements, so it cannot exhaust an uncountable set. Section 5.2 proves that the answer is yes, by Zorn's lemma, a principle equivalent to @ax-choice. Nothing in this chapter needs comparability."
6. **`exm-closed-open-interval`, "With the theorem" (04:185).** Before its first sentence, add the table (with the lead "Planned as in @exm-method-injections-both-ways:"):

   | Givens | Goal |
   |---|---|
   | (0, 1) ⊆ [0, 1] | |[0, 1]| = |(0, 1)| |
   | the inclusion (0, 1) → [0, 1], injective | an injection [0, 1] → (0, 1) |
   | gap: squeeze [0, 1] into a closed interval inside (0, 1) | u(x) ≔ x/2 + 1/4, with values in [¼, ¾] |

   The rest of the solution is unchanged.
7. **`exm-reals-open-interval`, last part (04:226).** "By @thm-schroder-bernstein" → "By the method of @exm-method-injections-both-ways (@thm-schroder-bernstein)".
8. **B4** `[B4: Prove or disprove]`.
   - (a) |ℤ| < |ℚ|.
   - (b) If |A| < |B| and |B| ≤ |C|, then |A| < |C|.
   - (c) If |A| ≤ |B| and B is countable, then A is countable.
   - (d) |{0, 1}^ℕ| = |ℕ^ℕ|, where ℕ^ℕ is the set of functions ℕ → ℕ.
   - (e) If A ⊆ B and |B| ≤ |A|, then |A| = |B|.
   - *Solution:*
     - (a) False. Both are countably infinite (@thm-integers-rationals-countable), so |ℤ| = |ℕ| = |ℚ| (@prp-equinumerous-properties), and there is a bijection ℤ → ℚ.
     - (b) True. |A| ≤ |C| by @prp-card-le-preorder (b). Suppose there were a bijection φ: A → C. Composing an injection B → C with φ⁻¹ gives |B| ≤ |A|. With |A| ≤ |B|, @thm-schroder-bernstein gives |A| = |B|, against |A| < |B|.
     - (c) True. Compose the injection A → B with an injection B → ℕ (@thm-countable-characterizations, (i) ⇒ (ii)); the composite is injective, and (ii) ⇒ (i) gives A countable.
     - (d) True, by the method. *Into ℕ^ℕ:* a ↦ a, read with codomain ℕ, is injective (same values). *Back:* f ↦ its graph Γ_f ⊆ ℕ × ℕ is injective into 𝒫(ℕ × ℕ) (@prp-function-equality). S ↦ p(S), the image under the injective p(m, n) = 2^m 3^n of @thm-product-countable, is injective 𝒫(ℕ × ℕ) → 𝒫(ℕ): if p(S) = p(T) and x ∈ S, then p(x) = p(y) for some y ∈ T, so x = y ∈ T, and symmetrically. S ↦ 𝟙_S is injective 𝒫(ℕ) → {0, 1}^ℕ. Compose the three (@prp-card-le-preorder (b)) and apply @thm-schroder-bernstein.
     - (e) True. The inclusion gives |A| ≤ |B|, and @thm-schroder-bernstein applies.

Count: box 120 + check 70 + remark net +20 + table 60 + clause 5 ≈ +270 → ~2,670.

### 4.5 Section 3.5: Infinite Sets (`05`)

Terse (layout §1). Main line unchanged except pointers (~1,450).

1. **Pointers:** the 05 rows of §4.6.
2. **`exr-infinite-sets-r1`, solution.** After "By @thm-well-ordering it has a least element \( m \).", add "(the method of @exm-method-least-element)". The solution text is otherwise kept.
3. **`exr-infinite-sets-r4`, solution, "Why the look-alike fails".** The last sentence becomes: "A diagonal argument proves uncountability only when the diagonal object stays inside the set; this is the usual failure named in @exm-method-diagonal."
4. **R items, coverage check (no change).** R1 reaches back to Chapter 2 (strong induction, least element), R2 and R3 to *Logic and Proof* (counter-models, truth functions, with 2.5's power-set count), and R4 within Chapter 3. Layout §1's "R items reach back over Ch1–3 and fd1" is met. To reach Chapter 1 by method, not only vocabulary: in `exr-infinite-sets-r3`'s solution, the sentence that checks the bijection L → 𝒫({1, …, n}) gains the clause "(injective and surjective by @exm-method-injectivity and @exm-method-surjectivity)". If R3's solution has no such check, the drafter adds the clause where the bijection is asserted. No problem text names its source (STYLE §11.5); none does now.

### 4.6 Pointers inside the chapter (S3 drafter, by hand)

Section map for old-numbered text: 3.1 → 2.5, 3.2 → 3.1, 3.3 → 3.2, 3.4 → 3.3, 3.5 → 3.4, 3.6 → 3.5. Chapter 1 pointers (Sections 1.2–1.6) are already in final numbering (Ch1 S3 sweep) and are not touched.

| File:line | Now | Becomes |
|---|---|---|
| 01:3 | "Section 3.1 made 'the same size' exact …" | "Section 2.5 made …" |
| 01:33, 01:35 (first), 01:47, 01:112, 01:150 | Section 3.1 | Section 2.5 |
| 01:35 (second) | Section 3.4 | Section 3.3 |
| 01:125, 01:183, 01:274, 01:302 | Section 3.3 | Section 3.2 |
| 01:271 | "Exercise C2 (a) of Section 3.1" | "@exr-finite-sets-c2 (a)" |
| 01, `exr-countable-sets-c1` solution, Step 4 (01:443) | "the remark at the end of Section 3.1" | "the remark at the end of Section 2.5" |
| 02:3, 02:11, 02:114 | Section 3.2 | Section 3.1 |
| 02:47 | "A later chapter states …"; "in Section 3.6" | "Chapter 5 states …"; "in Section 3.5" |
| 02:139, 02:201 | Section 3.4 | Section 3.3 |
| 03:93 | Section 3.5 | Section 3.4 |
| 03:195 | Section 3.3 | Section 3.2 |
| 04:3, 04:17 | Section 3.1 | Section 2.5 |
| 04:52 | repair | §4.4 item 2 |
| 04:171 | "a later chapter devoted to Zorn's lemma" | replaced (§4.4 item 5, "Section 5.2") |
| 04:240 | Section 3.2 | Section 3.1 |
| 04:335 (`exr-comparing-cardinalities-c1` stem) | Section 3.4 | Section 3.3 |
| 05:3 | Section 3.5 | Section 3.4 |
| 05:71, 05:80, 05:103 | Section 3.1 | Section 2.5 |
| ix | | §4.0 |

**Kept** (correct as they stand): 01:278 ("Section 2.1"), 01:377 ("Section 2.2 sets it aside"), 01:431 ("Section 2.3"); every "Section 1.k" in 01–05; the fd1 pointers (03:204, 03:208, 04:166, 05:281).

**Dependency-ledger tags** (the closing `<!-- dependency ledger -->` comments of 01–05; evidence prose that no checker reads). Some tags carry pre-re-cut numbers: "F2.3 §01" means finite sets (now F2.2 §05); "F2.3 §0k" for k ≥ 2 means the old 3.k (now §0(k−1)); several "F2.1 §0k" are old Chapter 1 numbers (now §0(k+1)). Old and new numbers cannot be told apart by tag alone (e.g. "F2.1 §05"), so the S4 coordinator re-keys each tag by the label or fact it names, with `tools/ledger.py`, together with `authoring/ledger/ch03.yaml`.

## 5. Budgets and Time

| § | Main now | Budget | Expected | Folds |
|---|---|---|---|---|
| 3.1 | 3,610 | 5,000 | ~4,300 | 0 |
| 3.2 | 3,068 | 5,000 | ~3,730 | 0 |
| 3.3 | 2,960 | 5,000 | ~3,905 | 0 |
| 3.4 | 2,398 | 4,200 | ~2,670 | 0 |
| 3.5 | 1,448 | 3,700 | ~1,450 | 0 |
| total | 13,484 | 22,900 | ~16,055 | 0 |

**Exercises.** Four new B4s; the chapter goes from 35 to 39 exercises. The core track is all A, one B and one C per section, and the exit checks: about 16 items. The current index reads 30 h core and 40 h full, at 24,372 whole-file words and 35 exercises (about 45 min per exercise on the full track). After S3 the files hold about 27,500–28,000 words (main line +2,570, the four B4 solutions about +1,000, small clauses) and 39 exercises, four of them five-part. At the index's rates that projects **about 30 h core and 45 h full**. The Time can only rise. The coordinator recomputes with `check_structure.py --words` and the index's per-exercise rate after S3 and reports the full-track overrun against layout §2's 25/30 to the author as a departure (§8 item 2), as Chapter 1 did.

## 6. Pointers, promises, edits outside the chapter

Not edited by this chapter's drafters. Listed for the coordinator.

- **STATUS** (coordinator):
  - Mark the 1.5 promise "Chapter 3 comes back to this game" as paid by F2.3 §03 `exm-five-strings-diagonal`.
  - Mark 1.2's Cantor pointer (1/02:441) as paid by `thm-cantor` and the subsection `## Back to Russell: Cantor's theorem`.
  - Add a promise row: F2.3 §04 "whether any two sets are comparable" → Section 5.2 (Zorn), to be paid by ch05-deepen.
  - Retag any F2.3 rows that name the old 3.2–3.6 by the layout §3.2 table.
- **ch05-deepen / Chapter 5:** 5.2 must open its comparability application as "Back to comparability", answering 04's `[Looking ahead]` remark (§4.4 item 5) and citing `def-card-le`.
- **ch02-deepen §4.6 and the Chapter-3 rows of §4.8:** superseded by §4.0 and §4.6 here. If the Chapter 2 coordinator has not applied them yet, it should leave Chapter 3's files to this chapter's S3.
- **Preface `fd2/src/index.md`:** the Chapter 3 row of ch02-deepen §4.8 ("Countable sets, the axiom of choice, diagonal arguments and Cantor's theorem, the Schröder–Bernstein theorem, infinite sets") stands. No further change.
- **config.json:** the chapter title, if config lists one, is "Countable and Uncountable Sets" (the volume config at line 102 lists only the directory).
- **NOTATION:** nothing new. |A| ≤ |B|, 𝒫, 𝟙_S, {0, 1}^ℕ and Y^X are already there.
- **Layout §3.3 sweep** (fd1, fd3, fd4: "Section 3.2–3.6" → 3.1–3.5; finite-set mentions of "Section 3.1" → 2.5): not this chapter's work.

## 7. S2a: claims to verify

1. 3.1 Quick check: n² + 3n is an image; the pairs (q, n) form a subset of the countable ℚ × ℕ.
2. 3.1 scratch work and table match the unchanged proof of `thm-product-countable` (parity claim, monotonicity of 3^k).
3. `exm-list-integer-combinations`: the surjection; ℕ ⊆ S; the aftermath's use of @fd1:thm-sqrt2-irrational (that label proves √2 irrational).
4. `exm-list-two-element-subsets`: min and max named by a rule; injectivity through p; n ↦ {0, n + 1} injective; the infinitude argument cites only 2.5 results.
5. 01 B4 (a)–(e), especially (b) (finite image ⇒ ℕ finite) and (d) (A = ∅).
6. 3.2 Quick check: (n + 1)² > n.
7. `exm-choice-or-rule`: (a) via @prp-finite-max; (b) density of ℚ is a school fact, and the least index is a rule once q is fixed by one ∃E; (c) the family's index set (countably infinite subsets of ℝ) is a set (specification in 𝒫(ℝ)), and its members are non-empty; (d) the least index in A_n; no overlap with 02 B1; no reason rests on 3.3.
8. 3.2 scratch-work table agrees with the proof's lines (J, S_n, F, the one bold line).
9. 02 B4 (a)–(e); (e)'s c is a rule, and "ℕ equinumerous with a subset of a finite set ⇒ ℕ finite".
10. `exm-five-strings-diagonal`: diagonal 01001, flip 10110, the five differing places; it agrees with 1/05:202's list, and differs from Chapter 1's Quick check answer 10010 (1/05:209, an unrelated indicator of {1, 4}), so 1.5 does not give the diagonal away.
11. The six-strings Quick check.
12. 3.3 scratch work: the table rows; non-emptiness is in the proof.
13. The unflipped-diagonal Quick check (the zero list).
14. `exm-diagonal-outgrows-list`: @prp-finite-max applies to n + 1 numbers; g(n) > f_k(n) for n ≥ k; the example's text never states g ≠ f_k or that g is off the list (B1's blank).
15. The Russell hook paragraph agrees with `thm-russell`'s statement and does not repeat 03:91.
16. 03 B4: (a) periodicity ⇒ determined by the first p values (division algorithm, induction on q), and the union over p listed by a rule; (b) the interleaving map lands in the set and is injective; (c) left inverse needs a non-empty domain, 𝒫(X) ∋ ∅; (e) the restriction is onto.
17. 3.4 repair: no `@def-partial-order` or "(PO2)" remains, and the analogy sentence is true.
18. The 3.4 Quick check (5 ∉ [0, 1]; x/2 ≤ ½ < 1); the `[Looking ahead]` remark's claim (the image of ℕ under any map is countable, @prp-countable-image).
19. 04 B4: (b) the composite and Schröder–Bernstein; (c) the composite injection; (d) injectivity of S ↦ p(S); (a).
20. Every row of §4.6 by grep after S3: no "Section 3.6", and no "Section 3.1" meaning finite sets.

**Frozen after S2 (2026-10-25).**

## 8. Notes for S3 and S4

- **Drafters:** two. (i) 3.1 and 3.2. (ii) 3.3, 3.4 and 3.5. Neither cites the other's new labels, so they can run in parallel. The coordinator writes the index last, against the delivered sections. Sonnet may take 3.4 and 3.5 (Idea-level and terse; lean workflow).
- **Sidecars** (`fd2/verify/ch03/`, new):
  - `exm-list-two-element-subsets.py`: injectivity of 2^{min} 3^{max} on the two-element subsets of {0, …, 40}.
  - `exm-five-strings-diagonal.py`: the given list, plus all 5-lists drawn at random from the 32 strings.
  - `exm-diagonal-outgrows-list.py`: random lists of functions on {0, …, 30}.
  - `exr-countable-sets-b4.py`: the counterexamples, and (a) on a finite range.
  - `exr-countable-unions-and-choice-b4.py`: (e)'s c on small finite families.
  - `exr-diagonal-arguments-b4.py`: periodic sequences on {0, …, 23} determined by p values; restriction onto.
  - `exr-comparing-cardinalities-b4.py`: S ↦ p(S) injective on 𝒫({0, 1, 2}²).
  - The existing sidecars are unchanged.
- **Checkers:**
  - `check_structure.py`: 0 fatal. Its whole-file word advisory is accepted; the budget is measured to `## Exercises`, as in ch02-deepen §8.
  - `check_numbers.py`, `check_notation.py`.
  - `check_forward_deps.py`: Chapter 3 cites no Chapter 4 or 5 label.
- **Review (lean workflow, layout §7):** every Chapter 3 section is a moved section, so S8 and a changed-only blind review. The boxes, scratch work, tables, new examples, B4s, checks, the 04:52 repair and the pointer edits count as changes. No section runs the full pipeline.
- **Open for the author** (none blocking):
  1. 3.4 is a method section (it introduces a box) at layout level "Idea". It gets the box, one Givens/Goal table and a Prove-or-disprove item, but no `[Scratch work]`. STYLE §12.14's four devices are met except the scratch idea, which the layout's level excludes.
  2. The Time projects to about 30 h core and 45 h full, above layout §2's 25/30 (§5).
  3. 3.4 and 3.5 already exceed the layout's whole-file figures (4,214 > 4,200; 3,709 > 3,700). The blueprint reads all budgets as main line to Exercises, as Chapters 1–2 did.

## S2 replies (round 1)

Two blind referees (R1, R2). Every finding is applied unless marked "answered".

**R1**
1. *exm-choice-or-rule (d), forward reason (gap).* Applied: the comparison with 02 B1 (c) is dropped; (d) ends on its formula and the closing sentence stands. No reason rests on 3.3 (S2a 7).
2. *thm-algebraic-countable Idea clause (error).* Applied: "Steps 2 and 3 are route (S) …: each union is the image of a countable grid. Step 1 only cites closure under products and subsets."
3. *Rule 3 / comparability paragraph (minor).* Applied: rule 3 restated (no @label into Chapters 4–5; later-section pointers are prose and never reasons; the existing in-chapter previews are kept, renumbered). The comparability hook becomes a `[Looking ahead]` remark at the end of 3.4's main line (§12.1's form).
4. *03 B4 (b) repeats 03 B2 (minor).* Applied: (b) is now "no two consecutive 1s", by the interleaving injection and (ii) ⇒ (i).
5. *04 B4 (c) answered in the text (minor).* Applied: (c) is now "If |A| ≤ |B| and B is countable, then A is countable" (true, composite injection).
6. *exm-list-integer-combinations title (minor).* Applied: `[Integer combinations of 1 and √2]`; infinitude uses ℕ ⊆ S directly.
7. *Quick check wording (minor).* Applied: "Does this line need @ax-choice?"; "No: it need not."
8. *list-it Template citation (minor).* Applied: (S) cites @def-countable or @prp-countable-image; (I) cites (ii) ⇒ (i).
9. *[0,1] ∪ {5} check (minor).* Applied: "Since 5 ∉ [0, 1], the two clauses define a function into [0, 1]."
10. *"first contradiction" (minor).* Applied: the hook says "proved Russell's theorem".
11. *S2a 10 misreads 1.5's check (minor).* Applied: 10010 is recorded as an unrelated indicator that differs from the diagonal.
12. *Whole-file vs main-line budgets (minor).* Applied: §8 "Open for the author" item 3; the word-count paragraph says so.

**R2**
1. *exm-choice-or-rule (d) (gap).* Applied, as R1.1.
2. *Forward-pointer count; Looking-ahead form (gap).* Applied, as R1.3. The true state is recorded in rule 3; 02:139 and 02:201 are kept as in-chapter previews (renumbered to 3.3), carrying no reason.
3. *exm-diagonal-outgrows-list gives away 03 B1 (gap).* Applied, fix (1): the "In particular … not on the list" sentence is removed; the text never states g ≠ f_k. S2a 14 checks this.
4. *Time projection (gap).* Applied: §5 projects about 30 h core / 45 h full from the index's rates, whole-file words about 27,500–28,000; the overrun against layout §2 goes to the author (§8 item 2).
5. *Box word caps (minor).* Applied: list-it and name-the-choice cut to ≤ 120 words; list-it keeps two failures (01:35 named as the existing warning); name-the-choice merges the empty-set point into the failure line.
6. *Quick check (b) duplicates the second example (minor).* Applied: (b) is now the pairs (q, n) ∈ ℚ × ℕ with q·n ∈ ℤ (a subset, by inclusion). `exm-list-two-element-subsets` keeps its data; its overlap with 01 B1 (b) is answered: B1 (b) is ordered pairs by a surjection-style listing, the example codes unordered sets by an injection.
7. *Russell payoff not a "Back to …" subsection; says it twice (minor).* Applied: the subsection is retitled `## Back to Russell: Cantor's theorem`; the hook is cut to two sentences and leaves the identification to 03:91.
8. *03:3 frame (minor).* Applied: §4.3 item 2 edits 03:3 to name the game of Section 1.5.
9. *02:47 history (minor).* Applied: the two Gödel/Cohen sentences become one line.
10. *S2a 10 (minor).* Applied, as R1.11.
11. *03 B4 (a) unflagged choice (minor).* Applied: one sentence says each P_p is listed by a rule, so no @ax-choice, as in @exm-choice-free-unions.
12. *R items reach Chapter 1 only by vocabulary (minor).* Applied: R3's solution gains a clause naming @exm-method-injectivity and @exm-method-surjectivity (§4.5 item 4).
