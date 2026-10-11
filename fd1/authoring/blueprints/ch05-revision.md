<!-- hand-written -->
# Revision blueprint: F1.5 From Derivations to Mathematical Prose (fd1 Chapter 5), R5

**What this is.** A **delta** blueprint (stage S1) for revising the released Chapter 5 of *Logic and Proof* so that a first-year reader gets in more easily. It is complete on its own: a drafter executes it with this file, the current `fd1/src/ch05-from-derivations-to-prose/`, the original blueprint `fd1/authoring/blueprints/ch05.md` (for anything this file does not change), `authoring/STYLE.md` (§11, §12), `DRAFTING.md` and `NOTATION.md`. The approved pilot `ch01-revision.md` is the model of format and register; where this file is silent on a convention, do what that file did. The frozen `ch02-revision.md` and `ch03-revision.md` are assumed delivered: every pointer below into Chapters 2 and 3 is checked against the text those files produce (rule cards, folds, Looking-ahead boxes, renumbered Chapter 1 pointers). All line numbers are of the **current** files (commit `da6e12e`), written `03:42` for `03-levels-of-abbreviation.md` line 42, and so on; `ix` is `index.md`. The Chapter 1 "Section 1.x" sweep (ch01-revision §6) has already been applied to this chapter (06:38-43 read "Section 1.4", "Section 1.6"; 01:137 "Section 1.6"; 02:137 "Section 1.3"); nothing below reverses it.

**Inputs.** The novice-reader report on Chapter 5 (workflow journal, `novice:ch05`), the fd1 revision plan (§2 Chapter 5 rows, §3 Chapter 5 items, §4–§6), the pilot, and the two frozen R3 blueprints. Reference books were used for teaching technique only (prose before the derivation, a picture for dependence, an easy instance before a hard one, errors grouped by family). **Every new example, figure, drill and exercise below is the book's own.** The S2 rules of `ch05.md` still bind: the self-explanation passage must not reuse the Loughborough booklet's example; every result of 5.7 stays `.optional`; `exm-not-allowed-catalogue` keeps entries (N1)–(N11) as a labelled list.

**Binding rules for this revision.**
1. **No label is lost.** Every label now in the chapter survives, in this chapter and in its section, with its content. Only uncited `exr-` labels change, each named in §3. The heading ids `what-the-sentence-does-not-say`, `one-extra-rule` and `what-a-proof-provides` are kept (STATUS row 74 names the last two).
2. **Reviewed content of cited results does not change.** `exm-not-allowed-catalogue` (cited 58 times in fd2, fd3, fd4) keeps every entry, its number, its rule and its instances; the one change is that (N11)'s three errors become lettered parts (a)–(c) of (N11), with one new instance for (a) (§4.6, S2a item 1). `def-levels-of-proof` and `def-silent-steps` are kept **verbatim** on the main line. `exm-rhetoric-universal`, `exm-rhetoric-induction`, `exr-connective-rhetoric-c1` (frozen), `thm-irrational-power-rational`, `prp-log2-9-irrational` keep their statements and solutions/proofs verbatim; `exm-rhetoric-existential` changes two phrases of its solution (§4.2, S2a item 2). Moving a passage into a Second-reading fold verbatim is not a change.
3. **Forward pointers.** No `@ref` to an unseen result is a reason. Each section's main line and folds carry **at most one** pointer to a later volume (or later chapter of another volume), in its Looking-ahead box (STYLE §12.1). This chapter is the last of the volume, so every such pointer is to *Sets, Relations, and Cardinality* or *Analysis on the Real Line*; the chapter now has three boxes (5.3, 5.6, 5.7), and every other pointer found by the grep of 2026-10-12 is cut or reworded as a non-promise (lists per section). Pointers to later sections **of this chapter** stay where they help, never as reasons. Plain pointers inside exercise statements and solutions stay only where this file keeps them. After drafting, grep each section's main line and folds for `Analysis on the Real Line`, `Sets, Relations`, `Number Systems`, `later volume`, `this series`; every hit other than the box is cut.
4. **Depends on R1 only.** Fold, Looking-ahead and drill-bank markup follow STYLE §12 as amended by R1. The derivation renderer of R0 changes nothing here; the colour highlighting asked for in the index (§4.0) waits for R0's row ids and is never the only carrier.

---

## 1. The volume-wide conventions, as applied to Chapter 5

Chapter 5 introduces **no rule of inference**, so it has no rule sections. The conventions STYLE scopes to rule sections apply as follows:
- **No snapshots** (STYLE §12.4 scopes them to Chapters 1–2 and 4.4–4.6). The worked derivations here are reprints, skeletons and level texts, each shown beside its prose.
- **One rule card**, at the top of 5.1 (the plan's "rule card at the top"): the chapter-wide reference card of every rule, its shape, its phrase and whether it may be silent (§4.1 item 2). No per-section cards.
- **The Givens/Goal table** appears once, as step 1 of 5.5's procedure and in its worked example (STYLE §12.5 names that place).

The conventions that do apply:
1. **Second-reading fold.** `::: {.second-reading title="…"}`, not `.optional`. Every fold is listed by current file:line below; nothing else goes into a fold. A fold never sits inside a `.proof`, `.solution` or `.claim` div: where part of a solution is folded, the fold follows the solution as a sibling (as ch03-revision §1 item 1).
2. **Looking ahead.** `::: {.remark}`, then the title line `[Looking ahead]`, a blank line and the sentence, as STYLE §12.1's template and delivered Chapter 1 have it. The last block before `## Exercises`. Three in this chapter: 5.3, 5.6, 5.7 (texts in §4). The index has none and no "Where this goes" note: its two later-volume sentences (ix:9) move to 5.3's box.
3. **Effort in proportion to difficulty** (STYLE §12.2) and **edge cases** (§12.3): the degenerate and minimal-change passages listed per section go to folds.
4. **Quick-check density** (§12.7): about one per 800–1,000 main-line words; the new checks are written out per section.
5. **Drill banks** (§12.8): STYLE requires them only of rule sections. This chapter adds `[A2: Drill]` to 5.1, 5.2, 5.3 and 5.6 (recognition and judgement: which rule a phrase carries, may it be silent, which entry a line commits), 8–10 parts each, answers in **one folded solution**, one or two lines per part. 5.4, 5.5 and 5.7 get none (their A1 already drills the one habit each teaches).
6. **School-level first** (§12.9): every section's first example is school mathematics (parity, divisibility, inequalities, a small set); ε–δ, uniform continuity and least upper bounds come after, as payoff.
7. **Rule tags.** New examples tag only the structural steps (openings, closings, choices, case splits, clashes, citations) and the rows of the group they illustrate, and write "algebra" for the rest (plan, 5.1). Kept examples keep their tags as printed, except `exm-annotate-abs` (§4.5) and the "arith" tags of new text, which read "algebra".
8. **Spelling.** No "non-" form in the chapter needs hyphenation (`noncomputable` is Lean code). New text writes non-zero, non-empty, non-negative.

---

## 2. Section map

| Sec | Title (the `#` line, unchanged) | File (unchanged) | Kind |
|---|---|---|---|
| index | From Derivations to Mathematical Prose | `index.md` | rewritten |
| 5.1 | The Connective Rules in Prose | `01-connective-rhetoric.md` | rewritten |
| 5.2 | The Quantifier Rules in Prose | `02-quantifier-rhetoric.md` | edited |
| 5.3 | Four Levels of One Proof | `03-levels-of-abbreviation.md` | rewritten |
| 5.4 | Reading a Proof: Self-Explanation | `04-reading-proofs.md` | nearly kept |
| 5.5 | Writing a Proof | `05-writing-proofs.md` | edited |
| 5.6 | Checking Proofs, and What Is Not Allowed | `06-checking-proofs.md` | edited |
| 5.7 | The Dispute over Excluded Middle | `07-excluded-middle.md` | edited |

Section numbers, titles and file names do not change: fd2 and fd3 name "*Logic and Proof*, Chapter 5" and "Section 5.1/5.2/5.3/5.6/5.7" about 30 times (§6), and fd1 Ch2–Ch4 point at "Chapter 5" eleven times. `##` headings that change: 5.1 gains "The rule card" and "Which steps may go unsaid"; 5.2's "Induction, lemmas and symmetry" gains three `###` subsections; 5.3 "One proof, four texts" → "One short proof, four texts", "Uniform continuity, four times" → "Uniform continuity, twice"; 5.5 "From the goal to prose" → "The procedure, run once" (moved up); 5.7's subsections are reordered (§4.7). No link anywhere targets any changed heading (grep of 2026-10-12 for `#` + each slug in fd1–fd4 and an1: only the three kept ids exist, and none is linked).

---

## 3. Labels

### 3.1 Every label now in the chapter

Citation counts are `@label` / `@fd1:label` hits (grep of 2026-10-12): "out" = fd1 Ch1–4, fd2, fd3, fd4, an1 (fd1 Ch1–4 and an1 cite none of this chapter's labels; the column says which volume); "in" = inside Chapter 5. Hand-written mentions are in §6.

| Label | Now | Status | Out | In |
|---|---|---|---|---|
| `exm-rhetoric-conjunction` | 01:83 | kept; **content replaced** by a school-level example (§4.1 item 7; S2a); the old content (least upper bound) moves verbatim to new `exr-connective-rhetoric-b3` | — | — |
| `exm-rhetoric-implication` | 01:110 | kept, unchanged | — | — |
| `exm-rhetoric-cases` | 01:139 | kept, unchanged | — | — |
| `exm-rhetoric-negation` | 01:176 | kept, unchanged | — | — |
| `exm-rhetoric-contradiction` | 01:201 | kept; statement drops the ¬I/¬¬E rewrite, which moves verbatim to fold F5.1-b after the solution (S2a) | — | 2 |
| `exm-rhetoric-biconditional` | 01:228 | kept, unchanged | — | — |
| `exm-costume-direct` | 01:268 | kept, unchanged | — | 2 |
| `exm-costume-contrapositive` | 01:286 | kept, unchanged | — | 1 |
| `exr-connective-rhetoric-a1` | 01:314 | kept; (d)'s solution reworded (no volume pointer) | — | — |
| `exr-connective-rhetoric-b1`, `-b2` | 01:337, 01:356 | kept | — | — |
| `exr-connective-rhetoric-c1` | 01:380 | **frozen** (fd3 03:416, fd3 ch03 index:9): label, tier, content unchanged, stem's pointer kept | fd3 2 | — |
| `exr-connective-rhetoric-c2` | 01:412 | kept; one solution sentence reworded (01:448) | — | — |
| `exm-rhetoric-universal` | 02:33 | kept, verbatim | fd2 1 | — |
| `exm-rhetoric-existential` | 02:61 | kept; solution's 02:68 preamble compressed, "cut" → "it suffices" (S2a) | fd2 1 | 2 |
| `exm-rhetoric-equality` | 02:106 | kept, unchanged | — | — |
| `exm-rhetoric-induction` | 02:139 | kept, verbatim; now after the three new subsections | fd2 2 | — |
| `exr-quantifier-rhetoric-a1` … `-c2` | 02:194–308 | all five kept | — | — |
| `def-levels-of-proof` | 03:13 | kept, **verbatim**, after the new opening example | fd2 2 | 4 |
| `def-silent-steps` | 03:42 | kept, **verbatim**, on the main line after the principle and a six-row table (§9 D1) | — | 20 |
| `exm-sqrt2-four-levels` | 03:92 | kept; solution reordered level 3 → 2 → 1 with \( L(r, p, q) \); level 0 and its paragraphs in fold F5.3-b; the prompt asks about level 1 (S2a) | — | 2 |
| `exm-uniform-four-levels` | 03:207 | kept; statement "levels 1 and 3"; levels 0 and 2 in fold F5.3-c (S2a) | — | 1 |
| `exr-levels-of-abbreviation-a1` | 03:319 | kept; (a), (b), (d) reworded for the main-line levels | — | — |
| `exr-levels-of-abbreviation-b1` | 03:347 | kept | — | — |
| `exr-levels-of-abbreviation-b2` | 03:384 | kept, **scaffolded**: same claim and level-3 proof, its solution's skeleton now printed with nine blanks; the new `-c3` is a different claim (S2) | — | — |
| `exr-levels-of-abbreviation-c1`, `-c2` | 03:449, 03:501 | kept (C2 is an exit check) | — | — |
| `exm-self-explanation` | 04:19 | kept, unchanged | — | 3 |
| `exr-reading-proofs-a1`, `-b2` | 04:121, 04:190 | kept | — | — |
| `exr-reading-proofs-b1` | 04:156 | kept; new plain-words solution, the old solution verbatim in a fold after it | — | — |
| `exr-reading-proofs-c1` | 04:212 | old item **moves** to new `-c2` (titled Challenge); the label now carries a new item (uniqueness of limits by contradiction) | — | — |
| `exm-annotate-abs` | 05:51 | kept; table relabelled structurally, old table and 05:75 in fold F5.5-b (S2a) | — | 1 |
| `exm-write-from-derivation` | 05:80 | kept; 05:112's last sentence reworded (no volume pointer) | — | — |
| `exm-subset-bounded-above` | 05:119 | kept; **moved** to right after the procedure; gains a Givens/Goal table (S2a) | — | — |
| `exr-writing-proofs-a1` … `-c2` | 05:179–441 | all seven kept (B2 ordering, B3 faded) | — | — |
| `exm-not-allowed-catalogue` | 06:28 | kept; (N11) split into parts (a)–(c) with one new instance; families table before the block (S2a item 1) | fd2 17, fd3 20, fd4 21 | 7 |
| `exm-verify-cases`, `-converse`, `-negation`, `-scope` | 06:66–129 | kept, unchanged | — | — |
| `exr-checking-proofs-a1` … `-c3` | 06:160–352 | all six kept (C1 faded, C3 exit check) | — | — |
| `prp-not-not-excluded-middle` (`.optional`) | 07:34 | kept, statement and proof verbatim (key proof) | — | 2 |
| `thm-irrational-power-rational` (`.optional`) | 07:123 | kept verbatim; **moved** to the opening of 5.7 | fd2 1 | 2 |
| `prp-log2-9-irrational` (`.optional`) | 07:157 | kept verbatim; moved with it | fd2 1 | 1 |
| `exr-excluded-middle-a1` … `-r4` | 07:237–561 | all twelve kept | — | — |

### 3.2 New labels

`exr-connective-rhetoric-a2`, `-b3`; `exr-quantifier-rhetoric-a2`; `exr-levels-of-abbreviation-a2`, `-c3`; `exr-reading-proofs-c2`; `exr-checking-proofs-a2`; `exr-excluded-middle-b4`. All eight are free (grep of `fd1`–`fd4` on 2026-10-12: no hit). No new `def-`, `prp-`, `thm-` or `exm-` label: the new examples of 5.1 (inside `exm-rhetoric-conjunction`), 5.3 (the four-level opening) and the index are either in a kept label or unlabelled prose.

### 3.3 Bookkeeping the moves force (coordinator, S4)

- `fd1/authoring/ledger/ch05.yaml`: re-key the entry of `exm-rhetoric-conjunction` to `exr-connective-rhetoric-b3` (its content moved verbatim; verdicts kept, all stale by hash) and open a new `exm-rhetoric-conjunction` entry; re-key `exr-reading-proofs-c1` → `-c2` the same way, with a new entry for the reused label. `exr-levels-of-abbreviation-b2` keeps its key (same claim, now scaffolded; verdicts stale by hash), and `exr-levels-of-abbreviation-c3` is a new entry. Every other entry keeps its key; every touched block's hash changes and its verdicts go stale (S5–S8 re-review). Retired entries, if any, go to `fd1/authoring/ledger/archive/ch05-r5-retired.yaml`.
- `fd1/verify/ch05/`: rename `exm-rhetoric-conjunction.py` → `exr-connective-rhetoric-b3.py` and write a new `exm-rhetoric-conjunction.py`; keep `exr-levels-of-abbreviation-b2.py` (the scaffolded B2 quotes the same values) and write `exr-levels-of-abbreviation-c3.py` for the new C3; extend `exm-not-allowed-catalogue.py` with (N11)(a)'s instance and the 2×2 table's values; new sidecars per section below.
- The in-file dependency ledgers: lines move with their blocks; new lines per section below.

---

## 4. Per-section plans

Budgets: **main line** = `prose_words` of `tools/check_structure.py`, counted outside `.second-reading` folds and before `## Exercises`. Exercises are budgeted separately. Totals in §5.

### 4.0 `index.md` (rewritten)

**Budget:** ≤ 1,100 words (now 1,001); fold ≤ 300.

1. `# From Derivations to Mathematical Prose`.
2. **Hook (new, ~200 words, replaces ix:3-7).** Lead: "Here is a proof that every schoolbook prints: for an integer \( n \), if \( n \) is even, then \( n^2 \) is even." The prose, as a quotation:

   > Suppose \( n \) is even, say \( n = 2k \). Then \( n^2 = 4k^2 = 2(2k^2) \), so \( n^2 \) is even.

   Then: "And here is the same proof as a derivation, for one fixed integer \( n \), with 'even' written out: \( n \) is even when \( n = 2k \) for some integer \( k \)." The derivation (6 lines; the integer \( n \) fixed, so no ∀I; domain ℤ):

   ```
   1 | ∃k (n = 2·k)                      assumption
   2 | | n = 2·k₀                        assumption, flag k₀ (∃E box)
   3 | | n·n = 2·(2·k₀·k₀)               arith 2
   4 | | ∃j (n·n = 2·j)                  ∃I 3
   5 | ∃j (n·n = 2·j)                    ∃E 1, 2–4
   6 ∃k (n = 2·k) → ∃j (n·n = 2·j)       →I 1–5
   ```
   (`\open \hypo{1}{\exists k\,(n = 2 \cdot k)} \open[k_0] \hypo{2}{n = 2 \cdot k_0} \have{3}{n \cdot n = 2 \cdot (2 \cdot k_0 \cdot k_0)} \by{arith}{2} \have{4}{\exists j\,(n \cdot n = 2 \cdot j)} \Ei{3} \close \have{5}{\exists j\,(n \cdot n = 2 \cdot j)} \Ee{1,2-4} \close \have{6}{\exists k\,(n = 2 \cdot k) \to \exists j\,(n \cdot n = 2 \cdot j)} \ii{1-5}`.) The side condition at line 5: \( k_0 \) is not in line 5, not in line 1, and in no other open assumption.

   Then the **alignment table** (two columns of the hook; in the web edition, once R0's row ids exist, the words and the box they open may share a highlight colour, never as the only carrier):

   | Words | Lines | What they do |
   |---|---|---|
   | "Suppose \( n \) is even" | 1 | open the →I box |
   | "say \( n = 2k \)" | 2 | open the ∃E box, with a new name |
   | "Then \( n^2 = 4k^2 = 2(2k^2) \)" | 3 | algebra inside both boxes |
   | "so \( n^2 \) is even" | 4 | ∃I, with the witness \( 2k^2 \) |
   | (the paragraph ends) | 5, 6 | the two boxes close |

   Then ix:7 from "Words such as 'let', 'choose', 'suppose' and 'in either case' are the boxes, spoken." to the end of the paragraph, verbatim (the slogan, "This chapter makes that correspondence exact in both directions", hearing/speaking). The analysis paragraph ix:3-5 and ix:7's first four sentences are **cut** (uniform continuity is 5.3's payoff, where `exm-uniform-four-levels` prints the same paragraph).
3. **Second hook (new, ~130 words): Proof B.** "Words can also deceive. Here is a proof whose every sentence is true and which is still wrong." Then the claim and lines (1)–(5) of `exm-verify-converse` (06:90-92) as a quotation, without its label, then: "Every sentence is true, and so is the claim. But the box opens with '\( n \) is even', so what the lines prove is the converse, 'if \( n \) is even, then \( n^2 \) is even'. Section 5.6 checks this proof line by line; by the end of the chapter you will see the error at a glance."
4. **The chapter in one paragraph** (ix:9, cut to ~70 words): "The chapter builds a dictionary from rules to phrases, writes proofs at four levels from full derivation to plain prose, fixes which steps plain prose may leave unsaid, and turns all of this into habits for reading, writing and checking proofs, with a catalogue of the errors that recur. It ends with the one rule mathematicians have seriously argued about: reductio ad absurdum." ix:9's two sentences on later volumes move to 5.3's Looking-ahead box.
5. **What you need** (replaces ix:11; four bullets, ~90 words):
   - **Boxes.** An assumption opens a box, the line written after it closes it, and a line may cite only lines and boxes available to it (@def-derivation).
   - **The rules.** The introduction and elimination rules of every connective and quantifier, and the derived rules of Chapter 2; Section 5.1 collects them on one card.
   - **Choosing.** "Choose" needs a fresh name, and a chosen constant may depend only on the names of the boxes around it (Sections 4.6 and 4.10).
   - **The classical rule.** RAA is the one rule that belongs to no connective; ¬¬E and LEM are its other two forms (Section 2.5).

   Then fold F5.0-a `title="Every earlier result this chapter cites"`: ix:11 verbatim from "From Chapters 1 and 2:" to the end, with "the proof of @lem-atom-splitting" → "the proof of @lem-atom-splitting (for a Challenge exercise of Section 5.4)".
6. **Time:** recomputed from the delivered text (§5). §5's estimate: about 31 hours on the core track, about 47 for everything.
7. **Roadmap** (seven bullets, replacing ix:17-23):
   - **The connective rules in prose.** The rule card for the whole chapter, and which steps may go unsaid; the dictionary rows for the connectives and the classical rules, each with a short proof annotated phrase by phrase; why ¬I and RAA are told apart; the three faces of "proof by contradiction"; the costumes.
   - **The quantifier rules in prose.** The rows for "for every", "there exists", equality and unique existence; what a chosen constant depends on, in a picture and in numbers; "it suffices to show", induction and "without loss of generality"; the quantifiers that English leaves unwritten or puts in the wrong place.
   - **Four levels of one proof.** One short proof written four times; the levels named; the convention on silent steps; the irrationality of \( \sqrt 2 \) and "uniformly continuous implies continuous" at the levels that show most; how to check a doubtful sentence by expanding it.
   - **Reading a proof: self-explanation.** ix:20 verbatim.
   - **Writing a proof.** A seven-step procedure, run at once on one example; scratch paper against the page; the conventions of written mathematics; two more examples.
   - **Checking proofs, and what is not allowed.** Two questions for every line; the catalogue (N1)–(N11) in six families; four student proofs checked line by line.
   - **The dispute over excluded middle.** A proof of existence that names nothing; what a proof provides under the BHK reading; reductio as the one extra rule; why excluded middle cannot be refuted; a short history; what analysis would lose; proofs as programs; the book's position.
8. **Named moves:** ix:25-32 verbatim (six moves).

**Sidecar:** `verify/ch05/index-hook.py` is not needed (one identity, \( (2k)^2 = 2(2k^2) \)); the ledger line cites school algebra.

### 4.1 Section 5.1: The Connective Rules in Prose (`01-connective-rhetoric.md`, rewritten)

**Budget:** main line ≤ 4,750 words (now 4,400); folds ≤ 450. (Raised at S2 from 4,300: measured with `prose_words`, the cuts and rewordings below remove about 630 words and the additions come to about 950–1,000, since the card's table text counts. The section stays under STYLE's 5,000.) **No Looking-ahead box** (no later-volume pointer survives on the main line).

**New order of material.**
1. **Opening frame** (01:3, cut to ~80 words, no volume pointer): "Chapters 1–4 built a calculus in which every step of a proof is one rule applied to lines that are available. Mathematicians do not write Fitch boxes; yet every proof they write is a derivation underneath, written in sentences. This section and the next compile the dictionary between the two: for each rule, the phrases that carry it, a sentence in which it does its work, and whether a writer may leave it unsaid. This section covers the connectives and the classical rules; Section 5.2 the quantifiers, equality and induction."
2. `## The rule card` **(new; ~70 words of prose + the table).** Lead: "Here is every rule of the book on one card: its shape, the words that carry it in a written proof, and whether plain prose may leave it out. The last column is explained in the next subsection; Section 5.2 gives the quantifier rows their examples." The card (columns as Chapter 1's card, `ch01-connectives-and-derivations/07-disjunction-and-cases.md` lines 680-689 as delivered, with the column heads "Rule | Shape | You write" kept and the Lean column replaced by the silence column; the shapes of the Chapter 1 rows are copied from that card, so ∨I reads "\( \varphi \) ⟹ \( \varphi \vee \psi \) (or \( \psi \vee \varphi \))" and R "\( \varphi \) (available) ⟹ \( \varphi \), copied"):

   | Rule | Shape | You write | Silent in plain prose? |
   |---|---|---|---|
   | ∧I | \( \varphi \), \( \psi \) ⟹ \( \varphi \wedge \psi \) | "…, and …"; "both hold" | when both parts are displayed |
   | ∧E | \( \varphi \wedge \psi \) ⟹ \( \varphi \) (or \( \psi \)) | "in particular" | yes |
   | →I | box \( \varphi \) … \( \psi \) ⟹ \( \varphi \to \psi \) | "Suppose \( P \). … So \( Q \)." | the opening never; the closing yes |
   | →E | \( \varphi \to \psi \), \( \varphi \) ⟹ \( \psi \) | "since …"; "by (the lemma), …" | yes when the implication is a line of the proof itself; never when it is a hypothesis or a cited result |
   | R | \( \varphi \) (available) ⟹ \( \varphi \), copied | "recall that" | yes |
   | ∨I | \( \varphi \) ⟹ \( \varphi \vee \psi \) (or \( \psi \vee \varphi \)) | "so certainly … or …" | yes |
   | ∨E | \( \varphi \vee \psi \), box \( \varphi \) … \( \chi \), box \( \psi \) … \( \chi \) ⟹ \( \chi \) | "Case 1 … Case 2 … In either case" | the split and why it is exhaustive never; "in either case" yes |
   | ¬I | box \( \varphi \) … \( \bot \) ⟹ \( \neg\varphi \) | "Suppose \( P \). … a contradiction. Hence not \( P \)." | never |
   | ¬E | \( \varphi \), \( \neg\varphi \) ⟹ \( \bot \) | "this contradicts …" | never: both lines of the clash are named |
   | ⊥E | \( \bot \) ⟹ \( \varphi \) | "this case cannot occur" | yes, once the clash or the empty case is stated |
   | ↔I | box \( \varphi \) … \( \psi \), box \( \psi \) … \( \varphi \) ⟹ \( \varphi \leftrightarrow \psi \) | "\( (\Rightarrow) \) … \( (\Leftarrow) \) …"; "conversely" | never either direction |
   | ↔E | \( \varphi \leftrightarrow \psi \), \( \varphi \) ⟹ \( \psi \) | "that is"; "by definition" | yes, for a definition |
   | RAA | box \( \neg\varphi \) … \( \bot \) ⟹ \( \varphi \) | "suppose, for a contradiction, that not \( P \)" | never |
   | ¬¬E, LEM | \( \neg\neg\varphi \) ⟹ \( \varphi \); ⟹ \( \varphi \vee \neg\varphi \) | "\( P \) must hold, since …"; "either \( P \) or not" | never: written out |
   | MT, CP | \( \varphi \to \psi \), \( \neg\psi \) ⟹ \( \neg\varphi \); \( \varphi \to \psi \) ⟹ \( \neg\psi \to \neg\varphi \) | "so \( P \) cannot hold"; "we prove the contrapositive" | the announcement never |
   | DS | \( \varphi \vee \psi \), \( \neg\varphi \) ⟹ \( \psi \) | "the first case is impossible, so …" | the name yes; the fact it uses never |
   | ∀I | box (fresh \( a \)) … \( \varphi(a) \) ⟹ \( \forall x\, \varphi(x) \) | "let \( x \in A \)"; "fix \( \varepsilon > 0 \)" | the opening never; "since \( x \) was arbitrary" yes |
   | ∀E | \( \forall x\, \varphi(x) \) ⟹ \( \varphi(t) \) | "in particular, for \( x = \dots \)" | at the obvious term yes; otherwise the term is named |
   | ∃I | \( \varphi(t) \) ⟹ \( \exists x\, \varphi(x) \) | "take \( N \coloneqq \dots \)"; "… will do" | never: the witness and what it depends on |
   | ∃E | \( \exists x\, \varphi(x) \), box (fresh \( a \)) \( \varphi(a) \) … \( \chi \) ⟹ \( \chi \) | "choose \( N \) such that …" | the choice with its fresh name never; the closing yes |
   | =I, =E | ⟹ \( t = t \); \( s = t \), \( \varphi(s) \) ⟹ \( \varphi(t) \) | "… = … = …"; "substituting" | yes, inside chains |

   One sentence under it: "The exact conditions are those of @def-silent-steps in Section 5.3; the card abbreviates them." (A forward pointer inside the chapter, not a reason: nothing in 5.1 or 5.2 argues from the definition.) **Quick check (new):** "Which rule does each phrase carry: (i) 'say \( n = 2k \)', after '\( n \) is even'; (ii) 'in either case'; (iii) 'this contradicts \( x^2 \ge 0 \)'?" Solution: (i) ∃E, opening the box of \( k \) ("\( n \) is even" unwound to \( \exists k\, (n = 2k) \)); (ii) ∨E, closing; (iii) ¬E, with both lines of the clash named.
3. `## Which steps may go unsaid` **(new, ~120 words; the principle moves here from 03:38-40).** "Plain prose leaves steps out. If it left out whatever a writer found obvious, a reader could never tell an omission from a gap, so the book fixes the omissions by one principle: *a step may go unsaid when a reader who knows the rules can restore it uniquely from what is written.* A step that **creates** something (a name, a witness, a case split), **assumes** something, or **cites** something cannot be restored that way, so it is always written." Then 03:40's slogan verbatim, in italics: "*Silent steps are the ones whose result is forced by the lines around them; every choice, assumption and citation is spoken.*" Then: "The last column of the card is this principle applied rule by rule." **Quick check (new):** "In 'Since \( 0 < x < 1 \), in particular \( x > 0 \)', may the words 'in particular \( x > 0 \)' be left out if the next sentence uses \( x > 0 \)? May 'choose \( k \) with \( n = 2k + 1 \)' be left out?" Solution: the first yes: ∧E has two possible results and the next sentence shows which one was used, so it is forced; the second no: ∃E creates a name, and a name cannot be restored.
4. `## The same proof, twice` (01:5-59, reordered: prose first). 01:7 → "Section 2.3 proved @thm-square-even-implies-even ('if \( n^2 \) is even, then \( n \) is even') a second way, in @exm-square-even-via-contrapositive, with the derived rules CP and DS, and wrote it as four sentences. Here are four sentences for it, with the box of the second sentence spelled out:" Then the paragraph 01:35 verbatim. Then a prompt (italic): "*Before reading on: where in the paragraph does a box open, and where does one close?*" Then 01:37 and the table 01:39-49 verbatim (the two-column alignment: words | lines | rule). Then: "The derivation the table refers to is the one of Section 2.3, with the facts (E1)–(E3) of Section 2.1 (every integer is even or odd; no integer is both; the square of an odd integer is odd) as its premises, written here with its atoms in words:" and the derivation 01:9-31 **with the atoms in words**: \( E \) → \( \text{$n$ even} \), \( O \) → \( \text{$n$ odd} \), \( S \) → \( \text{$n^2$ even} \), \( T \) → \( \text{$n^2$ odd} \), every line, rule and number unchanged (line 11 "or commutes" kept: ch02-revision §3 keeps it for this reprint). 01:51 kept, with "(the convention on silent steps of Section 5.3 lets the exchange be silent)" → "(the principle above lets the exchange be silent: the order a schema wants is forced)". Quick check 01:53-59 kept verbatim.
5. `## How to read the dictionary` (01:61-72) **cut to two sentences** (~60 words): "Each group of rows below repeats the card's rows for one connective, with the phrases a reader must recognize, and then works one short proof annotated phrase by phrase. A tag such as [∧E] after a phrase says which rule it carries; any wording that does the same job is correct." Cut: 01:63-68 (the four-entry description and the volume pointers), 01:70 (Lean), 01:72's volume sentence (its content moves to 5.3's box).
6. `## Conjunction`: table 01:76-79 kept. 01:81 **replaced** (~60 words): "In a proof, ∧I is a claim with two parts, proved one after the other and then put together; often the parts are labeled (a) and (b), and the last sentence says nothing more. ∧E is the step from a chain to one of its links: 'since \( x \in (0, 1) \), in particular \( x > 0 \)' takes the left conjunct of \( 0 < x \wedge x < 1 \)." (01:81's least-upper-bound sentences and the parenthesis on another volume's clause (S2) are cut: the example moves to B3.)
7. `exm-rhetoric-conjunction` **(content replaced, ~140 words; S2a item 3):**

   ::: {#exm-rhetoric-conjunction} [Two parts, and one part] "Let \( x \) be a real number with \( 0 < x < 1 \). Prove that \( x^2 < x \) and \( x^2 > 0 \). Tag the steps that carry the logic."

   Solution: "The hypothesis \( 0 < x < 1 \) is the conjunction '\( 0 < x \) and \( x < 1 \)'; so \( x > 0 \) [∧E] and \( x < 1 \) [∧E]. *(a)* Multiplying \( x < 1 \) by the positive number \( x \) gives \( x^2 < x \) [algebra]. *(b)* As \( x > 0 \), \( x^2 = x \cdot x > 0 \) [algebra]. So \( x^2 < x \) and \( x^2 > 0 \) [∧I]." Then: "Both ∧E steps could be silent ('multiplying \( x < 1 \) by \( x > 0 \) gives …'), because the next sentence shows which part of the hypothesis is used. The final ∧I may be silent too, since both parts are displayed: a proof of a two-part claim usually proves (a), proves (b), and stops."
8. `## Implication`: table 01:101-106 kept. 01:108 first sentence kept. Its second sentence (the continuity theorem of a later volume) **replaced**: "→E is every citation of a theorem: 'since \( 42 \) is divisible by \( 2 \) and by \( 3 \), it is divisible by \( 6 \)' applies the theorem used in Section 1.3 to two facts in hand, and the word 'since' introduces those facts." The rest of 01:108 kept. `exm-rhetoric-implication` kept.
9. `## Disjunction and cases`: 01:128-161 kept verbatim (table, 01:137, `exm-rhetoric-cases`, the warning on "clearly").
10. `## Negation and contradiction`: table 01:165-170 and 01:172 kept. 01:174 → its first two sentences, then one sentence: "Write the negated form out; do not leave the reader to push a 'not' through a quantifier in their head." The rest of 01:174 ("The passage uses @prp-bounded-quantifier-negation (a) …" to "… and the proof needs no name.") → fold F5.1-a, with "*Analysis on the Real Line*, Chapter 1's proof that \( \nN \) is not bounded above is the instructive case." → "A proof that \( \nN \) is not bounded above is the instructive case." `exm-rhetoric-negation` kept.
11. `## Proof by contradiction`: **the BHK preview (new, ~80 words), first in the subsection:** "Why tell RAA from ¬I at all? Some mathematicians accept every rule of this book except RAA. For them a proof should hand over what it claims: a proof that something exists should say what exists, and a proof of '\( P \) or \( Q \)' should say which. ¬I keeps that promise; RAA can break it, and Section 5.7 shows a proof that two such numbers exist which never says which numbers they are. For now, learn to see which of the two a proof uses." Then the table 01:194-197 kept. 01:199: first three sentences kept (`prp-arbitrarily-close-equal`); "a split such as 'either the sequence has infinitely many terms in the left half of the interval, or it does not', the step of the bisection proof of the Bolzano–Weierstrass theorem (*Analysis on the Real Line*, Chapter 2 proves the theorem)" → "a split such as 'either the sequence has infinitely many terms in the left half of the interval, or it does not', a step of the bisection proof of the Bolzano–Weierstrass theorem"; "which *Analysis on the Real Line*, Chapter 1 takes as an axiom" → "one of the axioms for the real numbers". The rest kept.
   `exm-rhetoric-contradiction`: statement → "… Prove that \( a \le b \), first by RAA; then rewrite the proof as a case split." (S2a item 4.) Solution: 01:208-210 kept; 01:212 removed from the solution; 01:214 kept; 01:216 **replaced** on the main line by: "The two proofs share their mathematics, the instance \( \varepsilon = (a - b)/2 \), and differ only in how the classical step is written: as RAA, or as a split on trichotomy, which over \( \nR \) is an axiom, so neither is flagged. The fold below writes the same box closed by ¬I and followed by ¬¬E." Fold F5.1-b `title="The same proof by ¬I and ¬¬E"` (a sibling after the solution): 01:212 and 01:216 verbatim.
12. `## The biconditional`: 01:219-242 kept verbatim.
13. `## The three faces of "by contradiction"`: 01:246 → "'Proof by contradiction' is used in practice for three different arguments. Each opens a box and finds \( \bot \) inside it; they differ in what the box assumes and what the proof concludes. Only face (i) is free of a classical step." Its clause on face (ii)'s RAA "unless \( Q \) is itself a negation" → fold F5.1-c. The table gains a column **"A tiny example"**: (i) "\( 7 \) is not even"; (ii) "if \( n^2 \) is even, then \( n \) is even"; (iii) "if \( a \le b + \varepsilon \) for every \( \varepsilon > 0 \), then \( a \le b \)". 01:254 kept. 01:256: "(avoidable when \( Q \) is itself a negation, as Section 2.5 notes after the proof)" cut → fold F5.1-c. 01:258 kept. 01:260: "*Analysis on the Real Line*, Chapter 1 uses them for a face (i) proof" → "a proof that \( \nN \) is not bounded above uses them for a face (i) proof: it supposes \( \nN \) bounded and concludes that it is not". 01:262 kept. **Quick check (new):** "Which face? (i) 'Suppose \( \sqrt 3 = p/q \) with integers \( p \), \( q \). … a contradiction. Hence \( \sqrt 3 \) is irrational.' (ii) 'Suppose \( n^2 \) is odd. Suppose, for a contradiction, that \( n \) is not odd. Then \( n \) is even, say \( n = 2k \), so \( n^2 = 4k^2 = 2(2k^2) \) is even, hence not odd, which contradicts \( n^2 \) being odd. Hence \( n \) is odd.'" (The wording of (ii) matches `exm-costume-contrapositive`: the box assumes \( \neg Q \) itself, and the choice of \( k \) is written.) Solution: (i) face (i): the box assumes the positive statement "\( \sqrt 3 \) is rational" and concludes its negation, by ¬I. (ii) face (ii): the box assumes \( \neg Q \), "\( n \) is not odd", and derives "\( n^2 \) is not odd" from it alone; the hypothesis "\( n^2 \) is odd" enters only at the clash. That is a contrapositive in costume.
14. `## Costumes`: 01:264-304 verbatim (both examples, both tests, the smell). Warning 01:306-308 kept.

**Folds.** F5.1-a `title="For the record: where the classical step sits"`: 01:174 from its third sentence to its end, with the one rewording of item 10. F5.1-b `title="The same proof by ¬I and ¬¬E"`: 01:212 and 01:216 verbatim. F5.1-c `title="When the contrapositive needs no classical step"`: "Face (ii) ends with @prp-contrapositive-converse, which Section 2.5 derives with RAA; that RAA is avoidable when \( Q \) is itself a negation, by the fold 'RAA is never needed to finish a negation' of Section 2.5. So face (ii) uses RAA unless \( Q \) is itself a negation." (~55 words; the content of 01:246's and 01:256's clauses, S2a item 5.)

**Cut outright:** 01:63-72 except the two kept sentences; 01:81's least-upper-bound sentences (moved to B3) and its parenthesis; 01:108's continuity sentence; the volume pointers of 01:3, 01:199 (×2), 01:260.

**Quick checks:** card phrases (new), principle (new), "were" (kept), faces (new): four in ~4,750 words.

**Exercises.**
- **A1** kept; (d)'s solution (01:332): "*Analysis on the Real Line*, Chapter 1's proof that \( \nN \) is not bounded above begins" → "A proof that \( \nN \) is not bounded above may begin".
- **A2: Drill** (new, `exr-connective-rhetoric-a2`). Stem: "Name the rule each phrase carries, and say whether plain prose may leave it out." Answers in one folded solution:
  (a) "Suppose \( n \) is odd." at the start of a proof of "if \( n \) is odd, then \( n^2 \) is odd". — →I, opening; never silent.
  (b) "In either case, \( x^2 \ge 0 \)." — ∨E, closing; may be silent.
  (c) "Since \( x \ne 0 \), the first case is impossible, so \( x = 3 \)", after "\( x = 0 \) or \( x = 3 \)". — DS; its name may go, the fact \( x \ne 0 \) may not.
  (d) "\( x > 2 \), so certainly \( x \ge 2 \)." — ∨I (\( x \ge 2 \) is \( x > 2 \vee x = 2 \)); may be silent.
  (e) "This contradicts \( n^2 \ge 0 \)." — ¬E; never silent: both lines of the clash are named.
  (f) "Conversely, suppose \( x^2 = 4 \) and \( x > 0 \)." — ↔I, opening the second direction; never silent.
  (g) "Suppose, for a contradiction, that \( n \) is not prime", in a proof that ends "Hence \( n \) is prime." — RAA, opening; never silent.
  (h) "Suppose \( 15 \) is a perfect square. … a contradiction. Hence \( 15 \) is not a perfect square." Which face? — (i), refuting: ¬I.
  (i) A proof of "if \( x^2 < 1 \), then \( x > -1 \)" begins "Suppose \( x \le -1 \). Then \( -x \ge 1 \), so \( x^2 = (-x)^2 \ge 1 \)." What should come before it? — the announcement "We prove the contrapositive" (CP; never silent).
  (j) "Let \( n \) be even, say \( n = 2k \). Suppose, for a contradiction, that \( n^2 \) is not even. Then \( n^2 = 4k^2 = 2(2k^2) \) is even, which contradicts \( n^2 \) not being even. Hence \( n^2 \) is even." (The box opens with the negation of the goal, so the item is not an instance of (N11)(a).) In costume? — Yes, a direct proof in costume: the assumption is cited only at the clash; delete the box.
- **B1**, **B2** kept.
- **B3** (new label `exr-connective-rhetoric-b3`), `[B3: Two clauses of a least upper bound]`: the statement of old `exm-rhetoric-conjunction` (01:86) verbatim, then "*Hint:* in the second part, take a number halfway between \( \max\{t, 0\} \) and \( 2 \)." Solution: 01:90-96 verbatim, except in 01:96 "as the warning below requires" → "as the warning on 'clearly' in 'Disjunction and cases' requires" and "as the \( \rulename{\neg E} \) row below requires" → "as the \( \rulename{\neg E} \) row of the dictionary requires" (S2a item 3).
- **C1** frozen, unchanged (its stem's pointer to *Sets, Relations, and Cardinality* stays: fd3 relies on the item as printed).
- **C2** kept; its solution 01:448: "which rests on the trichotomy of the order, an axiom of *Analysis on the Real Line*, Chapter 1; Section 5.7 explains why that axiom is where the book makes its classical commitment" → "which rests on the trichotomy of the order, one of the axioms for the real numbers; Section 5.7 explains why that axiom is where the book makes its classical commitment".

**Sidecars:** `exm-rhetoric-conjunction.py` new (\( 0 < x < 1 \Rightarrow x^2 < x \) and \( x^2 > 0 \), exactly on rationals and on a grid); `exr-connective-rhetoric-b3.py` (the old script, renamed); A2 (i) (\( x \le -1 \Rightarrow x^2 \ge 1 \)) in `exr-connective-rhetoric-a2.py`. Ledger: new lines for the card (each "Silent?" entry read off @def-silent-steps, F1.5 §03, prose pointer), the principle (moved from 03, now its first statement), the 42 sentence (F1.1 §04's theorem, prose pointer), the BHK preview (F1.5 §07, prose pointer), the face examples; the old `exm-rhetoric-conjunction` lines move to `exr-connective-rhetoric-b3`; the two lines about other volumes' statements (01:463, 01:465, 01:468, 01:471) go with the cut sentences or move to the folds.

### 4.2 Section 5.2: The Quantifier Rules in Prose (`02-quantifier-rhetoric.md`, edited)

**Budget:** main line ≤ 3,700 words (now 3,129); no fold. **No Looking-ahead box.**

**New order of material.**
1. 02:3 kept.
2. `## Three sentences, three rules`: 02:7 → "Section 4.8 derived 'if \( a_n \to L \), then \( 2a_n \to 2L \)' in sixteen lines. Written the way a mathematician writes it, the same argument takes three sentences:" Then the quotation 02:9. Then **the derivation reprinted** (new lead, ~40 words): "Here is the derivation of Section 4.8 again, with the same line numbers. To keep its lines short, write \( A(n, \varepsilon) \) for \( \abs{a_n - L} < \varepsilon \) and \( B(n, \varepsilon) \) for \( \abs{2a_n - 2L} < \varepsilon \)." The 16 lines of ch04 08 (the block after ch04 08:262), every rule and citation unchanged, with \( A(\cdot,\cdot) \), \( B(\cdot,\cdot) \) replacing the two inequalities (line 1 \( \forall \varepsilon > 0 \; \exists N \in \nN \; \forall n \in \nN \; (n \ge N \to A(n, \varepsilon)) \); line 10 \( A(n_0, \varepsilon_0/2) \); line 11 \( B(n_0, \varepsilon_0) \), arith 10; and so on). If R4 delivers 4.8 with named matrices of its own, use its names and its line numbers, and renumber the bullets below to match. Then **the brackets** (new table, beside or under the derivation):

   | Sentence | Lines |
   |---|---|
   | "Let \( \varepsilon > 0 \)." | opens the box 2–15; its closing line 16 is not written |
   | "Since \( a_n \to L \) and \( \varepsilon/2 > 0 \), we may choose \( N \) …" | 3 and 4, then opens the box 5–14 |
   | "Then for every \( n \ge N \), \( \abs{2a_n - 2L} = 2\abs{a_n - L} < \varepsilon \)." | 7–13 |
   | (the paragraph ends) | 14, 15, 16 |

   Then 02:11-18 verbatim, with "in the derivation of Section 4.8" (02:13) → "in the derivation above".
3. `## The quantifier rows`: 02:20-31 kept; `exm-rhetoric-universal` verbatim.
4. `## The dependency parenthesis`: 02:53-57 kept. Then **the dependency picture** (new TikZ, two panels side by side, ~50 words of caption). Each panel: three nested rounded rectangles, outermost labelled "let \( x \in A \)", middle "let \( \varepsilon > 0 \)", innermost "choose \( \delta \)"; inside the innermost a small node "the line \( \delta \) comes from". Panel (a), titled "continuity at every point": that node reads "mentions \( x \) and \( \varepsilon \)", with two solid arrows from \( \delta \) to the labels \( x \) and \( \varepsilon \). Panel (b), titled "uniform continuity": the node reads "mentions \( \varepsilon \) only", one solid arrow from \( \delta \) to \( \varepsilon \), and a dashed arrow to \( x \) labelled "may, but does not". Caption: "A chosen constant **may** depend on the names of the boxes it sits in, and **does** depend only on the names in the line it comes from (the solid arrows)." (Labels as `\text{}`; no reference inside the picture; both themes; no colour needed.)
   Then **the numbers** (new, ~120 words): "Numbers show why the arrows matter. Take \( f(x) = x^2 \) and \( \varepsilon = 1 \). At the point \( a \ge 0 \), the largest \( \delta \) with \( \abs{x^2 - a^2} < 1 \) for every \( x \) with \( \abs{x - a} < \delta \) is \( \sqrt{a^2 + 1} - a \): about \( 0.41 \) at \( a = 1 \), and about \( 0.005 \) at \( a = 100 \). No single \( \delta \) serves every point, so \( \delta \) must depend on the point as well as on \( \varepsilon \): panel (a). For \( f(x) = 3x + 1 \), \( \abs{f(x) - f(a)} = 3\abs{x - a} \), so \( \delta = \varepsilon/3 \) works at every point at once: \( \delta \) depends on \( \varepsilon \) only, panel (b)." Then 02:59 kept. **Quick check (new):** "For \( f(x) = x^2 \) and \( \varepsilon = 1 \), does \( \delta = 0.1 \) work at the point \( a = 2 \)? At \( a = 10 \)?" Solution: at \( a = 2 \), yes, since \( 0.1 < \sqrt 5 - 2 \approx 0.236 \); at \( a = 10 \), no: \( x = 10.06 \) has \( \abs{x - 10} = 0.06 < 0.1 \) and \( x^2 - 100 = 1.2036 \ge 1 \).
   `exm-rhetoric-existential`: statement and solution verbatim except two phrases (S2a item 2): 02:68's first sentence → "The sequence starts at \( n = 1 \), so in the definition of Section 4.8 the numbers \( N \) and \( n \) range over the positive integers \( \nZ_{>0} \)."; 02:68's last sentence "(*Analysis on the Real Line*, Chapter 1 proves it from the axioms of \( \nR \).)" → "(It follows from the axioms for the real numbers; here we take it as known.)"; 02:74's tag "[cut: the claim (\( \ast \)) displayed, then used]" → "[it suffices: the claim (\( \ast \)) displayed, then used]"; 02:78's "The second is a cut, in the sense of the row below:" → "The second is an 'it suffices to show', in the sense of the row below:". Everything else verbatim. Quick check 02:83-89 kept.
5. `## Equality and unique existence`: 02:91-125 verbatim.
6. `## Induction, lemmas and symmetry`: 02:129 kept. The table 02:131-135 with its rows **reordered** (cut, induction, symmetry) and the cut row's first cell "it suffices to show; a lemma (a cut, @lem-weakening-cut)". 02:137 is split into three subsections, each with a small picture:
   - `### It suffices to show` (02:137's sentences on the lemma, rewritten plain-first, ~110 words): "'It suffices to show \( \varphi \)' does two things. It shows on the spot that \( \varphi \) gives the goal, and it leaves \( \varphi \) to be proved: the goal is replaced by \( \varphi \). As Section 1.3 observed, to show \( \psi \) it suffices to show \( \varphi \) when \( \varphi \to \psi \) is in hand. A lemma is the same move in the other order: prove \( \varphi \) first, then use it as if it were a premise. (Logicians call both a **cut**; @lem-weakening-cut (b) is the precise statement.) In analysis, 'it suffices to show \( \abs{a_n - L} < \varepsilon \) for \( n \ge N \)' reduces a limit to one estimate; @exm-rhetoric-existential made one with the claim (\( \ast \))." **Picture (new TikZ):** three nodes in a column, "the goal" (top), "the claim \( \varphi \)" (middle), "the hypotheses" (bottom); a solid arrow from \( \varphi \) up to the goal labelled "shown at once"; a dashed arrow from the hypotheses up to \( \varphi \) labelled "proved next". **Quick check (new):** "In @exm-rhetoric-existential, which sentence is the 'it suffices' step, and what does it leave to prove?" Solution: "It suffices to find \( N \in \nZ_{>0} \) with \( 1/N < \varepsilon \), since then …"; it leaves (\( \ast \)), proved in the next paragraph.
   - `### Induction` (02:137's first three sentences verbatim, ~90 words). **Picture (new TikZ):** at the left a single line "\( P(0) \)" labelled "base case"; at the right a box "let \( n \in \nN \)" containing a box "suppose \( P(n) \)" whose last line is "\( P(n + 1) \)", labelled "step"; both feed one arrow labelled "→E on the axiom" into "\( \forall n \in \nN \; P(n) \)". Caption names @ax-induction.
   - `### Without loss of generality` (02:137's last sentence expanded, ~80 words): "Symmetry is a case split ∨E whose second box is the first with two letters exchanged. 'Without loss of generality \( x \le y \)' writes the first box and leaves the second to the reader, who must be able to get it by swapping the letters; that works when the statement and the hypotheses come back unchanged under the swap, up to identities such as \( \abs{b - a} = \abs{a - b} \)." **Picture (new TikZ):** two boxes side by side, "case \( a \le b \): … ⟹ claim" (solid, written) and "case \( b \le a \): the same lines with \( a \), \( b \) swapped ⟹ claim" (dashed, not written), joined by an arrow labelled "swap \( a \leftrightarrow b \)", both above one line "∨E on '\( a \le b \) or \( b \le a \)'". **Quick check (new):** "May a proof that \( x^2 + y^2 \ge 2xy \) for all real \( x \), \( y \) begin 'Without loss of generality \( x \le y \)'?" Solution: yes: swapping \( x \) and \( y \) leaves the statement unchanged and there are no hypotheses; the case split is legitimate, though not needed, since \( x^2 + y^2 - 2xy = (x - y)^2 \ge 0 \).
   Then `exm-rhetoric-induction` verbatim: its (a) is the worked induction and its (b) the worked symmetry (§9 D3). Warning 02:166-168 kept.
7. `## What the sentence does not say {#what-the-sentence-does-not-say}`: 02:170-188 verbatim.

**Cut outright:** 02:7's volume pointer; 02:68's volume sentence (reworded); nothing else.

**Quick checks:** δ at two points (new), hidden ∃N (kept), it-suffices (new), WLOG (new): four in ~3,700 words.

**Exercises.**
- **A1** kept.
- **A2: Drill** (new, `exr-quantifier-rhetoric-a2`):
  (a) "Fix \( \varepsilon > 0 \)." Which rule, and may it be silent? — bounded ∀I, opening; never.
  (b) "Applying the hypothesis with \( \varepsilon/3 \) in place of \( \varepsilon \)" — ∀E at a term that is not the obvious one; the term must be named.
  (c) "Take \( \delta \coloneqq \varepsilon/5 \)." — ∃I's witness, written before the work; never silent; it depends on \( \varepsilon \).
  (d) "By hypothesis there is \( k \) with \( m = 2k + 1 \); choose such a \( k \)." — ∃E, with a fresh name.
  (e) In "Let \( \varepsilon > 0 \). Choose \( N \) such that … . Let \( n \ge N \).", may \( N \) depend on \( n \)? — No: the box of \( n \) opens after \( N \) is chosen.
  (f) In "Let \( x \in A \). Let \( \varepsilon > 0 \). Choose \( \delta > 0 \) such that …", may \( \delta \) depend on \( x \)? — It may, since both boxes are open; whether it does depends on the line it comes from.
  (g) Write "\( x^2 > 0 \) for all \( x \ne 0 \)" with the quantifier in front. — \( \forall x\, (x \ne 0 \to x^2 > 0) \).
  (h) Negate "\( a_n > 0 \) for all large \( n \)" with no ¬ in front of a quantifier. — For every \( N \) there is \( n \ge N \) with \( a_n \le 0 \).
  (i) A proof of "\( \max\{a, b\} \ge a \)" begins "Without loss of generality \( a \le b \)." Legitimate? — No: the swap turns the claim into \( \max\{b, a\} \ge b \), a different claim; each case needs its own line (both are one line long).
  (j) In an induction, which sentence opens the box of the induction hypothesis? — "Suppose \( P(n) \) holds", inside "Let \( n \in \nN \)".
- **B1**, **B2**, **C1**, **C2** kept.

**Sidecars:** `verify/ch05/` script for the dependency numbers (named after the block the drafter ledgers them under, `exm-rhetoric-existential` being the nearest labelled block, or a check script per DRAFTING): \( \sqrt{a^2 + 1} - a \) is the largest δ at \( a \ge 0 \) for \( \varepsilon = 1 \) (sampled: no \( x \) with \( \abs{x - a} < \delta \) has \( \abs{x^2 - a^2} \ge 1 \); at \( \delta + 10^{-6} \) one does), its values at \( a = 1, 2, 10, 100 \), the witness \( x = 10.06 \); the A2 answers need none. Ledger: the reprint (= F1.4 §08's derivation, abbreviations only), the picture's claims (F1.4 §10's reading of dependence), the numbers (sidecar), the WLOG check identity.

### 4.3 Section 5.3: Four Levels of One Proof (`03-levels-of-abbreviation.md`, rewritten)

**Budget:** main line ≤ 4,000 words (now 4,064); folds ≤ 1,300. **Looking ahead** (item 9).

**New order of material.**
1. **Opening frame** (03:3, cut to ~70 words): "Sections 5.1 and 5.2 matched each rule with the phrases that carry it. A proof, though, is read and written whole. This section writes proofs several times, from a full derivation to the plain prose of a textbook, names the four levels this gives, fixes exactly which steps the last level may leave unsaid, and ends with the use that matters most to a reader working alone: when a sentence looks doubtful, rewrite it, and only it, as a skeleton, and look."
2. `## One short proof, four texts` **(new, ~260 words of prose plus two short derivations).** Lead: "Here is one proof, for every integer \( n \): *if \( n \) is odd, then \( n^2 \) is odd*, written four times, starting from the version a textbook prints and zooming in." Then, each under a bold label:
   - **Plain prose.** "Let \( n \) be odd, say \( n = 2k + 1 \). Then \( n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1 \), so \( n^2 \) is odd."
   - **Prose with the rules tagged.** "Let \( n \) be an integer [∀I], and suppose \( n \) is odd [→I]; choose an integer \( k \) with \( n = 2k + 1 \) [∃E, fresh \( k \)]. Then \( n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1 \) [algebra], so \( n^2 \) is odd, with the witness \( 2k^2 + 2k \) [∃I; then ∃E closes, since '\( n^2 \) is odd' does not mention \( k \)]. Since \( n \) was arbitrary, every odd integer has an odd square [→I, ∀I, closing]."
   - **The skeleton** (7 lines; domain ℤ): `\open[n_0] \open \hypo{1}{\exists k\,(n_0 = 2 \cdot k + 1)} \open[k_0] \hypo{2}{n_0 = 2 \cdot k_0 + 1} \have{3}{n_0 \cdot n_0 = 2 \cdot (2 \cdot k_0 \cdot k_0 + 2 \cdot k_0) + 1} \by{arith}{2} \have{4}{\exists j\,(n_0 \cdot n_0 = 2 \cdot j + 1)} \Ei{3} \close \have{5}{\exists j\,(n_0 \cdot n_0 = 2 \cdot j + 1)} \Ee{1,2-4} \close \have{6}{\exists k\,(n_0 = 2 \cdot k + 1) \to \exists j\,(n_0 \cdot n_0 = 2 \cdot j + 1)} \ii{1-5} \close \have{7}{\forall n\,(\exists k\,(n = 2 \cdot k + 1) \to \exists j\,(n \cdot n = 2 \cdot j + 1))} \Ai{1-6}`.
   - **The full derivation** (8 lines): the skeleton with line 3 split into two arith lines, each one fact: 3 \( n_0 \cdot n_0 = 4 \cdot k_0 \cdot k_0 + 4 \cdot k_0 + 1 \) (arith 2: the square of \( 2k_0 + 1 \)); 4 \( n_0 \cdot n_0 = 2 \cdot (2 \cdot k_0 \cdot k_0 + 2 \cdot k_0) + 1 \) (arith 3: a factor 2 taken out); then 5 ∃I 4, 6 ∃E 1, 2–5, 7 →I 1–6, 8 ∀I 1–7.

   Then (~60 words): "Four texts, one proof. Each keeps the box of \( n \), the assumption that \( n \) is odd, the choice of \( k \) and the computation; they differ in how much of the routine work the reader is trusted to restore." Then 03:11's slogan verbatim, in italics. **Quick check (new):** "In the plain prose, which words stand for line 2 of the skeleton, and which skeleton lines have no words at all?" Solution: "say \( n = 2k + 1 \)" is line 2, the opening of the ∃E box with the fresh name \( k \); lines 5, 6 and 7, the closings of the three boxes, have no words; "so \( n^2 \) is odd" is line 4, the ∃I.
3. "The four texts you have just read are the four levels of the next definition." `def-levels-of-proof` **verbatim**, then 03:24 ("In words …") verbatim. 03:7-9 cut to one sentence before the definition: "Sections 2.2 and 4.10 already printed proofs twice, once as a derivation and once as a paragraph." 03:26 and 03:28 → fold F5.3-a. 03:30 kept to "… a proof will not come clear (Section 5.4)." then "Level 2 is for learning, which is why this volume uses it. Level 3 is what mathematicians read and write." (its sentence about other volumes moves to the Looking-ahead box). Warning 03:32-34 kept.
4. `## Which steps may be silent`: 03:38-40 → one sentence: "Section 5.1 stated the principle: a step may go unsaid when its result is forced by the lines around it; every choice, assumption and citation is spoken." Then the **six-row table** (new; "The most common cases"):

   | The step | Silent? | Why |
   |---|---|---|
   | the closing line of →I, ∀I, ∨E or ∃E (not of ¬I, RAA or ↔I): "since \( x \) was arbitrary", "in either case", "hence if \( P \) then \( Q \)" | may be | the box decides it |
   | ∧E; ∨I; repeating a line already shown | may be | the next sentence shows which part or form was used |
   | ∀E at the name in sight; =E inside a chain | may be | the sentence that uses it forces it |
   | opening a box: "let", "suppose", "choose … " with a new name | never | it creates a name or an assumption |
   | a witness, with what it depends on; a case split, with why the cases cover everything | never | it is a choice |
   | a citation of a hypothesis or a result; the clash of ¬E; the conclusion of ¬I or RAA | never | the reader cannot guess what licensed it |

   Then: "The official list, which the rest of the book checks written proofs against, is the next definition. The table gives its most common entries; the definition gives all of them." `def-silent-steps` **verbatim** (§9 D1). Then one sentence (new): "The eighth and ninth items of the first list, for instance, say this: after 'choose \( N \) such that \( \abs{a_n - L} < \varepsilon \) for every \( n \ge N \)', applying that line to a particular \( n \ge N \) needs no comment." 03:78 **cut** (plan). 03:80 kept. 03:82 kept. Warning 03:84-86 kept. **Quick check (new):** "At level 3, may each of these be left out: (i) 'since \( \varepsilon \) was arbitrary'; (ii) 'choose \( \delta > 0 \) (depending on \( \varepsilon \)) such that …'; (iii) 'by the triangle inequality'?" Solution: (i) yes, the closing of ∀I; (ii) no, an ∃E with a fresh name, and the dependence of a witness; (iii) no, a citation.
5. `## The irrationality of the square root of two, four times`: 03:90 kept, plus one sentence at its end: "To keep the lines short, write \( L(r, p, q) \) for \( p = r \cdot q \wedge \neg(E(p) \wedge E(q)) \)." `exm-sqrt2-four-levels`: statement verbatim. Idea: its first paragraph verbatim; the prompt → "*Before reading on: the level-3 proof below has four sentences. Which lines of the level-1 skeleton does its second sentence, 'By (L), write \( r = p/q \) …', stand for?*" Solution, **in reverse order** (S2a item 6): **Level 3** (03:188 verbatim); **Level 2** (03:184 verbatim); **Level 1**: 03:148's lead → "Level 1 keeps every box, every assumption and every closing line, and compresses the work between them into three lines." and the derivation 03:150-178 with \( L(r, p, q) \) in lines 1, 4, 6, 8 (line 1 \( \forall r \in \nQ \; \exists p \in \nZ \; \exists q \in \nZ \; L(r, p, q) \); line 4 \( \exists p \in \nZ \; \exists q \in \nZ \; L(r_0, p, q) \); line 6 \( \exists q \in \nZ \; L(r_0, p_0, q) \); line 8 \( L(r_0, p_0, q_0) \)), every justification unchanged; then "Line 9 takes the first conjunct out of \( L(r_0, p_0, q_0) \), and line 11 the second." Then the answer to the prompt (new): "'By (L), write \( r = p/q \) with integers \( p \), \( q \), not both even' stands for line 4 (∀E of premise 1 at \( r_0 \)) and for the openings of the two ∃E boxes, lines 5–8. It also displays the conjunct \( r = p/q \) on its own, so the ∧E inside line 9 that takes it out has nothing left to say." Optional (R0): the lines that level 1 compresses may be marked. After the solution, fold F5.3-b (level 0). 03:193 kept with "fifteen lines" unchanged. Quick check 03:195-201 **rewritten for level 1** (S2a item 6): "Which lines of the level-1 skeleton in @exm-sqrt2-four-levels have no counterpart in the level-3 text, and which item of @def-silent-steps lets each go?" Solution: "Four lines. Line 4 is ∀E of premise 1 at the obvious term \( r_0 \), the name in sight; 'By (L)' cites premise 1, and the instance is not written. Lines 12 and 13 are the closing lines of the two ∃E boxes. Line 15 is the closing line of ∀I: level 3 never says 'since \( r \) was arbitrary'. Every other line has a phrase: line 1 is 'By (L)'; lines 2, 3 and 5–8 the openings; lines 9 and 10 the computations with their citations of @thm-square-even-implies-even; line 11 the clash, 'both even, a contradiction'; and line 14, 'hence \( r^2 \ne 2 \)', the conclusion of ¬I, which is never silent."
6. `## Uniform continuity, twice` (retitled): 03:205 kept. `exm-uniform-four-levels`: statement → "Write the proof of @exm-uniform-implies-continuous, that a function uniformly continuous on \( A \) is continuous at every point of \( A \), at levels 1 and 3, and say where each level records what \( \delta \) depends on." (S2a item 7.) Solution: "**Level 1.** Every line of the full derivation of @exm-uniform-implies-continuous opens or closes a box, or is cited by a closing line, except one stretch inside the box of \( \delta_0 \), which becomes line 7." and the level-1 derivation 03:242-263 verbatim; **Level 3** (03:271-273 verbatim); then "**Where the dependence of \( \delta \) is recorded.** At level 1, in two places: the box of \( \delta_0 \) lies inside the boxes of \( x_0 \) and \( \varepsilon_0 \), so \( \delta_0 \) **may** depend on both; and the line it comes from, line 4, mentions \( \varepsilon_0 \) and not \( x_0 \), so it **does** depend only on \( \varepsilon_0 \) (Section 4.10). At level 3 it is the parenthesis '(depending on \( \varepsilon \) only)', and nothing else: the parenthesis is the whole of the box structure that survives. Section 5.2's picture draws the same record." After the solution, fold F5.3-c. 03:278 → "From level 1 to level 3, ten lines become three sentences. What the level-3 text keeps is exactly the never-silent part of @def-silent-steps: the openings of the two ∀I boxes ('let \( x \in A \) and \( \varepsilon > 0 \)'), the citation and the choice with its fresh name ('by uniform continuity, choose \( \delta \)'), the dependence of the witness, and the witness itself ('this \( \delta \) works'). The ∀E at \( u = x \), inside line 7, is the obvious instance and becomes 'in particular'. The ∃E closing line 8 and the two ∀I closing lines 9 and 10 are silent." **Quick check (new):** "In the level-3 text, which words record that \( \delta \) was chosen inside the box of \( \varepsilon \) from a line that mentions \( \varepsilon \) only?" Solution: the parenthesis "(depending on \( \varepsilon \) only)".
7. `## Expand to check`: 03:282 kept. **The easy expansion first (new, ~170 words):** "Start with a sentence whose fault is close to the surface:" quotation: "Some element of \( A \) is positive; let \( x \) be one. Since \( x \) was arbitrary, every element of \( A \) is positive." Then: "Expand it. 'Some element of \( A \) is positive' is the line \( \exists x\, (x \in A \wedge x > 0) \); 'let \( x \) be one' opens an ∃E box with a fresh name \( x_0 \); 'since \( x \) was arbitrary' needs a ∀I. At level 1, with that line marked:"
   ```
   % expect-invalid
   1 ∃x (x ∈ A ∧ x > 0)                       premise
   2 | x₀ ∈ A ∧ x₀ > 0                          assumption, flag x₀ (∃E box)
   3 | | x₀ ∈ A                                 assumption (→I box)
   4 | | x₀ > 0                                 ∧E 2
   5 | x₀ ∈ A → x₀ > 0                          →I 3–4
   6 | ∀x (x ∈ A → x > 0)                       ∀I? 2–5
   ```
   (`\hypo{1}{\exists x\,(x \in A \wedge x > 0)} \open[x_0] \hypo{2}{x_0 \in A \wedge x_0 > 0} \open \hypo{3}{x_0 \in A} \have{4}{x_0 > 0} \ae{2} \close \have{5}{x_0 \in A \to x_0 > 0} \ii{3-4} \have{6}{\forall x\,(x \in A \to x > 0)} \by{$\forall$I?}{2-5} \close`, with the expect-invalid marker of `tools/check_fitch.py`. Line 5 is the instance \( \varphi[x_0/x] \) of the formula line 6 wants, so the shape is right and the only fault is the one named next.) "Line 6 is what 'since \( x \) was arbitrary' needs, and no rule gives it. It cannot cite the box 2–5, which is still open (and is the ∃E box of \( x_0 \)); and a new ∀I box flagged \( x_0 \), opened inside it, breaks the side condition of ∀I (@def-rules-universal), because \( x_0 \) appears in the open assumption on line 2. That assumption says that \( x_0 \) is positive, so \( x_0 \) is one particular element, not an arbitrary one. Section 5.6 catalogues the error as (N3). For \( A = \{-1, 1\} \) the premise is true and the conclusion false." Then "Here is a harder one, which sounds like the level-3 proof above run backwards." and 03:284-311 verbatim from its quotation on. 03:313 kept.
8. `## Exercises` follows item 9.
9. **Looking ahead** (`[Looking ahead]`): "From *Analysis on the Real Line*, Chapter 1 on, proofs are written at level 3, and a rule tag appears only where the rule is itself the point; *Sets, Relations, and Cardinality*, Chapters 1–3 may still tag some proofs at level 2." (The content of ix:9's last two sentences and 03:30's; STATUS rows 106–107.)

**Folds.** F5.3-a `title="Levels already on the page, and a skeleton missing a box"`: 03:26 and 03:28, verbatim except two changes in 03:26: "The example below" → "The example of the square root of two below", and "the arithmetic fact of its line 15" → "the arithmetic fact of line 15 of its level-0 derivation (in the fold 'Level 0 of the square root of two')" (on the main line the example's derivation is level 1, whose line 15 is the ∀I line). F5.3-b `title="Level 0 of the square root of two"`: 03:105 ("**Level 0.** Premise 1 is (L) in the form above …"), the derivation 03:107-144, 03:146 and 03:180, verbatim, then 03:190 with its lead "The answer to the prompt: \"By (L), …\" stands for line 5" → "At level 0, \"By (L), …\" stands for line 5" (the prompt now on the main line asks about level 1 and is answered there; the rest of 03:190 verbatim), and the original Quick check 03:195-201 with its solution, verbatim, under the bold lead-in "**A check at level 0.**" (it is not the section's only check). F5.3-c `title="Levels 0 and 2 of the same proof"`: 03:214 ("**Level 0** is the derivation …"), the derivation 03:216-238, 03:240's first sentence, 03:265-269 (level 2 and the renaming sentence), 03:275 and 03:278's first sentence, all verbatim.

**Cut outright:** 03:3's middle sentences; 03:7-9 (one sentence kept); 03:38-40 (moved to 5.1); 03:78; 03:30's volume sentence (to the box).

**Quick checks:** four texts (new), silent or spoken (new), level-1 lines without words (rewritten), the dependence parenthesis (new): four in ~4,000 words, plus the level-0 check in a fold.

**Exercises.**
- **A1:** stem "Parts (a)–(c) are about @exm-uniform-four-levels, parts (d) and (e) about @exm-sqrt2-four-levels." kept. (a) → "Which lines of the level-1 skeleton does the level-3 sentence 'Let \( x \in A \) and \( \varepsilon > 0 \)' stand for? Which open a box, which close one, and which are written at level 3?" Answer: lines 2, 3, 9 and 10; 2 and 3 open the flagged boxes of \( x_0 \) and \( \varepsilon_0 \) with their bounds, 9 and 10 close them by ∀I; the openings are written ("let"), the closings silent at level 3 (@def-silent-steps). (b) → "Where is the dependence of \( \delta \) recorded at levels 1 and 3?" Answer: at level 1, the box of \( \delta_0 \) sits inside those of \( x_0 \) and \( \varepsilon_0 \), and line 4 mentions \( \varepsilon_0 \) only; at level 3, "(depending on \( \varepsilon \) only)". (c) kept. (d) → "At which line of levels 1, 2 and 3 is the 'not both even' clause of (L) used to reach the contradiction?" Answer: 03:340 without its level-0 sentence, level 1 reading "the second conjunct of \( L(r_0, p_0, q_0) \) on line 8, used at line 11". (e) kept.
- **A2: Drill** (new, `exr-levels-of-abbreviation-a2`):
  (a) "Let \( \varepsilon > 0 \) [∀I]. Take \( \delta \coloneqq \varepsilon/2 \) [∃I]. …" Which level? — Level 2.
  (b) At level 3, may "since \( x \) was arbitrary" be left out? — Yes: the closing of ∀I.
  (c) May "choose \( k \) with \( n = 2k \)" be left out? — No: ∃E with a fresh name.
  (d) May "by the triangle inequality" be left out? — No: a citation.
  (e) May "in particular \( x > 0 \)", after "since \( 0 < x < 1 \)", be left out? — Yes: ∧E.
  (f) May the split "\( x \ge 0 \) or \( x < 0 \), and every real \( x \) is one or the other" be left out? — No: the split of ∨E, with the reason it exhausts.
  (g) A skeleton has the line "\( \abs{f(x) - f(y)} < \varepsilon \), arith". Is the proof finished? — No: a skeleton is a plan; every arith line must be expanded (the warning "A skeleton is not a finished proof").
  (h) A text says "Let \( r \) be rational. Then \( p \) is even." Which never-silent step is missing? — The choice of \( p \) (∃E with a fresh name): \( p \) appears from nowhere.
- **B1** kept.
- **B2** (kept, now scaffolded; same claim and ledger key), `[B2: Back from prose to a skeleton, with blanks]`: the claim and level-3 proof of 03:389-391 verbatim, the domain sentence of 03:393, then "Here is its level-1 skeleton with nine blanks, labelled (i)–(ix). *Name the move, then complete it*, and say where the proof uses the fact (E1) of Section 2.1." The skeleton is old B2's 22-line solution derivation (03:399-442) with one blank per slot: (i) the formula of line 4; (ii), (iii), (iv) the justifications of lines 9, 14 and 15; (v) the assumption formula of line 16; (vi), (vii) the justifications of lines 19 and 20; (viii), (ix) those of lines 21 and 22. Each blank is typeset `\underline{\quad(i)\quad}` with its own label, on its own line; the block carries the marker `tools/check_fitch.py` documents for a partial derivation (as Chapter 1's snapshots did), or its expect-invalid marker if the checker requires one. Solution: "*The move* is skeleton first: every box closes by the rule its opening asks for: a 'choose' by ∃E on a line that does not mention the chosen name, the split by ∨E, 'suppose \( n \) is odd' by →I, 'let \( n \)' by ∀I. *Completion:* (i) \( \exists j\, (k_0 = 2 \cdot j) \vee \exists j\, (k_0 = 2 \cdot j + 1) \), by (E1) at \( k_0 \); (ii) ∃E 5, 6–8; (iii) ∃E 10, 11–13; (iv) ∨E 4, 5–9, 10–14; (v) \( k_0 \cdot (k_0 + 1) = 2 \cdot i_0 \), with \( i_0 \) fresh; (vi) ∃E 15, 16–18; (vii) ∃E 1, 2–19; (viii) →I 1–20; (ix) ∀I 1–21. (E1) enters at line 4; in the prose it is 'if \( k = 2j \) … if \( k = 2j + 1 \)', whose reason for covering every case is not written, so the given proof is slightly short of level 3 there." (The last sentence restates 03:444's verdict.)
- **C1** and **C2** (exit check) kept.
- **C3** (new label `exr-levels-of-abbreviation-c3`, new item; S2: old B2 is no longer repeated here, since B2 now prints its skeleton), `[C3: Back from prose to a skeleton]`. Statement, in old B2's format (03:387-393):

  > **Claim.** For every integer \( n \), \( 4 \mid n^2 \) or \( 4 \mid n^2 - 1 \).
  >
  > Let \( n \) be an integer. If \( n \) is even, say \( n = 2k \), then \( n^2 = 4k^2 \), so \( 4 \mid n^2 \). If \( n \) is odd, say \( n = 2k + 1 \), then \( n^2 - 1 = 4k^2 + 4k = 4(k^2 + k) \), so \( 4 \mid n^2 - 1 \).

  "Reconstruct its level-1 skeleton. Work over the domain \( \nZ \), with '\( n \) is even' as \( \exists k\, (n = 2k) \), '\( n \) is odd' as \( \exists k\, (n = 2k + 1) \) and \( 4 \mid m \) as \( \exists t\, (m = 4t) \). Name the rule that closes each box, and name every step of the skeleton that the prose leaves unsaid." Solution: the derivation, written by the drafter in the notation of B2's solution and checked by `tools/check_fitch.py`: the ∀I box of \( n_0 \); in it (E1) at \( n_0 \), \( \exists k\, (n_0 = 2k) \vee \exists k\, (n_0 = 2k + 1) \), cited as in B2's line 4; ∨E on it with two case boxes; in the first, an ∃E box on \( n_0 = 2k_0 \), then \( n_0 \cdot n_0 = 4 \cdot (k_0 \cdot k_0) \) (arith), ∃I, and ∨I (left) to the disjunction \( \exists t\, (n_0 \cdot n_0 = 4t) \vee \exists t\, (n_0 \cdot n_0 - 1 = 4t) \); in the second, an ∃E box on \( n_0 = 2k_1 + 1 \) (a sibling box, which may also reuse \( k_0 \)), then \( n_0 \cdot n_0 - 1 = 4 \cdot (k_1 \cdot k_1 + k_1) \) (arith), ∃I and ∨I (right); each ∃E closes on the disjunction, which does not mention the chosen name; then ∨E, then ∀I (about 15 lines). Then: "The prose leaves unsaid the disjunction (E1) and its reason for covering every case (as in B2, the proof is slightly short of level 3 there), the two ∨I steps (silent: the case's last words, "so \( 4 \mid n^2 \)", show which disjunct was reached), the ∃E closings, the ∨E closing and the ∀I closing (silent closings). It writes every opening ('let', 'if', 'say'), both witnesses (\( k^2 \) and \( k^2 + k \)) and both computations." Hint: "The claim is a disjunction for every \( n \). Which disjunct is reached in each case, and by which rule?" (Not on the core track, which takes the exit check C2.)

**Sidecars:** the four-level opening (\( (2k + 1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1 \)); the easy expansion's \( A = \{-1, 1\} \); `exr-levels-of-abbreviation-b2.py` kept for the scaffolded B2 (same values); new `exr-levels-of-abbreviation-c3.py` (\( (2k)^2 = 4k^2 \), \( (2k + 1)^2 - 1 = 4(k^2 + k) \), and the claim on a range of integers). `tools/check_fitch.py`: the 7- and 8-line derivations, the \( L(r, p, q) \) skeleton (if the checker cannot treat \( L \) as a predicate letter, the drafter reports it and the block gets the marker for derivations checked by hand), the expect-invalid expansion, B2's blanks, C3's solution derivation.

### 4.4 Section 5.4: Reading a Proof: Self-Explanation (`04-reading-proofs.md`, nearly kept)

**Budget:** main line ≤ 2,000 words (now 1,895); fold in the exercises ≤ 550. No Looking-ahead box.

**Changes.**
1. Everything 04:1-115 verbatim except strategy 3 (04:111): its second and third sentences ("A claim inside a proof is a cut (the cut row of Section 5.2's dictionary): it is proved once and then used. Here the claim is proved inside the box on \( x \) and \( y \), so it is simply a line that later lines of the box may cite (@def-derivation); @lem-weakening-cut (b) is the same move for sequents proved outside every box.") → "A claim inside a proof is proved once and then used, as with a lemma in Section 5.2 ('It suffices to show')." (S2: 5.2's subsection calls prove-then-use a lemma, the order opposite to "it suffices".)
2. **Quick check (new)**, after 04:68: "Which of the four questions does the bad explanation of line 3 in @exm-self-explanation fail to answer?" Solution: the fourth, whether the step is legitimate here (does dividing by \( x \) keep the direction of the inequality?), and with it the second, since the warrant \( x > 0 \) is never named.

**Quick checks:** lines 2–4 (kept), the four questions (new): two in ~1,950 words.

**Exercises.**
- **A1**, **B2** kept.
- **B1**: statement kept. **New main solution, at the level of the training passage** (~170 words):
  "*(1)* The goal 'not uniformly continuous' is replaced by the displayed formula: the negation of uniform continuity with no ¬ in front of a quantifier (Section 4.9's recipe, @exm-negating-definitions (c)). The proof now proves that formula. *(2)* \( 1 \) is the witness for 'there is \( \varepsilon > 0 \)', and \( 1 > 0 \). It is written first and justified by the end. *(3)* \( \delta > 0 \) is arbitrary: what follows must work for every \( \delta \). The numbers \( x \) and \( y \) are built from \( \delta \), which is allowed because \( \delta \) is already given; \( 1/\delta \) exists because \( \delta \ne 0 \). *(4)* \( y - x = \delta/2 > 0 \), so \( \abs{x - y} = \delta/2 \), and \( \delta/2 < \delta \) because \( \delta > 0 \). *(5)* Both numbers are positive and \( y > x \), so \( \abs{x^2 - y^2} = y^2 - x^2 = (y - x)(y + x) \); multiplying out gives \( 1 + \delta^2/4 \), at least \( 1 \) because a square is at least \( 0 \). *(6)* \( \delta \) was arbitrary, so the displayed formula holds with \( \varepsilon = 1 \), and uniform continuity fails. \( \delta > 0 \) is used in (3), in (4) twice, and in (5)."
  Then fold (sibling after the solution) `title="The same lines, rule by rule"`: the old solution 04:175-187 verbatim.
- **C1** (label reused, new item), `[C1: A longer proof]`:
  "Here is a proof that a sequence has at most one limit, with its lines numbered.

  > **Claim.** If \( a_n \to L \) and \( a_n \to M \), then \( L = M \).
  >
  > (1) Suppose \( a_n \to L \) and \( a_n \to M \), and suppose, for a contradiction, that \( L \ne M \). (2) Let \( \varepsilon \coloneqq \abs{L - M}/2 \). Then \( \varepsilon > 0 \). (3) Choose \( N_1 \in \nN \) such that \( \abs{a_n - L} < \varepsilon \) for every \( n \ge N_1 \), and \( N_2 \in \nN \) such that \( \abs{a_n - M} < \varepsilon \) for every \( n \ge N_2 \). (4) Let \( n \coloneqq \max\{N_1, N_2\} \). (5) Then \( \abs{L - M} \le \abs{L - a_n} + \abs{a_n - M} < \varepsilon + \varepsilon = \abs{L - M} \). (6) So \( \abs{L - M} < \abs{L - M} \), which is impossible. (7) Hence \( L = M \).

  Self-explain each line, citing labels where a line uses an earlier result. Say where the assumption \( L \ne M \) is used, and which rule closes the box it opens."
  Hint 1: "Line (3) applies the definition of a limit at \( \varepsilon \). What does that need, and which line supplies it?" Hint 2: "Line (5) uses one named result and two lines of (3). Which?"
  Solution: "*(1)* Two openings: the →I box with the two hypotheses, and inside it a box on \( L \ne M \), that is, \( \neg(L = M) \); the goal \( L = M \) is positive, so this is an RAA box. *(2)* A constant, defined from \( L \) and \( M \). It is positive because \( L \ne M \) gives \( \abs{L - M} > 0 \): the one use of the assumption. *(3)* The definition of \( a_n \to L \) applied at \( \varepsilon \) (∀E at a term that is not the obvious one, with its bound \( \varepsilon > 0 \) from (2)), then ∃E with the fresh name \( N_1 \); the same for \( M \), with a second fresh name \( N_2 \) (one name for both would be (N4) of Section 5.6). *(4)* A constant: the larger of two natural numbers, so \( n \ge N_1 \) and \( n \ge N_2 \). *(5)* The triangle inequality (@exm-triangle-inequality-cases), with \( \abs{L - a_n} = \abs{a_n - L} \); then the two bounds of (3) at this \( n \) (∀E at \( n \), →E with \( n \ge N_1 \) and with \( n \ge N_2 \)); then \( \varepsilon + \varepsilon = \abs{L - M} \) by (2). *(6)* The clash: \( \abs{L - M} < \abs{L - M} \) against the fact that no number is less than itself (¬E). The line does not mention \( N_1 \) or \( N_2 \), so the two ∃E boxes close on it. *(7)* RAA: the box assumed \( \neg(L = M) \) and the line written after it is \( L = M \). The closing of the →I box is silent. The assumption is used once, at (2), and it does work there, so the proof is not in costume; Section 5.2 proved the same claim without opening this box (@exm-rhetoric-equality)."
  **Marking scheme.** (10 points) 2: (1) and (7), the two boxes and RAA as the closing rule (not ¬I). 2: (2), \( \varepsilon > 0 \) from \( L \ne M \), named as the use of the assumption. 2: (3), the instance named, two fresh names. 2: (5), the triangle inequality cited and both bounds applied at \( n \ge N_1, N_2 \). 2: (6), the clash named, and the ∃E boxes closing because \( \bot \) does not mention \( N_1 \), \( N_2 \). Fatal errors (0 for the step): calling (7) ¬I; applying the definition at \( \varepsilon \) without its positivity.
- **C2** (new label `exr-reading-proofs-c2`), `[C2: Challenge: A proof about derivations]`: old C1 (04:212-252) verbatim, statement, hints, solution, marking scheme.

**Sidecars:** none new (C1's arithmetic is \( \varepsilon + \varepsilon = 2\varepsilon \)). Ledger: C1's triangle inequality (cited), max of two naturals (school), no number less than itself (school order); the C2 lines move with the item; 04:260's ledger line loses its "lem-weakening-cut (b)" clause.

### 4.5 Section 5.5: Writing a Proof (`05-writing-proofs.md`, edited)

**Budget:** main line ≤ 2,600 words (now 2,413); folds ≤ 650. No Looking-ahead box.

**New order of material.**
1. 05:3 kept.
2. `## A procedure`: 05:7 kept. The algorithm 05:9-19 verbatim except step 1, which gains a second sentence (S2a item 8): "**Write the goal in symbols.** Translate the statement, its hypotheses and its conclusion into a formula, as in Section 4.8, with every quantifier and its bound. Read a letter that is not introduced as universally quantified (Section 4.1). Set up the Givens/Goal table: the hypotheses on the left, the goal on the right." 05:21 kept, its last sentence → "A picture after the next example shows steps 4 and 5." (so that 05:117's sentence alone announces the run of all seven steps) Quick check 05:27-33 kept, here.
3. `## The procedure, run once` (new heading; was "From the goal to prose"): 05:117's first sentence **changed** to "This example runs all seven steps on a statement not seen before." (S2: the example is now the first of the three, not the third), its second sentence kept, its last clause ("*Sets, Relations, and Cardinality*, Chapter 1 develops sets properly") cut. `exm-subset-bounded-above` **moved here** (from 05:119), statement and solution verbatim except: after "*Steps 1 and 2 …*" (05:126) insert the **Givens/Goal table** (S2a item 9):

   | Givens | Goal |
   |---|---|
   | \( A \subseteq B \); \( B \) bounded above | \( A \) bounded above |
   | \( \forall x \in A \; (x \in B) \); \( \exists M \; \forall b \in B \; (b \le M) \) | \( \exists M \; \forall a \in A \; (a \le M) \) |
   | \( \forall x \in A \; (x \in B) \); \( \forall b \in B \; (b \le M_0) \) (∃E, \( M_0 \) fresh) | \( \exists M \; \forall a \in A \; (a \le M) \) |
   | the same | \( \forall a \in A \; (a \le M_0) \) (try the witness \( M_0 \)) |
   | the same, and \( a_0 \in A \) (∀I, \( a_0 \) fresh) | \( a_0 \le M_0 \) |
   | the same, and \( a_0 \in B \) (∀E at \( a_0 \)) | \( a_0 \le M_0 \) ✓ (∀E at \( a_0 \)) |

   with one sentence: "Each row is one move of steps 3 and 4; the table's last row is where the search ends." 05:165 kept after the example.
4. `### Scratch paper and the page` **(new, ~150 words with the picture; replaces 05:23 and 05:25, which go to fold F5.5-a).** "Steps 4 and 5 say that the search runs backwards and the page runs forwards. Here is the example's search beside its page." A two-column figure (a Markdown table is enough):

   | Scratch paper (from the goal, backwards) | The page (from the hypotheses, forwards) |
   |---|---|
   | 1. Goal: an \( M \) with \( a \le M \) for every \( a \in A \). | 1. Suppose \( B \) is bounded above, and choose an upper bound \( M \) of \( B \). |
   | 2. \( B \) bounded above gives some bound \( M \): try it. | 2. Let \( a \in A \). |
   | 3. Need \( a \le M \) for an arbitrary \( a \in A \). | 3. Since \( A \subseteq B \), \( a \in B \). |
   | 4. That needs \( a \in B \). | 4. So \( a \le M \). |
   | 5. \( a \in B \) comes from \( A \subseteq B \). ✓ | 5. Hence \( M \) is an upper bound of \( A \). |

   (Both columns name the bound \( M \), as the page does; the derivation of the example calls it \( M_0 \), and the figure does not need the subscript, S2.) Then: "Read the scratch column from the bottom up and it is the page. The constant \( M \) is found at scratch line 2, after the goal has been read; on the page it is chosen in the first sentence, before anything uses it." Then the two warnings 05:167-173 verbatim. **Quick check (new):** "On the page, which sentence carries the witness of the final ∃I, and why can the choice of \( M \) not come after 'Let \( a \in A \)'?" Solution: "Hence \( M \) is an upper bound of \( A \)" offers \( M \) as the witness (chosen in sentence 1); chosen after "Let \( a \in A \)", \( M \) would sit inside the box of \( a \) and the proof would give only \( \forall a \in A \; \exists M \; (a \le M) \), which says nothing (step 7 of the example). **Quick check (new):** "A writer's scratch paper reads: 'want \( \abs{3x - 6} < \varepsilon \) when \( \abs{x - 2} < \delta \); \( \abs{3x - 6} = 3\abs{x - 2} \); so \( \delta = \varepsilon/3 \).' Write the first two sentences of the page." Solution: "Let \( \varepsilon > 0 \), and let \( \delta \coloneqq \varepsilon/3 \), which is positive and depends on \( \varepsilon \) only. Let \( x \) be a real number with \( \abs{x - 2} < \delta \)."
5. `## Conventions of written mathematics`: 05:35-45 verbatim.
6. `## Matching sentences and rules`: 05:49 **changed** to "The next two examples go in opposite directions." (S2: they are now the second and third). `exm-annotate-abs`: statement verbatim; solution **relabelled structurally** (S2a item 10):

   | Sentence | What it does | Rule |
   |---|---|---|
   | (1) | opens a box with the hypothesis | assumption for →I |
   | (2) | states the disjunction the split needs | a fact about real numbers |
   | (3) | opens the first case | assumption for ∨E |
   | (4) | | algebra |
   | (5) | opens the second case | assumption for ∨E |
   | (6) | | algebra |
   | (7) | uses the assumption of (1), whose box is still open | algebra |
   | (8) | combines the cases, then closes the outer box | ∨E on (2), (3)–(4), (5)–(7); then →I |

   Then 05:73's first sentence kept, and 05:75 → one sentence plus its last: "Measured against @def-silent-steps, nothing that must be written is missing: the split is on the page with a disjunction that covers every real \( x \), each case opens with its assumption, and what is left out may be silent. Labeling also shows where the work is: the case split exists only because \( \abs{\cdot} \) is defined by cases, and the school fact \( -\abs{u} \le u \), used with \( u = x - 1 \), gives \( -1 < x - 1 \) in one step, with no ∨E at all." After the solution, fold F5.5-b. 05:78 and `exm-write-from-derivation` kept; its solution's last sentence (05:112, "premise 1 … is not, and *Sets, Relations, and Cardinality*, Chapter 2 proves it") → "premise 1, that every integer is even or odd, is the fact (E1) that this volume takes as known."

**Folds.** F5.5-a `title="Why the page runs forwards"`: 05:23 and 05:25 verbatim. F5.5-b `title="Every sentence labeled, school facts included"`: the old table 05:62-71 and 05:73's last two sentences and 05:75, verbatim.

**Cut outright:** 05:117's volume clause; 05:112's volume clause (reworded).

**Changed sentences (besides the above):** 05:21's last sentence; 05:117's first sentence; 05:49.

**Quick checks:** step 3/6 (kept), the witness on the page (new), scratch to page (new): three in ~2,600 words.

**Exercises.** A1, B1, B2 (ordering), B3 (faded, last step), C1, C2: all kept verbatim. (A1(a)'s instruction "as in @exm-annotate-abs" now points at a structural table; A1(a)'s solution 05:199-207 labels every sentence by its rule, which the fold's table models. Keep A1 as is: it asks for more detail than the example's main table, and the fold shows that detail.)

**Sidecars:** the scratch example's \( \abs{3x - 6} = 3\abs{x - 2} \) (inline, no script). Ledger: the Givens/Goal table (read off the derivation, F1.2 §06's search, prose pointer); the picture (the same derivation); the two folds' lines move with their text.

### 4.6 Section 5.6: Checking Proofs, and What Is Not Allowed (`06-checking-proofs.md`, edited)

**Budget:** main line ≤ 2,600 words (now 2,240); folds ≤ 120. **Looking ahead** (item 5).

**New order of material.**
1. 06:3 kept. `## Two questions for every line`: 06:7-12 kept. 06:14 → its first three sentences kept, then the **2×2 table** (new, ~110 words):

   | | It follows | It does not follow |
   |---|---|---|
   | **It is true** | the normal case: "\( n = 2k \), so \( n^2 = 2(2k^2) \)", in a proof that \( n^2 \) is even when \( n \) is | the dangerous case: Proof B's last line, "if \( n^2 \) is even, then \( n \) is even", true and not earned |
   | **It is false** | the fault is higher up: from the false line "every real \( x \) has \( x \ge 1 \) or \( x \le 0 \)", ∀E at \( \tfrac12 \) gives "\( \tfrac12 \ge 1 \) or \( \tfrac12 \le 0 \)", which follows and is false | "\( x < 1 \), so \( x^2 < 1 \)": false at \( x = -2 \) |

   Then: "'False' means false in some situation where the hypotheses and the open assumptions are true. When a line follows and is false, some line it rests on, neither a hypothesis nor an open assumption, is false there too, because the rules never lead from true lines to a false one (@thm-soundness); follow it back until the second column fails." 06:14's parenthesis "(Proof C's '\( 1 \) is even' is true given its box's assumption.)" and its "Section 4.11 for predicate logic" → fold F5.6-a. Quick check 06:16-22 kept.
2. `## The catalogue`: 06:26 kept, then the **families table** (new, ~100 words; §9 D2):

   | Family | Entries | Slogan |
   |---|---|---|
   | "For all" errors | (N1), (N2), (N3) | A "for all" needs one argument about a name that is new and arbitrary. |
   | Naming errors | (N4) | A new choice gets a new name. |
   | Implication errors | (N5), (N6) | The box of \( P \to Q \) opens with \( P \); \( Q \) alone gives no \( P \). |
   | Case errors | (N7), (N8) | Every case, from a disjunction that covers everything. |
   | Scope and citation errors | (N9), (N10) | Cite only what is proved, given, or open around you. |
   | Negation errors | (N11) | Negate exactly: an RAA box opens with the negation of the goal; negate the quantifier, not the bound; \( \varphi \wedge \neg\psi \), not an implication. |

   `exm-not-allowed-catalogue`: 06:31 and entries (N1)–(N10) **verbatim**. (N11) → (S2a item 1):

   "11. **A wrong negation**, in three forms. Each breaks \( \rulename{RAA} \), which closes only a box opened with \( \neg\varphi \) (Section 2.5), or the laws of Section 4.9.
       (a) An \( \rulename{RAA} \) box opened with a statement that is not the negation of the goal. Instance: "if \( x^2 > 9 \) and \( x > 0 \), then \( x > 3 \): suppose, for a contradiction, that \( x < 3 \); then \( 0 < x < 3 \) gives \( x^2 < 9 \), against \( x^2 > 9 \); hence \( x > 3 \)" (**true**: the box should open with \( x \le 3 \), and the case \( x = 3 \) is never examined).
       (b) A bound negated instead of a quantifier (@prp-bounded-quantifier-negation). Instance: "\( a_n = 0 \) does not converge to \( 0 \), since some \( \varepsilon \le 0 \) has \( \abs{a_n - 0} \ge \varepsilon \) for all \( n \)" (**false**).
       (c) The negation of \( \varphi \to \psi \) written as an implication, \( \neg\varphi \to \neg\psi \) or \( \varphi \to \neg\psi \), instead of \( \varphi \wedge \neg\psi \) (@prp-negated-implication). Instance: "if \( x > 2 \), then \( x^2 > 4 \)" is "refuted" because "if \( x \le 2 \), then \( x^2 \le 4 \)" holds at \( x = 0 \) (**false**: both are true at \( x = 0 \), so one is not the negation of the other)."

   (The parts are a nested list inside item 11, so the entry keeps its number; "(N11) of @exm-not-allowed-catalogue", as fd2 cites it, still names the whole entry.) 06:48: its first two sentences kept; "From *Sets, Relations, and Cardinality*, Chapter 1 on, a warning about one of these errors cites the entry by number, as in '(N3) of @exm-not-allowed-catalogue'." → the Looking-ahead box; "and two parts of (N11) are warnings of Section 4.9" → "and parts (b) and (c) of (N11) are warnings of Section 4.9". **Quick check (new)**, after the families table: "Which family, and which entry, does this belong to: 'Some integer \( n \) has \( n^2 = n + 6 \); fix such an \( n \). Since \( n \) was arbitrary, every integer \( n \) satisfies \( n^2 = n + 6 \)'?" Solution: a "for all" error, (N3): a name chosen by ∃E is not arbitrary (the premise holds at \( n = 3 \), the conclusion fails at \( n = 0 \)). (S2: not (N3)'s printed instance, nor 5.3's easy expansion.) Quick check 06:50-56 kept. Warning 06:58-60 kept.
3. `## Four proofs, checked`: 06:62-154 verbatim.
4. `## Exercises` after item 5.
5. **Looking ahead** (`[Looking ahead]`): "From *Sets, Relations, and Cardinality*, Chapter 1 on, a warning about one of these errors cites its entry by number, as in '(N3) of the catalogue'."

**Folds.** F5.6-a `title="Two notes on the second column"`: "The same holds for derivations with quantifiers and equality, by the soundness statement for predicate logic in Section 4.11." and 06:14's parenthesis about Proof C, verbatim.

**Quick checks:** two questions (kept), family (new), (N2) (kept): three in ~2,600 words.

**Exercises.**
- **A1** kept; (d)'s answer still reads "(N11)" (it is part (a)); add "(part (a))" after it.
- **A2: Drill** (new, `exr-checking-proofs-a2`). Stem: "Name the entry of @exm-not-allowed-catalogue that each line commits, and say whether its conclusion is true." Answers:
  (a) "We checked that \( n^2 + n \) is even for \( n = 1, \dots, 6 \), so it is even for every \( n \)." — (N1); true (\( n^2 + n = n(n + 1) \)), still not a proof.
  (b) "Let \( \varepsilon > 0 \) and choose \( N \) with \( \abs{a_n - L} < \varepsilon \) for \( n \ge N \); since \( \varepsilon \) was arbitrary, this one \( N \) works for every \( \varepsilon \)." — (N2); in general false.
  (c) "\( x \) and \( y \) are odd, so \( x = 2k + 1 \) and \( y = 2k + 1 \)." — (N4); false (\( x = 1 \), \( y = 3 \)).
  (d) "If \( n \) is divisible by \( 4 \), then \( n \) is even; \( n \) is not divisible by \( 4 \), so \( n \) is not even." — (N6), denying the antecedent; false (\( n = 2 \)).
  (e) "\( n^3 - n \) is even for every integer \( n \): if \( n \) is even, say \( n = 2k \), then \( n^3 - n = 2(4k^3 - k) \); so \( n^3 - n \) is even." — (N7), a missing case: the odd case is never written; the conclusion is true (\( n^3 - n = (n - 1)n(n + 1) \), and of \( n - 1 \), \( n \) one is even), still not a proof.
  (f) "Suppose \( x > 0 \); then \( x^2 > 0 \). Hence if \( x > 0 \), then \( x^2 > 0 \). Since \( x^2 > 0 \), …" — (N10); "\( x^2 > 0 \)" is false at \( x = 0 \).
  (g) "The negation of 'for every \( \varepsilon > 0 \), \( \abs{x} < \varepsilon \)' is 'for some \( \varepsilon \le 0 \), \( \abs{x} \ge \varepsilon \)'." — (N11), part (b); false: the stated "negation" holds for every \( x \) (take \( \varepsilon = -1 \)), also at \( x = 0 \), where the original holds too, so it is not the negation; the negation is "for some \( \varepsilon > 0 \), \( \abs{x} \ge \varepsilon \)".
  (h) "To prove 'if \( n^2 \) is odd, then \( n \) is odd': suppose \( n \) is odd; then \( n^2 \) is odd." — (N5); the claim is true, the proof proves the converse.
- **B1**, **B2**, **C1** (faded), **C2**, **C3** (exit check) kept.

**Sidecars:** `exm-not-allowed-catalogue.py` extended: (N11)(a)'s instance (\( 0 < x < 3 \Rightarrow x^2 < 9 \); \( x^2 > 9 \wedge x > 0 \Rightarrow x > 3 \); \( x = 3 \) has \( x^2 = 9 \)); the 2×2 table's \( x = -2 \), \( \tfrac12 \); A2 (a) (\( n(n + 1) \) even), (c), (d), (e) (\( n^3 - n \) even; \( (2k)^3 - 2k = 2(4k^3 - k) \)), (f); the family Quick check (\( n^2 = n + 6 \) at \( n = 3 \), not at \( n = 0 \)). Ledger: the families table (a regrouping, read off the entries); (N11)(a)'s instance (school algebra; sidecar); 06:393's soundness line now also covers the table's sentence.

### 4.7 Section 5.7: The Dispute over Excluded Middle (`07-excluded-middle.md`, edited)

**Budget:** main line ≤ 3,800 words (now 3,781); folds ≤ 200. **Looking ahead** (item 9). Every result stays `.optional`.

**New order of material.**
1. **Opening** (07:3 rewritten, ~90 words): "Here is a proof that two numbers with a certain property exist which, when it is finished, still does not tell you what the numbers are. It is correct by the rules of this book. Some mathematicians, called **intuitionists**, reject it, for a century now and for reasons that are mathematical rather than merely fussy. This section shows the proof, says what those mathematicians ask of a proof, finds the one rule that fails to provide it, and asks what can be proved without that rule and what analysis would lose." (07:3's sentences on RAA and `thm-raa-independent` move to item 4.)
2. `## Irrational powers, with and without a witness` (**moved up**, 07:119-181): 07:121, `thm-irrational-power-rational` with its Try it first, Idea and proof, all verbatim. 07:149: its first four sentences kept, except that "Every other step is intuitionistic." → "Every other step uses only rules other than RAA." (S2: "intuitionistic" is defined only at 07:9, now in the third subsection); "Under the BHK reading a proof of an existence claim must name the object, so this proof is not one." → "The next subsection says why some mathematicians do not accept such a proof."; its last sentence kept. Remark 07:151-153 kept. 07:155, `prp-log2-9-irrational` with Idea and proof, verbatim. 07:181: "and this one provides what the BHK reading asks for" → "and this one names its witness"; its last parenthesis → "(The exponent laws for real exponents are school facts here.)" **Quick check (new):** "Does the proof of @prp-log2-9-irrational use a classical rule? Does it name its witness?" Solution: no classical rule: its box assumes \( \log_2 9 = p/q \) and concludes the negation, by ¬I; and yes, the witness \( (\sqrt 2, \log_2 9) \) is written down.
3. `## What a proof provides {#what-a-proof-provides}` (07:87-117, moved second): 07:89-101 verbatim. 07:103: "Each intuitionistic rule builds exactly what its clause asks for." → "Each rule other than RAA builds exactly what its clause asks for." 07:105 kept, with one sentence appended: "The proof of @thm-irrational-power-rational is of this kind: it splits on '\( s \) is rational or not' by LEM, and so never says which pair works." 07:107 ("**The proposition under BHK.**") **moves** to item 5. 07:109: "Classical mathematics accepts the step, and *Analysis on the Real Line*, Chapter 1 uses it at the end of its proof of the Archimedean property." → "Classical mathematics accepts the step." Quick check 07:111-117 kept.
4. `## One extra rule {#one-extra-rule}` (07:5-18, moved third): first, 07:3's first two sentences (RAA stands apart; @thm-classical-rules-interderivable; @thm-raa-independent), lightly joined: "Chapter 2 found that one rule stands apart …" Then 07:7, 07:9 verbatim. 07:11: "(the remark after @thm-classical-rules-interderivable)" → "(the remark in the second-reading fold after @thm-classical-rules-interderivable)". Table 07:13-16 kept. 07:18: its last sentence "the Quick check asks for them" → "Exercise B4 asks for them." The Quick check 07:20-28 **moves** to B4 (plan: an optional exercise). **Quick check (new):** "Is the derivation of @prp-double-negation (a), \( P \vdash \neg\neg P \), intuitionistic? Is that of (b)?" Solution: (a) yes: a ¬I box on \( \neg P \); (b) no: \( \neg\neg P \vdash P \) is derived with RAA.
5. `## Excluded middle cannot be refuted` (07:30-85): 07:32, the proposition, Try it first, Idea, proof, 07:73 verbatim. 07:75 (non-example) → fold F5.7-a. 07:77 **reordered, plain sentence first** (S2a item 11): "What the proposition says is this: **nobody can refute excluded middle**. A refutation of \( P \vee \neg P \), put beside this derivation, would prove \( \bot \) from no premises, and no derivation does that. (That last fact is soundness: @thm-soundness, or the soundness statement for predicate logic in Section 4.11 when \( P \) or the derivation involves quantifiers or equality, since no valuation, and no structure and assignment, makes \( \bot \) true.) The intuitionist does not claim that excluded middle fails. …" (07:77's last two sentences verbatim). Then 07:107 ("**The proposition under BHK.**") moved here, verbatim. Remark 07:79-81 and warning 07:83-85 kept. **Quick check (new):** "Does @prp-not-not-excluded-middle show that \( P \vee \neg P \) is derivable without RAA?" Solution: no: it derives \( \neg\neg(P \vee \neg P) \); writing \( P \vee \neg P \) after the same box needs RAA, and Chapter 3's optional @thm-raa-independent shows that no derivation without RAA reaches it.
6. `## A short history`: 07:183-197 verbatim. Then fold F5.7-b.
7. `## What analysis would lose`: 07:201 → "What does analysis look like without the rule? Here are four previews, stated informally and without proof. Classical analysis takes the first as an axiom and proves the other three; each is a place where classical reasoning, by the rule or by an axiom, does work that a constructive proof cannot." Bullets: 07:203 "*Analysis on the Real Line*, Chapter 1 takes as an axiom" → "Classical analysis takes as an axiom"; 07:204 "which *Analysis on the Real Line*, Chapter 2 proves from the axiom" → "which classical analysis proves from that axiom"; 07:205 "Classically, *Analysis on the Real Line*, Chapter 6 proves" → "Classically, one proves"; 07:206 "(*Analysis on the Real Line*, Chapter 2 proves it by another route)" cut. Everything else verbatim.
8. `## Proofs as programs`: 07:208-225 verbatim.
9. `## The book's position`: 07:229 → "The main line of this book stays classical. The decision is made once, in the axioms for the real numbers, which include trichotomy: for real numbers \( a \) and \( b \), exactly one of \( a < b \), \( a = b \), \( b < a \) holds. …" (rest verbatim). 07:231 verbatim. Then **Looking ahead** (`[Looking ahead]`): "*Analysis on the Real Line* takes trichotomy as one of its axioms in Chapter 1, and flags in one clause each genuinely non-constructive step it makes." (STATUS rows 101–103. S2: "pointing back to this section" is dropped, as §8 item 19 directs: the one drafted AN1 chapter flags its classical step, at the end of the Archimedean proof, with a pointer to *Logic and Proof*, Chapter 4, nothing in an1 cites Section 5.7, and STATUS row 99 records the point-back only as asked of AN1.1.)

**Folds.** F5.7-a `title="Non-example by minimal change"`: 07:75 verbatim. F5.7-b `title="Another dispute: the conditional"` (new, ~80 words; instructor note; §9 D9): "Excluded middle is not the only rule that has been questioned. Chapter 1 read \( P \to Q \) as a promise that is broken only when \( P \) holds and \( Q \) fails, so a true \( Q \) makes \( P \to Q \) true whatever \( P \) says, and \( \vdash P \to (Q \to P) \). Some logicians find that too generous: an 'if' should connect its two parts. Logics built on that view, called **relevance logics**, reject \( P \to (Q \to P) \). This book keeps Chapter 1's reading, which is the one mathematics uses."

**Cut outright:** the volume pointers of 07:109, 07:181, 07:201, 07:203-206, 07:229 (reworded as above); 07:149's BHK sentence (moved into item 3).

**Quick checks:** \( \log_2 9 \) (new), BHK of \( \neg(P \wedge \neg P) \) (kept), double negation (new), "cannot be refuted" (new): four in ~3,800 words.

**Exercises.**
- **A1** kept (its stem names the proposition and the theorem, both still in the section).
- **B1**, **B2**, **B3** kept.
- **B4** (new, `exr-excluded-middle-b4`), `[B4: Census of the classical results]`: the Quick check 07:20-22 as the statement, its solution 07:24-28 verbatim as the solution. (A fourth B is off the core track, which takes one B per section: this is the plan's "optional exercise".)
- **C1**, **C2**, **R1**–**R4** kept. (R3's solution "the remark of this section" still finds the Glivenko remark on the main line.)

**Sidecars:** none new. Ledger: the opening's meta-claim ("correct by the rules of this book"); F5.7-b's claims (relevance logic rejects \( P \to (Q \to P) \): stated without proof, nothing depends on it); `excluded-middle-check-1` moves to `exr-excluded-middle-b4`.

---

## 5. Budgets and the Time line

| Section | Main line now (before Exercises) | Main-line budget | Folds |
|---|---|---|---|
| index | 1,001 | ≤ 1,100 | ≤ 300 |
| 5.1 | 4,400 | ≤ 4,750 | ≤ 450 |
| 5.2 | 3,129 | ≤ 3,700 | — |
| 5.3 | 4,064 | ≤ 4,000 | ≤ 1,300 |
| 5.4 | 1,895 | ≤ 2,000 | ≤ 550 (in the exercises) |
| 5.5 | 2,413 | ≤ 2,600 | ≤ 650 |
| 5.6 | 2,240 | ≤ 2,600 | ≤ 120 |
| 5.7 | 3,781 | ≤ 3,800 | ≤ 200 |
| total | 22,923 | ≤ 24,550 | ≤ 3,570 |

The main line grows by about 1,600 words (5.1's budget was raised at S2, §4.1): the chapter was already under STYLE's 5,000 per section, and the new text is the card, the pictures, the tables and the Quick checks the plan asks for, while about 2,300 words of edge cases, meta-remarks and bookkeeping move to folds or are cut. Every section stays under 5,000 main-line words; the whole-file advisory count of `check_structure.py` (exercises included) will exceed 5,000 in 5.1, 5.3 and 5.7, which is advisory.

**Exercises after the revision:** 7 A1; 4 A2 drill banks with 36 parts (5.1: 10, 5.2: 10, 5.3: 8, 5.6: 8), which count as 9 exercises at one per four parts (STYLE §12.8); 18 B (new: 5.1 B3, 5.7 B4; 5.3 B2 now scaffolded); 16 C (new content: 5.4 C1, 5.3 C3; moved: 5.4 C2, a Challenge); 4 R. Exit checks: 5.3 C2, 5.6 C3. Faded triple unchanged: `exm-sqrt2-four-levels` (full), 5.5 B3 (last step blank), 5.6 C1 (last half blank). Proof ordering: 5.5 B2. Try it first: the two of 5.7.

**Time (B1 formula: 15 min per 400 main-line words; 20–45 min per exercise; a drill bank counts as one exercise per four parts).**
- **Core track** = every main line, all of A, one non-Challenge B and one non-Challenge C per section (the exit check where there is one).
  - Reading: about 24,550 words ≈ 15.3 h.
  - Exercises: 7 A1 × 25 min; 9 drill exercises × 30 min; 7 B × 30 min; 7 C × 40 min. That is ≈ 15.6 h.
  - Total ≈ 30.9 h, so "**About 31 hours on the core track** (all of A, one B and one C per section, the exit checks)". At the 20-minute floor for drills it would be about 29.4 h, so 31 is not shaded down.
- **Full track** = main lines and folds, every exercise.
  - Reading: about 28,120 words ≈ 17.6 h.
  - Exercises: 7 A1 × 25; 9 × 30; 18 B × 30; 16 C × 40; 4 R × 40. That is ≈ 29.75 h.
  - Total ≈ 47.3 h, so "**about 47 hours for everything**".
- The plan's target of 28 core hours is not reached. The drafter of the index recomputes from the delivered text by the same rule and does not shade the number down (STYLE §11.9); §4.0 fixes no figure in advance.

---

## 6. Edits needed outside Chapter 5

Section numbers, labels and entry numbers do not change, so no sweep is needed. Every hand-written mention found by the grep of 2026-10-12 was read against the new text:

| Where | Now says | Should read |
|---|---|---|
| fd2 ch02 06:425 | "negating the bound instead is entry (N11) of @fd1:exm-not-allowed-catalogue" | unchanged ((N11) keeps its number; the case is its part (b)); optional sharpening "(N11) (b)" |
| fd2, fd3, fd4: 58 citations of (N1), (N2), (N3), (N4), (N5), (N7), (N9) of the catalogue | the entries and their numbers | unchanged (entries verbatim) |
| fd2 ch01 01:130, 01:161, 03:200, 03:446, 04:324, 04:400, 04:627, 02:486, 02:495, 06:334, 06:536, 06:556, 06:591 | "*Logic and Proof*, Chapter 5('s catalogue)", "Section 5.6", entry (N4), (N7) | unchanged |
| fd2 ch01 01:203, 04:475; ch01 index:7 | the silent-step convention allows ∀E at the obvious term and the closings; never the opening "let" and the citations | unchanged (`def-silent-steps` verbatim) |
| fd2 ch01 04:443, 06:644; ch03 07-gate-0:9, :364 | level 0 / level 3 of Section 5.3 (`def-levels-of-proof`) | unchanged (verbatim) |
| fd2 ch03 07-gate-0:363 | Section 5.2 (`exm-rhetoric-universal`) | unchanged (verbatim) |
| fd2 ch02 index:7, 02:3 | how an induction is written in prose (`exm-rhetoric-induction`) | unchanged (verbatim; still in 5.2) |
| fd2 ch02 02:192 | "the prime-factor fact that *Logic and Proof*, Chapter 5 used" | unchanged (5.1 C1, frozen) |
| fd2 ch02 01:174; ch03 05:166, 04:204, 04:208 | Section 5.7 on non-constructive proofs; `thm-irrational-power-rational` names no witness, `prp-log2-9-irrational` does | unchanged |
| fd3 ch03 index:9, 03:416 | Section 5.1's C1 (`exr-connective-rhetoric-c1`), its part (c) | unchanged (frozen) |
| fd3 ch01, ch02, ch03, ch05 index:7/9 | Chapter 5's catalogue | unchanged |
| fd1 ch04 04:369 | "The first of them opens Chapter 5's catalogue" | unchanged ((N1) stays first) |
| fd1 ch04 01:246 | "Chapter 5 names this convention and lists the others" | unchanged (5.2, "What the sentence does not say") |
| fd1 ch04 09:290, 09:695 | "Chapter 5 catalogues this slip among the wrong negations" | unchanged ((N11) (b) and (c)) |
| fd1 ch04 07:419, 10:83 | "Chapter 5 turns the middle column into a full dictionary"; "Chapter 5 studies this passage … at several levels" | unchanged (R4 decides whether these pointers survive its budget) |
| fd1 ch02 02:76, 05:600, 05:627, 05:636; ch03 05:356 | Chapter 5 on \( \neg\varphi \approx \varphi \to \bot \), on those who declined RAA, on costumes, on the dictionary | unchanged where ch02-/ch03-revision keep them (all remaining ones stay true) |
| ch03-revision §6, row "fd1 ch05 04:215" | "Self-explain the proof of @lem-atom-splitting … its five numbered steps" is a C item of 5.4 | the item is now 5.4 C2 (a Challenge), verbatim; ch03's reason to keep the proof on its main line still holds |

**Other files (coordinator):**
- `authoring/STATUS.md` promise rows: 67 and 68 (paid by F1.5) add "the rule card at the top of §01" beside the dictionary tables; 74 unchanged (the subsection ids are kept); 98 unchanged (the facts are still used; the ledger lines keep their F2.2 sources); 99: the clause (S2) of `def-supremum` leaves §01 (01:81 cut; the lub proof is now B3, which quotes no clause of another volume); `thm-naturals-unbounded` stays as a sample sentence without a volume name (F5.1-a, 01:260, A1(d)): the row's pointer is gone; 100: the §02 pointer is reworded as a non-promise (02:68); 101: the §01 and §07 Bolzano–Weierstrass sentences name no volume; 102 (sequential criterion, §01) **retired** (the sample sentence is replaced by the theorem of Section 1.3); 103, 104: the §07 pointers are reworded, the facts stay; 105: "sets developed properly" (§05) retired, "a warning cites the entry by number" now §06's Looking-ahead box; 106 and 107: source "§03 Looking ahead" (no longer the index); a new row for §07's Looking-ahead box (AN1 takes trichotomy as an axiom and flags each non-constructive step; no point-back is promised). The F1.5 row of the chapter table records the R5 revision when it lands.
- `fd1/authoring/ledger/ch05.yaml` and `fd1/verify/ch05/`: §3.3.
- R4 (Chapter 4's revision, not frozen when this file was written): 5.2 reprints the derivation of ch04 08 with its line numbers, and 5.3's folds copy ch04 10's derivation "with the same line numbers". If R4 changes either derivation, the drafter of whichever chapter lands second updates 5.2's reprint and bracket table, and F5.3-c, to the delivered text (S8 seam).
- NOTATION.md: no change (the abbreviations \( A(n, \varepsilon) \), \( B(n, \varepsilon) \), \( L(r, p, q) \) are local to one display each).

---

## 7. What stays exactly as it is

- The slogan "the words are the boxes, spoken" (ix:7) and the six named moves (ix:27-32).
- The costumes (01:264-304), their tests and their smell; 5.1 B1, B2 and C1 (frozen).
- Every dictionary table (01:76-197, 01:221-224, 02:22-27, 02:93-96, 02:131-135 with its rows reordered).
- `exm-rhetoric-implication`, `-cases`, `-negation`, `-biconditional`, `-universal`, `-equality`, `-induction`; `exm-costume-direct`, `exm-costume-contrapositive`.
- The quantifier-order warnings and "What the sentence does not say" (02:166-188); 5.2 B1.
- `def-levels-of-proof` and `def-silent-steps`, verbatim; the warning "A skeleton is not a finished proof"; the warning "Level 3 is not level 0 with steps missing at random"; the continuity-to-uniform-continuity expansion (03:284-313).
- All of 5.4's main line except one sentence of strategy 3: the training passage, the broken claim at \( x \ne 0 \), the four questions, the five strategies.
- The seven-step procedure (one sentence added to step 1), the two warnings of 5.5, and its exercises (B2 ordering, B3 faded).
- The two-column check, the catalogue's entries (N1)–(N10) and every instance of (N11), Proofs A–D, and 5.6's exercises (C1 faded, C2 find-the-error with a true conclusion, C3 exit check).
- 5.7's results and proofs (all `.optional`), the BHK clauses, the history, "What analysis would lose" (with its pointers reworded), "Proofs as programs", the R group.
- Every statement of a labelled result, and every proof of a cited result, except the changes listed in §8 items 1–11.

---

## 8. S2a: every new or changed claim that needs blueprint verification

**Changed wording or position of cited or kept results:**
1. `exm-not-allowed-catalogue`: (N11) split into (a)–(c) inside entry 11, with the new instance for (a) ("if \( x^2 > 9 \) and \( x > 0 \), then \( x > 3 \)", box on \( x < 3 \), marked **true**; the box should open with \( x \le 3 \); the case \( x = 3 \) is never examined). Is the instance an instance of (a) and of nothing else? Is "true" right (the claim holds: \( x = 3 \) has \( x^2 = 9 \))? Do fd2 06:425 and fd1 ch04 09:290, 09:695 still name the right error? Is 06:48's "parts (b) and (c) of (N11) are warnings of Section 4.9" true? Does the families table assign each entry to one family correctly?
2. `exm-rhetoric-existential`: the compressed ℤ_{>0} sentence, the school fact "taken as known", "it suffices" for "cut" (02:74, 02:78). Equivalent to the old solution? Does 02:137's (now the "It suffices" subsection's) reference to "the claim (\( \ast \))" still hold?
3. `exm-rhetoric-conjunction`, new content: \( 0 < x < 1 \Rightarrow x^2 < x \) and \( x^2 > 0 \); the two silence claims. `exr-connective-rhetoric-b3`: old content verbatim with the two pointer rewordings; is the hint correct (halfway between \( \max\{t, 0\} \) and \( 2 \) is the \( a \) of the solution)?
4. `exm-rhetoric-contradiction`: statement without the ¬I/¬¬E rewrite; the new main-line closing paragraph; F5.1-b carries 01:212 and 01:216 verbatim. Do 01:262 and 01:304 still point at what they claim?
5. F5.1-c's sentence (face (ii) uses RAA unless \( Q \) is a negation), against ch02-revision's fold F2.5-c.
6. `exm-sqrt2-four-levels`: reverse order; \( L(r, p, q) \) in level 1 (lines 1, 4, 6, 8); the level-1 prompt and its answer (lines 4 and 5–8; the ∧E inside line 9); the rewritten Quick check (lines 4, 12, 13, 15 without words, and the phrase of every other line); F5.3-b verbatim except 03:190's lead ("At level 0, …"), and F5.3-a's changed line reference in 03:26. Is the main line still a complete "full" member of the faded triple with the fold closed (levels 3, 2, 1 shown and matched)?
7. `exm-uniform-four-levels`: statement "levels 1 and 3"; the reworded dependence paragraph and 03:278 (level-1 line numbers 7, 8, 9, 10); F5.3-c verbatim. A1 (a), (b), (d) as reworded (level-1 lines 2, 3, 9, 10; line 8 and line 11).
8. 5.5's algorithm, step 1's added sentence (Givens/Goal), against STYLE §12.5.
9. `exm-subset-bounded-above`: the Givens/Goal table (each row one move; the ∀E rows at \( a_0 \)); the moved position (does anything in it rely on 05:23-25, now folded, or on `exm-annotate-abs`, now after it?).
10. `exm-annotate-abs`: the structural table and the one-sentence audit; F5.5-b verbatim. Is "nothing that must be written is missing" still justified on the main line?
11. 5.7 item 5: the plain-sentence version of 07:77 (a refutation beside the derivation proves \( \bot \) from no premises) and the parenthesis that carries soundness; 07:107 moved after the proposition; 07:103 "each rule other than RAA" (is every rule other than RAA, including ⊥E and the quantifier and equality rules, fairly described as building what its clause asks for, as the old "intuitionistic rule" was?).

**New claims and examples in the main text:**
12. Index: the 6-line derivation (rules, citations, the side condition at line 5); the alignment table; Proof B quoted from 06:92 with the claim "every sentence true; the lines prove the converse".
13. 5.1 rule card: every "Silent?" entry agrees with @def-silent-steps (in particular →E, ∀E, ∃E, ∧I, MT/CP, DS) and every shape with the schemas of Chapters 1, 2, 4; the principle (moved from 03:38-40); the two Quick checks (phrases; silence); the 42 sentence (Section 1.3's theorem as delivered, ch01-revision §4.3); the BHK preview ("RAA can break it"; "Section 5.7 shows a proof that two such numbers exist which never says which numbers they are": 5.7's theorem names two candidate pairs without saying which works); the faces table's tiny examples; the faces Quick check (√3 by ¬I; the costume of face (ii), with its box on "\( n \) is not odd" and the choice of \( k \) written).
14. 5.2: the reprint equals ch04 08's derivation (abbreviations only); the bracket table's line ranges; the dependency picture's claims; \( \sqrt{a^2 + 1} - a \) as the largest δ at \( a \ge 0 \) for \( \varepsilon = 1 \), its values \( \approx 0.41 \) (\( a = 1 \)), \( \approx 0.005 \) (\( a = 100 \)), \( \approx 0.236 \) (\( a = 2 \)), \( \approx 0.0499 \) (\( a = 10 \)), and \( x = 10.06 \); \( \delta = \varepsilon/3 \) for \( 3x + 1 \); the three subsection texts and pictures; the WLOG Quick check (\( x^2 + y^2 \ge 2xy \) symmetric, \( (x - y)^2 \ge 0 \)).
15. 5.3: the four texts of "if \( n \) is odd, then \( n^2 \) is odd" (levels 0 and 1 as derivations, side conditions at the ∃E and ∀I lines; level 2's tags; level 3) and their Quick check; the six-row table against @def-silent-steps (no row may say more than the definition; row 1 names the closings of →I, ∀I, ∨E and ∃E only); the "eighth and ninth items" sentence (∀E at the obvious term, then →E on a line of the proof: is the paraphrase exact?); the two new Quick checks; the easy expansion (expect-invalid at line 6 for exactly the stated reasons: the box 2–5 still open, and a new ∀I box violating the side condition; line 5 has the shape \( \varphi[x_0/x] \); \( A = \{-1, 1\} \)); the Looking-ahead wording against STATUS rows 106–107.
16. 5.4: strategy 3's shortened sentence ("as with a lemma"); the four-questions Quick check.
17. 5.5: the scratch/page picture (the page column is the level-3 text of the example; the scratch column is the search of step 4; one name \( M \) in both); the two Quick checks; the reworded 05:21, 05:117 and 05:49 against the new order of the three examples.
18. 5.6: the 2×2 table (each example in its cell; "follows and false" via ∀E from a false line; "false at \( x = -2 \)"); the main-line soundness sentence and fold F5.6-a; the families table and its slogans (N11's covers parts (a)–(c)); the family Quick check (an unprinted (N3) instance); the Looking-ahead wording.
19. 5.7: the new opening ("called intuitionists"); 07:149's "uses only rules other than RAA"; the moved BHK sentence on `thm-irrational-power-rational`; the three new Quick checks; the reworded "What analysis would lose" (no claim that a particular volume proves something); fold F5.7-b (relevance logics reject \( P \to (Q \to P) \); \( \vdash P \to (Q \to P) \) in this book's rules, as Chapter 1 derives it); the Looking-ahead claim that *Analysis on the Real Line* takes trichotomy as an axiom and flags each genuinely non-constructive step (check against STATUS rows 101–103 and AN1's drafted text; "pointing back to this section" was dropped at S2, since AN1.1 points to Chapter 4).

**New and changed exercise answers:**
20. 5.1 A1 (d)'s solution; A2 (a)–(j); C2's reworded sentence.
21. 5.2 A2 (a)–(j).
22. 5.3 A1 (a), (b), (d); A2 (a)–(h); B2 (the nine blanks and their answers, against old B2's skeleton); C3 (new claim "\( 4 \mid n^2 \) or \( 4 \mid n^2 - 1 \)": the level-3 proof, the skeleton described, the list of unsaid steps).
23. 5.4 B1's plain-words solution (every line's warrant matches the folded formal solution; the uses of \( \delta > 0 \)); C1 (the proof is correct; each explanation; RAA at (7); the marking scheme); C2 (moved verbatim).
24. 5.6 A1 (d)'s "(part (a))"; A2 (a)–(h) (each entry; each true/false verdict; (b) "in general false"; (e) now an (N7) item, true; (g) false).
25. 5.7 B4 (the moved Quick check, verbatim; is B4 doable with the folds of Chapters 2–4 closed? ch02-revision folds Peirce's proof and the interderivability proof, so "derived with RAA" must be readable from the main-line statements or the folds: B4 is off the core track, which is acceptable).

**Routes to confirm do not rest on removed or folded material:** no main-line proof or claim cites a step that now exists only in a fold (F5.3-b's level 0 is cited by nothing on the main line; the level-1 answers replace it); every A and B exercise is doable with the folds closed (5.3 A1 now asks about levels 1 and 3; 5.4 B1's main solution stands alone; 5.7 B4 is off the core track); the forward-pointer grep of binding rule 3 finds only the three boxes.

---

## 9. Decisions this file makes against the plan's or the report's wording (for S2 and the author)

- **D1.** `def-silent-steps` is not reduced to the principle with its 27-item list folded. The definition is cited 20 times inside the chapter and by name in fd2 (01:203, 04:475: "Chapter 5's convention allows: the two instances of ∀E at the obvious term …"), and STYLE §12.0 forbids folding a definition the main line uses. Instead the principle is stated first (in 5.1, where the card's column needs it), a six-row table gives the common cases, and the definition follows verbatim as "the official list". The report's rewording of the ninth item (03:55) is given as a sentence after the block, together with the eighth.
- **D2.** The catalogue's entries keep their order and wording, with the families as a table before the block, not as headings inside it and not as slogans prefixed to each entry; (N11) is split into lettered parts inside entry 11, not into new numbered entries. Fifty-eight later citations name entries by number, and one of them names (N11).
- **D3.** `exm-rhetoric-induction` stays one example after the three new subsections, since fd2 cites it twice as "how an induction is written". "A worked example under each" is met by `exm-rhetoric-existential` for "it suffices" and by parts (a) and (b) for induction and symmetry.
- **D4.** The report's suggested section reorder (5.4 first, 5.6's proofs as motivation) is not taken: section numbers are fixed (plan §2), and the index's second hook, Proof B, gives the motivation it asked for.
- **D5.** `exm-rhetoric-contradiction` keeps the RAA and case versions on the main line, and folds the ¬I/¬¬E version verbatim (not cut): 5.1 B2 asks the reader for exactly that rewrite on another proof, and the fold is its model. ch02-revision made 2.5 "the single home of ¬I vs RAA" with the \( x^3 \) proof both ways; 5.1's subsection is now short, with the BHK preview saying why the distinction matters.
- **D6.** Rule tags: new examples tag only structure and their group's rows; kept examples keep their tags (they illustrate the rows they tag), except `exm-annotate-abs`, which the plan names.
- **D7.** 5.4 C1 is a new proof of the uniqueness of limits, by RAA with \( \varepsilon = \abs{L - M}/2 \), not `exm-rhetoric-equality` again: that proof is already annotated rule by rule in 5.2, so self-explaining it would be re-reading.
- **D8.** Uniform continuity appears at levels 1 and 3 on the main line, with levels 0 and 2 folded verbatim rather than cut (the plan says "shown only at levels 1 and 3"; the folded text is reviewed and costs nothing on the core track).
- **D9.** The plan's "pointer to the debate about the material conditional (Read)" is a fold that names the view (relevance logics) and no book: a book title would be a forward pointer outside the box, and the plan's rule is techniques only.
- **D10.** Chapter 5 has no rule sections, so it gets no snapshots and no per-section cards (§1); drill banks go only to the four sections whose skills are recognition (§1 item 5).
- **D11.** The index gets no "Where this goes" note (ch03-revision gave its index one): Chapter 5 is the last chapter of the volume, and its three later-volume pointers belong to the sections they concern (5.3, 5.6, 5.7).

---

## 10. S2 replies

**Round 1.** Every finding applied; none disputed. Duplicates were applied once: the 5.5 example order (05:117, 05:49; the 05:21 sentence also reworded so that it no longer repeats 05:117), the undefined "intuitionistic" in 5.7 (the opening says "called intuitionists"; 07:149 reads "uses only rules other than RAA"), the faces Quick check (ii) together with 5.1 A2 (j), the nine blanks of 5.3 B2, and the verdicts of 5.6 A2 (e) and (g) ((e) replaced by an (N7) item). Choices among offered fixes: the easy expansion of 5.3 both ends with \( x_0 \in A \to x_0 > 0 \) (shape matches) and names both faults as 03:311 does; 5.1's budget is raised to 4,750 rather than cut further, and §5 is recomputed (31 and 47 hours unchanged); 5.3 C3 is a new claim ("\( 4 \mid n^2 \) or \( 4 \mid n^2 - 1 \)", with ∨I steps to restore) and B2 keeps old B2's claim, so §3 and the bookkeeping no longer re-key B2.
