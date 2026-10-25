<!-- hand-written -->
# Deepening blueprint: F2.1 Sets and Functions: Proofs from Definitions (fd2 Chapter 1), stage S1

**Status: S1 draft, 2026-10-25.**

**What this is.** The S1 blueprint for fd2 Chapter 1 under the binding layout `fd2/authoring/design/layout-final.md` (option C; §1 Ch1 rows, §3, §4, §5). It is complete on its own: a drafter executes it with this file, the current `fd2/src/ch01-sets-and-functions/` files, `authoring/STYLE.md` (§1 "House manner from fd2 on", §2 item 6, §4 item 3, §11, §12.0, §12.5, §12.13.4, §12.14), `DRAFTING.md` and `NOTATION.md`. The format follows `fd1/authoring/blueprints/ch06-deepen.md`, leaner.

**File numbering.** The S1 commit renamed old 1.1–1.6 with `git mv` (`0k-<slug>.md` → `0(k+1)-<slug>.md`). Line counts did not change. Line references below are to the renamed files at that commit: `02:161` is `02-sets-and-subsets.md` line 161, then `03:` set operations, `04:` products and relations, `05:` functions, `06:` inverses, `07:` images and preimages, `ix:` `index.md`, and `22:` `fd2/src/ch02-relations-and-induction/02-induction-in-practice.md`. `01-proofs-from-definitions.md` is new. The verify sidecars in `fd2/verify/ch01/` are named by label, not by file number, so none moved.

**Word counts** are main-line prose words as `tools/check_structure.py`'s `prose_words` counts them: a math span is one word, and code blocks and folds are excluded. Counts run from the top of the file to `## Exercises`. Measured at the S1 commit:

| File | Main line now (to Exercises) | Layout budget |
|---|---|---|
| 02 | 5,069 | 5,000 |
| 03 | 4,698 | 5,000 |
| 04 | 3,764 | 4,500 |
| 05 | 5,187 | 5,000 |
| 06 | 4,143 | 5,000 |
| 07 | 4,525 | 5,000 |

**Inputs.** layout-final §1 (Ch1 rows), §3.1–3.2 (labels), §4 (fd3 division of labour), §5 (devices and threads), §7 (pipeline). STYLE as above. The Cummings long-form skill is used for its moves only: motivation before a major definition, scratch work kept apart from the proof, hooks and payoffs. There are no footnotes, no jokes, no history beyond one line, and no first person. *Proofs* (Cummings) was consulted for technique only. Its chessboard and domino tilings, its hair, sock and point-in-square pigeonhole problems, and its parity and divisibility propositions and exercises (n² + n + 6, n² + 3n − 6, 6 | n³ − n and others) are **not** used. Every example, item and answer below is the book's own. The old blueprint `ch01.md` fixed the items kept here: the key proofs `thm-de-morgan-families`, `thm-left-inverse-iff-injective` and `thm-preimage-operations`; the faded element-chasing triple; the find-the-error items 03 C2 and 07 C2; the Try-it-firsts on `thm-russell` and `thm-image-intersection`; the exit checks 05 C1 and 07 C3; and R1–R4.

**Binding rules.**
1. **No label is lost or renamed.** Every label now in Chapter 1 stays in its file. The 39 downstream-cited Chapter 1 labels (layout §3.2) keep the content of their blocks. `def-divides` and `def-prime` move **verbatim** from 22:90–93 and 22:106–109 into 1.1 (layout §3.2 row "2.2 → 1.1"), and 2.2 keeps a pointer (§4.8). Moving a passage verbatim into a fold is not a change. No cited statement goes into a fold; only proofs, justifications and edge discussions do (STYLE §12.0).
2. **fd1 is cited, never re-taught.** The connective and quantifier rules, induction (`@fd1:ax-induction`, Section 4.2), "without loss of generality" (8.2, `@fd1:exm-rhetoric-induction` (b)), double inclusion in prose (`@fd1:exm-rhetoric-double-inclusion`), two witnesses (`@fd1:exm-sum-of-evens`), the catalogue `@fd1:exm-not-allowed-catalogue` (N1–N14) and n odd ⇔ n² odd (`@fd1:thm-odd-iff-square-odd`) are recalled in a clause and linked.
3. **fd3 division (layout §4).** 1.1 only unwinds definitions over the school integers: divisibility closed under combinations, transitivity, parity of sums and products, cases mod 2 (mod 3 only in C1, which proves its own three forms). There is no gcd, Bézout, Euclid's lemma, unique factorization or ℤ/n. One prose pointer to fd3 is allowed (in `exm-refute-divides-product`). No proof in 1.1 cites `prp-integers-closed` (2.1, forward). Closure of ℤ under +, −, · and "no integer lies strictly between 0 and 1" are school facts and go in the ledger.
4. **Pigeonhole is not used as a reason.** 1.1 states it informally in the hook and proves nothing from it. One Looking-ahead box points to Section 2.5.
5. **New numbering.** Before any S3 drafting, the coordinator runs `tools/renumber.py` once, series-wide, with `{"fd2": {"sections": {"1.1": "1.2", "1.2": "1.3", "1.3": "1.4", "1.4": "1.5", "1.5": "1.6", "1.6": "1.7"}}}`, and records in STATUS that layout §3.3's later sweep must not repeat this map. Drafters then write every pointer in the final numbering. Hand fixes to "Chapter N" pointers are listed in §4.9.
6. **No drill banks.** Layout §5 keeps drill banks in fd1 only, so this chapter has no A2 drill. Quick-check density is about one per 800–1,000 main-line words (layout §5).

---

## 1. Devices as applied

- **Method boxes** (§2 item 6): ten. Each is `::: {#exm-method-<slug>}` with title `[Method: …]` and three bold lead-ins, **Template.**, **When to use it.** and **The usual failure.** (each box ≤ 130 words). The boxes are `direct-proof`, `cases`, `counterexample` (1.1); `element-chasing`, `double-inclusion` (1.2); `chain-of-iff` (1.3); `uniqueness` (1.4); `injectivity`, `surjectivity` (1.5); `construct-and-verify` (1.6). Each is linked from the index's Named moves.
- **`[Scratch work]` ideas** (§4 item 3), one at each method's first full appearance: `prp-divides-transitive` (direct proof), `thm-even-or-odd` (cases), `exm-refute-divides-product` (counterexample), `prp-subset-transitive` (element-chasing), `exm-set-builder-small` (a) (double inclusion, a short guess paragraph), `exm-difference-chain` (chain of iff), `exm-coordinates-unique` (uniqueness), `exm-fraction-map` (surjectivity backwards, proof forwards; the injectivity scratch is three lines in the same example), and `thm-left-inverse-iff-injective` (construct and verify).
- **Givens/Goal tables in prose form** (§12.5): one in each method section, inside the scratch work of the first proof by the new method. The last row shows the gap.
- **Prove or disprove** (§12.13.4): 1.1 B4, 1.2 B4, 1.3 B4, 1.4 B4, 1.5 B4, 1.6 B4. Verdicts are withheld in the stem. Solutions give the verdict first, then the proof or the counterexample. 1.7 is not a method section and gets none.
- **Fading** (layout §1): cases fall to an Idea with a back-reference from 1.4 on; element-chasing falls to an Idea from 1.3 on and is terse in 1.7; surjectivity scratch falls to an Idea from 1.6 on; uniqueness is a back-reference in 1.6.
- **Threads** (§5): the lattice-point hook in 1.1 is paid in 2.5 ("Back to the pigeons"); the five-string game is planted in 1.5 and paid in 3.3; Russell in 1.2, as the first contradiction, is paid by Cantor in 3.3; "same size" runs 1.6 → 2.5 → 4.2. All four are listed in the index.
- **Motivation before a major definition**: `def-divides`, by weird examples as a Quick check (1.1). The others already comply: `def-subset` (02:67–71), `def-ordered-pair` (04:7–9, the naive set {a, b}), `def-function` (05:7–9, the naive "rule"), `def-left-right-inverse` (06:7–27).

## 2. Section map

| § | File | Main line now → budget (expected) | Changes |
|---|---|---|---|
| index | `index.md` | — | retitle, story, What you need, Time, Roadmap, Named moves (10 boxes), Threads |
| 1.1 | `01-proofs-from-definitions.md` **new** | — → ≤ 4,500 (~4,350) | hook; definitions (`def-parity`, moved `def-divides`, `def-prime`); 3 method boxes; `prp-divides-transitive`, `thm-even-or-odd`; 5 examples; Looking ahead; A1, B1–B4, C1–C3 |
| 1.2 | `02-sets-and-subsets.md` | 5,069 → ≤ 5,000 (~4,850) | 2 boxes, scratch work and table, short main proof of transitivity; Russell lead-in; 2 Quick checks; folds F1.2-a…e; B4 |
| 1.3 | `03-set-operations.md` | 4,698 → ≤ 5,000 (~4,800) | box, `exm-difference-chain`, Idea rewrite, 2 Quick checks; fold F1.3-a; B4 |
| 1.4 | `04-products-and-relations.md` | 3,764 → ≤ 4,500 (~4,270) | box, `exm-coordinates-unique`, relabelled `exm-pair-equations`, 2 Quick checks; B4 |
| 1.5 | `05-functions.md` | 5,187 → ≤ 5,000 (~4,990) | 2 boxes replacing 05:339–343; `exm-fraction-map`; the five-string game; 2 Quick checks; folds F1.5-a…f; B4 |
| 1.6 | `06-inverses.md` | 4,143 → ≤ 5,000 (~4,540) | box; scratch work and table for `thm-left-inverse-iff-injective`; uniqueness Idea; 3 Quick checks; B4 |
| 1.7 | `07-images-and-preimages.md` | 4,525 → ≤ 5,000 (~4,840) | "Hunting a counterexample" paragraph; 4 Quick checks |

## 3. Labels

**Kept, in place:** every label now in 02–07 (layout §3.2 rows 1.1–1.6 → 1.2–1.7).

**Moved in:** `def-divides`, `def-prime` (verbatim, from 22).

**New (1.1):** `def-parity`, `prp-divides-transitive`, `thm-even-or-odd`, `exm-method-direct-proof`, `exm-method-cases`, `exm-method-counterexample`, `exm-divides-combination`, `exm-cubes-plus-five-n`, `exm-parity-of-sums`, `exm-refute-2p-plus-1`, `exm-refute-divides-product`, `exm-lattice-midpoint`, `exr-proofs-from-definitions-a1`, `-b1`…`-b4`, `-c1`…`-c3`.

**New elsewhere:**
- 1.2: `exm-method-element-chasing`, `exm-method-double-inclusion`, `exr-sets-and-subsets-b4`.
- 1.3: `exm-method-chain-of-iff`, `exm-difference-chain`, `exr-set-operations-b4`.
- 1.4: `exm-method-uniqueness`, `exm-coordinates-unique`, `exr-products-and-relations-b4`.
- 1.5: `exm-method-injectivity`, `exm-method-surjectivity`, `exm-fraction-map`, `exr-functions-b4`.
- 1.6: `exm-method-construct-and-verify`, `exr-inverses-b4`.

The five-string game is a bold-lead-in paragraph, not a label: 3.3 points to "Section 1.5" in prose.

**Downstream:** fd3's twins already exist. `prp-divides-transitive` ↔ `@fd3:prp-divisibility-rules-integers` (b), and `thm-even-or-odd` ↔ `@fd3:cor-integers-even-odd` (a). §6 lists the fd3 index edit.

---

## 4. Per-section plans

### 4.0 `index.md`

- **Title** `# Sets and Functions: Proofs from Definitions`.
- **Story, ix:3.** Insert as the new second sentence: "It is also where proofs start being about mathematics rather than about logic: each section teaches one method of proof on the material it introduces, starting in Section 1.1 with statements about integers proved straight from their definitions." The rest is kept.
- **ix:5** kept.
- **What you need (ix:7).** Add "Chapter 4, Section 4.2: induction (@fd1:ax-induction)" and "Chapter 8: … and the catalogue of what is not allowed (@fd1:exm-not-allowed-catalogue)".
- **Time.** "About 40 hours on the core track …; about 50 hours for everything" (layout §2). This is recomputed with `check_structure.py --words` after drafting.
- **Roadmap.** New first bullet: "**Proofs from definitions.** Even, odd, divides and prime; a direct proof unwinds a definition and rewinds another; proofs by cases and without loss of generality; refuting a claim by one counterexample; a puzzle about lattice points that the book finishes in Chapter 2." The other bullets are kept.
- **Named moves (ix:16–21).** The ten method boxes, one line each, linked in section order, then the two existing non-box moves, "Unwind the image" and "Refute with a small witness" (the latter now citing `exm-method-counterexample`). The current element-chasing and build-the-inverse entries become the box links.
- **Threads** (new, after Named moves): four bullets as in §1, each naming where it is planted and where it is paid ("Section 2.5", "Section 3.3", in prose).

### 4.1 Section 1.1: Proofs from Definitions (`01-proofs-from-definitions.md`, new)

**Budget:** main line ≤ 4,500 (expected ~4,350). No folds. Five Quick checks, two warnings, one Looking-ahead box. Subsections in this order.

**Opening (~110).** "*Logic and Proof* taught the rules of proof and how to write them as prose. From here on the statements are about mathematical objects, and every word in them that matters has a definition. A proof begins by writing the hypotheses out by their definitions, writes out what the conclusion demands, and closes the gap between them. This section practises that on the integers, where the definitions are one line long and every claim can be tested by hand. It teaches five moves: direct proof, proof by cases, without loss of generality, disproof by counterexample, and proof of existence by an example."

**`## A puzzle about lattice points` (hook, ~300).** A **lattice point** is a point (a, b) of the plane with a, b ∈ ℤ, used here as in school geometry; Section 1.4 makes pairs precise. The midpoint of (a, b) and (c, d) is ((a + c)/2, (b + d)/2), and it may or may not be a lattice point: (0, 0) and (2, 4) have midpoint (1, 2), while (0, 0) and (1, 4) have (1/2, 2). Two questions:

- **(Q1)** Among **any five** lattice points, must two have a lattice point as midpoint?
- **(Q2)** Among **any four**?

"Before reading on, place a few sets of points on squared paper." Then: "Both answers come from two words this section defines, even and odd. Question (Q2) is settled in this section. Question (Q1) needs, besides parity, a principle about finite collections that sounds too obvious to need proof; we will state it and leave its proof to Chapter 2." No answer is given here.

**`## Definitions first` (~520).**
1. Lead (one sentence), then **`def-parity`** `[Even and Odd]`: "An integer n is **even** if n = 2k for some k ∈ ℤ, and **odd** if n = 2k + 1 for some k ∈ ℤ." Then one sentence: *Logic and Proof* used these words informally (Section 5.6, @fd1:exm-sum-of-evens), and from now on they mean exactly this, a "there exists".
2. **`def-divides`**, verbatim from 22:90–93.
3. A paragraph of examples. It takes 22:94 without its last sentence (transitivity, now a proposition) and without the `@prp-integers-closed` clause: "So 3 | 12, with k = 4, and −3 | 12, with k = −4. Every integer a divides 0 … (verbatim to) … '\( n \) is even' is '\( 2 \mid n \)'."
4. **Quick check** (weird examples, the motivation mode). "Decide, from the definitions alone: (a) Is 0 even? (b) Does 0 divide 0? Does 0 divide 5? (c) Is −7 odd? (d) Does 12 divide 3?" *Solution:* (a) Yes, 0 = 2·0. (b) Yes, 0 = k·0 for any k (k = 0 will do); no, k·0 = 0 ≠ 5 for every k. (c) Yes, −7 = 2·(−4) + 1. (d) No: 3 = 12k would need 0 < k < 1, and no integer lies strictly between 0 and 1.
5. **`def-prime`**, verbatim from 22:106–109. One example sentence: "So 2, 3, 5 and 7 are prime (for 7, none of 2, 3, 4, 5, 6 divides it, and a positive divisor of 7 is at most 7); 9 = 3·3 and 15 = 3·5 are not, and neither is 1." Ledger: the positive divisor bound and the trial divisions are school facts.

**`## Direct proof` (~800).**
1. Lead: transitivity is the first claim.
2. **`prp-divides-transitive`** `[Divisibility Is Transitive]`: "For all integers a, b, c, if a | b and b | c, then a | c."
3. **`[Scratch work]`** idea (≤ 20 lines). The hypotheses unwind to two existentials, so name the witnesses, with **different** names, since nothing says they agree (@fd1:exm-sum-of-evens; (N4)). The goal unwinds to an existential: we must **produce** an integer m with c = ma. The table:

   | Givens | Goal |
   |---|---|
   | a \| b, b \| c | a \| c |
   | b = ka, c = lb, with k, l ∈ ℤ | c = m·a for some m ∈ ℤ: find m |
   | b = ka, c = lb | c = l(ka) = (lk)a: try m = lk, and check that lk ∈ ℤ |

   The last line closes the gap. "The proof writes this forwards: the witness m is named, then checked."
4. **Proof:** "Let a, b, c ∈ ℤ with a | b and b | c. By @def-divides there are k, l ∈ ℤ with b = ka and c = lb. Then c = l(ka) = (lk)a, and lk ∈ ℤ, as a product of integers. So a | c, with witness lk, by @def-divides." Aftermath (one sentence): the proof used nothing but the definition, read in both directions.
5. **`exm-method-direct-proof`** `[Method: direct proof from a definition]`.
   - **Template.** To prove "if P, then Q": (1) assume P and write it out by its definition, giving each witness a new name; (2) write out what Q demands, for example which object must be produced; (3) close the gap by computation, on scrap paper if need be; (4) write the proof forwards: assume, unwind, compute, and rewind into the definition of Q, naming the witness and checking that it is of the required kind.
   - **When to use it.** The hypotheses and the conclusion are defined notions, and the gap between them is computation.
   - **The usual failure.** Stopping at the computation, as in "c = (lk)a, done", without checking that lk ∈ ℤ, which is the clause the definition demands. Also one name for two witnesses (N4), and using what is to be proved (N9).
6. **`exm-divides-combination`** `[Divisors of a combination]`: "Let a, b, c ∈ ℤ with a | b and a | c. Show that a | bx + cy for all x, y ∈ ℤ." *Solution*, with a two-line Idea citing the box: b = ka and c = la, so bx + cy = kax + lay = (kx + ly)a, with kx + ly ∈ ℤ. The aftermath has three special cases: x = y = 1 gives a | b + c; x = 1, y = −1 gives a | b − c; y = 0 gives a | bx. With a = 2 and x = y = 1 this is "even + even is even", @fd1:exm-sum-of-evens.
7. **Quick check:** "The proof of @prp-divides-transitive named two witnesses, k and l. Find integers a, b, c with a | b and b | c for which one name could not serve for both." *Solution:* a = 1, b = 2, c = 6: b = 2a and c = 3b, and no single k has both 2 = k·1 and 6 = k·2. One name would claim the two multipliers equal, (N4).

**`## Proof by cases` (~750).**
1. Lead: some claims depend on what kind of integer we have. The first such fact is the one behind every parity argument.
2. **`thm-even-or-odd`** `[Every Integer Is Even or Odd]`: "Every integer is even or odd, and no integer is both."
3. **`[Scratch work]`** (≤ 20 lines). On ℕ, use induction (@fd1:ax-induction) with P(n): "n is even or n is odd". The step needs P(n + 1) from P(n), but P(n) is an "or", and knowing that n is even **or** odd does not tell us which. So split into the two cases (∨E, @fd1:def-rules-disjunction). Each case is a new given, and each must reach the same goal:

   | Givens | Goal |
   |---|---|
   | P(n): n even or n odd | n + 1 even or n + 1 odd |
   | Case 1: n = 2k | n + 1 = 2k + 1: odd |
   | Case 2: n = 2k + 1 | n + 1 = 2(k + 1): even |

   Then the negative integers, by cases again: −n ∈ ℕ. "Not both" says 2a = 2b + 1 is impossible, so it ends in a contradiction (¬I).
4. **Proof.** *Every natural number is even or odd*, by induction on n: P(0) holds since 0 = 2·0; for the step, the two cases as in the table; so P(n) for all n ∈ ℕ by @fd1:ax-induction. *Every integer.* Let n ∈ ℤ. If n ≥ 0, then n ∈ ℕ and we are done. If n < 0, then −n ∈ ℕ is even or odd. If −n = 2k, then n = 2(−k). If −n = 2k + 1, then n = −2k − 1 = 2(−k − 1) + 1. *Not both.* Suppose n = 2a and n = 2b + 1 with a, b ∈ ℤ. Then 2(a − b) = 1, with c ≔ a − b ∈ ℤ. If c ≥ 1 then 2c ≥ 2, and if c ≤ 0 then 2c ≤ 0; either way 2c ≠ 1, a contradiction. So no integer is both (¬I).
5. Aftermath, one sentence: a fact *Logic and Proof* took from school is now proved; the proof has three case splits, each into cases that together cover everything.
6. **`exm-method-cases`** `[Method: proof by cases]`.
   - **Template.** Find a disjunction you already have, such as "n is even or n is odd" (@thm-even-or-odd), "x ≥ 0 or x < 0", or excluded middle (@fd1:prp-excluded-middle). Write one paragraph per case, labelled *Case 1.*, *Case 2.*. In each, add the case to the givens, unwind it, and reach the **same** goal.
   - **When to use it.** The definitions or the algebra behave differently on different kinds of input, so the givens give no grip until you know which kind you have.
   - **The usual failure.** Cases that do not cover every possibility (N8), or a case forgotten (N7). Before splitting, say why the cases are exhaustive.
7. **`exm-cubes-plus-five-n`** `[A proof by cases]`: "Show that n³ + 5n is even for every integer n." Idea (two lines) citing the box and @thm-even-or-odd. *Solution:* Case n = 2k: n³ + 5n = 8k³ + 10k = 2(4k³ + 5k). Case n = 2k + 1: n³ = 8k³ + 12k² + 6k + 1 and 5n = 10k + 5, so n³ + 5n = 8k³ + 12k² + 16k + 6 = 2(4k³ + 6k² + 8k + 3). In each case the bracket is an integer.
8. **Quick check:** "Why does the proof of @exm-cubes-plus-five-n need no third case?" *Solution:* by @thm-even-or-odd every integer is even or odd, so the two cases cover ℤ.

**`## Without loss of generality` (~380).**
1. Lead: when two cases are mirror images, one is written and the other is "the same with the roles exchanged". *Logic and Proof*, Section 8.2 read the phrase as a ∨E whose second box is the first with the letters swapped, and it is licensed only when the statement and the hypotheses are unchanged by the swap (@fd1:exm-rhetoric-induction (b)).
2. **`exm-parity-of-sums`** `[The parity of a sum]`: "Let m, n ∈ ℤ. (a) If m and n have the same parity (both even or both odd), then m + n is even. (b) If they have opposite parity, then m + n is odd." *Solution:* (a) Case both even: @exm-divides-combination with a = 2. Case both odd: (2k + 1) + (2l + 1) = 2(k + l + 1). (b) The statement is symmetric in m and n (m + n = n + m, and "opposite parity" does not change when the two are exchanged), so without loss of generality m is even and n is odd: 2k + (2l + 1) = 2(k + l) + 1. The case m odd and n even is the same with m and n exchanged.
3. **Warning** `**Check the symmetry first.**` "'Without loss of generality m ≤ n' is legitimate for a claim about m + n, and not for a claim about m − 2n: exchanging m and n changes that claim. Before writing the phrase, exchange the letters in the statement and in the hypotheses, and check that nothing changes."

**`## Counterexamples and examples` (~850).**
1. Lead: a universal claim, "for every x, if P(x) then Q(x)", is refuted by one x with P(x) and not Q(x). By the negation laws (@fd1:prp-quantifier-negation, @fd1:prp-negated-implication), ¬∀x (P(x) → Q(x)) is ∃x (P(x) ∧ ¬Q(x)). An existential claim is proved by one example (∃I).
2. **`exm-refute-2p-plus-1`** `[A pattern that breaks]`: "Is 2p + 1 prime for every prime p?" *Solution:* p = 2, 3, 5 give 5, 7, 11, all prime. At p = 7 the pattern breaks: 7 is prime, and 2·7 + 1 = 15 = 3·5 has the positive divisor 3 ∉ {1, 15}, so 15 is not prime (@def-prime). The claim is false, and p = 7 is a counterexample. Three successes proved nothing (N1); one failure settles it.
3. **Warning** `**A counterexample must satisfy the hypothesis.**` "p = 4 makes 2p + 1 = 9, which is not prime, but 4 is not prime either, so p = 4 says nothing about the claim. A counterexample to 'if P(x), then Q(x)' needs P(x) true **and** Q(x) false, and both are checked on the page."
4. **`exm-refute-divides-product`** `[Dividing a product]`: "Prove or disprove: for all integers a, b, c, if a | bc, then a | b or a | c."
   - **`[Scratch work]`** (≤ 15 lines). Try small a. For a = 2, if 2 | bc then b or c is even, since the product of two odd numbers is odd: (2k + 1)(2l + 1) = 2(2kl + k + l) + 1. So a = 2 gives no counterexample. a = 3 resists too. For a = 4, take b = c = 2: then bc = 4. Table:

     | Givens | Goal |
     |---|---|
     | — | integers a, b, c with a \| bc, a ∤ b, a ∤ c |
     | a = 4, b = c = 2 | 4 \| 4, 4 ∤ 2 (twice) |
     | 4 = 1·4 | 4 ∤ 2: no k ∈ ℤ with 2 = 4k |

   - *Solution:* "False. Take a = 4, b = c = 2. Then bc = 4 = 1·4, so 4 | bc. And 4 ∤ 2: if 2 = 4k with k ∈ ℤ, then k ≥ 1 gives 4k ≥ 4 and k ≤ 0 gives 4k ≤ 0, so 4k ≠ 2." Aftermath (the allowed prose pointer to fd3): "The search failed for a = 2 and a = 3, and that is no accident: for a prime a the statement is true, a fact *Number Systems*, Chapter 3 proves."
5. **`exm-method-counterexample`** `[Method: disproof by counterexample, proof by example]`.
   - **Template.** To refute "for every x, if P(x) then Q(x)": name one x, check P(x), and check that Q(x) fails. To prove "there is an x with P(x)": name one x and check P(x).
   - **When to use it.** The claim survives a few tries, yet you doubt it; or the statement is existential. Search small and extreme cases first: 0, 1, negative numbers, the smallest sets.
   - **The usual failure.** A "counterexample" that does not satisfy the hypothesis; refuting a different claim from the one stated; and the mirror error, concluding "for every" from examples (N1). One example refutes a universal claim, and no number of examples proves one.
6. One line of existence by example: "There is an integer n > 1 with n | 2ⁿ + 1: n = 3, since 2³ + 1 = 9 = 3·3."
7. **Quick check:** "Is p = 2 a counterexample to the claim of @exm-refute-2p-plus-1? Is p = 11?" *Solution:* No and no: 5 and 23 are prime, so in each case the conclusion holds.

**`## Back to the lattice points` (~500).**
1. **(Q2) is false.** The four points (0, 0), (0, 1), (1, 0), (1, 1) have six midpoints, (0, ½), (½, 0), (½, ½), (½, ½), (½, 1), (1, ½), and none is a lattice point. A counterexample to a universal claim is also an existence proof by example: there are four lattice points with no lattice midpoint.
2. **The parity pattern** of (a, b) is the pair of words (parity of a, parity of b): even–even, even–odd, odd–even or odd–odd. By @thm-even-or-odd every lattice point has exactly one of the four patterns. The four points above have one pattern each, which is why they fail.
3. **`exm-lattice-midpoint`** `[Same pattern, lattice midpoint]`: "If two lattice points have the same parity pattern, then their midpoint is a lattice point." *Solution:* a and c have the same parity, so a + c is even by @exm-parity-of-sums (a): a + c = 2s with s ∈ ℤ, and (a + c)/2 = s ∈ ℤ. Likewise for b + d.
4. **Quick check:** "Which pattern does (−3, 8) have? Find a second point with the same pattern, and their midpoint." *Solution:* odd–even. For example (1, 0), with midpoint (−1, 4).
5. **(Q1), almost.** Five points, four patterns: two of the points must share a pattern, and then @exm-lattice-midpoint finishes. The step "five objects in four boxes put two in one box" is the **pigeonhole principle**. It is stated here, not proved, and so the answer to (Q1) is "yes, once the principle is proved". Four points also show that five cannot be lowered to four.
6. **Looking ahead** (`::: {.remark}` `[Looking ahead]`, the section's only forward pointer): "Chapter 2 proves the pigeonhole principle, from a precise definition of 'finite', and comes back to these five points."

**Exercises (1.1).**
- **A1** (four parts, one folded solution).
  - (a) Write out "6 | n" and "n is odd" by their definitions, each as a "there exists".
  - (b) True or false, with reasons: −1 is odd; 7 | 0; 0 | 7; 1 is prime.
  - (c) What must a counterexample to "every multiple of 4 is a multiple of 8" satisfy? Give one.
  - (d) In the proof of @thm-even-or-odd, name the three case splits and say why each is exhaustive.
  - *Solution:* (a) 6 | n: n = 6k for some k ∈ ℤ; odd: n = 2k + 1 for some k ∈ ℤ. (b) True (−1 = 2·(−1) + 1); true (0 = 0·7); false (k·0 = 0 ≠ 7); false (1 < 2). (c) It must be a multiple of 4 that is not a multiple of 8, for example 4 = 1·4 (and 4 = 8k has no integer solution, since 0 < ½ < 1). (d) Even or odd in the induction step (the induction hypothesis); n ≥ 0 or n < 0 (order of ℤ); c ≥ 1 or c ≤ 0 (no integer strictly between 0 and 1).
- **B1** `[B1: Direct proofs]`. Prove for all integers a, b, c, d: (a) if a | b, then a | b²; (b) if a | b and c | d, then ac | bd. *Solution:* (a) b = ka gives b² = (kb)a, with kb ∈ ℤ. (b) b = ka and d = lc give bd = (kl)(ac), with kl ∈ ℤ.
- **B2** `[B2: Two cases]`. Prove that for every integer n, either 4 | n² or 4 | n² − 1. *Solution:* by @thm-even-or-odd. Case n = 2k: n² = 4k². Case n = 2k + 1: n² − 1 = 4k² + 4k = 4(k² + k).
- **B3** `[B3: Name the move, then complete it]`. "Prove that if m, n ∈ ℤ have opposite parity, then m² + n² is odd." Given lines: "The statement is unchanged when m and n are exchanged, so we may assume … ⋮ … Hence m² + n² is odd." *Solution:* the move is *without loss of generality*: assume m = 2k and n = 2l + 1. Then m² + n² = 4k² + 4l² + 4l + 1 = 2(2k² + 2l² + 2l) + 1. The other case is the same with m and n exchanged.
- **B4** `[B4: Prove or disprove]`. "Prove each true statement and refute each false one with a counterexample."
  - (a) For all integers a, b, c: if a | b and a | c, then a | b − c.
  - (b) For all integers a, b: if a | b and b | a, then a = b.
  - (c) For every integer n, n⁴ + n² + 1 is odd.
  - (d) The sum of any three odd integers is even.
  - (e) There is an integer n > 5 with n | n + 6.
  - (f) For all integers m, n: if mn is even, then m and n are both even.
  - *Solution:* (a) True: b = ka and c = la give b − c = (k − l)a. (b) False: a = 1, b = −1 (−1 = (−1)·1 and 1 = (−1)·(−1)), and 1 ≠ −1. (c) True. Case n = 2k: n⁴ + n² + 1 = 2(8k⁴ + 2k²) + 1. Case n = 2k + 1: n² = 2j + 1 with j = 2k² + 2k, so n⁴ + n² = n²(n² + 1) = (2j + 1)(2j + 2) = 2(2j + 1)(j + 1), and n⁴ + n² + 1 = 2(2j + 1)(j + 1) + 1. (d) False: 1 + 1 + 1 = 3 = 2·1 + 1 is odd, hence not even (@thm-even-or-odd). (e) True: n = 6, since 12 = 2·6. (f) False: m = 2, n = 1, with mn = 2 even and n odd.
- **C1** `[C1: Three cases]`.
  - (a) By the method of @thm-even-or-odd, show that every integer has the form 3k, 3k + 1 or 3k + 2 for some k ∈ ℤ.
  - (b) Deduce that 3 | n³ + 2n for every integer n.
  - (c) With @exm-cubes-plus-five-n, deduce that 6 | n³ + 5n.
  - *Hints* (ladder): 1. "For (c), write n³ + 5n = (n³ + 2n) + 3n." 2. "If m = 2a and m = 3b, look at 3m − 2m."
  - *Solution:* (a) Induction on ℕ: 0 = 3·0. In the step, 3k → 3k + 1, 3k + 1 → 3k + 2, 3k + 2 → 3(k + 1). For n < 0, write −n in one of the forms: −3k = 3(−k), −(3k + 1) = 3(−k − 1) + 2, −(3k + 2) = 3(−k − 1) + 1. (b) Cases. n = 3k: n³ + 2n = 3(9k³ + 2k). n = 3k + 1: n³ + 2n = 27k³ + 27k² + 15k + 3 = 3(9k³ + 9k² + 5k + 1). n = 3k + 2: n³ + 2n = 27k³ + 54k² + 42k + 12 = 3(9k³ + 18k² + 14k + 4). (c) m ≔ n³ + 5n = (n³ + 2n) + 3n, so 3 | m by (b) and @exm-divides-combination. And 2 | m by @exm-cubes-plus-five-n. With m = 2a and m = 3b: m = 3m − 2m = 3(2a) − 2(3b) = 6(a − b).
- **C2** `[C2: Find the error]` (true conclusion). "Claim: if n ∈ ℤ and n² is odd, then n is odd. 'Proof': Let n be odd, n = 2k + 1. Then n² = 4k² + 4k + 1 = 2(2k² + 2k) + 1 is odd." Is the conclusion true? Does the argument prove it? *Solution:* The conclusion is true (@fd1:thm-odd-iff-square-odd). The argument proves the converse: its first line assumes the conclusion, which is (N5). The →I box must open with "n² is odd". A counterexample to the step "Q → P, hence P → Q": "if n² > 0 then n > 0", 'proved' by "let n > 0, then n² > 0", which is false at n = −1. A correct proof is by cases: if n = 2k, then n² = 2(2k²) is even, hence not odd (@thm-even-or-odd), against the hypothesis, so this case cannot occur (⊥E). So n is odd.
- **C3** `[C3: Lattice points in space]`. "A lattice point of space is (a, b, c) with a, b, c ∈ ℤ. (a) Give eight lattice points of which no two have a lattice point as midpoint. (b) Show that two lattice points with the same three parities have a lattice midpoint. (c) Which principle, stated in this section and not yet proved, would show that among any nine lattice points two have a lattice midpoint?" *Solution:* (a) the eight points with coordinates in {0, 1}: any two differ in some coordinate, where the sum is 1. (b) As in @exm-lattice-midpoint, coordinate by coordinate. (c) The pigeonhole principle: nine points, 2³ = 8 patterns.

**Ledger (1.1).** Closure of ℤ under +, −, ·; the order of ℤ (n ≥ 0 or n < 0, no integer strictly between 0 and 1, k ≥ 1 ⇒ 4k ≥ 4); a positive divisor of a positive n is at most n; the trial divisions for 7; −n ∈ ℕ for an integer n < 0. All are school facts. `prp-integers-closed` is **not** cited.

### 4.2 Section 1.2: Sets, Subsets and Russell's Paradox (`02`)

Budget: 5,069 → ≤ 5,000 (expected ~4,850). Folds ≤ 720.

1. **Opening, 02:3.** Replace its first two sentences with: "Section 1.1 proved statements about integers straight from their definitions. Analysis needs the same for collections: …" (continue from "Analysis talks about collections all the time"). The rest is kept.
2. **02:98** (`exm-subset-first-examples` (b)): replace the inline definition "Here \( d \mid n \) … means that \( n = dk \) for some integer \( k \), so" with "By @def-divides,". Sidecar unchanged.
3. **02:87–91.** Keep 87. Replace 89 and 91 (84 words) with one sentence, "We call this move **element-chasing**:", followed by **`exm-method-element-chasing`** `[Method: element-chasing]`.
   - **Template.** "Let x ∈ A." Unwind the definition of A to see what is known about x. Rewind the definition of B to see what must be shown. End "Hence x ∈ B; since x was arbitrary, A ⊆ B."
   - **When to use it.** The goal is an inclusion, or any statement ∀x (x ∈ A → …).
   - **The usual failure.** Checking some elements (N1, the warning at 02:129); starting from x ∈ B, which proves the converse (N5); and choosing a particular x.

   Then 02:91's last two sentences ("Here is the move three times …") and the example follow.
4. **02:155–157** (100 words) are replaced by **`exm-method-double-inclusion`** `[Method: two inclusions]`.
   - **Template.** Two paragraphs, labelled (⊆) and (⊇), each an element-chase. To compute a set, first guess it from small cases, then prove the guess. The two paragraphs are separate boxes: neither uses the other's assumption.
   - **When to use it.** A set equality that no law gives at once. For "S = ∅", only (⊆) needs work.
   - **The usual failure.** Proving one inclusion only, or using the (⊆) assumption in the (⊇) paragraph. *Logic and Proof* wrote such a proof in prose (@fd1:exm-rhetoric-double-inclusion).
5. **02:159–203, "Transitivity, rule by rule."** The heading becomes `### Inclusions chain`. 02:161 is replaced by "The second payoff is that inclusions chain, as ≤ does." The Idea 02:169–171 is replaced by a **`[Scratch work]`** idea (≤ 14 lines): the goal A ⊆ C is a ∀ around a →, so let x ∈ A, and we must reach x ∈ C. Each hypothesis is a ∀ around a → too, used at the same x. Table:

   | Givens | Goal |
   |---|---|
   | A ⊆ B, B ⊆ C | A ⊆ C |
   | A ⊆ B, B ⊆ C, x ∈ A (x arbitrary) | x ∈ C |
   | …, x ∈ B (by A ⊆ B at x) | x ∈ C: gap closed by B ⊆ C at x |

   The **proof** becomes the level-3 proof of 02:203, as its own block: "Let x ∈ A. Since A ⊆ B, x ∈ B; since B ⊆ C, x ∈ C. Since x was arbitrary, A ⊆ C." The old proof body 02:174–200, with 02:161's parenthetical on levels and the paragraph 02:203, moves verbatim into **fold F1.2-a** `title="Transitivity, rule by rule"`. Its lead is the 161 parenthetical, kept: "(These are levels 0 and 2 … brackets appear only on the step a proof is about.)". The Quick check 02:205–211 stays on the main line.
6. **Fold F1.2-b** `title="An element and a subset at once"`: 02:127 verbatim.
7. **02:245.** Its first four sentences (from "These rules are enough …" to "… which completes (W6).") go verbatim into **fold F1.2-c** `title="Where the working rules come from"`. The sentences "What matters here is what is missing … would be contradictory." stay on the main line.
8. **exm-set-builder-small (02:302–303).** The first paragraph of (a)'s solution becomes the double-inclusion scratch work: "Scratch: squares of 0, ±1, ±2 are below 5 and (±3)² = 9 is not, so guess S = {−2, …, 2}. Then prove the guess by the method of @exm-method-double-inclusion; (⊆) is the inclusion that needs an argument." 02:318 ("Two remarks on the example") moves verbatim into **fold F1.2-d** `title="A finite list of cases is a proof"`, with one added clause after "legitimate": "(the method of @exm-method-cases)".
9. **Russell (02:352–377).** The derivation and its paragraph go verbatim into **fold F1.2-e** `title="Russell's theorem as a derivation"`. Keep 02:19's pointer ("lines 4–11 of the derivation after Russell's theorem"): a link into a fold opens it. Before 02:381, add a lead-in paragraph (≤ 80 words): "**A first proof by contradiction.** @thm-russell proves a negative statement, \( R_A \notin A \), and its proof has the shape every such proof has: suppose the statement to be refuted and derive a contradiction; \( \rulename{\neg I} \) (@fd1:def-rules-negation) then gives the negation. No proof by contradiction in this book is more economical: it never assumes the negation of its goal, and so needs no \( \rulename{RAA} \)." Then 02:381 is kept as it is (it is the Cantor payoff pointer, already there).
10. **Two Quick checks.**
    - After the element-chasing box: "Write the first and last sentences of an element-chasing proof that {n ∈ ℤ : 4 | n} ⊆ {n ∈ ℤ : 2 | n}, then fill in the middle." *Solution:* "Let n ∈ ℤ with 4 | n, so n = 4k with k ∈ ℤ. Then n = 2(2k) with 2k ∈ ℤ, so 2 | n. Since n was arbitrary, the inclusion holds." (Or @prp-divides-transitive with 2 | 4.)
    - After the double-inclusion box: "To prove {x ∈ ℝ : x² = 1} = {−1, 1}, which inclusion needs algebra and which only a check?" *Solution:* (⊆) needs algebra: x² = 1 gives (x − 1)(x + 1) = 0, so x = 1 or x = −1. (⊇) checks two cases.
11. **B4** `[B4: Prove or disprove]`.
    - (a) {n ∈ ℤ : 6 | n} = {n ∈ ℤ : 2 | n and 3 | n}.
    - (b) {n ∈ ℤ : 2 | n and 4 | n} = {n ∈ ℤ : 8 | n}.
    - (c) {x ∈ ℝ : x³ = x} = {−1, 0, 1}.
    - (d) For all sets A, B, C: if A ⊆ B and B ⊈ C, then A ⊈ C.
    - (e) For all sets A, B, C: if A ⊆ B, B ⊆ C and C ⊆ A, then A = C.
    - *Solution:* (a) True. (⊆) n = 6k = 2(3k) = 3(2k). (⊇) n = 2a = 3b, so n = 3n − 2n = 6a − 6b = 6(a − b). (b) False: 4 is in the left set (4 = 2·2 = 4·1) and not in the right (4 = 8k has no integer solution, since 0 < ½ < 1). (c) True: x³ − x = x(x − 1)(x + 1), which is 0 exactly when one factor is 0. Two inclusions. (d) False: A = C = ∅, B = {1}. (e) True: A ⊆ C by @prp-subset-transitive, and C ⊆ A is given, so A = C by @prp-subset-antisymmetric.

Main-line count: +555 (boxes ~230, scratch work and proof ~135, Russell lead-in 80, checks 110) − 700 folded or absorbed (F1.2-a ~240 net, F1.2-b 85, F1.2-c ~121, F1.2-d 86, F1.2-e 107, 89–91 and 155–157 ~145) ≈ 4,920 or less. **Reserve:** 02:113 (94, "A nonexample by minimal change") into a fold, if needed.

### 4.3 Section 1.3: Unions, Intersections, Complements and Families (`03`)

Budget: 4,698 → ≤ 5,000 (expected ~4,800). Folds ≤ 400.

1. **The Idea of `thm-set-algebra` (03:92–94)** is rewritten (≤ 110): keep the uniform license of fd1 Chapter 4. Replace "We also write out two laws in full … (the uniform argument uses one for every law, …)" with "Two of the laws are written out as element-chases in the fold after the proof, and the chain-of-equivalences method below is how a reader proves a new law by hand."
2. **Fold F1.3-a** `title="Two laws by element-chasing, and where each law comes from"`. It takes 03:116 and 03:118 (the two "in full" paragraphs; the proof now ends at "This proves all eight laws."), and 03:120–134 (the source table and the two paragraphs on the difference laws), verbatim, after the proof. Its lead is "Here are two of the laws as element-chases." 03:136 stays on the main line.
3. **`exm-method-chain-of-iff`** `[Method: a chain of equivalences]`, after F1.3-a.
   - **Template.** For L = R: let x be arbitrary. Write x ∈ L ⟺ … ⟺ x ∈ R, one line per step. Each step either unwinds a definition (@def-set-operations) or applies a propositional equivalence to membership statements, with its name on the line. Since ⊣⊢ is used like = (@fd1:prp-provable-equivalence-basics (b)), the chain gives x ∈ L ⟺ x ∈ R, and @def-set-equality finishes.
   - **When to use it.** Identities built from ∪, ∩, ∖ and families, where every step is reversible.
   - **The usual failure.** A step that holds in one direction only, written as ⟺ (for example x ∈ A ⟹ x ∈ A ∪ B). When a chain will not close, look for a small witness instead (@exm-method-counterexample; a membership table finds one).
4. **`exm-difference-chain`** `[A law by a chain]`: "Show that (A ∖ B) ∖ C = A ∖ (B ∪ C)."
   - **`[Scratch work]`**: work from both ends.

     | Givens | Goal |
     |---|---|
     | x arbitrary | x ∈ (A ∖ B) ∖ C ⟺ x ∈ A ∖ (B ∪ C) |
     | left unwound: x ∈ A ∧ x ∉ B ∧ x ∉ C | right unwound: x ∈ A ∧ ¬(x ∈ B ∨ x ∈ C) |
     | gap: x ∉ B ∧ x ∉ C ⟺ ¬(x ∈ B ∨ x ∈ C) | De Morgan (a), (b) (@fd1:prp-de-morgan) |

   - *Solution:* "Let x be arbitrary. x ∈ (A ∖ B) ∖ C ⟺ (x ∈ A ∧ x ∉ B) ∧ x ∉ C [@def-set-operations, twice] ⟺ x ∈ A ∧ (x ∉ B ∧ x ∉ C) [regrouping ∧] ⟺ x ∈ A ∧ ¬(x ∈ B ∨ x ∈ C) [@fd1:prp-de-morgan (a), (b)] ⟺ x ∈ A ∧ x ∉ B ∪ C ⟺ x ∈ A ∖ (B ∪ C). By @def-set-equality the sets are equal." No step needs RAA.
5. **`thm-de-morgan-families`, Idea (03:315).** Add a first clause: "Element-chasing (@exm-method-element-chasing), with 'or' and 'and' replaced by 'for some index' and 'for every index'." The key proof itself is unchanged.
6. **Two Quick checks.**
   - After `exm-difference-chain`: "Which step of the chain fails if B ∪ C is replaced by B ∩ C? Show with a small witness that (A ∖ B) ∖ C = A ∖ (B ∩ C) can fail." *Solution:* De Morgan gives ¬(q ∧ r) ⟺ ¬q ∨ ¬r, not ¬q ∧ ¬r. Take A = {1, 2}, B = {1}, C = {2}: the left side is ∅ and the right side is {1, 2}.
   - After the empty-family paragraph (03:337): "For X = ℝ and the empty index set, what are ⋃ and ⋂?" *Solution:* ∅ and ℝ (@def-family-union-intersection).
7. **B4** `[B4: Prove or disprove]`.
   - (a) A ∖ (A ∖ B) = A ∩ B.
   - (b) (A ∪ B) ∖ B = A.
   - (c) (A ∪ B) ∖ B = A ∖ B.
   - (d) A ∪ (B ∖ C) = (A ∪ B) ∖ C.
   - (e) A ∩ (B ∖ C) = (A ∩ B) ∖ C.
   - *Solution:* (a) True. x ∈ A ∧ ¬(x ∈ A ∧ x ∉ B) ⟺ x ∈ A ∧ (x ∉ A ∨ x ∈ B), by De Morgan (d) and (c) and double negation, classical for (⟹). This is ⟺ (x ∈ A ∧ x ∉ A) ∨ (x ∈ A ∧ x ∈ B) by distributivity, ⟺ x ∈ A ∧ x ∈ B, since the first disjunct is impossible. (b) False: A = B = {1}, where the left side is ∅. (c) True: (p ∨ q) ∧ ¬q ⟺ (p ∧ ¬q) ∨ (q ∧ ¬q) ⟺ p ∧ ¬q. (d) False: A = C = {1}, B = ∅: the left side is {1} and the right side is ∅. (e) True: p ∧ (q ∧ ¬r) ⟺ (p ∧ q) ∧ ¬r (associativity).

Count: +485 − 390 ≈ 4,795.

### 4.4 Section 1.4: Ordered Pairs, Products and Relations (`04`)

Budget: 3,764 → ≤ 4,500 (expected ~4,270). No folds.

1. **`exm-pair-equations`, solution 04:35–40.** Relabel the first paragraph with *Uniqueness.* ("any solution satisfies x + y = 3 and x − y = 1, so x = 2 and y = 1") and *Existence.* ("conversely x = 2, y = 1 is a solution"). The words are kept, the order is kept, two italic tags are added.
2. **`exm-method-uniqueness`** `[Method: existence and uniqueness]`, after 04:44 ("The first part is typical. …").
   - **Template.** "There is exactly one x with P(x)" is two claims (@fd1:def-unique-existence, @fd1:prp-unique-existence-use). For *existence*, name a candidate x₀ and check P(x₀), or obtain one from a given "there exists". For *uniqueness*, take x and x′ with P(x) and P(x′), two names about which nothing else is assumed, and prove x = x′; or show that every x with P(x) equals x₀.
   - **When to use it.** Whenever a definition says "the": the coordinates of a pair, the value f(x), the empty set (@prp-empty-set-unique), an inverse.
   - **The usual failure.** Proving only one half: a uniqueness proof with no candidate, or a candidate never shown to be the only one. Also checking P(x₀) twice and calling it uniqueness, and naming "the" object before either half (N14).
3. **`exm-coordinates-unique`** `[The coordinates of an element of a product]`, after `def-cartesian-product` and (∗) (04:84): "Let p ∈ A × B. Show that there is exactly one a and exactly one b such that a ∈ A, b ∈ B and p = (a, b)."
   - **`[Scratch work]`:**

     | Givens | Goal |
     |---|---|
     | p ∈ A × B | some a ∈ A, b ∈ B with p = (a, b); any two such agree |
     | p = (a, b), a ∈ A, b ∈ B (∃E twice, @def-cartesian-product) | existence: done |
     | p = (a, b) and p = (a′, b′) | a = a′, b = b′: gap is (a, b) = (a′, b′) (=E), then @def-ordered-pair |

   - *Solution:* "*Existence.* By @def-cartesian-product there are a ∈ A and b ∈ B with p = (a, b). *Uniqueness.* If also p = (a′, b′) with a′ ∈ A, b′ ∈ B, then (a, b) = p = (a′, b′), so a = a′ and b = b′ by the characteristic property (@def-ordered-pair)." Aftermath (one sentence): this licenses "**the** first coordinate of p", and so the map p ↦ its first coordinate, which the next section will call a function.
4. **`prp-product-set-laws`, Idea (04:153–156).** Add "As in @exm-method-element-chasing, " at the start; a pair needs its coordinates named first.
5. **Two Quick checks.**
   - After the box: "Is there exactly one real x with (x², x³) = (4, −8)? With (x², x) = (4, 3)?" *Solution:* Yes: x³ = −8 forces x = −2, and (−2)² = 4. No: x = 3 is forced, but 3² ≠ 4, so there is none.
   - After `exm-coordinates-unique`: "Which half of the proof used @def-cartesian-product, and which @def-ordered-pair?" *Solution:* existence used the first, uniqueness the second.
6. **B4** `[B4: Prove or disprove]`.
   - (a) For all real a, b there is exactly one pair (x, y) of reals with (x + 2y, x − y) = (a, b).
   - (b) For every real a there is exactly one pair (x, y) of reals with (x², y) = (a, 0).
   - (c) For all sets A, B, C: if A × B = A × C, then B = C.
   - (d) For all sets A, B, C with A ≠ ∅: if A × B = A × C, then B = C.
   - (e) There is exactly one set E with E × E = ∅.
   - *Solution:* (a) True. Uniqueness: subtracting gives 3y = a − b, so y = (a − b)/3 and x = (a + 2b)/3. Existence: check (a + 2b)/3 + 2(a − b)/3 = a and (a + 2b)/3 − (a − b)/3 = b. (b) False: for a = 1 both (1, 0) and (−1, 0) qualify. (c) False: A = ∅, B = {1}, C = {2}, where both products are ∅. (d) True: fix a ∈ A. For b ∈ B, (a, b) ∈ A × B = A × C, so b ∈ C by (∗); the other inclusion is symmetric. (e) True. Existence: ∅ × ∅ = ∅ (04:168). Uniqueness: if E × E = ∅ and e ∈ E, then (e, e) ∈ E × E, which is impossible, so E has no elements and E = ∅ (@prp-empty-set-unique).

Count: +505 ≈ 4,270.

### 4.5 Section 1.5: Functions, Composition, Injections and Surjections (`05`)

Budget: 5,187 → ≤ 5,000 (expected ~4,990). Folds ≤ 780.

1. **Folds, all verbatim:**
   - F1.5-a `title="Why each clause, and why a codomain"`: 05:96 and 05:98 (201).
   - F1.5-b `title="Where Y^X comes from"`: 05:172 from "It is a set by the working rules …" to "… by specification (W1)." (~70). The sentences on \( m^n \) and \( \{0,1\}^{\nN} \) stay on the main line.
   - F1.5-c `title="The empty function, proved"`: the proof 05:205–211 (130). The statement stays on the main line.
   - F1.5-d `title="Composites defined in one order only"`: 05:241 (37).
   - F1.5-e `title="Part (a) as a derivation"`: 05:443–475 (190).
   - F1.5-f `title="Each hypothesis is needed"`: 05:477 (71).
   - In 05:335, the sentences after "… and its two halves are the two properties." go into F1.5-a's sibling fold F1.5-g `title="Why a bijection reaches each point once"` (~65), with a uniqueness back-reference (@exm-method-uniqueness) added in it.
2. **05:337–344 ("Worked examples" lead and the three bullets, 100)** are replaced by the two boxes, under the heading `### Worked examples`.
   - **`exm-method-injectivity`** `[Method: proving injectivity]`.
     - **Template.** "Let x₁, x₂ ∈ X with f(x₁) = f(x₂)." Compute until x₁ = x₂. To refute, name two different inputs with one output.
     - **When to use it.** Any claim that f is injective; the equation form is the one to compute with (05:294).
     - **The usual failure.** Starting from x₁ = x₂, which proves the wrong implication (N5, the warning 05:399), or assuming x₁ ≠ x₂ and never using it.
   - **`exm-method-surjectivity`** `[Method: proving surjectivity]`.
     - **Template.** On scrap paper, solve f(x) = y for x, working **backwards**, and note what the solving needed. The proof runs **forwards**: "Let y ∈ Y. Put x ≔ …", check x ∈ X, check f(x) = y. To refute, name one y ∈ Y and show f(x) = y has no solution in X.
     - **When to use it.** Any claim that f is surjective.
     - **The usual failure.** Writing the scratch work as the proof, so that the proof assumes y = f(x) and never checks that the x it found lies in X; and testing a few y (N1, the warning 05:323).
3. **`exm-fraction-map`** `[Solving backwards, proving forwards]`, right after the boxes and before `exm-injective-surjective-first`: "Let f: ℝ ∖ {1} → ℝ ∖ {2}, f(x) = 2x/(x − 1). Show that f is a function, and that it is injective and surjective."
   - **`[Scratch work]`** (≤ 20 lines). First, f is a function: the denominator is not 0 for x ≠ 1, and the value is never 2, since 2x/(x − 1) = 2 would give 2x = 2x − 2. Injectivity, three lines: cross-multiply. Surjectivity, backwards: y = 2x/(x − 1) gives yx − y = 2x, so x(y − 2) = y, so x = y/(y − 2), which needs y ≠ 2. This is why 2 was taken out of the codomain. Is the x found in the domain? x = 1 would give y = y − 2, which is impossible. Table:

     | Givens | Goal |
     |---|---|
     | y ∈ ℝ, y ≠ 2 | some x ∈ ℝ ∖ {1} with 2x/(x − 1) = y |
     | x ≔ y/(y − 2), defined since y ≠ 2 | x ≠ 1, and f(x) = y: the two checks left |

   - *Solution:* "*Function:* for x ≠ 1 the formula makes sense, and f(x) ≠ 2, as above. *Injective:* if 2x₁/(x₁ − 1) = 2x₂/(x₂ − 1), then 2x₁(x₂ − 1) = 2x₂(x₁ − 1), so −2x₁ = −2x₂, and x₁ = x₂. *Surjective:* let y ∈ ℝ ∖ {2} and put x ≔ y/(y − 2). Then x ∈ ℝ, and x ≠ 1, since x = 1 would give y = y − 2. Moreover x − 1 = 2/(y − 2), so f(x) = (2y/(y − 2)) / (2/(y − 2)) = y." The aftermath (one sentence) names the order: solve backwards, check forwards.
4. **The five-string game** (bold lead-in `**A game with five strings.**`, ≤ 120 words), after 05:193. "A string of five symbols, each 0 or 1, such as 01101, is a function {1, …, 5} → {0, 1}: its value at k is its k-th symbol. One player writes five such strings, say 00000, 11111, 01010, 10101, 00111. The other must write a string that is not on the list. With 32 strings and five listed, one can always search; but is there a rule that builds a missing string from **any** list of five in five steps, without comparing it against all 32? Try one. Chapter 3 comes back to this game, where the rule settles a question about infinite sets." No answer is given.
5. **05:373.** Replace "Chapter 3 proves facts of this kind in general, starting from the pigeonhole principle." with "Section 2.5 proves facts of this kind in general, from the pigeonhole principle of the lattice-point puzzle of Section 1.1."
6. **Two Quick checks.**
   - After the game: "Which string is the indicator function of {2, 5} ⊆ {1, …, 5}? What is the value at 3 of the string 10110?" *Solution:* 01001; 1.
   - After `exm-fraction-map`: "Show that n ↦ 5n − 2 on ℤ is injective and not surjective." *Solution:* 5n₁ − 2 = 5n₂ − 2 gives n₁ = n₂. Witness 0: 5n = 2 has no integer solution (n ≥ 1 ⇒ 5n ≥ 5; n ≤ 0 ⇒ 5n ≤ 0).
7. **B4** `[B4: Prove or disprove]`.
   - (a) n ↦ n² + n, ℤ → ℤ, is injective.
   - (b) x ↦ x³ + 2x, ℝ → ℝ, is injective.
   - (c) (m, n) ↦ 2m + 3n, ℤ × ℤ → ℤ, is surjective.
   - (d) (m, n) ↦ 2m + 4n, ℤ × ℤ → ℤ, is surjective.
   - (e) x ↦ x² + 4x, from [−2, ∞) to [−4, ∞), is a bijection.
   - *Solution:* (a) False: 0 and −1 both go to 0. (b) True: x³ + 2x = y³ + 2y gives (x − y)(x² + xy + y² + 2) = 0, and x² + xy + y² + 2 = (x + y/2)² + 3y²/4 + 2 > 0, so x = y. (c) True: for k ∈ ℤ, (m, n) = (−k, k) gives −2k + 3k = k. (d) False: 1 is not reached, since 2m + 4n = 2(m + 2n) is even and 1 is odd (@thm-even-or-odd). (e) True: x² + 4x = (x + 2)² − 4 ≥ −4, so the map lands in [−4, ∞). Injective: (x₁ + 2)² = (x₂ + 2)² with both bases ≥ 0 gives x₁ = x₂ (@fd1:thm-squares-order). Surjective: for y ≥ −4 put x ≔ −2 + √(y + 4) ≥ −2; then (x + 2)² − 4 = y.

Count: +600 (boxes net +120, `exm-fraction-map` ~260, game 120, checks 100) − 764 ≈ 5,020; with F1.5-g ≈ 4,960. **Reserve:** 05:193 (51) or 05:213 (41) into F1.5-c.

### 4.6 Section 1.6: Left, Right and Two-Sided Inverses (`06`)

Budget: 4,143 → ≤ 5,000 (expected ~4,540). No folds.

1. **06:21.** "every \( m \in \nN \) is even or odd and not both" gains "(@thm-even-or-odd)".
2. **`thm-left-inverse-iff-injective`, Idea 06:109–118** becomes a **`[Scratch work]`** idea (≤ 20 lines). Keep the (a) paragraph and ① ② ③. Add after ③ the table:

   | Givens | Goal |
   |---|---|
   | f injective, x₀ ∈ X | g: Y → X with g(f(x)) = x for all x ∈ X |
   | Case y ∈ f(X): y = f(x), x unique by injectivity | g(y) ≔ that x |
   | Case y ∉ f(X): nothing is forced | g(y) ≔ x₀ |
   | g defined on all of Y | check (Fn1), (Fn2); then g(f(x)) = x |

   Add "② is a proof by cases (@exm-method-cases)". The *Before reading on* prompt is kept.
3. **`exm-method-construct-and-verify`** `[Method: construct and verify]`, after the proof of the theorem (before 06:154).
   - **Template.** To prove that an object with property P exists: on scrap paper, find where its values are forced and where they are free; define it explicitly, by cases if need be; check that it is the kind of object claimed (for a function, (Fn1) and (Fn2), with values in the codomain); then verify P. For an "if and only if", two directions: one uses the object, the other builds it.
   - **When to use it.** Existence of an inverse, a function or a set with stated properties.
   - **The usual failure.** Verifying P for an object never shown to exist or to be well defined (N14); and a definition that depends on how an input is written (@exm-not-a-function (b)).
4. **`prp-inverse-unique` (06:224).** Add a one-line Idea before the proof: "Uniqueness, as in @exm-method-uniqueness: two candidates, shown equal by computing g ∘ f ∘ h two ways."
5. **Three Quick checks.**
   - After the box: "Construct a left inverse of e: {1, 2} → {1, 2, 3}, e(k) = k + 1, and verify it." *Solution:* g(2) = 1, g(3) = 2, g(1) = 1 (any value in {1, 2} will do at 1); g(e(1)) = g(2) = 1 and g(e(2)) = g(3) = 2.
   - After `thm-bijection-iff-inverse`: "Why does the inverse of a bijection need no fixed point x₀ and no case split?" *Solution:* every y has exactly one preimage, so g(y) is forced at every point.
   - After `exm-two-sided-inverses`: "Give the inverse of f: ℝ → ℝ, f(x) = x³, and verify both composites." *Solution:* g(y) = ∛y, the unique real cube root; f(g(y)) = y, and g(f(x)) = ∛(x³) = x by uniqueness of the real cube root.
6. **B4** `[B4: Prove or disprove]`.
   - (a) f: ℤ → ℤ, f(n) = n + 3, has a two-sided inverse.
   - (b) f: ℕ → ℕ, f(n) = n + 3, has a right inverse.
   - (c) f: ℕ → ℕ, f(n) = n + 3, has a left inverse.
   - (d) For f: X → Y and g: Y → X, if g ∘ f = id_X and f ∘ g ≠ id_Y, then f is not surjective.
   - (e) Every function {1, 2} → {1, 2, 3} has a left inverse.
   - *Solution:* (a) True: g(n) = n − 3, and both composites are the identity. (b) False: 0 is not a value (n + 3 ≥ 3), so f is not surjective and has no right inverse (@prp-right-inverse-surjective). (c) True: g(m) = m − 3 for m ≥ 3 and g(m) = 0 for m < 3. g is a function ℕ → ℕ, and g(f(n)) = n. (d) True: if f were surjective, it would be bijective (it is injective by @thm-left-inverse-iff-injective (a)), with a two-sided inverse h (@thm-bijection-iff-inverse); then g = h by @prp-inverse-unique, so f ∘ g = id_Y, a contradiction. (e) False: the constant map with value 1 is not injective, so it has no left inverse (@thm-left-inverse-iff-injective (a)).

Count: +400 ≈ 4,540.

### 4.7 Section 1.7: Images and Preimages (`07`)

Budget: 4,525 → ≤ 5,000 (expected ~4,840). No folds. Faded: Ideas only, no new box.

1. **"Hunting a counterexample"**, a bold-lead-in paragraph at the start of `## Images and intersections`, after 07:319 (≤ 110): "Suppose we did not know the answer. The inclusion that might fail is f(A) ∩ f(B) ⊆ f(A ∩ B). A failure needs a point y in both images with no preimage in A ∩ B: a preimage a ∈ A and a preimage b ∈ B, with a ≠ b. So f must send two different points to one, and the smallest attempt is A = {a}, B = {b} (@exm-method-counterexample). For squaring, a = −1 and b = 1 is the opening's failure, cut down to two points." 07:319's text stays.
2. **Four Quick checks.**
   - After `def-preimage` (07:58): "For f(x) = x² on ℝ, compute f({−1, 2}) and f⁻¹({4})." *Solution:* {1, 4}; {−2, 2}.
   - After `thm-preimage-operations` (07:263): "Show f⁻¹(Y) = X and f⁻¹(∅) = ∅ for every f: X → Y." *Solution:* every x has f(x) ∈ Y; no x has f(x) ∈ ∅.
   - After the hunting paragraph: "For a constant map c: X → Y with value y₀ and two points x₁ ≠ x₂ of X, compute c({x₁} ∩ {x₂}) and c({x₁}) ∩ c({x₂})." *Solution:* ∅ and {y₀}.
   - After `prp-image-preimage` (07:409): "For f(x) = x² on ℝ, compute f⁻¹(f([0, 1]))." *Solution:* f([0, 1]) = [0, 1] and f⁻¹([0, 1]) = [−1, 1] ⊋ [0, 1].

Exercises and R1–R4 are unchanged. Count ≈ 4,840. **Reserve:** 07:372–376 (126) into a fold.

### 4.8 The edit in Section 2.2 (`22`, done by the 1.1 drafter in the same commit)

- **22:90–94** (the `def-divides` block and the paragraph after it) are replaced by: "Divisibility and primes were defined in Section 1.1: for integers a and b, a | b means b = ka for some k ∈ ℤ (@def-divides), and a prime is an integer p ≥ 2 whose only positive divisors are 1 and p (@def-prime); divisibility is transitive (@prp-divides-transitive). For instance, 3 | 12, with k = 4."
- **22:96** ("Change 12 to 14 …") is kept as it is.
- **22:106–109** (the `def-prime` block) are deleted. 22:111 is prefixed with "Recall @def-prime. ".
- **22:284.** "as in the example \( 3 \mid 4^n - 1 \) after @def-divides" becomes "as in the example \( 3 \mid 4^n - 1 \) at the start of this subsection".
- **Ledger.** Re-key 22's ledger lines 450–452 with `tools/ledger.py` (coordinator, S4).
- **Left to `ch02-deepen`:** 22:3 ("proves facts … every integer is even or odd and not both") and 22:151–154. These should now say that Section 1.1 proved even-or-odd (@thm-even-or-odd) and that the division algorithm gives it again with n = 2.

### 4.9 Chapter-pointer hand fixes in Chapter 1 (not covered by renumber.py)

| Where | Now | Becomes |
|---|---|---|
| 03:175 | "proved in Chapter 3" | "proved in Section 2.5" |
| 04:288, 04:291 | "Chapter 2" (relations) | "Chapter 4" |
| 05:93 | "returns in Chapter 2 for functions defined on classes" | "returns in Chapter 4 …" |
| 05:172 | "counting is Chapter 3's business" | "counting is the business of Section 2.5" |
| 05:193 | "which Chapter 3 solves" | "which Section 2.5 solves" |
| 05:373 | "Chapter 3 proves facts …" | as in §4.5 item 5 |

These stay as they are: 02:245, 02:381, 03:191, 05:93 ("well-ordering, proved in Chapter 2"), 05:172 ("{0,1}^ℕ … Chapter 3"), 06:218 and 06:347 (choice, now 3.2).

## 5. Budgets and Time

| § | Main now | Budget | Expected | Folds |
|---|---|---|---|---|
| 1.1 | — | 4,500 | ~4,350 | 0 |
| 1.2 | 5,069 | 5,000 | ~4,850 | ~640 |
| 1.3 | 4,698 | 5,000 | ~4,800 | ~390 |
| 1.4 | 3,764 | 4,500 | ~4,270 | 0 |
| 1.5 | 5,187 | 5,000 | ~4,990 | ~830 |
| 1.6 | 4,143 | 5,000 | ~4,540 | 0 |
| 1.7 | 4,525 | 5,000 | ~4,840 | 0 |
| total | 27,386 | 34,000 | ~32,640 | ~1,860 |

**Exercises.** New items: 1.1's eight; six B4s. Core track: all A, one B and one C per section, R1–R4. The Time line is recomputed by `check_structure.py --words` (layout §2: about 40 h core, about 50 h full) and written into the index by the coordinator after S3.

## 6. Pointers, promises, edits outside the chapter

- **Forward pointers.** 1.1's Looking-ahead (pigeonhole → 2.5; a promise row in STATUS, paid by `thm-pigeonhole` and 2.5's "Back to the pigeons"). The 1.5 game names "Chapter 3" in prose (a promise row, paid by 3.3's "Back to the five strings"). Russell → Cantor is already prose at 02:381 (paid by `thm-binary-sequences-uncountable`'s section, 3.3).
- **NOTATION.** In the `d \mid n` row, "formally defined in F2.2 §02, `def-divides`" becomes "F2.1 §01". Add a row "even, odd: n = 2k, n = 2k + 1 with k ∈ ℤ (F2.1 §01, `def-parity`)".
- **fd3 `ch03…/index.md:7`** ("Two integers, one theory"). "Chapter 2 proved its facts about divisibility" becomes "Chapters 1 and 2 proved …". Add the twins: transitivity (@fd2:prp-divides-transitive) ↔ @prp-divisibility-rules-integers (b), and even or odd (@fd2:thm-even-or-odd) ↔ @cor-integers-even-odd (a), both in Section 3.1. This is part of layout §3.3's sweep, but the coordinator does it with this chapter's S4.
- **STATUS.** Add rows for the two promises above. Retag F2.2 §02 `def-divides`/`def-prime` → F2.1 §01. The renumber note from binding rule 5.
- **Not touched:** fd1. Layout §3.3's other prose pointers (fd3, fd4, "Section 2.2" → 1.1 where it means divides or prime) are left to the sweep.

## 7. S2a: claims to verify

1. 1.1 Quick check (weird examples): 0 even; 0 | 0; 0 ∤ 5; −7 odd; 12 ∤ 3.
2. `prp-divides-transitive`: the proof and its table; no use of `prp-integers-closed`.
3. `exm-divides-combination`, with its three special cases and the link to `@fd1:exm-sum-of-evens`.
4. The Quick check a = 1, b = 2, c = 6: no single k.
5. `thm-even-or-odd`: the induction (base, both step cases), the negative cases (−2k − 1 = 2(−k − 1) + 1), and not-both (c ≥ 1 or c ≤ 0).
6. `exm-cubes-plus-five-n`: both expansions.
7. `exm-parity-of-sums`: (a) both cases, (b) the WLOG licence (symmetric statement and hypothesis).
8. `exm-refute-2p-plus-1`: 2, 3, 5, 7 prime; 15 = 3·5; 5, 7, 11, 23 prime (Quick check).
9. `exm-refute-divides-product`: 4 | 4, 4 ∤ 2; the product of two odds is odd; the fd3 pointer is prose only (fd3 proves Euclid's lemma in Chapter 3; check the section).
10. n = 3 divides 2³ + 1.
11. Lattice: the six midpoints of the four points; patterns exhaustive and exclusive; `exm-lattice-midpoint`; the Quick check (−3, 8) and (1, 0) with midpoint (−1, 4); no claim rests on pigeonhole.
12. 1.1 A1–C3 answers. In particular B4 (c) (j = 2k² + 2k), B4 (b) (1 and −1), C1 (b) (the three expansions), C1 (c) (m = 6(a − b)), C2 (the N5 diagnosis and its counterexample to the step), C3 (eight points; 2³ patterns).
13. 1.2: the transitivity scratch work and the short proof are equivalent to the folded derivation; the folds F1.2-a…e hold no cited statement and no section's only check or warning; 02:19's pointer into F1.2-e still resolves; Quick checks; B4 (a)–(e).
14. 1.3: the folded F1.3-a leaves the proof of `thm-set-algebra` complete (the uniform argument proves all eight laws); `exm-difference-chain` (De Morgan (a), (b) without RAA); Quick checks; B4 (a) (the classical step), (b)–(e).
15. 1.4: the relabelled `exm-pair-equations`; `exm-coordinates-unique`; Quick checks; B4 (a)–(e), with (e)'s citation 04:168.
16. 1.5: `exm-fraction-map` (well-definedness, injectivity, x ≠ 1, f(x) = y, x − 1 = 2/(y − 2)); the game's 32 strings and the indicator 01001; Quick check 5n − 2; B4 (a)–(e), with (b)'s positivity and (e)'s range check; the folds hold no cited statement (`prp-empty-function`'s statement stays on the main line).
17. 1.6: the scratch-work table; the Quick checks (e, ∛); B4 (c)'s g is a function ℕ → ℕ; B4 (d)'s argument cites only earlier results.
18. 1.7: the hunting paragraph; the four Quick checks.
19. 2.2: after the edit, every `@def-divides` and `@def-prime` in fd2, fd3 and fd4 resolves to 1.1, and 22's remaining text (22:96, 22:111) reads correctly.

## 8. Notes for S3 and S4

- **Before S3:** the coordinator runs renumber.py (binding rule 5) and commits.
- **Drafters:** three. (i) 1.1, the 2.2 edit and nothing else; it lands first, since later drafters cite `def-divides`, `thm-even-or-odd`, `exm-method-cases`, `exm-method-counterexample` and `prp-divides-transitive`. (ii) 1.2, 1.3 and 1.4. (iii) 1.5, 1.6 and 1.7. The coordinator writes the index last, against the delivered sections. Sonnet may take (iii)'s 1.6 and 1.7 (minor changes; lean workflow).
- **Sidecars** (`fd2/verify/ch01/`, new):
  - `exm-refute-2p-plus-1.py`, `exm-refute-divides-product.py`, `exm-cubes-plus-five-n.py`, `exm-lattice-midpoint.py` (including the four-point counterexample), `exm-fraction-map.py` (exact Fractions);
  - `exr-proofs-from-definitions-b4.py`, `exr-proofs-from-definitions-c1.py`;
  - `exr-sets-and-subsets-b4.py`, `exr-set-operations-b4.py` (with `_sets.py`), `exr-products-and-relations-b4.py`, `exr-functions-b4.py`.
- **Checkers:** `check_structure.py` (0 fatal; main line ≤ 5,000 per section by `--words`), `check_fitch.py` (the derivations moved into F1.2-e and F1.5-e unchanged), `check_numbers.py`, `check_notation.py`, the forward-deps check (1.1 cites nothing after 1.1 except fd1).
- **Review (lean workflow):** 1.1, 1.2 and 1.5 run the full pipeline (layout §7). 1.3, 1.4, 1.6 and 1.7 get a changed-only blind review: the boxes, scratch work, tables, B4s, checks and folds count as changes.
- **Open for the author:** none blocking. Two calls were made here. First, (Q1) is left "yes, once pigeonhole is proved" rather than proved, since layout §5 says nothing is proved from pigeonhole in 1.1. Second, parity of products appears only in the scratch work and in exercises, not as a labelled result.
