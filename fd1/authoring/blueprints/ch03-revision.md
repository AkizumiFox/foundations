<!-- hand-written -->
# Revision blueprint: F1.3 Truth, Soundness and Completeness (fd1 Chapter 3), R3

**What this is.** A **delta** blueprint (stage S1) for revising the released Chapter 3 of *Logic and Proof* so that a first-year reader gets in more easily. It is complete on its own: a drafter executes it with this file, the current `fd1/src/ch03-semantics-soundness-completeness/`, the original blueprint `fd1/authoring/blueprints/ch03.md` (for anything this file does not change), `authoring/STYLE.md` (§11, §12), `DRAFTING.md` and `NOTATION.md`. The approved pilot `ch01-revision.md` is the model of format and register; where this file is silent on a convention, do what that file did. All line numbers below are of the **current** files (commit `03155f6`), written `02:249` for `02-induction.md` line 249, and so on; `ix` is `index.md`.

**Inputs.** The novice-reader report on Chapter 3 (workflow journal, `novice:ch03`), the corpus and classic-texts comparisons as digested in the fd1 revision plan (§2 Chapter 3 rows, §3 Chapter 3 items, §4–§6), and the pilot. Reference books were used for teaching technique only (a picture before a formal clause, a worked run before a general proof, a table of rows before a list of sequents). **Every new example, figure, drill and exercise below is the book's own.** The S2 rule of `ch03.md` (the text must not call the completeness route new; no Horn clauses, no SAT solvers) still binds.

**Binding rules for this revision.**
1. **No label is lost.** Every label now in the chapter survives, in this chapter, with its content. Only uncited `exr-` labels change, each named in §3. Every label cited anywhere (fd1 Ch2, Ch4, Ch5, fd2, fd3, fd4, an1) keeps its name and its section.
2. **Reviewed content of cited results does not change.** A statement or proof of a cited result is either kept on the main line or moved **verbatim** into a second-reading fold. The three places where this file rewords a cited proof (the table in `lem-coincidence`, the descent sentence in `thm-completeness`, the roadmap references in `exm-completeness-run`) keep the verbatim original in a fold beside the new wording and are S2a items (§8, items 1–3). Besides these, the vocabulary sweep of §4.7 item 2 ("conjunct" → "conjunctive clause"/"minterm") changes words in 3.7 results that are cited only inside the chapter (the statement of `prp-cnf-validity` (b); the proofs of `thm-dnf`, `thm-cnf`, `prp-cnf-validity`; one word of the proof of `thm-adequate-connectives`), without a verbatim fold (S2a item 7); and the spelling sweep "nonempty" → "non-empty" (§1 item 9) touches verbatim text everywhere.
3. **Forward pointers.** No `@ref` to an unseen result is a reason. Each section's main line and folds carry **at most one** pointer to a later chapter or volume, in its Looking-ahead box (STYLE §12.1); the cross-volume pointers now spread over §01 and §02 are gathered into one "Where this goes" note in `index.md` (§4.0). The index is not a section; its budget (≤ 1,100 words, §5) covers the note. Pointers to later sections **of this chapter** stay where they help, but never as reasons. After drafting, grep each section's main line and folds for `Chapter [4-9]`, `Section [4-9]\.`, `Sets, Relations`, `Analysis on the Real`, `Number Systems`; every hit other than the box is cut.
4. **Depends on R1 only.** The fold, Looking-ahead and drill-bank markup follow STYLE as amended by step R1 (already in STYLE §12). Nothing here needs the ∧I change of R0. The derivation renderer of R0 changes nothing in this file.

---

## 1. The volume-wide conventions, as applied to Chapter 3

Chapter 3 has **no rule sections**: it introduces no rule of inference. So the conventions that STYLE scopes to rule sections do not apply, and this file adds none of them:
- **no snapshots** (STYLE §12.4 scopes them to Chapters 1–2 and 4.4–4.6); the long derivations of 3.6 get a **case-split tree** instead (§4.6), as the plan asks;
- **no rule card** (STYLE §12.6);
- **no Givens/Goal table** (STYLE §12.5).

The conventions that do apply:
1. **Second-reading fold.** `::: {.second-reading title="…"}`. It is **not** `.optional`. Every fold is listed by current file:line in its section's plan; nothing else goes into a fold. A fold never sits inside a `.proof` or `.claim` div (the engine's behaviour there is untested): where part of a proof is folded, the fold follows the proof as a sibling.
2. **Meta-proofs** (STYLE §12.12): the proofs of `thm-structural-induction`, `lem-parenthesis-count`, `thm-unique-readability` (with the one-parse-tree argument), `thm-structural-recursion`, `lem-replacement`, `lem-context-inclusion`, `lem-weakening-cut` and `lem-connective-rows` go into folds, verbatim. Their statements and a one-sentence meaning stay on the main line. **Kept on the main line**, by decision: the proofs of `thm-strong-induction` (the reader's first proof by induction; fd2 ch02 01:88 discusses its base case), `lem-coincidence` (the full member of the chapter's faded triple, `ch03.md` Scaffolding), `lem-substitution` (its claim is what the new worked example illustrates), `thm-soundness`, `lem-truth-table-line` and `thm-completeness` (the three key proofs, with comprehension items in A1, an ordering item and two exit checks: STYLE §12.0's test fails if they are folded), and `lem-atom-splitting` (fd1 ch05 04:215 trains self-explanation on it, "its five numbered steps").
3. **Looking ahead.** `::: {.remark}`, then the title line `[Looking ahead]`, a blank line and the sentence, exactly as STYLE §12.1's template and delivered Chapter 1 (ch01 01:338, 02:696, 04:409) have it; no bold lead-in. It is the last block before `## Exercises`, at most one per section. The box texts in §4 give only the sentence. 3.2, 3.3 and 3.5 get one (texts in §4); 3.1 gets an in-chapter one; 3.4, 3.6, 3.7 get none.
4. **Quick-check density.** About one per 800–1,000 main-line words (STYLE §12.7). The new checks are written out per section.
5. **Drill banks.** STYLE §12.8 requires them only of rule sections. This chapter adds a bank `exr-<slug>-a2`, titled `[A2: Drill]`, to 3.1–3.6 anyway (the plan's §5 counts on them), 6–8 parts each, recall and judgement before construction, **one folded solution** answering every part in one or two lines. 3.7 gets none (second pass).
6. **Edge cases** (STYLE §12.3) go into folds where listed. The degenerate cases that the ⊥ case of every structural induction relies on (01:80, the warning 02:235) stay on the main line.
7. **School-level first** (STYLE §12.9): Chapter 3 has no analysis example before the warning 03:313, which stays.
8. **Notation.** Atoms are lower-case from 3.1 on, and 3.1's letter box (§4.1 item 3) is the one place that says who is who. The superscript in \( \varphi^{v} \) is glossed once as a label, not an exponent (§4.6). "Conjunct" keeps its ordinary meaning (one side of a conjunction) everywhere. 3.7's short form "conjunct" for a conjunction of literals becomes the full **conjunctive clause** (already the gloss at 07:33), and \( C_v \) is the **minterm** of the row of \( v \) (§4.7). *Recorded deviation from the plan (§3, 3.7: "renamed term").* "Term" is not free in fd1: Chapter 4 defines it formally (`def-term`, ch04 02:47, used throughout 4.2, 4.11, 4.12), and Chapter 3 already uses it in its ordinary sense, a part of a sum or of a long conjunction or disjunction (02:80-96, verbatim and quoted by fd2; 04:251; 07:7; the label `eq-many-term-values`). "Conjunctive clause" and "minterm" occur nowhere in fd1–fd3 or an1 outside 07:33 (grep of 2026-10-12), and "conjunctive clause" pairs with the "clause" of `def-cnf`.
9. **Spelling.** "nonempty" → "non-empty" everywhere in Chapter 3 (STYLE, "Hyphenation of 'non-'"), verbatim statements and proofs included: 02:266 (inside the statement of `lem-parenthesis-count` (b)), 02:271, 02:293, 02:296, 02:551-566 (C-solution), 03:520, and wherever else a grep finds it. Labels are exempt. As in the pilot, a spelling change alters neither label, tier nor content, and does not count as a rewording.

---

## 2. Section map

| Sec | Title (the `#` line, unchanged) | File (unchanged) | Kind |
|---|---|---|---|
| index | Truth, Soundness and Completeness | `index.md` | rewritten |
| 3.1 | Formulas as Objects | `01-formulas-and-parse-trees.md` | rewritten |
| 3.2 | Induction on Numbers and on Formulas | `02-induction.md` | rewritten |
| 3.3 | Valuations and Truth Tables | `03-valuations-and-truth-tables.md` | edited |
| 3.4 | Tautologies, Entailment and Equivalence | `04-entailment-and-equivalence.md` | edited |
| 3.5 | Soundness | `05-soundness.md` | edited |
| 3.6 | Completeness | `06-completeness.md` | edited |
| 3.7 | Normal Forms and Adequate Connectives | `07-normal-forms.md` | edited; second pass on the reading path |

Section numbers, titles and file names do not change (fd1 Ch4–5, fd2, fd3 and an1 name "Section 3.1" … "Section 3.7" and "Chapter 3" about 60 times). Two `##` headings change their wording: 3.1 "Subformulas and height" → "Subformulas"; 3.2 "Counting parentheses" → "Counting parentheses: the depth profile". No link anywhere targets either heading id (grep of 2026-10-12 for `#subformulas-and-height` and `#counting-parentheses` in fd1–fd3 and an1: no hit). 3.5's subsection "Reductio says something new" moves after the exercises (§4.5).

---

## 3. Labels

### 3.1 Every label now in the chapter

Citation counts are `@label` / `@fd1:label` hits outside Chapter 3 (grep of 2026-10-12): fd1 Ch2, Ch4, Ch5 (`fd1`), fd2, fd3, an1. fd4 cites two Chapter 3 labels, both kept verbatim: `ax-induction` (56 hits by `grep -o`, dependency-ledger comments included; 51 in prose) and `thm-strong-induction` (7; 5 in prose: fd4 ch03 01:5, 01:206, 04:230, 05:435; ch05 03:218). No other fd4 citation of a Chapter 3 label exists. Rather than widen the table for two rows, they are recorded here. "in-ch" counts hits inside Chapter 3. Every label stays in its current section unless the Status column says otherwise.

| Label | Now | Status | in-ch | fd1 | fd2 | fd3 | an1 |
|---|---|---|---|---|---|---|---|
| `def-formula` | 01:41 | kept, verbatim | 16 | 3 | 2 | — | — |
| `exm-formation-sequences` | 01:73 | kept; fourth string replaced (§4.1 item 4; S2a) | — | — | — | — | — |
| `exm-not-formulas` | 01:99 | kept | — | — | — | — | — |
| `def-parse-tree` | 01:161 | kept, verbatim | 2 | — | — | — | — |
| `exm-parse-trees` | 01:181 | kept | 2 | — | — | — | — |
| `def-subformula` | 01:236 | kept, verbatim | 2 | — | — | — | — |
| `def-height` | 01:258 | kept verbatim; **moves to 3.2**, after the one-parse-tree argument (§4.2 item 9; S2a) | 2 | — | — | — | — |
| `exm-shorthand-translation` | 01:302 | kept | 1 | — | — | — | — |
| `exr-formulas-and-parse-trees-a1` | 01:400 | kept; (b), (c) changed | — | — | — | — | — |
| `exr-formulas-and-parse-trees-b1` | 01:434 | kept; height dropped from the task and solution | — | — | — | — | — |
| `exr-formulas-and-parse-trees-b2`, `-c1` | 01:471, 01:492 | kept | — | — | — | — | — |
| `ax-induction` | 02:21 | kept, verbatim | 15 | 15 | 60 | 50 | 6 |
| `exm-sum-consecutive-products` | 02:70 | kept, verbatim (fd2 ch02 01:79 quotes 02:96) | — | — | 3 | — | — |
| `exm-power-inequality` | 02:101 | kept, verbatim; the warning after it kept (fd2 ch02 03:439, 02:253 cite "the warning after") | — | — | 4 | — | — |
| `thm-strong-induction` | 02:133 | kept; statement and proof verbatim, on the main line | 13 | 4 | 13 | 2 | — |
| `exm-threes-and-fives` | 02:167 | kept, verbatim | 1 | — | 4 | — | — |
| `thm-structural-induction` | 02:197 | kept; statement main line, proof → fold F3.2-b verbatim | 30 | 3 | 2 | — | — |
| `lem-parenthesis-count` | 02:259 | kept; statement main line, proof → fold F3.2-c verbatim | 10 | — | — | — | — |
| `thm-unique-readability` | 02:311 | kept; statement and idea main line, proof → fold F3.2-d verbatim | 6 | 1 | 1 | 2 | — |
| `thm-structural-recursion` | 02:352 | kept; statement and idea main line, proof → fold F3.2-e verbatim | 10 | 4 | 2 | 2 | — |
| `exm-recursive-definitions` | 02:391 | kept, verbatim | 2 | — | — | — | — |
| `exr-induction-a1` | 02:430 | kept; (c)–(e) → new `-c4`; new (c), (d) | — | — | — | — | — |
| `exr-induction-b1` | 02:460 | **frozen** (an1 cites it) | — | — | — | — | 1 |
| `exr-induction-b2`, `-b3`, `-c1`, `-c2`, `-c3` | 02:480–607 | kept | — | — | — | — | — |
| `def-valuation` | 03:53 | kept, verbatim | 1 | 1 | — | — | — |
| `def-truth-value` | 03:75 | kept, verbatim | 24 | 3 | 1 | — | — |
| `exm-value-down-the-tree` | 03:121 | kept | 1 | — | — | — | — |
| `lem-coincidence` | 03:164 | kept; statement and idea verbatim; proof: atoms, ⊥, ¬, ∧ verbatim, ∨/→/↔ as a three-row table, the three verbatim paragraphs in fold F3.3-b (S2a) | 13 | 3 | — | — | — |
| `def-truth-table` | 03:212 | kept, verbatim | 2 | — | — | — | — |
| `exm-truth-table-modus-ponens`, `exm-table-contrapositive` | 03:224, 03:249 | kept | 5, 4 | — | — | — | — |
| `exm-backwards-from-f` | 03:273 | kept, verbatim | — | 2 | — | — | — |
| `exr-valuations-and-truth-tables-a1`, `-b1`, `-b2`, `-b3` | 03:329–456 | kept (`-b2` is the faded triple's middle item) | — | — | — | — | — |
| `exr-valuations-and-truth-tables-c1` | 03:478 | old item **moves** to 3.4 as new `exr-entailment-and-equivalence-c3` (restated with ⊨, S2a); the label now carries a new item (§4.3) | — | — | — | — | — |
| `exr-valuations-and-truth-tables-c2` | 03:526 | **frozen** (cited 07:334) | 1 | — | — | — | — |
| `def-tautology` | 04:11 | kept, verbatim | 2 | — | 1 | — | — |
| `def-satisfiable` | 04:28 | kept, verbatim | 2 | — | — | — | — |
| `def-valid-argument` | 04:54 | kept, verbatim | 5 | 3 | 1 | — | — |
| `exm-affirming-the-consequent` | 04:86 | kept | 2 | 1 | — | — | — |
| `exm-three-premise-entailment`, `exm-grouping-of-implications` | 04:100, 04:114 | kept | —, 1 | — | — | — | — |
| `def-semantic-equivalence` | 04:146 | kept, verbatim | 4 | — | 1 | — | — |
| `prp-standard-equivalences` | 04:162 | kept; statement and proof verbatim | 6 | — | 6 | — | — |
| `lem-replacement` | 04:271 | kept; statement and idea main line, proof → fold F3.4-b verbatim | 1 | — | — | — | — |
| `lem-substitution` | 04:326 | kept; statement and proof verbatim, main line | 5 | 1 | — | — | — |
| `exr-entailment-and-equivalence-a1`, `-b1`, `-b2`, `-b3`, `-c1`, `-c2` | 04:383–557 | kept (`-c1` is the faded triple's last item) | — | — | — | — | — |
| `lem-context-inclusion` | 05:65 | kept; statement and idea main line with a new picture, proof → fold F3.5-a verbatim | 22 | 8 | — | — | — |
| `thm-soundness` | 05:124 | kept; statement, Try-it-first, Idea and proof verbatim, main line | 17 | 19 | — | — | — |
| `exm-soundness-run` | 05:224 | kept | 1 | — | — | — | — |
| `cor-refuting-row` | 05:266 | kept, verbatim | 11 | 15 | 1 | — | — |
| `thm-raa-independent` (.optional) | 05:323 | kept, verbatim, `.optional`; **moves after the exercises** of 3.5 into the optional excursion (§4.5) | 2 | 7 | — | — | — |
| `exr-soundness-a1`, `-b1`, `-b2`, `-c1`, `-c2` | 05:363–525 | kept | — | — | — | — | — |
| `lem-weakening-cut` | 06:30 | kept; statement and idea main line, proof → fold F3.6-b verbatim | 11 | 5 | — | — | — |
| `lem-connective-rows` | 06:82 | kept; statement main line, proof (table and seven derivations) → fold F3.6-c verbatim | 15 | — | — | — | — |
| `lem-truth-table-line` | 06:253 | kept, verbatim, main line | 15 | — | — | — | — |
| `exm-truth-table-line-run` | 06:305 | kept | — | — | — | — | — |
| `lem-atom-splitting` | 06:343 | kept, verbatim, main line | 9 | 3 | — | — | — |
| `thm-completeness` | 06:396 | kept; statement verbatim; proof verbatim except 06:445 (T(m)), replaced by one sentence, verbatim in fold F3.6-d (S2a) | 14 | 3 | 3 | — | — |
| `exm-completeness-run` | 06:456 | kept; **moves before the proof** (after the Idea), "Step 2"/"Step 3" → the roadmap's ②/③ (S2a) | — | — | — | — | — |
| `cor-derivable-iff-valid` | 06:519 | kept, verbatim | 2 | 2 | — | — | — |
| `exr-completeness-a1`, `-b1`, `-b2`, `-b3`, `-c2` | 06:572–815 | kept (`-b2` gains a case-split tree) | — | — | — | — | — |
| `exr-completeness-c1` | 06:781 | **frozen** (cited 06:301) | 1 | — | — | — | — |
| `eq-many-term-values`, `eq-row-conjunct` | 07:13, 07:83 | kept (labels unchanged; the prose around `eq-row-conjunct` says "minterm", and "term" in `eq-many-term-values` keeps its ordinary sense) | 11, 3 | — | — | — | — |
| `def-literal`, `def-dnf`, `def-cnf` | 07:22–43 | kept, verbatim (their texts do not use "conjunct") | —, 1, — | — | — | — | — |
| `exm-dnf-exclusive-or` | 07:86 | kept; "conjunct" → "conjunctive clause" | 1 | — | — | — | — |
| `thm-dnf`, `thm-cnf` | 07:102, 07:132 | kept; statements verbatim; proofs verbatim except "conjunct(s)" → "conjunctive clause(s)" or "minterm(s)" (S2a) | 5, 2 | — | — | — | — |
| `exm-normal-forms-two-routes`, `exm-cnf-validity-glance` | 07:162, 07:247 | kept; "conjunct" → "conjunctive clause" | — | — | — | — | — |
| `prp-cnf-validity` | 07:214 | kept; (b) "some conjunct" → "some conjunctive clause", proof likewise (S2a) | 4 | — | — | — | — |
| `def-truth-function` | 07:270 | kept, verbatim (fd2 cites it) | — | — | 1 | — | — |
| `def-adequate`, `thm-adequate-connectives` | 07:283, 07:291 | kept; statements verbatim; proof of `thm-adequate-connectives` verbatim except "the conjuncts \( C_{v} \)" → "the minterms \( C_{v} \)" at 07:305 (S2a) | —, 6 | — | — | — | — |
| `exr-normal-forms-a1`, `-b1`, `-b2`, `-b3`, `-c2`, `-r1`, `-r2`, `-r3` | 07:354–680 | kept; "conjunct" → "conjunctive clause" where it means one (07:359, 07:369, 07:373, 07:375, 07:395, 07:397, 07:430, 07:436) | — | — | — | — | — |
| `exr-normal-forms-c1` | 07:441 | **frozen** (cited 07:336) | 1 | — | — | — | — |
| `exr-normal-forms-c3` | 07:507 | **renamed → `exr-completeness-c3`**, moved to 3.6, content unchanged (§4.6) | — | — | — | — | — |
| `exr-normal-forms-c4` | 07:582 | **renamed → `exr-normal-forms-c3`**, content unchanged except "conjuncts" → "minterms" at 07:620 (one per T-row) | — | — | — | — | — |

Fold-held results are not `.optional` and remain citable (STYLE §12.0); `check_optional.py` and `check_forward_deps.py` read them as main line.

### 3.2 New labels

`exr-formulas-and-parse-trees-a2`, `exr-induction-a2`, `exr-induction-c4`, `exr-valuations-and-truth-tables-a2`, `exr-entailment-and-equivalence-a2`, `exr-entailment-and-equivalence-c3`, `exm-substitution-in-one-row`, `exr-soundness-a2`, `exr-completeness-a2`, `exr-completeness-c3`. No new `def-`, `thm-`, `lem-` or `prp-` label. Each was grepped free in `fd1/src` on 2026-10-12; grep again before creating it (DRAFTING rule).

### 3.3 Bookkeeping the renames force (coordinator, S4)

- `fd1/authoring/ledger/ch03.yaml`: re-key `exr-normal-forms-c3` → `exr-completeness-c3` (file `06-completeness.md`) and `exr-normal-forms-c4` → `exr-normal-forms-c3`, verdicts kept but stale (new hash), as the pilot did for renamed items. The old `exr-valuations-and-truth-tables-c1` entry is re-keyed to `exr-entailment-and-equivalence-c3` (file `04-…`; stale); the label `exr-valuations-and-truth-tables-c1` gets a **new** entry for its new item, no verdict carried. `def-height` changes `file:` to `02-induction.md`. `exr-induction-a1` keeps its key (changed item, re-reviewed). Retire nothing.
- `fd1/verify/ch03/`: rename `exr-normal-forms-c3.py` → `exr-completeness-c3.py` and `exr-normal-forms-c4.py` → `exr-normal-forms-c3.py`; `exr-valuations-and-truth-tables-c1.py` moves to `exr-entailment-and-equivalence-c3.py` and a new `exr-valuations-and-truth-tables-c1.py` checks the parity item; `thm-raa-independent.py` gains the 3×3 table. New sidecars are listed per section.
- `NOTATION.md`: row 144 (`\hgt`): "F1.3 §01 `def-height`" → "F1.3 §02 `def-height`, after `thm-unique-readability`". Row 157 (`u`, `\models_3`): "local to F1.3 §05, the optional excursion after its exercises". Row 159 (`\varphi^{v}`): "the literals of §07 rows" → "the literals of §07 minterms"; add "the superscript is a label, not an exponent". Row 160: NAND is in §04 C1 and §07 C1 (unchanged). Add two rows: "conjunctive clause: a conjunction of one or more literals (F1.3 §07; not Chapter 4's `def-term`, and not a conjunct)"; "minterm \( C_v \): the conjunctive clause of the signed atoms of the row of \( v \) (F1.3 §07)". Add one row for 3.3 C1: "\( f_v(\varphi) \): the number of occurrences of atoms in \( \varphi \) false under \( v \) (local to F1.3 §03 C1)".

---

## 4. Per-section plans

Budgets: **main line** = prose words by `tools/check_structure.py`'s `prose_words`, counted outside `.second-reading` folds and before `## Exercises`; folds counted apart. Exercises are budgeted separately (drill answers one or two lines each). Totals in §5.

### 4.0 `index.md` (rewritten)

1. **Opening (new, ~150 words; replaces ix:3).** "Section 2.6 searched for a derivation of \( P \to Q \vdash Q \to P \), and every route stalled. A search that fails proves nothing: a cleverer derivation might exist. Here is something that does prove it." Then the four-row table, in a Markdown table with the refuting row in **bold** and a fifth column whose only entry, in that row, is **"this row"**:

   | \( p \) | \( q \) | \( p \to q \) | \( q \to p \) | |
   |---|---|---|---|---|
   | T | T | T | T | |
   | T | F | F | T | |
   | **F** | **T** | **T** | **F** | **this row** |
   | F | F | T | T | |

   Then: "In the third row the premise \( p \to q \) is true, because its hypothesis is false (the promise reading of Section 1.1), and the conclusion \( q \to p \) is false. By the end of this chapter this one row is a **proof** that no derivation of \( q \to p \) from \( p \to q \) exists, however long." (The atoms are lower-case already, as in the chapter; "Section 3.1 says why" in parentheses after the first lower-case letter.)
2. **Story (ix:5, cut to ~110 words, no `@ref`):** the answer is to give formulas a meaning; soundness (whatever can be derived is true in every row where the premises are true, so one such row with a false conclusion proves that no derivation exists); completeness (whatever is true in every such row can be derived). To prove them, formulas become objects and induction arrives. Last sentence of ix:5 ("The chapter ends with normal forms …") kept.
3. **The chapter map:** the "two kinds of follows" table of 04:367-373, reproduced with two changes: the "Defined in" row reads "@def-derivable (Section 1.2)" and "Section 3.4" (no `@ref` to the unseen `def-valid-argument`), and a last row **"Tied together by"**: "soundness, Section 3.5: if \( \Gamma \vdash \psi \), then \( \Gamma \models \psi \)" | "completeness, Section 3.6: if \( \Gamma \models \psi \), then \( \Gamma \vdash \psi \)". Lead sentence: "The chapter is about two meanings of 'follows' and the two theorems that say they agree." (The table stays in 3.4 as well, where its symbols are defined.)
4. **What you need:** ix:7 kept.
5. **Time:** recomputed from the delivered text (§5). §5's estimate is "About 33 hours on the core track (Sections 3.1–3.6: …); about 56 hours for everything"; no figure is fixed in advance.
6. **How to read this chapter (new, ~120 words; bold lead-in):** "A first reading takes Sections 3.1–3.6 with every second-reading fold closed. Each section's main line teaches the section, and every A and B exercise can be done from it. The folds hold the proofs of structural induction, the parenthesis count, unique readability and structural recursion, the bookkeeping lemmas of 3.4–3.6, and the descent in the completeness proof. They are not optional: later proofs use those results, and the proofs are complete. They can wait for a second pass. Section 3.7, on normal forms, is a second-pass section as a whole. Nothing in Chapters 4 and 5 uses it."
7. **Roadmap:** seven bullets. 3.1 as ix:13 minus "and height". 3.2 as ix:14, adding "and a picture, the depth profile, that shows why the parentheses settle the reading". 3.3–3.7 as ix:15-19.
8. **Named moves:** ix:23-27 verbatim.
9. **Where this goes (new, ~140 words; bold lead-in):** "Chapter 4 looks inside the atoms: it gives 'every' and 'some' their rules and their meaning. Chapter 5 says what reductio asserts that the other rules do not, and who objected to it. Three later volumes take up threads of this chapter. *Sets, Relations, and Cardinality* makes 'the smallest collection of strings closed under the building steps' and 'function' exact (Chapter 1). It proves induction equivalent to the well-ordering principle and shows a famous false induction that breaks at its first step (Chapter 2). *Number Systems: From \(\nN\) to \(\nR\)* derives induction from the axioms of set theory (Chapter 1). *Analysis on the Real Line* takes the least upper bound axiom as given, as this chapter takes induction (Chapter 1)." These are the pointers cut from 01:13, 01:139, 02:13, 02:42, 02:124 and 02:348 (§4.1, §4.2). STATUS rows 79–84 move their source to "index" (§6).

### 4.1 Section 3.1: Formulas as Objects (`01-formulas-and-parse-trees.md`, rewritten)

**Budget:** main line ≤ 4,400 words (now 4,821; about 800 folded, moved or cut and about 400 new); folds ≤ 650. Looking ahead (in-chapter; `[Looking ahead]` title line, §1 item 3): "Section 3.2 proves that every formula is built in only one way. Then 'the parse tree' of a formula makes sense, and with it the height of a formula."

**New order of material.**
1. **Opening frame** (01:3), cut to ~70 words: keep the first two sentences and "A theorem about every formula needs, first of all, an exact description of what a formula is. This section gives it." Cut the rest.
2. `## Why formulas must become objects`: 01:7-11 kept. 01:13: keep up to "is not a description anyone can reason from."; replace its last sentence ("So we now do for formulas what *Analysis on the Real Line*, Chapter 1 will do …") by "So we now say exactly which objects we mean, in a form that later proofs can use." 01:15 kept.
3. `## The alphabet`: 01:19-24 kept. 01:26 kept up to "the theorems of this chapter need the difference.". Then **the letter box** (`::: {.remark}`, first words `**Who is who: the letters of this chapter.**`, ~130 words with the table), replacing 01:28-31:

   | Letter | Stands for | Inside a formula? | Example |
   |---|---|---|---|
   | \( p, q, r, p_1, p_2, \dots \) | an **atom**, one symbol of the language | yes | \( (p \wedge \neg q) \) |
   | \( \varphi, \psi, \chi \) (phi, psi, chi) | any formula: a **metavariable**, a name we use when talking about formulas | never | "if \( \varphi \) is a formula, so is \( \neg\varphi \)" |
   | \( \Gamma, \Delta \) (capital gamma, delta) | a finite list of formulas, as in the sequents of Chapter 1 (@def-derivable) | never | \( \Gamma \vdash \psi \) |
   | \( P, Q, R \) of Chapters 1–2 | arbitrary statements; read from now on as atoms, or as any formulas (the last part of this section) | they are replaced | \( P \to Q \) read as \( p \to q \) |

   After the box, 01:29's sentence "Chapter 1 already used these three letters in exactly this way, in the schemas of its rules (@def-rule-schema)." kept as prose. 01:33 (the circle) **moves** to just before `def-formula` (item 4), the first place it is needed ((F4) uses it), as one sentence: "In clause (F4) below, \( \circ \) stands for any one of the four binary connectives, as \( \varphi \) stands for any formula: \( (\chi_j \circ \chi_l) \) means any one of \( (\chi_j \wedge \chi_l) \), \( (\chi_j \vee \chi_l) \), \( (\chi_j \to \chi_l) \), \( (\chi_j \leftrightarrow \chi_l) \)." **Quick check (new):** "Which of these is a formula, and which is a name for formulas or for a list: \( (p \to q) \); \( (\varphi \to q) \); \( \Gamma \)?" Solution: \( (p \to q) \) is a formula. \( (\varphi \to q) \) is not a formula, since \( \varphi \) is no symbol of the language; it is a pattern, and each formula put in for \( \varphi \) gives a formula. \( \Gamma \) names a list of formulas.
4. `## Formulas`: 01:37 kept. Then **"Building one formula"** (new, ~180 words, bold lead-in), the build-up before the definition: "Here is the formula \( ((p \wedge \neg q) \to p) \) built one step at a time. Each entry of the list is an atom, or is made from earlier entries by one connective." The list, as a **figure** (TikZ, `\begin{tikzpicture}`, not an `nd` block): five nodes in a row, left to right, with their numbers above: 1 \( p \), 2 \( q \), 3 \( \neg q \), 4 \( (p \wedge \neg q) \), 5 \( ((p \wedge \neg q) \to p) \). Curved arrows run from each entry back to the earlier entries it is made from: 3 → 2; 4 → 1 and 4 → 3; 5 → 4 and 5 → 1. Below each node a short label: "atom", "atom", "¬ on 2", "1 ∧ 3", "4 → 1". Caption: "Each entry is an atom, or is built from earlier entries by one connective. The atom \( p \) is used twice and listed once." Then: "A list like this is called a formation sequence. The definition below has one more clause than the building steps. Its clause (F4) says that the formulas are exactly the last entries of such lists: the list you just saw, in general." Then the sentence on \( \circ \) (item 3), the gloss 01:39, `def-formula` **verbatim**, "In words, clause by clause" 01:54-59 kept; the (F4) bullet ends with one new sentence: "Think of building blocks: (F1) lists the blocks, (F2) and (F3) the two ways of joining them, and (F4) says that only what is built in this way counts." 01:61-71 (two facts, the first-symbol test) kept.
   **Quick check (new, after 01:71):** "Write a formation sequence for \( \neg(p \vee \bot) \), and say which earlier entries each entry uses." Solution: \( p \), \( \bot \), \( (p \vee \bot) \), \( \neg(p \vee \bot) \); entry 3 uses 1 and 2, entry 4 uses 3; entries 1 and 2 use none.
   `exm-formation-sequences`: the statement's fourth string \( ((p \wedge \neg q) \to p) \) (built above) is replaced by \( (\neg p \vee (q \to \bot)) \). Solution 01:80 and 01:82-86 kept; 01:88-92 replaced: "For \( (\neg p \vee (q \to \bot)) \): \( p, \ \neg p, \ q, \ \bot, \ (q \to \bot), \ (\neg p \vee (q \to \bot)) \). Entries 1, 3 and 4 are atoms or \( \bot \). Entry 2 is \( \neg \) in front of entry 1. Entry 5 is \( (\chi_3 \to \chi_4) \), and entry 6 is \( (\chi_2 \vee \chi_5) \)." 01:94 → fold F3.1-a, placed right after the example's solution (a sibling of the `.solution` div, before 01:97), with its opening adjusted to name its example (S2a item 6): "A formula has many formation sequences. In @exm-formation-sequences we could have listed \( q \) before \( p \) in the last list, or added entries that are never used, such as \( r \) or \( \neg r \)." The rest of 01:94 verbatim. 01:97 kept; `exm-not-formulas` kept; 01:115 kept; Quick check 01:117-133 kept.
5. `## Why this definition`: 01:137 kept. 01:139 kept to "the formulas are only those strings that the building steps reach."; its last sentence becomes "In other words, the formulas are the **smallest** collection of strings closed under (F1)–(F3)." (fd2 ch01 02:233 and 02:256 rely on the phrase; the pointer to *Sets, Relations, and Cardinality* moves to the index, §4.0 item 9.) 01:141: delete the parenthesis "(Section 3.3 makes 'true under an assignment of values' exact; the everyday reading of Chapter 1 is enough here.)" and put "(the everyday reading of Chapter 1 is enough here)" after "they say different things:". The rest of 01:141-145 is kept. 01:147 and 01:149 → fold F3.1-b, placed after 01:145 where they now stand. Warning 01:151-153 kept.
6. `## Parse trees`: 01:157-230 kept (`def-parse-tree`, 01:175, 01:177, 01:179, `exm-parse-trees`, 01:230).
7. `## Subformulas` (renamed): 01:234-254 kept (`def-subformula`, 01:242, 01:244-252, 01:254). 01:256-266 **leave 3.1**: `def-height` with 01:264 goes to 3.2 (§4.2 item 9). 01:266 (the "promise" paragraph) is cut. The Quick check 01:268-278 loses its height question. Its prompt becomes "Draw the parse tree of … and list its subformulas.", and its solution drops the last paragraph (01:277). The height warning 01:280-282 → 3.2, after `def-height`. Warning 01:284-286 kept.
8. `## Shorthand and official formulas`: 01:290-338 kept (`exm-shorthand-translation` with its two trees).
9. `## Letters, metavariables and substitution`: 01:342-361 kept. Then the slogan, italic, as its own paragraph: "*A derivation written with letters is a template.*" Then 01:363 (the bold **Substitution.** statement) kept. 01:365-369 ("Here is why", three paragraphs) → fold F3.1-c, verbatim, placed right after 01:363 with the lead sentence on the main line: "The fold below checks that every line stays a formula and stays justified." The worked example 01:371-388 kept on the main line. 01:390 is cut to its first two sentences and one more: "We use it twice later in the chapter, in the soundness proof of Section 3.5 and in the completeness proof of Section 3.6." The pointer to "a lemma of Section 3.4" is cut, since 3.4's box (§4.4) makes the comparison. Remark 01:392-394 kept.
10. **Looking ahead** (text above).

**Folds.** F3.1-a `title="Many formation sequences"`, after `exm-formation-sequences`: 01:94, its opening adjusted as in item 4. F3.1-b `title="Two smaller points"`, in "Why this definition": 01:147 (why no parentheses around a negation) and 01:149 (why atoms), verbatim. F3.1-c `title="Why the result is again a derivation"`: 01:365-369 verbatim.

**Cut outright:** 01:13's comparison with *Analysis on the Real Line*; 01:139's pointer to *Sets, Relations, and Cardinality*; 01:266; the height parts of the Quick check; old 01:88-92 (now the build-up's figure).

**Quick checks:** formulas (01:117, kept), parse tree and subformulas (01:268, cut down), letters (new), formation sequence (new). That is four in about 4,400 words.

**Exercises.**
- **A1** (kept label). (a), (d), (e) unchanged. (b) → "List the subformulas of \( (\neg(p \to q) \vee q) \)." Answer: the five of 01:423, without the height sentence. (c) → "Write a formation sequence of \( ((p \vee q) \wedge \neg(p \vee q)) \) in which \( (p \vee q) \) is listed once." Answer: \( p, \ q, \ (p \vee q), \ \neg(p \vee q), \ ((p \vee q) \wedge \neg(p \vee q)) \). Old (c) (subformulas have smaller height) moves to 3.2's drill (g).
- **A2: Drill** (new), with answers:
  (a) Is \( \neg\neg\neg p \) a formula? — Yes: \( p, \neg p, \neg\neg p, \neg\neg\neg p \).
  (b) Is \( (p \wedge (q)) \) a formula? — No. It would be \( (\varphi \wedge \psi) \) with \( \psi \) the string \( (q) \). That string begins with \( ( \) and has length 3, and a formula beginning with \( ( \) has length at least 5.
  (c) How many symbols has \( ((p \to q) \vee \neg r) \)? — Ten: \( ( \ ( \ p \to q \ ) \ \vee \ \neg \ r \ ) \).
  (d) Write the official formula for \( \neg p \vee q \to r \). — \( ((\neg p \vee q) \to r) \).
  (e) Main connective of \( \neg(p \wedge q) \to r \)? — \( \to \); officially \( (\neg(p \wedge q) \to r) \).
  (f) Draw the parse tree of \( (p \to (q \to p)) \) and list its leaves. — Root \( \to \), left the leaf \( p \), right \( \to \) over \( q \) and \( p \); the leaves are \( p \), \( q \), \( p \).
  (g) Which of these are subformulas of \( ((p \wedge q) \to r) \): \( (p \wedge q) \); the string \( q) \to r \); \( (q \to r) \); \( r \)? — \( (p \wedge q) \) and \( r \). The string \( q) \to r \) is not a formula. \( (q \to r) \) is a formula, but no node of the tree carries it.
  (h) In the derivation of @prp-implication-transitive printed in this section, put \( q \) for \( P \), \( q \) for \( Q \) and \( p \) for \( R \). Is the result a derivation? — Yes. Lines 1–6 become \( q \to q \), \( q \to p \), \( q \), \( q \), \( p \), \( q \to p \), and lines 4, 5, 6 are still instances of \( \rulename{{\to}E} \), \( \rulename{{\to}E} \), \( \rulename{{\to}I} \). A substitution may put the same formula for two letters.
- **B1** (kept label): "list its subformulas, and give its height" → "and list its subformulas". The solutions drop "Height 3 …" and 01:468's "Height \( 3 \)."
- **B2**: kept.
- **C1**: kept, except that its solution 01:523 is reworded without height, which is now defined only in 3.2: "Their parse trees have the root \( \to \) in each case: in the first two, the leaf \( p \) on the left and a chain of two arrows on the right (leaning right, or leaning left); in the third, two one-arrow trees side by side; in the last two, a chain of two arrows on the left and the leaf \( s \) on the right." (S2a item 4.)

**Dependency ledger (in-file).** 01's line for `def-height` (01:539) moves to 02's in-file ledger, reworded "the parse tree, hence the height, is well defined | thm-unique-readability (this section), proved just before". 01:539's last clause ("nothing here uses the height before then except examples of drawing") is dropped: 01 no longer uses height, and 02's F3.2-b remark mentions height before `def-height`, so the clause would be false in 02. 02's full replacement line: `def-height (claim): "the" parse tree, hence the height, is well defined | thm-unique-readability (this section), proved just before`. 01 keeps no `def-height` line.

**Sidecars:** the build-up figure's sequence and the new `exm-formation-sequences` string (in `_s0102_formulas.py`); drill (b), (c); drill (h) (`check_fitch` on the substituted derivation).

### 4.2 Section 3.2: Induction on Numbers and on Formulas (`02-induction.md`, rewritten)

**Budget:** main line ≤ 4,900 words (now 6,187; about 1,780 folded and 190 cut, about 680 new with the hook at ~110 words and 02:251's first sentence cut); folds ≤ 2,300. Looking ahead (`[Looking ahead]` title line, §1 item 3): "Chapter 4 gives 'for every' and 'there is' their rules, among them the step from 'this \( n \) was arbitrary' to 'for every \( n \)' that every inductive step takes."

**New order of material.**
1. **Opening frame** (02:3), cut to ~90 words: keep its first three sentences and "It is **induction**, first on the natural numbers, where it is familiar, then on formulas." Cut "With it we prove …" (the roadmap says it).
2. `## One argument for infinitely many cases`: 02:7-11 kept. 02:13 → "As in Chapters 1 and 2, 'for every \( n \in \nN \)' and 'there is a \( k \)' are used in their everyday sense. As in the rest of the book, \( \nN = \{0, 1, 2, \dots\} \) starts at \( 0 \), and the arithmetic and order of the natural numbers are school facts." The pointers to Chapter 4 and to *Sets, Relations, and Cardinality* are cut. The quantifier pointer is now the Looking-ahead box; the sets pointer is in the index.
3. `## The principle of induction`: 02:17-32 kept (`ax-induction` verbatim). 02:34 → "In symbols (here \( \forall \) abbreviates the words 'for every'):", with the display 02:35-38 unchanged (fd1 ch04 01:165 and 02:431 refer to "the display after @ax-induction"). 02:40 kept. 02:42 → "**Its status.** We take @ax-induction as a basic property of \( \nN \), given and not proved. It is, in a precise sense, what the three dots in \( \{0, 1, 2, \dots\} \) mean: the natural numbers are what we reach from \( 0 \) by adding one, again and again, and nothing else. Every later use cites this principle." (fd3 ch01 03:3 and fd2 ch02 index:3 stay true.) Dominoes 02:44 kept. 02:46 → fold F3.2-a. 02:48-62 (the step as a box, with the schema) kept. 02:64 → "For now, 'let \( n \in \nN \)' means what Chapter 1 made it mean (Section 1.1): one fixed number, not further specified." (Chapter 4's clause goes to the box.) 02:66 ("Starting from another number") kept verbatim (fd2 ch02 02:7 names it).
4. `exm-sum-consecutive-products` and `exm-power-inequality` verbatim (02:68-121). **Quick check (new, after 02:121):** "For the claim '\( 5^n - 1 \) is divisible by \( 4 \) for every \( n \in \nN \)', write down the base case and the statement of the inductive step, without proving the step." Solution: base case: \( 5^0 - 1 = 0 = 4 \cdot 0 \). Step: for every \( n \in \nN \), if \( 4 \mid 5^n - 1 \), then \( 4 \mid 5^{n+1} - 1 \). (It holds, since \( 5^{n+1} - 1 = 5(5^n - 1) + 4 \).) Warning 02:123-125 kept except its last sentence ("*Sets, Relations, and Cardinality*, Chapter 2 shows a famous 'proof' …"), which moves to the index.
5. `## Strong induction`: 02:129-187 kept on the main line: the theorem, the hidden base case 02:141, the Idea, the proof, the Quick check 02:157-163 and `exm-threes-and-fives`. fd2 ch02 01:88 discusses this proof's base case, and the novice report's worry about 02:141 is met by the threes-and-fives cases. Decision: kept, not folded.
6. `## Structural induction`: 02:191-195 kept; `thm-structural-induction` verbatim; 02:211 kept. The Idea 02:213-215 kept, followed by a **figure** (new, TikZ): the five-entry sequence of 3.1's build-up figure, \( p \), \( q \), \( \neg q \), \( (p \wedge \neg q) \), \( ((p \wedge \neg q) \to p) \), with the same back-arrows, and under each entry a check mark and its reason: "✓ by (i)", "✓ by (i)", "✓ by (ii), from 2", "✓ by (iii), from 1 and 3", "✓ by (iii), from 4 and 1". Caption: "The property spreads from left to right. Each entry gets its check mark from (i), or from entries to its left that already have one." Then one sentence on the main line: "The proof, in the fold below, makes 'from left to right' exact with strong induction on the position in the list." The proof 02:217-227, the sentence 02:229 and the remark 02:231-233 → fold F3.2-b. The remark is **reworded**, because `def-height` now comes later in the section (S2a): "A tempting alternative is induction on the **height** of a formula (the number of nodes on a longest branch of its parse tree, defined later in this section). That route is circular here. The height is read off the parse tree, and that a formula has only one parse tree is proved below from unique readability, whose proof uses structural induction. Inducting on the position in a formation sequence needs nothing but @def-formula." Warning 02:235-237 and Quick check 02:239-247 kept.
7. `## Counting parentheses: the depth profile` (renamed; new main line ~350 words before the lemma):
   - **The hook** (new, ~110 words; the text below is the whole of it): "Section 3.1 met the string \( p \wedge q \vee r \), which can be read as \( (p \wedge q) \vee r \) or as \( p \wedge (q \vee r) \). With \( p \) and \( q \) false and \( r \) true, the first reading is true and the second false. Section 3.3 defines the truth value of a formula one clause per connective, and the clause to use is decided by the main connective. A string with two main connectives would get two values. Formulas carry parentheses, and the parentheses are meant to settle the reading. This subsection and the next prove that they do, for every formula. The tool is a count."
   - **The depth profile** (new, ~150 words): "Read a formula from left to right, keeping a running count: add one at each \( ( \), subtract one at each \( ) \). The count just before a symbol is its **depth**: how many pairs of parentheses are open around it." **Figure** (new, TikZ step graph): for \( ((p \wedge q) \vee r) \), the nine symbols along the horizontal axis, and above each one its depth: \( ( \) 0, \( ( \) 1, \( p \) 2, \( \wedge \) 2, \( q \) 2, \( ) \) 2, \( \vee \) 1, \( r \) 1, \( ) \) 1, then 0 after the last symbol. The \( \vee \) is circled ("main connective, depth 1") and the \( \wedge \) marked "depth 2". Caption: "The depth profile of \( ((p \wedge q) \vee r) \). It starts at 0, stays at 1 or more strictly inside, comes back to 0 only after the last symbol, and the only binary connective at depth 1 is the main connective." Then: "For every formula of the form \( (\varphi \circ \psi) \) the lemma below says the same: (a) the count returns to 0, (b) it never goes below 0 and stays at 1 or more strictly inside, (c) every binary connective is at depth 1 or more. The remark after the proof adds that only the main connective is at depth exactly 1." (A negation such as \( \neg(p \to \neg q) \) starts with a symbol at depth 0 followed by a \( ( \) at depth 0, as drill (e) shows; the lemma's "at least 1" sentence is about formulas \( (\varphi \circ \psi) \) only.)
   - 02:251: its first sentence ("Our first structural induction proves the claim this section began with, together with two refinements …") is **cut**, since the sentence above now says what the lemma proves. Its second sentence, "We count parentheses in strings, and for this some words about strings.", is kept, right after the depth-profile paragraph and before 02:253.
   - 02:253-257 (initial segment, proper, excess, its additivity and the example) kept, with one sentence added after 02:257's example: "So the depth of a symbol is the excess of the initial segment that ends just before it." `lem-parenthesis-count` verbatim. "In words" 02:271 kept. The Idea 02:273-275 kept. The proof 02:277-301 and the strengthening remark 02:305 → fold F3.2-c, verbatim. 02:303 (the proof gives more: the main connective is the only binary connective at depth one) **stays on the main line**, reworded only in its first clause: "The proof (in the fold) gives a little more than (c) states, and the next proof uses the extra."
   - **Quick check (new):** "Write down the depth of each symbol of \( (p \wedge (q \vee r)) \). Which binary connective is at depth 1?" Solution: \( ( \) 0, \( p \) 1, \( \wedge \) 1, \( ( \) 1, \( q \) 2, \( \vee \) 2, \( r \) 2, \( ) \) 2, \( ) \) 1, and 0 after the last symbol. The \( \wedge \) is at depth 1, and it is the main connective. Compare the figure, whose main connective was the \( \vee \).
8. `## Unique readability`: 02:309 kept; `thm-unique-readability` verbatim; "In words" 02:324 kept; the Idea 02:326-328 kept. The proof 02:330-338 → fold F3.2-d, verbatim. 02:340 kept. 02:342: its bold first sentence and the sentence "We know it has one. That it has only one is proved by structural induction." stay on the main line, with one sentence: "The induction, in the fold below, uses unique readability at each compound formula." The rest of 02:342, up to "is a well-defined number.", → fold F3.2-d after the proof, verbatim except that its last clause ("and the height of @def-height is a well-defined number") is cut, because `def-height` now follows (S2a).
9. **Height, now well defined** (moved from 3.1): "From now on we speak of **the** parse tree of a formula." Then `def-height` **verbatim** (from 01:258-262), 01:264 kept (its references to `@exm-parse-trees` (b), (c) are backward), and the warning 01:280-282 kept. 01:266 is not carried. The recursive form follows in `exm-recursive-definitions`, and 02:418 already shows that the two heights agree.
10. `## Definition by recursion`: 02:346 kept. 02:348 → "We say **function on formulas** for a rule that assigns to each formula exactly one value; the values may be numbers, truth values, formulas, or collections of atoms. Nothing here needs more than this everyday sense of 'function'." (The pointer moves to the index.) The gloss 02:350, `thm-structural-recursion` verbatim, 02:371 and the Idea 02:373-375 kept. The proof 02:377-387 and 02:389 → fold F3.2-e, verbatim. `exm-recursive-definitions` (02:391-416) verbatim. 02:418-420 kept, except 02:418's opening "Two checks connect these definitions with Section 3.1." → "Two checks connect these definitions with the parse trees." (the tree height is now defined in this section, S2a item 4). Warning 02:422-424 kept.
11. **Looking ahead** (text above).

**Folds.** F3.2-a `title="Why induction is not a rule of logic"`: 02:46. F3.2-b `title="The proof of structural induction"`: 02:217-233, with the reworded remark. F3.2-c `title="The proof of the parenthesis count"`: 02:277-301 and 02:305. F3.2-d `title="The proof of unique readability"`: 02:330-338, then 02:342 from "An atom or \( \bot \) has only the one-node tree" to "the parse trees of \( \varphi \) and \( \psi \)." F3.2-e `title="The proof of structural recursion"`: 02:377-389.

**Cut outright:** the forward pointers of 02:13, 02:34, 02:42 (*Analysis on the Real Line*, *Sets, Relations, and Cardinality*, *Number Systems*), 02:64, 02:124 (last sentence) and 02:348. The ones about other volumes reappear in the index note.

**Quick checks:** strong induction (02:157, kept), the clause for ¬ (02:239, kept), \( 5^n - 1 \) (new), depth (new). That is four in about 4,900 words, plus the worked examples.

**Exercises.**
- **A1** (kept label): (a), (b) unchanged. (c)–(e) move to the new C4 (below). New parts:
  (c) "A reader proves 'every formula has at least one symbol that is not a parenthesis' by structural induction. They check atoms, the step for \( \neg \), and the step for \( (\varphi \circ \psi) \). Which case is missing? Does the claim hold there?" Answer: the case \( \bot \) is missing. The claim holds there, since \( \bot \) is itself such a symbol. The proof is incomplete, though the claim is true; compare the warning on "every formula contains an atom", where the missing case makes the claim false.
  (d) "Write down, without proving them, the base cases and the inductive steps of a structural induction for: every formula has exactly as many left parentheses as binary connectives." Answer: base cases: an atom and \( \bot \) have none of either. Step for \( \neg \): if \( \varphi \) has as many of each, so has \( \neg\varphi \), which adds neither. Step for \( (\varphi \circ \psi) \): if each of \( \varphi, \psi \) has as many of each, the whole adds one left parenthesis and one binary connective.
- **A2: Drill** (new):
  (a) In the inductive step of @exm-power-inequality, where is the induction hypothesis used? — In \( 3 \cdot 3^n \ge 3(2n + 1) \).
  (b) Write down the base case and the step for "\( n^2 + n \) is even for every \( n \in \nN \)". — Base: \( 0 \) is even. Step: if \( n^2 + n \) is even, then so is \( (n + 1)^2 + (n + 1) = (n^2 + n) + 2(n + 1) \).
  (c) Ordinary or strong induction for "every \( n \ge 2 \) is a product of one or more primes"? — Strong: a composite \( n = ab \) with \( 1 < a, b < n \) reaches back to \( a \) and \( b \), not to \( n - 1 \).
  (d) Which kind of induction proves "every formula has as many left as right parentheses"? — Structural induction, or strong induction on the position in a formation sequence, which is how structural induction is proved.
  (e) Write down the depth of each symbol of \( \neg(p \to \neg q) \). Which binary connective is at depth 1? — \( \neg \) 0, \( ( \) 0, \( p \) 1, \( \to \) 1, \( \neg \) 1, \( q \) 1, \( ) \) 1, and 0 after. The \( \to \) is at depth 1: it is the main connective of the part inside the parentheses. The main connective of the whole formula is the first \( \neg \).
  (f) Height of \( ((p \wedge q) \vee \neg\neg r) \)? — \( 1 + \max\{2, 3\} = 4 \).
  (g) True or false: every subformula of \( \varphi \) other than \( \varphi \) itself has smaller height than \( \varphi \). (Old 3.1 A1(c).) — True. The answer is 01:425 verbatim.
  (h) Is "\( f(\varphi) \coloneqq f(\varphi) + 1 \) for every formula \( \varphi \)" a definition by recursion? — No. It gives no value at atoms or \( \bot \), and it defines the value at \( \varphi \) from the value at \( \varphi \) itself, not from the immediate parts. No function obeys it, since no number equals itself plus one.
- **B1** frozen; **B2**, **B3** kept.
- **C1**, **C2** kept; **C3** (exit check) kept.
- **C4** (new label `exr-induction-c4`), `[C4: Challenge: Inside the folded proofs]`: old A1 (c), (d), (e) with their answers (02:436-438, 02:451-455), verbatim. Lead line: "*These parts are about the proofs in the second-reading folds of this section; read the folds first.*"

**Dependency ledger (in-file).** 02 gains 01:539's `def-height` line (§4.1) and 03:564's line for the two readings of \( p \wedge q \vee r \) (values T and F at \( p = q = \mathrm{F} \), \( r = \mathrm{T} \)), now the hook's claim; 03:564 is replaced in 03 by "recalled from F1.3 §02 (hook)".

**Sidecars:** the hook's two values (moved from `def-truth-table.py`'s check of 03:115-119, or re-checked there with a §02 tag); the \( 5^n - 1 \) step identity; the depth profiles of \( ((p \wedge q) \vee r) \), \( (p \wedge (q \vee r)) \) and \( \neg(p \to \neg q) \) (extend `lem-parenthesis-count.py`); drill (b) identity, (f) height.

### 4.3 Section 3.3: Valuations and Truth Tables (`03-valuations-and-truth-tables.md`, edited)

**Budget:** main line ≤ 3,400 words (now 3,555); folds ≤ 300. Looking ahead (`[Looking ahead]` title line, §1 item 3): "Chapter 4 looks inside atoms." This is the last sentence of the warning 03:313-315, moved out of the warning into the box. fd1 ch04 01:25 needs a matching edit (§6).

**Changes, in the file's order.**
1. 03:3-5 kept.
2. `## Reading a table off the rules` 03:7-45 kept. 03:45's "and Exercise C1 below asks for a sharper version of the argument for \( \to \)" → "and Exercise C3 of Section 3.4 asks for a sharper version of the argument for \( \to \)" (the exercise moves, item 9).
3. `## Valuations`: `def-valuation` verbatim; 03:59 kept. After 03:59, one new sentence: "We let a valuation decide **every** atom so that one valuation gives a value to every formula at once. In practice only the few atoms a formula contains matter, and the Coincidence Lemma below says so." The bullets 03:63-64 kept. Bullet 03:65 (odd/even atoms) cut. Nonexample 03:67 → fold F3.3-a.
4. `## The value of a formula`: 03:71-113 kept (`def-truth-value` verbatim, the tables, 03:111, 03:113). 03:115 "**Well defined.**" kept to "This is what Section 3.2 was for."; then one sentence replaces the rest of 03:115-119: "Section 3.2 showed the danger with the string \( p \wedge q \vee r \), whose two readings take different values when \( p \) and \( q \) are false and \( r \) is true. A formula of @def-formula carries its parentheses, and has one value." `exm-value-down-the-tree` kept. Nonexample 03:144 → fold F3.3-a. Warning 03:146-148 kept. Quick check 03:150-156 kept. **Quick check (new, after it):** "Let \( v(p) = \mathrm{T} \) and \( v(q) = \mathrm{F} \). What is \( v(\neg p \vee (q \leftrightarrow \bot)) \)?" Solution: \( \mathrm{T} \). \( \neg p \) is F by (V2). \( q \leftrightarrow \bot \) is T by (V6), since both sides are F (\( \bot \) by (V1)). So the disjunction is T by (V4).
5. `## Only the atoms of a formula matter`: 03:160-162 kept; `lem-coincidence` statement and Idea verbatim. **Proof:** 03:175-183 (the property, atoms, ⊥, negation, conjunction) verbatim. Then, replacing 03:185-189 on the main line:
   "*Disjunction, implication, biconditional.* Assume \( C(\varphi) \) and \( C(\psi) \), and let \( v \), \( w \) agree on the atoms of \( \varphi \circ \psi \). As in the conjunction case, \( v(\varphi) = w(\varphi) \) and \( v(\psi) = w(\psi) \). One clause of @def-truth-value then turns these equal inputs into equal outputs:"

   | \( \circ \) | Clause | Why \( v(\varphi \circ \psi) = w(\varphi \circ \psi) \) |
   |---|---|---|
   | \( \vee \) | (V4) | T exactly when one of the two parts is T, and the parts have the same values under \( v \) and under \( w \) |
   | \( \to \) | (V5) | F exactly when the first part is T and the second F, and the parts have the same values under \( v \) and under \( w \) |
   | \( \leftrightarrow \) | (V6) | T exactly when the two parts have equal values, and the parts have the same values under \( v \) and under \( w \) |

   Then 03:191 (the closing sentence of the proof) verbatim. After the proof, fold F3.3-b with 03:185-189 verbatim. 03:194 → "The table's three cases are the conjunction case again, with another clause. The fold writes each one out in words." 03:196 kept. Quick check 03:198-204 kept. (This is still the faded triple's fully worked member: every case is proved on the main line.)
6. `## Truth tables`: 03:208-311 kept (`def-truth-table` verbatim, 03:218-222, the three examples, 03:271, 03:311).
7. Warning 03:313-315 kept, without its last sentence, which becomes the Looking-ahead box. Quick check 03:317-323 kept.
8. **Looking ahead** (text above), as the last main-line block.
9. **Exercises.** A1, B1, B2, B3 kept. C2 frozen, kept. Old C1 → 3.4 C3 (§4.4).
   - **A2: Drill** (new):
     (a) \( v(p) = \mathrm{T} \), \( v(q) = \mathrm{F} \): \( v(p \to q) \)? — F.
     (b) Same \( v \): \( v(\neg p \to q) \)? — T: the hypothesis \( \neg p \) is F.
     (c) Same \( v \): \( v(\bot \leftrightarrow q) \)? — T: both sides F.
     (d) How many rows has a table on \( p, q, r, s, t \)? — \( 2^5 = 32 \).
     (e) Give a row making \( (p \vee q) \to (p \wedge q) \) false. — \( p = \mathrm{T} \), \( q = \mathrm{F} \) (or \( p = \mathrm{F} \), \( q = \mathrm{T} \)).
     (f) Is there a row making \( p \to \neg p \) true? — Yes, \( p = \mathrm{F} \).
     (g) Work backwards from F: in which rows is \( p \to (q \to r) \) false? — Only \( p = q = \mathrm{T} \), \( r = \mathrm{F} \).
     (h) Valuations \( v, w \) agree on \( p \) and differ on \( q \). Must \( v((p \to p) \vee q) = w((p \to p) \vee q) \)? — Yes, both are T, since \( p \to p \) is T under every valuation. But @lem-coincidence does not say so, because \( v \) and \( w \) differ on the atom \( q \). The lemma gives a sufficient condition, not a necessary one.
   - **C1** (label `exr-valuations-and-truth-tables-c1`, new item), `[C1: A formula built from biconditionals]`: "Call a formula **\( \leftrightarrow \)-built** if it is built from atoms by \( \leftrightarrow \) alone. For a valuation \( v \) and a formula \( \varphi \), let \( f_v(\varphi) \) be the number of occurrences of atoms in \( \varphi \) that are false under \( v \), counted with repetition. (a) Prove by structural induction that every \( \leftrightarrow \)-built \( \varphi \) is true under \( v \) exactly when \( f_v(\varphi) \) is even. (b) Deduce that \( (p \leftrightarrow q) \leftrightarrow p \) has the same value as \( q \) under every valuation." Hint 1: "Put 'if \( \varphi \) is \( \leftrightarrow \)-built' inside the property, as in Exercise B2." Hint 2: "In the step, \( f_v(\varphi \leftrightarrow \psi) = f_v(\varphi) + f_v(\psi) \); when is a sum of two numbers even?" Solution: the property is "if \( \varphi \) is \( \leftrightarrow \)-built, then for every valuation \( v \): \( v(\varphi) = \mathrm{T} \) iff \( f_v(\varphi) \) is even". ⊥, \( \neg \) and the other binary connectives are vacuous, since such formulas are not \( \leftrightarrow \)-built. *Atom:* if \( v(p) = \mathrm{T} \), then \( f_v(p) = 0 \), which is even; if \( v(p) = \mathrm{F} \), then \( f_v(p) = 1 \), which is odd. *Step:* the parts of a \( \leftrightarrow \)-built \( \varphi \leftrightarrow \psi \) are \( \leftrightarrow \)-built. By (V6), \( v(\varphi \leftrightarrow \psi) = \mathrm{T} \) iff \( v(\varphi) = v(\psi) \), iff \( f_v(\varphi) \) and \( f_v(\psi) \) are both even or both odd (by the hypotheses), iff their sum \( f_v(\varphi \leftrightarrow \psi) \) is even. (b) \( p \) occurs twice and \( q \) once, so \( f_v \) counts 2 if \( p \) is false (0 otherwise) plus 1 if \( q \) is false (0 otherwise), which is even exactly when \( q \) is true. So the formula is true exactly when \( q \) is. Marking scheme (10): 2 property stated for every formula, with the restriction inside and "for every \( v \)"; 1 vacuous cases named; 2 atom case, both values; 4 step, with (V6) and the parity of a sum; 1 (b). Fatal errors: a step that uses the hypothesis for one part only; fixing \( v \) outside the property and then using another valuation.

**Folds.** F3.3-a `title="Edge cases"`: 03:67 and 03:144, verbatim. F3.3-b `title="The three remaining cases, written out"`: 03:185-189 verbatim.

**Cut outright:** 03:65; the computation 03:115 ("The string …")–03:119, now in 3.2's hook.

**Quick checks:** 03:150, 03:198, 03:317 (kept), \( \neg p \vee (q \leftrightarrow \bot) \) (new). That is four in about 3,400 words.

**Sidecars:** new Quick check; drill (a)–(h) (extend `def-truth-table.py`); the C1 parity claim, checked on random \( \leftrightarrow \)-built formulas over four atoms, and (b) on its four rows (new `exr-valuations-and-truth-tables-c1.py`).

### 4.4 Section 3.4: Tautologies, Entailment and Equivalence (`04-entailment-and-equivalence.md`, edited)

**Budget:** main line ≤ 4,500 words (now 4,299, with ~460 new words and ~305 folded); folds ≤ 400. No Looking-ahead box.

**Changes, in the file's order.**
1. 04:3-22 kept. Bullet 04:23 (atom-free formulas) → fold F3.4-a. Bullet 04:24 and 04:26-46 kept.
2. `## Semantic entailment`: 04:50-84 kept. **Quick check (new, after 04:84):** "Does \( p \wedge q \models p \vee r \) hold? Does \( p \vee r \models p \wedge q \)?" Solution: The first holds: a row making \( p \wedge q \) true makes \( p \) true, so \( p \vee r \) is true. The second fails, for instance at \( p = \mathrm{F} \), \( r = \mathrm{T} \) (any \( q \)), which makes \( p \vee r \) true and \( p \wedge q \) false.
3. Examples 04:86-126 kept. Warning 04:128-130: "(Exercise B3 shows …)" → "(Exercise B3 below asks you to prove that \( \varphi \models \psi \) holds exactly when \( \varphi \to \psi \) is a tautology)", so that nothing in the warning rests on the exercise. Quick check 04:132-138 kept.
4. `## Semantic equivalence` 04:142-263 kept (`prp-standard-equivalences` with its proof; 04:242; the long conjunctions 04:244-255, which fd1 ch04 05:17 and 07:635 cite; Quick check 04:257).
5. **New box before `## Replacing a part by an equivalent part`** (`::: {.remark}`, first words `**Three ways to change a formula.**`, ~170 words with the table). Lead: "The chapter has three operations that put one thing in place of another. Their names are close, and what each one keeps is different."

   | Operation | What is put in | Where | What it keeps | Example |
   |---|---|---|---|---|
   | replace a part | one occurrence of a subformula, by a formula equivalent to it | the next subsection | the truth table of the whole formula | \( \neg\neg r \) by \( r \) inside \( p \to (q \vee \neg\neg r) \) |
   | substitute for atoms | formulas for chosen atoms, at **every** occurrence, all at once | the last subsection | tautologies stay tautologies, valid arguments stay valid | \( q \wedge r \) for \( p \) turns \( p \vee \neg p \) into \( (q \wedge r) \vee \neg(q \wedge r) \) |
   | substitute in a derivation | formulas for the letters of a derivation, at every occurrence | Section 3.1, last subsection | being a derivation | \( p_1 \wedge p_2 \) for \( P \) in the derivation of @prp-implication-transitive |

   **Quick check (new):** "Which of the three operations turns \( p \vee \neg p \) into \( (q \to r) \vee \neg(q \to r) \), and what does it keep?" Solution: substitution of \( q \to r \) for the atom \( p \), at both occurrences. It keeps tautologies, so the new formula is a tautology too. It is not a replacement of a part: \( q \to r \) is not equivalent to \( p \).
6. `## Replacing a part by an equivalent part`: 04:267-269 kept; `lem-replacement` statement and Idea verbatim. One sentence after the Idea: "The proof, by structural induction with exactly that case split, is in the fold below." The proof 04:281-293 → fold F3.4-b verbatim. 04:295-303 (the chain of three equivalences) and warning 04:305-307 kept.
7. `## Substituting formulas for atoms`: 04:311-324 kept. Then **`exm-substitution-in-one-row`** (new, ~200 words), placed before `lem-substitution`:
   `[One row, two valuations]` "Let \( \sigma \) put \( q \wedge r \) for \( p \) and \( p \) for \( q \), as above, and let \( v(p) = \mathrm{F} \), \( v(q) = \mathrm{T} \), \( v(r) = \mathrm{T} \). Compute \( v(\sigma(\chi)) \) for \( \chi = (p \to q) \vee \neg p \). Then define \( w \) by \( w(s) \coloneqq v(\sigma(s)) \) for every atom \( s \), and compute \( w(\chi) \)." Solution: \( \sigma(\chi) = ((q \wedge r) \to p) \vee \neg(q \wedge r) \). Under \( v \): \( q \wedge r \) is T and \( p \) is F, so \( (q \wedge r) \to p \) is F; \( \neg(q \wedge r) \) is F; so \( v(\sigma(\chi)) = \mathrm{F} \). Next, \( w(p) = v(q \wedge r) = \mathrm{T} \), \( w(q) = v(p) = \mathrm{F} \), and \( w(r) = v(r) = \mathrm{T} \). Under \( w \): \( p \to q \) is F and \( \neg p \) is F, so \( w(\chi) = \mathrm{F} \). The two values agree. "The formula \( \sigma(\chi) \) under \( v \) behaves exactly as \( \chi \) does under \( w \). The lemma below says this happens for every formula and every valuation, and draws the consequences."
   `lem-substitution` statement, Idea, proof verbatim. 04:357, warning 04:359-361 kept.
8. `## Two questions, side by side` 04:365-377 kept (the index shows the table too).

**Folds.** F3.4-a `title="Formulas with no atoms"`: 04:23. F3.4-b `title="The proof of the replacement lemma"`: 04:281-293.

**Quick checks:** 04:132, 04:257 (kept), \( \models \) in two directions (new), three operations (new). That is four in about 4,500 words.

**Exercises.** A1, B1, B2, B3, C1, C2 kept.
- **A2: Drill** (new):
  (a) Tautology, contradiction, or neither: \( (p \to q) \vee p \)? — A tautology. If \( p \) is F, the left disjunct is T; if \( p \) is T, the right one is.
  (b) The same for \( (p \vee q) \wedge \neg p \wedge \neg q \). — A contradiction.
  (c) Is the list \( p \vee q, \ \neg p, \ \neg q \) satisfiable? — No.
  (d) Does \( p \to q \models \neg p \vee q \)? — Yes. The two are equivalent, by @prp-standard-equivalences (c).
  (e) Give a refuting row for \( p \vee q \models p \wedge q \). — \( p = \mathrm{T} \), \( q = \mathrm{F} \).
  (f) Does \( \bot \models p \)? — Yes: no row makes \( \bot \) true.
  (g) Does \( p \models q \to p \)? — Yes: in every row with \( p \) true, \( q \to p \) has a true conclusion.
  (h) Is \( \neg(p \to q) \equiv p \wedge \neg q \)? — Yes: both are T in the row TF only.
- **C3** (new label `exr-entailment-and-equivalence-c3`; the old 3.3 C1 moved here), `[C3: The rows of implication are forced]`. The statement and solution are 03:478-524 verbatim, with one change, the restatement of (I) in the language of this section (S2a): "(I) For every list of formulas \( \Gamma \) and all formulas \( \varphi, \psi \): if \( \Gamma, \varphi \models \psi \), then \( \Gamma \models \varphi \to \psi \), where \( \models \) is read with the table \( t \) for \( \to \)." In the solution, 03:510's "Its hypothesis, 'every valuation making \( p \) true makes \( p \) true', holds" → "Its hypothesis \( p \models p \) holds", and 03:512's "Every valuation making \( q \) and \( p \) true makes \( q \) true, so every valuation making \( q \) true makes \( p \to q \) true" → "\( q, p \models q \) holds, so \( q \models p \to q \)". 03:514's last sentence ("Conditions (E) and (I) are what Section 3.5 proves …") is kept. The marking scheme is kept.

**Sidecars:** new Quick checks; `exm-substitution-in-one-row` (both values, and \( w \)); drills (extend `exr-entailment-and-equivalence-a1.py`); C3 (moved script).

### 4.5 Section 3.5: Soundness (`05-soundness.md`, edited)

**Budget:** main line ≤ 3,800 words (now 4,963); folds ≤ 550; the optional excursion after the exercises ≤ 1,000 (counted in the full track only). Looking ahead (`[Looking ahead]` title line, §1 item 3): "Chapter 5 says what reductio asserts that the other rules do not, and who objected to it." (This is the clause cut from 05:356; STATUS row 80 keeps its payer, F1.5.)

**Changes, in the file's order.**
1. 05:3-61 kept on the main line: the opening, the failed first attempt (the novice report's model passage), derivations of formulas, and the context with its table and 05:57-61. **Quick check (new, after the context table 05:49-55):** "In that derivation, which lines have \( p \) in their context?" Solution: lines 3, 4 and 5, the lines of the box opened by \( p \).
2. 05:63 kept. `lem-context-inclusion` statement verbatim. Then **a picture for (b)** (new, TikZ, ~40 words of caption): a Fitch-style drawing. The outer bar is labelled "premises and the boxes around line \( k \)". Inside it, a box opens at line \( a \) with \( \varphi_a \) above a short horizontal rule, a dotted gap, and its last line \( b \) holding \( \varphi_b \). Below the box, outside it, line \( k \) holds \( \varphi_k \), with an arrow from line \( k \) to the whole box (the citation). On the right, two braces: at line \( k \), "context \( \Gamma_k \)"; at line \( b \), "context \( \Gamma_k, \varphi_a \)". Caption: "Part (b): the last line of a cited box depends on everything line \( k \) depends on, and on the box's own assumption." The Idea 05:76-78 kept. One sentence: "The proof reads both parts off the scope rule; it is in the fold below." The proof 05:80-88 → fold F3.5-a verbatim. 05:90 (both parts checked on the contrapositive derivation) kept on the main line. Warning 05:92-110 → fold F3.5-b verbatim (the main line keeps the warnings 05:292 and 05:296). Quick check 05:112-118 kept.
3. `## The soundness theorem`: 05:122-220 kept verbatim (the statement, Try it first, the Idea with its Step roadmap and prompt, the proof, 05:220). This is a key proof, with an exit check and A1 comprehension parts, so it stays on the main line (§1 item 2). 05:222 → fold F3.5-c. `exm-soundness-run` kept.
4. `## Refuting with one row`: 05:264-306 kept (`cor-refuting-row`, 05:276, Chapter 2's question, affirming the consequent, the Chapter 2 stall, both warnings, Quick check 05:300). **Quick check (new, after 05:276):** "Does the row \( p = q = \mathrm{T} \) refute \( p \to q \vdash q \)? Does the row \( p = q = \mathrm{F} \)?" Solution: the first does not, since its conclusion \( q \) is true. The second does: \( p \to q \) is T and \( q \) is F. So \( p \to q \nvdash q \), by @cor-refuting-row.
5. **Looking ahead** (text above), the last main-line block.
6. `## Exercises` (below).
7. **`## Optional excursion: reductio says something new`** (moved from 05:308-357; a `##` heading **after** the exercise groups, before the dependency ledger). Its first block is new, an italic line: "*Optional: nothing later depends on this excursion. It answers a question Chapter 2 raised.*" It then **leads with the tables**: 05:312's first two sentences (the three values and their reading), then the new display

   \[
   \begin{array}{c|ccc}
   u(\varphi \to \psi) & u(\psi) = 0 & u(\psi) = \tfrac12 & u(\psi) = 1 \\
   \hline
   u(\varphi) = 0 & 1 & 1 & 1 \\
   u(\varphi) = \tfrac12 & 0 & 1 & 1 \\
   u(\varphi) = 1 & 0 & \tfrac12 & 1
   \end{array}
   \qquad
   \begin{array}{c|c}
   u(\varphi) & u(\neg\varphi) \\
   \hline
   0 & 1 \\
   \tfrac12 & 0 \\
   1 & 0
   \end{array}
   \]

   with one sentence: "An implication gets 1 when its conclusion is at least as true as its hypothesis, and otherwise the value of its conclusion; a negation is 1 only on 0." Then 05:310 (its last sentence, "This result is optional: …", is now said by the italic line, so it is cut), the rest of 05:312, the definitions 05:313-321, `thm-raa-independent` (still `.optional`) with its Idea and proof verbatim, 05:353, and the remark 05:355-357 without its last clause ("and Chapter 5 says what it is and who objected to it"), which is now the Looking-ahead box. Then 05:356 ends "\( \rulename{RAA} \) says something the other rules cannot."
   *Recorded deviation from STYLE §2's skeleton (a `##` after the Exercises).* The plan asks for the excursion "after the exercises as a boxed optional excursion". If `check_structure.py` or the build objects to a `##` heading after the exercise groups, the drafter puts the excursion at the end of the main line instead. It then goes inside a fold `title="Optional excursion: reductio says something new"`, with a bold lead-in in place of the heading (a fold may hold an optional result, STYLE §12.0). The Looking-ahead box stays the last block before the Exercises. Either way the content is the same.

**Folds.** F3.5-a `title="The proof: reading the scope rule"`: 05:80-88. F3.5-b `title="A box that ends inside another"`: 05:92-110. F3.5-c `title="Why induction on the position of a line"`: 05:222.

**Quick checks:** 05:112, 05:300 (kept), contexts (new), refuting rows (new). That is four in about 3,800 words.

**Exercises.** A1 (key-proof comprehension), B1, B2 (proof ordering), C1, C2 (exit check) kept.
- **A2: Drill** (new):
  (a) Give a refuting row for \( p \vee q \vdash p \). — \( p = \mathrm{F} \), \( q = \mathrm{T} \).
  (b) Give one for \( p \to q, \ \neg p \vdash \neg q \). — \( p = \mathrm{F} \), \( q = \mathrm{T} \).
  (c) Does \( p = \mathrm{T} \), \( q = \mathrm{F} \) refute \( p \wedge q \vdash q \)? — No: it makes the premise false.
  (d) Is there a refuting row for \( p, \ p \to q \vdash q \)? — No. The only row making both premises true has \( q \) true. (The sequent is derivable, by one line of \( \rulename{{\to}E} \).)
  (e) Refute \( \vdash p \vee q \). — \( p = q = \mathrm{F} \). With no premises, every row qualifies.
  (f) Refute \( p \to (q \vee r) \vdash p \to q \). — \( p = \mathrm{T} \), \( q = \mathrm{F} \), \( r = \mathrm{T} \).
  (g) Line 5 of a derivation lies in the boxes opened at lines 2 and 4, and line 1 is the only premise. What is \( \Gamma_5 \)? — \( \varphi_1, \varphi_2, \varphi_4 \).
  (h) Line \( k \) is justified by \( \rulename{\neg I} \) citing the box 3–6. What is \( \Gamma_6 \), in terms of \( \Gamma_k \)? — \( \Gamma_k, \varphi_3 \), by @lem-context-inclusion (b).

**Sidecars:** new Quick checks and drills (extend `cor-refuting-row.py`); the 3×3 and 3×1 tables (extend `thm-raa-independent.py`).

### 4.6 Section 3.6: Completeness (`06-completeness.md`, edited)

**Budget:** main line ≤ 4,700 words (now 5,324, with ~1,170 folded and ~500 new words); folds ≤ 1,400. No Looking-ahead box.

**New order of material.**
1. 06:3-22 kept (the opening, the question, the target sequent, the two-idea plan). 06:24: keep "We keep the premises \( \Gamma \) throughout, and we isolate the two ingredients as lemmas so that each can be checked on its own. Before either, we need a little bookkeeping about derivations." Its first sentence (Kalmár's lemma, "the route is the classical one") → fold F3.6-a. The text still does not call the route new (S2 recheck #2 of `ch03.md`).
2. `## Bookkeeping: adding premises and chaining derivations`: 06:28 kept; `lem-weakening-cut` verbatim; "In words" 06:42 and the Idea 06:44-46 kept. Then **one concrete paste** (new, ~150 words, with three short `nd` blocks):
   "Here is (b) once, with \( \Gamma \) the list \( p \wedge q \), \( \varphi = q \) and \( \psi = q \vee r \). A derivation \( D \) of \( q \) from \( p \wedge q \), and a derivation \( E \) of \( q \vee r \) from the premise \( q \):"
   - \( D \): 1 \( p \wedge q \) (premise); 2 \( q \), \( \rulename{\wedge E} \) 1.
   - \( E \): 1 \( q \) (premise); 2 \( q \vee r \), \( \rulename{\vee I} \) 1.
   "Write \( D \), then the lines of \( E \) that are not premises, and let the line of \( E \) that cited its premise \( q \) cite the last line of \( D \) instead:"
   - \( F \): 1 \( p \wedge q \) (premise); 2 \( q \), \( \rulename{\wedge E} \) 1; 3 \( q \vee r \), \( \rulename{\vee I} \) 2.
   "\( F \) is a derivation of \( q \vee r \) from \( p \wedge q \) alone: so \( p \wedge q \vdash q \vee r \). The proof in the fold below checks that the same pasting works for any two derivations, boxes included."
   The proof 06:48-66 and 06:68 → fold F3.6-b verbatim. Quick check 06:70-76 kept.
3. `## The rules prove their own truth tables`: 06:80 kept; `lem-connective-rows` statement **verbatim** (its fifteen tags are its content). Then **the tables with tagged rows** (new; replaces on the main line the 15-row proof table, which moves to the fold). Lead sentence: "Here are the tables of @def-truth-value again, with each row tagged by the sequent of the lemma that derives it from the signed parts. Where two sequents fit a row, the tag is the one the proof of the next lemma uses."

   | \( \alpha \) | \( \beta \) | \( \alpha \wedge \beta \) | \( \alpha \vee \beta \) | \( \alpha \to \beta \) | \( \alpha \leftrightarrow \beta \) |
   |---|---|---|---|---|---|
   | T | T | T \( (\wedge 1) \) | T \( (\vee 1) \) | T \( ({\to}2) \) | T \( ({\leftrightarrow}1) \) |
   | T | F | F \( (\wedge 3) \) | T \( (\vee 1) \) | F \( ({\to}3) \) | F \( ({\leftrightarrow}3) \) |
   | F | T | F \( (\wedge 2) \) | T \( (\vee 2) \) | T \( ({\to}1) \) | F \( ({\leftrightarrow}4) \) |
   | F | F | F \( (\wedge 2) \) | F \( (\vee 3) \) | T \( ({\to}1) \) | T \( ({\leftrightarrow}2) \) |

   and, beside it: \( \alpha \) T gives \( \neg\alpha \) F: \( (\neg 1) \); \( \alpha \) F gives \( \neg\alpha \) T: no sequent needed, since the signed part \( \neg\alpha \) is already the signed whole (06:229); \( \bot \) is always F: \( (\bot 1) \). Then 06:96 ("Each sequent has as premises only the parts it needs …") kept, the Idea 06:98-100 kept, and one sentence: "The derivations, with a check that none uses \( \rulename{RAA} \), are in the fold below." The proof 06:102-227 (the table, 06:123, the seven printed derivations, 06:226) → fold F3.6-c verbatim. 06:229 and warning 06:231-233 kept.
   **Quick check (new):** "Which tagged sequent covers \( \alpha \) F, \( \beta \) T for \( \to \)? And for \( \leftrightarrow \)?" Solution: \( ({\to}1) \), \( \neg\alpha \vdash \alpha \to \beta \). (The row also fits \( ({\to}2) \).) For \( \leftrightarrow \): \( ({\leftrightarrow}4) \), \( \neg\alpha, \beta \vdash \neg(\alpha \leftrightarrow \beta) \).
4. `## One row, one derivation`: opens with **the signed-row picture** (new, ~60 words): "A row of a truth table can be written as a list of premises: each atom as it stands in the row, itself if true, negated if false." Display (Markdown table):

   | \( p \) | \( q \) | \( r \) | the row, as premises |
   |---|---|---|---|
   | T | F | T | \( p, \ \neg q, \ r \) |

   Then 06:237-249 (gloss, the definition of \( \varphi^{v} \), the example), with one sentence added after the display: "The superscript \( v \) is a label naming the row, not an exponent." 06:251, `lem-truth-table-line` (key proof) with its Idea and proof verbatim, 06:301, `exm-truth-table-line-run`, Quick check 06:331-337 kept.
5. `## Gluing the rows: splitting on an atom`: 06:341-390 kept verbatim (`lem-atom-splitting` with its Idea, prompt and proof, the schema, 06:390).
6. `## The completeness theorem`, **reordered**: 06:394, `thm-completeness`, 06:402 and the Idea 06:404-406 kept. In the Idea, ③ is reworded: "③ Remove the signed atoms one at a time, the last first, by @lem-atom-splitting: an induction on the number of atoms removed." Its remaining sentences are kept. **Then the worked run, before the proof:** 06:454 and `exm-completeness-run` **move here**. Since the proof has not yet been read, 06:454 becomes "Let us run the method of the roadmap on the tautology of the opening.", and the example's statement "Run the proof of @thm-completeness on …" becomes "Run the roadmap of @thm-completeness on …" (S2a item 3). In its solution, "Step 2 is always Case 1" → "the Claim ② always falls in its first case (the row makes the premises, here none, true)", and "Step 3 first splits on \( q = p_2 \)" → "③ first splits on \( q = p_2 \)" (S2a). Before the 20-line derivation, add **a case-split tree** (new, TikZ). The root is "\( \vdash \chi \): line 20, \( \rulename{\vee E} \) on line 1"; two edges, labelled \( p \) and \( \neg p \), go to "box 2–10" and "box 11–19"; each of those has two edges, labelled \( q \) and \( \neg q \), to the leaves "box 4–6: \( ({\to}2) \), \( \rulename{\vee I} \)", "box 7–9: \( ({\to}1) \), \( \rulename{\vee I} \)", "box 13–15: \( ({\to}1) \), \( \rulename{\vee I} \)", "box 16–18: \( ({\to}1) \), \( \rulename{\vee I} \)". Caption: "Each leaf is one row of the table; each inner node is one use of @lem-atom-splitting." 06:510 kept after the derivation. **Quick check (new, after 06:510):** "In the tree, which two leaves do the same thing, and why?" Solution: the boxes 13–15 and 16–18. Both write \( p \to q \) by \( ({\to}1) \) from \( \neg p \) on line 11, because in a row with \( p \) false, \( p \to q \) is true whatever \( q \) is.
   **Then the proof**, verbatim except 06:445. Step 1, Step 2 with its Claim, Step 3 with its Claim, and Step 4 are kept. 06:445 is replaced on the main line by: "Step 2 is \( S(n) \). Applying the Claim with \( j = n \), then \( j = n - 1 \), and so on down to \( j = 1 \), removes the signed atoms one at a time and reaches \( S(0) \). This descent is an induction on the number of atoms removed; the fold after the proof writes it out." (S2a.) 06:445 itself goes verbatim into fold F3.6-d, placed directly after the proof. 06:450 and 06:452 kept.
7. Warning 06:513-515, `cor-derivable-iff-valid` with its proof, and 06:533 kept. Remark 06:535-537 (compactness) → fold F3.6-e.
8. `## Two roads to every answer` 06:539-566 kept.

**Folds.** F3.6-a `title="Where the route comes from"`: the first sentence of 06:24. F3.6-b `title="The proof: pasting derivations"`: 06:48-68. F3.6-c `title="The fifteen derivations"`: 06:102-227. F3.6-d `title="The descent, as an induction"`: 06:445. F3.6-e `title="Infinitely many premises"`: 06:535-537.

**Quick checks:** 06:70, 06:331 (kept), tagged rows (new), the tree (new). That is four in about 4,700 words.

**Exercises.** A1 (key proofs), B1, B3, C1 (frozen), C2 (exit check) kept.
- **B2**: the solution gains a case-split tree before the 21-line derivation (new, TikZ, as in item 6). Root: "line 21, \( \rulename{\vee E} \) on line 3"; edges \( p \) / \( \neg p \) to "box 4–11 (\( \rulename{\vee E} \) at 11 on line 5)" and "box 12–20 (\( \rulename{\vee E} \) at 20 on line 13)". Leaves: "box 6–6: the goal is the assumption", "box 7–10: \( ({\to}3) \), clash with line 2, \( \rulename{\bot E} \)", "box 14–16: clash of lines 1 and 12, \( \rulename{\bot E} \)", "box 17–19: the same clash".
- **A2: Drill** (new):
  (a) \( v(p) = \mathrm{F} \), \( v(q) = \mathrm{T} \). Write \( p^{v} \), \( q^{v} \), \( (p \to q)^{v} \), \( (q \to p)^{v} \). — \( \neg p \), \( q \), \( p \to q \), \( \neg(q \to p) \).
  (b) \( \varphi = \neg p \wedge q \), \( v(p) = v(q) = \mathrm{T} \). Which sequent does @lem-truth-table-line give? — \( p, q \vdash \neg(\neg p \wedge q) \).
  (c) In (b), which tagged sequent does the proof use at the root, and where does its premise come from? — \( (\wedge 2) \) with \( \alpha = \neg p \): \( \neg\neg p \vdash \neg(\neg p \wedge q) \). The premise \( \neg\neg p \) comes from \( p \) by \( (\neg 1) \).
  (d) A sequent has three atoms. How many row derivations and how many uses of @lem-atom-splitting does the method build? — \( 8 \) and \( 7 \).
  (e) In the step from \( S(j) \) to \( S(j - 1) \), which signed atom disappears? — \( p_j^{v} \).
  (f) \( \Gamma = q \), \( \psi = p \vee q \), \( v(p) = v(q) = \mathrm{F} \). Which case of the Claim of Step 2 applies? — Case 2, with \( \gamma = q \), which \( v \) makes false.
- **C3** (`exr-completeness-c3`, renamed from `exr-normal-forms-c3`), `[C3: Exit check: deciding sequents]`. Statement, solution and marking scheme unchanged (07:507-580). It moves here because it tests this section and 3.5, and 3.7 is now second pass (§4.0 item 6). 3.6 now has two exit checks, C2 and C3.

**Sidecars:** the paste (`check_fitch` on \( D \), \( E \), \( F \)); the tag table against the case choices of `lem-truth-table-line`'s proof (extend `lem-connective-rows.py`); both trees' line ranges against the two printed derivations (`exm-completeness-run.py`, `exr-completeness-b2.py`); drills (a)–(f).

### 4.7 Section 3.7: Normal Forms and Adequate Connectives (`07-normal-forms.md`, edited, second pass)

**Budget:** main line ≤ 4,450 words (now 4,288, with ~160 folded and ~300 new: the \( t_1 \) passage, the table, the italic line, 07:33's parenthetical, and the longer "conjunctive clause"); folds ≤ 300. No Looking-ahead box.

**Changes, in the file's order.**
1. 07:3 kept; one italic sentence added after it: "*On a first reading this section may wait: nothing in Chapters 4 and 5 uses it.*"
2. **"Conjunct" → "conjunctive clause" (and "minterm" for \( C_v \)).** 07:33 → "A **conjunctive clause** joins one or more literals by \( \wedge \), such as \( p \wedge \neg q \wedge r \), or \( \neg q \) alone. (We do not shorten it to 'conjunct', which keeps its ordinary meaning, one side of a conjunction.)" Every later "conjunct(s)" that means a conjunctive clause becomes "conjunctive clause(s)", and every one that means a \( C_v \) becomes "minterm(s)", in prose, proofs, examples and exercise solutions: 07:53, 07:55, 07:56, 07:71, 07:93, 07:97, 07:109 (Idea of `thm-dnf`: "disjoin their minterms \( C_v \)"), 07:119, 07:121, 07:124 ("The minterms \( C_v \)"), 07:139, 07:143, 07:150-152 (inside the display), 07:158, 07:184 (minterm), 07:198, 07:201, 07:203, 07:207, 07:219 (`prp-cnf-validity` (b)), 07:236-243, 07:261, 07:305 (proof of `thm-adequate-connectives`: "the minterms \( C_{v} \)"; the one allowed change inside that otherwise verbatim proof, item 5), 07:359 (A1(b) prompt), 07:369, 07:373, 07:375, 07:395 ("three one-literal conjunctive clauses"), 07:397 ("This single conjunctive clause"), 07:430 (minterm), 07:434 ("each minterm is T in its own row only"), 07:436, 07:620 (minterms), and the in-file dependency ledger, 07:730 ("no DNF with fewer conjunctive clauses works | inline (a conjunctive clause missing an atom is true on two rows of different parity)"). Ledger comments are swept with the prose. The drafter greps `conjunct` after the sweep: every remaining hit is the ordinary sense, and the `eq-row-conjunct` label. At 07:76-84: "form the **minterm** of the row of \( v \), the conjunctive clause of its signed atoms," then \( C_v \coloneqq \dots \). Labels (`eq-row-conjunct`) do not change. "Term" is not introduced, so 07:7, 04:251 and `eq-many-term-values` keep their ordinary "terms".
3. 07:58 (nonexample by minimal change) kept: it is the section's one edge case of the definitions, and short. 07:126 (why not \( \bot \)) → fold F3.7-a.
4. 07:243 (the duality paragraph, "two faces of one fact") → fold F3.7-b.
5. **Before `thm-adequate-connectives`: "Rewriting 'or' with 'not' and 'and'"** (new, ~230 words, bold lead-in, placed after 07:289):
   "The DNF of a truth table uses \( \neg \), \( \wedge \) and \( \vee \). To do without \( \vee \), rewrite each disjunction by De Morgan's law: \( \alpha \vee \beta \) has the same table as \( \neg(\neg\alpha \wedge \neg\beta) \). Done everywhere, from the leaves up, this is a translation \( t_1 \) of the formulas built from atoms with \( \neg \), \( \wedge \), \( \vee \) (the proof below gives the clauses for \( \bot \), \( \to \), \( \leftrightarrow \)): \( t_1(p) = p \), \( t_1(\neg\alpha) = \neg t_1(\alpha) \), \( t_1(\alpha \wedge \beta) = t_1(\alpha) \wedge t_1(\beta) \), \( t_1(\alpha \vee \beta) = \neg(\neg t_1(\alpha) \wedge \neg t_1(\beta)) \). For instance
   \[ t_1\bigl( (p \vee q) \wedge \neg r \bigr) = \neg(\neg p \wedge \neg q) \wedge \neg r . \]
   In the row \( p = \mathrm{F} \), \( q = \mathrm{T} \), \( r = \mathrm{F} \) both sides are T: on the left \( p \vee q \) and \( \neg r \) are T; on the right \( \neg p \wedge \neg q \) is F, so its negation is T, and \( \neg r \) is T." Then the three translations side by side, in a table (rows \( \neg\alpha \), \( \alpha \wedge \beta \), \( \alpha \vee \beta \); columns \( t_1 \) into \( \{\neg, \wedge\} \), \( t_2 \) into \( \{\neg, \vee\} \), \( t_3 \) into \( \{\to, \bot\} \)), with entries copied from 07:309-311. Then the **Quick check 07:342-348 moves here**, before the theorem (unchanged; its \( t_3 \) clause is in the table). The theorem, Idea and proof 07:291-332 stay verbatim, except the one word at 07:305 ("conjuncts" → "minterms", item 2) (S2a items 7 and 16: the proof repeats the table's clauses, which is intended).
6. Everything else kept.

**Folds.** F3.7-a `title="Why not the constant for contradiction"` (no math in a fold title): 07:126. F3.7-b `title="Two faces of one fact"`: 07:243.

**Quick checks:** 07:66, the \( t_3 \) check (moved): two, in a second-pass section. Add none.

**Exercises.** A1, B1–B3, C1 (frozen), C2, R1–R3 kept, with "conjunctive clause" for "conjunct" in A1(b) (07:359, "a clause, a conjunctive clause, both, or neither") and its solutions 07:369, 07:373, 07:375, in B1's solutions 07:395, 07:397, and in B3's solution 07:430, 07:434 ("each minterm is T in its own row only"), 07:436; the in-file ledger line 07:730 likewise ("conjunctive clause(s)"). Old C3 → 3.6 (`exr-completeness-c3`). Old C4 → **C3** (`exr-normal-forms-c3`), `[C3: Exit check: normal forms]`, content unchanged except "conjuncts" → "minterms" at 07:620. The R group stays in this, the chapter's last section (STYLE §11.5), although the section is second pass. The index's reading path says nothing about R items, which review Chapters 1–2 and are on the full track.

**Sidecars:** the \( t_1 \) example row (extend `thm-adequate-connectives.py`).

---

## 5. Budgets and the Time line

| Section | Main line now (before Exercises) | Main-line budget | Folds | After the exercises |
|---|---|---|---|---|
| index | 665 | ≤ 1,100 | — | — |
| 3.1 | 4,821 | ≤ 4,400 | ≤ 650 | — |
| 3.2 | 6,187 | ≤ 4,900 | ≤ 2,300 | — |
| 3.3 | 3,555 | ≤ 3,400 | ≤ 300 | — |
| 3.4 | 4,299 | ≤ 4,500 | ≤ 400 | — |
| 3.5 | 4,963 | ≤ 3,800 | ≤ 550 | ≤ 1,000 (excursion) |
| 3.6 | 5,324 | ≤ 4,700 | ≤ 1,400 | — |
| 3.7 | 4,288 | ≤ 4,450 | ≤ 300 | — |
| total (3.1–3.7) | 33,437 | ≤ 30,150 | ≤ 5,900 | ≤ 1,000 |

The budgets are the S2 round-1 estimates: each moved, folded or cut block measured with `prose_words`, plus this file's own estimate of the new text (index: 665 + ~150 opening + ~140 "Where this goes" + ~120 reading path + ~95 chapter map + ~15 roadmap − ~80 trimmed ≈ 1,105, so the budget is ≤ 1,100; S2 round 2 raised it from ≤ 1,000, whose own estimate did not add up).

Every section stays under 5,000 main-line words. The whole-file advisory count of `check_structure.py` includes the exercises and will exceed 5,000 in 3.2, 3.5, 3.6 and 3.7. That count is advisory; the binding budget is the main line.

**Exercises after the revision.** 7 A1; 6 A2 drill banks with 46 parts, which count as about 12 exercises at one per four parts (STYLE §12.8); 19 B (none new); 18 C (new: 3.2 C4, a Challenge; 3.3 C1, new item; 3.4 C3, moved; 3.6 C3, moved and renamed); 3 R. Exit checks: 3.2 C3, 3.5 C2, 3.6 C2, 3.6 C3, and 3.7 C3 (now second pass).

**Time (B1 formula: 15 min per 400 main-line words; 20–45 min per exercise; a drill bank counts as one exercise per four parts).**
- **Core track** = the main lines of 3.1–3.6 (3.7 is second pass, §4.0 item 6), all of A, one B and one C per section of 3.1–3.6, and the exit checks of 3.1–3.6.
  - Reading: about 26,800 words (the index and the main lines of 3.1–3.6, at their budgets) ≈ 16.75 h.
  - Exercises: 6 A1 × 25 min; about 12 drill-bank exercises × 30 min; 6 B × 30 min; 6 C × 40 min, the C being the exit check where there is one; 3.6's second exit check, 40 min. That is ≈ 16.2 h.
  - Total ≈ 33.0 h, so "**About 33 hours on the core track** (Sections 3.1–3.6: all of A, one B and one C per section, the exit checks)". At the 20-minute floor for drills it would be about 31.0 h, so 33 is not shaded down.
- **Full track** = every main line, every fold and the excursion.
  - Reading: about 38,150 words (index 1,100, main lines 30,150, folds 5,900, excursion 1,000) ≈ 23.8 h.
  - Exercises: 7 A1 × 25 min; 12 × 30; 19 B × 30; 18 C × 40; 3 R × 40. That is ≈ 32.4 h.
  - Total ≈ 56.2 h, so "**about 56 hours for everything**".
- The plan's target of 25 core hours is not reached. The drafter recomputes from the delivered text by the same rule and does not shade the number down (STYLE §11.9). §4.0 fixes no figure in advance.

---

## 6. Edits needed outside Chapter 3

Section numbers do not change, so no "Section 3.x" sweep is needed. Every hand-written mention in fd1, fd2, fd3, fd4 and an1 found by the grep of 2026-10-12 was read against the new text (fd4's cite only `ax-induction` and `thm-strong-induction`, both verbatim on the main line, so none needs an edit):

| Where | Now says | Should read |
|---|---|---|
| fd1 ch04 01:25 ✱ | "Section 3.3 ended that warning with the remark that this chapter looks inside atoms." | "Section 3.3 closed with the remark that this chapter looks inside atoms." (The remark is now 3.3's Looking-ahead box, right after the warning.) |
| fd1 ch04 01:165, 02:431 | the display after @ax-induction used ∀ as an abbreviation of the words | unchanged (02:34 keeps "here \( \forall \) abbreviates the words") |
| fd1 ch04 02:31, 02:63, 02:77, 02:108, 02:116 | Section 3.1's alphabet, shorthand, parse trees | unchanged |
| fd1 ch04 02:266 | the substitution σ of Section 3.4 (@lem-substitution) | unchanged |
| fd1 ch04 05:17, 07:635 | grouped to the right, as in Section 3.4 | unchanged (04:244 kept) |
| fd1 ch04 11:154–178; ledger 11:701 | structural induction "as for @lem-coincidence"; "the cases not, or, ->, <-> repeat the conjunction argument" | unchanged: the main line now says exactly that, with the table, and the fold writes the cases out |
| fd1 ch04 12:11, 12:19, 12:21–23 | the thirteen primitive rules (Section 3.5); the context "(Section 3.5, before @lem-context-inclusion)"; "The proof of (b) in Section 3.5 is unchanged. It showed …" | unchanged (05:37, 05:43 stay on the main line; the proof of (b) is in fold F3.5-a, verbatim) |
| fd1 ch05 04:215 | "Self-explain the proof of @lem-atom-splitting in Section 3.6: … its five numbered steps … the paragraph that follows them" | unchanged (the proof stays on the main line, verbatim) |
| fd1 ch05 index:11 | "the proof of @lem-atom-splitting", "@thm-raa-independent" "for Section 5.7 only" | unchanged (the optional result still exists; it now sits in 3.5's excursion) |
| fd1 ch02 04:227, 05:37, 05:309 | Chapter 3 proves that ¬¬P ⊢ P needs RAA (@thm-raa-independent) | unchanged. Ch2's own revision (R3) decides how it words its forward pointers. |
| fd2 ch01 02:233, 02:256 | Chapter 3 described the formulas as the smallest collection of strings closed under (F1)–(F3) | unchanged (01:139's sentence kept) |
| fd2 ch02 01:79 | quotes 02:96 | unchanged (verbatim) |
| fd2 ch02 01:88 | the base case of the proof of @fd1:thm-strong-induction | unchanged (main line, verbatim) |
| fd2 ch02 02:7 | "Section 3.2, 'Starting from another number'" | unchanged (02:66 kept, same bold lead-in) |
| fd2 ch02 03:7; fd3 ch01 07:390 | structural recursion works because of unique readability | unchanged (statements and the idea on the main line; proofs in folds) |
| fd2 ch02 03:439, 02:253 | the warning after @fd1:exm-power-inequality on \( 2^n \ge n^2 \) | unchanged (the warning stays; only its last sentence, the pointer to fd2's own famous proof, moves to the index) |
| fd2 ch03 07:365–366 | "*Logic and Proof*, Section 3.2 (@fd1:ax-induction)", "(@fd1:thm-strong-induction)" | unchanged |
| fd3 ch01 03:3; an1 ch01 05:64 | Chapter 3 described ℕ as what we reach from 0 by adding 1, and took induction as basic | unchanged (02:42's first sentences kept) |

**Other files (coordinator):**
- `authoring/STATUS.md` promise rows: 79 (F1.3 §02, §03, §05 → F1.4) becomes "§02 Looking ahead (the rules for every and some), §03 Looking ahead (looking inside atoms), index 'Where this goes'; F1.4's soundness extension cites `lem-context-inclusion` (b) (§05)". 80 (RAA, F1.5) becomes "§05 Looking ahead". 81, 82, 83, 84 move their source from §01/§02 to "index, 'Where this goes'". Row 83's "(02:42 …)" goes, and row 84 keeps "AN1.1 (paid)". The F1.3 row of the chapter table records the R3 revision when it lands.
- `NOTATION.md`: §3.3 above.
- `fd1/authoring/ledger/ch03.yaml` and `fd1/verify/ch03/`: §3.3 above.

---

## 7. What stays exactly as it is

- The "first attempt fails" opening of 3.5 (05:5-31).
- "Reading a table off the rules" (03:7-45).
- "Working backwards from F" (`exm-backwards-from-f`, 03:311) and its reuse in 3.4–3.7.
- The two-follows table (04:363-377), now shown in the index as well.
- The gloss before every definition and the "In words" after it.
- The Idea boxes and Step roadmaps (05:133-143, 06:404-406; ③ reworded only to name the induction).
- The Try-it-first prompts (05:130, 07:223).
- The warnings built on minimal counterexamples: \( 2^n \ge n^2 \) at \( n = 3 \) (02:124); "every formula contains an atom" at \( \bot \) (02:236); replacement needs equivalence (04:306); a refuting row must make every premise true (05:293).
- The find-the-error items with true conclusions (3.2 C2, 3.3 C2) and every marking scheme.
- The honest length comparisons, 20 lines against 13 (06:510) and 21 against 3 (06:724).
- `exm-threes-and-fives`.
- The normal-forms opening that reuses the signed atoms (07:3, 07:124).
- The Catalan count (3.1 C1).
- The faded triple: `lem-coincidence` with every case proved on the main line; 3.3 B2; 3.4 C1.
- The proof-ordering item (3.5 B2).
- The exit checks (3.2 C3, 3.5 C2, 3.6 C2, the deciding-sequents check now 3.6 C3, the normal-forms check now 3.7 C3).
- The R group.
- Every statement of a labelled result, and every proof of a cited result, except the three rewordings with verbatim folds (S2a items 1–3), plus the "conjunct" sweep of §4.7 item 2 in 3.7 results cited only in-chapter (S2a item 7) and the spelling-only "non-empty" sweep (§1 item 9).

---

## 8. S2a: every new or changed claim that needs blueprint verification

**Changed wording or position of cited results (check every later citation still holds):**
1. `lem-coincidence`: the ∨, →, ↔ cases as a table (§4.3 item 5), with the verbatim cases in fold F3.3-b. Is the table proof complete and equivalent? Check fd1 ch04 11:168 ("as for @lem-coincidence") and its ledger line 11:701.
2. `thm-completeness`: 06:445 replaced by the descent sentence (§4.6 item 6), 06:445 verbatim in fold F3.6-d; the Idea's ③ reworded. Is the main-line proof still complete with the fold closed? (The sentence names the induction; the fold carries it out.) Check fd2's three citations and fd1 ch05 07:27.
3. `exm-completeness-run` moved before the proof, with "Step 2"/"Step 3" → the roadmap's ②/③, its statement's "Run the proof of" → "Run the roadmap of", and 06:454's "run the proof" → "run the method of the roadmap". Is every reference it makes defined at its new place (the roadmap, `lem-truth-table-line`, `lem-atom-splitting`, `lem-connective-rows`, all earlier)?
4. `def-height` moved verbatim to 3.2 after the one-parse-tree argument; 01:264 with it; 01:266 cut; F3.2-d's copy of 02:342 loses "and the height of @def-height is a well-defined number". Check every use of height now comes after it: 3.2 drill (f), (g), `exm-recursive-definitions`, 02:418 (reworded opening), B3, the remark in F3.2-b (reworded, with a one-line gloss of height and no `@def-height`), and in 3.1 nothing: A1 (b), (c), B1, the Quick check 01:268 and the C1 solution 01:523 (reworded with "a chain of two arrows", "one-arrow trees") no longer mention height. Check that the ledger line for `def-height` moved from 01:539 to 02, and 03:564 to 02 (§4.2).
5. The F3.2-b remark (02:231-233) reworded: "the height is read off the parse tree, and that a formula has only one parse tree is proved below from unique readability, whose proof uses structural induction". Is it still true and non-circular as stated?
6. `exm-formation-sequences`: fourth string \( (\neg p \vee (q \to \bot)) \) and its six-entry sequence; the adjusted opening of 01:94 in fold F3.1-a (listing \( q \) before \( p \) in that sequence still gives a formation sequence).
7. 3.7: "conjunct" → "conjunctive clause", \( C_v \) the "minterm", in the statement of `prp-cnf-validity` (b), the proofs of `thm-dnf`, `thm-cnf`, `prp-cnf-validity` and `thm-adequate-connectives` (07:305 only, one word, in an otherwise verbatim proof), the Idea of `thm-dnf` (07:109), the exercise solutions (07:369-375, 07:395, 07:397, 07:430, 07:434, 07:436, 07:620), the in-file ledger line 07:730, and the prose. Is the sweep complete, and is every remaining "conjunct" the ordinary sense?
8. `exr-entailment-and-equivalence-c3`: (I) restated as "if \( \Gamma, \varphi \models \psi \), then \( \Gamma \models \varphi \to \psi \), with ⊨ read with the table \( t \)". Is it equivalent to old (I)? Is the solution, with the two reworded sentences, still correct and non-circular?

**New claims and examples in the main text:**
9. Index: the four-row table, and the claim that row F, T makes \( p \to q \) true and \( q \to p \) false; the chapter map's last row; the reading path's claims: "nothing in Chapters 4 and 5 uses 3.7" (grep: no `@` citation of a §07 label in fd1 Ch4–5), and "every A and B exercise can be done with the folds closed" (check each A and B item of 3.1–3.6 against §4); the "Where this goes" note matches what the named volumes contain (STATUS rows 79–84).
10. 3.1: the letter box (each row's "inside a formula?" answer); the build-up figure (entries, arrows, labels); the two new Quick checks; "the smallest collection" sentence without its pointer.
11. 3.2: the hook (values of the two readings at \( p = q = \mathrm{F} \), \( r = \mathrm{T} \)); the depth figure (every depth value), and the claim that its three features are the three parts of `lem-parenthesis-count` (part (c) together with 02:303 for "only binary connective at depth 1"); the sentence "the depth of a symbol is the excess of the initial segment ending just before it"; the two Quick checks (\( 5^{n+1} - 1 = 5(5^n - 1) + 4 \); depths of \( (p \wedge (q \vee r)) \)); the check-mark figure (reasons and sources); the reworded 02:13, 02:34, 02:42, 02:64, 02:348 (no claim lost that a proof uses; fd1 ch04 01:165 and 02:431 still true).
12. 3.3: the valuation sentence; the trimmed "Well defined" paragraph; the new Quick check (\( v(\neg p \vee (q \leftrightarrow \bot)) = \mathrm{T} \)); the Looking-ahead box replacing the warning's last sentence.
13. 3.4: the three-operations box (each "what it keeps" claim, each example); the two new Quick checks; `exm-substitution-in-one-row` (every value, \( w \), and agreement); the reworded warning 04:129.
14. 3.5: the picture for `lem-context-inclusion` (b) (labels match the lemma); the two new Quick checks; the 3×3 and 3×1 tables against 05:315-321; the italic optional line; the trimmed 05:356; the placement after the exercises (or the fallback fold).
15. 3.6: the paste (\( D \), \( E \), \( F \) are derivations, and \( F \) is what the construction of (∗) builds); the tagged tables (every tag matches `lem-connective-rows` and the case choices of `lem-truth-table-line`'s proof, including \( (\wedge 2) \) for F, F, \( (\vee 1) \) for T, T and T, F, and \( ({\to}1) \) for F, T); the signed-row display; the superscript sentence; the tree beside the 20-line derivation (every line range and rule); the two new Quick checks.
16. 3.7: the \( t_1 \) example and its row check; the translation table copied from 07:309-311; the moved Quick check.

**New and changed exercise answers:**
17. 3.1 A1 (b), (c); A2 (a)–(h); B1 without height; C1's solution 01:523 without height.
18. 3.2 A1 (c), (d); A2 (a)–(h); C4 (old A1 (c)–(e), verbatim).
19. 3.3 A2 (a)–(h); C1 (the parity item, (a) and (b), hints, marking scheme).
20. 3.4 A2 (a)–(h); C3 (item 8).
21. 3.5 A2 (a)–(h).
22. 3.6 A2 (a)–(f); B2's tree (line ranges against the 21-line derivation); C3 (moved, unchanged).
23. 3.7 C3 (renamed, "minterms" at 07:620); A1 (b), B1 and B3 with "conjunctive clause".

**Routes to confirm do not rest on removed or folded material:** no main-line proof cites a step that now exists only in a fold, except as a cited, stated result (`lem-parenthesis-count`, `thm-unique-readability`, `thm-structural-recursion`, `lem-replacement`, `lem-context-inclusion`, `lem-weakening-cut`, `lem-connective-rows`, all with their statements on the main line). The cut forward pointers carried no argument: 02:42's "Nothing in this book depends on those two routes" goes with them.

---

## 9. S2 replies (round 1)

All findings applied. Three notes on how:
- **"Term".** Of the two fixes offered, the free word was chosen: "conjunctive clause" (the existing gloss of 07:33) and "minterm" for \( C_v \), recorded as a deviation from the plan in §1 item 8. Keeping "term" would have left a clash with Chapter 4's `def-term` and with the verbatim "terms" of 02:80-96 that fd2 quotes.
- **fd4 citations.** Recorded as a note above the §3.1 table rather than a new column, since only two rows would carry an entry; rule 1 and §6 now name fd4.
- **Duplicates.** The two findings on 3.1 C1's height (01:523), the two on the `thm-adequate-connectives` proof and 07:109/395/397, and the two on F3.1-a's placement were each applied once.

## 10. S2 replies (round 2)

All three findings applied.
- **Index budget.** The estimate sums to ≈ 1,105, so the index budget is raised to ≤ 1,100 (§5 table and note; §1 item 3 now names it) rather than trimming the story or the "Where this goes" note, both already at their minimum for the content they carry. Core reading ≈ 26,800 words ≈ 16.75 h, core total ≈ 33.0 h (still "about 33"); full reading ≈ 38,150 words, full total still ≈ 56 h.
- **"Conjunct" sweep.** 07:434 ("each minterm is T in its own row only") added to §4.7 item 2, the Exercises paragraph and S2a item 7; ledger comments are swept, with 07:730 named.
- **`def-height` ledger line.** The last clause of 01:539 is dropped, and 02's full replacement line is given (§4.1).
